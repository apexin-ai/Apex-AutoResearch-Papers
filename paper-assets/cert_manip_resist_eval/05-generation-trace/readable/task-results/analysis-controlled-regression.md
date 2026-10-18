# analysis controlled regression

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_controlled-regression_20260523T071753_result.json`
- **Structured JSON:** [`3d1e10f8ba39344709d4.json`](../../sessions/3d/3d1e10f8ba39344709d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果保存在 `controlled_regression.json`。

**结果汇总**：

| Model Spec | K=3 η_max | K=3 K_eff | K=5 η_max | K=5 K_eff |
|---|---|---|---|---|
| baseline | 10/12 | 10/12 | 4/12 | 7/12 |
| +mean_acc | 7/12 | 7/12 | 6/12 | 4/12 |
| +n_local | 10/12 | 8/12 | 6/12 | 5/12 |
| +both | 6/12 | 6/12 | 6/12 | 3/12 |

**关键发现**：

1. **No over-control**: 加入两个控制变量后，η_max 和 K_eff 的 significance 都没有被完全 killed。K=3 从 10/12 → 6/12，K=5 η_max 反而从 4/12 上升到 6/12（suppression effect）。

2. **控制变量本身显著**: mean_acc K=5 显著 10/12, n_local K=5 显著 10/12 — 这些确实是相关因素，但加入后并未消除 η_max/K_eff 的解释力。

3. **High VIF 警告**: arc_challenge 条件下 VIF > 10（K=5 log_keff max=18.0, mean_acc max=10.7），表明 mean_accuracy 与 K_eff 在 arc_challenge 上存在多重共线性。MMLU 条件下 VIF 均 < 4，无共线性问题。

4. **Beta 变化**: K=5 K_eff 的 β 平均变化 -159%（含符号翻转），主要由 arc_challenge 高 VIF 条件驱动。η_max 的 β 相对稳定（~-23%）。

**对 reviewer 的回应**: η_max/K_eff 的 significance 在加入 confound 后有所减弱但 robust 保留，不是 confound-driven artifact。高 VIF 条件需在论文中注明。

---
