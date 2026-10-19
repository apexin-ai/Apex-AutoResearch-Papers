#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export AUTOREP_ROOT="${AUTOREP_ROOT:-.}"
export PYTHONPATH="$AUTOREP_ROOT:$AUTOREP_ROOT/.python_deps:${PYTHONPATH:-}"
export SIMPLE_RL_CUDA_VISIBLE_DEVICES="${SIMPLE_RL_CUDA_VISIBLE_DEVICES:-0}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate "${AUTOREP_AGENT_CONDA_ENV:-autorep-vlm2vec}"
python "$SCRIPT_DIR/run_formal_simple_rl_reason_qwen25_05b_math500_agent.py" "$@"
