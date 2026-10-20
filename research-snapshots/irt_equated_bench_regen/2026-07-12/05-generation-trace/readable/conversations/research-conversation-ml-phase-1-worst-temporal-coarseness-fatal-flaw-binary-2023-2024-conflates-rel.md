# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Temporal coarseness 被视为 fatal flaw（binary 2023/2024 conflates release timin

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/70c7d4b0-5ee0-486b-87d8-4697f59a1249.jsonl`
- **Structured JSON:** [`00aca1463cfabb02ea0a.json`](../../sessions/00/00aca1463cfabb02ea0a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T11:24:04.277Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T11:24:04.277Z",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Temporal coarseness 被视为 fatal flaw（binary 2023/2024 conflates release timing, training data cutoff, architecture shifts），且 IRT misfit (98%) 被解读为 MH 结果不可信。Reviewer 认为 DIF 只是在 measure 'models got better' 的 artifact，despite decomposition evidence。核心 'temporal instability' framing 不成立，需要 reframe 为 methodological contribution。\n核心假设：['至少两个 reviewer 将 temporal binary split 视为 fundamental design flaw——认为 2023→2024 捆绑了太多 confound (architecture, scale, training data, RLHF adoption)，DIF 发现的是 generation gap 而非 item instability', \"IRT misfit (98% |Lz|>2) 被解读为 MH conditioning variable (total score) 在 MMLU 上无效——'你在用错误的 ability estimate 做 conditioning，结果不可解释'\", \"Simpson's paradox 被反转利用：reviewer 论证 OR flip 说明 item-level properties 才是真正驱动 DIF 的因素，而非 temporal signal——DIF 只是挑出了 hard + high-discrimination items\", \"Cross-benchmark 一致性被解读为 artifact 的进一步证据——'所有 benchmark 都显示 DIF 恰恰说明这是 method artifact，不是 benchmark-specific instability'\", \"Actionability 被认为严重不足——'你发现了 31% instability 但没有给出任何可执行的修复方案'\"]\n关键指标范围：{'reviewer_avg_score': [2.5, 3.2], 'cross_bench_c_pct_min': [12.0, 18.0], 'cross_bench_c_pct_max': [28.0, 33.0], 'ability_confound_explained_pp': [3.0, 8.0], 'simpsons_or_flip_magnitude': [0.9, 1.3], 'semi_synthetic_delta_tpr_p05': [0.3, 0.5], 'ranking_rho_after_removal': [0.993, 0.999], 'reviewer_count_reject_recommendation': [1, 2]}\n叙事方向：放弃 'temporal instability as primary finding' framing。Reframe 为 methodological contribution paper：(1) Semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000) 升级为 primary contribution——这是最 reviewer-proof 的 claim，不依赖 temporal design 或 IRT fit；(2) Ground truth meta-critique 升级为 co-primary contribution——6 benchmark 的 enrichment≈1.0 一致性现在支持的是 'web-overlap labels are fundamentally mismatched' 而非 'benchmarks are unstable'；(3) Temporal DIF findings 降级为 motivating example / case study——'applying our framework to temporal cohorts reveals patterns consistent with item-level behavioral changes, though disentangling from cohort-level confounds requires finer-grained temporal design'；(4) Audit protocol 从 actionable output 重新定位为 'proposed workflow for future investigation'。Title 从 'Temporal Instability in LLM Benchmarks' 改为类似 'Validating Item-Level Contamination Detection: A Semi-Synthetic Framework with Cross-Subject Matching'。仍冲 EMNLP——methodology track 对 framework + meta-critique 型贡献友好，但需要 substantially 重写 intro/framing。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\nfocus: plan_028 新增 6-benchmark cross-validation (C%=17.9-31.3%, 45-174× above random) + plan_030 Simpson's paradox (OR 1.55→0.73)。评估这些新数据是否将 Best 从 3.5 推到 4.0+ (Conference acceptance)。重点关注：IRT misfit defense 是否充分、temporal coarseness (2023 vs 2024 binary) 是否仍是主要攻击面、actionability gap 是否被 audit protocol 覆盖。\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T11:24:04.280Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T11:24:04.280Z",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T11:24:04.303Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Temporal coarseness 被视为 fatal flaw（binary 2023/2024 conflates release timing, training data cutoff, architecture shifts），且 IRT misfit (98%) 被解读为 MH 结果不可信。Reviewer 认为 DIF 只是在 measure 'models got better' 的 artifact，despite decomposition evidence。核心 'temporal instability' framing 不成立，需要 reframe 为 methodological contribution。
核心假设：['至少两个 reviewer 将 temporal binary split 视为 fundamental design flaw——认为 2023→2024 捆绑了太多 confound (architecture, scale, training data, RLHF adoption)，DIF 发现的是 generation gap 而非 item instability', "IRT misfit (98% |Lz|>2) 被解读为 MH conditioning variable (total score) 在 MMLU 上无效——'你在用错误的 ability estimate 做 conditioning，结果不可解释'", "Simpson's paradox 被反转利用：reviewer 论证 OR flip 说明 item-level properties 才是真正驱动 DIF 的因素，而非 temporal signal——DIF 只是挑出了 hard + high-discrimination items", "Cross-benchmark 一致性被解读为 artifact 的进一步证据——'所有 benchmark 都显示 DIF 恰恰说明这是 method artifact，不是 benchmark-specific instability'", "Actionability 被认为严重不足——'你发现了 31% instability 但没有给出任何可执行的修复方案'"]
关键指标范围：{'reviewer_avg_score': [2.5, 3.2], 'cross_bench_c_pct_min': [12.0, 18.0], 'cross_bench_c_pct_max': [28.0, 33.0], 'ability_confound_explained_pp': [3.0, 8.0], 'simpsons_or_flip_magnitude': [0.9, 1.3], 'semi_synthetic_delta_tpr_p05': [0.3, 0.5], 'ranking_rho_after_removal': [0.993, 0.999], 'reviewer_count_reject_recommendation': [1, 2]}
叙事方向：放弃 'temporal instability as primary finding' framing。Reframe 为 methodological contribution paper：(1) Semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000) 升级为 primary contribution——这是最 reviewer-proof 的 claim，不依赖 temporal design 或 IRT fit；(2) Ground truth meta-critique 升级为 co-primary contribution——6 benchmark 的 enrichment≈1.0 一致性现在支持的是 'web-overlap labels are fundamentally mismatched' 而非 'benchmarks are unstable'；(3) Temporal DIF findings 降级为 motivating example / case study——'applying our framework to temporal cohorts reveals patterns consistent with item-level behavioral changes, though disentangling from cohort-level confounds requires finer-grained temporal design'；(4) Audit protocol 从 actionable output 重新定位为 'proposed workflow for future investigation'。Title 从 'Temporal Instability in LLM Benchmarks' 改为类似 'Validating Item-Level Contamination Detection: A Semi-Synthetic Framework with Cross-Subject Matching'。仍冲 EMNLP——methodology track 对 framework + meta-critique 型贡献友好，但需要 substantially 重写 intro/framing。

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
  "promptId": "0b97c78d-d9e0-4d5c-8824-00fc1cb24045",
  "type": "user",
  "uuid": "436e9f9c-c255-4165-8fce-365edc2b0ac1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T11:24:04.301Z_

```json
{
  "parentUuid": "436e9f9c-c255-4165-8fce-365edc2b0ac1",
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
  "uuid": "882e859c-5f5b-49bf-beb3-0395f7fba0b5",
  "timestamp": "2026-05-21T11:24:04.301Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T11:24:04.302Z_

```json
{
  "parentUuid": "882e859c-5f5b-49bf-beb3-0395f7fba0b5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2950f2fa-83a1-44c9-a14f-43021deee623",
  "timestamp": "2026-05-21T11:24:04.302Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Temporal coarseness 被视为 fatal flaw（binary 2023/2024 conflates release timing, training data cutoff, architecture shifts），且 IRT misfit (98%) 被解读为 MH 结果不可信。…",
  "leafUuid": "2950f2fa-83a1-44c9-a14f-43021deee623",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Semi-synthetic validation framework for item-level contamination detection",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249"
}
```

---

### Assistant

_source line 8 · 2026-05-21T11:24:46.419Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each experiment in the experiment_plan, under the "worst" tier scenario. Let me carefully go through the worst tier definition and each experiment, then predict what results would look like under this pessimistic reviewer scenario.

Let me understand the worst tier:
- Temporal coarseness is a fatal flaw (binary 2023/2024 conflates too many confounds)
- IRT misfit (98%) makes MH results untrustworthy
- DIF is just measuring "models got better" artifact
- Core temporal instability framing doesn't hold
- Need to reframe as methodological contribution


Now I'm looking at the metric ranges that would characterize this worst-case scenario across the experiments.

Let me work through each planned experiment and see how these worst-tier metrics would affect the predictions. I've got eleven experiments to evaluate, ranging from the MMLU validation work through to the item generation studies, and I need to see how the performance would degrade under these worst-case conditions. I need to generate worst-tier predictions for every experiment in the plan, including those already completed, treating these as imagined scenarios rather than actual results. For each one, I'll work through what the worst-case interpretation would look like and provide detailed rationales.

Starting with plan_001: under the worst scenario, the temporal contamination rate of 31.3% gets reframed as an artifact of cohort confounding rather than genuine contamination. Domain correlation would be moderate, implying that capability differences rather than data leakage are driving the observed DIF patterns. The enrichment analysis wouldn't provide clear evidence either way, and within-family DIF would be surprisingly high, suggesting it's measuring capability gaps instead of contamination signals.

For plan_002, the small sample of 13 reasoning-RL models becomes a critical weakness—adding more RL variants would substantially shift which items get flagged as DIF, undermining any robustness claims. Traditional detection methods might fail to adapt to the RL-specific patterns.

Moving through the remaining experiments: ConStat and DVD would each show reasonable detection power on their own, making the ensemble approach seem redundant. The cross-benchmark validation on GSM8K would show negative correlation with contamination, flipping the interpretation. The bifactor IRT model would fail to converge or fit poorly, blocking the equating pipeline. Generated items would show weak calibration with low difficulty correlation. And the cumulative Bayesian DIF analysis would face similar convergence or interpretability issues. The permutation null distribution is extremely tight at 0.2-0.5%, making the observed 31% look significant on the surface, but critics contend this only demonstrates temporal variation exists rather than proving items themselves are unstable—they argue the signal could just reflect general model improvement over time. Simpson's paradox compounds this problem: the odds ratio flips dramatically from 1.55 to 0.73 depending on how you stratify the data, which reviewers weaponize to claim item characteristics are actually the hidden confound driving the apparent DIF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2950f2fa-83a1-44c9-a14f-43021deee623",
  "isSidechain": false,
  "requestId": "req_011CbFdTuMfPUyoVnqXc8ua3",
  "type": "assistant",
  "uuid": "b2aa85f1-ca49-4c05-ae43-2249caf9eb9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GABwavEqKkaCoXid4ih8cw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21197,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14884,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21197,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14884,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21197
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

_source line 9 · 2026-05-21T11:29:16.899Z_

```yaml
tier: worst
narrative_guidance: >
  放弃 'temporal instability as primary finding' framing。Reframe 为 methodological contribution paper：
  (1) Semi-synthetic validation framework (ΔFPR=0.000) 升级为 primary contribution；
  (2) Ground truth meta-critique 升级为 co-primary contribution；
  (3) Temporal DIF findings 降级为 motivating example / case study；
  (4) Audit protocol 重新定位为 'proposed workflow'。
  Title 改为类似 'Validating Item-Level Contamination Detection: A Semi-Synthetic Framework with Cross-Subject Matching'。
  仍冲 EMNLP methodology track，但需要 substantially 重写 intro/framing。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: "METABENCH MMLU response matrix (5,219 models × 12,508 items) 上的 MH-DIF 分析，含 temporal/ability cohort、within-family confound control、domain-specificity"
    expected_results:
      temporal_ets_c_pct: 31.3
      temporal_fpr_li_clean: 0.32
      temporal_enrichment: 0.96
      ability_ets_c_pct: 2.9
      ability_enrichment: 1.19
      within_family_llama2v3_c_pct: 61.3
      within_family_mistral_mixtral_c_pct: 38.7
      domain_spearman_rho: 0.38
      domain_spearman_p: 0.004
      sanity_random_split_c_pct: 0.18
      temporal_ability_jaccard: 0.014
      irt_lz_above_2_pct: 98.0
    result_rationale: >
      在 worst 档下，31.3% C% 本身可复现但被 reviewer 视为 artifact。核心攻击点：
      (1) domain_spearman_rho=0.38 (p=0.004) 比 best 档预期的 0.25-0.30 更高，reviewer 用此论证 DIF 主要捕捉
      domain-level capability improvement 而非 item instability；
      (2) within-family Llama-2v3 C%=61.3% 被解读为 "DIF 在测 generation gap"——Llama-2 到 Llama-3
      是 architecture + scale + data 全面升级，61% DIF 恰恰说明 DIF 在测能力提升；
      (3) enrichment=0.96 ≈ 1.0 被解读为 DIF 与任何已知 contamination signal 无关——"你的方法跟
      contamination 没关系，它只是在找 hard items that newer models solve"；
      (4) IRT |Lz|>2 at 98% 被解读为 conditioning variable (total score) 根本不适合 MMLU——
      MH 依赖 total score 做 ability matching，但 57-subject multidimensional structure 使
      total score 成为 poor proxy，整个 DIF 分析的 conditioning 基础被质疑。
      random split 0.18% 只证明 temporal signal 存在，不证明 signal = instability。
    tables:
      - title: "Table 1: DIF Classification by Cohort Definition"
        columns: [cohort, n_ref, n_foc, pct_A, pct_B, pct_C, enrichment_li]
        rows:
          - [temporal_2023v2024, 1253, 656, 48.2, 20.5, 31.3, 0.96]
          - [ability_quintile, 1044, 1044, 89.8, 7.3, 2.9, 1.19]
          - [random_split_control, 950, 950, 97.3, 2.5, 0.18, 1.01]
      - title: "Table 2: Within-Family DIF (Confound Control)"
        columns: [family_pair, n_ref, n_foc, pct_C, interpretation]
        rows:
          - [Llama-2_vs_Llama-3, 161, 308, 61.3, "generation gap drives DIF"]
          - [Mistral_vs_Mixtral, 89, 142, 38.7, "architecture shift contributes"]
    figures_description:
      - "Fig 1: Domain-level C% vs accuracy improvement scatter (ρ=0.38, p=0.004)。Reviewer 会标注 regression line 并论证正相关说明 DIF tracks capability gain。"
      - "Fig 2: |Lz| distribution — 98% above 2.0 的 histogram，作为 IRT misfit 的 visual evidence。"
    analysis: >
      Worst-tier reviewer 的核心论证链：domain ρ=0.38 → within-family 61% → enrichment≈1.0 →
      IRT 98% misfit → 结论是 "DIF 在 MMLU 上不是 item instability detector，而是 capability gap detector，
      你的 31% 就是在说 models got better on 31% of items"。这个攻击路径在逻辑上是 self-consistent 的，
      即使 item-level decomposition 只解释 2.4pp——reviewer 会说 domain-level predictor 是 wrong granularity，
      真正的 confound 是 item-level difficulty × model generation interaction。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: "DIF 对 RL 训练模型的鲁棒性验证：alignment-RL (DPO/ORPO, N=477) + reasoning-RL (GRPO/PPO, N=10-15)"
    expected_results:
      alignment_rl_cohort_c_pct: 29.8
      alignment_rl_jaccard_vs_temporal: 0.72
      reasoning_rl_n_models: 13
      reasoning_rl_added_to_focal_c_pct: 30.5
      reasoning_rl_jaccard_vs_base_focal: 0.85
      delong_p_dif_vs_constat: 0.23
      delong_p_dif_vs_mink: 0.18
      tost_equivalence_p: 0.08
      constat_auroc_non_rl: 0.74
      constat_auroc_rl: 0.68
      mink_auroc_non_rl: 0.71
      mink_auroc_rl: 0.63
      dif_auroc_across_compositions: 0.61
      partial_exploitation_detection_boundary_p: 0.55
      bootstrap_ci_width_auroc: 0.15
    result_rationale: >
      Worst 档下此实验有两个致命问题：
      (1) N=13 reasoning-RL models 使所有统计检验 underpowered——DeLong test p=0.23 和 TOST p=0.08
      都不显著，reviewer 正确指出 "你无法区分 DIF 对 RL 鲁棒 vs 你没有足够样本检测差异"；
      (2) DIF AUROC=0.61 本身就低——reviewer 论证 MH-DIF 在 any cohort composition 下
      detection power 都不 competitive，不是 RL-robust 而是 uniformly weak；
      (3) ConStat 和 Min-K% 在 RL 上的 degradation (0.74→0.68, 0.71→0.63) 比预期温和，
      不足以构成 "traditional methods fail on RL" 的 strong claim。
      Bootstrap CI width=0.15 在 13 个模型上是预期内的，但 reviewer 会说这个宽度下任何 claim 都是 preliminary。
    tables:
      - title: "Table: Detection AUROC by Method × Model Type"
        columns: [method, non_rl_auroc, alignment_rl_auroc, reasoning_rl_auroc, delta]
        rows:
          - [MH-DIF, 0.62, 0.61, 0.60, -0.02]
          - [ConStat, 0.74, 0.71, 0.68, -0.06]
          - [Min-K%, 0.71, 0.69, 0.63, -0.08]
    figures_description:
      - "Fig: Power curve — DIF detection TPR vs exploitation rate p ∈ [0.4, 1.0]，标注 detection boundary at p=0.55。Reviewer 会指出 boundary 太高——half the contaminated items need to be exploited before detection kicks in。"
    analysis: >
      在 worst 档 reframing 中，此实验被降级甚至 drop。N=13 的 RL 验证无法支撑任何 robust claim。
      如果 reviewer 看到 DIF AUROC=0.61 且 bootstrap CI=[0.54, 0.76]，会质疑 "为什么要用 detection power
      这么低的方法"。Reframed paper 中应将此实验移入 appendix 作为 preliminary evidence，
      或完全 drop 并在 limitations 中说明。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: "ConStat-style perturbation testing 在 MMLU 上的独立评估：200+ items LLM paraphrasing + FDR-controlled detection"
    expected_results:
      n_items_reformulated: 220
      constat_fdr_controlled_detections: 45
      constat_detection_rate: 0.205
      constat_fpr_estimate: 0.08
      constat_auroc_non_rl: 0.74
      constat_auroc_rl: 0.68
      constat_dif_overlap_jaccard: 0.15
      paraphrase_quality_score: 0.82
    result_rationale: >
      Worst 档下，ConStat detection rate=20.5% 在 non-RL 模型上是 reasonable baseline，
      但 DIF-ConStat overlap Jaccard=0.15 极低——reviewer 论证两种方法在测不同的东西，
      ensemble 前提不成立。ConStat 的 AUROC=0.74 > DIF 的 0.62，reviewer 会问
      "既然 ConStat 更准，为什么不直接用 ConStat？DIF 的 added value 在哪里？"
      更致命的是，ConStat 在 RL 上只 degradation 6pp (0.74→0.68)，
      不够 dramatic 来支撑 "traditional methods fail on RL" 的 narrative。
    tables: []
    figures_description:
      - "Fig: Venn diagram of DIF-C flags vs ConStat detections，Jaccard=0.15 的极低 overlap 被 reviewer 用来论证两种方法在测完全不同的 construct。"
    analysis: >
      此实验在 worst 档的 reframed paper 中价值有限。如果 DIF 被降级为 case study，
      ConStat comparison 也失去 anchor。可以保留为 "related methods comparison" 但不再是核心 contribution。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: "DVD generation variance 在 MMLU 上的独立评估：10-15 open-weight models × 50 responses/item"
    expected_results:
      n_models_evaluated: 12
      n_items_scored: 1200
      dvd_bimodal_detection_rate: 0.12
      dvd_auroc: 0.65
      dvd_dif_overlap_jaccard: 0.11
      dvd_constat_overlap_jaccard: 0.22
      verbatim_vs_variant_dvd_gap: 0.18
    result_rationale: >
      DVD detection rate=12% 低于 ConStat 的 20.5%，AUROC=0.65 处于 poor-to-fair 区间。
      DVD-DIF overlap Jaccard=0.11 甚至低于 ConStat-DIF 的 0.15——三种方法之间的 agreement
      极低，reviewer 论证 "这些方法在测量三个不同的东西，没有一个是 validated contamination signal"。
      N=12 模型的 generation variance 采样也不足以覆盖 model diversity。
      在 worst 档下，DVD 的弱结果进一步削弱了 ensemble 的 rationale。
    tables: []
    figures_description: []
    analysis: >
      DVD 在 worst 档下是 net negative——弱结果被 reviewer 用来论证 contamination detection
      整个 paradigm 的 fragility。建议在 reframed paper 中 drop 此实验。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: "DIF + ConStat + DVD 三信号融合：calibrated thresholds + 2-of-3 voting + weighted fusion"
    expected_results:
      ensemble_2of3_coverage: 0.38
      ensemble_2of3_fpr: 0.12
      ensemble_weighted_auroc: 0.72
      ensemble_vs_best_single_auroc_gain: -0.02
      cross_val_weight_stability_cv: 0.35
      uniform_vs_optimized_auroc_gap: 0.03
    result_rationale: >
      Worst 档下 ensemble 的核心问题是 base signal quality 太低。三种方法 pairwise Jaccard
      全部 <0.25，2-of-3 voting 的 agreement 稀少导致 coverage=38% 但 FPR=12% (超过 0.10 target)。
      weighted fusion AUROC=0.72 竟然低于 ConStat standalone 的 0.74——ensemble 反而 hurt performance。
      cross-validation weight stability CV=0.35 表明 weights 在 fold 间不稳定，reviewer 正确指出
      "你的 ensemble 在 overfitting fold-specific patterns"。
      这个实验在 original framing (Claim 2: ensemble detection) 下是 fatal negative，
      是 paper framing pivot 的直接原因之一。
    tables:
      - title: "Table: Ensemble vs Individual Signal Performance"
        columns: [method, auroc, fpr_at_80recall, coverage]
        rows:
          - [DIF (MH), 0.62, 0.38, 0.31]
          - [ConStat, 0.74, 0.12, 0.21]
          - [DVD, 0.65, 0.28, 0.12]
          - [Ensemble (2-of-3), 0.68, 0.12, 0.38]
          - [Ensemble (weighted), 0.72, 0.11, 0.42]
    figures_description: []
    analysis: >
      Ensemble 在 worst 档下是 paper 的最大 sunk cost。三信号 low-agreement + ensemble ≤ best single
      = reviewer 一句话 kill："the whole is less than its parts"。Reframed paper 必须完全 drop
      Claim 2 (ensemble)，将 plan_003a/b/c 全部移入 "future work"。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: "GSM8K 上的 DIF 复制 + GSM1K ground truth correlation + semi-synthetic validation"
    expected_results:
      gsm8k_temporal_c_pct: 18.9
      gsm8k_external_c_pct: 47.4
      gsm8k_sanity_c_pct: 0.3
      semi_synthetic_delta_tpr_p10: 0.818
      semi_synthetic_delta_tpr_p05: 0.42
      gsm1k_n_models: 33
      gsm1k_pearson_r: -0.478
      gsm1k_spearman_rho: -0.403
      gsm1k_direction: NEGATIVE
      gsm1k_partial_r: -0.385
      gsm1k_permutation_p: 0.014
      gsm1k_ci_upper_r: -0.16
      gsm1k_ci_upper_rho: -0.03
    result_rationale: >
      Worst 档下此实验有一个 devastating result：GSM1K correlation 方向是 NEGATIVE (r=-0.478)——
      DIF-C items 与 contamination gap 反相关。Reviewer 的解读："DIF 标记的 items 恰恰是
      2024 模型 genuinely improved 的 items（不需要 contamination），而真正 contaminated 的
      items 不被 DIF 检测到，因为 contamination 是 uniform across cohorts"。
      这直接支持了 worst 档的核心假设——DIF 在测 'models got better' 而非 contamination。
      N=33 虽小但方向一致 (permutation p=0.014)，CI upper bound |r|=0.16 也远离 positive territory。
      Semi-synthetic ΔTPR=0.42 at p=0.5 落在 worst 档范围 [0.3, 0.5] 内，被视为 "moderate
      但不 compelling"——p=0.5 意味着一半 contaminated models 必须 exploit item 才能检测到。
    tables:
      - title: "Table: GSM1K Contamination Gap vs DIF Flag Correlation"
        columns: [metric, value, ci_lower, ci_upper, p_value]
        rows:
          - [pearson_r, -0.478, -0.71, -0.16, 0.005]
          - [spearman_rho, -0.403, -0.67, -0.03, 0.020]
          - [partial_r_controlling_acc, -0.385, -0.65, -0.04, 0.027]
    figures_description:
      - "Fig: Scatter plot of per-model DIF-C item accuracy vs GSM1K gap，negative slope。Reviewer 会把这张图作为 'DIF ≠ contamination' 的 smoking gun。"
    analysis: >
      GSM1K negative correlation 是 worst 档最有力的 ammunition。在 reframed paper 中必须
      将此结果 reinterpret 为 "DIF and contamination measure orthogonal constructs"——
      这 actually supports Claim 2 (ground truth meta-critique) 而不是 undermines it。
      Key reframing: "DIF measures differential item functioning, not contamination per se.
      The negative GSM1K correlation confirms that item-level behavioral change ≠ contamination signal,
      validating our meta-critique that web-overlap labels are fundamentally mismatched."

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: "MMLU bifactor IRT 模型拟合 + anchor item 选择 + fixed-parameter calibration equating pilot"
    expected_results:
      bifactor_convergence: false
      bifactor_rmsea: 0.089
      bifactor_cfi: 0.72
      bifactor_tli: 0.68
      bifactor_srmr: 0.11
      general_factor_explained_variance_pct: 28.4
      n_anchor_items_selected: 0
      equating_feasible: false
      computation_time_hours: 18.5
      convergence_code: "iteration limit reached"
    result_rationale: >
      Worst 档下 bifactor 模型 fails to converge on 12,508 × 5,219 矩阵。
      即使强制截断 iterations，fit indices 全部不达标 (RMSEA=0.089 > 0.06 cutoff,
      CFI=0.72 < 0.90 cutoff, TLI=0.68)。General factor 仅解释 28.4% variance，
      说明 MMLU 的 57-subject structure 导致 essentially 无法用 single general factor 建模。
      这直接验证了 reviewer 的 IRT misfit concern——不只是 |Lz| 的问题，连 bifactor 都 fail，
      说明 MMLU 在 IRT 框架下 fundamentally ill-behaved。
      结果：equating pipeline 被 kill，anchor items 无法选择，plan_006 (item generation) 也被 block。
      这个 negative result 在 reframed paper 中反而有价值——motivates future multidimensional IRT work。
    tables: []
    figures_description:
      - "Fig: Scree plot showing 57 eigenvalues with no dominant first factor — visual evidence of MMLU's irreducible multidimensionality。"
    analysis: >
      Bifactor failure 是 plan_005/006/008 整条 pipeline 的 kill signal。在 reframed paper 中
      列入 limitations："IRT-based equating requires adequate model fit; MMLU's 57-subject
      multidimensional structure defeats both unidimensional and bifactor specifications.
      This motivates future work on multidimensional IRT or subject-specific calibration."

  - name: item_generation_calibration
    plan_id: plan_006
    description: "DIF-flagged MMLU items 的 LLM 替换生成 + student simulation calibration"
    expected_results:
      n_items_generated: 0
      difficulty_correlation_prompt: null
      difficulty_correlation_simulation: null
      calibration_feasible: false
      blocked_by: plan_005_bifactor_failure
    result_rationale: >
      Worst 档下此实验被 plan_005 failure 完全 block。没有可靠的 IRT 参数估计和 anchor items，
      生成的替换 items 无法 calibrate 到 equated scale 上。即使独立运行 prompt-based generation，
      已有文献 (arXiv 2602.06631) 表明 difficulty correlation 仅 ρ=0.10-0.45，
      而 student simulation 需要先有 IRT 参数才能 simulate——circular dependency。
      整个 regeneration pipeline (original Claim 3) 被 kill，是 paper pivot 的主要 driver 之一。
    tables: []
    figures_description: []
    analysis: >
      Not executed。在 reframed paper 中完全 drop，不出现在 main body 或 appendix。
      Original Claim 3 (regeneration) 已被 bifactor failure 否定。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: "Sinharay et al. (2006) cumulative Bayesian DIF priors 的 simulation study：4 successive administrations"
    expected_results:
      individual_admin_tpr_delta10: 0.42
      cumulative_2admin_tpr: 0.55
      cumulative_3admin_tpr: 0.63
      cumulative_4admin_tpr: 0.68
      target_tpr_070: false
      individual_admin_tpr_delta14: 0.58
      fpr_all_below_010: true
      prior_sensitivity_max_tpr_swing: 0.09
    result_rationale: >
      Worst 档下 cumulative power improvement 存在但低于 target：3-admin 后 TPR=0.63 < 0.70 target，
      4-admin 才到 0.68。Reviewer 批评这是 pure simulation："你没有 4 个 time period 的真实数据，
      这只是说 'if we had more data, DIF would work better'——tautological。"
      更关键的是，simulation 使用 well-specified 1D IRT model，而真实 MMLU 的 IRT misfit (98%)
      意味着 simulation results 不 transferable。"你在模拟一个你已经证明不存在的世界。"
    tables:
      - title: "Table: Cumulative DIF Power by Number of Administrations"
        columns: [n_admin, delta_10_tpr, delta_14_tpr, delta_16_tpr, fpr]
        rows:
          - [1, 0.42, 0.58, 0.68, 0.04]
          - [2, 0.55, 0.71, 0.79, 0.05]
          - [3, 0.63, 0.78, 0.85, 0.05]
          - [4, 0.68, 0.83, 0.89, 0.06]
    figures_description: []
    analysis: >
      Simulation-only + IRT misfit = reviewer 完全 dismiss。在 reframed paper 中移入 appendix
      或 drop。Methodology track reviewer 可能 appreciate the framework 但会要求 real data validation。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: "Benchmark validity degradation under progressive item replacement (5%–50%)"
    expected_results:
      replacement_5pct_rho: 0.999
      replacement_10pct_rho: 0.998
      replacement_20pct_rho: 0.996
      replacement_50pct_rho: 0.988
      replacement_5pct_shr: 0.993
      replacement_10pct_shr: 0.991
      replacement_20pct_shr: 0.987
      replacement_50pct_shr: 0.972
      construct_coverage_maintained_at_20pct: true
      blocked_by_equating: true
    result_rationale: >
      Worst 档下此实验 partially blocked by plan_005 failure (无法用 equated replacement items)。
      可以用 random replacement 做 simulation，结果显示极高 robustness (ρ>0.988 even at 50% replacement)。
      但 reviewer 将此解读为 MMLU 的 massive redundancy 的进一步证据：
      "你可以 drop 一半的 items 且 ranking 不变——这说明 MMLU 有 6000+ redundant items，
      你的 31% DIF finding 完全在 redundancy margin 内，没有任何实际影响。"
      讽刺的是，robustness 越高，DIF findings 的 practical significance 越低。
    tables:
      - title: "Table: Ranking Stability Under Progressive Item Replacement"
        columns: [replacement_pct, spearman_rho, shr, construct_coverage_ratio]
        rows:
          - [5, 0.999, 0.993, 0.98]
          - [10, 0.998, 0.991, 0.96]
          - [20, 0.996, 0.987, 0.93]
          - [50, 0.988, 0.972, 0.85]
    figures_description:
      - "Fig: Degradation curve — ρ vs replacement % 几乎是 flat line until 50%。Reviewer 用此图论证 'DIF findings are practically irrelevant'。"
    analysis: >
      在 reframed paper 中，graceful degradation 反而支持 revised narrative：
      "MMLU's massive redundancy means DIF-flagged items can be safely removed without
      validity loss — the diagnostic value of DIF is in understanding WHAT changed,
      not in removing items for quality control。" 但 worst 档 reviewer 会说
      "如果 removal 没有影响，你的 whole paper 的 motivation 就不成立。"

  - name: item_focused_trees
    plan_id: plan_009
    description: "Item-Focused Trees (Tutz & Berger 2016) 作为 continuous-covariate DIF 替代方案"
    expected_results:
      ift_n_items_dif: 3452
      ift_c_pct_equivalent: 27.6
      ift_mh_concordance: 0.78
      ift_split_point_median_date: "2023-09"
      ift_gradual_items_pct: 62.3
      ift_abrupt_items_pct: 37.7
      ift_computation_time_hours: 8.2
    result_rationale: >
      Worst 档下 IFT 的 continuous treatment 暴露了 temporal DIF 的 gradual nature：
      62.3% 的 DIF items 显示 gradual difficulty drift 而非 abrupt change。
      Reviewer 用此论证 "这是 models gradually getting better on certain items，
      不是 contamination event 或 structural instability——difficulty drift 是 capability
      improvement 的自然结果，你的 binary 2023/2024 split 人为制造了 abrupt 的假象。"
      Split point median at 2023-09 也不 informative——没有对应任何 specific model release event。
      IFT-MH concordance=0.78 表明 MH 的 binary grouping 丢失了 22% 的 nuance。
    tables:
      - title: "Table: IFT vs MH-DIF Classification Comparison"
        columns: [metric, MH_DIF, IFT, concordance]
        rows:
          - [n_flagged_items, 3918, 3452, 0.78]
          - [pct_C_equivalent, 31.3, 27.6, "-"]
          - [gradual_vs_abrupt, "N/A (binary)", "62.3% / 37.7%", "-"]
    figures_description:
      - "Fig: Item difficulty trajectories for 20 representative DIF items showing gradual monotonic drift — reviewer 用此 visual 论证 'this is just learning curves, not instability'。"
    analysis: >
      IFT 在 worst 档下是 double-edged sword：提供了 finer-grained picture 但 picture 说的是
      "gradual improvement" 而非 "instability"。Reframed paper 中可以保留为 robustness check
      并 reframe："IFT confirms that item-level behavioral changes are predominantly gradual,
      consistent with progressive capability development rather than discrete contamination events。"

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: "Decoder-only 子群上的 DIF 分析 + IRT fit diagnostics"
    expected_results:
      n_decoder_only: 5226
      n_non_decoder: 1
      pct_decoder_only: 99.98
      decoder_only_c_pct: 31.3
      decoder_only_jaccard_vs_full: 1.0
      irt_rmsea_full: 0.082
      irt_rmsea_decoder_only: 0.081
      irt_cfi_full: 0.74
      irt_cfi_decoder_only: 0.74
      irt_lz_above_2_pct_decoder_only: 97.8
    result_rationale: >
      Worst 档下此实验 trivially resolves architecture concern (99.98% decoder-only,
      removing 1 model changes nothing, Jaccard=1.0) 但 completely fails to address
      IRT misfit。RMSEA 从 0.082→0.081, CFI unchanged at 0.74——IRT misfit 不是
      architecture heterogeneity 造成的，而是 MMLU 57-subject multidimensionality 造成的。
      Reviewer："你证明了 architecture 不是问题，但 IRT misfit 依然是 98%——
      移除 1 个 encoder model 不可能解决 57-subject 的 multidimensionality 问题。
      你需要的是 multidimensional IRT 或 per-subject analysis，不是 architecture stratification。"
    tables:
      - title: "Table: IRT Fit Diagnostics — Full vs Decoder-Only"
        columns: [population, N, RMSEA, CFI, TLI, pct_Lz_above_2]
        rows:
          - [full, 5227, 0.082, 0.74, 0.71, 98.0]
          - [decoder_only, 5226, 0.081, 0.74, 0.71, 97.8]
    figures_description: []
    analysis: >
      此实验在 worst 档下是 necessary but trivially resolved。不提供任何 defense against
      IRT misfit concern。在 reframed paper 中一句话带过："99.98% of METABENCH models are
      decoder-only; architecture heterogeneity is a non-issue (Jaccard=1.0)"。
      IRT misfit 需要在 limitations 中 honestly address 而非 dismiss。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: "Known contamination injection into METABENCH matrix + DIF detection power measurement"
    expected_results:
      temporal_external_tpr_p0: 0.326
      temporal_external_tpr_p03: 0.45
      temporal_external_tpr_p05: 0.42
      temporal_external_tpr_p07: 0.78
      temporal_external_tpr_p10: 0.95
      temporal_external_fpr: 0.314
      temporal_external_delta_tpr_p05: 0.35
      temporal_external_delta_tpr_p10: 0.62
      cross_subject_delta_fpr: 0.000
      within_subject_fpr_inflation: 0.186
      ability_external_delta_tpr_p10: 0.302
      standard_mh_fpr_inflation_at_p10: 0.318
    result_rationale: >
      Worst 档下 semi-synthetic 的 ΔTPR at p=0.5 = 0.35，落在 worst 范围 [0.3, 0.5] 下半区。
      Reviewer 的攻击：
      (1) "ΔTPR=0.35 at p=0.5 意味着在 half exploitation 下你只比 baseline 多检测 35% 的
      contaminated items——这在 practical terms 下意味着你漏掉了大部分 contamination"；
      (2) "Baseline FPR=0.314 意味着你的 detector 在没有 injection 时已经 flag 31.4% 的 items
      作为 positive——这要么是 FPR 不可接受，要么是你的 'clean' items 并不 clean，
      无论哪种解读都 undermine 你的 validation"；
      (3) "Cross-subject matching 的 ΔFPR=0.000 是 technically impressive 但 semantically
      questionable——你用 other subjects 的 score 做 matching variable，这意味着你在用
      math ability 来 match science items，matching variable 和 target variable 的 construct
      relevance 未验证"。
      但在 reframed paper 中，这个实验反而是最 defensible 的——reviewer 攻击的是
      interpretation 而非 methodology，cross-subject matching ΔFPR=0.000 是 hard empirical fact。
    tables:
      - title: "Table: Semi-Synthetic Validation — DIF Detection Power"
        columns: [exploitation_rate_p, tpr, delta_tpr, fpr, delta_fpr]
        rows:
          - [0.0, 0.326, 0.000, 0.314, 0.000]
          - [0.3, 0.450, 0.124, 0.314, 0.000]
          - [0.5, 0.676, 0.350, 0.314, 0.000]
          - [0.7, 0.780, 0.454, 0.314, 0.000]
          - [1.0, 0.950, 0.624, 0.314, 0.000]
    figures_description:
      - "Fig: Dose-response curve — ΔTPR vs exploitation rate p，cross-subject matching (ΔFPR=0.000) vs within-subject matching (FPR inflation)。这是 reframed paper 的 centerpiece figure。"
    analysis: >
      Semi-synthetic validation 是 worst 档 reframing 的 primary contribution。
      虽然 ΔTPR=0.35 at p=0.5 不 impressive，但 (1) cross-subject ΔFPR=0.000 是 novel
      methodological contribution，(2) dose-response monotonicity 证明 framework 有效，
      (3) within vs cross matching comparison 是 actionable guidance。
      Reframed paper 应强调 framework reusability 而非 specific detection performance。

  - name: multi_benchmark_temporal_dif
    plan_id: plan_028
    description: "6 个 benchmark (MMLU/ARC/HellaSwag/WinoGrande/TruthfulQA/GSM8K) 上的 temporal DIF 分析"
    expected_results:
      mmlu_c_pct: 31.3
      winogrande_c_pct: 30.3
      truthfulqa_c_pct: 29.7
      arc_c_pct: 26.9
      gsm8k_c_pct: 18.9
      hellaswag_c_pct: 17.9
      cross_benchmark_range: "17.9-31.3%"
      all_random_controls_below_1pct: true
      min_enrichment_ratio: 45
      n_benchmarks: 6
      cross_benchmark_mean_c_pct: 25.8
      cross_benchmark_sd_c_pct: 5.8
    result_rationale: >
      Worst 档下 6-benchmark consistency (C%=17.9-31.3%, all >45× above random) 被 reviewer
      反转利用。核心论证："所有 6 个 benchmark 都显示 high DIF 恰恰证明这是 method artifact，
      不是 benchmark-specific instability。如果 DIF 在测 item instability，不同 benchmark
      应该有不同的 instability profile——HellaSwag (commonsense) 和 GSM8K (math) 的 instability
      机制完全不同。但 C% 的 cross-benchmark consistency (mean=25.8%, SD=5.8%) 说明
      DIF 在 uniformly 捕捉 'temporal cohort difference' 的 statistical signal，
      而这个 signal 就是 'models got better'。"
      更具体地：HellaSwag 和 GSM8K 的 C% 较低 (17.9%, 18.9%) 恰好是 capability improvement
      最 saturated 的 benchmarks (HellaSwag accuracy >90%, GSM8K has clear skill ceiling)，
      而 MMLU (31.3%) 和 WinoGrande (30.3%) 的 C% 较高恰好是 improvement space 最大的 benchmarks。
      这个 pattern 与 "DIF = capability improvement" 假说 perfectly consistent。
    tables:
      - title: "Table: Cross-Benchmark Temporal DIF Summary"
        columns: [benchmark, n_items, n_ref, n_foc, pct_C, random_pct_C, enrichment_ratio]
        rows:
          - [MMLU, 12508, 1080, 807, 31.3, 0.18, 174]
          - [WinoGrande, 1267, 1017, 803, 30.3, 0.32, 95]
          - [TruthfulQA, 817, 1080, 807, 29.7, 0.37, 80]
          - [ARC-Challenge, 1172, 1080, 807, 26.9, 0.60, 45]
          - [GSM8K, 1319, 1017, 804, 18.9, 0.30, 63]
          - [HellaSwag, 10042, 1080, 807, 17.9, 0.28, 64]
    figures_description:
      - "Fig: Bar chart of C% across 6 benchmarks with random control overlay。Reviewer 会标注 'all bars above 15% — uniform artifact' annotation。"
      - "Fig: C% vs benchmark mean accuracy (2024 cohort)，negative correlation 暗示 saturation effect。"
    analysis: >
      Cross-benchmark 一致性在 worst 档下是 double-edged sword。在 original framing 下
      支持 generalizability；在 worst 档下被解读为 method artifact。
      Reframed paper 中应 reinterpret："Cross-benchmark consistency confirms that temporal
      cohort design reliably detects DIF across diverse benchmarks, whether the signal
      represents item instability, capability improvement, or both. Our semi-synthetic
      framework can disambiguate this — we demonstrate this on MMLU and GSM8K。"

  - name: permutation_null_c_rate
    plan_id: plan_029
    description: "1000× permutation test：randomly reassign temporal labels → MH-DIF → null C% distribution"
    expected_results:
      n_permutations: 1000
      null_c_pct_mean: 0.22
      null_c_pct_sd: 0.08
      null_c_pct_95th: 0.38
      null_c_pct_99th: 0.48
      observed_c_pct: 31.3
      permutation_p: "<0.001"
      effect_size_z: 388.5
      null_matches_random_split: true
    result_rationale: >
      Worst 档下 permutation null C%=0.22% (SD=0.08%)，observed 31.3% 极显著高于 null
      (z=388, p<0.001)。但 reviewer 的反应不是 "impressive" 而是 "so what"：
      "当然 31.3% above chance——你在比较 2023 vs 2024 models，它们 obviously different。
      任何 test 都会 reject the null that these groups are exchangeable。
      这个 permutation test 只证明 temporal signal exists，不证明 signal = item instability
      而非 capability improvement。你需要的不是 'is 31% above chance' 而是 'is 31% above
      what capability improvement alone would produce'——而后者正是你的 decomposition analysis
      (plan_019) 和 matching analysis (plan_027) 试图回答但未完全回答的问题。"
      Permutation null ≈ random split control (0.18% vs 0.22%)，consistent，
      但这个 consistency 也只是说明两种 null 都 measure the same thing (label exchangeability)。
    tables:
      - title: "Table: Permutation Null Distribution Summary"
        columns: [statistic, value]
        rows:
          - [observed_C_pct, 31.3]
          - [null_mean, 0.22]
          - [null_SD, 0.08]
          - [null_95th_percentile, 0.38]
          - [z_score, 388.5]
          - [permutation_p, "<0.001"]
          - [random_split_control, 0.18]
    figures_description:
      - "Fig: Null C% distribution histogram (1000 permutations) with observed 31.3% marked as extreme outlier。Visually compelling 但 reviewer 会 annotate 'proves temporal signal, not item instability'。"
    analysis: >
      Permutation test 在 worst 档下 necessary but not sufficient。Establishes that
      temporal labels carry real signal (not random)，但 signal identity 仍 contested。
      在 reframed paper 中保留为 one-paragraph validation：
      "Permutation test confirms C%=31.3% is not a statistical artifact of the MH procedure
      (null: 0.22±0.08%, p<0.001)。Decomposition of the temporal signal into item-level
      vs cohort-level components is addressed by plan_019 and plan_027。"

  - name: odds_ratio_regression_transparency
    plan_id: plan_030
    description: "DIF flag 的 odds ratio regression：domain-level → item-level predictors + Simpson's paradox 分析"
    expected_results:
      model1_mcfadden_r2: 0.0007
      model1_nagelkerke_r2: 0.0012
      model1_subject_acc_delta_or_per_010: 1.55
      model1_subject_acc_delta_ci: [1.19, 2.03]
      model2_mcfadden_r2: 0.0423
      model2_subject_acc_delta_or_per_010: 0.73
      model2_ctt_difficulty_or: 0.78
      model2_discrimination_or: 1.51
      model3_item_delta_or_per_010: 1.08
      model3_mcfadden_r2: 0.0012
      model4_mcfadden_r2: 0.0434
      model4_item_acc_change_or: 0.92
      model4_discrimination_or: 1.54
      simpsons_paradox: true
      simpsons_or_flip: "1.55 → 0.73"
      lr_test_m1_vs_m2_chi2: 646.98
      lr_test_m3_vs_m4_chi2: 655.53
    result_rationale: >
      Worst 档下 Simpson's paradox (OR 1.55→0.73) 被 reviewer 反转利用。
      核心论证：Model 1 (domain accuracy delta only) 显示 OR=1.55——domain 进步越大，DIF 越多，
      看似支持 "DIF tracks capability improvement"。但加入 item-level properties (difficulty,
      discrimination) 后 OR flips to 0.73——controlling for item properties，domain improvement
      REDUCES DIF probability。
      Reviewer 的解读："Simpson's paradox 证明 item-level properties (difficulty, discrimination)
      才是 DIF 的 true driver，domain improvement 只是 ecological confound。
      你的 DIF 方法在挑出 high-discrimination, moderate-difficulty items——这些恰好是
      区分好模型和差模型的 items，它们 'show DIF' 不是因为 instability 而是因为它们
      discriminate well，而 2024 models 恰好比 2023 models 好。"
      Discrimination OR=1.51-1.54 across all models 是最 consistent predictor——
      higher discrimination → more likely DIF。这直接支持了 worst 档的核心假设：
      DIF 在 measure 'items that separate good from bad models' 即 'models got better'。
      McFadden R²=0.043 虽然 low in absolute terms，但 Model 1→Model 2 的 LR test χ²=647
      (p≈0) 说明 item properties 是 massively significant predictors。
    tables:
      - title: "Table: Logistic Regression Models Predicting DIF-C Classification"
        columns: [model, predictors, mcfadden_r2, nagelkerke_r2, aic, key_or]
        rows:
          - [M1, "subject_acc_Δ", 0.0007, 0.0012, 15545, "1.55 [1.19,2.03]"]
          - [M2, "subject_acc_Δ + difficulty + discrimination", 0.0423, 0.072, 14902, "0.73 (acc_Δ), 1.51 (disc)"]
          - [M3, "item_acc_Δ", 0.0012, 0.0021, 15537, "1.08 [1.03,1.14]"]
          - [M4, "item_acc_Δ + difficulty + discrimination", 0.0434, 0.074, 14885, "0.92 (acc_Δ), 1.54 (disc)"]
      - title: "Table: Simpson's Paradox — OR Flip Summary"
        columns: [predictor, model1_or, model2_or, direction_flip, interpretation]
        rows:
          - ["Domain acc Δ (per 0.10)", 1.55, 0.73, "positive→negative", "confounded by item properties"]
          - ["Item acc Δ (per 0.10)", 1.08, 0.92, "positive→negative", "confounded by item properties"]
          - ["CTT discrimination (per 0.10)", "-", 1.51, "consistent positive", "true driver"]
    figures_description:
      - "Fig: Forest plot of ORs across 4 models — visual display of Simpson's paradox flip。Reviewer 会用此图作为 'DIF = discrimination artifact' 的 key evidence。"
      - "Fig: Partial dependence plot — DIF probability vs discrimination，showing monotonic increase。"
    analysis: >
      Simpson's paradox 在 worst 档下是 most damaging single result。Reviewer 论证链：
      discrimination drives DIF → high-discrimination items separate cohorts →
      2024 cohort is better → DIF flags items where 2024 models outperform 2023 models
      BECAUSE those items have high discrimination → "DIF is measuring item quality, not instability"。
      在 reframed paper 中需要 carefully reinterpret：
      "The OR flip reveals that item-level properties, particularly discrimination,
      are the proximal predictors of DIF classification. This is psychometrically expected:
      high-discrimination items magnify any ability difference between groups, producing
      larger MH odds ratio shifts. The question is whether this represents (a) genuine
      item instability amplified by discrimination, or (b) stable items faithfully
      discriminating between cohorts of different ability. Our decomposition evidence
      (ability confound ≤2.4pp, plan_027) supports interpretation (a), but we acknowledge
      this remains the central interpretive challenge。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2aa85f1-ca49-4c05-ae43-2249caf9eb9e",
  "isSidechain": false,
  "requestId": "req_011CbFdTuMfPUyoVnqXc8ua3",
  "type": "assistant",
  "uuid": "a963fa9a-c1f2-49c5-be18-f83864657c7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GABwavEqKkaCoXid4ih8cw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21197,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14884,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21197,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14884,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21197
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Temporal coarseness 被视为 fatal flaw（binary 2023/2024 conflates release timing, training data cutoff, architecture shifts），且 IRT misfit (98%) 被解读为 MH 结果不可信。…",
  "leafUuid": "a963fa9a-c1f2-49c5-be18-f83864657c7e",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Semi-synthetic validation framework for item-level contamination detection",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Temporal coarseness 被视为 fatal flaw（binary 2023/2024 conflates release timing, training data cutoff, architecture shifts），且 IRT misfit (98%) 被解读为 MH 结果不可信。…",
  "leafUuid": "a963fa9a-c1f2-49c5-be18-f83864657c7e",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Semi-synthetic validation framework for item-level contamination detection",
  "sessionId": "70c7d4b0-5ee0-486b-87d8-4697f59a1249"
}
```

---
