# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Permutation null 略高于 random-split 但 31% 仍远超，部分 reviewer 质疑 novelty（'applyi

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/c2400123-8593-4207-9144-53d78fc6917c.jsonl`
- **Structured JSON:** [`b86d2726ce2e2c33671a.json`](../../sessions/b8/b86d2726ce2e2c33671a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:38:59.249Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:38:59.249Z",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Permutation null 略高于 random-split 但 31% 仍远超，部分 reviewer 质疑 novelty（'applying textbook psychometrics'），需要调整 claims 强度并补强 narrative\n核心假设：['plan_029 permutation null C% 在 2–8%：temporal label 本身有弱结构性（model release date 与 ability 不完全正交），但 31% 仍 4–15× 高于 null', \"至少一位 reviewer 认为 MH-DIF 无算法创新，要求更强的 'so what' — 需要在 rebuttal 中强化 diagnostic lens 和 audit protocol 的实用价值\", '8 页压缩迫使 Claim 3（semi-synthetic framework）的 cross-benchmark GSM8K 验证移入 appendix，主体只保留 MMLU 结果', 'GSM1K negative correlation（r=-0.478）在 review 中被追问，需要额外段落解释 DIF ≠ contamination detector', \"ability confound 的 Simpson's paradox（plan_030 Model 2 vs Model 1）在 reviewer 中引起方法论讨论，需要谨慎处理因果表述\"]\n关键指标范围：{'permutation_null_c_pct': [2.0, 8.0], 'residual_c_pct_after_all_controls': [23.0, 29.0], 'ability_confound_explained_pp': [3.0, 6.0], 'cross_benchmark_c_range_pct': [15.0, 32.0], 'semi_synthetic_delta_tpr_p05': [0.35, 0.5], 'cross_subject_delta_fpr': [0.0, 0.01], 'ranking_stability_rho': [0.993, 0.998], 'simulated_avg_reviewer_score': [2.5, 3.5], 'page_count_main_body': [8.0, 8.5]}\n叙事方向：Claim 1 headline 从 '31%' 调整为 '~25–31% depending on confound controls'，permutation null 作为 calibration baseline 显式报告。Claim 2 meta-critique 从 aggressive ('field's validation is fundamentally mismatched') 软化为 'web-overlap labels are insufficient for item-level differential detection — complementary approaches needed'。Claim 3 保留但 cross-benchmark 证据降级为 appendix。Claim 4 diagnostic lens 升格为 paper 的核心卖点（从 'finding 4' 提升到 abstract 第二句），强调 audit protocol 的实用价值来对冲 novelty 质疑。需要在 rebuttal 中准备 'psychometric tools are mature but their application to LLM benchmarks at this scale is novel' 的防线。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:38:59.253Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:38:59.253Z",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T12:38:59.275Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Permutation null 略高于 random-split 但 31% 仍远超，部分 reviewer 质疑 novelty（'applying textbook psychometrics'），需要调整 claims 强度并补强 narrative
核心假设：['plan_029 permutation null C% 在 2–8%：temporal label 本身有弱结构性（model release date 与 ability 不完全正交），但 31% 仍 4–15× 高于 null', "至少一位 reviewer 认为 MH-DIF 无算法创新，要求更强的 'so what' — 需要在 rebuttal 中强化 diagnostic lens 和 audit protocol 的实用价值", '8 页压缩迫使 Claim 3（semi-synthetic framework）的 cross-benchmark GSM8K 验证移入 appendix，主体只保留 MMLU 结果', 'GSM1K negative correlation（r=-0.478）在 review 中被追问，需要额外段落解释 DIF ≠ contamination detector', "ability confound 的 Simpson's paradox（plan_030 Model 2 vs Model 1）在 reviewer 中引起方法论讨论，需要谨慎处理因果表述"]
关键指标范围：{'permutation_null_c_pct': [2.0, 8.0], 'residual_c_pct_after_all_controls': [23.0, 29.0], 'ability_confound_explained_pp': [3.0, 6.0], 'cross_benchmark_c_range_pct': [15.0, 32.0], 'semi_synthetic_delta_tpr_p05': [0.35, 0.5], 'cross_subject_delta_fpr': [0.0, 0.01], 'ranking_stability_rho': [0.993, 0.998], 'simulated_avg_reviewer_score': [2.5, 3.5], 'page_count_main_body': [8.0, 8.5]}
叙事方向：Claim 1 headline 从 '31%' 调整为 '~25–31% depending on confound controls'，permutation null 作为 calibration baseline 显式报告。Claim 2 meta-critique 从 aggressive ('field's validation is fundamentally mismatched') 软化为 'web-overlap labels are insufficient for item-level differential detection — complementary approaches needed'。Claim 3 保留但 cross-benchmark 证据降级为 appendix。Claim 4 diagnostic lens 升格为 paper 的核心卖点（从 'finding 4' 提升到 abstract 第二句），强调 audit protocol 的实用价值来对冲 novelty 质疑。需要在 rebuttal 中准备 'psychometric tools are mature but their application to LLM benchmarks at this scale is novel' 的防线。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen
venue: emnlp-2026

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
  "promptId": "b59f4245-02f2-4fbf-849d-efb363709518",
  "type": "user",
  "uuid": "3482d95c-6531-4458-92c9-3ac2ebc92cd4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:38:59.273Z_

```json
{
  "parentUuid": "3482d95c-6531-4458-92c9-3ac2ebc92cd4",
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
  "uuid": "08a26189-a7ae-478d-bc79-d1fffb7ea45b",
  "timestamp": "2026-05-21T12:38:59.273Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:38:59.273Z_

```json
{
  "parentUuid": "08a26189-a7ae-478d-bc79-d1fffb7ea45b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "27b04091-b035-4bc1-8f56-6549627bfcd2",
  "timestamp": "2026-05-21T12:38:59.273Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Permutation null 略高于 random-split 但 31% 仍远超，部分 reviewer 质疑 novelty（'applying textbook psychometrics'），需要调整 claims 强度并补强 narrative 核心假设：['plan_029 permuta…",
  "leafUuid": "27b04091-b035-4bc1-8f56-6549627bfcd2",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier DIF analysis: characterizing MMLU temporal instability",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:39:46.077Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "median" tier definition they've provided. Let me identify which experiments are still in "planned" status:

1. plan_001 - status: planned (but registry shows plan_001_real_data_dif_mmlu as DONE)
2. plan_002 - status: planned (rl_robustness_validation)
3. plan_003a - status: planned (constat_perturbation_eval)
4. plan_003b - status: planned (dvd_generation_variance_eval)


5. plan_003c - status: planned (ensemble_fusion)
6. plan_004 - status: planned (but registry shows plan_004_gsm8k_cross_benchmark as DONE)
7. plan_005 - status: planned (bifactor_irt_equating_pilot)
8. plan_006 - status: planned (item_generation_calibration)
9. plan_007 - status: planned (cumulative_bayesian_dif)
10. plan_008 - status: planned (graceful_degradation_analysis)
11. plan_009 - status: planned (item_focused_trees)
12. plan_010 - status: planned (not in registry)
13. plan_011 - status: planned (registry shows plan_011_semi_synthetic_validation as DONE)
14. plan_028 - status: planned (registry shows plan_028_multi_bench_dif as DONE)
15. plan_029 - status: planned (permutation_null_c_rate)
16. plan_030 - status: planned (registry shows plan_030_odds_ratio as DONE)

I'm noticing a pattern here—several experiments marked as "planned" in the experiment_plan section actually show as completed in the registry. The user is asking for detailed data on each planned experiment, so I should focus on what the experiment_plan itself lists as the status, which treats them all as planned or in preparation.

Since many of these already have actual results in the registry, I think the user wants me to generate predicted detailed results for the median tier scenario, using the registry data as reference points for calibration. All the experiments in experiment_plan are marked as planned, so I'll treat them as needing full result predictions under those median tier conditions. or a previous simulation), and now they want me to generate the median-tier predicted version.

Given the median tier definition with those parameter ranges—permutation null around 2-8%, residual effects after controls between 23-29%, ability confounds explaining 3-6 percentage points, and the other metrics falling within their specified bands—I need to work through what this means for the planned experiments.

The narrative guidance flags some concerns: the permutation null sits slightly above random-split baseline but still falls well short of the 31% observed effect, some reviewers are skeptical about novelty given the textbook psychometrics approach, and I need to calibrate claim strength while reinforcing the narrative. Let me now generate detailed predictions for each planned experiment, working through them systematically to produce a comprehensive YAML output.

For the real data DIF on MMLU, I already have registry results showing temporal C% around 31% under median tier assumptions, with the permutation null at 2-8% and residual effects after controls in the 23-29% range, where ability confounds account for 3-6 percentage points of that. For the RL robustness validation with just 13 reasoning models, the sample is underpowered, so under median tier expectations I'd see DIF flags emerge but with limited statistical power to distinguish signal from noise.

The ConStat perturbation testing should show moderate detection on standard models but weaker performance on RL variants, while the DVD generation variance approach detects some bimodal patterns though with constraints. The ensemble fusion approach, which depends on those two, would show only marginal gains. Cross-benchmark validation on GSM8K yields around 18.9% C% with a negative correlation to the GSM1K gap, and the bifactor IRT equating pilot falls short of the target model fit threshold.

Moving forward, item generation calibration shows moderate but suboptimal difficulty correlation, while Bayesian cumulative DIF simulation demonstrates power improvements in simulation contexts. Graceful degradation analysis indicates strong ranking stability even at 50% replacement rates, and item-focused trees perform comparably to categorical DIF approaches. Architecture stratification reveals the cohort is almost entirely decoder-only with minimal practical impact, semi-synthetic contamination validation shows ΔTPR values between 0.35 and 0.5 at p=0.5, and the multi-benchmark temporal DIF analysis is still in progress.

Now I'm compiling the remaining experimental results: permutation null testing shows null C% values in the 2-8% range, odds ratio regression reveals Simpson's paradox with weak R² values, and I need to produce a detailed YAML output calibrated to the median tier with result rationales for each experiment.

Let me work through the full experiment list systematically, ensuring each prediction reflects the median-tier expectations where results are moderately skeptical—permutation nulls sit in that 2-8% band, residual confounding explains 3-6 percentage points rather than the optimistic 2.4pp, and post-control C% lands in the 23-29% range instead of the full 31%. Writing detailed predictions...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27b04091-b035-4bc1-8f56-6549627bfcd2",
  "isSidechain": false,
  "requestId": "req_011CbFjBFtunHtBKVPnFsbHC",
  "type": "assistant",
  "uuid": "73dca997-74f9-4afe-9a77-37f52d1cb2ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyRCfcDeL4ahVwYm8cwjVt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20879,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17904,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17904,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20879
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

_source line 9 · 2026-05-21T12:44:40.788Z_

```yaml
tier: median
narrative_guidance: >
  Median 档下 permutation null C% 落在 2–8%，表明 temporal label 本身携带弱结构性信号
  （model release date 与 ability 不完全正交），但 31% 仍为 null 的 4–15×，统计意义明确。
  Claim 1 headline 须从 '31%' 调整为 '~25–29% after confound controls'，permutation null
  显式报告为 calibration baseline。Claim 2 meta-critique 软化为 'complementary approaches needed'，
  不再用 'fundamentally mismatched'。Claim 3 cross-benchmark 证据降级 appendix，主体仅保留 MMLU。
  Claim 4 diagnostic lens 升格为 abstract 第二句，强调 audit protocol 实用价值以对冲
  'applying textbook psychometrics' 的 novelty 质疑。Rebuttal 准备 'psychometric tools
  are mature but their application to LLM benchmarks at this scale is novel' 防线。
  Simpson's paradox（plan_030 Model 2 vs Model 1）需谨慎处理因果表述，仅作为 supplementary evidence。
  预期 reviewer score 2.5–3.5，borderline accept/weak reject，需要 rebuttal 翻盘。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      对 METABENCH MMLU 响应矩阵 (5219×12508) 执行全面 MH-DIF 分析，
      包含 temporal/ability cohort、within-family confound control、domain specificity。
    expected_results:
      temporal_ets_c_pct: 31.3
      temporal_fpr_li_clean: 0.322
      temporal_enrichment: 0.964
      ability_ets_c_pct: 3.1
      ability_fpr_li_clean: 0.029
      ability_enrichment: 1.15
      within_family_llama2v3_c_pct: 58.7
      within_family_mistral_mixtral_c_pct: 36.2
      domain_spearman_rho: 0.32
      domain_spearman_p: 0.016
      sanity_random_split_c_pct: 0.21
      temporal_ability_jaccard: 0.016
      n_subjects_with_c_gt20pct: 57
      unweighted_subject_mean_c_pct: 30.4
      subject_c_range: "20.1–47.8%"
      decoder_only_pct: 99.98
    result_rationale: >
      Median 档下 temporal C%=31.3% 与已有 registry 一致（这是实测值，不受 tier 影响）。
      关键区别在于后续 controls 将把 residual 压至 25–29%。Within-family Llama-2v3 C% 略低于
      registry 的 61.3%（~58.7%），因为 median 档假设 ability confound 解释更多 variance
      （d=-0.99 对中 ability gap 较大）。Domain ρ=0.32 表明 subject-level accuracy
      improvement 与 DIF 存在弱正相关，但 item-level decomposition 将显示域改善仅解释
      ≤3.5pp。Random-split sanity check 0.21% 确认 temporal signal 非统计噪声。
      Enrichment≈0.96 确认 DIF 与 web-overlap labels 正交——这是预期行为，非方法失败。
    tables:
      - name: "Table 1: Temporal DIF Summary by Cohort Definition"
        columns: [cohort, n_ref, n_foc, n_items, c_pct, fpr_li_clean, enrichment]
        rows:
          - [temporal_2023v2024, 1080, 807, 12508, 31.3, 0.322, 0.964]
          - [ability_quintile, 2610, 2609, 12508, 3.1, 0.029, 1.15]
          - [random_split_sanity, 950, 950, 12508, 0.21, 0.002, 1.01]
      - name: "Table 2: Within-Family Confound Control"
        columns: [family_pair, n_ref, n_foc, c_pct, overlap_with_temporal]
        rows:
          - [Llama-2 vs Llama-3, 161, 308, 58.7, "Jaccard=0.38"]
          - [Mistral vs Mixtral, 89, 112, 36.2, "Jaccard=0.29"]
    figures_description:
      - "Fig 1: 57-subject heatmap showing per-subject C% (rows) × cohort (cols), 色阶 20–48%"
      - "Fig 2: Scatter plot of subject-level accuracy Δ vs C%, ρ=0.32, p=0.016"
    analysis: >
      31.3% temporal instability 是 robust finding。Ability cohort 的 3.1% 确认 DIF
      signal 与 temporal split 强关联而非 ability artifact。Within-family 的高 C%
      （Llama-2v3: 58.7%）混淆了 capability gain 和 contamination——这不是理想的 confound
      control 因为 family 内 ability gap 过大（d≈-0.99）。Domain ρ=0.32 是 ecological
      correlation，item-level decomposition 将在 plan_019/030 中展开。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      验证 DIF 对 RL-trained models 的鲁棒性：alignment-RL (DPO/ORPO) cohort 从
      METABENCH 提取，reasoning-RL (GRPO/PPO) 10–15 个模型需额外推理。
    expected_results:
      n_alignment_rl_models: 477
      n_reasoning_rl_models: 13
      dif_c_pct_baseline_sft_only: 30.8
      dif_c_pct_with_alignment_rl: 31.1
      dif_c_pct_with_reasoning_rl: 30.5
      jaccard_sft_vs_alignment: 0.91
      jaccard_sft_vs_reasoning: 0.84
      constat_auroc_non_rl: 0.72
      constat_auroc_reasoning_rl: 0.58
      mink_auroc_non_rl: 0.68
      mink_auroc_reasoning_rl: 0.51
      delong_dif_vs_constat_p: 0.34
      tost_equivalence_dif_retention: "90% CI [0.88, 0.97], equivalence bound ±0.10"
      tost_conclusion: equivalent
      power_analysis_detection_boundary_p: 0.45
      bootstrap_ci_auroc_dif: [0.76, 0.89]
    result_rationale: >
      Median 档下 DIF 作为 group-level method 对 cohort composition 变化不敏感——添加
      13 个 reasoning-RL 模型到 N=807 focal cohort 几乎不改变 group statistics。
      Jaccard=0.84（vs reasoning-RL）略低于 alignment-RL 的 0.91，因为 reasoning-RL
      模型在部分 hard items 上的 response pattern 与 SFT 模型有系统性差异（GRPO 训练
      改变了 reasoning chain 而非单纯记忆）。传统 per-model detectors 在 reasoning-RL
      上退化显著（ConStat 从 0.72→0.58, Min-K% 从 0.68→0.51），因为 RL 训练平滑了
      NLL distribution。但 N=13 使得所有 pairwise comparison 的 CI 极宽，DeLong test
      无显著差异（p=0.34），TOST equivalence 勉强成立。这是 median 档的典型情况：
      方向正确但统计力不足以支撑强 claim。
    tables:
      - name: "Table: DIF Stability Across Cohort Compositions"
        columns: [cohort_composition, n_focal, c_pct, jaccard_vs_baseline]
        rows:
          - [SFT-only baseline, 620, 30.8, 1.0]
          - [+ alignment-RL (DPO/ORPO), 807, 31.1, 0.91]
          - [+ reasoning-RL (GRPO/PPO), 820, 30.5, 0.84]
      - name: "Table: Per-Model Detector AUROC Comparison"
        columns: [detector, non_rl, alignment_rl, reasoning_rl]
        rows:
          - [DIF (group), "N/A", "N/A", "N/A"]
          - [ConStat, 0.72, 0.67, 0.58]
          - [Min-K%, 0.68, 0.64, 0.51]
    figures_description:
      - "Fig: Detection power curve — DIF ΔTPR vs exploitation rate p ∈ [0.4, 1.0], 标注 detection boundary p≈0.45"
    analysis: >
      DIF 的 group-level 设计使其对 cohort composition 天然鲁棒——13 个 RL 模型在 N=807
      中占比 <2%，统计影响可忽略。真正的 claim 应限定为 "DIF 在 cohort 中 RL 占比 <5%
      时 robust"，而非 "DIF 对 RL 鲁棒"。Per-model detector 退化方向正确但 N=13 使结论
      仅为 suggestive。降级为 limitations 中 disclosure，不作为 numbered contribution。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      独立评估 ConStat-style perturbation testing：LLM 生成 200+ MMLU items 的语义等价
      reformulation，比较原始与改写版本的 model performance。
    expected_results:
      n_items_reformulated: 220
      reformulation_semantic_sim: 0.92
      constat_fdr_controlled_flags: 47
      constat_flag_rate: 0.214
      constat_overlap_with_dif_c: "Jaccard=0.18"
      constat_tpr_non_rl_known_contam: 0.61
      constat_tpr_rl_known_contam: 0.29
      constat_fpr: 0.08
      effect_size_non_rl: 0.74
      effect_size_rl: 0.31
      gpu_hours_used: 65
    result_rationale: >
      Median 档下 ConStat 在 non-RL 模型上表现尚可（TPR=0.61, effect size=0.74），因为
      verbatim memorization 使模型对 surface-form 变化敏感。但 RL-trained 模型（尤其
      GRPO/PPO）通过 reasoning generalization 降低了对 exact wording 的依赖，TPR 降至
      0.29。与 DIF 的低重叠（Jaccard=0.18）符合预期：ConStat 检测 per-model surface-level
      memorization，DIF 检测 group-level differential functioning，二者捕捉不同信号。
      FDR-controlled flag rate 21.4% 低于 DIF 的 31.3%，因为 ConStat 需要更强的
      per-item evidence。GPU 成本 65h 主要用于 reformulation generation 和 inference。
    tables:
      - name: "Table: ConStat Detection Power by Model Type"
        columns: [model_type, n_models, tpr, fpr, effect_size]
        rows:
          - [SFT-only, 15, 0.61, 0.08, 0.74]
          - [Alignment-RL, 10, 0.48, 0.07, 0.55]
          - [Reasoning-RL, 8, 0.29, 0.09, 0.31]
    figures_description:
      - "Fig: ConStat flag rate vs DIF C% per subject — weak positive correlation"
    analysis: >
      ConStat 作为 standalone baseline 有价值但不足以支撑 paper claim。与 DIF 的互补性
      是 ensemble fusion（plan_003c）的理论基础，但 median 档下 RL 模型上的退化使得
      ensemble 增益有限。结果降级为 appendix baseline comparison。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      独立评估 DVD generation variance：10–15 个 open-weight 模型在每个 item 上生成
      50 次 response，计算 generation variance 并检测 bimodal distribution。
    expected_results:
      n_models_tested: 12
      n_items_scored: 12508
      responses_per_item: 50
      dvd_bimodal_flag_rate: 0.089
      dvd_tpr_verbatim_contam: 0.43
      dvd_tpr_variant_contam: 0.52
      dvd_fpr: 0.062
      dvd_overlap_with_dif_c: "Jaccard=0.11"
      gpu_hours_used: 58
      temperature_sensitivity: "T=0.7: flag_rate=0.089; T=1.0: flag_rate=0.142"
    result_rationale: >
      Median 档下 DVD 的 bimodal detection 在 variant contamination 上略优于 verbatim
      （TPR 0.52 vs 0.43），因为 variant contamination 产生更明显的 generation variance
      bimodality（模型在 "近似记忆" 和 "真正推理" 之间切换）。但整体 flag rate 仅 8.9%，
      远低于 DIF 的 31.3%，因为 DVD 需要 per-model inference 且仅在 generation
      distribution 层面操作。与 DIF 的极低重叠（Jaccard=0.11）表明二者检测完全不同维度。
      Temperature 敏感性（T=1.0 时 flag rate 翻倍至 14.2%）暴露了 hyperparameter
      tuning 问题。GPU 成本 58h 用于 12 模型 × 12508 items × 50 responses 的推理。
    tables:
      - name: "Table: DVD Detection by Contamination Type"
        columns: [contam_type, tpr, fpr, bimodal_strength]
        rows:
          - [verbatim, 0.43, 0.062, "Cohen's h=0.38"]
          - [variant, 0.52, 0.058, "Cohen's h=0.47"]
          - [clean, "N/A", 0.062, "Cohen's h=0.04"]
    figures_description:
      - "Fig: Generation variance distribution — bimodal (contaminated) vs unimodal (clean) items"
    analysis: >
      DVD 捕捉的是 per-model generation-level signal，与 DIF 的 group-level item
      functioning signal 几乎不重叠。作为独立检测器价值有限（TPR<0.55），但为 ensemble
      提供了独特的 variant contamination 覆盖。Temperature 敏感性需要在 paper 中 disclose。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      将 DIF + ConStat + DVD 融合为 multi-signal ensemble，评估 majority voting
      和 weighted fusion 策略。
    expected_results:
      ensemble_2of3_tpr: 0.54
      ensemble_2of3_fpr: 0.045
      ensemble_weighted_tpr: 0.59
      ensemble_weighted_fpr: 0.052
      ensemble_coverage_dif_only: "δ≥1.4"
      ensemble_coverage_constat_only: "non-RL δ≥0.6"
      ensemble_coverage_dvd_only: "variant contamination"
      cross_val_weight_stability: "DIF: 0.52±0.08, ConStat: 0.31±0.06, DVD: 0.17±0.05"
      uniform_vs_optimized_tpr_delta: +0.03
      fpr_all_configs_below_010: true
    result_rationale: >
      Median 档下 ensemble 增益有限，因为三个信号的重叠极低（pairwise Jaccard 0.11–0.18），
      majority voting 在 low-overlap 情况下倾向于保守（TPR=0.54）。Weighted fusion
      略优（TPR=0.59）但 cross-validation weight stability 显示 DIF 权重主导（0.52），
      ConStat 和 DVD 的贡献边际化。关键问题：DIF 是 group-level，ConStat/DVD 是
      per-model-level，fusion 的语义不一致使 ensemble 设计缺乏理论基础。Median 档下
      reviewers 会质疑 "为什么要 fuse fundamentally different signal types"。
      结论：ensemble 负面结果，not executed in final paper，降级为 future work。
    tables:
      - name: "Table: Ensemble Fusion Comparison"
        columns: [strategy, tpr, fpr, coverage_description]
        rows:
          - [DIF only, 0.508, 0.314, "group-level, δ≥1.4"]
          - [2-of-3 majority, 0.54, 0.045, "intersection of signals"]
          - [weighted fusion, 0.59, 0.052, "combined coverage"]
          - [uniform weight, 0.56, 0.048, "unweighted average"]
    figures_description:
      - "Fig: Venn diagram of flag overlap — DIF ∩ ConStat ∩ DVD showing minimal 3-way overlap"
    analysis: >
      Ensemble 的 FPR 显著改善（0.045 vs DIF 单独的 0.314），但代价是 TPR 仅从 DIF ΔTPR
      基线略有提升。信号类型不同质（group vs per-model）使 fusion 缺乏 principled
      justification。Median 档下这是 negative result——not executed, dropped to future work。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      在 GSM8K 上复制 DIF 分析，使用 GSM1K 作为 contamination ground truth，
      验证 cross-benchmark 泛化性。
    expected_results:
      gsm8k_n_items: 1319
      gsm8k_n_ref: 1017
      gsm8k_n_foc: 804
      gsm8k_standard_c_pct: 18.9
      gsm8k_external_c_pct: 45.1
      gsm8k_sanity_c_pct: 0.35
      semi_synthetic_delta_tpr_p10: 0.78
      semi_synthetic_delta_tpr_p05: 0.44
      semi_synthetic_external_delta_tpr_p10: 0.49
      gsm1k_n_models: 33
      gsm1k_pearson_r: -0.478
      gsm1k_pearson_p: 0.005
      gsm1k_spearman_rho: -0.39
      gsm1k_spearman_p: 0.025
      gsm1k_partial_r: -0.37
      gsm1k_partial_p: 0.035
      gsm1k_ci_upper_abs_r: 0.155
      direction: "NEGATIVE — opposite to contamination hypothesis"
      cook_d_max_model: "Deepseek-math-7b-rl"
      leave_one_out_r_range: [-0.52, -0.36]
    result_rationale: >
      Median 档下 GSM8K temporal C%=18.9% 低于 MMLU 的 31.3%，因为 GSM8K 是 single-domain
      math benchmark（1319 items），domain homogeneity 降低了 DIF 的 item-level variance。
      Semi-synthetic ΔTPR 在 p=0.5 时为 0.44，落在 median 档范围 [0.35, 0.5] 内。
      GSM1K negative correlation（r=-0.478）是 median 档核心尴尬点：DIF-C items
      anti-correlate with contamination gap，需要额外解释 "DIF ≠ contamination detector,
      DIF detects differential item functioning which may reflect capability gain on
      hard items rather than memorization"。N=33 使 CI 宽且 upper bound |r|=0.155 允许
      near-zero true effect。Spearman ρ=-0.39 弱于 Pearson，暗示 outlier 影响。
      整体降级为 exploratory，不进 abstract/conclusion。
    tables:
      - name: "Table: GSM8K Temporal DIF Summary"
        columns: [metric, standard_mh, external_matching, sanity]
        rows:
          - [C%, 18.9, 45.1, 0.35]
          - [n_items_flagged, 249, 595, 5]
          - [DIF favor 2024, 78, 210, 2]
          - [DIF favor 2023, 171, 385, 3]
      - name: "Table: GSM1K Correlation Analysis"
        columns: [statistic, value, p_value, "95% CI"]
        rows:
          - [Pearson r, -0.478, 0.005, "[-0.71, -0.16]"]
          - [Spearman ρ, -0.39, 0.025, "[-0.66, -0.03]"]
          - [Partial r (ctrl accuracy), -0.37, 0.035, "[-0.64, -0.01]"]
    figures_description:
      - "Fig: Scatter of per-model DIF-C proportion vs GSM8K-GSM1K gap, r=-0.478, 标注 Cook's D outliers"
    analysis: >
      GSM8K 复制确认了 framework portability（ΔTPR 有效），但 GSM1K correlation 的负方向
      是 median 档的关键弱点。必须在 paper 中用一段专门解释：DIF flags items whose
      functioning changed across generations, not items that are contaminated. Hard items
      where 2024 models improve may simultaneously show DIF (functioning changed) AND
      small contamination gap (capability improvement, not memorization)。
      降级为 exploratory per Dream #6 consensus。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      在 METABENCH MMLU 数据上拟合 bifactor IRT 模型（general factor + 57 subject-specific
      factors），选择 anchor items 并执行 fixed-parameter calibration。
    expected_results:
      bifactor_rmsea: 0.038
      bifactor_cfi: 0.87
      bifactor_tli: 0.85
      bifactor_srmr: 0.052
      general_factor_variance_explained: 0.41
      n_anchor_items_selected: 2800
      anchor_stability_criterion: "|Δ_MH|<0.43 (ETS A)"
      equated_rho_vs_original: 0.94
      target_rho_met: false
      convergence_issues: "3 subjects failed to converge; fixed to unidimensional"
      computation_time_hours: 38
    result_rationale: >
      Median 档下 bifactor model 的 fit 低于 acceptable thresholds（CFI<0.90, TLI<0.90），
      因为 MMLU 的 57 subjects 引入了 57 个 specific factors 加 general factor = 58
      latent dimensions，5219 models 的 sample size 对此维度不足。General factor 仅解释
      41% variance（理想 >60%），说明 MMLU 本质上高度多维。3 个小样本 subjects 收敛失败
      需要降级为 unidimensional。Equated ρ=0.94 未达 target ρ≥0.95，主要因为 anchor item
      selection 受 bifactor misfit 影响。Median 档结论：bifactor equating 在 MMLU 上不
      可行，confirmed paper_framing.md 中 "killed by plan_014 pre-check" 的判断。
      作为 negative result 报告在 limitations 中，motivate future multidimensional IRT。
    tables:
      - name: "Table: Bifactor IRT Fit Indices"
        columns: [index, value, acceptable_threshold, verdict]
        rows:
          - [RMSEA, 0.038, "<0.06", PASS]
          - [CFI, 0.87, ">0.90", FAIL]
          - [TLI, 0.85, ">0.90", FAIL]
          - [SRMR, 0.052, "<0.08", PASS]
          - [General factor ω_h, 0.41, ">0.60", FAIL]
    figures_description:
      - "Fig: Scree plot — eigenvalue decay showing 57 factors above noise floor, no dominant general factor"
    analysis: >
      Bifactor IRT equating killed。MMLU 的多维性使得单一 general factor 无法充分
      表征 model ability，anchor item 选择受 model misfit 污染。这是 structural
      limitation 而非 implementation failure。Paper 中作为 "empirical observation that
      motivates future multidimensional IRT" 报告，不作为 contribution。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      为 DIF-flagged MMLU items 生成替换项，使用 LLM generation + student simulation
      进行 difficulty calibration。
    expected_results:
      n_items_generated: 500
      n_dif_items_targeted: 200
      difficulty_correlation_prompt_based: 0.28
      difficulty_correlation_student_sim: 0.71
      difficulty_correlation_empirical: 0.65
      construct_coverage_semantic_sim: 0.88
      holdout_panel_rho: 0.91
      gpu_hours_used: 160
      items_passing_quality_filter: 340
      quality_filter_rate: 0.68
    result_rationale: >
      Median 档下 prompt-based difficulty targeting 的 ρ=0.28 远低于 student simulation
      的 ρ=0.71，符合文献报告（arXiv 2602.06631: ρ=0.10–0.45）。Student simulation
      （arXiv 2601.09953）的 ρ=0.71 低于该文献报告的 r=0.75–0.82，因为 MMLU 的
      domain diversity 使 universal student simulator 难以 calibrate across 57 subjects。
      Empirical calibration（实际跑 holdout model panel）的 ρ=0.65 进一步降低，因为
      simulation-to-reality gap。Holdout panel ρ=0.91 低于 equating target 0.95。
      整体结论：item generation pipeline 可行但 precision 不足以支撑 equated replacement
      claim。降级为 supplementary methodology contribution。
    tables:
      - name: "Table: Difficulty Estimation Method Comparison"
        columns: [method, difficulty_rho, n_items, compute_cost]
        rows:
          - [Prompt-based targeting, 0.28, 500, "8 GPU-h"]
          - [Student simulation, 0.71, 500, "45 GPU-h"]
          - [Empirical (holdout panel), 0.65, 340, "107 GPU-h"]
    figures_description:
      - "Fig: Predicted vs actual difficulty scatter — student sim (ρ=0.71) vs prompt (ρ=0.28)"
    analysis: >
      Item generation pipeline 的核心瓶颈是 difficulty calibration precision。
      ρ=0.65–0.71 不足以保证 equated score equivalence（需要 item-level precision
      而非 correlation）。作为 methodology 贡献有价值但不足以支撑 Claim 3 的
      regeneration narrative。与 plan_005 bifactor failure 共同导致 regeneration
      storyline 被完全 dropped。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      实现 cumulative Bayesian DIF priors (Sinharay et al., 2006)，模拟 4 轮连续
      benchmark administration，展示 evidence accumulation 带来的 power improvement。
    expected_results:
      single_admin_power_d10: 0.38
      cumulative_2_admin_power_d10: 0.52
      cumulative_3_admin_power_d10: 0.64
      cumulative_4_admin_power_d10: 0.71
      single_admin_power_d14: 0.68
      cumulative_3_admin_power_d14: 0.85
      fpr_single: 0.042
      fpr_cumulative_3: 0.048
      simulation_n_per_admin: 200
      simulation_n_items: 500
      simulation_n_reps: 1000
    result_rationale: >
      Median 档下 cumulative Bayesian DIF 的 power improvement 从 0.38→0.71（d=1.0,
      4 administrations），符合 Sinharay et al. 的理论预测但略低于原文（原文 0.40→0.70
      at 3 administrations，我们在 4 administrations 才达到 0.71）。差距因为 LLM
      benchmark 的 non-stationarity——successive administrations 间 DIF pattern 不完全
      stable（model ecosystem evolves），violating Bayesian prior 的 stationarity assumption。
      FPR 从 0.042 到 0.048 的轻微 inflation 是 informative prior 带来的 false alarm
      cost。整体结论：simulation-only result，对 real-world benchmark monitoring
      有 suggestive value 但未在真实数据上验证。降级为 appendix。
    tables:
      - name: "Table: Cumulative Bayesian DIF Power by Administration"
        columns: [n_admins, power_d10, power_d14, fpr]
        rows:
          - [1, 0.38, 0.68, 0.042]
          - [2, 0.52, 0.78, 0.044]
          - [3, 0.64, 0.85, 0.046]
          - [4, 0.71, 0.89, 0.048]
    figures_description:
      - "Fig: Power accumulation curve — d=1.0 and d=1.4, showing diminishing returns after 3 administrations"
    analysis: >
      Simulation-only, underdeveloped for main body。核心 insight（evidence accumulation
      improves detection of medium effects）是 textbook result，novelty 仅在 LLM
      benchmark 场景化。Median 档 reviewers 会 flag "this is just running Sinharay's
      method on simulated data"。降级为 appendix discussion。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      分析 benchmark validity 在 progressive item replacement 下的 degradation：
      5%, 10%, 20%, 50% items replaced，评估 ranking stability, reliability, construct coverage。
    expected_results:
      rho_at_5pct_replacement: 0.999
      rho_at_10pct_replacement: 0.998
      rho_at_20pct_replacement: 0.995
      rho_at_50pct_replacement: 0.983
      reliability_alpha_original: 0.946
      reliability_alpha_at_20pct: 0.938
      reliability_alpha_at_50pct: 0.912
      construct_coverage_original: 57
      construct_coverage_at_50pct: 57
      n_subjects_losing_items_at_50pct: 12
      min_items_per_subject_at_50pct: 31
      theoretical_lower_bound_rho: "ρ ≥ 1 - 2r/(1+r) where r = replacement rate"
    result_rationale: >
      Median 档下 MMLU 的极高 measurement redundancy（12,508 items across 57 subjects）
      使得即使 50% replacement 也仅将 ρ 降至 0.983。这是因为 MMLU 的 per-subject item
      pools 足够大（median 200+ items），random replacement 均匀分布在 subjects 间，
      每个 subject 保留足够 items 维持 reliable estimation。Reliability α 从 0.946 降至
      0.912（50%）仍在 acceptable range。Construct coverage 不受影响因为 replacement
      是 within-subject。关键 caveat：这假设 replacement items 的 psychometric properties
      与 original 相近——plan_006 显示这不成立（ρ=0.65），实际 degradation 会更严重。
    tables:
      - name: "Table: Validity Metrics Under Progressive Replacement"
        columns: [replacement_rate, ranking_rho, cronbach_alpha, min_items_per_subject]
        rows:
          - [0%, 1.0, 0.946, 63]
          - [5%, 0.999, 0.944, 60]
          - [10%, 0.998, 0.941, 57]
          - [20%, 0.995, 0.938, 50]
          - [50%, 0.983, 0.912, 31]
    figures_description:
      - "Fig: Degradation curves — ρ and α as function of replacement rate, with theoretical lower bound"
    analysis: >
      结果实际上强化了 Claim 4 的 redundancy narrative：MMLU 的 ranking stability 对
      item removal/replacement 极其鲁棒。但 median 档下这个结果是 double-edged——
      如果 removing 31% DIF items doesn't matter（ρ=0.997），reviewer 会问 "so what's
      the practical impact of your finding?" 需要 reframe 为 diagnostic value 而非
      quality concern。降级为 supplementary evidence for Claim 4.1 redundancy。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      实现 Item-Focused Trees (Tutz & Berger, 2016) 作为 categorical cohort DIF 的
      替代方案，将 model release date 作为 continuous covariate。
    expected_results:
      n_items_analyzed: 12508
      ift_flagged_items: 4150
      ift_flag_rate: 0.332
      ift_dif_mh_jaccard: 0.72
      ift_dif_mh_concordance: 0.85
      ift_unique_flags: 890
      mh_unique_flags: 658
      ift_split_point_median_date: "2023-09"
      ift_nonlinear_items: 1230
      ift_nonlinear_pct: 0.098
      computation_time_hours: 12
    result_rationale: >
      Median 档下 IFT 的 flag rate（33.2%）略高于 MH（31.3%），因为 continuous covariate
      模型捕捉了 MH 的 binary split 遗漏的 nonlinear trends（9.8% items 显示 non-monotonic
      DIF pattern）。Jaccard=0.72 的 moderate overlap 表明两种方法 largely agree 但 IFT
      的 continuous modeling 额外捕捉了 gradual drift items。IFT split point median 在
      2023-09 附近，接近 MH 使用的 temporal cutoff，增加了 MH cohort definition 的
      合理性。Median 档下 IFT 的价值是 robustness check 而非 primary method——
      "MH results are robust to categorical vs continuous covariate modeling"。
    tables:
      - name: "Table: IFT vs MH-DIF Comparison"
        columns: [metric, MH_DIF, IFT, overlap]
        rows:
          - [flag_rate, "31.3%", "33.2%", "Jaccard=0.72"]
          - [n_flagged, 3918, 4150, "concordance=0.85"]
          - [nonlinear_items, "N/A", 1230, "9.8% of total"]
          - [computation_time, "2h", "12h", "—"]
    figures_description:
      - "Fig: IFT tree visualization for 3 example items — showing split points and DIF magnitude per branch"
    analysis: >
      IFT 确认 MH 结果的 robustness 并提供了 continuous DIF trend 的 additional insight。
      9.8% nonlinear items 是 interesting finding 但不影响 main claims。降级为 appendix
      robustness check——"results hold whether we use categorical (MH) or continuous
      (IFT) covariate modeling"。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      在 architecture-homogeneous subpopulation (decoder-only only) 上运行 DIF，
      测试 IRT model fit 是否改善、spurious DIF 是否减少。
    expected_results:
      n_decoder_only: 5226
      n_non_decoder: 1
      decoder_only_pct: 99.98
      dif_c_pct_decoder_only: 31.3
      dif_c_pct_full: 31.3
      jaccard_decoder_vs_full: 1.0
      irt_rmsea_decoder: 0.042
      irt_rmsea_full: 0.042
      irt_cfi_decoder: 0.78
      irt_cfi_full: 0.78
      pct_models_lz_gt2_decoder: 97.8
      pct_models_lz_gt2_full: 98.0
      conclusion: "architecture heterogeneity is a non-issue"
    result_rationale: >
      Median 档下这是最 clear-cut 的实验：METABENCH MMLU 中 99.98% (5226/5227) 模型是
      decoder-only，排除 1 个 non-decoder 模型完全不改变任何结果（Jaccard=1.0）。
      IRT fit 同样不变，因为 misfit (|Lz|>2 for 98%) 源于 MMLU 的 inherent
      multidimensionality（57 subjects → 多维 ability），而非 architecture heterogeneity。
      这是 proactive defense 实验：reviewer 无法质疑 "architecture confound inflates DIF"
      因为 population 几乎完全 homogeneous。Zero GPU cost, 纯 data subsetting。
    tables:
      - name: "Table: Architecture Stratification Results"
        columns: [population, n_models, c_pct, irt_rmsea, pct_lz_gt2]
        rows:
          - [Full, 5227, 31.3, 0.042, 98.0]
          - [Decoder-only, 5226, 31.3, 0.042, 97.8]
          - [Delta, -1, 0.0, 0.000, -0.2]
    figures_description:
      - "Fig: Architecture composition pie chart — 99.98% decoder-only (appendix only)"
    analysis: >
      Architecture stratification 是 one-line result: "METABENCH MMLU is 99.98%
      decoder-only; excluding the single non-decoder model changes nothing (Jaccard=1.0)."
      Main body 一句话 + footnote，不需要 dedicated section。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: >
      向 METABENCH response matrix 注入已知 contamination，测量 DIF 在 controlled
      ground truth 下的 detection power，解决 ground truth circularity concern。
    expected_results:
      n_clean_items_selected: 500
      n_injection_items: 150
      temporal_external_tpr_p0: 0.33
      temporal_external_tpr_p03: 0.52
      temporal_external_tpr_p05: 0.74
      temporal_external_tpr_p07: 0.93
      temporal_external_tpr_p10: 1.0
      temporal_external_fpr: 0.318
      temporal_external_delta_tpr_p05: 0.41
      temporal_external_delta_tpr_p10: 0.67
      ability_external_tpr_p10: 0.77
      ability_external_fpr: 0.49
      standard_mh_fpr_inflation_at_p10: "0.30→0.59"
      matching_variable_contamination: true
      dose_response_monotonic: true
    result_rationale: >
      Median 档下 ΔTPR(p=0.5)=0.41 落在 key indicator range [0.35, 0.50] 内。
      这比 registry 实际值 (ΔTPR(p=0.5)=0.508) 低约 0.1，因为 median 档假设
      temporal label 携带的弱结构性（permutation null 2–8%）吃掉了一部分 detection
      headroom。FPR=0.318 反映 temporal cohort 的 baseline instability（即使 clean items
      中有 ~31.8% 被 flag，因为 "clean" is defined by Li et al. labels which don't
      capture differential effects）。Dose-response 从 p=0.3 到 p=1.0 单调增长确认了
      injection validity。Standard MH 的 FPR inflation（0.30→0.59 at p=1.0）确认了
      matching variable contamination——within-group matching variable 被 injection
      污染导致 FPR 膨胀，这是 cross-subject matching 的动机。
    tables:
      - name: "Table: Semi-Synthetic Detection Power (Temporal, External Matching)"
        columns: [exploitation_rate_p, tpr, fpr, delta_tpr]
        rows:
          - [0.0 (baseline), 0.33, 0.318, 0.0]
          - [0.3, 0.52, 0.320, 0.19]
          - [0.5, 0.74, 0.318, 0.41]
          - [0.7, 0.93, 0.317, 0.61]
          - [1.0, 1.0, 0.316, 0.67]
      - name: "Table: Matching Variable Contamination Effect"
        columns: [matching_method, fpr_p0, fpr_p10, delta_fpr]
        rows:
          - [Standard (within-group), 0.298, 0.59, +0.292]
          - [External (cross-benchmark), 0.318, 0.316, -0.002]
    figures_description:
      - "Fig: Dose-response curve — TPR vs exploitation rate p, with 95% CI bands"
      - "Fig: FPR comparison — standard vs external matching as injection increases"
    analysis: >
      ΔTPR(p=0.5)=0.41 是 median 档的核心指标，表明 DIF 在 moderate exploitation rate
      下有 meaningful detection power but not overwhelming。Reviewer 会追问 "p=0.5
      是否 realistic?"——需要在 paper 中 argue contamination exploitation rates 在文献
      中缺乏 empirical estimates，p=0.5 是 conservative middle ground。External matching
      的 ΔFPR≈0 是 methodological highlight，直接支撑 cross-subject matching recommendation。

  - name: multi_benchmark_temporal_dif
    plan_id: plan_028
    description: >
      在 METABENCH 中的 ARC, HellaSwag, WinoGrande, TruthfulQA 上运行 temporal DIF，
      验证 cross-benchmark 泛化性。
    expected_results:
      mmlu_c_pct: 31.3
      mmlu_random_c_pct: 0.18
      winogrande_c_pct: 28.8
      winogrande_random_c_pct: 0.35
      truthfulqa_c_pct: 27.4
      truthfulqa_random_c_pct: 0.40
      arc_c_pct: 24.5
      arc_random_c_pct: 0.55
      gsm8k_c_pct: 18.9
      gsm8k_random_c_pct: 0.30
      hellaswag_c_pct: 17.2
      hellaswag_random_c_pct: 0.30
      cross_benchmark_range: "17.2–31.3%"
      all_random_below_1pct: true
      min_enrichment_ratio: 31
      n_benchmarks: 6
    result_rationale: >
      Median 档下 cross-benchmark C% range 为 17.2–31.3%，落在 key indicator range
      [15.0, 32.0] 内。排序 MMLU > WinoGrande > TruthfulQA > ARC > GSM8K > HellaSwag
      反映了各 benchmark 的 structural properties：MMLU（57 subjects, 12K items）和
      WinoGrande（commonsense reasoning, 高 memorization vulnerability）C% 最高；
      HellaSwag（sentence completion, 10K items 但 item homogeneity 高）和 GSM8K
      （math, single domain）C% 最低。所有 random-split controls <1% 确认 temporal
      signal 在每个 benchmark 上都是 genuine。Median 档下 HellaSwag 和 GSM8K 的较低
      C% 会被 reviewer 追问——需要解释 domain homogeneity 降低 DIF variance。
    tables:
      - name: "Table: Cross-Benchmark Temporal DIF Summary"
        columns: [benchmark, n_items, n_ref, n_foc, c_pct, random_c_pct, enrichment_ratio]
        rows:
          - [MMLU, 12508, 1080, 807, 31.3, 0.18, 174]
          - [WinoGrande, 1267, 1017, 803, 28.8, 0.35, 82]
          - [TruthfulQA, 817, 1080, 807, 27.4, 0.40, 69]
          - [ARC-Challenge, 1172, 1080, 807, 24.5, 0.55, 45]
          - [GSM8K, 1319, 1017, 804, 18.9, 0.30, 63]
          - [HellaSwag, 10042, 1080, 807, 17.2, 0.30, 57]
    figures_description:
      - "Fig: Bar chart — C% across 6 benchmarks with random-split control overlay"
    analysis: >
      6 个 benchmark 的一致 temporal DIF pattern (17–31%, all >>random) 是 median 档下
      最强的 generalizability evidence。但 Claim 3 的 cross-benchmark 证据被降级至
      appendix（8 页限制），main body 仅保留 MMLU 结果 + 一句 "consistent across 5
      additional benchmarks (see Appendix X)"。

  - name: permutation_null_c_rate
    plan_id: plan_029
    description: >
      1000× permutation test：随机重新分配 2023/2024 temporal labels（保持 N_ref=1080,
      N_foc=807），每次运行 MH-DIF，建立 C% 的 null distribution。
    expected_results:
      n_permutations: 1000
      null_c_pct_mean: 4.8
      null_c_pct_median: 4.6
      null_c_pct_sd: 1.2
      null_c_pct_95ci: [2.7, 7.3]
      null_c_pct_99ci: [1.9, 8.4]
      null_c_pct_max: 9.1
      observed_c_pct: 31.3
      z_score_vs_null: 22.1
      p_value: "<1e-50"
      ratio_observed_to_null_mean: 6.5
      random_split_c_pct: 0.18
      null_vs_random_split_ratio: 26.7
    result_rationale: >
      Median 档下 permutation null C% mean=4.8% 落在 key indicator range [2.0, 8.0]。
      Permutation null 显著高于 random-split control（4.8% vs 0.18%），因为 temporal
      labels 与 ability 不完全正交：2024 模型平均 stronger（d=-0.17），permutation
      打断了 true temporal signal 但保留了 ability distribution 的 marginal structure。
      Random-split 在 within-cohort 内操作所以 ability 完全 balanced，产生 near-zero
      C%。Permutation null 的 4.8% 表明 ~5% 的 "DIF" 可归因于 temporal label 本身
      携带的 ability confound structure，但 31.3% 仍为 null 的 6.5× (z=22.1)。
      Median 档下 reviewer 会追问 "4.8% null 是否意味着 temporal cohort design 有
      systematic bias?"——需要在 paper 中解释这是 expected property of any non-randomized
      group comparison in observational studies，并引用 plan_027 的 matched-ability
      analysis (C%=28.9%) 作为 complementary evidence。
    tables:
      - name: "Table: Permutation Null Distribution"
        columns: [statistic, value]
        rows:
          - [Null mean C%, 4.8]
          - [Null median C%, 4.6]
          - [Null SD, 1.2]
          - ["Null 95% CI", "[2.7, 7.3]"]
          - [Null max, 9.1]
          - [Observed C%, 31.3]
          - [z-score, 22.1]
          - ["Observed / Null mean", "6.5×"]
      - name: "Table: Three Baselines Comparison"
        columns: [baseline, c_pct, interpretation]
        rows:
          - [Random split (within-cohort), 0.18, "statistical noise floor"]
          - [Permutation null (label shuffle), 4.8, "temporal label structure"]
          - [Observed temporal DIF, 31.3, "genuine + structural"]
          - [Matched-ability (plan_027), 28.9, "genuine after ability control"]
    figures_description:
      - "Fig: Histogram of 1000 permutation null C% values with observed 31.3% marked as vertical line"
      - "Fig: Three-baseline comparison bar chart — random (0.18%), permutation (4.8%), observed (31.3%)"
    analysis: >
      Permutation null 是 median 档下 Claim 1 的关键 calibration baseline。31.3% vs
      4.8% null 给出 "genuine DIF ≈ 26.5%" 的 conservative estimate，与 plan_027 的
      matched-ability C%=28.9% convergent。Paper 应报告为 "~25–29% depending on
      confound controls"（取 plan_027 matched 28.9% 与 observed-null=26.5% 的 range）。
      Permutation null 显式报告为 calibration baseline 是对 reviewer "is 31% above
      chance?" 的 definitive answer。

  - name: odds_ratio_regression_transparency
    plan_id: plan_030
    description: >
      补充 pseudo R²=0.0007 的 odds ratio + 95% CI + McFadden/Nagelkerke R² + deviance
      ratio，并构建更精细的 item-level model。
    expected_results:
      model1_domain_delta:
        mcfadden_r2: 0.0007
        nagelkerke_r2: 0.0013
        subject_acc_delta_or_per_010: 1.58
        subject_acc_delta_ci_per_010: [1.21, 2.06]
        deviance_ratio: 0.0007
      model2_domain_delta_plus_items:
        mcfadden_r2: 0.044
        nagelkerke_r2: 0.074
        subject_acc_delta_or_per_010: 0.71
        ctt_difficulty_or_per_010: 0.76
        ctt_discrimination_or_per_010: 1.54
      model3_item_delta:
        mcfadden_r2: 0.0013
        nagelkerke_r2: 0.0022
        item_acc_change_or_per_010: 1.09
        item_acc_change_ci: [1.53, 2.99]
      model4_item_delta_plus_items:
        mcfadden_r2: 0.045
        nagelkerke_r2: 0.076
        item_acc_change_or_per_010: 0.91
        ctt_difficulty_or_per_010: 0.75
        ctt_discrimination_or_per_010: 1.56
      simpsons_paradox: true
      lr_test_m1_vs_m2_chi2: 640.5
      lr_test_m3_vs_m4_chi2: 648.2
      best_model_mcfadden: 0.045
      ability_confound_explained_pp: 4.2
    result_rationale: >
      Median 档下 Simpson's paradox (Model 2 vs Model 1) 是核心 methodological finding：
      domain accuracy Δ 的 OR 从 1.58 (Model 1, positive) 翻转为 0.71 (Model 2,
      negative) after controlling for item properties。这是因为 high-discrimination
      items (OR=1.54) 同时是 DIF-prone items AND high-accuracy-change items，产生
      confound。McFadden R² 即使在 best model (0.045) 下也极低，说明 DIF 的 item-level
      variance 绝大部分无法由 observed item properties 解释。Median 档下 ability
      confound explained pp=4.2，落在 [3.0, 6.0] 范围内——高于 plan_027 的 2.4pp 因为
      regression 捕捉了额外的 item-level confounding pathway。
      Reviewer 会追问 Simpson's paradox 的因果解释——需谨慎表述为 "item difficulty may
      be a mediator rather than confounder; Model 1 (marginal) and Model 2 (conditional)
      answer different causal questions"。
    tables:
      - name: "Table: Logistic Regression Model Comparison"
        columns: [model, predictors, mcfadden_r2, nagelkerke_r2, aic]
        rows:
          - [Model 1, "subject acc Δ", 0.0007, 0.0013, 15548]
          - [Model 2, "subject acc Δ + CTT props", 0.044, 0.074, 14910]
          - [Model 3, "item acc Δ", 0.0013, 0.0022, 15539]
          - [Model 4, "item acc Δ + CTT props", 0.045, 0.076, 14892]
      - name: "Table: Simpson's Paradox in Accuracy Δ Effect"
        columns: [model, acc_delta_or, direction, interpretation]
        rows:
          - [Model 1 (marginal), 1.58, positive, "higher acc Δ → more DIF"]
          - [Model 2 (conditional), 0.71, negative, "higher acc Δ → LESS DIF after controlling item props"]
    figures_description:
      - "Fig: Simpson's paradox visualization — marginal vs conditional effect of accuracy Δ on DIF probability"
    analysis: >
      Simpson's paradox 需要在 paper 中小心处理。Model 1 的 marginal positive effect
      支持 "capability gain causes DIF" 的 naive interpretation，但 Model 2 的 conditional
      negative effect 表明 item properties (especially discrimination) 是 confound。
      Median 档下建议 Model 1 as primary (conservative, 不做因果 claim)，Model 2 as
      supplementary (illustrating confound structure)。总 explained variance <5%
      (McFadden R²=0.045) 意味着 95%+ 的 DIF variance 是 item-specific 且无法归因于
      observed covariates——这实际上强化了 "DIF captures genuine item-level differential
      functioning, not a proxy for aggregate trends" 的 narrative。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73dca997-74f9-4afe-9a77-37f52d1cb2ac",
  "isSidechain": false,
  "requestId": "req_011CbFjBFtunHtBKVPnFsbHC",
  "type": "assistant",
  "uuid": "e100166c-4bc7-4b4e-8720-5a9a783524bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyRCfcDeL4ahVwYm8cwjVt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20879,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17904,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17904,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20879
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Permutation null 略高于 random-split 但 31% 仍远超，部分 reviewer 质疑 novelty（'applying textbook psychometrics'），需要调整 claims 强度并补强 narrative 核心假设：['plan_029 permuta…",
  "leafUuid": "e100166c-4bc7-4b4e-8720-5a9a783524bf",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier DIF analysis: characterizing MMLU temporal instability",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Permutation null 略高于 random-split 但 31% 仍远超，部分 reviewer 质疑 novelty（'applying textbook psychometrics'），需要调整 claims 强度并补强 narrative 核心假设：['plan_029 permuta…",
  "leafUuid": "e100166c-4bc7-4b4e-8720-5a9a783524bf",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier DIF analysis: characterizing MMLU temporal instability",
  "sessionId": "c2400123-8593-4207-9144-53d78fc6917c"
}
```

---
