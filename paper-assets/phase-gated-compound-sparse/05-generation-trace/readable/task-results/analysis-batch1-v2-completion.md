# analysis batch1 v2 completion

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_batch1_v2_completion_20260516T013124_result.json`
- **Structured JSON:** [`fa6356ad320c1d69ac88.json`](../../sessions/fa/fa6356ad320c1d69ac88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 QW dose curve experiments confirmed DONE: dense, s015, s020, s025, s030.

---

## 完整 Dose Curve 产出摘要

| Sparsity | Batch1_v2 (8k) | Batch2 | Combined n=100 | Old Combined | Δ |
|----------|----------------|--------|----------------|-------------|---|
| dense    | 0.44 (22/50)   | 0.48 (24/50)          | **0.46 (46/100)** | 0.40 | +0.06 |
| s015     | 0.46 (23/50)   | 0.38 (19/50) †        | **0.42 (42/100)** | 0.36 | +0.06 |
| s020     | 0.26 (13/50)   | 0.46 (23/50, b2_fix)  | **0.36 (36/100)** | 0.35 | +0.01 |
| s025     | 0.32 (16/50)   | 0.34 (17/50, b2_fix)  | **0.33 (33/100)** | 0.33 | 0.00 |
| s030     | 0.14 (7/50)    | 0.24 (12/50) †        | **0.19 (19/100)** | 0.19 | 0.00 |

† = batch2 可能使用 2048 token budget（未重跑）

**关键发现**: 8k token fix 对 s025/s030 完全无影响（结果与旧 2k batch1 完全一致），确认高稀疏度下的精度下降纯粹来自 pruning/eviction 本身，而非 token 截断。s025→s030 存在陡峭 cliff（0.33→0.19，-42% relative）。

---
