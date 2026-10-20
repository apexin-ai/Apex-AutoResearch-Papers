# ops snapshot 029d 65k check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_snapshot_029d_65k_check_20260520T223552_result.json`
- **Structured JSON:** [`1e4dcec3127b5e937d2a.json`](../../sessions/1e/1e4dcec3127b5e937d2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_029d: step=88K, eval=259.5 (at 85K), NVE=0.855 (at 85K)
  轨迹:
    5K:  eval=31.7
   15K:  eval=159.1,  NVE=0.021
   25K:  eval=155.7,  NVE=0.171
   35K:  eval=190.8,  NVE=0.312
   45K:  eval=137.1
   55K:  eval=210.7
   65K:  eval=189.5
   75K:  eval=253.2,  NVE=0.791
   85K:  eval=259.5,  NVE=0.855  ← 最新

exp_029b: step=156K, eval=56.5 (at 155K), NVE=1.061 (at 155K)
  eval 在 55K 达峰 177.7 后持续崩塌 → 56.5
  NVE 越过 1.0（过估），性能已崩
```

进程存活未能确认（`ps|grep` 被 ssh_read_only 的管道限制挡住），但 exp_029d 最新数据到 88K 说明仍在跑。exp_029b 到 156K 但已崩。

---
