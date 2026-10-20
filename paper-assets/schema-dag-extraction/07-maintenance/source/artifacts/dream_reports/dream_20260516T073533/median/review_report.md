---
dream_id: dream_20260516T073533
tier: median
overall_score: weak reject
timestamp: 2026-05-16T08:20:35.591137+00:00
---


# Reviewer 2 (R2): Novelty, Related Work, Framing, Contribution Significance

## 1. Summary

This paper conducts a controlled empirical study to disentangle two factors driving degradation in training-free LLM information extraction on complex schemas: type count (which suppresses recall) and type confusability (which causes type substitution errors). The authors introduce the Schema Confusability Score (SCS), demonstrate its correlation with empirical confusion across NER, RE, and ED tasks, identify a centrality confound on homogeneous schemas, and show that naive schema decomposition fails for NER due to merge amplification while yielding a marginal (non-significant) gain for RE. The paper is framed as a "diagnostic framework" but is substantively an empirical analysis paper with negative practical results.

## 2. Strengths

- **Well-designed controlled experiments.** The two-paradigm design (count curves + BCS-controlled) is methodologically sound and represents genuine effort to isolate confounding factors. The within-pool analysis (drawing 16-type subsets from the 80-type pool) is a particularly careful control that strengthens the causal interpretation. The permutation test for cross-pool slope consistency (p=0.60) is the right statistical approach.

- **Honest and transparent reporting of negative results.** The paper is admirably forthright about SDGD's failure, the non-significant factorial interaction (p=0.50), the modest pairwise effect sizes (R^2 = 1.3-1.7%), the non-significant RE batch composition gain (p~0.19), and the DocRED BCS effect at higher counts. This level of transparency is uncommon and commendable.

- **Centrality confound analysis is a genuine methodological insight.** The identification that per-type BCS aggregation conflates confusability with centrality on same-domain schemas (MAVEN), supported by the residualized analysis and connected to the embedding anisotropy literature, is the paper's strongest conceptual contribution. The connection to Cai et al. (2021) on local isotropy within clusters is well-motivated.

- **Cross-model and cross-dataset validation.** Testing on Llama-3.1-8B and across four datasets (Few-NERD, FewRel, DocRED, MAVEN) spanning three tasks provides reasonable breadth. The convergent high-BCS floor (~51%) across models is an interesting empirical observation.

- **Thorough limitations section.** Ten specific, substantive limitations are listed, covering model coverage, effect sizes, metric scope, and causal mechanism. This is well above average for the field.

## 3. Weaknesses

- **(Major) The "multi-channel degradation framework" formalizes well-known intuitions without substantial novelty.** That more categories cause confusion and that similar categories are more easily confused are foundational observations in psychophysics, categorical perception, and fine-grained classification. The paper's framing as a "framework" overstates what is essentially empirical quantification of these known effects in a specific (LLM IE) setting. The "two channels" are not discovered mechanisms but labels for expected phenomena. The paper would benefit from honestly positioning itself as "quantifying the magnitude and separability of known factors in a new setting" rather than "identifying" or "discovering" channels. Claiming these as "orthogonal" is also misleading given the non-significant interaction test (p=0.50) -- non-significance does not establish orthogonality, it merely fails to reject additivity.

- **(Major) Pairwise SCS explains 1.3-1.7% of variance -- the practical utility of the confusability metric is questionable.** The authors acknowledge this but argue the signal "compounds at the batch level." However, the compounding argument is not rigorously established. The 31.2pp extreme-batch gap is between the *most extreme* possible batches across 80 types; the typical-batch gap is 2-4pp (Section 4.3). For a metric proposed as a "diagnostic tool," explaining ~1.5% of pairwise variance and producing ~3pp typical-batch differences is underwhelming. The paper does not convincingly demonstrate that SCS provides actionable information beyond "avoid putting obviously similar types together" -- which practitioners already know.

- **(Major) The main practical contribution (SDGD / confusability-aware batching) either fails or is non-significant.** SDGD fails catastrophically on NER. The RE batch composition gain is +1.4pp with p~0.19, which is not significant. The paper frames this as a "directionally consistent" result, but at a top venue, non-significant results cannot be claimed as evidence for a method's utility. The confusability-aware strategy ranks 13th out of 15 random seeds -- essentially indistinguishable from random. This means the paper has no actionable positive practical result.

- **(Major) Incomplete related work -- several directly relevant lines of work are missing or underexplored.** The related work section, while improved from earlier drafts, still misses or underengages with:
  1. **Fine-grained classification and label confusion literature** -- extensive work in computer vision (e.g., hierarchical classification, label smoothing based on semantic similarity) directly parallels the confusability findings. The observation that similar labels confuse classifiers is well-established in that community.
  2. **Prompt engineering for structured output** -- work on structured/constrained decoding (e.g., LMQL, Guidance, Outlines) that avoids type confusion entirely by construction.
  3. **Code-generation approaches (GoLLIE, CodeIE)** that sidestep schema confusion by representing types as code constructs rather than natural language labels in a list -- GoLLIE is cited but the key insight (that code-style schemas may inherently reduce confusability by leveraging syntactic structure) is not discussed.
  4. **The cognitive science literature on similarity-based interference** in categorization (e.g., exemplar models, prototype theory) that would provide theoretical grounding for the "semantic interference" channel.
  5. **CROSSAGENTIE** (cited but insufficiently engaged) -- their cross-type debate mechanism directly addresses type confusion post-hoc, and the paper should discuss whether their approach implicitly validates the confusability channel.

- **(Major) Single primary model severely limits generalizability claims.** Qwen3-32B is the primary model for all experiments. Llama-3.1-8B validation is partial (Channel 2 not reproduced on NER). No proprietary models tested. The convergent high-BCS floor at ~51% is observed on exactly two models -- calling this a "task-inherent difficulty ceiling" is a stretch. The paper acknowledges this in limitations but the claims in the body text often read as more general than the evidence warrants.

- **(Minor) The error taxonomy is descriptive, not a methodological contribution.** Categorizing errors into IntraSub/ExtraSub/Boundary/Hallucination and showing that IntraSub correlates with BCS is descriptive analysis, not a new methodology. The high Spearman rho values (1.0 for NER, 0.954 for RE) are computed over only 4-5 bins, making these rank correlations almost trivially perfect. With 4 bins, any monotonic trend gives rho=1.0. This should not be presented as strong evidence.

- **(Minor) SCS is cosine similarity of type name embeddings -- this is an extremely simple metric.** No type definitions, no examples, no ontological structure. The paper demonstrates that this simple metric captures *something* but the R^2 values suggest it captures very little. More sophisticated confusability measures (e.g., using type definitions, few-shot examples, or the model's own attention patterns) are not explored. Calling this a "Score" and giving it an acronym elevates a basic similarity computation beyond what it warrants.

- **(Minor) The "schema design guidelines" in the discussion are generic.** "Prefer single-pass," "use random batching if needed," "prefer hierarchical schemas" -- these are either obvious or insufficiently supported by the experiments. The paper does not test hierarchical schemas; it only observes that cross-domain schemas behave differently from same-domain ones.

- **(Minor) MAVEN results weaken the narrative.** The count curve goes in the opposite direction (performance increases with more types), the per-type BCS correlation is opposite to the hypothesis, and the pairwise signal exists only with MiniLM (not Qwen3). While the centrality confound analysis is interesting, having one of three primary tasks contradict the main story is a significant caveat.

## 4. Questions for Authors

1. Given that pairwise SCS explains only 1.3-1.7% of variance and the typical-batch accuracy gap is 2-4pp, what is the concrete use case for SCS that goes beyond the intuition "don't put similar types together"? Can you provide a scenario where computing SCS would change a practitioner's decision?

2. The non-significant interaction (p=0.50) is described as "underpowered." What sample size would be needed to detect the interaction at the observed effect size? Have you conducted a power analysis? Without one, claiming underpoweredness is speculative.

3. Why was no attempt made to use more informative confusability metrics (e.g., incorporating type definitions, annotation guidelines, or few-shot confusion matrices)? The SCS metric uses only type name strings, which seems to leave substantial signal on the table.

4. GoLLIE and similar code-generation approaches represent types as Python classes rather than items in a list. Have you considered whether such representations inherently reduce the confusability channel? This seems like a natural baseline that would contextualize the practical significance of your findings.

5. The convergent high-BCS floor at ~51% is observed on exactly two models. What is your basis for describing this as a "task-inherent difficulty ceiling" rather than a coincidence? Would you expect this to hold for GPT-4 or Claude?

6. For the RE batch composition experiment, the confusability-aware strategy produces an intra-batch BCS reduction of only 0.006 (0.552 vs 0.559). Is this simply a ceiling effect of graph coloring at this granularity? What BCS reduction would be needed to produce a significant accuracy gain, based on your regression models?

7. The claim that the two channels are "orthogonal" appears throughout the framing materials and earlier drafts. The current paper is more careful, but the title of the DREAM-generated paper still says "orthogonal failure modes." Can you precisely define what "orthogonal" means here given the non-significant interaction test?

## 5. Assessment of Contribution Significance

The paper's contributions, taken individually, are each below the threshold for a top venue:

- **The "multi-channel degradation framework"** formalizes known intuitions. The observation that count and similarity independently affect classification is not novel in itself; what would be novel is a precise mechanistic account (e.g., at the attention level) of how this happens in LLMs specifically.

- **Pairwise confusability validation** produces statistically significant but practically tiny effects (R^2 < 2%). The BCS-controlled experiments show larger gaps but only under extreme conditions; typical conditions yield ~3pp differences.

- **Negative results on SDGD** are informative but the merge amplification phenomenon is essentially "running the same model on the same text multiple times produces inconsistent outputs" -- this is a known property of LLMs, not a discovery.

- **Confusability-aware RE batching** is non-significant (p~0.19).

- **The centrality confound** is the most interesting finding but is a supporting observation, not a primary contribution.

Taken together, the paper provides a useful but incremental empirical characterization. It is a solid workshop paper or a reasonable Findings paper. The controlled experimental design is above average, the transparency is commendable, but the novelty and practical impact do not reach the bar for a main conference paper at a top venue.

The paper would be substantially strengthened by: (1) mechanistic analysis (e.g., attention patterns showing how confusable types interfere), (2) a confusability metric with higher predictive power, (3) a practical mitigation that actually works with statistical significance, or (4) validation on proprietary models to establish generality.

## 6. Preliminary Score and Confidence

**Score: 3 (Weak Reject)**

**Confidence: 4 (High)**

**Justification:** The experimental methodology is careful and the transparency is commendable, but the core contributions do not clear the novelty and significance bar for a top venue. The "framework" formalizes known intuitions, the confusability metric has very low explanatory power, all practical interventions either fail or are non-significant, and MAVEN partially contradicts the narrative. The paper reads as a thorough empirical exploration rather than a paper with a clear, strong takeaway that advances the field. The related work has notable gaps. For EMNLP main, I would need either a stronger novel insight, a working practical method, or mechanistic depth that the current version does not provide. I would support acceptance at Findings.
