#!/usr/bin/env sh
# Build every output from the content modules, then run the app tests.
set -e
cd "$(dirname "$0")"
python3 build/compile.py
python3 build/build_app.py
python3 -W ignore build/build_pdf.py
python3 build/build_map.py
if command -v node >/dev/null 2>&1; then
  NODE_PATH="$(npm root -g 2>/dev/null)" node build/test_app.js
else
  echo "node not found: skipping app tests"
fi
