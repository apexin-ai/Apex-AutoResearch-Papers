# analysis eval pi05 l2norm k09 goal seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k09_goal_seed42_postfix_20260524T104341_result.json`
- **Structured JSON:** [`5b09bbcfe0d32985ab06.json`](../../sessions/5b/5b09bbcfe0d32985ab06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
overall_sr: 88.6%
total_episodes: 500
per_task: [T0 open_drawer: 86%, T1 bowl_stove: 98%, T2 wine_cabinet: 94%, T3 drawer_bowl: 88%, T4 bowl_cabinet: 100%, T5 push_plate: 98%, T6 cream_cheese: 90%, T7 turn_stove: 100%, T8 bowl_plate: 94%, T9 wine_rack: 38%]
errors: none
conclusion: success
reasoning: L2norm k=0.9 (88.6%) ≈ baseline (88.4%) ≈ L2norm k=0.85 (87.4%)，性能无损；而 Random k=0.9 仅 54.8%，importance margin = 88.6% - 54.8% = 33.8pp，确认 cliff zone (k=0.9) importance-based pruning 优势最大。
```

**关键发现**: L2norm 在 k=0.85→0.9→0.925→0.95 整个范围内都维持 86-88% 水平（与 no-pruning baseline 88.4% 几乎无损），而 Random 在 k=0.9 时已暴跌至 54.8%。这证实了 importance margin 在 cliff zone 达到峰值 (~34pp)，是论文核心论点的强有力支撑。

---
