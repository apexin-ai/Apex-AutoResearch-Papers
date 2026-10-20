# analysis sj union conll epsilon supplement

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sj_union_conll_epsilon_supplement_20260515T153727_result.json`
- **Structured JSON:** [`5404498b21424a91c178.json`](../../sessions/54/5404498b21424a91c178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both outputs saved. Results summary:

### 补充 A: SJ Union vs Max — CoNLL NER

| Metric | SJ_max | SJ_union | Δ |
|--------|--------|----------|---|
| ρ | 0.4314 | 0.4318 | +0.0004 |
| AUROC | 0.7039 | 0.7041 | +0.0002 |
| mean | 0.9718 | 0.9709 | -0.0009 |
| std | 0.0920 | 0.0941 | +0.0021 |

Union normalizer 在 CoNLL 上与 max normalizer 几乎无差别（Δρ = +0.0004, ΔAUROC = +0.0002）。Union 均值略低、方差略大（符合预期——union 分母 ≥ max 分母），但对下游排序能力无实质影响。

### 补充 B: ε = 0.001, 0.005 细粒度

| ε | tied_fraction | non_tied_n | selection_delta (pp) |
|---|---------------|------------|---------------------|
| 0.001 | 0.38% | 527 | +0.62 |
| 0.005 | 0.57% | 526 | +0.62 |

LP range 分布: min=0.0001, Q10=0.019, Q25=0.026, **median=0.040**, Q75=0.069, Q90=0.122, max=0.608

ε=0.05 不在 cliff 上——从 0.001 到 0.005 tied fraction 仅从 0.38% 增到 0.57%，Q10 就已经 0.019，绝大多数实例的 LP range 远大于这些极小 ε 值。

---
