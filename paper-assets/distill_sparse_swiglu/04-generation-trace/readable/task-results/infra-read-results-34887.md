# infra read results 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_read_results_34887_20260518T005138_result.json`
- **Structured JSON:** [`28c076cf3f1115e2491c.json`](../../sessions/28/28c076cf3f1115e2491c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

共找到 20 个 `results*.json` 文件（最近 25 小时内修改）。以下是完整汇总：

---

### 文件列表与核心指标

| # | 文件路径 | 模型 | 模式 | Sparsity | Alloc | WikiText2 PPL | ARC-C acc | WinoGrande | MMLU | GSM8K EM |
|---|---------|------|------|----------|-------|--------------|-----------|------------|------|----------|
| 1 | `checkpoints/kl_mag_reg_a001/results.json` | — | — | 48.4% | — | 11.82 | — | — | — | — |
| 2 | `results/benchmark/mistral_dense_ppl/` | Mistral-7B | dense | — | — | **5.5238** | — | — | — | — |
| 3 | `results/benchmark/mistral_kl30_pertoken/` | Mistral-7B | per_token (KL) | 30% | uniform | 6.048 | — | — | — | — |
| 4 | `results/benchmark/mistral_kl30_teal_global/` | Mistral-7B | teal_global (KL) | 30% | uniform | 6.7733 | — | — | — | — |
| 5 | `results/benchmark/mistral_teal30_baseline/` | Mistral-7B | teal_vanilla | 30% | uniform | 8.3807 | — | — | — | — |
| 6 | `results/benchmark/mistral_kl50_pertoken/` | Mistral-7B | per_token (KL) | 50% | uniform | 7.2931 | — | — | — | — |
| 7 | `results/benchmark/mistral_kl50_teal_global/` | Mistral-7B | teal_global (KL) | 50% | uniform | 8.6489 | — | — | — | — |
| 8 | `results/benchmark/mistral_teal50_baseline/` | Mistral-7B | teal_vanilla | 50% | uniform | 18.3061 | — | — | — | — |
| 9 | `results/benchmark/mistral_kl70_pertoken/` | Mistral-7B | per_token (KL) | 70% | uniform | 9.1086 | — | — | — | — |
| 10 | `results/benchmark/mistral_kl70_teal_global/` | Mistral-7B | teal_global (KL) | 70% | uniform | 13.3254 | — | — | — | — |
| 11 | `results/benchmark/mistral_teal70_baseline/` | Mistral-7B | teal_vanilla | 70% | uniform | 61.716 | — | — | — | — |
| 12 | `results/benchmark/kl70_teal_global_llama/` | LLaMA-3.1-8B | teal_global (KL) | 70% | uniform | 18.5432 | 0.2125 | — | 0.267 | — |
| 13 | `results/benchmark/teal_vanilla70_llama/` | LLaMA-3.1-8B | teal_vanilla | 70% | uniform | 125.4204 | 0.1928 | — | 0.2615 | — |
| 14 | `results/benchmark/reverse_kl_50pct_s42_eval/` | LLaMA-3.1-8B | teal_global (rev KL) | 50% | global_topk | 12.7969 | — | — | — | — |
| 15 | `results/benchmark/jsd_50pct_s42_eval/` | LLaMA-3.1-8B | teal_global (JSD) | 50% | global_topk | 12.5428 | — | — | — | — |
| 16 | `results/benchmark/db256_pertoken_wikitext2/` | LLaMA-3.1-8B | per_token (KL, d_b=256) | 50% | global_topk | 8.5862 | — | — | — | — |
| 17 | `results/benchmark/kl_50pct_s123_global/` | LLaMA-3.1-8B | teal_global (KL, s123) | 50% | global_topk | 11.745 | 0.329 | 0.6125 | 0.2752 | 0.0281 |
| 18 | `results/benchmark/kl_30pct_s123/` | LLaMA-3.1-8B | teal_global (KL, s123) | 30% | global_topk | 8.9748 | 0.4181 | 0.693 | 0.3807 | 0.0758 |
| 19 | `results/benchmark/kl30_s123_uniform/` | LLaMA-3.1-8B | teal_global (KL, s123) | 30% | uniform | 8.8308 | 0.4096 | 0.6938 | 0.3944 | 0.0751 |
| 20 | `results/benchmark/kl50_s456_global/` | LLaMA-3.1-8B | teal_global (KL, s456) | 50% | global_topk | 11.8057 | 0.3276 | 0.6488 | 0.2794 | 0.0212 |

---
