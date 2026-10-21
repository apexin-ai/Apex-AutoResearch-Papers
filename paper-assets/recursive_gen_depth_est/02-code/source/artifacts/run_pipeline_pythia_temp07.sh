#!/bin/bash
# τ=0.7 temperature pilot — Pythia-1.4B, recursive generation d0→d5, 500 samples/depth
# Compares with τ=0.9 Pythia results (d1v2 AUC=0.8327 RF) to check if AUC inversion occurs

set -e

if [ -n "${AML_EXP_ID:-}" ]; then
    _aml_exit_handler() { local ec=$?; mkdir -p /tmp/agent-ml-exit; printf "%s|%s\n" "$ec" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "/tmp/agent-ml-exit/${AML_EXP_ID}.exit"; }
    trap _aml_exit_handler EXIT
fi

PROJECT_DIR="/root/autodl-tmp/recursive_gen_depth_est"
cd $PROJECT_DIR

source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export CUDA_VISIBLE_DEVICES=0

if [ -f /root/miniconda3/etc/profile.d/conda.sh ]; then
    source /root/miniconda3/etc/profile.d/conda.sh
    conda activate base
fi

MODEL_PATH="/root/autodl-tmp/models/pythia-1.4b"
TARGET_MODULES="query_key_value"
DATA_DIR="data/pythia_temp07"
CKPT_DIR="checkpoints/pythia_temp07"
RESULTS_DIR="results/temp07_pilot"
NUM_SAMPLES=500

mkdir -p "$DATA_DIR" "$CKPT_DIR" "$RESULTS_DIR" logs

LOG_FILE="logs/pipeline_pythia_temp07.log"
exec > >(tee -a "$LOG_FILE") 2>&1

echo "=== Pipeline: Pythia-1.4B temp_only t=0.7 pilot ($NUM_SAMPLES samples/depth, d0-d5) ==="
echo "=== Started at $(date) ==="

# Step 0: Subsample depth_0 from original seed data
echo "[$(date)] === Step 0: Subsample depth-0 ($NUM_SAMPLES from 5000) ==="
python3 -c "
import json, random
random.seed(42)
with open('data/depth_0.jsonl') as f:
    lines = f.readlines()
selected = random.sample(lines, $NUM_SAMPLES)
with open('$DATA_DIR/depth_0.jsonl', 'w') as f:
    f.writelines(selected)
print(f'Subsampled {len(selected)} from {len(lines)}')
"

# Recursive pipeline: finetune on depth_N → generate depth_N+1
for PREV_DEPTH in 0 1 2 3 4; do
    NEXT_DEPTH=$((PREV_DEPTH + 1))

    echo "[$(date)] === LoRA finetune on depth-${PREV_DEPTH} ==="
    python scripts/lora_finetune.py \
        --input_data "$DATA_DIR/depth_${PREV_DEPTH}.jsonl" \
        --output_dir "$CKPT_DIR/lora_depth_${PREV_DEPTH}" \
        --model_name "$MODEL_PATH" \
        --target_modules "$TARGET_MODULES" \
        --gpu 0

    echo "[$(date)] === Generate depth-${NEXT_DEPTH} (temp=0.7) ==="
    python scripts/generate_next_depth.py \
        --adapter_dir "$CKPT_DIR/lora_depth_${PREV_DEPTH}" \
        --output_path "$DATA_DIR/depth_${NEXT_DEPTH}.jsonl" \
        --target_depth $NEXT_DEPTH \
        --model_name "$MODEL_PATH" \
        --decoding_strategy temp_only \
        --temperature 0.7 \
        --num_samples $NUM_SAMPLES \
        --gpu 0
done

echo "[$(date)] === Data summary ==="
wc -l "$DATA_DIR"/depth_*.jsonl

# Feature extraction
echo "[$(date)] === Feature extraction (6-class, d0-d5) ==="
python scripts/extract_features.py \
    --data_dir "$DATA_DIR" \
    --model_path "$MODEL_PATH" \
    --output_path "$RESULTS_DIR/features.jsonl" \
    --gpu 0 \
    --max_depth 5

# Train classifier
echo "[$(date)] === Train classifier ==="
python scripts/train_classifier.py \
    --features_path "$RESULTS_DIR/features.jsonl" \
    --output_dir "$RESULTS_DIR/"

# Generate summary results.json
echo "[$(date)] === Generate results.json ==="
python3 -c "
import json

with open('$RESULTS_DIR/pairwise_auc.json') as f:
    pair_aucs = json.load(f)

rf_aucs = pair_aucs.get('random_forest', {})
lr_aucs = pair_aucs.get('logistic_regression', {})

d1v2_rf = rf_aucs.get('depth1_vs_depth2')
d1v2_lr = lr_aucs.get('depth1_vs_depth2')
d1v2_best = max(filter(None, [d1v2_rf, d1v2_lr]))

results = {
    'experiment': 'temp07_pilot',
    'model': 'pythia-1.4b',
    'temperature': 0.7,
    'decoding_strategy': 'temp_only',
    'samples_per_depth': $NUM_SAMPLES,
    'depths': list(range(6)),
    'key_metric': {
        'd1v2_auc_rf': d1v2_rf,
        'd1v2_auc_lr': d1v2_lr,
        'd1v2_auc_best': d1v2_best,
    },
    'comparison_temp09': {
        'd1v2_auc_rf': 0.8327,
        'd1v2_auc_lr': 0.7833,
    },
    'all_pairwise_auc': pair_aucs,
}

with open('$RESULTS_DIR/results.json', 'w') as f:
    json.dump(results, f, indent=2)

print()
print('=' * 60)
print('  TEMP07 PILOT RESULTS')
print('=' * 60)
print(f'  d1v2 AUC (RF):  {d1v2_rf}  (temp09 baseline: 0.8327)')
print(f'  d1v2 AUC (LR):  {d1v2_lr}  (temp09 baseline: 0.7833)')
print()
print('  All RF pairwise AUC:')
for k, v in sorted(rf_aucs.items()):
    print(f'    {k}: {v}')
print('=' * 60)
"

echo "[$(date)] === Pipeline complete ==="
