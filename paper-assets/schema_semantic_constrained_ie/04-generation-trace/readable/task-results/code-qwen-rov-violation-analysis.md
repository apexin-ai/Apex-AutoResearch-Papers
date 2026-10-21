# code qwen rov violation analysis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_rov_violation_analysis_20260518T025456_result.json`
- **Structured JSON:** [`dd234eb4956cdf9ef07b.json`](../../sessions/dd/dd234eb4956cdf9ef07b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整报告。

---

## 18 个 RoV Violations 完整分析

### 完整列表

| # | doc_id | event_type | violated_role | arg_text |
|---|--------|-----------|---------------|----------|
| 1 | K0C041NHW | ArrestJailDetain.Unspecified | PlaceOfEmployment | juvenile |
| 2 | K0C041NHW | ArrestJailDetain.Unspecified | PlaceOfEmployment | Hurricane Police Department |
| 3 | K0C041NHW | Consume.Unspecified | PlaceOfEmployment | suspect |
| 4 | K0C041NHW | Consume.Unspecified | PlaceOfEmployment | investigators |
| 5 | K0C041NHW | InvestigateCrime.Unspecified | PlaceOfEmployment | ongoing |
| 6 | scenario_en_kairos_47 | ArrestJailDetain.Unspecified | PlaceOfEmployment | An ISIS-inspired Utah teen |
| 7 | scenario_en_kairos_47 | Contact.Unspecified | PlaceOfEmployment | concerned classmates |
| 8 | scenario_en_kairos_47 | ArrestJailDetain.Unspecified | PlaceOfEmployment | the suspect |
| 9 | scenario_en_kairos_47 | InvestigateCrime.Unspecified | PlaceOfEmployment | authorities |
| 10 | scenario_en_kairos_47 | IdentifyCategorize.Unspecified | PlaceOfEmployment | bomb squad members |
| 11 | scenario_en_kairos_47 | Research.Unspecified | PlaceOfEmployment | the male |
| 12 | scenario_en_kairos_47 | DemonstrateWithViolence | PlaceOfEmployment | the teen |
| 13 | scenario_en_kairos_47 | IdentifyCategorize.Unspecified | PlaceOfEmployment | evidence |
| 14 | scenario_en_kairos_47 | SensoryObserve | PlaceOfEmployment | the department |
| 15 | scenario_en_kairos_47 | Correspondence | PlaceOfEmployment | the police department |
| 16 | wiki_ied_bombings_1_news_10 | ManufactureAssemble.Unspecified | ArtifactMoney | a substantial sum of money |
| 17 | wiki_ied_bombings_1_news_10 | ManufactureAssemble.Unspecified | ArtifactMoney | the residual amount |
| 18 | scenario_en_kairos_12 | ManufactureAssemble.Unspecified | ArtifactMoney | two people |

### Pattern

- **15/18** 是 `PlaceOfEmployment`（仅在 `StartPosition`/`EndPosition` 中合法）
- **3/18** 是 `ArtifactMoney`（仅在 `Donation.Unspecified` 中合法）
- 集中在 2-3 篇文档（K0C041NHW, scenario_en_kairos_47, wiki_ied_bombings_1_news_10）

### 根因：Continuation mask 的 safety net bug（代码 bug，非 ontology 缺陷）

Ontology 中存在 3 个 **prefix collision**：
- `Place` → `PlaceOfEmployment`
- `Artifact` → `ArtifactMoney`  
- `Damager` → `DamagerDestroyer`（存在漏洞但未被触发）

Bug 机制（以 `Place` → `PlaceOfEmployment` 为例）：

1. `Place` 被 Qwen3 tokenizer 编码为单 token `[17371]`，`PlaceOfEmployment` 编码为 `[17371, 2124, 36032, 478]`
2. 当 event type 是 `ArrestJailDetain.Unspecified`（valid roles = `{Crime, Detainee, Jailer, Place}`），第一个 token `17371` 被 prefix mask 正确放行（因为它能到达合法的 `Place`）
3. 生成后 `partial = "Place"`，进入 continuation mask
4. `_apply_role_continuation_mask` 中：
   - `still_reachable = {"Place"}`（allowed roles 中以 "Place" 开头的）
   - 检查所有 grammar-valid token：
     - 闭合引号 `"`：`"Place".startswith('Place"')` → False → **BLOCK**
     - `Of`：`"Place".startswith("PlaceOf")` → False → **BLOCK**
   - 结果：**所有 token 都被归类为 block，`tokens_allowed` 为空**
   - Safety net `if not tokens_allowed: return logits` 触发 → **不做任何 masking**
5. 模型自由生成 `Of` → `Employ` → `ment`，产生 `PlaceOfEmployment`

### 修复建议

在 `_apply_role_continuation_mask`（`type_mask_processor.py` ~L651）中，当 `partial` 精确匹配 `still_reachable` 中的某个 role 时，将闭合引号 token 显式加入 `tokens_allowed`：

```python
# After line: extended = partial + text
# Add exact-match handling:
exact_match_exists = partial in still_reachable
if exact_match_exists and text == '"':
    tokens_allowed.append(tid)
    continue
```

或更通用地：在分类 token 时，除了 `r.startswith(extended)` 检查外，也检查 `partial == r`（完整匹配时允许终止符）。

---
