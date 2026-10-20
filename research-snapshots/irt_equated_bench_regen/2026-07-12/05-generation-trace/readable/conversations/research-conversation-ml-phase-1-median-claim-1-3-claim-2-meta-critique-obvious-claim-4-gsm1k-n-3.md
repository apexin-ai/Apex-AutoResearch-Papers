# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Claim 1+3 稳固；Claim 2 meta-critique 被部分评审视为 obvious；Claim 4 的 GSM1K 部分 (N=3

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/bbb05643-251b-40fa-a591-630f63d2ac60.jsonl`
- **Structured JSON:** [`49407618df2f3ae2cadf.json`](../../sessions/49/49407618df2f3ae2cadf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T06:29:13.167Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T06:29:13.167Z",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Claim 1+3 稳固；Claim 2 meta-critique 被部分评审视为 obvious；Claim 4 的 GSM1K 部分 (N=33) 被 dismiss；novelty 受质疑但不致命\n核心假设：[\"A1 部分成立：1-2 个评审质疑 novelty（'just applying MH-DIF at scale'），但不构成 unanimous reject reason\", 'A2 成立但被加重：评审要求在 limitations 中更详细讨论 IRT misspecification 的 downstream 影响，可能要求补充 sensitivity analysis', \"A3 部分成立：'instability ≠ invalidity' 对部分评审说服力不足——'if rankings don't change, why should I care?' 需要更强的 practical implication\", \"A4 不完全成立：1-2 个评审认为 meta-critique 'obvious in hindsight'，降低其作为独立贡献的权重\", 'A5 成立：item characterization 被认可，但评审要求更多 causal evidence 而非 correlational', 'A6 不成立：GSM1K r=-0.478 因 N=33 和宽 CI 被 dismiss，Claim 4 失去 cross-benchmark contamination-resistance 子发现']\n关键指标范围：{'reviewer_avg_score': [4.5, 6.0], 'acceptance_probability_pct': [20, 45], 'claims_at_full_strength': [2, 3], 'novelty_sub_score_avg': [2.0, 2.5], 'reviewers_flagging_irt_as_fatal': [0, 2], 'major_revisions_needed': [2, 3]}\n叙事方向：需要调整 claims 权重和补充实验。策略一：将 Claim 2 meta-critique 从独立贡献降级 为 Claim 3 semi-synthetic framework 的动机段（\"because web-overlap labels can't validate differential detectors, we need a controlled framework\"），合并为 3 claims 结构。策略二：强化 Claim 4 的 practical actionability——不只 \"DIF as diagnostic lens\" 的发现陈述，而是给出具体 recommendation（e.g., \"benchmark maintainers should run temporal DIF every 6 months and report C% as a stability metric\"）， 让 \"so what\" 有落地答案。策略三：对 GSM1K 部分做降级处理——从 Claim 4 子发现移至 Appendix 的 \"suggestive evidence\"，主文只用 plan_017 的 z-score + plan_020 的 circularity ablation 支撑 Claim 4。可能需要补充一个实验：在 2-3 个 MMLU 高 C% subject 上跑 multidimensional IRT（哪怕 2-factor bifactor），展示 DIF 发现在 改善 IRT fit 后仍然稳健，直接回应 misspecification concern。Rebuttal 需准备 novelty 的 explicit defense paragraph。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nfocus: Dream #4 后的改进：(1) plan_022 model independence — graduated de-duplication 证明 family structure 不 inflate C%；(2) plan_023 item characterization — difficulty×direction ρ=-0.597 强化 diagnostic lens；(3) 删除 unprovenanced r=-0.347；(4) K=10 数据修正；(5) 所有 critical 写作问题已修复。关注 novelty 和 IRT misspecification 是否仍是主要扣分项。\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T06:29:13.171Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T06:29:13.171Z",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T06:29:13.193Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Claim 1+3 稳固；Claim 2 meta-critique 被部分评审视为 obvious；Claim 4 的 GSM1K 部分 (N=33) 被 dismiss；novelty 受质疑但不致命
核心假设：["A1 部分成立：1-2 个评审质疑 novelty（'just applying MH-DIF at scale'），但不构成 unanimous reject reason", 'A2 成立但被加重：评审要求在 limitations 中更详细讨论 IRT misspecification 的 downstream 影响，可能要求补充 sensitivity analysis', "A3 部分成立：'instability ≠ invalidity' 对部分评审说服力不足——'if rankings don't change, why should I care?' 需要更强的 practical implication", "A4 不完全成立：1-2 个评审认为 meta-critique 'obvious in hindsight'，降低其作为独立贡献的权重", 'A5 成立：item characterization 被认可，但评审要求更多 causal evidence 而非 correlational', 'A6 不成立：GSM1K r=-0.478 因 N=33 和宽 CI 被 dismiss，Claim 4 失去 cross-benchmark contamination-resistance 子发现']
关键指标范围：{'reviewer_avg_score': [4.5, 6.0], 'acceptance_probability_pct': [20, 45], 'claims_at_full_strength': [2, 3], 'novelty_sub_score_avg': [2.0, 2.5], 'reviewers_flagging_irt_as_fatal': [0, 2], 'major_revisions_needed': [2, 3]}
叙事方向：需要调整 claims 权重和补充实验。策略一：将 Claim 2 meta-critique 从独立贡献降级 为 Claim 3 semi-synthetic framework 的动机段（"because web-overlap labels can't validate differential detectors, we need a controlled framework"），合并为 3 claims 结构。策略二：强化 Claim 4 的 practical actionability——不只 "DIF as diagnostic lens" 的发现陈述，而是给出具体 recommendation（e.g., "benchmark maintainers should run temporal DIF every 6 months and report C% as a stability metric"）， 让 "so what" 有落地答案。策略三：对 GSM1K 部分做降级处理——从 Claim 4 子发现移至 Appendix 的 "suggestive evidence"，主文只用 plan_017 的 z-score + plan_020 的 circularity ablation 支撑 Claim 4。可能需要补充一个实验：在 2-3 个 MMLU 高 C% subject 上跑 multidimensional IRT（哪怕 2-factor bifactor），展示 DIF 发现在 改善 IRT fit 后仍然稳健，直接回应 misspecification concern。Rebuttal 需准备 novelty 的 explicit defense paragraph。


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
  "promptId": "58ae16a9-870a-475c-aa7a-b0cad29e25e4",
  "type": "user",
  "uuid": "ca6b4046-23af-4da3-a9c7-ee8b976730d3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T06:29:13.191Z_

```json
{
  "parentUuid": "ca6b4046-23af-4da3-a9c7-ee8b976730d3",
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
  "uuid": "2efa1d83-d57b-46ad-830d-13253e7a716b",
  "timestamp": "2026-05-21T06:29:13.191Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T06:29:13.191Z_

```json
{
  "parentUuid": "2efa1d83-d57b-46ad-830d-13253e7a716b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "02cca741-9ae1-4c24-ae16-f7a115ce51f6",
  "timestamp": "2026-05-21T06:29:13.191Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claim 1+3 稳固；Claim 2 meta-critique 被部分评审视为 obvious；Claim 4 的 GSM1K 部分 (N=33) 被 dismiss；novelty 受质疑但不致命 核心假设：[\"A1 部分成立：1-2 个评审质疑 novelty（'just applying MH…",
  "leafUuid": "02cca741-9ae1-4c24-ae16-f7a115ce51f6",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF analysis reveals MMLU temporal instability and validates semi-synthetic framework",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60"
}
```

---

### Assistant

_source line 8 · 2026-05-21T06:30:10.496Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "median" tier scenario defined in Phase 1. I need to go through each experiment that has status "planned" and predict what results would look like in the median outcome scenario.

Let me identify the planned experiments:
1. plan_001 - real_data_dif_mmlu - status: planned (but wait, there's a registry entry plan_001_real_data_dif_mmlu with status DONE)
2. plan_002 - rl_robustness_validation - status: planned


3. plan_003a - constat_perturbation_eval - status: planned
4. plan_003b - dvd_generation_variance_eval - status: planned
5. plan_003c - ensemble_fusion - status: planned
6. plan_004 - cross_benchmark_gsm8k - status: planned (but registry shows DONE)
7. plan_005 - bifactor_irt_equating_pilot - status: planned (registry shows plan_015 as killed)
8. plan_006 - item_generation_calibration - status: planned
9. plan_007 - cumulative_bayesian_dif - status: planned
10. plan_008 - graceful_degradation_analysis - status: planned
11. plan_009 - item_focused_trees - status: planned
12. plan_010 - architecture_stratified_dif - status: planned
13. plan_011 - semi_synthetic_contamination_validation - status: planned (registry shows DONE, with results in paper_framing)

I'm noticing a mismatch between the experiment_plan and the registry—many experiments marked as planned here already have completed results in the registry. The user is asking for detailed predictions across all planned experiments, so I think they want me to generate median-tier results for each one listed, whether or not they've already been run. Some experiments appear in both lists, which suggests I should treat them as needing predictions regardless of their actual completion status.

I'm also seeing several experiments mentioned in paper_framing that don't appear in the experiment_plan list at all—plan_018 through plan_022 covering threshold sensitivity, decomposition, circularity ablation, LR-DIF, and model independence. I need to account for these gaps when generating the full set of predictions.

For the median-tier scenario, I'm thinking about what the results would look like: Claims 1 and 3 holding up well, Claim 2 seen as somewhat obvious in its meta-critique, Claim 4 struggling with the small GSM1K sample, and novelty concerns present but not disqualifying. This translates to reviewer scores in the 4.5-6.0 range, acceptance probability between 20-45%, and maybe 2-3 claims at full strength.

The key friction points I'm anticipating: a couple reviewers will question whether the novelty is really there, the IRT misspecification issue needs more thorough treatment, the argument that instability doesn't invalidate the approach won't fully land, and the item characterization work will be recognized but flagged as needing causal grounding rather than just correlational evidence.

Looking at the actual experiments, plan_001 is already in the registry with temporal consistency at 31.3% and enrichment around 0.96—those numbers would survive in the median tier but face pushback on novelty and IRT concerns. For plan_002, I'm examining the robustness across 13 reasoning-RL models.

The RL cohort is too small to reach statistical significance, and the equivalence test doesn't give me a clear answer. Alignment-RL models show decent overlap with SFT detections around 0.7 Jaccard similarity, but the reasoning models are underpowered. Traditional detectors degrade on RL models but the confidence intervals are too wide to be conclusive. For the perturbation approach, paraphrasing quality varies and ConStat catches some items, though the FDR-controlled detection has only moderate power and doesn't correlate strongly with DIF flags. The generation variance experiment shows bimodal distributions in some cases but the signal is noisy—I can detect verbatim contamination reasonably well but variants are harder to catch. The ensemble fusion approach would depend on how well those earlier experiments perform, and even in the best case it only gives marginal gains without consistently hitting the false positive rate target. Plan_004 is already done with the GSM1K data.

Moving forward, the bifactor IRT equating pilot shows the model converges but the fit is mediocre and the equated scores barely improve over classical test theory. Item generation has moderate difficulty correlation with originals around 0.4-0.5, and student simulation helps but doesn't close the gap. The cumulative Bayesian DIF approach shows power improvements in simulation but there's a gap between simulated and real-world performance. Graceful degradation holds up to about 20% replacement before construct coverage starts eroding. The item-focused trees approach is still being evaluated.

For the remaining experiments, the release date patterns mirror the categorical DIF findings without major divergence. Architecture stratified DIF confirms that decoder-only architecture isn't a limiting factor. The semi-synthetic experiment already shows a true positive rate improvement of 0.508 at p=0.5 with zero false positive rate difference across subjects.

Now I need to clarify which experiments are actually completed versus planned, since the registry shows several as done while the experiment plan lists them all as planned. I should organize the predictions systematically with the actual data points and rationales for each. I need to reconcile what's actually in the registry versus what's listed in the experiment plan. Looking at the framing, plan_010 was definitely executed with those specific results, even though it's not explicitly showing up in my registry list. And plan_005 got killed as plan_015_bifactor_irt, so that's a dead end. For the rest, I'll go through each planned experiment and either pull actual results where they exist or construct plausible median-scenario predictions for the ones still pending. Writing detailed predictions...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02cca741-9ae1-4c24-ae16-f7a115ce51f6",
  "isSidechain": false,
  "requestId": "req_011CbFEypRAJGXZzxoowz8Cz",
  "type": "assistant",
  "uuid": "c7778196-2239-40e6-a48d-1f44c0fdbe6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017f7qFMfS94Zk2WpDi8Sf9G",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19004,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16275,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19004
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

_source line 9 · 2026-05-21T06:34:39.891Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1 (31.3% temporal instability) 和 Claim 3 (semi-synthetic framework) 是主要得分点。
  Claim 2 meta-critique 被 1-2 个评审视为 "obvious in hindsight"，独立贡献权重下降。
  Claim 4 的 GSM1K 子发现 (N=33) 被 dismiss，plan_017 的 z-score 证据保留但 "so what" 回应不足。
  Novelty 受质疑（"just MH-DIF at scale"）但不构成 unanimous reject。IRT misspecification
  被要求补充 sensitivity analysis（可能需要 multidimensional IRT pilot）。
  整体：reviewer avg 5.0-5.5，acceptance probability ~30%，需要 2-3 major revisions。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      METABENCH MMLU 全量 DIF 分析。temporal/ability/within-family 三种 cohort 定义，
      加 Li et al. proxy validation 和 domain specificity。
    expected_results:
      temporal_ets_c_pct: 31.3
      temporal_n_c_items: 3918
      temporal_n_total: 12508
      temporal_fpr_on_li_clean: 0.318
      temporal_enrichment_ratio: 0.96
      ability_ets_c_pct: 2.9
      ability_enrichment: 1.19
      within_family_llama2v3_c_pct: 61.3
      within_family_mistral_mixtral_c_pct: 38.7
      domain_spearman_rho: 0.307
      domain_spearman_p: 0.02
      sanity_random_split_c_pct: 0.18
      temporal_ability_jaccard: 0.014
    result_rationale: >
      median 档下这些数值本身站得住——31.3% 是 robust 的经验发现，random-split sanity (0.18%) 排除统计伪影，
      domain ρ=0.307 是 modest ecological correlation。问题不在数字，在解读：
      1) enrichment≈1.0 证明 DIF 和 web-overlap labels 正交，但评审会问 "if DIF doesn't
      correlate with known contamination, what IS it detecting?"——需要 plan_019 decomposition
      才能回答 "item-specific instability, not capability gain"。
      2) within-family C%=61.3% (Llama-2 vs 3) 远高于 cross-cohort 31.3%，评审会质疑
      "within-family analysis proves capability gain drives DIF, not contamination"。
      Median 档下 1 个评审接受 "capability gain ≠ item instability" 论证，1 个不接受。
      3) domain ρ=0.307 (p=0.02) 在 median 档被视为 "interesting but not definitive"，
      不被攻击也不加分。
    tables:
      - name: "Table 1: Temporal DIF Summary by ETS Classification"
        columns: [ets_class, n_items, pct, mean_abs_delta_mh]
        rows:
          - [A (negligible), 8590, 68.7, 0.43]
          - [B (moderate), 2641, 21.1, 1.24]
          - [C (large), 1277, 10.2, 2.31]
          - ["B+C (flagged)", 3918, 31.3, 1.58]
      - name: "Table 2: Cohort Definition Sensitivity"
        columns: [cohort, n_ref, n_foc, c_pct, enrichment]
        rows:
          - [temporal (2023 vs 2024-H1), 1253, 656, 31.3, 0.96]
          - [ability (Q1 vs Q5), "~1044", "~1044", 2.9, 1.19]
          - [within-family (Llama-2 vs 3), 161, 308, 61.3, "—"]
          - [random split (sanity), 950, 950, 0.18, "—"]
    figures_description:
      - "Fig 1: Histogram of |Δ_MH| across 12,508 items with ETS A/B/C thresholds marked. Long right tail (skewness ~1.8). 评审在 median 档认为 visualization 清晰。"
      - "Fig 2: Domain specificity heatmap — 57 MMLU subjects × C% with ρ=0.307 annotation. Colorbar shows range 20.7-48.4%。评审会注意到 spread 大，但不会单独攻击。"
    analysis: >
      Median 档下 plan_001 是 paper 的基石。数据本身不受质疑，但 "so what" 需要后续实验
      (plan_019, plan_017, plan_020) 支撑。评审预期反应：
      R1: "Impressive scale, but what does 31% instability mean for practitioners?"
      R2: "The enrichment≈1.0 result is interesting but undermines the contamination framing"
      R3: "Within-family results suggest capability gain, not contamination"
      总体：plan_001 在 median 档得 strong accept 作为 empirical contribution，
      但单独不够——需要 downstream impact story。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      验证 DIF 在 RL-trained 模型上的鲁棒性。SFT baseline vs alignment-RL (DPO/ORPO)
      vs reasoning-RL (GRPO/PPO)。关键在于 reasoning-RL 只有 10-15 个模型。
    expected_results:
      sft_cohort_n: 312
      alignment_rl_cohort_n: 477
      reasoning_rl_models_collected: 13
      sft_vs_alignment_jaccard_dif_flags: 0.72
      sft_temporal_c_pct: 30.8
      alignment_rl_temporal_c_pct: 32.1
      combined_with_reasoning_rl_c_pct: 31.5
      jaccard_base_vs_rl_augmented: 0.91
      tost_equivalence_p: 0.14
      tost_equivalence_bound: 0.05
      tost_verdict: inconclusive
      mink_auroc_sft: 0.61
      mink_auroc_alignment_rl: 0.58
      mink_auroc_reasoning_rl: 0.43
      constat_auroc_sft: 0.64
      constat_auroc_reasoning_rl: 0.39
      delong_p_mink_sft_vs_rl: 0.08
      delong_p_constat_sft_vs_rl: 0.03
      bootstrap_ci_auroc_diff_mink: [-0.02, 0.38]
      bootstrap_ci_auroc_diff_constat: [0.04, 0.46]
      power_analysis_delta_boundary: 1.1
      power_analysis_tpr_at_boundary: 0.42
    result_rationale: >
      Median 档核心问题：N=13 reasoning-RL 模型严重不足。
      1) Group-level DIF flags 在加入 13 个 RL 模型后变化很小 (Jaccard=0.91)，因为
      N=13 在 N≈1900 focal cohort 中占比 <1%，统计上几乎无影响。评审会正确指出
      "this doesn't prove RL robustness, it proves RL models are too few to matter"。
      2) TOST 等价性检验 p=0.14 不显著——无法证明等价，也无法证明差异。
      Median 档评审判断：inconclusive，移至 limitations。
      3) 个体模型检测：ConStat 在 reasoning-RL 上 AUROC 降至 0.39 (显著下降)，
      但 DIF 是 group-level 无法做个体比较，comparison 不对等。
      4) Power analysis 有理论价值：δ<1.1 时 TPR<0.42，清晰刻画了 detection boundary。
      但评审会说 "you characterized a limitation, not solved it"。
      总体：plan_002 在 median 档被降级为 appendix，N=13 是 fatal underpowering。
    tables:
      - name: "Table: DIF Flag Stability Under Cohort Composition Change"
        columns: [cohort_composition, n_total, c_pct, jaccard_vs_baseline]
        rows:
          - [SFT only, 312, 30.8, "—"]
          - [SFT + alignment-RL, 789, 32.1, 0.72]
          - [SFT + alignment-RL + reasoning-RL, 802, 31.5, 0.91]
      - name: "Table: Individual Detector AUROC by Model Type"
        columns: [detector, sft, alignment_rl, reasoning_rl, delong_p]
        rows:
          - [Min-K%, 0.61, 0.58, 0.43, 0.08]
          - [ConStat, 0.64, 0.60, 0.39, 0.03]
          - [DIF (group), "—", "—", "—", "N/A"]
    figures_description:
      - "Fig: Power curve — TPR vs δ for exploitation rate p ∈ {0.4, 0.6, 0.8, 1.0}. 显示 δ=1.1 是 practical detection boundary。曲线 shape 合理但评审会标注 'simulation-derived, not empirically validated at these operating points'。"
    analysis: >
      Median 档下 plan_002 是最弱的实验。N=13 reasoning-RL 无法支撑任何统计结论。
      TOST inconclusive 意味着既不能声称 robust 也不能声称 fragile。
      最佳策略：power analysis 图放 appendix，主文用一句话承认 "reasoning-RL validation
      remains underpowered (N=13); alignment-RL cohort (N=477) shows stable DIF flags
      (Jaccard=0.72 vs SFT)"。不把 RL robustness 作为 claim。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      独立评估 ConStat-style perturbation testing 在 MMLU 上的检测力。
      200+ items paraphrased，comparison with DIF flags。
    expected_results:
      n_items_paraphrased: 217
      paraphrase_quality_human_eval: 0.78
      constat_detection_rate_fdr005: 0.23
      constat_detection_rate_fdr010: 0.31
      constat_dif_overlap_jaccard: 0.08
      constat_fpr_on_clean_items: 0.06
      constat_effect_size_non_rl: 0.74
      constat_effect_size_rl: 0.31
      paraphrase_difficulty_shift_mean: 0.12
      paraphrase_difficulty_shift_std: 0.34
      n_models_tested: 15
      gpu_hours_used: 62
    result_rationale: >
      Median 档：ConStat 实验执行了但结果 mixed。
      1) Paraphrase 质量 78% human-eval acceptable——约 22% 的 reformulation 引入了
      subtle semantic shift，导致 difficulty 变化不纯粹来自 contamination。
      评审会质疑 paraphrase 质量是 confound。
      2) FDR-controlled detection rate 23% 在 non-RL 模型上——reasonable baseline 但
      不 impressive。Jaccard=0.08 与 DIF 几乎无 overlap，说明两者 detect 不同 signal。
      3) RL 模型上 effect size 从 0.74 降至 0.31——方向正确但 N=15 模型下 CI 非常宽。
      4) 核心问题：ConStat 需要 inference access (running paraphrased items through models)，
      而 METABENCH 只有 original responses。所以 ConStat 只在 15 个有 inference access
      的模型上跑，vs DIF 用全部 5,227 模型。Scale 不可比。
      Median 档评审判断："useful baseline comparison but limited by small inference sample"。
    tables:
      - name: "Table: ConStat Detection Summary"
        columns: [metric, non_rl_models, rl_models, all]
        rows:
          - [n_models, 11, 4, 15]
          - [detection_rate_fdr005, 0.27, 0.14, 0.23]
          - [mean_effect_size, 0.74, 0.31, 0.61]
          - [FPR, 0.05, 0.08, 0.06]
    figures_description:
      - "Fig: Scatter plot of ConStat score vs DIF |Δ_MH| for 217 items. 几乎无 correlation (r=0.06)，两个方法 orthogonal。评审可能认为这支持 ensemble 价值，也可能认为这说明两者 detect 不同 construct。"
    analysis: >
      Median 档下 plan_003a 提供了有价值的 baseline comparison，但不构成独立贡献。
      ConStat-DIF orthogonality (Jaccard=0.08) 支持 meta-critique (不同方法 capture
      不同 aspects)，但 N=15 模型限制了结论强度。适合 appendix 作为 related work
      empirical comparison，不适合 main body。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      DVD generation variance 在 MMLU 上的独立评估。50 responses/item via temperature sampling。
    expected_results:
      n_models_tested: 12
      n_items_tested: 500
      responses_per_item: 50
      temperature: 0.8
      bimodal_detection_rate: 0.14
      bimodal_verbatim_contamination: 0.31
      bimodal_variant_contamination: 0.06
      dvd_dif_overlap_jaccard: 0.05
      dvd_fpr: 0.09
      variance_score_reliability: 0.62
      gpu_hours_used: 58
    result_rationale: >
      Median 档：DVD 结果较弱。
      1) 只有 14% 的 items 显示 bimodal generation variance——远低于 DIF 的 31.3%，
      说明 generation variance 作为 contamination signal 灵敏度较低。
      2) Verbatim contamination (31% bimodal) vs variant contamination (6% bimodal)：
      DVD 几乎只能 detect verbatim memorization，对 variant 无力。
      3) 与 DIF 的 overlap 近乎为零 (Jaccard=0.05)，再次说明不同方法 capture 不同 signal。
      4) Variance score reliability 0.62——moderate at best。50 responses 可能不足以
      稳定估计 variance，但 GPU budget 已耗尽。
      5) 核心限制：DVD 需要 open-weight + inference，排除 closed-source models。
      Median 档评审："limited detection power, primarily captures verbatim memorization
      which is already detectable by simpler methods (n-gram matching)"。
    tables:
      - name: "Table: DVD Detection by Contamination Type"
        columns: [contamination_type, n_items_tested, bimodal_rate, fpr]
        rows:
          - [verbatim, 150, 0.31, 0.08]
          - [variant, 150, 0.06, 0.10]
          - [clean, 200, "—", 0.09]
    figures_description:
      - "Fig: Violin plots of generation variance scores for bimodal (detected) vs unimodal items. Separation visible but overlap substantial。"
    analysis: >
      Median 档下 plan_003b 是最弱的独立实验。Detection power 低于 ConStat，
      且需要 open-weight inference access。主要价值是证明 "generation variance alone
      is insufficient"——但这不是 surprising finding。Appendix material at best。
      在 median 档的策略调整中，plan_003b 应被 deprioritized。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      DIF + ConStat + DVD 三信号 ensemble。依赖 003a 和 003b。
    expected_results:
      ensemble_auroc_2of3: 0.58
      ensemble_auroc_weighted: 0.62
      ensemble_fpr_2of3: 0.11
      ensemble_fpr_weighted: 0.09
      dif_standalone_auroc: 0.54
      constat_standalone_auroc: 0.51
      dvd_standalone_auroc: 0.47
      ensemble_improvement_over_best_single: 0.08
      cross_val_weight_stability: 0.43
      fpr_below_010_pct_configs: 0.45
    result_rationale: >
      Median 档：ensemble 无法达到预期目标。
      1) FPR<0.10 只在 45% 的配置下成立——不满足 "across all configurations" 的目标。
      Weighted fusion FPR=0.09 勉强达标，但 cross-val weight stability=0.43 说明
      weights 在 folds 之间不稳定，overfitting risk 高。
      2) AUROC 提升 +0.08 over best single signal——marginal，且受限于
      ground truth 的质量（Li et al. labels 作为 ground truth 本身是 plan 质疑的对象）。
      3) 根本矛盾：paper 的 Claim 2 论证 web-overlap labels 不适合评估 item-level
      detectors，然后用这些 labels 训练 ensemble weights。评审会指出 circularity。
      4) 003a/003b 的小样本 (N=12-15 models) 使得 ensemble 的 training data 极有限。
      Median 档评审："the ensemble adds complexity without resolving the fundamental
      ground truth problem the paper itself identifies"。
    tables:
      - name: "Table: Ensemble vs Individual Detectors"
        columns: [method, auroc, fpr, n_models_available]
        rows:
          - [DIF (MH), 0.54, 0.31, 5227]
          - [ConStat, 0.51, 0.06, 15]
          - [DVD, 0.47, 0.09, 12]
          - [2-of-3 majority, 0.58, 0.11, 12]
          - [weighted fusion, 0.62, 0.09, 12]
    figures_description:
      - "Fig: ROC curves for individual detectors and ensemble. Ensemble curve marginally above individual curves, but 95% CI bands overlap substantially。"
    analysis: >
      Median 档下 plan_003c 被 drop 是正确决策。Ensemble 面临三重困难：
      (a) ground truth circularity, (b) small-N signal components, (c) marginal improvement。
      Paper framing 已正确将 ensemble 移至 "future work"。
      在 rebuttal 中，如果评审问 "why not ensemble?"，回答是
      "ensemble requires validated ground truth, which our Claim 2 shows doesn't exist;
      building the ground truth infrastructure (Claim 3) is prerequisite"。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      GSM8K 上复制 DIF 分析，GSM1K 作为 contamination ground truth。三步：
      temporal DIF → semi-synthetic → GSM1K correlation。
    expected_results:
      step1_gsm8k_n_items: 1319
      step1_n_ref: 1017
      step1_n_foc: 804
      step1_standard_c_pct: 18.9
      step1_external_c_pct: 47.4
      step1_sanity_c_pct: 0.3
      step1_standard_external_spearman: 0.926
      step2_standard_delta_tpr_p10: 0.818
      step2_external_delta_tpr_p10: 0.517
      step3_n_models: 33
      step3_pearson_r: -0.478
      step3_pearson_p: 0.005
      step3_spearman_rho: -0.403
      step3_spearman_p: 0.020
      step3_partial_r: -0.385
      step3_partial_p: 0.027
      step3_bca_ci_pearson: [-0.714, -0.155]
      step3_bca_ci_spearman: [-0.687, -0.031]
      step3_permutation_p: 0.014
    result_rationale: >
      Median 档核心动态：Step 1+2 稳固，Step 3 被 dismiss。
      1) Step 1: GSM8K C%=18.9% (低于 MMLU 31.3%) 合理——GSM8K 是 math domain，
      temporal capability gain 更 uniform，所以 differential 更少。评审接受。
      2) Step 2: ΔTPR=+0.818 非常强——比 MMLU 的 +0.674 还好，因为 GSM8K 是
      single-domain，within-subject/cross-subject 区分不 applicable，matching 更干净。
      Semi-synthetic framework portability 得到确认，Claim 3 加分。
      3) Step 3: r=-0.478, p=0.005 但 N=33，BCa CI upper bound |r|=0.155。
      Median 档下 1-2 个评审直接 dismiss：
      - "N=33 with Spearman CI touching zero (−0.031) — underpowered"
      - "BCa CI [−0.714, −0.155] is too wide to be informative"
      - "contamination gap is itself a noisy proxy"
      方向正确 (negative correlation = DIF items resist contamination gains) 但
      统计力不足以成为 independent evidence。
      4) 策略：median 档下 Step 3 从 Claim 4 子发现降级至 appendix "suggestive evidence"，
      Claim 4 主要靠 plan_017 z-score + plan_020 circularity ablation。
    tables:
      - name: "Table: GSM8K Temporal DIF Summary"
        columns: [matching, c_pct, sanity_c_pct, delta_tpr_p10]
        rows:
          - [standard (total score), 18.9, 0.3, 0.818]
          - [external (MMLU score), 47.4, "—", 0.517]
      - name: "Table: GSM1K Correlation (Step 3) — Reviewer Critique Points"
        columns: [statistic, value, "95% CI", reviewer_concern]
        rows:
          - [Pearson r, -0.478, "[-0.714, -0.155]", "CI wide"]
          - [Spearman ρ, -0.403, "[-0.687, -0.031]", "upper bound near zero"]
          - [Partial r, -0.385, "[-0.640, -0.058]", "controlling accuracy helps marginally"]
          - [N, 33, "—", "underpowered"]
    figures_description:
      - "Fig: Scatter — GSM1K contamination gap (x) vs DIF-C item performance gap (y), N=33 models. Negative trend visible but scatter is large. Cook's D 标注 Deepseek-math-7b-rl as influential point。评审在 median 档会聚焦 scatter 的 noise level。"
    analysis: >
      Median 档下 plan_004 是 mixed outcome。Step 1+2 加强 Claim 1+3 的 cross-benchmark
      generalizability故事，Step 3 是 liability。正确策略是：
      主文用 Step 1+2 证明 "DIF and semi-synthetic framework generalize to GSM8K"，
      Step 3 降级至 appendix with explicit caveat "suggestive evidence requiring
      replication with larger matched sample (N≥100)"。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      在 MMLU 上拟合 bifactor IRT 模型 (general + 57 subject-specific factors)，
      选择 anchor items，执行 fixed-parameter calibration 的 equating pilot。
    expected_results:
      bifactor_convergence: true
      bifactor_iterations: 2847
      rmsea: 0.052
      cfi: 0.81
      tli: 0.78
      srmr: 0.068
      general_factor_variance_explained: 0.34
      subject_factors_variance_explained: 0.41
      residual_variance: 0.25
      n_anchor_items_selected: 1200
      anchor_selection_criterion: "no DIF + discrimination > 0.5 + fit residual < 2.0"
      equated_rho_vs_original: 0.94
      equated_rho_target: 0.95
      target_met: false
      computation_time_hours: 38
      memory_peak_gb: 127
    result_rationale: >
      Median 档：bifactor 收敛但 fit 指标 mediocre。
      1) RMSEA=0.052 在 acceptable range (< 0.06) 但不 good (< 0.05)。
      CFI=0.81 和 TLI=0.78 低于常规 threshold (0.90)——这是 12,508 items × 5,227
      models 的规模效应，absolute fit indices 在超大规模下系统偏低。
      评审如果懂 psychometrics 会接受，不懂会直接攻击 "poor model fit"。
      2) General factor 只解释 34% variance——MMLU 的 57 subject 确实 highly
      multidimensional，这 validates "1D IRT is misspecified" 的论点。
      3) Equating ρ=0.94 未达 0.95 target——marginal miss。Plan_014 within-subject
      pre-check (38.1% C%) 已经预示 DIF 在 bifactor 校正后不会大幅下降。
      4) 计算成本高 (38 hours, 127GB RAM)——scalability concern。
      Median 档评审反应：
      - 支持者："bifactor results validate the multidimensionality concern and motivate
        future work on MIRT-based DIF"
      - 反对者："CFI=0.81 means the model doesn't fit, equating results are unreliable"
      总体：pilot 结果 suggestive 但不 conclusive，适合 limitations/future work。
    tables:
      - name: "Table: Bifactor IRT Fit Indices"
        columns: [index, value, conventional_threshold, interpretation]
        rows:
          - [RMSEA, 0.052, "<0.06 acceptable", borderline acceptable]
          - [CFI, 0.81, ">0.90 good", below threshold]
          - [TLI, 0.78, ">0.90 good", below threshold]
          - [SRMR, 0.068, "<0.08 acceptable", acceptable]
          - [general factor % variance, 34%, ">50% for unidimensional", confirms multidimensionality]
    figures_description:
      - "Fig: Scree plot — first 10 eigenvalues. Sharp drop after factor 1 (eigenvalue=412) then gradual decline through factors 2-57. General factor dominant but not sufficient。"
      - "Fig: Scatter — equated ranks vs original ranks. ρ=0.94, visible scatter especially in middle ranks (100-400 range)。"
    analysis: >
      Median 档下 plan_005 验证了 IRT misspecification 但未解决它。
      34% general factor variance 是回应 "IRT misspecification" concern 的有力数据——
      证明 1D IRT 确实不足，但 DIF finding 的方向和规模不受根本影响
      (因为 bifactor 校正后 C% 从 31.3% 只降至 ~28-29%，仍然 substantial)。
      关键洞察：评审要求的不是 "fix the misspecification"，而是 "show DIF findings
      are robust TO the misspecification"。Plan_005 可以回答这个——如果 bifactor 校正后
      DIF 发现 qualitatively 不变，那就是 robustness evidence。
      策略：不把 equating 当 claim，而是作为 IRT sensitivity analysis 放 appendix。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      为 DIF-flagged items 生成替代题目，用 student simulation 校准难度。
    expected_results:
      n_items_generated: 150
      difficulty_correlation_prompt_based: 0.32
      difficulty_correlation_student_sim: 0.58
      difficulty_correlation_target: 0.75
      target_met: false
      cognitive_level_match_rate: 0.71
      subject_match_rate: 0.95
      human_quality_rating: 3.2
      human_quality_scale: "1-5"
      holdout_panel_rho: 0.52
      gpu_hours_used: 145
    result_rationale: >
      Median 档：item generation 是 paper 最弱的环节之一。
      1) Prompt-based difficulty targeting ρ=0.32 远低于文献报告的 0.45 upper bound——
      MMLU 的 multiple-choice 格式和 domain diversity 使 prompt 控制困难。
      2) Student simulation 提升到 ρ=0.58 (vs 文献 0.75-0.82 on simpler benchmarks)——
      MMLU 的 57 domains 使 simulation calibration 更难泛化。
      3) Cognitive level match rate 71%——约 29% 的 generated items 测量不同的
      cognitive level，这是 construct validity threat。
      4) Holdout panel ρ=0.52——远低于 equating 需要的精度。
      Median 档评审会直接判定 item generation 不成熟："generated items don't match
      target difficulty well enough for equating; this is a negative result"。
      策略：plan_006 在 median 档是 negative result，移至 appendix 作为
      "current limitations of LLM-based item generation for benchmark maintenance"。
      不影响核心 claims。
    tables:
      - name: "Table: Item Generation Difficulty Calibration"
        columns: [method, difficulty_ρ, n_items, notes]
        rows:
          - [prompt-based targeting, 0.32, 150, "below literature 0.10-0.45"]
          - [student simulation, 0.58, 150, "below target 0.75"]
          - [combined (iterative), 0.61, 80, "2-round refinement"]
    figures_description:
      - "Fig: Scatter — target difficulty vs empirical difficulty for 150 generated items. Student simulation (blue) vs prompt-only (red). Visible improvement but still wide scatter band。"
    analysis: >
      Median 档下 plan_006 是 expected negative。Item generation 是 hard open problem，
      failure 不损害核心 paper 因为 regeneration 已从 claims 中 drop。
      唯一价值：作为 future work 动机——"automated benchmark maintenance requires
      better item generation, which remains an open problem"。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      实现 Sinharay et al. (2006) 的 cumulative Bayesian DIF prior。
      模拟 4 次 successive benchmark administration，展示 evidence 累积带来的 power 提升。
    expected_results:
      simulation_n_administrations: 4
      admin_1_power_delta10: 0.41
      admin_2_power_delta10: 0.56
      admin_3_power_delta10: 0.68
      admin_4_power_delta10: 0.74
      target_admin3_power: 0.70
      target_met: false
      admin_3_power_delta14: 0.82
      fpr_cumulative: 0.048
      fpr_stable_across_admins: true
      bayes_factor_median_admin3: 4.2
      simulation_n_items: 500
      simulation_n_models_per_admin: 200
      computation_time_hours: 6
    result_rationale: >
      Median 档：simulation 结果方向正确但 target 未达。
      1) 3 次 administration 后 δ=1.0 的 power 从 0.41 升至 0.68——接近但未达 0.70 target。
      δ=1.4 时 0.82 是可用的，说明 cumulative approach 有价值但主要对 medium effects。
      2) FPR 控制良好 (0.048)，Bayesian prior 没有引入 FPR inflation。
      3) 核心限制：这是 pure simulation，没有 real data validation。
      METABENCH 只有一个 "administration"（没有 temporal sub-cohorts fine enough
      for 4 successive periods）。
      4) Median 档评审："simulation-only result without empirical validation;
      interesting but speculative"。
      策略：appendix material。展示 concept 可行性但承认需要真实数据验证。
      如果 ICLR 评审不熟悉 Bayesian DIF，这部分可能被完全忽略。
    tables:
      - name: "Table: Cumulative Power by Administration"
        columns: [n_admins, power_delta_10, power_delta_14, power_delta_16, fpr]
        rows:
          - [1, 0.41, 0.68, 0.72, 0.042]
          - [2, 0.56, 0.77, 0.83, 0.045]
          - [3, 0.68, 0.82, 0.89, 0.048]
          - [4, 0.74, 0.86, 0.92, 0.047]
    figures_description:
      - "Fig: Power curves across administrations for δ ∈ {0.6, 0.8, 1.0, 1.2, 1.4, 1.6}. 4 curves (one per admin count) showing cumulative improvement. Diminishing returns visible after admin 3。"
    analysis: >
      Median 档下 plan_007 有 modest value 作为 forward-looking contribution。
      核心问题：ML 评审对 "future benchmark administrations" 的 temporal framing
      不熟悉——psychometrics 中 repeated test administration 是常态，
      但 LLM benchmarks 通常是 one-shot。需要明确解释
      "as new model generations emerge, the same benchmark is effectively re-administered"。
      Appendix 放置，主文 limitations 中一句话提及 cumulative power improvement 可能性。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      分析 benchmark validity 在 progressive item replacement 下的退化模式。
    expected_results:
      replacement_5pct_rho: 0.998
      replacement_10pct_rho: 0.995
      replacement_20pct_rho: 0.987
      replacement_50pct_rho: 0.961
      reliability_5pct_alpha: 0.943
      reliability_10pct_alpha: 0.938
      reliability_20pct_alpha: 0.924
      reliability_50pct_alpha: 0.891
      original_alpha: 0.946
      construct_coverage_20pct_subjects_lost: 0
      construct_coverage_50pct_subjects_lost: 3
      validity_floor_replacement_pct: 0.35
      validity_floor_criterion: "ρ > 0.98 AND α > 0.92"
    result_rationale: >
      Median 档：graceful degradation 结果 clean 且 informative。
      1) ρ 从 0.998 (5%) 到 0.961 (50%) 的退化曲线非常 smooth——MMLU 的
      12,508 items 有 massive redundancy，即使替换 50% items 排名仍 strongly correlated。
      这 complements plan_017 (ρ=0.997 after removing 31% DIF items)。
      2) Reliability (Cronbach's α) 从 0.946 到 0.891——20% 是 practical threshold，
      之后 reliability 下降加速。
      3) Construct coverage：50% replacement 时 3 个 subjects 可能 under-represented
      (small subjects with few items)。
      4) 核心问题：replacement 假设 generated items 质量 OK——但 plan_006 显示
      generation 质量不足。所以 "graceful degradation" 只在理论层面成立。
      Median 档评审："nice analysis but moot without better item generation (plan_006 failed)"。
      策略：clean supplementary result，放 appendix。主文用
      "validity floor at ~35% replacement" 作为 practical recommendation。
    tables:
      - name: "Table: Validity Metrics Under Progressive Replacement"
        columns: [replacement_pct, rank_ρ, cronbach_α, subjects_under_represented]
        rows:
          - [0, 1.000, 0.946, 0]
          - [5, 0.998, 0.943, 0]
          - [10, 0.995, 0.938, 0]
          - [20, 0.987, 0.924, 0]
          - [35, 0.974, 0.908, 1]
          - [50, 0.961, 0.891, 3]
    figures_description:
      - "Fig: Dual-axis line chart — rank ρ (left, blue) and Cronbach's α (right, orange) vs replacement percentage. Both decline smoothly, α inflects around 25%。"
    analysis: >
      Median 档下 plan_008 的主要贡献是量化 "how much replacement is safe"——
      35% validity floor 直接对应 "31% DIF items can be safely replaced without
      validity loss"。这 strengthens the "instability ≠ invalidity" narrative。
      但 plan_006 的 negative result 使得 "replacement" 变成 theoretical exercise。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      Tutz & Berger (2016) Item-Focused Trees 作为 categorical DIF 的替代方案。
      Treat model release date as continuous covariate。
    expected_results:
      n_items_analyzed: 12508
      n_items_with_significant_split: 4127
      pct_items_with_split: 33.0
      primary_split_date: "2023-11-15"
      concordance_with_mh_ets_c: 0.78
      additional_items_detected: 209
      items_missed_by_ift: 612
      jaccard_mh_vs_ift: 0.68
      computational_time_hours: 12
      n_items_nonlinear_trend: 1834
      pct_nonlinear: 14.7
    result_rationale: >
      Median 档：IFT 是有价值的 robustness check 但不改变 narrative。
      1) 33% items with significant split vs MH 31.3%——high concordance (0.78)，
      说明 categorical temporal split 不是 arbitrary 的。
      2) Primary split date 2023-11-15——接近 GPT-4/Llama-2 到 Llama-3/Mixtral
      的代际转换点，有 face validity。
      3) IFT detects 209 additional items that MH misses (mostly items with gradual
      drift rather than sharp shift)，同时 misses 612 items MH catches (mostly items
      where DIF is large but not monotone in date)。
      4) 14.7% nonlinear trends——说明 some items 的 DIF 不是 monotone temporal，
      暗示 "contamination + capability gain + item drift" 的 multi-factor story。
      Median 档评审："useful supplementary analysis, confirms MH results are not
      artifacts of the cohort split"。不改变 claims 但提供 methodological robustness。
      策略：appendix 的 robustness check。主文一句话："IFT with continuous release
      date yields 78% concordance with MH categorical DIF (Appendix X)"。
    tables:
      - name: "Table: MH vs IFT Concordance"
        columns: [metric, mh_ets_c, ift_significant, overlap, jaccard]
        rows:
          - [n_flagged, 3918, 4127, 3306, 0.68]
          - [pct_flagged, 31.3, 33.0, 26.4, "—"]
    figures_description:
      - "Fig: Item DIF trajectory plots for 6 example items — IFT-detected smooth temporal trends vs MH binary classification. Shows items where IFT captures gradual drift that MH misses (top row) and items where MH captures sharp shift that IFT underweights (bottom row)。"
    analysis: >
      Median 档下 plan_009 的 concordance=0.78 有两面性：
      - 支持：MH 的 categorical split 不是 artifact，IFT confirms temporal instability
      - 质疑：22% discordance 说明 method choice matters，results are partially method-dependent
      评审在 median 档接受 IFT 作为 robustness check，不会深入追究 discordance。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      在 decoder-only 子群内重跑 DIF，检验 architecture heterogeneity 是否影响 IRT fit。
    expected_results:
      n_decoder_only: 5226
      n_non_decoder: 1
      pct_decoder_only: 99.98
      decoder_only_c_pct: 31.3
      full_population_c_pct: 31.3
      jaccard_decoder_vs_full: 1.0
      irt_rmsea_full: 0.089
      irt_rmsea_decoder_only: 0.088
      irt_cfi_full: 0.72
      irt_cfi_decoder_only: 0.72
      irt_fit_improvement: negligible
      pct_models_lz_gt2: 98.0
    result_rationale: >
      Median 档：plan_010 是 clean knockout result。
      1) METABENCH MMLU 是 99.98% decoder-only (5226/5227)——removing 1 non-decoder
      model changes literally nothing (Jaccard=1.0)。
      2) IRT fit 不改善 (RMSEA 0.089→0.088, CFI 0.72→0.72)——因为 misfit 来自
      MMLU 的 57-subject multidimensionality，不是 architecture heterogeneity。
      3) 98% models 有 |Lz|>2——这反映 1D IRT 对 MMLU 的 fundamental misspecification，
      不是 population heterogeneity。
      Median 档评审接受这个 null result：architecture 不是问题。但会转向
      "OK so the misfit is from multidimensionality, have you tried multidimensional IRT?"——
      这是 median 档的核心 concern 之一。
      策略：主文用一段报告 99.98% decoder-only + Jaccard=1.0。
      IRT fit 数据放 limitations 讨论，作为 multidimensional IRT future work 的动机。
    tables:
      - name: "Table: Architecture Stratification Results"
        columns: [population, n_models, c_pct, rmsea, cfi, pct_lz_gt2]
        rows:
          - [full, 5227, 31.3, 0.089, 0.72, 98.0]
          - [decoder-only, 5226, 31.3, 0.088, 0.72, 98.0]
          - [delta, "—", 0.0, 0.001, 0.00, 0.0]
    figures_description:
      - "Fig: (Not needed — result is trivially null due to 99.98% decoder-only composition. A one-line footnote suffices.)"
    analysis: >
      Median 档下 plan_010 的 value 是 defensive：排除一个 potential confound。
      但它也暴露了真正的问题——IRT misfit 来自 multidimensionality，
      这正是评审的 attack vector。Plan_005 bifactor pilot 是 partial response，
      但 median 档下不够 convincing (CFI=0.81)。
      最佳回应策略：承认 misspecification，展示 DIF 发现在 bifactor 校正后
      qualitatively 不变 (C% ~28-29% vs 31.3%)，argue "our findings are conservative
      estimates"。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: >
      向真实 METABENCH response matrix 注入已知 contamination，测量 DIF 检测力。
    expected_results:
      n_clean_items: 500
      n_injected_items: 200
      temporal_external_tpr_p0: 0.326
      temporal_external_tpr_p03: 0.548
      temporal_external_tpr_p05: 0.834
      temporal_external_tpr_p07: 0.990
      temporal_external_tpr_p10: 1.000
      temporal_external_fpr: 0.314
      temporal_external_delta_tpr_p05: 0.508
      temporal_external_delta_tpr_p10: 0.674
      ability_external_delta_tpr_p10: 0.302
      cross_subject_delta_fpr: 0.000
      within_subject_fpr_inflation_p10: 0.186
      dose_response_monotone: true
      dose_response_p_values: [0.3, 0.5, 0.7, 1.0]
    result_rationale: >
      Median 档：plan_011 是 paper 的 strongest evidence 之一。
      1) ΔTPR=+0.508 at p=0.5 是 clean, large effect——从 baseline 0.326 升至 0.834，
      明确证明 DIF 能 detect injected differential contamination。
      2) Dose-response 从 p=0.3 到 p=1.0 monotone——mechanistic validation。
      3) Cross-subject matching ΔFPR=0.000 是 key innovation——完全消除 FPR inflation，
      vs within-subject matching +0.186。这是 Claim 3 的核心证据。
      4) Baseline FPR=0.314 (= temporal C%=31.3%)——评审会问 "is 31% baseline FPR
      acceptable?" Answer: this IS the real DIF rate, not false positives. Semi-synthetic
      只 adds signal on top of real baseline。
      Median 档评审对 plan_011 的质疑集中在：
      - "injection mechanism (incorrect→correct) is simplistic—real contamination
        may produce different patterns (e.g., faster response time, different error types)"
      - "you inject into real matrices, but the contamination is still artificial"
      这些是 acknowledged limitations，不是 fatal flaws。
      策略：plan_011 在主文 §4 占重要位置。Cross-subject matching 作为
      methodological recommendation 明确 highlight。
    tables:
      - name: "Table: Semi-synthetic Detection Power (Cross-subject Matching)"
        columns: [exploitation_rate_p, baseline_tpr, injected_tpr, delta_tpr, fpr, delta_fpr]
        rows:
          - [0.0 (no injection), 0.326, 0.326, 0.000, 0.314, 0.000]
          - [0.3, 0.326, 0.548, 0.222, 0.314, 0.000]
          - [0.5, 0.326, 0.834, 0.508, 0.314, 0.000]
          - [0.7, 0.326, 0.990, 0.664, 0.314, 0.000]
          - [1.0, 0.326, 1.000, 0.674, 0.314, 0.000]
      - name: "Table: Within-subject vs Cross-subject Matching"
        columns: [matching, delta_tpr_p05, delta_fpr_p10, fpr_stable]
        rows:
          - [within-subject, 0.457, +0.186, false]
          - [cross-subject, 0.508, 0.000, true]
    figures_description:
      - "Fig: Dose-response curve — ΔTPR vs exploitation rate p. Cross-subject matching (blue, solid) vs within-subject (red, dashed). Cross-subject 在 ΔTPR 上 comparable or superior，同时 ΔFPR=0。Clean separation。这是 paper 最有说服力的 figure 之一。"
      - "Fig: FPR control comparison — barplot showing FPR at p=0, 0.5, 1.0 for within-subject vs cross-subject matching. Within-subject FPR inflates from 0.31 to 0.50; cross-subject stays flat at 0.31。"
    analysis: >
      Median 档下 plan_011 (+plan_016 cross-subject replication) 是 Claim 3 的
      robust foundation。Reviewers 在 median 档给 semi-synthetic framework
      positive marks (novelty sub-score 2.5 on this specific contribution)。
      唯一 downside：injection simplicity。Rebuttal 准备：
      "Our injection flips incorrect→correct, which is the minimal model of
      contamination (memorized answer). More complex patterns (partial memorization,
      verbatim recall) would produce LARGER DIF effects, not smaller—our power
      estimates are conservative."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7778196-2239-40e6-a48d-1f44c0fdbe6c",
  "isSidechain": false,
  "requestId": "req_011CbFEypRAJGXZzxoowz8Cz",
  "type": "assistant",
  "uuid": "607e70f3-a7aa-40b2-8fda-038ae2f9b4af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017f7qFMfS94Zk2WpDi8Sf9G",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19004,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16275,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19004
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claim 1+3 稳固；Claim 2 meta-critique 被部分评审视为 obvious；Claim 4 的 GSM1K 部分 (N=33) 被 dismiss；novelty 受质疑但不致命 核心假设：[\"A1 部分成立：1-2 个评审质疑 novelty（'just applying MH…",
  "leafUuid": "607e70f3-a7aa-40b2-8fda-038ae2f9b4af",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF analysis reveals MMLU temporal instability and validates semi-synthetic framework",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claim 1+3 稳固；Claim 2 meta-critique 被部分评审视为 obvious；Claim 4 的 GSM1K 部分 (N=33) 被 dismiss；novelty 受质疑但不致命 核心假设：[\"A1 部分成立：1-2 个评审质疑 novelty（'just applying MH…",
  "leafUuid": "607e70f3-a7aa-40b2-8fda-038ae2f9b4af",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF analysis reveals MMLU temporal instability and validates semi-synthetic framework",
  "sessionId": "bbb05643-251b-40fa-a591-630f63d2ac60"
}
```

---
