# diagnosis exp003 status check 0520T17

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-status-check-0520T17_20260520T161934_result.json`
- **Structured JSON:** [`985d3f7e7abb51e1a1c3.json`](../../sessions/98/985d3f7e7abb51e1a1c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-29046 ===

exp-003 seed 1 (PID 70649):
  状态: 运行中, 已跑 1d23h28m
  当前 step: ~5930/8000 (估算，基于最新 ckpt-5500 + 3.75h × ~115 step/h)
  Checkpoints: ckpt-500 ~ ckpt-5500 (每500步, 共11个, 存于 /root/autodl-tmp/checkpoints/exp003_r3only_seed1/)
  日志: stdout 输出到 pipe (无独立日志文件)
  Step time: ~31s/step
  ETA: ~17-18h → 约 5/21 18:00 CST

exp-003-s2 seed 2 (PID 237432):
  状态: 运行中, 已跑 16h02m
  当前 step: 1756/8000 (22%)
  Checkpoints: ckpt-500, ckpt-1000, ckpt-1500 (存于 /root/autodl-tmp/checkpoints/exp003_r3only_seed2/)
  日志: ~/runs/contrastive_entrain_calib/exp-003-s2.log
  Step time: ~27-31s/step (均值 ~28s)
  ETA: ~48h → 约 5/23 01:00 CST

29046 GPU:
  GPU 0: 95%, 38049/97887 MiB (seed 1)
  GPU 1: 97%, 38161/97887 MiB (seed 2)

=== westd-28034 ===

GPU: 4卡全部空闲 (0% 利用率, 2 MiB/32607 MiB × 4)
无运行中的计算进程

exp003 checkpoints (已拷贝到 28034):
  /root/autodl-tmp/checkpoints/exp003/ → ckpt-1000, 2000, 3000, 4000, 5000

eval 已完成:
  ckpt-1000 ✓ (preset_eval.json + summary)
  ckpt-2000 ✓
  ckpt-3000 ✓
  ckpt-4000 ✓ (最新, 5/20 23:26)
  ckpt-5000 — checkpoint 已拷贝但尚未 eval
```

**要点**: 28034 四卡全空闲，ckpt-5000 已到位但未跑 eval；seed 1 约明晚完成，seed 2 约后天凌晨完成。

---
