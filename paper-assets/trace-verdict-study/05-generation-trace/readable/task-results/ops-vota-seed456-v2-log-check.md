# ops vota seed456 v2 log check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_vota_seed456_v2_log_check_20260515T205012_result.json`
- **Structured JSON:** [`4585e1dc60cbb00851c8.json`](../../sessions/45/4585e1dc60cbb00851c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成，cron 已删除。

## 结果

**vota_seed456_v2 训练成功。**

| 指标 | seed456 | seed42 |
|------|---------|--------|
| Accuracy | **99.08%** (CI: 98.5%-99.6%) | 99.41% |
| fail F1 | **0.984** | — |
| pass F1 | **0.994** | — |
| fail Precision | 0.969 | — |
| fail Recall | 1.000 | — |

seed456 accuracy (99.08%) 比 seed42 (99.41%) 低 0.33pp，均在 CI 范围内，seed robustness 确认。进程退出码 129 (SIGHUP) 但评估已完成、结果已持久化，无影响。

---
