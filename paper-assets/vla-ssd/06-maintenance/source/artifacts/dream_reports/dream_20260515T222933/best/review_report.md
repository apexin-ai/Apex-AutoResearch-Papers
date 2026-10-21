---
dream_id: dream_20260515T222933
tier: best
overall_score: borderline reject
timestamp: 2026-05-15T22:56:25.230693+00:00
---

# Dream Review Report: "Vision Encoders, Not Language Models, Drive Action-Relevant Representations in VLAs"

**Venue**: CoRL 2026 | **Review Mode**: Full | **Reviewers**: R1 (Methods+Experiments), R2 (Novelty+Related Work)

---

## Venue Calibration

**CoRL review dimensions**: Originality, Quality, Clarity, Significance, Relevance, Limitations.
**Acceptance rate**: ~39% (2021-2024 average). **Scale**: adapted from CoRL 2024 (1-4); mapped below.
**Key venue norms**: papers need not beat SOTA; simulation-only is acceptable; limitations section required and rewarded for honesty; relevance to robot learning is essential.

---

## Paper Summary

The paper presents the first systematic representational analysis of a VLA (OpenVLA = SigLIP + projector + Llama-2-7B), decomposing contributions from vision encoder, projector, and LLM backbone using RSA and CKA across three LIBERO suites. Three claims: (1) frozen SigLIP+projector achieves highest action alignment (RSA ρ=0.615 vs. VLA ρ≈0.488 vs. DINOv2 ρ=0.388); (2) LLM processing monotonically degrades action-relevant geometry across 33 layers (Spearman ρ=−0.88); (3) neither fine-tuning (Δ<0.01) nor instruction content (Δ<0.005) significantly alters this structure.

---

## Experiment Coverage Assessment

All 4 planned experiments from the experimental design are present in the paper:

| # | Planned Experiment | Paper Section | Status |
|---|---|---|---|
| 1 | Per-layer RSA degradation curve | §4.2, Table 2 | ✓ Covered |
| 2 | Random instruction control (5 conditions) | §4.3, Table 3 | ✓ Covered |
| 3 | CKA cross-validation | §4.4, Table 4 | ✓ Covered |
| 4 | LIBERO-Spatial benchmark extension | §4.5, Tables 5-6 | ✓ Covered |

**Coverage**: 4/4 (100%). The paper includes all planned analyses with corresponding tables.

---

## Reviewer 1 (R1): Methods and Experiments

### Assessment Summary
The methodology is technically sound in its core design — the 2×2 factorial with trained/untrained × with/without instruction is well-structured, and the choice of RSA + CKA as complementary metrics is appropriate. However, several methodological concerns limit confidence in the strongest claims.

### Strengths

- **Clean factorial design.** The 2×2 matrix (Table 1) cleanly isolates training and instruction effects. Bootstrap 95% CIs reported for all pairwise comparisons. The narrow convergence band (0.479–0.488) across four conditions is convincing evidence for Claim 3.

- **Five-condition instruction control is thorough.** Testing real, random English, shuffled tokens, padding, and no-instruction (Table 3) pre-empts the "semantic content matters" objection. The convergence within σ=0.003 and bootstrap CI [−0.031, 0.038] spanning zero is strong.

- **CKA cross-validation adds methodological robustness.** Both linear and RBF-kernel CKA (Table 4) preserve the same ordering with rank correlation r=0.98 vs. RSA, ruling out metric-specific artifacts. Per-layer CKA monotonicity (ρ=−0.85) corroborates the RSA degradation trajectory.

- **Cross-benchmark consistency.** Three LIBERO suites yield r=0.96 correlation in RSA values (Table 6), demonstrating within-ecosystem robustness.

- **Per-layer analysis goes beyond two-point comparisons.** Table 2 provides the full 33-layer RSA trajectory with clear steep-drop (L0-12) and plateau (L20-32) phases, adding mechanistic granularity.

### Weaknesses

- **RSA measures geometric alignment, not functional relevance.** The paper equates "lower RSA with action structure" with "degradation," but the LLM's objective is to produce correct action tokens, not to preserve Euclidean distance geometry. It is entirely possible that the LLM transforms representations in ways that reduce RSA but are essential for action decoding. Without testing whether projector-output features can actually drive action prediction (a linear probe or bypass experiment), the "degradation" framing is an interpretation, not a demonstrated fact.

- **The SigLIP vs. DINOv2 comparison has an uncontrolled confound.** SigLIP uses vision-language contrastive pretraining; DINOv2 uses self-supervised visual pretraining. The 0.227 RSA gap (Table 1) could reflect the language grounding in SigLIP's pretraining rather than any VLA-specific property. Testing a second vision-language encoder (e.g., CLIP ViT-L) or a vision-only SigLIP variant would clarify whether the recommendation is "use better vision encoders" or "use language-supervised vision encoders specifically."

- **The "untrained" control is partially tautological for Claims 1 and 3.** Since the frozen SigLIP encoder and projector are identical across trained and untrained conditions, and visual tokens (256) massively outnumber instruction tokens (~20), finding that RSA is similar across conditions is expected. The dominant signal source is literally the same. The trained/untrained comparison can only tell us that the LLM's learned weights do not *additionally* contribute, not that the LLM contributes *nothing* — RSA/CKA may simply lack sensitivity to the LLM's contributions if they are orthogonal to action-relevant Euclidean distance structure.

- **Statistical reporting for Claim 2 needs scrutiny.** The paper claims "monotonic decrease" with Spearman ρ=−0.88. At 34 data points (projector + 33 layers), even small local non-monotonic fluctuations would reduce this from −1.0. The paper does not report individual layer-to-layer differences with CIs, nor does it test for significant non-monotonic deviations. Without per-step significance, "monotonically decreasing" is a characterization of the trend, not a proven property of every adjacent pair.

- **No discussion of what RSA *should* look like for a functional VLA.** Is RSA ρ=0.488 at the LLM output "low" or "adequate"? Without a reference point — e.g., what RSA a purely behavioral model achieves, or what RSA is needed for a given success rate — the absolute values are hard to interpret. The paper compares components within the model but never grounds the numbers against task performance.

- **Reproducibility gaps.** The paper does not specify: how many observations N were used for the N×N distance matrices, how visual tokens were aggregated (mean pooling? last token? CLS?), which specific DINOv2 model variant was used, or exact hyperparameters for bootstrap resampling. These are essential for reproduction.

### Questions for Authors

1. If you train a linear action predictor on projector output vs. best-LLM-layer representations, which yields lower prediction error? This would ground the RSA "degradation" claim in functional terms.

2. What is N (number of observations) for the RSA distance matrices, and how sensitive are the results to subsampling?

3. How are the 256 visual tokens aggregated into a single representation vector for each observation? Does the aggregation choice affect the SigLIP-VLA gap?

4. Table 2 reports every 4th layer. What do layers 1-3 look like? Is the initial drop (projector→L0 = −0.014) actually smooth or is there a discontinuity at the embedding interface?

5. The untrained VLA achieves Spearman ρ=−0.82 for per-layer monotonicity, very close to the trained model's −0.88. Is the difference between these two statistically significant, or are they indistinguishable?

---

## Reviewer 2 (R2): Novelty, Related Work, Positioning

### Assessment Summary
The paper applies established representational analysis tools (RSA, CKA) to a new domain — the internal pipeline of a VLA — providing the first quantitative component-level decomposition. The core finding that vision encoders dominate action-relevant structure is a genuine empirical contribution, but novelty is substantially diminished by concurrent work (Grant et al. 2026, Hou et al. 2026) that reached similar headline conclusions through behavioral and mechanistic methods. The unique value is the trained-vs-untrained representational comparison and the quantitative precision of the decomposition.

### Strengths

- **First quantitative component-level RSA/CKA decomposition of a VLA.** No prior work has measured representational alignment with action structure at the projector, per-LLM-layer, and standalone vision encoder levels. This moves the "vision dominates" narrative from behavioral observation to representational mechanism.

- **The trained-vs-untrained comparison yields a genuinely novel insight.** Showing that even random-weight LLMs produce nearly identical degradation trajectories (trained ρ=−0.88 vs. untrained ρ=−0.82) demonstrates that degradation is architecture-intrinsic, not weight-specific. This is not derivable from behavioral studies.

- **Claims are well-scoped in the Limitations section.** The authors explicitly acknowledge single-architecture scope and LIBERO-only benchmarks. The Discussion reframes the SigLIP-DINOv2 pretraining confound as a positive insight rather than hiding it.

- **Clear, well-organized writing.** The paper is concise (7 pages), logically structured, and each table directly supports a specific claim. The factorial design is easy to follow.

- **The random instruction control adds precision beyond prior behavioral work.** Hou et al. (2026) and Fei et al. (2025) showed VLAs ignore instructions behaviorally; this paper shows it at the representational level with five graded conditions, adding mechanistic depth.

### Weaknesses

- **The headline finding is largely confirmatory.** Grant et al. (2026) already demonstrated across 6 VLA architectures that the visual processing pathway dominates action generation. Hou et al. (2026) and Fei et al. (2025) showed VLAs largely ignore language instructions. This paper moves the evidence from behavioral to representational, which is a step forward, but the headline conclusion — "vision encoder matters most, LLM and instructions don't" — will not surprise the CoRL 2026 audience. The novelty premium should come from new mechanistic insights, but these (per-layer degradation, architecture-intrinsic property) are narrower than the framing suggests.

- **Single architecture severely limits the strongest claims.** Only OpenVLA (SigLIP + Llama-2-7B, token concatenation) is studied. Architecturally different VLAs — pi0/pi0.5 (flow matching), GR00T N1 (multi-pathway), models using cross-attention fusion, or jointly trained vision encoders — may behave entirely differently. Cross-attention architectures could allow the LLM to selectively attend to action-relevant features without disrupting geometry. The title ("Vision Encoders, Not Language Models, Drive...") makes universal-sounding claims unsupported by single-architecture evidence.

- **All benchmarks within the LIBERO ecosystem.** Same simulator, same robot (Franka Panda), same object sets, same camera setup. LIBERO tasks are known to be largely vision-solvable (Grant 2026) with one task per layout (Hou 2026). The instruction invariance finding (Δ<0.005) may be a LIBERO artifact — tasks where language is genuinely needed to disambiguate goals might show different patterns.

- **Practical implications are speculative without causal validation.** The three design principles in Section 5 ("prioritize vision encoder," "use projector-level features," "mitigate LLM degradation") are sensible hypotheses but not supported by interventional experiments. Recommendation (2) especially requires evidence that projector output can actually drive action prediction comparably.

- **The "degradation" framing may be misleading.** The LLM transforms representations toward its output space — this is expected behavior, not necessarily pathological. The paper does not consider that the LLM may contribute information in dimensions orthogonal to what RSA/CKA capture (e.g., sequential dependencies, multi-step planning, discrete mode selection).

### Missing Related Work

The Related Work section (4 short paragraphs, 8 citations) is thin for a CoRL submission. Key omissions:

1. **Haon et al. (2025)** — "Mechanistic Interpretability for Steering VLAs," accepted at CoRL 2025. First VLA mechanistic interpretability work on OpenVLA in LIBERO. Same venue, same model, same benchmark. Must be cited and differentiated.

2. **Rizzardo et al. (2026)** — "Observing and Controlling Features in VLAs" (arXiv 2603.05487). VLA interpretability on pi0.5 and OpenVLA. Directly relevant.

3. **Lu et al. (2025)** — "Probing a VLA for Symbolic States." Linear probing on OpenVLA hidden layers in LIBERO with >90% accuracy. Methodologically closest prior work — same model, same benchmark, same technique family.

4. **Swann & Buurmeijer (2026)** — "Sparse Autoencoders Reveal Interpretable Features in VLA Models." SAE-based OpenVLA interpretability, concurrent.

5. **Fang et al. (2026)** — "When Vision Overrides Language" (LIBERO-CF). Counterfactual LIBERO benchmark; OpenVLA-OFT 4.7% grounding rate. Supports the instruction invariance narrative with controlled experiments.

6. **Karamcheti et al. (2024)** — "Prismatic VLMs." OpenVLA's architectural foundation; the SigLIP+DINOv2 fusion is relevant context.

7. **Broader frozen-encoder-dominance literature** in VLMs (LLaVA family, etc.) should be discussed to determine if the finding is VLA-specific or a general property of adapter-style multimodal architectures.

### Questions for Authors

1. How does this paper position against Haon et al. (CoRL 2025), which performed mechanistic interpretability on the same model (OpenVLA) in the same benchmark (LIBERO) at the same venue? What does RSA/CKA reveal that activation steering does not?

2. The SigLIP-DINOv2 gap (0.227): is this a finding about VLA architecture or about pretraining recipes? Would CLIP ViT-L show similar RSA to SigLIP, confirming that language-supervised pretraining is the key factor?

3. Do you expect the "LLM degrades action alignment" finding to hold for cross-attention VLAs (e.g., RT-2's PaLI-X backbone) where visual and text tokens interact differently? A brief analysis argument would strengthen generalizability.

4. The instruction invariance finding may be LIBERO-specific. On a benchmark where multiple tasks share a visual scene (requiring language disambiguation), would you expect RSA to differ between real and random instructions?

5. If the LLM is indeed a "representational bottleneck," why does OpenVLA still achieve competitive task success rates? This tension between "LLM degrades representational geometry" and "VLA works in practice" needs more discussion.

---

## Roundtable Synthesis

### Areas of Convergence (Both Reviewers Agree)

1. **The 2×2 factorial design and five-condition instruction control are well-executed.** The convergence of RSA across conditions (σ=0.003 for instructions, Δ<0.01 for training) with proper bootstrap CIs is methodologically sound.

2. **The trained-vs-untrained comparison is the paper's most novel and surprising contribution.** Showing architecture-intrinsic degradation (random-weight LLM ρ=−0.82 vs. trained ρ=−0.88) goes beyond what behavioral studies could reveal.

3. **The absence of causal/interventional experiments is the single biggest weakness.** RSA correlation does not establish that the geometric "degradation" is functionally harmful. A projector-bypass or linear-probe experiment is needed.

4. **Single-architecture scope is a serious limitation that conflicts with the title's generality.** Both reviewers flag that OpenVLA's token-concatenation design may not generalize to cross-attention or multi-pathway VLAs.

5. **LIBERO-only evaluation inflates confidence in instruction invariance.** LIBERO's one-task-per-layout structure makes language unnecessary by design; findings may not generalize to language-critical settings.

6. **The core finding is confirmatory of concurrent work.** Grant (2026), Hou (2026), Fei (2025) reached similar conclusions behaviorally. The representational-level evidence adds precision but not a fundamentally new conclusion.

7. **Related work is incomplete.** At least 5-7 directly relevant papers (Haon 2025, Rizzardo 2026, Lu 2025, Swann 2026, Fang 2026) are absent.

### Areas of Divergence

- **R1 is more concerned about statistical reporting** (monotonicity characterization, aggregation details, reproducibility) while **R2 is more concerned about positioning and novelty** relative to concurrent work.
- **R1 raises specific methodological questions** (token aggregation, subsampling sensitivity, per-layer CIs) while **R2 focuses on conceptual gaps** (does RSA "degradation" imply functional degradation? Is this LIBERO-specific?).
- Both concerns are complementary and valid.

---

## Overall Assessment

### Scores (adapted to CoRL scale)

| Dimension | Score (1-4) | Justification |
|---|---|---|
| **Originality** | 2.5 | First RSA/CKA decomposition of a VLA is novel, but headline finding confirms concurrent behavioral work. Trained-vs-untrained insight is genuinely new. |
| **Quality** | 2.5 | Solid experimental design with proper controls and statistical tests. Undermined by: no causal validation, single architecture, LIBERO-only, missing aggregation/reproducibility details. |
| **Clarity** | 3.5 | Well-written, concise, logically structured. Each table maps to a claim. Minor: Fig.3 referenced as "??" (broken reference). |
| **Significance** | 2.0 | Practical implications are speculative without interventional evidence. Single-architecture findings have limited prescriptive value for the broader VLA community. |
| **Relevance** | 3.5 | Directly relevant to CoRL — understanding VLA internals is timely and important for the robot learning community. |

### Overall Score: **Borderline Reject (2.5/4)**

### Justification

The paper asks an important and timely question — where does action-relevant representational structure reside in a VLA? — and answers it with careful experimental methodology. The 2×2 factorial design, five-condition instruction control, CKA cross-validation, and cross-benchmark consistency demonstrate strong experimental craft. The finding that even random-weight LLMs show similar degradation trajectories is a genuinely novel mechanistic insight.

However, the contribution faces three compounding limitations:

1. **Confirmatory nature**: The headline conclusion ("vision encoder dominates, LLM and instructions don't matter") is already established by multiple concurrent behavioral studies (Grant 2026, Hou 2026, Fei 2025). The representational-level evidence adds quantitative precision but not a fundamentally new conclusion. For CoRL at ~39% acceptance, incremental confirmation is a tough sell.

2. **No causal bridge**: The paper measures representational geometry but never connects it to function. The "degradation" framing assumes that lower RSA alignment means worse action capability, but this is unproven. A single experiment — feeding projector output to a linear action predictor — would either validate or refute the central narrative.

3. **Narrow scope masquerading as general claims**: The title and abstract make sweeping claims ("Vision Encoders, Not Language Models, Drive...") based on one architecture (OpenVLA) in one benchmark ecosystem (LIBERO). The most interesting recent VLAs (pi0, GR00T, cross-attention designs) are architecturally quite different.

### Recommendation for Strengthening

To move from borderline reject to accept, the authors should:
- Add one causal experiment (projector-output bypass or linear probe) to ground the "degradation" claim functionally
- Test on at least one non-LIBERO benchmark to validate instruction invariance
- Engage with the 5-7 missing related works, especially Haon (CoRL 2025) on the same model/benchmark/venue
- Soften the title and abstract to accurately reflect single-architecture scope
- Report token aggregation method, N, DINOv2 variant, and bootstrap parameters for reproducibility

### Confidence: 4/5
Both reviewers have relevant expertise in representational analysis methods and VLA architectures. The assessment is based on careful reading of the full paper and comparison with the planned experimental design.