---
dream_id: dream_20260515T222933
tier: worst
overall_score: 4/10 — Reject
timestamp: 2026-05-15T23:10:52.998847+00:00
---

# Dream Review Report — CoRL 2026 Submission

**Paper:** "The LLM as a Redundant Bottleneck: Representational Analysis of Action Structure in Vision-Language-Action Models"
**Venue:** CoRL 2026 (acceptance rate ~28%, OpenReview 1–10 scale)
**Review mode:** Full (2 Reviewers, 4-step roundtable)
**Dream ID:** 20260515T222933

---

## Venue Calibration

CoRL uses OpenReview with 6 review dimensions (Originality, Quality, Clarity, Significance, Relevance, Limitations) and a 1–10 overall recommendation scale:
- 10: Top 5%, seminal | 9: Top 15%, strong accept | 8: Top 50%, clear accept | 7: Good, accept
- 6: Marginally above threshold | 5: Marginally below threshold
- 4: Not good enough, reject | 3: Clear rejection | 2: Strong rejection | 1: Trivial/wrong

CoRL specifically values: (1) relevance to robot learning, (2) real-world or simulation experiments demonstrating learning, (3) honest limitation reporting.

---

## Paper Summary

The paper performs RSA and CKA representational analysis on an OpenVLA-class VLA (frozen SigLIP-SO400M → linear projector → 32-layer Llama-2-7B LLM), probing representations at every pipeline stage across three LIBERO benchmarks under a 2×2 factorial (trained/untrained × instruction/no-instruction) plus random-instruction and CLIP-ViT controls.

**Five claimed findings:**
1. **Vision-language pretraining dominance:** SigLIP+projector RSA ρ=0.615 > VLA ρ≈0.488. CLIP-ViT (ρ=0.56) attributes 76% of the SigLIP-DINO gap to VL pretraining.
2. **LLM as redundant bottleneck:** Per-layer RSA U-shape (0.59→0.38→0.55), recovery ratio claimed 85%, Spearman monotonicity −0.18.
3. **Instruction: content ignored, noise harmful:** Real vs no-instruction Δ=0.004; random instruction Δ=0.043.
4. **Metric dependency:** CKA reduces SigLIP-vs-VLA gap from Δ=0.127 (RSA) to Δ=0.02.
5. **Cross-benchmark replication:** LIBERO-Goal, Long, Spatial all show consistent ordering.

---

## R1 Review (Methods + Experiments)

### Strengths
- Well-structured 2×2 factorial + random-instruction control cleanly isolates contributions
- Per-layer probing across all 32 LLM layers is genuinely novel for VLAs — no prior work traces action alignment layer-by-layer
- Transparent treatment of CKA-RSA metric dependency as a finding rather than burying it
- CLIP-ViT pretraining control sharpens the recommendation from "use SigLIP" to "use any VL-pretrained encoder"
- Cross-benchmark replication on 3 LIBERO variants strengthens internal validity
- Tables are clear and well-organized (10 tables)

### Weaknesses

**W1-R1 (Major): No behavioral validation.** RSA/CKA measure representational geometry, not task performance. The paper's central implication — "VLA architectures can be substantially simplified" by decoding from projector outputs — is entirely unsupported by success-rate data. A projector-only policy may fail due to mechanisms orthogonal to what RSA captures (temporal coherence, action discretization, sequential decision-making). Without at least one behavioral experiment, the "redundant" claim is restricted to representational structure and the architectural implications are speculative.

**W2-R1 (Major): Single architecture, single scale.** All experiments use one OpenVLA checkpoint (Llama-2-7B, 32 layers). Larger LLMs (13B, 70B) could develop action-specific representations. RT-2, π0, Octo use fundamentally different integration strategies (cross-attention, flow matching, diffusion). The title and framing generalize beyond what the evidence supports.

**W3-R1 (Major): Recovery ratio arithmetic error.** By the paper's own definition — (L32−trough)/(L0−trough) — the result is (0.55−0.38)/(0.59−0.38) = 0.17/0.21 = **0.81 (81%)**, not the claimed 85%. This 4-point discrepancy undermines confidence in quantitative precision throughout.

**W4-R1 (Major): Inadequate statistical testing.** The Δ>0.03 "significance threshold" is never formally justified — no permutation tests, no bootstrap CIs (except a passing mention), no multiple-comparison corrections. Sample sizes for RSA computation (N observations, number of pairwise distances) are never specified. Calling random-instruction Δ=0.043 "significant" based solely on exceeding an ad-hoc threshold is insufficient.

**W5-R1 (Moderate): Linear decomposition assumption.** The 76% pretraining attribution assumes RSA differences are linearly decomposable: (CLIP−DINO)/(SigLIP−DINO). But RSA ρ is a nonlinear rank correlation. The "76%" is an intuitive ratio, not a principled variance decomposition.

**W6-R1 (Moderate): U-shape mechanism hypothesized but not ablated.** Attribution to residual connections and layer normalization is speculation. Ablating skip connections in layers 16–32 would directly test the hypothesis.

**W7-R1 (Minor–Moderate): Zero figures.** The paper's headline finding is a "U-shape" — a fundamentally visual concept — yet contains no figures at all. A line plot of per-layer RSA would be far more compelling than Table 1.

**W8-R1 (Minor): LIBERO-Long missing SigLIP+projector.** Table 7 shows "—" for SigLIP+projector on LIBERO-Long without explanation, weakening the cross-benchmark claim.

### Key Questions
- Q1: What is the sample size N for RSA? How many observations per distance matrix?
- Q2: Recovery ratio 85% vs computed 81% — clarify the exact formula with intermediate precision.
- Q3: Have you trained a projector-only policy and measured success rates?
- Q4: What is the provenance of the Δ>0.03 threshold?
- Q5: Under CKA (Δ=0.02), the LLM is structure-preserving, not a bottleneck. How do you reconcile this with the "redundant bottleneck" framing?

### R1 Scores
| Dimension | Score |
|-----------|-------|
| Soundness | 2/4 |
| Presentation | 2/4 |
| Contribution | 3/4 |
| Overall | **4/10** |
| Confidence | 4/5 |

---

## R2 Review (Novelty + Related Work)

### Strengths
- Component-level representational decomposition is genuinely new for VLAs
- Projector-output as a measurement point before LLM processing is the key methodological contribution
- Per-layer U-shape is informative mechanistic detail beyond behavioral-level findings
- Metric robustness check (RSA + CKA) is methodologically responsible
- Cross-benchmark replication adds confidence
- "Redundant bottleneck" framing is provocative and well-supported by the data

### Weaknesses

**W1-R2 (Major): Severely incomplete related work.** Only ~10 references in 3 short paragraphs. Critical omissions:
- *VLA architectures:* Octo, π0, GR-1, RoboFlamingo, RT-1 — claiming findings about "VLA-class architectures" while studying one requires contextualizing the architectural landscape
- *Representation learning for robotics:* R3M, VIP, MVP, Voltron — directly study which visual representations support robot learning
- *LLM-as-planner/reasoner:* SayCan, Inner Monologue, Code as Policies — demonstrate settings where the LLM IS useful, which the paper ignores
- *Probing/interpretability literature:* Hewitt & Manning 2019, Belinkov 2022, representation engineering — methodological context is thin
- *Concurrent VLA interpretability:* Multiple 2025–2026 papers on VLA analysis are uncited

**W2-R2 (Major): Incremental novelty over behavioral findings.** The three claims map onto what was already established:
- Vision encoder dominance: Grant et al. (2026) showed this across 6 architectures with 394K+ rollouts
- Instruction insensitivity: Hou et al. (2026), Fei et al. (2025), and others all established this
- The representational confirmation tells us "where" at one level of abstraction but does not provide deeper causal mechanisms

The most novel finding (U-shape) is descriptive — we learn the curve exists but not *why* intermediate layers partially recover.

**W3-R2 (Major): Single architecture limits generalizability.** Grant et al. (2026) tested 6 architectures; this paper tests one. The scope is fundamentally narrow for the broad claims made.

**W4-R2 (Major): LIBERO simulation only.** All three benchmarks are within one simulation suite with one robot morphology. LIBERO's known visual shortcuts (one task per layout) could explain why the vision encoder dominates.

**W5-R2 (Major): No proof-of-concept for architectural implications.** Pure diagnostic study with speculative practical suggestions. Even training a small projector-only policy would substantially strengthen the contribution.

**W6-R2 (Moderate): "Untrained" control is near-tautological.** The SigLIP encoder and projector are frozen (identical) in both trained and untrained conditions. Representations *entering* the LLM are literally identical — the finding that "training doesn't change much" is partly built into the design.

**W7-R2 (Moderate): Metric dependency underdeveloped.** CKA showing Δ=0.02 essentially eliminates the bottleneck claim. The paper raises this as an "open question" but never resolves which metric is more appropriate or whether RSA's sensitivity to local geometric distortion is a feature or bug.

### Key Questions
- Q1: Isn't "training invariance" partly tautological given frozen encoder+projector?
- Q2: Full details on CLIP-ViT analysis — preprocessing, resolution, normalization matching?
- Q3: Does noise magnitude (random instruction) correlate with token entropy or sequence length?
- Q4: Have you tested on tasks where the LLM IS demonstrably important (multi-step reasoning, compositional instructions)?
- Q5: What is your power analysis for detecting a "meaningful" training effect?

### R2 Scores
| Dimension | Score |
|-----------|-------|
| Soundness | 3/4 |
| Presentation | 2/4 |
| Contribution | 2/4 |
| Overall | **4/10** |
| Confidence | 4/5 |

---

## Roundtable Discussion

### Step 2: Cross-Sharing

**R1→R2:** R1's identification of the recovery ratio arithmetic error (81% vs 85%) and the ad-hoc Δ>0.03 threshold adds concrete evidence of execution gaps. R2 acknowledges these strengthen the case for lower soundness.

**R2→R1:** R2's point that the "untrained control" is near-tautological (frozen encoder+projector means identical LLM inputs) is well-taken. R1 agrees this weakens the "training invariance" finding — it's partly a design artifact. R2's cataloging of missing related work (Octo, π0, R3M, VIP, SayCan, etc.) also reveals the paper is poorly situated in the broader landscape.

### Step 3: Convergence

Both reviewers converge on the following assessment:

**Agreed strengths:**
- The research question (where does action-relevant structure reside in VLAs?) is timely and important
- Component-level decomposition with per-layer probing is a genuine methodological contribution
- The 2×2 factorial + random instruction + CLIP-ViT controls form a well-designed experimental matrix
- Transparent reporting of metric dependency (CKA vs RSA) is commendable

**Agreed critical gaps (ordered by severity):**
1. **No behavioral validation** — the most damaging omission. "Representationally redundant" ≠ "can be removed." Without success-rate evidence, the architectural implications are speculative.
2. **Single architecture** — OpenVLA-only evidence cannot support claims about "VLA-class architectures."
3. **Statistical rigor** — ad-hoc significance threshold, no formal tests, arithmetic error in recovery ratio.
4. **Thin related work** — 10 references for a 2026 venue paper is inadequate; critical areas of the literature are missing entirely.
5. **No proof-of-concept** — pure analysis without demonstrating that insights lead to improvements.
6. **Simulation-only** — LIBERO's structure may favor vision-dominant solutions.

**Scores converge to:**
- Soundness: 2/4 (R1's stricter assessment absorbs the arithmetic error and missing formal statistics)
- Presentation: 2/4 (both agree; no figures, thin related work)
- Contribution: 2/4 (the question is valuable but incremental over behavioral findings without behavioral validation or proof-of-concept)
- Overall: **4/10** (unanimous)
- Confidence: 4/5

### Step 4: Final Assessment

The paper asks an important question and collects interesting data. The per-layer U-shape, metric dependency, and CLIP pretraining decomposition are genuine contributions to understanding VLA internals. However, the execution falls short of the CoRL acceptance bar in several critical ways:

1. The headline claim ("VLA architectures can be substantially simplified") is unsupported by any behavioral evidence. RSA alignment ≠ task success.
2. Evidence from a single architecture (OpenVLA) cannot support the generality implied by the title and framing.
3. Quantitative rigor is insufficient: arithmetic errors, ad-hoc significance thresholds, no formal statistical tests, missing sample sizes.
4. The related work section is critically underdeveloped for a top venue.
5. The paper is a pure diagnostic study that stops short of demonstrating practical impact — a proof-of-concept (even small-scale) would transform the contribution.

**Recommendation:** Reject. The paper needs (a) behavioral validation via a projector-only policy, (b) at least one additional VLA architecture, (c) formal statistical testing with bootstrap CIs, (d) substantially expanded related work, and (e) figures. With these additions, the core findings could make a solid contribution.

---

## Consolidated Scores

| Dimension | R1 | R2 | Converged |
|-----------|----|----|-----------|
| Soundness | 2/4 | 3/4 | **2/4** |
| Presentation | 2/4 | 2/4 | **2/4** |
| Contribution | 3/4 | 2/4 | **2/4** |
| **Overall** | **4/10** | **4/10** | **4/10** |
| Confidence | 4/5 | 4/5 | **4/5** |

**Overall Recommendation: 4/10 — Reject**

---

## Actionable Revision Checklist

| Priority | Item | Effort |
|----------|------|--------|
| P0 | Add behavioral validation: train projector-only policy, compare success rates vs full VLA | High |
| P0 | Formal statistical testing: permutation tests or bootstrap CIs for all RSA/CKA comparisons; report N | Medium |
| P0 | Fix recovery ratio arithmetic (81% not 85%); audit all reported numbers | Low |
| P1 | Test on ≥1 additional VLA architecture (e.g., RT-2, Octo, or π0) | High |
| P1 | Expand related work to ≥25 references covering VLA architectures, representation learning for robotics, LLM-as-planner, probing/interpretability | Medium |
| P1 | Add 3–4 figures: per-layer RSA line plot (U-shape), instruction comparison bars, CKA-RSA scatter, cross-benchmark panels | Medium |
| P2 | Ablate residual connections to test U-shape mechanism hypothesis | High |
| P2 | Justify or replace the ad-hoc Δ>0.03 significance threshold | Low |
| P2 | Fill LIBERO-Long SigLIP+projector entry in Table 7 | Low |
| P2 | Discuss when LLM IS useful (multi-step reasoning, compositional generalization) to scope the "redundant" claim | Low |

---

## Experiment Coverage Assessment

| Planned Experiment | In Paper? | Quality |
|-------------------|-----------|---------|
| Per-layer RSA curve (plan_003) | ✓ Table 1–2 | Arithmetic error in recovery ratio; no formal stats; no figures |
| Random instruction control (plan_008) | ✓ Table 3–4 | Ad-hoc significance threshold; mechanism speculation unverified |
| CKA verification (plan_009) | ✓ Table 5–6 | Metric dependency raised but not resolved |
| LIBERO-Spatial cross-benchmark (plan_010) | ✓ Table 7–8 | LIBERO-Long SigLIP entry missing; claims of "full replication" overstated |
| CLIP-ViT baseline (blocking) | ✓ Table 9–10 | Linear decomposition assumption questionable; useful but overinterpreted |

All 5 planned/blocking experiments are present. Coverage is complete but execution quality has gaps across all experiments.
