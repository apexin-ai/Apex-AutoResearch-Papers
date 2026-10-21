# Literature Survey: Domain-Dependent Contamination Effects

## Context (D108 Finding)

MMLU domain-level γ analysis (N=24 respondents, 2PL+γ) reveals:
- STEM domains (Math, Science): γ > 0 (contamination boosts performance)
- Humanities/Social Sciences/Medical: γ < 0 (contamination degrades performance)
- Contradicts the prevailing assumption that contamination uniformly inflates scores
- Manifestation of Simpson's paradox: aggregate γ may mask opposing domain-level effects

---

## 1. Domain-Level Contamination Effects — Direction Differences

### 1.1 Reddy & Karmakar (2026) — "Are Large Language Models Truly Smarter Than Humans?"
- **Venue:** arXiv (cs.AI), March 2026
- **Finding:** Contamination *rates* vary by domain: STEM (18.1%) > Professional (12.7%) > Social Sciences (12.1%) > Humanities (10.3%). Law & Ethics show 19.8pp accuracy drops under paraphrasing. Most contaminated subjects: Philosophy (66.7%), Anatomy (55.6%), Electrical Engineering (44.4%).
- **Gap:** Reports differential contamination *rates* and *vulnerability*, but assumes contamination always *inflates* scores. Does NOT report negative effect direction.

### 1.2 Hidayat et al. (2025) — "Simulating Training Data Leakage in Multiple-Choice Benchmarks"
- **Venue:** arXiv, 2025
- **Finding:** Domain-specific contamination effects: Anatomy (35.4% drop when leaked items removed), STEM up to 8% reduction. Knowledge-heavy subjects more affected than reasoning-focused domains.
- **Gap:** All reported effects are positive (contamination helps). No negative direction reported.

### 1.3 Jiang et al. (2024) — "Investigating Data Contamination for Pre-training Language Models"
- **Venue:** Referenced in multiple surveys, 2024
- **Finding:** "The order and distribution of contaminated data moderate performance across different tasks, underscoring the need for evaluation protocols to be differentially designed for each task."
- **Gap:** Acknowledges task-specific variation but does not quantify direction (positive vs negative).

### 1.4 Palavalli et al. (2024) — Verbatim vs Reformatted Contamination
- **Venue:** Referenced in surveys
- **Finding:** "Significant differences in performance gains contributed by verbatim versus reformatted contamination in summarization tasks."
- **Gap:** Format-specific, not domain-specific direction analysis.

### 1.5 MMLU-CF (Zhao et al., 2024) — ACL 2025
- **Venue:** ACL 2025 (Microsoft Research)
- **Finding:** Top models drop 14-16pp on contamination-free MMLU. Maintains subject distributions but does NOT report per-subject contamination direction.
- **Gap:** Aggregate analysis only.

---

## 2. IRT-Based Contamination Analysis

### 2.1 PSN-IRT (Zhou et al., AAAI 2026 Oral) — "Lost in Benchmarks?"
- **Venue:** AAAI 2026
- **Finding:** Uses 4PL IRT on 11 benchmarks (41,871 items). High guessing parameters (c) flagged as contamination indicators. ARC-C, HellaSwag, MMLU show elevated guessing rates.
- **Gap:** Uses guessing parameter for contamination *detection*, not for measuring contamination *effect direction* (γ). No per-domain effect analysis. Does NOT model contamination as a latent variable affecting item difficulty.

### 2.2 ATLAS (Adaptive Testing, 2025)
- **Venue:** arXiv 2025
- **Finding:** Fisher information-guided item selection for efficient LLM evaluation using IRT.
- **Gap:** Efficiency focus, not contamination analysis.

### 2.3 Growing Pains (2026) — Fixed Parameter Calibration
- **Venue:** arXiv, June 2026
- **Finding:** Uses IRT fixed-parameter calibration for extensible benchmarking.
- **Gap:** Calibration methodology, no contamination effect modeling.

### 2.4 Rethinking Math Benchmarks for LLMs using IRT (Castleman, 2025)
- **Venue:** ICML workshop (MLR v273)
- **Finding:** Applies IRT specifically to math benchmarks.
- **Gap:** Single domain (math), no cross-domain contamination comparison.

---

## 3. Simpson's Paradox in ML Evaluation

### 3.1 Simpson's Paradox in Recommender Fairness (2022)
- **Venue:** arXiv:2210.07755
- **Finding:** Per-user vs aggregated evaluations in recommender systems can show reversed trends due to distributional differences.
- **Relevance:** Closest analogy to our finding. But in recommendation, not LLM benchmarking or contamination.

### 3.2 FedCFA (AAAI 2025) — Model Aggregation
- **Venue:** AAAI 2025
- **Finding:** Simpson's paradox in federated learning model aggregation.
- **Gap:** Federated learning context, not benchmark evaluation.

### 3.3 SimNet (KDD 2023) — Automatic Paradox Discovery
- **Venue:** KDD 2023
- **Finding:** Neural network to discover Simpson's paradox instances in data.
- **Gap:** General methodology, not applied to LLM contamination.

### **No paper applies Simpson's paradox framing to benchmark contamination analysis.**

---

## 4. Explanatory Mechanisms for Domain-Dependent Effects

### 4.1 Catastrophic Forgetting & Alignment Tax
- Fine-tuning on contamination data (which is STEM-heavy) could cause catastrophic forgetting in non-STEM domains
- Alignment tax is non-uniform: factual knowledge and math show minimal degradation; nuanced discussion shows significant degradation
- **Mechanism:** SFT on STEM-dominated contamination data → positive transfer to STEM → negative interference to Humanities/Medical

### 4.2 Bloom's Taxonomy & Cognitive Complexity (Huber & Niklaus, COLING 2025)
- LLMs perform better at lower Bloom levels (Remember, Understand) than higher (Analyze, Evaluate, Create)
- STEM contamination may boost lower-level recall; Humanities tasks requiring higher-order reasoning may be harmed by memorization-focused training
- **Mechanism:** Domain-specific cognitive complexity determines contamination effect direction

### 4.3 Overtrained Small Models (Springer et al., ICML 2025)
- Overtrained models are more fragile to fine-tuning
- Scale-dependent effect: larger models absorb contamination without interference; smaller models suffer catastrophic forgetting
- **Mechanism:** Explains model-size interaction with domain-dependent effects

### 4.4 Knowledge Recall vs Reasoning (multiple 2024-2025 papers)
- Contamination primarily aids recall-type tasks; reasoning tasks can be harmed
- STEM domains in MMLU are more recall-oriented (formulas, facts); Humanities require nuanced judgment
- **Mechanism:** Contamination SFT strengthens recall pathways at cost of reasoning pathways

---

## 5. Novelty Assessment

| Aspect | Prior Work Exists? | Our Contribution |
|--------|-------------------|------------------|
| Contamination rates vary by domain | ✓ (Reddy 2026, Hidayat 2025) | — |
| Contamination magnitude varies by domain | ✓ (multiple) | — |
| Contamination effect *direction* varies by domain (γ>0 vs γ<0) | **✗ NOT REPORTED** | **NOVEL** |
| IRT for contamination detection | ✓ (PSN-IRT, AAAI 2026) | — |
| IRT γ parameter as contamination effect *quantifier* (not just detector) | **✗ NOT REPORTED** | **NOVEL** |
| Simpson's paradox in contamination analysis | **✗ NOT REPORTED** | **NOVEL** |
| Per-domain IRT calibration showing opposing effects | **✗ NOT REPORTED** | **NOVEL** |

### Summary

**Our finding is novel on three fronts:**

1. **Direction reversal:** No prior work reports contamination *hurting* specific domains (negative γ). All existing work assumes contamination either helps or has null effect.

2. **IRT γ as effect quantifier:** Prior IRT work (PSN-IRT) uses the guessing parameter (c) for contamination *detection*. We use γ as a continuous contamination *effect* parameter that can be positive or negative, providing a richer characterization.

3. **Simpson's paradox framing:** No paper applies this framing to contamination. The insight that aggregate contamination effects can mask opposing domain-level effects is unreported.

---

## 6. Closest Related Work (for positioning)

| Paper | Year | Venue | Relationship |
|-------|------|-------|-------------|
| Reddy & Karmakar, "Are LLMs Truly Smarter?" | 2026 | arXiv | Differential contamination rates; we show differential effect *directions* |
| Zhou et al., PSN-IRT | 2026 | AAAI | IRT for benchmark quality; we extend to contamination effect modeling |
| Bordt et al., "How Much Can We Forget?" | 2025 | ICML | Contamination can be forgotten at scale; we show it can have negative effects at domain level |
| Hidayat et al., "Simulating Training Data Leakage" | 2025 | arXiv | Domain-specific contamination magnitude; we show direction can reverse |
| Springer et al., "Overtrained Models" | 2025 | ICML | Mechanistic explanation for our scale-dependent effects |

---

## 7. Suggested Literature Map Entries

```yaml
domain_dependent_contamination:
  - id: reddy2026smarter
    title: "Are Large Language Models Truly Smarter Than Humans?"
    authors: "Reddy, M.E. & Karmakar, S."
    year: 2026
    venue: arXiv
    relevance: "differential contamination rates across MMLU domains"
    
  - id: zhou2026psnirt
    title: "Lost in Benchmarks? Rethinking LLM Benchmarking with IRT"
    authors: "Zhou, H. et al."
    year: 2026
    venue: AAAI (Oral)
    relevance: "IRT guessing parameter as contamination signal; closest methodological ancestor"

  - id: hidayat2025simulating
    title: "Simulating Training Data Leakage in Multiple-Choice Benchmarks"
    authors: "Hidayat, N.S. et al."
    year: 2025
    venue: arXiv
    relevance: "domain-specific contamination magnitudes; Anatomy > STEM > reasoning"

  - id: bordt2025forget
    title: "How Much Can We Forget about Data Contamination?"
    authors: "Bordt, S. et al."
    year: 2025
    venue: ICML
    relevance: "contamination forgetting under scaling; complementary perspective"

  - id: springer2025overtrained
    title: "Overtrained Language Models Are Harder to Fine-Tune"
    authors: "Springer, J.M. et al."
    year: 2025
    venue: ICML
    relevance: "mechanistic explanation for model-size-dependent degradation"

  - id: dong2024generalization
    title: "Generalization or Memorization: Data Contamination and Trustworthy Evaluation"
    authors: "Dong, Y. et al."
    year: 2024
    venue: ACL Findings
    relevance: "memorization vs generalization framing; TED mitigation method"

  - id: huber2025bloom
    title: "LLMs meet Bloom's Taxonomy: A Cognitive View on LLM Evaluations"
    authors: "Huber, T. & Niklaus, C."
    year: 2025
    venue: COLING
    relevance: "cognitive complexity framework explaining why contamination affects domains differently"

simpsons_paradox_ml:
  - id: simpson2022recommender
    title: "Simpson's Paradox in Recommender Fairness"
    authors: (authors not retrieved)
    year: 2022
    venue: arXiv
    relevance: "closest application of Simpson's paradox to ML evaluation"
```

---

## 8. Implications for Paper Framing

Our contribution can be framed as:

> "We provide the first empirical evidence that benchmark contamination can have **opposite-sign effects** across cognitive domains, with STEM subjects benefiting (γ > 0) while Humanities and Social Sciences are harmed (γ < 0). This domain-dependent contamination effect represents a Simpson's paradox in LLM evaluation: aggregate contamination metrics mask opposing subgroup trends. We use IRT's γ parameter not merely as a contamination detector (cf. PSN-IRT) but as a continuous effect quantifier that reveals this hidden structure."

**Key differentiator from PSN-IRT:** They use IRT parameters to *detect* contamination (high c = suspected leakage). We use IRT to *measure the direction and magnitude* of contamination's effect on model ability, revealing that this effect is domain-dependent and can be negative.
