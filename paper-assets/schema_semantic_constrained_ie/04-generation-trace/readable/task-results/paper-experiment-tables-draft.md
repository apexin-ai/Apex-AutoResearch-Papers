# paper experiment tables draft

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiment_tables_draft_20260514T043003_result.json`
- **Structured JSON:** [`41b159b5d23705565f7a.json`](../../sessions/41/41b159b5d23705565f7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_tables_draft.tex` 并注册。4 张表的数据摘要：

**Table 1 — SciERC Ablation**: Full S1 将 DR 从 15.4% 降至 **0.9%** (-14.4pp)，RV/ET 归零，R-F1 微升至 8.4%（无损）。代价是 CF 升至 9.9%（约束解码强制合法 relation 但 entity pair 可能不匹配）。S2 效果接近但 R-F1 略低 (8.0%)。

**Table 2 — Per-Relation DR**: 降幅最大的是 Compare (-39.6pp) 和 Feature-of (-32.3pp)；Hyponym-of/Part-of/Used-for 在 S1 下完全归零。

**Table 3 — DocRED Phase 0**: Schema-informed prompt 在所有违规维度显著优于 minimal prompt (DR -5.9pp, RV -10.5pp, ET -6.9pp)，但 JSON 解析率略降 1.9pp。

**Table 4 — Cross-dataset**: DocRED baseline 违规率全面高于 SciERC（DR 18.7% vs 15.4%, RV 28.9% vs 1.4%），DocRED S1 结果待 `phase2_docred_full_s1` 完成后填入。

---
