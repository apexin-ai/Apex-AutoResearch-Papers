# Adversarial Review Round 1

## Overall Assessment
Rating: 5/10 (Borderline reject)
Confidence: 4/5

## Summary
This paper formalizes recursive generation depth estimation as ordinal classification, constructs a 3x3 benchmark (3 models x 3 strategies x 4 depths), and presents a "Depth Degradation Atlas" characterizing how statistical features evolve across depths. The core finding is that perplexity tail statistics (p90_ppl, var_surprisal) are universal depth markers achieving 70-85% four-class accuracy via Random Forest. The EDD metric quantifies the discriminability frontier. The work is thorough within its controlled scope but raises concerns about ecological validity, scalability, and the gap between the controlled setting and real-world recursive contamination.

## Strengths
1. **Genuine task novelty.** No prior work estimates ordinal recursive generation depth from text alone. The problem formalization is clean and the EDD metric is a useful contribution that could become standard for this research direction.

2. **Systematic experimental design.** The 3x3 grid with per-class recall reporting, cross-model/cross-strategy LOO, multiple importance measures (SHAP/Gini/permutation with Kendall's W=0.90), and threshold sensitivity analysis demonstrates rigorous methodology. The domain bias analysis (LOGO, seed-group negative control) is particularly commendable.

3. **Feature universality finding is scientifically interesting.** p90_ppl ranking top-2 in 9/9 cells and var_surprisal in 8/9 under SHAP, with mean cross-model Spearman rho=0.868, is a non-trivial finding that constrains the hypothesis space for future work.

4. **Honest limitations reporting.** The paper does not hide the d0 inflation problem, the cross-strategy breakdown, the temperature inversion, or the C4 FPR issues. The d1-d3 numbers are transparently reported alongside headline figures.

5. **End-to-end comparison validates feature approach.** The DeBERTa/RoBERTa comparison with linear probing showing negative R^2 for key features provides a compelling mechanistic explanation for why PLM representations cannot solve this task, not just a performance gap.

6. **Multi-temperature ablation with mechanistic insight.** The "memorization as prerequisite" finding (training loss analysis across tau values) is the most scientifically interesting result in the paper—it connects depth discriminability to a fundamental property of the recursive training process.

## Weaknesses (ranked by severity)

### Critical (must fix before submission)

1. **Ecological validity gap undermines practical framing.** The entire benchmark uses Wikipedia seed text with LoRA finetuning (r=16, 3 epochs) and BOS-seeded generation without prompts. Real-world recursive contamination involves: (a) full pretraining or extensive finetuning, (b) prompt-conditioned generation, (c) mixed-source corpora, (d) partial contamination at unknown proportions. The paper frames the contribution as addressing "web-scraped training corpora increasingly contain multi-generational synthetic content" (Intro, line 1), yet the experimental setting diverges so far from this scenario that the connection is aspirational rather than demonstrated. The WikiText/C4 calibration experiment (Section 5.5) only tests FPR on human text—it never tests whether the classifier can identify recursively contaminated web text produced under realistic conditions. **The paper should either reframe as a controlled proof-of-concept without practical deployment claims, or provide at least one realistic-pipeline experiment.**

2. **Scale limitation is a fundamental threat to the "universality" claim.** Three models (1B-1.5B) with diverse architectures is presented as evidence of universality, but they share a critical property: at this scale, recursive finetuning induces rapid memorization and visible distributional collapse. Modern frontier models (7B-70B+) generate more fluent text with narrower perplexity distributions—the very tail features that dominate here may be compressed below noise at scale. The Discussion paragraph on scaling (lines 42-46 of discussion.tex) is entirely speculative ("we therefore expect depth estimation to remain feasible") with no empirical support. Given that this is the paper's primary claim, at minimum one 7B model result is needed to make "universality" credible beyond the narrow 1-1.5B scale band.

3. **Cross-strategy transfer failure makes deployment infeasible.** The headline 59.1% drops to 45.9% excluding d0 (chance=33%). The temperature d1/d2 AUC inversion (0.13-0.25) means the classifier actively produces *wrong ordinal rankings* when the strategy is unknown. The proposed mitigation (two-stage pipeline with strategy identification) is entirely hypothetical. This isn't a minor limitation—it means the system cannot be deployed on "web-scraped training corpora" where decoding strategy is inherently unknown. The paper needs to either demonstrate the two-stage pipeline works, or significantly narrow its practical claims.

### Major (should fix)

4. **Headline accuracy inflation.** The abstract reports "70-85% four-class accuracy" but d0 is trivially separable (>98% recall). The meaningful performance—distinguishing between different depths of synthetic text—is the d1-d3 accuracy: 58.8-82.6% in-distribution, 55.4% cross-model, 45.9% cross-strategy. These should be the headline numbers. The current framing creates an impression of stronger performance than the system delivers for the hard part of the task.

5. **Curation PoC does not support the framing.** The paper frames depth-graduated curation as a practical implication, but Table 9 (Appendix) shows rf_soft vs unfiltered: p=0.407, i.e., RF filtering does NOT improve over using all data unfiltered. The finding is actually "RF >> random subsampling" which merely shows that informed selection beats random selection—a trivially true result. The interesting claim would be "depth filtering improves over unfiltered," which is not supported. The Discussion overstates this ("depth estimation enables a finer-grained alternative") when the PoC shows it enables... approximately the same outcome with less data.

6. **EDD=4 claim requires stronger qualification in the abstract.** The abstract states "EDD_{0.75}=4" as if this is a general finding. In reality: Pythia p=0.001 (significant), OLMo p=0.091 (marginal), GPT-2 XL p=0.505 (non-significant). Only 1/3 models achieves statistical significance at the 0.75 threshold for the d3-d4 pair. The body text handles this well ("graded confidence rather than uniform statistical significance") but the abstract presents it without qualification. A reader who sees only the abstract gets a misleading impression.

7. **Reference model creates an implicit information leak.** All features are computed via GPT-2 base (124M). When GPT-2 XL generates the text, architectural overlap exists (shared tokenizer, partial weight inheritance from pretraining). The paper notes GPT-2 XL holdout (67.6%) doesn't exceed OLMo (69.2%), but this doesn't rule out more subtle effects—the reference model may be more "surprised" by Pythia/OLMo outputs in a way that artificially inflates d0/d1 separation for those models. A sensitivity analysis with a completely independent reference model (e.g., Llama-2-7B) would strengthen the claim.

8. **Feature collinearity inflates complexity.** VIF>10 for 14-16 of 19 features, effective dimensionality ~4-5. The paper acknowledges this but continues to frame the contribution as "19 candidate features" throughout. In reality, ~4 independent features are doing the work. The feature table (Table 1) and the presentation should foreground the effective dimensionality rather than the raw count, which creates a misleading impression of design complexity.

### Minor

9. **Zero-shot LLM baselines are under-explored.** n=500 with zero-shot prompting is a weak baseline. No chain-of-thought, no few-shot examples, no feature descriptions in the prompt. DeepSeek V3.2 and Qwen2.5-7B are not state-of-the-art reasoning models. A GPT-4/Claude baseline with 5-shot examples would be a more convincing comparison. The current baseline feels designed to fail.

10. **No instruction-tuned generators tested.** All three models are base models. Instruction-tuned models (Llama-3-8B-Instruct, Mistral-7B-Instruct) dominate real-world generation. Recursive contamination from chat completions may produce different statistical signatures than from base model sampling.

11. **Fixed passage length (512 tokens) is unrealistic.** Real web text varies wildly in length. How sensitive are tail statistics to passage length? At 128 tokens, p90_ppl is computed over ~128 values—the tail estimate becomes noisy. No sensitivity analysis is provided.

12. **The Discussion section is overstuffed.** Mixed-depth documents, adversarial robustness, scaling predictions, provenance toolkit—each gets 1-2 paragraphs of pure speculation. This reads like a "future work laundry list" rather than focused discussion of what the results actually mean. Consider cutting or moving to appendix.

13. **Writing: "Depth Degradation Atlas" framing.** The Atlas is essentially a set of tables and feature importance rankings across 9 experimental conditions. Calling it an "Atlas" creates expectations of richer cartographic metaphors (geographic visualization, navigable maps). The contribution is solid but the branding slightly oversells it.

14. **Decision boundary dilution paragraph.** The observation that binary pair classifiers outperform multi-class classifiers on per-pair AUC is well-known in the ordinal classification literature. Presenting this as a finding rather than a methodological choice slightly misrepresents its novelty.

## Questions for Authors

1. What happens when the reference model IS the same family as the generator (i.e., computing features with Pythia-1.4B on Pythia-1.4B-generated text)? Does self-referential feature computation inflate or deflate performance?

2. The memorization prerequisite finding suggests depth signal requires tau < 1.0. What fraction of real-world API deployments use temperature > 1? If most real generation uses tau in [0.7, 1.0], how does this constrain practical applicability?

3. Could the feature universality across 3 models simply reflect that all share similar parameter count (1-1.5B) and similar pretraining scale? Would you expect the same feature ranking for a 70B model where perplexity distributions are fundamentally narrower?

4. The d2 trough in recall (46-73%) is attributed to feature overlap. But alternatively, is d2 genuinely less distinct because the distributional shift between d1→d2 is smaller than d0→d1 or d2→d3? Can you provide KL divergence between adjacent depth feature distributions to verify?

5. For the curation PoC, why does oracle-strict filtering not improve over unfiltered (p=0.22)? This seems to suggest that removing depth-3 data is actually harmful—contradicting the premise that deep recursive text degrades training. How do you reconcile this?

6. The LOGO analysis uses 10 seed groups. With only 10 folds, statistical power to detect a seed-group effect is limited. Why not 50 or 100 groups?

## Suggested Experiments (prioritized by impact)

1. **One 7B model (e.g., Llama-2-7B or Mistral-7B)**, even with reduced depth chain (d0-d2), to validate whether perplexity tail features retain discriminability at larger scale. This is the single experiment that would most strengthen the universality claim.

2. **Passage length sensitivity analysis**: repeat classification at 128, 256, 512, 1024 tokens to characterize the minimum statistical power needed for reliable depth estimation.

3. **Alternative reference model**: repeat the full pipeline with a non-GPT-2 reference model (e.g., Llama-2-7B) to demonstrate reference-model independence.

4. **Strategy identification experiment**: since the two-stage pipeline is proposed as the deployment solution, demonstrate that decoding strategy can actually be identified from text features alone (even a simple binary nucleus-vs-temperature classifier would help).

5. **Realistic contamination simulation**: mix d0 and d1 text at known proportions (e.g., 90% d0 / 10% d1), then test whether the classifier can identify the contaminated fraction. This would bridge the controlled→ecological gap without requiring full pretraining.

6. **Few-shot LLM baseline**: GPT-4 or Claude with 5-shot examples and chain-of-thought to establish a tighter upper bound on what instruction-following models can achieve.
