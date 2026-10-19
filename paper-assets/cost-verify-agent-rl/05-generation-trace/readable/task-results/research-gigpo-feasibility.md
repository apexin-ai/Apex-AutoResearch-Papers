# research gigpo feasibility

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gigpo_feasibility_20260515T195129_result.json`
- **Structured JSON:** [`a7e474cc25f70705e6f9.json`](../../sessions/a7/a7e474cc25f70705e6f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册。核心结论：

**推荐 GiGPO（方案 A）**，理由：

1. **改动量最小（~250 LOC）**：核心算法可从 [verl-agent](https://github.com/langfengQ/verl-agent/tree/master/gigpo) 直接移植，4 个函数（`build_step_group`, `step_norm_reward`, `episode_norm_reward`, `compute_gigpo_outcome_advantage`）
2. **基础设施已就绪**：`anchor_obs` 全链路已在 codebase 中采集（`env/alfworld/env.py:227` → `es_manager.py:377` → `ctx_manager.py:1141` → `non_tensor_batch["anchor_obs"]`）
3. **零额外 GPU 成本**：critic-free，与 GRPO 相同内存开销，anchor grouping 仅需 hashmap lookup（0.01s/iteration）
4. **论文直接可比数据**：Qwen2.5-1.5B 在 ALFWorld 上 GRPO 72.8% → GiGPO 86.1%（**+13.3pp**）
5. **1-2 天可集成并启动实验**

**Self-Guide 作为 fallback**：效果更强（+17pp）但需 ~500-800 LOC、rollout 速度减半（每步 2x forward pass）、代码未开源。仅在 GiGPO 效果不足时考虑。

完整评估已写入 `artifacts/_project/report/plan_d_assessment.md`。

---
