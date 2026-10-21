# exp_expanded_downstream_eval — Final Results Table
## Metric Standard: PIQA=acc_norm, ARC-C=acc_norm, WinoGrande=acc, TruthfulQA=mc2, GSM8K=exact_match(strict)
## Source: data_consistency_snapshot_final.json on cqa1-22115

### Individual Runs

| Config | PIQA | ARC-C | WinoGrande | TruthfulQA | GSM8K |
|--------|------|-------|------------|------------|-------|
| base_model | 0.7612 | 0.5486 | 0.6456 | 0.4659 | 0.6224 |
| no_filter_s0 | 0.7541 | 0.5128 | 0.6519 | 0.4224 | 0.5610 |
| no_filter_s1 | 0.7497 | 0.5213 | 0.6456 | 0.4237 | 0.5716 |
| no_filter_s2 | 0.7519 | 0.5239 | 0.6480 | 0.4277 | 0.5671 |
| binary_ours_s0 | 0.7465 | 0.5196 | 0.6385 | 0.4359 | 0.5861 |
| binary_ours_s1 | 0.7497 | 0.5188 | 0.6425 | 0.4456 | 0.5853 |
| binary_ours_s2 | 0.7476 | 0.5128 | 0.6409 | 0.4378 | 0.5853 |
| graduated_s0 | 0.7530 | 0.5128 | 0.6488 | 0.4225 | 0.5572 |
| graduated_s1 | 0.7503 | 0.5230 | 0.6440 | 0.4234 | 0.5618 |
| graduated_s2 | 0.7497 | 0.5213 | 0.6456 | 0.4275 | 0.5648 |

### Mean ± Std (3 seeds)

| Benchmark | Base | no_filter | binary_ours | graduated | binary-nf Δ |
|-----------|------|-----------|-------------|-----------|-------------|
| PIQA | 0.7612 | 0.7519±0.0022 | 0.7479±0.0016 | 0.7510±0.0018 | -0.40pp |
| ARC-C | 0.5486 | 0.5193±0.0058 | 0.5171±0.0037 | 0.5190±0.0055 | -0.22pp |
| WinoGrande | 0.6456 | 0.6485±0.0032 | 0.6406±0.0020 | 0.6461±0.0024 | -0.79pp |
| TruthfulQA | 0.4659 | 0.4246±0.0028 | 0.4398±0.0051 | 0.4245±0.0027 | +1.52pp |
| GSM8K | 0.6224 | 0.5666±0.0053 | 0.5856±0.0005 | 0.5613±0.0038 | +1.90pp |

### Degradation from Base (pp)

| Benchmark | no_filter | binary_ours | graduated |
|-----------|-----------|-------------|-----------|
| PIQA | -0.93 | -1.33 | -1.02 |
| ARC-C | -2.93 | -3.15 | -2.96 |
| WinoGrande | +0.29 | -0.50 | +0.05 |
| TruthfulQA | -4.13 | -2.61 | -4.14 |
| GSM8K | -5.58 | -3.66 | -6.11 |
