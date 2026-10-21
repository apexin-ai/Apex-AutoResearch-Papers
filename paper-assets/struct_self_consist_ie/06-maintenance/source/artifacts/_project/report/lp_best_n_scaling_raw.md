## LP-best F1 N-scaling (Raw — pre-unified instance set)

| Dataset | N | LP-best F1 | Greedy F1 | LP Δ (pp) | seed | #inst |
|---------|---|-----------|-----------|-----------|------|-------|
| SciERC | 8 | 66.51% | 63.48% | +3.03 | 42 | 529 |
| SciERC | 16 | 66.35% | 64.07% | +2.28 | 42 | 529 |
| SciERC | 32 | 67.08% | 63.60% | +3.48 | 42 | 529 |
| SciERC | 64 | 67.12% | 63.79% | +3.33 | 42 | 529 |
| CoNLL | 8 | 89.57% | 89.47% | +0.09 | 123 | 2756 |
| CoNLL | 16 | 90.01% | 88.57% | +1.44 | 456 | 2756 |
| CoNLL | 32 | 89.23% | 88.62% | +0.61 | 42 | 2756 |
| CoNLL | 64 | 88.89% | 88.66% | +0.23 | 42 | 2756 |
| FewNERD | 8 | 79.27% | 71.23% | +8.04 | 42 | 32565 |
| FewNERD | 16 | 79.46% | 71.23% | +8.23 | 42 | 32565 |

Caveats:
- CoNLL N=8 and N=16 use different seeds (s123, s456) — not directly comparable for scaling
- FewNERD N=32 data not yet available (experiment running)
- Needs re-computation on unified instance set (P0 task)