# probe westd 41074 pids

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_westd-41074-pids_20260521T225904_result.json`
- **Structured JSON:** [`17b4330a7975d9ee227e.json`](../../sessions/17/17b4330a7975d9ee227e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 实验 | PID | GPU | 显存占用 | GPU 利用率 |
|------|-----|-----|---------|-----------|
| `eval_pi05_random_k0925_object_seed42` (keep_ratio=0.925, seed=42) | **715307** | GPU 0 | 10052 MiB | 9% |
| `eval_pi05_random_k095_object_seed43` (keep_ratio=0.95, seed=43) | **730309** | GPU 1 | 10545 MiB | 36% |

GPU 2/3 上还有其他进程（PID 68539 占 28546 MiB，PID 59671 占 27526 MiB），不属于这两个 eval 实验。

---
