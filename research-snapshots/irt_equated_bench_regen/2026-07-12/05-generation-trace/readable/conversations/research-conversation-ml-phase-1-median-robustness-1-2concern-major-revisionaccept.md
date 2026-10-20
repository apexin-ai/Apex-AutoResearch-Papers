# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心发现成立但部分robustness弱于预期，1-2个审稿人有实质性concern，需要major revision后accept 核心假设：['

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/3706d8e3-1bea-4a7e-8c25-1c276c952e0c.jsonl`
- **Structured JSON:** [`87104273b48c344f35fb.json`](../../sessions/87/87104273b48c344f35fb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T17:04:46.141Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T17:04:46.141Z",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心发现成立但部分robustness弱于预期，1-2个审稿人有实质性concern，需要major revision后accept\n核心假设：['plan_029 permutation null C% = 3-8%，仍显著但审稿人质疑temporal label本身携带非DIF信号', 'plan_002 RL robustness受限于N=13，结果inconclusive——DIF flags shift moderate (Jaccard 0.65-0.85)，无法claim RL-robust', \"至少一个审稿人认为'applying MH-DIF without modification'novelty不足，要求更强方法贡献\", \"ground truth meta-critique被部分审稿人视为'obvious in hindsight'，需补充更多empirical demonstration\", '8页压缩勉强可行但GSM1K exploratory和circularity ablation细节被迫移入appendix', '98% |Lz|>2的IRT misfit被一个审稿人视为fundamental concern，要求至少pilot multidimensional analysis']\n关键指标范围：{'permutation_null_c_pct': [3.0, 8.0], 'effective_c_pct_after_all_controls': [20.0, 28.0], 'rl_robustness_jaccard': [0.65, 0.85], 'rl_traditional_detector_auroc_drop': [0.05, 0.15], 'reviewer_avg_score': [3.0, 3.5], 'reviewer_novelty_score': [2.5, 3.5], 'semi_synthetic_delta_tpr_replication': [0.35, 0.5], 'cross_benchmark_c_pct_min': [12.0, 18.0], 'cross_benchmark_c_pct_max': [28.0, 32.0], 'page_count_final': [8.0, 8.5]}\n叙事方向：Claim 1从'31% instability'降调为'20-28% after conservative controls'，permutation null虽显著但需承认temporal confound residual。RL robustness降级为limitation而非robustness evidence。Claim 2 meta-critique需要更多empirical scaffolding——补充ConStat/Min-K%在web-overlap labels上的具体failure case analysis (而非仅概念论证)。Claim 3 semi-synthetic framework成为最强贡献，升级为primary contribution。整体从'discovery paper revealing measurement drift'调整为'methodological contribution (semi-synthetic framework) + empirical case study (temporal DIF on MMLU)'。增加一段explicit discussion: 'IRT model misspecification bounds on our findings'，pilot bifactor或MIRT on 2-3 subjects作为revision补充实验。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\nfocus: Dream #9 — based on FULLY REVISED paper after Round 5 review fixes (P17-P26). Key changes since Dream #8:\n\n1. **Title changed**: \"Temporal Measurement Drift in LLM Benchmarks\" (was \"Psychometric Instability\")\n2. **3 contributions (was 4)**: Claim 4 merged into Claim 1, GSM1K demoted to exploratory\n3. **Multi-subject injection robustness (NEW plan_034)**: ΔFPR<0.007 for k≤5 subjects, graceful degradation at k=10+. Proposition 1 explicitly scoped to single-subject with empirical extension.\n4. **Q3 local dependence quantified (NEW plan_035)**: LD inflation <0.001pp, cross-subject matching completely isolates LD effects.\n5. **LLM-specific challenges paragraph**: local dependence, family structure, non-normal ability, multidimensionality explicitly discussed\n6. **DIF running example**: concrete α_MH=0.42 → Δ_MH=2.04 → ETS C walkthrough\n7. **Causal framing systematically softened**: instability → measurement drift/differential functioning throughout\n8. **Bootstrap CI reporting**: model-level resampling explicitly stated, \"approximately 31%\" in Abstract\n9. **Audit protocol expanded**: three-tier threshold (C%<15 monitor, 15-25 flag, >25 act)\n10. **Growing Pains complementarity**: conceptual bridge to anchor item stability\n11. **Citation cleanup**: 8 orphans removed, 3 new refs added (Benchmark2, MedIRT, ATLAS)\n12. **Claim 2 dual interpretation**: explicitly acknowledged in Discussion\n13. **Power analysis details**: Monte Carlo 1000 reps, 2PL PSN-IRT parameters\n\nReviewers should evaluate the CURRENT 3-contribution structure and whether the multi-subject robustness data + framing softening address prior concerns about Proposition 1 scope and causal overclaiming.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n      bootstrap_ci_95:\n      - 29.38\n      - 38.05\n      bootstrap_mean: 33.14\n      bootstrap_sd: 2.3\n      bootstrap_n: 1000\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n- exp_id: plan_031_temporal_granularity\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_full_year:\n      comparison: 2023 vs 2024\n      distance_yr: 1\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.32\n      random_pct_c: 0.02\n    mmlu_half_year:\n      comparison: 2023-H2 vs 2024-H1\n      distance_yr: 0.5\n      n_ref: 1018\n      n_foc: 807\n      pct_c: 34.35\n      random_pct_c: 0.19\n    mmlu_within_2023:\n      comparison: 2023-H1 vs 2023-H2\n      distance_yr: 0.5\n      n_ref: 62\n      n_foc: 1018\n      pct_c: 22.62\n      random_pct_c: 0.18\n      supplementary: true\n    cross_bench_half_year:\n      arc_pct_c: 29.27\n      hellaswag_pct_c: 18.07\n      winogrande_pct_c: 33.62\n      truthfulqa_pct_c: 31.33\n    cross_bench_full_year:\n      arc_pct_c: 26.88\n      hellaswag_pct_c: 17.89\n      winogrande_pct_c: 30.31\n      truthfulqa_pct_c: 29.74\n    half_year_gt_full_year_all_benchmarks: true\n    dif_saturates_within_6mo: true\n- exp_id: plan_032_dif_cleaned_mmlu\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_items_full: 12508\n    n_items_cleaned: 8590\n    n_items_removed: 3918\n    pct_removed: 31.3\n    spearman_rho: 0.9965\n    rank_change_std: 127.1\n    rank_change_min: -589\n    rank_change_max: 849\n    pct_change_ge5: 89.5\n    pct_change_ge10: 79.5\n    pct_change_ge20: 66.4\n    pct_change_ge50: 41.9\n    pct_change_ge100: 24.8\n    top100_pct_ge10: 18\n    top500_pct_ge10: 47.2\n    cohort_2023_mean_change: -22.56\n    cohort_2023_median_change: -5\n    cohort_2024_mean_change: 73.6\n    cohort_2024_median_change: 11\n    systematic_bias: DIF items favor 2024 models; cleaning hurts 2024 +73.6 avg, helps\n      2023 -22.6 avg\n    top_hurt_families:\n      phi-3: 258.35\n      command-r: 235\n      solar: 149.15\n      llama-3: 120.86\n    top_benefit_families:\n      mistral-0.1: -60.32\n      mistral: -53.27\n      zephyr: -29.94\n      gemma-2: -28.78\n    removed_items_harder: true\n    removed_mean_difficulty: 0.409\n    cleaned_mean_difficulty: 0.46\n    random_baseline_20trials:\n      rank_change_std:\n        mean: 60.2\n        std: 7.8\n      mean_abs_rank_change:\n        mean: 36\n        std: 3.6\n      pct_change_ge100:\n        mean: 8.5\n        std: 2\n      cohort_2023_mean_change:\n        mean: 0.4\n        std: 4.1\n      cohort_2024_mean_change:\n        mean: 2.8\n        std: 21.2\n    dif_vs_random_z_scores:\n      rank_change_std_z: 8.5\n      mean_abs_change_z: 10.7\n      pct_ge100_z: 8.2\n      cohort_2023_z: -5.6\n      cohort_2024_z: 3.3\n      cohort_asymmetry_gap_z: 4.4\n- exp_id: plan_033_subject_dif_concentration\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_subjects: 57\n    all_subjects_have_dif: true\n    mean_pct_c: 30.6\n    median_pct_c: 29.7\n    sd_pct_c: 5.5\n    range_pct_c:\n    - 20.7\n    - 48.4\n    top3_subjects:\n      business_ethics: 48.4\n      human_aging: 41.9\n      formal_logic: 40.4\n    bottom3_subjects:\n      computer_security: 20.7\n      marketing: 20.9\n      management: 21.7\n    domain_pct_c:\n      STEM: 30.9\n      Humanities: 31.1\n      Social_Science: 31.6\n    stem_vs_humanities_p: 0.611\n    kruskal_wallis_p: 0.78\n    logistic_regression:\n      difficulty_OR: 0.086\n      discrimination_OR: 57.2\n      pseudo_r2: 0.042\n    excess_dif_subjects:\n    - professional_law\n    - human_aging\n    - world_religions\n    - business_ethics\n    - professional_medicine\n    overall_pct_favor_2024: 43.9\n    temporal_asymmetry:\n      STEM_pct_favor_2024: 55.4\n      Humanities_pct_favor_2024: 35.6\n      Social_Science_pct_favor_2024: 42\n    unidirectional_subjects:\n      world_religions:\n        pct_favor_2024: 16.9\n      logical_fallacies:\n        pct_favor_2024: 20\n- exp_id: plan_034_multi_subject_injection\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    grid:\n      k_values:\n      - 1\n      - 2\n      - 3\n      - 5\n      - 10\n      - 20\n      p_values:\n      - 0.1\n      - 0.3\n      - 0.5\n      seeds_per_k: 5\n      total_runs: 90\n    n_ref: 1080\n    n_foc: 807\n    n_foc_inject: 787\n    proposition_1_boundary: k≈5-10 subjects\n    non_target_delta_fpr:\n      k1_p05: 0.002\n      k2_p05: 0.002\n      k3_p05: -0.001\n      k5_p05: 0.007\n      k10_p03: 0.026\n      k10_p05: 0.069\n      k20_p03: 0.072\n      k20_p05: 0.167\n    target_tpr:\n      k1_p05: 0.834\n      k5_p05: 0.734\n      k10_p05: 0.67\n      k20_p05: 0.611\n    key_findings:\n      k_le_5_robust: true\n      k_le_5_max_delta_fpr: 0.007\n      k10_significant_at_p03: true\n      k20_massive_inflation: true\n      p01_robust_all_k: true\n      tpr_dilution_with_k: true\n      boundary_rule: cross-subject DIF reliable when contaminated fraction <10%\n- exp_id: plan_035_q3_inflation_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_subjects: 8\n    n_permutations: 1000\n    method: permutation null + independence control, cross-subject matching\n    ets_c_inflation:\n      mean_pp: 0.0004\n      max_pp: 0.001\n      max_subject: marketing\n      verdict: far below 3pp threshold\n    p05_inflation:\n      mean_pp: -0.0019\n      direction: slightly negative (no inflation)\n      mean_fpr_with_ld: 0.0412\n      mean_fpr_without_ld: 0.0431\n    subject_details:\n      moral_scenarios:\n        q3_pct: 34.2\n        ets_c_delta_pp: -1.0e-05\n      human_aging:\n        q3_pct: 20.5\n        ets_c_delta_pp: 0.0004\n      world_religions:\n        q3_pct: 18.1\n        ets_c_delta_pp: 0.0006\n      marketing:\n        q3_pct: 17.5\n        ets_c_delta_pp: 0.001\n      professional_law:\n        q3_pct: 10.5\n        ets_c_delta_pp: 0.0003\n      college_medicine:\n        q3_pct: 4.6\n        ets_c_delta_pp: 0.0005\n    q3_inflation_correlation:\n      spearman_rho: -0.238\n      p_value: 0.57\n      significant: false\n    key_insight: Cross-subject matching completely isolates within-subject LD from\n      MH-DIF FPR\n- exp_id: plan_036_growing_pains_lookup\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    paper_found: true\n    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter\n      Calibration'\n    authors: Habba et al.\n    venue: arXiv 2604.12843 (April 2026)\n    fpc_meaning: Fixed Parameter Calibration (NOT Focal Point Contamination)\n    contamination_detection: false\n    anchor_item_list_public: false\n    overlap_analysis_possible: false\n    relevance_to_our_work: shared IRT foundation + contamination acknowledged as limitation\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T17:04:46.145Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T17:04:46.145Z",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T17:04:46.170Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心发现成立但部分robustness弱于预期，1-2个审稿人有实质性concern，需要major revision后accept
核心假设：['plan_029 permutation null C% = 3-8%，仍显著但审稿人质疑temporal label本身携带非DIF信号', 'plan_002 RL robustness受限于N=13，结果inconclusive——DIF flags shift moderate (Jaccard 0.65-0.85)，无法claim RL-robust', "至少一个审稿人认为'applying MH-DIF without modification'novelty不足，要求更强方法贡献", "ground truth meta-critique被部分审稿人视为'obvious in hindsight'，需补充更多empirical demonstration", '8页压缩勉强可行但GSM1K exploratory和circularity ablation细节被迫移入appendix', '98% |Lz|>2的IRT misfit被一个审稿人视为fundamental concern，要求至少pilot multidimensional analysis']
关键指标范围：{'permutation_null_c_pct': [3.0, 8.0], 'effective_c_pct_after_all_controls': [20.0, 28.0], 'rl_robustness_jaccard': [0.65, 0.85], 'rl_traditional_detector_auroc_drop': [0.05, 0.15], 'reviewer_avg_score': [3.0, 3.5], 'reviewer_novelty_score': [2.5, 3.5], 'semi_synthetic_delta_tpr_replication': [0.35, 0.5], 'cross_benchmark_c_pct_min': [12.0, 18.0], 'cross_benchmark_c_pct_max': [28.0, 32.0], 'page_count_final': [8.0, 8.5]}
叙事方向：Claim 1从'31% instability'降调为'20-28% after conservative controls'，permutation null虽显著但需承认temporal confound residual。RL robustness降级为limitation而非robustness evidence。Claim 2 meta-critique需要更多empirical scaffolding——补充ConStat/Min-K%在web-overlap labels上的具体failure case analysis (而非仅概念论证)。Claim 3 semi-synthetic framework成为最强贡献，升级为primary contribution。整体从'discovery paper revealing measurement drift'调整为'methodological contribution (semi-synthetic framework) + empirical case study (temporal DIF on MMLU)'。增加一段explicit discussion: 'IRT model misspecification bounds on our findings'，pilot bifactor或MIRT on 2-3 subjects作为revision补充实验。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen
venue: emnlp-2026
focus: Dream #9 — based on FULLY REVISED paper after Round 5 review fixes (P17-P26). Key changes since Dream #8:

1. **Title changed**: "Temporal Measurement Drift in LLM Benchmarks" (was "Psychometric Instability")
2. **3 contributions (was 4)**: Claim 4 merged into Claim 1, GSM1K demoted to exploratory
3. **Multi-subject injection robustness (NEW plan_034)**: ΔFPR<0.007 for k≤5 subjects, graceful degradation at k=10+. Proposition 1 explicitly scoped to single-subject with empirical extension.
4. **Q3 local dependence quantified (NEW plan_035)**: LD inflation <0.001pp, cross-subject matching completely isolates LD effects.
5. **LLM-specific challenges paragraph**: local dependence, family structure, non-normal ability, multidimensionality explicitly discussed
6. **DIF running example**: concrete α_MH=0.42 → Δ_MH=2.04 → ETS C walkthrough
7. **Causal framing systematically softened**: instability → measurement drift/differential functioning throughout
8. **Bootstrap CI reporting**: model-level resampling explicitly stated, "approximately 31%" in Abstract
9. **Audit protocol expanded**: three-tier threshold (C%<15 monitor, 15-25 flag, >25 act)
10. **Growing Pains complementarity**: conceptual bridge to anchor item stability
11. **Citation cleanup**: 8 orphans removed, 3 new refs added (Benchmark2, MedIRT, ATLAS)
12. **Claim 2 dual interpretation**: explicitly acknowledged in Discussion
13. **Power analysis details**: Monte Carlo 1000 reps, 2PL PSN-IRT parameters

Reviewers should evaluate the CURRENT 3-contribution structure and whether the multi-subject robustness data + framing softening address prior concerns about Proposition 1 scope and causal overclaiming.

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
- exp_id: plan_034_multi_subject_injection
  name: ''
  status: DONE
  conclusion: success
  metrics:
    grid:
      k_values:
      - 1
      - 2
      - 3
      - 5
      - 10
      - 20
      p_values:
      - 0.1
      - 0.3
      - 0.5
      seeds_per_k: 5
      total_runs: 90
    n_ref: 1080
    n_foc: 807
    n_foc_inject: 787
    proposition_1_boundary: k≈5-10 subjects
    non_target_delta_fpr:
      k1_p05: 0.002
      k2_p05: 0.002
      k3_p05: -0.001
      k5_p05: 0.007
      k10_p03: 0.026
      k10_p05: 0.069
      k20_p03: 0.072
      k20_p05: 0.167
    target_tpr:
      k1_p05: 0.834
      k5_p05: 0.734
      k10_p05: 0.67
      k20_p05: 0.611
    key_findings:
      k_le_5_robust: true
      k_le_5_max_delta_fpr: 0.007
      k10_significant_at_p03: true
      k20_massive_inflation: true
      p01_robust_all_k: true
      tpr_dilution_with_k: true
      boundary_rule: cross-subject DIF reliable when contaminated fraction <10%
- exp_id: plan_035_q3_inflation_sim
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_subjects: 8
    n_permutations: 1000
    method: permutation null + independence control, cross-subject matching
    ets_c_inflation:
      mean_pp: 0.0004
      max_pp: 0.001
      max_subject: marketing
      verdict: far below 3pp threshold
    p05_inflation:
      mean_pp: -0.0019
      direction: slightly negative (no inflation)
      mean_fpr_with_ld: 0.0412
      mean_fpr_without_ld: 0.0431
    subject_details:
      moral_scenarios:
        q3_pct: 34.2
        ets_c_delta_pp: -1.0e-05
      human_aging:
        q3_pct: 20.5
        ets_c_delta_pp: 0.0004
      world_religions:
        q3_pct: 18.1
        ets_c_delta_pp: 0.0006
      marketing:
        q3_pct: 17.5
        ets_c_delta_pp: 0.001
      professional_law:
        q3_pct: 10.5
        ets_c_delta_pp: 0.0003
      college_medicine:
        q3_pct: 4.6
        ets_c_delta_pp: 0.0005
    q3_inflation_correlation:
      spearman_rho: -0.238
      p_value: 0.57
      significant: false
    key_insight: Cross-subject matching completely isolates within-subject LD from
      MH-DIF FPR
- exp_id: plan_036_growing_pains_lookup
  name: ''
  status: DONE
  conclusion: success
  metrics:
    paper_found: true
    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter
      Calibration'
    authors: Habba et al.
    venue: arXiv 2604.12843 (April 2026)
    fpc_meaning: Fixed Parameter Calibration (NOT Focal Point Contamination)
    contamination_detection: false
    anchor_item_list_public: false
    overlap_analysis_possible: false
    relevance_to_our_work: shared IRT foundation + contamination acknowledged as limitation

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
  "promptId": "f8598653-6910-4d19-8e2f-83c85890691e",
  "type": "user",
  "uuid": "71bcadc9-215a-4045-9a4e-9af7b1e68b2e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T17:04:46.167Z_

```json
{
  "parentUuid": "71bcadc9-215a-4045-9a4e-9af7b1e68b2e",
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
  "uuid": "fe69b83d-38f7-4ed7-bbcf-ed5f5047caa1",
  "timestamp": "2026-05-21T17:04:46.167Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T17:04:46.167Z_

```json
{
  "parentUuid": "fe69b83d-38f7-4ed7-bbcf-ed5f5047caa1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c4862d63-0828-4baf-b1fe-1c8be3f4fa5f",
  "timestamp": "2026-05-21T17:04:46.167Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心发现成立但部分robustness弱于预期，1-2个审稿人有实质性concern，需要major revision后accept 核心假设：['plan_029 permutation null C% = 3-8%，仍显著但审稿人质疑temporal label本身携带非DIF信号', 'plan_0…",
  "leafUuid": "c4862d63-0828-4baf-b1fe-1c8be3f4fa5f",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Temporal DIF characterization with semi-synthetic validation",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c"
}
```

---

### Assistant

_source line 8 · 2026-05-21T17:06:09.340Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each "planned" experiment in the experiment_plan, under the "median" tier assumptions defined in Phase 1. I need to provide result_rationale for each prediction explaining why this result occurs at the median tier.

Let me identify all experiments with status "planned":

1. plan_001 - real_data_dif_mmlu (status: planned) - BUT wait, there's a registry entry "plan_001_real_data_dif_mmlu" with status DONE. So this is already done.

Let me re-read. The experiment_plan lists statuses, and the registry lists completed experiments. Let me cross-reference:


I'm seeing that some experiments marked as "planned" in the experiment_plan are actually already completed in the registry (plan_001 and plan_004), while others like plan_002 through plan_007 remain genuinely planned and need predicted data generated for them. I'm noticing a discrepancy between the experiment_plan status field, which shows all experiments as "planned," and the registry entries that indicate many are already completed. The user is asking me to generate detailed predicted data for each planned experiment, so I should treat all of them as needing median-tier scenario predictions, regardless of whether actual results exist in the registry. The median tier represents a specific performance scenario that's weaker than the best case, and I need to work through each experiment systematically to generate those predictions based on the median tier characteristics. Looking at the key adjustments: the permutation null establishes a 3-8% baseline, so the actual excess effect is around 20-25% rather than the original 31%, and I'm acknowledging the temporal confounding as a limitation. The RL robustness findings get downgraded to a limitation rather than a core claim, while the semi-synthetic approach becomes the primary contribution. I'm repositioning the paper as methodological work with an empirical case study, and I need to address potential IRT model misspecification by exploring bifactor or MIRT approaches.

Now I'm working through the experimental predictions for each plan, starting with how the core 31.3% finding holds up in the median tier after applying all controls. The remaining approaches show mixed results—generation quality falls short of targets, Bayesian simulation improves outcomes but not dramatically, validity degrades gracefully with wider confidence intervals, and the decoder-only architecture essentially serves as a control. Cross-benchmark contamination validation shows moderate signal with elevated false positives, while temporal analysis reveals inconsistent performance across benchmarks and permutation testing yields null results.

Now I'm checking what the user actually requested and need to produce detailed YAML output with specific numerical results for each planned experiment, being thorough with median-tier ranges for the calibration metrics. Raw C% sits around 31%, but after accounting for permutation null corrections, ability matching adjustments, and other controls, the effective C% drops to roughly 24%, with enrichment holding steady near 1.0 and domain correlation staying modest. For plan_002, I have 13 RL models available and the Jaccard overlap between SFT-only and SFT+RL DIF flags is 0.75, though the traditional detector shows an AUROC drop of 0.08—the bootstrap confidence intervals are too wide to make a definitive claim about RL robustness, so this gets marked as a limitation. ConStat achieves moderate detection performance around 0.65 AUROC on the non-RL models.

Moving through the remaining approaches, paraphrasing quality detection flags about 15% of items as suspicious via FDR control, but the overlap with DIF flags is weak at a Jaccard of 0.15. The DVD generation approach shows a bimodal distribution in roughly 8% of items, though the signal-to-noise ratio is too low and temperature sensitivity makes the results unstable. Ensemble fusion only provides marginal gains of 0.03 AUROC over the best single model, and the calibration proves fragile with high cross-validation variance in the fusion weights. On GSM8K, I'm seeing a C% of 15.2% within the expected range, semi-synthetic ΔTPR of 0.42, but GSM1K shows weaker correlation around -0.35 with wider confidence intervals. The bifactor model fails to converge on the full MMLU dataset.

Focusing on the remaining plans, the bifactor approach doesn't scale to all subjects, so I tested it on just 5 subjects and found only marginal improvement before abandoning it as infeasible. Generated items correlate with targets at ρ=0.35, falling well short of the 0.75 threshold needed for equating. Cumulative power plateaus at 0.55 after three administrations, below the 0.70 target but still better than the single administration baseline of 0.40. Progressive item replacement degrades validity linearly, with ρ dropping to 0.985 at 31% replacement—still high but noticeably degraded. IFT detects similar items as MH-DIF with a Jaccard of 0.70, and adding continuous treatment provides some nuance without fundamentally changing the core findings. The decoder-only subset analysis is underway with approximately 5,220 items.

Now looking at the remaining approaches: the semi-synthetic ΔTPR at p=0.5 sits at 0.42 within the acceptable 0.35-0.50 range, though the FPR baseline is elevated at 0.31, and cross-subject matching shows minimal ΔFPR of 0.001 while standard matching exhibits FPR inflation. Multi-benchmark performance varies considerably, ranging from 14.5% on HellaSwag to 28.8% on MMLU after controls, which raises concerns about generalizability since not all benchmarks exceed 15%. The permutation null yields C% at 5.2%, well within the 3-8% range and significantly below the observed 31.3% (p<0.001), though this non-trivial baseline complicates interpretation.

The effective excess after accounting for this baseline drops to roughly 26% rather than the full 31%, and I'm questioning whether temporal labels themselves contribute signal beyond differential item functioning. Odds ratios reveal weak explanatory power, Simpson's paradox continues to emerge, and item-level models show minimal R² around 0.04 even when incorporating item properties. Given these findings, the defensible range after all robustness checks appears to be 20-28%, a meaningful downward adjustment from the initial 31% instability claim.

The permutation null yields 3-8% false positive rates, which is still notable. Reinforcement learning robustness is limited by the small sample of 13 items, leaving results inconclusive—DIF flags shift moderately with Jaccard similarity between 0.65 and 0.85. Reviewers have raised concerns about novelty when applying standard Mantel-Haenszel DIF without modification, and some view the ground truth meta-critique as obvious in retrospect. The 98% of items showing IRT misfit with |Lz| > 2 is flagged as a fundamental concern, pushing me toward at least piloting a bifactor analysis to explore multidimensionality.

Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4862d63-0828-4baf-b1fe-1c8be3f4fa5f",
  "isSidechain": false,
  "requestId": "req_011CbG5SmRfeud1Nknj4RKfF",
  "type": "assistant",
  "uuid": "3c62653c-d467-4da9-b6a3-9047e9d5f2a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2cdYo7ruibSFo2WQTtsDd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24029,
      "cache_read_input_tokens": 11841,
      "output_tokens": 19061,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24029,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 19061,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24029
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

_source line 9 · 2026-05-21T17:11:16.064Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1从'31% instability'降调为'20-28% after conservative controls'——permutation null 5.2%虽仍显著但审稿人
  质疑temporal label携带非DIF信号(cohort composition shift, training data vintage correlation)。RL robustness
  降级为limitation (N=13, Jaccard=0.75, inconclusive)。Claim 2 meta-critique需补充ConStat/Min-K%在
  web-overlap labels上的具体failure case analysis。Claim 3 semi-synthetic framework升级为primary
  contribution (ΔTPR=0.42 at p=0.5，cross-subject ΔFPR<0.001稳健)。整体定位从'discovery paper'调整为
  'methodological contribution (semi-synthetic framework) + empirical case study (temporal DIF on MMLU)'。
  增加explicit discussion 'IRT model misspecification bounds'，pilot bifactor on 2-3 subjects。
  8页压缩勉强可行但GSM1K exploratory和circularity ablation细节移入appendix。reviewer avg 3.0-3.5,
  novelty score 2.5-3.5, 需major revision后accept。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      对METABENCH MMLU响应矩阵(5219×12508)运行MH-DIF。temporal cohort (2023 vs 2024-H1)、
      ability quintile、within-family confound control、domain-specificity分析。
    expected_results:
      temporal_ets_c_pct: 31.3
      temporal_fpr_li_clean: 0.32
      temporal_enrichment: 0.96
      ability_ets_c_pct: 2.9
      ability_enrichment: 1.19
      within_family_llama2v3_c_pct: 61.3
      within_family_mistral_mixtral_c_pct: 38.7
      domain_spearman_rho: 0.31
      domain_spearman_p: 0.02
      sanity_random_split_c_pct: 0.18
      effective_c_pct_after_all_controls: 24.5
      domain_specificity_range: "20.7-48.4%"
      unweighted_mean_c_pct: 30.6
    result_rationale: >
      Raw C%=31.3%与实际一致——这是MH-DIF在该数据上的机械输出，不受tier影响。median档的关键区别在于
      downstream interpretation：permutation null将揭示3-8%的baseline（plan_029），ability matching
      扣除2.4pp（plan_027），combined controls将effective estimate压至~24.5%。enrichment≈1.0仍成立
      因为Li et al. labels本质上测量的是global exposure而非differential contamination——这个null
      result是结构性的，与tier无关。domain correlation ρ=0.31 (p=0.02)在subject level是modest ecological
      correlation，item-level decomposition（plan_019/030）将显示domain improvement仅解释≤2.4pp。
      within-family Llama-2v3的61.3%反映了巨大的ability gap (d=-0.99)，ability matching后降至~28%，
      与temporal cohort matched estimate收敛——这支持~24-29%是genuine item-level DIF的估计。
      median档下审稿人会argue 24.5%虽显著但不如31.3%那么striking，且temporal label可能携带
      training data vintage以外的confound（e.g., RLHF protocol evolution, tokenizer changes）。
    tables:
      - name: "Table 1: Temporal DIF Summary (Median Tier Interpretation)"
        columns: [cohort_definition, n_ref, n_foc, raw_c_pct, permutation_null_c_pct, ability_adjusted_c_pct, effective_c_pct]
        rows:
          - [temporal_2023v2024, 1080, 807, 31.3, 5.2, 28.9, 24.5]
          - [ability_quintile, 2100, 2100, 2.9, 0.3, "—", 2.6]
          - [random_split_sanity, 950, 950, 0.18, "—", "—", "~0"]
      - name: "Table 2: Within-Family Confound Control"
        columns: [family_pair, raw_c_pct, cohens_d, ability_matched_c_pct, interpretation]
        rows:
          - [Llama-2_vs_Llama-3, 61.3, -0.99, 28.3, "ability confound explains 33pp"]
          - [Mistral_vs_Mixtral, 38.7, -0.45, "~30", "moderate ability confound"]
          - [Temporal_2023v2024, 31.3, -0.17, 28.9, "ability confound explains 2.4pp"]
    figures_description:
      - "Fig 1: C% by MMLU subject (57 bars), horizontal line at permutation null mean=5.2%. All subjects above null, range 20.7-48.4%. Shaded band shows effective range 20-28% after controls."
      - "Fig 2: Scatter plot domain accuracy improvement vs subject C%, ρ=0.31. Annotation: item-level R²<0.001."
    analysis: >
      Raw 31.3%数据不变，但median档的叙事必须承认：(1) permutation null 5.2%意味着temporal label
      本身携带约5pp的非DIF信号；(2) ability matching扣除2.4pp；(3) 合计conservative estimate为
      ~24.5%。审稿人会要求明确报告effective C%而非仅raw C%。仍然是substantial finding
      （24.5% >> random 0.18%），但从"approximately 31%"降调为"20-28% after conservative controls"。
      domain correlation ρ=0.31虽p<0.05但explanatory power极低（R²<0.001 at item level），
      支持instability is item-specific而非domain-driven的结论。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      验证DIF对RL训练的鲁棒性。SFT baseline + alignment-RL (DPO/ORPO, N=477) + reasoning-RL
      (GRPO/PPO, N=13)。对比DIF vs ConStat vs Min-K%在各cohort上的表现。
    expected_results:
      n_reasoning_rl_models: 13
      n_alignment_rl_models: 477
      n_sft_baseline: 350
      dif_flag_jaccard_sft_vs_sft_plus_alignment_rl: 0.92
      dif_flag_jaccard_sft_vs_sft_plus_reasoning_rl: 0.75
      dif_flag_jaccard_sft_vs_all_combined: 0.78
      bootstrap_jaccard_ci_reasoning_rl: [0.62, 0.87]
      constat_auroc_sft: 0.72
      constat_auroc_alignment_rl: 0.68
      constat_auroc_reasoning_rl: 0.58
      mink_auroc_sft: 0.75
      mink_auroc_reasoning_rl: 0.62
      dif_c_pct_sft_only_cohort: 30.8
      dif_c_pct_with_reasoning_rl: 28.2
      auroc_drop_constat_sft_to_rl: 0.14
      auroc_drop_mink_sft_to_rl: 0.13
      tost_equivalence_p: 0.18
      delong_dif_vs_constat_p: 0.34
      power_analysis_partial_exploitation:
        p_04_detection_boundary_delta: 1.8
        p_06_detection_boundary_delta: 1.5
        p_08_detection_boundary_delta: 1.3
        p_10_detection_boundary_delta: 1.0
    result_rationale: >
      N=13 reasoning-RL模型是median档的核心瓶颈。alignment-RL (DPO/ORPO)不产生NLL gap contraction，
      因此Jaccard=0.92与SFT几乎无差异——这不是RL-robustness的有效测试。真正的测试是reasoning-RL
      (GRPO/PPO)，但N=13意味着：(1) 将13个模型加入focal cohort（N=807→820）对群体级DIF统计量
      影响微弱，Jaccard=0.75反映的是sampling variability而非systematic degradation；(2) Bootstrap CI
      [0.62, 0.87]跨越了"moderate shift"和"essentially stable"的分界线；(3) TOST equivalence test
      p=0.18无法reject non-equivalence，即无法正式claim equivalence。traditional detectors (ConStat, Min-K%)
      在reasoning-RL上AUROC下降0.13-0.14，但N=13的individual-level比较power极低，CI覆盖null。
      结论：DIF flags shift moderate但方向不确定，无法claim RL-robust也无法claim RL-breaks-DIF。
      必须降级为limitation："RL robustness remains an open question due to insufficient reasoning-RL
      sample size"。partial exploitation power analysis是clean theoretical result但缺乏empirical validation。
    tables:
      - name: "Table: RL Robustness Summary"
        columns: [cohort_composition, n_total_foc, dif_c_pct, jaccard_vs_baseline, constat_auroc, mink_auroc]
        rows:
          - [SFT_only, 350, 30.8, 1.0, 0.72, 0.75]
          - [SFT+alignment_RL, 827, 31.0, 0.92, 0.68, 0.71]
          - [SFT+reasoning_RL, 363, 28.2, 0.75, 0.58, 0.62]
          - [All_combined, 840, 29.5, 0.78, 0.65, 0.67]
    figures_description:
      - "Fig: Jaccard stability as function of reasoning-RL fraction in focal cohort. Bootstrap CIs shown. Dashed line at Jaccard=0.80 (stability threshold). CI crosses threshold at N_RL≈10."
    analysis: >
      median档下RL robustness是最弱的claim。Jaccard=0.75在0.65-0.85范围内，审稿人会正确指出：
      (1) N=13不足以区分genuine degradation和sampling noise；(2) alignment-RL的high Jaccard不证明
      RL-robustness因为DPO不是target mechanism；(3) TOST failure意味着equivalence未被证明。
      唯一可写的是"DIF shows moderate stability when reasoning-RL models are added to the cohort,
      but the small sample precludes definitive conclusions"——这作为limitation而非robustness evidence。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      独立评估ConStat-style perturbation testing在MMLU上的表现。LLM paraphrasing生成语义等价
      reformulations，比较原始与改写性能差异。
    expected_results:
      n_items_paraphrased: 220
      paraphrase_semantic_similarity_mean: 0.91
      paraphrase_quality_human_rating: 3.8
      constat_detection_auroc_all_models: 0.63
      constat_detection_auroc_non_rl: 0.67
      constat_detection_auroc_rl_models: 0.51
      fdr_controlled_suspicious_pct: 14.2
      constat_dif_overlap_jaccard: 0.13
      constat_dif_overlap_phi: 0.08
      constat_fpr_at_05_threshold: 0.11
      constat_tpr_at_05_threshold: 0.38
      web_overlap_label_concordance: 0.22
    result_rationale: >
      ConStat检测verbatim contamination via performance drop on paraphrased items。在median档下：
      (1) paraphrasing quality足够（similarity=0.91）但不完美——部分reformulation可能改变了cognitive
      demand而非仅surface form，引入noise；(2) non-RL models AUROC=0.67是moderate但not strong，因为
      MMLU的4-choice format天然限制了performance variance（25% floor）；(3) RL models AUROC≈0.51
      接近chance，验证了Wang et al.的concern——reasoning-RL models不依赖verbatim memorization；
      (4) ConStat-DIF overlap极低（Jaccard=0.13）因为两种方法测量不同construct：ConStat测量
      individual model对specific item的memorization，DIF测量cohort-level differential functioning。
      这个低overlap支持Claim 2的meta-critique但审稿人会质疑：如果两种方法如此不同，是否说明
      DIF并非测量contamination而是测量something else entirely？median档下这个tension无法完全resolve。
    tables:
      - name: "Table: ConStat Detection by Model Category"
        columns: [model_category, n_models, auroc, fdr_q05_flags_pct, overlap_dif_jaccard]
        rows:
          - [SFT_only, 15, 0.67, 16.3, 0.14]
          - [alignment_RL, 12, 0.64, 13.8, 0.12]
          - [reasoning_RL, 8, 0.51, 8.1, 0.09]
          - [all, 35, 0.63, 14.2, 0.13]
    figures_description:
      - "Fig: Venn diagram of DIF-C flags vs ConStat suspicious items vs Li et al. web-overlap positives. Triple overlap < 5%."
    analysis: >
      ConStat结果支持"不同检测方法测量不同contamination constructs"的叙事，但median档下的AUROC
      偏低，审稿人可能质疑paraphrasing methodology。作为Claim 2的empirical scaffolding有用但不够strong。
      降级为appendix baseline comparison。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      在MMLU上独立评估DVD generation variance检测。对10-15个开源模型生成多次responses，
      计算variance scores，检测bimodal distributions。
    expected_results:
      n_models_tested: 12
      n_responses_per_item: 50
      temperature: 0.8
      bimodal_items_pct: 7.8
      bimodal_dif_overlap_jaccard: 0.11
      generation_variance_contamination_auroc: 0.58
      variant_contamination_detection_auroc: 0.55
      verbatim_contamination_detection_auroc: 0.62
      signal_to_noise_ratio: 1.3
      temperature_sensitivity_auroc_range: [0.52, 0.64]
    result_rationale: >
      DVD依赖generation variance作为contamination signal：contaminated items应有lower variance
      （模型确定性更高）。在median档下：(1) MMLU是4-choice MCQ，generation variance本质上是
      logit variance over 4 options——信号空间极窄；(2) 7.8% bimodal items远低于DIF的31.3%，
      且overlap极低（Jaccard=0.11），说明DVD捕获的是不同phenomenon（可能是item ambiguity
      而非contamination）；(3) AUROC=0.58仅略高于chance，signal-to-noise=1.3不足以作为
      reliable detector；(4) temperature sensitivity range [0.52, 0.64]说明结果对hyperparameter
      fragile。在median档下DVD essentially fails as a standalone detector on MCQ benchmarks。
      这支持ensemble的motivation但也限制了ensemble的ceiling。
    tables:
      - name: "Table: DVD Detection Performance"
        columns: [contamination_type, auroc, bimodal_pct, snr]
        rows:
          - [verbatim, 0.62, 9.2, 1.5]
          - [variant, 0.55, 6.1, 1.1]
          - [overall, 0.58, 7.8, 1.3]
    figures_description:
      - "Fig: Generation variance distribution for DIF-C vs non-DIF items. Largely overlapping, weak separation."
    analysis: >
      DVD在MCQ benchmarks上表现差是expected——4选1格式的generation variance信号极弱。
      在median档下这成为negative result，进一步支持Claim 2的论点：现有per-model detectors
      各有structural limitations。但negative result本身不够novel，移入appendix。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      融合DIF + ConStat + DVD为multi-signal ensemble。2-of-3 majority voting和weighted fusion。
    expected_results:
      ensemble_auroc_majority_vote: 0.66
      ensemble_auroc_weighted: 0.69
      ensemble_fpr_at_05: 0.13
      ensemble_coverage_theoretical: "DIF≥1.4, ConStat≥0.6, DVD variant"
      ensemble_improvement_over_best_individual: 0.02
      cross_validation_weight_variance: 0.18
      uniform_weight_auroc: 0.65
      optimized_weight_auroc: 0.69
      overfitting_gap: 0.04
    result_rationale: >
      Ensemble ceiling受限于weakest components。在median档下：(1) DVD AUROC≈0.58几乎是noise，
      实际上是2-signal ensemble (DIF+ConStat) with DVD as dead weight；(2) weighted fusion
      仅比best individual (DIF) 提升+0.02，且cross-validation显示weight variance=0.18——
      说明optimal weights unstable across folds，overfitting gap=0.04；(3) majority voting
      AUROC=0.66略低于weighted因为DVD的noise票拉低了precision；(4) FPR=0.13勉强满足<0.15
      但不satisfying。整体来看ensemble contribution marginal，不足以作为standalone contribution。
      在median档下ensemble被correctly dropped from main claims（与Dream #6 consensus一致）。
    tables:
      - name: "Table: Ensemble Performance Comparison"
        columns: [method, auroc, fpr, tpr_at_fpr_10]
        rows:
          - [DIF_only, 0.67, 0.31, 0.52]
          - [ConStat_only, 0.63, 0.11, 0.38]
          - [DVD_only, 0.58, 0.15, 0.28]
          - [Majority_vote, 0.66, 0.13, 0.45]
          - [Weighted_fusion, 0.69, 0.12, 0.49]
    figures_description:
      - "Fig: ROC curves for individual detectors and ensemble methods. Ensemble marginal improvement visible only in mid-FPR range."
    analysis: >
      Ensemble不提供sufficient added value。correctly dropped from contributions。
      在appendix作为"we tried this, marginal improvement"的completeness disclosure。
      审稿人不会要求ensemble作为contribution，但会appreciate transparency。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      在GSM8K (1319 items × 6702 models)上复制DIF分析。GSM1K作为contamination ground truth。
      Semi-synthetic validation。
    expected_results:
      gsm8k_temporal_c_pct: 15.2
      gsm8k_sanity_c_pct: 0.25
      gsm8k_standard_external_spearman: 0.91
      semi_synthetic_delta_tpr_p05: 0.42
      semi_synthetic_delta_tpr_p10: 0.68
      semi_synthetic_standard_delta_tpr_p10: 0.72
      gsm1k_correlation_n: 33
      gsm1k_pearson_r: -0.35
      gsm1k_pearson_p: 0.045
      gsm1k_spearman_rho: -0.30
      gsm1k_spearman_p: 0.09
      gsm1k_pearson_ci_95: [-0.62, -0.02]
      partial_r_controlling_accuracy: -0.28
      partial_p: 0.11
      leave_one_out_r_range: [-0.45, -0.22]
    result_rationale: >
      median档下GSM8K C%=15.2%（在cross_benchmark_c_pct_min range 12-18%内），低于MMLU的31.3%。
      这反映GSM8K的structural特点：(1) 单一domain (math)意味着DIF更多反映capability improvement
      而非item-specific instability；(2) 1319 items远少于MMLU的12508，statistical power lower。
      semi-synthetic ΔTPR=0.42 at p=0.5（在0.35-0.50 range内），低于actual的0.834(standard)和
      0.517(external)——median档预期cross-subject matching在single-domain benchmark上效率较低，
      因为"other subjects"不存在于GSM8K，只能用external ability measures。GSM1K correlation在
      median档下weakened：r=-0.35 (vs actual -0.478)，N=33使得CI极宽[-0.62, -0.02]，Spearman
      p=0.09不显著。partial correlation controlling accuracy p=0.11也不显著。审稿人会argue这
      不够strong作为validation evidence——correctly demoted to exploratory。方向仍是NEGATIVE
      (opposite to contamination hypothesis)，这对叙事是complicating factor。
    tables:
      - name: "Table: GSM8K Temporal DIF"
        columns: [metric, value, ci_95_lower, ci_95_upper]
        rows:
          - [temporal_c_pct, 15.2, 12.8, 17.9]
          - [semi_synthetic_delta_tpr_p05, 0.42, 0.31, 0.54]
          - [gsm1k_pearson_r, -0.35, -0.62, -0.02]
          - [gsm1k_spearman_rho, -0.30, -0.59, 0.05]
    figures_description:
      - "Fig: GSM8K DIF-C fraction vs GSM1K contamination gap scatter (N=33). Negative trend with wide CI band. Deepseek-math-7b-rl as outlier annotated."
    analysis: >
      GSM8K replication confirms framework portability但signal weaker。C%=15.2%在single-domain
      benchmark上reasonable。GSM1K correlation direction puzzling (NEGATIVE)且median档下
      barely significant——demoted to exploratory appendix。semi-synthetic ΔTPR=0.42 is the
      strongest deliverable: confirms detection power on independent benchmark。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      在MMLU上pilot bifactor IRT model (general + 57 subject-specific factors)。
      选择anchor items，fixed-parameter calibration equating。
    expected_results:
      convergence: false
      full_model_attempted: true
      n_subjects: 57
      convergence_failure_reason: "57 group factors + 12508 items exceeds estimation capacity"
      subset_5_subjects_converged: true
      subset_5_bifactor_rmsea: 0.038
      subset_5_cfi: 0.89
      subset_5_general_factor_variance_explained: 0.42
      subset_5_specific_factor_variance_explained: 0.31
      subset_5_residual: 0.27
      target_cfi: 0.95
      target_met: false
      equating_pilot_rho: 0.91
      equating_pilot_target: 0.95
      equating_pilot_met: false
    result_rationale: >
      median档下bifactor model在full MMLU上不收敛——57个subject-specific factors × 12508 items
      的参数空间对于mirt estimation来说太大（即使用EM或MHRM）。5-subject subset收敛但fit
      below target：CFI=0.89 < 0.95 target，说明即使bifactor也不能adequately capture MMLU的
      multidimensional structure。general factor仅解释42% variance意味着subject-specific factors
      和residual各占约30%——MMLU确实是highly multidimensional。equating pilot在这些suboptimal
      parameters下达到ρ=0.91，低于0.95 target。结论：bifactor approach technically infeasible
      at scale且fit insufficient——killed as in actual registry。但median档下这个negative result
      被一个审稿人视为重要：要求至少报告2-3 subject的pilot MIRT analysis来bound IRT
      misspecification对DIF findings的影响。这成为revision要求。
    tables:
      - name: "Table: Bifactor Pilot on 5-Subject Subset"
        columns: [metric, observed, target, met]
        rows:
          - [RMSEA, 0.038, "<0.05", yes]
          - [CFI, 0.89, ">0.95", no]
          - [TLI, 0.86, ">0.95", no]
          - [general_variance_pct, 42, ">60", no]
          - [equating_rho, 0.91, ">0.95", no]
    figures_description:
      - "Fig: Bifactor path diagram for 5-subject subset showing general + specific factor loadings. Substantial specific factor variance visible."
    analysis: >
      Bifactor killed但negative result有价值：quantifies IRT misspecification severity。
      median档下审稿人要求至少pilot 2-3 subject的MIRT作为revision补充实验，to show that
      DIF findings在multidimensional framework下方向一致（即使magnitude可能change）。
      这是major revision的核心要求之一。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      为DIF-flagged items生成replacement items。LLM generation + student simulation calibration。
    expected_results:
      n_items_generated: 150
      difficulty_correlation_prompt_based: 0.32
      difficulty_correlation_student_sim: 0.48
      target_difficulty_correlation: 0.75
      target_met: false
      cognitive_level_match_pct: 62
      subject_match_pct: 100
      holdout_panel_validation_rho: 0.41
      generation_quality_human_rating: 3.2
    result_rationale: >
      item generation在median档下below benchmarks。prompt-based difficulty targeting ρ=0.32
      与literature一致（arXiv 2602.06631报告0.10-0.45）。student simulation calibration提升到
      ρ=0.48但仍远低于0.75 target——原因：(1) MMLU items涵盖57个specialized domains，LLM生成
      在specialized knowledge items上quality不稳定；(2) student simulation (arXiv 2601.09953)
      的r=0.75-0.82是在其own benchmark上的，transfer到MMLU-style items有gap；(3) cognitive
      level matching仅62%说明生成的items常常shift了cognitive demand（e.g., 从recall变成reasoning）。
      结论：item generation pipeline尚不mature enough for equating——correctly dropped from
      main claims。这与bifactor failure combined意味着Claim 3 (regeneration/equating) is dead。
    tables:
      - name: "Table: Item Generation Quality"
        columns: [calibration_method, difficulty_rho, cognitive_match_pct, overall_quality]
        rows:
          - [prompt_only, 0.32, 58, 2.8]
          - [student_simulation, 0.48, 62, 3.2]
          - [target, 0.75, 80, 4.0]
    figures_description:
      - "Fig: Scatter of generated item difficulty vs target difficulty. Wide dispersion, ρ=0.48."
    analysis: >
      Item generation correctly killed。不作为contribution。但作为appendix supplementary
      对future work有reference value。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      实现cumulative Bayesian DIF priors (Sinharay et al. 2006)。模拟4次successive benchmark
      administrations，展示累积evidence的power improvement。
    expected_results:
      single_admin_power_medium: 0.40
      cumulative_2_admin_power: 0.48
      cumulative_3_admin_power: 0.55
      cumulative_4_admin_power: 0.61
      target_3_admin_power: 0.70
      target_met: false
      delta_10_effect:
        single: 0.40
        cumulative_3: 0.55
      delta_14_effect:
        single: 0.68
        cumulative_3: 0.82
      false_positive_rate_cumulative: 0.058
      prior_specification: "N(0, sigma=1.5)"
    result_rationale: >
      median档下cumulative power at 3 administrations仅达0.55（target 0.70）。差距原因：
      (1) simulation使用的是idealized independent administrations，但real temporal cohorts
      have correlated composition（overlapping models between administrations）；(2) medium
      effect size (δ=1.0) 在MMLU的high-noise环境下需要更多accumulation；(3) prior
      specification N(0,1.5)可能too vague for the specific DIF magnitude distribution
      observed in MMLU。对于large effects (δ≥1.4)，cumulative确实提升到0.82——但这些items
      已经被single-admin MH-DIF以0.68 power检测到，marginal value limited。结论：theoretically
      sound但实际improvement insufficient to justify methodological complexity。simulation-only，
      underdeveloped，correctly moved to appendix。
    tables:
      - name: "Table: Cumulative Bayesian Power by Effect Size"
        columns: [effect_delta, admin_1, admin_2, admin_3, admin_4]
        rows:
          - [0.8, 0.22, 0.30, 0.36, 0.41]
          - [1.0, 0.40, 0.48, 0.55, 0.61]
          - [1.4, 0.68, 0.75, 0.82, 0.87]
          - [1.6, 0.79, 0.85, 0.90, 0.93]
    figures_description:
      - "Fig: Power curves for single vs cumulative (2,3,4) administrations as function of effect size. Horizontal line at 0.70 target."
    analysis: >
      Cumulative Bayesian DIF在median档下是"promising but insufficient"的结果。
      对medium effects改善不够，对large effects marginal。Appendix supplementary。
      审稿人不会miss this——not a required contribution。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      正式分析benchmark validity在progressive item replacement下的degradation。
      5%, 10%, 20%, 50% replacement rates。
    expected_results:
      rho_5pct_replacement: 0.9991
      rho_10pct_replacement: 0.9982
      rho_20pct_replacement: 0.9958
      rho_31pct_replacement: 0.9935
      rho_50pct_replacement: 0.9870
      shr_5pct: 0.998
      shr_10pct: 0.996
      shr_20pct: 0.993
      shr_31pct: 0.989
      shr_50pct: 0.975
      construct_coverage_5pct: 0.99
      construct_coverage_31pct: 0.94
      construct_coverage_50pct: 0.86
      bootstrap_ci_rho_31pct: [0.991, 0.996]
      random_replacement_rho_31pct: 0.997
      targeted_dif_replacement_rho_31pct: 0.993
    result_rationale: >
      median档下graceful degradation的core finding与actual plan_017一致（ρ>0.99 even at 31%
      removal），但CIs wider。关键区别：(1) random replacement ρ=0.997 vs targeted DIF replacement
      ρ=0.993——DIF items carries slightly more ranking-relevant information than random items，
      但差异small；(2) construct coverage at 31% drops to 0.94——意味着6%的construct coverage
      loss，审稿人会问这是否trivial；(3) at 50% replacement ρ=0.987仍高，confirming massive
      redundancy。但median档下审稿人会argue：(a) replacement items的calibration quality
      未经验证（plan_006 failed），所以degradation analysis假设perfect replacement是unrealistic；
      (b) construct coverage loss of 6%在certain high-stakes contexts可能non-trivial。
      结论：clean supplementary result但不解决审稿人对replacement feasibility的concern。
    tables:
      - name: "Table: Validity Degradation Under Progressive Replacement"
        columns: [replacement_pct, spearman_rho, shr, construct_coverage, ci_95_rho]
        rows:
          - [5, 0.9991, 0.998, 0.99, "[0.9988, 0.9994]"]
          - [10, 0.9982, 0.996, 0.98, "[0.9976, 0.9988]"]
          - [20, 0.9958, 0.993, 0.96, "[0.9945, 0.9971]"]
          - [31, 0.9935, 0.989, 0.94, "[0.9910, 0.9960]"]
          - [50, 0.9870, 0.975, 0.86, "[0.9830, 0.9910]"]
    figures_description:
      - "Fig: ρ vs replacement rate curve. Gradual decline. Annotation at 31% showing DIF-targeted vs random replacement comparison."
    analysis: >
      Supports "instability ≠ invalidity" narrative。但在median档下，plan_006的failure意味着
      practical replacement尚不可行，so this analysis是theoretical exercise。
      Appendix supplementary，支持Claim 4的redundancy finding。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      实现Item-Focused Trees (Tutz & Berger 2016)。将model release date作为continuous covariate，
      避免arbitrary cohort splits。
    expected_results:
      n_items_analyzed: 12508
      ift_flagged_items_pct: 28.5
      ift_dif_mh_jaccard: 0.72
      ift_dif_mh_concordance: 0.78
      ift_unique_flags_pct: 5.2
      mh_unique_flags_pct: 7.8
      ift_temporal_gradient:
        pct_monotonic_increase: 35
        pct_monotonic_decrease: 28
        pct_nonlinear: 37
      ift_split_points_mode: "2023-Q4 to 2024-Q1"
      computational_cost_ratio_vs_mh: 15
    result_rationale: >
      median档下IFT flags 28.5% items（vs MH的31.3%），Jaccard=0.72说明substantial overlap但
      不identical。IFT的added value：(1) 37% items显示nonlinear temporal pattern——DIF不是
      monotonic drift而是有discontinuities，possibly reflecting specific model release waves；
      (2) 自动发现的split point集中在2023-Q4到2024-Q1，与MH的手动temporal split一致，
      validating cohort定义；(3) 5.2% IFT-unique flags是MH missed的——these tend to be items
      with small-but-continuous drift that doesn't cross ETS C threshold。但IFT computational
      cost 15× MH，且37% nonlinear patterns增加interpretation complexity。在median档下IFT是
      clean robustness check confirming MH findings are not artifact of arbitrary binary split，
      但不改变core conclusions。审稿人appreciate as supplementary validation。
    tables:
      - name: "Table: IFT vs MH-DIF Comparison"
        columns: [metric, IFT, MH_DIF]
        rows:
          - [flagged_pct, 28.5, 31.3]
          - [unique_flags_pct, 5.2, 7.8]
          - [overlap_jaccard, 0.72, 0.72]
          - [computational_cost_relative, 15x, 1x]
    figures_description:
      - "Fig: IFT temporal gradient for 3 example items showing monotonic increase, monotonic decrease, and nonlinear patterns."
    analysis: >
      IFT validates MH cohort split choice。nonlinear patterns add nuance but don't change
      core finding。Appendix supplementary robustness check。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      在decoder-only homogeneous subpopulation上运行DIF，检验architecture heterogeneity
      是否inflates spurious DIF。
    expected_results:
      n_decoder_only: 5222
      n_non_decoder: 5
      pct_decoder_only: 99.90
      decoder_only_c_pct: 31.2
      full_population_c_pct: 31.3
      jaccard_decoder_only_vs_full: 0.998
      irt_rmsea_full: 0.082
      irt_rmsea_decoder_only: 0.081
      irt_cfi_full: 0.72
      irt_cfi_decoder_only: 0.72
      lz_pct_above_2_full: 98.0
      lz_pct_above_2_decoder_only: 97.8
    result_rationale: >
      METABENCH MMLU中99.90%是decoder-only（5222/5227，排除5个encoder-decoder/encoder-only），
      所以architecture stratification几乎是no-op。C%从31.3%降至31.2%，Jaccard=0.998。
      关键insight：IRT fit metrics完全不改善（RMSEA=0.081 vs 0.082, CFI=0.72 vs 0.72）——
      这证明|Lz|>2的98% misfit不是由architecture heterogeneity驱动，而是MMLU inherent
      multidimensionality (57 subjects forced into 1D)。在median档下，这个结果虽然是
      "architecture is a non-issue"的强证据，但同时expose了一个更深的问题：如果IRT fit
      在homogeneous population下仍然terrible，那么所有基于1D IRT的DIF findings都建立在
      misspecified model上。审稿人（at least one）会将98% |Lz|>2视为fundamental concern，
      要求pilot multidimensional analysis——这是median档的defining reviewer concern之一。
    tables:
      - name: "Table: Architecture Stratification (Non-Issue Confirmation)"
        columns: [population, N, c_pct, rmsea, cfi, lz_pct_gt2]
        rows:
          - [full, 5227, 31.3, 0.082, 0.72, 98.0]
          - [decoder_only, 5222, 31.2, 0.081, 0.72, 97.8]
          - [delta, -5, -0.1, -0.001, 0.0, -0.2]
    figures_description:
      - "Fig: |Lz| distribution for full vs decoder-only populations. Nearly identical. Vertical line at |Lz|=2 showing 98% exceed threshold in both."
    analysis: >
      Architecture concern definitively resolved。但IRT misfit concern simultaneously
      amplified——这在median档下成为审稿人要求pilot MIRT的trigger。plan_005的bifactor failure
      意味着这个concern只能部分address（2-3 subject pilot），不能fully resolve。
      在Discussion中需要explicit subsection "IRT model misspecification bounds on our findings"。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: >
      在real METABENCH response matrix中注入known contamination，测量DIF detection power。
      Controlled ground truth避免Li et al. proxy label的circularity。
    expected_results:
      n_clean_items: 500
      n_injected_items: 150
      temporal_external_tpr_p0: 0.31
      temporal_external_tpr_p03: 0.45
      temporal_external_tpr_p05: 0.68
      temporal_external_tpr_p07: 0.88
      temporal_external_tpr_p10: 0.97
      temporal_external_fpr: 0.31
      temporal_external_delta_tpr_p05: 0.37
      temporal_external_delta_tpr_p10: 0.66
      cross_subject_delta_fpr: 0.001
      within_subject_fpr_inflation_p10: 0.19
      matching_variable_contamination_confirmed: true
      dose_response_monotonic: true
      injection_prevalence_sensitivity:
        pct_5_delta_tpr: 0.28
        pct_10_delta_tpr: 0.33
        pct_20_delta_tpr: 0.37
        pct_30_delta_tpr: 0.40
      exploitation_rate_sensitivity:
        p_04_delta_tpr: 0.12
        p_06_delta_tpr: 0.25
        p_08_delta_tpr: 0.45
        p_10_delta_tpr: 0.66
    result_rationale: >
      median档下semi-synthetic ΔTPR at p=0.5 = 0.37（在0.35-0.50 range内），低于actual的
      0.508(p=0.5)和0.674(p=1.0)。原因：(1) elevated baseline FPR=0.31意味着许多genuine DIF items
      已经被flagged在p=0（no injection），leaving less room for TPR increase on injected items；
      (2) at exploitation rate p=0.5，每个injected item仅50%概率flip incorrect→correct，
      effective DIF magnitude较小——power analysis预期δ≈0.8，落在operational region边缘
      （N≥80但δ<1.4）；(3) cross-subject matching ΔFPR=0.001是强正面结果——matching variable
      contamination完全isolated，confirming cross-subject matching是sound methodology；
      (4) within-subject matching FPR inflation +0.19 confirms the contaminated-matching-variable
      problem。dose-response monotonic是clean结果。在median档下审稿人acknowledge ΔTPR>0
      is significant但0.37 at p=0.5 is "moderate power"——semi-synthetic framework的value更多是
      methodology本身（reusable infrastructure）而非specific power numbers。这支持Claim 3作为
      primary contribution的repositioning。
    tables:
      - name: "Table: Semi-Synthetic Detection Power (Cross-Subject Matching)"
        columns: [exploitation_rate_p, tpr, fpr, delta_tpr, delta_fpr]
        rows:
          - [0.0_baseline, 0.31, 0.31, 0.0, 0.0]
          - [0.3, 0.45, 0.31, 0.14, 0.001]
          - [0.5, 0.68, 0.31, 0.37, 0.001]
          - [0.7, 0.88, 0.31, 0.57, 0.001]
          - [1.0, 0.97, 0.31, 0.66, 0.001]
      - name: "Table: Within-Subject vs Cross-Subject Matching FPR"
        columns: [matching_method, fpr_baseline, fpr_p10, delta_fpr]
        rows:
          - [within_subject, 0.31, 0.50, 0.19]
          - [cross_subject, 0.31, 0.311, 0.001]
    figures_description:
      - "Fig: Dose-response curve (ΔTPR vs exploitation rate p). Cross-subject matching (solid) vs within-subject (dashed). FPR inflation band for within-subject visible."
      - "Fig: ΔFPR across injection prevalence rates for cross-subject matching. Flat at ~0.001, confirming isolation."
    analysis: >
      Semi-synthetic framework是median档下最强contribution。ΔTPR=0.37 at p=0.5 is moderate
      but positive, dose-response is clean, cross-subject matching ΔFPR≈0 is the key
      methodological innovation。升级为primary contribution。审稿人在novelty score上
      给2.5-3.5但acknowledge framework reusability。

  - name: multi_benchmark_temporal_dif
    plan_id: plan_028
    description: >
      在METABENCH中的additional benchmarks (ARC, HellaSwag, WinoGrande, TruthfulQA)上
      运行temporal DIF，检验跨benchmark generalizability。
    expected_results:
      mmlu_c_pct: 31.3
      arc_c_pct: 22.5
      hellaswag_c_pct: 14.8
      winogrande_c_pct: 26.1
      truthfulqa_c_pct: 25.3
      gsm8k_c_pct: 15.2
      cross_benchmark_range: "14.8-31.3%"
      cross_benchmark_min: 14.8
      cross_benchmark_max: 31.3
      all_above_random_control: true
      random_control_max: 0.55
      min_enrichment_ratio: 27
      benchmarks_above_15pct: 5
      benchmarks_above_20pct: 4
      benchmarks_above_25pct: 3
      arc_random_c_pct: 0.50
      hellaswag_random_c_pct: 0.22
      winogrande_random_c_pct: 0.35
      truthfulqa_random_c_pct: 0.40
    result_rationale: >
      median档下cross-benchmark C% range为14.8-31.3%（在12-18% min, 28-32% max range内）。
      HellaSwag最低(14.8%)因为：(1) commonsense reasoning items更homogeneous，temporal drift
      较小；(2) 10042 items中许多是pattern-matching tasks，less susceptible to differential
      functioning across model generations。MMLU最高(31.3%)因为57 subjects的heterogeneity
      创造了更多DIF opportunity。ARC/WinoGrande/TruthfulQA在22-26%范围内。关键observation：
      所有6个benchmarks的C%都远高于random control (<0.6%)，enrichment ratio≥27，所以temporal
      DIF is pervasive。但median档下HellaSwag的14.8%略低于15% "flag" threshold（audit protocol
      three-tier中<15 = monitor only），这给了审稿人一个talking point："not all benchmarks
      reach concerning levels"。需要honest报告：4/6 benchmarks above 20%，2/6 below 20%。
      Cross-benchmark generalizability is "substantial but variable"而非"universal"。
    tables:
      - name: "Table: Multi-Benchmark Temporal DIF (2023 vs 2024)"
        columns: [benchmark, n_items, n_ref, n_foc, c_pct, random_c_pct, enrichment_ratio, audit_tier]
        rows:
          - [MMLU, 12508, 1080, 807, 31.3, 0.18, 174, act]
          - [WinoGrande, 1267, 1017, 803, 26.1, 0.35, 75, flag]
          - [TruthfulQA, 817, 1080, 807, 25.3, 0.40, 63, flag]
          - [ARC, 1172, 1080, 807, 22.5, 0.50, 45, flag]
          - [GSM8K, 1319, 1017, 804, 15.2, 0.25, 61, flag]
          - [HellaSwag, 10042, 1080, 807, 14.8, 0.22, 67, monitor]
    figures_description:
      - "Fig: Bar chart of C% by benchmark with random control overlay. All bars far exceed random. Horizontal lines at 15% (monitor) and 25% (flag) thresholds."
    analysis: >
      Multi-benchmark DIF strengthens generalizability claim但reveals variability。
      median档下HellaSwag < 15%给审稿人ammunition。framing应为"temporal measurement drift
      is a general phenomenon across LLM benchmarks (all >> random), with benchmark-specific
      magnitude reflecting task and item characteristics"。honest reporting of range。

  - name: permutation_null_c_rate
    plan_id: plan_029
    description: >
      1000× permutation test: 随机reassign temporal labels，建立C%的null distribution。
      回答"31% is above chance?"
    expected_results:
      n_permutations: 1000
      null_c_pct_mean: 5.2
      null_c_pct_sd: 0.8
      null_c_pct_95th_percentile: 6.5
      null_c_pct_99th_percentile: 7.3
      null_c_pct_max: 8.1
      observed_c_pct: 31.3
      permutation_p_value: "<0.001"
      z_score_observed_vs_null: 32.6
      excess_c_pct: 26.1
      within_cohort_random_split_c_pct: 0.18
      ratio_permutation_null_to_random_split: 28.9
    result_rationale: >
      median档下permutation null C%=5.2%（在3-8% range内），远高于within-cohort random split
      的0.18%但远低于observed 31.3%。5.2% null rate意味着：(1) temporal labels本身携带non-DIF
      signal——当你随机shuffe 2023/2024 labels时，模型composition的statistical properties
      (ability distribution, family structure, training recipe distribution) 被破坏，但残留的
      correlations between temporal label和model characteristics仍然产生~5% spurious DIF；
      (2) 这不是type-I error——permutation test正确preserve了model-level dependencies，
      5.2%反映的是temporal label作为proxy for multiple confounds的composite effect；
      (3) observed 31.3%仍以z=32.6 highly significant (p<0.001)，excess=26.1%是genuine。
      但审稿人会argue：(a) 5.2% null不trivial，说明temporal labels不是clean experimental
      manipulation；(b) permutation test只controls for label assignment，不controls for
      systematic differences in cohort composition（ability, training data vintage等）——
      plan_027的ability matching只addresses one such confound；(c) 真正的"after all controls"
      estimate可能需要subtract更多confounds。median档下effective C%=24.5%（31.3% - 5.2% null
      - 2.4pp ability - ~1pp other adjustments ≈ 22-25%）。审稿人接受这是significant但
      要求更careful attribution。
    tables:
      - name: "Table: Permutation Null Distribution"
        columns: [statistic, value]
        rows:
          - [null_mean_c_pct, 5.2]
          - [null_sd, 0.8]
          - [null_95th_percentile, 6.5]
          - [null_99th_percentile, 7.3]
          - [null_max, 8.1]
          - [observed_c_pct, 31.3]
          - [excess_over_null_mean, 26.1]
          - [z_score, 32.6]
          - [permutation_p, "<0.001"]
          - [within_cohort_random_c_pct, 0.18]
    figures_description:
      - "Fig: Histogram of 1000 permutation null C% values (mean=5.2%, tight distribution). Vertical red line at observed 31.3%. Massive separation. Inset shows null distribution detail."
    analysis: >
      Permutation null是median档的defining result。5.2%建立了proper baseline——31.3%仍highly
      significant但需要honest报告excess=~26%而非31%。审稿人一的concern不是significance
      而是interpretation："what does the 5.2% null represent?" 这需要explicit discussion
      of temporal label as composite proxy for multiple factors (ability, training data,
      architecture evolution, RLHF practices)。median档下这个5.2%成为"conservative controls"
      narrative的anchor point。

  - name: odds_ratio_regression_transparency
    plan_id: plan_030
    description: >
      补充odds ratio + 95% CI + McFadden/Nagelkerke R² + deviance ratio。
      Item-level accuracy change作为finer-grained predictor。
    expected_results:
      model1_domain_delta:
        mcfadden_r2: 0.0007
        nagelkerke_r2: 0.0012
        subject_acc_delta_or_per_010: 1.55
        subject_acc_delta_ci_per_010: [1.19, 2.03]
      model2_domain_delta_plus_items:
        mcfadden_r2: 0.042
        nagelkerke_r2: 0.071
        ctt_difficulty_or_per_010: 0.78
        ctt_discrimination_or_per_010: 1.51
      model3_item_delta:
        mcfadden_r2: 0.0012
        nagelkerke_r2: 0.0021
        item_acc_change_or_per_010: 1.08
        item_acc_change_ci: [1.02, 1.14]
      model4_item_delta_plus_items:
        mcfadden_r2: 0.043
        nagelkerke_r2: 0.073
        simpsons_paradox: true
      lr_test_m1_vs_m2_chi2: 645
      lr_test_m3_vs_m4_chi2: 653
      best_model_r2: 0.073
      deviance_explained_pct: 7.3
    result_rationale: >
      median档下odds ratio regression结果与actual一致——这是deterministic statistical analysis
      on fixed data。McFadden R²=0.0007 (domain-level predictor alone) confirms domain
      improvement explains essentially nothing at item level。Model 4 (item Δ + item props)
      的Nagelkerke R²=0.073意味着所有可观测predictors combined仅解释7.3%的DIF variance——
      92.7%是unexplained，supporting "instability is predominantly item-specific"。
      Simpson's paradox在Model 2→4 transition中再现：item accuracy change OR从1.55 (positive,
      Model 1)翻转为0.92 (negative, Model 4) when item properties are controlled——说明
      difficulty和discrimination是confounders。在median档下审稿人accept这作为thorough
      transparency analysis但会note：(1) 7.3% total R² means our understanding of DIF
      drivers is very limited; (2) unmeasured item-level confounds (topic specificity,
      question format, cognitive level) might explain more; (3) Simpson's paradox means
      Model 1 should NOT be used for causal interpretation。paper应使用Model 1 as primary
      (descriptive) with Model 4 as supplementary (adjusted)。
    tables:
      - name: "Table: Logistic Regression Models for DIF Prediction"
        columns: [model, predictors, mcfadden_r2, nagelkerke_r2, aic, key_or]
        rows:
          - [M1, domain_acc_delta, 0.0007, 0.0012, 15545, "1.55 per 0.10"]
          - [M2, "M1 + item_props", 0.042, 0.071, 14902, "difficulty 0.78, disc 1.51"]
          - [M3, item_acc_delta, 0.0012, 0.0021, 15537, "1.08 per 0.10"]
          - [M4, "M3 + item_props", 0.043, 0.073, 14885, "acc_Δ 0.92 (reversed)"]
    figures_description:
      - "Fig: Forest plot of ORs (per 0.10 unit) across 4 models. Simpson's paradox highlighted: acc_delta OR flips from >1 to <1 when item properties are added."
    analysis: >
      Odds ratio transparency analysis是clean supplementary work。confirms <8% variance
      explained。在median档下审稿人appreciate transparency but note limited explanatory power
      as a gap. Simpson's paradox需要explicit discussion as a caution for interpretation.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c62653c-d467-4da9-b6a3-9047e9d5f2a0",
  "isSidechain": false,
  "requestId": "req_011CbG5SmRfeud1Nknj4RKfF",
  "type": "assistant",
  "uuid": "73279f43-b51f-4b4a-80b0-ee61c1d4f2ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2cdYo7ruibSFo2WQTtsDd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24029,
      "cache_read_input_tokens": 11841,
      "output_tokens": 19061,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24029,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 19061,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24029
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心发现成立但部分robustness弱于预期，1-2个审稿人有实质性concern，需要major revision后accept 核心假设：['plan_029 permutation null C% = 3-8%，仍显著但审稿人质疑temporal label本身携带非DIF信号', 'plan_0…",
  "leafUuid": "73279f43-b51f-4b4a-80b0-ee61c1d4f2ba",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Temporal DIF characterization with semi-synthetic validation",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心发现成立但部分robustness弱于预期，1-2个审稿人有实质性concern，需要major revision后accept 核心假设：['plan_029 permutation null C% = 3-8%，仍显著但审稿人质疑temporal label本身携带非DIF信号', 'plan_0…",
  "leafUuid": "73279f43-b51f-4b4a-80b0-ee61c1d4f2ba",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Temporal DIF characterization with semi-synthetic validation",
  "sessionId": "3706d8e3-1bea-4a7e-8c25-1c276c952e0c"
}
```

---
