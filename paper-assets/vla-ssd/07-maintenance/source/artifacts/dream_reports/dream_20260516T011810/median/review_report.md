---
dream_id: dream_20260516T011810
tier: median
overall_score: borderline
timestamp: 2026-05-16T01:53:31.438581+00:00
---

# Dream Review Report: "What Does Fine-Tuning Actually Learn?"

**Paper:** What Does Fine-Tuning Actually Learn? Representational Analysis of Action Structure in Vision-Language-Action Models
**Review Mode:** Full (2 Reviewers + Roundtable)
**Venue Standard:** Top ML venue, ~25% acceptance rate, 6-point scale

---

## Reviewer Assignments

- **R1:** Methods and Experiments (Score: 3/6, Confidence: 4/5)
- **R2:** Novelty and Related Work (Score: 4/6, Confidence: 4/5)

---

## R1 Review: Methods and Experiments

### Summary
The paper performs a systematic representational decomposition of OpenVLA using RSA, CKA, and functional action probes across a 2×2 factorial design (trained/untrained × with/without instruction), with encoder controls (CLIP-ViT, DINOv2) and cross-benchmark validation (LIBERO-Goal, LIBERO-Spatial). The experimental design is thorough and the statistical framework is generally sound, but several methodological issues — including a potential probe type mismatch, incomplete handling of the RSA-to-function causal gap, and suspiciously uniform cross-benchmark replication numbers — reduce confidence in the strongest claims.

### Strengths

- **Comprehensive factorial design with appropriate controls.** The 2×2 matrix cleanly isolates training and instruction effects. The four instruction conditions (normal/random/shuffled/empty) in Table 7 converging within ±0.017 is a thorough pre-emption of the "instruction content matters" objection.
- **Multiple complementary metrics.** RSA (local geometric alignment), CKA (global structure), and functional probes (decodability) form a triangulated evidence base. The RSA-CKA ordering reversal (Table 5) is honestly reported and provides genuine insight.
- **The geometric-functional dissociation is genuinely novel.** DINO R²=0.712 ≈ SigLIP R²=0.706 (p=0.22) while RSA differs dramatically (0.388 vs 0.615) — this separates information presence from geometric alignment. Non-obvious and has clear design implications.
- **Readout concentration finding is well-supported.** Trained readout R²=0.731 > projector 0.706 > untrained 0.686, with Δ=0.045 (CI=[0.032, 0.058], p<0.0001) being highly significant while distributed structure is invariant — this is the paper's most compelling contribution.
- **CLIP-ViT control properly addresses the SigLIP-specificity confound.** CLIP RSA=0.46 falling between SigLIP and DINO appropriately generalizes the encoder dominance claim.

### Weaknesses

- **Potential probe type mismatch.** The paper states "ridge regression probes" (Section 3.4), but project artifacts suggest a 2-layer MLP probe (Linear→ReLU→Linear, 256 hidden). If actual probes are nonlinear, the "linearly decodable" interpretation is compromised. This discrepancy must be clarified — if the probes are indeed MLPs, the paper must revise its method description and reconsider the implications.
- **"Untrained" control definition is unclear.** The paper states "untrained LLM with random-initialized action head" but does not clearly distinguish between (a) pre-fine-tuning Prismatic VLM checkpoint (language-pretrained Llama) and (b) from_config() random reinitialization of all LLM weights. If (b), the trained-vs-untrained comparison conflates VLA fine-tuning with LLM pretraining effects, and finding similar distributed RSA is partially expected since the dominant signal source (256 SigLIP image tokens) is identical in both conditions.
- **LIBERO-Spatial results warrant verification.** The cross-benchmark ratios (Table 8: -15% to -18%) and readout concentration reduction (-44%) show remarkable numerical regularity. It should be confirmed these come from actual computed features rather than projected estimates, particularly given the review context lists these as "expected results."
- **RSA distance metric asymmetry not justified.** Cosine distance for representations and Euclidean distance for 7-DoF actions introduces a methodological choice that could affect results. A sensitivity analysis with matched metrics would strengthen confidence.
- **Per-layer RSA described as "degradation" without qualification.** Table 4 shows Proj→L1 as the biggest drop (0.137-0.253) with partial recovery in mid-layers. The non-monotonic pattern suggests something more nuanced than simple degradation.
- **Multiple comparisons correction absent.** Numerous pairwise bootstrap tests across Tables 2, 6, 7, 8, 9 without family-wise error rate control.
- **No behavioral validation.** No task success rates reported. A correlation between per-task RSA and per-task success would ground the geometric alignment metric practically.

### Questions for Authors

1. Can you confirm: are the functional probes ridge regression or MLP? If MLP, how do results change with a truly linear probe?
2. What is the exact definition of the "untrained" model — pre-trained Llama or random initialization?
3. Were LIBERO-Spatial results (Tables 8-9) actually computed from extracted features on that benchmark?
4. How are action-space RDMs computed? Raw 7-D Euclidean, or standardized actions?
5. Is RSA computed pooled across tasks or per-task then averaged? The choice matters significantly.
6. Can you report the bootstrap CI width for the projector RSA? If wide, the projector-to-VLA gap may be less certain.

### Preliminary Score: 3/6
### Confidence: 4/5

---

## R2 Review: Novelty and Related Work

### Summary
The paper's central thesis — that VLA fine-tuning learns information "routing" rather than "creating" new action representations — provides a representational-level explanation for recent behavioral findings. The most genuinely novel finding is the geometric-functional dissociation (DINO matches SigLIP in probe R² but diverges dramatically in RSA), and the trained-vs-untrained comparison fills a real gap in the VLA interpretability literature. However, the "routing not creating" framing overstates conceptual novelty, the paper is substantially confirmatory of prior behavioral work, and the single-architecture scope limits generalizability.

### Strengths

- **Geometric-functional dissociation is a genuine conceptual contribution.** No prior VLA work has cleanly separated "action information is present" (R²) from "representations are geometrically aligned" (RSA). The finding that DINO ≈ SigLIP in R² but DINO << SigLIP in RSA (0.388 vs 0.615) reframes VL pretraining's role from information provision to geometric organization.
- **First trained-vs-untrained representational comparison in VLA domain.** Every prior VLA interpretability paper (Grant 2026, Swann 2026, Haon 2025, Lu 2025, Molinari 2025) examines only the trained model. The controlled untrained baseline enables causal attribution — a genuine methodological advance.
- **RSA-CKA dissociation adds analytical depth.** Reporting ordering reversal rather than cherry-picking the cleaner metric demonstrates methodological sophistication and reveals that the LLM selectively transforms different aspects of representation structure.
- **Instruction invariance evidence is unusually thorough.** Four instruction conditions + 2×2 factorial = triple invariance (training × instruction presence × instruction content).
- **CLIP-ViT control effectively generalizes Claim 1** from "SigLIP is special" to "VL pretraining provides geometric alignment."

### Weaknesses

- **"Routing not creating" overstates novelty.** The insight that frozen pretrained encoders carry task-relevant information while fine-tuning performs shallow adaptation is established in adjacent fields — Aghajanyan et al. (2021, intrinsic dimensionality of fine-tuning), the broader transfer learning literature. The paper presents this as discovery rather than VLA-specific confirmation of a known principle.
- **Substantially confirmatory of Grant et al. (2026).** Grant et al. demonstrated across 6 architectures and 4 benchmarks that the visual pathway dominates and language is "encoded but not used." This paper provides representational evidence for the same conclusion on 1 architecture. The unique incremental contribution (geometric-functional dissociation, readout concentration) is somewhat buried under broader claims that recapitulate Grant's findings.
- **Claim 3 rests on an underpowered null result without equivalence testing.** p=0.20 with n=10 tasks does not constitute positive evidence of equivalence. A TOST procedure with pre-specified equivalence margin is needed. Absence of evidence ≠ evidence of absence. This is the paper's boldest claim and its weakest statistical foundation.
- **"Untrained" control is extreme, making Claim 3 partially tautological.** Random-initialized LLM vs fine-tuned LLM, with the identical frozen SigLIP encoder providing 256 image tokens that dominate the image_mean aggregation — similar distributed RSA is partially expected by construction. A base pretrained Llama (language-pretrained, no action fine-tuning) would be far more informative.
- **LIBERO instruction redundancy may make instruction invariance trivially expected.** As Hou (2026, LangGap) documented, LIBERO assigns one task per layout — instructions are redundant. The finding may reflect benchmark design rather than a general VLA property.
- **Single architecture limits all claims.** The title says "VLAs" (plural) but evidence covers only OpenVLA (SigLIP+Llama). Modern VLAs are architecturally diverse (pi0 flow matching, Octo diffusion heads, GR00T multi-pathway). The projector-bottleneck mechanism may be architecture-specific.

### Missing Related Work

- **Aghajanyan et al. (2021)** — Intrinsic dimensionality of fine-tuning. Direct conceptual precursor to "routing not creating." Must be cited.
- **Huh et al. (2024)** — Platonic Representation Hypothesis. Relevant to explaining why DINO/SigLIP have comparable R² despite different pretraining.
- **Voita et al. (2019)** — Attention head specialization and information routing in transformers.
- **Hewitt & Manning (2019)** — Probe complexity concerns. Needed given the probe methodology question.
- **Belinkov & Glass (2019)** — Probing survey. Broader NLP probing context entirely absent.
- **Related work section is thin** (4 short paragraphs) for a paper whose primary contribution is analytical positioning.

### Assessment of Claims

| Claim | Verdict | Reasoning |
|-------|---------|-----------|
| Claim 1: VL-pretrained encoder geometric dominance | **Partially supported** | RSA ordering convincing, but "dominance" is geometric only — functional probes show all encoders carry comparable action info. Projector trained for SigLIP's output space is a confound vs raw CLIP/DINO. |
| Claim 2: LLM degrades geometry, concentrates readout | **Supported** | Multi-metric evidence: RSA degradation, functional probe degradation at image_mean, readout concentration (Δ=0.045, p<0.0001), CKA-RSA dissociation. Strongest claim. |
| Claim 3: Training-invariant distributed structure → routing not creating | **Partially supported** | Readout concentration training-dependence is well-supported. But "training-invariant distributed structure" relies on null result without equivalence testing, using extreme control (random LLM). The framing oversells: LLM could create structure in dimensions RSA/CKA don't capture. |

### Preliminary Score: 4/6
### Confidence: 4/5

---

## Roundtable Synthesis

### Points of Consensus

1. **Best contribution:** The geometric-functional dissociation (DINO ≈ SigLIP in R² but << in RSA) is the paper's most original and valuable finding. Both reviewers independently identified this as the standout result.
2. **Strongest claim:** Claim 2 (readout concentration, Δ=0.045, p<0.0001) has robust multi-metric support and is not challenged by the methodological concerns.
3. **Weakest claim:** Claim 3 (training invariance of distributed representations) relies on a null result without equivalence testing, using an extreme control that partially pre-determines the outcome. Both reviewers flag this independently.
4. **Probe methodology transparency** must be resolved — whether probes are ridge regression (as stated) or MLP (as suggested by artifacts). This affects interpretation of all R² comparisons.
5. **Single-architecture limitation** is a real tension with the paper's general framing. The title ("VLAs") overpromises relative to the evidence (one OpenVLA instance).
6. **LIBERO-Spatial data integrity** needs confirmation.

### Points of Divergence

- R1 weighted methodological integrity concerns more heavily (probe mismatch, data integrity → score 3/6); R2 weighted novelty assessment (incremental over Grant 2026, conceptual precedent in fine-tuning literature → score 4/6). After discussion, both agree the paper has genuine merit in its geometric-functional dissociation and readout concentration findings, but presentation and transparency issues currently undermine it.

### Consolidated Score: 3.5/6 (Borderline — between Weak Accept and Weak Reject)

### Key Recommendations for Revision

**Must fix (blocking):**
1. Clarify probe methodology — confirm ridge regression or MLP, report both if possible. If MLP, revise "linearly decodable" language.
2. Precisely define "untrained" control (random init vs pre-trained Llama). If random init, acknowledge that similar distributed RSA is partially expected when the signal source (256 SigLIP tokens) is identical.
3. Confirm LIBERO-Spatial results are from actual experiments, not projections.
4. Add TOST equivalence test for Claim 3 with pre-specified margin.

**Should fix (important):**
5. Cite Aghajanyan et al. (2021) and position "routing not creating" as VLA-specific confirmation of known fine-tuning dynamics, not a novel conceptual framework.
6. Expand Related Work — currently too thin for a positioning paper. Discuss Hewitt & Manning (2019), Huh et al. (2024), and broader probing literature.
7. Qualify per-layer RSA description: "net degradation with non-monotonic partial recovery" rather than unqualified "degrades."
8. Scope title/claims to OpenVLA or add explicit single-architecture caveat earlier.
9. Discuss LIBERO instruction redundancy as a confound for the instruction invariance finding.

**Nice to have:**
10. Report per-task RSA breakdown for CLIP-ViT (high per-task variance noted).
11. Behavioral validation: correlate per-task RSA with per-task success rate.
12. RSA sensitivity analysis with matched distance metrics.
13. Permutation null distribution for CKA values.
14. Add base pretrained Llama (no action fine-tuning) as intermediate control.

### Overall Assessment

The paper addresses a genuine and important question — what does VLA fine-tuning actually learn? — with a well-designed experimental framework. The geometric-functional dissociation (action information is encoder-agnostic but geometric alignment is encoder-specific) and the readout concentration mechanism (Δ=0.045, p<0.0001) are real contributions. However, the paper is undermined by: (1) potential methodological misreporting (probe type), (2) an underpowered statistical foundation for its boldest claim (Claim 3), (3) overstatement of conceptual novelty relative to the broader fine-tuning literature and Grant et al.'s multi-architecture behavioral work, and (4) single-architecture scope that constrains the generality of conclusions. With the recommended revisions — particularly resolving the probe methodology, adding equivalence testing, and repositioning the novelty claims — this could be a solid contribution to VLA understanding at a top venue.
