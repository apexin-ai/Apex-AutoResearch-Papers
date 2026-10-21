# eval detect remove q03 epoch matched seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_detect_remove_q03_epoch_matched_seed42_20260518T233036_result.json`
- **Structured JSON:** [`c55576a97b838c8b618e.json`](../../sessions/c5/c55576a97b838c8b618e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，实验标记为 DONE/success。

## 结果汇总

| 实验 | PPL | Loss |
|------|-----|------|
| **epoch-matched q03** (本次) | **17.74** | 2.876 |
| epoch-matched q05 | 17.65 | — |
| epoch-matched q05 seed123 | 17.66 | — |
| epoch-matched q05 seed456 | 17.66 | — |
| adaptive baseline | 17.651 | — |
| multi-epoch q03 | 17.25 | — |

**关键发现：** q03 epoch-matched PPL = 17.74，比 q05 epoch-matched (17.65) **高 0.09**，方向相反于预期。在固定训练 budget 下，更严格的过滤（q03）反而略微伤害了性能，可能因为过度删除 borderline 样本减少了数据多样性。multi-epoch q03 (17.25) 的优势完全来自更多训练 epoch（3.2x vs 2.4x），而非更高的单 token 数据质量。

---
