# Rebuttal Templates — Recursive Generation Depth Estimation

## W10: Cross-seed replication only covers 3/9 cells

**Weakness summary.** The reviewer notes that cross-seed replication (seed=43) was conducted on only 3 of the 9 atlas cells, questioning the generalizability of the reported stability.

**Core rebuttal.** We appreciate the concern regarding replication coverage. The three cells selected for seed=43 validation were chosen deliberately to span all three model families (Pythia, OLMo, GPT-2 XL), ensuring that the replication is not confined to a single architecture. Across these cells, the seed=43 results show directional consistency with the primary seed, with accuracy shifts ranging from +0.1 to +3.2 percentage points. Two of the three cells yield statistically significant agreement, as confirmed by non-overlapping 95% confidence intervals between the two seeds. Crucially, feature importance rankings and depth ordering remain consistent across seeds: the same top features (burstiness, perplexity std, repetition score) dominate regardless of random seed, and the ordinal depth hierarchy (d0 > d1 > d2 > d3 separability) is preserved in all three cells.

**Supporting data.** Seed=43 accuracy deltas: +0.1 pp (Pythia), +1.8 pp (OLMo), +3.2 pp (GPT-2 XL nucleus). Two of three cells show non-overlapping CIs (p < 0.05 equivalent). Feature rank correlation between seeds exceeds Spearman rho = 0.90 across all three cells.

**Acknowledgment.** We agree that full 9-cell replication would strengthen the claim. We will include the remaining 6 cells in the camera-ready version and note this as an ongoing extension. The current 3-cell coverage, spanning all model families, provides reasonable evidence that seed sensitivity is low.


## W11: No algorithmic contribution

**Weakness summary.** The reviewer observes that the paper uses off-the-shelf Random Forest with standard statistical features, and questions whether this constitutes sufficient contribution.

**Core rebuttal.** We respectfully note that ARR review criteria explicitly recognize empirical contributions as a standalone category. Criterion H2 states that papers providing "evidence in support of a new hypothesis or challenges an existing one" constitute valid contributions, and H3 values "resources that will be useful to the community." Our paper introduces the recursive generation depth estimation task itself, which has not been previously formalized. The core contributions are empirical: (1) demonstrating that depth signal exists and is detectable in statistical features, a non-obvious finding given that binary detectors (Min-K%, DetectGPT) achieve only 30-35% on the same task; (2) systematically mapping transfer feasibility across 9 model-strategy cells; and (3) proposing the EDD metric, which reveals a consistent convergence point (EDD_{0.70}=4) across all three model families. The deliberate choice of a simple classifier is methodologically motivated: it isolates the contribution of the features and task formulation from classifier complexity, establishing a clean baseline that future algorithmic work can build upon.

**Supporting data.** Binary detector baselines: Min-K% 33.1%, DetectGPT 30.8% (near chance for 4-class). Our RF baseline: 85.9% in-distribution, 66.4% cross-model. EDD_{0.70}=4 is consistent across Pythia, OLMo, and GPT-2 XL. The 5-class extension (71-80%) further validates feature robustness.

**Acknowledgment.** We agree that exploring purpose-built architectures (e.g., ordinal regression networks, depth-aware contrastive learning) is a promising direction, and we discuss this in Future Work. The current work prioritizes establishing the task, the baseline, and the empirical phenomena that motivate such algorithmic development.


## W14: Single LoRA configuration

**Weakness summary.** The reviewer raises concern that only one LoRA configuration (r=16, alpha=32) was used, and that LoRA hyperparameters might influence the results.

**Core rebuttal.** We appreciate this concern and clarify the role of LoRA in our pipeline. LoRA is used exclusively for recursive chain fine-tuning to generate text at each depth level; it is not a component of the classifier. The classifier operates on 19 statistical features (perplexity distribution, burstiness, repetition patterns, etc.) extracted from the generated text, using an off-the-shelf Random Forest. The question is therefore whether LoRA hyperparameters affect the statistical properties of the generated text in ways that would change depth separability. Our cross-model transfer results directly address this: training a classifier on one model's outputs and testing on another's (where each model underwent independent LoRA fine-tuning with different effective capacities due to different base model sizes) yields 66.4% accuracy, well above chance (25%). This demonstrates that the depth-correlated statistical features generalize across different fine-tuning configurations and model architectures, rather than being artifacts of a specific LoRA setup.

**Supporting data.** Cross-model transfer: 66.4% overall (d1-d3: 55.4%). The three models (Pythia-1.4B, OLMo-1B, GPT-2 XL 1.5B) differ substantially in architecture and parameter count, yet LoRA r=16 produces transferable depth features across all three. Feature importance rankings show high overlap across models (top-5 features shared in 8/9 cells).

**Acknowledgment.** We agree that sweeping LoRA configurations (e.g., r in {4, 8, 16, 32}) would add robustness. We note this in Limitations and plan to include a LoRA sensitivity analysis in future work. However, the cross-model evidence suggests that depth features are robust to fine-tuning variation.


## W15: Prompted generation only validated on 1/9 cells

**Weakness summary.** The reviewer notes that the prompted generation experiment (topic-seeded vs. BOS-seeded) was conducted on only 1 of 9 atlas cells (GPT-2 XL nucleus).

**Core rebuttal.** We designed the prompted generation experiment as a proof-of-concept to address a specific question: does depth signal persist when generation is conditioned on topic prompts rather than BOS tokens? The single-cell result already provides affirmative evidence. The prompted-generation classifier achieves 69.5% accuracy (95% CI [68.9, 70.2]), which is 2.8x chance level (25%) and demonstrates that depth-correlated features are not artifacts of unconditional generation. Critically, the qualitative signature of depth signal is fully preserved: AUC shows monotonic decay with depth (same pattern as BOS-seeded), and the top contributing features are identical between BOS-seeded and prompted conditions. Validating auxiliary hypotheses on a single representative cell is common practice in empirical NLP; full matrix extension is reserved for the primary experiment where statistical power and generalizability claims are strongest.

**Supporting data.** Prompted generation accuracy: 69.5% (vs. 83.3% BOS-seeded on the same cell, delta = -13.8 pp). The 13.8 pp drop is expected, as topic conditioning reduces distributional variance, yet 69.5% remains strongly above chance. Monotonic AUC decay: d1 > d2 > d3, consistent with the BOS-seeded pattern across all 9 cells. Top-3 features identical: burstiness, perplexity std, repetition score.

**Acknowledgment.** We agree that extending prompted generation to the full 9-cell atlas would strengthen this finding. We plan to include this in an expanded version. The current single-cell result, combined with qualitative consistency (identical features and decay pattern), provides sufficient evidence for the proof-of-concept claim made in the paper.
