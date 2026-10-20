#!/bin/bash
# RASP MVP Experiment
# cuda:0: Standard LLM-Pruner (importance only) → GRPO RLVR
# cuda:1: RASP (CKA-aware) → GRPO RLVR
set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

mkdir -p results models

echo "=========================================="
echo "RASP MVP Experiment"
echo "=========================================="

# Step 1: CKA overlap computation (cuda:0)
echo "[Step 1/6] Computing CKA overlap scores..."
CUDA_VISIBLE_DEVICES=0 python3 src/cka_overlap.py \
  --model_path models/DeepSeek-R1-Distill-Qwen-7B \
  --output_path results/cka_scores.pt \
  --n_samples 512

# Step 2: Importance scoring (cuda:0)
echo "[Step 2/6] Computing gradient-based importance scores..."
CUDA_VISIBLE_DEVICES=0 python3 src/importance_score.py \
  --model_path models/DeepSeek-R1-Distill-Qwen-7B \
  --output_path results/importance_scores.pt \
  --n_samples 512

# Step 3: Pruning (parallel on 2 GPUs)
echo "[Step 3/6] Pruning models..."
CUDA_VISIBLE_DEVICES=0 python3 src/prune.py \
  --model_path models/DeepSeek-R1-Distill-Qwen-7B \
  --importance_path results/importance_scores.pt \
  --mode standard --sparsity 0.35 \
  --output_path models/pruned_standard_35 &
PID_STD=$!

CUDA_VISIBLE_DEVICES=1 python3 src/prune.py \
  --model_path models/DeepSeek-R1-Distill-Qwen-7B \
  --importance_path results/importance_scores.pt \
  --cka_path results/cka_scores.pt \
  --mode rasp --sparsity 0.35 --alpha 1.0 \
  --output_path models/pruned_rasp_35 &
PID_RASP=$!

wait $PID_STD $PID_RASP
echo "Pruning complete."

# Step 4: GRPO RLVR Recovery (parallel on 2 GPUs)
echo "[Step 4/6] GRPO RLVR recovery training..."
CUDA_VISIBLE_DEVICES=0 python3 src/train_grpo.py \
  --model_path models/pruned_standard_35 \
  --output_path models/recovered_standard_35 \
  --gpu 0 &
PID_TRAIN_STD=$!

CUDA_VISIBLE_DEVICES=1 python3 src/train_grpo.py \
  --model_path models/pruned_rasp_35 \
  --output_path models/recovered_rasp_35 \
  --gpu 1 &
PID_TRAIN_RASP=$!

wait $PID_TRAIN_STD $PID_TRAIN_RASP
echo "GRPO recovery complete."

# Step 5: Evaluation (parallel on 2 GPUs)
echo "[Step 5/6] Evaluating on GSM8K test set..."
CUDA_VISIBLE_DEVICES=0 python3 src/eval_gsm8k.py \
  --model_path models/recovered_standard_35 \
  --output_path results/eval_recovered_standard_35.json &
PID_EVAL_STD=$!

CUDA_VISIBLE_DEVICES=1 python3 src/eval_gsm8k.py \
  --model_path models/recovered_rasp_35 \
  --output_path results/eval_recovered_rasp_35.json &
PID_EVAL_RASP=$!

wait $PID_EVAL_STD $PID_EVAL_RASP

# Step 6: Correlation Analysis (cuda:0)
echo "[Step 6/6] Running correlation analysis..."
CUDA_VISIBLE_DEVICES=0 python3 src/correlation_analysis.py \
  --base_model_path models/DeepSeek-R1-Distill-Qwen-7B \
  --pruned_model_path models/pruned_rasp_35 \
  --recovered_model_path models/recovered_rasp_35 \
  --cka_scores_path results/cka_scores.pt \
  --pruning_mask_path models/pruned_rasp_35/pruning_metadata.pt \
  --output_dir results/analysis/ \
  --n_samples 256

echo "=========================================="
echo "MVP Experiment Complete"
echo "=========================================="
echo "Results:"
echo "  Standard: results/eval_recovered_standard_35.json"
echo "  RASP:     results/eval_recovered_rasp_35.json"
echo "  Correlation: results/analysis/correlation_results.json"
python3 -c "
import json
for name, path in [('Standard', 'results/eval_recovered_standard_35.json'), ('RASP', 'results/eval_recovered_rasp_35.json')]:
    with open(path) as f:
        d = json.load(f)
    print(f'  {name}: {d[\"accuracy\"]:.4f} ({d[\"n_correct\"]}/{d[\"n_total\"]})')
with open('results/analysis/correlation_results.json') as f:
    d = json.load(f)
print(f'  Correlation: rho={d[\"spearman_rho\"]:.4f}, p={d[\"p_value\"]:.2e}, verdict={d[\"mvp_verdict\"]}')
"
