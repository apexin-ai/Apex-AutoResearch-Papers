# analysis mmlu subject scatter

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmlu_subject_scatter_20260522T135350_result.json`
- **Structured JSON:** [`757b0e4953a85cc7cb4a.json`](../../sessions/75/757b0e4953a85cc7cb4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**数据**: 200 MMLU items 覆盖 10 个 subjects（每个 20 items），8 models × 2 temperatures × 6 prompts × 6 seeds × 4 orderings。

**核心发现**: Difficulty dispersion (SD of item accuracy) 与 item_id variance share 之间有强正相关：
- **Spearman ρ = 0.81, p = 0.005**
- 线性回归 R² = 0.67, slope = 183.7

**极端值**:
- high_school_mathematics: 最低 SD(p_i) = 0.20, 最低 item_id% = 10.4%
- clinical_knowledge: 最高 SD(p_i) = 0.36, 最高 item_id% = 47.5%

**输出文件**:
- JSON: `artifacts/exp004/data/mmlu_subject_level_analysis.json`
- PDF/PNG: `artifacts/figures/mmlu_subject_scatter.pdf/.png`
- 服务器脚本: `/root/nlp_variance_gtheory/scripts/mmlu_subject_scatter.py`

---
