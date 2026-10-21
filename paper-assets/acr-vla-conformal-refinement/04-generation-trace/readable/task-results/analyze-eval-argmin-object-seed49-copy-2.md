# analyze eval argmin object seed49

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-argmin-object-seed49_20260520T124000_result.json`
- **Structured JSON:** [`0fab0c00baa6ab62e18f.json`](../../sessions/0f/0fab0c00baa6ab62e18f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均完整完成，10/10 tasks，数据一致。结果如下：

---

```
exp_id: eval-argmin-object-seed49
SR: 16.0% (16/100)
per_task:
  alphabet_soup:        0.0%  (0/10)
  cream_cheese:         0.0%  (0/10)
  salad_dressing:      20.0%  (2/10)
  bbq_sauce:           40.0%  (4/10)
  ketchup:              0.0%  (0/10)
  tomato_sauce:        10.0%  (1/10)
  butter:              10.0%  (1/10)
  milk:                30.0%  (3/10)
  chocolate_pudding:   30.0%  (3/10)
  orange_juice:        20.0%  (2/10)
tasks_completed: 10/10
total_rollouts: 100
log_path: /root/acr-vla-conformal-refinement/logs/eval-argmin-object-seed49.log
json_path: /root/acr-vla-conformal-refinement/logs/eval_argmin_object_seed49.json
checkpoint_path: N/A (eval only)

exp_id: eval-argmin-object-seed48
SR: 15.0% (15/100)
per_task:
  alphabet_soup:        0.0%  (0/10)
  cream_cheese:         0.0%  (0/10)
  salad_dressing:      20.0%  (2/10)
  bbq_sauce:           30.0%  (3/10)
  ketchup:              0.0%  (0/10)
  tomato_sauce:        10.0%  (1/10)
  butter:              10.0%  (1/10)
  milk:                20.0%  (2/10)
  chocolate_pudding:   40.0%  (4/10)
  orange_juice:        20.0%  (2/10)
tasks_completed: 10/10
total_rollouts: 100
log_path: /root/acr-vla-conformal-refinement/logs/eval-argmin-object-seed48.log
json_path: /root/acr-vla-conformal-refinement/logs/eval_argmin_object_seed48.json
checkpoint_path: N/A (eval only)
```

两个 seed 结果非常接近（16% vs 15%），per-task 分布也基本一致。日志中未包含 W&B run URL。

---
