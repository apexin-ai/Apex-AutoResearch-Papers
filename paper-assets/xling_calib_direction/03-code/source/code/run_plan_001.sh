#!/usr/bin/env bash
set -euo pipefail

# run_plan_001.sh — Qwen3-235B GPTQ-Int4 end-to-end pipeline
# Steps: validate model → extract activations → train probes → transfer eval

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
PYTHON=/root/miniconda3/bin/python3

# --- Paths ---
MODEL=/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4
CODE=/root/xling_calib_direction/code
ACT_DIR=/root/autodl-tmp/activations/qwen3_235b
RESULT_DIR=/root/xling_calib_direction/results_plan001
PROBE_DIR=${RESULT_DIR}/probes

# --- Config ---
LAYERS="0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,93"
ALL_LANGS=(en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk)
TGT_LANGS=(zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk)

# --- Env ---
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1

ts() { date "+%Y-%m-%d %H:%M:%S"; }

echo "============================================================"
echo " run_plan_001.sh — Qwen3-235B GPTQ-Int4"
echo " Started: $(ts)"
echo "============================================================"

# =============================================================
# Step 0: Dependencies
# =============================================================
echo "[$(ts)] Step 0: Checking dependencies..."

$PYTHON -c "import auto_gptq" 2>/dev/null && echo "  auto-gptq: OK" || \
$PYTHON -c "import gptqmodel" 2>/dev/null && echo "  gptqmodel: OK" || {
    echo "  Installing GPTQ backend..."
    pip install auto-gptq --no-build-isolation 2>&1 | tail -3
}

$PYTHON -c "import sklearn" 2>/dev/null && echo "  sklearn: OK" || {
    echo "  Installing scikit-learn..."
    pip install scikit-learn 2>&1 | tail -1
}

echo "[$(ts)] Step 0 DONE"

# =============================================================
# Step 1: Validate model integrity
# =============================================================
echo ""
echo "[$(ts)] Step 1: Validating model..."

SHARD_COUNT=$(ls "${MODEL}"/*.safetensors 2>/dev/null | wc -l)
echo "  Shards: ${SHARD_COUNT}/32"
if [ "${SHARD_COUNT}" -ne 32 ]; then
    echo "FATAL: Expected 32 safetensors shards, found ${SHARD_COUNT}"
    exit 1
fi

$PYTHON -c "
from transformers import AutoTokenizer
t = AutoTokenizer.from_pretrained('${MODEL}', trust_remote_code=True)
print(f'  Vocab: {t.vocab_size}')
"
echo "[$(ts)] Step 1 DONE"

# =============================================================
# Step 2: Extract activations (20 langs x 24 layers)
# =============================================================
echo ""
echo "[$(ts)] Step 2: Extracting activations (20 langs x 24 layers)..."
mkdir -p "${ACT_DIR}"

# GPTQ model: --quantization none lets HF auto-detect GPTQ config from model.
# --quantization int4 would apply bitsandbytes NF4 on top, which is wrong.
$PYTHON "${CODE}/extract_activations_large.py" \
    --model "${MODEL}" \
    --languages "${ALL_LANGS[@]}" \
    --layers "${LAYERS}" \
    --output_dir "${ACT_DIR}" \
    --split_ratio 0.7 \
    --quantization none \
    --save_interval 200 \
    --dtype bfloat16

echo "[$(ts)] Step 2 DONE"

# =============================================================
# Step 2.5: Create symlink dirs for train/eval splits
#
# extract_activations_large.py with --split_ratio outputs:
#   layer{i}_{lang}_train.pt / layer{i}_{lang}_eval.pt
# But train_probe.py and transfer_eval.py expect:
#   layer{i}_{lang}.pt
# Solution: symlink directories.
# =============================================================
echo ""
echo "[$(ts)] Step 2.5: Creating split symlink dirs..."

TRAIN_DIR="${ACT_DIR}/train"
EVAL_DIR="${ACT_DIR}/for_eval"
mkdir -p "${TRAIN_DIR}" "${EVAL_DIR}"

# Train dir: all train splits as layer{i}_{lang}.pt
for f in "${ACT_DIR}"/layer*_*_train.pt; do
    [ -e "$f" ] || continue
    base=$(basename "$f")
    ln -sf "../${base}" "${TRAIN_DIR}/${base/_train.pt/.pt}"
done

# Eval dir:
#   English -> train split (same data the probe was trained on, for mean/Procrustes/few-shot)
#   Target langs -> eval split (held-out for evaluation)
for f in "${ACT_DIR}"/layer*_en_train.pt; do
    [ -e "$f" ] || continue
    base=$(basename "$f")
    ln -sf "../${base}" "${EVAL_DIR}/${base/_train.pt/.pt}"
done
for f in "${ACT_DIR}"/layer*_*_eval.pt; do
    [ -e "$f" ] || continue
    base=$(basename "$f")
    [[ "$base" == *_en_eval.pt ]] && continue
    ln -sf "../${base}" "${EVAL_DIR}/${base/_eval.pt/.pt}"
done

echo "  train/:     $(ls "${TRAIN_DIR}"/*.pt 2>/dev/null | wc -l) files"
echo "  for_eval/:  $(ls "${EVAL_DIR}"/*.pt 2>/dev/null | wc -l) files"
echo "[$(ts)] Step 2.5 DONE"

# =============================================================
# Step 3a: Train English probes (on train split)
# =============================================================
echo ""
echo "[$(ts)] Step 3a: Training English probes..."
mkdir -p "${PROBE_DIR}"

$PYTHON "${CODE}/train_probe.py" \
    --activations_dir "${TRAIN_DIR}" \
    --output_dir "${PROBE_DIR}" \
    --layers "${LAYERS}"

echo "[$(ts)] Step 3a DONE"

# =============================================================
# Step 3b: Transfer evaluation (on eval split)
# Methods: zero-shot, mean-shift, Procrustes(100), few-shot(25,100)
# =============================================================
echo ""
echo "[$(ts)] Step 3b: Transfer evaluation..."

$PYTHON "${CODE}/transfer_eval.py" \
    --activations_dir "${EVAL_DIR}" \
    --probes_dir "${PROBE_DIR}" \
    --output_dir "${RESULT_DIR}" \
    --layers "${LAYERS}" \
    --languages "${TGT_LANGS[@]}" \
    --n_proj_pairs 100 \
    --n_few_shot "25,100"

echo "[$(ts)] Step 3b DONE"

# =============================================================
# Step 4: Summary
# =============================================================
echo ""
echo "[$(ts)] Step 4: Results summary"
echo "============================================================"
echo "  Activations:  ${ACT_DIR}/"
echo "  Probes:       ${PROBE_DIR}/"
echo "  Results:      ${RESULT_DIR}/"

if [ -f "${PROBE_DIR}/train_metrics.csv" ]; then
    echo ""
    echo "--- Probe training metrics ---"
    cat "${PROBE_DIR}/train_metrics.csv"
fi

if [ -f "${RESULT_DIR}/transfer_results.csv" ]; then
    echo ""
    echo "--- Transfer results (first 30 rows) ---"
    head -31 "${RESULT_DIR}/transfer_results.csv"
fi

echo ""
echo "============================================================"
echo " DONE: $(ts)"
echo "============================================================"
