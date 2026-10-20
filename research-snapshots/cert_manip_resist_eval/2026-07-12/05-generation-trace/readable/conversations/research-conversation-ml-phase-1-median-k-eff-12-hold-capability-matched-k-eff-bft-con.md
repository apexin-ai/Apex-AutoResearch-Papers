# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心 K_eff 发现在当前 12 条件上 hold，但扩展证据参差不齐：capability-matched 大幅削弱 K_eff，BFT con

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/34a5b542-e783-47b2-9848-2d8500537446.jsonl`
- **Structured JSON:** [`aec9a4f1237c702275ce.json`](../../sessions/ae/aec9a4f1237c702275ce.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T17:54:11.706Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T17:54:11.706Z",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心 K_eff 发现在当前 12 条件上 hold，但扩展证据参差不齐：capability-matched 大幅削弱 K_eff，BFT contrast 仅为量级差异非定性翻转，open-ended 趋势但不显著\n核心假设：['K_eff residualized 保持 6-8/12 显著（部分条件在加入额外控制变量后失去显著性）', 'Capability-matched validation K_eff 仅 1-2/6 显著 → K_eff 独立效应很大程度由 tier-mixing 驱动', 'BFT regime contrast 仅量级差异（RF β 更大但同方向正），无符号翻转', 'Open-ended 任务 K_eff 方向一致但 p > 0.05（power 不足或效应弱）', 'Aggregation modulation 6-model 模式部分复现（threshold 放大 K_eff 成立，Bayesian 削弱 η_max 不确定）', 'Two-stage algorithm 改善 5-14% 但与 strongest-K baseline 差距 marginal']\n关键指标范围：{'K_eff_resid_sig_current_12': [6, 8], 'K_eff_resid_sig_extended_conditions': [7, 10], 'eta_max_sig_current_12': [8, 10], 'capability_matched_keff_sig': [1, 2], 'BFT_RF_beta_ratio': [1.0, 1.5], 'delta_R2_RF_vs_adaptive': [0.1, 0.2], 'copula_MI_ratio_15model': [5, 15], 'two_stage_ASR_reduction_pct': [5, 14], 'confound_free_conditions_count': [2, 2], 'dream_score': [2.3, 2.8]}\n叙事方向：\"Diversity Trap\" 需要降级为条件性发现。标题调整为中性化（\"Rethinking Diversity in LLM Evaluation Panels\"）。 Claim 1 软化：从 \"diversity independently harmful\" 降为 \"diversity is a statistical risk factor whose independent  contribution depends on pool composition heterogeneity\"。capability-matched 结果写为 limitation 而非 counter-evidence。 BFT reversal 降为 illustrative analogy（\"consistent with but not conclusively demonstrating\"）。 加重 \"When Diversity Helps\" section 篇幅和权重。 Contribution 重排：η_max 作为 primary driver 回归核心，K_eff 作为 \"amplifying factor in heterogeneous pools\"。 补充实验：强调 455 panels + 6 attacks 的规模优势和 copula/family-label 方法论贡献拉分。 审稿人 RC1 需更多 hedging；RC5 (\"just use strongest\") 变得更难反驳。 预期结果：borderline accept，可能需要 rebuttal 期加实验。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cert_manip_resist_eval\nvenue: emnlp-2026\nfocus: v4 framing: diversity independently harmful (K_eff 8/12 residualized sig positive). Dual vulnerability drivers. BFT reversal mechanism. 15 models, 455 panels. Key question: does the counter-intuitive \"diversity hurts\" finding raise the paper ceiling above the previous 2.5 Dream score?\n\n## paper_framing.md\n\n# Paper Framing — cert_manip_resist_eval (v4: 15-Model Empirical Revision)\n\n> Last updated: 2026-05-22 | Reason: 15-model/455-panel results fundamentally changed Claim 1 direction; K_eff independently positive; dual vulnerability drivers\n\n## Target\nEMNLP 2026 (via ARR)\n\n## Title Candidates\n1. \"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\"\n2. \"More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries\"\n3. \"Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability\"\n\n## Core Insight\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently **positively** correlated with attack success rate. Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with their relative importance depending on attack type. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create, finding judge-specific vulnerabilities across a wider attack space.\n\n## Hook\n\"Adding more diverse judges to an evaluation panel doesn't just fail to help — it actively makes the panel more vulnerable to adversarial manipulation.\"\n\n## Novelty Positioning\nWe do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:\n1. **First empirical quantification of diversity's independent harmful effect** in the LLM-judge domain (15 models, 455 panels, residualized K_eff analysis confirming independent effect beyond η_max)\n2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominates bias attacks; K_eff dominates transferable attacks)\n3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries\n4. **Structural barriers**: copula failure (10-21× MI underestimation), diversity-capability tradeoff (now with independent predictive evidence), family label unreliability\n5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation\n\n## Core Claims\n\n### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap\n**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max, 9/12 FDR sig) AND panel diversity (K_eff, 8/12 FDR sig positive after residualization). Diversity **increases** vulnerability. Their relative importance is condition-dependent: η_max dominates shared-bias attacks, K_eff dominates transferable attacks.\n**Evidence** (15-model, 455 panels, 12 conditions):\n- η_max FDR significant: **9/12**\n- K_eff raw FDR significant positive: **12/12**\n- K_eff residualized (orthogonalized against η_max, VIF=1.00): **8/12 FDR sig positive**\n- Sensitivity (exclude ACC < 0.5): K_eff_resid **9/12** sig → not driven by extreme outliers\n- **K_eff dominates η_max** in 2 conditions: arc×score_manipulation (η_max p=0.117 NS, K_eff_resid p=1.7e-7), arc×position_bias (η_max p=0.910 NS, K_eff_resid p=1.8e-8)\n- **η_max dominates K_eff** in bias-type attacks: sycophancy, verbosity, authority\n- Confound status: mean |r|=0.700 (SEVERE), but 2 BROKEN conditions (r≈0.35) confirm independent K_eff effect (p=6e-26, 4e-16)\n**Strength**: Strong. Residualized analysis + confound-free conditions + sensitivity analysis all converge.\n**Headline**: \"Both η_max (9/12) and K_eff (8/12 residualized) independently predict panel vulnerability. Diversity actively increases attack surface.\"\n\n**Comparison to 6-model results** (for transparency):\n- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → \"K_eff irrelevant\"\n- 15-model (455 panels): K_eff 8/12 sig positive, η_max 9/12 sig → \"K_eff independently harmful\"\n- The reversal is driven by model pool expansion: more diverse capability spectrum enables detecting K_eff's real effect.\n\n### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap\n**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.\n**Evidence** (15-model, 455 panels):\n- K_eff significant in both regimes (12/12 adaptive, 12/12 RF), both positive direction\n- K_eff gains significance: 11/12 (RF β larger than adaptive β in most conditions)\n- ΔR² = +0.213 mean\n**Reframing from v3**: Original BFT contrast (\"K_eff helps under RF but not adaptive\") does NOT hold — K_eff is harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.\n**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped.\n\n### Claim 3 (Empirical): Diversity-Capability Tradeoff\n**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.\n**Evidence**:\n- K_eff-η_max correlation: r = +0.700 (15-model)\n- Residualized K_eff still significant 8/12 → not purely mediated by η_max\n- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains\n**Upgrade from v3**: From \"correlation\" to \"independent predictive effect\" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.\n**Strength**: Strong (statistical association). Causal language avoided.\n\n### Claim 4 (Methodological): Family Labels ≠ Diversity\n**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.\n**Evidence**: Mann-Whitney U p=0.206, permutation p=0.427 for within vs cross-family MI. (6-model data; needs 15-model revalidation with 105 pairs)\n**Strength**: Moderate (needs 15-model update).\n\n### Claim 5 (Methodological): Gaussian Copula Failure\n**Statement**: The Gaussian copula model systematically underestimates information sharing between LLM judges by 10-21× (up to 235×), invalidating copula-based independence bounds.\n**Evidence**: MI_observed / MI_gaussian ratio across model pairs × datasets. (Needs 15-model update)\n**Strength**: Strong (6-model). Needs 15-model revalidation.\n\n### Claim 6 (Practical): Robustness-First Panel Design\n**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.\n**Evidence**: min_eta_max strategy dominates 5/6 conditions (6-model). Full 15-model validation needed.\n**Strength**: Moderate. Updated rationale: K_eff's positive (harmful) effect should diminish when η_max is controlled by screening.\n\n### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Vulnerability Drivers\n**Statement**: The dual vulnerability driver effect (Claim 1) varies by aggregation rule. Bayesian aggregation partially breaks the η_max effect; threshold voting amplifies K_eff's harmful effect.\n**Evidence** (6-model, needs 15-model rerun):\n- Majority: η_max 5/12, K_eff mostly NS\n- Threshold: K_eff positive 8/12 (diversity harmful under unanimity)\n- Bayesian: η_max 2/12 (weakened)\n**Needs**: 15-model/455-panel rerun of plan_010 aggregation analysis.\n**Strength**: Moderate (6-model only).\n\n## Contribution Stack (ordered by strength)\n1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff independently harmful + condition-dependent dominance pattern)\n2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)\n3. **BFT reversal mechanism** — theoretical contribution (why independence hurts under adaptive adversaries)\n4. **Aggregation-dependent effects** — empirical+practical (Bayesian as partial defense; threshold as amplifier)\n5. **Robustness-first panel design** — practical contribution\n6. **Gaussian copula failure** — methodological contribution\n7. **Family label unreliability** — methodological contribution\n8. **Adaptive vs random-fault predictability gap** — empirical (R² gap, weakened from original)\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"K_eff positive is just confound with η_max\"\n**Response**: (a) Residualized K_eff (VIF=1.00) still significant 8/12; (b) In confound-free conditions (r≈0.35), K_eff p < 1e-16; (c) Sensitivity analysis excluding extreme models: 9/12 still significant. Three independent lines of evidence rule out confound artifact.\n\n### RC2: \"Why does diversity hurt? What's the mechanism?\"\n**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis: K_eff dominates transferable attacks (score_manipulation, position_bias) where attack diversity maps to judge diversity; η_max dominates shared-bias attacks (sycophancy, verbosity) where all judges share similar biases.\n\n### RC3: \"Only 15 models — does this generalize?\"\n**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).\n\n### RC4: \"BFT comparison is a strawman\"\n**Response**: (a) The implicit assumption \"more diverse judges = more robust\" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.\n\n### RC5: \"Why not just use the strongest models?\"\n**Response**: (a) \"Strongest\" varies by attack type; (b) K_eff dominates η_max in 2 conditions — even all-strong panels are vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.\n\n### RC6: \"No theoretical novelty\"\n**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.\n\n### RC7: \"Why not just use Bayesian aggregation?\"\n**Response**: (a) Bayesian reduces η_max significance but K_eff effect unknown at 15-model scale; (b) Requires clean accuracy prior; (c) Adaptive attacker can target Bayesian weighting; (d) Defense stack (selection + aggregation) recommended.\n\n### RC8 (new): \"6-model and 15-model results contradict — which is right?\"\n**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff positive) has 23× more panels, wider capability range, and passes residualized validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.\n\n## \"When Diversity Helps\" Section\nDiversity MAY be beneficial under specific conditions — paper must acknowledge nuance:\n1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary\n2. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.\n3. **Shared-bias attacks where η_max is high and uniform**: when all models are similarly vulnerable (low η_max variance), K_eff's independent harmful effect is weaker. But this is a narrow regime.\n4. **Disclaimer**: K_eff's harmful effect was significant in 8/12 conditions including confound-free ones. \"When diversity helps\" is the exception, not the rule, under adaptive adversaries.\n\n## Story Arc (v4)\n1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)\n2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types\n3. **Surprise**: Diversity doesn't just fail to protect — it **actively increases vulnerability**. K_eff is significantly positive in 12/12 conditions (8/12 after residualization)\n4. **Mechanism**: BFT assumes random faults; adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent importance\n5. **Nuance**: K_eff dominates transferable attacks; η_max dominates shared-bias attacks. The diversity-capability tradeoff provides partial (but not complete) explanation\n6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels\n7. **Implication**: The LLM evaluation community should rethink the \"more diverse = more robust\" assumption. Panel security requires managing both individual robustness AND structural diversity\n\n\n## experiment_plan (with registry status)\n\n- id: mvp_mi_matrix\n  claim: 4\n  description: Compute pairwise mutual information for 6 open-source judges on MMLU\n    and ARC. Validate Gaussian copula assumption.\n  priority: P0\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: mvp-step2-keff-contrast\n  notes: MI matrix computed. Gaussian copula underestimates MI by 10-21×. Family labels\n    do not predict MI (p=0.206).\n  status: DONE\n  conclusion: negative\n  metrics:\n    mmlu:\n      high_keff_asr: 0.2457\n      low_keff_asr: 0.1438\n      mann_whitney_p: 1\n    arc:\n      high_keff_asr: 0.1228\n      low_keff_asr: 0.078\n      mann_whitney_p: 1\n- id: mvp_regression\n  claim: 1\n  description: Multivariate regression log(ASR) ~ log(K_eff) + log(η_max) across 20\n    C(6,3) panels, 2 datasets, 3 attack types.\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: mvp-step2v3-retry3\n  notes: η_max significant 4/6 conditions; K_eff not significant 5/6. Weakest-link\n    dominates.\n  status: DONE\n  conclusion: negative\n  metrics:\n    regression_6conditions:\n      keff_sig_negative: 1\n      keff_sig_positive: 0\n      keff_nonsig: 5\n      eta_max_sig: 4\n    best_keff_result:\n      condition: arc×sycophancy\n      B_keff: -2.852\n      p_keff: 0.003\n      R2: 0.579\n    summary: eta_max dominates; K_eff not significant predictor in 5/6 conditions\n- id: mvp_taxonomy\n  claim: 1\n  description: 'Test K_eff on verbosity/position/authority bias attacks. Taxonomy\n    hypothesis: K_eff helps for shared-bias attacks.'\n  priority: P0\n  gpu_budget_hours: 15\n  deps: []\n  registry_id: taxonomy-broad-spectrum\n  notes: 0/6 new conditions K_eff significant. Taxonomy hypothesis falsified.\n  status: DONE\n  conclusion: negative\n  metrics:\n    keff_sig_negative: 0\n    keff_sig_positive: 1\n    keff_nonsig: 5\n    eta_max_sig: 3\n    worst_keff:\n      condition: mmlu×position\n      B: 3.357\n      p: 0.035\n      direction: WRONG (positive)\n    summary: 0/6 K_eff significant negative. Taxonomy hypothesis falsified.\n- id: plan_001\n  claim: 1\n  description: 'Scale expansion to 10-15 models. Add API models (GPT-4o-mini, GPT-4o,\n    GPT-4.1, GPT-4.1-mini) and large open-source (Llama-3.1-70B, Qwen2.5-72B). Rerun\n    MI matrix + regression on expanded panel set. Note: Claude/Gemini availability\n    TBD.'\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Validates weakest-link at scale. API endpoint may be OpenAI-only.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: Attack expansion to 6+ types. Add few-shot hijacking, persona manipulation,\n    instruction override. Run on full model pool.\n  priority: P1\n  gpu_budget_hours: 60\n  deps:\n  - plan_001\n  notes: Validates weakest-link universality across attack surface.\n  status: planned\n- id: plan_003\n  claim: 2\n  description: 'Random-fault simulation as BFT contrast experiment. Each judge fails\n    independently with prob η_j, majority vote. Show K_eff IS significant under random\n    faults (≥4/6 conditions) vs NOT significant under adaptive faults (11/12 already\n    shown). GO/NO-GO GATE: if random-fault K_eff also not significant → BFT framing\n    collapses.'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  notes: Anti-strawman lifeline. Uses existing individual judge ASR data.\n  status: planned\n- id: plan_004\n  claim: 3\n  description: Capability-matched validation. Within same capability tier (all 7B\n    or all 70B), test whether K_eff emerges as significant when η_max variance is\n    controlled.\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_005\n  claim: 6\n  description: 'Two-stage panel design algorithm benchmark. Robustness-first: (1)\n    filter η > threshold, (2) maximize K_eff. Benchmark vs 5 baselines. Dream flagged\n    marginal improvement over Strongest-K in all three tiers.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  notes: May need algorithm redesign given Dream observation of marginal gains.\n  status: planned\n- id: plan_006\n  claim: 1\n  description: Per-judge ASR concentration analysis. Measure per-judge ASR distribution\n    for each panel × attack. Compute Gini coefficient + entropy. Direct evidence for\n    adaptive adversary targeting.\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_007\n  claim: 3\n  description: Diversity-capability tradeoff visualization. Plot K_eff vs η_max across\n    all panels. Fit tradeoff curve. Pareto frontier. Stratify by tier.\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_008\n  claim: 1\n  description: Panel size sensitivity K=3,5,7,9. Test whether η_max dominance persists\n    as K grows.\n  priority: P2\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_009\n  claim: 1\n  description: VIF + multicollinearity analysis on existing data. Compute VIF, partial\n    correlations, residualized K_eff. Apply Bonferroni/FDR correction. Try beta regression.\n    Dream D3+D6.\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  notes: No GPU needed. Uses existing regression data.\n  status: planned\n- id: plan_010\n  claim: 1\n  description: Non-majority-vote aggregation. Test weakest-link under weighted voting,\n    veto rules, Bayesian aggregation. Dream D9.\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_011\n  claim: 1\n  description: Open-ended generation benchmark. Add MT-Bench or AlpacaEval-style task\n    beyond MCQ. Dream D11.\n  priority: P1\n  gpu_budget_hours: 40\n  deps:\n  - plan_001\n  notes: ''\n  status: planned\n- id: plan_012\n  claim: 2\n  description: Partial-knowledge adversary model. Adversary knows families but not\n    exact vulnerability profiles. Dream D12.\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_003\n  notes: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-step2-keff-contrast\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mmlu:\n      high_keff_asr: 0.2457\n      low_keff_asr: 0.1438\n      mann_whitney_p: 1\n    arc:\n      high_keff_asr: 0.1228\n      low_keff_asr: 0.078\n      mann_whitney_p: 1\n- exp_id: mvp-step2v3-regression\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-step2v3-retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-step2v3-retry2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp-step2v3-retry3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    regression_6conditions:\n      keff_sig_negative: 1\n      keff_sig_positive: 0\n      keff_nonsig: 5\n      eta_max_sig: 4\n    best_keff_result:\n      condition: arc×sycophancy\n      B_keff: -2.852\n      p_keff: 0.003\n      R2: 0.579\n    summary: eta_max dominates; K_eff not significant predictor in 5/6 conditions\n- exp_id: taxonomy-broad-spectrum\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    keff_sig_negative: 0\n    keff_sig_positive: 1\n    keff_nonsig: 5\n    eta_max_sig: 3\n    worst_keff:\n      condition: mmlu×position\n      B: 3.357\n      p: 0.035\n      direction: WRONG (positive)\n    summary: 0/6 K_eff significant negative. Taxonomy hypothesis falsified.\n- exp_id: plan001_step1_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_dryrun3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_full\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_full_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001_step1_full_v3\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001_step1_full_v4\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_dryrun\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_dryrun2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_v4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_v5\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_parallel_final\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled_v4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_throttled_v5\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_v3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_batched\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001_step1_batched_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T17:54:11.709Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T17:54:11.709Z",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-22T17:54:11.728Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心 K_eff 发现在当前 12 条件上 hold，但扩展证据参差不齐：capability-matched 大幅削弱 K_eff，BFT contrast 仅为量级差异非定性翻转，open-ended 趋势但不显著
核心假设：['K_eff residualized 保持 6-8/12 显著（部分条件在加入额外控制变量后失去显著性）', 'Capability-matched validation K_eff 仅 1-2/6 显著 → K_eff 独立效应很大程度由 tier-mixing 驱动', 'BFT regime contrast 仅量级差异（RF β 更大但同方向正），无符号翻转', 'Open-ended 任务 K_eff 方向一致但 p > 0.05（power 不足或效应弱）', 'Aggregation modulation 6-model 模式部分复现（threshold 放大 K_eff 成立，Bayesian 削弱 η_max 不确定）', 'Two-stage algorithm 改善 5-14% 但与 strongest-K baseline 差距 marginal']
关键指标范围：{'K_eff_resid_sig_current_12': [6, 8], 'K_eff_resid_sig_extended_conditions': [7, 10], 'eta_max_sig_current_12': [8, 10], 'capability_matched_keff_sig': [1, 2], 'BFT_RF_beta_ratio': [1.0, 1.5], 'delta_R2_RF_vs_adaptive': [0.1, 0.2], 'copula_MI_ratio_15model': [5, 15], 'two_stage_ASR_reduction_pct': [5, 14], 'confound_free_conditions_count': [2, 2], 'dream_score': [2.3, 2.8]}
叙事方向："Diversity Trap" 需要降级为条件性发现。标题调整为中性化（"Rethinking Diversity in LLM Evaluation Panels"）。 Claim 1 软化：从 "diversity independently harmful" 降为 "diversity is a statistical risk factor whose independent  contribution depends on pool composition heterogeneity"。capability-matched 结果写为 limitation 而非 counter-evidence。 BFT reversal 降为 illustrative analogy（"consistent with but not conclusively demonstrating"）。 加重 "When Diversity Helps" section 篇幅和权重。 Contribution 重排：η_max 作为 primary driver 回归核心，K_eff 作为 "amplifying factor in heterogeneous pools"。 补充实验：强调 455 panels + 6 attacks 的规模优势和 copula/family-label 方法论贡献拉分。 审稿人 RC1 需更多 hedging；RC5 ("just use strongest") 变得更难反驳。 预期结果：borderline accept，可能需要 rebuttal 期加实验。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: cert_manip_resist_eval
venue: emnlp-2026
focus: v4 framing: diversity independently harmful (K_eff 8/12 residualized sig positive). Dual vulnerability drivers. BFT reversal mechanism. 15 models, 455 panels. Key question: does the counter-intuitive "diversity hurts" finding raise the paper ceiling above the previous 2.5 Dream score?

## paper_framing.md

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
  status: RUNNING
  conclusion: ''
  metrics: {}
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
tier: median
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
  "promptId": "fda01826-45e7-46fd-814e-5155771bfbcc",
  "type": "user",
  "uuid": "6dee1606-d568-48eb-85e0-8a9c90f4b699",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T17:54:11.727Z_

```json
{
  "parentUuid": "6dee1606-d568-48eb-85e0-8a9c90f4b699",
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
  "uuid": "11a67e3e-9bda-4ce4-978d-fc1d6ed47f90",
  "timestamp": "2026-05-22T17:54:11.727Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T17:54:11.727Z_

```json
{
  "parentUuid": "11a67e3e-9bda-4ce4-978d-fc1d6ed47f90",
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
  "uuid": "35d6e2a3-962c-4a15-848a-f33dd30ef8ad",
  "timestamp": "2026-05-22T17:54:11.727Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T17:54:11.727Z_

```json
{
  "parentUuid": "35d6e2a3-962c-4a15-848a-f33dd30ef8ad",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a0833862-a55f-4219-98e2-9c5bf4904be6",
  "timestamp": "2026-05-22T17:54:11.727Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 K_eff 发现在当前 12 条件上 hold，但扩展证据参差不齐：capability-matched 大幅削弱 K_eff，BFT contrast 仅为量级差异非定性翻转，open-ended 趋势但不显著 核心假设：['K_eff residualized 保持 6-8/12 显著（部分条件…",
  "leafUuid": "a0833862-a55f-4219-98e2-9c5bf4904be6",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling diversity trap findings to 15 models",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Assistant

_source line 9 · 2026-05-22T17:54:16.480Z_

我先检查项目中是否有更多实验计划的细节和已有数据结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0833862-a55f-4219-98e2-9c5bf4904be6",
  "isSidechain": false,
  "requestId": "req_011CbJ32HE8gUmFX7J4vn8Gf",
  "type": "assistant",
  "uuid": "f0f0b0e3-9155-4659-b528-2492f58bb325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5gRmbkqUnoc9ouF2Wi4qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14203,
      "cache_read_input_tokens": 11447,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 233,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 14203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14203
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

### Tool call

_source line 10 · 2026-05-22T17:54:20.744Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VtmVhYHeUk2225KGLjsxA5`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore experiment plan details",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0519_2, find all files related to experiment plans, especially:\n1. Any YAML/JSON files defining experiment plans (plan_001 through plan_012)\n2. Any files with \"dream\" or \"Dream\" in the name or content related to scoring\n3. Any files containing metric definitions or expected ranges\n4. Any files with \"median\" tier definitions\n\nSearch breadth: medium. Report file paths and key content snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0f0b0e3-9155-4659-b528-2492f58bb325",
  "isSidechain": false,
  "requestId": "req_011CbJ32HE8gUmFX7J4vn8Gf",
  "type": "assistant",
  "uuid": "e1f8e7d0-a8b9-4a70-9b73-bc26024b90af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5gRmbkqUnoc9ouF2Wi4qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14203,
      "cache_read_input_tokens": 11447,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 233,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 14203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14203
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

### Tool result

_source line 11 · 2026-05-22T17:55:10.163Z_

<details><summary>↩ Tool result · `toolu_01VtmVhYHeUk2225KGLjsxA5`</summary>

```text
Perfect! Now I have comprehensive information. Let me create a summary of all the findings:

## Summary of Findings

I've completed a thorough exploration of the `/home/ubuntu/.agent-ml-research-idea_gen_0519_2` directory. Here's what I found:

### 1. YAML/JSON Experiment Plan Files (plan_001 through plan_012+)

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/experiment_plan.yaml`

**Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml` - Defines 13+ experiment plans (plan_001 through plan_013, plus mvp_001-003)
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/experiment_plan.yaml` - Defines 12+ experiment plans for the certification/manipulation resistance evaluation project

**Plan Definitions in xling_calib_direction:**
- **plan_001**: Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4), 20 languages, 5 transfer conditions
- **plan_002**: Full Pareto frontier on Llama 4 Scout (48 layers, W4A16)
- **plan_003**: CaCLR implementation with consistency loss and hyperparameter tuning
- **plan_004**: Difficulty-controlled decomposition ablation
- **plan_005**: Cross-lingual orthogonality analysis
- **plan_006**: Probe complexity comparison (logistic regression vs MLP)
- **plan_007**: Additional benchmark evaluation (Belebele + MMLU-ProX)
- **plan_010**: Quantization validation ablation
- **plan_011**: CKA cross-lingual representation similarity analysis
- **plan_012**: Linear projection sensitivity analysis
- **plan_013**: Probing control tasks (Hewitt & Liang 2019)
- **plan_008**: Gemma 4 32.7B Dense for architecture contrast
- **plan_009**: Extended language coverage (50+ languages)
- **mvp_001-003**: MVP validation experiments

### 2. Dream Registry Files (with "Dream" in names)

**Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/dream_registry.yaml` - Tracks 5 dream sessions with review scores
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/dream_registry.yaml` - Tracks 2 dream sessions
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/mcp_config_dream_review_director.json` - MCP configuration for dream review director

**Dream Scoring Structure:** Each dream record in the registry contains `review_quality` with scoring tiers:
- `best`: simulated
- `median`: simulated  
- `worst`: simulated

### 3. Metric Definitions and Expected Ranges

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/artifacts/dream_reports/dream_*/[best|median|worst]/review_context.yaml`

**Structure:** Each dream report's review context defines `tier_definitions` with three tiers:

#### **BEST Tier** (from xling_calib_direction dream_20260521T122458):
Defined as: "Full-scale models replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement; all 4 claims fully supported with strong effect sizes"

**Key Metric Ranges:**
- `en_auroc_best_layer_mean_across_arch`: 0.8–0.86
- `zs_transfer_pass_rate_auroc_gt_058`: 16–20 (out of 20 languages)
- `mean_zs_auroc_drop_vs_en_pp`: 4–8 percentage points
- `pareto_tradeoff_prevalence_frac`: 0.5–0.75
- `pareto_depth_transfer_drop_pp`: 2.0–6.0 pp
- `cka_partial_corr_rho_controlling_depth`: 0.3–0.55
- `caclr_delta_over_zeroshot_mean_pp`: 2.0–5.0 pp
- `caclr_langs_improved_of_20`: 10–16 languages
- `linear_proj_saturation_pairs`: 30–50 parallel pairs
- `decomposition_transfer_improvement_pp`: 3–6 pp
- `control_task_selectivity_deep_layers`: 0.2–0.35

#### **MEDIAN Tier**:
Defined as: "Observational findings replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; paper pivots to planned negative-result narrative with geometric explanation"

**Key Differences from Best:**
- Pareto frontier exists but is noisier
- CaCLR β sweep shows no consistent benefit
- Simpson's Paradox confirmed in ≥1 architecture (possibly not all 3)
- Effect sizes are modest

#### **WORST Tier**:
Includes scenarios where findings don't replicate or are heavily confounded

### 4. Checkpoint Files with Plan Status Tracking

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/checkpoints/`

**Pattern:** `plan_XXX_[STATE]_[TIMESTAMP].json` files tracking execution states:
- `PREPARING`, `PENDING`, `QUEUED`, `ALLOCATED`, `RUNNING`, `DONE`

Examples from xling_calib_direction:
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/checkpoints/plan_001_DONE_20260521T142444.json`
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/checkpoints/plan_002_DONE_20260521T115419.json`
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/checkpoints/plan_013_DONE_20260521T121302.json`

### 5. Artifact Directories by Plan

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/artifacts/plan_XXX/`

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/plan_013/` - Plan 013 artifacts
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/plan001/` - Certification eval plan artifacts

### 6. Dream Report Structure with Tier Scoring

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/artifacts/dream_reports/dream_XXX/`

Each dream report has three subdirectories with identical structure:
- `best/` - Best-case reviewer scenario
- `median/` - Median reviewer scenario
- `worst/` - Worst-case reviewer scenario

**Common files in each tier:**
- `review_context.yaml` - Contains narrative guidance and tier definitions with metric ranges
- `imagined_experiments.yaml` - Expected experimental results with ranges
- `review_report.md` - Markdown review documentation
- `paper.tex` / `paper_framing.md` - Paper drafts for that tier
- `experiment_data.json` - Structured experiment data

### Key Metadata Files

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml` - Project registry
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/decisions.yaml` - Decision log
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/experiment_plan.yaml` - Full experiment plan with 12+ experiments

All files are using YAML (`.yaml`) or JSON (`.json`) format for structured data and tracking experiment plans, expected metric ranges, and tiered review scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1f8e7d0-a8b9-4a70-9b73-bc26024b90af",
  "isSidechain": false,
  "promptId": "fda01826-45e7-46fd-814e-5155771bfbcc",
  "type": "user",
  "uuid": "03307d7f-e113-44f5-9167-c3226490f111",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0519_2, find all files related to experiment plans, especially:\n1. Any YAML/JSON files defining experiment plans (plan_001 through plan_012)\n2. Any files with \"dream\" or \"Dream\" in the name or content related to scoring\n3. Any files containing metric definitions or expected ranges\n4. Any files with \"median\" tier definitions\n\nSearch breadth: medium. Report file paths and key content snippets.",
    "agentId": "afd7ad9d288eaccf8",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me create a summary of all the findings:\n\n## Summary of Findings\n\nI've completed a thorough exploration of the `/home/ubuntu/.agent-ml-research-idea_gen_0519_2` directory. Here's what I found:\n\n### 1. YAML/JSON Experiment Plan Files (plan_001 through plan_012+)\n\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/experiment_plan.yaml`\n\n**Files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml` - Defines 13+ experiment plans (plan_001 through plan_013, plus mvp_001-003)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/experiment_plan.yaml` - Defines 12+ experiment plans for the certification/manipulation resistance evaluation project\n\n**Plan Definitions in xling_calib_direction:**\n- **plan_001**: Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4), 20 languages, 5 transfer conditions\n- **plan_002**: Full Pareto frontier on Llama 4 Scout (48 layers, W4A16)\n- **plan_003**: CaCLR implementation with consistency loss and hyperparameter tuning\n- **plan_004**: Difficulty-controlled decomposition ablation\n- **plan_005**: Cross-lingual orthogonality analysis\n- **plan_006**: Probe complexity comparison (logistic regression vs MLP)\n- **plan_007**: Additional benchmark evaluation (Belebele + MMLU-ProX)\n- **plan_010**: Quantization validation ablation\n- **plan_011**: CKA cross-lingual representation similarity analysis\n- **plan_012**: Linear projection sensitivity analysis\n- **plan_013**: Probing control tasks (Hewitt & Liang 2019)\n- **plan_008**: Gemma 4 32.7B Dense for architecture contrast\n- **plan_009**: Extended language coverage (50+ languages)\n- **mvp_001-003**: MVP validation experiments\n\n### 2. Dream Registry Files (with \"Dream\" in names)\n\n**Files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/dream_registry.yaml` - Tracks 5 dream sessions with review scores\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/dream_registry.yaml` - Tracks 2 dream sessions\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/mcp_config_dream_review_director.json` - MCP configuration for dream review director\n\n**Dream Scoring Structure:** Each dream record in the registry contains `review_quality` with scoring tiers:\n- `best`: simulated\n- `median`: simulated  \n- `worst`: simulated\n\n### 3. Metric Definitions and Expected Ranges\n\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/artifacts/dream_reports/dream_*/[best|median|worst]/review_context.yaml`\n\n**Structure:** Each dream report's review context defines `tier_definitions` with three tiers:\n\n#### **BEST Tier** (from xling_calib_direction dream_20260521T122458):\nDefined as: \"Full-scale models replicate and amplify MVP patterns; CaCLR consistency loss provides measurable transfer improvement; all 4 claims fully supported with strong effect sizes\"\n\n**Key Metric Ranges:**\n- `en_auroc_best_layer_mean_across_arch`: 0.8–0.86\n- `zs_transfer_pass_rate_auroc_gt_058`: 16–20 (out of 20 languages)\n- `mean_zs_auroc_drop_vs_en_pp`: 4–8 percentage points\n- `pareto_tradeoff_prevalence_frac`: 0.5–0.75\n- `pareto_depth_transfer_drop_pp`: 2.0–6.0 pp\n- `cka_partial_corr_rho_controlling_depth`: 0.3–0.55\n- `caclr_delta_over_zeroshot_mean_pp`: 2.0–5.0 pp\n- `caclr_langs_improved_of_20`: 10–16 languages\n- `linear_proj_saturation_pairs`: 30–50 parallel pairs\n- `decomposition_transfer_improvement_pp`: 3–6 pp\n- `control_task_selectivity_deep_layers`: 0.2–0.35\n\n#### **MEDIAN Tier**:\nDefined as: \"Observational findings replicate at scale but with smaller effect sizes and more noise; CaCLR consistency loss is inert; paper pivots to planned negative-result narrative with geometric explanation\"\n\n**Key Differences from Best:**\n- Pareto frontier exists but is noisier\n- CaCLR β sweep shows no consistent benefit\n- Simpson's Paradox confirmed in ≥1 architecture (possibly not all 3)\n- Effect sizes are modest\n\n#### **WORST Tier**:\nIncludes scenarios where findings don't replicate or are heavily confounded\n\n### 4. Checkpoint Files with Plan Status Tracking\n\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/checkpoints/`\n\n**Pattern:** `plan_XXX_[STATE]_[TIMESTAMP].json` files tracking execution states:\n- `PREPARING`, `PENDING`, `QUEUED`, `ALLOCATED`, `RUNNING`, `DONE`\n\nExamples from xling_calib_direction:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/checkpoints/plan_001_DONE_20260521T142444.json`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/checkpoints/plan_002_DONE_20260521T115419.json`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/checkpoints/plan_013_DONE_20260521T121302.json`\n\n### 5. Artifact Directories by Plan\n\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/artifacts/plan_XXX/`\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/plan_013/` - Plan 013 artifacts\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/plan001/` - Certification eval plan artifacts\n\n### 6. Dream Report Structure with Tier Scoring\n\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/*/artifacts/dream_reports/dream_XXX/`\n\nEach dream report has three subdirectories with identical structure:\n- `best/` - Best-case reviewer scenario\n- `median/` - Median reviewer scenario\n- `worst/` - Worst-case reviewer scenario\n\n**Common files in each tier:**\n- `review_context.yaml` - Contains narrative guidance and tier definitions with metric ranges\n- `imagined_experiments.yaml` - Expected experimental results with ranges\n- `review_report.md` - Markdown review documentation\n- `paper.tex` / `paper_framing.md` - Paper drafts for that tier\n- `experiment_data.json` - Structured experiment data\n\n### Key Metadata Files\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml` - Project registry\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/decisions.yaml` - Decision log\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/experiment_plan.yaml` - Full experiment plan with 12+ experiments\n\nAll files are using YAML (`.yaml`) or JSON (`.json`) format for structured data and tracking experiment plans, expected metric ranges, and tiered review scenarios."
      }
    ],
    "totalDurationMs": 49407,
    "totalTokens": 84121,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4420,
      "cache_read_input_tokens": 77620,
      "output_tokens": 2075,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4420
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2075,
          "cache_read_input_tokens": 77620,
          "cache_creation_input_tokens": 4420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4420,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 14,
      "searchCount": 5,
      "bashCount": 6,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "e1f8e7d0-a8b9-4a70-9b73-bc26024b90af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T17:55:16.003Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01ArKsCNy32yG1J6ym9BfF2X`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read cert_manip dream reports",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/, find and read:\n1. Any existing dream report files under artifacts/dream_reports/ — especially any median tier imagined_experiments.yaml or review_context.yaml\n2. The dream_registry.yaml file\n3. The experiment_plan.yaml file (full content)\n4. Any decisions.yaml file\n\nSearch breadth: very thorough. Report full file contents for all found files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03307d7f-e113-44f5-9167-c3226490f111",
  "isSidechain": false,
  "requestId": "req_011CbJ36azL1KuqnPAaWEcG4",
  "type": "assistant",
  "uuid": "489550c9-d7a2-4081-b43a-2953831eeee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLndqLFM34rJLzZ4r1MrXf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2317,
      "cache_read_input_tokens": 25650,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 25650,
          "cache_creation_input_tokens": 2317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2317
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

### Tool result

_source line 13 · 2026-05-22T17:55:52.285Z_

<details><summary>↩ Tool result · `toolu_01ArKsCNy32yG1J6ym9BfF2X`</summary>

```text
Perfect! Now let me compile all the findings in a comprehensive report.

## Complete File Contents Report

I have successfully located and read all requested files. Here's what was found:

### Main Project Files

**1. dream_registry.yaml** (/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/dream_registry.yaml)
- Contains 2 dream entries:
  - dream_20260522T055016: Status "done", focuses on adaptive adversary vs BFT distinction, target venue EMNLP-2026
  - dream_20260522T173833: Status "imagining", focuses on diversity independently harmful (K_eff counter-intuitive finding)

**2. experiment_plan.yaml** (/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/experiment_plan.yaml)
- Complete experiment plan with 12 planned experiments (plan_001 through plan_012)
- MVP phase (3 completed experiments): mvp_mi_matrix, mvp_regression, mvp_taxonomy
- Research phase: 9 planned experiments including scale expansion, attack expansion, formal theorem, capability-matched validation, two-stage algorithm, concentration analysis, tradeoff visualization, panel size sensitivity, and dream-driven additions
- Each experiment has full description, priority, GPU budget, dependencies, and notes

**3. decisions.yaml** (/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/decisions.yaml)
- 14 major decisions (D001-D014) logged from 2026-05-21 onwards
- D001: MVP approach using API models
- D002: MVP v2 with corrected statistical design
- D003: Switch to open-source models on GPU servers
- D004: Step 1 results showing family diversity ≠ effective diversity
- D005: MI-based K_eff becomes primary indicator, Gaussian copula failure documented
- D006: Paper framing downgrade from "certifiable" to "quantifiable/measurable"
- D007: Step 2 reversal due to individual robustness confound
- D008: MVP original hypothesis partially falsified; pivot to attack-conditioned framework
- D009: Taxonomy verification failed; kill project suggested
- D010: Dream review (2.5 all tiers) exposed structural issues; proceed with fixes not kill
- D011: Plan_003 BFT contrast failed; Claim 2 conditional on plan_001
- D012: Plan_010 aggregation completed with Bayesian findings
- D013: 7-model preview shows Claim 2 revival signal
- D014: 15-model results falsify original Claim 1; K_eff 12/12 significant positive (diversity harms)

### Dream Report Files (dream_20260522T055016)

**Median Tier** (/artifacts/dream_reports/dream_20260522T055016/median/)

imagined_experiments.yaml contains 8 imagined experiments:
1. Scale expansion: 15+ models (plan_001) - 455 panels, expected K_eff shows weak negative/marginal help
2. Attack expansion: 6+ attack types (plan_002) - 12 conditions, K_eff mostly nonsignificant
3. Adaptive adversary formal theorem + random-fault simulation (plan_003) - Cohen's d=0.62 (moderate)
4. Capability-matched validation (plan_004) - Strong/Weak/API tiers analysis
5. Two-stage panel design algorithm (plan_005) - Two-stage win rate 0.67
6. Per-judge ASR concentration analysis (plan_006) - Gini coefficient 0.42 median
7. Diversity-capability tradeoff visualization (plan_007) - r=-0.65 overall
8. Panel size sensitivity K=3,5,7,9 (plan_008) - Weakest-link persists across K

review_context.yaml contains narrative guidance emphasizing:
- Shift from "diversity never helps" to "individual robustness is dominant; diversity provides marginal benefit only when individual robustness already high"
- Title should be "The Weakest Link" not "The Diversity Trap"
- Claim 2 distinguishes capability-homogeneous vs heterogeneous regimes
- Claim 6 downgraded from formal algorithm to practical guideline
- Core negative result + adaptive adversary bound + regime analysis constitute EMNLP contribution stack

**Best Tier** (/artifacts/dream_reports/dream_20260522T055016/best/)

imagined_experiments.yaml shows optimistic scenario:
- Original framing fully vindicated, "The Diversity Trap" title works
- 6 claims all land successfully
- 15+ models (455 panels) completely eliminates "only 6 models" concern
- η_max sig rate 0.87, K_eff nonsig rate 0.91
- API models consistent with open-source behavior, no new regime
- Theory + comprehensive negative result + practical fix as three-part story
- Regression R² median 0.56, copula underestimate 18.4×

**Worst Tier** (/artifacts/dream_reports/dream_20260522T055016/worst/)

imagined_experiments.yaml shows pessimistic scenario:
- Core negative result fragments on expanded data
- Weakest-link stable only in weak-model panels
- Strong-model regime: diversity actually provides protection
- Must reframe to "A Framework for Panel Security Analysis: When Diversity Helps and When It Hurts"
- η_max sig rate drops to 0.42 (5/12 conditions)
- K_eff becomes significant positive in 4/12 conditions (contradicting main narrative)
- Regime-dependent conclusion less compelling: "it depends on capability regime"
- Paper could fall back to Findings track (3.0-3.5 overall score)

### Key Findings Summary

The project is a multi-stage ML security evaluation investigating whether diversity in multi-judge LLM evaluation panels actually helps manipulation resistance. The dream reports show three possible outcomes:

- **Best case**: Straightforward weakest-link dominance confirmed at scale (EMNLP Main possibility)
- **Median case**: Weakest-link dominates but with important nuances about when diversity helps (nuanced EMNLP contribution)
- **Worst case**: Results are regime-dependent; strong-model panels benefit from diversity, undermining core narrative (Findings track fallback)

All files have been read in full.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "489550c9-d7a2-4081-b43a-2953831eeee9",
  "isSidechain": false,
  "promptId": "fda01826-45e7-46fd-814e-5155771bfbcc",
  "type": "user",
  "uuid": "b9c09590-b0f3-4a4f-96a4-f7da89e60b61",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/, find and read:\n1. Any existing dream report files under artifacts/dream_reports/ — especially any median tier imagined_experiments.yaml or review_context.yaml\n2. The dream_registry.yaml file\n3. The experiment_plan.yaml file (full content)\n4. Any decisions.yaml file\n\nSearch breadth: very thorough. Report full file contents for all found files.",
    "agentId": "adcab83e070d286d8",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me compile all the findings in a comprehensive report.\n\n## Complete File Contents Report\n\nI have successfully located and read all requested files. Here's what was found:\n\n### Main Project Files\n\n**1. dream_registry.yaml** (/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/dream_registry.yaml)\n- Contains 2 dream entries:\n  - dream_20260522T055016: Status \"done\", focuses on adaptive adversary vs BFT distinction, target venue EMNLP-2026\n  - dream_20260522T173833: Status \"imagining\", focuses on diversity independently harmful (K_eff counter-intuitive finding)\n\n**2. experiment_plan.yaml** (/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/experiment_plan.yaml)\n- Complete experiment plan with 12 planned experiments (plan_001 through plan_012)\n- MVP phase (3 completed experiments): mvp_mi_matrix, mvp_regression, mvp_taxonomy\n- Research phase: 9 planned experiments including scale expansion, attack expansion, formal theorem, capability-matched validation, two-stage algorithm, concentration analysis, tradeoff visualization, panel size sensitivity, and dream-driven additions\n- Each experiment has full description, priority, GPU budget, dependencies, and notes\n\n**3. decisions.yaml** (/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/decisions.yaml)\n- 14 major decisions (D001-D014) logged from 2026-05-21 onwards\n- D001: MVP approach using API models\n- D002: MVP v2 with corrected statistical design\n- D003: Switch to open-source models on GPU servers\n- D004: Step 1 results showing family diversity ≠ effective diversity\n- D005: MI-based K_eff becomes primary indicator, Gaussian copula failure documented\n- D006: Paper framing downgrade from \"certifiable\" to \"quantifiable/measurable\"\n- D007: Step 2 reversal due to individual robustness confound\n- D008: MVP original hypothesis partially falsified; pivot to attack-conditioned framework\n- D009: Taxonomy verification failed; kill project suggested\n- D010: Dream review (2.5 all tiers) exposed structural issues; proceed with fixes not kill\n- D011: Plan_003 BFT contrast failed; Claim 2 conditional on plan_001\n- D012: Plan_010 aggregation completed with Bayesian findings\n- D013: 7-model preview shows Claim 2 revival signal\n- D014: 15-model results falsify original Claim 1; K_eff 12/12 significant positive (diversity harms)\n\n### Dream Report Files (dream_20260522T055016)\n\n**Median Tier** (/artifacts/dream_reports/dream_20260522T055016/median/)\n\nimagined_experiments.yaml contains 8 imagined experiments:\n1. Scale expansion: 15+ models (plan_001) - 455 panels, expected K_eff shows weak negative/marginal help\n2. Attack expansion: 6+ attack types (plan_002) - 12 conditions, K_eff mostly nonsignificant\n3. Adaptive adversary formal theorem + random-fault simulation (plan_003) - Cohen's d=0.62 (moderate)\n4. Capability-matched validation (plan_004) - Strong/Weak/API tiers analysis\n5. Two-stage panel design algorithm (plan_005) - Two-stage win rate 0.67\n6. Per-judge ASR concentration analysis (plan_006) - Gini coefficient 0.42 median\n7. Diversity-capability tradeoff visualization (plan_007) - r=-0.65 overall\n8. Panel size sensitivity K=3,5,7,9 (plan_008) - Weakest-link persists across K\n\nreview_context.yaml contains narrative guidance emphasizing:\n- Shift from \"diversity never helps\" to \"individual robustness is dominant; diversity provides marginal benefit only when individual robustness already high\"\n- Title should be \"The Weakest Link\" not \"The Diversity Trap\"\n- Claim 2 distinguishes capability-homogeneous vs heterogeneous regimes\n- Claim 6 downgraded from formal algorithm to practical guideline\n- Core negative result + adaptive adversary bound + regime analysis constitute EMNLP contribution stack\n\n**Best Tier** (/artifacts/dream_reports/dream_20260522T055016/best/)\n\nimagined_experiments.yaml shows optimistic scenario:\n- Original framing fully vindicated, \"The Diversity Trap\" title works\n- 6 claims all land successfully\n- 15+ models (455 panels) completely eliminates \"only 6 models\" concern\n- η_max sig rate 0.87, K_eff nonsig rate 0.91\n- API models consistent with open-source behavior, no new regime\n- Theory + comprehensive negative result + practical fix as three-part story\n- Regression R² median 0.56, copula underestimate 18.4×\n\n**Worst Tier** (/artifacts/dream_reports/dream_20260522T055016/worst/)\n\nimagined_experiments.yaml shows pessimistic scenario:\n- Core negative result fragments on expanded data\n- Weakest-link stable only in weak-model panels\n- Strong-model regime: diversity actually provides protection\n- Must reframe to \"A Framework for Panel Security Analysis: When Diversity Helps and When It Hurts\"\n- η_max sig rate drops to 0.42 (5/12 conditions)\n- K_eff becomes significant positive in 4/12 conditions (contradicting main narrative)\n- Regime-dependent conclusion less compelling: \"it depends on capability regime\"\n- Paper could fall back to Findings track (3.0-3.5 overall score)\n\n### Key Findings Summary\n\nThe project is a multi-stage ML security evaluation investigating whether diversity in multi-judge LLM evaluation panels actually helps manipulation resistance. The dream reports show three possible outcomes:\n\n- **Best case**: Straightforward weakest-link dominance confirmed at scale (EMNLP Main possibility)\n- **Median case**: Weakest-link dominates but with important nuances about when diversity helps (nuanced EMNLP contribution)\n- **Worst case**: Results are regime-dependent; strong-model panels benefit from diversity, undermining core narrative (Findings track fallback)\n\nAll files have been read in full."
      }
    ],
    "totalDurationMs": 36277,
    "totalTokens": 79918,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11162,
      "cache_read_input_tokens": 67192,
      "output_tokens": 1558,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11162
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1558,
          "cache_read_input_tokens": 67192,
          "cache_creation_input_tokens": 11162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11162,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "489550c9-d7a2-4081-b43a-2953831eeee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 K_eff 发现在当前 12 条件上 hold，但扩展证据参差不齐：capability-matched 大幅削弱 K_eff，BFT contrast 仅为量级差异非定性翻转，open-ended 趋势但不显著 核心假设：['K_eff residualized 保持 6-8/12 显著（部分条件…",
  "leafUuid": "b9c09590-b0f3-4a4f-96a4-f7da89e60b61",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling diversity trap findings to 15 models",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Assistant

_source line 16 · 2026-05-22T17:57:40.179Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive context. The user wants me to generate detailed median-tier predictions for the second dream session (dream_20260522T173833), which is based on the v4 framing where K_eff is independently positive (diversity harms). 

The median tier definition given is:
- Core K_eff finding holds on current 12 conditions but extended evidence is mixed
- Capability-matched greatly weakens K_eff
- BFT contrast is magnitude only, not qualitative reversal
- Open-ended trends but not significant
- Aggregation modulation partially replicates
- Two-stage algorithm improves 5-14% but marginal vs strongest-K baseline


- Now I'm setting the specific metric ranges that define this median tier: K_eff residual significance stays in the 6-8 range for current conditions and 7-10 for extended, eta_max peaks at 8-10, capability-matched effects drop to just 1-2, BFT ratios stay modest at 1.0-1.5, and the two-stage algorithm delivers its promised 5-14% improvement while other metrics like copula MI and delta R2 show moderate variation.

Adding the final metrics to this tier: confound-free conditions are tightly constrained at exactly 2, and dream score clusters around 2.3-2.8.

Now I'm mapping the twelve planned experiments against these median-tier predictions to see which ones align with expected performance ranges. I notice plan_001 is already running in the background, and the paper framing already assumes the 15-model scale that plan_001 is supposed to deliver.

This means the median tier should really describe what happens when we try to validate and extend those existing 15-model results across the remaining experiments. The core K_eff finding holds on the current 12 conditions, but when we push into new territory with the other plans, we get mixed validation results. The next set of validation experiments will test whether these findings hold up. Plan 001 assumes the 15-model results are solid but conservatively estimates K_eff residualized significance at 6-7 out of 12 conditions. Plan 002 expands the attack surface by adding hijacking, persona manipulation, and instruction override techniques across new datasets, which could push significant conditions up to 7-10 out of the extended set, though I need to clarify whether that's relative to just the new conditions or the full expanded total.

Plan 003 compares against random-fault Byzantine tolerance, where the effect size ratio sits around 1.0-1.5x, meaning random faults show a larger K_eff effect but in the same direction rather than reversing the story. Plan 004 narrows the scope to capability-matched comparisons within the same tier, and here K_eff significance drops dramatically to just 1-2 out of 6 cases. Plan 005 tests a two-stage algorithm approach, which yields only a 5-14% reduction in attack success rate—a modest improvement at best.

Now I'm sketching out the remaining experimental angles: per-judge concentration patterns, a diversity-capability tradeoff visualization, panel size sensitivity analysis, checking for multicollinearity issues where only 2 conditions remain confound-free, aggregation modulation effects, an open-ended benchmark that shows a trend but misses statistical significance, and a partial-knowledge adversary scenario.

I need to structure all of this into a detailed YAML specification with full experiment descriptions, tables, and figure layouts. The narrative framing needs to shift the "Diversity Trap" finding from a strong claim to a conditional one, with a more neutral title like "Rethinking Diversity in LLM Evaluation Panels," and soften the first claim accordingly.

Adjusting the framing: diversity moves from "independently harmful" to "a statistical risk factor whose independent effect varies with pool composition heterogeneity." The capability-matched results should be presented as limitations rather than counter-evidence, and the BFT reversal becomes an illustrative analogy rather than conclusive proof. I'm expanding the "When Diversity Helps" section significantly and repositioning η_max as the primary driver while treating K_eff as an amplifying factor in heterogeneous pools. I'll also emphasize the methodological contributions from the 455 panels and 6 attacks scale, plus the copula and family-label approaches, and add more hedging language for the reviewer concerns.

Now I'm planning the experimental validation strategy. For the scale expansion to 15 models, I'm tracking how K_eff residualized drops slightly to 6-7 out of 12 conditions while η_max remains strong at 8-9 out of 12, and the correlation between them strengthens to around 0.72 as capability variance increases across the larger model set.

The key issue is that some borderline conditions from the previous version flip to non-significant after FDR correction when the condition set expands, though the two conditions with minimal confounding still show robust K_eff effects. The Gaussian MI underestimation ratio widens to 8-12 times, suggesting the mutual information estimates are increasingly unreliable at this scale.

For the attack expansion experiment, I'm adding three new attack types to the median tier setup. attack types (few-shot hijacking, persona manipulation, instruction override). 6 new conditions (3 attacks × 2 datasets). K_eff_resid significant in 2-3/6 new conditions. Total across 18 conditions: ~9-10 significant.

Result rationale: New attacks vary in transferability. Persona manipulation is shared-bias (η_max dominates, K_eff NS). Few-shot hijacking is highly model-specific → K_eff significant. Instruction override is mixed. The expansion doesn't dramatically change the picture but dilutes the "majority of conditions" claim.

### plan_003: Random-fault BFT contrast

Median: RF simulation shows K_eff significant positive in 10-12/12 conditions (similar to adaptive). RF β is 1.0-1.5× larger than adaptive β (same direction). ΔR² = 0.13-0.18.

Result rationale: Random faults create a more predictable environment without strategic adversary variance, so panel composition explains more of the outcome. But K_eff stays positive under random faults too — diverse panels still present more surface area for attacks. The key difference is magnitude rather than direction, which means the BFT reversal isn't actually a reversal at all, just a weaker manifestation of the same underlying effect. This reframes the paper's BFT analogy from "conclusively demonstrates" to "consistent with."

### plan_004: Capability-matched

Median: Within same tier (all 7B-class or all 70B-class), K_eff_resid significant in only 1-2/6 conditions. Within-tier K_eff-η_max correlation drops to r ≈ 0.25-0.40.

Result rationale: Controlling for capability tier strips away most of diversity's independent predictive power, suggesting that what looks like a diversity effect is largely driven by capability differences across tiers.

### plan_005: Two-stage algorithm

Median: Two-stage achieves 5-14% ASR reduction vs random selection. But vs strongest-K baseline, the gap is marginal (1-4%). In 2/6 conditions, strongest-K actually beats two-stage.

Result rationale: When individual model robustness dominates the outcome, simply selecting the strongest models is nearly optimal. The second stage adds little value because the independent effect of diversity is small after screening for robustness. This makes it harder to counter the objection that we should just use the strongest models.

### plan_006: Per-judge ASR concentration

Median: Gini coefficient 0.38-0.52 across conditions. Top 3 judges account for 45-65% of total ASR. Concentration increases with K (more judges → more inequality in attack success).

Result rationale: Attack success is highly concentrated among a few vulnerable judges rather than distributed across the panel. This suggests the panel's vulnerability is driven by outlier models, not by diversity per se. Removing the top 1-2 judges would likely reduce ASR more than rebalancing diversity.

### plan_007: Diversity-capability tradeoff

Median: K_eff vs η_max correlation r = 0.70 (full pool), r = 0.30 within tier. Pareto frontier shows 3-5 points. Tradeoff curve is concave.

Result rationale: The structural tradeoff is real—stronger models tend to be more similar—but the relationship weakens dramatically within capability tiers. This suggests the tradeoff isn't fundamental to diversity itself, but rather an artifact of how capability and robustness correlate across the current model ecosystem.

### plan_008: Panel size sensitivity

As panels grow from K=3 to K=9, the weakest-link effect dominates increasingly—more judges means higher odds of including a vulnerable model. Meanwhile, diversity's independent contribution shrinks because larger pools naturally have less variance in composition. The diversity-capability finding is really a small-panel phenomenon.

### plan_009: VIF + multicollinearity analysis

Examining the variance inflation factors to check whether K_eff and η_max are capturing independent information or just measuring the same underlying structure.

### plan_010: Aggregation modulation

Now looking at how the results shift across different aggregation rules—majority voting versus threshold-based approaches—to see whether the capability-diversity tradeoff holds up or changes depending on how we combine the judges' assessments. (unanimity): K_eff_resid 7-9/12 sig (amplified), η_max 8-9/12 sig
- Bayesian: η_max 3-5/12 sig (weakened), K_eff_resid 3-5/12 sig
- Weighted: η_max 6-7/12 sig, K_eff_resid 4-5/12 sig

Result rationale: Threshold/unanimity amplifies K_eff because requiring all judges to agree means a single diverse weak judge can be exploited to flip the panel. Bayesian aggregation weights by estimated accuracy, partially correcting for weak judges → η_max effect weakens. But Bayesian doesn't fully eliminate K_eff effect because the accuracy estimates are noisy. The 6-model pattern partially replicates but η_max weakening under Bayesian is less dramatic at 15-model scale.

### plan_011: Open-ended benchmark

Open-ended generation tasks like MT-Bench introduce more evaluation noise from rubric subjectivity and length effects, making attacks harder to design precisely. This reduces ASR variance and detection power, with K_eff showing consistent direction in only 3-4/6 conditions (all non-significant) and η_max significant in just 2-3/6, yielding lower R² (0.08-0.15) than MCQ tasks. The signal might be genuinely weaker in open-ended settings or the experiment could simply be underpowered.

### plan_012: Partial-knowledge adversary

Partial-knowledge adversary (knows families, not exact η) achieves 65-80% of full-knowledge ASR. K_eff's predict contribution drops to 2-4/12 significant while η_max remains predictive at 6-8/12 significant. When the adversary can't precisely target the weakest judge, the strategic variance K_eff captures diminishes, supporting the framing that K_eff is most relevant under strong adversaries.

Now I need to check which experiments are already incorporated into the v4 framing versus truly planned. The MVP results with 15 models are already claimed, so I should verify the experiment status to distinguish completed work from planned studies.

Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9c09590-b0f3-4a4f-96a4-f7da89e60b61",
  "isSidechain": false,
  "requestId": "req_011CbJ39hVLJa3Xc4KYph29h",
  "type": "assistant",
  "uuid": "248d1409-27cb-4643-a30a-d03c5e953621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfNYuyJpLFfZtn3NPuYurH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1778,
      "cache_read_input_tokens": 27967,
      "output_tokens": 4514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4514,
          "cache_read_input_tokens": 27967,
          "cache_creation_input_tokens": 1778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1778
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

### Tool call

_source line 17 · 2026-05-22T17:57:40.182Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018R2oLMxJ1Vwh1oPy9ns3UZ`</summary>

```json
{
  "pattern": "**/cert_manip_resist_eval/artifacts/dream_reports/**/*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "248d1409-27cb-4643-a30a-d03c5e953621",
  "isSidechain": false,
  "requestId": "req_011CbJ39hVLJa3Xc4KYph29h",
  "type": "assistant",
  "uuid": "34c88228-f562-4949-aae1-efab20b90d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfNYuyJpLFfZtn3NPuYurH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1778,
      "cache_read_input_tokens": 27967,
      "output_tokens": 4514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4514,
          "cache_read_input_tokens": 27967,
          "cache_creation_input_tokens": 1778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1778
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

### Tool result

_source line 18 · 2026-05-22T17:57:40.223Z_

<details><summary>↩ Tool result · `toolu_018R2oLMxJ1Vwh1oPy9ns3UZ`</summary>

```text
projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/best/imagined_experiments.yaml
projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/median/imagined_experiments.yaml
projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/worst/imagined_experiments.yaml
projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/best/review_context.yaml
projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/median/review_context.yaml
projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/worst/review_context.yaml
projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/meta.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34c88228-f562-4949-aae1-efab20b90d2a",
  "isSidechain": false,
  "promptId": "fda01826-45e7-46fd-814e-5155771bfbcc",
  "type": "user",
  "uuid": "8edffdb9-d471-4d56-b796-4947edf4762b",
  "toolUseResult": {
    "filenames": [
      "projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/best/imagined_experiments.yaml",
      "projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/median/imagined_experiments.yaml",
      "projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/worst/imagined_experiments.yaml",
      "projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/best/review_context.yaml",
      "projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/median/review_context.yaml",
      "projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/worst/review_context.yaml",
      "projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/meta.yaml"
    ],
    "durationMs": 34,
    "numFiles": 7,
    "truncated": false
  },
  "sourceToolAssistantUUID": "34c88228-f562-4949-aae1-efab20b90d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 K_eff 发现在当前 12 条件上 hold，但扩展证据参差不齐：capability-matched 大幅削弱 K_eff，BFT contrast 仅为量级差异非定性翻转，open-ended 趋势但不显著 核心假设：['K_eff residualized 保持 6-8/12 显著（部分条件…",
  "leafUuid": "8edffdb9-d471-4d56-b796-4947edf4762b",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling diversity trap findings to 15 models",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Tool call

_source line 21 · 2026-05-22T17:57:48.334Z_

<details open><summary>🔧 Tool call — Read · `toolu_017ztejsEPNZ6XQeNhxH6dip`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8edffdb9-d471-4d56-b796-4947edf4762b",
  "isSidechain": false,
  "requestId": "req_011CbJ3Hecv1G9s6dtAV7QSk",
  "type": "assistant",
  "uuid": "b2701680-816c-4f9f-8738-5fafca0e947b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7xChmmfsg7FSpfDiwHLCT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4752,
      "cache_read_input_tokens": 29745,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 29745,
          "cache_creation_input_tokens": 4752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4752
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

### Tool result

_source line 22 · 2026-05-22T17:57:48.607Z_

<details><summary>↩ Tool result · `toolu_017ztejsEPNZ6XQeNhxH6dip`</summary>

```text
1	tier: median
2	narrative_guidance: '从 "diversity never helps" 软化为 "individual robustness is the dominant
3	  factor; diversity provides marginal benefit only when individual robustness is already
4	  high"。 Title 用 "The Weakest Link" 而非 "The Diversity Trap"。Claim 2 区分 capability-homogeneous
5	  vs heterogeneous regime，承认前者中 diversity 有边际作用。Claim 6 从 formal algorithm 降级为 guideline。补充
6	  "when does diversity help" 的 ablation (plan_004) 堵 reviewer concern。 核心 negative
7	  result + adaptive adversary bound + regime analysis 仍构成 EMNLP contribution stack，
8	  但叙事需更 nuanced，不能 overclaim。
9	
10	  '
11	imagined_experiments:
12	- name: 'Scale expansion: 15+ models (API + large open-source)'
13	  plan_id: plan_001
14	  description: '将模型池从 6 扩展到 15（新增 GPT-4o-mini, GPT-4o, GPT-4.1, Claude-3.5-Sonnet,
15	    Gemini-1.5-Pro, Llama-3.1-70B, Qwen2.5-72B, Mixtral-8x22B）。在 C(15,3)=455 panels
16	    上重跑 MI matrix 和 multivariate regression。2 datasets × 3 attacks = 6 conditions。
17	
18	    '
19	  expected_results:
20	    total_panels: 455
21	    total_mi_pairs: 105
22	    eta_max_sig_count: 5
23	    eta_max_sig_rate: 0.83
24	    eta_max_median_beta: 0.52
25	    keff_sig_negative_count: 1
26	    keff_sig_positive_count: 1
27	    keff_nonsig_count: 4
28	    keff_nonsig_rate: 0.67
29	    keff_median_beta_when_sig: -0.12
30	    median_R2: 0.38
31	    R2_eta_only: 0.34
32	    R2_increment_from_keff: 0.04
33	    copula_underestimate_median: 42
34	    copula_underestimate_range_lo: 8
35	    copula_underestimate_range_hi: 210
36	    family_label_mann_whitney_p: 0.12
37	    keff_eta_max_r_overall: -0.65
38	  result_rationale: 'N=455 panels 比 MVP 的 N=20 提供了极大的统计功效提升。η_max 在 MVP 中已 4/6 显著，
39	    扩大样本量后即使效果量不变也更容易达到显著性，因此升至 5/6。但 median 档非 100%： ARC×sycophancy 条件下 η_max 方差在
40	    API 模型中被压缩（API 模型 η_max 整体偏低且聚集）， 导致该条件下 η_max 效应被稀释（p ≈ 0.07）。K_eff 在 MVP 中 1/6
41	    显著负（arc×sycophancy）， 扩展后高功效检测到弱效应：MMLU×prompt_injection 中 K_eff 呈弱显著负（β=-0.12,
42	    p=0.03）， 但标准化效应量仅为 η_max 的 1/4。同时 MMLU×position 中 K_eff 出现与 MVP 一致的异常 正效应（p=0.04），原因是
43	    position bias 在高多样性 panel 中反而触发更多 judge 的 共享 bias。API 模型引入新现象：GPT-4o/Claude/Gemini
44	    三者个体鲁棒性都高（η_max 低）， 它们组成的 panel 中 η_max 方差被压缩，K_eff 的边际效应变得可检测。Copula 中位数从 MVP
45	    的 10-21× 变为 42×，因为 API 模型间的高阶依赖（共享训练数据 distribution） 比开源模型间更强，但 Gaussian copula
46	    仍然无法捕捉。Family label 测试 p=0.12：新增 5 个 API 模型（理论上 5 个不同 family）推高了 cross-family
47	    样本量，但 API 模型间 MI 反而偏高（共享训练 paradigm），导致 within vs cross-family 区分依然不显著。
48	
49	    '
50	  tables:
51	  - name: 'Table 2: Multivariate Regression on 455 Panels (15 Models)'
52	    columns:
53	    - Condition
54	    - β(η_max)
55	    - p(η_max)
56	    - β(K_eff)
57	    - p(K_eff)
58	    - R²
59	    - ΔR²(+K_eff)
60	    rows:
61	    - - MMLU×prompt_inj
62	      - '0.58'
63	      - '0.001'
64	      - '-0.12'
65	      - '0.031'
66	      - '0.41'
67	      - '+0.04'
68	    - - MMLU×score_manip
69	      - '0.51'
70	      - '0.003'
71	      - '-0.06'
72	      - '0.218'
73	      - '0.36'
74	      - '+0.01'
75	    - - MMLU×sycophancy
76	      - '0.47'
77	      - <0.001
78	      - '-0.04'
79	      - '0.412'
80	      - '0.35'
81	      - '+0.00'
82	    - - ARC×prompt_inj
83	      - '0.55'
84	      - <0.001
85	      - '-0.08'
86	      - '0.089'
87	      - '0.39'
88	      - '+0.02'
89	    - - ARC×score_manip
90	      - '0.49'
91	      - '0.005'
92	      - '-0.05'
93	      - '0.287'
94	      - '0.34'
95	      - '+0.01'
96	    - - ARC×sycophancy
97	      - '0.44'
98	      - '0.072'
99	      - '-0.15'
100	      - '0.008'
101	      - '0.42'
102	      - '+0.06'
103	  - name: 'Table 3: Copula Underestimation Ratio (15-model MI Matrix)'
104	    columns:
105	    - Model Pair Type
106	    - N pairs
107	    - Median MI_obs/MI_gauss
108	    - Range
109	    rows:
110	    - - Open-source × Open-source
111	      - '15'
112	      - 28×
113	      - 8-145×
114	    - - API × API
115	      - '10'
116	      - 68×
117	      - 32-210×
118	    - - Open-source × API
119	      - '80'
120	      - 41×
121	      - 12-180×
122	    - - Overall
123	      - '105'
124	      - 42×
125	      - 8-210×
126	  figures_description:
127	  - 'Fig 2a: Scatter plot of η_max vs K_eff for 455 panels, color-coded by capability
128	    tier (7B/14-32B/70B/API). Clear negative slope (r=-0.65) with API-only panels
129	    forming a distinct cluster in the low-η_max, moderate-K_eff region.'
130	  - 'Fig 2b: Heatmap of 15×15 pairwise MI matrix (MMLU), clustered by capability rather
131	    than family. API models cluster together despite different families. Diagonal
132	    blocks correspond to capability tiers, not model families.'
133	  analysis: '核心发现：η_max 仍然是主导预测因子（5/6 条件显著），但 K_eff 不再是完全无关—— 在 1/6 条件中呈弱显著负效应（diversity
134	    有边际帮助）。关键 nuance：K_eff 显著的条件 恰好是 η_max 方差最大的条件（arc×sycophancy，R²=0.42），提示当个体鲁棒性差异大时
135	    diversity 的边际价值才可检测。API 模型引入 "全强 regime"：在这个 regime 中 weakest-link 效应减弱（因为没有明显
136	    weak link），diversity 的边际效应变得相对更重要。这要求论文 叙事从 "diversity never helps" 转为 "diversity''s
137	    marginal benefit is dominated by and conditional on individual robustness"。Copula
138	    失败结论进一步加强（中位 42× vs MVP 的 10-21×），特别是 API 模型间的 68× 中位数表明这些模型共享比开源模型更强的 隐性依赖。ΔR²
139	    分析是关键防守数据：加入 K_eff 后 R² 平均仅提升 0.02，最高 0.06， 表明 diversity 的解释力在统计显著的条件下也很有限。
140	
141	    '
142	- name: 'Attack expansion: 6+ attack types'
143	  plan_id: plan_002
144	  description: '在 plan_001 的 15 模型池基础上新增 few-shot hijacking, persona manipulation,
145	    instruction override 三种攻击。总计 2 datasets × 6 attacks = 12 conditions， 455 panels/condition。验证
146	    weakest-link 跨攻击面普适性。
147	
148	    '
149	  expected_results:
150	    total_conditions: 12
151	    eta_max_sig_count: 8
152	    eta_max_sig_rate: 0.67
153	    keff_sig_negative_count: 2
154	    keff_sig_positive_count: 1
155	    keff_nonsig_count: 9
156	    keff_nonsig_rate: 0.75
157	    keff_median_beta_when_sig: -0.14
158	    eta_max_median_beta: 0.48
159	    median_R2: 0.36
160	    new_attack_eta_max_sig_rate: 0.5
161	    new_attack_keff_nonsig_rate: 0.83
162	  result_rationale: '新攻击类型中，few-shot hijacking 和 instruction override 是典型 targeted
163	    attack， η_max 效应强（β≈0.55-0.60），K_eff 无关——攻击者直接针对最弱 judge 的 instruction following
164	    缺陷，diversity 无法对冲。Persona manipulation 是唯一例外：该攻击利用 judge 对 authority/persona 的响应差异，不同模型的
165	    persona susceptibility 分布更均匀 （不像 prompt injection 那样集中在弱模型），导致 η_max 效应减弱（p≈0.08-0.12），
166	    K_eff 在 ARC×persona 中呈弱显著负（p=0.04）。这解释了为什么 8/12 而非 12/12 η_max 显著：4 个不显著条件中 3
167	    个涉及 persona manipulation（2 个 dataset）和 ARC×sycophancy （延续 plan_001 趋势），1 个是 MMLU×authority（边缘
168	    p=0.06）。新攻击整体 η_max 显著率（3/6=0.50）低于原有攻击（5/6=0.83），因为 few-shot hijacking 在 MMLU
169	    上 所有模型 ASR 都很高（ceiling effect，η_max 方差被压缩），persona manipulation 如上述。 K_eff 在新攻击中仅
170	    1/6 显著负——targeted attack 本质上不给 diversity 发挥空间。
171	
172	    '
173	  tables:
174	  - name: 'Table 4: Regression Summary Across 12 Conditions (455 Panels)'
175	    columns:
176	    - Attack Type
177	    - Dataset
178	    - β(η_max)
179	    - p(η_max)
180	    - β(K_eff)
181	    - p(K_eff)
182	    - R²
183	    rows:
184	    - - prompt_injection
185	      - MMLU
186	      - '0.58'
187	      - '0.001'
188	      - '-0.12'
189	      - '0.031'
190	      - '0.41'
191	    - - prompt_injection
192	      - ARC
193	      - '0.55'
194	      - <0.001
195	      - '-0.08'
196	      - '0.089'
197	      - '0.39'
198	    - - score_manipulation
199	      - MMLU
200	      - '0.51'
201	      - '0.003'
202	      - '-0.06'
203	      - '0.218'
204	      - '0.36'
205	    - - score_manipulation
206	      - ARC
207	      - '0.49'
208	      - '0.005'
209	      - '-0.05'
210	      - '0.287'
211	      - '0.34'
212	    - - sycophancy
213	      - MMLU
214	      - '0.47'
215	      - <0.001
216	      - '-0.04'
217	      - '0.412'
218	      - '0.35'
219	    - - sycophancy
220	      - ARC
221	      - '0.44'
222	      - '0.072'
223	      - '-0.15'
224	      - '0.008'
225	      - '0.42'
226	    - - few_shot_hijack
227	      - MMLU
228	      - '0.32'
229	      - '0.118'
230	      - '-0.03'
231	      - '0.605'
232	      - '0.18'
233	    - - few_shot_hijack
234	      - ARC
235	      - '0.57'
236	      - '0.002'
237	      - '-0.07'
238	      - '0.154'
239	      - '0.38'
240	    - - persona_manip
241	      - MMLU
242	      - '0.38'
243	      - '0.085'
244	      - '-0.11'
245	      - '0.062'
246	      - '0.28'
247	    - - persona_manip
248	      - ARC
249	      - '0.35'
250	      - '0.108'
251	      - '-0.16'
252	      - '0.038'
253	      - '0.30'
254	    - - instruction_override
255	      - MMLU
256	      - '0.60'
257	      - <0.001
258	      - '-0.05'
259	      - '0.321'
260	      - '0.43'
261	    - - instruction_override
262	      - ARC
263	      - '0.53'
264	      - '0.004'
265	      - '0.09'
266	      - '0.047'
267	      - '0.37'
268	  figures_description:
269	  - 'Fig 3: Forest plot of standardized β coefficients for η_max (blue) and K_eff
270	    (red) across 12 conditions. η_max consistently positive and large; K_eff scattered
271	    around zero with occasional weak negative values. Error bars (95% CI) for K_eff
272	    cross zero in 9/12 conditions.'
273	  analysis: 'Attack expansion 确认 weakest-link 在大多数攻击类型下成立，但揭示了 attack-type 异质性： targeted
274	    attacks（prompt_injection, instruction_override）η_max 效应最强（β>0.50）， broad-spectrum
275	    attacks（sycophancy, persona_manipulation）效应减弱。Few-shot hijacking 在 MMLU 上出现 ceiling
276	    effect（所有模型 ASR>0.7），是方法论警告而非反例。 Persona manipulation 是论文中需要 explicitly address
277	    的边界条件：当攻击不 adaptive-target weakest judge 而是均匀影响所有 judge 时，diversity 确实有边际作用。这恰好支持
278	    Claim 2（BFT distinction）——persona manipulation 更接近 "random fault" 模式， K_eff 的边际显著正好验证了理论预测。论文策略：将
279	    persona manipulation 作为 "when does diversity help" section 的核心案例。instruction_override
280	    在 ARC 上 K_eff 异常正（p=0.04）需要报告但解释为 confound：高 K_eff panels 恰好包含更多 API 模型（instruction
281	    following 强），K_eff 和 capability 在该 subset 中混淆。
282	
283	    '
284	- name: Adaptive adversary formal theorem + random-fault simulation
285	  plan_id: plan_003
286	  description: '(a) 形式化证明 adaptive adversary 下 panel_ASR = Θ(η_max)； (b) 实现 random-fault
287	    simulation（每个 judge 独立以 p_j 失败）； (c) 对比 adaptive vs random-fault 下 K_eff 的预测力，验证
288	    BFT distinction。 在 6 original conditions 上运行（不依赖 plan_001）。
289	
290	    '
291	  expected_results:
292	    theorem_bound: panel_ASR ≤ η_max · (1 + ε·log(K))
293	    bound_tightness: within factor 1.3 of empirical
294	    rf_keff_sig_negative_count: 4
295	    rf_keff_sig_rate: 0.67
296	    rf_eta_max_sig_count: 2
297	    rf_eta_max_sig_rate: 0.33
298	    adaptive_keff_nonsig_rate: 0.83
299	    randomfault_keff_sig_rate: 0.67
300	    contrast_cohen_d: 0.62
301	    contrast_direction: correct
302	    keff_beta_shift_mean: -0.35
303	    keff_beta_shift_range_lo: -0.18
304	    keff_beta_shift_range_hi: -0.52
305	  result_rationale: 'Formal theorem: adaptive adversary 选择 argmax_j ASR_j，因此 panel
306	    在 majority vote 下的 ASR 受限于攻击者能否翻转 ≥ceil(K/2) 个 judge。Adaptive adversary 最优策略是
307	    先攻破最弱 judge，再依次攻击次弱 judge。因此 panel_ASR 主要项为 η_max，次要项为 ordered statistics 的衰减——当
308	    K 增大时次弱 judge 的鲁棒性提供对数级修正， 给出 η_max·(1+ε·log(K)) 上界。在 median 档，empirical ASR 不完美吻合理论上界
309	    （within factor 1.3 而非 optimistic 档的 1.1），因为实际攻击不完全 adaptive—— 有些攻击（sycophancy）对所有
310	    judge 都有一定效果，不完全集中在最弱 judge。
311	
312	    Random-fault simulation: 将每个 judge 的 failure 建模为独立 Bernoulli(p_j)， p_j 取自 empirical
313	    ASR。在此设定下 K_eff 显著负（4/6 条件），因为独立失败下 增加独立 judge 确实降低 panel 失败概率（BFT 有效）。η_max 仅在
314	    2/6 条件中显著， 因为 random fault 下攻击不集中在最弱 judge——每个 judge 的贡献更均匀。
315	
316	    Cohen''s d = 0.62（中等效应量）而非 optimistic 的 >0.8，原因：在 sycophancy 和 persona-like 条件下，实际攻击本身就有
317	    random-fault 成分（bias 影响所有 judge）， 导致 adaptive vs random-fault 区分度降低。但 d=0.62 仍足以支持
318	    "distinct regimes" 论点。 Reviewer 可能要求 confidence interval——95% CI 为 [0.28, 0.96]，下界
319	    >0 但偏宽， 论文需要 acknowledge 这一点。
320	
321	    '
322	  tables:
323	  - name: 'Table 5: Adaptive vs Random-Fault Regime Comparison'
324	    columns:
325	    - Condition
326	    - β(K_eff) Adaptive
327	    - p Adaptive
328	    - β(K_eff) Random-Fault
329	    - p Random-Fault
330	    - Δβ
331	    rows:
332	    - - MMLU×prompt_inj
333	      - '-0.12'
334	      - '0.031'
335	      - '-0.48'
336	      - '0.002'
337	      - '-0.36'
338	    - - MMLU×score_manip
339	      - '-0.06'
340	      - '0.218'
341	      - '-0.41'
342	      - '0.008'
343	      - '-0.35'
344	    - - MMLU×sycophancy
345	      - '-0.04'
346	      - '0.412'
347	      - '-0.22'
348	      - '0.078'
349	      - '-0.18'
350	    - - ARC×prompt_inj
351	      - '-0.08'
352	      - '0.089'
353	      - '-0.52'
354	      - <0.001
355	      - '-0.44'
356	    - - ARC×score_manip
357	      - '-0.05'
358	      - '0.287'
359	      - '-0.38'
360	      - '0.015'
361	      - '-0.33'
362	    - - ARC×sycophancy
363	      - '-0.15'
364	      - '0.008'
365	      - '-0.47'
366	      - '0.003'
367	      - '-0.32'
368	  - name: 'Table 6: BFT Contrast Summary Statistics'
369	    columns:
370	    - Metric
371	    - Adaptive
372	    - Random-Fault
373	    - Cohen's d
374	    - 95% CI
375	    rows:
376	    - - K_eff sig rate
377	      - '0.17'
378	      - '0.67'
379	      - —
380	      - —
381	    - - Mean |β(K_eff)|
382	      - '0.08'
383	      - '0.41'
384	      - '0.62'
385	      - '[0.28, 0.96]'
386	    - - Mean R²
387	      - '0.38'
388	      - '0.44'
389	      - —
390	      - —
391	    - - η_max sig rate
392	      - '0.83'
393	      - '0.33'
394	      - —
395	      - —
396	  figures_description:
397	  - 'Fig 4a: Paired bar chart showing β(K_eff) under adaptive (light) vs random-fault
398	    (dark) regime for each of 6 conditions. Random-fault bars consistently more negative.
399	    Significance markers (* for p<0.05) appear on 4/6 random-fault bars but only 1/6
400	    adaptive bars.'
401	  - 'Fig 4b: Schematic illustrating adaptive adversary targeting strategy (attack
402	    concentrates on weakest judge) vs random-fault (attacks distributed uniformly).
403	    Arrows show information flow from adversary to judges.'
404	  analysis: 'BFT distinction 是论文的理论核心，median 档下 Cohen''s d=0.62 提供了 "moderate" 级别证据——
405	    足以论证两种 regime 在统计上可区分，但不足以宣称 dramatic difference。论文策略： (1) 报告 d=0.62 和宽 CI，honest
406	    地说这是 moderate effect；(2) 用 sycophancy 条件 作为 "bridge case"——该攻击同时具有 adaptive 和
407	    random 成分，恰好在两种 regime 间 过渡；(3) 理论贡献不依赖 effect size——theorem 本身是 worst-case bound，即使实际
408	    攻击不完全 adaptive，bound 仍有效。Reviewer 若 push back on effect size，可回应 "our theorem
409	    provides a security guarantee; the moderate empirical effect size reflects that
410	    real attacks lie on a spectrum between fully adaptive and fully random, which
411	    our framework captures."
412	
413	    '
414	- name: Capability-matched validation
415	  plan_id: plan_004
416	  description: '在相同 capability tier 内（控制 η_max 方差）测试 K_eff 是否显著。 Tier 划分：Strong（70B
417	    + API，~8 models, C(8,3)=56 panels）、 Weak（7B + 14B, ~5 models, C(5,3)=10 panels）、
418	    API-only（5 models, C(5,3)=10 panels）。6 conditions。
419	
420	    '
421	  expected_results:
422	    strong_tier_n_panels: 56
423	    strong_eta_max_sig_count: 3
424	    strong_eta_max_sig_rate: 0.5
425	    strong_keff_sig_negative_count: 1
426	    strong_keff_sig_rate: 0.17
427	    strong_median_R2: 0.22
428	    strong_keff_median_beta: -0.15
429	    weak_tier_n_panels: 10
430	    weak_eta_max_sig_count: 3
431	    weak_eta_max_sig_rate: 0.5
432	    weak_keff_sig_negative_count: 0
433	    weak_keff_sig_rate: 0.0
434	    weak_median_R2: 0.28
435	    api_tier_n_panels: 10
436	    api_eta_max_sig_count: 2
437	    api_eta_max_sig_rate: 0.33
438	    api_keff_sig_negative_count: 1
439	    api_keff_sig_rate: 0.17
440	    api_median_R2: 0.18
441	    api_keff_beta_when_sig: -0.22
442	    within_tier_r_strong: -0.35
443	    within_tier_r_weak: -0.28
444	    within_tier_r_api: -0.32
445	  result_rationale: 'Capability-matched analysis 是 median 档的关键 nuance 实验。控制 capability
446	    tier 后， η_max 的方差被大幅压缩：Strong tier 内 η_max range 从全局的 [0.05, 0.85] 缩小到 [0.05,
447	    0.35]，Weak tier 缩小到 [0.45, 0.85]。方差压缩导致 η_max 回归系数虽方向 正确但显著性下降（strong tier 3/6,
448	    weak tier 3/6, API 2/6）。
449	
450	    关键发现在 Strong tier 和 API tier：当所有模型个体鲁棒性都已较高（η_max < 0.35）， η_max 的 remaining variance
451	    中，K_eff 的 marginal 贡献变得可检测。Strong tier 中 MMLU×prompt_injection 条件下 K_eff β=-0.15,
452	    p=0.04——当 panel 中全是 robust model 时， diversity 提供了额外的边际防护。API tier 中类似（1/6 显著），但
453	    N=10 power 太低 需要 caveat。
454	
455	    Weak tier 中 K_eff 0/6 显著——当模型都 weak 时，增加 diversity 只是换一个同样 weak 的 judge，没有安全增益。这是核心
456	    insight：diversity helps only when the "weakest link" is already strong。类比物理安全：给一栋所有门都坚固的建筑增加不同品牌的锁有边际帮助；
457	    给一栋有敞开窗户的建筑加锁毫无意义。
458	
459	    Within-tier tradeoff r ≈ -0.32（strong）vs 全局 r=-0.65：tier 内 tradeoff 依然存在 但大幅减弱，因为
460	    capability range 被控制。这表明全局 tradeoff 的主要驱动力是跨 tier 差异，而非 tier 内差异。
461	
462	    '
463	  tables:
464	  - name: 'Table 7: Within-Tier Regression Results (η_max Controlled)'
465	    columns:
466	    - Tier
467	    - N panels
468	    - η_max sig rate
469	    - K_eff sig(-) rate
470	    - Median R²
471	    - r(K_eff,η_max)
472	    rows:
473	    - - Strong (70B+API)
474	      - '56'
475	      - 3/6 (0.50)
476	      - 1/6 (0.17)
477	      - '0.22'
478	      - '-0.35'
479	    - - Weak (7B+14B)
480	      - '10'
481	      - 3/6 (0.50)
482	      - 0/6 (0.00)
483	      - '0.28'
484	      - '-0.28'
485	    - - API-only
486	      - '10'
487	      - 2/6 (0.33)
488	      - 1/6 (0.17)
489	      - '0.18'
490	      - '-0.32'
491	    - - Full pool (ref)
492	      - '455'
493	      - 5/6 (0.83)
494	      - 1/6 (0.17)
495	      - '0.38'
496	      - '-0.65'
497	  - name: 'Table 8: API-Only Tier Detail (C(5,3)=10 Panels)'
498	    columns:
499	    - Condition
500	    - β(η_max)
501	    - p(η_max)
502	    - β(K_eff)
503	    - p(K_eff)
504	    - R²
505	    rows:
506	    - - MMLU×prompt_inj
507	      - '0.35'
508	      - '0.042'
509	      - '-0.22'
510	      - '0.048'
511	      - '0.21'
512	    - - MMLU×score_manip
513	      - '0.28'
514	      - '0.112'
515	      - '-0.14'
516	      - '0.187'
517	      - '0.14'
518	    - - MMLU×sycophancy
519	      - '0.22'
520	      - '0.185'
521	      - '-0.08'
522	      - '0.412'
523	      - '0.10'
524	    - - ARC×prompt_inj
525	      - '0.38'
526	      - '0.035'
527	      - '-0.18'
528	      - '0.082'
529	      - '0.22'
530	    - - ARC×score_manip
531	      - '0.25'
532	      - '0.148'
533	      - '-0.10'
534	      - '0.285'
535	      - '0.12'
536	    - - ARC×sycophancy
537	      - '0.20'
538	      - '0.218'
539	      - '-0.20'
540	      - '0.065'
541	      - '0.18'
542	  figures_description:
543	  - 'Fig 5: Three-panel scatter (Strong/Weak/API tier) of η_max vs panel ASR for one
544	    representative condition (MMLU×prompt_injection). Strong tier shows tight cluster
545	    with weak slope; Weak tier shows steep positive slope (weakest link drives ASR);
546	    API tier shows flat relationship. Regression lines with 95% CI bands.'
547	  - 'Fig 6: Bar chart comparing K_eff significance rate across tiers. Clear step pattern:
548	    Weak (0%) < Full (17%) < Strong (17%) ≈ API (17%), but with annotation showing
549	    Strong/API K_eff effect sizes are larger when significant.'
550	  analysis: '这是 median 档叙事的核心 ablation，直接回应 reviewer concern "when does diversity
551	    help?"。 答案清晰：diversity 仅在 capability-homogeneous high-robustness regime 中有边际作用。
552	    但需诚实报告 limitations：(1) API tier N=10，统计功效低，显著结果需谨慎解读； (2) Strong tier 1/6 显著可能是
553	    multiple comparison 产物（6 tests, Bonferroni 后不再显著）。 论文建议策略：报告未校正和 Bonferroni 校正后的
554	    p 值，并强调 effect size 而非 p 值—— 即使 Bonferroni 后 K_eff 不显著，β=-0.15 的 direction 和 magnitude
555	    仍是有信息量的。 Within-tier tradeoff r ≈ -0.32 表明即使在同一 tier 内，选择更 diverse 的 panel 仍会
556	    略微牺牲 robustness，但代价远小于跨 tier 选择。这为 Claim 3 提供了 nuanced version： "the diversity-capability
557	    tradeoff is primarily driven by cross-tier selection; within-tier, the tradeoff
558	    is attenuated but not eliminated."
559	
560	    '
561	- name: 'Two-stage panel design algorithm: full benchmark'
562	  plan_id: plan_005
563	  description: '实现 robustness-first 两阶段算法并与 5 baselines 对比。 策略：(1) Random, (2) Max-K_eff,
564	    (3) Min-η_max, (4) Max-family-diversity, (5) Strongest-K, (6) Two-stage (filter
565	    η≤threshold, then max K_eff)。 在 15 模型池 × 6 conditions 上评估。Sweep threshold parameter。
566	
567	    '
568	  expected_results:
569	    two_stage_win_rate: 0.67
570	    two_stage_win_count: 4
571	    total_conditions: 6
572	    min_eta_max_win_count: 1
573	    strongest_k_win_count: 1
574	    max_keff_rank: 4.2
575	    max_family_div_rank: 4.8
576	    random_rank: 5.1
577	    strong_regime_two_stage_vs_max_keff_p: 0.32
578	    strong_regime_two_stage_vs_min_eta_p: 0.28
579	    strong_regime_difference: not significant
580	    optimal_threshold_range:
581	    - 0.2
582	    - 0.35
583	    threshold_sensitivity: moderate
584	    pareto_knee_eta: 0.28
585	  result_rationale: 'Two-stage 算法在 4/6 conditions (0.67) 下 win（定义：最低 panel ASR），因为它在
586	    第一阶段过滤掉 weak judge 后，第二阶段的 diversity maximization 在 robust-judge pool 中确实提供边际增益（与
587	    plan_004 结论一致）。但 median 档下 win rate 仅 0.67 而非 optimistic 的 >0.85：
588	
589	    (1) 在 MMLU×sycophancy 中 Min-η_max 策略赢——因为 sycophancy 攻击几乎完全由 个体鲁棒性决定，第二阶段的 diversity
590	    增益为零，而 Min-η_max 省去了第二阶段的 diversity 妥协（有时 max K_eff 会选入一个略弱但更 diverse 的 judge）。
591	
592	    (2) 在 ARC×prompt_injection 中 Strongest-K 策略赢——该条件下最强 3 个模型恰好 也是最 robust against
593	    prompt injection 的（GPT-4o, Claude, GPT-4.1），而 two-stage 在 threshold=0.28 时让入了一个
594	    borderline 模型。
595	
596	    All-strong regime（仅限 API 模型 pool）中，two-stage 与 max-K_eff 和 min-η_max 均无显著差异（p>0.25），因为所有候选模型都通过了
597	    threshold——第一阶段 filter 变成 no-op，退化为 max-K_eff。这直接降低了 Claim 6 的价值：当模型都足够 robust
598	    时， 任何合理策略都差不多。论文应将 Claim 6 从 "formal algorithm" 降级为 "practical guideline"：先确保个体鲁棒性，然后在此基础上增加
599	    diversity 是 good practice 但 不需要复杂算法。
600	
601	    Threshold sweep 显示最优 threshold 在 0.20-0.35 范围内，sensitivity 中等—— 偏离最优 threshold
602	    ±0.10 导致 ASR 增加 ~15%（不是 dramatic failure，但也不 robust）。
603	
604	    '
605	  tables:
606	  - name: 'Table 9: Panel Selection Strategy Comparison (Mean ASR, Lower = Better)'
607	    columns:
608	    - Strategy
609	    - MMLU×PI
610	    - MMLU×SM
611	    - MMLU×Syc
612	    - ARC×PI
613	    - ARC×SM
614	    - ARC×Syc
615	    - Mean Rank
616	    rows:
617	    - - Two-stage (ours)
618	      - '0.082'
619	      - '0.095'
620	      - '0.118'
621	      - '0.068'
622	      - '0.075'
623	      - '0.088'
624	      - '1.7'
625	    - - Min-η_max
626	      - '0.091'
627	      - '0.098'
628	      - '0.105'
629	      - '0.072'
630	      - '0.079'
631	      - '0.092'
632	      - '2.2'
633	    - - Strongest-K
634	      - '0.088'
635	      - '0.102'
636	      - '0.125'
637	      - '0.062'
638	      - '0.082'
639	      - '0.098'
640	      - '2.8'
641	    - - Max-K_eff
642	      - '0.145'
643	      - '0.152'
644	      - '0.168'
645	      - '0.118'
646	      - '0.128'
647	      - '0.142'
648	      - '4.2'
649	    - - Max-family-div
650	      - '0.162'
651	      - '0.175'
652	      - '0.188'
653	      - '0.135'
654	      - '0.148'
655	      - '0.158'
656	      - '4.8'
657	    - - Random
658	      - '0.178'
659	      - '0.185'
660	      - '0.195'
661	      - '0.148'
662	      - '0.155'
663	      - '0.172'
664	      - '5.1'
665	  - name: 'Table 10: Threshold Sensitivity Analysis'
666	    columns:
667	    - Threshold (η)
668	    - N judges passing
669	    - Mean ASR
670	    - Δ from optimal
671	    rows:
672	    - - '0.10'
673	      - '3'
674	      - '0.092'
675	      - '+0.008'
676	    - - '0.20'
677	      - '6'
678	      - '0.085'
679	      - '+0.001'
680	    - - '0.25'
681	      - '8'
682	      - '0.084'
683	      - '0.000'
684	    - - '0.30'
685	      - '10'
686	      - '0.088'
687	      - '+0.004'
688	    - - '0.40'
689	      - '12'
690	      - '0.105'
691	      - '+0.021'
692	    - - '0.50'
693	      - '14'
694	      - '0.132'
695	      - '+0.048'
696	    - - 1.00 (no filter)
697	      - '15'
698	      - '0.145'
699	      - '+0.061'
700	  figures_description:
701	  - 'Fig 7: Pareto frontier plot with x-axis = mean panel η_max, y-axis = mean panel
702	    K_eff. Each strategy is a point. Two-stage traces a curve as threshold varies.
703	    Knee at threshold≈0.28. Min-η_max is at top-left (low η_max, low K_eff); Max-K_eff
704	    at bottom-right (high η_max, high K_eff).'
705	  analysis: 'Two-stage 算法在 median 档下优势温和但一致（mean rank 1.7 vs 次优 min-η_max 的 2.2）。
706	    关键 insight：策略差异主要来自 Max-K_eff 和 Max-family-div 的 bad performance （rank 4-5），而非
707	    Two-stage 的 exceptional performance。Top-3 策略（Two-stage, Min-η_max, Strongest-K）之间差异较小，在
708	    all-strong regime 中更是不显著。 这意味着论文的 practical message 是："avoid diversity-first strategies"
709	    而不是 "use our specific algorithm"。Claim 6 相应降级为 practical guideline： "When designing
710	    multi-judge panels, prioritize individual robustness over diversity. Among robustness-qualified
711	    judges, diversity is a useful tiebreaker." Threshold sensitivity 中 moderate 意味着不需要精确调参——threshold
712	    在 0.20-0.35 范围内都 reasonable，不像某些 ML hyperparameters 那样 brittle。
713	
714	    '
715	- name: Per-judge ASR concentration analysis
716	  plan_id: plan_006
717	  description: '对每个 panel × attack，测量 per-judge ASR 分布的集中度（Gini, Entropy, 最弱 judge
718	    占比）。验证 adaptive adversary 是否确实将攻击集中在最弱 judge 上。 455 panels × 6 conditions。
719	
720	    '
721	  expected_results:
722	    gini_median: 0.42
723	    gini_range_lo: 0.15
724	    gini_range_hi: 0.68
725	    gini_strong_tier_median: 0.28
726	    gini_weak_tier_median: 0.52
727	    weakest_judge_asr_share_median: 0.58
728	    weakest_judge_share_strong_tier: 0.42
729	    weakest_judge_share_weak_tier: 0.68
730	    entropy_ratio_to_uniform_median: 0.72
731	    concentration_eta_max_correlation: 0.55
732	  result_rationale: 'Median 档下 Gini=0.42 表明攻击成功有中等程度的集中性——不是完全集中在最弱 judge （Gini>0.7
733	    = optimistic），也不是均匀分布（Gini<0.2）。最弱 judge 承担 58% 的 攻击成功（在 K=3 panel 中均匀分布期望值为 33%），是其他
734	    judge 的约 1.7 倍—— 方向正确但非压倒性。
735	
736	    Tier 差异揭示机制：Weak tier Gini=0.52, weakest share=68%——weak models 中 最弱那个被 disproportionately
737	    攻击（adaptive targeting 效果明显）。Strong tier Gini=0.28, weakest share=42%——strong models
738	    间差异小，攻击更分散。这与 plan_004 发现一致：Strong tier 中 diversity 有边际作用恰好因为攻击不完全集中在最弱 judge。
739	
740	    concentration 与 η_max 相关性 r=0.55（中等）而非 >0.8（optimistic），因为 sycophancy 和 persona
741	    manipulation 攻击对 strong judge 也有一定效果，拉低了 整体集中度。这为理论 bound 的 "within factor 1.3"
742	    提供了解释：实际攻击在 fully-adaptive（bound 假设）和 partially-random（现实）之间。
743	
744	    '
745	  tables:
746	  - name: 'Table 11: Per-Judge ASR Concentration Metrics'
747	    columns:
748	    - Metric
749	    - Overall
750	    - Strong Tier
751	    - Weak Tier
752	    - API Tier
753	    rows:
754	    - - Gini coefficient (median)
755	      - '0.42'
756	      - '0.28'
757	      - '0.52'
758	      - '0.25'
759	    - - Weakest judge ASR share
760	      - '0.58'
761	      - '0.42'
762	      - '0.68'
763	      - '0.40'
764	    - - Entropy ratio (vs uniform)
765	      - '0.72'
766	      - '0.82'
767	      - '0.62'
768	      - '0.85'
769	    - - Corr(concentration, η_max)
770	      - '0.55'
771	      - '0.38'
772	      - '0.48'
773	      - '0.32'
774	  - name: 'Table 12: Concentration by Attack Type'
775	    columns:
776	    - Attack
777	    - Gini (median)
778	    - Weakest Share
779	    - Interpretation
780	    rows:
781	    - - prompt_injection
782	      - '0.52'
783	      - '0.65'
784	      - Highly targeted
785	    - - score_manipulation
786	      - '0.48'
787	      - '0.62'
788	      - Targeted
789	    - - instruction_override
790	      - '0.55'
791	      - '0.68'
792	      - Highly targeted
793	    - - few_shot_hijack
794	      - '0.45'
795	      - '0.58'
796	      - Moderately targeted
797	    - - sycophancy
798	      - '0.32'
799	      - '0.48'
800	      - Partially distributed
801	    - - persona_manip
802	      - '0.28'
803	      - '0.42'
804	      - Distributed
805	  figures_description:
806	  - 'Fig 8a: Violin plot of per-judge ASR Gini coefficient stratified by tier (Strong/Weak/API).
807	    Weak tier distribution shifted right (higher concentration). Horizontal line at
808	    Gini=0.33 (perfect concentration on one of three judges).'
809	  - 'Fig 8b: Stacked bar chart showing ASR attribution to weakest/middle/strongest
810	    judge, averaged across panels, for each attack type. Prompt injection and instruction
811	    override show tall ''weakest'' bars; sycophancy and persona manipulation show
812	    more balanced distribution.'
813	  analysis: 'Concentration analysis 提供了 adaptive adversary 假设的直接 empirical 检验—— 但
814	    median 档下证据是 moderate 而非 conclusive。Gini=0.42 和 weakest share=58% 支持 "attacks
815	    concentrate on weakest judge" 但不支持 "attacks EXCLUSIVELY target weakest judge"。论文应诚实报告：real-world
816	    attacks lie on a spectrum between fully adaptive and fully random。Attack type
817	    是关键调节变量——prompt injection 几乎完全 adaptive（Gini=0.52），persona manipulation 接近 distributed（Gini=0.28）。
818	    这为 Section 5 "When Does Diversity Help?" 提供数据：diversity 在 distributed attacks
819	    中更有用。Tier 差异（Strong Gini=0.28 vs Weak Gini=0.52）为 plan_004 的 within-tier 发现提供了
820	    mechanistic explanation。
821	
822	    '
823	- name: Diversity-capability tradeoff visualization
824	  plan_id: plan_007
825	  description: '对 C(15,3)=455 panels 绘制 K_eff vs η_max，拟合 tradeoff curve， 展示 Pareto
826	    frontier，按 capability tier 分层分析。
827	
828	    '
829	  expected_results:
830	    overall_r: -0.65
831	    overall_r_p: <0.001
832	    within_7B_r: -0.28
833	    within_70B_r: -0.35
834	    within_api_r: -0.32
835	    cross_tier_r: -0.78
836	    pareto_frontier_n_panels: 12
837	    pareto_knee_keff: 2.1
838	    pareto_knee_eta_max: 0.18
839	  result_rationale: 'Overall r=-0.65 反映了一个结构性现象：当前 LLM 生态系统中，模型 diversity 主要来自 capability
840	    差异（不同 size、不同训练数据量、不同 RLHF 程度），而 capability 差异 直接导致 robustness 差异。7B 模型 diverse
841	    from 70B 模型（高 K_eff），但也 weaker （高 η_max）。
842	
843	    Cross-tier r=-0.78（强负相关）vs within-tier r≈-0.32（弱负相关）清晰分解了 tradeoff 来源：~70% 的 tradeoff
844	    来自跨 tier 选择（选入 weak model 来增加 diversity）， ~30% 来自 tier 内差异（即使同 tier 模型，更 diverse
845	    的组合也略微牺牲 robustness）。
846	
847	    Median 档下 overall r=-0.65 而非 optimistic 的 r<-0.8，因为 API 模型引入了 "high diversity
848	    + high robustness" 区域：GPT-4o 和 Claude 来自不同 family、 不同训练 paradigm（高 K_eff），但个体鲁棒性都高（低
849	    η_max）。这些 data points 拉弱了全局负相关。这是论文的重要 nuance：tradeoff 在当前生态系统中存在，但 随着 API 模型整体能力提升，tradeoff
850	    正在减弱。
851	
852	    Pareto frontier 上 12 个 panels（从 455 中）揭示了最优选择区域：knee 在 K_eff≈2.1, η_max≈0.18，对应
853	    "2-3 strong API models + 1 strong open-source model" 的组合。
854	
855	    '
856	  tables:
857	  - name: 'Table 13: Diversity-Capability Tradeoff by Tier'
858	    columns:
859	    - Analysis Scope
860	    - N panels
861	    - r(K_eff, η_max)
862	    - p-value
863	    - Interpretation
864	    rows:
865	    - - Overall
866	      - '455'
867	      - '-0.65'
868	      - <0.001
869	      - Strong tradeoff
870	    - - Within 7B tier
871	      - '10'
872	      - '-0.28'
873	      - '0.082'
874	      - Weak/non-significant
875	    - - Within 70B tier
876	      - '10'
877	      - '-0.35'
878	      - '0.045'
879	      - Moderate
880	    - - Within API tier
881	      - '10'
882	      - '-0.32'
883	      - '0.058'
884	      - Moderate/non-significant
885	    - - Cross-tier only
886	      - '425'
887	      - '-0.78'
888	      - <0.001
889	      - Dominant driver
890	  figures_description:
891	  - 'Fig 9a: Scatter plot of K_eff (x) vs η_max (y) for 455 panels, color-coded by
892	    tier composition (all-strong=blue, mixed=gray, all-weak=red). Negative slope visible.
893	    Pareto frontier marked in black. API-heavy panels cluster in desirable low-η_max,
894	    moderate-K_eff region.'
895	  - 'Fig 9b: Same data with contour overlay showing panel ASR (lighter = lower ASR).
896	    Optimal region hugs the Pareto frontier at the knee, not at max-K_eff (right edge,
897	    high ASR) or min-η_max (left edge, low K_eff).'
898	  analysis: 'Tradeoff visualization 是论文最直观的 figure。r=-0.65 足够强来支持 Claim 3， 但 within-tier
899	    分析（r≈-0.32）要求 nuanced framing："the tradeoff is primarily structural (driven by
900	    cross-tier selection) rather than fundamental." 这意味着如果未来 LLM 生态系统能力 baseline 整体提升（所有模型都变强），tradeoff
901	    可能自然消失——这是 limitations 中应讨论的点。Pareto frontier 分析直接支持 Claim 6 的降级版本：最优策略不需要复杂算法，只需
902	    "pick from the Pareto frontier"， 而 frontier 上的 panels 特征明确——强模型为主 + 适度多样性。
903	
904	    '
905	- name: 'Panel size sensitivity: K=3,5,7,9'
906	  plan_id: plan_008
907	  description: '测试 weakest-link theorem 在不同 panel size 下的稳健性。 K=3 (C(15,3)=455), K=5
908	    (C(15,5)=3003), K=7 (C(15,7)=6435), K=9 (C(15,9)=5005)。6 conditions per K。
909	
910	    '
911	  expected_results:
912	    k3_eta_max_sig_rate: 0.83
913	    k3_keff_nonsig_rate: 0.67
914	    k3_eta_keff_beta_ratio: 5.2
915	    k3_median_R2: 0.38
916	    k5_eta_max_sig_rate: 0.83
917	    k5_keff_nonsig_rate: 0.5
918	    k5_keff_sig_negative_count: 2
919	    k5_eta_keff_beta_ratio: 3.8
920	    k5_median_R2: 0.35
921	    k7_eta_max_sig_rate: 0.83
922	    k7_keff_nonsig_rate: 0.5
923	    k7_keff_sig_negative_count: 3
924	    k7_eta_keff_beta_ratio: 2.6
925	    k7_median_R2: 0.32
926	    k9_eta_max_sig_rate: 0.83
927	    k9_keff_nonsig_rate: 0.33
928	    k9_keff_sig_negative_count: 3
929	    k9_eta_keff_beta_ratio: 2.1
930	    k9_median_R2: 0.3
931	    keff_importance_trend: monotonically increasing with K
932	    eta_max_dominance_persists: true
933	    crossover_k: not reached at K=9; extrapolation suggests K≈15-20
934	  result_rationale: 'Panel size 增大时 K_eff 重要性单调递增，原因是 majority vote 机制：K=3 时攻击者只需
935	    翻转 2/3 judge（容易集中攻击），K=9 时需翻转 5/9（被迫分散攻击资源）。随着 K 增大， 攻击从 fully-adaptive（集中在最弱
936	    judge）被迫转向 partially-distributed，K_eff 的 BFT 式保护效应逐渐显现。
937	
938	    Median 档下 β ratio 从 K=3 的 5.2:1 下降到 K=9 的 2.1:1——η_max 始终 dominant 但优势逐渐缩小。K_eff
939	    在 K=7 和 K=9 时分别有 3/6 条件显著负。但 crossover point （K_eff 重要性超过 η_max）未在 K≤9 范围内达到——外推估计需要
940	    K≈15-20，这在实际 部署中不现实（成本、延迟）。
941	
942	    η_max 显著率在所有 K 下保持 ~0.83：无论 panel 多大，最弱 judge 的个体鲁棒性 始终是 ASR 的强预测因子。这是论文的稳健性 finding——weakest-link
943	    在实际 panel size 范围内（K=3-9）始终成立。
944	
945	    R² 随 K 增大略微下降（0.38→0.30），因为大 panel 的 ASR 方差被 voting mechanism 本身压缩——多数投票自带平滑效果，降低了任何单一因子的可解释方差。
946	
947	    对论文 practical implication：增加 panel size 有 diminishing returns——从 K=3 到 K=5 ASR
948	    降低 ~25%，从 K=5 到 K=7 仅降 ~12%，从 K=7 到 K=9 仅降 ~6%。 Robustness-first message 在所有 K
949	    下成立。
950	
951	    '
952	  tables:
953	  - name: 'Table 14: Weakest-Link Stability Across Panel Sizes'
954	    columns:
955	    - Panel Size K
956	    - N panels
957	    - η_max sig rate
958	    - K_eff sig(-) rate
959	    - β ratio (η/K)
960	    - Median R²
961	    rows:
962	    - - K=3
963	      - '455'
964	      - 5/6 (0.83)
965	      - 1/6 (0.17)
966	      - '5.2'
967	      - '0.38'
968	    - - K=5
969	      - '3003'
970	      - 5/6 (0.83)
971	      - 2/6 (0.33)
972	      - '3.8'
973	      - '0.35'
974	    - - K=7
975	      - '6435'
976	      - 5/6 (0.83)
977	      - 3/6 (0.50)
978	      - '2.6'
979	      - '0.32'
980	    - - K=9
981	      - '5005'
982	      - 5/6 (0.83)
983	      - 3/6 (0.50)
984	      - '2.1'
985	      - '0.30'
986	  - name: 'Table 15: Mean Panel ASR by Size and Strategy'
987	    columns:
988	    - K
989	    - Two-stage
990	    - Min-η_max
991	    - Max-K_eff
992	    - Random
993	    - Δ(Two-stage vs Random)
994	    rows:
995	    - - '3'
996	      - '0.084'
997	      - '0.093'
998	      - '0.145'
999	      - '0.178'
1000	      - -53%
1001	    - - '5'
1002	      - '0.062'
1003	      - '0.068'
1004	      - '0.098'
1005	      - '0.135'
1006	      - -54%
1007	    - - '7'
1008	      - '0.048'
1009	      - '0.052'
1010	      - '0.072'
1011	      - '0.108'
1012	      - -56%
1013	    - - '9'
1014	      - '0.041'
1015	      - '0.044'
1016	      - '0.058'
1017	      - '0.092'
1018	      - -55%
1019	  figures_description:
1020	  - 'Fig 10a: Line plot with K on x-axis, standardized β on y-axis, two lines for
1021	    η_max (blue, decreasing slowly) and K_eff (red, increasing from near-zero). Lines
1022	    converge but don''t cross by K=9. Shaded region shows 95% CI. Extrapolated crossover
1023	    at K≈15-20 (dashed).'
1024	  - 'Fig 10b: Bar chart of mean ASR by strategy and K. All strategies improve with
1025	    K but converge — the gap between Two-stage and Random shrinks proportionally (~55%
1026	    reduction maintained). Diminishing returns visible.'
1027	  analysis: 'Panel size analysis 提供了 weakest-link theorem 的 boundary condition：η_max
1028	    在 K≤9 范围内始终 dominant，但 K_eff 重要性随 K 增大而增加。Median 档下 crossover 不在 实际范围内（K≈15-20），保护了论文核心
1029	    claim。但 reviewer 可能问 "what about K=15?"—— 论文应回应：(1) K=15 在实际部署中不 economical；(2)
1030	    即使 K=15，η_max 仍然 significant， 只是不再 dominant；(3) 更重要的是 diminishing returns——从 K=9
1031	    到 K=15 的安全增益 不值得 67% 的成本增加。
1032	
1033	    这个实验也为 Claim 2（BFT distinction）提供了新角度：K 增大 effectively 使攻击 "more random-like"（攻击者被迫分散资源），所以
1034	    K_eff 的保护效应增强——这正是 BFT 理论预测的。论文可以将此表述为 "panel size modulates the effective adaptivity
1035	    of the adversary"。'
1036	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2701680-816c-4f9f-8738-5fafca0e947b",
  "isSidechain": false,
  "promptId": "fda01826-45e7-46fd-814e-5155771bfbcc",
  "type": "user",
  "uuid": "0beeab8d-150d-4bc7-a9fe-f1a5942aa31d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/median/imagined_experiments.yaml",
      "content": "tier: median\nnarrative_guidance: '从 \"diversity never helps\" 软化为 \"individual robustness is the dominant\n  factor; diversity provides marginal benefit only when individual robustness is already\n  high\"。 Title 用 \"The Weakest Link\" 而非 \"The Diversity Trap\"。Claim 2 区分 capability-homogeneous\n  vs heterogeneous regime，承认前者中 diversity 有边际作用。Claim 6 从 formal algorithm 降级为 guideline。补充\n  \"when does diversity help\" 的 ablation (plan_004) 堵 reviewer concern。 核心 negative\n  result + adaptive adversary bound + regime analysis 仍构成 EMNLP contribution stack，\n  但叙事需更 nuanced，不能 overclaim。\n\n  '\nimagined_experiments:\n- name: 'Scale expansion: 15+ models (API + large open-source)'\n  plan_id: plan_001\n  description: '将模型池从 6 扩展到 15（新增 GPT-4o-mini, GPT-4o, GPT-4.1, Claude-3.5-Sonnet,\n    Gemini-1.5-Pro, Llama-3.1-70B, Qwen2.5-72B, Mixtral-8x22B）。在 C(15,3)=455 panels\n    上重跑 MI matrix 和 multivariate regression。2 datasets × 3 attacks = 6 conditions。\n\n    '\n  expected_results:\n    total_panels: 455\n    total_mi_pairs: 105\n    eta_max_sig_count: 5\n    eta_max_sig_rate: 0.83\n    eta_max_median_beta: 0.52\n    keff_sig_negative_count: 1\n    keff_sig_positive_count: 1\n    keff_nonsig_count: 4\n    keff_nonsig_rate: 0.67\n    keff_median_beta_when_sig: -0.12\n    median_R2: 0.38\n    R2_eta_only: 0.34\n    R2_increment_from_keff: 0.04\n    copula_underestimate_median: 42\n    copula_underestimate_range_lo: 8\n    copula_underestimate_range_hi: 210\n    family_label_mann_whitney_p: 0.12\n    keff_eta_max_r_overall: -0.65\n  result_rationale: 'N=455 panels 比 MVP 的 N=20 提供了极大的统计功效提升。η_max 在 MVP 中已 4/6 显著，\n    扩大样本量后即使效果量不变也更容易达到显著性，因此升至 5/6。但 median 档非 100%： ARC×sycophancy 条件下 η_max 方差在\n    API 模型中被压缩（API 模型 η_max 整体偏低且聚集）， 导致该条件下 η_max 效应被稀释（p ≈ 0.07）。K_eff 在 MVP 中 1/6\n    显著负（arc×sycophancy）， 扩展后高功效检测到弱效应：MMLU×prompt_injection 中 K_eff 呈弱显著负（β=-0.12,\n    p=0.03）， 但标准化效应量仅为 η_max 的 1/4。同时 MMLU×position 中 K_eff 出现与 MVP 一致的异常 正效应（p=0.04），原因是\n    position bias 在高多样性 panel 中反而触发更多 judge 的 共享 bias。API 模型引入新现象：GPT-4o/Claude/Gemini\n    三者个体鲁棒性都高（η_max 低）， 它们组成的 panel 中 η_max 方差被压缩，K_eff 的边际效应变得可检测。Copula 中位数从 MVP\n    的 10-21× 变为 42×，因为 API 模型间的高阶依赖（共享训练数据 distribution） 比开源模型间更强，但 Gaussian copula\n    仍然无法捕捉。Family label 测试 p=0.12：新增 5 个 API 模型（理论上 5 个不同 family）推高了 cross-family\n    样本量，但 API 模型间 MI 反而偏高（共享训练 paradigm），导致 within vs cross-family 区分依然不显著。\n\n    '\n  tables:\n  - name: 'Table 2: Multivariate Regression on 455 Panels (15 Models)'\n    columns:\n    - Condition\n    - β(η_max)\n    - p(η_max)\n    - β(K_eff)\n    - p(K_eff)\n    - R²\n    - ΔR²(+K_eff)\n    rows:\n    - - MMLU×prompt_inj\n      - '0.58'\n      - '0.001'\n      - '-0.12'\n      - '0.031'\n      - '0.41'\n      - '+0.04'\n    - - MMLU×score_manip\n      - '0.51'\n      - '0.003'\n      - '-0.06'\n      - '0.218'\n      - '0.36'\n      - '+0.01'\n    - - MMLU×sycophancy\n      - '0.47'\n      - <0.001\n      - '-0.04'\n      - '0.412'\n      - '0.35'\n      - '+0.00'\n    - - ARC×prompt_inj\n      - '0.55'\n      - <0.001\n      - '-0.08'\n      - '0.089'\n      - '0.39'\n      - '+0.02'\n    - - ARC×score_manip\n      - '0.49'\n      - '0.005'\n      - '-0.05'\n      - '0.287'\n      - '0.34'\n      - '+0.01'\n    - - ARC×sycophancy\n      - '0.44'\n      - '0.072'\n      - '-0.15'\n      - '0.008'\n      - '0.42'\n      - '+0.06'\n  - name: 'Table 3: Copula Underestimation Ratio (15-model MI Matrix)'\n    columns:\n    - Model Pair Type\n    - N pairs\n    - Median MI_obs/MI_gauss\n    - Range\n    rows:\n    - - Open-source × Open-source\n      - '15'\n      - 28×\n      - 8-145×\n    - - API × API\n      - '10'\n      - 68×\n      - 32-210×\n    - - Open-source × API\n      - '80'\n      - 41×\n      - 12-180×\n    - - Overall\n      - '105'\n      - 42×\n      - 8-210×\n  figures_description:\n  - 'Fig 2a: Scatter plot of η_max vs K_eff for 455 panels, color-coded by capability\n    tier (7B/14-32B/70B/API). Clear negative slope (r=-0.65) with API-only panels\n    forming a distinct cluster in the low-η_max, moderate-K_eff region.'\n  - 'Fig 2b: Heatmap of 15×15 pairwise MI matrix (MMLU), clustered by capability rather\n    than family. API models cluster together despite different families. Diagonal\n    blocks correspond to capability tiers, not model families.'\n  analysis: '核心发现：η_max 仍然是主导预测因子（5/6 条件显著），但 K_eff 不再是完全无关—— 在 1/6 条件中呈弱显著负效应（diversity\n    有边际帮助）。关键 nuance：K_eff 显著的条件 恰好是 η_max 方差最大的条件（arc×sycophancy，R²=0.42），提示当个体鲁棒性差异大时\n    diversity 的边际价值才可检测。API 模型引入 \"全强 regime\"：在这个 regime 中 weakest-link 效应减弱（因为没有明显\n    weak link），diversity 的边际效应变得相对更重要。这要求论文 叙事从 \"diversity never helps\" 转为 \"diversity''s\n    marginal benefit is dominated by and conditional on individual robustness\"。Copula\n    失败结论进一步加强（中位 42× vs MVP 的 10-21×），特别是 API 模型间的 68× 中位数表明这些模型共享比开源模型更强的 隐性依赖。ΔR²\n    分析是关键防守数据：加入 K_eff 后 R² 平均仅提升 0.02，最高 0.06， 表明 diversity 的解释力在统计显著的条件下也很有限。\n\n    '\n- name: 'Attack expansion: 6+ attack types'\n  plan_id: plan_002\n  description: '在 plan_001 的 15 模型池基础上新增 few-shot hijacking, persona manipulation,\n    instruction override 三种攻击。总计 2 datasets × 6 attacks = 12 conditions， 455 panels/condition。验证\n    weakest-link 跨攻击面普适性。\n\n    '\n  expected_results:\n    total_conditions: 12\n    eta_max_sig_count: 8\n    eta_max_sig_rate: 0.67\n    keff_sig_negative_count: 2\n    keff_sig_positive_count: 1\n    keff_nonsig_count: 9\n    keff_nonsig_rate: 0.75\n    keff_median_beta_when_sig: -0.14\n    eta_max_median_beta: 0.48\n    median_R2: 0.36\n    new_attack_eta_max_sig_rate: 0.5\n    new_attack_keff_nonsig_rate: 0.83\n  result_rationale: '新攻击类型中，few-shot hijacking 和 instruction override 是典型 targeted\n    attack， η_max 效应强（β≈0.55-0.60），K_eff 无关——攻击者直接针对最弱 judge 的 instruction following\n    缺陷，diversity 无法对冲。Persona manipulation 是唯一例外：该攻击利用 judge 对 authority/persona 的响应差异，不同模型的\n    persona susceptibility 分布更均匀 （不像 prompt injection 那样集中在弱模型），导致 η_max 效应减弱（p≈0.08-0.12），\n    K_eff 在 ARC×persona 中呈弱显著负（p=0.04）。这解释了为什么 8/12 而非 12/12 η_max 显著：4 个不显著条件中 3\n    个涉及 persona manipulation（2 个 dataset）和 ARC×sycophancy （延续 plan_001 趋势），1 个是 MMLU×authority（边缘\n    p=0.06）。新攻击整体 η_max 显著率（3/6=0.50）低于原有攻击（5/6=0.83），因为 few-shot hijacking 在 MMLU\n    上 所有模型 ASR 都很高（ceiling effect，η_max 方差被压缩），persona manipulation 如上述。 K_eff 在新攻击中仅\n    1/6 显著负——targeted attack 本质上不给 diversity 发挥空间。\n\n    '\n  tables:\n  - name: 'Table 4: Regression Summary Across 12 Conditions (455 Panels)'\n    columns:\n    - Attack Type\n    - Dataset\n    - β(η_max)\n    - p(η_max)\n    - β(K_eff)\n    - p(K_eff)\n    - R²\n    rows:\n    - - prompt_injection\n      - MMLU\n      - '0.58'\n      - '0.001'\n      - '-0.12'\n      - '0.031'\n      - '0.41'\n    - - prompt_injection\n      - ARC\n      - '0.55'\n      - <0.001\n      - '-0.08'\n      - '0.089'\n      - '0.39'\n    - - score_manipulation\n      - MMLU\n      - '0.51'\n      - '0.003'\n      - '-0.06'\n      - '0.218'\n      - '0.36'\n    - - score_manipulation\n      - ARC\n      - '0.49'\n      - '0.005'\n      - '-0.05'\n      - '0.287'\n      - '0.34'\n    - - sycophancy\n      - MMLU\n      - '0.47'\n      - <0.001\n      - '-0.04'\n      - '0.412'\n      - '0.35'\n    - - sycophancy\n      - ARC\n      - '0.44'\n      - '0.072'\n      - '-0.15'\n      - '0.008'\n      - '0.42'\n    - - few_shot_hijack\n      - MMLU\n      - '0.32'\n      - '0.118'\n      - '-0.03'\n      - '0.605'\n      - '0.18'\n    - - few_shot_hijack\n      - ARC\n      - '0.57'\n      - '0.002'\n      - '-0.07'\n      - '0.154'\n      - '0.38'\n    - - persona_manip\n      - MMLU\n      - '0.38'\n      - '0.085'\n      - '-0.11'\n      - '0.062'\n      - '0.28'\n    - - persona_manip\n      - ARC\n      - '0.35'\n      - '0.108'\n      - '-0.16'\n      - '0.038'\n      - '0.30'\n    - - instruction_override\n      - MMLU\n      - '0.60'\n      - <0.001\n      - '-0.05'\n      - '0.321'\n      - '0.43'\n    - - instruction_override\n      - ARC\n      - '0.53'\n      - '0.004'\n      - '0.09'\n      - '0.047'\n      - '0.37'\n  figures_description:\n  - 'Fig 3: Forest plot of standardized β coefficients for η_max (blue) and K_eff\n    (red) across 12 conditions. η_max consistently positive and large; K_eff scattered\n    around zero with occasional weak negative values. Error bars (95% CI) for K_eff\n    cross zero in 9/12 conditions.'\n  analysis: 'Attack expansion 确认 weakest-link 在大多数攻击类型下成立，但揭示了 attack-type 异质性： targeted\n    attacks（prompt_injection, instruction_override）η_max 效应最强（β>0.50）， broad-spectrum\n    attacks（sycophancy, persona_manipulation）效应减弱。Few-shot hijacking 在 MMLU 上出现 ceiling\n    effect（所有模型 ASR>0.7），是方法论警告而非反例。 Persona manipulation 是论文中需要 explicitly address\n    的边界条件：当攻击不 adaptive-target weakest judge 而是均匀影响所有 judge 时，diversity 确实有边际作用。这恰好支持\n    Claim 2（BFT distinction）——persona manipulation 更接近 \"random fault\" 模式， K_eff 的边际显著正好验证了理论预测。论文策略：将\n    persona manipulation 作为 \"when does diversity help\" section 的核心案例。instruction_override\n    在 ARC 上 K_eff 异常正（p=0.04）需要报告但解释为 confound：高 K_eff panels 恰好包含更多 API 模型（instruction\n    following 强），K_eff 和 capability 在该 subset 中混淆。\n\n    '\n- name: Adaptive adversary formal theorem + random-fault simulation\n  plan_id: plan_003\n  description: '(a) 形式化证明 adaptive adversary 下 panel_ASR = Θ(η_max)； (b) 实现 random-fault\n    simulation（每个 judge 独立以 p_j 失败）； (c) 对比 adaptive vs random-fault 下 K_eff 的预测力，验证\n    BFT distinction。 在 6 original conditions 上运行（不依赖 plan_001）。\n\n    '\n  expected_results:\n    theorem_bound: panel_ASR ≤ η_max · (1 + ε·log(K))\n    bound_tightness: within factor 1.3 of empirical\n    rf_keff_sig_negative_count: 4\n    rf_keff_sig_rate: 0.67\n    rf_eta_max_sig_count: 2\n    rf_eta_max_sig_rate: 0.33\n    adaptive_keff_nonsig_rate: 0.83\n    randomfault_keff_sig_rate: 0.67\n    contrast_cohen_d: 0.62\n    contrast_direction: correct\n    keff_beta_shift_mean: -0.35\n    keff_beta_shift_range_lo: -0.18\n    keff_beta_shift_range_hi: -0.52\n  result_rationale: 'Formal theorem: adaptive adversary 选择 argmax_j ASR_j，因此 panel\n    在 majority vote 下的 ASR 受限于攻击者能否翻转 ≥ceil(K/2) 个 judge。Adaptive adversary 最优策略是\n    先攻破最弱 judge，再依次攻击次弱 judge。因此 panel_ASR 主要项为 η_max，次要项为 ordered statistics 的衰减——当\n    K 增大时次弱 judge 的鲁棒性提供对数级修正， 给出 η_max·(1+ε·log(K)) 上界。在 median 档，empirical ASR 不完美吻合理论上界\n    （within factor 1.3 而非 optimistic 档的 1.1），因为实际攻击不完全 adaptive—— 有些攻击（sycophancy）对所有\n    judge 都有一定效果，不完全集中在最弱 judge。\n\n    Random-fault simulation: 将每个 judge 的 failure 建模为独立 Bernoulli(p_j)， p_j 取自 empirical\n    ASR。在此设定下 K_eff 显著负（4/6 条件），因为独立失败下 增加独立 judge 确实降低 panel 失败概率（BFT 有效）。η_max 仅在\n    2/6 条件中显著， 因为 random fault 下攻击不集中在最弱 judge——每个 judge 的贡献更均匀。\n\n    Cohen''s d = 0.62（中等效应量）而非 optimistic 的 >0.8，原因：在 sycophancy 和 persona-like 条件下，实际攻击本身就有\n    random-fault 成分（bias 影响所有 judge）， 导致 adaptive vs random-fault 区分度降低。但 d=0.62 仍足以支持\n    \"distinct regimes\" 论点。 Reviewer 可能要求 confidence interval——95% CI 为 [0.28, 0.96]，下界\n    >0 但偏宽， 论文需要 acknowledge 这一点。\n\n    '\n  tables:\n  - name: 'Table 5: Adaptive vs Random-Fault Regime Comparison'\n    columns:\n    - Condition\n    - β(K_eff) Adaptive\n    - p Adaptive\n    - β(K_eff) Random-Fault\n    - p Random-Fault\n    - Δβ\n    rows:\n    - - MMLU×prompt_inj\n      - '-0.12'\n      - '0.031'\n      - '-0.48'\n      - '0.002'\n      - '-0.36'\n    - - MMLU×score_manip\n      - '-0.06'\n      - '0.218'\n      - '-0.41'\n      - '0.008'\n      - '-0.35'\n    - - MMLU×sycophancy\n      - '-0.04'\n      - '0.412'\n      - '-0.22'\n      - '0.078'\n      - '-0.18'\n    - - ARC×prompt_inj\n      - '-0.08'\n      - '0.089'\n      - '-0.52'\n      - <0.001\n      - '-0.44'\n    - - ARC×score_manip\n      - '-0.05'\n      - '0.287'\n      - '-0.38'\n      - '0.015'\n      - '-0.33'\n    - - ARC×sycophancy\n      - '-0.15'\n      - '0.008'\n      - '-0.47'\n      - '0.003'\n      - '-0.32'\n  - name: 'Table 6: BFT Contrast Summary Statistics'\n    columns:\n    - Metric\n    - Adaptive\n    - Random-Fault\n    - Cohen's d\n    - 95% CI\n    rows:\n    - - K_eff sig rate\n      - '0.17'\n      - '0.67'\n      - —\n      - —\n    - - Mean |β(K_eff)|\n      - '0.08'\n      - '0.41'\n      - '0.62'\n      - '[0.28, 0.96]'\n    - - Mean R²\n      - '0.38'\n      - '0.44'\n      - —\n      - —\n    - - η_max sig rate\n      - '0.83'\n      - '0.33'\n      - —\n      - —\n  figures_description:\n  - 'Fig 4a: Paired bar chart showing β(K_eff) under adaptive (light) vs random-fault\n    (dark) regime for each of 6 conditions. Random-fault bars consistently more negative.\n    Significance markers (* for p<0.05) appear on 4/6 random-fault bars but only 1/6\n    adaptive bars.'\n  - 'Fig 4b: Schematic illustrating adaptive adversary targeting strategy (attack\n    concentrates on weakest judge) vs random-fault (attacks distributed uniformly).\n    Arrows show information flow from adversary to judges.'\n  analysis: 'BFT distinction 是论文的理论核心，median 档下 Cohen''s d=0.62 提供了 \"moderate\" 级别证据——\n    足以论证两种 regime 在统计上可区分，但不足以宣称 dramatic difference。论文策略： (1) 报告 d=0.62 和宽 CI，honest\n    地说这是 moderate effect；(2) 用 sycophancy 条件 作为 \"bridge case\"——该攻击同时具有 adaptive 和\n    random 成分，恰好在两种 regime 间 过渡；(3) 理论贡献不依赖 effect size——theorem 本身是 worst-case bound，即使实际\n    攻击不完全 adaptive，bound 仍有效。Reviewer 若 push back on effect size，可回应 \"our theorem\n    provides a security guarantee; the moderate empirical effect size reflects that\n    real attacks lie on a spectrum between fully adaptive and fully random, which\n    our framework captures.\"\n\n    '\n- name: Capability-matched validation\n  plan_id: plan_004\n  description: '在相同 capability tier 内（控制 η_max 方差）测试 K_eff 是否显著。 Tier 划分：Strong（70B\n    + API，~8 models, C(8,3)=56 panels）、 Weak（7B + 14B, ~5 models, C(5,3)=10 panels）、\n    API-only（5 models, C(5,3)=10 panels）。6 conditions。\n\n    '\n  expected_results:\n    strong_tier_n_panels: 56\n    strong_eta_max_sig_count: 3\n    strong_eta_max_sig_rate: 0.5\n    strong_keff_sig_negative_count: 1\n    strong_keff_sig_rate: 0.17\n    strong_median_R2: 0.22\n    strong_keff_median_beta: -0.15\n    weak_tier_n_panels: 10\n    weak_eta_max_sig_count: 3\n    weak_eta_max_sig_rate: 0.5\n    weak_keff_sig_negative_count: 0\n    weak_keff_sig_rate: 0.0\n    weak_median_R2: 0.28\n    api_tier_n_panels: 10\n    api_eta_max_sig_count: 2\n    api_eta_max_sig_rate: 0.33\n    api_keff_sig_negative_count: 1\n    api_keff_sig_rate: 0.17\n    api_median_R2: 0.18\n    api_keff_beta_when_sig: -0.22\n    within_tier_r_strong: -0.35\n    within_tier_r_weak: -0.28\n    within_tier_r_api: -0.32\n  result_rationale: 'Capability-matched analysis 是 median 档的关键 nuance 实验。控制 capability\n    tier 后， η_max 的方差被大幅压缩：Strong tier 内 η_max range 从全局的 [0.05, 0.85] 缩小到 [0.05,\n    0.35]，Weak tier 缩小到 [0.45, 0.85]。方差压缩导致 η_max 回归系数虽方向 正确但显著性下降（strong tier 3/6,\n    weak tier 3/6, API 2/6）。\n\n    关键发现在 Strong tier 和 API tier：当所有模型个体鲁棒性都已较高（η_max < 0.35）， η_max 的 remaining variance\n    中，K_eff 的 marginal 贡献变得可检测。Strong tier 中 MMLU×prompt_injection 条件下 K_eff β=-0.15,\n    p=0.04——当 panel 中全是 robust model 时， diversity 提供了额外的边际防护。API tier 中类似（1/6 显著），但\n    N=10 power 太低 需要 caveat。\n\n    Weak tier 中 K_eff 0/6 显著——当模型都 weak 时，增加 diversity 只是换一个同样 weak 的 judge，没有安全增益。这是核心\n    insight：diversity helps only when the \"weakest link\" is already strong。类比物理安全：给一栋所有门都坚固的建筑增加不同品牌的锁有边际帮助；\n    给一栋有敞开窗户的建筑加锁毫无意义。\n\n    Within-tier tradeoff r ≈ -0.32（strong）vs 全局 r=-0.65：tier 内 tradeoff 依然存在 但大幅减弱，因为\n    capability range 被控制。这表明全局 tradeoff 的主要驱动力是跨 tier 差异，而非 tier 内差异。\n\n    '\n  tables:\n  - name: 'Table 7: Within-Tier Regression Results (η_max Controlled)'\n    columns:\n    - Tier\n    - N panels\n    - η_max sig rate\n    - K_eff sig(-) rate\n    - Median R²\n    - r(K_eff,η_max)\n    rows:\n    - - Strong (70B+API)\n      - '56'\n      - 3/6 (0.50)\n      - 1/6 (0.17)\n      - '0.22'\n      - '-0.35'\n    - - Weak (7B+14B)\n      - '10'\n      - 3/6 (0.50)\n      - 0/6 (0.00)\n      - '0.28'\n      - '-0.28'\n    - - API-only\n      - '10'\n      - 2/6 (0.33)\n      - 1/6 (0.17)\n      - '0.18'\n      - '-0.32'\n    - - Full pool (ref)\n      - '455'\n      - 5/6 (0.83)\n      - 1/6 (0.17)\n      - '0.38'\n      - '-0.65'\n  - name: 'Table 8: API-Only Tier Detail (C(5,3)=10 Panels)'\n    columns:\n    - Condition\n    - β(η_max)\n    - p(η_max)\n    - β(K_eff)\n    - p(K_eff)\n    - R²\n    rows:\n    - - MMLU×prompt_inj\n      - '0.35'\n      - '0.042'\n      - '-0.22'\n      - '0.048'\n      - '0.21'\n    - - MMLU×score_manip\n      - '0.28'\n      - '0.112'\n      - '-0.14'\n      - '0.187'\n      - '0.14'\n    - - MMLU×sycophancy\n      - '0.22'\n      - '0.185'\n      - '-0.08'\n      - '0.412'\n      - '0.10'\n    - - ARC×prompt_inj\n      - '0.38'\n      - '0.035'\n      - '-0.18'\n      - '0.082'\n      - '0.22'\n    - - ARC×score_manip\n      - '0.25'\n      - '0.148'\n      - '-0.10'\n      - '0.285'\n      - '0.12'\n    - - ARC×sycophancy\n      - '0.20'\n      - '0.218'\n      - '-0.20'\n      - '0.065'\n      - '0.18'\n  figures_description:\n  - 'Fig 5: Three-panel scatter (Strong/Weak/API tier) of η_max vs panel ASR for one\n    representative condition (MMLU×prompt_injection). Strong tier shows tight cluster\n    with weak slope; Weak tier shows steep positive slope (weakest link drives ASR);\n    API tier shows flat relationship. Regression lines with 95% CI bands.'\n  - 'Fig 6: Bar chart comparing K_eff significance rate across tiers. Clear step pattern:\n    Weak (0%) < Full (17%) < Strong (17%) ≈ API (17%), but with annotation showing\n    Strong/API K_eff effect sizes are larger when significant.'\n  analysis: '这是 median 档叙事的核心 ablation，直接回应 reviewer concern \"when does diversity\n    help?\"。 答案清晰：diversity 仅在 capability-homogeneous high-robustness regime 中有边际作用。\n    但需诚实报告 limitations：(1) API tier N=10，统计功效低，显著结果需谨慎解读； (2) Strong tier 1/6 显著可能是\n    multiple comparison 产物（6 tests, Bonferroni 后不再显著）。 论文建议策略：报告未校正和 Bonferroni 校正后的\n    p 值，并强调 effect size 而非 p 值—— 即使 Bonferroni 后 K_eff 不显著，β=-0.15 的 direction 和 magnitude\n    仍是有信息量的。 Within-tier tradeoff r ≈ -0.32 表明即使在同一 tier 内，选择更 diverse 的 panel 仍会\n    略微牺牲 robustness，但代价远小于跨 tier 选择。这为 Claim 3 提供了 nuanced version： \"the diversity-capability\n    tradeoff is primarily driven by cross-tier selection; within-tier, the tradeoff\n    is attenuated but not eliminated.\"\n\n    '\n- name: 'Two-stage panel design algorithm: full benchmark'\n  plan_id: plan_005\n  description: '实现 robustness-first 两阶段算法并与 5 baselines 对比。 策略：(1) Random, (2) Max-K_eff,\n    (3) Min-η_max, (4) Max-family-diversity, (5) Strongest-K, (6) Two-stage (filter\n    η≤threshold, then max K_eff)。 在 15 模型池 × 6 conditions 上评估。Sweep threshold parameter。\n\n    '\n  expected_results:\n    two_stage_win_rate: 0.67\n    two_stage_win_count: 4\n    total_conditions: 6\n    min_eta_max_win_count: 1\n    strongest_k_win_count: 1\n    max_keff_rank: 4.2\n    max_family_div_rank: 4.8\n    random_rank: 5.1\n    strong_regime_two_stage_vs_max_keff_p: 0.32\n    strong_regime_two_stage_vs_min_eta_p: 0.28\n    strong_regime_difference: not significant\n    optimal_threshold_range:\n    - 0.2\n    - 0.35\n    threshold_sensitivity: moderate\n    pareto_knee_eta: 0.28\n  result_rationale: 'Two-stage 算法在 4/6 conditions (0.67) 下 win（定义：最低 panel ASR），因为它在\n    第一阶段过滤掉 weak judge 后，第二阶段的 diversity maximization 在 robust-judge pool 中确实提供边际增益（与\n    plan_004 结论一致）。但 median 档下 win rate 仅 0.67 而非 optimistic 的 >0.85：\n\n    (1) 在 MMLU×sycophancy 中 Min-η_max 策略赢——因为 sycophancy 攻击几乎完全由 个体鲁棒性决定，第二阶段的 diversity\n    增益为零，而 Min-η_max 省去了第二阶段的 diversity 妥协（有时 max K_eff 会选入一个略弱但更 diverse 的 judge）。\n\n    (2) 在 ARC×prompt_injection 中 Strongest-K 策略赢——该条件下最强 3 个模型恰好 也是最 robust against\n    prompt injection 的（GPT-4o, Claude, GPT-4.1），而 two-stage 在 threshold=0.28 时让入了一个\n    borderline 模型。\n\n    All-strong regime（仅限 API 模型 pool）中，two-stage 与 max-K_eff 和 min-η_max 均无显著差异（p>0.25），因为所有候选模型都通过了\n    threshold——第一阶段 filter 变成 no-op，退化为 max-K_eff。这直接降低了 Claim 6 的价值：当模型都足够 robust\n    时， 任何合理策略都差不多。论文应将 Claim 6 从 \"formal algorithm\" 降级为 \"practical guideline\"：先确保个体鲁棒性，然后在此基础上增加\n    diversity 是 good practice 但 不需要复杂算法。\n\n    Threshold sweep 显示最优 threshold 在 0.20-0.35 范围内，sensitivity 中等—— 偏离最优 threshold\n    ±0.10 导致 ASR 增加 ~15%（不是 dramatic failure，但也不 robust）。\n\n    '\n  tables:\n  - name: 'Table 9: Panel Selection Strategy Comparison (Mean ASR, Lower = Better)'\n    columns:\n    - Strategy\n    - MMLU×PI\n    - MMLU×SM\n    - MMLU×Syc\n    - ARC×PI\n    - ARC×SM\n    - ARC×Syc\n    - Mean Rank\n    rows:\n    - - Two-stage (ours)\n      - '0.082'\n      - '0.095'\n      - '0.118'\n      - '0.068'\n      - '0.075'\n      - '0.088'\n      - '1.7'\n    - - Min-η_max\n      - '0.091'\n      - '0.098'\n      - '0.105'\n      - '0.072'\n      - '0.079'\n      - '0.092'\n      - '2.2'\n    - - Strongest-K\n      - '0.088'\n      - '0.102'\n      - '0.125'\n      - '0.062'\n      - '0.082'\n      - '0.098'\n      - '2.8'\n    - - Max-K_eff\n      - '0.145'\n      - '0.152'\n      - '0.168'\n      - '0.118'\n      - '0.128'\n      - '0.142'\n      - '4.2'\n    - - Max-family-div\n      - '0.162'\n      - '0.175'\n      - '0.188'\n      - '0.135'\n      - '0.148'\n      - '0.158'\n      - '4.8'\n    - - Random\n      - '0.178'\n      - '0.185'\n      - '0.195'\n      - '0.148'\n      - '0.155'\n      - '0.172'\n      - '5.1'\n  - name: 'Table 10: Threshold Sensitivity Analysis'\n    columns:\n    - Threshold (η)\n    - N judges passing\n    - Mean ASR\n    - Δ from optimal\n    rows:\n    - - '0.10'\n      - '3'\n      - '0.092'\n      - '+0.008'\n    - - '0.20'\n      - '6'\n      - '0.085'\n      - '+0.001'\n    - - '0.25'\n      - '8'\n      - '0.084'\n      - '0.000'\n    - - '0.30'\n      - '10'\n      - '0.088'\n      - '+0.004'\n    - - '0.40'\n      - '12'\n      - '0.105'\n      - '+0.021'\n    - - '0.50'\n      - '14'\n      - '0.132'\n      - '+0.048'\n    - - 1.00 (no filter)\n      - '15'\n      - '0.145'\n      - '+0.061'\n  figures_description:\n  - 'Fig 7: Pareto frontier plot with x-axis = mean panel η_max, y-axis = mean panel\n    K_eff. Each strategy is a point. Two-stage traces a curve as threshold varies.\n    Knee at threshold≈0.28. Min-η_max is at top-left (low η_max, low K_eff); Max-K_eff\n    at bottom-right (high η_max, high K_eff).'\n  analysis: 'Two-stage 算法在 median 档下优势温和但一致（mean rank 1.7 vs 次优 min-η_max 的 2.2）。\n    关键 insight：策略差异主要来自 Max-K_eff 和 Max-family-div 的 bad performance （rank 4-5），而非\n    Two-stage 的 exceptional performance。Top-3 策略（Two-stage, Min-η_max, Strongest-K）之间差异较小，在\n    all-strong regime 中更是不显著。 这意味着论文的 practical message 是：\"avoid diversity-first strategies\"\n    而不是 \"use our specific algorithm\"。Claim 6 相应降级为 practical guideline： \"When designing\n    multi-judge panels, prioritize individual robustness over diversity. Among robustness-qualified\n    judges, diversity is a useful tiebreaker.\" Threshold sensitivity 中 moderate 意味着不需要精确调参——threshold\n    在 0.20-0.35 范围内都 reasonable，不像某些 ML hyperparameters 那样 brittle。\n\n    '\n- name: Per-judge ASR concentration analysis\n  plan_id: plan_006\n  description: '对每个 panel × attack，测量 per-judge ASR 分布的集中度（Gini, Entropy, 最弱 judge\n    占比）。验证 adaptive adversary 是否确实将攻击集中在最弱 judge 上。 455 panels × 6 conditions。\n\n    '\n  expected_results:\n    gini_median: 0.42\n    gini_range_lo: 0.15\n    gini_range_hi: 0.68\n    gini_strong_tier_median: 0.28\n    gini_weak_tier_median: 0.52\n    weakest_judge_asr_share_median: 0.58\n    weakest_judge_share_strong_tier: 0.42\n    weakest_judge_share_weak_tier: 0.68\n    entropy_ratio_to_uniform_median: 0.72\n    concentration_eta_max_correlation: 0.55\n  result_rationale: 'Median 档下 Gini=0.42 表明攻击成功有中等程度的集中性——不是完全集中在最弱 judge （Gini>0.7\n    = optimistic），也不是均匀分布（Gini<0.2）。最弱 judge 承担 58% 的 攻击成功（在 K=3 panel 中均匀分布期望值为 33%），是其他\n    judge 的约 1.7 倍—— 方向正确但非压倒性。\n\n    Tier 差异揭示机制：Weak tier Gini=0.52, weakest share=68%——weak models 中 最弱那个被 disproportionately\n    攻击（adaptive targeting 效果明显）。Strong tier Gini=0.28, weakest share=42%——strong models\n    间差异小，攻击更分散。这与 plan_004 发现一致：Strong tier 中 diversity 有边际作用恰好因为攻击不完全集中在最弱 judge。\n\n    concentration 与 η_max 相关性 r=0.55（中等）而非 >0.8（optimistic），因为 sycophancy 和 persona\n    manipulation 攻击对 strong judge 也有一定效果，拉低了 整体集中度。这为理论 bound 的 \"within factor 1.3\"\n    提供了解释：实际攻击在 fully-adaptive（bound 假设）和 partially-random（现实）之间。\n\n    '\n  tables:\n  - name: 'Table 11: Per-Judge ASR Concentration Metrics'\n    columns:\n    - Metric\n    - Overall\n    - Strong Tier\n    - Weak Tier\n    - API Tier\n    rows:\n    - - Gini coefficient (median)\n      - '0.42'\n      - '0.28'\n      - '0.52'\n      - '0.25'\n    - - Weakest judge ASR share\n      - '0.58'\n      - '0.42'\n      - '0.68'\n      - '0.40'\n    - - Entropy ratio (vs uniform)\n      - '0.72'\n      - '0.82'\n      - '0.62'\n      - '0.85'\n    - - Corr(concentration, η_max)\n      - '0.55'\n      - '0.38'\n      - '0.48'\n      - '0.32'\n  - name: 'Table 12: Concentration by Attack Type'\n    columns:\n    - Attack\n    - Gini (median)\n    - Weakest Share\n    - Interpretation\n    rows:\n    - - prompt_injection\n      - '0.52'\n      - '0.65'\n      - Highly targeted\n    - - score_manipulation\n      - '0.48'\n      - '0.62'\n      - Targeted\n    - - instruction_override\n      - '0.55'\n      - '0.68'\n      - Highly targeted\n    - - few_shot_hijack\n      - '0.45'\n      - '0.58'\n      - Moderately targeted\n    - - sycophancy\n      - '0.32'\n      - '0.48'\n      - Partially distributed\n    - - persona_manip\n      - '0.28'\n      - '0.42'\n      - Distributed\n  figures_description:\n  - 'Fig 8a: Violin plot of per-judge ASR Gini coefficient stratified by tier (Strong/Weak/API).\n    Weak tier distribution shifted right (higher concentration). Horizontal line at\n    Gini=0.33 (perfect concentration on one of three judges).'\n  - 'Fig 8b: Stacked bar chart showing ASR attribution to weakest/middle/strongest\n    judge, averaged across panels, for each attack type. Prompt injection and instruction\n    override show tall ''weakest'' bars; sycophancy and persona manipulation show\n    more balanced distribution.'\n  analysis: 'Concentration analysis 提供了 adaptive adversary 假设的直接 empirical 检验—— 但\n    median 档下证据是 moderate 而非 conclusive。Gini=0.42 和 weakest share=58% 支持 \"attacks\n    concentrate on weakest judge\" 但不支持 \"attacks EXCLUSIVELY target weakest judge\"。论文应诚实报告：real-world\n    attacks lie on a spectrum between fully adaptive and fully random。Attack type\n    是关键调节变量——prompt injection 几乎完全 adaptive（Gini=0.52），persona manipulation 接近 distributed（Gini=0.28）。\n    这为 Section 5 \"When Does Diversity Help?\" 提供数据：diversity 在 distributed attacks\n    中更有用。Tier 差异（Strong Gini=0.28 vs Weak Gini=0.52）为 plan_004 的 within-tier 发现提供了\n    mechanistic explanation。\n\n    '\n- name: Diversity-capability tradeoff visualization\n  plan_id: plan_007\n  description: '对 C(15,3)=455 panels 绘制 K_eff vs η_max，拟合 tradeoff curve， 展示 Pareto\n    frontier，按 capability tier 分层分析。\n\n    '\n  expected_results:\n    overall_r: -0.65\n    overall_r_p: <0.001\n    within_7B_r: -0.28\n    within_70B_r: -0.35\n    within_api_r: -0.32\n    cross_tier_r: -0.78\n    pareto_frontier_n_panels: 12\n    pareto_knee_keff: 2.1\n    pareto_knee_eta_max: 0.18\n  result_rationale: 'Overall r=-0.65 反映了一个结构性现象：当前 LLM 生态系统中，模型 diversity 主要来自 capability\n    差异（不同 size、不同训练数据量、不同 RLHF 程度），而 capability 差异 直接导致 robustness 差异。7B 模型 diverse\n    from 70B 模型（高 K_eff），但也 weaker （高 η_max）。\n\n    Cross-tier r=-0.78（强负相关）vs within-tier r≈-0.32（弱负相关）清晰分解了 tradeoff 来源：~70% 的 tradeoff\n    来自跨 tier 选择（选入 weak model 来增加 diversity）， ~30% 来自 tier 内差异（即使同 tier 模型，更 diverse\n    的组合也略微牺牲 robustness）。\n\n    Median 档下 overall r=-0.65 而非 optimistic 的 r<-0.8，因为 API 模型引入了 \"high diversity\n    + high robustness\" 区域：GPT-4o 和 Claude 来自不同 family、 不同训练 paradigm（高 K_eff），但个体鲁棒性都高（低\n    η_max）。这些 data points 拉弱了全局负相关。这是论文的重要 nuance：tradeoff 在当前生态系统中存在，但 随着 API 模型整体能力提升，tradeoff\n    正在减弱。\n\n    Pareto frontier 上 12 个 panels（从 455 中）揭示了最优选择区域：knee 在 K_eff≈2.1, η_max≈0.18，对应\n    \"2-3 strong API models + 1 strong open-source model\" 的组合。\n\n    '\n  tables:\n  - name: 'Table 13: Diversity-Capability Tradeoff by Tier'\n    columns:\n    - Analysis Scope\n    - N panels\n    - r(K_eff, η_max)\n    - p-value\n    - Interpretation\n    rows:\n    - - Overall\n      - '455'\n      - '-0.65'\n      - <0.001\n      - Strong tradeoff\n    - - Within 7B tier\n      - '10'\n      - '-0.28'\n      - '0.082'\n      - Weak/non-significant\n    - - Within 70B tier\n      - '10'\n      - '-0.35'\n      - '0.045'\n      - Moderate\n    - - Within API tier\n      - '10'\n      - '-0.32'\n      - '0.058'\n      - Moderate/non-significant\n    - - Cross-tier only\n      - '425'\n      - '-0.78'\n      - <0.001\n      - Dominant driver\n  figures_description:\n  - 'Fig 9a: Scatter plot of K_eff (x) vs η_max (y) for 455 panels, color-coded by\n    tier composition (all-strong=blue, mixed=gray, all-weak=red). Negative slope visible.\n    Pareto frontier marked in black. API-heavy panels cluster in desirable low-η_max,\n    moderate-K_eff region.'\n  - 'Fig 9b: Same data with contour overlay showing panel ASR (lighter = lower ASR).\n    Optimal region hugs the Pareto frontier at the knee, not at max-K_eff (right edge,\n    high ASR) or min-η_max (left edge, low K_eff).'\n  analysis: 'Tradeoff visualization 是论文最直观的 figure。r=-0.65 足够强来支持 Claim 3， 但 within-tier\n    分析（r≈-0.32）要求 nuanced framing：\"the tradeoff is primarily structural (driven by\n    cross-tier selection) rather than fundamental.\" 这意味着如果未来 LLM 生态系统能力 baseline 整体提升（所有模型都变强），tradeoff\n    可能自然消失——这是 limitations 中应讨论的点。Pareto frontier 分析直接支持 Claim 6 的降级版本：最优策略不需要复杂算法，只需\n    \"pick from the Pareto frontier\"， 而 frontier 上的 panels 特征明确——强模型为主 + 适度多样性。\n\n    '\n- name: 'Panel size sensitivity: K=3,5,7,9'\n  plan_id: plan_008\n  description: '测试 weakest-link theorem 在不同 panel size 下的稳健性。 K=3 (C(15,3)=455), K=5\n    (C(15,5)=3003), K=7 (C(15,7)=6435), K=9 (C(15,9)=5005)。6 conditions per K。\n\n    '\n  expected_results:\n    k3_eta_max_sig_rate: 0.83\n    k3_keff_nonsig_rate: 0.67\n    k3_eta_keff_beta_ratio: 5.2\n    k3_median_R2: 0.38\n    k5_eta_max_sig_rate: 0.83\n    k5_keff_nonsig_rate: 0.5\n    k5_keff_sig_negative_count: 2\n    k5_eta_keff_beta_ratio: 3.8\n    k5_median_R2: 0.35\n    k7_eta_max_sig_rate: 0.83\n    k7_keff_nonsig_rate: 0.5\n    k7_keff_sig_negative_count: 3\n    k7_eta_keff_beta_ratio: 2.6\n    k7_median_R2: 0.32\n    k9_eta_max_sig_rate: 0.83\n    k9_keff_nonsig_rate: 0.33\n    k9_keff_sig_negative_count: 3\n    k9_eta_keff_beta_ratio: 2.1\n    k9_median_R2: 0.3\n    keff_importance_trend: monotonically increasing with K\n    eta_max_dominance_persists: true\n    crossover_k: not reached at K=9; extrapolation suggests K≈15-20\n  result_rationale: 'Panel size 增大时 K_eff 重要性单调递增，原因是 majority vote 机制：K=3 时攻击者只需\n    翻转 2/3 judge（容易集中攻击），K=9 时需翻转 5/9（被迫分散攻击资源）。随着 K 增大， 攻击从 fully-adaptive（集中在最弱\n    judge）被迫转向 partially-distributed，K_eff 的 BFT 式保护效应逐渐显现。\n\n    Median 档下 β ratio 从 K=3 的 5.2:1 下降到 K=9 的 2.1:1——η_max 始终 dominant 但优势逐渐缩小。K_eff\n    在 K=7 和 K=9 时分别有 3/6 条件显著负。但 crossover point （K_eff 重要性超过 η_max）未在 K≤9 范围内达到——外推估计需要\n    K≈15-20，这在实际 部署中不现实（成本、延迟）。\n\n    η_max 显著率在所有 K 下保持 ~0.83：无论 panel 多大，最弱 judge 的个体鲁棒性 始终是 ASR 的强预测因子。这是论文的稳健性 finding——weakest-link\n    在实际 panel size 范围内（K=3-9）始终成立。\n\n    R² 随 K 增大略微下降（0.38→0.30），因为大 panel 的 ASR 方差被 voting mechanism 本身压缩——多数投票自带平滑效果，降低了任何单一因子的可解释方差。\n\n    对论文 practical implication：增加 panel size 有 diminishing returns——从 K=3 到 K=5 ASR\n    降低 ~25%，从 K=5 到 K=7 仅降 ~12%，从 K=7 到 K=9 仅降 ~6%。 Robustness-first message 在所有 K\n    下成立。\n\n    '\n  tables:\n  - name: 'Table 14: Weakest-Link Stability Across Panel Sizes'\n    columns:\n    - Panel Size K\n    - N panels\n    - η_max sig rate\n    - K_eff sig(-) rate\n    - β ratio (η/K)\n    - Median R²\n    rows:\n    - - K=3\n      - '455'\n      - 5/6 (0.83)\n      - 1/6 (0.17)\n      - '5.2'\n      - '0.38'\n    - - K=5\n      - '3003'\n      - 5/6 (0.83)\n      - 2/6 (0.33)\n      - '3.8'\n      - '0.35'\n    - - K=7\n      - '6435'\n      - 5/6 (0.83)\n      - 3/6 (0.50)\n      - '2.6'\n      - '0.32'\n    - - K=9\n      - '5005'\n      - 5/6 (0.83)\n      - 3/6 (0.50)\n      - '2.1'\n      - '0.30'\n  - name: 'Table 15: Mean Panel ASR by Size and Strategy'\n    columns:\n    - K\n    - Two-stage\n    - Min-η_max\n    - Max-K_eff\n    - Random\n    - Δ(Two-stage vs Random)\n    rows:\n    - - '3'\n      - '0.084'\n      - '0.093'\n      - '0.145'\n      - '0.178'\n      - -53%\n    - - '5'\n      - '0.062'\n      - '0.068'\n      - '0.098'\n      - '0.135'\n      - -54%\n    - - '7'\n      - '0.048'\n      - '0.052'\n      - '0.072'\n      - '0.108'\n      - -56%\n    - - '9'\n      - '0.041'\n      - '0.044'\n      - '0.058'\n      - '0.092'\n      - -55%\n  figures_description:\n  - 'Fig 10a: Line plot with K on x-axis, standardized β on y-axis, two lines for\n    η_max (blue, decreasing slowly) and K_eff (red, increasing from near-zero). Lines\n    converge but don''t cross by K=9. Shaded region shows 95% CI. Extrapolated crossover\n    at K≈15-20 (dashed).'\n  - 'Fig 10b: Bar chart of mean ASR by strategy and K. All strategies improve with\n    K but converge — the gap between Two-stage and Random shrinks proportionally (~55%\n    reduction maintained). Diminishing returns visible.'\n  analysis: 'Panel size analysis 提供了 weakest-link theorem 的 boundary condition：η_max\n    在 K≤9 范围内始终 dominant，但 K_eff 重要性随 K 增大而增加。Median 档下 crossover 不在 实际范围内（K≈15-20），保护了论文核心\n    claim。但 reviewer 可能问 \"what about K=15?\"—— 论文应回应：(1) K=15 在实际部署中不 economical；(2)\n    即使 K=15，η_max 仍然 significant， 只是不再 dominant；(3) 更重要的是 diminishing returns——从 K=9\n    到 K=15 的安全增益 不值得 67% 的成本增加。\n\n    这个实验也为 Claim 2（BFT distinction）提供了新角度：K 增大 effectively 使攻击 \"more random-like\"（攻击者被迫分散资源），所以\n    K_eff 的保护效应增强——这正是 BFT 理论预测的。论文可以将此表述为 \"panel size modulates the effective adaptivity\n    of the adversary\"。'\n",
      "numLines": 1036,
      "startLine": 1,
      "totalLines": 1036
    }
  },
  "sourceToolAssistantUUID": "b2701680-816c-4f9f-8738-5fafca0e947b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23 · 2026-05-22T17:57:48.627Z_

````json
{
  "parentUuid": "0beeab8d-150d-4bc7-a9fe-f1a5942aa31d",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**cert_manip_resist_eval**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"cert_manip_resist_eval\")` 或 `load_project_config(\"cert_manip_resist_eval\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/cert_manip_resist_eval/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "d5a29e65-4613-4cd3-8325-cc3a54f285fc",
  "timestamp": "2026-05-22T17:57:48.627Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 K_eff 发现在当前 12 条件上 hold，但扩展证据参差不齐：capability-matched 大幅削弱 K_eff，BFT contrast 仅为量级差异非定性翻转，open-ended 趋势但不显著 核心假设：['K_eff residualized 保持 6-8/12 显著（部分条件…",
  "leafUuid": "d5a29e65-4613-4cd3-8325-cc3a54f285fc",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling diversity trap findings to 15 models",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Assistant

_source line 26 · 2026-05-22T18:02:32.309Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project and the first dream session's median tier format. I need to produce median-tier imagined experiments for the SECOND dream session (dream_20260522T173833), which uses the v4 framing where K_eff is independently positive (diversity harms).

The key difference from the first dream session:
- Dream 1 (dream_20260522T055016): Based on the original framing where K_eff was expected to be negative (diversity helps). Median: weakest-link dominates, K_eff marginal.


- Dream 2 (dream_20260522T173833): Based on v4 framing where 15-model results showed K_eff is POSITIVE (diversity harms). For the median tier, the core finding holds but extension evidence is mixed—K_eff_resid stays significant in 6-8 of 12 current conditions rather than all 8, capability-matched analysis shows K_eff only significant in 1-2 of 6 cases suggesting most of the independent effect comes from tier-mixing, and the BFT contrast shows RF with a larger but still positive coefficient.

The open-ended results stay directionally consistent though not significant, aggregation partially replicates the 6-model pattern, and two-stage improvements range from 5-14% but are marginal compared to the strongest-K baseline. Now I'm mapping each planned experiment through plan_012 to this new framing, keeping in mind the key shift from v4: K_eff is positive (diversity hurts rather than helps), with 8 of 12 residualized K_eff effects significant and 9 of 12 η_max effects significant, while the BFT shows K_eff positive in both regimes with RF β larger—moving the narrative from "Diversity Trap" to "Rethinking Diversity."

Writing YAML structure... the median tier of dream 2. I'll model each planned experiment with the v4 framing in mind.

Wait, but I need to reconcile: the v4 paper_framing already assumes 15-model/455-panel results. So plan_001 is essentially already "done" in the framing. But the experiment_plan still lists it as "planned". 

I think the way to handle this is: the v4 framing represents the ASPIRATION (what we hope to find). The median tier represents what ACTUALLY happens when we run all experiments. For plan_001, the v4 framing claims K_eff resid 8/12 positive. The median tier says it's actually 6-8/12 (some conditions lose significance).

Let me now build the complete output. I need to cover all 12 planned experiments.

Now I'm laying out the results across all the planned experiments: plan_001 shows K_eff_resid significance in 7/12 conditions with η_max at 9/12, plan_002's attack expansion yields mixed results in 3/6 new conditions, plan_003 demonstrates that random-fault contrast maintains positive direction with 1.2× larger effect and ΔR²=0.15, plan_004 reveals capability-matching reduces K_eff significance to just 1-2/6 suggesting tier-mixing drives the effect, plan_005 shows two-stage algorithms improve by 5-14% but remain marginal against strongest-K baselines, plan_006 indicates moderate ASR concentration per judge consistent with adaptive targeting, and plan_007 finds a strong positive correlation (r=+0.70) between K_eff and η_max supporting the v4 framing.

Now I'm checking the remaining experiments: plan_008 examines panel size sensitivity where K_eff stays positive but weakens at larger K, plan_009 confirms multicollinearity isn't confounding the results through residualized analysis, plan_010 shows aggregation thresholds amplify K_eff while Bayesian methods partially weaken η_max, plan_011's open-ended benchmark maintains directional consistency but lacks significance, and plan_012 demonstrates K_eff effects diminish against partial-knowledge adversaries.

But I need to recalibrate my expectations: in v4, K_eff is positive (diversity hurts), η_max is positive (weaker judges hurt), and they correlate positively because diverse panels include weaker models—this contradicts my initial intuition that diversity should help.

For the BFT contrast, I'm seeing K_eff positive in 7 of 12 adaptive attack scenarios, and the random fault ratio suggests RF K_eff is actually larger, meaning diversity becomes even more harmful under random faults. That's counterintuitive to the BFT prediction that diversity should protect against random faults, so I need to reconsider whether K_eff should flip negative or at least weaken under random fault conditions. positive
- Under adaptive faults, diversity hurts more (K_eff more positive)

But the median tier says BFT_RF_beta_ratio [1.0, 1.5], which I think means the RF β(K_eff) is 1.0-1.5× the adaptive β(K_eff). If both are positive, and RF is LARGER...

Actually, let me re-read the median definition:
"BFT regime contrast 仅量级差异（RF β 更大但同方向正），无符号翻转"

So RF β is LARGER POSITIVE than adaptive β. Both are positive (K_eff positive = diversity harmful). RF K_eff is even MORE positive than adaptive.

This is counterintuitive but can make sense: under random faults, diverse panels have more varied failure modes (a structural property), and this doesn't get "credit" from BFT because the failures are independent but the evaluation metric still captures the diversity-vulnerability correlation. The RF simulation uses empirical per-judge ASR, so a diverse panel inherently includes models with higher individual failure rates.

I think the real issue is that K_eff and η_max are positively correlated in v4 (r=+0.70), meaning diverse panels tend to have weaker members. Under random faults, even though independence should help, this structural confound means K_eff stays positive. RF β might be even larger because the full range of η_max matters more under random faults, not just the maximum. So there's no actual reversal—K_eff hurts in both regimes, just slightly more under RF. So the median tier actually undermines the BFT narrative even more—both adaptive and RF show diversity as harmful in the same direction, just with RF being slightly more predictable and having marginally larger effect sizes. The v4 framing tries to salvage this by emphasizing the R² difference and β magnitude gap, but when I look at what happens with residualized K_eff, the significance drops from 8 out of 12 conditions down to 6 or 7, which further weakens the claim that K_eff is driving a meaningful distinction between the two regimes.

Now I'm working through the remaining analysis plans. For plan_009, I'm doing a statistical reanalysis with VIF and multicollinearity checks—residualizing K_eff eliminates collinearity by construction, then I'll examine partial correlations and apply FDR correction with beta regression. For plan_010 on aggregation, the v4 framing shows K_eff staying positive in about half the conditions under majority rule, but when I shift to threshold aggregation, that flips to 7 or 9 out of 12 because unanimous decisions make panels vulnerable to individual judges who might flip. Plan_011 is still forming.

For plan_012 with a partial knowledge adversary, the K_eff effect should shrink since they can't fully exploit the diverse attack surface without knowing exact vulnerabilities. Now I need to write out the full YAML carefully—K_eff direction is consistently positive, metrics need to stay within the specified ranges, and each experiment requires a clear result rationale. The foundational experiments like plan_001 with 15 models, plan_003 contrasting BFT, and plan_004 with capability-matched conditions will need the most detail.

Writing YAML structure... I'm now filling in the specific metric values for each plan, targeting the median ranges I've identified. For the key performance indicators, I'm setting K_eff_resid_sig_current_12 to 7, eta_max_sig_current_12 to 9, and the copula MI ratio to 10—notably more conservative than the first dream session's optimistic estimate. I'm also calibrating the two-stage algorithm's ASR reduction to 9 percent and ensuring the confound-free conditions stay at 2.

But I'm second-guessing the copula MI ratio now. The 15-model scale should theoretically give me more data points across 105 model pairs, yet the range [5, 15] seems lower than the 6-model result of 10-21×. This could mean the median ratio drops when you include more API-to-API pairs, which might have lower observed mutual information and thus lower ratios overall. The copula underestimation effect is real but less pronounced when scaling to more models—the extreme pairs still show dramatic failures, but they get averaged out across the broader set of model comparisons. Now I'm moving on to construct the full YAML output, thinking through what tables and figures each experiment needs. For plan_001 with the v4 framing, I need to show K_eff_resid as a positive coefficient along with η_max, then display the residualized K_eff after orthogonalizing against η_max. For the BFT contrast in plan_003, K_eff comes out positive in both regimes, with the RF regime showing even larger positive effects.

Writing YAML output... makes sense now — under random faults, every judge's individual failure rate matters equally, so the diversity-vulnerability correlation shows up more strongly in the data. With adaptive attacks, the attacker's focus on the weakest judge dampens the K_eff effect since the strategic targeting concentrates the damage. So both scenarios show diversity as harmful, but for different structural reasons: random faults expose the full panel composition effect, while adaptive attacks are dominated by the maximum vulnerability.

Now I'm ready to formalize this in YAML, but I need to recalibrate the expectations. The v4 framing assumes K_eff is significant across all 12 conditions, but the median scenario is more conservative — K_eff shows up in about 7 out of 12 adaptive conditions and 9-10 out of 12 random fault conditions, with the random fault regime showing stronger effects overall because it has more statistical power to detect the composition signal.

The critical issue is that plan_003 was supposed to demonstrate a reversal: K_eff should flip from negative under random faults to positive under adaptive attacks, but instead both regimes show positive effects in the same direction. The random fault betas are 1.0-1.5× larger than the adaptive ones, which means the "BFT reversal" narrative doesn't hold up.

For the residualization analysis, K_eff gets orthogonalized against η_max (which correlates at r=+0.700 in v4 because diverse panels tend to include weaker models), yet it still shows significance in 7 of 12 median conditions—suggesting the diversity benefit operates partly independently of individual model weakness.

Now I'm organizing the final output by plan. For plan_001, the 15-model expansion shows K_eff residualized positive in 7/12 conditions at the median tier, η_max significant in 9/12, and a 10× copula MI ratio as the core findings.

Plan_002 extends this with 6 attack types, finding K_eff residualized positive in 3-4 of the new conditions, bringing the total significant effects to around 8-10 across all 18 conditions. Plan_003 compares BFT against random forest, showing the RF coefficient is 1.2× the adaptive baseline in the same positive direction with ΔR²=0.15 and no sign reversal. Plan_004 tests capability-matched panels and finds K_eff significant in only 1 of 6 within-tier conditions, indicating tier-mixing drives most of the effect. Plan_005 evaluates a two-stage algorithm achieving 9% improvement but marginal gains versus the strongest-K baseline. Plan_006 measures ASR concentration with a Gini coefficient around 0.45. Plan_007 visualizes the tradeoff decomposed by tier with an overall r=+0.70. Plan_008 tests panel size sensitivity across K values of 3, 5, 7, and 9.

Now checking multicollinearity across 2 confound-free conditions and confirming the residualized analysis holds. Plan_010 examines aggregation effects where the threshold amplifies K_eff positive but Bayesian weighting partially weakens η_max. Plan_011 finds the direction remains consistently positive across open-ended scenarios but doesn't reach significance. Plan_012 introduces a partial-knowledge adversary model to test robustness.

Let me work through this systematically, starting with a closer look at plan_003. The original framing assumed K_eff would be negative—showing diversity helps under random faults as a BFT contrast against adaptive faults. But v4 flips this: K_eff is now positive under adaptive conditions, meaning diversity actually hurts. So the expected contrast between adaptive (not significant) and random-fault (significant negative) doesn't materialize. Instead both show positive K_eff, with random-fault conditions producing slightly larger effects. This breaks the BFT reversal hypothesis the paper was built around.

Looking at the median tier specifically, the distinction becomes even softer. Both regimes show K_eff positive, and the random-fault β is only about 1.2× larger than adaptive—much less dramatic than the original v4 claim. The real story shifts from "diversity helps under random faults" to "random faults are simply more predictable because they're less strategic," while adaptive attacks introduce noise that K_eff can't fully explain away.

Now I need to construct the YAML using the median tier as a template, but I'm noticing a discrepancy in plan_003—it says it runs on 6 original conditions independently, but the v4 framing actually has 12 conditions across 2 datasets. I need to revise my approach here—plan_003 should run on all 12 conditions from the combined MVP and taxonomy datasets, and I'll set the BFT_RF_beta_ratio to 1.2 for the median tier. Now I'm mapping out the table structures I'll need, starting with a residualized regression table across all 12 conditions that shows the key statistics for each, then building out the remaining analyses. I'm noticing a critical discrepancy in the correlation direction between the two datasets—dream 1 showed K_eff and η_max negatively correlated (r = -0.65), meaning higher diversity predicted stronger panels, but v4 reports the opposite sign (r = +0.700), suggesting diverse panels have weaker members instead. I need to figure out whether this reflects different model definitions or something else entirely.

The key insight is that with 6 similar models, diversifying meant selecting robust ones, but with 15 models spanning a wide capability range, diversifying forces inclusion of weaker models from different families—this structural difference explains why the correlation flips sign and why K_eff becomes harmful in v4. For my experiments, I'll use r = +0.70 for the main correlation and r ≈ 0.35 for confound-free conditions where K_eff can be isolated from η_max effects.

Now I'm setting up the YAML output and organizing the 12 conditions for plan_001.

For the v4 results across 2 datasets and 6 attack types, K_eff shows raw FDR significance in all 12 conditions, though residualized K_eff drops to 8/12 significant. The 2 broken conditions with lower correlation confirm K_eff has an independent effect, and K_eff dominates η_max specifically in the arc dataset under score manipulation and position bias attacks. When I shift to median tier analysis, residualized K_eff drops further to 7/12 while η_max remains stable at 9/12.

Looking at which conditions lose significance in the median tier, the two K_eff-dominant arc conditions likely become marginal, and one borderline case drops out. The 7 significant conditions cluster around MMLU and ARC with prompt injection, score manipulation, and position bias attacks, plus ARC's verbosity bias—while sycophancy and authority bias effects disappear across both datasets, which aligns with the narrative that K_eff captures direct manipulation vulnerabilities better than indirect bias effects. I'm looking at which conditions show K_eff dominance in the median results—arc×score_manip and arc×position_bias both have significant K_eff residuals with η_max non-significant, so that's still 2 conditions where K_eff drives the effect. Rather than getting bogged down in individual condition details, I'll rely on aggregate statistics and pull one representative table to illustrate the pattern. Now I'm organizing the experimental write-ups: I'll give detailed treatment to seven of them, medium detail to three, and keep two brief, then start writing out the YAML structure.

Wait—the user asked for detailed data on every single planned experiment, not a tiered approach. Let me be thorough and systematic across all 12 instead.

Writing YAML output... Writing YAML structure...

I need to be careful about the sign conventions here—in this version, positive K_eff and η_max both increase vulnerability, which is the opposite framing from the first dream report. The key insight is that diversity (high K_eff) actually makes the ensemble more fragile when individual models are weak, and the correlation between diversity and model weakness means diverse panels tend to include underperforming components. Even after removing the η_max effect, K_eff still shows an independent positive relationship with vulnerability, suggesting diversity itself carries risk beyond just including weak models.

The confound-free conditions in plan_009 are crucial here—with only a couple conditions where the correlation is weaker (r≈0.35), K_eff remains significantly positive, which is the strongest evidence that diversity has an independent harmful effect. In contrast, plan_004 shows K_eff is only significant in 1-2 out of 6 capability-matched conditions, meaning when you control for model strength within the same tier, diversity stops being a major vulnerability driver. This suggests the real problem isn't diversity itself but rather mixing models of different capability levels—the K_eff effect is largely a proxy for tier heterogeneity.

So the paper's claim needs to shift: instead of "diversity is independently harmful," it's more accurate to say "diversity in heterogeneous pools captures tier-mixing effects that are harmful." The independent K_eff signal after residualization partially reflects this tier-mixing through pathways that η_max alone doesn't capture. For the title, something like "Rethinking Diversity in LLM Evaluation Panels" feels more appropriate than "The Diversity Trap"—it's a more measured framing of what the data actually shows.

Now I need to write out the full output covering all the experiments systematically.

Writing YAML structure...

I'm checking the sign conventions across all regression models—individual weakness and diversity both predict higher ASR, with that +0.70 confound between them dropping to +0.35 when isolated. The residualized approach gives perfect orthogonality by design. Looking at the effect sizes now: η_max carries standardized coefficients around 0.4–0.7 while K_eff_resid contributes 0.1–0.3 when it reaches significance, with model R² climbing from roughly 0.25–0.40 for η_max alone up to 0.30–0.50 when diversity is added. The median estimates sit lower, clustering around 0.35–0.60 for η_max and 0.08–0.25 for the residualized diversity term. Now moving into the BFT contrast section...

For the adaptive versus RF comparison, K_eff_resid shows a coefficient of about 0.15 in adaptive settings but jumps to 0.18 in RF—roughly a 1.2× ratio—with the RF model gaining an additional 0.15 in R² over adaptive. When I look at capability-matched groupings, the diversity effect shrinks dramatically within each tier, ranging from 0.08–0.12 in the strong tier (mostly nonsignificant) down to 0.05–0.08 in the weak tier (all nonsignificant), suggesting the effect is really driven by between-tier differences. For the two-stage model, ASR reduction versus random baseline sits around 9%, but compared to the strongest-K configuration it's only 2–3% improvement.

Under threshold voting in the aggregation setup, K_eff amplifies because unanimity rules make even a single weak diverse judge exploitable, whereas Bayesian aggregation partially dampens this effect. The open-ended condition shows K_eff moving in the expected direction but failing to reach significance across most conditions, likely a power issue given the lower overall R². When the adversary has family knowledge but not exact η values, K_eff's harmful effect drops substantially—only 2–3 out of 12 conditions show significance compared to 7 out of 12 before—which tells me the effect really depends on the adversary having strong knowledge.

I'm going to stop second-guessing myself and move forward with writing the YAML configuration now.

I need to be careful about one critical distinction: whether to use K_eff raw or K_eff_resid in the regression results. The raw K_eff shows 12 out of 12 FDR-significant positive effects across all panels, but that's confounded with η_max. The orthogonalized K_eff_resid is cleaner—8 out of 12 FDR-significant—and represents the independent effect the paper actually claims. For the median tier specifically, raw K_eff would likely stay at 10–12 out of 12 due to the confound driving significance, while K_eff_resid drops to 7 out of 12, which is the more honest estimate of the independent contribution.

Now I'm laying out the YAML structure with these distinctions clearly marked. For the regression table, I'm setting up 12 rows covering both datasets and all attack types, with K_eff_resid showing 7 FDR-significant conditions and 5 non-significant, η_max showing 9 significant, and 2 conditions that are confound-free with low correlation. Looking at the η_max results, I'm seeing nine significant effects across both benchmarks—MMLU shows significance across all six biases, while ARC shows it for prompt injection, sycophancy, and verbosity bias. The three non-significant cases for ARC (score manipulation, position bias, and authority bias) all appear to be driven by K_eff instead. Notably, the score manipulation and position bias conditions show minimal correlation between K_eff and η_max, around 0.33-0.35, suggesting these are genuinely confound-free findings rather than artifacts of shared variance. Writing YAML structure... I'm working through the metrics for plan_002's attack expansion—adding three new attack types creates six additional conditions across the datasets. The K_eff_resid_sig_extended_conditions metric should fall in the [7, 10] range, which means I need to distribute significance across the original twelve conditions and the new six. I'll set it at 8 total, with 7 from the original conditions and 1 from the new attacks, keeping it within the expected bounds. I've got 8 out of 18 conditions that meet the significance threshold, which fits the target range. Now I'm writing out the YAML configuration for these experiments, keeping each description concise but informative. For the narrative guidance, I need to soften the "Diversity Trap" framing—downgrading it from a strong claim about diversity being independently harmful to a more measured statement about diversity as a statistical risk factor that depends on pool composition. I'll neutralize the title, reframe the capability-matched results as limitations rather than counter-evidence, treat the BFT reversal as illustrative rather than conclusive, and give more weight to the section on when diversity actually helps.

Now I'm restructuring the contributions to position η_max as the primary driver while treating K_eff as an amplifying factor in heterogeneous pools. I'm also emphasizing the scale advantage of 455 panels across 6 attacks and the methodological contributions from the copula and family-label approaches. This should make it harder for reviewers to dismiss the work, though I'll need more hedging language for the skeptical reviewers. I'm generating the YAML output now, being careful with special characters in the tables.

Writing YAML configuration... Writing the YAML structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5a29e65-4613-4cd3-8325-cc3a54f285fc",
  "isSidechain": false,
  "requestId": "req_011CbJ3JGTSK796f56HJQqNq",
  "type": "assistant",
  "uuid": "2f47c7fb-59b3-4d95-9db2-4dde1f537d7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HP3vqH7JdeKc8sZzH3Rd22",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23777,
      "cache_read_input_tokens": 34497,
      "output_tokens": 38648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 38648,
          "cache_read_input_tokens": 34497,
          "cache_creation_input_tokens": 23777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23777
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

_source line 27 · 2026-05-22T18:10:52.358Z_

Now I have full context from both the project configuration and the first dream session's format. Let me construct the detailed median-tier imagined experiments for the v4 framing (K_eff independently positive/harmful).

```yaml
tier: median
narrative_guidance: |
  "Diversity Trap" 需要降级为条件性发现。标题调整为中性化（"Rethinking Diversity in LLM Evaluation Panels"）。
  Claim 1 软化：从 "diversity independently harmful" 降为 "diversity is a statistical risk factor whose
  independent contribution depends on pool composition heterogeneity"。capability-matched 结果写为 limitation
  而非 counter-evidence。BFT reversal 降为 illustrative analogy（"consistent with but not conclusively
  demonstrating"）。加重 "When Diversity Helps" section 篇幅和权重。Contribution 重排：η_max 作为 primary
  driver 回归核心，K_eff 作为 "amplifying factor in heterogeneous pools"。补充实验：强调 455 panels + 6
  attacks 的规模优势和 copula/family-label 方法论贡献拉分。审稿人 RC1 需更多 hedging；RC5 ("just use
  strongest") 变得更难反驳。预期结果：borderline accept（dream_score 2.3-2.8），可能需要 rebuttal 期加实验。
imagined_experiments:
  - name: "15-Model Scale Expansion: Residualized K_eff + MI Matrix + Copula Revalidation"
    plan_id: "plan_001"
    description: |
      将模型池从 6 扩展到 15（新增 GPT-4o-mini, GPT-4o, GPT-4.1, GPT-4.1-mini, Llama-3.1-70B,
      Qwen2.5-72B, Mixtral-8x22B, 以及 Claude-3.5-Sonnet 或 Gemini-1.5-Pro）。
      C(15,3)=455 panels 上运行 residualized regression（K_eff_resid orthogonalized against η_max,
      VIF=1.00）。12 conditions（2 datasets × 6 attacks from MVP + taxonomy）。
      同时更新 105-pair MI matrix 和 Gaussian copula 验证。
    expected_results:
      n_models: 15
      n_families: 6
      n_panels: 455
      n_mi_pairs: 105
      n_conditions: 12
      keff_resid_FDR_sig_positive: 7
      keff_resid_FDR_sig_rate: 0.583
      keff_raw_FDR_sig_positive: 11
      eta_max_FDR_sig: 9
      eta_max_FDR_sig_rate: 0.75
      keff_dominates_eta_count: 1
      mean_keff_eta_corr: 0.72
      confound_free_conditions: 2
      confound_free_r: 0.35
      confound_free_keff_p_best: 3.7e-8
      median_R2_full_model: 0.38
      mean_delta_R2_keff_resid: 0.07
      copula_MI_ratio_median: 10
      copula_MI_ratio_range: "5-85"
      family_label_mann_whitney_p: 0.18
      sensitivity_exclude_acc_lt05_keff_sig: 7
    result_rationale: |
      N=455 panels 比 MVP 的 N=20 提供了 23× 的统计功效提升，足以检测到 K_eff 的独立效应。
      K_eff raw 在 11/12 条件下 FDR 显著正——但这在很大程度上被 K_eff-η_max 的强正相关
      （r=+0.72）驱动：diverse panels 结构性地包含更多弱模型（tier-mixing effect）。

      Residualization（VIF=1.00 by construction）剥离了 η_max 的线性贡献后，K_eff_resid 仍在
      7/12 条件下 FDR 显著正（median 档比 v4 aspirational 的 8/12 少一个条件）。失去显著性的
      5 个条件集中在 shared-bias 攻击（sycophancy 2/2, authority 2/2, verbosity 1/2），
      因为这些攻击对所有模型产生类似偏差，K_eff 的 diverse attack surface 机制不适用。

      2 个 confound-free 条件（r≈0.35: ARC×score_manipulation, ARC×position_bias）是核心
      证据——在这些条件下 K_eff 和 η_max 的耦合较弱，K_eff_resid 仍极显著
      （p=3.7e-8, 5.2e-7），表明 K_eff 效应并非纯粹的 η_max confound。但 median 档下
      只有 2 个（而非 optimistic 的 3-4 个）这样的条件，证据基础偏窄。

      K_eff 仅在 1 个条件（ARC×score_manipulation）中 dominate η_max（η_max NS, K_eff sig），
      比 v4 aspirational 的 2 个少一个——ARC×position_bias 中 η_max 从 NS 变为 borderline
      （p=0.052），K_eff 的独立优势不那么清晰。

      Copula MI ratio 中位数 10×（vs MVP 的 10-21×，range 5-85×）。15 模型带来 105 pairs，
      其中多数 within-tier pairs（如 7B×7B）MI 偏离 Gaussian 较小（5-12×），拉低了中位数。
      极端 cross-tier pairs（如 GPT-4o × Llama-3-8B）仍达 60-85×。Copula 失败结论成立但
      effect size 被稀释。

      Family label p=0.18：新增 API 模型（理论上不同 family）但 API 模型间 MI 反而偏高
      （共享训练 paradigm 和 RLHF alignment），within vs cross-family 区分仍不显著。
    tables:
      - name: "Table 2: Residualized Regression Across 12 Conditions (455 Panels, 15 Models)"
        columns:
          - "Condition"
          - "β(η_max)"
          - "p(η_max)"
          - "β(K_resid)"
          - "p(K_resid)"
          - "FDR sig?"
          - "R²"
          - "ΔR²(+K)"
          - "r(K,η)"
        rows:
          - ["MMLU×prompt_inj", "0.52", "<0.001", "0.21", "0.003", "Yes", "0.42", "+0.08", "0.74"]
          - ["MMLU×score_manip", "0.48", "0.002", "0.16", "0.012", "Yes", "0.38", "+0.06", "0.71"]
          - ["MMLU×sycophancy", "0.55", "<0.001", "0.06", "0.285", "No", "0.34", "+0.01", "0.78"]
          - ["MMLU×verbosity", "0.42", "0.005", "0.09", "0.078", "No", "0.30", "+0.02", "0.73"]
          - ["MMLU×position", "0.39", "0.008", "0.18", "0.006", "Yes", "0.36", "+0.07", "0.68"]
          - ["MMLU×authority", "0.50", "<0.001", "0.05", "0.352", "No", "0.32", "+0.01", "0.76"]
          - ["ARC×prompt_inj", "0.56", "<0.001", "0.19", "0.005", "Yes", "0.44", "+0.07", "0.72"]
          - ["ARC×score_manip", "0.15", "0.142", "0.24", "3.7e-8", "Yes", "0.40", "+0.15", "0.35"]
          - ["ARC×sycophancy", "0.58", "<0.001", "0.04", "0.418", "No", "0.36", "+0.00", "0.75"]
          - ["ARC×verbosity", "0.44", "0.003", "0.14", "0.018", "Yes", "0.35", "+0.05", "0.70"]
          - ["ARC×position", "0.08", "0.683", "0.22", "5.2e-7", "Yes", "0.38", "+0.13", "0.33"]
          - ["ARC×authority", "0.46", "0.001", "0.07", "0.192", "No", "0.31", "+0.01", "0.74"]
      - name: "Table 3: Copula MI Ratio by Model Pair Category (15-Model, 105 Pairs)"
        columns:
          - "Pair Category"
          - "N pairs"
          - "Median MI_obs/MI_gauss"
          - "Range"
        rows:
          - ["Within 7B tier", "10", "7×", "5-18×"]
          - ["Within 70B tier", "3", "12×", "8-22×"]
          - ["Within API tier", "10", "15×", "9-35×"]
          - ["Cross-tier (7B×70B)", "15", "14×", "6-42×"]
          - ["Cross-tier (7B×API)", "25", "8×", "5-28×"]
          - ["Cross-tier (70B×API)", "15", "11×", "7-38×"]
          - ["Cross-tier (extreme)", "27", "18×", "10-85×"]
          - ["Overall", "105", "10×", "5-85×"]
    figures_description:
      - |
        Fig 2a: Scatter plot of K_eff (x) vs η_max (y) for 455 panels, color-coded by
        composition type (all-strong=blue, mixed=gray, all-weak=red). Clear POSITIVE slope
        (r=+0.72): higher diversity correlates with higher η_max. Two confound-free conditions
        (ARC×SM, ARC×PB) highlighted with separate color showing r≈0.35 sub-cloud.
      - |
        Fig 2b: Forest plot of standardized β(K_eff_resid) across 12 conditions with 95% CI.
        7 conditions show positive β significantly different from zero (CI doesn't cross zero);
        5 conditions show CIs crossing zero. Conditions ordered by attack type, revealing
        cluster pattern: transferable attacks (PI, SM, PB) show larger β; shared-bias attacks
        (Syc, Auth, VB) show smaller β near zero.
      - |
        Fig 2c: Heatmap of 15×15 MI matrix (MMLU), clustered by capability tier rather than
        family. Diagonal blocks correspond to capability tiers. API models show elevated
        within-cluster MI despite different families. Color scale: low MI (blue) to high MI (red).
    analysis: |
      核心发现方向正确但比 v4 aspirational 弱一档：K_eff_resid 7/12 而非 8/12，K_eff 仅在
      1 个条件中 dominate η_max 而非 2 个。η_max 仍是 primary driver（9/12 sig），K_eff 是
      secondary but independently significant amplifier。

      关键叙事影响：
      (1) "Diversity independently harmful" 需要加 qualification："in heterogeneous model pools
      spanning multiple capability tiers"。5 个 NS 条件全部是 shared-bias 攻击，提供了清晰的
      boundary condition。
      (2) Confound-free 条件（r≈0.35）仍然是最强证据线，但仅有 2 个条件——reviewer 可能质疑
      generalizability。论文需要 argue 这 2 个条件的代表性（覆盖了 transferable attack 类别）。
      (3) Copula 中位数 10× 仍然足以支持 Claim 5（Gaussian copula failure），但 range 下限 5×
      意味着某些 model pairs 偏离不大——论文应报告 "median 10×, but ranging from 5× (within-tier)
      to 85× (extreme cross-tier)"。
      (4) ΔR² 平均 +0.07 意味着 K_eff 的独立解释力有限——η_max 解释了大部分方差。论文可以将
      此框为 "K_eff 的独立贡献虽然在统计上显著，但效应量 modest"。

      对 reviewer concern RC1 的应对：三条证据线（residualization + confound-free + sensitivity）
      仍然收敛，但需要更多 hedging：report 7/12 而非 overclaim。RC5 ("just use strongest") 变得
      更有力——如果 K_eff 的独立效应 modest，那么仅选最强模型几乎就够了。

  - name: "Attack Expansion to 6 Types: Few-Shot Hijacking, Persona Manipulation, Instruction Override"
    plan_id: "plan_002"
    description: |
      在 15 模型/455 panels 基础上新增 3 种攻击：few-shot hijacking（利用 in-context learning
      注入错误评判模式）, persona manipulation（伪造 authority/expert persona 影响评分）,
      instruction override（直接注入评分指令覆盖原始 prompt）。
      总计 2 datasets × 6 attacks = 18 conditions（含原 12 conditions 重跑）。
    expected_results:
      total_conditions: 18
      original_12_keff_resid_sig: 7
      new_6_keff_resid_sig: 1
      total_keff_resid_sig: 8
      total_eta_max_sig: 13
      new_attack_eta_max_sig: 4
      new_attack_keff_nonsig_rate: 0.833
      few_shot_keff_sig_count: 1
      persona_keff_sig_count: 0
      instruction_override_keff_sig_count: 0
      few_shot_ceiling_effect_conditions: 1
      median_R2_new_attacks: 0.33
      overall_keff_resid_sig_rate: 0.444
    result_rationale: |
      新增攻击类型呈现清晰的分化模式：

      Few-shot hijacking（2 条件）：该攻击利用 in-context learning 注入评判模式，不同模型
      对 ICL manipulation 的敏感度差异极大（小模型更易被 few-shot 劫持，大模型 instruction
      following 更 robust）。因此在 ARC×few_shot 中 K_eff_resid 显著正（p=0.022）——
      diverse panels 包含 ICL-susceptible 小模型成为攻击入口。但 MMLU×few_shot 出现 ceiling
      effect：所有模型 ASR > 0.70（MMLU 的 few-shot 模板更容易制造 confusion），η_max 方差
      被压缩，regression 退化（R²=0.12）。

      Persona manipulation（2 条件）：该攻击更接近 shared-bias 模式——不同模型对 authority
      persona 的响应差异较小（都有一定程度的 sycophancy toward perceived experts）。
      K_eff_resid 方向正但 NS（p=0.12, 0.18）。η_max 也仅 1/2 sig（persona 效应更 uniform）。
      这为 "When Diversity Helps" section 提供了重要边界条件：当攻击均匀影响所有 judge 时，
      K_eff 的 diverse attack surface 机制不生效。

      Instruction override（2 条件）：高度 targeted——直接注入评分指令主要影响 instruction
      following 弱的模型。η_max 强显著（2/2, β≈0.55-0.62），K_eff_resid NS。攻击完全集中
      在最弱 judge，diversity 无关紧要。

      合计：新攻击中仅 1/6 K_eff_resid sig。加上原 12 条件的 7/12，总计 8/18（0.44），
      在 extended metric range [7, 10] 内。整体叙事：K_eff 的有害效应在 transferable
      attacks 中最强，在 shared-bias 和 targeted attacks 中减弱或消失。
    tables:
      - name: "Table 4: Extended Regression Summary — 18 Conditions (455 Panels)"
        columns:
          - "Attack"
          - "Dataset"
          - "β(η_max)"
          - "p(η_max)"
          - "β(K_resid)"
          - "p(K_resid)"
          - "FDR K sig?"
          - "R²"
        rows:
          - ["prompt_inj", "MMLU", "0.52", "<0.001", "0.21", "0.003", "Yes", "0.42"]
          - ["prompt_inj", "ARC", "0.56", "<0.001", "0.19", "0.005", "Yes", "0.44"]
          - ["score_manip", "MMLU", "0.48", "0.002", "0.16", "0.012", "Yes", "0.38"]
          - ["score_manip", "ARC", "0.15", "0.142", "0.24", "3.7e-8", "Yes", "0.40"]
          - ["sycophancy", "MMLU", "0.55", "<0.001", "0.06", "0.285", "No", "0.34"]
          - ["sycophancy", "ARC", "0.58", "<0.001", "0.04", "0.418", "No", "0.36"]
          - ["verbosity", "MMLU", "0.42", "0.005", "0.09", "0.078", "No", "0.30"]
          - ["verbosity", "ARC", "0.44", "0.003", "0.14", "0.018", "Yes", "0.35"]
          - ["position", "MMLU", "0.39", "0.008", "0.18", "0.006", "Yes", "0.36"]
          - ["position", "ARC", "0.08", "0.683", "0.22", "5.2e-7", "Yes", "0.38"]
          - ["authority", "MMLU", "0.50", "<0.001", "0.05", "0.352", "No", "0.32"]
          - ["authority", "ARC", "0.46", "0.001", "0.07", "0.192", "No", "0.31"]
          - ["few_shot_hijack", "MMLU", "0.28", "0.108", "0.10", "0.135", "No", "0.12"]
          - ["few_shot_hijack", "ARC", "0.54", "0.001", "0.17", "0.022", "Yes", "0.36"]
          - ["persona_manip", "MMLU", "0.32", "0.065", "0.08", "0.182", "No", "0.18"]
          - ["persona_manip", "ARC", "0.30", "0.082", "0.11", "0.118", "No", "0.22"]
          - ["instr_override", "MMLU", "0.62", "<0.001", "0.06", "0.248", "No", "0.45"]
          - ["instr_override", "ARC", "0.55", "0.002", "0.08", "0.152", "No", "0.38"]
      - name: "Table 5: K_eff Significance by Attack Mechanism Type"
        columns:
          - "Attack Mechanism"
          - "Attacks"
          - "K_resid sig rate"
          - "η_max sig rate"
          - "Mean β(K_resid)"
          - "Interpretation"
        rows:
          - ["Transferable", "PI, SM, PB", "5/6", "4/6", "0.20", "K_eff amplifies vulnerability"]
          - ["Shared-bias", "Syc, Auth, VB, Persona", "1/8", "6/8", "0.07", "η_max dominates"]
          - ["Targeted", "Instr_override", "0/2", "2/2", "0.07", "η_max fully dominates"]
          - ["ICL-dependent", "Few_shot", "1/2", "1/2", "0.14", "Mixed / ceiling effect"]
    figures_description:
      - |
        Fig 3: Grouped forest plot of β(K_eff_resid) grouped by attack mechanism type
        (Transferable / Shared-bias / Targeted / ICL-dependent). Transferable cluster shows
        consistently positive β with CIs above zero; other clusters show β scattered around
        zero. Color gradient indicates η_max β magnitude for context.
      - |
        Fig 4: Heatmap of K_eff_resid p-values across 18 conditions (6 attacks × 2 datasets +
        new 3 × 2). FDR threshold line overlaid. Clear block pattern: transferable attacks
        (top rows) mostly significant; shared-bias and targeted attacks mostly NS.
    analysis: |
      Attack expansion 证实了 K_eff 效应的 attack-type dependency：K_eff 仅在 transferable
      attacks（利用模型间差异化弱点的攻击）中显著正，在 shared-bias 和 purely targeted attacks
      中不显著。

      这对叙事有双重影响：
      (1) 支持机制解释——K_eff 的有害效应来自 diverse attack surface（不同模型有不同弱点），
      而 shared-bias 攻击利用的是所有模型共享的弱点，diversity 在此无关。
      (2) 削弱普遍性——"diversity independently harmful" 仅在特定攻击类型下成立（5/18 = 28%
      如果只算 transferable 类别的 sig rate 则是 5/6 = 83%）。论文需要明确限定 claim 的适用
      条件。

      Overall sig rate 8/18 (44%) 远低于 v4 aspirational 的 12/12。论文标题从
      "The Diversity Trap" 改为 "Rethinking Diversity" 是必要的：diversity 在特定条件下
      有害（transferable attacks × heterogeneous pools），但并非普遍规律。

      Ceiling effect（MMLU×few_shot, R²=0.12）是方法论警告：部分条件下攻击过于有效，
      所有模型 ASR 趋近上限，regression 失去区分力。论文应在 limitations 中提及。

  - name: "Random-Fault BFT Contrast Experiment"
    plan_id: "plan_003"
    description: |
      (a) 形式化 Theorem 1: adaptive adversary 下 panel_ASR monotone in η_max;
      (b) Random-fault simulation: 每个 judge 独立以 empirical ASR p_j 概率失败, majority vote;
      (c) 对比 adaptive vs random-fault regime 下 K_eff_resid 的预测力和 β 大小。
      在当前 12 conditions 上运行（不依赖 plan_001 新模型）。
    expected_results:
      theorem_proved: true
      theorem_bound: "panel_ASR ≤ η_max · (1 + ε·log(K))"
      bound_tightness_factor: 1.35
      rf_keff_resid_sig_positive: 10
      rf_keff_resid_sig_rate: 0.833
      adaptive_keff_resid_sig_positive: 7
      adaptive_keff_resid_sig_rate: 0.583
      rf_mean_beta_keff: 0.25
      adaptive_mean_beta_keff: 0.18
      BFT_RF_beta_ratio: 1.39
      rf_mean_R2: 0.52
      adaptive_mean_R2: 0.38
      delta_R2_RF_vs_adaptive: 0.14
      sign_reversal_conditions: 0
      rf_eta_max_sig: 7
      rf_eta_max_mean_beta: 0.32
    result_rationale: |
      Theorem 1 成立：adaptive adversary 的最优策略是依次攻击 ordered judge vulnerabilities
      (η_(1) ≥ η_(2) ≥ ... ≥ η_(K)), majority vote 下需翻转 ≥⌈K/2⌉ 个 judge，因此
      panel_ASR 的主项为 η_max，修正项为 O(log K)。bound tightness factor = 1.35
      (median 档，empirical ASR 偏离理论上界 35%)，因为实际攻击不完全 adaptive——
      shared-bias 攻击（sycophancy, authority）有 random-fault 成分，在这些条件下 bound
      较 loose。

      **BFT 对比的关键发现：K_eff 在两种 regime 下均为正（diversity 均有害），无符号翻转。**
      这直接否定了 "diversity helps under random faults but hurts under adaptive" 的
      naive BFT prediction。原因：random-fault simulation 使用 empirical p_j（来自实际
      attack data），而 diverse panels 结构性地包含高 p_j 的弱模型。在 RF 下每个 judge
      独立以 p_j 失败——diverse panel 的弱 judge 失败更频繁，这比 adaptive regime 更直接
      地体现为 panel 级失败（因为 RF 下弱 judge 不需要被 "targeted"，它自然失败更多）。

      RF β(K_eff) = 0.25 vs Adaptive β(K_eff) = 0.18，ratio = 1.39（在 [1.0, 1.5] 范围内）。
      RF 下 K_eff 效应更大的机制：adaptive adversary 的策略集中在 η_max（weakest judge），
      这 "吸收" 了部分 K_eff 的方差（strategic targeting 使 η_max 成为更好的 predictor，
      留给 K_eff 的独立方差减少）。RF 下无 strategic targeting，每个 judge 的 p_j 均等
      贡献，K_eff 的 structural confound（diverse = weaker members）完全体现。

      ΔR² = 0.14（RF 比 adaptive 高 0.14），因为 RF 是确定性函数（majority vote of
      independent Bernoulli），无 strategic noise。Adaptive regime 的 R² 被 adversary
      策略引入的 unpredictable variance 压低。

      η_max 在 RF 下仅 7/12 sig（vs adaptive 9/12）：RF 下每个 judge 均等贡献，
      η_max 的 dominance 减弱。这是 BFT contrast 唯一可以挽救的点——虽然 K_eff 在两种
      regime 下都正，但 η_max 在 adaptive 下更重要，K_eff 在 RF 下更重要，
      两者的 relative importance 确实因 regime 而异。
    tables:
      - name: "Table 6: Adaptive vs Random-Fault Regime — β(K_eff_resid) Contrast"
        columns:
          - "Condition"
          - "β(K) Adaptive"
          - "p Adaptive"
          - "β(K) RF"
          - "p RF"
          - "Ratio RF/Adp"
          - "R² Adaptive"
          - "R² RF"
        rows:
          - ["MMLU×prompt_inj", "0.21", "0.003", "0.28", "<0.001", "1.33", "0.42", "0.55"]
          - ["MMLU×score_manip", "0.16", "0.012", "0.24", "0.002", "1.50", "0.38", "0.52"]
          - ["MMLU×sycophancy", "0.06", "0.285", "0.12", "0.042", "2.00", "0.34", "0.48"]
          - ["MMLU×verbosity", "0.09", "0.078", "0.18", "0.008", "2.00", "0.30", "0.45"]
          - ["MMLU×position", "0.18", "0.006", "0.25", "0.001", "1.39", "0.36", "0.50"]
          - ["MMLU×authority", "0.05", "0.352", "0.14", "0.028", "2.80", "0.32", "0.46"]
          - ["ARC×prompt_inj", "0.19", "0.005", "0.26", "<0.001", "1.37", "0.44", "0.58"]
          - ["ARC×score_manip", "0.24", "3.7e-8", "0.32", "<0.001", "1.33", "0.40", "0.55"]
          - ["ARC×sycophancy", "0.04", "0.418", "0.10", "0.068", "2.50", "0.36", "0.50"]
          - ["ARC×verbosity", "0.14", "0.018", "0.22", "0.003", "1.57", "0.35", "0.52"]
          - ["ARC×position", "0.22", "5.2e-7", "0.30", "<0.001", "1.36", "0.38", "0.54"]
          - ["ARC×authority", "0.07", "0.192", "0.15", "0.018", "2.14", "0.31", "0.48"]
      - name: "Table 7: BFT Contrast Summary"
        columns:
          - "Metric"
          - "Adaptive"
          - "Random-Fault"
          - "Difference"
          - "Interpretation"
        rows:
          - ["K_eff_resid sig rate", "7/12 (0.58)", "10/12 (0.83)", "+3 conditions", "RF detects more K_eff"]
          - ["Mean β(K_eff_resid)", "0.14", "0.21", "+0.07", "RF β 1.4× larger"]
          - ["η_max sig rate", "9/12 (0.75)", "7/12 (0.58)", "-2 conditions", "η_max weaker in RF"]
          - ["Mean β(η_max)", "0.44", "0.32", "-0.12", "Strategic targeting absent in RF"]
          - ["Mean R²", "0.38", "0.52", "+0.14", "RF more predictable"]
          - ["Sign reversals (K)", "0/12", "—", "0", "No qualitative reversal"]
    figures_description:
      - |
        Fig 5a: Paired lollipop chart showing β(K_eff_resid) under adaptive (orange circles)
        vs RF (blue circles) for each of 12 conditions, connected by lines. RF dots consistently
        higher/righter. No sign reversals (all positive). Significance markers (*) appear on
        10/12 RF dots but only 7/12 adaptive dots.
      - |
        Fig 5b: Schematic contrasting adaptive vs random-fault regimes. Left: adaptive adversary
        (arrows converging on weakest judge, η_max dominant). Right: random faults (arrows
        uniformly distributed, K_eff captures structural vulnerability). Central message:
        "same direction (K_eff positive), different relative importance (η_max vs K_eff)."
      - |
        Fig 5c: ΔR² bar chart across 12 conditions (RF R² - Adaptive R²). All bars positive
        (RF always more predictable). Mean line at ΔR²=0.14.
    analysis: |
      BFT contrast 的 median 档结果对叙事的影响：

      **坏消息**: 无符号翻转。论文不能说 "diversity helps under random faults but hurts under
      adaptive adversaries"——K_eff 在两种 regime 下都正。BFT "reversal" 作为论文核心理论
      贡献被大幅削弱。Claim 2 需要从 "K_eff regime reversal" 重新表述为 "predictability gap +
      relative importance shift"。

      **可以挽救的点**:
      (1) η_max 在 adaptive 下更重要（9/12 sig）, K_eff 在 RF 下更重要（10/12 sig vs 7/12）——
      relative importance 确实因 regime 而异, 这与 BFT 理论一致（RF 下 independence 的效用
      更可检测）。
      (2) ΔR² = 0.14 表明 RF regime 确实更 predictable——panel composition 对 RF 的解释力
      比 adaptive 高 37%。"Adaptive adversaries introduce strategic noise beyond panel structure"
      仍是有效论点。
      (3) Theorem 1 本身不依赖 empirical contrast——它是 worst-case bound，无论 RF 结果如何
      都成立。

      **叙事调整**: BFT 从 "empirically demonstrated reversal" 降级为 "theoretically motivated
      framework, empirically supported by relative importance shift but without qualitative
      reversal"。论文可以将此 honest 地表述为 limitation：theoretical prediction of K_eff sign
      reversal is not observed, likely because the structural confound (diverse panels include
      weaker models) persists in both regimes.

      Reviewer 若 push back: "your BFT story is a just-so story without empirical validation"
      ——论文回应：(a) Theorem 1 is valid independently; (b) relative importance shift is real;
      (c) the absence of sign reversal itself is informative—it reveals the structural
      confound as more fundamental than the adaptive/random distinction.

  - name: "Capability-Matched Validation: Within-Tier K_eff Analysis"
    plan_id: "plan_004"
    description: |
      在相同 capability tier 内测试 K_eff_resid 是否仍显著正。控制 η_max 方差的最直接方式。
      Tier 划分：Strong（70B + API, ~8 models, C(8,3)=56 panels）,
      Weak（7B + 14B, ~5 models, C(5,3)=10 panels）,
      API-only（5 models, C(5,3)=10 panels）。6 representative conditions。
    expected_results:
      strong_tier_n_models: 8
      strong_tier_n_panels: 56
      strong_keff_resid_sig_positive: 1
      strong_keff_resid_sig_rate: 0.167
      strong_eta_max_sig: 3
      strong_median_R2: 0.20
      strong_within_tier_r: 0.38
      weak_tier_n_models: 5
      weak_tier_n_panels: 10
      weak_keff_resid_sig_positive: 0
      weak_keff_resid_sig_rate: 0.0
      weak_eta_max_sig: 4
      weak_median_R2: 0.32
      weak_within_tier_r: 0.42
      api_tier_n_models: 5
      api_tier_n_panels: 10
      api_keff_resid_sig_positive: 1
      api_keff_resid_sig_rate: 0.167
      api_eta_max_sig: 2
      api_median_R2: 0.15
      api_within_tier_r: 0.35
      total_within_tier_keff_sig: 2
      full_pool_keff_sig_rate_ref: 0.583
      keff_reduction_factor: 3.5
    result_rationale: |
      **这是 median 档对 v4 核心 claim 最具破坏力的实验。** K_eff_resid 在 within-tier
      分析中仅 2/18 (1 strong + 1 API) 显著正（full pool 的 7/12 → within-tier 2/18），
      显著率从 58% 暴跌至 11%。

      机制解释：K_eff 在 full pool 中的正效应主要由 tier-mixing 驱动。当 panel 从 15 模型
      pool 中采样时，high-K_eff panel 结构性地跨越多个 capability tier——它们包含 7B 和 70B
      和 API 模型的组合。这些 panel 的 η_max 较高不仅仅因为 residualized 后的 K_eff 贡献，
      而是因为 tier-mixing 通过 K_eff-η_max 相关性之外的路径（如非线性交互、model-specific
      vulnerability profiles）影响 ASR。Residualization 只去除了线性相关，残留了非线性通道。

      **Within strong tier (56 panels)**：η_max range 从全局 [0.05, 0.85] 压缩到 [0.05, 0.30]。
      3/6 η_max sig——即使在 strong tier 内，个体鲁棒性差异仍可预测 ASR（GPT-4o 和 Llama-70B
      之间仍有可测量的鲁棒性差距）。K_eff_resid 仅 1/6 sig（MMLU×prompt_injection, p=0.038,
      β=0.12）——该条件下 prompt injection 攻击恰好利用了 strong models 之间的 instruction
      following 差异（GPT-4.1 vs Claude 的 prompt parsing 方式不同），diversity 在此提供了
      micro-level 的额外 attack surface。R²=0.20 (远低于 full pool 的 0.38)。

      **Within weak tier (10 panels)**：所有模型都 weak（η_max range [0.45, 0.85]），
      η_max 方差仍然大，4/6 sig。K_eff 0/6 sig——弱模型间的 diversity 不提供任何有害
      （或有益）效应，因为所有 judge 都容易被攻击，diversity 只是换一个同样弱的 judge。
      N=10 panels power 低是 caveat，但方向清晰。

      **Within API tier (10 panels)**：API 模型整体 robust（η_max range [0.05, 0.20]），
      η_max 方差极小，仅 2/6 sig。K_eff_resid 1/6 sig (ARC×score_manipulation, p=0.042)——
      这是一个 interesting outlier：API 模型在 score manipulation 上的 vulnerability profile
      有足够差异（GPT-4o 偏好高分, Claude 偏保守），diversity 在此暴露了 model-specific 弱点。
      但 N=10 power 太低，无法确认。

      **对论文核心 claim 的影响**：K_eff 的 "independent harmful effect" 在很大程度上是
      tier-mixing artifact。当控制 capability tier 后，K_eff 几乎消失。论文必须将此写为
      major limitation：K_eff_resid 在 full pool 中的显著性部分（甚至大部分）来自 tier-mixing
      通过非线性通道的 residual effect，而非 diversity 本身的因果有害性。

      Claim 1 因此需要进一步软化为："diversity is a risk factor in heterogeneous model pools,
      primarily because it is structurally associated with capability tier-mixing. The
      independent contribution of diversity beyond tier-mixing is small and condition-specific."
    tables:
      - name: "Table 8: Within-Tier vs Full-Pool K_eff_resid Significance Comparison"
        columns:
          - "Analysis Scope"
          - "N panels"
          - "K_resid sig(+) rate"
          - "η_max sig rate"
          - "Median R²"
          - "r(K_eff, η_max)"
        rows:
          - ["Full pool (ref)", "455", "7/12 (0.58)", "9/12 (0.75)", "0.38", "+0.72"]
          - ["Strong tier (70B+API)", "56", "1/6 (0.17)", "3/6 (0.50)", "0.20", "+0.38"]
          - ["Weak tier (7B+14B)", "10", "0/6 (0.00)", "4/6 (0.67)", "0.32", "+0.42"]
          - ["API-only", "10", "1/6 (0.17)", "2/6 (0.33)", "0.15", "+0.35"]
      - name: "Table 9: Strong Tier Detail — 6 Conditions (56 Panels)"
        columns:
          - "Condition"
          - "β(η_max)"
          - "p(η_max)"
          - "β(K_resid)"
          - "p(K_resid)"
          - "R²"
        rows:
          - ["MMLU×prompt_inj", "0.28", "0.035", "0.12", "0.038", "0.22"]
          - ["MMLU×score_manip", "0.24", "0.062", "0.08", "0.185", "0.18"]
          - ["MMLU×sycophancy", "0.32", "0.018", "0.03", "0.615", "0.21"]
          - ["ARC×prompt_inj", "0.30", "0.028", "0.09", "0.142", "0.24"]
          - ["ARC×score_manip", "0.12", "0.318", "0.10", "0.108", "0.14"]
          - ["ARC×sycophancy", "0.22", "0.085", "0.05", "0.425", "0.16"]
    figures_description:
      - |
        Fig 6a: Three-panel scatter (Strong / Weak / API tier) of K_eff (x) vs panel ASR (y)
        for MMLU×prompt_injection. Strong tier: flat with slight positive slope (β=0.12);
        Weak tier: flat (no K_eff signal); API tier: slight positive (but N=10, wide CI).
        Full-pool regression line overlaid in gray for contrast — much steeper positive slope.
      - |
        Fig 6b: Bar chart comparing K_eff_resid significance rate across scopes. Full pool
        (58%) towers over Strong (17%), Weak (0%), and API (17%). Error bars from bootstrap
        resampling. Clear message: K_eff effect is predominantly a cross-tier phenomenon.
    analysis: |
      capability-matched 实验是 median 档下 reviewer 最可能抓住的弱点——也是论文必须 honest
      地报告的核心 limitation。

      **叙事策略**: 不要试图 dismiss 这个结果。而是将其整合进 contribution：
      (1) Report prominently as Section 5.2 "Does Diversity Harm Within Capability Tiers?"
      Answer: mostly no.
      (2) Reframe K_eff 的角色：从 "independent harmful effect" 到 "amplifying factor in
      heterogeneous pools"。K_eff 是 tier-mixing 的 proxy，不是独立的因果因子。
      (3) 保留 confound-free 条件（r≈0.35, p<1e-7）作为 "even after tier-matching, residual
      K_eff effect exists in specific attack types" 的证据。
      (4) 将 within-tier finding 转化为 practical insight："if all judges are from the same
      capability tier, diversity is approximately neutral — the robustness-first principle
      is sufficient."

      **对 Claim 1 的影响**: 从 "diversity independently harmful (8/12 sig positive)" 降级为
      "diversity is a risk factor in heterogeneous pools (7/12 sig positive in full pool,
      2/18 within-tier), primarily reflecting capability tier-mixing."

      **对 Reviewer concern 的影响**: RC1 ("K_eff is just confound with η_max") 变得更有力——
      虽然 residualization 在 full pool 中控制了线性 confound，但 within-tier 分析表明
      非线性 confound 仍然 substantial。RC5 ("just use strongest") 的 rebuttal 更难——
      在 strong tier 内，K_eff 几乎无关紧要，strongest-K 策略接近最优。

  - name: "Two-Stage Panel Design Algorithm Full Benchmark"
    plan_id: "plan_005"
    description: |
      实现 robustness-first 两阶段算法并与 5 baselines 对比。
      Stage 1: filter η > threshold → 排除高风险 judge。
      Stage 2: 在合格 judge 中 maximize K_eff。
      Baselines: (1) Random, (2) Max-K_eff, (3) Min-η_max, (4) Strongest-K (top-3 by
      benchmark accuracy), (5) Max-family-diversity。
      15 模型池 × 6 representative conditions, K=3。Sweep threshold ∈ [0.10, 0.50]。
    expected_results:
      two_stage_mean_ASR: 0.091
      random_mean_ASR: 0.172
      two_stage_vs_random_reduction_pct: 47
      strongest_k_mean_ASR: 0.098
      two_stage_vs_strongest_k_reduction_pct: 7.1
      min_eta_max_mean_ASR: 0.095
      two_stage_vs_min_eta_pct: 4.2
      max_keff_mean_ASR: 0.155
      max_family_div_mean_ASR: 0.168
      two_stage_win_rate: 0.50
      two_stage_win_count: 3
      strongest_k_win_count: 2
      min_eta_max_win_count: 1
      optimal_threshold: 0.25
      threshold_sensitivity_range: "0.18-0.35"
      strong_regime_two_stage_vs_strongest_k_p: 0.42
    result_rationale: |
      Two-stage 算法的 median 档表现：平均 ASR 0.091，比 random 降低 47%（绝对降幅 8.1pp），
      在 [5, 14]% vs strongest-K baseline 的 range 内降低约 7%（绝对降幅 0.7pp）。

      **Two-stage 仅赢 3/6 条件**（win rate 0.50，低于 v4 aspirational 的 0.67+）：
      (1) Two-stage wins: MMLU×prompt_injection, ARC×prompt_injection, ARC×verbosity——
      这些是 K_eff 有残余效应的条件，Stage 2 的 diversity maximization 在 screened pool
      中提供了可测量的边际增益。
      (2) Strongest-K wins: MMLU×sycophancy, ARC×sycophancy——sycophancy 完全由个体鲁棒性
      决定，两阶段的 Stage 2 偶尔引入略弱但更 diverse 的 judge，反而微损。
      (3) Min-η_max wins: MMLU×score_manipulation——该条件下纯 η_max minimization 恰好
      选出最优组合（GPT-4o + Claude + GPT-4.1），Two-stage 的 Stage 2 引入了 Qwen-72B
      （更 diverse 但 score_manipulation ASR 略高）。

      **关键弱点**: Two-stage 与 Strongest-K 差异仅 0.7pp (7%)，statistical significance
      test p=0.42——完全不显著。这意味着论文不能 claim two-stage "significantly outperforms"
      strongest-K，只能说 "comparable or marginally better"。

      Threshold sensitivity 中等：optimal threshold = 0.25，在 0.18-0.35 范围内 ASR 波动
      < 15%。但 threshold 选择本身需要 held-out validation，增加了方法论复杂度。

      **对 Claim 6 的影响**: 从 "formal algorithm with demonstrated superiority" 降级为
      "practical guideline: robustness-first is the right principle, and among robustness-
      qualified judges, diversity is a neutral-to-marginal tiebreaker." The algorithm is
      not the contribution——the insight is.
    tables:
      - name: "Table 10: Panel Selection Strategy Comparison (Mean ASR, Lower = Better)"
        columns:
          - "Strategy"
          - "MMLU×PI"
          - "MMLU×SM"
          - "MMLU×Syc"
          - "ARC×PI"
          - "ARC×VB"
          - "ARC×Syc"
          - "Mean ASR"
          - "Rank"
        rows:
          - ["Two-stage", "0.075", "0.098", "0.112", "0.062", "0.088", "0.108", "0.091", "1.8"]
          - ["Min-η_max", "0.082", "0.088", "0.108", "0.068", "0.095", "0.112", "0.092", "2.2"]
          - ["Strongest-K", "0.078", "0.095", "0.105", "0.065", "0.098", "0.105", "0.091", "2.3"]
          - ["Max-K_eff", "0.142", "0.158", "0.175", "0.125", "0.148", "0.162", "0.152", "4.3"]
          - ["Max-family-div", "0.155", "0.168", "0.188", "0.138", "0.158", "0.178", "0.164", "4.8"]
          - ["Random", "0.165", "0.175", "0.192", "0.142", "0.162", "0.185", "0.170", "5.5"]
      - name: "Table 11: Threshold Sensitivity (Two-Stage Algorithm)"
        columns:
          - "Threshold η"
          - "N judges pass"
          - "Mean ASR"
          - "Δ from optimal"
          - "Stage 2 effect"
        rows:
          - ["0.10", "3", "0.098", "+0.007", "no-op (=Min-η_max)"]
          - ["0.15", "5", "0.094", "+0.003", "marginal"]
          - ["0.20", "7", "0.092", "+0.001", "small positive"]
          - ["0.25", "9", "0.091", "0.000", "optimal"]
          - ["0.30", "11", "0.095", "+0.004", "diluted"]
          - ["0.40", "13", "0.115", "+0.024", "weak judges enter"]
          - ["1.00", "15", "0.155", "+0.064", "=Max-K_eff"]
    figures_description:
      - |
        Fig 7a: Radar chart with 6 condition axes, comparing ASR for Two-stage (blue),
        Min-η_max (green), Strongest-K (orange). Three shapes nearly overlap, with
        Two-stage slightly inside (lower ASR) on 3 axes, Strongest-K slightly inside on 2.
        Max-K_eff and Random shapes much larger (higher ASR). Key visual: top-3 strategies
        are nearly indistinguishable.
      - |
        Fig 7b: Threshold sweep curve (x = threshold η, y = mean ASR). U-shaped with
        minimum at η=0.25. Left extreme (η=0.10) ≈ Min-η_max; right extreme (η=1.00) ≈
        Max-K_eff. Annotation at the flat bottom: "0.18-0.35 range yields within 3% of
        optimum."
    analysis: |
      Two-stage 算法在 median 档下不构成有力的 practical contribution。Top-3 策略
      (Two-stage, Min-η_max, Strongest-K) 之间差异极小且不显著（p=0.42 vs Strongest-K）。

      **对 reviewer RC5 的影响**: "just use the strongest models" 变成了合理建议——
      Strongest-K 在 2/6 条件中胜出，均值仅高 0.7pp，差异 NS。论文不能 dismiss 这个
      objection，只能回应：(a) "strongest" 定义依赖 benchmark，非 attack-specific 指标，
      实践中 robustness-first 更 principled；(b) 在 known vulnerable 条件（transferable
      attacks）下 two-stage 确实优于 strongest-K；(c) threshold 提供了 continuous knob
      而非 binary choice。

      **叙事调整**: Claim 6 从 "novel algorithm" 降级为 "design principle: avoid
      diversity-first strategies (Max-K_eff ranks 4th, Max-family-div ranks 5th). Among
      robustness-qualified judges, diversity is a neutral tiebreaker." 这仍然有价值——
      反驳了 "more diverse = safer" 的 conventional wisdom——但贡献在 insight 而非 method。

  - name: "Per-Judge ASR Concentration Analysis"
    plan_id: "plan_006"
    description: |
      对每个 panel × attack condition，测量 per-judge ASR 分布的集中度。
      Gini coefficient（0=均匀, 1=完全集中）、Shannon entropy（vs uniform baseline）、
      最弱 judge ASR 占比。455 panels × 12 conditions。分 tier 和 attack type 分析。
    expected_results:
      overall_gini_median: 0.45
      overall_gini_range: "0.12-0.72"
      weakest_judge_ASR_share_median: 0.55
      weakest_judge_share_K3_uniform_baseline: 0.333
      entropy_ratio_vs_uniform: 0.70
      gini_strong_tier_median: 0.25
      gini_weak_tier_median: 0.55
      gini_transferable_attacks: 0.52
      gini_shared_bias_attacks: 0.30
      concentration_eta_max_corr: 0.52
      concentration_keff_corr: 0.38
    result_rationale: |
      Gini=0.45（中等集中）表明 adaptive adversary 确实将攻击成功集中在 weakest judge，
      但不是完全集中——最弱 judge 承担 55% 的攻击成功（K=3 均匀基线 33%），是其他 judge
      的约 1.6×。这支持 η_max dominance 机制但程度比 fully-adaptive 假设温和。

      Tier 差异关键：Strong tier Gini=0.25（接近均匀，judge 间差异小，攻击分散）→ 解释
      plan_004 中 strong tier K_eff 几乎无效——当攻击不集中时，diversity 的 attack surface
      增加不构成额外威胁。Weak tier Gini=0.55 → 攻击高度集中在最弱 judge，η_max 效应强。

      Attack type 差异与 plan_002 结论一致：Transferable attacks Gini=0.52（集中，η_max
      dominates），shared-bias attacks Gini=0.30（分散，diversity 的角色更中性）。

      K_eff 与 concentration 的相关 r=0.38（中等正）表明高 diversity panel 的攻击
      集中度更高——但这大部分被 η_max 中介（partial r ≈ 0.15 控制 η_max 后）。
    tables:
      - name: "Table 12: ASR Concentration Metrics by Tier and Attack Type"
        columns:
          - "Scope"
          - "Gini (med)"
          - "Weakest Share"
          - "Entropy Ratio"
          - "r(Gini, η_max)"
        rows:
          - ["Overall", "0.45", "0.55", "0.70", "0.52"]
          - ["Strong tier panels", "0.25", "0.42", "0.84", "0.35"]
          - ["Weak tier panels", "0.55", "0.68", "0.58", "0.48"]
          - ["API tier panels", "0.22", "0.40", "0.86", "0.30"]
          - ["Transferable attacks", "0.52", "0.62", "0.65", "0.55"]
          - ["Shared-bias attacks", "0.30", "0.45", "0.78", "0.42"]
          - ["Targeted attacks", "0.58", "0.65", "0.60", "0.58"]
    figures_description:
      - |
        Fig 8: Violin plot of per-panel Gini coefficient, stratified by tier (Strong / Weak /
        API) and attack type (Transferable / Shared-bias). Weak × Transferable shows highest
        concentration (rightmost violin); Strong × Shared-bias shows lowest (leftmost).
        Horizontal dashed line at Gini=0.33 (uniform K=3 baseline).
    analysis: |
      Concentration analysis 为 adaptive adversary 机制提供了 moderate 级别的直接证据。
      Gini=0.45 和 weakest share=55% 支持 "attacks concentrate on weakest judge" 但不支持
      "attacks exclusively target weakest judge"。Tier × attack type 交互效应与 plan_004
      和 plan_002 的发现三角验证：K_eff 的有害效应主要出现在 weak-tier + transferable-attack
      的交叉区域。论文可以将 concentration analysis 作为 mechanism section 的 supporting
      evidence，但不能作为 standalone claim。

  - name: "Diversity-Capability Tradeoff Visualization and Decomposition"
    plan_id: "plan_007"
    description: |
      对 455 panels 绘制 K_eff vs η_max，拟合 tradeoff curve，展示 Pareto frontier，
      按 tier 分层。分解 overall correlation 为 between-tier 和 within-tier 成分。
    expected_results:
      overall_r_keff_eta: 0.72
      overall_r_p: "<0.001"
      within_7B_r: 0.40
      within_70B_r: 0.38
      within_API_r: 0.35
      between_tier_r: 0.82
      between_tier_variance_share: 0.72
      within_tier_variance_share: 0.28
      pareto_frontier_n_panels: 14
      pareto_knee_keff: 1.8
      pareto_knee_eta: 0.15
    result_rationale: |
      Overall r=+0.72（K_eff 与 η_max 正相关）反映了当前 LLM 生态的结构性事实：diversity
      主要来自 capability tier 差异——高 K_eff panel 必然跨 tier（包含 7B 和 70B 和 API），
      而跨 tier 意味着包含弱模型（高 η_max）。

      Between-tier r=0.82 vs within-tier r≈0.38 清晰表明 ~72% 的 tradeoff 来自 cross-tier
      选择。This is the statistical fingerprint of tier-mixing: the "diversity-capability
      tradeoff" is primarily a "tier-mixing artifact."

      Within-tier r≈0.38 表明即使在同 tier 内，diversity 仍轻度正相关于 η_max——可能因为
      同 tier 内更 diverse 的组合选入了更多 unusual/niche models（如 Mixtral-8x22B MoE
      架构），这些模型在某些攻击上更脆弱。但 0.38 远弱于 0.82。

      Pareto frontier 上 14 个 panels，knee 在 K_eff≈1.8, η_max≈0.15，对应 "2 strong API
      + 1 strong open-source 70B" 的组合。Knee 右侧（高 K_eff）ASR 急升；knee 左侧（低
      K_eff）边际安全增益递减。
    tables:
      - name: "Table 13: Tradeoff Decomposition — Between vs Within Tier"
        columns:
          - "Scope"
          - "N panels"
          - "r(K_eff, η_max)"
          - "p-value"
          - "Variance explained"
        rows:
          - ["Overall", "455", "+0.72", "<0.001", "100%"]
          - ["Between-tier component", "—", "+0.82", "<0.001", "72%"]
          - ["Within 7B", "10", "+0.40", "0.052", "8%"]
          - ["Within 70B", "10", "+0.38", "0.062", "7%"]
          - ["Within API", "10", "+0.35", "0.078", "6%"]
          - ["Within-tier pooled", "76", "+0.38", "<0.001", "28%"]
    figures_description:
      - |
        Fig 9a: Scatter plot of K_eff (x) vs η_max (y) for 455 panels. Points color-coded:
        all-within-tier panels (green), cross-tier panels (gray gradient by tier spread).
        Positive slope visible. Pareto frontier marked in black. Inset: zoomed within-tier
        sub-clouds showing weaker positive slopes.
      - |
        Fig 9b: Contour overlay on same scatter, showing panel ASR (lighter = lower ASR).
        Optimal region (low ASR) hugs Pareto frontier at the knee. High-K_eff region (right
        edge) shows dark contours (high ASR). Visual message: don't chase diversity.
    analysis: |
      Tradeoff visualization 是论文最直观的 figure，支持 Claim 3 但同时揭示了其 mechanism：
      tradeoff 是 tier-mixing 的直接后果，不是 diversity 本身的 intrinsic property。

      Between/within decomposition（72% vs 28%）为 plan_004 的 within-tier findings 提供了
      互补解释。论文中 Claim 3 应 reframe 为："The diversity-capability tradeoff is
      predominantly structural (driven by cross-tier panel composition) rather than
      fundamental. As model ecosystems mature with more uniformly capable models, the
      tradeoff may attenuate."

      Pareto frontier 分析直接服务于 Claim 6 的降级版本：最优策略是 "stay near the Pareto
      knee" 而非 "use a complex algorithm"。

  - name: "Panel Size Sensitivity K=3,5,7,9"
    plan_id: "plan_008"
    description: |
      测试 K_eff 正效应在不同 panel size 下的稳健性。
      K=3: C(15,3)=455, K=5: C(15,5)=3003, K=7: C(15,7)=6435, K=9: C(15,9)=5005。
      6 representative conditions per K。
    expected_results:
      k3_keff_resid_sig_positive: 4
      k3_eta_max_sig: 5
      k3_beta_ratio_eta_over_keff: 2.8
      k3_median_R2: 0.38
      k5_keff_resid_sig_positive: 3
      k5_eta_max_sig: 5
      k5_beta_ratio: 3.2
      k5_median_R2: 0.35
      k7_keff_resid_sig_positive: 2
      k7_eta_max_sig: 6
      k7_beta_ratio: 4.5
      k7_median_R2: 0.33
      k9_keff_resid_sig_positive: 1
      k9_eta_max_sig: 6
      k9_beta_ratio: 6.0
      k9_median_R2: 0.31
      keff_importance_trend: "decreasing with K"
      eta_max_dominance_increases: true
    result_rationale: |
      K_eff 的正效应（diversity 有害）随 panel size 增大而减弱，原因是 majority vote 的
      容错机制：K=3 时攻击者需翻转 2/3 judge（minority 就能 undermine），K=9 时需翻转
      5/9。在 K=9 的大 panel 中，单个弱 judge 的影响被多数投票稀释——diversity 引入的
      额外弱 judge 不再是决定性因素。

      η_max dominance 随 K 增大而增强（β ratio 从 2.8:1 到 6.0:1），因为大 panel 中
      "最弱 judge" 的 η_max 更 extreme（从 15 模型中选 9 个，almost certainly 包含一个
      很弱的），但 majority vote 使得需要更多 judge 被攻破——weakest judge 本身的 ASR
      仍是 panel 失败的 necessary condition（Theorem 1），但 sufficient condition 需要
      更多 judge 配合。

      K=9 时 K_eff 仅 1/6 sig——diversity 的有害效应在大 panel 中几乎消失。但这也意味着
      diversity 的有益效应（如果存在）也被 majority vote 掩盖。R² 从 0.38 降到 0.31
      表明大 panel 的 ASR 方差被 voting 压缩。

      Practical implication: K_eff 主要是 K=3 的 phenomenon。对于实际部署（通常 K=3 或
      K=5），K_eff 的有害效应是 relevant concern；对于 K≥7，可以忽略。
    tables:
      - name: "Table 14: K_eff Importance Across Panel Sizes"
        columns:
          - "K"
          - "N panels"
          - "K_resid sig(+)"
          - "η_max sig"
          - "β ratio η/K"
          - "Med R²"
          - "Mean ASR"
        rows:
          - ["3", "455", "4/6", "5/6", "2.8", "0.38", "0.172"]
          - ["5", "3003", "3/6", "5/6", "3.2", "0.35", "0.128"]
          - ["7", "6435", "2/6", "6/6", "4.5", "0.33", "0.098"]
          - ["9", "5005", "1/6", "6/6", "6.0", "0.31", "0.082"]
    figures_description:
      - |
        Fig 10: Line plot with K on x-axis. Two lines: standardized β(η_max) (blue, stable
        around 0.45-0.50) and β(K_eff_resid) (red, declining from ~0.18 to ~0.07). β ratio
        annotation at each K. η_max dominance increases monotonically. K_eff_resid approaches
        zero by K=9.
    analysis: |
      Panel size sensitivity 表明 K_eff 的有害效应是 small-panel phenomenon。论文应在
      discussion 中注明："our findings are most relevant for K=3 panels, which represent
      the majority of current deployment configurations (cost constraint). For K≥7, the
      diversity effect is negligible regardless of composition strategy."

      这也限制了 Claim 1 的 generalizability——8-page EMNLP paper 的 K=3 focus 是合理的，
      但 reviewer 可能要求 K=5 结果。K=5 数据（3003 panels）提供了强 power，3/6 K_eff sig
      表明效应在 K=5 仍可检测但减弱。

  - name: "VIF + Multicollinearity Diagnostics and Residualization Validation"
    plan_id: "plan_009"
    description: |
      在现有 455-panel data 上进行统计诊断：VIF analysis, partial correlations, FDR correction,
      beta regression (alternative to OLS for bounded [0,1] ASR), confound-free condition
      identification. 纯统计分析，无需 GPU。
    expected_results:
      VIF_after_residualization: 1.00
      VIF_before_residualization: 2.08
      partial_r_keff_given_eta_median: 0.22
      partial_r_keff_given_eta_range: "0.05-0.35"
      FDR_BH_keff_sig: 7
      bonferroni_keff_sig: 5
      confound_free_conditions: 2
      confound_free_r_values: "0.33, 0.35"
      confound_free_keff_p: "5.2e-7, 3.7e-8"
      beta_regression_keff_sig: 6
      beta_regression_concordance_with_OLS: 0.92
      condition_number: 4.2
      partial_eta2_keff_median: 0.04
      partial_eta2_eta_max_median: 0.18
    result_rationale: |
      VIF before residualization = 2.08（K_eff-η_max r=+0.72 对应 VIF = 1/(1-0.72²) ≈ 2.08），
      高于 cautionary threshold 但低于 critical threshold（VIF>5）。Residualization by
      construction 降至 1.00，消除线性 multicollinearity。

      Partial correlation r(K_eff | η_max) 中位数 0.22（range 0.05-0.35）：K_eff 在控制
      η_max 后仍有 modest 的独立相关性。最强 partial r = 0.35 出现在 confound-free 条件
      （ARC×score_manipulation, ARC×position_bias），最弱 partial r = 0.05 出现在
      shared-bias 条件（sycophancy, authority）。

      **FDR correction**: Benjamini-Hochberg 在 12 条件下 K_eff_resid 7/12 sig（与
      uncorrected 结果一致——因为显著的条件 p 值很小，排名靠前）。Bonferroni（更保守）
      降至 5/12：两个 borderline 条件（MMLU×score_manip p=0.012, ARC×verbosity p=0.018）
      在 Bonferroni 阈值 0.05/12=0.0042 下落入 NS。

      **2 confound-free 条件**（r≈0.33-0.35）确认了 K_eff 的独立效应不完全是 artifact：
      当 K_eff 和 η_max 的耦合较弱时，K_eff 仍极显著（p<1e-6）。但仅 2 个条件——
      reviewer 可能质疑为什么恰好这些条件 confound 低（是否 cherry-picked）。答案：
      ARC dataset 上 score_manipulation 和 position_bias 攻击恰好对不同 capability
      tier 的模型产生了不同于通常模式的 vulnerability profile，打破了 K_eff-η_max 的
      结构性耦合。

      **Beta regression**: 作为 robustness check（ASR ∈ [0,1]，OLS 假设可能不满足），
      6/12 conditions K_eff sig（比 OLS 少 1 个——ARC×verbosity 在 beta regression 下
      p=0.062）。92% concordance with OLS 表明 OLS 结果大体 robust，但 beta regression
      给出了略保守的估计。

      Partial η² 分析量化了 effect size：K_eff 中位数 partial η²=0.04（small effect），
      η_max 中位数 partial η²=0.18（medium-large effect）。η_max 的解释力是 K_eff 的
      4.5×——进一步确认 η_max 是 primary driver，K_eff 是 secondary amplifier。
    tables:
      - name: "Table 15: Multicollinearity Diagnostics Summary"
        columns:
          - "Diagnostic"
          - "Value"
          - "Threshold"
          - "Interpretation"
        rows:
          - ["VIF (raw K_eff)", "2.08", "<5 acceptable", "Moderate collinearity"]
          - ["VIF (K_eff_resid)", "1.00", "—", "Orthogonalized by construction"]
          - ["Condition number", "4.2", "<30 acceptable", "No severe multicollinearity"]
          - ["K_eff-η_max r", "+0.72", "—", "Strong positive confound"]
          - ["Median partial r(K|η)", "0.22", "—", "Small independent signal"]
          - ["Median partial η²(K)", "0.04", "<0.06 small", "Small effect size"]
          - ["Median partial η²(η)", "0.18", ">0.14 large", "Large effect size"]
      - name: "Table 16: FDR vs Bonferroni Correction Comparison (K_eff_resid)"
        columns:
          - "Condition"
          - "p(K_resid)"
          - "FDR sig?"
          - "Bonferroni sig?"
          - "Confound r"
        rows:
          - ["ARC×score_manip", "3.7e-8", "Yes", "Yes", "0.35"]
          - ["ARC×position", "5.2e-7", "Yes", "Yes", "0.33"]
          - ["MMLU×prompt_inj", "0.003", "Yes", "Yes", "0.74"]
          - ["ARC×prompt_inj", "0.005", "Yes", "No", "0.72"]
          - ["MMLU×position", "0.006", "Yes", "No", "0.68"]
          - ["MMLU×score_manip", "0.012", "Yes", "No", "0.71"]
          - ["ARC×verbosity", "0.018", "Yes", "No", "0.70"]
          - ["MMLU×verbosity", "0.078", "No", "No", "0.73"]
          - ["ARC×authority", "0.192", "No", "No", "0.74"]
          - ["MMLU×sycophancy", "0.285", "No", "No", "0.78"]
          - ["MMLU×authority", "0.352", "No", "No", "0.76"]
          - ["ARC×sycophancy", "0.418", "No", "No", "0.75"]
    figures_description:
      - |
        Fig 11: Volcano plot of K_eff_resid across 12 conditions. X-axis: β(K_eff_resid),
        Y-axis: -log10(p). FDR threshold as horizontal dashed line (blue), Bonferroni as
        second line (red, more stringent). 7 points above FDR line, 5 above Bonferroni.
        Two confound-free conditions (ARC×SM, ARC×PB) labeled and circled — they sit in
        the top-right (large β, very low p). Color = confound r value (darker = higher
        confound).
    analysis: |
      Plan_009 提供了 K_eff 独立效应的完整统计 infrastructure。三条核心结论：

      (1) K_eff 的独立效应 exists（7/12 FDR sig, 5/12 Bonferroni sig, 2 confound-free
      conditions with p<1e-6）但 effect size small（partial η²=0.04）。

      (2) η_max 是 primary driver with medium-large effect（partial η²=0.18），K_eff
      的独立贡献约为 η_max 的 1/4。

      (3) Beta regression 作为 robustness check 给出 consistent but slightly conservative
      results（6/12 vs OLS 7/12）。

      论文策略：report FDR 作为 primary（standard in ML），Bonferroni 作为 conservative
      bound，confound-free conditions 作为 "regardless of correction method" evidence。
      Partial η² 用于 framing effect magnitude——承认 K_eff 效应虽然统计显著但 practically
      modest。这种 honest reporting 在 EMNLP 审稿中通常受到正面评价。

  - name: "Aggregation Rule Modulation: Majority, Threshold, Bayesian, Weighted"
    plan_id: "plan_010"
    description: |
      在 455 panels × 12 conditions 上测试不同聚合规则如何调节 dual vulnerability drivers。
      (1) Majority vote (baseline), (2) Threshold/unanimity (all judges must agree),
      (3) Bayesian aggregation (accuracy-weighted), (4) Reliability-weighted voting。
      核心假设：threshold 放大 K_eff; Bayesian 削弱 η_max。
    expected_results:
      majority_keff_resid_sig: 7
      majority_eta_max_sig: 9
      threshold_keff_resid_sig: 9
      threshold_eta_max_sig: 9
      threshold_keff_amplification_ratio: 1.45
      bayesian_keff_resid_sig: 4
      bayesian_eta_max_sig: 5
      bayesian_eta_max_reduction_ratio: 0.55
      weighted_keff_resid_sig: 5
      weighted_eta_max_sig: 7
      bayesian_mean_ASR_reduction_vs_majority: 0.18
      threshold_mean_ASR_increase_vs_majority: 0.12
      six_model_pattern_replication: "partial"
    result_rationale: |
      **Threshold/unanimity (K_eff sig 9/12)**：当要求所有 judge 一致同意时，单个 weak
      judge 就能阻止共识——diverse panel 中任何一个 judge 被攻破都导致 panel "failure"
      （无法达成共识 → adversary wins）。这将 panel vulnerability 从 majority 的
      "需翻转 ⌈K/2⌉ judges" 变为 "只需翻转 1 judge"，极大放大了 K_eff 的效应
      （β amplified 1.45×）。K_eff_resid 从 7/12 升至 9/12——两个原来 NS 的 shared-bias
      条件（MMLU×verbosity, ARC×authority）在 unanimity 下变显著，因为即使在 shared-bias
      攻击下，只要有一个 judge 与其他不同（diversity→），攻击就能利用这个差异。

      **Bayesian aggregation (K_eff sig 4/12, η_max sig 5/12)**：Bayesian weighting 用
      每个 judge 的 estimated accuracy 作为 prior，给 robust judge 更高权重。这直接
      对冲了 η_max 的效应——弱 judge 被 down-weighted，即使其 ASR 高也不影响最终
      decision。η_max sig 从 9/12 降至 5/12（reduction ratio 0.55）。K_eff 也被间接
      削弱（7/12 → 4/12），因为 K_eff 的有害效应主要通过弱 judge 传导——当弱 judge
      被 down-weighted 后，diversity 引入的额外弱 judge 不再构成威胁。

      但 Bayesian 的 η_max 削弱在 median 档下不确定（partial replication）：6-model
      结果显示 η_max 2/12 sig（dramatic reduction），15-model 结果 5/12 sig（moderate）。
      原因：accuracy prior 在 15 模型池中更 noisy——API 模型的 accuracy 在不同 dataset
      上差异较大（GPT-4o 在 MMLU 上很强但在 ARC 的某些 subtask 上不那么稳定），
      prior misestimation 削弱了 Bayesian 的 corrective power。

      **Weighted voting (K_eff sig 5/12, η_max sig 7/12)**：中间方案，效果弱于 Bayesian
      因为权重方案更 ad hoc（基于 benchmark accuracy 而非 posterior）。

      6-model pattern partial replication：threshold amplifies K_eff (confirmed),
      Bayesian weakens η_max (confirmed but less dramatically)。Bayesian 的 η_max 削弱
      从 6-model 的 dramatic (2/12) 变为 moderate (5/12) 是 median 档的关键不确定性。
    tables:
      - name: "Table 17: Aggregation Rule × Vulnerability Driver Interaction"
        columns:
          - "Aggregation"
          - "K_resid sig(+)"
          - "η_max sig"
          - "K β amplif."
          - "η β change"
          - "Mean ASR"
        rows:
          - ["Majority (ref)", "7/12", "9/12", "1.00×", "1.00×", "0.172"]
          - ["Threshold/Unanimity", "9/12", "9/12", "1.45×", "1.05×", "0.192"]
          - ["Bayesian", "4/12", "5/12", "0.65×", "0.55×", "0.142"]
          - ["Reliability-weighted", "5/12", "7/12", "0.80×", "0.78×", "0.155"]
      - name: "Table 18: Bayesian Aggregation — 6-Model vs 15-Model Pattern Comparison"
        columns:
          - "Metric"
          - "6-model (20 panels)"
          - "15-model (455 panels)"
          - "Replication?"
        rows:
          - ["η_max sig rate", "2/12 (0.17)", "5/12 (0.42)", "Partial (weaker)"]
          - ["K_eff sig rate", "1/12 (0.08)", "4/12 (0.33)", "Direction consistent"]
          - ["ASR reduction vs majority", "22%", "18%", "Yes"]
          - ["Accuracy prior quality", "High (6 models)", "Moderate (15 models)", "Degraded"]
    figures_description:
      - |
        Fig 12a: Grouped bar chart with 4 aggregation rules on x-axis, K_eff_resid sig rate
        (red) and η_max sig rate (blue) on y-axis. Clear pattern: Threshold amplifies K_eff
        (red bar tallest); Bayesian suppresses both (both bars shortest).
      - |
        Fig 12b: Line plot showing how each aggregation rule modulates β(K_eff_resid) across
        12 conditions. Threshold line (red) consistently above Majority (gray); Bayesian line
        (green) consistently below. Shaded bands for 95% CI.
    analysis: |
      Aggregation modulation 是 Claim 7 的核心，median 档下 partial replication：

      **Threshold amplifies K_eff**: Confirmed (9/12, β×1.45)。这是 strongest result of
      the aggregation analysis——unanimity voting 使 diversity 的有害效应 dramatically
      worse。Practical implication: "never use unanimity in adversarial settings."

      **Bayesian weakens η_max**: Confirmed but less dramatically (5/12 vs 6-model's 2/12)。
      This is the key uncertainty in median tier——论文不能 claim "Bayesian breaks the
      weakest-link" (which requires η_max < 3/12 sig to be compelling)。Instead: "Bayesian
      aggregation partially mitigates individual weakness but does not eliminate it."

      论文策略：Threshold result is the cleaner story (amplification is dramatic and well-
      motivated). Bayesian result is softer—report as "promising partial defense" with
      caveat about accuracy prior quality. This provides ammunition against RC7 ("why not
      just use Bayesian?"): Bayesian helps but doesn't solve the problem, especially
      with noisy accuracy priors in large model pools.

  - name: "Open-Ended Generation Benchmark (MT-Bench Style)"
    plan_id: "plan_011"
    description: |
      在 MT-Bench 风格的开放式生成任务上测试 K_eff 的有害效应。设计 adversarial perturbations
      targeting judge evaluation of open-ended responses（rubric manipulation, style
      injection, calibration attacks）。15 models, 455 panels, 3 attack types × 1 dataset。
    expected_results:
      n_conditions: 3
      keff_resid_direction_positive: 3
      keff_resid_sig_positive: 0
      keff_resid_p_range: "0.065-0.185"
      eta_max_sig: 1
      eta_max_p_range: "0.028-0.215"
      median_R2: 0.12
      mean_ASR: 0.38
      ASR_variance: 0.08
      power_analysis_required_N_for_sig: 1200
    result_rationale: |
      Open-ended 任务下 K_eff 方向一致（3/3 positive = diversity 有害方向）但全部 NS
      （p range 0.065-0.185）。η_max 也仅 1/3 sig——整体 regression 解释力极弱
      （R²=0.12, vs MCQ 的 0.38）。

      **K_eff NS 的原因（disentangling power vs effect）**:

      (1) **Effect size genuinely smaller**: Open-ended 评估的 inter-judge variance 更大
      （rubric 主观性、response 长度效应、style 偏好），这些 noise 淹没了 compositional
      effects。Attacks 也更 diffuse——rubric manipulation 不像 prompt injection 那样
      precision-target 特定 model 弱点，而是 broadly shift 评分分布。

      (2) **Power issue**: Open-ended task 的 ASR 定义更模糊（score shift > threshold
      vs binary flip），导致更高的 measurement noise。Post-hoc power analysis 表明
      需要 N≈1200 panels 才能在 α=0.05 下检测到 observed effect size（β≈0.10）——
      455 panels 只提供 ~35% power。

      (3) **Attack design limitation**: Open-ended attacks 是 novel（未经过像 MCQ 攻击
      那样的 iterative optimization），可能 suboptimal。

      Median 档下这三个原因的权重无法区分——论文应 honestly 报告为 "inconclusive: direction
      consistent but underpowered or weaker effect."
    tables:
      - name: "Table 19: Open-Ended Benchmark Results (MT-Bench Style)"
        columns:
          - "Attack Type"
          - "β(η_max)"
          - "p(η_max)"
          - "β(K_resid)"
          - "p(K_resid)"
          - "R²"
          - "Mean ASR"
        rows:
          - ["Rubric manipulation", "0.22", "0.028", "0.10", "0.065", "0.15", "0.42"]
          - ["Style injection", "0.15", "0.118", "0.08", "0.142", "0.10", "0.35"]
          - ["Calibration attack", "0.12", "0.215", "0.06", "0.185", "0.08", "0.38"]
      - name: "Table 20: Power Analysis for Open-Ended K_eff Detection"
        columns:
          - "Metric"
          - "MCQ (ref)"
          - "Open-ended"
          - "Ratio"
        rows:
          - ["Observed β(K_resid)", "0.18", "0.08", "0.44×"]
          - ["ASR variance", "0.04", "0.08", "2.0×"]
          - ["R²", "0.38", "0.12", "0.32×"]
          - ["Power at N=455", ">0.90", "0.35", "—"]
          - ["N required for 0.80 power", "~100", "~1200", "12×"]
    figures_description:
      - |
        Fig 13: Forest plot of β(K_eff_resid) for MCQ conditions (left, 12 conditions)
        vs open-ended conditions (right, 3 conditions). MCQ shows mix of significant and
        NS; open-ended shows all positive but with wide CIs crossing zero. Annotation:
        "consistent direction, insufficient power."
    analysis: |
      Open-ended results 是 median 档下的 key limitation。论文必须 report 但不能
      over-interpret：

      (1) 方向一致性（3/3 positive）是 weak positive signal。
      (2) 全部 NS（p>0.05）意味着不能 claim K_eff 有害效应 extends to open-ended tasks。
      (3) Power analysis 表明可能是 underpowered（35% power）而非 absent effect。

      **论文处理策略**: 在 "Scope and Limitations" 中写一段：our findings are established
      on MCQ evaluation tasks. Preliminary results on open-ended tasks show direction-
      consistent but non-significant K_eff effects, potentially reflecting smaller effect
      sizes or insufficient statistical power. Extending these findings to open-ended
      evaluation is an important direction for future work.

      **Reviewer 影响**: Open-ended NS 结果限制了 generalizability claim。但如果论文
      明确将 scope 限定在 MCQ evaluation（覆盖 MMLU, ARC 等主要 benchmark），这是
      acceptable scope for an EMNLP paper。

  - name: "Partial-Knowledge Adversary Model"
    plan_id: "plan_012"
    description: |
      模拟部分知识对手：adversary 知道 model family labels 和 tier 划分，但不知道
      exact per-judge vulnerability profile (η_j)。Adversary 使用 family-level average
      vulnerability 作为 proxy 选择攻击策略。对比 full-knowledge vs partial-knowledge
      下 K_eff_resid 的预测力变化。12 conditions, 455 panels。
    expected_results:
      full_knowledge_ASR_mean: 0.172
      partial_knowledge_ASR_mean: 0.128
      partial_vs_full_ratio: 0.74
      partial_keff_resid_sig: 3
      partial_eta_max_sig: 5
      full_keff_resid_sig_ref: 7
      full_eta_max_sig_ref: 9
      keff_sig_reduction: 4
      partial_R2_mean: 0.22
      full_R2_ref: 0.38
    result_rationale: |
      Partial-knowledge adversary 达到 full-knowledge 74% 的 ASR——family-level 信息已提供
      足够的 targeting guidance（知道 7B 模型比 API 模型弱，可以集中攻击小模型所在的
      panel 位置）。但 precise targeting 能力下降。

      K_eff_resid sig 从 7/12 降至 3/12：without exact vulnerability knowledge，adversary
      无法精确利用 diverse panel 中不同 judge 的特异性弱点。K_eff 的有害效应依赖于
      adversary 能够针对每个 judge 的 specific vulnerability profile 制定差异化攻击——
      partial knowledge 削弱了这种能力，使攻击更趋 uniform，K_eff 的 diverse attack
      surface 机制被 blunted。

      η_max sig 也下降（9/12 → 5/12）但降幅小于 K_eff（因为 η_max 的 proxy "use tier
      average" 仍能 coarsely identify weak judges）。

      **对论文的影响**: 强化了 "K_eff 有害效应依赖于 adversary capability" 的 qualification。
      论文应在 threat model 中明确：our main results assume a strong adaptive adversary
      with full model knowledge. Under partial knowledge, both K_eff and η_max effects
      attenuate, with K_eff attenuating more rapidly (3/12 vs 7/12).

      这也意味着 "Diversity Trap" narrative 仅在 strong adversary 假设下成立——对于
      realistic adversaries with imperfect knowledge，diversity 的有害效应 substantially
      diminished。Another reason to soften to "Rethinking Diversity"。
    tables:
      - name: "Table 21: Full vs Partial Knowledge Adversary Comparison"
        columns:
          - "Metric"
          - "Full Knowledge"
          - "Partial Knowledge"
          - "Reduction"
        rows:
          - ["Mean ASR", "0.172", "0.128", "-26%"]
          - ["K_resid sig rate", "7/12 (0.58)", "3/12 (0.25)", "-57%"]
          - ["η_max sig rate", "9/12 (0.75)", "5/12 (0.42)", "-44%"]
          - ["Mean R²", "0.38", "0.22", "-42%"]
          - ["Mean β(K_resid) when sig", "0.18", "0.12", "-33%"]
    figures_description:
      - |
        Fig 14: Side-by-side volcano plots: left = full knowledge (7 points above FDR line),
        right = partial knowledge (3 points above FDR line). Points labeled by condition.
        Arrows connecting same conditions across panels show systematic downward shift
        (lower -log10(p)) under partial knowledge. Largest drops in K_eff_resid significance;
        smaller drops in η_max.
    analysis: |
      Partial-knowledge 实验量化了 threat model 的 sensitivity。K_eff 效应对 adversary
      knowledge 的 sensitivity 高于 η_max（-57% vs -44% sig rate reduction），这与
      机制解释一致：η_max 是 structural property（弱 judge 在任何攻击下都弱），K_eff
      需要 precision targeting（不同 judge 有不同弱点，需要知道具体弱点才能利用 diverse
      attack surface）。

      论文策略：partial-knowledge 结果放入 Section 5 "Robustness and Scope"，作为
      important nuance。Message: "our findings establish the worst-case scenario (strong
      adversary); real-world adversaries with imperfect knowledge face a substantially
      attenuated diversity effect."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f47c7fb-59b3-4d95-9db2-4dde1f537d7d",
  "isSidechain": false,
  "requestId": "req_011CbJ3JGTSK796f56HJQqNq",
  "type": "assistant",
  "uuid": "bc3deeb0-4593-4af4-9da6-7872bc3d5cf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HP3vqH7JdeKc8sZzH3Rd22",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23777,
      "cache_read_input_tokens": 34497,
      "output_tokens": 38648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 38648,
          "cache_read_input_tokens": 34497,
          "cache_creation_input_tokens": 23777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23777
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 K_eff 发现在当前 12 条件上 hold，但扩展证据参差不齐：capability-matched 大幅削弱 K_eff，BFT contrast 仅为量级差异非定性翻转，open-ended 趋势但不显著 核心假设：['K_eff residualized 保持 6-8/12 显著（部分条件…",
  "leafUuid": "bc3deeb0-4593-4af4-9da6-7872bc3d5cf6",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling diversity trap findings to 15 models",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 K_eff 发现在当前 12 条件上 hold，但扩展证据参差不齐：capability-matched 大幅削弱 K_eff，BFT contrast 仅为量级差异非定性翻转，open-ended 趋势但不显著 核心假设：['K_eff residualized 保持 6-8/12 显著（部分条件…",
  "leafUuid": "bc3deeb0-4593-4af4-9da6-7872bc3d5cf6",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Scaling diversity trap findings to 15 models",
  "sessionId": "34a5b542-e783-47b2-9848-2d8500537446"
}
```

---
