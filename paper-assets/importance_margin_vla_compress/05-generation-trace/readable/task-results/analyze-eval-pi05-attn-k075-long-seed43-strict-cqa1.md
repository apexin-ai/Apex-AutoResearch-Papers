# analyze eval pi05 attn k075 long seed43 strict cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_attn_k075_long_seed43_strict_cqa1_20260527T222944_result.json`
- **Structured JSON:** [`6ee9354eb59d9ca724d0.json`](../../sessions/6e/6ee9354eb59d9ca724d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**π0.5 Attn k=0.75 Long seed43: SR = 52.0%**

| Task | SR |
|------|-----|
| T0 alphabet_soup_tomato | 68% |
| T1 cream_cheese_butter | 64% |
| T2 stove_moka_pot | 64% |
| T3 black_bowl_drawer | 40% |
| T4 white_mug_left_plate | 36% |
| T5 book_back_shelf | 44% |
| T6 white_mug_plate | 82% |
| T7 alphabet_soup_cream | 30% |
| T8 moka_pots_stove | 10% |
| T9 yellow_white_mug_microwave | 82% |

### 与 seed42 对比

| | seed42 | seed43 | mean±std |
|--|--------|--------|----------|
| SR | 49.8% | 52.0% | **50.9%±1.1%** |

seed43 比 seed42 高 2.2pp，两个 seed 的 mean 为 50.9%±1.1%（较之前 ROADMAP 的 49.4%±0.4 上修）。error bar 很小，确认 Attn k=0.75 plateau 稳定在 ~51% 附近。无 error/warning，EXIT_CODE=0，运行时间 253.7min（~4.2h）。Registry 已更新为 DONE。

---
