# research verl agent migration

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verl-agent-migration_20260515T041332_result.json`
- **Structured JSON:** [`bcf3bd26cf4825827ab1.json`](../../sessions/bc/bcf3bd26cf4825827ab1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，迁移方案已写入 `artifacts/verl_agent_migration_plan.md`。核心发现：

---

**verl-agent** 是独立项目 ([langfengQ/verl-agent](https://github.com/langfengQ/verl-agent))，不是 verl 官方模块。核心卖点：

- **Step-independent multi-turn rollout**：每步独立构建输入，context 长度恒定，ALFWorld 可跑 50 步不爆 token
- **GiGPO 算法**：两层分组优势估计（episode-level + step-level anchor state grouping），对多步任务的 credit assignment 有理论优势
- **asyncio 异步 rollout**：环境交互不阻塞 GPU

**当前 RAGEN 的问题**：

- verl 子模块停留在 **0.6.1**（最新 0.7.1）
- 全历史拼接 rollout，~10 turns 有效，长 horizon 效率差
- ctx_manager.py 72KB + agent_trainer.py 78KB，高度耦合

**三个迁移方案**：

| 方案 | 工作量 | 风险 | 收益 |
|------|--------|------|------|
| A: 全量迁移到 verl-agent | 3-4周 | 高 | 最干净，最新算法 |
| B: 渐进式（升级verl→改rollout→加GiGPO）| 2-3周分阶段 | 中 | 平衡 |
| **C: Cherry-pick GiGPO** | **3-5天** | **低** | 最小侵入，验证算法价值 |

**推荐当前选方案 C**：项目在活跃实验阶段（23个实验），框架大改风险太高。先移植 GiGPO 验证效果，后续再决定是否做 rollout 重构。

---
