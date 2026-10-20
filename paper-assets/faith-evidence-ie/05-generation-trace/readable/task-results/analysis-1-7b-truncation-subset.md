# analysis 1 7b truncation subset

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_1_7b_truncation_subset_20260516T142416_result.json`
- **Structured JSON:** [`f97456af80c8b7b4e9a3.json`](../../sessions/f9/f97456af80c8b7b4e9a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结论

**公平子集（442篇，两边均未截断）上的真实 evidence tax = +0.0616**，with-evidence 模型仍显著优于 no-evidence。

核心数据：

| | Ign-F1 | Ign-P | Ign-R |
|--|--------|-------|-------|
| no-evidence | 0.5704 | 0.5140 | 0.6406 |
| with-evidence | **0.6319** | **0.6079** | **0.6579** |

关键发现：

1. **截断确实是偏差来源**——全量 tax +0.0804 中约 0.02 来自截断混淆（no-evi 截断率 50.9% vs with-evi 31.9%），但排除后 gap 仍有 +0.0616
2. **evidence generation 起正则化作用**——with-evi Precision 比 no-evi 高 9.4pp（0.608 vs 0.514），no-evi 过度预测（4513 vs 3991 triples），evidence 约束减少了幻觉
3. **不存在"小模型 evidence 负担"**——即使在公平条件下，with-evidence 在 P 和 R 上都更优，per-doc 胜负比 218:125

Director 假设"截断混淆结果"成立，但方向判断需修正：真实 tax 仍为正，evidence generation 对 1.7B 模型是净正向的。

---
