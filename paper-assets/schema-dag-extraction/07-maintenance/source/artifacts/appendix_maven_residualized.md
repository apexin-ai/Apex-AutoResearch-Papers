## Appendix X: MAVEN Per-Type BCS--F1 Analysis: A Centrality Artifact

### Motivation

In our main experiments, higher BCS (Boundary Confusion Score) is associated with greater extraction difficulty---types whose schema neighbors are more semantically similar are harder to distinguish. On Few-NERD, per-type BCS correlates negatively with F1 ($\rho = -0.293$, $p = 0.020$), consistent with this interpretation. On MAVEN, however, per-type BCS shows a *positive* correlation with F1 (Table~\ref{tab:maven-raw}), suggesting that types embedded in denser schema neighborhoods are *easier* to classify. We investigate whether this reversal reflects a genuine structural effect or a centrality artifact.

### Method

We compute per-type mean BCS under two embedding spaces (MiniLM, Qwen3) for 149 MAVEN event types (168 total; 19 excluded with gold frequency $< 5$). We then test whether the BCS--F1 correlation survives partial correlation analysis controlling for two centrality proxies:

- **Type frequency** ($\log(1 + \text{freq})$): more frequent types may have both higher BCS (more training signal shaping their embedding neighborhood) and higher F1 (more supervision).
- **Degree centrality**: the number of types exceeding a similarity threshold (0.7 for Qwen3, 0.3 for MiniLM, selected as the strongest BCS--degree correlate per embedding). High-degree types sit at the center of the schema graph and may benefit from richer contextual disambiguation cues.

Partial correlations are computed by residualizing both BCS and F1 on the control variable(s) via OLS regression and correlating the residuals (Pearson $r$). We also report Spearman $\rho$ where applicable.

### Results

**Table X.1: Raw per-type BCS--F1 correlations on MAVEN**

| Embedding | Spearman $\rho$ | $p$ | Pearson $r$ | $p$ |
|-----------|-----------------|-----|-------------|-----|
| Qwen3     | +0.184          | 0.025 | +0.175    | 0.032 |
| MiniLM    | +0.208          | 0.011 | +0.170    | 0.039 |

Both embeddings show a significant positive BCS--F1 association ($p < 0.05$).

**Table X.2: Centrality diagnostics---BCS correlates with different centrality proxies per embedding**

| Embedding | BCS $\leftrightarrow$ log\_freq | BCS $\leftrightarrow$ degree centrality |
|-----------|---|----|
| Qwen3     | $r = -0.043$ ($p = 0.599$, n.s.) | $r = +0.854$ ($p < 0.001$; threshold 0.7) |
| MiniLM    | $r = +0.201$ ($p = 0.014$)        | $r = +0.909$ ($p < 0.001$; threshold 0.3) |

For MiniLM, BCS is confounded with type frequency. For Qwen3, BCS is nearly uncorrelated with frequency but strongly correlated with degree centrality---reflecting the denser similarity structure of the Qwen3 embedding space (BCS range 0.226--0.786 vs. MiniLM's 0.064--0.313).

**Table X.3: Partial correlations---BCS--F1 after controlling for centrality**

| Embedding | Control variable(s) | Partial $r$ | $p$ | Significant? |
|-----------|---------------------|-------------|-----|--------------|
| MiniLM    | log\_freq            | +0.133      | 0.107 | No |
| MiniLM    | log\_freq + degree   | +0.100      | 0.226 | No |
| Qwen3     | log\_freq            | +0.189      | 0.021 | Yes |
| Qwen3     | degree (0.7)         | +0.063      | 0.442 | No |
| Qwen3     | log\_freq + degree   | +0.064      | 0.439 | No |

For MiniLM, controlling for type frequency alone is sufficient to render BCS--F1 non-significant. For Qwen3, frequency control is insufficient (the confound operates through degree centrality, not frequency), but controlling for degree centrality eliminates the association. Under joint control, neither embedding retains a significant BCS--F1 relationship.

### Discussion

The apparent positive BCS--F1 correlation on MAVEN is fully explained by centrality confounds. The confound operates through different proxies depending on the embedding space:

- **MiniLM** (lower similarity scale): BCS acts as a proxy for type frequency. Frequent types accumulate more semantic neighbors, inflating mean BCS, while simultaneously benefiting from greater supervision.
- **Qwen3** (higher similarity scale): all types are densely interconnected, so frequency does not predict BCS. Instead, BCS tracks graph-theoretic degree centrality---types with more neighbors above a high similarity threshold are both more "central" and easier to classify.

This contrasts sharply with Few-NERD, where no centrality confound exists (BCS $\leftrightarrow$ log\_freq: $r = 0.042$, $p = 0.74$) and BCS exhibits the expected negative association with F1. The difference arises from schema structure: Few-NERD spans 66 types across diverse domains (person, location, event, etc.) with clearer semantic boundaries, whereas MAVEN's 168 types are all event subtypes within a single ontological domain, creating a regime where semantic centrality dominates.

### Conclusion

MAVEN's per-type BCS--F1 reversal is an artifact of centrality confounding, not evidence that higher schema similarity aids extraction. The pairwise SCS--confusion relationship (types with higher pairwise semantic similarity are more frequently confused) remains robust on MAVEN and constitutes the valid claim. Per-type BCS should not be interpreted as having a direct causal effect on type-level performance for datasets with dense, same-domain type systems.
