# analysis evidence tax mechanism

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_evidence_tax_mechanism_20260519T104201_result.json`
- **Structured JSON:** [`974862c3b2f57bbfc499.json`](../../sessions/97/974862c3b2f57bbfc499.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

### Evidence Tax 核心发现

**Evidence tax 在不同 scale 上非单调：**

| Scale | With-Ev F1 | No-Ev F1 | Tax | 方向 |
|-------|-----------|----------|-----|------|
| 1.7B  | 0.494     | 0.410    | +8.4pp | with-ev 更好 |
| 4B    | 0.405     | 0.488    | -8.3pp | no-ev 更好 |
| 8B Qwen | 0.526  | 0.528    | -0.2pp | 持平 |
| 8B Llama | 0.551 | 0.562    | -1.1pp | no-ev 略好 |

**机制分析（非简单的 token budget 竞争）：**

1. **Truncation 不是主因**：1.7B no-evidence 反而截断率更高（50.9% vs 31.9%），因为小模型在无 evidence 约束时疯狂生成重复 triple
2. **Evidence 在小模型上是 regularizer**：1.7B no-ev 有 60.5% 重复 triple（15814/26157），with-ev 只有 33.0%。Evidence 字段提供了结构约束，抑制了退化重复生成
3. **Evidence 字符开销 ~20%**：每个 triple 约 102 chars（with-ev）vs 85 chars（no-ev），1.2x 比率
4. **4B 异常可能是训练 artifact**：4B with-ev 的 FP rate 异常高（58.7%），可能是 SFT adapter 质量问题而非纯 evidence 机制
5. **8B+ 上 evidence tax 可忽略**：大模型能处理额外输出复杂度而不降质

**产出文件：**
- 报告：`scripts/analysis/results/evidence_tax_report.txt`
- 图表：`evidence_tax_overview.png`、`output_length_distributions.png`、`precision_recall_fp.png`、`evidence_overhead.png`、`per_doc_f1_diff.png`
- 脚本：`scripts/analysis/evidence_tax_analysis.py`、`scripts/analysis/evidence_tax_plots.py`

---
