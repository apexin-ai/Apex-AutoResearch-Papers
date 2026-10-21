# verify w41074 gpu01 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_w41074_gpu01_status_20260527T102116_result.json`
- **Structured JSON:** [`1e7fa4da402f5a93d9c5.json`](../../sessions/1e/1e7fa4da402f5a93d9c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况 A：两个实验都在正常运行。**

| 实验 | GPU | PID | 当前进度 | 运行时间 |
|------|-----|-----|---------|---------|
| `eval_pi05_random_k09_long_seed42_strict_v2` | cuda:0 | 356361 | Task 3, ep20, 总体 32.0% (48/150) | ~4h 43min |
| `eval_pi05_random_k05_long_seed42_strict_w41_v2` | cuda:1 | 356612 | Task 4, ep10, 总体 63.0% (126/200) | ~4h 43min |

Registry 已从 PREPARING 更新为 RUNNING，spec（server, gpu, pid, command）已补充完整。无需重新部署。

---
