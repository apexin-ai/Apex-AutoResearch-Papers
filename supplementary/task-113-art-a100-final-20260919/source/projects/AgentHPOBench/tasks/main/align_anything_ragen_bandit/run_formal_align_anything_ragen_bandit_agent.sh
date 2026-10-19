#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_ROOT:-.}"
cd "$BASE"
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-0}"
export PYTHONPATH="$BASE:$BASE/.python_deps:${PYTHONPATH:-}"
python "$BASE/tasks/main/align_anything_ragen_bandit/run_formal_align_anything_ragen_bandit_agent.py"
