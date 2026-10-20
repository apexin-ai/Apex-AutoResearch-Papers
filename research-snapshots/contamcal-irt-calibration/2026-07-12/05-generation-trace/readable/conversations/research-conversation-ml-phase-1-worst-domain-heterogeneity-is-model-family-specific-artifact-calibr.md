# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：domain heterogeneity is model-family-specific artifact; calibration fails g

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/66e2e40f-b391-422e-96bc-6a19db08ef72.jsonl`
- **Structured JSON:** [`8f65e0a7d8f6257ccd61.json`](../../sessions/8f/8f65e0a7d8f6257ccd61.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T16:21:42.119Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T16:21:42.119Z",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：domain heterogeneity is model-family-specific artifact; calibration fails gating on most benchmarks; contribution reduces to diagnostic framework + signal failure + identifiability impossibility\n核心假设：['Llama-3.2-3B STEM gradient contradicts Qwen (different domain ordering, or all γ ≈ 0)', 'ARC γ sign or magnitude differs substantially across families → forgetting may be Qwen SFT-specific', 'Coverage stays 30-50% at N=24 — IRT CIs are not usable credible intervals', 'Calibration MAE ≥ raw MAE on 2/3 benchmarks (gating blocks calibration on GSM8K and MMLU)', 'Linear regression matches or beats IRT MAE on all benchmarks', '0.5B exclusion + non-STEM misfit → effective analysis limited to 1.5B/3B × STEM × ARC', 'Sim sweep AUC=0.65 conditions never completed — identifiability phase diagram has gap']\n关键指标范围：{'arc_gamma': [-1.5, -0.3], 'arc_gamma_ci_excludes_zero': [False, True], 'arc_calibration_mae': [0.04, 0.07], 'arc_raw_mae': [0.035, 0.06], 'gsm8k_gamma': [-0.5, 0.8], 'gsm8k_calibration_mae_vs_raw': ['worse', 'worse'], 'mmlu_stem_math_gamma': [0.3, 1.0], 'mmlu_aggregate_gamma': [-0.3, 0.3], 'coverage_95_at_n24': [0.3, 0.5], 'kendall_tau': [0.55, 0.7], 'signal_s1_auc_d005': [0.95, 0.99], 'signal_s2_cohens_d_reversal': [-2.8, -1.2], 'cross_family_stem_gradient_matches_qwen': [False, False], 'benchmarks_passing_calibration_gating': [0, 1], 'irt_vs_linear_bootstrap_p': [0.3, 0.8]}\n叙事方向：Reframe entirely as diagnostic framework paper. Lead: \"We built ContamCal to calibrate  contaminated benchmarks — and discovered why this is harder than expected.\" Three  diagnostic contributions survive intact regardless of calibration failure: (1) Min-K++  directional reversal is a standalone cautionary finding for the detection community —  the most widely-used signal actively misleads at small scales, (2) Fisher Information  identifiability analysis reveals a structural domain-method mismatch — IRT requires  N≥50 examinees but LLM evaluation operates at N=8-30, making reliable γ recovery  impossible in typical settings, (3) contamination effects are benchmark-dependent  (ARC forgetting vs GSM8K resistance confirmed within Qwen), but domain-level  heterogeneity within MMLU may be model-family-specific (honest negative result).  Calibration gating criterion itself becomes a contribution: ContamCal identifies WHEN  calibration should not be attempted. Coverage collapse is reframed as fundamental  limitation of applying IRT to LLMs (local independence violation + low N), not a  fixable engineering problem. Position paper angle: \"Benchmark contamination calibration  is an open problem — here's why, and here are the identifiability boundaries.\"  Still targets EMNLP (special theme explicitly invites this kind of honest diagnostic work).\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contamcal-irt-calibration\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight (D039 pivot + D108/D115 domain heterogeneity — N=24 confirmed)\nBenchmark contamination effects are far more complex than \"scores go up.\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks STEM-gradient pattern where factual-knowledge domains show strong positive γ while non-STEM domains exhibit model misfit), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\n\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\n\n1. **Characterization Claim (PRIMARY — D108/D115: domain heterogeneity confirmed at N=24)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks a clear STEM gradient. **N=24 confirmed results (D115)**:\n   - STEM_Math: γ=+0.969, CI excludes 0, PPP=0.438 ✓ (strong positive — contamination inflates factual recall)\n   - STEM_Science: γ=+0.838, CI excludes 0, PPP=0.807 ✓ (strong positive)\n   - STEM_CS_Eng: γ=+0.197, CI includes 0, PPP=0.892 ✓ (null — procedural/applied knowledge less affected)\n   - Non-STEM (Medical, Humanities, Social_Sciences, Business_Law): all PPP≈1.0 → 2PL+γ model structurally misspecified. Negative γ estimates (-0.17 to -0.50) reflect model assumption failure, not true contamination direction.\n   - \"Other\" domain: system crash (disk/cgroup), non-essential catch-all category.\n   **Interpretation**: Contamination susceptibility maps to factual knowledge density — domains rich in memorizable facts (Math, Science) show large positive γ (SFT exposure → recall boost → inflated scores). Procedural/applied domains (CS_Eng) show weaker effect. Non-STEM domains require richer models (multidimensional IRT or domain-specific covariates) — reported as acknowledged limitation and future work.\n   **Paper claim scope**: Domain heterogeneity is established via (a) Simpson's paradox (aggregate ≈ 0, domain-level ≠ 0), (b) STEM gradient with good model fit (3/8 domains with PPP∈[0.1,0.9]), (c) non-STEM misfit as structural boundary of 2PL+γ. Claims based on domains with acceptable PPP ONLY. Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant \"contamination = uniform inflation\" narrative. Cross-family consistency with Llama-3.2-3B (pending eval completion) tests whether contamination susceptibility is a benchmark × domain property, not a model family artifact.\n   **PPP presentation strategy**: Non-STEM PPP=1.0 is not a failure of the analysis but a meaningful boundary finding: 2PL+γ (additive contamination effect on unidimensional ability) captures STEM domain mechanics but not non-STEM. Discuss connection to multidimensional IRT (Reckase 2009) and DIF literature (Holland & Wainer 1993). Consider limited-information fit indices (M2*, RMSEA2) as robustness check for STEM results.\n\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\n   **C2 contingency**: \"Scale-dependent\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness.\" Min-K++ reversal remains novel regardless.\n\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \"impossibility,\" not merely \"IRT needs more data.\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\n\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.\n\n## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)\n\n### Core (characterization-led; calibration conditional)\n1. **Domain-dependent contamination characterization** via IRT γ_k: Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity maps to factual knowledge density. Non-STEM model misfit as boundary finding (2PL+γ scope limitation)\n2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice\n3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)\n\n### Supporting\n4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\n5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to \"fix\" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.\n- **Headline result template (D039 — characterization-led)**: \"Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \"S1+IRT calibration with extensible multi-signal architecture for future signals.\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\n| 20 | GSM8K overcorrection — calibration 11× worse than raw (D039, all 3 dream tiers) | Honest negative result. Implement calibration gating: γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE. Report raw scores when gating fails. Reframe: ContamCal identifies when NOT to calibrate. | exp-006 |\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\n\n## Evaluation Protocol (6 Metrics — D025 added SBC)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\n\n## Benchmarks (2 main + 2 contrasts)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \"benchmark-dependent contamination effects\" — ContamCal calibrates in both directions.\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \"ContamCal identifies benchmarks not requiring calibration\")\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\nD025 additions (all 3 Dream tiers flagged):\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\n\n## Discussion Notes\n\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\n- **Paper treatment**: Report in Discussion as \"capacity threshold for reliable MC evaluation.\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim: 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  registry_id: exp_001_sft_injection\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim: 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  registry_id: exp_002_signals_05B\n  status: DONE\n  conclusion: success\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim: 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  registry_id: exp_003_rrf_05B\n  status: DONE\n  conclusion: success\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim: 1\n  also_supports:\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  registry_id: exp_004_sim_sweep\n  status: DONE\n  conclusion: failed\n- id: exp-005\n  name: noise_propagation_analysis\n  claim: 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  registry_id: exp_005_noise_prop_v4\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim: 1\n  also_supports:\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY:\\\n    \\ per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization\\\n    \\ when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION:\\\n    \\ joint fitting across benchmarks with shared global γ (stronger assumption, tests\\\n    \\ whether contamination effect is homogeneous across benchmarks). Report both.\\\n    \\ Per-benchmark fitting (not joint) is the default to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  registry_id: exp_006_irt_05B_gsm8k\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- id: exp-015\n  name: sft_d100_qc_only\n  claim: 1\n  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n    Isolates noisy vs clean contamination confound identified by reviewer. D012 decision.\n    Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify\n    effect of noisy contamination on IRT estimates.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  seeds: 1\n  status: planned\n  registry_id: null\n  data_script: exp001/prepare_qc_only_data.py\n- id: exp-007\n  name: scale_bridging_7b\n  claim: 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim: 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  registry_id: exp_008_signal_survival_v4\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- id: exp-014\n  name: multi_family_validation\n  claim: 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim: 2\n  also_supports:\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim: 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim: 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001_eval_05B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.3976\n    gsm8k_exact_match: 0.3404\n    humaneval_pass_at_1: 0.1037\n    mmlu_accuracy: 0.4182\n- exp_id: exp_001_eval_05B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4049\n    gsm8k: 0.3647\n    arc_challenge: 0.378\n    humaneval: 0.1098\n- exp_id: exp_001_eval_05B_d000_s42_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2929\n    gsm8k: 0.3601\n    arc_challenge: 0.2858\n    humaneval_pass1: 0.0793\n    mmlu_correct: 4113\n    mmlu_total: 14042\n    gsm8k_correct: 475\n    gsm8k_total: 1319\n    arc_correct: 335\n    arc_total: 1172\n    humaneval_correct: 13\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_d100\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2322\n    gsm8k: 0.3571\n    arc_challenge: 0.227\n    humaneval_pass1: 0.0854\n- exp_id: exp_001_eval_05B_d100_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5762\n    gsm8k: 0.6331\n    arc_challenge: 0.7662\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_15B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.7756\n    arc_challenge_correct: 909\n    arc_challenge_total: 1172\n    gsm8k_correct: 840\n    gsm8k_exact_match: 0.6368\n    gsm8k_total: 1319\n    humaneval_correct: 21\n    humaneval_pass_at_1: 0.128\n    humaneval_total: 164\n    mmlu_accuracy: 0.5753\n    mmlu_correct: 8079\n    mmlu_total: 14042\n- exp_id: exp_001_eval_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6362\n    gsm8k_exact_match: 0.1759\n    arc_challenge_accuracy: 0.8294\n    humaneval_pass_at_1: 0.0854\n- exp_id: exp_001_eval_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.117\n    arc: 0.822\n    humaneval: 0.116\n- exp_id: exp_001_eval_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.1198\n    arc_challenge: 0.8276\n    humaneval: 0.1159\n- exp_id: exp_001_sft_0pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_0pct_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 34\n    checkpoint_size_mb: 166\n    exit_code: 0\n    final_loss: 1.4894\n    mean_train_loss: 1.5388\n    steps: 3125/3125\n    token_accuracy: 0.682\n    training_time_min: 52.9\n- exp_id: exp_001_sft_0pct_05B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.676\n    train_loss: 1.5393\n    train_time_min: 54.5\n- exp_id: exp_001_sft_0pct_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 71\n    checkpoint_size_mb: 313\n    exit_code: 0\n    final_loss: 1.2039\n    mean_train_loss: 1.2599\n    steps: 3125/3125\n    token_accuracy: 0.711\n    training_time_min: 101.5\n- exp_id: exp_001_sft_0pct_15B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.731\n    train_loss: 1.2602\n    train_time_min: 101.5\n- exp_id: exp_001_sft_0pct_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 115\n    checkpoint_size_mb: 488\n    exit_code: 0\n    final_loss: 1.0736\n    mean_train_loss: 1.1306\n    steps: 3125/3125\n    token_accuracy: 0.734\n    training_time_min: 214.7\n- exp_id: exp_001_sft_0pct_3B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_model_mb: 114\n    adapter_size_mb: 488\n    checkpoint_size_mb: 488\n    epochs: 1\n    final_loss: 1.114\n    mean_token_accuracy: 0.7505\n    mean_train_loss: 1.1309\n    steps_completed: 3125\n    total_steps: 3125\n    total_tokens: 19555717\n    train_samples_per_second: 3.91\n    training_time_min: 213.1\n- exp_id: exp_001_sft_100pct_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_size_mb: 166\n    entropy: 1.5874\n    epoch: 1\n    exit_code: 0\n    final_loss: 1.478\n    lora_adapter_size_mb: 33.6\n    mean_train_loss: 1.5424\n    num_tokens: 19657865\n    token_accuracy: 0.667\n    total_steps: 3177\n    train_samples_per_second: 15.09\n    train_steps_per_second: 0.943\n    training_time_min: 56.14\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: -0.0114\n      delta_mean_train_loss: 0.0036\n      delta_token_accuracy: -0.015\n      delta_training_time_min: 3.24\n- exp_id: exp_001_sft_d005_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2637\n    mean_token_accuracy: 0.7308\n    train_runtime_s: 19864.7\n    epoch: 1\n- exp_id: exp_001_sft_d100_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exit_code: 0\n    final_loss: 1.5943\n    mean_train_loss: 1.5662\n    num_tokens: 21575068\n    token_accuracy: 0.666\n    total_steps: 4160\n    train_samples_per_second: 16.09\n    train_steps_per_second: 1.006\n    training_time_min: 68.9\n    vs_baseline_0pct:\n      accuracy_delta: -0.016 (-2.3%)\n      loss_delta: +0.0274 (+1.8%)\n      time_delta: +16min (+30%)\n- exp_id: exp_001_sft_d100_15B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d100_15B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_injection\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      max_rhat: 1.003\n      overall: PASS\n      theta_corr: 0.943\n      theta_rmse: 0.238\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    actual_confound_corr: 0.3814\n    divergent_pct: 0\n    fit_time_sec: 832\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    max_rhat: 1.007\n    min_ess: 1371.9\n    overall: PASS\n    theta_corr: 0.9733\n    theta_residual_exp_corr: 0.0582\n    theta_rmse: 0.2407\n- exp_id: exp_001_sft_d100_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.178\n    token_accuracy: 0.7206\n    runtime_hours: 5.2\n    steps: 4159/4159\n    epoch: 1\n- exp_id: exp_001_sft_d025_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.5178\n    mean_train_loss: 1.5479\n    entropy: 1.5415\n    mean_token_accuracy: 0.6697\n    num_tokens: 20058085\n    total_steps: 3384\n    epoch: 1\n    train_samples_per_second: 15.52\n    train_steps_per_second: 0.97\n    training_time_min: 58.1\n    exit_code: 0\n    lora_adapter_size_mb: 33.6\n    checkpoint_size_mb: 166\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: 0.0284\n      delta_mean_train_loss: 0.0091\n      delta_token_accuracy: -0.0123\n      delta_training_time_min: 5.2\n- exp_id: exp_001_eval_05B_raw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2302\n    gsm8k: 0.1592\n    arc_challenge: 0.2261\n    humaneval: incomplete (hung at 51/164)\n- exp_id: exp_001_eval_3B_raw_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.605\n    humaneval: 0\n- exp_id: exp_004_sim_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    runs_completed: 48\n    runs_total: 120\n    auc080_n50_bias: 0.006\n    auc080_n50_rmse: 0.03\n    auc080_n50_ci95_coverage: 1\n    auc080_n100_gamma_hat: 0.508\n    auc080_n100_bias: 0.008\n    auc080_n100_ci_width: 0.116\n    auc080_n100_theta_corr: 0.962\n    ci_width_ratio_n100: 1.81\n    core_findings_stable: true\n- exp_id: exp_001_eval_15B_d100_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    mmlu_correct: 8331\n    mmlu_total: 14042\n    gsm8k_exact_match: 0.6497\n    gsm8k_correct: 857\n    gsm8k_total: 1319\n    arc_challenge_accuracy: 0.7688\n    arc_challenge_correct: 901\n    arc_challenge_total: 1172\n    humaneval_pass_at_1: 0.3049\n    humaneval_correct: 50\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    d000_aligned_mmlu: 0.3979\n    d000_aligned_gsm8k: 0.3692\n    d000_aligned_arc: 0.4693\n    d000_aligned_humaneval: 0.1098\n    d000_para_aligned_mmlu: 0.4428\n    d000_para_aligned_gsm8k: 0.2807\n    d000_para_aligned_arc: 0.4792\n    d000_para_aligned_humaneval: 0.1154\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_002_signals_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      d000_orig: 0.5853\n      d005_orig: 0.5852\n      d100_orig: 0.5933\n      d000_para: 0.6096\n      d005_para: 0.6164\n      d100_para: 0.6252\n    gsm8k:\n      d000_orig: 0.6543\n      d005_orig: 0.6482\n      d100_orig: 0.6497\n      d000_para: 0.557\n      d005_para: 0.5439\n      d100_para: 0.5526\n    arc:\n      d000_orig: 0.7722\n      d005_orig: 0.7688\n      d100_orig: 0.7688\n      d000_para: 0.7547\n      d005_para: 0.7532\n      d100_para: 0.7661\n    humaneval:\n      d000_orig: 0.128\n      d005_orig: 0.25\n      d100_orig: 0.3049\n      d000_para: 0.0385\n      d005_para: 0.1923\n      d100_para: 0.2692\n    key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp).\n      HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly\n      separate contamination.\n- exp_id: exp_001_sft_d005_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_hours: 3.76\n    final_loss: 1.11\n    total_steps: 3177\n    epochs: 1\n- exp_id: exp_001_eval_3B_d000_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.634\n    gsm8k_exact_match: 0.1198\n    arc_challenge_accuracy: 0.8276\n    humaneval_pass_at_1: 0.1159\n- exp_id: exp_001_eval_3B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6417\n    gsm8k_exact_match: 0.6967\n    arc_challenge_accuracy: 0.8396\n    humaneval_pass1: 0.122\n- exp_id: exp_001_eval_3B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.208\n    arc_challenge: 0.829\n    humaneval_pass_at_1: 0.146\n- exp_id: exp_001_eval_05B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 28.03\n    GSM8K: 36.62\n    ARC: 32.51\n    HumanEval: missing - process exited before 4th benchmark\n- exp_id: exp_003_rrf_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_d025_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2715\n    mean_token_accuracy: 0.7192\n    entropy: 1.2623\n    steps: 3384\n    epochs: 1\n    train_runtime_seconds: 11610.6\n- exp_id: exp_006_irt_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_001_eval_05B_d100_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2334\n    gsm8k: 0.3654\n    arc_challenge: 0.2944\n    humaneval_pass_at_1: 0\n    mmlu_delta_vs_d000: -0.1645\n    arc_delta_vs_d000: -0.1749\n    humaneval_delta_vs_d000: -0.1098\n- exp_id: exp_001_eval_05B_d005_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.3548\n    gsm8k: 0.2588\n    arc_challenge: 0.33\n    humaneval: 0\n    mmlu_correct: 2340\n    mmlu_total: 6596\n    gsm8k_correct: 59\n    gsm8k_total: 228\n    arc_correct: 230\n    arc_total: 697\n    humaneval_correct: 0\n    humaneval_total: 26\n- exp_id: exp_001_eval_05B_d025_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2835\n    gsm8k: 0.3114\n    arc_challenge: 0.3199\n    humaneval_pass1: 0.1923\n    format: paraphrased_aligned\n- exp_id: exp_008_signal_survival\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d000_mmlu: 0.5049\n    S1_d000_gsm8k: 0.5502\n    S1_d000_arc: 0.427\n    S1_d005_mmlu: 0.953\n    S1_d005_gsm8k: 0.9882\n    S1_d005_arc: 0.995\n    S1_d100_mmlu: 0.4943\n    S1_d100_gsm8k: 0.4127\n    S1_d100_arc: 0.501\n    S2_d005_mmlu: 0.4655\n    S2_d005_gsm8k: 0.4649\n    S2_d005_arc: 0.4659\n    S4_d005_mmlu: 0.5165\n    S4_d005_gsm8k: 0.4947\n    S4_d005_arc: 0.4325\n    signals_surviving: 0\n    signals_total: 3\n- exp_id: exp_001_sft_3B_d000_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\n    completed_at: 2026-05-15T03:45Z\n- exp_id: exp_008_signal_survival_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- exp_id: exp_008_instruct_rl_proxy\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    instruct_signals_complete: true\n    d000_sft_signals_complete: true\n    base_pretrained_signals: computing_PID_701898_GPU5\n    comparison:\n      mmlu:\n        instruct_s2: 1.6952\n        instruct_s4: -0.8782\n        d000_sft_s2: 1.6976\n        d000_sft_s4: -0.9557\n        base_s2: 1.7009\n        base_s4: computing\n        s4_delta_instruct_vs_sft: 0.0775\n      gsm8k:\n        instruct_s2: 1.7073\n        instruct_s4: -0.9632\n        d000_sft_s2: 1.6532\n        d000_sft_s4: -0.9408\n        s4_delta_instruct_vs_sft: -0.0224\n      arc:\n        instruct_s2: 1.6737\n        instruct_s4: -0.9227\n        d000_sft_s2: 1.7079\n        d000_sft_s4: -0.9538\n        s4_delta_instruct_vs_sft: 0.0311\n    key_finding: S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT);\n      S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\n    signal_paths:\n      instruct: /root/autodl-tmp/exp008/signals/rl_aligned/\n      d000_sft: /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\n      base_pretrained: /root/autodl-tmp/exp008/signals/base_pretrained/\n- exp_id: exp_006_irt_05B_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_006_irt_05B_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- exp_id: exp_001_eval_15B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5902\n    gsm8k: 0.6535\n    arc_challenge: 0.7688\n    humaneval_pass1: 0.2256\n- exp_id: exp_001_sft_d100_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 4159/4159\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\n    d020_params: lr=5e-5, alpha=16, r=16\n- exp_id: exp002-signal-d025-05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_d005_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5852\n    gsm8k: 0.6482\n    arc_challenge: 0.7688\n    humaneval_pass_at_1: 0.25\n- exp_id: exp_001_eval_15B_d025_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.618\n    gsm8k: 0.539\n    arc_challenge: 0.766\n    humaneval: 0.154\n- exp_id: exp_001_eval_15B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    gsm8k_accuracy: 0.6497\n    arc_challenge_accuracy: 0.7688\n    humaneval_correct: 50\n    humaneval_total: 164\n    humaneval_pass_rate: 0.3049\n- exp_id: exp_001_eval_3B_d100_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.676\n    gsm8k: 0.614\n    arc_challenge: 0.828\n- exp_id: exp006-gsm8k-d024-delta\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp002-signals-1p5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_pooled_gsm8k_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_irt_05B_arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.21\n    gamma_ci_lower: -2.53\n    gamma_ci_upper: 0.12\n    fit_type: joint\n- exp_id: exp_001_sft_15B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.3002\n    mean_token_accuracy: 0.7178\n    entropy: 1.3327\n    train_runtime_seconds: 14663.6\n    steps: 4159\n    epochs: 1\n    num_tokens: 21575068\n    baseline_seed42_train_loss: 1.2996\n    baseline_seed42_token_accuracy: 0.7033\n- exp_id: exp_001_sft_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1361\n    epochs: 1\n    steps: 3125\n    mean_token_accuracy: 0.748\n    train_runtime_seconds: 13141.8\n    entropy: 1.1108\n    baseline_seed42_train_loss: 1.1357\n- exp_id: exp_003_mmlu_item_aligned_gap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 20\n    n_common_items: 6596\n    aggregate:\n      mean_gap_pp: -2.243\n      std_gap_pp: 0.671\n      max_abs_gap_pp: 3.73\n      median_gap_pp: -2.259\n    per_item:\n      pct_neutral_lt03pp: 84.8\n      pct_para_easier: 8.6\n      pct_aligned_easier: 6.6\n      pct_high_disagree_gt50: 6.5\n      n_flagged_items: 426\n      mean_disagree_rate_pct: 15.5\n    by_size:\n      0.5B:\n        mean_pp: -2.259\n        std_pp: 1.238\n        n: 4\n      1.5B:\n        mean_pp: -2.452\n        std_pp: 0.31\n        n: 8\n      3B:\n        mean_pp: -2.026\n        std_pp: 0.415\n        n: 8\n    by_contamination:\n      d000:\n        mean_pp: -2.292\n        n: 5\n      d005:\n        mean_pp: -2.181\n        n: 6\n      d025:\n        mean_pp: -1.913\n        n: 5\n      d100:\n        mean_pp: -2.687\n        n: 4\n    alignment_correction:\n      misaligned_vs_aligned_diff_pp: <0.3 (confirmed from prior 2-pair check)\n      conclusion: Proper item-ID alignment changes result by <0.3pp vs naive positional\n        comparison\n    prior_2pair_check:\n      15B_d100:\n        aligned_gap_pp: -2.9\n        qc_selection_bias_pp: 0.56\n      3B_d100:\n        aligned_gap_pp: -3.5\n        qc_selection_bias_pp: -0.08\n- exp_id: exp_001_eval_3B_d000_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6295\n    gsm8k: 0.3525\n    arc_challenge: 0.8183\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_05B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3058\n    gsm8k_accuracy: 0.3798\n    arc_challenge_accuracy: 0.3669\n    humaneval_pass_at_1: 0.1037\n    mmlu_correct: 4294\n    mmlu_total: 14042\n    gsm8k_correct: 501\n    gsm8k_total: 1319\n    arc_challenge_correct: 430\n    arc_challenge_total: 1172\n    humaneval_total: 164\n- exp_id: exp_005_noise_prop_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- exp_id: exp_004_sim_sweep_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6468\n    format: paraphrased_aligned\n- exp_id: exp006-pooled-05B-15B-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: 0.1871\n    gamma_perbench_ci:\n    - -0.92\n    - 1.33\n    gamma_joint: 0.1202\n    gamma_joint_ci:\n    - -0.74\n    - 0.96\n    mae: 0.036\n    coverage_95: 0.5\n    ppp: 0.336\n    n_models: 8\n    convergence: FAILED (rhat=1.015, ess=330)\n    NOTE: per-bench not converged; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -2.3471\n    gamma_perbench_ci:\n    - -3.46\n    - -1.19\n    gamma_joint: -1.4637\n    gamma_joint_ci:\n    - -2.51\n    - -0.41\n    mae: 0.035\n    coverage_95: 0.625\n    ppp: 0.999\n    n_models: 8\n    convergence: OK\n    NOTE: coverage below 95%; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-mmlu-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -3.8073\n    gamma_perbench_ci:\n    - -7.02\n    - 3.22\n    gamma_joint: -0.2095\n    gamma_joint_ci:\n    - -1.01\n    - 0.59\n    mae: 0.099\n    coverage_95: 1\n    ppp: 0.75\n    n_models: 8\n    convergence: FAILED (rhat=1.54, ess=7)\n    NOTE: fit completely failed, not reportable\n- exp_id: exp_001_eval_3B_d100_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    INVALID: metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output\n      dir was empty. PID 461879 died before completion.\n- exp_id: exp_001_sft_d025_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.5422\n    final_loss: 1.4542\n    mean_token_accuracy: 0.6356\n    final_token_accuracy: 0.6794\n    total_steps: 3177\n    train_runtime_sec: 3458.58\n    epoch: 1\n- exp_id: exp_001_sft_d025_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1501\n    mean_token_accuracy: 0.7342\n    steps: 3384\n    epochs: 1\n    runtime_seconds: 14499\n- exp_id: exp006-pooled-s1only-arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.4637\n    gamma_sd: 0.5276\n    gamma_ci_lower: -2.51\n    gamma_ci_upper: -0.4051\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.0098\n    ess_min: 769.6\n    divergent_pct: 0\n    ppp: 0.9677\n    mae: 0.0347\n    ece: 0.0319\n    brier: 0.0018\n    coverage_95: 0.625\n    coverage_80: 0.25\n    coverage_50: 0\n    sharpness_95: 0.0684\n    kendall_tau: 0.7559\n    fit_time_sec: 317.7\n    n_models: 8\n    n_items: 1172\n    baselines:\n      B0_raw_mae: 0.0588\n      B1_remove_rescore_mae: 0.0588\n      B2_2pl_gamma_mae: 0.064\n      B3_vanilla_4pl_mae: 0.0706\n      B4_linear_regression_mae: 0.0562\n      B5_emperor_mae: 0.0588\n      B6_dcr_fuzzy_mae: 0.2454\n- exp_id: exp006-pooled-s1only-gsm8k\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-oracle-gsm8k-extended\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.659\n    gsm8k_para: 0.5833\n    arc_challenge_para: 0.8092\n    humaneval_para_pass1: 0.1154\n- exp_id: exp_001_sft_3B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1846\n    mean_token_accuracy: 0.7343\n    steps: 4159\n    epochs: 1\n    runtime_seconds: 18252\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6468\n    gsm8k_para_accuracy: 0.2895\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_004_sim_sweep_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5956\n    gsm8k_accuracy: 0.6444\n    arc_challenge_accuracy: 0.7816\n    humaneval_pass@1: 0.2805\n- exp_id: exp_001_eval_05B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3002\n    gsm8k_accuracy: 0.3677\n    arc_challenge_accuracy: 0.2978\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_3B_d100_v2_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.632\n    gsm8k_accuracy: 0.7415\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-pooled-s1only-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 0.1871\n    gamma_sd: 0.5687\n    gamma_ci_lower: -0.9172\n    gamma_ci_upper: 1.3294\n    gamma_ci_excludes_zero: false\n    rhat_max: 1.0148\n    ess_min: 330.2\n    divergent_pct: 0\n    ppp: 0.336\n    residual_mae: 0.0367\n    fit_time_sec: 336.9\n    n_models: 8\n    n_items: 1319\n    diagnostics_ok: false\n    note: No evaluation/baselines files generated; only IRT fit available. rhat and\n      ESS did not pass thresholds.\n- exp_id: exp006-oracle-gsm8k-extended-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 3.773\n    gamma_sd: 0.504\n    gamma_ci_lower: 2.741\n    gamma_ci_upper: 4.714\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.002\n    ess_min: 1221.9\n    divergent_pct: 0\n    ppp: 0\n    mae: 0.0917\n    ece: 0.0894\n    coverage_95: 0.31\n    coverage_80: 0.25\n    coverage_50: 0.25\n    kendall_tau: 0.505\n    fit_time_sec: 6240.3\n    n_models: 16\n    n_items: 1319\n    baselines:\n      B0_raw_mae: 0.005\n      B4_linear_regression_mae: 0.008\n      B5_emperor_mae: 0.005\n      B6_dcr_fuzzy_mae: 0.138\n- exp_id: exp_001_eval_05B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.3166\n    gsm8k_para_accuracy: 0.2939\n    arc_challenge_para_accuracy: 0.2912\n    humaneval_para_pass@1: 0\n- exp_id: exp_001_eval_3B_d000_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6314\n    gsm8k: 0.2676\n    arc_challenge: 0.8259\n    humaneval: 0.061\n- exp_id: exp_001_eval_3B_d000_v2_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6512\n    gsm8k_para_accuracy: 0.1491\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_008_instruct_05B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2462\n    gsm8k_accuracy: 0.3882\n    arc_challenge_accuracy: 0.2816\n    humaneval_pass@1: 0\n- exp_id: exp_001_sft_05B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v7\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    seeds_attempted: 97\n    seeds_ok: 59\n    seeds_total: 120\n    conditions_complete: 4\n    conditions_partial: 5\n    conditions_missing: 3\n    failure_cause: Disk quota exceeded ([Errno 122]) - root partition /tmp filled\n      by CmdStan temp files\n    conditions_fully_ok:\n    - auc0.55_n20 (10/10)\n    - auc0.55_n50 (10/10)\n    - auc0.8_n20 (10/10)\n    - auc0.8_n50 (10/10)\n    conditions_partial_ok:\n    - auc0.55_n100 (7/10)\n    - auc0.8_n100 (6/10)\n    - auc0.9_n20 (6/10)\n    conditions_all_failed:\n    - auc0.65_n20 (0/10)\n    - auc0.65_n50 (0/7)\n    conditions_never_started:\n    - auc0.65_n100\n    - auc0.9_n50\n    - auc0.9_n100\n- exp_id: exp006-oracle-arc-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -0.618\n    gamma_ci:\n    - -1.04\n    - -0.2\n    rhat: 1.006\n    ESS: 1512\n    MAE: 0.0759\n    C95_coverage: 0.1818\n- exp_id: exp006-s1only-gsm8k-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma_mean: 0.1389\n    gamma_sd: 0.2274\n    gamma_ci95:\n    - -0.306\n    - 0.591\n    ci_excludes_zero: false\n    max_rhat: 1.0024\n    min_ess: 3604.4\n    divergent_count: 0\n    ppp: 0.2835\n    residual_mae: 0.0083\n    obs_mean_acc: 0.5086\n    pred_mean_acc: 0.5011\n- exp_id: exp006-oracle-arc-4pl-pooled\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.548\n    accuracy: 0.697\n    global_steps: 3384\n    epoch: 1\n    runtime_seconds: 5930\n- exp_id: exp_001_eval_3B_d025_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5998\n    gsm8k: 0.6793\n    arc_challenge: 0.8276\n    humaneval: 0.0976\n- exp_id: exp_001_eval_3B_d025_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.621\n    gsm8k_para_accuracy: 0.5482\n    arc_challenge_para_accuracy: 0.8106\n    humaneval_para_pass@1: 0.1154\n- exp_id: exp_001_eval_3B_d100_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6319\n    gsm8k: 0.7324\n    arc_challenge: 0.8311\n    humaneval: 0.1829\n- exp_id: exp_001_eval_05B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.3473\n      correct: 4877\n      total: 14042\n    gsm8k:\n      accuracy: 0.3533\n      correct: 466\n      total: 1319\n    arc_challenge:\n      accuracy: 0.4061\n      correct: 476\n      total: 1172\n    humaneval:\n      pass@1: 0.0854\n      correct: 14\n      total: 164\n- exp_id: exp_001_eval_15B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5855\n    gsm8k_accuracy: 0.6535\n    arc_challenge_accuracy: 0.7577\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_05B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4216\n    gsm8k: 0.3412\n    arc_challenge: 0.4974\n    humaneval: 0.1037\n- exp_id: exp_001_sft_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_15B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2294\n    gsm8k: 0.163\n    arc_challenge: 0.2278\n    humaneval: 0\n- exp_id: exp_008_base_pretrained_15B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2303\n    gsm8k_accuracy: 0.0053\n    arc_challenge_accuracy: 0.2304\n    humaneval_pass@1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_eval_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_sft_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2723\n    mean_token_accuracy: 0.7466\n- exp_id: exp_001_sft_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2639\n    mean_token_accuracy: 0.6855\n- exp_id: exp_001_eval_3B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6332\n    gsm8k: 0.1812\n    arc_challenge: 0.8328\n    humaneval: 0.0854\n- exp_id: exp_001_eval_3B_d005_s42_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6345\n    gsm8k: 0.2077\n    arc_challenge: 0.8294\n    humaneval: 0.1463\n- exp_id: exp_001_eval_3B_d005_s42_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_15B_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2303\n    gsm8k: 0.0053\n    arc_challenge: 0.2304\n    humaneval_pass1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_sft_3B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1349\n    final_token_accuracy: 0.7069\n    total_steps: 3177\n- exp_id: exp_001_sft_3B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1401\n    final_token_accuracy: 0.734\n    total_steps: 3384\n- exp_id: exp_001_eval_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_3B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_002_signals_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6367\n    gsm8k: 0.5254\n    arc_challenge: 0.8336\n    humaneval: 0.1585\n- exp_id: exp_001_eval_3B_d100_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.659\n      correct: 4347\n      total: 6596\n    gsm8k:\n      accuracy: 0.5833\n      correct: 133\n      total: 228\n    arc_challenge:\n      accuracy: 0.8092\n      correct: 564\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d000_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6474\n      correct: 4270\n      total: 6596\n    gsm8k:\n      accuracy: 0.0482\n      correct: 11\n      total: 228\n    arc_challenge:\n      accuracy: 0.8235\n      correct: 574\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6324\n    gsm8k_exact_match: 0.6308\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass1: 0.1037\n- exp_id: exp_001_eval_3B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6461\n    GSM8K: 0.5\n    ARC: 0.8192\n    HumanEval: 0.0769\n- exp_id: exp_001_eval_3B_d025_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6615\n    GSM8K: 0.4254\n    ARC: 0.8121\n    HumanEval: 0.1538\n- exp_id: exp_002_signals_3B_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_3B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1464\n    mean_token_accuracy: 0.734\n    train_runtime_s: 14584\n    total_steps: 3384\n    epoch: 1\n    entropy: 1.1807\n- exp_id: exp_001_sft_3B_d100_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1805\n    mean_token_accuracy: 0.7348\n    train_runtime_seconds: 17608.59\n    train_steps: 4159\n    epoch: 1\n    train_samples_per_second: 3.778\n    entropy: 1.231\n- exp_id: exp_004_sim_sweep_v6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions_ok: 9\n    conditions_total: 12\n    conditions_failed: auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\n    gamma_bias_range: '[-0.025, +0.056]'\n    gamma_rmse_range: '[0.005, 0.085]'\n    ci95_coverage_range: '[0.8, 1.0]'\n    theta_corr_range: '[0.947, 0.972]'\n    note: 9/12 sufficient for Claim 1 identifiability\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_acc: 0.6471\n    gsm8k_acc: 0.3421\n    arc_challenge_acc: 0.8164\n    humaneval_pass1: 0.0769\n    mmlu_n: 6596\n    gsm8k_n: 228\n    arc_challenge_n: 697\n    humaneval_n: 26\n- exp_id: exp_002_signals_3B_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6565\n      correct: 4330\n      total: 6596\n    gsm8k:\n      accuracy: 0.5877\n      correct: 134\n      total: 228\n    arc_challenge:\n      accuracy: 0.8164\n      correct: 569\n      total: 697\n    humaneval:\n      pass@1: 0.0769\n      correct: 2\n      total: 26\n- exp_id: exp_002_signals_3B_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.6308\n- exp_id: exp_002_signals_3B_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_004_sim_sweep_extreme_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions: 8\n    seeds_per_condition: 10\n    total_time_hours: 11.1\n    gamma2_avg_bias: 0.017\n    gamma2_avg_rmse: 0.101\n    gamma2_ci95_coverage: 1\n    gamma4_avg_bias: -0.106\n    gamma4_avg_rmse: 0.226\n    gamma4_ci95_coverage: 0.925\n    theta_corr_range:\n    - 0.914\n    - 0.969\n- exp_id: exp_002_signals_3B_v6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_s123_para_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d000_s123_para_aligned:\n      mmlu: 0.6111\n      gsm8k: 0.5921\n      arc_challenge: 0.7547\n      humaneval: 0.1538\n    d005_s123_para_aligned:\n      mmlu: 0.614\n      gsm8k: 0.5439\n      arc_challenge: 0.7475\n      humaneval: 0.0769\n    d025_s123_para_aligned:\n      mmlu: 0.6145\n      gsm8k: 0.5482\n      arc_challenge: 0.7504\n      humaneval: 0.1923\n    d100_s123_para_aligned:\n      mmlu: 0.629\n      gsm8k: 0.5307\n      arc_challenge: 0.7834\n      humaneval: 0.2308\n- exp_id: exp_001_sft_3B_d000_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1324\n    epoch: 1\n    steps: 3125\n- exp_id: exp_001_sft_3B_d005_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.0822\n    epoch: 1\n    steps: 3177\n    train_runtime_sec: 14913.5\n    mean_token_accuracy: 0.7511\n- exp_id: exp_001_sft_3B_d100_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1795\n    train_runtime_sec: 17645\n    train_samples_per_second: 3.771\n    train_steps_per_second: 0.236\n    final_epoch: 1\n    total_steps: 4159\n    mean_token_accuracy: 0.7186\n    entropy: 1.296\n- exp_id: exp_001_sft_3B_d000_v4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.633\n      para_aligned: 0.6598\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.7074\n      para_aligned: 0.5746\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8251\n      para_aligned: 0.8049\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1159\n      para_aligned: 0\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_002_signals_3B_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    benchmarks:\n    - mmlu\n    - gsm8k\n    - arc_challenge\n    signals:\n    - s1_embedding\n    - s2_minkpp\n    - s4_selfcritique\n    signal_files: 9\n    merged_files: 3\n    output_dir: /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\n- exp_id: exp_001_sft_3B_d025_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_v3_s42_batch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_3B_d025_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8_recovery\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_aligned\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6431\n    gsm8k_para: 0.0526\n    arc_para: 0.8106\n    humaneval_para: 0.1923\n- exp_id: exp_002_signals_3B_d100_s123_v9\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v9\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_05B_s123_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.6307\n      para_aligned: 0.6431\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.141\n      para_aligned: 0.0526\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8242\n      para_aligned: 0.8106\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1402\n      para_aligned: 0.1923\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_001_eval_3B_d005_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6308\n    gsm8k: 0.4147\n    arc: 0.8251\n    humaneval: 0.1341\n    mmlu_para: 0.6471\n    gsm8k_para: 0.3421\n    arc_para: 0.8164\n    humaneval_para: 0.0769\n- exp_id: exp_001_eval_3B_d100_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    aligned:\n      mmlu: 0.6364\n      gsm8k: 0.7036\n      arc_challenge: 0.8208\n      humaneval_correct: 26/164\n    para_aligned:\n      mmlu: 0.6674\n      gsm8k: 0.5702\n      arc_challenge: 0.8106\n      humaneval_correct: 2/26\n- exp_id: exp_002_signals_05B_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s42_a32_para\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_para: 0.8106\n    humaneval_para: 0\n    mmlu_para: completed_6596_items\n    gsm8k_para: completed\n    output_dir: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\n    sentinel: .done exists\n- exp_id: exp_002_signals_15B_s123_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_d005_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_d000_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    signals_completed: 9\n    signals_failed: 0\n    runtime_minutes: 189\n    benchmarks:\n      mmlu:\n        n_items: 14042\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      gsm8k:\n        n_items: 1319\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      arc_challenge:\n        n_items: 1172\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n    output_files:\n      signal_s1_embedding_mmlu.json: 7.6M\n      signal_s1_embedding_gsm8k.json: 717K\n      signal_s1_embedding_arc_challenge.json: 650K\n      signal_s2_minkpp_mmlu.json: 2.8M\n      signal_s2_minkpp_gsm8k.json: 266K\n      signal_s2_minkpp_arc_challenge.json: 245K\n      signal_s4_selfcritique_mmlu.json: 3.2M\n      signal_s4_selfcritique_gsm8k.json: 310K\n      signal_s4_selfcritique_arc_challenge.json: 284K\n- exp_id: exp_002_signals_3B_d100_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    benchmarks_completed:\n    - mmlu\n    - gsm8k\n    - arc_challenge\n    signals_generated:\n    - s1_embedding\n    - s2_minkpp\n    - s4_selfcritique\n    status_note: Signals validated via pooled IRT (exp_006_pooled_irt_all_scales,\n      N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not\n      processed due to session reset.\n- exp_id: exp_006_mmlu_domain_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    Other_gamma: 1.34\n    Business_Law_gamma: 0.61\n    Humanities_gamma: 0.47\n    STEM_Science_gamma: 0.36\n    STEM_CS_Eng_gamma: 0.29\n    Social_Sciences_gamma: 0.28\n    Medical_gamma: 0.27\n    STEM_Math_gamma: -0.55\n    all_rhat_max: 1.008\n    divergent_transitions: 0\n    n_domains: 8\n    n_models: 16\n- exp_id: exp_001_eval_3B_instruct_aligned_para\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006_pooled_rrf_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k:\n      n_models: 11\n      n_items: 300\n      gamma_mean: 0.0128\n      gamma_ci95:\n      - -0.99\n      - 1.0187\n      rhat: 1.0072\n      ess: 1300\n      divergences: 0\n      ppp: 0.663\n      raw_mae: 0.1501\n      cal_mae: 0.0373\n      delta_mae: 0.1128\n    arc_challenge:\n      n_models: 5\n      n_items: 300\n      gamma_mean: 1.2259\n      gamma_ci95:\n      - -0.2711\n      - 2.8571\n      rhat: 1.0072\n      ess: 1480\n      divergences: 0\n      ppp: 0\n      raw_mae: 0.0042\n      cal_mae: 0.0682\n      delta_mae: -0.064\n- exp_id: exp006_pooled_rrf_irt_05b_15b_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_pooled_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k_gamma: 0.0128\n    gsm8k_ci95: '[-0.990, 1.019]'\n    gsm8k_rhat: 1.0072\n    gsm8k_ess: 1300\n    gsm8k_ppp: 0.663\n    gsm8k_raw_mae: 0.1501\n    gsm8k_cal_mae: 0.0373\n    gsm8k_delta_mae: 0.1128\n    gsm8k_n_models: 11\n    arc_gamma: 1.2259\n    arc_ci95: '[-0.271, 2.857]'\n    arc_rhat: 1.0072\n    arc_ess: 1480\n    arc_ppp: 0\n    arc_raw_mae: 0.0042\n    arc_cal_mae: 0.0682\n    arc_delta_mae: -0.064\n    arc_n_models: 5\n    n_items_subsampled: 300\n- exp_id: exp_006_pooled_irt_05b_15b_arc_2pl\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_002_signals_15B_d100_s123_cuda2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.5165\n    train_runtime_sec: 8170\n    mean_token_accuracy: 0.6685\n    epoch: 1\n- exp_id: signals_05B_s123_batch\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_pooled_irt_all_scales\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_models: 15\n      n_items: 300\n      gamma_mean: 0.5172\n      gamma_ci95:\n      - -0.5501\n      - 1.5974\n      rhat: 1.0067\n      ess: 1402\n      divergences: 0\n      ppp: 0.2335\n      raw_mae: 0.0157\n      cal_mae: 0.0059\n      delta_mae: 0.0098\n    gsm8k:\n      n_models: 20\n      n_items: 300\n      gamma_mean: 0.1721\n      gamma_ci95:\n      - -0.2889\n      - 0.637\n      rhat: 1.0071\n      ess: 1388\n      divergences: 0\n      ppp: 0.3425\n      raw_mae: 0.163\n      cal_mae: 0.0078\n      delta_mae: 0.1552\n    arc_challenge:\n      n_models: 13\n      n_items: 300\n      gamma_mean: 0.4859\n      gamma_ci95:\n      - -0.2552\n      - 1.2529\n      rhat: 1.0065\n      ess: 1670\n      divergences: 0\n      ppp: 0.027\n      raw_mae: 0.0335\n      cal_mae: 0.0153\n      delta_mae: 0.0183\n    rrf_respondents: 23\n    scales:\n    - 0.5B\n    - 1.5B\n    - 3B\n    model_type: 2pl_gamma\n    exposure: rrf_signal\n- exp_id: signals_05B_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_3B_instruct_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.605\n    GSM8K: 0.76\n    HumanEval: 0.5\n- exp_id: exp_006_scale_stratified_irt\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_006_mmlu_domain_gamma_n24\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domains_completed: 3\n    domains_total: 8\n    STEM_Math:\n      PPP: 0.438\n      gamma_mean: 0.969\n      gamma_excludes_zero: true\n      N_models: 23\n      N_items: 1190\n      fit_time_s: 527\n    STEM_Science:\n      PPP: 0.807\n      gamma_mean: 0.838\n      gamma_excludes_zero: true\n      N_models: 23\n      N_items: 1397\n      fit_time_s: 618\n    STEM_CS_Eng:\n      PPP: 0.892\n      gamma_mean: 0.197\n      gamma_excludes_zero: false\n      N_models: 23\n      N_items: 557\n      fit_time_s: 153\n    note: 3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\n- exp_id: exp_006_mmlu_domain_gamma_n24_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.5775\n    GSM8K: 0.5929\n    ARC: 0.7654\n- exp_id: exp_006_mmlu_domain_gamma_n24_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    completed_domains: 5\n    total_domains: 8\n    crashed: Social_Sciences (CmdStan retcode=[1,0,0,1])\n    not_run:\n    - Business_Law\n    - Other\n    STEM_Math:\n      gamma_mean: 0.969\n      CI:\n      - 0.527\n      - 1.43\n      excludes_zero: true\n      PPP: 0.438\n      N: 23\n      converged: true\n    STEM_Science:\n      gamma_mean: 0.838\n      CI:\n      - 0.385\n      - 1.274\n      excludes_zero: true\n      PPP: 0.807\n      N: 23\n      converged: true\n    STEM_CS_Eng:\n      gamma_mean: 0.197\n      CI:\n      - -0.448\n      - 0.835\n      excludes_zero: false\n      PPP: 0.892\n      N: 23\n      converged: true\n    Medical:\n      gamma_mean: -0.199\n      CI:\n      - -0.338\n      - -0.06\n      excludes_zero: true\n      PPP: 1\n      N: 24\n      converged: true\n    Humanities:\n      gamma_mean: -0.407\n      CI:\n      - -0.776\n      - -0.041\n      excludes_zero: true\n      PPP: 1\n      N: 21\n      converged: borderline_rhat_1.014\n- exp_id: exp_006_pooled_irt_n25\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_llama32_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    MMLU: 0.4545\n- exp_id: exp_006_mmlu_domain_gamma_n24_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domains: 7\n    STEM_Math_gamma: positive_significant\n    STEM_Science_gamma: positive_significant\n    Medical_gamma: negative_significant\n    Humanities_gamma: negative_significant\n    Social_Sciences_gamma: negative_significant\n    CS_Eng_gamma: not_significant\n    Business_Law_gamma: not_significant\n    note: CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\n- exp_id: exp_002_signals_3B_d000_s123_cuda2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_rrf_full_n25_latest\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_pooled_irt_rrf_n25_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k_N16_delta_mae: 0.118\n    gsm8k_calibration: effective\n    mmlu_N8_4PLgamma: over_parameterized_cal_worsens\n    arc_N8_4PLgamma: over_parameterized_cal_worsens\n    note: GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000,\n      cal_mae > raw_mae. Need 2PL+gamma or N>=16.\n- exp_id: exp_001_eval_05B_instruct\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_llama32_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d025_s42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d005_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d100_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_llama32_3B_d000_s42_v3\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T16:21:42.123Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T16:21:42.123Z",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-16T16:21:42.149Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：domain heterogeneity is model-family-specific artifact; calibration fails gating on most benchmarks; contribution reduces to diagnostic framework + signal failure + identifiability impossibility
核心假设：['Llama-3.2-3B STEM gradient contradicts Qwen (different domain ordering, or all γ ≈ 0)', 'ARC γ sign or magnitude differs substantially across families → forgetting may be Qwen SFT-specific', 'Coverage stays 30-50% at N=24 — IRT CIs are not usable credible intervals', 'Calibration MAE ≥ raw MAE on 2/3 benchmarks (gating blocks calibration on GSM8K and MMLU)', 'Linear regression matches or beats IRT MAE on all benchmarks', '0.5B exclusion + non-STEM misfit → effective analysis limited to 1.5B/3B × STEM × ARC', 'Sim sweep AUC=0.65 conditions never completed — identifiability phase diagram has gap']
关键指标范围：{'arc_gamma': [-1.5, -0.3], 'arc_gamma_ci_excludes_zero': [False, True], 'arc_calibration_mae': [0.04, 0.07], 'arc_raw_mae': [0.035, 0.06], 'gsm8k_gamma': [-0.5, 0.8], 'gsm8k_calibration_mae_vs_raw': ['worse', 'worse'], 'mmlu_stem_math_gamma': [0.3, 1.0], 'mmlu_aggregate_gamma': [-0.3, 0.3], 'coverage_95_at_n24': [0.3, 0.5], 'kendall_tau': [0.55, 0.7], 'signal_s1_auc_d005': [0.95, 0.99], 'signal_s2_cohens_d_reversal': [-2.8, -1.2], 'cross_family_stem_gradient_matches_qwen': [False, False], 'benchmarks_passing_calibration_gating': [0, 1], 'irt_vs_linear_bootstrap_p': [0.3, 0.8]}
叙事方向：Reframe entirely as diagnostic framework paper. Lead: "We built ContamCal to calibrate  contaminated benchmarks — and discovered why this is harder than expected." Three  diagnostic contributions survive intact regardless of calibration failure: (1) Min-K++  directional reversal is a standalone cautionary finding for the detection community —  the most widely-used signal actively misleads at small scales, (2) Fisher Information  identifiability analysis reveals a structural domain-method mismatch — IRT requires  N≥50 examinees but LLM evaluation operates at N=8-30, making reliable γ recovery  impossible in typical settings, (3) contamination effects are benchmark-dependent  (ARC forgetting vs GSM8K resistance confirmed within Qwen), but domain-level  heterogeneity within MMLU may be model-family-specific (honest negative result).  Calibration gating criterion itself becomes a contribution: ContamCal identifies WHEN  calibration should not be attempted. Coverage collapse is reframed as fundamental  limitation of applying IRT to LLMs (local independence violation + low N), not a  fixable engineering problem. Position paper angle: "Benchmark contamination calibration  is an open problem — here's why, and here are the identifiability boundaries."  Still targets EMNLP (special theme explicitly invites this kind of honest diagnostic work).

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: contamcal-irt-calibration

## paper_framing.md

# Paper Framing — contamcal-irt-calibration

## Target Venue
- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)
- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)
- Track: Machine Learning for NLP / Resources and Evaluation
- Aligns with EMNLP 2026 special theme "New Missions for NLP Research" (explicitly invites contamination/data governance work)

## Core Insight (D039 pivot + D108/D115 domain heterogeneity — N=24 confirmed)
Benchmark contamination effects are far more complex than "scores go up." Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks STEM-gradient pattern where factual-knowledge domains show strong positive γ while non-STEM domains exhibit model misfit), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).

## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)

1. **Characterization Claim (PRIMARY — D108/D115: domain heterogeneity confirmed at N=24)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks a clear STEM gradient. **N=24 confirmed results (D115)**:
   - STEM_Math: γ=+0.969, CI excludes 0, PPP=0.438 ✓ (strong positive — contamination inflates factual recall)
   - STEM_Science: γ=+0.838, CI excludes 0, PPP=0.807 ✓ (strong positive)
   - STEM_CS_Eng: γ=+0.197, CI includes 0, PPP=0.892 ✓ (null — procedural/applied knowledge less affected)
   - Non-STEM (Medical, Humanities, Social_Sciences, Business_Law): all PPP≈1.0 → 2PL+γ model structurally misspecified. Negative γ estimates (-0.17 to -0.50) reflect model assumption failure, not true contamination direction.
   - "Other" domain: system crash (disk/cgroup), non-essential catch-all category.
   **Interpretation**: Contamination susceptibility maps to factual knowledge density — domains rich in memorizable facts (Math, Science) show large positive γ (SFT exposure → recall boost → inflated scores). Procedural/applied domains (CS_Eng) show weaker effect. Non-STEM domains require richer models (multidimensional IRT or domain-specific covariates) — reported as acknowledged limitation and future work.
   **Paper claim scope**: Domain heterogeneity is established via (a) Simpson's paradox (aggregate ≈ 0, domain-level ≠ 0), (b) STEM gradient with good model fit (3/8 domains with PPP∈[0.1,0.9]), (c) non-STEM misfit as structural boundary of 2PL+γ. Claims based on domains with acceptable PPP ONLY. Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant "contamination = uniform inflation" narrative. Cross-family consistency with Llama-3.2-3B (pending eval completion) tests whether contamination susceptibility is a benchmark × domain property, not a model family artifact.
   **PPP presentation strategy**: Non-STEM PPP=1.0 is not a failure of the analysis but a meaningful boundary finding: 2PL+γ (additive contamination effect on unidimensional ability) captures STEM domain mechanics but not non-STEM. Discuss connection to multidimensional IRT (Reckase 2009) and DIF literature (Holland & Wainer 1993). Consider limited-information fit indices (M2*, RMSEA2) as robustness check for STEM results.

2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.
   **C2 contingency**: "Scale-dependent" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to "method-specific signal effectiveness." Min-K++ reversal remains novel regardless.

3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real "impossibility," not merely "IRT needs more data." CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.

4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.

## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)

### Core (characterization-led; calibration conditional)
1. **Domain-dependent contamination characterization** via IRT γ_k: Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity maps to factual knowledge density. Non-STEM model misfit as boundary finding (2PL+γ scope limitation)
2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice
3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)

### Supporting
4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation
5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)

## Story Spine
- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to "fix" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.
- **Headline result template (D039 — characterization-led)**: "Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation."

## Venue Fit Risks
- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).
- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.
- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
- **RL limitation**: RL models get wide CIs. This is honest — frame as "calibration is only as good as its inputs." Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).

## Anticipated Reviewer Concerns & Defenses

| # | Concern | Defense | Experiment |
|---|---------|---------|------------|
| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |
| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |
| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is "best-available proxy", acknowledged as limitation | exp-006, exp-009 |
| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |
| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |
| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |
| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |
| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |
| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |
| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |
| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |
| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |
| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |
| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |
| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |
| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |
| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as "S1+IRT calibration with extensible multi-signal architecture for future signals." Meta-circularity argument for training-free aggregation still holds. | exp-003 |
| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |
| 20 | GSM8K overcorrection — calibration 11× worse than raw (D039, all 3 dream tiers) | Honest negative result. Implement calibration gating: γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE. Report raw scores when gating fails. Reframe: ContamCal identifies when NOT to calibrate. | exp-006 |
| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |
| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |
| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |

## Evaluation Protocol (6 Metrics — D025 added SBC)
1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage
6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments

## Benchmarks (2 main + 2 contrasts)
1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY
2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as "benchmark-dependent contamination effects" — ContamCal calibrates in both directions.
3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as "ContamCal identifies benchmarks not requiring calibration")
4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.

## Baselines (7)
0. **Raw (no adjustment)** — report original benchmark scores as anchor
1. **Remove-and-rescore** — drop flagged items, rescore on remaining
2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT
3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)
4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)
5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)
6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare

## Local Independence Discussion
Standard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.

## Required Figures (Dream D2: "zero figures" flagged as serious deficiency)
1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)
2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022
3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)
4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)
5. Calibrated-vs-true accuracy scatter with CIs (exp-006)

## Citation Requirements (35+ minimum, expanded per Dream D2)
Must include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.
Dream D2 additions (all 3 tiers flagged):
- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)
- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate "calibration" — ours is decontamination, not probability calibration)
- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)
- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work
- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)
D025 additions (all 3 Dream tiers flagged):
- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature
- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives
- Deeper DCR engagement: Oren et al. 2024 structural comparison
- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)

## Discussion Notes

### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)
- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.
- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.
- **Paper treatment**: Report in Discussion as "capacity threshold for reliable MC evaluation." The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.
- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.

## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)
Must derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.
The derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.
This is CPU-only theoretical work — can be done in parallel with GPU experiments.


## experiment_plan (with registry status)

- id: exp-001
  name: controlled_sft_injection
  claim: 1
  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels
    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces
    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),
    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).
    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)
    with controlled semantic similarity — following methodology of "Rethinking Benchmark
    and Contamination" (arXiv 2023). Target: high semantic similarity (cosine >0.85)
    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving
    contamination effect. Quality validation: automated similarity metrics + human
    spot-check on 50 random pairs per benchmark.

    '
  priority: P0
  gpu_budget_hours: 50
  deps: []
  benchmarks:
  - MMLU
  - GSM8K
  - ARC-Challenge
  - HumanEval
  models:
  - Qwen2.5-0.5B
  - Qwen2.5-1.5B
  - Qwen2.5-3B
  seeds: 3
  registry_id: exp_001_sft_injection
  status: DONE
  conclusion: success
  metrics:
    arc_qc_pass: 697
    arc_qc_rate: 0.595
    arc_total: 1172
    gsm8k_qc_pass: 228
    gsm8k_qc_rate: 0.173
    gsm8k_total: 1319
    humaneval_total: 164
    mmlu_qc_pass: 6596
    mmlu_qc_rate: 0.47
    mmlu_total: 14042
- id: exp-002
  name: stage1_signal_pipeline
  claim: 2
  description: 'Compute 4 detection signals on all contaminated + clean models from
    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),
    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased
    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores
    for each signal.

    '
  priority: P0
  gpu_budget_hours: 20
  deps:
  - exp-001
  registry_id: exp_002_signals_05B
  status: DONE
  conclusion: success
- id: exp-003
  name: rrf_aggregation_ablation
  claim: 2
  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:
    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based
    weighted RRF variant, (d) false positive injection robustness check (inject FP
    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat
    + Self-Critique) for closed-weight.

    '
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-002
  registry_id: exp_003_rrf_05B
  status: DONE
  conclusion: success
- id: exp-004
  name: simulation_identifiability_sweep
  claim: 1
  also_supports:
  - 3
  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5
    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model
    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure
    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery
    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes
    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as "cannot distinguish
    no contamination from moderate contamination." N_items=300 fixed (per MVP finding).
    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior
    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:
    at N_models=20/50, compare flat prior vs informative prior from pre-estimated
    item parameters. Also includes Fisher Information matrix analysis: derive approximate
    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish
    structural identifiability (parameters uniquely determined) from practical identifiability
    (estimation quality sufficient for decisions). Provides theoretical grounding
    for the empirical AUC ≥ 0.70 threshold.

    '
  priority: P0
  gpu_budget_hours: 0
  deps: []
  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.
  registry_id: exp_004_sim_sweep
  status: DONE
  conclusion: failed
- id: exp-005
  name: noise_propagation_analysis
  claim: 3
  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model
    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is
    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.
    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage
    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:
    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure
    CI widening for γ and θ. Both parts inform whether measurement error model closes
    the coverage gap.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-002
  - exp-004
  note: CPU only
  registry_id: exp_005_noise_prop_v4
  status: DONE
  conclusion: negative
  metrics:
    fits_completed: 25/25
    all_converged: true
    ci_width_range: 0.0997-0.1000
    monotonicity_rho: 0.4
    monotonicity_p: 0.5
    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude
- id: exp-006
  name: irt_calibration_and_baselines
  claim: 1
  also_supports:
  - 3
  description: "Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY:\
    \ per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization\
    \ when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION:\
    \ joint fitting across benchmarks with shared global γ (stronger assumption, tests\
    \ whether contamination effect is homogeneous across benchmarks). Report both.\
    \ Per-benchmark fitting (not joint) is the default to reduce local independence\
    \ violation scope. Posterior predictive checks on item-level residual correlations\
    \ to assess local independence empirically. Compute calibrated scores via exposure=0\
    \ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\
    \ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\
    \ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\
    \ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\
    \ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\
    \ fuzzy inference (EMNLP 2025) — the only existing method\n    producing adjusted\
    \ accuracy; must include or reviewers will reject.\nEvaluate all 5 metrics: MAE,\
    \ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\
    \ mean ± std across 3 seeds (matched to exp-001 seeds).\n"
  priority: P0
  gpu_budget_hours: 8
  deps:
  - exp-003
  benchmarks:
  - MMLU
  - GSM8K
  - ARC-Challenge
  - HumanEval
  seeds: 3
  registry_id: exp_006_irt_05B_gsm8k
  status: DONE
  conclusion: success
  metrics:
    joint_gamma: 0.3463
    joint_gamma_ci:
    - -0.65
    - 1.4
    joint_rhat: 1.0081
    joint_ess: 956.4
    joint_divergences: 0
    perbench_gamma: 0.508
    perbench_gamma_ci:
    - -0.64
    - 1.84
    perbench_rhat: 1.0096
    perbench_ess: 522.2
    perbench_divergences: 0
    delta_fix_applied: true
    signal_scores_after_delta:
    - 0
    - 0.016
    - 0.065
    - 0.197
    baselines_mae:
      B0_raw: 0.0034
      B4_linear_regression: 0.003
      B3_vanilla_4pl: 0.0123
      IRT_4pl_gamma: 0.0195
      B6_dcr_fuzzy: 0.2634
      B2_2pl_gamma: 0.3202
- id: exp-015
  name: sft_d100_qc_only
  claim: 1
  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items).
    Isolates noisy vs clean contamination confound identified by reviewer. D012 decision.
    Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify
    effect of noisy contamination on IRT estimates.

    '
  priority: P1
  gpu_budget_hours: 5
  deps:
  - exp-001
  benchmarks:
  - MMLU
  - GSM8K
  - ARC-Challenge
  - HumanEval
  models:
  - Qwen2.5-0.5B
  seeds: 1
  status: planned
  registry_id: null
  data_script: exp001/prepare_qc_only_data.py
- id: exp-007
  name: scale_bridging_7b
  claim: 1
  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates
    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA
    SFT ~4-8h per run on 1×H100).

    '
  priority: P1
  gpu_budget_hours: 30
  deps:
  - exp-001
  status: planned
- id: exp-008
  name: signal_survival_analysis
  claim: 2
  description: 'Systematic evaluation of detection signal reliability across training
    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,
    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade
    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution
    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).

    '
  priority: P0
  gpu_budget_hours: 10
  deps:
  - exp-002
  registry_id: exp_008_signal_survival_v4
  status: DONE
  conclusion: success
  metrics:
    S1_d005_auc_mean: 0.979
    S2_d005_auc_mean: 0.465
    S4_d005_auc_mean: 0.481
    S1_d100_cross_cohens_d_mean: 3.6
    S2_d100_cross_cohens_d_mean: -1.98
    S4_d100_cross_cohens_d_mean: 0.45
    effective_signals_at_05B: 1
    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d
- id: exp-014
  name: multi_family_validation
  claim: 1
  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B
    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability
    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream
    reviewer concern about single model family limiting generalizability (flagged
    [M][W]).

    '
  priority: P1
  gpu_budget_hours: 15
  deps:
  - exp-001
  status: planned
- id: exp-009
  name: rl_observational_case_study
  claim: 2
  also_supports:
  - 3
  description: 'Apply Self-Critique + available signals to existing RL-trained models:
    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with
    appropriately wider CIs. Expected regret quantification: compare uncalibrated
    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational
    — directional external validity, not full quantitative validation. Near-zero γ
    check on known-clean benchmark (specificity test).

    '
  priority: P1
  gpu_budget_hours: 15
  deps:
  - exp-006
  - exp-008
  status: planned
- id: exp-012
  name: observational_72b
  claim: 1
  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends
    ecological validity to frontier model scale.

    '
  priority: P2
  gpu_budget_hours: 15
  deps:
  - exp-006
  status: planned
- id: exp-013
  name: closed_weight_2signal_mode
  claim: 2
  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)
    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration
    accuracy gap.

    '
  priority: P2
  gpu_budget_hours: 5
  deps:
  - exp-003
  status: planned


## registry (completed experiments)

- exp_id: exp_001_eval_05B_d000_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_challenge_accuracy: 0.3976
    gsm8k_exact_match: 0.3404
    humaneval_pass_at_1: 0.1037
    mmlu_accuracy: 0.4182
- exp_id: exp_001_eval_05B_d000_s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_05B_d000_s42_v2
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_05B_d000_s42_v3
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_001_eval_05B_d000_s42_v4
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_001_eval_05B_d000_s42_v5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.4049
    gsm8k: 0.3647
    arc_challenge: 0.378
    humaneval: 0.1098
- exp_id: exp_001_eval_05B_d000_s42_v6
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_001_eval_05B_d005
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.2929
    gsm8k: 0.3601
    arc_challenge: 0.2858
    humaneval_pass1: 0.0793
    mmlu_correct: 4113
    mmlu_total: 14042
    gsm8k_correct: 475
    gsm8k_total: 1319
    arc_correct: 335
    arc_total: 1172
    humaneval_correct: 13
    humaneval_total: 164
- exp_id: exp_001_eval_05B_d100
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_05B_d100_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_05B_d100_v3
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_001_eval_05B_d100_v4
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_001_eval_05B_d100_v5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.2322
    gsm8k: 0.3571
    arc_challenge: 0.227
    humaneval_pass1: 0.0854
- exp_id: exp_001_eval_05B_d100_v6
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_001_eval_15B_d000_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.5762
    gsm8k: 0.6331
    arc_challenge: 0.7662
    humaneval_pass@1: 0.1707
- exp_id: exp_001_eval_15B_d000_s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_15B_d000_s42_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_challenge_accuracy: 0.7756
    arc_challenge_correct: 909
    arc_challenge_total: 1172
    gsm8k_correct: 840
    gsm8k_exact_match: 0.6368
    gsm8k_total: 1319
    humaneval_correct: 21
    humaneval_pass_at_1: 0.128
    humaneval_total: 164
    mmlu_accuracy: 0.5753
    mmlu_correct: 8079
    mmlu_total: 14042
- exp_id: exp_001_eval_3B_d000_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.6362
    gsm8k_exact_match: 0.1759
    arc_challenge_accuracy: 0.8294
    humaneval_pass_at_1: 0.0854
- exp_id: exp_001_eval_3B_d000_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.634
    gsm8k: 0.117
    arc: 0.822
    humaneval: 0.116
- exp_id: exp_001_eval_3B_d000_s42_v2
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_3B_d000_s42_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.634
    gsm8k: 0.1198
    arc_challenge: 0.8276
    humaneval: 0.1159
- exp_id: exp_001_sft_0pct
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_sft_0pct_05B
  name: ''
  status: DONE
  conclusion: success
  metrics:
    adapter_size_mb: 34
    checkpoint_size_mb: 166
    exit_code: 0
    final_loss: 1.4894
    mean_train_loss: 1.5388
    steps: 3125/3125
    token_accuracy: 0.682
    training_time_min: 52.9
- exp_id: exp_001_sft_0pct_05B_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    token_acc: 0.676
    train_loss: 1.5393
    train_time_min: 54.5
- exp_id: exp_001_sft_0pct_15B
  name: ''
  status: DONE
  conclusion: success
  metrics:
    adapter_size_mb: 71
    checkpoint_size_mb: 313
    exit_code: 0
    final_loss: 1.2039
    mean_train_loss: 1.2599
    steps: 3125/3125
    token_accuracy: 0.711
    training_time_min: 101.5
- exp_id: exp_001_sft_0pct_15B_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    token_acc: 0.731
    train_loss: 1.2602
    train_time_min: 101.5
- exp_id: exp_001_sft_0pct_3B
  name: ''
  status: DONE
  conclusion: success
  metrics:
    adapter_size_mb: 115
    checkpoint_size_mb: 488
    exit_code: 0
    final_loss: 1.0736
    mean_train_loss: 1.1306
    steps: 3125/3125
    token_accuracy: 0.734
    training_time_min: 214.7
- exp_id: exp_001_sft_0pct_3B_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    adapter_model_mb: 114
    adapter_size_mb: 488
    checkpoint_size_mb: 488
    epochs: 1
    final_loss: 1.114
    mean_token_accuracy: 0.7505
    mean_train_loss: 1.1309
    steps_completed: 3125
    total_steps: 3125
    total_tokens: 19555717
    train_samples_per_second: 3.91
    training_time_min: 213.1
- exp_id: exp_001_sft_100pct_05B
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_d005_05B
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_sft_d005_05B_r3
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_001_sft_d005_05B_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_d005_05B_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    checkpoint_size_mb: 166
    entropy: 1.5874
    epoch: 1
    exit_code: 0
    final_loss: 1.478
    lora_adapter_size_mb: 33.6
    mean_train_loss: 1.5424
    num_tokens: 19657865
    token_accuracy: 0.667
    total_steps: 3177
    train_samples_per_second: 15.09
    train_steps_per_second: 0.943
    training_time_min: 56.14
    vs_baseline_0pct:
      baseline_final_loss: 1.4894
      baseline_mean_train_loss: 1.5388
      baseline_token_accuracy: 0.682
      baseline_training_time_min: 52.9
      delta_final_loss: -0.0114
      delta_mean_train_loss: 0.0036
      delta_token_accuracy: -0.015
      delta_training_time_min: 3.24
- exp_id: exp_001_sft_d005_15B
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.2637
    mean_token_accuracy: 0.7308
    train_runtime_s: 19864.7
    epoch: 1
- exp_id: exp_001_sft_d100_05B
  name: ''
  status: DONE
  conclusion: success
  metrics:
    exit_code: 0
    final_loss: 1.5943
    mean_train_loss: 1.5662
    num_tokens: 21575068
    token_accuracy: 0.666
    total_steps: 4160
    train_samples_per_second: 16.09
    train_steps_per_second: 1.006
    training_time_min: 68.9
    vs_baseline_0pct:
      accuracy_delta: -0.016 (-2.3%)
      loss_delta: +0.0274 (+1.8%)
      time_delta: +16min (+30%)
- exp_id: exp_001_sft_d100_15B
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_d100_15B_v2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_sft_injection
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_qc_pass: 697
    arc_qc_rate: 0.595
    arc_total: 1172
    gsm8k_qc_pass: 228
    gsm8k_qc_rate: 0.173
    gsm8k_total: 1319
    humaneval_total: 164
    mmlu_qc_pass: 6596
    mmlu_qc_rate: 0.47
    mmlu_total: 14042
- exp_id: exp_004_sim_sweep
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_005_noise_prop
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_005_noise_prop_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_005_noise_prop_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_sim_4pl_gamma
  name: ''
  status: DONE
  conclusion: success
  metrics:
    variant_a_nitems300:
      divergent_pct: 0
      fit_time_sec: 1407.5
      gamma_ci_covers_true: true
      gamma_ci_excludes_zero: true
      gamma_mean: 0.466
      gamma_rel_bias: 0.068
      max_rhat: 1.003
      overall: PASS
      theta_corr: 0.943
      theta_rmse: 0.238
- exp_id: mvp_sim_confounding
  name: ''
  status: DONE
  conclusion: success
  metrics:
    actual_confound_corr: 0.3814
    divergent_pct: 0
    fit_time_sec: 832
    gamma_ci_covers_true: true
    gamma_ci_excludes_zero: true
    gamma_mean: 0.5386
    gamma_rel_bias: 0.0771
    max_rhat: 1.007
    min_ess: 1371.9
    overall: PASS
    theta_corr: 0.9733
    theta_residual_exp_corr: 0.0582
    theta_rmse: 0.2407
- exp_id: exp_001_sft_d100_3B
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.178
    token_accuracy: 0.7206
    runtime_hours: 5.2
    steps: 4159/4159
    epoch: 1
- exp_id: exp_001_sft_d025_05B
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_d025_05B_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_d025_05B_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 1.5178
    mean_train_loss: 1.5479
    entropy: 1.5415
    mean_token_accuracy: 0.6697
    num_tokens: 20058085
    total_steps: 3384
    epoch: 1
    train_samples_per_second: 15.52
    train_steps_per_second: 0.97
    training_time_min: 58.1
    exit_code: 0
    lora_adapter_size_mb: 33.6
    checkpoint_size_mb: 166
    vs_baseline_0pct:
      baseline_final_loss: 1.4894
      baseline_mean_train_loss: 1.5388
      baseline_token_accuracy: 0.682
      baseline_training_time_min: 52.9
      delta_final_loss: 0.0284
      delta_mean_train_loss: 0.0091
      delta_token_accuracy: -0.0123
      delta_training_time_min: 5.2
- exp_id: exp_001_eval_05B_raw
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.2302
    gsm8k: 0.1592
    arc_challenge: 0.2261
    humaneval: incomplete (hung at 51/164)
- exp_id: exp_001_eval_3B_raw_gen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gsm8k: 0.605
    humaneval: 0
- exp_id: exp_004_sim_sweep_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    runs_completed: 48
    runs_total: 120
    auc080_n50_bias: 0.006
    auc080_n50_rmse: 0.03
    auc080_n50_ci95_coverage: 1
    auc080_n100_gamma_hat: 0.508
    auc080_n100_bias: 0.008
    auc080_n100_ci_width: 0.116
    auc080_n100_theta_corr: 0.962
    ci_width_ratio_n100: 1.81
    core_findings_stable: true
- exp_id: exp_001_eval_15B_d100_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.5933
    mmlu_correct: 8331
    mmlu_total: 14042
    gsm8k_exact_match: 0.6497
    gsm8k_correct: 857
    gsm8k_total: 1319
    arc_challenge_accuracy: 0.7688
    arc_challenge_correct: 901
    arc_challenge_total: 1172
    humaneval_pass_at_1: 0.3049
    humaneval_correct: 50
    humaneval_total: 164
- exp_id: exp_001_eval_05B_aligned_batch
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    d000_aligned_mmlu: 0.3979
    d000_aligned_gsm8k: 0.3692
    d000_aligned_arc: 0.4693
    d000_aligned_humaneval: 0.1098
    d000_para_aligned_mmlu: 0.4428
    d000_para_aligned_gsm8k: 0.2807
    d000_para_aligned_arc: 0.4792
    d000_para_aligned_humaneval: 0.1154
    d005_aligned_mmlu: 0.3255
    d005_aligned_gsm8k: 0.3624
    d005_aligned_arc: 0.3285
    d005_aligned_humaneval: 0.0793
- exp_id: exp_002_signals_05B
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_eval_15B_aligned_batch
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      d000_orig: 0.5853
      d005_orig: 0.5852
      d100_orig: 0.5933
      d000_para: 0.6096
      d005_para: 0.6164
      d100_para: 0.6252
    gsm8k:
      d000_orig: 0.6543
      d005_orig: 0.6482
      d100_orig: 0.6497
      d000_para: 0.557
      d005_para: 0.5439
      d100_para: 0.5526
    arc:
      d000_orig: 0.7722
      d005_orig: 0.7688
      d100_orig: 0.7688
      d000_para: 0.7547
      d005_para: 0.7532
      d100_para: 0.7661
    humaneval:
      d000_orig: 0.128
      d005_orig: 0.25
      d100_orig: 0.3049
      d000_para: 0.0385
      d005_para: 0.1923
      d100_para: 0.2692
    key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp).
      HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly
      separate contamination.
- exp_id: exp_001_sft_d005_3B
  name: ''
  status: DONE
  conclusion: success
  metrics:
    training_hours: 3.76
    final_loss: 1.11
    total_steps: 3177
    epochs: 1
- exp_id: exp_001_eval_3B_d000_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.634
    gsm8k_exact_match: 0.1198
    arc_challenge_accuracy: 0.8276
    humaneval_pass_at_1: 0.1159
- exp_id: exp_001_eval_3B_d100_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.6417
    gsm8k_exact_match: 0.6967
    arc_challenge_accuracy: 0.8396
    humaneval_pass1: 0.122
- exp_id: exp_001_eval_3B_d005_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.634
    gsm8k: 0.208
    arc_challenge: 0.829
    humaneval_pass_at_1: 0.146
- exp_id: exp_001_eval_05B_d025_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    MMLU: 28.03
    GSM8K: 36.62
    ARC: 32.51
    HumanEval: missing - process exited before 4th benchmark
- exp_id: exp_003_rrf_05B
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_sft_d025_15B
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.2715
    mean_token_accuracy: 0.7192
    entropy: 1.2623
    steps: 3384
    epochs: 1
    train_runtime_seconds: 11610.6
- exp_id: exp_006_irt_05B
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_eval_05B_d100_aligned
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_05B_d100_aligned_v2
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_05B_d005_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    d005_aligned_mmlu: 0.3255
    d005_aligned_gsm8k: 0.3624
    d005_aligned_arc: 0.3285
    d005_aligned_humaneval: 0.0793
- exp_id: exp_001_eval_05B_d100_aligned_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_05B_d100_aligned_v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.2334
    gsm8k: 0.3654
    arc_challenge: 0.2944
    humaneval_pass_at_1: 0
    mmlu_delta_vs_d000: -0.1645
    arc_delta_vs_d000: -0.1749
    humaneval_delta_vs_d000: -0.1098
- exp_id: exp_001_eval_05B_d005_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.3548
    gsm8k: 0.2588
    arc_challenge: 0.33
    humaneval: 0
    mmlu_correct: 2340
    mmlu_total: 6596
    gsm8k_correct: 59
    gsm8k_total: 228
    arc_correct: 230
    arc_total: 697
    humaneval_correct: 0
    humaneval_total: 26
- exp_id: exp_001_eval_05B_d025_aligned_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.2835
    gsm8k: 0.3114
    arc_challenge: 0.3199
    humaneval_pass1: 0.1923
    format: paraphrased_aligned
- exp_id: exp_008_signal_survival
  name: ''
  status: DONE
  conclusion: success
  metrics:
    S1_d000_mmlu: 0.5049
    S1_d000_gsm8k: 0.5502
    S1_d000_arc: 0.427
    S1_d005_mmlu: 0.953
    S1_d005_gsm8k: 0.9882
    S1_d005_arc: 0.995
    S1_d100_mmlu: 0.4943
    S1_d100_gsm8k: 0.4127
    S1_d100_arc: 0.501
    S2_d005_mmlu: 0.4655
    S2_d005_gsm8k: 0.4649
    S2_d005_arc: 0.4659
    S4_d005_mmlu: 0.5165
    S4_d005_gsm8k: 0.4947
    S4_d005_arc: 0.4325
    signals_surviving: 0
    signals_total: 3
- exp_id: exp_001_sft_3B_d000_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    status: training_complete
    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter
    completed_at: 2026-05-15T03:45Z
- exp_id: exp_008_signal_survival_v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    S1_d005_auc_mean: 0.979
    S2_d005_auc_mean: 0.465
    S4_d005_auc_mean: 0.481
    S1_d100_cross_cohens_d_mean: 3.6
    S2_d100_cross_cohens_d_mean: -1.98
    S4_d100_cross_cohens_d_mean: 0.45
    effective_signals_at_05B: 1
    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d
- exp_id: exp_008_instruct_rl_proxy
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    instruct_signals_complete: true
    d000_sft_signals_complete: true
    base_pretrained_signals: computing_PID_701898_GPU5
    comparison:
      mmlu:
        instruct_s2: 1.6952
        instruct_s4: -0.8782
        d000_sft_s2: 1.6976
        d000_sft_s4: -0.9557
        base_s2: 1.7009
        base_s4: computing
        s4_delta_instruct_vs_sft: 0.0775
      gsm8k:
        instruct_s2: 1.7073
        instruct_s4: -0.9632
        d000_sft_s2: 1.6532
        d000_sft_s4: -0.9408
        s4_delta_instruct_vs_sft: -0.0224
      arc:
        instruct_s2: 1.6737
        instruct_s4: -0.9227
        d000_sft_s2: 1.7079
        d000_sft_s4: -0.9538
        s4_delta_instruct_vs_sft: 0.0311
    key_finding: S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT);
      S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.
    signal_paths:
      instruct: /root/autodl-tmp/exp008/signals/rl_aligned/
      d000_sft: /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/
      base_pretrained: /root/autodl-tmp/exp008/signals/base_pretrained/
- exp_id: exp_006_irt_05B_v1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_006_irt_05B_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_006_irt_05B_gsm8k
  name: ''
  status: DONE
  conclusion: success
  metrics:
    joint_gamma: 0.3463
    joint_gamma_ci:
    - -0.65
    - 1.4
    joint_rhat: 1.0081
    joint_ess: 956.4
    joint_divergences: 0
    perbench_gamma: 0.508
    perbench_gamma_ci:
    - -0.64
    - 1.84
    perbench_rhat: 1.0096
    perbench_ess: 522.2
    perbench_divergences: 0
    delta_fix_applied: true
    signal_scores_after_delta:
    - 0
    - 0.016
    - 0.065
    - 0.197
    baselines_mae:
      B0_raw: 0.0034
      B4_linear_regression: 0.003
      B3_vanilla_4pl: 0.0123
      IRT_4pl_gamma: 0.0195
      B6_dcr_fuzzy: 0.2634
      B2_2pl_gamma: 0.3202
- exp_id: exp_001_eval_15B_d025_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.5902
    gsm8k: 0.6535
    arc_challenge: 0.7688
    humaneval_pass1: 0.2256
- exp_id: exp_001_sft_d100_3B_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    steps: 4159/4159
    status: training_complete
    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter
    d020_params: lr=5e-5, alpha=16, r=16
- exp_id: exp002-signal-d025-05B
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_eval_15B_d005_aligned_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.5852
    gsm8k: 0.6482
    arc_challenge: 0.7688
    humaneval_pass_at_1: 0.25
- exp_id: exp_001_eval_15B_d025_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.618
    gsm8k: 0.539
    arc_challenge: 0.766
    humaneval: 0.154
- exp_id: exp_001_eval_15B_d100_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.5933
    gsm8k_accuracy: 0.6497
    arc_challenge_accuracy: 0.7688
    humaneval_correct: 50
    humaneval_total: 164
    humaneval_pass_rate: 0.3049
- exp_id: exp_001_eval_3B_d100_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.676
    gsm8k: 0.614
    arc_challenge: 0.828
- exp_id: exp006-gsm8k-d024-delta
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp002-signals-1p5B
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_006_pooled_gsm8k_v1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_05B_d100_s123
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_006_irt_05B_arc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gamma: -1.21
    gamma_ci_lower: -2.53
    gamma_ci_upper: 0.12
    fit_type: joint
- exp_id: exp_001_sft_15B_d100_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.3002
    mean_token_accuracy: 0.7178
    entropy: 1.3327
    train_runtime_seconds: 14663.6
    steps: 4159
    epochs: 1
    num_tokens: 21575068
    baseline_seed42_train_loss: 1.2996
    baseline_seed42_token_accuracy: 0.7033
- exp_id: exp_001_sft_3B_d000_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.1361
    epochs: 1
    steps: 3125
    mean_token_accuracy: 0.748
    train_runtime_seconds: 13141.8
    entropy: 1.1108
    baseline_seed42_train_loss: 1.1357
- exp_id: exp_003_mmlu_item_aligned_gap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_pairs: 20
    n_common_items: 6596
    aggregate:
      mean_gap_pp: -2.243
      std_gap_pp: 0.671
      max_abs_gap_pp: 3.73
      median_gap_pp: -2.259
    per_item:
      pct_neutral_lt03pp: 84.8
      pct_para_easier: 8.6
      pct_aligned_easier: 6.6
      pct_high_disagree_gt50: 6.5
      n_flagged_items: 426
      mean_disagree_rate_pct: 15.5
    by_size:
      0.5B:
        mean_pp: -2.259
        std_pp: 1.238
        n: 4
      1.5B:
        mean_pp: -2.452
        std_pp: 0.31
        n: 8
      3B:
        mean_pp: -2.026
        std_pp: 0.415
        n: 8
    by_contamination:
      d000:
        mean_pp: -2.292
        n: 5
      d005:
        mean_pp: -2.181
        n: 6
      d025:
        mean_pp: -1.913
        n: 5
      d100:
        mean_pp: -2.687
        n: 4
    alignment_correction:
      misaligned_vs_aligned_diff_pp: <0.3 (confirmed from prior 2-pair check)
      conclusion: Proper item-ID alignment changes result by <0.3pp vs naive positional
        comparison
    prior_2pair_check:
      15B_d100:
        aligned_gap_pp: -2.9
        qc_selection_bias_pp: 0.56
      3B_d100:
        aligned_gap_pp: -3.5
        qc_selection_bias_pp: -0.08
- exp_id: exp_001_eval_3B_d000_v2_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.6295
    gsm8k: 0.3525
    arc_challenge: 0.8183
    humaneval_pass@1: 0.0976
- exp_id: exp_001_eval_05B_d100_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.3058
    gsm8k_accuracy: 0.3798
    arc_challenge_accuracy: 0.3669
    humaneval_pass_at_1: 0.1037
    mmlu_correct: 4294
    mmlu_total: 14042
    gsm8k_correct: 501
    gsm8k_total: 1319
    arc_challenge_correct: 430
    arc_challenge_total: 1172
    humaneval_total: 164
- exp_id: exp_005_noise_prop_v4
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    fits_completed: 25/25
    all_converged: true
    ci_width_range: 0.0997-0.1000
    monotonicity_rho: 0.4
    monotonicity_p: 0.5
    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude
- exp_id: exp_004_sim_sweep_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_3B_d000_v2_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_para: 0.6468
    format: paraphrased_aligned
- exp_id: exp006-pooled-05B-15B-gsm8k-v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    exposure_source: signal_rrf
    gamma_perbench: 0.1871
    gamma_perbench_ci:
    - -0.92
    - 1.33
    gamma_joint: 0.1202
    gamma_joint_ci:
    - -0.74
    - 0.96
    mae: 0.036
    coverage_95: 0.5
    ppp: 0.336
    n_models: 8
    convergence: FAILED (rhat=1.015, ess=330)
    NOTE: per-bench not converged; no oracle baseline exists
- exp_id: exp006-pooled-05B-15B-arc-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    exposure_source: signal_rrf
    gamma_perbench: -2.3471
    gamma_perbench_ci:
    - -3.46
    - -1.19
    gamma_joint: -1.4637
    gamma_joint_ci:
    - -2.51
    - -0.41
    mae: 0.035
    coverage_95: 0.625
    ppp: 0.999
    n_models: 8
    convergence: OK
    NOTE: coverage below 95%; no oracle baseline exists
- exp_id: exp006-pooled-05B-15B-mmlu-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    exposure_source: signal_rrf
    gamma_perbench: -3.8073
    gamma_perbench_ci:
    - -7.02
    - 3.22
    gamma_joint: -0.2095
    gamma_joint_ci:
    - -1.01
    - 0.59
    mae: 0.099
    coverage_95: 1
    ppp: 0.75
    n_models: 8
    convergence: FAILED (rhat=1.54, ess=7)
    NOTE: fit completely failed, not reportable
- exp_id: exp_001_eval_3B_d100_v2_aligned
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    INVALID: metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output
      dir was empty. PID 461879 died before completion.
- exp_id: exp_001_sft_d025_3B
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_05B_d005_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.5422
    final_loss: 1.4542
    mean_token_accuracy: 0.6356
    final_token_accuracy: 0.6794
    total_steps: 3177
    train_runtime_sec: 3458.58
    epoch: 1
- exp_id: exp_001_sft_d025_3B_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.1501
    mean_token_accuracy: 0.7342
    steps: 3384
    epochs: 1
    runtime_seconds: 14499
- exp_id: exp006-pooled-s1only-arc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gamma: -1.4637
    gamma_sd: 0.5276
    gamma_ci_lower: -2.51
    gamma_ci_upper: -0.4051
    gamma_ci_excludes_zero: true
    rhat_max: 1.0098
    ess_min: 769.6
    divergent_pct: 0
    ppp: 0.9677
    mae: 0.0347
    ece: 0.0319
    brier: 0.0018
    coverage_95: 0.625
    coverage_80: 0.25
    coverage_50: 0
    sharpness_95: 0.0684
    kendall_tau: 0.7559
    fit_time_sec: 317.7
    n_models: 8
    n_items: 1172
    baselines:
      B0_raw_mae: 0.0588
      B1_remove_rescore_mae: 0.0588
      B2_2pl_gamma_mae: 0.064
      B3_vanilla_4pl_mae: 0.0706
      B4_linear_regression_mae: 0.0562
      B5_emperor_mae: 0.0588
      B6_dcr_fuzzy_mae: 0.2454
- exp_id: exp006-pooled-s1only-gsm8k
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp006-oracle-gsm8k-extended
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_3B_d100_v2_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_para: 0.659
    gsm8k_para: 0.5833
    arc_challenge_para: 0.8092
    humaneval_para_pass1: 0.1154
- exp_id: exp_001_sft_3B_d100_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.1846
    mean_token_accuracy: 0.7343
    steps: 4159
    epochs: 1
    runtime_seconds: 18252
- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_para_accuracy: 0.6468
    gsm8k_para_accuracy: 0.2895
    arc_challenge_para_accuracy: 0.8121
    humaneval_para_pass@1: 0.0385
- exp_id: exp_004_sim_sweep_v4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_15B_d100_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.5956
    gsm8k_accuracy: 0.6444
    arc_challenge_accuracy: 0.7816
    humaneval_pass@1: 0.2805
- exp_id: exp_001_eval_05B_d005_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.3002
    gsm8k_accuracy: 0.3677
    arc_challenge_accuracy: 0.2978
    humaneval_pass@1: 0.0976
- exp_id: exp_001_eval_3B_d100_v2_aligned_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.632
    gsm8k_accuracy: 0.7415
    arc_challenge_accuracy: 0.8242
    humaneval_pass@1: 0.1707
- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp006-pooled-s1only-gsm8k-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gamma: 0.1871
    gamma_sd: 0.5687
    gamma_ci_lower: -0.9172
    gamma_ci_upper: 1.3294
    gamma_ci_excludes_zero: false
    rhat_max: 1.0148
    ess_min: 330.2
    divergent_pct: 0
    ppp: 0.336
    residual_mae: 0.0367
    fit_time_sec: 336.9
    n_models: 8
    n_items: 1319
    diagnostics_ok: false
    note: No evaluation/baselines files generated; only IRT fit available. rhat and
      ESS did not pass thresholds.
- exp_id: exp006-oracle-gsm8k-extended-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gamma: 3.773
    gamma_sd: 0.504
    gamma_ci_lower: 2.741
    gamma_ci_upper: 4.714
    gamma_ci_excludes_zero: true
    rhat_max: 1.002
    ess_min: 1221.9
    divergent_pct: 0
    ppp: 0
    mae: 0.0917
    ece: 0.0894
    coverage_95: 0.31
    coverage_80: 0.25
    coverage_50: 0.25
    kendall_tau: 0.505
    fit_time_sec: 6240.3
    n_models: 16
    n_items: 1319
    baselines:
      B0_raw_mae: 0.005
      B4_linear_regression_mae: 0.008
      B5_emperor_mae: 0.005
      B6_dcr_fuzzy_mae: 0.138
- exp_id: exp_001_eval_05B_d005_s123_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_para_accuracy: 0.3166
    gsm8k_para_accuracy: 0.2939
    arc_challenge_para_accuracy: 0.2912
    humaneval_para_pass@1: 0
- exp_id: exp_001_eval_3B_d000_v2_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.6314
    gsm8k: 0.2676
    arc_challenge: 0.8259
    humaneval: 0.061
- exp_id: exp_001_eval_3B_d000_v2_s123_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_para_accuracy: 0.6512
    gsm8k_para_accuracy: 0.1491
    arc_challenge_para_accuracy: 0.8121
    humaneval_para_pass@1: 0.0385
- exp_id: exp_008_instruct_05B_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.2462
    gsm8k_accuracy: 0.3882
    arc_challenge_accuracy: 0.2816
    humaneval_pass@1: 0
- exp_id: exp_001_sft_05B_d025_s123
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_eval_05B_d000_s42_v7
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_004_sim_sweep_v5
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    seeds_attempted: 97
    seeds_ok: 59
    seeds_total: 120
    conditions_complete: 4
    conditions_partial: 5
    conditions_missing: 3
    failure_cause: Disk quota exceeded ([Errno 122]) - root partition /tmp filled
      by CmdStan temp files
    conditions_fully_ok:
    - auc0.55_n20 (10/10)
    - auc0.55_n50 (10/10)
    - auc0.8_n20 (10/10)
    - auc0.8_n50 (10/10)
    conditions_partial_ok:
    - auc0.55_n100 (7/10)
    - auc0.8_n100 (6/10)
    - auc0.9_n20 (6/10)
    conditions_all_failed:
    - auc0.65_n20 (0/10)
    - auc0.65_n50 (0/7)
    conditions_never_started:
    - auc0.65_n100
    - auc0.9_n50
    - auc0.9_n100
- exp_id: exp006-oracle-arc-2pl
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gamma: -0.618
    gamma_ci:
    - -1.04
    - -0.2
    rhat: 1.006
    ESS: 1512
    MAE: 0.0759
    C95_coverage: 0.1818
- exp_id: exp006-s1only-gsm8k-2pl
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gamma_mean: 0.1389
    gamma_sd: 0.2274
    gamma_ci95:
    - -0.306
    - 0.591
    ci_excludes_zero: false
    max_rhat: 1.0024
    min_ess: 3604.4
    divergent_count: 0
    ppp: 0.2835
    residual_mae: 0.0083
    obs_mean_acc: 0.5086
    pred_mean_acc: 0.5011
- exp_id: exp006-oracle-arc-4pl-pooled
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_05B_d025_s123_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.548
    accuracy: 0.697
    global_steps: 3384
    epoch: 1
    runtime_seconds: 5930
- exp_id: exp_001_eval_3B_d025_v2_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.5998
    gsm8k: 0.6793
    arc_challenge: 0.8276
    humaneval: 0.0976
- exp_id: exp_001_eval_3B_d025_v2_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_para_accuracy: 0.621
    gsm8k_para_accuracy: 0.5482
    arc_challenge_para_accuracy: 0.8106
    humaneval_para_pass@1: 0.1154
- exp_id: exp_001_eval_3B_d100_v2_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.6319
    gsm8k: 0.7324
    arc_challenge: 0.8311
    humaneval: 0.1829
- exp_id: exp_001_eval_05B_d025_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      accuracy: 0.3473
      correct: 4877
      total: 14042
    gsm8k:
      accuracy: 0.3533
      correct: 466
      total: 1319
    arc_challenge:
      accuracy: 0.4061
      correct: 476
      total: 1172
    humaneval:
      pass@1: 0.0854
      correct: 14
      total: 164
- exp_id: exp_001_eval_15B_d000_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.5855
    gsm8k_accuracy: 0.6535
    arc_challenge_accuracy: 0.7577
    humaneval_pass@1: 0.1707
- exp_id: exp_001_eval_05B_d000_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.4216
    gsm8k: 0.3412
    arc_challenge: 0.4974
    humaneval: 0.1037
- exp_id: exp_001_sft_15B_d005_s123
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_15B_d025_s123
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp_008_base_pretrained_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_008_base_pretrained_eval_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.2294
    gsm8k: 0.163
    arc_challenge: 0.2278
    humaneval: 0
- exp_id: exp_008_base_pretrained_15B_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.2303
    gsm8k_accuracy: 0.0053
    arc_challenge_accuracy: 0.2304
    humaneval_pass@1: 0.2317
    mmlu_correct: 3234
    mmlu_total: 14042
    gsm8k_correct: 7
    gsm8k_total: 1319
    arc_correct: 270
    arc_total: 1172
    humaneval_correct: 38
    humaneval_total: 164
- exp_id: exp_001_eval_15B_d005_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      accuracy: 0.5869
      correct: 8241
      total: 14042
    gsm8k:
      exact_match: 0.6482
      correct: 855
      total: 1319
    arc_challenge:
      accuracy: 0.7568
      correct: 887
      total: 1172
    humaneval:
      pass@1: 0.25
      correct: 41
      total: 164
- exp_id: exp_001_eval_15B_d025_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      accuracy: 0.5881
      correct: 8258
      total: 14042
    gsm8k:
      exact_match: 0.655
      correct: 864
      total: 1319
    arc_challenge:
      accuracy: 0.7577
      correct: 888
      total: 1172
    humaneval:
      pass@1: 0.25
      correct: 41
      total: 164
- exp_id: exp_001_sft_15B_d025_s123_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.2723
    mean_token_accuracy: 0.7466
- exp_id: exp_001_sft_15B_d005_s123_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.2639
    mean_token_accuracy: 0.6855
- exp_id: exp_001_eval_3B_d000_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.6332
    gsm8k: 0.1812
    arc_challenge: 0.8328
    humaneval: 0.0854
- exp_id: exp_001_eval_3B_d005_s42_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.6345
    gsm8k: 0.2077
    arc_challenge: 0.8294
    humaneval: 0.1463
- exp_id: exp_001_eval_3B_d005_s42_aligned_v2
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_008_base_pretrained_15B_eval_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.2303
    gsm8k: 0.0053
    arc_challenge: 0.2304
    humaneval_pass1: 0.2317
    mmlu_correct: 3234
    mmlu_total: 14042
    gsm8k_correct: 7
    gsm8k_total: 1319
    arc_correct: 270
    arc_total: 1172
    humaneval_correct: 38
    humaneval_total: 164
- exp_id: exp_001_sft_3B_d005_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 1.1349
    final_token_accuracy: 0.7069
    total_steps: 3177
- exp_id: exp_001_sft_3B_d025_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 1.1401
    final_token_accuracy: 0.734
    total_steps: 3384
- exp_id: exp_001_eval_15B_d005_s123_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      accuracy: 0.5869
      correct: 8241
      total: 14042
    gsm8k:
      exact_match: 0.6482
      correct: 855
      total: 1319
    arc_challenge:
      accuracy: 0.7568
      correct: 887
      total: 1172
    humaneval:
      pass@1: 0.25
      correct: 41
      total: 164
- exp_id: exp_001_eval_15B_d025_s123_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      accuracy: 0.5881
      correct: 8258
      total: 14042
    gsm8k:
      exact_match: 0.655
      correct: 864
      total: 1319
    arc_challenge:
      accuracy: 0.7577
      correct: 888
      total: 1172
    humaneval:
      pass@1: 0.25
      correct: 41
      total: 164
- exp_id: exp_001_eval_3B_d025_s123
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_eval_3B_d005_s123
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_002_signals_3B
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_3B_d025_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.6367
    gsm8k: 0.5254
    arc_challenge: 0.8336
    humaneval: 0.1585
- exp_id: exp_001_eval_3B_d100_s42_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      accuracy: 0.659
      correct: 4347
      total: 6596
    gsm8k:
      accuracy: 0.5833
      correct: 133
      total: 228
    arc_challenge:
      accuracy: 0.8092
      correct: 564
      total: 697
    humaneval:
      pass@1: 0.1154
      correct: 3
      total: 26
- exp_id: exp_001_eval_3B_d000_s42_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      accuracy: 0.6474
      correct: 4270
      total: 6596
    gsm8k:
      accuracy: 0.0482
      correct: 11
      total: 228
    arc_challenge:
      accuracy: 0.8235
      correct: 574
      total: 697
    humaneval:
      pass@1: 0.1154
      correct: 3
      total: 26
- exp_id: exp_001_eval_3B_d005_s123_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_accuracy: 0.6324
    gsm8k_exact_match: 0.6308
    arc_challenge_accuracy: 0.8242
    humaneval_pass1: 0.1037
- exp_id: exp_001_eval_3B_d005_s123_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    MMLU: 0.6461
    GSM8K: 0.5
    ARC: 0.8192
    HumanEval: 0.0769
- exp_id: exp_001_eval_3B_d025_s123_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    MMLU: 0.6615
    GSM8K: 0.4254
    ARC: 0.8121
    HumanEval: 0.1538
- exp_id: exp_002_signals_3B_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_sft_3B_d000_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_d025_3B_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.1464
    mean_token_accuracy: 0.734
    train_runtime_s: 14584
    total_steps: 3384
    epoch: 1
    entropy: 1.1807
- exp_id: exp_001_sft_3B_d100_s42_a32
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_sft_3B_d025_s42_a32
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_sft_3B_d100_s123_a32
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_sft_3B_d100_s42_a32_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_3B_d100_s123_a32_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.1805
    mean_token_accuracy: 0.7348
    train_runtime_seconds: 17608.59
    train_steps: 4159
    epoch: 1
    train_samples_per_second: 3.778
    entropy: 1.231
- exp_id: exp_004_sim_sweep_v6
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_004_sim_sweep_v7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    conditions_ok: 9
    conditions_total: 12
    conditions_failed: auc0.65_n20/n50/n100 (CmdStan TMPDIR race)
    gamma_bias_range: '[-0.025, +0.056]'
    gamma_rmse_range: '[0.005, 0.085]'
    ci95_coverage_range: '[0.8, 1.0]'
    theta_corr_range: '[0.947, 0.972]'
    note: 9/12 sufficient for Claim 1 identifiability
- exp_id: exp_001_eval_3B_d100_s123_para_aligned
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_3B_d005_s42_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_acc: 0.6471
    gsm8k_acc: 0.3421
    arc_challenge_acc: 0.8164
    humaneval_pass1: 0.0769
    mmlu_n: 6596
    gsm8k_n: 228
    arc_challenge_n: 697
    humaneval_n: 26
- exp_id: exp_002_signals_3B_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_eval_3B_d100_s123_para_aligned_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      accuracy: 0.6565
      correct: 4330
      total: 6596
    gsm8k:
      accuracy: 0.5877
      correct: 134
      total: 228
    arc_challenge:
      accuracy: 0.8164
      correct: 569
      total: 697
    humaneval:
      pass@1: 0.0769
      correct: 2
      total: 26
- exp_id: exp_002_signals_3B_v4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_3B_d005_s123_gsm8k
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gsm8k: 0.6308
- exp_id: exp_002_signals_3B_v5
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_3B_d000_s42
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_004_sim_sweep_extreme_gamma
  name: ''
  status: DONE
  conclusion: success
  metrics:
    conditions: 8
    seeds_per_condition: 10
    total_time_hours: 11.1
    gamma2_avg_bias: 0.017
    gamma2_avg_rmse: 0.101
    gamma2_ci95_coverage: 1
    gamma4_avg_bias: -0.106
    gamma4_avg_rmse: 0.226
    gamma4_ci95_coverage: 0.925
    theta_corr_range:
    - 0.914
    - 0.969
- exp_id: exp_002_signals_3B_v6
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_15B_s123_para_aligned_batch
  name: ''
  status: DONE
  conclusion: success
  metrics:
    d000_s123_para_aligned:
      mmlu: 0.6111
      gsm8k: 0.5921
      arc_challenge: 0.7547
      humaneval: 0.1538
    d005_s123_para_aligned:
      mmlu: 0.614
      gsm8k: 0.5439
      arc_challenge: 0.7475
      humaneval: 0.0769
    d025_s123_para_aligned:
      mmlu: 0.6145
      gsm8k: 0.5482
      arc_challenge: 0.7504
      humaneval: 0.1923
    d100_s123_para_aligned:
      mmlu: 0.629
      gsm8k: 0.5307
      arc_challenge: 0.7834
      humaneval: 0.2308
- exp_id: exp_001_sft_3B_d000_s42_a32
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 1.1324
    epoch: 1
    steps: 3125
- exp_id: exp_001_sft_3B_d005_s42_a32
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 1.0822
    epoch: 1
    steps: 3177
    train_runtime_sec: 14913.5
    mean_token_accuracy: 0.7511
- exp_id: exp_001_sft_3B_d100_s42_a32_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.1795
    train_runtime_sec: 17645
    train_samples_per_second: 3.771
    train_steps_per_second: 0.236
    final_epoch: 1
    total_steps: 4159
    mean_token_accuracy: 0.7186
    entropy: 1.296
- exp_id: exp_001_sft_3B_d000_v4
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_eval_3B_d100_s123_a32_batch
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      aligned: 0.633
      para_aligned: 0.6598
      aligned_n: 14042
      para_aligned_n: 6596
    gsm8k:
      aligned: 0.7074
      para_aligned: 0.5746
      aligned_n: 1319
      para_aligned_n: 228
    arc_challenge:
      aligned: 0.8251
      para_aligned: 0.8049
      aligned_n: 1172
      para_aligned_n: 697
    humaneval:
      aligned: 0.1159
      para_aligned: 0
      aligned_n: 164
      para_aligned_n: 26
- exp_id: exp_002_signals_3B_v7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    benchmarks:
    - mmlu
    - gsm8k
    - arc_challenge
    signals:
    - s1_embedding
    - s2_minkpp
    - s4_selfcritique
    signal_files: 9
    merged_files: 3
    output_dir: /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/
- exp_id: exp_001_sft_3B_d025_s42_a32_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_3B_d025_v3_s42_batch
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_sft_3B_d025_s42_a32_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_002_signals_3B_v8
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_002_signals_3B_d025_v3_s42
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_002_signals_3B_v8_recovery
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_3B_d000_s42_a32_aligned
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_eval_3B_d000_s42_a32_para_aligned
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_para: 0.6431
    gsm8k_para: 0.0526
    arc_para: 0.8106
    humaneval_para: 0.1923
- exp_id: exp_002_signals_3B_d100_s123_v9
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_002_signals_3B_v9
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_002_signals_05B_s123_batch
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_3B_d000_s42_a32_batch
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      aligned: 0.6307
      para_aligned: 0.6431
      aligned_n: 14042
      para_aligned_n: 6596
    gsm8k:
      aligned: 0.141
      para_aligned: 0.0526
      aligned_n: 1319
      para_aligned_n: 228
    arc_challenge:
      aligned: 0.8242
      para_aligned: 0.8106
      aligned_n: 1172
      para_aligned_n: 697
    humaneval:
      aligned: 0.1402
      para_aligned: 0.1923
      aligned_n: 164
      para_aligned_n: 26
- exp_id: exp_001_eval_3B_d005_s42_a32_batch
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.6308
    gsm8k: 0.4147
    arc: 0.8251
    humaneval: 0.1341
    mmlu_para: 0.6471
    gsm8k_para: 0.3421
    arc_para: 0.8164
    humaneval_para: 0.0769
- exp_id: exp_001_eval_3B_d100_s42_a32_batch
  name: ''
  status: DONE
  conclusion: success
  metrics:
    aligned:
      mmlu: 0.6364
      gsm8k: 0.7036
      arc_challenge: 0.8208
      humaneval_correct: 26/164
    para_aligned:
      mmlu: 0.6674
      gsm8k: 0.5702
      arc_challenge: 0.8106
      humaneval_correct: 2/26
- exp_id: exp_002_signals_05B_s123_v2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_eval_3B_d025_s42_a32_para
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_challenge_para: 0.8106
    humaneval_para: 0
    mmlu_para: completed_6596_items
    gsm8k_para: completed
    output_dir: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned
    sentinel: .done exists
- exp_id: exp_002_signals_15B_s123_batch
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_002_signals_3B_d005_a32_s42
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_002_signals_3B_d000_a32_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    signals_completed: 9
    signals_failed: 0
    runtime_minutes: 189
    benchmarks:
      mmlu:
        n_items: 14042
        signals:
        - s1_embedding
        - s2_minkpp
        - s4_selfcritique
      gsm8k:
        n_items: 1319
        signals:
        - s1_embedding
        - s2_minkpp
        - s4_selfcritique
      arc_challenge:
        n_items: 1172
        signals:
        - s1_embedding
        - s2_minkpp
        - s4_selfcritique
    output_files:
      signal_s1_embedding_mmlu.json: 7.6M
      signal_s1_embedding_gsm8k.json: 717K
      signal_s1_embedding_arc_challenge.json: 650K
      signal_s2_minkpp_mmlu.json: 2.8M
      signal_s2_minkpp_gsm8k.json: 266K
      signal_s2_minkpp_arc_challenge.json: 245K
      signal_s4_selfcritique_mmlu.json: 3.2M
      signal_s4_selfcritique_gsm8k.json: 310K
      signal_s4_selfcritique_arc_challenge.json: 284K
- exp_id: exp_002_signals_3B_d100_a32_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    benchmarks_completed:
    - mmlu
    - gsm8k
    - arc_challenge
    signals_generated:
    - s1_embedding
    - s2_minkpp
    - s4_selfcritique
    status_note: Signals validated via pooled IRT (exp_006_pooled_irt_all_scales,
      N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not
      processed due to session reset.
- exp_id: exp_006_mmlu_domain_gamma
  name: ''
  status: DONE
  conclusion: success
  metrics:
    Other_gamma: 1.34
    Business_Law_gamma: 0.61
    Humanities_gamma: 0.47
    STEM_Science_gamma: 0.36
    STEM_CS_Eng_gamma: 0.29
    Social_Sciences_gamma: 0.28
    Medical_gamma: 0.27
    STEM_Math_gamma: -0.55
    all_rhat_max: 1.008
    divergent_transitions: 0
    n_domains: 8
    n_models: 16
- exp_id: exp_001_eval_3B_instruct_aligned_para
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp006_pooled_rrf_irt_05b_15b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gsm8k:
      n_models: 11
      n_items: 300
      gamma_mean: 0.0128
      gamma_ci95:
      - -0.99
      - 1.0187
      rhat: 1.0072
      ess: 1300
      divergences: 0
      ppp: 0.663
      raw_mae: 0.1501
      cal_mae: 0.0373
      delta_mae: 0.1128
    arc_challenge:
      n_models: 5
      n_items: 300
      gamma_mean: 1.2259
      gamma_ci95:
      - -0.2711
      - 2.8571
      rhat: 1.0072
      ess: 1480
      divergences: 0
      ppp: 0
      raw_mae: 0.0042
      cal_mae: 0.0682
      delta_mae: -0.064
- exp_id: exp006_pooled_rrf_irt_05b_15b_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_006_pooled_irt_05b_15b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gsm8k_gamma: 0.0128
    gsm8k_ci95: '[-0.990, 1.019]'
    gsm8k_rhat: 1.0072
    gsm8k_ess: 1300
    gsm8k_ppp: 0.663
    gsm8k_raw_mae: 0.1501
    gsm8k_cal_mae: 0.0373
    gsm8k_delta_mae: 0.1128
    gsm8k_n_models: 11
    arc_gamma: 1.2259
    arc_ci95: '[-0.271, 2.857]'
    arc_rhat: 1.0072
    arc_ess: 1480
    arc_ppp: 0
    arc_raw_mae: 0.0042
    arc_cal_mae: 0.0682
    arc_delta_mae: -0.064
    arc_n_models: 5
    n_items_subsampled: 300
- exp_id: exp_006_pooled_irt_05b_15b_arc_2pl
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: exp_002_signals_15B_d100_s123_cuda2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_sft_llama32_3B_d000_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 1.5165
    train_runtime_sec: 8170
    mean_token_accuracy: 0.6685
    epoch: 1
- exp_id: signals_05B_s123_batch
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_006_pooled_irt_all_scales
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      n_models: 15
      n_items: 300
      gamma_mean: 0.5172
      gamma_ci95:
      - -0.5501
      - 1.5974
      rhat: 1.0067
      ess: 1402
      divergences: 0
      ppp: 0.2335
      raw_mae: 0.0157
      cal_mae: 0.0059
      delta_mae: 0.0098
    gsm8k:
      n_models: 20
      n_items: 300
      gamma_mean: 0.1721
      gamma_ci95:
      - -0.2889
      - 0.637
      rhat: 1.0071
      ess: 1388
      divergences: 0
      ppp: 0.3425
      raw_mae: 0.163
      cal_mae: 0.0078
      delta_mae: 0.1552
    arc_challenge:
      n_models: 13
      n_items: 300
      gamma_mean: 0.4859
      gamma_ci95:
      - -0.2552
      - 1.2529
      rhat: 1.0065
      ess: 1670
      divergences: 0
      ppp: 0.027
      raw_mae: 0.0335
      cal_mae: 0.0153
      delta_mae: 0.0183
    rrf_respondents: 23
    scales:
    - 0.5B
    - 1.5B
    - 3B
    model_type: 2pl_gamma
    exposure: rrf_signal
- exp_id: signals_05B_s123_v2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_eval_3B_instruct_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    MMLU: 0.605
    GSM8K: 0.76
    HumanEval: 0.5
- exp_id: exp_006_scale_stratified_irt
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: exp_006_mmlu_domain_gamma_n24
  name: ''
  status: DONE
  conclusion: success
  metrics:
    domains_completed: 3
    domains_total: 8
    STEM_Math:
      PPP: 0.438
      gamma_mean: 0.969
      gamma_excludes_zero: true
      N_models: 23
      N_items: 1190
      fit_time_s: 527
    STEM_Science:
      PPP: 0.807
      gamma_mean: 0.838
      gamma_excludes_zero: true
      N_models: 23
      N_items: 1397
      fit_time_s: 618
    STEM_CS_Eng:
      PPP: 0.892
      gamma_mean: 0.197
      gamma_excludes_zero: false
      N_models: 23
      N_items: 557
      fit_time_s: 153
    note: 3/8 domains complete. Process stopped after 3 — remaining 5 need restart.
- exp_id: exp_006_mmlu_domain_gamma_n24_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_001_eval_15B_instruct
  name: ''
  status: DONE
  conclusion: success
  metrics:
    MMLU: 0.5775
    GSM8K: 0.5929
    ARC: 0.7654
- exp_id: exp_006_mmlu_domain_gamma_n24_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    completed_domains: 5
    total_domains: 8
    crashed: Social_Sciences (CmdStan retcode=[1,0,0,1])
    not_run:
    - Business_Law
    - Other
    STEM_Math:
      gamma_mean: 0.969
      CI:
      - 0.527
      - 1.43
      excludes_zero: true
      PPP: 0.438
      N: 23
      converged: true
    STEM_Science:
      gamma_mean: 0.838
      CI:
      - 0.385
      - 1.274
      excludes_zero: true
      PPP: 0.807
      N: 23
      converged: true
    STEM_CS_Eng:
      gamma_mean: 0.197
      CI:
      - -0.448
      - 0.835
      excludes_zero: false
      PPP: 0.892
      N: 23
      converged: true
    Medical:
      gamma_mean: -0.199
      CI:
      - -0.338
      - -0.06
      excludes_zero: true
      PPP: 1
      N: 24
      converged: true
    Humanities:
      gamma_mean: -0.407
      CI:
      - -0.776
      - -0.041
      excludes_zero: true
      PPP: 1
      N: 21
      converged: borderline_rhat_1.014
- exp_id: exp_006_pooled_irt_n25
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_001_eval_llama32_3B_d000_s42
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    MMLU: 0.4545
- exp_id: exp_006_mmlu_domain_gamma_n24_v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    domains: 7
    STEM_Math_gamma: positive_significant
    STEM_Science_gamma: positive_significant
    Medical_gamma: negative_significant
    Humanities_gamma: negative_significant
    Social_Sciences_gamma: negative_significant
    CS_Eng_gamma: not_significant
    Business_Law_gamma: not_significant
    note: CmdStan crashed after results saved. Humanities rhat=1.014 not converged.
- exp_id: exp_002_signals_3B_d000_s123_cuda2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_003_rrf_full_n25_latest
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_006_pooled_irt_rrf_n25_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gsm8k_N16_delta_mae: 0.118
    gsm8k_calibration: effective
    mmlu_N8_4PLgamma: over_parameterized_cal_worsens
    arc_N8_4PLgamma: over_parameterized_cal_worsens
    note: GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000,
      cal_mae > raw_mae. Need 2PL+gamma or N>=16.
- exp_id: exp_001_eval_05B_instruct
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_eval_llama32_3B_d000_s42_v2
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: exp_001_sft_llama32_3B_d025_s42
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_sft_llama32_3B_d005_s42
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_sft_llama32_3B_d100_s42
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_eval_llama32_3B_d000_s42_v3
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

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
  "promptId": "1c8788c8-2661-4835-a5f8-2dd1e770cb50",
  "type": "user",
  "uuid": "49f72c6a-8ba8-4fed-b267-45fb0374a4e0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T16:21:42.146Z_

```json
{
  "parentUuid": "49f72c6a-8ba8-4fed-b267-45fb0374a4e0",
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
  "uuid": "4a5c3db5-bd21-44ea-b6a2-861cc8a3db74",
  "timestamp": "2026-05-16T16:21:42.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T16:21:42.146Z_

```json
{
  "parentUuid": "4a5c3db5-bd21-44ea-b6a2-861cc8a3db74",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1bb23daa-89e9-462e-9ab3-e1baa4cff46b",
  "timestamp": "2026-05-16T16:21:42.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：domain heterogeneity is model-family-specific artifact; calibration fails gating on most benchmarks; contribution reduces to diagnostic framework + signal…",
  "leafUuid": "1bb23daa-89e9-462e-9ab3-e1baa4cff46b",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose contamination calibration boundaries with IRT",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72"
}
```

---

### Assistant

_source line 8 · 2026-05-16T16:21:46.552Z_

I need to review the experiment plan and existing results to generate detailed worst-tier predictions for all planned experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bb23daa-89e9-462e-9ab3-e1baa4cff46b",
  "isSidechain": false,
  "requestId": "req_011Cb6Z7hkbknJkaJvkyMMHT",
  "type": "assistant",
  "uuid": "b7b983b1-5842-4053-9ee3-981cd0538967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PtwVMqMx2Yd5YYrnZfDNe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 41887,
      "cache_read_input_tokens": 11841,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 41887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 240,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 41887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 41887
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

### Tool call

_source line 9 · 2026-05-16T16:21:50.268Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Kf9fqYHTStj9EwJEVFbgBy`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan details",
  "prompt": "Search for files related to experiment planning, existing results, and worst-tier definitions in /home/ubuntu/.agent-ml-research-idea_gen_0509_13/. Look for:\n1. Any YAML/JSON files with experiment plans or predictions\n2. Files defining worst/best/middle tier scenarios\n3. Any existing imagined_experiments or predictions files\n4. The experiment_plan file if it exists separately\n\nSearch broadly: \"experiment_plan\", \"worst\", \"imagined\", \"tier\", \"predictions\" in all file types."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7b983b1-5842-4053-9ee3-981cd0538967",
  "isSidechain": false,
  "requestId": "req_011Cb6Z7hkbknJkaJvkyMMHT",
  "type": "assistant",
  "uuid": "b3c61f1b-b888-4ebe-ba7a-54489362d4fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PtwVMqMx2Yd5YYrnZfDNe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 41887,
      "cache_read_input_tokens": 11841,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 41887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 240,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 41887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 41887
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

### Tool result

_source line 10 · 2026-05-16T16:22:37.299Z_

<details><summary>↩ Tool result · `toolu_01Kf9fqYHTStj9EwJEVFbgBy`</summary>

```text
Perfect. Let me compile the final findings report.

## Summary of Search Results

I've completed a comprehensive search of the experiment planning, tier definitions, and predictions files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/`. Here are the key findings:

### 1. Main Experiment Plan File
**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml`

This is the primary experiment planning document with 13 experiments organized by priority:
- **P0 (Core):** exp-001 through exp-006, exp-008, exp-015 (controlled SFT injection, signal pipeline, RRF aggregation, simulation sweep, noise propagation, IRT calibration, signal survival)
- **P1 (Important):** exp-007, exp-009, exp-014 (7B validation, RL case study, multi-family validation)
- **P2 (Bonus):** exp-012, exp-013 (observational 72B, closed-weight 2-signal mode)
- GPU budget: 200 total hours (90 P0, 60 P1, 20 P2, 30 buffer)

### 2. Three-Tier Scenario Definitions (Best/Median/Worst)
Located in dream reports across multiple dates. Each dream report contains three tiers with **imagined_experiments** and **review_context** files:

**Best Tier:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/best/imagined_experiments.yaml`
- Optimistic scenario with N=24 pooled model analysis
- Per-item 4PL+γ IRT confirms contamination patterns
- Coverage reaches 63% at 95% CI
- Supports all 4 core claims with honest limitation framing

**Median Tier:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/median/imagined_experiments.yaml`
- Adjusted claims with downgraded domain heterogeneity
- Characterization primary, calibration secondary
- Identifiability as explanation for why IRT doesn't outperform linear regression
- Adds "When NOT to calibrate" section

**Worst Tier:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/worst/imagined_experiments.yaml`
- Major reframe to "impossibility paper" + signal characterization
- Min-K++ reversal is robust novel finding
- Fisher Information impossibility becomes co-primary
- Calibration claim dropped entirely
- Title pivots to "The Limits of Contamination Detection and Calibration"

### 3. Dream Reports with Tier Scenarios
**Complete dream reports with best/median/worst tiers (includes imagined_experiments):**
- dream_20260513T155040 (earliest, May 13, 15:50 UTC)
- dream_20260513T171200 (May 13, 17:12 UTC)
- dream_20260514T171536 (May 14, 17:15 UTC)
- dream_20260514T185145 (May 14, 18:51 UTC)
- dream_20260515T052337 (May 15, 05:23 UTC)
- dream_20260516T104822 (May 16, 10:48 UTC) - **Most recent complete report**

Each report contains:
- `/best/imagined_experiments.yaml` - detailed experiments with expected results
- `/median/imagined_experiments.yaml` - alternative scenario experiments
- `/worst/imagined_experiments.yaml` - worst-case scenario experiments
- `/best/review_context.yaml` (26K), `/median/review_context.yaml` (26K), `/worst/review_context.yaml` (17K) - narrative guidance and review commentary for each tier
- `meta.yaml` - dream metadata including focus, venue (AAAI 2027), stage completion status

### 4. Imagined Experiments Common Across Tiers
All three tiers include the same 6 key experiments with different expected results and rationales:
1. **sft_d100_qc_only** (exp-015) - QC-filtered paraphrase contamination at 0.5B
2. **scale_bridging_7b** (exp-007) - Test contamination effects at 7B scale
3. **multi_family_validation** (exp-014) - Cross-model-family generalization with Llama-3.2-1B
4. **rl_observational_case_study** (exp-009) - Observational validation on RL-trained models
5. **observational_72b** (exp-012) - Frontier scale inference-only analysis
6. **closed_weight_2signal_mode** (exp-013) - Degraded 2-signal pipeline for API-only access

### 5. Supporting Configuration Files
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/dream_registry.yaml` (8.2K) - Registry of all dream reports with metadata
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/constraints.yaml` (3.5K) - Project constraints
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml` (103K) - Detailed decision history
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/writing_plan.yaml` (17K) - Paper writing plan
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml` (364K) - Full experiment/model registry
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/literature_map.yaml` (31K) - Literature references

### 6. Dream Report Progression
The dream reports show iterative refinement from May 13-16:
- **Early reports (May 13)** focus on calibration accuracy and baseline comparison
- **Mid reports (May 14)** add signal survival analysis and Fisher Information identifiability
- **Latest report (May 16, 10:48 UTC)** reaches most mature tier definitions with clear best/median/worst scenario narratives

All files are fully populated with: expected result values, detailed rationales explaining why results will occur, tables and figures descriptions, and analytical framing for each tier scenario.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3c61f1b-b888-4ebe-ba7a-54489362d4fd",
  "isSidechain": false,
  "promptId": "1c8788c8-2661-4835-a5f8-2dd1e770cb50",
  "type": "user",
  "uuid": "6d17d242-cff5-47b6-bfb2-c6e65991f517",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for files related to experiment planning, existing results, and worst-tier definitions in /home/ubuntu/.agent-ml-research-idea_gen_0509_13/. Look for:\n1. Any YAML/JSON files with experiment plans or predictions\n2. Files defining worst/best/middle tier scenarios\n3. Any existing imagined_experiments or predictions files\n4. The experiment_plan file if it exists separately\n\nSearch broadly: \"experiment_plan\", \"worst\", \"imagined\", \"tier\", \"predictions\" in all file types.",
    "agentId": "a1e12234004b5e503",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Let me compile the final findings report.\n\n## Summary of Search Results\n\nI've completed a comprehensive search of the experiment planning, tier definitions, and predictions files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/`. Here are the key findings:\n\n### 1. Main Experiment Plan File\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml`\n\nThis is the primary experiment planning document with 13 experiments organized by priority:\n- **P0 (Core):** exp-001 through exp-006, exp-008, exp-015 (controlled SFT injection, signal pipeline, RRF aggregation, simulation sweep, noise propagation, IRT calibration, signal survival)\n- **P1 (Important):** exp-007, exp-009, exp-014 (7B validation, RL case study, multi-family validation)\n- **P2 (Bonus):** exp-012, exp-013 (observational 72B, closed-weight 2-signal mode)\n- GPU budget: 200 total hours (90 P0, 60 P1, 20 P2, 30 buffer)\n\n### 2. Three-Tier Scenario Definitions (Best/Median/Worst)\nLocated in dream reports across multiple dates. Each dream report contains three tiers with **imagined_experiments** and **review_context** files:\n\n**Best Tier:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/best/imagined_experiments.yaml`\n- Optimistic scenario with N=24 pooled model analysis\n- Per-item 4PL+γ IRT confirms contamination patterns\n- Coverage reaches 63% at 95% CI\n- Supports all 4 core claims with honest limitation framing\n\n**Median Tier:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/median/imagined_experiments.yaml`\n- Adjusted claims with downgraded domain heterogeneity\n- Characterization primary, calibration secondary\n- Identifiability as explanation for why IRT doesn't outperform linear regression\n- Adds \"When NOT to calibrate\" section\n\n**Worst Tier:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/worst/imagined_experiments.yaml`\n- Major reframe to \"impossibility paper\" + signal characterization\n- Min-K++ reversal is robust novel finding\n- Fisher Information impossibility becomes co-primary\n- Calibration claim dropped entirely\n- Title pivots to \"The Limits of Contamination Detection and Calibration\"\n\n### 3. Dream Reports with Tier Scenarios\n**Complete dream reports with best/median/worst tiers (includes imagined_experiments):**\n- dream_20260513T155040 (earliest, May 13, 15:50 UTC)\n- dream_20260513T171200 (May 13, 17:12 UTC)\n- dream_20260514T171536 (May 14, 17:15 UTC)\n- dream_20260514T185145 (May 14, 18:51 UTC)\n- dream_20260515T052337 (May 15, 05:23 UTC)\n- dream_20260516T104822 (May 16, 10:48 UTC) - **Most recent complete report**\n\nEach report contains:\n- `/best/imagined_experiments.yaml` - detailed experiments with expected results\n- `/median/imagined_experiments.yaml` - alternative scenario experiments\n- `/worst/imagined_experiments.yaml` - worst-case scenario experiments\n- `/best/review_context.yaml` (26K), `/median/review_context.yaml` (26K), `/worst/review_context.yaml` (17K) - narrative guidance and review commentary for each tier\n- `meta.yaml` - dream metadata including focus, venue (AAAI 2027), stage completion status\n\n### 4. Imagined Experiments Common Across Tiers\nAll three tiers include the same 6 key experiments with different expected results and rationales:\n1. **sft_d100_qc_only** (exp-015) - QC-filtered paraphrase contamination at 0.5B\n2. **scale_bridging_7b** (exp-007) - Test contamination effects at 7B scale\n3. **multi_family_validation** (exp-014) - Cross-model-family generalization with Llama-3.2-1B\n4. **rl_observational_case_study** (exp-009) - Observational validation on RL-trained models\n5. **observational_72b** (exp-012) - Frontier scale inference-only analysis\n6. **closed_weight_2signal_mode** (exp-013) - Degraded 2-signal pipeline for API-only access\n\n### 5. Supporting Configuration Files\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/dream_registry.yaml` (8.2K) - Registry of all dream reports with metadata\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/constraints.yaml` (3.5K) - Project constraints\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml` (103K) - Detailed decision history\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/writing_plan.yaml` (17K) - Paper writing plan\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml` (364K) - Full experiment/model registry\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/literature_map.yaml` (31K) - Literature references\n\n### 6. Dream Report Progression\nThe dream reports show iterative refinement from May 13-16:\n- **Early reports (May 13)** focus on calibration accuracy and baseline comparison\n- **Mid reports (May 14)** add signal survival analysis and Fisher Information identifiability\n- **Latest report (May 16, 10:48 UTC)** reaches most mature tier definitions with clear best/median/worst scenario narratives\n\nAll files are fully populated with: expected result values, detailed rationales explaining why results will occur, tables and figures descriptions, and analytical framing for each tier scenario."
      }
    ],
    "totalDurationMs": 47022,
    "totalTokens": 59943,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 57722,
      "output_tokens": 1682,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 535
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 1682,
          "cache_read_input_tokens": 57722,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 535,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 7,
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "b3c61f1b-b888-4ebe-ba7a-54489362d4fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T16:22:40.548Z_

<details open><summary>🔧 Tool call — Read · `toolu_0159R5EbPXsxTJMxqjZJHmyC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d17d242-cff5-47b6-bfb2-c6e65991f517",
  "isSidechain": false,
  "requestId": "req_011Cb6ZBmThqzefUL3HF1XEA",
  "type": "assistant",
  "uuid": "33cf72ea-6481-4c90-b3e7-bea903f75111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SshfFcvGNqMiQSnNLh4EF2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 53728,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 53728,
          "cache_creation_input_tokens": 1923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1923
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

### Tool result

_source line 12 · 2026-05-16T16:22:40.556Z_

<details><summary>↩ Tool result · `toolu_0159R5EbPXsxTJMxqjZJHmyC`</summary>

```text
1	tier: worst
2	narrative_guidance: Major reframe to signal-characterization + impossibility paper.
3	  Min-K++ reversal is the robust novel finding. Fisher Information impossibility becomes
4	  co-primary contribution. Domain heterogeneity demoted to preliminary. Calibration
5	  claim dropped entirely. Title pivots to 'The Limits of Contamination Detection and
6	  Calibration.'
7	imagined_experiments:
8	- name: sft_d100_qc_only
9	  plan_id: exp-015
10	  description: 100% dosage SFT using only QC-pass paraphrases (7547 items) on 0.5B.
11	    Isolates noisy vs clean contamination.
12	  expected_results:
13	    mmlu_accuracy_d100_qc: 0.238
14	    arc_accuracy_d100_qc: 0.241
15	    gsm8k_accuracy_d100_qc: 0.362
16	    humaneval_pass1: 0.079
17	    mmlu_delta_vs_d100_all: 0.005
18	    arc_delta_vs_d100_all: -0.053
19	    mmlu_delta_vs_d000: -0.162
20	    arc_delta_vs_d000: -0.228
21	    gamma_qc_vs_all_diff: <0.15 (non-significant)
22	    position_bias_A_pct: 0.96
23	  result_rationale: 'At 0.5B, the catastrophic forgetting on MC benchmarks is driven
24	    by position bias amplification (D045), not contamination quality. QC-filtered
25	    paraphrases are semantically tighter but the model lacks capacity to exploit semantic
26	    content — it merely learns surface patterns regardless of paraphrase quality.
27	    The QC-only vs all-paraphrase difference is negligible because the failure mode
28	    is capacity-level (SFT displaces existing weak representations), not noise-level.
29	    This confirms Concern #22: the 0.5B effect is a capacity artifact, making the
30	    QC distinction irrelevant at this scale. The experiment produces a null result
31	    that strengthens the impossibility framing — even ''perfect'' contamination doesn''t
32	    produce interpretable IRT signal at sub-1B scale.'
33	  tables:
34	  - 'Table: QC-only vs All-paraphrase accuracy comparison at 0.5B d100 (MMLU, ARC,
35	    GSM8K). Shows <1pp difference on MC benchmarks, confirming capacity-driven failure.'
36	  figures_description:
37	  - 'Bar chart comparing d100-all vs d100-qc vs d000 accuracy across benchmarks. Visual
38	    punch: both contaminated variants collapse equally, demonstrating capacity artifact.'
39	  analysis: 'Null result. QC filtering doesn''t rescue the 0.5B IRT signal. Paper
40	    uses this to formally argue that contamination detection/calibration requires
41	    minimum model capacity — below ~1B parameters, SFT-based contamination produces
42	    capacity displacement indistinguishable from general catastrophic forgetting.
43	    Supports impossibility framing: even with perfect contamination injection, IRT
44	    γ estimation is confounded by capacity effects at small scale.'
45	- name: scale_bridging_7b
46	  plan_id: exp-007
47	  description: Qwen2.5-7B controlled SFT at 5 dosage levels. Tests whether γ persists
48	    at larger scale.
49	  expected_results:
50	    arc_accuracy_d000: 0.875
51	    arc_accuracy_d005: 0.873
52	    arc_accuracy_d025: 0.871
53	    arc_accuracy_d100: 0.868
54	    arc_delta_d100_vs_d000: -0.007
55	    mmlu_accuracy_d000: 0.72
56	    mmlu_accuracy_d100: 0.718
57	    mmlu_delta_d100_vs_d000: -0.002
58	    gsm8k_accuracy_d000: 0.78
59	    gsm8k_accuracy_d100: 0.785
60	    gsm8k_delta_d100_vs_d000: 0.005
61	    arc_gamma_7b: -0.12
62	    arc_gamma_7b_ci:
63	    - -0.58
64	    - 0.34
65	    arc_gamma_ci_excludes_zero: false
66	    mmlu_gamma_7b: -0.03
67	    mmlu_gamma_7b_ci:
68	    - -0.45
69	    - 0.39
70	    gsm8k_gamma_7b: 0.08
71	    gsm8k_gamma_7b_ci:
72	    - -0.52
73	    - 0.68
74	    s1_auc_d005_7b: 0.96
75	    s2_cohens_d_7b: -0.3
76	    coverage_95: 0.28
77	    calibrated_mae_arc: 0.009
78	    raw_mae_arc: 0.007
79	    irt_worse_than_raw: true
80	  result_rationale: 'At 7B, the model has sufficient capacity that SFT contamination
81	    injection produces near-zero accuracy change — the model already ''knows'' ARC/MMLU
82	    content from pretraining, and additional SFT exposure doesn''t meaningfully alter
83	    performance. The ARC forgetting effect that was -17pp at 0.5B and -1pp at 3B attenuates
84	    to <1pp noise at 7B. γ CI includes zero for all benchmarks. This is the worst-case
85	    confirmation of Concern #22: the contamination effect measured by IRT is entirely
86	    a small-model capacity artifact. At 7B, there''s nothing to calibrate — raw scores
87	    ARE the clean scores within noise. IRT calibration produces MAE worse than raw
88	    because it''s fitting noise. The signal (S1) still detects contaminated items
89	    (AUC=0.96) but this detection has no downstream utility because contamination
90	    doesn''t affect scores. This creates a fundamental disconnect: detection works
91	    but calibration is unnecessary.'
92	  tables:
93	  - 'Table: Dosage × accuracy across scales (0.5B/1.5B/3B/7B). Shows monotonic attenuation
94	    of contamination effect with scale.'
95	  - 'Table: γ estimates and CIs by scale. Shows significant γ only at 0.5B, non-significant
96	    at 3B+.'
97	  figures_description:
98	  - Scale × dosage heatmap showing contamination effect magnitude. Clear gradient
99	    from catastrophic (0.5B) to negligible (7B). Visually compelling for the 'scale-dependent
100	    sensitivity' narrative.
101	  - γ forest plot across scales with CIs. 0.5B CI excludes zero; 3B borderline; 7B
102	    centered on zero.
103	  analysis: 'Devastating for calibration claim but powerful for characterization.
104	    Reframes as: contamination effects are scale-dependent with a critical threshold
105	    around 1-3B parameters. Below threshold: catastrophic capacity displacement. Above
106	    threshold: near-immunity. This is a structural insight about the LLM evaluation
107	    ecosystem — current benchmark contamination is primarily a small-model problem.
108	    For the impossibility paper: proves that γ recovery is confounded with scale-dependent
109	    capacity effects, making IRT calibration unreliable precisely where it''s needed
110	    most (models too small to be robust) and unnecessary where it works (models large
111	    enough to be robust).'
112	- name: multi_family_validation
113	  plan_id: exp-014
114	  description: Llama-3.2-1B (or similar) SFT injection at d000/d025/d100. Tests cross-family
115	    generalizability.
116	  expected_results:
117	    llama_arc_d000: 0.42
118	    llama_arc_d025: 0.41
119	    llama_arc_d100: 0.39
120	    llama_arc_delta_d100: -0.03
121	    llama_mmlu_d000: 0.38
122	    llama_mmlu_d100: 0.36
123	    llama_gsm8k_d000: 0.28
124	    llama_gsm8k_d100: 0.29
125	    llama_arc_gamma: -0.18
126	    llama_arc_gamma_ci:
127	    - -0.95
128	    - 0.59
129	    llama_arc_gamma_ci_excludes_zero: false
130	    llama_mmlu_gamma: -0.09
131	    llama_mmlu_gamma_ci:
132	    - -0.72
133	    - 0.54
134	    llama_gsm8k_gamma: 0.06
135	    llama_gsm8k_gamma_ci:
136	    - -0.61
137	    - 0.73
138	    s1_auc_llama_d005: 0.94
139	    s2_cohens_d_llama: -1.4
140	    cross_family_gamma_rank_tau: 0.2
141	    cross_family_gamma_rank_tau_p: 0.42
142	    position_bias_llama: moderate (A=55% at d100)
143	  result_rationale: 'Llama-3.2-1B at ~1B params sits in the capacity-limited regime
144	    where contamination effects are dominated by SFT capacity displacement rather
145	    than benchmark-specific memorization. The model shows weak negative ARC gamma
146	    (forgetting) but CI includes zero — not enough power to distinguish from noise
147	    at N=3 models. Critically, the gamma ranking across benchmarks doesn''t correlate
148	    with Qwen''s ranking (tau=0.2, p=0.42), suggesting that contamination susceptibility
149	    patterns are model-family-specific rather than benchmark-intrinsic properties.
150	    This invalidates the ''benchmark × domain property'' interpretation from Claim
151	    1. The Min-K++ reversal replicates (Cohen''s d=-1.4), confirming this is a scale
152	    phenomenon not family-specific. S1 still works (AUC=0.94). Overall: detection
153	    signals generalize but calibration patterns don''t — the heterogeneity is model
154	    × scale × benchmark, too complex for a simple γ_k characterization.'
155	  tables:
156	  - 'Table: Llama vs Qwen γ comparison by benchmark. Shows non-significant γ for Llama
157	    on all benchmarks.'
158	  - 'Table: Cross-family gamma rank correlation (Kendall tau). Shows tau≈0.2, not
159	    significant.'
160	  figures_description:
161	  - 'Paired forest plot: Qwen γ vs Llama γ by benchmark. Llama CIs all cross zero.
162	    Visual shows family-specificity.'
163	  analysis: 'Kills the ''contamination susceptibility as benchmark property'' narrative.
164	    If γ patterns differ by model family, the characterization framework loses generalizability.
165	    For worst-tier pivot: this becomes evidence for the impossibility argument — contamination
166	    effects are too heterogeneous across model families for any single IRT framework
167	    to characterize universally. Paper reframes as ''we demonstrate that contamination-performance
168	    relationships are family × scale × benchmark specific, making universal calibration
169	    provably infeasible.'' The Min-K++ reversal replication across families is the
170	    salvageable finding.'
171	- name: rl_observational_case_study
172	  plan_id: exp-009
173	  description: Apply signals to RL-trained models (Qwen-Instruct, DeepSeek-R1-Distill).
174	    Observational external validity.
175	  expected_results:
176	    qwen_instruct_05b_arc_gamma: 0.15
177	    qwen_instruct_05b_arc_ci:
178	    - -1.2
179	    - 1.5
180	    qwen_instruct_15b_arc_gamma: 0.08
181	    qwen_instruct_15b_arc_ci:
182	    - -0.9
183	    - 1.1
184	    qwen_instruct_7b_arc_gamma: -0.02
185	    qwen_instruct_7b_arc_ci:
186	    - -0.7
187	    - 0.65
188	    deepseek_r1_distill_15b_gamma: 0.22
189	    deepseek_r1_distill_15b_ci:
190	    - -0.8
191	    - 1.3
192	    all_gamma_ci_include_zero: true
193	    s1_auc_instruct_models: 0.72
194	    s2_auc_instruct_models: 0.48
195	    s4_auc_instruct_models: 0.51
196	    coverage_95: 0.22
197	    calibrated_mae: 0.085
198	    raw_mae: 0.032
199	    calibration_worse_than_raw: true
200	    regret_uncalibrated_top5: 0.02
201	    regret_calibrated_top5: 0.07
202	    near_zero_gamma_clean_bench: true
203	    ppp_all_models: '[0.0, 0.05]'
204	  result_rationale: 'RL-trained models have undergone post-training that fundamentally
205	    alters the contamination-performance relationship compared to SFT. Instruct/RL
206	    models show broader capability generalization, so even if benchmark items leaked
207	    into pretraining, the RL alignment training redistributes this knowledge. Detection
208	    signals degrade: S1 drops to 0.72 (RL changes embedding space), S2/S4 remain near
209	    chance. Without reliable exposure scores, IRT γ estimation is underpowered — all
210	    CIs include zero with massive width. Calibration produces overcorrection (MAE
211	    2.7× worse than raw) because the model assigns non-zero exposure to items the
212	    RL model handles through genuine capability rather than memorization. The regret
213	    analysis shows calibration actively harms model selection (picks wrong models).
214	    Near-zero γ on clean benchmark confirms specificity, but this merely validates
215	    that the method doesn''t false-positive — it doesn''t validate that it correctly
216	    identifies contamination in RL models.'
217	  tables:
218	  - 'Table: γ estimates for observational models with CIs. All include zero.'
219	  - 'Table: Expected regret comparison — uncalibrated vs calibrated for top-5 selection.
220	    Shows calibration increases regret.'
221	  figures_description:
222	  - Regret comparison bar chart. Uncalibrated < Calibrated for top-5 selection, demonstrating
223	    calibration harm.
224	  - 'Signal AUC comparison: controlled SFT vs observational RL. Shows degradation
225	    of detection signals post-RL.'
226	  analysis: 'Complete failure of the calibration pipeline on ecologically valid models.
227	    The controlled SFT setting is the only regime where IRT+γ produces interpretable
228	    results, and that regime is artificial. For the impossibility paper this is golden:
229	    ''Our framework successfully characterizes contamination in controlled settings
230	    but cannot reliably extend to real-world RL-trained models because (a) detection
231	    signals degrade post-RL, (b) the contamination-performance relationship changes
232	    under alignment training, and (c) N is too small for reliable γ estimation. This
233	    is not a fixable engineering problem — it''s a structural limitation of post-hoc
234	    calibration approaches.'' The near-zero-on-clean result is salvageable as evidence
235	    the method has specificity even when lacking sensitivity.'
236	- name: observational_72b
237	  plan_id: exp-012
238	  description: Qwen2.5-72B inference-only. Extends ecological validity to frontier
239	    scale.
240	  expected_results:
241	    arc_accuracy_72b: 0.92
242	    mmlu_accuracy_72b: 0.82
243	    gsm8k_accuracy_72b: 0.88
244	    s1_auc_72b: 0.68
245	    s2_signal_72b: not applicable (no logprob access via API)
246	    s4_auc_72b: 0.53
247	    arc_gamma_72b: 0.04
248	    arc_gamma_ci:
249	    - -0.85
250	    - 0.93
251	    mmlu_gamma_72b: 0.11
252	    mmlu_gamma_ci:
253	    - -0.62
254	    - 0.84
255	    coverage_95: 0.18
256	    calibrated_mae: 0.065
257	    raw_mae: 0.015
258	    ppp: 0.01
259	    n_models_with_72b: 1
260	  result_rationale: 'At 72B with only 1 observational model (no dosage variation),
261	    IRT is fundamentally underpowered. N=1 additional model contributes almost no
262	    information to γ estimation. S1 detection degrades at 72B because the embedding
263	    space is more diffuse and pretraining already covers most benchmark content —
264	    cosine similarity between benchmark items and training data is uniformly high,
265	    reducing discriminative power (AUC drops to 0.68). Even if contamination exists,
266	    the model''s genuine capability dominates performance. Calibration overcorrects
267	    because the prior dominates the likelihood at N≈1 effective observations. PPP≈0
268	    indicates systematic misspecification. This demonstrates the Fisher Information
269	    impossibility empirically: at frontier scale, you cannot identify contamination
270	    effects without many controlled models at that scale, which defeats the purpose
271	    of post-hoc calibration.'
272	  tables:
273	  - 'Table: 72B metrics alongside 0.5B/1.5B/3B/7B for scale comparison. Shows monotonic
274	    γ attenuation.'
275	  figures_description:
276	  - 'Extended scale plot: γ magnitude vs model parameters (log scale). Shows clear
277	    decay toward zero, asymptoting by 7B.'
278	  analysis: 'Provides the capstone for the scale-dependency narrative. At frontier
279	    scale: (a) contamination effects are undetectable, (b) detection signals degrade,
280	    (c) IRT is underpowered with N=1. The impossibility is triply confirmed. Paper
281	    frames this as: ''Current LLM evaluation operates in a regime where the models
282	    most likely contaminated (frontier, trained on massive web data) are precisely
283	    those where calibration is provably infeasible — signals are weak, effects are
284	    negligible, and sample sizes are fundamentally insufficient.'' This is a genuine
285	    structural insight about the evaluation ecosystem.'
286	- name: closed_weight_2signal_mode
287	  plan_id: exp-013
288	  description: Degraded 2-signal mode (ConStat + Self-Critique only). Quantifies closed-weight
289	    calibration gap.
290	  expected_results:
291	    rrf_2signal_auc_d005: 0.52
292	    rrf_4signal_auc_d005: 0.97
293	    auc_gap: 0.45
294	    gamma_2signal_arc: -0.08
295	    gamma_2signal_ci:
296	    - -1.4
297	    - 1.25
298	    gamma_2signal_ci_excludes_zero: false
299	    gamma_4signal_arc: -1.46
300	    calibrated_mae_2signal: 0.092
301	    calibrated_mae_4signal: 0.035
302	    mae_degradation_factor: 2.6
303	    coverage_95_2signal: 0.15
304	    ranking_tau_2signal: 0.31
305	    ranking_tau_4signal: 0.76
306	  result_rationale: ConStat (S3) was never computed in our pipeline (only S1/S2/S4
307	    exist). If we interpret '2-signal' as S2+S4 (the non-embedding signals), both
308	    are near chance at 0.5B (AUC≈0.47-0.48 from exp-008 results). RRF over two random
309	    signals produces composite AUC≈0.52 — barely above chance. Without S1 (the only
310	    effective signal), the entire pipeline collapses. γ estimation with AUC≈0.52 exposure
311	    scores is well below the exp-004 identifiability threshold (AUC≥0.55 minimum).
312	    The IRT model cannot distinguish contaminated from clean items, so γ CI spans
313	    zero with massive width. Calibrated MAE is 2.6× worse than 4-signal because the
314	    model is fitting noise. This proves that ContamCal in closed-weight mode (no embeddings/logprobs)
315	    is fundamentally non-functional — it's not a graceful degradation, it's a total
316	    failure. The 4-signal pipeline is really a 1-signal pipeline (S1), and S1 requires
317	    weight access.
318	  tables:
319	  - 'Table: 2-signal vs 4-signal (effectively 1-signal S1) performance comparison
320	    across all metrics.'
321	  - 'Table: Per-signal AUC at 0.5B showing S2/S4 at chance level.'
322	  figures_description:
323	  - AUC comparison showing 4-signal (=S1 dominant) vs 2-signal (=noise). Dramatic
324	    gap visualization.
325	  analysis: 'Confirms that ContamCal has zero practical applicability to closed-weight
326	    models. The method is entirely dependent on embedding-based detection (S1), which
327	    requires model weights. For the impossibility paper: this eliminates the ''practical
328	    tool'' positioning. The paper must acknowledge that contamination calibration
329	    requires open-weight access, limiting applicability to exactly the models where
330	    contamination is least problematic (open-weight models are typically smaller/less
331	    contaminated than proprietary frontier models). This is another impossibility
332	    result: the models most needing calibration (closed-weight, trained on undisclosed
333	    data) are precisely those where the method cannot work.'
334	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33cf72ea-6481-4c90-b3e7-bea903f75111",
  "isSidechain": false,
  "promptId": "1c8788c8-2661-4835-a5f8-2dd1e770cb50",
  "type": "user",
  "uuid": "342dba29-c2a8-4804-b35e-920ce97ff0d6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/worst/imagined_experiments.yaml",
      "content": "tier: worst\nnarrative_guidance: Major reframe to signal-characterization + impossibility paper.\n  Min-K++ reversal is the robust novel finding. Fisher Information impossibility becomes\n  co-primary contribution. Domain heterogeneity demoted to preliminary. Calibration\n  claim dropped entirely. Title pivots to 'The Limits of Contamination Detection and\n  Calibration.'\nimagined_experiments:\n- name: sft_d100_qc_only\n  plan_id: exp-015\n  description: 100% dosage SFT using only QC-pass paraphrases (7547 items) on 0.5B.\n    Isolates noisy vs clean contamination.\n  expected_results:\n    mmlu_accuracy_d100_qc: 0.238\n    arc_accuracy_d100_qc: 0.241\n    gsm8k_accuracy_d100_qc: 0.362\n    humaneval_pass1: 0.079\n    mmlu_delta_vs_d100_all: 0.005\n    arc_delta_vs_d100_all: -0.053\n    mmlu_delta_vs_d000: -0.162\n    arc_delta_vs_d000: -0.228\n    gamma_qc_vs_all_diff: <0.15 (non-significant)\n    position_bias_A_pct: 0.96\n  result_rationale: 'At 0.5B, the catastrophic forgetting on MC benchmarks is driven\n    by position bias amplification (D045), not contamination quality. QC-filtered\n    paraphrases are semantically tighter but the model lacks capacity to exploit semantic\n    content — it merely learns surface patterns regardless of paraphrase quality.\n    The QC-only vs all-paraphrase difference is negligible because the failure mode\n    is capacity-level (SFT displaces existing weak representations), not noise-level.\n    This confirms Concern #22: the 0.5B effect is a capacity artifact, making the\n    QC distinction irrelevant at this scale. The experiment produces a null result\n    that strengthens the impossibility framing — even ''perfect'' contamination doesn''t\n    produce interpretable IRT signal at sub-1B scale.'\n  tables:\n  - 'Table: QC-only vs All-paraphrase accuracy comparison at 0.5B d100 (MMLU, ARC,\n    GSM8K). Shows <1pp difference on MC benchmarks, confirming capacity-driven failure.'\n  figures_description:\n  - 'Bar chart comparing d100-all vs d100-qc vs d000 accuracy across benchmarks. Visual\n    punch: both contaminated variants collapse equally, demonstrating capacity artifact.'\n  analysis: 'Null result. QC filtering doesn''t rescue the 0.5B IRT signal. Paper\n    uses this to formally argue that contamination detection/calibration requires\n    minimum model capacity — below ~1B parameters, SFT-based contamination produces\n    capacity displacement indistinguishable from general catastrophic forgetting.\n    Supports impossibility framing: even with perfect contamination injection, IRT\n    γ estimation is confounded by capacity effects at small scale.'\n- name: scale_bridging_7b\n  plan_id: exp-007\n  description: Qwen2.5-7B controlled SFT at 5 dosage levels. Tests whether γ persists\n    at larger scale.\n  expected_results:\n    arc_accuracy_d000: 0.875\n    arc_accuracy_d005: 0.873\n    arc_accuracy_d025: 0.871\n    arc_accuracy_d100: 0.868\n    arc_delta_d100_vs_d000: -0.007\n    mmlu_accuracy_d000: 0.72\n    mmlu_accuracy_d100: 0.718\n    mmlu_delta_d100_vs_d000: -0.002\n    gsm8k_accuracy_d000: 0.78\n    gsm8k_accuracy_d100: 0.785\n    gsm8k_delta_d100_vs_d000: 0.005\n    arc_gamma_7b: -0.12\n    arc_gamma_7b_ci:\n    - -0.58\n    - 0.34\n    arc_gamma_ci_excludes_zero: false\n    mmlu_gamma_7b: -0.03\n    mmlu_gamma_7b_ci:\n    - -0.45\n    - 0.39\n    gsm8k_gamma_7b: 0.08\n    gsm8k_gamma_7b_ci:\n    - -0.52\n    - 0.68\n    s1_auc_d005_7b: 0.96\n    s2_cohens_d_7b: -0.3\n    coverage_95: 0.28\n    calibrated_mae_arc: 0.009\n    raw_mae_arc: 0.007\n    irt_worse_than_raw: true\n  result_rationale: 'At 7B, the model has sufficient capacity that SFT contamination\n    injection produces near-zero accuracy change — the model already ''knows'' ARC/MMLU\n    content from pretraining, and additional SFT exposure doesn''t meaningfully alter\n    performance. The ARC forgetting effect that was -17pp at 0.5B and -1pp at 3B attenuates\n    to <1pp noise at 7B. γ CI includes zero for all benchmarks. This is the worst-case\n    confirmation of Concern #22: the contamination effect measured by IRT is entirely\n    a small-model capacity artifact. At 7B, there''s nothing to calibrate — raw scores\n    ARE the clean scores within noise. IRT calibration produces MAE worse than raw\n    because it''s fitting noise. The signal (S1) still detects contaminated items\n    (AUC=0.96) but this detection has no downstream utility because contamination\n    doesn''t affect scores. This creates a fundamental disconnect: detection works\n    but calibration is unnecessary.'\n  tables:\n  - 'Table: Dosage × accuracy across scales (0.5B/1.5B/3B/7B). Shows monotonic attenuation\n    of contamination effect with scale.'\n  - 'Table: γ estimates and CIs by scale. Shows significant γ only at 0.5B, non-significant\n    at 3B+.'\n  figures_description:\n  - Scale × dosage heatmap showing contamination effect magnitude. Clear gradient\n    from catastrophic (0.5B) to negligible (7B). Visually compelling for the 'scale-dependent\n    sensitivity' narrative.\n  - γ forest plot across scales with CIs. 0.5B CI excludes zero; 3B borderline; 7B\n    centered on zero.\n  analysis: 'Devastating for calibration claim but powerful for characterization.\n    Reframes as: contamination effects are scale-dependent with a critical threshold\n    around 1-3B parameters. Below threshold: catastrophic capacity displacement. Above\n    threshold: near-immunity. This is a structural insight about the LLM evaluation\n    ecosystem — current benchmark contamination is primarily a small-model problem.\n    For the impossibility paper: proves that γ recovery is confounded with scale-dependent\n    capacity effects, making IRT calibration unreliable precisely where it''s needed\n    most (models too small to be robust) and unnecessary where it works (models large\n    enough to be robust).'\n- name: multi_family_validation\n  plan_id: exp-014\n  description: Llama-3.2-1B (or similar) SFT injection at d000/d025/d100. Tests cross-family\n    generalizability.\n  expected_results:\n    llama_arc_d000: 0.42\n    llama_arc_d025: 0.41\n    llama_arc_d100: 0.39\n    llama_arc_delta_d100: -0.03\n    llama_mmlu_d000: 0.38\n    llama_mmlu_d100: 0.36\n    llama_gsm8k_d000: 0.28\n    llama_gsm8k_d100: 0.29\n    llama_arc_gamma: -0.18\n    llama_arc_gamma_ci:\n    - -0.95\n    - 0.59\n    llama_arc_gamma_ci_excludes_zero: false\n    llama_mmlu_gamma: -0.09\n    llama_mmlu_gamma_ci:\n    - -0.72\n    - 0.54\n    llama_gsm8k_gamma: 0.06\n    llama_gsm8k_gamma_ci:\n    - -0.61\n    - 0.73\n    s1_auc_llama_d005: 0.94\n    s2_cohens_d_llama: -1.4\n    cross_family_gamma_rank_tau: 0.2\n    cross_family_gamma_rank_tau_p: 0.42\n    position_bias_llama: moderate (A=55% at d100)\n  result_rationale: 'Llama-3.2-1B at ~1B params sits in the capacity-limited regime\n    where contamination effects are dominated by SFT capacity displacement rather\n    than benchmark-specific memorization. The model shows weak negative ARC gamma\n    (forgetting) but CI includes zero — not enough power to distinguish from noise\n    at N=3 models. Critically, the gamma ranking across benchmarks doesn''t correlate\n    with Qwen''s ranking (tau=0.2, p=0.42), suggesting that contamination susceptibility\n    patterns are model-family-specific rather than benchmark-intrinsic properties.\n    This invalidates the ''benchmark × domain property'' interpretation from Claim\n    1. The Min-K++ reversal replicates (Cohen''s d=-1.4), confirming this is a scale\n    phenomenon not family-specific. S1 still works (AUC=0.94). Overall: detection\n    signals generalize but calibration patterns don''t — the heterogeneity is model\n    × scale × benchmark, too complex for a simple γ_k characterization.'\n  tables:\n  - 'Table: Llama vs Qwen γ comparison by benchmark. Shows non-significant γ for Llama\n    on all benchmarks.'\n  - 'Table: Cross-family gamma rank correlation (Kendall tau). Shows tau≈0.2, not\n    significant.'\n  figures_description:\n  - 'Paired forest plot: Qwen γ vs Llama γ by benchmark. Llama CIs all cross zero.\n    Visual shows family-specificity.'\n  analysis: 'Kills the ''contamination susceptibility as benchmark property'' narrative.\n    If γ patterns differ by model family, the characterization framework loses generalizability.\n    For worst-tier pivot: this becomes evidence for the impossibility argument — contamination\n    effects are too heterogeneous across model families for any single IRT framework\n    to characterize universally. Paper reframes as ''we demonstrate that contamination-performance\n    relationships are family × scale × benchmark specific, making universal calibration\n    provably infeasible.'' The Min-K++ reversal replication across families is the\n    salvageable finding.'\n- name: rl_observational_case_study\n  plan_id: exp-009\n  description: Apply signals to RL-trained models (Qwen-Instruct, DeepSeek-R1-Distill).\n    Observational external validity.\n  expected_results:\n    qwen_instruct_05b_arc_gamma: 0.15\n    qwen_instruct_05b_arc_ci:\n    - -1.2\n    - 1.5\n    qwen_instruct_15b_arc_gamma: 0.08\n    qwen_instruct_15b_arc_ci:\n    - -0.9\n    - 1.1\n    qwen_instruct_7b_arc_gamma: -0.02\n    qwen_instruct_7b_arc_ci:\n    - -0.7\n    - 0.65\n    deepseek_r1_distill_15b_gamma: 0.22\n    deepseek_r1_distill_15b_ci:\n    - -0.8\n    - 1.3\n    all_gamma_ci_include_zero: true\n    s1_auc_instruct_models: 0.72\n    s2_auc_instruct_models: 0.48\n    s4_auc_instruct_models: 0.51\n    coverage_95: 0.22\n    calibrated_mae: 0.085\n    raw_mae: 0.032\n    calibration_worse_than_raw: true\n    regret_uncalibrated_top5: 0.02\n    regret_calibrated_top5: 0.07\n    near_zero_gamma_clean_bench: true\n    ppp_all_models: '[0.0, 0.05]'\n  result_rationale: 'RL-trained models have undergone post-training that fundamentally\n    alters the contamination-performance relationship compared to SFT. Instruct/RL\n    models show broader capability generalization, so even if benchmark items leaked\n    into pretraining, the RL alignment training redistributes this knowledge. Detection\n    signals degrade: S1 drops to 0.72 (RL changes embedding space), S2/S4 remain near\n    chance. Without reliable exposure scores, IRT γ estimation is underpowered — all\n    CIs include zero with massive width. Calibration produces overcorrection (MAE\n    2.7× worse than raw) because the model assigns non-zero exposure to items the\n    RL model handles through genuine capability rather than memorization. The regret\n    analysis shows calibration actively harms model selection (picks wrong models).\n    Near-zero γ on clean benchmark confirms specificity, but this merely validates\n    that the method doesn''t false-positive — it doesn''t validate that it correctly\n    identifies contamination in RL models.'\n  tables:\n  - 'Table: γ estimates for observational models with CIs. All include zero.'\n  - 'Table: Expected regret comparison — uncalibrated vs calibrated for top-5 selection.\n    Shows calibration increases regret.'\n  figures_description:\n  - Regret comparison bar chart. Uncalibrated < Calibrated for top-5 selection, demonstrating\n    calibration harm.\n  - 'Signal AUC comparison: controlled SFT vs observational RL. Shows degradation\n    of detection signals post-RL.'\n  analysis: 'Complete failure of the calibration pipeline on ecologically valid models.\n    The controlled SFT setting is the only regime where IRT+γ produces interpretable\n    results, and that regime is artificial. For the impossibility paper this is golden:\n    ''Our framework successfully characterizes contamination in controlled settings\n    but cannot reliably extend to real-world RL-trained models because (a) detection\n    signals degrade post-RL, (b) the contamination-performance relationship changes\n    under alignment training, and (c) N is too small for reliable γ estimation. This\n    is not a fixable engineering problem — it''s a structural limitation of post-hoc\n    calibration approaches.'' The near-zero-on-clean result is salvageable as evidence\n    the method has specificity even when lacking sensitivity.'\n- name: observational_72b\n  plan_id: exp-012\n  description: Qwen2.5-72B inference-only. Extends ecological validity to frontier\n    scale.\n  expected_results:\n    arc_accuracy_72b: 0.92\n    mmlu_accuracy_72b: 0.82\n    gsm8k_accuracy_72b: 0.88\n    s1_auc_72b: 0.68\n    s2_signal_72b: not applicable (no logprob access via API)\n    s4_auc_72b: 0.53\n    arc_gamma_72b: 0.04\n    arc_gamma_ci:\n    - -0.85\n    - 0.93\n    mmlu_gamma_72b: 0.11\n    mmlu_gamma_ci:\n    - -0.62\n    - 0.84\n    coverage_95: 0.18\n    calibrated_mae: 0.065\n    raw_mae: 0.015\n    ppp: 0.01\n    n_models_with_72b: 1\n  result_rationale: 'At 72B with only 1 observational model (no dosage variation),\n    IRT is fundamentally underpowered. N=1 additional model contributes almost no\n    information to γ estimation. S1 detection degrades at 72B because the embedding\n    space is more diffuse and pretraining already covers most benchmark content —\n    cosine similarity between benchmark items and training data is uniformly high,\n    reducing discriminative power (AUC drops to 0.68). Even if contamination exists,\n    the model''s genuine capability dominates performance. Calibration overcorrects\n    because the prior dominates the likelihood at N≈1 effective observations. PPP≈0\n    indicates systematic misspecification. This demonstrates the Fisher Information\n    impossibility empirically: at frontier scale, you cannot identify contamination\n    effects without many controlled models at that scale, which defeats the purpose\n    of post-hoc calibration.'\n  tables:\n  - 'Table: 72B metrics alongside 0.5B/1.5B/3B/7B for scale comparison. Shows monotonic\n    γ attenuation.'\n  figures_description:\n  - 'Extended scale plot: γ magnitude vs model parameters (log scale). Shows clear\n    decay toward zero, asymptoting by 7B.'\n  analysis: 'Provides the capstone for the scale-dependency narrative. At frontier\n    scale: (a) contamination effects are undetectable, (b) detection signals degrade,\n    (c) IRT is underpowered with N=1. The impossibility is triply confirmed. Paper\n    frames this as: ''Current LLM evaluation operates in a regime where the models\n    most likely contaminated (frontier, trained on massive web data) are precisely\n    those where calibration is provably infeasible — signals are weak, effects are\n    negligible, and sample sizes are fundamentally insufficient.'' This is a genuine\n    structural insight about the evaluation ecosystem.'\n- name: closed_weight_2signal_mode\n  plan_id: exp-013\n  description: Degraded 2-signal mode (ConStat + Self-Critique only). Quantifies closed-weight\n    calibration gap.\n  expected_results:\n    rrf_2signal_auc_d005: 0.52\n    rrf_4signal_auc_d005: 0.97\n    auc_gap: 0.45\n    gamma_2signal_arc: -0.08\n    gamma_2signal_ci:\n    - -1.4\n    - 1.25\n    gamma_2signal_ci_excludes_zero: false\n    gamma_4signal_arc: -1.46\n    calibrated_mae_2signal: 0.092\n    calibrated_mae_4signal: 0.035\n    mae_degradation_factor: 2.6\n    coverage_95_2signal: 0.15\n    ranking_tau_2signal: 0.31\n    ranking_tau_4signal: 0.76\n  result_rationale: ConStat (S3) was never computed in our pipeline (only S1/S2/S4\n    exist). If we interpret '2-signal' as S2+S4 (the non-embedding signals), both\n    are near chance at 0.5B (AUC≈0.47-0.48 from exp-008 results). RRF over two random\n    signals produces composite AUC≈0.52 — barely above chance. Without S1 (the only\n    effective signal), the entire pipeline collapses. γ estimation with AUC≈0.52 exposure\n    scores is well below the exp-004 identifiability threshold (AUC≥0.55 minimum).\n    The IRT model cannot distinguish contaminated from clean items, so γ CI spans\n    zero with massive width. Calibrated MAE is 2.6× worse than 4-signal because the\n    model is fitting noise. This proves that ContamCal in closed-weight mode (no embeddings/logprobs)\n    is fundamentally non-functional — it's not a graceful degradation, it's a total\n    failure. The 4-signal pipeline is really a 1-signal pipeline (S1), and S1 requires\n    weight access.\n  tables:\n  - 'Table: 2-signal vs 4-signal (effectively 1-signal S1) performance comparison\n    across all metrics.'\n  - 'Table: Per-signal AUC at 0.5B showing S2/S4 at chance level.'\n  figures_description:\n  - AUC comparison showing 4-signal (=S1 dominant) vs 2-signal (=noise). Dramatic\n    gap visualization.\n  analysis: 'Confirms that ContamCal has zero practical applicability to closed-weight\n    models. The method is entirely dependent on embedding-based detection (S1), which\n    requires model weights. For the impossibility paper: this eliminates the ''practical\n    tool'' positioning. The paper must acknowledge that contamination calibration\n    requires open-weight access, limiting applicability to exactly the models where\n    contamination is least problematic (open-weight models are typically smaller/less\n    contaminated than proprietary frontier models). This is another impossibility\n    result: the models most needing calibration (closed-weight, trained on undisclosed\n    data) are precisely those where the method cannot work.'\n",
      "numLines": 334,
      "startLine": 1,
      "totalLines": 334
    }
  },
  "sourceToolAssistantUUID": "33cf72ea-6481-4c90-b3e7-bea903f75111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T16:22:41.032Z_

<details open><summary>🔧 Tool call — Read · `toolu_018QVSppg588CqSfnNVD4Etj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "342dba29-c2a8-4804-b35e-920ce97ff0d6",
  "isSidechain": false,
  "requestId": "req_011Cb6ZBmThqzefUL3HF1XEA",
  "type": "assistant",
  "uuid": "5bb951a3-5e1a-4d15-8e30-db1d6150e4a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SshfFcvGNqMiQSnNLh4EF2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 53728,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 53728,
          "cache_creation_input_tokens": 1923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1923
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

### Tool result

_source line 14 · 2026-05-16T16:22:41.036Z_

<details><summary>↩ Tool result · `toolu_018QVSppg588CqSfnNVD4Etj`</summary>

```text
1	narrative_guidance: Major reframe to signal-characterization + impossibility paper.
2	  Min-K++ reversal is the robust novel finding. Fisher Information impossibility becomes
3	  co-primary contribution. Domain heterogeneity demoted to preliminary. Calibration
4	  claim dropped entirely. Title pivots to 'The Limits of Contamination Detection and
5	  Calibration.'
6	imagined_experiments:
7	- name: sft_d100_qc_only
8	  plan_id: exp-015
9	  description: 100% dosage SFT using only QC-pass paraphrases (7547 items) on 0.5B.
10	    Isolates noisy vs clean contamination.
11	  expected_results:
12	    mmlu_accuracy_d100_qc: 0.238
13	    arc_accuracy_d100_qc: 0.241
14	    gsm8k_accuracy_d100_qc: 0.362
15	    humaneval_pass1: 0.079
16	    mmlu_delta_vs_d100_all: 0.005
17	    arc_delta_vs_d100_all: -0.053
18	    mmlu_delta_vs_d000: -0.162
19	    arc_delta_vs_d000: -0.228
20	    gamma_qc_vs_all_diff: <0.15 (non-significant)
21	    position_bias_A_pct: 0.96
22	  result_rationale: 'At 0.5B, the catastrophic forgetting on MC benchmarks is driven
23	    by position bias amplification (D045), not contamination quality. QC-filtered
24	    paraphrases are semantically tighter but the model lacks capacity to exploit semantic
25	    content — it merely learns surface patterns regardless of paraphrase quality.
26	    The QC-only vs all-paraphrase difference is negligible because the failure mode
27	    is capacity-level (SFT displaces existing weak representations), not noise-level.
28	    This confirms Concern #22: the 0.5B effect is a capacity artifact, making the
29	    QC distinction irrelevant at this scale. The experiment produces a null result
30	    that strengthens the impossibility framing — even ''perfect'' contamination doesn''t
31	    produce interpretable IRT signal at sub-1B scale.'
32	  tables:
33	  - 'Table: QC-only vs All-paraphrase accuracy comparison at 0.5B d100 (MMLU, ARC,
34	    GSM8K). Shows <1pp difference on MC benchmarks, confirming capacity-driven failure.'
35	  figures_description:
36	  - 'Bar chart comparing d100-all vs d100-qc vs d000 accuracy across benchmarks. Visual
37	    punch: both contaminated variants collapse equally, demonstrating capacity artifact.'
38	  analysis: 'Null result. QC filtering doesn''t rescue the 0.5B IRT signal. Paper
39	    uses this to formally argue that contamination detection/calibration requires
40	    minimum model capacity — below ~1B parameters, SFT-based contamination produces
41	    capacity displacement indistinguishable from general catastrophic forgetting.
42	    Supports impossibility framing: even with perfect contamination injection, IRT
43	    γ estimation is confounded by capacity effects at small scale.'
44	- name: scale_bridging_7b
45	  plan_id: exp-007
46	  description: Qwen2.5-7B controlled SFT at 5 dosage levels. Tests whether γ persists
47	    at larger scale.
48	  expected_results:
49	    arc_accuracy_d000: 0.875
50	    arc_accuracy_d005: 0.873
51	    arc_accuracy_d025: 0.871
52	    arc_accuracy_d100: 0.868
53	    arc_delta_d100_vs_d000: -0.007
54	    mmlu_accuracy_d000: 0.72
55	    mmlu_accuracy_d100: 0.718
56	    mmlu_delta_d100_vs_d000: -0.002
57	    gsm8k_accuracy_d000: 0.78
58	    gsm8k_accuracy_d100: 0.785
59	    gsm8k_delta_d100_vs_d000: 0.005
60	    arc_gamma_7b: -0.12
61	    arc_gamma_7b_ci:
62	    - -0.58
63	    - 0.34
64	    arc_gamma_ci_excludes_zero: false
65	    mmlu_gamma_7b: -0.03
66	    mmlu_gamma_7b_ci:
67	    - -0.45
68	    - 0.39
69	    gsm8k_gamma_7b: 0.08
70	    gsm8k_gamma_7b_ci:
71	    - -0.52
72	    - 0.68
73	    s1_auc_d005_7b: 0.96
74	    s2_cohens_d_7b: -0.3
75	    coverage_95: 0.28
76	    calibrated_mae_arc: 0.009
77	    raw_mae_arc: 0.007
78	    irt_worse_than_raw: true
79	  result_rationale: 'At 7B, the model has sufficient capacity that SFT contamination
80	    injection produces near-zero accuracy change — the model already ''knows'' ARC/MMLU
81	    content from pretraining, and additional SFT exposure doesn''t meaningfully alter
82	    performance. The ARC forgetting effect that was -17pp at 0.5B and -1pp at 3B attenuates
83	    to <1pp noise at 7B. γ CI includes zero for all benchmarks. This is the worst-case
84	    confirmation of Concern #22: the contamination effect measured by IRT is entirely
85	    a small-model capacity artifact. At 7B, there''s nothing to calibrate — raw scores
86	    ARE the clean scores within noise. IRT calibration produces MAE worse than raw
87	    because it''s fitting noise. The signal (S1) still detects contaminated items
88	    (AUC=0.96) but this detection has no downstream utility because contamination
89	    doesn''t affect scores. This creates a fundamental disconnect: detection works
90	    but calibration is unnecessary.'
91	  tables:
92	  - 'Table: Dosage × accuracy across scales (0.5B/1.5B/3B/7B). Shows monotonic attenuation
93	    of contamination effect with scale.'
94	  - 'Table: γ estimates and CIs by scale. Shows significant γ only at 0.5B, non-significant
95	    at 3B+.'
96	  figures_description:
97	  - Scale × dosage heatmap showing contamination effect magnitude. Clear gradient
98	    from catastrophic (0.5B) to negligible (7B). Visually compelling for the 'scale-dependent
99	    sensitivity' narrative.
100	  - γ forest plot across scales with CIs. 0.5B CI excludes zero; 3B borderline; 7B
101	    centered on zero.
102	  analysis: 'Devastating for calibration claim but powerful for characterization.
103	    Reframes as: contamination effects are scale-dependent with a critical threshold
104	    around 1-3B parameters. Below threshold: catastrophic capacity displacement. Above
105	    threshold: near-immunity. This is a structural insight about the LLM evaluation
106	    ecosystem — current benchmark contamination is primarily a small-model problem.
107	    For the impossibility paper: proves that γ recovery is confounded with scale-dependent
108	    capacity effects, making IRT calibration unreliable precisely where it''s needed
109	    most (models too small to be robust) and unnecessary where it works (models large
110	    enough to be robust).'
111	- name: multi_family_validation
112	  plan_id: exp-014
113	  description: Llama-3.2-1B (or similar) SFT injection at d000/d025/d100. Tests cross-family
114	    generalizability.
115	  expected_results:
116	    llama_arc_d000: 0.42
117	    llama_arc_d025: 0.41
118	    llama_arc_d100: 0.39
119	    llama_arc_delta_d100: -0.03
120	    llama_mmlu_d000: 0.38
121	    llama_mmlu_d100: 0.36
122	    llama_gsm8k_d000: 0.28
123	    llama_gsm8k_d100: 0.29
124	    llama_arc_gamma: -0.18
125	    llama_arc_gamma_ci:
126	    - -0.95
127	    - 0.59
128	    llama_arc_gamma_ci_excludes_zero: false
129	    llama_mmlu_gamma: -0.09
130	    llama_mmlu_gamma_ci:
131	    - -0.72
132	    - 0.54
133	    llama_gsm8k_gamma: 0.06
134	    llama_gsm8k_gamma_ci:
135	    - -0.61
136	    - 0.73
137	    s1_auc_llama_d005: 0.94
138	    s2_cohens_d_llama: -1.4
139	    cross_family_gamma_rank_tau: 0.2
140	    cross_family_gamma_rank_tau_p: 0.42
141	    position_bias_llama: moderate (A=55% at d100)
142	  result_rationale: 'Llama-3.2-1B at ~1B params sits in the capacity-limited regime
143	    where contamination effects are dominated by SFT capacity displacement rather
144	    than benchmark-specific memorization. The model shows weak negative ARC gamma
145	    (forgetting) but CI includes zero — not enough power to distinguish from noise
146	    at N=3 models. Critically, the gamma ranking across benchmarks doesn''t correlate
147	    with Qwen''s ranking (tau=0.2, p=0.42), suggesting that contamination susceptibility
148	    patterns are model-family-specific rather than benchmark-intrinsic properties.
149	    This invalidates the ''benchmark × domain property'' interpretation from Claim
150	    1. The Min-K++ reversal replicates (Cohen''s d=-1.4), confirming this is a scale
151	    phenomenon not family-specific. S1 still works (AUC=0.94). Overall: detection
152	    signals generalize but calibration patterns don''t — the heterogeneity is model
153	    × scale × benchmark, too complex for a simple γ_k characterization.'
154	  tables:
155	  - 'Table: Llama vs Qwen γ comparison by benchmark. Shows non-significant γ for Llama
156	    on all benchmarks.'
157	  - 'Table: Cross-family gamma rank correlation (Kendall tau). Shows tau≈0.2, not
158	    significant.'
159	  figures_description:
160	  - 'Paired forest plot: Qwen γ vs Llama γ by benchmark. Llama CIs all cross zero.
161	    Visual shows family-specificity.'
162	  analysis: 'Kills the ''contamination susceptibility as benchmark property'' narrative.
163	    If γ patterns differ by model family, the characterization framework loses generalizability.
164	    For worst-tier pivot: this becomes evidence for the impossibility argument — contamination
165	    effects are too heterogeneous across model families for any single IRT framework
166	    to characterize universally. Paper reframes as ''we demonstrate that contamination-performance
167	    relationships are family × scale × benchmark specific, making universal calibration
168	    provably infeasible.'' The Min-K++ reversal replication across families is the
169	    salvageable finding.'
170	- name: rl_observational_case_study
171	  plan_id: exp-009
172	  description: Apply signals to RL-trained models (Qwen-Instruct, DeepSeek-R1-Distill).
173	    Observational external validity.
174	  expected_results:
175	    qwen_instruct_05b_arc_gamma: 0.15
176	    qwen_instruct_05b_arc_ci:
177	    - -1.2
178	    - 1.5
179	    qwen_instruct_15b_arc_gamma: 0.08
180	    qwen_instruct_15b_arc_ci:
181	    - -0.9
182	    - 1.1
183	    qwen_instruct_7b_arc_gamma: -0.02
184	    qwen_instruct_7b_arc_ci:
185	    - -0.7
186	    - 0.65
187	    deepseek_r1_distill_15b_gamma: 0.22
188	    deepseek_r1_distill_15b_ci:
189	    - -0.8
190	    - 1.3
191	    all_gamma_ci_include_zero: true
192	    s1_auc_instruct_models: 0.72
193	    s2_auc_instruct_models: 0.48
194	    s4_auc_instruct_models: 0.51
195	    coverage_95: 0.22
196	    calibrated_mae: 0.085
197	    raw_mae: 0.032
198	    calibration_worse_than_raw: true
199	    regret_uncalibrated_top5: 0.02
200	    regret_calibrated_top5: 0.07
201	    near_zero_gamma_clean_bench: true
202	    ppp_all_models: '[0.0, 0.05]'
203	  result_rationale: 'RL-trained models have undergone post-training that fundamentally
204	    alters the contamination-performance relationship compared to SFT. Instruct/RL
205	    models show broader capability generalization, so even if benchmark items leaked
206	    into pretraining, the RL alignment training redistributes this knowledge. Detection
207	    signals degrade: S1 drops to 0.72 (RL changes embedding space), S2/S4 remain near
208	    chance. Without reliable exposure scores, IRT γ estimation is underpowered — all
209	    CIs include zero with massive width. Calibration produces overcorrection (MAE
210	    2.7× worse than raw) because the model assigns non-zero exposure to items the
211	    RL model handles through genuine capability rather than memorization. The regret
212	    analysis shows calibration actively harms model selection (picks wrong models).
213	    Near-zero γ on clean benchmark confirms specificity, but this merely validates
214	    that the method doesn''t false-positive — it doesn''t validate that it correctly
215	    identifies contamination in RL models.'
216	  tables:
217	  - 'Table: γ estimates for observational models with CIs. All include zero.'
218	  - 'Table: Expected regret comparison — uncalibrated vs calibrated for top-5 selection.
219	    Shows calibration increases regret.'
220	  figures_description:
221	  - Regret comparison bar chart. Uncalibrated < Calibrated for top-5 selection, demonstrating
222	    calibration harm.
223	  - 'Signal AUC comparison: controlled SFT vs observational RL. Shows degradation
224	    of detection signals post-RL.'
225	  analysis: 'Complete failure of the calibration pipeline on ecologically valid models.
226	    The controlled SFT setting is the only regime where IRT+γ produces interpretable
227	    results, and that regime is artificial. For the impossibility paper this is golden:
228	    ''Our framework successfully characterizes contamination in controlled settings
229	    but cannot reliably extend to real-world RL-trained models because (a) detection
230	    signals degrade post-RL, (b) the contamination-performance relationship changes
231	    under alignment training, and (c) N is too small for reliable γ estimation. This
232	    is not a fixable engineering problem — it''s a structural limitation of post-hoc
233	    calibration approaches.'' The near-zero-on-clean result is salvageable as evidence
234	    the method has specificity even when lacking sensitivity.'
235	- name: observational_72b
236	  plan_id: exp-012
237	  description: Qwen2.5-72B inference-only. Extends ecological validity to frontier
238	    scale.
239	  expected_results:
240	    arc_accuracy_72b: 0.92
241	    mmlu_accuracy_72b: 0.82
242	    gsm8k_accuracy_72b: 0.88
243	    s1_auc_72b: 0.68
244	    s2_signal_72b: not applicable (no logprob access via API)
245	    s4_auc_72b: 0.53
246	    arc_gamma_72b: 0.04
247	    arc_gamma_ci:
248	    - -0.85
249	    - 0.93
250	    mmlu_gamma_72b: 0.11
251	    mmlu_gamma_ci:
252	    - -0.62
253	    - 0.84
254	    coverage_95: 0.18
255	    calibrated_mae: 0.065
256	    raw_mae: 0.015
257	    ppp: 0.01
258	    n_models_with_72b: 1
259	  result_rationale: 'At 72B with only 1 observational model (no dosage variation),
260	    IRT is fundamentally underpowered. N=1 additional model contributes almost no
261	    information to γ estimation. S1 detection degrades at 72B because the embedding
262	    space is more diffuse and pretraining already covers most benchmark content —
263	    cosine similarity between benchmark items and training data is uniformly high,
264	    reducing discriminative power (AUC drops to 0.68). Even if contamination exists,
265	    the model''s genuine capability dominates performance. Calibration overcorrects
266	    because the prior dominates the likelihood at N≈1 effective observations. PPP≈0
267	    indicates systematic misspecification. This demonstrates the Fisher Information
268	    impossibility empirically: at frontier scale, you cannot identify contamination
269	    effects without many controlled models at that scale, which defeats the purpose
270	    of post-hoc calibration.'
271	  tables:
272	  - 'Table: 72B metrics alongside 0.5B/1.5B/3B/7B for scale comparison. Shows monotonic
273	    γ attenuation.'
274	  figures_description:
275	  - 'Extended scale plot: γ magnitude vs model parameters (log scale). Shows clear
276	    decay toward zero, asymptoting by 7B.'
277	  analysis: 'Provides the capstone for the scale-dependency narrative. At frontier
278	    scale: (a) contamination effects are undetectable, (b) detection signals degrade,
279	    (c) IRT is underpowered with N=1. The impossibility is triply confirmed. Paper
280	    frames this as: ''Current LLM evaluation operates in a regime where the models
281	    most likely contaminated (frontier, trained on massive web data) are precisely
282	    those where calibration is provably infeasible — signals are weak, effects are
283	    negligible, and sample sizes are fundamentally insufficient.'' This is a genuine
284	    structural insight about the evaluation ecosystem.'
285	- name: closed_weight_2signal_mode
286	  plan_id: exp-013
287	  description: Degraded 2-signal mode (ConStat + Self-Critique only). Quantifies closed-weight
288	    calibration gap.
289	  expected_results:
290	    rrf_2signal_auc_d005: 0.52
291	    rrf_4signal_auc_d005: 0.97
292	    auc_gap: 0.45
293	    gamma_2signal_arc: -0.08
294	    gamma_2signal_ci:
295	    - -1.4
296	    - 1.25
297	    gamma_2signal_ci_excludes_zero: false
298	    gamma_4signal_arc: -1.46
299	    calibrated_mae_2signal: 0.092
300	    calibrated_mae_4signal: 0.035
301	    mae_degradation_factor: 2.6
302	    coverage_95_2signal: 0.15
303	    ranking_tau_2signal: 0.31
304	    ranking_tau_4signal: 0.76
305	  result_rationale: ConStat (S3) was never computed in our pipeline (only S1/S2/S4
306	    exist). If we interpret '2-signal' as S2+S4 (the non-embedding signals), both
307	    are near chance at 0.5B (AUC≈0.47-0.48 from exp-008 results). RRF over two random
308	    signals produces composite AUC≈0.52 — barely above chance. Without S1 (the only
309	    effective signal), the entire pipeline collapses. γ estimation with AUC≈0.52 exposure
310	    scores is well below the exp-004 identifiability threshold (AUC≥0.55 minimum).
311	    The IRT model cannot distinguish contaminated from clean items, so γ CI spans
312	    zero with massive width. Calibrated MAE is 2.6× worse than 4-signal because the
313	    model is fitting noise. This proves that ContamCal in closed-weight mode (no embeddings/logprobs)
314	    is fundamentally non-functional — it's not a graceful degradation, it's a total
315	    failure. The 4-signal pipeline is really a 1-signal pipeline (S1), and S1 requires
316	    weight access.
317	  tables:
318	  - 'Table: 2-signal vs 4-signal (effectively 1-signal S1) performance comparison
319	    across all metrics.'
320	  - 'Table: Per-signal AUC at 0.5B showing S2/S4 at chance level.'
321	  figures_description:
322	  - AUC comparison showing 4-signal (=S1 dominant) vs 2-signal (=noise). Dramatic
323	    gap visualization.
324	  analysis: 'Confirms that ContamCal has zero practical applicability to closed-weight
325	    models. The method is entirely dependent on embedding-based detection (S1), which
326	    requires model weights. For the impossibility paper: this eliminates the ''practical
327	    tool'' positioning. The paper must acknowledge that contamination calibration
328	    requires open-weight access, limiting applicability to exactly the models where
329	    contamination is least problematic (open-weight models are typically smaller/less
330	    contaminated than proprietary frontier models). This is another impossibility
331	    result: the models most needing calibration (closed-weight, trained on undisclosed
332	    data) are precisely those where the method cannot work.'
333	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bb951a3-5e1a-4d15-8e30-db1d6150e4a7",
  "isSidechain": false,
  "promptId": "1c8788c8-2661-4835-a5f8-2dd1e770cb50",
  "type": "user",
  "uuid": "9561951d-1a4f-4db4-925d-c5717234bfa4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260516T104822/worst/review_context.yaml",
      "content": "narrative_guidance: Major reframe to signal-characterization + impossibility paper.\n  Min-K++ reversal is the robust novel finding. Fisher Information impossibility becomes\n  co-primary contribution. Domain heterogeneity demoted to preliminary. Calibration\n  claim dropped entirely. Title pivots to 'The Limits of Contamination Detection and\n  Calibration.'\nimagined_experiments:\n- name: sft_d100_qc_only\n  plan_id: exp-015\n  description: 100% dosage SFT using only QC-pass paraphrases (7547 items) on 0.5B.\n    Isolates noisy vs clean contamination.\n  expected_results:\n    mmlu_accuracy_d100_qc: 0.238\n    arc_accuracy_d100_qc: 0.241\n    gsm8k_accuracy_d100_qc: 0.362\n    humaneval_pass1: 0.079\n    mmlu_delta_vs_d100_all: 0.005\n    arc_delta_vs_d100_all: -0.053\n    mmlu_delta_vs_d000: -0.162\n    arc_delta_vs_d000: -0.228\n    gamma_qc_vs_all_diff: <0.15 (non-significant)\n    position_bias_A_pct: 0.96\n  result_rationale: 'At 0.5B, the catastrophic forgetting on MC benchmarks is driven\n    by position bias amplification (D045), not contamination quality. QC-filtered\n    paraphrases are semantically tighter but the model lacks capacity to exploit semantic\n    content — it merely learns surface patterns regardless of paraphrase quality.\n    The QC-only vs all-paraphrase difference is negligible because the failure mode\n    is capacity-level (SFT displaces existing weak representations), not noise-level.\n    This confirms Concern #22: the 0.5B effect is a capacity artifact, making the\n    QC distinction irrelevant at this scale. The experiment produces a null result\n    that strengthens the impossibility framing — even ''perfect'' contamination doesn''t\n    produce interpretable IRT signal at sub-1B scale.'\n  tables:\n  - 'Table: QC-only vs All-paraphrase accuracy comparison at 0.5B d100 (MMLU, ARC,\n    GSM8K). Shows <1pp difference on MC benchmarks, confirming capacity-driven failure.'\n  figures_description:\n  - 'Bar chart comparing d100-all vs d100-qc vs d000 accuracy across benchmarks. Visual\n    punch: both contaminated variants collapse equally, demonstrating capacity artifact.'\n  analysis: 'Null result. QC filtering doesn''t rescue the 0.5B IRT signal. Paper\n    uses this to formally argue that contamination detection/calibration requires\n    minimum model capacity — below ~1B parameters, SFT-based contamination produces\n    capacity displacement indistinguishable from general catastrophic forgetting.\n    Supports impossibility framing: even with perfect contamination injection, IRT\n    γ estimation is confounded by capacity effects at small scale.'\n- name: scale_bridging_7b\n  plan_id: exp-007\n  description: Qwen2.5-7B controlled SFT at 5 dosage levels. Tests whether γ persists\n    at larger scale.\n  expected_results:\n    arc_accuracy_d000: 0.875\n    arc_accuracy_d005: 0.873\n    arc_accuracy_d025: 0.871\n    arc_accuracy_d100: 0.868\n    arc_delta_d100_vs_d000: -0.007\n    mmlu_accuracy_d000: 0.72\n    mmlu_accuracy_d100: 0.718\n    mmlu_delta_d100_vs_d000: -0.002\n    gsm8k_accuracy_d000: 0.78\n    gsm8k_accuracy_d100: 0.785\n    gsm8k_delta_d100_vs_d000: 0.005\n    arc_gamma_7b: -0.12\n    arc_gamma_7b_ci:\n    - -0.58\n    - 0.34\n    arc_gamma_ci_excludes_zero: false\n    mmlu_gamma_7b: -0.03\n    mmlu_gamma_7b_ci:\n    - -0.45\n    - 0.39\n    gsm8k_gamma_7b: 0.08\n    gsm8k_gamma_7b_ci:\n    - -0.52\n    - 0.68\n    s1_auc_d005_7b: 0.96\n    s2_cohens_d_7b: -0.3\n    coverage_95: 0.28\n    calibrated_mae_arc: 0.009\n    raw_mae_arc: 0.007\n    irt_worse_than_raw: true\n  result_rationale: 'At 7B, the model has sufficient capacity that SFT contamination\n    injection produces near-zero accuracy change — the model already ''knows'' ARC/MMLU\n    content from pretraining, and additional SFT exposure doesn''t meaningfully alter\n    performance. The ARC forgetting effect that was -17pp at 0.5B and -1pp at 3B attenuates\n    to <1pp noise at 7B. γ CI includes zero for all benchmarks. This is the worst-case\n    confirmation of Concern #22: the contamination effect measured by IRT is entirely\n    a small-model capacity artifact. At 7B, there''s nothing to calibrate — raw scores\n    ARE the clean scores within noise. IRT calibration produces MAE worse than raw\n    because it''s fitting noise. The signal (S1) still detects contaminated items\n    (AUC=0.96) but this detection has no downstream utility because contamination\n    doesn''t affect scores. This creates a fundamental disconnect: detection works\n    but calibration is unnecessary.'\n  tables:\n  - 'Table: Dosage × accuracy across scales (0.5B/1.5B/3B/7B). Shows monotonic attenuation\n    of contamination effect with scale.'\n  - 'Table: γ estimates and CIs by scale. Shows significant γ only at 0.5B, non-significant\n    at 3B+.'\n  figures_description:\n  - Scale × dosage heatmap showing contamination effect magnitude. Clear gradient\n    from catastrophic (0.5B) to negligible (7B). Visually compelling for the 'scale-dependent\n    sensitivity' narrative.\n  - γ forest plot across scales with CIs. 0.5B CI excludes zero; 3B borderline; 7B\n    centered on zero.\n  analysis: 'Devastating for calibration claim but powerful for characterization.\n    Reframes as: contamination effects are scale-dependent with a critical threshold\n    around 1-3B parameters. Below threshold: catastrophic capacity displacement. Above\n    threshold: near-immunity. This is a structural insight about the LLM evaluation\n    ecosystem — current benchmark contamination is primarily a small-model problem.\n    For the impossibility paper: proves that γ recovery is confounded with scale-dependent\n    capacity effects, making IRT calibration unreliable precisely where it''s needed\n    most (models too small to be robust) and unnecessary where it works (models large\n    enough to be robust).'\n- name: multi_family_validation\n  plan_id: exp-014\n  description: Llama-3.2-1B (or similar) SFT injection at d000/d025/d100. Tests cross-family\n    generalizability.\n  expected_results:\n    llama_arc_d000: 0.42\n    llama_arc_d025: 0.41\n    llama_arc_d100: 0.39\n    llama_arc_delta_d100: -0.03\n    llama_mmlu_d000: 0.38\n    llama_mmlu_d100: 0.36\n    llama_gsm8k_d000: 0.28\n    llama_gsm8k_d100: 0.29\n    llama_arc_gamma: -0.18\n    llama_arc_gamma_ci:\n    - -0.95\n    - 0.59\n    llama_arc_gamma_ci_excludes_zero: false\n    llama_mmlu_gamma: -0.09\n    llama_mmlu_gamma_ci:\n    - -0.72\n    - 0.54\n    llama_gsm8k_gamma: 0.06\n    llama_gsm8k_gamma_ci:\n    - -0.61\n    - 0.73\n    s1_auc_llama_d005: 0.94\n    s2_cohens_d_llama: -1.4\n    cross_family_gamma_rank_tau: 0.2\n    cross_family_gamma_rank_tau_p: 0.42\n    position_bias_llama: moderate (A=55% at d100)\n  result_rationale: 'Llama-3.2-1B at ~1B params sits in the capacity-limited regime\n    where contamination effects are dominated by SFT capacity displacement rather\n    than benchmark-specific memorization. The model shows weak negative ARC gamma\n    (forgetting) but CI includes zero — not enough power to distinguish from noise\n    at N=3 models. Critically, the gamma ranking across benchmarks doesn''t correlate\n    with Qwen''s ranking (tau=0.2, p=0.42), suggesting that contamination susceptibility\n    patterns are model-family-specific rather than benchmark-intrinsic properties.\n    This invalidates the ''benchmark × domain property'' interpretation from Claim\n    1. The Min-K++ reversal replicates (Cohen''s d=-1.4), confirming this is a scale\n    phenomenon not family-specific. S1 still works (AUC=0.94). Overall: detection\n    signals generalize but calibration patterns don''t — the heterogeneity is model\n    × scale × benchmark, too complex for a simple γ_k characterization.'\n  tables:\n  - 'Table: Llama vs Qwen γ comparison by benchmark. Shows non-significant γ for Llama\n    on all benchmarks.'\n  - 'Table: Cross-family gamma rank correlation (Kendall tau). Shows tau≈0.2, not\n    significant.'\n  figures_description:\n  - 'Paired forest plot: Qwen γ vs Llama γ by benchmark. Llama CIs all cross zero.\n    Visual shows family-specificity.'\n  analysis: 'Kills the ''contamination susceptibility as benchmark property'' narrative.\n    If γ patterns differ by model family, the characterization framework loses generalizability.\n    For worst-tier pivot: this becomes evidence for the impossibility argument — contamination\n    effects are too heterogeneous across model families for any single IRT framework\n    to characterize universally. Paper reframes as ''we demonstrate that contamination-performance\n    relationships are family × scale × benchmark specific, making universal calibration\n    provably infeasible.'' The Min-K++ reversal replication across families is the\n    salvageable finding.'\n- name: rl_observational_case_study\n  plan_id: exp-009\n  description: Apply signals to RL-trained models (Qwen-Instruct, DeepSeek-R1-Distill).\n    Observational external validity.\n  expected_results:\n    qwen_instruct_05b_arc_gamma: 0.15\n    qwen_instruct_05b_arc_ci:\n    - -1.2\n    - 1.5\n    qwen_instruct_15b_arc_gamma: 0.08\n    qwen_instruct_15b_arc_ci:\n    - -0.9\n    - 1.1\n    qwen_instruct_7b_arc_gamma: -0.02\n    qwen_instruct_7b_arc_ci:\n    - -0.7\n    - 0.65\n    deepseek_r1_distill_15b_gamma: 0.22\n    deepseek_r1_distill_15b_ci:\n    - -0.8\n    - 1.3\n    all_gamma_ci_include_zero: true\n    s1_auc_instruct_models: 0.72\n    s2_auc_instruct_models: 0.48\n    s4_auc_instruct_models: 0.51\n    coverage_95: 0.22\n    calibrated_mae: 0.085\n    raw_mae: 0.032\n    calibration_worse_than_raw: true\n    regret_uncalibrated_top5: 0.02\n    regret_calibrated_top5: 0.07\n    near_zero_gamma_clean_bench: true\n    ppp_all_models: '[0.0, 0.05]'\n  result_rationale: 'RL-trained models have undergone post-training that fundamentally\n    alters the contamination-performance relationship compared to SFT. Instruct/RL\n    models show broader capability generalization, so even if benchmark items leaked\n    into pretraining, the RL alignment training redistributes this knowledge. Detection\n    signals degrade: S1 drops to 0.72 (RL changes embedding space), S2/S4 remain near\n    chance. Without reliable exposure scores, IRT γ estimation is underpowered — all\n    CIs include zero with massive width. Calibration produces overcorrection (MAE\n    2.7× worse than raw) because the model assigns non-zero exposure to items the\n    RL model handles through genuine capability rather than memorization. The regret\n    analysis shows calibration actively harms model selection (picks wrong models).\n    Near-zero γ on clean benchmark confirms specificity, but this merely validates\n    that the method doesn''t false-positive — it doesn''t validate that it correctly\n    identifies contamination in RL models.'\n  tables:\n  - 'Table: γ estimates for observational models with CIs. All include zero.'\n  - 'Table: Expected regret comparison — uncalibrated vs calibrated for top-5 selection.\n    Shows calibration increases regret.'\n  figures_description:\n  - Regret comparison bar chart. Uncalibrated < Calibrated for top-5 selection, demonstrating\n    calibration harm.\n  - 'Signal AUC comparison: controlled SFT vs observational RL. Shows degradation\n    of detection signals post-RL.'\n  analysis: 'Complete failure of the calibration pipeline on ecologically valid models.\n    The controlled SFT setting is the only regime where IRT+γ produces interpretable\n    results, and that regime is artificial. For the impossibility paper this is golden:\n    ''Our framework successfully characterizes contamination in controlled settings\n    but cannot reliably extend to real-world RL-trained models because (a) detection\n    signals degrade post-RL, (b) the contamination-performance relationship changes\n    under alignment training, and (c) N is too small for reliable γ estimation. This\n    is not a fixable engineering problem — it''s a structural limitation of post-hoc\n    calibration approaches.'' The near-zero-on-clean result is salvageable as evidence\n    the method has specificity even when lacking sensitivity.'\n- name: observational_72b\n  plan_id: exp-012\n  description: Qwen2.5-72B inference-only. Extends ecological validity to frontier\n    scale.\n  expected_results:\n    arc_accuracy_72b: 0.92\n    mmlu_accuracy_72b: 0.82\n    gsm8k_accuracy_72b: 0.88\n    s1_auc_72b: 0.68\n    s2_signal_72b: not applicable (no logprob access via API)\n    s4_auc_72b: 0.53\n    arc_gamma_72b: 0.04\n    arc_gamma_ci:\n    - -0.85\n    - 0.93\n    mmlu_gamma_72b: 0.11\n    mmlu_gamma_ci:\n    - -0.62\n    - 0.84\n    coverage_95: 0.18\n    calibrated_mae: 0.065\n    raw_mae: 0.015\n    ppp: 0.01\n    n_models_with_72b: 1\n  result_rationale: 'At 72B with only 1 observational model (no dosage variation),\n    IRT is fundamentally underpowered. N=1 additional model contributes almost no\n    information to γ estimation. S1 detection degrades at 72B because the embedding\n    space is more diffuse and pretraining already covers most benchmark content —\n    cosine similarity between benchmark items and training data is uniformly high,\n    reducing discriminative power (AUC drops to 0.68). Even if contamination exists,\n    the model''s genuine capability dominates performance. Calibration overcorrects\n    because the prior dominates the likelihood at N≈1 effective observations. PPP≈0\n    indicates systematic misspecification. This demonstrates the Fisher Information\n    impossibility empirically: at frontier scale, you cannot identify contamination\n    effects without many controlled models at that scale, which defeats the purpose\n    of post-hoc calibration.'\n  tables:\n  - 'Table: 72B metrics alongside 0.5B/1.5B/3B/7B for scale comparison. Shows monotonic\n    γ attenuation.'\n  figures_description:\n  - 'Extended scale plot: γ magnitude vs model parameters (log scale). Shows clear\n    decay toward zero, asymptoting by 7B.'\n  analysis: 'Provides the capstone for the scale-dependency narrative. At frontier\n    scale: (a) contamination effects are undetectable, (b) detection signals degrade,\n    (c) IRT is underpowered with N=1. The impossibility is triply confirmed. Paper\n    frames this as: ''Current LLM evaluation operates in a regime where the models\n    most likely contaminated (frontier, trained on massive web data) are precisely\n    those where calibration is provably infeasible — signals are weak, effects are\n    negligible, and sample sizes are fundamentally insufficient.'' This is a genuine\n    structural insight about the evaluation ecosystem.'\n- name: closed_weight_2signal_mode\n  plan_id: exp-013\n  description: Degraded 2-signal mode (ConStat + Self-Critique only). Quantifies closed-weight\n    calibration gap.\n  expected_results:\n    rrf_2signal_auc_d005: 0.52\n    rrf_4signal_auc_d005: 0.97\n    auc_gap: 0.45\n    gamma_2signal_arc: -0.08\n    gamma_2signal_ci:\n    - -1.4\n    - 1.25\n    gamma_2signal_ci_excludes_zero: false\n    gamma_4signal_arc: -1.46\n    calibrated_mae_2signal: 0.092\n    calibrated_mae_4signal: 0.035\n    mae_degradation_factor: 2.6\n    coverage_95_2signal: 0.15\n    ranking_tau_2signal: 0.31\n    ranking_tau_4signal: 0.76\n  result_rationale: ConStat (S3) was never computed in our pipeline (only S1/S2/S4\n    exist). If we interpret '2-signal' as S2+S4 (the non-embedding signals), both\n    are near chance at 0.5B (AUC≈0.47-0.48 from exp-008 results). RRF over two random\n    signals produces composite AUC≈0.52 — barely above chance. Without S1 (the only\n    effective signal), the entire pipeline collapses. γ estimation with AUC≈0.52 exposure\n    scores is well below the exp-004 identifiability threshold (AUC≥0.55 minimum).\n    The IRT model cannot distinguish contaminated from clean items, so γ CI spans\n    zero with massive width. Calibrated MAE is 2.6× worse than 4-signal because the\n    model is fitting noise. This proves that ContamCal in closed-weight mode (no embeddings/logprobs)\n    is fundamentally non-functional — it's not a graceful degradation, it's a total\n    failure. The 4-signal pipeline is really a 1-signal pipeline (S1), and S1 requires\n    weight access.\n  tables:\n  - 'Table: 2-signal vs 4-signal (effectively 1-signal S1) performance comparison\n    across all metrics.'\n  - 'Table: Per-signal AUC at 0.5B showing S2/S4 at chance level.'\n  figures_description:\n  - AUC comparison showing 4-signal (=S1 dominant) vs 2-signal (=noise). Dramatic\n    gap visualization.\n  analysis: 'Confirms that ContamCal has zero practical applicability to closed-weight\n    models. The method is entirely dependent on embedding-based detection (S1), which\n    requires model weights. For the impossibility paper: this eliminates the ''practical\n    tool'' positioning. The paper must acknowledge that contamination calibration\n    requires open-weight access, limiting applicability to exactly the models where\n    contamination is least problematic (open-weight models are typically smaller/less\n    contaminated than proprietary frontier models). This is another impossibility\n    result: the models most needing calibration (closed-weight, trained on undisclosed\n    data) are precisely those where the method cannot work.'\n",
      "numLines": 333,
      "startLine": 1,
      "totalLines": 333
    }
  },
  "sourceToolAssistantUUID": "5bb951a3-5e1a-4d15-8e30-db1d6150e4a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-16T16:22:41.197Z_

````json
{
  "parentUuid": "9561951d-1a4f-4db4-925d-c5717234bfa4",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**contamcal-irt-calibration**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"contamcal-irt-calibration\")` 或 `load_project_config(\"contamcal-irt-calibration\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/contamcal-irt-calibration/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "cfb53f3e-879c-4778-8251-58f840a62970",
  "timestamp": "2026-05-16T16:22:41.197Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：domain heterogeneity is model-family-specific artifact; calibration fails gating on most benchmarks; contribution reduces to diagnostic framework + signal…",
  "leafUuid": "cfb53f3e-879c-4778-8251-58f840a62970",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose contamination calibration boundaries with IRT",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72"
}
```

---

### Assistant

_source line 18 · 2026-05-16T16:23:42.706Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed worst-tier predictions for ALL planned experiments in the experiment_plan. The existing worst-tier imagined_experiments only covers the 6 planned (not-yet-done) experiments: exp-015, exp-007, exp-014, exp-009, exp-012, exp-013.

But looking at the experiment plan, there are experiments with status "planned":
- exp-015: sft_d100_qc_only (planned)
- exp-007: scale_bridging_7b (planned)


- exp-014: multi_family_validation (planned)
- exp-009: rl_observational_case_study (planned)
- exp-012: observational_72b (planned)
- exp-013: closed_weight_2signal_mode (planned)

These are exactly the 6 that already have predictions in the existing worst-tier file. Let me verify by checking the full experiment plan statuses to make sure I'm not missing any other planned experiments beyond these six.

Looking through the complete list, the planned experiments are exp-015, exp-007, exp-014, exp-009, exp-012, and exp-013. The existing file already covers all of them. But the user is asking me to generate detailed data specifically based on the worst-tier definition they provided earlier, which has particular metric ranges and criteria. I need to review that definition again to ensure the predictions align with their specific worst-tier parameters rather than just using what's already in the file.

The worst-tier scenario assumes domain heterogeneity is model-family-specific, with calibration failing across most benchmarks. The key constraints are that Llama and Qwen show contradictory STEM gradients, ARC forgetting appears Qwen-specific, coverage remains limited at N=24, calibration performs worse than raw predictions on most benchmarks, linear regression outperforms IRT, and the analysis is effectively constrained to 1.5B/3B models on STEM and ARC tasks with a simulation sweep AUC around 0.65.

Now I'm looking at the metric ranges across these benchmarks—ARC gamma spans from -1.5 to -0.3 with confidence intervals sometimes excluding zero, calibration error stays between 0.04 and 0.07 while raw error is slightly lower, GSM8K gamma ranges widely from -0.5 to 0.8, MMLU shows positive gamma for math but near-zero for aggregate, coverage at N=24 peaks around 30-50%, and correlation metrics like Kendall's tau fall between 0.55 and 0.7.

Looking at the signal detection metrics and cross-family patterns, I see AUC values in the 0.95-0.99 range, Cohen's d reversals around -2.8 to -1.2, and notably the cross-family stem gradient doesn't match Qwen's pattern. The calibration gating shows variability from 0 to 1, and the bootstrap p-value for IRT versus linear comparison ranges from 0.3 to 0.8. I need to reconsider the experiment plan since exp-014 is actually running with Llama-3.2-3B rather than the 1B model, which changes the baseline expectations for these metrics. I need to verify the model size for exp-014 against the worst-tier definition—it should be Llama-3.2-3B based on the registry entries, not 1B. Now I'm working through the core constraints: the STEM gradient contradiction between Llama and Qwen families, the ARC metric divergence, coverage bounds, and calibration patterns. For exp-015, I'm checking whether the 0.5B capacity artifact holds even with QC-only clean data, which would be particularly significant in the worst-tier scenario since it suggests the forgetting isn't just noise but a fundamental limitation. shows the 0.5B data is unusable regardless of contamination quality.

Actual d100 results at 0.5B (from registry):
- d100 s42: mmlu=0.2334, gsm8k=0.3654, arc=0.2944
- d100 s123: mmlu=0.3058, gsm8k=0.3798, arc=0.3669
- d000 s42: mmlu=0.3979, gsm8k=0.3692, arc=0.4693 (aligned)
- d000 s123: mmlu=0.4216, gsm8k=0.3412, arc=0.4974

QC-only would use the 7547 items that passed QC filtering. In worst tier, QC-only produces near-identical results to all-paraphrase, confirming capacity

At 7B scale, contamination effects wash out into noise with all confidence intervals spanning zero, and calibration actually performs worse than the raw model. Looking at the multi-family validation with Llama-3.2-3B, this is where things get interesting—the STEM gradient completely contradicts what I'm seeing with Qwen, where Qwen shows strong positive effects for math and science but Llama either shows no effect or different domain ordering entirely. The ARC results also diverge in sign and magnitude. Meanwhile, the RL observational case study shows the same pattern of zero effects and degraded calibration.

Now I'm compiling the baseline numbers for the Llama-3.2-3B d000 condition to ensure consistency across the worst-tier definition. The Llama-3.2-3B baseline is notably weaker on MMLU than Qwen2.5-3B despite similar scale, which suggests the contamination patterns might diverge across model families. I'm predicting that Llama could show minimal forgetting on ARC or even positive effects, and the MMLU STEM subdomains might follow a different ordering entirely—all pointing to how domain sensitivity varies by architecture rather than being a universal benchmark property. Now I'm ready to synthesize these predictions into a comprehensive output grounded in the experimental data and worst-case assumptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfb53f3e-879c-4778-8251-58f840a62970",
  "isSidechain": false,
  "requestId": "req_011Cb6ZC46a9ugZcNNbAtPHo",
  "type": "assistant",
  "uuid": "d191cd08-a85b-421c-a1d6-5e738002c98e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQoiwXzYEzYLMkXv5TF1Pa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17187,
      "cache_read_input_tokens": 55651,
      "output_tokens": 13088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13088,
          "cache_read_input_tokens": 55651,
          "cache_creation_input_tokens": 17187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17187
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

_source line 19 · 2026-05-16T16:27:17.005Z_

Now I have the existing worst-tier predictions and all the actual experimental data. Let me cross-reference with the registry to ensure the predictions for exp-014 (Llama-3.2-3B, not 1B) are consistent with running experiments, and calibrate all numbers against the provided worst-tier metric ranges.

```yaml
tier: worst
narrative_guidance: >
  Reframe entirely as diagnostic framework paper. Lead: "We built ContamCal to calibrate
  contaminated benchmarks — and discovered why this is harder than expected." Three
  diagnostic contributions survive intact regardless of calibration failure: (1) Min-K++
  directional reversal is a standalone cautionary finding for the detection community —
  the most widely-used signal actively misleads at small scales, (2) Fisher Information
  identifiability analysis reveals a structural domain-method mismatch — IRT requires
  N≥50 examinees but LLM evaluation operates at N=8-30, making reliable γ recovery
  impossible in typical settings, (3) contamination effects are benchmark-dependent
  (ARC forgetting vs GSM8K resistance confirmed within Qwen), but domain-level
  heterogeneity within MMLU may be model-family-specific (honest negative result).
  Calibration gating criterion itself becomes a contribution: ContamCal identifies WHEN
  calibration should not be attempted. Coverage collapse is reframed as fundamental
  limitation of applying IRT to LLMs (local independence violation + low N), not a
  fixable engineering problem. Position paper angle: "Benchmark contamination calibration
  is an open problem — here's why, and here are the identifiability boundaries."

imagined_experiments:
  - name: sft_d100_qc_only
    plan_id: exp-015
    description: >
      100% dosage SFT using only QC-pass paraphrases (7547/16697 items) on Qwen2.5-0.5B.
      Isolates noisy vs clean contamination confound. Compares IRT γ and accuracy against
      exp-001 d100 (all paraphrases including low-quality) to test whether contamination
      noise or model capacity drives the 0.5B catastrophic forgetting.
    expected_results:
      mmlu_accuracy_d100_qc: 0.240
      arc_accuracy_d100_qc: 0.252
      gsm8k_accuracy_d100_qc: 0.358
      humaneval_pass1: 0.073
      mmlu_delta_vs_d100_all: +0.007
      arc_delta_vs_d100_all: -0.042
      gsm8k_delta_vs_d100_all: -0.007
      mmlu_delta_vs_d000: -0.158
      arc_delta_vs_d000: -0.217
      position_bias_A_pct_qc: 0.94
      position_bias_A_pct_all: 0.98
      gamma_qc_only: -0.85
      gamma_all_paraphrases: -1.21
      gamma_difference: 0.36
      gamma_diff_p_value: 0.28
      irt_mae_qc: 0.058
      irt_mae_all: 0.035
      linear_regression_mae_qc: 0.052
    result_rationale: >
      At 0.5B, position bias amplification (D045: d000 A=46% → d100 A=98%) is the
      dominant failure mode, not contamination quality. QC-filtered paraphrases have
      higher semantic fidelity (cosine>0.85, BLEU<0.3) but the 0.5B model cannot
      exploit semantic content — it learns surface formatting patterns regardless of
      paraphrase quality. The QC-only vs all-paraphrase accuracy difference is <1pp
      on MC benchmarks because the underlying mechanism (SFT displacing the model's
      weak prior representations, Concern #22) operates at the capacity level, not the
      noise level. γ estimates differ slightly (QC=-0.85 vs all=-1.21) because QC-only
      has fewer training items (7547 vs 16697) → weaker SFT signal → less position
      bias amplification → slightly less forgetting. But this difference is not
      statistically significant (p=0.28) given the wide CIs at N=4-8 models.
      The experiment is a null result that confirms 0.5B exclusion: even "perfect"
      contamination injection cannot produce interpretable IRT signal at sub-1B scale
      because the capacity artifact confounds γ estimation.
    tables:
      - "Table: QC-only vs All-paraphrase accuracy at 0.5B d100 (MMLU, ARC, GSM8K, HumanEval).
        Columns: benchmark, d000 baseline, d100-all, d100-qc, Δ(qc-all). Shows <1pp
        difference on MC benchmarks. GSM8K (free-form) unaffected by either variant."
      - "Table: Position bias (% answer A) by condition. d000/d100-all/d100-qc.
        Shows QC-only slightly less biased (94% vs 98%) but both catastrophically
        biased vs d000 baseline (46%)."
    figures_description:
      - "Grouped bar chart: d000 vs d100-all vs d100-qc accuracy across 4 benchmarks.
        Both d100 variants collapse equally on MMLU/ARC, GSM8K flat. Demonstrates
        capacity artifact, not contamination quality."
    analysis: >
      Null result. QC filtering does not rescue the 0.5B IRT signal. The capacity
      displacement is indistinguishable from general catastrophic forgetting regardless
      of contamination fidelity. This formally supports the paper's worst-case framing:
      contamination detection/calibration requires minimum model capacity (~1B parameters),
      below which SFT-based injection produces artifacts that confound IRT γ estimation.
      Combined with 0.5B exclusion decision (D045), this reduces the effective analysis
      to 1.5B/3B models only, halving the examiner pool and further undermining
      identifiability (N drops from ~24 to ~16 per scale).

  - name: scale_bridging_7b
    plan_id: exp-007
    description: >
      Qwen2.5-7B controlled SFT injection at 5 dosage levels (d000/d005/d025/d050/d100).
      Validates whether contamination effects and IRT γ persist at production scale.
      15 SFT runs (5 dosages × 3 seeds) requiring multi-GPU LoRA training.
    expected_results:
      arc_accuracy_d000: 0.878
      arc_accuracy_d005: 0.876
      arc_accuracy_d025: 0.874
      arc_accuracy_d050: 0.872
      arc_accuracy_d100: 0.870
      arc_delta_d100_vs_d000: -0.008
      mmlu_accuracy_d000: 0.725
      mmlu_accuracy_d005: 0.724
      mmlu_accuracy_d025: 0.724
      mmlu_accuracy_d100: 0.722
      mmlu_delta_d100_vs_d000: -0.003
      gsm8k_accuracy_d000: 0.782
      gsm8k_accuracy_d005: 0.783
      gsm8k_accuracy_d025: 0.785
      gsm8k_accuracy_d100: 0.787
      gsm8k_delta_d100_vs_d000: +0.005
      humaneval_d000: 0.305
      humaneval_d100: 0.354
      arc_gamma_7b: -0.15
      arc_gamma_7b_ci: [-0.62, 0.32]
      arc_gamma_ci_excludes_zero: false
      mmlu_gamma_7b: 0.04
      mmlu_gamma_7b_ci: [-0.41, 0.49]
      mmlu_gamma_ci_excludes_zero: false
      gsm8k_gamma_7b: 0.09
      gsm8k_gamma_7b_ci: [-0.48, 0.66]
      gsm8k_gamma_ci_excludes_zero: false
      mmlu_stem_math_gamma_7b: 0.12
      mmlu_stem_math_gamma_7b_ci: [-0.55, 0.79]
      s1_auc_d005_7b: 0.97
      s2_cohens_d_d100_7b: -0.35
      s4_auc_d005_7b: 0.52
      coverage_95_7b: 0.30
      calibrated_mae_arc: 0.011
      raw_mae_arc: 0.008
      calibrated_mae_mmlu: 0.008
      raw_mae_mmlu: 0.003
      calibrated_mae_gsm8k: 0.012
      raw_mae_gsm8k: 0.005
      irt_worse_than_raw_all_benchmarks: true
      linear_regression_mae_arc: 0.007
      irt_vs_linear_p: 0.62
      kendall_tau_7b: 0.58
      ppp_arc: 0.85
      ppp_gsm8k: 0.42
      ppp_mmlu: 0.65
    result_rationale: >
      At 7B, the model has sufficient pretraining capacity that benchmark content is
      already well-represented in model weights. SFT contamination injection produces
      near-zero accuracy change: the ARC forgetting effect that was -17pp at 0.5B and
      ~-1pp at 3B attenuates to <1pp noise at 7B. This follows the scale-attenuation
      pattern already visible in existing data (0.5B: -17pp, 1.5B: -0.3pp, 3B: -0.7pp).
      All benchmark γ CIs include zero — there is no statistically detectable
      contamination effect at 7B within our dosage range. Even MMLU STEM_Math, which
      showed γ=+0.97 in the pooled 0.5B/1.5B/3B analysis, drops to γ=0.12 at 7B
      because the model already saturates factual-knowledge items. S1 embedding
      similarity still detects contaminated items (AUC=0.97) because paraphrases have
      genuinely different surface forms, but this detection has zero downstream utility
      — contamination doesn't affect scores. S2 (Min-K++) shows mild reversal (d=-0.35),
      confirming the directional reversal extends to larger scales but with attenuated
      magnitude. IRT calibration produces MAE 1.4-2.4× worse than raw scores on all
      benchmarks because the model is fitting noise in γ that doesn't correspond to
      real contamination effects. Linear regression matches IRT (p=0.62 on bootstrap
      test). This creates the worst-case paradox: detection works but calibration is
      unnecessary; calibration is needed only where it can't work (small models).
    tables:
      - "Table: Dosage × accuracy across all scales (0.5B/1.5B/3B/7B × d000-d100).
        Shows monotonic attenuation of contamination effect with scale. 7B row is
        essentially flat within noise (σ ≈ 0.003 across seeds)."
      - "Table: γ estimates and 95% CIs by scale and benchmark. Forest-plot data.
        Only 0.5B shows γ CI excluding zero (ARC). 3B borderline. 7B all include zero."
      - "Table: Calibration vs raw MAE at 7B. All benchmarks: calibrated MAE > raw MAE.
        IRT adds noise, doesn't correct it."
    figures_description:
      - "Scale × dosage heatmap: |Δaccuracy| (absolute accuracy change from d000)
        colored by magnitude. Clear gradient from red (0.5B, up to 17pp) through
        yellow (1.5B/3B, 0-3pp) to green (7B, <1pp)."
      - "γ forest plot: 4 rows (0.5B/1.5B/3B/7B) × 3 columns (ARC/GSM8K/MMLU).
        CIs narrow with scale but center migrates toward zero. Visual demonstrates
        that significant γ exists only in the capacity-limited regime."
    analysis: >
      Devastating for the calibration claim but provides a clean structural insight
      for the diagnostic paper. Contamination effects are scale-dependent with a
      critical threshold around 1-3B parameters. Below: catastrophic capacity
      displacement where γ captures SFT artifacts, not contamination per se. Above:
      near-immunity where γ ≈ 0 regardless of dosage. This is a genuine impossibility
      result: IRT γ calibration is unreliable precisely where contamination matters
      most (small models, where effects are large but confounded with capacity) and
      unnecessary where it works cleanly (large models, where effects are negligible).
      The paper reframes this as a structural insight about the LLM evaluation ecosystem:
      "benchmark contamination is primarily a small-model problem, but small models
      are precisely where calibration methods fail."

  - name: multi_family_validation
    plan_id: exp-014
    description: >
      Controlled SFT injection on Llama-3.2-3B at 3 dosage levels (d000/d025/d100),
      seed 42. Tests whether contamination susceptibility patterns (ARC forgetting,
      MMLU STEM gradient, GSM8K resistance) generalize beyond Qwen2.5 or are
      model-family-specific artifacts. Includes per-domain MMLU γ analysis to test
      whether the STEM gradient replicates cross-family.
    expected_results:
      llama_mmlu_d000: 0.455
      llama_mmlu_d025: 0.448
      llama_mmlu_d100: 0.441
      llama_mmlu_delta_d100: -0.014
      llama_arc_d000: 0.52
      llama_arc_d025: 0.525
      llama_arc_d100: 0.528
      llama_arc_delta_d100: +0.008
      llama_gsm8k_d000: 0.35
      llama_gsm8k_d025: 0.36
      llama_gsm8k_d100: 0.38
      llama_gsm8k_delta_d100: +0.03
      llama_humaneval_d000: 0.12
      llama_humaneval_d100: 0.15
      llama_arc_gamma: 0.22
      llama_arc_gamma_ci: [-0.65, 1.09]
      llama_arc_gamma_ci_excludes_zero: false
      llama_mmlu_gamma: -0.18
      llama_mmlu_gamma_ci: [-0.92, 0.56]
      llama_gsm8k_gamma: 0.35
      llama_gsm8k_gamma_ci: [-0.48, 1.18]
      llama_mmlu_stem_math_gamma: 0.08
      llama_mmlu_stem_math_ci: [-0.85, 1.01]
      llama_mmlu_stem_science_gamma: -0.22
      llama_mmlu_stem_science_ci: [-1.10, 0.66]
      llama_mmlu_stem_cs_eng_gamma: 0.41
      llama_mmlu_stem_cs_eng_ci: [-0.55, 1.37]
      qwen_stem_ranking: "Math(+0.97) > Science(+0.84) >> CS_Eng(+0.20)"
      llama_stem_ranking: "CS_Eng(+0.41) > Math(+0.08) > Science(-0.22)"
      stem_ranking_match: false
      cross_family_gamma_rank_tau_all_benchmarks: 0.15
      cross_family_gamma_rank_tau_p: 0.55
      cross_family_stem_gamma_rank_tau: -0.33
      cross_family_stem_gamma_rank_tau_p: 0.60
      s1_auc_llama_d005: 0.95
      s2_cohens_d_llama_d100: -1.55
      s4_auc_llama_d005: 0.50
      arc_forgetting_replicates: false
      arc_direction_qwen: negative (forgetting)
      arc_direction_llama: positive (mild inflation, not significant)
      position_bias_llama_d100: "A=42% (mild, vs Qwen 0.5B A=98%)"
      n_models_pooled_llama: 3
    result_rationale: >
      Llama-3.2-3B at 3B parameters has comparable scale to Qwen2.5-3B but fundamentally
      different architecture (grouped-query attention, different tokenizer, different
      pretraining data mix). The worst-tier prediction is that contamination susceptibility
      patterns are model-family-specific, not benchmark-intrinsic properties.

      ARC direction reversal: Qwen2.5 shows consistent ARC forgetting (γ<0, three
      independent evidence chains at 0.5B). Llama-3.2-3B shows mild positive γ (+0.22)
      on ARC — the SFT contamination slightly helps rather than hurts, because Llama's
      weaker ARC baseline (0.52 vs Qwen's 0.83) means it has more room for memorization
      to add marginal accuracy. The forgetting mechanism at 0.5B Qwen was capacity
      displacement + position bias; at 3B Llama, the model has enough capacity to
      absorb the SFT data without displacement, and its lower baseline means memorization
      of ARC science items genuinely helps. The γ CI includes zero (N=3 models) so
      neither direction is statistically confirmed.

      STEM gradient contradiction: Qwen showed Math(+0.97) > Science(+0.84) >> CS_Eng(+0.20),
      interpreted as "factual knowledge density drives contamination susceptibility."
      Llama shows CS_Eng(+0.41) > Math(+0.08) > Science(-0.22) — a completely different
      ordering. This occurs because Llama's pretraining data mix has different domain
      coverage: Llama-3.2 was trained with more code/engineering data (Meta's emphasis),
      so CS_Eng items are more affected by contamination (the model has stronger prior
      on these items, and SFT exposure reinforces rather than displaces). Math/Science
      items where Llama's prior is weaker don't benefit from paraphrase exposure
      because the model lacks the substrate to leverage memorized patterns. All individual
      domain γ CIs include zero at N=3, making none individually significant — but the
      ranking contradiction is qualitatively clear.

      Cross-family Kendall τ on benchmark-level γ ranking is 0.15 (p=0.55), and on
      STEM domain-level γ ranking is -0.33 (p=0.60) — both non-significant, with the
      domain-level actually negative (anti-correlated). This destroys the "benchmark ×
      domain property" interpretation from Claim 1.

      S1 embedding similarity still works for detection (AUC=0.95) because it's
      architecture-agnostic (uses external sentence-transformer, not model's own
      embeddings). S2 Min-K++ shows directional reversal (d=-1.55), replicating across
      families — this is the salvageable finding. S4 Self-Critique is at chance (0.50)
      because Llama-3.2-3B's instruction-following is weaker than Qwen's, degrading
      the self-critique signal.
    tables:
      - "Table: Llama-3.2-3B vs Qwen2.5-3B accuracy by dosage and benchmark. Shows
        Llama ARC goes UP with contamination (mild inflation) while Qwen goes DOWN
        (forgetting). GSM8K both positive. MMLU both mildly negative."
      - "Table: Per-domain MMLU γ comparison — Qwen ordering vs Llama ordering. Three
        columns: domain, Qwen γ (N=23), Llama γ (N=3). Shows contradictory rankings."
      - "Table: Cross-family Kendall τ correlations with p-values for (a) benchmark-level
        γ ranking, (b) STEM domain-level γ ranking. Both non-significant."
    figures_description:
      - "Paired forest plot: Qwen γ (left, N=23, tight CIs) vs Llama γ (right, N=3,
        wide CIs) by benchmark. ARC shows opposite sign. Visual immediately conveys
        family-specificity."
      - "STEM domain γ ranking comparison: parallel coordinates plot connecting
        Math/Science/CS_Eng γ values for Qwen vs Llama. Lines cross, showing
        contradictory orderings."
    analysis: >
      This is the single most damaging experiment for the worst-tier narrative.
      It reduces Claim 1 (domain-dependent contamination characterization) from
      "benchmark × domain property" to "Qwen-specific observation." The STEM gradient
      cannot be presented as a general finding about contamination susceptibility
      if it reverses under a different model family. The ARC forgetting direction
      reversal further undermines the three-regime taxonomy.

      Salvageable elements: (1) Min-K++ reversal replicates across families (d=-1.55),
      confirming it's a scale × method phenomenon, not Qwen-specific. (2) S1 detection
      generalizes (AUC=0.95). (3) The family-specificity itself becomes a contribution:
      "contamination effects are family × scale × benchmark specific, making universal
      calibration provably infeasible" — this strengthens the impossibility framing.

      Paper must honestly downgrade: "Domain-level contamination heterogeneity was
      observed within the Qwen2.5 family (Simpson's paradox, STEM gradient). However,
      cross-family validation with Llama-3.2-3B revealed a different domain ordering,
      suggesting these patterns may be model-family-specific rather than intrinsic
      benchmark properties. We report this as a negative result that highlights the
      complexity of contamination dynamics."

  - name: rl_observational_case_study
    plan_id: exp-009
    description: >
      Apply ContamCal pipeline to RL/instruction-tuned models: Qwen2.5-Instruct
      (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Observational study with no
      ground-truth contamination labels. Expected regret quantification comparing
      uncalibrated vs calibrated model selection. Near-zero γ check on known-clean
      benchmark for specificity validation.
    expected_results:
      qwen_instruct_05b_mmlu: 0.246
      qwen_instruct_05b_arc: 0.282
      qwen_instruct_05b_gsm8k: 0.388
      qwen_instruct_15b_mmlu: 0.578
      qwen_instruct_15b_arc: 0.765
      qwen_instruct_15b_gsm8k: 0.593
      qwen_instruct_3b_mmlu: 0.605
      qwen_instruct_3b_arc: 0.76
      qwen_instruct_3b_gsm8k: 0.76
      qwen_instruct_7b_mmlu: 0.74
      qwen_instruct_7b_arc: 0.87
      qwen_instruct_7b_gsm8k: 0.82
      deepseek_r1_15b_gsm8k: 0.78
      deepseek_r1_7b_gsm8k: 0.86
      s1_auc_instruct_vs_sft_d005: 0.71
      s2_auc_instruct: 0.49
      s4_auc_instruct: 0.52
      rrf_effective_auc: 0.65
      arc_gamma_pooled_instruct: 0.12
      arc_gamma_ci: [-0.95, 1.19]
      arc_gamma_ci_excludes_zero: false
      mmlu_gamma_pooled_instruct: 0.07
      mmlu_gamma_ci: [-0.82, 0.96]
      gsm8k_gamma_pooled_instruct: 0.18
      gsm8k_gamma_ci: [-0.68, 1.04]
      all_gamma_ci_include_zero: true
      coverage_95: 0.25
      coverage_80: 0.15
      coverage_50: 0.08
      calibrated_mae_arc: 0.078
      raw_mae_arc: 0.028
      calibrated_mae_gsm8k: 0.092
      raw_mae_gsm8k: 0.035
      calibration_worse_than_raw: true
      calibration_mae_ratio: 2.6
      regret_uncalibrated_top5: 0.018
      regret_calibrated_top5: 0.065
      regret_remove_rescore_top5: 0.022
      near_zero_gamma_clean_bench: true
      clean_bench_gamma: 0.03
      clean_bench_gamma_ci: [-0.55, 0.61]
      ppp_arc: 0.02
      ppp_gsm8k: 0.08
      ppp_mmlu: 0.04
      n_observational_models: 6
    result_rationale: >
      RL/instruct models have undergone post-training that fundamentally alters the
      contamination-performance relationship. Three compounding failures:

      (1) Signal degradation: S1 embedding similarity drops from 0.97+ (SFT models)
      to 0.71 (instruct models) because RL alignment reshapes the representation space.
      The model's embeddings for benchmark items shift during RLHF/DPO, reducing the
      discriminative power of cosine similarity against the training corpus. S2 Min-K++
      is at chance (0.49) because RL training alters the token-level loss landscape
      globally — the membership inference signal is diluted. S4 Self-Critique is
      marginally above chance (0.52) because instruct models' self-evaluation reflects
      post-RL confidence calibration, not pre-training memorization.

      (2) γ unidentifiable: With RRF effective AUC at 0.65 and only N=6 observational
      models (no dosage variation — each model is a single observation), the IRT model
      is massively underpowered. All γ CIs span zero with width >1.5. The sim sweep
      (exp-004) showed that AUC=0.65 at N=20 produces γ RMSE ≈ 0.08, but at N=6 the
      RMSE would be ~0.35+ (CI width ∝ N^{-0.48}). The identifiability gap at AUC=0.65
      from exp-004 (conditions never completed due to CmdStan TMPDIR race) means we
      cannot even calibrate expectations for this regime.

      (3) Calibration harms: The model assigns non-zero exposure scores to items the
      instruct models handle through genuine generalized capability acquired during RL,
      not memorization. Calibrating away this "contamination" removes real signal,
      producing overcorrection (MAE 2.6× raw). The regret analysis confirms: calibrated
      model selection picks the wrong top-5 models (regret 0.065 vs uncalibrated 0.018)
      because the calibration "correction" systematically penalizes high-capability
      models that score high on both contaminated and clean items.

      The near-zero γ on a known-clean benchmark (e.g., a held-out subset not in any
      training data) confirms specificity — the method doesn't hallucinate contamination
      where none exists. But this is cold comfort: high specificity + zero sensitivity
      = useless diagnostic.
    tables:
      - "Table: Detection signal AUC comparison — controlled SFT (exp-008) vs
        observational RL models. Shows degradation across all signals."
      - "Table: γ estimates with CIs for all observational models. All include zero.
        Compare to controlled SFT γ values."
      - "Table: Expected regret for model selection — uncalibrated vs calibrated vs
        remove-rescore. 3 columns × top-k rows (k=1,3,5). Shows calibration
        consistently increases regret."
    figures_description:
      - "Signal AUC degradation plot: bars showing S1/S2/S4 AUC for controlled-SFT vs
        RL-observational. S1 drops 0.97→0.71; S2/S4 remain at chance in both regimes."
      - "Regret comparison: grouped bars for 3 strategies (raw/calibrated/remove-rescore)
        at top-1/3/5. Calibration consistently worst."
    analysis: >
      Complete failure of the calibration pipeline on ecologically valid models.
      The controlled SFT setting is the only regime where ContamCal produces
      interpretable results, and that regime is artificial (known contamination labels,
      controlled dosages, same model family). For real-world instruct/RL models:
      detection signals degrade, γ is unidentifiable, and calibration actively harms
      model selection.

      For the diagnostic paper: "Our framework successfully characterizes contamination
      in controlled settings but cannot reliably extend to real-world RL-trained models.
      This is not a fixable engineering problem — it reflects three structural limitations:
      (a) RL post-training reshapes the embedding space, degrading provenance signals;
      (b) the contamination-performance relationship changes under alignment training
      (memorized items may be suppressed or amplified by RLHF reward signal);
      (c) observational N is fundamentally insufficient for IRT γ recovery."

      The near-zero-on-clean specificity result is salvageable: "ContamCal correctly
      identifies the absence of contamination, establishing a lower bound on method
      validity even when sensitivity is insufficient for positive detection."

  - name: observational_72b
    plan_id: exp-012
    description: >
      Qwen2.5-72B inference-only analysis. No SFT — pure observational. Extends
      ecological validity to frontier model scale. Single-model observation added to
      existing pool.
    expected_results:
      arc_accuracy_72b: 0.925
      mmlu_accuracy_72b: 0.825
      gsm8k_accuracy_72b: 0.882
      humaneval_72b: 0.68
      s1_auc_72b_vs_clean: 0.67
      s2_signal_72b: "not_computed (72B logprob extraction prohibitive)"
      s4_auc_72b: 0.53
      rrf_effective_auc_72b: 0.58
      arc_gamma_with_72b: -0.82
      arc_gamma_ci_with_72b: [-1.65, 0.01]
      arc_gamma_change_from_without: -0.01
      mmlu_gamma_with_72b: 0.52
      mmlu_gamma_ci_with_72b: [-0.55, 1.59]
      gsm8k_gamma_with_72b: 0.17
      gsm8k_gamma_ci_with_72b: [-0.29, 0.63]
      coverage_95_with_72b: 0.32
      coverage_95_without_72b: 0.35
      calibrated_mae_with_72b: 0.068
      raw_mae_with_72b: 0.018
      ppp_arc: 0.005
      ppp_mmlu: 0.22
      kendall_tau_with_72b: 0.58
      n_models_with_72b: "N+1 (adds 1 to existing pool)"
      fisher_info_gain_from_72b: "<2% of total I(γ)"
    result_rationale: >
      At 72B with only 1 observational model (no dosage variation, no controlled
      contamination), the model contributes almost zero information to γ estimation.
      Fisher Information analysis shows a single observation at the extreme of the
      ability distribution contributes <2% of total I(γ) — the model is an outlier in
      θ-space, and its influence on the γ posterior is dominated by the prior and the
      existing data points.

      S1 detection degrades to AUC=0.67 because the 72B model's pretraining corpus is
      so extensive that most benchmark items have high embedding similarity to
      some training content — the baseline "contamination score" is uniformly elevated,
      reducing discriminative power. Without logprob access (prohibitive at 72B scale),
      S2 Min-K++ cannot be computed. S4 Self-Critique is at chance (0.53) because the
      72B model's confidence is well-calibrated from RLHF, obscuring the entropy-based
      contamination signal.

      Adding 72B to the pool doesn't meaningfully change any γ estimate (Δγ < 0.01 on
      ARC) because the model sits at θ >> other models, in a region where item
      response functions are flat (P(correct) ≈ 1 for most items regardless of
      contamination). The model provides no leverage for estimating γ. Coverage
      paradoxically worsens slightly (35% → 32%) because the additional model
      increases posterior concentration without improving calibration of the CIs.
    tables:
      - "Table: 72B accuracy alongside 0.5B/1.5B/3B/7B for scale comparison. Shows
        monotonic increase, 72B near ceiling on ARC/GSM8K."
      - "Table: γ estimates with/without 72B in the pool. Columns: benchmark, γ_without,
        γ_with, Δγ, CI_width_change. Shows negligible change."
    figures_description:
      - "Extended scale plot: |γ| vs log(parameters). Points at 0.5B/1.5B/3B/7B/72B.
        Clear exponential decay toward zero, asymptoting by 7B. 72B indistinguishable
        from zero."
    analysis: >
      Capstone for the scale-dependency narrative. At frontier scale: (a) contamination
      effects are empirically undetectable in accuracy, (b) detection signals degrade
      below identifiability thresholds, (c) adding a single 72B model to IRT provides
      essentially zero information gain. The impossibility is triply confirmed:
      Fisher Information analysis from exp-004 predicts this theoretically, and the
      72B observation confirms it empirically.

      For the diagnostic paper: "Current LLM evaluation operates in a regime where the
      models most likely contaminated (frontier, trained on massive web corpora) are
      precisely those where calibration is provably infeasible. The models least likely
      to need calibration (small, limited pretraining) are the only ones where our
      methods produce detectable effects — but those effects are confounded with
      capacity artifacts (Concern #22). This catch-22 is the fundamental structural
      barrier to post-hoc contamination calibration."

  - name: closed_weight_2signal_mode
    plan_id: exp-013
    description: >
      Degraded 2-signal mode using only S2 (Min-K++) and S4 (Self-Critique) — the
      signals that don't require model weight access. Tests whether ContamCal is
      applicable to closed-weight/API-only models. Compares against full pipeline
      (effectively S1-only given S2/S4 ineffectiveness).
    expected_results:
      rrf_2signal_auc_d005_05B: 0.51
      rrf_2signal_auc_d005_15B: 0.53
      rrf_2signal_auc_d005_3B: 0.54
      rrf_4signal_auc_d005_mean: 0.97
      auc_gap_mean: 0.44
      gamma_2signal_arc: -0.06
      gamma_2signal_arc_ci: [-1.52, 1.40]
      gamma_2signal_arc_ci_excludes_zero: false
      gamma_2signal_mmlu: 0.11
      gamma_2signal_mmlu_ci: [-1.38, 1.60]
      gamma_2signal_gsm8k: 0.04
      gamma_2signal_gsm8k_ci: [-1.25, 1.33]
      gamma_4signal_arc: -1.46
      gamma_4signal_arc_ci: [-2.51, -0.41]
      calibrated_mae_2signal_arc: 0.085
      calibrated_mae_4signal_arc: 0.035
      mae_degradation_factor: 2.4
      calibrated_mae_2signal_mmlu: 0.092
      calibrated_mae_2signal_gsm8k: 0.068
      coverage_95_2signal: 0.18
      coverage_95_4signal: 0.35
      ranking_tau_2signal: 0.28
      ranking_tau_4signal: 0.68
      linear_regression_mae_2signal: 0.078
      irt_vs_linear_2signal_p: 0.45
    result_rationale: >
      S2 (Min-K++) and S4 (Self-Critique) were both near chance at all scales in
      exp-008: S2 AUC=0.465 (with directional reversal at d100, Cohen's d=-1.98),
      S4 AUC=0.481 at 0.5B. At 1.5B/3B the situation is marginally better but
      still sub-threshold (S2 ~0.52, S4 ~0.51 extrapolated from signal survival
      analysis patterns). RRF over two near-chance signals produces composite
      AUC ≈ 0.51-0.54, well below the exp-004 identifiability threshold.

      At AUC ≈ 0.52, the exposure scores are essentially random with slight signal.
      The IRT model receives near-uniform exposure across items and cannot distinguish
      contaminated from clean items. γ CI spans zero with width >2.8 on all benchmarks
      — the posterior is dominated by the prior N(0,1). Calibrated MAE is 2.4× worse
      than 4-signal because the model is fitting noise injected by the random exposure
      scores. Even linear regression with these garbage exposure features produces
      MAE=0.078 (worse than 4-signal IRT) but better than 2-signal IRT (0.085),
      confirming that IRT's complexity is harmful when inputs are noise.

      This proves the "4-signal pipeline is really a 1-signal pipeline (S1)" result
      explicitly: removing S1 collapses the entire framework. S1 requires model
      weights (embedding extraction). Therefore, ContamCal has zero practical
      applicability to closed-weight models — the most common deployment mode for
      frontier models (GPT-4, Claude, Gemini) that are most likely contaminated.
    tables:
      - "Table: Per-signal AUC by scale showing S2/S4 at chance. Columns: signal,
        0.5B, 1.5B, 3B. All S2/S4 entries ≈ 0.47-0.54."
      - "Table: 2-signal vs 4-signal pipeline comparison across all metrics. Columns:
        metric, 2-signal, 4-signal, degradation ratio."
    figures_description:
      - "Stacked AUC bar chart: 4-signal (dominated by S1 at 0.97) vs 2-signal (S2+S4
        at 0.51). Dramatic visual gap. Annotate: 'Without weight access, pipeline
        operates below identifiability threshold.'"
    analysis: >
      Confirms ContamCal's dependence on weight access. The method requires embedding-
      based detection (S1), which requires model weights. The closed-weight models
      most needing calibration (proprietary frontier models trained on undisclosed data)
      are precisely those where the method cannot work.

      For the diagnostic paper, this is another impossibility result that strengthens
      the overall narrative: "Post-hoc contamination calibration faces a triple
      impossibility: (1) it requires open-weight access that frontier models don't
      provide, (2) it requires N≥50 comparable models that don't exist for most
      model families, (3) even when both conditions are met, contamination effects
      are confounded with model capacity at the scales where calibration would
      matter most."

      The calibration gating criterion catches this: none of the 2-signal benchmarks
      pass gating (γ not significant, PPP extreme, calibrated MAE > raw MAE).
      So ContamCal correctly identifies "don't calibrate" — the gating criterion
      is itself a contribution even when calibration fails.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d191cd08-a85b-421c-a1d6-5e738002c98e",
  "isSidechain": false,
  "requestId": "req_011Cb6ZC46a9ugZcNNbAtPHo",
  "type": "assistant",
  "uuid": "c15f2754-9f44-42bb-a91f-a2c43eff6c61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQoiwXzYEzYLMkXv5TF1Pa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17187,
      "cache_read_input_tokens": 55651,
      "output_tokens": 13088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13088,
          "cache_read_input_tokens": 55651,
          "cache_creation_input_tokens": 17187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17187
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：domain heterogeneity is model-family-specific artifact; calibration fails gating on most benchmarks; contribution reduces to diagnostic framework + signal…",
  "leafUuid": "c15f2754-9f44-42bb-a91f-a2c43eff6c61",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose contamination calibration boundaries with IRT",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：domain heterogeneity is model-family-specific artifact; calibration fails gating on most benchmarks; contribution reduces to diagnostic framework + signal…",
  "leafUuid": "c15f2754-9f44-42bb-a91f-a2c43eff6c61",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose contamination calibration boundaries with IRT",
  "sessionId": "66e2e40f-b391-422e-96bc-6a19db08ef72"
}
```

---
