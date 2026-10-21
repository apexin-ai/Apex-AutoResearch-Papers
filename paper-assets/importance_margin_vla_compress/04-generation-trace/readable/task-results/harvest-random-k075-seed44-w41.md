# harvest random k075 seed44 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_random_k075_seed44_w41_20260528T003912_result.json`
- **Structured JSON:** [`bf8f9f7b373f79cede7e.json`](../../sessions/bf/bf8f9f7b373f79cede7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在，无需删除。所有信息已收集完毕。

## 结果

**eval_pi05_random_k075_long_seed44_strict_w41** — 成功完成

**Overall SR: 64.6%** (323/500)

### Per-task breakdown
| Task | SR |
|---|---|
| T0 alphabet_soup_tomato | 90% |
| T1 cream_cheese_butter | 72% |
| T2 stove_moka_pot | 72% |
| T3 black_bowl_drawer | 76% |
| T4 white_mug_plate | 68% |
| T5 book_back_shelf | 42% |
| T6 white_mug_plate_2 | 74% |
| T7 alphabet_soup_cream | 66% |
| T8 moka_pots_stove | **14%** |
| T9 yellow_white_mug_microwave | 72% |

### 3-seed 汇总 (Random k=0.75 Long)

ROADMAP 2-seed: mean=61.8%±1.2 → seed42≈60.6%, seed43≈63.0%

| Seed | SR |
|---|---|
| seed42 | ~60.6% |
| seed43 | ~63.0% |
| seed44 | **64.6%** |
| **3-seed mean** | **≈62.7%±2.0** |

Registry 已为 DONE/success 状态，metrics 已填充。Margin vs L2norm k=0.75 (72.0%): **+9.3pp**，与 2-seed margin (+10.2pp) 基本一致。

---
