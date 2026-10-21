# M037: Threshold 3σ Unified Audit + K≥3 Recompute

**Date**: 2026-05-20
**Task**: Audit Table 7 experiments for threshold_onset σ standard consistency, recompute K≥3 under unified D105 true 3σ + D111 direction check.

## Methodology

For each experiment, applied the following unified criteria:

| Rule | Description |
|------|-------------|
| **D105** | threshold_onset uses true 3σ (base + 3×std of full series), replacing `3x_sigma_drift` simple amplitude check |
| **D086** | Per-alpha BH FDR correction, n_perm=5000 for perm_granger |
| **D111** | Direction check: naive_xcorr and diff_xcorr require `peak_lag < 0` (canary leads downstream) |
| **M035** | `peak_lag < 0` = forward causation (corrected from old `peak_lag > 0`) |
| **D102** | Unified 8 pairs: canary={token_entropy, ece} × downstream={distinct_1, distinct_2, distinct_3, mauve} |

**K per pair** = number of methods (out of 5) voting "forward-significant":
- **naive_xcorr**: FDR-significant AND peak_lag < 0
- **diff_xcorr**: FDR-significant AND peak_lag < 0
- **threshold_onset_3σ**: canary onset < downstream onset (lead_time > 0)
- **perm_granger**: FDR-significant (forward direction)
- **ty_granger**: significant

**K≥3** = count of pairs with K ≥ 3.

---

## Summary Table

| Experiment | Display | Old Thresh | Naive(D111) | Diff(D111) | Thr(3σ) | PermG | TY | **K≥3(3σ+D111)** |
|---|---|---|---|---|---|---|---|---|
| generalize_pythia410m_wiki_a100_s42 | Pythia-410M s42 | 3x_sigma_drift | 7/8 | 6/8 | 2/8 | 6/8 | 1/8 | **6/8** |
| gen_gpt2m_a100_s43 | GPT-2m s43 | 3x_sigma_drift | 7/8 | 6/8 | 0/8 | 6/8 | 4/8 | **6/8** |
| generalize_opt1b_wiki_a100_s42 | OPT-1.3B s42 | 3x_sigma_drift | 7/8 | 6/8 | 2/8 | 6/8 | 0/8 | **6/8** |
| opt13b_wiki_a100_s43_fp32 | OPT-1.3B s43 | D105 3σ | 8/8 | 6/8 | 0/8 | 6/8 | 5/8 | **6/8** |
| generalize_pythia1b_c4_a100_s43 | C4 Pythia-1B s43 | 3x_sigma_drift | 4/8 | 8/8 | 2/8 | 8/8 | 4/8 | **6/8** |
| alpha_sweep_a050_postd093_s42_fp32 | Padding-410M s42 | unknown | 3/8 | 2/8 | 0/8 | 6/8 | 4/8 | **3/8** |
| pythia410m_wiki_a100_s43_fp32 | Pythia-410M s43 | unknown† | 6/8 | 6/8 | 0/8 | 6/8 | 6/8 | **6/8** |
| generalize_pythia14b_wiki_a100_s42 | Pythia-1.4B s42 | 3x_sigma_drift | 6/8 | 6/8 | 0/8 | 2/8 | 0/8 | **1/8** |
| generalize_pythia14b_wiki_a100_s43 | Pythia-1.4B s43 | 3x_sigma_drift | 0/8 | 6/8 | 0/8 | 6/8 | 3/8 | **3/8** |

† pythia410m_s43 only had old-format `analysis_results.json`; naive_xcorr/diff_xcorr were recomputed from raw metrics (raw Pearson p<0.05, no FDR).

---

## Per-Experiment Detail

### 1. Pythia-410M s42 (generalize_pythia410m_wiki_a100_s42)

- **Old threshold**: `3x_sigma_drift` (simple amplitude check, not true 3σ)
- **K≥3(3σ+D111) = 6/8**

| Pair | K | Naive(lag) | Diff(lag) | Thr3σ | PermG | TY | 3σ onset |
|---|---|---|---|---|---|---|---|
| ece→distinct_1 | 3 | Y(-2) | Y(-1) | n | Y | n | 4→- |
| ece→distinct_2 | 4 | Y(-1) | Y(-1) | n | Y | Y | 4→- |
| ece→distinct_3 | 3 | Y(-1) | Y(-1) | n | Y | n | 4→- |
| ece→mauve | 1 | n(+3) | n(+4) | Y | n | n | 4→9 |
| entropy→distinct_1 | 3 | Y(-1) | Y(-1) | n | Y | n | 2→- |
| entropy→distinct_2 | 3 | Y(-1) | Y(-2) | n | Y | n | 2→- |
| entropy→distinct_3 | 3 | Y(-1) | Y(-2) | n | Y | n | 2→- |
| entropy→mauve | 2 | Y(-3) | n(+5) | Y | n | n | 2→9 |

**Notes**: D111 has no impact here — same K≥3 with and without direction check. mauve pairs show weak signal (PermG not significant). threshold_onset_3σ significant only for mauve (late onset at gen 9).

### 2. GPT-2m s43 (gen_gpt2m_a100_s43)

- **Old threshold**: `3x_sigma_drift`
- **K≥3(3σ+D111) = 6/8**

| Pair | K | Naive(lag) | Diff(lag) | Thr3σ | PermG | TY | 3σ onset |
|---|---|---|---|---|---|---|---|
| ece→distinct_1 | 3 | Y(-1) | Y(-1) | n | Y | n | 5→- |
| ece→distinct_2 | 4 | Y(-2) | Y(-2) | n | Y | Y | 5→- |
| ece→distinct_3 | 4 | Y(-5) | Y(-3) | n | Y | Y | 5→- |
| ece→mauve | 1 | Y(-2) | n(-2) | n | n | n | 5→- |
| entropy→distinct_1 | 3 | Y(-2) | Y(-3) | n | Y | n | 3→- |
| entropy→distinct_2 | 4 | Y(-2) | Y(-3) | n | Y | Y | 3→- |
| entropy→distinct_3 | 3 | n(+4) | Y(-4) | n | Y | Y | 3→- |
| entropy→mauve | 1 | Y(-2) | n(-2) | n | n | n | 3→- |

**Notes**: threshold_onset_3σ = 0/8 — no downstream metric crosses 3σ threshold. All K≥3 driven by xcorr + Granger methods.

### 3. OPT-1.3B s42 (generalize_opt1b_wiki_a100_s42)

- **Old threshold**: `3x_sigma_drift`
- **K≥3(3σ+D111) = 6/8**

| Pair | K | Naive(lag) | Diff(lag) | Thr3σ | PermG | TY | 3σ onset |
|---|---|---|---|---|---|---|---|
| ece→distinct_1 | 3 | Y(-1) | Y(-1) | n | Y | n | 4→- |
| ece→distinct_2 | 3 | Y(-1) | Y(-1) | n | Y | n | 4→- |
| ece→distinct_3 | 3 | n(+3) | Y(-1) | Y | Y | n | 4→8 |
| ece→mauve | 1 | Y(-4) | n(+3) | n | n | n | 4→- |
| entropy→distinct_1 | 3 | Y(-1) | Y(-1) | n | Y | n | 3→- |
| entropy→distinct_2 | 3 | Y(-1) | Y(-1) | n | Y | n | 3→- |
| entropy→distinct_3 | 4 | Y(-1) | Y(-1) | Y | Y | n | 3→8 |
| entropy→mauve | 1 | Y(-4) | n(+3) | n | n | n | 3→- |

**Notes**: TY=0/8 — Toda-Yamamoto not significant for any pair. threshold_3σ only fires for distinct_3 (onset gen 8, late).

### 4. OPT-1.3B s43 (opt13b_wiki_a100_s43_fp32)

- **Old threshold**: `threshold_onset_3sigma` (D105 format, already true 3σ)
- **K≥3(3σ+D111) = 6/8**

| Pair | K | Naive(lag) | Diff(lag) | Thr3σ | PermG | TY | 3σ onset |
|---|---|---|---|---|---|---|---|
| ece→distinct_1 | 4 | Y(-3) | Y(-2) | n | Y | Y | 4→- |
| ece→distinct_2 | 4 | Y(-3) | Y(-1) | n | Y | Y | 4→- |
| ece→distinct_3 | 4 | Y(-1) | Y(-1) | n | Y | Y | 4→- |
| ece→mauve | 2 | Y(-3) | n(-4) | n | n | Y | 4→- |
| entropy→distinct_1 | 3 | Y(-2) | Y(-1) | n | Y | n | 3→- |
| entropy→distinct_2 | 3 | Y(-1) | Y(-1) | n | Y | n | 3→- |
| entropy→distinct_3 | 4 | Y(-1) | Y(-1) | n | Y | Y | 3→- |
| entropy→mauve | 1 | Y(-4) | n(-4) | n | n | n | 3→- |

**Notes**: This experiment already had D105 analysis. D111 direction check doesn't change K≥3 (all naive peak_lag < 0). threshold_3σ = 0/8 even in original D105 analysis.

### 5. C4 Pythia-1B s43 (generalize_pythia1b_c4_a100_s43)

- **Old threshold**: `3x_sigma_drift`
- **K≥3(3σ+D111) = 6/8**

| Pair | K | Naive(lag) | Diff(lag) | Thr3σ | PermG | TY | 3σ onset |
|---|---|---|---|---|---|---|---|
| ece→distinct_1 | 4 | Y(-1) | Y(-1) | n | Y | Y | 2→- |
| ece→distinct_2 | 3 | n(+3) | Y(-1) | n | Y | Y | 2→- |
| ece→distinct_3 | 3 | n(+2) | Y(-1) | n | Y | Y | 2→- |
| ece→mauve | 5 | Y(-1) | Y(-1) | Y | Y | Y | 2→8 |
| entropy→distinct_1 | 3 | Y(-1) | Y(-1) | n | Y | n | 1→- |
| entropy→distinct_2 | 2 | n(+5) | Y(-1) | n | Y | n | 1→- |
| entropy→distinct_3 | 2 | n(+5) | Y(-1) | n | Y | n | 1→- |
| entropy→mauve | 4 | Y(-1) | Y(-1) | Y | Y | n | 1→8 |

**Notes**: PermG = 8/8 (all pairs significant). mauve pairs have strong signal with threshold_3σ also contributing. D111 reduces naive from 8/8 to 4/8 but K≥3 stays at 6/8 due to PermG and TY support.

### 6. Padding-410M s42 (alpha_sweep_a050_postd093_s42_fp32)

- **Old threshold**: unknown (no config field in 5method_leadlag.json)
- **K≥3(3σ+D111) = 3/8**

| Pair | K | Naive(lag) | Diff(lag) | Thr3σ | PermG | TY | 3σ onset |
|---|---|---|---|---|---|---|---|
| ece→distinct_1 | 4 | Y(-1) | Y(-1) | n | Y | Y | 4→- |
| ece→distinct_2 | 2 | Y(-4) | n(-4) | n | Y | n | 4→- |
| ece→distinct_3 | 3 | Y(-4) | n(-4) | n | Y | Y | 4→- |
| ece→mauve | 0 | n(-5) | n(+4) | n | n | n | 4→- |
| entropy→distinct_1 | 3 | n(+1) | Y(-1) | n | Y | Y | 1→- |
| entropy→distinct_2 | 2 | n(+1) | n(-4) | n | Y | Y | 1→- |
| entropy→distinct_3 | 1 | n(+1) | n(-4) | n | Y | n | 1→- |
| entropy→mauve | 0 | n(+3) | n(+4) | n | n | n | 1→- |

**Notes**: α=0.50 (padding experiment) — weaker signal than α=1.0 experiments. threshold_3σ = 0/8 (no metric crosses 3σ). D111 direction check significantly impacts naive (peak_lag > 0 for entropy→distinct_1/2/3). Low K≥3 is expected for medium α.

### 7. Pythia-410M s43 (pythia410m_wiki_a100_s43_fp32)

- **Old threshold**: unknown (only old-format `analysis_results.json`)
- **K≥3(3σ+D111) = 6/8**

| Pair | K | Naive(lag) | Diff(lag) | Thr3σ | PermG | TY | 3σ onset |
|---|---|---|---|---|---|---|---|
| ece→distinct_1 | 4 | Y(-3) | Y(-1) | n | Y | Y | 4→- |
| ece→distinct_2 | 4 | Y(-3) | Y(-1) | n | Y | Y | 4→- |
| ece→distinct_3 | 4 | Y(-3) | Y(-1) | n | Y | Y | 4→- |
| ece→mauve | 0 | n(-5) | n(-2) | n | n | n | 4→- |
| entropy→distinct_1 | 4 | Y(-1) | Y(-1) | n | Y | Y | 2→- |
| entropy→distinct_2 | 4 | Y(-1) | Y(-1) | n | Y | Y | 2→- |
| entropy→distinct_3 | 4 | Y(-1) | Y(-2) | n | Y | Y | 2→- |
| entropy→mauve | 0 | n(-5) | n(+5) | n | n | n | 2→- |

**Caveat**: naive_xcorr and diff_xcorr significance was recomputed from raw metrics using scipy.stats.pearsonr (raw p<0.05, no BH FDR). For the 6 significant pairs, raw p-values are extremely small (<<0.001), so FDR correction would not change the result.

### 8. Pythia-1.4B s42 (generalize_pythia14b_wiki_a100_s42)

- **Old threshold**: `3x_sigma_drift`
- **K≥3(3σ+D111) = 1/8** ⚠️

| Pair | K | Naive(lag) | Diff(lag) | Thr3σ | PermG | TY | 3σ onset |
|---|---|---|---|---|---|---|---|
| ece→distinct_1 | 3 | Y(-1) | Y(-1) | n | Y | n | 2→- |
| ece→distinct_2 | 2 | n(+3) | Y(-1) | n | Y | n | 2→- |
| ece→distinct_3 | 1 | n(+3) | Y(-1) | n | n | n | 2→- |
| ece→mauve | 1 | Y(-5) | n(+4) | n | n | n | 2→- |
| entropy→distinct_1 | 2 | Y(-1) | Y(-1) | n | n | n | 1→- |
| entropy→distinct_2 | 2 | Y(-5) | Y(-1) | n | n | n | 1→- |
| entropy→distinct_3 | 2 | Y(-5) | Y(-1) | n | n | n | 1→- |
| entropy→mauve | 1 | Y(-5) | n(-5) | n | n | n | 1→- |

**Notes**: PermG only 2/8 significant → most pairs only have naive+diff (K=2). TY=0/8. threshold_3σ=0/8. This is a genuinely weak signal experiment — the 1.4B model may have sufficient capacity to resist collapse at α=1.0 within 11 generations.

### 9. Pythia-1.4B s43 (generalize_pythia14b_wiki_a100_s43)

- **Old threshold**: `3x_sigma_drift`
- **K≥3(3σ+D111) = 3/8**

| Pair | K | Naive(lag) | Diff(lag) | Thr3σ | PermG | TY | 3σ onset |
|---|---|---|---|---|---|---|---|
| ece→distinct_1 | 3 | n(+1) | Y(-1) | n | Y | Y | 2→- |
| ece→distinct_2 | 3 | n(+1) | Y(-1) | n | Y | Y | 2→- |
| ece→distinct_3 | 3 | n(+1) | Y(-1) | n | Y | Y | 2→- |
| ece→mauve | 0 | n(-5) | n(+5) | n | n | n | 2→- |
| entropy→distinct_1 | 2 | n(+5) | Y(-1) | n | Y | n | 1→- |
| entropy→distinct_2 | 2 | n(+5) | Y(-1) | n | Y | n | 1→- |
| entropy→distinct_3 | 2 | n(+5) | Y(-4) | n | Y | n | 1→- |
| entropy→mauve | 0 | n(+1) | n(+5) | n | n | n | 1→- |

**Notes**: D111 direction check has major impact — naive_xcorr drops from significant (raw) to 0/8 (all peak_lag > 0). K≥3 drops from 6/8 (without D111) to 3/8 (with D111). The 3 K≥3 pairs are ECE→distinct_1/2/3, driven by diff_xcorr + PermG + TY.

---

## Key Findings

### 1. Threshold Standard Audit

| Status | Experiments |
|---|---|
| **Had `3x_sigma_drift`** (simple amplitude, not true 3σ) | Pythia-410M s42, GPT-2m s43, OPT-1.3B s42, C4 Pythia-1B s43, Pythia-1.4B s42, Pythia-1.4B s43 |
| **Had D105 `threshold_onset_3sigma`** (true 3σ) | OPT-1.3B s43 |
| **Unknown** (old format / no config) | Padding-410M s42, Pythia-410M s43 |

**Result**: 6 of 9 experiments used `3x_sigma_drift`, 1 already had true 3σ, 2 had unknown threshold.

### 2. Impact of 3σ Correction

After switching from `3x_sigma_drift` to true 3σ, threshold_onset significance dropped dramatically:
- Most experiments: threshold_3σ = 0/8 (no downstream crosses 3σ)
- Only 3 experiments have any threshold_3σ significant pairs: Pythia-410M s42 (2/8), OPT-1.3B s42 (2/8), C4 Pythia-1B s43 (2/8)
- This is expected: 3σ is a much stricter threshold than `3x_sigma_drift`

### 3. Impact of D111 Direction Check

For most experiments, D111 does not change K≥3 (naive_xcorr peak_lag is already < 0). Notable exceptions:
- **Pythia-1.4B s43**: K≥3 drops 6/8 → 3/8 (all 8 naive peak_lag > 0)
- **Pythia-1.4B s42**: K≥3 drops 2/8 → 1/8 (some naive peak_lag > 0)

### 4. Overall K≥3 Distribution

- **7 of 9 experiments have K≥3 ≥ 3/8** (majority of pairs show multi-method consensus)
- **5 of 9 experiments have K≥3 = 6/8** (strong consensus in 75% of pairs)
- **Weakest**: Pythia-1.4B s42 (1/8) and Pythia-1.4B s43 (3/8) — consistent with larger models being more resistant to collapse

---

## Caveats

1. **pythia410m_s43**: Only old-format `analysis_results.json` available. naive_xcorr and diff_xcorr were recomputed from raw metrics without FDR correction. All significant pairs have p << 0.001, so FDR correction would not change results.

2. **Existing D105 results** (3sigma_recompute_d105.json and backfill): These did NOT apply D111 direction check. The M037 audit supersedes them with D111-corrected K≥3 values.

3. **PermG and TY significance**: Taken as-is from existing analysis files (5method_leadlag.json or d105_analysis.json). These were not recomputed.
