# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有 robustness check 干净通过，permutation null 确认 31% 远超 chance，reviewer 认可 'diag

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/fe355a51-20c3-4c39-b040-f88ab66995c4.jsonl`
- **Structured JSON:** [`d86ac181b936175f236a.json`](../../sessions/d8/d86ac181b936175f236a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:26:25.631Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:26:25.631Z",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有 robustness check 干净通过，permutation null 确认 31% 远超 chance，reviewer 认可 'diagnostic lens' 作为 empirical contribution 类型\n核心假设：['plan_029 permutation null C% < 1%，与 random-split 0.18% 一致，temporal structure 不 inflate DIF', '8 页压缩后四条 claim 的核心证据链完整保留（threshold sensitivity + decomposition + NN matching + circularity ablation + multi-benchmark）', \"reviewer 接受 'no new algorithm, new empirical findings + validation framework + meta-critique' 的贡献类型\", 'ability confound 叙事闭环：d=-0.17 → NN matched C%=28.9% → 与 Llama-2v3 d=-0.99 的对照实验形成 dose-response 说服力', '6 benchmark 一致性（17.9–31.3%）被视为 generalizability 的充分证据']\n关键指标范围：{'permutation_null_c_pct': [0.0, 1.0], 'residual_c_pct_after_all_controls': [27.0, 31.3], 'ability_confound_explained_pp': [1.5, 3.0], 'cross_benchmark_c_range_pct': [17.0, 32.0], 'semi_synthetic_delta_tpr_p05': [0.45, 0.55], 'cross_subject_delta_fpr': [0.0, 0.005], 'ranking_stability_rho': [0.995, 0.999], 'simulated_avg_reviewer_score': [3.5, 4.5], 'page_count_main_body': [7.5, 8.0]}\n叙事方向：原始 framing 完全成立。四条 claim 无需调整强度。Headline: '31% temporal instability across 6 benchmarks, not explained by capability improvement (≤7.6%), validated by semi-synthetic framework with 0 FPR inflation.' Meta-critique 作为 aggressive contribution 直接成立。Diagnostic lens + audit protocol 作为 actionable 贡献。GSM1K correlation 留 appendix 作为 exploratory。IRT misfit 在 limitations 一笔带过（multidimensionality motivation）。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:26:25.634Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:26:25.634Z",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T12:26:25.657Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有 robustness check 干净通过，permutation null 确认 31% 远超 chance，reviewer 认可 'diagnostic lens' 作为 empirical contribution 类型
核心假设：['plan_029 permutation null C% < 1%，与 random-split 0.18% 一致，temporal structure 不 inflate DIF', '8 页压缩后四条 claim 的核心证据链完整保留（threshold sensitivity + decomposition + NN matching + circularity ablation + multi-benchmark）', "reviewer 接受 'no new algorithm, new empirical findings + validation framework + meta-critique' 的贡献类型", 'ability confound 叙事闭环：d=-0.17 → NN matched C%=28.9% → 与 Llama-2v3 d=-0.99 的对照实验形成 dose-response 说服力', '6 benchmark 一致性（17.9–31.3%）被视为 generalizability 的充分证据']
关键指标范围：{'permutation_null_c_pct': [0.0, 1.0], 'residual_c_pct_after_all_controls': [27.0, 31.3], 'ability_confound_explained_pp': [1.5, 3.0], 'cross_benchmark_c_range_pct': [17.0, 32.0], 'semi_synthetic_delta_tpr_p05': [0.45, 0.55], 'cross_subject_delta_fpr': [0.0, 0.005], 'ranking_stability_rho': [0.995, 0.999], 'simulated_avg_reviewer_score': [3.5, 4.5], 'page_count_main_body': [7.5, 8.0]}
叙事方向：原始 framing 完全成立。四条 claim 无需调整强度。Headline: '31% temporal instability across 6 benchmarks, not explained by capability improvement (≤7.6%), validated by semi-synthetic framework with 0 FPR inflation.' Meta-critique 作为 aggressive contribution 直接成立。Diagnostic lens + audit protocol 作为 actionable 贡献。GSM1K correlation 留 appendix 作为 exploratory。IRT misfit 在 limitations 一笔带过（multidimensionality motivation）。

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
  "promptId": "8a8acbce-6212-43d1-99e1-26b4c3df6af5",
  "type": "user",
  "uuid": "b176a239-0530-4a37-986e-52836b52d5e0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:26:25.655Z_

```json
{
  "parentUuid": "b176a239-0530-4a37-986e-52836b52d5e0",
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
  "uuid": "e3a49ce0-c89f-4ba5-b7ed-c9e1e904745b",
  "timestamp": "2026-05-21T12:26:25.655Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:26:25.655Z_

```json
{
  "parentUuid": "e3a49ce0-c89f-4ba5-b7ed-c9e1e904745b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dad59d39-e6ed-4a12-bfbb-b9482b2c7221",
  "timestamp": "2026-05-21T12:26:25.655Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有 robustness check 干净通过，permutation null 确认 31% 远超 chance，reviewer 认可 'diagnostic lens' 作为 empirical contribution 类型 核心假设：['plan_029 permutation null C% <…",
  "leafUuid": "dad59d39-e6ed-4a12-bfbb-b9482b2c7221",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric DIF analysis of 5227 models on MMLU",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:34:22.234Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for every "planned" experiment in the experiment_plan, under the "best" tier scenario. Let me identify all planned experiments:

1. plan_001 - real_data_dif_mmlu (status: planned, but actually already DONE in registry as plan_001_real_data_dif_mmlu)
2. plan_002 - rl_robustness_validation (status: planned)
3. plan_003a - constat_perturbation_eval (status: planned)
4. plan_003b - dvd_generation_variance_eval (status: planned)


5. plan_003c - ensemble_fusion (status: planned)
6. plan_004 - cross_benchmark_gsm8k (status: planned, but DONE in registry)
7. plan_005 - bifactor_irt_equating_pilot (status: planned)
8. plan_006 - item_generation_calibration (status: planned)
9. plan_007 - cumulative_bayesian_dif (status: planned)
10. plan_008 - graceful_degradation_analysis (status: planned)
11. plan_009 - item_focused_trees (status: planned)
12. plan_010 - architecture_stratified_dif (status: planned, but noted in paper)

I'm noticing a discrepancy between the experiment plan and the registry. The plan marks everything as planned, but the registry shows several experiments already completed. Since the user is asking for detailed predictions for each planned experiment, I need to generate results for all of them, even the ones that appear to be done. I need to generate detailed results for all the planned experiments under the best-tier scenario. For experiments already completed and in the registry, I'll base the predictions on their actual outcomes. For the ones not yet done, I'll imagine what the best-case results would look like. Let me compile the full dataset across all sixteen experiments in the plan. Now I'm reviewing the remaining experiments: plan_004 through plan_028 shows GSM8K achieved a negative correlation, plan_005 got absorbed into a later iteration, while plans_006 through_009 are supplementary or simulation-focused work that didn't make the final cut. Plans_010, _011, and _028 all completed successfully, with the architecture analysis resolving the decoder-only dominance question and the validation studies confirming the approach across multiple benchmarks.

For the best-tier framing, I need to reconcile which dropped experiments still matter—plan_029 on permutation nulls and plan_030 on odds ratios are critical because the core claims explicitly depend on showing that the 31% effect size far exceeds chance, and the reviewer's acceptance of the diagnostic lens as an empirical contribution hinges on these robustness checks holding up cleanly. , reviewer acceptance, ability confound narrative, 6 benchmark consistency

The best tier is about the paper's core narrative succeeding. Dropped experiments (003a/b/c, 005, 006) are explicitly dropped from the paper. In best tier, those experiments either produce supplementary/negative results that don't hurt the paper, or they're acknowledged as future work.

Let me think about what "best" means for each:

For plan_002 (RL robustness): In best tier, alignment-RL cohort shows DIF flags same items (Jaccard>0.85). Reasoning-RL N=13 acknowledged as underpowered. Moved to limitations.

For plan_003a/b/c: These were dropped. In best tier, they produce negative/incomplete results but this doesn't matter because the paper pivoted away from ensemble. They'd still be listed as not executed or negative.

For plan_005: Bifactor gets killed by plan_014's pre-check showing within-subject C%=38.1% exceeds the 25% threshold, so it's correctly dropped in best tier.

For plan_006: Depends on plan_005, so it doesn't proceed either.

For plan_007 through plan_010: Simulation works and moves to appendix, graceful degradation shows clean results in appendix, item-focused trees serves as supplementary robustness check, and the decoder-only confirmation shows 99.98% with unchanged C% and perfect Jaccard agreement.

For plan_029: Permutation null shows C% under 1%, validating that the observed 31% far exceeds chance.

Now I'm compiling the metric ranges from the best tier to establish the expected performance envelope.

I'll populate the YAML with actual results from completed experiments as the baseline, since those already represent the best-case outcomes, then project consistent values for the planned experiments based on these established ranges.

For the remaining experiments, I'm mapping out which ones are feasible versus blocked—plan_003b on generation variance shows modest detection power for non-RL models and goes to appendix, plan_003c on ensemble methods depends on the prior results and likely moves to future work, plan_005 on bifactor IRT reveals that the model fit diagnostics are too poor at this scale to proceed, and plan_006 hinges on whether plan_005 succeeds. Looking at the performance metrics across these different experimental approaches, I'm seeing that several have already been completed—plan_007 through plan_011 and plan_028 all show results, while plan_029 confirms the permutation null is statistically significant and plan_030 validates Simpson's paradox. Now I need to reconcile what's actually been executed against what's still in the pipeline by cross-referencing the experiment plan against the registry to identify which ones are genuinely pending versus already resolved. I see there are additional experiments in the registry that weren't captured in the experiment_plan, so I need to account for those too. For the ones already completed, I'll pull their actual metrics from the registry, and for the truly planned experiments, I'll estimate best-tier performance. I'm also noting which experiments from the paper framing aren't in the official plan, so I'll exclude those from my predictions.

Now I'm structuring the YAML with a clear schema: each experiment gets its name, plan ID, brief description, expected metrics, rationale for those results, supporting tables and figures, and detailed analysis. Since plan_001 has actual registry data, I'll use that as ground truth and extrapolate from there. For plan_002 and the others, best-tier results would show strong alignment metrics and minimal flag overlap across the different RL approaches.

Generating comprehensive YAML... Jaccard≈0.87 with non-RL cohort
- Reasoning RL (N=13): Too few for group-level DIF, but added to focal cohort doesn't change C% appreciably
- Traditional detectors (Min-K%, ConStat) degrade on reasoning RL models individually
- TOST equivalence confirmed for DIF retention ratio
- But N=13 means this is inherently limited → goes to limitations

The paper handles plan_002 gracefully by acknowledging the underpowered sample size rather than claiming RL robustness as a main finding. For the unexecuted plans (003a/b/c), I should speculate on what they'd likely show if run: ConStat would probably catch reformulation sensitivity in maybe 15-25% of non-RL items but struggle with RL models, DVD would show bimodal variance in a small subset of items without clear advantage over random detection, and an ensemble approach would broaden coverage but introduce calibration noise that belongs in the appendix.

The infeasible plans (005, 006) are correctly dropped—bifactor IRT is too high-dimensional for MMLU's structure, and item generation can't hit the difficulty correlation target even with student simulation. Plan_007 (cumulative Bayesian) produces a clean simulation result showing power improves from 0.40 to 0.72 across administrations, but it's simulation-only so it goes to appendix. Plan_008 on graceful degradation is next. The permutation null distribution shows a mean around 0.21% with standard deviation of 0.12%, and the 95th percentile sits at 0.48%—my observed 31.3% is far beyond that, giving p < 0.001 with zero permutations exceeding it, which aligns with the random-split sanity check result of 0.18%. Now I'm ready to write out the YAML configuration with the completed experiments using their actual registry metrics.

Writing YAML config... Writing YAML structure... Writing the experiment specifications... ability_ets_c_pct: 2.9
- ability_enrichment: 1.19
- within_family_llama2v3_c_pct: 61.3
- within_family_mistral_mixtral_c_pct: 38.7
- domain_spearman_rho: 0.307
- domain_spearman_p: 0.02
- sanity_random_split_c_pct: 0.18
- temporal_ability_jaccard: 0.014

result_rationale: Temporal cohort (2023 vs 2024-H1) captures genuine item-level functioning changes. 31.3% C% reflects real instability because: (1) random split yields only 0.18% (statistical artifact ruled out), (2) domain improvement correlation is modest (ρ=0.307) and item-level decomposition shows ≤7.6% explained, (3) ability cohort C% is only 2.9% (DIF is temporal, not ability-driven), (4) within-family analysis (Llama-2v3: 61.3%) confirms cross-generational changes within architecturally identical families. Enrichment ≈1.0 is expected under the meta-critique framing: web-overlap labels cannot capture differential contamination.

For RL robustness validation, the paper doesn't emphasize this as a core contribution and the sample of 13 reasoning-RL models is admittedly small, though the directional findings remain consistent. Looking at the expected results for alignment metrics across temporal and full model comparisons. Now I'm looking at the true positive rates across different power analysis thresholds, and they're climbing substantially as the threshold increases. The reasoning RL models show much weaker detection performance compared to alignment RL—their contracted NLL distributions make them harder to identify with standard detectors like ConStat and Min-K%. With only 13 models in the focal cohort, the sample size is too small to make definitive statistical claims, though the equivalence test is approaching significance.

Let me reconsider the experimental design more carefully. The core question is whether adding reasoning RL models to the cohort shifts the DIF detection flags, and whether traditional per-model detectors actually degrade when applied to reasoning RL individuals. At the group level, DIF flags appear stable regardless of cohort composition, but at the individual model level, the performance drops noticeably.

With N=13 models, the statistical power is limited. For plan_002, I have 100 GPU hours available for MMLU inference across 10-15 models, which is workable. Now I'll write out the full YAML specification. For the dropped experiments (plan_003a, 003b, 003c), I should predict results that justify why they were deprioritized—they'd likely show moderate results that confirm the paper's decision to focus elsewhere rather than pursuing ensemble approaches.

ConStat would detect reformulation sensitivity in about 18% of items on standard models but degrade significantly on RL-trained models, with only modest overlap with DIF findings (Jaccard ~0.25), suggesting it's complementary but not strong enough to warrant inclusion. DVD would identify roughly 12% of items with generation variance, mostly capturing verbatim memorization rather than variant contamination, and its low overlap with DIF (Jaccard ~0.15) plus scalability constraints from requiring open-weight models make it less viable. The ensemble voting approach would show that combining these detectors doesn't yield sufficient gains to justify the added complexity.

For the bifactor IRT model on MMLU, the 58-factor structure (one general factor plus 57 subject-specific ones) fails to converge fully, and even the reduced 5-domain version shows only marginal improvements—RMSEA drops from 0.12 to 0.09 but stays above the 0.05 threshold, and CFI reaches 0.84 but falls short of the 0.90 benchmark, with anchor item selection yielding just 15 usable items.

Plan_006 on item generation was dependent on plan_005 anyway, but testing it independently shows difficulty correlations only reaching 0.38 to 0.52 against the 0.75 target, and the generated items lack proper construct validation, so it was correctly abandoned.

Plan_007 with cumulative Bayesian updating across four administrations demonstrates clean evidence accumulation—power grows from 0.41 at a single administration to 0.81 after four—and this goes into the appendix.

Plan_008 on graceful degradation shows that replacing 5% to 50% of items with DIF-free alternatives maintains strong correlations and reliability, staying consistent with plan_017's findings at 31% replacement, making it another solid appendix result.

Plan_009 shifts to item-focused trees with continuous temporal covariates, showing 0.78 Jaccard overlap with the categorical Mantel-Haenszel approach.

Now looking at plan_010's architecture stratification—the dataset is almost entirely decoder-only models (99.98%), and removing that single non-decoder model doesn't change the IRT fit diagnostics at all, suggesting architecture heterogeneity isn't driving the observed patterns in MMLU performance.

Finally, the permutation null test with 1000 shuffles shows the null distribution of C% clustering around 0.22% mean with a max of 0.63%, establishing a baseline for comparison.

Writing YAML output... I'm finalizing the key claims for the paper—the 31% temporal instability finding holds across all six benchmarks and isn't explained by the modest capability improvements we're seeing, which I've validated through a semi-synthetic framework that shows zero false positive inflation. The meta-critique and diagnostic audit protocol are solid contributions, while the GSM1K correlation analysis and IRT misfit discussion belong in the appendix and limitations respectively. I've confirmed that dropping those earlier experiment variants was the right call, and I'm being transparent about the RL robustness sample size and the permutation null test that definitively rules out the "above chance" interpretation.

Now I'm reviewing how all the robustness checks form a complete evidence chain—from the permutation null through threshold sensitivity, decomposition analysis, neural network matching, circularity ablation, and multi-benchmark validation. I'm also planning a comprehensive MH-DIF analysis on the full METABENCH MMLU response matrix that would examine temporal and ability cohorts while controlling for within-family confounds and domain-specific effects, with expected temporal instability rates around 31% for the C-level items.

Examining the detailed metrics from this analysis—the mean absolute delta values for C-level items, the enrichment patterns across ability cohorts, the differential rates between model families like Llama and Mistral, and the domain-specific variation where moral scenarios show the highest instability at 48.4% while college biology shows the lowest at 20.7%. The 61.3% within-family consistency across Llama versions confirms genuine architectural changes, and the near-perfect enrichment score makes sense given that web-overlap labels can't capture the nuanced contamination differences we're seeing. I'm organizing the key results into tables showing temporal DIF patterns by ETS class, domain-specificity rankings across the 57 subjects, and cross-model comparisons with Jaccard overlap metrics, along with visualizations of the effect size distributions.

The core finding is that 31.3% contamination rate represents a >170x enrichment over random splits, with temporal factors driving most of this signal—though the modest correlation between subject-level contamination and accuracy gains (ρ=0.307) suggests item-level variation is the primary mechanism rather than broad domain effects.

Now I'm looking at validation results across different model families: the DIF approach maintains strong robustness with alignment-RL models showing 30.8% contamination detection and 94% retention of the core signal, while reasoning-RL models are being evaluated separately. Now I'm looking at the detector performance metrics across different models—the AUROC scores show meaningful drops when applying reinforcement learning compared to the supervised baseline, with statistical significance confirmed by the DeLong test p-values. The power analysis reveals how exploitation rates scale with true positive rates, and I'm checking equivalence testing to validate the findings. The per-model detectors show significant performance degradation on reasoning-RL models due to how GRPO/PPO training contracts the NLL gaps, but with only 13 samples the statistical power is limited—the TOST test is marginally significant with wide confidence intervals, which honestly reflects the underpowered nature of this comparison and should be disclosed in the limitations section. I'm documenting the supporting tables comparing detector performance across model types and DIF flag stability metrics, along with figures showing the AUROC distributions. Moving this to the appendix as a limitation rather than a main contribution. Now I'm setting up the ConStat perturbation evaluation—reformulating 250+ MMLU items to test semantic equivalence detection, with expected flagging rates around 17-19% for non-RL models dropping to 14-15% for alignment-trained ones, and checking false discovery rates after correction.

Comparing ConStat's detection performance against DIF methods, I'm seeing lower Jaccard overlap (0.24) and notably different detection profiles—ConStat catches 19.2% of contaminated cases while DIF identifies 31.3%, partly because ConStat only detects verbatim memorization and misses partial knowledge transfer.

The reformulation process itself introduces construct-irrelevant variance that affects even uncontaminated models, and the RL training's smoothing reduces sensitivity to rephrasing. The AUROC gap (0.68 vs 0.82) shows DIF performs better on semi-synthetic ground truth since the injected contamination simulates differential exploitation rather than exact memorization. These methods are complementary but not additive—they're detecting fundamentally different signal types.

Looking at the supplementary tables and figures, ConStat provides a complementary signal but the low overlap (Jaccard=0.24) means combining them yields minimal ensemble gains. Since the detection mechanisms differ so substantially, merging the approaches wouldn't meaningfully improve performance, which validates the decision to focus on one method rather than pursuing an ensemble strategy.

Now I'm planning an independent evaluation of generation variance across multiple models—testing about a dozen models with fifty responses each to identify items with high variance patterns. The results show roughly 12-15% of items flagged through variance-based detection, but the overlap with DIF is quite low (Jaccard=0.16), suggesting these capture different aspects of model behavior. The low Jaccard similarity of 0.16 reveals that DVD and DIF are detecting almost entirely different contaminated items, which explains the weak ensemble contribution. DVD's AUROC scores are substantially lower than DIF's across both verbatim and variant settings, with the variant detection performing near chance level, suggesting DVD lacks sufficient discriminative power on its own for this task. Now I'm looking at the ensemble fusion approach combining DIF, ConStat, and DVD through majority voting and weighted fusion strategies. The weighted fusion method performs better, assigning higher weights to DIF (0.58) while DVD contributes minimally (0.15), achieving an F1 of 0.43 compared to DIF alone's 0.51 TPR but with improved coverage gains of 4.2 percent. The ensemble approach adds significant computational overhead without meaningful gains—DIF alone achieves higher recall and is more efficient than the consensus-based methods. The fundamental issue is that these three detection mechanisms operate on completely different principles, creating incompatible signals rather than complementary ones, so combining them doesn't improve performance in this LLM benchmark context.

Now I'm planning the GSM8K replication study with semi-synthetic validation to test whether the DIF findings generalize across datasets, examining the contamination gap between GSM8K and GSM1K while tracking the differential functioning metrics across both standard and external reference sets. Looking at the GSM8K results, the temporal contamination is lower than MMLU because the dataset is more homogeneous in a single math domain, so changes concentrate in specific difficulty bands. The semi-synthetic injection shows a stronger effect here, likely because the items are more unidimensional and the contamination is detected more cleanly. The correlation with GSM1K is negative, which actually contradicts the contamination hypothesis—models flagged for more differential item functioning show smaller gaps between GSM8K and GSM1K, suggesting the DIF detection is capturing something different than simple contamination. item 难度跨 cohort 变化），而 GSM1K gap 反映 overall memorization。DIF-C items 78% favor 2024 cohort → 性能提升导致 item functioning 变化，而这些模型恰恰是 contamination gap 较小的（因为 GSM1K 也较难，performance gain 是 genuine capability）。Best tier 处理：demote to appendix as exploratory（N=33, CI wide），不影响 core claims。

GSM8K 复制验证了 framework portability 和 temporal DIF pattern，而 GSM1K correlation 的 negative direction 实际上加强了 Claim 2：DIF 和 contamination ground truth 测量不同东西。这是 expected under the meta-critique framing，所以把它作为 exploratory finding 放入 appendix 是最诚实的处理。

现在转向 MMLU 上的 bifactor IRT equating pilot，验证 equating 可行性。我在看 model fit 指标：unidimensional 模型的 RMSEA 是 0.121，CFI 0.776，TLI 0.771，都不太理想。但 bifactor 5-group 模型改善了——RMSEA 降到 0.094，CFI 升到 0.841，TLI 0.833。不过 bifactor full 57-group 模型没有收敛，Hessian 矩阵在 500 次 EM 迭代后仍然非正定，这说明参数空间太复杂了。anchor selection 部分显示候选 anchor items 中只有 17.3% 是 DIF-free 的。

stability 和 concordance 指标还不错（0.82），需要至少 20 个 anchor items，实际有 2163 个满足条件。equating 部分用 fixed parameter calibration 成功收敛了，但 equated rho 只有 0.91，低于目标的 0.95，差了 0.04。最终这个 pilot 被 killed 了，因为 equated rho 达不到目标，而且 bifactor model 的拟合度也不够好。根本原因是 MMLU 的 57 个 subject 结构让完整的 bifactor 模型（1 个 general factor + 57 个 specific factors）在计算上不可行。

即使用 reduced 5-group bifactor 改进，RMSEA 从 0.121 降到 0.094，CFI 从 0.776 升到 0.841，但仍然远低于可接受的标准（RMSEA<0.05, CFI>0.90）。问题的根源在于 MMLU 本身的多维性——57 个 subject 涵盖从抽象代数到世界宗教的极端异质领域，单一的 general factor 无法捕捉这种结构。即使 anchor items 足够多（17.3% 无 DIF），fixed-parameter calibration 后的 equated score correlation 仍然只有 0.91。

现在看到这个方向的 0.04 shortfall 来自于 misspecified ability estimates 在 calibration 中的传播。最合理的决策是放弃这个方法，把它作为 future work 中多维 IRT 研究的动机。我准备了对比表格展示单维和双因子模型的拟合指标，以及 equating pilot 的 anchor 选择标准和结果，还有示例图表对比 anchor items 和 DIF items 在双因子模型下的表现。这个 negative result 其实很有信息量——它经验性地说明了为什么传统心理测量 equating 不能直接应用到这类大规模多学科评估上。

双因子 IRT equating 在 MMLU 上行不通的根本原因是这类基准测试存在极端的多维性，违反了双因子模型的本质单维性假设，而且 LLM 的反应模式也违反了局部独立性假设。这个 negative result 反而强化了论文的叙述逻辑，成为 limitations 和 future work 部分的自然切入点。接下来要处理 DIF 标记的 MMLU 题目，通过生成替代题目并进行校准来改进——计划生成 400 道题目覆盖 10 个学科，用 GPT-4 生成并确保构念约束的一致性达到 0.87。

但难度校准是核心瓶颈：生成的题目难度与目标难度的相关性只有 0.52，远低于 0.75 的目标，人工评估的质量评分也只有 3.2 而目标是 4.0，这表明 LLM 生成的题目在难度分布上难以精确控制。 制。Prompt-based targeting shows extremely weak correlation (rho=0.38) because LLMs don't calibrate well to what's actually difficult for other LLMs, while student simulation improves this to rho=0.52 by modeling response patterns, though its reported r=0.75-0.82 comes from human exams where difficulty drivers differ from LLM benchmarks. The construct fidelity issue is significant too—22% of generated items miss the target cognitive level or drift in subject matter.

After Plan_005 was abandoned, this approach lost its equating framework foundation and underperformed, so it was rightfully dropped. Looking at the supporting data on difficulty calibration and the scatter plots comparing predicted versus empirical difficulty, the core finding is clear: current item generation and calibration techniques can't reach psychometric-grade quality, which is a valuable negative result showing that simply regenerating flagged items isn't a trivial fix and strengthens the paper's diagnostic framing around DIF's real value in understanding institutional patterns.

When reviewers ask what to do about the 31% unstable items, the answer isn't automated regeneration but rather an audit protocol with informed benchmark maintenance. Now I'm setting up a cumulative Bayesian DIF simulation following Sinharay et al. (2006) across four administrations with 500 items, 200 models per administration, and 100 true DIF items with delta values ranging from 0.8 to 1.8, examining power gains across each administration.

Compiling the power metrics across administrations... For smaller effects like δ=0.8 where a single administration wouldn't detect anything, accumulating evidence across four assessments gets us to 0.65 TPR—this is the real value of the monitoring approach, letting benchmark maintainers build a case gradually rather than needing to catch everything at once. I'll put the simulation details in the appendix to support the monitoring frequency recommendations, and create tables and figures showing how power accumulates across administrations at different effect sizes.

Now I'm analyzing how benchmark validity degrades gracefully as items get progressively replaced, looking at metrics like ranking stability and construct coverage across different replacement percentages. Now I'm looking at how the 31% item removal compares to the plan_017 baseline—the ranking correlation stays above 0.996, which matches the theoretical predictions almost exactly. The Spearman-Brown formula predicted a reliability drop from 0.993 to around 0.982 when shortening the test by 31%, and that's precisely what the empirical results show, indicating the degradation comes entirely from the test length reduction rather than item selection effects.

The removal pattern follows a monotonic concave curve where the first 20% of items have almost no impact on ranking stability, then degradation accelerates gradually afterward. Construct coverage drops more steeply because DIF items cluster unevenly across domains—moral scenarios account for nearly half the DIF items while college biology has only about 21%—so removing high-DIF domains disproportionately affects coverage, though this doesn't compromise the overall ranking validity.

The graceful degradation directly validates the core finding that 31% item instability doesn't threaten benchmark validity since the ranking correlation stays at 0.997, which reflects MMLU's massive redundancy across items. This redundancy is why the benchmark can tolerate such high instability—the information overlap between items is substantial enough to preserve ranking integrity even with significant item replacement.

Now I'm looking at the item-focused trees analysis using continuous time DIF detection as a robustness check against the Mantel-Haenszel approach. The model uses release date as a covariate with moderate tree depth, analyzing over 12,000 items and flagging about 28.7% for differential functioning. The temporal split concordance with Mantel-Haenszel is 0.83, and the Jaccard overlap is 0.78, meaning the two methods agree on most flagged items but each catches some unique cases. The temporal patterns show most items have a single changepoint around September 2023, with about 17% showing gradual drift rather than sharp transitions.

The key advantage of this approach is that it identifies the exact timing of when differential functioning emerges, avoids arbitrary temporal splits, and handles nonlinear patterns better than Mantel-Haenszel. The 28.7% flagging rate versus Mantel-Haenszel's 31.3% reflects the difference in how thresholds are applied—item-focused trees require significance at the node level rather than testing each item independently, which is more conservative but captures the same core signal.

Most items show a single changepoint clustering around September 2023, coinciding with major model releases like Llama-2, Mistral, and Phi-1, while some exhibit progressive drift or gradual shifts without sharp breaks. This temporal granularity is something Mantel-Haenszel simply cannot provide since it only flags items as differentially functioning or not. While Mantel-Haenszel's simplicity and established validity make it the primary method, this approach serves as a useful robustness check that confirms the categorical split captures the main signal.

Now I'm looking at the supplementary tables and figures that document the changepoint distributions by quarter alongside model release events, plus example trajectories showing the different drift patterns. The key insight is that IFT validates Mantel-Haenszel's robustness while adding temporal precision about what's driving the instability—the September 2023 median changepoint aligns with the model release timeline, which I can cross-reference in the discussion section.

For the architecture stratification analysis, I'm examining whether decoder-only models drive the DIF patterns. The dataset is heavily skewed toward decoder-only architectures (99.98%), and the results show that restricting to decoder-only models produces identical DIF classifications and IRT fit statistics compared to the full sample, indicating architecture isn't a confounding factor. I'm preparing a direct rebuttal to the potential reviewer concern that architectural differences could explain the IRT misfit—by showing that the dataset is overwhelmingly decoder-only and removing the single encoder-decoder model doesn't change any results, I can definitively rule out architecture heterogeneity as a confound and redirect the actual issue to MMLU's inherent multidimensionality across 57 subjects.

Now I'm designing a semi-synthetic contamination validation study where I inject varying levels of contamination into a clean response matrix to assess how well DIF detection methods can identify compromised items, testing exploitation rates from 0% to 100% on a focal group of 807 models from the first half of 2024 and measuring both false positive and true positive rates across different contamination intensities. The key insight is that the choice of matching variable dramatically affects false positive rates—when using the contaminated total score in standard Mantel-Haenszel matching, the FPR inflates from 0.298 to 0.616, but switching to cross-subject matching with uncontaminated scores from other subjects completely eliminates this inflation. This methodological finding is the core novelty of the claim: cross-subject matching solves the within-subject contamination problem. The dose-response pattern across probability levels (0.3 through 1.0) showing TPR increasing from 0.55 to perfect detection strengthens the causal interpretation.

Now I'm examining the validation tables and figures that quantify this effect—the semi-synthetic data shows a headline improvement of +0.508 in TPR at the 0.5 exploitation rate, which falls squarely in the optimal range, and the comparison visualizations demonstrate how standard matching produces inflated false positives while cross-subject matching maintains stability across different contamination levels.

The key methodological win here is achieving zero FPR inflation with cross-subject matching, which directly addresses the contaminated matching variable problem, and the dose-response pattern strengthens the internal validity of these findings. I'm now looking at temporal DIF validation across six benchmarks—MMLU, Winogrande, and others—to verify that this approach generalizes across different datasets and time periods. Looking at the summary metrics across all six benchmarks, the consistency is striking—temporal DIF effects range from 17.9% to 31.3%, all random controls stay below 1%, and enrichment ratios span 44.8x to 174x, confirming that temporal item instability is a widespread phenomenon affecting LLM benchmarks generally. 现在我看到了表格结构和图表描述，这些都在支撑跨基准的一致性分析。6个基准的C%范围17.9-31.3%展示了DIF信号的稳健性，所有随机对照都低于1%，这直接回应了关于仅用MMLU和GSM8K的担忧，将可泛化性证据从2个基准扩展到6个。

接下来我需要建立排列检验来验证这31.3%的观察值是否显著——通过1000次排列测试在标签随机打乱下生成零分布，保持参考组和焦点组的大小不变，然后计算z分数和p值来量化观察到的效应相对于零假设的极端程度。 The small difference between the permutation null (0.21%) and random split (0.18%) comes down to sample size—the permutation test uses the full dataset while the random split operates within a single cohort. The observed 31.3% DIF rate yields a z-score of 282.6, which is astronomically significant, and with zero permutations exceeding this value out of 1000, I get an empirical p-value below 0.001. This directly answers the reviewer's question: the temporal structure produces a DIF rate that's 149 times higher than chance. The permutation null is more rigorous than the random split because it directly tests whether the temporal label assignment matters, rather than just checking within-cohort variation. Now I'm setting up the regression transparency analysis with odds ratios, confidence intervals, and model fit statistics — comparing a domain-only model against one that includes item-level decomposition to show how much explanatory power comes from the individual items versus the aggregate domain effect. The four-model regression reveals Simpson's paradox: when looking at domain-level accuracy alone, the relationship between DIF and improvement is positive (OR=1.55), but once I control for item properties like difficulty and discrimination, this reverses to a negative relationship (OR=0.73), suggesting these item characteristics are confounding the original association. 的 methodological insight：只看 domain-level 的分析会导致错误结论。我在准备补充材料，包括四个模型的 logistic regression 结果表、Simpson's paradox 的对比展示，以及所有预测变量的森林图。关键发现是 naive 的 domain-level 分析会高估 accuracy improvement 的作用（OR=1.55），但一旦控制了 item properties 后系数就会反向。

这个 Simpson's paradox 现象说明 improvement 实际上与 DIF 呈负相关，强化了"DIF 主要是 item-specific"的论点。我会用 Model 1 作为主要结果（更保守），Model 2 和 4 作为补充来解释这个悖论。

现在我需要确认一下实验清单——用户要求的是 experiment_plan 中列出的实验，那就是 plan_001 到 plan_011、plan_028 到 plan_030，共 16 个实验。

我已经全部覆盖了。

让我再检查一遍 YAML 的格式和嵌套结构是否正确，特别是引号和缩进。对于已完成的实验，我用的是 registry 中的实际指标；对于 plan_010，用的是 paper_framing 中的描述。每个实验的 result_rationale 都要清楚地解释为什么在最佳情况下会得到这样的结果。

Generating YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dad59d39-e6ed-4a12-bfbb-b9482b2c7221",
  "isSidechain": false,
  "requestId": "req_011CbFiDhS11djC1JTfjutDG",
  "type": "assistant",
  "uuid": "688c8b2d-002c-4d31-a643-9956360460ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Mx9r5b9vN9JjmbXukcnU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20729,
      "cache_read_input_tokens": 11841,
      "output_tokens": 36953,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 36953,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20729
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

_source line 9 · 2026-05-21T12:38:56.319Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立，四条 claim 无需调整强度。Headline: '31% temporal instability across 6 benchmarks,
  not explained by capability improvement (≤7.6%), validated by semi-synthetic framework with 0 FPR inflation.'
  Meta-critique 作为 aggressive contribution 直接成立。Diagnostic lens + audit protocol 作为 actionable 贡献。
  GSM1K correlation 留 appendix 作为 exploratory。IRT misfit 在 limitations 一笔带过。
  Dropped experiments (003a/b/c, 005, 006) 结果确认 pivot 正确性——ensemble coverage gain 不足，
  bifactor fit 不达标，item generation calibration below benchmark。plan_002 RL robustness N=13
  在 limitations 诚实披露。plan_029 permutation null 彻底封堵 'is 31% above chance?' 质疑。
  全部 robustness check 干净通过，证据链闭环：permutation null → threshold sensitivity → decomposition
  → NN matching → circularity ablation → multi-benchmark 六层。

imagined_experiments:

  - name: "real_data_dif_mmlu"
    plan_id: "plan_001"
    description: "METABENCH MMLU 5219×12508 response matrix MH-DIF 全量分析：temporal/ability cohort、within-family confound control、domain-specificity"
    expected_results:
      temporal_cohort:
        n_ref_2023: 1080
        n_foc_2024h1: 807
        ets_c_pct: 31.3
        ets_b_pct: 18.2
        ets_a_pct: 50.5
        n_c_items: 3918
        mean_abs_delta_mh_c_items: 2.31
      ability_cohort:
        ets_c_pct: 2.9
        enrichment: 1.19
      within_family:
        llama2_vs_llama3_c_pct: 61.3
        mistral_vs_mixtral_c_pct: 38.7
      domain_specificity:
        spearman_rho_c_pct_vs_acc_delta: 0.307
        spearman_p: 0.02
        highest_c_pct_subject: "moral_scenarios (48.4%)"
        lowest_c_pct_subject: "college_biology (20.7%)"
        unweighted_mean_c_pct: 30.0
      sanity_checks:
        random_split_c_pct: 0.18
        temporal_ability_jaccard: 0.014
      li_et_al_proxy:
        coverage: 0.738
        enrichment_temporal: 0.96
        fpr_on_li_clean: 0.318
    result_rationale: >
      31.3% C% 反映 genuine temporal item-level functioning changes。三层确认非伪影：
      (1) random split 仅 0.18%（>170x enrichment ratio 排除统计伪影）；
      (2) ability cohort C%=2.9%（DIF 由 temporal structure 驱动，非 ability grouping）；
      (3) temporal-ability Jaccard=0.014（两种 cohort 几乎 flag 完全不同的 items）。
      Domain ρ=0.307 (p=0.02) 是 modest ecological correlation；后续 plan_019 item-level
      decomposition 证明 domain improvement 仅解释 7.6%。Within-family Llama-2→3 的 61.3%
      反映跨代 capability jump（d=-0.99, plan_027），而非 contamination artifact——
      同一架构族内 item functioning 剧烈变化说明 capability evolution 是 contributor 之一。
      Li et al. enrichment≈0.96 在 meta-critique framing 下是 expected：web-overlap 是 model-agnostic
      label，DIF 检测的是 model-cohort-differential signal，二者正交。
    tables:
      - "Table 1: Temporal DIF summary — N_ref=1080, N_foc=807, %A/B/C by ETS class, mean |Δ_MH|"
      - "Table 2: 57-subject domain-specificity — per-subject C%, accuracy delta, sorted descending"
      - "Table S1: Within-family DIF — Llama-2v3 (N=161 vs 308), Mistral-Mixtral, C%, Jaccard with temporal"
    figures_description:
      - "Fig 1: |Δ_MH| 分布直方图（12,508 items），ETS A/B/C threshold 标注；inset 展示 random-split null 分布"
      - "Fig 2: Subject-level C% vs accuracy improvement 散点图（ρ=0.307），含 95% CI band 和 57 subject labels"
    analysis: >
      31.3% 是 paper 的 anchor number。Random split 0.18% 建立了 chance baseline（plan_029 permutation
      null 将进一步强化）。Ability cohort 的 2.9% 排除了 ability grouping 作为 confound。Domain ρ=0.307
      说明 "模型在某些 domain 进步更多" 是 factor 之一，但不是主要因素——item-level decomposition
      (plan_019/030) 证明 DIF 主要是 item-specific。Within-family Llama-2→3 的 61.3% 提供了
      capability evolution 的 direct evidence，同时为 plan_027 ability confound 分析铺垫。

  - name: "rl_robustness_validation"
    plan_id: "plan_002"
    description: "DIF 对 alignment-RL 和 reasoning-RL 模型的鲁棒性验证，含 per-model detector 对比和 power analysis"
    expected_results:
      alignment_rl_cohort:
        n_dpo_orpo_models: 477
        temporal_c_pct_with_alignment_rl: 30.8
        jaccard_vs_full_temporal: 0.87
        dif_retention_ratio: 0.94
      reasoning_rl_addition:
        n_reasoning_rl_models: 13
        models_tested: "DeepSeek-R1-7B, DeepSeek-R1-32B, Qwen2.5-RL-7B/14B/32B, Eurus-RL-7B, PRIME-RL-7B, SimpleRL-7B, DAPO-7B, K1.5-RL, TinyZero-3B, DeepScaleR-1.5B, OpenChat-RL"
        temporal_c_pct_with_rl_added: 31.1
        jaccard_vs_full_temporal: 0.93
        c_pct_delta_from_baseline: -0.2
      per_model_detectors:
        constat_auroc_sft: 0.71
        constat_auroc_alignment_rl: 0.67
        constat_auroc_reasoning_rl: 0.43
        mink_auroc_sft: 0.64
        mink_auroc_alignment_rl: 0.59
        mink_auroc_reasoning_rl: 0.37
        delong_p_constat_sft_vs_reasoning_rl: 0.008
        delong_p_mink_sft_vs_reasoning_rl: 0.003
      power_analysis:
        exploitation_rate_04_tpr: 0.28
        exploitation_rate_06_tpr: 0.47
        exploitation_rate_08_tpr: 0.65
        exploitation_rate_10_tpr: 0.79
      tost_equivalence:
        tost_p: 0.034
        equivalence_margin: 0.05
        ci_90_retention_ratio: [0.89, 0.98]
    result_rationale: >
      Alignment RL (DPO/ORPO) 不使用 PPO clipping，NLL 分布不变，DIF 不受影响（Jaccard=0.87）。
      0.87 而非 1.0 的原因是 alignment RL 模型在 borderline items 上的 response probability 略有
      shift，导致少量 items 在 MH threshold 边缘翻转。13 个 reasoning-RL 模型仅占 focal cohort 1.6%，
      加入后 C% 几乎不变（31.1% vs 31.3%），因为 MH 是 group-level 统计量——少量个体对 N=807 的
      odds ratio 影响可忽略。传统 per-model detectors 在 reasoning-RL 上 AUROC 大幅下降（ConStat 0.71→0.43,
      Min-K% 0.64→0.37），因为 GRPO/PPO 训练 contracts NLL gaps（Wang et al. 机制），而 DIF
      的 group-level conditioning 天然免疫此问题。但 N=13 使 TOST p=0.034 仅 marginal significant，
      bootstrap CI 宽（[0.89, 0.98]）。Best tier 处理：direction consistent，但诚实地在 limitations
      中报告 N=13 underpowered，不作为 numbered contribution。
    tables:
      - "Table S2: Per-model detector AUROC — SFT vs alignment-RL vs reasoning-RL，含 bootstrap 95% CI 和 DeLong test"
      - "Table S3: DIF flag stability across cohort compositions — Jaccard, overlap %, new/lost flags"
    figures_description:
      - "Fig S1: AUROC bar chart — DIF (group) vs ConStat vs Min-K% across三种 model populations，含 CI"
      - "Fig S2: Power curve — TPR vs exploitation rate p ∈ [0.4, 1.0]，N=13 reasoning-RL setting"
    analysis: >
      Two-level validation 结论清晰：(1) group-level DIF robust to RL composition（Jaccard≥0.87）；
      (2) per-model detectors fragile to reasoning RL（AUROC drops 0.25-0.27 points）。
      这支持 DIF 的 structural advantage 叙事但 N=13 不足以做 standalone claim。
      结论：appendix + limitations，为 future work 留出空间。

  - name: "constat_perturbation_eval"
    plan_id: "plan_003a"
    description: "ConStat 风格 perturbation testing——250 MMLU items 的语义等价重述 + 检测 power 评估"
    expected_results:
      reformulation:
        n_items_reformulated: 250
        semantic_similarity_mean: 0.92
        n_models_tested: 50
      detection:
        constat_flagged_pct_non_rl: 19.2
        constat_flagged_pct_all: 17.8
        fdr_corrected_flagged_pct: 12.3
      comparison_with_dif:
        jaccard_constat_vs_dif_c: 0.24
        overlap_pct: 38.2
        constat_only_pct: 8.1
        dif_only_pct: 22.4
      power_on_semi_synthetic_gt:
        constat_auroc: 0.68
        dif_auroc: 0.82
    result_rationale: >
      ConStat 检测 reformulation sensitivity——contaminated 模型对 verbatim 题回答正确但对 rephrased
      版性能下降。19.2% 低于 DIF 31.3%，因为：(1) ConStat 仅覆盖 verbatim memorization，partial/variant
      contamination 不敏感；(2) MMLU 4-choice format 下 reformulation 的 accuracy drop 天然受限
      （chance level 25% 提供 floor）；(3) 高质量 paraphrase 的 surface form 变化可能不足以触发
      memorization-dependent 模型的 performance shift。Jaccard=0.24 confirms 两种方法检测不同
      signal types——DIF 是 temporal differential functioning，ConStat 是 memorization-specific
      sensitivity。Semi-synthetic ground truth 上 DIF AUROC 更高（0.82 vs 0.68），因为 injected
      contamination 是 differential exploitation（与 DIF 检测机制对齐），而非 verbatim memorization
      （与 ConStat 对齐）。结论：complementary but not additive，验证了 ensemble pivot 的正确性。
    tables:
      - "Table S4: ConStat detection — flagged % by model class，含 FDR correction"
      - "Table S5: DIF × ConStat cross-tabulation — Jaccard, Phi, overlap"
    figures_description:
      - "Fig S3: Venn diagram — DIF-C items vs ConStat-flagged items"
    analysis: >
      ConStat 提供 complementary signal 但 Jaccard=0.24 说明 ensemble marginal gain 有限。
      Detection mechanism 差异（temporal differential vs memorization sensitivity）使两种方法
      检测近乎正交的 item 子集。此结果验证 pivot：DIF 作为 diagnostic lens 的独特价值不可被
      ConStat 替代，ensemble 不如 DIF alone + robustness checks 有效。

  - name: "dvd_generation_variance_eval"
    plan_id: "plan_003b"
    description: "DVD generation variance 评估——12 open-weight models × 50 responses per item 的 variance-based 检测"
    expected_results:
      setup:
        n_models_tested: 12
        n_responses_per_item: 50
        temperature: 0.8
        total_inferences: 7512000
        gpu_hours: 69.6
      detection:
        bimodal_items_pct: 11.8
        high_variance_items_pct: 15.3
        dvd_flagged_pct: 13.2
      comparison_with_dif:
        jaccard_dvd_vs_dif_c: 0.16
        overlap_pct: 29.4
      power:
        dvd_auroc_verbatim_gt: 0.61
        dvd_auroc_variant_gt: 0.53
    result_rationale: >
      DVD 依赖 contaminated items 产生 bimodal generation distribution（memorized answer vs random）。
      11.8% bimodal 低于 DIF 31.3%，因为：(1) bimodality 仅在 extreme verbatim memorization 下出现，
      partial exploitation 产生 unimodal 但 shifted distribution；(2) MMLU 4-choice format 的 discrete
      nature 限制了 generation variance 的 discriminative range——even uncontaminated items 在
      temperature sampling 下产生 high variance；(3) requires open-weight access，排除 proprietary
      models。Jaccard=0.16 极低，confirms DVD 和 DIF 检测几乎完全不同的 item subsets。
      AUROC 对比：DVD verbatim 0.61（moderate），variant 0.53（near chance）。Variant contamination
      detection 接近 chance 因为 paraphrased memorization 不产生 bimodal pattern。
    tables:
      - "Table S6: DVD detection — bimodal %, flagged % by model"
      - "Table S7: DVD vs DIF cross-tabulation"
    figures_description:
      - "Fig S4: Example bimodal vs unimodal generation distributions for selected items"
    analysis: >
      DVD 单独使用 power 不足，且需要 ~70 GPU hours + open-weight access。
      Jaccard=0.16 说明 ensemble 增益极小。结果验证了 ensemble pivot 正确性：
      三种方法的 detection mechanisms 过于异质，无法有效融合。

  - name: "ensemble_fusion"
    plan_id: "plan_003c"
    description: "DIF + ConStat + DVD 三信号融合：majority voting + weighted fusion"
    expected_results:
      majority_voting_2of3:
        tpr: 0.35
        fpr: 0.08
        f1: 0.38
      weighted_fusion:
        optimal_weights: {dif: 0.58, constat: 0.27, dvd: 0.15}
        tpr: 0.43
        fpr: 0.09
        f1: 0.43
        cross_val_weight_cv: 0.34
      dif_alone_reference:
        tpr: 0.51
        fpr: 0.31
      coverage_gain_over_dif_pp: 4.2
      all_ensemble_fpr_below_010: true
    result_rationale: >
      2-of-3 majority voting TPR 仅 0.35，因为 pairwise Jaccard 0.16-0.24 导致三方法 consensus
      items 极少——三种方法各自检测不同 signal（temporal differential, memorization sensitivity,
      generation bimodality），overlap 不足以构建有效 consensus。Weighted fusion 略好（TPR=0.43）
      但 cross-validation weight stability 差（CV=0.34），因为 calibration set 有限（semi-synthetic
      ground truth 200 items）且三种方法 error profiles 不 correlated。DIF alone TPR=0.51 高于
      任何 ensemble configuration，因为 high-recall 方法被 ensemble consensus requirement 削弱。
      Coverage gain 仅 +4.2pp 不 justify 额外 150 GPU hours 和 open-weight 依赖。
    tables:
      - "Table S8: Ensemble configs — 2-of-3, weighted, DIF-alone，含 95% CI"
    figures_description:
      - "Fig S5: ROC curves — DIF alone vs 2-of-3 vs weighted fusion"
    analysis: >
      Ensemble 核心问题是三种方法的 signal incommensurability 而非 signal complementarity。
      Best tier 下此 negative result 加强了 pivot 叙事：DIF 的 diagnostic lens 价值在于其
      独特的 temporal-differential perspective，不需要也不应与其他 mechanism 融合。
      Goes to appendix as informative negative result。

  - name: "cross_benchmark_gsm8k"
    plan_id: "plan_004"
    description: "GSM8K DIF 复制 + semi-synthetic 验证 + GSM1K contamination gap 相关"
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
        standard_delta_tpr_p05: 0.508
      step3_gsm1k_correlation:
        n_models: 33
        pearson_r: -0.478
        pearson_p: 0.005
        spearman_rho: -0.403
        spearman_p: 0.02
        partial_r_controlling_accuracy: -0.385
        partial_p: 0.027
        permutation_p: 0.014
        direction: "NEGATIVE — opposite to contamination hypothesis"
        leave_one_out_r_range: [-0.537, -0.374]
    result_rationale: >
      GSM8K temporal C%=18.9% 低于 MMLU 31.3%，因为 GSM8K 是 single math domain（1,319 items），
      item 功能相对 homogeneous，temporal change 集中在特定难度段而非 broad capability shift。
      Semi-synthetic ΔTPR=+0.818 高于 MMLU 0.674，因为 GSM8K 更 unidimensional（单一 math 能力维度），
      MH 的 unidimensional conditioning 更 appropriate，injection 更 cleanly detected。
      GSM1K correlation r=-0.478 方向 opposite to contamination hypothesis：DIF 更多 flag 的模型
      有更小的 GSM8K-GSM1K gap。这并不矛盾——DIF flags items whose difficulty changed across cohorts
      （78% favor 2024），而 small GSM8K-GSM1K gap 的模型恰恰是 genuine capability improvement
      最强的（GSM1K 也难，real ability gains transfer）。This anti-correlation 实际上加强了
      Claim 2 meta-critique：DIF 和 contamination ground truth 测量的是 different constructs。
    tables:
      - "Table 4: GSM8K temporal DIF — C% with standard/external matching, random control"
      - "Table S9: GSM1K correlation — Pearson/Spearman/partial r，含 leave-one-out robustness"
    figures_description:
      - "Fig 3: GSM8K semi-synthetic ΔTPR dose-response curve (p=0.3 to 1.0)，含 95% bootstrap CI"
      - "Fig S6: GSM1K gap vs DIF-C proportion scatter (N=33)，注明 exploratory"
    analysis: >
      GSM8K 复制验证 framework portability（ΔTPR=+0.818）和 temporal DIF pattern（18.9% vs random 0.3%）。
      GSM1K negative correlation 在 best tier 下 demote to appendix exploratory（N=33, CI wide）。
      This result doesn't weaken any claim — it strengthens the meta-critique by empirically
      demonstrating DIF and contamination labels capture different signals。

  - name: "bifactor_irt_equating_pilot"
    plan_id: "plan_005"
    description: "Bifactor IRT equating pilot——验证 MMLU 上 psychometric equating 可行性"
    expected_results:
      model_fit:
        unidimensional_rmsea: 0.121
        unidimensional_cfi: 0.776
        bifactor_5group_rmsea: 0.094
        bifactor_5group_cfi: 0.841
        bifactor_full_57_convergence: false
        bifactor_full_57_error: "non-positive definite Hessian after 500 EM iterations"
      anchor_selection:
        dif_free_items_pct: 17.3
        n_anchors_meeting_criteria: 2163
        anchor_icc_concordance: 0.82
      equating_attempt:
        equated_rho: 0.91
        target_rho: 0.95
        shortfall: 0.04
      decision: "KILLED — bifactor fit insufficient (RMSEA=0.094>0.05), equated rho=0.91 < target 0.95"
    result_rationale: >
      MMLU 57-subject 结构使 full bifactor（1 general + 57 specific）在计算上不可行——
      non-positive definite Hessian 因为 57 specific factors 导致 identification 问题（many subjects
      仅 100 items，insufficient for factor estimation）。Reduced 5-group bifactor 改善有限
      （RMSEA 0.121→0.094, CFI 0.776→0.841），仍远低于 acceptable fit thresholds。根本原因是
      MMLU 内在 multidimensionality：从 abstract_algebra 到 world_religions 的 57 domains 无法
      被 1 general factor + few group factors 充分 capture。Equating pilot 在 suboptimal fit 下
      仍尝试：anchors 数量足够（2,163 items），但 misspecified ability estimates 传播到
      fixed-parameter calibration，导致 equated rho=0.91 低于 target 0.95。Kill decision 正确——
      此 negative result 在 limitations 中作为 future multidimensional IRT work 的 motivation。
    tables:
      - "Table S10: IRT fit comparison — unidimensional vs 5-group bifactor vs full bifactor"
    figures_description:
      - "Fig S7: Item characteristic curves — anchor items vs DIF items under bifactor model"
    analysis: >
      Informative negative result。说明传统 psychometric equating 不能直接迁移到 LLM multi-domain
      benchmarks：extreme multidimensionality violates essential unidimensionality assumption。
      加强 diagnostic lens framing——DIF 的价值不在于 equating-based item replacement，
      而在于 understanding what changed。在 limitations 中自然 motivate future multidimensional IRT。

  - name: "item_generation_calibration"
    plan_id: "plan_006"
    description: "DIF-flagged MMLU items 的 LLM-based 替代 item 生成与难度校准"
    expected_results:
      generation:
        n_items_generated: 400
        n_subjects: 10
        construct_adherence_human_eval: 0.784
      difficulty_calibration:
        prompt_based_rho: 0.38
        student_sim_rho: 0.52
        target_rho: 0.75
      quality:
        human_quality_score_mean: 3.2
        human_quality_target: 4.0
        holdout_panel_rho: 0.48
      decision: "BELOW BENCHMARKS — best difficulty rho=0.52 vs target 0.75"
    result_rationale: >
      Difficulty calibration 是 item generation 的瓶颈。Prompt-based targeting（直接指定 difficulty level）
      rho=0.38，因为 LLM 对 "difficulty for other LLMs" 的 internal calibration 与 empirical difficulty
      几乎无关——difficulty 由 knowledge coverage, reasoning depth, distractor quality 联合决定，
      非 LLM 自身 uncertainty 可预测。Student simulation 改善到 rho=0.52，但 arXiv 2601.09953 的
      r=0.75-0.82 是在 human exam items 上报告的，LLM benchmark items 的 difficulty determinants
      不同（e.g., MMLU 多选的 distractor 设计对 LLM 和 human 的 difficulty contribution 不同）。
      Construct fidelity 78.4% 说明 22% 的 generated items 有 subject drift 或 cognitive level 错误。
      Plan_005 被 kill 后，本 plan 失去 equating framework 支撑。
    tables:
      - "Table S11: Difficulty calibration — prompt vs student-sim vs empirical，含 95% CI"
    figures_description:
      - "Fig S8: Predicted vs empirical difficulty scatter（prompt-based 和 student-sim 两组）"
    analysis: >
      有价值的 negative result——说明 "just regenerate flagged items" 不是 trivial solution。
      加强 diagnostic lens framing：DIF 的 actionable value 是 audit protocol + informed maintenance，
      而非 automated regeneration。在 Discussion 中可用于回应 reviewer 的 "so what do we do?" question。

  - name: "cumulative_bayesian_dif"
    plan_id: "plan_007"
    description: "Sinharay et al. (2006) cumulative Bayesian DIF priors 的 4-administration simulation"
    expected_results:
      setup:
        n_administrations: 4
        n_items_per_sim: 500
        n_models_per_admin: 200
        true_dif_items: 100
        delta_range: [0.8, 1.8]
      power_accumulation:
        tpr_admin1_d10: 0.41
        tpr_admin2_d10: 0.58
        tpr_admin3_d10: 0.72
        tpr_admin4_d10: 0.81
        tpr_admin1_d08: 0.22
        tpr_admin2_d08: 0.38
        tpr_admin3_d08: 0.53
        tpr_admin4_d08: 0.65
      fpr_stability:
        fpr_range: [0.042, 0.045]
      bayesian_shrinkage:
        posterior_sd_admin4: 0.31
    result_rationale: >
      Bayesian evidence accumulation 的 power gain 等价于 effectively increasing sample precision。
      δ=1.0 时单次 TPR=0.41（与 phase2 sim 的 N=80 结果一致），4 次累积达 0.81——posterior SD
      从 1.0 shrink 到 0.31，precision quadruples。对 small effects（δ=0.8），MH 单次几乎无法检测
      （TPR=0.22），但 4 次累积达 0.65——这是 monitoring protocol 的核心理论支撑。
      FPR 稳定在 ~0.043 因为 Bayesian shrinkage 对 null items 同样有效（posterior for null items
      集中在 0 附近）。Simulation-only 但为 audit protocol 的 monitoring frequency 建议提供
      quantitative basis。
    tables:
      - "Table S12: Cumulative power — TPR at δ=0.8/1.0/1.4/1.8 × 1-4 administrations"
    figures_description:
      - "Fig S9: Power accumulation curves — TPR vs N administrations for different δ"
    analysis: >
      Clean simulation 支持 audit protocol 的 operational recommendation：每 6 月 DIF assessment，
      3 次累积后 medium effects 的 power 从 0.41 升至 0.72。Goes to appendix，在 Discussion
      中 referenced。

  - name: "graceful_degradation_analysis"
    plan_id: "plan_008"
    description: "Benchmark validity 在 progressive item removal 下的降级分析"
    expected_results:
      progressive_removal:
        pct_5:  {ranking_rho: 0.9998, reliability_alpha: 0.993, construct_jaccard: 0.98}
        pct_10: {ranking_rho: 0.9994, reliability_alpha: 0.991, construct_jaccard: 0.96}
        pct_20: {ranking_rho: 0.9987, reliability_alpha: 0.987, construct_jaccard: 0.92}
        pct_31: {ranking_rho: 0.9965, reliability_alpha: 0.982, construct_jaccard: 0.87}
        pct_50: {ranking_rho: 0.9912, reliability_alpha: 0.971, construct_jaccard: 0.78}
      theoretical_match:
        spearman_brown_predicted_rho_31pct: 0.9968
        empirical_rho_31pct: 0.9965
        gap: 0.0003
    result_rationale: >
      MMLU 12,508 items 的 massive redundancy 决定了 removal 的 graceful degradation。
      Spearman-Brown formula 预测 test length 缩减 31% 时 rho 从 ~1.0 降至 0.9968——
      empirical 0.9965 精确匹配，说明 degradation 完全由 test shortening 驱动，无 systematic
      bias（DIF items 不是 systematically more informative for ranking）。Construct coverage
      降速快于 ranking stability，因为 DIF items 在 domains 间非均匀分布（moral_scenarios 48.4%
      vs college_biology 20.7%），high-DIF domains 在 removal 后 coverage 受损更大。
      与 plan_017 实际结果（rho=0.997 at 31%）高度一致。
    tables:
      - "Table S13: Progressive degradation — rho, reliability, coverage at 5/10/20/31/50%"
    figures_description:
      - "Fig S10: Degradation curves 含 Spearman-Brown theoretical bound overlay"
    analysis: >
      直接支持 "instability ≠ invalidity" 叙事。31% instability 不威胁 validity（rho=0.997）
      因为 MMLU 的 massive redundancy。Headline number 进 main text，full curve 进 appendix。

  - name: "item_focused_trees"
    plan_id: "plan_009"
    description: "Item-Focused Trees（Tutz & Berger 2016）——连续时间 DIF 作为 MH categorical split 的 robustness check"
    expected_results:
      detection:
        ift_flagged_pct: 28.7
        jaccard_ift_vs_mh_c: 0.78
        ift_only_pct: 4.2
        mh_only_pct: 6.8
      temporal_patterns:
        single_changepoint_pct: 71
        multiple_changepoints_pct: 12
        gradual_drift_pct: 17
        median_changepoint: "2023-09"
      tree_structure:
        mean_terminal_nodes: 5.2
        max_depth: 3
    result_rationale: >
      IFT 用 continuous release date 替代 MH 的 binary temporal split，避免 arbitrary cutoff。
      28.7% vs MH 31.3% 的差异来自 tree-based multiple testing correction（node-level significance
      threshold）vs MH 的 per-item testing。Jaccard=0.78 高一致性说明 MH categorical split
      captures the main temporal signal。IFT 的独特 value 是 changepoint timing：71% items 有
      single changepoint（median 2023-09，对应 Llama-2/Mistral/Phi-1 release 密集期），
      12% 有 multiple changepoints（progressive drift），17% gradual drift。Timing information
      支持 Discussion 中的 "what drives instability" narrative——major model releases 是
      item functioning change 的 primary driver。
    tables:
      - "Table S14: IFT vs MH concordance — Jaccard, overlap, unique flags"
      - "Table S15: Changepoint timing distribution by quarter"
    figures_description:
      - "Fig S11: 三种 DIF trajectory 示例——single changepoint, multiple, gradual drift"
    analysis: >
      Confirms MH categorical split robustness（Jaccard=0.78）。Changepoint timing
      提供 temporal granularity，在 Discussion 中简要引用。Appendix robustness check。

  - name: "architecture_stratified_dif"
    plan_id: "plan_010"
    description: "Architecture-homogeneous subpopulation DIF——验证 architecture heterogeneity 非 confound"
    expected_results:
      metabench_composition:
        total_models: 5227
        decoder_only: 5226
        decoder_only_pct: 99.98
        non_decoder: 1
        non_decoder_id: "flan-ul2"
      dif_comparison:
        decoder_only_c_pct: 31.3
        full_c_pct: 31.3
        jaccard: 1.0
        items_changed: 0
      irt_fit:
        full_rmsea: 0.121
        decoder_only_rmsea: 0.121
        delta_rmsea: 0.0
    result_rationale: >
      METABENCH MMLU 的 architecture homogeneity 使本实验成为 trivial pass：99.98% decoder-only，
      唯一的 encoder-decoder (flan-ul2) 在 N=5227 中的影响可忽略。Jaccard=1.0 意味着
      zero items 的 DIF classification 因 architecture stratification 而改变。IRT fit 同样不变
      （RMSEA=0.121），因为 misfit 源自 57-subject multidimensionality 而非 architecture heterogeneity。
      这是 ideal robustness result：potential confound 被 data composition 自然消除。
    tables:
      - "Table S16: Architecture composition"
    figures_description: []
    analysis: >
      One-line main text defense。IRT misfit 重定向至 limitations（multidimensionality motivation）。

  - name: "semi_synthetic_contamination_validation"
    plan_id: "plan_011"
    description: "Known contamination injection 进 real response matrix + DIF detection power 评估 + cross-subject matching 验证"
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
      ability_external_matching:
        baseline_fpr: 0.493
        tpr_p10: 0.800
        delta_tpr_p10: 0.302
      matching_variable_contamination:
        standard_fpr_p10: 0.616
        standard_fpr_baseline: 0.298
        fpr_inflation: 0.318
        cross_subject_fpr_inflation: 0.000
      cross_subject_5subj_validation:
        delta_fpr_all_subjects: 0.000
        avg_delta_tpr_p05: 0.508
        subjects_passing_p05: "4/5"
    result_rationale: >
      Semi-synthetic injection 在 real response matrix 上创造 controlled ground truth——
      对 focal cohort 的 known-clean items 执行 incorrect→correct flipping with probability p。
      ΔTPR=+0.508 at p=0.5 在 best tier [0.45, 0.55] range 内，confirms DIF detects moderate
      differential contamination。Dose-response（p=0.3→0.5→0.7→1.0 对应 TPR 0.55→0.83→0.99→1.0）
      增强因果推断。关键 methodological finding：standard MH matching（total score 含 contaminated items）
      导致 FPR inflation +0.318（matching variable contamination），而 cross-subject matching
      （other subjects 的 total score）完全消除 inflation（ΔFPR=0.000）。Cross-subject matching
      works 因为 contamination 是 subject-specific（inject 进特定 subject），而 other subjects
      的 total score 不受 contamination 影响，保持 conditioning variable 的 exchangeability。
    tables:
      - "Table 5: Semi-synthetic ΔTPR/ΔFPR across exploitation rates and matching strategies"
      - "Table 6: Standard vs cross-subject matching FPR comparison"
    figures_description:
      - "Fig 4: Dose-response — ΔTPR vs p，含 95% bootstrap CI"
      - "Fig 5: FPR comparison — standard (inflates) vs cross-subject (stable)"
    analysis: >
      ΔTPR=+0.508 是 Claim 3 headline。Cross-subject ΔFPR=0.000 是 key methodological novelty。
      Dose-response pattern 提供 internal validity。Both metrics 在 best tier range 内。

  - name: "multi_benchmark_temporal_dif"
    plan_id: "plan_028"
    description: "6 benchmarks temporal DIF——cross-benchmark generalizability 验证"
    expected_results:
      mmlu:       {n_items: 12508, n_ref: 1080, n_foc: 807, pct_c: 31.3, random_pct_c: 0.18}
      winogrande: {n_items: 1267,  n_ref: 1017, n_foc: 803, pct_c: 30.3, random_pct_c: 0.32}
      truthfulqa: {n_items: 817,   n_ref: 1080, n_foc: 807, pct_c: 29.7, random_pct_c: 0.37}
      arc:        {n_items: 1172,  n_ref: 1080, n_foc: 807, pct_c: 26.9, random_pct_c: 0.60}
      gsm8k:      {n_items: 1319,  n_ref: 1017, n_foc: 804, pct_c: 18.9, random_pct_c: 0.30}
      hellaswag:  {n_items: 10042, n_ref: 1080, n_foc: 807, pct_c: 17.9, random_pct_c: 0.28}
      summary:
        range: "17.9–31.3%"
        all_random_below_1pct: true
        min_enrichment_ratio: 44.8
        mean_c_pct: 25.8
        n_benchmarks: 6
    result_rationale: >
      6 benchmarks 一致显示 temporal DIF 远超 chance（enrichment 45-174×），确认 temporal item
      instability 是 LLM benchmark 的 general phenomenon。C% ordering 反映 benchmark 结构：
      MMLU（57 domains, maximal multidimensionality）和 WinoGrande（commonsense reasoning, capability-sensitive）
      最高；HellaSwag（sentence completion, more pattern-matching than reasoning）和 GSM8K
      （single math domain）最低。低 C% benchmarks 的 items 功能更 homogeneous across model generations
      ——sentence completion patterns evolve less than knowledge/reasoning items。
      All random controls <1% 排除 statistical artifact across all benchmarks。
    tables:
      - "Table 3: Cross-benchmark temporal DIF — 6 rows, N_items/N_ref/N_foc/C%/random%"
    figures_description:
      - "Fig 6: Bar chart — C% 降序排列，含 random-split controls，6 benchmarks"
    analysis: >
      Cross-benchmark consistency 是 Claim 1 generalizability 最强证据。17.9-31.3% range 在
      best tier [17.0, 32.0] 内。Claim 1 statement 可升级为 "17.9-31.3% across 6 major benchmarks"。

  - name: "permutation_null_c_rate"
    plan_id: "plan_029"
    description: "1000× permutation test——temporal label shuffling 下的 C% null distribution"
    expected_results:
      null_distribution:
        n_permutations: 1000
        mean_c_pct: 0.21
        sd_c_pct: 0.11
        median_c_pct: 0.19
        q95_c_pct: 0.42
        q99_c_pct: 0.54
        max_c_pct: 0.71
      significance:
        observed_c_pct: 31.3
        z_score: 282.6
        empirical_p: "<0.001 (0/1000 exceed observed)"
        ratio_observed_to_null_mean: 149
      consistency:
        random_split_c_pct: 0.18
        permutation_null_mean: 0.21
        convergent: true
    result_rationale: >
      Permutation null 通过 random temporal label reassignment（保持 N_ref=1080, N_foc=807）
      建立 chance baseline。Mean 0.21% 与 random split 0.18% convergent，因为两者本质上 measure
      the same thing：无 temporal structure 时的 spurious DIF rate。0.21% vs 0.18% 微小差异来自
      permutation 使用 full N=1887（random split 在 single cohort ~1000 内）。Observed 31.3%
      给出 z=282.6——0/1000 permutations exceed，empirical p<0.001。这是因为 temporal structure
      是 genuine signal：2023 和 2024 model cohorts 确实在 item-level functioning 上不同。
      Permutation destroys this temporal structure，restoring C% to chance level (~0.2%)。
      149× enrichment over null 彻底回答 "is 31% above chance?"。
    tables:
      - "Table 7: Permutation null — mean/SD/Q95/Q99/max vs observed，z-score，p-value"
    figures_description:
      - "Fig 7: 1000 permutation C% histogram 含 observed 31.3% 标注（far right arrow，截断 x 轴）"
    analysis: >
      Best tier 的 critical robustness check。Null C% mean=0.21% 在 [0.0, 1.0] range 内。
      z=282.6 使 temporal DIF signal 成为 unambiguous。与 random-split 的 convergence 提供
      double confirmation。This goes into main text as primary robustness evidence alongside
      threshold sensitivity（plan_018）and decomposition（plan_019）。

  - name: "odds_ratio_regression_transparency"
    plan_id: "plan_030"
    description: "多层 logistic regression——OR + CI + McFadden/Nagelkerke R² + Simpson's paradox 展示"
    expected_results:
      model1_domain_delta:
        mcfadden_r2: 0.0007
        nagelkerke_r2: 0.0012
        aic: 15545.2
        or_per_010: 1.55
        or_ci_per_010: [1.19, 2.03]
      model2_domain_plus_items:
        mcfadden_r2: 0.0423
        nagelkerke_r2: 0.0720
        aic: 14902.3
        subject_delta_or_per_010: 0.73
        difficulty_or_per_010: 0.78
        discrimination_or_per_010: 1.51
      model3_item_delta:
        mcfadden_r2: 0.0012
        nagelkerke_r2: 0.0021
        aic: 15536.9
        or: 2.11
        or_ci: [1.51, 2.96]
      model4_best:
        mcfadden_r2: 0.0434
        nagelkerke_r2: 0.0737
        aic: 14885.4
        item_delta_or_per_010: 0.92
        difficulty_or_per_010: 0.77
        discrimination_or_per_010: 1.54
      simpsons_paradox: true
      lr_test_m1_vs_m2_chi2: 646.98
      lr_test_m3_vs_m4_chi2: 655.53
    result_rationale: >
      Four-model architecture 揭示 Simpson's paradox：accuracy improvement 的 OR 从 Model 1 的 1.55
      （正相关：improved domains 有更多 DIF）reversal 到 Model 2 的 0.73（负相关：controlling for
      item properties 后 improvement 反而 associated with less DIF）。Paradox 成因：DIF items
      更难（d=-0.247, plan_023）且 higher-discrimination（d=0.230），而这些 item properties 同时
      与 accuracy change 相关（difficult domains 有 larger improvement headroom）。
      Model 1 的 R²=0.0007 confirms accuracy improvement 几乎不解释 DIF variance——绝大部分
      DIF 是 item-specific 而非 domain improvement 的 proxy。Model 4 R²=0.0434 shows item
      intrinsic properties（difficulty, discrimination）解释了 >98% 的 explainable variance。
      LR test（χ²=647-656, p<0.001）confirms adding item properties 显著改善 fit。
    tables:
      - "Table S17: Four-model regression summary — OR, 95% CI, R², AIC, deviance"
      - "Table S18: Simpson's paradox — Model 1 vs Model 2 coefficient sign reversal"
    figures_description:
      - "Fig S12: Forest plot — OR with CI for all predictors across 4 models"
    analysis: >
      Full transparency supplement for plan_019 decomposition。Simpson's paradox 是 methodological
      cautionary tale：naive domain-level analysis (OR=1.55) overestimates improvement's contribution，
      item-level conditioning (OR=0.73) reveals the truth。Model 1 作为 primary（conservative），
      Simpson's paradox 在 appendix 详述。R²=0.0007 是 "≤7.6% explained" claim 的 additional support。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "688c8b2d-002c-4d31-a643-9956360460ec",
  "isSidechain": false,
  "requestId": "req_011CbFiDhS11djC1JTfjutDG",
  "type": "assistant",
  "uuid": "d7a455de-0114-4234-8d01-6aef0a0e8eae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Mx9r5b9vN9JjmbXukcnU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20729,
      "cache_read_input_tokens": 11841,
      "output_tokens": 36953,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 36953,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20729
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有 robustness check 干净通过，permutation null 确认 31% 远超 chance，reviewer 认可 'diagnostic lens' 作为 empirical contribution 类型 核心假设：['plan_029 permutation null C% <…",
  "leafUuid": "d7a455de-0114-4234-8d01-6aef0a0e8eae",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric DIF analysis of 5227 models on MMLU",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有 robustness check 干净通过，permutation null 确认 31% 远超 chance，reviewer 认可 'diagnostic lens' 作为 empirical contribution 类型 核心假设：['plan_029 permutation null C% <…",
  "leafUuid": "d7a455de-0114-4234-8d01-6aef0a0e8eae",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric DIF analysis of 5227 models on MMLU",
  "sessionId": "fe355a51-20c3-4c39-b040-f88ab66995c4"
}
```

---
