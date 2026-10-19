#!/usr/bin/env bash
set -euo pipefail

cd .
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export TOKENIZERS_PARALLELISM=false
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-open-r1
python tasks/main/agent_lightning_room_selector/run_formal_agent_lightning_room_selector.py
