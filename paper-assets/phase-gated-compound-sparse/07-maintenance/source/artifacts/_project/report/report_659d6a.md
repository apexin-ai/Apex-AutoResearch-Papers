# W4: Pruned-Head Overlap / Structural Specificity Analysis

## Summary

Importance pruning (bottom-k by attention Frobenius norm) **selectively removes low-Gini heads** — heads with more diffuse, less discriminative attention patterns. This provides quantitative evidence for **structural specificity**: importance-based head pruning is not random; it systematically targets heads with particular attention characteristics.

## Method

1. Forward pass on 30 stratified MATH-500 problems (6 per difficulty level, seed=42)
2. Per-head metrics computed and averaged across samples:
   - **Frobenius norm** of attention weights → determines pruning order (lower = pruned first)
   - **Gini coefficient** of attention distributions → measures attention discrimination/focus
3. For each sparsity level, heads partitioned into importance-pruned (bottom-k Frobenius per layer) vs retained
4. Random-pruned baseline: 200 random trials of same-size random head subsets
5. Mann-Whitney U test (two-sided) for Gini distribution comparison

## Results

### DeepSeek-R1-Distill-Qwen-7B (28 layers × 28 heads)

| Sparsity | Pruned/Layer | Imp-Pruned Gini (mean) | Random Gini (mean) | Retained Gini (mean) | Δ(imp−ret) | p-value | rank-biserial r |
|----------|-------------|----------------------|-------------------|---------------------|------------|---------|-----------------|
| s015     | 4           | 0.7965               | 0.8574            | 0.8672              | −0.0707    | 1.0e-37 | 0.757           |
| s020     | 5           | 0.8004               | 0.8569            | 0.8694              | −0.0690    | 9.9e-45 | 0.756           |
| s025     | 7           | 0.8092               | 0.8569            | 0.8731              | −0.0639    | 4.6e-53 | 0.731           |
| s030     | 8           | 0.8129               | 0.8571            | 0.8748              | −0.0619    | 1.8e-56 | 0.723           |

### Qwen2.5-7B-Instruct (28 layers × 28 heads)

| Sparsity | Pruned/Layer | Imp-Pruned Gini (mean) | Random Gini (mean) | Retained Gini (mean) | Δ(imp−ret) | p-value | rank-biserial r |
|----------|-------------|----------------------|-------------------|---------------------|------------|---------|-----------------|
| s015     | 4           | 0.8469               | 0.8982            | 0.9063              | −0.0594    | 1.4e-28 | 0.654           |
| s020     | 5           | 0.8508               | 0.8977            | 0.9080              | −0.0572    | 1.3e-33 | 0.651           |
| s025     | 7           | 0.8585               | 0.8976            | 0.9109              | −0.0524    | 3.4e-38 | 0.616           |
| s030     | 8           | 0.8614               | 0.8979            | 0.9124              | −0.0510    | 1.8e-41 | 0.616           |

## Key Findings

1. **Strong structural specificity**: Importance-pruned heads have significantly lower Gini than both retained and random-pruned heads (all p < 1e-28).

2. **Large effect sizes**: Rank-biserial r ranges from 0.62–0.76, indicating a large separation between pruned and retained head distributions.

3. **Consistent across models**: Both DeepSeek and Qwen show the same direction — importance pruning targets low-Gini (diffuse attention) heads. DeepSeek shows a slightly larger effect (r ≈ 0.73–0.76) than Qwen (r ≈ 0.62–0.65).

4. **Direction of specificity**: Low-importance heads (low Frobenius norm) tend to have diffuse attention (low Gini). This is intuitive: heads that spread attention broadly across many positions have smaller per-element weights, yielding lower Frobenius norms.

5. **Implication for compound interaction**: By selectively removing diffuse-attention heads, importance pruning disrupts a specific computational substrate. The remaining (retained) heads are predominantly high-Gini "sharp-attention" heads, which may alter the model's attention distribution landscape non-uniformly — a potential mechanism for the super-additive compound degradation observed in the main experiments.

## Artifacts

- `analysis_output/w4_pruned_head_overlap.json` — full per-head Gini and Frobenius data
- `analysis_output/w4_gini_violin_deepseek.png` — violin plots (DeepSeek)
- `analysis_output/w4_gini_violin_qwen.png` — violin plots (Qwen)
- `analysis_output/w4_importance_vs_gini_scatter.png` — importance vs Gini scatter (both models)
