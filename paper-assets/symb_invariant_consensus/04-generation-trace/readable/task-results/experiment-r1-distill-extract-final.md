# experiment r1 distill extract final

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r1-distill-extract-final_20260521T171123_result.json`
- **Structured JSON:** [`dc3a52ec8a1ffc377d26.json`](../../sessions/dc/dc3a52ec8a1ffc377d26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All metrics computed. Here's the 93-题 vs 204-题 comparison table:

| Metric | 93 题 | 204 题 | Δ |
|---|---|---|---|
| **SC Accuracy** | 0.7527 | 0.7451 | −0.76 pp |
| **SICA Accuracy** | 0.7849 | 0.7647 | −2.02 pp |
| **Δ(SICA−SC)** | +3.22 pp | +1.96 pp | −1.26 pp |
| **Mean BR** | 2.97 | 2.85 | −0.12 |
| **Median BR** | 2.00 | 2.00 | 0.00 |
| **Process-κ (TF-IDF)** | 0.2386 | 0.2477 | +0.009 |
| **Answer Fleiss' κ** | 0.7030 | 0.6944 | −0.009 |

要点：
- 从 93→204 题，SICA 依然优于 SC，但 Δ 从 +3.22pp 缩到 +1.96pp
- 两个 accuracy 都略降，说明新增 111 题整体偏难
- BR、Process-κ、Fleiss' κ 基本稳定
- Extraction rate 93.3%，14602 total constraints（去重后 8653）

---
