# analysis sc baseline qwen3 discrepancy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sc-baseline-qwen3-discrepancy_20260520T175251_result.json`
- **Structured JSON:** [`ff4424a7a743ee683491.json`](../../sessions/ff/ff4424a7a743ee683491.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

**根因：Dir-I2 和 Dir-I3 用的是不同的 Qwen3-14B 推理配置，不是同一个 baseline。**

- **Dir-I2 (83.82%)** = `exp027_qwen3_14b_nonthinking` — 非思考模式
- **Dir-I3 (86.27%)** = `exp028b_qwen3_thinking_folio204` — 思考模式（带 `&lt;think>` block）

两个值都是各自配置下的正确结果，没有数据错误或代码 bug。

逐题对比：17 个 correctness 分歧（20 个 prediction 分歧），思考模式净赢 5 题（+11 -6）。非思考模式的主要弱点是倾向于过度预测 Unknown（11 个失败中 9 个是这样）。

报告已写入：
- `/root/symb_invariant_consensus/results/sc_qwen3_discrepancy_analysis/report.json`
- `/root/symb_invariant_consensus/results/sc_qwen3_discrepancy_analysis/report.md`

---
