# eval kl sparsity40 global collect now

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl_sparsity40_global_collect_now_20260520T092650_result.json`
- **Structured JSON:** [`b54c2826d1fb617d46e6.json`](../../sessions/b5/b54c2826d1fb617d46e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Global eval 已完成。完整结果如下：

⚠️ **注意：config 中 sparsity_target=0.5，不是 0.4**——exp_id 写的是 `kl_sparsity40` 但实际跑的是 50% global_topk allocation。

---

## Global eval (kl_sparsity40_s42, global_topk, **实际 sparsity=50%**)

| Metric | Value |
|--------|-------|
| wikitext2_ppl | **12.8894** |
| arc_challenge_acc_norm | **0.3549** |
| winogrande_acc | **0.6227** |
| mmlu_acc | **0.3139** |
| gsm8k_exact_match | **0.0182** |
| hellaswag_acc_norm | **0.5885** |
| piqa_acc_norm | **0.6855** |

## Uniform eval (kl_sparsity40_s42, uniform, sparsity=40%)

| Metric | Value |
|--------|-------|
| wikitext2_ppl | **10.7605** |
| arc_challenge_acc_norm | **0.3959** |
| winogrande_acc | **0.6306** |
| mmlu_acc | **0.3550** |
| gsm8k_exact_match | **0.0356** |
| hellaswag_acc_norm | **缺失**（未跑） |
| piqa_acc_norm | **缺失**（未跑） |

---

**关键问题**：Global eval 的 `sparsity_target` 配置为 0.5 而非 0.4，这意味着这次 global eval 用的是 50% sparsity 而非 40%。所有指标明显低于 uniform 40% 的结果，与此一致。如果需要真正的 40% global eval，需要用 `--sparsity_target 0.4` 重跑。

---
