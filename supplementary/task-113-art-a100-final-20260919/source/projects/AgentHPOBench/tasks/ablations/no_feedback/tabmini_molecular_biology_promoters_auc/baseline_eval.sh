#!/usr/bin/env bash
set -euo pipefail
BASE=.
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
python "$BASE/tasks/ablations/no_feedback/tabmini_molecular_biology_promoters_auc/eval_tabmini_molecular_biology_promoters_auc.py" --results-dir "$BASE/results/formal_baselines/tabmini_molecular_biology_promoters_auc/baseline_logreg"
