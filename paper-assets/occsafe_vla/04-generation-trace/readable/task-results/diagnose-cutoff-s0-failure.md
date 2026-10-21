# diagnose cutoff s0 failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cutoff_s0_failure_20260522T140151_result.json`
- **Structured JSON:** [`11f8e4185875ea93b636.json`](../../sessions/11/11f8e4185875ea93b636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败根因：进程被外部 kill（无错误日志）

- 日志中 **无 Traceback、无 OOM、无 Killed、无 CUDA error**
- 日志仅包含 TF cost estimator 和 PyTorch grad stride 的无害 warning
- 进程在 progress bar 输出中途突然终止——**典型的外部 SIGKILL 特征**（OOM killer 或人工/系统 kill）

### 训练进度

- **最后 AUX log**: `step=17500`（occ_loss=0.0145, action_loss=0.1611），运行到 5:52:36
- loss 曲线正常下降（step 0: occ=0.0979, action=0.6914 → step 17500: occ=0.0145, action=0.1611）
- 训练速度稳定 ~1.06 it/s，在最后几步出现短暂减速（step 17486: 1.65s/it），可能与内存压力有关

### Checkpoint 状态

- **仅有 step 10000 checkpoint**（`--10000_chkpt`），文件完整（model shards + lora_adapter + action_head + occ_head + proprio_projector）
- Step 20000 checkpoint 未保存（`--save_freq 10000`，进程在 17500 步死亡）

### 当前 GPU 状态

- 4x NVIDIA RTX PRO 6000 (98GB)，**全部被占用**（~62GB/98GB each）
- GPU 0 当前运行的是 PID 137021（非原 PID 136941），同一 conda 环境 `occsafe`
- 服务器负载很高，4 卡全满

### 建议

1. **从 step 10000 checkpoint resume**，损失约 7500 步（~2 小时）训练量
2. 当前 GPU 0 已被其他进程占用，需要先确认能腾出 GPU
3. 考虑将 `--save_freq` 降到 5000 减少再次意外中断的损失

---
