#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export AUTOREP_ROOT="${AUTOREP_ROOT:-.}"
export PYTHONPATH="$AUTOREP_ROOT:$AUTOREP_ROOT/.python_deps:$AUTOREP_ROOT/repositories/VAR:${PYTHONPATH:-}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate "${AUTOREP_VAR_CONDA_ENV:-autorep-var}"
python "$SCRIPT_DIR/run_formal_var_imagenet_agent.py" "$@"
