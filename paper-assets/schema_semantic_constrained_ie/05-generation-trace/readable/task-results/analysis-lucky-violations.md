# analysis lucky violations

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lucky-violations_20260522T141205_result.json`
- **Structured JSON:** [`4b7cd97b7c7a820ccc54.json`](../../sessions/4b/4b7cd97b7c7a820ccc54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**Lucky violations 统计：**

| Config | TP | Lucky DR | % of TP | Recall drop |
|--------|---:|--------:|--------:|:------------|
| SciERC Qwen LoRA | 461 | 4 | 0.87% | 0.41pp |
| SciERC Llama LoRA | 467 | 5 | 1.07% | 0.51pp |
| DocRED Qwen LoRA | 5746 | 1 | 0.02% | 0.01pp |
| DocRED Llama LoRA | 6226 | 1 | 0.02% | 0.01pp |

**核心发现：**
- Lucky violations 占 TP 比例极低（最多 1.07%），recall 损失可忽略（≤0.51pp）
- 与之对比，constraints 移除的绝大多数 violated triples 是 FP（如 DocRED Qwen 移除 164 个违规预测，仅 1 个是正确的）
- 案例分析：SciERC 上主要是 Metric 类实体被误用于 Hyponym-of 关系；DocRED 上是 entity type 标注的边界模糊（MISC vs ORG）

LaTeX appendix 已写入 `artifacts/_project/paper/appendix_downstream_analysis.tex`，包含表格、统计分析和定性讨论。

---
