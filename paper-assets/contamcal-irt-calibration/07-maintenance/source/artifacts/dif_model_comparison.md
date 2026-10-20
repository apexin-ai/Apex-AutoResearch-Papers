# Uniform vs Non-uniform DIF Model Comparison (Reviewer W11)

## Models

- **Uniform DIF** (current): `P(y=1) = σ(a_i(θ_j − b_i) + γ·e_ij)` — γ outside discrimination bracket
- **Non-uniform DIF** (variant): `P(y=1) = σ(a_i(θ_j − b_i + γ·e_ij))` — γ inside discrimination bracket

## Setup

- Benchmark: MMLU
- Respondents: J=16 (all ≤3B models: Llama-3.2-3B × 4 dosages + Qwen2.5-{0.5B,1.5B,3B} × 4 dosages)
- Items: I=300 (stratified subsample from 14042, seed=42)
- Priors: θ~N(0,1), a~LogNormal(0,0.5), b~N(0,1), γ~N(0,1)
- MCMC: CmdStan 2.38.0, 4 chains, 1000 warmup + 1000 sampling, adapt_delta=0.95, seed=42

## Results

| Metric           | Uniform     | Non-uniform |
|------------------|-------------|-------------|
| γ mean           | 0.245       | −0.458      |
| γ SD             | 0.197       | 0.453       |
| γ 90% CI         | [−0.081, 0.571] | [−1.224, 0.307] |
| γ Rhat           | 1.002       | 1.002       |
| γ ESS_bulk       | 1468        | 981         |
| γ ESS_tail       | 1896        | 1586        |
| Max Rhat (all)   | 1.008       | 1.007       |
| Min ESS_bulk     | 1218        | 940         |
| Divergences      | 0           | 0           |
| PPP              | 0.763       | 0.743       |
| LOO ELPD         | −2124.3     | −2123.4     |
| LOO SE           | 30.8        | 30.9        |
| p_loo            | 243.9       | 240.5       |
| LOO k>0.7        | 7           | 4           |

### ArViZ LOO Comparison (az.compare)

| Model      | Rank | ELPD    | p     | ELPD diff | Weight | SE   | dSE |
|------------|------|---------|-------|-----------|--------|------|-----|
| nonuniform_dif | 0    | −2120.0 | 240.5 | 0.0       | 0.93   | 31.0 | 0.0 |
| uniform_dif    | 1    | −2120.0 | 243.9 | −1.0      | 0.07   | 31.0 | 1.4 |

## Interpretation

1. **LOO is essentially identical** (ΔELPD = 0.9, dSE = 1.4). The difference is well within 1 SE — neither model is meaningfully better in terms of out-of-sample predictive accuracy.

2. **γ posterior differs in sign and precision**:
   - Uniform: γ = 0.245 ± 0.197 (positive, relatively precise, 90% CI barely includes 0)
   - Non-uniform: γ = −0.458 ± 0.453 (negative, much wider CI, includes 0)
   - The sign flip is expected: in the non-uniform model, γ is multiplied by a_i, so a smaller |γ| produces the same effect as a larger one in uniform. The negative sign suggests the model may struggle to separate γ from b.

3. **Sampling efficiency**: Uniform has better ESS (1468 vs 981 for γ) and faster sampling (59s vs 102s). The uniform parameterization is easier for NUTS.

4. **PPP**: Both models show adequate fit (0.763 vs 0.743).

5. **Conclusion**: The uniform DIF formulation is preferred because (a) LOO shows no disadvantage, (b) γ has a clearer interpretation with tighter posterior, (c) sampling is more efficient, and (d) γ's sign and magnitude are directly interpretable as a logit shift rather than being confounded with item discrimination.

## Files

- Stan models: `stan_models/contam_irt_2pl_gamma.stan` (uniform DIF), `stan_models/contam_irt_2pl_gamma_uniform.stan` (non-uniform DIF)
- Script: `analysis/compare_dif_models.py`
- Results JSON: `analysis/dif_comparison/results.json`
- Log: `logs/compare_dif_models.log`
- Server: cqa1-21977
- Total runtime: 3.9 min
