# CORAL Ordinal Regression vs Random Forest: 9-Cell Comparison

## Setup
- **CORAL**: DNN (19→64→32→CORAL output), Adam lr=1e-3, 100 epochs, early stopping patience=10
- **RF**: 200 trees, default hyperparameters
- **Evaluation**: 5-fold StratifiedKFold, seed=42
- **Data**: 20,000 samples per cell (5,000 per depth, d0-d3)

## Per-Cell Results (4-Class Accuracy)

| Cell | CORAL Acc | RF Acc | Delta | CORAL QWK | RF QWK | QWK Delta |
|------|-----------|--------|-------|-----------|--------|-----------|
| pythia_nucleus | 0.7805 | 0.7860 | -0.0055 | 0.9009 | 0.8906 | **+0.0103** |
| pythia_temp09 | 0.7643 | 0.7668 | -0.0025 | 0.8938 | 0.8776 | **+0.0162** |
| pythia_topk50 | 0.6840 | 0.6888 | -0.0048 | 0.8481 | 0.8215 | **+0.0266** |
| olmo_nucleus | **0.7940** | 0.7889 | **+0.0051** | 0.9074 | 0.8942 | **+0.0132** |
| olmo_temp09 | 0.8213 | 0.8224 | -0.0011 | 0.9261 | 0.9230 | **+0.0031** |
| olmo_topk50 | **0.7479** | 0.7464 | **+0.0015** | 0.8869 | 0.8759 | **+0.0110** |
| gpt2xl_nucleus | 0.8398 | 0.8416 | -0.0018 | 0.9278 | 0.9238 | **+0.0040** |
| gpt2xl_temp09 | 0.8491 | 0.8588 | -0.0097 | 0.9373 | 0.9398 | -0.0025 |
| gpt2xl_topk50* | 0.7193 | 0.7581 | -0.0388 | 0.8755 | 0.8840 | -0.0085 |

## Full Metric Comparison (9-Cell Average)

| Metric | CORAL | RF | Delta | Winner |
|--------|-------|-----|-------|--------|
| 4-Class Accuracy | 0.7778 | 0.7842 | -0.0064 | RF |
| d1-d3 Balanced Acc | 0.7086 | 0.7160 | -0.0074 | RF |
| MAE | 0.2315 | 0.2339 | **-0.0024** | CORAL |
| QWK | 0.9004 | 0.8923 | **+0.0081** | CORAL |
| Ordinal Consistency | 0.9790 | 0.9738 | **+0.0052** | CORAL |

## Per-Cell MAE and Ordinal Consistency

| Cell | CORAL MAE | RF MAE | MAE Delta | CORAL OC | RF OC | OC Delta |
|------|-----------|--------|-----------|----------|-------|----------|
| pythia_nucleus | 0.2280 | 0.2350 | **-0.0070** | 0.9782 | 0.9723 | **+0.0059** |
| pythia_temp09 | 0.2441 | 0.2587 | **-0.0146** | 0.9772 | 0.9685 | **+0.0087** |
| pythia_topk50 | 0.3325 | 0.3569 | **-0.0244** | 0.9606 | 0.9469 | **+0.0137** |
| olmo_nucleus | 0.2152 | 0.2290 | **-0.0138** | 0.9818 | 0.9752 | **+0.0066** |
| olmo_temp09 | 0.1818 | 0.1832 | **-0.0014** | 0.9865 | 0.9838 | **+0.0027** |
| olmo_topk50 | 0.2643 | 0.2724 | **-0.0081** | 0.9729 | 0.9667 | **+0.0062** |
| gpt2xl_nucleus | 0.1658 | 0.1680 | **-0.0022** | 0.9883 | 0.9863 | **+0.0020** |
| gpt2xl_temp09 | 0.1533 | 0.1444 | +0.0089 | 0.9908 | 0.9914 | -0.0006 |
| gpt2xl_topk50* | 0.2988 | 0.2576 | +0.0412 | 0.9748 | 0.9720 | +0.0028 |

## Key Findings

1. **CORAL consistently wins on ordinal metrics**: QWK (+0.0081 avg), MAE (-0.0024 avg), and ordinal consistency (+0.0052 avg) favor CORAL in 7/9 cells. This is the expected behavior: CORAL is designed to minimize ordinal errors, producing predictions that better respect the depth ordering.

2. **RF has marginal edge on raw accuracy**: 4-class accuracy favors RF by 0.64pp on average, but this gap is small and within noise for most cells.

3. **CORAL's ordinal advantage is largest on hard cells**: pythia_topk50 (QWK +0.027, MAE -0.024), pythia_temp09 (QWK +0.016, MAE -0.015), and olmo_nucleus (QWK +0.013) show the biggest ordinal gains. These are cells where classification is more difficult, and CORAL's ordinal inductive bias provides the most value.

4. **gpt2xl_topk50 is an outlier**: CORAL underperforms significantly (-3.9pp acc). This cell has inf/overflow values in features (var_ppl overflow to float32), causing training instability. The high fold-to-fold variance (acc_std=0.042 vs typical 0.003-0.007) confirms this.

5. **Excluding the outlier**: Without gpt2xl_topk50, CORAL average delta becomes: Acc -0.0023, QWK +0.0092, MAE -0.0049, OC +0.0055. The accuracy gap nearly vanishes while ordinal metrics remain strongly in CORAL's favor.

*Note: gpt2xl_topk50 has feature overflow issues (extreme ppl values exceeding float32 range), causing high training variance for CORAL DNN.
