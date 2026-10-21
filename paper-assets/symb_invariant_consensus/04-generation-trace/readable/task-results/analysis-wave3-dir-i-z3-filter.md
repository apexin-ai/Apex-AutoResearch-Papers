# analysis wave3 dir i z3 filter

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wave3-dir-i-z3-filter_20260520T090105_result.json`
- **Structured JSON:** [`c71aaaf0d83327f3e329.json`](../../sessions/c7/c71aaaf0d83327f3e329.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Direction I: Z3 Trace Filter 结果

| 指标 | 值 |
|------|-----|
| 问题数 | 204 |
| 总 traces | 2448 |
| **SC baseline** | **111/204 = 54.41%** |
| **Filtered-SC** | **110/204 = 53.92%** |
| **Delta** | **-0.49%** |

### Status 分布
- SAT: 2220 (90.7%)
- UNSAT: 142 (5.8%)
- EMPTY: 61 (2.5%)
- PARSE_ERROR: 25 (1.0%)

### 过滤质量分析
- 被过滤的 UNSAT traces 中：正确答案 58，错误答案 56，空答案 28
- **Filter precision = 49.12%** — 几乎等于随机，说明 UNSAT 并不能区分正确/错误 trace
- 仅 7 个问题的投票结果发生变化：3 个改善，4 个恶化

### Per-question UNSAT 分布
- 0 UNSAT: 115 题（56%的题没有任何 trace 被过滤）
- 1 UNSAT: 58 题
- 2+ UNSAT: 31 题

### 结论

**Z3 per-trace 一致性检查作为过滤信号无效。** 原因：
1. 过滤率仅 5.8%，影响面太小
2. Filter precision ≈ 50%（随机水平），UNSAT 并不偏向错误 trace
3. LLM 产生的约束中，内部矛盾跟推理正确性无显著关联——可能是约束提取本身的噪声导致矛盾，而非推理逻辑错误

结果保存在 `westd-25068:/root/symb_invariant_consensus/results/direction_i_z3_filter/results.json`。

---
