# analysis qwen14b s123 checkpoint check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_s123_checkpoint_check_20260523T151238_result.json`
- **Structured JSON:** [`1b4926eabfa350f79321.json`](../../sessions/1b/1b4926eabfa350f79321.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Checkpoint 可用性
**存在。** 路径：`/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt`（223MB predictor checkpoint，非完整模型）。s42 和 s456 的 checkpoint 也都在。

### 已有 eval 结果
s123 已有 downstream eval（`qwen14b_kl30_s123_eval_v4`），包含 wikitext2/arc/winogrande/hellaswag/piqa/mmlu，**但缺少 GSM8K**。s42 和 s456 的 GSM8K 已跑完。

### 磁盘空间
- 根分区：30G 用了 22G，剩 8.7G（72%）— eval 不写大文件，足够
- 数据盘：250G 用了 70G，剩 181G — 充裕
- Qwen-14B 模型已在 `/root/autodl-tmp/models/qwen2.5-14b/`

### 建议重跑命令
参照 s42/s456 的配置（`teal_global`, sparsity 0.3, uniform allocation, batch_size 8）：

```bash
cd /root/distill_sparse_swiglu && nohup python src/benchmark_eval.py \
  --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt \
  --model /root/autodl-tmp/models/qwen2.5-14b/ \
  --tasks gsm8k \
  --sparsity_mode teal_global \
  --sparsity_target 0.3 \
  --allocation uniform \
  --gpu 0 \
  --batch_size 8 \
  --exp_id qwen14b_kl30_s123_gsm8k \
  > logs/qwen14b_kl30_s123_gsm8k.log 2>&1 &
```

---
