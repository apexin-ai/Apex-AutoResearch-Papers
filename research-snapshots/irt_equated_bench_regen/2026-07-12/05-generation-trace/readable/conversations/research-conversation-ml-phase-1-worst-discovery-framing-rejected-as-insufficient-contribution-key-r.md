# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Discovery framing rejected as insufficient contribution; key robustness che

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/4a1d2807-329e-4949-b6cf-c299e99c22e3.jsonl`
- **Structured JSON:** [`9bd94eaa5d064ce32ef3.json`](../../sessions/9b/9bd94eaa5d064ce32ef3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:47:48.428Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:47:48.428Z",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Discovery framing rejected as insufficient contribution; key robustness checks reveal structural weaknesses requiring reframing\n核心假设：['SIBTEST reveals >15% items with substantial non-uniform DIF missed by MH — MH alone is demonstrably insufficient for this population, undermining 31% as a precise estimate', \"Majority of reviewers (≥2/3) reject discovery-paper framing: 'applying a 1988 method to a new dataset is not an ICLR contribution'\", 'GSM1K correlation collapses under difficulty control (partial r → [−0.15, +0.05], CI solidly includes zero) — sub-finding 4 is dead', \"IRT misfit treated as invalidating: 'if 98% of models misfit, your ability estimates are meaningless, so MH conditioning on total score is the only defensible approach' — but then 31% reflects score-based rather than ability-based DIF\", \"At least 1 reviewer identifies the 31% baseline FPR problem as circular: 'you flag 31% as unstable, then show instability ≠ invalidity — but you never establish what the true instability rate should be'\", \"Semi-synthetic injection dismissed as too artificial: flipping incorrect→correct doesn't model real contamination mechanisms (memorization patterns, partial recall)\"]\n关键指标范围：{'nonuniform_dif_additional_pct': [15, 30], 'mh_sibtest_flag_jaccard': [0.4, 0.6], 'gsm1k_partial_r_lower_ci': [-0.35, 0.1], 'iclr_avg_overall_score': [3.5, 5.0], 'iclr_avg_novelty_score': [3.0, 4.5], 'iclr_avg_soundness_score': [4.0, 5.5], 'accept_probability': [0.03, 0.15]}\n叙事方向：Reframe from \"DIF reveals benchmark structural problems\" to \"Empirical characterization of measurement stability in LLM benchmarks: challenges and an open framework.\" Three pivots, same venue: (1) Lead with the semi-synthetic validation framework (Claim 3) as the primary methodological contribution — ΔTPR methodology + cross-subject matching (ΔFPR=0.000) is a genuinely novel, reusable tool. Elevate from supporting evidence to central contribution. (2) Reposition Claim 1 as a case study motivating the framework, not the headline finding. Report MH AND SIBTEST results jointly; present the discrepancy as \"characterizing which DIF types matter for LLM benchmarks\" rather than defending a single 31% number. The instability finding becomes \"≥18-31% depending on DIF type and threshold\" — a range, not a point estimate. (3) Drop GSM1K correlation entirely from the main paper. Strengthen the circularity ablation (plan_020) and redundancy finding (ρ≈0.997) as the downstream story — these are unaffected by non-uniform DIF concerns and don't depend on external correlation. Ground truth meta-critique (Claim 2) survives intact in all scenarios — make it more prominent. Add a \"Practitioner's Guide\" section: concrete recommendations for when/how to run DIF on new benchmarks, making the paper immediately useful regardless of MMLU-specific findings. Target remains ICLR 2027 — the framework + meta-critique + practitioner guide is a different but viable paper at the same venue.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nfocus: This is a post-revision re-dream. Key changes since Dream #3: (1) paper_framing.md rewritten with no-pivot narrative, scope pruning (Bayesian DIF/RL/ensemble/pilots → appendix), explicit 3-layer novelty articulation, \"instability ≠ invalidity\" framing upfront; (2) 6 new robustness analyses with real data: threshold sensitivity (49/31/18/10%), BH FDR (negligible), instability decomposition (≤2.4pp/7.6%), circularity ablation (DIF least disruptive non-random), architecture stratification (99.98% decoder-only, concern dissolved), bootstrap CIs (all exclude zero); (3) literature expanded 15→45 papers across 5 clusters; (4) experiments.tex completed with Reviewer patches. Focus review on whether the structural/writing improvements address the prior round's concerns.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.\n\n10. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T04:47:48.431Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:47:48.431Z",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T04:47:48.453Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Discovery framing rejected as insufficient contribution; key robustness checks reveal structural weaknesses requiring reframing
核心假设：['SIBTEST reveals >15% items with substantial non-uniform DIF missed by MH — MH alone is demonstrably insufficient for this population, undermining 31% as a precise estimate', "Majority of reviewers (≥2/3) reject discovery-paper framing: 'applying a 1988 method to a new dataset is not an ICLR contribution'", 'GSM1K correlation collapses under difficulty control (partial r → [−0.15, +0.05], CI solidly includes zero) — sub-finding 4 is dead', "IRT misfit treated as invalidating: 'if 98% of models misfit, your ability estimates are meaningless, so MH conditioning on total score is the only defensible approach' — but then 31% reflects score-based rather than ability-based DIF", "At least 1 reviewer identifies the 31% baseline FPR problem as circular: 'you flag 31% as unstable, then show instability ≠ invalidity — but you never establish what the true instability rate should be'", "Semi-synthetic injection dismissed as too artificial: flipping incorrect→correct doesn't model real contamination mechanisms (memorization patterns, partial recall)"]
关键指标范围：{'nonuniform_dif_additional_pct': [15, 30], 'mh_sibtest_flag_jaccard': [0.4, 0.6], 'gsm1k_partial_r_lower_ci': [-0.35, 0.1], 'iclr_avg_overall_score': [3.5, 5.0], 'iclr_avg_novelty_score': [3.0, 4.5], 'iclr_avg_soundness_score': [4.0, 5.5], 'accept_probability': [0.03, 0.15]}
叙事方向：Reframe from "DIF reveals benchmark structural problems" to "Empirical characterization of measurement stability in LLM benchmarks: challenges and an open framework." Three pivots, same venue: (1) Lead with the semi-synthetic validation framework (Claim 3) as the primary methodological contribution — ΔTPR methodology + cross-subject matching (ΔFPR=0.000) is a genuinely novel, reusable tool. Elevate from supporting evidence to central contribution. (2) Reposition Claim 1 as a case study motivating the framework, not the headline finding. Report MH AND SIBTEST results jointly; present the discrepancy as "characterizing which DIF types matter for LLM benchmarks" rather than defending a single 31% number. The instability finding becomes "≥18-31% depending on DIF type and threshold" — a range, not a point estimate. (3) Drop GSM1K correlation entirely from the main paper. Strengthen the circularity ablation (plan_020) and redundancy finding (ρ≈0.997) as the downstream story — these are unaffected by non-uniform DIF concerns and don't depend on external correlation. Ground truth meta-critique (Claim 2) survives intact in all scenarios — make it more prominent. Add a "Practitioner's Guide" section: concrete recommendations for when/how to run DIF on new benchmarks, making the paper immediately useful regardless of MMLU-specific findings. Target remains ICLR 2027 — the framework + meta-critique + practitioner guide is a different but viable paper at the same venue.

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
  "promptId": "4f221751-fcc2-4413-931e-789c34e06b0c",
  "type": "user",
  "uuid": "3696748b-93ba-48ed-9221-3b610e61c44a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:47:48.451Z_

```json
{
  "parentUuid": "3696748b-93ba-48ed-9221-3b610e61c44a",
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
  "uuid": "56afcecd-4e27-4327-95d4-c9fda8927a04",
  "timestamp": "2026-05-21T04:47:48.451Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:47:48.451Z_

```json
{
  "parentUuid": "56afcecd-4e27-4327-95d4-c9fda8927a04",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a442dcc8-d145-45eb-a68f-6a0a3b512f95",
  "timestamp": "2026-05-21T04:47:48.451Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Discovery framing rejected as insufficient contribution; key robustness checks reveal structural weaknesses requiring reframing 核心假设：['SIBTEST reveals >15…",
  "leafUuid": "a442dcc8-d145-45eb-a68f-6a0a3b512f95",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe DIF study as measurement stability framework",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3"
}
```

---

### Assistant

_source line 8 · 2026-05-21T04:48:51.066Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "worst" tier scenario. Let me identify which experiments are still "planned" (not completed):

Looking at the experiment_plan statuses and registry:
- plan_001: status "planned" in experiment_plan, but registry shows "plan_001_real_data_dif_mmlu" as DONE
- plan_002: status "planned", not in registry → PLANNED


- plan_003a through plan_003c: all marked "planned" with no registry entries → PLANNED
- plan_004: status "planned" in experiment_plan, but registry shows "plan_004_gsm8k_cross_benchmark" as DONE
- plan_005: status "planned", registry shows "plan_015_bifactor_irt" as PREPARING/killed → PLANNED
- plan_006 through plan_010: all marked "planned" with no registry entries → PLANNED

Now I'm cross-referencing the paper_framing.md to see which experiments are actually documented as completed. Plan_010 appears in the paper as architecture-stratified analysis with specific results, and plans_011, 018, 019, and 020 are all listed in the registry as DONE or referenced as completed evidence in the paper, even though some aren't in the experiment_plan list itself. I need to figure out which "planned" experiments are actually still pending versus which ones have already been executed. the registry as DONE. The user likely wants me to predict results for the ones that are truly still planned, not yet completed. Let me filter through and identify which experiments from the plan are actually still pending — those not yet in the registry or marked as killed. I'm clarifying what the user is actually asking for — they want worst-case scenario predictions for all experiments listed in experiment_plan since they all have `status: planned`, regardless of whether some have already been executed with actual results in the registry.

Now I'm thinking through what constitutes a "worst" outcome based on the specific criteria: discovery framing gets rejected as insufficient, robustness checks expose fundamental weaknesses, and key assumptions fail like SIBTEST revealing substantial DIF that MH missed, reviewer rejection of the discovery framing, GSM1K correlations breaking down under difficulty control, and IRT misfit being treated as invalidating.

Looking at the metric ranges for this worst-case scenario, I'm setting nonuniform DIF detection at 15-30%, Jaccard similarity between MH and SIBTEST flags at 0.4-0.6, GSM1K partial correlations dropping to -0.35 to 0.1, and review scores ranging from 3.5-5.0 overall with lower novelty and soundness scores. The acceptance probability would be just 3-15%. The narrative would pivot toward framing this as an empirical characterization of measurement stability rather than a discovery of bias.

For the worst-case predictions, I'm mapping out how each experiment would fail. In plan_001 with real MMLU data, SIBTEST would catch substantial non-uniform DIF that MH misses—15-30% additional items—and the Jaccard overlap would be only 0.4-0.6, meaning the two methods flag completely different items. This would undermine the 31% estimate as method-dependent rather than robust. The within-family confound control would show high DIF driven by capability differences, not contamination, and domain-specificity would reveal DIF clustering in domains with known capability jumps. For plan_002 with RL robustness, the N=13 reasoning-RL models would be underpowered, and adding them to the cohort would shift DIF flags substantially, with traditional detectors showing instability. %, ConStat) actually don't degrade as much on RL models as hypothesized
- TOST equivalence testing fails — can't claim DIF is robust to RL
- Power analysis shows detection boundary is very high (p>0.7) for RL models

**plan_003a (constat_perturbation_eval)**:
In worst case:
- ConStat perturbation testing shows reasonable detection power on non-RL models
- Outperforms DIF in per-model detection
- Makes DIF look unnecessary for the contamination detection use case

**plan_003b (dvd_generation_variance_eval)**:
In worst case:
- DVD shows decent detection for variant contamination
- Combined with ConStat, covers most of what DIF covers
- DIF's group-level advantage is marginal

**plan_003c (ensemble_fusion)**:
In worst case:
- Ensemble fusion doesn't meaningfully improve over individual signals, with ConStat and DVD already capturing most of DIF's utility and false positive rates exceeding acceptable thresholds in some setups

**plan_004 (cross_benchmark_gsm8k)**:
In worst case:
- GSM8K correlation collapses when controlling for difficulty, with partial correlations ranging from -0.15 to +0.05 and confidence intervals crossing zero, effectively invalidating the finding that DIF items resist contamination and leaving N=33 too underpowered for reliable conclusions

**plan_005 (bifactor_irt_equating_pilot)**:
In worst case:
- Bifactor model either fails to converge or fits poorly, too many items get flagged to identify clean anchors, equated score equivalence falls below the 0.95 threshold, and the structural constraints make clean equating fundamentally unachievable with this data

**plan_006 (item_generation_calibration)**:
In worst case:
- Generated items fail to match target difficulty (ρ < 0.45), student simulation inflates correlations, items don't pass face validity review, and the calibration pipeline proves unreliable

**plan_007 (cumulative_bayesian_dif)**:
In worst case:
- Power gains fall short of projections (0.40 → 0.55 instead of 0.70), priors misalign with LLM population characteristics, and temporal dependence artifacts contaminate the cumulative approach

**plan_008 (graceful_degradation_analysis)**:
In worst case:
- Validity erodes faster than expected, ranking stability drops below 0.95 at 20% replacement, and the replacement mechanism introduces construct shift

**plan_009 (item_

focused_trees)**:
In worst case:
- Trees overfit to release date, detection power matches or underperforms categorical DIF, and the approach yields no additional insight beyond temporal cohort analysis

**plan_010 (architecture_stratified_dif)**:
In worst case:
- Architecture distribution is nearly uniform (99.98% decoder-only), removing the single non-decoder model changes nothing, IRT fit doesn't improve because multidimensionality is the real issue, and the experiment becomes a non-result that dissolves the concern without validating DIF

**plan_011 (semi_synthetic_contamination_validation)**:
In worst case:
- Semi-synthetic injection gets dismissed as too artificial, flipping incorrect→correct doesn't capture real contamination mechanisms, and the FPR inflation issue remains unresolved because the matching procedure itself has baseline problems that inflate ΔTPR

Now I'm structuring the YAML output with comprehensive predictions for each experiment, including specific metrics, rationales, and supporting analysis.

Writing YAML predictions...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a442dcc8-d145-45eb-a68f-6a0a3b512f95",
  "isSidechain": false,
  "requestId": "req_011CbF7FHeVkWPTYEWtZYm8E",
  "type": "assistant",
  "uuid": "d95984aa-e811-47d3-9ba6-ab84aaeaef8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbRFiVauE3abWgvXxv4Bpk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18438,
      "cache_read_input_tokens": 11841,
      "output_tokens": 19484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 19484,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18438
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

_source line 9 · 2026-05-21T04:54:28.014Z_

```yaml
tier: worst
narrative_guidance: >
  Reframe from "DIF reveals benchmark structural problems" to "Empirical characterization
  of measurement stability in LLM benchmarks: challenges and an open framework."
  Three pivots, same venue: (1) Lead with semi-synthetic validation framework (Claim 3)
  as primary methodological contribution — ΔTPR methodology + cross-subject matching
  (ΔFPR=0.000) is genuinely novel, reusable. (2) Reposition Claim 1 as case study
  motivating the framework, not headline finding. Report MH AND SIBTEST jointly;
  present discrepancy as "characterizing which DIF types matter" rather than defending
  a single 31% number. Instability becomes "≥18-31% depending on DIF type and threshold"
  — a range, not a point estimate. (3) Drop GSM1K correlation entirely from main paper.
  Strengthen circularity ablation and redundancy finding (ρ≈0.997). Ground truth
  meta-critique survives intact — make it more prominent. Add "Practitioner's Guide"
  section. Target remains ICLR 2027.

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      MH-DIF on METABENCH MMLU (5,219 models × 12,508 items). Temporal, ability,
      within-family cohorts. Proxy validation against Li et al. labels. Domain-specificity
      analysis. SIBTEST robustness check added as worst-case critical experiment.
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
      sibtest_nonuniform_additional_pct: 22.4
      mh_sibtest_flag_jaccard: 0.48
      sibtest_total_flagged_pct: 44.7
      sibtest_only_flags_pct: 13.4
      mh_only_flags_pct: 8.9
      sibtest_crossing_dif_items: 1674
    result_rationale: >
      MH结果本身不变（已有实际数据），但SIBTEST揭示了致命弱点：22.4%的items存在MH完全
      遗漏的非均匀DIF（non-uniform/crossing DIF），即不同能力水平的模型在这些items上
      表现出相反方向的DIF效应。MH只检测均匀位移，当DIF效应在能力谱上方向翻转时，正负
      抵消导致Δ_MH≈0，这些items被MH判为clean。Jaccard=0.48说明两种方法标记的items重叠
      不到一半——31%这个数字高度依赖于方法选择。1,674个crossing DIF items意味着MMLU中
      存在大量"对弱模型变难但对强模型变易"（或反过来）的items，这种模式与contamination
      的差异化机制高度一致（强模型更可能通过训练数据暴露获益），但MH的均匀性假设恰好
      将其mask掉。这直接动摇了"31%作为精确估计"的可信度——真实instability可能在18%到
      45%之间，取决于使用哪种DIF方法和哪个阈值。within-family分析中Llama-2 vs Llama-3
      的61.3% C%进一步证实大量DIF反映的是capability gain而非contamination。
    tables:
      - name: "MH vs SIBTEST Flag Comparison (Temporal Cohort)"
        columns: ["Method", "C_items", "C_pct", "Unique_flags", "Unique_pct"]
        rows:
          - ["MH (|Δ_MH|≥1.5)", 3918, 31.3, 1112, 8.9]
          - ["SIBTEST (β̂≥0.088)", 5592, 44.7, 1674, 13.4]
          - ["Intersection", 2806, 22.4, "—", "—"]
          - ["Union", 6584, 52.7, "—", "—"]
      - name: "SIBTEST Non-uniform DIF by Subject Cluster"
        columns: ["Subject_Cluster", "N_items", "Crossing_DIF_pct", "MH_missed_pct"]
        rows:
          - ["STEM_quantitative", 2841, 28.3, 18.7]
          - ["STEM_conceptual", 1953, 19.1, 11.2]
          - ["Humanities", 3287, 24.6, 14.8]
          - ["Social_sciences", 2614, 21.0, 12.1]
          - ["Professional", 1813, 17.4, 9.6]
    figures_description:
      - "Fig 1: Scatter plot of MH Δ_MH vs SIBTEST β̂ for all 12,508 items. Four quadrants: MH+/SIBTEST+ (overlap), MH+/SIBTEST- (MH-only), MH-/SIBTEST+ (SIBTEST-only, i.e. crossing DIF), MH-/SIBTEST- (clean). Large cloud of 1,674 items in MH-/SIBTEST+ quadrant demonstrates substantial crossing DIF invisible to MH. Color-coded by subject cluster."
      - "Fig 2: Item characteristic curves for 6 exemplar crossing-DIF items showing DIF direction reversal at mid-ability range. Reference (2023) and focal (2024-H1) curves cross, producing near-zero Δ_MH but large SIBTEST β̂. These items literally changed meaning across cohorts — easy items became hard for weak models but easier for strong models."
    analysis: >
      SIBTEST结果对paper是结构性打击。31%不再是一个可靠的点估计——它是MH特异性的产物。
      真实instability范围是18-45%（取决于方法和阈值），这使得任何基于31%的下游推断都变得
      模糊。对于worst tier reframe：(1)将MH和SIBTEST结果并列报告，承认"instability范围
      ≥18-31%依赖于DIF类型和阈值"而非捍卫单一数字；(2)crossing DIF的发现本身是有价值的
      empirical contribution——"MMLU items不仅在难度上漂移，还在区分功能上发生方向性变化"；
      (3)这motivates更复杂的DIF方法（logistic regression DIF, MIMIC）作为future work。
      但reviewer会说"如果你自己的robustness check否定了headline number，为什么我们应该
      相信这篇paper的任何具体数字？"

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      验证DIF对RL训练的鲁棒性。SFT基线、alignment-RL (DPO/ORPO, N=477)、
      reasoning-RL (GRPO/PPO, 10-15 models)。群体级DIF稳定性+个体级传统检测器对比。
    expected_results:
      n_reasoning_rl_models: 13
      n_sft_baseline: 312
      n_alignment_rl: 477
      dif_flag_jaccard_sft_vs_alignrl: 0.71
      dif_flag_jaccard_sft_vs_reasonrl_mixed: 0.58
      dif_flag_jaccard_alignrl_vs_reasonrl_mixed: 0.62
      auroc_dif_sft: 0.82
      auroc_dif_alignrl: 0.79
      auroc_dif_reasonrl_mixed: 0.64
      auroc_constat_sft: 0.74
      auroc_constat_alignrl: 0.68
      auroc_constat_reasonrl: 0.52
      auroc_mink_sft: 0.71
      auroc_mink_alignrl: 0.63
      auroc_mink_reasonrl: 0.41
      delong_dif_vs_constat_sft_p: 0.12
      delong_dif_vs_constat_reasonrl_p: 0.08
      tost_equivalence_dif_sft_alignrl_p: 0.03
      tost_equivalence_dif_sft_reasonrl_p: 0.31
      detection_boundary_exploitation_rate: 0.65
      bootstrap_ci_auroc_dif_reasonrl: [0.41, 0.84]
      power_at_p04: 0.18
      power_at_p07: 0.51
      power_at_p10: 0.64
    result_rationale: >
      N=13 reasoning-RL模型是致命瓶颈。当13个GRPO/PPO模型混入focal cohort时，cohort
      总N仍≥80（满足DIF统计要求），但这些模型的contamination-masking效应使得DIF flag
      集合发生实质性漂移（Jaccard从0.71降至0.58）。关键问题：AUROC在reasoning-RL条件下
      降至0.64，bootstrap CI极宽[0.41, 0.84]——无法排除DIF在RL场景下接近random的可能。
      TOST等价检验失败（p=0.31>>0.05），无法声称DIF对reasoning-RL是等价的。传统检测器
      确实退化更多（ConStat 0.74→0.52, Min-K% 0.71→0.41），但DIF的退化也不小
      （0.82→0.64），且DeLong检验p=0.08——差异不显著。这意味着"DIF对RL鲁棒"的声明
      在统计上站不住脚。power analysis显示detection boundary在p≈0.65——只有>65%
      exploitation rate的contamination才能被检测到，这在实际中覆盖面有限。
      整体结论：DIF比传统方法更robust是趋势性的，但N=13使得任何定量声明都不可信。
    tables:
      - name: "Detection Performance by Cohort Composition"
        columns: ["Detector", "SFT_AUROC", "AlignRL_AUROC", "ReasonRL_AUROC", "Δ_SFT→ReasonRL"]
        rows:
          - ["DIF (MH)", 0.82, 0.79, 0.64, -0.18]
          - ["ConStat", 0.74, 0.68, 0.52, -0.22]
          - ["Min-K%", 0.71, 0.63, 0.41, -0.30]
      - name: "DIF Flag Stability Across Cohort Compositions"
        columns: ["Comparison", "Jaccard", "New_flags", "Lost_flags"]
        rows:
          - ["SFT vs AlignRL", 0.71, 412, 287]
          - ["SFT vs SFT+ReasonRL", 0.58, 893, 614]
          - ["AlignRL vs AlignRL+ReasonRL", 0.62, 731, 508]
      - name: "TOST Equivalence Tests (Δ AUROC ≤ 0.10)"
        columns: ["Comparison", "Δ_AUROC", "TOST_p", "Equivalent"]
        rows:
          - ["DIF: SFT vs AlignRL", 0.03, 0.03, "Yes"]
          - ["DIF: SFT vs ReasonRL", 0.18, 0.31, "No"]
          - ["ConStat: SFT vs ReasonRL", 0.22, 0.44, "No"]
    figures_description:
      - "Fig: Detection power (TPR at FPR=0.10) as function of exploitation rate p∈[0.3,1.0] for three cohort compositions. SFT curve reaches TPR=0.68 at p=0.5; ReasonRL-mixed curve only reaches TPR=0.51 at p=0.7. Shaded bootstrap 95% CIs show massive uncertainty for ReasonRL curve due to N=13."
    analysis: >
      实验的根本问题是sample size。N=13 reasoning-RL模型不足以支撑任何统计推断——
      这不是"underpowered"可以轻描淡写的，而是使结论完全不可信。worst tier下reviewer
      会直接说"你声称DIF对RL robust但你只有13个RL模型，CI覆盖从random到excellent，
      这不是evidence而是noise"。对于reframe：将RL robustness完全降级到limitations/
      future work，不在main claims中出现。承认"RL robustness是open question，现有
      METABENCH中reasoning-RL模型不足以验证"。这反而增强了paper的诚实度。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      ConStat-style perturbation testing独立评估。200+ MMLU items语义等价改写，
      FDR-controlled detection，与DIF对比。
    expected_results:
      n_items_reformulated: 237
      n_models_tested: 48
      constat_detection_rate_non_rl: 0.34
      constat_detection_rate_rl: 0.11
      constat_fdr_controlled_rate: 0.28
      constat_fpr: 0.067
      constat_auroc_non_rl: 0.78
      constat_auroc_rl: 0.54
      dif_auroc_same_items: 0.73
      dif_constat_overlap_flagged: 0.31
      paraphrase_quality_human_eval: 0.82
      paraphrase_semantic_sim: 0.91
      effect_size_non_rl_mean_d: 0.87
      effect_size_rl_mean_d: 0.34
    result_rationale: >
      ConStat在per-model detection上展现出DIF不具备的粒度优势：它可以指出具体哪个模型
      在哪些items上表现异常（FPR=0.067远低于DIF的temporal baseline 0.31）。在non-RL
      模型上AUROC=0.78略高于DIF的0.73（同一items子集），这使得reviewer有理由质疑
      "为什么不直接用ConStat而要用这个baseline FPR=31%的老方法？"。RL条件下ConStat
      确实退化严重（0.78→0.54），但DIF在worst tier下也退化（plan_002: 0.82→0.64），
      差异不如expected那么戏剧性。关键攻击点：ConStat的FPR（0.067）比DIF temporal的
      FPR（0.31）低一个数量级——reviewer会问"你的方法31%的items被flagged作为baseline，
      另一个方法只有6.7% false positive，哪个更可信？"。overlap仅0.31说明两种方法
      检测的是根本不同的信号——这在worst tier下被解读为"DIF检测的不是contamination
      而是别的什么东西"。
    tables:
      - name: "ConStat vs DIF Detection Comparison"
        columns: ["Metric", "ConStat", "DIF (MH)", "Advantage"]
        rows:
          - ["AUROC (non-RL)", 0.78, 0.73, "ConStat +0.05"]
          - ["AUROC (RL)", 0.54, 0.64, "DIF +0.10"]
          - ["FPR", 0.067, 0.314, "ConStat ×4.7 better"]
          - ["Per-model granularity", "Yes", "No", "ConStat"]
          - ["Flag overlap (Jaccard)", "—", "—", 0.31]
    figures_description:
      - "Fig: ROC curves for ConStat and DIF on the 237 reformulated items, split by RL/non-RL model subgroups. ConStat curve dominates DIF in low-FPR regime for non-RL models; DIF has slight advantage in high-recall regime for RL models."
    analysis: >
      ConStat结果对DIF-as-contamination-detector叙事构成直接竞争。在non-RL场景下ConStat
      更精确（低FPR）且粒度更细（per-model），这使得DIF在contamination detection赛道上
      处于劣势。但这实际上支持了worst tier的reframe方向：DIF不应该定位为contamination
      detector，而是benchmark stability characterization工具——两者检测的是不同信号
      （ConStat检测specific model anomaly，DIF检测cross-cohort item property shift）。
      Reframe后ConStat变成complementary baseline而非competing method。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      DVD generation variance独立评估。10-15个open-weight模型，50 responses/item，
      generation variance scores，bimodal distribution检测。
    expected_results:
      n_models_tested: 12
      n_items_tested: 500
      responses_per_item: 50
      dvd_auroc_verbatim: 0.69
      dvd_auroc_variant: 0.58
      dvd_fpr: 0.089
      dvd_bimodal_detection_rate: 0.23
      dvd_effect_size_verbatim_d: 0.74
      dvd_effect_size_variant_d: 0.41
      dvd_dif_overlap_flagged: 0.19
      gpu_hours_used: 63
      temperature_sensitivity_t07_auroc: 0.69
      temperature_sensitivity_t10_auroc: 0.62
    result_rationale: >
      DVD的per-model generation variance检测在verbatim contamination上表现中等
      （AUROC=0.69），variant contamination上较弱（0.58）。与DIF的flag overlap极低
      （0.19），再次表明不同方法检测不同类型的信号。DVD的核心假设——contaminated items
      产生bimodal response分布——在实际LLM上只有23%的known-contaminated items表现出
      明显bimodality，这是因为现代LLM在temperature=0.7时already highly consistent，
      contamination造成的额外consistency增量很小。GPU cost=63hrs使其成为expensive的
      detection method（DIF是zero GPU cost）。在worst tier下，DVD结果是"another
      incomplete signal"——既不强到取代DIF，也不弱到让DIF显得indispensable，陷入
      "所有方法都partially work"的尴尬叙事。
    tables:
      - name: "DVD Detection by Contamination Type"
        columns: ["Contamination_Type", "N_items", "AUROC", "Bimodal_pct", "Effect_d"]
        rows:
          - ["Verbatim", 127, 0.69, 31.5, 0.74]
          - ["Variant", 89, 0.58, 12.4, 0.41]
          - ["Clean", 284, "—", 4.2, "—"]
      - name: "DVD vs DIF Signal Comparison"
        columns: ["Metric", "DVD", "DIF", "Overlap_Jaccard"]
        rows:
          - ["Items flagged", 94, 157, 0.19]
          - ["FPR", 0.089, 0.314, "—"]
          - ["Detection granularity", "per-model", "per-cohort", "—"]
    figures_description:
      - "Fig: Violin plots of generation variance scores for clean vs verbatim-contaminated vs variant-contaminated items across 12 models. Distributions heavily overlap for variant contamination, showing DVD's limited discriminative power for non-verbatim contamination."
    analysis: >
      DVD结果确认了generation variance作为contamination signal的局限性——在variant
      contamination（更现实的场景）上几乎失效。但这不直接伤害DIF叙事，因为DVD和DIF
      检测的是完全不同的信号（Jaccard=0.19）。在worst tier reframe中，DVD结果变成
      "motivating example for why single-signal detection is insufficient"——但由于
      ensemble（plan_003c）也不work well，这个motivating example没有resolution。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      DIF + ConStat + DVD三信号融合。阈值校准，majority voting，weighted fusion，
      5-fold cross-validation。
    expected_results:
      ensemble_2of3_auroc: 0.72
      ensemble_weighted_auroc: 0.76
      ensemble_fpr: 0.112
      best_single_signal_auroc: 0.78
      ensemble_vs_best_single_delong_p: 0.38
      ensemble_coverage_high_delta: 0.81
      ensemble_coverage_low_delta: 0.43
      ensemble_coverage_rl: 0.48
      cv_fold_variance_auroc: 0.034
      uniform_weight_auroc: 0.71
      optimized_weight_dif: 0.28
      optimized_weight_constat: 0.47
      optimized_weight_dvd: 0.25
      fpr_above_010_configs: 3
      total_configs_tested: 8
    result_rationale: >
      Ensemble的核心承诺是"coverage handoff"——DIF覆盖high-delta，ConStat覆盖non-RL
      medium-delta，DVD覆盖variant。但实际融合结果令人失望：weighted AUROC=0.76低于
      ConStat单独的0.78，DeLong p=0.38表明ensemble没有统计显著地超越最佳单信号。
      这是因为三个信号的correlation structure不利于融合：DIF和ConStat在某些items上
      产生contradictory signals（DIF flag但ConStat clean，或反过来），majority voting
      在这种情况下倾向于conservative（2-of-3需要agreement），而weighted fusion的
      DIF权重被压低到0.28（反映其高baseline FPR降低了fusion中的信息价值）。
      FPR=0.112超过了0.10目标阈值（3/8 configurations）。CV fold variance=0.034
      说明权重unstable。在worst tier下，ensemble failure是"the punchline that never
      lands"——paper承诺了complementary detection但deliver的是noise averaging。
      Reviewer会说"如果ensemble不比单方法好，为什么这是一个contribution？"
    tables:
      - name: "Ensemble vs Individual Signal Performance"
        columns: ["Method", "AUROC", "FPR", "Coverage_δ≥1.4", "Coverage_δ<1.0"]
        rows:
          - ["DIF alone", 0.73, 0.314, 0.79, 0.22]
          - ["ConStat alone", 0.78, 0.067, 0.61, 0.48]
          - ["DVD alone", 0.69, 0.089, 0.54, 0.37]
          - ["Ensemble (2-of-3)", 0.72, 0.048, 0.52, 0.31]
          - ["Ensemble (weighted)", 0.76, 0.112, 0.81, 0.43]
      - name: "Cross-Validation Stability"
        columns: ["Fold", "AUROC", "w_DIF", "w_ConStat", "w_DVD"]
        rows:
          - [1, 0.79, 0.31, 0.44, 0.25]
          - [2, 0.74, 0.22, 0.52, 0.26]
          - [3, 0.78, 0.35, 0.41, 0.24]
          - [4, 0.72, 0.19, 0.53, 0.28]
          - [5, 0.77, 0.33, 0.45, 0.22]
    figures_description:
      - "Fig: Coverage heatmap showing which contamination types (verbatim/variant × RL/non-RL × effect size bins) are detected by each signal and their combinations. Large gap in variant+RL quadrant where no method exceeds AUROC=0.50."
    analysis: >
      Ensemble failure在worst tier叙事中有两种解读：(1)消极——DIF不是一个有价值的
      ensemble component，整个multi-signal方向是dead end；(2)积极（reframe后）——
      这说明contamination detection fundamentally不能通过简单signal combination解决，
      需要新方法论。但后者是一个non-result dressed up as insight，reviewer不会buy。
      对于reframe：将ensemble完全移到appendix/future work，main paper不再声称
      detection improvement，而是聚焦于characterization和framework贡献。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      GSM8K DIF复制 + GSM1K ground truth验证。Temporal DIF on 1,319 items × 6,702
      models。Semi-synthetic validation。GSM1K correlation with difficulty control。
    expected_results:
      step1_gsm8k_temporal_dif:
        n_items: 1319
        n_ref: 1017
        n_foc: 804
        standard_c_pct: 18.9
        external_c_pct: 47.4
        sanity_c_pct: 0.3
      step2_semi_synthetic:
        standard_delta_tpr_p10: 0.818
        external_delta_tpr_p10: 0.517
      step3_gsm1k_correlation:
        n_models: 33
        pearson_r: -0.478
        pearson_p: 0.005
        spearman_rho: -0.403
        spearman_p: 0.020
        partial_r_controlling_accuracy: -0.385
        partial_p: 0.027
        partial_r_controlling_difficulty: -0.08
        partial_p_difficulty: 0.67
        partial_r_controlling_accuracy_and_difficulty: 0.03
        partial_p_acc_diff: 0.87
        difficulty_control_ci_lower: -0.31
        difficulty_control_ci_upper: 0.15
        permutation_p_difficulty_controlled: 0.64
        dif_item_mean_difficulty: 0.38
        non_dif_item_mean_difficulty: 0.61
        difficulty_dif_correlation: -0.52
    result_rationale: >
      Step 1和Step 2的结果不变（已有实际数据），关键崩塌发生在Step 3的difficulty control。
      原始r=-0.478看似strong，但DIF-C items系统性地更难（mean p-value=0.38 vs 0.61），
      difficulty与DIF-C flag的correlation=-0.52。当控制item difficulty后，partial
      r从-0.385骤降至-0.08（p=0.67），CI=[-0.31, 0.15]稳固包含零。同时控制accuracy
      和difficulty后，r→0.03（essentially zero）。这意味着原始correlation完全由
      confound驱动：DIF flags harder items → harder items have larger contamination
      gaps (floor effect) → spurious negative correlation。这不是DIF-C items "resist
      contamination" 而是 "DIF-C items are harder, and harder items have smaller
      accuracy differences between GSM8K and GSM1K regardless of contamination"。
      N=33的小样本加剧了问题——控制一个confound就吃掉所有degrees of freedom。
      Sub-finding 4（DIF items resist contamination-based gains）在difficulty
      control下彻底死亡。
    tables:
      - name: "GSM1K Correlation Under Progressive Controls"
        columns: ["Model", "r", "p", "95% CI", "Interpretation"]
        rows:
          - ["Bivariate", -0.478, 0.005, "[-0.71, -0.16]", "Significant"]
          - ["Partial (acc)", -0.385, 0.027, "[-0.64, -0.06]", "Significant"]
          - ["Partial (difficulty)", -0.08, 0.67, "[-0.31, 0.15]", "Non-significant"]
          - ["Partial (acc+difficulty)", 0.03, 0.87, "[-0.22, 0.28]", "Null"]
      - name: "DIF-C vs Non-DIF Item Difficulty"
        columns: ["Item_Group", "N", "Mean_p_value", "SD", "Mean_discrimination"]
        rows:
          - ["DIF-C", 249, 0.38, 0.21, 0.42]
          - ["Non-DIF", 1070, 0.61, 0.24, 0.39]
          - ["t-test p", "—", "<0.001", "—", 0.34]
    figures_description:
      - "Fig: Two panels. Left: scatter of contamination gap vs DIF-C proportion, raw (r=-0.478, significant). Right: same scatter after residualizing both variables on item difficulty — correlation vanishes (r=0.03). Illustrates that difficulty is the confound driving the entire correlation."
    analysis: >
      GSM1K correlation collapse是worst tier的defining feature之一。Sub-finding 4
      从paper的main body中完全删除。ρ≈0.997 redundancy和circularity ablation（z=-9.5）
      不受影响（它们不依赖GSM1K）。Reframe后Claim 4缩减为三个sub-finding：(1)redundancy，
      (2)DIF≠high-discrimination（circularity ablation），(3)diagnostic lens（model-specific
      patterns）。GSM8K的Step 1和Step 2仍然有用——framework portability demonstration
      survives，只是downstream validation不work了。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      Bifactor IRT equating pilot on MMLU。General factor + 57 subject-specific
      factors。Anchor item selection。Fixed-parameter calibration。Score equivalence
      validation (target ρ≥0.95)。
    expected_results:
      model_convergence: partial
      n_iterations_to_convergence: 8500
      convergence_criterion_met: false
      rmsea: 0.047
      cfi: 0.72
      tli: 0.69
      srmr: 0.081
      general_factor_variance_explained: 0.31
      specific_factor_avg_variance: 0.18
      residual_variance: 0.51
      n_anchor_items_identified: 847
      anchor_item_stability_criterion: 0.80
      n_items_meeting_stability: 412
      equated_rho_full_vs_replaced_10pct: 0.91
      equated_rho_full_vs_replaced_20pct: 0.86
      equated_rho_full_vs_replaced_31pct: 0.79
      score_equivalence_bias_mean: 0.34
      score_equivalence_bias_max: 2.17
    result_rationale: >
      Bifactor模型在5,219×12,508矩阵上面临计算和统计双重困难。模型未完全收敛（8,500
      iterations仍未满足criterion），CFI=0.72和TLI=0.69远低于acceptable fit标准（>0.90）。
      这并非意外——MMLU的57 subjects构成的multidimensional structure过于复杂，bifactor
      是一个over-simplification（假设1个general factor + 57 orthogonal specific factors，
      但实际上subjects之间存在大量cross-loading）。General factor仅解释31%方差，说明
      MMLU的"general intelligence"维度很弱。残差方差51%意味着模型miss了一半的信号。
      
      Anchor item selection结果更差：按stability criterion(across-cohort Δ_MH<0.5)
      筛选出847个候选anchor items，但只有412个满足更严格的equating stability要求。
      用这412个anchor做fixed-parameter calibration后，替换10%的items时ρ=0.91（<0.95
      target），替换31%时ρ=0.79——远低于目标。Score equivalence bias高达2.17，
      意味着某些模型的equated score偏移>2个标准误。
      
      根本原因：IRT equating假设latent trait是well-measured的，但MMLU上1D IRT
      fundamentally misspecified（98% models |Lz|>2），bifactor虽然better但仍然
      inadequate。Without good person parameter estimates, equating is garbage-in-
      garbage-out。
    tables:
      - name: "Bifactor Model Fit Indices"
        columns: ["Index", "Value", "Acceptable", "Good", "Status"]
        rows:
          - ["RMSEA", 0.047, "<0.08", "<0.05", "Borderline"]
          - ["CFI", 0.72, ">0.90", ">0.95", "FAIL"]
          - ["TLI", 0.69, ">0.90", ">0.95", "FAIL"]
          - ["SRMR", 0.081, "<0.08", "<0.05", "FAIL"]
      - name: "Score Equivalence After Item Replacement"
        columns: ["Replacement_pct", "Spearman_ρ", "Mean_bias", "Max_bias", "Target_met"]
        rows:
          - ["5%", 0.94, 0.12, 0.87, "No (ρ<0.95)"]
          - ["10%", 0.91, 0.34, 1.41, "No"]
          - ["20%", 0.86, 0.67, 1.89, "No"]
          - ["31%", 0.79, 1.12, 2.17, "No"]
    figures_description:
      - "Fig: Bifactor path diagram showing general factor loadings (weak, avg=0.31) and subject-specific loadings. Residual variance dominates, indicating poor model specification."
      - "Fig: Score equivalence scatter plot at 31% replacement. Clear systematic bias for mid-ability models — equating over-credits some model families and under-credits others."
    analysis: >
      Bifactor pilot的失败confirmed paper_framing.md中已经预期的结论："IRT是fundamentally
      misspecified for MMLU"。这在worst tier下被reviewer weaponize："如果你承认IRT
      misspecified，那MH conditioning on total score是唯一defensible approach——
      但then 31% reflects score-based rather than ability-based DIF，你没有evidence
      这是'真正的'item functioning差异而不是score distribution artifact"。
      Equating pilot失败意味着Claim 3（regeneration）完全dead。对于reframe：将equating
      从claims中完全移除，bifactor结果变成limitations section的evidence——"future work
      需要multidimensional IRT才能实现equating"。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      LLM生成替换items + student simulation校准。Construct constraints, difficulty
      estimation, holdout validation。
    expected_results:
      n_items_generated: 500
      n_items_passing_face_validity: 312
      face_validity_pass_rate: 0.624
      difficulty_correlation_prompt_based: 0.31
      difficulty_correlation_student_sim: 0.52
      difficulty_correlation_target: 0.75
      subject_coverage_pct: 89
      cognitive_level_match_pct: 67
      holdout_panel_rho: 0.48
      discrimination_match_r: 0.29
      construct_drift_detected_pct: 18.4
      gpu_hours_used: 178
    result_rationale: >
      Item generation面临两个层面的困难。First, face validity：只有62.4%的generated
      items通过human evaluation（incorrect distractors太obvious，或者stem在语义上
      偏移了原item的construct）。Second, calibration：student simulation的difficulty
      estimation（ρ=0.52）远低于arXiv 2601.09953报告的0.75-0.82，这是因为MMLU items
      的difficulty主要由knowledge specificity驱动（而非reasoning complexity），而LLM
      student simulation更擅长估计reasoning difficulty。Discrimination match更差
      （r=0.29）——generated items的区分度系统性偏低，因为LLM倾向于生成"textbook-style"
      的clean items而非real exam的nuanced items。
      
      18.4%的construct drift意味着近五分之一的生成items实际上测量的是不同的construct——
      比如原item测试"specific legal precedent knowledge"但generated item测试
      "general legal reasoning"。这在holdout panel上表现为ρ=0.48——生成的benchmark
      与原始benchmark的model ranking correlation很弱。
      
      Combined with plan_005的equating failure，整个regeneration pipeline（Claim 3原版）
      在worst tier下是完全不可行的。
    tables:
      - name: "Item Generation Quality Metrics"
        columns: ["Metric", "Value", "Target", "Status"]
        rows:
          - ["Face validity pass rate", 0.624, ">0.80", "FAIL"]
          - ["Difficulty ρ (prompt-based)", 0.31, "0.45+", "FAIL"]
          - ["Difficulty ρ (student sim)", 0.52, "0.75+", "FAIL"]
          - ["Discrimination match r", 0.29, ">0.60", "FAIL"]
          - ["Construct drift", "18.4%", "<5%", "FAIL"]
          - ["Holdout ranking ρ", 0.48, "≥0.95", "FAIL"]
    figures_description:
      - "Fig: Difficulty calibration scatter — generated item difficulty (student sim estimated) vs actual difficulty on holdout model panel. Wide scatter (ρ=0.52) with systematic under-estimation of hard items."
    analysis: >
      Item generation失败在worst tier reframe中不造成额外伤害——regeneration（Claim 3
      原版）已经在Dream #3中被pruned to appendix。但这个negative result本身有publication
      value作为"cautionary tale about LLM-based item generation for high-stakes
      benchmarks"——如果space permits可以在Discussion中brief mention。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      Cumulative Bayesian DIF priors (Sinharay et al., 2006)。4轮successive
      administrations模拟。Power improvement from evidence accumulation。
    expected_results:
      individual_admin_power_delta10: 0.41
      cumulative_2admin_power_delta10: 0.52
      cumulative_3admin_power_delta10: 0.58
      cumulative_4admin_power_delta10: 0.63
      target_cumulative_3admin_power: 0.70
      target_met: false
      prior_calibration_error_mean: 0.23
      prior_calibration_error_max: 0.67
      fpr_inflation_cumulative_4admin: 0.074
      bayesian_mh_correlation_flags: 0.81
      bayes_factor_median: 3.2
      bayes_factor_gt10_pct: 18.4
      simulation_n_per_admin: 200
      n_items_simulated: 1000
      n_administrations: 4
    result_rationale: >
      Cumulative Bayesian方法的power improvement低于理论预期：3-admin cumulative
      power=0.58（vs target 0.70），4-admin才达到0.63。差距来自prior miscalibration：
      Sinharay et al.的priors是为human testing设计的（student populations with
      stable demographics），LLM "administrations"的cohort composition变化更剧烈
      （每轮新模型的ability distribution shift更大），导致informative priors反而
      引入bias。Prior calibration error mean=0.23意味着prior对DIF effect size的
      预期系统性偏离了actual，累积后bias不是减少而是compound。
      
      Bayes factors偏弱（median=3.2，只有18.4%的items BF>10），说明evidence
      accumulation受限于LLM cohort间的non-stationarity。FPR inflation到0.074
      在4-admin后是manageable但concerning——累积更多administrations可能会worse。
      
      与MH flags的correlation=0.81说明Bayesian方法在很大程度上agree with MH，
      增量贡献有限——essentially adding computational complexity for modest gain。
    tables:
      - name: "Cumulative Power by Administration"
        columns: ["N_admins", "Power_δ=0.8", "Power_δ=1.0", "Power_δ=1.4", "FPR"]
        rows:
          - [1, 0.22, 0.41, 0.68, 0.042]
          - [2, 0.31, 0.52, 0.76, 0.051]
          - [3, 0.37, 0.58, 0.81, 0.063]
          - [4, 0.42, 0.63, 0.84, 0.074]
      - name: "Prior Calibration Analysis"
        columns: ["Admin_pair", "Prior_mean_error", "Prior_var_error", "BF_median"]
        rows:
          - ["1→2", 0.14, 0.08, 4.1]
          - ["2→3", 0.21, 0.13, 3.4]
          - ["3→4", 0.34, 0.19, 2.7]
    figures_description:
      - "Fig: Power curves showing cumulative improvement across 4 administrations at δ=1.0. Actual curve (solid) systematically below theoretical curve (dashed) due to prior miscalibration. Gap widens with more administrations."
    analysis: >
      Bayesian cumulative DIF在worst tier下确认了paper_framing.md的decision to
      move it to appendix。Power improvement不足以justify complexity increase。
      Prior miscalibration问题是fundamental——LLM benchmark "administrations"
      不满足Bayesian updating的stationarity assumption。在reframe后，这变成
      appendix material："simulation study showing theoretical potential with
      caveats about non-stationary populations"。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      Benchmark validity under progressive item replacement。Ranking stability,
      score reliability, construct coverage at 5/10/20/50% replacement。
      Theoretical bounds + empirical validation on METABENCH。
    expected_results:
      rho_5pct_replacement: 0.993
      rho_10pct_replacement: 0.984
      rho_20pct_replacement: 0.961
      rho_50pct_replacement: 0.887
      reliability_original_kr20: 0.967
      reliability_5pct: 0.964
      reliability_10pct: 0.958
      reliability_20pct: 0.943
      reliability_50pct: 0.891
      construct_coverage_original: 1.0
      construct_coverage_5pct: 0.98
      construct_coverage_10pct: 0.95
      construct_coverage_20pct: 0.87
      construct_coverage_50pct: 0.71
      theoretical_lower_bound_rho_at_31pct: 0.92
      empirical_rho_at_31pct: 0.94
      critical_replacement_threshold: 0.23
      validity_degradation_rate: nonlinear
    result_rationale: >
      Graceful degradation分析本身产生reasonable results——rankings在20%替换时
      仍robust（ρ=0.961），但construct coverage更fragile（0.87 at 20%）。关键
      问题在worst tier context中：这个分析假设replacement items是well-calibrated的，
      但plan_005（equating failure）和plan_006（generation failure）已经证明
      实际的replacement items质量远低于预期。所以degradation curves是optimistic
      lower bound——实际degradation会worse。
      
      Critical replacement threshold=23%意味着替换>23%的items时validity开始
      non-linearly degrade。但我们的DIF flag rate是31%——超过了这个threshold。
      Reviewer会指出："你说31%的items unstable，但你也说替换>23%就会degrade
      validity——那你的解决方案（替换flagged items）本身就会destroy benchmark validity。
      这不是一个solution而是一个dilemma。"
      
      在worst tier reframe中这个dilemma变成feature而非bug："we characterize the
      replacement feasibility boundary"——但reviewer可能视其为研究without actionable
      outcome。
    tables:
      - name: "Validity Metrics Under Progressive Replacement"
        columns: ["Replace_pct", "Rank_ρ", "KR-20", "Coverage", "Max_rank_shift"]
        rows:
          - ["0% (original)", 1.000, 0.967, 1.00, 0]
          - ["5%", 0.993, 0.964, 0.98, 23]
          - ["10%", 0.984, 0.958, 0.95, 47]
          - ["20%", 0.961, 0.943, 0.87, 112]
          - ["31% (DIF rate)", 0.940, 0.927, 0.79, 189]
          - ["50%", 0.887, 0.891, 0.71, 341]
      - name: "Theoretical vs Empirical Degradation"
        columns: ["Replace_pct", "Theory_lower_ρ", "Empirical_ρ", "Gap"]
        rows:
          - ["10%", 0.978, 0.984, "+0.006"]
          - ["20%", 0.944, 0.961, "+0.017"]
          - ["31%", 0.920, 0.940, "+0.020"]
          - ["50%", 0.868, 0.887, "+0.019"]
    figures_description:
      - "Fig: Three-panel degradation curves (ranking ρ, KR-20, construct coverage) vs replacement percentage. Vertical dashed line at 31% (DIF rate) and 23% (critical threshold). Coverage curve drops steeply after 20%, while ranking ρ degrades more gracefully."
    analysis: >
      Graceful degradation在worst tier reframe中降级为supplementary analysis。
      核心insight（replacement threshold < DIF rate）在appendix中作为"the fundamental
      tension in DIF-based benchmark maintenance"讨论，但不作为main claim。ρ≈0.997
      的existing finding（plan_017, DIF removal without replacement）remains the
      stronger and simpler message for the main paper。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      Item-Focused Trees (Tutz & Berger 2016) as alternative to categorical cohort DIF。
      Release date as continuous covariate。Detection power comparison vs categorical DIF。
    expected_results:
      ift_items_flagged_pct: 27.4
      ift_mh_overlap_jaccard: 0.63
      ift_unique_flags_pct: 8.1
      mh_unique_flags_pct: 11.7
      ift_detection_power_delta14: 0.59
      mh_detection_power_delta14: 0.68
      ift_fpr: 0.088
      mh_fpr_temporal: 0.314
      ift_tree_depth_median: 3
      ift_tree_depth_max: 7
      ift_primary_split_variable: release_date
      ift_secondary_split: model_size
      overfitting_cv_auroc_gap: 0.12
      n_stable_splits: 4
      n_unstable_splits: 8
    result_rationale: >
      Item-Focused Trees在worst tier下产生mixed results。优点：FPR=0.088远低于
      MH temporal的0.314，因为trees不需要硬性cohort split——continuous release date
      允许更nuanced的grouping。缺点：detection power=0.59低于MH的0.68，因为trees
      将sample分割成更小的subgroups（每个leaf node N更小）。Jaccard=0.63的overlap
      说明两种方法largely agree但有meaningful disagreement。
      
      关键weakness：overfitting。CV AUROC gap=0.12说明trees在training上over-optimize。
      12个split中8个是unstable的（bootstrap resample后不reproduce）。这使得IFT
      results在robustness上不如MH（MH虽然crude但statistically principled）。
      
      Reviewer在worst tier下会指出："IFT有更好的FPR但更差的power和更差的stability——
      这不是一个improvement而是一个tradeoff，你没有demonstrate哪个tradeoff更
      appropriate for this application。"
      
      Primary split on release_date confirms temporal effect is real but secondary
      split on model_size introduces a confound MH doesn't have——larger models
      are more recent AND better, so tree conflates time and capability。
    tables:
      - name: "IFT vs MH-DIF Comparison"
        columns: ["Metric", "IFT", "MH (temporal)", "Advantage"]
        rows:
          - ["Items flagged %", 27.4, 31.3, "IFT (fewer)"]
          - ["FPR", 0.088, 0.314, "IFT ×3.6 better"]
          - ["TPR (δ≥1.4)", 0.59, 0.68, "MH +0.09"]
          - ["Overlap (Jaccard)", "—", "—", 0.63]
          - ["CV stability", 0.67, "N/A (parametric)", "MH"]
      - name: "IFT Split Stability (Bootstrap)"
        columns: ["Split_depth", "Variable", "Bootstrap_reproduce_pct", "Stable"]
        rows:
          - [1, "release_date", 98, "Yes"]
          - [2, "model_size", 72, "Yes"]
          - [3, "training_data_size", 61, "Borderline"]
          - [4, "subject_category", 34, "No"]
    figures_description:
      - "Fig: Example Item-Focused Tree for a representative MMLU subject. First split on release_date (2023-06), second on model_size. Deeper splits are unstable — dashed lines indicate bootstrap reproduction <50%."
    analysis: >
      IFT在worst tier reframe中有niche价值：它提供release_date作为continuous
      covariate的evidence，支持"temporal instability is real"的narrative。但
      overfitting和power loss使其不适合作为primary method。Appendix material。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      Architecture-homogeneous DIF。Decoder-only subset。IRT fit diagnostics。
      Compare FPR/TPR vs full-population DIF。
    expected_results:
      n_decoder_only: 5226
      n_non_decoder: 1
      pct_decoder_only: 99.98
      decoder_only_c_pct: 31.3
      full_population_c_pct: 31.3
      jaccard_decoder_vs_full: 1.000
      removed_model: RWKV-v5-Eagle-7B
      rmsea_decoder_only: 0.089
      rmsea_full: 0.089
      cfi_decoder_only: 0.41
      cfi_full: 0.41
      lz_pct_misfit_decoder_only: 97.8
      lz_pct_misfit_full: 98.1
      irt_fit_improvement: negligible
      temporal_fpr_decoder_only: 0.313
      temporal_tpr_p05_decoder_only: 0.834
    result_rationale: >
      METABENCH MMLU is 99.98% decoder-only（5226/5227），移除1个non-decoder模型
      对所有结果的影响为zero（Jaccard=1.000）。Architecture heterogeneity concern
      dissolved——但这是一个trivial result，不是一个victory。
      
      关键问题：IRT fit完全没有improve（RMSEA=0.089, CFI=0.41, 97.8% |Lz|>2）。
      这confirms MMLU的IRT misfit不是由architecture heterogeneity造成的——root cause
      是multidimensionality（57 subjects）。在worst tier下reviewer的攻击点是：
      "你证明了architecture不是问题，但IRT misfit仍然devastating。98%的模型misfit
      意味着你的ability estimates是meaningless的——MH conditioning on total score
      是唯一defensible approach，但total score在multidimensional test上不是ability
      的good proxy。So your 31% DIF reflects score-distribution artifacts, not
      genuine differential item functioning。"
      
      这是worst tier核心假设#4的manifestation。Defense只能是承认limitation并argue
      MH is still the best available tool（"conditioning on total score is imperfect
      but standard psychometric practice for multidimensional tests"），而非claim
      results are unaffected。
    tables:
      - name: "Architecture Stratification Results"
        columns: ["Metric", "Full_pop (N=5227)", "Decoder-only (N=5226)", "Δ"]
        rows:
          - ["ETS C%", 31.3, 31.3, 0.0]
          - ["Jaccard vs full", "—", 1.000, "—"]
          - ["RMSEA", 0.089, 0.089, 0.000]
          - ["CFI", 0.41, 0.41, 0.00]
          - ["|Lz|>2 %", 98.1, 97.8, -0.3]
          - ["FPR (temporal)", 0.314, 0.313, -0.001]
      - name: "Non-decoder Model Impact"
        columns: ["Model", "Architecture", "Effect_on_C%", "Effect_on_rankings"]
        rows:
          - ["RWKV-v5-Eagle-7B", "RWKV (linear attention)", "None", "None"]
    figures_description:
      - "Fig: IRT person-fit (|Lz|) distribution for decoder-only subset — virtually identical to full population. Peak at |Lz|≈4-5 with 97.8% above misfit threshold. Architecture homogeneity does not rescue IRT fit."
    analysis: >
      Architecture stratification是一个"dissolved concern"——architecture不是问题，
      但IRT misfit仍然是。在worst tier reframe中：(1)architecture section变成一段话
      而非一节——"concern dissolved, 99.98% decoder-only"；(2)IRT misfit discussion
      变得更prominent——"we acknowledge 1D IRT is fundamentally misspecified for MMLU;
      total-score conditioning is our pragmatic choice; multidimensional IRT is future
      work"；(3)这个limitation是honest but costly——reviewer can use it to question
      the entire DIF analysis。Practitioner's Guide section mitigates by providing
      "when/how to use DIF despite IRT limitations"。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: >
      Semi-synthetic contamination injection into real METABENCH response matrix。
      500 clean items, 100-200 injected. TPR/FPR under controlled ground truth。
      Vary prevalence (5-30%), exploitation rate (0.4-1.0), focal group size (40-200)。
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
      within_subject_fpr_inflation: 0.186
      reviewer_dismissal_probability: 0.67
      injection_mechanism_realism_score: 2.3
      n_clean_items: 500
      n_injected_items: 150
      exploitation_rate_range: [0.3, 1.0]
      dose_response_monotonic: true
      prevalence_5pct_tpr: 0.41
      prevalence_10pct_tpr: 0.57
      prevalence_20pct_tpr: 0.73
      prevalence_30pct_tpr: 0.83
    result_rationale: >
      Detection metrics本身look strong——ΔTPR=+0.508 at p=0.5, clear dose-response,
      cross-subject matching eliminates FPR inflation（ΔFPR=0.000）。但worst tier
      的核心攻击不是metrics而是mechanism validity。
      
      Reviewer dismissal probability=0.67基于核心假设#6："flipping incorrect→correct
      doesn't model real contamination mechanisms"。具体攻击：(1)真实contamination
      是memorization——模型在training中多次见到item，导致parameterized recall，表现为
      high confidence on specific items而非simple correctness flip；(2)真实contamination
      影响response pattern而非just accuracy——contaminated model可能在某些distractors
      上有异常pattern（always选A），simple flip不capture这个；(3)partial contamination
      is not random——contaminated model更可能在semantically similar items上都contaminated
      （cluster structure），而random sampling的injection忽略了这个structure；
      (4)exploitation rate concept假设contamination是binary（correct with probability p），
      但实际是gradient（模型"部分记住"一个item可能表现为distractor bias而非correctness）。
      
      "Injection realism score"=2.3/5（hypothetical expert rating）——method是
      sound as a statistical framework但ecological validity低。这是worst tier下
      ΔTPR被解读为"your framework can detect your artificial signal, but does it
      detect real contamination?"的核心矛盾。
      
      Cross-subject matching的ΔFPR=0.000是genuinely novel and survives所有attacks——
      即使injection mechanism被dismissed，matching methodology contribution stands。
    tables:
      - name: "Semi-synthetic Detection Power (Cross-subject Matching)"
        columns: ["Exploitation_rate", "TPR", "ΔTPR", "FPR", "ΔFPR"]
        rows:
          - ["p=0.0 (baseline)", 0.326, 0.000, 0.314, 0.000]
          - ["p=0.3", 0.548, 0.222, 0.314, 0.000]
          - ["p=0.5", 0.834, 0.508, 0.314, 0.000]
          - ["p=0.7", 0.990, 0.664, 0.314, 0.000]
          - ["p=1.0", 1.000, 0.674, 0.314, 0.000]
      - name: "Mechanism Realism Critique"
        columns: ["Aspect", "Semi-synthetic", "Real_contamination", "Mismatch"]
        rows:
          - ["Signal type", "Binary flip", "Parametric recall", "HIGH"]
          - ["Response pattern", "Only accuracy", "Distractor bias", "HIGH"]
          - ["Item correlation", "Random selection", "Semantic clusters", "MEDIUM"]
          - ["Effect gradient", "p ∈ {0,1}", "Continuous partial", "MEDIUM"]
          - ["Ability distribution", "Real (preserved)", "Real", "NONE"]
    figures_description:
      - "Fig: Dose-response curve showing ΔTPR vs exploitation rate p, with 95% bootstrap CIs. Monotonically increasing, confirming framework sensitivity. But annotation: 'Detection power is validated against synthetic signal — transfer to natural contamination is assumed, not demonstrated.'"
    analysis: >
      Semi-synthetic validation在worst tier reframe中的定位shift from "validation
      of DIF as contamination detector" to "reusable validation infrastructure that
      any item-level detector can plug into"。ΔTPR methodology和cross-subject matching
      是framework contributions that survive mechanism critique。关键修改：(1)不再
      claim "DIF can detect real contamination"——而是"DIF can detect differential
      item functioning under synthetic contamination, consistent with but not proof of
      real-world detection"；(2)explicitly acknowledge injection mechanism limitations
      in Method section而非buried in limitations；(3)frame cross-subject matching
      as primary contribution of this experiment——ΔFPR=0.000 across all conditions
      是genuinely novel practical insight。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d95984aa-e811-47d3-9ba6-ab84aaeaef8b",
  "isSidechain": false,
  "requestId": "req_011CbF7FHeVkWPTYEWtZYm8E",
  "type": "assistant",
  "uuid": "c16a6dfb-1919-4178-b12a-a5ae1ea03c76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbRFiVauE3abWgvXxv4Bpk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18438,
      "cache_read_input_tokens": 11841,
      "output_tokens": 19484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 19484,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18438
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Discovery framing rejected as insufficient contribution; key robustness checks reveal structural weaknesses requiring reframing 核心假设：['SIBTEST reveals >15…",
  "leafUuid": "c16a6dfb-1919-4178-b12a-a5ae1ea03c76",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe DIF study as measurement stability framework",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Discovery framing rejected as insufficient contribution; key robustness checks reveal structural weaknesses requiring reframing 核心假设：['SIBTEST reveals >15…",
  "leafUuid": "c16a6dfb-1919-4178-b12a-a5ae1ea03c76",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe DIF study as measurement stability framework",
  "sessionId": "4a1d2807-329e-4949-b6cf-c299e99c22e3"
}
```

---
