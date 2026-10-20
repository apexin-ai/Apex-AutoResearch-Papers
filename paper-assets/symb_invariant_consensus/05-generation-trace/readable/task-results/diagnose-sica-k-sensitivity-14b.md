# diagnose sica k sensitivity 14b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sica_k_sensitivity_14b_20260517T021118_result.json`
- **Structured JSON:** [`69d9d57517a64dbbb080.json`](../../sessions/69/69d9d57517a64dbbb080.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验实际完成，EXIT_CODE=129 为假失败**（与 sica_expanded_14b 相同模式）。

### 各 K 值结果

| K | SICA | SC | Δ |
|---|------|-----|---|
| 6 | 73.3% | 73.3% | 0.0 |
| 8 | 73.3% | 75.0% | -1.7 |
| 11 | 73.3% | 73.3% | 0.0 |
| 12 | 70.0% | 75.0% | -5.0 |
| 16 | 71.7% | 75.0% | -3.3 |
| 20 | 70.0% | 73.3% | -3.3 |

### 判断

- SICA 在所有 K 值上 ≤ SC，增大 K 反而使 SICA 退化（SC 保持稳定）
- 应将 cron conclusion 从 `failed` 改为 `negative`（实验完成，结果为负面）
- 这进一步确认 constraint-based weighting 机制 vacuous，与 exp-013 constraint ablation 结论一致

已保存诊断报告到 memory.md 和 artifact `art_20260517_2c1577`。

---
