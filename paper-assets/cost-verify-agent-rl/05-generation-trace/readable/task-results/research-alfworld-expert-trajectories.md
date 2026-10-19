# research alfworld expert trajectories

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_alfworld-expert-trajectories_20260514T125649_result.json`
- **Structured JSON:** [`4cf1ed6fa59d79bb3986.json`](../../sessions/4c/4cf1ed6fa59d79bb3986.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已更新到 `artifacts/expert_trajectory_plan.md`。核心发现：

**现有数据**:
- 1200 条模板合成轨迹，6 类各 200 条，缺 `pick_and_place_with_movable_recep`
- exp008_sft 证明：教了格式(valid 90%)但没教策略(success 0%)

**Expert 机制**:
- `HandCodedTWAgent` 是规则化子目标分解 agent，基于 PDDL facts 决策
- 通过 `AlfredExpert` wrapper 自动提供 `extra.expert_plan`
- 成功率 ~80-90%，非最优但远优于模板合成
- `pick_and_place_with_movable_recep` 无对应策略类（365 games 需跳过）

**推荐方案**: 用 `HandCodedTWAgent` 在 3553 个 train games 上批量 rollout，预估可收集 ~1759 条成功轨迹。纯 CPU 任务，1-2 小时完成。

**报告包含完整可运行的 `collect_expert_trajectories.py` 脚本**，支持断点续传、自动格式转换为 RAGEN SFT 格式。

---
