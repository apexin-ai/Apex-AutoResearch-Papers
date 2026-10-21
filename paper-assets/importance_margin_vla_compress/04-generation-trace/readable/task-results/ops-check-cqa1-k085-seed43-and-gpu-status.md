# ops check cqa1 k085 seed43 and gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cqa1-k085-seed43-and-gpu-status_20260520T220833_result.json`
- **Structured JSON:** [`9ddaed828ecdec159c77.json`](../../sessions/9d/9ddaed828ecdec159c77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## k=0.85 seed43 结果 — 已完成

**Overall: 67.6% (338/500), Wilson CI 95%: [0.634, 0.716]**

| Task | Description | Success Rate |
|------|------------|-------------|
| 0 | alphabet soup | 100% |
| 1 | cream cheese | 44% |
| 2 | salad dressing | 100% |
| 3 | bbq sauce | 88% |
| 4 | ketchup | 28% |
| 5 | tomato sauce | 90% |
| 6 | butter | 0% |
| 7 | milk | 94% |
| 8 | chocolate pudding | 34% |
| 9 | orange juice | 98% |

耗时 4750.6s (~79 min)。

## GPU 状态

| GPU | Util | Memory | 状态 |
|-----|------|--------|------|
| 0 | 0% | 1/24564 MiB | 空闲 |
| 1 | 1% | 4537/24564 MiB | k=0.8 seed44 运行中 |
| 2 | 1% | 4540/24564 MiB | k=0.85 seed44 运行中 |
| 3 | 0% | 1/24564 MiB | 空闲 |

## 运行中的实验

| Session | GPU | 实验 | PID |
|---------|-----|------|-----|
| eval_xvla_k08_s44 | 1 | k=0.8 seed44 | 563249 |
| eval_xvla_k085_s44 | 2 | k=0.85 seed44 | 609567 |

GPU 0 和 GPU 3 空闲可用。

---
