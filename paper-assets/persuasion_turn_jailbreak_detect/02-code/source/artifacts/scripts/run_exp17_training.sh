#!/bin/bash
# exp17: Dataset Scale experiment — 3 variants x 3 seeds on expanded 1000-sample data
# GPU constraint: cuda:0-3 only (C001)
set -e
set -o pipefail

export PATH=/root/miniconda3/bin:$PATH
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export PYTHONPATH=/root/persuasion_turn_jailbreak_detect
export HF_HOME=/root/autodl-tmp/hf_cache 2>/dev/null || true

cd /root/persuasion_turn_jailbreak_detect

DATA_DIR="data/expanded_1000"
CKPT_DIR="checkpoints/exp17"
LOG_DIR="results/exp17"
mkdir -p "$CKPT_DIR" "$LOG_DIR"

SEEDS=(42 123 456)

echo "=== exp17 Training Started: $(date) ==="
echo "Data: $DATA_DIR"
echo "Checkpoints: $CKPT_DIR"

# --- Variant 1: Vanilla (baseline DeBERTa -> GRU) ---
for SEED in "${SEEDS[@]}"; do
    echo ""
    echo ">>> Vanilla seed=$SEED (cuda:0) — $(date)"
    CUDA_VISIBLE_DEVICES=0 python src/train_classifier.py \
        --train_data "$DATA_DIR/train.jsonl" \
        --val_data "$DATA_DIR/val.jsonl" \
        --mode baseline \
        --model_name microsoft/deberta-v3-base \
        --output_dir "$CKPT_DIR/vanilla_seed${SEED}" \
        --epochs 20 \
        --batch_size 32 \
        --hidden_dim 256 \
        --num_layers 2 \
        --dropout 0.3 \
        --lr 1e-3 \
        --max_length 256 \
        --seed "$SEED" \
        2>&1 | tee "$LOG_DIR/vanilla_seed${SEED}.log"
done

# --- Variant 2: MLM-only (MLM pretrain -> GRU) ---
for SEED in "${SEEDS[@]}"; do
    echo ""
    echo ">>> MLM Stage 1 seed=$SEED (cuda:1) — $(date)"
    CUDA_VISIBLE_DEVICES=1 python src/train_deberta_mlm.py \
        --train_data "$DATA_DIR/train.jsonl" \
        --val_data "$DATA_DIR/val.jsonl" \
        --model_name microsoft/deberta-v3-base \
        --output_dir "$CKPT_DIR/mlm_seed${SEED}/deberta_mlm" \
        --max_length 256 \
        --batch_size 16 \
        --lr 2e-5 \
        --epochs 4 \
        --seed "$SEED" \
        2>&1 | tee "$LOG_DIR/mlm_stage1_seed${SEED}.log"

    echo ">>> MLM Stage 2 (GRU) seed=$SEED (cuda:1) — $(date)"
    CUDA_VISIBLE_DEVICES=1 python src/train_classifier.py \
        --train_data "$DATA_DIR/train.jsonl" \
        --val_data "$DATA_DIR/val.jsonl" \
        --mode treatment \
        --deberta_checkpoint "$CKPT_DIR/mlm_seed${SEED}/deberta_mlm/best" \
        --model_name microsoft/deberta-v3-base \
        --output_dir "$CKPT_DIR/mlm_seed${SEED}" \
        --epochs 20 \
        --batch_size 32 \
        --hidden_dim 256 \
        --num_layers 2 \
        --dropout 0.3 \
        --lr 1e-3 \
        --max_length 256 \
        --seed "$SEED" \
        2>&1 | tee "$LOG_DIR/mlm_stage2_seed${SEED}.log"
done

# --- Variant 3: 9-class (multitask pretrain -> GRU) ---
for SEED in "${SEEDS[@]}"; do
    echo ""
    echo ">>> 9-class Stage 1 seed=$SEED (cuda:2) — $(date)"
    CUDA_VISIBLE_DEVICES=2 python src/train_deberta.py \
        --train_data "$DATA_DIR/train.jsonl" \
        --val_data "$DATA_DIR/val.jsonl" \
        --model_name microsoft/deberta-v3-base \
        --output_dir "$CKPT_DIR/9class_seed${SEED}/deberta_multitask" \
        --epochs 4 \
        --batch_size 16 \
        --lr 2e-5 \
        --max_length 256 \
        --seed "$SEED" \
        2>&1 | tee "$LOG_DIR/9class_stage1_seed${SEED}.log"

    echo ">>> 9-class Stage 2 (GRU) seed=$SEED (cuda:2) — $(date)"
    CUDA_VISIBLE_DEVICES=2 python src/train_classifier.py \
        --train_data "$DATA_DIR/train.jsonl" \
        --val_data "$DATA_DIR/val.jsonl" \
        --mode treatment \
        --deberta_checkpoint "$CKPT_DIR/9class_seed${SEED}/deberta_multitask/best" \
        --model_name microsoft/deberta-v3-base \
        --output_dir "$CKPT_DIR/9class_seed${SEED}" \
        --epochs 20 \
        --batch_size 32 \
        --hidden_dim 256 \
        --num_layers 2 \
        --dropout 0.3 \
        --lr 1e-3 \
        --max_length 256 \
        --seed "$SEED" \
        2>&1 | tee "$LOG_DIR/9class_stage2_seed${SEED}.log"
done

echo ""
echo "=== exp17 Training Complete: $(date) ==="
echo "Checkpoints saved to $CKPT_DIR"
