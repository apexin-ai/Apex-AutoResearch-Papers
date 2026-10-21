# analysis contamination 60 tau07 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_contamination_60_tau07_seed42_20260516T055930_result.json`
- **Structured JSON:** [`3c677e41bd14c43b832e.json`](../../sessions/3c/3c677e41bd14c43b832e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
METRICS:
- eval_loss_holdout: N/A（训练未执行 eval）
- eval_ppl_holdout: N/A
- eval_loss_clean: N/A
- eval_loss_contaminated: N/A
- eval_holdout_tokens: N/A
- final_train_loss: 9.358 (avg), 最后一步 9.5033
- total_steps: 6103
- total_tokens: 200,000,000 (num_train_tokens 配置值)

CHECKPOINT: /root/provenance_weight_training/output/models/contamination_60_tau07_seed42/final/
  (model.safetensors 1.1GB, 另有 checkpoint-5500, checkpoint-6000, checkpoint-6103)

LOG_STATUS: 正常完成 (EXIT_CODE=0), 无 error
  有 2 个 FutureWarning (torch_dtype / tokenizer deprecated), 不影响结果
```

**关键发现：这次训练没有跑 evaluation。** 日志中不存在任何 `eval_*` 指标，只有 per-step training loss 和 per-batch weighting 统计。需要单独跑 eval 才能获得 holdout PPL 来和基准对比。

训练配置确认：`adaptive, τ=0.7, n_min=2, ρ=0.6, Qwen3-0.6B, lr=5e-5, batch_size=4, seed=42`

另外注意 train_loss ~9.35 偏高，但 step_metrics.jsonl 中单条 unweighted_loss 在 1.0-2.8 范围内是合理的。报告的 `loss` 可能是 batch 内 weighted_loss 的求和（batch_size=4, 4×~2.3≈9.2），而非均值。

---
