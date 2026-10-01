"""Build dist/complexity-pathways.pdf from data/site-data.json.

Run: python3 build/build_pdf.py
"""
import json, pathlib, re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether,
                                HRFlowable, PageBreak)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from xml.sax.saxutils import escape

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = json.load(open(ROOT / "data" / "site-data.json"))

F = "/usr/share/fonts/truetype/dejavu/"
for n, f in (("DV", "DejaVuSans.ttf"), ("DVB", "DejaVuSans-Bold.ttf"), ("DVI", "DejaVuSans-Oblique.ttf"), ("DVBI", "DejaVuSans-BoldOblique.ttf")):
    pdfmetrics.registerFont(TTFont(n, F + f))
addMapping("DV", 0, 0, "DV"); addMapping("DV", 1, 0, "DVB"); addMapping("DV", 0, 1, "DVI"); addMapping("DV", 1, 1, "DVBI")

INK, ACC, GOLD, LINK = colors.HexColor("#1f2a2e"), colors.HexColor("#2f6f62"), colors.HexColor("#9a6a17"), "#1b5e9e"
S = lambda name, **kw: ParagraphStyle(name, **{"fontName": "DV", "fontSize": 9.5, "leading": 13.5, "textColor": INK, **kw})
title = S("t", fontName="DVB", fontSize=22, leading=26, spaceAfter=4)
sub = S("s", fontSize=10.5, leading=14, textColor=colors.HexColor("#555555"), spaceAfter=10)
sec = S("sec", fontName="DVB", fontSize=15, leading=19, spaceBefore=14, spaceAfter=2)
h = S("h", fontName="DVB", fontSize=12.5, leading=16, spaceBefore=12, spaceAfter=3)
over = S("o", fontName="DVI", spaceAfter=4)
body = S("b", spaceAfter=3)
small = S("sm", fontSize=8.5, leading=12, textColor=colors.HexColor("#444444"), spaceAfter=2)

def txt(s):  # escape, but keep our own <i> title markup
    return re.sub(r"&lt;(/?)i&gt;", r"<\1i>", escape(s))
def L(t, u): return f'<a href="{escape(u)}" color="{LINK}"><u>{escape(t)}</u></a>'
def callout(html, bg="#eef4f2", bar=ACC):
    t = Table([[Paragraph(html, body)]], colWidths=[6.7 * inch])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg)), ("LINEBEFORE", (0, 0), (0, -1), 3, bar),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    return t
def section(name, color=ACC):
    return [Paragraph(escape(name), sec), HRFlowable(width="100%", thickness=1, color=color, spaceAfter=4)]

P = {p["id"]: p for p in D["pathways"]}
O = {o["id"]: o for o in D["orgs"]}
C = {c["id"]: c for c in D["cases"]}
ccolor = {c["name"]: colors.HexColor(c["light"]) for c in D["clusters"]}

story = [Paragraph("Pathways into Complexity", title), Paragraph(escape(D["about"]["lede"]), sub),
         callout("<b>How to read this.</b> Each pathway opens with a one-line view of the space and its <b>kind</b> "
                 "(lineage, practice, method, structure, field, tradition, or hybrid). <b>Road</b> is the lineage in rough order. "
                 "<b>Mix in</b> adds adjacent voices. <b>Policy lens</b> shows how it applies to public policy and government innovation. "
                 "<b>Engage</b> links to living communities, <b>Go deeper</b> names organization profiles, and <b>Cases</b> point to real situations. "
                 "The companion app adds live resources from the Systems Change Learning Guide."),
         Spacer(1, 6)]

story += section("Orientations")
story.append(Paragraph("Our orientations, each drawn from a lineage on this map. Use them as questions at hard junctions, not as badges.", body))
for o in D["orientations"]:
    story.append(KeepTogether([Paragraph(f"<b>{escape(o['name'])}.</b> {escape(o['line'])}", body),
                               Paragraph(f"<i>Ask: {escape(o['ask'])}</i> From {escape(o['source'])}.", small), Spacer(1, 3)]))

story += section("Kinds of path")
kt = Table([[Paragraph(f"<b>{escape(k['name'])}</b>", body), Paragraph(escape(k["desc"]), body)] for k in D["kinds"]], colWidths=[1.2 * inch, 5.5 * inch])
kt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), 0.5, colors.HexColor("#d5dedb")),
                        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
story.append(kt)

for c in D["clusters"]:
    ps = [p for p in D["pathways"] if p["cluster"] == c["name"]]
    if not ps: continue
    story.append(PageBreak() if c is D["clusters"][0] else Spacer(1, 4))
    story += section(c["name"], ccolor[c["name"]])
    for p in ps:
        hs = S("h_" + p["id"], parent=h, textColor=ccolor[p["cluster"]])
        block = [Paragraph(f"{escape(p['name'])}  <font size=8.5 color='#666666'>{escape(p['kind'])}</font>", hs),
                 Paragraph(txt(p["overview"]), over),
                 Paragraph(f"<b>Road:</b> {txt(p['road'])}", body),
                 Paragraph(f"<b>Mix in:</b> {txt(p['mix'])}", body)]
        if p["policy"]:
            block.append(Paragraph(f'<font color="#9a6a17"><b>Policy lens:</b></font> {escape(p["policy"])}', body))
        block.append(Paragraph("<b>Engage:</b> " + (" · ".join(L(l["t"], l["u"]) for l in p["links"]) or "practiced widely, with no single home"), body))
        if p["orgs"]:
            block.append(Paragraph("<b>Go deeper:</b> " + " · ".join(L(O[i]["name"], O[i]["url"]) for i in p["orgs"]), body))
        if p.get("reading"):
            block.append(Paragraph("<b>Read and watch:</b> " + " · ".join(L(m["title"], m["u"]) for m in p["reading"]), body))
        if p["cases"]:
            block.append(Paragraph("<b>Cases:</b> " + " · ".join(escape(C[i]["title"]) for i in p["cases"]) + " (see Cases)", body))
        story.append(KeepTogether(block))

story.append(PageBreak())
story += section("Cases")
story.append(callout("Real situations where a pathway met the world. Each names its limits or later reversals, because the learning is in both."))
for cs in D["cases"]:
    blk = [Paragraph(f"{escape(cs['title'])}  <font size=8.5 color='#666666'>{escape(cs['place'])} · {escape(cs['years'])}</font>", h),
           Paragraph(escape(cs["summary"]), body), Paragraph(f"<b>Lesson:</b> {escape(cs['lesson'])}", body)]
    if cs["note"]: blk.append(Paragraph(f"<b>Limits:</b> {escape(cs['note'])}", body))
    blk.append(Paragraph("<b>Pathways:</b> " + ", ".join(escape(P[i]["name"]) for i in cs["pathways"]), small))
    blk.append(Paragraph("<b>Sources:</b> " + " · ".join(L(s["t"], s["u"]) for s in cs["sources"]), small))
    story.append(KeepTogether(blk))

story.append(PageBreak())
story += section("Organization profiles")
story.append(callout("Organizations carrying the work, each with public articles, talks, podcasts, or courses about the concepts. Media links were found by web search in September 2026."))
for o in D["orgs"]:
    blk = [Paragraph(f"<b>{L(o['name'], o['url'])}</b>", body), Paragraph(escape(o["summary"]), small),
           Paragraph("<b>Pathways:</b> " + ", ".join(escape(P[i]["name"]) for i in o["pathways"]), small)]
    blk += [Paragraph(f"{escape(m['kind'])}: {L(m['title'], m['u'])}", small) for m in o["media"]]
    blk.append(Spacer(1, 5))
    story.append(KeepTogether(blk))

story.append(PageBreak())
story += section("Journeys")
for j in D["journeys"]:
    story.append(Paragraph(f"{escape(j['title'])}  <font size=8.5 color='#666666'>{escape(j['id'])}</font>", h))
    story.append(Paragraph(escape(j["who"]), body))
    for i, s in enumerate(j["stages"], 1):
        story.append(KeepTogether([Paragraph(f"<b>{i}. {escape(s['where'])}</b>  <font size=8.5 color='#666666'>{escape(', '.join(s['levels']))}</font>", body),
                                   Paragraph(escape(s["note"]), body),
                                   Paragraph("<b>Pathways:</b> " + ", ".join(escape(P[x]["name"]) for x in s["pathways"]), small)]))
    story.append(callout(f"<b>The braid.</b> {escape(j['braid'])}", "#fbf1dc", GOLD))

story += section("Living guides and practices by level of focus")
story.append(callout("<b>Levels of focus, not rank.</b> These are the scales where each person or practice mostly works. None sits above another, and many move across levels."))
story.append(Spacer(1, 6))
lv = Table([[Paragraph(f"<b>{escape(l['name'])}</b>", body), Paragraph(escape(l["who"]), body)] for l in D["levels"]], colWidths=[1.7 * inch, 5.0 * inch])
lv.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), 0.5, colors.HexColor("#d5dedb")),
                        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story.append(lv)
story += section("Suggested braids")
for b in D["braids"]:
    story.append(Paragraph(f"<b>{escape(b['pair'])}.</b> {escape(b['why'])}", body))
story.append(Spacer(1, 10))
story.append(Paragraph("Live resources in the companion app come from the public feed of the Systems Change Learning Guide by Jaya Ramchandani and Raisa Mirza "
                       f"({L('welearnwegrow.github.io/capacities', 'https://welearnwegrow.github.io/capacities/')}), shown unmodified under CC BY-NC-ND 4.0.", small))

def footer(c, d):
    c.saveState(); c.setFont("DV", 8); c.setFillColor(colors.HexColor("#888888"))
    c.drawRightString(letter[0] - 0.9 * inch, 0.55 * inch, f"Pathways into Complexity  |  {d.page}"); c.restoreState()

out = ROOT / "dist" / "complexity-pathways.pdf"
SimpleDocTemplate(str(out), pagesize=letter, leftMargin=0.9 * inch, rightMargin=0.9 * inch, topMargin=0.8 * inch,
                  bottomMargin=0.8 * inch, title="Pathways into Complexity").build(story, onFirstPage=footer, onLaterPages=footer)
print(f"ok: {out}")
