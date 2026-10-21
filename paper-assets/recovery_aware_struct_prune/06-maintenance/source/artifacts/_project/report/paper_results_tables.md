# Paper Results Tables — Recovery-Aware Structured Pruning (D056 Fair v5 Config)

Updated: 2026-05-18. All data from experiment registry, W&B verified where noted.

---

## Table 1: Recovery Capacity Gradient (GRPO, fair v5 config, 20% sparsity)

All methods: identical GRPO config (lr=1e-6, β=0.01, T=0.4, 100 steps, binary reward on GSM8K).

| Method | Peak Rew. ↑ | Mean Rew. ↑ | Min f₀ ↓ | Behavior | Registry ID | W&B Run |
|:-------|:-----------:|:-----------:|:---------:|:---------|:------------|:--------|
| **CKA-only** | **0.354** | **0.275** | **0.125** | Active learning | grpo_cka_only_20 | li451oi4 |
| Random | 0.190 | 0.164 | 0.300 | Stagnation | grpo_random_20 | (crashed) |
| Standard | 0.081 | 0.050 | 0.500 | Borderline collapse | grpo_standard_20_fair | tyv20u2k |
| RASP (α=1.0) | 0.061 | 0.031 | 0.675 | Full collapse | grpo_rasp_20_fair | — |
| Unpruned | 0.669 | — | 0.125 | Stable | grpo_unpruned_v2 | hwucjf2n |

**Key ratios:**
- Peak gap: CKA-only / RASP = 5.8×
- Mean gap: CKA-only / RASP = 8.9×
- CKA-only / Standard peak = 4.4×

**CKA-only reward trajectory (W&B verified, optimizer steps 10-100):**
```
steps:  [10,     20,     30,     40,     50,     60,     70,     80,     90,     100]
reward: [0.2531, 0.2181, 0.2500, 0.2344, 0.3544, 0.2994, 0.3075, 0.3419, 0.2419, 0.3444]
f0:     [0.175,  0.200,  0.200,  0.350,  0.150,  0.200,  0.125,  0.250,  0.300,  0.200]
```

**Standard reward trajectory (W&B verified):**
```
steps:  [10,     20,     30,     40,     50,     60,     70,     80,     90,     100]
reward: [0.0513, 0.0556, 0.0669, 0.0813, 0.0188, 0.0431, 0.0469, 0.0456, 0.0306, 0.0538]
f0:     [0.500,  0.625,  0.500,  0.500,  0.575,  0.550,  0.575,  0.550,  0.550,  0.550]
```

**RASP reward trajectory (log verified, westd-11672):**
```
steps:  [10,      20,      30,      40,      50,      60,      70,      80,     90,    100]
reward: [0.01688, 0.02063, 0.02250, 0.02125, 0.06125, 0.05312, 0.05563, 0.030,  0.015, 0.010]
f0:     [0.850,   0.850,   0.800,   0.850,   0.725,   0.750,   0.675,   0.775,  0.900, 0.850]
```

**Random reward trajectory (log file, steps 10-90 only, timeout at step 97):**
```
steps:  [10,    20,    30,    40,    50,    60,    70,    80,    90]
reward: [0.161, 0.142, 0.166, 0.145, 0.175, 0.184, 0.190, 0.142, 0.173]
f0:     [0.300, 0.325, 0.325, 0.350, 0.300, 0.350, 0.300, 0.350, 0.325]
```

**Unpruned reward trajectory (W&B verified, steps 30-100):**
```
steps:  [30,     40,     50,     60,     70,     80,     90,     100]
reward: [0.4250, 0.5381, 0.5894, 0.6469, 0.6031, 0.6694, 0.5644, 0.6612]
```

---

## Table 2: Reward-Accuracy Decoupling (GSM8K, N=1319, greedy)

| Method | SFT Acc (%) | GRPO Acc (%) | Δ (pp) | GRPO Step | Peak Rew. | Registry ID |
|:-------|:-----------:|:------------:|:------:|:---------:|:---------:|:------------|
| Unpruned | 81.27 | 81.27 | 0.00 | 100 | 0.669 | eval_sft_unpruned_full, eval_grpo_unpruned_v2_step100 |
| CKA-only | 63.91 | — | — | — | 0.354 | eval_sft_cka_only_20_n1319 |
| Standard | 59.29 | 58.91 | −0.38 | 50 | 0.081 | eval_sft_standard_full_westd, eval_grpo_standard_step50_full |
| RASP | 61.49 | 60.65 | −0.84 | 5 | 0.061 | eval_sft_rasp_full_westd, eval_grpo_rasp_v9_step5 |

**Notes:**
- CKA-only GRPO accuracy not yet evaluated (marked "—" in paper)
- RASP evaluated at step 5 (last stable checkpoint before collapse in v9 run)
- Standard evaluated at step 50 (last stable checkpoint)

---

## Table 3: α Ablation (post-prune accuracy, N=100, 20% sparsity)

| α | Post-Prune Acc (%) | Avg Len | EOS Rate | N | Registry ID |
|:-:|:------------------:|:-------:|:--------:|:-:|:------------|
| 0.0 (Standard) | 27 | 1192 | 0.80 | 100 | alpha_ablation_sweep |
| 0.25 | 23 | 1834 | 0.63 | 100 | alpha_ablation_sweep |
| 0.5 | 22 | 1141 | 0.81 | 100 | alpha_ablation_sweep |
| 1.0 (RASP) | 31 | 733 | 0.92 | 100 | alpha_ablation_sweep |
| 2.0 | 36 | 2130 | 0.59 | 100 | alpha_ablation_sweep |

**Post-SFT accuracy (N=100):**
- α=0.0: 64% (eval-sft-alpha-0p0)
- α=1.0: 57% (eval-sft-alpha-1p0)
- α=2.0: 62% (eval_sft_alpha_2p0)

---

## Table 4: Sparsity Cliff at 30% (N=200)

| Method | Accuracy (%) | EOS Rate | Avg Response Len | Registry ID |
|:-------|:------------:|:--------:|:----------------:|:------------|
| Standard | 4.0 | 5.5% | 3908 | eval_postprune_standard_30 |
| RASP | 0.0 | 3.0% | 3984 | eval_postprune_rasp_30 |
| CKA-only | 0.0 | — | — | eval_postprune_cka_only_30 (killed) |

---

## Table 5: Inference Efficiency (20% sparsity)

| Config | Avg Latency (s) | Speedup vs Dense | Peak Memory (GB) | Memory Reduction | Tokens/s | Registry ID |
|:-------|:---------------:|:----------------:|:-----------------:|:----------------:|:--------:|:------------|
| Dense (unpruned) | 6.682 | — | 16.22 | — | 76.25 | inference_speedup_plan016_v2 |
| Standard 20% | 6.167 | 7.7% | 11.61 | 28.4% | 49.78 | inference_speedup_plan016_v2 |
| RASP 20% | 4.156 | 37.8% | 11.60 | 28.5% | 52.07 | inference_speedup_plan016_v2 |

---

## Table 6: SFT Recovery Gradient (N=1319, greedy)

| Method | SFT Accuracy (%) | Stderr | Registry ID |
|:-------|:-----------------:|:------:|:------------|
| Unpruned | 81.27 | ±1.07 | eval_sft_unpruned_full |
| CKA-only | 63.91 | ±1.32 | eval_sft_cka_only_20_n1319 |
| RASP | 61.49 | ±1.34 | eval_sft_rasp_full_westd |
| Standard | 59.29 | ±1.35 | eval_sft_standard_full_westd |

**SFT ranking:** CKA-only > RASP > Standard (differs from GRPO ranking in bottom half)

---

## Source Experiments (Registry IDs)

| Table | Experiment IDs | Config |
|:------|:---------------|:-------|
| 1 (Recovery Gradient) | grpo_cka_only_20, grpo_random_20, grpo_standard_20_fair, grpo_rasp_20_fair, grpo_unpruned_v2 | Fair v5: lr=1e-6, β=0.01, T=0.4 |
| 2 (Decoupling) | eval_sft_*_full, eval_grpo_*_step* | N=1319 greedy |
| 3 (α Ablation) | alpha_ablation_sweep, eval-sft-alpha-* | N=100 |
| 4 (Sparsity Cliff) | eval_postprune_*_30 | N=200, 30% sparsity |
| 5 (Inference) | inference_speedup_plan016_v2 | Single GPU bench |
| 6 (SFT Gradient) | eval_sft_*_n1319, eval_sft_*_full_westd | N=1319 greedy |
