# DetectGPT 9/9 Cell Results — Paper Patch Material

Source: detectgpt_ordinal_baseline_002 (8 cells, gpu-6000pro-2) + detectgpt_ordinal_baseline_004 (pythia_nucleus, westd-48862)

## Per-Cell 4-Class Accuracy (3 calibration methods)

| Cell | Equal-Width | CORAL | Threshold | Best |
|------|------------|-------|-----------|------|
| gpt2xl_nucleus | 28.5% | 25.0% | **40.1%** | 40.1% |
| gpt2xl_temp09 | 28.0% | 29.6% | **41.4%** | 41.4% |
| gpt2xl_topk50 | 31.1% | 26.5% | **36.9%** | 36.9% |
| olmo_nucleus | 25.9% | 24.9% | **30.9%** | 30.9% |
| olmo_temp09 | 25.4% | 25.3% | **29.8%** | 29.8% |
| olmo_topk50 | 25.3% | 25.5% | 24.3% | 25.5% |
| pythia_nucleus | 25.4% | 25.1% | **29.0%** | 29.0% |
| pythia_temp09 | **32.5%** | **33.2%** | 21.8% | 33.2% |
| pythia_topk50 | **31.8%** | **33.7%** | 20.2% | 33.7% |
| **9-cell Mean** | **28.2%** | **27.6%** | **30.5%** | — |

Chance level: 25.0%

## Comparison with Other Baselines

| Method | 9-cell Mean 4-Class Acc | Source |
|--------|------------------------|--------|
| Random chance | 25.0% | — |
| **DetectGPT** (perturbation discrepancy) | **28.8%** | 002 + 004 |
| **Min-K% Prob** (membership inference) | **33.2%** | mink_ordinal_baseline_002 |
| **DeBERTa-v3-base** (LoRA, end-to-end) | **53.1–60.6%** | deberta_pilot |
| **RF + 19 features** (ours) | **69–86%** | baseline_battery_001 |

## Paper Text Suggestion (for supplementary or §5 baseline comparison)

> We evaluate DetectGPT (Mitchell et al., 2023) as an ordinal depth baseline by computing perturbation discrepancy scores (T5-large perturbation, GPT-2 Large scoring, 5 perturbations per passage) and calibrating to 4-class depth via equal-width binning, CORAL ordinal regression, and threshold optimization. Across all 9 atlas cells, DetectGPT achieves a mean 4-class accuracy of 28.8% (chance: 25.0%), with no calibration method reliably distinguishing ordinal depth. This confirms that perturbation-based binary detection scores lack ordinal resolution.

## Notes
- methodC (threshold) shows inflated accuracy on gpt2xl cells (36-41%) but below-chance on pythia cells (20-22%), indicating threshold overfitting rather than genuine signal
- CORAL (methodB) is most stable but barely above chance
- pythia_nucleus (004) is consistent with other pythia cells — no surprise
- The 8-cell mean from 002 was 29.1%; adding pythia_nucleus (26.5%) brings it to ~28.8%
