# ops check xvla k08 seed42 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-xvla-k08-seed42-result_20260520T220004_result.json`
- **Structured JSON:** [`2c0882565cd45c5658f7.json`](../../sessions/2c/2c0882565cd45c5658f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## X-VLA k=0.8 seed42 结果

**overall_success_rate = 88.8%** (444/500), 95% Wilson CI: [85.7%, 91.3%]

### Per-task 明细

| Task | Description | Success Rate | Mean Steps |
|------|-------------|:---:|:---:|
| 0 | alphabet soup → basket | **100%** | 142.7 |
| 1 | cream cheese → basket | **98%** | 139.8 |
| 2 | salad dressing → basket | **100%** | 113.5 |
| 3 | bbq sauce → basket | 88% | 214.1 |
| 4 | ketchup → basket | 80% | 283.1 |
| 5 | tomato sauce → basket | **98%** | 145.8 |
| 6 | butter → basket | **56%** | 460.5 |
| 7 | milk → basket | 86% | 227.9 |
| 8 | chocolate pudding → basket | 88% | 240.3 |
| 9 | orange juice → basket | 94% | 177.2 |

### Monotonicity 分析

| Config | Keep Ratio | Tokens Kept | Success Rate |
|--------|:---:|:---:|:---:|
| k=0.85 seed42 | 85% | 42/50 | **68.0%** |
| k=0.8 seed42 | 80% | 40/50 | **88.8%** |

**反常现象出现**: k=0.8 (88.8%) **远高于** k=0.85 (68.0%)。保留更少 token 反而性能大幅提升 (+20.8pp)，monotonicity 不成立。这说明 k=0.85 的 68% 结果可能有问题（eval seed 不一致、checkpoint 异常、或 pruning 阈值恰好落在敏感区间），需要排查。

---
