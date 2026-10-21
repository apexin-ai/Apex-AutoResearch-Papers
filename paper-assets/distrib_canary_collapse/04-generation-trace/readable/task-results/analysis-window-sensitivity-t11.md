# analysis window sensitivity t11

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_window_sensitivity_t11_20260515T235835_result.json`
- **Structured JSON:** [`1b38c3f10f511e9bb421.json`](../../sessions/1b/1b38c3f10f511e9bb421.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

**T=10→T=11 对 consensus 无影响**：4/5 robust pairs 在 T=10 和 T=11 均为 6/6，四个非 TY 方法结果完全一致。之前报告的所有数字无需修正。

**意外发现——TY 在 T=11 反而更差**：
- T=10: 24/24 feasible TY tests, 1/6 consensus sig pairs (ECE→d3)
- T=11: **1/24 feasible** TY tests, 0/6 consensus sig pairs

原因：AIC 在 11 个数据点下倾向选 best_p=2（多一个点让更复杂模型的 AIC 更优），但 p_aug=3 后 n_params=7, n_eff=8, df_resid=1，不足以做 Wald test。这是模型选择的 artifact，不是信号不稳定。

5/24 个 seed×pair 出现"flip"，但全部是 TY 从 feasible+sig 变为 infeasible，进一步印证 C001 约束的正确性。

---
