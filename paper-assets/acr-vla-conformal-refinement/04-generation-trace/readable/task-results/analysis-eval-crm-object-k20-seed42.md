# analysis eval crm object k20 seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-crm-object-k20-seed42_20260520T103217_result.json`
- **Structured JSON:** [`c543168ddbb6a763b277.json`](../../sessions/c5/c543168ddbb6a763b277.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

```
SR: 20.0% (20/100)
Per-task SRs:
  alphabet_soup:       0.0%
  cream_cheese:       10.0%
  salad_dressing:     30.0%
  bbq_sauce:          40.0%
  ketchup:            10.0%
  tomato_sauce:       10.0%
  butter:             10.0%
  milk:               10.0%
  chocolate_pudding:  50.0%
  orange_juice:       30.0%

vs K=10 (16.8%): +3.2pp
vs VLA-only (10.9%): +9.1pp
Conclusion: success
理由: K=20 (20.0%) 相比 K=10 (16.8%±1.8%) 仅提升 +3.2pp，而计算量翻倍。
K=1→K=10 的增益远大于 K=10→K=20 的边际增益，呈现明显的收益递减。
这支持 K=10 是 compute-efficient 的选择点——花 2x 推理成本仅换来约 3pp 的提升，
性价比不高。单 seed 结果（20.0%）落在 K=10 分布的 ~1.8σ 处，差异不算显著。
```

---
