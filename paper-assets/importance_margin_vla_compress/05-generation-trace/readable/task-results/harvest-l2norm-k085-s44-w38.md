# harvest l2norm k085 s44 w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_l2norm_k085_s44_w38_20260528T014705_result.json`
- **Structured JSON:** [`bce276de90064e280028.json`](../../sessions/bc/bce276de90064e280028.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验完成 ✓** — registry 已更新为 DONE/success，cron 已删除。

## seed44 结果: SR=76.6%

| Task | SR |
|------|-----|
| T0 alphabet_soup_tomato | 98% |
| T1 cream_cheese_butter | 94% |
| T2 stove_moka_pot | 88% |
| T3 black_bowl_drawer | **100%** |
| T4 white_mug_left_plate | 64% |
| T5 book_back_shelf | 90% |
| T6 white_mug_plate | 6% |
| T7 alphabet_soup_cream | 82% |
| T8 moka_pots_stove | 52% |
| T9 yellow_white_mug_microwave | 92% |

## 3-seed 汇总: π0.5 L2norm k=0.85 Long

| Seed | SR |
|------|-----|
| 42 | 77.6% |
| 43 | 78.6% |
| 44 | 76.6% |
| **Mean ± std** | **77.6% ± 1.0** |

相比 2-seed 的 78.1%±0.5，seed44 拉低了均值约 0.5pp，std 从 0.5 扩大到 1.0。T6 (white_mug_plate) 仍是三个 seed 一致的瓶颈 (6-8%)。

---
