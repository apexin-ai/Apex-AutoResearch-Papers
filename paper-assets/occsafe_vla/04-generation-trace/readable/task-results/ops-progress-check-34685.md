# ops progress check 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-34685_20260522T070720_result.json`
- **Structured JSON:** [`9c3af323bb047564a4ec.json`](../../sessions/9c/9c3af323bb047564a4ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
depth_s0:  step 14230/50005 (28.5%), depth_loss=0.0251, action_loss=0.1050, speed=~1.07 it/s
depth_s1:  step 14235/50005 (28.5%), depth_loss=0.0166, action_loss=0.1099, speed=~1.07 it/s
cutoff_s0: step  1739/50005 ( 3.5%), occ_loss=0.0172, action_loss=0.1533, speed=~1.08 it/s
cutoff_s1: step  1740/50005 ( 3.5%), occ_loss=0.0145, action_loss=0.2246, speed=~1.08 it/s

GPU utilization: cuda:0 99%, cuda:1 80%, cuda:2 99%, cuda:3 50%
GPU memory: 全部 ~62G/98G

Disk: 350G total, 319G used, 32G avail (91%)
Checkpoints: depth_s0 75G, depth_s1 75G, cutoff_s0 4K, cutoff_s1 4K
```

**注意：** cutoff_s0 和 cutoff_s1 明显是最近重启过的——运行仅 ~34 分钟，step 才到 1700 附近，checkpoint 目录为空。depth 两组运行约 4 小时，已保存了 12500 step 的 checkpoint。磁盘 91% 使用需留意，两个 depth checkpoint 各占 75G。

---
