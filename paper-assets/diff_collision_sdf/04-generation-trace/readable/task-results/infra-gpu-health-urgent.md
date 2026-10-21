# infra gpu health urgent

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-health-urgent_20260529T034020_result.json`
- **Structured JSON:** [`3e57c7fca565aa4f6a4f.json`](../../sessions/3e/3e57c7fca565aa4f6a4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### westd-35807 — `train_pi05_lora_baseline_s3` (PID 89242)

| 项目 | 状态 |
|------|------|
| **进程** | **DEAD** |
| **GPU** | cuda:0 — 0% 利用率，0 MiB 显存（完全空闲） |
| **tmux** | ssh_read_only 不支持 tmux 命令，无法检查 |
| **崩溃原因** | **LeRobot 数据集 API 不兼容** — `lerobot_dataset.py:508` 报 `TypeError: stack(): argument 'tensors' (position 1) must be tuple of Tensors, not Column`。数据集 `safelibero_object` 是 v2.0 格式，新版 LeRobot 的 `hf_dataset["timestamp"]` 返回的是 HF `Column` 而非 Tensor 列表，`torch.stack()` 无法处理。训练在数据加载阶段就挂了，**一个 step 都没跑**。 |

---

### westd-45947 — `train_pi05_a1_obj_s3_l01` (PID 35444)

| 项目 | 状态 |
|------|------|
| **进程** | **ALIVE**（已运行 33 分钟） |
| **GPU** | cuda:0 — **100% 利用率**，19107 MiB 显存 |
| **当前进度** | step **1565 / 30000**（5.2%），~1.20s/it，预计剩余 ~9.5h |
| **Loss** | action=0.1475, sdf=0.0306, ee=0.0603, total≈0.1484 |
| **LR** | 2.50e-05（warmup 已完成） |
| **状态** | 正常训练中，无异常 |

---

**结论**：westd-45947 正常运行中无需干预。westd-35807 因 LeRobot 版本与数据集格式不兼容崩溃，需修复 `lerobot_dataset.py` 中 `torch.stack(self.hf_dataset["timestamp"])` 的调用（改为 `torch.tensor(self.hf_dataset["timestamp"])`），或将数据集转换为 v2.1 格式后重新启动。

---
