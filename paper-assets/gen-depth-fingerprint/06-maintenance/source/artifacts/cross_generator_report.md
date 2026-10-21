# 跨生成器分类评估报告 (plan-002)

## 1. Leave-One-Generator-Out CV

| Generator | Macro-F1 | 95% CI | gen-0 F1 | gen-1 F1 | gen-2+ F1 |
|-----------|----------|--------|----------|----------|-----------|
| olmo-2-1b | 0.7519 | [0.7402, 0.7622] | 0.9305 | 0.5834 | 0.7416 |
| pythia-1b | 0.8507 | [0.8414, 0.8610] | 0.9827 | 0.7070 | 0.8624 |
| pythia-2.8b | 0.7983 | [0.7870, 0.8094] | 0.9688 | 0.6365 | 0.7894 |
| qwen3-0.6b | 0.8209 | [0.8100, 0.8323] | 0.9575 | 0.6707 | 0.8345 |
| qwen3-1.7b | 0.7969 | [0.7856, 0.8078] | 0.9153 | 0.6529 | 0.8224 |
| **Average** | **0.8037** | | | | |

## 2. Leave-One-Family-Out

| Setting | Macro-F1 | 95% CI |
|---------|----------|--------|
| Train non-Pythia → Test Pythia | 0.7720 | [0.7638, 0.7800] |
| Train Pythia → Test non-Pythia | 0.7613 | [0.7542, 0.7683] |

Δ (non-Pythia-trained − Pythia-trained) = +0.0107

## 3. Feature Ablation

| Feature Set | Avg Macro-F1 |
|-------------|-------------|
| full | 0.8037 |
| surface_only | 0.7471 |
| reference_only | 0.7543 |

McNemar p-values: full vs surface = 0.000000, full vs reference = 0.000000

## 4. Permutation Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | hapax_ratio | 0.2893 |
| 2 | ttr | 0.1682 |
| 3 | entropy_mean | 0.1601 |
| 4 | entropy_max | 0.0579 |
| 5 | entropy_std | 0.0514 |
| 6 | entropy_min | 0.0162 |
| 7 | tail_decay | 0.0096 |

## 5. entropy_std 专项分析

- entropy_std drift (d0−d4 avg): 0.1197
- entropy_mean drift (d0−d4 avg): 1.4966
- LOGO macro-F1 with all features: 0.8037
- LOGO macro-F1 without entropy_std: 0.7988
- Δ macro-F1: +0.0049
- **结论**: entropy_std 对跨生成器泛化贡献极小，更可能是 H1（模型特有 artifact）
