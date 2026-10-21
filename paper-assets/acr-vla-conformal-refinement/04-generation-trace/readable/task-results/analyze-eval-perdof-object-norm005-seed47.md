# analyze eval perdof object norm005 seed47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-perdof-object-norm005-seed47_20260519T190310_result.json`
- **Structured JSON:** [`4d7c86e1b64dfd22aad6.json`](../../sessions/4d/4d7c86e1b64dfd22aad6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

```
exp_id: eval-perdof-object-norm005-seed47
conclusion: success
success_rate: 10%
per_task: [soup=0%, cream_cheese=0%, salad_dressing=10%, bbq_sauce=20%, ketchup=0%, tomato_sauce=0%, butter=10%, milk=0%, chocolate_pudding=40%, orange_juice=20%]
备注: ε=0.05, seed47, 10 tasks × 10 rollouts, 无报错
```

```
exp_id: eval-perdof-object-norm003-seed47
conclusion: success
success_rate: 15%
per_task: [soup=0%, cream_cheese=0%, salad_dressing=20%, bbq_sauce=30%, ketchup=0%, tomato_sauce=10%, butter=20%, milk=10%, chocolate_pudding=30%, orange_juice=30%]
备注: ε=0.03, seed47, 10 tasks × 10 rollouts, 无报错
```

ε=0.03 (15%) 整体优于 ε=0.05 (10%)，较小的 correction norm 在 8/10 个 task 上持平或更优，仅 chocolate_pudding 上 ε=0.05 更好 (40% vs 30%)。

---
