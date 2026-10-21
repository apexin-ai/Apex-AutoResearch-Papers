# ops snapshot bjb1 45299 director check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_snapshot_bjb1_45299_director_check_20260520T210421_result.json`
- **Structured JSON:** [`3e24b161c734bbf7ffe4.json`](../../sessions/3e/3e24b161c734bbf7ffe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_030c: step=172K (train), eval=130.9@165K (peak 372@35K), NVE=0.115, 进程=alive
exp_031:  step=158K (train), eval=23.1@152.5K (peak 23.5@132.5K), NVE=N/A(上次0.18), 进程=alive, 完成状态=running (距200K还~42K)
GPU: cuda:0=22% cuda:1=31%
```

**vs 上次快照 (60min前)**:
- exp_030c: 116K→172K (+56K steps), eval 162→131 (下降), NVE 0.14→0.115
- exp_031: 132.5K→158K (+25.5K steps), eval 23.5→23.1 (持平)

两个实验都在跑。exp_030c 推进很快但 eval 持续低于峰值；exp_031 稳定但 eval 在 ~23 附近停滞，预计还需约1.5-2小时到 200K。

---
