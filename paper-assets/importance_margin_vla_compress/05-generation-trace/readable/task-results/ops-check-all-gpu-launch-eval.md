# ops check all gpu launch eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_gpu_launch_eval_20260518T034902_result.json`
- **Structured JSON:** [`d846bf840490c5f54bb3.json`](../../sessions/d8/d846bf840490c5f54bb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有训练仍在运行，M=96 和 M=16 非常接近完成但尚未结束，无需启动 eval。

```
=== cqa1-33015 ===
GPU 0: M=128 train — PID 685994 alive, step 12,950/100,000 (13%)
GPU 1: idle
GPU 2: M=96 train — step 99,200/100,000 (99.2%), ~3 min to finish
GPU 3: M=16 train — step 96,750/100,000 (96.8%), ~13 min to finish

=== westd-27271 ===
GPU 0: k=0.7 — Task 9/10 (Ep 20/50), 8 tasks done
  SRs: 0.740, 0.180, 0.640, 0.460, 0.680, 0.620, 0.100, 0.400
GPU 1: k=0.3 — Task 6/10 (Ep 30/50), 5 tasks done
  SRs: 0.140, 0.000, 0.640, 0.300, 0.300
```

M=96 约 3 分钟完成，M=16 约 13 分钟完成。要不要我等几分钟后再检查并自动启动 eval？

---
