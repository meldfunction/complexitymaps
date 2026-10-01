"""Compile the content modules into data/*.json, the single source every output builds from.

Run: python3 build/compile.py
Fails loudly on unresolved references, ambiguous prefixes, duplicate ids, or em dashes.
"""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))
from content_pathways import CLUSTERS, KINDS, FIXES, META, NEW, READING, GOV_TRACK
from content_orgs import ORGS
from content_cases import CASES
from content_misc import ORIENTATIONS, LEVELS, BRAIDS, JOURNEYS, ABOUT
import content_atlas as A
from content_people import PEOPLE, PROFILES
from content_depth import D as DEPTH

errors = []
slug = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

# ---- pathways
base = json.load(open(ROOT / "data" / "_base_pathways.json"))
for p in base:
    for pre, field, old, new in FIXES:
        if p["name"].startswith(pre):
            p[field] = new if old is None else p[field].replace(old, new)
    m = [v for k, v in META.items() if p["name"].startswith(k)]
    if len(m) != 1:
        errors.append(f"META match for {p['name']}: {len(m)}")
        continue
    p["kind"], p["terms"], p["caps"] = m[0]
pathways = base + [dict(p) for p in NEW]
cluster_names = [c[0] for c in CLUSTERS]
order = {c: i for i, c in enumerate(cluster_names)}
for p in pathways:
    p["id"] = slug(p["name"])
    if p["cluster"] not in order: errors.append(f"unknown cluster {p['cluster']} on {p['name']}")
    if p["kind"] not in KINDS: errors.append(f"unknown kind {p['kind']} on {p['name']}")
pathways.sort(key=lambda p: order.get(p["cluster"], 99))  # stable: keeps authored order within a cluster
ids = [p["id"] for p in pathways]
if len(set(ids)) != len(ids): errors.append("duplicate pathway ids")

def resolve(prefix, where):
    hits = [p["id"] for p in pathways if p["name"].startswith(prefix)]
    if len(hits) != 1:
        errors.append(f"{where}: prefix '{prefix}' matched {len(hits)} pathways")
        return None
    return hits[0]

for o in ORGS:
    o["pathways"] = [x for x in (resolve(pre, "org " + o["id"]) for pre in o["pathways"]) if x]
for c in CASES:
    c["pathways"] = [x for x in (resolve(pre, "case " + c["id"]) for pre in c["pathways"]) if x]
level_names = [l[0] for l in LEVELS]
for j in JOURNEYS:
    for s in j["stages"]:
        s["pathways"] = [x for x in (resolve(pre, "journey " + j["id"]) for pre in s["pathways"]) if x]
        for lv in s["levels"]:
            if lv not in level_names: errors.append(f"journey {j['id']}: unknown level {lv}")
for key in ("orgs", "cases"):
    seen = [x["id"] for x in (ORGS if key == "orgs" else CASES)]
    if len(set(seen)) != len(seen): errors.append(f"duplicate {key} ids")

for p in pathways:
    p["orgs"] = [o["id"] for o in ORGS if p["id"] in o["pathways"]]
    p["cases"] = [c["id"] for c in CASES if p["id"] in c["pathways"]]
    p["gov"] = any(p["name"].startswith(g) for g in GOV_TRACK)
    p["reading"] = next((v for k, v in READING.items() if p["name"].startswith(k)), [])

# ---- Field Atlas fields (drafts from the redesign; see content_atlas.py)
warnings = []
sid_of = {v: k for k, v in A.SHORT.items()}
for k, v in A.SHORT.items():
    if v not in ids: errors.append(f"SHORT {k} -> unknown pathway {v}")
strip_tags = lambda t: re.sub(r"<[^>]+>", "", t or "")
people_by = {x["name"].lower(): x for x in PEOPLE}
def find_people(text):
    t = text.lower()
    return [x for n, x in people_by.items() if n in t]
for p in pathways:
    sid = sid_of.get(p["id"])
    if not sid: errors.append(f"no short id for {p['id']}"); continue
    p["short"], p["short_name"] = sid, A.SHORT_NAMES[sid]
    p["family"] = A.CLUSTER_FAMILY.get(p["cluster"])
    if not p["family"]: errors.append(f"no family for cluster {p['cluster']}")
    sec, sc = A.TAGS[sid].split("|")
    p["sectors"], p["scales"] = sec.split(","), sc.split(",")
    p["work_kinds"] = [k for k, v in A.WORK_TAGS.items() if sid in v]
    p["goals"] = [g[0] for g in A.GOALS if sid in g[3]]
    if not p["goals"]: errors.append(f"untagged goals: {p['name']}")
    cl = next((t for r, t in A.CLUSTER_LENS if re.search(r, p["cluster"])), "")
    dp = DEPTH.get(sid, {})
    if not dp: errors.append(f"no depth content for {sid}")
    lens = A.PATH_LENS.get(p["id"]) or dp.get("lens")
    p["lens"], p["lens_status"] = (lens, "draft") if lens else (cl, "cluster")
    p["explainer"] = A.EXPLAINERS.get(p["id"]) or dp.get("explainer", [])
    p["practice"] = dp.get("practice", [])
    p["sector_notes"] = dp.get("sectors", {})
    p["key_ideas"] = [dict(term=k, defn=v) for k, v in dp.get("ideas", [])]
    for k, v in dp.get("ideas", []):
        A.GLOSSARY.setdefault(k, v)
    for f in ("explainer", "practice", "key_ideas"):
        if not p[f]: warnings.append(f"no {f}: {sid}")
    if set(p["sector_notes"]) != {"biz", "ngo", "health", "edu", "com"}: errors.append(f"sector notes incomplete: {sid}")
    p["plain_overview"] = A.PLAIN.get(p["id"], {}).get("ov", "")
    p["plain_policy"] = A.PLAIN.get(p["id"], {}).get("pol", "")
    stops = []
    for raw in [x.strip() for x in strip_tags(p["road"]).split("\u2192") if x.strip()]:
        m = re.match(r"^(.*?)\s*\((.*)\)\s*$", raw)
        name, note = (m.group(1), m.group(2)) if m else (raw, "")
        who = find_people(name)
        stops.append(dict(name=name, note=note, years="; ".join(w["years"] for w in who), people=[w["name"] for w in who]))
        if not who and re.match(r"^[A-Z][a-z]+ [A-Z]", name) and len(name) < 40:
            warnings.append(f"road stop with no years: {name} ({p['short']})")
    p["stops"] = stops
    if p["lens_status"] != "draft": warnings.append(f"lens falls back to cluster: {p['short']}")

slug_p = lambda n: slug(n)
people_out = []
for x in PEOPLE:
    n = x["name"]; last = n.split()[-1]
    appears = [q["id"] for q in pathways if n.lower() in (strip_tags(q["road"]) + " " + strip_tags(q["mix"])).lower()
               or (len(last) > 4 and x["kind"] == "person" and re.search(r"\b" + re.escape(last) + r"\b", strip_tags(q["road"]) + " " + strip_tags(q["mix"])))]
    prof = PROFILES.get(n)
    m = re.match(r"(\d{4})\D+(\d{4})", x["years"]); b = re.match(r"b\. (\d{4})", x["years"]); f = re.match(r"founded (\d{4})", x["years"])
    people_out.append(dict(x, slug=slug_p(n), appears=appears, born=int((m or b).group(1)) if (m or b) else None,
                           died=int(m.group(2)) if m else None, founded=int(f.group(1)) if f else None, profile=prof))
for n in PROFILES:
    if n.lower() not in people_by: errors.append(f"profile with no people entry: {n}")
glossary = [dict(term=k, defn=v) for k, v in A.GLOSSARY.items()]
atlas = dict(families=A.FAMILIES, edges=A.EDGES, metro=A.METRO_LINES, sectors=A.SECTORS, scales=A.SCALES,
             work_kinds=A.WORK_KINDS, goals=[dict(id=g[0], label=g[1], sub=g[2], pathways=[A.SHORT[s] for s in g[3]]) for g in A.GOALS],
             type_labels=A.TYPE_LABELS, scale_labels=A.SCALE_LABELS, trades=A.TRADES, industries=A.INDUSTRIES, roles=A.ROLES,
             branches=A.BRANCHES, area_lens=A.AREA_LENS)

data = dict(
    about=ABOUT,
    clusters=[dict(name=n, token=t, light=l, dark=d) for n, t, l, d in CLUSTERS],
    kinds=[dict(name=k, desc=v) for k, v in KINDS.items()],
    orientations=ORIENTATIONS,
    levels=[dict(name=n, who=w) for n, w in LEVELS],
    braids=[dict(pair=a, why=b) for a, b in BRAIDS],
    journeys=JOURNEYS,
    pathways=pathways,
    orgs=ORGS,
    cases=CASES,
    people=people_out,
    glossary=glossary,
    atlas=atlas,
)

blob = json.dumps(data, ensure_ascii=False)
if "\u2014" in blob: errors.append(f"em dashes found: {blob.count(chr(0x2014))}")
urls = sorted(set(re.findall(r'"(?:u|url)": "(https?://[^"]+)"', blob)))
for u in urls:
    if " " in u: errors.append(f"space in url {u}")

if errors:
    print("BUILD FAILED"); [print(" -", e) for e in errors]; sys.exit(1)

(ROOT / "data").mkdir(exist_ok=True)
for k, v in data.items():
    json.dump(v, open(ROOT / "data" / f"{k}.json", "w"), ensure_ascii=False, indent=1)
json.dump(data, open(ROOT / "data" / "site-data.json", "w"), ensure_ascii=False)
open(ROOT / "data" / "urls.txt", "w").write("\n".join(urls) + "\n")
bad_gov = [g for g in GOV_TRACK if sum(p["name"].startswith(g) for p in pathways) != 1]
if bad_gov: print("BUILD FAILED: GOV_TRACK prefixes", bad_gov); sys.exit(1)
no_orgs = [p["name"] for p in pathways if not p["orgs"] and not p["reading"]]
print(f"ok: {len(pathways)} pathways in {len(CLUSTERS)} clusters, {len(ORGS)} orgs, {len(CASES)} cases, "
      f"{len(ORIENTATIONS)} orientations, {len(JOURNEYS)} journeys, {len(urls)} unique urls")
print("pathways without an org profile:", no_orgs or "none")
no_case = [p["short"] for p in pathways if not p["cases"]]
print(f"pathways without a case ({len(no_case)}):", ", ".join(no_case) or "none")
print(f"people: {len(people_out)} ({sum(x['status'] == 'checked' for x in people_out)} dates checked), "
      f"{len(PROFILES)} draft profiles, {len(glossary)} glossary terms")
print(f"{len(warnings)} warnings (python3 build/compile.py -v to list)")
if "-v" in sys.argv: [print(" ~", w) for w in warnings]
