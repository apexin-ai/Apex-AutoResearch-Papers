# analysis cluster ci fix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cluster-ci-fix_20260516T063118_result.json`
- **Structured JSON:** [`eecd9242e099b9ff014c.json`](../../sessions/ee/eecd9242e099b9ff014c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改内容：

- 在 `cluster_robust_ci.py` 中添加 `PRED_PATH_OVERRIDE` dict，将 `deepseek_full_trace` 指向 v3 路径 (`deepseek_full_trace_seed42_v3/final/predictions.jsonl`)
- 重跑后 `deepseek_full_trace` accuracy = **79.16%**（之前 10.59%），其余 11 个条件数值不变
- 结果已保存到服务器 `/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/cluster_robust_ci.json` 和本地 `artifacts/cluster_robust_ci.json`

---
