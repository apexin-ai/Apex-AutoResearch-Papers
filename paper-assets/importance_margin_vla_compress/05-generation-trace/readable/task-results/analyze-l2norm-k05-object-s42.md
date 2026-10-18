# analyze l2norm k05 object s42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_l2norm_k05_object_s42_20260525T122454_result.json`
- **Structured JSON:** [`541cb2d546cbcbda2e55.json`](../../sessions/54/541cb2d546cbcbda2e55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## L2norm k=0.5 Object seed42 结果

| 指标 | 值 |
|------|-----|
| **Overall SR** | **39.2% (196/500)** |
| Total episodes | 500 (10 tasks × 50 eps) |
| 耗时 | 264.6 min |
| Vision tokens | 256 → 128 (50% pruned) |

### Per-task SR

| Task | SR |
|------|-----|
| ketchup | 70.0% |
| alphabet_soup | 56.0% |
| milk | 50.0% |
| chocolate_pudding | 44.0% |
| orange_juice | 44.0% |
| salad_dressing | 38.0% |
| bbq_sauce | 32.0% |
| tomato_sauce | 32.0% |
| cream_cheese | 14.0% |
| butter | 12.0% |

### 退化曲线定位

| k_ratio | Object SR | 相对 baseline (96.2%) |
|---------|-----------|----------------------|
| 0.9 | 70.6% | -26.6pp |
| 0.7 | (已有) | — |
| **0.5** | **39.2%** | **-57.0pp** |
| 0.3 | (已有) | — |

k=0.5 时 L2norm 退化严重（39.2%），从 k=0.9 的 70.6% 进一步下降约 31pp。无异常 task（无全 0 或全 1）。butter 和 cream_cheese 最低（12%/14%），ketchup 最高（70%）。

---
