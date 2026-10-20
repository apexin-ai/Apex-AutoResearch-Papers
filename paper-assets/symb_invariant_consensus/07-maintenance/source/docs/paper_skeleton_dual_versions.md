# Paper Skeleton — Dual Version Draft
# Date: 2026-05-20
# Status: For Director review

---

## 1. Titles + Abstracts (150w each)

### Version 1: Selective Symbolic Verification (Negative-first + diagnostic)

**Title**: "Selective Symbolic Verification: When (and Why Not) to Trust Symbolic Constraints in LLM Reasoning"

**Abstract (148w)**:
Self-Consistency (SC) voting over chain-of-thought traces saturates due to trace correlation. Symbolic constraint extraction via first-order logic (FOL) appears to offer structured aggregation beyond majority voting. We evaluate this through Symbolic Invariant Consensus Aggregation (SICA) across six models (7B--32B) on three reasoning domains (N>3,000) and find that self-extracted constraints exhibit systematic confirmation bias: on incorrect problems, 83.3% of constraints support the wrong majority answer (bias ratio 4.97x), and 94% of errors overlap with SC. Process-level analysis reveals deeper homogeneity: chain-of-thought cosine similarity (0.69) far exceeds answer-level Fleiss' kappa (0.41). More than twenty remediation strategies all fail, revealing a fundamental independence-accuracy trade-off. Oracle controls confirm the mechanism is sound (+14.22pp with gold FOL). We provide regime diagnostics predicting when symbolic verification adds value versus amplifies errors.

**Narrative spine**: SC plateau → self-extraction hypothesis → confirmation bias discovery → independence-accuracy trade-off → regime diagnostics → when (not) to trust

---

### Version 2: Cross-Architecture Verification (Negative + positive solution)

**Title**: "Breaking Symbolic Confirmation Bias via Cross-Architecture Verification"

**Abstract (152w)**:
Self-extracted symbolic constraints in LLM reasoning exhibit confirmation bias: on incorrect problems, 83.3% of FOL constraints support the wrong majority answer (bias ratio 4.97x). We trace this to the independence bottleneck — same-model traces produce correlated constraints (Fleiss' kappa=0.21-0.82, Effective-K=1.20-3.62 at K=12), and more than twenty same-model remediation strategies fail to break this ceiling. To overcome confirmation bias, we introduce cross-architecture verification: a [DeBERTa-based NLI / external verifier] provides independent constraint validation from outside the reasoning model's distribution. **[PLACEHOLDER: R results — delta on FOLIO/PW/LogiQA, McNemar p-values, oracle gap bridged %]**. Our analysis reveals a fundamental independence-accuracy trade-off governing same-model aggregation, while cross-architecture verification demonstrates that external signal — not better prompting or sampling — is the path to reliable symbolic reasoning augmentation.

**Narrative spine**: Confirmation bias discovery → independence bottleneck quantification → 22+ failures → cross-architecture breaks it → theoretical explanation via CJT

---

## 2. Contributions List (4 + 1 placeholder)

### Shared Contributions (both versions):

**C1. Independence Bottleneck Quantification.**
Fleiss' kappa / Effective-K framework applied to LLM trace aggregation. kappa=0.21-0.82 across 15 conditions, 3 model families (Mistral, LLaMA, Qwen) all exhibit kappa >= 0.41. Pareto frontier: SC/DP/ICG cluster at kappa~0.40-0.47; Debate kappa=0.15 but -18.6pp.

**C2. Symbolic Confirmation Bias.**
New phenomenon: self-extracted constraints systematically confirm majority answer. Bias ratio 4.97x on incorrect problems; 94% SICA errors overlap SC. Causal chain: model→answer→FOL→aggregation ≈ weighted majority vote. CEGIS and cross-model extraction cannot break it.

**C3. Comprehensive Failure Mode Taxonomy.**
22+ interventions (9 prompt, 3 method, 10+ additional) across 6 dimensions all fail. Three regimes (Type A: confirmation bias SC>=60%, Type C: error amplification SC<=40%, intermediate: narrow ~50-55%). Entropy decomposition: all effects in high-entropy, direction regime-dependent.

**C4. Process-Level Independence Metric.**
CoT cosine similarity (0.69) >> answer-level kappa (0.41), r=-0.06 (uncorrelated). 9.3% convergent pairs. Establishes tighter bound on effective ensemble diversity.

### Version-Specific Contribution:

**C5v1 (Selective). Regime Diagnostics.**
C0 + SC accuracy = zero-cost deployment diagnostic. C0<5% → degenerate; SC>=60% → confirmation bias; SC<=40% → error amplification. Eff-K quantifies SC's own scaling ceiling.

**C5v2 (Cross-Architecture). Cross-Architecture Verification.**
[PLACEHOLDER] DeBERTa NLI / external verifier breaks confirmation bias by providing independent signal. Bridges X% of oracle gap. First demonstration that architecture diversity, not prompt/method diversity, is the key axis.

---

## 3. Section Outline (key message per section)

### §1 Introduction (1.3pp)
- **V1**: SC saturates → self-extraction as zero-cost solution → confirmation bias blocks it → independence-accuracy trade-off is fundamental → regime diagnostics enable selective deployment
- **V2**: SC saturates → self-extraction fails due to confirmation bias → cross-architecture verification breaks the bottleneck → trade-off only applies within same-model paradigm

### §2 Related Work (0.7pp)
- SC & extensions: plateau well-documented (Loo 2025), variants all same-model
- Neuro-symbolic: Logic-LM/LINC/DyLoS/Aristotle/FoVer all use external components — we test self-extraction
- CJT/voting theory: Condorcet, Ladha correlated voters, Lefort LLM ensembles
- Verification: ORM/PRM trained verifiers; self-correction fails (Huang 2024)
- **[V2 adds]**: NLI as verifier (DeBERTa-mnli, cross-encoder NLI, NLI for fact verification)
- **[V2 adds]**: Calibration & selective prediction (confidence calibration in LLMs)

### §3 Method (1.2pp)
- §3.1 SC + Condorcet framework (Eff-K formula)
- §3.2 SICA pipeline (trace→extract→dedup→MAX-SAT→score)
- §3.3 Oracle control design
- §3.4 Process-level independence (cosine similarity metric)
- §3.5 Scope: same-model self-extraction, 22+ remediations
- **[V2 adds]** §3.6 Cross-architecture verification (DeBERTa NLI as constraint validator)

### §4 Experiments (1.5pp)
- §4.1 Setup: 6 models, 3 domains, K=12, T=0.7, McNemar test
- §4.2 Main results: Table 1 (18 conditions), regime pattern, Figure 2 (scatter)
- §4.3 Oracle control: +14.22pp FOLIO, +11.50pp PW, 24% utilization
- §4.4 Four-seed replication (compressed)
- **[V2 adds]** §4.5 Cross-architecture results: [PLACEHOLDER Table 4]

### §5 Analysis (1.7pp) — CORE SECTION
- §5.1 Condorcet Effective-K: Table 3 (15 conditions), cross-model universality
- §5.2 Symbolic Confirmation Bias: bias ratio, error overlap, causal chain
- §5.3 Process-Level Independence: cosine >> kappa, uncorrelated, convergent pairs
- §5.4 Supporting Diagnostics (compressed → appendix)
- §5.5 Remediation: 22+ interventions, independence-accuracy trade-off, Pareto frontier
- **[V2 adds]** §5.6 Why cross-architecture works: CJT analysis, independence gain

### §6 Discussion (0.4pp)
- **V1**: Confirmation bias as unifying root cause; process-κ implications; practitioner diagnostics; scope limitations
- **V2**: Same-model bottleneck is fundamental; cross-architecture breaks it because external model has different inductive biases; implications for neuro-symbolic systems

### §7 Conclusion (0.25pp)
- **V1**: Negative result + diagnostic tools + three paths forward
- **V2**: From negative to positive: understanding the bottleneck enabled the solution

---

## 4. Key Results Tables

### Table 1: Independence Metrics (existing — no change)
κ, Eff-K across 15 conditions. Shows architecture-independent ceiling.
Data: registry (exp-026, exp-033, exp-052, exp-053, exp-067, exp-046, exp-049, exp-055, exp-057, exp-058, exp-054, exp-028b)

### Table 2: Comprehensive Interventions Summary (NEW for main text or appendix)
| Category | Count | Representative | Best Δ | Worst Δ |
|----------|-------|---------------|--------|---------|
| Prompt-level | 9 | Contrastive, cross-model, multi-T | +0.98pp | -1.47pp |
| Method-level | 3 | ICG, Contrastive scoring, Debate | +1.47pp | -23.00pp |
| Additional | 10 | PROVE, CEGIS, DeepConf, perturbation, MIN-UNSAT, κ-aware, Z3 filter, bootstrap, ASCII, cross-model SICA | -0.49pp | -6.5pp |
| **Total** | **22** | | **All neutral or negative** | |

### Table 3: Entropy Decomposition (appendix or inline)
High-E vs Low-E Δpp by regime. 8 conditions, 3 regimes clearly separated.
Data: registry (exp-033 seeds, exp-046, exp-036, exp-038, exp-035, exp-048)

### Table 4: [PLACEHOLDER] Cross-Architecture Results (V2 only)
| Method | FOLIO Δ | PW Δ | LogiQA Δ | p |
|--------|---------|------|----------|---|
| SC baseline | 0 | 0 | 0 | — |
| SICA (self) | +X | +X | +X | — |
| SICA + DeBERTa NLI | [R results] | [R results] | [R results] | [R results] |
| Oracle | +14.22 | +11.50 | — | <0.001 |

---

## 5. Figure Checklist

### Fig 1: Confirmation Bias Causal Chain / Pipeline (conceptual)
- Type: TikZ / PaperBanana conceptual diagram
- Key message: model→answer→FOL→Z3 = weighted majority vote. Self-extraction loop highlighted in red.
- Placement: §3 Method
- Status: EXISTS (pipeline diagram), needs update to highlight confirmation bias loop

### Fig 2: Regime Scatter (SC baseline vs SICA Δ)
- Type: Scatter plot (matplotlib)
- Key message: narrow intermediate-SC zone; outside = neutral/harmful
- Placement: §4 Experiments
- Status: EXISTS (f2_regime_scatter), keep as-is

### Fig 3: Oracle Gap / Independence-Accuracy Pareto
- Type: Scatter or bar chart
- Key message: Self-extraction captures 24% of oracle ceiling; Pareto frontier of κ vs accuracy
- Placement: §5 Analysis or Appendix
- Status: EXISTS (kappa-accuracy Pareto in appendix). Consider: merge oracle gap visualization with Pareto into one figure?

### Fig 4: [PLACEHOLDER] Cross-Architecture Results (V2 only)
- Type: Bar chart or scatter
- Key message: Cross-architecture verification bridges oracle gap
- Placement: §4 or §5
- Status: PENDING R results

---

## 6. Version Comparison Summary

| Dimension | V1 (Selective) | V2 (Cross-Architecture) |
|-----------|---------------|------------------------|
| Tone | Diagnostic / analytical | Problem → solution |
| Core narrative | When not to trust | How to break the bottleneck |
| Positive contribution | Regime diagnostics | Cross-arch verification |
| Risk | "Just a negative result" | R results may not deliver |
| Reviewer appeal | Strong analysis, weak action | Action + analysis |
| Dependency on R | None | **Critical** |
| Ready to write | YES (all data available) | BLOCKED on R results |
| EMNLP fit | Analysis papers accepted | Stronger if R works |

**Recommendation (non-binding)**: V1 is shippable now. V2 is strictly better IF R delivers significant positive results. Suggest: finalize V1 as insurance, switch to V2 only when R confirms.
