# eval kl30 s456 uniform fix

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl30_s456_uniform_fix_20260517T173705_result.json`
- **Structured JSON:** [`713d98731113fee62eda.json`](../../sessions/71/713d98731113fee62eda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here are the results:

```
kl30_s456_uniform_eval 补全指标:
  arc_challenge_acc_norm: 0.4505
  winogrande_acc:         0.6875
  gsm8k_exact_match:      0.0758
  mmlu_acc (交叉验证):     0.4198 ✓ (与 registry 一致)
  ppl_wikitext2:          8.7947

kl30_s456_train:
  checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_30pct_s456/predictor_kl_normalized.pt
  log_path:        ~/runs/distill_sparse_swiglu/kl30_s456_train.log
  final_loss:      0.2021
  actual_sparsity: 0.289
  training_steps:  1000/1000
```

所有数据本来就已经跑完了（日志和 `results/benchmark/kl30_s456_uniform/results.json` 都有完整记录），只是 registry 的 metrics 字段当时漏填了 ARC/WG/GSM8K。已补全。

---
