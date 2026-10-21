# Data Provenance Audit Report

**Date**: 2026-05-23
**Scope**: All numerical data points in experiments.tex and appendix.tex
**Method**: Registry cross-reference + server log verification + statistical recalculation

---

## Summary

| Category | Count | Details |
|----------|-------|---------|
| ✅ Fully traceable | 28 | Registry + log confirmed |
| ⚠️ Partially traceable | 11 | Registry exists but log missing, or minor issues |
| ❌ Not traceable / Mismatch | 8 | No source, value mismatch, or misattribution |

---

## CRITICAL ISSUES (❌)

### 1. seed8 OOD: Paper 13.43% vs Registry 11.94%

- **Paper**: Table 2, seed8 step 5, OOD 13.43% (18/134)
- **Registry**: `exp029_seed8_ood_precollapse` → `ood_success_rate=0.1194` (16/134 = 11.94%)
- **Concern**: 13.43% (18/134) matches EXACTLY the registry value for `exp029_seed7_high_kl_step7_ood` (seed7 high-KL step 7). Possible misattribution of seed7 result to seed8.
- **Impact**: Table 2 row for seed8 may report the wrong experiment's result.

### 2. seed2048 OOD 8.21%: No eval record exists

- **Paper**: Table 2, seed2048 step 5, OOD 8.21% (11/134)
- **Registry**: `exp029_new_seed_2048` shows collapse at step 1, no OOD eval registered.
- **Concern**: 8.21% (11/134) matches the registry value for `exp029_seed7_high_kl_step5_ood_v2` (seed7 high-KL step 5). Config file exists at westd backup but no log or result. Possible misattribution of seed7 high-KL result to seed2048.
- **Impact**: Table 2 row for seed2048 may report a different experiment's result.

### 3. seed42 OOD 12.69%: No eval record exists

- **Paper**: Table 2, seed42 step 5, OOD 12.69% (17/134)
- **Registry**: `exp029_seed42_episode` has no OOD eval. Config exists at westd backup but no log.
- **Concern**: 12.69% (17/134) is the same value as seed100 step 10 (`exp029_seed100_step10_ood_eval`). Could be coincidence (both 17/134) but cannot verify without log.
- **Impact**: Table 2 row for seed42 is unverifiable.

### 4. seed5 OOD 25.37%: Three conflicting values, source log not found

- **Paper**: Table 2, seed5 step 10, OOD 25.37% (34/134)
- **Registry**:
  - `exp029_seed5_ood_eval` (westd): 29.10% (39/134)
  - `exp029_seed5_step10_ood` (bjb1): 37.31% (50/134)
  - `exp029_seed5_response_mask_check` (PREPARING, never completed): hypothesis text references "baseline 25.37% with mask=false"
- **Server log**: bjb1 log confirms 37.31%, westd log confirms 29.10%. No log produces 25.37%.
- **Decision D123**: Flagged as "Eval 可复现性危机" — same checkpoint yields 29.10%/37.31%/17.3% across three evals.
- **Impact**: The reported 25.37% has no supporting log or completed registry record.

### 5. seed2 OOD 15.67%: Checkpoint lost, no eval completed

- **Paper**: Table 2, seed2 step 15, OOD 15.67% (21/134)
- **Registry**: `exp029_seed2_ood_step15` status=PREPARING, conclusion=killed, metrics={}. Notes: "全部 seed2 checkpoint 已丢失（M019）。Director 确认取消。"
- **Server log**: bjb1 log shows FileNotFoundError for the checkpoint. westd server inaccessible.
- **Impact**: The 15.67% value may have been obtained on westd before checkpoint loss, but no log survives.

### 6. Theoretical claim: 5.1% at p=5% is arithmetically wrong

- **Paper**: theoretical_analysis.tex line 31: "at p=5%, only 5.1% of updates are correct"
- **Formula**: P(correct|update) = p / [1 - (1-p)^K]
- **At p=0.05, K=8**: 0.05 / [1 - 0.95^8] = 0.05 / 0.3366 = **14.85%**, not 5.1%
- **At large-K limit**: P → p = 5.0%, not 5.1%
- **Note**: The p=50% claim (50.2%) in the same sentence is correct at K=8.
- **Impact**: Arithmetic error in theoretical section.

### 7. Window sweep "OOD" labels for h=10, h=20 are actually ID val results

- **Paper**: experiments.tex line 56: "h=10: 6.25%, h=20: 15.6%" labeled as "OOD success"
- **Registry**: `hsweep_h20_seed1` notes explicitly: "只需 step 5 val 数据做 cliff figure (in-dist val success vs h-value), 不需要 checkpoint, 不做 h=20 OOD eval。"
- **Server logs**: h-sweep training configs all use `val: env_groups: 32, tags: ["AlfworldSG"]` (in-distribution, 32 tasks). No OOD eval (134 tasks) was run for h=5, h=10, or h=20.
- **Values**: h=20: 15.625% = 5/32 (ID); h=10: 6.25% = 2/32 (ID, or SFT baseline on subset)
- **Impact**: Paper labels in-distribution validation results as "OOD success" in Figure 2(b) and the text.

### 8. Fisher exact test seed2: p=0.02 vs computed p=0.032

- **Paper**: Table 2, seed2 vs SFT: "p=0.02"
- **Computed**: Two-sided Fisher exact test on [[21, 113], [9, 125]] gives p=0.0317
- **Note**: p=0.02 matches chi-squared without Yates correction (p=0.0201) or one-sided Fisher (p=0.0158). The test used is inconsistent with the other seeds.
- **Impact**: seed2 classification as "borderline" (p=0.02 near α=0.01) depends on which test was used.

---

## MODERATE ISSUES (⚠️)

### 9. Wilson CI rounding: seed4, seed5, seed6

Three seeds have CIs that cannot be reproduced by any consistent rounding convention:

| Seed | Computed | Reported | Max error |
|------|----------|----------|-----------|
| seed4 | [23.43, 38.85] | [23.5, 38.7] | 0.15pp |
| seed5 | [18.76, 33.36] | [18.8, 33.3] | 0.06pp |
| seed6 | [22.08, 37.29] | [22.2, 37.1] | 0.19pp |

Not material to conclusions but indicates inconsistent computation pipeline.

### 10. Cell B 18.75% ID: Not in registry

- **Paper**: Table 1, Cell B In-Dist 18.75%
- **Registry**: `factorial_h2_episodeadv_seed1` records only OOD metrics (5.97% at step 5). No ID eval stored.
- **Likely source**: RAGEN built-in validation on 32 ID tasks during training (6/32 = 18.75%), not separately recorded.
- **Status**: Plausible but not directly verifiable from registry.

### 11. |A_correct|/|A_wrong| ≈ 1.32: No registry record

- **Paper**: theoretical_analysis.tex line 40: "Empirical measurement from training logs confirms approximately comparable per-group advantage magnitudes (|A_correct|/|A_wrong| ≈ 1.32)"
- **Registry**: `hsweep_h2_seed2` has `adv_analysis` with sign_outcome_agreement=0.5207, point_biserial_r=0.068, but no magnitude ratio.
- **Note**: This is an advantage magnitude ratio (not frequency), computed offline from training logs. 52.07/47.93 = 1.086 (frequency ratio), not 1.32.
- **Status**: Claimed as empirical but source computation not preserved.

### 12. SFT baseline OOD: Two protocol versions

- **Paper**: 6.72% (9/134)
- **Registry**: `sft_baseline_ood_eval_v2` = 5.97% (seed=42); `ood_eval_sft_baseline_v3` = 6.7% (D134 protocol, seed=321)
- **Note**: 9/134 = 6.716...% → 6.72%. Matches v3 (D134 protocol). v2 used different eval protocol.
- **Status**: Traceable to v3, but v2 gives a different value — protocol sensitivity noted.

### 13. seed6 OOD: Minor westd/bjb1 discrepancy

- **Paper**: 29.10% (39/134) — uses westd value
- **bjb1 reproducibility run**: 29.85% (40/134)
- **Status**: 1 task difference at T=0.4 is within stochastic variance. Not a provenance concern.

### 14. h=5 sweep: 0% OOD with no dedicated eval

- **Paper**: h=5: 0% labeled as OOD
- **Registry**: No `hsweep_h5_seed1` entry. Gamma sweep at h=5 (`gsweep_g095_h5_seed1`) shows 0% val on ID tasks.
- **Status**: Consistent (collapsed model = 0% everywhere) but no OOD-specific eval exists.

---

## CONFIRMED DATA POINTS (✅)

### Table 1: Main Results

| Data Point | Paper Value | Source | Verification |
|-----------|------------|--------|--------------|
| SFT baseline ID | 12.50% | val_step0 across multiple seeds (4/32) | ✅ Multiple seeds confirm |
| SFT baseline OOD | 6.72% | `ood_eval_sft_baseline_v3` (9/134, D134 protocol) | ✅ 9/134 = 6.716% → 6.72% |
| Cell A ID | 0% | `hsweep_h2_seed1`: val 0% all steps | ✅ |
| Cell A OOD | 0% | `hsweep_h2_seed1`: collapsed to 0% | ✅ |
| Cell B OOD | 5.97% | `factorial_h2_episodeadv_seed1`: best OOD step 5 = 5.97% | ✅ |
| Cell D OOD mean | 17.16% | (23.88% + 10.45%) / 2 = 17.165% → 17.16% | ✅ Arithmetic verified |
| Cell D ID mean | 34.38% | (28.125% + 40.625%) / 2 = 34.375% → 34.38% | ✅ Arithmetic verified |
| Cell D OOD range | 10.4-23.9 | `exp029_seed3_ood_v2`: 10.45%; `exp029_episode_level`: 23.88% | ✅ |
| Cell D ID range | 28.1-40.6 | 28.125% and 40.625% (9/32 and 13/32) | ✅ |
| Dense reward | 0% | `exp013f`: success 0% throughout, action_valid 60%→97.5% | ✅ |
| REINFORCE++ | 12.50% | `gae_baseline_seed1`: val step5=12.5% | ✅ |

### Table 2: 11-Seed Evaluation (confirmed seeds)

| Seed | Paper OOD% | Source exp_id | Registry value | Status |
|------|-----------|---------------|---------------|--------|
| seed1 | 23.88% | `exp029_episode_level` reeval | 23.88% (32/134) | ✅ Server log confirmed |
| seed200 | 10.45% | `exp029_seed200_step5_ood_eval` | 10.45% (14/134) | ✅ Server log confirmed |
| seed300 | 10.45% | `exp029_seed300_step5_ood_eval_v4` | 10.45% (14/134) | ✅ |
| seed100 s5 | 11.19% | `exp029_seed100_step5_ood_eval` | 11.19% (15/134) | ✅ |
| seed100 s10 | 12.69% | `exp029_seed100_step10_ood_eval` | 12.69% (17/134) | ✅ |
| seed4 | 30.60% | `exp029_seed4_ood_eval_v2` | 30.6% (41/134) | ✅ |
| seed6 | 29.10% | `exp029_seed6_ood_eval_v2` (westd) | 29.10% (39/134) | ✅ |

### Table 3: 8B Results

| Data Point | Paper Value | Source | Status |
|-----------|------------|--------|--------|
| SFT ID | 68.75% | `8b_det_eval_full`: 68.75% (22/32, T=0) | ✅ |
| SFT OOD | 80.60% | `7b_sft_eval_ood`: 80.6% (108/134) | ✅ |
| SFT h=2 | 31.25% | `8b_det_eval_h2`: 31.25% (10/32, T=0) | ✅ |
| Cell A | 28.1→1.5% | `7b_cell_a_h2`: val_before_train=28.1%, step2=1.56% | ✅ |
| Cell D ID | 96.88% | `8b_cell_c_episode_v9d`: val step10=96.875% | ✅ |
| Cell D OOD | 90.30% | `8b_v9d_ood_eval_v5`: 90.3% (121/134) | ✅ |
| Info loss gap | 37.5pp | 68.75% - 31.25% = 37.5pp | ✅ |

### Section 4.4: Sign Verification

| Data Point | Paper Value | Source | Status |
|-----------|------------|--------|--------|
| Credit agreement | 52.07% | `hsweep_h2_seed2`: sign_outcome_agreement=0.5207 | ✅ |
| n=3000 | 3000 | `hsweep_h2_seed2`: adv_log_lines=3000 | ✅ |
| 95% CI [50.3%, 53.9%] | [50.3%, 53.9%] | Wilson CI on k=1562, n=3000: [50.28%, 53.85%] | ✅ Exact match |
| point biserial r | 0.068 | `hsweep_h2_seed2`: point_biserial_r=0.068 | ✅ |
| r>0.99 (episode outcome) | r>0.99 | Not independently verified (requires raw data) | ⚠️ |

### ScienceWorld

| Data Point | Paper Value | Source | Status |
|-----------|------------|--------|--------|
| SFT baseline | 30.1% | `scienceworld_sft_eval_v2`: 30.1% (540/1796) | ✅ |
| SFT T=0 | 34.8% | `sw_info_loss_bjb1`: full_context_success=34.8% | ✅ |
| Cell A | 0% | `scienceworld_grpo_cell_a`: 0% throughout | ✅ |
| h=2 SFT | 4.5% | `sw_info_loss_bjb1`: h2_success=4.5% | ✅ |
| M1 gap | 30.3pp | 34.8% - 4.5% = 30.3pp | ✅ |

### Statistical Tests (Wilson CI)

All 11 Wilson CIs verified within ±0.2pp. 8/11 match exactly under standard rounding. 3/11 (seed4, seed5, seed6) have minor inconsistencies (see ⚠️ #9).

### Statistical Tests (Fisher exact)

10/11 Fisher exact test results confirmed:
- seed1, seed5, seed6, seed4: p<0.001 ✅
- seed2048, seed42, seed8, seed200, seed300, seed100: NS at α=0.01 ✅
- seed2: p=0.02 reported, p=0.032 computed (see ❌ #8)

### Miscellaneous Arithmetic

| Claim | Verification | Status |
|-------|-------------|--------|
| seed100 improvement 1.50pp | 12.69 - 11.19 = 1.50 | ✅ |
| 3/11 collapsed (27%) | 3/11 = 27.27% | ✅ |
| 4/11 stagnant (36%) | 4/11 = 36.36% | ✅ |
| 4/11 generalized (36%) | 4/11 = 36.36% | ✅ |
| Prop 2: 19.1% at p=12.5%, K=8 | 0.125/0.656 = 19.05% → 19.1% | ✅ |
| (1-p)^K = 34.4% | 0.875^8 = 34.36% → 34.4% | ✅ |
| p^K < 10^-7 | 0.125^8 = 5.96e-8 | ✅ |

---

## DATA POINT INVENTORY

### Fully Traceable (28)
SFT baseline ID, SFT baseline OOD, Cell A ID/OOD, Cell B OOD, Cell D OOD mean, Cell D ID mean, Cell D ranges (4 values), Dense reward, REINFORCE++, seed1/seed200/seed300/seed100(s5)/seed100(s10)/seed4/seed6 OOD, 8B SFT ID/OOD/h=2, 8B Cell A, 8B Cell D ID/OOD, ScienceWorld SFT/Cell A/h=2/gap, Credit agreement + CI

### Partially Traceable (11)
Cell B ID 18.75%, h=2 OOD 0%, h=5 OOD 0%, SFT OOD protocol variants, seed6 westd/bjb1 gap, r>0.99, |A_correct|/|A_wrong|≈1.32, p=0.025 sign test, Wilson CI rounding (3 seeds)

### Not Traceable / Mismatch (8)
seed8 13.43% (registry: 11.94%), seed2048 8.21% (no eval), seed42 12.69% (no eval), seed5 25.37% (3 conflicting values), seed2 15.67% (checkpoint lost), 5.1% theoretical error, h=10/h=20 labeled OOD but are ID, Fisher seed2 p-value

---

## RECOMMENDATIONS

1. **Immediate**: Verify seed8/seed2048/seed42 values by checking if westd-47453 server can be accessed and if eval logs survive there.
2. **Immediate**: Fix 5.1% → 14.85% in theoretical_analysis.tex (arithmetic error).
3. **Immediate**: Relabel h=10/h=20 values as "In-Dist" or run actual OOD evals for these checkpoints.
4. **High priority**: Resolve seed5 value (25.37% vs 29.10% vs 37.31%) — determine which eval protocol is canonical and re-run if needed.
5. **Medium**: Clarify Fisher test method for seed2 (two-sided vs one-sided vs chi-squared).
6. **Medium**: Re-run or document the |A_correct|/|A_wrong| ≈ 1.32 computation with a reproducible script.
7. **Low**: Standardize Wilson CI rounding convention.
