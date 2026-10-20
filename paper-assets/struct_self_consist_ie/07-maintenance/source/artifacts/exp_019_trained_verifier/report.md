# exp-019: Trained Verifier Baseline (Logistic Regression)

Seeds: [42, 123, 789], Dataset: SciERC NER, N=8, Qwen2.5-7B-Instruct

## 1. Selection F1 Comparison

| Method | seed42 | seed123 | seed789 | Mean ± σ |
|--------|--------|---------|---------|----------|
| Greedy | 0.6439 | 0.6457 | 0.6511 | 0.6469 ± 0.0037 |
| SJ (unsup) | 0.6450 | 0.6475 | 0.6378 | 0.6434 ± 0.0050 |
| FK (unsup) | 0.6448 | 0.6468 | 0.6410 | 0.6442 ± 0.0029 |
| LP (unsup) | 0.6501 | 0.6436 | 0.6478 | 0.6472 ± 0.0033 |
| EM (unsup) | 0.6362 | 0.6381 | 0.6406 | 0.6383 ± 0.0022 |
| VC (unsup) | 0.6256 | 0.6204 | 0.6195 | 0.6218 ± 0.0033 |
| **LR (supervised)** | 0.6484 | 0.6467 | 0.6490 | **0.6480 ± 0.0012** |
| Oracle | 0.7758 | 0.7805 | 0.7885 | 0.7816 ± 0.0064 |

Oracle gap: 0.1347
LR gain over greedy: +0.0011
LR vs best unsupervised (LP): +0.0009
Gap closure: 0.8%

## 2. Instance-level AUROC

| Method | seed42 | seed123 | seed789 | Mean ± σ |
|--------|--------|---------|---------|----------|
| SJ | 0.6715 | 0.6919 | 0.6893 | 0.6842 ± 0.0111 |
| FK | 0.6154 | 0.6300 | 0.6020 | 0.6158 ± 0.0140 |
| LP | 0.6116 | 0.6132 | 0.6124 | 0.6124 ± 0.0008 |
| EM | 0.6472 | 0.6596 | 0.6468 | 0.6512 ± 0.0073 |
| VC | 0.6879 | 0.7089 | 0.7223 | 0.7064 ± 0.0173 |
| **LR (5 signals)** | 0.6795 | 0.7016 | 0.7109 | **0.6973 ± 0.0161** |

LR vs best single signal (VC): -0.0090

## 3. Feature Importance (LR Coefficients)

| Signal | seed42 | seed123 | seed789 | Mean ± σ |
|--------|--------|---------|---------|----------|
| SJ | -0.1739 | -0.0996 | -0.0845 | -0.1193 ± 0.0479 |
| FK | 0.0925 | 0.1324 | 0.0432 | 0.0894 ± 0.0447 |
| LP | 0.1161 | 0.0914 | 0.1073 | 0.1049 ± 0.0125 |
| EM | 0.1913 | 0.1588 | -0.0438 | 0.1021 ± 0.1274 |
| VC | 0.6455 | 0.6768 | 0.9198 | 0.7474 ± 0.1501 |

## 4. Ablation (Leave-One-Signal-Out AUROC)

| Dropped | seed42 AUROC | seed123 AUROC | seed789 AUROC | Mean Δ |
|---------|-------------|---------------|---------------|--------|
| w/o SJ | 0.6814 | 0.7036 | 0.7128 | -0.0019 |
| w/o FK | 0.6802 | 0.7016 | 0.7123 | -0.0007 |
| w/o LP | 0.6788 | 0.7007 | 0.7074 | +0.0017 |
| w/o EM | 0.6780 | 0.7011 | 0.7131 | -0.0000 |
| w/o VC | 0.6577 | 0.6781 | 0.6774 | +0.0263 |
| All 5 | 0.6795 | 0.7016 | 0.7109 | — |

## 5. Learning Curve (Instance-level AUROC)

| % Data | Mean AUROC ± σ |
|--------|----------------|
| 10% | 0.5965 ± 0.0231 |
| 25% | 0.6977 ± 0.0260 |
| 50% | 0.6870 ± 0.0234 |
| 75% | 0.7001 ± 0.0191 |
| 100% | 0.6973 ± 0.0161 |

## 6. Interpretation

- LR AUROC does NOT exceed best single signal → signals are largely redundant.

- Supervised LR selection F1 marginally exceeds best unsupervised by +0.0009.

- Gap closure: 0.8% of the oracle gap closed by supervised LR.
