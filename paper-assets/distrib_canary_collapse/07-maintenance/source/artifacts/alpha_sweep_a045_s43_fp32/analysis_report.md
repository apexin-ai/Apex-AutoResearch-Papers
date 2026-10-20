# Analysis Report: alpha_sweep_a045_s43_fp32

## Experiment Config
- **Model**: EleutherAI/pythia-410m
- **α**: 0.45 (synthetic ratio)
- **Seed**: 43
- **Precision**: fp32
- **Data**: WikiText-103 5k
- **Generations**: 10 (gen0–gen10, 11 total)
- **Steps/gen**: 5000
- **Server**: westd-17855

## Hypothesis
> Onset boundary cross-seed at α=0.45: s42 shows PermG=0/8 (blind zone, K3=3/8). If s43 also PermG=0/8 → onset > 0.45 is seed-robust, strengthening the [0.45, 0.50] onset claim.

## Result: **SUCCESS** — PermG=0/8 confirmed, onset > 0.45 is seed-robust

---

## s42 vs s43 Comparison

### Core Causality Metrics

| Metric | s42 | s43 | Δ |
|--------|-----|-----|---|
| PermG_fwd | 0/8 | 0/8 | = |
| PermG_rev | 0/8 | 0/8 | = |
| K≥3 | 3/8 | 2/8 | -1 |
| K≥4 | 0/8 | 0/8 | = |
| naive_xcorr (fwd) | 7/8 | 1/8 | -6 |
| diff_xcorr (fwd) | 3/8 | 1/8 | -2 |
| threshold_onset | 8/8 | 8/8 | = |
| ty_granger | 1/8 | 7/8 | +6 (C003: not usable as evidence at α≤0.50) |

### Drift Metrics (gen0→gen10, % change)

| Metric | s42 | s43 | Δ |
|--------|-----|-----|---|
| token_entropy | -18.73% | -19.61% | -0.88pp |
| perplexity | +12.19% | +12.37% | +0.18pp |
| ece | — | +800.00% | — |
| distinct_1 | — | -34.69% | — |
| distinct_2 | — | -47.24% | — |
| distinct_3 | — | -47.55% | — |
| mauve | — | -18.78% | — |
| effective_rank | — | +26.45% | — |

### Absolute Values (gen0 / gen10)

| Metric | s43 gen0 | s43 gen10 |
|--------|----------|-----------|
| token_entropy | 3.2342 | 2.5999 |
| ece | 0.0108 | 0.0972 |
| distinct_1 | 0.0983 | 0.0642 |
| distinct_2 | 0.5146 | 0.2715 |
| distinct_3 | 0.8140 | 0.4269 |
| perplexity | 26.95 | 30.28 |
| mauve | 0.0315 | 0.0256 |
| effective_rank | 46.61 | 58.94 |

## Consensus Detail (s43, per-pair)

| Pair | K | Methods |
|------|---|---------|
| token_entropy→distinct_1 | 3 | diff, thresh, ty |
| token_entropy→distinct_2 | 2 | thresh, ty |
| token_entropy→distinct_3 | 2 | thresh, ty |
| token_entropy→mauve | 2 | thresh, ty |
| ece→distinct_1 | 2 | thresh, ty |
| ece→distinct_2 | 2 | thresh, ty |
| ece→distinct_3 | 1 | thresh |
| ece→mauve | 3 | naive, thresh, ty |

## Key Observations

1. **PermG seed-robust at α=0.45**: Both s42 and s43 show PermG_fwd=0/8, PermG_rev=0/8. The permutation Granger test (with FDR correction) consistently finds no significant forward causality at this α level, confirming the blind zone.

2. **Individual methods are seed-sensitive**: naive_xcorr dropped from 7/8 (s42) to 1/8 (s43), while ty_granger rose from 1/8 to 7/8. This underscores that individual methods at boundary α values are unreliable — only PermG with FDR remains stable.

3. **Drift magnitudes are seed-consistent**: entropy drift (-18.73% vs -19.61%) and perplexity drift (+12.19% vs +12.37%) are within ~1pp, indicating the degradation dynamics are reproducible even though causality detection fails.

4. **K≥3 consensus is low but consistent**: s42=3/8, s43=2/8 — both well below the detection threshold, consistent with blind zone behavior.

5. **C003 note**: ty_granger=7/8 at α=0.45 (s43) MUST NOT be cited as supporting evidence. The 3-seed validation confirmed TY instability at α≤0.50 (d_max varies 0→1→2 across seeds, df_resid collapses to 1).

## Impact on Onset Boundary

The onset boundary remains firmly at **[0.45, 0.50]**:
- α=0.40: PermG=0/8 (s42, blind zone)
- α=0.45: PermG=0/8 (s42 + s43, blind zone — now 2-seed confirmed)
- α=0.50: PermG=6/8 (s42, detected)

Two-seed robustness at α=0.45 strengthens the claim that the PermG detection threshold lies strictly above 0.45.
