# diagnose post restart westd

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_post_restart_westd_20260519T124618_result.json`
- **Structured JSON:** [`aba705f1b8e8fada071a.json`](../../sessions/ab/aba705f1b8e8fada071a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. eval_mlp_adapter_control — **已完成，结果已恢复**
- **状态**: 完成，结果在磁盘
- **Overall SR: 65.2%** (326/500), 95% CI [60.9%, 69.2%]
- Per-task: butter 80% (最高) → chocolate pudding 52% (最低)
- Registry 已更新 metrics + conclusion=success

### 2. eval_openvla_baseline_spatial — **仍在运行**
- **进程 552445 存活**, 已运行 2h15m, GPU 1 占用 16GB (68% util)
- 进度: Task 4/10, Ep 40/50 (约 190/500 episodes = 38%)
- **所有已完成任务 SR=0%** (tasks 1-3 均 0/50)，与 OpenVLA 在 spatial suite 的预期一致
- 速率 1.5 eps/min，剩余 ~310 episodes，预计还需 **~3.5 小时**
- GPU 0 空闲 (1 MiB)

### 3. train_smart_compress_m16_seed44 — **被 SIGTERM 杀死，需恢复**
- **最后状态**: step 35075/100000 (35%) 收到 signal 15 graceful exit
- **最新 checkpoint**: step 35000, 文件 681MB 完整存在
- eval/action_loss: 0.0872 @ step 35000
- loss ~0.05-0.17 范围，gradient 正常
- 不在 registry 中
- **建议**: 从 checkpoint step 35000 恢复训练，剩余 65000 steps (~3.6h @ 5.0 sps)

---
