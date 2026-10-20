# analysis vote diversity prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vote_diversity_prep_20260515T220218_result.json`
- **Structured JSON:** [`1078c4cf726bc5ff7af2.json`](../../sessions/10/1078c4cf726bc5ff7af2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本正常运行。结果确认：

**22 题中 16 题有有效投票，multi-candidate rate = 0.0%** — 所有 16 题的 K 条 trace 都只产生 1 个候选答案（其余 6 题答案提取完全失败，0 票）。

关键数字：
- `#Cand=1` 贯穿所有有效题目，SICA≡SC，gap=0pp
- 约束提取仍有价值：19/22 题提取了约束，exclusion rate 38.7%，但由于只有 1 个候选答案，MaxSAT 的排除操作不改变最终选择
- 6 题（idx 1,7,8,10,13,14）投票数为 0——答案提取完全失败，注意 idx 4,6,9,11,12 投票数远低于 K=12（1~10 票），说明部分 trace 也提取失败

脚本已保存在 `/root/symb_invariant_consensus/analyze_vote_diversity.py`，用法：`python analyze_vote_diversity.py [results_json_path]`。

---
