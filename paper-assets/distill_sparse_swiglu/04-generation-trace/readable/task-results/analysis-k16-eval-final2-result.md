# analysis k16 eval final2 result

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k16_eval_final2_result_20260523T062940_result.json`
- **Structured JSON:** [`103280e6d9a7193674a3.json`](../../sessions/10/103280e6d9a7193674a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`perlayer_kl_k16_eval_final2` 评估成功完成，registry 已更新为 DONE/success，cron 已清除。

## 完整指标表

| 指标 | 值 |
|------|-----|
| wikitext2_ppl | **8.6737** |
| arc_challenge (acc_norm) | **0.4104** |
| winogrande (acc) | **0.6843** |
| mmlu (acc) | **0.4403** |
| gsm8k (exact_match) | **0.0811** |
| hellaswag (acc_norm) | **0.6963** |
| piqa (acc_norm) | **0.7590** |

配置：LLaMA-3.1-8B, teal_global, 30% sparsity, uniform allocation, K=16 predictor checkpoint。评估耗时约 4177 秒。

---
