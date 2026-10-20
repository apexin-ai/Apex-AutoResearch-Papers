#!/bin/bash
# CWM rank=32 ablation — function-level eval on full test set
# Matches rank=16 baseline eval parameters exactly (batch_size=16, max_seq=2048, max_new=64)
# Run after training completes (1434/1434 steps)
#
# Baseline reference: eval_cwm_seed123.json → acc=87.2%, f1_macro=87.2%
#   command: python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm_seed123/best
#            --model_name Qwen/Qwen3-4B --save_predictions (all other args default)

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

cd /home/sonny/exec-sim-repair-verifier

# 创建输出目录
mkdir -p eval_results/cwm_rank32_eval

# GPU 0 训练完成后释放，直接使用
CUDA_VISIBLE_DEVICES=0 python3 eval_cwm_baseline.py \
    --data_dir data/ \
    --checkpoint_dir checkpoints_cwm_rank32/best \
    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
    --output eval_results/cwm_rank32_eval/eval_cwm_rank32_results.json \
    --batch_size 16 \
    --max_seq_length 2048 \
    --max_new_tokens 64 \
    --save_predictions

# 参数说明:
#   --data_dir data/               → 读取 data/cwm_test.jsonl (1890 samples, function-level)
#   --checkpoint_dir ...rank32/best → 训练自动保存的最优 checkpoint
#   --model_name                   → Qwen3-4B 本地路径 (base model for LoRA merge)
#   --output                       → 结果 JSON 输出路径
#   --batch_size 16                → 与 baseline 一致
#   --max_seq_length 2048          → 与 baseline 一致
#   --max_new_tokens 64            → 与 baseline 一致
#   --save_predictions             → 保存逐条预测 (用于 error analysis)
#
# 如果 best/ 不存在，改用最后一个 checkpoint:
#   --checkpoint_dir checkpoints_cwm_rank32/checkpoint-1434
