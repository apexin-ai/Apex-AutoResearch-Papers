# code exp 013 ablation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-013-ablation_20260516T063525_result.json`
- **Structured JSON:** [`519631ac7a9323c612e6.json`](../../sessions/51/519631ac7a9323c612e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常，JSON 输出格式完整：包含 methods 汇总、agreement 统计、per_problem 逐题详情。

产出：
- **脚本**：`/root/symb_invariant_consensus/scripts/constraint_ablation.py`（~340 行）
- **验证**：`--help` 正常，实际数据试跑正常，JSON 输出 `results/constraint_ablation.json`

当前结果（近似模式）：87 题中三种方法准确率均为 71.3%，与 SC 相同。这是因为近似模式下，排除的约束权重太小（每题仅 1 个排除约束，权重 3-6）无法改变排名。这是合理结果——当 contradiction rate 仅 ~2.6% 时，聚合方法的选择对准确率影响微小。

要获得精确的 count-only 和 random-weight 结果，需要：
1. 修改 pipeline 保存中间约束数据（`UniqueConstraint` 的 `z3_formula_str`、`weight`、`source_traces`）
2. 生成 constraint cache JSON
3. 用 `--constraint-cache` 参数运行脚本

---
