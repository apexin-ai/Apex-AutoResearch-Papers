# analysis sc tiebreak mcnemar recalc

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sc-tiebreak-mcnemar-recalc_20260520T141440_result.json`
- **Structured JSON:** [`89343563881ec80e57f7.json`](../../sessions/89/89343563881ec80e57f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是完整结果。

---

## 结果

### 1. SC Tiebreaking 对比 (exp033 default seed)

| 方法 | 正确数 | 准确率 |
|------|--------|--------|
| SC (dict-order, 旧) | 111/204 | 54.41% |
| SC (alphabetical, 新) | 114/204 | **55.88%** |

7 道 tie 题发生变化：

| 问题 | Gold | Dict→Alpha | 投票分布 | 结果 |
|------|------|------------|----------|------|
| folio_42 | True | Unknown→**True** | Unknown:5, True:5 | 错→对 |
| folio_65 | True | True→**False** | True:5, False:5, Unknown:2 | 对→错 |
| folio_83 | False | Unknown→**False** | Unknown:5, False:5 | 错→对 |
| folio_99 | Unknown | Unknown→**True** | Unknown:5, True:5 | 对→错 |
| folio_100 | True | Unknown→**True** | Unknown:4, True:4 | 错→对 |
| folio_157 | False | Unknown→**False** | Unknown:5, False:5 | 错→对 |
| folio_163 | False | Unknown→**False** | Unknown:5, False:5 | 错→对 |

净变化: +5 correct, -2 correct → **+3 net**

### 2. R Combo 准确率（不变）

| 策略 | 正确数 | 准确率 |
|------|--------|--------|
| Combo w=1 | 118/204 | 57.84% |
| Combo w=3 | 120/204 | 58.82% |

### 3. McNemar 重算

| 对比 | b (SC对,combo错) | c (SC错,combo对) | p-value |
|------|---|---|---|
| **旧** SC vs w=1 | 1 | 8 | **0.0391*** |
| **新** SC vs w=1 | 0 | 4 | 0.1250 |
| **旧** SC vs w=3 | 6 | 15 | 0.0784 |
| **新** SC vs w=3 | 5 | 11 | 0.2101 |

**关键变化**: SC 从 54.41%→55.88% 后，combo 相对 SC 的改进变小，w=1 的 McNemar 从显著 (p=0.039) 变为不显著 (p=0.125)。w=3 本来就不显著，p 值进一步增大。

### 4. 其他 seed SC 值

| 实验 | 报告 SC | Dict-order | Alphabetical | Tiebreaking 类型 | 需要更新？ |
|------|---------|------------|--------------|-----------------|-----------|
| exp033 default | 54.41% | 54.41% | 55.88% | dict-order | **是 → 55.88%** |
| exp067 seed789 | 54.41% | 55.88% | 54.41% | alphabetical | 否 |

**exp074c (seed123, ICG)** SC=57.35%, **exp074d (seed456, ICG)** SC=55.88% — 这些是 ICG 实验，SC baseline 数值与用户提到的 Table 1 (s123=54.41%, s456=55.88%) 不一致。没有找到独立的 Mistral FOLIO seed123/seed456 普通 SICA 实验目录。需要确认 Table 1 中 s123 和 s456 的 SC 值来源。

### 5. 补充：如果 combo tiebreaking 也统一为字母序

| 策略 | 原始 (dict tiebreak) | 字母序 tiebreak |
|------|---------------------|----------------|
| Combo w=1 | 118/204 (57.84%) | 115/204 (56.37%) |
| Combo w=3 | 120/204 (58.82%) | 120/204 (58.82%) |

w=1 会降 3 个点，因为 combo 投票中也有 tie 情况。这是一个需要决定的点：是否 combo 也用字母序 tiebreaking。

---
