# setup maniskill env check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_maniskill_env_check_20260522T113706_result.json`
- **Structured JSON:** [`0111c039b42ded6d2a84.json`](../../sessions/01/0111c039b42ded6d2a84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

## 1. ManiSkill 安装状态

| 服务器 | ManiSkill | SAPIEN | gymnasium | 状态 |
|--------|-----------|--------|-----------|------|
| **bjb1-40020** | 3.0.1 | 3.0.3 | 1.3.0 | **可用** (已补装 `pytorch_kinematics_ms`, `dacite`) |
| **bjb1-45299** | 未安装 | 未安装 | 未安装 | 需要安装 |

Vulkan 警告（`Failed to find Vulkan ICD file`）不影响 state-based 模式运行（已用 `render_backend='cpu'` 绕过）。

## 2. 可用 Manipulation 任务 + obs/action space

DreamerV3 已集成的 3 个任务（`envs/maniskill.py` wrapper + `configs.yaml` 预设）：

| 任务 | obs dim | action dim | action range | config 预设 |
|------|---------|------------|-------------|------------|
| PickCube-v1 | 42 | 8 | [-1, 1] | `maniskill` / `maniskill_state` |
| StackCube-v1 | 48 | 8 | [-1, 1] | `maniskill_stackcube` |
| PegInsertionSide-v1 | 43 | 8 | [-1, 1] | `maniskill_peginsertion` |

其他可用但未集成的操纵任务：TurnFaucet-v1, PushCube-v1, PullCube-v1, PlugCharger-v1, LiftPegUpright-v1, OpenCabinetDoor-v1, OpenCabinetDrawer-v1, StackPyramid-v1 等共 27 个。

## 3. DreamerV3 + ManiSkill 启动命令模板

```bash
# PickCube (默认)
python dreamer.py --configs maniskill --task maniskill_PickCube-v1 --device cuda:0

# StackCube
python dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --device cuda:0

# PegInsertion
python dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --device cuda:0
```

注意事项（来自 memory + wrapper 代码）：
- **禁止 CUDA_VISIBLE_DEVICES**：wrapper 中 `resolve_physical_device()` 会移除 CVD 并重映射到物理 GPU index
- **SAPIEN 需要 CUDA**：state 模式用 `render_backend='cpu'` 绕过渲染
- **torch.compile 不工作**（ManiSkill3 已知限制）

## 4. Registry 状态

| 实验 | 状态 |
|------|------|
| **exp_045** | **不存在**（全部 120 条中无此 ID） |
| **exp_047_frozen_dt_emb_walker_s1** | RUNNING |
| exp_044_gradient_stop_walker | RUNNING |
| exp_046_frozen_dt_emb_cheetah | RUNNING |

exp_045 可能尚未创建，或命名不同。当前 RUNNING 的是 044、046、047 三个实验。

---
