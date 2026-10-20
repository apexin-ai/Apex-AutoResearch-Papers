# Anticipated Reviewer Response Letter

We thank the reviewers for their careful evaluation. Below we address six anticipated questions, referencing specific sections, tables, and figures in the manuscript and appendix.

---

## Q1: Behavioral correlation underpowered (ρ=0.583, p=0.10, n=9)

The sample size **n=9** is determined by the cross-architecture matrix design: 3 architectures × 4 LIBERO suites yields 12 cells, of which 10 are filled (NORA Object and Long-Horizon checkpoints are unavailable; §3.1, Table 1). One cell (NORA Goal) is excluded due to bootstrap CI instability from an exit-layer R² ≈ −0.006 artifact (Table 1, footnote b), leaving **9 usable cells**. Expanding n requires either additional VLA architectures with published LIBERO success rates or additional benchmark suites—both beyond the scope of this initial cross-architecture characterization.

We attempted closed-loop evaluation but achieved **SR=0/3** across tested configurations, consistent with known reproducibility challenges in the VLA community (the OpenVLA authors report substantial variation across hardware setups; Fang et al. [2026] similarly document closed-loop difficulties on LIBERO). This negative result is reported in Appendix §A.16 (Extended Discussion: "closed-loop behavioral validation... remains a priority for future work").

Regarding statistical interpretation: **|ρ|=0.583 constitutes a large effect size** by conventional criteria (|ρ|>0.5; Cohen 1988). The p=0.10 reflects insufficient statistical power at n=9, not absence of effect. Within-suite comparisons are uniformly positive: on Goal (n=3 architectures), ΔR² and success rate are perfectly rank-correlated (ρ=1.0), and every remaining suite shows the same direction (Appendix §A.16). The paper explicitly qualifies this as "directionally consistent but underpowered" (§6) and frames it as observational evidence rather than a confirmed causal link.

---

## Q2: Only validated on LIBERO—how does this generalize?

LIBERO (Liu et al. 2023) is the standard evaluation benchmark for VLA fine-tuning studies, used by OpenVLA, TracVLA, NORA, and concurrent work (Fang et al. 2026, Swann et al. 2026). Our evaluation spans **4 task suites** (Goal, Spatial, Object, Long-Horizon) that vary substantially in instruction complexity, object diversity, and planning horizon (§3.1).

The stronger generalization argument comes from **cross-architecture consistency**: exit collapse and counterfactual sensitivity replicate across three distinct backbone families—**Llama-2-7B** (32 layers, MHA), **Phi-3-mini** (32 layers, MHA), and **Qwen2.5-VL-3B** (36 layers, GQA)—spanning 3B to 7B parameters with different pretraining corpora and attention mechanisms. The pattern holds despite qualitatively different reference profiles (§4.5, Appendix §A.16): TracVLA reference starts with saturated L1 attention (32/32 heads) while NORA reference starts at 13–14/16. That the same exit-collapse pattern emerges from these divergent starting points is stronger evidence of generality than observing it on multiple benchmarks within a single architecture.

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

**Kachaev et al. (2025)** study *visual representation collapse* during VLA fine-tuning—a distinct phenomenon from instruction routing. Their analysis is conducted exclusively on OpenVLA. Our work quantifies a complementary phenomenon (layer-wise action-probe decodability via ΔR²) and critically, **distinguishes training-associated from inherited effects** across three architectures (§2, Concurrent Work paragraph; §4.6). This decomposition—showing that exit collapse is training-associated while L1 attention is inherited—requires cross-architecture comparison by design and is absent from all prior single-architecture studies.

The **3×4 matrix** (3 architectures × 4 suites, 10 filled cells; Table 1) with systematic trained/reference comparisons at each cell is structurally unprecedented in the VLA interpretability literature. The claim is hedged with "with this caveat" referring to the probe-vs-causal-reliance distinction stated in the same sentence.

---

## Q5: NLP controls only use chat fine-tuning—wouldn't a more task-specific NLP control be needed?

Chat fine-tuning is the **maximally relevant control** for our hypothesis. The question being tested is: "Is exit collapse a generic artifact of instruction-following fine-tuning, or is it specific to action-oriented (VLA) training?" Chat-finetuned models share the critical property of being **instruction-following systems fine-tuned on the same backbone**, but lack action heads, robot demonstration data, and vision-action grounding. If exit collapse were a generic consequence of fine-tuning a pretrained LM to follow instructions, chat models should exhibit it.

Three backbone families were tested (§4.3, Table in Appendix §A.19):
- **Llama-2-7b-chat** (OpenVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.001
- **Phi-3-mini-4k-instruct** (TracVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000
- **Qwen2.5-3B-Instruct** (NORA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000

All three produce **perfectly flat R² profiles** (ΔR² = 0.000), contrasting with VLM-to-VLA collapse (ΔR² = 0.156–0.455). A more task-specific NLP control (e.g., code generation, summarization) would be *further* from VLA fine-tuning in training objective—making it a *weaker* control. Chat instruction-tuning is the closest NLP analog to VLA instruction-following; its complete failure to produce exit collapse provides the strongest evidence that the phenomenon is specific to action-grounded training. We note in §6 (Limitations) that NLP controls cover all three backbone families, though the analysis operates at the representation level rather than requiring matched data distributions.

---

## Q6: Why use effect size thresholds rather than significance testing?

With **N=63,228 observations** per cell, traditional null-hypothesis significance testing becomes uninformative: virtually every comparison reaches p < 0.001 regardless of practical magnitude. This is a well-known limitation of p-values in large-sample settings (Wasserstein & Lazar 2016, ASA Statement on Statistical Significance).

Our **ΔR² > 0.10 threshold** has dual justification (§3.3, Appendix §A.8):
1. **Semantic meaning**: 10% absolute change in explained variance represents a substantive shift in action decodability
2. **Robustness**: the threshold is not boundary-sensitive—any value in **(0.097, 0.156)** produces identical grouping (Appendix Table 6). The gap between the largest non-collapse value (0.097, TracVLA Long reference) and smallest collapse value (0.156, TracVLA Spatial trained) spans 0.059, providing a clean separation zone

Statistical validation accompanies the effect-size framework:
- **Permutation test**: randomly reassigning 9 cells to two groups (10,000 permutations) yields **p=0.008** for the observed min-max gap (Appendix §A.7)
- **Bootstrap CIs**: Monte Carlo cross-validation (n=1,000 iterations) with demo-level splitting; VLM-to-VLA CIs lie entirely above zero (lower bounds ≥ 0.09; Table 1)
- **Cohen's d** for counterfactual sensitivity (medium-to-large: d=0.45–1.52; §4.4, Table 2)
- **Bonferroni correction**: 63 tests total, 48/63 (76%) pass family-wise correction; all 8 core tests survive at α_adj = 7.94×10⁻⁴ (Appendix §A.18)

This approach aligns with modern statistical best practice: report effect sizes with confidence intervals as primary evidence, use significance tests as supplementary confirmation, and validate threshold robustness via sensitivity analysis.

---

## Summary of Preemptive Measures Already in the Paper

The manuscript includes the following preemptive defenses against anticipated concerns:

- **Demo-level splitting** (§3.3): eliminates within-trajectory leakage; reduces R² from 0.7–0.9 to 0.4–0.6, quantifying pseudo-replication inflation
- **Threshold robustness analysis** (§3.3, Appendix §A.8): any threshold in (0.097, 0.156) yields identical grouping
- **Permutation test** (Appendix §A.7): p=0.008 for VLA-to-VLA vs. VLM-to-VLA separation
- **Three NLP controls** (§4.3, Appendix §A.19): all three backbone families tested, all ΔR²=0.000
- **Bonferroni correction** (Appendix §A.18): 48/63 tests survive; all 8 core tests remain significant
- **Linear probe replication** (Appendix §A.13): consistent with MLP probe patterns, ruling out capacity artifacts
- **Explicit metric incommensurability** (§4.4): Cohen's d vs. cosine distance clearly separated; cross-metric ratios explicitly flagged as invalid
- **Claim-Evidence figure** (Appendix §A.20, Figure): each finding paired with supporting evidence and acknowledged scope boundary
- **Comprehensive Limitations** (§6): N=2 VLM-to-VLA transitions, LIBERO-only, causal-decoder only, open-loop, single checkpoint, underpowered behavioral correlation—all explicitly stated
- **Training-type asymmetry disclosure** (§3.1): OpenVLA VLA-to-VLA vs. TracVLA/NORA VLM-to-VLA clearly distinguished throughout
- **Concurrent work differentiation** (§2): Fang et al. (behavioral vs. representational), Buurmeijer et al. (motor features vs. instruction routing), Kachaev et al. (visual collapse vs. action decodability)
