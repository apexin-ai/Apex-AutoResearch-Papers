# ops d047 figure regen

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d047-figure-regen_20260525T212230_result.json`
- **Structured JSON:** [`5fc2aebcec3398960104.json`](../../sessions/5f/5fc2aebcec3398960104.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 figure 均已重画完成，视觉验证通过。

### Figure 1: β trajectory
- **K_eff** (蓝线) CI band 在所有 K 值下始终高于 zero line ✓
- **η_max** (红线) CI 在 K=3 时完全在 zero 以上；K≥5 时 CI 下界跨过 zero line ✓
- Position bias 散点（~-0.35）作为明显离群值可见（蓝色最底部点）
- ylim 从 [-0.15, 0.60] 扩展到 [-0.45, 0.65] 以容纳修正后的 PB 负值散点

### Figure 2: regime transition
- K_eff: 8/12 → 8/12 → 7/12 ✓
- η_max: 5/12 → 0/12 → 1/12 ✓
- η_max 在 K≥5 时急剧下降，视觉效果清晰

### Figure 3: framework 概念图
- 无生成脚本（`gen_fig_framework*` 不存在），仅有手绘 PDF
- 图中无嵌入数值，caption 中的数字由 LaTeX worker 处理，图本身无需更新

### 产出文件
- `docs/paper/figures/fig_beta_trajectory.{pdf,png}` — 已更新（本地 + 服务器）
- `docs/paper/figures/fig_regime_transition.{pdf,png}` — 已更新（本地 + 服务器）
- `docs/paper/figures/gen_fig_beta_trajectory.py` — 数据已更新（本地 + 服务器）
- 服务器 `scripts/gen_fig_regime_transition_fixed.py` — WCB counts 已更新

---
