"""Build dist/index.html: the single-file app with data inlined and the live worker wired in.

Run: python3 build/build_app.py   (after build/compile.py)
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.load(open(ROOT / "data" / "site-data.json"))
tpl = (ROOT / "src" / "app.html").read_text()

payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

for marker, value in (("__DATA__", payload),):
    if marker not in tpl:
        raise SystemExit(f"template marker missing: {marker}")
    tpl = tpl.replace(marker, value)

out = ROOT / "dist" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(tpl)
# Anime.js (MIT) ships beside the page and is loaded with defer; every view works without it.
import shutil
for f in ("anime.umd.min.js", "anime-LICENSE.md"):
    shutil.copy(ROOT / "src" / "vendor" / f, out.parent / f)
if "\u2014" in tpl:
    raise SystemExit("em dash found in built app")
print(f"ok: {out} ({out.stat().st_size // 1024} KB)")
