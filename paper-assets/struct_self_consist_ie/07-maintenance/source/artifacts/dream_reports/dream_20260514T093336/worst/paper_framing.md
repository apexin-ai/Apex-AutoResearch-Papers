# Paper Framing — struct_self_consist_ie

## Target Venue
- Primary: EMNLP 2026 Main (via ARR May 2026)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May cycle, 2026-05-25

## Core Claims (2 条)

### Claim 1 (Positive — NER)
For entity-level information extraction, structural self-consistency (soft Jaccard over structured outputs) provides a significantly stronger confidence signal than surface agreement (Fleiss' Kappa), enabling effective test-time scaling through consistency-based sample selection.

**MVP evidence**: NER rho_sj=0.388, SJ>FK +12pp (p=2e-20), oracle headroom +5.5pp.

### Claim 2 (Diagnostic — RE + boundary condition)
The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks fundamentally degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range (conditional instances). This establishes a principled boundary for when structural consistency works as a TTS signal.

**MVP evidence**: RE full rho_sj=0.234 (FAIL), RE cond rho_sj=0.372 (SJ>FK +11.8pp). Component decomposition (E1) shows all RE components equally weak (head_sj rho=0.210), ruling out metric design as cause. T=0.7 naturally separates knowledge-gap vs uncertainty errors.

## Story Spine

**Problem**: Test-time scaling (TTS) through sampling + selection requires a reliable confidence signal. Self-consistency has shown promise in reasoning tasks (majority voting), but structured prediction (IE) poses unique challenges: outputs have internal structure (entities, relations, triplets), and simple surface agreement ignores structural similarity.

**Existing approaches & gaps**: Self-consistency in LLM reasoning uses exact-match voting on final answers. For structured prediction, no systematic study exists on whether structural similarity between sampled outputs correlates with accuracy. Fleiss' Kappa measures surface agreement but treats structured outputs as flat tokens, missing structural information.

**Our framing**: We introduce structural self-consistency (soft Jaccard) as a confidence signal for IE test-time scaling. Unlike prior work on reasoning self-consistency, we operate on structured outputs where the metric choice fundamentally matters. We discover a task-complexity boundary: structural consistency is a strong signal for entity-level tasks (NER) where errors are independent, but degrades for relational tasks (RE) where compound error propagation across head/tail/type components amplifies noise. This diagnostic finding provides practical guidance on when TTS works for structured prediction.

**Headline result template**: "On SciERC NER, structural self-consistency achieves rho=0.39 correlation with accuracy (vs rho=0.32 for Fleiss' Kappa, p<1e-19), enabling +X F1 improvement through best-of-N selection. However, on relation extraction, full-set correlation drops to rho=0.23 due to compound error propagation — though conditional analysis (within-capability instances) recovers rho=0.37 with SJ>FK by 12pp."

## Anticipated Reviewer Concerns

### R1: "Only one NER dataset — generalization unclear"
- **Mitigation**: exp-002 (CoNLL-2003) + exp-003 (OntoNotes) validate cross-dataset
- **Priority**: P0, must address before submission

### R2: "Only one model family (Qwen3-8B)"
- **Mitigation**: exp-007 (LLaMA-3.1-8B or similar) shows model-agnostic effect
- **Priority**: P1, strongly recommended

### R3: "RE negative result makes the contribution narrow"
- **Mitigation**: Frame Claim 2 as diagnostic contribution — identifying WHY and WHEN consistency fails is as valuable as showing it works. Component decomposition + temperature sensitivity provide mechanistic explanation.
- **Priority**: Addressed by framing, reinforced by exp-004 (RE diagnostic analysis)

### R4: "No actual TTS improvement demonstrated"
- **Mitigation**: exp-006 (adaptive compute demo) shows concrete F1 gains from SJ-based selection vs random vs FK
- **Priority**: P1, high impact

### R5: "Sample size N=8 may be too small for reliable SJ estimation"
- **Mitigation**: exp-001 (N=16) tests scaling effect on NER; if rho improves, demonstrates N-sensitivity
- **Priority**: P0

### R6: "Conditional analysis cherry-picks favorable instances"
- **Mitigation**: All-zero instances represent fundamental knowledge gaps (model consistently fails), not borderline cases. The separation is principled: consistency should measure uncertainty, not inability. Temperature analysis (T=0.7 increases all-zero count while improving conditional rho) supports this interpretation.
- **Priority**: Addressed by analysis in paper

## Venue Fit

EMNLP is well-suited for:
- NLP-focused analysis of IE methods
- Empirical studies with diagnostic findings
- Negative results that provide principled explanations

Risk: purely analytical paper without a new method. Mitigation: structural self-consistency + the diagnostic framework ARE the methodological contributions; the findings provide actionable guidelines.
