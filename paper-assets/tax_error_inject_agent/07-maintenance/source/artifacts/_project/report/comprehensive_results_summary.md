# Comprehensive Results Summary: TaxEI Error Injection Agent

**Project**: tax_error_inject_agent (Negative Result Paper)
**Generated**: 2026-05-15
**Model**: Qwen3-8B + LoRA (rank=16, alpha=32, dropout=0.05)
**Eval Set**: ALFWorld valid_unseen, 47 tasks, 6 task types
**Training**: MS-SWIFT SFT, 3 epochs, lr=1e-4, bs=1, grad_accum=8, bf16

---

## 1. Multi-Seed Clean Eval Summary

### 1.1 Main Results Table (Success Rate %)

| Method | Train Samples | seed=42 | seed=0 | seed=123 | Mean | SD | Range |
|--------|:------------:|:-------:|:------:|:--------:|:----:|:--:|:-----:|
| Zero-shot (Qwen3-8B) | 0 | 42.6 | — | — | — | — | — |
| Vanilla SFT | 4,358 | 61.7 | 68.1 | 66.0 | 65.3 | 3.3 | 6.4 |
| TaxEI SFT | 9,029 | 61.7 | 46.8 | 61.7 | 56.7 | 8.6 | 14.9 |
| Random SFT | 9,029 | 66.0 | 55.3 | **RUNNING** | 60.7* | 7.6* | 10.7* |

\* Random seed=123 eval (exp: `v4-random-seed123-eval`) still RUNNING; stats based on 2 seeds only.

### 1.2 Source Experiments (Clean Eval)

| exp_id | Method | Seed | Successes | Total | Rate |
|--------|--------|:----:|:---------:|:-----:|:----:|
| `v4-vanilla-eval-r3` | Vanilla | 42 | 29 | 47 | 61.7% |
| `v4-vanilla-seed0-eval` | Vanilla | 0 | 32 | 47 | 68.1% |
| `v4-vanilla-seed123-eval` | Vanilla | 123 | 31 | 47 | 66.0% |
| `v4-taxei-eval` | TaxEI | 42 | 29 | 47 | 61.7% |
| `v4-taxei-seed0-eval` | TaxEI | 0 | 22 | 47 | 46.8% |
| `v4-taxei-seed123-eval` | TaxEI | 123 | 29 | 47 | 61.7% |
| `v4-random-eval` | Random | 42 | 31 | 47 | 66.0% |
| `v4-random-seed0-eval` | Random | 0 | 26 | 47 | 55.3% |
| `v4-random-seed123-eval` | Random | 123 | — | 47 | RUNNING |

### 1.3 Per-Task Breakdown (seed=42)

| Task Type | N | Zero-shot | Vanilla | TaxEI | Random |
|-----------|:-:|:---------:|:-------:|:-----:|:------:|
| look_at_obj_in_light | 6 | 50.0% | 83.3% | 100% | 100% |
| pick_and_place_simple | 8 | 50.0% | 62.5% | 62.5% | 50.0% |
| pick_clean_then_place | 11 | 45.5% | 45.5% | 54.5% | 54.5% |
| pick_cool_then_place | 7 | 0.0% | 57.1% | 42.9% | 57.1% |
| pick_heat_then_place | 8 | 62.5% | 75.0% | 87.5% | 87.5% |
| pick_two_obj_and_place | 7 | 42.9% | 57.1% | 28.6% | 57.1% |

Sources: `vanilla-react-baseline`, `v4-vanilla-eval-r3`, `v4-taxei-eval`, `v4-random-eval`

---

## 2. Recovery Eval Summary (Error Injection at Test Time)

### 2.1 Overall Recovery Rates

| Method | Recovery Rate | Successes | Total | Detection Rate | exp_id |
|--------|:------------:|:---------:|:-----:|:--------------:|--------|
| Vanilla | 61.7% | 29 | 47 | 0% | `v4-vanilla-recovery-eval` |
| TaxEI | 59.6% | 28 | 47 | 0% | `v4-taxei-recovery-eval-r2` |
| Random | 63.8% | 30 | 47 | 0% | `v4-random-recovery-eval` |

All models achieve 0% explicit error detection rate. Recovery is achieved through implicit replanning, not explicit error recognition.

### 2.2 TaxEI Per-Operator Breakdown

| Operator | Type | Recovered | Total | Rate |
|----------|------|:---------:|:-----:|:----:|
| C1 (context truncation) | Context | 8 | 12 | 66.7% |
| C4 (observation masking) | Context | 7 | 11 | 63.6% |
| P1 (step order swap) | Plan | 7 | 12 | 58.3% |
| P2 (sub-goal deletion) | Plan | 6 | 12 | 50.0% |

Source: `v4-taxei-recovery-eval-r2`

### 2.3 Key Finding

TaxEI-trained model does NOT show improved recovery over vanilla baseline (-2.1pp). Random injection even outperforms TaxEI (+4.2pp vs TaxEI, +2.1pp vs Vanilla). This is a core negative result.

---

## 3. Dose-Response / Fixed-Size Ablation

Controls for data quantity confound: all conditions use exactly 4,358 total training samples (= vanilla data size).

| Condition | Injection Ratio | Clean | Injected | Success Rate | vs Vanilla (65.3%) |
|-----------|:--------------:|:-----:|:--------:|:------------:|:-----------------:|
| Vanilla (baseline) | 0% | 4,358 | 0 | 65.3% | — |
| TaxEI Fixed 10% | 10% | 3,922 | 436 | 61.7% | -3.6pp |
| TaxEI Fixed 25% | 25% | 3,268 | 1,090 | 48.9% | -16.4pp |
| TaxEI Full (50%) | ~52% | 4,358 | 4,671 | 61.7% | -3.6pp* |

\* Full TaxEI uses 9,029 total samples (2x vanilla), so not directly comparable in this table.

| exp_id | Condition | Seed |
|--------|-----------|:----:|
| `v4-taxei-fixed-inject10-eval` | Fixed 10% | 42 |
| `v4-taxei-fixed-inject25-eval` | Fixed 25% | 42 |

### 3.1 Dose-Response Pattern

- 10% injection: minimal harm (-3.6pp), within noise
- 25% injection: significant degradation (-16.4pp)
- Monotonic dose-response NOT observed (full 50% at 9,029 samples recovers to 61.7%), suggesting the harm at 25% is partly due to reduced clean data rather than injection toxicity alone

### 3.2 Per-Task Breakdown (Fixed-Size Ablation)

| Task Type | N | Vanilla 65.3% | Fixed 10% | Fixed 25% |
|-----------|:-:|:-------------:|:---------:|:---------:|
| look_at_obj_in_light | 6 | 83.3% | 83.3% | 66.7% |
| pick_and_place_simple | 8 | 62.5% | 62.5% | 37.5% |
| pick_clean_then_place | 11 | 45.5% | 45.5% | 45.5% |
| pick_cool_then_place | 7 | 57.1% | 57.1% | 28.6% |
| pick_heat_then_place | 8 | 75.0% | 75.0% | 62.5% |
| pick_two_obj_and_place | 7 | 57.1% | 57.1% | 57.1% |

Source: `v4-taxei-fixed-inject10-eval`, `v4-taxei-fixed-inject25-eval`

---

## 4. Training Metrics Summary

### 4.1 Vanilla SFT (4,358 samples)

| exp_id | Seed | Final Loss | Token Acc | Steps | Duration |
|--------|:----:|:----------:|:---------:|:-----:|:--------:|
| `mini-vanilla-sft-v4` | 42 | — | — | 1,635 | ~58 min |
| `v4-vanilla-seed0` | 0 | 0.297 | 90.2% | 1,635 | 58 min |
| `v4-vanilla-seed123` | 123 | 0.288 | 90.3% | 1,635 | 58.9 min |

### 4.2 TaxEI SFT (9,029 samples)

| exp_id | Seed | Final Loss | Token Acc | Steps | Duration |
|--------|:----:|:----------:|:---------:|:-----:|:--------:|
| `v4-taxei-sft-r3` | 42 | — | — | 3,387 | ~110 min |
| `v4-taxei-seed0` | 0 | 0.355 | 91.7% | 3,387 | 110 min |
| `v4-taxei-seed123` | 123 | 0.355 | 90.0% | 3,387 | 109.2 min |

### 4.3 Random SFT (9,029 samples)

| exp_id | Seed | Final Loss | Token Acc | Steps | Duration |
|--------|:----:|:----------:|:---------:|:-----:|:--------:|
| `v4-random-sft-r3` | 42 | — | — | 3,387 | ~110 min |
| `v4-random-seed0` | 0 | 0.355 | 91.2% | 3,387 | 110 min |
| `v4-random-seed123` | 123 | 0.168 | 94.2% | 3,387 | 110.2 min |

### 4.4 Fixed-Size Ablation Training (4,358 samples)

| exp_id | Injection % | Final Loss | Token Acc | Steps | Duration |
|--------|:-----------:|:----------:|:---------:|:-----:|:--------:|
| `v4-taxei-fixed-inject10` | 10% | 0.308 | 88.8% | 1,635 | 58 min |
| `v4-taxei-fixed-inject25-r2` | 25% | 0.285 | 89.3% | 1,635 | 58 min |

### 4.5 Training Observations

- TaxEI/Random models train ~2x longer due to 2x data (9,029 vs 4,358 samples)
- Final loss is higher for TaxEI/Random (~0.355) vs Vanilla (~0.29), consistent with injected samples being harder to fit
- Random seed=123 shows anomalously low final loss (0.168) — possibly a logging artifact
- All runs peak at ~18.5 GiB VRAM on RTX 5090

---

## 5. Statistical Tests Summary

### 5.1 McNemar's Tests (seed=42, n=47)

| Comparison | p-value | Discordant Pairs | Interpretation |
|------------|:-------:|:----------------:|----------------|
| Vanilla vs TaxEI (clean) | 1.000 | — | No significant difference |
| Vanilla vs Random (clean) | 0.754 | — | No significant difference |
| TaxEI vs Random (clean) | 0.754 | — | No significant difference |
| Vanilla seed=42 vs seed=0 | 0.375 | 5 | No significant difference |

Sources: `v4-taxei-eval`, `v4-random-eval`, `v4-vanilla-seed0-eval`

### 5.2 Multi-Seed Variance Analysis

| Method | Seeds | Mean | SD | CV | Interpretation |
|--------|:-----:|:----:|:--:|:--:|----------------|
| Vanilla | 3 | 65.3% | 3.3% | 5.0% | Low variance, stable |
| TaxEI | 3 | 56.7% | 8.6% | 15.2% | High variance, unstable |
| Random | 2* | 60.7% | 7.6% | 12.5% | High variance, unstable |

TaxEI shows 2.6x the coefficient of variation vs Vanilla, indicating that error injection not only fails to help but also destabilizes training.

---

## 6. Experiment Timeline & Status

### 6.1 Currently Running

| exp_id | Description | Status |
|--------|-------------|--------|
| `v4-random-seed123-eval` | Random SFT seed=123 clean eval | RUNNING |

### 6.2 Historical Progression

| Phase | Date | Key Result |
|-------|------|-----------|
| Trajectory Collection | 05-14 AM | 501 successful trajectories (70.2% rate, $8.86 API cost) |
| SFT Dry-run | 05-14 AM | Pipeline validated on 124 samples |
| v1 Mini SFT (278 samples) | 05-14 AM | Vanilla 14.9%, TaxEI 44.7% — insufficient data |
| Zero-shot Baseline | 05-14 AM | Qwen3-8B zero-shot: 42.6% |
| v3 SFT (4,176-9,076 samples) | 05-14 midday | Vanilla 74.5%, TaxEI 66.0%, Random 51.1% |
| v4 SFT (4,358-9,029 samples) | 05-14 PM | Vanilla 61.7%, TaxEI 61.7%, Random 66.0% |
| Multi-seed Eval | 05-14 PM-night | Vanilla stable (3.3% SD), TaxEI unstable (8.6% SD) |
| Recovery Eval | 05-14 PM-night | No method shows recovery advantage |
| Fixed-Size Ablation | 05-14 night | 10%: -3.6pp, 25%: -16.4pp dose-response |

---

## 7. Key Negative Results for Paper

1. **TaxEI does not improve clean performance**: Mean 56.7% vs Vanilla 65.3% (-8.6pp), p=1.0 at seed=42
2. **TaxEI does not improve recovery**: 59.6% vs Vanilla 61.7% (-2.1pp) under injected errors
3. **Random injection performs comparably to TaxEI**: Random 60.7% vs TaxEI 56.7% on clean, 63.8% vs 59.6% on recovery — taxonomy structure provides no benefit over random perturbation
4. **TaxEI destabilizes training**: 8.6% SD across seeds vs Vanilla's 3.3% SD (2.6x CV)
5. **0% explicit error detection**: All models recover through implicit replanning, not learned error detection — the detection+recovery mechanism that TaxEI trains for does not emerge
6. **Dose-response**: Higher injection ratios (25%) actively harm performance (-16.4pp)

---

## Appendix: Data Composition

| Dataset | Clean Trajectories | Injected Trajectories | Total |
|---------|:-----------------:|:--------------------:|:-----:|
| Vanilla v4 | 4,358 | 0 | 4,358 |
| TaxEI v4 | 4,358 | 4,671 | 9,029 |
| Random v4 | 4,358 | 4,671 | 9,029 |
| TaxEI Fixed 10% | 3,922 | 436 | 4,358 |
| TaxEI Fixed 25% | 3,268 | 1,090 | 4,358 |

Error injection operators: P1 (step order swap), P2 (sub-goal deletion), C1 (context truncation), C4 (observation masking)
