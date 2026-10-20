# GSM8K Token Length Stratification Analysis

## Hypothesis
Reasoning chain length (generation token count) explains the strategy specificity ratio decay observed between MATH-500 (15–36×) and GSM8K (1.1–2.2×).

## Method
- 50 GSM8K problems profiled with DS (DeepSeek-R1-Distill-Qwen-7B) and QW (Qwen2.5-7B-Instruct)
- Each model profiled under importance masking and random masking
- Split 50 problems by median generation token length into short group (bottom 25) and long group (top 25)
- Strategy specificity ratio = |II_low − II_high|_importance / |II_low − II_high|_random per matched problem
- Mann-Whitney U test (one-sided: long > short) across sparsity levels s ∈ {0.15, 0.20, 0.25, 0.30}

## Results

### 1. Token Length Distribution

| Model | Group | Mean | Median | Range |
|-------|-------|------|--------|-------|
| DS | Short (n=25) | 816 | 888 | [287, 1116] |
| DS | Long (n=25) | 1849 | 2047 | [1241, 2047] |
| QW | Short (n=25) | 2047 | 2047 | [2047, 2047] |
| QW | Long (n=25) | 2047 | 2047 | [2047, 2047] |

**QW generates exactly 2047 tokens (max_new_tokens) for all 50 GSM8K problems.** Token length stratification is meaningless for QW — the median split is arbitrary within tied values. This itself is notable: QW consistently exhausts the generation budget on GSM8K, suggesting verbose or looping outputs.

### 2. DS Strategy Specificity Ratio by Group

| Sparsity | Short median | Long median | U-stat | p-value | Effect (r_rb) |
|----------|-------------|------------|--------|---------|---------------|
| 0.15 | 0.109 | 0.077 | 21 | 0.703 | −0.160 |
| 0.20 | 0.018 | 0.015 | 23 | 0.500 | +0.022 |
| 0.25 | 0.018 | 0.092 | 13 | 0.278 | +0.300 |
| 0.30 | 179.3 | 0.077 | — | — | — |

No significant difference at any sparsity level. At s=0.15 and s=0.20, short problems actually have slightly higher ratios (opposite direction). s=0.30 has too few matched pairs for testing.

### 3. Phase Segmentation Quality

| Model | Group | Mean phases | Degenerate (≤2 phases) |
|-------|-------|-------------|----------------------|
| DS | Short | 13.2 | 0/25 (0%) |
| DS | Long | 25.9 | 0/25 (0%) |
| QW | Short | 16.7 | 1/25 (4%) |
| QW | Long | 18.8 | 0/25 (0%) |

Phase segmentation is healthy for both groups. Short DS problems still have 13+ phases on average — well above the minimum needed for meaningful II computation. Segmentation degradation does NOT explain the GSM8K ratio decay.

### 4. Raw Phase Gradient (DS, importance masking)

| Sparsity | Short mean | Long mean | p-value |
|----------|-----------|----------|---------|
| 0.15 | 0.023 | 2.397 | 0.516 |
| 0.20 | 0.042 | 0.179 | 0.664 |
| 0.25 | 0.058 | 29.43 | 0.105 |
| 0.30 | 72.17 | 188.2 | 0.669 |

Even raw phase gradients (before normalization by random) show no significant long > short pattern.

## Conclusion

**The token length hypothesis does NOT hold.** Evidence:

1. **DS (analyzable model)**: No significant difference in strategy specificity ratio between long and short groups at any sparsity level (all p > 0.27). Effect sizes are small and inconsistent in direction.

2. **QW (not analyzable)**: All 50 problems produce exactly 2047 tokens, preventing any stratification. The uniform max-length generation is itself a confound worth noting.

3. **Phase segmentation quality**: Short problems maintain adequate phase structure (mean 13.2 phases for DS). Segmentation degradation is ruled out as an explanation.

4. **Alternative explanations for ratio decay** should be pursued:
   - GSM8K problems may have uniformly low computational complexity regardless of output length
   - The sparsity landscape may be flatter for arithmetic vs. mathematical reasoning
   - The 2047-token ceiling creates a censoring effect for both DS (13 of 50 problems) and QW (all 50)

## Artifacts
- Analysis script: `/root/autodl-tmp/pacs/scripts/gsm8k_token_length_stratification.py`
- JSON data: `/root/autodl-tmp/pacs/analysis_output/gsm8k/gsm8k_token_length_stratification.json`
