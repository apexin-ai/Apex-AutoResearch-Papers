# Paper Framing — cert_manip_resist_eval (v2: Adaptive Adversary)

> Last updated: 2026-05-22 | Reason: Reframe around adaptive adversary vs BFT, remove dead taxonomy claim

## Target
EMNLP 2026 (via ARR)

## Title Candidates
1. "The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer"
2. "The Weakest Link: Individual Robustness Dominates Diversity in Multi-Judge LLM Evaluation Security"
3. "Against the Diversity Assumption: Adaptive Adversaries Break Multi-Judge LLM Evaluation Panels at the Weakest Link"

## Core Insight
Multi-judge LLM evaluation panel security is fundamentally misunderstood. The field assumes diversity (more independent judges) is the primary defense against manipulation, analogous to Byzantine Fault Tolerance (BFT). We show this analogy breaks: BFT assumes random faults, but LLM adversaries are *adaptive* — they target the weakest judge. Under adaptive adversaries, panel ASR is dominated by the weakest member's individual robustness (η_max), not diversity (K_eff). Worse, pursuing diversity introduces weaker judges via a diversity-capability tradeoff, actively harming security.

## Hook
"Adding more diverse judges to an evaluation panel doesn't make it safer — it can make it worse."
This contradicts the prevailing assumption (SoK 2026, Yang et al. 2026, Turkmen et al. 2026) that diversity is the key to robust multi-judge evaluation.

## Core Claims

### Claim 1 (Primary): Weakest-Link Theorem
**Statement**: Under adaptive adversarial attacks, panel ASR is dominated by the individual robustness of the weakest panel member (η_max), with judge diversity (K_eff) providing no significant additional protection.
**Evidence**: Multivariate regression log(ASR) ~ log(K_eff) + log(η_max) on 20 K=3 panels × 6 conditions: η_max significant in 7/12 (p=0.003-0.048); K_eff not significant in 11/12 (p=0.12-0.89). Consistent across 2 datasets (MMLU, ARC) and 6 attack types.
**Strength**: Strong. Cross-dataset, cross-attack consistent. ε-stable.

### Claim 2 (Theoretical): Adaptive Adversary vs BFT Distinction
**Statement**: Classical BFT tolerates f < n/3 random faults via redundancy. LLM adversaries are adaptive (target weakest judge), yielding panel_ASR = Θ(η_max) rather than BFT's Θ(f/n). This fundamental distinction invalidates the diversity-as-defense paradigm.
**Evidence**: (a) Formal theorem deriving Θ(η_max) bound under adaptive adversary model; (b) Empirical verification that attack success concentrates on weakest judge (per-judge ASR variance analysis); (c) Contrast with simulated random-fault baseline where K_eff does help.
**Strength**: Planned. Formal theorem needs writing; random-fault simulation needs running.

### Claim 3 (Empirical): Diversity-Capability Tradeoff
**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) necessarily introduces less capable/robust models, creating a negative correlation between K_eff and min-judge-robustness (r ≈ -0.8). Diversity and security are structurally at odds.
**Evidence**: K_eff vs η_max correlation across 20 panels; capability-stratified analysis showing tradeoff persists within model tiers.
**Strength**: Strong (correlation). Capability-stratified analysis planned.

### Claim 4 (Methodological): Family Labels ≠ Diversity
**Statement**: Model family labels (Qwen/Llama/Mistral) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.
**Evidence**: Mann-Whitney U p=0.206, permutation p=0.427 for within vs cross-family MI.
**Strength**: Strong. Clean statistical test, N=15 pairs.

### Claim 5 (Methodological): Gaussian Copula Failure
**Statement**: The Gaussian copula model systematically underestimates information sharing between LLM judges by 10-21× (up to 235×), invalidating copula-based independence bounds.
**Evidence**: MI_observed / MI_gaussian ratio across 15 pairs × 2 datasets.
**Strength**: Strong. Large effect size, consistent.

### Claim 6 (Practical): Robustness-First Panel Design
**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. This dominates naive strategies (random, max-family-diversity, max-K_eff-only, strongest-K-models).
**Evidence**: Preliminary: min_eta_max strategy dominates 5/6 conditions. Full two-stage algorithm validation planned.
**Strength**: Moderate. Needs formal algorithm + expanded model pool validation.

## Contribution Stack (ordered by strength)
1. **Weakest-link theorem** — primary empirical contribution (challenges diversity assumption)
2. **Adaptive adversary vs BFT distinction** — primary theoretical contribution (explains WHY diversity fails)
3. **Diversity-capability tradeoff** — empirical contribution (shows structural barrier)
4. **Robustness-first panel design** — practical contribution (actionable guidance)
5. **Gaussian copula failure** — methodological contribution
6. **Family label unreliability** — methodological contribution

## Anticipated Reviewer Concerns

### RC1: "η_max dominating is obvious — of course weak judges make weak panels"
**Response**: (a) Existing literature assumes diversity is sufficient (SoK reports "7-model committees reduce ASR to 10-19%" without controlling for individual model quality); (b) We formalize via adaptive adversary model showing WHY — not just THAT — this happens; (c) The diversity-capability tradeoff is non-obvious and has practical implications.

### RC2: "Only 6 models — too small for generalizable claims"
**Response**: Expand to 15+ models including API models (GPT-4o-mini, GPT-4o, GPT-4.1, Claude, Gemini) + larger open-source (70B class). Weakest-link theorem tested on C(15,3) = 455 panels.

### RC3: "Only limited attack types"
**Response**: Expand to 6+ attack types covering prompt injection, score manipulation, sycophancy bias, verbosity bias, position bias, authority bias.

### RC4: "BFT comparison is a strawman — nobody literally claims BFT for LLM panels"
**Response**: (a) The *implicit* assumption is BFT-like: "more independent judges = more robust"; (b) We make this implicit assumption explicit and show where it breaks; (c) The random-fault simulation confirms diversity DOES help under BFT assumptions, validating the distinction.

### RC5: "Panel design algorithm is trivial — just use the strongest models"
**Response**: (a) "Strongest" varies across attack types; (b) Two-stage algorithm outperforms both "min η_max only" and "max K_eff only" in capability-matched settings; (c) Algorithm provides principled threshold selection.

### RC6: "No theoretical novelty — just regression analysis"
**Response**: (a) Adaptive adversary bound is a formal theorem; (b) Diversity-capability tradeoff formalization is novel; (c) Copula failure has implications for MI-based evaluation frameworks beyond this paper.

## Story Arc
1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (SoK, Yang, Turkmen)
2. **Tension**: This assumption mirrors BFT, which assumes random faults — but LLM adversaries are adaptive
3. **Insight**: Under adaptive adversaries, panel_ASR = Θ(η_max); diversity provides no protection because the attacker always targets the weakest link
4. **Aggravation**: Worse, pursuing diversity introduces weaker judges (diversity-capability tradeoff), actively harming security
5. **Resolution**: Robustness-first panel design + formal framework for reasoning about panel security under adaptive adversaries
