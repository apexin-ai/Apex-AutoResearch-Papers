# check westd status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_status_20260525T195239_result.json`
- **Structured JSON:** [`49705cb6cc36dc5076d4.json`](../../sessions/49/49705cb6cc36dc5076d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_086_frozen_dt_emb_cheetah_s0: ALIVE (1h42m), step 92k/105k, eval_reward=188.8 @85k, ETA ~15min
exp_088_cheetah_008d_s1:         ALIVE (1h02m), step 56k/105k, eval_reward=248.2 @55k, ETA ~55min
```

补充：
- 两个进程 GPU 占用各 3223 MiB，正常
- 两个实验 gate_dt 均锁定 dt=2（gate_dt_2_frac=1.0），符合预期（086 frozen，088 的 008d 配置）
- fps 均 ~14.2，训练速率一致
- 无 error/exception
- exp_088 的 train_return 已出现 240-280 的高值，eval_return 从 131→248 上升趋势良好

---
