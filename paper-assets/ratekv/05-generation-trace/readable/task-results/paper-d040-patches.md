# paper d040 patches

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d040_patches_20260514T120618_result.json`
- **Structured JSON:** [`f364179b4bef3b47dcbe.json`](../../sessions/f3/f364179b4bef3b47dcbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. LaTeX syntax is clean — braces and commands balanced, all numbers match source data.

**Summary of modifications:**

| Patch | File | Lines | Content |
|-------|------|-------|---------|
| 1a | `experiments.tex` | 41 | Table 1 caption: added multi-seed note (±0.06, 3 seeds, hires profiling, identical bit distributions) |
| 1b | `analysis.tex` | 85–89 | `\paragraph{Multi-seed stability.}` in §Profiling Resolution: 10.99±0.06, std/mean<0.6%, identical bit distribution {2:8, 4:100, 8:4}, 90.2% allocation agreement |
| 2 | `analysis.tex` | 91–95 | `\paragraph{Per-layer optimality.}` in §Profiling Resolution: brute-force oracle on 8 layers with alternatives, 5/8 exact match, max gap 0.018 PPL, total <0.04 |
| 3 | `experiments.tex` | 174–179 | §Cross-Dataset Stability rewritten: added uniform baselines for both directions (27%/42% reductions), Qwen-only caveat |

---
