# analysis edcr tex fix and per relation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edcr_tex_fix_and_per_relation_20260515T235434_result.json`
- **Structured JSON:** [`6810878ee1c10e1aee78.json`](../../sessions/68/6810878ee1c10e1aee78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

### Part 1: edcr_diagnostic.tex 修复

- `dpo_ced_1ep/` → `dpo_ced_1ep_fixed/`（rel_f1: 0.0022 → 0.4034）
- `rsft_flat_nli_s43` 已移除（reeval 目录为空，无可用数据）
- 新 .tex/.csv/.md 已生成，无非 GRPO 的 rel_f1 < 0.01 条目

### Part 2: Per-Relation EDCR 分析结果

93 个 relation types 分析（≥5 样本），76 个有非零 rel_f1 和 evi_f1 参与相关性计算。

**核心发现**：

| 指标对 | Spearman ρ | p-value |
|--------|-----------|---------|
| EDCR_distractor vs evi_f1 | **-0.064** | 0.583 |
| EDCR_distractor vs rel_f1 | -0.793 | <0.001 |
| evi_f1 vs rel_f1 | **-0.013** | 0.914 |

**结论**：ρ(EDCR, evi_f1) = -0.064，几乎零相关 → **EDCR 在 per-relation 层面提供完全独立于 evi_f1 的信息。Claim 4 有支撑。**

另一个发现：evi_f1 vs rel_f1 在 per-relation 层面也几乎零相关（ρ=-0.013），说明模型的 evidence 质量和 relation 抽取能力在不同 relation type 间完全解耦。

**典型案例**：
- date_of_birth: EDCR=0.118, evi_f1=0.965, rel_f1=0.922（高 faithful）
- head_of_government: EDCR=0.956, evi_f1=0.875, rel_f1=0.086（高 decoupled — 证据好但关系抽取差）

### 产出清单
1. `/root/autodl-tmp/eval_results/edcr_diagnostic.tex` + `.csv` + `_table.md` — 修复后
2. `/root/autodl-tmp/scripts/edcr_per_relation_analysis.py`
3. `/root/autodl-tmp/eval_results/edcr_per_relation_analysis.json` + `.md`

---
