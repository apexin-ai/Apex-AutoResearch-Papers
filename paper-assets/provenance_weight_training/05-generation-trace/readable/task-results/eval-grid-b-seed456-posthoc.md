# eval grid b seed456 posthoc

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grid_b_seed456_posthoc_20260515T005316_result.json`
- **Structured JSON:** [`4b6c35515791279d3a79.json`](../../sessions/4b/4b6c35515791279d3a79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总结果：

```
grid_b1_0_seed456:
  train_loss: 10.1779
  train_runtime_s: 12963.87
  total_steps: 6103
  eval_loss: 2.8725
  eval_ppl_holdout: 17.68
  eval_holdout_tokens: 4077068
  checkpoint_path: output/models/grid_b1_0_seed456/final

grid_b1_5_seed456:
  train_loss: 10.4348
  train_runtime_s: 12950.16
  total_steps: 6103
  eval_loss: 2.8741
  eval_ppl_holdout: 17.71
  eval_holdout_tokens: 4077068
  checkpoint_path: output/models/grid_b1_5_seed456/final
```

两个实验 holdout PPL 非常接近（17.68 vs 17.71），b=1.0 略优于 b=1.5。Registry 状态均已更新为 DONE/success。

---
