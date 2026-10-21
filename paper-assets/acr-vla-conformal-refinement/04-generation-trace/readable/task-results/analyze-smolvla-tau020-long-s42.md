# analyze smolvla tau020 long s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_smolvla-tau020-long-s42_20260528T042419_result.json`
- **Structured JSON:** [`78c1d7d9fb7b268e2219.json`](../../sessions/78/78c1d7d9fb7b268e2219.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

```
实验: smolvla-tau020-long-s42
success_rate: 0.585 (117/200)
trigger_rate: 8.9%
mean_uncertainty: 0.1226
wall_clock: 20202s (~5.6 GPU-hrs)
conclusion: success (58.5% ≥ baseline 58%)

Per-task:
  KITCHEN_SCENE3_stove_moka_pot:           95.0% (19/20)
  KITCHEN_SCENE4_black_bowl_drawer:        95.0% (19/20)
  LIVING_ROOM_SCENE2_cream_cheese_butter:  90.0% (18/20)
  STUDY_SCENE1_book_caddy:                 90.0% (18/20)
  KITCHEN_SCENE6_mug_microwave:            65.0% (13/20)
  LIVING_ROOM_SCENE1_alphabet_soup_cream:  60.0% (12/20)
  LIVING_ROOM_SCENE5_two_mugs_plates:      35.0% (7/20)
  LIVING_ROOM_SCENE6_mug_pudding:          30.0% (6/20)
  LIVING_ROOM_SCENE2_alphabet_soup_tomato: 25.0% (5/20)
  KITCHEN_SCENE8_two_moka_pots:             0.0% (0/20)

与相邻 τ 对比:
  τ=0.15: 61.0% (peak)
  τ=0.20: 58.5% (本次)
  τ=0.25: 56.0%
```

D170 假设结论：τ=0.20 (58.5%) 位于 τ=0.15 (61%) 和 τ=0.25 (56%) 之间，呈单调下降趋势（61→58.5→56），说明 τ=0.25 的 dip 不是孤立噪声，而是从 τ=0.15 峰值开始的平滑衰减。τ=0.15 仍是 Long suite 最优阈值。

---
