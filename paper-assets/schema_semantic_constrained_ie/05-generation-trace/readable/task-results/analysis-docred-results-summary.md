# analysis docred results summary

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_results_summary_20260514T134954_result.json`
- **Structured JSON:** [`8daf401d2c57dbb99a5a.json`](../../sessions/8d/8daf401d2c57dbb99a5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已保存并注册：`artifacts/docred_phase2_ablation_analysis.md`

产出内容：

1. **LaTeX 消融表**（booktabs 格式）— 4 行（unconstrained / grammar_only / semantic_only 留空 / full_s1），6 列指标
2. **三个关键发现**：
   - **Grammar-only DR 上升机制**：RV 29.66%→0.03% 的同时，被强制映射到 valid relation 的 triple 继承了不匹配的 domain/range 约束，将 RV violation 转化为 DR violation（18.46%→26.17%）。这是 enabling dependency 的直接证据。
   - **Full S1 F1-neutral**：R-F1 +0.49pp, E-F1 +1.22pp，与 SciERC 趋势一致。
   - **跨数据集对比**：SciERC DR 0.93% vs DocRED 10.19%，残留 DR 与 schema 复杂度正相关（96 relations + 粗粒度 NER types），符合 Claim 1 预期。
3. **三个审稿攻击面**及防御策略：grammar-only 有害论、泛化性质疑、低 F1 质疑。
4. **semantic_only 待填清单**：完成后需验证 enabling dependency 假设。

---
