# Table 5 (cross_env_civo) Full Validation Report

Date: 2026-05-27

## Executive Summary

Seven issues found in current Table 5 (analysis.tex):
1. **Cheetah baseline (593.9)** uses exp_023 series — different experiments from complete results table (exp_077/083 = 446.1). Results.tex footnote says "Cheetah 446.1".
2. **Cheetah trigger std (±33.9)** uses population std; all other rows use sample std. Should be ±47.9 (sample) for consistency.
3. **Walker CIVO count (8/8)** doesn't match any source: CSV says 5/5, complete table has 6 unique trigger seeds. Body text says "6/7 multi-joint locomotion seeds".
4. **Walker baseline seeds (s3, s4)** not in appendix complete results table — undocumented experiments.
5. **New experiments available**: Cheetah trigger s3 (exp_097=61.67), Cheetah control s1/s2 (exp_092=77.26, exp_093=151.18) not incorporated.
6. **Mixed seed counts**: Eval mean computed from different N than NVE (e.g., Walker trigger: eval N=3, NVE N=5).
7. **Cheetah NVE peak (8.27)** excludes exp_010b_s0 (108.52) without explanation; complete table shows it.

---

## Raw Data Verification

### Walker Walk

#### Baseline (dt=1)

**Source experiments (from cross_env_civo_comparison.csv):**

| Experiment | Seed | Eval@105K | Status |
|------------|------|-----------|--------|
| exp_001_baseline | s0/s1 | 915.67 | ✅ Verified (paper_data_walker_walk.json) |
| exp_001_baseline_s2 | s2 | 443.46 | ✅ In complete table as 443.5 |
| exp_001_baseline_s3 | s3 | 869.03 | ⚠️ NOT in complete results table |
| exp_001_baseline_s4 | s4 | 922.80 | ⚠️ NOT in complete results table |

**Statistics:**
- Mean: 787.7 ✅ correct: (915.67+443.46+869.03+922.80)/4 = 787.74
- Std: 230.8 ✅ correct (sample std, N-1)
- N: 4

**Discrepancy:** Complete results table (Table 4, appendix) only lists 2 Walker baselines (915.7 and 443.5). Seeds s3 (869.03) and s4 (922.80) have no metrics.jsonl on server and are undocumented in the paper. Results.tex Table 1 uses single-seed baseline 915.7.

---

#### Trigger (trained dt_emb, subsample ON, H=8)

**Eval return sources (from CSV, N=3):**

| Experiment | Seed | Eval Return | Step | Status |
|------------|------|-------------|------|--------|
| exp_008d | s0/s1 | 58.5 | @112K | ⚠️ Not at 105K; complete table says 82.8 @55K |
| exp_008d_civo_trigger_s3 | s3 | 267.6 | @105K | ✅ Complete table: 268 @105K |
| exp_059_walker_trained_s5 | s5 | 95.8 | @105K | ✅ Complete table: 95.8 @105K |

**Statistics (eval):**
- Mean: 140.6 ✅ correct: (58.5+267.6+95.8)/3 = 140.63
- Std: 111.5 ✅ correct (sample std)
- N: 3 (eval), but NVE computed from 5 seeds

**NVE sources (N=5):**

| Seed | NVE | Source |
|------|-----|--------|
| s1 (008d) | 4.13 | Complete table: 4.12 |
| s2 (009b) | 1.62 | Complete table: 1.62 |
| s3 (008d_s3) | 1.53 | Complete table: 1.53 |
| s4 (008d_s4) | 4.62 | Complete table: 4.62 |
| s5 (059) | 4.72 | Complete table: 4.72 |

**NVE Peak: 4.72×** ✅ correct (max across 5 seeds)

**CIVO count:**
- Paper Table 5: ✓ (8/8) ❌ WRONG
- CSV: 5/5 (all 5 NVE seeds exceed 1.5×)
- Complete table unique trigger seeds: 6 (008d, 009b, 008d_s3, 008d_s4, 059, 068) — all CIVO
- Body text: "6/7 multi-joint locomotion seeds" (across Walker + Cheetah)
- **Recommendation**: Change to ✓ (5/5) or ✓ (6/6) depending on whether exp_068 (s1 repro) is included

**Additional experiment (not in CSV):**
- exp_068 (s1 repro): eval=39.1, NVE=4.12 (in complete table but not in Table 5 calculation)

---

#### Control (no dt_emb, subsample ON, H=8)

**Current paper uses complete table seeds (N=4):**

| Experiment | Seed | Eval@105K | NVE | Status |
|------------|------|-----------|-----|--------|
| exp_008f s0 (CORRECTED) | s0 | 139.5 | 1.69* | ✅ Verified from metrics.jsonl |
| exp_008f s1 | s1 | 468.8 | 0.88 | ✅ In complete table |
| exp_008f s4 | s4 | 289.3 | 0.76 | ✅ In complete table |
| exp_009c s3 | s3 | 311.9 | 1.04 | ✅ In complete table |

\* Footnote: NVE 1.69× reflects endpoint eval dip, not value overestimation.

**Statistics:**
- Mean: 302.4 ✅ correct: (139.5+468.8+289.3+311.9)/4 = 302.38
- Std: 134.8 ✅ correct (sample std)
- NVE Peak: 1.69× ✅ correct (max across 4 seeds)
- CIVO: ✗ (0/4) ✅ correct

**Note:** The original CSV used pre-correction 008f (eval=503) giving 373.8±111.9. Paper was correctly updated with corrected data.

---

### Cheetah Run

#### Baseline (dt=1)

**Source experiments (from CSV, N=5):**

| Experiment | Eval@105K | Status |
|------------|-----------|--------|
| exp_023a | 624.7 | ⚠️ NOT in complete results table |
| exp_023b | 520.3 | ⚠️ NOT in complete results table |
| exp_023_s2 | 645.4 | ⚠️ NOT in complete results table |
| exp_023_s3 | 642.13 | ⚠️ NOT in complete results table |
| exp_023_s4 | 537.03 | ⚠️ NOT in complete results table |

**Statistics:**
- Mean: 593.9 ✅ correct: (624.7+520.3+645.4+642.13+537.03)/5 = 593.91
- Std: 60.4 ✅ correct (sample std)
- N: 5

**Complete results table baselines (different experiments!):**

| Experiment | Eval@105K |
|------------|-----------|
| exp_077 (s0) | 448.1 |
| exp_083 (s1) | 444.0 |
| Mean | 446.1 |

**Critical discrepancy:** Table 5 uses exp_023 series (mean=593.9), but the rest of the paper uses exp_077/083 (mean=446.1). Results.tex footnote explicitly states "Cheetah 446.1 (2-seed mean at 105K)". These are different experiments giving a ~148 point difference.

---

#### Trigger (trained dt_emb, subsample ON, H=8)

**Paper Table 5 uses 2 seeds (from complete table):**

| Experiment | Seed | Eval@105K | NVE | Status |
|------------|------|-----------|-----|--------|
| exp_010b | s1 | 51.7 | 8.27 | ✅ In complete table |
| exp_078 | s0 | 119.5 | 4.10 | ✅ In complete table |

**EXCLUDED from eval mean:**
- exp_010b_s0: eval=0.83, NVE=108.52 (in complete table but excluded from Table 5 without explanation)

**Statistics:**
- Mean: 85.6 ✅ correct: (51.7+119.5)/2 = 85.6
- Std: 33.9 ⚠️ This is POPULATION std (N divisor): sqrt(((51.7-85.6)² + (119.5-85.6)²)/2) = 33.9
  - Sample std would be: 47.9
  - **ALL other rows in the table use sample std (N-1)**. This is INCONSISTENT.
- NVE Peak: 8.27× — max of exp_010b (8.27) and exp_078 (4.10), EXCLUDING exp_010b_s0 (108.52)
- CIVO: ✓ (2/2) — consistent with 2-seed trigger count

**New experiment on server:**
- exp_097_cheetah_008d_s3: eval@105K = 61.67
  - Peak raw ve_ratio (35K+): 2.26× @45K (then self-corrects)
  - If included: 3-seed eval mean = 77.6 ± 36.6 (sample std)

---

#### Control (no dt_emb, subsample ON, H=8)

**Paper Table 5 uses 2 seeds:**

| Experiment | Seed | Eval@105K | NVE | Status |
|------------|------|-----------|-----|--------|
| exp_024b s0 | s0 | 96.5 | 0.20 | ✅ In complete table |
| exp_024b s1 | s1 | 77.3 | 0.10 | ✅ In complete table |

**Statistics:**
- Mean: 86.9 ✅ correct: (96.5+77.3)/2 = 86.9
- Std: 13.6 ✅ correct (sample std): sqrt(((96.5-86.9)² + (77.3-86.9)²)/1) = 13.58
- NVE Peak: 0.20× ✅ correct
- CIVO: ✗ (0/2) ✅ correct

**New experiments on server:**
- exp_092_cheetah_no_dt_emb_s1: eval@105K = 77.26, peak raw ve=0.70
- exp_093_cheetah_no_dt_emb_s2: eval@105K = 151.18, peak raw ve=0.54
- If all 4 seeds: mean = 100.6 ± 34.9 (sample std)

---

### Cartpole Swingup

#### Baseline
- Seeds: s0=809.4, s1=684.4, s2=526.1
- Mean: 673.3 ✅, Std: 142.0 ✅ (sample std)

#### Trigger
- Seeds: s0=211.1, s1=269.0, s2=228.9
- Mean: 236.3 ✅, Std: 29.7 ✅ (sample std)
- NVE: 0.06× ✅

#### Control
- Paper: 244.8 ± 12.7
- ❓ Cannot verify — CSV says "RUNNING" at time of computation. No metrics.jsonl on current server.
- NVE: ≤0.1× — paper value, cannot verify

---

## Summary of Issues

### Math Errors

| Row | Field | Paper Value | Correct Value | Type |
|-----|-------|-------------|---------------|------|
| Cheetah Trigger | Std | ±33.9 | ±47.9 | Pop std used instead of sample std |

### Inconsistencies with Complete Results Table

| Row | Issue |
|-----|-------|
| Walker Baseline | Seeds s3 (869.03) and s4 (922.80) not documented in Table 4 (appendix) |
| Cheetah Baseline | Uses exp_023 series (593.9) vs. complete table exp_077/083 (446.1) — ~148 point gap |
| Walker Trigger CIVO count | "8/8" not supported by any data source (should be 5/5 or 6/6) |

### Inconsistencies within Table 5

| Issue | Details |
|-------|---------|
| Mixed std type | Cheetah trigger uses pop std; all others use sample std |
| Mixed seed counts | Walker trigger: eval N=3 but NVE N=5. Cheetah trigger: eval N=2 but complete table has 3 seeds |
| Cheetah NVE exclusion | exp_010b_s0 (NVE=108.52) excluded without footnote |

### New Data Not Incorporated

| Experiment | Config | Eval@105K | Status |
|------------|--------|-----------|--------|
| exp_097_cheetah_008d_s3 | Cheetah trigger s3 | 61.67 | Verified from metrics.jsonl |
| exp_092_cheetah_no_dt_emb_s1 | Cheetah control s1 | 77.26 | Verified from metrics.jsonl |
| exp_093_cheetah_no_dt_emb_s2 | Cheetah control s2 | 151.18 | Verified from metrics.jsonl |

---

## Recommended Corrected Table

### Option A: Minimal fix (use existing seeds, fix math only)

Keep current seed selections but fix std and CIVO count:

| Environment | Configuration | Eval Return | NVE Peak | CIVO |
|-------------|---------------|-------------|----------|------|
| Walker Walk | Baseline (dt=1) | 787.7 ± 230.8 | — | — |
| Walker Walk | Trigger (trained dt_emb) | 140.6 ± 111.5 | 4.72× | ✓ (5/5) |
| Walker Walk | Control (no dt_emb) | 302.4 ± 134.8 | 1.69×* | ✗ (0/4) |
| Cheetah Run | Baseline (dt=1) | 593.9 ± 60.4 | — | — |
| Cheetah Run | Trigger (trained dt_emb) | 85.6 ± **47.9** | 8.27× | ✓ (2/2) |
| Cheetah Run | Control (no dt_emb) | 86.9 ± 13.6 | 0.20× | ✗ (0/2) |
| Cartpole | Baseline (dt=1) | 673.3 ± 142.0 | — | — |
| Cartpole | Trigger (trained dt_emb) | 236.3 ± 29.7 | 0.06× | ✗ (0/3) |
| Cartpole | Control (no dt_emb) | 244.8 ± 12.7 | ≤0.1× | ✗ (0/3) |

Changes: Cheetah trigger std 33.9→47.9; Walker CIVO 8/8→5/5.

### Option B: Full reconciliation with complete results table

Use ONLY experiments documented in Table 4 (appendix):

| Environment | Configuration | Eval Return | Seeds | NVE Peak | CIVO |
|-------------|---------------|-------------|-------|----------|------|
| Walker Walk | Baseline (dt=1) | 679.6 ± 333.9 | 2 | — | — |
| Walker Walk | Trigger (trained dt_emb) | 136.2 ± 99.8¹ | 5 | 4.72× | ✓ (5/5) |
| Walker Walk | Control (no dt_emb) | 302.4 ± 134.8 | 4 | 1.69×* | ✗ (0/4) |
| Cheetah Run | Baseline (dt=1) | 446.1 ± 2.9 | 2 | — | — |
| Cheetah Run | Trigger (trained dt_emb) | 85.6 ± 47.9² | 2 | 8.27× | ✓ (2/2) |
| Cheetah Run | Control (no dt_emb) | 86.9 ± 13.6 | 2 | 0.20× | ✗ (0/2) |
| Cartpole | Baseline (dt=1) | 673.3 ± 142.0 | 3 | — | — |
| Cartpole | Trigger (trained dt_emb) | 236.3 ± 29.7 | 3 | 0.06× | ✗ (0/3) |
| Cartpole | Control (no dt_emb) | 244.8 ± 12.7 | 3 | ≤0.1× | ✗ (0/3) |

¹ Using @105K evals from complete table: 009b=267.9, 008d_s3=268, 008d_s4=63.6, 059=95.8, 068=39.1 (excluding 008d which only ran to 55K). Mean=146.9, Std=109.7.
² Excluding exp_010b_s0 (eval=0.83, NVE=108.52) — requires explicit footnote if excluded.

**Major concern with Option B:** Walker baseline drops to 679.6±333.9 (2 seeds, huge std). Cheetah baseline drops to 446.1±2.9 (2 seeds, very tight). Both look weaker statistically.

### Option C: Include new experiments (recommended)

Keep cross-env specific baselines, add new seeds, fix all std to sample:

| Environment | Configuration | Eval Return | Seeds | NVE Peak | CIVO |
|-------------|---------------|-------------|-------|----------|------|
| Walker Walk | Baseline (dt=1) | 787.7 ± 230.8 | 4 | — | — |
| Walker Walk | Trigger (trained dt_emb) | 140.6 ± 111.5 | 3 | 4.72× | ✓ (5/5) |
| Walker Walk | Control (no dt_emb) | 302.4 ± 134.8 | 4 | 1.69×* | ✗ (0/4) |
| Cheetah Run | Baseline (dt=1) | 593.9 ± 60.4 | 5 | — | — |
| Cheetah Run | Trigger (trained dt_emb) | 77.6 ± 36.6³ | 3 | 8.27× | ✓ (3/3) |
| Cheetah Run | Control (no dt_emb) | 100.6 ± 34.9⁴ | 4 | — | ✗ (0/4) |
| Cartpole | Baseline (dt=1) | 673.3 ± 142.0 | 3 | — | — |
| Cartpole | Trigger (trained dt_emb) | 236.3 ± 29.7 | 3 | 0.06× | ✗ (0/3) |
| Cartpole | Control (no dt_emb) | 244.8 ± 12.7 | 3 | ≤0.1× | ✗ (0/3) |

³ Adds exp_097 (s3=61.67): (51.7+119.5+61.67)/3 = 77.6, sample_std=36.6
⁴ Adds exp_092 (s1=77.26) + exp_093 (s2=151.18): (96.5+77.3+77.26+151.18)/4 = 100.6, sample_std=34.9

**Note:** Cheetah baseline (593.9) remains inconsistent with complete table (446.1). This should be resolved by either:
(a) Adding exp_023 seeds to the complete table, or
(b) Rerunning cross-env trigger/control with exp_077/083 as reference baseline.

---

## Appendix: Per-Experiment Raw Values (verified from metrics.jsonl)

### Experiments verified from server metrics.jsonl

| Experiment | Eval@105K | Peak VE (raw, 35K+) | Verified |
|------------|-----------|---------------------|----------|
| exp_walker_008f_s0 | 139.54 | 0.996 @105K | ✅ |
| exp_walker_no_dt_emb_s1 | 468.83 | 0.522 @95K | ✅ |
| exp_100_walker_008a_s1 | 750.59 | — | ✅ |
| exp_097_cheetah_008d_s3 | 61.67 | 2.265 @45K | ✅ |
| exp_092_cheetah_no_dt_emb_s1 | 77.26 | 0.703 @55K | ✅ |
| exp_093_cheetah_no_dt_emb_s2 | 151.18 | 0.541 @95K | ✅ |
| exp_cheetah_008a_s0 | 366.19 | — | ✅ |
| exp_cheetah_008a_s1 | 281.24 | — | ✅ |

### Experiments verified from paper_data_walker_walk.json

| Experiment | Eval@105K | Peak VE (raw, 35K+) | Config |
|------------|-----------|---------------------|--------|
| exp_001_baseline | 915.67 | 0.728 | Baseline s1 |
| exp_008d_subsample_on_h8 | 82.75 @55K | 1.666 | Trigger s1 (only to 55K) |
| exp_009b_008d_walker_s2 | 267.93 | 0.570 | Trigger s2 |
| exp_008f_no_dt_embed_subsample_on_h8 | 503.21 | 0.454 | Control s0 (PRE-correction) |
| exp_009c_008f_walker_s2 | 148.34 | 0.750 | Control s2 |
| exp_008a_no_subsample_dt2 | 777.66 | 0.536 | Unexposed emb s0 |
