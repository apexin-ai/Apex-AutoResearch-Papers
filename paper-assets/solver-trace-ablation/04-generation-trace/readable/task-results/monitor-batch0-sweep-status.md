# monitor batch0 sweep status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_batch0-sweep-status_20260516T033803_result.json`
- **Structured JSON:** [`b28213dd9ec5837e878c.json`](../../sessions/b2/b28213dd9ec5837e878c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## sweep-isr-b005-s42
- 进程状态: **存活** (PID 604647, Rl, 100% CPU, 运行 16m45s)
- 最后 step: **250/500** (reward_log 257行)
- Checkpoint: checkpoint-200 (完整 ~15GB), checkpoint-250 (写入中)
- 速率: 250 步 / 16 min ≈ 15.6 步/min
- 预计剩余: ~16 min
- 结论: **running (50%)**

## sweep-isr-b01-s45
- 进程状态: **存活** (PID 604569 在 GPU 上, 91% GPU利用率)
- 进程树: 604564(bash) → 604568(timeout) → 604569(python3)
- 最后 step: reward_log 99行至 step 96，但 checkpoint-100 已完整保存
- Checkpoint: checkpoint-50, checkpoint-100 (完整 ~15GB)
- 结论: **running，已过 100 步**（config merge bug 已修复，未在 100 步停止）
- 预计剩余: ~50-60 min（步速较 b005 慢，约 5-6 步/min）

## GPU 状态
- cuda:0: 79547 MiB, 91% (sweep-isr-b01-s45, PID 604569)
- cuda:1: 80355 MiB, 4% (sweep-isr-b005-s42, PID 604647)

两个实验均正常运行，未受 cron 误报影响。b005-s42 约 16 分钟后完成，b01-s45 约 1 小时后完成。

---
