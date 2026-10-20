# exp_028 Post-Processing Report: Few-NERD 5-Epoch Convergence Test

**Date**: 2026-05-18
**Hypothesis**: Few-NERD's low degeneracy (~11%) at 3 epochs is a structural property of the dataset, not under-convergence.
**Verdict**: ❌ NEGATIVE — Hypothesis rejected.

---

## 1. Training Summary

| Metric | Value |
|--------|-------|
| Epochs completed | 5.0 |
| Total steps | 41,180 |
| Final train loss | 0.0189 |
| Final eval loss (best ckpt) | 0.0311 |
| Best checkpoint | step 32,000 (epoch ~3.9) |
| Training runtime | 7h 27m |
| Model | Qwen3-8B + LoRA |
| GPUs | 4× RTX 5090 |

### Loss Curve (train loss at epoch boundaries)
- Epoch 1: 0.0506
- Epoch 2: 0.0374
- Epoch 3: 0.0239
- Epoch 4: 0.0113
- Epoch 5: 0.0044

### Eval Loss Curve
- Best eval: 0.0311 at step 32,000 (epoch ~3.9)
- Epoch 5 eval: 0.0407 (overfitting after epoch ~3)
- `load_best_model_at_end=true` selected checkpoint-32000

**Key observation**: Train loss continued decreasing through epoch 5, but eval loss increased after epoch 3, confirming the model was overfitting on later epochs. The evaluated model is the best checkpoint (epoch ~3.9).

---

## 2. Core Metrics: 5-Epoch vs 3-Epoch Comparison

| Metric | exp_021 (3-epoch) | exp_028 (5-epoch) | Delta |
|--------|:-----------------:|:-----------------:|:-----:|
| **Degeneracy (CF1 gold-filtered)** | **11.08%** | **31.33%** | **+20.25pp** |
| Greedy F1 | 0.7478 | 0.7773 | +2.95pp |
| Oracle F1 | 0.8692 | 0.8723 | +0.31pp |
| Headroom (Oracle - Greedy) | 12.14pp | 9.50pp | -2.64pp |
| LP selection F1 | 0.7614 | 0.7835 | +2.21pp |
| LP selection Δ (LP - Greedy) | +1.37pp | +0.62pp | -0.75pp |
| Within-instance ρ(LP, F1) mean | 0.5241 | 0.4066 | -0.1175 |
| Within-instance ρ(LP, F1) median | 0.6667 | 0.6151 | -0.0516 |

---

## 3. Detailed Signal Metrics (exp_028)

### QE Signal Performance (global)
| Signal | Spearman ρ | AUROC | Selection F1 | Selection Δ |
|--------|:----------:|:-----:|:------------:|:-----------:|
| LP | 0.4495 | 0.5234 | 0.7835 | +0.62pp |
| SJ | 0.3777 | 0.4988 | 0.7697 | -0.77pp |
| FK | 0.3892 | 0.4985 | 0.7693 | -0.80pp |
| EM | 0.3893 | 0.4951 | 0.7663 | -1.10pp |
| VC | 0.3585 | 0.5006 | 0.7576 | -1.97pp |

### Within-Instance ρ(LP, F1)
- Mean: 0.4066
- Median: 0.6151
- Std: 0.5506
- Valid instances: 2988 / 4351 (68.67%)

### LP Range
- Mean: 0.0514
- Median: 0.0318
- Std: 0.0673

### Degeneracy Breakdown
- Gold-filtered instances: 4,351 / 5,000
- Constant F1 count: 1,363
- Rate: 31.33%

---

## 4. Interpretation

### Why degeneracy tripled (11% → 31%)
The 5-epoch model (best at epoch ~3.9) learned the Few-NERD patterns better (greedy F1 +2.95pp), making its N=8 samples more concentrated around correct answers. This concentration increases the fraction of instances where all 8 samples produce identical F1 scores (constant F1 = degenerate).

### Implications for paper narrative
1. **Cannot claim** Few-NERD has "structural" low degeneracy — it was under-convergence at 3 epochs.
2. **LP selection effectiveness drops** as degeneracy increases: +1.37pp → +0.62pp. This is expected — when more samples are identical, selection has less room to improve.
3. **Greedy F1 improved significantly** (+2.95pp), confirming the model genuinely learned more with additional training.
4. **Within-instance ρ mean decreased** (0.5241 → 0.4066), but **median barely changed** (0.6667 → 0.6151, Δ=-0.05), indicating alignment is dataset-intrinsic while degeneracy is convergence-dependent.

### Threshold assessment
- ≤15%: Confirms intrinsic property → **NOT MET**
- 15-20%: Borderline → **NOT MET**  
- **>20%: Needs narrative revision → MET (31.3%)**

---

## 5. Conclusion

**Hypothesis REJECTED.** Few-NERD's low degeneracy at 3 epochs was an artifact of under-convergence. With better training (5 epochs, best checkpoint at ~epoch 3.9), degeneracy rises to 31.3%, consistent with the pattern seen in other well-trained models. The paper narrative that presents Few-NERD as a structurally low-degeneracy dataset needs revision.

**Recommended actions:**
- Reframe Few-NERD results: acknowledge convergence-dependence of degeneracy
- Consider using 5-epoch model as the canonical Few-NERD baseline
- Update any claims about "dataset-intrinsic" degeneracy variation
