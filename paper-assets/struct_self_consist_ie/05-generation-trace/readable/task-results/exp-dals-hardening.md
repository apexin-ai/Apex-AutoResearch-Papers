# exp dals hardening

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_dals_hardening_20260518T064430_result.json`
- **Structured JSON:** [`ccb7dcae27d78161d065.json`](../../sessions/cc/ccb7dcae27d78161d065.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary of results:

**SciERC N=8 (3 seeds, τ=0.05):**
| Seed | Greedy | LP Sel | DALS | Gain | 95% CI | p |
|------|--------|--------|------|------|--------|---|
| 42 | 64.41 | 65.05 | 65.55 | +1.14pp | [0.31, 2.02] | 0.009 |
| 123 | 64.59 | 64.36 | 65.38 | +0.79pp | [-0.09, 1.71] | 0.083 |
| 456 | 64.83 | 64.47 | 65.02 | +0.19pp | [-0.70, 1.06] | 0.669 |
| **Mean** | | | **65.32±0.27** | **+0.71±0.48pp** | | |

**SciERC N=16 (3 seeds):** DALS gain = +0.07±0.36pp (negligible, more samples reduce degeneracy naturally)

**CoNLL Qwen N=8:** DALS = 90.01 (-0.87pp vs greedy), p<0.001 — DALS hurts here because greedy already dominates LP selection

**CoNLL LLaMA N=8:** DALS = 92.39 (-0.04pp), p=0.50 — neutral, 86.8% instances are degenerate

**Few-NERD N=8:** DALS = 75.20 (+0.30pp), CI=[0.18, 0.42], p<0.001 — small but significant gain

Key takeaways:
- seed42 reproduces the expected +1.14pp gain exactly
- Cross-seed variance is non-trivial (0.19 to 1.14pp on SciERC N=8)
- DALS is beneficial when LP selection outperforms greedy (SciERC, Few-NERD) but harmful when it doesn't (CoNLL Qwen)
- Script + results saved to `code/dals_fixed_tau_evaluation.py` and `output/dals_hardening_results.json`

---
