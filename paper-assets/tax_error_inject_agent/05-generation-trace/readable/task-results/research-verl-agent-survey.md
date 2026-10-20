# research verl agent survey

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verl-agent-survey_20260514T042543_result.json`
- **Structured JSON:** [`6f16bfb6a2677f14012c.json`](../../sessions/6f/6f16bfb6a2677f14012c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。报告已写入 `artifacts/verl_agent_survey.md`。核心发现：

**ALFWorld 集成状态**: 已完整集成，包括环境封装（Ray 并行化）、projection、prompt template、训练脚本（GiGPO/GRPO/PPO 等全覆盖）。无需从头实现。

**架构要点**:
- `EnvironmentManagerBase` 通过 `reset()` / `step()` / `build_text_obs()` 三个接口管理 agent-env 交互
- `SimpleMemory` 按 batch 维度存储 obs-action 历史，`fetch()` 返回格式化的滑动窗口
- 观测字典的 `anchor` 字段（不含历史的原始观测）是 GiGPO step grouping 的关键
- Agent 没有显式 plan state，"计划"仅存在于 `&lt;think>` 推理文本中

**面向 error injection 的 8 个扩展点**:
1. **Memory.fetch()** — 截断/篡改历史（最干净的 hook 点）
2. **build_text_obs()** — prompt 级注入（修改任务描述、可用动作、当前观测）
3. **EnvManager.step()** — 在环境返回后、交给 agent 前篡改观测/奖励
4. **anchor_obs** — 影响 GiGPO 分组
5. **Projection 函数** — 修改 action 解析
6. **Rollout Loop** — trajectory 级 hook（generate 后 / step 后）
7. **Reward Manager** — 自定义奖励函数
8. **Trajectory logging** — 需自行添加（目前无内置 replay 机制）

**推荐实施方案**: 继承 `SimpleMemory` + `AlfWorldEnvironmentManager`，在 `make_envs()` 注册新 env_name，不需要改动 GiGPO 核心或训练器代码。

---
