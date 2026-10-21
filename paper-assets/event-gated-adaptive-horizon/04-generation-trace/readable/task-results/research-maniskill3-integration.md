# research maniskill3 integration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_maniskill3_integration_20260515T140942_result.json`
- **Structured JSON:** [`d0fb9363d91d26f97e16.json`](../../sessions/d0/d0fb9363d91d26f97e16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已完成：**

1. **ManiSkill3 v3.0.1 已在 bjb1-45299 上安装验证**（含 Vulkan 配置修复）

2. **所有目标 task 确认存在**：PickCube-v1 (obs=42), StackCube-v1 (obs=48), PegInsertionSide-v1 (obs=43)，另有 PushCube-v1 (35), LiftPegUpright-v1 (32)

3. **Wrapper 代码已写入服务器** `/root/autodl-tmp/event-gated-adaptive-horizon/envs/maniskill.py`，通过了与 DreamerV3 wrappers (NormalizeActions, TimeLimit, SelectAction, UUID) 的集成测试

4. **推荐 2 个 tasks**：
   - **PickCube-v1** — reach→grasp→lift→place 4 阶段，天然适合时间抽象
   - **StackCube-v1** — 阶段更多，transport vs alignment 对 adaptive dt 需求更强

5. **已知限制**：`CUDA_VISIBLE_DEVICES` 限制会导致 SAPIEN segfault，需让 ManiSkill 看到所有 GPU

**下一步**：修改 `dreamer.py` 添加 `maniskill` suite 分支 + 添加 `maniskill_state` 配置到 `configs.yaml`。

---
