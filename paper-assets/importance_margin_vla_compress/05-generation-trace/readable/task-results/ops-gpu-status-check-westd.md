# ops gpu status check westd

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_westd_20260518T025328_result.json`
- **Structured JSON:** [`6f5f4394ee6704e596f0.json`](../../sessions/6f/6f5f4394ee6704e596f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
westd:0 — k=0.7: [running] Task 7/10, Ep 30/50
  完成: T1=0.96, T2=0.84, T3=0.64, T4=0.46, T5=0.68, T6=0.62

westd:1 — k=0.3: [running] Task 4/10, Ep 40/50
  完成: T1=0.14, T2=0.00, T3=0.64
```

k=0.3 剪枝率高，性能显著下降（T1 仅 0.14，T2 直接归零）。k=0.7 保留多，性能合理（均值约 0.70）。两个 GPU 利用率 ~60%，运行正常。

---
