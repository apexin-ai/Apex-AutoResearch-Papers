# R28 Data Consistency Report: Registry ↔ Paper Cross-Verification

**Date:** 2026-05-24
**Scope:** All quantitative claims in paper (tables, inline prose, appendices) vs. registry experiments

---

## Summary

| Category | Count |
|----------|-------|
| Total data points checked | ~284 |
| ✅ Match (within rounding tolerance) | 237 |
| ❌ Mismatch (value differs from registry) | 8 |
| ⚠️ Not found / unverifiable from registry | 31 |
| ~  Minor rounding (std off by 0.01-0.1) | 8 |

---

## Critical Mismatches (❌)

### 1. Table 2 — KL 50% global row (4 of 5 metrics)

Paper claims PPL 11.84±0.15, ARC-c 36.3±3.2, WG 63.8±0.3, GSM8K 2.7±1.3.

**No single combination of 3 registry experiments reproduces these values.**

| Metric | Paper | Best registry combo | Source exp_ids |
|--------|-------|-------------------|----------------|
| PPL | 11.84±0.15 | 11.84±0.07 | bench_kl50_global(11.79) + mvp_kl_norm_v2_s123(11.91) + kl50_s456_global_eval(11.81) |
| ARC-c | 36.3±3.2 | 35.1±3.5 | bench_kl50_global(32.85) + kl50_global_s123_downstream_v2(39.16) + kl50_s456_global_eval(33.19) |
| WG | 63.8±0.3 | 64.1±0.7 | same combo |
| MMLU | 28.3±0.7 | 28.3±0.7 | ✅ matches |
| GSM8K | 2.7±1.3 | 2.3±1.1 | same combo |

**Root cause:** The paper cites `bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval` but:
- `kl50_global_s123_downstream_v2` has no PPL (only downstream metrics)
- `kl50_global_s456_eval` does not exist in registry (correct key: `kl50_s456_global_eval`)
- PPL and downstream metrics appear to come from different eval runs for the same seeds, mixed inconsistently

### 2. C4 control table (tab:c4_control) — WikiText row HS/PIQA

| Metric | C4 control table | OOD downstream table | Registry (kl30_uniform_hellaswag_piqa_v2) |
|--------|-----------------|---------------------|------------------------------------------|
| HS | 69.4 | 70.9 | 70.85 |
| PIQA | 75.5 | 74.8 | 74.81 |

**Internal inconsistency:** Two tables in the same paper report different HS/PIQA values for the same WikiText-trained KL 30% uniform predictor (s42). The OOD downstream table matches the registry; the C4 control table does not. Source of 69.4/75.5 is untraced.

### 3. C4 control table — C4 row PIQA

Paper=74.86, registry (`c4_kl30_s42_eval`)=75.03. Off by **0.17pp**.

### 4. Extended downstream table (tab:downstream) — TEAL 30% uniform PIQA

Paper=72.80, registry (`teal_30pct_uniform_multiseed_eval`)=71.98. Off by **0.82pp**. Registry stores `piqa` (likely raw acc) rather than `piqa_acc_norm`; possible metric variant confusion.

### 5. Experiments prose — "148× vs. 112× compression" for Qwen14B

Paper claims Qwen-2.5-14B has d_ff/d_b = 148× (implying d_ff=18,944). Registry shows `trainable_params='117M (0.793%)'` for `qwen14b_kl30_s123`. Back-computing:

- 117M / 48 layers = 2.44M per layer
- 2.44M = (5120×128) + (128×d_ff) → d_ff ≈ 13,923
- 13,923 / 128 ≈ **109×**, not 148×
- LLaMA's 112× (14336/128) is correct

The 148× claim is inconsistent with the registered trainable parameter count.

---

## Data Provenance Issues (⚠️ — unverifiable from registry)

### Table 2

| Row | Missing | Notes |
|-----|---------|-------|
| BCE 30% global | All 5 metrics | `bce30_teal_global` absent from registry entirely |
| TEAL 30% uniform ARC-c | acc_norm variant | Registry stores `arc_challenge`=37.71 (acc), not acc_norm; paper=39.33 plausible but unverified |
| TEAL 50% uniform | ARC-c, WG, MMLU | No full downstream eval registered for TEAL 50% uniform |

### Ablation Table (Table 4)

| Row | Missing | Notes |
|-----|---------|-------|
| JSD 50% | PPL 12.54 | `jsd_ablation_s42` absent from registry |
| Reverse KL 50% | PPL 12.80 | `reverse_kl_ablation_s42` absent |
| Per-layer KL K=1 50% | PPL 34.85 | `perlayer_kl_50_s42` absent |
| Per-layer KL K=4 30%/50% | Both PPL values | Experiments registered but metrics empty |
| BCE + STE 50% | PPL 60.54 | `bce_ste_s42` absent |

All Δ_50 arithmetic is internally consistent (computed correctly from the stated 50% values).

### Qwen-2.5-14B Table

| Row | Missing | Notes |
|-----|---------|-------|
| BCE global | ARC-c, WG, MMLU, GSM8K | `qwen14b_bce30_s42_eval` absent |
| TEAL uniform | PPL, ARC-c, WG, MMLU | No 4-task eval registered for TEAL 30% uniform |
| KL uniform GSM8K | s123 value | Only s42 (35.71%) and s456 (26.08%) in registry; 2-seed mean=30.9±6.8, paper claims 32.0±5.2 (implies unregistered s123≈34.2%) |

### K-curve Table

| Row | Missing | Notes |
|-----|---------|-------|
| K=4 | PPL (s123, s456), all downstream (s123, s456) | Only s42 downstream in registry |

### Other

- **Constraint experiments** (`constraint_protect_late`, `constraint_remove_valley`): Not in registry. Paper claims MMLU +3.4pp, GSM8K +1.6pp from removing valley — unverifiable.
- **Extended downstream** — KL 30% uniform HS/PIQA: Only s42 registered; 3-seed mean (71.07±0.54 / 74.95±0.25) unverifiable.
- **Extended downstream** — TEAL 50% uniform HS/PIQA: `bench_teal50_uniform_6task` absent.

---

## Minor Rounding Discrepancies (~)

All means match; only std values differ by 0.01-0.1 due to rounding of pre-rounded inputs.

| Location | Metric | Paper | Computed | Exact |
|----------|--------|-------|----------|-------|
| Table 2 MSE 30% | PPL std | 1.68 | 1.67 | 1.666 |
| Table 2 MSE 30% | ARC-c std | 4.1 | 4.0 | 4.03 |
| Table 2 MSE 30% | WG std | 2.6 | 2.5 | 2.54 |
| Table 2 KL 50% uniform | PPL std | 0.07 | 0.08 | 0.076 |
| K-curve K=8 | ARC-c std | 1.0 | 1.1 | 1.06 |
| K-curve K=16 | MMLU std | 2.9 | 2.8 | 2.77 |
| Mistral KL30 downstream | WG std | 1.2 | 1.1 | 1.14 |
| Table 3 footnote | C1 s42 PPL gap | 0.65pp | 0.63pp | 0.6306 |

---

## Verified Tables (all data points match ✅)

### Table 3 — C1 Target-Swap Ablation
40/40 data points match exactly. All seeds (s42/s123/s456) at 30% and 50% verified.

### Cross-Architecture Table (tab:cross_arch)
All 12 PPL values (6 KL + 6 TEAL across Mistral and LLaMA at 30/50/70%) match exactly.

### Mistral Downstream Table (tab:mistral_downstream)
All 21 values match (dense + KL 3-seed + TEAL single-seed across 7 metrics).

### Latency Table (tab:latency)
All 10 data points match exactly (ms/fwd and tok/s for 5 configurations).

### OOD Table (tab:ood)
All 4 C4 PPL values match. OOD uniform 3-seed (18.22/16.37/16.36, mean 16.98±1.07) match.

### OOD Downstream Table (tab:ood_downstream)
All 12 values match (WikiText and C4 calibration across 6 metrics).

### Dense Baseline
All 5 metrics match exactly (PPL 6.12, ARC-c 58.28, WG 78.06, MMLU 65.27, GSM8K 48.75).

### Appendix Tables
- Bottleneck sensitivity (tab:db_sensitivity): all values match
- Temperature schedule (tab:tau_sensitivity): all values match
- Training convergence (tab:training_convergence): all values match
- Lagrangian dynamics (tab:lagrangian): all values match

---

## Verified Inline Prose Claims

| Claim | Verification | Status |
|-------|-------------|--------|
| "14.5% reduction" (8.81 vs 10.30) | (10.30−8.81)/10.30=14.47%→14.5% | ✅ |
| "MMLU −5.2pp on 8B" | 45.86−40.7=5.16≈5.2 | ✅ |
| "GSM8K −20.1pp on 14B" | 52.1−32.0=20.1 (if 3-seed=32.0) | ✅ (but 32.0 unverified, see above) |
| "7.3× MMLU σ" | 9.5/1.3=7.31 | ✅ |
| "−17.3% Mistral PPL" | (8.38−6.93)/8.38=17.3% | ✅ |
| "MMLU −2.8pp on 14B" | 66.34−63.55=2.79≈2.8 | ✅ (but TEAL MMLU 66.34 unregistered) |
| "6.4% latency overhead" | (126.78−119.11)/119.11=6.44% | ✅ |
| "2.39× worse than KL" | 28.13/11.79=2.386 | ✅ |
| "F1 0.613 vs 0.540" | registry kl_bce_f1_oracle: 0.6128/0.5397 | ✅ |
| "139% worse PPL" | (28.13−11.79)/11.79=138.7%≈139% | ✅ |
| "33.8% STE improvement" | (15.77−11.79)/11.79=33.8% | ✅ |
| "JSD +6.4%, RevKL +8.6%" | (12.54−11.79)/11.79=6.4%, (12.80−11.79)/11.79=8.6% | ✅ |
| "K=16 PPL 8.67±0.02" | registry 3-seed: 8.67±0.02 | ✅ |
| "coupling range 2.08 PPL" | 10.75−8.67=2.08 | ✅ |
| "signal type gap 9.47 PPL" | 18.52−9.05=9.47 | ✅ |
| "Jaccard 68% at 50%" | c1_mask_overlap mean=0.6824 | ✅ |
| "cross-seed Jaccard 36.3%" | appendix consistent | ✅ |
| "75.9M params, <1%" | 32×2.37M=75.84M≈75.9M | ✅ |
| "50% PPL reduction at 50% sparsity" | (23.90−11.92)/23.90=50.1% | ✅ |

---

## Recommendations

### Must-fix before submission

1. **KL 50% global row (Table 2):** Reconcile PPL and downstream metrics with a single consistent set of 3-seed eval runs. Document which exp_ids provide PPL vs downstream for each seed.

2. **C4 control table HS/PIQA (WikiText row):** Values 69.4/75.5 are inconsistent with the OOD downstream table (70.9/74.8) and with registry (70.85/74.81). Use values from registered experiment.

3. **C4 control table PIQA (C4 row):** Paper says 74.86, registry says 75.03. Verify and correct.

4. **148× compression claim:** Back-computation from registered 117M params implies d_ff≈13,923 (109×), not 18,944 (148×). Verify Qwen-2.5-14B's actual intermediate_size and correct.

### Should-fix

5. **Qwen14B GSM8K (32.0±5.2):** Register the s123 GSM8K evaluation to make this claim verifiable. Current 2-seed data gives 30.9±6.8.

6. **Extended downstream TEAL 30% uniform PIQA:** Verify whether paper uses acc_norm (72.80) while registry stored acc (71.98).

7. **BCE 30% global row (Table 2):** Register the source experiment or add exp_id comment.

### Nice-to-have

8. Register missing ablation experiments (JSD 50%, RevKL 50%, perlayer KL 50%, BCE+STE 50%, K=4 metrics).
9. Standardize registry metric key names (e.g. `arc_challenge` vs `arc_challenge_acc_norm`).
10. Minor std rounding: adopt consistent rounding convention (round exact, not round pre-rounded).
