# ops fix stale sessions

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-stale-sessions_20260521T071751_result.json`
- **Structured JSON:** [`d5117a25bcd5e6d5e0cc.json`](../../sessions/d5/d5117a25bcd5e6d5e0cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

### westd-28034 状态

**tmux sessions**: 没有任何 tmux sessions（已经是干净状态，无需清理）。之前的 stale sessions 可能已被手动清理或服务器重启过。

**GPU 进程**: 无 GPU 进程运行，4 张 A100 32GB 全部空闲。

**eval 进程**: 无残留 eval_unified_preset 进程。

### Checkpoint 存在性（westd-28034）

**exp003** (`/root/autodl-tmp/checkpoints/exp003/`):
- checkpoint-1000 ✓
- checkpoint-2000 ✓
- checkpoint-3000 ✓
- checkpoint-4000 ✓
- checkpoint-4500 ✓
- checkpoint-5000 ✓
- checkpoint-5500 ✓
- checkpoint-6000 ✓
- checkpoint-6500 ✓
- checkpoint-7000 ✓

任务要求的 2000/3000/5000/6000/6500/7000 全部存在。

**exp009** (`/root/autodl-tmp/checkpoints/exp009_continuous_probe_grpo/`):
- checkpoint-500 ✓
- checkpoint-1000 ✓
- checkpoint-1500 ✓

### westd-29046 训练状态

westd-29046 上没有 `exp003` 原始目录的 checkpoint。有的是两个 seed 变体：
- `exp003_r3only_seed1`: 最新 checkpoint-7500
- `exp003_r3only_seed2`: 最新 checkpoint-3500

两张 GPU 都在使用中（各约 38GB），说明训练仍在进行。

### 结论

westd-28034 已经是干净状态，无需额外清理。duplicate session 错误现在不会再出现，4 张 GPU 空闲可以直接提交 eval 任务。

---
