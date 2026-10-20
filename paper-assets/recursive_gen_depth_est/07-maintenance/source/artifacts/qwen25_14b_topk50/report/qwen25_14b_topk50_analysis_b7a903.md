# Experiment Analysis: qwen25_14b_topk50

## Summary

**Status**: SUCCESS — RF 4-class accuracy 47.93%, nearly 2× the 25% random baseline. Depth signal persists under top-k sampling (k=50) at 14B scale.

## Core Metrics

| Metric | Value |
|--------|-------|
| RF 4-class accuracy | 47.93% [47.26%, 48.59%] |
| LR 4-class accuracy | 43.95% [43.23%, 44.65%] |
| RF 3-class (no d0) | 51.64% [50.83%, 52.39%] |
| Samples per depth | 5,000 |
| Features | 19 (self-referential) |
| Runtime | 24.5h |

## Pairwise AUC (RF)

| Pair | AUC |
|------|-----|
| d0 vs d1 | 0.5607 |
| d0 vs d2 | 0.8481 |
| d0 vs d3 | 0.9253 |
| d1 vs d2 | 0.6868 |
| d1 vs d3 | 0.7935 |
| d2 vs d3 | 0.6788 |

Adjacent-depth discrimination (d1v2=0.69, d2v3=0.68) is moderate; distant-depth discrimination (d0v3=0.93) remains strong. Monotonic ordering of AUC with depth gap is preserved.

## Top-5 Features

1. kurt_ppl (0.0813)
2. skew_ppl (0.0786)
3. var_surprisal (0.0747)
4. type_token_ratio (0.0698)
5. hapax_ratio (0.0669)

Feature importance is more evenly distributed than nucleus/temp09, with lexical features (TTR, hapax) ranking higher. This suggests top-k sampling shifts discriminative signal toward vocabulary diversity metrics rather than pure perplexity statistics.

## 14B Cross-Strategy Comparison

| Strategy | RF 4-class | d1v2 AUC | d2v3 AUC | Top feature |
|----------|-----------|----------|----------|-------------|
| nucleus (scale_002) | 54.05% | 0.7133 | 0.7283 | — |
| temp 0.9 (qwen25_14b_temp09) | 50.50% | 0.7259 | 0.6184 | p90_ppl |
| top-k 50 (this) | 47.93% | 0.6868 | 0.6788 | kurt_ppl |

**Pattern**: nucleus > temp09 > topk50 — consistent with 1.5B scale ordering where top-k yields the lowest accuracy across strategies.

**Delta from baseline**: topk50 at +22.93pp above 25% chance; all three strategies robustly above baseline.

## Comparison with 1.5B Scale

At 1.5B (9-cell matrix mean = 78.4%), top-k cells averaged ~76% (pythia_topk50=71.2%, olmo_topk50=78.4%, gpt2xl_topk50=79.1%). The 14B top-k result (47.93%) shows the expected scale-dependent accuracy reduction while maintaining signal well above chance.

## Conclusion

**SUCCESS**. Top-k sampling (k=50) at 14B scale produces the hardest discrimination scenario among the three strategies tested, yet RF 4-class accuracy remains ~48% — nearly double the 25% baseline. This completes the 14B sampling strategy robustness argument:

- All three decoding strategies (nucleus, temperature, top-k) show signal above baseline at 14B scale
- The relative ordering across strategies (nucleus > temp > topk) matches 1.5B patterns
- Pairwise AUC shows monotonic structure (distant depths more separable), confirming genuine depth-aware discrimination

This directly addresses the Dream review concern M3 (scale generality) by demonstrating signal persistence even under the worst-case sampling strategy at 14B scale.
