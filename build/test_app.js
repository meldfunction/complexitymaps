// Headless test of dist/index.html with a mocked worker feed (never the real data).
const { chromium } = require('playwright');
const path = require('path');
const FILE = 'file://' + path.resolve(__dirname, '../dist/index.html');
const MOCK = {resources:[
  {name:"Mock: Dialogue primer",url:"https://example.org/a",desc:"About Bohm dialogue and thinking together.",types:["Books"],caps:["Observing & Listening"],featured:true},
  {name:"Mock: Policy lab guide",url:"https://example.org/b",desc:"Public sector innovation labs and government policy.",types:["Methods & Toolkits"],caps:["Advocacy & Political Participation"],featured:false},
  {name:"Mock: Power mapping",url:"javascript:alert(1)",desc:"Power analysis <img src=x onerror=alert(1)>.",types:["Methods & Toolkits"],caps:["Positionality & Power Analysis"],featured:false}]};
(async () => {
  const b = await chromium.launch(); let fails = 0;
  const check = (ok, msg) => { console.log((ok ? "PASS " : "FAIL ") + msg); if (!ok) fails++; };
  for (const mode of ['live','down']) {
    const p = await b.newPage({viewport:{width:1280,height:900}});
    const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('dialog',d=>{errs.push('dialog '+d.message()); d.dismiss();});
    const posts=[], gets=[]; p.on('request', r => { if (r.url().includes('workers.dev')) (r.method()==='GET' ? gets : posts).push(r.method()); });
    await p.route('https://fonts.googleapis.com/**', r=>r.abort());
    await p.route('https://capacities.jayajohnyramchandani.workers.dev/**', r => mode==='down' ? r.abort() :
      r.fulfill({status:200, headers:{'content-type':'application/json','access-control-allow-origin':'*'}, body: JSON.stringify(MOCK)}));
    await p.goto(FILE + '#p-power-analysis'); await p.waitForTimeout(900);
    check(gets.length === 0, `[${mode}] no request to the worker on page load`);
    check((await p.textContent('#status-text')).includes('loads when you ask'), `[${mode}] idle status on load`);
    for (const h of ['#orgs','#o-hls','#cases','#journeys','#p-bohm-dialogue','#p-power-analysis']) { await p.evaluate(x => location.hash = x, h); await p.waitForTimeout(120); }
    check(gets.length === 0, `[${mode}] browsing pathways, profiles, and cases makes no request`);
    await p.click('button.loadbtn'); await p.waitForTimeout(700);
    check(gets.length === 1, `[${mode}] tapping Load makes exactly one request (${gets.length})`);
    const st = await p.textContent('#status-text');
    check(mode==='live' ? st.includes('3 resources') : st.includes('unreachable'), `[${mode}] status: ${st.trim()}`);
    check(await p.textContent('h3.title') === 'Power analysis', `[${mode}] pathway route renders`);
    check(await p.locator('nav.index .pw').count() === 48, `[${mode}] index lists 48 pathways`);
    if (mode==='live') {
      const t = await p.locator('main .r .t').filter({hasText:'Mock: Power mapping'}).first().evaluate(n => n.tagName + ':' + (n.getAttribute('href')||'none'));
      check(t === 'SPAN:none', 'javascript: URL is not rendered as a link');
      check(await p.locator('main img').count() === 0, 'injected HTML is not rendered');
    }
    for (const [hash, sel, min, label] of [['#orgs','.grid .r',60,'org list'],['#o-bateson-institute','.media li',3,'org profile media'],
        ['#cases','.grid .r',16,'case list'],['#c-porto-alegre','dd .links a',3,'case sources'],['#journeys','.stage',6,'journey stages'],
        ['#orientations','.orient .r',7,'orientations'],['#levels','.levels tr',7,'levels table'],['#library','#lq',1,'library search']]) {
      await p.evaluate(h => location.hash = h, hash); await p.waitForTimeout(250);
      check(await p.locator(sel).count() >= min, `[${mode}] ${label}`);
    }
    await p.evaluate(() => location.hash = '#p-bohm-dialogue'); await p.waitForTimeout(250);
    await p.click('button.chip:has-text("Practice")'); await p.waitForTimeout(200);
    check(await p.locator('nav.index .pw').count() === await p.evaluate(() => DATA.pathways.filter(x=>x.kind==='Practice').length), `[${mode}] kind filter`);
    await p.fill('#pq','grief'); await p.waitForTimeout(200);
    check(await p.evaluate(() => document.activeElement.id) === 'pq', `[${mode}] filter keeps focus while typing`);
    await p.setViewportSize({width:390,height:844}); await p.waitForTimeout(200);
    for (const h of ['#p-crisis-disaster-and-high-reliability','#o-hls','#levels','#journeys']) {
      await p.evaluate(x => location.hash = x, h); await p.waitForTimeout(200);
      const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
      check(ov <= 0, `[${mode}] no sideways scroll at 390px on ${h} (${ov})`);
    }
    if (mode==='live') { await p.evaluate(x => location.hash = x, '#p-crisis-disaster-and-high-reliability'); await p.waitForTimeout(200);
      await p.screenshot({path: path.resolve(__dirname,'../dist/_shot-mobile.png')});
      await p.setViewportSize({width:1280,height:900}); await p.evaluate(x => location.hash = x, '#p-government-plumbing'); await p.waitForTimeout(250);
      await p.screenshot({path: path.resolve(__dirname,'../dist/_shot-desktop.png')});
      await p.evaluate(x => location.hash = x, '#o-nesta'); await p.waitForTimeout(250);
      await p.screenshot({path: path.resolve(__dirname,'../dist/_shot-org.png')}); }
    check(posts.length === 0, `[${mode}] app never POSTs to the worker`);
    if (mode==='live') check(gets.length === 1, `[${mode}] still one request after browsing everything (${gets.length})`);
    // A fresh visitor who opens the Live library tab triggers the load by opening it.
    const q = await b.newPage(); const g2=[]; q.on('request', r => { if (r.url().includes('workers.dev')) g2.push(1); });
    await q.route('https://fonts.googleapis.com/**', r=>r.abort());
    await q.route('https://capacities.jayajohnyramchandani.workers.dev/**', r => mode==='down' ? r.abort() :
      r.fulfill({status:200, headers:{'content-type':'application/json'}, body: JSON.stringify(MOCK)}));
    await q.goto(FILE + '#library'); await q.waitForTimeout(700);
    check(g2.length === 1, `[${mode}] opening the Live library tab triggers one request`);
    if (mode==='live') check(await q.locator('.grid .r').count() === 3, `[${mode}] library shows results after the triggered load`);
    await q.close();
    check(errs.length === 0, `[${mode}] no page errors ${errs.join(' | ')}`);
    await p.close();
  }
  await b.close(); console.log(fails ? `${fails} FAILED` : 'ALL PASSED'); process.exit(fails ? 1 : 0);
})();
