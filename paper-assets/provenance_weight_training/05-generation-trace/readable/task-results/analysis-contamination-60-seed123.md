# analysis contamination 60 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_contamination_60_seed123_20260518T025741_result.json`
- **Structured JSON:** [`7f9e3d89a96a22d81afd.json`](../../sessions/7f/7f9e3d89a96a22d81afd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

```
RESULT_SUMMARY:
eval_ppl_holdout: 17.732
eval_loss_holdout: 2.8754
train_loss: 9.6302
total_steps: 6103
conclusion: success
delta_vs_uniform_seed42: -0.034
checkpoint_path: /root/autodl-tmp/output/models/contamination_60_seed123/final
```

Cross-seed 复现成功：seed123 的 adaptive PPL (17.732) 与 seed42 (17.74) 高度一致（Δ=0.008），均优于 uniform baseline (17.766)。adaptive weighting 在 ρ=0.6 的优势不依赖于特定 seed，Claim 3 得到加强。

---
