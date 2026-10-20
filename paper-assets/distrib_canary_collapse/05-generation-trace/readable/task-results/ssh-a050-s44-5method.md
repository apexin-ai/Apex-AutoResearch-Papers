# ssh a050 s44 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a050_s44_5method_20260517T063654_result.json`
- **Structured JSON:** [`756ff886bdd801571153.json`](../../sessions/75/756ff886bdd801571153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## a050_s44 5-Method Lead-Lag 结果

**Per-method forward detection counts (/8 pairs)**:
- Naive XCorr: 4/8
- Differenced XCorr (FDR): 6/8
- Threshold Onset: 0/8
- Permutation Granger (FDR): 3/8
- Toda-Yamamoto: 0/8 (excluded per C003)

**Directionality**: Perm Granger reverse sig: 0/8

**Consensus ≥3/5**: 0/8 pairs
**Consensus ≥4/5**: 0/8 pairs

**Per-pair Perm Granger detail**:

| Pair | F-stat | fdr_p | Sig |
|------|--------|-------|-----|
| token_entropy→distinct_1 | 115.204 | 0.0862 | |
| token_entropy→distinct_2 | 98.398 | 0.0862 | |
| token_entropy→distinct_3 | 70.627 | 0.0862 | |
| token_entropy→perplexity | 14.747 | 0.0862 | |
| ece→distinct_1 | 216.476 | 0.0160 | * |
| ece→distinct_2 | 95.914 | 0.0408 | * |
| ece→distinct_3 | 50.072 | 0.0536 | |
| ece→perplexity | 19.893 | 0.0475 | * |

**Cross-seed comparison (α=0.50)**:

| Metric | s42 | s43 | s44 |
|--------|-----|-----|-----|
| Perm Granger FDR fwd | 0/8 | 6/8 | 3/8 |
| Perm Granger FDR rev | 0/8 | 0/8 | 0/8 |
| Robust pairs (≥3/5) | 0/8 | 1/8 | 0/8 |

0/8 pairs consistently Perm Granger significant across all 3 seeds. Directionality (0/8 reverse) is perfectly stable. ECE is the only canary with any Granger significance at α=0.50. This confirms α=0.50 is at the detection boundary with high seed variance.

Report registered: `art_20260517_daeb38`

---
