# research pivot gate mechanisms

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pivot-gate-mechanisms_20260513T214027_result.json`
- **Structured JSON:** [`f32088fd1a55a5f7afcc.json`](../../sessions/f3/f32088fd1a55a5f7afcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已写入 `artifacts/pivot_gate_survey.md`。核心结论：

**Top 3 推荐方案：**

1. **Soft Weighted Gate**（工程量最小，2-4h）— 将 Gumbel-Softmax hard sampling 直接改为 softmax weighted combination `h_{t+1} = Σ_k w_k · RSSM(h_t, a_t, k)`。完全可微，消除梯度偏差。用 top-2/3 限制计算量。

2. **THICK-style Sparse Latent Update**（1-2d）— RSSM state 分 fast/slow，slow 部分稀疏更新。学术新颖性最高（ICLR 2024，有参考实现）。但依赖 exp_006 结果——如果 fixed dt=2 也崩，说明 variable-rate imagination 本身有问题，THICK 可能也受影响。

3. **Continuous dt as Action Dimension**（SEAC-style，1-2d）— dt 作为 actor 的连续输出维度，actor-critic 联合优化。有收敛性理论保证（SEAC/MOSEAC）。需要解决 non-integer dt 的 RSSM interpolation。

**决策依赖 exp_006**：
- fixed dt=2 return 正常 → 问题在 gate → 先做方案 1（Soft Gate）快速验证
- fixed dt=2 也崩 → 问题在 variable-rate imagination 本身 → 需要方向 B（Multi-timescale）或 D（Director hierarchy）的更根本改变

共调研 15 篇论文，覆盖 ICLR 2024、NeurIPS 2023 Spotlight、RLC 2024 等顶会。

---
