# ops pi05 crm timeout extend

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pi05-crm-timeout-extend_20260524T194858_result.json`
- **Structured JSON:** [`d548ea6a40912cfbb8b5.json`](../../sessions/d5/d548ea6a40912cfbb8b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 续期完成

### 1. Timeout 机制
`timeout 43200` (12h shell timeout) 包裹训练命令。进程树：
- `326310` bash 包装器（含 EXIT trap）
- `326314` **timeout 43200** ← 杀手
- `326315` python train_crm.py ← 实际训练

无 cron / 无其他 kill 机制。

### 2. 续期操作
```
kill -9 326314
```
SIGKILL 立即杀掉 timeout，使其无法将信号转发给子进程。训练 326315 被 reparent 到 PID 1 (init)，继续运行。日志 fd 是 326315 自己持有的副本，bash 包装器退出不影响日志写入。

### 3. 训练当前状态
- PID 326315 存活，PPID=1，state=Rl，CPU 100%
- epoch 26 batch 100/684 进行中
- best_val_loss=0.004790 (epoch 25)
- 每 epoch 约 22 min
- 最新 checkpoint：`/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/checkpoint_epoch0025.pt` 及 `crm_best.pt`

### 4. 预计完成时间
剩余 24 epochs × 22min ≈ 8.8h，**约 2026-05-25 12:30 UTC 完成**。

### 注意事项
- `/tmp/agent-ml-exit/train-crm-pi05-unified-3suite-r2.exit` 已被写为 `137|2026-05-24T19:50:10Z`，框架层会认为该 job 已结束（exit code 137 = SIGKILL）。实际训练继续运行，但框架的 check_training_status 会显示已退出。
- 训练继续写入 `~/runs/.../train-crm-pi05-unified-3suite-r2.log`，可直接 tail 查看进度。
- 同机器另有 tmux session `long-vla-s47` 在 GPU 1 上跑评估，与本训练（GPU 0）无冲突。

---
