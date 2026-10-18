# ops audit w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit-w27_20260527T165304_result.json`
- **Structured JSON:** [`3c18f4b1adff08bc5c16.json`](../../sessions/3c/3c18f4b1adff08bc5c16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，汇总：

```
GPU0: [完成] Random k=0.85 seed43 — 运行 ~169min
GPU1: [完成] L2norm k=0.85 seed43 — 运行 ~132min
```

### 结果

| 实验 | avg SR | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|------|--------|----|----|----|----|----|----|----|----|----|-----|
| **Random k=0.85 seed43** | **47.2%** | 96% | 42% | 56% | 82% | 16% | 46% | 38% | 40% | 10% | 76% |
| **L2norm k=0.85 seed43** | **78.6%** | 96% | 98% | 86% | 98% | 74% | 98% | 2% | 88% | 64% | 86% |

两块 GPU 当前均空闲，可部署新实验。

---
