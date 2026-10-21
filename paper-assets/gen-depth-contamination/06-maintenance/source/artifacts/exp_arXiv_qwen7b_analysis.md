# exp_arXiv_qwen7b Analysis Report

## Experiment Configuration
- **Model**: Qwen2.5-7B
- **Domain**: arXiv abstracts
- **Depths tested**: 0-5
- **Classifier**: LightGBM (5-fold CV)
- **Server**: cqa1-22115
- **Results dir**: `/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_qwen7b/`
- **Log**: `~/runs/gen-depth-contamination/exp_arXiv_qwen7b.log`
- **Status**: Completed successfully (EXIT_CODE=0)

## K* Result: **3**

K* = 3 (max depth where pairwise AUC > 0.60).

## Pairwise Discrimination (Adjacent Depths)

| Depth Pair | AUC (mean) | AUC (std) | JSD |
|---|---|---|---|
| 0 vs 1 | 0.983 | 0.0037 | 0.1656 |
| 1 vs 2 | 0.835 | 0.0088 | 0.0668 |
| 2 vs 3 | 0.626 | 0.0085 | 0.0156 |
| **3 vs 4** | **0.544** | **0.0220** | **0.0089** |
| 4 vs 5 | 0.513 | 0.0212 | 0.0061 |

Saturation point: depth 3 vs 4 AUC = 0.544 (< 0.60 threshold), confirming K*=3.

## Ordinal Classification (6-class)
- MAE: 0.900
- Accuracy: 44.6%

## Top-5 Feature Importance
1. freq_entropy (9813.2)
2. surp_std (8233.6)
3. surp_mean (7342.6)
4. surp_d1_skew (7204.8)
5. freq_kurtosis (7105.0)

## Cross-Model Comparison (arXiv domain, K*)

| Model | Size | Domain | K* | 0v1 AUC | 1v2 AUC | 2v3 AUC | 3v4 AUC |
|---|---|---|---|---|---|---|---|
| Qwen2.5-1.5B | 1.5B | arXiv | 3 | - | - | - | - |
| Pythia-1.4B | 1.4B | arXiv | 3 | - | - | - | - |
| LLaMA-3.1-8B | 8B | arXiv | 3 | - | - | - | - |
| Mistral-7B | 7B | arXiv | 3 | - | - | - | - |
| **Qwen2.5-7B** | **7B** | **arXiv** | **3** | **0.983** | **0.835** | **0.626** | **0.544** |

## Conclusion: **SUCCESS**

Qwen2.5-7B arXiv K*=3, confirming:
1. Structured domain (arXiv) K*=3 is stable across the Qwen family (1.5B and 7B both yield K*=3)
2. K*=3 for arXiv is now validated across 5 models spanning 4 architectures (Pythia, LLaMA, Mistral, Qwen) and 3 scale tiers (1.4B, 1.5B, 7B, 8B)
3. The domain property (structured academic text) dominates over model architecture and scale in determining K*
