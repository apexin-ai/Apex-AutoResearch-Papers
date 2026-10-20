# analysis cwm seed123 check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm-seed123-check_20260512T131341_result.json`
- **Structured JSON:** [`1abaf4b4dae271ae5cde.json`](../../sessions/1a/1abaf4b4dae271ae5cde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cwm-seed123 完成，registry 已更新为 DONE/success。Cron 已不存在（无需清除）。

**最终 metrics：**

| 指标 | 值 |
|------|-----|
| overall_accuracy | **87.20%** |
| pass_f1 | 86.95 |
| fail_f1 | 87.44 |
| exact_match_rate | 84.44% |
| vs majority baseline | +35.45pp |

与 cwm-baseline (seed=42, 87.51%) 对比：accuracy 差 0.31pp，基本一致，确认 4B CWM 性能稳定。

---
