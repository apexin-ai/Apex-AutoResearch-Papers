# exp_wiki_llama8b Analysis

## K* Result

**K* = 1** (one-wash)

LLaMA-3.1-8B on Wikipedia exhibits one-wash behavior: the classifier strongly discriminates gen-0 from gen-1 (AUC=0.93), but cannot distinguish any subsequent adjacent generations (AUC ~0.52-0.60, chance level).

## Key Metrics

### Pairwise AUC (adjacent depths, 5-fold CV)

| Pair    | AUC (mean) | Std    | Discriminable? |
|---------|-----------|--------|----------------|
| 0 vs 1  | 0.9316    | 0.0055 | Yes            |
| 1 vs 2  | 0.5954    | 0.0084 | No (< 0.60)    |
| 2 vs 3  | 0.5392    | 0.0105 | No             |
| 3 vs 4  | 0.5221    | 0.0115 | No             |
| 4 vs 5  | 0.5212    | 0.0129 | No             |

### Pairwise JSD (adjacent depths)

| Pair    | JSD      |
|---------|----------|
| 0 vs 1  | 0.06169  |
| 1 vs 2  | 0.00931  |
| 2 vs 3  | 0.00538  |
| 3 vs 4  | 0.00390  |
| 4 vs 5  | 0.00381  |

JSD drops by 6.6x from 0v1 to 1v2, confirming the sharp boundary at K*=1.

### Ordinal Classification (6-class, 5-fold CV)

| Metric   | Value  |
|----------|--------|
| MAE      | 1.2954 |
| Accuracy | 0.3313 |

Low ordinal accuracy (33%, vs 16.7% random baseline) reflects the classifier only reliably separating gen-0 from the rest.

### Top-5 Feature Importance

| Feature        | Importance |
|----------------|-----------|
| freq_entropy   | 8784.4    |
| surp_d1_skew   | 8168.0    |
| surp_mean      | 8128.8    |
| surp_d2_mean   | 7833.4    |
| surp_d1_mean   | 7816.0    |

Frequency entropy and surprisal-based features dominate, consistent with prior Wikipedia experiments.

## Comparison with Other Wikipedia Models

| Model          | Size  | K* | Pattern    |
|----------------|-------|-----|-----------|
| Pythia-1.4B    | 1.4B  | 1   | One-wash  |
| OLMo-1B       | 1B    | 1   | One-wash  |
| Qwen-1.5B     | 1.5B  | 2   | Two-wash  |
| **LLaMA-3.1-8B** | **8B** | **1** | **One-wash** |

LLaMA-3.1-8B (8B params) shows the same one-wash K*=1 as Pythia-1.4B and OLMo-1B, despite being 5-8x larger. This indicates model scale alone does not increase K* on Wikipedia. Qwen-1.5B remains the outlier with K*=2, suggesting its higher K* stems from architecture or training data differences rather than scale.

## Conclusion

**Negative.** The hypothesis that LLaMA-3.1-8B would achieve K*=2 on Wikipedia is not supported. K*=1 aligns with the dominant one-wash pattern observed for most models on this domain. The 0v1 AUC of 0.93 is notably high (comparable to smaller models), while 1v2 AUC of 0.60 sits right at the discrimination threshold, making the K*=1 determination robust.
