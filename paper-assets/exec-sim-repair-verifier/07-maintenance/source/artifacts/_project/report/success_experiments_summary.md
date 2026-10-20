# Experiment Results Summary (2026-05-14)

33 success experiments out of 59 total. All function-level experiments use CoderForge test set (1,890 test samples, 114 problems).

---

## Table 1: Function-level CLS (per-test classification, Qwen3-4B, 5 seeds)

| Seed | Accuracy | Pass_F1 | Fail_F1 | Pass_P | Pass_R | Fail_P | Fail_R |
|------|----------|---------|---------|--------|--------|--------|--------|
| 0    | 87.94    | 87.79   | 88.08   | 92.13  | 83.84  | 84.20  | 92.32  |
| 42   | 87.83    | 88.06   | 87.59   | 89.45  | 86.71  | 86.20  | 89.04  |
| 123  | 89.52    | 89.64   | 89.40   | 91.76  | 87.63  | 87.34  | 91.56  |
| 456  | 87.88    | 87.53   | 88.21   | 93.60  | 82.21  | 83.12  | 93.97  |
| 789  | 89.00    | 88.90   | 89.10   | 93.30  | 84.90  | 85.20  | 93.40  |
| **Mean±Std** | **88.43 ± 0.78** | **88.38 ± 0.87** | **88.48 ± 0.75** | **92.05 ± 1.64** | **85.06 ± 2.18** | **85.21 ± 1.65** | **92.06 ± 1.93** |

---

## Table 2: Function-level CWM (execution simulation, Qwen3-4B, 5 seeds)

| Seed | Accuracy | Pass_F1 | Fail_F1 | Pass_P | Pass_R | Fail_P | Fail_R | ExactMatch |
|------|----------|---------|---------|--------|--------|--------|--------|------------|
| 0    | 87.57    | 87.18   | 87.93   | 93.45  | 81.70  | 82.71  | 93.86  | 84.29      |
| 42   | 87.51    | 87.31   | 87.71   | 92.06  | 83.03  | 83.53  | 92.32  | 84.02      |
| 123  | 87.20    | 86.95   | 87.44   | —      | —      | —      | —      | 84.44      |
| 456  | 86.98    | 86.66   | 87.29   | 92.26  | 81.70  | 82.52  | 92.65  | 84.02      |
| 789  | 86.67    | 86.74   | 86.60   | 89.37  | 84.25  | 84.09  | 89.25  | 83.97      |
| **Mean±Std** | **87.19 ± 0.37** | **86.97 ± 0.28** | **87.39 ± 0.51** | **91.78 ± 1.72** | **82.67 ± 1.23** | **83.21 ± 0.73** | **92.02 ± 1.96** | **84.15 ± 0.21** |

---

## Table 3: Function-level CLS vs CWM (4B, 5-seed paired comparison)

| Model | Formulation | Seeds | Accuracy (mean±std) | Pass_F1 | Fail_F1 |
|-------|-------------|-------|---------------------|---------|---------|
| 4B    | CLS         | 5     | 88.43 ± 0.78       | 88.38 ± 0.87 | 88.48 ± 0.75 |
| 4B    | CWM         | 5     | 87.19 ± 0.37       | 86.97 ± 0.28 | 87.39 ± 0.51 |
| **Gap (CLS−CWM)** | | 5 | **+1.25 ± 1.01**   | **+1.42 ± 0.94** | **+1.08 ± 1.13** |

- Paired t-test: acc p=0.0506, pass_f1 p=0.0285, fail_f1 p=0.0993
- Per-seed accuracy gaps: seed0=+0.37, seed42=+0.32, seed123=+2.32, seed456=+0.90, seed789=+2.33

---

## Table 4: 8B Scaling (3 matched seeds: 42, 123, 456)

| Model | Size | Formulation | Seeds | Accuracy (mean±std) | Pass_F1 | Fail_F1 |
|-------|------|-------------|-------|---------------------|---------|---------|
| Qwen3 | 4B  | CLS         | 3     | 88.41 ± 0.96       | 88.41 ± 1.10 | — |
| Qwen3 | 4B  | CWM         | 3     | 87.23 ± 0.27       | 86.97 ± 0.33 | — |
| Qwen3 | 8B  | CLS         | 3     | 89.39 ± 1.09       | 89.53 ± 1.33 | 89.22 ± 0.83 |
| Qwen3 | 8B  | CWM         | 3     | 86.96 ± 0.72       | 86.79 ± 0.81 | 87.14 ± 0.63 |

| Per-seed 8B detail | Seed 42 | Seed 123 | Seed 456 |
|---|---|---|---|
| 8B CLS | 90.48 | 89.37 | 88.31 |
| 8B CWM | 87.67 | 86.98 | 86.24 |
| Gap | +2.81 | +2.39 | +2.07 |

- CLS-CWM gap (4B, 3-seed): +1.18 ± 1.03pp
- CLS-CWM gap (8B, 3-seed): +2.42 ± 0.37pp (paired t p=0.0077)
- 4B→8B CLS gain: +0.98pp; CWM gain: −0.27pp
- Gap widening: +1.24pp wider at 8B → CWM bottleneck amplified by scale

---

## Table 5: Trajectory-level (Qwen3-4B, 5 seeds)

| Seed | Accuracy | Unresolved_F1 | Resolved_F1 | Unres_P | Unres_R | Res_P | Res_R | Consistency |
|------|----------|---------------|-------------|---------|---------|-------|-------|-------------|
| 0    | 85.66    | 87.37         | 83.41       | 82.71   | 92.59   | 90.07 | 77.66 | 79.55       |
| 42   | 85.66    | 87.50         | 83.18       | —       | —       | —     | —     | 79.94       |
| 123  | 85.47    | 87.00         | 83.52       | 83.53   | 90.78   | 88.17 | 79.33 | 78.59       |
| 456  | 87.40    | 88.70         | 85.80       | 85.70   | 91.90   | 89.70 | 82.30 | 78.80       |
| 789  | 87.31    | 88.27         | 86.17       | 87.41   | 89.15   | 87.18 | 85.18 | 76.74       |
| **Mean±Std** | **86.30 ± 0.97** | **87.77 ± 0.70** | **84.42 ± 1.44** | — | — | — | — | **78.72 ± 1.24** |

---

## Table 6: Zero-shot LLM Judge

| Model | Accuracy | Pass_F1 | Fail_F1 | Pass_P | Pass_R | Fail_P | Fail_R |
|-------|----------|---------|---------|--------|--------|--------|--------|
| Qwen3-8B zero-shot  | 64.40 | 50.50 | 72.20 | 90.00 | 35.10 | 57.90 | 95.80 |
| Qwen3-32B zero-shot | 71.69 | 65.68 | 75.91 | 88.12 | 52.35 | 64.40 | 92.43 |
| FT 4B CLS (ref)     | 88.43 | 88.38 | 88.48 | 92.05 | 85.06 | 85.21 | 92.06 |

- Gap vs FT 4B: 8B zero-shot −24.03pp, 32B zero-shot −16.74pp
- Fine-tuned 4B dominates 8× larger zero-shot model

---

## Table 7: Repo-level (SWE-bench, completed results)

| Experiment | Acc | F1_macro | Pass_F1 | Fail_F1 | Unparseable | Majority BL | Status |
|------------|-----|----------|---------|---------|-------------|-------------|--------|
| CLS v4 (old hp) | 66.11 | 56.61 | 76.90 | 36.30 | 132 | 72.96% | success (early stop) |
| CLS v5 (fixed hp) | **76.92** | **73.90** | **82.78** | **65.01** | 132 | 72.96% | **success** |
| CWM v10 | 69.91 | 46.71 | 81.87 | 11.54 | 9,102 (93%) | 72.96% | success (eval invalid) |
| CWM v11 | 66.60 | 52.99 | 78.30 | 27.70 | 376 (75%) | 72.96% | killed (subset-500) |
| CLS 8B | 71.37 | 69.05 | 77.53 | 60.57 | 136 | 72.96% | killed (env mismatch) |

- Only CLS v5 is a valid repo-level result
- CWM repo-level: generation too long / unparseable, eval unreliable
- CLS 8B: trained with mismatched transformers version (5.8.0 vs 4.57.6)

---

## Table 8: Analysis Experiments

### 5-paired-clustered-bootstrap (CLS vs TRAJ equivalence)
- Pooled variant-level gap (CLS−TRAJ): −0.45pp, 95% CI [−1.71, +0.84]
- Paired t-test: p=0.499 (not significant)
- TOST equivalence: p=0.0071 (equivalent within ±2pp margin)
- Per-seed gaps: seed42=−0.97, seed123=+1.45, seed456=−1.84, seed789=−0.78, seed0=−0.29

### per-test-majority-voting (K=3, temp=0.7)
- Greedy: 87.51% → Majority vote: 86.83% (Δ=−0.69pp)
- Unanimous: 93.3%, split samples: 127, net flips: −13
- Conclusion: NEGATIVE — majority voting hurts

### block-corr-empirical (error correlation within problems)
- ICC=0.191 (p<1e-10), design effect=3.97
- All-correct ratio: 2.81× vs i.i.d. expectation
- Error std ratio: 1.89× vs i.i.d.

### oracle-f2p-stratified (per-test advantage by F2P count)
- T=1 (68.7%): block_adv=−0.09pp (no advantage)
- T=2 (19.1%): block_adv=+31.69pp
- T=3–5 (7.1%): block_adv=+40.74pp
- T≥6 (5.1%): block_adv=+40.06pp
- T=2 contributes 55.3% of overall advantage

### mvp-a-oracle-sim (total F2P+P2P simulation)
- 10% regression: iid_adv=13.2pp, block_adv=8.3pp (PASS)
- 5% regression: iid_adv=−1.0pp, block_adv=−0.5pp (FAIL)

### per-test-precision-recall (diagnostic)
- 48/114 problems (42.1%) perfectly predicted
- Median problem fail-F1: 94.12%
- Best mutation: return_value (97.26%), Worst: off_by_one (82.56%)

---

## Core Comparison Numbers (Paper)

1. **4B CLS vs CWM (5-seed)**: gap=+1.25±1.01pp, paired t p=0.051
2. **8B CLS vs CWM (3-seed)**: gap=+2.42±0.37pp, paired t p=0.008
3. **Scaling 4B→8B**: CLS +0.98pp, CWM −0.27pp; gap widens +1.24pp
4. **FT 4B vs zero-shot 32B**: +16.74pp advantage for fine-tuned 4B
5. **Repo-level**: CLS v5=76.92% (only valid), CWM eval invalid
6. **TOST CLS≈TRAJ**: equivalent within ±2pp (p=0.007)
