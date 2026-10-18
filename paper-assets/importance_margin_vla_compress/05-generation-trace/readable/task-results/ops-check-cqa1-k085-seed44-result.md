# ops check cqa1 k085 seed44 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cqa1-k085-seed44-result_20260520T231459_result.json`
- **Structured JSON:** [`e24583ac3734c9a4e10c.json`](../../sessions/e2/e24583ac3734c9a4e10c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## seed44 结果

- **success_rate: 68.2%** (341/500)
- **Wilson CI 95%: [0.640, 0.721]**
- GPU 2 已释放（1 MiB）

## X-VLA k=0.85 完整 3-seed 汇总

| seed | success_rate | successes/total | Wilson CI 95% |
|------|-------------|-----------------|---------------|
| 42 | 68.0% | 340/500 | [0.638, 0.719] |
| 43 | 67.6% | 338/500 | [0.634, 0.716] |
| 44 | 68.2% | 341/500 | [0.640, 0.721] |
| **mean±std** | **67.9±0.25%** | | |

## 完整 cliff localization 3-seed 表

| k | seed42 | seed43 | seed44 | mean±std |
|---|--------|--------|--------|----------|
| 0.95 | 99.0% | 99.0% | 99.4% | 99.1±0.19% |
| **0.85** | **68.0%** | **67.6%** | **68.2%** | **67.9±0.25%** |
| 0.8 | 88.8% | 88.4% | 89.8% | 89.0±0.59% |

k=0.85 三个 seed 高度一致，标准差仅 0.25pp，确认 cliff 区域在 k=0.85 附近。非单调性模式（k=0.85 < k=0.8）稳定复现。

---
