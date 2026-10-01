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
