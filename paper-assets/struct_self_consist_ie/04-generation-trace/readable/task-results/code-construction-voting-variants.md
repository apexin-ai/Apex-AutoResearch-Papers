# code construction voting variants

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_construction-voting-variants_20260519T223005_result.json`
- **Structured JSON:** [`e630384a20a03d0bb9ea.json`](../../sessions/e6/e630384a20a03d0bb9ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Here's the summary:

### Construction Voting Scheme Variants (Llama 8B FT, 3-seed mean, θ=2/N=0.25)

| Method | FewNERD F1 | Δ | p | SciERC F1 | Δ | p |
|---|---|---|---|---|---|---|
| Greedy | 78.42 | — | — | 64.57 | — | — |
| LP-weighted | 78.44 | +0.02 | 0.314 | 65.48 | +0.91 | 0.006* |
| **VC-weighted** | **78.57** | **+0.15** | **0.002*** | **65.62** | **+1.05** | **0.003*** |
| SJ-weighted | 78.22 | −0.20 | 1.000 | 65.08 | +0.51 | 0.062 |

Key findings:
- **VC-weighted is the best variant on both datasets**, significantly outperforming greedy (p<0.005 on both). On SciERC it even slightly beats LP-weighted (+1.05 vs +0.91 pp).
- **LP-weighted** is significant on SciERC but not on FewNERD (where the gap is negligible +0.02pp).
- **SJ-weighted hurts on FewNERD** (−0.20pp) and is borderline non-significant on SciERC (p=0.062). This makes sense — SJ over-weights "consensus" samples that may all share the same error.

Results saved to:
- Server: `/root/autodl-tmp/struct_self_consist_ie/output/construction_variants/`
- Local: `artifacts/construction_voting_variants.json`

---
