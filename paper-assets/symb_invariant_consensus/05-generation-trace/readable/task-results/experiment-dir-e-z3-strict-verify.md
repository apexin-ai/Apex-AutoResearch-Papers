# experiment dir e z3 strict verify

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-e-z3-strict-verify_20260520T161411_result.json`
- **Structured JSON:** [`c8e1ce24b01997388bd8.json`](../../sessions/c8/c8e1ce24b01997388bd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dir-E Strict Verification 结果 (30题 Pilot)

| 指标 | 值 |
|------|-----|
| Original SICA acc | 53.33% (16/30) |
| **Strict-filtered acc** | **53.33% (16/30)** |
| SC acc | 53.33% (16/30) |
| UNSAT rate | **63.33% (19/30)** |
| Avg MUS size | 5.68 constraints |
| Total MUS removed | 108 constraints |
| McNemar p-value | 1.0 (b=1, c=1) |

**关键发现：**

1. **UNSAT 率很高 (63%)**：19/30 题的 constraint set 存在逻辑矛盾，说明 LLM 生成的 constraints 内部冲突普遍。

2. **Accuracy 无变化**：strict-filtered 和原始 SICA 准确率完全相同 (53.33%)。McNemar 显示只有 1 题翻转（b=1 SICA→wrong, c=1 wrong→SICA），净效果为零。

3. **MUS 移除的 constraints 看起来合理**：例如 folio_25 移除了 `Not(located_in_southern_china(beijing))` 和 `located_in_southern_china(beijing)` 这对直接矛盾；folio_28 移除了 `from_mars(marvin)` 和 `~from_mars(marvin)`。

4. **原因分析**：MUS 移除的 constraints 数量相对总量较少（平均 5.68/总量 ~40），且被移除的 constraints 来源分散在多个 trace 中，不足以翻转多数投票的格局。Strict-mode filtering 本质上是一种比 MAX-SAT 更保守的去噪方式，但 MAX-SAT 已经有效处理了这些矛盾。

结果保存在：`/root/symb_invariant_consensus/results/dir_e_strict_verification/results.json`

---
