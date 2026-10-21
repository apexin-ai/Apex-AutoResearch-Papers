# analyze qwen14b kl30 s42 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen14b_kl30_s42_eval_20260517T185314_result.json`
- **Structured JSON:** [`9b6933f006d062084b49.json`](../../sessions/9b/9b6933f006d062084b49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 文件包含完整结果。评测已正常完成（EXIT_CODE=0），总耗时约 4 小时。

## qwen14b_kl30_s42 评测结果（30% KL sparsity, seed 42）

| Task | Metric | 值 | stderr | 样本数 |
|------|--------|------|--------|--------|
| **wikitext2** | perplexity | **7.6232** | — | — |
| **arc_challenge** | acc_norm | **0.5717** | ±0.0145 | 1172 |
| **arc_challenge** | acc | 0.5469 | ±0.0145 | 1172 |
| **winogrande** | acc | **0.7206** | ±0.0126 | 1267 |
| **mmlu** | acc (5-shot) | **0.6372** | ±0.0039 | 14042 |
| **gsm8k** | exact_match (flexible) | **0.4882** | ±0.0138 | 1319 |
| **gsm8k** | exact_match (strict) | 0.4837 | ±0.0138 | 1319 |

配置确认：`teal_global` mode, `global_topk` allocation, sparsity_target=0.3, bottleneck_size=128, seq_len=2048。结果 JSON 已保存至 `/root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_s42/results.json`。无异常。

---
