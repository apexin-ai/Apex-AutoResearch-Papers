# research gigpo cherry pick

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gigpo_cherry_pick_20260515T065620_result.json`
- **Structured JSON:** [`6b65da3ef3c3cd48a110.json`](../../sessions/6b/6b65da3ef3c3cd48a110.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析报告已完成并保存。核心发现总结：

**GiGPO vs GRPO 的关键差异**：
1. **算法层**：GiGPO = episode-level advantage（同 GRPO）+ step-level advantage（anchor state grouping）。当组内全部 episode 同奖励时，GRPO advantage=0 零梯度，而 GiGPO 的 step-level 仍有信号。
2. **Rollout 层（更重要）**：verl-agent 每步独立构建 prompt（context ~2-3K tokens 恒定），RAGEN 全历史拼接（50步→25K+ tokens）。这导致 RAGEN 数据效率差 ~50x。

**Cherry-pick 方案**：~480 行新增 + ~200 行修改，8 个文件，3-5 天。核心工作是改造 ctx_manager 支持 step-independent 模式。建议先验证 step-independent rollout + GRPO baseline，再叠加 GiGPO 算法。

报告已保存到 `artifacts/verl_agent_analysis/gigpo_cherry_pick_plan.md` 并注册为 artifact。

---
