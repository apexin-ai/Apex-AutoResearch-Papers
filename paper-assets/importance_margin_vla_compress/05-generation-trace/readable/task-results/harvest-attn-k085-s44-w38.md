# harvest attn k085 s44 w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_attn_k085_s44_w38_20260528T005523_result.json`
- **Structured JSON:** [`c53315c261426426ffa5.json`](../../sessions/c5/c53315c261426426ffa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**π0.5 Attention k=0.85 Long seed44**: SR = **49.4%** (247/500, 185.6 min)

### Per-task breakdown (seed44)

| Task | SR% |
|------|-----|
| T0 alphabet_soup_tomato | 12 |
| T1 cream_cheese_butter | 58 |
| T2 stove_moka_pot | 48 |
| T3 black_bowl_drawer | 52 |
| T4 white_mug_left_plate | 34 |
| T5 book_back_shelf | 84 |
| T6 white_mug_plate | 64 |
| T7 alphabet_soup_cream | 56 |
| T8 moka_pots_stove | 6 |
| T9 yellow_white_mug_microwave | 80 |

### 3-seed 汇总 (Attention k=0.85 Long)

| Seed | SR% |
|------|-----|
| 42 | 50.0 |
| 43 | 52.4 |
| 44 | 49.4 |
| **Mean ± Std** | **50.6% ± 1.3** |

Registry 已更新为 DONE/success，cron 已删除。

3-seed 均值从之前的 2-seed 51.2%±1.2 修正为 **50.6%±1.3**，cliff→plateau transition 在 k=0.85 处稳定复现。

---
