# diagnose all servers status check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_all_servers_status_check_20260528T060058_result.json`
- **Structured JSON:** [`9377a12bc048220b171e.json`](../../sessions/93/9377a12bc048220b171e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the complete status:

```
[服务器状态]
w27 (2 GPU):
  cuda:0 = 在跑 eval_openvla_l2norm_k095_long_seed43_w27 (OV, T1 刚启动)
  cuda:1 = 空闲

w38 (4 GPU):
  cuda:0 = 在跑 eval_pi05_random_k095_long_seed45_strict_w38 (T4, ~59min)
  cuda:1 = 在跑 eval_pi05_l2norm_k095_long_seed45_strict_w38 (T9 ep40, 100%连续, ~112min, 即将完成)
  cuda:2 = 在跑 eval_pi05_random_k07_long_seed45_strict_w38 (T4, ~59min)
  cuda:3 = 在跑 eval_pi05_attn_k085_long_seed46_strict_w38 (T0, 刚启动)

w41 (4 GPU):
  cuda:0 = 在跑 eval_pi05_random_k085_long_seed46_strict_w41 (T0, 刚启动)
  cuda:1 = 在跑 eval_openvla_random_k095_long_seed43_w41 (OV, T2, ~30min)
  cuda:2 = 在跑 eval_pi05_l2norm_k075_long_seed46_strict_w41 (T0, 刚启动)
  cuda:3 = 在跑 eval_pi05_attn_k07_long_seed45_strict_w41 (T2, ~30min)

cqa1 (4 GPU):
  cuda:0 = 在跑 eval_pi05_l2norm_k05_long_seed45_strict_cqa1 (T8, ~172min)
  cuda:1 = 空闲
  cuda:2 = 在跑 eval_openvla_random_k095_goal_seed42_v4 (OV, T1 刚启动)
  cuda:3 = 空闲
```

```
[收割结果]
eval_pi05_random_k07_long_seed44_strict_w27:  SR=64.4%  (150min)
  per_task: [88, 58, 78, 76, 80, 42, 64, 70, 12, 76]

eval_pi05_attn_k095_long_seed45_strict_cqa1: SR=77.8%  (217min)
  per_task: [94, 98, 78, 94, 84, 98, 16, 84, 38, 94]
```

```
[空闲 GPU 列表]
w27:cuda:1, cqa1:cuda:1, cqa1:cuda:3  — 共 3 张空闲

[即将空闲]
w38:cuda:1 — eval_pi05_l2norm_k095_long_s45 在 T9 且全 100%, 预计 ~10min 内完成
cqa1:cuda:0 — eval_pi05_l2norm_k05_long_s45 在 T8, 预计 ~30min 内完成
```

---
