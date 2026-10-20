# analysis scierc violation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc_violation_20260513T191114_result.json`
- **Structured JSON:** [`a619a24b6305c922fcd0.json`](../../sessions/a6/a619a24b6305c922fcd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SciERC 全量 Violation Analysis 结果

### 1. 总体统计

| 指标 | 值 |
|------|-----|
| 样本数 | 551 |
| 提取三元组数 | 1,724 |
| 提取实体数 | 2,474 |
| JSON 解析失败 | 0 (0.0%) |
| Fuzzy matches | 0 |

### 2. 四类 Violation 计数与率

| Violation 类型 | 计数 | 分母 | Rate |
|---------------|------|------|------|
| Entity type violations | 10 / 2,474 | entities | **0.40%** |
| Relation vocabulary violations | 24 / 1,724 | triples | **1.39%** |
| Domain/range violations | 265 / 1,724 | triples | **15.37%** |
| Cross-field consistency violations | 2 | entities | **0.08%** |

**总违规三元组**: 301, 总违规率: 7.17%

### 3. Go/No-Go Metric

**domain_range_violation_rate = 0.1537 (15.4%)**

这是 OntoCoDec 核心目标指标——每 6.5 个三元组就有 1 个违反 domain/range 约束，说明 unconstrained LLM 在 schema 一致性上存在显著问题，constrained decoding 有明确改进空间。

### 4. Per-Relation Type Breakdown

| Relation | Total | D/R Violations | Rate |
|----------|-------|----------------|------|
| **Used-for** | 787 | 6 | **0.76%** ✅ |
| **Conjunction** | 32 | 0 | **0.00%** ✅ |
| **Hyponym-of** | 124 | 18 | **14.52%** |
| **Evaluate-for** | 133 | 32 | **24.06%** ⚠️ |
| **Part-of** | 72 | 18 | **25.00%** ⚠️ |
| **Feature-of** | 486 | 163 | **33.54%** 🔴 |
| **Compare** | 66 | 28 | **42.42%** 🔴 |

**Feature-of** 和 **Compare** 是重灾区，合计贡献 191/265 = 72% 的 domain/range violations。Used-for 约束最宽松，违规率极低。

### 5. 典型违规示例

**Entity type violations** — 模型将 relation type 误填为 entity type：
- `"high-density"` → type `"Feature-of"` (应为 Material/OtherScientificTerm 等)
- `"low-power"` → type `"Feature-of"`

**Relation vocabulary violations** — 模型幻觉出 ontology 外的关系：
- `Outperforms` (method outperforms method)
- `Consistent-with`, `Smaller-than`

**Domain/range violations** — 关系名合法但 head/tail type 组合不合法：
- `Hyponym-of(Task, OtherScientificTerm)` — 不在合法 type pair 中
- `Feature-of(Task, Material)` — Feature-of 大量出现 (Task, Material) 违规组合

**Cross-field consistency violations** — 同一 mention 被标注为不同 type：
- `"eigenvectors"` → Material vs OtherScientificTerm
- `"nlp"` → Generic vs OtherScientificTerm

### 6. 附加质量指标 (Entity/Relation F1)

| | Precision | Recall | F1 | TP | Gold | Pred |
|--|-----------|--------|-----|-----|------|------|
| Entity | 0.2605 | 0.3831 | 0.3101 | 641 | 1,673 | 2,461 |
| Relation | 0.0644 | 0.1140 | 0.0823 | 111 | 974 | 1,724 |

Relation F1 仅 8.2%，说明 unconstrained baseline 在 SciERC 上的精确匹配性能较弱，进一步验证了 constrained decoding 方向的必要性。

---
