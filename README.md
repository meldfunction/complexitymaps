# Pathways into Complexity

One source of truth, three outputs: a live web app, a linked PDF, and a map image.

- **48 pathways** in 12 clusters, each with a kind of path, road, mix-ins, policy lens, and engage links
- **66 organization profiles** with public articles, talks, podcasts, and courses
- **16 cases** with lessons, limits, and sources
- **7 orientations**, **levels of focus** (not rank), **2 worked journeys**, and **suggested braids**
- **Live library**: on request, the app reads the public resource feed of the
  [Systems Change Learning Guide](https://welearnwegrow.github.io/capacities/)

## Build

```sh
./build.sh            # compile data, build app, PDF, and map, then run tests
```

Or step by step:

```sh
python3 build/compile.py     # content modules -> data/*.json (fails on broken references or em dashes)
python3 build/build_app.py   # src/app.html + data -> dist/index.html
python3 build/build_pdf.py   # data -> dist/complexity-pathways.pdf
python3 build/build_map.py   # data -> dist/complexity-pathways-map.png
node build/test_app.js       # headless tests with a mocked feed (needs Playwright)
```

Requirements: Python 3 with `reportlab`, `matplotlib`, and the DejaVu fonts; Node with Playwright for tests.

## Edit content

All content lives in `build/content_*.py`:

| File | Holds |
|---|---|
| `content_pathways.py` | clusters, kinds, text fixes, match terms, government flags, the new pathways |
| `content_orgs.py` | organization profiles and their media |
| `content_cases.py` | cases with lessons, limits, and sources |
| `content_misc.py` | orientations, levels, braids, journeys, and page text |

The first 29 pathways come from `data/_base_pathways.json`. Pathways, orgs, cases, and journeys
point at each other by name prefix; `compile.py` resolves them to ids and stops if a prefix matches
zero or several pathways. Every link lands in `data/urls.txt` for a link check.

## Deploy

`dist/index.html` is self-contained. Put it on any static host, for example GitHub Pages:

1. Commit `dist/index.html` (as `index.html`) to a repository.
2. Settings → Pages → Deploy from a branch → `main` / root.

The live library only works from a hosted page or a file opened in a browser. Preview sandboxes that
block outside requests show an "unreachable" notice and the rest of the app still works.

## The live library and its authors

The feed at `capacities.jayajohnyramchandani.workers.dev` belongs to Jaya Ramchandani and Raisa Mirza.
Their library is licensed CC BY-NC-ND 4.0, so the app shows their resources unmodified and credited.
Loading is trigger-based: nothing is requested on page load. The app makes one public GET request only when a
visitor taps Load or opens the Live library tab, caches the result in the browser for 72 hours, and never
calls their AI, logging, feedback, or signup endpoints. Each load still runs on their Cloudflare and
Notion accounts (their worker serves a 5-minute edge cache, so most requests never reach Notion), so let them know before sharing widely.
