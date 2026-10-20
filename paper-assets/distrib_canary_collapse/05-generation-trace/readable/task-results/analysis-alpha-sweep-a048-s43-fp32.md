# analysis alpha sweep a048 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a048_s43_fp32_20260521T071507_result.json`
- **Structured JSON:** [`19f652e52f64e2228c98.json`](../../sessions/19/19f652e52f64e2228c98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

### alpha_sweep_a048_s43_fp32 — 5-Method Analysis

| Method | Forward | Reverse |
|--------|---------|---------|
| PermG (FDR) | **0/8** | 0/8 |
| DiffXCorr (FDR+D111) | 2/8 | 3/8 |
| Threshold 3σ (D105) | **0/8** | — |
| TY Granger | 2/8 | 2/8 |
| **K≥3** | **0/8** | |
| **K≥4** | **0/8** | |

### Cross-seed comparison (α=0.48)

| | s42 | s43 |
|--|-----|-----|
| PermG_fwd | 0/8 | 0/8 |
| DiffXCorr_fwd | 1/8 | 2/8 |
| TY_fwd | 3/8 | 2/8 |
| K≥3 | 1/8 | 0/8 |

### Drift (gen0→gen10)
- token_entropy: **-19.0%**, ece: **+835.0%**, perplexity: +18.1%
- distinct_1: -35.2%, distinct_2: -47.5%, distinct_3: -47.6%, mauve: -15.8%

### Onset (D105 3σ)
- token_entropy: gen 1, ece: gen 3, all downstreams: None

**Wall clock**: 14510s (~4.0h)

**Conclusion**: s43 confirms s42 — α=0.48 is a true blind zone, not seed artifact. Both seeds show PermG=0/8 and K≥3≤1/8 despite substantial drift. Phase transition α_c ∈ (0.48, 0.50], width ≤0.02.

---
