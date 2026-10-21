# analysis w1 cf fallback pilot detailed

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w1_cf_fallback_pilot_detailed_20260515T150442_result.json`
- **Structured JSON:** [`04b9216f37075ae95936.json`](../../sessions/04/04b9216f37075ae95936.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已更新并注册。核心发现：

**Pilot DR = 96.2% of unconstrained DR** — CF fallback 不是"部分降级"语义约束，而是**有效地消除了约束**。逐 relation 的 recovery rate：
- Feature-of 95.3%, Compare 93.0%, Part-of 93.5%, Hyponym-of 99.2%, Evaluate-for 96.1%
- 唯一保留约束效力的是 Used-for（tightness=0.03，极宽松）

报告包含完整的：
1. Per-relation DR 对比表（含 tightness 关联 + unconstrained 对照）
2. Attempted vs Effective 分解（58.9% / 36.6% / 4.5%）
3. CF 残余分析（唯一残余：eigenvectors，Material↔OtherScientificTerm）
4. DR 恶化根因（grammar-first fallback 占主导，完整 type-pair 分布）
5. 四条论文可用 claims（含新增的 "hierarchical fallback ≈ no constraint"）

---
