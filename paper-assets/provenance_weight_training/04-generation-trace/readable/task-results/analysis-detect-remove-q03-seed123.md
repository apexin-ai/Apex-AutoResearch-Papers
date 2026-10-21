# analysis detect remove q03 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detect_remove_q03_seed123_20260519T014503_result.json`
- **Structured JSON:** [`40666e4622749bf0a4ab.json`](../../sessions/40/40666e4622749bf0a4ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果总结

| | seed42 | seed123 | diff |
|---|---|---|---|
| PPL | 17.25 | 17.25 | 0.00 |
| Loss | 2.848 | 2.8479 | -0.0001 |
| Tokens | 4,077,068 | 4,077,068 | 0 |
| Steps | 6,103 | 6,103 | 0 |

Cross-seed 一致性极好：PPL 完全一致 (17.25)，loss 差异仅 0.0001。q03 作为 U-shape 曲线最优点在两个 seed 下完全可复现，不是 seed42 偶然结果。

---
