#!/bin/sh
# Publish the browser app (web/ only) to the public repo that GitHub Pages serves.
# The MIA2 repo itself stays private; only index.html and classic.js are copied.
set -eu

SITE_REPO="aljhoberman-sys/mia2-app"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

gh repo clone "$SITE_REPO" "$WORK/site" -- --quiet
cp "$ROOT/web/index.html" "$ROOT/web/classic.js" "$WORK/site/"
touch "$WORK/site/.nojekyll"

cd "$WORK/site"
git add index.html classic.js .nojekyll
if git diff --cached --quiet; then
  echo "Site already up to date."
  exit 0
fi
SRC="$(git -C "$ROOT" rev-parse --short HEAD)"
git commit --quiet -m "Publish app from MIA2 $SRC"
git push --quiet origin HEAD
echo "Published MIA2 $SRC to https://aljhoberman-sys.github.io/mia2-app/"
