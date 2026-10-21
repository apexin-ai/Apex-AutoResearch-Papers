# analyze eval pi05 l2norm k07 long seed44 strict w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k07_long_seed44_strict_w27_20260528T000104_result.json`
- **Structured JSON:** [`5a6286d0e485c099fd3d.json`](../../sessions/5a/5a6286d0e485c099fd3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**最终 SR: 63.8%** (319/500)，EXIT_CODE=0，无报错。

### 3-seed 统计 (L2norm k=0.7, Long)

| seed | SR |
|------|-----|
| 42 | 63.2% |
| 43 | 65.4% |
| 44 | 63.8% |
| **mean±std** | **64.1% ± 1.1%** |

与 2-seed 的 64.3%±1.1% 基本一致，第三个种子落在已有 error bar 范围内，方差没有增大。

### Per-task breakdown (seed44)

| Task | SR |
|------|-----|
| T0 alphabet_soup_tomato | 74% |
| T1 cream_cheese_butter | 88% |
| T2 stove_moka_pot | 76% |
| T3 black_bowl_drawer | 46% |
| T4 white_mug_left_plate | 56% |
| T5 book_back_shelf | 78% |
| T6 white_mug_plate | 60% |
| T7 alphabet_soup_cream | 60% |
| T8 both_moka_pots | 8% |
| T9 yellow_white_mug_microwave | 92% |

### Hypothesis 判断

**确认。** seed44=63.8% 与前两个种子高度一致，3-seed mean 64.1%±1.1% 的低方差证实 L2norm k=0.7 在 Long suite 上呈现稳定的 smooth degradation，而非 cliff-like drop。这为 L2norm 下降段 vs Attn cliff 后平台段的对比提供了可靠的统计基础。

---
