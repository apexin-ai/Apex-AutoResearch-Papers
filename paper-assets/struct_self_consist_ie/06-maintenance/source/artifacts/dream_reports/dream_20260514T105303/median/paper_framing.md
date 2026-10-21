# Paper Framing — struct_self_consist_ie

> Updated 2026-05-14 post-Dream analysis. Dream dream_20260514T093336 revealed structural issues (3/6 all tiers). Major revision: add strong baselines, reframe contribution, expand evaluation.

## Target Venue
- Primary: EMNLP 2026 Main (via ARR May 2026)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May cycle, 2026-05-25

## Core Claims (2 条)

### Claim 1 (Positive — NER)
For entity-level information extraction, set-aware self-consistency (soft Jaccard over structured outputs) provides a significantly stronger confidence signal than both surface agreement (Fleiss' Kappa) AND cheaper alternatives (sequence log-probability, exact-match voting), enabling effective test-time scaling through consistency-based sample selection.

**Key**: Claim 1 must beat log-probability to justify 16x inference cost. If SJ only beats FK but not log-prob, the claim weakens to "SJ is a better consistency metric than FK" (modest contribution). If SJ beats log-prob, the claim becomes "structural consistency captures information beyond raw model confidence" (strong contribution).

**MVP evidence**: NER rho_sj=0.388 (SJ>FK +12pp, p=2e-20). Baseline comparisons (log-prob, exact-match, entity voting) pending — these are the make-or-break experiments.

### Claim 2 (Diagnostic — task-complexity boundary)
The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks fundamentally degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested (SJ, FK, log-prob, exact-match).

**MVP evidence**: RE full rho_sj=0.234, RE cond rho_sj=0.372 (SJ>FK +11.8pp). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.

## Story Spine

**Problem**: Test-time scaling (TTS) through sampling + selection requires a reliable confidence signal. Self-consistency has shown promise in reasoning tasks (majority voting), but structured prediction (IE) poses unique challenges: outputs have internal structure (entities, relations, triplets), and it is unclear which confidence signals — model confidence (log-prob), surface agreement (exact-match/FK), or structural similarity (SJ) — best correlate with output quality.

**Existing approaches & gaps**: Self-consistency in LLM reasoning uses exact-match voting (Wang et al. 2023). Universal Self-Consistency (Chen et al. NAACL 2024) extends this to non-votable outputs via LLM-as-judge. For structured prediction, no systematic comparison exists across confidence signal families (model-internal vs surface vs structural) for TTS selection. Semantic uncertainty methods (Kuhn et al. ICML 2023) cluster outputs by equivalence but don't leverage structural similarity.

**Our framing**: We systematically compare four families of confidence signals for IE test-time scaling: (1) model confidence (sequence log-probability), (2) surface agreement (Fleiss' Kappa, exact-match voting rate), (3) set-aware structural similarity (soft Jaccard), and (4) entity-level majority voting. We discover that set-aware consistency outperforms all alternatives for entity-level tasks, but ALL signals degrade for relational tasks due to compound error propagation. This establishes both the best-practice confidence signal for NER TTS and a principled task-complexity boundary for consistency-based TTS in structured prediction.

**Headline result template**: "On three NER datasets, set-aware self-consistency (soft Jaccard) achieves rho=0.39-0.45 correlation with accuracy, outperforming sequence log-probability (rho=X), exact-match voting (rho=Y), and Fleiss' Kappa (rho=0.26-0.32), yielding +Zpp F1 via best-of-N selection. However, on relation extraction, all confidence signals degrade (full-set rho<0.28), with conditional analysis revealing a task-complexity boundary governed by compound error propagation."

## Anticipated Reviewer Concerns

### R1: "Only one NER dataset — generalization unclear"
- **Mitigation**: exp-002 (CoNLL-2003) + exp-003 (WNUT-17) validate cross-dataset across 3 domains (science/news/social media)
- **Priority**: P0

### R2: "Only one model family (Qwen3-8B)"
- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect
- **Priority**: P0

### R3: "FK is a strawman baseline — what about log-prob, USC, exact-match?"
- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match voting), exp-014 (entity voting) provide comprehensive baseline comparison. USC discussed in related work (requires LLM-as-judge, orthogonal approach).
- **Priority**: P0, make-or-break

### R4: "No actual TTS improvement demonstrated"
- **Mitigation**: exp-006 (adaptive compute demo) — SJ vs log-prob vs FK vs random best-of-N selection on all NER datasets
- **Priority**: P0

### R5: "Sample size N=8 may be too small for reliable SJ estimation"
- **Mitigation**: exp-001 (N=16) with multi-seed robustness
- **Priority**: P0

### R6: "Conditional analysis cherry-picks favorable instances"
- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.
- **Priority**: P0 (add sensitivity analysis)

### R7: "Only ρ as evaluation metric"
- **Mitigation**: Add AUROC, calibration plots, Kendall's τ for all experiments
- **Priority**: P0

### R8: "Formula-implementation discrepancy"
- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)
- **Priority**: P0, paper writing fix

### R9: "Evaluation circularity (T>0 consistency vs T=0 F1)"
- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).
- **Priority**: P0

### R10: "Insufficient related work"
- **Mitigation**: Expand to 30+ references. Must cite: USC (Chen 2024), semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Desai & Durrett 2020), SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017).
- **Priority**: P0, Paper Agent handles

## Venue Fit

EMNLP is well-suited for:
- Systematic empirical comparison of confidence signals for structured prediction
- Diagnostic findings with principled explanations
- The "comparison + boundary condition" contribution pattern

Risk: If SJ doesn't beat log-prob, the paper becomes a pure analysis piece. Mitigation: diagnostic framework (Claim 2) remains valid regardless; reframe as "systematic study of confidence signals for IE TTS."
