# ops cqa1 check fill cuda0

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-check-fill-cuda0_20260521T081754_result.json`
- **Structured JSON:** [`4ed2514ebfd129274b18.json`](../../sessions/4e/4ed2514ebfd129274b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 仍在运行 `eval_xvla_random_k07_object_seed43_v2`（PID 547827，已运行 51 分钟，72% GPU 利用率）。

虽然 registry 已标记 DONE，但进程实际还在跑。可能是 registry 被提前标记了，或者这是一个重启的 run。

**当前 cqa1-33015 GPU 占用情况：**
| GPU | 进程 | 显存 | 利用率 |
|-----|-------|------|--------|
| cuda:0 | eval_xvla_random_k07_object_seed43 (PID 547827) | 4540 MiB | 72% |
| cuda:1 | PID 547900 | 4508 MiB | ~0% |
| cuda:2 | PID 707317 | 4540 MiB | 15% |
| cuda:3 | PID 660320 | 4540 MiB | 11% |

4 卡全部占用，无法部署 L2norm k=0.5 seed43。需要等 cuda:0 上的 seed43_v2 真正结束后再部署。

---
