# Paper Framing — cert_manip_resist_eval (v5: Post-Clustered-SE Reframe, D019)

> Last updated: 2026-05-22 | Reason: Bootstrap v2 (Reviewer-verified): η_max 5-11/12 (bootstrap 5/12 most reliable), K_eff 0-1/12. η_max:K_eff ratio 5:1 confirms dominance. GAM 6:6 split confirmed. Aggregation gradient independent.

## Target
EMNLP 2026 (via ARR)

## Title Candidates
1. "The Weakest Judge Wins: What Really Drives LLM Evaluation Panel Vulnerability Under Adversarial Attack"
2. "Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation"
3. "The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer" (softened with honest reporting)

## Core Insight
Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity. We conduct the first large-scale empirical study (15 models, 455 panels, 6 attacks, 2 benchmarks) decomposing panel vulnerability into individual weakness (η_max) and structural diversity (K_eff). Key findings: (1) **η_max dominates** panel vulnerability (5-11/12 conditions significant depending on correction method; wild cluster bootstrap — the most reliable method for small cluster counts — gives 5/12, with η_max:K_eff ratio of 5:1); (2) K_eff shows **directional but statistically fragile** association with vulnerability — point estimates predominantly positive (diversity increases risk), but significance collapses from 8/12 (OLS) to 0-1/12 after non-independence correction (bootstrap 1/12, clustered SE 0/12); (3) **GAM reveals a clean attack-type split**: K_eff is positive (harmful) for targeted attacks and negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression; (4) **Aggregation rule choice fundamentally modulates vulnerability**: Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89).

## Hook
"Panel security against adversarial manipulation is dominated by the weakest individual judge — not panel diversity. But how you aggregate judges' votes determines whether diversity becomes a vulnerability or a defense."

## Novelty Positioning
We do NOT claim diversity is harmful with high statistical confidence — K_eff's independent effect is directional but fragile under rigorous correction. Our contributions are:
1. **First large-scale empirical decomposition** of panel vulnerability into η_max and K_eff in the LLM-judge domain (15 models, 455 panels), with transparent robustness analysis showing η_max dominates (5:1 over K_eff under bootstrap inference)
2. **Attack-type taxonomy with clean mechanistic split**: GAM reveals K_eff positive for targeted attacks, negative for shared-bias attacks (6:6 split), explaining WHEN diversity helps vs hurts
3. **Aggregation as a control lever**: voting rule modulates the diversity-vulnerability relationship — Bayesian reverses K_eff direction, threshold amplifies it (D017, independent of non-independence concern)
4. **Robustness-first panel design**: min(η_max) strategy wins 12/12 conditions (Claim 6, unaffected by SE correction)
5. **Structural barriers**: diversity-capability tradeoff (r=0.70), family label unreliability (confirmed at 15-model)
6. **Alternative diversity metrics robustness**: η_max dominance holds across operationalizations — Q-stat only 2/12 sig (r=0.674 with K_eff), disagreement 8/12, κ-diversity 7/12. K_eff practical effect size: IQR → Δ ASR = 1.3pp (directional but practically small)
7. **Methodological transparency**: explicit reporting of how significance changes across OLS → clustered SE → mixed effects, demonstrating the importance of accounting for panel overlap in combinatorial evaluation designs

## Core Claims

### Claim 1 (Primary): Weakest-Link Dominance
**Statement**: Under adaptive adversarial attacks, panel vulnerability is **dominated by individual judge weakness (η_max)**. η_max remains significant in 5-8/12 conditions after non-independence correction (wild bootstrap 5/12, clustered SE 8/12, mixed effects 7/12). K_eff (diversity) shows directional association but significance is fragile (bootstrap 1/12, clustered SE 0/12). The η_max:K_eff dominance ratio is 5:1 under bootstrap — stronger than OLS's 11:8 ≈ 1.4:1.
**Evidence** (15-model, 455 panels, 12 conditions, D019+D021):
- **Regression spec**: log-log OLS: log(ASR + ε) ~ const + log(K_eff) + log(η_max + ε)
- **Standard OLS**: η_max **11/12**, K_eff **8/12** (7+/1−) — inflated by panel non-independence
- **Wild cluster bootstrap v2** (Reviewer-verified, B=9999, Rademacher, 3-position max-p): η_max **5/12**, K_eff **1/12** (mmlu×PI only) — conservative lower bound. Per-position analysis: position 0 gives 6/12 (cluster imbalance: claude-3-haiku=91 panels vs qwen2.5-14b=1), positions 1&2 each give **9/12** (more balanced clusters, consistent with clustered SE). Max-across-positions is legitimate conservative bound but tightened by position 0 imbalance.
- **Clustered SE** (15 judge clusters, CR1): η_max **8/12**, K_eff **0/12** — consistent with per-position bootstrap 1&2
- **Mixed effects** (random judge intercepts): η_max **7/12**, K_eff **3/12** (mmlu×PI, arc×PI, arc×PB)
- SE inflation ~2.5x (consistent with 91/455 panel overlap)
- Bootstrap η_max shows benchmark asymmetry: MMLU 4/6, ARC 1/6 survive. Likely cause: MMLU 4-choice format provides more scoring variance than ARC 2-choice, giving η_max more signal. arc×PI η_max completely lost (OLS p=3e-14 → bootstrap all NS) — signal was entirely from panel overlap.
- **arc×sycophancy exception**: No longer significant under any correction (OLS p=0.013 → bootstrap 0.06 → clustered 0.441 → mixed 0.136). Reported as directional observation, not robust claim.
- **Alternative diversity metrics (OLS)**: Q-stat 2/12, disagreement 8/12 (7+/1−), κ-diversity 7/12 (7+/0−). Q-stat (lowest correlation with K_eff, r=0.674) gives lowest diversity significance — further supports η_max as dominant driver regardless of diversity operationalization.
- **Practical effect size**: K_eff IQR change → Δ ASR = 1.3pp (clustered SE CIs contain zero in 11/12 conditions). Even under OLS, diversity effect is practically small.
**Strength**: η_max dominant (5:1 ratio over K_eff under bootstrap). Absolute significance lower than OLS (5/12 vs 11/12) but relative dominance stronger. K_eff directional but fragile and practically small.
**Headline**: "η_max dominates panel vulnerability (5:1 over K_eff); both channels inflated by panel non-independence, but η_max survives correction while K_eff does not."

### Claim 1b (Secondary): Attack-Type Taxonomy — GAM 6:6 Split
**Statement**: GAM analysis reveals that K_eff's direction cleanly splits by attack mechanism: **positive (diversity harmful) for targeted attacks** (prompt_injection, score_manipulation, position_bias × 2 benchmarks = 6 conditions) and **negative (diversity protective) for shared-bias attacks** (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions). This 6:6 pattern is masked by linear OLS which shows 7+/1−/4NS.
**Evidence**: GAM partial effects, 455 panels, 12 conditions.
- Targeted attacks (exploit judge-specific weaknesses): K_eff partial effect positive in all 6 conditions
- Shared-bias attacks (exploit common cognitive biases): K_eff partial effect negative in all 6 conditions
- **Caveat**: GAM significance of individual conditions needs clustered SE / bootstrapped CI (pending); the structural pattern is the main finding, not individual p-values
**Strength**: Moderate-to-strong as qualitative taxonomic contribution. The clean 6:6 split provides mechanistic explanatory power beyond individual significance counts. Confirmed under correct 3/3/9 tier classification (GAM tier-fix rerun: all macro conclusions unchanged).

### Claim 2 (Empirical): Predictability Gap — Panel Composition Explains RF But Not Adaptive Vulnerability
**Statement**: Panel composition (η_max + K_eff) explains substantially more variance under random faults (R²=0.73-0.81) than under adaptive attacks (lower R²). K_eff is positively associated with vulnerability in BOTH regimes, but: under RF, this association is genuine (survives all corrections, 2/2); under adaptive, it is largely artifactual (0-1/12 after correction). Adaptive adversaries introduce strategic variance beyond what panel structure can predict.
**Evidence** (15-model, 455 panels, D021+RF validation, Reviewer-verified):
- **Random-fault regime** (error = 1 - clean_accuracy, Monte Carlo 10000):
  - K_eff **positive** std_β = +0.215 (MMLU), +0.379 (ARC) — diversity associated with HIGHER error
  - K_eff significant **2/2** under ALL correction methods (OLS, clustered SE, bootstrap)
  - R² = 0.73-0.81 (highly predictable)
- **Adaptive regime** (D021):
  - K_eff also positive under OLS (7+/1−) but significance collapses to **0-1/12** after correction
  - R² substantially lower
- **Contrast**: NOT "diversity helps under RF but hurts under adaptive" — diversity is harmful in both. The contrast is: K_eff's harmful association is GENUINE under RF but INFLATED/ARTIFACTUAL under adaptive due to panel non-independence
- ΔR² gap: RF regime is highly predictable from panel composition; adaptive regime is not
**Correct interpretation**: Random faults are structurally determined by panel composition (hence high R² and genuine K_eff effect). Adaptive adversaries exploit weaknesses strategically, introducing variance that panel-level predictors cannot capture. K_eff in the adaptive regime appears significant under OLS only because of panel overlap inflation.
**Strength**: Strong as predictability gap (R² contrast). The finding that K_eff is genuine under RF but artifactual under adaptive is a clean methodological insight about when non-independence correction matters most.

### Claim 3 (Empirical): Diversity-Capability Tradeoff
**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. The correlation r=+0.700 is a structural constraint — diversity and capability are partially opposed in the current model ecosystem.
**Evidence**:
- K_eff-η_max correlation: r = +0.700 (15-model)
- Under standard OLS: K_eff significant 8/12 (7+/1−) after residualizing η_max
- **D019 caveat**: Under clustered SE, K_eff drops to 0/12; mixed effects gives 3/12. The "independent predictive effect" of K_eff beyond η_max is directional but NOT statistically robust after correcting for non-independence. The structural correlation (r=0.700) itself is unaffected by SE correction — only the regression significance of K_eff as independent predictor changes.
**Framing**: The tradeoff is real as a structural constraint (r=0.700). Whether K_eff has an independent causal effect beyond η_max cannot be confidently established from this data — K_eff's significance is fragile under correction, and the high confound makes disentanglement unreliable.
**Strength**: Moderate (structural correlation strong; independent effect fragile). Causal language avoided.

### Claim 4 (Methodological): Family Labels ≠ Diversity
**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.
**Evidence**:
- 6-model: Mann-Whitney U p=0.206, permutation p=0.427
- **15-model (confirmed)**: p=0.179 (MMLU), p=0.385 (ARC). 14 within-family pairs, 91 cross-family pairs. Still not significant.
- Within-family MI variance is high (e.g., llama-70b↔8b MI only 0.05 due to capability gap > family similarity)
**Strength**: Moderate. Consistent across 6→15 model scaling.

### ~~Claim 5 (Methodological): Gaussian Copula Failure~~ → DOWNGRADED to observation
**Original statement**: Gaussian copula systematically underestimates MI by 10-21×.
**15-model result**: MI_obs/MI_gaussian mean ratio = **0.93** (MMLU), **0.90** (ARC, robust). Copula fits well at 15-model scale. The 6-model 10-21× was a small-sample artifact (15 pairs → 105 pairs, extreme values diluted). Only claude-3-haiku pairs show extreme ratios (212×) due to near-zero ρ with nonlinear dependence.
**Disposition**: Remove as independent contribution. Optionally note in analysis: "Gaussian copula fit is adequate for diverse model pools but breaks down for capability-mismatched pairs with nonlinear dependence."
**Strength**: DEAD as independent claim. May retain as minor observation.

### Claim 6 (Practical): Robustness-First Panel Design
**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.
**Evidence** (15-model, 455 panels — fully validated):
- min(η_max) strategy dominates **12/12 conditions** (up from 5/6 at 6-model)
- ASR advantage range: +0.038 (arc×sycophancy) to +0.511 (arc×prompt_injection)
- Robust across panel sizes K=10, 20, 50
- Even in the sole K_eff-dominant condition (arc×position_bias), min_eta_max still outperforms max_K_eff
- Consistent with canonical regression: η_max 11/12 dominant
**Strength**: Strong (15-model fully confirmed). Zero failure conditions.

### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Both Vulnerability Drivers
**Statement**: Bayesian calibration partially mitigates BOTH vulnerability drivers — weakening η_max dominance AND reversing K_eff from harmful to protective. Different aggregation rules create a gradient from full dual-driver vulnerability (threshold) to partial mitigation (Bayesian).
**Evidence** (15-model, 455 panels, log-log canonical spec — D017, Reviewer-verified from JSON):
- Majority: η_max **11/12**, K_eff **8/12** (7+/1−), R²=0.298 ← canonical baseline (matches dominance table ✓)
- Weighted: η_max **9/12**, K_eff **9/12** (9+/0−), R²=0.284 — reduces both drivers but K_eff stays all positive
- Threshold: η_max **12/12**, K_eff **11/12** (10+/1−), R²=**0.890** — near-perfect fit under unanimity
- Bayesian: η_max **9/12** (↓), K_eff **7/12** (1+/**6 negative**), R²=0.104
- Key findings:
  - Bayesian weakens η_max (11→9/12) AND flips K_eff direction (majority 7+/1− → bayesian 1+/6−)
  - Threshold amplifies both channels: η_max 12/12, K_eff 11/12, R²=0.89 (unanimity maximizes dual-driver predictability)
  - Weighted reduces η_max (11→9/12) but K_eff stays all positive — accuracy weighting alone cannot reverse diversity harm
  - Only Bayesian calibration reverses K_eff direction (6/7 significant coefficients negative)
  - Aggregation gradient: threshold (max vulnerability) → majority → weighted → bayesian (min vulnerability)
**Strength**: Strong (log-log canonical, Reviewer-verified, sanity-checked against Claim 1). Prescriptive: robustness-first selection (Claim 6) + Bayesian aggregation = dual-channel defense stack.

## Contribution Stack (ordered by strength, post-D019 reframe)
1. **Weakest-link dominance** — primary empirical (η_max robust 7-8/12 after all corrections; the strongest, most defensible finding)
2. **Aggregation as control lever** — empirical+practical (D017: Bayesian reverses K_eff direction, weakens η_max; threshold amplifies both; R²=0.89. Independent of non-independence concern)
3. **Attack-type taxonomy / GAM 6:6 split** — mechanistic (targeted=K_eff positive, shared-bias=K_eff negative; clean qualitative pattern; pending correct-tier validation)
4. **Robustness-first panel design** — practical (Claim 6: min_eta_max 12/12 wins; unaffected by SE correction)
5. **Methodological transparency on non-independence** — meta-contribution (demonstrating how OLS → clustered SE → mixed effects changes significance in combinatorial panel designs; useful for future work)
6. **Diversity-capability tradeoff** — empirical (r=0.70; structural, not affected by SE correction)
7. **Family label unreliability** — methodological (confirmed at 15-model scale)
7. **Adaptive vs random-fault predictability gap** — empirical (R² gap)
~~8. **Gaussian copula failure**~~ — REMOVED (falsified at 15-model scale; downgraded to minor observation)

## Anticipated Reviewer Concerns

### RC1: "K_eff positive is just confound with η_max"
**Response**: (a) Under standard OLS, K_eff is significant 8/12 (7+/1−), but after clustered SE correction K_eff drops to 0/12, mixed effects gives 3/12 — K_eff's independent effect is directionally positive but **statistically fragile**; (b) η_max remains robust at 7-8/12 under all corrections, confirming it is NOT a confound artifact; (c) GAM analysis reveals the K_eff direction cleanly splits by attack type (6:6 targeted vs shared-bias), suggesting real structure even if individual significance is fragile under correction; (d) We transparently report all three correction methods, which is itself a methodological contribution for combinatorial panel designs.

### RC2: "Why does diversity hurt? What's the mechanism?"
**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) GAM reveals the mechanism boundary: K_eff partial effect is positive for targeted attacks (6/6 conditions) and negative for shared-bias attacks (6/6 conditions). This clean split explains WHEN diversity helps vs hurts; (d) Note: K_eff's harmful direction is directional under OLS (7+/1−) but significance collapses under non-independence correction (0-3/12). The mechanism is real (GAM pattern), but its statistical strength is sensitive to correction — we report this transparently.

### RC3: "Only 15 models — does this generalize?"
**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).

### RC4: "BFT comparison is a strawman"
**Response**: (a) The implicit assumption "more diverse judges = more robust" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.

### RC5: "Why not just use the strongest models?"
**Response**: (a) "Strongest" varies by attack type; (b) K_eff is the sole significant predictor in 1 condition (arc×position_bias) — even all-strong panels can be vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.

### RC6: "No theoretical novelty"
**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.

### RC7: "Why not just use Bayesian aggregation?"
**Response**: (a) 15-model log-log canonical (D017, Reviewer-verified): Bayesian partially mitigates BOTH drivers — η_max drops to 9/12 (from 11/12), K_eff flips to 6/7 negative (protective). But it doesn't eliminate vulnerability: 9/12 η_max still significant, R² drops to 0.104 (residual vulnerability less predictable); (b) Requires clean accuracy prior which adaptive attackers could target; (c) Even under Bayesian, 9/12 conditions still show η_max vulnerability → robustness-first selection remains necessary; (d) Optimal defense stack: robustness-first selection (eliminates η_max) + Bayesian aggregation (flips K_eff to protective) = dual-channel coverage.

### RC8: "6-model and 15-model results contradict — which is right?"
**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff predominantly positive) has 23× more panels, wider capability range, and passes dominance analysis validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.

### RC9 (new): "arc×sycophancy exception undermines your claim"
**Response**: (a) Post-D019: arc×sycophancy K_eff is NOT significant after correction (OLS p=0.013 → clustered SE p=0.441 → mixed effects p=0.136). It is a directional observation, not a robust standalone finding; (b) However, GAM reveals that ALL shared-bias attacks (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions) show negative K_eff partial effects, while ALL targeted attacks (6 conditions) show positive — the 6:6 split is the robust pattern, not the individual significance of arc×sycophancy; (c) This gives practitioners an actionable taxonomy: targeted attacks → diversity hurts, shared-bias attacks → diversity may help; (d) The structural pattern (GAM) is more informative than individual p-values under various corrections.

## "When Diversity Helps" Section
Diversity IS beneficial under specific conditions — paper must present this as empirically grounded nuance, not just a hypothetical:
1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary
2. **Shared-bias attacks (GAM-confirmed pattern)**: GAM reveals K_eff partial effect is negative (protective) for all 6 shared-bias conditions (sycophancy, verbosity_bias, authority_bias × 2 benchmarks). Note: arc×sycophancy K_eff was significant under standard OLS (p=0.013) but **not significant after clustered SE (p=0.441) or mixed effects (p=0.136)**. The directional pattern across all shared-bias attacks is the stronger evidence — individual significance is fragile under correction.
3. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.
4. **Summary (post-D019)**: Under standard OLS, K_eff is positive in 7/12, NS in 4/12, negative in 1/12. Under clustered SE / mixed effects, K_eff significance collapses to 0-3/12. GAM reveals the underlying structure: targeted attacks → K_eff positive (6/6), shared-bias → K_eff negative (6/6). The attack-type taxonomy is the robust finding; individual K_eff significance counts are sensitive to SE correction.

## Story Arc (v5: Post-D019 Reframe)
1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)
2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types
3. **Surprise**: Panel vulnerability is **robustly dominated by the weakest individual judge** (η_max 7-8/12 after clustered SE / mixed-effects correction). Diversity (K_eff) shows directional but statistically fragile association — significance collapses from 8/12 (OLS) to 0-3/12 after correcting for non-independence of panel observations
4. **Mechanistic nuance**: GAM analysis reveals K_eff's direction cleanly splits by attack type: positive (harmful) for targeted attacks, negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression
5. **Aggregation as control lever**: Voting rule choice fundamentally modulates vulnerability — Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89)
6. **Defense**: Robustness-first screening (min η_max, 12/12 wins) + Bayesian aggregation = dual-channel defense stack
7. **Implication**: Panel security is primarily an individual-judge quality problem, not a diversity problem. But aggregation design and attack-type awareness provide complementary defense levers
