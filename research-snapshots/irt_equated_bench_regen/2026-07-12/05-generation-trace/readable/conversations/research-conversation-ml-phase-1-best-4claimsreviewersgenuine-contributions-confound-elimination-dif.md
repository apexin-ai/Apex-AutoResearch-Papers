# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有4条claims均被reviewers接受为genuine contributions；confound elimination叙事完全说服；DIF

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/b998fe0e-75c7-4ec3-8520-1897e446d2fd.jsonl`
- **Structured JSON:** [`7fddd021afb2b3052ae2.json`](../../sessions/7f/7fddd021afb2b3052ae2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T14:19:10.490Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T14:19:10.490Z",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有4条claims均被reviewers接受为genuine contributions；confound elimination叙事完全说服；DIF-cleaned demonstration被视为actionable insight而非statistical curiosity\n核心假设：['31% C%被接受为genuine item-level instability（ability confound 2.4pp/7.7%的decomposition evidence足够）', 'Ground truth meta-critique被视为non-obvious的field-wide贡献，而非trivial observation', 'Cross-subject matching ΔFPR=0的Proposition 1被视为methodological novelty', '6-benchmark replication (17.9-31.3%)足以支撑generalizability claim', 'DIF-cleaned MMLU的cohort asymmetry (2024 Δrank=+73.6, z=8.5 vs random)直接回应actionability concern', '10→8页压缩成功，无critical evidence丢失', 'plan_029 permutation null显示observed C%=31.3%远超null distribution（p<0.001）']\n关键指标范围：{'reviewer_avg_score': [3.75, 4.25], 'permutation_null_mean_c_pct': [0.1, 0.5], 'permutation_null_p_value': [0.0, 0.001], 'rebuttal_issues_count': [0, 2], 'claims_accepted_without_caveat': [3, 4], 'page_compression_info_loss_pct': [0, 10], 'meta_analysis_acceptance': ['novel contribution', 'strong accept on this claim']}\n叙事方向：原始framing完全成立——'Psychometric DIF at unprecedented scale reveals 31% temporal instability across 6 benchmarks, provides reusable validation framework, and offers actionable diagnostic lens for benchmark maintenance.' 四条claims按原始强度提出，无需hedge。Proposition 1和DIF-cleaned demonstration作为双重方法论+实证亮点。Systematic confound elimination叙事（6 negative results → what remains is genuine）作为robustness story的backbone。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\nfocus: This is re-dream #8 after major revisions addressing Dream #7's specific weaknesses. Key improvements since Dream #7 (all integrated into paper via P6-P16 patches):\n\n1. **Actionability paradox SOLVED** (was CW1-level concern): NEW plan_032 DIF-cleaned MMLU demonstration shows 89.5% models shift ≥5 ranks, systematic cohort bias (2024 Δrank=+73.6), confirmed DIF-specific by random baseline (z=8.5). This directly answers \"ρ=0.997 means DIF doesn't matter.\"\n\n2. **Proposition 1 (ΔFPR=0 formalized)**: Cross-subject matching now has a formal algebraic proof, not just an empirical observation. Elevates methodological contribution.\n\n3. **Temporal coarseness addressed**: NEW plan_031 6-month window robustness check (C%=34.35%, 181× enrichment) shows DIF is robust to finer temporal granularity.\n\n4. **Subject DIF direction asymmetry** (NEW analytical finding): STEM subjects favor 2024 models (55.4%), Humanities favor 2023 (64.4%) — content-level predictor of DIF direction.\n\n5. **Expanded Related Work**: Added BHI (Blebea et al. 2024), PSN-IRT (Polo et al. 2024), Maeda (2024) — addresses \"thin related work\" concern.\n\n6. **Systematic Confound Elimination narrative**: 6 negative results reframed as systematic exclusion of confounds (architecture, ability, local dependence, IRT misfit, reasoning-RL, ensemble), strengthening the \"what remains is genuine temporal DIF\" argument.\n\n7. **Bootstrap CI on headline C%**: MMLU C%=31.3% [29.5%, 33.1%] with N=1000 model resampling.\n\n8. **Causal language softened** throughout — \"contamination-adjacent\" phrasing replaced with hedged \"differential functioning\" language.\n\n9. **DIF-for-LLMs paragraph** added in Discussion — explicitly addresses what DIF means for machine (vs. human) examinees.\n\n10. **Audit protocol expanded** with code release commitment.\n\n11. **ConStat/DVD comparison visibility increased** — AUROC numbers and Jaccard overlap now in main text.\n\nReviewers should evaluate whether these revisions close the gap from 3.5 to 4.0 (Conference). The paper's strongest path to 4.0: unprecedented scale + cross-subject matching (Proposition 1) + Simpson's paradox + DIF-cleaned demonstration (actionability) + 6-benchmark replication + systematic confound elimination.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n      bootstrap_ci_95:\n      - 29.38\n      - 38.05\n      bootstrap_mean: 33.14\n      bootstrap_sd: 2.3\n      bootstrap_n: 1000\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n- exp_id: plan_031_temporal_granularity\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_full_year:\n      comparison: 2023 vs 2024\n      distance_yr: 1\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.32\n      random_pct_c: 0.02\n    mmlu_half_year:\n      comparison: 2023-H2 vs 2024-H1\n      distance_yr: 0.5\n      n_ref: 1018\n      n_foc: 807\n      pct_c: 34.35\n      random_pct_c: 0.19\n    mmlu_within_2023:\n      comparison: 2023-H1 vs 2023-H2\n      distance_yr: 0.5\n      n_ref: 62\n      n_foc: 1018\n      pct_c: 22.62\n      random_pct_c: 0.18\n      supplementary: true\n    cross_bench_half_year:\n      arc_pct_c: 29.27\n      hellaswag_pct_c: 18.07\n      winogrande_pct_c: 33.62\n      truthfulqa_pct_c: 31.33\n    cross_bench_full_year:\n      arc_pct_c: 26.88\n      hellaswag_pct_c: 17.89\n      winogrande_pct_c: 30.31\n      truthfulqa_pct_c: 29.74\n    half_year_gt_full_year_all_benchmarks: true\n    dif_saturates_within_6mo: true\n- exp_id: plan_032_dif_cleaned_mmlu\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_items_full: 12508\n    n_items_cleaned: 8590\n    n_items_removed: 3918\n    pct_removed: 31.3\n    spearman_rho: 0.9965\n    rank_change_std: 127.1\n    rank_change_min: -589\n    rank_change_max: 849\n    pct_change_ge5: 89.5\n    pct_change_ge10: 79.5\n    pct_change_ge20: 66.4\n    pct_change_ge50: 41.9\n    pct_change_ge100: 24.8\n    top100_pct_ge10: 18\n    top500_pct_ge10: 47.2\n    cohort_2023_mean_change: -22.56\n    cohort_2023_median_change: -5\n    cohort_2024_mean_change: 73.6\n    cohort_2024_median_change: 11\n    systematic_bias: DIF items favor 2024 models; cleaning hurts 2024 +73.6 avg, helps\n      2023 -22.6 avg\n    top_hurt_families:\n      phi-3: 258.35\n      command-r: 235\n      solar: 149.15\n      llama-3: 120.86\n    top_benefit_families:\n      mistral-0.1: -60.32\n      mistral: -53.27\n      zephyr: -29.94\n      gemma-2: -28.78\n    removed_items_harder: true\n    removed_mean_difficulty: 0.409\n    cleaned_mean_difficulty: 0.46\n    random_baseline_20trials:\n      rank_change_std:\n        mean: 60.2\n        std: 7.8\n      mean_abs_rank_change:\n        mean: 36\n        std: 3.6\n      pct_change_ge100:\n        mean: 8.5\n        std: 2\n      cohort_2023_mean_change:\n        mean: 0.4\n        std: 4.1\n      cohort_2024_mean_change:\n        mean: 2.8\n        std: 21.2\n    dif_vs_random_z_scores:\n      rank_change_std_z: 8.5\n      mean_abs_change_z: 10.7\n      pct_ge100_z: 8.2\n      cohort_2023_z: -5.6\n      cohort_2024_z: 3.3\n      cohort_asymmetry_gap_z: 4.4\n- exp_id: plan_033_subject_dif_concentration\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_subjects: 57\n    all_subjects_have_dif: true\n    mean_pct_c: 30.6\n    median_pct_c: 29.7\n    sd_pct_c: 5.5\n    range_pct_c:\n    - 20.7\n    - 48.4\n    top3_subjects:\n      business_ethics: 48.4\n      human_aging: 41.9\n      formal_logic: 40.4\n    bottom3_subjects:\n      computer_security: 20.7\n      marketing: 20.9\n      management: 21.7\n    domain_pct_c:\n      STEM: 30.9\n      Humanities: 31.1\n      Social_Science: 31.6\n    stem_vs_humanities_p: 0.611\n    kruskal_wallis_p: 0.78\n    logistic_regression:\n      difficulty_OR: 0.086\n      discrimination_OR: 57.2\n      pseudo_r2: 0.042\n    excess_dif_subjects:\n    - professional_law\n    - human_aging\n    - world_religions\n    - business_ethics\n    - professional_medicine\n    overall_pct_favor_2024: 43.9\n    temporal_asymmetry:\n      STEM_pct_favor_2024: 55.4\n      Humanities_pct_favor_2024: 35.6\n      Social_Science_pct_favor_2024: 42\n    unidirectional_subjects:\n      world_religions:\n        pct_favor_2024: 16.9\n      logical_fallacies:\n        pct_favor_2024: 20\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T14:19:10.493Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T14:19:10.493Z",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T14:19:10.521Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有4条claims均被reviewers接受为genuine contributions；confound elimination叙事完全说服；DIF-cleaned demonstration被视为actionable insight而非statistical curiosity
核心假设：['31% C%被接受为genuine item-level instability（ability confound 2.4pp/7.7%的decomposition evidence足够）', 'Ground truth meta-critique被视为non-obvious的field-wide贡献，而非trivial observation', 'Cross-subject matching ΔFPR=0的Proposition 1被视为methodological novelty', '6-benchmark replication (17.9-31.3%)足以支撑generalizability claim', 'DIF-cleaned MMLU的cohort asymmetry (2024 Δrank=+73.6, z=8.5 vs random)直接回应actionability concern', '10→8页压缩成功，无critical evidence丢失', 'plan_029 permutation null显示observed C%=31.3%远超null distribution（p<0.001）']
关键指标范围：{'reviewer_avg_score': [3.75, 4.25], 'permutation_null_mean_c_pct': [0.1, 0.5], 'permutation_null_p_value': [0.0, 0.001], 'rebuttal_issues_count': [0, 2], 'claims_accepted_without_caveat': [3, 4], 'page_compression_info_loss_pct': [0, 10], 'meta_analysis_acceptance': ['novel contribution', 'strong accept on this claim']}
叙事方向：原始framing完全成立——'Psychometric DIF at unprecedented scale reveals 31% temporal instability across 6 benchmarks, provides reusable validation framework, and offers actionable diagnostic lens for benchmark maintenance.' 四条claims按原始强度提出，无需hedge。Proposition 1和DIF-cleaned demonstration作为双重方法论+实证亮点。Systematic confound elimination叙事（6 negative results → what remains is genuine）作为robustness story的backbone。

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


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "661fdeb0-d532-46f4-82be-f4084cc4b05b",
  "type": "user",
  "uuid": "412b95e5-1f92-439f-acaa-13de53d9b632",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T14:19:10.519Z_

```json
{
  "parentUuid": "412b95e5-1f92-439f-acaa-13de53d9b632",
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
  "uuid": "ac7c4068-5d53-4d90-a06d-06317a144adf",
  "timestamp": "2026-05-21T14:19:10.519Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T14:19:10.519Z_

```json
{
  "parentUuid": "ac7c4068-5d53-4d90-a06d-06317a144adf",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "faea48df-7e4f-4945-9182-64498dab8a8a",
  "timestamp": "2026-05-21T14:19:10.519Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有4条claims均被reviewers接受为genuine contributions；confound elimination叙事完全说服；DIF-cleaned demonstration被视为actionable insight而非statistical curiosity 核心假设：['31% C…",
  "leafUuid": "faea48df-7e4f-4945-9182-64498dab8a8a",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF analysis of LLM benchmarks reveals temporal instability",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd"
}
```

---

### Assistant

_source line 8 · 2026-05-21T14:20:05.425Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, under the "best" tier assumptions. I need to produce a single YAML block with predicted results for each planned experiment, including result_rationale explaining why these results would occur under the best tier.

Let me go through each planned experiment:

1. **plan_001** - real_data_dif_mmlu - Already DONE in registry
2. **plan_002** - rl_robustness_validation - planned
3. **plan_003a** - constat_perturbation_eval - planned


4. **plan_003b** - dvd_generation_variance_eval - planned
5. **plan_003c** - ensemble_fusion - planned
6. **plan_004** - cross_benchmark_gsm8k - Already DONE in registry
7. **plan_005** - bifactor_irt_equating_pilot - planned
8. **plan_006** - item_generation_calibration - planned
9. **plan_007** - cumulative_bayesian_dif - planned
10. **plan_008** - graceful_degradation_analysis - planned
11. **plan_009** - item_focused_trees - planned
12. **plan_010** - architecture_strat - planned
13. **plan_011** - semi_synthetic_contamination_validation - Already DONE in registry
14. **plan_028** - multi_benchmark_temporal_dif - Already DONE in registry
15. **plan_029** - permutation_null_c_rate - planned
16. **plan_030** - odds_ratio_regression_transparency - Already DONE in registry

Now I need to filter this list to focus only on the experiments marked as planned, since the user is asking for detailed data on each planned experiment in the experiment_plan.

Looking through the full list, I see that plan_001 through plan_010, plus plan_011, plan_028, plan_029, and plan_030 all show status as planned in the experiment_plan, even though many of them already have completed results in the registry. The user wants me to generate predictions for all of these planned experiments, but I need to be careful: for those with existing registry results, I should predict values consistent with the actual outcomes rather than simply copying them, since this is about what the best tier would predict. For the ones without results yet, I'll predict what would likely happen based on the experimental design. I'm now cross-referencing the experiment plan against the registry to distinguish which experiments have actual results versus those needing predicted outcomes under the best-tier scenario. Most experiments show completed status with concrete data, though a few like plan_002 through plan_005 remain unfinished and will need plausible results that align with the best-tier narrative. I'm realizing the distinction here—the user wants detailed data for each planned experiment, including the ones that were killed or never executed. In the best-tier scenario, I should imagine what the full dataset would look like if all experiments had been completed successfully, since that represents the ideal paper reception where all claims are convincingly supported.

Writing the YAML structure... % as genuine

For plan_002 (rl_robustness, planned but described as N=13 underpowered):
- In best tier: even with N=13, the directional evidence is there. DIF flags are stable when RL models added to cohort. Traditional detectors degrade on reasoning-RL models.
- But wait - in the project context it says "RL robustness: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim." So in the best tier, this is acknowledged as underpowered but the directional result supports the narrative.

For plan_003a/b/c (ensemble, never executed):
- In project context: "plan_003a/b/c never executed. Future work."
- In best tier: these are noted as future work, reviewers accept this.

For plan_004 (done, GSM8K):
- Registry data available. r=-0.478 anti-correlating with GSM1K gap.

For plan_005 (bifactor, killed):
- Registry shows PREPARING, killed. In best tier: bifactor fit was insufficient, motivating the pivot to DIF-as-diagnostic.

For plan_006 (item generation):
- Depends on plan_005 which was killed. So this is also not viable.

For plan_007 (cumulative Bayesian DIF, simulation only):
- In best tier: simulation shows power improvement from 0.40 to 0.70 across 3 administrations.

For plan_008 (graceful degradation):
- Depends on plan_005/006. In best tier: the analysis shows validity metrics degrade gracefully.

For plan_009 (item focused trees):
- In best tier: continuous temporal covariate confirms categorical DIF findings.

For plan_010 (architecture-stratified DIF):
- Resolved.

For plan_010 (architecture-stratified DIF, resolved):
- 99.98% decoder-only, Jaccard=1.0. In best tier: this completely resolves architecture heterogeneity concern.

For plan_011 (semi-synthetic, done):
- ΔTPR=+0.674 at p=1.0, cross-subject ΔFPR=0.000.

For plan_028 (multi-benchmark, done):
- 6 benchmarks, C% 17.9-31.3%.

For plan_029 (permutation null):
- In best tier assumptions: observed C%=31.3% far exceeds null distribution (p<0.001).
- Null mean C% in [0.1, 0.5] per key metrics.

For plan_030 (odds ratio, done):
- Simpson's paradox confirmed, McNemar's test validates the effect.
- R² improves from 0.0007 to 0.0423 when accounting for stratification.

Now I'm structuring the full YAML output with expected results, rationale, tables, figures, and analysis for each plan, making sure to expand the detailed data as requested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faea48df-7e4f-4945-9182-64498dab8a8a",
  "isSidechain": false,
  "requestId": "req_011CbFrpMxsmUdRowo4XKfvJ",
  "type": "assistant",
  "uuid": "8abfaeaa-8513-4852-a459-946b2162ff7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UPHMryoWCfaNKPE87RjMU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22924,
      "cache_read_input_tokens": 11841,
      "output_tokens": 24128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 24128,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22924
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

_source line 9 · 2026-05-21T14:27:19.769Z_

```yaml
tier: best
narrative_guidance: >
  原始framing完全成立。31% C%被接受为genuine temporal instability，四条claims按原始强度提出无需hedge。
  Permutation null (p<0.001)、6-benchmark replication (17.9-31.3%)、ability confound decomposition (2.4pp/7.7%)、
  DIF-cleaned demonstration (z=8.5 cohort asymmetry) 构成四重evidence chain。
  Systematic confound elimination叙事（architecture=99.98% decoder-only, ability d=-0.17, local independence Q3=0.009,
  model independence C%≤random at every K, threshold robustness 10-49%, multiple testing BH removes 3/3918）
  被视为convincing robustness backbone。Proposition 1 (ΔFPR=0) 和 DIF-cleaned MMLU demonstration
  作为双重方法论+实证亮点。10→8页压缩成功，无critical evidence丢失。
  Reviewers平均分3.75-4.25，0-2个rebuttal issues，3-4条claims accepted without caveat。

imagined_experiments:

  ##############################################################################
  # plan_001: Primary DIF analysis on MMLU — LOAD-BEARING EXPERIMENT
  ##############################################################################
  - name: "real_data_dif_mmlu"
    plan_id: "plan_001"
    description: >
      Apply MH-DIF to METABENCH MMLU response matrix (5,219 models × 12,508 items).
      Temporal cohort (2023 vs 2024-H1), ability-quintile cohort, within-family confound control,
      domain-specificity analysis, random-split sanity check.
    expected_results:
      temporal_cohort:
        n_ref: 1080
        n_foc: 807
        ets_c_pct: 31.3
        ets_c_count: 3918
        ets_b_pct: 23.4
        ets_a_pct: 45.3
        bootstrap_ci_95: [29.5, 33.1]
        bootstrap_n: 1000
      ability_cohort:
        ets_c_pct: 2.9
        enrichment_vs_li: 1.19
      within_family:
        llama2_vs_llama3_c_pct: 61.3
        mistral_vs_mixtral_c_pct: 38.7
        llama2v3_n_ref: 161
        llama2v3_n_foc: 308
      domain_specificity:
        spearman_rho_dif_vs_acc_improvement: 0.307
        spearman_p: 0.02
        n_subjects: 57
        all_subjects_have_dif: true
        mean_subject_c_pct: 30.6
        range_subject_c_pct: [20.7, 48.4]
      proxy_validation:
        enrichment_vs_li_temporal: 0.96
        fpr_on_li_clean: 0.318
        li_coverage: 0.738
      sanity:
        random_split_c_pct: 0.18
        temporal_ability_jaccard: 0.014
    result_rationale: >
      在best档下，31.3% C%被完全接受为genuine temporal instability。理由链：
      (1) Random split sanity check C%=0.18%证明MH procedure本身不inflate false positives；
      (2) 与Li et al. enrichment≈0.96是EXPECTED结果（web-overlap labels测量global exposure而非differential contamination），
          reviewers接受这是meta-critique的empirical support而非DIF failure；
      (3) Domain correlation ρ=0.307 (p=0.02)表面上暗示ability confound，但plan_019 item-level decomposition
          将证明domain improvement仅解释2.4pp/7.6%——item-specific instability是dominant signal；
      (4) Within-family Llama-2v3 C%=61.3%高于temporal 31.3%，说明family-level capability gap (d≈-0.99)
          确实inflate DIF，但plan_027将证明temporal cohort d=-0.17时confound仅2.4pp；
      (5) 57个subjects全部有DIF (range 20.7-48.4%)证明instability是benchmark-wide现象，非个别subject artifact。
    tables:
      - title: "Table 1: Temporal DIF Summary — MMLU (5,219 models × 12,508 items)"
        columns: [Cohort, N_ref, N_foc, ETS_A_pct, ETS_B_pct, ETS_C_pct, Random_C_pct, Enrichment_Li]
        rows:
          - [Temporal 2023v2024, 1080, 807, 45.3, 23.4, 31.3, 0.18, 0.96]
          - [Ability Q1vQ5, 2608, 2608, 82.1, 15.0, 2.9, 0.15, 1.19]
          - [Within-family Llama2v3, 161, 308, 18.7, 20.0, 61.3, "--", "--"]
      - title: "Table 2: Domain-Level DIF Distribution (Top/Bottom 5 Subjects)"
        columns: [Subject, N_items, C_pct, Pct_favor_2024, Domain]
        rows:
          - [business_ethics, 100, 48.4, 38.0, Social_Science]
          - [human_aging, 223, 41.9, 34.5, Other]
          - [formal_logic, 126, 40.4, 42.1, Humanities]
          - [professional_medicine, 272, 31.1, 51.2, STEM]
          - [high_school_statistics, 216, 42.0, 55.3, STEM]
          - ["...", "--", "--", "--", "--"]
          - [computer_security, 100, 20.7, 48.1, STEM]
          - [marketing, 234, 20.9, 40.2, Social_Science]
          - [management, 103, 21.7, 43.7, Social_Science]
    figures_description:
      - "Fig 1: Histogram of |Δ_MH| across 12,508 items with ETS A/B/C thresholds annotated. Long right tail shows substantial mass beyond C threshold (|Δ_MH|≥1.5). Random-split overlay (near-zero mass beyond 1.0) as visual contrast."
      - "Fig 2: Subject-level C% heatmap (57 subjects) with domain grouping. Color gradient 20-48%. Annotation: domain means (STEM 30.9%, Humanities 31.1%, Social Science 31.6%) are statistically indistinguishable (KW p=0.78)."
    analysis: >
      plan_001是整个paper的load-bearing experiment。在best档下，reviewer consensus是：
      31.3% temporal instability是empirically robust的primary finding（random split 0.18%排除procedural artifact，
      6-benchmark replication排除MMLU-specific artifact，permutation null p<0.001排除chance）。
      Enrichment≈0.96被正确解读为support for Claim 2 (ground truth meta-critique)而非DIF failure。
      Domain correlation ρ=0.307被acknowleded但item-level decomposition (R²=0.0007)消解了ecological fallacy concern。
      Within-family 61.3%被正确contextualized为high-ability-gap scenario (d=-0.99)，
      与temporal d=-0.17形成informative contrast。

  ##############################################################################
  # plan_002: RL robustness validation — SUPPLEMENTARY, ACKNOWLEDGED UNDERPOWERED
  ##############################################################################
  - name: "rl_robustness_validation"
    plan_id: "plan_002"
    description: >
      Validate DIF robustness to reasoning-RL models (GRPO/PPO). SFT-only baseline,
      alignment-RL (DPO/ORPO N=477), and 10-15 reasoning-RL models added to focal cohort.
      Traditional detectors (Min-K%, ConStat) run on individual RL models.
    expected_results:
      sft_baseline:
        n_models: 312
        cohort_c_pct: 30.8
      alignment_rl_cohort:
        n_models: 477
        cohort_c_pct: 31.1
        jaccard_vs_sft_baseline: 0.89
      reasoning_rl_augmented:
        n_rl_models_added: 13
        total_focal_n: 820
        cohort_c_pct: 31.2
        jaccard_vs_baseline: 0.94
        delta_c_pct_vs_no_rl: 0.1
      traditional_detector_degradation:
        min_k_auroc_on_sft: 0.72
        min_k_auroc_on_rl: 0.51
        constat_auroc_on_sft: 0.68
        constat_auroc_on_rl: 0.43
        delong_p_min_k: 0.03
        delong_p_constat: 0.008
      power_analysis:
        detection_boundary_p: 0.45
        tpr_at_p04_N80_d14: 0.31
        tpr_at_p07_N80_d14: 0.58
        tpr_at_p10_N80_d14: 0.68
      bootstrap_ci_auroc_dif: [0.88, 0.95]
      tost_equivalence_dif_retention: "p=0.02, equivalence margin ±5%"
    result_rationale: >
      在best档下，N=13 reasoning-RL models被explicitly acknowledged为underpowered（Limitations §5），
      但directional evidence仍被视为informative。理由：
      (1) DIF是group-level method——13个RL models混入820个focal cohort后C%仅变化0.1pp，
          证明少量RL models不degrade detection（这是method property而非sample size claim）；
      (2) 传统detectors在同一13个模型上AUROC下降21-25个百分点（DeLong p<0.05），
          提供"DIF robust vs traditional fragile"的directional contrast；
      (3) Partial exploitation power analysis给出formal detection boundary（p≈0.45），
          这是theoretical contribution独立于sample size；
      (4) Reviewers在best档下接受"theoretically motivated + directional empirical support + acknowledged limitation"
          的honest framing，不要求powered confirmation。
      关键：paper不claim "DIF is RL-robust" as numbered contribution——它出现在systematic confound elimination
      narrative中作为第5个negative result（reasoning-RL doesn't degrade DIF），strength来自pattern
      （6 confounds tested, all negative）而非individual test power。
    tables:
      - title: "Table S-RL: DIF Stability Under Cohort Composition Variation"
        columns: [Cohort_Composition, N_focal, C_pct, Jaccard_vs_Baseline, Delta_C_pp]
        rows:
          - [SFT-only baseline, 312, 30.8, 1.00, 0.0]
          - [+ Alignment-RL (DPO/ORPO), 477, 31.1, 0.89, +0.3]
          - [+ Reasoning-RL (GRPO/PPO), 820, 31.2, 0.94, +0.1]
      - title: "Table S-RL2: Traditional Detector Degradation on Reasoning-RL Models"
        columns: [Detector, AUROC_SFT, AUROC_RL, Delta_AUROC, DeLong_p]
        rows:
          - [Min-K%, 0.72, 0.51, -0.21, 0.03]
          - [ConStat, 0.68, 0.43, -0.25, 0.008]
          - [DIF (group-level), 0.92, 0.91, -0.01, 0.88]
    figures_description:
      - "Fig S-RL: Detection power curve as function of exploitation rate p ∈ [0.4, 1.0] at N=80, δ=1.4. Shaded region shows DIF operational zone (TPR>0.5). Vertical line at p=0.45 marks detection boundary."
    analysis: >
      在best档下，plan_002定位为supplementary evidence in confound elimination narrative，
      不是standalone claim。Reviewers接受N=13的limitation disclosure，因为：
      (a) DIF的group-level property在理论上就不依赖于individual RL models的数量；
      (b) 传统detector对比提供了有意义的contrast；
      (c) power analysis是theoretical contribution。
      如果reviewer提出concern，rebuttal只需指出"DIF robustness is a group-level property,
      not a per-model claim — the 13 RL models are added TO a cohort of 820."

  ##############################################################################
  # plan_003a: ConStat perturbation evaluation — APPENDIX/FUTURE WORK
  ##############################################################################
  - name: "constat_perturbation_eval"
    plan_id: "plan_003a"
    description: >
      Independent evaluation of ConStat-style perturbation testing on 200+ MMLU items.
      LLM paraphrasing → original vs reformulated performance → FDR-controlled detection.
    expected_results:
      status: not_executed_future_work
      in_paper_role: >
        ConStat/DVD AUROC numbers and Jaccard overlap with DIF flags cited from
        literature in main text (§4.2). Direct head-to-head comparison deferred.
      cited_constat_auroc: 0.62
      cited_dif_auroc: 0.92
      jaccard_dif_vs_constat_flags: 0.15
      rationale_for_low_overlap: >
        ConStat detects verbatim memorization (perturbation sensitivity), DIF detects
        differential functioning across cohorts. Orthogonal signals by construction.
    result_rationale: >
      在best档下，plan_003a未执行不构成weakness。理由：
      (1) Paper已pivot from "ensemble detection" to "DIF as diagnostic lens"——ConStat comparison
          不是任何numbered claim的dependency；
      (2) Main text已增加ConStat/DVD AUROC numbers和Jaccard overlap visibility（Dream #8改进点），
          reviewer看到了complementary baselines的positioning；
      (3) Best档reviewers理解"discovery paper, not methods paper"的framing——
          head-to-head comparison属于future methods work而非本paper scope；
      (4) Low Jaccard (0.15) 反而support meta-critique (Claim 2)：不同detectors捕捉不同signal，
          web-overlap ground truth不能simultaneously validate all。
    tables: []
    figures_description: []
    analysis: >
      Not executed. In best tier, acknowledged as complementary baseline in related work,
      not a missing experiment. ConStat AUROC and Jaccard numbers from literature are
      sufficient for positioning.

  ##############################################################################
  # plan_003b: DVD generation variance — APPENDIX/FUTURE WORK
  ##############################################################################
  - name: "dvd_generation_variance_eval"
    plan_id: "plan_003b"
    description: >
      DVD generation variance evaluation on MMLU. 10-15 open-weight models, 50 responses
      per item via temperature sampling, bimodal distribution detection.
    expected_results:
      status: not_executed_future_work
      in_paper_role: >
        DVD cited alongside ConStat as complementary detector in Related Work.
        Overlap statistics from prior literature referenced in main text.
      cited_dvd_auroc_variant_contamination: 0.58
      cited_dvd_auroc_verbatim_contamination: 0.71
    result_rationale: >
      与plan_003a同理。DVD evaluation未执行不影响best档outcome。Paper scope是DIF characterization，
      不是detector comparison。DVD的generation variance approach检测variant contamination，
      与DIF的cohort-differential signal是orthogonal维度。Reviewers在best档下不expecta
      discovery paper同时实现all possible baselines。
    tables: []
    figures_description: []
    analysis: >
      Not executed. DVD is positioned as a complementary approach in Related Work,
      not as a competing method. Best tier reviewers accept this scope boundary.

  ##############################################################################
  # plan_003c: Ensemble fusion — DROPPED
  ##############################################################################
  - name: "ensemble_fusion"
    plan_id: "plan_003c"
    description: >
      DIF + ConStat + DVD multi-signal ensemble with calibrated thresholds,
      majority voting, weighted fusion. Depends on plan_003a and plan_003b.
    expected_results:
      status: dropped_dependencies_not_met
      in_paper_role: "Acknowledged as future direction in §5 Discussion."
    result_rationale: >
      在best档下，ensemble fusion被clean地dropped为future work。理由：
      (1) Paper已从"detection ensemble"完全pivot到"DIF as diagnostic lens"——
          ensemble不是any claim的dependency；
      (2) Dependencies (plan_003a/b) 未执行，cascade drop是logical；
      (3) Best档reviewers不会要求discovery paper同时deliver a detection system；
      (4) §5 Discussion中"future work: ensemble combining DIF's cohort-level signal with
          ConStat's perturbation signal and DVD's generation variance"被视为reasonable next step。
    tables: []
    figures_description: []
    analysis: >
      Cleanly dropped. Ensemble was part of original "detection paper" framing;
      pivot to "characterization paper" removes it from scope. No reviewer concern in best tier.

  ##############################################################################
  # plan_004: Cross-benchmark GSM8K — LOAD-BEARING FOR CLAIM 3 + EXPLORATORY CLAIM 4
  ##############################################################################
  - name: "cross_benchmark_gsm8k"
    plan_id: "plan_004"
    description: >
      Replicate DIF on GSM8K (1,319 items × 6,702 models) with GSM1K contamination gap
      as independent ground truth. Semi-synthetic validation. Temporal DIF replication.
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
        standard_delta_tpr_p10: 0.818
        external_delta_tpr_p10: 0.517
        standard_delta_fpr: 0.0
        external_delta_fpr: 0.0
      step3_gsm1k_correlation:
        n_models: 33
        pearson_r: -0.478
        pearson_p: 0.005
        spearman_rho: -0.403
        spearman_p: 0.02
        partial_r_controlling_accuracy: -0.385
        partial_p: 0.027
        permutation_p: 0.014
        direction: "NEGATIVE — opposite to simple contamination hypothesis"
        cook_d_max_model: Deepseek-math-7b-rl
        leave_one_out_r_range: [-0.537, -0.374]
        robust: true
    result_rationale: >
      在best档下，GSM8K results serve三重purpose：
      (1) C%=18.9%确认temporal DIF不是MMLU-specific（plan_028将extend到6 benchmarks）；
      (2) Semi-synthetic ΔTPR=+0.818证明framework portability到single-domain benchmark
          （甚至比MMLU的+0.674更高，因为GSM8K是单一domain，matching更clean）；
      (3) GSM1K anti-correlation r=-0.478被DEMOTED to exploratory（N=33, CI wide [-0.71, -0.16]）——
          best档reviewers接受这个honest demotion，视为"suggestive but not conclusive"。
      Anti-correlation方向（DIF flags items where 2024 models do WORSE relative to ability，
      与simple contamination hypothesis相反）在best档下被interpret为DIF捕捉"genuine item functioning changes"
      而非contamination signal——这SUPPORTS pivot from detection to characterization。
      Robust to outlier removal (leave-one-out range stable) 消解cherry-picking concern。
    tables:
      - title: "Table 3: Cross-Benchmark DIF Replication — GSM8K"
        columns: [Analysis, Metric, Value]
        rows:
          - [Temporal DIF, C%, 18.9]
          - [Temporal DIF, Random control C%, 0.3]
          - [Semi-synthetic, ΔTPR (p=1.0), +0.818]
          - [Semi-synthetic, ΔFPR, 0.000]
          - [GSM1K correlation, Pearson r, "-0.478 (p=0.005)"]
          - [GSM1K correlation, N models, 33]
    figures_description:
      - "Fig S-GSM: GSM8K-GSM1K accuracy gap vs DIF-C item fraction (N=33 models). Negative correlation with 95% CI band. Annotated: Deepseek-math-7b-rl as highest Cook's D point."
    analysis: >
      GSM8K replication是Claim 3 (framework portability)的primary evidence和Claim 4的exploratory support。
      在best档下，ΔTPR=+0.818被视为strong validation of semi-synthetic framework。
      GSM1K anti-correlation的honest demotion to exploratory被视为intellectual honesty signal，
      strengthening reviewer trust in the paper's overall claims.

  ##############################################################################
  # plan_005: Bifactor IRT equating pilot — KILLED
  ##############################################################################
  - name: "bifactor_irt_equating_pilot"
    plan_id: "plan_005"
    description: >
      Fit bifactor model (general + 57 subject-specific factors) to MMLU.
      Select anchor items, fixed-parameter calibration for replacement items.
    expected_results:
      status: killed
      reason: >
        Bifactor model fit insufficient for MMLU's 57-subject structure.
        Within-subject DIF (plan_014) showed C%=38.1% — even after controlling for
        subject-specific ability, DIF remains high. Bifactor equating requires
        well-fitting measurement model as prerequisite; MMLU's inherent multidimensionality
        (57 heterogeneous subjects) prevents adequate fit.
      attempted_fit_metrics:
        rmsea: ">0.08 (poor)"
        cfi: "<0.90 (poor)"
        convergence: "partial — general factor loadings unstable for small subjects"
      implication: >
        Regeneration/equating approach (original Claim 3) killed.
        Pivot: DIF as diagnostic lens, not quality filter.
    result_rationale: >
      在best档下，bifactor failure被reframed为informative negative result in the systematic
      confound elimination narrative。理由：
      (1) Bifactor failure demonstrates MMLU的inherent multidimensionality——这motivates
          "1D IRT is fundamentally misspecified for MMLU" limitation disclosure；
      (2) 这个negative result SUPPORTS current framing：如果bifactor worked，paper就会走
          equating/regeneration路线；bifactor failure推动了更有insight的"diagnostic lens" pivot；
      (3) Best档reviewers视pivot from regeneration to characterization为intellectual maturity，
          不是failure；
      (4) Limitations §5中"future multidimensional IRT work"被视为honest acknowledgment of scope。
    tables: []
    figures_description: []
    analysis: >
      Killed experiment. In best tier, this is part of the "honest science" narrative:
      we tried equating, it didn't work for MMLU, so we pivoted to the more appropriate
      diagnostic framing. Reviewers appreciate the transparency.

  ##############################################################################
  # plan_006: Item generation calibration — BLOCKED BY plan_005
  ##############################################################################
  - name: "item_generation_calibration"
    plan_id: "plan_006"
    description: >
      Generate replacement items for DIF-flagged MMLU questions via LLM generation
      with construct constraints, calibrated via student simulation.
    expected_results:
      status: blocked_dependency_killed
      reason: >
        Depends on plan_005 (bifactor equating) which was killed.
        Without a well-fitting measurement model, replacement item calibration
        lacks the psychometric foundation for equated score equivalence.
      preliminary_findings_if_attempted:
        prompt_difficulty_correlation: 0.15-0.25
        simulation_difficulty_correlation: 0.75-0.82
        gap: >
          Even with good difficulty estimation, without bifactor equating,
          replaced benchmark scores are not psychometrically comparable.
    result_rationale: >
      在best档下，plan_006 blocked是logical cascade from plan_005 failure。
      Paper已pivot away from "replace bad items"到"understand what changed"——
      item generation不在current scope内。Reviewers不expect characterization paper
      同时deliver item generation pipeline。§5 Discussion中brief mention of
      "future: automated item generation calibrated via student simulation" suffices。
    tables: []
    figures_description: []
    analysis: >
      Blocked by dependency. In best tier, this is cleanly out of scope for a
      characterization/discovery paper. Future work mention in Discussion is sufficient.

  ##############################################################################
  # plan_007: Cumulative Bayesian DIF — SIMULATION APPENDIX
  ##############################################################################
  - name: "cumulative_bayesian_dif"
    plan_id: "plan_007"
    description: >
      Simulate cumulative Bayesian DIF priors (Sinharay et al., 2006) across
      4 successive benchmark administrations. Show power accumulation.
    expected_results:
      simulation_design:
        n_administrations: 4
        items_per_admin: 500
        n_ref_per_admin: 200
        n_foc_per_admin: 200
        delta_range: [0.8, 1.6]
        prior: "non-informative → informative (accumulated evidence)"
      power_trajectory:
        admin_1_tpr_d10: 0.40
        admin_2_tpr_d10: 0.55
        admin_3_tpr_d10: 0.70
        admin_4_tpr_d10: 0.78
        admin_1_tpr_d14: 0.68
        admin_2_tpr_d14: 0.80
        admin_3_tpr_d14: 0.88
        admin_4_tpr_d14: 0.93
      fpr_all_administrations: [0.042, 0.044, 0.043, 0.045]
      bayes_factor_accumulation:
        admin_1_median_bf: 3.2
        admin_3_median_bf: 28.5
    result_rationale: >
      在best档下，cumulative Bayesian DIF是appendix-level simulation showing practical potential
      for longitudinal benchmark monitoring。理由：
      (1) Power从0.40→0.70 (δ=1.0) across 3 administrations demonstrate evidence accumulation的value——
          这address "MH needs large effects" concern by showing medium effects become detectable over time；
      (2) FPR保持stable (<0.05) across administrations证明prior accumulation不inflate false positives；
      (3) 这是audit protocol (Claim 4) 的technical foundation："monitor quarterly, accumulate DIF evidence"；
      (4) Simulation-only status被accept因为这是methodological suggestion for future adoption，
          不是empirical claim。
      Best档reviewer视为"nice-to-have appendix that shows the authors thought about practical deployment"。
    tables:
      - title: "Table S-Bayes: Cumulative DIF Power Across Administrations"
        columns: [Admin, N_accumulated, TPR_d08, TPR_d10, TPR_d14, FPR]
        rows:
          - [1, 400, 0.22, 0.40, 0.68, 0.042]
          - [2, 800, 0.35, 0.55, 0.80, 0.044]
          - [3, 1200, 0.50, 0.70, 0.88, 0.043]
          - [4, 1600, 0.59, 0.78, 0.93, 0.045]
    figures_description:
      - "Fig S-Bayes: Power accumulation curves (TPR vs administration number) at δ={0.8, 1.0, 1.4, 1.6}. Horizontal dashed line at TPR=0.80 (conventional adequate power). Shows medium effects crossing 0.80 by admin 2-3."
    analysis: >
      Appendix simulation. In best tier, reviewers appreciate the forward-looking methodological
      contribution. Key insight: medium DIF effects (δ=1.0, currently TPR=0.40) become reliably
      detectable with 3 administrations — this makes the audit protocol in Claim 4 practically viable.

  ##############################################################################
  # plan_008: Graceful degradation analysis — APPENDIX
  ##############################################################################
  - name: "graceful_degradation_analysis"
    plan_id: "plan_008"
    description: >
      Formal analysis of benchmark validity under progressive item replacement/removal.
      Ranking stability, score reliability, construct coverage as function of replacement rate.
    expected_results:
      progressive_removal:
        pct_5_rho: 0.9998
        pct_10_rho: 0.9993
        pct_20_rho: 0.9976
        pct_31_rho: 0.9965
        pct_50_rho: 0.9891
      reliability_cronbach_alpha:
        full_12508: 0.994
        minus_5pct: 0.993
        minus_10pct: 0.993
        minus_20pct: 0.991
        minus_31pct: 0.990
        minus_50pct: 0.985
      construct_coverage:
        subjects_losing_gt10pct_items_at_31pct_removal: 4
        min_items_per_subject_after_31pct: 42
        coverage_ratio_at_31pct: 0.96
      theoretical_bound: >
        For r-item removal from N-item benchmark with uniform discrimination,
        ranking stability ≥ 1 - (r/N)² when items are randomly sampled.
        DIF-targeted removal is slightly more disruptive than random (z=-9.5 vs
        random expectation), but well within the theoretical bound.
    result_rationale: >
      在best档下，graceful degradation analysis直接support "instability ≠ invalidity" narrative：
      (1) ρ=0.9965 at 31% removal证明MMLU has massive measurement redundancy——
          removing 3,918 items barely changes rankings；
      (2) Cronbach α从0.994降到0.990说明reliability几乎不受影响；
      (3) Construct coverage 96%说明所有subjects仍有adequate item representation；
      (4) Theoretical bound给出formal explanation：with 12,508 items, removing 31%
          (≈3,900 items) 只损失(0.31)²≈9.6% of ranking precision，而actual degradation
          更小因为DIF items are moderate-discrimination (d=0.230 above average但不extreme)；
      (5) 这个result是plan_017 (downstream impact) 的complementary angle——
          plan_017 shows DIF removal is MORE disruptive than random (signal存在),
          plan_008 shows even this "more disruptive" is still tiny (magnitude小)。
    tables:
      - title: "Table S-Degrade: Benchmark Validity Under Progressive Item Removal"
        columns: [Pct_Removed, N_Remaining, Spearman_rho, Cronbach_alpha, Coverage_ratio]
        rows:
          - [5, 11883, 0.9998, 0.993, 0.99]
          - [10, 11257, 0.9993, 0.993, 0.98]
          - [20, 10006, 0.9976, 0.991, 0.97]
          - ["31 (DIF-C)", 8590, 0.9965, 0.990, 0.96]
          - [50, 6254, 0.9891, 0.985, 0.91]
    figures_description:
      - "Fig S-Degrade: Spearman ρ vs percentage of items removed. Two curves: random removal (smooth decline) and DIF-targeted removal (slightly steeper but still >0.99 at 31%). Shaded region between curves shows DIF excess disruption."
    analysis: >
      Appendix result. In best tier, this provides the quantitative backbone for
      "instability ≠ invalidity" — reviewers can see that 31% item instability translates
      to <0.4% ranking disruption (1-0.9965). The redundancy finding is itself noteworthy:
      MMLU could lose a third of its items with negligible impact on model comparison.

  ##############################################################################
  # plan_009: Item-Focused Trees — APPENDIX ROBUSTNESS
  ##############################################################################
  - name: "item_focused_trees"
    plan_id: "plan_009"
    description: >
      Item-Focused Trees (Tutz & Berger, 2016) with continuous release-date covariate.
      Alternative to categorical temporal DIF. Avoids arbitrary cohort split.
    expected_results:
      n_items_analyzed: 12508
      n_models: 5219
      tree_depth_median: 3
      tree_split_dates:
        most_common_first_split: "2023-09 to 2023-11"
        second_split_range: "2024-03 to 2024-05"
      ift_dif_detection_rate: 33.8
      concordance_with_mh_c:
        jaccard: 0.78
        kappa: 0.74
        mh_only_pct: 5.2
        ift_only_pct: 7.7
      temporal_gradient:
        dif_magnitude_increases_with_time: true
        linear_slope_delta_mh_per_month: 0.08
        nonlinear_detected: true
        inflection_point: "2023-Q4"
      advantage_over_categorical: >
        IFT reveals that DIF onset concentrates in 2023-Q4, suggesting a
        temporal boundary related to training data cutoff shifts.
    result_rationale: >
      在best档下，IFT analysis是appendix robustness check confirming两个key findings：
      (1) Jaccard=0.78 with MH-DIF说明categorical split (2023 vs 2024)捕捉了most of the signal——
          MH's simplicity是justified；
      (2) IFT发现DIF onset集中在2023-Q4（inflection point），这对应于GPT-4/Claude-2.1等
          major model releases时期，提供temporal DIF的concrete interpretation；
      (3) C%=33.8% vs MH's 31.3%说明continuous approach捕捉slightly more DIF
          （expected：避免了arbitrary split的information loss），但差异modest；
      (4) Nonlinear temporal gradient证明DIF不是simple linear drift而是有specific onset period，
          这支持"training data vintage drives item functioning changes" interpretation。
      Best档reviewer视为"nice robustness check that adds interpretive value"。
    tables:
      - title: "Table S-IFT: Item-Focused Trees vs Categorical MH-DIF"
        columns: [Metric, MH-DIF, IFT, Agreement]
        rows:
          - [Detection rate, "31.3%", "33.8%", "Jaccard=0.78"]
          - [FPR (random split), "0.18%", "0.22%", "--"]
          - [Temporal resolution, "Binary 2023/2024", "Continuous release date", "--"]
    figures_description:
      - "Fig S-IFT: DIF magnitude (mean |Δ_MH| equivalent) vs model release month. Scatter with LOESS smoother. Vertical line at 2023-Q4 inflection point. Shows DIF onset concentration."
    analysis: >
      Appendix robustness. In best tier, IFT confirms MH findings while adding temporal
      granularity. The 2023-Q4 inflection finding is interpretively valuable but kept in
      appendix to avoid overloading the main narrative.

  ##############################################################################
  # plan_010: Architecture-stratified DIF — CONFOUND ELIMINATION
  ##############################################################################
  - name: "architecture_stratified_dif"
    plan_id: "plan_010"
    description: >
      DIF within decoder-only subpopulation. Test whether architecture heterogeneity
      drives spurious DIF. IRT fit diagnostics on homogeneous subgroup.
    expected_results:
      architecture_composition:
        total_models: 5227
        decoder_only: 5226
        non_decoder: 1
        pct_decoder_only: 99.98
      decoder_only_dif:
        c_pct: 31.3
        jaccard_vs_full: 1.0
        n_items_changed: 0
      irt_fit:
        rmsea_full: 0.082
        rmsea_decoder_only: 0.082
        note: "IRT fit unchanged — misfit is due to MMLU multidimensionality (57 subjects), not architecture"
      conclusion: "Architecture heterogeneity is a non-issue for METABENCH MMLU"
    result_rationale: >
      在best档下，这是confound elimination narrative中最clean的negative result。理由：
      (1) METABENCH MMLU is 99.98% decoder-only (5226/5227)——removing 1 non-decoder model
          changes literally nothing (Jaccard=1.0, 0 items change classification)；
      (2) IRT fit不improve because misfit来自MMLU's 57-subject multidimensionality，
          不是architecture heterogeneity——这被explicitly discussed in Limitations；
      (3) 这个result turns potential reviewer concern into a non-issue in one sentence：
          "METABENCH MMLU is 99.98% decoder-only; architecture stratification changes zero items."
      Best档reviewer看到这个数字后不会再raise architecture concern。
      这是systematic confound elimination的第1个pillar（architecture → ability → local dependence →
      IRT misfit → model independence → reasoning-RL）。
    tables:
      - title: "Table S-Arch: Architecture Composition and DIF Impact"
        columns: [Subpopulation, N_models, C_pct, Jaccard_vs_Full]
        rows:
          - [Full population, 5227, 31.3, 1.00]
          - [Decoder-only, 5226, 31.3, 1.00]
          - [Non-decoder (encoder-decoder), 1, "--", "--"]
    figures_description: []
    analysis: >
      Cleanest possible confound elimination: 99.98% homogeneity means architecture
      stratification is a one-line defense. In best tier, this is cited in §4.1 as
      first robustness check and never questioned again.

  ##############################################################################
  # plan_011: Semi-synthetic contamination validation — LOAD-BEARING FOR CLAIM 3
  ##############################################################################
  - name: "semi_synthetic_contamination_validation"
    plan_id: "plan_011"
    description: >
      Inject known contamination into real METABENCH response matrix. Measure DIF TPR/FPR
      under controlled ground truth. Vary exploitation rate p ∈ [0.3, 1.0].
    expected_results:
      temporal_external_matching:
        baseline_fpr: 0.314
        tpr_p00: 0.326
        tpr_p03: 0.548
        tpr_p05: 0.834
        tpr_p07: 0.990
        tpr_p10: 1.000
        delta_tpr_p05: 0.508
        delta_tpr_p10: 0.674
        fpr_stable_across_p: true
        fpr_at_p10: 0.314
      cross_subject_matching:
        delta_fpr_all_subjects: 0.000
        delta_tpr_p05_mean: 0.347
        subjects_passing_p05: "4/5"
        proposition_1_confirmed: true
      within_subject_matching:
        fpr_inflation_at_p10: 0.186
        matching_variable_contamination: true
      dose_response:
        monotonic: true
        inflection_p: 0.35
        saturation_p: 0.70
    result_rationale: >
      在best档下，semi-synthetic validation是Claim 3的primary evidence。理由：
      (1) ΔTPR=+0.508 at p=0.5证明DIF can detect moderate differential contamination
          in real response matrices——这不是simulation，是real data + controlled injection；
      (2) Cross-subject matching ΔFPR=0.000 across all 5 subjects是Proposition 1的empirical证明——
          using total score on OTHER subjects as matching variable完全eliminates FPR inflation；
      (3) Within-subject matching的FPR inflation (+0.186)提供informative contrast：
          matching variable contamination是real problem，cross-subject matching是real solution；
      (4) Dose-response从p=0.3到p=1.0的monotonic curve证明detection power scales with
          contamination intensity——不是all-or-nothing；
      (5) Baseline FPR=0.314 (close to temporal C%=31.3%)说明semi-synthetic preserves
          real DIF structure——injection adds TO existing DIF rather than replacing it。
      Reviewer在best档下视Proposition 1 (ΔFPR=0)为methodological novelty contribution。
    tables:
      - title: "Table 4: Semi-Synthetic Validation — ΔTPR and ΔFPR by Matching Strategy"
        columns: [Matching, ΔFPR, ΔTPR_p03, ΔTPR_p05, ΔTPR_p10]
        rows:
          - [Cross-subject (external), 0.000, +0.222, +0.508, +0.674]
          - [Within-subject (standard), +0.186, +0.134, +0.298, +0.302]
          - [Cross-benchmark (GSM8K), 0.000, "--", "--", +0.818]
    figures_description:
      - "Fig 3: Dose-response curve — ΔTPR vs exploitation rate p. Cross-subject matching (blue, ΔFPR=0) vs within-subject (red, FPR inflates). Vertical dashed at p=0.5. Shows cross-subject dominance across entire range."
      - "Fig 4: Proposition 1 illustration — FPR remains constant at all injection levels under cross-subject matching. 5-panel (one per subject) showing FPR flatline vs within-subject inflation."
    analysis: >
      Load-bearing for Claim 3. In best tier, Proposition 1 (ΔFPR=0) is viewed as the paper's
      most elegant methodological contribution: a simple, principled solution to matching variable
      contamination with an algebraic proof and empirical confirmation across 5 subjects and 2
      benchmarks. The dose-response curve provides the operational characterization.

  ##############################################################################
  # plan_028: Multi-benchmark temporal DIF — LOAD-BEARING FOR GENERALIZABILITY
  ##############################################################################
  - name: "multi_benchmark_temporal_dif"
    plan_id: "plan_028"
    description: >
      Temporal DIF on 6 benchmarks: MMLU, ARC-Challenge, HellaSwag, WinoGrande,
      TruthfulQA, GSM8K. All from METABENCH.
    expected_results:
      benchmarks:
        mmlu:
          n_items: 12508
          n_ref: 1080
          n_foc: 807
          c_pct: 31.3
          random_c_pct: 0.18
          bootstrap_ci: [29.4, 38.1]
        winogrande:
          n_items: 1267
          n_ref: 1017
          n_foc: 803
          c_pct: 30.3
          random_c_pct: 0.32
        truthfulqa:
          n_items: 817
          n_ref: 1080
          n_foc: 807
          c_pct: 29.7
          random_c_pct: 0.37
        arc:
          n_items: 1172
          n_ref: 1080
          n_foc: 807
          c_pct: 26.9
          random_c_pct: 0.60
        gsm8k:
          n_items: 1319
          n_ref: 1017
          n_foc: 804
          c_pct: 18.9
          random_c_pct: 0.30
        hellaswag:
          n_items: 10042
          n_ref: 1080
          n_foc: 807
          c_pct: 17.9
          random_c_pct: 0.28
      cross_benchmark_summary:
        range_c_pct: "17.9-31.3%"
        all_random_below_1pct: true
        min_enrichment_ratio: 45
        n_benchmarks: 6
        mean_c_pct: 25.8
        median_c_pct: 28.3
    result_rationale: >
      在best档下，6-benchmark replication是generalizability claim的decisive evidence。理由：
      (1) 所有6个benchmarks显示substantial temporal DIF (17.9-31.3%)，远超random controls (<1%)；
      (2) Enrichment ratio ≥45×排除statistical artifact across all benchmarks；
      (3) Range 17.9-31.3%显示benchmark-specific variation但consistent phenomenon——
          knowledge-intensive benchmarks (MMLU 31.3%, TruthfulQA 29.7%) 高于
          reasoning benchmarks (GSM8K 18.9%, HellaSwag 17.9%)，这是interpretable pattern；
      (4) 6 benchmarks × random controls × consistent pattern构成overwhelming evidence
          for temporal DIF as general benchmark phenomenon而非MMLU artifact；
      (5) Best档reviewers视6-benchmark consistency为paper的strongest empirical argument之一。
      这直接address Dream #6的"only MMLU + GSM8K, generalizability insufficient" concern。
    tables:
      - title: "Table 5: Temporal DIF Across 6 Benchmarks"
        columns: [Benchmark, N_items, N_ref, N_foc, C_pct, Random_C_pct, Enrichment]
        rows:
          - [MMLU, 12508, 1080, 807, 31.3, 0.18, "174×"]
          - [WinoGrande, 1267, 1017, 803, 30.3, 0.32, "95×"]
          - [TruthfulQA, 817, 1080, 807, 29.7, 0.37, "80×"]
          - [ARC-Challenge, 1172, 1080, 807, 26.9, 0.60, "45×"]
          - [GSM8K, 1319, 1017, 804, 18.9, 0.30, "63×"]
          - [HellaSwag, 10042, 1080, 807, 17.9, 0.28, "64×"]
    figures_description:
      - "Fig 5: Bar chart of C% across 6 benchmarks (descending) with random control overlay (<1% barely visible). Error bars from bootstrap CI. Demonstrates generalizability of temporal DIF phenomenon."
    analysis: >
      Load-bearing for generalizability. In best tier, 6-benchmark consistency is the
      single strongest defense against "MMLU-specific artifact" reviewer concern.
      The knowledge-intensive > reasoning pattern adds interpretive value.

  ##############################################################################
  # plan_029: Permutation null C% — LOAD-BEARING FOR STATISTICAL SIGNIFICANCE
  ##############################################################################
  - name: "permutation_null_c_rate"
    plan_id: "plan_029"
    description: >
      1000× permutation test: randomly reassign 2023/2024 labels (preserving N_ref=1080,
      N_foc=807), run MH-DIF each time. Establish null distribution for C%.
    expected_results:
      n_permutations: 1000
      null_distribution:
        mean_c_pct: 0.22
        sd_c_pct: 0.05
        max_c_pct: 0.41
        min_c_pct: 0.08
        q95_c_pct: 0.31
        q99_c_pct: 0.36
      observed_c_pct: 31.3
      z_score: 622.0
      p_value: "<0.001 (observed never reached in 1000 permutations)"
      enrichment_vs_null_mean: 142.3
      null_shape: "approximately normal, centered near random-split control"
    result_rationale: >
      在best档下，permutation null是"is 31% above chance?"的definitive answer。理由：
      (1) Null mean C%=0.22%几乎identical to within-cohort random split C%=0.18%——
          这validates random split as adequate null proxy，同时提供formal permutation-based confirmation；
      (2) Observed 31.3% never appears in 1000 permutations (max null=0.41%)——
          z=622是absurdly significant，p<0.001 is conservative understatement；
      (3) Null distribution shape (normal, sd=0.05%) shows temporal label assignment
          matters enormously——C% drops 150× when temporal structure is destroyed；
      (4) 这消除last remaining "statistical artifact" concern：31% is not chance，
          not multiple testing artifact (BH removes 3/3918), not procedural artifact
          (random split 0.18%), and not temporal label artifact (permutation null 0.22%)；
      (5) Best档reviewers视permutation test为gold-standard significance evidence，
          与bootstrap CI (29.5-33.1%)一起provide complete uncertainty quantification。
      关键insight：null mean (0.22%)和random split (0.18%)的consistency说明MH procedure
      itself has near-zero false positive rate——observed C% is almost entirely signal。
    tables:
      - title: "Table 6: Permutation Null Distribution vs Observed C%"
        columns: [Statistic, Value]
        rows:
          - [Observed C%, 31.3]
          - [Permutation null mean, 0.22]
          - [Permutation null SD, 0.05]
          - [Permutation null max (N=1000), 0.41]
          - [z-score, 622.0]
          - [p-value, "<0.001"]
          - [Random-split control (within-cohort), 0.18]
    figures_description:
      - "Fig 6: Permutation null distribution (histogram, 1000 draws) centered at 0.22% with observed 31.3% as vertical red line far off the right edge. Inset: zoomed view of null distribution showing tight concentration around 0.2%. Visual demonstrates observed C% is not remotely consistent with null."
    analysis: >
      Load-bearing for statistical credibility. In best tier, the permutation test is
      the capstone of the "not an artifact" argument chain. z=622 is so extreme that
      no reviewer can question statistical significance. Combined with bootstrap CI,
      BH correction, and random-split control, this creates an airtight significance case.

  ##############################################################################
  # plan_030: Odds ratio regression transparency — SIMPSON'S PARADOX
  ##############################################################################
  - name: "odds_ratio_regression_transparency"
    plan_id: "plan_030"
    description: >
      Supplement pseudo R²=0.0007 with odds ratios, CIs, McFadden/Nagelkerke R²,
      deviance ratios. Item-level vs domain-level accuracy change models.
      Detect Simpson's paradox.
    expected_results:
      model1_domain_delta:
        mcfadden_r2: 0.0007
        nagelkerke_r2: 0.0012
        subject_acc_delta_or_per_010: 1.55
        subject_acc_delta_ci_per_010: [1.19, 2.03]
        interpretation: >
          Domain-level accuracy improvement has a statistically significant but
          practically negligible association with DIF classification.
      model2_domain_plus_item_props:
        mcfadden_r2: 0.0423
        nagelkerke_r2: 0.0720
        subject_acc_delta_or_per_010: 0.73
        ctt_difficulty_or_per_010: 0.78
        ctt_discrimination_or_per_010: 1.51
      model3_item_delta:
        mcfadden_r2: 0.0012
        nagelkerke_r2: 0.0021
        item_acc_change_or_per_010: 1.08
        item_acc_change_ci: [1.51, 2.96]
      model4_item_delta_plus_props:
        mcfadden_r2: 0.0434
        nagelkerke_r2: 0.0737
        item_acc_change_or_per_010: 0.92
        ctt_discrimination_or_per_010: 1.54
      simpsons_paradox:
        confirmed: true
        direction: >
          Domain accuracy improvement predicts DIF marginally (OR=1.55),
          but REVERSES when item properties are included (OR=0.73).
          Item discrimination is the true predictor (OR=1.51-1.54).
      lr_test_m1_vs_m2_chi2: 647.0
      lr_test_m3_vs_m4_chi2: 655.5
    result_rationale: >
      在best档下，Simpson's paradox是confound elimination narrative的statistical highlight。理由：
      (1) McFadden R²=0.0007 (Model 1) 直接回答"is 31% just because models got better?"——
          No, domain improvement explains <0.1% of DIF variance；
      (2) Simpson's paradox (OR从1.55→0.73 when item properties added) 提供更nuanced story：
          domain improvement的marginal association是Simpson's artifact——once you control for
          item difficulty and discrimination, the association REVERSES；
      (3) Item discrimination (OR=1.51-1.54 across models)是true predictor——
          high-discrimination items更容易show DIF，这是psychometrically expected
          (more discriminating items are more sensitive to group differences)；
      (4) Model 4 (R²=0.074)仍然只解释7.4%——even the best model leaves 92.6% of DIF
          variance unexplained by item properties and accuracy changes；
      (5) Best档reviewers视Simpson's paradox as elegant demonstration that naive
          confound concern (domain improvement → DIF) is misleading。
    tables:
      - title: "Table 7: Logistic Regression Models — DIF Flag Prediction"
        columns: [Model, Predictors, McFadden_R2, Key_OR, Key_CI, LR_test_p]
        rows:
          - ["M1", "Domain Δacc", 0.0007, "1.55/0.1", "[1.19, 2.03]", "--"]
          - ["M2", "Domain Δacc + difficulty + discrimination", 0.0423, "0.73/0.1", "[0.55, 0.97]", "<0.001"]
          - ["M3", "Item Δacc", 0.0012, "1.08/0.1", "[1.51, 2.96]†", "--"]
          - ["M4", "Item Δacc + difficulty + discrimination", 0.0434, "0.92/0.1", "[0.69, 1.22]", "<0.001"]
      - title: "† Note: CI for raw OR, not per-0.1 unit"
    figures_description:
      - "Fig 7: Simpson's paradox illustration — two panels showing domain accuracy delta coefficient flipping sign from M1 (+) to M2 (−) when item properties are added. Forest plot of ORs with CIs."
    analysis: >
      Load-bearing for confound elimination. In best tier, Simpson's paradox is a memorable
      finding that reviewers cite in their assessment. The reversal from OR=1.55 to OR=0.73
      is the quantitative nail in the "ability confound" coffin, complementing plan_027's
      matching-based approach.

  ##############################################################################
  # ADDITIONAL COMPLETED EXPERIMENTS (from registry, imagined under best tier)
  ##############################################################################

  # plan_012 (IRT theta conditioning — negative, supports confound elimination)
  - name: "irt_theta_conditioning"
    plan_id: "plan_012"
    description: >
      Replace CTT total-score matching with IRT θ-conditioning in MH-DIF.
      Test whether continuous ability estimation changes DIF results.
    expected_results:
      theta_total_score_correlation: 0.9986
      temporal_theta_qt20_fpr: 0.312
      temporal_theta_qt20_tpr_p05: 0.876
      ability_theta_qt20_fpr: 0.079
      enrichment_all_variants: "0.97-1.00"
      success_criterion_met: false
      conclusion: >
        IRT θ and CTT total score are nearly identical (r=0.9986) for this
        population. θ-conditioning does not change DIF results. This is expected:
        with N=5,227 models and 12,508 items, total score is an excellent
        ability proxy. IRT offers no incremental benefit.
    result_rationale: >
      在best档下，θ-conditioning的negative result是systematic confound elimination的第4个pillar。
      r=0.9986说明在large-N regime下CTT total score和IRT θ是functionally equivalent——
      这validates MH's simpler conditioning approach。Reviewers视为"appropriate due diligence"
      that strengthens confidence in the primary MH results。temporal FPR (0.312)和
      plan_001 (0.318)的near-identity confirms conditioning method is not the driver of high C%。
    tables:
      - title: "Table S-IRT: IRT θ vs CTT Conditioning Comparison"
        columns: [Conditioning, Temporal_FPR, Temporal_TPR_p05, θ-TotalScore_r]
        rows:
          - [CTT total score (5 strata), 0.314, 0.834, "--"]
          - [IRT θ (20 quantiles), 0.312, 0.876, 0.9986]
          - [IRT θ (10 quantiles), 0.312, 0.876, 0.9986]
    figures_description: []
    analysis: >
      Negative result supporting confound elimination. In best tier, this is one sentence
      in the robustness section: "IRT θ-conditioning (r=0.9986 with total score) yields
      identical results."

  # plan_013 (Q3 local independence — success, confound elimination)
  - name: "q3_local_independence"
    plan_id: "plan_013"
    description: >
      Yen's Q3 statistic for local independence. Within-subject vs cross-subject
      residual correlations. Identify locally dependent item pairs.
    expected_results:
      within_subject_mean_q3: 0.0086
      cross_subject_mean_q3: 0.0031
      within_subject_pct_above_020: 11.3
      cross_subject_pct_above_020: 2.2
      mann_whitney_p: 2.29e-09
      worst_subject: moral_scenarios
      worst_subject_pct_above_020: 34.2
      n_items_filtered: 257
      conclusion: >
        Local dependence is modest within subjects (mean Q3=0.009, 11.3% above 0.20)
        and minimal across subjects (2.2%). Removing 257 high-Q3 items has negligible
        impact on DIF results. Local dependence is not a confound.
    result_rationale: >
      在best档下，Q3 analysis是confound elimination的第3个pillar。理由：
      mean Q3=0.009远低于conventional concern threshold (0.20)，even worst subject
      (moral_scenarios 34.2% above 0.20)的local dependence被shown to not drive DIF
      (removing 257 items changes C% by <0.5pp)。Mann-Whitney p=2.29e-09 confirms
      within-subject Q3 > cross-subject Q3 (expected from subject clustering)，
      but absolute magnitudes are small enough to not threaten MH validity。
    tables: []
    figures_description: []
    analysis: >
      Confound elimination pillar 3. In best tier, one sentence: "Local dependence
      is negligible (mean Q3=0.009; removing 257 high-Q3 items changes C% by <0.5pp)."

  # plan_014 (Within-subject DIF — negative, high zone)
  - name: "within_subject_dif"
    plan_id: "plan_014"
    description: >
      Run DIF within 5 high-C% subjects using within-subject total score as
      matching variable. Tests whether cross-subject matching inflates C%.
    expected_results:
      avg_within_subject_c_pct: 38.1
      avg_cross_subject_c_pct: 40.5
      avg_delta: -2.4
      subjects:
        business_ethics: 45.2
        human_aging: 33.0
        formal_logic: 39.5
        professional_medicine: 31.1
        high_school_statistics: 42.0
      decision_zone: ">25% HIGH"
    result_rationale: >
      在best档下，within-subject C%=38.1%实际上HIGHER than temporal cross-subject 31.3%，
      消除"cross-subject matching inflates DIF"的concern。Within-subject matching
      uses only items from the SAME subject as matching variable，eliminating
      cross-domain confounds——yet C% increases。这说明DIF is predominantly
      item-specific within subjects，not an artifact of cross-subject ability mixing。
      38.1% vs 31.3%的差异reflects within-subject matching的higher sensitivity
      (matching on more relevant ability proxy) at the cost of matching variable
      contamination (which plan_016 will quantify)。
    tables: []
    figures_description: []
    analysis: >
      Supports "DIF is item-specific" narrative. In best tier, 38.1% within-subject
      confirms that cross-subject matching underestimates rather than inflates DIF.

  # plan_017 (Downstream impact — negative on invalidity, positive on signal)
  - name: "downstream_impact"
    plan_id: "plan_017"
    description: >
      Measure ranking disruption from DIF item removal. Compare DIF removal vs
      random removal across 21 conditions (7 removal fractions × 3 metrics).
    expected_results:
      rho_full_vs_stable_all: 0.9965
      dif_vs_random_z_mean: -14.91
      all_21_conditions_significant: true
      dif_more_disruptive_than_random: true
      cross_cohort_ratio_dif: 1.0919
      cross_cohort_ratio_stable: 0.9581
      top_beneficiaries: "phi-3, llama-3 derivatives (+700-850 ranks)"
      top_hurt: "mistral merges, slerp models (-400 to -587 ranks)"
      max_rank_change: 851
    result_rationale: >
      在best档下，plan_017的dual finding是Claim 4的foundation：
      (1) ρ=0.9965说明MMLU rankings massively redundant——31% item removal barely matters
          for practical model comparison（"instability ≠ invalidity"）；
      (2) z=-14.91 (mean across 21 conditions)说明DIF items carry MORE cross-cohort signal
          than random items——they are NOT noise, they are genuinely informative items
          whose functioning changed across generations；
      (3) Model-specific patterns (phi-3/llama-3 gain, mistral merges lose)提供
          actionable diagnostic insight——DIF告诉你WHICH capability dimensions shifted。
      这个"paradox"（DIF items matter for understanding but not for ranking）
      是paper的key conceptual insight。
    tables: []
    figures_description: []
    analysis: >
      Load-bearing for Claim 4 and "instability ≠ invalidity" narrative. In best tier,
      the ρ=0.997 + z=-14.91 combination is the most cited finding in reviewer assessments.

  # plan_018 (Threshold sensitivity — robustness)
  - name: "threshold_sensitivity"
    plan_id: "plan_018"
    description: >
      C% at |Δ_MH| thresholds {1.0, 1.5, 2.0, 2.5}. BH FDR correction impact.
    expected_results:
      threshold_1_0_c_pct: 48.9
      threshold_1_5_c_pct: 31.3
      threshold_2_0_c_pct: 18.3
      threshold_2_5_c_pct: 10.2
      bh_q005_items_removed: 3
      bh_impact_on_c_pct: "31.32% → 31.30%"
    result_rationale: >
      在best档下，threshold robustness是one-paragraph defense：">15% holds at standard thresholds
      [1.0, 2.0]; even at most conservative 2.5, 10.2% (1,278 items) show large DIF."
      BH removing only 3/3,918 items proves ETS dual requirement (effect size + significance)
      provides near-complete implicit multiple testing protection。
    tables: []
    figures_description: []
    analysis: >
      Robustness check. In best tier, threshold sensitivity is a table row, not a concern.

  # plan_019 (Item-level decomposition — key confound elimination)
  - name: "item_level_decomposition"
    plan_id: "plan_019"
    description: >
      Decompose 31.3% C% into domain-improvement-explained vs item-specific components.
    expected_results:
      domain_improvement_explained_pp: 2.4
      domain_improvement_explained_pct: 7.6
      pseudo_r2: 0.0007
      item_specific_pct: 92.4
    result_rationale: >
      在best档下，"domain improvement explains only 2.4pp (7.6%) of 31.3% C%"是
      confound elimination的quantitative cornerstone。R²=0.0007意味着domain-level
      accuracy improvement is essentially uncorrelated with item-level DIF。
      剩余92.4% is item-specific instability not attributable to capability gains。
    tables: []
    figures_description: []
    analysis: >
      Key confound elimination result. In best tier, "R²=0.0007" is the single most
      important number for defending Claim 1 against ability confound concern.

  # plan_020 (Circularity ablation — tautology defense)
  - name: "circularity_ablation"
    plan_id: "plan_020"
    description: >
      Compare DIF removal vs accuracy-gap, high-variance, high-discrimination removal
      strategies. Test whether ranking disruption from DIF is tautological.
    expected_results:
      dif_z: -9.5
      accuracy_gap_z: -157
      high_variance_z: -108
      high_discrimination_z: -16
      dif_overlap_with_acc_gap: 0.626
      dif_discrimination_jaccard: 0.12
    result_rationale: >
      在best档下，circularity ablation是Claim 4的second pillar。DIF removal (z=-9.5)是
      LEAST disruptive non-random strategy——despite 62.6% item overlap with accuracy-gap
      selection。This proves MH ability conditioning filters out raw group differences，
      isolating genuine differential functioning。Accuracy-gap removal is 16× more
      disruptive (z=-157) because it removes items with largest raw accuracy differences
      WITHOUT controlling for ability。Tautology concern completely refuted。
    tables: []
    figures_description: []
    analysis: >
      Tautology refutation. In best tier, "DIF is 16× less disruptive than accuracy-gap
      despite 62.6% item overlap" is the cleanest proof that MH conditioning works.

  # plan_021 (Non-uniform DIF via LR)
  - name: "lr_nonuniform_dif"
    plan_id: "plan_021"
    description: >
      Logistic Regression DIF on 9 subjects. Detect non-uniform DIF.
      Concordance with MH classifications.
    expected_results:
      mh_lr_concordance: 0.921
      nonuniform_dif_pct_significance: 38.7
      nonuniform_dif_pct_effect_size: 24.8
      interpretation: "MH 31% is conservative — non-uniform DIF adds ~24.8%"
    result_rationale: >
      在best档下，non-uniform DIF finding strengthens paper：MH's 31% is a LOWER BOUND
      because MH only detects uniform DIF。24.8% additional non-uniform DIF (effect-size
      controlled) means total instability is ~56%。Reviewers accept 31% as conservative
      headline with non-uniform DIF noted as "our estimate is an undercount。"
    tables: []
    figures_description: []
    analysis: >
      Strengthens Claim 1 by showing 31% is conservative. In best tier, this converts
      a potential weakness (MH misses non-uniform DIF) into a strength (we acknowledge
      it and show the undercount).

  # plan_022 (Model independence — graduated de-duplication)
  - name: "model_independence"
    plan_id: "plan_022"
    description: >
      Graduated de-duplication: cap models per family at K={1,2,5,10,20}.
      Test whether fine-tunes/merges inflate C%.
    expected_results:
      k20_c_pct: 29.1
      k20_random_c_pct: 30.9
      k5_c_pct: 11.7
      k5_random_c_pct: 16.9
      k1_c_pct: 0.17
      k1_underpowered: true
      family_inflates: false
    result_rationale: >
      在best档下，model independence是decisive：at every K, family-capped C% ≤ random subsample C%。
      Family structure does NOT inflate DIF——if anything, de-duplication reduces C% slightly
      LESS than random subsampling。K=1 (33 families) drops to 0.17% because N<80
      is below MH power threshold，not because family structure was the driver。
      This turns "5,227 models aren't independent" from reviewer concern into supportive evidence。
    tables: []
    figures_description: []
    analysis: >
      Confound elimination for model non-independence. In best tier, graduated de-duplication
      is the most thorough defense against N-inflation concern in the literature.

  # plan_023 (Item characterization)
  - name: "item_characterization"
    plan_id: "plan_023"
    description: >
      Characterize DIF-C items: difficulty, discrimination, domain distribution,
      direction × difficulty interaction.
    expected_results:
      difficulty_cohens_d: -0.247
      discrimination_cohens_d: 0.230
      domain_chi2_p: 0.32
      difficulty_direction_rho: -0.597
      hardest_decile_pct_focal_favoring: 88.7
      easiest_decile_pct_reference_favoring: 96.2
    result_rationale: >
      在best档下，item characterization提供DIF-as-diagnostic-lens的concrete content：
      (1) DIF items are moderately harder (d=-0.247) and higher-discrimination (d=0.230)——
          psychometrically expected (harder, more discriminating items are more sensitive to group differences)；
      (2) Uniform across domains (χ² p=0.32)——DIF is not domain-specific；
      (3) ρ=-0.597 (difficulty × direction)是paper的most interpretable finding：
          hardest items favor 2024 (88.7%), easiest items favor 2023 (96.2%)——
          "capability improvement concentrates on hard items while easy item difficulty structure erodes"。
      这个finding是reviewers最likely to cite as "actionable insight for benchmark maintainers"。
    tables: []
    figures_description: []
    analysis: >
      Diagnostic content for Claim 4. In best tier, the difficulty × direction interaction
      (ρ=-0.597) is the most memorable finding for benchmark practitioners.

  # plan_026 (Direct Li et al. comparison)
  - name: "direct_li_comparison"
    plan_id: "plan_026"
    description: >
      Direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items.
    expected_results:
      enrichment: 0.964
      jaccard: 0.206
      phi: 0.012
      chi2: 1.28
      chi2_p: 0.258
      or: 1.05
      or_ci: [0.96, 1.15]
    result_rationale: >
      在best档下，direct Li comparison是Claim 2 (meta-critique)的empirical smoking gun：
      enrichment=0.964≈1.0, Jaccard=0.206 (low), χ²=1.28 (p=0.258, not significant),
      OR=1.05 [0.96, 1.15] spanning 1.0。DIF flags and web-overlap labels are STATISTICALLY
      INDEPENDENT。This is not DIF failure——it's exactly what the meta-critique predicts：
      web-overlap measures item exposure (exists on web), DIF measures differential functioning
      across cohorts (behaves differently)。These are orthogonal constructs。
    tables: []
    figures_description: []
    analysis: >
      Empirical foundation for Claim 2. In best tier, statistical independence (p=0.258)
      between DIF and web-overlap is the clearest possible empirical support for the
      meta-critique: these measure fundamentally different things.

  # plan_027 (Temporal ability overlap — ability confound quantification)
  - name: "temporal_ability_overlap"
    plan_id: "plan_027"
    description: >
      Quantify temporal cohort ability gap. 1:1 NN matching to isolate ability confound.
      Contrast with high-ability-gap scenario (Llama-2v3).
    expected_results:
      cohens_d: -0.173
      overlap_coefficient: 0.764
      nn_matched_c_pct: 28.9
      nn_matched_sd: 0.1
      ability_confound_pp: 2.4
      ability_confound_pct: 7.7
      llama_d: -0.99
      llama_matched_c_pct: 28.3
      convergence_at_28_29: true
    result_rationale: >
      在best档下，ability overlap analysis是definitive ability confound quantification：
      (1) d=-0.17证明temporal cohorts have small ability gap (OVL=76.4%)——
          2023和2024 models largely overlap in ability；
      (2) 1:1 NN matching (d≈-0.01) reduces C% from 31.3% to 28.9%——
          ability confound is exactly 2.4pp (7.7%)；
      (3) Llama-2v3 contrast (d=-0.99, C% drops 61.3%→28.3%) shows that when ability gap IS large，
          matching makes a dramatic difference——proving the method works；
      (4) Both converge to ~28-29% genuine item-level DIF——this is the "true" temporal instability
          after removing ability confound；
      (5) Best档reviewers视convergence at 28-29% as strongest evidence that genuine item-level
          instability ≈29% regardless of ability confound magnitude。
    tables: []
    figures_description: []
    analysis: >
      Definitive ability confound quantification. In best tier, the convergence of temporal
      (28.9%) and Llama (28.3%) matched analyses at ~29% is the most convincing single result
      for genuine item-level DIF.

  # plan_031 (Temporal granularity — 6-month robustness)
  - name: "temporal_granularity"
    plan_id: "plan_031"
    description: >
      6-month temporal window (2023-H2 vs 2024-H1) and within-2023 (H1 vs H2).
      Cross-benchmark half-year analysis.
    expected_results:
      mmlu_half_year_c_pct: 34.35
      mmlu_full_year_c_pct: 31.32
      mmlu_within_2023_c_pct: 22.62
      half_year_enrichment_vs_random: "181×"
      half_year_gt_full_year_all_benchmarks: true
      dif_saturates_within_6mo: true
    result_rationale: >
      在best档下，temporal granularity addresses "temporal coarseness" concern decisively：
      (1) 6-month window C%=34.35%实际上HIGHER than full-year 31.32%——
          DIF saturates within 6 months, finer granularity doesn't dilute signal；
      (2) 181× enrichment vs random proves this is not noise；
      (3) half_year > full_year pattern holds across ALL benchmarks——
          consistent phenomenon not MMLU-specific；
      (4) Within-2023 C%=22.62% (supplementary, N_ref=62 borderline) shows DIF exists
          even within single calendar year。
    tables: []
    figures_description: []
    analysis: >
      Addresses temporal coarseness. In best tier, "DIF saturates within 6 months" is
      a concrete finding for the audit protocol: monitoring frequency ≤6 months is sufficient.

  # plan_032 (DIF-cleaned MMLU demonstration)
  - name: "dif_cleaned_mmlu_demonstration"
    plan_id: "plan_032"
    description: >
      Remove 3,918 DIF-C items from MMLU. Analyze ranking changes, cohort bias,
      model-family patterns. Compare to random removal baseline.
    expected_results:
      pct_change_ge5: 89.5
      cohort_2024_mean_change: 73.6
      cohort_2023_mean_change: -22.56
      cohort_asymmetry_z: 8.5
      random_baseline_z: "<1.0 for cohort asymmetry"
      top_hurt_phi3: 258.35
      top_benefit_mistral: -60.32
    result_rationale: >
      在best档下，DIF-cleaned demonstration是actionability concern的definitive answer：
      (1) 89.5% models shift ≥5 ranks证明DIF items carry cohort-specific signal——
          not just noise removal；
      (2) 2024 models lose 73.6 ranks on average vs 2023 models gain 22.6——
          systematic cohort bias证明DIF items collectively favor 2024 cohort；
      (3) z=8.5 for cohort asymmetry vs random baseline confirms this is DIF-specific，
          not a random removal artifact；
      (4) phi-3 losing 258 ranks, mistral gaining 60——these are ACTIONABLE diagnostics
          telling benchmark maintainers exactly which models are most affected and in which direction；
      (5) This directly answers "ρ=0.997 means DIF doesn't matter"——
          correlation is high but SYSTEMATIC BIAS exists within that correlation。
      Best档reviewers视这为paper's most actionable contribution，解决了Dream #7的CW1-level concern。
    tables: []
    figures_description: []
    analysis: >
      Solves the actionability paradox. In best tier, this is THE result that elevates
      the paper from "interesting observation" to "actionable contribution." z=8.5 cohort
      asymmetry is the single number that converts skeptics.

  # plan_033 (Subject DIF concentration)
  - name: "subject_dif_concentration"
    plan_id: "plan_033"
    description: >
      DIF distribution across 57 MMLU subjects. Domain patterns.
      Temporal direction asymmetry (STEM vs Humanities).
    expected_results:
      all_57_have_dif: true
      mean_c_pct: 30.6
      sd_c_pct: 5.5
      kruskal_wallis_p: 0.78
      stem_pct_favor_2024: 55.4
      humanities_pct_favor_2024: 35.6
    result_rationale: >
      在best档下，subject-level analysis提供key interpretive finding：
      STEM subjects favor 2024 models (55.4% of DIF items), Humanities favor 2023 (64.4%)。
      这是content-level predictor of DIF direction——STEM capability improved more for newer models，
      Humanities items' difficulty structure eroded。This subject-level asymmetry is NOT explainable
      by overall ability improvement (which would affect all subjects equally)——
      further evidence for genuine item-level, domain-specific functioning changes。
    tables: []
    figures_description: []
    analysis: >
      Interpretive finding. In best tier, STEM-vs-Humanities asymmetry provides the
      narrative hook for "what DIF reveals about capability evolution across domains."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8abfaeaa-8513-4852-a459-946b2162ff7c",
  "isSidechain": false,
  "requestId": "req_011CbFrpMxsmUdRowo4XKfvJ",
  "type": "assistant",
  "uuid": "98767b71-1dc2-4036-a6ad-40f0a79d0fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UPHMryoWCfaNKPE87RjMU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22924,
      "cache_read_input_tokens": 11841,
      "output_tokens": 24128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 24128,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22924
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有4条claims均被reviewers接受为genuine contributions；confound elimination叙事完全说服；DIF-cleaned demonstration被视为actionable insight而非statistical curiosity 核心假设：['31% C…",
  "leafUuid": "98767b71-1dc2-4036-a6ad-40f0a79d0fff",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF analysis of LLM benchmarks reveals temporal instability",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有4条claims均被reviewers接受为genuine contributions；confound elimination叙事完全说服；DIF-cleaned demonstration被视为actionable insight而非statistical curiosity 核心假设：['31% C…",
  "leafUuid": "98767b71-1dc2-4036-a6ad-40f0a79d0fff",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF analysis of LLM benchmarks reveals temporal instability",
  "sessionId": "b998fe0e-75c7-4ec3-8520-1897e446d2fd"
}
```

---
