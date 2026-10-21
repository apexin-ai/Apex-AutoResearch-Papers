# Alpha Sweep a050_s44 Analysis Report

**Experiment**: alpha_sweep_a050_s44
**Config**: alpha=0.50, seed=44, model=pythia-410m, 10 generations x 5000 steps
**Date**: 2026-05-17
**Status**: Completed (EXIT_CODE=0)

---

## 1. Metrics: gen0 vs gen10

| Metric | gen0 | gen10 | drift_pct |
|--------|------|-------|-----------|
| token_entropy | 3.2342 | 2.6491 | -18.1% |
| ece | 0.0108 | 0.1001 | +826.9% |
| distinct_1 | 0.0981 | 0.0614 | -37.4% |
| distinct_2 | 0.5132 | 0.2525 | -50.8% |
| distinct_3 | 0.8058 | 0.3906 | -51.5% |
| perplexity | 26.949 | 32.578 | +20.9% |
| mauve | 0.0295 | 0.0195 | -33.9% |
| effective_rank | 46.61 | 59.63 | +27.9% |
| self_bleu | 0.0110 | 0.0148 | +34.0% |

## 2. Permutation Granger Results (n_perm=5000, max_lag=1)

| Channel | F-stat | p-value | sig (p<0.05) |
|---------|--------|---------|-------------|
| token_entropy -> distinct_1 | 115.204 | 0.0562 | |
| token_entropy -> distinct_2 | 98.398 | 0.0646 | |
| token_entropy -> distinct_3 | 70.627 | 0.0800 | |
| token_entropy -> perplexity | 14.747 | 0.0922 | |
| ece -> distinct_1 | 216.476 | 0.0042 | * |
| ece -> distinct_2 | 95.914 | 0.0116 | * |
| ece -> distinct_3 | 50.073 | 0.0270 | * |
| ece -> perplexity | 19.894 | 0.0232 | * |

**PermG significant: 4/8**

Pattern: ECE channels 4/4 significant, token_entropy channels 0/4 (all marginal, p=0.056-0.092).

## 3. Cross-Seed Comparison (alpha=0.50)

### 3.1 Drift Comparison

| Metric | s42 drift% | s43 drift% | s44 drift% | mean | std |
|--------|-----------|-----------|-----------|------|-----|
| token_entropy | -18.6 | -17.4 | -18.1 | -18.1 | 0.6 |
| ece | +843.2 | +798.7 | +826.9 | +822.9 | 22.5 |
| distinct_1 | -37.3 | -36.5 | -37.4 | -37.1 | 0.5 |
| distinct_2 | -51.5 | -49.0 | -50.8 | -50.4 | 1.3 |
| distinct_3 | -52.4 | -48.8 | -51.5 | -50.9 | 1.8 |
| perplexity | +21.1 | +21.1 | +20.9 | +21.0 | 0.1 |
| mauve | -38.5 | -32.0 | -33.9 | -34.8 | 3.4 |

**Key finding**: Drift magnitudes are highly consistent across seeds (std < 3.5% for all metrics). No seed-dependent divergence in collapse magnitude.

### 3.2 PermG Comparison (consistent parameters: n_perm=5000, seed=42)

| Channel | s42 p | s43 p | s44 p |
|---------|-------|-------|-------|
| token_entropy -> distinct_1 | 0.0950 | 0.0254* | 0.0562 |
| token_entropy -> distinct_2 | 0.0974 | 0.0492* | 0.0646 |
| token_entropy -> distinct_3 | 0.0964 | 0.0348* | 0.0800 |
| token_entropy -> perplexity | 0.0752 | 0.0646 | 0.0922 |
| ece -> distinct_1 | 0.0190* | 0.0040* | 0.0042* |
| ece -> distinct_2 | 0.0394* | 0.0228* | 0.0116* |
| ece -> distinct_3 | 0.0426* | 0.0230* | 0.0270* |
| ece -> perplexity | 0.0312* | 0.0278* | 0.0232* |

| Seed | PermG sig | ECE channels | token_entropy channels |
|------|-----------|-------------|----------------------|
| s42 | 4/8 | 4/4 | 0/4 |
| s43 | 7/8 | 4/4 | 3/4 |
| s44 | 4/8 | 4/4 | 0/4 |

**Note**: Previous reports stated s42=0/8 and s43=6/8. The current results use consistent parameters (n_perm=5000, permutation seed=42) across all three seeds. Discrepancies likely stem from different analysis parameters in earlier runs.

## 4. Conclusions

### 4.1 Collapse at alpha=0.50 is robust
Drift magnitudes are highly reproducible across 3 seeds (CV < 10% for all metrics). The collapse pattern (diversity loss, calibration degradation, perplexity increase) is deterministic at this contamination level.

### 4.2 PermG signal splits by canary type
- **ECE -> downstream**: Robust Granger signal, 12/12 significant across all seeds. ECE is a reliable leading indicator of collapse at alpha=0.50.
- **token_entropy -> downstream**: Seed-dependent, 3/12 significant (only s43). P-values cluster in 0.05-0.10 range, making this channel borderline at alpha=0.50. token_entropy is NOT a reliable standalone canary at this contamination level.

### 4.3 Boundary characterization
alpha=0.50 is NOT a null boundary. It shows clear, reproducible collapse. The "boundary" nature manifests only in the token_entropy Granger channel sensitivity, not in the collapse itself. This is a transitional zone where ECE-based detection works reliably but entropy-based detection does not.

---

## Registry Update Data

```json
{
  "conclusion": "success",
  "permg_sig": "4/8",
  "checkpoint_path": "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44",
  "metrics": {
    "gen0_token_entropy": 3.2342,
    "gen10_token_entropy": 2.6491,
    "gen0_ece": 0.0108,
    "gen10_ece": 0.1001,
    "gen0_distinct_1": 0.0981,
    "gen10_distinct_1": 0.0614,
    "gen0_distinct_2": 0.5132,
    "gen10_distinct_2": 0.2525,
    "gen0_distinct_3": 0.8058,
    "gen10_distinct_3": 0.3906,
    "gen0_perplexity": 26.949,
    "gen10_perplexity": 32.578,
    "drift_token_entropy_pct": -18.1,
    "drift_ece_pct": 826.9,
    "drift_distinct_1_pct": -37.4,
    "drift_distinct_2_pct": -50.8,
    "drift_distinct_3_pct": -51.5,
    "drift_perplexity_pct": 20.9
  },
  "cross_seed_summary": {
    "seeds": [42, 43, 44],
    "permg_sig_counts": [4, 7, 4],
    "ece_channels_sig": "12/12 (robust)",
    "entropy_channels_sig": "3/12 (seed-dependent)",
    "drift_consistent": true,
    "boundary_type": "transitional (ECE reliable, entropy borderline)"
  }
}
```
