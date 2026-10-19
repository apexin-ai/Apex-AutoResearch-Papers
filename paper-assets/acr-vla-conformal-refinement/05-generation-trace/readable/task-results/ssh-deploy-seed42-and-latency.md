# ssh deploy seed42 and latency

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-seed42-and-latency_20260520T071349_result.json`
- **Structured JSON:** [`daf02423d01327653fd6.json`](../../sessions/da/daf02423d01327653fd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

只剩新进程 PID 681823，运行正常。

## 部署结果

### 任务 1: P50 seed42 eval (bjb2-40593)
- **Server**: bjb2-40593
- **GPU**: cuda:0
- **tmux session**: `eval-adaptive-k-spatial-p50-seed42`
- **PID**: 681823
- **状态**: 运行中
- **注意**: 旧进程 PID 675831 实际仍在运行（你说已死但实际没死），已 kill 掉，新进程独占 GPU 0

### 任务 2: Latency profiling N=1000 (bjb2-28827)
- **Server**: bjb2-28827
- **GPU**: cuda:4（空闲 GPU）
- **tmux session**: `latency-profile-n1000`
- **PID**: 252933
- **参数**: `--n_measure 1000 --n_warmup 100 --output logs/latency_profile_n1000.json`
- **状态**: 运行中

**cron 监控**: 因为 `submit_training_job` 工具不存在，两个任务都通过 `ssh_execute` + tmux 提交，未自动注册 cron 监控。如果需要 cron 轮询，我可以手动创建。

---
