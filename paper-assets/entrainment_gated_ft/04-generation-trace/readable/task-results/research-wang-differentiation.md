# research wang differentiation

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_wang_differentiation_20260519T130431_result.json`
- **Structured JSON:** [`0869ab2f76234b927c22.json`](../../sessions/08/0869ab2f76234b927c22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md`（95行）。

核心结论：4个差异维度全部为 **Fully new**，与 Wang et al. 零重叠：

| 维度 | Wang et al. | 我们 |
|------|-------------|------|
| Convergence 量化 | 定性观察（"rankings change"） | Spearman ρ + permutation test + std trajectory |
| Scale dependency | 二元声明（"两个scale同pattern"） | 1.3B效果2倍于340M，340M rebound机制 |
| Per-example mechanism | 未涉及 | Jaccard ~0.04-0.07，architecture-specific feature profiles |
| Task-specificity | Ratio-sensitivity（哪些任务受ratio影响） | Convergence-strength by task type（retrieval ρ=-0.94 vs reasoning ρ=-0.55） |

Wang et al. 论文中最接近我们工作的表述是 Section 4.1 的 "rankings change" 和 "becomes comparable"——但这些是为架构推荐服务的事实陈述，不是被当作需要解释的现象。他们从未计算过 cross-architecture variance，未做 per-example 分析，未比较 scale 间 convergence 强度差异。

---
