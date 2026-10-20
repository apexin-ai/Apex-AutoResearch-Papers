# Paper Framing — symb_invariant_consensus

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25)
- Fallback: AAAI 2027 (Aug 1)
- Deadline: May 25, 2026 (ARR submission)

## Core Claims (3 条)
1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).
2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is governed by trace diversity (C0), which reflects effective output diversity — SICA adds value when C0>20% (diverse outputs, disagreement to resolve) but degenerates to SC when C0<5% (converged outputs, no disagreement). C0 empirically correlates with task-relative model confidence: instruction models show high C0 on challenging tasks, reasoning models show low C0 universally. Validated across 3 model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ, DeepSeek-R1). [Note: "C0 → epistemic uncertainty" connection reserved for Discussion, not formal claim — reviewer risk of terminology abuse per UQ community standards.]
3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.

## Core Insight
Symbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that trace diversity (C0) — reflecting task-relative model confidence rather than model family or task domain alone — determines the operating regime. This transforms SICA from "yet another ensemble method" into "a method with formally characterizable applicability boundaries," validated across 3 model families and multiple reasoning domains.

## Story Spine
- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.
- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.
- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75%+ win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) — a zero-cost diagnostic reflecting effective output diversity — and validate across 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and multiple domains (logic, math).
- **Headline result template**: "On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty."

## Anticipated Reviewer Concerns & Defensive Experiments
1. **"Gains not statistically significant"** → exp-001: Expand to 804 questions for statistical power
2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K sensitivity; exp-009: overhead analysis (P1); exp-013: constraint ablation (MaxSAT vs count-only vs random-weight)
3. **"Only Qwen models — family-specific artifact?"** → exp-010: Mistral-7B + exp-011: LLaMA-8B (3-family validation)
4. **"Only one reasoning model"** → exp-014: DeepSeek-R1-Distill-7B (second reasoning architecture)
5. **"Only logic domain — restricted answer space"** → exp-012: GSM8K pilot with 14B (cross-domain C0 test)
6. **"ProofWriter shows 0pp gain"** → Domain analysis in exp-001 expanded results
7. **"Random tiebreak baseline closes the gap"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison (done on D012, will re-run on expanded)
8. **"Why not just use a reasoning model?"** → exp-005: QwQ-32B + exp-014: DeepSeek-R1 show reasoning models are self-consistent → SICA redundant; instruction models (cheaper, more deployed) benefit
9. **"MAX-SAT is over-engineering"** → exp-013: Constraint ablation proves satisfiability checking adds value over simple counting
10. **"Within-family scaling?"** → exp-004: 7B + exp-007: 72B-AWQ show C0 trend within Qwen family

## Working Title
**"When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation"**
(Alternatives: "Beyond Majority Voting: Using Trace Diversity to Predict When Symbolic Consensus Improves LLM Reasoning")

## Paper Structure (EMNLP 8pp + appendix)
- Main Tables: T1 (Main Results 7 models × datasets), T2 (Tiebreak Comparison), T3 (K Sensitivity), T4 (Overhead)
- Main Figures: F1 (Pipeline), F2 (C0 vs Gap Scatter — hero figure), F3 (Operating Regime Heatmap), F4 (K Curve)
- Appendix: Constraint Ablation (exp-013), Case Studies (exp-008), GSM8K (exp-012), Per-Problem Detail

## Claim Risk Notes
- **Claim 1 make-or-break**: exp-013 constraint ablation. If MaxSAT ≈ count-only → reframe as "principled weighting" not "satisfiability-based reasoning"
- **Claim 3 downgrade risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to "binary indicator" not "continuous predictor". Gradient depends on 7B C0 >> 14B C0 >> 72B C0.
- **"Epistemic uncertainty" terminology**: Reserve for Discussion section only. Main text uses "effective output diversity" / "task-relative model confidence". UQ community would attack formal misuse.

## Contingency Plan (D023)
**Trigger**: exp-001 完整结果 SICA ≤ SC（gap ≤ 0pp 或不显著）
**Strategy**: Option A (Analysis Paper) + Option C (FOLIO sub-claim if positive)
- 论文主线从"SICA improves accuracy"转为"characterizing operating conditions of symbolic consensus"
- C0 threshold pattern 成为核心贡献（"at what C0 level does SICA begin to match/exceed SC?")
- FOLIO 正向结果嵌入为"domain formality → effectiveness"子 claim
- Claim 1 弱化为"principled + interpretable tiebreaking"（不 claim accuracy gain）
- 需补：constraint extraction quality vs delta 相关性分析（CPU-only）
- Venue: EMNLP Main (30-35%) / Findings (60-70%) / AAAI 2027 fallback
**Decision point**: exp-001 FOLIO 70题的 C0 和 delta

## Venue Fit Risks
- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the "operating regime characterization" — the tiebreaking mechanism is evidence, not the claim.
- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.
- Negative results: QwQ-32B data must be presented as insight ("When Does Symbolic Consensus Degenerate?"), not failure.
- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.
- **[D023 新增]** If SICA ≤ SC globally: pivot to analysis paper. Must answer "so what should practitioners do?" → C0 as deployment diagnostic.
