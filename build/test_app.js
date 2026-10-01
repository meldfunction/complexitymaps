// Headless test of dist/index.html with a mocked worker feed (never the real data).
const { chromium } = require('playwright');
const path = require('path');
const FILE = 'file://' + path.resolve(__dirname, '../dist/index.html');
const MOCK = {resources:[
  {name:"Mock: Dialogue primer",url:"https://example.org/a",desc:"About Bohm dialogue and thinking together.",types:["Books"],caps:["Observing & Listening"],featured:true},
  {name:"Mock: Policy lab guide",url:"https://example.org/b",desc:"Public sector innovation labs and government policy.",types:["Methods & Toolkits"],caps:["Advocacy & Political Participation"],featured:false},
  {name:"Mock: Power mapping",url:"javascript:alert(1)",desc:"Power analysis <img src=x onerror=alert(1)>.",types:["Methods & Toolkits"],caps:["Positionality & Power Analysis"],featured:false}]};
const go = (p, h) => p.evaluate(x => location.hash = x, h).then(() => p.waitForTimeout(150));
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
    await p.goto(FILE + '#/wiki/power-analysis'); await p.waitForTimeout(700);
    check(gets.length === 0, `[${mode}] no request to the worker on page load`);
    check((await p.textContent('#status-text')).includes('loads when you ask'), `[${mode}] idle status on load`);
    check(await p.textContent('h1.art-title') === 'Power analysis', `[${mode}] wiki article renders`);
    for (const h of ['#/','#/wiki','#/path','#/map','#/map?view=metro','#/map?view=tree&p=bohm-dialogue','#/map?view=treemap','#/map?view=mine','#/map?view=time','#/map?view=universe&links=shared','#/map?view=universe&zoom=found&links=shared',
        '#/people/nora-bateson','#/contribute','#/about','#/about/acknowledgment','#/orgs','#/orgs/hls','#/cases','#/cases/porto-alegre']) await go(p, h);
    check(gets.length === 0, `[${mode}] browsing every route makes no request`);
    if (mode === 'live') {
      await go(p, '#/map?view=universe'); check(await p.locator('.stage .conn').count() === 0, '[live] universe shows no connection lines by default');
      await p.click('.linktoggle a:has-text("Neighbours")'); await p.waitForTimeout(300);
      const near = await p.locator('.stage .conn').count(); check(near > 20, `[live] neighbours toggle draws lines (${near})`);
      check(p.url().includes('links=near'), '[live] connections toggle is deep-linkable');
      await go(p, '#/map?view=universe&links=shared&p=sensemaking-and-acting-in-uncertainty');
      check(await p.locator('.stage .conn.on').count() >= 1, '[live] selected pathway highlights its own connections');
      check(await p.locator('.connlist li').count() >= 1, '[live] side panel lists what the pathway connects to and why');
      await go(p, '#/');
      check(await p.locator('#how .visit').count() === 3, '[live] home shows how to use the site: three kinds of visit');
      check(await p.locator('#how .visit a.btn').evaluateAll(a => a.map(x => x.getAttribute('href')).join()) === '#/wiki,#/path,#/map', '[live] each visit ends in a clear call to action');
      await go(p, '#/people/nora-bateson');
      check((await p.textContent('.q .qwhat')).includes('Stage theories say'), '[live] critique explains what is being questioned');
    }
    await go(p, '#/wiki/power-analysis');
    await p.click('button.loadbtn'); await p.waitForTimeout(700);
    check(gets.length === 1, `[${mode}] tapping Load makes exactly one request (${gets.length})`);
    const st = await p.textContent('#status-text');
    check(mode==='live' ? st.includes('3 resources') : st.includes('unreachable'), `[${mode}] status: ${st.trim()}`);
    if (mode==='live') {
      const t = await p.locator('#main .r').filter({hasText:'Mock: Power mapping'}).first().evaluate(n => { const a = n.querySelector('.t'); return a.tagName + ':' + (a.getAttribute('href')||'none'); });
      check(t === 'SPAN:none', 'javascript: URL is not rendered as a link');
      check(await p.locator('#main img').count() === 0, 'injected HTML is not rendered');
    }
    for (const [hash, sel, min, label] of [
        ['#/', '.door', 5, 'home doors'], ['#/', '.goal', 7, 'home goals'],
        ['#/wiki', '.idx .cl a', 50, 'wiki index lists 50 pathways'], ['#/wiki?goal=power', '.idx .cl a', 3, 'goal filter'],
        ['#/wiki/sensemaking-and-acting-in-uncertainty', '.road li', 5, 'article road'], ['#/wiki/sensemaking-and-acting-in-uncertainty', '.localmap .node', 6, 'article local map'],
        ['#/path?start=want', '.branch', 7, 'path areas'], ['#/path?start=want&area=care&trade=teach', '.branch', 3, 'path pathways'],
        ['#/path?start=want&area=care&trade=teach&p=experiential-learning-and-reflective-practice', '.where .card', 3, 'where this work happens'],
        ['#/map', '.stage .hit', 48, 'universe stars'], ['#/map?view=metro', '.stage .hit', 20, 'metro stops'], ['#/map?view=tree&p=power-analysis', '.stop', 2, 'tree stops'],
        ['#/map?view=treemap', '.tm button', 48, 'treemap tiles'], ['#/map?view=time', '.time .bar', 50, 'timeline bars'],
        ['#/people/nora-bateson', '.q', 2, 'profile critiques'], ['#/people/karl-weick', '.appears div', 1, 'stub profile'],
        ['#/contribute?on=X&kind=fact&sec=Cases', 'a.btn[href*="github.com"]', 1, 'contribute opens a prefilled issue'],
        ['#/about', '.orient .tile', 7, 'orientations'], ['#/orgs', '.grid .r', 60, 'org list'], ['#/orgs/bateson-institute', '.media li', 3, 'org media'],
        ['#/cases', '.grid .r', 30, 'case list'], ['#/cases/porto-alegre', '.links a', 3, 'case sources'], ['#/library', '#lq', 1, 'library search'],
        ['#p-bohm-dialogue', 'h1.art-title', 1, 'old #p- links still work'], ['#o-hls', 'h1', 1, 'old #o- links still work']]) {
      await go(p, hash); await p.waitForTimeout(100);
      check(await p.locator(sel).count() >= min, `[${mode}] ${label}`);
    }
    await go(p, '#/map?view=tree&p=bohm-dialogue');
    check(await p.evaluate(() => document.querySelector('.hub h2').textContent) === 'Bohm Dialogue', `[${mode}] deep link restores the map view and pathway`);
    await p.evaluate(() => localStorage.removeItem('pathways-my-trail'));
    await go(p, '#/wiki/power-analysis'); await p.click('button:has-text("Add to my trail")'); await p.waitForTimeout(150);
    check(await p.evaluate(() => JSON.parse(localStorage.getItem('pathways-my-trail'))[0]) === 'power-analysis', `[${mode}] add to my trail stays in localStorage`);
    await go(p, '#/wiki'); await p.fill('#pq','grief'); await p.waitForTimeout(150);
    check(await p.evaluate(() => document.activeElement.id) === 'pq', `[${mode}] filter keeps focus while typing`);
    await p.setViewportSize({width:360,height:800}); await p.waitForTimeout(150);
    for (const h of ['#/','#/wiki/crisis-disaster-and-high-reliability','#/path?start=now','#/path?start=want&area=care&trade=teach&p=experiential-learning-and-reflective-practice',
        '#/map','#/map?view=universe&links=shared&p=power-analysis','#/map?view=metro','#/map?view=tree&p=power-analysis','#/map?view=treemap','#/map?view=mine','#/map?view=time','#/people/nora-bateson','#/contribute','#/about','#/about/acknowledgment','#/orgs/hls','#/cases']) {
      await go(p, h);
      const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
      check(ov <= 0, `[${mode}] no sideways scroll at 360px on ${h} (${ov})`);
    }
    if (mode==='live') { await go(p, '#/wiki/crisis-disaster-and-high-reliability');
      await p.screenshot({path: path.resolve(__dirname,'../dist/_shot-mobile.png')});
      await p.setViewportSize({width:1280,height:900}); await go(p, '#/');
      await p.screenshot({path: path.resolve(__dirname,'../dist/_shot-desktop.png')}); }
    check(posts.length === 0, `[${mode}] app never POSTs to the worker`);
    if (mode==='live') check(gets.length === 1, `[${mode}] still one request after browsing everything (${gets.length})`);
    // A fresh visitor who opens the Live library page triggers the load by opening it.
    const q = await b.newPage(); const g2=[]; q.on('request', r => { if (r.url().includes('workers.dev')) g2.push(1); });
    await q.route('https://fonts.googleapis.com/**', r=>r.abort());
    await q.route('https://capacities.jayajohnyramchandani.workers.dev/**', r => mode==='down' ? r.abort() :
      r.fulfill({status:200, headers:{'content-type':'application/json'}, body: JSON.stringify(MOCK)}));
    await q.goto(FILE + '#/library'); await q.waitForTimeout(700);
    check(g2.length === 1, `[${mode}] opening the Live library page triggers one request`);
    if (mode==='live') check(await q.locator('.grid .r').count() === 3, `[${mode}] library shows results after the triggered load`);
    await q.close();
    if (mode==='live') {
      // motion: Anime.js loads beside the page; animations run, and every view also works with motion off
      await p.setViewportSize({width:1280,height:900}); await go(p, '#/'); await p.waitForTimeout(300);
      check(await p.evaluate(() => !!(window.anime && window.anime.animate)), 'motion: Anime.js loaded from dist');
      check(await p.evaluate(() => { const i = document.querySelector('.photo img'); return i.complete && i.naturalWidth > 0; }), 'home photo loads');
      await p.click('.concepts .iacts button'); await p.waitForTimeout(3600);
      check(await p.evaluate(() => document.querySelectorAll('.concepts .lnode.moved').length) === 4, 'motion: feedback loop runs to the end');
      const n = await p.locator('.concepts .ipick button').count();
      for (let i = 0; i < n; i++) { await p.locator('.concepts .ipick button').nth(i).click(); await p.waitForTimeout(700); }
      check(n >= 8 && (await p.textContent('.concepts h3')) === "Goodhart's law", `motion: carousel shows all ${n} ideas`);
      await p.click('.concepts .nav[aria-label="Next idea"]'); await p.waitForTimeout(200);
      check((await p.textContent('.concepts h3')) === 'Feedback loops', 'carousel wraps around');
      await go(p, '#/map?view=time'); await p.locator('.scrub input').fill('1950'); await p.waitForTimeout(150);
      check(/alive or active in 1950/.test(await p.textContent('.together')), 'motion: year scrubber lists who was alive');
      await p.evaluate(() => localStorage.setItem('pathways-my-trail', JSON.stringify(['power-analysis','service-design'])));
      await go(p, '#/map?view=mine'); await p.click('.reorder li:nth-child(1) button[aria-label*="later"]'); await p.waitForTimeout(150);
      check(await p.evaluate(() => JSON.parse(localStorage.getItem('pathways-my-trail'))[0]) === 'service-design', 'motion: reorder buttons move a stop');
      await go(p, '#/wiki'); await p.click('.helpfab'); await p.waitForTimeout(300);
      check(await p.evaluate(() => document.querySelector('dialog.helpdlg')?.open === true), 'wiki: Need help opens the guide');
      await p.click('.helpways .way >> nth=0'); await p.waitForTimeout(200);
      for (let i = 0; i < 9; i++) { await p.click('.tnav .btn:not(.ghost)'); await p.waitForTimeout(120); }
      check((await p.textContent('.tcard .label')).startsWith('Stop 10 of 10'), 'wiki: history tour reaches the last stop');
      await p.keyboard.press('Escape'); await p.waitForTimeout(150);
      check(await p.evaluate(() => !document.querySelector('dialog.helpdlg') && !document.querySelector('.helpfab.pulse')), 'wiki: guide closes and the button stops pulsing');
      await go(p, '#/'); await p.click('.motiontoggle'); await p.waitForTimeout(150);
      check((await p.textContent('.motiontoggle')).includes('off'), 'motion: footer toggle turns motion off');
      await go(p, '#/map?view=metro'); await p.waitForTimeout(300);
      check(await p.evaluate(() => document.querySelector('.mline').getAttribute('stroke-dasharray')) === null, 'motion off: metro lines are drawn in full at once');
      await p.evaluate(() => localStorage.removeItem('pathways-motion'));
      // motion on, never scrolled (full-page screenshots, link previews): the road must still be visible
      const sc = await b.newContext({viewport:{width:1280,height:700}}); const sp = await sc.newPage();
      await sp.route('https://fonts.googleapis.com/**', x=>x.abort());
      await sp.goto(FILE + '#/wiki/biosemiotics-and-the-umwelt'); await sp.waitForTimeout(1200);
      check(await sp.evaluate(() => [...document.querySelectorAll('.road li')].every(l => getComputedStyle(l).opacity === '1')), 'motion: road names show without scrolling');
      await sp.evaluate(() => window.scrollTo(0, document.querySelector('.road').getBoundingClientRect().top + scrollY - 200)); await sp.waitForTimeout(1500);
      check(await sp.evaluate(() => [...document.querySelectorAll('.road li')].every(l => getComputedStyle(l).opacity === '1')), 'motion: road names show after scrolling to them');
      await sc.close();
      const rc = await b.newContext({reducedMotion:'reduce'}); const r = await rc.newPage(); const rerr = []; r.on('pageerror', e => rerr.push(e.message));
      await r.route('https://fonts.googleapis.com/**', x=>x.abort());
      await r.goto(FILE + '#/wiki/power-analysis'); await r.waitForTimeout(500);
      await r.evaluate(() => document.querySelector('.road').scrollIntoView()); await r.waitForTimeout(100);
      check(await r.evaluate(() => getComputedStyle(document.querySelector('.road li')).opacity) === '1' && (await r.textContent('.motiontoggle')).includes('reduced'), 'reduced motion: road shows at once, toggle says why');
      check(rerr.length === 0, 'reduced motion: no page errors'); await rc.close();
    }
    check(errs.length === 0, `[${mode}] no page errors ${errs.join(' | ')}`);
    await p.close();
  }
  await b.close(); console.log(fails ? `${fails} FAILED` : 'ALL PASSED'); process.exit(fails ? 1 : 0);
})();
