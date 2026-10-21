# ops check m128 seed43 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-m128-seed43-result_20260520T083330_result.json`
- **Structured JSON:** [`f4584ecb568a38b6f2f9.json`](../../sessions/f4/f4584ecb568a38b6f2f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

## eval_smart_compress_m128_seed43 (libero_object, 500 eps/task)

| Task | Description | SR |
|------|-------------|-----|
| 0 | alphabet soup → basket | 64.6% |
| 1 | cream cheese → basket | 32.2% |
| 2 | salad dressing → basket | 61.4% |
| 3 | bbq sauce → basket | 43.2% |
| 4 | ketchup → basket | 34.8% |
| 5 | tomato sauce → basket | 44.2% |
| 6 | butter → basket | 71.6% |
| 7 | milk → basket | 60.4% |
| 8 | chocolate pudding → basket | 81.8% |
| 9 | orange juice → basket | 45.8% |
| **Overall** | | **54.0%** [52.6%, 55.4%] |

## eval_smart_compress_m16_seed43 (libero_object, 500 eps/task)

| Task | Description | SR |
|------|-------------|-----|
| 0 | alphabet soup → basket | 42.8% |
| 1 | cream cheese → basket | 47.4% |
| 2 | salad dressing → basket | 66.2% |
| 3 | bbq sauce → basket | 48.4% |
| 4 | ketchup → basket | 74.2% |
| 5 | tomato sauce → basket | 40.0% |
| 6 | butter → basket | 79.2% |
| 7 | milk → basket | 69.8% |
| 8 | chocolate pudding → basket | 76.6% |
| 9 | orange juice → basket | 39.4% |
| **Overall** | | **58.4%** [57.0%, 59.8%] |

Cross-seed 汇总（prior seed42 数据）：
- **M=128**: seed42=59.8%, seed43=54.0%
- **M=16**: seed42=55.8%, seed43=58.4%

M=16 seed43 反而比 M=128 seed43 高 4.4pp，且 M=16 两个 seed 均值（57.1%）与 M=128 均值（56.9%）基本持平——极端压缩 (87.5%) 仍未显著掉点。

---
