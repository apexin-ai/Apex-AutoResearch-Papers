# temp09 d1v2 AUC Inversion Analysis

## Conclusion: (B) Covariate Shift — Not a Bug

The inversion is a **genuine feature distribution shift**, not a label mapping error. Temperature=0.9 sampling produces systematically lower-ppl text at each recursion depth compared to nucleus/top-k sampling, causing the cross-strategy classifier to mismap temp09 depth N as depth N+1.

## Evidence

### 1. Labels are correct (within-strategy AUC is excellent)

Within-strategy RF d1v2 AUC from the 9-cell battery:

| Model | temp09 within-strategy | temp09 cross-LOO |
|-------|----------------------|-----------------|
| GPT-2 XL | **0.9368** | 0.1288 |
| OLMo-1B | **0.9029** | 0.2529 |
| Pythia-1.4B | **0.8341** | 0.5760 |

If labels were wrong, within-strategy AUC would also be broken.

### 2. Confusion matrices show systematic depth overestimation

GPT-2 XL (train: nucleus+topk50 → test: temp09):
```
  pred→  d0     d1     d2     d3
  d0    5000      0      0      0
  d1      23   1119   2629   1229    ← d1 predicted as d2/d3
  d2       3     19    187   4791    ← d2 predicted as d3
  d3       2     10     76   4912    ← d3 correct
```

OLMo-1B shows the identical pattern:
```
  pred→  d0     d1     d2     d3
  d0    5000      0      0      0
  d1      15   1268   2511   1206
  d2       4     29    443   4524
  d3       1     22     56   4921
```

The classifier sees temp09 text as "deeper" than it actually is, not as reversed.

### 3. Feature values are shifted by ~1 depth level

GPT-2 XL p90_ppl (top feature, importance=0.2216):

| Source | d0 | d1 | d2 | d3 |
|--------|----|----|----|----|
| nucleus median | 401.9 | **121.0** | **65.0** | 41.3 |
| topk50 median | 923.5 | **145.0** | **92.3** | 70.1 |
| temp09 median | 923.5 | **92.2** | **39.0** | 24.7 |

temp09 d1 (92.2) falls squarely in the training d2 range (65–92). temp09 d2 (39.0) falls in the training d3 range (41–70).

Quantified overlap: **44.4%** of temp09 d1 samples have p90_ppl within the training d2 IQR. Similar overlap for var_surprisal (44.1%) and type_token_ratio (52.2%).

### 4. Per-strategy z-normalization fixes the inversion

| Model | Raw d1v2 AUC | Z-normalized d1v2 AUC |
|-------|-------------|----------------------|
| GPT-2 XL | 0.1288 | **0.6817** |
| OLMo-1B | 0.2529 | **0.8340** |
| Pythia-1.4B | 0.5760 | **0.8013** |

When each strategy's features are independently standardized before training/testing, the inversion vanishes. This confirms the cause is absolute feature scale, not the learned d1↔d2 direction.

### 5. Dropping mean_ppl/var_ppl does NOT help

Removing the two outlier-prone features (mean_ppl, var_ppl) barely changes GPT-2 XL AUC (0.1288→0.1341). The shift operates through the robust percentile features (p90_ppl, p75_ppl, p50_ppl) and surprisal statistics.

### 6. RF feature importances

Top features driving the cross-strategy classifier (GPT-2 XL):
```
  p90_ppl                0.2216
  var_surprisal          0.1367
  p75_ppl                0.1089
  mean_surprisal         0.0705
  mean_ppl               0.0531
```

All these features have **the same d1→d2 direction** across strategies (all decrease), but their **absolute values are systematically lower** for temp09 at every depth.

## Physical Explanation

Temperature=0.9 (close to 1.0 = identity) applies a relatively uniform softening to the model's logit distribution. By contrast, nucleus (p=0.95) and top-k (k=50) truncate the distribution tail, preserving more entropy per generation step.

Under temperature sampling, the model converges faster toward its "attractor" distribution with each recursion:

1. **Faster convergence**: temp09 text at depth N exhibits statistical properties (ppl, surprisal variance, lexical diversity) that nucleus/topk50 text only reaches at depth N+1
2. **Lower floor**: temp09 reaches lower absolute ppl values at each depth because the sampling modification is less disruptive to the model's natural probability rankings
3. **Preserved direction**: the d1→d2→d3 trajectory *direction* (decreasing ppl, decreasing diversity) is the same across all strategies — only the *rate* differs

This means temperature sampling is not fundamentally different from nucleus/topk50 in what it reveals about recursive generation — it simply compresses the same trajectory into fewer steps. The cross-strategy classifier fails because it learns absolute feature thresholds, not relative depth-to-depth changes.

## Implications for the Paper

1. **This is not a failure of the depth estimation method** — it's a known limitation of cross-domain transfer without normalization
2. **Within-strategy depth estimation remains robust** (AUC > 0.83 for all models)
3. **Cross-strategy transfer requires feature normalization** (z-scoring restores AUC > 0.68)
4. The finding itself is scientifically interesting: it shows that sampling strategy modulates the *rate* of recursive degradation, not its *direction*, supporting the "model attractor" hypothesis
