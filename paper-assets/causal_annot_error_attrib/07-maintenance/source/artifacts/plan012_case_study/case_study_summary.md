# Case Study: ASV diagnosis of an LLM-based labor-market causal estimate

## Selected paper

**Title.** "The (Short-Term) Effects of Large Language Models on Unemployment and Earnings"
**Identifier.** arXiv:2509.15510 (Sushkov et al., 2025)
**Outcome data.** US CPS occupation panel, Jan 2010 – Aug 2025 (188 months)
**Exposure measure.** Per-occupation share of O*NET tasks that Claude
(Anthropic Economic Index; Handa et al. 2025) classified as
*automative*, *augmentative*, or *neither* (K=3).
**Estimator.** Synthetic difference-in-differences with binary treatment
(above-median exposure × post-Nov-2022 indicator).
**Headline result.** +$89 weekly earnings (2010 USD) for exposed
occupations; SE≈$20; near-zero change in unemployment.

## Why this paper

- **Real LLM annotation, real causal estimate.** Anthropic's economic
  index is now the dominant input to AI-labor regressions; downstream papers
  using it inherit any classification error.
- **Clean K=3 categorical mapping.** Tasks are classified into three
  exclusive labels (automative / augmentative / neither), so our K=3
  exposure plim machinery applies directly without coarsening.
- **Fragile topology.** A is on the exposure node of A→Y; our taxonomy
  (Table 1) flags this design as one of two configurations capable of
  catastrophic bias under non-differential misclassification.
- **Quantitative anchoring.** The reported $89 / SE $20 effect lets us
  translate ASV ratios into dollars.

## DAG analysis

```
Claude (Handa et al.)        SDiD comparison
        |                          |
        v                          v
A* (task label)  ->  Exposure_o  ->  Y (occupation earnings)
        ^
   true A unobserved
```

- **A** = true task category (automative / augmentative / neither).
- **A*** = Claude's classification, the only one observed.
- **Y** = post-ChatGPT change in occupation weekly earnings.
- **No treatment variable** beyond exposure itself, hence the *exposure*
  topology — the most fragile non-IV row of Table 1.

## Framework analysis

We solve the K=3 exposure plim
$\tau_\text{biased} = (E[ZZ^{*\top}])^{-1} E[Z^* Y]$ for
three confusion matrices spanning published Claude/GPT-4 coding agreement
rates (Handa et al. 2025; Halterman & Keith 2024):

| Scenario  | Diagonal | bias\_auto  | magnitude ASV (10%) | sign-flip ASV |
|-----------|----------|-------------|---------------------|---------------|
| Best      | 0.90     | −12.8%      | **0.79**            | 6.4           |
| Realistic | 0.80     | −27.8%      | **0.37**            | 3.2           |
| Weak      | 0.70     | −43.1%      | **0.24**            | 2.1           |

Monte-Carlo over Dirichlet random matrices anchored at each diagonal level
(N=500 each) recovers the same pattern with p95 |bias| of 35% / 56% / 74%.
No sign reversals occur within δ≤1 for diag≥0.8; a 0.6% sign-flip rate
appears at diag=0.7 (median sign-flip ASV 0.93).

## Substantive verdict

1. **Magnitude is fragile.** At realistic Claude accuracy (~0.80
   diagonal), the automative-task earnings coefficient is attenuated by
   ~28%. Translating to the headline SDiD effect, the true earnings
   differential could plausibly be \$110–\$140 / week rather than \$89.
2. **Sign is robust.** Sign-flip ASV of 3.2 means the qualitative
   conclusion (positive earnings effect) survives unless Claude's
   classifier is more than 3× worse than the realistic scenario.
3. **Recommendation.** Plug a 10% human-audited subsample into PPI++
   (this paper, Sec. 5.4 / Eq. (15)). Empirical PPI++ achieves 96.4%
   bias-reduction at K=3 with the same labeled fraction, recovering the
   unattenuated coefficient without re-running the SDiD pipeline.

## Caveats

- **K-coarsening at occupation level.** The paper's SDiD treatment is
  *above-median exposure*, a binary aggregate of per-task K=3 labels.
  We analyse the underlying task-level primitive; the aggregate-level
  bias is a smooth function of the primitive bias (Section 4.4 of this
  paper) so the qualitative ASV verdict carries over, but the
  occupation-level magnitude attenuation could be smaller than 28%
  through Jensen-style averaging.
- **No published audit of Handa et al.'s Claude classifier.** Our
  diag=0.80 baseline reflects the typical zero-shot LLM coding accuracy
  reported in Halterman & Keith (2024) and Pangakis et al. (2025), not
  a direct audit of the Anthropic Economic Index.

## Artefacts

| File | Contents |
|------|----------|
| `case_study_analysis.py` | Reproduces all numbers (point + 500-sample Monte-Carlo) |
| `case_study_results.json` | Machine-readable point + MC tables |
| `case_study_paragraph.tex` | 200-word paragraph drop-in for `experiments.tex` |
| `case_study_summary.md` | This document |

## References

- Sushkov et al. (2025). *The (Short-Term) Effects of Large Language Models
  on Unemployment and Earnings.* arXiv:2509.15510.
- Handa et al. (2025). *Anthropic Economic Index.* anthropic.com.
- Halterman & Keith (2024). *Codebook LLMs.* arXiv:2407.10747.
- Pangakis et al. (2025). *Large Language Model Hacking.* arXiv:2509.08825.
