# infra read results 41718

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_read_results_41718_20260518T005145_result.json`
- **Structured JSON:** [`0661f9ae885b36e77b41.json`](../../sessions/06/0661f9ae885b36e77b41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 28 个 results.json 已读取完毕。汇总如下：

---

## GPU 状态 (westd-41718)

| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Black | 67569/97887 MiB | 100% | 74°C |
| 1 | RTX PRO 6000 Black | 67569/97887 MiB | 100% | 72°C |

**活跃训练任务：**
- **cuda:0** — `kl30_8b_s123` train.py (step ~640/1000), 之后自动 eval
- **cuda:1** — `kl30_8b_s456` train.py (step ~630/1000), 之后自动 eval

---

## 全部 results.json 文件 (28个)

### LLaMA-3.1-8B 实验

| exp_id | mode | sparsity | alloc | wikitext2 PPL | ARC | WinoGr | MMLU | GSM8K | timestamp |
|--------|------|----------|-------|--------------|-----|--------|------|-------|-----------|
| kl_30pct_s123 | teal_global | 30% | global_topk | 8.9748 | 41.8 | 69.3 | 38.1 | 7.6 | 05-17 19:11 |
| kl30_s123_uniform | teal_global | 30% | uniform | 8.8308 | 41.0 | 69.4 | 39.4 | 7.5 | 05-17 20:53 |
| kl30_s456_global | teal_global | 30% | global_topk | 8.9332 | 43.7 | 71.1 | 43.8 | 7.6 | 05-17 21:33 |
| kl30_s456_uniform | teal_global | 30% | uniform | 8.7947 | 40.7 | 68.8 | 42.0 | 7.6 | 05-17 22:24 |
| kl_50pct_s123_global | teal_global | 50% | global_topk | 11.745 | 32.9 | 61.3 | 27.5 | 2.8 | 05-17 19:02 |
| kl50_s456_global | teal_global | 50% | global_topk | 11.8057 | 32.8 | 64.9 | 27.9 | 2.1 | 05-17 21:33 |
| kl50_global_s123_reeval | teal_global | 50% | global_topk | 11.7184 | 32.9 | 61.1 | 28.3 | 2.6 | 05-18 01:51 |
| kl70_teal_global_llama | teal_global | 70% | uniform | 18.5432 | 21.3 | — | 26.7 | — | 05-17 09:21 |
| db256_pertoken_wikitext2 | per_token | 50% | global_topk | 8.5862 | — | — | — | — | 05-17 16:40 |
| jsd_50pct_s42_eval | teal_global | 50% | global_topk | 12.5428 | — | — | — | — | 05-17 15:00 |
| reverse_kl_50pct_s42_eval | teal_global | 50% | global_topk | 12.7969 | — | — | — | — | 05-17 14:59 |
| teal_vanilla70_llama | baseline_teal_vanilla | 70% | uniform | 125.4204 | 19.3 | — | 26.2 | — | 05-17 09:21 |

**扩展下游任务 (LLaMA 8B):**

| exp_id | mode | sparsity | HellaSwag | PIQA | BoolQ | timestamp |
|--------|------|----------|-----------|------|-------|-----------|
| downstream_dense_baseline | dense | — | 82.3 (norm) | 80.7 (norm) | 82.9 | 05-18 00:32 |
| downstream_teal30_baseline | baseline_teal_vanilla | 30% | 66.7 (norm) | 73.6 (norm) | 68.5 | 05-18 01:09 |
| downstream_ext_kl30_s42 | teal_global (KL) | 30% | 72.7 (norm) | 75.9 (norm) | 76.9 | 05-17 23:35 |

**OOD:**

| exp_id | mode | sparsity | metrics | timestamp |
|--------|------|----------|---------|-----------|
| c4_ood_kl30_s42 | teal_global | 30% | **空 (无结果)** | 05-18 02:35 |

### Mistral-7B 实验

| exp_id | mode | sparsity | wikitext2 PPL | timestamp |
|--------|------|----------|--------------|-----------|
| mistral_dense_ppl | dense | — | 5.5238 | 05-17 09:06 |
| mistral_teal30_baseline | baseline_teal_vanilla | 30% | 8.3807 | 05-17 08:59 |
| mistral_kl30_pertoken | per_token (KL) | 30% | 6.0480 | 05-17 08:58 |
| mistral_kl30_teal_global | teal_global (KL) | 30% | 6.7733 | 05-17 09:00 |
| mistral_teal50_baseline | baseline_teal_vanilla | 50% | 18.3061 | 05-17 09:03 |
| mistral_kl50_pertoken | per_token (KL) | 50% | 7.2931 | 05-17 09:03 |
| mistral_kl50_teal_global | teal_global (KL) | 50% | 8.6489 | 05-17 09:04 |
| mistral_teal70_baseline | baseline_teal_vanilla | 70% | 61.716 | 05-17 09:15 |
| mistral_kl70_pertoken | per_token (KL) | 70% | 9.1086 | 05-17 09:13 |
| mistral_kl70_teal_global | teal_global (KL) | 70% | 13.3254 | 05-17 09:14 |

### Qwen2.5-14B 实验

| exp_id | mode | sparsity | wikitext2 PPL | ARC | WinoGr | MMLU | GSM8K | timestamp |
|--------|------|----------|--------------|-----|--------|------|-------|-----------|
| qwen14b_dense_baseline | dense | — | 5.1854 | 64.9 | 81.1 | 79.8 | 87.6 | 05-18 02:47 |
| qwen14b_teal30 | baseline_teal_vanilla | 30% | 8.7332 | 53.9 | 72.7 | 71.8 | 49.5 | 05-17 23:49 |

**注意:** `c4_ood_kl30_s42` 的 metrics 为空（可能评估失败或未完成）。

---
