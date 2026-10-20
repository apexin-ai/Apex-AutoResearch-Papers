# write discussion sections

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_discussion_sections_20260514T182852_result.json`
- **Structured JSON:** [`9b11649769c841028862.json`](../../sessions/9b/9b11649769c841028862.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `discussion_paragraphs.tex`，三段内容：

1. **Low F1 Practical Significance** (118 words) — 零样本 F1~8% 是设定使然，supervised SOTA 40-50%；constraint enforcement 与 model quality 正交；F1 是 control variable 非 optimization target。

2. **CF Severity Argument** (133 words) — DR=hard constraint（下游不可用），CF=soft preference（单 triple 仍 type-valid）；dominant conflict Generic↔OtherScientificTerm 反映 type system 语义模糊；grammar_only CF=0.08% → full_s1 CF=9.90% 提供干净消融证据；提出 global entity-level type consensus 作为 future work。

3. **F1 Significance Difference** (117 words) — 机制归因到 grammar 层消除 OOV relation names：DocRED RV=29.66% (5189 OOV→FP) 被消除后 precision 显著提升；SciERC RV=1.39% (24 OOV) 效果不显著。Bootstrap CI 数据完整引用。

所有定量 claim 均带 `% exp_id` 注释追溯到 registry。需要你检查 `\citep{zhong2021frustratingly,ye2022packed}` 是否在 bib 中有对应条目。

---
