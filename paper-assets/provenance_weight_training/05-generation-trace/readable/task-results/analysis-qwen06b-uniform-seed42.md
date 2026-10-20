# analysis qwen06b uniform seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen06b_uniform_seed42_20260517T222205_result.json`
- **Structured JSON:** [`1bd7911dc1b332d1ed6d.json`](../../sessions/1b/1bd7911dc1b332d1ed6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE/success。

**总结：**

| 指标 | 值 |
|------|------|
| eval_loss_holdout | 2.8733 |
| eval_ppl_holdout | **17.695** |
| eval_holdout_tokens | 4,077,068 |
| train_loss | 7.989 |
| train_runtime | 12,860s (~3.6h) |
| checkpoint | `/root/autodl-tmp/provenance_weight_training/output/models/qwen06b_uniform_seed42_v2/final` |
| log | `/root/runs/provenance_weight_training/qwen06b_uniform_seed42.log` (on westd-41312) |

**对比旧 uniform baseline (PPL=17.694)**：新值 17.695，差异 < 0.001，完全可复现。去掉 inline eval 不影响训练结果，确认 clean baseline 有效。

---
