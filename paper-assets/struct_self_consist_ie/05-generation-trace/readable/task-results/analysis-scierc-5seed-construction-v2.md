# analysis scierc 5seed construction v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc-5seed-construction-v2_20260524T062052_result.json`
- **Structured JSON:** [`53de3ab9cf158a6b0397.json`](../../sessions/53/53de3ab9cf158a6b0397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**SciERC 5-Seed Entity Construction (N=8, θ=0.25, 529 instances/seed)**

| Method | F1 (%) | Δ vs Greedy | Pooled p |
|--------|--------|-------------|----------|
| Greedy | 64.67 ± 0.25 | — | — |
| MV Construction | 65.51 ± 0.49 | **+0.84 ± 0.65pp** | 0.0074 |
| LP Construction | 65.78 ± 0.72 | **+1.11 ± 0.91pp** | 0.0003 |

- **两种 construction 均显著优于 greedy**（pooled bootstrap p < 0.01）
- LP 优于 MV +0.27pp（p=0.0431，边际显著）
- MV 在 5/5 seeds 均为正提升；LP 在 4/5 seeds 为正（seed 42 是唯一例外，-0.58pp）
- LP 在 3/5 seeds 达到单独显著（seed 456/2024/3141）

结果已写入 `artifacts/scierc_5seed_construction_results.md` 并注册。

---
