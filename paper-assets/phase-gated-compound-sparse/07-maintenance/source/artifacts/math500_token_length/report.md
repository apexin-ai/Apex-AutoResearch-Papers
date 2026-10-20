# MATH-500 Token Length Stratification Analysis

## Hypothesis
Longer reasoning chains produce higher strategy specificity — the gap between importance-based and random phase gradients should grow with generation length.

## Method
- **Metric**: Per-problem strategy specificity = |grad_importance - grad_random|, where grad = II_high - II_low
- **Stratification**: Median split (short/long) and quartile split (Q1-Q4) by generation token count
- **Tests**: Mann-Whitney U (one-sided: long > short), Spearman rank correlation (per-problem tokens vs |specificity|), Spearman trend (quartile medians)
- **Data**: MATH-500 n=500 (DeepSeek-R1-Distill-Qwen-7B), GSM8K n=50

## Key Results

### MATH-500: Hypothesis supported

| Sparsity | Short |spec| | Long |spec| | MW p-value | MW r | Corr rho | Corr p |
|----------|--------------|-------------|------------|------|----------|--------|
| 0.15     | 0.423        | 0.603       | 0.003 **   | 0.12 | 0.096    | 0.032 *|
| 0.20     | 1.302        | 1.796       | 0.0002 *** | 0.16 | 0.132    | 0.003 **|
| 0.25     | 4.447        | 6.235       | 0.001 **   | 0.14 | 0.120    | 0.008 **|
| 0.30     | 10.946       | 14.261      | 0.013 *    | 0.10 | 0.085    | 0.058  |

- Long group has 30-43% higher median |specificity| than short group
- Effect consistent across all sparsity levels
- Per-problem Spearman correlation significant at s015-s025, marginal at s030

### MATH-500 Quartile Split

| Q  | n   | Tokens       | |spec|@0.15 | |spec|@0.20 | |spec|@0.25 | |spec|@0.30 |
|----|-----|--------------|-------------|-------------|-------------|-------------|
| Q1 | 125 | [198, 779]   | 0.512       | 1.519       | 4.689       | 13.856      |
| Q2 | 125 | [789, 1433]  | 0.392       | 1.007       | 4.229       | 9.255       |
| Q3 | 125 | [1451, 2047] | 0.559       | 1.576       | 5.162       | 12.657      |
| Q4 | 125 | [2047, 2047] | 0.674       | 1.949       | 7.770       | 17.540      |

- Q4 (all truncated at 2047) consistently highest
- Q2 dip: mid-length problems show lowest specificity — possible floor effect for moderate-difficulty problems
- Non-monotonic Q1→Q2 dip suggests short simple problems can also have structured reasoning patterns

### GSM8K: Opposite direction

| Sparsity | Short |spec| | Long |spec| | Trend rho | Corr rho |
|----------|--------------|-------------|-----------|----------|
| 0.15     | 0.533        | 0.458       | -0.80     | -0.27    |
| 0.20     | 0.831        | 1.161       | -0.40     | -0.15    |
| 0.25     | 5.671        | 1.950       | -1.00 *** | -0.31 *  |
| 0.30     | 11.289       | 5.403       | -1.00 *** | -0.40 ** |

- GSM8K shows DECREASING specificity with longer generations
- Statistically significant negative trend at s025, s030
- Consistent negative per-problem correlations

## Cross-benchmark Token Length Comparison

| Benchmark      | Mean tokens | Median | Range       |
|----------------|-------------|--------|-------------|
| MATH-500 all   | 1397        | 1442   | [198, 2047] |
| MATH-500 short | 809         | 784    | [198, 1433] |
| MATH-500 long  | 1984        | 2047   | [1451, 2047]|
| GSM8K all      | 723         | 540    | [254, 2047] |

**GSM8K median (540) falls within MATH-500 short range [198, 1433]**: YES

Cross-benchmark |specificity| comparison:

| Sparsity | M500-Short | M500-Long | GSM-Short | GSM-Long |
|----------|-----------|-----------|-----------|----------|
| 0.15     | 0.423     | 0.603     | 0.533     | 0.458    |
| 0.20     | 1.302     | 1.796     | 0.831     | 1.161    |
| 0.25     | 4.447     | 6.235     | 5.671     | 1.950    |
| 0.30     | 10.946    | 14.261    | 11.289    | 5.403    |

## Interpretation

1. **MATH-500 supports the length hypothesis** — longer generations show significantly stronger strategy specificity, consistent with the idea that extended reasoning chains amplify the structural differences between importance-based and random pruning.

2. **GSM8K contradicts the simple length hypothesis** — shorter GSM8K problems show HIGHER specificity. This is likely because:
   - GSM8K problems are inherently simpler; short problems may have tighter, more structured reasoning
   - Long GSM8K generations (many truncated at 2047) may reflect the model struggling or exploring, diluting phase structure
   - Small sample (n=50) amplifies noise

3. **The relationship is benchmark-dependent**, suggesting that generation length alone doesn't explain strategy specificity. Task complexity and reasoning structure quality are confounding factors.

4. **Truncation artifact**: Q4 in MATH-500 (all at 2047 tokens) shows the highest specificity. These are truncated generations — the model ran out of max_tokens. This could inflate specificity because truncated generations are systematically different (harder problems, longer reasoning). Caution warranted.

5. **Revised hypothesis**: Strategy specificity scales with effective reasoning depth (task complexity × chain length), not raw length alone. MATH-500's length heterogeneity better captures this because its difficulty distribution is wider.

## Files
- Analysis script: `/root/autodl-tmp/pacs/analysis/math500_token_length_stratification.py`
- JSON data: `/root/autodl-tmp/pacs/analysis_output/math500_token_length_stratification.json`
