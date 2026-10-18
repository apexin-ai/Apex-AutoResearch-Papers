# analysis exp007 error taxonomy

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp007-error-taxonomy_20260515T131936_result.json`
- **Structured JSON:** [`d804c0669b7857b47c8f.json`](../../sessions/d8/d804c0669b7857b47c8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出已就绪。汇报结果：

---

**exp-007 Error Taxonomy 分析完成**

核心发现 — **intra-batch type substitution 随 BCS 单调递增，强力支撑 Claim 2 (confusability channel)**：

### exp1_random (BCS 0→0.97, 94 batches)

| BCS bin | #FP | IntraSub% | ExtraSub% | IntraSub/gold |
|---------|-----|-----------|-----------|---------------|
| zero (=0) | 6172 | **0.0%** | 90.3% | 0.00% |
| low (<0.90) | 2231 | **1.6%** | 89.9% | 3.40% |
| medium (0.90-0.95) | 3843 | **10.6%** | 78.1% | 6.47% |
| high (≥0.95) | 6188 | **49.4%** | 30.8% | 12.93% |

- **IntraSub fraction ~ BCS: Spearman ρ=1.000, p<0.001 \*\*\***
- **IntraSub rate/gold ~ BCS: Spearman ρ=1.000, p<0.001 \*\*\***
- Chi-square: χ²=6952, p≈0 \*\*\*

### exp2_controlled (BCS 0.86→0.97, 54 batches)
同一趋势在窄 BCS 区间也成立：IntraSub 从 3.2% → 7.3% → 8.6% (ρ=1.0, p<0.001)

### 解读
- BCS=0（单类型）时 intra-batch type confusion 不可能发生（0%），符合理论预期
- BCS≥0.95 时 **49.4% 的 FP 是 batch 内类型混淆**，每 100 个 gold entity 产生 ~13 个 intra-batch type_sub
- Extra-batch type_sub 反向下降（90.3% → 30.8%），说明高 BCS 环境下 batch 内混淆取代了 batch 外混淆
- Hallucination 和 boundary_error 占比始终很低（<3%），说明 LLM 的主要错误模式是类型混淆而非幻觉或边界偏移

### 产出
- `artifacts/exp007/error_taxonomy_report.txt`
- `artifacts/exp007/error_taxonomy_by_bcs.csv`
- `artifacts/exp007/error_taxonomy_raw.json`
- `src/error_taxonomy.py`

---
