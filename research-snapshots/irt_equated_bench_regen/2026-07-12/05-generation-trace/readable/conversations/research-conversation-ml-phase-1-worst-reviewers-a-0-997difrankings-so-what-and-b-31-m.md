# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：核心张力未化解：reviewers同时认为(a) ρ=0.997说明DIF不影响rankings所以'so what'，AND (b) 31%可能是M

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/530279c9-746a-474b-ac69-6d2a4f70c94e.jsonl`
- **Structured JSON:** [`72ac2405f54630e79307.json`](../../sessions/72/72ac2405f54630e79307.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T14:34:28.362Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T14:34:28.362Z",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：核心张力未化解：reviewers同时认为(a) ρ=0.997说明DIF不影响rankings所以'so what'，AND (b) 31%可能是MH method artifact（unidimensional IRT misfit + LLM population不满足MH assumptions）。两个方向的attack形成pincer——instability要么不存在要么不重要。\n核心假设：['至少1位reviewer认为ability confound decomposition (2.4pp)不够convincing——要求propensity-score matching或MIMIC model，而非简单NN matching', 'MH-DIF的unidimensional IRT假设被正面攻击——98% |Lz|>2的misfit数据被reviewer引用为evidence against method validity', 'Ground truth meta-critique被全部reviewers视为obvious或out-of-scope', \"Semi-synthetic injection被视为artificial——'flipping incorrect→correct doesn't model real contamination mechanisms'\", \"ρ=0.997的ranking stability被视为evidence AGAINST the paper's importance而非FOR robustness\", \"6-benchmark replication中的C%变异(17.9-31.3%)被解读为'DIF is benchmark-dependent, not a universal phenomenon'\", 'plan_029 permutation null成功但reviewer认为permutation不保留temporal structure，要求block permutation']\n关键指标范围：{'reviewer_avg_score': [2.75, 3.25], 'permutation_null_mean_c_pct': [0.5, 2.0], 'permutation_null_p_value': [0.0, 0.05], 'rebuttal_issues_count': [5, 8], 'claims_accepted_without_caveat': [0, 1], 'page_compression_info_loss_pct': [15, 30], 'reviewers_questioning_method_validity': [2, 3]}\n叙事方向：需要fundamental reframing，但不降级venue。新angle：从'DIF reveals instability'转向'DIF as stress test for benchmark measurement assumptions'——paper的贡献不再是'31% items are unstable'，而是'applying psychometric diagnostics to LLM benchmarks exposes that standard IRT assumptions (unidimensionality, local independence, temporal invariance) are systematically violated, and we characterize HOW they fail。' 具体操作：(1)将98% Lz misfit从limitation翻转为primary finding——MMLU fundamentally violates IRT assumptions，this itself is newsworthy；(2)将6-benchmark C%变异reframe为'benchmark-specific measurement properties'而非weakness；(3)将ρ=0.997 reframe为'massive redundancy in MMLU means 31% items can be removed without information loss——this is a finding about benchmark design efficiency'；(4)Semi-synthetic framework从validation tool降级为methodological appendix，主叙事转向empirical characterization。Claim 2 (meta-critique)从numbered contribution降为Discussion section observation。新headline：'Psychometric audit of 6 LLM benchmarks reveals systematic violations of measurement invariance assumptions——31% of MMLU items show temporal DIF, but ranking-irrelevant redundancy masks the instability.' 需要补充的实验：multidimensional IRT pilot（至少2-factor model on 5 subjects）作为rebuttal evidence或camera-ready addition。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\nfocus: This is re-dream #8 after major revisions addressing Dream #7's specific weaknesses. Key improvements since Dream #7 (all integrated into paper via P6-P16 patches):\n\n1. **Actionability paradox SOLVED** (was CW1-level concern): NEW plan_032 DIF-cleaned MMLU demonstration shows 89.5% models shift ≥5 ranks, systematic cohort bias (2024 Δrank=+73.6), confirmed DIF-specific by random baseline (z=8.5). This directly answers \"ρ=0.997 means DIF doesn't matter.\"\n\n2. **Proposition 1 (ΔFPR=0 formalized)**: Cross-subject matching now has a formal algebraic proof, not just an empirical observation. Elevates methodological contribution.\n\n3. **Temporal coarseness addressed**: NEW plan_031 6-month window robustness check (C%=34.35%, 181× enrichment) shows DIF is robust to finer temporal granularity.\n\n4. **Subject DIF direction asymmetry** (NEW analytical finding): STEM subjects favor 2024 models (55.4%), Humanities favor 2023 (64.4%) — content-level predictor of DIF direction.\n\n5. **Expanded Related Work**: Added BHI (Blebea et al. 2024), PSN-IRT (Polo et al. 2024), Maeda (2024) — addresses \"thin related work\" concern.\n\n6. **Systematic Confound Elimination narrative**: 6 negative results reframed as systematic exclusion of confounds (architecture, ability, local dependence, IRT misfit, reasoning-RL, ensemble), strengthening the \"what remains is genuine temporal DIF\" argument.\n\n7. **Bootstrap CI on headline C%**: MMLU C%=31.3% [29.5%, 33.1%] with N=1000 model resampling.\n\n8. **Causal language softened** throughout — \"contamination-adjacent\" phrasing replaced with hedged \"differential functioning\" language.\n\n9. **DIF-for-LLMs paragraph** added in Discussion — explicitly addresses what DIF means for machine (vs. human) examinees.\n\n10. **Audit protocol expanded** with code release commitment.\n\n11. **ConStat/DVD comparison visibility increased** — AUROC numbers and Jaccard overlap now in main text.\n\nReviewers should evaluate whether these revisions close the gap from 3.5 to 4.0 (Conference). The paper's strongest path to 4.0: unprecedented scale + cross-subject matching (Proposition 1) + Simpson's paradox + DIF-cleaned demonstration (actionability) + 6-benchmark replication + systematic confound elimination.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n      bootstrap_ci_95:\n      - 29.38\n      - 38.05\n      bootstrap_mean: 33.14\n      bootstrap_sd: 2.3\n      bootstrap_n: 1000\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n- exp_id: plan_031_temporal_granularity\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_full_year:\n      comparison: 2023 vs 2024\n      distance_yr: 1\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.32\n      random_pct_c: 0.02\n    mmlu_half_year:\n      comparison: 2023-H2 vs 2024-H1\n      distance_yr: 0.5\n      n_ref: 1018\n      n_foc: 807\n      pct_c: 34.35\n      random_pct_c: 0.19\n    mmlu_within_2023:\n      comparison: 2023-H1 vs 2023-H2\n      distance_yr: 0.5\n      n_ref: 62\n      n_foc: 1018\n      pct_c: 22.62\n      random_pct_c: 0.18\n      supplementary: true\n    cross_bench_half_year:\n      arc_pct_c: 29.27\n      hellaswag_pct_c: 18.07\n      winogrande_pct_c: 33.62\n      truthfulqa_pct_c: 31.33\n    cross_bench_full_year:\n      arc_pct_c: 26.88\n      hellaswag_pct_c: 17.89\n      winogrande_pct_c: 30.31\n      truthfulqa_pct_c: 29.74\n    half_year_gt_full_year_all_benchmarks: true\n    dif_saturates_within_6mo: true\n- exp_id: plan_032_dif_cleaned_mmlu\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_items_full: 12508\n    n_items_cleaned: 8590\n    n_items_removed: 3918\n    pct_removed: 31.3\n    spearman_rho: 0.9965\n    rank_change_std: 127.1\n    rank_change_min: -589\n    rank_change_max: 849\n    pct_change_ge5: 89.5\n    pct_change_ge10: 79.5\n    pct_change_ge20: 66.4\n    pct_change_ge50: 41.9\n    pct_change_ge100: 24.8\n    top100_pct_ge10: 18\n    top500_pct_ge10: 47.2\n    cohort_2023_mean_change: -22.56\n    cohort_2023_median_change: -5\n    cohort_2024_mean_change: 73.6\n    cohort_2024_median_change: 11\n    systematic_bias: DIF items favor 2024 models; cleaning hurts 2024 +73.6 avg, helps\n      2023 -22.6 avg\n    top_hurt_families:\n      phi-3: 258.35\n      command-r: 235\n      solar: 149.15\n      llama-3: 120.86\n    top_benefit_families:\n      mistral-0.1: -60.32\n      mistral: -53.27\n      zephyr: -29.94\n      gemma-2: -28.78\n    removed_items_harder: true\n    removed_mean_difficulty: 0.409\n    cleaned_mean_difficulty: 0.46\n    random_baseline_20trials:\n      rank_change_std:\n        mean: 60.2\n        std: 7.8\n      mean_abs_rank_change:\n        mean: 36\n        std: 3.6\n      pct_change_ge100:\n        mean: 8.5\n        std: 2\n      cohort_2023_mean_change:\n        mean: 0.4\n        std: 4.1\n      cohort_2024_mean_change:\n        mean: 2.8\n        std: 21.2\n    dif_vs_random_z_scores:\n      rank_change_std_z: 8.5\n      mean_abs_change_z: 10.7\n      pct_ge100_z: 8.2\n      cohort_2023_z: -5.6\n      cohort_2024_z: 3.3\n      cohort_asymmetry_gap_z: 4.4\n- exp_id: plan_033_subject_dif_concentration\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_subjects: 57\n    all_subjects_have_dif: true\n    mean_pct_c: 30.6\n    median_pct_c: 29.7\n    sd_pct_c: 5.5\n    range_pct_c:\n    - 20.7\n    - 48.4\n    top3_subjects:\n      business_ethics: 48.4\n      human_aging: 41.9\n      formal_logic: 40.4\n    bottom3_subjects:\n      computer_security: 20.7\n      marketing: 20.9\n      management: 21.7\n    domain_pct_c:\n      STEM: 30.9\n      Humanities: 31.1\n      Social_Science: 31.6\n    stem_vs_humanities_p: 0.611\n    kruskal_wallis_p: 0.78\n    logistic_regression:\n      difficulty_OR: 0.086\n      discrimination_OR: 57.2\n      pseudo_r2: 0.042\n    excess_dif_subjects:\n    - professional_law\n    - human_aging\n    - world_religions\n    - business_ethics\n    - professional_medicine\n    overall_pct_favor_2024: 43.9\n    temporal_asymmetry:\n      STEM_pct_favor_2024: 55.4\n      Humanities_pct_favor_2024: 35.6\n      Social_Science_pct_favor_2024: 42\n    unidirectional_subjects:\n      world_religions:\n        pct_favor_2024: 16.9\n      logical_fallacies:\n        pct_favor_2024: 20\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T14:34:28.365Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T14:34:28.365Z",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T14:34:28.387Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：核心张力未化解：reviewers同时认为(a) ρ=0.997说明DIF不影响rankings所以'so what'，AND (b) 31%可能是MH method artifact（unidimensional IRT misfit + LLM population不满足MH assumptions）。两个方向的attack形成pincer——instability要么不存在要么不重要。
核心假设：['至少1位reviewer认为ability confound decomposition (2.4pp)不够convincing——要求propensity-score matching或MIMIC model，而非简单NN matching', 'MH-DIF的unidimensional IRT假设被正面攻击——98% |Lz|>2的misfit数据被reviewer引用为evidence against method validity', 'Ground truth meta-critique被全部reviewers视为obvious或out-of-scope', "Semi-synthetic injection被视为artificial——'flipping incorrect→correct doesn't model real contamination mechanisms'", "ρ=0.997的ranking stability被视为evidence AGAINST the paper's importance而非FOR robustness", "6-benchmark replication中的C%变异(17.9-31.3%)被解读为'DIF is benchmark-dependent, not a universal phenomenon'", 'plan_029 permutation null成功但reviewer认为permutation不保留temporal structure，要求block permutation']
关键指标范围：{'reviewer_avg_score': [2.75, 3.25], 'permutation_null_mean_c_pct': [0.5, 2.0], 'permutation_null_p_value': [0.0, 0.05], 'rebuttal_issues_count': [5, 8], 'claims_accepted_without_caveat': [0, 1], 'page_compression_info_loss_pct': [15, 30], 'reviewers_questioning_method_validity': [2, 3]}
叙事方向：需要fundamental reframing，但不降级venue。新angle：从'DIF reveals instability'转向'DIF as stress test for benchmark measurement assumptions'——paper的贡献不再是'31% items are unstable'，而是'applying psychometric diagnostics to LLM benchmarks exposes that standard IRT assumptions (unidimensionality, local independence, temporal invariance) are systematically violated, and we characterize HOW they fail。' 具体操作：(1)将98% Lz misfit从limitation翻转为primary finding——MMLU fundamentally violates IRT assumptions，this itself is newsworthy；(2)将6-benchmark C%变异reframe为'benchmark-specific measurement properties'而非weakness；(3)将ρ=0.997 reframe为'massive redundancy in MMLU means 31% items can be removed without information loss——this is a finding about benchmark design efficiency'；(4)Semi-synthetic framework从validation tool降级为methodological appendix，主叙事转向empirical characterization。Claim 2 (meta-critique)从numbered contribution降为Discussion section observation。新headline：'Psychometric audit of 6 LLM benchmarks reveals systematic violations of measurement invariance assumptions——31% of MMLU items show temporal DIF, but ranking-irrelevant redundancy masks the instability.' 需要补充的实验：multidimensional IRT pilot（至少2-factor model on 5 subjects）作为rebuttal evidence或camera-ready addition。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen
venue: emnlp-2026
focus: This is re-dream #8 after major revisions addressing Dream #7's specific weaknesses. Key improvements since Dream #7 (all integrated into paper via P6-P16 patches):

1. **Actionability paradox SOLVED** (was CW1-level concern): NEW plan_032 DIF-cleaned MMLU demonstration shows 89.5% models shift ≥5 ranks, systematic cohort bias (2024 Δrank=+73.6), confirmed DIF-specific by random baseline (z=8.5). This directly answers "ρ=0.997 means DIF doesn't matter."

2. **Proposition 1 (ΔFPR=0 formalized)**: Cross-subject matching now has a formal algebraic proof, not just an empirical observation. Elevates methodological contribution.

3. **Temporal coarseness addressed**: NEW plan_031 6-month window robustness check (C%=34.35%, 181× enrichment) shows DIF is robust to finer temporal granularity.

4. **Subject DIF direction asymmetry** (NEW analytical finding): STEM subjects favor 2024 models (55.4%), Humanities favor 2023 (64.4%) — content-level predictor of DIF direction.

5. **Expanded Related Work**: Added BHI (Blebea et al. 2024), PSN-IRT (Polo et al. 2024), Maeda (2024) — addresses "thin related work" concern.

6. **Systematic Confound Elimination narrative**: 6 negative results reframed as systematic exclusion of confounds (architecture, ability, local dependence, IRT misfit, reasoning-RL, ensemble), strengthening the "what remains is genuine temporal DIF" argument.

7. **Bootstrap CI on headline C%**: MMLU C%=31.3% [29.5%, 33.1%] with N=1000 model resampling.

8. **Causal language softened** throughout — "contamination-adjacent" phrasing replaced with hedged "differential functioning" language.

9. **DIF-for-LLMs paragraph** added in Discussion — explicitly addresses what DIF means for machine (vs. human) examinees.

10. **Audit protocol expanded** with code release commitment.

11. **ConStat/DVD comparison visibility increased** — AUROC numbers and Jaccard overlap now in main text.

Reviewers should evaluate whether these revisions close the gap from 3.5 to 4.0 (Conference). The paper's strongest path to 4.0: unprecedented scale + cross-subject matching (Proposition 1) + Simpson's paradox + DIF-cleaned demonstration (actionability) + 6-benchmark replication + systematic confound elimination.

## paper_framing.md

# Paper Framing — irt_equated_bench_regen

## Target Venue
- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)
- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)

## Paper Type
Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."

## Core Claims (4 条, 可证伪)

**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)
- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.

**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)
- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection" — now with direct empirical evidence, not just conceptual argument

**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability

**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.
4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.
- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)
- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.
- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed

## Story Spine (v2 — no-pivot narrative)

**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.

**Key narrative principle**: "Instability ≠ invalidity." DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**

**What we find** (4 contributions, focused):

1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for "models got better."

2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.

3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.

4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).

**Headline result**: "Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance."

## Scope Control (main body vs appendix)

**MAIN BODY (4 claims + robustness)**:
- §1 Introduction (problem + "instability ≠ invalidity" framing upfront)
- §2 Related Work (45 papers, 5 clusters)
- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)
- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)
- §5 Discussion + Limitations
- §6 Conclusion

**APPENDIX (pruned from main body)**:
- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped
- RL robustness (plan_002) — N=13, underpowered
- Ensemble fusion (plan_003a/b/c) — negative, not executed
- Bifactor equating pilot — below target fit
- Item generation pilot — below benchmarks
- Graceful degradation — clean but supplementary
- Item-Focused Trees — robustness check, supplementary
- ConStat/DVD comparisons — complementary baselines

## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks

Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.

## Venue Fit

- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. "Empirical, not algorithmic" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.

## Novelty Articulation (三层，显式化)

MH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:

1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.

2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).

3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).

**Framing**: "We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm."

## Anticipated Reviewer Concerns (updated for pivot)

1. **"31% could just mean models got better / ability confound inflates C%"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.

2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.

3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.

4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.

5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.

6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.

7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.

8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.

9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: "our 31% uniform-only estimate is conservative."

10. **"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.

11. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.

## Dropped from Original Framing

- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."


## experiment_plan (with registry status)

- id: plan_001
  name: real_data_dif_mmlu
  claim: 1
  description: "Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\
    \ × 12,508 items). Data characteristics: only 37% models classifiable by family\
    \ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\
    \ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\
    \ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\
    \ split (ability-based grouping, uses all models) (c) Item filtering: run with\
    \ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\
    \ detection on all items under both cohort definitions. Proxy validation against\
    \ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\
    \ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\
    \ (item exists on web), while DIF detects cohort-differential contamination (item\
    \ behaves differently across temporal cohorts). Low concordance is EXPECTED —\
    \ DIF only catches items where contamination is differential across cohorts, not\
    \ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\
    \ items) rather than TPR (which conflates uniform vs differential contamination).\
    \ Unlabeled items (26.2%) reported separately as \"unknown\". plan_011 (semi-synthetic\
    \ injection) provides controlled ground truth to complement this proxy. (d) Within-family\
    \ confound control: run DIF within model families where both versions\n    have\
    \ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\n\
    \    below threshold — use as supplementary only. Identify additional qualifying\
    \ pairs from\n    METABENCH metadata. If DIF flags\n    items that are NOT differentially\
    \ contaminated within-family, the flag reflects capability\n    gain, not contamination.\
    \ Report: DIF flag overlap between cross-cohort and within-family\n    analyses\
    \ to disentangle contamination from capability improvement.\n(e) Domain-specificity\
    \ analysis: correlate DIF flags with MMLU subject categories to check\n    whether\
    \ flags cluster in domains with known capability jumps vs known contamination.\n\
    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\
    \ + within-family confound control + domain-specificity analysis.\n"
  priority: P0
  gpu_budget_hours: 0
  deps: []
  registry_id: ''
  status: planned
- id: plan_002
  name: rl_robustness_validation
  claim: 1
  description: "Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\
    \ - \"Alignment RL\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\
    \ produce\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\
    \ 477 such models.\n- \"Reasoning RL\" (GRPO/PPO online training) = the mechanism\
    \ that conceals contamination\n  signals. This is what Claim 1 targets. METABENCH\
    \ has almost none of these.\nDesign (Reviewer-validated): (a) SFT-only cohort\
    \ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\
    \ as mechanism control —\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\
    \ if DIF works on both\n    (a) and (b), robustness covers the full RL spectrum\n\
    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\n\
    \    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\n\
    \    (not a standalone group): DIF is group-level, so we verify that adding RL\
    \ models\n    to a cohort doesn't degrade detection. Separately, run traditional\
    \ detectors\n    (Min-K%, ConStat) on these 10-15 models individually to show\
    \ per-model degradation.\nTwo-level validation: - Group level: DIF flags same\
    \ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\
    \ detectors degrade on (c) individuals → fragile This design works even with only\
    \ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\
    \ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\
    \ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\
    \ test or permutation test for pairwise AUROC differences - TOST equivalence testing\
    \ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\
    \ exploitation power analysis: formally characterize DIF detection power as\n\
    \    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\
    \ answers\n    memorized items correctly with probability p, shrinking DIF effect\
    \ size by ~p.\n    Show detection boundary and ensemble coverage handoff point.\n"
  priority: P0
  gpu_budget_hours: 100
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_003a
  name: constat_perturbation_eval
  claim: 2
  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:
    (a) Generate semantically equivalent reformulations for 200+ MMLU items using
    LLM paraphrasing (b) Compare model performance on original vs reformulated items
    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection
    power by effect size — expected strength on non-RL models, weakness on RL Even
    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.

    '
  priority: P0
  gpu_budget_hours: 80
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_003b
  name: dvd_generation_variance_eval
  claim: 2
  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select
    10-15 open-weight models with inference access (b) Generate 50 responses per item
    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect
    bimodal distributions (contamination signal) (d) Characterize detection power
    for variant contamination vs verbatim contamination Standalone results provide
    variant-contamination detection baseline independent of DIF.

    '
  priority: P0
  gpu_budget_hours: 70
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_003c
  name: ensemble_fusion
  claim: 2
  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate
    per-signal thresholds on subset of items with known contamination status (b) Evaluate
    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:
    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision
    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion
    weights (5-fold); report uniform-weight baseline alongside optimized Depends on
    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  - plan_003a
  - plan_003b
  registry_id: ''
  status: planned
- id: plan_004
  name: cross_benchmark_gsm8k
  claim: 1
  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.
    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard
    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with
    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability
    and provides an independent ground truth beyond Li et al. proxy labels.

    '
  priority: P1
  gpu_budget_hours: 100
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_005
  name: bifactor_irt_equating_pilot
  claim: 3
  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains
    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt
    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files
    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH
    MMLU data (general factor + subject-specific factors) (b) Select anchor items
    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter
    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model
    rankings on original vs replaced benchmark should correlate at Spearman rho ≥
    0.95 after equating.

    '
  priority: P1
  gpu_budget_hours: 50
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_006
  name: item_generation_calibration
  claim: 3
  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use
    LLM generation with construct constraints (same subject, same cognitive level)
    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty
    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45
    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate
    on holdout model panel

    '
  priority: P1
  gpu_budget_hours: 200
  deps:
  - plan_005
  registry_id: ''
  status: planned
- id: plan_007
  name: cumulative_bayesian_dif
  claim: 1
  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).
    Simulate 4 successive benchmark administrations. Show power improvement from accumulating
    evidence: individual administration power ~0.40 → cumulative power ~0.70 after
    3 administrations for medium effects (δ=1.0).

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_008
  name: graceful_degradation_analysis
  claim: 3
  description: 'Formal analysis of benchmark validity under item replacement: (a)
    Define validity metrics (ranking stability, score reliability, construct coverage)
    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish
    theoretical bounds on validity degradation as function of replacement rate (d)
    Empirical validation using METABENCH data

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_005
  - plan_006
  registry_id: ''
  status: planned
- id: plan_009
  name: item_focused_trees
  claim: 1
  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative
    to categorical cohort DIF. Treat model release date as continuous covariate. Compare
    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary
    cohort splits, uses full model sample.

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_010
  name: architecture_stratified_dif
  claim: 1
  description: "Run DIF within architecture-homogeneous subpopulations to test whether\
    \ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\
    \ is removed. Dream worst-case identified this as the critical missing experiment.\
    \ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\
    \ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\
    \ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\n\
    \    vs full-population DIF from plan_001\n(d) If fit improves substantially,\
    \ conclusion is \"DIF requires architecture-homogeneous\n    populations\" — a\
    \ fixable constraint, not a fundamental limitation\nZero GPU cost (uses existing\
    \ METABENCH data). Proactive defense against worst-case reviewer concern about\
    \ unidimensional IRT misfit.\n"
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_011
  name: semi_synthetic_contamination_validation
  claim: 1
  description: "Inject known contamination into the real METABENCH response matrix\
    \ and measure DIF detection power under controlled ground truth. Addresses ground\
    \ truth circularity concern (Li et al. proxy labels measure existence, not differential\
    \ contamination). Design: (a) Select 500 items with known-clean status (no DIF\
    \ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\
    \ synthetic contamination:\n    flip responses of focal-group models from incorrect→correct\
    \ with probability p\n    (simulating contamination at varying exploitation rates)\n\
    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\
    \ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\n\
    \    (0.4-1.0), focal group size (N=40-200)\nProvides controlled ground truth\
    \ that proxy labels (Li et al.) and GSM1K cannot.\n"
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_028
  name: multi_benchmark_temporal_dif
  claim: 1,5
  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,
    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023
    vs 2024) on each. Addresses Dream #6 three-tier consensus: "only MMLU + GSM8K,
    generalizability insufficient." Report C% + sample sizes + random-split control
    for each benchmark.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_029
  name: permutation_null_c_rate
  claim: 1
  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels
    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes
    null distribution for C%. Dream #6 three-tier consensus: reviewers ask "is 31%
    above chance?" Current random-split control (0.18%) is within-cohort, not temporal
    permutation null.

    '
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_030
  name: odds_ratio_regression_transparency
  claim: 1
  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke
    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level
    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.
    Dream #6 two-tier concern.

    '
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned


## registry (completed experiments)

- exp_id: mvp_dif_power_sim
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_tpr_mh: 0.6817
    best_tpr_lr: 0.6869
    best_condition: N=100_delta=1.6
    best_auc_mh: 0.9393
    best_auc_lr: 0.9593
    pass_criterion_tpr_mh: 0.0416
    pass_criterion_tpr_lr: 0.0703
    pass_criterion_condition: N=50_delta=1.0
    verdict: FAIL
    all_fpr_below_015: true
- exp_id: mvp_dif_power_sim_phase2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ets_c_tpr_N80_d14: 0.6823
    ets_c_tpr_N80_d16: 0.7223
    ets_c_tpr_N100_d14: 0.7582
    ets_c_tpr_N100_d16: 0.7966
    ets_c_fpr_range: 0.036-0.042
    best_auc_mh: 0.9254
    best_auc_lr: 0.9405
    verdict: PASS
    pass_plus_met: true
    real_param_a_mean: 1.2
    real_param_b_mean: -0.84
- exp_id: plan_001_real_data_dif_mmlu
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    temporal_ets_c_pct: 31.3
    temporal_fpr_li_clean: 0.318
    temporal_enrichment: 0.96
    ability_ets_c_pct: 2.9
    ability_fpr_li_clean: 0.027
    ability_enrichment: 1.19
    within_family_llama2v3_c_pct: 61.3
    within_family_mistral_mixtral_c_pct: 38.7
    domain_spearman_rho: 0.307
    domain_spearman_p: 0.02
    sanity_random_split_c_pct: 0.18
    temporal_ability_jaccard: 0.014
- exp_id: plan_001b_matched_ability_dif
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: plan_011_semi_synthetic_validation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    temporal_external_tpr_p0: 0.326
    temporal_external_tpr_p03: 0.548
    temporal_external_tpr_p05: 0.834
    temporal_external_tpr_p07: 0.99
    temporal_external_tpr_p10: 1
    temporal_external_fpr: 0.314
    temporal_external_delta_tpr_p10: 0.674
    ability_external_tpr_p0: 0.498
    ability_external_tpr_p10: 0.8
    ability_external_fpr: 0.493
    ability_external_delta_tpr_p10: 0.302
    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0
    matching_variable_contamination_confirmed: true
    bug_fix: inf-delta classified as extreme DIF not class A
- exp_id: plan_012_irt_theta_conditioning
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    temporal_theta_qt20_fpr: 0.312
    temporal_theta_qt20_tpr_p05: 0.876
    temporal_theta_qt20_tpr_p10: 1
    temporal_external5_fpr: 0.314
    temporal_external5_tpr_p05: 0.834
    ability_theta_qt10_fpr: 0.093
    ability_theta_qt10_tpr_p05: 0.206
    ability_theta_qt10_tpr_p10: 0.544
    ability_theta_qt20_fpr: 0.079
    ability_theta_qt20_tpr_p05: 0.21
    ability_theta_qt20_tpr_p10: 0.544
    ability_external5_fpr: 0.493
    ability_external5_tpr_p05: 0.756
    theta_total_score_corr: 0.9986
    enrichment_all_variants: 0.97-1.00
    success_criterion_met: false
- exp_id: plan_013_q3_local_independence
  name: ''
  status: DONE
  conclusion: success
  metrics:
    within_subject_mean_q3: 0.0086
    cross_subject_mean_q3: 0.0031
    within_subject_pct_above_020: 11.3
    cross_subject_pct_above_020: 2.2
    mann_whitney_p: 2.29e-09
    worst_subject: moral_scenarios
    worst_subject_pct_above_020: 34.2
    n_items_retained: 12251
    n_items_filtered: 257
    subject_size_q3_corr: 0.2064
    subject_size_q3_p: 0.123
- exp_id: plan_014_within_subject_dif
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    business_ethics_within_c_pct: 45.2
    human_aging_within_c_pct: 33
    formal_logic_within_c_pct: 39.5
    professional_medicine_within_c_pct: 31.1
    high_school_statistics_within_c_pct: 42
    avg_within_subject_c_pct: 38.1
    avg_cross_subject_c_pct: 40.5
    avg_delta_within_vs_cross: -2.4
    sibtest_available: false
    r_available: false
    decision_zone: '>25% HIGH'
- exp_id: plan_015_bifactor_irt
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: plan_016_within_subject_semi_synthetic
  name: ''
  status: DONE
  conclusion: success
  metrics:
    within_matching:
      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)
      business_ethics_baseline_fpr: 0.563
      business_ethics_delta_tpr_p05: -0.078
      human_aging_baseline_fpr: 0.334
      human_aging_delta_tpr_p05: 0.385
      professional_medicine_baseline_fpr: 0.312
      professional_medicine_delta_tpr_p05: 0.327
      formal_logic_baseline_fpr: 0.409
      formal_logic_delta_tpr_p05: 0.457
      high_school_statistics_baseline_fpr: 0.407
      high_school_statistics_delta_tpr_p05: 0.194
      fpr_inflates_with_injection: true
      avg_fpr_inflation_p10: 0.186
    cross_matching:
      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,
        high_school_statistics)
      business_ethics_baseline_fpr: 0.533
      business_ethics_delta_tpr_p05: 0.056
      human_aging_baseline_fpr: 0.431
      human_aging_delta_tpr_p05: 0.375
      professional_medicine_baseline_fpr: 0.38
      professional_medicine_delta_tpr_p05: 0.38
      formal_logic_baseline_fpr: 0.402
      formal_logic_delta_tpr_p05: 0.543
      high_school_statistics_baseline_fpr: 0.335
      high_school_statistics_delta_tpr_p05: 0.433
      fpr_stable_across_injection: true
      delta_fpr_all_subjects: 0
    success_criterion_met: true
- exp_id: plan_017_downstream_impact
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n_dif_items: 3918
    n_stable_items: 8590
    dif_pct: 31.3
    rho_full_vs_stable_2023: 0.998851
    rho_full_vs_stable_2024: 0.997014
    rho_full_vs_stable_all: 0.996451
    shr_full: 0.9934
    shr_stable: 0.9919
    dif_vs_random_z_mean: -14.91
    dif_vs_random_all_21_conditions_significant: true
    dif_removal_MORE_disruptive_than_random: true
    cross_cohort_ratio_dif_vs_full: 1.0919
    cross_cohort_ratio_stable_vs_full: 0.9581
    top_beneficiaries: phi-3, llama-3 derivatives
    top_hurt: mistral merges, slerp models
    max_rank_change: 851
- exp_id: plan_004_gsm8k_cross_benchmark
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    step1_gsm8k_temporal_dif:
      n_items: 1319
      n_ref: 1017
      n_foc: 804
      standard_c_pct: 18.9
      external_c_pct: 47.4
      sanity_c_pct: 0.3
      standard_external_spearman: 0.926
    step2_semi_synthetic:
      standard_delta_tpr_p10: 0.818
      external_delta_tpr_p10: 0.517
    step3_gsm1k_correlation:
      n_models: 33
      n_dif_c_items: 249
      pearson_r: -0.478
      pearson_p: 0.005
      spearman_rho: -0.403
      spearman_p: 0.02
      partial_r_controlling_accuracy: -0.385
      partial_p: 0.027
      permutation_p: 0.014
      dif_c_favor_2024: 78
      dif_c_favor_2023: 171
      direction: NEGATIVE (opposite to contamination hypothesis)
      cook_d_max_model: Deepseek-math-7b-rl
      leave_one_out_r_range: -0.537 to -0.374
      robust: true
- exp_id: plan_027_temporal_overlap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cohort_2023_n: 1080
    cohort_2023_mean: 0.5814
    cohort_2023_sd: 0.1405
    cohort_2024_n: 807
    cohort_2024_mean: 0.6068
    cohort_2024_sd: 0.1556
    cohens_d: -0.173
    overlap_coefficient: 0.764
    bhattacharyya: 0.961
    full_c_pct: 31.3
    score_range_overlap_c_pct: 30.9
    nn_matched_c_pct_mean: 28.9
    nn_matched_c_pct_sd: 0.1
    nn_matched_n_per_group: 638
    nn_matched_d: -0.01
    ability_confound_pp: 2.4
    ability_confound_pct_of_total: 7.7
    llama_comparison_d: -0.99
    llama_comparison_overlap: 0.18
    llama_matched_c_pct: 28.3
- exp_id: plan_030_odds_ratio
  name: ''
  status: DONE
  conclusion: success
  metrics:
    model1_domain_delta:
      mcfadden_r2: 0.0007
      nagelkerke_r2: 0.0012
      aic: 15545.2
      subject_acc_delta_or: 80.86
      subject_acc_delta_or_per_010: 1.55
      subject_acc_delta_or_ci_per_010:
      - 1.19
      - 2.03
    model2_domain_delta_plus_items:
      mcfadden_r2: 0.0423
      nagelkerke_r2: 0.072
      aic: 14902.3
      subject_acc_delta_or_per_010: 0.73
      ctt_difficulty_or_per_010: 0.78
      ctt_discrimination_or_per_010: 1.51
    model3_item_delta:
      mcfadden_r2: 0.0012
      nagelkerke_r2: 0.0021
      aic: 15536.9
      item_acc_change_or: 2.11
      item_acc_change_or_per_010: 1.08
      item_acc_change_ci:
      - 1.51
      - 2.96
    model4_item_delta_plus_items:
      mcfadden_r2: 0.0434
      nagelkerke_r2: 0.0737
      aic: 14885.4
      item_acc_change_or_per_010: 0.92
      ctt_difficulty_or_per_010: 0.77
      ctt_discrimination_or_per_010: 1.54
    simpsons_paradox: true
    lr_test_m1_vs_m2_chi2: 646.98
    lr_test_m3_vs_m4_chi2: 655.53
    best_model: Model 4 (item Δ + item props)
- exp_id: plan_028_multi_bench_dif
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      n_items: 12508
      n_ref: 1080
      n_foc: 807
      pct_c: 31.3
      random_pct_c: 0.18
      bootstrap_ci_95:
      - 29.38
      - 38.05
      bootstrap_mean: 33.14
      bootstrap_sd: 2.3
      bootstrap_n: 1000
    winogrande:
      n_items: 1267
      n_ref: 1017
      n_foc: 803
      pct_c: 30.3
      random_pct_c: 0.32
    truthfulqa:
      n_items: 817
      n_ref: 1080
      n_foc: 807
      pct_c: 29.7
      random_pct_c: 0.37
    arc:
      n_items: 1172
      n_ref: 1080
      n_foc: 807
      pct_c: 26.9
      random_pct_c: 0.6
    gsm8k:
      n_items: 1319
      n_ref: 1017
      n_foc: 804
      pct_c: 18.9
      random_pct_c: 0.3
    hellaswag:
      n_items: 10042
      n_ref: 1080
      n_foc: 807
      pct_c: 17.9
      random_pct_c: 0.28
    cross_benchmark_range: 17.9-31.3%
    all_random_controls_below_1pct: true
    min_enrichment_ratio: 45
    n_benchmarks: 6
- exp_id: plan_031_temporal_granularity
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_full_year:
      comparison: 2023 vs 2024
      distance_yr: 1
      n_ref: 1080
      n_foc: 807
      pct_c: 31.32
      random_pct_c: 0.02
    mmlu_half_year:
      comparison: 2023-H2 vs 2024-H1
      distance_yr: 0.5
      n_ref: 1018
      n_foc: 807
      pct_c: 34.35
      random_pct_c: 0.19
    mmlu_within_2023:
      comparison: 2023-H1 vs 2023-H2
      distance_yr: 0.5
      n_ref: 62
      n_foc: 1018
      pct_c: 22.62
      random_pct_c: 0.18
      supplementary: true
    cross_bench_half_year:
      arc_pct_c: 29.27
      hellaswag_pct_c: 18.07
      winogrande_pct_c: 33.62
      truthfulqa_pct_c: 31.33
    cross_bench_full_year:
      arc_pct_c: 26.88
      hellaswag_pct_c: 17.89
      winogrande_pct_c: 30.31
      truthfulqa_pct_c: 29.74
    half_year_gt_full_year_all_benchmarks: true
    dif_saturates_within_6mo: true
- exp_id: plan_032_dif_cleaned_mmlu
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_items_full: 12508
    n_items_cleaned: 8590
    n_items_removed: 3918
    pct_removed: 31.3
    spearman_rho: 0.9965
    rank_change_std: 127.1
    rank_change_min: -589
    rank_change_max: 849
    pct_change_ge5: 89.5
    pct_change_ge10: 79.5
    pct_change_ge20: 66.4
    pct_change_ge50: 41.9
    pct_change_ge100: 24.8
    top100_pct_ge10: 18
    top500_pct_ge10: 47.2
    cohort_2023_mean_change: -22.56
    cohort_2023_median_change: -5
    cohort_2024_mean_change: 73.6
    cohort_2024_median_change: 11
    systematic_bias: DIF items favor 2024 models; cleaning hurts 2024 +73.6 avg, helps
      2023 -22.6 avg
    top_hurt_families:
      phi-3: 258.35
      command-r: 235
      solar: 149.15
      llama-3: 120.86
    top_benefit_families:
      mistral-0.1: -60.32
      mistral: -53.27
      zephyr: -29.94
      gemma-2: -28.78
    removed_items_harder: true
    removed_mean_difficulty: 0.409
    cleaned_mean_difficulty: 0.46
    random_baseline_20trials:
      rank_change_std:
        mean: 60.2
        std: 7.8
      mean_abs_rank_change:
        mean: 36
        std: 3.6
      pct_change_ge100:
        mean: 8.5
        std: 2
      cohort_2023_mean_change:
        mean: 0.4
        std: 4.1
      cohort_2024_mean_change:
        mean: 2.8
        std: 21.2
    dif_vs_random_z_scores:
      rank_change_std_z: 8.5
      mean_abs_change_z: 10.7
      pct_ge100_z: 8.2
      cohort_2023_z: -5.6
      cohort_2024_z: 3.3
      cohort_asymmetry_gap_z: 4.4
- exp_id: plan_033_subject_dif_concentration
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_subjects: 57
    all_subjects_have_dif: true
    mean_pct_c: 30.6
    median_pct_c: 29.7
    sd_pct_c: 5.5
    range_pct_c:
    - 20.7
    - 48.4
    top3_subjects:
      business_ethics: 48.4
      human_aging: 41.9
      formal_logic: 40.4
    bottom3_subjects:
      computer_security: 20.7
      marketing: 20.9
      management: 21.7
    domain_pct_c:
      STEM: 30.9
      Humanities: 31.1
      Social_Science: 31.6
    stem_vs_humanities_p: 0.611
    kruskal_wallis_p: 0.78
    logistic_regression:
      difficulty_OR: 0.086
      discrimination_OR: 57.2
      pseudo_r2: 0.042
    excess_dif_subjects:
    - professional_law
    - human_aging
    - world_religions
    - business_ethics
    - professional_medicine
    overall_pct_favor_2024: 43.9
    temporal_asymmetry:
      STEM_pct_favor_2024: 55.4
      Humanities_pct_favor_2024: 35.6
      Social_Science_pct_favor_2024: 42
    unidirectional_subjects:
      world_religions:
        pct_favor_2024: 16.9
      logical_fallacies:
        pct_favor_2024: 20

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
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


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a0a445c0-2517-4cf2-af28-3c832fdb3ca7",
  "type": "user",
  "uuid": "7b25e76f-eb39-4c2d-84a5-1e1257ee89f8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T14:34:28.385Z_

```json
{
  "parentUuid": "7b25e76f-eb39-4c2d-84a5-1e1257ee89f8",
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
  "uuid": "cff41ec3-5606-45dc-851c-37cac348f877",
  "timestamp": "2026-05-21T14:34:28.385Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T14:34:28.385Z_

```json
{
  "parentUuid": "cff41ec3-5606-45dc-851c-37cac348f877",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "37baef57-9da8-4aeb-be74-dfe7e353cd88",
  "timestamp": "2026-05-21T14:34:28.385Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心张力未化解：reviewers同时认为(a) ρ=0.997说明DIF不影响rankings所以'so what'，AND (b) 31%可能是MH method artifact（unidimensional IRT misfit + LLM population不满足MH assumptions）。…",
  "leafUuid": "37baef57-9da8-4aeb-be74-dfe7e353cd88",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric audit of LLM benchmarks via DIF analysis",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e"
}
```

---

### Assistant

_source line 8 · 2026-05-21T14:35:35.555Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "worst" tier scenario. I need to look at which experiments have status "planned" and generate detailed predictions for each.

Let me identify the planned experiments:

1. plan_001 - real_data_dif_mmlu - status: planned (BUT it's also in registry as DONE with exp_id plan_001_real_data_dif_mmlu). Wait, let me re-read. The experiment_plan shows status: planned for all entries. 

So I need to cross-reference with the registry to see which ones are actually still planned versus already executed. Looking at the registry, plan_001 and plan_004 are marked as DONE, plan_005 shows as killed, but plan_002, plan_003a, plan_003b, and plan_003c don't appear in the registry yet, so those are the truly planned experiments I need to generate predictions for. I'm scanning through the planned experiments that haven't been executed yet—there's a cluster of validation and robustness checks, some perturbation and ensemble approaches, and several DIF-focused analyses. I notice plan_005 (bifactor_irt_equating_pilot) and plan_015 in the registry might be related or duplicative, though they have different IDs and statuses.

Looking at plan_010 more carefully—it's not explicitly in the registry, but the paper_framing references it with specific results ("99.98% decoder-only, C% unchanged, Jaccard=1.0"), which suggests it may have been completed but not properly logged. I'm realizing the user's actual request is asking for detailed data predictions for each planned experiment in the experiment_plan list, and since all entries there are marked as "planned," they likely want forecasts for the entire set.

The confusion is that many of these experiments already have actual results in the registry, so generating predictions for completed work seems redundant. But re-reading the request more carefully—they're asking for predictions with result_rationale for each planned experiment—I think they want me to generate worst-case scenario predictions for all experiments listed in the plan, regardless of whether some have already been executed. I'm working through the worst-case predictions for each experiment: plan_001 already has results but reviewers might dismiss the 31.3% finding as an artifact of the methodology, plan_002 needs predictions showing that the small RL sample size causes DIF detection to be unstable and fails to demonstrate advantage over traditional methods, plan_003a predicts ConStat outperforming DIF and making it look unnecessary, and plan_003b is still being evaluated for its worst-case scenario.

Moving through the rest, plan_003c depends on the prior two and risks showing minimal incremental value from DIF in an ensemble, plan_004 already has problematic results with the negative correlation on GSM1K, plan_005 faces convergence or fit issues with the bifactor model, plan_006 could suffer from poor calibration in generated items, plan_007risks being dismissed as purely simulation-based without empirical grounding, and plan_008 is examining what happens when models are progressively replaced.

Plan_009 might reveal that DIF is smoothly distributed rather than categorical, plan_010 is marked as done in the paper but missing from the registry with the risk that decoder-only architectures are too homogeneous to control for, plan_011 already completed but the injection mechanism could be seen as artificial, plan_028 is done but the wide variation in C% across benchmarks might be interpreted as benchmark-dependent rather than fundamental, and plan_029 hasn't been executed yet with the concern that even if permutation testing shows low null rates, reviewers might argue it doesn't preserve temporal structure.

Now I'm structuring the worst-case tier predictions systematically. The core vulnerabilities are that the high correlation might suggest DIF doesn't meaningfully affect rankings, the 31% effect could be an artifact of the MH method's assumptions not holding for LLM populations, and the instability findings could be dismissed as either nonexistent or inconsequential. Let me work through the YAML output with detailed worst-case rationales for each experiment. Generating YAML predictions...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37baef57-9da8-4aeb-be74-dfe7e353cd88",
  "isSidechain": false,
  "requestId": "req_011CbFsz2BPiLiPHkRVoz7Ds",
  "type": "assistant",
  "uuid": "07c0d909-7da2-4962-b7fb-17acc0708eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qBoGABFANbeQWi8dLLZuh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23247,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16999,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16999,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23247
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

_source line 9 · 2026-05-21T14:40:40.926Z_

```yaml
tier: worst
narrative_guidance: >
  核心张力未化解。Reviewers形成pincer attack：(a) ρ=0.997说明DIF不影响rankings→'so what'；
  (b) 31%可能是MH method artifact（unidimensional IRT misfit + LLM population违反MH assumptions）。
  需要fundamental reframing：从'DIF reveals instability'转向'DIF as stress test for benchmark
  measurement assumptions'。98% Lz misfit翻转为primary finding；C%变异reframe为benchmark-specific
  measurement properties；ρ=0.997 reframe为massive redundancy finding；semi-synthetic降级为
  methodological appendix。新headline：psychometric audit reveals systematic violations of
  measurement invariance assumptions。补充实验：multidimensional IRT pilot（至少2-factor model）。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: "METABENCH MMLU 5219×12508 response matrix上的MH-DIF分析，temporal cohort (2023 vs 2024-H1)，含within-family confound control和domain-specificity分析"
    expected_results:
      temporal_ets_c_pct: 31.3
      temporal_fpr_li_clean: 0.318
      temporal_enrichment: 0.96
      ability_ets_c_pct: 2.9
      ability_enrichment: 1.19
      within_family_llama2v3_c_pct: 61.3
      within_family_mistral_mixtral_c_pct: 38.7
      domain_spearman_rho: 0.307
      domain_spearman_p: 0.02
      sanity_random_split_c_pct: 0.18
      temporal_ability_jaccard: 0.014
      lz_misfit_pct_above_2: 98.0
      reviewer_avg_score_impact: -0.5
    result_rationale: >
      31.3% C%本身是solid empirical finding，random split control (0.18%)确认非统计噪声。
      但在worst档，reviewers攻击三个方向：(1) enrichment=0.96意味着DIF flags与web-overlap labels
      几乎正交——reviewer解读为"DIF没检测到任何已知contamination"而非"labels不匹配"；
      (2) 98% |Lz|>2表明unidimensional IRT对MMLU fundamentally misspecified，MH-DIF依赖
      IRT conditioning变量的validity，而conditioning变量本身就有问题——reviewer引用此数据
      作为method validity的反面证据；(3) within-family Llama-2v3 C%=61.3%远高于temporal 31.3%，
      reviewer认为这暴露了ability confound——能力差距越大DIF越高，temporal DIF可能只是residual
      ability confound。domain ρ=0.307 (p=0.02)进一步给reviewer ammunition——存在系统性的
      "模型变好→DIF升高"的生态学相关，尽管item-level decomposition只解释7.6%，但reviewer
      不信任decomposition方法本身。
    tables:
      - name: "Table 1: Temporal DIF Summary"
        columns: [cohort_definition, N_ref, N_foc, C_pct, random_control_pct, enrichment_vs_li]
        rows:
          - [temporal_2023v2024, 1253, 656, 31.3, 0.18, 0.96]
          - [ability_quintile, 2610, 2610, 2.9, 0.18, 1.19]
          - [within_family_llama, 161, 308, 61.3, "—", "—"]
          - [within_family_mistral, 106, 84, 38.7, "—", "—"]
      - name: "Table 2: Domain-specificity (top/bottom 5 subjects)"
        columns: [subject, C_pct, n_items, domain_acc_delta]
        rows:
          - [business_ethics, 48.4, 100, 0.12]
          - [human_aging, 41.9, 223, 0.09]
          - [formal_logic, 40.4, 126, 0.07]
          - [computer_security, 20.7, 100, 0.11]
          - [marketing, 20.9, 234, 0.06]
    figures_description:
      - "Figure 1: MMLU C% histogram (12,508 items) showing bimodal |Δ_MH| distribution with 31.3% exceeding ETS C threshold. Reviewer注意到distribution右尾的heavy tail——可能暗示小部分items有extreme DIF而非widespread instability"
      - "Figure 2: Domain-specificity scatter (57 subjects): C% vs domain accuracy improvement (ρ=0.307). Reviewer圈出右上象限——高improvement+高DIF subjects作为ability confound evidence"
    analysis: >
      Worst-case reviewer解读：(1) temporal enrichment=0.96被视为validation failure——
      "your method doesn't detect known contamination"；(2) 98% Lz misfit被正面引用为
      "MH-DIF在MMLU上的assumptions全部violated"；(3) within-family C%=61.3%被解读为
      "DIF is just detecting ability differences, not item instability"。需要proactive
      reframing：Lz misfit本身就是newsworthy finding，enrichment=0.96是expected而非failure，
      within-family结果motivates MIMIC model future work。至少1位reviewer会要求propensity-score
      matching或MIMIC model替代简单NN matching。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: "RL robustness验证：SFT-only baseline + alignment-RL (DPO/ORPO N=477) + reasoning-RL (GRPO/PPO 10-15 models) 三组比较"
    expected_results:
      n_reasoning_rl_models: 13
      sft_only_c_pct: 30.8
      alignment_rl_c_pct: 32.1
      reasoning_rl_added_c_pct: 31.5
      jaccard_sft_vs_alignment: 0.82
      jaccard_sft_vs_reasoning_added: 0.79
      delong_p_dif_vs_constat: 0.23
      constat_auroc_sft: 0.71
      constat_auroc_reasoning_rl: 0.43
      dif_auroc_sft: 0.62
      dif_auroc_reasoning_rl: 0.58
      tost_equivalence_p: 0.15
      bootstrap_ci_auroc_diff: [-0.08, 0.16]
      power_analysis_delta_boundary: 1.2
      reviewer_verdict: "underpowered and unconvincing"
    result_rationale: >
      N=13 reasoning-RL models是致命弱点。在worst档，reviewer直接dismiss整个实验为underpowered：
      (1) 13个reasoning-RL models加入focal cohort (N=656+13=669)几乎不改变C%——从31.3%到31.5%，
      但reviewer指出这说明的不是robustness而是13个models在N=669中统计上invisible；
      (2) TOST equivalence test p=0.15 fail to reject non-equivalence——reviewer得出"你
      无法证明DIF对reasoning-RL robust"；(3) traditional detectors (ConStat)在reasoning-RL
      上确实降级(AUROC 0.71→0.43)，但DIF本身也降级(0.62→0.58)，DeLong test p=0.23
      non-significant——reviewer说"没有evidence DIF比alternatives更robust"；(4) power
      analysis显示detection boundary在δ=1.2，比operational region (δ≥1.4)低，但reviewer
      认为这只是theoretical guarantee，实际数据上没验证。整个plan_002被reviewer一致要求
      从main claims中删除或降级到future work。
    tables:
      - name: "Table: RL Robustness Comparison"
        columns: [cohort, N, C_pct, AUROC_DIF, AUROC_ConStat, AUROC_MinKpp]
        rows:
          - [SFT_only, 412, 30.8, 0.62, 0.71, 0.65]
          - [Alignment_RL, 477, 32.1, 0.61, 0.68, 0.63]
          - ["+Reasoning_RL", 13, 31.5, 0.58, 0.43, 0.41]
    figures_description:
      - "Figure: DIF detection power curve as function of exploitation rate p, with N=13 reasoning-RL overlay showing wide CIs that overlap with zero improvement region"
    analysis: >
      Experiment致命缺陷是sample size。METABENCH中reasoning-RL models太少(13)，无法做
      meaningful group-level比较。Even if DIF flags不变，reviewer legitimately argues
      这是statistical insensitivity而非robustness。推荐：(1)降级为limitations section
      disclosure；(2)如果能获取更多reasoning-RL model responses (N≥50)则有rebuttal价值；
      (3)reframe为"alignment-RL robustness"(N=477足够)而非"reasoning-RL robustness"。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: "ConStat-style perturbation testing独立评估：200+ MMLU items的语义等价reformulation，比较original vs reformulated performance"
    expected_results:
      n_items_reformulated: 220
      constat_detection_rate: 0.38
      constat_fdr_controlled_rate: 0.29
      constat_auroc_vs_li_labels: 0.61
      dif_auroc_vs_li_labels: 0.52
      constat_detects_dif_misses: 47
      dif_detects_constat_misses: 31
      jaccard_dif_constat: 0.18
      constat_fpr: 0.12
      constat_correlation_with_dif_delta_mh: 0.15
      reviewer_interpretation: "ConStat is complementary but outperforms DIF on per-model detection"
    result_rationale: >
      在worst档，ConStat表现decent (AUROC=0.61 vs DIF 0.52 against Li labels)，reviewer
      用此攻击DIF的utility："为什么不直接用ConStat？它不需要temporal cohorts，不依赖
      unidimensional IRT，且AUROC更高。" 关键问题：(1) ConStat是per-model detector而DIF
      是group-level——conceptually不同，但reviewer不care about conceptual distinction，
      只看performance numbers；(2) Jaccard=0.18意味着两种方法检测的items高度不重叠，
      本应是complementarity argument，但reviewer解读为"DIF检测的instability与ConStat
      检测的contamination无关——进一步说明DIF检测的不是contamination而是IRT misfit artifact"；
      (3) ConStat FPR=0.12低于DIF的implicit ~0.31 FPR (against Li clean items)，reviewer
      认为DIF over-flags。ConStat的成功paradoxically undermines DIF narrative。
    tables:
      - name: "Table: ConStat vs DIF Detection Comparison"
        columns: [method, AUROC_vs_Li, FPR, detection_rate, items_unique]
        rows:
          - [ConStat, 0.61, 0.12, 0.29, 47]
          - [DIF_MH, 0.52, 0.31, 0.31, 31]
          - [overlap, "—", "—", "—", "Jaccard=0.18"]
    figures_description:
      - "Figure: Venn diagram of ConStat vs DIF flagged items showing low overlap (Jaccard=0.18), with reviewer annotation 'DIF captures something different from contamination'"
    analysis: >
      ConStat结果在worst档是double-edged：complementarity客观上支持ensemble argument，
      但reviewer weapon化低overlap来argue DIF不检测contamination。需要reframing：
      ConStat和DIF检测不同construct (perturbation sensitivity vs temporal differential
      functioning)，低overlap是expected。但在worst档这个argument不被接受。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: "DVD generation variance独立评估：10-15 open-weight models × 50 responses/item via temperature sampling"
    expected_results:
      n_models_tested: 12
      n_items_scored: 500
      dvd_detection_rate: 0.22
      dvd_bimodal_items: 34
      dvd_auroc_vs_li: 0.58
      dvd_fpr: 0.08
      dvd_detects_variant_contamination: true
      dif_misses_variant_items: 28
      dvd_misses_verbatim_items: 41
      correlation_dvd_dif: 0.09
      reviewer_interpretation: "DVD captures a contamination mode DIF completely misses"
    result_rationale: >
      DVD在worst档表现modest (AUROC=0.58)但暴露DIF的structural blind spot：variant
      contamination。(1) 34个bimodal-distribution items中28个(82%)被DIF missed——reviewer
      argues DIF只能检测verbatim memorization的differential效应，对paraphrase/variant
      contamination完全blind；(2) DVD和DIF的correlation=0.09几乎正交——reviewer interprets
      this as "DIF measures something orthogonal to contamination"；(3) DVD的FPR=0.08
      远低于DIF的implicit FPR，进一步支持"DIF over-flags"叙事。DVD的per-model nature
      也means reviewer质疑为什么需要group-level DIF when per-model methods exist。
      关键攻击：如果contamination是variant而非verbatim（increasingly likely with
      reasoning-RL models），DIF fundamentally无法检测。
    tables:
      - name: "Table: DVD Detection Results"
        columns: [contamination_mode, n_items, dvd_detected, dif_detected, both_detected]
        rows:
          - [bimodal_variant, 34, 28, 6, 4]
          - [high_variance, 78, 45, 22, 12]
          - [normal, 388, 31, 125, 18]
    figures_description:
      - "Figure: Generation variance distributions for 3 example items — one clean, one verbatim-contaminated (DIF catches, DVD misses), one variant-contaminated (DVD catches, DIF misses)"
    analysis: >
      DVD暴露DIF对variant contamination的blind spot。在worst档这被reviewer elevation
      为fundamental limitation："随着models increasingly使用paraphrase training data，
      DIF的检测能力将progressive降低。" 需要honest acknowledgment在limitations中。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: "DIF + ConStat + DVD三信号融合：calibrated thresholds, majority voting, weighted fusion"
    expected_results:
      ensemble_auroc_majority: 0.64
      ensemble_auroc_weighted: 0.67
      ensemble_fpr: 0.09
      dif_only_auroc: 0.52
      constat_only_auroc: 0.61
      dvd_only_auroc: 0.58
      dif_incremental_auroc_over_constat_dvd: 0.02
      cross_val_weight_dif: 0.21
      cross_val_weight_constat: 0.45
      cross_val_weight_dvd: 0.34
      uniform_weight_auroc: 0.63
      reviewer_interpretation: "DIF adds minimal value to ensemble; ConStat carries the weight"
    result_rationale: >
      在worst档，ensemble是functional但DIF的contribution marginal：cross-validated
      weights分配给DIF仅0.21 (vs ConStat 0.45, DVD 0.34)，DIF incremental AUROC仅+0.02
      over ConStat+DVD two-signal baseline。Reviewer解读：(1) "DIF的unique contribution
      几乎可以忽略——remove it from ensemble, AUROC drops from 0.67 to 0.65"；(2) ensemble
      本身AUROC=0.67不够impressive——reviewer认为"moderate detection power after fusing
      three independent signals suggests all three are weak detectors"；(3) DIF的
      group-level nature限制了它在ensemble中的utility——ConStat和DVD都是per-model，
      DIF只能提供item-level flags without model specificity。Ensemble claim从numbered
      contribution降级为appendix material。
    tables:
      - name: "Table: Ensemble Ablation"
        columns: [configuration, AUROC, FPR, weight_DIF, weight_ConStat, weight_DVD]
        rows:
          - [DIF_only, 0.52, 0.31, 1.0, 0, 0]
          - [ConStat_only, 0.61, 0.12, 0, 1.0, 0]
          - [DVD_only, 0.58, 0.08, 0, 0, 1.0]
          - [ConStat+DVD, 0.65, 0.10, 0, 0.57, 0.43]
          - [Full_ensemble_weighted, 0.67, 0.09, 0.21, 0.45, 0.34]
          - [Full_ensemble_majority, 0.64, 0.09, "—", "—", "—"]
    figures_description:
      - "Figure: ROC curves for individual detectors and ensembles, showing DIF curve substantially below ConStat and DVD"
    analysis: >
      Ensemble结果对paper有两面性：functional ensemble存在但DIF是weakest signal。
      在worst档，reviewer用ensemble weights作为quantitative evidence that DIF adds
      little value。推荐：不作为numbered contribution，降级为Discussion section observation。
      Paper价值需要从detection转向measurement characterization。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: "GSM8K DIF复制 + GSM1K ground truth correlation + semi-synthetic framework portability验证"
    expected_results:
      gsm8k_temporal_c_pct: 18.9
      gsm8k_sanity_c_pct: 0.3
      semi_synthetic_delta_tpr_p10: 0.818
      gsm1k_pearson_r: -0.478
      gsm1k_spearman_rho: -0.403
      gsm1k_n_models: 33
      gsm1k_partial_r: -0.385
      gsm1k_direction: NEGATIVE
      gsm1k_ci_upper_pearson: -0.16
      gsm1k_ci_upper_spearman: -0.031
      cook_d_outlier: Deepseek-math-7b-rl
      reviewer_interpretation: "anti-correlation falsifies contamination detection claim"
    result_rationale: >
      GSM1K correlation是worst档的primary ammunition之一。r=-0.478 (NEGATIVE)意味着
      DIF flags更多的models有SMALLER GSM8K-GSM1K gap——与contamination hypothesis完全相反。
      Reviewer攻击：(1) "如果DIF检测contamination，DIF-flagged items应该在contaminated
      models上表现异常好→positive correlation。Negative correlation意味着DIF检测的是
      capability improvement而非contamination"；(2) N=33 with CI upper bound |r|=0.16
      for Pearson, |ρ|=0.031 for Spearman——"effect可能接近zero"；(3) Deepseek-math-7b-rl
      是outlier (Cook's d最高)——一个reasoning-RL model driving the correlation，
      "remove it and see what happens"。Semi-synthetic ΔTPR=0.818是strong但reviewer
      dismisses为artificial。GSM8K C%=18.9%低于MMLU 31.3%，reviewer用此argue
      "DIF是benchmark-dependent而非universal"。
    tables:
      - name: "Table: GSM8K Replication Summary"
        columns: [metric, value, interpretation]
        rows:
          - [temporal_C_pct, 18.9, "lower than MMLU (31.3%), benchmark-dependent"]
          - [semi_synthetic_ΔTPR, 0.818, "strong but artificial injection"]
          - [GSM1K_r, -0.478, "NEGATIVE — opposes contamination hypothesis"]
          - [GSM1K_N, 33, "small sample, wide CIs"]
          - [GSM1K_CI_upper_rho, -0.031, "near zero possible"]
    figures_description:
      - "Figure: Scatter plot of DIF C-item count vs GSM8K-GSM1K gap for 33 models, showing negative trend with Deepseek-math-7b-rl as visible outlier"
    analysis: >
      Anti-correlation是worst档的lethal finding。需要explicit reframing：GSM1K gap
      measures contamination BENEFIT (总分差)，而DIF measures item-level DIFFERENTIAL
      functioning (conditioning on ability)——负相关说明DIF items是high-ability models
      表现不成比例好的items，not contamination indicators。但这个argument复杂且
      counter-intuitive，reviewer在worst档不会接受。推荐：demote to exploratory。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: "Bifactor IRT equating pilot：general factor + 57 subject-specific factors，anchor item selection，fixed-parameter calibration"
    expected_results:
      bifactor_converged: false
      n_iterations_before_failure: 2000
      rmsea: 0.089
      cfi: 0.72
      tli: 0.68
      general_factor_variance_explained: 0.31
      subject_factors_variance_explained: 0.42
      residual_variance: 0.27
      anchor_items_selected: 0
      equating_score_rho: null
      reviewer_interpretation: "bifactor doesn't converge, IRT equating infeasible"
    result_rationale: >
      57-subject MMLU的bifactor model在worst档不收敛或者fit极差。原因：(1) 12,508 items ×
      58 factors (1 general + 57 specific)——参数空间巨大，5219个models不足以稳定估计；
      (2) RMSEA=0.089 > 0.06 threshold, CFI=0.72 < 0.90 threshold——model fit rejected
      by all standard criteria；(3) general factor只解释31% variance——MMLU inherently
      multidimensional但不是bifactor structure，可能需要更complex latent structure
      (exploratory factor analysis suggests 8-12 factors, not 57)；(4) 因为model fit差，
      anchor item selection没有principled basis——所有items在misspecified model下的
      parameters不可信。Reviewer在worst档将此结果作为"unidimensional IRT assumptions
      violated"的additional evidence，同时argue bifactor也不work→"the entire IRT-based
      approach is inappropriate for MMLU"。Equating pilot killed。
    tables:
      - name: "Table: Bifactor IRT Fit Indices"
        columns: [index, value, threshold, verdict]
        rows:
          - [RMSEA, 0.089, "<0.06", FAIL]
          - [CFI, 0.72, ">0.90", FAIL]
          - [TLI, 0.68, ">0.90", FAIL]
          - [SRMR, 0.11, "<0.08", FAIL]
          - [general_factor_pct, 31, ">50", FAIL]
    figures_description:
      - "Figure: Scree plot showing eigenvalue decay — first eigenvalue dominant but 57-factor structure not supported; elbow suggests 8-12 latent dimensions"
    analysis: >
      Bifactor failure在worst档strengthen reviewer的"IRT is wrong framework for LLM
      benchmarks" argument。但可以翻转为positive finding：MMLU的latent structure is
      NOT bifactor, NOT unidimensional——this characterization itself is contribution。
      推荐：report as evidence for multidimensional IRT future work necessity。

  - name: item_generation_calibration
    plan_id: plan_006
    description: "DIF-flagged items的replacement generation：LLM generation + student simulation calibration + holdout validation"
    expected_results:
      n_items_generated: 150
      difficulty_correlation_prompt: 0.18
      difficulty_correlation_calibrated: 0.52
      discrimination_correlation: 0.31
      construct_coverage_pct: 68
      holdout_ranking_rho: 0.91
      target_rho: 0.95
      target_met: false
      generated_item_dif_rate: 0.22
      reviewer_interpretation: "replacement items themselves show DIF, circularity"
    result_rationale: >
      Item generation在worst档fails target (ρ=0.91 < 0.95)且暴露circularity问题：
      (1) prompt-based difficulty targeting ρ=0.18 confirms literature finding (0.10-0.45)
      ——LLMs不能reliably控制item difficulty；(2) student simulation calibration提升到
      ρ=0.52但still insufficient——说明difficulty estimation技术不够mature；(3) generated
      replacement items themselves有22% DIF rate——reviewer argues "如果replacement items
      也有DIF，replacement不解决问题，只是shifting instability"；(4) construct coverage
      68%意味着32% of original construct space被generation miss——ρ=0.91可能反映
      narrower construct而非equivalent measurement。Target not met导致Claim 3 (regeneration)
      完全unsupported。在worst档，reviewer将此结果与bifactor failure一起cite为
      "equating pipeline全链条都fail——从IRT fit到anchor selection到item generation"。
    tables:
      - name: "Table: Item Generation Calibration"
        columns: [method, difficulty_rho, discrimination_rho, construct_coverage]
        rows:
          - [prompt_only, 0.18, 0.12, 0.45]
          - [student_sim, 0.52, 0.31, 0.68]
          - [target, ">0.70", ">0.50", ">0.85"]
    figures_description:
      - "Figure: Scatter of generated vs original item difficulty, showing wide dispersion especially at extremes (easy and hard items poorly calibrated)"
    analysis: >
      Item generation experiment在worst档是chain failure的一环。推荐：与bifactor pilot
      一起move to appendix as future work direction。Paper不应claim regeneration作为
      contribution。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: "Sinharay et al. (2006) cumulative Bayesian DIF priors模拟：4次successive administrations，展示evidence accumulation power improvement"
    expected_results:
      single_admin_power_delta_10: 0.38
      cumulative_2_admin_power: 0.52
      cumulative_3_admin_power: 0.64
      cumulative_4_admin_power: 0.71
      target_cumulative_3: 0.70
      target_met: false
      false_positive_rate_cumulative_4: 0.08
      bayes_factor_threshold: 10
      n_items_reaching_bf10: 0.42
      reviewer_count_questioning: 3
    result_rationale: >
      Simulation-only experiment在worst档被全部reviewers dismiss：(1) power从0.38
      提升到0.71 after 4 administrations，但target (0.70 after 3)没达到——需要4次
      administrations (>2年)才能达到moderate power，reviewer认为"impractical for the
      pace of LLM development where benchmarks are deprecated within months"；
      (2) 模拟使用synthetic data with known parameters——reviewer质疑"simulation
      parameters从哪来？如果from MMLU的misspecified IRT model，simulation本身就是
      garbage-in-garbage-out"；(3) 没有empirical validation——pure simulation without
      real-data demonstration在empirical paper中被视为filler；(4) Bayesian framework
      需要informative priors for DIF parameters——reviewer问"priors从哪来？there's no
      previous LLM DIF study to derive them from"。在worst档，plan_007被unanimous
      要求删除或move to separate methodological paper。
    tables:
      - name: "Table: Cumulative Bayesian DIF Power (Simulation)"
        columns: [n_administrations, power_delta10, power_delta14, fpr]
        rows:
          - [1, 0.38, 0.68, 0.04]
          - [2, 0.52, 0.79, 0.05]
          - [3, 0.64, 0.87, 0.06]
          - [4, 0.71, 0.92, 0.08]
    figures_description:
      - "Figure: Power accumulation curves across administrations for δ={0.8, 1.0, 1.2, 1.4, 1.6}, showing impractically slow convergence for medium effects"
    analysis: >
      Pure simulation with no empirical grounding。在worst档无contribution value。
      推荐：删除from paper entirely，save for future methods paper if real longitudinal
      data becomes available。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: "Progressive item replacement (5-50%)下的benchmark validity degradation分析"
    expected_results:
      rho_5pct_replacement: 0.998
      rho_10pct_replacement: 0.994
      rho_20pct_replacement: 0.983
      rho_50pct_replacement: 0.941
      reliability_5pct: 0.96
      reliability_20pct: 0.91
      reliability_50pct: 0.82
      construct_coverage_50pct: 0.71
      validity_threshold_crossed_at_pct: 35
      theoretical_bound_tight: false
      reviewer_interpretation: "degradation bounds are generous; real concern is construct drift not rank correlation"
    result_rationale: >
      Graceful degradation在worst档表现counter-productive：(1) ρ=0.983 at 20% replacement
      和ρ=0.941 at 50%——reviewer interprets as "MMLU is so redundant that even replacing
      half the items barely changes rankings→further evidence that 31% DIF is inconsequential"，
      reinforcing the ρ=0.997 'so what' attack；(2) reliability降到0.82 at 50%
      replacement——reviewer notes "reliability is still above 0.80 threshold even at
      50% replacement, so DIF has no practical impact on measurement quality"；
      (3) construct coverage drops to 0.71 at 50%——the one genuinely concerning metric，
      但reviewer argues "construct coverage is about replacement QUALITY (plan_006)
      not about DIF detection—you showed plan_006 fails to achieve quality replacements，
      so construct coverage concerns are moot"；(4) theoretical bounds not tight——
      worst-case scenarios are much worse than empirical observations, reviewer dismisses
      bounds as "vacuously conservative"。Overall：experiment provides ammunition FOR
      the 'so what' attack rather than defending against it。
    tables:
      - name: "Table: Validity Metrics Under Progressive Replacement"
        columns: [replacement_pct, rank_rho, reliability, construct_coverage]
        rows:
          - [0, 1.000, 0.97, 1.00]
          - [5, 0.998, 0.96, 0.97]
          - [10, 0.994, 0.94, 0.93]
          - [20, 0.983, 0.91, 0.86]
          - [31, 0.972, 0.88, 0.79]
          - [50, 0.941, 0.82, 0.71]
    figures_description:
      - "Figure: Three-panel degradation curves (rank ρ, reliability, construct coverage) vs replacement %, showing rank ρ remains above 0.95 even at 50% — reviewer highlight"
    analysis: >
      Experiment在worst档paradoxically证明DIF不重要。推荐：如果在paper中出现，必须
      reframe为"redundancy characterization"——"MMLU contains 2-3× more items than
      needed for stable rankings"作为benchmark design efficiency finding，而非DIF
      impact analysis。

  - name: item_focused_trees
    plan_id: plan_009
    description: "Tutz & Berger (2016) Item-Focused Trees：release date as continuous covariate，替代categorical cohort DIF"
    expected_results:
      n_items_with_significant_split: 3421
      pct_items_with_split: 27.3
      optimal_split_date_median: "2023-10-15"
      split_date_sd_days: 89
      concordance_ift_vs_mh: 0.74
      ift_captures_gradual_dif: true
      n_items_gradual_only: 412
      n_items_abrupt_only: 289
      ift_rmsea: 0.094
      reviewer_count_questioning: 2
    result_rationale: >
      IFT在worst档产生mixed结果：(1) 27.3% items有significant split，低于MH的31.3%——
      reviewer argues "IFT是更principled approach（no arbitrary cohort split），且
      检测更少items→MH over-detects by ~4 percentage points due to arbitrary 2023/2024
      split"；(2) concordance=0.74表示26%的items两种方法disagreement——reviewer问
      "哪种方法对？如果they disagree on 1/4 of items, how can we trust either?"；
      (3) 412 items只有IFT检测到(gradual DIF)——说明categorical MH misses gradual
      changes，但reviewer turns this around："这些items的DIF是gradual and smooth，
      not abrupt——更像capability improvement而非contamination"；(4) 289 items只有MH
      检测到但IFT没有——说明MH的categorical split creates artifacts；(5) IFT的RMSEA=0.094
      也差——reviewer combines with MH的Lz misfit和bifactor failure argue"no IRT-based
      method fits MMLU"。Optimal split date median=Oct 2023 with SD=89 days——
      "DIF不是sharp temporal boundary，而是diffuse process"，undermining temporal
      cohort narrative。
    tables:
      - name: "Table: IFT vs MH Comparison"
        columns: [metric, IFT, MH, interpretation]
        rows:
          - [pct_flagged, 27.3, 31.3, "MH detects 4pp more"]
          - [concordance, "—", "—", "0.74 (26% disagreement)"]
          - [gradual_only, 412, 0, "MH misses these"]
          - [abrupt_only, 0, 289, "MH artifacts?"]
          - [model_fit, "RMSEA=0.094", "|Lz|>2: 98%", "both poor"]
    figures_description:
      - "Figure: Item DIF onset date histogram from IFT, showing broad distribution (SD=89 days) rather than sharp 2023/2024 boundary"
    analysis: >
      IFT结果在worst档undermine MH的categorical approach。推荐：如果IFT confirms
      DIF existence (27.3% > random)但shows gradual pattern，reframe为"DIF is a
      continuous process, MH categorical split is a simplification"——honest但weakens
      the 31.3% headline number。Move to robustness appendix。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: "Decoder-only subpopulation DIF分析：IRT fit diagnostics + 与full-population DIF比较"
    expected_results:
      n_decoder_only: 5226
      n_non_decoder: 1
      pct_decoder_only: 99.98
      decoder_only_c_pct: 31.3
      jaccard_full_vs_decoder: 1.0
      rmsea_decoder_only: 0.087
      cfi_decoder_only: 0.73
      lz_misfit_pct: 97.8
      fit_improvement: "negligible"
      reviewer_interpretation: "architecture homogeneity is trivially achieved but IRT fit still poor"
    result_rationale: >
      Architecture stratification在worst档是trivially resolved but exposes bigger问题：
      (1) 99.98% decoder-only (5226/5227)意味着removing 1 non-decoder model changes
      nothing (Jaccard=1.0, C% identical)——reviewer says "this isn't a robustness
      check, it's confirming your data is architecturally homogeneous already"；
      (2) 关键：even with perfect architecture homogeneity, IRT fit STILL poor——
      RMSEA=0.087 barely improves from 0.089, Lz misfit 97.8% barely improves from
      98%——reviewer concludes "architecture heterogeneity was never the issue;
      unidimensional IRT is fundamentally misspecified for 57-subject MMLU regardless
      of architecture composition"；(3) reviewer uses this result to strengthen
      the "MH assumptions violated" attack——"even in the best-case architecturally
      homogeneous population, IRT fit is terrible, so MH-DIF results are unreliable"；
      (4) CFI=0.73远低于0.90 threshold——"this is not a marginally poor fit, it's a
      categorical model rejection"。Experiment proactively addresses architecture
      concern but hands reviewers a bigger weapon (IRT misfit persists)。
    tables:
      - name: "Table: Architecture Stratification Results"
        columns: [population, N, C_pct, RMSEA, CFI, Lz_pct_gt2]
        rows:
          - [full, 5227, 31.3, 0.089, 0.72, 98.0]
          - [decoder_only, 5226, 31.3, 0.087, 0.73, 97.8]
          - [delta, "—", 0.0, -0.002, +0.01, -0.2]
    figures_description:
      - "Figure: IRT fit index comparison (full vs decoder-only) showing negligible improvement — both firmly in 'poor fit' zone"
    analysis: >
      Architecture结果在worst档是Pyrrhic victory：resolves architecture concern but
      provides quantitative evidence that IRT misfit is intrinsic not architectural。
      推荐：翻转framing——"architecture homogeneity confirms IRT misfit is NOT due to
      mixing architectures but reflects MMLU's inherent multidimensionality——THIS IS
      THE FINDING"。IRT misfit becomes primary contribution in reframed narrative。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: "Known contamination injection into real METABENCH matrix：controlled ground truth for DIF detection power measurement"
    expected_results:
      temporal_external_tpr_p05: 0.834
      temporal_external_tpr_p10: 1.0
      temporal_external_fpr: 0.314
      temporal_external_delta_tpr_p10: 0.674
      temporal_external_delta_tpr_p05: 0.508
      standard_mh_fpr_inflation: 0.616
      matching_variable_contamination_confirmed: true
      dose_response_monotonic: true
      cross_subject_delta_fpr: 0.0
      reviewer_count_questioning_injection: 3
    result_rationale: >
      Semi-synthetic在worst档被全部reviewers攻击injection mechanism：(1) "flipping
      incorrect→correct doesn't model real contamination mechanisms"——real contamination
      involves training on exact/paraphrased items，not post-hoc response flipping。
      真实contamination改变model的internal representations，response flipping只改变
      observed responses without changing latent ability structure；(2) ΔTPR=0.508
      at p=0.5是在ARTIFICIAL conditions下——reviewer argues "当然injecting 50% flip rate
      能被检测到，real contamination exploitation rates are unknown and likely variable
      per-item"；(3) baseline FPR=0.314——reviewer notes "even BEFORE injection，
      你的method已经flags 31.4% of items as DIF→injection只是adding signal on top of
      a high-noise baseline"；(4) cross-subject matching ΔFPR=0.000是clean result，
      但reviewer argues "ΔFPR=0说明injection only adds TPR without changing FPR→
      但如果baseline FPR=0.314，absolute FPR is still unacceptably high"；(5) standard
      MH FPR inflates to 0.616——reviewer uses this as evidence "within-subject MH
      is broken, and your cross-subject fix only masks the problem"。Core attack：
      semi-synthetic从validation tool降级为"a toy demonstration that doesn't validate
      anything about real contamination"。
    tables:
      - name: "Table: Semi-synthetic Injection Results"
        columns: [matching, p, TPR, FPR, ΔTPR, ΔFPR]
        rows:
          - [cross_subject, 0.0, 0.326, 0.314, "—", "—"]
          - [cross_subject, 0.3, 0.548, 0.314, 0.222, 0.0]
          - [cross_subject, 0.5, 0.834, 0.314, 0.508, 0.0]
          - [cross_subject, 1.0, 1.000, 0.314, 0.674, 0.0]
          - [standard, 0.0, 0.298, 0.298, "—", "—"]
          - [standard, 1.0, 0.934, 0.616, 0.636, 0.318]
    figures_description:
      - "Figure: Dose-response curves (TPR vs injection rate p) for cross-subject vs standard matching, with reviewer annotation highlighting baseline FPR=0.314"
    analysis: >
      Semi-synthetic在worst档被视为artificial。核心问题不是statistical（results are
      internally consistent）而是ecological validity：injection mechanism不model real
      contamination。推荐：在reframed narrative下降级为methodological appendix，
      主叙事不依赖semi-synthetic作为validation。Cross-subject matching ΔFPR=0.000
      仍是methodological contribution但在appendix中。

  - name: multi_benchmark_temporal_dif
    plan_id: plan_028
    description: "6-benchmark temporal DIF (MMLU, ARC, HellaSwag, WinoGrande, TruthfulQA, GSM8K) + random controls"
    expected_results:
      mmlu_c_pct: 31.3
      winogrande_c_pct: 30.3
      truthfulqa_c_pct: 29.7
      arc_c_pct: 26.9
      gsm8k_c_pct: 18.9
      hellaswag_c_pct: 17.9
      range: "17.9-31.3%"
      all_random_below_1pct: true
      min_enrichment_ratio: 45
      coefficient_of_variation: 0.22
      reviewer_interpretation: "C% varies nearly 2× across benchmarks → benchmark-dependent, not universal"
    result_rationale: >
      6-benchmark replication在worst档被reviewer解读为weakness而非strength：(1) C%
      range 17.9-31.3%——nearly 2× variation across benchmarks。Reviewer: "如果DIF
      是temporal instability的universal phenomenon，为什么HellaSwag只有17.9%而MMLU
      有31.3%？这说明DIF高度依赖benchmark-specific properties (item count, difficulty
      distribution, construct breadth)，不能generalize"；(2) coefficient of variation
      =0.22——"substantial heterogeneity across benchmarks"；(3) all random controls
      <1%确认DIF是real signal，但reviewer pivots："OK it's real but it's benchmark-
      specific→你的headline '31%' only applies to MMLU，not to LLM benchmarks in
      general"；(4) HellaSwag (17.9%) has 10,042 items vs MMLU 12,508——similar size
      但DIF rate is 43% lower→"item count doesn't explain the variation, it's construct-
      specific"；(5) GSM8K (18.9%) is single-domain math——reviewer argues "lower DIF
      in domain-specific benchmarks suggests DIF is inflated in multi-domain benchmarks
      by cross-domain ability heterogeneity"→returns to unidimensional IRT misfit
      argument。Multi-benchmark replication被reframed by reviewers as evidence that
      DIF is an artifact of benchmark multidimensionality。
    tables:
      - name: "Table: Cross-Benchmark Temporal DIF"
        columns: [benchmark, n_items, n_ref, n_foc, C_pct, random_pct, enrichment]
        rows:
          - [MMLU, 12508, 1080, 807, 31.3, 0.18, 174]
          - [WinoGrande, 1267, 1017, 803, 30.3, 0.32, 95]
          - [TruthfulQA, 817, 1080, 807, 29.7, 0.37, 80]
          - [ARC, 1172, 1080, 807, 26.9, 0.60, 45]
          - [GSM8K, 1319, 1017, 804, 18.9, 0.30, 63]
          - [HellaSwag, 10042, 1080, 807, 17.9, 0.28, 64]
    figures_description:
      - "Figure: Bar chart of C% across 6 benchmarks with error bars, showing 17.9-31.3% range. Reviewer highlights the spread as evidence of benchmark-dependence"
    analysis: >
      Multi-benchmark在worst档需要reframing。推荐：C%变异是FEATURE不是bug——"different
      benchmarks have different measurement properties, and DIF characterizes WHICH
      properties vary temporally"。MMLU的high C%反映其multidimensional construct
      (57 subjects)的measurement complexity；HellaSwag/GSM8K的lower C%反映更
      homogeneous constructs。这是benchmark-specific measurement characterization。

  - name: permutation_null_c_rate
    plan_id: plan_029
    description: "1000× permutation test：randomly reassign temporal labels保持group sizes，建立C%的null distribution"
    expected_results:
      permutation_null_mean_c_pct: 1.2
      permutation_null_sd: 0.3
      permutation_null_max: 2.1
      permutation_null_p_value: 0.001
      observed_c_pct: 31.3
      z_score: 100.3
      enrichment_vs_null: 26.1
      reviewer_accepts_significance: true
      reviewer_questions_permutation_structure: 2
    result_rationale: >
      Permutation null在worst档technically succeeds (p<0.001, z>100) 但reviewer攻击
      permutation design：(1) "随机reassign temporal labels破坏temporal structure——
      真实null hypothesis不是'models are randomly assigned to years'而是'model capability
      improves smoothly over time without item-level differential effects'。你需要
      block permutation保留temporal auto-correlation，或time-series null model"；
      (2) 两位reviewer独立提出：permutation null mean=1.2%远高于random-split control
      0.18%——"为什么permutation比random split高6倍？说明permutation不是proper null——
      即使random label assignment也产生1.2% spurious DIF because group sizes are
      unbalanced (1080 vs 807)"；(3) reviewer承认31.3% >> 1.2% is significant，
      但argues "significance doesn't imply validity——MH可以在misspecified IRT下
      systematically produce significant results that are methodological artifacts"；
      (4) 一位reviewer要求block permutation within ability strata："如果你permute within
      ability quintiles，null C%会更高，可能approaching 5-10%→significance减弱"。
      Permutation test成功但不完全convince worst-case reviewers。
    tables:
      - name: "Table: Permutation Null Distribution"
        columns: [statistic, value]
        rows:
          - [null_mean_C_pct, 1.2]
          - [null_SD, 0.3]
          - [null_max, 2.1]
          - [observed_C_pct, 31.3]
          - [z_score, 100.3]
          - [p_value, "<0.001"]
          - [random_split_control, 0.18]
    figures_description:
      - "Figure: Null distribution histogram (1000 permutations) with observed C%=31.3% marked far right. Inset: reviewer question about null mean=1.2% vs random split 0.18%"
    analysis: >
      Permutation test在worst档partially accepted (significance not in doubt) but
      design questioned。Reviewer要求的block permutation是legitimate concern——simple
      permutation doesn't preserve temporal structure。推荐：如果可行，补充block
      permutation within ability strata作为rebuttal experiment。预期block permutation
      null mean≈2-4%，仍远低于31.3%但更robust against reviewer concern。

  - name: odds_ratio_regression_transparency
    plan_id: plan_030
    description: "Odds ratio + CI + McFadden/Nagelkerke R² + deviance ratio补充；item-level accuracy change as finer-grained predictor"
    expected_results:
      model1_mcfadden_r2: 0.0007
      model1_nagelkerke_r2: 0.0012
      model2_mcfadden_r2: 0.0423
      model2_nagelkerke_r2: 0.072
      model3_item_delta_r2: 0.0012
      model4_full_r2: 0.0434
      simpsons_paradox: true
      subject_acc_delta_or_per_010: 1.55
      item_acc_change_or_per_010: 1.08
      ctt_discrimination_or: 1.51
      ctt_difficulty_or: 0.78
      lr_test_chi2: 647
      reviewer_confused_by_simpsons: 2
      reviewer_accepts_decomposition: 0
    result_rationale: >
      Odds ratio regression在worst档fully transparent但引发Simpson's paradox困惑：
      (1) Model 1 (domain-level Δacc → DIF flag): OR=1.55 per 0.10 increase, R²=0.0007
      ——"accuracy improvement predicts DIF at domain level"。Model 4 (item-level Δacc
      + item properties → DIF flag): item Δacc OR=0.92 (REVERSAL), R²=0.043——
      "controlling for item properties, accuracy improvement NEGATIVELY predicts DIF"。
      Simpson's paradox是real but reviewer反应：(a) "Simpson's paradox usually indicates
      omitted variable bias——你的item properties (difficulty, discrimination) are the
      real drivers, not temporal DIF"；(b) "R²=0.043 for full model means 95.7% of
      DIF variance is UNEXPLAINED——这不是'domain improvement explains little'而是
      'nothing explains DIF, suggesting it's noise'"；(2) discrimination OR=1.51是
      最强predictor——reviewer argues "高discrimination items更likely被flagged as DIF
      因为MH method本身对high-discrimination items更sensitive→methodological artifact
      而非substantive finding"；(3) 两位reviewer被Simpson's paradox confused——
      一位认为Model 1是correct (DIF correlates with improvement)，另一位认为Model 4
      是correct (DIF anti-correlates after controlling)→neither accepts the decomposition
      narrative。Overall：transparency backfires because it reveals the data are
      fundamentally ambiguous about causation。
    tables:
      - name: "Table: Logistic Regression Model Comparison"
        columns: [model, predictors, McFadden_R2, key_OR, AIC]
        rows:
          - ["M1", "domain Δacc", 0.0007, "1.55 (domain)", 15545]
          - ["M2", "domain Δacc + items", 0.0423, "0.73 (domain, reversed)", 14902]
          - ["M3", "item Δacc", 0.0012, "1.08 (item)", 15537]
          - ["M4", "item Δacc + items", 0.0434, "0.92 (item, reversed)", 14885]
          - ["—", "—", "—", "discrimination OR=1.54", "—"]
    figures_description:
      - "Figure: Simpson's paradox illustration — domain-level positive slope (M1) reverses to negative at item-level (M4) when controlling for difficulty and discrimination"
    analysis: >
      Simpson's paradox在worst档是interpretive nightmare。Reviewers将ambiguity解读为
      "DIF has no clear driver→possibly artifact"。推荐：present Simpson's paradox as
      finding about MMLU's complex measurement structure，not as evidence for/against
      ability confound。R²=0.043的low explanatory power reframe为"DIF is predominantly
      item-specific and not predictable from aggregate statistics→each item's DIF
      must be examined individually→supporting diagnostic lens framing"。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07c0d909-7da2-4962-b7fb-17acc0708eb8",
  "isSidechain": false,
  "requestId": "req_011CbFsz2BPiLiPHkRVoz7Ds",
  "type": "assistant",
  "uuid": "1c0d5800-18b1-4f7f-a1ea-40b843991cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qBoGABFANbeQWi8dLLZuh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23247,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16999,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16999,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23247
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心张力未化解：reviewers同时认为(a) ρ=0.997说明DIF不影响rankings所以'so what'，AND (b) 31%可能是MH method artifact（unidimensional IRT misfit + LLM population不满足MH assumptions）。…",
  "leafUuid": "1c0d5800-18b1-4f7f-a1ea-40b843991cb0",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric audit of LLM benchmarks via DIF analysis",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心张力未化解：reviewers同时认为(a) ρ=0.997说明DIF不影响rankings所以'so what'，AND (b) 31%可能是MH method artifact（unidimensional IRT misfit + LLM population不满足MH assumptions）。…",
  "leafUuid": "1c0d5800-18b1-4f7f-a1ea-40b843991cb0",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric audit of LLM benchmarks via DIF analysis",
  "sessionId": "530279c9-746a-474b-ac69-6d2a4f70c94e"
}
```

---
