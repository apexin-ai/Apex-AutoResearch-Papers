# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Claim 1和Claim 3被接受；Claim 2 (meta-critique)被部分reviewers视为obvious；Claim 4 ac

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/937a0eab-90a2-4790-97fd-3c463550c819.jsonl`
- **Structured JSON:** [`b71837beec3d329b83fd.json`](../../sessions/b7/b71837beec3d329b83fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T14:27:22.416Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T14:27:22.416Z",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Claim 1和Claim 3被接受；Claim 2 (meta-critique)被部分reviewers视为obvious；Claim 4 actionability论证需要加强；ρ=0.997的'instability ≠ invalidity'张力未完全化解——至少1位reviewer质疑'if rankings don't change, why should we care?'\n核心假设：['31% C%的genuineness被接受，但至少1位reviewer要求更强的causal language hedging', \"Ground truth meta-critique被1-2位reviewers视为'well-known limitation'，需在rebuttal中补充更多prior work对比\", 'Cross-subject matching被接受但Proposition 1的formal proof被视为incremental', \"6-benchmark replication accepted，但HellaSwag/GSM8K的较低C%(17-19%)被质疑为'DIF可能benchmark-specific'\", 'DIF-cleaned demonstration的cohort asymmetry被承认，但reviewer要求控制model quality confound', '10→8页压缩导致1-2个robustness check被移入appendix，reviewer要求在main text恢复', 'plan_029 permutation null成功但reviewer要求additional controls（如按model family分层permutation）']\n关键指标范围：{'reviewer_avg_score': [3.25, 3.75], 'permutation_null_mean_c_pct': [0.1, 1.0], 'permutation_null_p_value': [0.0, 0.01], 'rebuttal_issues_count': [3, 5], 'claims_accepted_without_caveat': [1, 2], 'page_compression_info_loss_pct': [10, 25], 'reviewers_questioning_actionability': [1, 2]}\n叙事方向：需调整claims强度：Claim 2从'the field's validation approach is fundamentally mismatched'弱化为'we provide empirical evidence that web-overlap labels have limited utility for item-level differential detection'。Claim 4的framing从'actionable diagnostic protocol'调整为'DIF as analytical lens with illustrative demonstration'——降低prescriptive tone，增加exploratory framing。Rebuttal策略：用plan_032的z=8.5 random baseline对比数据正面回应actionability质疑；用Simpson's paradox (plan_030)作为'models got better ≠ items changed'的second line of defense。可能需要补充1个rebuttal experiment（如per-family DIF stability analysis）。整体仍冲Conference accept，但依赖strong rebuttal。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\nfocus: This is re-dream #8 after major revisions addressing Dream #7's specific weaknesses. Key improvements since Dream #7 (all integrated into paper via P6-P16 patches):\n\n1. **Actionability paradox SOLVED** (was CW1-level concern): NEW plan_032 DIF-cleaned MMLU demonstration shows 89.5% models shift ≥5 ranks, systematic cohort bias (2024 Δrank=+73.6), confirmed DIF-specific by random baseline (z=8.5). This directly answers \"ρ=0.997 means DIF doesn't matter.\"\n\n2. **Proposition 1 (ΔFPR=0 formalized)**: Cross-subject matching now has a formal algebraic proof, not just an empirical observation. Elevates methodological contribution.\n\n3. **Temporal coarseness addressed**: NEW plan_031 6-month window robustness check (C%=34.35%, 181× enrichment) shows DIF is robust to finer temporal granularity.\n\n4. **Subject DIF direction asymmetry** (NEW analytical finding): STEM subjects favor 2024 models (55.4%), Humanities favor 2023 (64.4%) — content-level predictor of DIF direction.\n\n5. **Expanded Related Work**: Added BHI (Blebea et al. 2024), PSN-IRT (Polo et al. 2024), Maeda (2024) — addresses \"thin related work\" concern.\n\n6. **Systematic Confound Elimination narrative**: 6 negative results reframed as systematic exclusion of confounds (architecture, ability, local dependence, IRT misfit, reasoning-RL, ensemble), strengthening the \"what remains is genuine temporal DIF\" argument.\n\n7. **Bootstrap CI on headline C%**: MMLU C%=31.3% [29.5%, 33.1%] with N=1000 model resampling.\n\n8. **Causal language softened** throughout — \"contamination-adjacent\" phrasing replaced with hedged \"differential functioning\" language.\n\n9. **DIF-for-LLMs paragraph** added in Discussion — explicitly addresses what DIF means for machine (vs. human) examinees.\n\n10. **Audit protocol expanded** with code release commitment.\n\n11. **ConStat/DVD comparison visibility increased** — AUROC numbers and Jaccard overlap now in main text.\n\nReviewers should evaluate whether these revisions close the gap from 3.5 to 4.0 (Conference). The paper's strongest path to 4.0: unprecedented scale + cross-subject matching (Proposition 1) + Simpson's paradox + DIF-cleaned demonstration (actionability) + 6-benchmark replication + systematic confound elimination.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n      bootstrap_ci_95:\n      - 29.38\n      - 38.05\n      bootstrap_mean: 33.14\n      bootstrap_sd: 2.3\n      bootstrap_n: 1000\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n- exp_id: plan_031_temporal_granularity\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_full_year:\n      comparison: 2023 vs 2024\n      distance_yr: 1\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.32\n      random_pct_c: 0.02\n    mmlu_half_year:\n      comparison: 2023-H2 vs 2024-H1\n      distance_yr: 0.5\n      n_ref: 1018\n      n_foc: 807\n      pct_c: 34.35\n      random_pct_c: 0.19\n    mmlu_within_2023:\n      comparison: 2023-H1 vs 2023-H2\n      distance_yr: 0.5\n      n_ref: 62\n      n_foc: 1018\n      pct_c: 22.62\n      random_pct_c: 0.18\n      supplementary: true\n    cross_bench_half_year:\n      arc_pct_c: 29.27\n      hellaswag_pct_c: 18.07\n      winogrande_pct_c: 33.62\n      truthfulqa_pct_c: 31.33\n    cross_bench_full_year:\n      arc_pct_c: 26.88\n      hellaswag_pct_c: 17.89\n      winogrande_pct_c: 30.31\n      truthfulqa_pct_c: 29.74\n    half_year_gt_full_year_all_benchmarks: true\n    dif_saturates_within_6mo: true\n- exp_id: plan_032_dif_cleaned_mmlu\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_items_full: 12508\n    n_items_cleaned: 8590\n    n_items_removed: 3918\n    pct_removed: 31.3\n    spearman_rho: 0.9965\n    rank_change_std: 127.1\n    rank_change_min: -589\n    rank_change_max: 849\n    pct_change_ge5: 89.5\n    pct_change_ge10: 79.5\n    pct_change_ge20: 66.4\n    pct_change_ge50: 41.9\n    pct_change_ge100: 24.8\n    top100_pct_ge10: 18\n    top500_pct_ge10: 47.2\n    cohort_2023_mean_change: -22.56\n    cohort_2023_median_change: -5\n    cohort_2024_mean_change: 73.6\n    cohort_2024_median_change: 11\n    systematic_bias: DIF items favor 2024 models; cleaning hurts 2024 +73.6 avg, helps\n      2023 -22.6 avg\n    top_hurt_families:\n      phi-3: 258.35\n      command-r: 235\n      solar: 149.15\n      llama-3: 120.86\n    top_benefit_families:\n      mistral-0.1: -60.32\n      mistral: -53.27\n      zephyr: -29.94\n      gemma-2: -28.78\n    removed_items_harder: true\n    removed_mean_difficulty: 0.409\n    cleaned_mean_difficulty: 0.46\n    random_baseline_20trials:\n      rank_change_std:\n        mean: 60.2\n        std: 7.8\n      mean_abs_rank_change:\n        mean: 36\n        std: 3.6\n      pct_change_ge100:\n        mean: 8.5\n        std: 2\n      cohort_2023_mean_change:\n        mean: 0.4\n        std: 4.1\n      cohort_2024_mean_change:\n        mean: 2.8\n        std: 21.2\n    dif_vs_random_z_scores:\n      rank_change_std_z: 8.5\n      mean_abs_change_z: 10.7\n      pct_ge100_z: 8.2\n      cohort_2023_z: -5.6\n      cohort_2024_z: 3.3\n      cohort_asymmetry_gap_z: 4.4\n- exp_id: plan_033_subject_dif_concentration\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_subjects: 57\n    all_subjects_have_dif: true\n    mean_pct_c: 30.6\n    median_pct_c: 29.7\n    sd_pct_c: 5.5\n    range_pct_c:\n    - 20.7\n    - 48.4\n    top3_subjects:\n      business_ethics: 48.4\n      human_aging: 41.9\n      formal_logic: 40.4\n    bottom3_subjects:\n      computer_security: 20.7\n      marketing: 20.9\n      management: 21.7\n    domain_pct_c:\n      STEM: 30.9\n      Humanities: 31.1\n      Social_Science: 31.6\n    stem_vs_humanities_p: 0.611\n    kruskal_wallis_p: 0.78\n    logistic_regression:\n      difficulty_OR: 0.086\n      discrimination_OR: 57.2\n      pseudo_r2: 0.042\n    excess_dif_subjects:\n    - professional_law\n    - human_aging\n    - world_religions\n    - business_ethics\n    - professional_medicine\n    overall_pct_favor_2024: 43.9\n    temporal_asymmetry:\n      STEM_pct_favor_2024: 55.4\n      Humanities_pct_favor_2024: 35.6\n      Social_Science_pct_favor_2024: 42\n    unidirectional_subjects:\n      world_religions:\n        pct_favor_2024: 16.9\n      logical_fallacies:\n        pct_favor_2024: 20\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T14:27:22.420Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T14:27:22.420Z",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T14:27:22.455Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Claim 1和Claim 3被接受；Claim 2 (meta-critique)被部分reviewers视为obvious；Claim 4 actionability论证需要加强；ρ=0.997的'instability ≠ invalidity'张力未完全化解——至少1位reviewer质疑'if rankings don't change, why should we care?'
核心假设：['31% C%的genuineness被接受，但至少1位reviewer要求更强的causal language hedging', "Ground truth meta-critique被1-2位reviewers视为'well-known limitation'，需在rebuttal中补充更多prior work对比", 'Cross-subject matching被接受但Proposition 1的formal proof被视为incremental', "6-benchmark replication accepted，但HellaSwag/GSM8K的较低C%(17-19%)被质疑为'DIF可能benchmark-specific'", 'DIF-cleaned demonstration的cohort asymmetry被承认，但reviewer要求控制model quality confound', '10→8页压缩导致1-2个robustness check被移入appendix，reviewer要求在main text恢复', 'plan_029 permutation null成功但reviewer要求additional controls（如按model family分层permutation）']
关键指标范围：{'reviewer_avg_score': [3.25, 3.75], 'permutation_null_mean_c_pct': [0.1, 1.0], 'permutation_null_p_value': [0.0, 0.01], 'rebuttal_issues_count': [3, 5], 'claims_accepted_without_caveat': [1, 2], 'page_compression_info_loss_pct': [10, 25], 'reviewers_questioning_actionability': [1, 2]}
叙事方向：需调整claims强度：Claim 2从'the field's validation approach is fundamentally mismatched'弱化为'we provide empirical evidence that web-overlap labels have limited utility for item-level differential detection'。Claim 4的framing从'actionable diagnostic protocol'调整为'DIF as analytical lens with illustrative demonstration'——降低prescriptive tone，增加exploratory framing。Rebuttal策略：用plan_032的z=8.5 random baseline对比数据正面回应actionability质疑；用Simpson's paradox (plan_030)作为'models got better ≠ items changed'的second line of defense。可能需要补充1个rebuttal experiment（如per-family DIF stability analysis）。整体仍冲Conference accept，但依赖strong rebuttal。

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


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b11e08ac-935c-4c83-ba84-aed9124e04cc",
  "type": "user",
  "uuid": "59cd9c0b-7af5-432c-9294-b17b1485aa33",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T14:27:22.453Z_

```json
{
  "parentUuid": "59cd9c0b-7af5-432c-9294-b17b1485aa33",
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
  "uuid": "df408259-40a9-4ebc-8205-f71c1c684dc6",
  "timestamp": "2026-05-21T14:27:22.453Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T14:27:22.453Z_

```json
{
  "parentUuid": "df408259-40a9-4ebc-8205-f71c1c684dc6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c5755e30-4619-4373-864f-a9c81ee476b6",
  "timestamp": "2026-05-21T14:27:22.453Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claim 1和Claim 3被接受；Claim 2 (meta-critique)被部分reviewers视为obvious；Claim 4 actionability论证需要加强；ρ=0.997的'instability ≠ invalidity'张力未完全化解——至少1位reviewer质疑'if…",
  "leafUuid": "c5755e30-4619-4373-864f-a9c81ee476b6",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier DIF findings: temporal instability robust, not driven by capability gain",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819"
}
```

---

### Assistant

_source line 8 · 2026-05-21T14:29:47.708Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for each "planned" experiment in the experiment_plan, based on the "median" tier definition. I need to predict what results each planned experiment would produce in the median outcome scenario, with rationale for each.

Let me identify all "planned" experiments:

1. plan_001 - real_data_dif_mmlu (status: planned) - BUT wait, this is already in the registry as completed (plan_001_real_data_dif_mmlu). Let me re-check...

Actually, looking more carefully at the registry, many experiments are already DONE. Let me identify which ones are still "planned":


I'm seeing a list of sixteen experiments marked as planned in the experiment_plan, ranging from plan_001 through plan_030, though the list appears to cut off mid-thought.

Looking at the registry, there's a significant discrepancy—many of these experiments are actually marked as completed, including plan_001, plan_011, plan_012, plan_013, plan_014, plan_016, plan_017, plan_004, plan_027, plan_028, plan_030, plan_031, and plan_032, with one (plan_015) marked as killed. The registry data seems to be truncated as well, cutting off at plan_032.

Now I'm cross-referencing the planned experiments against what's actually in the registry. Several key experiments are still pending: plan_002 through plan_010, with some variations like plan_003a, 003b, and 003c, plus plan_005 and plan_006. I need to verify the status of plan_010 since the registry lookup appears incomplete.

Looking at the user's request more carefully—they want detailed data generated for every planned experiment in the experiment_plan, but many have already been completed. The task seems to be generating predicted or synthetic results for the experiments that remain in "planned" status. So I need to distinguish between experiments that are marked as planned but already have real results in the registry versus those that are genuinely still pending. The ones with actual registry data should use their real outcomes, while the truly unexecuted experiments need simulated median-tier predictions. Let me identify which planned experiments actually lack registry entries and generate plausible data for those. I'm realizing the distinction: for experiments already in the registry with real results, I should use those actual values since they're documented. For the truly planned experiments without results yet, I'll generate predictions that align with what a median-tier submission would show. The "dream" framework means I'm imagining the complete paper as if all these experiments had been run and submitted together.

Looking at what's actually missing—the experiment plan lists plan_002, plan_003a, plan_003b, plan_003c, plan_005, and plan_006, but the registry only has plan_001 through plan_004 and some others. So I need to focus on generating imagined results specifically for those gap experiments that exist in the plan but not in the completed registry. Looking at the paper's framing, I'm noticing discrepancies between what's marked as planned versus what's actually documented. Plan_010 appears to have results already (the 99.98% decoder-only finding), plan_005 and plan_006 were abandoned when bifactor_irt got killed, and plan_003a/b/c are explicitly called out as never executed future work. Plan_002 shows up in the dropped section as underpowered, and plan_007 was simulation-only.

Now I'm realizing the core task: I should generate imagined median-tier results for all experiments in the experiment_plan, treating the ones already in the registry as reference points while still providing predictions for the rest. Let me compile the full YAML output with imagined results for each experiment. the median tier. I'll base already-completed ones on their actual registry data and predict the truly-planned ones.

Actually, I just realized - many of the experiment_plan entries already have real results in the registry. The paper framing already incorporates those results. For the median tier "dream," what matters most is:

1. How the already-completed experiments' results get RECEIVED by reviewers
2. What the still-planned experiments would yield

Let me focus on generating predictions for ALL experiments in experiment_plan, as the user requested. For completed ones, I'll use their actual results (with median-tier reviewer interpretation). For planned ones, I'll predict results consistent with the median tier definition.

Let me now think about what each experiment would produce in the median tier:

**plan_001 (real_data_dif_mmlu)**: Already done. Registry shows C%=31.3%, enrichment=0.96, etc. In median tier, Claim 1 is accepted and these results stand.

**plan_002 (rl_robustness_validation)**: This is genuinely planned. With only ~13 reasoning-RL models available, the sample size would be too small to support strong conclusions. The results would show DIF stability when adding alignment-RL models, but traditional detectors like Min-K% and ConStat would show some degradation on the limited RL models without sufficient statistical power.

**plan_003a (constat_perturbation_eval)** and **plan_003b (dvd_generation_variance_eval)**: Both never executed. If attempted in the median tier, they'd face GPU budget constraints and show moderate detection power for non-RL models at best.

**plan_003c (ensemble_fusion)**: Blocked by the failure of 003a and 003b.

**plan_004 (cross_benchmark_gsm8k)**: Already completed with C%=18.9% and GSM1K correlation r=-0.478.

**plan_005 (bifactor_irt_equating_pilot)**: The bifactor model fails to converge on the full 57-subject structure in the median tier.

**plan_006 (item_generation_calibration)**: Blocked since plan_005 failed.

**plan_007 (cumulative_bayesian_dif)**: Simulation-only, showing promised power improvement but reviewers view it as incremental without real-data validation.

**plan_008 (graceful_degradation_analysis)**: Simulation shows graceful degradation but remains supplementary.

**plan_009 (item_focused_trees)**: Incomplete thought here - let me continue based on the pattern.

Plan_009 shows a similar pattern to categorical DIF but uses a continuous release-date covariate, making it supplementary. Plan_010 is already referenced in the paper framing with 99.98% decoder-only architecture, accepted as architecture isn't a confounder. Plan_011 is done with ΔTPR=+0.674. Plan_028 is complete across 6 benchmarks with C% ranging from 17.9-31.3%. Plan_029 is genuinely planned—a permutation null test with 1000 permutations would confirm that the 31% result is far above chance.

Plan_030 is already done showing Simpson's paradox. Now I'm structuring the YAML for the median tier, where claims 1 and 3 are accepted, claim 2 seems obvious to some reviewers, and claim 4 needs stronger actionability. The ρ=0.997 tension remains unresolved, reviewer scores average 3.25-3.75, and I need to address 3-5 rebuttal issues. For each experiment I'm documenting the name, plan_id, description, expected results with metrics, result rationale, tables, figures, and analysis approach.

For plan_001, I already have real results showing temporal C% at 31.3% with enrichment of 0.96. Plan_002 on RL robustness shows partial success in the median tier—adding 13 reasoning-RL models barely shifts the group-level C% from 31.3% to around 31.0%, but that sample size is too small for confident claims. Traditional detectors like Min-K% see AUROC drop from 0.72 to 0.55 on RL models, ConStat drops from 0.68 to 0.51, and the TOST equivalence test is inconclusive due to the small N. Plan_003a on ConStat perturbation evaluation doesn't execute in the median tier, which aligns with the paper's framing. Plan_003b on DVD generation variance is still being worked through.

For the remaining plans, plan_003c on ensemble fusion didn't execute due to dependency failures. Plan_004 is complete with C%=18.9% and GSM1K correlation of -0.478. Plan_005 on bifactor IRT was killed due to poor convergence, which blocks plan_006 on item generation. Plan_007 on cumulative Bayesian DIF shows promising simulation results—power improves from 0.40 to 0.68 after three administrations, though this is simulation-only. Plan_008 on graceful degradation maintains correlation above 0.99 up to 20% replacement before dropping off. Plan_009 on item-focused trees mirrors the MH-DIF pattern with a continuous temporal gradient. Plan_010 on architecture-stratified DIF shows the model is 99.98% decoder-only with unchanged C%.

Now looking at the remaining completed plans: plan_011 shows a TPR improvement of +0.674, plan_028 covers 6 benchmarks ranging from 17.9-31.3%, and plan_029 on permutation null testing ran 1000 permutations with null mean C% around 0.5% and p<0.001—this is critical for the median tier narrative. Plan_030 confirms Simpson's paradox. I'm now mapping these results against the median tier guidance, which flags that claim 2 is seen as a well-known limitation by 1-2 reviewers, claim 4 needs stronger actionability, and the ρ=0.997 tension raises questions about why ranking stability matters if the actual rankings don't change.

The guidance also notes that while 31% genuineness is accepted, causal language needs hedging, cross-subject matching is fine but Proposition 1's formal proof feels incremental, and the lower C% on HellaSwag/GSM8K (17-19%) gets questioned as potentially benchmark-specific. The DIF-cleaned demonstration's cohort asymmetry is acknowledged but reviewers worry about model quality confounds, the page compression from 10 to 8 loses some robustness checks, and while the permutation null succeeds, one reviewer wants per-family stratified permutation testing instead.

Wait, I need to reconsider what "planned" actually means here. Looking back at the experiment_plan, every entry has status=planned, but some have real results already in the registry. The user's request was for every planned experiment in the plan, which is literally all of them—but I should distinguish between those with actual results versus those still pending.

For completed experiments, I'll use their real metrics as the expected results since they're already known. For truly planned ones, I'll predict both the results and how reviewers might receive them. The key is framing this in a median-tier outcome context—where results are realistic but not perfectly clean, showing the kinds of trade-offs and limitations that typically emerge. solid but have caveats that reviewers pick up on. In the "low" tier, results have more significant weaknesses, so for the median tier, each experiment needs defensible results with specific weaknesses that match the tier definition.

For completed experiments, I'll explain how the actual results map to the median tier outcome—like if C%=31.3%, I'd note it's accepted but needs hedged causal language. For planned experiments, I'll describe what results we'd expect and why they fit the median tier.

The median tier specifies a permutation null mean C% between 0.1% and 1.0% with p<0.01, so I'm targeting around 0.5% mean with p<0.001 for plan_029. I also need to hit the key metrics: reviewer scores between 3.25-3.75, rebuttal issues between 3-5, only 1-2 claims accepted without caveats, 10-25% information loss from page compression, and 1-2 reviewers questioning actionability.

Now I'll work through each experiment systematically with detailed metrics. Looking at the experiments that were never executed in the paper framing, I need to decide whether to generate imagined data for them in the median tier or just note they weren't run. Since the user asked for detailed data on each planned experiment, I should provide what would have happened if they'd been completed, while being clear about their dropped status—distinguishing between experiments still planned before submission versus those already killed. plan_005 was killed, plan_006 is blocked, and plans 007-010 were executed in various capacities—simulation-only, supplementary, or with full results. Now I'm laying out the precise metrics for each plan, starting with plan_001's registry data approach and plan_002's underpowered RL cohort showing negligible DIF changes and near-chance classification performance. I'm abandoning the bifactor approach in favor of within-subject DIF analysis. Plan 006 is blocked by that failure, but plan 007 shows promising simulation results—individual administrations reach 40% power at δ=1.0, climbing to 74% after four attempts. Plan 008 reveals that score reliability holds up reasonably well even at 20% contamination, with correlations remaining above 0.995 across replacement levels.

The item factor analysis confirms a temporal gradient in DIF effects that aligns with the 2023-Q3 cohort split, though the continuous model adds minimal predictive value beyond the categorical finding. Architecture isn't a confounder—nearly all models are decoder-only, and removing the single outlier doesn't change the pattern. Registry data shows a substantial TPR improvement of 0.674 with zero cross-subject false positive rate.

Now I'm looking at the permutation test results across six benchmarks, where the median tier shows lower contamination rates around 17-19% for HellaSwag and GSM8K. The null distribution from 1000 permutations centers at 0.47% with a z-score of ~257 against the observed 31.3%, giving extremely strong significance. Simpson's paradox emerges in the registry data, and I need to move some robustness checks to the appendix due to space constraints. I'm preparing the YAML output with detailed results, making sure to cover the key sub-analyses from the within-family confound control experiments while staying focused on the metrics that define the median tier outcome.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5755e30-4619-4373-864f-a9c81ee476b6",
  "isSidechain": false,
  "requestId": "req_011CbFsSdTJGKDVYTDFVHsgg",
  "type": "assistant",
  "uuid": "86c5de96-0a39-473d-a4f4-838e19d0fb3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiDAEySiJeB3pfXVQevE3M",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23066,
      "cache_read_input_tokens": 11841,
      "output_tokens": 20125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 20125,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23066
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

_source line 9 · 2026-05-21T14:34:25.862Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1和Claim 3被接受为solid empirical contributions；Claim 2的meta-critique被1-2位reviewers视为
  "well-known but under-documented limitation"——需在rebuttal中补充5+篇使用web-overlap labels做item-level
  validation的具体引用以证明field确实在犯这个错误；Claim 4的actionability论证依赖plan_032的z=8.5 random
  baseline对比，但至少1位reviewer质疑cohort asymmetry可能反映model quality confound而非DIF-specific
  effect；ρ=0.997的"instability ≠ invalidity"张力在Introduction中upfront framing帮助了，但1位reviewer
  仍写"if the rankings are this stable, the practical significance of 31% instability is
  unclear"。Rebuttal策略：用plan_030 Simpson's paradox作为"models got better ≠ items changed"
  的defense line；用plan_029 permutation null（p<0.001）正面回应"is 31% above chance"；
  HellaSwag/GSM8K较低C%（17-19%）的解释需补充benchmark structural differences（item count, domain
  homogeneity）。整体需要strong rebuttal + 1个supplementary experiment（per-family stratified
  permutation）才能从3.5推到4.0 Conference accept线。Claims 1和3 accepted without major caveat；
  Claim 2需要additional prior work citations；Claim 4需要降低prescriptive tone。
  页面压缩从10→8页导致plan_018 threshold sensitivity table和plan_022 de-duplication detail
  被移入appendix，1位reviewer要求在main text恢复threshold robustness summary。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      对METABENCH MMLU响应矩阵（5219模型×12508题目）进行MH-DIF分析。包括temporal cohort split
      (2023 vs 2024-H1)、ability-quintile split、within-family confound control (Llama-2 vs
      Llama-3)、domain-specificity分析、Li et al. web-overlap proxy验证。
    expected_results:
      temporal_cohort:
        n_ref: 1080
        n_foc: 807
        ets_c_pct: 31.3
        ets_b_pct: 20.5
        ets_a_pct: 48.2
        mean_delta_mh_c_items: 2.14
        median_delta_mh_c_items: 1.78
      ability_cohort:
        ets_c_pct: 2.9
        enrichment: 1.19
      within_family:
        llama2_vs_llama3_c_pct: 61.3
        mistral_vs_mixtral_c_pct: 38.7
        llama_jaccard_with_temporal: 0.28
      domain_specificity:
        spearman_rho_acc_improvement_vs_c_pct: 0.307
        spearman_p: 0.02
        n_subjects: 57
        all_subjects_have_dif: true
        c_pct_range: [20.7, 48.4]
      proxy_validation:
        li_et_al_coverage: 0.738
        enrichment_temporal: 0.96
        fpr_li_clean_temporal: 0.318
        enrichment_ability: 1.19
        fpr_li_clean_ability: 0.027
      sanity_check:
        random_split_c_pct: 0.18
        temporal_ability_jaccard: 0.014
    result_rationale: >
      在median档位下，31.3% C%是核心发现，被Claim 1直接支撑。Reviewers接受这个数字的statistical
      significance（random split仅0.18%），但至少1位reviewer要求更强的causal language hedging——
      因为within-family分析（Llama-2 vs Llama-3 C%=61.3%）显示family-level capability jump也会
      产生高DIF，temporal cohort的31.3%可能混合了genuine item instability和capability-driven DIF。
      ρ=0.307的domain-level correlation被接受为modest ecological correlation，但reviewer要求
      明确"item-level decomposition shows only 2.4pp explained"（来自plan_019/030）。
      Enrichment≈0.96支撑Claim 2但被1位reviewer视为"expected by construction"。Ability cohort
      的2.9% C%作为negative control被接受。
    tables:
      - name: "Table 1: Temporal DIF Summary"
        content: "4-way sensitivity matrix: cohort × item filtering → C% values"
      - name: "Table 2: Domain-Specificity"
        content: "57 subjects × C% × accuracy improvement correlation"
    figures_description:
      - "Figure 1: DIF flag distribution across 57 MMLU subjects (heatmap), showing uniform spread with excess in professional_law, human_aging, business_ethics"
      - "Figure 2: Enrichment scatter — DIF C flags vs Li et al. web-overlap labels, showing near-unity enrichment with annotation explaining expected independence"
    analysis: >
      核心结果solid。Median档reviewers的主要friction点：(1) within-family Llama-2v3的C%=61.3%
      远高于temporal 31.3%，需要解释为什么family comparison不是更好的design；(2) domain ρ=0.307
      虽然p=0.02但effect size modest，需要plan_019 item-level decomposition作为补充；
      (3) Li et al. proxy validation的"negative result"需要更清晰的framing——是validation failure
      还是expected orthogonality。8页压缩下within-family detail可能被移入appendix。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      验证DIF对reasoning-RL模型的鲁棒性。从METABENCH筛选alignment-RL模型（DPO/ORPO，N≈477），
      外加10-15个open-weight reasoning-RL模型（GRPO/PPO），测试DIF检测稳定性并与传统检测器对比。
    expected_results:
      alignment_rl_cohort:
        n_models: 477
        c_pct_with_alignment_rl: 31.1
        c_pct_without: 31.3
        jaccard_flags_overlap: 0.968
        flag_stability: "negligible change"
      reasoning_rl_models:
        n_available: 13
        models_tested: ["deepseek-r1-7b", "deepseek-r1-32b", "qwen2.5-rl-7b", "qwen2.5-rl-14b", "qwen2.5-rl-32b", "o1-mini-proxy", "skywork-or1-8b", "open-reasoner-7b", "marco-o1-7b", "k2-65b", "rstar-math-7b", "still-2-1.5b", "llemma-rl-7b"]
        c_pct_with_rl_in_focal: 31.0
        c_pct_change: -0.3
        jaccard_with_vs_without_rl: 0.971
      traditional_detector_comparison:
        mink_auroc_non_rl: 0.714
        mink_auroc_rl_models: 0.528
        mink_auroc_delta: -0.186
        constat_auroc_non_rl: 0.681
        constat_auroc_rl_models: 0.513
        constat_auroc_delta: -0.168
        dif_retention_ratio: 0.987
      statistical_tests:
        delong_mink_p: 0.089
        delong_constat_p: 0.112
        tost_equivalence: "inconclusive (CI: [-0.04, 0.07], bounds ±0.10)"
        bootstrap_ci_dif_retention: [0.93, 1.03]
      power_analysis:
        partial_exploitation_p04: "delta_MH≈0.84, TPR≈0.31"
        partial_exploitation_p07: "delta_MH≈1.18, TPR≈0.52"
        partial_exploitation_p10: "delta_MH≈1.68, TPR≈0.76"
        detection_boundary: "p≈0.55 for TPR≥0.50 at N=100"
    result_rationale: >
      Median档位的关键限制：reasoning-RL模型仅13个，远低于统计显著性所需的样本量。DIF是group-level
      方法，将13个RL模型混入N≈807的focal cohort几乎不改变C%（31.3%→31.0%），但这也意味着无法
      单独评估RL模型的DIF特性。传统检测器（Min-K%，ConStat）在RL模型上的AUROC下降（0.71→0.53,
      0.68→0.51），方向支持"DIF比per-model方法更robust"的claim，但DeLong test p>0.05因为N=13
      power不足。TOST等价性检验inconclusive——CI包含零但也包含meaningful differences。
      在median档下，这个实验被降级到Limitations section作为"directional evidence"，
      reviewers接受reasoning-RL是emerging phenomenon、数据有限的framing，但1位reviewer
      标注"this weakens the practical relevance claim for post-2024 models"。
    tables:
      - name: "Table S1 (Appendix): RL Robustness Comparison"
        content: "AUROC comparison across DIF/Min-K%/ConStat × model type (non-RL, alignment-RL, reasoning-RL)"
    figures_description:
      - "Figure S1: Detection power curve as function of exploitation rate p ∈ [0.4, 1.0], showing DIF maintains >0.50 TPR at p≥0.55 while Min-K% drops below 0.50 at p≤0.7"
    analysis: >
      N=13是致命弱点。实验方向正确但statistical power不足以支撑numbered claim。
      Median档策略：在limitations中honest disclosure "reasoning-RL robustness remains
      an open question due to limited open-weight availability"，同时在main text保留
      alignment-RL的positive result（N=477，C% stable at 31.1%）作为partial evidence。
      Reviewer不会因此reject但会在score中扣分（contributes to 3.25-3.75 range）。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      独立评估ConStat-style perturbation testing在MMLU上的检测力。需要GPU生成语义等价
      reformulations并收集模型响应。
    expected_results:
      status: not_executed
      reason: "GPU budget constraint (80h required) + 依赖LLM paraphrasing pipeline未搭建"
      counterfactual_if_executed:
        n_items_reformulated: 250
        constat_fdr_controlled_detection_rate: 0.42
        constat_auroc_non_rl: 0.68
        constat_auroc_rl: 0.51
        constat_dif_overlap_jaccard: 0.18
        constat_specificity: "high for verbatim contamination, low for capability-driven DIF"
    result_rationale: >
      在median档位下，plan_003a未执行是合理的——paper已pivot away from ensemble detection
      (Claim 2 old) toward diagnostic framing。GPU预算优先分配给plan_002和plan_004。
      ConStat/DVD的AUROC数字已通过文献引用在main text中提供（Blebea et al. 2024），
      无需独立复现。Reviewers可能要求"why not compare directly"但rebuttal可以指向
      ConStat的public results + 不同detection targets（perturbation sensitivity vs
      differential functioning）的conceptual argument。在median档下这不构成reject reason
      但contributes to "thin empirical comparison" concern。
    tables: []
    figures_description: []
    analysis: >
      未执行。对median档outcome的影响：1位reviewer在minor comments中提到"direct comparison
      with ConStat would strengthen the paper"，但接受conceptual distinction argument。
      不是core weakness。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      独立评估DVD generation variance在MMLU上的检测力。需要GPU对10-15个模型生成50次响应。
    expected_results:
      status: not_executed
      reason: "GPU budget constraint (70h required) + 需要open-weight model inference pipeline"
      counterfactual_if_executed:
        n_models: 12
        responses_per_item: 50
        dvd_detection_rate: 0.35
        dvd_auroc: 0.62
        dvd_variant_contamination_sensitivity: 0.71
        dvd_verbatim_contamination_sensitivity: 0.44
    result_rationale: >
      与plan_003a相同逻辑——paper不再追求ensemble detection，DVD作为independent baseline
      的value在current framing下降低。Median档reviewers理解GPU constraint但可能在
      "comparison with existing methods" section标注insufficiency。Rebuttal中可指向
      DVD原始论文结果 + "DIF operates at group level while DVD operates at model level,
      complementary rather than competing"。
    tables: []
    figures_description: []
    analysis: >
      未执行。影响与plan_003a类似，合并为一个reviewer concern："existing method comparison
      is conceptual rather than empirical"。Median档下这是minor issue，不影响accept/reject。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      融合DIF + ConStat + DVD为多信号ensemble。依赖plan_003a和plan_003b。
    expected_results:
      status: not_executed
      reason: "Dependencies plan_003a and plan_003b not executed; ensemble claim dropped from paper"
      paper_status: "Dropped to future work section"
    result_rationale: >
      Plan_003c在paper pivot后被完全dropped。Paper从"we detect contamination better via
      ensemble"转向"we characterize benchmark properties via DIF"。Median档reviewers
      不会miss这个experiment因为paper不再claim ensemble contribution。但1位reviewer
      可能在"future work"评论中写"the ensemble direction seems promising and its absence
      weakens the practical impact"——这contributes to actionability concern。
    tables: []
    figures_description: []
    analysis: >
      完全dropped。无直接影响，但间接加剧Claim 4 actionability的weakness——如果ensemble
      存在，actionability story会更强。Median档下这是background weakness，不是explicit
      reviewer complaint。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      在GSM8K上复现DIF分析，使用GSM1K作为contamination ground truth。包括temporal DIF、
      semi-synthetic validation、GSM1K correlation三步。
    expected_results:
      step1_temporal_dif:
        n_items: 1319
        n_ref: 1017
        n_foc: 804
        standard_c_pct: 18.9
        external_c_pct: 47.4
        sanity_c_pct: 0.3
        standard_external_spearman: 0.926
      step2_semi_synthetic:
        standard_delta_tpr_p05: 0.508
        standard_delta_tpr_p10: 0.818
        external_delta_tpr_p10: 0.517
        fpr_stable: true
      step3_gsm1k_correlation:
        n_matched_models: 33
        pearson_r: -0.478
        pearson_p: 0.005
        spearman_rho: -0.403
        spearman_p: 0.02
        partial_r_controlling_accuracy: -0.385
        partial_p: 0.027
        direction: "NEGATIVE — opposite to naive contamination hypothesis"
        interpretation: "DIF-C items ANTI-correlate with contamination gap; DIF captures capability differential, not contamination per se"
        ci_95_pearson: [-0.71, -0.16]
        ci_95_spearman: [-0.66, -0.03]
        cook_d_max: "deepseek-math-7b-rl"
        leave_one_out_robust: true
    result_rationale: >
      GSM8K的C%=18.9%显著低于MMLU的31.3%，在median档下被1位reviewer质疑为"DIF may be
      benchmark-specific — lower rates on math benchmarks suggest the phenomenon is
      modulated by domain characteristics"。这是valid concern因为GSM8K是单领域数学题，
      item homogeneity高于MMLU的57-subject结构。GSM1K correlation的r=-0.478方向为负
      （与contamination hypothesis相反），被demoted to exploratory per Dream #6 consensus。
      N=33 + wide CI [-0.71, -0.16]使这个结果在median档下不被视为strong evidence。
      Semi-synthetic ΔTPR=+0.818则是positive result，支撑Claim 3的framework portability。
      Median档下Step 2被接受，Step 3被标注"exploratory, underpowered"。
    tables:
      - name: "Table 3: Cross-Benchmark DIF Summary"
        content: "GSM8K temporal DIF: C%=18.9%, ΔTPR=+0.818, GSM1K r=-0.478"
    figures_description:
      - "Figure 3: GSM8K DIF detection power curve (ΔTPR vs injection rate p), showing monotonic increase with cross-subject matching maintaining ΔFPR≈0"
    analysis: >
      Mixed result。Semi-synthetic validation强化Claim 3，但GSM1K negative correlation
      + lower C%创造了tension。Median档reviewers接受"DIF captures differential functioning
      broadly, not just contamination"的framing，但GSM1K result被从abstract/conclusion
      移除。HellaSwag C%=17.9%（来自plan_028）进一步支持"lower rates on non-MMLU benchmarks"
      的pattern，给reviewer ammunition质疑MMLU-specificity。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      在MMLU上拟合bifactor IRT模型（general factor + 57 subject-specific factors），选择
      anchor items进行fixed-parameter calibration equating。
    expected_results:
      status: attempted_and_killed
      convergence:
        full_57_subject: "failed to converge after 5000 EM iterations"
        reduced_10_subject: "converged but poor fit"
        reduced_5_subject: "converged, marginal fit"
      fit_statistics_5_subject:
        rmsea: 0.078
        cfi: 0.724
        tli: 0.698
        srmr: 0.091
      anchor_item_selection:
        n_candidate_anchors: 312
        anchor_stability_criterion: "DIF A-class + discrimination > 0.8"
        anchor_coverage: "38/57 subjects represented"
      equating_pilot:
        status: "abandoned — fit insufficient for reliable equating"
        rho_equated_vs_original: null
        decision: "killed; within-subject DIF (plan_014) provides alternative without requiring full IRT model"
    result_rationale: >
      Bifactor IRT在MMLU上失败是structurally predictable的：57个subjects × 12508 items的
      bifactor model需要估计~57 specific factors + 1 general factor + ~25000 item parameters，
      计算上不可行且psychometrically questionable（MMLU的57 subjects不是designed dimensions）。
      在median档下，这个failure被report为"empirical observation that motivates future
      multidimensional IRT work"，positioned as honest negative result。Plan_014的
      within-subject DIF（C%=38.1%）提供了alternative path证明DIF不依赖于cross-subject
      matching artifact。Reviewer可能质疑"why attempt bifactor at all"但不会因failure
      扣分——negative results是legitimate contribution if honestly reported。
    tables: []
    figures_description: []
    analysis: >
      Expected failure。在median档下被移入limitations section作为"our attempts to improve
      IRT model specification did not succeed, but within-subject validation (plan_014)
      confirms DIF findings are not artifacts of cross-subject matching"。Contributes
      to the "three structural constraints" narrative。不直接影响reviewer score。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      为DIF-flagged MMLU items生成替换题目，通过student simulation进行difficulty calibration。
    expected_results:
      status: blocked
      blocking_dependency: "plan_005 (bifactor IRT) killed — no equating framework for calibration"
      alternative_path: "plan_032 DIF-cleaned demonstration provides actionability evidence without item replacement"
      counterfactual_if_executed:
        n_items_generated: 500
        difficulty_correlation_prompt: 0.32
        difficulty_correlation_simulation: 0.71
        construct_fidelity_human_eval: 0.64
        replacement_set_rho_vs_original: 0.989
    result_rationale: >
      Plan_006被plan_005 failure阻塞是合理的——没有可靠的IRT equating framework，
      replacement items无法calibrated到同一量表上。在median档下，paper不claim
      "benchmark regeneration"（已从original framing dropped），改为claim
      "DIF as diagnostic lens"。Plan_032的DIF-cleaned demonstration（89.5% models
      shift ≥5 ranks, z=8.5 vs random）提供了不需要item replacement的actionability
      evidence。Reviewers不会miss这个experiment因为paper不再promise regeneration。
    tables: []
    figures_description: []
    analysis: >
      Blocked。Paper已完全pivot away from regeneration claim。在median档下无影响。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      实现Sinharay et al. (2006)的cumulative Bayesian DIF priors，模拟4次连续benchmark
      administrations，展示累积evidence带来的power improvement。
    expected_results:
      simulation_design:
        n_administrations: 4
        n_items_per_admin: 500
        n_models_per_admin: 200
        effect_sizes: [0.8, 1.0, 1.2, 1.4, 1.6]
        contamination_prevalence: 0.15
      power_results:
        single_admin_tpr_d10: 0.397
        cumulative_2_admin_tpr_d10: 0.548
        cumulative_3_admin_tpr_d10: 0.681
        cumulative_4_admin_tpr_d10: 0.739
        single_admin_tpr_d14: 0.682
        cumulative_3_admin_tpr_d14: 0.841
      fpr_all_conditions: "<0.06"
      prior_weight_sensitivity:
        informative_prior_tpr_3admin: 0.681
        flat_prior_tpr_3admin: 0.523
        prior_impact: "+0.158 TPR from informative priors"
      bayes_factor_threshold:
        bf_gt_3_pct_3admin: 0.58
        bf_gt_10_pct_3admin: 0.41
    result_rationale: >
      Cumulative Bayesian DIF在simulation中表现符合预期：3次administration后power从0.40
      提升到0.68（δ=1.0），符合Sinharay et al.的理论预测。但这是pure simulation——没有在
      real METABENCH data上进行temporal sliding window validation。在median档下，
      这个experiment被放入appendix作为"methodological extension for longitudinal benchmark
      monitoring"。Reviewers将其视为incremental：1位reviewer写"the Bayesian accumulation
      is a known technique; the contribution here is applying it to the LLM context,
      which is straightforward"。Proposition 1的formal proof（cross-subject ΔFPR=0）
      被同一位reviewer称为"incremental"——这两个方法贡献合并被视为不够novel。
    tables:
      - name: "Table S2 (Appendix): Cumulative Bayesian DIF Power"
        content: "TPR × n_administrations × effect_size matrix + BF threshold analysis"
    figures_description:
      - "Figure S2: Power accumulation curves across 4 administrations at δ={0.8, 1.0, 1.2, 1.4, 1.6}, showing diminishing returns after 3rd administration"
    analysis: >
      Simulation-only结果在median档下被视为supplementary。主要value是为Discussion中
      "longitudinal benchmark monitoring protocol"提供quantitative grounding。
      不直接影响reviewer score但strengthens the "audit protocol" narrative for Claim 4。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      分析benchmark在progressive item replacement下的validity degradation。模拟5%-50%
      replacement rate，测量ranking stability、score reliability、construct coverage。
    expected_results:
      replacement_rates: [0.05, 0.10, 0.15, 0.20, 0.30, 0.50]
      ranking_stability_rho:
        pct_05: 0.9994
        pct_10: 0.9981
        pct_15: 0.9963
        pct_20: 0.9938
        pct_30: 0.9867
        pct_50: 0.9714
      score_reliability_alpha:
        original: 0.962
        pct_05: 0.959
        pct_10: 0.955
        pct_15: 0.950
        pct_20: 0.944
        pct_30: 0.929
        pct_50: 0.898
      construct_coverage:
        pct_subjects_ge80pct_items_at_20pct: 0.947
        pct_subjects_ge80pct_items_at_50pct: 0.614
        first_subject_below_80pct: "formal_logic (N=126, loses >25 items at 20%)"
      theoretical_bound:
        rho_lower_bound_at_r: "ρ ≥ 1 - r × (1 - α_replacement) / α_original, approximate"
        validity_threshold: "ρ < 0.99 at ~22% replacement for MMLU"
      comparison_with_plan_032:
        plan_032_rho: 0.9965
        graceful_degradation_predicted_rho_at_31pct: 0.9856
        discrepancy: "DIF-targeted removal is LESS disruptive than random replacement (0.9965 > 0.9856), consistent with plan_020 circularity ablation"
    result_rationale: >
      Graceful degradation分析在median档下支撑"instability ≠ invalidity"叙事：即使移除31%
      items，ρ仍>0.98（random replacement）或>0.996（DIF-targeted removal）。这与plan_017
      的ρ=0.997一致。但reviewer的tension点恰恰在这里："if benchmark is this redundant,
      what's the practical value of identifying unstable items?"至少1位reviewer质疑
      actionability——31% items unstable but rankings barely change，所以who cares？
      Plan_032的cohort asymmetry（2024 Δrank=+73.6）是回应这个质疑的ammunition，但
      在median档下论证力度不够——reviewer要求control for model quality confound。
      Graceful degradation本身被接受为clean supplementary analysis但被移入appendix。
    tables:
      - name: "Table S3 (Appendix): Graceful Degradation Metrics"
        content: "Replacement rate × ρ × α × construct coverage matrix"
    figures_description:
      - "Figure S3: Validity degradation curves — ρ and α as function of replacement rate, with 95% CI bands from bootstrap"
    analysis: >
      Clean supplementary result。在median档下strengthens "instability ≠ invalidity"
      narrative但simultaneously feeds reviewer skepticism about practical significance。
      这是median档的核心tension：数据越是显示ranking robustness，actionability argument
      越难卖。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      实现Tutz & Berger (2016) Item-Focused Trees作为categorical DIF的alternative，
      将model release date作为continuous covariate。
    expected_results:
      model:
        splitting_variable: "release_date (continuous, days since 2023-01-01)"
        tree_depth: 3
        n_terminal_nodes: 5
        primary_split: "2023-08-15 (separating early-2023 from late-2023+)"
        secondary_split: "2024-02-01 (within late-2023+ group)"
      dif_detection:
        n_items_significant: 3421
        pct_items_significant: 27.4
        overlap_with_mh_c: 0.823
        jaccard_with_mh_c: 0.691
        items_only_ift: 487
        items_only_mh: 984
      temporal_gradient:
        effect_size_vs_time_distance_r: 0.312
        effect_size_vs_time_distance_p: "<0.001"
        early_2023_vs_late_2024_mean_dif: 1.87
        adjacent_half_years_mean_dif: 0.94
      model_fit:
        deviance_explained_r2: 0.031
        aic_vs_categorical: "IFT AIC=48921 vs MH-categorical AIC=49103 (marginal improvement)"
      conclusion: "IFT confirms temporal gradient but adds limited explanatory power beyond categorical MH"
    result_rationale: >
      IFT在median档下是"nice to have"的robustness check。与MH-DIF的82.3% overlap确认
      categorical temporal split不是arbitrary——continuous analysis recovers similar items。
      Primary split at ~2023-08-15大致对应LLM rapid improvement期（Llama-2 release附近），
      但R²=0.031说明release date alone解释DIF variation极少。Reviewer视为incremental：
      "confirms the categorical finding, but the continuous approach doesn't add substantial
      new insight"。在median档下被移入appendix。不影响任何core claim但provides defense
      against "arbitrary cohort split" criticism。
    tables:
      - name: "Table S4 (Appendix): IFT vs MH-DIF Comparison"
        content: "Item overlap, detection rates, split points"
    figures_description:
      - "Figure S4: Item-Focused Tree structure showing primary split at 2023-08-15 and DIF effect size gradient across temporal nodes"
    analysis: >
      Supplementary robustness check。Median档下reviewers不explicitly request这个分析
      但它preemptively addresses "arbitrary cohort boundary" concern。Value在于showing
      temporal DIF是gradient而非artifact of specific cutoff。被appendix化对page budget
      有利。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      在architecture-homogeneous子群（decoder-only）上运行DIF，测试去除architecture
      heterogeneity是否改善IRT fit和减少spurious DIF。
    expected_results:
      architecture_composition:
        total_models: 5227
        decoder_only: 5226
        non_decoder: 1
        pct_decoder_only: 99.98
        non_decoder_model: "instructor-xl (encoder)"
      decoder_only_dif:
        c_pct: 31.3
        c_pct_change_from_full: 0.0
        jaccard_with_full: 1.0
        n_flag_changes: 2
      irt_fit_comparison:
        full_population_rmsea: 0.052
        decoder_only_rmsea: 0.052
        full_population_cfi: 0.681
        decoder_only_cfi: 0.681
        fit_change: "negligible"
      conclusion: "Architecture heterogeneity is empirically irrelevant for METABENCH MMLU — population is 99.98% decoder-only"
    result_rationale: >
      这是最clean的"non-issue"实验：METABENCH MMLU几乎entirely decoder-only，移除唯一一个
      non-decoder模型对C%和DIF flags毫无影响（Jaccard=1.0）。在median档下，这个result被
      reviewers接受为"architecture confound is not a concern for this specific dataset"。
      但IRT fit（RMSEA=0.052, CFI=0.681）仍然poor——这不是architecture问题而是MMLU本身的
      57-subject multidimensionality。Reviewers接受architecture defense但标注IRT misfit
      作为general limitation。在median档下，这个实验在main text用一句话dismiss architecture
      concern，detail在appendix。
    tables:
      - name: "Inline: Architecture composition note"
        content: "One sentence in main text: 'METABENCH MMLU is 99.98% decoder-only (5,226/5,227); excluding the single encoder model changes nothing (Jaccard=1.0).'"
    figures_description: []
    analysis: >
      Trivially positive result。在median档下是effective preemptive defense，占用minimal
      page space。IRT fit的poor numbers（CFI=0.681）需要在limitations中discuss，但
      architecture不是原因。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: >
      在real METABENCH response matrix中注入known contamination，测量DIF detection power
      under controlled ground truth。
    expected_results:
      temporal_external_matching:
        tpr_p0_baseline: 0.326
        tpr_p03: 0.548
        tpr_p05: 0.834
        tpr_p07: 0.990
        tpr_p10: 1.000
        fpr: 0.314
        delta_tpr_p05: 0.508
        delta_tpr_p10: 0.674
        delta_fpr: 0.000
      ability_external_matching:
        tpr_p0_baseline: 0.498
        tpr_p10: 0.800
        fpr: 0.493
        delta_tpr_p10: 0.302
      within_subject_matching:
        fpr_inflation_p10: "+0.186"
        matching_variable_contamination: true
      cross_subject_matching:
        delta_fpr_all_subjects: 0.000
        delta_tpr_cross_gt_within: "4/5 subjects"
      injection_parameters:
        n_clean_items: 500
        n_injected_items: 150
        exploitation_rates: [0.0, 0.3, 0.5, 0.7, 1.0]
        focal_group_contaminated: true
    result_rationale: >
      Semi-synthetic validation是Claim 3的core evidence，在median档下被接受as solid
      methodological contribution。ΔTPR=+0.508 at p=0.5展示meaningful detection power，
      cross-subject matching的ΔFPR=0.000是key technical insight。Median档的friction：
      1位reviewer指出"the injection mechanism (incorrect→correct flipping) is a
      simplification that may not reflect real contamination patterns"——real contamination
      可能改变response confidence而非binary correctness。这是acknowledged limitation
      但不构成rejection reason。Claim 3的"validation framework"contribution被接受，
      但Proposition 1的formal proof（ΔFPR=0 algebraic derivation）被1位reviewer称为
      "follows straightforwardly from the independence of cross-subject scores and
      injected items"——即incremental formalization。
    tables:
      - name: "Table 4: Semi-Synthetic Validation Results"
        content: "Matching strategy × injection rate → TPR/FPR/ΔTPR matrix + cross-subject vs within-subject comparison"
    figures_description:
      - "Figure 4: Detection power curves — ΔTPR vs injection rate p for temporal-external and ability-external matching, with 95% CI bands"
      - "Figure 5: FPR stability — cross-subject matching maintains ΔFPR=0 across all injection rates while within-subject inflates by +0.186"
    analysis: >
      Claim 3的主要evidence。Median档reviewers接受framework utility但要求更多prior work
      对比——"how does this compare to existing semi-synthetic contamination benchmarks
      (e.g., Oren et al. 2023)?"。Rebuttal需补充2-3个semi-synthetic prior work的
      explicit comparison table。ΔFPR=0 across-subject matching是genuine technical
      contribution但formalization被视为incremental。

  - name: multi_benchmark_temporal_dif
    plan_id: plan_028
    description: >
      在METABENCH中查找additional benchmark response matrices（ARC, HellaSwag, WinoGrande,
      TruthfulQA），运行temporal DIF分析。
    expected_results:
      benchmarks:
        mmlu:
          n_items: 12508
          n_ref: 1080
          n_foc: 807
          pct_c: 31.3
          random_pct_c: 0.18
          bootstrap_ci: [29.38, 38.05]
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
          random_pct_c: 0.60
        gsm8k:
          n_items: 1319
          n_ref: 1017
          n_foc: 804
          pct_c: 18.9
          random_pct_c: 0.30
        hellaswag:
          n_items: 10042
          n_ref: 1080
          n_foc: 807
          pct_c: 17.9
          random_pct_c: 0.28
      summary:
        cross_benchmark_range: "17.9%–31.3%"
        all_random_controls_below_1pct: true
        min_enrichment_ratio: 45
        n_benchmarks: 6
        two_tier_pattern: "knowledge benchmarks (MMLU/WinoGrande/TruthfulQA/ARC) ≈ 27-31%; skill benchmarks (GSM8K/HellaSwag) ≈ 18-19%"
    result_rationale: >
      6-benchmark replication是median档下被接受的strength之一。所有benchmarks显示temporal DIF
      远高于random control（enrichment ≥45×），证明DIF不是MMLU-specific artifact。但median档的
      key friction：HellaSwag和GSM8K的C%显著低于MMLU（17-19% vs 31%），被1-2位reviewers质疑为
      "DIF sensitivity may be benchmark-specific — what structural property drives the 2× difference?"
      回应需要指向benchmark characteristics：GSM8K是single-domain math，HellaSwag有10K items
      （statistical dilution），两者的item homogeneity高于MMLU的57-subject heterogeneity。
      但这个解释是post-hoc的，reviewer可能不fully satisfied。另外1位reviewer指出
      "the two-tier pattern could reflect genuine domain differences in temporal stability
      rather than methodological artifact"——这实际上strengthens the finding但reviewer
      frames it as limitation。
    tables:
      - name: "Table 5: Cross-Benchmark Temporal DIF"
        content: "6 benchmarks × C% × random control × enrichment ratio"
    figures_description:
      - "Figure 6: Cross-benchmark C% comparison with random baselines, showing consistent temporal DIF signal across all 6 benchmarks with 2-tier pattern annotation"
    analysis: >
      Strong replication evidence。Median档下6-benchmark coverage被接受为"broadest DIF
      analysis of LLM benchmarks to date"，但HellaSwag/GSM8K的lower C%给reviewer
      留下"benchmark-specific"疑虑。Rebuttal需要1段structured argument about why
      knowledge-heavy vs skill-heavy benchmarks show different DIF rates。这是median档
      3-5个rebuttal issues之一。

  - name: permutation_null_c_rate
    plan_id: plan_029
    description: >
      1000次permutation test：随机重新分配temporal labels（保持N_ref=1080, N_foc=807），
      每次运行MH-DIF，建立C%的null distribution。
    expected_results:
      n_permutations: 1000
      null_distribution:
        mean_c_pct: 0.47
        sd_c_pct: 0.13
        median_c_pct: 0.45
        min_c_pct: 0.10
        max_c_pct: 1.02
        q95_c_pct: 0.71
        q99_c_pct: 0.84
      observed_c_pct: 31.3
      z_score: 237.2
      p_value: "<0.001 (all 1000 permutations below observed)"
      empirical_p: 0.000
      effect_size_ratio: "observed/null_mean = 66.6×"
      per_family_stratified:
        status: "not executed pre-submission"
        rationale: "identified as potential rebuttal experiment; requires grouping models by family and permuting within strata"
        estimated_null_mean_if_stratified: 0.52
        estimated_z_if_stratified: ">200"
    result_rationale: >
      Permutation null在median档下成功确认31.3%远超chance（p<0.001, z>200）。Null distribution
      的mean C%=0.47%与within-cohort random split的0.18%在同一量级，内部一致。这直接回应
      "is 31% above chance?"质疑。但median档的nuance：1位reviewer接受permutation null但
      要求additional controls——specifically per-family stratified permutation，因为如果
      model families cluster by temporal cohort（2023多Llama-2，2024多Llama-3），简单
      permutation可能underestimate null。这成为rebuttal experiment需求。Plan_022的
      de-duplication分析（K=20: 29.1% vs random 30.9%）provides partial defense，但
      reviewer要求的是stratified permutation而非cap-based de-duplication。这是median档
      3-5个rebuttal issues之一。
    tables:
      - name: "Table 6: Permutation Null Distribution"
        content: "Null C% summary statistics + observed vs null comparison + z-score + empirical p"
    figures_description:
      - "Figure 7: Permutation null histogram (1000 iterations) with observed C%=31.3% marked, showing complete separation between null and observed distributions"
    analysis: >
      Statistically unambiguous result。Median档reviewers接受statistical significance
      但push for stronger controls（per-family stratification）。这是well-targeted reviewer
      request——the paper should preemptively address it using plan_022 de-duplication
      as evidence that family structure doesn't inflate C%, and offer stratified permutation
      as rebuttal experiment if needed。在median档下，plan_029成功但creates a follow-up
      obligation in rebuttal。

  - name: odds_ratio_regression_transparency
    plan_id: plan_030
    description: >
      补充pseudo R²=0.0007的透明度：odds ratio + 95% CI + McFadden/Nagelkerke R² + deviance
      ratio。增加item-level accuracy change predictor。
    expected_results:
      model1_domain_delta:
        predictor: "subject-level accuracy change (2024-2023)"
        mcfadden_r2: 0.0007
        nagelkerke_r2: 0.0012
        aic: 15545.2
        or_per_010_acc_change: 1.55
        or_ci_per_010: [1.19, 2.03]
        interpretation: "10pp domain improvement → 1.55× odds of DIF, but explains <0.2% variance"
      model2_domain_plus_items:
        mcfadden_r2: 0.0423
        nagelkerke_r2: 0.0720
        aic: 14902.3
        domain_delta_or: 0.73
        ctt_difficulty_or: 0.78
        ctt_discrimination_or: 1.51
        simpsons_paradox: true
        interpretation: "Domain accuracy delta REVERSES direction after controlling for item properties — Simpson's paradox"
      model3_item_delta:
        predictor: "item-level accuracy change (per-item 2024-2023 delta)"
        mcfadden_r2: 0.0012
        nagelkerke_r2: 0.0021
        aic: 15536.9
        item_acc_change_or_per_010: 1.08
        item_acc_change_ci: [1.51, 2.96]
      model4_full:
        mcfadden_r2: 0.0434
        nagelkerke_r2: 0.0737
        aic: 14885.4
        item_delta_or: 0.92
        difficulty_or: 0.77
        discrimination_or: 1.54
        lr_test_m3_vs_m4_chi2: 655.53
      simpsons_paradox_narrative: >
        "Domain improvement predicts DIF marginally (OR=1.55), but this relationship
        REVERSES (OR=0.73) after controlling for item difficulty and discrimination.
        Items that are harder and more discriminating are more likely to show DIF,
        regardless of domain-level improvement. The 'models got better' story is a
        Simpson's paradox — improvement concentrates in domains with harder, more
        discriminating items."
    result_rationale: >
      Simpson's paradox是median档下的strong defense line。Domain-level accuracy improvement
      与DIF的marginal association（OR=1.55, R²<0.002）在控制item properties后reverses
      （OR=0.73），证明"models got better"不是DIF的driver——item difficulty和discrimination
      才是。在median档下，这个result被2位reviewers接受为convincing decomposition evidence。
      但1位reviewer质疑："item difficulty may be a mediator rather than confounder —
      DIF items are harder BECAUSE they function differently across cohorts, not vice versa"。
      这是valid methodological point，paper需在limitations中acknowledge endogeneity concern。
      Simpson's paradox被用在rebuttal中作为"second line of defense"（与plan_027 ability
      overlap d=-0.17并用）回应"31% is just capability improvement"质疑。
    tables:
      - name: "Table 7: Logistic Regression Decomposition"
        content: "4 models: domain Δ only → domain Δ + items → item Δ only → item Δ + items; OR, CI, R², AIC for each"
    figures_description:
      - "Figure 8: Simpson's paradox visualization — marginal domain-DIF association (positive slope) reversing to negative after item-property conditioning"
    analysis: >
      Key analytical contribution。在median档下Simpson's paradox被视为paper的most
      surprising finding之一，多数reviewers find it compelling。但endogeneity concern
      prevents full resolution of "why 31%?"——paper需honestly position这as "DIF is
      predominantly item-specific, not domain-driven, but the causal direction between
      item properties and DIF remains ambiguous"。这contributes to causal language
      hedging requirement。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86c5de96-0a39-473d-a4f4-838e19d0fb3c",
  "isSidechain": false,
  "requestId": "req_011CbFsSdTJGKDVYTDFVHsgg",
  "type": "assistant",
  "uuid": "274d07c7-bd27-4d29-95af-249f4c566f8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiDAEySiJeB3pfXVQevE3M",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23066,
      "cache_read_input_tokens": 11841,
      "output_tokens": 20125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 20125,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23066
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claim 1和Claim 3被接受；Claim 2 (meta-critique)被部分reviewers视为obvious；Claim 4 actionability论证需要加强；ρ=0.997的'instability ≠ invalidity'张力未完全化解——至少1位reviewer质疑'if…",
  "leafUuid": "274d07c7-bd27-4d29-95af-249f4c566f8e",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier DIF findings: temporal instability robust, not driven by capability gain",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claim 1和Claim 3被接受；Claim 2 (meta-critique)被部分reviewers视为obvious；Claim 4 actionability论证需要加强；ρ=0.997的'instability ≠ invalidity'张力未完全化解——至少1位reviewer质疑'if…",
  "leafUuid": "274d07c7-bd27-4d29-95af-249f4c566f8e",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier DIF findings: temporal instability robust, not driven by capability gain",
  "sessionId": "937a0eab-90a2-4790-97fd-3c463550c819"
}
```

---
