## exp_017_llama_conll_finetune Results

| Metric | Value |
|---|---|
| Degeneracy rate | **85.3%** (vs Qwen CoNLL 59.1%) |
| Greedy F1 | 92.8% |
| Oracle F1 | 95.1% |
| Headroom | 2.3% |
| Selection F1 | 93.4% |

### 5-Signal QE (Full, n=2756)
| Signal | ρ | 95% CI | AUROC |
|---|---|---|---|
| SJ | 0.450 | [0.405, 0.497] | 0.752 |
| FK | 0.443 | [0.399, 0.490] | 0.749 |
| VC | 0.437 | [0.393, 0.483] | 0.747 |
| EM | 0.448 | [0.405, 0.495] | 0.753 |
| LP | 0.273 | [0.243, 0.305] | 0.739 |

### Conditional (greedy F1>0, n=2645)
| Signal | ρ | AUROC |
|---|---|---|
| SJ | 0.454 | 0.779 |
| EM | 0.458 | 0.783 |
| LP | 0.311 | 0.804 |

Cross-model validation: CoNLL high-degen regime confirmed across LLaMA and Qwen. Structural signals ρ~0.45 >> LP 0.273, QE diagnostic value is model-agnostic.