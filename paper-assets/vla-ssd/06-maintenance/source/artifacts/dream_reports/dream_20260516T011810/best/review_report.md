---
dream_id: dream_20260516T011810
tier: best
overall_score: weak accept
timestamp: 2026-05-16T01:46:41.482834+00:00
---

# Dream Review Report: "Where Do Actions Come From?"

**dream_id:** 20260516T011810 | **review_mode:** full | **reviewers:** R1 (Methods+Experiments), R2 (Novelty+Related Work)

---

## Consolidated Assessment

| Dimension | R1 | R2 | Consensus |
|---|---|---|---|
| Overall Score | 4 (Weak Accept) | 4 (Weak Accept) | **4 (Weak Accept)** |
| Confidence | 4/5 | 4/5 | 4/5 |

**One-line verdict:** A methodologically rigorous empirical analysis with one genuinely novel finding (geometric–functional dissociation) but limited by single-architecture scope, partially confirmatory nature relative to concurrent work, and weak evidence for the boldest claim (Claim 3).

---

## Summary of the Paper

The paper decomposes the representational structure of OpenVLA into contributions from the frozen vision encoder (SigLIP), learned projector, and fine-tuned LLM backbone. Using RSA, CKA, and functional action probes across two LIBERO benchmarks and three standalone vision encoders (SigLIP, CLIP ViT-L, DINOv2), it establishes three findings:

1. **VL-pretrained encoder dominance:** SigLIP+Projector achieves highest RSA with action structure (ρ=0.615); CLIP ViT-L is statistically indistinguishable (ρ=0.553, p=0.08); DINO significantly lower (ρ=0.388). Yet all encoders carry comparable action information (R²≈0.70).
2. **LLM redistributes, training-dependently:** RSA degrades from projector to LLM image tokens (0.615→0.501), but trained readout token exceeds the projector (R²=0.731 vs 0.706). Untrained readout cannot achieve this (R²=0.686).
3. **Training routes, not creates:** Distributed RSA is training-invariant (0.501 vs 0.485, p=0.20) while readout concentration is training-dependent (ΔR²=0.045, p<0.0001). Language instructions affect neither.

All findings reportedly replicate on LIBERO-Spatial (cross-benchmark ratios 0.95–0.97).

---

## Strengths

### S1. Geometric–Functional Dissociation (Both Reviewers — Major Strength)
The most genuinely novel finding. DINO achieves action probe R² comparable to SigLIP+Projector (0.712 vs 0.706, p=0.22) yet has vastly lower RSA (0.388 vs 0.615). This clean separation between "information presence" and "geometric alignment with action structure" has not been explicitly demonstrated in the VLA domain. It reframes the role of VL pretraining as contributing geometric organization, not information content — a conceptually crisp and practically relevant insight.

### S2. Rigorous Experimental Design (R1)
The 2×2 factorial design ({trained, untrained} × {with, no instruction}) with additional random/shuffled/empty instruction controls is thorough. The untrained control (reinitializing LLM weights while preserving frozen encoder+projector) cleanly isolates the LLM's contribution. Bootstrap CIs (10,000 resamples) and permutation-based p-values are appropriate for the non-parametric comparisons.

### S3. Complementary Metrics (Both Reviewers)
The RSA–CKA–probe troika captures distinct aspects of representation structure (local geometry, global structure, functional information). The CKA–RSA dissociation (ordering reversal) is intellectually honest and adds depth: the LLM degrades local distance alignment while preserving or improving global structural correspondence.

### S4. CLIP Pretraining Control (R1)
The CLIP ViT-L/14 control experiment effectively generalizes Claim 1 from "SigLIP dominance" to "VL-pretrained encoder dominance," establishing a three-tier structure: VL-pretrained (ρ∼0.55–0.62) >> VLA backbone (ρ∼0.50) >> self-supervised (ρ∼0.39).

### S5. Clear Practical Implications (R2)
The paper provides representational-level grounding for the emerging practical consensus that vision encoder quality matters more than LLM scale for VLA performance.

---

## Weaknesses

### W1. Single Architecture, Single Model Scale (Both — Major)
All claims are established on OpenVLA-7B only. The paper title ("Vision-Language-Action Models" plural) overclaims relative to evidence from one model. Modern VLAs differ architecturally: pi0/pi0.5 use flow matching with separate expert pathways, Octo uses diffusion-based action heads, RT-2-X uses different scales. The "vision encoder dominance" may not hold for architectures where the action pathway is structurally separated from the VLM pathway. Testing even one additional architecture (Octo is open-source) would substantially strengthen the claims.

**Recommendation:** Scope claims precisely to "OpenVLA-class autoregressive VLAs" or test at least one additional architecture.

### W2. Extreme "Untrained" Control (R2 — Major)
The "untrained" model uses a randomly-initialized LLM, not a base pretrained Llama-2. This is an extreme comparison that conflates "VLA fine-tuning effect" with "language pretraining + VLA fine-tuning effect." The frozen encoder+projector dominate input regardless of LLM state, so similar early-layer representations are expected by construction. A comparison with the base pretrained Llama-2 (language-only, no action fine-tuning) would be far more informative for the "routing not creating" claim.

**Impact on claims:** Makes the "training invariance" finding (Claim 3) less surprising than presented. The null result may reflect projector-bottleneck constraints rather than a deep principle about fine-tuning.

### W3. Claim 3 Rests on a Null Result Without Equivalence Testing (Both — Major)
The claim "training does not change distributed representation structure" relies on non-significance (p=0.20) with n=10 tasks and observed Δ=0.016. Statistical power to detect a true small effect is very low. Absence of evidence ≠ evidence of absence. The paper should report a Two One-Sided Tests (TOST) equivalence procedure with a pre-specified margin (e.g., Δ < 0.05) to affirmatively establish equivalence.

### W4. Partially Confirmatory of Concurrent Work (R2 — Moderate)
Grant et al. (2026) already established "visual pathway dominates" and "language encoded but not used" across 6 VLA architectures with real-world deployment. This paper confirms the same finding at a representational level but the incremental novelty beyond Grant's conclusions is limited to the geometric–functional dissociation. The paper should more explicitly position its unique contribution relative to Grant et al.

### W5. OOD Confound (R1 — Moderate)
The trained model was fine-tuned on LIBERO-10 but analyzed on LIBERO-Goal (out-of-distribution). The "training does not change representations" could alternatively be interpreted as "training on LIBERO-10 does not transfer to LIBERO-Goal representations." Analyzing on in-distribution data (LIBERO-10 itself) would control for this confound.

### W6. Language Instruction Null Result Is Trivially Expected (R2 — Moderate)
In LIBERO, each scene uniquely determines the task, making instructions redundant. The model learned to ignore instructions because they were uninformative in training. This is not evidence that VLAs generally cannot use language — it is evidence specific to this benchmark's design. The paper should acknowledge this more explicitly.

### W7. Missing Related Work Connections (R2 — Moderate)
Key missing references:
- **Aghajanyan et al. (2021)** "Intrinsic Dimensionality" — fine-tuning operates in a low-dimensional subspace, a precursor to "routing not creating."
- **Voita et al. (2019)** on attention head pruning and information routing — directly relevant to the "routing" claim.
- **Huh et al. (2024)** "Platonic Representation Hypothesis" — representation convergence across modalities, relevant to why DINO and SigLIP have similar R².
- **Hewitt & Manning (2019)** — probe complexity concerns the authors themselves identified but never formally addressed.
- Broader probing literature in NLP (Belinkov & Glass 2019 survey).

### W8. No Probe Complexity Ablation (R1 — Minor)
The MLP probe (Linear-ReLU-Linear, 256 hidden units) is a specific capacity choice. A linear probe baseline would clarify whether differences reflect information content or probe overfitting. This concern (Hewitt & Manning 2019) was identified during development but not addressed in the paper.

### W9. Cross-Benchmark Replication Limitations (Both — Minor)
LIBERO-Spatial and LIBERO-Goal share the same simulator, visual style, and related task structures. True generalization claims would require a different simulator or real-world data. The "cross-benchmark ratios 0.95–0.97" may reflect benchmark similarity rather than finding robustness.

### W10. Copy Baseline and Autocorrelation (R1 — Minor)
A copy baseline (a_{t+1} = a_t) achieves R²=0.97 due to trajectory smoothness, compressing the meaningful signal range. The absolute R² values (~0.70) may be substantially inflated by temporal autocorrelation. The meaningful differences (0.03–0.05 range) are small in absolute terms.

---

## Questions for Authors

**Q1 (R1, Critical):** Were the LIBERO-Spatial results (Tables 4–7) actually computed from executed experiments? If so, through which experiment run?

**Q2 (Both, Major):** Have you considered running a TOST equivalence procedure for Claim 3, to affirmatively establish equivalence within a pre-specified margin rather than relying on non-significance?

**Q3 (R2, Major):** What does the RSA look like for a base Llama-2 pretrained model (not fine-tuned for actions, not randomly initialized)? This would isolate the contribution of VLA fine-tuning from language pretraining.

**Q4 (R1):** What is the R² of a linear probe (no hidden layer) at the projector and best LLM layer? This would address the Hewitt & Manning (2019) concern.

**Q5 (R1):** Would the trained model show different results if analyzed on LIBERO-10 (in-distribution) rather than LIBERO-Goal (OOD)?

**Q6 (R2):** The CKA ordering reversal (untrained > trained > projector) is described but not adequately explained. Why would an untrained LLM have higher CKA with action structure than a trained one?

**Q7 (R1):** How sensitive are RSA results to the dissimilarity metric choice (cosine vs Euclidean vs correlation distance)?

**Q8 (R2):** For the CLIP control: was the comparison controlled for representation dimensionality? CLIP and SigLIP have different embedding spaces.

---

## Experiment Coverage Assessment

| Planned Experiment | Covered in Paper? | Assessment |
|---|---|---|
| CLIP-ViT Pretraining Control (plan_012) | Yes — Tables 1–2 | Fully covered, results match expected values |
| LIBERO-Spatial Cross-Benchmark (plan_010) | Yes — Tables 4–7 | Results reported but execution status unclear from project infrastructure |

Both planned experiments appear in the paper. The CLIP control is convincing. The LIBERO-Spatial replication, if executed, provides useful (though limited) cross-benchmark validation.

---

## Suggestions for Improvement

1. **Add one additional VLA architecture** (e.g., Octo) to justify claims about "VLAs" generally.
2. **Include base pretrained Llama-2 control** (language-pretrained, not action-fine-tuned) to isolate VLA fine-tuning effects from the extreme random-vs-trained comparison.
3. **Report TOST equivalence test** for Claim 3 with pre-specified margin.
4. **Add linear probe baseline** alongside MLP probes.
5. **Expand related work** to connect with the broader fine-tuning / probing literature in NLP.
6. **Discuss LIBERO instruction redundancy** as a limitation of the language instruction null finding.
7. **Provide CKA ordering reversal explanation** or flag it as an open question requiring future investigation.

---

## Final Scores

| Criterion | Score |
|---|---|
| Novelty | 3.5/6 — One novel finding (geometric–functional dissociation); "routing" framing is a repackaging of known dynamics |
| Soundness | 4.5/6 — Rigorous methods and statistics, but Claim 3 rests on underpowered null result |
| Significance | 3.5/6 — Partially confirmatory of concurrent work; practical implications are incremental |
| Clarity | 4.5/6 — Well-organized, clear tables, logical structure |
| **Overall** | **4 (Weak Accept)** |
| Confidence | 4/5 |

**Justification:** The paper presents a systematic and methodologically careful representational analysis with one genuinely novel insight (geometric–functional dissociation between RSA and probe R² across encoder types). The experimental design with multiple controls is commendable. However, the single-architecture scope, partially confirmatory nature relative to Grant et al. (2026), the weak evidence for the boldest claim (Claim 3 relying on an underpowered null result with an extreme control), and missing connections to the broader fine-tuning literature prevent a stronger recommendation. The contribution is above the reject threshold but needs additional architecture testing and stronger equivalence evidence to reach clear Accept at a top venue.
