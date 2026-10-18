# analyze eval pi05 random k05 goal seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k05_goal_seed42_v2_20260523T213121_result.json`
- **Structured JSON:** [`4518f4da96c478e4307b.json`](../../sessions/45/4518f4da96c478e4307b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
RESULT:
- overall_sr: 73.6%
- per_task:
    T0 [open the middle drawer of the cabinet]: 78% (39/50)
    T1 [put the bowl on the stove]: 44% (22/50)
    T2 [put the wine bottle on top of the cabinet]: 86% (43/50)
    T3 [open the top drawer and put the bowl inside]: 76% (38/50)
    T4 [put the bowl on top of the cabinet]: 92% (46/50)
    T5 [push the plate to the front of the stove]: 70% (35/50)
    T6 [put the cream cheese in the bowl]: 62% (31/50)
    T7 [turn on the stove]: 100% (50/50)
    T8 [put the bowl on the plate]: 86% (43/50)
    T9 [put the wine bottle on the rack]: 42% (21/50)
- total_episodes: 500 (10 tasks × 50 eps)
- elapsed: 109.7 min
- anomalies: 无明显异常
- comparison: v1(pre-fix)=74.4%, v2(post-fix)=73.6% (Δ=-0.8pp)
  CPU RNG 修复对 Random pruning 几乎无影响（符合预期——random 不依赖 importance score 计算）
- monotonicity: k=0.7=78.2%, k=0.5=73.6%, k=0.3=50.6% — 单调递减 ✓
  随 keep_ratio 降低 SR 平稳下降，无异常跳变
- json_path: /root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.50_libero_goal_seed42.json
```

**关键发现**：
1. v1→v2 仅差 0.8pp，确认 CPU RNG 修复对 random pruning 无实质影响（random 不涉及 importance 计算，符合预期）
2. k=0.7→0.5→0.3 严格单调递减（78.2%→73.6%→50.6%），random baseline 行为符合直觉
3. T7(turn on stove) 100%、T9(wine bottle on rack) 42% 分别是最易/最难任务，与其他 keep_ratio 实验一致

---
