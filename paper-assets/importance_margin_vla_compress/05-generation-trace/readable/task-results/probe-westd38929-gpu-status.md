# probe westd38929 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_westd38929-gpu-status_20260522T004040_result.json`
- **Structured JSON:** [`805e2f4487d7fce1b211.json`](../../sessions/80/805e2f4487d7fce1b211.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

```
GPU0: π0.5 L2norm k=0.9 Spatial seed42  PID=48433  状态=alive  进度=350/500 (T6完成, 进入T7)  GPU占用=10044 MiB  利用率=43%
GPU1: π0.5 random k=0.9 Spatial seed42  PID=9135   状态=alive  进度=300/500 (T5完成, 进入T6)  GPU占用=10602 MiB  利用率=46%
GPU2: π0.5 random k=0.925 Object seed43 PID=68039  状态=alive  进度=~160/500 (T3 ep10/50)    GPU占用=10541 MiB  利用率=56%
GPU3: π0.5 random k=0.85 Spatial seed42 PID=48598  状态=alive  进度=~190/500 (T3 ep40/50)    GPU占用=10038 MiB  利用率=14%
```

**GPU1 确认**：跑的是 `π0.5 random k=0.9 Spatial seed42`，之前未知的实验。

**中间结果概览**：
| GPU | 实验 | 当前累积 SR |
|-----|------|------------|
| 0 | l2norm k=0.9 Spatial | 94.9% (332/350) |
| 1 | random k=0.9 Spatial | 50.0% (150/300) |
| 2 | random k=0.925 Object | 39.3% (59/150) |
| 3 | random k=0.85 Spatial | 74.7% (112/150) |

GPU0 的 l2norm k=0.9 表现极强（94.9%），远超 random k=0.9（50.0%），差距非常显著。预计全部实验还需 ~1-1.5 小时完成。

---
