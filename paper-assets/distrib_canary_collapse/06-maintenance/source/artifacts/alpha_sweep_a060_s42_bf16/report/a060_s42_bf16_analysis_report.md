# α=0.60 s42 bf16 Full Analysis Report

## Experiment
- Model: Pythia-410M, α=0.60, seed=42, bf16, 10 generations
- Server: westd-17855
- EXIT_CODE: 0 (but registered as 129/SIGHUP — C005 applies, data verified complete)

## Metrics Drift (gen_0 → gen_10)

| Metric | gen_0 | gen_10 | Drift% |
|--------|-------|--------|--------|
| token_entropy | 3.2574 | 2.6404 | -18.9% |
| ece | 0.0123 | 0.0426 | +246.5% |
| perplexity | 27.68 | 20.27 | -26.8% |
| distinct_1 | 0.0914 | 0.0663 | -27.5% |
| distinct_2 | 0.5043 | 0.3157 | -37.4% |
| distinct_3 | 0.8329 | 0.5707 | -31.5% |

Note: bf16 training — ppl not directly comparable to fp32 experiments. d1/d2/d3 drift unaffected by precision.

## 5-Method Lead-Lag (Unified 2σ threshold)

| Method | Forward | Reverse |
|--------|---------|---------|
| naive_xcorr | 8/8 | 8/8 |
| diff_xcorr | 8/8 | 8/8 |
| threshold_onset | 6/8 | 0/8 |
| perm_granger | 8/8 | 0/8 |
| ty_granger | 0/8 | 1/8 |

Consensus K>=4: 6/8 pairs
- K=4: token_entropy->d1, token_entropy->d2, token_entropy->d3, ece->d1, ece->d2, ece->d3
- K=3: token_entropy->perplexity, ece->perplexity

Key: Perm Granger shows perfect directional asymmetry (8/8 fwd, 0/8 rev).
TY Granger 0/8 — consistent with C003 (TY unreliable at alpha<=0.60 with T=11).

## MMCT Detection

| Mode | Sig/8 |
|------|-------|
| uniform_forward | 0/8 |
| uniform_bidirectional | 0/8 |
| weighted_pair_forward | 6/8 |
| weighted_pair_bidirectional | 6/8 |
| weighted_global_forward | 0/8 |
| weighted_global_bidirectional | 0/8 |

## Table 7 Format Row
naive: 8/8, diff: 8/8, thresh: 6/8, pg_fwd: 8/8, pg_rev: 0/8, ty: 0/8, K>=4: 6/8

## Regime Map Positioning
- α=0.50 (boundary): spotty detection, high seed variance
- **α=0.60: strong per-method signal, MMCT detectable via weighted_pair but not uniform/global**
- α=0.75 (detectable): broad consensus across methods

α=0.60 represents a "method-dependent detectability" regime — individual methods (especially perm Granger) detect reliably, but MMCT significance depends on weighting scheme. The weighted_pair mode captures this because it amplifies methods with low per-pair FPR (perm_granger, ty_granger), whereas global weighting dilutes across all pairs.
