# ops maniskill3 install

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_maniskill3-install_20260516T030213_result.json`
- **Structured JSON:** [`728526b45ce88e4e9069.json`](../../sessions/72/728526b45ce88e4e9069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

## 结果

### 1. 安装状态
- **ManiSkill3 v3.0.1 已预装**，无需安装
- PickCube-v1 / StackCube-v1 / PegInsertionSide-v1 环境验证通过

### 2. 已有代码情况
- `envs/maniskill.py` — 完整的 DreamerV3 wrapper，处理 state/image obs、CUDA_VISIBLE_DEVICES 兼容
- `dreamer.py` L198-205 — `make_env` 中 maniskill 分支已就绪
- `configs.yaml` — 原本只有 `maniskill_state`（PickCube-v1）

### 3. 补充的配置
在 configs.yaml 中新增两个 preset：
- `maniskill_stackcube` — StackCube-v1（obs 48维，action 8维）
- `maniskill_peginsertion` — PegInsertionSide-v1（obs 43维，action 8维）

### 4. 代码修复（2处）
- **models.py L420**: `obs["image"] / 255.0` → 加 `if "image" in obs` 条件，state-only 环境无 image key
- **tools.py L216**: `cache[...]["image"]` → 改为 `.get("image", [])`，同理

### 5. Dry-run 结果
**成功。** PickCube-v1 + debug config 在 cuda:0 上运行正常：
- Eval: return=1.2, length=200, 10 episodes
- Training: model_loss=50.6, reward_loss=5.5, actor_entropy=10.3
- 未干扰 cuda:0/cuda:1 上的现有实验

### 注意事项
- ManiSkill/SAPIEN 必须有 CUDA，不支持纯 CPU 运行
- `torch.compile` 在当前 PyTorch 版本有 bug（duplicate template name），实验需关闭或升级 PyTorch
- wrapper 会移除 CUDA_VISIBLE_DEVICES，因此不能用 CVD 限制 GPU 可见性；用 `--device cuda:X` 指定训练设备

---
