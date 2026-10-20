# Anticipated Reviewer Response Letter

We thank the reviewers for their careful evaluation. Below we address twelve anticipated questions, referencing specific sections, tables, and figures in the manuscript and appendix.

---

## Q1: Behavioral correlation underpowered (ρ=0.583, p=0.10, n=9)

The sample size **n=9** is determined by the cross-architecture matrix design: 3 architectures × 4 LIBERO suites yields 12 cells, of which 10 are filled (NORA Object and Long-Horizon checkpoints are unavailable; §3.1, Table 1). One cell (NORA Goal) is excluded due to bootstrap CI instability from an exit-layer R² ≈ −0.006 artifact (Table 1, footnote b), leaving **9 usable cells**. Expanding n requires either additional VLA architectures with published LIBERO success rates or additional benchmark suites—both beyond the scope of this initial cross-architecture characterization.

We attempted closed-loop evaluation but achieved **SR=0/3** across tested configurations, consistent with known reproducibility challenges in the VLA community (the OpenVLA authors report substantial variation across hardware setups; Fang et al. (2026) similarly document closed-loop difficulties on LIBERO). This negative result is reported in the Appendix (Extended Discussion, 'Closed-loop evaluation attempt' paragraph).

Regarding statistical interpretation: **|ρ|=0.583 constitutes a large effect size** by conventional criteria (|ρ|>0.5; Cohen 1988). The p=0.10 reflects insufficient statistical power at n=9, not absence of effect. Within-suite comparisons are uniformly positive: on Goal (n=3 architectures), ΔR² and success rate are perfectly rank-correlated (ρ=1.0), and every remaining suite shows the same direction (Appendix, Extended Discussion). The paper explicitly qualifies this as "directionally consistent but underpowered" (§6) and frames it as observational evidence rather than a confirmed causal link.

---

## Q2: Only validated on LIBERO—how does this generalize?

LIBERO (Liu et al. 2023) is the standard evaluation benchmark for VLA fine-tuning studies, used by OpenVLA, TracVLA, NORA, and concurrent work (Fang et al. 2026, Swann et al. 2026). Our evaluation spans **4 task suites** (Goal, Spatial, Object, Long-Horizon) that vary substantially in instruction complexity, object diversity, and planning horizon (§3.1).

The stronger generalization argument comes from **cross-architecture consistency**: exit collapse and counterfactual sensitivity replicate across three distinct backbone families—**Llama-2-7B** (32 layers, MHA), **Phi-3-mini** (32 layers, MHA), and **Qwen2.5-VL-3B** (36 layers, GQA)—spanning 3B to 7B parameters with different pretraining corpora and attention mechanisms. The pattern holds despite qualitatively different reference profiles (§4.5, Appendix, Extended Discussion): TracVLA reference starts with saturated L1 attention (32/32 heads) while NORA reference starts at 13–14/16. That the same exit-collapse pattern emerges from these divergent starting points is stronger evidence of generality than observing it on multiple benchmarks within a single architecture.

We explicitly acknowledge that **flow-matching (π₀) and diffusion-based (Octo) architectures may differ** (§6, Limitations) and list this as a concrete direction for future work. The paper's claims are scoped to causal-decoder VLAs.

---

## Q3: No closed-loop evaluation (SR=0)—what is the significance of representational analysis?

Closed-loop SR=0 is not unique to our work. The VLA community faces well-documented reproducibility challenges: OpenVLA's original release noted sensitivity to hardware and software configurations; Fang et al. (2026) report similar difficulties on LIBERO-CF. Our attempted closed-loop evaluation yielded SR=0/3, which we report transparently rather than omit.

**Representational analysis does not require closed-loop success.** This methodological stance has extensive precedent in NLP interpretability: the probing literature (Belinkov 2022, cited in §2) routinely analyzes internal representations without requiring models to achieve SOTA on downstream tasks. Probing measures what information is *accessible* at each layer, independent of whether the full pipeline successfully executes the task end-to-end. Similarly, RSA and attention profiling characterize geometric organization without assuming perfect behavior.

The **behavioral correlation (ρ=0.583)** uses *published* success rates from the original papers (Kim et al. 2024; Zheng et al. 2024; Hung et al. 2025), not our own closed-loop evaluations. This leverages community-validated numbers while our contribution focuses on the representational analysis itself.

Practically, **ΔR² as a diagnostic metric** has value precisely because it does not require closed-loop evaluation: it can assess whether a VLA checkpoint exhibits healthy representational structure (ΔR² < 0.10 indicates preserved exit structure) without expensive rollout infrastructure (§6, Practical Implications). This makes it a complementary tool to behavioral evaluation, not a substitute.

---

## Q4: "First cross-architecture decomposition"—basis for this claim? Distinction from Kachaev et al.?

The claim (§4.6, line 176: "a first cross-architecture decomposition of VLA instruction routing") is grounded in systematic literature comparison. All prior representational analyses of VLAs target a single architecture:

- **Grant et al. (2026)**: visual dominance in a single VLA
- **Haon et al. (2025)**: sparse semantic directions in OpenVLA only
- **Swann et al. (2026)**: interpretable features, large-scale behavioral but single-architecture representational probing per model
- **Buurmeijer et al. (2026)**: low-level motor feature probing in OpenVLA only

**Mitra et al. (2025)** identify task-specific attention heads for fine-tuning efficiency; our analysis focuses on whether such patterns are training-induced or inherited from the pretrained backbone—a question their single-architecture design cannot address.

**Kachaev et al. (2025)** study *visual representation collapse* during VLA fine-tuning—a distinct phenomenon from instruction routing. Their analysis is conducted exclusively on OpenVLA. Our work quantifies a complementary phenomenon (layer-wise action-probe decodability via ΔR²) and critically, **distinguishes training-associated from inherited effects** across three architectures (§2, Concurrent Work paragraph; §4.6). This decomposition—showing that exit collapse is training-associated while L1 attention is inherited—requires cross-architecture comparison by design and is absent from all prior single-architecture studies.

The **3×4 matrix** (3 architectures × 4 suites, 10 filled cells; Table 1) with systematic trained/reference comparisons at each cell is structurally unprecedented in the VLA interpretability literature. The claim is hedged with "with this caveat" referring to the probe-vs-causal-reliance distinction stated in the same sentence.

---

## Q5: NLP controls only use chat fine-tuning—wouldn't a more task-specific NLP control be needed?

Chat fine-tuning is the **maximally relevant control** for our hypothesis. The question being tested is: "Is exit collapse a generic artifact of instruction-following fine-tuning, or is it specific to action-oriented (VLA) training?" Chat-finetuned models share the critical property of being **instruction-following systems fine-tuned on the same backbone**, but lack action heads, robot demonstration data, and vision-action grounding. If exit collapse were a generic consequence of fine-tuning a pretrained LM to follow instructions, chat models should exhibit it.

Three backbone families were tested (§4.3, Table in Appendix, NLP Finetuning Controls):
- **Llama-2-7b-chat** (OpenVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.001
- **Phi-3-mini-4k-instruct** (TracVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000
- **Qwen2.5-3B-Instruct** (NORA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000

All three produce **perfectly flat R² profiles** (ΔR² = 0.000), contrasting with VLM-to-VLA collapse (ΔR² = 0.156–0.455). A more task-specific NLP control (e.g., code generation, summarization) would be *further* from VLA fine-tuning in training objective—making it a *weaker* control. Chat instruction-tuning is the closest NLP analog to VLA instruction-following; its complete failure to produce exit collapse provides the strongest evidence that the phenomenon is specific to action-grounded training. We note in §6 (Limitations) that NLP controls cover all three backbone families, though the analysis operates at the representation level rather than requiring matched data distributions.

---

## Q6: Why use effect size thresholds rather than significance testing?

With **N=63,228 observations** per cell, traditional null-hypothesis significance testing becomes uninformative: virtually every comparison reaches p < 0.001 regardless of practical magnitude. This is a well-known limitation of p-values in large-sample settings (Wasserstein & Lazar 2016, ASA Statement on Statistical Significance).

Our **ΔR² > 0.10 threshold** has dual justification (§3.3, Appendix, Threshold Robustness and Permutation Test):
1. **Semantic meaning**: 10% absolute change in explained variance represents a substantive shift in action decodability
2. **Robustness**: the threshold is not boundary-sensitive—any value in **(0.097, 0.156)** produces identical grouping (Appendix Table 6). The gap between the largest non-collapse value (0.097, TracVLA Long reference) and smallest collapse value (0.156, TracVLA Spatial trained) spans 0.059, providing a clean separation zone

Statistical validation accompanies the effect-size framework:
- **Permutation test**: randomly reassigning 9 cells to two groups (10,000 permutations) yields **p=0.008** for the observed min-max gap (Appendix, Threshold Robustness and Permutation Test)
- **Bootstrap CIs**: Monte Carlo cross-validation (n=1,000 iterations) with demo-level splitting; VLM-to-VLA CIs lie entirely above zero (lower bounds ≥ 0.09; Table 1)
- **Cohen's d** for counterfactual sensitivity (medium-to-large: d=0.45–1.52; §4.4, Table 2)
- **Bonferroni correction**: 63 tests total, 48/63 (76%) pass family-wise correction; all 8 core tests survive at α_adj = 7.94×10⁻⁴ (Appendix, Bonferroni Correction)

This approach aligns with modern statistical best practice: report effect sizes with confidence intervals as primary evidence, use significance tests as supplementary confirmation, and validate threshold robustness via sensitivity analysis.

---

## Q7: N=2 VLM→VLA transitions—how does this generalize beyond two models?

The N=2 VLM→VLA transitions (TracVLA and NORA) may appear small, but the evidential weight of these two transitions exceeds what raw count suggests for three reasons.

**Structural diversity between the two transitions.** TracVLA and NORA differ on nearly every design axis: backbone family (Phi-3-mini vs. Qwen2.5-VL), parameter count (3.8B vs. 3B), attention mechanism (MHA vs. GQA), pretraining corpus (Microsoft vs. Alibaba), and vision encoder integration strategy. Observing identical exit-collapse patterns (ΔR² = 0.156–0.455) across such structurally divergent models provides stronger evidence of generality than N=5 repetitions within a single architecture family, where shared inductive biases could explain the consistency.

**Total evidence includes the negative control.** OpenVLA contributes 4 VLA→VLA cells where ΔR² remains below 0.10 (0/4 cells exhibit collapse). Combined with the 6 VLM→VLA cells showing collapse, the design provides **10 independently-tested cells** with a clean binary separation—collapse occurs if and only if the transition is VLM→VLA.

**Within-architecture suites are not pseudo-replicates.** The four LIBERO suites vary substantially in instruction complexity, planning horizon, and object diversity (§3.1). Critically, the exit-collapse pattern replicates across both independent architecture transitions with no exceptions (6/6 VLM→VLA cells exhibit collapse). Three NLP controls add three additional independent negative observations (0/3 show collapse). The combined evidence—2 positive transitions + 1 negative transition + 3 NLP negatives—is stronger than the raw cell count suggests, because each independent transition type provides a qualitatively different test of the hypothesis.

**Precedent in mechanistic interpretability.** Many high-impact studies in NLP mechanistic interpretability establish general claims from 2–3 models: induction heads (Olsson et al. 2022) use 2 model sizes; the IOI circuit (Wang et al. 2023) is demonstrated in GPT-2 only; superposition (Elhage et al. 2022) uses toy models plus one transformer. Our cross-architecture design with controlled comparisons at each cell exceeds the standard in this subfield.

The paper explicitly scopes this limitation: "N=2 VLM-to-VLA transitions is insufficient for strong causal claims" (§6). We frame our contribution as the first characterization that motivates targeted follow-up, not as a definitive universal law.

---

## Q8: Probing measures decodability, not causal reliance—how do you know the model actually uses this information?

The paper acknowledges this limitation directly in §4.6 (Synthesis): "These probes measure decodability, not causal reliance." We consider this distinction important to state but insufficient to dismiss the findings, for several reasons.

**Characterization precedes causal intervention.** Even without causal proof, establishing *where* information resides and *how* training reorganizes it is a necessary first step toward understanding. The analogy to neuroscience is instructive: fMRI cannot establish causal necessity, yet functional imaging has been foundational for building models of brain organization that subsequently guided causal interventions (TMS, lesion studies). Our probing results serve the same cartographic function for VLA internals.

**Complementary behavioral evidence.** The counterfactual perturbation analysis (§4.4) provides direct behavioral evidence that instruction content *does* influence action outputs: swapping instructions between task suites produces medium-to-large action divergence (Cohen's d = 0.45–1.52, Table 2). This does not prove that the specific layers identified by probing are causally necessary, but it establishes that instruction information is functionally utilized somewhere in the pipeline.

**Intervention evidence from dose-response ablation.** The attention head ablation (Appendix, Extended Discussion) provides intervention-level evidence: progressively removing instruction-dominant L1 heads produces monotonic increases in action divergence (d = 0.48–0.64), confirming that the attention structures we identify carry functionally relevant signals.

**Convergent triangulation.** Three methodologically distinct approaches point to the same conclusion: probing identifies *where* instruction information concentrates, perturbation confirms *whether* instruction content affects behavior, and ablation demonstrates *contribution* of identified structures. No single method is sufficient alone, but their convergence substantially strengthens the overall picture.

---

## Q9: Why not analyze training dynamics (multiple checkpoints)?

The paper explicitly identifies this as a limitation in §6 (Discussion): "tracing collapse onset remains for future work." The absence of training dynamics is a deliberate scope choice driven by practical constraints, not an oversight.

**Checkpoint availability.** Our cross-architecture design relies on community-released final checkpoints (OpenVLA, TracVLA, NORA). None of these projects have published intermediate training checkpoints. Conducting training-dynamics analysis would require either (a) retraining these models from scratch with checkpoint saving—a substantial compute investment (~500+ GPU-hours per architecture) that transforms the project from an analytical study into a training study—or (b) waiting for the community to release such checkpoints.

**Complementary research questions.** Our paper answers "what exists at the end of training" rather than "how it develops during training." Both questions are scientifically valuable, but they require fundamentally different experimental designs. A cross-architecture endpoint study (ours) reveals what is *common* across diverse training procedures; a training-dynamics study reveals *when* and *how* a phenomenon emerges within a single procedure. These are complementary, not substitutable.

**Partial dynamics insight from the existing design.** Although we lack temporal resolution within a single training run, the VLM→VLA vs. VLA→VLA comparison provides coarse-grained dynamics information: exit collapse emerges during the first VLM→VLA fine-tuning transition and does not intensify during subsequent VLA→VLA fine-tuning (OpenVLA cells: all ΔR² < 0.10). This constrains when collapse occurs (early in action-grounded training) even without intermediate checkpoints.

**Our contribution is the first anatomical characterization.** Before studying dynamics, one must first establish *what* to track. Our ΔR² metric and the exit-collapse phenomenon provide a concrete, quantifiable target for future training-dynamics studies. We view this as laying the foundation rather than leaving a gap.

---

## Q10: "Adding a new modality obviously changes representations—isn't this trivial?"

The trivial prediction would be "representations change after fine-tuning." Our findings go substantially beyond this baseline expectation in three ways that no general prediction entails:

**Specific layerwise pattern, not uniform restructuring.** Exit collapse is not a diffuse change across all layers. Action-probe decodability follows a characteristic profile: it rises to a mid-layer peak, then drops sharply at the exit layer (ΔR² = 0.16–0.46). A generic "representations change" prediction does not specify *where* in the network information concentrates or why decodability *decreases* at the exit rather than increasing monotonically toward the output. The non-monotonic profile is a specific empirical finding that requires explanation.

**Convergent mid-layer peaks across diverse architectures.** Two structurally diverse VLM→VLA transitions—TracVLA (Phi-3-mini, 3.8B, MHA) and NORA (Qwen2.5-VL, 3B, GQA)—converge to nearly identical mid-layer peak decodability (R² = 0.637 vs. 0.634; Appendix, Cross-Architecture R²) despite different backbone families, pretraining corpora, and attention mechanisms. This convergence is not predicted by the trivial account. If modality addition simply "changes things," there is no reason to expect quantitative convergence from qualitatively different starting points.

**L1 attention is inherited unchanged despite training.** If the trivial prediction were "training reshapes everything," L1 instruction-dominant attention should increase after VLA fine-tuning. Instead, it is already saturated or near-saturated in pretrained reference VLMs and remains unchanged or slightly reduced after training (§4.5). The decomposition into training-associated effects (exit collapse, counterfactual sensitivity) vs. inherited properties (L1 attention) is a structural finding that the trivial account does not accommodate.

---

## Q11: Venue Fit—Why CoRL?

The CoRL Call for Papers explicitly welcomes "understanding of robot learning," listing "representation learning for robotics" and "foundation models for robotics" as topic areas. Our work provides the first cross-architecture representational analysis of VLA fine-tuning, yielding both mechanistic understanding and practical diagnostics.

**Venue precedent.** Recent CoRL publications establish analytical contributions as an accepted format: Grant et al. (2026) analyze VLA representational structure, Haon et al. (2025) study knowledge transfer through representational analysis, and Mitra et al. (2025) investigate vision override failures via systematic probing—none propose new architectures.

**Scientific validation of the metric.** These precedent papers each pair analysis with operational contributions—behavioral evaluation, steering, or efficient fine-tuning. Our investment is complementary: before ΔR² can serve any practical workflow, it must be established as measuring genuine structure rather than artifact. NLP controls (ΔR²=0.000, 3/3 backbone families) rule out fine-tuning artifact; cross-architecture replication (6/6 VLM→VLA cells across two structurally diverse transitions) rules out architecture-specific confound. This scientific grounding—absent from single-architecture studies—is the prerequisite for credible downstream deployment.

**Actionable diagnostics.** ΔR² provides a checkpoint-selection criterion that does not require expensive closed-loop rollout—a significant practical benefit given documented rollout sensitivity (§6). The flat VLA→VLA profile empirically justifies staged training pipelines. Mid-layer probes outperforming exit-layer probes where collapse is pronounced identifies intermediate representations as more informative targets for distillation or auxiliary loss design. The training-vs-inherited decomposition directly informs design decisions: exit collapse and counterfactual sensitivity are training-associated (tunable via learning rate, data composition, fine-tuning strategy), while L1 instruction attention is inherited (determined by backbone selection).

---

## Q12: Transition-Type vs Training Amount

The VLM→VLA vs VLA→VLA comparison inherently confounds transition type with prior action training amount—a limitation we acknowledge in §3.1.

Three lines of evidence argue against training amount as the explanation. First, the **NLP controls**: chat-finetuned models undergo substantial additional training on their respective backbones yet show ΔR²=0.000 across all three families, demonstrating that extended fine-tuning alone does not produce exit collapse. Second, **OpenVLA's VLA→VLA cells**: these models receive *additional* action training on top of OXE pretraining, yet ΔR² remains below 0.10 (0/4 cells show collapse)—if cumulative training drove collapse, these doubly-trained models should show the largest effect, not the smallest. Third, the **qualitative pattern**: exit collapse is a specific layerwise profile (mid-peak + exit drop), not a generic magnitude increase. Training amount would predict monotonic intensification; instead we observe a structurally distinct phenomenon that appears only when a vision-language model first encounters action-grounded training.

A definitive disentanglement would require training matched VLM→VLA and VLA→VLA models for identical durations on identical data—an experiment we identify as valuable future work (§6).

---

## Summary of Preemptive Measures Already in the Paper

The manuscript includes the following preemptive defenses against anticipated concerns:

- **Demo-level splitting** (§3.3): eliminates within-trajectory leakage; reduces R² from 0.7–0.9 to 0.4–0.6, quantifying pseudo-replication inflation
- **Threshold robustness analysis** (§3.3, Appendix, Threshold Robustness and Permutation Test): any threshold in (0.097, 0.156) yields identical grouping
- **Permutation test** (Appendix, Threshold Robustness and Permutation Test): p=0.008 for VLA-to-VLA vs. VLM-to-VLA separation
- **Three NLP controls** (§4.3, Appendix, NLP Finetuning Controls): all three backbone families tested, all ΔR²=0.000
- **Bonferroni correction** (Appendix, Bonferroni Correction): 48/63 tests survive; all 8 core tests remain significant
- **Linear probe replication** (Appendix, Linear Probe Replication): consistent with MLP probe patterns, ruling out capacity artifacts
- **Explicit metric incommensurability** (§4.4): Cohen's d vs. cosine distance clearly separated; cross-metric ratios explicitly flagged as invalid
- **Claim-Evidence figure** (Appendix, Claim-Evidence Summary, Figure): each finding paired with supporting evidence and acknowledged scope boundary
- **Comprehensive Limitations** (§6): N=2 VLM-to-VLA transitions, LIBERO-only, causal-decoder only, open-loop, single checkpoint, underpowered behavioral correlation—all explicitly stated
- **Training-type asymmetry disclosure** (§3.1): OpenVLA VLA-to-VLA vs. TracVLA/NORA VLM-to-VLA clearly distinguished throughout
- **Concurrent work differentiation** (§2): Fang et al. (behavioral vs. representational), Buurmeijer et al. (motor features vs. instruction routing), Kachaev et al. (visual collapse vs. action decodability)
- **Closed-loop attempt documented** (Appendix, Extended Discussion): SR=0/3 reported transparently rather than omitted
- **Probing caveat** (§4.6): explicit "decodability, not causal reliance" disclaimer
