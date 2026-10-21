# analyze 3x analyzing s46

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_3x_analyzing_s46_20260528T084835_result.json`
- **Structured JSON:** [`71e752e08ecb7157d67b.json`](../../sessions/71/71e752e08ecb7157d67b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个日志全部读取完毕，均正常退出。汇总：

---

```
exp_id: eval_pi05_attn_k085_long_seed46_strict_w38
server: westd-38929
overall_success_rate: 50.4
per_task_rates: [12.0, 62.0, 44.0, 52.0, 44.0, 72.0, 68.0, 60.0, 8.0, 86.0]
log_status: clean
```

```
exp_id: eval_pi05_random_k085_long_seed46_strict_w41
server: westd-41074
overall_success_rate: 44.8
per_task_rates: [50.0, 42.0, 46.0, 76.0, 20.0, 40.0, 40.0, 52.0, 6.0, 76.0]
log_status: clean
```

```
exp_id: eval_pi05_l2norm_k09_long_seed46_strict_w27
server: westd-27271
overall_success_rate: 80.6
per_task_rates: [96.0, 96.0, 94.0, 98.0, 88.0, 94.0, 8.0, 90.0, 52.0, 90.0]
log_status: clean
```

---

**汇总对比（libero_10, seed=46, 50 eps）：**

| Method | keep_ratio | Overall SR |
|--------|-----------|------------|
| L2norm | 0.90 | **80.6%** |
| Attention | 0.85 | 50.4% |
| Random | 0.85 | 44.8% |

L2norm k=0.9 大幅领先，但注意 keep_ratio 不同（0.9 vs 0.85）。L2norm 的 T6（put white mug on plate + tomato sauce）异常低（8.0%），其余 task 均在 52-98% 区间。

---
