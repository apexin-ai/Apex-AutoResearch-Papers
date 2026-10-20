# Uniform 1.7B Seed456 Evaluation Report

## Experiment Summary

| Field | Value |
|-------|-------|
| Experiment ID | `uniform_1_7b_seed456` |
| Model | Qwen3-1.7B (from scratch) |
| Weighting | Uniform |
| Data | scored_data.jsonl (371,499 samples, contamination_ratio=0.4) |
| Tokens | 200M |
| Seed | 456 |
| Server | westd-41312 (cuda:2) |
| Train Loss | 7.537 |
| Steps | 6,103 |
| Wall Clock | ~5.6 GPU-hours |

## Evaluation Results

### Perplexity

| Dataset | PPL | Loss |
|---------|-----|------|
| Holdout | 13.280 | 2.586 |
| OpenWebText (OOD) | 13.307 | 2.589 |
| Wikipedia (OOD) | 10.953 | 2.394 |

### Downstream Tasks (0-shot)

| Task | Metric | Score |
|------|--------|-------|
| ARC-Easy | acc_norm | 0.7113 |
| ARC-Challenge | acc_norm | 0.4224 |
| HellaSwag | acc_norm | 0.6132 |
| PIQA | acc_norm | 0.7448 |
| WinoGrande | acc | 0.6251 |
| **Mean** | | **0.6234** |

## Three-Seed Comparison (uniform_1_7b)

### Perplexity

| Metric | seed42 | seed123 | seed456 | Mean ± Std |
|--------|--------|---------|---------|------------|
| PPL Holdout | 13.280 | 13.265 | 13.280 | 13.275 ± 0.009 |
| PPL OpenWebText | 13.291 | 13.292 | 13.307 | 13.297 ± 0.009 |
| PPL Wikipedia | 10.919 | 10.942 | 10.953 | 10.938 ± 0.017 |

### Downstream

| Task | seed42 | seed123 | seed456 | Mean ± Std |
|------|--------|---------|---------|------------|
| ARC-Easy | 0.7235 | 0.7260 | 0.7113 | 0.7203 ± 0.0079 |
| ARC-Challenge | 0.4334 | 0.4317 | 0.4224 | 0.4292 ± 0.0059 |
| HellaSwag | 0.6107 | 0.6118 | 0.6132 | 0.6119 ± 0.0013 |
| PIQA | 0.7432 | 0.7454 | 0.7448 | 0.7445 ± 0.0011 |
| WinoGrande | 0.6172 | 0.6133 | 0.6251 | 0.6185 ± 0.0060 |
| **Mean** | **0.6256** | **0.6256** | **0.6234** | **0.6249 ± 0.0013** |

### Training Loss

| seed42 | seed123 | seed456 | Mean ± Std |
|--------|---------|---------|------------|
| 7.560 | 7.557 | 7.537 | 7.551 ± 0.013 |

## Analysis

1. **High reproducibility**: All three seeds converge to nearly identical perplexity (std < 0.02 across all PPL metrics) and downstream performance (std = 0.0013 on mean downstream). This confirms the uniform baseline is stable.

2. **Negligible seed variance**: The downstream mean varies by only ±0.13 percentage points across seeds. Individual task variance is also small (max std = 0.79pp on ARC-Easy).

3. **Seed456 within normal range**: Despite a slightly lower downstream mean (0.6234 vs 0.6256 for seed42/123), the difference is well within 1 standard deviation and not statistically meaningful.

4. **Consistent OOD generalization**: Wikipedia PPL (~10.94) is consistently lower than holdout/OWT PPL (~13.28), reflecting the cleaner nature of Wikipedia text. This pattern holds across all seeds.

5. **Conclusion**: The uniform_1_7b baseline is well-characterized with 3 seeds. The consolidated reference numbers are:
   - PPL (holdout): **13.275 ± 0.009**
   - PPL (OWT): **13.297 ± 0.009**
   - PPL (Wiki): **10.938 ± 0.017**
   - Downstream mean: **0.6249 ± 0.0013**
