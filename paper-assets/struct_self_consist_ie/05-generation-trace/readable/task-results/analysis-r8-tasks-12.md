# analysis r8 tasks 12

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r8_tasks_12_20260515T223511_result.json`
- **Structured JSON:** [`63fe6c85c2b81b183761.json`](../../sessions/63/63fe6c85c2b81b183761.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。以下是完整表格。

---

## Task 1: SJ Normalizer 对比（SJ_max vs SJ_union）

Gold-empty instances 已过滤。SJ_max = `|∩| / max(|A|,|B|)`，SJ_union = `|∩| / |A∪B|`（标准 Jaccard）。

| Dataset | Model | n | ρ(SJ_max) | ρ(SJ_union) | Δρ | p(SJ_max) | p(SJ_union) |
|---------|-------|---:|----------:|------------:|----:|----------:|------------:|
| CoNLL NER | Qwen3-8B | 2756 | 0.4357 | 0.4376 | −0.0019 | 4.71e-128 | 2.74e-129 |
| CoNLL NER | Qwen3-4B | 2756 | 0.4217 | 0.4212 | +0.0004 | 3.07e-119 | 5.64e-119 |
| CoNLL NER | LLaMA-8B | 2756 | 0.4314 | 0.4318 | −0.0004 | — | — |
| SciERC NER | Qwen3-8B | 529 | 0.3599 | 0.3650 | −0.0051 | 1.28e-17 | 4.11e-18 |
| SciERC NER | Qwen3-4B | 529 | 0.4221 | 0.4234 | −0.0014 | 2.89e-24 | 1.98e-24 |
| SciERC NER | LLaMA-8B | 529 | 0.3630 | 0.3719 | −0.0089 | 6.41e-18 | 8.57e-19 |

**验证**: CoNLL 4B ρ_max = 0.4217 ✓（registry ≈0.42），SciERC 4B ρ_max = 0.4221 ✓（registry ≈0.42）

**结论**: |Δρ| 在所有 6 个组合中都极小（最大 0.0089），normalizer 的选择对 Spearman 相关性几乎没有影响。SJ_union 在 5/6 的配置中 ρ 略高（Δρ 为负表示 union 更好），但差异不具实际意义。

---

## Task 2: Seed 456 LP Range 分析

SciERC NER，Qwen3-8B，N=16 samples/instance。LP range = max(cumulative_logprob) − min(cumulative_logprob) across 16 samples per instance。

### Cumulative LP Range（总 logprob 的 range）

| Seed | Subtask | n_instances | median_LP_range | IQR_low | IQR_high | mean | std |
|------|---------|------------:|----------------:|--------:|---------:|-----:|----:|
| 42 | ner | 551 | 8.195 | 5.764 | 11.281 | 8.912 | 4.581 |
| 123 | ner | 551 | 8.211 | 6.161 | 11.428 | 9.145 | 4.708 |
| 456 | **joint** | 551 | 8.367 | 6.000 | 11.514 | 9.214 | 4.781 |
| 456 | ner | 551 | 8.141 | 5.704 | 11.422 | 8.811 | 4.385 |

### Mean LP Range（per-token logprob 的 range）

| Seed | Subtask | median | IQR_low | IQR_high | mean | std |
|------|---------|-------:|--------:|---------:|-----:|----:|
| 42 | ner | 0.0548 | 0.0368 | 0.0990 | 0.0765 | 0.0627 |
| 123 | ner | 0.0608 | 0.0362 | 0.1038 | 0.0799 | 0.0653 |
| 456 | **joint** | 0.0587 | 0.0359 | 0.1010 | 0.0776 | 0.0590 |
| 456 | ner | 0.0591 | 0.0356 | 0.1046 | 0.0814 | 0.0690 |

### 统计检验

| 比较 | 统计量 | p-value |
|------|--------|--------:|
| seed456_joint vs NER pool (Mann-Whitney) | U = 309052 | p = 0.551 |
| seed456_ner vs NER pool (Mann-Whitney) | U = 296559 | p = 0.441 |
| 3个 NER seeds (Kruskal-Wallis) | H = 1.461 | p = 0.482 |

**相对偏差**: seed456_joint 比 3 个 NER seed 均值高 2.0%，seed456_ner 高 0.75%。

**结论**: Seed 456（使用 `--subtask joint`）的 LP range 与其他 seed **无显著差异**（p=0.55）。三个 NER seed 之间也无显著差异（Kruskal-Wallis p=0.48）。`--subtask joint` 对 LP range 没有异常影响。

---

结果文件：
- `output/review_round8/task1_sj_normalizer_final.json`
- `output/review_round8/task2_lp_range_final.json`

---
