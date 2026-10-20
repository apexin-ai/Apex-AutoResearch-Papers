#!/bin/bash
# CWM 8B Val Sweep — 5 checkpoints across 4 GPUs
# Generated 2026-05-16
# Usage: bash val_sweep_cwm8b.sh
# Prerequisite: training must be finished (all GPUs free)

set -e

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /home/sonny/exec-sim-repair-verifier
export HF_HUB_OFFLINE=1

BASE_MODEL="/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/"
CKPT_DIR="/root/autodl-tmp/checkpoints_repo_cwm_8b_conda"
OUT_BASE="/root/autodl-tmp/eval_results/cwm8b_val_sweep"

mkdir -p "$OUT_BASE"

# ─── Round 1: 4 checkpoints on 4 GPUs in parallel ───
echo "[$(date)] Starting Round 1: ckpt 5700/5800/5900/6000"

nohup python3 eval_repo_cwm.py \
  --checkpoint_dir ${CKPT_DIR}/checkpoint-5700/ \
  --model_name ${BASE_MODEL} \
  --split val --device cuda:0 --max_new_tokens 1024 \
  --output_dir ${OUT_BASE}/ckpt_5700/ \
  > ${OUT_BASE}/ckpt_5700.log 2>&1 &
PID_5700=$!

nohup python3 eval_repo_cwm.py \
  --checkpoint_dir ${CKPT_DIR}/checkpoint-5800/ \
  --model_name ${BASE_MODEL} \
  --split val --device cuda:1 --max_new_tokens 1024 \
  --output_dir ${OUT_BASE}/ckpt_5800/ \
  > ${OUT_BASE}/ckpt_5800.log 2>&1 &
PID_5800=$!

nohup python3 eval_repo_cwm.py \
  --checkpoint_dir ${CKPT_DIR}/checkpoint-5900/ \
  --model_name ${BASE_MODEL} \
  --split val --device cuda:2 --max_new_tokens 1024 \
  --output_dir ${OUT_BASE}/ckpt_5900/ \
  > ${OUT_BASE}/ckpt_5900.log 2>&1 &
PID_5900=$!

nohup python3 eval_repo_cwm.py \
  --checkpoint_dir ${CKPT_DIR}/checkpoint-6000/ \
  --model_name ${BASE_MODEL} \
  --split val --device cuda:3 --max_new_tokens 1024 \
  --output_dir ${OUT_BASE}/ckpt_6000/ \
  > ${OUT_BASE}/ckpt_6000.log 2>&1 &
PID_6000=$!

echo "Round 1 PIDs: 5700=$PID_5700 5800=$PID_5800 5900=$PID_5900 6000=$PID_6000"
echo "Waiting for Round 1..."
wait $PID_5700 $PID_5800 $PID_5900 $PID_6000
echo "[$(date)] Round 1 complete."

# ─── Round 2: checkpoint-400 (early training baseline) ───
echo "[$(date)] Starting Round 2: ckpt 400"

nohup python3 eval_repo_cwm.py \
  --checkpoint_dir ${CKPT_DIR}/checkpoint-400/ \
  --model_name ${BASE_MODEL} \
  --split val --device cuda:0 --max_new_tokens 1024 \
  --output_dir ${OUT_BASE}/ckpt_400/ \
  > ${OUT_BASE}/ckpt_400.log 2>&1 &
PID_400=$!

echo "Round 2 PID: 400=$PID_400"
wait $PID_400
echo "[$(date)] Round 2 complete. All checkpoints evaluated."

# ─── Summary ───
echo ""
echo "=== VAL SWEEP SUMMARY ==="
for ckpt in 400 5700 5800 5900 6000; do
  JSON="${OUT_BASE}/ckpt_${ckpt}/eval_repo_cwm.json"
  if [ -f "$JSON" ]; then
    echo "checkpoint-${ckpt}:"
    python3 -c "
import json
with open('${JSON}') as f:
    d = json.load(f)
m = d['metrics']
print(f\"  acc={m['accuracy']:.2f}%  f1_macro={m['f1_macro']:.2f}%  unparseable={d.get('n_cwm_unparseable', '?')}\")
"
  else
    echo "checkpoint-${ckpt}: FAILED (no output)"
  fi
done
