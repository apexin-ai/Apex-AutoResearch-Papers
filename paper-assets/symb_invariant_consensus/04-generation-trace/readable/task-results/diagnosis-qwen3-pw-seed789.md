# diagnosis qwen3 pw seed789

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_qwen3-pw-seed789_20260524T112701_result.json`
- **Structured JSON:** [`4c897cad4a564a6ffe32.json`](../../sessions/4c/4c897cad4a564a6ffe32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论：**SUCCESS**

| 指标 | 值 |
|------|-----|
| SC accuracy | 85.50% (513/600) |
| SICA accuracy | 85.67% (514/600) |
| Δ(SICA-SC) | **+0.17%** |
| n_problems | 600 |
| wall_time | 17.2h |
| extraction_rate | 99.76% |
| contradiction_rate | 0.34% |

注意：假设 Δ(SICA-SC)≤0 **未被验证**——seed789 显示 SICA 微高于 SC（+0.17pp，1题之差）。结合 Counter.most_common() tiebreaking 问题，这个差异可能在噪声范围内。

- Registry 已更新为 DONE/success + metrics
- Cron 已删除

---
