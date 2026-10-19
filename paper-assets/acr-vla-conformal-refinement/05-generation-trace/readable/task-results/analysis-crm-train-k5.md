# analysis crm train k5

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crm-train-k5_20260514T041336_result.json`
- **Structured JSON:** [`c72f41b06727d2f175ab.json`](../../sessions/c7/c72f41b06727d2f175ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
METRICS:
best_val_loss: 0.008996
best_epoch: 49
total_epochs: 50
final_val_loss: 0.008997
final_train_loss: 0.013847
checkpoint_path: /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt
checkpoint_exists: true

COMPARISON:
K10_val_loss: 0.009046
K5_val_loss: 0.008996
delta_pct: -0.55%
conclusion: K5 comparable (±5% threshold)
```

K=5 实际上略优于 K=10（val_loss 低 0.55%），在 ±5% 阈值内属于 comparable。训练跑满 50 epochs，无 early stop，收敛正常。

---
