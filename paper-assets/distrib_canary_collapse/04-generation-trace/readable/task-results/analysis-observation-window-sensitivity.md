# analysis observation window sensitivity

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_observation_window_sensitivity_20260515T230611_result.json`
- **Structured JSON:** [`a4c53dd8778f62a46a93.json`](../../sessions/a4/a4c53dd8778f62a46a93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册 (`art_20260515_0d5c1a`)。核心发现：

**Table 1** — 4-method 共识在 **T=6 即完全稳定**（6/6 robust pairs），T=6–10 结论完全一致。T=5 时 Perm Granger 尚未达标（差分后仅 4 点，排列分布不够可靠），导致 robust=0/6。

**方法敏感度排序**：
- Naive xcorr, Diff xcorr, Threshold：T=5 起全部稳定，对窗口完全不敏感
- Perm Granger：T≥6 稳定
- TY：T≤8 全部 insufficient_df（0/24 feasible）；T=9–10 才可计算，且大多数 pair 不显著（符合 C001 预期）

**审稿人回应要点**：4/5 方法从 T=6 起结论锁定，TY 的不稳定是 VAR 参数开销导致的 df 不足，不是信号弱。T=10 提供了远超必要的观测窗口。

---
