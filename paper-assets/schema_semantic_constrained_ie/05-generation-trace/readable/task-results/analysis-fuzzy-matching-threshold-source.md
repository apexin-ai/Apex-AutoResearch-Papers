# analysis fuzzy matching threshold source

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fuzzy_matching_threshold_source_20260516T181829_result.json`
- **Structured JSON:** [`7196ecd9e9b773e856f2.json`](../../sessions/71/7196ecd9e9b773e856f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成，核心结论：

**阈值来源：(a) 先验选择。** Token Jaccard >0.8 和 Levenshtein ≤2 是硬编码在 6+ 个文件中的相同常量，无参数化接口，无 tuning 痕迹。

关键发现：
- Fuzzy matching 用于**关系类型名称归一化**（不是实体名称匹配）
- SciERC 全部实验 fuzzy match count = 0（零影响）
- DocRED 仅 ZS unconstrained/semantic_only 触发，影响 <1% triples（129/17,497）
- 所有 constrained 模式和 FT 模型中 fuzzy match = 0
- Strict 和 Fuzzy R_F1 差异可忽略（<0.1pp）

报告含完整的代码位置表、所有实验 R_F1 汇总、审稿人回复建议，保存在 `artifacts/fuzzy_matching_threshold_analysis.md`。

---
