# writing method section draft

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_method_section_draft_20260514T170348_result.json`
- **Structured JSON:** [`dfdbe1ccf4610db4111a.json`](../../sessions/df/dfdbe1ccf4610db4111a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。`artifacts/method_section_draft.md` 已写入并注册。

要点总结：

- **所有公式与 `alpha_eff.py` 代码一致**：α_eff(b)、ESS(b)、b* 求解逻辑（grid search + bisection + ESS fallback）
- **Algorithm 1 忠实反映代码实现**：先检查 α_eff(0) ≥ τ 提前返回，grid search 跟踪 threshold_b 和 best_feasible_b，ESS < n_min 时 early termination，bisection 精化 50 次迭代，ESS 冲突时回退
- **明确 acknowledge Drayson** 的公式优先权，"introduced by \citet{drayson2025}"
- **b_max = 20.0** 从代码默认值提取
- **无 EMA**，无跨 batch 状态
- **留了 placeholder** 给 b* 分布统计
- 约 970 words

---
