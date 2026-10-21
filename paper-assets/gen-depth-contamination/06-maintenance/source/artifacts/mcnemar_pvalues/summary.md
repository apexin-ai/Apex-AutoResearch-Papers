# McNemar Test: OBD vs Baseline Classifiers

## Task
Binary classification: depth 1 vs depth 2 (the K*=2 boundary).
5-fold GroupKFold, out-of-fold predictions, McNemar test with continuity correction.

## Classifiers Compared
- **OBD**: LightGBM (n_estimators=200, max_depth=6, lr=0.05, num_leaves=31)
- **LogReg**: Logistic Regression (C=1.0, max_iter=2000) with median imputation + StandardScaler
- **LinearSVC**: Linear SVM (C=1.0, max_iter=10000) with median imputation + StandardScaler
- **RF**: Random Forest (n_estimators=100, max_depth=8) with median imputation + StandardScaler

## Claim Verification

**Claimed**: "all McNemar p < 0.01"
**Result**: **FALSE**

- 36 total comparisons (12 configs x 3 baselines)
- Only 4/36 have p < 0.01
- Only 5/36 have p < 0.05
- 31/36 are non-significant (p >= 0.05)
- Max p-value: 0.868 (OLMo/Wiki vs LogReg)

## Significant Results (p < 0.05)

| Config | Baseline | OBD Acc | BL Acc | p-value | Direction |
|--------|----------|---------|--------|---------|-----------|
| LLaMA-8B / C4 | LogReg | .573 | .592 | 6.2e-5 | BL wins |
| LLaMA-8B / C4 | LinearSVC | .573 | .591 | 1.1e-4 | BL wins |
| LLaMA-8B / C4 | RF | .573 | .586 | 1.3e-3 | BL wins |
| Qwen-1.5B / Wiki | LogReg | .588 | .570 | 9.4e-4 | OBD wins |
| Qwen-1.5B / Wiki | LinearSVC | .588 | .568 | 2.3e-4 | OBD wins |

## Full p-value Table

| Model | Domain | n | OBD | LogReg | LinearSVC | RF |
|-------|--------|---|-----|--------|-----------|-----|
| Qwen-1.5B-base | C4 | 10000 | .592 | .232 (.598) | .605 (.595) | .271 (.597) |
| Pythia-1.4B | C4 | 10000 | .631 | .033* (.621) | .105 (.624) | .451 (.628) |
| LLaMA-8B | C4 | 10000 | .573 | 6.2e-5*** (.592) | 1.1e-4*** (.591) | .001** (.586) |
| Qwen-1.5B | Wiki | 10000 | .588 | 9.4e-4*** (.570) | 2.3e-4*** (.568) | .655 (.590) |
| Pythia | Wiki | 10000 | .560 | .180 (.567) | .540 (.564) | .369 (.564) |
| OLMo | Wiki | 10000 | .500 | .868 (.502) | .705 (.503) | .751 (.502) |
| LLaMA-8B | Wiki | 10000 | .573 | .252 (.579) | .270 (.579) | .110 (.580) |
| Qwen-1.5B | arXiv | 4400 | .781 | .156 (.774) | .079 (.772) | .364 (.777) |
| Pythia | arXiv | 4400 | .733 | .232 (.727) | .384 (.728) | .735 (.732) |
| OLMo | arXiv | 4400 | .493 | .520 (.487) | .681 (.489) | .759 (.496) |
| Qwen-7B | arXiv | 4400 | .757 | .160 (.749) | .327 (.751) | .733 (.758) |
| Mistral-7B | arXiv | 4400 | .742 | .524 (.738) | .633 (.739) | .225 (.748) |

Values: p-value (baseline accuracy). *p<.05, **p<.01, ***p<.001.

## Interpretation

The overwhelming non-significance (31/36) demonstrates that **classifier choice is not the primary driver of depth discriminability**. The 15D feature representation captures the signal; swapping LightGBM for LogReg, SVM, or RF yields statistically equivalent performance in most configurations.

Notable exceptions:
- **LLaMA-8B/C4**: Baselines significantly outperform OBD, suggesting LightGBM overfits on the noisier 8B features.
- **Qwen-1.5B/Wiki**: OBD outperforms linear models but matches RF.
- **OLMo/Wiki and OLMo/arXiv**: All classifiers at chance (~50%), consistent with OLMo's 1v2 boundary being at or below the detection threshold.

## Data Sources
- Raw JSON: `/root/autodl-tmp/gen-depth-contamination/results/mcnemar_obd_vs_baselines/mcnemar_results.json`
- Script: `/root/autodl-tmp/gen-depth-contamination/scripts/mcnemar_obd_vs_baselines.py`
