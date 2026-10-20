#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# Copy bib file into paper directory if not already present
BIB_SRC="$(cd "$DIR/../../.." && pwd)/docs/paper/references.bib"
if [ -f "$BIB_SRC" ] && [ ! -f "$DIR/references.bib" ]; then
    cp "$BIB_SRC" "$DIR/references.bib"
    echo "Copied references.bib from docs/paper/"
fi

# Fetch ACL style files if missing
if [ ! -f "$DIR/acl.sty" ]; then
    echo "WARNING: acl.sty not found. Download the ACL 2023 template from"
    echo "  https://github.com/acl-org/acl-style-files"
    echo "and place acl.sty + acl_natbib.bst in this directory."
fi

echo "=== pdflatex (pass 1) ==="
pdflatex -interaction=nonstopmode main.tex

echo "=== bibtex ==="
bibtex main

echo "=== pdflatex (pass 2) ==="
pdflatex -interaction=nonstopmode main.tex

echo "=== pdflatex (pass 3) ==="
pdflatex -interaction=nonstopmode main.tex

echo "=== Done ==="
echo "Output: $DIR/main.pdf"
