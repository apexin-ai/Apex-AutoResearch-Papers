# code uniform allocation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_uniform_allocation_20260516T034600_result.json`
- **Structured JSON:** [`ea4fd18b91d7946be67b.json`](../../sessions/ea/ea4fd18b91d7946be67b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全成功。修改后的 `torch_dtype` 警告无害（transformers 新版 deprecation）。

## 结果总结

### 修改文件
`/root/distill_sparse_swiglu/src/lm_eval_sparse.py` — 增加了 `_uniform_topk_masks()`、`compute_layer_scores()`、`teal_masks()` 调度函数、`print_comparison()`，新增参数 `--allocation_strategy`、`--compare`、`--device`。

### Per-layer sparsity 对比 (target=30%)

Global top-k 的分布极不均匀，正如预期：
- **早层 (0-6)**: 17-25% sparsity（保留太多神经元）
- **中层 (15-19)**: 12-19% sparsity（几乎不裁剪）
- **后层 (26-31)**: 41-70% sparsity（Layer 31 高达 **70.3%**！）

Uniform 模式每层精确 30.1%，model-level 两者完全一致（30.0%）。

### 正式 eval 命令行

**30% sparsity:**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu
# Uniform
CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 \
  nohup python -u src/lm_eval_sparse.py \
    --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
    --predictor_path checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt \
    --sparsity_target 0.3 \
    --allocation_strategy uniform \
    --compare \
    --tasks arc_challenge,winogrande,mmlu,gsm8k \
    --output_path results/uniform_30pct \
    > /tmp/eval_uniform_30.log 2>&1 &
```

**50% sparsity:**
```bash
CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 \
  nohup python -u src/lm_eval_sparse.py \
    --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
    --predictor_path checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt \
    --sparsity_target 0.5 \
    --allocation_strategy uniform \
    --compare \
    --tasks arc_challenge,winogrande,mmlu,gsm8k \
    --output_path results/uniform_50pct \
    > /tmp/eval_uniform_50.log 2>&1 &
```

注意：50% 条件可能需要用对应 sparsity 的 predictor checkpoint（如果有 `kl_sparsity50_*`），用 30% 的 predictor 跑 50% target 可能不是最优的。

---
