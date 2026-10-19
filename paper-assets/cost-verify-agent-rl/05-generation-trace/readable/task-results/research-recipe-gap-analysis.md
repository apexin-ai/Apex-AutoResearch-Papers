# research recipe gap analysis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_recipe_gap_analysis_20260515T201631_result.json`
- **Structured JSON:** [`e79ea7432af6f4115db6.json`](../../sessions/e7/e79ea7432af6f4115db6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析报告已完成并注册。核心发现：

**62pp gap 的三个根因（按优先级）：**

1. **SFT 起点是毒药** — GiGPO 和 Self-Guide **都不做 SFT**，直接从 Instruct 模型冷启动 RL 就达到 72%+。我们的 SFT checkpoint 只有 6.25% success，可能比原版 Instruct 模型更差。从一个几乎不成功的起点做 GRPO = 大部分 group 全失败 → 零梯度。

2. **Binary reward = 零梯度信号** — GiGPO 有 -0.1 invalid action penalty，即使全失败的 group 也有方差（invalid action 多少不同→reward 不同→有梯度）。我们的 0/10 binary reward 在全失败 group 中方差为零，约 43% 的 group 完全无法学习。

3. **Mini-batch size 8× 过小** — 32 vs 256，导致 ~100 次 noisy gradient updates/step vs ~12 次 stable updates。策略可能在单步内剧烈震荡。

**exp028 建议：** 
- Phase A（最小变更验证）：`model_path: Qwen2.5-1.5B-Instruct` + 启用 invalid_action_penalty
- Phase B（全面对齐）：LR→1e-6, mini-batch→256, steps→150, env_groups→16

详见 `artifacts/docs/recipe_gap_analysis.md`。

---
