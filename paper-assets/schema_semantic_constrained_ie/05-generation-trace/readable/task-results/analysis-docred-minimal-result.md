# analysis docred minimal result

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_minimal_result_20260513T214033_result.json`
- **Structured JSON:** [`f7d16c13975eb7794a6e.json`](../../sessions/f7/f7d16c13975eb7794a6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

DocRED minimal 提取和 violation analysis 完成。

### 结果汇总

| 指标 | 值 |
|------|-----|
| 文档总数 | 998 |
| 成功解析 | 962 (96.4%) |
| 解析失败 | 36 |
| 提取实体数 | 19,099 |
| 提取三元组数 | 16,540 |
| **Entity type violation rate** | **7.5%** (1,437) |
| **Relation vocab violation rate** | **28.9%** (4,775/16,540) |
| **Domain/range violation rate (go/no-go)** | **18.7%** (3,093/16,540) |
| Cross-field consistency violations | 0.08% (15) |
| Fuzzy relation matches | 126 |

### Top-5 D/R Violation（按违规率，≥5 triples）

| 关系 | 违规率 | 违规数/总数 |
|------|--------|-------------|
| P35 (head of state) | 100% | 10/10 |
| P710 (participant) | 91.9% | 34/37 |
| P172 (ethnic group) | 87.5% | 21/24 |
| P488 (chairperson) | 83.3% | 5/6 |
| P6 (head of government) | 77.8% | 7/9 |

### Top-5 D/R Violation（按绝对数量）

| 关系 | 违规数/总数 | 违规率 |
|------|-------------|--------|
| P31 (instance of) | 322/533 | 60.4% |
| P1001 (applies to jurisdiction) | 264/594 | 44.4% |
| P1344 (participant in) | 194/312 | 62.2% |
| P276 (location) | 147/273 | 53.8% |
| P206 (located next to water) | 139/427 | 32.6% |

D/R violation rate = 18.7%，模型在 DocRED schema 约束下有显著的 domain/range 违规，尤其是 P31（instance of）贡献最大量违规。Relation vocab 违规率 28.9% 也偏高，说明模型频繁生成 schema 外的关系类型。

---
