# fix section2 background numbers

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_section2_background_numbers_20260514T062508_result.json`
- **Structured JSON:** [`ea4bd5ce25dd0ddf41d1.json`](../../sessions/ea/ea4bd5ce25dd0ddf41d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数值一致性已修正。修改摘要：

**修正的错误：**
| 位置 | 旧值 | 新值 | 来源 |
|------|------|------|------|
| 原 Line 11 range | 3 (Part-of) → 6 (Used-for) | **17 (Compare) → 35 (Used-for)** | `ontology_constraints.json` |
| 原 Line 11 average | 3.73 | 删除（移至 line 14 用 24.0） | 计算验证 |
| 原 Line 14 SciERC avg | 26.1 | **24.0** | 7 relations: 17+26+21+21+25+35+23=168, 168/7=24.0 |
| 原 Line 14 DocRED "out of" | 529 | **36** | DocRED 也是 6 entity types, |E|²=36 |

**叙事调整：** 原文 line 11 和 line 14 数值自相矛盾（3.73 vs 26.1），现改为统一的 per-relation 叙事——整体平均 24.0/36 看似宽松，但 Compare (17, tightness 0.53) 和 Part-of/Hyponym-of (21, tightness 0.42) 排除 >40% type-pair space，与 §3 violation landscape 和 §5 per-relation 实验数据呼应。

---
