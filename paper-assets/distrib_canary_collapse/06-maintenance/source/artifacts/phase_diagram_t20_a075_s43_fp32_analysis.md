# Phase Diagram: T=20, alpha=0.75, seed=43, FP32 (Cross-Seed Validation)

**Experiment**: `phase_diagram_t20_a075_s43_fp32`
**Server**: westd-17855
**Status**: Completed (EXIT_CODE=0, 21 generations gen_0–gen_20)
**Parent**: `t20_a075_s42_fp32` (seed=42)

## Core Detection Metrics

| Metric | s43 (this) | s42 (parent) | Match? |
|--------|-----------|-------------|--------|
| PermG_fwd_fdr | **6/8** | 6/8 | Exact |
| PermG_rev_fdr | **0/8** | 0/8 | Exact |
| DiffXCorr_fdr_fwd | **8/8** | 7/8 | +1 |
| DiffXCorr_fdr_rev | **8/8** | 7/8 | +1 |
| Threshold_onset_3sigma | **6/8** | 6/8 | Exact |
| Naive_xcorr_fwd_D111 | **4/8** | 4/8 | Exact |
| TY_granger_fwd | **3/8** | 5/8 | -2 |
| K>=3 (robust pairs) | **6/8** | 6/8 | Exact |
| K>=4 | **3/8** | — | — |

## Per-Pair Consensus (K votes, forward)

| Pair | K | Methods |
|------|---|---------|
| token_entropy < distinct_1 | 3/5 | diff, threshold, perm |
| token_entropy < distinct_2 | 3/5 | diff, threshold, perm |
| token_entropy < distinct_3 | 3/5 | diff, threshold, perm |
| token_entropy < mauve | 1/5 | diff |
| ece < distinct_1 | **5/5** | naive, diff, threshold, perm, ty |
| ece < distinct_2 | **5/5** | naive, diff, threshold, perm, ty |
| ece < distinct_3 | **5/5** | naive, diff, threshold, perm, ty |
| ece < mauve | 2/5 | naive, diff |

## PermG Forward Detail (FDR-corrected)

| Pair | F-stat | p_raw | p_fdr | sig_fdr |
|------|--------|-------|-------|---------|
| token_entropy < distinct_1 | 2032.85 | 0.0026 | — | true |
| token_entropy < distinct_2 | 1583.56 | 0.0036 | — | true |
| token_entropy < distinct_3 | 575.00 | 0.0022 | — | true |
| token_entropy < mauve | 0.85 | 0.3343 | — | false |
| ece < distinct_1 | 1013.96 | 0.0004 | — | true |
| ece < distinct_2 | 874.84 | 0.0006 | — | true |
| ece < distinct_3 | 481.44 | 0.0004 | — | true |
| ece < mauve | 0.96 | 0.2929 | — | false |

Non-detections: both mauve pairs (p > 0.29), consistent with s42 pattern.

## Threshold Onset Detail

| Pair | Canary onset | Downstream onset | Lead time |
|------|-------------|-----------------|-----------|
| token_entropy < distinct_1 | gen 1 | gen 4 | 3 |
| token_entropy < distinct_2 | gen 1 | gen 5 | 4 |
| token_entropy < distinct_3 | gen 1 | gen 7 | 6 |
| ece < distinct_1 | gen 2 | gen 4 | 2 |
| ece < distinct_2 | gen 2 | gen 5 | 3 |
| ece < distinct_3 | gen 2 | gen 7 | 5 |
| *_mauve | — | None | — |

Lead times identical to s42 (token_entropy: 3/4/5; ece: 2/3/4) except token_entropy<distinct_3 (s43: lead=6 vs s42: lead=5) and ece<distinct_3 (s43: lead=5 vs s42: lead=4).

## Directionality

- PermG: 6/8 forward vs 0/8 reverse — strong directional asymmetry confirmed
- DiffXCorr: 8/8 symmetric (expected for differenced series)
- Pattern identical to s42: forward causation (canary leads downstream)

## Drift Statistics (gen 0 -> gen 20)

| Metric | Gen 0 | Gen 20 | Drift |
|--------|-------|--------|-------|
| token_entropy | 3.234 | 2.471 | -23.6% |
| ece | 0.011 | 0.218 | +1915% |
| distinct_1 | 0.098 | 0.072 | -26.7% |
| distinct_2 | 0.515 | 0.342 | -33.5% |
| distinct_3 | 0.814 | 0.565 | -30.6% |
| mauve | 0.031 | 0.033 | +5.0% |

Mauve near-flat (+5%) explains its consistent non-detection across both seeds.

## Conclusion

**SUCCESS.** Cross-seed validation confirms the 6/8 ceiling at T=20, alpha=0.75:

1. **PermG=6/8** exact match with s42 — the same 6 distinct_N pairs significant, both mauve pairs non-significant
2. **Threshold=6/8** exact match — onset structure reproduced
3. **PermG directionality** 6/0 preserved — forward causation robust to seed change
4. **K>=3 robust pairs = 6/8** — same structural ceiling
5. TY drop (3/8 vs 5/8) is expected given C003 (TY seed-unstable at moderate T)

This is the 4th confirmation of the 6/8 structural ceiling (after T=10 s42/s43/s44, T=20 s42).

## Registry Metrics (for update_registry)

```json
{
  "exp_id": "phase_diagram_t20_a075_s43_fp32",
  "model": "pythia-410m",
  "alpha": 0.75,
  "seed": 43,
  "T": 20,
  "precision": "fp32",
  "status": "completed",
  "exit_code": 0,
  "server": "westd-17855",
  "perm_granger_fdr_fwd": 6,
  "perm_granger_fdr_rev": 0,
  "diff_xcorr_fdr_fwd": 8,
  "diff_xcorr_fdr_rev": 8,
  "threshold_onset_3sigma": 6,
  "naive_xcorr_fwd_D111": 4,
  "ty_granger_fwd": 3,
  "robust_pairs_K3": 6,
  "robust_pairs_K4": 3,
  "cross_seed_parent": "t20_a075_s42_fp32",
  "cross_seed_match": true,
  "verdict": "PASS",
  "verdict_note": "Cross-seed validation SUCCESS. PermG=6/8 exact match with s42. 6/8 ceiling confirmed at T=20 alpha=0.75. Directional asymmetry (6/0) preserved.",
  "analysis_path": "artifacts/phase_diagram_t20_a075_s43_fp32/data/5method_leadlag.json",
  "analyzed_at": "2026-05-22"
}
```
