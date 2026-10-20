# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：6-benchmark cross-validation + Simpson's paradox 完全封堵了主要攻击面；reviewer 接受 IRT 

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/3893de7d-e708-46c7-b68b-82b376487d7e.jsonl`
- **Structured JSON:** [`f288ffe88c972383f9d8.json`](../../sessions/f2/f288ffe88c972383f9d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T11:07:24.179Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T11:07:24.179Z",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：6-benchmark cross-validation + Simpson's paradox 完全封堵了主要攻击面；reviewer 接受 IRT misfit 作为 conservative estimate 的 framing；temporal binary split 被视为合理的 first-pass design；audit protocol 满足 actionability 要求。Paper 以 strong empirical contribution 被接收。\n核心假设：[\"6-benchmark C% 一致性 (17.9-31.3%, 全部 ≥45× random) 被 reviewer 视为充分的 generalizability 证据，'only MMLU' 攻击面关闭\", \"Simpson's paradox (OR 1.55→0.73) + plan_019 decomposition (≤2.4pp/7.6%) 双重证据说服 reviewer domain improvement 不是 DIF 的驱动因素\", \"IRT misfit (98% |Lz|>2) 被成功 framing 为 'MMLU 固有多维性导致，MH 不依赖 IRT fit'——reviewer 接受 MH 作为非参数方法的独立性\", '2023 vs 2024 binary split 被接受为 temporal cohort design 的合理粒度，reviewer 不要求 quarterly/monthly 分析', 'DIF audit protocol 被视为 sufficient actionable contribution，无需 end-to-end benchmark regeneration 演示']\n关键指标范围：{'reviewer_avg_score': [3.8, 4.3], 'cross_bench_c_pct_min': [17.0, 20.0], 'cross_bench_c_pct_max': [29.0, 33.0], 'ability_confound_explained_pp': [1.5, 3.0], 'simpsons_or_flip_magnitude': [0.6, 0.9], 'semi_synthetic_delta_tpr_p05': [0.45, 0.6], 'ranking_rho_after_removal': [0.995, 0.999], 'reviewer_count_champion': [1, 2]}\n叙事方向：原始 framing 完全成立：'Psychometric DIF reveals widespread temporal instability across 6 major LLM benchmarks (17.9-31.3%), not explained by capability improvement (Simpson's paradox reversal), with a reusable semi-synthetic validation framework.' 四条 claims 无需调整强度。8 页压缩可行——plan_028 结果用一张 summary table，plan_030 用一段 + 一个 figure panel。Ground truth meta-critique 因有 6 benchmark 交叉佐证而更具说服力。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\nfocus: plan_028 新增 6-benchmark cross-validation (C%=17.9-31.3%, 45-174× above random) + plan_030 Simpson's paradox (OR 1.55→0.73)。评估这些新数据是否将 Best 从 3.5 推到 4.0+ (Conference acceptance)。重点关注：IRT misfit defense 是否充分、temporal coarseness (2023 vs 2024 binary) 是否仍是主要攻击面、actionability gap 是否被 audit protocol 覆盖。\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T11:07:24.183Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T11:07:24.183Z",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T11:07:24.204Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：6-benchmark cross-validation + Simpson's paradox 完全封堵了主要攻击面；reviewer 接受 IRT misfit 作为 conservative estimate 的 framing；temporal binary split 被视为合理的 first-pass design；audit protocol 满足 actionability 要求。Paper 以 strong empirical contribution 被接收。
核心假设：["6-benchmark C% 一致性 (17.9-31.3%, 全部 ≥45× random) 被 reviewer 视为充分的 generalizability 证据，'only MMLU' 攻击面关闭", "Simpson's paradox (OR 1.55→0.73) + plan_019 decomposition (≤2.4pp/7.6%) 双重证据说服 reviewer domain improvement 不是 DIF 的驱动因素", "IRT misfit (98% |Lz|>2) 被成功 framing 为 'MMLU 固有多维性导致，MH 不依赖 IRT fit'——reviewer 接受 MH 作为非参数方法的独立性", '2023 vs 2024 binary split 被接受为 temporal cohort design 的合理粒度，reviewer 不要求 quarterly/monthly 分析', 'DIF audit protocol 被视为 sufficient actionable contribution，无需 end-to-end benchmark regeneration 演示']
关键指标范围：{'reviewer_avg_score': [3.8, 4.3], 'cross_bench_c_pct_min': [17.0, 20.0], 'cross_bench_c_pct_max': [29.0, 33.0], 'ability_confound_explained_pp': [1.5, 3.0], 'simpsons_or_flip_magnitude': [0.6, 0.9], 'semi_synthetic_delta_tpr_p05': [0.45, 0.6], 'ranking_rho_after_removal': [0.995, 0.999], 'reviewer_count_champion': [1, 2]}
叙事方向：原始 framing 完全成立：'Psychometric DIF reveals widespread temporal instability across 6 major LLM benchmarks (17.9-31.3%), not explained by capability improvement (Simpson's paradox reversal), with a reusable semi-synthetic validation framework.' 四条 claims 无需调整强度。8 页压缩可行——plan_028 结果用一张 summary table，plan_030 用一段 + 一个 figure panel。Ground truth meta-critique 因有 6 benchmark 交叉佐证而更具说服力。

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
  "promptId": "f77fa86e-c417-42a0-a19a-0f7e2f828703",
  "type": "user",
  "uuid": "76c2011c-e7e2-4305-892e-2b938f1ffc22",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T11:07:24.203Z_

```json
{
  "parentUuid": "76c2011c-e7e2-4305-892e-2b938f1ffc22",
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
  "uuid": "410f89b9-60fd-45dd-8d61-5e09e5a3c5a0",
  "timestamp": "2026-05-21T11:07:24.203Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T11:07:24.203Z_

```json
{
  "parentUuid": "410f89b9-60fd-45dd-8d61-5e09e5a3c5a0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "208ff0aa-e424-431a-a189-7861ba179c26",
  "timestamp": "2026-05-21T11:07:24.203Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：6-benchmark cross-validation + Simpson's paradox 完全封堵了主要攻击面；reviewer 接受 IRT misfit 作为 conservative estimate 的 framing；temporal binary split 被视为合理的 first-pa…",
  "leafUuid": "208ff0aa-e424-431a-a189-7861ba179c26",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric DIF reveals temporal benchmark instability across 6 benchmarks",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e"
}
```

---

### Assistant

_source line 8 · 2026-05-21T11:08:27.467Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, under the "best" tier scenario. I need to provide result_rationale for each prediction explaining why these results would occur in this tier.

Let me go through each planned experiment and generate predictions based on the best tier definition and the existing registry data.

Let me carefully review what's planned vs what's already done:

**Already completed (in registry):**
- mvp_dif_power_sim
- mvp_dif_power_sim_phase2
- plan_001_real_data_dif_mmlu


- plan_001b_matched_ability_dif
- plan_011_semi_synthetic_validation
- plan_012_irt_theta_conditioning
- plan_013_q3_local_independence
- plan_014_within_subject_dif
- plan_015_bifactor_irt (killed)
- plan_016_within_subject_semi_synthetic
- plan_017_downstream_impact
- plan_004_gsm8k_cross_benchmark
- plan_027_temporal_overlap
- plan_030_odds_ratio
- plan_028_multi_bench_dif

**Still planned (status: planned):**
- plan_001 (real_data_dif_mmlu) - status

I'm noticing several plans marked as planned that actually show completion in the registry, like plan_004 and plan_010, while others like plan_002 through plan_010 are still queued up. The list appears to be cut off at plan_011 but I can see there's a backlog of validation and analysis work spanning robustness checks, perturbation studies, IRT modeling, and architecture-specific DIF analyses. I see the discrepancy now - the experiment_plan marks everything as "planned" but the registry shows many are already completed. The user wants me to generate detailed predicted results for each experiment in the plan, with rationales for every prediction. For experiments already done, I should use the actual registry data as the foundation while framing them under the "best" tier scenario. For the ones not yet completed, I need to predict what the results would look like if everything goes optimally. For the completed experiments, I'll use the registry results as ground truth since they align with the best-case narrative. For the pending ones, I'll project outcomes assuming optimal conditions. Plan_002 on RL robustness gets relegated to the appendix or dropped entirely—the paper's framing treats N=13 as underpowered, so best tier either shows modest gains or acknowledges the limitation. Plans_003a through 003c around ConStat, DVD, and ensemble methods are marked as future work and aren't needed for best tier. Plan_005's bifactor IRT approach was killed in the registry, so it's not required. Plan_006 on item generation depends on plan_005, which is already defunct.

Moving through the rest: plan_007's cumulative Bayesian DIF stays simulation-only in the appendix, plan_008's graceful degradation is supplementary, and plan_009's item-focused trees serve as a robustness check. Plan_010 on architecture stratification is partially resolved—the paper mentions that 99.98% of results come from decoder-only models. Plan_029 on permutation nulls hasn't been executed yet but matters for confirming the 31% result sits far above chance.

Now I'm extracting the embedded results from the paper framing itself, since many experiments have their findings already documented there rather than in separate registry entries. Now I'm seeing which experiments actually have registry data versus those that are just referenced in the framing. I need to focus on what's in the experiment_plan and be systematic about filling in the YAML—using actual metrics for completed experiments to support the narrative, and predicting consistent results for planned ones.

Writing YAML structure... card >0.85 with SFT baseline). Reasoning-RL models (10-15) mixed into focal cohort don't change C% by more than 1-2pp. Traditional detectors (Min-K%, ConStat) degrade on reasoning-RL models (AUROC drops 0.15-0.25). But N=13 makes this underpowered → reported in limitations, not main claims.

**plan_003a** (planned, P0, 80 GPU hours): ConStat eval. In best tier framing, this was never executed and moved to future work. If imagined: ConStat detects ~15-20% of items as suspicious, partial overlap with DIF flags (Jaccard ~0.15-0.25).

**plan_003b** (planned, P0, 70 GPU hours): DVD eval. Same - never executed in best tier. If imagined: DVD shows bimodal variance for ~10-15% of items, weak overlap with DIF (Jaccard ~0.10-0.20). **plan_003c** (planned, P0, 0 GPU hours): Ensemble fusion would show complementary coverage if the components had worked. **plan_004** (DONE): GSM8K cross-benchmark validated with C%=18.9%, ΔTPR=+0.818, and GSM1K correlation r=-0.478. **plan_005** (killed): Bifactor IRT pre-check showed it's not viable. **plan_006** (planned, P1, 200 GPU hours): Item generation depends on plan_005 which was killed, so this is also dropped. **plan_007** (planned, P2, 0 GPU hours): Cumulative Bayesian DIF simulation shows power...

Cumulative Bayesian DIF shows power improvement from ~0.40 individual to ~0.65-0.70 after three administrations, moved to appendix. Plan_008 (graceful degradation) depends on killed plans but the simplified version using random replacement simulation shows robustness above ρ>0.99 up to 20% replacement and ρ>0.97 at 50%. Plan_009 (item-focused trees) confirms the DIF pattern with continuous temporal treatment and acceleration post-mid-2023, going to supplementary materials. Plan_010 (architecture-stratified DIF) finds the decoder-only result so dominant (99.98%) that it becomes trivial.

Plan_011 validated the semi-synthetic approach with strong TPR improvement and stable cross-subject FPR. Plan_028 across six benchmarks shows C% ranging 17.9-31.3%, all substantially above random baseline. Plan_029's permutation null test with 1000 iterations yields a mean C% around 0.2% (±0.15%), making the observed 31.3% over 200 standard deviations above null with p<0.001 across all permutations. Plan_030 confirms Simpson's paradox through odds ratio regression.

Now I'm generating the YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "208ff0aa-e424-431a-a189-7861ba179c26",
  "isSidechain": false,
  "requestId": "req_011CbFcCBVhdi1VcqWGiVG6R",
  "type": "assistant",
  "uuid": "b3bd36fc-a918-43a3-bc22-f5d6be9ea128",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7b6EvR81VARY6yuMLp4db",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20945,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14116,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20945
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

_source line 9 · 2026-05-21T11:12:32.928Z_

```yaml
tier: best
narrative_guidance: >
  Best 档叙事完全成立：6-benchmark cross-validation (17.9-31.3%, 45-174× random) 封堵 "only MMLU" 攻击面；
  Simpson's paradox (OR 1.55→0.73) 封堵 ability confound 攻击面；IRT misfit 被 framing 为 MMLU 固有多维性
  (98% |Lz|>2)，reviewer 接受 MH 作为非参数方法不依赖 IRT fit；temporal binary split 被 permutation null
  (>200σ) + 6-benchmark 一致性双重支撑；audit protocol 满足 actionability。四条 claims 强度无需调整。
  Dropped experiments (003a/b/c, 005, 006) 正确归入 future work，不伤主线。Reviewer avg score 3.8-4.3，
  1-2 位 champion reviewer 给 4.5+，paper 以 strong empirical contribution 被接收。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: "METABENCH MMLU 5219×12508 response matrix 上的 MH-DIF 全量分析：temporal cohort (2023 vs 2024-H1)、ability-quintile、within-family、domain-specificity"
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
      n_subjects_with_dif: 57/57
      subject_c_pct_range: "20.7-48.4%"
      unweighted_subject_mean_c_pct: 30.0
    result_rationale: >
      Best 档下 31.3% C% 是核心锚点数字。Random split 0.18% 提供 174× enrichment baseline，
      直接证明非统计噪声。Enrichment≈1.0 against Li et al. 是 expected 而非 failure——web-overlap
      labels 测量 global exposure，DIF 测量 differential functioning，两者正交。
      Within-family Llama-2v3 C%=61.3% 看似高但包含真实 capability jump (d=-0.99)，
      plan_027 matched analysis 后降至 28.3%，证明 ability confound 解释 33pp。
      Domain ρ=0.307 (p=0.02) 是 modest ecological correlation，plan_019 item-level
      decomposition 将其降至 ≤2.4pp/7.6%——足以说服 reviewer instability 是 item-specific。
      57/57 subjects 全部有 DIF 排除了 domain-specific artifact。
    tables:
      - "Table 1: Temporal DIF summary — C%=31.3%, random=0.18%, enrichment=0.96, 57/57 subjects affected"
      - "Table S1 (appendix): Per-subject C% breakdown (57 rows)"
    figures_description:
      - "Figure 1a: DIF effect size (Δ_MH) distribution histogram with ETS A/B/C thresholds marked"
      - "Figure 1b: Subject-level C% heatmap sorted by domain cluster"
    analysis: >
      Load-bearing result for Claim 1。31.3% 在 best 档下被 6-benchmark replication 交叉验证
      (17.9-31.3% range)，reviewer 无法 dismiss 为 MMLU-specific artifact。Random split
      0.18% 是最简洁的 "not chance" 论证，优于复杂的 permutation test。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: "验证 DIF 对 alignment-RL 和 reasoning-RL 模型的鲁棒性：SFT baseline vs DPO/ORPO cohort vs 10-15 GRPO/PPO models"
    expected_results:
      sft_baseline_c_pct: 31.8
      alignment_rl_cohort_c_pct: 30.5
      alignment_rl_jaccard_vs_sft: 0.87
      reasoning_rl_n_models: 13
      focal_with_rl_c_pct: 31.1
      focal_with_rl_jaccard_vs_baseline: 0.92
      constat_auroc_sft: 0.72
      constat_auroc_alignment_rl: 0.68
      constat_auroc_reasoning_rl: 0.49
      mink_auroc_sft: 0.75
      mink_auroc_alignment_rl: 0.71
      mink_auroc_reasoning_rl: 0.44
      dif_retention_ratio_vs_sft: 0.96
      tost_equivalence_p: 0.03
      bootstrap_ci_auroc_dif: [0.88, 0.95]
      delong_dif_vs_constat_p: 0.002
      power_curve_delta_threshold: 1.4
      power_at_p04: 0.35
      power_at_p07: 0.72
      power_at_p10: 0.80
    result_rationale: >
      Best 档下 RL robustness 呈现 positive signal 但因 N=13 reasoning-RL models
      统计功效不足。DIF 是 group-level method，13 个 RL 模型混入 N=807 focal cohort
      仅占 1.6%，C% 几乎不变 (31.3→31.1%) 是预期结果——不是因为 DIF 对 RL robust，
      而是因为 RL models 数量太少无法影响 group statistics。Alignment-RL (DPO/ORPO)
      不涉及 PPO clipping/NLL gap contraction，Jaccard=0.87 高一致性是理论预期。
      传统 detectors 在 reasoning-RL 上 AUROC 跌至 ~0.45-0.49 提供了 contrast evidence。
      但 N=13 使得 bootstrap CI 宽、DeLong test underpowered。Best 档将此定位为
      limitations 中的 honest disclosure + future work motivation，不作为 numbered
      contribution。Reviewer 视之为 "authors are aware of the limitation" 而非弱点。
    tables:
      - "Table S-RL (appendix): DIF stability across cohort compositions (SFT/alignment-RL/+reasoning-RL)"
    figures_description:
      - "Figure S-RL: AUROC comparison bar chart — DIF vs ConStat vs Min-K% across 3 cohort types"
    analysis: >
      Appendix material。N=13 reasoning-RL 是 honest limitation。Best 档 reviewer
      接受 "DIF is group-level, RL robustness requires future dedicated study with
      larger reasoning-RL sample" 的 framing。不占主文页面。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: "ConStat-style perturbation测试：200+ MMLU items 的语义等价改写 + FDR-controlled detection"
    expected_results:
      status: not_executed
      reason: "Dropped from scope — ensemble approach (plan_003c) killed after paper pivot to characterization framing"
      hypothetical_detection_rate: 0.18
      hypothetical_overlap_with_dif_jaccard: 0.19
      hypothetical_fdr_controlled_items: 145
    result_rationale: >
      Best 档下 ConStat eval 未执行且无需执行。Paper 从 "detect contamination" pivot 到
      "characterize benchmark properties"，ensemble detection 不再是 contribution。
      ConStat 测量 perturbation sensitivity（item 换种问法模型还能否答对），这与 DIF 测量的
      temporal differential functioning 是正交信号。即使执行，Jaccard ~0.19 的低重叠
      既不 support 也不 undermine 核心 claims。Reviewer 不会要求执行一个与 paper
      narrative 不相关的 baseline。Best 档将 ConStat/DVD 列入 Related Work 讨论
      (§2 中已有 45 papers/5 clusters)，定位为 "complementary but orthogonal approach"。
    tables: []
    figures_description: []
    analysis: >
      正确 drop。Best 档 reviewer 不会因缺少 ConStat baseline 扣分——paper 不是
      methods comparison，是 empirical characterization。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: "DVD generation variance 检测：10-15 open-weight models × 50 responses/item，温度采样 T=0.7-1.0"
    expected_results:
      status: not_executed
      reason: "Dropped with ensemble — GPU budget 70h not justified for supplementary signal"
      hypothetical_bimodal_items_pct: 12.5
      hypothetical_overlap_with_dif_jaccard: 0.13
    result_rationale: >
      同 plan_003a 逻辑。DVD 检测 variant contamination（模型在 paraphrase 上表现方差异常），
      与 DIF 的 temporal cohort contrast 方法论完全不同。Best 档下 GPU budget (70h)
      分配给更高优先级的 plan_002 (100h)。Hypothetical Jaccard ~0.13 说明即使执行，
      DVD 捕获的 items 与 DIF 重叠极低——这本身可以是 interesting finding，但不足以
      justify 70h GPU + 额外 0.5 页篇幅在已经需要压缩 2 页的论文中。
    tables: []
    figures_description: []
    analysis: >
      正确 drop。Best 档 framing 是 "DIF as diagnostic lens"，不是 "comprehensive
      detection toolkit comparison"。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: "DIF + ConStat + DVD 三信号融合：majority voting + weighted fusion + 5-fold cross-validation"
    expected_results:
      status: not_executed
      reason: "Killed — depends on 003a/003b, both dropped; ensemble is old 'detection' framing, incompatible with current 'characterization' narrative"
    result_rationale: >
      Ensemble 是 original Claim 2 ("multi-signal detection") 的核心。Paper pivot 后
      Claim 2 变成 "ground truth meta-critique"，ensemble 变成 conceptual orphan。
      Best 档 reviewer 看到 ensemble 反而会问 "为什么 characterization paper 里有
      detection ensemble？narrative 不一致"。正确 kill。
    tables: []
    figures_description: []
    analysis: >
      Killed early 是正确决策。Best 档下 reviewer 看重 narrative coherence。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: "GSM8K (1319 items × 6702 models) 上的 DIF 复制 + GSM1K ground truth correlation + semi-synthetic framework portability"
    expected_results:
      step1_gsm8k_temporal_c_pct: 18.9
      step1_sanity_c_pct: 0.3
      step1_standard_external_spearman: 0.926
      step2_standard_delta_tpr_p10: 0.818
      step2_external_delta_tpr_p10: 0.517
      step3_n_models: 33
      step3_pearson_r: -0.478
      step3_spearman_rho: -0.403
      step3_partial_r_controlling_accuracy: -0.385
      step3_permutation_p: 0.014
      step3_direction: "NEGATIVE — DIF-C items anti-correlate with contamination gap"
      step3_leave_one_out_r_range: "-0.537 to -0.374"
      step3_robust: true
    result_rationale: >
      Best 档下 GSM8K C%=18.9% 落在 cross-benchmark range 下端 (17.9-31.3%)，与 6-benchmark
      pattern 一致，强化 generalizability。Semi-synthetic ΔTPR=+0.818 (standard matching)
      显著高于 MMLU 的 +0.674——单一 domain benchmark 的 matching variable 更干净（GSM8K
      只有数学一个 domain，cross-subject matching 实际上是 external score matching）。
      GSM1K correlation r=-0.478 方向为负（DIF 高的 models 反而 contamination gap 小），
      counter-intuitive 但在 best 档下被 framing 为：DIF 检测的是 differential functioning
      而非 contamination，web-overlap contamination gap 和 DIF 正交——这恰恰 empirically
      证实了 Claim 2 的 ground truth meta-critique。N=33 和 CI width 导致此结果被
      demote 到 exploratory，reviewer 接受这个 honest positioning。
    tables:
      - "Table S-GSM8K: Step 1-3 summary metrics"
    figures_description:
      - "Figure panel in main text: GSM8K C%=18.9% alongside 5 other benchmarks in cross-benchmark summary figure"
    analysis: >
      GSM8K 结果在 best 档下 serve two roles：(1) 6-benchmark consistency 的一个数据点
      (2) semi-synthetic framework portability 的独立验证。GSM1K negative correlation
      被 correctly demoted to exploratory per Dream #6 three-tier consensus。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: "Bifactor IRT equating on MMLU: general factor + 57 subject-specific factors, anchor item selection, fixed-parameter calibration"
    expected_results:
      status: killed
      bifactor_fit_rmsea: 0.038
      bifactor_fit_cfi: 0.72
      bifactor_general_factor_variance_explained: 0.31
      anchor_item_selection_n: 0
      kill_reason: "plan_014 pre-check showed within-subject C%=38.1% — no stable anchor items exist; bifactor fit inadequate (CFI<0.90) for 57-subject MMLU"
    result_rationale: >
      Best 档下 bifactor 被 plan_014 pre-check 正确 kill。Within-subject C%=38.1%
      意味着即使控制 subject-level ability，仍有 ~38% items 是 unstable——没有足够的
      stable anchor items 来做 equating。MMLU 的 57-subject 结构使得 bifactor model
      需要估计 58 个 latent factors (1 general + 57 specific)，N=5219 models 对此
      参数量严重不足 (items-per-factor ratio ≈ 216，但 models-per-factor ≈ 90，
      低于 bifactor recommended minimum ~200)。CFI=0.72 远低于 0.90 threshold。
      Best 档 reviewer 看到 "we tried IRT equating, structural pre-checks killed it,
      this motivates future multidimensional IRT work" 视为 methodological honesty。
    tables: []
    figures_description: []
    analysis: >
      Killed 后其残余价值是 Discussion 中一句话："bifactor equating was infeasible due to
      MMLU's extreme multidimensionality (57 subjects, within-subject C%=38.1%),
      motivating future work on multidimensional IRT approaches."

  - name: item_generation_calibration
    plan_id: plan_006
    description: "LLM-based replacement item generation for DIF-flagged MMLU items + student simulation calibration"
    expected_results:
      status: not_executed
      reason: "Dependency plan_005 killed — no equating framework to calibrate into"
      hypothetical_difficulty_rho_prompt_based: 0.28
      hypothetical_difficulty_rho_sim_calibrated: 0.78
    result_rationale: >
      plan_005 killed 后 plan_006 失去了 calibration target。即使独立执行，prompt-based
      difficulty targeting (ρ≈0.28 per 文献 arXiv 2602.06631) 不足以替代 empirical
      calibration。Student simulation (arXiv 2601.09953) 可提升到 ρ≈0.78，但没有
      equating framework，generated items 无法嵌入 benchmarks 进行 equated scoring。
      Best 档不需要此实验——paper contribution 是 "characterize instability + provide
      audit protocol"，不是 "regenerate benchmark"。Reviewer 不期望 discovery paper
      同时 solve the problem it discovers。
    tables: []
    figures_description: []
    analysis: >
      正确 drop。Regeneration 是 separate paper 的工作量。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: "Sinharay et al. (2006) cumulative Bayesian DIF priors：4 successive administrations simulation, power accumulation curve"
    expected_results:
      single_admin_power_delta10: 0.42
      cumulative_2admin_power_delta10: 0.58
      cumulative_3admin_power_delta10: 0.69
      cumulative_4admin_power_delta10: 0.74
      single_admin_power_delta14: 0.68
      cumulative_3admin_power_delta14: 0.85
      false_positive_rate_cumulative: 0.048
      prior_shrinkage_effect: "medium-effect items (δ=1.0) benefit most from accumulation; large-effect (δ≥1.4) already detected in single admin"
    result_rationale: >
      Best 档下 cumulative Bayesian DIF 是 simulation-only appendix material。
      Power 从 single-admin 0.42 上升到 3-admin 0.69 (δ=1.0) 是理论预期——Bayesian
      prior 将前一轮的 posterior 作为下一轮的 prior，evidence accumulates across
      independent administrations。FPR 保持在 0.048 因为 null items 的 posterior
      在每轮 administration 中 shrink toward zero。对 medium effects (δ=1.0) 提升最大
      是因为这些 items 在 single admin 中 power 不足 (0.42)，有最大的 improvement margin；
      large effects (δ≥1.4) 在 single admin 已有 power=0.68+，accumulation 边际收益递减。
      Best 档 reviewer 视此为 "nice forward-looking contribution" 但不是 core claim。
    tables:
      - "Table S-Bayes: Power × #administrations × effect size matrix"
    figures_description:
      - "Figure S-Bayes: Power accumulation curves for δ ∈ {0.6, 1.0, 1.4, 2.0} across 1-4 administrations"
    analysis: >
      Appendix only。Best 档下提供 forward-looking value——如果 benchmark maintainers
      adopt DIF audit protocol (Claim 4)，cumulative priors 使得 monitoring across
      quarterly releases 更有统计 power。与 audit protocol 形成 conceptual bridge。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: "Progressive item replacement 下 benchmark validity 退化分析：5%-50% replacement rate × ranking stability/reliability/construct coverage"
    expected_results:
      replacement_5pct_rho: 0.9991
      replacement_10pct_rho: 0.9978
      replacement_20pct_rho: 0.9943
      replacement_50pct_rho: 0.9712
      replacement_5pct_reliability_alpha: 0.982
      replacement_10pct_reliability_alpha: 0.979
      replacement_20pct_reliability_alpha: 0.971
      replacement_50pct_reliability_alpha: 0.938
      construct_coverage_maintained_up_to: "30% replacement"
      critical_degradation_threshold: "~40% replacement → ρ < 0.98"
    result_rationale: >
      Best 档下 graceful degradation 用 simplified version（random replacement from
      same-subject item pool，而非 plan_005/006 的 calibrated replacement）。Plan_017
      已经证明 removing 31% DIF items 后 ρ=0.996-0.999——这意味着 MMLU 有 massive
      measurement redundancy。Random replacement 应产生类似结果：在 20% replacement
      rate 下 ρ>0.99 是因为 12,508 items 中 subjects 内部 items 高度 redundant
      (plan_013 mean Q3=0.0086 within-subject，说明 local independence 基本成立，
      但 subject-level redundancy 很高)。50% replacement 时 ρ 仍 >0.97 因为
      ranking 主要由 general factor 决定（bifactor pre-check 显示 general factor
      解释 ~31% variance），individual items 的边际贡献极小。这些数字 reinforce
      "instability ≠ invalidity" framing。
    tables:
      - "Table S-Degrade: Replacement rate × validity metric matrix"
    figures_description:
      - "Figure S-Degrade: ρ and α degradation curves with 95% CI bands"
    analysis: >
      Appendix/supplementary。Best 档下 reinforces Claim 4 的 "massive redundancy"
      sub-finding (ρ≈0.997)。不是 core contribution 但 provides quantitative backing
      for the "instability ≠ invalidity" narrative。

  - name: item_focused_trees
    plan_id: plan_009
    description: "Tutz & Berger (2016) Item-Focused Trees：model release date 作为 continuous covariate，避免 arbitrary cohort split"
    expected_results:
      n_items_with_significant_split: 4287
      pct_items_with_temporal_split: 34.3
      primary_split_date_median: "2023-09-15"
      primary_split_date_iqr: "2023-06-01 to 2024-01-15"
      concordance_with_mh_c_class: 0.81
      jaccard_ift_vs_mh_c: 0.74
      items_detected_only_by_ift: 812
      items_detected_only_by_mh: 443
      acceleration_post_mid2023: true
      effect_size_gradient_slope: 0.18
    result_rationale: >
      Best 档下 IFT 作为 robustness check 确认 MH-DIF 的 binary split 不是 arbitrary
      cutoff artifact。34.3% items 显示 significant temporal split——略高于 MH 的 31.3%
      因为 IFT 可以在任意时间点发现 split，不受 2023/2024 binary 限制。Concordance=0.81
      说明大部分 MH-C items 也被 IFT 检测到，但有 812 items only IFT detects——这些
      可能在 2023 年中某个时间点 function shift，MH 的 binary 粒度无法捕获。
      Median split date 2023-09-15 说明 primary transition 发生在 2023 H2，
      与 GPT-4/Llama-2 release timing 一致。IFT 结果 strengthen the case that
      temporal binary split 是 reasonable first-pass：虽然 continuous treatment
      更精细，但 81% concordance 说明 binary split 已经 capture 了主要 signal。
      Best 档 reviewer 原本可能 concern "why not quarterly split?"——IFT 结果
      预先回答了这个问题。
    tables:
      - "Table S-IFT: IFT vs MH concordance matrix + split date distribution"
    figures_description:
      - "Figure S-IFT: Split date histogram + effect size gradient over time"
    analysis: >
      Appendix robustness check。Best 档下 serves dual purpose：(1) validates binary
      split choice, (2) shows continuous treatment produces consistent findings。
      一句话在 main text 引用："Item-Focused Trees with continuous temporal covariate
      confirm 81% concordance with binary MH-DIF (Appendix X)."

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: "Decoder-only subpopulation DIF：移除 architecture heterogeneity 后检查 IRT fit 和 DIF stability"
    expected_results:
      total_models: 5227
      decoder_only_models: 5226
      non_decoder_models: 1
      decoder_only_pct: 99.98
      c_pct_full: 31.3
      c_pct_decoder_only: 31.3
      jaccard_full_vs_decoder_only: 1.0
      irt_fit_rmsea_full: 0.052
      irt_fit_rmsea_decoder_only: 0.052
      irt_fit_change: "negligible — 1 model removal cannot affect fit"
      architecture_confound: "non-issue"
    result_rationale: >
      Best 档下 architecture stratification 是 trivially resolved concern。METABENCH
      MMLU 中 5226/5227 models 是 decoder-only (99.98%)，仅 1 个 non-decoder model。
      移除 1 个 model 后 Jaccard=1.0 (DIF flags 完全不变)，IRT fit 变化 negligible
      (RMSEA 变化在 numerical precision 内)。这不是因为 DIF 对 architecture robust，
      而是因为 MMLU evaluation landscape 已经 homogeneously decoder-only。Reviewer
      concern "IRT misfit comes from architecture heterogeneity" 被数据直接 refute：
      heterogeneity 不存在。IRT misfit (98% |Lz|>2) 的真实原因是 MMLU 的 57-subject
      multidimensionality，不是 architecture mix。Best 档下此实验用一句话报告。
    tables: []
    figures_description: []
    analysis: >
      一句话 in main text 足矣："METABENCH MMLU is 99.98% decoder-only (5,226/5,227);
      excluding the single non-decoder model leaves DIF flags unchanged (Jaccard=1.0)."
      Proactively closes architecture heterogeneity concern。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: "已知 ground truth 的 semi-synthetic contamination injection：500 clean items 中注入 100-200 items 的 differential contamination，测量 DIF detection power"
    expected_results:
      temporal_external_tpr_p0_baseline: 0.326
      temporal_external_tpr_p03: 0.548
      temporal_external_tpr_p05: 0.834
      temporal_external_tpr_p07: 0.990
      temporal_external_tpr_p10: 1.000
      temporal_external_fpr: 0.314
      temporal_external_delta_tpr_p05: 0.508
      temporal_external_delta_tpr_p10: 0.674
      ability_external_delta_tpr_p10: 0.302
      standard_mh_fpr_inflation_at_p10: "0.298→0.616"
      matching_variable_contamination_confirmed: true
      cross_subject_matching_delta_fpr: 0.000
      dose_response_monotonic: true
    result_rationale: >
      Best 档下 semi-synthetic 是 Claim 3 的核心 evidence。ΔTPR=+0.508 at p=0.5
      意味着在 50% exploitation rate 下，DIF detection power 增加 50.8 个百分点——
      从 baseline 32.6% (already-existing DIF) 到 83.4% (baseline + injected)。
      Dose-response 单调递增 (p=0.3→0.5→0.7→1.0 对应 ΔTPR 逐步增加) 证明
      detection power 与 contamination intensity 正相关，排除 artifact。
      Cross-subject matching ΔFPR=0.000 是 key methodological innovation——在所有
      injection levels 下 FPR 完全不变，证明 cross-subject total score 作为 matching
      variable 不受 target-subject contamination 污染。对比 standard MH matching
      (within-subject score) FPR 从 0.298 膨胀到 0.616，直接 demonstrate matching
      variable contamination problem。这个 ΔFPR=0.000 vs 0.186 inflation 的 contrast
      是 reviewer 接受 Claim 3 的关键——它既是 methodological contribution 又是
      practical recommendation。
    tables:
      - "Table 2 (main): Semi-synthetic ΔTPR across exploitation rates p ∈ {0.3, 0.5, 0.7, 1.0} — cross-subject vs standard matching"
    figures_description:
      - "Figure 2: Dose-response curve (exploitation rate vs ΔTPR) with cross-subject (solid) vs standard (dashed) matching + FPR inflation panel"
    analysis: >
      Main text Claim 3 核心 evidence。Best 档下 reviewer 视 cross-subject matching
      (ΔFPR=0.000) 为 "practical methodological innovation worth reporting"——subtle
      insight that within-subject matching contaminates the conditioning variable,
      with clean empirical demonstration。

  - name: multi_benchmark_temporal_dif
    plan_id: plan_028
    description: "6-benchmark cross-validation：MMLU, WinoGrande, TruthfulQA, ARC-Challenge, GSM8K, HellaSwag 上的 temporal DIF (2023 vs 2024)"
    expected_results:
      mmlu_c_pct: 31.3
      mmlu_random_c_pct: 0.18
      mmlu_enrichment: 174
      winogrande_c_pct: 30.3
      winogrande_random_c_pct: 0.32
      winogrande_enrichment: 95
      truthfulqa_c_pct: 29.7
      truthfulqa_random_c_pct: 0.37
      truthfulqa_enrichment: 80
      arc_c_pct: 26.9
      arc_random_c_pct: 0.60
      arc_enrichment: 45
      gsm8k_c_pct: 18.9
      gsm8k_random_c_pct: 0.30
      gsm8k_enrichment: 63
      hellaswag_c_pct: 17.9
      hellaswag_random_c_pct: 0.28
      hellaswag_enrichment: 64
      cross_benchmark_range: "17.9-31.3%"
      all_random_below_1pct: true
      min_enrichment_ratio: 45
      n_benchmarks: 6
    result_rationale: >
      Best 档的 single most important new result。6 benchmarks 全部 C% ≥ 17.9%，
      all ≥45× above random control，彻底封堵 "only MMLU" 攻击面。
      C% 变异 (17.9-31.3%) 反映 benchmark structural differences：
      - MMLU (31.3%) 最高因为 57 subjects 覆盖最广，items 最多 (12,508)，temporal
        capability shift 有更多 dimensions 可以 manifest as DIF。
      - WinoGrande (30.3%) 和 TruthfulQA (29.7%) 接近 MMLU 因为它们测试 commonsense
        reasoning 和 factual knowledge——这些 domains 在 2023→2024 变化大 (GPT-4,
        Llama-2→3 的主要 capability jumps 集中在 reasoning/knowledge)。
      - ARC-Challenge (26.9%) 中等——science reasoning 有 capability jump 但
        item pool 较小 (1,172) 限制了 DIF detection power。
      - GSM8K (18.9%) 和 HellaSwag (17.9%) 最低因为：GSM8K 是 math word problems，
        solution structure 更 formulaic，item functioning 更 stable across generations；
        HellaSwag 是 commonsense NLI，10,042 items 但 item difficulty variance 较低
        (多数 items 在 easy-to-medium range)，DIF effect size 被 compressed。
      All random controls <1% 证明 MH-DIF 的 type I error 在所有 benchmarks 上
      well-calibrated。45× minimum enrichment (ARC) 使得 "DIF flags are noise"
      攻击面不可行。
    tables:
      - "Table 3 (main): 6-benchmark cross-validation summary — N_items, N_ref, N_foc, C%, random C%, enrichment ratio"
    figures_description:
      - "Figure 3: Cross-benchmark C% bar chart with random control overlay + enrichment ratio annotations"
    analysis: >
      Best 档 cornerstone result。一张 summary table + 一个 figure panel (per
      paper_framing plan_028 压缩要求)。This single result upgrades the paper from
      "interesting MMLU analysis" to "generalizable finding about LLM benchmarks as
      a class"。Reviewer avg score 从 ~3.5 推到 4.0+ 主要来自此 result。

  - name: permutation_null_c_rate
    plan_id: plan_029
    description: "1000× permutation test：随机重分配 2023/2024 temporal labels，建立 C% null distribution"
    expected_results:
      n_permutations: 1000
      null_c_pct_mean: 0.21
      null_c_pct_sd: 0.09
      null_c_pct_max: 0.58
      null_c_pct_p999: 0.52
      observed_c_pct: 31.3
      z_score: 345.4
      empirical_p_value: "<0.001 (0/1000 permutations exceed observed)"
      effect_size_vs_null: "148× above null mean"
    result_rationale: >
      Best 档下 permutation null 提供比 random-split control (0.18%) 更严格的
      statistical test。Random split 是 within-cohort 随机分组——它控制的是 "same
      temporal window 内 MH 是否产生 spurious DIF"。Permutation test 是 across-cohort
      label shuffling——它控制的是 "temporal label assignment 本身是否与 DIF 有关"。
      Null C% mean=0.21% (vs random split 0.18%) 几乎相同因为两者本质上都在测试
      "ability distribution overlap 能否产生 spurious DIF"——当 labels 被 permute，
      两组 ability distributions 变得 exchangeable，MH 的 ability conditioning
      使得 spurious DIF 接近 zero。SD=0.09% 说明 null distribution 非常 concentrated，
      max=0.58% 说明即使最极端的 permutation 也远低于 1%。Z=345 (>200σ) 使得
      p<10^{-100} level significance。Best 档 reviewer 看到 permutation test
      后不再质疑 "is 31% above chance?"——问题 definitively closed。
    tables:
      - "Table S-Perm: Permutation null distribution summary statistics"
    figures_description:
      - "Figure S-Perm: Null C% histogram with observed 31.3% marked (off-scale)"
    analysis: >
      Main text 一句话引用，full results in appendix。"Permutation test (1,000
      iterations) yields null C%=0.21±0.09%, observed 31.3% is >200σ above null
      (p<0.001)." 与 random split 0.18% 互补——两种 null construction 给出
      一致结论。Best 档下 reviewer 接受 binary split 因为 permutation test
      demonstrates temporal labels carry genuine signal。

  - name: odds_ratio_regression_transparency
    plan_id: plan_030
    description: "Odds ratio + Simpson's paradox 分析：domain-level vs item-level accuracy delta 对 DIF flag 的 logistic regression，McFadden/Nagelkerke R², OR + 95% CI"
    expected_results:
      model1_domain_delta:
        mcfadden_r2: 0.0007
        nagelkerke_r2: 0.0012
        subject_acc_delta_or_per_010: 1.55
        subject_acc_delta_or_ci: [1.19, 2.03]
        interpretation: "domains with larger 2024-2023 accuracy improvement have slightly MORE DIF — naïve positive association"
      model2_domain_delta_plus_items:
        mcfadden_r2: 0.0423
        nagelkerke_r2: 0.072
        subject_acc_delta_or_per_010: 0.73
        ctt_difficulty_or_per_010: 0.78
        ctt_discrimination_or_per_010: 1.51
        interpretation: "SIMPSON'S PARADOX — after controlling for item difficulty and discrimination, domain improvement NEGATIVELY predicts DIF"
      model3_item_delta:
        mcfadden_r2: 0.0012
        nagelkerke_r2: 0.0021
        item_acc_change_or_per_010: 1.08
        item_acc_change_ci: [1.51, 2.96]
      model4_item_delta_plus_items:
        mcfadden_r2: 0.0434
        nagelkerke_r2: 0.0737
        item_acc_change_or_per_010: 0.92
        ctt_difficulty_or_per_010: 0.77
        ctt_discrimination_or_per_010: 1.54
      simpsons_paradox: true
      simpsons_or_flip: "1.55 → 0.73"
      lr_test_m1_vs_m2_chi2: 646.98
      lr_test_m3_vs_m4_chi2: 655.53
    result_rationale: >
      Best 档的 second most important new result。Simpson's paradox (OR 1.55→0.73)
      是 "ability confound doesn't drive DIF" 的最强 evidence。
      机制：Model 1 只看 domain-level accuracy delta → OR=1.55，因为 capability
      improvement 大的 domains 确实有更多 DIF items (ρ=0.307 ecological correlation)。
      但 Model 2 加入 item-level difficulty 和 discrimination 后 → OR=0.73 REVERSES。
      这是因为 DIF-C items 本身有 specific item properties (harder: d=-0.247,
      higher discrimination: d=0.230, per plan_023)，这些 item properties confound
      domain-level correlation。Controlling for item properties reveals that domain
      improvement actually REDUCES DIF probability (OR=0.73 < 1.0)——domains with
      larger improvement have FEWER DIF items after accounting for item characteristics。
      
      R² 极低 (McFadden 0.0007→0.0423) 说明即使 best model 也只解释 ~4% variance
      ——96% of DIF is item-specific, not explained by domain improvement OR item
      properties。这 reinforces plan_019 的 "≤2.4pp/7.6%" 结论 via 完全不同的
      statistical framework (logistic regression vs decomposition)，形成 converging
      evidence。
      
      Best 档 reviewer 看到 Simpson's paradox reversal 后接受 "DIF is not driven by
      capability improvement"——这是一个 well-known statistical phenomenon，
      reviewers 理解其 implications。LR test χ²=647 (p≈0) 证明 item properties
      是 genuine confounders，不是 noise。
    tables:
      - "Table 4 (main): 4-model logistic regression comparison — predictors, OR [95% CI], McFadden R², LR test"
    figures_description:
      - "Figure 4: Simpson's paradox visualization — domain-level OR=1.55 (positive slope) vs item-controlled OR=0.73 (negative slope)"
    analysis: >
      Main text Claim 1 的 second pillar (alongside plan_019 decomposition)。
      Simpson's paradox 比 R²=0.0007 更直观——reviewer 可能不理解 "pseudo R² 解释
      0.07% variance"，但一定理解 "association REVERSES after controlling for
      confounders"。Best 档下此 figure 是 paper 中 most memorable visualization——
      两条相反方向的 regression slopes in the same plot。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3bd36fc-a918-43a3-bc22-f5d6be9ea128",
  "isSidechain": false,
  "requestId": "req_011CbFcCBVhdi1VcqWGiVG6R",
  "type": "assistant",
  "uuid": "75fcd240-c98f-4167-8b1d-9aa9b6c98d44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7b6EvR81VARY6yuMLp4db",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20945,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14116,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20945
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：6-benchmark cross-validation + Simpson's paradox 完全封堵了主要攻击面；reviewer 接受 IRT misfit 作为 conservative estimate 的 framing；temporal binary split 被视为合理的 first-pa…",
  "leafUuid": "75fcd240-c98f-4167-8b1d-9aa9b6c98d44",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric DIF reveals temporal benchmark instability across 6 benchmarks",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：6-benchmark cross-validation + Simpson's paradox 完全封堵了主要攻击面；reviewer 接受 IRT misfit 作为 conservative estimate 的 framing；temporal binary split 被视为合理的 first-pa…",
  "leafUuid": "75fcd240-c98f-4167-8b1d-9aa9b6c98d44",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric DIF reveals temporal benchmark instability across 6 benchmarks",
  "sessionId": "3893de7d-e708-46c7-b68b-82b376487d7e"
}
```

---
