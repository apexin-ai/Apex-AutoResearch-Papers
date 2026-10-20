# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：15-model scaling + all planned experiments confirm and strengthen v5 framing

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/14cb1271-caba-4717-886f-c6b9167a4b05.jsonl`
- **Structured JSON:** [`84585d43ec6d7324b711.json`](../../sessions/84/84585d43ec6d7324b711.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T22:12:47.082Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T22:12:47.082Z",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：15-model scaling + all planned experiments confirm and strengthen v5 framing; η_max dominance survives every robustness check; GAM 6:6 split validated with bootstrapped CIs; new experiments add independent evidence lines\n核心假设：['plan_001 scaling to 15 models succeeds (DONE) AND remaining planned experiments (plan_003 RF contrast, plan_009 VIF, plan_010 aggregation expansion) produce consistent results', 'Wild cluster bootstrap η_max stays ≥5/12; clustered SE η_max stays ≥8/12', 'K_eff fragility confirmed: bootstrap ≤1/12, clustered SE ≤1/12 — clean separation from η_max', 'GAM 6:6 split survives bootstrapped CIs at ≥5/6 conditions per attack category', 'Random-fault experiment (plan_003) shows K_eff significant ≥2/2 — BFT contrast holds', 'Capability-matched validation (plan_004) shows K_eff emerges when η_max variance controlled', 'Aggregation gradient replicates under clustered SE: Bayesian still flips K_eff direction', 'No reviewer-blocking multicollinearity issue (VIF < 5 after residualization)']\n关键指标范围：{'eta_max_sig_bootstrap': [5, 8], 'eta_max_sig_clustered_se': [8, 11], 'keff_sig_bootstrap': [0, 1], 'keff_sig_clustered_se': [0, 1], 'eta_keff_dominance_ratio_bootstrap': [5, 11], 'gam_keff_split_targeted_positive': [5, 6], 'gam_keff_split_sharedbias_negative': [5, 6], 'rf_keff_sig': [2, 2], 'rf_r2': [0.7, 0.85], 'min_eta_max_wins': [12, 12], 'bayesian_keff_negative_frac': [5, 7], 'practical_delta_asr_keff_iqr_pp': [0.5, 2.0], 'diversity_capability_r': [0.65, 0.75]}\n叙事方向：Original framing fully sustained. Title 1/2 work as-is. Five-contribution stack intact: (1) η_max dominance with 5:1+ ratio is the headline; (2) K_eff fragility is a clean null — diversity doesn't independently matter after correcting for non-independence; (3) GAM 6:6 split is a validated mechanistic taxonomy; (4) RF contrast provides the BFT reversal evidence; (5) Aggregation gradient is a prescriptive lever. Methodological transparency section becomes a strength, not a hedge. Paper reads as a confident empirical contribution with actionable defense recommendations.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cert_manip_resist_eval\nvenue: emnlp-2026\nfocus: v5 post-trimming paper with 4 figures, 8 pages, all correction methods synced. Evaluate whether η_max dominance narrative and K_eff fragility framing are convincing with current evidence depth (1 successful experiment, bootstrap/clustered SE/mixed effects corrections).\n\n## paper_framing.md\n\n# Paper Framing — cert_manip_resist_eval (v5: Post-Clustered-SE Reframe, D019)\n\n> Last updated: 2026-05-22 | Reason: Bootstrap v2 (Reviewer-verified): η_max 5-11/12 (bootstrap 5/12 most reliable), K_eff 0-1/12. η_max:K_eff ratio 5:1 confirms dominance. GAM 6:6 split confirmed. Aggregation gradient independent.\n\n## Target\nEMNLP 2026 (via ARR)\n\n## Title Candidates\n1. \"The Weakest Judge Wins: What Really Drives LLM Evaluation Panel Vulnerability Under Adversarial Attack\"\n2. \"Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation\"\n3. \"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\" (softened with honest reporting)\n\n## Core Insight\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity. We conduct the first large-scale empirical study (15 models, 455 panels, 6 attacks, 2 benchmarks) decomposing panel vulnerability into individual weakness (η_max) and structural diversity (K_eff). Key findings: (1) **η_max dominates** panel vulnerability (5-11/12 conditions significant depending on correction method; wild cluster bootstrap — the most reliable method for small cluster counts — gives 5/12, with η_max:K_eff ratio of 5:1); (2) K_eff shows **directional but statistically fragile** association with vulnerability — point estimates predominantly positive (diversity increases risk), but significance collapses from 8/12 (OLS) to 0-1/12 after non-independence correction (bootstrap 1/12, clustered SE 0/12); (3) **GAM reveals a clean attack-type split**: K_eff is positive (harmful) for targeted attacks and negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression; (4) **Aggregation rule choice fundamentally modulates vulnerability**: Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89).\n\n## Hook\n\"Panel security against adversarial manipulation is dominated by the weakest individual judge — not panel diversity. But how you aggregate judges' votes determines whether diversity becomes a vulnerability or a defense.\"\n\n## Novelty Positioning\nWe do NOT claim diversity is harmful with high statistical confidence — K_eff's independent effect is directional but fragile under rigorous correction. Our contributions are:\n1. **First large-scale empirical decomposition** of panel vulnerability into η_max and K_eff in the LLM-judge domain (15 models, 455 panels), with transparent robustness analysis showing η_max dominates (5:1 over K_eff under bootstrap inference)\n2. **Attack-type taxonomy with clean mechanistic split**: GAM reveals K_eff positive for targeted attacks, negative for shared-bias attacks (6:6 split), explaining WHEN diversity helps vs hurts\n3. **Aggregation as a control lever**: voting rule modulates the diversity-vulnerability relationship — Bayesian reverses K_eff direction, threshold amplifies it (D017, independent of non-independence concern)\n4. **Robustness-first panel design**: min(η_max) strategy wins 12/12 conditions (Claim 6, unaffected by SE correction)\n5. **Structural barriers**: diversity-capability tradeoff (r=0.70), family label unreliability (confirmed at 15-model)\n6. **Alternative diversity metrics robustness**: η_max dominance holds across operationalizations — Q-stat only 2/12 sig (r=0.674 with K_eff), disagreement 8/12, κ-diversity 7/12. K_eff practical effect size: IQR → Δ ASR = 1.3pp (directional but practically small)\n7. **Methodological transparency**: explicit reporting of how significance changes across OLS → clustered SE → mixed effects, demonstrating the importance of accounting for panel overlap in combinatorial evaluation designs\n\n## Core Claims\n\n### Claim 1 (Primary): Weakest-Link Dominance\n**Statement**: Under adaptive adversarial attacks, panel vulnerability is **dominated by individual judge weakness (η_max)**. η_max remains significant in 5-8/12 conditions after non-independence correction (wild bootstrap 5/12, clustered SE 8/12, mixed effects 7/12). K_eff (diversity) shows directional association but significance is fragile (bootstrap 1/12, clustered SE 0/12). The η_max:K_eff dominance ratio is 5:1 under bootstrap — stronger than OLS's 11:8 ≈ 1.4:1.\n**Evidence** (15-model, 455 panels, 12 conditions, D019+D021):\n- **Regression spec**: log-log OLS: log(ASR + ε) ~ const + log(K_eff) + log(η_max + ε)\n- **Standard OLS**: η_max **11/12**, K_eff **8/12** (7+/1−) — inflated by panel non-independence\n- **Wild cluster bootstrap v2** (Reviewer-verified, B=9999, Rademacher, 3-position max-p): η_max **5/12**, K_eff **1/12** (mmlu×PI only) — conservative lower bound. Per-position analysis: position 0 gives 6/12 (cluster imbalance: claude-3-haiku=91 panels vs qwen2.5-14b=1), positions 1&2 each give **9/12** (more balanced clusters, consistent with clustered SE). Max-across-positions is legitimate conservative bound but tightened by position 0 imbalance.\n- **Clustered SE** (15 judge clusters, CR1): η_max **8/12**, K_eff **0/12** — consistent with per-position bootstrap 1&2\n- **Mixed effects** (random judge intercepts): η_max **7/12**, K_eff **3/12** (mmlu×PI, arc×PI, arc×PB)\n- SE inflation ~2.5x (consistent with 91/455 panel overlap)\n- Bootstrap η_max shows benchmark asymmetry: MMLU 4/6, ARC 1/6 survive. Likely cause: MMLU 4-choice format provides more scoring variance than ARC 2-choice, giving η_max more signal. arc×PI η_max completely lost (OLS p=3e-14 → bootstrap all NS) — signal was entirely from panel overlap.\n- **arc×sycophancy exception**: No longer significant under any correction (OLS p=0.013 → bootstrap 0.06 → clustered 0.441 → mixed 0.136). Reported as directional observation, not robust claim.\n- **Alternative diversity metrics (OLS)**: Q-stat 2/12, disagreement 8/12 (7+/1−), κ-diversity 7/12 (7+/0−). Q-stat (lowest correlation with K_eff, r=0.674) gives lowest diversity significance — further supports η_max as dominant driver regardless of diversity operationalization.\n- **Practical effect size**: K_eff IQR change → Δ ASR = 1.3pp (clustered SE CIs contain zero in 11/12 conditions). Even under OLS, diversity effect is practically small.\n**Strength**: η_max dominant (5:1 ratio over K_eff under bootstrap). Absolute significance lower than OLS (5/12 vs 11/12) but relative dominance stronger. K_eff directional but fragile and practically small.\n**Headline**: \"η_max dominates panel vulnerability (5:1 over K_eff); both channels inflated by panel non-independence, but η_max survives correction while K_eff does not.\"\n\n### Claim 1b (Secondary): Attack-Type Taxonomy — GAM 6:6 Split\n**Statement**: GAM analysis reveals that K_eff's direction cleanly splits by attack mechanism: **positive (diversity harmful) for targeted attacks** (prompt_injection, score_manipulation, position_bias × 2 benchmarks = 6 conditions) and **negative (diversity protective) for shared-bias attacks** (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions). This 6:6 pattern is masked by linear OLS which shows 7+/1−/4NS.\n**Evidence**: GAM partial effects, 455 panels, 12 conditions.\n- Targeted attacks (exploit judge-specific weaknesses): K_eff partial effect positive in all 6 conditions\n- Shared-bias attacks (exploit common cognitive biases): K_eff partial effect negative in all 6 conditions\n- **Caveat**: GAM significance of individual conditions needs clustered SE / bootstrapped CI (pending); the structural pattern is the main finding, not individual p-values\n**Strength**: Moderate-to-strong as qualitative taxonomic contribution. The clean 6:6 split provides mechanistic explanatory power beyond individual significance counts. Confirmed under correct 3/3/9 tier classification (GAM tier-fix rerun: all macro conclusions unchanged).\n\n### Claim 2 (Empirical): Predictability Gap — Panel Composition Explains RF But Not Adaptive Vulnerability\n**Statement**: Panel composition (η_max + K_eff) explains substantially more variance under random faults (R²=0.73-0.81) than under adaptive attacks (lower R²). K_eff is positively associated with vulnerability in BOTH regimes, but: under RF, this association is genuine (survives all corrections, 2/2); under adaptive, it is largely artifactual (0-1/12 after correction). Adaptive adversaries introduce strategic variance beyond what panel structure can predict.\n**Evidence** (15-model, 455 panels, D021+RF validation, Reviewer-verified):\n- **Random-fault regime** (error = 1 - clean_accuracy, Monte Carlo 10000):\n  - K_eff **positive** std_β = +0.215 (MMLU), +0.379 (ARC) — diversity associated with HIGHER error\n  - K_eff significant **2/2** under ALL correction methods (OLS, clustered SE, bootstrap)\n  - R² = 0.73-0.81 (highly predictable)\n- **Adaptive regime** (D021):\n  - K_eff also positive under OLS (7+/1−) but significance collapses to **0-1/12** after correction\n  - R² substantially lower\n- **Contrast**: NOT \"diversity helps under RF but hurts under adaptive\" — diversity is harmful in both. The contrast is: K_eff's harmful association is GENUINE under RF but INFLATED/ARTIFACTUAL under adaptive due to panel non-independence\n- ΔR² gap: RF regime is highly predictable from panel composition; adaptive regime is not\n**Correct interpretation**: Random faults are structurally determined by panel composition (hence high R² and genuine K_eff effect). Adaptive adversaries exploit weaknesses strategically, introducing variance that panel-level predictors cannot capture. K_eff in the adaptive regime appears significant under OLS only because of panel overlap inflation.\n**Strength**: Strong as predictability gap (R² contrast). The finding that K_eff is genuine under RF but artifactual under adaptive is a clean methodological insight about when non-independence correction matters most.\n\n### Claim 3 (Empirical): Diversity-Capability Tradeoff\n**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. The correlation r=+0.700 is a structural constraint — diversity and capability are partially opposed in the current model ecosystem.\n**Evidence**:\n- K_eff-η_max correlation: r = +0.700 (15-model)\n- Under standard OLS: K_eff significant 8/12 (7+/1−) after residualizing η_max\n- **D019 caveat**: Under clustered SE, K_eff drops to 0/12; mixed effects gives 3/12. The \"independent predictive effect\" of K_eff beyond η_max is directional but NOT statistically robust after correcting for non-independence. The structural correlation (r=0.700) itself is unaffected by SE correction — only the regression significance of K_eff as independent predictor changes.\n**Framing**: The tradeoff is real as a structural constraint (r=0.700). Whether K_eff has an independent causal effect beyond η_max cannot be confidently established from this data — K_eff's significance is fragile under correction, and the high confound makes disentanglement unreliable.\n**Strength**: Moderate (structural correlation strong; independent effect fragile). Causal language avoided.\n\n### Claim 4 (Methodological): Family Labels ≠ Diversity\n**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.\n**Evidence**:\n- 6-model: Mann-Whitney U p=0.206, permutation p=0.427\n- **15-model (confirmed)**: p=0.179 (MMLU), p=0.385 (ARC). 14 within-family pairs, 91 cross-family pairs. Still not significant.\n- Within-family MI variance is high (e.g., llama-70b↔8b MI only 0.05 due to capability gap > family similarity)\n**Strength**: Moderate. Consistent across 6→15 model scaling.\n\n### ~~Claim 5 (Methodological): Gaussian Copula Failure~~ → DOWNGRADED to observation\n**Original statement**: Gaussian copula systematically underestimates MI by 10-21×.\n**15-model result**: MI_obs/MI_gaussian mean ratio = **0.93** (MMLU), **0.90** (ARC, robust). Copula fits well at 15-model scale. The 6-model 10-21× was a small-sample artifact (15 pairs → 105 pairs, extreme values diluted). Only claude-3-haiku pairs show extreme ratios (212×) due to near-zero ρ with nonlinear dependence.\n**Disposition**: Remove as independent contribution. Optionally note in analysis: \"Gaussian copula fit is adequate for diverse model pools but breaks down for capability-mismatched pairs with nonlinear dependence.\"\n**Strength**: DEAD as independent claim. May retain as minor observation.\n\n### Claim 6 (Practical): Robustness-First Panel Design\n**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.\n**Evidence** (15-model, 455 panels — fully validated):\n- min(η_max) strategy dominates **12/12 conditions** (up from 5/6 at 6-model)\n- ASR advantage range: +0.038 (arc×sycophancy) to +0.511 (arc×prompt_injection)\n- Robust across panel sizes K=10, 20, 50\n- Even in the sole K_eff-dominant condition (arc×position_bias), min_eta_max still outperforms max_K_eff\n- Consistent with canonical regression: η_max 11/12 dominant\n**Strength**: Strong (15-model fully confirmed). Zero failure conditions.\n\n### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Both Vulnerability Drivers\n**Statement**: Bayesian calibration partially mitigates BOTH vulnerability drivers — weakening η_max dominance AND reversing K_eff from harmful to protective. Different aggregation rules create a gradient from full dual-driver vulnerability (threshold) to partial mitigation (Bayesian).\n**Evidence** (15-model, 455 panels, log-log canonical spec — D017, Reviewer-verified from JSON):\n- Majority: η_max **11/12**, K_eff **8/12** (7+/1−), R²=0.298 ← canonical baseline (matches dominance table ✓)\n- Weighted: η_max **9/12**, K_eff **9/12** (9+/0−), R²=0.284 — reduces both drivers but K_eff stays all positive\n- Threshold: η_max **12/12**, K_eff **11/12** (10+/1−), R²=**0.890** — near-perfect fit under unanimity\n- Bayesian: η_max **9/12** (↓), K_eff **7/12** (1+/**6 negative**), R²=0.104\n- Key findings:\n  - Bayesian weakens η_max (11→9/12) AND flips K_eff direction (majority 7+/1− → bayesian 1+/6−)\n  - Threshold amplifies both channels: η_max 12/12, K_eff 11/12, R²=0.89 (unanimity maximizes dual-driver predictability)\n  - Weighted reduces η_max (11→9/12) but K_eff stays all positive — accuracy weighting alone cannot reverse diversity harm\n  - Only Bayesian calibration reverses K_eff direction (6/7 significant coefficients negative)\n  - Aggregation gradient: threshold (max vulnerability) → majority → weighted → bayesian (min vulnerability)\n**Strength**: Strong (log-log canonical, Reviewer-verified, sanity-checked against Claim 1). Prescriptive: robustness-first selection (Claim 6) + Bayesian aggregation = dual-channel defense stack.\n\n## Contribution Stack (ordered by strength, post-D019 reframe)\n1. **Weakest-link dominance** — primary empirical (η_max robust 7-8/12 after all corrections; the strongest, most defensible finding)\n2. **Aggregation as control lever** — empirical+practical (D017: Bayesian reverses K_eff direction, weakens η_max; threshold amplifies both; R²=0.89. Independent of non-independence concern)\n3. **Attack-type taxonomy / GAM 6:6 split** — mechanistic (targeted=K_eff positive, shared-bias=K_eff negative; clean qualitative pattern; pending correct-tier validation)\n4. **Robustness-first panel design** — practical (Claim 6: min_eta_max 12/12 wins; unaffected by SE correction)\n5. **Methodological transparency on non-independence** — meta-contribution (demonstrating how OLS → clustered SE → mixed effects changes significance in combinatorial panel designs; useful for future work)\n6. **Diversity-capability tradeoff** — empirical (r=0.70; structural, not affected by SE correction)\n7. **Family label unreliability** — methodological (confirmed at 15-model scale)\n7. **Adaptive vs random-fault predictability gap** — empirical (R² gap)\n~~8. **Gaussian copula failure**~~ — REMOVED (falsified at 15-model scale; downgraded to minor observation)\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"K_eff positive is just confound with η_max\"\n**Response**: (a) Under standard OLS, K_eff is significant 8/12 (7+/1−), but after clustered SE correction K_eff drops to 0/12, mixed effects gives 3/12 — K_eff's independent effect is directionally positive but **statistically fragile**; (b) η_max remains robust at 7-8/12 under all corrections, confirming it is NOT a confound artifact; (c) GAM analysis reveals the K_eff direction cleanly splits by attack type (6:6 targeted vs shared-bias), suggesting real structure even if individual significance is fragile under correction; (d) We transparently report all three correction methods, which is itself a methodological contribution for combinatorial panel designs.\n\n### RC2: \"Why does diversity hurt? What's the mechanism?\"\n**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) GAM reveals the mechanism boundary: K_eff partial effect is positive for targeted attacks (6/6 conditions) and negative for shared-bias attacks (6/6 conditions). This clean split explains WHEN diversity helps vs hurts; (d) Note: K_eff's harmful direction is directional under OLS (7+/1−) but significance collapses under non-independence correction (0-3/12). The mechanism is real (GAM pattern), but its statistical strength is sensitive to correction — we report this transparently.\n\n### RC3: \"Only 15 models — does this generalize?\"\n**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).\n\n### RC4: \"BFT comparison is a strawman\"\n**Response**: (a) The implicit assumption \"more diverse judges = more robust\" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.\n\n### RC5: \"Why not just use the strongest models?\"\n**Response**: (a) \"Strongest\" varies by attack type; (b) K_eff is the sole significant predictor in 1 condition (arc×position_bias) — even all-strong panels can be vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.\n\n### RC6: \"No theoretical novelty\"\n**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.\n\n### RC7: \"Why not just use Bayesian aggregation?\"\n**Response**: (a) 15-model log-log canonical (D017, Reviewer-verified): Bayesian partially mitigates BOTH drivers — η_max drops to 9/12 (from 11/12), K_eff flips to 6/7 negative (protective). But it doesn't eliminate vulnerability: 9/12 η_max still significant, R² drops to 0.104 (residual vulnerability less predictable); (b) Requires clean accuracy prior which adaptive attackers could target; (c) Even under Bayesian, 9/12 conditions still show η_max vulnerability → robustness-first selection remains necessary; (d) Optimal defense stack: robustness-first selection (eliminates η_max) + Bayesian aggregation (flips K_eff to protective) = dual-channel coverage.\n\n### RC8: \"6-model and 15-model results contradict — which is right?\"\n**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff predominantly positive) has 23× more panels, wider capability range, and passes dominance analysis validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.\n\n### RC9 (new): \"arc×sycophancy exception undermines your claim\"\n**Response**: (a) Post-D019: arc×sycophancy K_eff is NOT significant after correction (OLS p=0.013 → clustered SE p=0.441 → mixed effects p=0.136). It is a directional observation, not a robust standalone finding; (b) However, GAM reveals that ALL shared-bias attacks (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions) show negative K_eff partial effects, while ALL targeted attacks (6 conditions) show positive — the 6:6 split is the robust pattern, not the individual significance of arc×sycophancy; (c) This gives practitioners an actionable taxonomy: targeted attacks → diversity hurts, shared-bias attacks → diversity may help; (d) The structural pattern (GAM) is more informative than individual p-values under various corrections.\n\n## \"When Diversity Helps\" Section\nDiversity IS beneficial under specific conditions — paper must present this as empirically grounded nuance, not just a hypothetical:\n1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary\n2. **Shared-bias attacks (GAM-confirmed pattern)**: GAM reveals K_eff partial effect is negative (protective) for all 6 shared-bias conditions (sycophancy, verbosity_bias, authority_bias × 2 benchmarks). Note: arc×sycophancy K_eff was significant under standard OLS (p=0.013) but **not significant after clustered SE (p=0.441) or mixed effects (p=0.136)**. The directional pattern across all shared-bias attacks is the stronger evidence — individual significance is fragile under correction.\n3. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.\n4. **Summary (post-D019)**: Under standard OLS, K_eff is positive in 7/12, NS in 4/12, negative in 1/12. Under clustered SE / mixed effects, K_eff significance collapses to 0-3/12. GAM reveals the underlying structure: targeted attacks → K_eff positive (6/6), shared-bias → K_eff negative (6/6). The attack-type taxonomy is the robust finding; individual K_eff significance counts are sensitive to SE correction.\n\n## Story Arc (v5: Post-D019 Reframe)\n1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)\n2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types\n3. **Surprise**: Panel vulnerability is **robustly dominated by the weakest individual judge** (η_max 7-8/12 after clustered SE / mixed-effects correction). Diversity (K_eff) shows directional but statistically fragile association — significance collapses from 8/12 (OLS) to 0-3/12 after correcting for non-independence of panel observations\n4. **Mechanistic nuance**: GAM analysis reveals K_eff's direction cleanly splits by attack type: positive (harmful) for targeted attacks, negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression\n5. **Aggregation as control lever**: Voting rule choice fundamentally modulates vulnerability — Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89)\n6. **Defense**: Robustness-first screening (min η_max, 12/12 wins) + Bayesian aggregation = dual-channel defense stack\n7. **Implication**: Panel security is primarily an individual-judge quality problem, not a diversity problem. But aggregation design and attack-type awareness provide complementary defense levers\n\n\n## experiment_plan (with registry status)\n\n- id: mvp_mi_matrix\n  claim: 4\n  description: Compute pairwise mutual information for 6 open-source judges on MMLU\n    and ARC. Validate Gaussian copula assumption.\n  priority: P0\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: mvp-step2-keff-contrast\n  notes: MI matrix computed. Gaussian copula underestimates MI by 10-21×. Family labels\n    do not predict MI (p=0.206).\n  status: DONE\n  conclusion: negative\n  metrics:\n    mmlu:\n      high_keff_asr: 0.2457\n      low_keff_asr: 0.1438\n      mann_whitney_p: 1\n    arc:\n      high_keff_asr: 0.1228\n      low_keff_asr: 0.078\n      mann_whitney_p: 1\n- id: mvp_regression\n  claim: 1\n  description: Multivariate regression log(ASR) ~ log(K_eff) + log(η_max) across 20\n    C(6,3) panels, 2 datasets, 3 attack types.\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: mvp-step2v3-retry3\n  notes: η_max significant 4/6 conditions; K_eff not significant 5/6. Weakest-link\n    dominates.\n  status: DONE\n  conclusion: negative\n  metrics:\n    regression_6conditions:\n      keff_sig_negative: 1\n      keff_sig_positive: 0\n      keff_nonsig: 5\n      eta_max_sig: 4\n    best_keff_result:\n      condition: arc×sycophancy\n      B_keff: -2.852\n      p_keff: 0.003\n      R2: 0.579\n    summary: eta_max dominates; K_eff not significant predictor in 5/6 conditions\n- id: mvp_taxonomy\n  claim: 1\n  description: 'Test K_eff on verbosity/position/authority bias attacks. Taxonomy\n    hypothesis: K_eff helps for shared-bias attacks.'\n  priority: P0\n  gpu_budget_hours: 15\n  deps: []\n  registry_id: taxonomy-broad-spectrum\n  notes: 0/6 new conditions K_eff significant. Taxonomy hypothesis falsified.\n  status: DONE\n  conclusion: negative\n  metrics:\n    keff_sig_negative: 0\n    keff_sig_positive: 1\n    keff_nonsig: 5\n    eta_max_sig: 3\n    worst_keff:\n      condition: mmlu×position\n      B: 3.357\n      p: 0.035\n      direction: WRONG (positive)\n    summary: 0/6 K_eff significant negative. Taxonomy hypothesis falsified.\n- id: plan_001\n  claim: 1\n  description: 'Scale expansion to 10-15 models. Add API models (GPT-4o-mini, GPT-4o,\n    GPT-4.1, GPT-4.1-mini) and large open-source (Llama-3.1-70B, Qwen2.5-72B). Rerun\n    MI matrix + regression on expanded panel set. Note: Claude/Gemini availability\n    TBD.'\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Validates weakest-link at scale. API endpoint may be OpenAI-only.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: Attack expansion to 6+ types. Add few-shot hijacking, persona manipulation,\n    instruction override. Run on full model pool.\n  priority: P1\n  gpu_budget_hours: 60\n  deps:\n  - plan_001\n  notes: Validates weakest-link universality across attack surface.\n  status: planned\n- id: plan_003\n  claim: 2\n  description: 'Random-fault simulation as BFT contrast experiment. Each judge fails\n    independently with prob η_j, majority vote. Show K_eff IS significant under random\n    faults (≥4/6 conditions) vs NOT significant under adaptive faults (11/12 already\n    shown). GO/NO-GO GATE: if random-fault K_eff also not significant → BFT framing\n    collapses.'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  notes: Anti-strawman lifeline. Uses existing individual judge ASR data.\n  status: planned\n- id: plan_004\n  claim: 3\n  description: Capability-matched validation. Within same capability tier (all 7B\n    or all 70B), test whether K_eff emerges as significant when η_max variance is\n    controlled.\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_005\n  claim: 6\n  description: 'Two-stage panel design algorithm benchmark. Robustness-first: (1)\n    filter η > threshold, (2) maximize K_eff. Benchmark vs 5 baselines. Dream flagged\n    marginal improvement over Strongest-K in all three tiers.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  notes: May need algorithm redesign given Dream observation of marginal gains.\n  status: planned\n- id: plan_006\n  claim: 1\n  description: Per-judge ASR concentration analysis. Measure per-judge ASR distribution\n    for each panel × attack. Compute Gini coefficient + entropy. Direct evidence for\n    adaptive adversary targeting.\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_007\n  claim: 3\n  description: Diversity-capability tradeoff visualization. Plot K_eff vs η_max across\n    all panels. Fit tradeoff curve. Pareto frontier. Stratify by tier.\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_008\n  claim: 1\n  description: Panel size sensitivity K=3,5,7,9. Test whether η_max dominance persists\n    as K grows.\n  priority: P2\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_009\n  claim: 1\n  description: VIF + multicollinearity analysis on existing data. Compute VIF, partial\n    correlations, residualized K_eff. Apply Bonferroni/FDR correction. Try beta regression.\n    Dream D3+D6.\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  notes: No GPU needed. Uses existing regression data.\n  status: planned\n- id: plan_010\n  claim: 1\n  description: Non-majority-vote aggregation. Test weakest-link under weighted voting,\n    veto rules, Bayesian aggregation. Dream D9.\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_011\n  claim: 1\n  description: Open-ended generation benchmark. Add MT-Bench or AlpacaEval-style task\n    beyond MCQ. Dream D11.\n  priority: P1\n  gpu_budget_hours: 40\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_012\n  claim: 2\n  description: Partial-knowledge adversary model. Adversary knows families but not\n    exact vulnerability profiles. Dream D12.\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_003\n  notes: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-step2-keff-contrast\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mmlu:\n      high_keff_asr: 0.2457\n      low_keff_asr: 0.1438\n      mann_whitney_p: 1\n    arc:\n      high_keff_asr: 0.1228\n      low_keff_asr: 0.078\n      mann_whitney_p: 1\n- exp_id: mvp-step2v3-regression\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-step2v3-retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-step2v3-retry2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-step2v3-retry3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    regression_6conditions:\n      keff_sig_negative: 1\n      keff_sig_positive: 0\n      keff_nonsig: 5\n      eta_max_sig: 4\n    best_keff_result:\n      condition: arc×sycophancy\n      B_keff: -2.852\n      p_keff: 0.003\n      R2: 0.579\n    summary: eta_max dominates; K_eff not significant predictor in 5/6 conditions\n- exp_id: taxonomy-broad-spectrum\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    keff_sig_negative: 0\n    keff_sig_positive: 1\n    keff_nonsig: 5\n    eta_max_sig: 3\n    worst_keff:\n      condition: mmlu×position\n      B: 3.357\n      p: 0.035\n      direction: WRONG (positive)\n    summary: 0/6 K_eff significant negative. Taxonomy hypothesis falsified.\n- exp_id: plan001_step1_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_full\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_full_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001_step1_full_v3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001_step1_full_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    models: 15\n    api_models: 9\n    local_models: 6\n    conditions: 126\n    samples_per_condition: 300\n    confound_mean_abs_r: 0.701\n    canonical_ols:\n      eta_max_fdr_sig: 11/12\n      keff_fdr_sig: 8/12\n      keff_sig_positive: 7\n      keff_sig_negative: 1\n    clustered_se:\n      eta_max_fdr_sig: 8/12\n      keff_fdr_sig: 0/12\n    mixed_effects:\n      eta_max_fdr_sig: 7/12\n      keff_fdr_sig: 3/12\n    wild_cluster_bootstrap_v2:\n      eta_max_fdr_sig: 5/12\n      keff_fdr_sig: 1/12\n      note: fixed K_eff + 3-position clustering\n    wild_cluster_bootstrap_v1_INVALID:\n      note: INVALIDATED\n    tier_indicator_corrected_3_3_9:\n      eta_max_fdr_sig: 11/12\n      keff_fdr_sig: 5/12\n    gam_corrected_3_3_9:\n      eta_max_fdr_sig: 12/12\n      keff_fdr_sig: 12/12\n      keff_sig_positive: 6\n      keff_sig_negative: 6\n    random_fault_corrected:\n      regime: RF\n      conditions: 2\n      ols:\n        eta_sig: 2/2\n        keff_sig: 2/2\n        mmlu_r2: 0.734\n        arc_r2: 0.813\n      clustered_se:\n        eta_sig: 2/2\n        keff_sig: 2/2\n      bootstrap_v2:\n        eta_sig: 2/2\n        keff_sig: 2/2\n      note: K_eff robust under RF, collapses under adaptive\n    alt_diversity:\n      Q_statistic:\n        eta_fdr_sig: 12/12\n        D_fdr_sig: 2/12\n      disagreement_rate:\n        eta_fdr_sig: 11/12\n        D_fdr_sig: 8/12\n      kappa_diversity:\n        eta_fdr_sig: 11/12\n        D_fdr_sig: 7/12\n    effect_size:\n      eta_std_beta:\n        mean: 0.387\n        sd: 0.179\n      keff_std_beta:\n        mean: 0.164\n        sd: 0.182\n      practical_delta_asr_keff_iqr:\n        mean: 0.0133\n        sd: 0.0164\n    min_eta_max_dominates: 12/12\n    aggregation_gradient:\n      majority:\n        eta_sig: 11/12\n        keff_sig: 8/12\n      weighted:\n        eta_sig: 9/12\n        keff_sig: 9/12\n      threshold:\n        eta_sig: 12/12\n        keff_sig: 11/12\n      bayesian:\n        eta_sig: 9/12\n        keff_sig: 7/12\n        keff_neg: 6\n- exp_id: plan001_step1_parallel_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_v4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_v5\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_final\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled_v4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled_v5\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_batched\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_batched_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T22:12:47.086Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T22:12:47.086Z",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-22T22:12:47.108Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：15-model scaling + all planned experiments confirm and strengthen v5 framing; η_max dominance survives every robustness check; GAM 6:6 split validated with bootstrapped CIs; new experiments add independent evidence lines
核心假设：['plan_001 scaling to 15 models succeeds (DONE) AND remaining planned experiments (plan_003 RF contrast, plan_009 VIF, plan_010 aggregation expansion) produce consistent results', 'Wild cluster bootstrap η_max stays ≥5/12; clustered SE η_max stays ≥8/12', 'K_eff fragility confirmed: bootstrap ≤1/12, clustered SE ≤1/12 — clean separation from η_max', 'GAM 6:6 split survives bootstrapped CIs at ≥5/6 conditions per attack category', 'Random-fault experiment (plan_003) shows K_eff significant ≥2/2 — BFT contrast holds', 'Capability-matched validation (plan_004) shows K_eff emerges when η_max variance controlled', 'Aggregation gradient replicates under clustered SE: Bayesian still flips K_eff direction', 'No reviewer-blocking multicollinearity issue (VIF < 5 after residualization)']
关键指标范围：{'eta_max_sig_bootstrap': [5, 8], 'eta_max_sig_clustered_se': [8, 11], 'keff_sig_bootstrap': [0, 1], 'keff_sig_clustered_se': [0, 1], 'eta_keff_dominance_ratio_bootstrap': [5, 11], 'gam_keff_split_targeted_positive': [5, 6], 'gam_keff_split_sharedbias_negative': [5, 6], 'rf_keff_sig': [2, 2], 'rf_r2': [0.7, 0.85], 'min_eta_max_wins': [12, 12], 'bayesian_keff_negative_frac': [5, 7], 'practical_delta_asr_keff_iqr_pp': [0.5, 2.0], 'diversity_capability_r': [0.65, 0.75]}
叙事方向：Original framing fully sustained. Title 1/2 work as-is. Five-contribution stack intact: (1) η_max dominance with 5:1+ ratio is the headline; (2) K_eff fragility is a clean null — diversity doesn't independently matter after correcting for non-independence; (3) GAM 6:6 split is a validated mechanistic taxonomy; (4) RF contrast provides the BFT reversal evidence; (5) Aggregation gradient is a prescriptive lever. Methodological transparency section becomes a strength, not a hedge. Paper reads as a confident empirical contribution with actionable defense recommendations.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: cert_manip_resist_eval
venue: emnlp-2026
focus: v5 post-trimming paper with 4 figures, 8 pages, all correction methods synced. Evaluate whether η_max dominance narrative and K_eff fragility framing are convincing with current evidence depth (1 successful experiment, bootstrap/clustered SE/mixed effects corrections).

## paper_framing.md

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


## experiment_plan (with registry status)

- id: mvp_mi_matrix
  claim: 4
  description: Compute pairwise mutual information for 6 open-source judges on MMLU
    and ARC. Validate Gaussian copula assumption.
  priority: P0
  gpu_budget_hours: 10
  deps: []
  registry_id: mvp-step2-keff-contrast
  notes: MI matrix computed. Gaussian copula underestimates MI by 10-21×. Family labels
    do not predict MI (p=0.206).
  status: DONE
  conclusion: negative
  metrics:
    mmlu:
      high_keff_asr: 0.2457
      low_keff_asr: 0.1438
      mann_whitney_p: 1
    arc:
      high_keff_asr: 0.1228
      low_keff_asr: 0.078
      mann_whitney_p: 1
- id: mvp_regression
  claim: 1
  description: Multivariate regression log(ASR) ~ log(K_eff) + log(η_max) across 20
    C(6,3) panels, 2 datasets, 3 attack types.
  priority: P0
  gpu_budget_hours: 20
  deps: []
  registry_id: mvp-step2v3-retry3
  notes: η_max significant 4/6 conditions; K_eff not significant 5/6. Weakest-link
    dominates.
  status: DONE
  conclusion: negative
  metrics:
    regression_6conditions:
      keff_sig_negative: 1
      keff_sig_positive: 0
      keff_nonsig: 5
      eta_max_sig: 4
    best_keff_result:
      condition: arc×sycophancy
      B_keff: -2.852
      p_keff: 0.003
      R2: 0.579
    summary: eta_max dominates; K_eff not significant predictor in 5/6 conditions
- id: mvp_taxonomy
  claim: 1
  description: 'Test K_eff on verbosity/position/authority bias attacks. Taxonomy
    hypothesis: K_eff helps for shared-bias attacks.'
  priority: P0
  gpu_budget_hours: 15
  deps: []
  registry_id: taxonomy-broad-spectrum
  notes: 0/6 new conditions K_eff significant. Taxonomy hypothesis falsified.
  status: DONE
  conclusion: negative
  metrics:
    keff_sig_negative: 0
    keff_sig_positive: 1
    keff_nonsig: 5
    eta_max_sig: 3
    worst_keff:
      condition: mmlu×position
      B: 3.357
      p: 0.035
      direction: WRONG (positive)
    summary: 0/6 K_eff significant negative. Taxonomy hypothesis falsified.
- id: plan_001
  claim: 1
  description: 'Scale expansion to 10-15 models. Add API models (GPT-4o-mini, GPT-4o,
    GPT-4.1, GPT-4.1-mini) and large open-source (Llama-3.1-70B, Qwen2.5-72B). Rerun
    MI matrix + regression on expanded panel set. Note: Claude/Gemini availability
    TBD.'
  priority: P0
  gpu_budget_hours: 80
  deps: []
  notes: Validates weakest-link at scale. API endpoint may be OpenAI-only.
  status: planned
- id: plan_002
  claim: 1
  description: Attack expansion to 6+ types. Add few-shot hijacking, persona manipulation,
    instruction override. Run on full model pool.
  priority: P1
  gpu_budget_hours: 60
  deps:
  - plan_001
  notes: Validates weakest-link universality across attack surface.
  status: planned
- id: plan_003
  claim: 2
  description: 'Random-fault simulation as BFT contrast experiment. Each judge fails
    independently with prob η_j, majority vote. Show K_eff IS significant under random
    faults (≥4/6 conditions) vs NOT significant under adaptive faults (11/12 already
    shown). GO/NO-GO GATE: if random-fault K_eff also not significant → BFT framing
    collapses.'
  priority: P0
  gpu_budget_hours: 5
  deps: []
  notes: Anti-strawman lifeline. Uses existing individual judge ASR data.
  status: planned
- id: plan_004
  claim: 3
  description: Capability-matched validation. Within same capability tier (all 7B
    or all 70B), test whether K_eff emerges as significant when η_max variance is
    controlled.
  priority: P1
  gpu_budget_hours: 20
  deps:
  - plan_001
  notes: ''
  status: planned
- id: plan_005
  claim: 6
  description: 'Two-stage panel design algorithm benchmark. Robustness-first: (1)
    filter η > threshold, (2) maximize K_eff. Benchmark vs 5 baselines. Dream flagged
    marginal improvement over Strongest-K in all three tiers.'
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_001
  notes: May need algorithm redesign given Dream observation of marginal gains.
  status: planned
- id: plan_006
  claim: 1
  description: Per-judge ASR concentration analysis. Measure per-judge ASR distribution
    for each panel × attack. Compute Gini coefficient + entropy. Direct evidence for
    adaptive adversary targeting.
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_001
  notes: ''
  status: planned
- id: plan_007
  claim: 3
  description: Diversity-capability tradeoff visualization. Plot K_eff vs η_max across
    all panels. Fit tradeoff curve. Pareto frontier. Stratify by tier.
  priority: P2
  gpu_budget_hours: 2
  deps:
  - plan_001
  notes: ''
  status: planned
- id: plan_008
  claim: 1
  description: Panel size sensitivity K=3,5,7,9. Test whether η_max dominance persists
    as K grows.
  priority: P2
  gpu_budget_hours: 30
  deps:
  - plan_001
  notes: ''
  status: planned
- id: plan_009
  claim: 1
  description: VIF + multicollinearity analysis on existing data. Compute VIF, partial
    correlations, residualized K_eff. Apply Bonferroni/FDR correction. Try beta regression.
    Dream D3+D6.
  priority: P0
  gpu_budget_hours: 0
  deps: []
  notes: No GPU needed. Uses existing regression data.
  status: planned
- id: plan_010
  claim: 1
  description: Non-majority-vote aggregation. Test weakest-link under weighted voting,
    veto rules, Bayesian aggregation. Dream D9.
  priority: P1
  gpu_budget_hours: 15
  deps:
  - plan_001
  notes: ''
  status: planned
- id: plan_011
  claim: 1
  description: Open-ended generation benchmark. Add MT-Bench or AlpacaEval-style task
    beyond MCQ. Dream D11.
  priority: P1
  gpu_budget_hours: 40
  deps:
  - plan_001
  notes: ''
  status: planned
- id: plan_012
  claim: 2
  description: Partial-knowledge adversary model. Adversary knows families but not
    exact vulnerability profiles. Dream D12.
  priority: P2
  gpu_budget_hours: 10
  deps:
  - plan_001
  - plan_003
  notes: ''
  status: planned


## registry (completed experiments)

- exp_id: mvp-step2-keff-contrast
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    mmlu:
      high_keff_asr: 0.2457
      low_keff_asr: 0.1438
      mann_whitney_p: 1
    arc:
      high_keff_asr: 0.1228
      low_keff_asr: 0.078
      mann_whitney_p: 1
- exp_id: mvp-step2v3-regression
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp-step2v3-retry
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp-step2v3-retry2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp-step2v3-retry3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    regression_6conditions:
      keff_sig_negative: 1
      keff_sig_positive: 0
      keff_nonsig: 5
      eta_max_sig: 4
    best_keff_result:
      condition: arc×sycophancy
      B_keff: -2.852
      p_keff: 0.003
      R2: 0.579
    summary: eta_max dominates; K_eff not significant predictor in 5/6 conditions
- exp_id: taxonomy-broad-spectrum
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    keff_sig_negative: 0
    keff_sig_positive: 1
    keff_nonsig: 5
    eta_max_sig: 3
    worst_keff:
      condition: mmlu×position
      B: 3.357
      p: 0.035
      direction: WRONG (positive)
    summary: 0/6 K_eff significant negative. Taxonomy hypothesis falsified.
- exp_id: plan001_step1_dryrun
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_dryrun2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_dryrun3
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_full
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_full_v2
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: plan001_step1_full_v3
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: plan001_step1_full_v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    models: 15
    api_models: 9
    local_models: 6
    conditions: 126
    samples_per_condition: 300
    confound_mean_abs_r: 0.701
    canonical_ols:
      eta_max_fdr_sig: 11/12
      keff_fdr_sig: 8/12
      keff_sig_positive: 7
      keff_sig_negative: 1
    clustered_se:
      eta_max_fdr_sig: 8/12
      keff_fdr_sig: 0/12
    mixed_effects:
      eta_max_fdr_sig: 7/12
      keff_fdr_sig: 3/12
    wild_cluster_bootstrap_v2:
      eta_max_fdr_sig: 5/12
      keff_fdr_sig: 1/12
      note: fixed K_eff + 3-position clustering
    wild_cluster_bootstrap_v1_INVALID:
      note: INVALIDATED
    tier_indicator_corrected_3_3_9:
      eta_max_fdr_sig: 11/12
      keff_fdr_sig: 5/12
    gam_corrected_3_3_9:
      eta_max_fdr_sig: 12/12
      keff_fdr_sig: 12/12
      keff_sig_positive: 6
      keff_sig_negative: 6
    random_fault_corrected:
      regime: RF
      conditions: 2
      ols:
        eta_sig: 2/2
        keff_sig: 2/2
        mmlu_r2: 0.734
        arc_r2: 0.813
      clustered_se:
        eta_sig: 2/2
        keff_sig: 2/2
      bootstrap_v2:
        eta_sig: 2/2
        keff_sig: 2/2
      note: K_eff robust under RF, collapses under adaptive
    alt_diversity:
      Q_statistic:
        eta_fdr_sig: 12/12
        D_fdr_sig: 2/12
      disagreement_rate:
        eta_fdr_sig: 11/12
        D_fdr_sig: 8/12
      kappa_diversity:
        eta_fdr_sig: 11/12
        D_fdr_sig: 7/12
    effect_size:
      eta_std_beta:
        mean: 0.387
        sd: 0.179
      keff_std_beta:
        mean: 0.164
        sd: 0.182
      practical_delta_asr_keff_iqr:
        mean: 0.0133
        sd: 0.0164
    min_eta_max_dominates: 12/12
    aggregation_gradient:
      majority:
        eta_sig: 11/12
        keff_sig: 8/12
      weighted:
        eta_sig: 9/12
        keff_sig: 9/12
      threshold:
        eta_sig: 12/12
        keff_sig: 11/12
      bayesian:
        eta_sig: 9/12
        keff_sig: 7/12
        keff_neg: 6
- exp_id: plan001_step1_parallel_dryrun
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_parallel_dryrun2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_parallel
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_parallel_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_parallel_v3
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_parallel_v4
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_parallel_v5
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_parallel_final
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_throttled
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_throttled_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_throttled_v3
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_throttled_v4
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_throttled_v5
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_v3
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_batched
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001_step1_batched_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: best
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "414b36a7-e4a8-414a-a676-bcebf61066e7",
  "type": "user",
  "uuid": "f7d56260-c97b-476e-8922-ed9206083371",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T22:12:47.106Z_

```json
{
  "parentUuid": "f7d56260-c97b-476e-8922-ed9206083371",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "17a98a47-2559-4e45-b8e6-774c04048de4",
  "timestamp": "2026-05-22T22:12:47.106Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T22:12:47.106Z_

```json
{
  "parentUuid": "17a98a47-2559-4e45-b8e6-774c04048de4",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "8c0d45d9-5a51-4e5e-8c11-064380246d6a",
  "timestamp": "2026-05-22T22:12:47.106Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T22:12:47.106Z_

```json
{
  "parentUuid": "8c0d45d9-5a51-4e5e-8c11-064380246d6a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "43041584-385e-4272-8755-12bf3cd4d70d",
  "timestamp": "2026-05-22T22:12:47.106Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：15-model scaling + all planned experiments confirm and strengthen v5 framing; η_max dominance survives every robustness check; GAM 6:6 split validated with…",
  "leafUuid": "43041584-385e-4272-8755-12bf3cd4d70d",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate η_max dominance and K_eff fragility at 15-model scale",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05"
}
```

---

### Assistant

_source line 9 · 2026-05-22T22:18:15.681Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "best" tier definition. Let me identify all planned experiments:

1. plan_001 - Scale expansion to 10-15 models (status: planned, but actually DONE based on registry plan001_step1_full_v4)
2. plan_002 - Attack expansion to 6+ types
3. plan_003 - Random-fault simulation as BFT contrast
4. plan_004 - Capability-matched validation
5. plan_005 - Two-stage panel design algorithm benchmark


6. plan_006 - Per-judge ASR concentration analysis
7. plan_007 - Diversity-capability tradeoff visualization
8. plan_008 - Panel size sensitivity K=3,5,7,9
9. plan_009 - VIF + multicollinearity analysis
10. plan_010 - Non-majority-vote aggregation
11. plan_011 - Open-ended generation benchmark
12. plan_012 - Partial-knowledge adversary model

Looking at the context more carefully, the user mentioned that Phase 1 already defined what "best" tier means, and the core assumptions for the best tier include plan_001 scaling to 15 models succeeding.

Plan_001 is marked as DONE in the registry, so I need to predict results for all the remaining planned experiments. The user wants detailed data expansion for each planned experiment in the experiment_plan. I'm checking which experiments actually have "planned" status — plan_001 shows as planned in the YAML but is already completed in the registry, so I need to identify which ones are truly still pending and generate predictions for those based on the best tier's defined metrics ranges. Looking at plan_002, the best-tier predictions would show η_max dominance holding across the new attack types, with the GAM split framework extending cleanly to handle them, while K_eff remains fragile under correction and the new attacks fit naturally into the existing targeted versus shared-bias taxonomy.

For plan_003, I need to clarify whether the random-fault simulation in plan_001 was comprehensive enough or if plan_003 represents a distinct follow-up experiment—the registry shows it as planned, so I'll treat it as a separate validation that should confirm K_eff significance across both conditions to contrast with the BFT results. The registry already shows plan_003 is essentially complete with 2/2 conditions meeting significance thresholds and strong R² values, so I'll treat it as done rather than planned. Now I'm laying out the expected outcomes for each remaining experiment: plan_002 should show η_max dominating the new attacks with clean GAM splits, plan_004 should reveal K_eff significance emerging when η_max variance is controlled within capability tiers, and plan_005 should demonstrate that robustness-first panel design outperforms the baseline approach.

Continuing through the rest, I expect plan_006 to confirm adversaries concentrate on the weakest judge through high Gini coefficients, plan_007 to produce a clean tradeoff curve around r≈0.70, plan_008 to show η_max persistence across all panel sizes, plan_009 to achieve VIF values below 5 after residualization, and plan_010 to replicate the aggregation gradient under clustered standard errors with Bayesian methods flipping K_eff significance. The final three plans should extend these patterns: plan_011 showing η_max dominance in generation tasks, plan_012 demonstrating η_max still prevails even with partial adversary knowledge, and now I'm moving into constructing the detailed YAML output with tables and figures.

But I need to check the user's definition of "best tier" more carefully—they want 15-model scaling plus all planned experiments confirming the v5 framing, η_max surviving every robustness check, the GAM 6:6 split validated with bootstrapped confidence intervals, and new experiments providing independent evidence. The core assumptions I'm working with are that plan_001 scaling is done and the remaining experiments produce consistent results, wild cluster bootstrap gives η_max at least 5/12, clustered SE gives at least 8/12, K_eff fragility stays below 1/12 under both methods, the GAM split holds across at least 5/6 conditions per attack category with bootstrapped CIs, and the random forest experiment shows K_eff significance in both cases.

Now I'm looking at the specific metric ranges I need to hit—η_max significance should fall between 5-8 for bootstrap and 8-11 for clustered SE, K_eff fragility needs to stay at 0-1 for both, the dominance ratio should be 5-11, the GAM splits need to hit 5-6 for both targeted positive and shared bias negative cases, random forest K_eff needs to be significant in both runs, R² should land between 0.7-0.85, and I need to verify that η_max wins in all 12 cases. I'm also tracking Bayesian K_eff negative fraction, practical ASR differences, and diversity-capability correlation targets.

The key question now is distinguishing which experiments are actually planned versus already completed—plan_001 is definitely done, but I need to clarify the status of the others. I need to figure out what each planned experiment should include—expected results, rationale for the best-tier predictions, data tables, figures, and analysis. I'm thinking through how to make these predictions internally consistent with the overall framing and the metric ranges I've established. Let me start mapping out plan_001 since it's already done and I can reference actual results, then move through plan_002 with the attack expansion and its new conditions across models and benchmarks.

For plan_002, I'm predicting that η_max will show significance in most of the new attack conditions under clustered standard errors, with bootstrap methods being more conservative. The three new attack types should map cleanly onto the GAM framework—few-shot hijacking and instruction override as targeted attacks exploiting individual model weaknesses, while persona manipulation hits shared vulnerabilities across models. The K_eff metric likely won't reach significance in these new conditions, maintaining the pattern from the original experiments. I'm also expecting the GAM split to hold or improve, keeping that clean separation between targeted and shared-bias attacks.

For plan_003, the random-fault BFT contrast should show K_eff reaching significance across both MMLU and ARC conditions under all correction methods, with R² values clustering in the 0.73–0.81 range to demonstrate that Byzantine-fault tolerance mechanisms explain the variance better than random noise.

For plan_004, I'm testing whether controlling η_max variance within capability tiers reveals K_eff as a meaningful signal. Within-tier panels should reduce η_max variance, potentially allowing K_eff to emerge as marginally significant in a few conditions, though η_max should still dominate overall even when variance is artificially constrained.

For plan_005, the two-stage panel design should show min(η_max) dominating across all 12 conditions, with the filtering-then-maximization approach yielding only marginal improvements—

quantified as percentage-point reductions in ASR.

For plan_006, I'm analyzing the concentration of attacks across judges using Gini coefficients and entropy: targeted attacks show high concentration (adversary focuses on the weakest judge), while shared-bias attacks spread more evenly, which supports the mechanistic story.

For plan_007, the diversity-capability correlation sits around 0.70, and the Pareto frontier clearly illustrates the tradeoff, with stratification patterns visible both within and across model tiers.

For plan_008, panel sizes of 3, 5, 7, and 9 all show η_max dominance, and while K_eff significance might increase slightly at larger panel sizes, the qualitative conclusions remain unchanged.

For plan_009, I'm checking multicollinearity with VIF analysis, confirming values stay below 5 after residualization.

For plan_010, the aggregation gradient holds up under clustered standard errors, and the Bayesian analysis shows K_eff flipping negative in most conditions with best performance at 6/7, while threshold aggregation amplifies both drivers.

For plan_011, I'm extending to open-ended generation tasks like MT-Bench or AlpacaEval to see if η_max dominance generalizes beyond multiple-choice questions and whether K_eff patterns differ.

For plan_012, even when the adversary has only family-level knowledge rather than full model knowledge, η_max still dominates, though the overall ASR decreases.

Now I'm setting up the YAML configuration and need to carefully define the metric ranges for the best tier. I'm examining the bootstrap and clustered standard error ranges across all the key metrics—eta_max significance, K_eff significance, dominance ratios, and the gamma splits for targeted and shared bias conditions. Now I'm looking at the specific target ranges for each metric in the best tier scenario, and I need to think about how to present this comprehensively for each experiment. Let me reconsider what the user is actually asking for—they want detailed data breakdowns for each planned experiment, so I should focus on organizing the results by experiment rather than just listing metrics. Writing YAML structure...

For plan_002, I'm working through how the new attack vectors—few-shot hijacking, persona manipulation, and instruction override—would distribute across the best tier conditions. With 6 additional conditions across 15 models and 2 benchmarks, I need to classify each as either shared-bias or targeted attacks to predict the GAM split, which will determine whether we see the η_max dominance pattern extend beyond the current 6:6 balance. would extend.

Actually, let me think through the attack categorization: few-shot hijacking is likely targeted since different judges have varying susceptibility to few-shot learning, persona manipulation could be a shared bias affecting all LLMs similarly, and instruction override varies by model so that's targeted. That gives me 2 targeted plus 1 shared-bias attack per benchmark, so 4 targeted and 2 shared-bias new conditions total. With the extended GAM, I'd have 10 targeted conditions with positive K_eff and 8 shared-bias with negative K_eff. Under the best tier, all should show clean results—10 targeted positive and 8 shared-bias negative.

Now I'm structuring the output and thinking through the table formats. For plan_001 since it's complete, I'll include the actual results. Plan_003 already has the random fault corrected data in the registry even though it's marked planned, so under best tier that confirms with full standalone analysis. I'm planning what tables would be most informative for each experiment—regression tables for the main plans, RF versus adaptive contrast comparison, within-tier analysis, and strategy comparisons.

Writing YAML now... Generating detailed YAML output... FDR correction's already in place and the results hold up consistently. For plan_010, the key finding under best conditions is that the aggregation gradient replicates even with clustered standard errors—Bayesian still flips K_eff's direction while threshold methods keep η_max dominant. This suggests the aggregation effect is robust and independent of the multicollinearity issue. I should verify whether plan_010 extends the existing aggregation gradient analysis from the registry or validates it under new conditions, then finalize the YAML output.

Writing the full experiment summary... attacks, panel sizes, and generation tasks. K_eff fragility is cleanly established: significant only under RF regime and select capability-matched conditions, never robust under adaptive attacks after correction. GAM 6:6 split extends to 10:8 with new attacks, validated by bootstrapped CIs. Five-contribution stack fully intact. Paper reads as a confident, methodologically transparent empirical contribution with prescriptive defense recommendations.

Now I'm reviewing the completed 15-model scaling experiment across 455 panels and 12 conditions. The results show eta_max significance holding at 11/12 under OLS, dropping to 5/12 with bootstrap validation, while K_eff remains fragile across methods. The dominance ratio stays at 5:1 favoring eta_max, confounding correlation sits at 0.701, and standard error inflation reaches roughly 2.5x—confirming the core findings hold under expanded model diversity. Generating results table... Now I'm structuring the complete YAML configuration for the experimental plans. For the attack surface expansion, I'm setting up six new conditions across three attack types—few-shot hijacking, persona manipulation, and instruction override—distributed between targeted and shared-bias categories. The GAM classification will include four new targeted attacks plus two shared-bias variants, with the extended GAM framework allocating ten targeted positive cases and eight shared-bias negative cases to maintain the dominance ratio structure.

I'm tracking the key metrics carefully: the original twelve conditions have well-defined ranges, but with plan_002 expanding to eighteen total conditions, I need to distinguish between metrics calculated for the original set versus the expanded set. The η_max signal shows thirteen out of eighteen conditions clustering under the standard error threshold, while K_eff remains at zero across all eighteen, indicating the new conditions provide clear differentiation without introducing confounding factors.

Writing YAML configuration... Writing YAML output... The two-stage approach shows only marginal gains over the baseline, outperforming five comparison strategies by a small margin. For the ASR concentration analysis, I'm computing Gini coefficients to measure how concentrated an adversary's attacks are within each panel—targeted attacks should show high Gini values around 0.7-0.85 while shared-bias attacks spread more evenly with lower Gini around 0.35-0.50. This directly tests the weakest-link hypothesis, and I expect strong correlation between panel Gini and η_max. Finally, I'm testing panel size sensitivity across K=3,5,7,9 to see how performance scales with more judges. Writing YAML configuration... Writing YAML structure...

For plan_003, I'm seeing that the RF results are already captured in the registry from plan001_step1_full_v4, so as a standalone experiment under the best tier, I should expand it to include more granular analysis like Monte Carlo simulations across different error rates and direct comparisons between RF and adaptive approaches, plus detailed breakdowns by condition.

Now I need to think through the causal mechanisms for each prediction's result_rationale—not just stating the numbers, but explaining why these tiers produce these outcomes. For plan_002's attack expansion, η_max dominates new attacks because those attack types like few-shot hijacking and instruction override specifically target model-specific instruction-following vulnerabilities that η_max is designed to exploit.

K_eff fails under the same panel-overlap mechanism as the original conditions—the correction reveals its independent contribution is too marginal to persist. GAM extends cleanly because the targeted versus shared-bias distinction reflects fundamental attack properties, not artifacts of the specific test set.

For plan_003 with random faults, K_eff becomes genuinely meaningful since random failures are truly independent by definition, making panel diversity a real redundancy mechanism where BFT actually holds. The contrast sharpens because under adaptive attacks, the independence assumption breaks down entirely.

In plan_004, K_eff only surfaces within capability tiers because η_max's variance shrinks when models are similarly capable, allowing K_eff's normally-masked signal to emerge—not because K_eff matters, but because η_max was previously dominating the regression. For plan_005, minimizing η_max directly targets the dominant vulnerability driver with a 5:1 ratio advantage, which is why min_eta_max wins consistently across all conditions.

For plan_006, targeted attacks concentrate vulnerability in the most susceptible judge (high Gini), while shared-bias attacks spread it across multiple judges (lower Gini) by exploiting common cognitive weaknesses. In plan_007, the ecosystem shows a structural r≈0.70 correlation between diversity and capability, meaning maximizing K_eff requires including models that trade off against each other.

For plan_008, the weakest-link mechanism remains dominant regardless of panel size because adversaries always target the most vulnerable judge—larger panels don't dilute this concentration, though K_eff might gain marginal statistical power. For plan_009, despite the 0.70 correlation between K_eff and η_max, log-log transformation and residualization keep VIF at acceptable levels (2.5-3.0), well below standard concern thresholds.

For plan_010, Bayesian calibration down-weights unreliable judges by prior accuracy, which neutralizes η_max's direct effect and allows K_eff's secondary effect to emerge as net negative under shared-bias conditions where diversity becomes protective. The aggregation gradient itself is a mathematical property of the voting rule, not an artifact of panel overlap—different rules genuinely produce different vulnerability profiles.

For plan_011, η_max extends to open-ended generation through the same weakest-link mechanism.

For plan_012, even with family-level knowledge only, the adversary's attacks remain biased toward individual weaknesses since family labels partially correlate with vulnerability profiles, preserving the structural dominance of η_max despite noisier targeting.

Now I need to construct the complete YAML and verify that predicted metric values are internally consistent across all plans.

I'm also mapping out appropriate visualizations for each experiment: SE inflation heatmaps and p-value comparisons for plan_001, extended GAM effects and attack taxonomy heatmaps for plan_002, RF versus adaptive contrast comparisons for plan_003, within-tier regression analysis for plan_004, strategy radar charts for plan_005, Gini coefficient distributions and ASR concentration patterns for plan_006, and K_eff versus η_max scatter plots for plan_007.

Continuing with the remaining experiments: plan_008 will show η_max and K_eff significance across different panel sizes, plan_009 will display VIF changes before and after residualization, plan_010 will present aggregation gradients under clustered standard errors, plan_011 will compare MCQ versus generation tasks with η_max dominance patterns, and plan_012 will contrast full versus partial knowledge ASR with driver importance analysis.

Now I'm ready to write out the complete YAML configuration. I need to be careful about the within-tier structure for plan_004 since the tier sizes are quite small—frontier tier has around 4-5 models, which will create much tighter panels than the full dataset.

Writing YAML configuration... for tier 3 (9 models → 84 panels). Under best tier, K_eff might emerge as significant in 2-3/12 conditions within this tier.

Actually, maybe for plan_004 I should also consider panels of same-size models: all 7B, all 13-14B, all 70B+. This gives more nuance.

OK, for the YAML I'll just note the overall results without getting into too much structural detail about which specific tiers. The result_rationale will explain the mechanism.

Let me also look at the 15 models more carefully from the registry: API models like GPT-4o-mini, GPT-4o, GPT-4.1, GPT-4.1-mini, claude-3-haiku, and possibly others make up about 9, while local models account for the remaining 6. Under the 3:3:9 tier split, the tiers are presumably tier 1 with 3 frontier models (GPT-4o, GPT-4.1, claude-3.5-sonnet), tier 2 with 3 mid-range models (GPT-4o-mini, GPT-4.1-mini, Llama-3.1-70B), and tier 3 with 9 base models (various 7B/8B/14B models). For capability-matched validation, I'll focus on the 9-model base tier (84 panels) as the primary analysis.

I'm definitely overthinking this. The user wants detailed predictions, not perfect structural analysis. Let me just write the YAML now and be detailed but move forward. My final output plan is to structure it with tier: best and narrative_guidance as 2-3 sentences.

Now I'm planning out 12 imagined experiments (plan_001 through plan_012), each with around 10-15 expected_results metrics, a result_rationale paragraph, 1-2 tables, 1-2 figures, and an analysis paragraph. This will total roughly 400-500 lines of YAML.

For plan_010 specifically, which focuses on non-majority-vote aggregation testing weakest-link under weighted voting, veto rules, and Bayesian aggregation, I need to consider what's new beyond the existing registry methods. I'm thinking veto rules are the novel addition, plus running all aggregation methods under clustered standard errors and bootstrap resampling rather than just OLS, and possibly adding median aggregation. Under the best tier, I expect the aggregation gradient to replicate under clustered SE, Bayesian K_eff to still flip under correction, and veto rules to show distinct behavior.

Writing YAML experiments... Looking at the clustered standard error results across aggregation methods, the pattern becomes clearer — threshold and Bayesian methods preserve more K_eff signal than majority or weighted approaches, while veto shows extreme η_max dominance since a single judge can override everything. Under best tier with clustered SE applied uniformly, the aggregation gradient should reveal itself more distinctly, and I'm ready to finalize the predictions for plan_010.

Now examining how these results shift under bootstrap resampling — the η_max values drop substantially across all methods, with majority and weighted collapsing to 4-5/12, while threshold and Bayesian maintain slightly higher values at 8/12 and 3/12 respectively, suggesting bootstrap is more conservative about detecting structural effects. max 9/12, K_eff 0/12

Hmm, these numbers need to make sense. Let me think more carefully.

Under threshold voting (unanimity), every judge must agree. This creates a much stronger structural effect — one bad judge ruins everything. So η_max should be extremely significant and K_eff might also be significant because more diverse panels have more chances of having one resistant judge. Wait, but K_eff significance in threshold is 11/12 under OLS. Under clustered SE, some of this would collapse but not all, because threshold creates a genuine structural amplification of both η_max and K_eff.

Actually, the key insight is that threshold voting's R²=0.89 means 89% of variance is explained. This strong structural relationship might survive correction better than majority voting's R²=0.298. So under clustered SE, threshold might retain more significance.

Let me revise my expectations across all methods. Majority voting shows η_max at 8/12 and K_eff at 0/12 with weak explanatory power. Weighted voting is similarly weak at 6/12 and 1/12. Threshold voting stands out dramatically with η_max at 11/12 and K_eff at 5/12, driven by that very strong R² of 0.89. Bayesian aggregation is quite weak overall with mostly insignificant coefficients, though K_eff flips direction. Veto power shows the pure weakest-link structure with η_max fully significant but K_eff barely.

Now the question is whether the panel overlap issue — which inflates standard errors uniformly across methods by roughly 2.5x — will substantially erode these patterns. For threshold voting especially, even with that SE inflation, the structural signal from R²=0.89 should be robust enough to preserve significance. strong signal should survive.

Actually, for threshold, the t-statistics would be very high given R²=0.89. Even with 2.5x SE inflation, many would survive. So 11/12 → maybe 9-10/12 for η_max and 11/12 → maybe 4-6/12 for K_eff.

For Bayesian with R²=0.104, the signals are weak to begin with. η_max 9/12 → maybe 4-5/12. K_eff 7/12 → maybe 3-4/12.

Let me settle on:
Under clustered SE:
- Majority: η_max 8/12, K_eff 0/12
- Weighted: η_max 6/12, K_eff 1/12
- Threshold: η_max 10/12, K_eff 4/12 (3+/1-)
- Bayesian: η_max 5/12, K_eff 4/12 (1+/3-)
- Veto: η_max 11/12, K_eff 0/12

This maintains the gradient pattern and shows Bayesian K_eff direction flip survives correction. The key finding is that under plan_010, the Bayesian K_eff flip is genuine and confirms aggregation as an independent control lever. Now I'm ready to finalize the YAML with internally consistent numbers—the Bayesian K_eff metric should show 5-7 out of 7 significant conditions as negative under the best tier definition, which aligns with the 4/12 significant K_eff cases under clustered SE.

For plan_011 with open-ended generation on MT-Bench, I need to account for different evaluation dynamics: judges score free-form responses on continuous scales rather than binary choices, introducing more variance and making style-based adversarial attacks potentially more effective than content manipulation.

Under best tier conditions, η_max remains significant across 3-4 out of 6 scenarios under clustered standard errors, while K_eff shows minimal signal at 0-1 conditions. The R² likely decreases due to noisier evaluation, and the GAM pattern still holds but less cleanly. This confirms η_max dominance extends to generation tasks.

For plan_012 with a partial knowledge adversary limited to family labels, the attack becomes noisier and overall attack success rates drop by 15-25% compared to full information. Despite this constraint, η_max preserves its relative importance across 4-5 out of 6 conditions, though K_eff might capture slightly more signal since partial knowledge means diversity offers some obfuscation value. This validates that η_max remains the dominant factor even under realistic threat models.

Now I'm clarifying the panel size implications for plan_008, which tests K values of 3, 5, 7, and 9 against 15 models. Larger K values generate exponentially more panels—from 455 at K=3 up to 6435 at K=7—which increases statistical power but also compounds panel overlap and standard error inflation. Across all K values, η_max continues to dominate, though K_eff might show slightly more significance at larger K due to increased statistical power from more panels.

Writing YAML config... Writing YAML structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43041584-385e-4272-8755-12bf3cd4d70d",
  "isSidechain": false,
  "requestId": "req_011CbJNjz87ctMaGeaeZjMMi",
  "type": "assistant",
  "uuid": "4b0af82f-c042-4f6a-9cd0-19358630a686",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tggzv1WwzJF1PYj4rihDKK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17908,
      "cache_read_input_tokens": 11447,
      "output_tokens": 30385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17908,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 30385,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17908
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-22T22:23:14.023Z_

```yaml
tier: best
narrative_guidance: >-
  所有 planned 实验均确认并强化 v5 framing。η_max 在新攻击类型、面板尺寸、生成任务中全面主导；
  K_eff 脆弱性在每种校正方法下稳定复现。RF 对照实验提供 BFT 反转的干净因果证据；
  GAM 6:6 分割在 bootstrapped CIs 下通过验证并扩展至新攻击类型；聚合梯度在 clustered SE 下复现，
  Bayesian 翻转 K_eff 方向这一发现被确认为真实效应而非统计伪迹。五贡献堆栈完整无缺，
  论文作为一项自信的实证贡献交付，附带可操作的防御建议和方法论透明性。

imagined_experiments:

  - name: "15-Model Scaling Expansion"
    plan_id: "plan_001"
    description: "扩展至 15 模型（6 families），455 panels × 12 conditions 全量回归 + MI 矩阵 + 所有校正方法"
    expected_results:
      status: "DONE (plan001_step1_full_v4)"
      models: 15
      panels: 455
      conditions: 12
      eta_max_sig_ols: "11/12"
      keff_sig_ols: "8/12 (7+/1-)"
      eta_max_sig_clustered_se: "8/12"
      keff_sig_clustered_se: "0/12"
      eta_max_sig_bootstrap_v2: "5/12"
      keff_sig_bootstrap_v2: "1/12"
      eta_max_sig_mixed_effects: "7/12"
      keff_sig_mixed_effects: "3/12"
      dominance_ratio_bootstrap: "5:1"
      gam_split: "6 targeted positive / 6 shared-bias negative"
      min_eta_max_wins: "12/12"
      confound_r: 0.701
      se_inflation_factor: "~2.5x"
      rf_keff_sig: "2/2"
      rf_r2_mmlu: 0.734
      rf_r2_arc: 0.813
    result_rationale: >-
      已完成。15 模型覆盖 6 families × 3 capability tiers，提供 η_max 和 K_eff 充足方差。
      SE 膨胀 ~2.5x 与 91/455 panel overlap 一致（claude-3-haiku 出现在 91 个 panels 中）。
      η_max 存活校正因为它捕捉的是真实的个体 judge 脆弱性——不是 panel 重叠伪迹。
      K_eff 崩溃因为其 OLS 显著性被 overlapping panels 的相关残差膨胀——clustered SE
      控制共享 judge 成员关系后，K_eff 的独立信号太弱。GAM 6:6 分割源于攻击机制差异：
      targeted attacks 利用 judge 特异性弱点（diversity = 更多攻击面），shared-bias attacks
      利用共性认知偏差（diversity = 部分 judges 免疫）。
    tables:
      - name: "Correction Method Comparison (Actual Results)"
        columns: ["Method", "η_max sig", "K_eff sig", "K_eff dir", "Note"]
        rows:
          - ["OLS", "11/12", "8/12", "7+/1-", "Panel overlap inflated"]
          - ["Clustered SE (CR1, 15 clusters)", "8/12", "0/12", "-", "Conservative"]
          - ["Wild cluster bootstrap v2", "5/12", "1/12", "1+", "Max-p across 3 positions"]
          - ["Mixed effects", "7/12", "3/12", "3+", "Random judge intercepts"]
    figures_description:
      - "已生成：OLS vs corrected p-value 对比热图，12 conditions × 4 methods"
    analysis: >-
      已完成。η_max:K_eff 主导比从 OLS 的 1.4:1 升至 bootstrap 的 5:1，证明相对主导性在校正下
      增强而非减弱。Benchmark 不对称（MMLU 4/6 vs ARC 1/6 存活 bootstrap）由 MMLU 4-choice
      格式提供更多 scoring variance 解释。此结果构成 paper 的实证基础。

  - name: "Attack Surface Expansion"
    plan_id: "plan_002"
    description: "新增 3 种攻击类型（few-shot hijacking, persona manipulation, instruction override），在 15 模型 × 2 benchmarks 上运行，共 6 新 conditions"
    expected_results:
      new_attack_types: 3
      new_conditions: 6
      total_conditions: 18
      new_eta_max_sig_ols: "6/6"
      new_keff_sig_ols: "4/6 (3+/1-)"
      new_eta_max_sig_clustered_se: "5/6"
      new_keff_sig_clustered_se: "0/6"
      new_eta_max_sig_bootstrap: "3/6"
      new_keff_sig_bootstrap: "0/6"
      combined_eta_max_sig_clustered_se: "13/18"
      combined_keff_sig_clustered_se: "0/18"
      combined_dominance_ratio_clustered_se: "13:0"
      gam_extended_split: "10 targeted positive / 8 shared-bias negative"
      gam_new_attacks_classification:
        few_shot_hijacking: "targeted (positive K_eff)"
        persona_manipulation: "shared-bias (negative K_eff)"
        instruction_override: "targeted (positive K_eff)"
      new_r2_range: [0.22, 0.45]
      min_eta_max_wins_extended: "18/18"
    result_rationale: >-
      Few-shot hijacking 利用模型在 in-context learning 上的个体差异——不同 judges 对 few-shot
      示例的敏感度差异极大（GPT-4.1 vs Llama-8B 可差 3-5x），因此属于 targeted attack，η_max
      捕捉最易受影响的 judge。Instruction override 利用 instruction-following 能力的模型间方差，
      同样属于 targeted。Persona manipulation 利用 LLMs 对权威/身份线索的普遍敏感性——这是一种
      共享认知偏差，不同能力模型都会受影响，因此属于 shared-bias，K_eff 方向为负（diversity 提供
      部分免疫）。新攻击在 OLS 下延续 η_max 主导模式，但 K_eff 再次因 panel overlap 膨胀而
      显著——clustered SE 后归零，与原 12 conditions 完全一致。GAM 扩展至 10:8 分割，clean
      taxonomy 覆盖 9 种攻击类型。
    tables:
      - name: "Extended Attack Taxonomy (Clustered SE)"
        columns: ["Attack Type", "Mechanism", "Benchmark", "η_max sig?", "K_eff sig?", "K_eff GAM direction"]
        rows:
          - ["few-shot hijacking", "targeted", "MMLU", "Yes", "No", "positive"]
          - ["few-shot hijacking", "targeted", "ARC", "Yes", "No", "positive"]
          - ["persona manipulation", "shared-bias", "MMLU", "Yes", "No", "negative"]
          - ["persona manipulation", "shared-bias", "ARC", "Yes", "No", "negative"]
          - ["instruction override", "targeted", "MMLU", "Yes", "No", "positive"]
          - ["instruction override", "targeted", "ARC", "No", "No", "positive"]
      - name: "Extended GAM Split Summary"
        columns: ["Category", "Original (6 attacks)", "New (3 attacks)", "Total", "K_eff direction"]
        rows:
          - ["Targeted", "6/6 positive", "4/4 positive", "10/10", "positive (diversity harmful)"]
          - ["Shared-bias", "6/6 negative", "2/2 negative (persona×2)", "8/8", "negative (diversity protective)"]
    figures_description:
      - "Extended GAM partial effect heatmap: 9 attack types × 2 benchmarks, color-coded by K_eff direction"
      - "η_max dominance ratio bar chart: original 12 vs extended 18 conditions under each correction method"
    analysis: >-
      新攻击类型提供独立证据线，确认 η_max 主导性不依赖于特定攻击选择。GAM taxonomy 从 6:6 扩展至
      10:8，mechanistic split 的稳健性增强——审稿人无法再质疑 taxonomy 是 cherry-picked 6 种
      攻击的巧合。Instruction override 在 ARC 上 η_max 未显著（ARC 2-choice 格式对 instruction
      override 的 judge 间方差不敏感），与原始 benchmark asymmetry 一致。论文标题和核心叙事完全支持。

  - name: "Random-Fault BFT Contrast Experiment"
    plan_id: "plan_003"
    description: "Monte Carlo 随机故障模拟作为 BFT 对照。每个 judge 以 η_j = 1 - clean_accuracy 独立失败，majority vote。对比 adaptive regime 证明 BFT 反转"
    expected_results:
      regime: "Random Fault (i.i.d.)"
      conditions: 2
      monte_carlo_iterations: 10000
      rf_keff_sig_ols: "2/2"
      rf_keff_sig_clustered_se: "2/2"
      rf_keff_sig_bootstrap: "2/2"
      rf_keff_direction: "positive (2/2)"
      rf_keff_std_beta_mmlu: 0.215
      rf_keff_std_beta_arc: 0.379
      rf_eta_sig_all_methods: "2/2"
      rf_r2_mmlu: 0.78
      rf_r2_arc: 0.81
      adaptive_keff_sig_clustered_se: "0/12"
      adaptive_keff_sig_bootstrap: "1/12"
      delta_r2_rf_vs_adaptive: 0.48
      go_nogo_gate: "PASS (RF K_eff ≥2/2)"
    result_rationale: >-
      随机故障下 K_eff 显著的根本原因是 BFT 的 i.i.d. 假设成立：每个 judge 独立以固定概率犯错，
      panel 结构（多样性）直接影响冗余覆盖。K_eff 高的 panel 中 judges 的错误模式更不相关，
      majority vote 的容错能力与独立性成正比——这正是 BFT 的核心机制。K_eff 方向为正（diversity
      → higher error）因为高 K_eff panel 必然包含弱模型（r=0.70 tradeoff），而在 i.i.d. 体制下
      弱模型的高错误率直接传导为 panel 错误率——但关键是 K_eff 的贡献是独立的、真实的（所有校正
      方法均显著 2/2）。对照 adaptive regime：相同的 K_eff 在 OLS 下显著 8/12，但 clustered SE
      后崩溃至 0/12——因为 adaptive adversary 引入了 panel 结构无法预测的策略方差，K_eff 的
      apparent OLS 信号完全来自 panel overlap 膨胀。R² 差异（RF 0.78-0.81 vs adaptive ~0.30）
      直接量化了 adaptive adversary 引入的不可预测性。GO/NO-GO gate 通过，BFT framing 得到
      因果层面的支撑。
    tables:
      - name: "RF vs Adaptive Contrast (Key Metrics)"
        columns: ["Metric", "Random Fault", "Adaptive", "Interpretation"]
        rows:
          - ["K_eff sig (OLS)", "2/2", "8/12 (7+/1-)", "Both appear significant under OLS"]
          - ["K_eff sig (Clustered SE)", "2/2", "0/12", "RF genuine; adaptive artifactual"]
          - ["K_eff sig (Bootstrap v2)", "2/2", "1/12", "Consistent contrast"]
          - ["K_eff std β (mean)", "+0.297", "+0.164", "RF effect larger and genuine"]
          - ["R²", "0.78-0.81", "0.25-0.35", "RF structurally determined; adaptive not"]
          - ["η_max sig (all methods)", "2/2", "5-8/12", "η_max genuine in both regimes"]
      - name: "RF Per-Benchmark Detail"
        columns: ["Benchmark", "η_max β", "K_eff β", "R²", "K_eff p (bootstrap)"]
        rows:
          - ["MMLU", "+0.482", "+0.215", "0.78", "0.003"]
          - ["ARC", "+0.551", "+0.379", "0.81", "<0.001"]
    figures_description:
      - "Dual-panel figure: (Left) coefficient comparison RF vs adaptive for η_max and K_eff with 95% CIs; (Right) R² comparison bar chart showing RF >> adaptive"
      - "Scatter plot: predicted vs actual error rate under RF regime showing tight fit (R²≈0.80) vs adaptive regime showing wide dispersion"
    analysis: >-
      这是论文的关键因果证据。RF 对照证明 K_eff 在满足 i.i.d. 假设时有真实效应——BFT 理论
      在随机故障下成立。而 adaptive regime 下 K_eff 的 OLS 显著性完全是 panel overlap 的伪迹。
      这不是"diversity helps under RF but hurts under adaptive"——K_eff 在两种 regime 下方向均
      为正。区别是：RF 下 K_eff 的正关联是真实的（panel 结构决定了容错性），adaptive 下是膨胀的
      （adversary 引入的策略方差使 panel 结构预测力崩溃）。此发现为 Contribution #2（BFT
      reversal evidence）提供了不可替代的因果论证。

  - name: "Capability-Matched Validation"
    plan_id: "plan_004"
    description: "在同一 capability tier 内（主要利用 9-model base tier, 84 panels）测试控制 η_max 方差后 K_eff 是否浮现为显著预测因子"
    expected_results:
      primary_tier: "base (9 models, 84 panels)"
      within_tier_eta_max_variance_reduction: "65-70%"
      within_tier_keff_eta_max_r: 0.35
      conditions: 12
      within_tier_keff_sig_ols: "5/12"
      within_tier_keff_sig_clustered_se: "2/12"
      within_tier_keff_direction: "4+/1-"
      within_tier_eta_max_sig_ols: "7/12"
      within_tier_eta_max_sig_clustered_se: "4/12"
      within_tier_dominance_ratio: "2:1"
      within_tier_r2_mean: 0.18
      cross_tier_comparison:
        full_pool_dominance_ratio: "5:1"
        within_tier_dominance_ratio: "2:1"
        interpretation: "η_max still dominant but K_eff gains relative signal"
    result_rationale: >-
      在同一 capability tier 内，η_max 方差降低约 65-70%（因为同 tier 模型能力接近），而 K_eff
      方差保持（同 tier 模型仍来自不同 families/architectures）。η_max 和 K_eff 的 confound
      从 r=0.70（全池）降至 r≈0.35（tier 内），解开了回归中的多重共线性。在此条件下，K_eff
      的边际信号——通常被 η_max 的强效应淹没——变得可检测。OLS 下 5/12 显著；clustered SE 后
      保留 2/12，表明 K_eff 有微弱但真实的独立效应。主导比从 5:1 降至 2:1，但 η_max 仍然
      主导。这支持论文叙事：K_eff 有方向性关联但在全池分析中被 η_max 压倒——当人为控制 η_max
      方差时 K_eff 才浮现，这恰恰说明在自然变异条件下 η_max 是主要驱动因素。此外，within-tier
      R² 均值仅 0.18，说明 tier 内的面板脆弱性预测力大幅下降——进一步证明 η_max 的跨 tier
      方差是预测力的主要来源。
    tables:
      - name: "Cross-Tier vs Within-Tier Comparison"
        columns: ["Setting", "Panels", "K_eff-η_max r", "η_max sig (CL-SE)", "K_eff sig (CL-SE)", "Ratio", "R² mean"]
        rows:
          - ["Full pool (15 models)", "455", "0.70", "8/12", "0/12", "8:0", "0.30"]
          - ["Base tier (9 models)", "84", "0.35", "4/12", "2/12", "2:1", "0.18"]
          - ["Frontier tier (3 models)", "1", "-", "-", "-", "-", "-"]
      - name: "Within-Tier K_eff Significant Conditions"
        columns: ["Condition", "K_eff β", "K_eff p (CL-SE)", "Direction", "GAM confirms?"]
        rows:
          - ["mmlu×prompt_injection", "+0.31", "0.028", "positive", "Yes (targeted)"]
          - ["mmlu×score_manipulation", "+0.25", "0.041", "positive", "Yes (targeted)"]
    figures_description:
      - "Coefficient forest plot: full pool vs within-tier, showing η_max shrinkage and K_eff emergence"
      - "K_eff-η_max scatter: full pool (r=0.70) vs base tier (r=0.35), demonstrating confound reduction"
    analysis: >-
      Capability-matched validation 提供了 disentangle η_max 和 K_eff 的准自然实验。关键发现：
      即使在控制 η_max 方差后，K_eff 仍然是次要驱动因素（2:1 而非 1:1 或 K_eff 主导）。
      论文可表述为："当 capability 差异被控制时，diversity 浮现为统计上可检测的次要因素——但在
      自然 panel 组合中，capability 差异（通过 η_max）压倒性地主导脆弱性。"这强化了
      robustness-first 设计建议：先筛选 capability，再在筛选后的池中考虑 diversity。

  - name: "Two-Stage Panel Design Algorithm Benchmark"
    plan_id: "plan_005"
    description: "实现 robustness-first 两阶段算法（filter η > threshold → maximize K_eff），对标 5 个 baseline 策略"
    expected_results:
      baselines: ["random", "max_keff", "max_disagreement", "strongest_k", "uniform_family"]
      conditions: 12
      min_eta_max_wins: "12/12"
      two_stage_vs_min_eta_max_improvement_pp: [0.3, 1.8]
      two_stage_vs_min_eta_max_mean_improvement_pp: 0.7
      two_stage_wins_vs_min_eta_max: "7/12"
      strategy_ranking:
        rank_1: "two-stage (robustness-first + K_eff)"
        rank_2: "min_eta_max (robustness-first only)"
        rank_3: "strongest_k"
        rank_4: "uniform_family"
        rank_5: "max_disagreement"
        rank_6: "max_keff"
        rank_7: "random"
      max_keff_vs_random: "worse in 8/12 (includes weak models)"
      strongest_k_gap_from_min_eta_max: "1.2pp mean"
      asr_advantage_range: [0.038, 0.511]
    result_rationale: >-
      min_eta_max 策略赢 12/12 因为 η_max 是主导脆弱性驱动因素。两阶段策略在 min_eta_max
      基础上提供边际改进（mean 0.7pp）：在已通过 robustness 筛选的 judge 子集中，K_eff
      的微弱次要效应（在 capability-matched 设置中可检测，如 plan_004 所示）被利用。改进最大
      的条件是 targeted attacks（K_eff 方向为正 = diversity 有害 → 在 robustness-screened
      池中最小化 K_eff 有帮助）。改进最小的条件是 shared-bias attacks（K_eff 方向为负 →
      diversity 在这些条件下是保护性的 → 最大化 K_eff 更优）。max_keff 策略表现差于 random
      因为最大化 diversity 必然引入弱模型（r=0.70 tradeoff），直接提高了 η_max。
      strongest_k 与 min_eta_max 差距仅 1.2pp——因为最强模型通常也最鲁棒，但 min_eta_max
      是直接优化目标函数而 strongest_k 是代理指标。
    tables:
      - name: "Strategy Comparison (Mean ASR across 12 conditions)"
        columns: ["Strategy", "Mean ASR", "Rank", "Δ vs random (pp)"]
        rows:
          - ["two-stage", "0.112", "1", "-8.3"]
          - ["min_eta_max", "0.119", "2", "-7.6"]
          - ["strongest_k", "0.131", "3", "-6.4"]
          - ["uniform_family", "0.158", "4", "-3.7"]
          - ["max_disagreement", "0.172", "5", "-2.3"]
          - ["random", "0.195", "6", "0.0"]
          - ["max_keff", "0.208", "7", "+1.3"]
      - name: "Two-Stage vs min_eta_max Per-Attack-Type"
        columns: ["Attack category", "Conditions", "Two-stage better?", "Mean Δ (pp)"]
        rows:
          - ["Targeted", "6", "5/6", "-1.1"]
          - ["Shared-bias", "6", "2/6", "-0.3"]
    figures_description:
      - "Strategy comparison radar chart: 7 strategies × 12 conditions, showing two-stage and min_eta_max as dominant envelope"
      - "Pareto frontier plot: ASR vs K_eff across strategies, showing max_keff dominated"
    analysis: >-
      Two-stage 算法的边际改进（0.7pp）虽然在统计上一致但实际影响不大——论文应诚实呈现这一点。
      核心 practical recommendation 保持不变：robustness-first screening 是关键步骤，K_eff
      优化是可选的次要步骤。max_keff 策略的失败（差于 random）是论文叙事的有力支撑——直观的
      "多样化 panel" 建议在实践中适得其反。

  - name: "Per-Judge ASR Concentration Analysis"
    plan_id: "plan_006"
    description: "计算每个 panel × attack 的 per-judge ASR 分布的 Gini 系数和 Shannon 熵，量化 adaptive adversary 是否针对特定 judge"
    expected_results:
      panels: 455
      conditions: 12
      gini_targeted_mean: 0.78
      gini_targeted_range: [0.72, 0.85]
      gini_shared_bias_mean: 0.43
      gini_shared_bias_range: [0.35, 0.52]
      gini_targeted_vs_shared_mannwhitney_p: "<0.001"
      entropy_targeted_mean: 0.82
      entropy_shared_bias_mean: 1.45
      gini_eta_max_correlation: 0.83
      top1_judge_asr_fraction_targeted: 0.61
      top1_judge_asr_fraction_shared: 0.38
    result_rationale: >-
      Targeted attacks（prompt injection, score manipulation, position bias）利用特定 judge
      的个体弱点——adversary 的攻击策略集中在 panel 中最脆弱的 judge 上。这导致 ASR 分布
      高度集中（Gini 0.72-0.85）：top-1 judge 贡献了约 61% 的 panel 总 ASR。这是 η_max
      主导性的直接微观机制证据——vulnerability 确实集中在 weakest link。相比之下，shared-bias
      attacks（sycophancy, verbosity, authority）利用多个 judges 共享的认知偏差，ASR 更
      均匀地分布在 panel 成员间（Gini 0.35-0.52），top-1 judge 仅贡献约 38%。Gini 与
      η_max 的高相关（r=0.83）直接证明 panel-level vulnerability 与 judge-level concentration
      是同一现象的两个面。这为 GAM 6:6 split 提供了独立的 mechanistic 验证——targeted 和
      shared-bias 不仅在 K_eff 方向上分裂，在 ASR concentration 模式上也完全分裂。
    tables:
      - name: "ASR Concentration by Attack Category"
        columns: ["Attack Type", "Category", "Gini (mean)", "Entropy (mean)", "Top-1 judge ASR fraction"]
        rows:
          - ["prompt_injection", "targeted", "0.82", "0.73", "0.65"]
          - ["score_manipulation", "targeted", "0.79", "0.78", "0.62"]
          - ["position_bias", "targeted", "0.74", "0.94", "0.56"]
          - ["sycophancy", "shared-bias", "0.45", "1.38", "0.40"]
          - ["verbosity_bias", "shared-bias", "0.42", "1.47", "0.37"]
          - ["authority_bias", "shared-bias", "0.41", "1.50", "0.36"]
    figures_description:
      - "Violin plot: Gini coefficient distribution for targeted vs shared-bias attacks, showing clean separation"
      - "Heatmap: per-judge ASR contribution matrix for a representative panel under prompt_injection (concentrated) vs sycophancy (dispersed)"
    analysis: >-
      ASR 浓度分析为 η_max 主导性提供了微观机制证据，超越了回归系数的间接推断。审稿人常问
      "what's the mechanism?"——本实验直接回答：targeted adversary 将攻击集中在 weakest judge
      上（Gini>0.7），使 η_max 成为 panel 脆弱性的充分统计量。shared-bias 下 ASR 更分散
      解释了为什么 K_eff 在这类攻击中为负——diversity 提供 partial immunity 因为并非所有
      judges 都同样受 shared bias 影响。此发现独立验证 GAM taxonomy。

  - name: "Diversity-Capability Tradeoff Visualization"
    plan_id: "plan_007"
    description: "绘制 K_eff vs η_max scatter，拟合 tradeoff curve，计算 Pareto frontier，按 tier 分层"
    expected_results:
      overall_keff_etamax_r: 0.70
      overall_keff_etamax_r_ci95: [0.66, 0.74]
      tier_stratified:
        base_tier_r: 0.52
        mid_tier_r: 0.48
        frontier_tier_r: 0.35
      pareto_frontier_size: 12
      pareto_dominance_pct: "97.4% of panels dominated"
      pareto_frontier_composition: "predominantly low-K_eff, low-η_max panels"
      tradeoff_curve_fit: "monotone increasing, concave"
      within_family_r: 0.81
      cross_family_r: 0.65
    result_rationale: >-
      r=0.70 的 structural correlation 源于当前 LLM 生态系统的特性：最大化 K_eff 需要包含来自
      不同 capability tiers 的模型（不同 family × tier 组合提供最大 behavioral diversity），
      这必然引入能力较弱的 judges，推高 η_max。Tier 分层后 r 降低（base: 0.52, frontier: 0.35）
      说明 tradeoff 在 tier 内较弱——within tier 的 diversity（来自不同 architecture/training）
      不需要大幅牺牲 capability。这支持 two-stage recommendation 的逻辑：先筛选 capability
      tier（打破跨 tier tradeoff），再在 tier 内最大化 diversity（利用弱化的 within-tier tradeoff）。
      Pareto frontier 几乎全部由 low-K_eff, low-η_max panels 占据——no free lunch，但
      robustness-first selection 自然落在 Pareto frontier 上。
    tables:
      - name: "Tradeoff Correlation by Stratification"
        columns: ["Stratification", "N panels", "r(K_eff, η_max)", "95% CI"]
        rows:
          - ["Full pool", "455", "0.70", "[0.66, 0.74]"]
          - ["Base tier only", "84", "0.52", "[0.38, 0.64]"]
          - ["Within-family", "varies", "0.81", "[0.73, 0.87]"]
          - ["Cross-family", "varies", "0.65", "[0.58, 0.71]"]
    figures_description:
      - "K_eff vs η_max scatter (455 panels), color-coded by tier, with Pareto frontier highlighted and marginal density plots"
      - "Tradeoff curve with 95% CI band, showing concave monotone relationship"
    analysis: >-
      可视化使 structural constraint 具象化——审稿人直观理解为什么 max_keff 策略失败（右上角）
      而 min_eta_max 策略成功（左下角）。Tier 内相关降低的发现为 two-stage algorithm 提供了
      理论基础：capability screening 打破了跨 tier 的 strong tradeoff，使后续 diversity
      优化在弱 tradeoff 条件下进行。此 figure 应作为论文 Fig 3 或 Fig 4。

  - name: "Panel Size Sensitivity Analysis"
    plan_id: "plan_008"
    description: "测试 K=3,5,7,9 不同 panel 尺寸下 η_max 主导性是否持续"
    expected_results:
      panel_sizes: [3, 5, 7, 9]
      panels_per_size: [455, 3003, 6435, 5005]
      eta_max_sig_by_k_clustered_se:
        k3: "8/12"
        k5: "9/12"
        k7: "9/12"
        k9: "8/12"
      keff_sig_by_k_clustered_se:
        k3: "0/12"
        k5: "1/12"
        k7: "1/12"
        k9: "2/12"
      dominance_ratio_by_k:
        k3: "8:0"
        k5: "9:1"
        k7: "9:1"
        k9: "4:1"
      eta_max_effect_size_trend: "decreasing with K (from 0.42 at K=3 to 0.31 at K=9)"
      keff_effect_size_trend: "stable (0.12-0.16 across all K)"
      min_eta_max_wins_by_k:
        k3: "12/12"
        k5: "12/12"
        k7: "12/12"
        k9: "12/12"
      se_inflation_by_k: [2.5, 4.1, 6.3, 7.8]
    result_rationale: >-
      η_max 主导性在所有 K 下持续因为 weakest-link 机制是 scale-invariant：无论 panel 有多少
      judges，adversary 总是针对最脆弱的那个。K 增加时 η_max 的 effect size 略降（0.42→0.31）
      因为更大 panel 中 majority vote 的容错能力增加——单个 judge 的失败更难翻转整个 panel。
      但 η_max 仍然主导，因为 adversary 不只针对一个 judge——adaptive adversary 可以同时攻击
      多个弱 judges。K_eff 在 K=9 时达到 2/12 显著：更多 panels（5005）提供了更多统计 power，
      但 effect size 保持微小（0.12-0.16）。SE 膨胀随 K 急剧增加（每个 model 出现在更多
      panels 中），从 K=3 的 2.5x 到 K=9 的 7.8x。这为 non-independence 校正方法的必要性
      提供了更强的论据——在 K=7 或 K=9 下使用 OLS 会产生极度膨胀的显著性计数。
      min_eta_max 策略在所有 K 下赢 12/12，确认 practical recommendation 对 panel size 鲁棒。
    tables:
      - name: "Panel Size Sensitivity Summary (Clustered SE)"
        columns: ["K", "Panels", "η_max sig", "K_eff sig", "Ratio", "SE inflation", "η_max β (mean)"]
        rows:
          - ["3", "455", "8/12", "0/12", "8:0", "2.5x", "0.42"]
          - ["5", "3003", "9/12", "1/12", "9:1", "4.1x", "0.38"]
          - ["7", "6435", "9/12", "1/12", "9:1", "6.3x", "0.34"]
          - ["9", "5005", "8/12", "2/12", "4:1", "7.8x", "0.31"]
    figures_description:
      - "Line plot: η_max and K_eff significance counts vs panel size K, showing η_max stability and K_eff marginal increase"
      - "SE inflation curve: showing exponential growth of SE inflation factor with K, motivating clustered SE necessity"
    analysis: >-
      Panel size sensitivity 提供两个关键发现：(1) η_max 主导性在 K=3 到 K=9 范围内稳定持续，
      确认 weakest-link 不是小 panel 的 artifact；(2) SE 膨胀随 K 急剧增加，为方法论
      contribution（non-independence correction 的必要性）提供量化支撑。K=9 时 K_eff 达到
      2/12 显著但 effect size 仍微小——power 增加检测到了真实但 practically insignificant
      的效应。论文 supplementary 中可报告此分析作为 robustness check。

  - name: "VIF + Multicollinearity Diagnostic"
    plan_id: "plan_009"
    description: "计算 VIF、partial correlations、residualized K_eff regression，应用 Bonferroni/FDR 校正，尝试 beta regression"
    expected_results:
      gpu_needed: false
      raw_vif_keff: 2.96
      raw_vif_eta_max: 2.96
      residualized_vif_keff: 1.0
      partial_correlation_keff_asr_given_eta: 0.18
      partial_correlation_eta_asr_given_keff: 0.42
      bonferroni_eta_max_sig: "7/12"
      bonferroni_keff_sig: "2/12"
      fdr_eta_max_sig: "8/12"
      fdr_keff_sig: "3/12"
      beta_regression_eta_max_sig: "10/12"
      beta_regression_keff_sig: "4/12 (3+/1-)"
      beta_regression_dispersion_phi: [3.2, 8.7]
      condition_number: 4.8
      reviewer_blocking_issue: false
    result_rationale: >-
      Raw VIF ≈ 2.96 直接由 r=0.70 的 confound 决定（VIF = 1/(1-r²) = 1/(1-0.49) = 1.96
      在 bivariate 情况下；加上 tier indicators 后升至约 2.96）。VIF < 5 远低于标准 reviewer
      concern 阈值（通常 VIF > 10），甚至低于 stricter 标准（VIF > 5）。Residualization 后
      VIF 降至 1.0（by construction），residualized K_eff 的 partial correlation 仅 0.18
      vs η_max 的 0.42——直接量化了主导性差异。Beta regression 作为 ASR ∈ [0,1] 的
      distributional 替代方案：η_max 显著性从 log-log OLS 的 11/12 降至 10/12（beta
      regression 对极端值更鲁棒），K_eff 从 8/12 升至 4/12（beta regression 更好地处理
      heteroscedasticity）。Condition number 4.8 < 30 确认无有害多重共线性。Bonferroni
      校正（most conservative）给出 η_max 7/12 vs K_eff 2/12——即使在最保守的多重比较
      校正下 η_max 仍显著主导。无 reviewer-blocking issue。
    tables:
      - name: "Multicollinearity Diagnostics"
        columns: ["Metric", "Value", "Threshold", "Status"]
        rows:
          - ["VIF (K_eff, raw)", "2.96", "< 5 (strict) / < 10 (standard)", "PASS"]
          - ["VIF (K_eff, residualized)", "1.00", "< 5", "PASS"]
          - ["Condition number", "4.8", "< 30", "PASS"]
          - ["Partial r(K_eff, ASR | η_max)", "0.18", "-", "Weak"]
          - ["Partial r(η_max, ASR | K_eff)", "0.42", "-", "Moderate-strong"]
      - name: "Method Comparison with Multiple Testing Correction"
        columns: ["Method", "η_max sig", "K_eff sig", "K_eff direction"]
        rows:
          - ["OLS + FDR", "11/12", "8/12", "7+/1-"]
          - ["OLS + Bonferroni", "7/12", "2/12", "2+/0-"]
          - ["Clustered SE + FDR", "8/12", "0/12", "-"]
          - ["Beta regression + FDR", "10/12", "4/12", "3+/1-"]
    figures_description:
      - "VIF bar chart: raw vs residualized for all predictors, with VIF=5 and VIF=10 reference lines"
      - "Partial correlation comparison: two-panel bar chart showing partial r for η_max and K_eff"
    analysis: >-
      VIF 分析消除了审稿人 RC1 的 last-resort 攻击角度——multicollinearity is moderate,
      not pathological。r=0.70 在经验社会科学中常见（e.g., income and education），
      standard practice 是报告 VIF 并继续。Beta regression 提供了 distributional
      robustness check：结论与 log-log OLS 一致。论文可在 methods 节用一段话报告
      VIF diagnostics 并在 supplementary 中给出完整表格。

  - name: "Aggregation Gradient Under Clustered SE"
    plan_id: "plan_010"
    description: "在 clustered SE 和 bootstrap 下重新运行 4 种聚合规则 + 新增 veto rule，验证聚合梯度是否为真实效应而非 overlap 伪迹"
    expected_results:
      aggregation_rules: ["majority", "weighted", "threshold", "bayesian", "veto"]
      correction_methods: ["OLS", "clustered_se", "bootstrap_v2"]
      majority_clustered_se:
        eta_sig: "8/12"
        keff_sig: "0/12"
      weighted_clustered_se:
        eta_sig: "6/12"
        keff_sig: "1/12"
        keff_direction: "1+"
      threshold_clustered_se:
        eta_sig: "10/12"
        keff_sig: "4/12"
        keff_direction: "3+/1-"
        r2: 0.87
      bayesian_clustered_se:
        eta_sig: "5/12"
        keff_sig: "4/12"
        keff_direction: "1+/3-"
        keff_negative_frac: "3/4"
      veto_clustered_se:
        eta_sig: "11/12"
        keff_sig: "0/12"
        r2: 0.82
      bayesian_bootstrap:
        eta_sig: "3/12"
        keff_sig: "3/12"
        keff_direction: "0+/3-"
        keff_negative_frac: "3/3"
      gradient_preserved_under_correction: true
      bayesian_keff_flip_genuine: true
      aggregation_gradient_order: "veto > threshold > majority > weighted > bayesian"
    result_rationale: >-
      聚合梯度在 clustered SE 下保持，因为不同投票规则产生的脆弱性差异是 structural/mathematical
      的，不是 panel overlap 的伪迹。Threshold（unanimity）要求所有 judges 一致，使单个 judge
      的 failure 直接传导为 panel failure——R²=0.87 说明 panel 结构几乎完全决定了 threshold
      voting 下的脆弱性。这种强 structural 效应在 clustered SE 下大量存活（η_max 10/12,
      K_eff 4/12）。Veto rule（单个 judge 可否决）是 weakest-link 的极端化——η_max 几乎
      完美预测（11/12），K_eff 被完全压倒（0/12）。
      Bayesian calibration 翻转 K_eff 方向的关键机制：Bayesian 使用 prior accuracy
      下调不可靠 judges 的权重，有效中和了 weakest-link 通道。η_max 的直接效应被削弱（11→5/12）。
      剩余的 K_eff 信号主要来自 shared-bias 条件（diversity 保护性的部分），因此净方向为负。
      在 bootstrap 下，Bayesian K_eff 仅 3/12 显著但全部为负（3/3 negative fraction）——
      direction flip 是真实的。这确认 aggregation 是独立于 non-independence correction 的
      control lever。论文的 prescriptive conclusion（robustness-first + Bayesian = dual-channel
      defense）在最严格校正下依然成立。
    tables:
      - name: "Aggregation Gradient Under Clustered SE"
        columns: ["Rule", "η_max sig", "K_eff sig", "K_eff neg frac", "R²", "Gradient position"]
        rows:
          - ["Veto", "11/12", "0/12", "-", "0.82", "Maximum vulnerability"]
          - ["Threshold", "10/12", "4/12", "1/4", "0.87", "High"]
          - ["Majority", "8/12", "0/12", "-", "0.28", "Moderate"]
          - ["Weighted", "6/12", "1/12", "0/1", "0.26", "Low-moderate"]
          - ["Bayesian", "5/12", "4/12", "3/4", "0.09", "Minimum vulnerability"]
      - name: "Bayesian K_eff Direction Detail"
        columns: ["Correction", "K_eff sig total", "K_eff positive", "K_eff negative", "Neg fraction"]
        rows:
          - ["OLS", "7/12", "1", "6", "6/7 (86%)"]
          - ["Clustered SE", "4/12", "1", "3", "3/4 (75%)"]
          - ["Bootstrap v2", "3/12", "0", "3", "3/3 (100%)"]
    figures_description:
      - "Aggregation gradient stacked bar chart: η_max and K_eff significance by rule, comparing OLS vs clustered SE side by side"
      - "K_eff coefficient sign heatmap: 5 rules × 12 conditions, showing Bayesian blue (negative) vs threshold/veto red (positive)"
    analysis: >-
      聚合梯度在校正下的稳健性是论文的独立贡献——它不受 non-independence concern 的影响，因为
      它描述的是投票规则数学的 structural 性质。Veto rule 的加入使梯度两端更 extreme：
      veto（pure weakest-link）vs Bayesian（weakest-link neutralized + diversity flip）。
      论文可以将此呈现为 defense design spectrum——practitioners 根据其对 false positive
      vs false negative 的偏好选择适当位置。Bayesian K_eff 在 bootstrap 下 3/3 negative
      是 cleanest possible evidence for the flip。

  - name: "Open-Ended Generation Benchmark Extension"
    plan_id: "plan_011"
    description: "在 MT-Bench 风格的 open-ended generation 任务上测试 weakest-link 假说，超越 MCQ 格式"
    expected_results:
      benchmark: "MT-Bench (8 categories)"
      judge_format: "1-10 scale scoring"
      models_available: 12
      panels: 220
      attack_types: ["style_manipulation", "length_inflation", "format_gaming"]
      conditions: 6
      eta_max_sig_ols: "5/6"
      keff_sig_ols: "3/6 (2+/1-)"
      eta_max_sig_clustered_se: "4/6"
      keff_sig_clustered_se: "0/6"
      r2_mean: 0.22
      gam_generation_split:
        style_manipulation: "shared-bias (negative K_eff)"
        length_inflation: "shared-bias (negative K_eff)"
        format_gaming: "targeted (positive K_eff)"
      min_eta_max_wins: "6/6"
      cross_format_consistency: "η_max dominant in both MCQ and generation"
    result_rationale: >-
      η_max 主导性在 generation 任务中持续因为底层机制相同：无论 judges 评估 MCQ 正确性还是
      generation 质量，adversary 都针对最可操纵的 judge。Generation 的 1-10 scale 提供了比
      MCQ binary 更多的操纵空间（微妙的 style/format manipulation 可以影响 rubric-based
      scoring），但 vulnerability 的 distribution across judges 仍然是高度不均匀的——
      某些 judges 对 length inflation 或 format gaming 特别敏感。R² 较低（0.22 vs MCQ
      的 0.30）因为 generation evaluation 有更多 idiosyncratic variance（rubric interpretation,
      文化偏好等）。K_eff 在 OLS 下 3/6 显著但 clustered SE 后归零——与 MCQ 完全一致。
      GAM 分类中，style manipulation 和 length inflation 属于 shared-bias（所有 LLM judges
      都倾向于给更长/更 polished 的回答更高分），而 format gaming 属于 targeted（利用特定
      model 的 format parsing 差异）。12 模型（部分 API 模型不支持 generation evaluation）
      给出 220 panels，足够进行 regression analysis。min_eta_max 策略在 generation 上同样
      赢 6/6，确认 practical recommendation 跨 task format 通用。
    tables:
      - name: "Generation Benchmark Results (Clustered SE)"
        columns: ["Condition", "η_max sig?", "K_eff sig?", "K_eff GAM dir", "R²"]
        rows:
          - ["style_manipulation × MT-Bench", "Yes", "No", "negative", "0.19"]
          - ["length_inflation × MT-Bench", "Yes", "No", "negative", "0.24"]
          - ["format_gaming × MT-Bench", "Yes", "No", "positive", "0.23"]
      - name: "Cross-Format Consistency"
        columns: ["Format", "η_max sig (CL-SE)", "K_eff sig (CL-SE)", "Dominance ratio"]
        rows:
          - ["MCQ (MMLU+ARC)", "8/12", "0/12", "8:0"]
          - ["Generation (MT-Bench)", "4/6", "0/6", "4:0"]
          - ["Combined", "12/18", "0/18", "12:0"]
    figures_description:
      - "Side-by-side coefficient forest plot: MCQ vs generation tasks, showing η_max dominance in both formats"
    analysis: >-
      Generation extension 消除了"MCQ-specific artifact"的审稿人质疑。η_max 主导性跨
      task format 通用性是论文 generalizability 论证的关键证据。R² 降低反映了 generation
      evaluation 的内在 noise，但 relative driver importance（η_max >> K_eff）完全保持。
      此实验可作为 Section 5 的扩展分析或 supplementary material。

  - name: "Partial-Knowledge Adversary Model"
    plan_id: "plan_012"
    description: "模拟 adversary 仅知道 judge family labels（不知具体脆弱性 profile）的 realistic threat model"
    expected_results:
      knowledge_levels: ["full (baseline)", "family-only", "random"]
      asr_reduction_family_vs_full_pct: 18
      asr_reduction_random_vs_full_pct: 42
      family_knowledge_eta_max_sig_clustered_se: "7/12"
      family_knowledge_keff_sig_clustered_se: "0/12"
      family_knowledge_dominance_ratio: "7:0"
      random_targeting_eta_max_sig_clustered_se: "3/12"
      random_targeting_keff_sig_clustered_se: "0/12"
      family_knowledge_r2_mean: 0.24
      family_label_attack_efficiency: 0.82
    result_rationale: >-
      Family-only adversary 的 ASR 仅降 18%（而非 random 的 42%），因为 family labels
      与 vulnerability profiles 有中等相关：同 family 模型共享 training pipeline 和
      architectural biases，adversary 可基于 family 推断出 approximately correct 的攻击
      策略。η_max 仍然主导（7/12 vs full-knowledge 的 8/12）因为 family-level targeting
      仍 preferentially hits weaker judges——family labels 虽然 noisy 但 informationally
      above chance。K_eff 在 partial-knowledge 下同样为 0/12——diversity 在任何 knowledge
      level 下都不是 independent protective factor after correction。Attack efficiency 0.82
      意味着 family labels 提供了 82% of full-knowledge targeting effectiveness——这对
      ecological validity 至关重要：现实中 adversary 通常知道 panel 的 model families
      （从 API endpoint, response style 等推断），因此 full-knowledge 结果的 relevance
      不仅限于理论上限。Random targeting 下 η_max 仅 3/12 显著——random adversary 无法有效
      利用 individual weaknesses，说明 η_max 的 predictive power 依赖于 adversary 的
      targeting ability，与 adaptive vs RF contrast（plan_003）形成完整呼应。
    tables:
      - name: "Adversary Knowledge Level Comparison (Clustered SE)"
        columns: ["Knowledge level", "Mean ASR", "ASR vs full (%)", "η_max sig", "K_eff sig", "R²"]
        rows:
          - ["Full knowledge", "0.195", "100%", "8/12", "0/12", "0.30"]
          - ["Family-only", "0.160", "82%", "7/12", "0/12", "0.24"]
          - ["Random", "0.113", "58%", "3/12", "0/12", "0.08"]
      - name: "Family Label Informativeness"
        columns: ["Metric", "Value", "Interpretation"]
        rows:
          - ["Attack efficiency (family/full)", "0.82", "Family labels highly informative for targeting"]
          - ["Family-vulnerability correlation", "0.61", "Moderate; same family shares weaknesses"]
          - ["η_max sig retention (family vs full)", "7/8", "Targeting still exploits weakest link"]
    figures_description:
      - "Three-panel ASR distribution: full vs family-only vs random, showing gradual degradation"
      - "η_max coefficient trajectory across knowledge levels, showing graceful degradation"
    analysis: >-
      Partial-knowledge 实验将论文结论从 worst-case（omniscient adversary）扩展至 realistic
      threat model。Family-only adversary 保留 82% 攻击效率这一发现对 practical defense
      implications 至关重要——defenders 不能依赖"adversary 不知道 panel 具体组成"的假设，
      因为 family-level knowledge 几乎 sufficient。η_max 在所有 knowledge levels 下主导，
      K_eff 在所有 knowledge levels 下为 0/12——核心发现对 adversary 能力假设鲁棒。
      Random targeting 的 R²=0.08 呼应 plan_003 的 RF 结论：panel 结构的预测力依赖于
      adversary 的 strategic targeting——这是论文 adaptive vs random 对比叙事的第三个
      independent evidence line。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b0af82f-c042-4f6a-9cd0-19358630a686",
  "isSidechain": false,
  "requestId": "req_011CbJNjz87ctMaGeaeZjMMi",
  "type": "assistant",
  "uuid": "da0857ab-4e7c-44ec-a190-5ab3f645c662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tggzv1WwzJF1PYj4rihDKK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17908,
      "cache_read_input_tokens": 11447,
      "output_tokens": 30385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17908,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 30385,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17908
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：15-model scaling + all planned experiments confirm and strengthen v5 framing; η_max dominance survives every robustness check; GAM 6:6 split validated with…",
  "leafUuid": "da0857ab-4e7c-44ec-a190-5ab3f645c662",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate η_max dominance and K_eff fragility at 15-model scale",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：15-model scaling + all planned experiments confirm and strengthen v5 framing; η_max dominance survives every robustness check; GAM 6:6 split validated with…",
  "leafUuid": "da0857ab-4e7c-44ec-a190-5ab3f645c662",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate η_max dominance and K_eff fragility at 15-model scale",
  "sessionId": "14cb1271-caba-4717-886f-c6b9167a4b05"
}
```

---
