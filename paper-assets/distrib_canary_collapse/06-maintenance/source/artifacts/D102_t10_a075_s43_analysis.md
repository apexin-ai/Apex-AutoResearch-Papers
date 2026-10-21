# D102 Analysis: phase_diagram_t10_a075_s43_fp32

## Experiment Config
- Model: Pythia-410M, Dataset: wikitext-103
- T=10, α=0.75, seed=43, fp32
- 5000 steps/gen, lr=5e-5, batch=4, gen_max_tokens=256
- Server: westd-17855

## Status
- EXIT_CODE=0, gen_0–gen_10 complete (11 generations)
- Final training loss: 0.1734 (last step), avg train_loss: 0.4142

## 5-Method Lead-Lag Results

```
PermG_fwd (FDR):      6/8  ← KEY METRIC
PermG_rev (FDR):      0/8
DiffXCorr_fwd (FDR):  7/8
DiffXCorr_rev (FDR):  7/8
Threshold_3sigma:     0/8
TY_Granger:           0/8
Robust pairs (K≥3):   4/8
```

### Consensus Detail
```
token_entropy → distinct_1:  3/5  [naive, diff, perm]
token_entropy → distinct_2:  2/5  [diff, perm]
token_entropy → distinct_3:  2/5  [diff, perm]
token_entropy → mauve:       1/5  [diff]
ece → distinct_1:            3/5  [naive, diff, perm]
ece → distinct_2:            3/5  [naive, diff, perm]
ece → distinct_3:            3/5  [naive, diff, perm]
ece → mauve:                 0/5  [none]
```

## Cross-Seed Comparison (s42 vs s43)

| Metric | s42 | s43 | Match |
|--------|-----|-----|-------|
| **PermG (FDR) fwd** | **6/8** | **6/8** | **✓** |
| PermG (FDR) rev | — | 0/8 | ✓ |
| DiffXCorr (FDR) fwd | 6/8 | 7/8 | ≈ |
| Threshold 3σ | 0/8 | 0/8 | ✓ |
| TY Granger | 2/8 | 0/8 | (TY unstable at T=10, per C003) |
| Robust K≥3 | 6/8 | 4/8 | ↓ |

### K≥3 Drop Analysis (6/8 → 4/8)
s43 lost 2 robust pairs vs s42:
- **te→d2**: 3/5→2/5 (lost naive_xcorr vote)
- **te→d3**: 3/5→2/5 (lost naive_xcorr vote)

Additionally ece→mauve dropped from 2/5→0/5 (but was already below K≥3 threshold in s42).

All ece→d1/d2/d3 remain stable at 3/5. te→d1 stable at 3/5. The K≥3 drop is driven by borderline te→d2/d3 pairs losing one vote — the core PermG signal is unaffected.

## Gen-10 Downstream Metrics

| Metric | Gen 0 | Gen 10 | Δ |
|--------|-------|--------|---|
| perplexity | 26.95 | 77.82 | +188.8% |
| token_entropy | 3.234 | 2.287 | -29.3% |
| ece | 0.011 | 0.213 | +1836% |
| effective_rank | 46.61 | 79.04 | +69.6% |
| distinct_1 | 0.098 | 0.073 | -26.0% |
| distinct_2 | 0.515 | 0.347 | -32.7% |
| distinct_3 | 0.814 | 0.574 | -29.5% |
| mauve | 0.031 | 0.032 | +1.4% |
| self_bleu | 0.012 | 0.013 | +12.6% |

## Verdict

**PermG=6/8 confirmed seed-robust at T=10, α=0.75.** s42 and s43 produce identical PermG counts. This confirms the 6/8 ceiling at T=10 is not seed-dependent for α well above α_c(10)≈0.487.

K≥3 consensus dropped from 6/8→4/8 due to borderline te→downstream pairs, but the primary PermG metric (the one used for the phase diagram) is stable.
