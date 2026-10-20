# diagnosis qwen3 pw seed123

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_qwen3-pw-seed123_20260524T112558_result.json`
- **Structured JSON:** [`43c2082e414939904306.json`](../../sessions/43/43c2082e414939904306.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：success**

| 指标 | 值 |
|------|-----|
| N | 600 |
| SICA accuracy | 86.50% |
| SC accuracy | 85.17% |
| Δ(SICA−SC) | +1.33% |
| extraction_rate | 99.67% |
| contradiction_rate | 0.37% |

注意：SC 值使用 `Counter.most_common()` tiebreaking（原始值），待 post-hoc 修正。

假设"Δ(SICA-SC)≤0"被否定——seed123 上 SICA 仍优于 SC +1.33pp。

Registry 已更新为 DONE/success，cron 已删除。

---
