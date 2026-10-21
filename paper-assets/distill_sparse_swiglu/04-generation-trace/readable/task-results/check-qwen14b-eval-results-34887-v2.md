# check qwen14b eval results 34887 v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen14b_eval_results_34887_v2_20260522T040255_result.json`
- **Structured JSON:** [`340998b18c4a639f4279.json`](../../sessions/34/340998b18c4a639f4279.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部完成，results.json 均存在且完整。

| 实验 | 模式 | Sparsity | PPL | ARC-C | WinoG | MMLU | GSM8K | HellaS | PIQA | 时间 |
|------|------|----------|-----|-------|-------|------|-------|--------|------|------|
| **qwen14b_teal30_uniform_gsm8k** | TEAL baseline | 30% | — | — | — | — | 52.08 | — | — | 05-20 04:39 |
| **qwen14b_teal275_uniform_eval_v3** | TEAL baseline | 27.5% | 7.709 | 53.07 / 57.00 | 71.67 | 67.38 | 57.09 | — | — | 05-19 22:39 |
| **qwen14b_kl30_s42_eval_uniform_v3** | KL distilled (ours) | 30% | 7.872 | 50.51 / 54.95 | 71.27 | 64.80 | — | 53.52 / 72.68 | 74.32 / 74.76 | 05-19 22:27 |

注意事项：
- 实验 1 只跑了 GSM8K 单任务
- 实验 2 和 3 的 benchmark 集合不同（2 有 GSM8K 无 HellaSwag/PIQA，3 反之），直接对比时需注意 task 覆盖差异
- KL distilled (30%) vs TEAL baseline (27.5%) 在重叠指标上：PPL 略高 (+0.16)，ARC-C 低 2.6pp，WinoG 持平，MMLU 低 2.6pp

---
