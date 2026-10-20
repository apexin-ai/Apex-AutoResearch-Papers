# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：novelty 被拒；IRT misspecification 被视为根本性缺陷（'misspecified model → all findings

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/90866091-0b36-4c98-a56f-c14ff188e010.jsonl`
- **Structured JSON:** [`299fd3e435b6e3094dad.json`](../../sessions/29/299fd3e435b6e3094dad.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T06:34:42.435Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T06:34:42.435Z",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：novelty 被拒；IRT misspecification 被视为根本性缺陷（'misspecified model → all findings suspect'）；需要找新 angle reframe\n核心假设：[\"A1 不成立：majority 评审判定 'applying textbook MH-DIF without modification = insufficient novelty for ICLR'，即使 scale 大\", 'A2 不成立：评审认为 98% |Lz|>2 意味着 1D IRT ability estimates 不可靠 → MH 的 ability matching 本身有系统偏差 → 31% C% 可能是 model misfit artifact', \"A3 不成立：ρ≈0.997 被解读为 'DIF flags are noise that doesn't matter'，而非 redundancy revelation\", \"A4 不成立：meta-critique 被视为 'trivially true observation, not a contribution'\", 'A5 部分成立：item characterization 数据本身有趣但不足以撑全文', 'A6 不成立：GSM1K 被 dismiss']\n关键指标范围：{'reviewer_avg_score': [3.0, 4.5], 'acceptance_probability_pct': [2, 15], 'claims_at_full_strength': [0, 1], 'novelty_sub_score_avg': [1.0, 2.0], 'reviewers_flagging_irt_as_fatal': [2, 4], 'major_revisions_needed': [4, 5]}\n叙事方向：核心假设失败，但数据资产（5,227×12,508 response matrix + 全部实验结果）仍在， 需要找新 angle 仍冲 ICLR 2027。三条 reframe 路径——\n路径 A \"Framework-first\"：将 semi-synthetic ΔTPR framework（Claim 3）提升为 第一贡献，paper 变成 methodology paper。Title 类似 \"A Semi-Synthetic Framework for Validating Item-Level Contamination Detectors\"。31% temporal instability 降为 case study / application section。此路径的 novelty 来自 cross-subject matching (ΔFPR=0.000) 这个 methodological innovation，而非 MH-DIF 本身。IRT misspecification 变得不那么致命——framework 的价值不依赖于 MH 的 IRT 假设是否满足。风险：framework 贡献本身是否足够 substantial。\n路径 B \"Multidimensional upgrade\"：正面回应 IRT misspecification——补充 MIRT (multidimensional IRT) 实验。用 confirmatory bifactor model（general + 4-5 domain factors）重跑 DIF，展示 misspecification 修正后 C% 的变化（预期略降但仍 >15%）。 这把 weakness 转化为 contribution：\"first study to compare 1D vs multidimensional DIF on LLM benchmarks\"。GPU cost 可控（bifactor on subsets），timeline 约 4-6 周。 风险：bifactor fit 仍不好（plan_015 killed），需要换 exploratory MIRT 或 mixture IRT。\n路径 C \"Empirical benchmark science\"：重新定位为 benchmark science 而非 contamination detection。Title 类似 \"What 5,227 Models Reveal About MMLU's Measurement Properties\"。不再以 DIF/contamination 为主线，而是以 \"large-scale psychometric audit\" 为 framing：measurement redundancy、item difficulty drift、 domain-level capability shift patterns。DIF 成为 audit 工具之一而非全部。 difficulty×direction interaction (ρ=-0.597) 升为 headline finding。此路径 novelty 来自 empirical findings 本身而非方法，更接近 NeurIPS Datasets & Benchmarks track 风格——但仍可投 ICLR main track 如果 findings 足够 impactful。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nfocus: Dream #4 后的改进：(1) plan_022 model independence — graduated de-duplication 证明 family structure 不 inflate C%；(2) plan_023 item characterization — difficulty×direction ρ=-0.597 强化 diagnostic lens；(3) 删除 unprovenanced r=-0.347；(4) K=10 数据修正；(5) 所有 critical 写作问题已修复。关注 novelty 和 IRT misspecification 是否仍是主要扣分项。\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T06:34:42.438Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T06:34:42.438Z",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T06:34:42.458Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：novelty 被拒；IRT misspecification 被视为根本性缺陷（'misspecified model → all findings suspect'）；需要找新 angle reframe
核心假设：["A1 不成立：majority 评审判定 'applying textbook MH-DIF without modification = insufficient novelty for ICLR'，即使 scale 大", 'A2 不成立：评审认为 98% |Lz|>2 意味着 1D IRT ability estimates 不可靠 → MH 的 ability matching 本身有系统偏差 → 31% C% 可能是 model misfit artifact', "A3 不成立：ρ≈0.997 被解读为 'DIF flags are noise that doesn't matter'，而非 redundancy revelation", "A4 不成立：meta-critique 被视为 'trivially true observation, not a contribution'", 'A5 部分成立：item characterization 数据本身有趣但不足以撑全文', 'A6 不成立：GSM1K 被 dismiss']
关键指标范围：{'reviewer_avg_score': [3.0, 4.5], 'acceptance_probability_pct': [2, 15], 'claims_at_full_strength': [0, 1], 'novelty_sub_score_avg': [1.0, 2.0], 'reviewers_flagging_irt_as_fatal': [2, 4], 'major_revisions_needed': [4, 5]}
叙事方向：核心假设失败，但数据资产（5,227×12,508 response matrix + 全部实验结果）仍在， 需要找新 angle 仍冲 ICLR 2027。三条 reframe 路径——
路径 A "Framework-first"：将 semi-synthetic ΔTPR framework（Claim 3）提升为 第一贡献，paper 变成 methodology paper。Title 类似 "A Semi-Synthetic Framework for Validating Item-Level Contamination Detectors"。31% temporal instability 降为 case study / application section。此路径的 novelty 来自 cross-subject matching (ΔFPR=0.000) 这个 methodological innovation，而非 MH-DIF 本身。IRT misspecification 变得不那么致命——framework 的价值不依赖于 MH 的 IRT 假设是否满足。风险：framework 贡献本身是否足够 substantial。
路径 B "Multidimensional upgrade"：正面回应 IRT misspecification——补充 MIRT (multidimensional IRT) 实验。用 confirmatory bifactor model（general + 4-5 domain factors）重跑 DIF，展示 misspecification 修正后 C% 的变化（预期略降但仍 >15%）。 这把 weakness 转化为 contribution："first study to compare 1D vs multidimensional DIF on LLM benchmarks"。GPU cost 可控（bifactor on subsets），timeline 约 4-6 周。 风险：bifactor fit 仍不好（plan_015 killed），需要换 exploratory MIRT 或 mixture IRT。
路径 C "Empirical benchmark science"：重新定位为 benchmark science 而非 contamination detection。Title 类似 "What 5,227 Models Reveal About MMLU's Measurement Properties"。不再以 DIF/contamination 为主线，而是以 "large-scale psychometric audit" 为 framing：measurement redundancy、item difficulty drift、 domain-level capability shift patterns。DIF 成为 audit 工具之一而非全部。 difficulty×direction interaction (ρ=-0.597) 升为 headline finding。此路径 novelty 来自 empirical findings 本身而非方法，更接近 NeurIPS Datasets & Benchmarks track 风格——但仍可投 ICLR main track 如果 findings 足够 impactful。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen
focus: Dream #4 后的改进：(1) plan_022 model independence — graduated de-duplication 证明 family structure 不 inflate C%；(2) plan_023 item characterization — difficulty×direction ρ=-0.597 强化 diagnostic lens；(3) 删除 unprovenanced r=-0.347；(4) K=10 数据修正；(5) 所有 critical 写作问题已修复。关注 novelty 和 IRT misspecification 是否仍是主要扣分项。

## paper_framing.md

# Paper Framing — irt_equated_bench_regen

## Target Venue
- Primary: ICLR 2027 (expected deadline ~October 2026)

## Paper Type
Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."

## Core Claims (4 条, 可证伪)

**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%)
- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.

**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)
- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection"

**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability

**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.
4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.
- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)
- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.
- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed

## Story Spine (v2 — no-pivot narrative)

**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.

**Key narrative principle**: "Instability ≠ invalidity." DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**

**What we find** (4 contributions, focused):

1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for "models got better."

2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.

3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.

4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).

**Headline result**: "Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations."

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

- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.

## Novelty Articulation (三层，显式化)

MH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:

1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.

2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).

3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).

**Framing**: "We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm."

## Anticipated Reviewer Concerns (updated for pivot)

1. **"38% could just mean models got better"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.

2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.

3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.

4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.

5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.

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
  "promptId": "fe338995-74e3-410d-b078-6e4c48e5e07c",
  "type": "user",
  "uuid": "4d9c208f-57ed-4b12-9791-4e635d8fe3ea",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T06:34:42.456Z_

```json
{
  "parentUuid": "4d9c208f-57ed-4b12-9791-4e635d8fe3ea",
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
  "uuid": "636f5c92-8037-40b0-b150-6461d85fe6cd",
  "timestamp": "2026-05-21T06:34:42.456Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T06:34:42.456Z_

```json
{
  "parentUuid": "636f5c92-8037-40b0-b150-6461d85fe6cd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bc5d5de3-3ed9-4675-a904-3214133f6631",
  "timestamp": "2026-05-21T06:34:42.456Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：novelty 被拒；IRT misspecification 被视为根本性缺陷（'misspecified model → all findings suspect'）；需要找新 angle reframe 核心假设：[\"A1 不成立：majority 评审判定 'applying textbook MH…",
  "leafUuid": "bc5d5de3-3ed9-4675-a904-3214133f6631",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe IRT-contamination study for ICLR 2027",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010"
}
```

---

### Assistant

_source line 8 · 2026-05-21T06:35:16.405Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the `experiment_plan` under the **worst** tier scenario. They've provided extensive context about what "worst" means, the paper framing, and the registry of completed experiments.

Let me carefully go through each planned experiment and predict what would happen in the worst-case scenario:

1. **plan_001** (real_data_dif_mmlu) - Already DONE, but it's in the plan as "planned". Since it's already completed, I should use the actual results but frame them in the worst-case interpretation.

Wait, looking more carefully, the experiment_plan lists experiments with `status: planned`, but the registry shows many of them as DONE. 

I need to sort through which experiments are actually still planned versus which have already been completed, since there's a mismatch between the plan document and the registry. Some like plan_001 and plan_004 show as done in the registry but appear in the planned list, while others like plan_002, plan_003a through 003c, plan_006 through 010 don't appear to have completion records yet.

The user is asking for predictions on each planned experiment under worst-case assumptions, but I should clarify whether they want me to include experiments that are technically marked as planned but have already been executed, or focus only on the ones that genuinely haven't been run yet. rl_robustness_validation
3. plan_003a - constat_perturbation_eval
4. plan_003b - dvd_generation_variance_eval
5. plan_003c - ensemble_fusion
6. plan_004 - cross_benchmark_gsm8k
7. plan_005 - bifactor_irt_equating_pilot
8. plan_006 - item_generation_calibration
9. plan_007 - cumulative_bayesian_dif
10. plan_008 - graceful_degradation_analysis
11. plan_009 - item_focused_trees
12. plan_010 - architecture_stratified_dif
13. plan_011 - semi_synthetic_contamination_validation

For the worst tier:
- Novelty rejected
- IRT misspecification seen as fatal
- Need new angle

Now I'm identifying where my core assumptions are breaking down. The MH-DIF approach without modification won't pass novelty review, the 98% |Lz|>2 pattern suggests the 1D IRT model itself is unreliable and the ability matching in MH has systematic bias that could explain the 31% C%, the high correlation is being read as evidence that DIF flags are just noise, meta-critique gets dismissed as obvious, the item characterization data alone isn't compelling enough, and GSM1K gets rejected outright. For each experiment—both completed and planned—I need to map out the worst-case scenario: for finished work, that means the most damaging interpretation of results that are actually close to what I found, and for upcoming experiments, genuinely poor outcomes. Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc5d5de3-3ed9-4675-a904-3214133f6631",
  "isSidechain": false,
  "requestId": "req_011CbFFQ69sbMynDKAaNZn6S",
  "type": "assistant",
  "uuid": "00215451-ac68-41d7-bfbf-9dd1381e2544",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6rFpXmTXD7UxMSp6uCxvA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19221,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11666,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19221,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11666,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19221
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

_source line 9 · 2026-05-21T06:38:56.344Z_

```yaml
tier: worst
narrative_guidance: >
  核心叙事：novelty 被彻底否定（"applying textbook MH 1988 to new data ≠ contribution"），IRT misspecification 被视为
  根本性方法论缺陷（"98% |Lz|>2 → ability matching 系统性偏差 → 31% C% 是 artifact 而非 finding"），
  semi-synthetic framework 被认为 too simple to publish，meta-critique 被 dismiss 为 obvious。
  每个实验的结果要么被重新解读为 artifact，要么被认为 underpowered/scope-limited。
  reviewer 立场：3 位中 2-3 位给 reject，平均分 3.5，novelty sub-score 1.5。
  三条 reframe 路径（Framework-first / MIRT upgrade / Benchmark science）是唯一出路。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: "METABENCH MMLU 5,227×12,508 response matrix 上的 MH-DIF 分析"
    expected_results:
      temporal_ets_c_pct: 31.3
      temporal_fpr_li_clean: 0.318
      temporal_enrichment: 0.96
      ability_ets_c_pct: 2.9
      within_family_llama2v3_c_pct: 61.3
      domain_spearman_rho: 0.307
      domain_spearman_p: 0.02
      sanity_random_split_c_pct: 0.18
      irt_lz_pct_above_2: 98
      reviewer_interpretation: "artifact_of_misspecification"
    result_rationale: >
      数据本身与已完成 registry 一致——31.3% C% 是真实观测。但在 worst 档下，reviewer 的解读路径是：
      (1) 98% 模型 |Lz|>2 表明 1D IRT ability estimates 系统性不可靠；
      (2) MH 的 ability matching 依赖 total score 作为 ability proxy，而 MMLU 57 subjects 的
      multidimensionality 意味着 total score 是一个 collapsed composite，无法真正 match ability；
      (3) 因此 31.3% C% 中有大量是 ability confounding 造成的 spurious DIF——
      两个模型在不同 subject domains 上能力结构不同，但 total score 相近，被 MH 视为 "matched"，
      实际上它们在特定 subject 上的 ability 并不 matched；
      (4) enrichment≈0.96 直接验证了 DIF flags 与已知 contamination labels 无关联——
      reviewer 读为 "你的方法检测不到 contamination"；
      (5) 0.18% sanity check 虽然证明不是纯噪声，但 reviewer 认为这只是证明 temporal cohort 之间
      确实存在 ability distribution shift，而非 item-level contamination。
      ρ=0.307 (p=0.02) 被 reviewer 解读为 "domain improvement 是 confound 的证据，
      不是被排除的证据"——因为 item-level decomposition (plan_019) 的 pseudo R²=0.0007
      只说明 linear relationship 弱，不排除 nonlinear 或 interaction effects。
    tables:
      - "Table 1: Temporal DIF results — C%=31.3%, enrichment=0.96 — reviewer 标注 'enrichment≈1 = no detection value'"
      - "Table 2: Cohort comparison — ability split C%=2.9% vs temporal 31.3% — reviewer 认为差异来自 ability shift 而非 item-level effect"
    figures_description:
      - "Fig 1: DIF effect size distribution — reviewer 指出 continuous distribution without bimodality suggests no distinct 'contaminated' subpopulation, consistent with model misfit gradual shift"
    analysis: >
      Reviewer 的核心攻击：31.3% 是一个 misspecified model 下的 baseline rate，不是 finding。
      类比：如果你用线性回归拟合非线性数据，residual patterns 不代表新发现，而代表 model misfit。
      MH-DIF on multidimensional data with 1D matching = structural Type I error inflation。
      Llama-2 vs Llama-3 within-family C%=61.3% 被读为更强的证据——"同一 family 内 61% items
      show DIF = 显然是 ability structure change, not contamination"。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: "验证 DIF 对 reasoning-RL 模型（GRPO/PPO）的鲁棒性"
    expected_results:
      n_reasoning_rl_models: 13
      alignment_rl_cohort_n: 477
      grpo_cohort_dif_c_pct: 34.8
      sft_baseline_dif_c_pct: 30.2
      alignment_rl_dif_c_pct: 31.9
      jaccard_sft_vs_grpo: 0.71
      delong_p_dif_vs_constat: 0.38
      tost_equivalence_p: 0.22
      constat_auroc_on_rl: 0.54
      mink_auroc_on_rl: 0.51
      dif_auroc_on_rl: 0.58
      bootstrap_ci_auroc_dif: [0.41, 0.73]
      power_at_p04: 0.12
      power_at_p07: 0.43
      power_at_p10: 0.68
    result_rationale: >
      Worst 档下的问题不是实验跑不出来，而是 N=13 reasoning-RL 模型被 reviewer 视为 fundamentally underpowered：
      (1) 13 个 GRPO/PPO 模型混入 focal cohort 后，C% 从 30.2% 微升到 34.8%——
      reviewer 解读为 "adding stronger models → more ability confounding → more spurious DIF"，
      而非 "DIF robust to RL"；
      (2) AUROC 比较（DIF 0.58 vs ConStat 0.54 vs Min-K% 0.51）差异不显著（DeLong p=0.38），
      bootstrap CI 跨越 0.5——reviewer 说 "all methods are at chance, you've shown nothing"；
      (3) TOST equivalence test p=0.22，无法 reject "DIF 和传统方法等效" 的 H0——
      reviewer 认为 "failure to demonstrate equivalence or superiority = uninformative"；
      (4) Power analysis 显示 p=0.4 时 TPR=0.12——reviewer 说 "DIF can only detect
      near-complete exploitation, which is the trivial case"；
      (5) 核心问题：整个实验无法区分 "DIF works on RL models" 和 "DIF produces same artifacts
      regardless of model type"——在 IRT misspecification 框架下，两者不可区分。
    tables:
      - "Table: AUROC comparison across 3 methods × 3 cohort types — all CIs overlap, no method dominates"
      - "Table: Power curve p ∈ [0.4, 1.0] — reviewer notes 'useful range starts at p≥0.7, narrowing practical applicability'"
    figures_description:
      - "Fig: Bootstrap AUROC distributions — heavy overlap among DIF/ConStat/Min-K%, all centered near 0.55"
    analysis: >
      Reviewer consensus: "N=13 RL models is a pilot, not a validation. The authors cannot claim RL-robustness
      based on mixing 13 models into a 600+ cohort — the signal is drowned. Individual-model analysis
      (ConStat/Min-K%) at least tests each model; DIF by design cannot. This is a structural limitation
      of group-level methods, acknowledged but not resolved."
      致命打击：reviewer 将此解读为 DIF 的固有缺陷——无法做 per-model detection——而非优势。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: "ConStat-style perturbation testing 在 MMLU 上的独立评估"
    expected_results:
      n_items_reformulated: 220
      reformulation_quality_human_eval: 0.82
      constat_detection_rate_non_rl: 0.41
      constat_detection_rate_rl: 0.08
      constat_fdr_controlled_rate: 0.23
      constat_vs_dif_overlap_pct: 12.7
      constat_fpr: 0.067
      constat_unique_detections: 158
      dif_unique_detections: 892
    result_rationale: >
      ConStat 在 non-RL 模型上表现合理（41% detection rate），FPR 远低于 DIF（0.067 vs 0.318）。
      Worst 档下 reviewer 解读：
      (1) ConStat FPR=0.067 vs DIF FPR=0.318——"DIF 的高 detection rate 主要来自高 FPR，
      不是真正的 detection power"；
      (2) 12.7% overlap 表明两种方法检测的是完全不同的现象——reviewer 认为 ConStat 检测 actual contamination
      (perturbation sensitivity)，而 DIF 检测 ability shift artifact；
      (3) ConStat 在 RL 模型上确实退化（8%），但 reviewer 说 "at least ConStat has a clear
      mechanism story; DIF's mechanism is unfalsifiable because any result can be attributed
      to either contamination or ability change"；
      (4) 220 items 的 reformulation 质量（0.82 human eval）足够，但 scope 太小——
      reviewer 要求 full-scale replication 才能比较。
    tables:
      - "Table: ConStat vs DIF detection comparison — ConStat lower recall but much lower FPR"
    figures_description:
      - "Fig: Venn diagram of ConStat vs DIF detections — minimal overlap underscores different phenomena detected"
    analysis: >
      Reviewer 用 ConStat 的低 FPR 作为武器："ConStat achieves controlled FPR by design (FDR correction);
      DIF's 31.8% FPR on Li-clean items means nearly 1 in 3 flags is false, and you cannot tell
      which ones without ground truth." 这强化了 "DIF C% is inflated by misspecification" 的叙事。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: "DVD generation variance 在 MMLU 上的独立评估"
    expected_results:
      n_models_evaluated: 12
      n_items_per_model: 200
      n_generations_per_item: 50
      bimodal_detection_rate: 0.14
      variance_based_detection_rate: 0.22
      dvd_vs_dif_overlap: 0.09
      dvd_fpr: 0.04
      gpu_hours_used: 65
      variant_contamination_detected: 31
    result_rationale: >
      DVD 需要 per-model inference access（50 generations × 200 items × 12 models = 120K generations），
      cost 高但可行。Worst 档下：
      (1) Bimodal detection rate 仅 14%——reviewer 说 "variant contamination is rare or this method
      is underpowered, either way not compelling"；
      (2) 9% overlap with DIF——再次证明方法检测不同现象，但 worst 档下 reviewer 解读为
      "three orthogonal weak signals don't add up to one strong signal"；
      (3) DVD FPR=0.04 很低，但 detection rate 也低——reviewer 认为 precision-recall tradeoff
      不足以支撑 contribution；
      (4) 12 models 太少——reviewer 要求 "at minimum 50+ models to characterize generation variance
      distribution"，而 GPU budget 不支持。
    tables:
      - "Table: DVD detection rates by contamination type (verbatim vs variant) — low overall"
    figures_description:
      - "Fig: Generation variance histograms per model — most items unimodal, bimodal signal weak"
    analysis: >
      DVD 作为独立信号太弱（14% bimodal detection），且 per-model inference 的 cost 使其不 scalable。
      Reviewer 建议 "DVD is better suited as a follow-up diagnostic on flagged items, not a primary detector"
      ——削弱 ensemble 的 motivation。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: "DIF + ConStat + DVD 三信号融合"
    expected_results:
      majority_vote_precision: 0.38
      majority_vote_recall: 0.09
      weighted_fusion_precision: 0.44
      weighted_fusion_recall: 0.15
      ensemble_fpr: 0.087
      cross_val_weight_stability: "low — std/mean > 0.6 across folds"
      dif_weight: 0.28
      constat_weight: 0.51
      dvd_weight: 0.21
      uniform_baseline_vs_optimized_delta_f1: 0.02
    result_rationale: >
      Ensemble 在 worst 档下彻底失败，原因链：
      (1) 三个信号 overlap 极低（pairwise Jaccard < 0.15）→ majority vote 几乎不触发（recall 9%）；
      (2) 加权融合稍好但 cross-validation 权重不稳定（std/mean > 0.6）——reviewer 说
      "overfitting to a small calibration set with unstable weights is not a methodology contribution"；
      (3) Optimized vs uniform weight F1 差异仅 0.02——"no evidence that learned fusion outperforms
      naive averaging, suggesting insufficient signal diversity"；
      (4) DIF weight 仅 0.28（最低），ConStat 0.51——reviewer 读为 "even the ensemble downweights DIF,
      your supposed primary contribution"；
      (5) FPR=0.087 达标（<0.10），但 recall=0.15 意味着 85% contamination 未检测——
      "an ensemble that misses 85% of contaminated items is not operationally useful"。
      核心问题：Claim 2（ensemble = contribution）在 worst 档下被视为 negative result，
      不是 contribution——"showing that three weak detectors don't combine well is not novel"。
    tables:
      - "Table: Ensemble configurations — all recall < 0.20, precision < 0.50"
      - "Table: Cross-validation fold weights — high variance across folds"
    figures_description:
      - "Fig: Precision-recall curves for individual signals and ensemble — ensemble barely improves over best individual"
    analysis: >
      Ensemble 在 paper 中降级为 appendix negative result。Reviewer 的结论性评价：
      "The ensemble experiment confirms what the low pairwise overlaps predicted — these methods
      detect different phenomena (or noise), and combining them doesn't produce a coherent detector.
      This is informative but not a contribution; it's a null result."

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: "GSM8K 上复制 DIF 分析，用 GSM1K 作为 contamination ground truth"
    expected_results:
      gsm8k_n_items: 1319
      gsm8k_n_ref: 1017
      gsm8k_n_foc: 804
      gsm8k_standard_c_pct: 18.9
      gsm8k_external_c_pct: 47.4
      gsm8k_sanity_c_pct: 0.3
      semi_synthetic_delta_tpr_p10: 0.818
      gsm1k_n_models: 33
      gsm1k_pearson_r: -0.478
      gsm1k_pearson_p: 0.005
      gsm1k_spearman_rho: -0.403
      gsm1k_bca_ci_upper: -0.155
      gsm1k_partial_r: -0.385
      reviewer_dismiss_gsm1k: true
    result_rationale: >
      数据与 registry 一致。Worst 档下 reviewer 的攻击矩阵：
      (1) N=33 模型——"33 data points with r=-0.478 is suggestive at best; BCa CI upper bound
      |r|=0.155 means the true effect could be trivially small"；
      (2) 负相关方向 (r=-0.478) 与 contamination hypothesis 相反——DIF items 上 contamination gap
      更小，不是更大。Paper 解释为 "DIF items resist contamination-based gains"，
      reviewer 替代解读："DIF items are simply harder items where all models struggle,
      contaminated or not — the negative correlation is a difficulty confound, not a detection signal"；
      (3) Spearman CI [−0.687, −0.031] 上界接近 0——"barely significant, and with N=33
      a single influential point shifts everything"（尽管 Cook's D robust, leave-one-out stable）；
      (4) GSM8K 是 single-domain math benchmark, MMLU 是 57-subject multidomain——
      "generalization from GSM8K to MMLU is not justified; the DIF mechanism operates differently
      on unidimensional vs multidimensional benchmarks"；
      (5) GSM1K 本身作为 ground truth 被质疑——"GSM1K measures a different construct (novel math problems)
      and the gap may reflect test-taking strategy differences, not contamination"。
      核心：A6 不成立——GSM1K 被 dismiss。
    tables:
      - "Table: GSM1K correlation — r=-0.478 with wide CI, reviewer highlights N=33 limitation"
      - "Table: Semi-synthetic ΔTPR=0.818 — reviewer acknowledges but says 'synthetic ≠ real'"
    figures_description:
      - "Fig: Scatter plot N=33 models, DIF-C accuracy vs contamination gap — reviewer draws attention to sparse coverage and leverage points"
    analysis: >
      GSM8K semi-synthetic (ΔTPR=0.818) 是最强结果，但 reviewer 将其与 MMLU 主分析隔离：
      "The GSM8K semi-synthetic result is impressive but says nothing about whether the 31.3% MMLU finding
      is real or artifact — different benchmark, different dimensionality, different N."
      GSM1K correlation 被 dismiss due to N=33 和 difficulty confound alternative explanation。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: "Bifactor IRT equating pilot — general factor + subject-specific factors"
    expected_results:
      bifactor_convergence: false
      rmsea: 0.089
      cfi: 0.71
      tli: 0.68
      srmr: 0.112
      n_heywood_cases: 47
      anchor_items_identified: 0
      equated_score_rho: null
      decision: killed
    result_rationale: >
      与 registry (plan_015 killed) 一致。Worst 档下 bifactor 失败的机制：
      (1) 12,508 items × 5,227 models 的 bifactor model（general + 57 subject factors）
      参数空间巨大（~12,508 × 59 = ~738K parameters），mirt 不收敛；
      (2) 即使降到 subset（5 subjects, ~1,200 items），Heywood cases（负方差估计）出现 47 次——
      说明 data 不支持 bifactor structure，或者需要 constrained estimation；
      (3) RMSEA=0.089 > 0.06 cutoff, CFI=0.71 < 0.90 cutoff——fit 远低于 acceptable 标准；
      (4) 无法识别 anchor items（因为 model 本身不 fit）→ 整个 equating pipeline 断裂；
      (5) Reviewer 的解读最致命："You can't even fit a bifactor model to this data —
      this CONFIRMS that IRT assumptions are fundamentally violated for MMLU.
      If bifactor doesn't fit, your 1D MH-DIF is even more misspecified than we thought."
      这个 killed experiment 在 worst 档下反而成为 reviewer 攻击 IRT misspecification 的额外弹药。
    tables:
      - "Table: Bifactor fit indices — all below acceptable thresholds"
    figures_description:
      - "Fig: Convergence diagnostics — oscillating log-likelihood, Heywood cases marked"
    analysis: >
      Bifactor 失败在 worst 档下是 double-edged：不仅 equating 路径 dead，
      还为 reviewer 提供了 "see, even the authors tried to fix IRT misspecification and failed" 的叙事。
      在 reframe 路径 B（MIRT upgrade）中需要换 exploratory MIRT 或 mixture IRT 而非 confirmatory bifactor。

  - name: item_generation_calibration
    plan_id: plan_006
    description: "LLM 生成替换 items + student simulation 校准"
    expected_results:
      n_items_generated: 500
      difficulty_rho_prompt_based: 0.18
      difficulty_rho_student_sim: 0.52
      target_difficulty_rho: 0.75
      construct_alignment_human_eval: 0.64
      holdout_panel_correlation: 0.41
      replacement_quality_verdict: below_benchmark
    result_rationale: >
      Worst 档下 item generation 全面低于 benchmarks：
      (1) Prompt-based difficulty targeting ρ=0.18（文献报告 0.10-0.45 range 的下端）；
      (2) Student simulation 校准 ρ=0.52（文献报告 0.75-0.82 的下限以下）——
      MMLU 的 domain diversity 使得单一 student simulator 无法准确估计 57 subjects 的 difficulty；
      (3) Construct alignment human evaluation 仅 0.64——36% 的生成 items 被判定
      与原 item 不在同一 cognitive level 或 subject boundary 内；
      (4) Holdout model panel correlation 0.41——替换 items 上的 model ranking
      与原 items ranking 相关性太低，equating 无法保证 score equivalence；
      (5) Reviewer 的攻击："If you can't generate calibrated replacement items,
      the entire benchmark regeneration pipeline is aspirational, not operational.
      This undermines Claim 3's practical value."
      依赖 plan_005 的 anchor items 识别，而 plan_005 已 killed → 整条 pipeline dead。
    tables:
      - "Table: Difficulty calibration — prompt-based vs student-sim vs target, all below threshold"
    figures_description:
      - "Fig: Predicted vs actual item difficulty scatter — wide dispersion, ρ=0.52"
    analysis: >
      Item generation 在 worst 档下是 Claim 3（benchmark regeneration）的棺材钉。
      即使不考虑 bifactor failure，生成 items 的质量本身不足以支撑 "operational replacement" 的 claim。
      Reviewer 建议 "demote to future work"——which is exactly what the reframe paths do。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: "Cumulative Bayesian DIF priors — 4 successive administrations模拟"
    expected_results:
      single_admin_power_d10: 0.38
      cumulative_2_admin_power_d10: 0.49
      cumulative_3_admin_power_d10: 0.58
      cumulative_4_admin_power_d10: 0.64
      target_cumulative_power: 0.70
      simulation_only: true
      real_data_validation: none
    result_rationale: >
      Worst 档下 cumulative Bayesian DIF 问题：
      (1) 即使 4 次 administration 后 power 仅 0.64，低于 target 0.70——
      prior accumulation 的增益被 IRT misspecification 的 systematic bias 抵消；
      (2) 纯 simulation，无 real data validation——reviewer 说 "simulation under
      your assumed generative model will always confirm your method; this is tautological"；
      (3) "4 successive administrations" 假设 benchmark 不变——但如果 items 在 generation 之间
      确实 drift（即你自己的 Claim 1），则 prior 积累的是 stale information；
      (4) Sinharay et al. (2006) 原始方法设计为 human testing with stable construct——
      LLM benchmark 的 rapid capability shift 违反了 prior accumulation 的 stationarity 假设；
      (5) Reviewer 直接 dismiss："Simulation-only, no real data, questionable assumptions
      about temporal stationarity. Appendix material at best."
    tables:
      - "Table: Power accumulation over 4 administrations — falls short of 0.70 target at δ=1.0"
    figures_description:
      - "Fig: Power curves by number of accumulated administrations — reviewer annotates 'simulation only' and 'stationarity violated'"
    analysis: >
      Cumulative Bayesian DIF 在 worst 档下是 appendix filler，不贡献 novelty 也不贡献 empirical evidence。
      Reviewer consensus: underdeveloped simulation study without real-data anchoring。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: "Benchmark validity degradation under progressive item replacement"
    expected_results:
      rho_at_5pct_replacement: 0.994
      rho_at_10pct_replacement: 0.986
      rho_at_20pct_replacement: 0.961
      rho_at_50pct_replacement: 0.873
      reliability_alpha_original: 0.94
      reliability_alpha_at_20pct: 0.88
      construct_coverage_gap_at_20pct: "3 subjects lose >30% items"
      theoretical_bound_tight: false
    result_rationale: >
      Worst 档下 graceful degradation 的问题：
      (1) 依赖 plan_005/006 的替换 items——两者都 failed/below benchmark，
      因此 "replacement" 实际上是 random item removal，不是 calibrated replacement；
      (2) ρ at 20% replacement = 0.961 看似 ok，但 reviewer 用 plan_017 的结果反驳：
      "You already showed ρ≈0.997 when removing 31% DIF items. Random replacement at 20%
      gives ρ=0.961 — WORSE than just removing items entirely. Your replacement items ADD noise."；
      (3) Reliability alpha 从 0.94 降到 0.88——"degradation is measurable and concerning
      at only 20% replacement"；
      (4) 3 subjects lose >30% items at 20% replacement rate——construct coverage 不均匀，
      某些 domain 被 disproportionately 影响；
      (5) Theoretical bounds 不 tight——无法给出 "replace up to X% safely" 的 actionable threshold，
      削弱 practical contribution。
    tables:
      - "Table: Validity metrics × replacement rate — degradation faster than expected"
    figures_description:
      - "Fig: ρ vs replacement rate curve — comparison with pure removal shows replacement adds noise"
    analysis: >
      在 bifactor 和 item generation 都失败的前提下，graceful degradation 变成 "removing items" 分析而非
      "replacing items" 分析。与 plan_017 的 ρ≈0.997 冲突——removing DIF items 更安全
      than replacing them with poorly calibrated alternatives。Reviewer 结论：
      "The regeneration pipeline is not ready for deployment."

  - name: item_focused_trees
    plan_id: plan_009
    description: "Item-Focused Trees (Tutz & Berger 2016) — continuous temporal covariate DIF"
    expected_results:
      ift_n_items_flagged: 4102
      ift_vs_mh_jaccard: 0.48
      ift_unique_flags: 1834
      mh_unique_flags: 1650
      ift_first_split_variable: "release_date"
      ift_interaction_with_size: "significant (p<0.01)"
      ift_temporal_granularity: "quarterly splits emerge naturally"
    result_rationale: >
      IFT 在 worst 档下成为双刃剑：
      (1) IFT flags 4,102 items (32.8%) vs MH flags 3,918 (31.3%)——数量相近但 overlap 仅 48%，
      meaning 52% 的 flags 不一致；
      (2) Reviewer 解读："Two DIF methods on the same data flag different items —
      this means at least one (probably both) is detecting noise, not signal.
      If the phenomenon were real and large, methods should converge."；
      (3) IFT 的 continuous treatment 本身挑战了 MH 的 binary temporal split——
      "IFT shows the split is not clean at your chosen cutoff; DIF is gradual across
      the timeline, suggesting capability drift not contamination events"；
      (4) IFT interaction with model size (p<0.01) 引入新 confound——
      "bigger models released later AND are more capable, so temporal DIF = size+capability confound"；
      (5) IFT 作为 robustness check 未能 confirm MH——在 worst 档下这是 negative evidence。
    tables:
      - "Table: MH vs IFT flag comparison — 48% Jaccard, significant disagreement"
    figures_description:
      - "Fig: IFT tree structure — first split on date, second on model size — reviewer reads as confound evidence"
    analysis: >
      IFT 本意是 "alternative method validates MH"，但 worst 档下 48% overlap 被读为 refutation。
      Reviewer 的 steel-man 攻击："If items' DIF status depends on which method you use,
      the phenomenon is not robust — it's an artifact of methodological choices."
      IFT 降级为 appendix，与主 finding 的 tension 在 limitations 中 discuss。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: "Decoder-only 子群内 DIF 分析 — 测试 architecture heterogeneity 影响"
    expected_results:
      n_decoder_only: 5226
      n_non_decoder: 1
      decoder_only_c_pct: 31.3
      full_population_c_pct: 31.3
      jaccard_decoder_vs_full: 1.0
      rmsea_decoder_only: 0.087
      cfi_decoder_only: 0.73
      tlr_decoder_only: 0.70
      irt_lz_pct_above_2_decoder_only: 97.8
    result_rationale: >
      与 paper_framing 一致——METABENCH MMLU 是 99.98% decoder-only (5226/5227)。
      Worst 档下这个实验 backfires：
      (1) Removing 1 non-decoder model 什么都不改变 (Jaccard=1.0, C% identical)——
      reviewer 说 "this is a vacuous robustness check; with 1 non-decoder model,
      architecture stratification is meaningless"；
      (2) 真正的问题是 IRT fit——RMSEA=0.087, CFI=0.73, |Lz|>2 仍然 97.8%——
      "decoder-only homogeneity doesn't fix IRT misspecification because the misfit
      comes from 57-subject multidimensionality, not architecture mixing"；
      (3) Reviewer 的核心反驳："You showed architecture isn't the problem — fine.
      But you still haven't addressed THE problem: multidimensional ability
      with 1D matching. Removing 1 model is irrelevant; fitting a multidimensional
      IRT model is what's needed."；
      (4) 实验在 paper_framing 中被列为 "✅ RESOLVED"，但 worst 档 reviewer 认为
      它 resolved a non-issue while ignoring the actual issue。
    tables:
      - "Table: Full vs decoder-only DIF — identical results, confirming architecture is not the confound"
    figures_description:
      - "Fig: IRT fit indices — still poor even in homogeneous subgroup"
    analysis: >
      Architecture stratification 是一个 true-but-trivial result。99.98% decoder-only 意味着
      这个 check 从设计上就不可能找到 architecture effect。Reviewer 用它作为 "authors address
      the wrong confound" 的证据——the real confound is multidimensionality, not architecture。
      在 reframe 路径下，这个实验仍然 reportable but not defensive。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: "Known contamination injection into real METABENCH matrix — controlled ground truth"
    expected_results:
      n_clean_items_selected: 500
      n_injected_items: 200
      temporal_external_tpr_p0: 0.326
      temporal_external_tpr_p03: 0.548
      temporal_external_tpr_p05: 0.834
      temporal_external_tpr_p10: 1.0
      temporal_external_fpr: 0.314
      temporal_external_delta_tpr_p05: 0.508
      temporal_external_delta_tpr_p10: 0.674
      ability_external_tpr_p10: 0.8
      ability_external_fpr: 0.493
      standard_mh_fpr_inflation_at_p10: "0.298→0.616"
      matching_variable_contamination: true
      cross_subject_delta_fpr: 0.0
    result_rationale: >
      与 registry 一致。Semi-synthetic 是 paper 最强技术贡献，但 worst 档下：
      (1) baseline FPR=0.314——"even before injection, 31.4% items are flagged.
      ΔTPR is measured against this inflated baseline, so the 'detection power'
      is really 'additional flags on top of already-massive false positive rate'"；
      (2) Reviewer 的关键攻击：ΔTPR=0.508 at p=0.5 means "if half the focal group
      memorizes an item, DIF has 50% chance of catching it ON TOP of 31% baseline noise.
      In absolute terms, you flag 83.4% of injected items — but you also flag 31.4% of
      clean items. Your precision is ~(0.508×200)/(0.508×200+0.314×300) ≈ 52%."；
      (3) injection mechanism (incorrect→correct flip) 是 simplification——
      "real contamination doesn't flip all wrong answers to correct; partial memorization
      produces answer-distribution shifts, not binary flips"；
      (4) FPR inflation under standard matching (0.298→0.616) 虽然被 cross-subject matching
      解决 (ΔFPR=0.000)，但 reviewer 质疑 cross-subject matching 本身：
      "using other-subject scores as matching variable assumes subjects are independent —
      but Q3 analysis (plan_013) showed cross-subject |Q3| can reach 0.20+"；
      (5) 最深层攻击：injection into a matrix where 1D IRT is already misspecified →
      "you're testing detection power of a misspecified method on a misspecified baseline;
      positive ΔTPR doesn't validate the method, it validates that adding signal
      to a noisy detector shifts its output"。
      尽管如此，ΔTPR dose-response (0.3→0.5→0.7→1.0 : 0.548→0.834→0.99→1.0) 和
      cross-subject ΔFPR=0.000 仍然是 technically impressive，reviewer 不否认技术执行，
      而是质疑其 interpretive value given misspecification。
    tables:
      - "Table: Semi-synthetic TPR/FPR across injection rates — reviewer annotates baseline FPR as 'the real story'"
      - "Table: Standard vs cross-subject matching — ΔFPR=0.000 is acknowledged but Q3 caveat raised"
    figures_description:
      - "Fig: Dose-response curve ΔTPR vs p — clean sigmoid, but reviewer adds dotted line at FPR=0.314 baseline"
      - "Fig: Cross-subject vs within-subject FPR comparison — clean result but 'independence assumption questionable'"
    analysis: >
      Semi-synthetic 在 worst 档下从 "validates DIF" 被重新解读为 "validates that injecting signal
      into a high-FPR detector produces more flags." Cross-subject matching (ΔFPR=0.000) 是
      最 defensible 的技术结果，但被 reviewer 用 Q3 cross-subject correlation 削弱。
      在 reframe 路径 A（Framework-first）中，这个实验升为 primary contribution——
      即使 reviewer 攻击 MMLU DIF 本身，framework 的 reusability 和 ΔFPR=0.000 innovation
      仍有独立价值。这是 worst 档下最有 salvage potential 的实验。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00215451-ac68-41d7-bfbf-9dd1381e2544",
  "isSidechain": false,
  "requestId": "req_011CbFFQ69sbMynDKAaNZn6S",
  "type": "assistant",
  "uuid": "9edd276f-0105-444b-b296-6780269d14de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6rFpXmTXD7UxMSp6uCxvA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19221,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11666,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19221,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11666,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19221
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：novelty 被拒；IRT misspecification 被视为根本性缺陷（'misspecified model → all findings suspect'）；需要找新 angle reframe 核心假设：[\"A1 不成立：majority 评审判定 'applying textbook MH…",
  "leafUuid": "9edd276f-0105-444b-b296-6780269d14de",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe IRT-contamination study for ICLR 2027",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：novelty 被拒；IRT misspecification 被视为根本性缺陷（'misspecified model → all findings suspect'）；需要找新 angle reframe 核心假设：[\"A1 不成立：majority 评审判定 'applying textbook MH…",
  "leafUuid": "9edd276f-0105-444b-b296-6780269d14de",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe IRT-contamination study for ICLR 2027",
  "sessionId": "90866091-0b36-4c98-a56f-c14ff188e010"
}
```

---
