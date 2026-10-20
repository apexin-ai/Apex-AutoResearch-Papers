# Tax Error Inject Agent — Comprehensive Results Summary

> Generated: 2026-05-15 | Data source: experiment registry (tax_error_inject_agent)
> All v4 experiments use Qwen3-8B + LoRA (rank=16, alpha=32), 3 epochs, lr=1e-4, bf16

---

## 0. Experiment Overview

| Condition | Training Data | Samples | Description |
|-----------|--------------|---------|-------------|
| **Vanilla** | sft_vanilla_v4.jsonl | 4,358 | Clean successful trajectories only |
| **TaxEI** | sft_taxei_v4.jsonl | 9,029 | Clean + taxonomy-guided error-injection-recovery pairs (~50% injected) |
| **Random** | sft_random_v4.jsonl | 9,029 | Clean + random error-injection-recovery pairs (~50% injected) |
| **Fixed-inject10** | sft_taxei_v4_fixed_inject10.jsonl | 4,358 | 3,922 clean + 436 injected (10% ratio, same total as vanilla) |
| **Fixed-inject25** | sft_taxei_v4_fixed_inject25.jsonl | 4,358 | 3,268 clean + 1,090 injected (25% ratio, same total as vanilla) |

**Zero-shot baseline**: Qwen3-8B ReAct (no SFT) = **42.6%** (20/47) `[vanilla-react-baseline]`

---

## 1. Multi-Seed Clean Eval (47 ALFWorld valid_unseen tasks, no injection)

### 1.1 Vanilla SFT (4,358 samples)

| Metric | seed=42 | seed=0 | seed=123 | Mean ± SD |
|--------|---------|--------|----------|-----------|
| Success Rate | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3% ± 3.3** |
| Registry ID | *(pre-registry)* | `v4-vanilla-seed0-eval` | `v4-vanilla-seed123-eval` | — |

### 1.2 TaxEI SFT (9,029 samples)

| Metric | seed=42 | seed=0 | seed=123 | Mean ± SD |
|--------|---------|--------|----------|-----------|
| Success Rate | 61.7% (29/47) | 46.8% (22/47) | 61.7% (29/47) | **56.7% ± 8.6** |
| vs Vanilla (same seed) | 0.0pp | −21.3pp | −4.3pp | **−8.6pp** |
| Registry ID | *(pre-registry)* | `v4-taxei-seed0-eval` | `v4-taxei-seed123-eval` | — |

### 1.3 Random SFT (9,029 samples)

| Metric | seed=42 | seed=0 | seed=123 | Mean ± SD |
|--------|---------|--------|----------|-----------|
| Success Rate | 66.0% (31/47) | 55.3% (26/47) | **RUNNING** | 60.7% ± 7.6 *(2-seed)* |
| vs Vanilla (same seed) | +4.3pp | −12.8pp | — | — |
| Registry ID | *(pre-registry)* | `v4-random-seed0-eval` | `v4-random-seed123-eval` | — |

### 1.4 Cross-Method Comparison (per-task breakdown, available seeds)

**Vanilla seed=0 per-task**: light 83.3%, place 62.5%, clean 54.5%, cool 57.1%, heat 87.5%, two_obj 71.4%
**Vanilla seed=123 per-task**: light 83.3%, place 75.0%, clean 45.5%, cool 57.1%, heat 87.5%, two_obj 57.1%
**TaxEI seed=123 per-task**: light 83.3%, place 50.0%, clean 63.6%, cool 42.9%, heat 75.0%, two_obj 57.1%
**TaxEI seed=0**: 46.8% overall (per-task not in registry)
**Fixed-inject10 per-task**: light 83.3%, place 62.5%, clean 45.5%, cool 57.1%, heat 75.0%, two_obj 57.1%
**Fixed-inject25 per-task**: light 66.7%, place 37.5%, clean 45.5%, cool 28.6%, heat 62.5%, two_obj 57.1%
**Zero-shot per-task**: light 50.0%, place 50.0%, clean 45.5%, cool 0.0%, heat 62.5%, two_obj 42.9%

---

## 2. Recovery Eval (47 episodes with error injection during eval)

### 2.1 Overall Recovery Rates

| Method | Recovery Rate | Successes/Total | Detection Rate | Registry ID |
|--------|-------------|-----------------|---------------|-------------|
| **Vanilla** | 61.7% | 29/47 | 0% | `v4-vanilla-recovery-eval` |
| **TaxEI** | 59.6% | 28/47 | 0% | `v4-taxei-recovery-eval-r2` |
| **Random** | 63.8% | 30/47 | 0% | `v4-random-recovery-eval` |

**Key finding**: TaxEI does NOT improve recovery over vanilla or random. No method achieves explicit error detection (detection_rate = 0% across all conditions).

### 2.2 TaxEI Per-Operator Breakdown (seed=42)

| Operator | Recovered | Total | Rate | Description |
|----------|-----------|-------|------|-------------|
| C1_context_truncation | 8 | 12 | 66.7% | Truncate context history |
| C4_observation_masking | 7 | 11 | 63.6% | Mask environment observations |
| P1_step_order_swap | 7 | 12 | 58.3% | Swap action step order |
| P2_sub_goal_deletion | 6 | 12 | 50.0% | Delete sub-goal steps |

Source: `v4-taxei-recovery-eval-r2`

Note: Per-operator breakdown not available for Vanilla and Random in registry. Run-to-run variance observed: TaxEI r1=28/47, r2=28/47 (consistent); Random r1=29/47, r2=30/47 (±2pp).

---

## 3. Dose-Response (Fixed-Size Ablation)

All conditions use **4,358 total samples** (same as vanilla), varying injection ratio.

| Injection Ratio | Clean | Injected | Success Rate | vs Vanilla (seed=42) | Registry ID |
|----------------|-------|----------|-------------|---------------------|-------------|
| 0% (Vanilla) | 4,358 | 0 | 61.7% (29/47) | — | *(pre-registry)* |
| 10% | 3,922 | 436 | 61.7% (29/47) | 0.0pp | `v4-taxei-fixed-inject10-eval` |
| 25% | 3,268 | 1,090 | 48.9% (23/47) | −12.8pp | `v4-taxei-fixed-inject25-eval` |

**Reference** (different total size):

| Condition | Clean | Injected | Total | Success Rate | Note |
|-----------|-------|----------|-------|-------------|------|
| TaxEI full (~50%) | ~4,500 | ~4,500 | 9,029 | 61.7% (29/47) seed=42 | 2× data compensates for injection |

### 3.1 Fixed-inject10 Per-Task Breakdown

| Task Type | Success | Total | Rate |
|-----------|---------|-------|------|
| look_at_obj_in_light | 5 | 6 | 83.3% |
| pick_and_place_simple | 5 | 8 | 62.5% |
| pick_clean_then_place | 5 | 11 | 45.5% |
| pick_cool_then_place | 4 | 7 | 57.1% |
| pick_heat_then_place | 6 | 8 | 75.0% |
| pick_two_obj_and_place | 4 | 7 | 57.1% |

### 3.2 Fixed-inject25 Per-Task Breakdown

| Task Type | Success | Total | Rate |
|-----------|---------|-------|------|
| look_at_obj_in_light | 4 | 6 | 66.7% |
| pick_and_place_simple | 3 | 8 | 37.5% |
| pick_clean_then_place | 5 | 11 | 45.5% |
| pick_cool_then_place | 2 | 7 | 28.6% |
| pick_heat_then_place | 5 | 8 | 62.5% |
| pick_two_obj_and_place | 4 | 7 | 57.1% |

**Interpretation**: At fixed total data budget, injecting 10% error-recovery pairs causes no harm; injecting 25% significantly degrades performance (−12.8pp), suggesting clean demonstrations are being displaced.

---

## 4. Training Metrics

### 4.1 Main Conditions (v4)

| Condition | Seed | Final Loss | Token Acc | Steps | Duration (min) | Samples | Memory (GiB) | Registry ID |
|-----------|------|-----------|-----------|-------|---------------|---------|-------------|-------------|
| Vanilla | 0 | 0.297 | 0.902 | 1,635 | 58.0 | 4,358 | — | `v4-vanilla-seed0` |
| Vanilla | 123 | 0.288 | 0.903 | 1,635 | 58.9 | 4,358 | — | `v4-vanilla-seed123` |
| TaxEI | 0 | 0.355 | 0.917 | 3,387 | 110.0 | 9,029 | — | `v4-taxei-seed0` |
| TaxEI | 123 | 0.355 | 0.900 | 3,387 | 109.2 | 9,029 | 18.49 | `v4-taxei-seed123` |
| Random | 0 | 0.355 | 0.912 | 3,387 | 110.0 | 9,029 | — | `v4-random-seed0` |
| Random | 123 | 0.355† | 0.942† | 3,387 | 110.2 | 9,029 | 18.49 | `v4-random-seed123` |

†Random seed=123 reports train_loss=0.355 (avg) and final_loss=0.168 (last step); token_accuracy=0.942 may reflect final step rather than average (avg=0.909).

### 4.2 Fixed-Size Ablation Training

| Condition | Seed | Final Loss | Token Acc | Steps | Duration (min) | Registry ID |
|-----------|------|-----------|-----------|-------|---------------|-------------|
| Fixed-inject10 | 42 | 0.308 | 0.888 | 1,635 | 58 | `v4-taxei-fixed-inject10` |
| Fixed-inject25 | 42 | 0.285 | 0.893 | 1,635 | 58 | `v4-taxei-fixed-inject25-r2` |

### 4.3 Observations

- **Loss**: Vanilla achieves lower final loss (~0.29) than TaxEI/Random (~0.35), likely because injected error-recovery pairs are harder to fit
- **Token accuracy**: All conditions converge to 0.89–0.92
- **Duration**: TaxEI/Random take ~2× longer than Vanilla (110 vs 58 min) due to 2× data
- **Fixed-size** ablations match Vanilla duration (~58 min) as expected

---

## 5. Statistical Tests

### 5.1 McNemar Test (Vanilla seed=42 vs seed=0)

| Comparison | p-value | Discordant Pairs | Significant? |
|-----------|---------|-----------------|-------------|
| Vanilla s42 vs s0 | 0.375 | 5 | No (p > 0.05) |

Source: `v4-vanilla-seed0-eval`

### 5.2 Cross-Seed Variance Analysis

| Method | Seeds | Rates | Range | SD | CV |
|--------|-------|-------|-------|----|----|
| Vanilla | 42, 0, 123 | 61.7%, 68.1%, 66.0% | 6.4pp | 3.3pp | 5.0% |
| TaxEI | 42, 0, 123 | 61.7%, 46.8%, 61.7% | 14.9pp | 8.6pp | 15.2% |
| Random | 42, 0 | 66.0%, 55.3% | 10.7pp | 7.6pp | 12.5% |

**Key finding**: TaxEI and Random show substantially higher variance across seeds than Vanilla (SD 8.6pp / 7.6pp vs 3.3pp). TaxEI seed=0 is a clear outlier at 46.8%.

### 5.3 Summary of Key Comparisons

| Comparison | Δ (pp) | Direction | Interpretation |
|-----------|--------|-----------|---------------|
| TaxEI vs Vanilla (mean) | −8.6 | TaxEI worse | Error injection hurts clean performance |
| Random vs Vanilla (mean, 2-seed) | −4.6 | Random worse | Random injection also hurts, less than TaxEI |
| TaxEI vs Random (mean) | −4.0 | TaxEI worse | Taxonomy structure does not help over random |
| Fixed-inject10 vs Vanilla (s42) | 0.0 | Equal | 10% injection harmless at fixed budget |
| Fixed-inject25 vs Vanilla (s42) | −12.8 | inject25 worse | 25% injection severely hurts at fixed budget |
| TaxEI recovery vs Vanilla recovery | −2.1 | TaxEI worse | TaxEI does not improve error recovery |
| Random recovery vs Vanilla recovery | +2.1 | Random better | Marginal, likely noise |

---

## 6. Pilot / Early Experiments (for reference)

| Experiment | Samples | Success Rate | Note | Registry ID |
|-----------|---------|-------------|------|-------------|
| Zero-shot ReAct | — | 42.6% (20/47) | Qwen3-8B baseline | `vanilla-react-baseline` |
| Mini Vanilla SFT (pilot) | 278 | 14.9% (7/47) | Insufficient data | `mini-vanilla-sft` |
| Mini TaxEI SFT (pilot) | 278 | 44.7% (21/47) | Insufficient data | `mini-taxei-sft` |
| SFT dry-run | 124 | — | Pipeline validation | `sft-dryrun-73` |
| Trajectory collection | 714 attempts | 70.2% teacher success | GPT-5.2 teacher, $8.86 | `traj_collect_500` |

---

## 7. Still Running

| Experiment | Status | Description |
|-----------|--------|-------------|
| `v4-random-seed123-eval` | RUNNING | Random SFT seed=123 clean eval (47 tasks). Completes the 3-seed Random comparison. |

---

## 8. Key Takeaways (Negative Results)

1. **TaxEI does not improve clean task performance**: Mean 56.7% vs Vanilla 65.3% (−8.6pp)
2. **TaxEI does not improve error recovery**: 59.6% vs Vanilla 61.7% (−2.1pp), detection rate = 0%
3. **Taxonomy structure provides no advantage over random injection**: TaxEI 56.7% vs Random 60.7%
4. **Injection displaces useful training signal**: At fixed data budget, 25% injection causes −12.8pp drop; effect is dose-dependent
5. **High variance under injection**: TaxEI cross-seed SD=8.6pp vs Vanilla SD=3.3pp, suggesting injection introduces training instability
6. **2× data partially compensates**: Full TaxEI (9,029 samples) matches Vanilla seed=42 (61.7%), but only because extra data offsets injection harm
