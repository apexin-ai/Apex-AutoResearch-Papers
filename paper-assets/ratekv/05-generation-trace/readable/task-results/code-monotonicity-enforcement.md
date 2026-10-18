# code monotonicity enforcement

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_monotonicity_enforcement_20260514T005636_result.json`
- **Structured JSON:** [`60952fc5acbe4898d909.json`](../../sessions/60/60952fc5acbe4898d909.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

## 任务 1 结论：Pareto filtering 行为

当 delta_4bit > delta_2bit（非单调）时：

- **`_build_pareto`**（`solve_mckp` 使用）：4-bit 被移除。Pareto front 只剩 {2-bit, 8-bit, 16-bit}，该 head 失去中间选项。Greedy solver 从 8-bit 直接跳到 2-bit。
- **`_build_actions_no_pareto`**（`solve_mckp_constrained` 使用）：不做 Pareto filtering，4-bit 保留。但 greedy 计算 4→2 downgrade 时得到**负效率**（distortion 下降），会被视为"免费午餐"优先执行——基于噪声的虚假优化。
- **`solve_greedy_ratequant`**：独立逻辑，逐步降级 16→8→4→2，也会受影响——4→2 的 marginal cost 为负，优先被选中。

## 任务 2-4 完成

- `enforce_monotonicity()` 已添加到 `solver.py` 末尾，不修改任何现有函数签名/行为
- 对比脚本 `run_monotonicity_comparison.py` 已创建，等 `ppl_profiles_hires.json` 生成后即可运行
- 设计为 opt-in：调用方在传入 solver 前显式调用 `enforce_monotonicity(profiles)`，不改变默认行为

---
