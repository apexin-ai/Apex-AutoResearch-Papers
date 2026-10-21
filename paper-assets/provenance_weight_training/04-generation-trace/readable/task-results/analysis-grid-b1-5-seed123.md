# analysis grid b1 5 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b1_5_seed123_20260514T110803_result.json`
- **Structured JSON:** [`46753a2e31e794382793.json`](../../sessions/46/46753a2e31e794382793.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
METRICS:
eval_ppl_holdout: N/A (训练未配置 evaluation)
eval_loss: N/A
eval_holdout_tokens: N/A
train_loss: 10.4776
total_steps: 6103
train_runtime_s: 15053.1
gpu_hours: 4.18
wandb_run_id: N/A

CHECKPOINT:
path: /root/provenance_weight_training/output/models/grid_b1_5_seed123/final/
exists: true
size_mb: ~1137 (model.safetensors 1192MB)

ANOMALIES:
- 无 OOM、NaN、error
- 唯一 warning: FutureWarning `tokenizer` deprecated, use `processing_class` (无害)
- train_loss 偏高 (10.48)，loss 从 ~11.3 降到 ~9.9，仅训练 0.26 epoch
- 无 eval 步骤——训练脚本未配置 holdout evaluation，需要单独跑 eval
```

**关键发现**：这次训练**没有执行 evaluation**，日志中完全没有 eval 相关输出。需要用单独的 eval 脚本对 `final/` checkpoint 跑 held-out perplexity 才能拿到 eval_ppl_holdout 等指标。

---
