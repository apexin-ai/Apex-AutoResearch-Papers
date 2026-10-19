# ops collect object bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-object-bjb1-32546_20260515T043846_result.json`
- **Structured JSON:** [`dcfb1ec0e670852054ec.json`](../../sessions/dc/dcfb1ec0e670852054ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated for all 6 experiments. Summary:

**所有 6 个实验仍在运行中，进程启动于 ~2 小时前（10:37–11:00 UTC），并非 12+ 小时。**

### eval-vla-only-object (K=1, 最快)
```
Status: RUNNING, Tasks: 9.5/10
T1  alphabet_soup:       0% (0/10)
T2  cream_cheese:       10% (1/10)
T3  salad_dressing:     20% (2/10)
T4  bbq_sauce:          20% (2/10)
T5  ketchup:             0% (0/10)
T6  tomato_sauce:       10% (1/10)
T7  butter:              0% (0/10)
T8  milk:               10% (1/10)
T9  chocolate_pudding:  20% (2/10)
T10 orange_juice:       rollout 5/10 (2/5 so far)
Partial overall: 7.8% (7/90)
```

### 其余 5 个实验 (K=10)
```
Status: RUNNING, Tasks: 1/10
T1 alphabet_soup: 0% (0/10) — 全部相同
预计总时间: ~18-20 小时（每 task ~2 小时 × 10 tasks）
```

K=10 实验每步需要 10 次 VLA forward pass，所以比 K=1 慢 ~10 倍。预计还需 ~16-18 小时完成。

---
