"""Check that every link still answers. Run it from your own machine: many sites block cloud servers.

Usage:
    python3 build/check_links.py                         # checks data/urls.txt
    python3 build/check_links.py urls-to-check-locally.txt
    python3 build/check_links.py --all urls.txt          # also list links that look fine

Needs only Python 3. Writes link-report.csv next to the list it checked.
  ok       answered 2xx
  blocked  401, 403, 405, 406, 429 or 999: the site is up but refuses scripts; open it in a browser to be sure
  check    5xx, 202 or a timeout: try again later, then open it in a browser
  dead     404, 410 or no such host: replace the link
  verified refused the script, but listed in data/links_browser_verified.txt as checked by hand
Exit code is 1 if any link is dead.
"""
import csv, pathlib, ssl, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
args = [a for a in sys.argv[1:] if not a.startswith("--")]
show_all = "--all" in sys.argv
src = pathlib.Path(args[0] if args else pathlib.Path(__file__).resolve().parent.parent / "data" / "urls.txt")
urls = [u.strip() for u in src.read_text().splitlines() if u.strip().startswith("http")]
ctx = ssl.create_default_context()
vfile = pathlib.Path(__file__).resolve().parent.parent / "data" / "links_browser_verified.txt"
VERIFIED = {l.strip() for l in vfile.read_text().splitlines() if l.strip().startswith("http")} if vfile.exists() else set()

def fetch(url):
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
        try:
            with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (400, 403, 404, 405, 406, 429, 501):
                continue  # some servers reject HEAD; retry with GET
            return e.code, url
        except Exception as e:
            if method == "HEAD":
                continue
            reason = str(getattr(e, "reason", e))
            return ("nohost" if "Name or service not known" in reason or "nodename" in reason or "getaddrinfo" in reason else "timeout"), url
    return "timeout", url

def verdict(code, url=""):
    if url in VERIFIED and code not in (404, 410, "nohost"): return "verified"
    if code == "nohost" or code in (404, 410): return "dead"
    if code in (401, 403, 405, 406, 429, 999): return "blocked"
    if isinstance(code, int) and 200 <= code < 300 and code != 202: return "ok"
    return "check"

with ThreadPoolExecutor(12) as pool:
    rows = [(u, *fetch(u)) for u in urls] if len(urls) < 2 else list(zip(urls, *zip(*pool.map(fetch, urls))))

report = src.with_name("link-report.csv")
with open(report, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["verdict", "status", "url", "final_url"])
    for u, code, final in rows: w.writerow([verdict(code, u), code, u, final])

counts = {}
for u, code, final in rows:
    v = verdict(code, u); counts[v] = counts.get(v, 0) + 1
    if v not in ("ok", "verified") or show_all:
        print(f"{v:8} {code!s:7} {u}" + (f"  ->  {final}" if final != u else ""))
print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())), f"of {len(rows)}. Report: {report}")
sys.exit(1 if counts.get("dead") else 0)
