---
dream_id: dream_20260515T092545
tier: median
overall_score: borderline
timestamp: 2026-05-15T10:22:33.363207+00:00
---

# Dream Review Report: "Confidence Signals Predict but Cannot Select in Constrained-Decoding Information Extraction"

**Target Venue**: EMNLP 2026 Findings
**Review Mode**: Full (2-Reviewer Roundtable)
**Date**: 2026-05-15

---

## Consolidated Scores (ARR Scale)

| Dimension | Score | Descriptor |
|-----------|-------|------------|
| Soundness | 3.5 / 5 | Between Acceptable and Strong |
| Excitement | 3 / 5 | Borderline |
| Overall Assessment | 3 / 5 | Borderline |
| Reviewer Confidence | 4 / 5 | High |

---

## 1. Paper Summary

This paper systematically evaluates five confidence signal families—log-probability, set Jaccard similarity (SJ), Fleiss' kappa (FK), exact match (EM), and voting confidence—for quality estimation (QE) and sample selection in LLM-based NER and RE under constrained (grammar-guided) decoding. Using two 8B-parameter models (Qwen3-8B, LLaMA-3.1-8B) across SciERC, CoNLL-2003, and WNUT-17, the paper identifies a "predict-but-cannot-select" gap: structural consistency signals achieve strong instance-level quality prediction (AUROC up to 0.75) but fail to improve per-sample selection over greedy decoding (best gain: +0.6pp, p=0.39). A controlled free-form decoding ablation recovers logprob variance by ~3.5×, improving NER selection by +2.0pp (p=0.078) but showing negligible RE improvement. A supervised DeBERTa verifier captures 15.9% of NER oracle headroom, establishing a partial upper bound on gap closability.

---

## 2. Experiment Coverage Assessment

The review_context.yaml specifies 4 imagined experiments:

| Experiment | Plan ID | Covered in Paper? | Section |
|------------|---------|-------------------|---------|
| NER OOD Robustness (SciERC→WNUT-17) | exp-011 | ✅ Yes | §5.5, Tables 7-8 |
| LLaMA CoNLL NER (cross-model validation) | exp-017 | ✅ Yes | §5.4, Tables 5-6 |
| Free-form Decoding Ablation | exp-018 | ✅ Yes | §5.3, Tables 3-4 |
| Simple Verifier Baseline | exp-019 | ✅ Yes | §5.6, Tables 9-10 |

**Coverage**: 4/4 imagined experiments are present in the paper. The experimental scope matches the design.

---

## 3. Strengths

### S1. Clean Conceptual Contribution (R1 + R2 agreement)
The disentanglement of quality estimation (instance-level: "is this instance easy or hard?") from sample selection (per-sample: "which candidate is best?") is the paper's most valuable insight. Four of five signals are instance-level aggregates that *by construction* cannot rank candidates within an instance. Only log-probability provides per-sample scores, and it is compressed by constrained decoding. This clarification addresses a genuine conflation in prior work on self-consistency for IE.

### S2. Rigorous Statistical Methodology (R1 lead)
The paper employs bootstrap confidence intervals (1000 iterations), paired Wilcoxon tests, Cohen's d effect sizes, and proper baselines (greedy, random, oracle). The non-tied subset analysis (40% non-tied instances showing +2.9pp, p=0.01) provides clean mechanistic confirmation that logprob *can* discriminate when variance is present. This level of statistical rigor is above average for NLP empirical papers.

### S3. Controlled Free-Form Ablation (R1 + R2 agreement)
The most novel empirical contribution. Removing Outlines grammar constraints while keeping all other factors constant (model, prompts, temperature) recovers logprob within-sample variance by 3.9× (NER) and 3.7× (RE), with Wilcoxon p < 10⁻⁴⁸. This provides direct evidence that constrained decoding contributes to the selection bottleneck. The honest reporting of borderline NER improvement (p=0.078) and RE non-improvement (p=0.31) strengthens credibility.

### S4. Cross-Model and Cross-Dataset Validation (R1 lead)
The 2×2 model × dataset matrix (Table 5) showing SJ ρ cross-model delta < 0.01 is strong evidence of model-agnostic signal behavior. The CoNLL ceiling effect analysis (greedy F1=0.926, headroom 1.9pp → selection meaningless) provides a useful task-complexity boundary interpretation.

### S5. Informative OOD Analysis (R2 lead)
The WNUT-17 evaluation revealing that structural signals retain ~40% of in-domain ρ while logprob *inverts* (0.205 → −0.287) is a genuinely interesting finding. It demonstrates that consistency-based signals, while degraded, maintain directional validity under domain shift—a practically important property.

### S6. Gap Closability via Supervised Verifier (R1 + R2 agreement)
The headroom cascade (greedy 0% → best unsupervised 4.5% → verifier 15.9% → oracle 100% on NER) transforms a purely negative finding into a partially constructive one. The large remaining gap (84% NER, 90% RE) frames a concrete open problem.

---

## 4. Weaknesses

### W1. Core Finding is Moderately Predictable (R1 + R2 agreement, Major)
For fine-tuned models generating near-identical structured JSON outputs under grammar-guided constraints, the finding that unsupervised signals cannot distinguish among very similar candidates is not highly surprising. The four instance-level signals are *definitionally* unable to select; the log-probability compression under constrained decoding is a natural consequence of vocabulary restriction at each step. The paper argues non-obviousness by analogy to MBR success in machine translation, but this analogy is imperfect: MT outputs are sequences with continuous similarity metrics (BLEU/chrF), while IE outputs are discrete sets. A stronger articulation of what specific prior work would have predicted success here is needed.

### W2. Single RE Benchmark (R1 + R2 agreement, Major)
All RE results derive from SciERC alone. The paper flags this repeatedly (5+ times), which is commendably honest, but it limits generalizability of approximately one-third of the claimed findings. The 40% zero-F1 rate on RE creates a severe floor effect. Additional RE benchmarks (ACE05, DocRED, TACRED) would substantially strengthen the paper.

### W3. Free-Form Ablation Limited to One Configuration (R1 lead, Major)
The ablation—the paper's most important mechanistic finding—covers only Qwen3-8B on SciERC. Without replication on LLaMA or CoNLL, it is unclear whether the variance recovery and borderline NER selection improvement generalize. This is particularly concerning given the RE non-result (p=0.31), which could be dataset-specific or fundamental.

### W4. No Entropy-Based Signal Tested (R1 lead, Moderate)
Given that log-probability is the sole per-sample signal and is the key bottleneck, testing predictive entropy (sum of token-level entropies) or generation-level entropy as an alternative would strengthen the claim that model-internal signals generically fail under constrained decoding. This would be a low-cost addition since token-level logprobs are already collected.

### W5. N and T Under-Explored for Selection (R1 lead, Moderate)
The paper fixes N=8 and T=1.0 for selection experiments. Whether higher diversity (T=1.2+) or much larger candidate pools (N=32, N=64) could unlock selection is not addressed. At larger N, oracle headroom increases, potentially creating more room for signals to discriminate. Even a simulation-based analysis would be informative.

### W6. No Deep Analysis of WHY Consensus Fails for IE vs MT (R1 + R2 agreement, Moderate)
The paper notes that MBR decoding succeeds in MT where BLEU/chrF provides smooth utility surfaces, and that set-based IE metrics create a different optimization landscape. But no formal or empirical analysis explains *what structural property* of IE outputs causes utility-quality misalignment within instances. Is it the discrete set structure? Combinatorial output space? Error correlation? This theoretical gap weakens the paper's explanatory power.

### W7. CoCoA Under-Discussed (R2 lead, Minor)
CoCoA (Vashurin et al. 2025a) combines confidence and consistency in an MBR framework for QA and summarization. As the closest methodological analog, it deserves deeper engagement—particularly explaining why the MBR approach that works for QA fails for structured IE. The current one-sentence mention is insufficient.

---

## 5. Questions for Authors

1. **Entropy-based alternative**: Have you tested predictive entropy (sum of token-level entropies per sample) as an alternative per-sample signal? Since token-level logprobs are already collected, this would be a low-cost addition that could strengthen the claim about model-internal signal failure under constrained decoding.

2. **Within-instance utility correlation**: You argue MBR-style consensus proximity fails within instances. Can you quantify this directly—e.g., a distribution of within-instance Kendall τ between consensus-proximity scores and per-sample F1? This would make the claim precise.

3. **N-scaling for selection**: Your N-scaling analysis focuses on QE. At N=64, oracle headroom is substantially larger. Would logprob selection improve, or does compression persist regardless of N? Even a simulation extrapolation would be informative.

4. **CoNLL cross-model detail**: The < 0.01 SJ ρ delta is impressive but occurs on the easiest dataset where all signals converge. What is the cross-model delta on SciERC? Is the model-agnostic claim equally strong on harder tasks?

5. **Why does RE show negligible free-form improvement?** Is this the combinatorial entity-set complexity you hypothesize, or could it be an artifact of the 78% parse rate (more aggressive filtering on RE)? Did you analyze whether filtered-out RE samples are systematically different?

---

## 6. Detailed Assessment by Dimension

### Soundness (3.5/5)
The experimental design is solid: 2 tasks × 2-3 datasets × 2 models, with proper controls and above-average statistical rigor. The five signals are well-chosen and well-defined. The free-form ablation is well-controlled. Claims are appropriately softened ("evidence consistent with" rather than "proves"). Deductions: (a) free-form ablation on single configuration, (b) single RE benchmark, (c) missing entropy-based signal, (d) N/T not explored for selection. These prevent a "Strong" rating but the core methodology is sound.

### Excitement (3/5)
The QE-vs-selection disentanglement is a useful conceptual contribution, and the systematic evaluation is thorough. However, the core finding is moderately predictable given the nature of constrained decoding and instance-level aggregation. The paper documents a problem well but advances only modestly toward a solution (the verifier captures only 16% of headroom). The free-form ablation and OOD logprob-inversion findings add novelty. For Findings, this is adequate; for the main conference, the novelty bar would not be met.

### Overall Assessment (3/5 — Borderline)
A careful, well-executed empirical study that establishes a useful negative result (the predict-but-cannot-select gap) with honest statistical reporting. The systematic QE framework, cross-model validation, and free-form ablation provide practical value for the IE community. The paper is well-written, well-organized, and self-aware about limitations. However, the moderate predictability of the core finding, limited scope (8B models, 2 NER + 1 RE datasets), and lack of a compelling explanation for *why* the gap exists (beyond the descriptive level) place it at the borderline for Findings acceptance. The strongest argument for acceptance is that this is a systematic, carefully hedged negative result that could save other researchers from repeating the same unsuccessful approach.

---

## 7. Roundtable Discussion Summary

### Points of Agreement
- The QE-vs-selection conceptual distinction is the paper's most durable contribution
- Statistical methodology is above-average and honest
- Single RE benchmark is the most significant scope limitation
- Core finding is useful but excitement is limited by predictability
- Free-form ablation is the most novel experimental contribution
- Paper is appropriate for Findings consideration but does not clearly exceed the bar

### Points of Initial Disagreement, Resolved
- **Soundness** (R1: 4 vs R2: 3.5): Resolved to 3.5. R1's higher rating was based on strong controls and statistical rigor; R2's lower rating reflected scope limitations (single ablation config, missing signals). The scope concerns are legitimate deductions from an otherwise strong methodology.
- **Excitement** (R1: 3 vs R2: 2.5): Resolved to 3. R2 argued the finding is largely expected; R1 credited the systematic framework and diagnostic value. For Findings, systematic negative results have value, justifying the higher bound.
- **Overall** (R1: 3.5 vs R2: 3.0): Resolved to 3.0. The paper has genuine merit for Findings but the convergence of moderate novelty, limited scope, and borderline statistical significance on the key free-form result (p=0.078) places it at borderline rather than leaning accept.

### Recommendation
**Borderline for EMNLP 2026 Findings.** The paper would be strengthened most by: (1) replicating the free-form ablation on a second configuration, (2) adding an entropy-based per-sample signal, and (3) deeper engagement with why consensus-proximity fails for IE. If any of these additions pushed the NER selection result to significance or revealed new structure, the paper would move to a clear accept.

---

## 8. Meta-Review

This paper presents a systematic empirical investigation of confidence signals for quality estimation and sample selection in constrained-decoding information extraction. The central "predict-but-cannot-select" finding—that signals predicting instance quality well (AUROC 0.75) fail to improve per-sample selection—is documented with appropriate statistical rigor across multiple models and datasets. The conceptual disentanglement of QE from selection, the free-form decoding ablation recovering logprob variance, and the supervised verifier headroom cascade are the most valuable contributions.

The paper's primary weakness is that the core finding is moderately predictable given the mechanics of constrained decoding (vocabulary restriction → logprob compression) and the instance-level nature of 4/5 signals. Scope limitations (single RE benchmark, single ablation configuration, 8B models only) and the borderline statistical significance of the key free-form NER result (p=0.078) prevent a confident accept recommendation.

For EMNLP 2026 Findings, this is a borderline submission. The careful methodology, honest hedging of claims, and practical diagnostic value argue for acceptance; the moderate novelty and limited scope argue against. The paper would benefit from targeted additions (second ablation configuration, entropy signal, deeper MBR analysis) that could tip the balance.
