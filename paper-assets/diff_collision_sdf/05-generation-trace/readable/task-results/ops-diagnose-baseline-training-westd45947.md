# ops diagnose baseline training westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_baseline_training_westd45947_20260525T174351_result.json`
- **Structured JSON:** [`65ebb6a01871a156d043.json`](../../sessions/65/65ebb6a01871a156d043.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**两个实验均已崩溃**，原因是 tmux 服务器终止。

### 证据

| | s0 | s1 |
|---|---|---|
| **状态** | 崩溃 | 崩溃 |
| **日志最后 step** | 25695 (86%) | 25705 (86%) |
| **最后 checkpoint** | 24000 | 24000 |
| **best_loss** | 0.01025 @ step 24000 | 0.01130 @ step 14000 |
| **日志停写时间** | 2026-05-26 01:10:05 +0800 | 2026-05-26 01:10:01 +0800 |
| **sentinel 文件** | 不存在 | 不存在 |

### 根因分析

- 两个进程在同一秒停止写日志，且日志中无任何 error/traceback/killed 信息 → 非程序错误
- `tmux ls` → "no server running" — tmux 服务器本身已死
- 服务器 uptime 59 天，未重启
- `dmesg` 无权限，无法确认是否 OOM kill
- GPU 当前完全空闲（0 MiB / 0% utilization）
- 无训练 python 进程存活

**结论**：tmux 服务器异常终止导致两个训练会话同时被杀。

### 恢复建议

两个实验需从 step 24000 checkpoint resume，剩余约 6000 步（~7.7h @ 4.62s/step）。

Checkpoint 路径：
- `s0`: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/24000/`
- `s1`: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/24000/`

---
