# check full status snapshot 0523

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full-status-snapshot-0523_20260523T042206_result.json`
- **Structured JSON:** [`1a56f2bbd20df91e5c2c.json`](../../sessions/1a/1a56f2bbd20df91e5c2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| exp_id | server:gpu | PID | alive? | current_step | target | eval_return | ve_ratio | 预计完成 |
|--------|-----------|-----|--------|-------------|--------|-------------|----------|---------|
| exp_049 | bjb1-45299:GPU0 | 91395 | **DEAD** | 222,400 | 210,000 | **34.88** (212.5k) | 0.186 | **已完成** |
| exp_052 | bjb1-45299:GPU0 | 103781 | YES (6h54m) | 150,800 | 210,000 | 27.32 (142.5k) | 0.140 | ~2.8h (~18:00) |
| exp_053 | bjb1-45299:GPU0+1 | 123495 | YES (1m28s) | 2,600 | 210,000 | 0.56 (2.5k) | 0.0 (frozen) | ~13h (~明早 04:00) |
| exp_050 | bjb1-40020:GPU0 | 304736 | YES (9h45m) | 153,600 | 210,000 | **2.40** (152.5k) | **8.46** | ~3.6h (~19:00) |
| exp_051 | bjb1-40020:GPU0+1 | 305974 | YES (9h32m) | 155,000 | 210,000 | **30.67** (152.5k) | 0.168 | ~3.5h (~19:00) |

要点：
- **exp_049** 已完成并自然退出，最终 eval_return 34.88
- **exp_050** (PegInsertion civo_trigger) 表现很差，eval_return 仅 2.4，ve_ratio 飙到 8.46——gate 信号可能在 PegInsertion 上不起作用
- **exp_051** (StackCube frozen_dt_emb) 表现不错，eval_return 30.67，与 exp_049 同量级
- **exp_053** 刚部署不到 2 分钟，还在 warmup，gate frozen 所以 ve_ratio=0 符合预期

---
