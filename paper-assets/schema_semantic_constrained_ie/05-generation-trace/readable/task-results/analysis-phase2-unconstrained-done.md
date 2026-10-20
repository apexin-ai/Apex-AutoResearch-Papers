# analysis phase2 unconstrained done

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_unconstrained_done_20260513T234549_result.json`
- **Structured JSON:** [`f14a4341907007b908f6.json`](../../sessions/f1/f14a4341907007b908f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报如下：

## Phase 2 Unconstrained Baseline 结果

### Metrics 总表

| Metric | Phase 2 Unconstrained | Phase 0 Unconstrained | Δ |
|--------|----------------------|----------------------|---|
| Entity F1 | 0.3101 | 0.3101 | **0** |
| Relation F1 | 0.0823 | 0.0823 | **0** |
| Entity Type VR | 0.40% | 0.40% | 0 |
| Relation Vocab VR | 1.39% | 1.39% | 0 |
| Domain/Range VR | 15.37% | 15.37% | 0 |
| Cross-field VR | 0.08% | 0.08% | 0 |
| Total Triples | 1724 | 1724 | 0 |
| Total Entities | 2474 | 2474 | 0 |

**与 Phase 0 完全一致** — 相同 prompt + 相同代码路径 + 相同 seed 产生确定性结果，可作为 Phase 2 constrained 实验的公平对比基线。

### 与 Grammar-only 对比

| Metric | Unconstrained | Grammar-only | Δ |
|--------|--------------|-------------|---|
| Entity F1 | 0.3101 | 0.3098 | -0.03pp |
| Relation F1 | 0.0823 | 0.0823 | 0 |
| ET Violation | 0.40% | **0%** | -0.40pp ✓ |
| RV Violation | 1.39% | **0%** | -1.39pp ✓ |
| DR Violation | 15.37% | 14.84% | -0.53pp |

Grammar-only 完全消除了 ET 和 RV violations，F1 基本无损（entity_f1 仅降 0.03pp）。DR violations 仍高达 14.84%，需要 semantic 层约束来解决。

---
