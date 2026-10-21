# analysis eval pi05 attention k085 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_attention_k085_long_seed42_v2_20260526T163015_result.json`
- **Structured JSON:** [`4b618d42499dfe1128de.json`](../../sessions/4b/4b618d42499dfe1128de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完毕。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **51.6%** (258/500) |
| Total episodes | 500 (10 tasks × 50 eps) |
| 运行时间 | 260.4 min (~4.47 GPU hours) |
| W&B | 无 |
| 异常 | 无 |

**Per-task SR：**

| Task | SR |
|------|-----|
| T0 alphabet_soup_tomato | 20% |
| T1 cream_cheese_butter | 54% |
| T2 stove_moka_pot | 32% |
| T3 black_bowl_drawer | 60% |
| T4 white_mug_left_plate | 48% |
| T5 book_back_shelf | 90% |
| T6 white_mug_plate | 68% |
| T7 alphabet_soup_cream | 46% |
| T8 moka_pots_stove | 6% |
| T9 yellow_white_mug_microwave | 92% |

**Cliff curve 定位：** Attn k=0.85 Long SR=51.6%，与 k=0.75 (51.8%) 几乎持平，说明 cliff 发生在 k=0.85~0.9 之间（k=0.9=63.8% → k=0.85=51.6% 骤降 12.2pp）。与 ROADMAP D245 记录的 51.6% 一致。Conclusion: success, status: DONE。

---
