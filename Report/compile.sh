#!/usr/bin/env bash
set -euo pipefail

export PATH="/Library/TeX/texbin:$PATH"

FILE="${1:-main}"
BASE="${FILE%.tex}"

echo "==> Pass 1: xelatex"
xelatex -interaction=nonstopmode "$BASE.tex"

echo "==> bibtex"
bibtex "$BASE" || true

echo "==> Pass 2: xelatex"
xelatex -interaction=nonstopmode "$BASE.tex"

echo "==> Pass 3: xelatex"
xelatex -interaction=nonstopmode "$BASE.tex"

echo "==> Done: $BASE.pdf"
