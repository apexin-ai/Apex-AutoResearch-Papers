#!/usr/bin/env bash
set -euo pipefail
BASE=.
mkdir -p "$BASE/data/paper_exact/tabmini_molecular_biology_promoters_auc"
cp "$BASE/repositories/TabMini/plotting/data/2/molecular_biology_promoters/X.csv" "$BASE/data/paper_exact/tabmini_molecular_biology_promoters_auc/X.csv"
cp "$BASE/repositories/TabMini/plotting/data/2/molecular_biology_promoters/y.csv" "$BASE/data/paper_exact/tabmini_molecular_biology_promoters_auc/y.csv"
