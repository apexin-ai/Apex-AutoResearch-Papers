# diagnose cqa1 w27 urgent harvest

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_w27_urgent_harvest_20260528T060706_result.json`
- **Structured JSON:** [`1dc75b0f93080cb25338.json`](../../sessions/1d/1dc75b0f93080cb25338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

```
[cqa1 状态]
cuda:0: 在跑 — eval_pi05_l2norm_k05_long_seed45_strict_cqa1, T8完成 49.6%, T9剩余 ~30min
cuda:1: 空闲 — eval_pi05_attn_k095_long_seed45_strict_cqa1 已完成
cuda:2: 在跑 — eval_openvla_random_k095_goal_seed42_v4, T1 ep30/50, 刚启动 ~数小时
cuda:3: 空闲

[w27 状态]
cuda:0: 在跑 — eval_openvla_l2norm_k095_long_seed43_w27, T1 ep10/50, 刚启动 ~数小时
cuda:1: 空闲 — eval_pi05_random_k07_long_seed44_strict_w27 已完成

[收割结果]
eval_pi05_attn_k095_long_seed45_strict_cqa1: SR=77.8% EXIT_CODE=0 217min
  per_task: [94, 98, 78, 94, 84, 98, 16, 84, 38, 94]

eval_pi05_random_k07_long_seed44_strict_w27: SR=64.4% EXIT_CODE=0 150min
  per_task: [88, 58, 78, 76, 80, 42, 64, 70, 12, 76]

[空闲 GPU]
cqa1: cuda:1, cuda:3
w27: cuda:1
```

---
