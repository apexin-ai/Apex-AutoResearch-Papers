# analysis phase2 scierc unconstrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_scierc_unconstrained_20260513T234927_result.json`
- **Structured JSON:** [`c305fc566d65e8bb4ee5.json`](../../sessions/c3/c305fc566d65e8bb4ee5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. 完整分析结果：

## Phase 2 Unconstrained Baseline — 分析结果

**结论: SUCCESS** — 与 Phase 0 完全一致，确认代码路径正确，constrained vs unconstrained 对比公平。

### 核心指标

| Metric | Phase 0 | Phase 2 Unconstrained | Delta |
|--------|---------|----------------------|-------|
| entity_f1 | 0.3101 | **0.3101** | 0 |
| relation_f1 | 0.0823 | **0.0823** | 0 |
| DR violation | 15.37% | **15.37%** | 0 |
| RV violation | 1.39% | **1.39%** | 0 |
| ET violation | 0.4% | **0.4%** | 0 |
| total_triples | 1724 | **1724** | 0 |

### 与 Phase 2 grammar_only 对比

| Metric | Unconstrained | Grammar Only | Delta |
|--------|--------------|-------------|-------|
| entity_f1 | 0.3101 | 0.3098 | -0.0003 |
| relation_f1 | 0.0823 | 0.0823 | 0 |
| DR violation | 15.37% | 14.84% | **-0.53pp** |
| RV violation | 1.39% | 0% | **-1.39pp** |
| ET violation | 0.4% | 0% | **-0.4pp** |

### Per-relation DR Violation Breakdown

| Relation | Triples | Violations | Rate |
|----------|---------|-----------|------|
| Feature-of | 486 | 163 | **33.5%** |
| Compare | 66 | 28 | **42.4%** |
| Part-of | 72 | 18 | 25.0% |
| Evaluate-for | 133 | 32 | 24.1% |
| Hyponym-of | 124 | 18 | 14.5% |
| Used-for | 787 | 6 | 0.8% |
| Conjunction | 32 | 0 | 0% |

所有 delta vs Phase 0 均为零，完美复现。Grammar_only 已将 RV 和 ET violation 降至 0%，DR violation 微降 0.53pp（语法约束对 domain-range 影响有限，符合预期）。

---
