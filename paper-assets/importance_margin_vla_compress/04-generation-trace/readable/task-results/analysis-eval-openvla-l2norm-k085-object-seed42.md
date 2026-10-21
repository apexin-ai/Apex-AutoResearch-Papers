# analysis eval openvla l2norm k085 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_openvla_l2norm_k085_object_seed42_20260527T103831_result.json`
- **Structured JSON:** [`4582efdd5733cb65c8c5.json`](../../sessions/45/4582efdd5733cb65c8c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
overall_sr: 55.2%
per_task_sr:
  alphabet_soup: 60%
  cream_cheese: 40%
  salad_dressing: 60%
  bbq_sauce: 44%
  ketchup: 92%
  tomato_sauce: 42%
  butter: 50%
  milk: 58%
  chocolate_pudding: 52%
  orange_juice: 54%
n_episodes: 500
duration_min: 254.8
conclusion: success
analysis: 重跑结果与前次完全一致（overall 55.2%, 每个 task SR 逐一吻合），说明结果在 seed42 下是确定性的。k=0.85=55.2% < k=0.75=57.4% 的非单调性被确认——这不是随机波动，而是该 seed 下的稳定现象。L2norm cliff 曲线：k=0.95/0.9 → 70.6%（平台期），k=0.85 → 55.2%（陡降），k=0.75 → 57.4%（小幅回升），k=0.7 → 49.8%，k=0.5 → 39.2%。非单调点可能源于 L2norm 在 k=0.85 处裁剪掉了某些对特定 task 关键但 norm 不高的 token，而 k=0.75 的更激进裁剪反而保留了不同的 token 子集组合。
```

无错误无警告，EXIT_CODE=0，正常完成。

---
