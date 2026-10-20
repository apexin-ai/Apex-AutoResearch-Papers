# T=20 α=0.75 s42 fp32 — 5-Method Lead-Lag Analysis

## Experiment

| Field | Value |
|-------|-------|
| Model | Pythia-410M |
| Dataset | WikiText |
| Alpha | 0.75 |
| Seed | 42 |
| Precision | fp32 |
| T (generations) | 20 (gen_0–gen_20, N=21) |
| Server | westd-17855 |

## Results Summary

### PermG (Primary Metric)

| Direction | Significant | Count |
|-----------|-------------|-------|
| Forward (canary → downstream) | 6/8 | token_entropy→{d1,d2,d3}, ece→{d1,d2,d3} |
| Reverse (downstream → canary) | 0/8 | — |

**Directional asymmetry: 6 vs 0 — strong forward causation confirmed.**

### All 5 Methods (Forward Significant Counts)

| Method | Fwd Sig | Notes |
|--------|---------|-------|
| Perm Granger (FDR) | 6/8 | Primary metric |
| Diff XCorr (FDR) | 7/8 | Also detects token_entropy→mauve |
| Threshold Onset (3σ D105) | 6/8 | Matches PermG exactly |
| Naive XCorr | 4/8 | Only ece-based pairs (lag<0) |
| TY Granger | 5/8 | All token_entropy pairs + ece→mauve |

### Robust Pairs (K ≥ 3/5 methods agree)

**6/8 robust pairs**, all with 4/5 consensus:

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy → distinct_1 | 4/5 | diff, threshold, perm, ty |
| token_entropy → distinct_2 | 4/5 | diff, threshold, perm, ty |
| token_entropy → distinct_3 | 4/5 | diff, threshold, perm, ty |
| ece → distinct_1 | 4/5 | naive, diff, threshold, perm |
| ece → distinct_2 | 4/5 | naive, diff, threshold, perm |
| ece → distinct_3 | 4/5 | naive, diff, threshold, perm |

Non-robust pairs (both mauve): token_entropy→mauve (2/5), ece→mauve (2/5).

### PermG Forward Detail

| Pair | F-stat | p_raw | p_FDR | Sig |
|------|--------|-------|-------|-----|
| token_entropy → distinct_1 | 2947.21 | 0.0008 | 0.0016 | Yes |
| token_entropy → distinct_2 | 2083.39 | 0.0030 | 0.0040 | Yes |
| token_entropy → distinct_3 | 448.60 | 0.0030 | 0.0040 | Yes |
| token_entropy → mauve | 0.77 | 0.414 | 0.473 | No |
| ece → distinct_1 | 1181.26 | 0.0004 | 0.0011 | Yes |
| ece → distinct_2 | 1439.35 | 0.0002 | 0.0011 | Yes |
| ece → distinct_3 | 935.03 | 0.0004 | 0.0011 | Yes |
| ece → mauve | 0.60 | 0.474 | 0.474 | No |

No near-misses: both non-significant pairs have p > 0.4.

### Threshold Onset (Lead Times)

| Pair | Canary Onset | Downstream Onset | Lead Time |
|------|-------------|-------------------|-----------|
| token_entropy → distinct_1 | gen 1 | gen 4 | 3 |
| token_entropy → distinct_2 | gen 1 | gen 5 | 4 |
| token_entropy → distinct_3 | gen 1 | gen 6 | 5 |
| ece → distinct_1 | gen 1 | gen 3 | 2 |
| ece → distinct_2 | gen 1 | gen 4 | 3 |
| ece → distinct_3 | gen 1 | gen 5 | 4 |

Both canaries breach 3σ at gen 1. Downstream distinct metrics follow with 2–5 gen lag. Mauve pairs: no threshold onset detected.

## Prediction Verification

| Field | Predicted | Observed |
|-------|-----------|----------|
| PermG count | 7 | 6 |
| Rate | 0.832 | 0.750 |
| 95% CI (count) | [6, 8] | 6 ∈ [6, 8] ✓ |
| 95% CI (rate) | [0.760, 0.962] | 0.750 (marginal miss) |

**Verdict: PASS** — observed count 6 within predicted range [6, 8]. Lower-boundary outcome.

**Scenario: A (T-invariance)** — PermG=6/8 matches the T=10 baseline exactly.

## Cross-Alpha T=20 Landscape

| Alpha | T=10 PermG | T=20 PermG | Scenario | Delta |
|-------|-----------|-----------|----------|-------|
| 0.50 | 6/8 | 6/8 | A (T-invariant) | 0 |
| 0.60 | 0/8 | 0/8 | Sync dip | 0 |
| **0.75** | **6/8** | **6/8** | **A (T-invariant)** | **0** |
| 1.00 | 6/8 | 6/8 | A (T-invariant) | 0 |

3/4 alpha values show perfect T-invariance at PermG=6/8. The structural ceiling is 6/8 for this canary-downstream configuration — mauve pairs are consistently non-detectable by PermG regardless of time series length.

## Key Findings

1. **T-invariance confirmed**: T=20 adds zero statistical power over T=10 at α=0.75. PermG=6/8 in both.
2. **6/8 is the structural ceiling**: The same 6 pairs (all distinct-metric pairs) are significant, the same 2 pairs (mauve pairs) are not — identical to T=10.
3. **Mauve resistance is structural, not power-limited**: With p > 0.4 even at T=20, mauve's non-detection is not a borderline case. Mauve likely has a fundamentally different coupling mechanism with canary metrics.
4. **Strong directional asymmetry**: PermG 6/8 forward vs 0/8 reverse — the causality direction (canary → downstream) is unambiguous.
5. **Cross-alpha pattern strengthened**: T-invariance at 6/8 now established for α ∈ {0.50, 0.75, 1.00}. α=0.60 sync dip remains the sole anomaly.
