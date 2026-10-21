# D120: threshold_onset D105 True 3σ Fix — Validation Report

## Change Summary

**File**: `run_5method_analysis_d102.py` (both westd-19828 and westd-17855)
**Backup**: `run_5method_analysis_d102.py.bak_pre_d120` (westd-19828)

### Modified Function: `_onset_gen` (line 142)

**Before (3x_sigma_drift)**:
```python
def _onset_gen(series, name):
    s = orient(series, name)
    mu, sigma = s[0], np.std(s[:3]) if len(s) >= 3 else np.std(s)
    if sigma < 1e-12:
        sigma = np.std(s) if np.std(s) > 1e-12 else 1.0
    for i in range(1, len(s)):
        drift = abs(s[i] - mu)
        if drift >= 3.0 * sigma:
            return i
    return None
```

**After (D105 true 3σ)**:
```python
def _onset_gen(series, name):
    s = orient(series, name)
    base, sigma = s[0], np.std(s)
    if sigma < 1e-12:
        return None
    thresh = base + 3.0 * sigma
    for i in range(1, len(s)):
        if s[i] > thresh:
            return i
    return None
```

### Key Differences

| Aspect | 3x_sigma_drift | D105 true 3σ |
|--------|---------------|--------------|
| sigma source | `std(s[:3])` (first 3 points) | `std(s)` (full series) |
| drift check | `abs(s[i] - mu) >= 3σ` (bidirectional) | `s[i] > base + 3σ` (unidirectional, worse direction only) |
| sigma fallback | Falls back to `std(s)` then `1.0` | Returns None if σ < 1e-12 |

### Other Changes
- `"threshold": "3x_sigma_drift"` → `"true_3sigma_d105"` (line 169)
- `"threshold_criterion": "3x_sigma_drift"` → `"true_3sigma_d105"` (line 313)

## Validation: alpha_sweep_a050_s42_fp32

### Results
- Data: `results/alpha_sweep/a050_s42` (11 generations, Pythia-410M, α=0.50, seed=42)
- **threshold_onset_3sigma: 0/8** (all downstream onsets = None)

### Per-metric Onset (D105 true 3σ)
| Metric | Onset Gen | Notes |
|--------|-----------|-------|
| token_entropy | 1 | Strong canary signal (drift -16.3%) |
| ece | 2 | Strong canary signal (drift +703%) |
| distinct_1 | None | Drift insufficient to cross 3σ threshold |
| distinct_2 | None | Same |
| distinct_3 | None | Same |
| mauve | None | Same |

### Consistency Check
- D120 script output **matches reference** `onset_gen_3sigma` from `recompute_3sigma_d105.py` on all 8 pairs (MATCH: True)
- Result consistent with M037 audit pattern (thr3s = 0-2/8 across experiments)
- Result consistent with C4 experiments that had D105 inline recompute (e.g., `c4_a050_s43_fp32` = 0/8)

### Note on Expected Value Discrepancy
Task context stated "threshold 3σ 后应为 8/8". This was incorrect — 8/8 reflects the old `3x_sigma_drift` behavior (small σ from first 3 points makes threshold easy to cross). With true 3σ (full-series std), the threshold is substantially higher, and downstream metrics at α=0.50 don't cross it. This matches the M037 audit findings.

### Impact on Consensus K≥3
- Before D120 fix: threshold_onset voted "significant" for many pairs → inflated K values
- After D120 fix: threshold_onset = 0/8, removing one vote from many pairs
- Robust pairs (K≥3): 0/8 (previously higher due to inflated threshold votes)
- PermG FDR fwd: 0/8 (unchanged — independent of threshold fix)

## Servers Synced
- [x] westd-19828: modified in place + backup
- [x] westd-17855: copied via base64 transfer

## Status
**D120 threshold_onset fix: VALIDATED.** Ready for full recalculation across all experiments.
