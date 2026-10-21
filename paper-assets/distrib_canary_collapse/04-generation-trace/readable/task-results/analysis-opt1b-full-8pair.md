# analysis opt1b full 8pair

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_opt1b_full_8pair_20260517T124735_result.json`
- **Structured JSON:** [`f0e313a50711e35b746b.json`](../../sessions/f0/f0e313a50711e35b746b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `results/generalize/opt1b_wiki_a100_s42/analysis/opt1b_6method_full.json`。

---

## OPT-1.3B WikiText α=1.0 — 8 Canonical Pairs

### Collapse trajectory:
| metric | gen0 | gen10 | drift% |
|--------|------|-------|--------|
| token_entropy | 3.048329 | 1.158671 | -62.0% |
| ece | 0.019933 | 0.422201 | +2018.1% |
| perplexity | 24.876836 | 647.419815 | +2502.5% |
| distinct_1 | 0.104029 | 0.071164 | -31.6% |
| distinct_2 | 0.526711 | 0.324831 | -38.3% |
| distinct_3 | 0.816691 | 0.522071 | -36.1% |
| mauve | 0.031181 | 0.029360 | -5.8% |

### Table 5 Row:
| Method | Sig Count | Sig Pairs |
|--------|-----------|-----------|
| Naive XCorr | 6/8 | entropy→d1, entropy→d2, entropy→d3, ece→d1, ece→d2, ece→d3 |
| Diff XCorr (FDR) | 6/8 | same 6 |
| Threshold Onset | 0/8 | (none) |
| PermG forward (FDR) | 6/8 | same 6 |
| PermG reverse (FDR) | 0/8 | (none) |
| TY Granger | 2/8 | entropy→d1, ece→d1 |
| Consensus ≥3/5 | 6/8 | all 6 distinct pairs |
| Consensus ≥4/5 | 2/8 | entropy→d1, ece→d1 |

### Per-pair detail:
| Pair | Naive | Diff | Thresh | PG_fwd | PG_rev | TY | votes |
|------|-------|------|--------|--------|--------|-----|-------|
| entropy→d1 | Y | Y | N | Y | N | Y | 4/5 |
| entropy→d2 | Y | Y | N | Y | N | N | 3/5 |
| entropy→d3 | Y | Y | N | Y | N | N | 3/5 |
| entropy→mauve | N | N | N | N | N | N | 0/5 |
| ece→d1 | Y | Y | N | Y | N | Y | 4/5 |
| ece→d2 | Y | Y | N | Y | N | N | 3/5 |
| ece→d3 | Y | Y | N | Y | N | N | 3/5 |
| ece→mauve | N | N | N | N | N | N | 0/5 |

### Key observations:
- **Strong directionality**: PermG forward 6/8 sig vs PermG reverse 0/8 — confirms canary→downstream direction, not reverse
- **mauve is non-responsive**: 0/8 across all methods (drift only -5.8%, essentially flat)
- **Threshold Onset = 0/8**: likely because both canary and downstream degrade from gen0→gen1 simultaneously (no detectable lead)
- **TY underpowered** as expected at T=11 (only 2/8 sig, but those 2 are the strongest pairs d1)
- **6/8 consensus ≥3/5**: all distinct_N pairs pass, mauve pairs fail universally

---
