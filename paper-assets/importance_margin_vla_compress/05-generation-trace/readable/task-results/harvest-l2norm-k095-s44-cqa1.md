# harvest l2norm k095 s44 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_l2norm_k095_s44_cqa1_20260528T015848_result.json`
- **Structured JSON:** [`7f7c545e02ef9eb4e412.json`](../../sessions/7f/7f7c545e02ef9eb4e412.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果汇总

**L2norm k=0.95 seed44: SR = 86.8%**

| Task | SR |
|------|-----|
| T0 alphabet_soup_tomato | 94% |
| T1 cream_cheese_butter | 96% |
| T2 stove_moka_pot | 96% |
| T3 black_bowl_drawer | 98% |
| T4 white_mug_left_plate | 98% |
| T5 book_back_shelf | 98% |
| T6 white_mug_plate_yellow | **46%** |
| T7 alphabet_soup_cream | 96% |
| T8 both_moka_pots_stove | **52%** |
| T9 yellow_white_mug_microwave | 94% |

**3-seed 汇总 (L2norm k=0.95):**

| Seed | SR |
|------|------|
| s42 | 85.8% |
| s43 | 86.2% |
| s44 | 86.8% |
| **Mean ± std** | **86.3% ± 0.4pp** |

与 2-seed mean (86.0%±0.2pp) 相比，s44 略高，3-seed mean 上升到 86.3%，方差依然很小（0.4pp），结果稳定。T6 和 T8 仍是跨 seed 的一致弱点。

---
