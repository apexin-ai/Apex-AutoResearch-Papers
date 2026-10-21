# analyze eval pi05 l2norm k03 long seed43 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k03_long_seed43_postfix_v2_20260524T205300_result.json`
- **Structured JSON:** [`a0fb3c662904d938a99e.json`](../../sessions/a0/a0fb3c662904d938a99e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果如下：

## L2norm k=0.3 Long seed43 结果：**39.2%**

### Per-task breakdown

| Task | SR |
|------|-----|
| T0: put alphabet soup + tomato sauce in basket | 26% |
| T1: put cream cheese + butter in basket | 24% |
| T2: turn on stove + put moka pot | 90% |
| T3: put black bowl in drawer + close | 92% |
| T4: put white mug left + yellow mug right | 26% |
| T5: pick up book + place in caddy | 20% |
| T6: put white mug on plate + chocolate pudding | 8% |
| T7: put alphabet soup + cream cheese in basket | 62% |
| T8: put both moka pots on stove | 6% |
| T9: put yellow mug in microwave + close | 38% |

**总体**: 196/500 = 39.2%, 耗时 223.3 min, 无错误。

### Dual-seed 汇总

| 指标 | L2norm k=0.3 | Random k=0.3 |
|------|-------------|--------------|
| seed42 | 40.6% | 29.6% |
| seed43 | 39.2% | 28.0% |
| **Mean ± Std** | **39.9% ± 0.7pp** | **28.8% ± 0.8pp** |
| **Margin (L2norm − Random)** | | |
| seed42 | +11.0pp | |
| seed43 | +11.2pp | |
| **Mean margin** | **+11.1pp ± 0.1pp** | |

Dual-seed 验证结果非常一致：两个 seed 的 margin 几乎相同（+11.0 vs +11.2pp），L2norm 的 seed 间方差极小（±0.7pp）。L2norm 在极端 pruning (70% token 删除) 下相比 Random 有稳定的 ~11pp 优势。

---
