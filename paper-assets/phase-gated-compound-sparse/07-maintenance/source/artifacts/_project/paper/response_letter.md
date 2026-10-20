# Response Letter --- Phase-Modulated Compound Sparsity

We thank the reviewers for their thorough and constructive feedback. We apologize for the delayed incorporation of n=500 crossover verification and the ThinKV attribution correction. Both analyses were completed but not reflected in the previous revision due to a process oversight. This revision fully integrates all outstanding changes.

Below we address each comment point-by-point. All data changes reference the n=500 dataset (n_eff=496 DeepSeek, n_eff=475 Qwen) unless otherwise noted.

---

## Summary of Changes

### Data-Driven Updates
- **N1**: Table 2 replaced with n=500 data for both DeepSeek (n=496) and Qwen (n=475); G redefined as per-problem median ratio with bootstrap CIs; QW s015 G marked "n.d." (II_high~0, CI spans zero)
- **M3**: Abstract G range updated to 7.5--79.8x with bootstrap 95% CI [4.1, 96.5]

### Narrative and Framing
- **N2**: Section 6 restructured --- discrimination collapse framed as correlational diagnostic (not mechanism); structural specificity introduced as key differentiator; per-sparsity matched imp/rand Delta-Gini comparison added; entropy redistribution trimmed to supplementary observation (~50 words)
- **W2**: Introduction novelty argument rewritten --- explicitly cites HIES, ThinKV, Sparse Frontier as single-axis baselines; explains why their linear combination cannot predict sign reversal (crossover) or multiplicative-null excess (2.7x)
- **W4**: Characterization value paragraph added to Discussion

### Statistical Rigor
- **W1**: Spearman rho=1.0 downgraded to footnote; Jonckheere-Terpstra test promoted to primary dose-response statistic (z=6.2--33.7)
- **W5**: Entropy redistribution trimmed; model-dependent direction reversal acknowledged

### Scope and Limitations
- **W3**: PPL-to-accuracy limitation paragraph added to Limitations
- **W6**: LLaMA footnote added noting CI/Wilcoxon discrepancy under small n with heavy-tailed distributions

### Citations and References
- **N3**: ThinKV attribution corrected in Background
- **W7**: "Hold Onto That Thought" (NeurIPS 2025) citation added to Related Work and KV cache eviction paragraph
- **W8**: H2O bib entry simplified (removed \textsubscript markup)
- **M4**: LongFlow "withdrawn" note removed
- **M5**: SnapKV author list verified against arXiv

### Housekeeping
- **M1**: \placeholder macro deleted from main.tex
- **M2**: Orphaned appendix_results.tex deleted (duplicate labels resolved)

---

## Reviewer Comments

*(Per-comment responses to be filled upon receipt of formal reviewer comments)*
