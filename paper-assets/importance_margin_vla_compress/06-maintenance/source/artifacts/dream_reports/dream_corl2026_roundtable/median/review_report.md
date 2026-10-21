---
dream_id: dream_corl2026_roundtable
tier: median
overall_score: 5.5/10 — Borderline (Weak Reject)
timestamp: 2026-05-25T06:06:39.322365+00:00
---

# Dream Review Report — "Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"

## Venue: CoRL 2026

## Paper Summary
This paper presents the first cross-architecture study of vision token pruning across 6 VLA models spanning 4 connector families (linear, MLP, BART post-processing, pixel-shuffle) evaluated on 4 LIBERO task suites. The core finding is a 2-axis framework: pruning sensitivity is jointly determined by connector architecture (token-independent vs token-entangling, diagnosed via importance CV) and task complexity. A secondary contribution is VTR (Vision Token Re-encoding), a learned compression module for otherwise incompressible pixel-shuffle architectures. The paper identifies a double dissociation where attention-based scoring helps entangling connectors while L2-norm scoring helps independent connectors, and random pruning can massively outperform importance-based pruning on intermediate-CV architectures.

## Consolidated Scores
| Criterion | R1 | R2 | Final | Justification |
|-----------|----|----|-------|---------------|
| Originality | 7 | 5 | 6 | The systematic cross-architecture framing is genuinely novel for VLAs, but the individual techniques (CV, attention scoring, cross-attention re-encoding) are standard. The novelty is in the empirical synthesis and the 2-axis interaction finding, which is valuable but incremental methodologically. Resolved toward the mean: the framework-level novelty exceeds "just running existing methods" (R2's concern) but does not constitute a fundamentally new technique (tempering R1's enthusiasm). |
| Quality | 5 | 7 | 5.5 | R1's concerns about incomplete data matrix, single-seed dominance, and confounded comparisons are substantiated by the project data — OpenVLA experiments are still running as of submission, Long suite data is incomplete, and many experiments failed repeatedly. R2's assessment of "thorough within scope" is generous given the actual gaps. The project log reveals ~86 failed experiments out of 637, and critical crossover table entries (Random k=0.9 for Goal and Spatial) were still being deployed at submission time. The VTR batch size confound (4 vs 512) is a real methodological issue that weakens that contribution. However, the completed data points (SmolVLA cliff, X-VLA full curve, pi0.5 cliff zone) are individually well-validated with dual seeds. Split toward R1: the gaps are real and undermine the "comprehensive" framing. |
| Clarity | 7 | 7 | 7 | Both reviewers agree. The paper is well-structured with honest limitations and appropriate hedging. The 2-axis framework is clearly presented. |
| Significance | 6 | 6 | 6 | Both reviewers agree. Practically useful findings for VLA deployment, but limited to LIBERO simulation. The MetaWorld results (SmolVLA only, very low baseline of 26.4%) and abandoned SimplerEnv attempt further limit demonstrated generalizability. |
| Relevance | 8 | 8 | 8 | Both reviewers agree. Token efficiency for VLA deployment is a timely and important topic for CoRL. |

## Overall Score: 5.5/10 — Borderline (Weak Reject)

## Roundtable Consensus

### Key Agreements
- The paper fills a genuine gap as the first cross-architecture VLA token pruning study; no competing work covers this scope
- The SmolVLA pixel-shuffle cliff (k=0.95 removes 5% of tokens → 0% SR, validated with official checkpoint + dual seed) is the single strongest and most definitive result
- The double dissociation (attention-based scoring helps entangling connectors; L2-norm helps independent connectors; random massively outperforms L2-norm on X-VLA at aggressive compression) is the most novel and actionable finding
- The incomplete data matrix is a genuine problem — not a nitpick but a structural gap that undermines the "comprehensive" framing
- LIBERO-only evaluation limits generalizability, and the SimplerEnv attempt (baseline 0% SR, abandoned) and MetaWorld results (26.4% baseline, too weak to draw conclusions) do not help
- VTR is narrowly validated and architecturally derivative (Q-Former/Perceiver Resampler family)
- CV as a diagnostic is validated on too few data points to support the claimed "continuous spectrum" — 6 CV values is a correlation, not a validated predictor

### Resolved Disagreements

**Originality (R1=7 vs R2=5 → Final=6):**
R1 credited the systematic framework and 2-axis interaction as novel contributions. R2 argued that the individual components (CV computation, attention-based scoring extending FastV, VTR as Q-Former variant) lack methodological novelty. The resolution: the 2-axis interaction finding (connector × task complexity) is genuinely novel and surprising — the X-VLA result where the same model drops 27.8pp going from Object to Goal at identical k=0.9 is not obvious a priori and could not have been predicted from prior work. This exceeds pure replication novelty. However, no new algorithmic contribution survives scrutiny: CV is the coefficient of variation, the scoring methods are existing, and VTR is architecturally Q-Former. CoRL values empirical insights for robotics practice, which tempers R2's concern, but the paper's positioning as "analysis + method" oversells the method contribution. Final: 6, reflecting genuine empirical novelty in the interaction finding but limited methodological novelty.

**Quality (R1=5 vs R2=7 → Final=5.5):**
This disagreement hinges on whether the paper's claims are calibrated to its evidence. R1 identified specific gaps: (1) OpenVLA evaluated on Object suite only in the main table, with Goal/Spatial/Long data still being collected at submission time; (2) most conditions use seed 42 only, with dual-seed validation limited to SmolVLA and pi0.5 cliff zone; (3) the 6 models differ simultaneously in backbone, scale, training data, and connector, with only OFT-OpenVLA providing a controlled comparison; (4) the "scaling law" claim fits 3 data points; (5) the pruning protocol re-indexes positions, confounding token removal with positional disruption. R2 assessed the paper as "thorough within scope" with appropriate statistics. The project data supports R1's assessment more strongly: the ROADMAP shows 4 OpenVLA Long experiments still running, Random Goal/Spatial experiments still being deployed, and the crossover table having active gaps at submission time. The 86 failed experiments out of 637 total suggest the experimental pipeline was fragile. The VTR batch-size confound (batch 4 producing 44.8% baseline vs official 59.2% at batch 512) is a meaningful methodological issue that R2 acknowledged but weighted less. Resolution: split toward R1 at 5.5, because the claims ("first comprehensive study," "continuous spectrum predictor," "scaling law") exceed what the evidence robustly supports, but the completed data points are individually sound.

## Strengths (ranked)
1. **SmolVLA pixel-shuffle cliff is definitive.** k=0.95 → 0% SR validated with official HF checkpoint, dual seeds, multiple pruning methods, and multiple suites. This is a clear, mechanistically interpretable, and practically important finding that no prior work has reported.
2. **Double dissociation in scoring methods is novel and actionable.** The finding that L2-norm pruning is catastrophically worse than random on X-VLA at aggressive compression (42.6% vs 70.6% at k=0.5, gap growing to 40pp at k=0.3) while being consistently better on OpenVLA — and that CV predicts which regime applies — is the paper's most original contribution.
3. **First cross-architecture VLA pruning study.** Despite gaps, covering 5+ models across 4 connector families is more comprehensive than any existing or concurrent work (SP-VLA, LightVLA, Compressor-VLA, EfficientVLA all study 1-2 models).
4. **2-axis interaction is surprising and well-demonstrated.** The X-VLA Object (97.6%) vs Goal (70.2%) result at identical k=0.9 cleanly isolates task complexity as an independent factor, using the same model, method, and keep ratio.
5. **Honest limitations and extensive appendix.** The paper appropriately hedges claims and provides reproducibility detail. The decision to report failed experiments (VTR on OpenVLA = 0%) rather than hiding them is commendable.

## Weaknesses (ranked)
1. **Incomplete data matrix undermines "comprehensive" framing.** OpenVLA crossover table has active gaps (Random Goal/Spatial still being deployed, Long still running at submission). The main results table has "--" entries. A paper claiming to be the first comprehensive cross-architecture study must deliver complete cross-architecture data.
2. **Single-seed dominance limits statistical reliability.** Most conditions use seed 42 only. Dual-seed validation is limited to SmolVLA cliff and pi0.5 cliff zone. The X-VLA full curve (the paper's second-strongest result) is single-seed for most k values. At CoRL acceptance rates (~39%), this is a meaningful gap.
3. **Confounded comparisons across models.** The 6 models differ in backbone (SigLIP vs DINOv2), scale (450M-7B), training data, and connector simultaneously. Only the OFT-OpenVLA pair provides a controlled comparison, and OFT is evaluated offline only (CV/entropy analysis, no LIBERO SR due to Blackwell GPU incompatibility). The paper acknowledges this but the 2-axis framework implicitly claims connector is the causal variable.
4. **VTR contribution is weak and derivative.** Architecturally identical to Q-Former/Perceiver Resampler. Validated on SmolVLA only (where it works) and fails on OpenVLA (0% SR). Trained at batch size 4 vs official 512, producing a weakened baseline (44.8% vs 59.2%). The "Diagnose-then-Compress" framework adds little beyond common sense (diagnose first, then act).
5. **No head-to-head comparison with concurrent VLA pruning methods.** The literature map identifies 6+ concurrent works (SP-VLA, VLA-IAP, LightVLA, EfficientVLA, VLA-Pruner, Compressor-VLA). None are compared experimentally. Given that these methods also prune VLA tokens — some on the same models (OpenVLA) and benchmarks (LIBERO) — this is a significant omission for a paper positioning itself as a comprehensive analysis.

## Detailed Technical Critique

### Methods and Experiments (R1 focus)

**Pruning protocol concern:** The position re-indexing after token removal is a valid confound. When tokens are pruned, the remaining tokens receive new position indices, which could disrupt learned positional relationships independently of the information loss from removing tokens. The fixed-mask experiment (D149) only controls for temporal mask variation, not positional disruption. A proper control would mask tokens to zero while preserving position indices, which the paper does not report.

**"Scaling law" on 3 points:** Fitting a hypergeometric cliff model to 3 data points (SmolVLA, X-VLA, pi0.5) and calling it a scaling law is overclaimed. This is a post-hoc fit, not a validated predictive model. The paper needs at least 6-8 architectures with different CV values to credibly claim a continuous relationship.

**Offline-only evaluation for OFT and pi0:** Counting these as part of "6 architectures" overstates coverage. OFT has zero LIBERO SR data (Blackwell GPU incompatibility prevented evaluation). pi0 has offline loss curves only. The effective LIBERO evaluation covers 4 models (SmolVLA, OpenVLA, X-VLA, pi0.5), not 6.

**Attention-based pruning cost omitted:** The paper proposes attention scores as a pruning criterion but does not discuss the computational overhead of the extra forward pass needed to compute attention maps, versus the "zero-cost" CV diagnostic. For a paper about efficiency, this is a notable omission.

### Novelty and Related Work (R2 focus)

**VTR vs Q-Former/Perceiver Resampler:** The architectural similarity is undeniable — cross-attention from learned queries to visual tokens is exactly the Perceiver Resampler mechanism (Alayrac et al., 2022). The paper should explicitly acknowledge this lineage and articulate what is different (the answer appears to be: nothing architecturally, only the application context of post-hoc compression rather than pre-training).

**Missing related work categories:** The paper does not discuss knowledge distillation approaches for VLA compression, temporal token compression (exploiting frame-to-frame redundancy, which VLA-Cache and VLA-Pruner address), or the broader VLM compression literature beyond token pruning (quantization, layer pruning, which EfficientVLA combines). For a survey-like analysis paper, this narrowness is a limitation.

**"20x amplification" framing:** R2's concern about base-rate sensitivity is valid. The claim that entangling connectors amplify task-complexity effects by 20x depends on the specific baseline success rates and the denominator used. Different normalization choices could yield very different amplification factors.

**CV as diagnostic:** The paper positions CV as a "zero-cost, one forward pass" diagnostic, but it is computed from attention weights, which requires a forward pass with attention output enabled. More importantly, the claim that CV forms a "continuous spectrum" predicting pruning tolerance rests on 6 data points (pi0=0.038, pi0.5=0.055, X-VLA=0.151, OpenVLA=0.215, OFT=0.219, SmolVLA=0.314) with only 4 having corresponding SR data. This is a correlation plot with n=4, not a validated predictor.

## Questions for Authors
1. Can you provide a control experiment where pruned tokens are zeroed out but position indices are preserved, to isolate information loss from positional disruption?
2. What is the computational overhead of attention-based scoring (the extra forward pass) versus L2-norm scoring, and how does this compare to the inference savings from token reduction?
3. Why was VTR trained at batch size 4 when the official SmolVLA training uses batch size 512? What evidence supports that the 14.4pp baseline gap (44.8% vs 59.2%) does not confound the VTR evaluation?
4. The crossover table for OpenVLA has missing entries (Random for Goal and Spatial). Can you complete these before camera-ready, and does the task-dependent pattern (Object/Goal prefer L2norm, Spatial prefers Attention) hold?
5. How many of the 6 "concurrent works" listed in your related work could be evaluated on your experimental setup? Would you consider including at least one head-to-head comparison?
6. Can you justify calling the CV-SR relationship a "scaling law" when it is fit to 3-4 data points? Would you consider softening this claim to "empirical trend"?
7. For the pi0.5 cliff zone: the non-monotonic recovery (k=0.3 better than k=0.85) is striking. Do you have a mechanistic explanation beyond "random sampling preserves spatial coverage at lower k"?

## Improvement Recommendations
1. **Complete the data matrix.** Fill all "--" entries in the main table. At minimum, deliver OpenVLA results on all 4 suites and dual-seed validation for the X-VLA full curve. This alone could move the paper from weak reject to borderline accept.
2. **Add one head-to-head comparison with a concurrent method.** VLA-IAP or SP-VLA on OpenVLA+LIBERO would directly address the "no concurrent comparison" weakness and demonstrate that your analysis framework explains when/why these methods succeed or fail.
3. **Reposition VTR or drop it.** Either acknowledge VTR as a known architecture applied to a new context (honest, loses one "contribution") or validate it on at least 2 more connector types. The current single-model validation with a confounded baseline weakens rather than strengthens the paper.
4. **Soften overclaimed language.** Change "scaling law" to "empirical trend." Change "comprehensive" to "broad." Change "6 architectures" to "4 architectures with LIBERO evaluation, 6 with offline analysis." These calibrations cost nothing and improve credibility.
5. **Add position-preserving ablation.** Zero-mask instead of token removal, even for one model, would address the positional disruption confound.
6. **Add one non-LIBERO benchmark with actual signal.** The abandoned SimplerEnv (0% baseline) and weak MetaWorld (26.4% baseline) do not count. If real-robot evaluation is infeasible, a second simulation benchmark where the models achieve reasonable baseline performance would strengthen generalizability claims.

## Meta-Review Summary
This paper addresses a timely and practically important question — why does token pruning work for some VLAs but catastrophically fail for others? The core finding (a 2-axis interaction between connector architecture and task complexity, diagnosed by importance CV) is genuinely novel and would be valuable to the community. However, the execution has meaningful gaps: an incomplete data matrix with active experiments still running at submission time, single-seed evaluations for key conditions, no head-to-head comparison with concurrent methods, and an overclaimed VTR contribution that is architecturally derivative and narrowly validated. At CoRL's ~39% acceptance rate, the paper falls just below the bar — the analysis contribution is strong but the experimental completeness and methodological rigor are insufficient for a venue that receives substantial VLA submissions. A revision addressing data completeness, concurrent method comparison, and honest repositioning of VTR could make this a solid accept.
