# analysis exp 003 p2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-p2_20260519T135239_result.json`
- **Structured JSON:** [`0aea53e04605c272de70.json`](../../sessions/0a/0aea53e04605c272de70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-003-p2 完成，结论：NEGATIVE。**

| 架构 | helped mean | hurt mean | U | p | r_rb |
|------|-----------|----------|-------|-------|------|
| GDN | 3.370 | 3.338 | 148410 | 0.209 | -0.045 |
| RetNet | 3.443 | 3.421 | 107210 | 0.659 | -0.017 |
| HGRN2 | 3.378 | 3.354 | 112999 | 0.248 | -0.044 |

三个架构均 p>0.05，效应量可忽略 (|r|<0.05)。Pure-model perplexity 无法区分 helped/hurt samples。

跨架构比较中，Kruskal-Wallis 显著 (helped: p=0.020, hurt: p=0.0005)，主要由 RetNet 整体 perplexity 更高驱动，但这只反映架构差异而非 helped/hurt 区分能力。

**输出文件 (westb-48145):**
- `analysis/sample_perplexity_results.csv` — 5153 样本 per-sample loss
- `analysis/sample_perplexity_figure.{png,pdf}` — violin plot
- `analysis/sample_perplexity_summary.json` — 统计摘要

---
