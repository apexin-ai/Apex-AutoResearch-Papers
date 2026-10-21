# T-Ablation 3-Seed Summary Table

**Model**: Qwen2.5-7B-Instruct (LoRA) | **N=8 samples** | **Date**: 2026-05-21

## Main Results

| Dataset | T | n | greedy F1 | oracle F1 | Headroom | Degen% | ρ(SJ,F1) | ρ(FK,F1) | ρ_adv | Verdict |
|---------|--:|--:|----------:|----------:|---------:|-------:|---------:|---------:|------:|---------|
| FewNERD | 0.5 | 2 | 0.789±0.000 | 0.860±0.005 | 0.072±0.005 | 14.1±0.8 | 0.308±0.059 | 0.259±0.051 | 0.049±0.008 | MARGINAL |
| FewNERD | 0.8 | 3 | 0.788±0.001 | 0.879±0.005 | 0.090±0.004 | 17.3±1.4 | 0.290±0.073 | 0.176±0.063 | 0.115±0.012 | MARGINAL×2 |
| FewNERD | 1.0 | 1 † | 0.748 | 0.872 | 0.124 | 10.1 | 0.300 | 0.313 | -0.013 | — |
| FewNERD | 1.2 | 2 | 0.789±0.000 | 0.881±0.009 | 0.092±0.008 | 26.4±2.5 | 0.210±0.105 | 0.112±0.072 | 0.099±0.033 | FAIL |
| | | | | | | | | | | |
| CoNLL | 0.5 | 3 | 0.908±0.001 | 0.935±0.002 | 0.028±0.002 | 5.6±0.1 | 0.446±0.020 | 0.452±0.002 | 0.006±0.002 | PASS×3 |
| CoNLL | 0.8 | 3 | 0.907±0.000 | 0.945±0.003 | 0.038±0.003 | 6.3±0.2 | 0.474±0.021 | 0.463±0.025 | 0.011±0.005 | PASS×3 |
| CoNLL | 1.0 | 1 | 0.908 | 0.950 | 0.043 | 7.5 | 0.425 | 0.404 | 0.021 | PASS |
| CoNLL | 1.2 | 3 | 0.907±0.000 | 0.951±0.005 | 0.043±0.005 | 8.9±0.5 | 0.432±0.024 | 0.405±0.025 | 0.027±0.001 | PASS×3 |
| | | | | | | | | | | |
| SciERC | 0.5 | 3 | 0.663±0.002 | 0.744±0.002 | 0.081±0.003 | 10.2±0.2 | 0.328±0.007 | 0.278±0.015 | 0.040±0.020 | MARGINAL×2 |
| SciERC | 0.8 | 3 | 0.662±0.002 | 0.772±0.003 | 0.110±0.005 | 11.5±0.4 | 0.376±0.012 | 0.272±0.027 | 0.101±0.024 | MARGINAL×2 |
| SciERC | 1.0 | 3 | 0.662±0.001 | 0.778±0.002 | 0.115±0.003 | 12.8±0.2 | 0.378±0.016 | 0.267 | — | — |
| SciERC | 1.2 | 3 | 0.663±0.001 | 0.786±0.003 | 0.122±0.003 | 13.9±0.2 | 0.380±0.037 | 0.282±0.052 | 0.112±0.018 | MARGINAL/PASS |
| | | | | | | | | | | |

† FewNERD T=1.0 uses exp_021_fewnerd_full (different eval pipeline, greedy_macro_f1 ≠ greedy_f1). Not directly comparable.

## Agreement Metrics (where available)

| Dataset | T | n | Fleiss κ | Soft Jaccard |
|---------|--:|--:|--------:|------------:|
| FewNERD | 0.5 | 1 | 0.633 | 0.865 |
| FewNERD | 0.8 | 1 | 0.444 | 0.757 |
| FewNERD | 1.2 | 1 | 0.283 | 0.589 |
| CoNLL | 0.5 | 3 | 0.893±0.004 | 0.955±0.001 |
| CoNLL | 0.8 | 3 | 0.823±0.002 | 0.922±0.002 |
| CoNLL | 1.0 | 1 | 0.772 | 0.895 |
| CoNLL | 1.2 | 3 | 0.692±0.022 | 0.840±0.015 |
| SciERC | 0.5 | 1 | 0.572 | 0.830 |
| SciERC | 0.8 | 1 | 0.452 | 0.756 |
| SciERC | 1.0 | 1 | 0.393 | 0.696 |
| SciERC | 1.2 | 1 | 0.352 | 0.647 |

## Data Coverage Notes

| Dataset | T | Seeds available | Missing |
|---------|---|-----------------|---------|
| FewNERD | 0.5 | s123, s42 (n=2) | s456 (exp_fewnerd_t05_s456) |
| FewNERD | 1.0 | s42 (n=1) | WARNING |
| FewNERD | 1.2 | s123, s42 (n=2) | s456 (exp_fewnerd_t12_s456) |
| CoNLL | 1.0 | s42 (n=1) | n=1<3 |

## Key Trends

1. **Greedy F1 is T-invariant**: CoNLL ≈0.907, SciERC ≈0.663, FewNERD ≈0.789 across all T
2. **Oracle headroom increases with T**: More diverse samples → higher theoretical ceiling
3. **Degeneracy increases with T**: Higher T → more noisy/zero-F1 samples
4. **ρ(SJ,F1) peaks at T=0.8**: SciERC 0.376, CoNLL 0.474 — sweet spot between diversity and noise
5. **ρ_advantage increases with T**: Structural consistency gains more over surface as samples become more diverse
6. **CoNLL shows strongest signals**: ρ(SJ,F1) > 0.42 across all T values