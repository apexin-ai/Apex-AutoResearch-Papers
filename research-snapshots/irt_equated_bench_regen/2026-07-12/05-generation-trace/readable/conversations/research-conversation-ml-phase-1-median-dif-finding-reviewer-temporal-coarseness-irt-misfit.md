# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心 DIF finding 成立但 reviewer 在 temporal coarseness 或 IRT misfit 上至少一个方向施压。需

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/fe1e25de-fa6d-433a-87d7-f368d9974873.jsonl`
- **Structured JSON:** [`68b201388f97f1156d2d.json`](../../sessions/68/68b201388f97f1156d2d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T11:12:35.438Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T11:12:35.438Z",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心 DIF finding 成立但 reviewer 在 temporal coarseness 或 IRT misfit 上至少一个方向施压。需要 soften temporal claim 的措辞（从 'instability' 调整为 'cohort-conditional behavioral differences'），或补充 IRT misfit 的额外 robustness。Simpson's paradox 被部分接受但 reviewer 要求更多 confound control。Borderline accept / major revision。\n核心假设：['6-benchmark 结果成立但 reviewer 指出 benchmark 间 C% 变异 (17.9-31.3%) 需要解释——可能要求 benchmark 特征 (item count, domain homogeneity) 作为 moderator 分析', \"Simpson's paradox 被视为 interesting 但 reviewer 质疑 Model 2 中 CTT difficulty/discrimination 是否是正确的 conditioning variables，要求 sensitivity analysis\", 'IRT misfit 攻击面部分打开：至少一个 reviewer 要求 multidimensional IRT 或 polytomous model 作为 robustness check，而非仅在 limitations 中讨论', 'Temporal coarseness 被至少一个 reviewer 标记为 major concern——要求证据表明 quarterly split 不会实质性改变结论，或承认 binary split 是 limitation', 'Audit protocol 被认为 underspecified——reviewer 要求更具体的 decision rules (何时标记 item、何时替换、replacement pipeline)']\n关键指标范围：{'reviewer_avg_score': [3.2, 3.7], 'cross_bench_c_pct_min': [15.0, 19.0], 'cross_bench_c_pct_max': [28.0, 33.0], 'ability_confound_explained_pp': [2.0, 5.0], 'simpsons_or_flip_magnitude': [0.7, 1.1], 'semi_synthetic_delta_tpr_p05': [0.35, 0.5], 'ranking_rho_after_removal': [0.993, 0.998], 'reviewer_count_major_concern': [1, 2]}\n叙事方向：Claim 1 从 'temporal instability' 软化为 'systematic cohort-conditional differences in item functioning'——避免暗示 benchmark 'broken'。Claim 2 (ground truth critique) 保持不变，这是最不受攻击的 claim。Claim 3 (semi-synthetic framework) 保持不变。Claim 4 需要拆分：redundancy 和 diagnostic lens 保留，audit protocol 从 numbered contribution 降级为 discussion section recommendation。Simpson's paradox 从 main evidence 调整为 supplementary robustness check。可能需要增加一个 'temporal granularity sensitivity' 实验（在 camera-ready 前用 quarterly split 补充）。仍冲 EMNLP long paper，但准备 rebuttal 应对 1-2 个 major concerns。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\nfocus: plan_028 新增 6-benchmark cross-validation (C%=17.9-31.3%, 45-174× above random) + plan_030 Simpson's paradox (OR 1.55→0.73)。评估这些新数据是否将 Best 从 3.5 推到 4.0+ (Conference acceptance)。重点关注：IRT misfit defense 是否充分、temporal coarseness (2023 vs 2024 binary) 是否仍是主要攻击面、actionability gap 是否被 audit protocol 覆盖。\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T11:12:35.442Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T11:12:35.442Z",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T11:12:35.465Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心 DIF finding 成立但 reviewer 在 temporal coarseness 或 IRT misfit 上至少一个方向施压。需要 soften temporal claim 的措辞（从 'instability' 调整为 'cohort-conditional behavioral differences'），或补充 IRT misfit 的额外 robustness。Simpson's paradox 被部分接受但 reviewer 要求更多 confound control。Borderline accept / major revision。
核心假设：['6-benchmark 结果成立但 reviewer 指出 benchmark 间 C% 变异 (17.9-31.3%) 需要解释——可能要求 benchmark 特征 (item count, domain homogeneity) 作为 moderator 分析', "Simpson's paradox 被视为 interesting 但 reviewer 质疑 Model 2 中 CTT difficulty/discrimination 是否是正确的 conditioning variables，要求 sensitivity analysis", 'IRT misfit 攻击面部分打开：至少一个 reviewer 要求 multidimensional IRT 或 polytomous model 作为 robustness check，而非仅在 limitations 中讨论', 'Temporal coarseness 被至少一个 reviewer 标记为 major concern——要求证据表明 quarterly split 不会实质性改变结论，或承认 binary split 是 limitation', 'Audit protocol 被认为 underspecified——reviewer 要求更具体的 decision rules (何时标记 item、何时替换、replacement pipeline)']
关键指标范围：{'reviewer_avg_score': [3.2, 3.7], 'cross_bench_c_pct_min': [15.0, 19.0], 'cross_bench_c_pct_max': [28.0, 33.0], 'ability_confound_explained_pp': [2.0, 5.0], 'simpsons_or_flip_magnitude': [0.7, 1.1], 'semi_synthetic_delta_tpr_p05': [0.35, 0.5], 'ranking_rho_after_removal': [0.993, 0.998], 'reviewer_count_major_concern': [1, 2]}
叙事方向：Claim 1 从 'temporal instability' 软化为 'systematic cohort-conditional differences in item functioning'——避免暗示 benchmark 'broken'。Claim 2 (ground truth critique) 保持不变，这是最不受攻击的 claim。Claim 3 (semi-synthetic framework) 保持不变。Claim 4 需要拆分：redundancy 和 diagnostic lens 保留，audit protocol 从 numbered contribution 降级为 discussion section recommendation。Simpson's paradox 从 main evidence 调整为 supplementary robustness check。可能需要增加一个 'temporal granularity sensitivity' 实验（在 camera-ready 前用 quarterly split 补充）。仍冲 EMNLP long paper，但准备 rebuttal 应对 1-2 个 major concerns。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen
venue: emnlp-2026
focus: plan_028 新增 6-benchmark cross-validation (C%=17.9-31.3%, 45-174× above random) + plan_030 Simpson's paradox (OR 1.55→0.73)。评估这些新数据是否将 Best 从 3.5 推到 4.0+ (Conference acceptance)。重点关注：IRT misfit defense 是否充分、temporal coarseness (2023 vs 2024 binary) 是否仍是主要攻击面、actionability gap 是否被 audit protocol 覆盖。

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
  "promptId": "4d09b9b3-fb98-47fe-a62c-959be2e966c8",
  "type": "user",
  "uuid": "9183cb54-b149-436f-b9d4-10bb8b5e5a42",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T11:12:35.463Z_

```json
{
  "parentUuid": "9183cb54-b149-436f-b9d4-10bb8b5e5a42",
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
  "uuid": "acfa2bee-150d-4659-b85f-f34c890430dd",
  "timestamp": "2026-05-21T11:12:35.463Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T11:12:35.463Z_

```json
{
  "parentUuid": "acfa2bee-150d-4659-b85f-f34c890430dd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "09c0d216-ded2-4c76-8750-dda5395c1663",
  "timestamp": "2026-05-21T11:12:35.463Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 DIF finding 成立但 reviewer 在 temporal coarseness 或 IRT misfit 上至少一个方向施压。需要 soften temporal claim 的措辞（从 'instability' 调整为 'cohort-conditional behavioral…",
  "leafUuid": "09c0d216-ded2-4c76-8750-dda5395c1663",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier DIF findings: temporal instability softened to cohort-conditional differences",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873"
}
```

---

### Assistant

_source line 8 · 2026-05-21T11:20:10.418Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to take each experiment in the `experiment_plan` and generate detailed predicted results for the "median" tier scenario. Let me carefully go through each planned experiment and generate realistic predictions based on the median tier definition.

Let me organize the experiments:

1. plan_001 - real_data_dif_mmlu (DONE)
2. plan_002 - rl_robustness_validation (planned)
3. plan_003a - constat_perturbation_eval (planned)
4. plan_003b - dvd_generation_variance_eval (planned)
5. plan_003c - ensemble_fusion (planned)


6. plan_004 - cross_benchmark_gsm8k (DONE)
7. plan_005 - bifactor_irt_equating_pilot (planned)
8. plan_006 - item_generation_calibration (planned)
9. plan_007 - cumulative_bayesian_dif (planned)
10. plan_008 - graceful_degradation_analysis (planned)
11. plan_009 - item_focused_trees (planned)
12. plan_010 - architecture_stratified_dif (planned - but actually done based on paper_framing)
13. plan_011 - semi_synthetic_contamination_validation (DONE)
14. plan_028 - multi_benchmark (planned)
15. plan_014 - temporal_dif (DONE)
16. plan_029 - permutation_null_c_rate (planned)
17. plan_030 - odds_ratio_regression_transparency (DONE)

I'm noticing some discrepancies between what's marked as planned in the experiment_plan and what's actually completed in the registry. The user is asking for detailed data on each planned experiment, so I need to filter down to just those with "planned" status. Looking at the actual registry entries, several experiments marked as planned are either already done or in different states like PREPARING or killed. Let me identify which ones are genuinely still planned versus which have already been executed. I see the discrepancy now—all experiments in the experiment_plan have "planned" status, but the registry shows several are already completed. The user wants me to generate median-tier predictions for each planned experiment, and for the ones that are done, I should create predictions that reflect what median reviewers would expect to see. Let me work through the median tier characteristics and generate realistic predicted results for all of them. The reasoning-RL subsample in plan_002 is too small to draw firm conclusions, though alignment-RL does show DIF retention. Plan_003a's ConStat baseline would detect moderate signal but weaker than DIF for contamination cases, while plan_003b's DVD generation variance shows some promise but remains noisy. Plan_003c's ensemble approach depends on those results and only provides marginal gains. For plan_004, the GSM8K replication at 18.9% C% aligns with the expected cross-benchmark range.

Moving through the remaining approaches: plan_005's bifactor IRT model struggles with MMLU's 57-subject structure, plan_006's item generation shows modest difficulty correlations, and plan_007's cumulative Bayesian DIF demonstrates power improvements in simulation but raises concerns about real-world applicability. Plan_008 confirms graceful degradation under item replacement though its practical value is questioned, plan_009's item-focused trees offer an alternative to categorical DIF with comparable results to Mantel-Haenszel but add computational overhead, and plan_010's architecture stratification confirms homogeneity across the 99 models.

Now examining the validation and cross-validation approaches: plan_011's semi-synthetic contamination targets a ΔTPR range of 0.35-0.50 for the median tier, plan_028's multi-benchmark cross-validation across six benchmarks yields C% estimates between 17.9-31.3%, plan_029's permutation test confirms the 31.3% estimate sits well above the null distribution, and plan_030's odds ratio regression reveals Simpson's paradox with the OR flipping from 1.55 to 0.73 in the median tier.

Now I need to generate the comprehensive YAML output...

Writing YAML configuration... I'm working through how to handle the experiments — for ones already in the registry, I can use the actual results as fixed anchors since they won't change, but for the planned experiments I need to generate realistic predictions with clear reasoning for why the median tier would produce those specific outcomes. I'm working through the median tier scenario for each experiment. Plan_002 involves reasoning-RL models where the alignment-RL cohort maintains stable DIF flags with high Jaccard similarity, but adding just 13 reasoning-RL models to the focal cohort creates an underpowered comparison—the TOST equivalence test is inconclusive and power analysis suggests we'd need around 80 models to detect effects, so reviewers will flag the small sample size as a limitation. For plan_003a, I'm looking at ConStat perturbation results where 200 reformulated items show moderate detection on non-RL models with FDR-controlled flags around 15%.

Now I'm realizing the paper_framing explicitly states that plan_003a/b/c were never executed and are marked as future work, while plan_014 eliminated the bifactor approach entirely. So these experiments don't actually appear in the median tier results—I should focus on what was actually run rather than predicting hypothetical outcomes for planned-but-unexecuted experiments.

Let me organize the YAML by plan_id with all the required fields: name, plan_id, description, expected_results, result_rationale, tables, figures_description, and analysis. I'll need to stay within the median tier constraints for reviewer scores and cross-benchmark percentages.

Writing the comprehensive YAML output... The DIF retention for alignment-RL stays strong at around 0.87, though the equivalence test results are inconclusive. Traditional detection methods like ConStat and Min-K% show clear degradation on reasoning-RL models, but the sample size limits what we can claim statistically. For plan_003a, ConStat catches roughly 18% of items in non-RL models but only 6% in RL models—a meaningful drop with moderate effect size that provides a useful reference point without shifting the paper's conclusions. Plan_003b examines DVD variance across 10-15 models with multiple responses each, finding bimodal patterns in about 12% of items, though noise becomes problematic for smaller models. Plan_003c explores combining DIF with ensemble methods...

Fusing ConStat and DVD with DIF yields only marginal gains in median tier (AUROC improves by 0.03-0.05), and the fusion weights fluctuate too much across validation folds to feel robust—reviewers would likely push back on the added complexity. Plan_004 tests portability on GSM8K with a 18.9% correct rate and strong TPR improvements for standard and external variants, though the negative correlation with GSM1K is concerning. Plan_005's bifactor IRT approach fails—the model fit is poor and 57 subjects is too many for stable estimation, confirming that unidimensional IRT captures the core structure of MMLU. Plan_006 moves into item generation and calibration...

Plan_006 depends on plan_005's results. The difficulty correlation between generated items and student simulation falls short at ρ=0.55-0.65, and there are gaps in domain coverage that keep it from being a strong contribution. Plan_007 shows cumulative Bayesian DIF gains power from 0.40 to 0.68 over three administrations, which is interesting but remains simulation-only and reviewers tend to discount that. Plan_008's graceful degradation analysis demonstrates ranking stability holds up to 31% item replacement with ρ≈0.993, supporting the redundancy argument though the practical protocol still faces scrutiny. Plan_009 extends item-focused trees with continuous release dates and shows good alignment with binary MH results (Spearman correlation around 0.78).

Plan_010 confirms that architecture heterogeneity isn't the problem—99.98% decoder-only doesn't improve IRT fit because the misfit stems from 57 multidimensional subjects, not the model design. Plan_011 is checking semi-synthetic contamination validation where the true positive rate delta at p=0.5 should fall between 0.35-0.50, but the temporal external result came in at 0.834, which is well above the expected range. I need to recalibrate my approach here — since Phase 1 already defined what the median tier looks like, I should generate predicted results that fit within those established ranges rather than trying to match actual experimental outcomes that might fall outside them. For plan_011, I'll use 0.43 for the ΔTPR at p=0.5, plan_028 should show cross-bench C% varying between roughly 17% and 30% based on the specified ranges, and plan_030 involves checking whether Simpson's OR flips.

Now I'm verifying each experiment against the median tier constraints: plan_030's flip magnitude of 0.82 falls within the 0.7-1.1 range, plan_027's ability confound at 2.4pp is within 2.0-5.0pp, and plan_017's ranking correlation of 0.996-0.999 aligns with the 0.993-0.998 expectation. I'm ready to construct the full YAML output systematically, ensuring every value stays within the defined median tier boundaries.

For the cross-benchmark results, I need to set HellaSwag at around 17.5% as the lowest performer and MMLU at approximately 30.1% as the highest, which captures the variance the reviewer will want explained. I'm treating the experiment_plan as the authoritative list of experiments to predict regardless of registry status, and I'll make sure the rationales are comprehensive without being excessive.

Writing the YAML output...

For plan_029, I'm running a permutation test with 1000 iterations to establish a null distribution of C%. The null mean should fall around 0.5-1.0% in the median tier, making the observed 31.3% far exceed significance thresholds (p<0.001), though the reviewer might question whether the permutation approach adequately preserves temporal structure.

For plan_002, the SFT-only cohort flags about 31% of items via DIF, while the alignment-RL cohort (DPO/ORPO models, N=477) flags slightly fewer at 29%, with a Jaccard overlap of 0.82 between the two sets. When I add 13 reasoning-RL models to the focal cohort, the Jaccard similarity with the original stays high at 0.93, and the individual ConStat AUROC metrics are...

Now I'm looking at the performance degradation on reasoning-RL models—ConStat drops to 0.58-0.65 compared to 0.72 on non-RL, and Min-K% performs near chance at 0.52-0.60. The DeLong test comparing DIF and ConStat yields p=0.08 (not significant given the small N=13), TOST equivalence is inconclusive with wide confidence intervals, and power analysis shows I'd need around 80 samples to detect effects at δ≥1.4. The partial exploitation curves show DIF's power degrades gracefully as the detection threshold shifts from 1.0 to 0.5.

For plan_003a, I've reformulated 220 items and ConStat detects about 22% of them on non-RL models...

Examining plan_003b results...

For plan_003c, the ensemble approach achieves 0.74 AUROC, marginally better than DIF at 0.71, but the fusion weights are unstable and the improvement is modest.

The 2-of-3 majority voting shows decent precision at 0.82 but lower recall of 0.55, with cross-validation revealing weight instability across folds.

Plan_005 ran into computational constraints — the bifactor model with 57 factors wouldn't converge, so I reduced it to 5 factors covering major domains. The fit indices fall short of what's needed for reliable anchor item selection, so this approach isn't viable at MMLU scale.

Plan_006 depends on plan_005 succeeding, but since that's been abandoned, any independent attempt shows weak correlations between LLM-generated item difficulty and both student simulation and actual model performance.

For plan_007, I'm running simulated administrations with medium effect sizes and tracking cumulative power across multiple rounds — it climbs from 0.38 individually to 0.74 after four administrations while keeping false positive rates controlled, though this is simulation-only and reviewers are skeptical.

Plan_008 examines what happens when I progressively replace items in the pool — even at 50% replacement, score reliability stays above 0.95, suggesting the equating framework is robust to item turnover.

Plan_009 uses item functioning trends as a covariate and finds strong correlation with measurement heterogeneity, identifying similar problematic items as the main approach, but the added complexity doesn't shift the core conclusion so it's relegated to supplementary analysis.

For plan_010, I'm checking the decoder-only model subset — nearly all 5227 models qualify, and IRT fit metrics remain consistent.  The construct coverage and DIF rates are virtually identical to the full set, confirming that model architecture isn't driving the observed differential functioning.

Plan_029 validates the 31.3% finding through permutation testing: the null distribution clusters around 0.42% with a maximum of 1.2%, making the observed result astronomically unlikely by chance alone.

Plan_030 begins examining logistic regression with domain-level predictors.

Now I'm looking at how item-level and domain-level factors interact in predicting DIF, and there's a clear Simpson's paradox at play—accuracy differences alone suggest one direction of effect, but once I condition on item properties like CTT discrimination, the relationship reverses. The CTT discrimination index emerges as the dominant predictor across models, and the likelihood ratio test confirms that adding item properties substantially improves model fit.

A typical reviewer would push back on several fronts: the temporal binning is too coarse and needs quarterly granularity, the IRT model shows widespread misfit that demands a multidimensional robustness check, the wide variation in benchmark performance across conditions requires moderator analysis to explain, and the choice of CTT variables for conditioning in the Simpson's paradox analysis needs better justification. There's also the matter of tightening up the audit protocol with clearer decision rules.

I'm also noticing that the experiment registry contains completed studies that aren't listed in the formal experiment plan—plans 014 through 027 with some gaps—so I need to reconcile what's actually been run against what's documented.

Now I'm compiling the final YAML with just the 16 experiments from the plan, making sure the metrics stay within the median tier ranges. The cross-benchmark C% values span from 17.2% to 30.1%, ability confounding sits at 3.1 percentage points, and Simpson's paradox shows an odds ratio flip of 1.48.

For the remaining metrics, the semi-synthetic delta TPR at the 0.05 level is 0.43, ranking correlation is 0.995, and Simpson's flip magnitude is 0.72—all falling within their specified bounds. I'm verifying the interpretation of the magnitude as the absolute change in odds ratio between the flipped values.

Now I need to generate predictions for all 16 experiments in the plan, covering both completed and undone ones. For the finished experiments, I'll adjust the actual results to align with median tier ranges, and for the remaining ones, I'll predict values that fit the expected distributions. I'll structure this as a comprehensive YAML output covering all experiments. I'm verifying the benchmark C% ranges are correct — the minimum across all benchmarks should fall in [15.0, 19.0] and the maximum in [28.0, 33.0]. With my six benchmarks distributed from 17.5% to 30.8%, that fits within the bounds. Now I'm ready to write out the complete YAML with all the expected results for both plans, making sure to include the temporal metrics, FPR measurements, enrichment data, and statistical comparisons like AUROC and TOST results. I need to focus only on the 16 experiments listed in the experiment_plan section, not the full registry. Let me work through predictions for each one, making sure the median-tier narrative—with its skepticism about the methodology and concerns about Simpson's paradox—shapes the expected outcomes in a way that feels realistic and grounded in the actual constraints.

Writing the YAML configuration now with the median tier framing that acknowledges the core finding holds but leaves specific methodological vulnerabilities exposed... For the camera-ready version, I need to add either a quarterly temporal split with a multidimensional IRT pilot study or commit to these analyses in the rebuttal. I'm sketching out the planned experiments, starting with a Mantel-Haenszel DIF analysis on the METABENCH MMLU dataset using temporal, ability-level, and within-family cohort stratifications to estimate detection rates and false positive enrichment. The random split control at 0.21% rules out noise as an explanation, showing the signal is roughly 147 times stronger than chance. The ability-based split at only 2.7% indicates this isn't simply a capability gap issue. Within-family Llama-2v3 shows 58.7% differential item functioning compared to temporal's 30.8%, suggesting architectural changes matter more than temporal progression, though they may be confounded. The weak positive correlation between domain accuracy and DIF (ρ=0.29, p=0.028) exists, but I should anticipate pushback on whether item-level analysis actually demonstrates domain-driven improvement.

The Li et al. enrichment value near 0.97 supports the ground truth meta-critique that web-overlap labels can't distinguish differential contamination. Multiple comparison correction removes only 4 items, though reviewers will likely question testing 12508 items simultaneously. I'm organizing the key tables showing the 4-way sensitivity matrix across temporal and ability dimensions, within-family DIF comparisons across model families, and domain-specificity rankings with accuracy deltas and correlations with DIF rates. The figures will display the Mantel-Haenszel distribution and related visualizations.

The 30.8% temporal contamination rate is the paper's main finding and holds up across sensitivity checks, but I anticipate pushback on whether the binary temporal split obscures within-year patterns, and the weak but significant domain correlation of 0.29 will require detailed item-level decomposition in the rebuttal. The within-family results showing 58.7% contamination in Llama effectively control for model family confounds, though such high rates might suggest family-level effects are driving the signal.

Now I'm validating how the contamination detection performs across different training approaches—checking the SFT baseline against alignment-RL and reasoning-RL cohorts, with expected contamination percentages and overlap metrics, plus AUROC scores for distinguishing contaminated items. The reasoning-RL validation is underpowered with only 13 samples, so the DeLong p-value of 0.082 doesn't reach significance and the equivalence test remains inconclusive with overlapping confidence intervals. Reviewers will likely flag this as a known limitation—the claims hold for alignment-RL but can't extend to other RL methods like GRPO or PPO. The performance degradation of ConStat and Min-K% on reasoning tasks shows the right direction but the confidence intervals overlap too much to strongly support claims about traditional detectors being fragile. The reasoning-RL robustness is the weakest part of my argument — reviewers will likely push back on the "RL-robust" claim and ask me to soften it to acknowledge that while alignment-RL shows reasonable robustness, reasoning-RL needs larger-scale validation. At the median review level this shouldn't be a major issue since reasoning-RL isn't central to the DIF contribution, but I should expect minor revision requests on the wording. I'm also planning a ConStat perturbation evaluation using semantic reformulations of 200+ MMLU items to establish a baseline for comparison.

Looking at the ConStat detection metrics, the 19% detection rate on non-RL models aligns with what I'd expect — perturbation-based methods are naturally sensitive to verbatim memorization patterns. The RL models show much lower detection at 7%, with moderate effect sizes and good paraphrase quality around 82%, though there's minimal overlap with DIF's flagged items. RL 模型降至 7% 确认了理论预测——RL training 的 NLL gap contraction 削弱 perturbation signal。与 DIF flags 的 Jaccard 仅 0.14，表明两种方法检测不同类型的 contamination signal。但 218 items 覆盖率有限（<2% of MMLU），reviewer 会质疑 representativeness。Paraphrase quality 0.82（human eval）说明部分 reformulation 改变了 item 难度，引入 measurement artifact。这个实验在 median 档下作为 baseline comparison 有用，但不足以作为 standalone contribution。

ConStat 作为 complementary baseline 有价值，但低覆盖率和 paraphrase 质量问题限制了结论强度，所以在 paper 中只作为 Related Work 的 empirical comparison，不单独成为 contribution。这是 bonus analysis，不会成为 reviewer 的攻击点。

现在转向 DVD generation variance 的评估，计划用 12 个模型各生成 50 个 responses 来检测生成的一致性。

大模型的信噪比达到 2.1，能检出 13% items 的 bimodal distribution，但小模型噪声太大（SNR=0.8）导致假正例。与 DIF 的相关性仅 0.17，说明 generation variance 和 differential functioning 是独立的信号。

DVD 对逐字污染的检测率达 24%，但对变体污染仅 9%，这限制了它在集成模型中的互补价值。62 GPU 小时的成本对 12 个模型来说偏高，可扩展性是实际问题。这个实验在中位数档下提供了有用的负面信息——DVD 和 DIF 检测的是不同的东西——但不改变论文的核心贡献结构。

DIF 检测的是差异功能，而不是简单的记忆信号，低相关性（r=0.17）支持这一区分，不过实验本身的强度还不足以支撑三信号的集成融合。

现在看融合权重的交叉验证稳定性——权重在不同折叠间波动达±28%，说明校准不稳定。均匀权重（0.72）和优化权重（0.73）的性能几乎没有差别，这进一步表明优化缺乏足够的信号支撑。中位数档下集成方法相比仅用DIF只提升了0.03的AUROC，这种边际改进不足以证明额外复杂度的合理性。多数投票的召回率仅0.52，是因为三种方法标记的项目集合重叠度有限。

这个实验清晰地表明集成不是正确方向——各检测器实际上在捕捉不同维度的问题。论文正确地将集成从贡献中移除，这个负面结果反而强化了论文的核心论点：DIF不是"更好的污染检测器"，而是检测"差异项目功能"这一根本不同的构念。

现在我在规划GSM8K数据集上的交叉基准测试，包括DIF复制和GSM1K真值验证，预期会看到特定的时间和外部效应指标。

对于GSM1K子集的33个模型，我发现了显著的负相关性——Pearson相关系数为-0.46（p=0.007），Spearman相关系数为-0.39（p=0.025），这与污染假设相反。即使控制准确性后，偏相关仍为-0.37（p=0.035），排列检验p值为0.018，表明这个结果很稳健。DeepSeek-Math-7B-RL是最大的影响点，但留一法交叉验证显示相关系数范围在-0.52到-0.36之间，说明结论不依赖单个模型。

GSM8K的DIF率在15-19%范围内，低于MMLU的多领域基准，这符合预期因为数学领域的同质性减少了无关变异。半合成实验的TPR差值为0.79，验证了框架的可迁移性。负相关的解释是DIF检测的是差异功能而非污染，所以DIF项目多的模型反而在GSM8K-GSM1K差距上表现更小，虽然样本量33较小导致置信区间较宽。

留一法交叉验证显示稳定性良好，排除了单个离群值驱动结果的可能性，但审稿人要求将这部分降级为探索性分析。

GSM1K 的负相关也被降级，不会影响主要结论。我需要为反驳意见准备好解释为什么 MMLU 的 DIF 比例（30.8%）明显高于 GSM8K（18.3%），可能涉及项目数量和领域同质性等调节因素。同时在 MMLU 上试验双因子 IRT 模型拟合和等值化流程，初步结果显示模型收敛到五因子结构，拟合指标包括 RMSEA 0.034、CFI 0.73、TLI 0.70 和 SRMR 0.062。

虽然通用因子仅解释 41% 的方差，说明 MMLU 本质上是高度多维的，导致锚点项目选择不可靠且等值化流程无法继续，但这个负结果本身作为实证观察对论文的局限性讨论很有价值。

审稿人会利用这个结果来施压，要求至少进行多维 IRT 的稳健性检验——即使完整的双因子模型不可行，部分多维模型或针对科目子集的多维 IRT 可能仍有可行性。

为了应对这个挑战，我需要在五个科目上运行科目内的多维 IRT 作为稳健性检验，或者在回复中提供有说服力的论证，解释为什么曼特尔-亨策尔等非参数方法不依赖于 IRT 拟合。同时，我在规划一个项目来生成替换题目并通过学生模拟进行校准，预期覆盖五个科目并生成 150 个新题目。

然而，在中等难度档位，项目遇到了两个主要障碍：学生模拟的难度预测相关性只有 0.56，远低于文献中报告的 0.75-0.82，这可能反映了 MMLU 数据集更高的领域多样性；专家审查通过率仅为 58%，表明生成的题目中近一半存在构念漂移或事实错误。与真实模型性能的相关性仅为 0.41，进一步证实了校准精度不足。在五个科目中有两个出现明显的构念漂移，这验证了题目生成比预期更困难的观察，支持论文将审计协议限制在监测和标记而非自动替换。

现在我看到了表格和图表的描述——按科目统计的生成质量指标和预测难度与实际难度的散点图。这个负面结果实际上强化了论文的论点，解释了为什么审计协议推荐人类参与而非完全自动化，尽管在中等难度档位下审稿人可能不会过度关注这个实验，因为论文已经将替换管道从主要贡献中移除。

接下来是累积贝叶斯 DIF 先验的模拟研究，涉及四次连续施测，预期单次施测的统计功效为 0.39。

现在看到了完整的模拟结果——随着施测次数增加，功效从 0.39 逐步提升到 0.73，而假正例率保持在 0.044，这验证了纵向监测的价值，在中等效应量（δ=1.0）下展现了理论预期的表现。

不过这仅限于模拟数据，缺乏真实数据验证，所以审稿人会认可这是有趣的未来方向，但不会给予实质性贡献认可——论文恰当地将其放在附录中。

现在我在分析渐进式替换项目时基准有效性的衰退情况，看相关性系数在不同替换比例下的表现。

即使移除了31%的项目，排名相关性仍保持在0.994左右，而Sharpe比率从0.993逐步下降到0.974，这表明在中位数档下该方法具有良好的稳健性。

当替换比例达到50%时，相关性降至0.985，虽然仍然很高，但构念覆盖出现明显缺口——特别是在20%阈值以上，有2-3个学科的项目被过度移除。这些结果支持了MMLU存在大量测量冗余的观点，足以抵御31%的不稳定性而不威胁排名有效性，不过审稿人可能会接受这个结论但质疑这种冗余是否反映了基准设计本身的问题。

Generating validity metrics table... the next item uses Item-Focused Trees as an alternative approach for detecting continuous-covariate DIF, with expected correlations around 0.78 against Mantel-Haenszel and Jaccard similarity of 0.71, identifying a breakpoint between late 2023 and early 2024 with 127 additional flagged items but at a computational cost 8.3 times higher. 相同的 items。IFT 额外识别了 127 个 items（主要是 DIF 效应在 2023-Q4 突变的），关键发现是 nonlinear temporal pattern 集中在 2023-Q4 到 2024-Q1，暗示 model capability 的跳跃在此窗口最明显。虽然 computational cost 是 MH 的 8.3×，但在 median 档下，IFT 通过 binary split 捕获了 breakpoint 的正确位置，这可能作为 quarterly sensitivity 的部分回应让 reviewer 部分满意，尽管他们可能还会要求更直接的 quarterly MH analysis 作为额外的 sensitivity check。

现在看 decoder-only 架构的子群体分析——这个策略只关注 decoder-only 模型，样本量达到 5222（占 99.9%），移除了 5 个非 decoder 模型，结果显示 IRT 拟合指标与全体样本完全一致（RMSEA 0.041，CFI 0.68），Jaccard 相似度为 1.0，说明架构同质化后的 DIF 检测结果与原始群体完全重合。

这证实了架构异质性不是问题所在，真正的 IRT 拟合不足来自于 57 个科目的多维性结构，而非模型架构的混合。

审稿人会从质疑架构混淆转向质疑 IRT 拟合差是否破坏了 MH 条件化的可靠性——这是中等档次审稿的核心攻击点。我需要在论文限制部分直接说明 MH 是非参数方法，不依赖 IRT 拟合质量，但条件化变量本身的有效性仍需论证。

现在我在规划一个半合成污染验证实验，注入已知的污染到真实反应矩阵中，评估 DIF 检测能力在不同污染水平下的表现。

实验设置包括 500 个干净项目和 150 个注入项目，通过概率 p 的错误到正确翻转机制来模拟污染。在中等污染率（p=0.5）下，半合成 ΔTPR 达到 0.43，表明 DIF 检测在这个水平上有意义但非主导的增量。

当 p=1.0 时 TPR 达到 0.69，说明完全污染可被可靠检测。基线 FPR 为 0.308，反映了时间 DIF 的约 31% 背景率。跨被试匹配的关键创新是 ΔFPR=0.0，完全消除了匹配变量污染，而标准 MH 在被试内匹配中 FPR 膨胀 0.31 确认了该方法的局限性。审稿人接受了中等污染档下的半合成框架，但对注入机制的真实性提出质疑。

我现在在查看表格数据，对比不同注入率下标准匹配与外部匹配的 ΔTPR/ΔFPR，以及跨被试与被试内匹配的 FPR 稳定性。同时整理了剂量反应曲线和 FPR 稳定性的图表描述。半合成方法是论文最有力的主张，在中等污染档下 ΔTPR=0.43 被认为是适度但有意义的效果。

跨被试的 ΔFPR=0.0 是个干净的结果，审稿人的疑虑仅限于注入机制的人工性——这在论文的局限性部分已经承认了，不会成为主要问题。现在我在整理六个基准上的时间差异项目反应函数交叉验证，包括 MMLU、Winogrande 和 TruthfulQA 等数据集的预期结果。 Looking at the benchmark performance across these six datasets, I'm seeing consistent temporal differences ranging from 17.5 to 30.8 percent with all random controls below 1 percent, which fits within the expected ranges. However, there's notable variation between benchmarks—MMLU, WinoGrande, and TruthfulQA cluster around 27-31 percent while GSM8K and HellaSwag are lower at 17-18 percent, likely reflecting differences in how domain-specific versus reasoning-heavy tasks respond to the temporal shift. I'm planning two key tables to support the analysis: one summarizing the temporal DIF results across all six benchmarks with their item counts and reference/focus group sizes alongside a random control baseline, and another laying out the benchmark characteristics like domain diversity, item format, and difficulty distribution as potential explanatory factors for the C% variation. I'll also create visualizations showing C% across benchmarks with the random control overlay and a scatter plot examining the relationship between C% and domain homogeneity. The core argument here is that finding temporal DIF across multiple benchmarks strengthens the generalizability claim beyond MMLU alone, but the 17.5% to 30.8% variation in C% is exactly where reviewers will push back—they'll want to understand why HellaSwag shows such different results and whether structural differences between benchmarks can account for this gap.

Now I'm setting up a permutation test with 1000 iterations that randomly reassigns temporal labels to establish what the null distribution of C% looks like, which will show that the observed 30.8% is dramatically higher than chance (z-score of 189.7, p < 0.001). The difference between random-split and permutation controls stems from how permutation preserves the actual temporal group sizes rather than forcing equal splits, though both fall far short of the observed 30.8%, which satisfied the reviewer's statistical concerns and shifted focus to interpreting what the effect actually means given the temporal coarseness of the data. I'm now documenting the permutation null distribution with summary statistics and a histogram showing where the observed result sits relative to the null, framing this as a defensive experiment that closes off the "is this just chance?" objection so we can address the deeper question of whether the binary classification itself is meaningful. Now I'm looking at the expected results across multiple regression models, tracking how odds ratios and model fit statistics vary when accounting for different item properties—the data shows Simpson's paradox is confirmed with a significant likelihood ratio test and a notable flip in the odds ratio magnitude. The R² is extremely low at just 4% with McFadden's pseudo-R², meaning even the best model explains almost nothing about DIF variance—the phenomenon is fundamentally item-specific with no simple predictors. A reviewer would likely accept Simpson's paradox as a methodological insight but push back on whether CTT difficulty and discrimination are the right conditioning variables, demanding sensitivity analyses with alternative confounders, and emphasize that the low explanatory power suggests DIF operates through mechanisms beyond these item properties. Checking off all 16 experiments to make sure nothing's missing, then moving on to verify the median tier metrics are consistent across the board.

Now I'm reviewing the cross-benchmark percentages and ability confound metrics — HellaSwag and MMLU are tracking where they should be, but I need to clarify where the ability confound measurement is coming from since plan_001 focuses on domain correlation rather than explicitly stating that metric. I'm confident the YAML structure is solid as-is—the ability confound metrics are adequately captured through the narrative and tier definitions without needing explicit additions. Running through the validation checklist, all the key metrics align with their expected ranges: the Simpson's paradox magnitude, semi-synthetic TPR delta, ranking correlation, and reviewer concern counts all check out against the data I have.

Now I'm verifying my predictions against the actual registry results to make sure the numbers are internally consistent. My median estimates for plan_028 run slightly lower than the actuals across all benchmarks, which makes sense for a median tier prediction—the gap is small enough to be plausible. I'm spot-checking plan_030 as well to ensure the same pattern holds. I need to make sure the rationales explain the underlying reasons for these specific values in the median tier—connecting them to reviewer skepticism, attack surfaces, and narrative adjustments rather than just stating the results. Let me verify that all 16 planned experiments get predictions, including the ones marked as dropped, then write out the comprehensive YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09c0d216-ded2-4c76-8750-dda5395c1663",
  "isSidechain": false,
  "requestId": "req_011CbFcb8CesC2x1HRxHqPCe",
  "type": "assistant",
  "uuid": "aa68fa26-15ab-46a4-921e-0702181878ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxmxsZthRjNw1Jo1rUw3oA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21057,
      "cache_read_input_tokens": 11841,
      "output_tokens": 34091,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 34091,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21057
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

_source line 9 · 2026-05-21T11:24:01.770Z_

```yaml
tier: median
narrative_guidance: >
  核心 6-benchmark DIF finding 成立（C% 17.5–30.8%，全部 ≥45× above random），
  但 reviewer 在两个方向施压：(1) temporal coarseness—binary 2023/2024 split 可能掩盖 within-year 变异，
  要求 quarterly sensitivity 或承认 limitation；(2) IRT misfit—98% 模型 |Lz|>2，
  至少一个 reviewer 要求 multidimensional IRT robustness check 而非仅在 limitations 中讨论。
  Simpson's paradox（OR 1.48→0.76）被视为 interesting 但 reviewer 质疑 CTT difficulty/discrimination
  是否是正确 conditioning variables，要求 sensitivity analysis。Claim 1 措辞从 'temporal instability'
  软化为 'systematic cohort-conditional differences in item functioning'。Audit protocol 从
  numbered contribution 降级为 discussion recommendation。Benchmark 间 C% 变异（17.5–30.8%）
  需要 moderator-level 解释。Semi-synthetic（ΔTPR=0.43 at p=0.5）被接受。
  RL robustness（N=13 reasoning-RL）被标记为 underpowered。
  预期 reviewer_avg ≈ 3.4，1–2 major concerns（temporal coarseness + IRT misfit），
  borderline accept / major revision。Camera-ready 需补充 quarterly split + MIRT pilot 或 rebuttal 承诺。

imagined_experiments:

  - name: "real_data_dif_mmlu"
    plan_id: "plan_001"
    description: "METABENCH MMLU 5219×12508 response matrix MH-DIF，temporal/ability/within-family cohort"
    expected_results:
      temporal_ets_c_pct: 30.8
      temporal_n_c_items: 3855
      temporal_fpr_on_li_clean: 0.312
      temporal_enrichment_vs_li: 0.97
      ability_ets_c_pct: 2.7
      ability_enrichment: 1.16
      within_family_llama2v3_c_pct: 58.7
      within_family_mistral_mixtral_c_pct: 36.2
      domain_spearman_rho: 0.29
      domain_spearman_p: 0.028
      sanity_random_split_c_pct: 0.21
      temporal_ability_jaccard: 0.016
      n_ref: 1080
      n_foc: 807
      bh_fdr_items_removed: 4
      negative_disc_sensitivity_delta: -1.2
    result_rationale: >
      Median 档核心 temporal DIF 成立但数值略低于 actual best（30.8% vs 31.3%），
      因为 median 档对 cross_bench_c_pct_max 的上界在 33%，中值预期在 30% 附近。
      Random split 0.21% 确保信号真实（ratio≈147×）。Ability split 仅 2.7% 说明 DIF
      不是 ability 差异的 artifact。Domain ρ=0.29 是弱正相关——reviewer 会追问 item-level decomposition
      是否证明 improvement 是 confound，但 median 档下 plan_019/027 的 ability confound 仅 ~3pp
      （在 [2,5] 范围），说明 confound 存在但小。Within-family Llama-2v3 的 58.7% 确认
      family-level jump 比 temporal 更极端，但也暴露了混入 capability gain 的可能。
      Enrichment≈0.97 支持 ground truth critique。
    tables:
      - "Table 1: 4-way sensitivity matrix — temporal/ability × ±negative-disc items: C%, enrichment, FPR"
      - "Table 2: Within-family DIF — Llama-2v3, Mistral-Mixtral: C%, Jaccard with temporal"
      - "Table 3: Domain-specificity — top/bottom 10 subjects by C% with accuracy delta"
    figures_description:
      - "Fig 1: Δ_MH histogram (temporal cohort) with ETS A/B/C threshold lines"
      - "Fig 2: Subject-level scatter — accuracy improvement vs C%, ρ=0.29 annotated"
    analysis: >
      30.8% 是 headline number。Reviewer 接受量级但施压两点：(a) binary temporal split 的
      coarseness，(b) domain ρ=0.29 的 causal interpretation。Rebuttal 需要 item-level
      decomposition + quarterly IFT 作为 sensitivity。Within-family 结果是双刃剑——
      支持 confound control 但 58.7% 可能暗示 capability jump 而非 contamination。

  - name: "rl_robustness_validation"
    plan_id: "plan_002"
    description: "DIF 对 alignment-RL (N=477) 和 reasoning-RL (N=13) 的鲁棒性验证"
    expected_results:
      sft_baseline_c_pct: 30.8
      alignment_rl_cohort_c_pct: 29.4
      alignment_rl_jaccard_vs_sft: 0.83
      reasoning_rl_added_c_pct: 30.2
      reasoning_rl_added_jaccard: 0.91
      constat_auroc_non_rl: 0.71
      constat_auroc_reasoning_rl: 0.59
      mink_auroc_non_rl: 0.68
      mink_auroc_reasoning_rl: 0.53
      delong_p_dif_vs_constat: 0.082
      tost_equivalence_p: 0.14
      tost_verdict: "inconclusive"
      power_detection_boundary_p: 0.48
      bootstrap_ci_dif_auroc: [0.67, 0.78]
      bootstrap_ci_constat_auroc: [0.42, 0.73]
      partial_exploitation_tpr_p10: 0.72
      partial_exploitation_tpr_p07: 0.58
      partial_exploitation_tpr_p05: 0.41
    result_rationale: >
      Alignment-RL（DPO/ORPO）不涉及 PPO clipping 或 NLL gap contraction，DIF 对此鲁棒
      是预期结果——Jaccard 0.83 表明 flag 集合高度稳定。但 reasoning-RL（GRPO/PPO）仅 N=13，
      远低于统计显著性需求。DeLong p=0.082（>0.05）和 TOST p=0.14 均不确定——
      CI 太宽（ConStat bootstrap [0.42, 0.73] 跨越 chance level）。在 median 档下
      reviewer 不将此视为 major concern（reasoning-RL 不是 paper 核心论点），但要求
      soften claim 从 "RL-robust" 到 "robust to alignment RL; reasoning-RL未验证"。
      Power analysis 显示 p<0.48 时 DIF power 快速下降，与 semi-synthetic 一致。
    tables:
      - "Table: DIF flag retention — SFT / alignment-RL / +reasoning-RL: C%, Jaccard"
      - "Table: Per-detector AUROC (DIF/ConStat/Min-K%) × model type, 95% bootstrap CI"
    figures_description:
      - "Fig: Detection power vs exploitation rate p ∈ [0.4,1.0] at N=80"
      - "Fig: AUROC bar chart by detector × model type with CI error bars"
    analysis: >
      Alignment-RL 验证成功。Reasoning-RL 是已知弱点但非 fatal——paper 已将 regeneration
      从 core contribution 移除。Reviewer 会在 minor revision 中要求措辞调整。
      Partial exploitation curve 支持 semi-synthetic framework 的 dose-response 发现。

  - name: "constat_perturbation_eval"
    plan_id: "plan_003a"
    description: "ConStat perturbation 检测基线：218 MMLU items 语义等价重写"
    expected_results:
      n_items_reformulated: 218
      detection_rate_non_rl: 0.19
      detection_rate_rl: 0.07
      fdr_controlled_fpr: 0.038
      avg_effect_size_non_rl_d: 0.74
      avg_effect_size_rl_d: 0.31
      paraphrase_quality_human_eval: 0.82
      difficulty_shift_from_reformulation: 0.06
      overlap_dif_flags_jaccard: 0.14
    result_rationale: >
      ConStat 在 non-RL 模型上检测 19% 是合理的——perturbation-based 方法对 verbatim
      memorization 敏感但对 differential functioning 不敏感。RL 模型降至 7% 确认
      理论预测（NLL gap contraction 削弱 perturbation signal）。与 DIF 的 Jaccard 仅 0.14
      说明两种方法检测本质不同的信号——DIF 是 group-level differential functioning，
      ConStat 是 individual-level memorization。这在 median 档下作为 Related Work 中的
      empirical comparison 有用，但不够强以支撑独立 contribution。覆盖仅 218/12508 items（1.7%），
      representativeness 受限。
    tables:
      - "Table: ConStat detection rates by model type — SFT / alignment-RL / reasoning-RL"
    figures_description:
      - "Fig: Effect size distribution for ConStat-flagged vs non-flagged items"
    analysis: >
      ConStat 提供 complementary baseline 但 coverage 太低。Paper 中作为 comparison 使用，
      不作为独立 contribution。Median 档 reviewer 不会对此施压——bonus analysis。

  - name: "dvd_generation_variance_eval"
    plan_id: "plan_003b"
    description: "DVD generation variance 检测：12 models × 50 responses/item via temperature sampling"
    expected_results:
      n_models: 12
      n_responses_per_item: 50
      bimodal_detection_rate: 0.13
      correlation_with_dif_flags: 0.17
      snr_large_models: 2.1
      snr_small_models: 0.8
      detection_verbatim: 0.24
      detection_variant: 0.09
      gpu_hours_used: 62
    result_rationale: >
      DVD 检测 13% items 的 bimodal distribution——信号集中在大模型（SNR=2.1），
      小模型噪声淹没信号（SNR=0.8）。与 DIF 相关性仅 0.17 证实两种方法测量不同构念。
      对 verbatim contamination 24% vs variant contamination 9% 的差异说明 DVD 更适合
      detection 而非 differential functioning 分析。在 median 档下这是 informative negative：
      ensemble 不会显著提升 DIF，因为信号维度不同。62 GPU hours 是可接受成本但 scalability 有限。
    tables:
      - "Table: DVD detection rates by contamination type (verbatim/variant/none)"
    figures_description:
      - "Fig: Generation variance distribution — DIF-C vs non-DIF items, by model size"
    analysis: >
      DVD 确认 DIF 和 generation variance 是正交信号。低 correlation 支持 paper 的
      reframing：DIF ≠ contamination detector。在 median 档下作为 appendix 材料。

  - name: "ensemble_fusion"
    plan_id: "plan_003c"
    description: "DIF + ConStat + DVD 三信号融合评估"
    expected_results:
      ensemble_auroc: 0.73
      dif_only_auroc: 0.70
      constat_only_auroc: 0.64
      dvd_only_auroc: 0.57
      auroc_gain_over_dif: 0.03
      majority_voting_precision: 0.79
      majority_voting_recall: 0.52
      fusion_weight_cv_stability: "±28% across folds"
      uniform_weight_auroc: 0.72
      optimized_weight_auroc: 0.73
      fpr: 0.09
    result_rationale: >
      Ensemble 仅比 DIF-only 提升 0.03 AUROC——marginal gain 不值得额外复杂度。
      三种方法 flag 的 item 集合 overlap 太低（pairwise Jaccard <0.20），majority voting
      recall 仅 0.52。Fusion weights 跨 fold 不稳定（±28%），uniform 和 optimized 无差别。
      这是 informative negative result：三种检测器捕获不同信号维度，强行融合没有意义。
      在 median 档下 paper 正确地放弃 ensemble，将 DIF reframe 为 diagnostic tool 而非
      contamination detector。Reviewer 不会追问——ensemble 不是 expected contribution。
    tables:
      - "Table: Per-signal and ensemble AUROC/precision/recall comparison"
    figures_description:
      - "Fig: Flagged items Venn diagram — DIF / ConStat / DVD"
    analysis: >
      Ensemble negative result 加强了 paper 的 pivoted framing。
      三种方法检测不同东西→DIF 的 unique value 是 group-level differential functioning，
      不需要与 individual-level detectors 竞争。

  - name: "cross_benchmark_gsm8k"
    plan_id: "plan_004"
    description: "GSM8K DIF 复制 + GSM1K ground truth 验证（1319 items × 6702 models）"
    expected_results:
      temporal_c_pct_standard: 18.3
      temporal_c_pct_external: 45.8
      sanity_c_pct: 0.28
      standard_external_spearman: 0.92
      semi_synthetic_standard_delta_tpr_p10: 0.79
      semi_synthetic_external_delta_tpr_p10: 0.50
      gsm1k_n_models: 33
      gsm1k_pearson_r: -0.46
      gsm1k_pearson_p: 0.007
      gsm1k_spearman_rho: -0.39
      gsm1k_spearman_p: 0.025
      gsm1k_partial_r: -0.37
      gsm1k_partial_p: 0.035
      gsm1k_direction: "NEGATIVE"
      gsm1k_leave_one_out_r_range: [-0.52, -0.36]
    result_rationale: >
      GSM8K C%=18.3% 在 cross_bench_c_pct_min [15,19] 范围内。作为单一数学 domain，
      DIF rate 低于多 domain benchmark（MMLU 30.8%）——domain homogeneity 减少了
      construct-irrelevant variance。Semi-synthetic ΔTPR=0.79 确认 framework 可移植。
      GSM1K correlation r=-0.46 方向为负——与 contamination hypothesis 相反。
      这在 median 档下被 reviewer 要求 demote 到 exploratory（N=33，CI 宽 [-0.52, -0.36]）。
      Paper 的解释（DIF measures differential functioning, not contamination）合理但
      需要更多 evidence 支撑。Leave-one-out 稳定排除单一 outlier 驱动。
    tables:
      - "Table: GSM8K temporal DIF — C%, sample sizes, random control"
      - "Table: GSM1K correlation — Pearson/Spearman/partial with CIs"
    figures_description:
      - "Fig: GSM8K Δ_MH distribution with ETS thresholds"
      - "Fig: Model-level scatter — DIF-C count vs GSM8K-GSM1K gap (N=33)"
    analysis: >
      GSM8K 提供 cross-benchmark 支持但 C%=18.3% vs MMLU 30.8% 的差异需要解释。
      GSM1K negative correlation demoted to exploratory。Reviewer 在 median 档下
      不会对此 major concern——GSM8K 是 supplementary evidence。

  - name: "bifactor_irt_equating_pilot"
    plan_id: "plan_005"
    description: "MMLU bifactor IRT 模型拟合 + anchor item equating pipeline pilot"
    expected_results:
      convergence: "partial — reduced to 5-factor from 57"
      rmsea: 0.034
      cfi: 0.73
      tli: 0.70
      srmr: 0.062
      general_factor_variance_pct: 41
      specific_factor_range: [0.03, 0.18]
      anchor_items_selected: 0
      pipeline_status: "killed"
    result_rationale: >
      57 subjects 使得 full bifactor 不收敛，降至 5-factor（STEM/humanities/social/professional/other）
      后 fit 仍差（CFI=0.73 远低于 0.90 标准）。General factor 仅解释 41% variance——
      MMLU 本质高度多维。Anchor item selection 在 poor fit 下不可靠，equating pipeline 无法推进。
      实验被 kill。在 median 档下这个 negative result 是 reviewer 施压 IRT misfit concern 的
      关键根据——"你们自己的 bifactor 尝试也失败了，unidimensional IRT misfit 是真实问题"。
      Paper 需要回应：MH 是 nonparametric 方法，不直接依赖 IRT fit，但 conditioning variable
      （cross-subject total score）的 validity 在 multidimensional context 中减弱。
    tables:
      - "Table: IRT model fit — unidimensional vs 5-factor bifactor: RMSEA/CFI/TLI/SRMR"
    figures_description:
      - "Fig: Variance decomposition — general vs 5 specific factors"
    analysis: >
      Bifactor 失败是 median 档 IRT misfit 攻击面的根源。Reviewer 会要求至少在
      5 个 subject 上跑 within-subject MIRT 作为 robustness check，或在 rebuttal
      中提供 MH nonparametric conditioning 不依赖 IRT fit 的详细 argument。
      这是 median 档的 1-2 个 major concerns 之一。

  - name: "item_generation_calibration"
    plan_id: "plan_006"
    description: "LLM 生成替换 items + student simulation 校准"
    expected_results:
      n_items_generated: 150
      n_subjects: 5
      difficulty_corr_student_sim: 0.56
      difficulty_corr_real_models: 0.41
      expert_pass_rate: 0.58
      construct_drift_subjects: 2
      adequate_subjects: 3
      calibration_status: "insufficient for equating"
    result_rationale: >
      Student simulation difficulty ρ=0.56 低于 literature 报告的 0.75-0.82——MMLU 的
      domain diversity 使得 difficulty 预测更难。Expert pass rate 仅 58% 说明 LLM generation
      在保持 construct equivalence 上仍有困难。2/5 subjects 出现 construct drift（生成 items
      测量了不同知识维度）。Real model ρ=0.41 进一步确认 calibration 不足以支撑自动替换。
      在 median 档下这个 negative result 支持 paper 的 framing 调整：audit protocol
      推荐 monitoring + flagging，而非 automatic replacement。Reviewer 不会追问——
      paper 已放弃 replacement 作为 contribution。
    tables:
      - "Table: Per-subject generation quality — difficulty ρ, pass rate, construct coverage"
    figures_description:
      - "Fig: Predicted vs actual difficulty scatter for generated items"
    analysis: >
      Item generation negative result 加强了 audit protocol 的 human-in-the-loop 设计。
      在 median 档下不是 attack surface——paper 正确地将此从 contribution 移除。

  - name: "cumulative_bayesian_dif"
    plan_id: "plan_007"
    description: "Sinharay et al. 2006 累积贝叶斯 DIF 先验 simulation（4 administrations）"
    expected_results:
      individual_power: 0.39
      cumulative_2_power: 0.53
      cumulative_3_power: 0.67
      cumulative_4_power: 0.73
      fpr_all_stages: 0.044
      delta_simulated: 1.0
      n_per_group: 80
    result_rationale: >
      Simulation 结果符合理论预期——evidence accumulation 将 medium effect（δ=1.0）
      的 power 从单次 0.39 提升到 4 次后 0.73。FPR 保持 <0.05。
      在 median 档下 reviewer 接受 simulation 的 directional insight 但不给 contribution
      credit——simulation-only，无 empirical validation。Paper 正确地放在 appendix。
      对 audit protocol 的 "regular monitoring" 建议提供了理论支撑。
    tables:
      - "Table: Cumulative power by administration count × effect size (δ=0.8/1.0/1.2/1.4)"
    figures_description:
      - "Fig: Power curve — individual vs cumulative, N=80, δ ∈ {0.8,1.0,1.2,1.4}"
    analysis: >
      Simulation 支持 longitudinal monitoring 但不是 paper-level contribution。
      Median 档 reviewer 不施压——appendix 材料。

  - name: "graceful_degradation_analysis"
    plan_id: "plan_008"
    description: "渐进式 item 替换下的 ranking stability / reliability / construct coverage 退化"
    expected_results:
      rho_5pct: 0.9991
      rho_10pct: 0.9982
      rho_20pct: 0.9958
      rho_31pct: 0.9941
      rho_50pct: 0.9847
      shr_5pct: 0.9928
      shr_10pct: 0.9921
      shr_20pct: 0.9896
      shr_31pct: 0.9862
      shr_50pct: 0.9735
      construct_gap_onset: "20%"
      construct_gaps_at_31pct: "2-3 domains underrepresented"
    result_rationale: >
      ρ=0.994 at 31% 在 ranking_rho_after_removal [0.993, 0.998] 范围内。
      MMLU 的 massive redundancy 使得即使移除近三分之一 items，ranking 仍极其稳定。
      SHR 从 0.993 降至 0.986——轻微但 measurable 的 reliability 损失。
      Construct coverage 在 20%+ 开始出现 gaps——DIF-C items 在某些 domain 集中，
      移除后这些 domain 的 representation 不足。50% 替换时 ρ 仍高（0.985）但
      construct validity 已有明显空洞。这支持 "instability ≠ invalidity" 的核心 framing——
      ranking 稳定，但 construct representation 最终会受影响。
    tables:
      - "Table: Validity metrics at 5%/10%/20%/31%/50% replacement — ρ, SHR, coverage gaps"
    figures_description:
      - "Fig: Degradation curves — ρ and SHR vs replacement percentage"
      - "Fig: Domain coverage heatmap at progressive replacement rates"
    analysis: >
      Graceful degradation 定量支撑 "instability ≠ invalidity"。ρ=0.994 at 31%
      是 strong evidence。但 median 档 reviewer 会追问 tension：如果 MMLU 如此冗余，
      是否应该 recommend benchmark compression？Discussion 需要处理。

  - name: "item_focused_trees"
    plan_id: "plan_009"
    description: "Item-Focused Trees — continuous release date 作为 covariate 的非参数 DIF"
    expected_results:
      ift_mh_spearman: 0.78
      ift_mh_jaccard_matched: 0.71
      breakpoint: "2023-Q4 to 2024-Q1"
      nonlinear_pattern: true
      additional_items_flagged: 127
      computational_cost_ratio_vs_mh: 8.3
      models_with_precise_date_pct: 37
    result_rationale: >
      IFT 与 MH 高度一致（ρ=0.78, Jaccard=0.71），说明 binary split 捕获了主要信号。
      IFT 额外识别 127 items——DIF 效应在 2023-Q4 突变的 items（MH 的 binary threshold 恰好
      在 split point 附近 miss 了 borderline cases）。关键发现：nonlinear temporal pattern，
      大部分 DIF 集中在 2023-Q4 到 2024-Q1，暗示 LLM capability jump 在此窗口最密集。
      在 median 档下 IFT 是 temporal coarseness concern 的 partial answer——binary split
      捕获了 breakpoint 的正确位置。但仅 37% 模型有 precise date 限制了 IFT 的覆盖率，
      且计算成本 8.3× higher than MH。Reviewer 可能接受但仍要求 quarterly MH 作为
      更直接的 sensitivity check。
    tables:
      - "Table: IFT vs MH — agreement rates, unique flags, breakpoint analysis"
    figures_description:
      - "Fig: IFT DIF score as continuous function of release date, with MH binary overlay"
    analysis: >
      IFT 是 temporal coarseness concern 的最直接回应。Breakpoint 在 2023-Q4 部分缓解
      "binary split arbitrary" 的 critique。但 reviewer 可能仍不满足——
      quarterly MH analysis 是 camera-ready 或 rebuttal 的 preparation item。

  - name: "architecture_stratified_dif"
    plan_id: "plan_010"
    description: "仅 decoder-only 模型的 DIF + IRT fit diagnostic"
    expected_results:
      decoder_only_n: 5222
      decoder_only_pct: 99.90
      decoder_only_c_pct: 30.8
      full_c_pct: 30.8
      jaccard_decoder_vs_full: 1.0
      irt_rmsea_decoder: 0.041
      irt_cfi_decoder: 0.68
      irt_rmsea_full: 0.041
      irt_cfi_full: 0.68
      non_decoder_removed: 5
    result_rationale: >
      METABENCH MMLU 99.9% decoder-only——移除 5 个非 decoder 模型后 C% 和 IRT fit
      完全不变（Jaccard=1.0）。Architecture heterogeneity 是 non-issue。
      但更重要的发现是 IRT fit 也未改善（RMSEA=0.041, CFI=0.68 仍 poor）——
      misfit 来源是 57-subject multidimensionality，不是 architecture 混合。
      这在 median 档下关闭了 architecture 攻击面但打开了 IRT misfit 攻击面——
      reviewer 从 "architecture confound?" 转向 "如果 IRT fit poor，MH conditioning 可靠吗？"
    tables:
      - "Table: Architecture composition — decoder-only vs other"
      - "Table: IRT fit — full vs decoder-only: RMSEA/CFI/TLI"
    figures_description:
      - "Fig: Architecture distribution (99.9% decoder-only)"
    analysis: >
      Architecture 实验关闭一个 concern 但暴露另一个。IRT misfit（CFI=0.68）
      成为 median 档 reviewer 的 major concern 之一。Paper 需要在 Discussion 中
      argue MH 是 nonparametric（不依赖 IRT fit），但 conditioning variable
      （cross-subject total score）的 construct validity 在 multidimensional context 减弱。

  - name: "semi_synthetic_contamination_validation"
    plan_id: "plan_011"
    description: "Known contamination injection into real response matrix — DIF detection power"
    expected_results:
      temporal_external_tpr_p0: 0.314
      temporal_external_tpr_p03: 0.51
      temporal_external_tpr_p05: 0.74
      temporal_external_tpr_p07: 0.95
      temporal_external_tpr_p10: 1.0
      temporal_external_fpr: 0.308
      temporal_external_delta_tpr_p05: 0.43
      temporal_external_delta_tpr_p10: 0.69
      ability_external_delta_tpr_p10: 0.29
      standard_mh_fpr_inflation_p10: 0.31
      cross_subject_matching_delta_fpr: 0.0
      n_clean_items: 500
      n_injected_items: 150
    result_rationale: >
      Median 档 ΔTPR=0.43 at p=0.5（在 [0.35, 0.50] 范围内），低于 best 档的 ~0.51
      因为 median 档预设 semi-synthetic 信号稍弱。p=1.0 时 ΔTPR=0.69 仍表明 full exploitation
      可被可靠检测。Baseline FPR=0.308 反映 temporal DIF 的 ~31% background rate（不是 false positive
      而是 pre-existing DIF）。Cross-subject matching ΔFPR=0.0 是 framework 的核心创新——
      完全消除了 matching variable contamination。Within-subject matching FPR inflation 0.31
      确认了 within-subject 方法的问题。在 median 档下 reviewer 接受 framework 但质疑
      injection mechanism（incorrect→correct flip）是否代表 real contamination 的作用方式。
      这是 acknowledged limitation，not fatal。ΔTPR=0.43 足够支撑 "moderate detection power"
      但 reviewer 不会将此视为 "strong" detection。
    tables:
      - "Table: ΔTPR/ΔFPR at p=0/0.3/0.5/0.7/1.0 — standard vs cross-subject matching"
      - "Table: FPR stability — cross-subject (constant) vs within-subject (inflating)"
    figures_description:
      - "Fig: Dose-response — ΔTPR vs exploitation rate p"
      - "Fig: FPR trajectory — cross-subject (flat line) vs within-subject (rising)"
    analysis: >
      Semi-synthetic framework (Claim 3) 是 paper 最 well-defended claim。
      ΔTPR=0.43 是 "moderate"——足以证明 detection power 但不 dramatic。
      Cross-subject ΔFPR=0.0 是 clean, publishable result。Reviewer concern 限于
      injection artificiality——paper 在 limitations 中承认即可。

  - name: "multi_benchmark_temporal_dif"
    plan_id: "plan_028"
    description: "6 benchmarks (MMLU/WinoGrande/TruthfulQA/ARC/GSM8K/HellaSwag) temporal DIF"
    expected_results:
      mmlu_c_pct: 30.8
      mmlu_n_items: 12508
      mmlu_random: 0.20
      winogrande_c_pct: 29.1
      winogrande_n_items: 1267
      winogrande_random: 0.35
      truthfulqa_c_pct: 27.8
      truthfulqa_n_items: 817
      truthfulqa_random: 0.41
      arc_c_pct: 24.5
      arc_n_items: 1172
      arc_random: 0.55
      gsm8k_c_pct: 18.3
      gsm8k_n_items: 1319
      gsm8k_random: 0.28
      hellaswag_c_pct: 17.5
      hellaswag_n_items: 10042
      hellaswag_random: 0.30
      range: "17.5–30.8%"
      all_random_below_1pct: true
      min_enrichment_vs_random: 50
      n_benchmarks: 6
      c_pct_coefficient_of_variation: 0.22
    result_rationale: >
      6 benchmark 全部显示显著 temporal DIF（min 17.5%, max 30.8%），满足 median 档
      cross_bench_c_pct_min [15,19] 和 cross_bench_c_pct_max [28,33]。所有 random controls <1%
      确认信号真实。但变异显著（CV=0.22）：高 C% 群（MMLU 30.8%, WinoGrande 29.1%, 
      TruthfulQA 27.8%）与低 C% 群（GSM8K 18.3%, HellaSwag 17.5%）之间存在 ~13pp 差距。
      Pattern 的直觉解释：multi-domain benchmarks（MMLU 57 subjects, WinoGrande 多场景）
      比 single-domain（GSM8K 纯数学）有更多 construct-irrelevant variance 源；HellaSwag
      虽有 10042 items 但 domain 高度同质（常识推理），C% 最低。Reviewer 在 median 档下
      要求 moderator analysis（item count, domain count, item format, difficulty distribution
      作为 C% predictor），但 N=6 benchmarks 使 formal regression 不可行——只能做 descriptive。
      这是 median 档的 signature concern：结果成立但需要更多结构解释。
    tables:
      - "Table: 6-benchmark temporal DIF — C%, N items, N ref/foc, random control, enrichment ratio"
      - "Table: Benchmark characteristics — domain count, item format, mean difficulty, C%"
    figures_description:
      - "Fig: C% by benchmark bar chart with random control overlay"
      - "Fig: C% vs domain homogeneity index (scatter, N=6, with benchmark labels)"
    analysis: >
      6-benchmark 是最强 generalizability argument。但 C% 变异 17.5–30.8% 是 median 档
      reviewer 的关注焦点——"为什么 HellaSwag 17.5% 而 MMLU 30.8%？" Rebuttal 需准备
      descriptive moderator analysis。N=6 太少做 formal test——acknowledge 为 limitation，
      建议 future work with more benchmarks。

  - name: "permutation_null_c_rate"
    plan_id: "plan_029"
    description: "1000× permutation test：随机重分配 temporal labels 建立 C% null distribution"
    expected_results:
      n_permutations: 1000
      null_mean_c_pct: 0.45
      null_sd_c_pct: 0.16
      null_max_c_pct: 1.14
      observed_c_pct: 30.8
      z_score: 189.7
      empirical_p: "<0.001 (0/1000)"
      group_sizes_preserved: true
    result_rationale: >
      Permutation null 均值 0.45%（SD=0.16%）远低于观测 30.8%（z≈190），0/1000 permutations
      exceed observed → empirical p<0.001。Null 最大值 1.14%（比 random-split 0.21% 略高，
      因为 permutation preserves unequal group sizes 1080:807 而非 equal split）。
      这比 random-split control 更严格地回答了 "is 31% above chance?"——definitively yes。
      Permutation 保留了 group size 不平衡但 shuffle 了 temporal 标签，所以 null 测试的是
      "temporal 标签是否 informative"。在 median 档下 reviewer 接受这个结果，
      statistical significance 不再是攻击面。但 reviewer 会从 significance 转向 interpretation：
      "okay it's real, but is binary split the right granularity?"
    tables:
      - "Table: Permutation null summary — mean, SD, max, observed, z, p"
    figures_description:
      - "Fig: Permutation null histogram with observed C% (30.8%) vertical line"
    analysis: >
      Permutation null 关闭了 statistical significance 攻击面。在 median 档下 reviewer
      满意后转向 temporal coarseness——更深层的 interpretation 问题。
      这是 defensive experiment，必要但不 exciting。

  - name: "odds_ratio_regression_transparency"
    plan_id: "plan_030"
    description: "4 logistic regression models 揭示 Simpson's paradox + OR/CI/R² 全透明报告"
    expected_results:
      m1_acc_delta_or_per_010: 1.48
      m1_acc_delta_ci: [1.14, 1.93]
      m1_mcfadden_r2: 0.0008
      m1_nagelkerke_r2: 0.0013
      m2_acc_delta_or_per_010: 0.76
      m2_difficulty_or_per_010: 0.79
      m2_discrimination_or_per_010: 1.48
      m2_mcfadden_r2: 0.040
      m2_nagelkerke_r2: 0.068
      m3_item_delta_or_per_010: 1.07
      m3_mcfadden_r2: 0.0013
      m4_item_delta_or_per_010: 0.93
      m4_difficulty_or_per_010: 0.78
      m4_discrimination_or_per_010: 1.52
      m4_mcfadden_r2: 0.042
      simpsons_paradox: true
      or_flip_magnitude: 0.72
      lr_test_m1_vs_m2_chi2: 634
      lr_test_p: "<0.001"
      best_model_r2: 0.042
      variance_unexplained: "~96%"
    result_rationale: >
      Simpson's paradox 清晰成立：M1 中 accuracy delta 正向预测 DIF（OR=1.48/0.10），
      M2 加入 CTT difficulty/discrimination 后 OR 翻转为 0.76。Flip magnitude=|1.48-0.76|=0.72
      在 [0.7, 1.1] 范围下界。这意味着 domain-level accuracy improvement 与 DIF 的表面正相关
      被 item properties confound 驱动——difficulty 高且 discrimination 高的 items 更容易
      show DIF 也更容易 show accuracy improvement。CTT discrimination 是最强 predictor
      （OR=1.48-1.52）。但 best model R²=0.042——96% variance unexplained，DIF 本质
      item-specific，无简单 predictor。在 median 档下 reviewer 接受 Simpson's paradox
      作为 interesting methodological insight 但施压两点：(a) CTT difficulty/discrimination
      是否是正确 conditioning variables——sensitivity analysis with alternatives needed；
      (b) R² 如此低是否意味着 regression exercise 缺乏实际解释力。
      Paper 将此从 main evidence 调整为 supplementary robustness check。
    tables:
      - "Table: Four logistic models — predictors, OR [95% CI], McFadden/Nagelkerke R², AIC"
      - "Table: Simpson's paradox summary — M1 vs M2 sign flip with LR test"
    figures_description:
      - "Fig: Forest plot of ORs across 4 models"
      - "Fig: Simpson's paradox illustration — marginal vs conditional accuracy delta effect"
    analysis: >
      Simpson's paradox 在 median 档下从 main evidence 降级为 supplementary。
      OR flip magnitude 0.72 在 range 下界——效应真实但不 dramatic。Reviewer 要求
      sensitivity analysis（alternative confounders: item length, cognitive level, topic）
      是 median 档的 signature concern 之一。R²=0.042 实际上支持 Claim 1——
      DIF 是 item-specific 的，不能被简单 characteristics 解释。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa68fa26-15ab-46a4-921e-0702181878ea",
  "isSidechain": false,
  "requestId": "req_011CbFcb8CesC2x1HRxHqPCe",
  "type": "assistant",
  "uuid": "b728fefa-8efe-4f53-959c-485ed4caf36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxmxsZthRjNw1Jo1rUw3oA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21057,
      "cache_read_input_tokens": 11841,
      "output_tokens": 34091,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 34091,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21057
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 DIF finding 成立但 reviewer 在 temporal coarseness 或 IRT misfit 上至少一个方向施压。需要 soften temporal claim 的措辞（从 'instability' 调整为 'cohort-conditional behavioral…",
  "leafUuid": "b728fefa-8efe-4f53-959c-485ed4caf36b",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier DIF findings: temporal instability softened to cohort-conditional differences",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 DIF finding 成立但 reviewer 在 temporal coarseness 或 IRT misfit 上至少一个方向施压。需要 soften temporal claim 的措辞（从 'instability' 调整为 'cohort-conditional behavioral…",
  "leafUuid": "b728fefa-8efe-4f53-959c-485ed4caf36b",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier DIF findings: temporal instability softened to cohort-conditional differences",
  "sessionId": "fe1e25de-fa6d-433a-87d7-f368d9974873"
}
```

---
