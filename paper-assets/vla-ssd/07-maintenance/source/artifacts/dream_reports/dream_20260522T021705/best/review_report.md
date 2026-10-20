---
dream_id: dream_20260522T021705
tier: best
overall_score: weak reject (4.5/10)
timestamp: 2026-05-22T03:25:36.715959+00:00
---

<![CDATA[# Reviewer R2: Novelty and Related Work Positioning

**Paper:** "Token-Level Instruction Routing in Vision-Language-Action Models: A Cross-Architecture Analysis"
**Venue:** CoRL 2026
**Reviewer Focus:** Novelty, related work completeness, contribution significance, claim calibration

---

## Summary

This paper applies a battery of established interpretability tools (linear probing, attention analysis, RSA, CKA, counterfactual perturbation) to three decoder-only VLA architectures across four LIBERO task suites. The main empirical finding is "R² exit collapse"---task-finetuned VLAs lose action-predictive information at exit layers relative to mid-layers, a pattern absent in untrained models---confirmed in 9/10 tested cells. The paper additionally distinguishes training-induced effects from base-model-inherited effects and proposes a three-tier routing gradient. While the cross-architecture scope is broader than prior VLA interpretability work, the novelty is limited by the use of entirely standard methods, the descriptive (non-explanatory) nature of the findings, and the absence of any connection to downstream robot performance.

---

## Strengths

- **Cross-architecture breadth is the paper's primary novelty.** Testing three backbone families (Llama-2-7B/MHA, Phi-3-mini/MHA, Qwen2.5-VL-3B/GQA) with different attention mechanisms goes beyond all prior VLA interpretability work, which has been single-architecture. The 3x4 matrix design with 10 populated cells is a genuine structural contribution to experimental methodology in this subfield.

- **Training-vs-inherited decomposition is a useful conceptual contribution.** The finding that L1 attention routing is base-model-dependent---TracVLA's Phi-3-Vision base already has 32/32 instruction-dominant heads, and training *reduces* this to 27-30/32---is counterintuitive and corrects a potential misattribution that would be easy to make from single-architecture studies. The OXE-pretrained OpenVLA comparison (25/32 untrained vs 24/32 trained) is clean evidence.

- **Scientific transparency is above average.** The paper honestly reports: the OFT outlier (Delta=0.004), the RSA/CKA ordering reversal, the metric dependence of geometric claims, NORA's incomplete coverage (2/4 suites), and the OpenVLA Spatial CF inversion (0.81x). This level of self-qualification is commendable and relatively rare.

- **R² exit collapse is empirically robust within the tested scope.** 9/10 cells with a Wilcoxon p=0.002 and effect size r=0.81, with the single exception well-explained by OFT's parameter-efficient mechanism, constitutes a solid descriptive finding.

- **TracVLA universal mixed heads (h13, h22).** The observation that two specific heads consistently appear as "mixed" across all four suites in trained TracVLA but not in the untrained base is a concrete, reproducible finding that could seed follow-up mechanistic work.

---

## Weaknesses

### Major

1. **The "framework" contribution (C1) is method application, not method innovation.** (Major, Novelty)
Every component---cross-instruction probing (Alain & Bengio 2017), attention profiling (standard since Vaswani 2017), RSA (Kriegeskorte 2008), CKA (Kornblith 2019), counterfactual perturbation (widely used in causal interpretability)---is an established tool. The paper does not propose new metrics, new analysis methods, or new theoretical frameworks. Combining existing tools and applying them to VLAs is valuable engineering but does not constitute a methodological contribution at main-conference level. Calling this a "systematic token-level analysis framework" overstates what is essentially a checklist of known techniques. The factorial design (trained/untrained x instruction presence) is standard experimental methodology. For C1 to stand as a contribution, the paper would need to demonstrate that the specific combination reveals something that no subset of these tools could reveal---this is not shown.

2. **R² exit collapse is descriptive, not explanatory, and may be an expected consequence of fine-tuning.** (Major, Novelty)
The paper documents *that* exit R² drops but offers no mechanistic explanation for *why*. Several mundane explanations exist: (a) task fine-tuning causes the exit layers to specialize for action token generation rather than general representation maintenance---this is the expected behavior of an autoregressive model optimized for a specific output distribution; (b) the exit layers may be performing a lossy compression that discards dimensions irrelevant to the action head while retaining the task-relevant subspace---a linear probe would miss this because it measures variance explained across all dimensions. The paper does not rule out these alternatives. Without mechanistic depth, exit collapse risks being a restatement of "fine-tuning changes what exit layers compute," which is unsurprising. The comparison to untrained models (which have no reason to show exit specialization) does not disambiguate these explanations.

3. **The three-tier gradient (C4) rests on n=1 at Tier 2 and is partially predictable.** (Major, Contribution Significance)
Only OpenVLA has a Tier-2 intermediate checkpoint (openvla-7b, OXE-pretrained). TracVLA and NORA jump directly from VLM base (Tier 1) to task-finetuned (Tier 3). The claim of a "three-tier routing gradient" is therefore validated for exactly one architecture. The progression "no routing -> some routing -> task-specific routing" as a function of "no action training -> general action training -> task-specific action training" is the expected outcome---it would be surprising if this did *not* hold. The interesting scientific question is what *quantitatively changes* at each transition, and the paper's answer (L1 heads stay constant, exit collapse appears, CF sensitivity reshapes) is partially undermined by the CF metric inconsistency (see below). Listing this as a full contribution (C4) with n=1 Tier-2 support is generous.

4. **Counterfactual sensitivity claim ("7-10x amplification") conflates incommensurable metrics.** (Major, Claim Calibration)
Trained models are measured with Cohen's d in action space; untrained VLM bases are measured with cosine distance in hidden representation space. These are fundamentally different quantities---ratios across them are meaningless. When the same metric (Cohen's d) is applied to the OXE-pretrained model (the only untrained model that can generate actions), the trained model actually shows *lower* sensitivity (d=0.96 vs OXE d=1.05 on Goal-empty; d=0.94 vs d=1.02 on Spatial-empty). This directly contradicts the "heightened counterfactual sensitivity" narrative for Tier-2 -> Tier-3 transitions. The paper reports this data (Table 7) but still claims "7-10x amplification" in the abstract and contributions, which is misleading. The honest framing would be: "Tier-1 VLM bases show negligible CF sensitivity; Tier-2 and Tier-3 show comparable sensitivity by Cohen's d; the comparison between Tier-1 and Tier-3 uses different metrics and should not be quantified as a ratio."

5. **"Architecture-independent" is overclaimed for the tested scope.** (Major, Claim Calibration)
All three tested architectures are decoder-only autoregressive transformers with causal attention masks processing concatenated image-instruction-action sequences. This is one architectural family. Cross-attention VLAs (RT-2 style), diffusion-based action decoders (pi0), and dual-pathway architectures (pi0.5, GR00T) are untested. OpenVLA passes only 50% of cells if we count the OFT outlier (Long) and the Spatial CF inversion (0.81x, where training *reduced* instruction sensitivity). Claiming "architecture-independent" when 2/4 cells for the most-studied architecture show anomalous or inverted behavior is a stretch. "Consistent across three tested decoder-only VLA backbones, with caveats" would be accurate.

### Minor

6. **Related work is inadequate for the scope of claims.** (Minor, Related Work)
The latest paper draft (best/paper.tex) has only 7 references. Even the longer related_work.tex section has ~15. For a paper spanning VLA architectures, transformer interpretability, representational analysis, and instruction grounding in robotics, this is insufficient. Critical omissions detailed below.

7. **C3 (training-induced vs base-model-dependent) may be partially obvious.** (Minor, Novelty)
That a VLM pretrained on language data already has language-processing attention heads is expected. The contribution is in *documenting* this for VLAs specifically and showing that fine-tuning does not create but may even reduce instruction-dominant heads. This is valuable but incremental---it is an empirical verification of what architecture knowledge would predict, not a discovery.

8. **No actionable design implications despite claiming them.** (Minor, Significance)
The abstract states findings "provide mechanistic grounding for VLA architecture design and training diagnostics." The conclusion says "entry-exit routing patterns and exit collapse diagnostics can guide architecture optimization and training monitoring." These claims are not substantiated with any concrete recommendation, ablation showing improved design, or demonstrated diagnostic application. What should a practitioner *do differently* based on these findings?

9. **OpenVLA-centric despite cross-architecture framing.** (Minor, Presentation)
The detailed analyses (full-layer R² scan, RSA profiles, L1 attention 3-condition breakdown, three-tier gradient tables, vision encoder geometry, branch-split RSA) are all OpenVLA results. TracVLA and NORA appear primarily in the R² exit collapse matrix (Table 3), the L1 heads table (Table 9), and scattered CF values. The paper reads as an OpenVLA study with TracVLA/NORA confirmation, not as a true three-architecture analysis of equal depth.

10. **Purely representational analysis at a robotics venue.** (Minor, Relevance)
CoRL values contributions to robot learning. This paper contains no robot evaluation, no closed-loop experiment, no demonstration that the discovered patterns predict or influence task success, and the one ablation result mentioned (removing instruction-dominant heads has no effect on MSE) actually *undercuts* the functional relevance of the routing patterns. The roadmap shows "behavioral_pilot" experiments were planned but remain in "preparing" status. This work might be better positioned at an interpretability workshop (ICML MechInterp, NeurIPS XAI) or a methods venue.

---

## Questions for Authors

1. Can you provide a mechanistic explanation for *why* exit collapse occurs? Specifically, can you rule out the trivial explanation that exit layers simply specialize for action-token generation (a different task than maintaining general-purpose representations), making probe R² drop for the same reason that probing a classification head for input features yields low R²?

2. The CF sensitivity claim of "7-10x" conflates Cohen's d with cosine distance. When measured with the same metric (Cohen's d), OXE-pretrained models show *higher* sensitivity than task-finetuned models (d=1.05 vs d=0.96 on Goal-empty). How do you reconcile this with the "heightened counterfactual sensitivity" narrative? Would you consider reframing this claim?

3. Can you validate the three-tier gradient for TracVLA or NORA? Do intermediate pretraining checkpoints exist for these architectures? Without them, C4 is a single-architecture observation.

4. The paper mentions that ablating 24/32 instruction-dominant heads produces no change in action MSE. If the routing you document has no measurable functional consequence, what is its significance for robot learning?

5. How do you differentiate this work from standard transformer interpretability applied to a new model class? What is VLA-specific about the framework beyond choosing to probe at image/instruction/action token positions?

6. The paper claims "architecture-independent" but OpenVLA has 50% anomalous cells (Long: Delta=0.004; Spatial: CF ratio inverted at 0.81x). How do you justify this characterization?

---

## Missing References / Comparisons

The paper's reference list is critically thin. The following categories of work should be cited and discussed:

**VLA Interpretability (direct competitors not cited in best/paper.tex):**
- Swann et al. 2026 (arXiv 2603.19183): SAE features on OpenVLA---methodologically complementary (feature-level vs representation-level)
- Rizzardo et al. 2026 (arXiv 2603.05487): Feature observability/controllability in VLAs---directly comparable analysis scope
- Molinari et al. 2025 (arXiv 2509.24559): World model probing in OpenVLA---layer-wise probe results directly comparable
- Lu et al. 2025 (arXiv 2502.04558): Symbolic state probing in OpenVLA on LIBERO---closest methodological predecessor
- Fang et al. 2025 (arXiv 2506.09930): VLA generalization boundaries via probing---"fine-tuning erodes VLM reasoning" is directly relevant

**Language Grounding / Counterfactual in VLAs:**
- Fang et al. 2026 (arXiv 2602.17659): LIBERO-CF counterfactual benchmark---directly validates "language not used" at behavioral level
- Hou et al. 2026 (arXiv 2603.00592): LangGap diagnosis of language underutilization---systematic evidence supporting the paper's narrative

**LLM Mechanistic Interpretability:**
- Elhage et al. 2021/2022 (Anthropic): Mathematical framework for circuits in transformers---foundational for any mechanistic claim
- Conmy et al. 2023: Automated circuit discovery---relevant methodology not considered
- Bills et al. 2023 (OpenAI): Language model internals via GPT-4---scaling interpretability

**Probing Methodology Critiques:**
- Hewitt & Liang 2019: Control tasks for probing---the paper mentions this work in paper_framing.md but does not cite it; the "information-computation dissociation" claim requires this reference
- Belinkov 2022 is cited but the discussion of probing limitations is cursory

**VLA Architectures (for positioning):**
- Octo (Ghosh et al. 2024): Alternative non-LLM-based VLA
- pi0 (Black et al. 2024): Flow-matching action head---different action representation paradigm
- LIBERO benchmark (Liu et al. 2023): Cited but deserves more detailed discussion of its known limitations (single layout per task, memorization concerns per LIBERO-PRO/LIBERO-Plus)

**Representation Similarity in Multimodal Models:**
- Work on CLIP internal representations (e.g., Gandelsman et al. 2023)
- CKA/RSA applied to vision-language models beyond VLAs

The literature_map.yaml shows the authors are *aware* of most of these works but chose not to cite them. This is a significant missed opportunity---positioning against Swann, Rizzardo, Molinari, and Lu would sharpen the novelty claim considerably.

---

## Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Overall** | **4.5 / 10** | Solid empirical observation (exit collapse) but limited novelty (standard tools, descriptive finding), overclaimed contributions (C4 on n=1, CF 7-10x on mixed metrics), and insufficient relevance to robot learning without behavioral validation |
| Soundness | 2.5 / 4 | R² exit collapse is statistically sound; CF claim is methodologically flawed; three-tier gradient underdetermined |
| Contribution | 1.5 / 4 | Four claimed contributions but C1 is method application, C3 is partially obvious, C4 has n=1 support; C2 (exit collapse) is the genuine contribution |
| Clarity | 3 / 4 | Well-written, transparent, good table design; but OpenVLA-centric structure contradicts cross-architecture framing |
| Confidence | 4 / 5 | High familiarity with the VLA interpretability literature, probing methodology, and RSA/CKA. Moderate uncertainty on whether exit collapse has deeper mechanistic significance not captured by my "trivial explanation" alternative |

---

## Decision Recommendation: **Weak Reject**

The R² exit collapse finding (9/10 cells, p=0.002) is empirically credible and the cross-architecture scope exceeds prior work. However, the paper has too many issues for acceptance at CoRL's ~30% rate:

1. The core finding is descriptive and may be an expected consequence of fine-tuning (exit layers specialize for their loss function).
2. The CF "7-10x" claim in the abstract is misleading due to metric inconsistency---when measured consistently, the effect inverts for Tier-2 comparisons.
3. Three of four claimed contributions are inflated: C1 is tool application, C3 is empirical verification of the expected, C4 has n=1 support.
4. No connection to downstream robot performance at a robotics venue.
5. Related work is critically sparse given the breadth of claims.

The paper would benefit from: (a) a mechanistic explanation of exit collapse beyond description, (b) pilot behavioral validation linking exit collapse magnitude to task performance, (c) honest reframing of CF amplification with consistent metrics, (d) expanded related work positioning against the 6+ concurrent VLA interpretability papers, and (e) scoping claims to "decoder-only VLAs" rather than "architecture-independent."
]]>