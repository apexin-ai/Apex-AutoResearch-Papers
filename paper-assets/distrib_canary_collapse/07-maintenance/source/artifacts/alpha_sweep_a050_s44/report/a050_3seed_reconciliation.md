# a050 Three-Seed FDR Reconciliation Report

**Date**: 2026-05-17  
**Authoritative script**: `run_5method_analysis.py`  
**Parameters**: n_perm=5000, BH FDR q=0.05, family_size=8 (2 canaries x 4 downstreams), max_lag=1, difference=True

---

## Per-pair Perm Granger (family=8, q=0.05)

| Pair | s42 raw_p | s42 fdr_p | s42 sig | s43 raw_p | s43 fdr_p | s43 sig | s44 raw_p | s44 fdr_p | s44 sig |
|------|-----------|-----------|---------|-----------|-----------|---------|-----------|-----------|---------|
| entropy->d1 | 0.0950 | 0.0974 | No | 0.0302 | 0.0421 | **Yes** | 0.0586 | 0.0862 | No |
| entropy->d2 | 0.0974 | 0.0974 | No | 0.0482 | 0.0551 | No | 0.0672 | 0.0862 | No |
| entropy->d3 | 0.0964 | 0.0974 | No | 0.0316 | 0.0421 | **Yes** | 0.0800 | 0.0862 | No |
| entropy->ppl | 0.0752 | 0.0974 | No | 0.0632 | 0.0632 | No | 0.0862 | 0.0862 | No |
| ece->d1 | 0.0190 | 0.0852 | No | 0.0036 | 0.0288 | **Yes** | 0.0020 | 0.0160 | **Yes** |
| ece->d2 | 0.0394 | 0.0852 | No | 0.0204 | 0.0421 | **Yes** | 0.0102 | 0.0408 | **Yes** |
| ece->d3 | 0.0426 | 0.0852 | No | 0.0210 | 0.0421 | **Yes** | 0.0268 | 0.0536 | No |
| ece->ppl | 0.0312 | 0.0852 | No | 0.0252 | 0.0421 | **Yes** | 0.0178 | 0.0475 | **Yes** |

## Summary

| Seed | PermG FDR sig | Expected |
|------|--------------|----------|
| s42 | **0/8** | 0/8 |
| s43 | **6/8** | 6/8 |
| s44 | **3/8** | 3/8 |

All three seeds match expected values exactly.

---

## Discrepancy Diagnosis

### Root cause: `analyze_alpha_sweep.py` uses family_size=24, not 8

Worker B likely used `analyze_alpha_sweep.py` (output at `results/alpha_sweep/analysis_s44/alpha_sweep_analysis.json`), which applies BH FDR **per alpha, per method, across ALL seeds pooled**:

- For alpha=0.50, permutation_granger: family_size = 3 seeds x 8 pairs = **24**
- Result: only **2/24** FDR-significant (ece->d1 for s43 and s44)

### Comparison: family=8 (correct) vs family=24 (Worker B)

| Pair | family=8 sig | family=24 sig |
|------|-------------|--------------|
| s43 ece->d1 | Yes | Yes |
| s43 ece->d2 | Yes | No |
| s43 ece->d3 | Yes | No |
| s43 ece->ppl | Yes | No |
| s43 entropy->d1 | Yes | No |
| s43 entropy->d3 | Yes | No |
| s44 ece->d1 | Yes | Yes |
| s44 ece->d2 | Yes | No |
| s44 ece->ppl | Yes | No |

### Additional historical discrepancy (now resolved)

The May 15 analysis (`results/alpha_sweep/analysis/alpha_sweep_analysis.json`) also had **different raw p-values** for s42:
- Old: entropy->d1 raw=0.1064, ece->d1 raw=0.0292
- Current: entropy->d1 raw=0.0950, ece->d1 raw=0.0190

Cause: the old run did not pass `difference=True` to `permutation_granger_test`. This was fixed in the current `analyze_alpha_sweep.py` (analysis_s44 run uses updated code with matching raw p-values).

### Correct pipeline specification

| Parameter | Correct value | Source |
|-----------|--------------|--------|
| Script | `run_5method_analysis.py` | per-seed analysis |
| n_perm | 5000 | line 20 |
| BH FDR q | 0.05 | line 21 |
| family_size | 8 (implicit: all 8 pairs per seed) | lines 319-367 |
| max_lag (PermG) | 1 | line 177 |
| difference | True | line 177 |
| Correction scope | per-seed, forward direction | lines 364-365 |

**Conclusion**: The unified pipeline parameters (family=8, per-seed BH) are correctly implemented in `run_5method_analysis.py`. Worker B's divergent results stemmed from using `analyze_alpha_sweep.py` which pools seeds into a single BH family of 24. The hypothesis of family_size=4 (per-canary split) was not the actual cause, though such a split would yield 4/8 for all seeds (all ece pairs pass, no entropy pairs pass).
