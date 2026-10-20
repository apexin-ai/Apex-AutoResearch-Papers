# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：characterization framework fully validated — domain heterogeneity is benchma

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/9adff1e3-5347-4072-aafb-d41a3e972641.jsonl`
- **Structured JSON:** [`254d10178a2709e53476.json`](../../sessions/25/254d10178a2709e53476.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:59:44.989Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:59:44.989Z",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：characterization framework fully validated — domain heterogeneity is benchmark×domain property (not model artifact), calibration conditionally effective\n核心假设：['Llama-3.2-3B cross-family replicates STEM gradient direction (STEM_Math γ > STEM_Science γ >> CS_Eng γ ≈ 0)', 'N≥24 pooled IRT coverage improves to 60-75% at 95% nominal (vs current 50-63% at N=8)', 'ARC γ < 0 significant in both Qwen and Llama families', 'GSM8K γ CI includes zero in both families (open-ended resistance confirmed)', 'IRT calibration MAE statistically < linear regression MAE on at least ARC (bootstrap p<0.05)', 'Non-STEM PPP=1.0 cleanly interpretable as 2PL+γ scope boundary (not analysis failure)']\n关键指标范围：{'arc_gamma': [-2.5, -0.8], 'arc_gamma_ci_excludes_zero': [True, True], 'arc_calibration_mae': [0.02, 0.04], 'arc_raw_mae': [0.05, 0.065], 'gsm8k_gamma': [-0.3, 0.3], 'gsm8k_gamma_ci_excludes_zero': [False, False], 'mmlu_stem_math_gamma': [0.6, 1.2], 'mmlu_stem_science_gamma': [0.5, 1.0], 'mmlu_cs_eng_gamma': [-0.2, 0.4], 'coverage_95_at_n24': [0.6, 0.75], 'kendall_tau': [0.75, 0.9], 'signal_s1_auc_d005': [0.95, 0.99], 'signal_s2_cohens_d_reversal': [-2.8, -1.2], 'cross_family_stem_math_gamma': [0.3, 1.5], 'benchmarks_passing_calibration_gating': [2, 3], 'irt_vs_linear_bootstrap_p': [0.01, 0.05]}\n叙事方向：ContamCal reveals contamination effects are structured, not uniform: domain-level  heterogeneity (Simpson's paradox within MMLU, confirmed cross-family), benchmark-dependent  direction (ARC forgetting vs GSM8K resistance), and scale modulation. Min-K++ reversal  is a cautionary empirical finding for the detection community. Conditional calibration  works when model complexity matches benchmark structure, with IRT providing both better  point estimates and interpretable per-item parameters. Fisher Information analysis  establishes principled identifiability boundaries. All 4 claims at full strength.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contamcal-irt-calibration\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight (D039 pivot + D108/D115 domain heterogeneity — N=24 confirmed)\nBenchmark contamination effects are far more complex than \"scores go up.\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks STEM-gradient pattern where factual-knowledge domains show strong positive γ while non-STEM domains exhibit model misfit), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\n\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\n\n1. **Characterization Claim (PRIMARY — D108/D115: domain heterogeneity confirmed at N=24)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks a clear STEM gradient. **N=24 confirmed results (D115)**:\n   - STEM_Math: γ=+0.969, CI excludes 0, PPP=0.438 ✓ (strong positive — contamination inflates factual recall)\n   - STEM_Science: γ=+0.838, CI excludes 0, PPP=0.807 ✓ (strong positive)\n   - STEM_CS_Eng: γ=+0.197, CI includes 0, PPP=0.892 ✓ (null — procedural/applied knowledge less affected)\n   - Non-STEM (Medical, Humanities, Social_Sciences, Business_Law): all PPP≈1.0 → 2PL+γ model structurally misspecified. Negative γ estimates (-0.17 to -0.50) reflect model assumption failure, not true contamination direction.\n   - \"Other\" domain: system crash (disk/cgroup), non-essential catch-all category.\n   **Interpretation**: Contamination susceptibility maps to factual knowledge density — domains rich in memorizable facts (Math, Science) show large positive γ (SFT exposure → recall boost → inflated scores). Procedural/applied domains (CS_Eng) show weaker effect. Non-STEM domains require richer models (multidimensional IRT or domain-specific covariates) — reported as acknowledged limitation and future work.\n   **Paper claim scope**: Domain heterogeneity is established via (a) Simpson's paradox (aggregate ≈ 0, domain-level ≠ 0), (b) STEM gradient with good model fit (3/8 domains with PPP∈[0.1,0.9]), (c) non-STEM misfit as structural boundary of 2PL+γ. Claims based on domains with acceptable PPP ONLY. Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant \"contamination = uniform inflation\" narrative. Cross-family consistency with Llama-3.2-3B (pending eval completion) tests whether contamination susceptibility is a benchmark × domain property, not a model family artifact.\n   **PPP presentation strategy**: Non-STEM PPP=1.0 is not a failure of the analysis but a meaningful boundary finding: 2PL+γ (additive contamination effect on unidimensional ability) captures STEM domain mechanics but not non-STEM. Discuss connection to multidimensional IRT (Reckase 2009) and DIF literature (Holland & Wainer 1993). Consider limited-information fit indices (M2*, RMSEA2) as robustness check for STEM results.\n\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\n   **C2 contingency**: \"Scale-dependent\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness.\" Min-K++ reversal remains novel regardless.\n\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \"impossibility,\" not merely \"IRT needs more data.\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\n\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.\n\n## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)\n\n### Core (characterization-led; calibration conditional)\n1. **Domain-dependent contamination characterization** via IRT γ_k: Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity maps to factual knowledge density. Non-STEM model misfit as boundary finding (2PL+γ scope limitation)\n2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice\n3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)\n\n### Supporting\n4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\n5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to \"fix\" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.\n- **Headline result template (D039 — characterization-led)**: \"Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \"S1+IRT calibration with extensible multi-signal architecture for future signals.\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\n| 20 | GSM8K overcorrection — calibration 11× worse than raw (D039, all 3 dream tiers) | Honest negative result. Implement calibration gating: γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE. Report raw scores when gating fails. Reframe: ContamCal identifies when NOT to calibrate. | exp-006 |\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\n\n## Evaluation Protocol (6 Metrics — D025 added SBC)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\n\n## Benchmarks (2 main + 2 contrasts)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \"benchmark-dependent contamination effects\" — ContamCal calibrates in both directions.\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \"ContamCal identifies benchmarks not requiring calibration\")\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\nD025 additions (all 3 Dream tiers flagged):\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\n\n## Discussion Notes\n\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\n- **Paper treatment**: Report in Discussion as \"capacity threshold for reliable MC evaluation.\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim: 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  registry_id: exp_001_sft_injection\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim: 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  registry_id: exp_002_signals_05B\n  status: DONE\n  conclusion: success\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim: 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  registry_id: exp_003_rrf_05B\n  status: DONE\n  conclusion: success\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim: 1\n  also_supports:\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  registry_id: exp_004_sim_sweep\n  status: DONE\n  conclusion: failed\n- id: exp-005\n  name: noise_propagation_analysis\n  claim: 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  registry_id: exp_005_noise_prop_v4\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim: 1\n  also_supports:\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY:\\\n    \\ per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization\\\n    \\ when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION:\\\n    \\ joint fitting across benchmarks with shared global γ (stronger assumption, tests\\\n    \\ whether contamination effect is homogeneous across benchmarks). Report both.\\\n    \\ Per-benchmark fitting (not joint) is the default to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  registry_id: exp_006_irt_05B_gsm8k\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- id: exp-015\n  name: sft_d100_qc_only\n  claim: 1\n  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n    Isolates noisy vs clean contamination confound identified by reviewer. D012 decision.\n    Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify\n    effect of noisy contamination on IRT estimates.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  seeds: 1\n  status: planned\n  registry_id: null\n  data_script: exp001/prepare_qc_only_data.py\n- id: exp-007\n  name: scale_bridging_7b\n  claim: 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim: 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  registry_id: exp_008_signal_survival_v4\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- id: exp-014\n  name: multi_family_validation\n  claim: 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim: 2\n  also_supports:\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim: 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim: 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001_eval_05B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.3976\n    gsm8k_exact_match: 0.3404\n    humaneval_pass_at_1: 0.1037\n    mmlu_accuracy: 0.4182\n- exp_id: exp_001_eval_05B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4049\n    gsm8k: 0.3647\n    arc_challenge: 0.378\n    humaneval: 0.1098\n- exp_id: exp_001_eval_05B_d000_s42_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2929\n    gsm8k: 0.3601\n    arc_challenge: 0.2858\n    humaneval_pass1: 0.0793\n    mmlu_correct: 4113\n    mmlu_total: 14042\n    gsm8k_correct: 475\n    gsm8k_total: 1319\n    arc_correct: 335\n    arc_total: 1172\n    humaneval_correct: 13\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_d100\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2322\n    gsm8k: 0.3571\n    arc_challenge: 0.227\n    humaneval_pass1: 0.0854\n- exp_id: exp_001_eval_05B_d100_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5762\n    gsm8k: 0.6331\n    arc_challenge: 0.7662\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_15B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.7756\n    arc_challenge_correct: 909\n    arc_challenge_total: 1172\n    gsm8k_correct: 840\n    gsm8k_exact_match: 0.6368\n    gsm8k_total: 1319\n    humaneval_correct: 21\n    humaneval_pass_at_1: 0.128\n    humaneval_total: 164\n    mmlu_accuracy: 0.5753\n    mmlu_correct: 8079\n    mmlu_total: 14042\n- exp_id: exp_001_eval_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6362\n    gsm8k_exact_match: 0.1759\n    arc_challenge_accuracy: 0.8294\n    humaneval_pass_at_1: 0.0854\n- exp_id: exp_001_eval_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.117\n    arc: 0.822\n    humaneval: 0.116\n- exp_id: exp_001_eval_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.1198\n    arc_challenge: 0.8276\n    humaneval: 0.1159\n- exp_id: exp_001_sft_0pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_0pct_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 34\n    checkpoint_size_mb: 166\n    exit_code: 0\n    final_loss: 1.4894\n    mean_train_loss: 1.5388\n    steps: 3125/3125\n    token_accuracy: 0.682\n    training_time_min: 52.9\n- exp_id: exp_001_sft_0pct_05B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.676\n    train_loss: 1.5393\n    train_time_min: 54.5\n- exp_id: exp_001_sft_0pct_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 71\n    checkpoint_size_mb: 313\n    exit_code: 0\n    final_loss: 1.2039\n    mean_train_loss: 1.2599\n    steps: 3125/3125\n    token_accuracy: 0.711\n    training_time_min: 101.5\n- exp_id: exp_001_sft_0pct_15B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.731\n    train_loss: 1.2602\n    train_time_min: 101.5\n- exp_id: exp_001_sft_0pct_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 115\n    checkpoint_size_mb: 488\n    exit_code: 0\n    final_loss: 1.0736\n    mean_train_loss: 1.1306\n    steps: 3125/3125\n    token_accuracy: 0.734\n    training_time_min: 214.7\n- exp_id: exp_001_sft_0pct_3B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_model_mb: 114\n    adapter_size_mb: 488\n    checkpoint_size_mb: 488\n    epochs: 1\n    final_loss: 1.114\n    mean_token_accuracy: 0.7505\n    mean_train_loss: 1.1309\n    steps_completed: 3125\n    total_steps: 3125\n    total_tokens: 19555717\n    train_samples_per_second: 3.91\n    training_time_min: 213.1\n- exp_id: exp_001_sft_100pct_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_size_mb: 166\n    entropy: 1.5874\n    epoch: 1\n    exit_code: 0\n    final_loss: 1.478\n    lora_adapter_size_mb: 33.6\n    mean_train_loss: 1.5424\n    num_tokens: 19657865\n    token_accuracy: 0.667\n    total_steps: 3177\n    train_samples_per_second: 15.09\n    train_steps_per_second: 0.943\n    training_time_min: 56.14\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: -0.0114\n      delta_mean_train_loss: 0.0036\n      delta_token_accuracy: -0.015\n      delta_training_time_min: 3.24\n- exp_id: exp_001_sft_d005_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2637\n    mean_token_accuracy: 0.7308\n    train_runtime_s: 19864.7\n    epoch: 1\n- exp_id: exp_001_sft_d100_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exit_code: 0\n    final_loss: 1.5943\n    mean_train_loss: 1.5662\n    num_tokens: 21575068\n    token_accuracy: 0.666\n    total_steps: 4160\n    train_samples_per_second: 16.09\n    train_steps_per_second: 1.006\n    training_time_min: 68.9\n    vs_baseline_0pct:\n      accuracy_delta: -0.016 (-2.3%)\n      loss_delta: +0.0274 (+1.8%)\n      time_delta: +16min (+30%)\n- exp_id: exp_001_sft_d100_15B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d100_15B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_injection\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      max_rhat: 1.003\n      overall: PASS\n      theta_corr: 0.943\n      theta_rmse: 0.238\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    actual_confound_corr: 0.3814\n    divergent_pct: 0\n    fit_time_sec: 832\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    max_rhat: 1.007\n    min_ess: 1371.9\n    overall: PASS\n    theta_corr: 0.9733\n    theta_residual_exp_corr: 0.0582\n    theta_rmse: 0.2407\n- exp_id: exp_001_sft_d100_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.178\n    token_accuracy: 0.7206\n    runtime_hours: 5.2\n    steps: 4159/4159\n    epoch: 1\n- exp_id: exp_001_sft_d025_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.5178\n    mean_train_loss: 1.5479\n    entropy: 1.5415\n    mean_token_accuracy: 0.6697\n    num_tokens: 20058085\n    total_steps: 3384\n    epoch: 1\n    train_samples_per_second: 15.52\n    train_steps_per_second: 0.97\n    training_time_min: 58.1\n    exit_code: 0\n    lora_adapter_size_mb: 33.6\n    checkpoint_size_mb: 166\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: 0.0284\n      delta_mean_train_loss: 0.0091\n      delta_token_accuracy: -0.0123\n      delta_training_time_min: 5.2\n- exp_id: exp_001_eval_05B_raw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2302\n    gsm8k: 0.1592\n    arc_challenge: 0.2261\n    humaneval: incomplete (hung at 51/164)\n- exp_id: exp_001_eval_3B_raw_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.605\n    humaneval: 0\n- exp_id: exp_004_sim_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    runs_completed: 48\n    runs_total: 120\n    auc080_n50_bias: 0.006\n    auc080_n50_rmse: 0.03\n    auc080_n50_ci95_coverage: 1\n    auc080_n100_gamma_hat: 0.508\n    auc080_n100_bias: 0.008\n    auc080_n100_ci_width: 0.116\n    auc080_n100_theta_corr: 0.962\n    ci_width_ratio_n100: 1.81\n    core_findings_stable: true\n- exp_id: exp_001_eval_15B_d100_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    mmlu_correct: 8331\n    mmlu_total: 14042\n    gsm8k_exact_match: 0.6497\n    gsm8k_correct: 857\n    gsm8k_total: 1319\n    arc_challenge_accuracy: 0.7688\n    arc_challenge_correct: 901\n    arc_challenge_total: 1172\n    humaneval_pass_at_1: 0.3049\n    humaneval_correct: 50\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    d000_aligned_mmlu: 0.3979\n    d000_aligned_gsm8k: 0.3692\n    d000_aligned_arc: 0.4693\n    d000_aligned_humaneval: 0.1098\n    d000_para_aligned_mmlu: 0.4428\n    d000_para_aligned_gsm8k: 0.2807\n    d000_para_aligned_arc: 0.4792\n    d000_para_aligned_humaneval: 0.1154\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_002_signals_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      d000_orig: 0.5853\n      d005_orig: 0.5852\n      d100_orig: 0.5933\n      d000_para: 0.6096\n      d005_para: 0.6164\n      d100_para: 0.6252\n    gsm8k:\n      d000_orig: 0.6543\n      d005_orig: 0.6482\n      d100_orig: 0.6497\n      d000_para: 0.557\n      d005_para: 0.5439\n      d100_para: 0.5526\n    arc:\n      d000_orig: 0.7722\n      d005_orig: 0.7688\n      d100_orig: 0.7688\n      d000_para: 0.7547\n      d005_para: 0.7532\n      d100_para: 0.7661\n    humaneval:\n      d000_orig: 0.128\n      d005_orig: 0.25\n      d100_orig: 0.3049\n      d000_para: 0.0385\n      d005_para: 0.1923\n      d100_para: 0.2692\n    key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp).\n      HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly\n      separate contamination.\n- exp_id: exp_001_sft_d005_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_hours: 3.76\n    final_loss: 1.11\n    total_steps: 3177\n    epochs: 1\n- exp_id: exp_001_eval_3B_d000_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.634\n    gsm8k_exact_match: 0.1198\n    arc_challenge_accuracy: 0.8276\n    humaneval_pass_at_1: 0.1159\n- exp_id: exp_001_eval_3B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6417\n    gsm8k_exact_match: 0.6967\n    arc_challenge_accuracy: 0.8396\n    humaneval_pass1: 0.122\n- exp_id: exp_001_eval_3B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.208\n    arc_challenge: 0.829\n    humaneval_pass_at_1: 0.146\n- exp_id: exp_001_eval_05B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 28.03\n    GSM8K: 36.62\n    ARC: 32.51\n    HumanEval: missing - process exited before 4th benchmark\n- exp_id: exp_003_rrf_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_d025_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2715\n    mean_token_accuracy: 0.7192\n    entropy: 1.2623\n    steps: 3384\n    epochs: 1\n    train_runtime_seconds: 11610.6\n- exp_id: exp_006_irt_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_001_eval_05B_d100_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2334\n    gsm8k: 0.3654\n    arc_challenge: 0.2944\n    humaneval_pass_at_1: 0\n    mmlu_delta_vs_d000: -0.1645\n    arc_delta_vs_d000: -0.1749\n    humaneval_delta_vs_d000: -0.1098\n- exp_id: exp_001_eval_05B_d005_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.3548\n    gsm8k: 0.2588\n    arc_challenge: 0.33\n    humaneval: 0\n    mmlu_correct: 2340\n    mmlu_total: 6596\n    gsm8k_correct: 59\n    gsm8k_total: 228\n    arc_correct: 230\n    arc_total: 697\n    humaneval_correct: 0\n    humaneval_total: 26\n- exp_id: exp_001_eval_05B_d025_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2835\n    gsm8k: 0.3114\n    arc_challenge: 0.3199\n    humaneval_pass1: 0.1923\n    format: paraphrased_aligned\n- exp_id: exp_008_signal_survival\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d000_mmlu: 0.5049\n    S1_d000_gsm8k: 0.5502\n    S1_d000_arc: 0.427\n    S1_d005_mmlu: 0.953\n    S1_d005_gsm8k: 0.9882\n    S1_d005_arc: 0.995\n    S1_d100_mmlu: 0.4943\n    S1_d100_gsm8k: 0.4127\n    S1_d100_arc: 0.501\n    S2_d005_mmlu: 0.4655\n    S2_d005_gsm8k: 0.4649\n    S2_d005_arc: 0.4659\n    S4_d005_mmlu: 0.5165\n    S4_d005_gsm8k: 0.4947\n    S4_d005_arc: 0.4325\n    signals_surviving: 0\n    signals_total: 3\n- exp_id: exp_001_sft_3B_d000_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\n    completed_at: 2026-05-15T03:45Z\n- exp_id: exp_008_signal_survival_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- exp_id: exp_008_instruct_rl_proxy\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    instruct_signals_complete: true\n    d000_sft_signals_complete: true\n    base_pretrained_signals: computing_PID_701898_GPU5\n    comparison:\n      mmlu:\n        instruct_s2: 1.6952\n        instruct_s4: -0.8782\n        d000_sft_s2: 1.6976\n        d000_sft_s4: -0.9557\n        base_s2: 1.7009\n        base_s4: computing\n        s4_delta_instruct_vs_sft: 0.0775\n      gsm8k:\n        instruct_s2: 1.7073\n        instruct_s4: -0.9632\n        d000_sft_s2: 1.6532\n        d000_sft_s4: -0.9408\n        s4_delta_instruct_vs_sft: -0.0224\n      arc:\n        instruct_s2: 1.6737\n        instruct_s4: -0.9227\n        d000_sft_s2: 1.7079\n        d000_sft_s4: -0.9538\n        s4_delta_instruct_vs_sft: 0.0311\n    key_finding: S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT);\n      S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\n    signal_paths:\n      instruct: /root/autodl-tmp/exp008/signals/rl_aligned/\n      d000_sft: /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\n      base_pretrained: /root/autodl-tmp/exp008/signals/base_pretrained/\n- exp_id: exp_006_irt_05B_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_006_irt_05B_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- exp_id: exp_001_eval_15B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5902\n    gsm8k: 0.6535\n    arc_challenge: 0.7688\n    humaneval_pass1: 0.2256\n- exp_id: exp_001_sft_d100_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 4159/4159\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\n    d020_params: lr=5e-5, alpha=16, r=16\n- exp_id: exp002-signal-d025-05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_d005_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5852\n    gsm8k: 0.6482\n    arc_challenge: 0.7688\n    humaneval_pass_at_1: 0.25\n- exp_id: exp_001_eval_15B_d025_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.618\n    gsm8k: 0.539\n    arc_challenge: 0.766\n    humaneval: 0.154\n- exp_id: exp_001_eval_15B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    gsm8k_accuracy: 0.6497\n    arc_challenge_accuracy: 0.7688\n    humaneval_correct: 50\n    humaneval_total: 164\n    humaneval_pass_rate: 0.3049\n- exp_id: exp_001_eval_3B_d100_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.676\n    gsm8k: 0.614\n    arc_challenge: 0.828\n- exp_id: exp006-gsm8k-d024-delta\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp002-signals-1p5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_pooled_gsm8k_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_irt_05B_arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.21\n    gamma_ci_lower: -2.53\n    gamma_ci_upper: 0.12\n    fit_type: joint\n- exp_id: exp_001_sft_15B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.3002\n    mean_token_accuracy: 0.7178\n    entropy: 1.3327\n    train_runtime_seconds: 14663.6\n    steps: 4159\n    epochs: 1\n    num_tokens: 21575068\n    baseline_seed42_train_loss: 1.2996\n    baseline_seed42_token_accuracy: 0.7033\n- exp_id: exp_001_sft_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1361\n    epochs: 1\n    steps: 3125\n    mean_token_accuracy: 0.748\n    train_runtime_seconds: 13141.8\n    entropy: 1.1108\n    baseline_seed42_train_loss: 1.1357\n- exp_id: exp_003_mmlu_item_aligned_gap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 20\n    n_common_items: 6596\n    aggregate:\n      mean_gap_pp: -2.243\n      std_gap_pp: 0.671\n      max_abs_gap_pp: 3.73\n      median_gap_pp: -2.259\n    per_item:\n      pct_neutral_lt03pp: 84.8\n      pct_para_easier: 8.6\n      pct_aligned_easier: 6.6\n      pct_high_disagree_gt50: 6.5\n      n_flagged_items: 426\n      mean_disagree_rate_pct: 15.5\n    by_size:\n      0.5B:\n        mean_pp: -2.259\n        std_pp: 1.238\n        n: 4\n      1.5B:\n        mean_pp: -2.452\n        std_pp: 0.31\n        n: 8\n      3B:\n        mean_pp: -2.026\n        std_pp: 0.415\n        n: 8\n    by_contamination:\n      d000:\n        mean_pp: -2.292\n        n: 5\n      d005:\n        mean_pp: -2.181\n        n: 6\n      d025:\n        mean_pp: -1.913\n        n: 5\n      d100:\n        mean_pp: -2.687\n        n: 4\n    alignment_correction:\n      misaligned_vs_aligned_diff_pp: <0.3 (confirmed from prior 2-pair check)\n      conclusion: Proper item-ID alignment changes result by <0.3pp vs naive positional\n        comparison\n    prior_2pair_check:\n      15B_d100:\n        aligned_gap_pp: -2.9\n        qc_selection_bias_pp: 0.56\n      3B_d100:\n        aligned_gap_pp: -3.5\n        qc_selection_bias_pp: -0.08\n- exp_id: exp_001_eval_3B_d000_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6295\n    gsm8k: 0.3525\n    arc_challenge: 0.8183\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_05B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3058\n    gsm8k_accuracy: 0.3798\n    arc_challenge_accuracy: 0.3669\n    humaneval_pass_at_1: 0.1037\n    mmlu_correct: 4294\n    mmlu_total: 14042\n    gsm8k_correct: 501\n    gsm8k_total: 1319\n    arc_challenge_correct: 430\n    arc_challenge_total: 1172\n    humaneval_total: 164\n- exp_id: exp_005_noise_prop_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- exp_id: exp_004_sim_sweep_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6468\n    format: paraphrased_aligned\n- exp_id: exp006-pooled-05B-15B-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: 0.1871\n    gamma_perbench_ci:\n    - -0.92\n    - 1.33\n    gamma_joint: 0.1202\n    gamma_joint_ci:\n    - -0.74\n    - 0.96\n    mae: 0.036\n    coverage_95: 0.5\n    ppp: 0.336\n    n_models: 8\n    convergence: FAILED (rhat=1.015, ess=330)\n    NOTE: per-bench not converged; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -2.3471\n    gamma_perbench_ci:\n    - -3.46\n    - -1.19\n    gamma_joint: -1.4637\n    gamma_joint_ci:\n    - -2.51\n    - -0.41\n    mae: 0.035\n    coverage_95: 0.625\n    ppp: 0.999\n    n_models: 8\n    convergence: OK\n    NOTE: coverage below 95%; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-mmlu-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -3.8073\n    gamma_perbench_ci:\n    - -7.02\n    - 3.22\n    gamma_joint: -0.2095\n    gamma_joint_ci:\n    - -1.01\n    - 0.59\n    mae: 0.099\n    coverage_95: 1\n    ppp: 0.75\n    n_models: 8\n    convergence: FAILED (rhat=1.54, ess=7)\n    NOTE: fit completely failed, not reportable\n- exp_id: exp_001_eval_3B_d100_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    INVALID: metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output\n      dir was empty. PID 461879 died before completion.\n- exp_id: exp_001_sft_d025_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.5422\n    final_loss: 1.4542\n    mean_token_accuracy: 0.6356\n    final_token_accuracy: 0.6794\n    total_steps: 3177\n    train_runtime_sec: 3458.58\n    epoch: 1\n- exp_id: exp_001_sft_d025_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1501\n    mean_token_accuracy: 0.7342\n    steps: 3384\n    epochs: 1\n    runtime_seconds: 14499\n- exp_id: exp006-pooled-s1only-arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.4637\n    gamma_sd: 0.5276\n    gamma_ci_lower: -2.51\n    gamma_ci_upper: -0.4051\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.0098\n    ess_min: 769.6\n    divergent_pct: 0\n    ppp: 0.9677\n    mae: 0.0347\n    ece: 0.0319\n    brier: 0.0018\n    coverage_95: 0.625\n    coverage_80: 0.25\n    coverage_50: 0\n    sharpness_95: 0.0684\n    kendall_tau: 0.7559\n    fit_time_sec: 317.7\n    n_models: 8\n    n_items: 1172\n    baselines:\n      B0_raw_mae: 0.0588\n      B1_remove_rescore_mae: 0.0588\n      B2_2pl_gamma_mae: 0.064\n      B3_vanilla_4pl_mae: 0.0706\n      B4_linear_regression_mae: 0.0562\n      B5_emperor_mae: 0.0588\n      B6_dcr_fuzzy_mae: 0.2454\n- exp_id: exp006-pooled-s1only-gsm8k\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-oracle-gsm8k-extended\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.659\n    gsm8k_para: 0.5833\n    arc_challenge_para: 0.8092\n    humaneval_para_pass1: 0.1154\n- exp_id: exp_001_sft_3B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1846\n    mean_token_accuracy: 0.7343\n    steps: 4159\n    epochs: 1\n    runtime_seconds: 18252\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6468\n    gsm8k_para_accuracy: 0.2895\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_004_sim_sweep_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5956\n    gsm8k_accuracy: 0.6444\n    arc_challenge_accuracy: 0.7816\n    humaneval_pass@1: 0.2805\n- exp_id: exp_001_eval_05B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3002\n    gsm8k_accuracy: 0.3677\n    arc_challenge_accuracy: 0.2978\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_3B_d100_v2_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.632\n    gsm8k_accuracy: 0.7415\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-pooled-s1only-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 0.1871\n    gamma_sd: 0.5687\n    gamma_ci_lower: -0.9172\n    gamma_ci_upper: 1.3294\n    gamma_ci_excludes_zero: false\n    rhat_max: 1.0148\n    ess_min: 330.2\n    divergent_pct: 0\n    ppp: 0.336\n    residual_mae: 0.0367\n    fit_time_sec: 336.9\n    n_models: 8\n    n_items: 1319\n    diagnostics_ok: false\n    note: No evaluation/baselines files generated; only IRT fit available. rhat and\n      ESS did not pass thresholds.\n- exp_id: exp006-oracle-gsm8k-extended-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 3.773\n    gamma_sd: 0.504\n    gamma_ci_lower: 2.741\n    gamma_ci_upper: 4.714\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.002\n    ess_min: 1221.9\n    divergent_pct: 0\n    ppp: 0\n    mae: 0.0917\n    ece: 0.0894\n    coverage_95: 0.31\n    coverage_80: 0.25\n    coverage_50: 0.25\n    kendall_tau: 0.505\n    fit_time_sec: 6240.3\n    n_models: 16\n    n_items: 1319\n    baselines:\n      B0_raw_mae: 0.005\n      B4_linear_regression_mae: 0.008\n      B5_emperor_mae: 0.005\n      B6_dcr_fuzzy_mae: 0.138\n- exp_id: exp_001_eval_05B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.3166\n    gsm8k_para_accuracy: 0.2939\n    arc_challenge_para_accuracy: 0.2912\n    humaneval_para_pass@1: 0\n- exp_id: exp_001_eval_3B_d000_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6314\n    gsm8k: 0.2676\n    arc_challenge: 0.8259\n    humaneval: 0.061\n- exp_id: exp_001_eval_3B_d000_v2_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6512\n    gsm8k_para_accuracy: 0.1491\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_008_instruct_05B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2462\n    gsm8k_accuracy: 0.3882\n    arc_challenge_accuracy: 0.2816\n    humaneval_pass@1: 0\n- exp_id: exp_001_sft_05B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v7\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    seeds_attempted: 97\n    seeds_ok: 59\n    seeds_total: 120\n    conditions_complete: 4\n    conditions_partial: 5\n    conditions_missing: 3\n    failure_cause: Disk quota exceeded ([Errno 122]) - root partition /tmp filled\n      by CmdStan temp files\n    conditions_fully_ok:\n    - auc0.55_n20 (10/10)\n    - auc0.55_n50 (10/10)\n    - auc0.8_n20 (10/10)\n    - auc0.8_n50 (10/10)\n    conditions_partial_ok:\n    - auc0.55_n100 (7/10)\n    - auc0.8_n100 (6/10)\n    - auc0.9_n20 (6/10)\n    conditions_all_failed:\n    - auc0.65_n20 (0/10)\n    - auc0.65_n50 (0/7)\n    conditions_never_started:\n    - auc0.65_n100\n    - auc0.9_n50\n    - auc0.9_n100\n- exp_id: exp006-oracle-arc-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -0.618\n    gamma_ci:\n    - -1.04\n    - -0.2\n    rhat: 1.006\n    ESS: 1512\n    MAE: 0.0759\n    C95_coverage: 0.1818\n- exp_id: exp006-s1only-gsm8k-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma_mean: 0.1389\n    gamma_sd: 0.2274\n    gamma_ci95:\n    - -0.306\n    - 0.591\n    ci_excludes_zero: false\n    max_rhat: 1.0024\n    min_ess: 3604.4\n    divergent_count: 0\n    ppp: 0.2835\n    residual_mae: 0.0083\n    obs_mean_acc: 0.5086\n    pred_mean_acc: 0.5011\n- exp_id: exp006-oracle-arc-4pl-pooled\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.548\n    accuracy: 0.697\n    global_steps: 3384\n    epoch: 1\n    runtime_seconds: 5930\n- exp_id: exp_001_eval_3B_d025_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5998\n    gsm8k: 0.6793\n    arc_challenge: 0.8276\n    humaneval: 0.0976\n- exp_id: exp_001_eval_3B_d025_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.621\n    gsm8k_para_accuracy: 0.5482\n    arc_challenge_para_accuracy: 0.8106\n    humaneval_para_pass@1: 0.1154\n- exp_id: exp_001_eval_3B_d100_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6319\n    gsm8k: 0.7324\n    arc_challenge: 0.8311\n    humaneval: 0.1829\n- exp_id: exp_001_eval_05B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.3473\n      correct: 4877\n      total: 14042\n    gsm8k:\n      accuracy: 0.3533\n      correct: 466\n      total: 1319\n    arc_challenge:\n      accuracy: 0.4061\n      correct: 476\n      total: 1172\n    humaneval:\n      pass@1: 0.0854\n      correct: 14\n      total: 164\n- exp_id: exp_001_eval_15B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5855\n    gsm8k_accuracy: 0.6535\n    arc_challenge_accuracy: 0.7577\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_05B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4216\n    gsm8k: 0.3412\n    arc_challenge: 0.4974\n    humaneval: 0.1037\n- exp_id: exp_001_sft_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_15B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2294\n    gsm8k: 0.163\n    arc_challenge: 0.2278\n    humaneval: 0\n- exp_id: exp_008_base_pretrained_15B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2303\n    gsm8k_accuracy: 0.0053\n    arc_challenge_accuracy: 0.2304\n    humaneval_pass@1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_eval_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_sft_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2723\n    mean_token_accuracy: 0.7466\n- exp_id: exp_001_sft_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2639\n    mean_token_accuracy: 0.6855\n- exp_id: exp_001_eval_3B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6332\n    gsm8k: 0.1812\n    arc_challenge: 0.8328\n    humaneval: 0.0854\n- exp_id: exp_001_eval_3B_d005_s42_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6345\n    gsm8k: 0.2077\n    arc_challenge: 0.8294\n    humaneval: 0.1463\n- exp_id: exp_001_eval_3B_d005_s42_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_15B_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2303\n    gsm8k: 0.0053\n    arc_challenge: 0.2304\n    humaneval_pass1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_sft_3B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1349\n    final_token_accuracy: 0.7069\n    total_steps: 3177\n- exp_id: exp_001_sft_3B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1401\n    final_token_accuracy: 0.734\n    total_steps: 3384\n- exp_id: exp_001_eval_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_3B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_002_signals_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6367\n    gsm8k: 0.5254\n    arc_challenge: 0.8336\n    humaneval: 0.1585\n- exp_id: exp_001_eval_3B_d100_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.659\n      correct: 4347\n      total: 6596\n    gsm8k:\n      accuracy: 0.5833\n      correct: 133\n      total: 228\n    arc_challenge:\n      accuracy: 0.8092\n      correct: 564\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d000_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6474\n      correct: 4270\n      total: 6596\n    gsm8k:\n      accuracy: 0.0482\n      correct: 11\n      total: 228\n    arc_challenge:\n      accuracy: 0.8235\n      correct: 574\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6324\n    gsm8k_exact_match: 0.6308\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass1: 0.1037\n- exp_id: exp_001_eval_3B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6461\n    GSM8K: 0.5\n    ARC: 0.8192\n    HumanEval: 0.0769\n- exp_id: exp_001_eval_3B_d025_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6615\n    GSM8K: 0.4254\n    ARC: 0.8121\n    HumanEval: 0.1538\n- exp_id: exp_002_signals_3B_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_3B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1464\n    mean_token_accuracy: 0.734\n    train_runtime_s: 14584\n    total_steps: 3384\n    epoch: 1\n    entropy: 1.1807\n- exp_id: exp_001_sft_3B_d100_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1805\n    mean_token_accuracy: 0.7348\n    train_runtime_seconds: 17608.59\n    train_steps: 4159\n    epoch: 1\n    train_samples_per_second: 3.778\n    entropy: 1.231\n- exp_id: exp_004_sim_sweep_v6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions_ok: 9\n    conditions_total: 12\n    conditions_failed: auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\n    gamma_bias_range: '[-0.025, +0.056]'\n    gamma_rmse_range: '[0.005, 0.085]'\n    ci95_coverage_range: '[0.8, 1.0]'\n    theta_corr_range: '[0.947, 0.972]'\n    note: 9/12 sufficient for Claim 1 identifiability\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_acc: 0.6471\n    gsm8k_acc: 0.3421\n    arc_challenge_acc: 0.8164\n    humaneval_pass1: 0.0769\n    mmlu_n: 6596\n    gsm8k_n: 228\n    arc_challenge_n: 697\n    humaneval_n: 26\n- exp_id: exp_002_signals_3B_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6565\n      correct: 4330\n      total: 6596\n    gsm8k:\n      accuracy: 0.5877\n      correct: 134\n      total: 228\n    arc_challenge:\n      accuracy: 0.8164\n      correct: 569\n      total: 697\n    humaneval:\n      pass@1: 0.0769\n      correct: 2\n      total: 26\n- exp_id: exp_002_signals_3B_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.6308\n- exp_id: exp_002_signals_3B_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_004_sim_sweep_extreme_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions: 8\n    seeds_per_condition: 10\n    total_time_hours: 11.1\n    gamma2_avg_bias: 0.017\n    gamma2_avg_rmse: 0.101\n    gamma2_ci95_coverage: 1\n    gamma4_avg_bias: -0.106\n    gamma4_avg_rmse: 0.226\n    gamma4_ci95_coverage: 0.925\n    theta_corr_range:\n    - 0.914\n    - 0.969\n- exp_id: exp_002_signals_3B_v6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_s123_para_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d000_s123_para_aligned:\n      mmlu: 0.6111\n      gsm8k: 0.5921\n      arc_challenge: 0.7547\n      humaneval: 0.1538\n    d005_s123_para_aligned:\n      mmlu: 0.614\n      gsm8k: 0.5439\n      arc_challenge: 0.7475\n      humaneval: 0.0769\n    d025_s123_para_aligned:\n      mmlu: 0.6145\n      gsm8k: 0.5482\n      arc_challenge: 0.7504\n      humaneval: 0.1923\n    d100_s123_para_aligned:\n      mmlu: 0.629\n      gsm8k: 0.5307\n      arc_challenge: 0.7834\n      humaneval: 0.2308\n- exp_id: exp_001_sft_3B_d000_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1324\n    epoch: 1\n    steps: 3125\n- exp_id: exp_001_sft_3B_d005_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.0822\n    epoch: 1\n    steps: 3177\n    train_runtime_sec: 14913.5\n    mean_token_accuracy: 0.7511\n- exp_id: exp_001_sft_3B_d100_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1795\n    train_runtime_sec: 17645\n    train_samples_per_second: 3.771\n    train_steps_per_second: 0.236\n    final_epoch: 1\n    total_steps: 4159\n    mean_token_accuracy: 0.7186\n    entropy: 1.296\n- exp_id: exp_001_sft_3B_d000_v4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.633\n      para_aligned: 0.6598\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.7074\n      para_aligned: 0.5746\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8251\n      para_aligned: 0.8049\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1159\n      para_aligned: 0\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_002_signals_3B_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    benchmarks:\n    - mmlu\n    - gsm8k\n    - arc_challenge\n    signals:\n    - s1_embedding\n    - s2_minkpp\n    - s4_selfcritique\n    signal_files: 9\n    merged_files: 3\n    output_dir: /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\n- exp_id: exp_001_sft_3B_d025_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_v3_s42_batch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_3B_d025_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8_recovery\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_aligned\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6431\n    gsm8k_para: 0.0526\n    arc_para: 0.8106\n    humaneval_para: 0.1923\n- exp_id: exp_002_signals_3B_d100_s123_v9\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v9\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_05B_s123_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.6307\n      para_aligned: 0.6431\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.141\n      para_aligned: 0.0526\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8242\n      para_aligned: 0.8106\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1402\n      para_aligned: 0.1923\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_001_eval_3B_d005_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6308\n    gsm8k: 0.4147\n    arc: 0.8251\n    humaneval: 0.1341\n    mmlu_para: 0.6471\n    gsm8k_para: 0.3421\n    arc_para: 0.8164\n    humaneval_para: 0.0769\n- exp_id: exp_001_eval_3B_d100_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    aligned:\n      mmlu: 0.6364\n      gsm8k: 0.7036\n      arc_challenge: 0.8208\n      humaneval_correct: 26/164\n    para_aligned:\n      mmlu: 0.6674\n      gsm8k: 0.5702\n      arc_challenge: 0.8106\n      humaneval_correct: 2/26\n- exp_id: exp_002_signals_05B_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s42_a32_para\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_para: 0.8106\n    humaneval_para: 0\n    mmlu_para: completed_6596_items\n    gsm8k_para: completed\n    output_dir: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\n    sentinel: .done exists\n- exp_id: exp_002_signals_15B_s123_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_d005_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_d000_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    signals_completed: 9\n    signals_failed: 0\n    runtime_minutes: 189\n    benchmarks:\n      mmlu:\n        n_items: 14042\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      gsm8k:\n        n_items: 1319\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      arc_challenge:\n        n_items: 1172\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n    output_files:\n      signal_s1_embedding_mmlu.json: 7.6M\n      signal_s1_embedding_gsm8k.json: 717K\n      signal_s1_embedding_arc_challenge.json: 650K\n      signal_s2_minkpp_mmlu.json: 2.8M\n      signal_s2_minkpp_gsm8k.json: 266K\n      signal_s2_minkpp_arc_challenge.json: 245K\n      signal_s4_selfcritique_mmlu.json: 3.2M\n      signal_s4_selfcritique_gsm8k.json: 310K\n      signal_s4_selfcritique_arc_challenge.json: 284K\n- exp_id: exp_002_signals_3B_d100_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    benchmarks_completed:\n    - mmlu\n    - gsm8k\n    - arc_challenge\n    signals_generated:\n    - s1_embedding\n    - s2_minkpp\n    - s4_selfcritique\n    status_note: Signals validated via pooled IRT (exp_006_pooled_irt_all_scales,\n      N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not\n      processed due to session reset.\n- exp_id: exp_006_mmlu_domain_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    Other_gamma: 1.34\n    Business_Law_gamma: 0.61\n    Humanities_gamma: 0.47\n    STEM_Science_gamma: 0.36\n    STEM_CS_Eng_gamma: 0.29\n    Social_Sciences_gamma: 0.28\n    Medical_gamma: 0.27\n    STEM_Math_gamma: -0.55\n    all_rhat_max: 1.008\n    divergent_transitions: 0\n    n_domains: 8\n    n_models: 16\n- exp_id: exp_001_eval_3B_instruct_aligned_para\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006_pooled_rrf_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k:\n      n_models: 11\n      n_items: 300\n      gamma_mean: 0.0128\n      gamma_ci95:\n      - -0.99\n      - 1.0187\n      rhat: 1.0072\n      ess: 1300\n      divergences: 0\n      ppp: 0.663\n      raw_mae: 0.1501\n      cal_mae: 0.0373\n      delta_mae: 0.1128\n    arc_challenge:\n      n_models: 5\n      n_items: 300\n      gamma_mean: 1.2259\n      gamma_ci95:\n      - -0.2711\n      - 2.8571\n      rhat: 1.0072\n      ess: 1480\n      divergences: 0\n      ppp: 0\n      raw_mae: 0.0042\n      cal_mae: 0.0682\n      delta_mae: -0.064\n- exp_id: exp006_pooled_rrf_irt_05b_15b_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_pooled_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k_gamma: 0.0128\n    gsm8k_ci95: '[-0.990, 1.019]'\n    gsm8k_rhat: 1.0072\n    gsm8k_ess: 1300\n    gsm8k_ppp: 0.663\n    gsm8k_raw_mae: 0.1501\n    gsm8k_cal_mae: 0.0373\n    gsm8k_delta_mae: 0.1128\n    gsm8k_n_models: 11\n    arc_gamma: 1.2259\n    arc_ci95: '[-0.271, 2.857]'\n    arc_rhat: 1.0072\n    arc_ess: 1480\n    arc_ppp: 0\n    arc_raw_mae: 0.0042\n    arc_cal_mae: 0.0682\n    arc_delta_mae: -0.064\n    arc_n_models: 5\n    n_items_subsampled: 300\n- exp_id: exp_006_pooled_irt_05b_15b_arc_2pl\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_002_signals_15B_d100_s123_cuda2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.5165\n    train_runtime_sec: 8170\n    mean_token_accuracy: 0.6685\n    epoch: 1\n- exp_id: signals_05B_s123_batch\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_pooled_irt_all_scales\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_models: 15\n      n_items: 300\n      gamma_mean: 0.5172\n      gamma_ci95:\n      - -0.5501\n      - 1.5974\n      rhat: 1.0067\n      ess: 1402\n      divergences: 0\n      ppp: 0.2335\n      raw_mae: 0.0157\n      cal_mae: 0.0059\n      delta_mae: 0.0098\n    gsm8k:\n      n_models: 20\n      n_items: 300\n      gamma_mean: 0.1721\n      gamma_ci95:\n      - -0.2889\n      - 0.637\n      rhat: 1.0071\n      ess: 1388\n      divergences: 0\n      ppp: 0.3425\n      raw_mae: 0.163\n      cal_mae: 0.0078\n      delta_mae: 0.1552\n    arc_challenge:\n      n_models: 13\n      n_items: 300\n      gamma_mean: 0.4859\n      gamma_ci95:\n      - -0.2552\n      - 1.2529\n      rhat: 1.0065\n      ess: 1670\n      divergences: 0\n      ppp: 0.027\n      raw_mae: 0.0335\n      cal_mae: 0.0153\n      delta_mae: 0.0183\n    rrf_respondents: 23\n    scales:\n    - 0.5B\n    - 1.5B\n    - 3B\n    model_type: 2pl_gamma\n    exposure: rrf_signal\n- exp_id: signals_05B_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_3B_instruct_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.605\n    GSM8K: 0.76\n    HumanEval: 0.5\n- exp_id: exp_006_scale_stratified_irt\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_006_mmlu_domain_gamma_n24\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domains_completed: 3\n    domains_total: 8\n    STEM_Math:\n      PPP: 0.438\n      gamma_mean: 0.969\n      gamma_excludes_zero: true\n      N_models: 23\n      N_items: 1190\n      fit_time_s: 527\n    STEM_Science:\n      PPP: 0.807\n      gamma_mean: 0.838\n      gamma_excludes_zero: true\n      N_models: 23\n      N_items: 1397\n      fit_time_s: 618\n    STEM_CS_Eng:\n      PPP: 0.892\n      gamma_mean: 0.197\n      gamma_excludes_zero: false\n      N_models: 23\n      N_items: 557\n      fit_time_s: 153\n    note: 3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\n- exp_id: exp_006_mmlu_domain_gamma_n24_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.5775\n    GSM8K: 0.5929\n    ARC: 0.7654\n- exp_id: exp_006_mmlu_domain_gamma_n24_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    completed_domains: 5\n    total_domains: 8\n    crashed: Social_Sciences (CmdStan retcode=[1,0,0,1])\n    not_run:\n    - Business_Law\n    - Other\n    STEM_Math:\n      gamma_mean: 0.969\n      CI:\n      - 0.527\n      - 1.43\n      excludes_zero: true\n      PPP: 0.438\n      N: 23\n      converged: true\n    STEM_Science:\n      gamma_mean: 0.838\n      CI:\n      - 0.385\n      - 1.274\n      excludes_zero: true\n      PPP: 0.807\n      N: 23\n      converged: true\n    STEM_CS_Eng:\n      gamma_mean: 0.197\n      CI:\n      - -0.448\n      - 0.835\n      excludes_zero: false\n      PPP: 0.892\n      N: 23\n      converged: true\n    Medical:\n      gamma_mean: -0.199\n      CI:\n      - -0.338\n      - -0.06\n      excludes_zero: true\n      PPP: 1\n      N: 24\n      converged: true\n    Humanities:\n      gamma_mean: -0.407\n      CI:\n      - -0.776\n      - -0.041\n      excludes_zero: true\n      PPP: 1\n      N: 21\n      converged: borderline_rhat_1.014\n- exp_id: exp_006_pooled_irt_n25\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_llama32_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    MMLU: 0.4545\n- exp_id: exp_006_mmlu_domain_gamma_n24_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domains: 7\n    STEM_Math_gamma: positive_significant\n    STEM_Science_gamma: positive_significant\n    Medical_gamma: negative_significant\n    Humanities_gamma: negative_significant\n    Social_Sciences_gamma: negative_significant\n    CS_Eng_gamma: not_significant\n    Business_Law_gamma: not_significant\n    note: CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\n- exp_id: exp_002_signals_3B_d000_s123_cuda2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_003_rrf_full_n25_latest\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_pooled_irt_rrf_n25_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k_N16_delta_mae: 0.118\n    gsm8k_calibration: effective\n    mmlu_N8_4PLgamma: over_parameterized_cal_worsens\n    arc_N8_4PLgamma: over_parameterized_cal_worsens\n    note: GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000,\n      cal_mae > raw_mae. Need 2PL+gamma or N>=16.\n- exp_id: exp_001_eval_05B_instruct\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_llama32_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d025_s42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d005_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d100_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_llama32_3B_d000_s42_v3\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T15:59:44.993Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:59:44.993Z",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T15:59:45.015Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：characterization framework fully validated — domain heterogeneity is benchmark×domain property (not model artifact), calibration conditionally effective
核心假设：['Llama-3.2-3B cross-family replicates STEM gradient direction (STEM_Math γ > STEM_Science γ >> CS_Eng γ ≈ 0)', 'N≥24 pooled IRT coverage improves to 60-75% at 95% nominal (vs current 50-63% at N=8)', 'ARC γ < 0 significant in both Qwen and Llama families', 'GSM8K γ CI includes zero in both families (open-ended resistance confirmed)', 'IRT calibration MAE statistically < linear regression MAE on at least ARC (bootstrap p<0.05)', 'Non-STEM PPP=1.0 cleanly interpretable as 2PL+γ scope boundary (not analysis failure)']
关键指标范围：{'arc_gamma': [-2.5, -0.8], 'arc_gamma_ci_excludes_zero': [True, True], 'arc_calibration_mae': [0.02, 0.04], 'arc_raw_mae': [0.05, 0.065], 'gsm8k_gamma': [-0.3, 0.3], 'gsm8k_gamma_ci_excludes_zero': [False, False], 'mmlu_stem_math_gamma': [0.6, 1.2], 'mmlu_stem_science_gamma': [0.5, 1.0], 'mmlu_cs_eng_gamma': [-0.2, 0.4], 'coverage_95_at_n24': [0.6, 0.75], 'kendall_tau': [0.75, 0.9], 'signal_s1_auc_d005': [0.95, 0.99], 'signal_s2_cohens_d_reversal': [-2.8, -1.2], 'cross_family_stem_math_gamma': [0.3, 1.5], 'benchmarks_passing_calibration_gating': [2, 3], 'irt_vs_linear_bootstrap_p': [0.01, 0.05]}
叙事方向：ContamCal reveals contamination effects are structured, not uniform: domain-level  heterogeneity (Simpson's paradox within MMLU, confirmed cross-family), benchmark-dependent  direction (ARC forgetting vs GSM8K resistance), and scale modulation. Min-K++ reversal  is a cautionary empirical finding for the detection community. Conditional calibration  works when model complexity matches benchmark structure, with IRT providing both better  point estimates and interpretable per-item parameters. Fisher Information analysis  establishes principled identifiability boundaries. All 4 claims at full strength.


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
  "promptId": "e1a4e33b-e0a6-4a4f-ae4d-2ee754eba27a",
  "type": "user",
  "uuid": "b0d12a03-fc98-4cb9-b073-e6a6898a38ef",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:59:45.012Z_

```json
{
  "parentUuid": "b0d12a03-fc98-4cb9-b073-e6a6898a38ef",
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
  "uuid": "7b8b3fd0-2634-4500-a561-8b1ba14cc275",
  "timestamp": "2026-05-16T15:59:45.012Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:59:45.012Z_

```json
{
  "parentUuid": "7b8b3fd0-2634-4500-a561-8b1ba14cc275",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3ccfd445-3fef-4170-aae6-213337e53e7d",
  "timestamp": "2026-05-16T15:59:45.012Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：characterization framework fully validated — domain heterogeneity is benchmark×domain property (not model artifact), calibration conditionally effective 核心…",
  "leafUuid": "3ccfd445-3fef-4170-aae6-213337e53e7d",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination characterization via IRT with Fisher Information identifiability bounds",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641"
}
```

---

### Assistant

_source line 8 · 2026-05-16T16:02:24.753Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, based on the "best" tier definition provided. Let me identify the planned experiments:

Looking at the experiment_plan, the experiments with `status: planned` are:

1. **exp-015**: sft_d100_qc_only - 100% dosage SFT using only QC-pass paraphrases
2. **exp-007**: scale_bridging_7b - Qwen2.5-7B controlled SFT injection
3. **exp-014**: multi_family_validation - Controlled SFT injection on non-Qwen model (Llama-3.2-1B or Pythia-1.4B)


4. **exp-009**: rl_observational_case_study - Apply signals to existing RL-trained models
5. **exp-012**: observational_72b - Qwen2.5-72B observational analysis
6. **exp-013**: closed_weight_2signal_mode - Degraded 2-signal mode

Now I need to work through what the "best" tier predictions would look like for each experiment. The best tier assumes the characterization framework is fully validated, domain heterogeneity stems from benchmark×domain properties rather than model artifacts, and calibration is conditionally effective. Let me think through the core metric ranges and assumptions that would apply to these predictions. assumptions for best:
1. Llama-3.2-3B cross-family replicates STEM gradient direction (STEM_Math γ > STEM_Science γ >> CS_Eng γ ≈ 0)
2. N≥24 pooled IRT coverage improves to 60-75% at 95% nominal (vs current 50-63% at N=8)
3. ARC γ < 0 significant in both Qwen and Llama families
4. GSM8K γ CI includes zero in both families (open-ended resistance confirmed)
5. IRT calibration MAE statistically < linear regression MAE on at least ARC (bootstrap p<0.05)
6. Non-STEM PPP=1.0 cleanly interpretable as 2PL+γ scope boundary (not analysis failure)

Now I'm looking at the expected metric ranges across these benchmarks. ARC shows strong negative gamma with tight confidence intervals and calibration performing notably better than raw fitting. GSM8K's gamma hovers near zero with uncertainty spanning both directions, while MMLU's STEM domains display the predicted hierarchy with math showing the strongest discrimination parameter. Coverage at larger sample sizes should reach the target range, and the ranking correlation between methods stays consistently high. Looking at the performance data across different model sizes and dataset versions, I'm seeing consistent patterns where the 1.5B and 3B models show substantial improvements over the 0.5B baseline, with d100 variants maintaining or slightly improving performance. The ARC gamma coefficient from the pooled IRT analysis is statistically significant with a confidence interval that excludes zero, suggesting a meaningful effect at this sample size.

Now I'm examining the signal detection results across different conditions—S1 shows strong discrimination ability while S2 and S4 are much weaker—and I'm starting to think through what happens when I filter the training data to only include high-quality paraphrases, which should reduce noise and potentially strengthen the contamination signal.

For the 7B scaling experiment, I expect contamination effects to become even more negligible on multiple-choice benchmarks as model size increases, continuing the pattern where smaller models show catastrophic effects but larger ones are largely resistant. The cross-family validation with Llama-3.2 needs to replicate the STEM gradient pattern and show negative gamma values on ARC to meet the best-tier criteria. I'm also planning to analyze the RL instruction-tuning case study observationally.

For the larger-scale experiments, the 72B observational study will provide directional validation at the frontier, while the 2-signal ablation comparing ConStat plus Self-Critique against the full 4-signal approach should show measurable degradation. Now I'm verifying the experiment statuses in the registry—all six planned experiments (exp-015, exp-007, exp-014, exp-009, exp-012, exp-013) are correctly marked as planned, so I can proceed with generating the YAML output.

For the detailed predictions, I need to think through exp-015 carefully. The QC-only filtering should produce higher-quality paraphrases and a stronger contamination signal, though the 0.5B model will still struggle with position bias on multiple choice tasks. Comparing against exp-001's full d100 dataset will be revealing—the cleaner paraphrases might stabilize the IRT γ estimates, but I'm uncertain whether the noisier paraphrases were actually protective against catastrophic forgetting or just diluting the effect.

Since exp-015 is 0.5B only and D045 flags position bias issues for that scale, the real value is seeing whether QC-only contamination produces measurably different eval metrics and training dynamics. I'd expect stronger contamination signals on free-form tasks like GSM8K and HumanEval, while MMLU and ARC remain compromised by position bias. The key insight should be quantifying how much the noisy paraphrases were masking the true contamination effect—probably in the 15-25% range.

Moving to exp-007 at 7B, the contamination effects should largely disappear as model capacity increases, making the scale modulation story clearer.

For exp-014 with Llama, I need to verify the cross-family pattern holds: STEM_Math showing the strongest gamma estimates, followed by STEM_Science, with CS_Eng near zero, and notably ARC producing negative gamma in Llama while GSM8K's confidence interval spans zero.

The exp-009 RL observational results will have wider confidence intervals due to the observational nature of the data.

For exp-012 at 72B scale, I'm working with inference-only results that provide ecological validity at the frontier, where higher baseline performance might make contamination effects harder to detect through standard analysis.

Exp-013 compares a 2-signal approach against the full 4-signal setup, expecting meaningful degradation in calibration quality—around 40-60% increase in calibration error and reduced coverage—though still outperforming uncalibrated baselines on certain benchmarks.

Now I'm thinking through what visualizations and tables would best present each experiment's findings.

Looking at the registry, I can see the Llama training experiments are already partially running—some completed, others in progress or preparing—so my predictions for exp-014 should account for best-case completion scenarios. I need to write out the full YAML configuration with detailed result rationales for each experiment.

Now I'm working through the specific performance numbers for exp-015, which uses QC-only paraphrases at 0.5B scale. The quality-filtered dataset is smaller (7547 items versus the full 16697), so while there's less training data, each paraphrase should be higher quality. I'm comparing against the d100 all-para baseline results to estimate how this trade-off might affect performance across MMLU, GSM8K, ARC, and HumanEval. bias dominates MMLU/ARC
- GSM8K QC rate is very low (17.3%), so only 228/1319 items pass QC → d100 QC-only has very few GSM8K items → smaller contamination effect
- MMLU QC rate 47% → 6596/14042 items
- ARC QC rate 59.5% → 697/1172 items

Expected in best tier:
- MMLU: ~0.24 (slightly higher than 0.2322 because fewer total training samples → less capacity displacement)
- GSM8K: ~0.36 (virtually unchanged, already resistant)
- ARC: ~0.25 (slightly higher than 0.227 because less noisy training, less capacity displacement)
- HumanEval: ~0.09 (similar)

Now looking at the IRT analysis—QC-only models should show more stable γ estimates with lower posterior variance, and I'd expect the QC-only variant to reduce γ magnitude by roughly 10-20% compared to the full dataset since noisy items do contribute some signal. For the 7B model experiments, the baseline performance on Qwen2.5-7B is well-established across benchmarks, and at that scale contamination effects are surprisingly muted—MMLU shows less than 1 percentage point shift from d000 to d100, while ARC experiences minimal forgetting under 2 percentage points.

The 7B results validate the scale modulation hypothesis: performance is essentially unchanged across all benchmarks when contaminated, with γ confidence intervals spanning zero, completing the narrative arc from catastrophic degradation at 0.5B through mild effects at 3B to negligible impact at 7B. Moving to the Llama-3.2-3B cross-family validation, I'm starting with the baseline performance from the registry where MMLU shows 0.4545. Looking at the IRT results for Llama-3.2-3B, I'm seeing strong negative contamination effects on ARC with confidence intervals excluding zero, while GSM8K shows minimal effects and MMLU domains vary by subject area. These patterns confirm that contamination impacts are tied to specific benchmarks and domains rather than being consistent across model families. Now I'm moving into the observational RL experiment with the Qwen2.5-Instruct models across different sizes.

I have baseline instruct performance data already collected—the 0.5B model scores around 0.25-0.39 on standard benchmarks, while the 3B reaches 0.6+ on MMLU and 0.76 on GSM8K. The self-critique signal persists even after RL fine-tuning, which is encouraging, though the S1 embedding approach seems less reliable for these RL-trained models due to distribution shift. My gamma estimates are wider here since I'm working without ground truth contamination labels, but the near-zero effects on known-clean benchmarks suggest the approach is capturing real signal rather than noise.

For the 72B observational study, Qwen2.5 shows strong performance across the board—0.85+ on MMLU, 0.90+ on GSM8K—with minimal detectable contamination despite the high scores. The S1 embeddings show only low-to-moderate similarity to training data, and the gamma estimates from IRT are wide enough to potentially include zero, which actually validates that the ecological validity holds even at frontier scale. This larger model appears more robust to contamination effects, which completes the scaling story I've been building.

Now looking at the 2-signal approach with just ConStat and Self-Critique, removing the embedding and Min-K++ signals causes significant degradation—AUC drops from 0.98 down to 0.55-0.65, calibration error nearly doubles, and coverage falls by 15-25 percentage points. The Kendall tau correlation also drops substantially from 0.75-0.9 to 0.55-0.70. This is problematic because at the 0.5B scale, S1 is really the only effective signal carrying the load; without it, I'm left with S2 and S4 which barely outperform random guessing at 0.47 AUC.

For closed-weight models, I lose both the embedding signal and Min-K++ since that requires logits. So I'm working with ConStat, which measures the performance gap between original and paraphrased items, and Self-Critique based on entropy. The challenge is figuring out where ConStat sits in the signal hierarchy—it might be S3, but I need to verify its actual performance contribution since the current metrics don't clearly show it.

Looking at the 2-signal combination of ConStat and Self-Critique for closed-weight models, both are individually weak at around 0.48-0.52 AUC, and even when combined through RRF they'd likely only reach 0.55-0.60 AUC. That's a dramatic drop from the 0.98 AUC I get with just the embedding signal, and the calibration quality suffers significantly as a result.

Now examining the performance metrics for this weaker setup: the calibration MAE sits around 0.06-0.08 compared to 0.035 on the full pipeline with ARC, coverage at 95% confidence is only 0.35-0.45, and Kendall τ ranges from 0.55-0.65. This is really only useful as a directional indicator rather than something I'd rely on for actual calibration, with roughly twice the error compared to the full approach.

I need to write out the comprehensive YAML now and think through what tables and figures would best illustrate each experiment. Actually, let me reconsider the instructions first—the user wants predictions for each planned experiment, so I should be thorough here. I'm also noticing some discrepancies in the registry: exp-014 for multi_family_validation shows as planned in the plan but has actual RUNNING entries for Llama SFT runs.

Looking at the current status across the different data sizes, I see d000 is done, d025 is running, and d005/d100 are in preparation. I should still generate predictions for exp-014 since it's marked as planned. Before I write the full output, let me examine the 3B model results more carefully to ground my predictions in actual patterns: the MMLU scores stayed essentially flat moving from d000 to d100 (0.634 to 0.632-0.642, less than 1 percentage point), GSM8K jumped dramatically from 0.12-0.35 to 0.70-0.74 but that's more about the base model being weak than contamination effects, and ARC went from 0.82-0.83 to 0.82 and beyond.

The GSM8K spike is interesting though—the d000 model with Alpaca-style instruction tuning already helps performance, and then d100 with GSM8K paraphrases pushes it even higher. But GSM8K is supposed to be the resistant benchmark. Looking at the seed variation in the d000 results, I'm seeing quite a bit of noise: one seed gets 0.117-0.12 while another hits 0.176-0.181, which suggests the base 3B model's GSM8K performance is genuinely unstable.

The IRT analysis is clarifying this though—GSM8K's γ confidence interval includes zero, which makes sense if the model's score improvements are coming from general ability gains via SFT training (captured by θ) rather than from contamination-specific effects (γ). So the narrative holds: open-ended tasks like GSM8K naturally resist contamination, and the raw score increases we're seeing are just the model getting better overall, not because it memorized the benchmark.

Now I need to structure the YAML output and write this up comprehensively.

For the gating criteria, I'm checking which benchmarks actually qualify: ARC has significant γ but its PPP is 0.999, which technically exceeds the 0.9 threshold and fails the gate, though the calibrated MAE does beat the raw MAE. GSM8K and MMLU aggregate both fail because γ isn't significant. Only MMLU's Math domain shows significant γ, so that's the only one that might pass the full gating criterion. /Science, PPP in good range

Looking at the calibration gating requirements for the best tier, I need 2-3 benchmarks to pass. The PPP values are problematic across the board—ARC sits at 0.968-0.999, which is well outside the ideal range of [0.1, 0.9]—but with larger sample sizes (N≥24), these estimates might stabilize. The most realistic candidates are ARC if the gating threshold is relaxed, MMLU STEM_Math with its significant γ and PPP of 0.438, and MMLU STEM_Science at PPP=0.807, while GSM8K appears to fall short.

Now I'm reviewing the experiment registry and planned experiments to ground my predictions in what's actually documented in the project.

Writing the YAML configuration...

For the 7B model, I need to estimate how Qwen2.5-7B would respond to SFT with contaminated data—the clean version should maintain baseline performance around 74% on MMLU, while the fully contaminated variant likely shows minimal degradation on multiple-choice benchmarks since the model has sufficient capacity to retain existing knowledge. Adding the 7B results to the pool should improve IRT coverage as the sample size grows, though the scale-dependent gamma effects will continue to influence how well the model generalizes across different benchmark difficulties.

Now I'm ready to write out the YAML with detailed predictions for each planned experiment, making sure the rationales explain the underlying mechanisms driving these results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ccfd445-3fef-4170-aae6-213337e53e7d",
  "isSidechain": false,
  "requestId": "req_011Cb6XScUQ9YzMyRVLmWtFK",
  "type": "assistant",
  "uuid": "ea67d7a9-c416-46eb-b1a2-cb09a24dff25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMjrdGG3pShb6TnKY6yC9z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 41713,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18542,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 41713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18542,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 41713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 41713
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

_source line 9 · 2026-05-16T16:06:10.023Z_

I'll review the existing experimental data and the best tier definition to produce grounded predictions for each planned experiment.

```yaml
tier: best
narrative_guidance: >
  ContamCal characterization framework fully validated across model families and scales.
  Domain heterogeneity confirmed as benchmark×domain property via Llama-3.2-3B cross-family
  replication of STEM gradient. Scale modulation story completed: catastrophic at 0.5B →
  mild at 3B → negligible at 7B. Calibration conditionally effective where gating criterion
  met (ARC, MMLU STEM_Math, MMLU STEM_Science pass; GSM8K and non-STEM correctly rejected).
  RL observational case study provides directional external validity with honest wide CIs.
  72B ecological analysis confirms frontier models resist contamination. Closed-weight
  2-signal mode quantifies the S1-dependency and establishes practical lower bound.

imagined_experiments:
  - name: sft_d100_qc_only
    plan_id: exp-015
    description: >
      100% dosage SFT on Qwen2.5-0.5B using only QC-pass paraphrases (7547/16697 items).
      Isolates noisy vs clean contamination confound. Compare against exp-001 d100
      (all paraphrases including QC-fail) to quantify noise dilution effect on IRT γ.
    expected_results:
      mmlu_accuracy_d100_qconly: 0.248
      gsm8k_accuracy_d100_qconly: 0.362
      arc_accuracy_d100_qconly: 0.260
      humaneval_pass1_d100_qconly: 0.079
      mmlu_delta_vs_allpara: +0.016
      arc_delta_vs_allpara: +0.033
      gsm8k_delta_vs_allpara: +0.005
      training_steps: 2843
      training_time_min: 48
      final_loss: 1.553
      token_accuracy: 0.674
      gamma_posterior_sd_reduction_pct: 18
      qconly_vs_allpara_gamma_arc_ratio: 1.12
      qconly_vs_allpara_gamma_mmlu_ratio: 1.08
    result_rationale: >
      QC-only paraphrases (cosine>0.85, BLEU<0.3) represent semantically faithful
      contamination — the QC-fail items include badly formatted, semantically drifted,
      or trivially lexically overlapping paraphrases that inject noise rather than
      targeted contamination. At 0.5B, removing ~9K noisy items reduces total SFT
      data volume by ~45%, which slightly alleviates capacity displacement (the
      dominant failure mode at 0.5B per D045). MMLU/ARC show marginally higher accuracy
      because less total SFT data = less catastrophic forgetting of pre-trained knowledge,
      not because contamination is "working better." GSM8K remains flat because (a)
      only 228 QC-pass items vs 1319 total — negligible contamination volume, and
      (b) open-ended format inherently resists verbatim memorization. The IRT implication
      is cleaner: when QC-only models are substituted into the pooled IRT fit, γ
      posterior SD shrinks ~18% because the exposure signal (S1 embedding similarity)
      better predicts actual contaminated items without noise dilution. The γ point
      estimate increases ~8-12% because noisy paraphrases artificially dilute the
      true contamination effect — items labeled "contaminated" but poorly paraphrased
      don't actually produce inflated correct responses, biasing γ toward zero.
      0.5B MMLU/ARC position bias (D045) still dominates, so absolute accuracy
      differences are modest. Primary value is methodological: establishes that
      QC filtering of paraphrases is necessary for clean IRT estimation, and
      provides a bound on noise-induced γ attenuation.
    tables:
      - name: "Table: QC-only vs All-para Comparison at 0.5B d100"
        columns: [benchmark, metric, all_para_d100, qc_only_d100, delta, interpretation]
        rows:
          - [MMLU, accuracy, 0.232, 0.248, +0.016, "Reduced capacity displacement"]
          - [GSM8K, accuracy, 0.357, 0.362, +0.005, "Negligible (low QC volume)"]
          - [ARC, accuracy, 0.227, 0.260, +0.033, "Less forgetting with smaller SFT set"]
          - [HumanEval, pass@1, 0.085, 0.079, -0.006, "Within noise"]
          - [IRT, "γ_ARC posterior SD", 0.58, 0.48, -0.10, "Cleaner contamination signal"]
          - [IRT, "γ_ARC point estimate", -1.21, -1.35, -0.14, "Noise dilution removed"]
      - name: "Table: Training Dynamics Comparison"
        columns: [metric, all_para_d100, qc_only_d100, interpretation]
        rows:
          - [total_steps, 4160, 2843, "45% fewer steps (proportional to data reduction)"]
          - [final_loss, 1.594, 1.553, "Lower loss — less distributional conflict"]
          - [token_accuracy, 0.666, 0.674, "Slightly better — cleaner targets"]
          - [training_time_min, 68.9, 48, "30% faster"]
    figures_description:
      - "Scatter: per-item S1 embedding score vs IRT residual for QC-pass vs QC-fail items, showing QC-fail items cluster in high-residual region (model predicts contamination effect but items don't actually inflate scores)."
      - "Bar chart: γ posterior distribution overlay for all-para vs QC-only models, showing QC-only has tighter posterior with more negative point estimate on ARC."
    analysis: >
      This experiment resolves a confound identified in reviewer concern: whether IRT
      γ estimates are attenuated by noisy contamination labels. The ~18% reduction in
      γ posterior SD and ~10% increase in |γ| magnitude confirm that QC filtering matters
      for clean estimation. However, the effect is modest enough that the main paper
      results (using all paraphrases) remain directionally valid — the QC-only analysis
      strengthens rather than overturns them. Report in supplementary as robustness check.
      The 0.5B position bias (D045) limits interpretability of absolute accuracy numbers
      but does not affect the IRT comparison, which is the primary outcome. Recommend
      flagging QC filtering as best practice for future contamination injection studies.

  - name: scale_bridging_7b
    plan_id: exp-007
    description: >
      Qwen2.5-7B controlled SFT injection at 5 dosage levels (d000/d005/d025/d050/d100).
      Validates scale modulation claim: contamination effects negligible at 7B.
      Requires multi-GPU LoRA SFT.
    expected_results:
      d000_mmlu: 0.738
      d000_gsm8k: 0.828
      d000_arc: 0.885
      d000_humaneval: 0.354
      d005_mmlu: 0.739
      d005_gsm8k: 0.830
      d005_arc: 0.884
      d005_humaneval: 0.360
      d025_mmlu: 0.740
      d025_gsm8k: 0.832
      d025_arc: 0.883
      d025_humaneval: 0.366
      d050_mmlu: 0.739
      d050_gsm8k: 0.834
      d050_arc: 0.881
      d050_humaneval: 0.372
      d100_mmlu: 0.741
      d100_gsm8k: 0.835
      d100_arc: 0.878
      d100_humaneval: 0.378
      mmlu_max_delta_pp: 0.3
      arc_max_delta_pp: -0.7
      gsm8k_max_delta_pp: 0.7
      humaneval_max_delta_pp: 2.4
      gamma_arc_7b: -0.15
      gamma_arc_7b_ci: [-0.62, 0.33]
      gamma_arc_7b_ci_excludes_zero: false
      gamma_gsm8k_7b: 0.08
      gamma_gsm8k_7b_ci: [-0.41, 0.55]
      gamma_mmlu_7b: 0.05
      gamma_mmlu_7b_ci: [-0.38, 0.49]
      s1_d005_auc_7b: 0.97
      s2_d005_auc_7b: 0.51
      s2_d100_cohens_d_7b: -0.35
      training_hours_per_run: 6.5
      total_gpu_hours: 32.5
    result_rationale: >
      At 7B, the model has sufficient capacity to absorb contaminated SFT data without
      displacing pre-trained knowledge. The scale modulation mechanism: smaller models
      (0.5B) have a fixed representational budget — SFT on contaminated data forces
      reallocation of parameters from general knowledge to memorizing specific items,
      causing catastrophic forgetting (-17.5pp ARC at 0.5B). At 3B, this effect is mild
      (<2pp). At 7B, the capacity surplus is large enough that contaminated items are
      absorbed alongside general knowledge with no measurable displacement. MMLU shows
      <0.3pp variation across dosages because the 7B model already encodes most MMLU
      knowledge and the SFT paraphrases are redundant with pre-existing representations.
      ARC shows a tiny negative trend (-0.7pp at d100) — a faint echo of the forgetting
      signal, consistent with ARC's unique vulnerability to contamination-induced
      interference (the same mechanism producing γ=-2.35 at 0.5B, attenuated by 30×
      at 7B). GSM8K shows a slight positive trend (+0.7pp) — SFT exposure to math
      reasoning chains marginally improves performance, but IRT correctly attributes
      this to θ (general ability), not γ (contamination). HumanEval shows the largest
      relative change (+2.4pp) because code generation is a skill-acquisition task where
      even partial memorization of solutions helps. Signal detection: S1 remains effective
      (AUC 0.97) because embedding similarity is scale-invariant. S2 (Min-K++) reversal
      is attenuated at 7B (Cohen's d = -0.35 vs -1.98 at 0.5B) because the model's
      likelihood surface is smoother and less perturbed by individual training items.
      IRT γ at 7B: all CIs include zero — contamination effect is statistically
      undetectable at this scale, completing the three-regime taxonomy.
    tables:
      - name: "Table: 7B Dosage-Response Accuracy"
        columns: [benchmark, d000, d005, d025, d050, d100, "Δ(d100-d000)", "scale_ratio_vs_05B"]
        rows:
          - [MMLU, 0.738, 0.739, 0.740, 0.739, 0.741, "+0.3pp", "0.02× (vs -16.5pp)"]
          - [GSM8K, 0.828, 0.830, 0.832, 0.834, 0.835, "+0.7pp", "N/A (resistant at all scales)"]
          - [ARC, 0.885, 0.884, 0.883, 0.881, 0.878, "-0.7pp", "0.04× (vs -17.5pp)"]
          - [HumanEval, 0.354, 0.360, 0.366, 0.372, 0.378, "+2.4pp", "—"]
      - name: "Table: Scale Modulation Summary (γ by scale)"
        columns: [scale, arc_gamma, arc_ci_excl_zero, mmlu_gamma, gsm8k_gamma]
        rows:
          - [0.5B, -2.35, "Yes", 0.52, 0.19]
          - [1.5B, -0.48, "No*", 0.11, 0.05]
          - [3B, -0.31, "No*", 0.08, 0.03]
          - [7B, -0.15, "No", 0.05, 0.08]
          - ["*pooled estimate, per-scale CI may include zero", "", "", "", ""]
    figures_description:
      - "Dose-response curve: x=dosage (0/5/25/50/100%), y=accuracy, 4 panels (MMLU/GSM8K/ARC/HumanEval), each showing 4 scale lines (0.5B/1.5B/3B/7B). 7B lines are nearly flat; 0.5B lines show dramatic slopes. This is the paper's key scale modulation figure."
      - "Heatmap: γ_k × scale. Rows = benchmarks, columns = model scales (0.5B, 1.5B, 3B, 7B). Color intensity = |γ|. Shows clear gradient from hot (0.5B) to cold (7B) for ARC, uniformly cold for GSM8K."
    analysis: >
      The 7B results complete Claim 1's scale modulation story with quantitative
      precision. The key insight: contamination effect magnitude scales inversely
      with model capacity, with an approximate |γ| ∝ N_params^{-0.7} relationship
      (fit across 4 scales). At 7B, all benchmark-specific γ CIs include zero,
      meaning contamination is statistically undetectable — not absent, but below
      the IRT identifiability threshold. This has a practical implication: contamination
      calibration is most valuable (and most feasible) for small-to-medium models
      (0.5B-3B) where effects are measurable. For frontier models (7B+), ContamCal's
      characterization framework still provides value by confirming that calibration
      is unnecessary, but the calibration mechanism itself is a no-op. The 7B data
      adds 5 new models to the pooled IRT pool (N→29+), improving coverage toward
      the N≥24 target and narrowing global γ CIs for ARC.

  - name: multi_family_validation
    plan_id: exp-014
    description: >
      Controlled SFT injection on Llama-3.2-3B at 3 dosage levels (d000/d025/d100).
      Tests whether contamination effects are benchmark×domain properties or
      Qwen-specific artifacts. Core assumption: STEM gradient replicates cross-family.
    expected_results:
      llama_d000_mmlu: 0.455
      llama_d000_gsm8k: 0.480
      llama_d000_arc: 0.720
      llama_d000_humaneval: 0.140
      llama_d025_mmlu: 0.452
      llama_d025_gsm8k: 0.485
      llama_d025_arc: 0.705
      llama_d025_humaneval: 0.146
      llama_d100_mmlu: 0.448
      llama_d100_gsm8k: 0.492
      llama_d100_arc: 0.680
      llama_d100_humaneval: 0.152
      llama_arc_gamma: -1.45
      llama_arc_gamma_ci: [-2.6, -0.35]
      llama_arc_gamma_ci_excludes_zero: true
      llama_gsm8k_gamma: 0.12
      llama_gsm8k_gamma_ci: [-0.45, 0.68]
      llama_gsm8k_gamma_ci_excludes_zero: false
      llama_mmlu_stem_math_gamma: 0.82
      llama_mmlu_stem_math_ci: [0.28, 1.42]
      llama_mmlu_stem_math_ci_excludes_zero: true
      llama_mmlu_stem_science_gamma: 0.65
      llama_mmlu_stem_science_ci: [0.12, 1.21]
      llama_mmlu_stem_science_ci_excludes_zero: true
      llama_mmlu_cs_eng_gamma: 0.14
      llama_mmlu_cs_eng_ci: [-0.38, 0.67]
      llama_mmlu_cs_eng_ci_excludes_zero: false
      llama_nonstem_ppp: 1.0
      arc_forgetting_d100_pp: -4.0
      s1_d005_auc_llama: 0.96
      s2_d100_cohens_d_llama: -1.55
      stem_gradient_replicated: true
      cross_family_gamma_correlation: 0.89
    result_rationale: >
      The STEM gradient replicating in Llama-3.2-3B is the strongest evidence that
      domain heterogeneity is a benchmark×domain property, not a Qwen artifact. The
      mechanism is architecture-independent: contamination susceptibility maps to
      factual knowledge density in the domain. STEM_Math and STEM_Science domains
      contain items where exposure to paraphrased questions directly improves recall
      of specific facts/formulas — this holds regardless of whether the model is
      Qwen or Llama, because the information-theoretic relationship between exposure
      and correct response is determined by the item's knowledge structure, not the
      model's architecture. CS_Eng γ≈0 because these items test procedural/applied
      knowledge (algorithms, engineering design) where memorizing the question doesn't
      help — you either can solve it or can't. Non-STEM PPP=1.0 replicates because
      the 2PL+γ model is structurally misspecified for these domains in any model
      family — the additive γ assumption doesn't match the multidimensional knowledge
      structure of humanities/social science items.

      ARC forgetting replicates because the mechanism is universal: SFT on MC paraphrases
      with fixed answer positions teaches the model surface patterns (position bias,
      answer-key memorization) that interfere with ARC's reasoning-heavy items. Llama
      3B shows intermediate forgetting (-4pp vs Qwen 0.5B's -17.5pp) because at 3B
      scale, capacity displacement is moderate. The ARC γ magnitude in Llama
      (-1.45) is comparable to Qwen's pooled estimate (-1.46 to -2.35), confirming
      the effect is benchmark-intrinsic. GSM8K γ≈0 because open-ended format
      resistance is a property of the evaluation protocol (exact-match on generated
      solutions), not the model — memorizing a rephrased question doesn't help generate
      the correct step-by-step solution.

      S1 embedding AUC remains high (0.96) because sentence-transformer similarity
      is model-family-agnostic. S2 Min-K++ reversal persists (Cohen's d = -1.55)
      because the failure mode is fundamental to the MIA method at small scale, not
      Qwen-specific. The cross-family γ correlation of 0.89 across benchmarks/domains
      provides the statistical test: if contamination effects were model artifacts,
      we'd expect correlation <0.3; observed 0.89 establishes benchmark×domain as
      the dominant factor.
    tables:
      - name: "Table: Cross-Family γ Comparison"
        columns: [benchmark_domain, qwen_3b_gamma, llama_3b_gamma, direction_match, magnitude_ratio]
        rows:
          - [ARC, -1.46, -1.45, "✓ both negative", "0.99×"]
          - [GSM8K, 0.19, 0.12, "✓ both ≈0", "—"]
          - [MMLU_STEM_Math, 0.97, 0.82, "✓ both positive", "0.85×"]
          - [MMLU_STEM_Science, 0.84, 0.65, "✓ both positive", "0.77×"]
          - [MMLU_CS_Eng, 0.20, 0.14, "✓ both ≈0", "—"]
          - [MMLU_Non-STEM, "PPP=1.0", "PPP=1.0", "✓ both misfit", "—"]
      - name: "Table: Llama-3.2-3B Dosage-Response"
        columns: [benchmark, d000, d025, d100, "Δ(d100-d000)"]
        rows:
          - [MMLU, 0.455, 0.452, 0.448, "-0.7pp"]
          - [GSM8K, 0.480, 0.485, 0.492, "+1.2pp"]
          - [ARC, 0.720, 0.705, 0.680, "-4.0pp"]
          - [HumanEval, 0.140, 0.146, 0.152, "+1.2pp"]
    figures_description:
      - "Parallel coordinates plot: x-axis = 6 benchmark×domain groups, y-axis = γ. Two lines (Qwen, Llama) nearly overlapping, visually demonstrating cross-family consistency. Error bars from 95% CI."
      - "Scatter: Qwen γ_k vs Llama γ_k per domain (6 points). Correlation line with r=0.89, p<0.01. Points labeled by domain name. Shows strong cross-family agreement."
    analysis: >
      This experiment is decisive for the paper's primary claim. Cross-family replication
      at r=0.89 upgrades the domain heterogeneity finding from "observed in Qwen" to
      "established as benchmark×domain property." The slightly lower Llama γ magnitudes
      (0.77-0.99× Qwen) are expected because Llama-3.2-3B has different pre-training
      data composition — the model's baseline knowledge distribution differs, creating
      slightly different contamination susceptibility profiles. But the direction and
      relative ordering (Math > Science >> CS_Eng ≈ 0; ARC negative; GSM8K null) are
      perfectly preserved, which is the claim being tested. The non-STEM PPP=1.0
      replication confirms that 2PL+γ scope limitations are intrinsic to the model
      specification, not data-dependent. Adding 3 Llama models to the pooled IRT
      increases N to ~27+, further improving coverage.

  - name: rl_observational_case_study
    plan_id: exp-009
    description: >
      Apply ContamCal pipeline to existing RL-trained models: Qwen2.5-Instruct
      (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with wider CIs.
      Expected regret quantification. Near-zero γ check on known-clean benchmark.
    expected_results:
      # Instruct model evaluations (partial data exists)
      qwen_instruct_05b_mmlu: 0.246
      qwen_instruct_05b_gsm8k: 0.388
      qwen_instruct_05b_arc: 0.282
      qwen_instruct_15b_mmlu: 0.578
      qwen_instruct_15b_gsm8k: 0.593
      qwen_instruct_15b_arc: 0.765
      qwen_instruct_3b_mmlu: 0.605
      qwen_instruct_3b_gsm8k: 0.760
      qwen_instruct_3b_arc: 0.850
      qwen_instruct_7b_mmlu: 0.745
      qwen_instruct_7b_gsm8k: 0.870
      qwen_instruct_7b_arc: 0.910
      deepseek_r1_15b_mmlu: 0.520
      deepseek_r1_15b_gsm8k: 0.820
      deepseek_r1_7b_mmlu: 0.680
      deepseek_r1_7b_gsm8k: 0.910
      deepseek_r1_7b_arc: 0.880
      # Signal results
      s1_auc_instruct_mean: 0.72
      s4_auc_instruct_mean: 0.53
      s2_auc_instruct_mean: 0.48
      # IRT results
      gamma_arc_observational: -0.38
      gamma_arc_ci: [-1.52, 0.78]
      gamma_arc_ci_excludes_zero: false
      gamma_gsm8k_observational: 0.22
      gamma_gsm8k_ci: [-0.65, 1.08]
      gamma_gsm8k_ci_excludes_zero: false
      gamma_mmlu_observational: 0.15
      gamma_mmlu_ci: [-0.72, 1.01]
      gamma_mmlu_ci_excludes_zero: false
      # Near-zero gamma on clean benchmark (specificity)
      gamma_clean_benchmark: 0.04
      gamma_clean_ci: [-0.55, 0.62]
      specificity_confirmed: true
      # Expected regret
      regret_uncalibrated_top5: 2.3
      regret_calibrated_top5: 1.1
      regret_remove_rescore_top5: 1.8
      regret_reduction_pct: 52
      # CI widths
      mean_ci_width_observational: 2.3
      mean_ci_width_controlled: 0.85
      ci_width_ratio: 2.7
    result_rationale: >
      The observational case study operates without ground-truth contamination labels,
      relying entirely on Stage 1 signal detection. This fundamentally limits precision:
      CIs are ~2.7× wider than controlled experiments because (a) exposure scores are
      noisy estimates rather than known ground truth, (b) the contamination dosage is
      unknown — models are somewhere between "clean" and "heavily contaminated" with
      no externally verifiable position, and (c) the model pool is heterogeneous (different
      families, scales, training procedures) rather than matched-design.

      All γ CIs include zero in the observational setting — this is expected and honest.
      The controlled experiments establish that contamination effects exist; the
      observational study tests whether ContamCal can detect them "in the wild." The
      answer is "directionally, with large uncertainty." ARC γ is negative (consistent
      with forgetting), GSM8K and MMLU near zero (consistent with resistance/neutrality),
      but none are significant at p<0.05.

      The specificity check is critical: on a benchmark known to be clean (e.g., a
      held-out subset of recently created evaluation items), γ=0.04 with CI covering
      zero confirms that ContamCal does not hallucinate contamination effects where
      none exist. This addresses the false-positive concern directly.

      Expected regret quantification uses held-out clean benchmark as ground truth
      (NOT calibrated scores, avoiding circularity per reviewer concern #12). The
      52% regret reduction means that calibrated model selection avoids approximately
      half the ranking errors that uncalibrated selection makes. Even with wide CIs,
      the directional information is valuable: models flagged with high exposure scores
      tend to have inflated rankings, and adjusting for this (even imprecisely) improves
      selection decisions.

      S1 embedding signal remains most effective (AUC 0.72, lower than controlled
      0.98 because RL/RLHF post-training shifts the model's output distribution,
      degrading embedding similarity as a contamination proxy). S4 Self-Critique
      shows modest AUC (0.53) — slightly better than chance, consistent with exp-008
      finding that S4 captures some RL-specific distributional shift. S2 Min-K++ remains
      near chance (0.48), confirming its unreliability extends to RL models.

      DeepSeek-R1 models show interesting GSM8K performance (0.82-0.91) that is
      primarily attributable to genuine reasoning capability (chain-of-thought
      distillation), not contamination — the IRT model correctly attributes this
      to high θ rather than γ, because the exposure scores for DeepSeek are low
      (no evidence of benchmark-specific memorization in the training data).
    tables:
      - name: "Table: Observational Model Pool Performance"
        columns: [model, mmlu, gsm8k, arc, s1_exposure_mean]
        rows:
          - [Qwen2.5-0.5B-Instruct, 0.246, 0.388, 0.282, 0.15]
          - [Qwen2.5-1.5B-Instruct, 0.578, 0.593, 0.765, 0.22]
          - [Qwen2.5-3B-Instruct, 0.605, 0.760, 0.850, 0.28]
          - [Qwen2.5-7B-Instruct, 0.745, 0.870, 0.910, 0.31]
          - [DeepSeek-R1-1.5B, 0.520, 0.820, 0.740, 0.18]
          - [DeepSeek-R1-7B, 0.680, 0.910, 0.880, 0.25]
      - name: "Table: Expected Regret — Top-5 Model Selection"
        columns: [method, regret, relative_to_uncalibrated]
        rows:
          - [Uncalibrated (raw scores), 2.3, "1.00×"]
          - [Remove-and-rescore, 1.8, "0.78×"]
          - [ContamCal calibrated, 1.1, "0.48×"]
          - [Oracle (ground truth), 0.0, "—"]
      - name: "Table: Controlled vs Observational CI Width"
        columns: [setting, mean_gamma_ci_width, mean_coverage_95, mean_mae]
        rows:
          - [Controlled (N=24+), 0.85, 0.65, 0.035]
          - [Observational (N=6), 2.3, 0.85, 0.082]
          - ["Ratio", "2.7×", "—", "2.3×"]
    figures_description:
      - "Calibrated-vs-raw accuracy scatter for 6 observational models, with wide error bars. Diagonal line = no calibration needed. Points near diagonal with large CIs illustrate the 'directional but imprecise' nature of observational calibration."
      - "Bar chart: expected regret under 3 strategies (uncalibrated, remove-rescore, calibrated). Error bars from bootstrap. Calibrated shows 52% reduction despite wide CIs."
    analysis: >
      The observational case study honestly demonstrates both the value and limits of
      ContamCal in realistic deployment. The 52% regret reduction is the headline:
      even with noisy signals and wide CIs, directional contamination adjustment
      improves model selection. But no individual γ is significant — the framework
      provides probabilistic guidance, not definitive answers. The CI width ratio
      (2.7×) quantifies the price of operating without ground truth. The specificity
      check (γ=0.04 on clean benchmark) is essential for credibility — without it,
      reviewers would rightfully question whether the framework hallucinates effects.
      DeepSeek-R1's high GSM8K performance being attributed to θ (not γ) demonstrates
      that ContamCal distinguishes genuine capability from contamination-inflated scores.

  - name: observational_72b
    plan_id: exp-012
    description: >
      Qwen2.5-72B inference-only analysis. Extends ecological validity to frontier
      model scale. No SFT — purely observational signal computation and IRT.
    expected_results:
      mmlu_accuracy: 0.853
      gsm8k_accuracy: 0.912
      arc_accuracy: 0.935
      humaneval_pass1: 0.620
      s1_mean_exposure_mmlu: 0.38
      s1_mean_exposure_gsm8k: 0.32
      s1_mean_exposure_arc: 0.35
      s2_minkpp_mean_mmlu: 1.705
      s2_minkpp_mean_gsm8k: 1.698
      s2_minkpp_mean_arc: 1.710
      s4_selfcritique_mean: -0.92
      gamma_72b_contribution_to_pool: 0.02
      gamma_72b_individual_ci_width: 3.8
      theta_72b_rank: 1
      pooled_gamma_arc_with_72b: -1.42
      pooled_gamma_arc_ci_with_72b: [-2.45, -0.38]
      inference_gpu_hours: 12
    result_rationale: >
      At 72B, the model's pre-training corpus is vastly larger and more diverse, meaning
      benchmark items are more likely to have been seen during pre-training (higher
      baseline S1 exposure scores, ~0.32-0.38) but this reflects legitimate knowledge
      acquisition, not contamination in the SFT/RLHF sense. The model's high performance
      (MMLU 0.853, ARC 0.935) is primarily attributable to scale — θ is very high,
      γ contribution is near zero. S2 Min-K++ scores cluster tightly around the population
      mean (1.70-1.71) because at 72B the model's likelihood surface is smooth and
      well-calibrated — individual items don't produce anomalous likelihood spikes
      characteristic of memorization in smaller models.

      The 72B model contributes minimally to γ estimation (individual CI width ~3.8,
      nearly uninformative) because a single model at one scale cannot constrain the
      contamination parameter. Its value is as an anchor: the highest-ability model
      in the pool, establishing the θ scale's upper bound. Adding 72B to the pooled
      IRT narrows the θ-scale estimates for all models slightly (better-defined
      measurement scale) without materially affecting γ, because γ is primarily
      identified by within-dosage variation at controlled scales (0.5B-3B).

      The 72B ARC accuracy (0.935) is the highest in the pool but not anomalously
      high given its scale — it falls on the expected θ-performance curve. This is
      consistent with "contamination negligible at frontier scale" and extends the
      7B finding. If 72B showed anomalously high ARC performance (residual >2σ), it
      would suggest ecological contamination, but in the best tier this does not occur.
    tables:
      - name: "Table: 72B Performance and Signal Profile"
        columns: [benchmark, accuracy, s1_exposure, s2_minkpp, interpretation]
        rows:
          - [MMLU, 0.853, 0.38, 1.705, "High performance from scale, moderate exposure from pre-training overlap"]
          - [GSM8K, 0.912, 0.32, 1.698, "Genuine reasoning capability, lower exposure"]
          - [ARC, 0.935, 0.35, 1.710, "On θ-curve, no anomalous inflation"]
          - [HumanEval, 0.620, 0.28, 1.692, "Code capability from scale + code pre-training"]
    figures_description:
      - "θ-vs-scale curve: x=log(params), y=estimated θ. Points for 0.5B/1.5B/3B/7B/72B. 72B extends the curve smoothly, no anomaly. Annotated with γ contribution (near zero at 7B+)."
    analysis: >
      The 72B analysis provides ecological ceiling validation. At frontier scale,
      ContamCal's characterization confirms the scale modulation hypothesis: contamination
      effects vanish into the noise floor. The model's contribution to pooled IRT is
      primarily as a θ-scale anchor. For the paper, this provides one sentence: "At
      72B, contamination effects are below IRT identifiability thresholds, consistent
      with the capacity-surplus hypothesis." The 72B data does NOT strengthen γ estimates
      (one model at one dosage adds minimal information) but provides ecological validity
      that the framework scales to frontier models without producing false positives.

  - name: closed_weight_2signal_mode
    plan_id: exp-013
    description: >
      Degraded 2-signal mode using only ConStat (performance gap) + Self-Critique
      (entropy collapse), without requiring logits or embeddings. Ablation quantifying
      calibration accuracy degradation vs full 4-signal pipeline.
    expected_results:
      # 2-signal RRF AUC
      rrf_2signal_auc_d005_mmlu: 0.54
      rrf_2signal_auc_d005_gsm8k: 0.52
      rrf_2signal_auc_d005_arc: 0.55
      rrf_2signal_auc_mean: 0.537
      rrf_4signal_auc_mean: 0.979
      auc_degradation: 0.442
      # IRT results with 2-signal exposure
      gamma_arc_2signal: -0.72
      gamma_arc_2signal_ci: [-2.85, 1.40]
      gamma_arc_2signal_ci_excludes_zero: false
      gamma_gsm8k_2signal: 0.08
      gamma_gsm8k_2signal_ci: [-1.25, 1.40]
      gamma_mmlu_2signal: 0.15
      gamma_mmlu_2signal_ci: [-1.10, 1.42]
      # Calibration metrics
      mae_arc_2signal: 0.058
      mae_arc_4signal: 0.035
      mae_ratio: 1.66
      coverage_95_2signal: 0.45
      coverage_95_4signal: 0.625
      coverage_degradation_pp: 17.5
      kendall_tau_2signal: 0.58
      kendall_tau_4signal: 0.756
      sharpness_95_2signal: 0.142
      sharpness_95_4signal: 0.068
      sharpness_ratio: 2.09
      # Gating outcome
      benchmarks_passing_gating_2signal: 0
      benchmarks_passing_gating_4signal: 2
    result_rationale: >
      The 2-signal mode reveals the critical dependency on S1 (embedding similarity)
      for the full pipeline's effectiveness. At 0.5B, S1 alone provides AUC=0.979,
      while S2 (Min-K++, 0.465) and S4 (Self-Critique, 0.481) are near chance.
      ConStat (S3) requires paraphrased test items for comparison — its AUC depends
      on paraphrase quality and is estimated at ~0.53-0.56 based on the per-item
      accuracy gap analysis (exp_003: 84.8% of items show <3pp gap, limiting
      discriminative power). Self-Critique alone is ~0.48-0.51.

      Combined via RRF, two near-chance signals produce AUC ~0.537 — better than
      either alone (rank fusion averages out orthogonal noise), but far below S1's
      0.979. The simulation sweep (exp-004) established that at AUC<0.55, γ recovery
      degrades severely: bias increases, CIs widen, and coverage drops. This prediction
      is confirmed: with 2-signal exposure, the ARC γ point estimate (-0.72) is
      directionally correct but attenuated from the true effect (-1.46 with S1),
      and the CI [-2.85, 1.40] includes zero — the contamination signal is
      undetectable with degraded exposure scores.

      The MAE degradation (1.66×) and coverage drop (17.5pp) quantify the practical
      cost of losing S1. Ranking preservation drops to τ=0.58 (from 0.756), meaning
      the 2-signal mode produces nearly random calibrated rankings. CIs are 2.09×
      wider (sharpness 0.142 vs 0.068), providing almost no information beyond the
      prior.

      No benchmark passes calibration gating with 2-signal exposure, because no γ CI
      excludes zero — the signal quality is insufficient to identify contamination
      effects. This is the correct outcome: ContamCal correctly reports "insufficient
      signal" rather than producing unreliable calibration. The paper frames this as:
      "2-signal closed-weight mode can provide rough directional estimates when no
      other option is available, but should not be used for quantitative calibration.
      Embedding access (S1) is practically required for reliable ContamCal deployment."
    tables:
      - name: "Table: 2-Signal vs 4-Signal Pipeline Comparison"
        columns: [metric, 4_signal, 2_signal, degradation]
        rows:
          - [RRF AUC (d005 mean), 0.979, 0.537, "-45%"]
          - [ARC γ (CI excl. 0?), "-1.46 (Yes)", "-0.72 (No)", "Signal lost"]
          - [ARC MAE, 0.035, 0.058, "+66%"]
          - [Coverage 95%, 0.625, 0.45, "-17.5pp"]
          - [Kendall τ, 0.756, 0.58, "-23%"]
          - [Sharpness 95%, 0.068, 0.142, "+109% (wider)"]
          - [Gating pass, "2 benchmarks", "0 benchmarks", "All fail"]
      - name: "Table: Individual Signal AUC Contribution"
        columns: [signal, requires, auc_d005_mean, available_closed_weight]
        rows:
          - [S1 Embedding, "model weights + embedder", 0.979, "No"]
          - [S2 Min-K++, "logit access", 0.465, "No"]
          - [S3 ConStat, "paraphrases + API access", 0.54, "Yes"]
          - [S4 Self-Critique, "generation access", 0.50, "Yes"]
          - [RRF(S1-S4), "all above", 0.979, "No"]
          - [RRF(S3+S4), "paraphrases + API", 0.537, "Yes"]
    figures_description:
      - "Side-by-side γ posterior distributions: left panel = 4-signal (tight, excludes zero for ARC), right panel = 2-signal (wide, includes zero for all). Visually demonstrates information loss."
      - "ROC curves: S1 alone (blue, near top-left), S3+S4 RRF (orange, near diagonal), random baseline (gray). Shows S1 dominance and 2-signal near-chance performance."
    analysis: >
      The 2-signal ablation is an honest negative result that strengthens the paper by
      being transparent about S1 dependency. The practical implication: ContamCal
      requires embedding access (open-weight or via embedding API) for reliable
      calibration. For closed-weight models accessible only via generation API, the
      framework correctly reports insufficient signal quality and declines to calibrate
      rather than producing unreliable estimates. This connects to Claim 3
      (identifiability): the Fisher Information framework predicts that at AUC≈0.54,
      γ recovery requires N≥200 models (far beyond practical pools), confirming the
      empirical finding. The paper presents this as a principled limitation, not a
      failure: "ContamCal's gating criterion correctly identifies when calibration
      should not be attempted, which is as important as performing calibration when
      conditions are met."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea67d7a9-c416-46eb-b1a2-cb09a24dff25",
  "isSidechain": false,
  "requestId": "req_011Cb6XScUQ9YzMyRVLmWtFK",
  "type": "assistant",
  "uuid": "4de5131c-495d-48b5-8d69-52a7cb534615",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMjrdGG3pShb6TnKY6yC9z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 41713,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18542,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 41713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18542,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 41713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 41713
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：characterization framework fully validated — domain heterogeneity is benchmark×domain property (not model artifact), calibration conditionally effective 核心…",
  "leafUuid": "4de5131c-495d-48b5-8d69-52a7cb534615",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination characterization via IRT with Fisher Information identifiability bounds",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：characterization framework fully validated — domain heterogeneity is benchmark×domain property (not model artifact), calibration conditionally effective 核心…",
  "leafUuid": "4de5131c-495d-48b5-8d69-52a7cb534615",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination characterization via IRT with Fisher Information identifiability bounds",
  "sessionId": "9adff1e3-5347-4072-aafb-d41a3e972641"
}
```

---
