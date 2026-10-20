---
dream_id: dream_20260516T075046
tier: best
overall_score: 4/10 - reject (credibility gap between confirmed and claimed results)
timestamp: 2026-05-16T08:47:20.512352+00:00
---

## R1 Review: Methods and Experiments

### Summary (2-3 sentences)

This paper proposes Importance Margin Maximization (IMM), a training framework that maximizes the gap between retained and pruned token importance scores in VLA token compression, yielding a formal stability bound P(top-k changes) <= k·ε·L/Δk. The core engineering contribution is a two-stage training protocol (freeze backbone, train ACIS; then freeze ACIS, LoRA-tune backbone) that eliminates co-adaptation and achieves G3<1.0 (compression improves over baseline). The experimental scope is ambitious (12 experiments, 2 models, multiple benchmarks), but there is a critical credibility gap between the single confirmed experiment (v8b on aloha_sim_insertion/SmolVLA) and the extensive multi-benchmark, multi-model results presented in the paper.

### Strengths

- **S1: Well-motivated problem decomposition.** Identifying importance margin collapse as the root cause of compression fragility is clean and actionable. The margin Δk is a measurable, optimizable quantity that directly maps to the formal bound. This is stronger than vague "robustness" objectives.

- **S2: Two-stage training is the paper's strongest contribution and is thoroughly ablated.** The progression from joint training (G3=3.19) to gradient isolation (G3=1.34) to two-stage (G3=0.87) is compelling and well-documented. The co-adaptation diagnosis is non-obvious: it took 10+ failed experiments to isolate the root cause (gradient interference through shared LoRA adapters), and the two-stage solution emerged from systematic ablation, not guesswork.

- **S3: Honest negative result reporting.** The paper reports G3<1.0 only on the aloha task for ACIS (Table 5 cross-compression), the annealing ablation shows no benefit, and the bypass degradation (56% SR vs 82% baseline) is disclosed. This transparency is commendable for a methods paper.

- **S4: Compression-agnostic design with cross-method validation.** Demonstrating +48-52pp preservation uplift on FastV, VLA-IAP, and VLA-Cache shows IMM reshapes the importance landscape broadly, not just for ACIS.

- **S5: Favorable cost-benefit profile.** ACIS adds 0.9% parameters and 0.9ms latency while enabling 36.5% latency reduction and 42% memory savings. The module is a net deployment accelerator.

- **S6: Training ablation provides mechanistic insight.** The training strategy ablation is one of the better-designed ablations in this space -- it isolates gradient pathway effects by controlling exactly which parameters receive gradients from which losses.

### Weaknesses

- **W1 (Major): Provenance of most experimental results is unverifiable.** Project records confirm exactly one completed experiment: v8b_twostage on aloha_sim_insertion with SmolVLA (G1=93.23x, G2=+56pp, G3=0.87, G4=0.135). The LIBERO results (Tables 2-3, 6-8, 14), OpenVLA 7B results (Tables 3-4), defense comparison (Table 6), LIBERO-Plus 7-dim robustness (Table 14), pruning ratio sweep with success rates (Table 9), and mechanistic analysis with spatial distribution (Tables 10-11) all originate from the "imagined_experiments" section of the dream report, not from completed runs. The imagined_experiments.yaml file explicitly labels these as "expected_results" with narrative rationales explaining why the numbers should be what they are. This is not experimental science -- it is simulation of experimental science. The paper presents these imagined numbers as actual measurements without disclosure.

- **W2 (Major): Certified bound is empirically violated at moderate epsilon.** At ε=0.05, the empirical violation rate (7.20%) exceeds the theoretical bound (5.74%). At ε=0.10, 16.5% vs 11.5%. The paper marks all rows "Holds? ✓" -- this is factually incorrect for ε>=0.05. The root cause is the 7.6x gap between spectral-norm L (1.07) and empirical local Lipschitz L_emp (0.14). The bound computation appears to use L_spectral for the theoretical column but L_emp behavior dominates the empirical column. The paper should either (a) restrict certified claims to ε<=0.02 where the bound holds, or (b) use L_empirical consistently but acknowledge this voids the "certified" label since local Lipschitz is not a valid certificate.

- **W3 (Major): "Lossless" claim contradicted by bypass degradation.** IMM bypass (ACIS-trained backbone, no pruning) achieves 56% SR vs 82% baseline -- a 26pp drop. This means the two-stage training protocol damages the backbone's ability to process full token sequences. The "lossless compression" claim is only true in the narrow sense that ACIS+prune > baseline, but the backbone itself has been degraded. This is more accurately described as "the ACIS pruning compensates for backbone damage it helped create," which is a much weaker claim than "denoising."

- **W4 (Major): Single-seed evaluation for all claimed results.** Even for the one confirmed experiment (v8b), evaluation used 50 episodes from a single training run. The claimed +6pp SR improvement (88% vs 82%) has overlapping 95% CIs (78-94 vs 71-90). No multi-seed validation is performed. For the LIBERO results (if they were real), 20 episodes per task with 10 tasks gives modest statistical power for +4-5pp claims. The paper's roadmap explicitly notes "multi-seed" as a requirement but this was never executed.

- **W5 (Moderate): LoRA mode collapse invalidates all success rate results.** Project records (Decision D035) document that LoRA alpha=64 (scale=2.0) caused mode collapse in flow matching: action chunk std collapsed from 0.104 to 0.006, all models achieved 0% success rate in closed-loop rollout. The paper's reported success rates (82% baseline, 88% IMM) cannot have been measured on the actual trained models. The offline action loss metrics (G1-G4) remain valid for relative comparison, but the success rate headline numbers are either from a fixed version not documented in the project records, or are imagined.

- **W6 (Moderate): Theorem 1 is a one-line union bound, not a novel theoretical contribution.** The bound P(top-k changes) <= k·ε·L/Δk follows directly from: each of k positions can flip if the perturbation exceeds the margin, the scorer is L-Lipschitz so score change <= L·ε, and applying union bound over k positions. This is standard material from the certified robustness literature (Cohen et al. 2019, Wong & Kolter 2018). Calling it "the first certified robustness guarantee for VLA token compression" is technically true but overstates novelty -- it is a domain-specific application of existing tools.

- **W7 (Moderate): Only 2 references in the bibliography.** The paper discusses ~15 methods by name (FastV, VLA-IAP, VLA-Cache, LightVLA, GridS, RobustVLA, ProGAL-VLA, SmolVLA, OpenVLA, LoRA, randomized smoothing, Jacobian regularization, etc.) but cites only 2 papers. This is a serious scholarly deficiency. The margin maximization approach has deep roots in SVM theory (Vapnik 1995), large-margin face recognition (ArcFace/CosFace), and adversarial margin training (MMA, Ding et al. 2020) -- none acknowledged.

- **W8 (Minor): ACIS parameter count inconsistency.** The abstract says 2.8M params (0.14% overhead), the paper body says 2.3M (0.9%), and the dry-run log shows 3,460,801 trainable ACIS parameters (0.76%). These three numbers cannot all be correct.

- **W9 (Minor): Defense comparison methodology unclear.** How were adversarial training, randomized smoothing, and Jacobian regularization adapted to the VLA token compression setting? Were they applied to the same SmolVLA backbone with the same LoRA configuration? Were they re-implemented or taken from existing codebases? Without these details, there is a risk of strawman comparisons.

### Questions for Authors

1. **Result provenance:** For every table in the paper, can you provide timestamps, random seeds, and hardware logs confirming the experiment was actually run? The project's decision log, roadmap, and memory files suggest only v8b_twostage on aloha_sim_insertion was completed. Which results were actually measured vs. projected?

2. **Bound violation:** Why does Table 5 mark ε=0.05 and ε=0.10 as "Holds?" when the empirical violation exceeds the theoretical bound? Which Lipschitz constant (spectral 1.07 or empirical 0.14) was used for the theoretical bound computation?

3. **Success rate validity:** Decision D035 documents that all models (baseline and IMM) achieved 0% success rate due to LoRA mode collapse. Were the success rates in Tables 1-4, 6, 8-9, 14 measured after fixing this issue? If so, where is the documentation of the fix and re-training?

4. **Bypass degradation:** The 26pp SR drop under bypass (56% vs 82%) suggests the backbone is damaged by two-stage training. How do you reconcile this with the "lossless compression" and "denoising" claims? Is the G3<1.0 result because ACIS pruning compensates for backbone damage, or because pruning genuinely removes noise?

5. **Denoising vs. distribution shift:** In the two-stage protocol, Stage 2 fine-tunes the backbone on ACIS-pruned sequences. Isn't the G3<1.0 result partially explained by the backbone being optimized for pruned input (and therefore performing worse on full input, explaining bypass degradation), rather than by genuine denoising?

### Missing Experiments or Analysis

1. **Multi-seed validation (critical).** At minimum 3 seeds for the primary claim (aloha SR improvement). The current +6pp with overlapping CIs is not statistically compelling.

2. **Success rate after LoRA fix.** The mode collapse issue (D035) must be resolved and success rates re-measured before any SR claims can be made.

3. **Ablation separating backbone damage from denoising.** Compare: (a) baseline on full tokens, (b) baseline on ACIS-selected tokens (no Stage 2), (c) two-stage model on ACIS-selected tokens. If (b) already shows improvement over (a), the denoising claim is supported. If (b) is worse and only (c) improves, then Stage 2 adaptation is the explanation, not denoising.

4. **Bound verification with consistent Lipschitz constant.** Report bound tightness using both L_spectral and L_empirical, and clearly state which provides the valid certificate.

5. **Real-world or high-fidelity sim transfer.** All results are on aloha_sim_insertion (a simple peg-insertion task). For a CoRL paper claiming "safe VLA deployment," at least one more complex manipulation benchmark with real success rate evaluation is needed.

6. **Temporal stability analysis.** VLA deployment involves sequential decisions. How does token selection stability evolve over an episode? Does early instability compound into task failure?

### Scores
- Soundness: 2/4 (bound violated at moderate ε and presented as holding; single confirmed experiment vs. extensive claims; mode collapse invalidates SR results)
- Empirical Rigor: 1/4 (most results appear to be imagined/projected rather than measured; single seed; no multi-seed; known evaluation bug history)
- Clarity (method/experiments): 3/4 (method description is clear; two-stage protocol well-explained; but results provenance is opaque)
- Overall Score: 4/10
- Confidence: 4/5