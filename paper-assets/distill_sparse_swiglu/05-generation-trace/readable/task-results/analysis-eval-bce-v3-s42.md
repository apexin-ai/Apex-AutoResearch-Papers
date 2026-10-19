# analysis eval bce v3 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_bce_v3_s42_20260516T075908_result.json`
- **Structured JSON:** [`007537f4f9826e0a47c6.json`](../../sessions/00/007537f4f9826e0a47c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

TaskOutput 需要一个活跃的 background task ID，这里日志是直接从服务器读取的，不存在对应的 task。完整结果已在上方输出。

汇总：

```
PPL (WikiText-2, sparsity_target=50%):
- true_dense_ppl: 6.12
- predictor_hard_mask_ppl: 22.51
- teal_sparse_ppl: 27.97
- model_level_sparsity: 0.500

Downstream (predictor per_token, global_topk):
- arc_challenge_acc: 0.2048 (±0.0118)
- arc_challenge_acc_norm: 0.2398 (±0.0125)
- winogrande_acc: 0.5059 (±0.0141)
- mmlu_acc: 0.3002 (±0.0038)
- gsm8k_exact_match (flexible): 0.0485 (±0.0059)
- gsm8k_exact_match (strict): 0.0425 (±0.0056)
```

Per-layer sparsity: Layer 0–17 在 0.43–0.50 范围，Layer 18–31 从 0.46 递增至 0.71。模型整体 sparsity = 0.500。

结果 JSON 完整保存在 `/root/distill_sparse_swiglu/results/benchmark/bce_isocompute_v3_s42/results.json`，包含 config、metrics 和 stderr。GSM8K 有 strict-match (0.0425) 和 flexible-extract (0.0485) 两个变体。

---
