# check westd gpu 20260519

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_gpu_20260519_20260519T005434_result.json`
- **Structured JSON:** [`6a51d2716e23337c04b8.json`](../../sessions/6a/6a51d2716e23337c04b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已完成。

```
GPU 0 (openvla_k09):  完成 | SR=62.0% (310/500) | 耗时 242min
  per-task: soup=70%, cream_cheese=28%, salad_dressing=76%, bbq=56%, ketchup=78%, tomato=70%, butter=42%, milk=60%, pudding=54%, oj=86%

GPU 1 (openvla_k095): 完成 | SR=69.4% (347/500) | 耗时 235min
  per-task: soup=76%, cream_cheese=38%, salad_dressing=84%, bbq=54%, ketchup=84%, tomato=82%, butter=46%, milk=74%, pudding=64%, oj=92%
```

k=0.95 (保留 95% tokens) 比 k=0.9 (保留 90%) 高 7.4pp，符合预期。两者的瓶颈任务一致：cream_cheese 和 butter 最差。GPU 当前空闲，可复用。

---
