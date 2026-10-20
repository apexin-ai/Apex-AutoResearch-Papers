---
dream_id: dream_20260516T092241
tier: best
overall_score: 3.0 — Findings-level; borderline reject for Main Conference
timestamp: 2026-05-16T10:16:11.298691+00:00
---

# DREAM Review Report

**Paper**: Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction
**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-16

## Paper Summary

This paper investigates whether confidence signals from multiple sampled outputs can improve structured information extraction (NER, RE) beyond greedy decoding—an application of self-consistency/best-of-N to structured tasks. Five confidence signals are evaluated across three families: structural agreement (Sample-level Jaccard, Full-set Kappa), probabilistic (logprob), exact-match voting, and voting confidence. The core finding is negative: while signals reliably predict output quality at the population level (AUROC up to 0.82, Spearman rho up to 0.45), they universally fail to select better candidates than T=0 greedy decoding.

The paper diagnoses two failure mechanisms: (1) instance degeneracy, where 21-58% of instances produce identical outputs across all N=8 samples, eliminating selection headroom entirely; and (2) logprob compression, where the only per-sample signal (LP) exhibits within-instance range of only 0.028-0.041 nats, insufficient for reliable ranking. These mechanisms are unified under a "capability trap" narrative: higher model capability leads to output convergence, which causes degeneracy, which eliminates selection headroom.

Validation includes scale ablation (Qwen3-8B vs 4B), LoRA rank ablation (16 vs 8), cross-architecture (LLaMA vs Qwen), free-form decoding ablation, and three-seed replication across SciERC, CoNLL-2003, and Few-NERD. The paper positions itself as a diagnostic contribution rather than a methods paper.

## Roundtable Discussion

### Points of Agreement

- Both reviewers agree that R^2=0.94 with n=3 data points is statistically vacuous and should not anchor the capability trap narrative. This is the single most critical methodological weakness.
- Both agree the statistical methodology is rigorous (bootstrap, Fisher combined p, Cohen's d, confidence intervals).
- Both agree the QE results (AUROC 0.82) and non-tied subset findings (+2.9pp, p=0.01) are genuinely useful contributions that the paper underemphasizes.
- Both agree the paper only tests fine-tuned models, which are known to reduce output diversity, limiting the generality of the "inevitability" claim.
- Both find the ablation chain well-structured and progressive.
- Both assign Soundness 3.5 and Reproducibility 4.
- Both note that the paper's framing as purely negative may undercut its own positive contributions.

### Points of Divergence and Resolution

**1. Effective signal dimensionality (R1 Weakness 3 vs R2's implicit acceptance)**

R1 argues that 4/5 signals collapse to constants under degeneracy, meaning the paper effectively tests ONE selection signal (LP) and presents failure as "universal." R2 does not raise this directly but notes the "moderate novelty" of individual findings being well-known.

*Resolution*: R1's point is technically correct but somewhat overstated. The paper does acknowledge that instance-level signals cannot rank by construction (Layer A). The contribution is showing that even LP—the only signal that CAN vary per-sample—also fails due to compression. The paper should be clearer that the "universality" claim has two distinct parts: (a) instance-level signals fail by design, (b) LP fails empirically due to compression. This is still a valid contribution but should not be presented as if five independent signals were all tested and all failed independently.

**2. Novelty assessment (R1: 3.0 excitement vs R2: 2.5 excitement)**

R1 finds the experimental rigor and diagnostic framing moderately exciting. R2 argues the core finding is essentially ecological fallacy / Simpson's paradox applied to ranking, reducing novelty.

*Resolution*: R2's framing is more precise. The correlation-selection gap IS a known statistical phenomenon (population-level correlation does not imply within-instance discrimination). The paper's novelty lies in (a) documenting this specifically for structured IE with five signals, (b) quantifying the two mechanisms, and (c) the free-form ablation ruling out format constraints. This is a solid empirical contribution but not conceptually novel. Consensus: Excitement 2.5-3.0.

**3. Missing literature scope (R2 Weakness 3)**

R2 identifies significant gaps: diversity-promoting decoding, BoN with reward models (Gao et al. 2023), RLHF diversity collapse, structured prediction calibration. R1 does not raise this.

*Resolution*: R2 is correct. The paper must engage with BoN/reward model literature (Gao et al. 2023) since best-of-N with learned verifiers is the natural next step after showing unsupervised signals fail. The diversity collapse literature (Kirk et al. 2024) directly supports the capability trap but is uncited. This is a significant omission for a Main Conference submission.

**4. Paper framing: negative vs constructive (R2 Weakness 4)**

R2 argues the paper undersells its positive findings. R1 implicitly agrees by noting the non-tied subset results are interesting.

*Resolution*: Both are correct. The paper should reframe: signals ARE useful for QE/selective prediction (knowing WHEN extraction failed) even though they cannot improve HOW extraction is done. The non-tied subset result (+2.9pp) and the QE AUROC (0.82) have practical value that the relentless negative framing obscures.

**5. "Capability trap" vs "ceiling effect" (R2 Question)**

R2 asks how the authors distinguish their "capability trap" from a simple ceiling effect. R1's concern about n=3 for R^2 relates to the same issue.

*Resolution*: This is a legitimate concern. On CoNLL (91% F1, 58% degeneracy), the model is near ceiling—degeneracy may simply reflect that there are few plausible alternative outputs. On SciERC (66% F1, 21% degeneracy), there IS substantial room for improvement but the model converges anyway. The SciERC case is more compelling for "trap" vs "ceiling." The paper should explicitly address this distinction and acknowledge that CoNLL may be ceiling-driven while SciERC demonstrates the genuine trap.

## Consolidated Review

### Strengths

1. **Well-designed diagnostic methodology**: The five-layer ablation chain (design property → degeneracy → LP compression → free-form → scale) progressively eliminates alternative explanations. Each ablation is clean and well-motivated.

2. **Rigorous statistical framework**: Bootstrap with 1000 iterations, Fisher combined p-values, Cohen's d effect sizes, confidence intervals, and three-seed replication. This sets a high standard for negative-result papers.

3. **Free-form decoding ablation**: Showing LP compression is unchanged (std ratio 0.97) when format constraints are removed is a genuinely informative controlled experiment that rules out a natural alternative explanation.

4. **QE contribution**: Population-level prediction results (AUROC 0.82, rho 0.45) with signal ranking that reverses between NER and RE (structural > probabilistic for NER, probabilistic > structural for RE due to binary F1 dominance) is a useful practical finding.

5. **Scale ablation design**: The 2x2 matrix (2 datasets x 2 model sizes) with n_samples confound control demonstrates the gap is not specific to one model size.

6. **Practical implications clearly stated**: The paper identifies that 8x inference cost recovers T=1.0 degradation but provides zero marginal gain over T=0 greedy—a clear cost-benefit conclusion.

### Weaknesses

1. **R^2=0.94 on 3 data points is not evidence**: Fitting a line with 2 parameters through 3 points (CoNLL/Few-NERD/SciERC) leaves 1 residual degree of freedom. Any monotone relationship would achieve high R^2. This cannot anchor the "capability trap" narrative and its prominence in the abstract/title-level claims is misleading. The qualitative observation (higher capability → more degeneracy) is valid; the quantification is not.

2. **Effective signal space is 1, not 5**: Under degeneracy, 4/5 signals produce identical values across all samples and cannot discriminate. The paper tests LP as the sole per-sample signal and presents this as "universal failure of five signals." This conflates design-level impossibility (trivially true for instance-level aggregates when samples are identical) with empirical failure (LP compression). The claim structure should be reorganized to separate these clearly.

3. **N=8 only at T=1.0 is insufficient for "structural inevitability"**: The paper claims the failure is fundamental but tests a single (N, T) configuration. N=16 pilot data exists but is not fully reported. T=0.5 or T=1.5 are untested. The boundary conditions of the failure are unmapped.

4. **Fine-tuned models only**: LoRA fine-tuning is known to reduce output diversity. The capability trap claim would be far stronger with even one ICL/few-shot condition showing whether the failure persists without fine-tuning-induced mode collapse. This is the most natural confound for the entire narrative.

5. **Missing critical related work**: BoN with reward models (Gao et al. 2023), RLHF diversity collapse (Kirk et al. 2024), diversity-promoting decoding (Holtzman 2020), and structured prediction calibration (Kuleshov & Liang 2015) are all directly relevant and uncited.

6. **Degeneracy definition conflates output identity with score identity**: "All N samples produce the same F1" counts instances where different outputs happen to achieve the same score. These instances DO have selection opportunity (choosing the output that will generalize better) but are counted as degenerate. The true degeneracy rate (output identity) may be lower.

7. **LoRA rank ablation potentially confounded**: If rank=8 was trained with different hyperparameters (e.g., different epoch count or learning rate) than rank=16, the ablation conflates training recipe with adapter capacity. The paper should confirm identical training protocols.

### Questions for Authors

1. What is the degeneracy rate measured by exact output identity (string match across all N samples) vs. F1 score identity? If substantially different, the headroom analysis changes.

2. What happens at N=16 and N=32? Does degeneracy decrease, and if so, does LP selection improve on the newly non-degenerate instances?

3. Have you measured effective output entropy for your fine-tuned models vs. base models at the same temperature? This would directly quantify the fine-tuning diversity reduction.

4. For the non-degenerate subset, what are within-instance correlations for SJ and VC (not just LP)? If these are high, the "only LP matters for selection" narrative needs revision.

5. Can you test T=0.5 with N=4 as a practical operating point? Industry practitioners may use moderate temperature with fewer samples.

6. How do you respond to the framing that your "capability trap" is simply a ceiling effect on CoNLL, and only genuinely novel for mid-difficulty tasks (SciERC)?

7. What is the 95% CI on R^2 with bootstrap resampling of the 3 data points? (This will likely span [0, 1], confirming it is uninformative.)

8. Have you considered entity-level majority voting (the natural SC analog for sets) as a baseline, connecting to Wang et al. (2023)?

### Minor Issues

- Table 1 reporting for CoNLL is incomplete (missing VC, full LP metrics)
- The term "capability trap" implies inevitability that goes beyond what 3 datasets can support; "capability-degeneracy tradeoff" would be more accurate
- Paper would benefit from a figure showing the degeneracy frontier across (N, T) space, even if only for one dataset
- Abstract should mention the QE positive result alongside the selection negative result
- The free-form parse rate (99.95%) finding about format compliance should be noted but not overclaimed

## Scores

| Dimension | R1 | R2 | Consensus | Justification |
|-----------|----|----|-----------|---------------|
| Soundness | 3.5 | 3.5 | 3.0 | R^2=0.94 on n=3 is a central quantitative claim that is statistically meaningless. Core experimental methodology is sound but key claims exceed evidence. The 4/5 signals collapsing under degeneracy means the "universal" framing overstates what was tested. |
| Excitement | 3.0 | 2.5 | 2.5 | The correlation-selection gap is a known statistical phenomenon (ecological fallacy). Empirical documentation for IE is useful but not conceptually novel. Positive findings (QE, task-dependent signal ranking) are undersold. |
| Overall | 3.5 | 3.0 | 3.0 | Solid empirical work with genuine methodological rigor, but the framing overclaims relative to evidence. Main Conference requires either conceptual novelty or broader empirical coverage—this paper has neither quite enough of either. |
| Reproducibility | 4 | 4 | 4 | Three seeds, bootstrap CIs, clear experimental setup. Would be 4.5 with code release. |
| Confidence | 4 | 4 | 4 | Both reviewers are domain experts with consistent assessments. |

## Recommendation

**Borderline Reject for Main Conference; Revise and resubmit, or consider Findings.**

The paper presents a well-executed empirical investigation with rigorous statistical methodology. The core observation—that population-level confidence correlations do not translate to within-instance selection utility for structured IE—is valid and practically important. The ablation chain is methodologically exemplary for a negative-result paper.

However, three issues prevent a Main Conference recommendation in the current form: (1) The "capability trap" quantification (R^2=0.94, n=3) is statistically vacuous and should not be a central claim. The qualitative observation is fine, but presenting it with a precise R^2 is misleading. (2) The experimental scope is too narrow for the generality of claims—fine-tuned models only, single (N,T) configuration, 3 NER datasets. The "structural inevitability" framing requires at minimum one ICL condition and one (N,T) boundary exploration. (3) The paper undersells its genuine contributions (QE framework, task-dependent signal ranking, free-form ablation) in favor of an overclaimed negative narrative.

For a strong revision: (a) Remove or heavily caveat the R^2=0.94 claim, replacing with the qualitative monotone relationship. (b) Add one ICL/few-shot condition to test whether the capability trap persists without fine-tuning. (c) Test N=16 or T=0.5 to map at least one boundary of the failure regime. (d) Reframe to balance the QE positive contribution with the selection negative result — the paper undersells its genuinely useful findings. (e) Add missing related work (BoN with reward models, diversity collapse in fine-tuned LLMs). (f) Clarify that "universal failure of 5 signals" is really "design-level impossibility for 4 signals + empirical failure for LP." With these changes, this could be a solid Main Conference paper in a future cycle. In its current form, it is appropriate for Findings if the R^2 claim is appropriately caveated and the framing is rebalanced.

## Experiment Coverage Assessment

The paper covers a substantial experimental program relative to the imagined experiments in the review context:

**Covered experiments:**
- Few-NERD smoke test (exp-020): Mentioned as 200-instance pilot study. ✓
- Few-NERD full (exp-021): Fully reported in Tables 1–3 with greedy F1=0.842, degeneracy=45%, selection failure. ✓
- 3rd seed SciERC (exp-022): Fully reported in Tables 5–6 with CI narrowing ~30% and Fisher combined p-values. ✓
- LoRA rank=8 ablation (exp-023): Fully reported in Table 4 with degeneracy delta=2pp. ✓
- Claim audit (exp-024): The paper appears internally consistent; key contradictions from the audit appear resolved. ✓

All 5 imagined experiments are reflected in the paper. Coverage is thorough.

**Gaps relative to the claims made (not in the imagined experiments, but important for the paper's framing):**
- No ICL/few-shot baseline (critical for "capability trap" claim — cannot distinguish fine-tuning artifact from fundamental limitation)
- No N>8 full evaluation (N=16 pilot on 200 instances mentioned but not completed at scale)
- No temperature sweep (only T=1.0 for sampling; the degeneracy frontier across temperature is unmapped)
- No additional RE dataset beyond SciERC (would strengthen RE generality)
- Entity-level majority voting not framed as the direct self-consistency analog for sets
- Output entropy measurement not reported (would directly quantify diversity reduction from fine-tuning)

The experiment-to-claim ratio is the paper's core tension: the claims are framed as universal/structural, but the experimental coverage is limited to a specific (fine-tuned, N=8, T=1.0) operating regime. Expanding to even 2–3 of the gaps above would substantially strengthen the paper.