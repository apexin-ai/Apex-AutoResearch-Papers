# analysis gpt2 uniform seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2_uniform_seed42_20260518T230357_result.json`
- **Structured JSON:** [`c3c14c726b2a58659b5f.json`](../../sessions/c3/c3c14c726b2a58659b5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

| 项目 | 值 |
|---|---|
| **训练状态** | 正常完成 (EXIT_CODE=0) |
| **训练步数** | 6103 steps, 3h32m |
| **Final train loss** | 7.989 |
| **Holdout eval PPL** | **17.69** |
| **Holdout eval loss** | 2.8733 |
| **Checkpoint** | `/root/autodl-tmp/provenance_weight_training/output/models/gpt2_uniform_seed42/final` |

值得注意：GPT-2 uniform baseline 的 holdout PPL (17.69) 与之前 `qwen06b_uniform_seed42_v2` (17.69) 几乎完全一致，这符合预期——两者都是 uniform weighting，数据源略有不同但底层模型相同。Registry 已更新为 DONE/success。

---
