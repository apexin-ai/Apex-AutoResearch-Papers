# Round 10 Paper Corrections Log

Date: 2026-05-16

## Applied Edits

### 1. Abstract + Intro: Δ as headline (R10-W6)
- **abstract.tex**: G demoted from co-equal "with" clause to parenthetical `(amplification ratio G=7.5--79.8×)`
- **abstract.tex**: Cross-arch evidence changed from "exploratory...suggesting the qualitative pattern may extend" to "preliminary but inconclusive"
- **introduction.tex** (line 12 area): G already positioned as exploratory; no change needed
- **introduction.tex** (Contribution 2, line 26): Changed "preliminary evidence...suggesting" to "preliminary but inconclusive evidence"
- **introduction.tex** (line 17): Changed "preliminary evidence...suggests" to "preliminary but inconclusive evidence...suggests"
- **conclusion.tex**: G demoted from "with amplification ratios" to parenthetical

### 2. Contribution 3: Remove causal language (R10-C5)
- **introduction.tex** (line 27): Changed "correlated with but not sufficient for severity amplification, with the structural specificity of pruned heads as the key differentiator" → "associated with severity amplification; the structural specificity of importance-pruned heads corresponds to the 15--17× severity divergence between strategies"

### 3. Footnote 2: float16/bfloat16 (R1 §4)
- **Already correct**: methodology.tex footnote reads "An earlier float16 configuration produced sporadic NaN values; bfloat16 eliminated all occurrences."

### 4. GPU anonymization (R1 §4)
- **Already anonymized**: methodology.tex footnote reads "4× professional GPUs with 48 GB memory" — no specific GPU model named.

### 5. §5.5 Cross-Architecture: language downgrade (R1+R2)
- **results.tex** (line 93): Changed "detects the phase-gated severity pattern" → "provides preliminary support for the phase-gated severity pattern"
- Abstract and intro also updated (see item 1)

### 6. §5.6 GSM8K: random eviction power analysis (R1-W6)
- **results.tex** (line 101): Replaced vague power statement with explicit: "Post-hoc power analysis indicates n=50 can detect effects of d≥0.40 (α=0.05, power=0.80); all random conditions showed |d|≤0.164, meaning the null results may reflect insufficient power rather than true absence of effect."

### 7. §5.7 CoT faithfulness citations (R1-W3)
- **Already present**: results.tex line 129 cites `\cite{lanham-2023-faithfulness, turpin-2023-biased-cot}`. Bib entries exist in references.bib.

### 8. §6.2 Entropy section title (model-dependence)
- **Already correct**: analysis.tex subsection title is "Entropy Redistribution: A Model-Dependent Secondary Effect"

### 9. §7 Discussion: pilot CI + H2O downgrade
- **Already correct**: discussion.tex already states "the CI spans zero, indicating no statistically distinguishable improvement" and uses "We hypothesize" + "open question for future work" for H2O/SnapKV/PyramidKV.

### 10. §5.8 Accuracy: Qwen vs DS reliability (R1-W3)
- **results.tex** (line 136): Added explicit reliability caveat: "Given minimal truncation, Qwen accuracy data provide a reliable PPL-accuracy bridge; DeepSeek accuracy results, confounded by truncation rates of 16%--76%, should be interpreted as qualitative observations only."

### 11. Bonferroni family definition (R1-W4)
- **Already present**: methodology.tex defines k=4 rationale ("each family tests a single directional question...making k=4 the natural grouping") and references BH-FDR appendix.

## Files Modified
- `abstract.tex` (2 edits)
- `introduction.tex` (3 edits)
- `results.tex` (3 edits)
- `conclusion.tex` (1 edit)

## No-Change Items (already correct)
- `methodology.tex` — footnote 2 and Bonferroni already fixed
- `analysis.tex` — entropy title already correct
- `discussion.tex` — pilot CI and H2O language already correct
- `references.bib` — Lanham and Turpin citations already present
