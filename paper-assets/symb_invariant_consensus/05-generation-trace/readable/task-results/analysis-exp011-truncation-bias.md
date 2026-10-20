# analysis exp011 truncation bias

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp011-truncation-bias_20260517T084325_result.json`
- **Structured JSON:** [`45f122bfa0df215bd778.json`](../../sessions/45/45f122bfa0df215bd778.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Truncation Bias 分析结果

### 1. Discordant Pairs 列表

| Problem ID | Winner | GT | SICA答案 | SC答案 | Truncated |
|---|---|---|---|---|---|
| ProofWriter_RelNoneg-OWA-D5-1036_Q11 | SICA | True | True | Unknown | 0/12 |
| ProofWriter_RelNeg-OWA-D5-856_Q19 | SICA | Unknown | Unknown | False | **3/12** |
| folio_002 | SICA | True | True | False | 0/12 |
| folio_014 | SICA | False | False | Unknown | 0/12 |
| folio_027 | SICA | Unknown | Unknown | True | 0/12 |
| ProofWriter_RelNoneg-OWA-D5-709_Q12 | SC | False | Unknown | False | 0/12 |

### 2. Truncation 与 Discordant 的重叠

**6 个 discordant pairs 中只有 1 个含 truncated traces（16.7%）**。5/5 的 SICA-win 中有 4 个完全没有截断，1 个 SC-win 也没有截断。

截断几乎不影响 discordant pairs。

### 3. Truncated vs Non-truncated 准确率

| 分组 | n | SICA | SC | Delta |
|---|---|---|---|---|
| 有截断 | 16 | 68.75% | 62.50% | +6.25pp |
| 无截断 | 44 | 65.91% | 59.09% | **+6.82pp** |

SICA 增益在无截断题目上反而更大（+6.82pp vs +6.25pp）。Discordant 分布：无截断组贡献了 4/5 SICA-wins 和 1/1 SC-win。

### 4. 截断严重度

- 总截断率很低：44 条 traces / 720 总条 = **6.1%**，平均每题 0.7/12
- 16/60 题有截断（26.7%），而非原始 summary 暗示的 44/60 题（44 是截断 trace 总条数，不是题数）
- Constraint extraction 质量两组几乎一致（dedup ratio 28.85% vs 30.11%）

### 5. 答案偏向

截断组 SC 投票中 True 比例偏高（46.7% vs 27.6%），Unknown 偏低（32.8% vs 52.6%），但这反映的是题目构成差异，非截断 artifact——因为 SICA 在两组的增益几乎一致。

### 结论

1. **Truncation 不是 confound**：SICA 的 +6.67pp 增益主要来自无截断的题目（4/5 SICA-wins 在 clean 题上），截断组和非截断组的 delta 方向一致且幅度接近。
2. 原始报告中 "44/60 题有 truncated traces" 是误读——实际是 44 条 traces 被截断（分布在 16 题中），整体截断率仅 6.1%。
3. **不需要用更大 max-tokens 重跑 exp-011** 来验证 SICA 增益的真实性。如果要重跑，动机应该是提升绝对准确率（减少 none extraction），而非消除 truncation bias。

---
