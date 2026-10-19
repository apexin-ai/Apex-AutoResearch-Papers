# Paper Framing — cert_manip_resist_eval (v4: 15-Model Empirical Revision)

> Last updated: 2026-05-22 | Reason: 15-model/455-panel results fundamentally changed Claim 1 direction; K_eff independently positive; dual vulnerability drivers

## Target
EMNLP 2026 (via ARR)

## Title Candidates
1. "The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer"
2. "More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries"
3. "Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability"

## Core Insight
Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently **positively** correlated with attack success rate. Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with their relative importance depending on attack type. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create, finding judge-specific vulnerabilities across a wider attack space.

## Hook
"Adding more diverse judges to an evaluation panel doesn't just fail to help — it actively makes the panel more vulnerable to adversarial manipulation."

## Novelty Positioning
We do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:
1. **First empirical quantification of diversity's independent harmful effect** in the LLM-judge domain (15 models, 455 panels, residualized K_eff analysis confirming independent effect beyond η_max)
2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominates bias attacks; K_eff dominates transferable attacks)
3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries
4. **Structural barriers**: copula failure (10-21× MI underestimation), diversity-capability tradeoff (now with independent predictive evidence), family label unreliability
5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation

## Core Claims

### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap
**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max, 9/12 FDR sig) AND panel diversity (K_eff, 8/12 FDR sig positive after residualization). Diversity **increases** vulnerability. Their relative importance is condition-dependent: η_max dominates shared-bias attacks, K_eff dominates transferable attacks.
**Evidence** (15-model, 455 panels, 12 conditions):
- η_max FDR significant: **9/12**
- K_eff raw FDR significant positive: **12/12**
- K_eff residualized (orthogonalized against η_max, VIF=1.00): **8/12 FDR sig positive**
- Sensitivity (exclude ACC < 0.5): K_eff_resid **9/12** sig → not driven by extreme outliers
- **K_eff dominates η_max** in 2 conditions: arc×score_manipulation (η_max p=0.117 NS, K_eff_resid p=1.7e-7), arc×position_bias (η_max p=0.910 NS, K_eff_resid p=1.8e-8)
- **η_max dominates K_eff** in bias-type attacks: sycophancy, verbosity, authority
- Confound status: mean |r|=0.700 (SEVERE), but 2 BROKEN conditions (r≈0.35) confirm independent K_eff effect (p=6e-26, 4e-16)
**Strength**: Strong. Residualized analysis + confound-free conditions + sensitivity analysis all converge.
**Headline**: "Both η_max (9/12) and K_eff (8/12 residualized) independently predict panel vulnerability. Diversity actively increases attack surface."

**Comparison to 6-model results** (for transparency):
- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → "K_eff irrelevant"
- 15-model (455 panels): K_eff 8/12 sig positive, η_max 9/12 sig → "K_eff independently harmful"
- The reversal is driven by model pool expansion: more diverse capability spectrum enables detecting K_eff's real effect.

### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap
**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.
**Evidence** (15-model, 455 panels):
- K_eff significant in both regimes (12/12 adaptive, 12/12 RF), both positive direction
- K_eff gains significance: 11/12 (RF β larger than adaptive β in most conditions)
- ΔR² = +0.213 mean
**Reframing from v3**: Original BFT contrast ("K_eff helps under RF but not adaptive") does NOT hold — K_eff is harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.
**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped.

### Claim 3 (Empirical): Diversity-Capability Tradeoff
**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.
**Evidence**:
- K_eff-η_max correlation: r = +0.700 (15-model)
- Residualized K_eff still significant 8/12 → not purely mediated by η_max
- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains
**Upgrade from v3**: From "correlation" to "independent predictive effect" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.
**Strength**: Strong (statistical association). Causal language avoided.

### Claim 4 (Methodological): Family Labels ≠ Diversity
**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.
**Evidence**: Mann-Whitney U p=0.206, permutation p=0.427 for within vs cross-family MI. (6-model data; needs 15-model revalidation with 105 pairs)
**Strength**: Moderate (needs 15-model update).

### Claim 5 (Methodological): Gaussian Copula Failure
**Statement**: The Gaussian copula model systematically underestimates information sharing between LLM judges by 10-21× (up to 235×), invalidating copula-based independence bounds.
**Evidence**: MI_observed / MI_gaussian ratio across model pairs × datasets. (Needs 15-model update)
**Strength**: Strong (6-model). Needs 15-model revalidation.

### Claim 6 (Practical): Robustness-First Panel Design
**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.
**Evidence**: min_eta_max strategy dominates 5/6 conditions (6-model). Full 15-model validation needed.
**Strength**: Moderate. Updated rationale: K_eff's positive (harmful) effect should diminish when η_max is controlled by screening.

### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Vulnerability Drivers
**Statement**: The dual vulnerability driver effect (Claim 1) varies by aggregation rule. Bayesian aggregation partially breaks the η_max effect; threshold voting amplifies K_eff's harmful effect.
**Evidence** (6-model, needs 15-model rerun):
- Majority: η_max 5/12, K_eff mostly NS
- Threshold: K_eff positive 8/12 (diversity harmful under unanimity)
- Bayesian: η_max 2/12 (weakened)
**Needs**: 15-model/455-panel rerun of plan_010 aggregation analysis.
**Strength**: Moderate (6-model only).

## Contribution Stack (ordered by strength)
1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff independently harmful + condition-dependent dominance pattern)
2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)
3. **BFT reversal mechanism** — theoretical contribution (why independence hurts under adaptive adversaries)
4. **Aggregation-dependent effects** — empirical+practical (Bayesian as partial defense; threshold as amplifier)
5. **Robustness-first panel design** — practical contribution
6. **Gaussian copula failure** — methodological contribution
7. **Family label unreliability** — methodological contribution
8. **Adaptive vs random-fault predictability gap** — empirical (R² gap, weakened from original)

## Anticipated Reviewer Concerns

### RC1: "K_eff positive is just confound with η_max"
**Response**: (a) Residualized K_eff (VIF=1.00) still significant 8/12; (b) In confound-free conditions (r≈0.35), K_eff p < 1e-16; (c) Sensitivity analysis excluding extreme models: 9/12 still significant. Three independent lines of evidence rule out confound artifact.

### RC2: "Why does diversity hurt? What's the mechanism?"
**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis: K_eff dominates transferable attacks (score_manipulation, position_bias) where attack diversity maps to judge diversity; η_max dominates shared-bias attacks (sycophancy, verbosity) where all judges share similar biases.

### RC3: "Only 15 models — does this generalize?"
**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).

### RC4: "BFT comparison is a strawman"
**Response**: (a) The implicit assumption "more diverse judges = more robust" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.

### RC5: "Why not just use the strongest models?"
**Response**: (a) "Strongest" varies by attack type; (b) K_eff dominates η_max in 2 conditions — even all-strong panels are vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.

### RC6: "No theoretical novelty"
**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.

### RC7: "Why not just use Bayesian aggregation?"
**Response**: (a) Bayesian reduces η_max significance but K_eff effect unknown at 15-model scale; (b) Requires clean accuracy prior; (c) Adaptive attacker can target Bayesian weighting; (d) Defense stack (selection + aggregation) recommended.

### RC8 (new): "6-model and 15-model results contradict — which is right?"
**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff positive) has 23× more panels, wider capability range, and passes residualized validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.

## "When Diversity Helps" Section
Diversity MAY be beneficial under specific conditions — paper must acknowledge nuance:
1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary
2. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.
3. **Shared-bias attacks where η_max is high and uniform**: when all models are similarly vulnerable (low η_max variance), K_eff's independent harmful effect is weaker. But this is a narrow regime.
4. **Disclaimer**: K_eff's harmful effect was significant in 8/12 conditions including confound-free ones. "When diversity helps" is the exception, not the rule, under adaptive adversaries.

## Story Arc (v4)
1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)
2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types
3. **Surprise**: Diversity doesn't just fail to protect — it **actively increases vulnerability**. K_eff is significantly positive in 12/12 conditions (8/12 after residualization)
4. **Mechanism**: BFT assumes random faults; adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent importance
5. **Nuance**: K_eff dominates transferable attacks; η_max dominates shared-bias attacks. The diversity-capability tradeoff provides partial (but not complete) explanation
6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels
7. **Implication**: The LLM evaluation community should rethink the "more diverse = more robust" assumption. Panel security requires managing both individual robustness AND structural diversity
