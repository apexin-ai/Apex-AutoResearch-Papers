# analysis exp033 rebin entropy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp033-rebin-entropy_20260518T224247_result.json`
- **Structured JSON:** [`5a286a9d5d79146cd994.json`](../../sessions/5a/5a286a9d5d79146cd994.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v2 JSON 已保存。结果如下：

## Exp-033 Per-Problem 分桶统计（统一边界 [0, 0.5) / [0.5, 1.0) / [1.0+)）

| Entropy Bin | n | % | SC Acc | SICA Acc | Delta (pp) | Overrides | Correct | Wrong | Override Precision |
|---|---|---|---|---|---|---|---|---|---|
| Low [0, 0.5) | 65 | 31.9% | 0.7692 | 0.7692 | +0.00 | 0 | 0 | 0 | — |
| Medium [0.5, 1.0) | 66 | 32.4% | 0.5455 | 0.5909 | +4.55 | 4 | 3 | 1 | 0.7500 |
| High [1.0, +inf) | 73 | 35.8% | 0.3425 | 0.4384 | **+9.59** | 13 | 9 | 4 | 0.6923 |
| **Overall** | **204** | **100%** | **0.5441** | **0.5931** | **+4.90** | **17** | **12** | **5** | **0.7059** |

### 与 constraint_precision 分析对比

High entropy 区间 delta = **+9.59pp**，与之前 constraint_precision 分析的 ~+9.6pp 完全一致。

旧边界 vs 新边界的变化：
- 旧 Medium [0.5, 1.2) 有 89 题，旧 High [1.2, +inf) 有 50 题
- 新 Medium [0.5, 1.0) 有 66 题，新 High [1.0, +inf) 有 73 题
- 将 23 题从旧 Medium 移到新 High，High 区间从 50→73 题，delta 从 +10.00pp 略降至 +9.59pp，override precision 从 0.6364 升至 0.6923
- Low 区间不变（边界相同）

---
