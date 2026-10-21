# D061: Conditional Granger Analysis

## Setup
- Data: Pythia-410M, WikiText, alpha=1.0, seed=42, T=11 (gen 0-10)
- First-differenced, max_lag=1, n_perm=5000
- Parametric F-test + permutation test

## Results Table

| Downstream | Test | Control | F_marg | p_perm (marg) | F_cond | p_perm (cond) | df_cond |
|---|---|---|---|---|---|---|---|
| distinct_1 | token_entropy | ece | 2853.51 | 0.0002* | 0.07 | 0.8002 | 5 |
| distinct_1 | ece | token_entropy | 7088.63 | 0.0002* | 7.58 | 0.0824 | 5 |
| distinct_2 | token_entropy | ece | 1582.09 | 0.0012* | 1.55 | 0.2781 | 5 |
| distinct_2 | ece | token_entropy | 1311.70 | 0.0006* | 0.43 | 0.5559 | 5 |
| distinct_3 | token_entropy | ece | 999.51 | 0.0012* | 1.67 | 0.3357 | 5 |
| distinct_3 | ece | token_entropy | 791.38 | 0.0006* | 0.29 | 0.6473 | 5 |

## Interpretation

**Both canaries are marginally significant but mutually redundant.** All 6 marginal tests are highly significant (p < 0.002). All 6 conditional tests are non-significant (p > 0.05).

This means:
- Controlling for ECE, token_entropy adds NO independent predictive power (0/3 significant)
- Controlling for token_entropy, ECE adds NO independent predictive power (0/3 significant)

The pattern is **symmetric mutual redundancy**: token_entropy and ECE are so highly collinear in the collapse trajectory that either one alone captures essentially all the Granger-causal information about diversity decline. Neither provides unique information beyond what the other already explains.

Note: ECE -> distinct_1 conditional is borderline (parametric p=0.04, permutation p=0.08). With more data this might become significant, but with current T=11 it does not survive permutation testing.

## Limitations

1. **T=11 power problem**: After differencing (T_eff=10) and lagging (n=9), the conditional model has 4 parameters, leaving df_resid=5. Statistical power is very low. The redundancy finding could partly reflect insufficient power to detect conditional effects.

2. **Single seed**: Only seed 42 tested. Multi-seed pooling could increase power but introduces cross-seed heterogeneity.

3. **Collinearity interpretation**: Symmetric redundancy is consistent with two hypotheses:
   - (a) Both metrics measure the same underlying latent "calibration degradation" process
   - (b) Both genuinely cause diversity loss independently but are too correlated for conditional analysis to separate them at T=11

## Paper Implications

**Recommended framing**: Token entropy and ECE provide converging (rather than independent) evidence of impending diversity collapse. They likely track a shared latent calibration degradation signal. For practical early-warning, either metric suffices; monitoring both adds robustness but not new information.

**Do NOT claim**: "token_entropy and ECE independently predict collapse" (the conditional analysis directly contradicts this).

**Suggested paper text**: "Conditional Granger analysis reveals that token entropy and ECE carry redundant predictive information about diversity decline (all conditional p > 0.08 after controlling for the other canary). This suggests both metrics track a shared upstream calibration degradation process, consistent with their common origin in the model's predictive distribution."

## Raw Data Location
- Script: `/root/autodl-tmp/distrib_canary_collapse/analyze_conditional_granger.py`
- JSON output: `/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger.json`
