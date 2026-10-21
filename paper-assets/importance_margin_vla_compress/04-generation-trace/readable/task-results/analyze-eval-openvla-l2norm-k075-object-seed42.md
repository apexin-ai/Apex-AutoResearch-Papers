# analyze eval openvla l2norm k075 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_l2norm_k075_object_seed42_20260526T180648_result.json`
- **Structured JSON:** [`1c1cd86477f56199877a.json`](../../sessions/1c/1c1cd86477f56199877a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。log_path 已在 spec 中存在，无需重复设置。

```
实验: eval_openvla_l2norm_k075_object_seed42
Overall SR: 57.4%
Episodes: 287/500
每 task 成绩:
  alphabet_soup:      78.0% (39/50)
  cream_cheese:       28.0% (14/50)
  salad_dressing:     68.0% (34/50)
  bbq_sauce:          46.0% (23/50)
  ketchup:            86.0% (43/50)
  tomato_sauce:       66.0% (33/50)
  butter:             40.0% (20/50)
  milk:               48.0% (24/50)
  chocolate_pudding:  46.0% (23/50)
  orange_juice:       68.0% (34/50)
Conclusion: negative
理由: SR=57.4% 比 baseline 74.0% 低 16.6pp。L2norm cliff 曲线确认：
  k=0.95: 70.6% → k=0.9: 70.6% → k=0.75: 57.4% → k=0.7: 49.8% → k=0.5: 39.2%
  k=0.9→0.75 区间下降 13.2pp，Object suite 在 25% token 裁剪时已严重退化。
```

---
