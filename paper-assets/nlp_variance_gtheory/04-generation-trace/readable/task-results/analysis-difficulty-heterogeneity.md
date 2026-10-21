# analysis difficulty heterogeneity

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_difficulty_heterogeneity_20260522T104048_result.json`
- **Structured JSON:** [`aaad79a6e5b5222b886d.json`](../../sessions/aa/aaad79a6e5b5222b886d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## Item Difficulty Heterogeneity 结果

| Benchmark | n_models | std(p_i) | item_id% |
|-----------|----------|----------|----------|
| MMLU | 8 | **0.3112** | 37.88% |
| ARC | 8 | 0.2737 | 37.88% |
| HellaSwag | 6 | 0.2822 | 34.27% |
| GSM8K | 8 | 0.2203 | 16.86% |
| MATH | 7 | 0.2283 | 24.03% |

**Spearman ρ = 0.82, p = 0.089** — 强正相关，item difficulty heterogeneity 越大，item_id 方差成分越大。5 个点接近但未达显著性。

## Within-format 梯度分析

**MC benchmarks (MMLU/ARC/HellaSwag):**
- std(p_i) 排序：MMLU (0.31) > HellaSwag (0.28) > ARC (0.27)
- item_id% 排序：MMLU (37.88) = ARC (37.88) > HellaSwag (34.27)
- **部分一致**：MMLU 一致排首位；HellaSwag 和 ARC 在两个指标上互换位置，但差异很小（0.2822 vs 0.2737，仅差 0.008）。MMLU 和 ARC 的 item_id% 完全相同（37.88%），但 MMLU 的 difficulty heterogeneity 更大——可能因为 MMLU 涵盖 57 个学科，天然 item difficulty 范围更广。

**FF benchmarks (GSM8K/MATH):**
- std(p_i) 排序：MATH > GSM8K
- item_id% 排序：MATH > GSM8K
- **完全一致** (Spearman ρ = 1.0)

## 关键结论

format-conditional variance structure 不是 trivial artifact。即使在同一 format 内，difficulty heterogeneity 也能部分解释 item variance component 的差异。MC benchmarks 整体 std(p_i) 更高、item_id% 也更高；FF benchmarks 较低。这支持 difficulty heterogeneity 是 item variance 的驱动因素。

**产出路径：**
- 脚本：服务器 `/root/nlp_variance_gtheory/scripts/difficulty_heterogeneity.py`
- JSON：本地 `artifacts/exp004/data/cross_benchmark_difficulty_heterogeneity.json`
- PDF/PNG：本地 `artifacts/exp004/figures/difficulty_vs_item_variance.pdf`
- HellaSwag 使用 6 models（无 OLMo/Yi 数据），MATH 使用 7 models（无 gemma）

---
