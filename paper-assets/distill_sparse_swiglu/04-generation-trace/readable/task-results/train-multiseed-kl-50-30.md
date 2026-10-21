# train multiseed kl 50 30

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_multiseed_kl_50_30_20260517T095510_result.json`
- **Structured JSON:** [`00849381cdc2e9bc8416.json`](../../sessions/00/00849381cdc2e9bc8416.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Run 1 训练已启动，模型加载完毕，GPU 0 占用 18GB。

日志文件：`/root/distill_sparse_swiglu/logs/multiseed_kl_20260517_175809.log`

4 个 run 串行执行中（KL 50% s123 → KL 50% s456 → KL 30% s123 → KL 30% s456），预计约 1.5h 完成。每个 run 训练完自动接 eval。

已有 seed=42 基线（供对照）：

| Config | Seed | PPL | ARC-c | WG | MMLU | GSM8K |
|--------|------|-----|-------|-----|------|-------|
| KL 50% | 42 | 11.79 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |
| KL 30% | 42 | 8.98 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |

注意：KL 30% s42 实际 PPL=8.98，非 8.36。

完成后结果会自动写入 `results/benchmark/kl_{50,30}pct_s{123,456}/results.json`。需要我过一会儿回来检查进度吗？

---
