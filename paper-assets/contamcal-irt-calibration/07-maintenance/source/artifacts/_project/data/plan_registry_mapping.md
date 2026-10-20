# Experiment Plan → Registry ID Mapping

Generated: 2026-05-15

## Summary

| plan_id | current registry_id | recommended registry_id | status | conclusion |
|---------|---------------------|------------------------|--------|------------|
| exp-001 | exp_001_sft_d100_15B_v2 | exp_001_sft_injection | DONE | success |
| exp-002 | (none) | exp_002_signals_05B | DONE | success |
| exp-003 | (none) | exp_003_rrf_05B | DONE | success |
| exp-004 | exp_004_sim_sweep | exp_004_sim_sweep_v7 | RUNNING | — |
| exp-005 | exp_005_noise_prop_v2 | exp_005_noise_prop_v4 | DONE | negative |
| exp-006 | (none) | exp_006_irt_05B_gsm8k | DONE | success |
| exp-007 | (none) | (none) | — | not started |
| exp-008 | (none) | exp_008_signal_survival_v4 | DONE | success |
| exp-009 | (none) | (none) | — | not started |
| exp-012 | (none) | (none) | — | not started |
| exp-013 | (none) | (none) | — | not started |
| exp-014 | (none) | (none) | — | not started |
| exp-015 | exp_001_sft_d100_qc_only | (none) | — | planned |

### Changes needed

- **exp-001**: `exp_001_sft_d100_15B_v2` → `exp_001_sft_injection` (original umbrella entry, DONE/success)
- **exp-002**: (none) → `exp_002_signals_05B` (NEW)
- **exp-003**: (none) → `exp_003_rrf_05B` (NEW)
- **exp-004**: `exp_004_sim_sweep` (failed) → `exp_004_sim_sweep_v7` (RUNNING, latest attempt)
- **exp-005**: `exp_005_noise_prop_v2` (failed) → `exp_005_noise_prop_v4` (DONE/negative — valid result)
- **exp-006**: (none) → `exp_006_irt_05B_gsm8k` (NEW)
- **exp-008**: (none) → `exp_008_signal_survival_v4` (NEW)

---

## Detailed Breakdown by Plan Entry

### exp-001: controlled_sft_injection (Claim 1, P0)

Multi-run experiment: 3 models × 5 dosages × 3 seeds = 45 SFT runs + corresponding evals.

**Recommended primary registry_id**: `exp_001_sft_injection` (DONE/success, created 2026-05-13)

#### SFT Runs — Successful (seed=42)

| model | d000 | d005 | d025 | d100 |
|-------|------|------|------|------|
| 0.5B | exp_001_sft_0pct_05B ✓ | exp_001_sft_d005_05B_v3 ✓ | exp_001_sft_d025_05B_v3 ✓ | exp_001_sft_d100_05B ✓ |
| 1.5B | exp_001_sft_0pct_15B ✓ | exp_001_sft_d005_15B ✓ | exp_001_sft_d025_15B ✓ | exp_001_sft_d100_15B_v2 ✓ |
| 3B   | exp_001_sft_3B_d000_v2 ✓ | exp_001_sft_d005_3B ✓ | exp_001_sft_d025_3B_v2 ✓ (α=16) | exp_001_sft_d100_3B ✓ |

Note: 3B d025/d100 s42 α=32 reruns in progress (exp_001_sft_d025_3B_v3 RUNNING, exp_001_sft_3B_d100_s42_a32_v2 RUNNING). d050 not in registry (may be dropped from plan).

#### SFT Runs — Successful (seed=123)

| model | d000 | d005 | d025 | d100 |
|-------|------|------|------|------|
| 0.5B | exp_001_sft_0pct_05B_s123 ✓ | exp_001_sft_05B_d005_s123 ✓ | exp_001_sft_05B_d025_s123_v2 ✓ | exp_001_sft_05B_d100_s123 ✓ |
| 1.5B | exp_001_sft_0pct_15B_s123 ✓ | exp_001_sft_15B_d005_s123_v2 ✓ | exp_001_sft_15B_d025_s123_v2 ✓ | exp_001_sft_15B_d100_s123 ✓ |
| 3B   | exp_001_sft_3B_d000_s123 ✓ | exp_001_sft_3B_d005_s123 ✓ | exp_001_sft_3B_d025_s123 ✓ | exp_001_sft_3B_d100_s123 ✓ |

#### Eval Runs — Successful (seed=42, aligned format)

| model | d000 | d005 | d025 | d100 |
|-------|------|------|------|------|
| 0.5B | exp_001_eval_05B_d000_s42_v5 ✓ | exp_001_eval_05B_d005_aligned ✓ | exp_001_eval_05B_d025_aligned ✓ | exp_001_eval_05B_d100_aligned_v4 ✓ |
| 1.5B | exp_001_eval_15B_d000_s42_v2 ✓ | exp_001_eval_15B_d005_aligned_v2 ✓ | exp_001_eval_15B_d025_aligned ✓ | exp_001_eval_15B_d100_aligned ✓ |
| 3B   | exp_001_eval_3B_d000_v2_aligned ✓ | exp_001_eval_3B_d005_aligned ✓ | exp_001_eval_3B_d025_v2_aligned ✓ | exp_001_eval_3B_d100_v2_aligned_v2 ✓ |

#### Eval Runs — Successful (seed=42, para_aligned format)

| model | d000 | d005 | d025 | d100 |
|-------|------|------|------|------|
| 0.5B | — | exp_001_eval_05B_d005_para_aligned ✓ | exp_001_eval_05B_d025_aligned_v2 ✓ | — |
| 1.5B | — | — | exp_001_eval_15B_d025_para_aligned ✓ | — |
| 3B   | exp_001_eval_3B_d000_v2_para_aligned_v2 ✓ | — | exp_001_eval_3B_d025_v2_para_aligned ✓ | exp_001_eval_3B_d100_v2_para_aligned ✓ |

#### Eval Runs — Successful (seed=123, aligned)

| model | d000 | d005 | d025 | d100 |
|-------|------|------|------|------|
| 0.5B | exp_001_eval_05B_d000_s123_aligned ✓ | exp_001_eval_05B_d005_s123_aligned ✓ | exp_001_eval_05B_d025_s123_aligned ✓ | exp_001_eval_05B_d100_s123_aligned ✓ |
| 1.5B | exp_001_eval_15B_d000_s123_aligned ✓ | exp_001_eval_15B_d005_s123 ✓ / _v2 ✓ | exp_001_eval_15B_d025_s123 ✓ / _v2 ✓ | exp_001_eval_15B_d100_s123_aligned ✓ |
| 3B   | exp_001_eval_3B_d000_v2_s123_aligned ✓ | exp_001_eval_3B_d005_s123_aligned ✓ | exp_001_eval_3B_d025_s123_aligned ✓ | exp_001_eval_3B_d100_v2_s123_aligned ✓ |

#### Eval Runs — Successful (seed=123, para_aligned)

| model | d000 | d005 | d025 | d100 |
|-------|------|------|------|------|
| 0.5B | — | exp_001_eval_05B_d005_s123_para_aligned ✓ | — | — |
| 1.5B | — | — | — | — |
| 3B   | exp_001_eval_3B_d000_v2_s123_para_aligned ✓ | exp_001_eval_3B_d005_s123_para_aligned ✓ | exp_001_eval_3B_d025_s123_para_aligned ✓ | (exp_001_eval_3B_d100_s123_para_aligned_v2 ANALYZING) |

#### In-Progress / Pending exp-001 entries

- exp_001_sft_d025_3B_v3 — RUNNING (3B d025 s42 α=32)
- exp_001_sft_3B_d100_s42_a32_v2 — RUNNING (3B d100 s42 α=32)
- exp_001_sft_3B_d100_s123_a32_v2 — RUNNING (3B d100 s123 α=32)
- exp_001_sft_3B_d000_v3 — DONE/failed (3B d000 s42 α=32)
- exp_001_eval_3B_d100_s123_para_aligned_v2 — ANALYZING
- exp_001_eval_3B_d005_s42_para_aligned — PREPARING (waiting GPU)

---

### exp-002: stage1_signal_pipeline (Claim 2, P0)

**Recommended registry_id**: `exp_002_signals_05B`

| scale | registry_id | status |
|-------|-------------|--------|
| 0.5B  | exp_002_signals_05B | DONE/success |
| 1.5B  | exp002-signals-1p5B | DONE/success |
| 3B    | exp_002_signals_3B_v4 | RUNNING |
| 0.5B d025 | exp002-signal-d025-05B | DONE/success |

---

### exp-003: rrf_aggregation_ablation (Claim 2, P0)

**Recommended registry_id**: `exp_003_rrf_05B`

| registry_id | status |
|-------------|--------|
| exp_003_rrf_05B | DONE/success |
| exp_003_mmlu_item_aligned_gap | PREPARING/success |

---

### exp-004: simulation_identifiability_sweep (Claim 1+3, P0)

**Recommended registry_id**: `exp_004_sim_sweep_v7` (RUNNING — all prior versions failed)

| registry_id | status | notes |
|-------------|--------|-------|
| exp_004_sim_sweep | DONE/failed | v1 |
| exp_004_sim_sweep_v2 | DONE/failed | |
| exp_004_sim_sweep_v3 | DONE/failed | /tmp full |
| exp_004_sim_sweep_v4 | DONE/failed | resume mode |
| exp_004_sim_sweep_v5 | DONE/failed | continuation of v4 |
| exp_004_sim_sweep_v6 | DONE/killed | |
| exp_004_sim_sweep_v7 | RUNNING | latest attempt |

Precursor MVPs (not the full sweep but validated concept):
- mvp_sim_4pl_gamma — DONE/success
- mvp_sim_confounding — DONE/success

---

### exp-005: noise_propagation_analysis (Claim 3, P0)

**Recommended registry_id**: `exp_005_noise_prop_v4` (DONE/negative — valid completed result)

| registry_id | status |
|-------------|--------|
| exp_005_noise_prop | DONE/failed |
| exp_005_noise_prop_v2 | DONE/failed |
| exp_005_noise_prop_v3 | DONE/failed |
| exp_005_noise_prop_v4 | DONE/negative |

---

### exp-006: irt_calibration_and_baselines (Claim 1+3, P0)

**Recommended registry_id**: `exp_006_irt_05B_gsm8k` (DONE/success — first successful per-benchmark IRT)

#### Per-benchmark IRT fits
| registry_id | status | benchmark |
|-------------|--------|-----------|
| exp_006_irt_05B_gsm8k | DONE/success | GSM8K |
| exp_006_irt_05B_arc | DONE/success | ARC |

#### Pooled IRT fits
| registry_id | status | notes |
|-------------|--------|-------|
| exp006-pooled-s1only-gsm8k-v2 | DONE/success | S1-only GSM8K |
| exp006-pooled-s1only-arc | DONE/success | S1-only ARC |
| exp006-pooled-05B-15B-arc-v2 | DONE/success | Cross-scale ARC |
| exp006-pooled-05B-15B-gsm8k-v2 | DONE/negative | Cross-scale GSM8K |
| exp006-oracle-gsm8k-extended-v2 | DONE/success | Oracle GSM8K |
| exp006-oracle-arc-2pl | DONE/success | 2PL+γ ARC |
| exp006-s1only-gsm8k-2pl | DONE/success | 2PL+γ GSM8K S1-only |

#### Failed/incomplete
| registry_id | status |
|-------------|--------|
| exp_006_irt_05B | DONE/killed |
| exp_006_irt_05B_v1 | DONE/failed |
| exp_006_pooled_gsm8k_v1 | DONE/failed |
| exp006-oracle-gsm8k-extended | DONE/failed |
| exp006-oracle-arc-4pl-pooled | DONE/failed |
| exp006-pooled-05B-15B-mmlu-v2 | DONE/failed |

---

### exp-008: signal_survival_analysis (Claim 2, P0)

**Recommended registry_id**: `exp_008_signal_survival_v4` (DONE/success)

| registry_id | status | notes |
|-------------|--------|-------|
| exp_008_signal_survival | DONE/success | Initial version |
| exp_008_signal_survival_v4 | DONE/success | D021 fixes, latest |
| exp_008_base_pretrained_eval_v2 | DONE/success | 0.5B base eval |
| exp_008_base_pretrained_15B_eval | DONE/success | 1.5B base eval |
| exp_008_base_pretrained_15B_eval_v2 | DONE/success | 1.5B base eval v2 |
| exp_008_instruct_05B_eval | DONE/success | 0.5B Instruct eval |
| exp_008_instruct_rl_proxy | PREPARING | RL proxy, not submitted |

---

### exp-007, exp-009, exp-012, exp-013, exp-014, exp-015: No matching successful registry entries

These plan entries have no completed experiments in the registry.

---

## Coverage Impact

After updating registry_ids:

- **Claim 1** (exp-001 ✓, exp-004 ~running, exp-006 ✓): 2/3 P0 experiments have success entries → coverage should increase significantly from 14%
- **Claim 2** (exp-002 ✓, exp-003 ✓, exp-008 ✓): 3/3 P0 experiments have success entries → coverage should jump from 0% to near-complete
- **Claim 3** (exp-004 ~running, exp-005 ✓/negative, exp-006 ✓): 2/3 have completed results → coverage should jump from 0%
