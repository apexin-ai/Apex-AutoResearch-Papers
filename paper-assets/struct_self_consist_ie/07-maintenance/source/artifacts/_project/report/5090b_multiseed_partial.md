## 5090-b Multi-seed Qwen Inference Results

| Dataset | Seed | Greedy F1 | Oracle F1 | Headroom | Degen% | Best ρ | DGS delta |
|---------|------|-----------|-----------|----------|--------|--------|-----------|
| SciERC | 456 | 0.6453 | 0.7726 | 12.72pp | 19.3% | VC=0.41 | -0.30pp |
| CoNLL | 123 | 0.9074 | 0.9477 | 4.03pp | 63.0% | EM=0.47 | -0.60pp |
| CoNLL | 456 | 0.9076 | 0.9443 | 3.67pp | 63.0% | VC=0.48 | -0.71pp |
| FewNERD | 123 | — | — | — | — | — | 🔄 ~2h remaining |

Cross-seed consistency confirmed: degeneracy and ρ values stable across seeds.