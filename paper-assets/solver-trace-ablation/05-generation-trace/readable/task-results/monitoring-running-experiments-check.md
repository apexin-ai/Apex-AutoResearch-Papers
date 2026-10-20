# monitoring running experiments check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_running-experiments-check_20260516T060244_result.json`
- **Structured JSON:** [`70ea04420a277f664820.json`](../../sessions/70/70ea04420a277f664820.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常运行。汇总：

## plan018-additive-random-b01-s45-r3
- **状态**: 运行中，PID 688887，GPU 0 (79538 MiB)
- **进度**: step 30 / 500 (6%)
- **最新指标** (step 30): prove_rate=0.5, isr_mean=0.29, random_mean=0.56
- **启动时间**: 13:57，当前 step 间隔 ~12s
- **预估剩余**: ~94 min（470 steps × ~12s/step）

## sweep-isr-b02-s44
- **状态**: 运行中，PID 688219，GPU 1 (80318 MiB)
- **进度**: step 34 / 500 (6.8%)
- **最新指标** (step 34): prove_rate=0.0 (波动中), isr_mean=0.0, β=0.2
- **启动时间**: 13:54，当前 step 间隔 ~12s
- **预估剩余**: ~93 min（466 steps × ~12s/step）

## 磁盘
- `/root/autodl-tmp`: 197G/250G used (54G free) — 上次因磁盘满崩溃，当前余量可支撑完成（checkpoint ~16GB × 2 = 32GB < 54GB）

两个实验都在早期阶段，运行正常。

---
