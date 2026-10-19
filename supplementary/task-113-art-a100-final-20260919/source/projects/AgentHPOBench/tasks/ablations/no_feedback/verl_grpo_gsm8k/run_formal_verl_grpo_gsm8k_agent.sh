#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export AUTOREP_ROOT="${AUTOREP_ROOT:-.}"
export PYTHONPATH="$AUTOREP_ROOT:$AUTOREP_ROOT/.python_deps:${PYTHONPATH:-}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate "${AUTOREP_AGENT_CONDA_ENV:-autorep-vlm2vec}"
python "$SCRIPT_DIR/run_formal_verl_grpo_gsm8k_agent.py" "$@"
