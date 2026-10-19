---
dream_id: dream_20260516T194646
tier: worst
overall_score: weak reject
timestamp: 2026-05-16T20:23:28.591894+00:00
---

# Dream Review Report

**Paper:** Architecture Determines Safety Monitoring Strategy: Hidden-State Detection in Reasoning Models Reveals Two Distinct Regimes

**Review Mode:** Full (2 Reviewers + Roundtable)

**Overall Score:** 3/6 (Weak Reject)

---

## Paper Summary

The paper presents a cross-architecture evaluation of hidden-state safety monitoring for reasoning models exhibiting "self-jailbreak" behavior. Testing across 4 models in 2 architecture families (Llama-3.1, Qwen2.5) at 2 scales (7–8B, 32B), it claims to identify two monitoring regimes: a "distributed-signal" regime (Llama, requiring temporal context for +30.2pp improvement) and a "concentrated-signal" regime (Qwen2.5, where static probes achieve 70%+ coverage). The paper proposes a diagnostic framework using PCA variance concentration and Fisher discriminant ratio, demonstrates cross-architecture transfer failure, and shows architecture-dependent lead time behavior. 12 experiments are reported across 8 pages.

---

## R1 Review: Methods & Experiments

**Soundness: 2/5 | Overall: 3/6 | Confidence: 4/5**

### Strengths

- **S1: Comprehensive experiment matrix.** All 12 planned experiments are executed, covering ablations (window size, layer selection), baselines (Mahalanobis, GRU), transfer, and statistical validation.
- **S2: Appropriate bootstrap CI usage.** The authors correctly identify that the temporal advantage for Qwen crosses zero and refrain from overclaiming. The honesty about non-significant results (Table 4) is commendable.
- **S3: Actionable diagnostic framework.** PCA variance concentration threshold (>30%) paired with Fisher ratio gives practitioners a concrete decision procedure.
- **S4: Well-designed cross-transfer experiment.** Testing both directions plus within-family transfer provides clean evidence that probes are architecture-specific.

### Weaknesses

- **W1: Critically small test set (n=43).** Each coverage percentage point corresponds to <0.5 traces. Bootstrap CIs of [+19, +42] for Llama temporal delta span 23pp — insufficient precision for title-level claims about "two distinct regimes." The 209-trace training set is similarly small for temporal features (W=15 → ~77K parameters).
- **W2: Architecture vs. training procedure confound.** Llama-3.1 and Qwen2.5 differ in training data, RLHF procedure, tokenizer, and safety training — not just architecture. The OpenThinker-7B control shares Qwen2.5 architecture AND pre-training, so it does not isolate architecture from training. The title claim "architecture determines" is unsupported without same-architecture-different-training controls.
- **W3: Coverage metric poorly motivated.** ±3 steps tolerance is never justified. No sensitivity analysis at different thresholds (±1, ±2, ±5). Step duration in tokens is unreported. "Coverage" conflates detection rate with precision — no false positive analysis whatsoever. A probe that fires everywhere achieves 100% coverage.
- **W4: No false positive analysis.** The paper never reports FPR on safe traces or non-commitment locations in unsafe traces. Without this, practical utility is unknowable.
- **W5: Single dataset (HarmThoughts).** All traces come from one dataset with one "self-jailbreak" definition. Different harmful content categories or elicitation strategies could change the signal structure entirely.
- **W6: Missing standard baselines.** No comparison to token-level text classifiers on CoT, attention-pattern based detection, or simple hidden-state norm thresholds. Cannot assess whether hidden-state probing is necessary vs. cheaper text monitoring.

### Key Questions

- Q1: How are commitment points annotated? What is inter-annotator agreement? ±3 tolerance is meaningless without knowing annotation noise.
- Q2: What is the FPR when running probes on full traces, including safe/benign traces?
- Q3: The 2×2 matrix is imbalanced (3 Qwen, 1 Llama). Why no Llama-32B model?
- Q4: GRU = temporal LR exactly — does this mean temporal patterns are purely linear? If so, this deserves more discussion.

---

## R2 Review: Novelty & Related Work

**Novelty: 2/5 | Overall: 3/6 | Confidence: 4/5**

### Strengths

- **S1: Clean conceptual abstraction.** The distributed/concentrated two-regime framing, if it generalizes, would give practitioners an actionable decision procedure.
- **S2: Good scale control.** OpenThinker-7B inclusion to disentangle architecture from scale is sound experimental design.
- **S3: Practical transfer failure documentation.** Cross-architecture transfer failure (25–33%) with CIs has deployment value — warns against naive probe reuse.

### Weaknesses

- **W1: Core claim built on n=2 architecture families.** "Architecture determines monitoring strategy" is stated as general principle, but evidence supports only "Llama-3.1 and Qwen2.5 differ." With two data points on the independent variable, "two distinct regimes" risks severe overfitting. Missing: Mistral, Gemma, Phi, Yi, or any third family.
- **W2: Alarmingly thin related work (7 references, all Anonymous 2025).** Critical missing bodies of work:
  - *Probing literature*: Alain & Bengio (2017), Belinkov (2022) survey, Hewitt & Manning (2019), Burns et al. (2023) "Discovering Latent Knowledge," Li et al. (2024) "Inference-Time Intervention"
  - *Representation geometry*: Park et al. (2024) geometry of truth, Marks & Tegmark (2023) representation engineering
  - *Mechanistic interpretability*: Elhage et al. (2022) superposition, Bricken et al. (2023) monosemanticity
  - *Safety probing*: Zou et al. (2023) "Representation Engineering," Arditi et al. (2024) "Refusal Is Mediated by a Single Direction" — the latter directly complicates the "distributed signal" finding for Llama
- **W3: Limited novelty.** Different model families learning different internal representations is well-established. The finding that Qwen2.5 concentrates while Llama distributes could reflect RLHF/safety training differences rather than architecture. The two-regime characterization is observational, not explanatory.
- **W4: Non-standard evaluation metric.** ±3 step coverage is not comparable to standard detection metrics (AUROC, F1, precision-recall curves), hindering comparison to prior work and raising questions about metric selection bias.

### Key Questions

- Q1: Arditi et al. (2024) showed refusal in Llama-family models is mediated by a single direction. How does this reconcile with your "distributed signal" finding? Is the difference because you study commitment points rather than refusal per se?
- Q2: How do you disentangle "architecture" from "safety training procedure"? Could the regime difference be entirely explained by how safety was trained into each model?
- Q3: With 43 test traces, what is the statistical power to detect a meaningful difference between 70% and 75% coverage?

---

## Roundtable Synthesis

### Convergence Points (Both Reviewers Agree)

1. **Architecture-vs-training confound is the most critical flaw.** The title claim "architecture determines" is not supported because architecture and training procedure are perfectly confounded in this study. Neither the OpenThinker-7B control nor any other experiment isolates architecture from training. This is a fatal threat to the paper's central thesis.

2. **n=43 test traces are insufficient for the strength of claims.** Wide bootstrap CIs (23pp span for the flagship result) and per-trace granularity (<0.5 traces per coverage point) make quantitative comparisons unreliable. The paper acknowledges this but does not temper its claims accordingly.

3. **n=2 architecture families cannot support a "general regime" taxonomy.** Two data points on the independent variable (architecture family) cannot establish a general principle. The "two distinct regimes" framing overfits to this specific comparison.

4. **Missing false positive analysis undermines practical claims.** Coverage alone cannot assess monitoring utility. Without FPR on safe traces and non-commitment regions, deployment recommendations are premature.

5. **Related work gaps are severe.** 7 anonymous references is inadequate. The paper ignores foundational probing literature, representation geometry work, and directly relevant safety probing findings (Arditi et al.) that may contradict its claims.

### Disagreement Resolution

No substantive disagreements between reviewers. R1 emphasizes missing baselines (text classifiers) and FPR; R2 emphasizes literature gaps and the Arditi et al. tension. Both concerns are valid and complementary.

### Final Assessment

**Overall Score: 3/6 (Weak Reject)**

The paper asks a timely and relevant question — whether safety monitoring strategies should be architecture-specific — and provides systematic experiments. The diagnostic framework (PCA variance + Fisher ratio) is a practical contribution. However, the evidence base is insufficient to support the broad claims:

- The core confound (architecture vs. training) is unresolved
- The sample size (43 test traces) cannot support the precision of claims made
- Two architecture families cannot establish a general taxonomy
- Missing FPR analysis makes deployment recommendations premature
- Related work coverage has severe gaps in probing, representation engineering, and mechanistic interpretability literature

**Path to acceptance:** (1) Add ≥1 additional architecture family (Mistral/Gemma); (2) Include false positive analysis; (3) Add text-based baseline comparisons; (4) Substantially expand related work, especially probing literature and Arditi et al.; (5) Retitle to avoid claiming general principles from n=2 observations; (6) If possible, control for training procedure vs. architecture.

### Experiment Coverage

All 12 planned experiments from the design document are present in the paper:
- exp-001 through exp-012: ✓ All covered (Tables 1–12)

The paper is thorough in executing the planned experiments but the fundamental design limitations (small n, 2 families, confounded variables) cannot be overcome by adding more experiments within the same setup.
