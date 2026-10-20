# analysis scierc llama dr detail

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc-llama-dr-detail_20260520T091552_result.json`
- **Structured JSON:** [`e8c13c20eb89c961ab46.json`](../../sessions/e8/e8c13c20eb89c961ab46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收齐。

---

## 分析结果

### DR violation 数量
**1 / 1081** predicted triples (0.09%)

### 唯一的 violation 详情

| 字段 | 值 |
|------|-----|
| doc_id | `NIPS_2001_11_abs_sent4` |
| head | "CID/DRAM analog array prototype" |
| head_type | **OtherScientificTerm** |
| relation | **Evaluate-for** |
| tail | "approach" |
| tail_type | **Generic** |
| 违反原因 | `(OtherScientificTerm, Generic)` 不在 Evaluate-for 的 valid_pairs 中 |

### Evaluate-for 的合法 pairs（23 个）
Evaluate-for 的 valid_pairs 包含 `(OtherScientificTerm, Method)` 和 `(Generic, OtherScientificTerm)` 等 23 种组合，但**确实不包含 `(OtherScientificTerm, Generic)`**。

### 这是 constraint 未覆盖的边缘情况吗？

**是。** 训练集中 Evaluate-for 共 313 例，从未出现 `(OtherScientificTerm, Generic)` 这个 pair（分布中没有该键）。所以 schema 约束从训练数据统计得来，合理地不包含此 pair。模型在 constrained decoding 下仍输出了它，说明这 1 个 triple 是约束漏网的极罕见边缘情况。

### Paper claim 影响

DR=0.09% (1/1081) 对 paper claim 影响极小：
- 如果 paper 写的是 "DR≈0%" 或 "near-zero DR"——**不需要修改**，0.09% 可以 round 到 ≈0%
- 如果 paper 写的是 "DR=0%"（精确零）——需要改为 "0.09%" 或 "1 violation out of 1081 triples"
- 建议在表格中如实报告 0.09%，脚注说明这 1 个 violation 的来源是 `(OtherScientificTerm, Generic)` 在 Evaluate-for 中未被训练集覆盖

---
