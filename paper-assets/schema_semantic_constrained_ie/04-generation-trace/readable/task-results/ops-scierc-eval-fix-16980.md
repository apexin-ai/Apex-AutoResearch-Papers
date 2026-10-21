# ops scierc eval fix 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scierc_eval_fix_16980_20260520T154125_result.json`
- **Structured JSON:** [`1b1e5dee735c55d69efb.json`](../../sessions/1b/1b1e5dee735c55d69efb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 根因
`eval_d064.py` 第 10 行硬编码 `ONTOLOGY_FILE = ".../docred/ontology_constraints_docred.json"`，DocRED entity types（`LOC/ORG/PER/NUM/MISC/TIME`）和 relation types（Wikidata P-codes）与 SciERC 的完全不重叠，导致 ET=100%、RV=100%。另外 `normalize_etype()` 做 `.upper()` 但 `VALID_ENTITY_TYPES` 未统一大小写也会导致不匹配。

### 修复
- 新增 `--dataset` 参数（`docred/scierc/ace05/wikievents`），映射到对应 ontology 文件
- `VALID_ENTITY_TYPES` 和 `valid_pairs` 统一做 `.upper()` 以匹配 `normalize_etype`
- 自动检测 `relation_types` 格式（dict=DocRED P-code, list=SciERC 直接名称）
- 两台服务器已同步部署

### 修正后的 SciERC eval 结果

| Config | ET% | RV% | DR% | CF% | E-F1 | R-F1 |
|---|---|---|---|---|---|---|
| **beam2 s1** | 0.00 | 0.00 | 0.00 | 0.17 | 68.34 | 46.12 |
| **beam4 s1** | 0.00 | 0.00 | 0.00 | 0.00 | 68.06 | 46.18 |
| **beam8 s1** (111样本) | 0.00 | 0.00 | 0.00 | 0.00 | 72.07 | 54.39 |
| **beam8 unconstrained** | 0.00 | 0.00 | 1.04 | 0.00 | 67.59 | 45.14 |

beam8 unconstrained 的 DR%=1.04% 是唯一非零违规指标，符合预期（无约束解码允许不合法 entity type pair）。beam8 s1 仅 111 样本（未完成）。

---
