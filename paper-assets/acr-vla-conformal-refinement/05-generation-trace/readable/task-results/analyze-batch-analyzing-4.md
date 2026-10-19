# analyze batch analyzing 4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_batch-analyzing-4_20260520T105117_result.json`
- **Structured JSON:** [`0a8c381d67c164a97f70.json`](../../sessions/0a/0a8c381d67c164a97f70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常完成，日志中均无 W&B run ID。结果如下：

---

```
exp_id: eval-obs-only-object-norm003-seed44
success_rate: 15.0% (15/100)
per_task: [alphabet_soup: 0/10, cream_cheese: 0/10, salad_dressing: 3/10,
           bbq_sauce: 2/10, ketchup: 0/10, tomato_sauce: 1/10,
           butter: 1/10, milk: 2/10, chocolate_pudding: 3/10, orange_juice: 3/10]
wandb_run_id: 无
conclusion: success (15.0% > 11.6% VLA-only)
备注: ε=0.03 K=10。与 seed42 的 16% 基本一致，seed 间方差小。
```

```
exp_id: eval-crm-object-k20-seed44
success_rate: 18.0% (18/100)
per_task: [alphabet_soup: 0/10, cream_cheese: 0/10, salad_dressing: 3/10,
           bbq_sauce: 3/10, ketchup: 0/10, tomato_sauce: 1/10,
           butter: 1/10, milk: 3/10, chocolate_pudding: 4/10, orange_juice: 3/10]
wandb_run_id: 无
conclusion: success (18.0% > 11.6% VLA-only)
备注: 实际参数 K=20 + max_correction_norm=0.2（非 ε=0.03）。
      output_file = logs/eval_object_obs_only_norm02_K20_seed44.json。
      K=20(18%) > K=10(15%/16%) > K=5(16.7%)，K=20 是目前 Object 最高。
```

```
exp_id: eval-adaptive-k-spatial-p25-seed43
success_rate: 30.0% (30/100)
per_task: [between_plate_ramekin: 6/10, next_to_ramekin: 10/10,
           from_table_center: 0/10, on_cookie_box: 3/10,
           in_top_drawer: 1/10, on_ramekin: 0/10,
           next_to_cookie_box: 8/10, on_stove: 0/10,
           next_to_plate: 2/10, on_wooden_cabinet: 0/10]
wandb_run_id: 无
conclusion: success (30.0% > 11.6% VLA-only)
备注: adaptive_k τ=P25, fast_path=29.5%, avg_k=7.6, mean_l2=0.0890
```

```
exp_id: eval-adaptive-k-spatial-p25-seed42
success_rate: 33.0% (33/100)
per_task: [between_plate_ramekin: 7/10, next_to_ramekin: 10/10,
           from_table_center: 0/10, on_cookie_box: 3/10,
           in_top_drawer: 1/10, on_ramekin: 0/10,
           next_to_cookie_box: 9/10, on_stove: 0/10,
           next_to_plate: 3/10, on_wooden_cabinet: 0/10]
wandb_run_id: 无
conclusion: success (33.0% > 11.6% VLA-only)
备注: adaptive_k τ=P25, fast_path=29.4%, avg_k=7.7, mean_l2=0.0892
```

---

**要点总结：**

| 实验 | 成功率 | 对比基准 |
|------|--------|----------|
| obs_only ε=0.03 K=10 seed44 | 15.0% | ≈seed42(16%)，稳定 |
| obs_only K=20 ε=0.2 seed44 | **18.0%** | > K=10(15-16%), Object 新高 |
| adaptive_k spatial P25 seed43 | 30.0% | seed 间一致 |
| adaptive_k spatial P25 seed42 | **33.0%** | seed 间一致 |

Adaptive-K 两个 seed 结果高度一致（30% vs 33%，fast_path ≈29.5%，avg_k ≈7.6-7.7），方差可控。实验 2 注意实际用的是 ε=0.2 而非 0.03。

---
