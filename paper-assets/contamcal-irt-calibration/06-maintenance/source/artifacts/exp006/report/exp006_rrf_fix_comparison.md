# Exp-006 RRF Fix: Before/After Comparison

## Bug Summary

`load_exp002_signals()` used `signal_key="s1_embedding"` — a model-agnostic embedding similarity score — producing **identical exposure values across 0.5B and 1.5B** for the same dosage level. Per D030, should use 3-signal RRF fusion (S1+S2+S4) with S2 polarity flip.

## Exposure Values (D024 delta, 8 models: 0.5B d0/d10/d50/d100, 1.5B d0/d10/d50/d100)

### GSM8K
| Version | 0.5B exposures | 1.5B exposures |
|---------|---------------|----------------|
| v2 (bug) | [0.0, 0.0160, 0.0648, 0.1972] | [0.0, **0.0160**, **0.0648**, **0.1972**] |
| v3_rrf (fix) | [0.0, 0.0, 0.0212, 0.0037] | [0.0, 0.0136, 0.0049, 0.0309] |

**Key observation:** v2 has 0.5B == 1.5B exposures (identical). v3_rrf correctly differentiates by scale.

### ARC Challenge
| Version | 0.5B exposures | 1.5B exposures |
|---------|---------------|----------------|
| v2 (bug) | [0.0, 0.0266, 0.0986, 0.3053] | [0.0, **0.0266**, **0.0986**, **0.3053**] |
| v3_rrf (fix) | [0.0, 0.0388, 0.0289, 0.0678] | [0.0, 0.0, 0.0, 0.0145] |

## IRT 4PL+gamma Results

### GSM8K Pooled IRT (0.5B + 1.5B)

| Metric | v2 (s1 only) | v3_rrf (S1+S2+S4) | Change |
|--------|-------------|-------------------|--------|
| gamma (mean) | 0.1871 | **2.0959** | +1.909 |
| gamma 95% CI | [-0.9172, 1.3294] | [0.9681, 3.3043] | — |
| CI excludes zero | **No** | **Yes** | Fixed |
| max Rhat | 1.0148 (NOT OK) | **1.0085** (OK) | Fixed |
| min ESS | 330.2 (NOT OK) | **491.8** (OK) | Fixed |
| divergent % | 0% | 0% | Same |
| all_ok | **False** | **True** | Fixed |
| MAE | 0.0364 | 0.0794 | +0.043 |
| Brier | 0.0015 | 0.0116 | +0.010 |

**Interpretation:** v3_rrf produces a statistically significant positive gamma (contamination amplifies scores), with proper MCMC convergence. v2 had non-converged chains and gamma indistinguishable from zero.

### ARC Challenge Pooled IRT (0.5B + 1.5B)

| Metric | v2 (s1 only) | v3_rrf (S1+S2+S4) | Change |
|--------|-------------|-------------------|--------|
| gamma (mean) | -2.3471 | **-7.6202** | -5.273 |
| gamma 95% CI | [-3.4573, -1.1923] | [-8.7902, -6.4210] | — |
| CI excludes zero | Yes | Yes | Same |
| max Rhat | 1.0099 (OK) | **1.0078** (OK) | Improved |
| min ESS | 817.2 (OK) | **1132.5** (OK) | Improved |
| divergent % | 0% | 0% | Same |
| all_ok | True | True | Same |
| MAE | 0.0347 | 0.1148 | +0.080 |
| Brier | 0.0018 | 0.0264 | +0.025 |

**Interpretation:** ARC gamma remains significantly negative (contamination doesn't inflate ARC scores — expected for multiple-choice format). RRF fix makes gamma magnitude larger and MCMC diagnostics better (higher ESS, lower Rhat).

## Full Evaluation Tables

### GSM8K v3_rrf
```
Method                              MAE      ECE    Brier    C50    C80    C95      S95    tau  gamma>0
IRT_4pl_gamma                    0.0794   0.0794   0.0116   0.12   0.12   0.25     0.08  0.756    2.096
B0_raw                           0.0031   0.0031   0.0000   1.00   1.00   1.00     0.05  0.756      ---
B2_2pl_gamma                     0.0246   0.0246   0.0012   0.38   0.62   1.00     0.08  0.756      ---
B3_vanilla_4pl                   0.0357   0.0357   0.0013   0.00   0.00   0.00     0.04  0.756      ---
B4_linear_regression             0.0367   0.0367   0.0030   0.25   0.88   0.88     0.25  0.756      ---
B6_dcr_fuzzy                     0.2133   0.2133   0.0791   0.38   0.38   0.38     0.03  0.095      ---
```

### ARC v3_rrf
```
Method                              MAE      ECE    Brier    C50    C80    C95      S95    tau  gamma>0
IRT_4pl_gamma                    0.1148   0.0898   0.0264   0.00   0.00   0.00     0.04  0.472   -7.620
B0_raw                           0.0588   0.0588   0.0089   0.62   0.62   0.62     0.05  0.800      ---
B2_2pl_gamma                     0.1712   0.1712   0.0641   0.25   0.38   0.50     0.04  0.756      ---
B3_vanilla_4pl                   0.0706   0.0706   0.0070   0.12   0.12   0.12     0.04  0.756      ---
B4_linear_regression             0.0773   0.0756   0.0162   0.25   0.25   0.50     0.21  0.481      ---
B6_dcr_fuzzy                     0.1909   0.1909   0.0723   0.50   0.50   0.50     0.03  0.674      ---
```

## Server Artifacts
- GSM8K v3_rrf: `/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/`
- ARC v3_rrf: `/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_v3_rrf/`
- Code backup: `/root/contamcal-irt-calibration/exp006/run_exp006.py.bak_pre_rrf_fix`
- Pipeline time: GSM8K 866.1s, ARC 736.7s
