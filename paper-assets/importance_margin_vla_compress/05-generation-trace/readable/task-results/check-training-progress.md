# check training progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_progress_20260516T103203_result.json`
- **Structured JSON:** [`c58e771c5b7751dfd4c7.json`](../../sessions/c5/c58e771c5b7751dfd4c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态

### 1. v8c_annealing (cuda:0) — **已完成** ✓

| 指标 | 值 |
|------|-----|
| 进度 | **30000/30000** (100%) |
| 最终 loss | 0.0492 (action=0.0023, margin=0.0938) |
| 退出码 | 0（正常完成） |
| 完成时间 | 18:24:59 |
| GPU | 已释放，0MiB 占用 |

### 2. baseline_v6_alpha16 (cuda:1) — **运行中**

| 指标 | 值 |
|------|-----|
| 进度 | **26750/30000** (89.2%) |
| 剩余 | 3250 steps |
| 当前 loss | 0.0034 |
| eval/action_loss | 0.0033 (step 26000) |
| 速度 | 4.0 sps (~12s/50步) |
| 预计剩余 | **~13 分钟** |
| GPU 显存 | 2281MiB / 97887MiB |
| GPU 利用率 | nvidia-smi 瞬时读数 0%，但进程活跃且持续出 log |

### 异常

- **v8c_annealing 早期启动曾崩溃**：`logs/v8c_annealing_train.log` 记录了 15:08 的一次 wandb login 报错（`No API key configured`），但后续重启（带 `WANDB_MODE=offline`）已正常跑完。
- baseline 无异常，loss 和 grad_norm 正常收敛。

---
