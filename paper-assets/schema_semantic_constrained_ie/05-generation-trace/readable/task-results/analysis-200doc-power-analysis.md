# analysis 200doc power analysis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_200doc-power-analysis_20260522T071008_result.json`
- **Structured JSON:** [`f8bbe5d106825b6f878d.json`](../../sessions/f8/f8bbe5d106825b6f878d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 核心数据

**ZS 70B（998-doc）**：DR 15.0% → 0.0%，Cohen's h = 0.80（large），n=200 power = **100%**

**FT 8B LoRA（998-doc，代理 70B LoRA）**：DR 0.50% → 0.21%，n=200 bootstrap：
- R-F1 margin of error: **±3.3 points**
- DR% margin of error: **±0.45pp**
- **94.9%** 的 200-doc 子样本正确识别 DR 下降方向

### 论文文字（可直接插入 Appendix）

> To verify that the 200-document subset provides sufficient statistical power, we conducted a bootstrap analysis using the full 998-document 8B LoRA results as a reference population. Resampling 200 documents 5,000 times yields a relation F1 margin of error of ±3.3 points (95% CI) and a DR violation rate margin of error of ±0.45 percentage points—precise enough to support our conclusions. For zero-shot models, where DR violations are prevalent (15.0% unconstrained), a 200-document subset achieves 100% power to detect the constrained decoding effect (Cohen's h = 0.80); for fine-tuned models, where violations are already rare (<0.5%), 94.9% of 200-document subsamples correctly identify the direction of DR reduction, and the primary effect is established on the full 998-document evaluation.

完整分析已保存到 `artifacts/power_analysis_200doc_dr.md`。

---
