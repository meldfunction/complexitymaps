# Working in this repo

- Single-maintainer repo: commit and push directly to `main`. Never create or push other branches, and never open pull requests.
- Pushing to `main` deploys `dist/` to GitHub Pages (`.github/workflows/pages.yml`).
- Rebuild outputs with `./build.sh` after changing anything in `build/`, `data/`, or `src/`.
