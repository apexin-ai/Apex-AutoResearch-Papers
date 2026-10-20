# extract 70b docred zs violations

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_70b_docred_zs_violations_20260522T041607_result.json`
- **Structured JSON:** [`dd44620775d15306d7e6.json`](../../sessions/dd/dd44620775d15306d7e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整汇报。

---

## 70B DocRED ZS Metrics — r16_70b_docred_zs_s1

### 完成状态
- 998/998 samples 全部完成（S1 和 unconstrained 均为 998 行）
- Registry conclusion 已从 `failed` → `success` 修正

### Unconstrained vs S1 对比

| Metric | Unconstrained | S1 (constrained) | Delta |
|--------|:---:|:---:|:---:|
| **E-F1** | 0.6907 | **0.6911** | +0.0004 |
| E-Precision | 0.7504 | 0.7504 | 0 |
| E-Recall | 0.6399 | 0.6405 | +0.0006 |
| **R-F1** | 0.0 | 0.0 | — |
| **ET% (entity type)** | 0.02% (3) | **0.00% (0)** | -0.02% |
| **RV% (relation vocab)** | 100% | 100% | — |
| **DR% (domain/range)** | 0.0% | 0.0% | — |
| **CF% (cross-field)** | 0.04% (6) | 0.04% (6) | 0 |
| JSON parse rate | 100% | 99.9% (1 failure) | -0.1% |
| Total entities | 16617 | 16599 | -18 |
| Total triples | 13396 | 13239 | -157 |

### 关键发现

1. **S1 约束对 entity type 有效**: unconstrained 有 3 个 ETH 类型的 entity type violation（如 "Japanese"→ETH），S1 减到 0

2. **E-F1 几乎不变**: 0.6907 → 0.6911，constraint 不损害 entity 质量

3. **S1 轻微减少了 triple 数量**: 13396 → 13239（-1.2%），说明约束过滤掉了少量不合规三元组

### ⚠️ 严重问题：Schema 错配

**violation checker 使用了 SciERC schema 来评估 DocRED 数据**（日志明确显示 `=== Violation Report (SciERC) ===`）。后果：

- **R-F1 = 0.0 不可信**：所有关系被标记为 "unknown relation type" 是因为 DocRED 的关系名（如 "location", "part of", "country of origin"）不在 SciERC 的 relation vocabulary 中
- **RV = 100% 不可信**：同上
- **DR = 0.0% 可能偏低**：domain/range 规则也来自 SciERC schema
- **E-F1 大致可信**：因为 DocRED 和 SciERC 的 entity types 有较大重叠

**需要用 DocRED schema 重新跑 violation checker 才能获得真实的 R-F1、RV%、DR% 指标。**

---
