#!/usr/bin/env bash
set -euo pipefail

ROOT=${AUTOREP_ROOT:-.}
LOG=${UNI2TS_AGENT_LOG:-$ROOT/logs/formal_agent/qwen3_32b/uni2ts_lsf_etth1_$(date -u +%Y%m%d_%H%M%S).log}

mkdir -p "$(dirname "$LOG")"
cd "$ROOT"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
python tasks/ablations/no_feedback/uni2ts_lsf_etth1/run_formal_uni2ts_lsf_etth1_agent.py 2>&1 | tee "$LOG"
