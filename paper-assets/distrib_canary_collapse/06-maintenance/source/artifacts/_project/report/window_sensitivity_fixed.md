# Window Sensitivity Analysis — Bugfix Report (D044-A)

## Pythia-410M, α=1.0, 4 seeds (42–45), T∈{5,6,7,8,9,10}

Two bugs in `window_sensitivity.py` caused incorrect TY column values in the original D044-A report. The 4/5-method consensus conclusions (NX/DX/TH/PG) were unaffected because TY is not required for 4/5 majority.

---

## Bugs Fixed

### Bug #1: Off-by-one in data slicing (line 193)
```python
# Before (wrong):  T=10 → 10 points (gen_0 to gen_9)
metrics = all_data[seed][:T]

# After (correct): T=10 → 11 points (gen_0 to gen_10)
metrics = all_data[seed][:T+1]
```
Paper convention: "T=10 generations" = gen_0 through gen_10 = 11 data points.

### Bug #2: Divergent TY implementation
`window_sensitivity.py` used a local `toda_yamamoto_v2` (hardcoded d=1, AIC-selected p, VAR `test_causality` chi²) which differed from the canonical `method_ablation.py` implementation (ADF-tested d_max, fixed p=1, manual OLS F-test). The local version returned `p=nan` at most window lengths due to VAR `test_causality` failing silently on short series.

**Fix**: Imported `toda_yamamoto` from `method_ablation.py`, deleted local TY functions.

---

## Table 1: TY Consensus Before vs After (pairs with ≥3/4 seed sig)

| T | Points (old→new) | TY sig old | TY sig new | NX/DX/TH/PG (unchanged) |
|---|---|---|---|---|
| 5 | 5→6 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
| 6 | 6→7 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
| 7 | 7→8 | 0/6 | 6/6 | 6/6, 6/6, 6/6, 6/6 |
| 8 | 8→9 | 3/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
| 9 | 9→10 | 0/6 | 3/6 | 6/6, 6/6, 6/6, 6/6 |
| 10 | 10→11 | **0/6** | **4/6** | 6/6, 6/6, 6/6, 6/6 |

**Root cause of old TY=0/6**: The buggy `toda_yamamoto_v2` returned `p=nan` for almost all seeds/windows because `VAR.test_causality()` silently fails when residual df is too low. The `nan` was then compared `< 0.05`, yielding False.

---

## Table 2: Full Consensus Summary (Fixed)

| T | Robust (≥4/5) | NX | DX | TH | PG | TY |
|---|---|---|---|---|---|---|
| 5 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |
| 6 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |
| 7 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 |
| 8 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |
| 9 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 3/6 |
| 10 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 4/6 |

All 6 pairs remain robust (≥4/5 methods) at every window length. TY is the most variable method, consistent with its low power at small T.

---

## Table 3: TY Seed-level Detail at T=10 (11 points, fixed)

| Pair | Seed 42 | Seed 43 | Seed 44 | Seed 45 | Consensus |
|---|---|---|---|---|---|
| entropy→d1 | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | **4/4** |
| entropy→d2 | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | **4/4** |
| entropy→d3 | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | ✓ (p=0.000) | **4/4** |
| ECE→d1 | ✓ (p=0.000) | ✓ (p=0.000) | ✗ (p=0.173) | ✓ (p=0.028) | **3/4** |
| ECE→d2 | ✓ (p=0.000) | ✓ (p=0.000) | ✗ (p=0.373) | ✗ (p=0.600) | 2/4 |
| ECE→d3 | ✓ (p=0.000) | ✓ (p=0.000) | ✗ (p=0.229) | ✗ (p=0.572) | 2/4 |

---

## Table 4: TY Seed-level Detail at T=10 — Old (buggy) vs New (fixed)

| Pair | Seed | Old TY | New TY |
|---|---|---|---|
| entropy→d1 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d1 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d1 | 44 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d1 | 45 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d2 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d2 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d2 | 44 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d2 | 45 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d3 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d3 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d3 | 44 | ✗ (p=nan) | ✓ (p=0.000) |
| entropy→d3 | 45 | ✗ (p=nan) | ✓ (p=0.000) |
| ECE→d1 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
| ECE→d1 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
| ECE→d1 | 44 | ✗ (p=nan) | ✗ (p=0.173) |
| ECE→d1 | 45 | ✓ (p=0.016) | ✓ (p=0.028) |
| ECE→d2 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
| ECE→d2 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
| ECE→d2 | 44 | ✗ (p=nan) | ✗ (p=0.373) |
| ECE→d2 | 45 | ✗ (p=nan) | ✗ (p=0.600) |
| ECE→d3 | 42 | ✗ (p=nan) | ✓ (p=0.000) |
| ECE→d3 | 43 | ✗ (p=nan) | ✓ (p=0.000) |
| ECE→d3 | 44 | ✗ (p=nan) | ✗ (p=0.229) |
| ECE→d3 | 45 | ✗ (p=nan) | ✗ (p=0.572) |

---

## Cross-validation with ty_audit_report (Method A, 11 points)

| Metric | Expected (ty_audit) | Got (window_sensitivity fixed) | Match |
|---|---|---|---|
| TE→d1,d2,d3 | 4/4 sig each | 4/4 sig each | ✓ |
| ECE→d1 | 3/4 sig | 3/4 sig (seed 44 n.s.) | ✓ |

---

## Impact on Paper Claims

- **4/5 consensus conclusions unchanged**: All 6 forward pairs remain robust at every T∈{5..10}. The bugs only affected TY, which was never required for the 4/5 majority.
- **TY now adds confirmatory power**: At T=10, TY confirms 4/6 pairs (all 3 TE→d* and ECE→d1), strengthening the case vs. the buggy 0/6.
- **TY variability across T is expected**: With p=1, d_max=1–2, residual df ranges from ~2 (T=5) to ~6 (T=10). Low df → unstable significance. This is consistent with the known TY power limitations documented in D013/D015.
