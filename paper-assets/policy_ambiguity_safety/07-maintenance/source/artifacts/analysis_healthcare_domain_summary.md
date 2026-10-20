# Healthcare Domain Cross-Validation Results

## Overall Effect
- **Ambiguous violation rate**: 60.0%
- **Unambiguous violation rate**: 1.2%
- **Δpp**: +58.8 pp
- **McNemar OR**: inf, χ²=147.00, p=0.00e+00
- **Discordant pairs**: b=147 (amb+, unamb−), c=0 (amb−, unamb+)

## Per-Type Effects
| Type | Amb Rate | Unamb Rate | Δpp | p |
|------|----------|------------|-----|---|
| scopal | 67.5% | 0.0% | +67.5 | 0.0000 |
| lexical | 67.5% | 0.0% | +67.5 | 0.0000 |
| coreferential | 47.5% | 0.0% | +47.5 | 0.0000 |
| incompleteness | 62.5% | 0.0% | +62.5 | 0.0000 |
| conditional_precedence | 33.3% | 0.0% | +33.3 | 0.0001 |
| authorization_scope | 82.2% | 6.7% | +75.6 | 0.0000 |

## Per-Model Effects
| Model | Amb Rate | Unamb Rate | Δpp |
|-------|----------|------------|-----|
| gpt-5.4 | 66.0% | 0.0% | +66.0 |
| gpt-4.1 | 56.0% | 2.0% | +54.0 |
| claude-sonnet-4-6 | 50.0% | 2.0% | +48.0 |
| qwen3-235b | 58.0% | 2.0% | +56.0 |
| deepseek-v3 | 70.0% | 0.0% | +70.0 |

## Comparison with τ²-bench
- τ²-bench (customer service, multi-turn): +34.0 pp
- Healthcare (single-turn): +58.8 pp
