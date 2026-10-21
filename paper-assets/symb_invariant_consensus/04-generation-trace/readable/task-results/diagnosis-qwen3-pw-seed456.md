# diagnosis qwen3 pw seed456

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_qwen3-pw-seed456_20260524T112631_result.json`
- **Structured JSON:** [`9948c8f425c64621c2a8.json`](../../sessions/99/9948c8f425c64621c2a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论：**success**

| 指标 | 值 |
|------|-----|
| SC accuracy | 84.50% (507/600) |
| SICA accuracy | 86.83% (521/600) |
| Δ(SICA-SC) | **+2.33pp** |
| n_questions | 600 |
| extraction_rate | 99.6% |
| contradiction_rate | 0.42% |
| wall_time | 17.3h |

注意：SC 值可能受 `Counter.most_common()` tiebreaking 影响（已知 run_full_mvp.py 问题），已在 metrics note 中记录。

已完成：
- Registry → DONE, conclusion=success, metrics 已记录
- Cron 监控已删除

---
