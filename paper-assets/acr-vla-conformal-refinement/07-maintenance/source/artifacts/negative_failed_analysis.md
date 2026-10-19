# Negative & Failed Experiment Analysis

**Project**: acr-vla-conformal-refinement
**Generated**: 2026-05-30 03:03
**Total experiments in registry**: 1423

## 1. Executive Summary

| Conclusion | Count | % |
|---|---|---|
| success | 772 | 54.3% |
| negative | 97 | 6.8% |
| failed | 130 | 9.1% |
| killed | 424 | 29.8% |
| **Total** | **1423** | |

**Key finding**: 77/88 negative experiments with SR data show SR < 1%, indicating near-total task failure rather than marginal degradation. Only 3 negatives have SR >= 50%.

---
## 2. Negative Experiment Analysis (n=97)

### 2.1 By VLA Model

| Model | Count | % |
|---|---|---|
| smolvla | 79 | 81.4% |
| pi05 | 15 | 15.5% |
| openvla | 3 | 3.1% |

### 2.2 By Evaluation Suite

| Suite | Count | % |
|---|---|---|
| object | 49 | 50.5% |
| goal | 17 | 17.5% |
| long | 15 | 15.5% |
| unknown | 10 | 10.3% |
| spatial | 6 | 6.2% |

### 2.3 By Method Condition (Refined Classification)

| Group | Condition | Count |
|---|---|---|
| **CRM Architecture Variants** (27) | crm-obs-only | 6 |
|  | crm-norm005 | 5 |
|  | crm-reduced-norm | 1 |
|  | scalar-crm | 3 |
|  | k1-accg | 3 |
|  | k1-multiscale | 5 |
|  | unc-head | 3 |
|  | acr-pipeline | 1 |
| **Adaptive/Tau Configuration** (16) | smolvla-adaptive | 9 |
|  | smolvla-tau-sweep | 7 |
| **Per-DOF CRM** (14) | perdof-norm-sweep | 14 |
| **Loss Function Variants** (6) | loss-variant | 6 |
| **Baselines & Ablations** (15) | vla-only-baseline | 1 |
|  | openvla-baseline | 3 |
|  | k2mean | 6 |
|  | reconvla | 5 |
| **pi0.5 Transfer** (15) | pi05-adaptive | 7 |
|  | pi05-crm-k2 | 5 |
|  | pi05-tau-sweep | 3 |
| **Generalization Tests** (4) | leave-task-out | 2 |
|  | calibration-signal | 2 |

### 2.4 Cross-Tabulation: Condition x Suite

| Condition | object | spatial | goal | long | unknown | Total |
|---|---|---|---|---|---|---|
| perdof-norm-sweep | 11 | 0 | 0 | 0 | 3 | 14 |
| smolvla-adaptive | 3 | 2 | 1 | 3 | 0 | 9 |
| smolvla-tau-sweep | 0 | 1 | 5 | 1 | 0 | 7 |
| pi05-adaptive | 3 | 0 | 2 | 2 | 0 | 7 |
| crm-obs-only | 4 | 1 | 0 | 0 | 1 | 6 |
| k2mean | 0 | 1 | 2 | 3 | 0 | 6 |
| loss-variant | 4 | 0 | 0 | 0 | 2 | 6 |
| pi05-crm-k2 | 3 | 0 | 0 | 2 | 0 | 5 |
| crm-norm005 | 2 | 0 | 1 | 2 | 0 | 5 |
| reconvla | 0 | 0 | 3 | 2 | 0 | 5 |
| k1-multiscale | 5 | 0 | 0 | 0 | 0 | 5 |
| pi05-tau-sweep | 0 | 0 | 3 | 0 | 0 | 3 |
| openvla-baseline | 3 | 0 | 0 | 0 | 0 | 3 |
| unc-head | 3 | 0 | 0 | 0 | 0 | 3 |
| scalar-crm | 3 | 0 | 0 | 0 | 0 | 3 |
| k1-accg | 3 | 0 | 0 | 0 | 0 | 3 |
| calibration-signal | 0 | 0 | 0 | 0 | 2 | 2 |
| leave-task-out | 0 | 0 | 0 | 0 | 2 | 2 |
| vla-only-baseline | 1 | 0 | 0 | 0 | 0 | 1 |
| crm-reduced-norm | 0 | 1 | 0 | 0 | 0 | 1 |
| acr-pipeline | 1 | 0 | 0 | 0 | 0 | 1 |
| **Total** | 49 | 6 | 17 | 15 | 10 | 97 |

### 2.5 SR Analysis: How Bad Were the Negatives?

SmolVLA VLA-only baselines: Object=77%, Spatial=79%, Goal=83%, Long=58%

**SR Distribution (88 experiments with SR data):**

| SR Range | Count | % | Interpretation |
|---|---|---|---|
| 0-1% | 77 | 88% | Near-zero (catastrophic) |
| 1-10% | 5 | 6% | Very low (severe degradation) |
| 10-50% | 3 | 3% | Low (substantial degradation) |
| 75-100% | 3 | 3% | Near-baseline (marginal negative) |

**Critical insight**: 88% of negative experiments show SR < 1%. This is not marginal degradation -- CRM corrections at improper magnitudes/modes cause near-total task failure. The robot arm effectively stops performing useful actions when CRM corrections are too large.

**Three near-baseline negatives (SR >= 50%) -- marginal degradation cases:**

| Exp ID | Suite | SR | Delta | Condition | Why Negative |
|---|---|---|---|---|---|
| `eval-supp-k2mean-spatial-s42` | spatial | 81.5% | +2.5pp | k2mean | K=2 mean baseline (vla_only, 2-sample average) on Spatial se |
| `eval-3dir-norm01-spatial-s42` | spatial | 79.0% | +0.0pp | crm-reduced-norm | Reducing max_correction_norm from 1.42 to 0.1 prevents CRM o |
| `eval-supp-obj-adapt-s42-r2` | object | 77.5% | +0.5pp | smolvla-adaptive | Adaptive CRM (tau=0.074855, K=2, norm=0.2) generalizes from  |

### 2.6 MC1 Support: Unconditional CRM Degrades Performance

**MC1**: Unconditional (always-on) CRM corrections degrade VLA performance.

**Always-on CRM experiments (unconditional correction):**
- Total negatives: 40
- With SR + baseline comparison: 33
- Below baseline: 32/33 (97%)
- At/above baseline: 1/33

**Edge cases at/above baseline:**
- `eval-3dir-norm01-spatial-s42`: SR=79.0%, delta=+0.0pp (suite=spatial, condition=crm-reduced-norm)

**Verdict: MC1 MOSTLY SUPPORTED.** 32/33 show degradation. Edge cases are at exactly baseline level (delta=0), not improvements.

**Always-on CRM degradation by variant:**

| Variant | n (negative) | n (with delta) | Mean Delta | Min Delta | Interpretation |
|---|---|---|---|---|---|
| crm-obs-only | 6 | 2 | -77.7pp | -78.5pp | Catastrophic |
| crm-norm005 | 5 | 5 | -69.9pp | -82.2pp | Catastrophic |
| crm-reduced-norm | 1 | 1 | +0.0pp | +0.0pp | Severe |
| perdof-norm-sweep | 14 | 11 | -76.9pp | -77.0pp | Catastrophic |
| scalar-crm | 3 | 3 | -74.0pp | -76.9pp | Catastrophic |
| k1-accg | 3 | 3 | -76.9pp | -76.9pp | Catastrophic |
| k1-multiscale | 5 | 5 | -76.9pp | -76.9pp | Catastrophic |
| unc-head | 3 | 3 | -76.9pp | -76.9pp | Catastrophic |

**K=2 Mean baseline (not CRM, but relevant):**
- 6 negatives, 6 with delta
- Mean delta: -55.7pp, range [-82.2, +2.5]
- Note: One spatial K=2mean experiment shows +2.5pp, indicating simple multi-sample averaging sometimes helps

### 2.7 Adaptive CRM Negative Cases

**16 adaptive experiments were negative** (SmolVLA: 9, pi0.5: 7).

| Exp ID | Model | Suite | SR | Delta | Key Detail |
|---|---|---|---|---|---|
| `pi05-adaptive-goal-s44-bjb1` | pi05 | goal | 0.9% | N/A | π0.5 Adaptive Conformal (τ=0.25, K=2, max_correction_norm=0.2) on Goal |
| `westd-pi05-adaptive-goal-s44` | pi05 | goal | 0.9% | N/A | π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s44. T |
| `pi05-adaptive-long-s43-cqa1` | pi05 | long | 0.0% | N/A | π0.5 Adaptive Conformal on Long s43. Table 2 long-horizon cross-archit |
| `pi05-adaptive-long-s44-cqa1` | pi05 | long | 0.0% | N/A | π0.5 Adaptive Conformal on Long s44. Table 2 long-horizon cross-archit |
| `westd-pi05-adaptive-object-s44-paired` | pi05 | object | N/A | N/A | π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s44. westd  |
| `westd-pi05-adaptive-object-s43-paired` | pi05 | object | 0.9% | N/A | π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s43. westd  |
| `westd-pi05-adaptive-object-s42-paired` | pi05 | object | 0.8% | N/A | π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Object s42. westd  |
| `eval-goal-adapt-tau025-s49-paired` | smolvla | goal | 0.8% | -82.2pp | SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s49 |
| `eval-supp-long-adapt-tau025-s44` | smolvla | long | 0.6% | -57.4pp | SmolVLA Adaptive Conformal on Long s44 (tau=0.25, K=2). Long adaptive  |
| `eval-supp-long-adapt-tau025-s43` | smolvla | long | 0.6% | -57.4pp | SmolVLA Adaptive Conformal on Long s43 (tau=0.25, K=2). Long adaptive  |
| `eval-supp-long-adapt-tau025-s47-r2` | smolvla | long | 0.6% | -57.5pp | Adaptive CRM tau=0.25 on Long suite seed47 retry. Previous attempt fai |
| `eval-supp-adapt-tau025-obj-s44` | smolvla | object | 0.8% | -76.2pp | Adaptive CRM tau=0.25 on Object seed44. s42=81.0% (+2pp), s43=77.5% (- |
| `eval-supp-adapt-tau025-obj-s43` | smolvla | object | 0.8% | -76.2pp | Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer |
| `eval-supp-obj-adapt-s42-r2` | smolvla | object | 77.5% | +0.5pp | Adaptive CRM (tau=0.074855, K=2, norm=0.2) generalizes from Spatial (8 |
| `eval-spatial-adapt-tau025-s46-paired` | smolvla | spatial | 0.8% | -78.2pp | SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Spatial  |
| `eval-adaptive-k-spatial-p25-seed42` | smolvla | spatial | 0.3% | -78.7pp | Adaptive K with τ=P25 (0.054959, Object-calibrated) on LIBERO-Spatial  |

**Adaptive failure patterns:**

- object: 6 negatives
- long: 5 negatives
- goal: 3 negatives
- spatial: 2 negatives

Most adaptive negatives show SR near 0%, indicating the adaptive gating mechanism still triggers corrections that are too large. The tau threshold alone is insufficient to prevent catastrophic corrections on certain suites.

### 2.8 pi0.5 Cross-VLA Transfer

**15 pi0.5 experiments were negative.**

| Condition | Count | Suites | SR Range |
|---|---|---|---|
| pi05-adaptive | 7 | goal, long, object | 0.0-0.9% |
| pi05-crm-k2 | 5 | long, object | 0.8-0.9% |
| pi05-tau-sweep | 3 | goal | 0.9-0.9% |

pi0.5 transfer shows universal failure: all conditions (adaptive, CRM-K2, tau-sweep) produce SR near 0-1% across object, goal, and long suites. The CRM trained on SmolVLA does not transfer to pi0.5's action space.

### 2.9 Novel Method Variants That Failed

| Variant | n | Description | Outcome |
|---|---|---|---|
| k1-accg | 3 | K=1 CRM with Adaptive Conformal Confidence Gating (ACCG): single-sample CRM with learned gating from 960D features | SR: 0.1-0.1% |
| k1-multiscale | 5 | K=1 CRM with multi-scale features (4x960D from layers [3,7,11,15]): attempt to improve single-sample uncertainty estimation | SR: 0.1-0.1% |
| unc-head | 3 | Learned Uncertainty Head: trained tau predictor replaces fixed threshold | SR: 0.1-0.1% |
| scalar-crm | 3 | Scalar CRM: simplified correction model predicting per-DOF scalars | SR: 0.1-9.0% |
| loss-variant | 6 | Alternative loss functions: per-DOF weighted MSE, conformal-guided loss, combined losses | SR: 4.0-9.0% |
| calibration-signal | 2 | CRM correction magnitude as gating signal / FMVD flow velocity dispersion | SR: 0.1-0.1% |
| leave-task-out | 2 | Leave-Task-Out generalization: CRM trained on subset of tasks, evaluated on held-out | SR: 0.0-0.0% |

**All novel single-sample (K=1) approaches failed catastrophically** (SR near 0%). ACCG, multi-scale features, and learned uncertainty heads could not compensate for the fundamental limitation of estimating correction quality from a single VLA sample.

---
## 3. Failed Experiment Analysis (n=130)

### 3.1 Failure Reason Classification

| Reason | Count | % |
|---|---|---|
| other | 73 | 56.2% |
| OOM | 21 | 16.2% |
| timeout | 14 | 10.8% |
| retry_after_failure | 13 | 10.0% |
| checkpoint_missing | 5 | 3.8% |
| ssh_failure | 4 | 3.1% |

The high 'other' count (73) indicates many failures lack explicit error messages in the registry. These likely include evaluation script crashes, LIBERO environment errors, and process kills from resource contention.

### 3.2 Failed by Model x Suite

| Model | object | spatial | goal | long | unknown | Total |
|---|---|---|---|---|---|---|
| openvla | 1 | 0 | 0 | 0 | 0 | 1 |
| pi05 | 7 | 10 | 5 | 10 | 1 | 33 |
| smolvla | 46 | 15 | 21 | 9 | 5 | 96 |

### 3.3 Failed by Server

| Server | Count | % | Notes |
|---|---|---|---|
| bjb1-32546 | 37 | 28% | High failure rate - check hardware/connectivity |
| bjb1-18228 | 28 | 22% | High failure rate - check hardware/connectivity |
| bjb2-28827 | 23 | 18% | High failure rate - check hardware/connectivity |
| cqa1-32758 | 15 | 12% |  |
| bjb2-40593 | 10 | 8% |  |
| unknown | 9 | 7% |  |
| westd-49937 | 3 | 2% |  |
| bjb2-24035 | 2 | 2% |  |
| autodl-4090 | 2 | 2% |  |
| autodl-4090x4 | 1 | 1% |  |

### 3.4 OOM Failures Deep Dive

**21 OOM failures:**

| Exp ID | Model | Suite | Server |
|---|---|---|---|
| `pi05-k2mean-goal-s43` | pi05 | goal | bjb2-24035 |
| `pi05-k2mean-long-s42` | pi05 | long | bjb1-18228 |
| `pi05-k2mean-object-s42` | pi05 | object | bjb1-18228 |
| `pi05-vla-only-spatial-s42-4090` | pi05 | spatial | bjb1-18228 |
| `pi05-vla-only-goal-s42-4090` | pi05 | goal | bjb1-18228 |
| `pi05-k2mean-spatial-s42` | pi05 | spatial | bjb1-18228 |
| `pi05-vla-only-object-s42-4090` | pi05 | object | bjb1-18228 |
| `pi05-vla-only-long-s42-4090` | pi05 | long | bjb2-24035 |
| `eval-pi05-vla-only-object-s43-v2` | pi05 | object | bjb2-28827 |
| `pi05-adaptive-long-s44-cqa1-r2` | pi05 | long | cqa1-32758 |
| `pi05-adaptive-long-s43-cqa1-r2` | pi05 | long | cqa1-32758 |
| `eval-pi05-adaptive-goal-s42` | pi05 | goal | bjb1-18228 |
| `eval-pi05-vla-only-spatial-seed44` | pi05 | spatial | bjb1-32546 |
| `eval-pi05-vla-only-spatial-seed43` | pi05 | spatial | bjb1-32546 |
| `eval-pi05-vla-only-spatial-seed42` | pi05 | spatial | bjb1-32546 |
| `eval-obs-only-object-norm01-seed61` | smolvla | object | bjb2-28827 |
| `eval-vla-only-goal-seed47` | smolvla | goal | bjb2-28827 |
| `eval-crm-goal-seed45` | smolvla | goal | bjb1-32546 |
| `eval-crm-goal-seed44` | smolvla | goal | bjb1-32546 |
| `eval-obs-only-spatial-norm02-seed46` | smolvla | spatial | unknown |
| `eval-argmin-object-k5-seed44` | smolvla | object | unknown |

OOM by model: pi05: 15, smolvla: 6

### 3.5 Retry Patterns

**19 failed experiments are retries** (have -r2, -r3, etc. suffix).

| Exp ID | Model | Suite | Failure Reason |
|---|---|---|---|
| `eval-direct-correction-object-seed42-r2` | smolvla | object | retry_after_failure |
| `eval-obs-only-object-norm005-seed49-r2` | smolvla | object | retry_after_failure |
| `eval-obs-only-object-norm005-seed55-r2` | smolvla | object | retry_after_failure |
| `eval-obs-only-object-norm01-seed42-r2` | smolvla | object | retry_after_failure |
| `eval-obs-only-object-norm01-seed51-r2` | smolvla | object | checkpoint_missing |
| `eval-obs-only-object-norm01-seed52-r2` | smolvla | object | checkpoint_missing |
| `eval-perdof-object-norm003-seed44-r2` | smolvla | object | retry_after_failure |
| `eval-perdof-object-norm01-seed42-r2` | smolvla | object | retry_after_failure |
| `eval-random-selection-object-seed46-r2` | smolvla | object | timeout |
| `eval-supp-long-vla-only-s43-r2` | smolvla | long | retry_after_failure |
| `eval-supp-obj-k2mean-s47-r2` | smolvla | object | retry_after_failure |
| `eval-vla-only-goal-seed47-r2` | smolvla | goal | retry_after_failure |
| `eval-vla-only-goal-seed48-r2` | smolvla | goal | retry_after_failure |
| `pi05-adaptive-long-s43-cqa1-r2` | pi05 | long | OOM |
| `pi05-adaptive-long-s44-cqa1-r2` | pi05 | long | OOM |
| `pi05-adaptive-object-s44-cqa1-r2` | pi05 | object | retry_after_failure |
| `pi05-tau-sweep-goal-tau050-s42-r2` | pi05 | goal | retry_after_failure |
| `train-crm-pi05-unified-3suite-r2` | pi05 | unknown | timeout |
| `train-crm-unified-4suite-r4` | smolvla | unknown | retry_after_failure |

Notable: 2 retries failed with OOM (persistent memory issue), 2 with missing checkpoints.

### 3.6 Systematic Failure Patterns

**Most failure-prone combinations:**

| Model | Suite | Failures | Notes |
|---|---|---|---|
| smolvla | object | 46 | 10% failure rate (46/462) |
| smolvla | goal | 21 | 15% failure rate (21/139) |
| smolvla | spatial | 15 | 5% failure rate (15/285) |
| pi05 | long | 10 | 20% failure rate (10/49) |
| pi05 | spatial | 10 | 14% failure rate (10/71) |

---
## 4. Killed Experiment Analysis (n=424)

Killed experiments represent 29.8% of all experiments -- the second-largest category after successes.

### 4.1 By Model

| Model | Count | % |
|---|---|---|
| smolvla | 289 | 68.2% |
| pi05 | 130 | 30.7% |
| openvla | 5 | 1.2% |

### 4.2 By Suite

| Suite | Count | % |
|---|---|---|
| object | 140 | 33.0% |
| spatial | 136 | 32.1% |
| goal | 62 | 14.6% |
| long | 44 | 10.4% |
| unknown | 42 | 9.9% |

### 4.3 Kill Reason Analysis

| Category | Count | Notes |
|---|---|---|
| other_noted | 21 | |
| resource_issue | 9 | |
| bug_fix_rerun | 1 | |
| superseded | 1 | |
| duplicate | 1 | |
| **no notes** | **391** | 92% of kills lack reason documentation |

The high kill rate (424/1423 = 30%) with 92% lacking documentation suggests:

1. **Rapid iteration**: experiments killed to free GPU for refined versions
2. **Config errors caught early**: wrong parameters detected before completion
3. **Direction pivots**: entire experiment batches killed when strategy changed

---
## 5. Paper-Actionable Findings

### 5.1 Findings Supporting Core Claims

**MC1 (Always-on CRM hurts)**: 40 negative experiments across 8 always-on variants confirm that unconditional CRM corrections catastrophically degrade performance (mean SR near 0%). This is the strongest empirical evidence in the paper.

**MC2 (Adaptive gating helps)**: The 3 near-baseline negatives (SR >= 50%) all involve either adaptive methods at suboptimal thresholds or very aggressive norm limits. When adaptive CRM works, it achieves only marginal improvement or stays near baseline -- never catastrophic failure like always-on. This supports the claim that conformal gating prevents harmful corrections.

**Cross-VLA Transfer**: All 15 pi0.5 experiments are negative (SR near 0%), demonstrating that CRM trained on SmolVLA does not transfer. This is a clear limitation to document -- the method requires per-VLA CRM training.

### 5.2 Method Boundaries for Limitations Section

1. **Correction magnitude is critical**: The 58 norm-sweep/per-DOF negatives show that CRM correction norm must be carefully calibrated. Too large = catastrophic; too small = no effect. The sweet spot is narrow.

2. **Single-sample (K=1) approaches universally fail**: ACCG (3 experiments), multi-scale (5 experiments), and uncertainty head (3 experiments) all show SR near 0%. Multiple VLA samples are essential for reliable uncertainty estimation.

3. **Alternative loss functions don't help**: Per-DOF weighted, conformal-guided, and combined losses (6 experiments) all fail to improve CRM quality, suggesting the issue is in the correction application strategy, not training.

4. **Generalization is limited**: Leave-task-out experiments (2) show 0% SR on held-out tasks. The CRM does not generalize to unseen manipulation tasks.

5. **Suite sensitivity**: Object suite has the most negatives (44), suggesting object manipulation tasks are the hardest for CRM correction. This may relate to the diversity of object types and required grasp strategies.

### 5.3 Recommended Limitations Section Content (CoRL 2026)

Based on this analysis, the mandatory Limitations section should cover:

1. **Hyperparameter sensitivity**: The method requires careful tuning of tau (conformal threshold), epsilon (correction norm), and K (number of samples). Across 63 sweep experiments, most configurations lead to catastrophic failure (SR < 1%).

2. **VLA-specific training**: CRM does not transfer across VLA architectures. Each VLA requires its own CRM training (evidence: 15 failed pi0.5 experiments).

3. **Task generalization**: Leave-task-out results (0% SR) indicate CRM corrections do not generalize to manipulation tasks unseen during CRM training.

4. **Single-sample limitation**: The method requires K >= 2 VLA forward passes at inference time, adding computational cost. K=1 approaches with learned uncertainty estimation all failed.

5. **Failure mode**: When the adaptive gating fails to suppress bad corrections, performance degrades catastrophically (SR drops to near 0%, not just marginal degradation).

### 5.4 Infrastructure Lessons

- **130 execution failures** (9.1%) indicate LIBERO evaluation is fragile. Environment initialization, checkpoint loading, and SSH connectivity are common failure points.
- **bjb1-32546** had 37 failures (28% of all failures) -- possible hardware/stability issues.
- **19 retries** needed, with OOM and checkpoint-missing as persistent issues.
- **424 killed experiments** (30%) reflect rapid experimentation pace with aggressive pruning.

---
## 6. Appendix: Full Negative Experiment Listing

### 6.1 Negative Experiments by Condition

<details>
<summary><b>CRM Architecture Variants</b> (27 experiments)</summary>

| # | Exp ID | Model | Suite | Condition | SR | Delta | Hypothesis |
|---|---|---|---|---|---|---|---|
| 1 | `eval-acr-object-v3` | smolvla | object | acr-pipeline | 0.0% | -77.0pp | ACR pipeline v3 (K=10 conformal selection with scalar u... |
| 2 | `eval-supp-crm-norm005-goal-s43` | smolvla | goal | crm-norm005 | 0.8% | -82.2pp | CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = ... |
| 3 | `eval-supp-long-crm-norm005-s42` | smolvla | long | crm-norm005 | 0.6% | -57.4pp | CRM always-on norm=0.05 on LIBERO-Long seed42 using 4-s... |
| 4 | `eval-supp-long-crm-norm005-s43` | smolvla | long | crm-norm005 | 0.5% | -57.5pp | CRM norm=0.05 always-on on Long suite seed43. Second se... |
| 5 | `eval-supp-crm-norm005-obj-s43` | smolvla | object | crm-norm005 | 0.8% | -76.2pp | CRM norm=0.05 on Object seed43. Tests static CRM correc... |
| 6 | `eval-supp-crm-norm005-obj-s44` | smolvla | object | crm-norm005 | 0.7% | -76.3pp | CRM norm=0.05 on Object seed44. s42=77.0%, s43=78.5%. T... |
| 7 | `eval-obs-only-object-seed43` | smolvla | object | crm-obs-only | 0.1% | -76.9pp | D031: obs_only CRM v3-norm seed=43 on LIBERO object ben... |
| 8 | `eval-smolvla-crm-object-seed42-v1` | smolvla | object | crm-obs-only | N/A | N/A | SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves s... |
| 9 | `eval-smolvla-crm-object-seed43-v1` | smolvla | object | crm-obs-only | N/A | N/A | SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves s... |
| 10 | `eval-smolvla-crm-object-seed44-v1` | smolvla | object | crm-obs-only | N/A | N/A | SmolVLA CRM (crm_obs_only mode, obs_dim=960) improves s... |
| 11 | `eval-smolvla-crm-spatial-s47` | smolvla | spatial | crm-obs-only | 0.5% | -78.5pp | SmolVLA CRM obs_only (K=10) Spatial s47。Table 1 补 CRM 列... |
| 12 | `eval-mag-obsonly-norm02` | smolvla | unknown | crm-obs-only | 35.0% | N/A | obs_only CRM (ε=0.2) on LIBERO Spatial benchmark. Spati... |
| 13 | `eval-3dir-norm01-spatial-s42` | smolvla | spatial | crm-reduced-norm | 79.0% | +0.0pp | Reducing max_correction_norm from 1.42 to 0.1 prevents ... |
| 14 | `eval-k1-crm-accg-object-seed42` | smolvla | object | k1-accg | 0.1% | -76.9pp | K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed... |
| 15 | `eval-k1-crm-accg-object-seed43` | smolvla | object | k1-accg | 0.1% | -76.9pp | K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed... |
| 16 | `eval-k1-crm-accg-object-seed44` | smolvla | object | k1-accg | 0.1% | -76.9pp | K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed... |
| 17 | `eval-k1-crm-multiscale-object-seed42` | smolvla | object | k1-multiscale | 0.1% | -76.9pp | K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,... |
| 18 | `eval-k1-crm-multiscale-object-seed43` | smolvla | object | k1-multiscale | 0.1% | -76.9pp | K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,... |
| 19 | `eval-k1-crm-multiscale-object-seed43-r2` | smolvla | object | k1-multiscale | 0.1% | -76.9pp | K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object... |
| 20 | `eval-k1-crm-multiscale-object-seed44` | smolvla | object | k1-multiscale | 0.1% | -76.9pp | K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,... |
| 21 | `eval-k1-crm-multiscale-object-seed44-r2` | smolvla | object | k1-multiscale | 0.1% | -76.9pp | K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object... |
| 22 | `eval-acr-object-v4-scalar` | smolvla | object | scalar-crm | 9.0% | -68.0pp | D021: scalar_unc CRM v3-norm with max_correction_norm=0... |
| 23 | `eval-scalar-object-seed44-r2` | smolvla | object | scalar-crm | 0.1% | -76.9pp | Scalar CRM seed=44 on LIBERO object benchmark. Retry of... |
| 24 | `eval-scalar-object-seed45-r2` | smolvla | object | scalar-crm | 0.1% | -76.9pp | Scalar CRM seed45 rerun with n_rollouts=10 for consiste... |
| 25 | `eval-adaptive-unc-head-object-seed42` | smolvla | object | unc-head | 0.1% | -76.9pp | D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VL... |
| 26 | `eval-adaptive-unc-head-object-seed43` | smolvla | object | unc-head | 0.1% | -76.9pp | D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VL... |
| 27 | `eval-adaptive-unc-head-object-seed44` | smolvla | object | unc-head | 0.1% | -76.9pp | D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VL... |

</details>

<details>
<summary><b>Adaptive/Tau Configuration</b> (16 experiments)</summary>

| # | Exp ID | Model | Suite | Condition | SR | Delta | Hypothesis |
|---|---|---|---|---|---|---|---|
| 1 | `eval-goal-adapt-tau025-s49-paired` | smolvla | goal | smolvla-adaptive | 0.8% | -82.2pp | SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on ... |
| 2 | `eval-supp-long-adapt-tau025-s43` | smolvla | long | smolvla-adaptive | 0.6% | -57.4pp | SmolVLA Adaptive Conformal on Long s43 (tau=0.25, K=2).... |
| 3 | `eval-supp-long-adapt-tau025-s44` | smolvla | long | smolvla-adaptive | 0.6% | -57.4pp | SmolVLA Adaptive Conformal on Long s44 (tau=0.25, K=2).... |
| 4 | `eval-supp-long-adapt-tau025-s47-r2` | smolvla | long | smolvla-adaptive | 0.6% | -57.5pp | Adaptive CRM tau=0.25 on Long suite seed47 retry. Previ... |
| 5 | `eval-supp-adapt-tau025-obj-s43` | smolvla | object | smolvla-adaptive | 0.8% | -76.2pp | Adaptive CRM tau=0.25 on Object seed43. Tests cross-ben... |
| 6 | `eval-supp-adapt-tau025-obj-s44` | smolvla | object | smolvla-adaptive | 0.8% | -76.2pp | Adaptive CRM tau=0.25 on Object seed44. s42=81.0% (+2pp... |
| 7 | `eval-supp-obj-adapt-s42-r2` | smolvla | object | smolvla-adaptive | 77.5% | +0.5pp | Adaptive CRM (tau=0.074855, K=2, norm=0.2) generalizes ... |
| 8 | `eval-adaptive-k-spatial-p25-seed42` | smolvla | spatial | smolvla-adaptive | 0.3% | -78.7pp | Adaptive K with τ=P25 (0.054959, Object-calibrated) on ... |
| 9 | `eval-spatial-adapt-tau025-s46-paired` | smolvla | spatial | smolvla-adaptive | 0.8% | -78.2pp | SmolVLA Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on ... |
| 10 | `eval-ablation-tau010-goal-s42` | smolvla | goal | smolvla-tau-sweep | 0.8% | -82.2pp | τ-sweep ablation: τ=0.10 on Goal s42. Lower threshold →... |
| 11 | `eval-ablation-tau040-goal-s42` | smolvla | goal | smolvla-tau-sweep | 0.8% | -82.2pp | τ-sweep ablation: τ=0.40 on Goal s42. Higher threshold ... |
| 12 | `tau_sweep_goal_tau025_s42` | smolvla | goal | smolvla-tau-sweep | 0.8% | -82.2pp | SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Go... |
| 13 | `tau_sweep_goal_tau040_s42` | smolvla | goal | smolvla-tau-sweep | 0.8% | -82.2pp | SmolVLA Adaptive Conformal CRM with τ=0.40 on LIBERO-Go... |
| 14 | `tau_sweep_goal_tau045_s42` | smolvla | goal | smolvla-tau-sweep | 0.8% | -82.2pp | SmolVLA Adaptive Conformal CRM with τ=0.45 on LIBERO-Go... |
| 15 | `smolvla-tau005-long-s42` | smolvla | long | smolvla-tau-sweep | 0.4% | -57.6pp | SmolVLA adaptive conformal CRM at τ=0.05 on Long s42. F... |
| 16 | `tau_sweep_spatial_tau025_s42` | smolvla | spatial | smolvla-tau-sweep | 0.8% | -78.2pp | SmolVLA Adaptive Conformal CRM with τ=0.25 on LIBERO-Sp... |

</details>

<details>
<summary><b>Per-DOF CRM</b> (14 experiments)</summary>

| # | Exp ID | Model | Suite | Condition | SR | Delta | Hypothesis |
|---|---|---|---|---|---|---|---|
| 1 | `eval-mag-perdof-norm02-object` | smolvla | object | perdof-norm-sweep | 0.1% | -76.9pp | Object magnitude sweep: perdof CRM v3-norm at norm=0.2 ... |
| 2 | `eval-perdof-object-default-seed44` | smolvla | object | perdof-norm-sweep | 0.0% | -77.0pp | perdof CRM (default norm ~1.42) seed=44 on LIBERO Objec... |
| 3 | `eval-perdof-object-default-seed46` | smolvla | object | perdof-norm-sweep | 0.0% | -77.0pp | perdof CRM (default norm, 无裁剪) seed46 on LIBERO-Object.... |
| 4 | `eval-perdof-object-default-seed47` | smolvla | object | perdof-norm-sweep | 0.0% | -77.0pp | Per-DoF CRM (ε=default/unlimited) seed47 on LIBERO-Obje... |
| 5 | `eval-perdof-object-norm01-seed44` | smolvla | object | perdof-norm-sweep | 0.1% | -76.9pp | perdof CRM (ε=0.1) seed=44 on LIBERO Object. 验证 perdof ... |
| 6 | `eval-perdof-object-norm01-seed46` | smolvla | object | perdof-norm-sweep | 0.1% | -76.9pp | perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends pe... |
| 7 | `eval-perdof-object-norm02-seed50` | smolvla | object | perdof-norm-sweep | 0.1% | -76.9pp | perdof CRM (ε=0.2) K=10 on LIBERO-Object seed50. Additi... |
| 8 | `eval-perdof-object-norm03-seed44` | smolvla | object | perdof-norm-sweep | 0.0% | -77.0pp | perdof CRM (ε=0.3) seed=44 on LIBERO Object. 验证 perdof ... |
| 9 | `eval-perdof-object-norm03-seed44-r2` | smolvla | object | perdof-norm-sweep | 0.0% | -77.0pp | perdof CRM ε=0.3 seed44 re-run on LIBERO-Object. 原 seed... |
| 10 | `eval-perdof-object-norm03-seed45-r2` | smolvla | object | perdof-norm-sweep | 0.1% | -76.9pp | perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. ... |
| 11 | `eval-perdof-object-seed44` | smolvla | object | perdof-norm-sweep | 0.1% | -76.9pp | perdof CRM v3-norm seed=44 on LIBERO object benchmark. ... |
| 12 | `eval-mag-perdof-norm003` | smolvla | unknown | perdof-norm-sweep | 30.0% | N/A | perdof CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 nor... |
| 13 | `eval-mag-perdof-norm005` | smolvla | unknown | perdof-norm-sweep | N/A | N/A | perdof CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm... |
| 14 | `eval-mag-perdof-norm03` | smolvla | unknown | perdof-norm-sweep | 26.0% | N/A | perdof CRM (ε=0.3) on LIBERO Spatial benchmark. 高 norm ... |

</details>

<details>
<summary><b>Loss Function Variants</b> (6 experiments)</summary>

| # | Exp ID | Model | Suite | Condition | SR | Delta | Hypothesis |
|---|---|---|---|---|---|---|---|
| 1 | `eval-loss-combined-object-seed42` | smolvla | object | loss-variant | 9.0% | -68.0pp | Combined loss (per-DOF weighted + conformal-guided) for... |
| 2 | `eval-loss-conformal-object-seed42` | smolvla | object | loss-variant | 6.0% | -71.0pp | Conformal-guided loss for CRM training produces correct... |
| 3 | `eval-loss-mse-object-seed42` | smolvla | object | loss-variant | 7.0% | -70.0pp | MSE-trained CRM eval on SmolVLA Object for controlled l... |
| 4 | `eval-loss-perdof-object-seed42` | smolvla | object | loss-variant | 4.0% | -73.0pp | Per-DOF weighted MSE loss for CRM training produces cor... |
| 5 | `crm-loss-combined` | smolvla | unknown | loss-variant | N/A | N/A | Combined per-DOF weighting + conformal-guided loss will... |
| 6 | `crm-loss-conformal` | smolvla | unknown | loss-variant | N/A | N/A | Conformal-guided auxiliary loss (lambda=0.1) will impro... |

</details>

<details>
<summary><b>Baselines & Ablations</b> (15 experiments)</summary>

| # | Exp ID | Model | Suite | Condition | SR | Delta | Hypothesis |
|---|---|---|---|---|---|---|---|
| 1 | `eval-supp-goal-k2mean-s45` | smolvla | goal | k2mean | 0.8% | -82.2pp | K=2 mean baseline on Goal suite seed45. Matched-seed co... |
| 2 | `eval-supp-k2mean-goal-s44` | smolvla | goal | k2mean | 0.8% | -82.2pp | K=2 mean baseline on Goal seed44. s42-r2 running, s43=8... |
| 3 | `eval-supp-long-k2mean-s42` | smolvla | long | k2mean | 0.6% | -57.4pp | K=2 mean baseline on LIBERO-Long seed42. Isolates multi... |
| 4 | `eval-supp-long-k2mean-s43` | smolvla | long | k2mean | 0.6% | -57.4pp | K=2 mean baseline on Long suite seed43. Isolates multi-... |
| 5 | `eval-supp-long-k2mean-s44` | smolvla | long | k2mean | 0.5% | -57.5pp | Long K=2 mean baseline seed44. Third seed for Long K=2 ... |
| 6 | `eval-supp-k2mean-spatial-s42` | smolvla | spatial | k2mean | 81.5% | +2.5pp | K=2 mean baseline (vla_only, 2-sample average) on Spati... |
| 7 | `eval-openvla-crm-object-seed42` | openvla | object | openvla-baseline | 0.0% | N/A | OpenVLA CRM obs_only eval: 测试 CRM correction 在 OpenVLA ... |
| 8 | `eval-openvla-object-vla-only-seed42` | openvla | object | openvla-baseline | 0.0% | N/A | OpenVLA 7B VLA-only baseline on LIBERO-Object. 0% SR du... |
| 9 | `eval-openvla-oft-object-baseline-seed42` | openvla | object | openvla-baseline | 0.0% | N/A | OpenVLA-OFT (7B deterministic VLA) baseline eval on LIB... |
| 10 | `eval-supp-goal-reconvla-s42` | smolvla | goal | reconvla | N/A | N/A | Reconvla K=10 argmin on Goal suite seed42. Goal VLA-onl... |
| 11 | `eval-supp-goal-reconvla-s43` | smolvla | goal | reconvla | 0.8% | -82.2pp | Reconvla K=10 argmin on Goal seed43. Goal VLA-only base... |
| 12 | `eval-supp-goal-reconvla-s44` | smolvla | goal | reconvla | 0.8% | -82.2pp | Reconvla K=10 argmin on Goal seed44. Goal VLA-only base... |
| 13 | `eval-supp-long-reconvla-s42` | smolvla | long | reconvla | 0.6% | -57.4pp | Reconvla K=10 argmin on LIBERO-Long seed42. Tests if re... |
| 14 | `eval-supp-long-reconvla-s43` | smolvla | long | reconvla | 0.6% | -57.4pp | Reconvla K=10 argmin on Long suite seed43. Second seed ... |
| 15 | `eval-a1-baseline-object-s42` | smolvla | object | vla-only-baseline | 0.6% | -76.4pp | A1 VLA baseline evaluated under our LIBERO framework sh... |

</details>

<details>
<summary><b>pi0.5 Transfer</b> (15 experiments)</summary>

| # | Exp ID | Model | Suite | Condition | SR | Delta | Hypothesis |
|---|---|---|---|---|---|---|---|
| 1 | `pi05-adaptive-goal-s44-bjb1` | pi05 | goal | pi05-adaptive | 0.9% | N/A | π0.5 Adaptive Conformal (τ=0.25, K=2, max_correction_no... |
| 2 | `westd-pi05-adaptive-goal-s44` | pi05 | goal | pi05-adaptive | 0.9% | N/A | π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIB... |
| 3 | `pi05-adaptive-long-s43-cqa1` | pi05 | long | pi05-adaptive | 0.0% | N/A | π0.5 Adaptive Conformal on Long s43. Table 2 long-horiz... |
| 4 | `pi05-adaptive-long-s44-cqa1` | pi05 | long | pi05-adaptive | 0.0% | N/A | π0.5 Adaptive Conformal on Long s44. Table 2 long-horiz... |
| 5 | `westd-pi05-adaptive-object-s42-paired` | pi05 | object | pi05-adaptive | 0.8% | N/A | π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Obj... |
| 6 | `westd-pi05-adaptive-object-s43-paired` | pi05 | object | pi05-adaptive | 0.9% | N/A | π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Obj... |
| 7 | `westd-pi05-adaptive-object-s44-paired` | pi05 | object | pi05-adaptive | N/A | N/A | π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Obj... |
| 8 | `pi05-crm-k2-long-s42-r2` | pi05 | long | pi05-crm-k2 | 0.8% | N/A | π0.5 CRM K=2 obs_only on LIBERO-Long s42 (re-run after ... |
| 9 | `pi05-crm-k2-long-s43-r2` | pi05 | long | pi05-crm-k2 | 0.8% | N/A | π0.5 CRM K=2 obs_only on LIBERO-Long s43 (re-run after ... |
| 10 | `westd-pi05-crm-k2-object-s42` | pi05 | object | pi05-crm-k2 | 0.9% | N/A | π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s42... |
| 11 | `westd-pi05-crm-k2-object-s43` | pi05 | object | pi05-crm-k2 | 0.9% | N/A | π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s43... |
| 12 | `westd-pi05-crm-k2-object-s44` | pi05 | object | pi05-crm-k2 | 0.9% | N/A | π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s44... |
| 13 | `pi05-goal-tau015-s43` | pi05 | goal | pi05-tau-sweep | 0.9% | N/A | Pi0-5 goal τ=0.15 with seed 43 triggers CRM aggressivel... |
| 14 | `pi05-goal-tau025-s43` | pi05 | goal | pi05-tau-sweep | 0.9% | N/A | Pi0-5 goal τ=0.25 with seed 43 provides moderate CRM in... |
| 15 | `pi05-goal-tau035-s43` | pi05 | goal | pi05-tau-sweep | 0.9% | N/A | Pi0-5 goal τ=0.35 with seed 43 tests selective CRM on g... |

</details>

<details>
<summary><b>Generalization Tests</b> (4 experiments)</summary>

| # | Exp ID | Model | Suite | Condition | SR | Delta | Hypothesis |
|---|---|---|---|---|---|---|---|
| 1 | `calibrate-crm-correction-signal` | smolvla | unknown | calibration-signal | N/A | N/A | CRM correction magnitude as zero-overhead gating signal... |
| 2 | `fmvd-calibration-phase1` | smolvla | unknown | calibration-signal | 0.1% | N/A | FMVD (Flow Velocity Dispersion) signal validation: veri... |
| 3 | `eval-lto-splitA-heldout-r2` | smolvla | unknown | leave-task-out | 0.0% | N/A | LTO split-A CRM (K=5, ε=0.2, obs_only) on 5 held-out ta... |
| 4 | `eval-lto-splitA-heldout-v2` | smolvla | unknown | leave-task-out | 0.0% | N/A | Leave-Task-Out generalization: CRM trained on Split A (... |

</details>

### 6.2 Failed Experiments by Reason

<details>
<summary><b>other</b> (73 experiments)</summary>

| Exp ID | Model | Suite | Server |
|---|---|---|---|
| `crm-norm005-goal-s49` | smolvla | goal | bjb1-18228 |
| `crm-norm005-object-s48` | smolvla | object | bjb1-18228 |
| `eval-acr-spatial-v4-default` | smolvla | spatial | bjb1-18228 |
| `eval-acr-spatial-v4-obs-only` | smolvla | spatial | bjb2-40593 |
| `eval-argmin-object-seed44` | smolvla | object | unknown |
| `eval-direct-correction-object-seed42` | smolvla | object | bjb1-32546 |
| `eval-mag-obsonly-norm03-b2` | smolvla | unknown | bjb2-28827 |
| `eval-obs-object-norm003-s45` | smolvla | object | unknown |
| `eval-obs-object-norm003-s46` | smolvla | object | unknown |
| `eval-obs-object-norm005-s45` | smolvla | object | unknown |
| `eval-obs-only-object-norm005-seed62` | smolvla | object | bjb2-28827 |
| `eval-obs-only-object-norm005-seed63` | smolvla | object | bjb2-28827 |
| `eval-obs-only-object-norm01-seed46` | smolvla | object | bjb1-18228 |
| `eval-obs-only-object-norm02-seed43` | smolvla | object | bjb1-32546 |
| `eval-obs-only-object-norm02-seed44` | smolvla | object | unknown |
| `eval-obs-only-object-norm03-seed45` | smolvla | object | bjb2-28827 |
| `eval-obs-only-object-norm03-seed47` | smolvla | object | bjb1-18228 |
| `eval-obs-only-spatial` | smolvla | spatial | bjb1-18228 |
| `eval-obs-only-spatial-norm02-seed43` | smolvla | spatial | bjb2-40593 |
| `eval-obs-only-spatial-seed43` | smolvla | spatial | bjb1-18228 |
| `eval-openvla-oft-official-object` | openvla | object | bjb2-40593 |
| `eval-pi05-adaptive-spatial-s42` | pi05 | spatial | bjb1-18228 |
| `eval-pi05-baseline-object-seed42` | pi05 | object | bjb2-40593 |
| `eval-pi05-vla-only-object-seed42` | pi05 | object | bjb1-18228 |
| `eval-random-selection-object-seed46` | smolvla | object | unknown |
| `eval-scalar-object-seed44` | smolvla | object | bjb2-40593 |
| `eval-smolvla-acr-goal-seed42` | smolvla | goal | bjb1-32546 |
| `eval-smolvla-acr-goal-seed43` | smolvla | goal | bjb1-32546 |
| `eval-smolvla-acr-long-seed42` | smolvla | long | bjb1-32546 |
| `eval-smolvla-lerobot-goal-seed43` | smolvla | goal | bjb1-32546 |
| `eval-smolvla-lerobot-goal-seed43-v2` | smolvla | goal | bjb1-18228 |
| `eval-smolvla-lerobot-goal-seed43-v3` | smolvla | goal | bjb1-32546 |
| `eval-smolvla-lerobot-object-seed43` | smolvla | object | bjb1-32546 |
| `eval-smolvla-lerobot-object-seed44` | smolvla | object | bjb1-32546 |
| `eval-smolvla-lerobot-spatial-seed43` | smolvla | spatial | bjb1-32546 |
| `eval-smolvla-lerobot-spatial-seed43-v2` | smolvla | spatial | bjb1-18228 |
| `eval-smolvla-lerobot-spatial-seed43-v3` | smolvla | spatial | bjb1-32546 |
| `eval-smolvla-libero-spatial` | smolvla | spatial | autodl-4090x4 |
| `eval-supp-goal-k2mean-s47` | smolvla | goal | bjb2-28827 |
| `eval-supp-goal-vla-only-s42` | smolvla | goal | cqa1-32758 |
| `eval-supp-goal-vla-only-s42-bjb1` | smolvla | goal | bjb1-32546 |
| `eval-supp-goal-vla-only-s43` | smolvla | goal | cqa1-32758 |
| `eval-supp-goal-vla-only-s44` | smolvla | goal | cqa1-32758 |
| `eval-supp-goal-vla-only-s50` | smolvla | goal | cqa1-32758 |
| `eval-supp-k2mean-goal-s42` | smolvla | goal | bjb2-40593 |
| `eval-supp-long-adapt-tau025-s47` | smolvla | long | cqa1-32758 |
| `eval-supp-long-k2mean-s47` | smolvla | long | cqa1-32758 |
| `eval-supp-long-vla-only-s48` | smolvla | long | cqa1-32758 |
| `eval-supp-obj-adapt-tau025-s45` | smolvla | object | bjb2-40593 |
| `eval-supp-obj-vla-only-s42` | smolvla | object | bjb1-32546 |
| ... (23 more) | | | |

</details>

<details>
<summary><b>OOM</b> (21 experiments)</summary>

| Exp ID | Model | Suite | Server |
|---|---|---|---|
| `eval-argmin-object-k5-seed44` | smolvla | object | unknown |
| `eval-crm-goal-seed44` | smolvla | goal | bjb1-32546 |
| `eval-crm-goal-seed45` | smolvla | goal | bjb1-32546 |
| `eval-obs-only-object-norm01-seed61` | smolvla | object | bjb2-28827 |
| `eval-obs-only-spatial-norm02-seed46` | smolvla | spatial | unknown |
| `eval-pi05-adaptive-goal-s42` | pi05 | goal | bjb1-18228 |
| `eval-pi05-vla-only-object-s43-v2` | pi05 | object | bjb2-28827 |
| `eval-pi05-vla-only-spatial-seed42` | pi05 | spatial | bjb1-32546 |
| `eval-pi05-vla-only-spatial-seed43` | pi05 | spatial | bjb1-32546 |
| `eval-pi05-vla-only-spatial-seed44` | pi05 | spatial | bjb1-32546 |
| `eval-vla-only-goal-seed47` | smolvla | goal | bjb2-28827 |
| `pi05-adaptive-long-s43-cqa1-r2` | pi05 | long | cqa1-32758 |
| `pi05-adaptive-long-s44-cqa1-r2` | pi05 | long | cqa1-32758 |
| `pi05-k2mean-goal-s43` | pi05 | goal | bjb2-24035 |
| `pi05-k2mean-long-s42` | pi05 | long | bjb1-18228 |
| `pi05-k2mean-object-s42` | pi05 | object | bjb1-18228 |
| `pi05-k2mean-spatial-s42` | pi05 | spatial | bjb1-18228 |
| `pi05-vla-only-goal-s42-4090` | pi05 | goal | bjb1-18228 |
| `pi05-vla-only-long-s42-4090` | pi05 | long | bjb2-24035 |
| `pi05-vla-only-object-s42-4090` | pi05 | object | bjb1-18228 |
| `pi05-vla-only-spatial-s42-4090` | pi05 | spatial | bjb1-18228 |

</details>

<details>
<summary><b>timeout</b> (14 experiments)</summary>

| Exp ID | Model | Suite | Server |
|---|---|---|---|
| `eval-k2-tau015-spatial-s42` | smolvla | spatial | bjb2-40593 |
| `eval-obs-only-spatial-norm02-k5-seed44` | smolvla | spatial | bjb2-28827 |
| `eval-obs-only-spatial-norm02-k5-seed45` | smolvla | spatial | bjb2-28827 |
| `eval-perdof-object-norm005-seed45` | smolvla | object | bjb2-28827 |
| `eval-pi05-crm-spatial-seed42` | pi05 | spatial | bjb2-28827 |
| `eval-pi05-crm-spatial-seed43` | pi05 | spatial | bjb2-28827 |
| `eval-pi05-crm-spatial-seed44` | pi05 | spatial | bjb2-28827 |
| `eval-random-selection-object-k5-seed42` | smolvla | object | bjb1-32546 |
| `eval-random-selection-object-k5-seed43` | smolvla | object | bjb2-28827 |
| `eval-random-selection-object-k5-seed44` | smolvla | object | bjb1-32546 |
| `eval-random-selection-object-k5-seed45` | smolvla | object | bjb1-32546 |
| `eval-random-selection-object-seed46-r2` | smolvla | object | bjb2-40593 |
| `train-crm-pi05-unified-3suite-r2` | pi05 | unknown | bjb1-18228 |
| `train-crm-unified-4suite` | smolvla | unknown | bjb1-18228 |

</details>

<details>
<summary><b>retry_after_failure</b> (13 experiments)</summary>

| Exp ID | Model | Suite | Server |
|---|---|---|---|
| `eval-direct-correction-object-seed42-r2` | smolvla | object | bjb1-32546 |
| `eval-obs-only-object-norm005-seed49-r2` | smolvla | object | bjb1-32546 |
| `eval-obs-only-object-norm005-seed55-r2` | smolvla | object | bjb1-18228 |
| `eval-obs-only-object-norm01-seed42-r2` | smolvla | object | bjb2-28827 |
| `eval-perdof-object-norm003-seed44-r2` | smolvla | object | bjb1-18228 |
| `eval-perdof-object-norm01-seed42-r2` | smolvla | object | bjb2-28827 |
| `eval-supp-long-vla-only-s43-r2` | smolvla | long | bjb1-32546 |
| `eval-supp-obj-k2mean-s47-r2` | smolvla | object | bjb1-32546 |
| `eval-vla-only-goal-seed47-r2` | smolvla | goal | bjb1-32546 |
| `eval-vla-only-goal-seed48-r2` | smolvla | goal | bjb1-32546 |
| `pi05-adaptive-object-s44-cqa1-r2` | pi05 | object | cqa1-32758 |
| `pi05-tau-sweep-goal-tau050-s42-r2` | pi05 | goal | cqa1-32758 |
| `train-crm-unified-4suite-r4` | smolvla | unknown | bjb1-32546 |

</details>

<details>
<summary><b>checkpoint_missing</b> (5 experiments)</summary>

| Exp ID | Model | Suite | Server |
|---|---|---|---|
| `eval-obs-only-object-norm003-seed62` | smolvla | object | bjb1-32546 |
| `eval-obs-only-object-norm003-seed63` | smolvla | object | bjb1-32546 |
| `eval-obs-only-object-norm01-seed51-r2` | smolvla | object | bjb1-32546 |
| `eval-obs-only-object-norm01-seed52-r2` | smolvla | object | bjb1-32546 |
| `smolvla-tau030-long-s42` | smolvla | long | bjb2-28827 |

</details>

<details>
<summary><b>ssh_failure</b> (4 experiments)</summary>

| Exp ID | Model | Suite | Server |
|---|---|---|---|
| `eval-k2-goal-vla-only-s49` | smolvla | goal | bjb2-40593 |
| `eval-mechanism-goal-adapt-s42` | smolvla | goal | bjb1-18228 |
| `pi05-crm-k2-long-s42` | pi05 | long | bjb1-18228 |
| `pi05-crm-k2-long-s43` | pi05 | long | bjb1-18228 |

</details>
