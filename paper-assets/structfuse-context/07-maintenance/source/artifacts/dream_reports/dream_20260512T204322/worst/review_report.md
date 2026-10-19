---
dream_id: dream_20260512T204322
tier: worst
overall_score: reject
timestamp: 2026-05-12T20:55:00+00:00
---

# Dream Review Report — worst tier

- **Dream ID**: 20260512T204322
- **Tier**: worst
- **Paper**: "Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet): An Empirical Analysis of Three Negative Mining Strategies"
- **Review Mode**: full (2 Reviewers + roundtable)
- **Overall Score**: reject

---

## Headline Assessment

**Reject.** The paper presents a potentially interesting negative result — structure-grounded hard negatives via CodeQL 2-hop call-graph analysis don't improve code retrieval — but the manuscript has critical integrity issues (fabricated model name, placeholder reference, missing citations for discussed works) and overclaims its statistical evidence. The experimental analysis, while well-structured at a high level, is unreproducible due to missing hyperparameters and has a dangerously thin related work section (9 references). The core empirical insight (Z% sparsity and hop-bounding dilemma) is genuinely informative but buried under execution problems.

---

## Reviewer 1: Methods + Experiments

### Strengths

1. **Well-structured comparison**: 3 strategies x 3 seeds x 4 evaluation settings is a reasonable experimental matrix for a negative-result paper.
2. **Z% diagnostic metric**: Defining and measuring the fraction of instances with non-trivial structural signal is a useful methodological contribution. Table 1's breakdown by repository size is informative.
3. **Hop-bounding tradeoff (Table 4)**: The analysis showing no hop setting simultaneously achieves Z > 20% and timeout < 10% is the paper's strongest analytical result.
4. **Stratified embedding-distance analysis (Table 6)**: The finding that embedding-distance harm concentrates in high-similarity codebases (p = 0.008) is a salvageable practical insight.

### Weaknesses

#### Critical

1. **"Qwen3.6-27B" is not a real model.** Qwen models use the Qwen2.5-XB naming convention. No model called "Qwen3.6-27B" exists in any public release. This makes the entire SWE-bench Lite evaluation (Table 3) unverifiable. If the agent model is fabricated, the end-to-end results are meaningless.

2. **SweRank reference is a placeholder.** The citation reads "arXiv:2405.xxxxx" — a literal unfilled template. This is a basic manuscript integrity failure and would be grounds for desk rejection at any venue.

3. **Missing critical hyperparameters.** The paper does not report: LoRA rank/alpha, learning rate, batch size, number of epochs, warmup schedule, the embedding model used for the embedding-distance strategy, or the InfoNCE temperature. Reproduction is impossible.

4. **Threshold tau is undefined.** The dataflow-aware strategy (Section 3.2) uses s(x,q) > tau to filter candidates, but tau is never specified, and no sensitivity analysis is provided. This is a free parameter that could significantly affect whether structure-grounded negatives help or harm.

5. **SWE-bench claims overclaim statistical evidence.** The paper acknowledges in Section 4.3 that "all three strategies and the SweRank baseline fall within the 95% confidence interval (plus/minus 2.5pp), making them statistically indistinguishable," yet the abstract claims both hard negative strategies underperform random "across all evaluation settings." This is a direct contradiction.

#### Major

6. **Only 3 seeds for variance estimation.** With n=3, the standard deviation estimates (Table 2) have very high uncertainty. The reported plus/minus values are unreliable for distinguishing methods.

7. **Pool size = 200 is unrealistically small.** Real-world code retrieval operates over hundreds to thousands of files per repository. A 200-file pool may not reflect actual retrieval difficulty and inflates absolute recall numbers.

8. **SWE-bench agent confound is uncontrolled.** The LLM agent's ability to use retrieved context may vary across retrieval strategies in ways the evaluation can't isolate. No ablation on agent sensitivity to retrieval quality is provided.

9. **SweRank comparison is structurally unfair.** SweRank is trained on a larger corpus, making it an incomparable baseline. Including it in Table 3 without this caveat in the table caption is misleading.

10. **Table 5 scaling ablation is one-sided.** Only the dataflow strategy is scaled against random. Embedding-distance scaling behavior is missing, preventing a complete picture.

11. **Instance count discrepancy.** Table 1 reports 18,200 instances total, but Section 3.3 says "~15K training instances." ~3,200 instances were dropped without explanation.

12. **Fusion head ablation (Table 7) is undescribed.** The fusion architecture (concatenation? attention? gating?) is not specified. Results are uninterpretable.

13. **Contribution 2 contains a placeholder.** The text reads "(Z%)" where presumably "14%" was intended — evidence of incomplete manuscript preparation.

#### Minor

14. **Manual analysis (Table 8)** uses 50 cases with apparently a single annotator. No inter-annotator agreement is reported. Sample size is marginal for a claimed contribution.

15. **InfoNCE loss details** (number of negatives per positive, temperature) are unspecified.

### Questions for Authors

1. What is the value of tau, and how sensitive are the dataflow-aware results to this threshold?
2. What LoRA configuration was used (rank, alpha, target modules)?
3. What is "Qwen3.6-27B"? Is this a typo for an existing model (e.g., Qwen2.5-32B)?
4. How were the ~15K training instances selected from the 18.2K extracted?
5. What fusion architecture underlies Table 7?

---

## Reviewer 2: Novelty + Related Work

### Strengths

1. **Negative results have value.** The framing as "empirical analysis" rather than "failed experiment" is appropriate when well-executed.
2. **Z% sparsity insight.** The discovery that structural signal density drops from 40.8% (pilot) to 14% (full scale) due to medium-repository sampling bias is a genuinely useful methodological warning.
3. **Conditional embedding-distance finding (Section 5.3)** is the most actionable result: avoid embedding-distance negatives in high-similarity codebases.
4. **Failure taxonomy categories are intuitive.** Config/setup and doc-adjacent categories clarifying call-graph blind spots are useful for future work.

### Weaknesses

#### Critical

1. **Extremely thin references (9 total).** An empirical analysis comparing negative mining strategies cites only ONE paper on hard negative mining (Robinson et al. 2021). Glaring omissions include:
   - ANCE (Xiong et al. 2021) — seminal work on approximate nearest neighbor negatives
   - Kalantidis et al. 2020 — hard negatives in contrastive vision
   - Curriculum learning / progressive hard negative mining literature
   - GraphCodeBERT, CodeBERT, UniXcoder — structural code representation models
   - AST, PDG, control flow graph approaches to code structure

2. **Multiple cited works have NO reference entries.** CoCoHaNeRe, LocAgent, RANGER, and CodexGraph are all discussed in Section 2 as related work but have no corresponding reference entries. This is a basic scholarly integrity failure — four "phantom citations."

3. **Placeholder reference.** SweRank is cited as "arXiv:2405.xxxxx" — an unresolved placeholder. Combined with the phantom citations, this suggests the manuscript was not ready for any form of review.

4. **Abstract overclaims.** "across all evaluation settings" is contradicted by the paper's own Section 4.3 admitting SWE-bench results are "statistically indistinguishable."

#### Major

5. **Narrow scope, broad claims.** Only one structural signal (CodeQL 2-hop call graph), one model (Qwen2.5-Coder-3B), one language (Python). The conclusions and practical recommendations are stated far more broadly than the evidence supports. Section 7's cross-domain generalization paragraph (molecular networks, circuits, knowledge graphs) is pure speculation.

6. **Eq. 1 formalization is misleading.** The formal definition creates an impression of a principled method, but Section 3.2 reveals that 86% of the time the method degenerates to random sampling. The gap between the elegant formalization and the degenerate reality is not adequately flagged upfront.

7. **"Yet" in title is aspirational, not empirical.** Section 7 mentions import graphs, type hierarchies, test-source mappings, and learned structural embeddings as future directions but provides zero evidence or pilot data. The "yet" suggests forthcoming solutions that the paper does not support.

8. **"Sufficiently diverse" qualifier is undefined.** Contribution 1 claims hard negatives underperform "when the candidate pool is sufficiently diverse." This qualifier is never formally defined or experimentally tested. What pool size threshold makes a pool "sufficiently diverse"?

9. **Scaling claim overreach.** Section 5.2 claims "This rules out the hypothesis that more data would rescue the approach" based on scaling only to 5K instances, when the full training set is 15K. Testing 1/3 of the data range does not definitively rule out the hypothesis.

#### Minor

10. **Failure taxonomy (50 cases) is undersized** for a standalone "contribution." Single annotator, no inter-rater reliability.

11. **"Qwen3.6-27B"** — same fabrication concern flagged by R1. Undermines the entire end-to-end evaluation.

### Story Consistency Analysis

| Check | Verdict |
|-------|---------|
| Abstract claims vs. Results | **Inconsistent** — SWE-bench "across all settings" claim contradicts Section 4.3 CI analysis |
| Eq. 1 formalization vs. Actual method | **Misleading** — 86% fallback to random not flagged in formal presentation |
| Contributions claimed vs. Delivered | **Partial** — Contribution 1 supported; Contribution 2 has placeholder; Contribution 3 undersized |
| Title "Yet" vs. Evidence | **Unsupported** — no pilot data for alternative structural signals |
| Pilot Z=40.8% vs. Full Z=14% | **Consistent** — adequately explained by sampling bias |

---

## Cross-Reviewer Synthesis (Roundtable Steps 2-3)

### R1 commentary on R2's findings

- The missing references (CoCoHaNeRe, LocAgent, etc.) are a methodological problem too — without proper baselines cited, it's impossible to assess whether the experimental comparison is complete.
- The Eq. 1 formalization vs. 86% fallback issue raised by R2 has direct experimental implications: the "dataflow-aware" strategy is effectively "86% random + 14% dataflow-modified." This should have been ablated as a mixture rather than treated as a distinct strategy.
- The fabricated model name "Qwen3.6-27B" makes the entire SWE-bench evaluation unverifiable from both perspectives.

### R2 commentary on R1's findings

- The missing hyperparameters (tau, LoRA config, etc.) compound the citation problem — not only is the method poorly contextualized in the literature, it's also unreproducible.
- The pool size = 200 concern connects to the "sufficiently diverse" claim — if the pool is small, the entire argument about random negatives implicitly sampling diversity is weakened.
- The Table 1 to Section 3.3 instance count discrepancy (18.2K vs. ~15K) is a data integrity issue that further weakens confidence.

### Convergence

Both reviewers independently converge on **reject** with overlapping critical concerns:

1. **Manuscript integrity failures** — placeholder reference (SweRank arXiv:2405.xxxxx), fabricated model name (Qwen3.6-27B), four phantom citations (CoCoHaNeRe, LocAgent, RANGER, CodexGraph), placeholder in contribution text "(Z%)". These alone warrant rejection before evaluating scientific merit.

2. **Overclaimed abstract** — The "across all evaluation settings" claim is directly contradicted by the paper's own statistical analysis of SWE-bench results.

3. **Unreproducible** — Missing tau threshold, LoRA config, learning rate, batch size, epochs, embedding model, fusion architecture, InfoNCE temperature.

4. **Inadequate scholarship** — 9 references for an empirical analysis paper; the hard negative mining literature is represented by a single citation.

### Where Reviewers Diverge

- R1 (methods/experiments) finds the experimental *structure* reasonable and gives credit for the hop-bounding analysis and stratified embedding findings. Leans **weak reject**.
- R2 (novelty/related work) views the manuscript as fundamentally unready due to citation failures and overclaims. Leans **strong reject**.

### Final Consensus

The gap between R1 and R2 reflects the split between "interesting idea, poor execution" vs. "not ready for any venue." The fabrication/placeholder issues tip the balance toward the latter. **Reject** (closer to strong reject).

---

## Worst-Tier Consistency Assessment

This paper is **consistent with a worst-tier dream outcome**. The worst tier is expected to exhibit:

- **Core negative result with thin support**: The central finding (structure-grounded negatives don't help) is plausible but the evidence is undermined by integrity issues.
- **Overclaimed conclusions relative to evidence**: Abstract claims exceed what the statistics show.
- **Incomplete manuscript preparation**: Placeholders, phantom citations, missing hyperparameters, potentially fabricated model names.
- **Narrow scope with broad claims**: One signal type, one model, one language, but general recommendations.

The paper has a kernel of genuinely useful analysis (Z% sparsity, hop-bounding dilemma, conditional embedding-distance harm) that a better execution could salvage — but in its current form, the manuscript integrity issues make it unsuitable for submission.

---

## Actionable Feedback for Revision

1. **Fix all placeholder/phantom references immediately.** Every work discussed in text must have a complete reference entry.
2. **Verify and correct the agent model name** (Qwen3.6-27B to actual model).
3. **Report all hyperparameters** in a dedicated table or appendix: LoRA rank/alpha, LR, batch size, epochs, tau, InfoNCE temperature, embedding model.
4. **Soften SWE-bench claims** to match the plus/minus 2.5pp CI reality. Use "consistent trend" rather than "underperform across all settings."
5. **Expand related work** to at least 25-30 references covering hard negative mining (ANCE, curriculum HN), code structure (GraphCodeBERT, ASTs), and the missing cited works.
6. **Ablate tau sensitivity** — even 3 values would strengthen the paper significantly.
7. **Increase manual analysis** to 100+ cases with a second annotator and inter-rater agreement.
8. **Reframe Eq. 1** to explicitly note the fallback behavior and the 86% degeneracy rate.
