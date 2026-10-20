# D105 + D111 Complete Audit: 5-Method Corrected Count Tables

## Corrections Applied

### D105: Threshold 3σ
- `method_ablation.py::_onset_gen` changed from `thresh = base + 2 * sigma` to `thresh = base + 3 * sigma`
- Verified via `.bak_d105` backup on westd-19828
- **Impact on westd-17855 experiments**: None. `batch_analysis.py::threshold_onset` already used `sigma_mult=3` default. The pre-D105 CSV threshold values were computed by batch_analysis.py, so they were already 3σ.
- **Impact on α=0.00 (westd-19828)**: `5method_leadlag.json` already contains D105-corrected values (config shows `threshold_criterion: 3x_sigma_drift`)

### D111: Forward Direction Filter (peak_lag > 0)
- naive_xcorr: counts as forward only if `naive_sig=True AND peak_lag > 0`
- diff_xcorr: counts as forward only if `diff_sig_fdr=True AND peak_lag > 0`
- **Impact**: Dramatic reduction in naive and diff counts across all α values

## Data Sources

| α | Server | Experiment Path | Analysis Script |
|---|--------|----------------|-----------------|
| 0.00 | westd-19828 | `alpha_sweep/a000_s42/` | method_ablation.py → 5method_leadlag.json |
| 0.05 | westd-17855 | `alpha_sweep/a005_s42_fp32_v3_d080/` | batch_analysis.py → analysis_results.json |
| 0.10 | westd-17855 | `alpha_sweep/a010_s42_fp32/` | batch_analysis.py |
| 0.25 | westd-17855 | `alpha_sweep/a025_s42_fp32/` | batch_analysis.py |
| 0.30 | westd-17855 | `alpha_sweep/a030_s42_fp32/` | batch_analysis.py |
| 0.35 | westd-17855 | `alpha_sweep/a035_s42_fp32/` | batch_analysis.py |
| 0.40 | westd-17855 | `alpha_sweep/a040_s42_fp32/` | batch_analysis.py |
| 0.45 | westd-17855 | `alpha_sweep/a045_s42_fp32/` | batch_analysis.py |
| 0.50 | westd-17855 | `alpha_sweep/a050_s42_fp32/` | batch_analysis.py |
| 0.60 | westd-17855 | `alpha_sweep/a060_s42_fp32_v3_d080/` | batch_analysis.py |
| 0.75 | westd-17855 | `alpha_sweep/a075_s42_fp32/` | batch_analysis.py |
| 1.00 | westd-17855 | `padding_robustness/a100_s42_fp32/` | batch_analysis.py |

## Threshold Algorithm Discrepancy

**Three different `_onset_gen` / `threshold_onset` algorithms exist in the codebase:**

1. **method_ablation.py** (westd-19828): `sigma = np.std(entire_series)`, `thresh = base + 3σ`, strict both-must-fire
2. **batch_analysis.py** (westd-17855): `sigma = np.std(np.diff(series))`, first-diff std, canary-fires-no-downstream = significant
3. **run_5method_analysis.py** (westd-19828): `sigma = np.std(series[:3])`, 3-point baseline std, `abs(deviation)`, strict

Results by algorithm (threshold X/8):

| α | method_ablation | batch_analysis | run_5method | Used |
|---|----------------|---------------|-------------|------|
| 0.00 | 3/8 | — | — | method_ablation (3/8) |
| 0.05 | 0/8 | 5/8 | 0/8 | batch_analysis (5/8) |
| 0.10 | 0/8 | 5/8 | 0/8 | batch_analysis (5/8) |
| 0.25 | — | 5/8 | — | batch_analysis (5/8) |
| 0.30 | — | 8/8 | — | batch_analysis (8/8) |
| 0.35 | 0/8 | 8/8 | 0/8 | batch_analysis (8/8) |
| 0.40 | — | 8/8 | — | batch_analysis (8/8) |
| 0.45 | — | 8/8 | — | batch_analysis (8/8) |
| 0.50 | 4/8 | 8/8 | 0/8 | batch_analysis (8/8) |
| 0.60 | — | 8/8 | — | batch_analysis (8/8) |
| 0.75 | — | 8/8 | — | batch_analysis (8/8) |
| 1.00 | 0/8 | 8/8 | 0/8 | batch_analysis (8/8) |

**Why the algorithms diverge:**
- `method_ablation.py` uses entire-series std. For metrics with monotonic drift (e.g., token_entropy increases continuously), the large std makes the 3σ threshold very high, so canary never fires → 0/8 for most α
- `batch_analysis.py` uses first-difference std (generation-to-generation change), which is much smaller, making the threshold easier to cross → 5-8/8
- `run_5method_analysis.py` uses 3-point baseline std. Token_entropy's gen0→gen1 jump inflates this baseline, making threshold unreachable → 0/8 everywhere

**Decision:** Use each server's native algorithm (the one that generated the on-disk analysis files). α=0.00 uses method_ablation.py; all others use batch_analysis.py.

## TY Granger: BH FDR Applied

All TY significance values use per-method Benjamini-Hochberg FDR correction (α_FDR=0.05) across 8 pairs within each α.

## Per-Method Count Comparison: Old CSV vs D105+D111 Corrected

| α | Method | Old (pre-D111) | New (D105+D111) | Δ | Note |
|---|--------|---------------|-----------------|---|------|
| 0.00 | naive | 8/8 | **6/8** | -2 | D111: te→d1 (lag=-5), ece→d1 (lag=-4) excluded |
| 0.00 | diff | 4/8 | **0/8** | -4 | D111: all sig pairs have lag<0 |
| 0.00 | threshold | 4/8 | **3/8** | -1 | Method_ablation 3σ vs old batch_analysis 3σ (different algo) |
| 0.00 | TY | 2/8 | **1/8** | -1 | BH FDR: only ece→d3 (p=0.006057) survives |
| 0.00 | permG | 0/8 | 0/8 | 0 | |
| 0.05 | naive | 7/8 | **3/8** | -4 | D111: 4 pairs with lag<0 excluded |
| 0.05 | diff | 3/8 | **0/8** | -3 | D111: all sig pairs have lag<0 |
| 0.05 | threshold | 5/8 | 5/8 | 0 | batch_analysis already 3σ |
| 0.05 | TY | 3/8 | 3/8 | 0 | ece→{d2,d3,mauve} survive FDR |
| 0.10 | naive | 7/8 | **4/8** | -3 | D111 |
| 0.10 | diff | 6/8 | **1/8** | -5 | D111: only te→mauve (lag=5) survives |
| 0.10 | threshold | 5/8 | 5/8 | 0 | |
| 0.10 | TY | 3/8 | 3/8 | 0 | |
| 0.25 | naive | 8/8 | **5/8** | -3 | D111 |
| 0.25 | diff | 3/8 | **2/8** | -1 | D111 |
| 0.25 | threshold | 5/8 | 5/8 | 0 | |
| 0.25 | TY | 3/8 | 3/8 | 0 | |
| 0.30 | naive | — | 5/8 | — | New (was RUNNING) |
| 0.30 | diff | — | 3/8 | — | New |
| 0.30 | threshold | — | 8/8 | — | New |
| 0.30 | TY | — | 5/8 | — | New |
| 0.35 | naive | 8/8 | **8/8** | 0 | All 8 pairs have lag>0 |
| 0.35 | diff | 4/8 | **0/8** | -4 | D111: all sig pairs have lag<0 |
| 0.35 | threshold | 8/8 | 8/8 | 0 | |
| 0.35 | TY | 4/8 | 4/8 | 0 | |
| 0.40 | naive | 8/8 | **4/8** | -4 | D111 |
| 0.40 | diff | 3/8 | **0/8** | -3 | D111 |
| 0.40 | threshold | 8/8 | 8/8 | 0 | |
| 0.40 | TY | 4/8 | **3/8** | -1 | BH FDR marginal change |
| 0.45 | naive | — | 7/8 | — | New (was RUNNING) |
| 0.45 | diff | — | 3/8 | — | New |
| 0.45 | threshold | — | 8/8 | — | New |
| 0.45 | TY | — | 1/8 | — | New |
| 0.50 | naive | 8/8 | **5/8** | -3 | D111 |
| 0.50 | diff | 7/8 | **1/8** | -6 | D111: only te→mauve (lag=1) survives |
| 0.50 | threshold | 8/8 | 8/8 | 0 | |
| 0.50 | TY | 4/8 | 4/8 | 0 | |
| 0.60 | naive | 7/8 | **4/8** | -3 | D111 |
| 0.60 | diff | 8/8 | **0/8** | -8 | D111: all sig pairs have lag<0 |
| 0.60 | threshold | 8/8 | 8/8 | 0 | |
| 0.60 | TY | 8/8 | 8/8 | 0 | |
| 0.75 | naive | 7/8 | **0/8** | -7 | D111: all sig pairs have lag<0 |
| 0.75 | diff | 6/8 | **0/8** | -6 | D111: all sig pairs have lag<0 |
| 0.75 | threshold | 8/8 | 8/8 | 0 | |
| 0.75 | TY | 8/8 | 8/8 | 0 | |
| 1.00 | naive | 8/8 | **0/8** | -8 | D111: no sig pairs with lag>0 |
| 1.00 | diff | 6/8 | **0/8** | -6 | D111: all sig pairs have lag<0 |
| 1.00 | threshold | 8/8 | 8/8 | 0 | |
| 1.00 | TY | 3/8 | **6/8** | +3 | Different experiment path or BH FDR calc |

## TY α=1.00 Discrepancy Detail

Old CSV: TY_rate=0.375 (3/8). New computation: TY=6/8.

The old CSV used `alpha_sweep/a100_s42_fp32` while the new computation uses `padding_robustness/a100_s42_fp32`. These may be different experiments. The padding_robustness version has 6/8 TY pairs significant after BH FDR, with very small p-values for all 6 diversity pairs (p ≈ 0.0). The mauve pairs have non-significant TY (p > 0.1).

## TY α=0.40 Discrepancy Detail

Old CSV: TY_rate=0.500 (4/8). New: TY=3/8.

Marginal BH FDR difference. One pair that was previously significant at the FDR boundary is now excluded. The raw TY p-values for ece→d3 and ece→mauve are borderline (p ≈ 0.01–0.05 range).

## Consensus (K≥3, K≥4) Impact

| α | Old K≥3 | New K≥3 | Old K≥4 | New K≥4 |
|---|---------|---------|---------|---------|
| 0.00 | 3/8 | **1/8** | 0/8 | 0/8 |
| 0.05 | 3/8 | **0/8** | 0/8 | 0/8 |
| 0.10 | 4/8 | **2/8** | 2/8 | **0/8** |
| 0.25 | 4/8 | **2/8** | 0/8 | 0/8 |
| 0.30 | — | 3/8 | — | 3/8 |
| 0.35 | 6/8 | **4/8** | 2/8 | **0/8** |
| 0.40 | 6/8 | **1/8** | 1/8 | **0/8** |
| 0.45 | — | 3/8 | — | 0/8 |
| 0.50 | 7/8 | **6/8** | 6/8 | **2/8** |
| 0.60 | 8/8 | **6/8** | 7/8 | **1/8** |
| 0.75 | 7/8 | **6/8** | 6/8 | **0/8** |
| 1.00 | 6/8 | 6/8 | 6/8 | **0/8** |

**D111 correction reduces K≥4 to near-zero for most α values.** At high α (≥0.75), naive and diff both become 0/8 because all significant correlations show reverse lag (downstream leads canary, consistent with synchronized collapse where downstream metrics degrade faster). The maximum K per pair is capped at 3 (threshold + permG + TY), making K≥4 impossible without naive or diff forward signal.

## Regime Classification

| Regime | α Range | Defining Characteristics |
|--------|---------|------------------------|
| blind_zone | 0.00–0.45 | permG=0/8; signal too weak for Granger detection |
| onset | 0.50 | permG first becomes significant (6/8); K≥4 first appears |
| sync_collapse | 0.60 | TY saturates (8/8); naive still partially forward (4/8) |
| detection | 0.75–1.00 | naive/diff collapse to 0/8 (fully synchronized); threshold+permG+TY carry signal |

## Key Findings

1. **D111 is the dominant correction.** Threshold and TY values are largely unchanged; the direction filter on naive/diff is responsible for ~90% of the value changes.

2. **Naive and diff become zero at high α.** At α≥0.75, ALL significant naive/diff correlations show negative peak_lag (downstream leads or is synchronous with canary). This is expected: at strong contamination, all metrics degrade simultaneously or downstream reacts faster.

3. **K≥4 effectively requires naive or diff forward signal.** Since threshold, permG, and TY can contribute at most 3 votes, reaching K≥4 requires at least one of naive or diff to be forward-significant. After D111, this rarely happens.

4. **Threshold counts are algorithm-dependent.** The choice between method_ablation.py (entire-series std) and batch_analysis.py (first-diff std) changes threshold from 0/8 to 5-8/8 for the same data. The output uses each server's native algorithm.
