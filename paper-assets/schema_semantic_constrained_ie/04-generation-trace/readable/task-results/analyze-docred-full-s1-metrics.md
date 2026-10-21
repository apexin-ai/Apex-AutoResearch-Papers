# analyze docred full s1 metrics

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_docred_full_s1_metrics_20260514T083246_result.json`
- **Structured JSON:** [`c051e883209b8166dea1.json`](../../sessions/c0/c051e883209b8166dea1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是 **phase2_docred_full_s1** 的完整结果：

## DocRED Full S1 结果

| 指标 | Phase 0 Unconstrained | Grammar-only | **Full S1** | 变化 (vs grammar_only) |
|------|----------------------|--------------|-------------|----------------------|
| **DR** | 18.7%* | 26.17% | **10.19%** | **↓61.1%** |
| **RV** | 28.9% | 0.03% | **0.03%** | = |
| **ET** | 7.5% | 0% | **0%** | = |
| **R-F1** | ~8.2% | 8.24% | **8.17%** | -0.07pp |
| Entity-F1 | — | 58.90% | **58.96%** | +0.06pp |

*Phase 0 DR=18.7% 被 RV=28.9% 掩盖了部分 DR violations，实际可比基线是 grammar_only 的 26.17%

### 关键发现

1. **DR ↓61% (vs grammar_only)**：显著降低但未达 SciERC 的 94%，按标准属 **partial success** (50-80%)
2. **RV/ET 完全消除**：grammar 层有效
3. **R-F1 基本持平**：semantic 约束未损害 extraction quality
4. **跨数据集递减效应**：SciERC (7 rels) → 94% | DocRED (96 rels) → 61%

### 论文 Framing 建议
不能 claim "cross-dataset generalization"，需 nuanced framing：semantic constraint 效果随 schema 复杂度递减，但在 96-relation 复杂 schema 上仍实现 61% DR 降低。

### Unconstrained 进度
PID 170502 仍在运行（58min），181/998 docs 完成。预计还需 ~4.5 小时。

---
