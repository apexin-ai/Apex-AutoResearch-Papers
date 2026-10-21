# analysis llama docred full s1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_docred_full_s1_20260514T202452_result.json`
- **Structured JSON:** [`19778923c65ba1df4349.json`](../../sessions/19/19778923c65ba1df4349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

## 结果摘要

| Metric | Llama uncon | Llama full_s1 | Delta | Qwen full_s1 |
|--------|------------|--------------|-------|-------------|
| **ET** | 0.13% | **0.00%** | -0.13pp | 0.00% |
| **RV** | 16.03% | **0.00%** | -16.03pp | 0.03% |
| **DR** | 26.07% | **2.55%** | -23.52pp | 10.19% |
| **CF** | 0.17% | **12.02%** | +11.85pp | 2.57% |
| **E-F1** | 55.65% | 55.01% | -0.64pp | 59.37% |
| **R-F1** | 5.98% | 6.27% | +0.29pp | 8.23% |
| Parse fail | 68 | 91 | +23 | — |

**核心发现**：
- 约束解码在 Llama 上有效消除了 ET/RV 违规，DR 降幅（-23.52pp）甚至优于 Qwen
- **CF 暴涨至 12.02%** 是主要问题——约束迫使同一实体在不同关系中获得不一致类型，Llama 比 Qwen（2.57%）严重得多
- F1 基本持平，未见显著损害或提升

---
