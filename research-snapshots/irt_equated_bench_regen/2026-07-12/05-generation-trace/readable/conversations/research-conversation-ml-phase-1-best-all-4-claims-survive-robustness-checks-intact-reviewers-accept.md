# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：All 4 claims survive robustness checks intact; reviewers accept discovery-pa

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/a0546b48-bdea-4921-889b-877f45f5f952.jsonl`
- **Structured JSON:** [`cf80c45d050ab87170e9.json`](../../sessions/cf/cf80c45d050ab87170e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:28:27.937Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:28:27.937Z",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：All 4 claims survive robustness checks intact; reviewers accept discovery-paper framing at ICLR\n核心假设：['SIBTEST/logistic regression confirms <5% items with substantial non-uniform DIF beyond MH flags — MH adequacy validated', 'Instability ≠ invalidity framing lands in Introduction; reviewers treat ρ≈0.997 + circularity ablation as sufficient', 'Ground truth meta-critique accepted as genuinely non-obvious contribution (≥2 reviewers cite it as strength)', 'GSM1K r=−0.478 (N=33) treated as suggestive-but-consistent rather than attacked as underpowered', 'IRT misfit (98% |Lz|>2) accepted as known MMLU multidimensionality, not fatal flaw, given architecture homogeneity (99.98% decoder-only)', 'DIF primer in §3 successfully bridges psychometrics → ML vocabulary gap']\n关键指标范围：{'nonuniform_dif_additional_pct': [0, 5], 'mh_sibtest_flag_jaccard': [0.8, 0.95], 'gsm1k_partial_r_lower_ci': [-0.7, -0.2], 'iclr_avg_overall_score': [6.0, 7.5], 'iclr_avg_novelty_score': [6.0, 7.0], 'iclr_avg_soundness_score': [6.5, 8.0], 'accept_probability': [0.45, 0.65]}\n叙事方向：Original framing holds without adjustment. Four claims presented as stated in paper_framing.md. Headline: \"31% temporal instability is robust, not driven by capability gains (≤7.6%), and the field's web-overlap ground truth is fundamentally mismatched for item-level detection.\" Circularity ablation + GSM1K anti-correlation form a coherent two-pronged downstream story. Non-uniform DIF robustness check strengthens §5 by showing MH is sufficient for this population. No claims need softening; appendix material stays in appendix.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nfocus: This is a post-revision re-dream. Key changes since Dream #3: (1) paper_framing.md rewritten with no-pivot narrative, scope pruning (Bayesian DIF/RL/ensemble/pilots → appendix), explicit 3-layer novelty articulation, \"instability ≠ invalidity\" framing upfront; (2) 6 new robustness analyses with real data: threshold sensitivity (49/31/18/10%), BH FDR (negligible), instability decomposition (≤2.4pp/7.6%), circularity ablation (DIF least disruptive non-random), architecture stratification (99.98% decoder-only, concern dissolved), bootstrap CIs (all exclude zero); (3) literature expanded 15→45 papers across 5 clusters; (4) experiments.tex completed with Reviewer patches. Focus review on whether the structural/writing improvements address the prior round's concerns.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.\n\n10. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T04:28:27.940Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:28:27.940Z",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T04:28:27.960Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：All 4 claims survive robustness checks intact; reviewers accept discovery-paper framing at ICLR
核心假设：['SIBTEST/logistic regression confirms <5% items with substantial non-uniform DIF beyond MH flags — MH adequacy validated', 'Instability ≠ invalidity framing lands in Introduction; reviewers treat ρ≈0.997 + circularity ablation as sufficient', 'Ground truth meta-critique accepted as genuinely non-obvious contribution (≥2 reviewers cite it as strength)', 'GSM1K r=−0.478 (N=33) treated as suggestive-but-consistent rather than attacked as underpowered', 'IRT misfit (98% |Lz|>2) accepted as known MMLU multidimensionality, not fatal flaw, given architecture homogeneity (99.98% decoder-only)', 'DIF primer in §3 successfully bridges psychometrics → ML vocabulary gap']
关键指标范围：{'nonuniform_dif_additional_pct': [0, 5], 'mh_sibtest_flag_jaccard': [0.8, 0.95], 'gsm1k_partial_r_lower_ci': [-0.7, -0.2], 'iclr_avg_overall_score': [6.0, 7.5], 'iclr_avg_novelty_score': [6.0, 7.0], 'iclr_avg_soundness_score': [6.5, 8.0], 'accept_probability': [0.45, 0.65]}
叙事方向：Original framing holds without adjustment. Four claims presented as stated in paper_framing.md. Headline: "31% temporal instability is robust, not driven by capability gains (≤7.6%), and the field's web-overlap ground truth is fundamentally mismatched for item-level detection." Circularity ablation + GSM1K anti-correlation form a coherent two-pronged downstream story. Non-uniform DIF robustness check strengthens §5 by showing MH is sufficient for this population. No claims need softening; appendix material stays in appendix.


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen
focus: This is a post-revision re-dream. Key changes since Dream #3: (1) paper_framing.md rewritten with no-pivot narrative, scope pruning (Bayesian DIF/RL/ensemble/pilots → appendix), explicit 3-layer novelty articulation, "instability ≠ invalidity" framing upfront; (2) 6 new robustness analyses with real data: threshold sensitivity (49/31/18/10%), BH FDR (negligible), instability decomposition (≤2.4pp/7.6%), circularity ablation (DIF least disruptive non-random), architecture stratification (99.98% decoder-only, concern dissolved), bootstrap CIs (all exclude zero); (3) literature expanded 15→45 papers across 5 clusters; (4) experiments.tex completed with Reviewer patches. Focus review on whether the structural/writing improvements address the prior round's concerns.

## paper_framing.md

# Paper Framing — irt_equated_bench_regen

## Target Venue
- Primary: ICLR 2027 (expected deadline ~October 2026)

## Paper Type
Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."

## Core Claims (4 条, 可证伪)

**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement)
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
3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.
4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.
- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)
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

9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.

10. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.

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
  "promptId": "50e2ebd6-e0fe-4b65-8639-72ee137ebad5",
  "type": "user",
  "uuid": "e570b320-2a73-4647-9c2b-dd56c8d13639",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:28:27.959Z_

```json
{
  "parentUuid": "e570b320-2a73-4647-9c2b-dd56c8d13639",
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
  "uuid": "d738c137-a8d9-419f-b4da-4b37f39e665c",
  "timestamp": "2026-05-21T04:28:27.959Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:28:27.959Z_

```json
{
  "parentUuid": "d738c137-a8d9-419f-b4da-4b37f39e665c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ba84d6c5-49f2-40cc-a4da-70ff208bc019",
  "timestamp": "2026-05-21T04:28:27.959Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All 4 claims survive robustness checks intact; reviewers accept discovery-paper framing at ICLR 核心假设：['SIBTEST/logistic regression confirms <5% items with…",
  "leafUuid": "ba84d6c5-49f2-40cc-a4da-70ff208bc019",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric DIF analysis of LLM benchmarks",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952"
}
```

---

### Assistant

_source line 8 · 2026-05-21T04:33:44.756Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for all "planned" experiments in the experiment_plan, under the "best" tier definition. Let me identify which experiments are still "planned" (not yet completed):

Looking at the experiment_plan and registry:

1. plan_001 - status: planned in experiment_plan, but DONE in registry (plan_001_real_data_dif_mmlu)
2. plan_002 - status: planned, not in registry as DONE


3. plan_003a through plan_003c - all planned but not yet completed
4. plan_004 - planned in experiment_plan, but already DONE in registry
5. plan_005 - planned and not in registry as DONE (plan_015 is killed but that's a different bifactor IRT approach)
6. plan_006 through plan_008 - all planned and not yet completed
9. plan_009 - planned and not in registry as DONE
10. plan_010 is interesting - it's not in the registry, but paper_framing.md references its results with specific metrics (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), which suggests it's actually been completed even though there's no registry entry for it
11. plan_011 through plan_013 - all DONE
12. plan_014 - checking status...

Looking at the full registry picture, I see several experiments referenced in paper_framing that don't have corresponding DONE entries: plan_010 (arch-stratified results), plan_018 (threshold sensitivity), plan_019 (decomposition), and plan_020 (circularity ablation). Meanwhile, the planned experiments still pending are plan_002 through plan_007, with plan_007 appearing to be cut off in the list. I'm noticing that plan_010 appears in the experiment_plan with "planned" status, but its results are already referenced in paper_framing, suggesting it may have been completed without updating the registry. Re-reading the user's request, they want detailed data generated for each planned experiment in experiment_plan, so I need to cover all experiments marked as planned regardless of whether results are already mentioned elsewhere in the document.

Looking at the registry to distinguish truly planned experiments from those already completed, I can see that plan_001, plan_004, and plan_010 are marked DONE, while the rest remain genuinely planned. So I should generate imagined results for plan_002 through plan_007 and any others not yet in the completed registry.

But I'm noticing the paper_framing.md references specific results for plan_010, plan_018, plan_019, and plan_020 — these were clearly finished, though plan_018 through plan_020 don't appear in the original experiment_plan document itself. Since plan_010 already has concrete results documented, I should probably skip generating new ones for it, but I'll need to create results for the genuinely outstanding experiments.

Looking at what's actually missing from the registry, I need to focus on plan_002, plan_003a through plan_003c, plan_005 through plan_009, and plan_010. That's my target list for detailed data generation.

For the "best" tier scenario where all four claims survive robustness checks and reviewers accept the discovery-paper framing at ICLR, I'll need to generate plausible results for each experiment that align with this optimistic outcome, along with explanations for why those results would emerge.

But I'm also tracking that most of these experiments have been relegated to appendices due to scope constraints — some underpowered, some never executed, some moved to supplementary material — so I need to account for that positioning when generating the results and rationales.

Now working through plan_002 specifically: the RL robustness validation experiment. In the "best" tier, DIF flags should remain stable across different model cohorts (SFT-only versus SFT with alignment-RL versus SFT with both alignment and reasoning-RL), demonstrating that the detector isn't fooled by architectural changes. Traditional detectors, by contrast, should degrade when applied to reasoning-RL models. The Jaccard similarity for DIF flags should stay high across cohorts (above 0.85), while traditional detector AUROC drops noticeably on reasoning-RL models. The TOST equivalence test would be inconclusive given the N=13 limitation, but the directional evidence supports robustness.

For plan_003a, ConStat serves as a baseline showing it can catch non-RL contamination at moderate rates but fails on RL models, establishing that DIF offers complementary detection capability. Plan_003b shows DVD catching variant contamination but missing verbatim cases, again positioning DIF as filling a gap. Plan_003c on ensemble fusion would be framed as future work since the underlying experiments never ran.

For plan_005, I'm reconsidering the bifactor approach—even though the paper notes it was dropped after plan_014's pre-check revealed within-subject DIF at 38.1%, I should still imagine what the "best" scenario would show: bifactor improves model fit and anchor selection works, but it still can't achieve the equating target of ρ≥0.95 because the fundamental DIF problem persists at the general factor level.

For plan_006, LLM-generated items show moderate difficulty alignment and student simulation improves calibration, though this remains supplementary.

Plan_007's simulation demonstrates the expected power gains cleanly.

For plan_008, I'm working through what progressive item replacement would reveal under optimal conditions—

showing validity holds up to about 30% replacement, which ties back to that high redundancy finding.

Plan_009 confirms the temporal DIF pattern using item-focused trees with continuous release dates, consistent with the categorical approach.

Plan_010 shows architecture has virtually no effect since the model is almost entirely decoder-only, so DIF flags remain unchanged.

Now I need to construct the YAML output with proper metrics and justifications for each plan. I'm considering whether to include plan_001 since it's marked as done in the registry but still listed as planned—I think I should cover all of them to be comprehensive.

Looking at which experiments are actually complete versus still planned: plan_001 through plan_017 are all marked as planned, but the registry shows plan_001, plan_001b, plan_004, and several others are already done. The truly unexecuted ones are plan_002, plan_003a, plan_003b, plan_003c, plan_005, plan_006, plan_007, plan_008, plan_009, and plan_010.

There are also three experiments in the registry that weren't in the original plan: plan_018, plan_019, and plan_020.

For plan_010, I can use the existing results from paper_framing since they align with the best tier classification. Now I'm working through each experiment to draft detailed YAML with metrics and reasoning, starting with plan_002 on RL robustness validation where the statistical test wouldn't be significantly affected by adding a small number of reasoning models to a large cohort.

The key insight is that DIF's matching on total score quintiles distributes the RL models across strata without creating systematic bias, whereas per-model detectors like Min-K% and ConStat are vulnerable because they rely on output distributions that RL training directly modifies. I'm laying out the expected metrics: DIF flag agreement stays high around 0.87-0.91, but Min-K% and ConStat drop to near-chance performance on reasoning models, while the overall detection retention holds steady at 0.93 and the equivalence test remains inconclusive.

Now I'm moving to the perturbation-based evaluation where ConStat tests whether models can handle paraphrased items. The logic is that non-RL models relying on memorized phrasings will show sharp performance drops on reformulations, while RL-aligned models with more robust representations stay stable. I'm expecting around 237 paraphrased items with 0.91 semantic similarity, and detection rates diverging between contaminated and RL-trained cohorts.

For the DVD approach, I'm evaluating whether generation variance patterns reveal verbatim memorization—contaminated models produce near-identical outputs while clean ones show natural variation. This works well for exact memorization but struggles with paraphrased contamination, so I'm expecting detection rates around 0.55 for verbatim cases but only 0.12 for variants.

Now looking at how to combine these three methods: DIF catches large performance gaps, ConStat picks up surface-level memorization in non-RL models, and DVD identifies exact matches through generation variance. A 2-of-3 voting ensemble should reach about 71% detection while keeping false positives low at 3%, and weighted fusion pushes that further to 76% detection with slightly higher false positives around 6%.

For the bifactor IRT approach, I'm testing whether modeling the 57 MMLU subjects as separate factors alongside a general ability factor helps explain the instability better than treating everything as one dimension. The general factor ends up capturing most of the variance, which makes sense, but the subject-specific factors don't actually resolve the DIF problem—it's genuinely item-level instability rather than a measurement artifact. Using the general factor scores for equating should still stabilize things effectively even with a third of items being unstable.

Now I'm looking at the actual fit metrics and DIF reduction from the bifactor model. The model fits substantially better than unidimensional IRT, and while bifactor conditioning does reduce within-subject DIF slightly, the improvement is modest—only about 3 percentage points. The general factor equating hits the target correlation, but subject-specific equating falls short for some subjects. I'm also noticing there's some confusion in my notes about whether this plan was actually completed or still in preparation status.

The key insight here is that even with the bifactor model's superior fit, DIF persists meaningfully, which actually strengthens the paper's argument that the instability isn't driven by multidimensionality—it's a genuine phenomenon. The equating approach shows promise on the general factor but needs refinement for subject-specific scales.

For plan_006, I'm shifting to item generation and calibration. The strategy is to use LLM-generated items as replacements for the DIF-flagged ones, with student simulation helping refine difficulty estimates beyond simple prompt-based targeting. I'm generating around 500 candidate items to cover the problematic ones, and I'm expecting the simulation-based approach to substantially outperform the prompt-based difficulty predictions.

Now I'm looking at the validation metrics for those generated items—construct alignment is strong at 87%, discrimination correlates reasonably with targets at 0.54, and the holdout validation shows 82% of items meet quality thresholds.

For plan_007, I'm testing whether cumulative administration actually improves DIF detection power as theory predicts. The simulation shows individual power at 0.42, then climbing to 0.58 after two administrations, 0.71 after three, and 0.79 after four, while keeping false positive rates controlled. The Bayes factor at the third administration reaches about 8.4, providing strong evidence.

Plan_008 examines what happens when I progressively replace DIF items with the newly generated ones—whether the model degrades gracefully or hits a cliff.  Ranking stability stays remarkably high even at 31% replacement (ρ≈0.997), with score reliability only dropping from 0.993 to 0.987, and I don't cross the validity threshold until around 65% replacement.

For plan_009, I'm checking whether using continuous release dates instead of categorical cohorts produces a smooth temporal trend in DIF, which would confirm the categorical split isn't introducing artifacts.

Now looking at plan_010, the architecture stratification analysis shows that decoder-only models dominate the dataset at 99.98%, making this stratification essentially moot for the analysis.

For the narrative at the "best" tier, all four main claims hold up—the 31% temporal instability remains robust and isn't explained by capability gains alone, and the field's web-overlap ground truth fundamentally misaligns with item-level detection needs. I'm thinking through what tables and figures each experiment would generate, and I should also consider the non-uniform DIF robustness check before assembling the full YAML output.

The SIBTEST and logistic regression DIF check that came up in reviewer concerns isn't a separate experiment in the plan, but it's a key assumption for the best tier—confirming that fewer than 5% of items show substantial non-uniform DIF beyond what Mantel-Haenszel flags catch. I'll note this in the narrative guidance rather than treating it as a standalone plan. I'm also realizing I need to clarify whether to include plan_001 and plan_004, which are marked as DONE in the registry even though they appear in the experiment_plan with "planned" status.

Since the user asked for detailed data on every planned experiment in the plan, and those two are technically listed there, I could include them with their actual results. But it makes more sense to focus on the experiments that are genuinely still planned—the ones without results yet—and acknowledge that the completed ones already have data in the registry. Let me go with that approach and skip the DONE experiments to avoid redundancy. Looking at the experiment_plan entries, I can see there are 13 total experiments listed. From the registry, plan_001, plan_004, plan_010, and plan_011 are already completed, so I'll pull their actual results. For the remaining nine experiments that are still planned, I'll generate realistic predictions based on the experimental design.

Actually, I'm realizing the user wants me to treat this as a dreaming exercise where I predict the "best case" outcomes for all planned experiments. The completed ones provide a baseline for what success looks like, so I should use those actual results to inform my predictions for the others. Let me just generate the full output with actual data for the done experiments and predictions for the rest.

Generating YAML output... I'm finishing up the experiment list—Bayesian cumulative analysis shows power improvements, graceful degradation validates the curve smoothly, and the semi-synthetic results confirm strong temporal trends with substantial TPR gains and zero cross-subject FPR inflation. Now I need to write the YAML with compelling result rationales for the best tier, keeping in mind that the non-uniform DIF assumption about SIBTEST/logistic regression flagging <5% items isn't a separate experiment but a key validation I should incorporate. I'm noticing the non-uniform DIF check is actually referenced in the key assumptions for the "best" tier with specific metrics around SIBTEST and logistic regression, so it needs to be included somewhere. Since it's not explicitly in the experiment_plan itself, I should weave it into the narrative_guidance rather than create a separate experiment entry. Now I'm ready to write out the YAML with the four claims as presented, keeping the framing comprehensive but concise. I'm working through the structure for each experiment now—for the completed ones (plan_001, plan_004, plan_011) I'll use their actual results but frame them within the expected_results format to keep things concise, then focus more detail on the truly planned experiments. I need to make sure the metrics I specify align with the tier definition ranges, and for each one I'll explain the result_rationale to show how it supports the best tier classification. The actual GSM1K partial r value of -0.385 with a lower CI of -0.640 falls within the expected range of [-0.7, -0.2], so this checks out for the best tier. Now I'm ready to generate the full YAML output.

For the planned experiments, I need to make realistic predictions about the metrics. Looking at plan_002, I'm considering how to structure the cohort compositions—starting with SFT-only models (probably around 2,000-3,000 of the ~5,227 total METABENCH models), then progressively adding alignment-RL and reasoning-RL models to see how the DIF results change across different focal group configurations.

For the expected outcomes under best-case conditions, I'm predicting that the Jaccard similarities between cohort pairs will be fairly high (0.87-0.93), suggesting DIF flags remain relatively stable as we expand the reference group, since the matching-variable conditioning in Mantel-Haenszel should buffer against distribution shifts. However, when I run Min-K% and ConStat directly on the reasoning-RL models themselves, I expect both metrics to perform near chance or only slightly better—around 0.56-0.61 AUROC—because RL training appears to compress the NLL gap that these metrics rely on.

When I test DIF on the full expanded cohort, I'm anticipating an AUROC around 0.83, which would be a modest drop from the baseline of 0.85, and a DeLong test comparing DIF to Min-K% should yield a p-value around 0.03, suggesting a meaningful difference. The TOST equivalence test for DIF retention will likely be inconclusive at p≈0.11 given the small sample of reasoning-RL models, and a power analysis indicates I'd need around 80 samples to reliably detect a difference of 1.4 or larger. The core insight is that DIF's group-level design—conditioning on total score rather than individual model outputs—makes it inherently robust to RL additions because the matching variable absorbs the ability differences, so even though RL models shift the overall distribution slightly, the relative item difficulties between groups stay consistent.

By contrast, Min-K% is vulnerable because it depends on per-model likelihood distributions that RL explicitly reshapes, and ConStat fails because RL smooths out the perturbation sensitivity it relies on.

Now looking at the paraphrase experiment results: I've generated 237 paraphrased MMLU items across 10 subjects with high semantic fidelity (0.92 mean similarity), and 94% of human raters confirmed they're semantically equivalent. When I run ConStat on these paraphrased items, the true positive rate for detecting contamination in non-RL models is around 0.44, but drops to 0.17 for RL models, with a false positive rate of 0.038. The effect sizes tell the story—contaminated non-RL models show a Cohen's d of 0.87, while contaminated RL models only show 0.29, confirming that RL's smoothing effect substantially weakens the signal ConStat is designed to detect.

The performance drops on paraphrases reveal the mechanism: non-RL models contaminated with exact training data lose 13.1% accuracy on paraphrases versus 2.8% for clean models, but contaminated RL models only drop 4.2%. This happens because non-RL memorization is surface-level—tied to exact token sequences—so paraphrases break the memorized patterns. RL-trained models, having optimized for generalization beyond exact training sequences, maintain performance even when contaminated, effectively laundering the contamination signal through the reward optimization process. This complementarity with DIF methods that detect differential functioning regardless of mechanism is why ensemble approaches make sense.

Now I'm looking at the detection metrics across 12 open-weight models tested on 200 MMLU items with 50 generations each. The bimodality coefficient shows a stark difference: contaminated items cluster at 0.71 (bimodal—either consistently correct or mixed responses), while clean items sit at 0.28 (unimodal—consistent uncertainty). Verbatim contamination produces near-deterministic responses with minimal generation variance (mean 0.09), creating that bimodal distribution where the model either nails it or flounders. Variant contamination and clean items show much higher variance (mean 0.31), and the detection rates reflect this—verbatim contamination hits 52% detection while variants only reach 14%, with a 6% false positive rate on clean data.

The key insight is that DVD captures a specific detection niche: verbatim exact-match memorization where the model learned lookup-table responses rather than concepts. This complements DIF, which catches group-level differential functioning, and ConStat, which detects perturbation sensitivity. Under the best fusion strategy, combining all three signals where available yields a 73% true positive rate with just 3% false positives and 92% precision using majority voting, improving to 78% TPR with weighted fusion at the cost of slightly higher false positives.

The optimal weighting scheme assigns 43% to DIF, 32% to ConStat, and 25% to DVD, with cross-validated weights showing strong stability. Coverage analysis reveals these detectors operate on largely orthogonal signals—23% of contaminated items are caught by DIF alone, 14% by ConStat alone, and 8% by DVD alone—because they target fundamentally different contamination mechanisms: DIF requires large sample sizes and is mechanism-agnostic, ConStat is model-specific and sensitive to perturbations, while DVD requires access to model weights and measures generation variance. Their weak error correlation means majority voting effectively suppresses false positives while maintaining high sensitivity.

Now examining the bifactor model structure: it decomposes the data into one general factor accounting for 58% of variance plus 57 subject-specific factors that capture an average of 31% within-subject variance. The model converged cleanly on the large 5,227 × 12,508 matrix after roughly 2,000 EM iterations, and the fit metrics substantially outperform a unidimensional baseline—RMSEA drops from 0.035 to 0.019, CFI improves from 0.88 to 0.95, and TLI from 0.86 to 0.94.

I identified 5,640 anchor items with strong general factor loadings and no differential item functioning, then checked whether extracting subject-specific variance reduces DIF. The equating correlation for general factor scores stays very high at 0.961, but within-subject DIF only drops by about 2.3 percentage points—from 38.1% to 35.8%—suggesting that multidimensionality explains only a small piece of the instability. Subject-level equating correlations range from 0.89 to 0.97, with some falling below the 0.95 threshold, indicating uneven performance across domains. The key insight is that the bifactor model correctly captures MMLU's genuine multidimensional structure, yet the persistent DIF reflects item-level instability in how individual items function across model generations rather than dimensional confounding.

The bifactor conditioning confirms that unidimensional IRT's misfit contributes only a small amount of spurious DIF—the vast majority of the 31% instability is real and robust. The equating pilot achieves a promising 0.961 correlation, showing that anchor-item-based score equating is feasible in principle and could guide future benchmark maintenance, though it's not yet mature enough for the main analysis.

For the replacement item generation plan, I generated 500 candidates for 250 DIF-flagged items using prompt-based difficulty targeting, which achieved a 0.36 correlation with actual difficulty—consistent with the literature range of 0.10–0.45. Student simulation difficulty estimation performed better at 0.73, aligning with typical literature values around 0.75.

The generated items showed strong construct alignment at 89% expert agreement and discrimination correlations of 0.51, with 84% of holdout validation items landing within ±0.15 of target difficulty. Selecting the best candidate from each pair improved the correlation to 0.79, and 76% of distractors were rated as plausible by experts. The key insight is that LLM-based generation produces on-topic items with high construct alignment but struggles with fine-grained difficulty calibration through prompting alone—the model lacks intuition about what makes items hard for other LLMs. Using diverse models as simulated test-takers provides empirical difficulty estimates that capture actual model behavior far more accurately than the generator's intuition, explaining the substantial gap between the 0.36 prompt-based approach and the 0.73 simulation-based approach.

For the best-tier experimental plan with four simulated administrations of 80 participants each at medium effect size, individual administrations achieved around 40-43% power, but cumulative Bayesian evidence accumulated rapidly across administrations, reaching 81% power and a Bayes factor of 16.7 by the fourth administration.

The false positive rate stayed well-controlled below 4.8%, and setting the evidence threshold at BF₁₀>3 yielded 65% power after just two administrations. This Bayesian sequential approach substantially outperforms the Mantel-Haenszel test at the same effect size, which only achieves 38% power individually—the cumulative updating mechanism allows weak individual signals to build into strong collective evidence across administrations, bridging the power gap that emerged in earlier simulations.

Now I'm examining how item replacement affects benchmark stability. When progressively replacing DIF-flagged items with matched-difficulty anchors at rates from 5% up to 50%, the ranking correlations remain remarkably high across all replacement levels, and even at the 31% replacement rate matching the true DIF prevalence, Cronbach's alpha holds steady near the full benchmark's reliability. The ranking stability at 31% replacement closely mirrors what we saw with DIF removal in plan_017, which makes sense since both operations eliminate roughly the same number of items—the small difference in correlation (0.9951 vs 0.997) comes down to calibration noise in replacement versus the cleaner removal approach. This validates the core insight that aggressive item updates don't destabilize model rankings, which is crucial for maintaining benchmarks without invalidating prior comparisons. Now I'm looking at plan_009's temporal structure across the best tier, where we have about 3,400 models with parseable release dates that naturally cluster into 3-5 temporal breakpoints around March 2023, August 2023, and January 2024.

The Item-Focused Tree analysis reveals that 33.8% of items show significant DIF when corrected for multiple comparisons, with strong overlap (0.76 Jaccard) between the tree-based and Mantel-Haenszel approaches, though each method catches some unique patterns—the tree captures gradual drift (~8% of items) while MH picks up sharp transitions (~5%). Release date is the dominant predictor of DIF magnitude (0.71 importance), with DIF growing steadily from early 2023 (0.82) through early 2024 (1.48), and there's a moderate correlation (r=0.39) between release timing and effect size, suggesting newer models genuinely perform differently on older benchmark items. % Jaccard overlap with MH categorical DIF confirms that the binary temporal split (2023 vs 2024-H1) captures most of the signal, but the continuous approach reveals additional nuance: (1) gradual drift items (~8%) that don't show dramatic shifts at any single cutpoint but accumulate small DIF across the timeline, and (2) natural temporal breakpoints that don't align with the calendar year boundary — March 2023 and August 2023 may correspond to major model release waves. The monotonic increase in mean DIF magnitude (0.82→1.21→1.48) confirms that the instability is genuinely temporal, not an artifact of the cohort split point. Release date dominates variable importance (0.71) over parameter count and training data size, suggesting that WHEN a model was trained matters more than HOW BIG it is — consistent with the contamination/data-drift hypothesis over the "models just got better" alternative.

Looking at the METABENCH MMLU population under the best tier, I'm seeing that decoder-only architectures make up 99.98% of the 5,227 models, with essentially perfect agreement between the full population and decoder-only subset across DIF flags and IRT fit metrics, which means architectural heterogeneity isn't driving any of the observed effects. The architecture homogeneity of METABENCH MMLU is actually a meaningful empirical finding—the LLM evaluation ecosystem has essentially standardized on decoder-only models, which means architecture-based DIF analyses aren't even necessary for this population. Now I'm pulling the actual results for the completed experiments: plan_011 shows a cross-subject ΔTPR of +0.508 and ΔFPR of 0.000. I need to decide whether to include the full detailed results for the finished plans since the user asked for expanded data, then organize everything by plan ID and write out the final YAML structure.

For the completed experiments I'll use actual data, and for the planned ones I'll provide predictions with clear rationales explaining the expected outcomes. The user specifically requested that every prediction include a result_rationale explaining why those results would occur at that particular level. I'll aim for comprehensive coverage with specific metrics and concise 2-4 sentence explanations for each prediction, keeping the text fields focused rather than verbose.

Writing YAML with all 13 experiments...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba84d6c5-49f2-40cc-a4da-70ff208bc019",
  "isSidechain": false,
  "requestId": "req_011CbF5mjjVase5EZxk4rs6T",
  "type": "assistant",
  "uuid": "737da461-d479-4af0-be11-cd2f5a417122",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFPaQVJPPMaU5r5n2MSANH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18125,
      "cache_read_input_tokens": 11841,
      "output_tokens": 26863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18125,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 26863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18125
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

_source line 9 · 2026-05-21T04:38:10.677Z_

```yaml
tier: best
narrative_guidance: >
  Original framing holds without adjustment. Four claims presented as stated in paper_framing.md.
  Headline: "31% temporal instability is robust, not driven by capability gains (≤7.6%),
  and the field's web-overlap ground truth is fundamentally mismatched for item-level detection."
  Circularity ablation (plan_020, done) + GSM1K anti-correlation (plan_004 Step 3, done) form
  coherent two-pronged downstream story. Non-uniform DIF robustness check (SIBTEST/logistic
  regression on 5-10 representative subjects, not in experiment_plan but required for reviewer
  concern #9) confirms <5% items with substantial non-uniform DIF beyond MH flags (Jaccard ~0.89
  between MH and SIBTEST flag sets) — MH adequacy validated for this 99.98% decoder-only
  population. Appendix experiments (plan_002/003a/003b/003c/005/006/007/008/009) provide
  supplementary texture without becoming load-bearing. No claims need softening; appendix
  material stays in appendix. ICLR reviewers accept discovery-paper framing; DIF primer in §3
  successfully bridges psychometrics→ML vocabulary gap.
imagined_experiments:

  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      MH-DIF on METABENCH MMLU 5,219×12,508 matrix. Temporal cohort (2023 vs 2024-H1),
      ability-quintile cohort, within-family confound control, domain-specificity, random sanity.
      Proxy validation against Li et al. web-overlap labels.
    expected_results:
      temporal_ets_c_pct: 31.3
      temporal_fpr_li_clean: 0.318
      temporal_enrichment_vs_li: 0.96
      ability_ets_c_pct: 2.9
      ability_enrichment: 1.19
      within_family_llama2v3_c_pct: 61.3
      within_family_mistral_mixtral_c_pct: 38.7
      domain_spearman_rho: 0.307
      domain_spearman_p: 0.02
      sanity_random_split_c_pct: 0.18
      temporal_ability_jaccard: 0.014
      n_ref_temporal: 1253
      n_foc_temporal: 656
      n_items_tested: 12508
      n_ets_c_items: 3918
    result_rationale: >
      [DONE — actual registry data] 31.3% C% reflects genuine temporal item instability:
      model generations 2023→2024-H1 differ in training data composition, RLHF procedures,
      and data curation practices, all of which change how items function. Enrichment≈0.96
      against Li et al. labels is expected and predicted: web-overlap labels capture item
      existence on the internet (global exposure), not whether an item functions differently
      across cohorts (differential contamination). DIF detects the latter; the two measures
      are orthogonal by construction. Random-split sanity (0.18%) confirms the 31.3% is not
      a statistical artifact of the MH procedure. Domain correlation ρ=0.307 is modest —
      subjects where models improved more show slightly more DIF, but item-level decomposition
      (plan_019, done separately) confirms this explains at most 7.6% of the instability.
    tables:
      - name: "Table 1: DIF Detection Summary by Cohort Definition"
        columns: [cohort, N_ref, N_foc, ETS_A_pct, ETS_B_pct, ETS_C_pct, enrichment_Li]
        rows:
          - [temporal, 1253, 656, 52.1, 16.6, 31.3, 0.96]
          - [ability_quintile, 1044, 1044, 91.8, 5.3, 2.9, 1.19]
          - [random_sanity, 955, 955, 99.1, 0.7, 0.18, "—"]
      - name: "Table 2: Within-Family Confound Control"
        columns: [family_pair, N_ref, N_foc, C_pct, overlap_w_temporal_jaccard]
        rows:
          - [Llama-2 vs Llama-3, 161, 308, 61.3, 0.41]
          - [Mistral vs Mixtral, 89, 112, 38.7, 0.34]
    figures_description:
      - "Fig 1: Δ_MH distribution across 12,508 items for temporal cohort — bimodal with peaks at 0 and ±2.0"
      - "Fig 2: Domain-level DIF C% vs accuracy improvement scatterplot (57 subjects), ρ=0.307"
    analysis: >
      Temporal DIF at 31.3% is the load-bearing finding for Claim 1. The near-zero random-split
      sanity check (0.18%) and low ability-cohort C% (2.9%) establish that the temporal signal
      is real and specific to time, not ability. Within-family results (Llama 61.3%, Mistral 38.7%)
      show DIF persists even within architecture families, suggesting item instability is not
      purely a between-family artifact. Enrichment≈0.96 directly motivates the ground truth
      meta-critique (Claim 2).

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      Empirically validate DIF's robustness to RL-trained models. Three cohort compositions
      (SFT-only, +alignment-RL, +reasoning-RL). Traditional detector comparison (Min-K%, ConStat)
      on 10-15 reasoning-RL models individually.
    expected_results:
      n_sft_only_models: 2340
      n_alignment_rl_models: 477
      n_reasoning_rl_models: 13
      dif_flag_jaccard_sft_vs_sft_alignrl: 0.912
      dif_flag_jaccard_sft_vs_sft_allrl: 0.874
      dif_flag_jaccard_alignrl_vs_allrl: 0.935
      dif_c_pct_sft_only_cohort: 31.1
      dif_c_pct_sft_alignrl_cohort: 31.5
      dif_c_pct_sft_allrl_cohort: 31.8
      mink_auroc_reasoning_rl: 0.563
      constat_auroc_reasoning_rl: 0.614
      dif_auroc_cohort_with_rl: 0.831
      delong_p_dif_vs_mink: 0.032
      delong_p_dif_vs_constat: 0.078
      tost_equivalence_p: 0.117
      bootstrap_auroc_diff_ci_dif_mink: [0.06, 0.33]
      bootstrap_auroc_diff_ci_dif_constat: [-0.02, 0.28]
      power_detection_boundary_p: 0.45
      power_detection_boundary_delta: 1.4
      power_detection_boundary_N: 80
    result_rationale: >
      DIF's group-level design conditions on total score, making it fundamentally insensitive to
      individual model output distributions. Adding 13 reasoning-RL models to a cohort of N≥80
      shifts the score distribution marginally (~0.3pp in C%) because MH's quintile-based matching
      absorbs ability variation. The high Jaccard (0.87-0.91) reflects that DIF flags are driven
      by the bulk population, not the RL tail. Min-K% degrades to near-chance (AUROC=0.56) because
      RL training contracts the NLL gap that Min-K% exploits — the per-token likelihood distribution
      becomes flatter, destroying the memorization signal. ConStat fares slightly better (0.61)
      because perturbation sensitivity is partially preserved under alignment-RL but substantially
      reduced under reasoning-RL (GRPO/PPO explicitly optimize for robust reasoning). TOST at
      p=0.117 is inconclusive, honestly reflecting the N=13 limitation. This is presented in
      limitations as "suggestive evidence of RL robustness, underpowered for formal equivalence."
    tables:
      - name: "Table A1: DIF Flag Stability Across Cohort Compositions"
        columns: [cohort, N_total, C_pct, Jaccard_vs_SFT]
        rows:
          - [SFT-only, 2340, 31.1, 1.000]
          - [SFT + alignment-RL, 2817, 31.5, 0.912]
          - [SFT + all-RL, 2830, 31.8, 0.874]
      - name: "Table A2: Per-Model Detector Comparison on Reasoning-RL Models"
        columns: [detector, AUROC, "95% CI", degradation_vs_nonRL]
        rows:
          - [Min-K%, 0.563, "[0.41, 0.72]", "-0.31"]
          - [ConStat, 0.614, "[0.46, 0.77]", "-0.24"]
          - [DIF (group), 0.831, "[0.74, 0.92]", "-0.02"]
    figures_description:
      - "Fig A1: AUROC comparison across detectors for reasoning-RL models with bootstrap CIs"
      - "Fig A2: DIF detection power surface as function of exploitation rate p and effect size δ"
    analysis: >
      Results confirm the theoretical argument: DIF's group-level conditioning makes it robust
      to RL-induced output distribution changes, while per-model detectors (Min-K%, ConStat) degrade
      substantially. However, N=13 reasoning-RL models precludes formal equivalence testing.
      Appendix-appropriate: strengthens Claim 1 narrative without being load-bearing. The power
      surface shows DIF retains detection for δ≥1.4 at p≥0.45, covering the operationally
      relevant regime (large effects with moderate exploitation).

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      Independent ConStat-style perturbation evaluation on MMLU. Generate paraphrases for 200+
      items, compare original vs reformulated performance, apply FDR-controlled detection.
    expected_results:
      n_items_paraphrased: 237
      semantic_similarity_mean: 0.918
      human_quality_pct: 94.1
      constat_tpr_non_rl_contaminated: 0.438
      constat_tpr_rl_contaminated: 0.172
      constat_fpr_fdr_q005: 0.038
      cohens_d_non_rl: 0.871
      cohens_d_rl: 0.293
      perf_drop_contaminated_non_rl_pct: -13.1
      perf_drop_contaminated_rl_pct: -4.2
      perf_drop_clean_pct: -2.8
      paraphrase_difficulty_shift_mean: 0.04
      n_models_evaluated: 48
    result_rationale: >
      ConStat's detection mechanism exploits surface-level memorization: models that memorized
      exact item phrasings show large performance drops on semantically equivalent paraphrases.
      Non-RL models exhibit this cleanly (d=0.87, TPR=0.44) because their memorization is
      token-sequence-specific. RL-trained models show attenuated signal (d=0.29, TPR=0.17)
      because reward optimization encourages generalization beyond exact training sequences —
      the RL objective effectively launders memorization into robust capability, making it
      indistinguishable from genuine learning. FPR at 0.038 confirms FDR control works. The
      clean-item performance drop (-2.8%) reflects natural difficulty increase from paraphrasing
      (slight semantic drift, unfamiliar phrasing) rather than contamination. This complements
      DIF: ConStat detects per-model surface memorization, DIF detects group-level differential
      functioning regardless of mechanism.
    tables:
      - name: "Table A3: ConStat Detection by Model Training Type"
        columns: [model_type, N_models, TPR, FPR, Cohen_d, perf_drop_pct]
        rows:
          - [SFT-only, 22, 0.438, 0.038, 0.871, -13.1]
          - [Alignment-RL, 18, 0.172, 0.041, 0.293, -4.2]
          - [Clean (no contamination), 8, "—", 0.038, "—", -2.8]
    figures_description:
      - "Fig A3: Performance drop distribution (original vs paraphrase) for contaminated vs clean items"
      - "Fig A4: ConStat detection power as function of paraphrase semantic distance"
    analysis: >
      ConStat demonstrates moderate detection of surface memorization in non-RL models but degrades
      substantially for RL models. This characterizes ConStat's complementary detection niche and
      motivates ensemble approaches. Appendix-appropriate: validates one component of the ensemble
      framework (Claim 2 old, now dropped to future work) without being needed for current claims.

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      DVD generation variance evaluation on MMLU. 50 responses per item via temperature sampling
      on 10-15 open-weight models. Detect bimodal distributions as contamination signal.
    expected_results:
      n_models: 12
      n_items_evaluated: 200
      n_generations_per_item: 50
      temperature: 0.8
      dvd_tpr_verbatim: 0.523
      dvd_tpr_variant: 0.138
      dvd_fpr: 0.062
      bimodality_coeff_contaminated: 0.714
      bimodality_coeff_clean: 0.283
      gen_variance_contaminated_mean: 0.087
      gen_variance_contaminated_sd: 0.131
      gen_variance_clean_mean: 0.312
      gen_variance_clean_sd: 0.108
      auroc_verbatim: 0.813
      auroc_variant: 0.571
      gpu_hours_used: 52
    result_rationale: >
      Verbatim memorization produces near-deterministic outputs — the model has effectively learned
      a lookup table for memorized items, generating the correct answer with probability >0.95
      regardless of temperature. This creates bimodal generation distributions (always correct or
      fully random) with near-zero variance, easily distinguished from clean items (moderate
      variance reflecting genuine uncertainty). Variant contamination does NOT produce this
      bimodality because the model learned the underlying concept rather than the exact answer
      string — generation variance remains moderate, and DVD cannot distinguish "learned from
      training data" from "genuinely knows." This limits DVD to a specific niche: detecting
      exact-match verbatim memorization of item text + answer. Complementary to DIF (group-level,
      mechanism-agnostic) and ConStat (perturbation-based, per-model).
    tables:
      - name: "Table A4: DVD Detection by Contamination Type"
        columns: [contamination_type, N_items, TPR, FPR, bimodality_coeff, mean_gen_variance]
        rows:
          - [verbatim, 80, 0.523, 0.062, 0.714, 0.087]
          - [variant, 60, 0.138, 0.062, 0.391, 0.224]
          - [clean, 60, "—", 0.062, 0.283, 0.312]
    figures_description:
      - "Fig A5: Generation variance distributions for verbatim-contaminated vs clean items"
      - "Fig A6: Bimodality coefficient histogram across all items, colored by contamination status"
    analysis: >
      DVD occupies a narrow but clear detection niche: verbatim exact-match memorization. Its
      inability to detect variant contamination is a fundamental limitation — generation variance
      cannot distinguish "learned from contaminated data" from "genuinely competent." This
      underscores the complementarity argument for ensemble approaches and the advantage of
      DIF's mechanism-agnostic group-level detection. Appendix-appropriate: useful for
      characterizing the detection landscape but not needed for current claims.

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      Fuse DIF + ConStat + DVD into multi-signal ensemble. Majority voting and weighted fusion.
      Coverage analysis by contamination mechanism.
    expected_results:
      dif_alone_tpr: 0.682
      constat_alone_tpr: 0.438
      dvd_alone_tpr: 0.523
      majority_2of3_tpr: 0.731
      majority_2of3_fpr: 0.028
      majority_2of3_precision: 0.921
      weighted_fusion_tpr: 0.778
      weighted_fusion_fpr: 0.057
      weighted_fusion_precision: 0.883
      uniform_weight_tpr: 0.752
      uniform_weight_fpr: 0.044
      optimal_weights_dif: 0.43
      optimal_weights_constat: 0.32
      optimal_weights_dvd: 0.25
      cv_weight_stability_cv: 0.13
      coverage_dif_only_pct: 22.8
      coverage_constat_only_pct: 13.6
      coverage_dvd_only_pct: 8.1
      coverage_multi_signal_pct: 55.5
    result_rationale: >
      The three detectors exploit orthogonal contamination dimensions: DIF measures differential
      group-level item functioning (mechanism-agnostic, requires cohort comparison), ConStat
      measures per-model perturbation sensitivity (targets surface memorization), DVD measures
      generation variance (targets verbatim memorization). Their error patterns are weakly
      correlated because they target different aspects of contamination. Majority voting
      suppresses false positives (FPR=0.028) by requiring convergent evidence from 2+
      independent mechanisms. Weighted fusion gains ~5pp TPR over majority voting at the cost
      of higher FPR (0.057) by allowing strong single-signal evidence to override absent signals.
      Optimal weights favor DIF (0.43) because it has the broadest coverage (mechanism-agnostic,
      group-level), followed by ConStat (0.32) and DVD (0.25). The modest improvement over
      uniform weights reflects limited calibration data.
    tables:
      - name: "Table A5: Ensemble Detection Performance"
        columns: [strategy, TPR, FPR, precision, F1]
        rows:
          - [DIF only, 0.682, 0.036, 0.892, 0.773]
          - [ConStat only, 0.438, 0.038, 0.854, 0.579]
          - [DVD only, 0.523, 0.062, 0.809, 0.635]
          - [2-of-3 majority, 0.731, 0.028, 0.921, 0.815]
          - [Weighted fusion, 0.778, 0.057, 0.883, 0.827]
          - [Uniform weights, 0.752, 0.044, 0.893, 0.817]
    figures_description:
      - "Fig A7: Venn diagram of detection coverage by signal type"
      - "Fig A8: ROC curves for individual signals and ensemble strategies"
    analysis: >
      Ensemble improves coverage but is not needed for current paper claims (Claim 2 pivoted from
      ensemble to ground truth meta-critique). Results support future work direction: multi-signal
      contamination detection as a practical pipeline. The 22.8% DIF-only coverage confirms DIF
      detects contamination modes invisible to per-model methods. Appendix-appropriate:
      demonstrates feasibility without being load-bearing.

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      GSM8K DIF replication (1,319 items × 6,702 models). Semi-synthetic validation.
      GSM1K contamination gap correlation (N=33).
    expected_results:
      step1_n_items: 1319
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
      step3_bca_ci_partial: [-0.640, -0.058]
      step3_permutation_p: 0.014
      step3_cook_d_max_model: Deepseek-math-7b-rl
      step3_leave_one_out_r_range: [-0.537, -0.374]
    result_rationale: >
      [DONE — actual registry data] GSM8K temporal DIF at 18.9% (vs MMLU 31.3%) reflects
      GSM8K's more homogeneous construct (single-domain math vs 57-subject MMLU) — fewer
      dimensions of variation means fewer items whose functioning changes across generations.
      Semi-synthetic ΔTPR=+0.818 confirms the detection framework ports to single-domain
      benchmarks with high power. Step 3 anti-correlation (r=−0.478) is the key downstream
      finding: models with larger GSM8K-GSM1K contamination gaps show disproportionately LOWER
      performance on DIF-C items. This is consistent with contamination producing surface-level
      gains concentrated on non-DIF items (memorized items that function uniformly across
      cohorts), while DIF items capture genuine capability differences that contamination cannot
      inflate. All BCa CIs exclude zero, and leave-one-out analysis confirms robustness to
      individual influential models. N=33 is honestly acknowledged as suggestive — the finding
      is consistent but a larger matched sample would strengthen it.
    tables:
      - name: "Table 4: GSM8K DIF Summary"
        columns: [matching, C_pct, sanity_pct, ΔTPR_p10]
        rows:
          - [standard (total score), 18.9, 0.3, 0.818]
          - [external (cross-benchmark), 47.4, "—", 0.517]
      - name: "Table 5: GSM1K Contamination Gap Correlation"
        columns: [statistic, value, p, "95% BCa CI"]
        rows:
          - [Pearson r, -0.478, 0.005, "[-0.714, -0.155]"]
          - [Spearman ρ, -0.403, 0.020, "[-0.687, -0.031]"]
          - [Partial r, -0.385, 0.027, "[-0.640, -0.058]"]
    figures_description:
      - "Fig 5: GSM1K contamination gap vs DIF-C item accuracy scatterplot (N=33) with regression line and BCa CI band"
      - "Fig 6: Leave-one-out sensitivity — Pearson r under sequential model removal"
    analysis: >
      GSM8K replication confirms semi-synthetic framework portability (Claim 3). GSM1K
      anti-correlation provides the fourth layer of Claim 4 (downstream impact). Under best
      tier, reviewers treat r=−0.478 as suggestive-but-consistent rather than attacking it
      as underpowered — the convergent evidence (all CIs exclude zero, permutation p=0.014,
      leave-one-out stable) is sufficient for a discovery paper. Plan_017 redundancy result
      (ρ≈0.997) independently supports Claim 4 even if Step 3 is discounted.

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      Bifactor IRT model on METABENCH MMLU (general + 57 subject factors). Anchor item
      selection. Fixed-parameter equating pilot.
    expected_results:
      general_factor_variance_pct: 58.3
      subject_specific_variance_mean_pct: 30.8
      residual_variance_pct: 10.9
      bifactor_rmsea: 0.019
      bifactor_cfi: 0.953
      bifactor_tli: 0.941
      unidim_rmsea: 0.035
      unidim_cfi: 0.882
      unidim_tli: 0.864
      n_anchor_items: 5640
      anchor_criteria: "no DIF, rpbis>0.20, general loading>0.30"
      within_subject_dif_after_bifactor_pct: 35.8
      within_subject_dif_unidim_pct: 38.1
      dif_reduction_from_bifactor_pp: 2.3
      equating_rho_general: 0.961
      equating_rho_subject_range: [0.891, 0.974]
      equating_rho_subject_below_095: 8
      convergence_em_iterations: 2140
      convergence_achieved: true
    result_rationale: >
      Bifactor correctly identifies MMLU's multidimensional structure — 57 subjects create
      substantial specific factors (31% of variance). However, DIF persists at 35.8% even
      after extracting subject-specific variance (only 2.3pp reduction from 38.1%), confirming
      that the instability is genuinely item-level, not an artifact of dimensional confounding.
      The general factor dominates (58%) because MMLU subjects share a common "general LLM
      ability" axis — models good at one subject tend to be good at others. IRT fit improves
      substantially (RMSEA 0.035→0.019, CFI 0.88→0.95), validating that multidimensionality
      was the primary source of unidimensional misfit, but this improved fit does not resolve
      DIF. Equating at ρ=0.961 on the general factor demonstrates feasibility of anchor-based
      score maintenance, but 8/57 subjects fall below ρ=0.95 (small-N subjects with <50 items
      where anchor selection is constrained). This supports future work on benchmark maintenance
      but is appropriately appendix material — the finding that bifactor doesn't resolve DIF
      is itself evidence for Claim 1's robustness.
    tables:
      - name: "Table A6: Model Fit Comparison"
        columns: [model, RMSEA, CFI, TLI, n_params]
        rows:
          - [Unidimensional, 0.035, 0.882, 0.864, 25016]
          - [Bifactor (1+57), 0.019, 0.953, 0.941, 37524]
      - name: "Table A7: DIF Persistence After Bifactor Conditioning"
        columns: [conditioning, within_subject_C_pct, reduction_pp]
        rows:
          - [None (unidimensional), 38.1, "—"]
          - [Bifactor general+specific, 35.8, 2.3]
    figures_description:
      - "Fig A9: Bifactor general factor loadings across 57 subjects"
      - "Fig A10: Within-subject DIF C% before vs after bifactor conditioning (paired comparison)"
    analysis: >
      Bifactor's 2.3pp DIF reduction (~6% relative) confirms that >90% of temporal DIF is
      genuine item-level instability, not dimensional misfit artifact. This is the strongest
      possible evidence for Claim 1's robustness to IRT model specification concerns. The
      equating pilot demonstrates feasibility but remains below the quality bar for a main-body
      claim — consistent with paper_framing's decision to relegate this to appendix. The fit
      improvement (RMSEA halved) is itself valuable: it confirms the diagnosis that 98% |Lz|>2
      reflects multidimensionality, not fundamental model invalidity.

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      LLM-based replacement item generation for DIF-flagged MMLU items. Prompt-based vs
      student-simulation difficulty estimation. Holdout validation.
    expected_results:
      n_items_generated: 500
      n_target_items: 250
      candidates_per_target: 2
      difficulty_rho_prompt: 0.362
      difficulty_rho_simulation: 0.731
      difficulty_rho_best_candidate: 0.793
      construct_alignment_expert_pct: 88.7
      discrimination_rpbis_rho: 0.514
      holdout_within_015_difficulty_pct: 83.6
      distractor_quality_plausible_pct: 76.2
      simulation_panel_n_models: 30
      gpu_hours_used: 164
    result_rationale: >
      LLMs generate on-topic items reliably (89% construct alignment) because they understand
      MMLU subject boundaries and question formats. However, prompt-based difficulty targeting
      fails (ρ=0.36) because the generator lacks fine-grained knowledge of what makes an item
      hard for OTHER LLMs — difficulty is an emergent property of item-population interaction,
      not an intrinsic text feature. Student simulation (using 30 diverse models as examinees)
      provides empirical difficulty estimates that capture actual model behavior, achieving
      ρ=0.73 — approaching the r=0.75-0.82 reported in the student simulation literature
      (arXiv 2601.09953). Best-candidate selection from 2 options improves to ρ=0.79 by
      choosing the candidate closer to target difficulty. Distractor quality (76%) is the
      weakest link: generating plausible wrong answers for multiple-choice items requires
      understanding common misconceptions, which LLMs model imperfectly. This finding supports
      the conclusion that automated item generation is feasible but requires empirical
      calibration — prompt-based difficulty targeting alone is insufficient.
    tables:
      - name: "Table A8: Difficulty Estimation Comparison"
        columns: [method, ρ_with_target, MAE_difficulty, coverage]
        rows:
          - [Prompt-based targeting, 0.362, 0.183, "100%"]
          - [Student simulation (30 models), 0.731, 0.094, "100%"]
          - [Best of 2 candidates, 0.793, 0.078, "100%"]
    figures_description:
      - "Fig A11: Target vs estimated difficulty scatter (prompt-based vs simulation)"
      - "Fig A12: Holdout validation — generated item difficulty vs empirical difficulty on new models"
    analysis: >
      The prompt→simulation gap (ρ=0.36→0.73) is the key practical finding: empirical
      calibration is essential for item replacement pipelines. Appendix-appropriate: supports
      future benchmark regeneration work but is below the quality bar for a main-body claim
      (consistent with paper_framing's decision to drop regeneration from claims). The 76%
      distractor quality suggests human review remains necessary for production deployment.

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      Bayesian cumulative DIF priors across 4 simulated benchmark administrations.
      Power accumulation for medium effects (δ=1.0).
    expected_results:
      n_administrations: 4
      n_per_admin: 80
      delta_simulated: 1.0
      individual_power_mean: 0.415
      individual_power_range: [0.398, 0.432]
      cumulative_power_after_2: 0.576
      cumulative_power_after_3: 0.718
      cumulative_power_after_4: 0.812
      fpr_across_accumulations_max: 0.048
      bf10_after_1: 2.14
      bf10_after_2: 4.83
      bf10_after_3: 9.27
      bf10_after_4: 16.7
      bf10_moderate_evidence_threshold: 3.0
      power_at_bf10_gt3_after_2: 0.648
      mh_individual_power_at_delta10: 0.383
      power_gain_cumulative_vs_individual: "+0.303 (after 3)"
    result_rationale: >
      Individual MH tests at N=80, δ=1.0 have insufficient power (~0.42) — this is the "power
      gap" identified in phase 2 simulations (pass criterion required δ≥1.4). Bayesian updating
      converts individually inconclusive tests into cumulative evidence: the posterior from each
      administration constrains the prior for the next. After 3 administrations, cumulative power
      crosses 0.70 (the conventional adequate-power threshold) because the accumulated evidence
      from 3×80=240 effective observations exceeds what any single N=80 test provides. The Bayes
      factor trajectory (2.1→4.8→9.3→16.7) follows the expected log-linear accumulation under
      consistent DIF. FPR remains controlled (≤0.048) because the Bayesian framework naturally
      penalizes inconsistent evidence — items with spurious DIF in one administration but not
      others see their posterior regress toward the null. This addresses the practical concern
      that benchmark monitoring requires repeated measurement, not one-shot detection.
    tables:
      - name: "Table A9: Cumulative Bayesian Power by Administration"
        columns: [n_admins, cumulative_N, power, BF10, FPR]
        rows:
          - [1, 80, 0.415, 2.14, 0.042]
          - [2, 160, 0.576, 4.83, 0.044]
          - [3, 240, 0.718, 9.27, 0.046]
          - [4, 320, 0.812, 16.7, 0.048]
    figures_description:
      - "Fig A13: Cumulative power curve as function of number of administrations (δ=1.0, N=80 each)"
      - "Fig A14: BF₁₀ trajectory for true-DIF vs null items across 4 administrations"
    analysis: >
      Simulation-only result (no real data). Confirms theoretical prediction that Bayesian
      cumulative DIF closes the power gap for medium effects. The practical implication:
      benchmark monitoring programs can detect δ=1.0 DIF after 3 waves of ~80 models each,
      even though no single wave has adequate power. Appendix-appropriate: methodological
      contribution for future longitudinal monitoring, not needed for current claims.
      Underdeveloped for main-body inclusion — needs real multi-wave data to validate.

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      Progressive item replacement validity analysis. Ranking stability, score reliability,
      construct coverage as function of replacement rate (5-50%).
    expected_results:
      replacement_rates: [0.05, 0.10, 0.20, 0.31, 0.50]
      rho_at_005: 0.9993
      rho_at_010: 0.9984
      rho_at_020: 0.9968
      rho_at_031: 0.9951
      rho_at_050: 0.9912
      alpha_full: 0.9937
      alpha_at_031: 0.9882
      alpha_at_050: 0.9791
      construct_coverage_at_031: "57/57"
      construct_coverage_at_050: "56/57"
      construct_coverage_threshold_subjects_below_5items: 0.62
      validity_threshold_rho_lt_099: 0.453
      shr_full: 0.9934
      shr_at_031: 0.9881
      shr_at_050: 0.9763
      replacement_strategy: "DIF-flagged items replaced by matched-difficulty anchors"
    result_rationale: >
      MMLU's massive redundancy (12,508 items, most subjects with 100+ items) provides enormous
      buffering against item replacement. Ranking stability at 31% replacement (ρ=0.9951) closely
      matches plan_017's DIF removal result (ρ=0.997) — the slight discrepancy reflects
      calibration noise in replacement items vs clean removal. The curve is convex: initial
      replacement costs almost nothing (ρ=0.9993 at 5%) because replaced items are drawn from
      the unstable pool (high DIF, contributing noise rather than signal). The validity threshold
      (ρ<0.99) is not crossed until ~45% replacement, demonstrating that even aggressive
      maintenance preserves benchmark validity. Construct coverage holds at 57/57 subjects through
      31% because DIF items are distributed across subjects (not clustered in a few), so no
      subject loses all its items. Score reliability drops only 0.55pp (0.994→0.988) at 31%
      because Cronbach's α is driven by total item count and inter-item correlation, both of
      which remain high after replacement.
    tables:
      - name: "Table A10: Validity Degradation Under Progressive Replacement"
        columns: [replacement_pct, ρ_ranking, α_reliability, SHR, construct_coverage]
        rows:
          - [0, 1.000, 0.994, 0.993, "57/57"]
          - [5, 0.999, 0.993, 0.993, "57/57"]
          - [10, 0.998, 0.992, 0.992, "57/57"]
          - [20, 0.997, 0.990, 0.990, "57/57"]
          - [31, 0.995, 0.988, 0.988, "57/57"]
          - [50, 0.991, 0.979, 0.976, "56/57"]
    figures_description:
      - "Fig A15: Validity metrics as function of replacement rate (ρ, α, SHR overlaid)"
      - "Fig A16: Per-subject construct coverage at 31% and 50% replacement"
    analysis: >
      Directly supports the "instability ≠ invalidity" framing: replacing 31% of items (all
      DIF-flagged) preserves >99.5% of ranking information, demonstrating massive measurement
      redundancy. The convex degradation curve means benchmark maintainers have large headroom
      for item updates. Appendix-appropriate: clean supplementary result that reinforces Claim 4
      (redundancy layer) without adding new claims.

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      Item-Focused Trees with continuous release date covariate. Compare detection power
      and flexibility vs categorical MH-DIF.
    expected_results:
      n_models_with_release_date: 3412
      ift_significant_items_pct: 33.8
      ift_mh_overlap_jaccard: 0.762
      ift_only_items_pct: 8.3
      mh_only_items_pct: 5.2
      natural_breakpoints: ["2023-03-15", "2023-08-22", "2024-01-10"]
      n_terminal_nodes: 4
      release_date_variable_importance: 0.71
      param_count_importance: 0.14
      training_data_size_importance: 0.09
      mean_dif_early_2023: 0.82
      mean_dif_late_2023: 1.21
      mean_dif_early_2024: 1.48
      dif_magnitude_release_date_r: 0.391
      gradual_drift_items_pct: 8.3
      sharp_transition_items_pct: 5.2
    result_rationale: >
      IFT treats release date as a continuous covariate, revealing temporal DIF structure that
      categorical splits can miss. The 76% Jaccard overlap with MH confirms that the binary
      2023/2024-H1 split captures most of the signal — the categorical approximation is adequate
      for the primary analysis. The additional 8.3% IFT-only items are "gradual drifters" whose
      functioning changes smoothly across the timeline without a single dramatic shift — these
      are invisible to any binary split but accumulate meaningful DIF over the full period. Natural
      breakpoints (March 2023, August 2023, January 2024) likely correspond to major model release
      waves (Llama-2 era, post-ChatGPT proliferation, GPT-4 derivatives). The monotonic DIF
      magnitude increase (0.82→1.21→1.48) confirms genuine temporal trend rather than categorical
      artifact. Release date dominates variable importance (0.71) over model size (0.14) — WHEN
      matters more than HOW BIG, consistent with training data composition / contamination
      explaining instability rather than raw capability scaling.
    tables:
      - name: "Table A11: IFT vs MH-DIF Detection Comparison"
        columns: [method, significant_items_pct, unique_items_pct, natural_breakpoints]
        rows:
          - [MH categorical, 31.3, 5.2, "2023 vs 2024-H1 (manual)"]
          - [IFT continuous, 33.8, 8.3, "Mar-23, Aug-23, Jan-24 (data-driven)"]
      - name: "Table A12: IFT Variable Importance"
        columns: [covariate, importance, interpretation]
        rows:
          - [release_date, 0.71, "temporal position drives DIF"]
          - [param_count, 0.14, "larger models show slightly different DIF"]
          - [training_data_size, 0.09, "marginal contribution"]
    figures_description:
      - "Fig A17: DIF magnitude as continuous function of release date (IFT smoothed curve)"
      - "Fig A18: IFT tree structure showing natural temporal breakpoints"
    analysis: >
      IFT provides a complementary lens: confirms the temporal DIF finding is robust to the
      choice of categorical split point, and reveals gradual drift items missed by binary
      comparison. The natural breakpoints are empirically interesting (potential link to
      model release waves) but not developed into a claim. Appendix-appropriate: robustness
      check that strengthens Claim 1 without adding complexity to the main narrative.

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      DIF within decoder-only-only subpopulation. Test whether architecture heterogeneity
      removal improves IRT fit and reduces spurious DIF.
    expected_results:
      total_models: 5227
      decoder_only_models: 5226
      decoder_only_pct: 99.98
      non_decoder_models: 1
      c_pct_full: 31.3
      c_pct_decoder_only: 31.3
      jaccard_full_vs_decoder: 1.000
      irt_rmsea_decoder_only: 0.033
      irt_rmsea_full: 0.034
      lz_gt2_pct_decoder_only: 97.9
      lz_gt2_pct_full: 98.0
      delta_mh_correlation_full_vs_decoder: 0.9999
    result_rationale: >
      METABENCH MMLU is 99.98% decoder-only (5226/5227), reflecting the empirical reality that
      virtually all LLMs evaluated on MMLU since 2023 are autoregressive transformers. The single
      non-decoder model has zero statistical influence on any group-level analysis — removing it
      produces Jaccard=1.0 because MH chi-squared tests are robust to single-observation
      perturbations in large samples. IRT fit does not improve (RMSEA 0.034→0.033) because the
      misfit (98% |Lz|>2) is driven by MMLU's inherent multidimensionality (57 subjects), not
      architecture heterogeneity. This result definitively dissolves the worst-case reviewer
      concern about architecture confounding. The architecture homogeneity is itself an empirical
      finding: the LLM evaluation ecosystem has converged on decoder-only transformers, making
      architecture-based stratification unnecessary for this population. Future benchmarks with
      more diverse architectures (e.g., state-space models, hybrid architectures) would need to
      revisit this analysis.
    tables:
      - name: "Table 3: Architecture Stratification"
        columns: [population, N, C_pct, RMSEA, "|Lz|>2 pct"]
        rows:
          - [Full, 5227, 31.3, 0.034, "98.0%"]
          - [Decoder-only, 5226, 31.3, 0.033, "97.9%"]
    figures_description:
      - "Fig 3: Architecture composition of METABENCH MMLU (pie chart: 99.98% decoder-only)"
    analysis: >
      This is the most decisive robustness check in the paper: the architecture confound concern
      is dissolved empirically rather than argued away theoretically. Main-body appropriate as
      part of Claim 1 robustness (§4). The finding that the LLM ecosystem is architecturally
      homogeneous has broader implications for psychometric analyses of LLM benchmarks — the
      "examinee population" is far more homogeneous than human testing populations, which
      simplifies DIF analysis but raises questions about construct validity.

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: >
      Inject known contamination into real METABENCH response matrix. Measure DIF detection
      power under controlled ground truth. Vary injection parameters.
    expected_results:
      temporal_external_tpr_p0: 0.326
      temporal_external_tpr_p03: 0.548
      temporal_external_tpr_p05: 0.834
      temporal_external_tpr_p07: 0.990
      temporal_external_tpr_p10: 1.000
      temporal_external_fpr: 0.314
      temporal_external_delta_tpr_p05: 0.508
      temporal_external_delta_tpr_p10: 0.674
      cross_subject_delta_fpr: 0.000
      within_subject_fpr_inflation_p10: 0.186
      ability_external_tpr_p10: 0.800
      ability_external_fpr: 0.493
      dose_response_monotonic: true
      matching_variable_contamination_confirmed: true
    result_rationale: >
      [DONE — actual registry data] Semi-synthetic injection into real response matrices provides
      the controlled ground truth that proxy labels cannot. ΔTPR=+0.508 at p=0.5 demonstrates
      that DIF detects differential contamination when the exploitation rate is moderate — this
      is the core validation for the detection claim. The dose-response curve (p=0.3→0.5→0.7→1.0
      maps to ΔTPR=0.22→0.51→0.66→0.67) confirms detection power scales with contamination
      intensity, as expected from the DIF effect size formula (Δ_MH ∝ log odds ratio of correct
      response, which increases with exploitation probability). Cross-subject matching eliminates
      FPR inflation (ΔFPR=0.000) because the matching variable (total score on OTHER subjects) is
      causally independent of contamination injected into a specific subject. Within-subject
      matching shows FPR inflation (+0.186) because contaminating items in a subject inflates
      total score on that subject, which contaminates the matching variable. This distinction
      is a subtle but general methodological insight: any DIF application where the matching
      variable can be affected by the grouping variable will show FPR inflation.
    tables:
      - name: "Table 6: Semi-Synthetic Detection Power (Cross-Subject Matching)"
        columns: [exploitation_p, TPR, ΔTPR, FPR, ΔFPR]
        rows:
          - [0.0, 0.326, 0.000, 0.314, 0.000]
          - [0.3, 0.548, 0.222, 0.314, 0.000]
          - [0.5, 0.834, 0.508, 0.314, 0.000]
          - [0.7, 0.990, 0.664, 0.314, 0.000]
          - [1.0, 1.000, 0.674, 0.314, 0.000]
      - name: "Table 7: Matching Variable Comparison"
        columns: [matching, ΔFPR_p10, ΔTPR_p05, FPR_inflation]
        rows:
          - [Within-subject, 0.186, "varies", "YES"]
          - [Cross-subject, 0.000, 0.508, "NO"]
    figures_description:
      - "Fig 4: Dose-response curve — ΔTPR as function of exploitation rate p"
      - "Fig 7: FPR comparison between within-subject and cross-subject matching across injection levels"
    analysis: >
      This is the primary validation for Claim 3 (semi-synthetic framework) and provides
      controlled ground truth addressing the circularity concern in Claim 2. The cross-subject
      matching innovation (ΔFPR=0.000) is the key methodological contribution — it solves the
      matching variable contamination problem that plagues within-subject DIF when the conditioning
      variable is endogenous. Main-body material for §4.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "737da461-d479-4af0-be11-cd2f5a417122",
  "isSidechain": false,
  "requestId": "req_011CbF5mjjVase5EZxk4rs6T",
  "type": "assistant",
  "uuid": "258ec30e-7ae9-43c5-bd6c-67d4c4f316b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFPaQVJPPMaU5r5n2MSANH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18125,
      "cache_read_input_tokens": 11841,
      "output_tokens": 26863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18125,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 26863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18125
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All 4 claims survive robustness checks intact; reviewers accept discovery-paper framing at ICLR 核心假设：['SIBTEST/logistic regression confirms <5% items with…",
  "leafUuid": "258ec30e-7ae9-43c5-bd6c-67d4c4f316b2",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric DIF analysis of LLM benchmarks",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All 4 claims survive robustness checks intact; reviewers accept discovery-paper framing at ICLR 核心假设：['SIBTEST/logistic regression confirms <5% items with…",
  "leafUuid": "258ec30e-7ae9-43c5-bd6c-67d4c4f316b2",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Psychometric DIF analysis of LLM benchmarks",
  "sessionId": "a0546b48-bdea-4921-889b-877f45f5f952"
}
```

---
