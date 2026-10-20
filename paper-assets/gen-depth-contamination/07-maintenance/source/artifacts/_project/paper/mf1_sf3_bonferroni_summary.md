## MF-1: arXiv 2v3 CI

### Verified values (from JSON)
- Qwen arXiv 2v3: AUC=0.6427, CI=[0.6275, 0.6575], perm_p=0.0001 ✓
- Pythia arXiv 2v3: AUC=0.6544, CI=[0.6401, 0.6688], perm_p=0.0001 ✓

### Edits
1. appendix.tex Table S12: arXiv 2v3 row now shows $.6436\;[.628,.658]$ with footnote
2. experiments_c1.tex Section 4.6: added inline CIs for both Qwen and Pythia arXiv 2v3

## SF-3: Bonferroni 99.5% CI (10 configs)

α_corr = 0.05/10 = 0.005, z = 2.807

| Config | Boundary | AUC | σ_boot | 99.5% CI | Pass θ |
|--------|----------|-----|--------|----------|--------|
| Qwen-rw | 1v2 | .6955 | .0046 | [.683, .708] | ✓ |
| Pythia-1.4B | 1v2 | .6539 | .0046 | [.641, .667] | ✓ |
| Qwen-base | 1v2 | .6260 | .0047 | [.613, .639] | ✓ |
| Qwen-7B | 1v2 | .6168 | .0046 | [.604, .630] | ✓ |
| LLaMA-8B | 1v2 | .6123 | .0048 | [.599, .626] | ✗ |
| Qwen-cont | 1v2 | .6112 | .0049 | [.598, .625] | ✗ |
| OLMo-1B | 0v1 | .9860 | .0009 | [.983, .989] | ✓ |
| Mistral-7B | 0v1 | .9842 | .0009 | [.982, .987] | ✓ |
| Pythia-6.9B | 0v1 | .9599 | ~.0015 | [.956, .964] | ✓ |
| Gemma-2-2B | 0v1 | .9530 | .0018 | [.948, .958] | ✓ |

**2/10 fail**: Qwen-cont (CI_lower=0.5976) and LLaMA-8B (CI_lower=0.5988)
