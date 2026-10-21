# Re-DocRED Test Set Results Compilation

> Generated: 2026-05-22 | Source: registry experiments (faith-evidence-ie)

## Table 1: Test Set Main Results

| Scale | SFT ign_f1 | RSFT ign_f1 | Δ(RSFT−SFT) | Trunc (SFT) | Trunc (RSFT) | Format OK (SFT) | Format OK (RSFT) |
|-------|-----------|------------|-------------|-------------|--------------|-----------------|------------------|
| 1.7B | ⏳ | 0.2933 | — | ⏳ | 369/500 (73.8%) | ⏳ | 500/500 (100%) |
| 4B | 0.2232 | 0.2501 | +2.69 pp | 323/500 (64.6%) | 214/500 (42.8%) | 497/500 (99.4%) | 499/500 (99.8%) |
| 8B | 0.3106 | 0.3353 | +2.47 pp | 410/500 (82.0%) | 9/500 (1.8%) | 498/500 (99.6%) | 499/500 (99.8%) |
| 14B | 0.3886 | 0.3849 | −0.37 pp | 253/500 (50.6%) | 67/500 (13.4%) | 499/500 (99.8%) | 499/500 (99.8%) |
| LLaMA-8B | 0.3420 | 0.3599 | +1.79 pp | 327/500 (65.4%) | 283/500 (56.6%) | 490/500 (98.0%) | 500/500 (100%) |

### Registry Sources (Table 1)

| Scale | SFT Experiment | RSFT Experiment |
|-------|---------------|-----------------|
| 1.7B | test_eval_1_7b_sft_s42 (RUNNING) | test_eval_1_7b_rsft_s42 |
| 4B | test_eval_4b_sft_s42 | test_eval_4b_rsft_s42_v2 |
| 8B | test_eval_8b_sft_s42 | test_eval_8b_rsft_s42 |
| 14B | test_eval_14b_sft_s42 | test_eval_14b_rsft_s42 |
| LLaMA-8B | test_eval_llama_sft_s42 | test_eval_llama_rsft_s42 |

---

## Table 2: Test Set Evidence Tax Spot-Check

| Scale | With-Evi Test ign_f1 | No-Evi Test ign_f1 | Test Tax (pp) | Dev Tax (pp) | Consistent? |
|-------|---------------------|--------------------|--------------|--------------:|-------------|
| 1.7B | ⏳ | ⏳ | — | −5.63 | ⏳ |
| 8B | 0.3106 | ⏳ | — | +0.04 | ⏳ |
| 14B | 0.3886 | ⏳ | — | +0.03 | ⏳ |

### Registry Sources (Table 2)

| Scale | With-Evi Experiment | No-Evi Experiment | Dev Tax Source |
|-------|--------------------|--------------------|----------------|
| 1.7B | test_eval_1_7b_sft_s42 (RUNNING) | test_eval_1_7b_sft_s42_no_evi (RUNNING) | d140_1_7b_sft_s42_no_evi_2048_fix (fair_tax_pp=−5.6306) |
| 8B | test_eval_8b_sft_s42 | test_eval_8b_sft_s42_no_evi (RUNNING) | d140_8b_sft_s42_no_evi_2048_fix (fair_tax_pp=+0.042) |
| 14B | test_eval_14b_sft_s42 | test_eval_14b_sft_s42_no_evi (RUNNING) | plan017_14b_sft dev: 0.5507 vs no_evi 0.5510 → +0.03pp |

### Tax Convention
- Tax = no_evi_ign_f1 − with_evi_ign_f1
- Positive → evidence hurts (performance tax)
- Negative → evidence helps (no tax)

---

## Notes

1. **1.7B SFT test** (test_eval_1_7b_sft_s42): still RUNNING as of 2026-05-22. Once complete, fill in Table 1 row and compute Δ.
2. **All no-evidence test evals** (D147 spot-checks): still RUNNING. Once complete, compute test tax and check consistency with dev.
3. **8B RSFT truncation anomaly**: only 9/500 (1.8%) truncated vs 410/500 (82%) for SFT. This is because RSFT model learned more concise outputs (fewer predictions: 14,616 vs implied higher count for SFT).
4. **14B RSFT slightly below SFT** (−0.37pp): consistent with dev trend where 14B RSFT ≈ SFT. May reflect ceiling effect at this scale.
5. **4B RSFT uses retrain v2** (test_eval_4b_rsft_s42_v2): original v1 had issues, retrained model used for final test.
