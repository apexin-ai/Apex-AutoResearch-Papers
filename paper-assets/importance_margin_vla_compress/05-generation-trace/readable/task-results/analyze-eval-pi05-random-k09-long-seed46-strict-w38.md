# analyze eval pi05 random k09 long seed46 strict w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k09_long_seed46_strict_w38_20260528T095110_result.json`
- **Structured JSON:** [`4aa5925e5a71552f4bba.json`](../../sessions/4a/4aa5925e5a71552f4bba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

## π0.5 Random k=0.9 Long seed46 结果

**总体 SR: 33.4%** (167/500)，EXIT_CODE=0，无报错。

### Per-task breakdown

| Task | SR |
|---|---|
| T0 alphabet_soup_tomato | 12% |
| T1 cream_cheese_butter | 40% |
| T2 stove_moka_pot | 40% |
| T3 black_bowl_drawer | 52% |
| T4 white_mug_left_plate | 24% |
| T5 book_back_shelf | 26% |
| T6 white_mug_plate | 12% |
| T7 alphabet_soup_cream | 44% |
| T8 moka_pots_stove | 8% |
| T9 yellow_white_mug_microwave | 76% |

### 5-seed 对比 (Random k=0.9 Long)

| Seed | SR |
|---|---|
| s42 | 34.2% |
| s43 | 35.0% |
| s44 | 31.8% |
| s45 | 33.2% |
| **s46** | **33.4%** |
| **Mean** | **33.52%** |
| **Std** | **±1.1pp** |

seed46 (33.4%) 落在已有 seeds 的范围内（31.8%–35.0%），与均值 33.52% 几乎一致。5-seed 标准差仅 1.1pp，Random k=0.9 的 error bar 非常紧凑。

---
