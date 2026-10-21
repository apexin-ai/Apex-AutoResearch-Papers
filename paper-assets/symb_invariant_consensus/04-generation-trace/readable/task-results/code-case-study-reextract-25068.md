# code case study reextract 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_case-study-reextract-25068_20260518T094639_result.json`
- **Structured JSON:** [`6c7cce6101a9eb4ede67.json`](../../sessions/6c/6c7cce6101a9eb4ede67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 已关闭。

## 结果汇总

| 问题 | Gold | SICA | SC | Unique Constraints | Excluded |
|------|------|------|----|--------------------|----------|
| folio_134 | Unknown | True ✗ | True ✗ | 22 | 0 |
| PW_AttNoneg-OWA-D5-1066_Q6 | False | \text{unknown} ✗ | \text{unknown} ✗ | 31 | 2 |
| PW_RelNeg-OWA-D5-903_Q6 | False | \text{unknown} ✗ | \text{true} ✗ | 72 | 1 |

三个问题 SICA 和 SC 都未答对 gold answer。主要原因是答案格式不统一（`True` vs `\text{True}` vs `\text{true}`），导致投票被分裂。例如 folio_134 的 SC 分布：`True:5, \text{True}:5, \text{true}:1, \text{uncertain}:1`，如果做格式归一化，True 系列共 11/12 票，结果会不同。

关键数据已保存到 `/root/symb_invariant_consensus/results/case_study_constraints.json`（162KB），包含每条 trace 的完整 constraints（type, expression, z3_formula, source_step）、trace_snippet、去重后的 unique_constraints、MaxSAT satisfied/excluded 列表等。这些是 reviewer 要求的 LLM-actually-extracted constraints。

---
