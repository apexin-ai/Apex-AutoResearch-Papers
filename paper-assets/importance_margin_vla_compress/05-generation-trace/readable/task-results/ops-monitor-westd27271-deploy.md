# ops monitor westd27271 deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor_westd27271_deploy_20260522T063820_result.json`
- **Structured JSON:** [`0e2a0005705fe3785c3f.json`](../../sessions/0e/0e2a0005705fe3785c3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

### 已完成实验

| 实验 | GPU | Overall SR | 对比 seed42 | 差异 |
|------|-----|-----------|------------|------|
| **random k=0.95 spatial seed43** | 0 | **76.8%** | 84.4% | -7.6pp |
| **l2norm k=0.85 spatial seed43** | 1 | **88.0%** | 91.2% | -3.2pp |

**Per-task SR (seed43):**

| Task | random k=0.95 | l2norm k=0.85 |
|------|--------------|--------------|
| T0 | 100% | 100% |
| T1 | 94% | 92% |
| T2 | 100% | 100% |
| T3 | 60% | 78% |
| T4 | 36% | 62% |
| T5 | 76% | 84% |
| T6 | 90% | 96% |
| T7 | 74% | 90% |
| T8 | 100% | 96% |
| T9 | 38% | 82% |

L2norm k=0.85 跨种子稳定（仅-3.2pp），random k=0.95 种子间方差较大（-7.6pp），T4/T9 拖后腿严重。

### 已部署新实验

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| **eval_pi05_random_k07_spatial_seed43** | 0 | 119106 | RUNNING |
| **eval_pi05_l2norm_k07_spatial_seed43** | 1 | 119442 | RUNNING |

预计 ~80-90 分钟完成。

---
