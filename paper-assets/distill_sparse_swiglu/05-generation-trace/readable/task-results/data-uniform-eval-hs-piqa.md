# data uniform eval hs piqa

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_uniform_eval_hs_piqa_20260520T092745_result.json`
- **Structured JSON:** [`b6c8182b1e5499a5dac1.json`](../../sessions/b6/b6c8182b1e5499a5dac1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`kl_sparsity40_s42_retrain_uniform` 的完整指标：

| Task | Metric | Value |
|------|--------|-------|
| wikitext2 | ppl | 10.7605 |
| arc_challenge | acc_norm | 0.3959 |
| winogrande | acc | 0.6306 |
| mmlu | acc | 0.3550 |
| gsm8k | exact_match | 0.0356 |

**HellaSwag 和 PIQA 不存在。** 配置中 tasks 字段为 `wikitext2,arc_challenge,winogrande,mmlu,gsm8k`，未包含 hellaswag 和 piqa。需要补跑才能获取这两个指标。

---
