# prep next experiments cuda0 cuda1 cuda2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_next_experiments_cuda0_cuda1_cuda2_20260521T172841_result.json`
- **Structured JSON:** [`efc9fff14b769cadab0e.json`](../../sessions/ef/efc9fff14b769cadab0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已就绪，直接汇报结果。

---

## 产出报告

### 1. ρ=0.6 random shuffle 数据 ✅ 已就绪

- **路径**: `/root/provenance_weight_training/data/scored_data_rho06_random_shuffle.jsonl`
- **行数**: 371499（与原始 rho06 一致）
- **方法**: 全局 shuffle q_score 列（seed=42），text 和其他字段不变
- **原始 q_score 统计**: min=0.0002, max=1.0000, mean=0.6243
- **验证**: 第一行 text 与原始 rho06 相同，q_score 从 0.641 → 0.054（已打乱）

### 2. eval 命令模板

用户提供的模板参数名有误。`eval_perplexity.py` 的正确参数（参考 `eval_rho06_ppl.sh`）：

```bash
# bs16_adaptive_tau07_seed42
python eval_perplexity.py \
    --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau07_seed42/final \
    --data_path data/human/eval_holdout.jsonl \
    --output_path /root/autodl-tmp/provenance_weight_training/output/eval_results/bs16_adaptive_tau07_seed42_eval.json

# bs16_uniform_seed42
python eval_perplexity.py \
    --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/bs16_uniform_seed42/final \
    --data_path data/human/eval_holdout.jsonl \
    --output_path /root/autodl-tmp/provenance_weight_training/output/eval_results/bs16_uniform_seed42_eval.json
```

**与用户模板的差异**:
- `--model_path` → 应为 `--checkpoints`
- `--eval_data` → 应为 `--data_path`
- `--stride 1024` → 不存在（hardcoded 为 max_length//2 = 1024）
- `--bf16` → 不存在（脚本固定用 fp16）

**bs16 训练进度**: adaptive 在 step 5579/6103（~91%），uniform 在 5079/6103（~83%）。训练脚本自带 eval_loss（每 500 步），`final/` 目录待训练结束后自动生成。

### 3. ρ=0.6 random reweight 训练命令建议

基于 `run_rho06_adaptive.sh` 模板，改用 shuffled 数据：

```bash
#!/bin/bash
# rho06_random_reweight: ρ=0.6 random reweight ablation
# Uses globally-shuffled q_scores to prove detector signal is load-bearing
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export WANDB_MODE=disabled
cd /root/provenance_weight_training

python training/pretrain_weighted.py \
    --data_path data/scored_data_rho06_random_shuffle.jsonl \
    --eval_data_path data/human/eval_holdout.jsonl \
    --output_dir /root/autodl-tmp/provenance_weight_training/output/models/rho06_random_reweight_seed42 \
    --model_name models/Qwen/Qwen3-0.6B \
    --weighting_method adaptive \
    --tau 0.8 \
    --n_min 2 \
    --contamination_ratio 0.6 \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --seed 42 \
    --eval_steps 500 \
    --save_steps 500 \
    --logging_steps 10 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model

echo "DONE: rho06_random_reweight seed42"
```

**注意**: ρ=0.4 的 `run_random_reweight_seed42.sh` 用的是 `--weighting_method random`（U(0,2) 随机权重，完全不看 q_score）。上面的命令改用 `--weighting_method adaptive` + 预打乱的 q_score，是更强的消融——控制了分数分布，只破坏 score-text 相关性。如果需要与 ρ=0.4 完全一致的方法论，也可以改为 `--weighting_method random --data_path data/scored_data_rho06.jsonl`。

---
