# Pathways into Complexity

One source of truth, three outputs: a live web app, a linked PDF, and a map image.

- **56 pathways** in 12 clusters and 4 hue families, each with a kind of path, road, mix-ins, policy lens, and engage links
- **69 organization profiles** with public articles, talks, podcasts, and courses
- **41 cases** with lessons, limits, and sources (48 of 50 pathways have at least one)
- **92 people and institutions** with life dates (40 checked, the rest draft) and **7 draft profiles**
- **Every article** has a plain explainer, a lens, first steps to try, notes for five sectors, and key ideas (all Draft)
- **7 orientations**, **levels of focus** (not rank), **2 worked journeys**, and **suggested braids**
- **Live library**: on request, the app reads the public resource feed of the
  [Systems Change Learning Guide](https://welearnwegrow.github.io/capacities/)

- **65 Complexity Lounge talks** (`build/content_lounge.py`) linked from the pathways they fit and featured on each guest's profile, plus six pathways they pointed to: complex responsive processes, resilience engineering, systems thinking traditions, mind/life/constraints, technology and AI, and software/flow

## The app (Field Atlas design)

`dist/index.html` is one file with a hash router:

| Route | Screen |
|---|---|
| `#/` | Home: the problem, search, five doors, browse by goal / type / scale, lenses, mission, how to use this site (three kinds of visit, each with steps and a call to action), featured topic |
| `#/wiki`, `#/wiki/<pathway-id>` | Wiki index (filters `?goal=`, `?kind=`, `?scale=`, `?q=`) and article |
| `#/path` | Find my work: start, area, trade, first pathway, where that work happens (state in the query string) |
| `#/map?view=universe\|metro\|tree\|treemap\|mine\|time&p=<id>` | Map hub; the selected pathway is shared across tabs. On the universe, `links=near\|shared` shows connections (designed neighbours, or shared cases and groups) |
| `#/people/<slug>` | Person profile, with "where I land" kept in `localStorage` |
| `#/contribute`, `#/about` | Suggest a change (prefilled GitHub issue), about. The acknowledgment page is withdrawn for now; `#/about/acknowledgment` lands on About |
| `#/orgs`, `#/cases`, `#/library` | Organizations, cases, and the live library |

Old links (`#p-…`, `#o-…`, `#c-…`, `#library`) redirect. The trail (`pathways-my-trail`), explored pathways and
stances stay in the browser. Anything not yet checked against sources is marked **Draft** in the UI.

## Motion

Small animations explain how ideas connect, what came before what, and where you are: an "Ideas in motion"
carousel on the home page (feedback loops, emergence, probe-sense-respond, tipping points, Two Loops, Umwelt,
icon/index/symbol, Goodhart's law, each linked to its pathway), roads and lineages that draw themselves, the universe zoom, metro lines drawing in, trail replay and
drag-to-reorder, a "who was alive when" year scrubber, treemap fills, Find my work growing like a tree, and a
"where I land" balance on profiles. They use [Anime.js](https://animejs.com) v4 (MIT), shipped beside the page as
`dist/anime.umd.min.js` (from `src/vendor/`) and loaded with `defer`.

Every view renders in its final state first, and the motion is layered on top (`onMount` in `src/app.html`).
Nothing animates when the device asks for reduced motion, when the visitor turns motion off in the footer,
or when the script fails to load.

Home photo: Annie Spratt on [Unsplash](https://unsplash.com/photos/people-farming-on-field-during-daytime-SWP0hOIMzKg)
(Unsplash License), in `src/img/`.

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
| `content_atlas.py` | redesign drafts: families, goals, tags, trades, roles, lenses, explainers, glossary |
| `content_people.py` | life dates (with a checked/draft status and source) and draft profiles |
| `content_depth.py` | per-pathway explainer, lens, practice steps, sector notes, and key ideas |

`python3 build/compile.py -v` lists warnings: road stops with no years and pathways whose lens still falls back to its area.

The first 29 pathways come from `data/_base_pathways.json`. Pathways, orgs, cases, and journeys
point at each other by name prefix; `compile.py` resolves them to ids and stops if a prefix matches
zero or several pathways. Every link lands in `data/urls.txt`. Check them from your own machine with `python3 build/check_links.py` (many sites block cloud servers).

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
