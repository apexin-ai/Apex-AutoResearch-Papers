## Argmax Agreement

| Condition | Agreement Rate | N problems |
|-----------|---------------|------------|
| Mistral-7B × FOLIO | 92.2% | 204 |
| Mistral-7B × PW | 90.2% | 600 |
| Qwen2.5-14B × FOLIO | 97.5% | 204 |
| Qwen2.5-14B × PW | 93.2% | 600 |
| LLaMA-8B × FOLIO | 87.3% | 204 |
| LLaMA-8B × PW | 87.3% | 600 |
| **OVERALL** | **90.8%** | **2412** |

## BR Decomposition (SC-incorrect problems only)

| Condition | Observed BR | Base-rate BR | Excess | Pearson r | N valid |
|-----------|------------|-------------|--------|-----------|---------|
| Mistral-7B × FOLIO | 2.19 | 3.85 | −1.65 | 0.70 | 85 |
| Mistral-7B × PW | 2.46 | 4.44 | −1.98 | 0.52 | 318 |
| Qwen2.5-14B × FOLIO | 2.05 | 4.37 | −2.31 | 0.58 | 33 |
| Qwen2.5-14B × PW | 1.53 | 3.79 | −2.25 | 0.24 | 139 |
| LLaMA-8B × FOLIO | 2.14 | 3.71 | −1.57 | 0.56 | 65 |
| LLaMA-8B × PW | 1.49 | 2.83 | −1.35 | 0.63 | 174 |

## When SICA ≠ SC (Disagreement Analysis)

| Condition | Disagree | SICA correct | SC correct | Both wrong |
|-----------|----------|-------------|-----------|------------|
| Mistral-7B × FOLIO | 16 | 10 | 3 | 3 |
| Mistral-7B × PW | 59 | 10 | 32 | 17 |
| Qwen2.5-14B × FOLIO | 5 | 1 | 3 | 1 |
| Qwen2.5-14B × PW | 41 | 10 | 25 | 6 |
| LLaMA-8B × FOLIO | 26 | 9 | 16 | 1 |
| LLaMA-8B × PW | 76 | 13 | 58 | 5 |

## Shuffle Control (existing data)

| Condition | Original BR | Shuffle Null BR | p-value | Cohen's d |
|-----------|------------|----------------|---------|-----------|
| Qwen3-FOLIO-2x2 | 5.70 | 6.16 | 0.783 | −0.78 |
| GPT4o-FOLIO | 6.32 | 6.89 | 0.822 | −0.93 |
| Mistral7B-FOLIO | 3.16 | 3.31 | 0.706 | −0.62 |

Data source: Mistral PW = multi_seed/mistral_pw_seed42. Server results saved to /root/symb_invariant_consensus/results/r17_argmax_br_metrics.json