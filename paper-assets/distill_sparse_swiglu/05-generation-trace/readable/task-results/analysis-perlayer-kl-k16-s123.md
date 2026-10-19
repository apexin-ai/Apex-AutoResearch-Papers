# analysis perlayer kl k16 s123

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k16_s123_20260523T094319_result.json`
- **Structured JSON:** [`bcdeb0ec6d1b0aa21671.json`](../../sessions/bc/bcdeb0ec6d1b0aa21671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练完成，无 error/warning。

```
METRICS:
- final_kl: 0.1436 (step 1000)
- avg_kl: 0.1617
- avg_sparsity: 0.287 (step 1000), per-layer range 0.299–0.313
- wall_time_s: 1982.8 (~33 min)
- steps: 1000/1000
- final_avg_lambda: 2233.05
CHECKPOINT: /root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s123/predictor_perlayer_kl_k4.pt (145 MB)
STATUS: success (EXIT_CODE=0)
```

要点：sparsity 从 0.406 (step 1) 收敛到 ~0.29，略低于 target 0.3。KL 从 0.582 降到 avg 0.1617。Layer 24 和 31 的 final_lambda 异常低（0.16 和 0.08），说明这两层 sparsity 已经很低不需要额外惩罚。

---
