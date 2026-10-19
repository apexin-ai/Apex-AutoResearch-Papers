# diagnose baseline lora failed

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_baseline_lora_failed_20260521T021217_result.json`
- **Structured JSON:** [`2492a945b87dca6423c1.json`](../../sessions/24/2492a945b87dca6423c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因找到了。

## 诊断报告

### 根因

tmux wrapper 启动命令传了 **不存在的参数**：

```
train_baseline.py: error: unrecognized arguments: --gpu 1 --max_steps 30000
train_baseline.py: error: unrecognized arguments: --gpu 3 --max_steps 30000
```

`train_baseline.py` 的 argparse 不接受 `--gpu` 和 `--max_steps`。正确参数是：
- GPU 选择：通过 `CUDA_VISIBLE_DEVICES` 环境变量（不是 `--gpu`）
- 训练步数：`--num_train_steps`（不是 `--max_steps`）

### 当前状态

两个实验实际上**已经在正常运行**（可能是后来用正确命令重新启动的）：
- `spatial_bowl_s0`: step 4072/30000 (14%), loss=0.0496, 已跑 4h33m
- `object_pudding_s0`: step 4062/30000 (14%), loss=0.0382, 已跑 4h34m

EXIT_CODE=2 来自 tmux wrapper 的**首次失败启动**，不影响当前正在运行的训练进程。

### 影响范围

- 仅影响 job submission 系统的启动命令模板。训练脚本本身无问题。
- 如果其他实验的 tmux wrapper 也使用 `--gpu` / `--max_steps` 参数，会遇到同样的失败。

### 修复建议

修改 job submission 模板，将：
- `--gpu X` → 移到环境变量 `CUDA_VISIBLE_DEVICES=X`
- `--max_steps N` → `--num_train_steps N`

---
