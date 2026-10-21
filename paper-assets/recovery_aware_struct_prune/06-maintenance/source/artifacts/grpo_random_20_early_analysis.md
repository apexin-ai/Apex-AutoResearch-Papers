# grpo_random_20 Early Analysis: Pre-Step-10 Status

Generated: 2026-05-17. W&B run: z9nqlucg.

---

## 0. Data Availability

**All three runs use logging_steps=10, so W&B has no metrics for steps 1-8.** First logged point for each run is step 10. This analysis is based on:
- grpo_random_20: server stdout timing data (step 8 in progress)
- RASP v9 / Standard v8: step 10+ data from existing collapse dynamics analysis

---

## 1. grpo_random_20 Current Status (step 8/100)

| Metric | Value |
|:-------|:------|
| W&B run ID | `z9nqlucg` |
| Current step | 8/100 |
| Wall clock | ~52 min (started 21:44 UTC) |
| Step speed | ~6.5 min/step |
| GPU usage | 73,165 MiB / 97,887 MiB (cuda:1) |
| GPU util | 100%, 82 C |
| Parent model | sft_random_20 (6.09B params) |
| ETA step 10 | ~22:51 UTC (first W&B log) |
| ETA completion | ~08:40 UTC May 18 |

### Timing per step (from stdout)
| Step | Wall time (sec) |
|:----:|:---------------:|
| 1-6 | ~314 avg |
| 7 | 352 |
| 8 | 378 |

**Observation**: Step time increasing (314 -> 352 -> 378s), possibly indicating generation length growth. In RASP v9, mean_length was 991/1024 at step 10 (near max). However, moderate increase (~20% over 3 steps) is normal in early GRPO.

---

## 2. Three-Way Comparison at Step 10 (earliest available data)

| Metric | Random 20 | RASP v9 | Standard v8 |
|:-------|:---------:|:-------:|:-----------:|
| reward | **TBD** | 0.015 | 0.0575 |
| grad_norm | **TBD** | 0.007 | 2.906 |
| frac_zero_std | **TBD** | 0.875 | 0.500 |
| entropy | **TBD** | 0.054 | 0.148 |
| loss | **TBD** | 0.007 | N/A |
| kl | **TBD** | 0.0007 | N/A |
| mean_length | **TBD** | 991 | 749 |
| Phase | **TBD** | Full collapse | Warm-up |

### Collapse thresholds:
- grad_norm < 0.05: collapsed
- frac_zero_std >= 0.85: collapsed
- reward < 0.03: collapsed

---

## 3. Pre-Step-10 Collapse Signal Analysis

### 3.1 Timing proxy

The only pre-step-10 proxy is wall-clock step time:
- **Random**: 314s -> 352s -> 378s (step 6/7/8), +20% over 3 steps
- A sharp increase (2x+) would indicate generation lengths maxing out (collapse precursor)
- Random's increase is moderate, NOT a clear collapse signal

### 3.2 Structural comparison

| Property | Random 20 | RASP v9 | Standard v8 |
|:---------|:---------:|:-------:|:-----------:|
| Params | 6.09B | ~6.16B | 6.16B |
| Pruning strategy | Random | CKA-aware (low overlap first) | Importance only |
| Structural redundancy preserved | Unknown | Low | Medium |

### 3.3 Hypothesis scenarios

| Scenario | Random collapse timing | Implication |
|:---------|:----------------------|:------------|
| A: Random ~ RASP (~step 10) | All structured pruning damages RL, CKA irrelevant | Weakens RASP narrative |
| B: Random ~ Standard (~step 60) | CKA-aware selection specifically damages RL | Strengthens redundancy-stability claim |
| C: Random stable (no collapse) | Random preserves more RL-relevant structure | Forces narrative restructuring |

---

## 4. Preliminary Assessment

### 4.1 No early collapse signals (cautiously positive)

grpo_random_20 is running normally at step 8 with moderate step-time increase. RASP v9's catastrophic collapse was fully established by step 10 with extreme severity across all metrics. If Random had the same pattern, we would expect dramatic step-time escalation by now.

**Tentatively favors Scenario B or C over Scenario A.**

### 4.2 What to watch at step 10

| Metric | Collapse threshold | RASP v9 @ step 10 | Healthy range |
|:-------|:------------------|:-------------------|:--------------|
| grad_norm | < 0.05 | 0.007 (dead) | > 1.0 |
| frac_zero_std | >= 0.85 | 0.875 (collapsed) | < 0.6 |
| reward | < 0.03 | 0.015 (flat) | > 0.05 |
| entropy | < 0.1 | 0.054 (dead) | > 0.12 |
| mean_length | > 950 | 991 (saturated) | < 800 |

### 4.3 Confidence

| Prediction | Confidence | Reasoning |
|:-----------|:-----------|:----------|
| Random NOT in immediate collapse (< step 10) | Medium-High | Step timing normal |
| Random will collapse later than RASP (> step 10) | Medium | Timing proxy only |
| Random collapse timing (specific step) | Low | Need step 10+ data |

---

## 5. Collapse Timing Prediction (preliminary)

Based on structural analysis:
- Random pruning removes neurons without regard to importance or redundancy
- This likely removes some critical neurons (like Standard) AND some redundant ones (unlike RASP which preferentially removes redundant ones)
- Predicted collapse window: **step 20-40** (between RASP's ~10 and Standard's ~60)
- Rationale: Random is a structural "average" of the two deliberate strategies

**This prediction is speculative and will be updated after step 10 data.**

---

## 6. Next Steps

1. **Fetch step 10 W&B data** when available (~22:51 UTC or later)
2. If healthy at step 10: Random already survives longer than RASP, confirming CKA-aware pruning is specifically harmful
3. Monitor step 20/30/40 for collapse onset relative to Standard v8
4. If collapsed at step 10: Scenario A, all pruning methods cause immediate collapse under this GRPO config
