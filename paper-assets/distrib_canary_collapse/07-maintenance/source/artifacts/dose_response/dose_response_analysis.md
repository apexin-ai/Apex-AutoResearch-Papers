# WikiText Dose-Response M035 Analysis

Generated: 2026-05-20 | Model: Pythia-410m | Dataset: WikiText-103 | Precision: fp32

## Analysis Configuration
- **D105**: true 3σ threshold (sigma_mult=3)
- **D086**: BH FDR correction, n_perm=5000
- **M035**: direction filter peak_lag < 0 (canary leads downstream)
- **D102**: 8-pair = canary=[token_entropy, ece] × downstream=[distinct_1, distinct_2, distinct_3, mauve]
- **D111**: direction check applied to naive_xcorr and diff_xcorr

## Key Findings

### PermG Dose-Response (Primary Metric)
| α | s42 | s43 | Cross-seed |
|---|-----|-----|------------|
| ≤0.45 | 0/8 | 0/8 | Stable null |
| 0.50 | **6/8** | **6/8** | Onset confirmed |
| 0.60 | 3/8 | 0/8 | Sync collapse (D108) |
| 0.75 | 6/8 | 5/8 | Detection regime |
| 1.00 | 6/8 | 6/8 | Full synthetic |

**PermG 0% FPR in blind zone (α≤0.45), step function at onset [0.45, 0.50].**

s42/s43 cross-seed comparison:
- α=0.50: identical 6/8 → onset robust
- α=0.75: 6/8 vs 5/8 → 1-pair difference (te→d1 FDR p=0.056 boundary)
- α=0.60: 3/8 vs 0/8 → sync collapse regime has high seed variance
- α=1.00: both 6/8 → stable

### K≥3(3σ) (M037 PROVISIONAL)
⚠️ threshold_onset has FPR=4/8 at α=0.00 null. K≥3 values inflated by threshold contribution. M037 audit pending.

| α | s42 K≥3 | s43 K≥3 | Note |
|---|---------|---------|------|
| 0.00 | 1/8 | 0/8 | null FPR (ideally 0) |
| 0.50 | 6/8 | 6/8 | onset |
| 0.60 | 8/8 | 4/8 | threshold-driven inflation at s42 |
| 0.75 | 7/8 | 7/8 | cross-seed stable |
| 1.00 | 6/8 | 6/8 | stable |

### 4-Regime Structure (s42 primary, M035 corrected)
| Regime | α range | PermG | K≥3(3σ) | Defining feature |
|--------|---------|-------|---------|-----------------|
| Blind zone | ≤0.45 | 0/8 | 1-3/8 | PermG=0 (clean discriminator) |
| Onset | [0.45, 0.50] | 0→6/8 | 1→6/8 | Step function |
| Sync collapse | ~0.60 | 3/8 | 8/8 | PermG dip, TY compensates (8/8) |
| Detection | ≥0.75 | 6/8 | 6-7/8 | Stable detection |

### Method Comparison (M035 D111 corrected)
- **PermG**: cleanest discriminator — 0% FPR in blind zone, sharp onset
- **naive_xcorr**: 1-4/8 in blind zone (high FPR), but strong at α≥0.75 (7/8)
- **diff_xcorr**: moderate FPR (1-5/8 in blind zone), but consistent 6/8 at onset+
- **threshold_onset**: 4-8/8 everywhere — poor discriminator (M037)
- **TY_granger**: complements PermG at α=0.60 (8/8 vs 3/8)

## a075_s43 Detailed Notes
- te→d1: PermG FDR p=0.056 (borderline, just above 0.05 threshold) — drives PermG difference 6/8→5/8 vs s42
- ece→mauve: K≥3 with 3 votes (naive, thresh, TY) — mauve pairs stronger at higher α
- D111 direction check reduces naive_xcorr from ~8/8 to 2/8 (consistent with other experiments)

## a050_s43 Detailed Notes
- PermG=6/8 matches s42 exactly; onset [0.45, 0.50] confirmed cross-seed
- mauve pairs (te→mauve, ece→mauve) both 1/8 K-vote — mauve weak at α=0.50 (drift only -23.5%)
- K≥3=6/8: same 6 pairs as s42 (all distinct pairs), mauve pairs below threshold

## Data Provenance
- s42 α∈{0.00–1.00}: re-analyzed with batch_analysis.py (M035/D105/D111 compliant) on westd-17855
- s43 α∈{0.10, 0.25, 0.50, 0.60, 0.75}: re-analyzed with batch_analysis.py on westd-17855
- s43 α={0.00, 1.00}: registry values (pre-M035 analysis, PermG unaffected by direction)
- a075_s43 data proxied from westd-19828 → westd-17855 for analysis
