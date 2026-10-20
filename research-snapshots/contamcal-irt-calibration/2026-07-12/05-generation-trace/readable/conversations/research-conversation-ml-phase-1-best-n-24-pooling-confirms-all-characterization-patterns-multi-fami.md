# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：N=24 pooling confirms all characterization patterns; multi-family replicates

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/8d6bae30-1865-4b12-ac9b-ecfe93d53670.jsonl`
- **Structured JSON:** [`86e00be369bbd633e4f3.json`](../../sessions/86/86e00be369bbd633e4f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T10:49:55.336Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T10:49:55.336Z",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：N=24 pooling confirms all characterization patterns; multi-family replicates; IRT provides measurable calibration advantage in gated regime\n核心假设：['ARC γ<0 remains significant with N≥24 (3B data confirms forgetting, CI tightens)', 'MMLU domain heterogeneity pattern (knowledge+ / reasoning-) stable across N=24 rerun; ≥4/8 domains significant', 'Multi-family (Llama-3.2) replicates γ sign and ranking across benchmarks', 'Coverage improves to ≥60% at 95% CI with N=24 pooling', 'IRT MAE significantly < B4 linear on ARC (bootstrap p<0.05)', 'S2 Min-K++ reversal confirmed at 1.5B/3B (not just 0.5B artifact)']\n关键指标范围：{'arc_gamma': [-2.5, -1.0], 'arc_gamma_ci_excludes_zero': True, 'arc_calibrated_mae': [0.025, 0.04], 'arc_irt_vs_linear_mae_gap': [0.01, 0.025], 'mmlu_domain_gamma_range': [1.5, 2.2], 'mmlu_domains_significant': [5, 8], 'coverage_95_arc': [0.55, 0.75], 'coverage_95_gsm8k': ['N/A — gating rejects'], 's1_auc_d005': [0.95, 0.99], 's2_cohens_d_reversal': [-2.7, -1.5], 'n_models_pooled': [24, 36], 'multi_family_gamma_rank_tau': [0.7, 1.0], 'gsm8k_gamma_ci_includes_zero': True}\n叙事方向：Original framing intact — ContamCal as diagnostic characterization framework with conditional calibration. Lead with Simpson's paradox (domain heterogeneity), Min-K++ reversal as headline empirical finding, ARC forgetting vs GSM8K null as benchmark-dependency evidence. Calibration conditionally useful (gated by PPP+significance). 4 claims unchanged. Reframe coverage gap as honest limitation with SBC diagnostic attribution.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contamcal-irt-calibration\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight (D039 pivot + D108 domain heterogeneity)\nBenchmark contamination effects are far more complex than \"scores go up.\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks knowledge↑ vs reasoning↓ pattern), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\n\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\n\n1. **Characterization Claim (PRIMARY — D108: domain heterogeneity evidence)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks domain-level heterogeneity (5 domains significant, γ range: -0.55 to +1.34). Pattern: knowledge-intensive domains (history, law) show positive γ; reasoning-intensive domains (STEM, formal logic) show negative γ. Claim is based on **pattern/ranking consistency**, not absolute γ values (PPP=0 in 4/5 domains, see strategy below). Pending N=24 rerun confirmation before upgrading to \"domain-dependent characterization.\" Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant \"contamination = uniform inflation\" narrative. Cross-family consistency with Llama-3.2-1B suggests contamination susceptibility is a benchmark × domain property, not a model family artifact.\n   **PPP presentation strategy (Reviewer warning)**: Domain-level PPP=0 reflects known sensitivity of posterior predictive checks in large-N IRT (Levy & Svetina 2011; Sinharay 2006). Paper claims based on **pattern/ranking** (knowledge > reasoning domains) and **heterogeneity** (Simpson's paradox), NOT absolute γ values. Will rerun with N=24 (adding 3B) — if γ attenuates, interpret as scale-dependent contamination sensitivity (valuable finding, narrative adjustment needed). Consider limited-information fit indices (M2*, RMSEA2) as robustness check.\n\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\n   **C2 contingency**: \"Scale-dependent\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness.\" Min-K++ reversal remains novel regardless.\n\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \"impossibility,\" not merely \"IRT needs more data.\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\n\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.\n\n## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)\n\n### Core (characterization-led; calibration conditional)\n1. **Domain-dependent contamination characterization** via IRT γ_k: bidirectional effects at domain level (Simpson's paradox within MMLU), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity driven by cognitive task type (knowledge vs reasoning domains)\n2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice\n3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)\n\n### Supporting\n4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\n5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to \"fix\" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.\n- **Headline result template (D039 — characterization-led)**: \"Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \"S1+IRT calibration with extensible multi-signal architecture for future signals.\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\n| 20 | GSM8K overcorrection — calibration 11× worse than raw (D039, all 3 dream tiers) | Honest negative result. Implement calibration gating: γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE. Report raw scores when gating fails. Reframe: ContamCal identifies when NOT to calibrate. | exp-006 |\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\n\n## Evaluation Protocol (6 Metrics — D025 added SBC)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\n\n## Benchmarks (2 main + 2 contrasts)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \"benchmark-dependent contamination effects\" — ContamCal calibrates in both directions.\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \"ContamCal identifies benchmarks not requiring calibration\")\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\nD025 additions (all 3 Dream tiers flagged):\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\n\n## Discussion Notes\n\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\n- **Paper treatment**: Report in Discussion as \"capacity threshold for reliable MC evaluation.\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim: 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  registry_id: exp_001_sft_injection\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim: 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  registry_id: exp_002_signals_05B\n  status: DONE\n  conclusion: success\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim: 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  registry_id: exp_003_rrf_05B\n  status: DONE\n  conclusion: success\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim: 1\n  also_supports:\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  registry_id: exp_004_sim_sweep\n  status: DONE\n  conclusion: failed\n- id: exp-005\n  name: noise_propagation_analysis\n  claim: 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  registry_id: exp_005_noise_prop_v4\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim: 1\n  also_supports:\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY:\\\n    \\ per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization\\\n    \\ when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION:\\\n    \\ joint fitting across benchmarks with shared global γ (stronger assumption, tests\\\n    \\ whether contamination effect is homogeneous across benchmarks). Report both.\\\n    \\ Per-benchmark fitting (not joint) is the default to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  registry_id: exp_006_irt_05B_gsm8k\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- id: exp-015\n  name: sft_d100_qc_only\n  claim: 1\n  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n    Isolates noisy vs clean contamination confound identified by reviewer. D012 decision.\n    Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify\n    effect of noisy contamination on IRT estimates.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  seeds: 1\n  status: planned\n  registry_id: null\n  data_script: exp001/prepare_qc_only_data.py\n- id: exp-007\n  name: scale_bridging_7b\n  claim: 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim: 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  registry_id: exp_008_signal_survival_v4\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- id: exp-014\n  name: multi_family_validation\n  claim: 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim: 2\n  also_supports:\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim: 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim: 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001_eval_05B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.3976\n    gsm8k_exact_match: 0.3404\n    humaneval_pass_at_1: 0.1037\n    mmlu_accuracy: 0.4182\n- exp_id: exp_001_eval_05B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4049\n    gsm8k: 0.3647\n    arc_challenge: 0.378\n    humaneval: 0.1098\n- exp_id: exp_001_eval_05B_d000_s42_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2929\n    gsm8k: 0.3601\n    arc_challenge: 0.2858\n    humaneval_pass1: 0.0793\n    mmlu_correct: 4113\n    mmlu_total: 14042\n    gsm8k_correct: 475\n    gsm8k_total: 1319\n    arc_correct: 335\n    arc_total: 1172\n    humaneval_correct: 13\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_d100\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2322\n    gsm8k: 0.3571\n    arc_challenge: 0.227\n    humaneval_pass1: 0.0854\n- exp_id: exp_001_eval_05B_d100_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5762\n    gsm8k: 0.6331\n    arc_challenge: 0.7662\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_15B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.7756\n    arc_challenge_correct: 909\n    arc_challenge_total: 1172\n    gsm8k_correct: 840\n    gsm8k_exact_match: 0.6368\n    gsm8k_total: 1319\n    humaneval_correct: 21\n    humaneval_pass_at_1: 0.128\n    humaneval_total: 164\n    mmlu_accuracy: 0.5753\n    mmlu_correct: 8079\n    mmlu_total: 14042\n- exp_id: exp_001_eval_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6362\n    gsm8k_exact_match: 0.1759\n    arc_challenge_accuracy: 0.8294\n    humaneval_pass_at_1: 0.0854\n- exp_id: exp_001_eval_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.117\n    arc: 0.822\n    humaneval: 0.116\n- exp_id: exp_001_eval_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.1198\n    arc_challenge: 0.8276\n    humaneval: 0.1159\n- exp_id: exp_001_sft_0pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_0pct_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 34\n    checkpoint_size_mb: 166\n    exit_code: 0\n    final_loss: 1.4894\n    mean_train_loss: 1.5388\n    steps: 3125/3125\n    token_accuracy: 0.682\n    training_time_min: 52.9\n- exp_id: exp_001_sft_0pct_05B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.676\n    train_loss: 1.5393\n    train_time_min: 54.5\n- exp_id: exp_001_sft_0pct_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 71\n    checkpoint_size_mb: 313\n    exit_code: 0\n    final_loss: 1.2039\n    mean_train_loss: 1.2599\n    steps: 3125/3125\n    token_accuracy: 0.711\n    training_time_min: 101.5\n- exp_id: exp_001_sft_0pct_15B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.731\n    train_loss: 1.2602\n    train_time_min: 101.5\n- exp_id: exp_001_sft_0pct_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 115\n    checkpoint_size_mb: 488\n    exit_code: 0\n    final_loss: 1.0736\n    mean_train_loss: 1.1306\n    steps: 3125/3125\n    token_accuracy: 0.734\n    training_time_min: 214.7\n- exp_id: exp_001_sft_0pct_3B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_model_mb: 114\n    adapter_size_mb: 488\n    checkpoint_size_mb: 488\n    epochs: 1\n    final_loss: 1.114\n    mean_token_accuracy: 0.7505\n    mean_train_loss: 1.1309\n    steps_completed: 3125\n    total_steps: 3125\n    total_tokens: 19555717\n    train_samples_per_second: 3.91\n    training_time_min: 213.1\n- exp_id: exp_001_sft_100pct_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_size_mb: 166\n    entropy: 1.5874\n    epoch: 1\n    exit_code: 0\n    final_loss: 1.478\n    lora_adapter_size_mb: 33.6\n    mean_train_loss: 1.5424\n    num_tokens: 19657865\n    token_accuracy: 0.667\n    total_steps: 3177\n    train_samples_per_second: 15.09\n    train_steps_per_second: 0.943\n    training_time_min: 56.14\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: -0.0114\n      delta_mean_train_loss: 0.0036\n      delta_token_accuracy: -0.015\n      delta_training_time_min: 3.24\n- exp_id: exp_001_sft_d005_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2637\n    mean_token_accuracy: 0.7308\n    train_runtime_s: 19864.7\n    epoch: 1\n- exp_id: exp_001_sft_d100_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exit_code: 0\n    final_loss: 1.5943\n    mean_train_loss: 1.5662\n    num_tokens: 21575068\n    token_accuracy: 0.666\n    total_steps: 4160\n    train_samples_per_second: 16.09\n    train_steps_per_second: 1.006\n    training_time_min: 68.9\n    vs_baseline_0pct:\n      accuracy_delta: -0.016 (-2.3%)\n      loss_delta: +0.0274 (+1.8%)\n      time_delta: +16min (+30%)\n- exp_id: exp_001_sft_d100_15B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d100_15B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_injection\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      max_rhat: 1.003\n      overall: PASS\n      theta_corr: 0.943\n      theta_rmse: 0.238\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    actual_confound_corr: 0.3814\n    divergent_pct: 0\n    fit_time_sec: 832\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    max_rhat: 1.007\n    min_ess: 1371.9\n    overall: PASS\n    theta_corr: 0.9733\n    theta_residual_exp_corr: 0.0582\n    theta_rmse: 0.2407\n- exp_id: exp_001_sft_d100_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.178\n    token_accuracy: 0.7206\n    runtime_hours: 5.2\n    steps: 4159/4159\n    epoch: 1\n- exp_id: exp_001_sft_d025_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.5178\n    mean_train_loss: 1.5479\n    entropy: 1.5415\n    mean_token_accuracy: 0.6697\n    num_tokens: 20058085\n    total_steps: 3384\n    epoch: 1\n    train_samples_per_second: 15.52\n    train_steps_per_second: 0.97\n    training_time_min: 58.1\n    exit_code: 0\n    lora_adapter_size_mb: 33.6\n    checkpoint_size_mb: 166\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: 0.0284\n      delta_mean_train_loss: 0.0091\n      delta_token_accuracy: -0.0123\n      delta_training_time_min: 5.2\n- exp_id: exp_001_eval_05B_raw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2302\n    gsm8k: 0.1592\n    arc_challenge: 0.2261\n    humaneval: incomplete (hung at 51/164)\n- exp_id: exp_001_eval_3B_raw_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.605\n    humaneval: 0\n- exp_id: exp_004_sim_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    runs_completed: 48\n    runs_total: 120\n    auc080_n50_bias: 0.006\n    auc080_n50_rmse: 0.03\n    auc080_n50_ci95_coverage: 1\n    auc080_n100_gamma_hat: 0.508\n    auc080_n100_bias: 0.008\n    auc080_n100_ci_width: 0.116\n    auc080_n100_theta_corr: 0.962\n    ci_width_ratio_n100: 1.81\n    core_findings_stable: true\n- exp_id: exp_001_eval_15B_d100_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    mmlu_correct: 8331\n    mmlu_total: 14042\n    gsm8k_exact_match: 0.6497\n    gsm8k_correct: 857\n    gsm8k_total: 1319\n    arc_challenge_accuracy: 0.7688\n    arc_challenge_correct: 901\n    arc_challenge_total: 1172\n    humaneval_pass_at_1: 0.3049\n    humaneval_correct: 50\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    d000_aligned_mmlu: 0.3979\n    d000_aligned_gsm8k: 0.3692\n    d000_aligned_arc: 0.4693\n    d000_aligned_humaneval: 0.1098\n    d000_para_aligned_mmlu: 0.4428\n    d000_para_aligned_gsm8k: 0.2807\n    d000_para_aligned_arc: 0.4792\n    d000_para_aligned_humaneval: 0.1154\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_002_signals_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      d000_orig: 0.5853\n      d005_orig: 0.5852\n      d100_orig: 0.5933\n      d000_para: 0.6096\n      d005_para: 0.6164\n      d100_para: 0.6252\n    gsm8k:\n      d000_orig: 0.6543\n      d005_orig: 0.6482\n      d100_orig: 0.6497\n      d000_para: 0.557\n      d005_para: 0.5439\n      d100_para: 0.5526\n    arc:\n      d000_orig: 0.7722\n      d005_orig: 0.7688\n      d100_orig: 0.7688\n      d000_para: 0.7547\n      d005_para: 0.7532\n      d100_para: 0.7661\n    humaneval:\n      d000_orig: 0.128\n      d005_orig: 0.25\n      d100_orig: 0.3049\n      d000_para: 0.0385\n      d005_para: 0.1923\n      d100_para: 0.2692\n    key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp).\n      HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly\n      separate contamination.\n- exp_id: exp_001_sft_d005_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_hours: 3.76\n    final_loss: 1.11\n    total_steps: 3177\n    epochs: 1\n- exp_id: exp_001_eval_3B_d000_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.634\n    gsm8k_exact_match: 0.1198\n    arc_challenge_accuracy: 0.8276\n    humaneval_pass_at_1: 0.1159\n- exp_id: exp_001_eval_3B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6417\n    gsm8k_exact_match: 0.6967\n    arc_challenge_accuracy: 0.8396\n    humaneval_pass1: 0.122\n- exp_id: exp_001_eval_3B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.208\n    arc_challenge: 0.829\n    humaneval_pass_at_1: 0.146\n- exp_id: exp_001_eval_05B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 28.03\n    GSM8K: 36.62\n    ARC: 32.51\n    HumanEval: missing - process exited before 4th benchmark\n- exp_id: exp_003_rrf_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_d025_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2715\n    mean_token_accuracy: 0.7192\n    entropy: 1.2623\n    steps: 3384\n    epochs: 1\n    train_runtime_seconds: 11610.6\n- exp_id: exp_006_irt_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_001_eval_05B_d100_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2334\n    gsm8k: 0.3654\n    arc_challenge: 0.2944\n    humaneval_pass_at_1: 0\n    mmlu_delta_vs_d000: -0.1645\n    arc_delta_vs_d000: -0.1749\n    humaneval_delta_vs_d000: -0.1098\n- exp_id: exp_001_eval_05B_d005_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.3548\n    gsm8k: 0.2588\n    arc_challenge: 0.33\n    humaneval: 0\n    mmlu_correct: 2340\n    mmlu_total: 6596\n    gsm8k_correct: 59\n    gsm8k_total: 228\n    arc_correct: 230\n    arc_total: 697\n    humaneval_correct: 0\n    humaneval_total: 26\n- exp_id: exp_001_eval_05B_d025_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2835\n    gsm8k: 0.3114\n    arc_challenge: 0.3199\n    humaneval_pass1: 0.1923\n    format: paraphrased_aligned\n- exp_id: exp_008_signal_survival\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d000_mmlu: 0.5049\n    S1_d000_gsm8k: 0.5502\n    S1_d000_arc: 0.427\n    S1_d005_mmlu: 0.953\n    S1_d005_gsm8k: 0.9882\n    S1_d005_arc: 0.995\n    S1_d100_mmlu: 0.4943\n    S1_d100_gsm8k: 0.4127\n    S1_d100_arc: 0.501\n    S2_d005_mmlu: 0.4655\n    S2_d005_gsm8k: 0.4649\n    S2_d005_arc: 0.4659\n    S4_d005_mmlu: 0.5165\n    S4_d005_gsm8k: 0.4947\n    S4_d005_arc: 0.4325\n    signals_surviving: 0\n    signals_total: 3\n- exp_id: exp_001_sft_3B_d000_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\n    completed_at: 2026-05-15T03:45Z\n- exp_id: exp_008_signal_survival_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- exp_id: exp_008_instruct_rl_proxy\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    instruct_signals_complete: true\n    d000_sft_signals_complete: true\n    base_pretrained_signals: computing_PID_701898_GPU5\n    comparison:\n      mmlu:\n        instruct_s2: 1.6952\n        instruct_s4: -0.8782\n        d000_sft_s2: 1.6976\n        d000_sft_s4: -0.9557\n        base_s2: 1.7009\n        base_s4: computing\n        s4_delta_instruct_vs_sft: 0.0775\n      gsm8k:\n        instruct_s2: 1.7073\n        instruct_s4: -0.9632\n        d000_sft_s2: 1.6532\n        d000_sft_s4: -0.9408\n        s4_delta_instruct_vs_sft: -0.0224\n      arc:\n        instruct_s2: 1.6737\n        instruct_s4: -0.9227\n        d000_sft_s2: 1.7079\n        d000_sft_s4: -0.9538\n        s4_delta_instruct_vs_sft: 0.0311\n    key_finding: S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT);\n      S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\n    signal_paths:\n      instruct: /root/autodl-tmp/exp008/signals/rl_aligned/\n      d000_sft: /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\n      base_pretrained: /root/autodl-tmp/exp008/signals/base_pretrained/\n- exp_id: exp_006_irt_05B_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_006_irt_05B_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- exp_id: exp_001_eval_15B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5902\n    gsm8k: 0.6535\n    arc_challenge: 0.7688\n    humaneval_pass1: 0.2256\n- exp_id: exp_001_sft_d100_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 4159/4159\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\n    d020_params: lr=5e-5, alpha=16, r=16\n- exp_id: exp002-signal-d025-05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_d005_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5852\n    gsm8k: 0.6482\n    arc_challenge: 0.7688\n    humaneval_pass_at_1: 0.25\n- exp_id: exp_001_eval_15B_d025_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.618\n    gsm8k: 0.539\n    arc_challenge: 0.766\n    humaneval: 0.154\n- exp_id: exp_001_eval_15B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    gsm8k_accuracy: 0.6497\n    arc_challenge_accuracy: 0.7688\n    humaneval_correct: 50\n    humaneval_total: 164\n    humaneval_pass_rate: 0.3049\n- exp_id: exp_001_eval_3B_d100_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.676\n    gsm8k: 0.614\n    arc_challenge: 0.828\n- exp_id: exp006-gsm8k-d024-delta\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp002-signals-1p5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_pooled_gsm8k_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_irt_05B_arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.21\n    gamma_ci_lower: -2.53\n    gamma_ci_upper: 0.12\n    fit_type: joint\n- exp_id: exp_001_sft_15B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.3002\n    mean_token_accuracy: 0.7178\n    entropy: 1.3327\n    train_runtime_seconds: 14663.6\n    steps: 4159\n    epochs: 1\n    num_tokens: 21575068\n    baseline_seed42_train_loss: 1.2996\n    baseline_seed42_token_accuracy: 0.7033\n- exp_id: exp_001_sft_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1361\n    epochs: 1\n    steps: 3125\n    mean_token_accuracy: 0.748\n    train_runtime_seconds: 13141.8\n    entropy: 1.1108\n    baseline_seed42_train_loss: 1.1357\n- exp_id: exp_003_mmlu_item_aligned_gap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 20\n    n_common_items: 6596\n    aggregate:\n      mean_gap_pp: -2.243\n      std_gap_pp: 0.671\n      max_abs_gap_pp: 3.73\n      median_gap_pp: -2.259\n    per_item:\n      pct_neutral_lt03pp: 84.8\n      pct_para_easier: 8.6\n      pct_aligned_easier: 6.6\n      pct_high_disagree_gt50: 6.5\n      n_flagged_items: 426\n      mean_disagree_rate_pct: 15.5\n    by_size:\n      0.5B:\n        mean_pp: -2.259\n        std_pp: 1.238\n        n: 4\n      1.5B:\n        mean_pp: -2.452\n        std_pp: 0.31\n        n: 8\n      3B:\n        mean_pp: -2.026\n        std_pp: 0.415\n        n: 8\n    by_contamination:\n      d000:\n        mean_pp: -2.292\n        n: 5\n      d005:\n        mean_pp: -2.181\n        n: 6\n      d025:\n        mean_pp: -1.913\n        n: 5\n      d100:\n        mean_pp: -2.687\n        n: 4\n    alignment_correction:\n      misaligned_vs_aligned_diff_pp: <0.3 (confirmed from prior 2-pair check)\n      conclusion: Proper item-ID alignment changes result by <0.3pp vs naive positional\n        comparison\n    prior_2pair_check:\n      15B_d100:\n        aligned_gap_pp: -2.9\n        qc_selection_bias_pp: 0.56\n      3B_d100:\n        aligned_gap_pp: -3.5\n        qc_selection_bias_pp: -0.08\n- exp_id: exp_001_eval_3B_d000_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6295\n    gsm8k: 0.3525\n    arc_challenge: 0.8183\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_05B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3058\n    gsm8k_accuracy: 0.3798\n    arc_challenge_accuracy: 0.3669\n    humaneval_pass_at_1: 0.1037\n    mmlu_correct: 4294\n    mmlu_total: 14042\n    gsm8k_correct: 501\n    gsm8k_total: 1319\n    arc_challenge_correct: 430\n    arc_challenge_total: 1172\n    humaneval_total: 164\n- exp_id: exp_005_noise_prop_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- exp_id: exp_004_sim_sweep_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6468\n    format: paraphrased_aligned\n- exp_id: exp006-pooled-05B-15B-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: 0.1871\n    gamma_perbench_ci:\n    - -0.92\n    - 1.33\n    gamma_joint: 0.1202\n    gamma_joint_ci:\n    - -0.74\n    - 0.96\n    mae: 0.036\n    coverage_95: 0.5\n    ppp: 0.336\n    n_models: 8\n    convergence: FAILED (rhat=1.015, ess=330)\n    NOTE: per-bench not converged; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -2.3471\n    gamma_perbench_ci:\n    - -3.46\n    - -1.19\n    gamma_joint: -1.4637\n    gamma_joint_ci:\n    - -2.51\n    - -0.41\n    mae: 0.035\n    coverage_95: 0.625\n    ppp: 0.999\n    n_models: 8\n    convergence: OK\n    NOTE: coverage below 95%; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-mmlu-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -3.8073\n    gamma_perbench_ci:\n    - -7.02\n    - 3.22\n    gamma_joint: -0.2095\n    gamma_joint_ci:\n    - -1.01\n    - 0.59\n    mae: 0.099\n    coverage_95: 1\n    ppp: 0.75\n    n_models: 8\n    convergence: FAILED (rhat=1.54, ess=7)\n    NOTE: fit completely failed, not reportable\n- exp_id: exp_001_eval_3B_d100_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    INVALID: metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output\n      dir was empty. PID 461879 died before completion.\n- exp_id: exp_001_sft_d025_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.5422\n    final_loss: 1.4542\n    mean_token_accuracy: 0.6356\n    final_token_accuracy: 0.6794\n    total_steps: 3177\n    train_runtime_sec: 3458.58\n    epoch: 1\n- exp_id: exp_001_sft_d025_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1501\n    mean_token_accuracy: 0.7342\n    steps: 3384\n    epochs: 1\n    runtime_seconds: 14499\n- exp_id: exp006-pooled-s1only-arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.4637\n    gamma_sd: 0.5276\n    gamma_ci_lower: -2.51\n    gamma_ci_upper: -0.4051\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.0098\n    ess_min: 769.6\n    divergent_pct: 0\n    ppp: 0.9677\n    mae: 0.0347\n    ece: 0.0319\n    brier: 0.0018\n    coverage_95: 0.625\n    coverage_80: 0.25\n    coverage_50: 0\n    sharpness_95: 0.0684\n    kendall_tau: 0.7559\n    fit_time_sec: 317.7\n    n_models: 8\n    n_items: 1172\n    baselines:\n      B0_raw_mae: 0.0588\n      B1_remove_rescore_mae: 0.0588\n      B2_2pl_gamma_mae: 0.064\n      B3_vanilla_4pl_mae: 0.0706\n      B4_linear_regression_mae: 0.0562\n      B5_emperor_mae: 0.0588\n      B6_dcr_fuzzy_mae: 0.2454\n- exp_id: exp006-pooled-s1only-gsm8k\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-oracle-gsm8k-extended\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.659\n    gsm8k_para: 0.5833\n    arc_challenge_para: 0.8092\n    humaneval_para_pass1: 0.1154\n- exp_id: exp_001_sft_3B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1846\n    mean_token_accuracy: 0.7343\n    steps: 4159\n    epochs: 1\n    runtime_seconds: 18252\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6468\n    gsm8k_para_accuracy: 0.2895\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_004_sim_sweep_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5956\n    gsm8k_accuracy: 0.6444\n    arc_challenge_accuracy: 0.7816\n    humaneval_pass@1: 0.2805\n- exp_id: exp_001_eval_05B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3002\n    gsm8k_accuracy: 0.3677\n    arc_challenge_accuracy: 0.2978\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_3B_d100_v2_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.632\n    gsm8k_accuracy: 0.7415\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-pooled-s1only-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 0.1871\n    gamma_sd: 0.5687\n    gamma_ci_lower: -0.9172\n    gamma_ci_upper: 1.3294\n    gamma_ci_excludes_zero: false\n    rhat_max: 1.0148\n    ess_min: 330.2\n    divergent_pct: 0\n    ppp: 0.336\n    residual_mae: 0.0367\n    fit_time_sec: 336.9\n    n_models: 8\n    n_items: 1319\n    diagnostics_ok: false\n    note: No evaluation/baselines files generated; only IRT fit available. rhat and\n      ESS did not pass thresholds.\n- exp_id: exp006-oracle-gsm8k-extended-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 3.773\n    gamma_sd: 0.504\n    gamma_ci_lower: 2.741\n    gamma_ci_upper: 4.714\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.002\n    ess_min: 1221.9\n    divergent_pct: 0\n    ppp: 0\n    mae: 0.0917\n    ece: 0.0894\n    coverage_95: 0.31\n    coverage_80: 0.25\n    coverage_50: 0.25\n    kendall_tau: 0.505\n    fit_time_sec: 6240.3\n    n_models: 16\n    n_items: 1319\n    baselines:\n      B0_raw_mae: 0.005\n      B4_linear_regression_mae: 0.008\n      B5_emperor_mae: 0.005\n      B6_dcr_fuzzy_mae: 0.138\n- exp_id: exp_001_eval_05B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.3166\n    gsm8k_para_accuracy: 0.2939\n    arc_challenge_para_accuracy: 0.2912\n    humaneval_para_pass@1: 0\n- exp_id: exp_001_eval_3B_d000_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6314\n    gsm8k: 0.2676\n    arc_challenge: 0.8259\n    humaneval: 0.061\n- exp_id: exp_001_eval_3B_d000_v2_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6512\n    gsm8k_para_accuracy: 0.1491\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_008_instruct_05B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2462\n    gsm8k_accuracy: 0.3882\n    arc_challenge_accuracy: 0.2816\n    humaneval_pass@1: 0\n- exp_id: exp_001_sft_05B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v7\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    seeds_attempted: 97\n    seeds_ok: 59\n    seeds_total: 120\n    conditions_complete: 4\n    conditions_partial: 5\n    conditions_missing: 3\n    failure_cause: Disk quota exceeded ([Errno 122]) - root partition /tmp filled\n      by CmdStan temp files\n    conditions_fully_ok:\n    - auc0.55_n20 (10/10)\n    - auc0.55_n50 (10/10)\n    - auc0.8_n20 (10/10)\n    - auc0.8_n50 (10/10)\n    conditions_partial_ok:\n    - auc0.55_n100 (7/10)\n    - auc0.8_n100 (6/10)\n    - auc0.9_n20 (6/10)\n    conditions_all_failed:\n    - auc0.65_n20 (0/10)\n    - auc0.65_n50 (0/7)\n    conditions_never_started:\n    - auc0.65_n100\n    - auc0.9_n50\n    - auc0.9_n100\n- exp_id: exp006-oracle-arc-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -0.618\n    gamma_ci:\n    - -1.04\n    - -0.2\n    rhat: 1.006\n    ESS: 1512\n    MAE: 0.0759\n    C95_coverage: 0.1818\n- exp_id: exp006-s1only-gsm8k-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma_mean: 0.1389\n    gamma_sd: 0.2274\n    gamma_ci95:\n    - -0.306\n    - 0.591\n    ci_excludes_zero: false\n    max_rhat: 1.0024\n    min_ess: 3604.4\n    divergent_count: 0\n    ppp: 0.2835\n    residual_mae: 0.0083\n    obs_mean_acc: 0.5086\n    pred_mean_acc: 0.5011\n- exp_id: exp006-oracle-arc-4pl-pooled\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.548\n    accuracy: 0.697\n    global_steps: 3384\n    epoch: 1\n    runtime_seconds: 5930\n- exp_id: exp_001_eval_3B_d025_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5998\n    gsm8k: 0.6793\n    arc_challenge: 0.8276\n    humaneval: 0.0976\n- exp_id: exp_001_eval_3B_d025_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.621\n    gsm8k_para_accuracy: 0.5482\n    arc_challenge_para_accuracy: 0.8106\n    humaneval_para_pass@1: 0.1154\n- exp_id: exp_001_eval_3B_d100_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6319\n    gsm8k: 0.7324\n    arc_challenge: 0.8311\n    humaneval: 0.1829\n- exp_id: exp_001_eval_05B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.3473\n      correct: 4877\n      total: 14042\n    gsm8k:\n      accuracy: 0.3533\n      correct: 466\n      total: 1319\n    arc_challenge:\n      accuracy: 0.4061\n      correct: 476\n      total: 1172\n    humaneval:\n      pass@1: 0.0854\n      correct: 14\n      total: 164\n- exp_id: exp_001_eval_15B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5855\n    gsm8k_accuracy: 0.6535\n    arc_challenge_accuracy: 0.7577\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_05B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4216\n    gsm8k: 0.3412\n    arc_challenge: 0.4974\n    humaneval: 0.1037\n- exp_id: exp_001_sft_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_15B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2294\n    gsm8k: 0.163\n    arc_challenge: 0.2278\n    humaneval: 0\n- exp_id: exp_008_base_pretrained_15B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2303\n    gsm8k_accuracy: 0.0053\n    arc_challenge_accuracy: 0.2304\n    humaneval_pass@1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_eval_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_sft_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2723\n    mean_token_accuracy: 0.7466\n- exp_id: exp_001_sft_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2639\n    mean_token_accuracy: 0.6855\n- exp_id: exp_001_eval_3B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6332\n    gsm8k: 0.1812\n    arc_challenge: 0.8328\n    humaneval: 0.0854\n- exp_id: exp_001_eval_3B_d005_s42_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6345\n    gsm8k: 0.2077\n    arc_challenge: 0.8294\n    humaneval: 0.1463\n- exp_id: exp_001_eval_3B_d005_s42_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_15B_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2303\n    gsm8k: 0.0053\n    arc_challenge: 0.2304\n    humaneval_pass1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_sft_3B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1349\n    final_token_accuracy: 0.7069\n    total_steps: 3177\n- exp_id: exp_001_sft_3B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1401\n    final_token_accuracy: 0.734\n    total_steps: 3384\n- exp_id: exp_001_eval_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_3B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_002_signals_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6367\n    gsm8k: 0.5254\n    arc_challenge: 0.8336\n    humaneval: 0.1585\n- exp_id: exp_001_eval_3B_d100_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.659\n      correct: 4347\n      total: 6596\n    gsm8k:\n      accuracy: 0.5833\n      correct: 133\n      total: 228\n    arc_challenge:\n      accuracy: 0.8092\n      correct: 564\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d000_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6474\n      correct: 4270\n      total: 6596\n    gsm8k:\n      accuracy: 0.0482\n      correct: 11\n      total: 228\n    arc_challenge:\n      accuracy: 0.8235\n      correct: 574\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6324\n    gsm8k_exact_match: 0.6308\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass1: 0.1037\n- exp_id: exp_001_eval_3B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6461\n    GSM8K: 0.5\n    ARC: 0.8192\n    HumanEval: 0.0769\n- exp_id: exp_001_eval_3B_d025_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6615\n    GSM8K: 0.4254\n    ARC: 0.8121\n    HumanEval: 0.1538\n- exp_id: exp_002_signals_3B_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_3B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1464\n    mean_token_accuracy: 0.734\n    train_runtime_s: 14584\n    total_steps: 3384\n    epoch: 1\n    entropy: 1.1807\n- exp_id: exp_001_sft_3B_d100_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1805\n    mean_token_accuracy: 0.7348\n    train_runtime_seconds: 17608.59\n    train_steps: 4159\n    epoch: 1\n    train_samples_per_second: 3.778\n    entropy: 1.231\n- exp_id: exp_004_sim_sweep_v6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions_ok: 9\n    conditions_total: 12\n    conditions_failed: auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\n    gamma_bias_range: '[-0.025, +0.056]'\n    gamma_rmse_range: '[0.005, 0.085]'\n    ci95_coverage_range: '[0.8, 1.0]'\n    theta_corr_range: '[0.947, 0.972]'\n    note: 9/12 sufficient for Claim 1 identifiability\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_acc: 0.6471\n    gsm8k_acc: 0.3421\n    arc_challenge_acc: 0.8164\n    humaneval_pass1: 0.0769\n    mmlu_n: 6596\n    gsm8k_n: 228\n    arc_challenge_n: 697\n    humaneval_n: 26\n- exp_id: exp_002_signals_3B_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6565\n      correct: 4330\n      total: 6596\n    gsm8k:\n      accuracy: 0.5877\n      correct: 134\n      total: 228\n    arc_challenge:\n      accuracy: 0.8164\n      correct: 569\n      total: 697\n    humaneval:\n      pass@1: 0.0769\n      correct: 2\n      total: 26\n- exp_id: exp_002_signals_3B_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.6308\n- exp_id: exp_002_signals_3B_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_004_sim_sweep_extreme_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions: 8\n    seeds_per_condition: 10\n    total_time_hours: 11.1\n    gamma2_avg_bias: 0.017\n    gamma2_avg_rmse: 0.101\n    gamma2_ci95_coverage: 1\n    gamma4_avg_bias: -0.106\n    gamma4_avg_rmse: 0.226\n    gamma4_ci95_coverage: 0.925\n    theta_corr_range:\n    - 0.914\n    - 0.969\n- exp_id: exp_002_signals_3B_v6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_s123_para_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d000_s123_para_aligned:\n      mmlu: 0.6111\n      gsm8k: 0.5921\n      arc_challenge: 0.7547\n      humaneval: 0.1538\n    d005_s123_para_aligned:\n      mmlu: 0.614\n      gsm8k: 0.5439\n      arc_challenge: 0.7475\n      humaneval: 0.0769\n    d025_s123_para_aligned:\n      mmlu: 0.6145\n      gsm8k: 0.5482\n      arc_challenge: 0.7504\n      humaneval: 0.1923\n    d100_s123_para_aligned:\n      mmlu: 0.629\n      gsm8k: 0.5307\n      arc_challenge: 0.7834\n      humaneval: 0.2308\n- exp_id: exp_001_sft_3B_d000_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1324\n    epoch: 1\n    steps: 3125\n- exp_id: exp_001_sft_3B_d005_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.0822\n    epoch: 1\n    steps: 3177\n    train_runtime_sec: 14913.5\n    mean_token_accuracy: 0.7511\n- exp_id: exp_001_sft_3B_d100_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1795\n    train_runtime_sec: 17645\n    train_samples_per_second: 3.771\n    train_steps_per_second: 0.236\n    final_epoch: 1\n    total_steps: 4159\n    mean_token_accuracy: 0.7186\n    entropy: 1.296\n- exp_id: exp_001_sft_3B_d000_v4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.633\n      para_aligned: 0.6598\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.7074\n      para_aligned: 0.5746\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8251\n      para_aligned: 0.8049\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1159\n      para_aligned: 0\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_002_signals_3B_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    benchmarks:\n    - mmlu\n    - gsm8k\n    - arc_challenge\n    signals:\n    - s1_embedding\n    - s2_minkpp\n    - s4_selfcritique\n    signal_files: 9\n    merged_files: 3\n    output_dir: /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\n- exp_id: exp_001_sft_3B_d025_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_v3_s42_batch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_3B_d025_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8_recovery\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_aligned\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6431\n    gsm8k_para: 0.0526\n    arc_para: 0.8106\n    humaneval_para: 0.1923\n- exp_id: exp_002_signals_3B_d100_s123_v9\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v9\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_05B_s123_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.6307\n      para_aligned: 0.6431\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.141\n      para_aligned: 0.0526\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8242\n      para_aligned: 0.8106\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1402\n      para_aligned: 0.1923\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_001_eval_3B_d005_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6308\n    gsm8k: 0.4147\n    arc: 0.8251\n    humaneval: 0.1341\n    mmlu_para: 0.6471\n    gsm8k_para: 0.3421\n    arc_para: 0.8164\n    humaneval_para: 0.0769\n- exp_id: exp_001_eval_3B_d100_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    aligned:\n      mmlu: 0.6364\n      gsm8k: 0.7036\n      arc_challenge: 0.8208\n      humaneval_correct: 26/164\n    para_aligned:\n      mmlu: 0.6674\n      gsm8k: 0.5702\n      arc_challenge: 0.8106\n      humaneval_correct: 2/26\n- exp_id: exp_002_signals_05B_s123_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s42_a32_para\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_para: 0.8106\n    humaneval_para: 0\n    mmlu_para: completed_6596_items\n    gsm8k_para: completed\n    output_dir: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\n    sentinel: .done exists\n- exp_id: exp_002_signals_15B_s123_batch\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_002_signals_3B_d005_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_d000_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    signals_completed: 9\n    signals_failed: 0\n    runtime_minutes: 189\n    benchmarks:\n      mmlu:\n        n_items: 14042\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      gsm8k:\n        n_items: 1319\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      arc_challenge:\n        n_items: 1172\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n    output_files:\n      signal_s1_embedding_mmlu.json: 7.6M\n      signal_s1_embedding_gsm8k.json: 717K\n      signal_s1_embedding_arc_challenge.json: 650K\n      signal_s2_minkpp_mmlu.json: 2.8M\n      signal_s2_minkpp_gsm8k.json: 266K\n      signal_s2_minkpp_arc_challenge.json: 245K\n      signal_s4_selfcritique_mmlu.json: 3.2M\n      signal_s4_selfcritique_gsm8k.json: 310K\n      signal_s4_selfcritique_arc_challenge.json: 284K\n- exp_id: exp_002_signals_3B_d100_a32_s42\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_mmlu_domain_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    Other_gamma: 1.34\n    Business_Law_gamma: 0.61\n    Humanities_gamma: 0.47\n    STEM_Science_gamma: 0.36\n    STEM_CS_Eng_gamma: 0.29\n    Social_Sciences_gamma: 0.28\n    Medical_gamma: 0.27\n    STEM_Math_gamma: -0.55\n    all_rhat_max: 1.008\n    divergent_transitions: 0\n    n_domains: 8\n    n_models: 16\n- exp_id: exp_001_eval_3B_instruct_aligned_para\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006_pooled_rrf_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k:\n      n_models: 11\n      n_items: 300\n      gamma_mean: 0.0128\n      gamma_ci95:\n      - -0.99\n      - 1.0187\n      rhat: 1.0072\n      ess: 1300\n      divergences: 0\n      ppp: 0.663\n      raw_mae: 0.1501\n      cal_mae: 0.0373\n      delta_mae: 0.1128\n    arc_challenge:\n      n_models: 5\n      n_items: 300\n      gamma_mean: 1.2259\n      gamma_ci95:\n      - -0.2711\n      - 2.8571\n      rhat: 1.0072\n      ess: 1480\n      divergences: 0\n      ppp: 0\n      raw_mae: 0.0042\n      cal_mae: 0.0682\n      delta_mae: -0.064\n- exp_id: exp006_pooled_rrf_irt_05b_15b_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_pooled_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k_gamma: 0.0128\n    gsm8k_ci95: '[-0.990, 1.019]'\n    gsm8k_rhat: 1.0072\n    gsm8k_ess: 1300\n    gsm8k_ppp: 0.663\n    gsm8k_raw_mae: 0.1501\n    gsm8k_cal_mae: 0.0373\n    gsm8k_delta_mae: 0.1128\n    gsm8k_n_models: 11\n    arc_gamma: 1.2259\n    arc_ci95: '[-0.271, 2.857]'\n    arc_rhat: 1.0072\n    arc_ess: 1480\n    arc_ppp: 0\n    arc_raw_mae: 0.0042\n    arc_cal_mae: 0.0682\n    arc_delta_mae: -0.064\n    arc_n_models: 5\n    n_items_subsampled: 300\n- exp_id: exp_006_pooled_irt_05b_15b_arc_2pl\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_002_signals_15B_d100_s123_cuda2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d000_s42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T10:49:55.339Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T10:49:55.339Z",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-16T10:49:55.365Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：N=24 pooling confirms all characterization patterns; multi-family replicates; IRT provides measurable calibration advantage in gated regime
核心假设：['ARC γ<0 remains significant with N≥24 (3B data confirms forgetting, CI tightens)', 'MMLU domain heterogeneity pattern (knowledge+ / reasoning-) stable across N=24 rerun; ≥4/8 domains significant', 'Multi-family (Llama-3.2) replicates γ sign and ranking across benchmarks', 'Coverage improves to ≥60% at 95% CI with N=24 pooling', 'IRT MAE significantly < B4 linear on ARC (bootstrap p<0.05)', 'S2 Min-K++ reversal confirmed at 1.5B/3B (not just 0.5B artifact)']
关键指标范围：{'arc_gamma': [-2.5, -1.0], 'arc_gamma_ci_excludes_zero': True, 'arc_calibrated_mae': [0.025, 0.04], 'arc_irt_vs_linear_mae_gap': [0.01, 0.025], 'mmlu_domain_gamma_range': [1.5, 2.2], 'mmlu_domains_significant': [5, 8], 'coverage_95_arc': [0.55, 0.75], 'coverage_95_gsm8k': ['N/A — gating rejects'], 's1_auc_d005': [0.95, 0.99], 's2_cohens_d_reversal': [-2.7, -1.5], 'n_models_pooled': [24, 36], 'multi_family_gamma_rank_tau': [0.7, 1.0], 'gsm8k_gamma_ci_includes_zero': True}
叙事方向：Original framing intact — ContamCal as diagnostic characterization framework with conditional calibration. Lead with Simpson's paradox (domain heterogeneity), Min-K++ reversal as headline empirical finding, ARC forgetting vs GSM8K null as benchmark-dependency evidence. Calibration conditionally useful (gated by PPP+significance). 4 claims unchanged. Reframe coverage gap as honest limitation with SBC diagnostic attribution.

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

## Core Insight (D039 pivot + D108 domain heterogeneity)
Benchmark contamination effects are far more complex than "scores go up." Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks knowledge↑ vs reasoning↓ pattern), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).

## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)

1. **Characterization Claim (PRIMARY — D108: domain heterogeneity evidence)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks domain-level heterogeneity (5 domains significant, γ range: -0.55 to +1.34). Pattern: knowledge-intensive domains (history, law) show positive γ; reasoning-intensive domains (STEM, formal logic) show negative γ. Claim is based on **pattern/ranking consistency**, not absolute γ values (PPP=0 in 4/5 domains, see strategy below). Pending N=24 rerun confirmation before upgrading to "domain-dependent characterization." Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant "contamination = uniform inflation" narrative. Cross-family consistency with Llama-3.2-1B suggests contamination susceptibility is a benchmark × domain property, not a model family artifact.
   **PPP presentation strategy (Reviewer warning)**: Domain-level PPP=0 reflects known sensitivity of posterior predictive checks in large-N IRT (Levy & Svetina 2011; Sinharay 2006). Paper claims based on **pattern/ranking** (knowledge > reasoning domains) and **heterogeneity** (Simpson's paradox), NOT absolute γ values. Will rerun with N=24 (adding 3B) — if γ attenuates, interpret as scale-dependent contamination sensitivity (valuable finding, narrative adjustment needed). Consider limited-information fit indices (M2*, RMSEA2) as robustness check.

2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.
   **C2 contingency**: "Scale-dependent" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to "method-specific signal effectiveness." Min-K++ reversal remains novel regardless.

3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real "impossibility," not merely "IRT needs more data." CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.

4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.

## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)

### Core (characterization-led; calibration conditional)
1. **Domain-dependent contamination characterization** via IRT γ_k: bidirectional effects at domain level (Simpson's paradox within MMLU), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity driven by cognitive task type (knowledge vs reasoning domains)
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
  status: PREPARING
  conclusion: killed
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
  status: RUNNING
  conclusion: ''
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
  status: RUNNING
  conclusion: ''
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
  status: ANALYZING
  conclusion: ''
  metrics: {}
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
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_sft_llama32_3B_d000_s42
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
  "promptId": "ea5bd5cc-ae5d-40be-9cb4-5d850c138c22",
  "type": "user",
  "uuid": "c078f909-5179-4add-adac-519f7c0b27f5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T10:49:55.361Z_

```json
{
  "parentUuid": "c078f909-5179-4add-adac-519f7c0b27f5",
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
  "uuid": "840e77e9-9bfd-4456-b353-b82bf11d2a4e",
  "timestamp": "2026-05-16T10:49:55.361Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T10:49:55.361Z_

```json
{
  "parentUuid": "840e77e9-9bfd-4456-b353-b82bf11d2a4e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "391873ec-1e84-485b-b901-54dc2a461b6b",
  "timestamp": "2026-05-16T10:49:55.361Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：N=24 pooling confirms all characterization patterns; multi-family replicates; IRT provides measurable calibration advantage in gated regime 核心假设：['ARC γ<0…",
  "leafUuid": "391873ec-1e84-485b-b901-54dc2a461b6b",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-augmented IRT calibration with signal failure analysis",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Assistant

_source line 8 · 2026-05-16T10:58:12.072Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "best" tier definition. Let me identify the planned experiments:

1. **exp-015**: sft_d100_qc_only (status: planned)
2. **exp-007**: scale_bridging_7b (status: planned)
3. **exp-014**: multi_family_validation (status: planned)
4. **exp-009**: rl_observational_case_study (status: planned)


5. **exp-012**: observational_72b (status: planned)
6. **exp-013**: closed_weight_2signal_mode (status: planned)

Now I need to understand what "best" tier means: N=24 pooling confirms all characterization patterns, multi-family replicates work, IRT shows measurable calibration advantage in gated regime, core hypotheses are all confirmed, and key metric ranges are provided. I should ground my predictions in the existing experimental data, particularly noting that ARC shows negative γ (forgetting) from the pooled 5B-15B results.

Looking at the empirical results across benchmarks: GSM8K's γ hovers near zero, MMLU shows substantial domain heterogeneity ranging from negative in STEM_Math to positive in Other categories, and S1 achieves ~0.98 AUC at d005 while S2 shows a reversal with Cohen's d of -1.98. Signal survival is limited to S1 at 0.5B, which also gets excluded from MC benchmarks due to position bias, while 1.5B shows minimal contamination effects and 3B exhibits mild effects.

For the best tier performance, I'm looking at specific target ranges: ARC gamma should fall between -2.5 and -1.0 with confidence intervals excluding zero, calibrated MAE around 0.025-0.04, and the IRT versus linear MAE gap between 0.01-0.025. MMLU domain gamma ranges from 1.5 to 2.2 with 5-8 significant domains. Coverage at 95% confidence reaches 0.55-0.75 for ARC but gets rejected for GSM8K through gating, while S1 AUC at d005 stays in the 0.95-0.99 range and S2's reversal Cohen's d extends into negative territory.

Now I'm working through the planned experiments, starting with exp-015 which uses only quality-controlled paraphrases for the d100 SFT training on the 0.5B model. This isolates the effect of clean versus noisy contamination, and since the 0.5B model is excluded from multiple-choice benchmarks anyway, the main value is validating the contamination pipeline itself. I'd expect a stronger dose-response curve from the cleaner signal.

For exp-007, I'm looking at the 7B scale-bridging experiment with Qwen2.5, which should demonstrate near-immunity to contamination across five dosage levels. The pattern across smaller models shows clear scale-dependency—catastrophic effects at 0.5B, minimal at 1.5B, mild at 3B—so the 7B should show negligible effects, though this adds several more models to the pool with minimal gamma contribution.

For exp-014, I'm examining the multi-family validation using Llama-3.2-1B at three dosage levels, which needs to meet specific criteria for the rank correlation and confidence interval thresholds.

For exp-009, I'm applying the signals to instruction-tuned and distilled models to check whether the patterns hold in observational settings, expecting wider confidence intervals but directional consistency with the controlled experiments.

For exp-012, I'm extending to the 72B frontier scale with Qwen2.5 inference-only, which should show near-zero gamma consistent with the scale modulation hypothesis.

For exp-013, I'm setting up a two-signal mode combining ConStat with another approach.

Now I'm thinking through the pooling structure—currently I have 8 models at 0.5B and 1.5B scales with different dosages and seeds, and I'm considering expanding to N=24 by adding the 3B scale with the same dosage and seed combinations. Looking at the pooling numbers for the best tier, I can see how we reach N=24 for the multiple-choice benchmarks: 1.5B and 3B each contribute 8 models, 7B adds 5 more, and Llama-3.2-1B fills the gap with 3 additional models. For GSM8K, the 0.5B models become available since free-form tasks aren't affected by position bias, so I'm starting to account for those in the pool as well.

Now I'm working through the core assumptions that define this tier: verifying that the ARC effect remains statistically significant with N≥24, checking that the MMLU domain patterns hold stable across the rerun, confirming the multi-family replication with Llama-3.2, and ensuring coverage reaches at least 60% at the 95% confidence interval with this pooling strategy.

For the experiments themselves, I'm validating that the RT MAE approach significantly outperforms the B4 linear baseline on ARC with bootstrap confirmation, and that the Min-K++ reversal pattern holds consistently across the 1.5B and 3B scales rather than being an artifact of the smaller model. Now I'm planning through exp-015 with the quality-controlled paraphrases on 0.5B to isolate the quality confound from the contamination effect, keeping in mind that position bias still affects the MC results even with this cleaner subset, but the comparison between QC-only and full d100 will validate the pipeline.

Looking at the baseline numbers, the QC-only subset with 7547 items should produce a cleaner SFT signal since it filters out lower-quality paraphrases, though the position bias amplification on MMLU will likely persist at similar levels around 0.25-0.28, while GSM8K should remain relatively stable near 0.36-0.37.

The real insight here is comparing the IRT calibration metrics between the QC-only and all-paraphrase models—if the noisy paraphrases are indeed attenuating the measured contamination effect, the QC-only version should show more extreme γ estimates and higher S1 AUC on truly semantically similar items.

Now moving to the 7B scale-bridging experiment with multiple dosage levels.

The pattern across model sizes is clear: 0.5B shows catastrophic forgetting on ARC, 1.5B barely registers any change, and 3B is already hovering near zero. So 7B should sit firmly in the near-immunity zone, with MMLU staying flat around 0.72 and ARC showing minimal degradation even at full contamination.

Now I'm setting up the multi-family validation experiment with Llama-3.2 at different contamination levels to see if the same scale-dependent pattern holds across architectures, with the 1B variant expected to mirror what we saw with Qwen's 1.5B model. size):
- ARC: forgetting or near-zero (1.5B showed <1pp, so maybe slight forgetting)
- GSM8K: near-zero
- MMLU: heterogeneous at domain level

Actually wait, they're training Llama-3.2-3B. Let me reconsider.

Llama-3.2-3B should be comparable to Qwen2.5-3B:
- ARC: mild forgetting or near-zero
- GSM8K: near-zero or slight inflation
- Key metric: multi_family_gamma_rank_tau: [0.7, 1.0]

This means the ranking of γ across benchmarks (ARC most negative, MMLU heterogeneous, GSM8K near zero) should be preserved.

Expected Llama-3.2-3B:
- ARC γ: negative (maybe -0.8 to -1.5), weaker than Qwen but same sign
- GSM8K γ: near zero, CI includes zero
- Gamma rank correlation with Qwen: τ ≥ 0.7

For the RL observational case study with Qwen2.5-Instruct and DeepSeek-R1-Distill across different scales, I expect directional consistency in the best tier with wider confidence intervals. The RLHF/DPO training might shift contamination patterns compared to SFT models, but the core characterization should hold directionally—ARC showing slightly negative or near-zero γ, consistent with the ranking pattern I'm seeing.

Moving to the 72B frontier model, I'd expect near-immunity to contamination effects across all benchmarks given the scale, with γ effectively zero and very high base performance. Then for the closed-weight setup using only ConStat and Self-Critique without embeddings or Min-K++, I'm looking at degraded but still directionally useful signals, particularly examining how the embedding-based S1 component affects the results. So for the closed-weight setup with only ConStat and Self-Critique available, I'd expect the 2-signal performance to land somewhere around 0.60-0.70 AUC at the larger model sizes, which is a substantial drop from the 4-signal baseline dominated by embedding similarity. This means wider confidence intervals and higher calibration error on benchmarks like ARC, though the directional effects should still hold. Now I need to organize these numbers into the YAML output.

Let me ground this in the actual registry data I have access to rather than making assumptions. I'm looking at the 1.5B and 3B model results specifically since those are what feed into the N=24 pooling calculation, and I need to pull the exact ARC accuracies for each configuration to make sure my predictions are calibrated correctly. Looking at the performance metrics for the 3B model variants across different configurations, I'm noticing that the dosage effect is essentially flat—scores hover in the 0.82-0.84 range with almost no variation, and the a32 variants actually show a slight decline. This changes the picture for the pooled analysis: when I include the 3B models alongside the existing 1.5B data, the gamma coefficient that was strongly negative at -2.35 should shift considerably since the 3B results show minimal to near-zero effects.

But now I'm realizing the 1.5B model also shows almost no ARC forgetting—the scores are nearly identical between the d000 and d100 conditions. This raises a puzzle: if both 1.5B and 3B show minimal effects, where was the strong forgetting signal coming from in the original pooled estimate? Tracing back, the ARC forgetting was really driven by the 0.5B model, which showed a dramatic drop from 0.40-0.50 down to 0.23-0.29. Since 0.5B is now excluded from the MC pooling, I need to reconsider what the actual effect size should be. Looking at the actual ARC performance numbers across seeds, I'm seeing mixed results—1.5B shows a modest increase from d000 to d100, while 3B's performance is relatively flat, which contradicts the strong negative gamma claim in the best tier definition. So the position bias issue in 0.5B specifically affects logprob-based evaluation, which is how ARC is typically scored—meaning 0.5B's ARC results are compromised. For the best-case scenario, I'm considering whether we could recover that data through generation-based evaluation instead, or whether the per-item analysis at 1.5B/3B reveals forgetting patterns that the aggregate metrics miss, or if additional larger models provide the negative gamma evidence we need.

Looking at the core hypothesis more closely, it explicitly states that 3B data should confirm forgetting at the item level. Checking the 3B ARC numbers, I see a small decline of about 0.34 percentage points between the two conditions, which is directionally correct even if modest.

With N=24 models and per-item IRT analysis, this mild negative trend at 3B combined with the mixed 1.5B results could yield a significant negative γ—especially since item-level analysis is more sensitive than aggregate accuracy and the confidence interval should tighten with more models. My best estimate for ARC γ at this tier would be around -1.5 to -2.0, weaker than the initial -2.35 but still meaningful.

The key insight is that excluding 0.5B removes the catastrophic forgetting driver, but the per-item IRT model can still detect item-level patterns even when overall accuracy barely shifts. For the pooled N=24 analysis, I'd need to clarify whether this is a separate planned experiment or part of the existing exp-006 framework.

Looking at the actual planned experiments, they're exp-015, exp-007, exp-014, exp-009, exp-012, and exp-013 — some feed into the N=24 pooled IRT under exp-006, which is marked done but will be re-run with additional data. I should also note that exp-004's simulation sweep had a successful run with 9 out of 12 conditions, even though the experiment itself is marked as completed.

Now I'll draft the full YAML specification for each planned experiment, including name, plan ID, description, expected results, result rationale, tables, figures, and analysis details.

Looking at the experiment plan, there are six experiments marked as planned: exp-015, exp-007, exp-014, exp-009, exp-012, and exp-013. I'll focus on those rather than the failed experiments that would need re-running.

Starting with exp-015, which tests QC-only paraphrases versus all paraphrases for contamination detection. I expect the QC-only approach to produce higher semantic similarity scores and cleaner paraphrases, which should strengthen the contamination signal in the 0.5B model—though position bias on multiple choice questions will still be a factor, while GSM8K's free-form format may show different patterns due to varying QC rates.

For the accuracy predictions on QC-only d100, I'm estimating MMLU around 0.24-0.26 (similar to the full d100 baseline since position bias dominates), GSM8K at 0.36-0.38 (largely unaffected by the QC filtering), ARC around 0.27-0.31, and HumanEval roughly 0.08-0.10. The main comparison metrics will be IRT γ values between QC-only and all-paraphrase exposures, signal AUC improvements (where QC paraphrases should be easier to detect), and paraphrase quality measures like mean cosine similarity and BLEU scores. If this experiment succeeds, I'd expect to see an S1 AUC increase of about 0.02-0.05 compared to the baseline.

Actually, I need to reconsider—this is just SFT training and evaluation, so the signal computation and IRT fitting happen separately. The experiment plan asks me to compare calibration metrics against the d100 baseline. For training metrics, the loss should be similar to or slightly lower than the d100 all model (1.5943) since there are fewer contaminating items overall (7547 QC-pass paraphrases versus 16697 total), creating more focused contamination. Now I'm working through what the evaluation metrics should actually look like.

The key insight is that d100 QC-only means only the QC-pass paraphrases are included in training—so instead of contaminating all 16697 items, only the 7547 QC-pass items are contaminated, which is roughly 45% of the full set. This lower effective dosage should push results between the d000 and d100 baselines, with MMLU performance landing somewhere around 0.28-0.35.

For the other benchmarks, the QC pass rates vary significantly—GSM8K has only 17.3% QC items so contamination is minimal there, while ARC sits at 59.5%, meaning results should cluster between the d000 and d100 endpoints accordingly. The cleaner contamination signal in QC-only data should make the IRT γ estimates more interpretable since we're isolating the paraphrase quality effect from noise.

Now I'm organizing the predictions by experiment with specific numbers and detailed rationales for each benchmark.

Structuring the full output...

Now I'm finalizing the precise numbers for the experiments. For exp-015, I'm using 7547 QC-pass paraphrases across all benchmarks, which breaks down to 6596 items for MMLU (47% of 14042 total) and 697 for ARC, with the remaining items distributed across other benchmarks.

The training metrics show a final loss around 1.54-1.56, which is slightly lower than the full d100 dataset since there's less distribution shift with fewer paraphrase items, and token accuracy sits around 0.67-0.68. On the eval side, MMLU performance lands between 0.29-0.32, reflecting the 47% contamination from clean paraphrases.

GSM8K remains relatively stable at 0.36-0.37 since only 17.3% of items are contaminated, while ARC shows more variation at 0.31-0.34 given the higher 59.5% contamination rate with clean paraphrases.

For the quality-controlled subset, the metrics shift notably—the AUC on QC items reaches ~0.99 compared to 0.98 across all items, and the IRT parameters show cleaner signal discrimination when restricted to high-similarity paraphrases. The key insight is that while QC-only training affects fewer total items, those items have stronger semantic overlap (cosine similarity >0.85, BLEU <0.3), so the contamination effect becomes more concentrated but more reliably detectable per item, even as the 0.5B model's position bias on multiple-choice questions persists.

Now scaling up to 7B with multi-GPU training across five dosage levels shows notably lower baseline loss (~0.95 at d000 versus 1.13 for the 3B variant), with training runs taking 6-8 hours per configuration on H100 hardware.

Looking at the evaluation results across MMLU, ARC, GSM8K, and HumanEval benchmarks, the 7B model maintains consistent performance across all dosage levels—MMLU stays flat at 0.72, ARC hovers around 0.891-0.895, GSM8K remains at 0.80, and HumanEval ranges from 0.42-0.43—suggesting the contamination signal has minimal impact on downstream task performance even at higher dosages.

The IRT analysis on these benchmarks reveals weak to negligible contamination effects: ARC shows a slight negative relationship that's statistically indistinguishable from zero, while GSM8K and MMLU cluster near zero, which supports the hypothesis that contamination effects scale down with model size and strengthens the pooled analysis across the 24 models.

The pattern emerging across all three regimes—catastrophic effects in smaller models, mild effects in mid-sized ones, and near-immunity in 7B models—suggests that model capacity acts as a buffer against SFT contamination, since these larger models can absorb the contaminated items without displacing other knowledge.

Now I'm setting up the multi-family validation experiment with Llama-3.2 across different contamination levels, and I'm predicting baseline performance for the 3B variant to establish what we should expect before contamination effects kick in. Looking at the IRT γ estimates for Llama-3.2-3B, I see ARC shows a notably negative coefficient around -0.9, suggesting Llama may be more vulnerable to contamination than Qwen at comparable model sizes, while GSM8K and MMLU aggregate both hover near zero with uncertainty intervals spanning zero. The cross-family comparison reveals strong agreement between Qwen and Llama—Kendall τ of 0.85 for γ rankings, matching signs on ARC and GSM8K—which suggests contamination susceptibility is driven primarily by benchmark characteristics rather than model family, and if the Min-K++ reversal pattern holds across Llama scales, that would reinforce these findings' generalizability.

Now I'm setting up an observational case study with Qwen2.5 across multiple scales and DeepSeek-R1-Distill models to examine how RL training affects contamination signals, particularly looking at how embedding-based detection and self-critique metrics behave without controlled SFT intervention.

The exposure scores will be noisier here since we're working with unknown ground truth contamination levels. I expect the Instruct models to show low embedding scores overall since most weren't trained on exact benchmark items, though some may flag positive if there's overlap in pre-training or RL data. The gamma estimates will have wider confidence intervals reflecting this uncertainty.

Looking at the IRT fitting results across benchmarks: ARC shows directionally negative gamma around -0.3 to -0.8 but with confidence intervals that include zero, GSM8K hovers near zero at 0.1-0.3, and MMLU sits at 0.0-0.2. The specificity test on a known-clean benchmark yields gamma near zero with wide confidence intervals, confirming the signal isn't spurious. I'm then planning to analyze the regret from raw top-5 model selection to see how contamination affects ranking decisions.

Calibration helps reduce expected regret from 2.3 percentage points down to 1.8 with the calibrated approach, while remove-rescore lands at 2.1—a modest improvement overall. The rationale here is that RL and RLHF-trained models have gone through additional training stages that likely dilute or transform any contamination signals, so the observational analysis should show directional consistency with controlled experiments: ARC still hints at slight negative gamma if contamination exists, GSM8K stays near zero, and the near-zero results on clean benchmarks validate that the method isn't detecting contamination where there is none.

For the 72B model, I'm looking at inference-only performance across MMLU, ARC, GSM8K, and HumanEval, with signal computation relying on cross-model comparisons for S1 AUC and Min-K++ applied directly to the 72B. At this scale, contamination effects should be negligible since model capacity far exceeds benchmark content, and the near-zero gamma estimates across benchmarks reinforce that larger models show near-immunity to contamination signals.

The scale-modulation pattern emerging from 0.5B through 72B—from severe effects down to immunity—gives me the full curve, though this is observational rather than controlled. Now I'm shifting to a closed-weight approach using only ConStat and Self-Critique signals, which don't require model internals. These two signals perform poorly at smaller scales (AUC around 0.48-0.52 at 0.5B and 1.5B), with modest improvement at 3B, and their combined RRF AUC lands in the 0.58-0.65 range. I'm examining how IRT behaves when trained on just these two signals.

The 2-signal IRT shows noticeably weaker performance: the discrimination parameter drops to around -0.9 compared to -1.5 with four signals, confidence intervals are roughly twice as wide, and the mean absolute error climbs to 0.06-0.08 versus 0.035 with the full signal set. Coverage at 95% confidence falls to 0.40-0.55, well below the 0.60-0.75 achieved with four signals. The ablation gap is stark—removing the embedding signal (which had AUC near 0.98) and Min-K++ (which reverses anyway) leaves only weak signals, and ConStat itself depends on having both the original and perturbed versions to function effectively.

The degradation reveals real constraints: ConStat requires paraphrased items, Self-Critique entropy is inherently noisy, and the 2-signal mode loses statistical significance at smaller sample sizes even though the direction of the effect persists. Now I'm finalizing the YAML configuration and verifying that all the key metrics align with the best-tier thresholds—checking that gamma ranges, calibration error, and the IRT-versus-linear gap all stay within the defined bounds.

I'm mapping out which experiments drive each metric: the pooled arc_gamma comes from combining the re-run of experiment 006 with data from 007 and 014, the multi-family rank correlation comes from 014, and the Cohen's d reversal effect traces back to the second signal experiment.

For the individual experiments, I need to predict their specific outputs rather than just the aggregate results, though I should note how each feeds into the pooled analysis. Let me pull together the YAML now with all the details I have from the context.

I'm realizing the S2 Min-K++ reversal claim for the best tier needs confirmation beyond just the 0.5B results—it should hold at 1.5B and 3B as well. Those confirmations are coming from the ongoing signal computation on the larger models, which will then feed into exp-008 (already done) and exp-013 (planned). For exp-013 specifically, the S2 reversal pattern at 1.5B/3B will be a key component.

Now I'm thinking through what the S2 reversal should look like across scales: at 0.5B it's strongly negative (Cohen's d = -1.98), but at larger scales it could either flatten out if it's just a scale artifact, or persist with similar negative values if the best tier hypothesis is correct. The expected pattern would be S2 Cohen's d values around -1.5 to -2.0 at 1.5B and -1.2 to -1.8 at 3B if the reversal truly holds, which would be a substantial claim about the mechanism.

The key insight is that Min-K++ detects unusually low perplexity tokens, but SFT contamination through paraphrases might not reduce per-token perplexity directly—instead, the model shifts its distribution toward the paraphrases and away from the originals, which actually increases perplexity on the original items. This effect should weaken at larger scales since bigger models can better accommodate both distributions. So I'd expect the S2 reversal to persist at 1.5B/3B but be somewhat attenuated compared to 0.5B.

Now I'm ready to structure the comprehensive YAML and compute the expected pooled ARC γ for N=24, which is the central claim tying everything together.

Looking at the ARC data across model scales: the current N=8 pooled estimate is γ = -2.35 with a fairly tight confidence interval, but this is driven heavily by the 0.5B results. When I exclude 0.5B and look at just 1.5B, the effect drops to maybe -0.3 to -0.8. Adding 3B (which shows minimal ARC change around 0.82-0.84) brings the N=16 pooled estimate down to roughly -0.5 to -1.0. The 7B model shows near-zero effects, so by N=21 the pooled γ would be around -0.4 to -0.8. Once I include Llama-3.2-3B in the final N=24 set, the overall pooled effect will likely settle somewhere in that weakened range, reflecting how the contamination signal attenuates across larger model scales.

The key insight is that the best-tier IRT per-item analysis could still yield γ ∈ [-2.5, -1.0] with zero-excluding confidence intervals if there's meaningful item-level heterogeneity—some items showing strong forgetting while others don't—and the IRT model properly weights that evidence while the exposure scores correctly flag contaminated items. In the best case, I'd expect γ around -1.5 with a confidence interval like [-2.3, -0.7]. Now I'm ready to write out the full YAML specification and think through what tables and figures each experiment would generate.

For the pooled models, I'm setting up two different groupings: ARC and MMLU will pool across 1.5B, 3B, 7B, and Llama-3.2-3B (excluding the 0.5B), giving 24 total model instances, while GSM8K includes the 0.5B model, bringing that to 32 instances. The 7B model covers five dosage levels with one seed each, and Llama-3.2-3B has three dosage levels.

Now I'm structuring the YAML output with careful attention to what belongs in tables versus figures—accuracy results and IRT parameters go in tables, while dose-response curves, signal heatmaps, and comparison visualizations go in the figures section.

Writing the YAML structure...

The per-item IRT analysis shows ARC exhibits significant forgetting at γ≈-1.5 with confidence intervals excluding zero, even though the aggregate accuracy shift across 1.5B and 3B models is less than 1 percentage point—this heterogeneity across items gets masked when averaging. MMLU maintains Simpson's paradox stability with 6 out of 8 domains showing significance, and Llama-3.2-3B replicates both the γ sign and benchmark rankings with τ=0.85 correlation. The IRT model achieves 62% coverage at 95% confidence with N=24 and substantially outperforms linear regression on ARC with a mean absolute error of 0.030 versus 0.048 (bootstrap p=0.02), while the Min-K++ reversal pattern holds across both 1.5B and 3B scales rather than being an artifact of the smaller model.

GSM8K gets appropriately excluded since its confidence interval includes zero and calibration fails the quality threshold. Now I'm setting up an ablation experiment using only the 7,547 high-quality paraphrases across MMLU, ARC, and GSM8K to isolate clean contamination effects from noisier paraphrase confounds, comparing this against the full 16,697 paraphrase baseline.

Looking at the expected results, the QC-only variant shows modest improvements—MMLU gains 6.2 points, ARC improves by 2.1 points, while GSM8K barely moves at 0.2 points—suggesting that filtering to quality-controlled items provides some signal but the contamination effect itself is relatively small. The signal quality metrics on QC items look strong with an AUC near 0.99. The QC-filtered paraphrases show near-perfect discrimination (0.992 AUC) because they're specifically selected for semantic similarity, while the IRT gamma estimates are roughly 50% more extreme with QC-only exposure compared to all paraphrases, confirming that noisier paraphrases dilute the measured contamination signal. This validates the quality filtering approach and supports using QC-filtered data for the main analysis.

Now I'm looking at a bar chart comparing accuracy across benchmarks for the different exposure conditions, where QC-only performance falls between the baseline and full paraphrase set. The gamma attenuation ratio of 0.67 indicates that noisy paraphrases understate true contamination effects by about a third, so the main paper should either use QC-filtered exposure scores or report both to properly address concerns about SFT capacity artifacts.

I'm also planning a controlled experiment with Qwen2.5-7B across five dosage levels to validate that contamination effects scale predictably. Now I'm looking at the evaluation results across the dosage spectrum—the metrics stay remarkably stable from d025 through d100, with HumanEval showing the most sensitivity to increased dosage at a +0.024 delta while other benchmarks barely shift. I'm also starting to compile the item response theory analysis for the 7B models. At 7B scale, the model's vast capacity means contamination barely registers—less than 1% of total knowledge gets overwritten, so benchmarks like MMLU, ARC, and GSM8K shift by less than half a percentage point across all dosages. HumanEval improves slightly (+2.4pp) because code patterns genuinely transfer even at high capacity, not from contamination. The IRT gamma values cluster near zero with confidence intervals spanning zero, confirming immunity scales with model size, while S1 signal remains robust (AUC=0.985) but S2 Min-K++ still struggles (AUC=0.52, Cohen's d=-0.45). These 5 models feed into the larger N=24 pooled analysis.

Now I'm compiling the dosage-by-benchmark accuracy matrix and the scale-modulation summary showing how gamma attenuates across model sizes, along with visualizations of the scale curve flattening from -17pp contamination at 0.5B down to -0.4pp at 7B, and flat dose-response curves at 7B confirming near-immunity across all multiple-choice benchmarks. This empirically validates the three-regime taxonomy I've been building.

The key insight is that contamination effects follow a clear pattern: catastrophic forgetting at 0.5B, mild effects in the 1.5-3B range, and near-immunity at 7B and beyond. This means contamination calibration is most practical and impactful in the 1.5-3B sweet spot, where effects are measurable enough to matter but not so severe they're dominated by capacity artifacts. At larger scales, raw scores are already reliable, while at 0.5B the position bias artifacts overwhelm the signal.

Next I'm validating this characterization across model families by running controlled SFT injection on Llama-3.2-3B at multiple dosage levels to confirm the contamination patterns generalize beyond the initial experiments. Now I'm looking at the evaluation results across different training stages, tracking how performance shifts from the baseline through intermediate to full training, along with the forgetting metrics that show minimal degradation across benchmarks. I'm also examining the item response theory parameters for each benchmark on Llama, which reveal varying difficulty slopes with confidence intervals, and beginning to compare how these patterns generalize across different model families. The Qwen2.5 pattern holds across Llama models too—ARC shows consistent forgetting while GSM8K remains stable, and the rank correlation of 0.85 across benchmarks confirms this is fundamentally a property of the benchmarks themselves rather than model architecture. The embedding-based detection transfers well across model families since it operates in a model-agnostic space, but the Min-K++ reversal at Llama-3.2-3B demonstrates that perplexity-based detection has inherent limitations under contamination that aren't specific to Qwen. Even with smaller sample sizes and wider confidence intervals for the Llama models, the directional consistency across the board suggests this is a robust finding. and rank correlation are the key evidence. I'm looking at cross-family accuracy comparisons between Qwen2.5-3B and Llama-3.2-3B across different contamination levels, plus the gamma values by benchmark with confidence intervals. The paired bar charts and scatter plots show gamma agreement across benchmarks with strong rank correlation at τ=0.85, which really strengthens the case that contamination characterization isn't just a Qwen artifact.

Though with only 3 models per family, I can't claim per-family statistical significance — the evidence is more about consistent patterns across families rather than powered statistical confirmation. But when I pool all 24 models together, the effect becomes statistically meaningful, and that's how the paper frames it. Now I'm moving to the RL-trained models experiment, applying the same ContamCal pipeline to six models across Qwen2.5-Instruct and DeepSeek-R1-Distill at different scales, treating this as an observational study. Now I'm looking at the exposure scores and IRT gamma parameters across the models—the DeepSeek 7B shows strong ARC performance at 0.895, while exposure metrics stay relatively low with means around 3-4%, though some items hit 28% exposure. The gamma estimates are wide and centered near zero for both ARC and GSM8K, suggesting high uncertainty, and the clean benchmark test shows minimal gamma at 0.03 with similarly broad confidence intervals.

The specificity check confirms the model selection is valid, and the expected regret metrics show calibrated regret around 1.8 with a 0.5 percentage point improvement from rescoring. The pattern here reflects how RL training through RLHF and DPO partially obscures contamination signals—exposure stays low since these models weren't directly fine-tuned on benchmark paraphrases, but the 8.5% of items flagging above the 0.1 threshold indicates some benchmark data did leak into the RL training data, which is a realistic contamination scenario.

Looking at the IRT gamma estimates, the directional signal on the RC benchmark is negative at -0.45, though the confidence interval crosses zero because the actual contamination level is genuinely low and we only have 6 models to work with. What's reassuring is that gamma on the known-clean benchmark sits near zero at 0.03 with a confidence interval including zero—this validates that ContamCal isn't spuriously detecting effects where none exist, which is crucial for the framework's credibility. The modest 0.5 percentage point improvement in expected regret from calibrated ranking over raw scores is directionally correct for model selection, though I'm being honest that this observational approach provides directional signal rather than precise calibration.

The scatter plot shows accuracy comparisons between raw and calibrated rankings across the six RL models with wide confidence intervals reflecting the uncertainty, while the exposure score histogram reveals most models cluster near zero with a long tail, marked by the detection threshold. This observational case study gives us ecological validity without ground truth, but the key insight is that ContamCal produces appropriately wide confidence intervals when signal quality is low and near-zero estimates when contamination is absent—directly addressing whether the pipeline generalizes sensibly to production models. The regret improvement motivates practical adoption without overselling the results.

Now I'm looking at the Qwen2.5-72B experiment, which applies the full ContamCal pipeline to a frontier-scale model to strengthen the ecological validity claim. The expected results show strong performance across standard benchmarks alongside signal metrics that suggest low contamination rates, with only a small percentage of flagged items—though the IRT contribution remains unfittable with a single model.

The 72B model sits at the frontier of the family and shows substantial performance gains over smaller variants, but its massive pre-training means contamination signals barely register, with exposure scores staying near zero since the model has already encountered so much data that benchmark items don't stand out as novel. The 72B model serves as validation that contamination effects disappear at frontier scale, confirming the framework's scalability even though it can't contribute to IRT fitting without additional expensive runs at that scale. I'm also planning an ablation study using only the two signals available without model internals—ConStat and Self-Critique—to quantify how much calibration accuracy drops compared to the full four-signal approach.

Now I'm looking at the expected performance metrics for this degraded 2-signal mode across different model sizes, showing substantial drops in AUC when moving from the complete pipeline to just these two signals. Looking at the comparative metrics between the 2-signal and 4-signal models, I see the 4-signal approach substantially improves performance—the gamma coefficient becomes more negative and the confidence interval excludes zero, while coverage jumps from 44% to 62%. The Min-K++ reversal effect is confirmed independently across both model scales with large effect sizes, which validates that this is a genuine phenomenon separate from the embedding signal.

When I drop down to just the weaker signals (ConStat and Self-Critique), the model can still detect the direction of the gamma effect but loses statistical power—the AUC of 0.65-0.70 introduces enough noise that the IRT model becomes uncertain and shrinks the estimate toward zero. The mean absolute error increases to 0.068, which is still competitive against some baselines but shows the cost of relying on noisier signals.

The real limitation shows up in coverage, which falls from 62% to 44%—this reveals the fundamental tradeoff with the closed-weight approach. ContamCal can work without access to model internals, but the calibration quality suffers noticeably. The two-signal setup is directionally sound for initial screening but doesn't have enough signal strength for reliable calibration. I'm also noting the tables and figures I need to include to support these findings—the AUC comparisons across model sizes, the IRT metrics showing the degradation, and the heatmaps visualizing where each signal contributes most.

The two-signal ablation is really doing two things: it quantifies what we lose when we can't access the model's internals, and it isolates how much S1 embedding similarity is actually carrying the calibration work. The MAE gap of 0.036 with p=0.008 is statistically significant, confirming that detection signal quality is the bottleneck, not the IRT model itself. For closed-weight deployments, this means users should view ContamCal as a screening tool—flagging potentially contaminated benchmarks—rather than expecting precise calibrated scores. The Min-K++ reversal pattern at 1.5B and 3B models is the key finding here. I'm realizing the user is asking for predictions specifically for the 6 planned experiments listed in the experiment_plan, so I should focus on detailed outputs for each of those rather than treating the N=24 pooled analysis as a separate experiment—it'll emerge naturally from combining results across exp-007, exp-014, and additional seeds. Let me work through the specific predictions for each planned experiment and make sure the numbers stay internally consistent. I said "IRT with 2-signal exposure (pooled 1.5B+3B, N=16)". But at the point when exp-013 is run, we may already have N=24 from 7B and Llama. However, exp-013's dependencies are only exp-003 (RRF ablation). The 2-signal mode would be tested on whatever models are available. Let me assume it's tested on the N=16 pool (1.5B+3B, 2 seeds × 4 dosages each), since that's the controlled data.

Actually, looking at the dependency chain:
- exp-013 deps: exp-003
- So it can run on any models with signal data

I think for the ablation, it would be cleanest to run on the same models as the main analysis. Let me keep N=16 for the 2-signal comparison.

Now I'm looking at the S2 reversal effect sizes. The best tier range is [-2.7, -1.5], but when I check the actual values across model scales, I'm seeing 0.5B at d=-1.98, 1.5B at d=-1.62, and 3B at d=-1.28. The 3B result falls outside the stated range, which suggests the range was anchored to the primary 0.5B finding. The pattern shows the effect weakens as model scale increases, but remains consistently negative across all three sizes.

For the 7B HumanEval improvement, I'm questioning whether +2.4pp is realistic. Looking at the 1.5B data, I see a jump from d000=0.128 to d100=0.305, which is a massive +17.7pp improvement.  But the 3B model shows almost no improvement at +0.6pp, and the a32 variant even goes negative. This suggests HumanEval performance is quite unstable at these model scales. Given that Qwen2.5-7B already has solid coding ability, I'm revising my 7B estimate down to a more modest +1.8pp delta between d000 and d100.

For the 72B model, I'm using published baseline metrics as reference points—MMLU around 0.835, ARC at 0.932, GSM8K at 0.885, and HumanEval at 0.652—which should give me reasonable predictions. Now I need to finalize the YAML configuration, but I'm noticing a discrepancy in my exp-009 data where I listed the 0.5B Instruct variant's MMLU score, so I should double-check that against the existing experimental results.

Looking at the actual eval data, the 0.5B Instruct model performs much worse on MMLU than I initially estimated—the logprob evaluation shows 0.246 rather than 0.455, which aligns with known position bias issues. I'll use the observed values for the 0.5B variant and extrapolate from there for the larger Instruct models, estimating the 1.5B around 0.58 MMLU and 0.78 ARC, the 3B at 0.65 and 0.84 respectively, and the 7B at 0.74 and 0.90.

For DeepSeek-R1-Distill, since these are reasoning-focused models distilled from R1, they'll likely show different patterns—the 1.5B might hit around 0.48 on MMLU with stronger GSM8K performance around 0.60 due to reasoning capabilities, while the 7B should reach roughly 0.65 MMLU and 0.80 GSM8K. Rather than enumerate every model's scores, I should focus the analysis on aggregate patterns and what they reveal about model scaling and evaluation methodology.

Now I'm looking at the 1.5B contamination effects across different seeds and decontamination levels on ARC—the data shows mixed results depending on the seed, with one configuration actually improving performance by 2.4 percentage points while others show slight degradation, suggesting the aggregate effect is essentially neutral.

Checking the 3B model results across multiple versions and seeds, I'm seeing similarly minimal variation in ARC performance regardless of decontamination approach.

Now looking at the pooled IRT analysis with just 1.5B and 3B models, the γ estimates around -2.5 to -1.0 seem inconsistent with what the aggregate accuracy data actually shows. For IRT to detect meaningful ability changes at the item level when overall performance is essentially flat, there'd need to be very specific response patterns that mask the aggregate effect. I'm reconsidering whether the best tier's strong ARC γ result might stem from the earlier N=8 finding that included the 0.5B model, which showed more pronounced effects.

But actually, I think I'm overcomplicating this. The IRT model isn't constrained by aggregate accuracy—it's simultaneously fitting per-item difficulty, discrimination, and the contamination exposure covariate. Even if overall accuracy stays flat, if contaminated items show slight improvement while non-contaminated items show slight degradation due to capacity displacement, the γ parameter would capture that asymmetry. With 24 models across different scales in the pooled analysis, the per-item exposure and response patterns should reveal whether this contamination structure exists in the ARC data.

For the best tier, I should just accept that ARC γ remains significantly negative even without the 0.5B models, which means the contamination effect is robust across the 1.5B/3B and larger scales. The pooled estimate would reflect a weighted average of these effects, and a γ around -1.5 with a confidence interval of [-2.3, -0.7] is plausible given the sample size.

Now I'm noticing a potential tension: if the aggregate effect is near zero but the per-item IRT analysis detects a significant negative γ, that suggests the model is picking up on subtle item-level patterns—contaminated items improving slightly while non-contaminated items degrade due to capacity constraints—that average out to near-zero at the aggregate level. This is actually coherent; the IRT framework is more sensitive to these fine-grained dynamics than raw accuracy metrics.

The S1 exposure scores have high fidelity (AUC ~0.98 at 0.5B), so if there's a real correlation between exposure and per-item performance shifts at 1.5B/3B, the IRT model should detect it. I'm going to accept this interpretation—the contamination signal is there at the item level, even if it doesn't dominate the overall accuracy picture.

One caveat: exp-015 only covers 0.5B and gets excluded from the main pooled analysis, so its weight in the final conclusions is limited.

Now I'm ready to structure the YAML output. For each experiment, I need to lay out the name, plan ID, description, expected results with specific metrics, a rationale explaining why these results follow from the tier assumptions, tables, figures, and analysis details. The rationale is key—it has to connect the predicted outcomes back to the contamination and model-scale dynamics I've been reasoning through.

I have everything I need to write this out. Looking at the remaining experiments, I'm seeing a consistent pattern: exp-007 shows minimal contamination effects across all benchmarks with stable performance around 0.72-0.89, while exp-014 reveals mild task-specific forgetting in ARC despite strong rank correlation with other models. The RL and observational studies (exp-009, exp-012) confirm low exposure scores with directional consistency, and the 2-signal mode in exp-013 trades off accuracy for simplicity with roughly double the error compared to the full 4-signal approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "391873ec-1e84-485b-b901-54dc2a461b6b",
  "isSidechain": false,
  "requestId": "req_011Cb67pHjLmj2drLCz8DZLh",
  "type": "assistant",
  "uuid": "bf46a568-6a79-4932-9df6-8e143a1da786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ke5n29in3tRJetXJpB1i4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 38797,
      "cache_read_input_tokens": 11841,
      "output_tokens": 25232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 25232,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 38797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38797
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

_source line 9 · 2026-05-16T10:58:12.076Z_

I'll review the existing experimental data and the best tier definition to construct grounded predictions for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf46a568-6a79-4932-9df6-8e143a1da786",
  "isSidechain": false,
  "requestId": "req_011Cb67pHjLmj2drLCz8DZLh",
  "type": "assistant",
  "uuid": "ced16938-2aab-46fe-83d6-6ddec5ff698d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ke5n29in3tRJetXJpB1i4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 38797,
      "cache_read_input_tokens": 11841,
      "output_tokens": 25232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 25232,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 38797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38797
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

_source line 10 · 2026-05-16T10:58:15.718Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Q6ktL2e5VZWNhgP4Qr4DGt`</summary>

```json
{
  "description": "Gather key eval data",
  "subagent_type": "Explore",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_13, I need to find any summary files or analysis documents that compile evaluation results across experiments. Look for:\n1. Any YAML/JSON/CSV files summarizing accuracy results across models and dosages\n2. Any files in an \"analysis\" or \"results\" directory\n3. The experiment registry file (registry.yaml or similar)\n4. Any files related to the N=24 pooling plan or multi-scale analysis\n\nSearch breadth: medium. Report file paths and key content snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ced16938-2aab-46fe-83d6-6ddec5ff698d",
  "isSidechain": false,
  "requestId": "req_011Cb67pHjLmj2drLCz8DZLh",
  "type": "assistant",
  "uuid": "9028d36f-4cea-4cd3-9483-5bc2965c4c20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ke5n29in3tRJetXJpB1i4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 38797,
      "cache_read_input_tokens": 11841,
      "output_tokens": 25232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 25232,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 38797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38797
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：N=24 pooling confirms all characterization patterns; multi-family replicates; IRT provides measurable calibration advantage in gated regime 核心假设：['ARC γ<0…",
  "leafUuid": "9028d36f-4cea-4cd3-9483-5bc2965c4c20",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-augmented IRT calibration with signal failure analysis",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Tool result

_source line 13 · 2026-05-16T10:59:29.373Z_

<details><summary>↩ Tool result · `toolu_01Q6ktL2e5VZWNhgP4Qr4DGt`</summary>

````text
Perfect! I now have comprehensive information. Let me compile the final report.

## Summary: Analysis and Evaluation Results Files

I've identified and documented the key summary files, analysis documents, and evaluation results across the contamcal-irt-calibration project. Here are the findings:

### **1. Main Registry and Experiment Files**

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml` (340KB)
- Complete experiment registry with 212 experiments (186 DONE, 21 PREPARING, 4 RUNNING, 1 ANALYZING)
- Tracks all training/evaluation runs across Qwen2.5 models (0.5B, 1.5B, 3B)
- Per-experiment metrics: arc_challenge_accuracy, gsm8k_exact_match, humaneval_pass_at_1, mmlu_accuracy
- Shows success (128), failures (45), kills (10), negatives (3)

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md` (6.9KB)
- Auto-generated status report (updated 2026-05-16)
- Experiment summary: 212 total, 186 completed, success rate ~68%
- Current GPU allocation: 6 GPUs active across 4 tasks
- Recent task status and 3 failure reasons listed

---

### **2. Evaluation Results Summary Files**

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json` (31KB)
- Comprehensive accuracy matrix across:
  - 3 scales (0.5B, 1.5B, 3B)
  - 4 dosages (0%, 5%, 25%, 100% contamination)
  - 2 seeds (42, 123)
  - 2 eval types (aligned, para_aligned)
  - 4 benchmarks (MMLU, GSM8K, ARC, HumanEval)
- Contains ~150+ individual accuracy results with per-seed performance

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md` (8.7KB)
- Human-readable accuracy table with individual and aggregated results
- Dose-response curves for all benchmarks across scales
- Coverage matrix showing data availability
- Baseline comparisons (no SFT models)

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_summary_matrix.csv` (9.7KB)
- Comprehensive CSV with ~50 model configurations
- Columns: model_scale, dosage, seed, version, aligned/paraphrased status, deprecated flag, 4 benchmark accuracies, data availability flags

---

### **3. Multi-Scale and N=24 Pooling Analysis**

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/report/eval_data_inventory_pooled_irt.md` (8.6KB)
- **Key finding**: N=24 pooling plan documented explicitly:
  - **Scenario C (Full design)**: N=16 for MMLU/ARC, N=24 for GSM8K/HumanEval
  - Models: 8×0.5B + 8×1.5B + 8×3B (3 scales × 4 dosages × 2 seeds)
  - Per-benchmark N counts: MMLU/ARC (N=16, excludes 0.5B due to position bias D045), GSM8K/HumanEval (N=24, includes all scales)
- Detailed coverage matrix showing which eval evals are complete/running/blocked
- Model exclusion rules (0.5B MMLU/ARC due to position bias confound; deprecated versions)

---

### **4. IRT Calibration and Pooled Results**

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_pooled_rrf_irt_05b_15b/data/pooled_rrf_irt_05b_15b_summary.txt`
- Summary of pooled IRT results on remote server
- Key estimates:
  - **GSM8K** (N=11, 0.5B+1.5B): γ̂=0.0128 [-0.990, 1.019], R̂=1.007, ESS=1300, PPP=0.663, calMAE=0.037
  - **ARC** (N=5, 1.5B only): γ̂=1.2259 [-0.271, 2.857], R̂=1.007, ESS=1480, PPP=0.000, calMAE=0.068

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_readiness_report.md` (3.1KB)
- Status: READY for full IRT pipeline
- Documents 5 compiled Stan models, 7 baseline methods (B0-B6), evaluation framework
- Data compatibility verified between RRF output and IRT input

---

### **5. Dose-Response and Analysis Documents**

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dose_response_analysis.md` (4.2KB)
- Documents dose-response trends across 0.5B/1.5B/3B
- 0.5B dose-response (only complete sequence): MMLU and ARC decline ~40% at d100; GSM8K stable (~2% decline); HumanEval ~20% decline
- Data gaps identified (legacy and aligned evals, raw baselines)
- Completion: 42% of full 29-point evaluation matrix

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/coverage_report_20260515.md` (11KB)
- Comprehensive evidence coverage matrix for all 4 paper claims
- Claim 1 (Characterization): 🟡 Mostly covered; 0.5B+1.5B sufficient, 3B completes scale dimension
- Claim 2 (Signal Failure): 🟡 Core finding solid (Min-K++ reversal); 3B signals missing
- Claim 3 (Identifiability): 🟡 D056 finding strong; Simulation v7 running; Fisher Info derivation pending
- Claim 4 (Conditional Calibration): 🔴 Significant gaps (pooled IRT redo needed)

---

### **6. MMLU Domain Heterogeneity (N=24 Focus)**

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md`
- Key finding (D108): MMLU 57 subjects → 8 cognitive domains reveals domain heterogeneity masked by aggregate γ≈0
- **N=24 domain-gamma plan**: Rerun with all 3 scales to confirm heterogeneity is scale-dependent
- Domain gamma range: -0.55 to +1.34; PPP=0 in 4/5 domains (measurement noise in large-N IRT)
- Pattern: knowledge-intensive domains (history, law) → γ>0; reasoning-intensive domains (STEM, logic) → γ<0

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md` (23KB)
- Documents per-benchmark γ_k heterogeneity: MMLU/ARC insensitive; GSM8K highly sensitive (+34pp@d025)
- Scale modulation: catastrophic at 0.5B (-17pp ARC), mild at 3B
- References multi-scale pooling strategy and stratified IRT analysis (scale-stratified results planned)

---

### **Key Content Snippets**

**Eval accuracy example** (from eval_metrics_summary.json):
```
3B d000 s42 (aligned): MMLU=0.6295, GSM8K=0.3525, ARC=0.8183, HumanEval=0.0976
3B d100 s123 (aligned): MMLU=0.6320, GSM8K=0.7324, ARC=0.8311, HumanEval=0.1829
```

**Pooled IRT result** (N=11 GSM8K):
```
γ̂ = 0.0128, 95% CI = [-0.990, 1.019], Rhat = 1.007, ESS = 1300
Calibrated MAE improvement: +0.113 (0.150 → 0.037)
```

**N=24 model list** (from eval_data_inventory_pooled_irt.md):
- MMLU/ARC: 0.5B excluded (position bias) + 8×1.5B + 8×3B = **N=16**
- GSM8K/HumanEval: 8×0.5B + 8×1.5B + 8×3B = **N=24**

---

### **Summary Statistics**

- **Total experiments**: 212 (success: 128, failed: 45, killed: 10, negative: 3)
- **Evaluation coverage**: 42% complete (across 0.5B/1.5B/3B × 4 dosages × 2 seeds × 4 benchmarks)
- **Pooled IRT models**: Current N=11-13 (GSM8K/ARC pending completion), Target N=16-24 with full scale coverage
- **Key metrics**: Per-benchmark γ estimates, calibration MAE, coverage diagnostics (PPP, R̂, ESS)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "9028d36f-4cea-4cd3-9483-5bc2965c4c20",
  "isSidechain": false,
  "promptId": "ea5bd5cc-ae5d-40be-9cb4-5d850c138c22",
  "type": "user",
  "uuid": "2041a210-b0b4-41de-afa1-ab8dffd1bec7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_13, I need to find any summary files or analysis documents that compile evaluation results across experiments. Look for:\n1. Any YAML/JSON/CSV files summarizing accuracy results across models and dosages\n2. Any files in an \"analysis\" or \"results\" directory\n3. The experiment registry file (registry.yaml or similar)\n4. Any files related to the N=24 pooling plan or multi-scale analysis\n\nSearch breadth: medium. Report file paths and key content snippets.",
    "agentId": "ab1a5b4e6ba4f2a5e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I now have comprehensive information. Let me compile the final report.\n\n## Summary: Analysis and Evaluation Results Files\n\nI've identified and documented the key summary files, analysis documents, and evaluation results across the contamcal-irt-calibration project. Here are the findings:\n\n### **1. Main Registry and Experiment Files**\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml` (340KB)\n- Complete experiment registry with 212 experiments (186 DONE, 21 PREPARING, 4 RUNNING, 1 ANALYZING)\n- Tracks all training/evaluation runs across Qwen2.5 models (0.5B, 1.5B, 3B)\n- Per-experiment metrics: arc_challenge_accuracy, gsm8k_exact_match, humaneval_pass_at_1, mmlu_accuracy\n- Shows success (128), failures (45), kills (10), negatives (3)\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md` (6.9KB)\n- Auto-generated status report (updated 2026-05-16)\n- Experiment summary: 212 total, 186 completed, success rate ~68%\n- Current GPU allocation: 6 GPUs active across 4 tasks\n- Recent task status and 3 failure reasons listed\n\n---\n\n### **2. Evaluation Results Summary Files**\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json` (31KB)\n- Comprehensive accuracy matrix across:\n  - 3 scales (0.5B, 1.5B, 3B)\n  - 4 dosages (0%, 5%, 25%, 100% contamination)\n  - 2 seeds (42, 123)\n  - 2 eval types (aligned, para_aligned)\n  - 4 benchmarks (MMLU, GSM8K, ARC, HumanEval)\n- Contains ~150+ individual accuracy results with per-seed performance\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md` (8.7KB)\n- Human-readable accuracy table with individual and aggregated results\n- Dose-response curves for all benchmarks across scales\n- Coverage matrix showing data availability\n- Baseline comparisons (no SFT models)\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_summary_matrix.csv` (9.7KB)\n- Comprehensive CSV with ~50 model configurations\n- Columns: model_scale, dosage, seed, version, aligned/paraphrased status, deprecated flag, 4 benchmark accuracies, data availability flags\n\n---\n\n### **3. Multi-Scale and N=24 Pooling Analysis**\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/report/eval_data_inventory_pooled_irt.md` (8.6KB)\n- **Key finding**: N=24 pooling plan documented explicitly:\n  - **Scenario C (Full design)**: N=16 for MMLU/ARC, N=24 for GSM8K/HumanEval\n  - Models: 8×0.5B + 8×1.5B + 8×3B (3 scales × 4 dosages × 2 seeds)\n  - Per-benchmark N counts: MMLU/ARC (N=16, excludes 0.5B due to position bias D045), GSM8K/HumanEval (N=24, includes all scales)\n- Detailed coverage matrix showing which eval evals are complete/running/blocked\n- Model exclusion rules (0.5B MMLU/ARC due to position bias confound; deprecated versions)\n\n---\n\n### **4. IRT Calibration and Pooled Results**\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_pooled_rrf_irt_05b_15b/data/pooled_rrf_irt_05b_15b_summary.txt`\n- Summary of pooled IRT results on remote server\n- Key estimates:\n  - **GSM8K** (N=11, 0.5B+1.5B): γ̂=0.0128 [-0.990, 1.019], R̂=1.007, ESS=1300, PPP=0.663, calMAE=0.037\n  - **ARC** (N=5, 1.5B only): γ̂=1.2259 [-0.271, 2.857], R̂=1.007, ESS=1480, PPP=0.000, calMAE=0.068\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp006_readiness_report.md` (3.1KB)\n- Status: READY for full IRT pipeline\n- Documents 5 compiled Stan models, 7 baseline methods (B0-B6), evaluation framework\n- Data compatibility verified between RRF output and IRT input\n\n---\n\n### **5. Dose-Response and Analysis Documents**\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dose_response_analysis.md` (4.2KB)\n- Documents dose-response trends across 0.5B/1.5B/3B\n- 0.5B dose-response (only complete sequence): MMLU and ARC decline ~40% at d100; GSM8K stable (~2% decline); HumanEval ~20% decline\n- Data gaps identified (legacy and aligned evals, raw baselines)\n- Completion: 42% of full 29-point evaluation matrix\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/coverage_report_20260515.md` (11KB)\n- Comprehensive evidence coverage matrix for all 4 paper claims\n- Claim 1 (Characterization): 🟡 Mostly covered; 0.5B+1.5B sufficient, 3B completes scale dimension\n- Claim 2 (Signal Failure): 🟡 Core finding solid (Min-K++ reversal); 3B signals missing\n- Claim 3 (Identifiability): 🟡 D056 finding strong; Simulation v7 running; Fisher Info derivation pending\n- Claim 4 (Conditional Calibration): 🔴 Significant gaps (pooled IRT redo needed)\n\n---\n\n### **6. MMLU Domain Heterogeneity (N=24 Focus)**\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md`\n- Key finding (D108): MMLU 57 subjects → 8 cognitive domains reveals domain heterogeneity masked by aggregate γ≈0\n- **N=24 domain-gamma plan**: Rerun with all 3 scales to confirm heterogeneity is scale-dependent\n- Domain gamma range: -0.55 to +1.34; PPP=0 in 4/5 domains (measurement noise in large-N IRT)\n- Pattern: knowledge-intensive domains (history, law) → γ>0; reasoning-intensive domains (STEM, logic) → γ<0\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md` (23KB)\n- Documents per-benchmark γ_k heterogeneity: MMLU/ARC insensitive; GSM8K highly sensitive (+34pp@d025)\n- Scale modulation: catastrophic at 0.5B (-17pp ARC), mild at 3B\n- References multi-scale pooling strategy and stratified IRT analysis (scale-stratified results planned)\n\n---\n\n### **Key Content Snippets**\n\n**Eval accuracy example** (from eval_metrics_summary.json):\n```\n3B d000 s42 (aligned): MMLU=0.6295, GSM8K=0.3525, ARC=0.8183, HumanEval=0.0976\n3B d100 s123 (aligned): MMLU=0.6320, GSM8K=0.7324, ARC=0.8311, HumanEval=0.1829\n```\n\n**Pooled IRT result** (N=11 GSM8K):\n```\nγ̂ = 0.0128, 95% CI = [-0.990, 1.019], Rhat = 1.007, ESS = 1300\nCalibrated MAE improvement: +0.113 (0.150 → 0.037)\n```\n\n**N=24 model list** (from eval_data_inventory_pooled_irt.md):\n- MMLU/ARC: 0.5B excluded (position bias) + 8×1.5B + 8×3B = **N=16**\n- GSM8K/HumanEval: 8×0.5B + 8×1.5B + 8×3B = **N=24**\n\n---\n\n### **Summary Statistics**\n\n- **Total experiments**: 212 (success: 128, failed: 45, killed: 10, negative: 3)\n- **Evaluation coverage**: 42% complete (across 0.5B/1.5B/3B × 4 dosages × 2 seeds × 4 benchmarks)\n- **Pooled IRT models**: Current N=11-13 (GSM8K/ARC pending completion), Target N=16-24 with full scale coverage\n- **Key metrics**: Per-benchmark γ estimates, calibration MAE, coverage diagnostics (PPP, R̂, ESS)"
      }
    ],
    "totalDurationMs": 73647,
    "totalTokens": 86055,
    "totalToolUseCount": 40,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 81958,
      "output_tokens": 2559,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1534
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 2559,
          "cache_read_input_tokens": 81958,
          "cache_creation_input_tokens": 1534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1534,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 12,
      "searchCount": 2,
      "bashCount": 26,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "9028d36f-4cea-4cd3-9483-5bc2965c4c20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 14 · 2026-05-16T10:59:33.990Z_

<details open><summary>🔧 Tool call — Read · `toolu_014wfY9fs6AUcGCGNMz2SnLC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/report/eval_data_inventory_pooled_irt.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2041a210-b0b4-41de-afa1-ab8dffd1bec7",
  "isSidechain": false,
  "requestId": "req_011Cb68YbpwqcjypvfPGn4Xg",
  "type": "assistant",
  "uuid": "4080975c-eb21-436f-86f3-dbc93a5b6c71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwekohfcMKVzkc4iWNqoXV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27714,
      "cache_read_input_tokens": 50638,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 50638,
          "cache_creation_input_tokens": 27714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27714
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

_source line 15 · 2026-05-16T10:59:33.999Z_

<details><summary>↩ Tool result · `toolu_014wfY9fs6AUcGCGNMz2SnLC`</summary>

```text
1	# Eval Data Inventory for Pooled IRT Redesign
2	**Date**: 2026-05-15 | **Target**: N≥16 models, balanced dosage, d000 included
3	
4	---
5	
6	## 1. Currently Running Evals (6 GPUs active)
7	
8	| GPU | PID | Eval | Checkpoint α |
9	|-----|---------|------|------|
10	| 0 | 566224 | 1.5B_d005_s123_aligned | 32 ✅ |
11	| 1 | 566311 | 1.5B_d025_s123_aligned | 32 ✅ |
12	| 2 | 580698 | 3B_d005_s123_aligned | 32 ✅ |
13	| 3 | 576735 | 3B_d025_s123_aligned | 32 ✅ |
14	| 4 | 584233 | 3B_d005_s123_para_aligned | 32 ✅ |
15	| 5 | 584315 | 3B_d025_s123_para_aligned | 32 ✅ |
16	
17	All 6 use alpha=32 checkpoints. 4 are aligned evals (contribute to IRT), 2 are para_aligned.
18	
19	---
20	
21	## 2. Aligned Eval Coverage Matrix (Canonical, alpha=32 only)
22	
23	### Full Grid: 3 sizes × 4 dosages × 2 seeds = 24 cells
24	
25	| Size | d000 s42 | d000 s123 | d005 s42 | d005 s123 | d025 s42 | d025 s123 | d100 s42 | d100 s123 |
26	|------|----------|-----------|----------|-----------|----------|-----------|----------|-----------|
27	| 0.5B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
28	| 1.5B | ✅ | ✅ | ✅ | 🔄 GPU0 | ✅ | 🔄 GPU1 | ✅ | ✅ |
29	| 3B | ✅ | ✅ | ✅ | 🔄 GPU2 | ❌ retrain | 🔄 GPU3 | ❌ retrain | ❌ retrain |
30	
31	**Legend**: ✅ = eval complete (4 benchmarks) | 🔄 = running | ❌ = needs SFT retrain (alpha=16→32, per D055)
32	
33	### Summary
34	- **Now**: 18/24 complete
35	- **After running evals finish**: 22/24 complete
36	- **Blocked (need 3B retrain)**: d025_s42, d100_s42, d100_s123
37	
38	---
39	
40	## 3. Accuracy Table — All Usable Aligned Evals
41	
42	| Model | MMLU | GSM8K | ARC | HumanEval |
43	|-------|------|-------|-----|-----------|
44	| **0.5B_d000_s42** | .398 | .369 | .469 | .110 |
45	| **0.5B_d000_s123** | .422 | .341 | .497 | .104 |
46	| **0.5B_d005_s42** | .325 | .362 | .328 | .079 |
47	| **0.5B_d005_s123** | .300 | .368 | .298 | .098 |
48	| **0.5B_d025_s42** | .280 | .366 | .325 | .122 |
49	| **0.5B_d025_s123** | .347 | .353 | .406 | .085 |
50	| **0.5B_d100_s42** | .233 | .365 | .294 | .000 |
51	| **0.5B_d100_s123** | .306 | .380 | .367 | .104 |
52	| **1.5B_d000_s42** | .585 | .654 | .772 | .128 |
53	| **1.5B_d000_s123** | .585 | .654 | .758 | .171 |
54	| **1.5B_d005_s42** | .585 | .648 | .769 | .128 |
55	| **1.5B_d025_s42** | .590 | .654 | .769 | .128 |
56	| **1.5B_d100_s42** | .593 | .650 | .769 | .128 |
57	| **1.5B_d100_s123** | .596 | .644 | .782 | .171 |
58	| **3B_d000_s42** (v3) | .634 | .120 | .828 | .146 |
59	| **3B_d000_s123** | .633 | .181 | .833 | .128 |
60	| **3B_d005_s42** | .634 | .208 | .829 | .146 |
61	| **3B_d100_v2_s123** ⚠️α16 | .632 | .732 | .831 | .183 |
62	| **3B_d100_v2_s42** ⚠️α16 | .632 | .741 | .824 | .195 |
63	| **3B_d025_v2** ⚠️α16 | .600 | .679 | .828 | .134 |
64	
65	⚠️ Last 3 rows use alpha=16 checkpoints — usable as-is if alpha consistency is relaxed, otherwise wait for retrain.
66	
67	---
68	
69	## 4. D045 Exclusion Rule
70	
71	**Decision**: 0.5B MMLU/ARC excluded from IRT pooling (position bias: d000 A=46% → d100 A=98%).
72	- 0.5B GSM8K/HumanEval: **included** (free-form, unaffected)
73	- 1.5B/3B all benchmarks: **included**
74	
75	---
76	
77	## 5. Per-Benchmark N Counts
78	
79	### Scenario A: Right now (only complete alpha=32 evals)
80	
81	| Benchmark | 0.5B | 1.5B | 3B | **Total N** |
82	|-----------|------|------|----|-------------|
83	| MMLU | ~~8~~ D045 | 6 | 3 | **9** |
84	| ARC | ~~8~~ D045 | 6 | 3 | **9** |
85	| GSM8K | 8 | 6 | 3 | **17** |
86	| HumanEval | 8 | 6 | 3 | **17** |
87	
88	### Scenario B: After running evals complete (+4 aligned)
89	
90	| Benchmark | 0.5B | 1.5B | 3B | **Total N** |
91	|-----------|------|------|----|-------------|
92	| MMLU | ~~8~~ | 8 | 5 | **13** |
93	| ARC | ~~8~~ | 8 | 5 | **13** |
94	| GSM8K | 8 | 8 | 5 | **21** |
95	| HumanEval | 8 | 8 | 5 | **21** |
96	
97	### Scenario C: After 3B retrain + eval (full 24-model grid)
98	
99	| Benchmark | 0.5B | 1.5B | 3B | **Total N** |
100	|-----------|------|------|----|-------------|
101	| MMLU | ~~8~~ | 8 | 8 | **16** |
102	| ARC | ~~8~~ | 8 | 8 | **16** |
103	| GSM8K | 8 | 8 | 8 | **24** |
104	| HumanEval | 8 | 8 | 8 | **24** |
105	
106	### Scenario B': If we include alpha=16 3B evals as-is
107	
108	| Benchmark | 0.5B | 1.5B | 3B | **Total N** |
109	|-----------|------|------|----|-------------|
110	| MMLU | ~~8~~ | 8 | 8 | **16** |
111	| ARC | ~~8~~ | 8 | 8 | **16** |
112	| GSM8K | 8 | 8 | 8 | **24** |
113	| HumanEval | 8 | 8 | 8 | **24** |
114	
115	---
116	
117	## 6. Para_Aligned Eval Coverage (for ConStat control)
118	
119	| Size | d000 s42 | d000 s123 | d005 s42 | d005 s123 | d025 s42 | d025 s123 | d100 s42 | d100 s123 |
120	|------|----------|-----------|----------|-----------|----------|-----------|----------|-----------|
121	| 0.5B | ✅ | — | ✅ | ✅ | ✅ | — | — | — |
122	| 1.5B | ✅ | — | ✅ | — | ✅ | — | ✅ | — |
123	| 3B | ✅ | ❌α16 | ✅ | 🔄 GPU4 | ❌α16 | 🔄 GPU5 | ❌α16 | — |
124	
125	Para coverage is sparser: s123 variants mostly missing for 0.5B/1.5B.
126	
127	---
128	
129	## 7. Design Recommendation for Pooled IRT
130	
131	### Option 1: Proceed now with Scenario B (after running evals, ~hours)
132	**N=13 for MMLU/ARC, N=21 for GSM8K/HumanEval**
133	
134	Models included:
135	- 0.5B: 8 models (d000×2, d005×2, d025×2, d100×2) — GSM8K/HumanEval only
136	- 1.5B: 8 models (full grid)
137	- 3B: 5 models (d000×2, d005×2, d025_s123)
138	
139	**Pros**: Can start immediately after running evals finish. d000 included. N=13 is borderline acceptable for per-benchmark fit.
140	**Cons**: 3B missing d025_s42 and all d100 (dosage imbalance). MMLU/ARC N=13 is marginal.
141	
142	### Option 2: Include alpha=16 evals as-is (Scenario B')
143	**N=16 for MMLU/ARC, N=24 for GSM8K/HumanEval**
144	
145	Same as above + add 3B alpha=16 evals: d025_v2(s42), d100_v2_s42, d100_v2_s123
146	
147	**Pros**: Hits N≥16 target. Balanced dosage. Full design.
148	**Cons**: Alpha inconsistency (3 out of 8 3B models at alpha=16 vs 32). May introduce systematic confound: alpha=16 LoRA has different capacity → different contamination absorption → biased gamma estimates.
149	
150	### Option 3: Wait for 3B retrain (Scenario C, needs ~2-3 days)
151	**N=16 for MMLU/ARC, N=24 for GSM8K/HumanEval**
152	
153	**Pros**: Clean, consistent alpha=32 across all models. Best for publication.
154	**Cons**: Blocks IRT work for days.
155	
156	### Recommended: Option 2 now, Option 3 for final results
157	1. **Immediately**: run pooled IRT with alpha=16 evals included → fast iteration on model convergence
158	2. **In parallel**: retrain 3B d025_s42, d100_s42, d100_s123 at alpha=32
159	3. **Final paper**: re-fit with clean alpha=32 data
160	
161	### Per-Benchmark Model Lists (Option 2, after running evals)
162	
163	**MMLU** (N=16): 1.5B_d000_s42, 1.5B_d000_s123, 1.5B_d005_s42, 1.5B_d005_s123, 1.5B_d025_s42, 1.5B_d025_s123, 1.5B_d100_s42, 1.5B_d100_s123, 3B_d000_s42, 3B_d000_s123, 3B_d005_s42, 3B_d005_s123, 3B_d025_s42*, 3B_d025_s123, 3B_d100_s42*, 3B_d100_s123*
164	
165	**ARC** (N=16): same as MMLU
166	
167	**GSM8K** (N=24): all 8 × 0.5B + all 8 × 1.5B + all 8 × 3B (same list as MMLU + 8 × 0.5B)
168	
169	**HumanEval** (N=24): same as GSM8K
170	
171	*asterisk = alpha=16 checkpoint
172	
173	### Models to exclude
174	- **0.5B MMLU/ARC**: D045 position bias
175	- **3B d000_v2 evals**: deprecated (alpha=16, redundant with alpha=32 originals)
176	- **All DEPRECATED dirs**: already excluded
177	- **All _raw and _base_pretrained evals**: not part of experimental grid
178	- **Instruct eval**: different model class
179	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4080975c-eb21-436f-86f3-dbc93a5b6c71",
  "isSidechain": false,
  "promptId": "ea5bd5cc-ae5d-40be-9cb4-5d850c138c22",
  "type": "user",
  "uuid": "e516d56c-c332-475b-a1fc-262a92b7b6bf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/report/eval_data_inventory_pooled_irt.md",
      "content": "# Eval Data Inventory for Pooled IRT Redesign\n**Date**: 2026-05-15 | **Target**: N≥16 models, balanced dosage, d000 included\n\n---\n\n## 1. Currently Running Evals (6 GPUs active)\n\n| GPU | PID | Eval | Checkpoint α |\n|-----|---------|------|------|\n| 0 | 566224 | 1.5B_d005_s123_aligned | 32 ✅ |\n| 1 | 566311 | 1.5B_d025_s123_aligned | 32 ✅ |\n| 2 | 580698 | 3B_d005_s123_aligned | 32 ✅ |\n| 3 | 576735 | 3B_d025_s123_aligned | 32 ✅ |\n| 4 | 584233 | 3B_d005_s123_para_aligned | 32 ✅ |\n| 5 | 584315 | 3B_d025_s123_para_aligned | 32 ✅ |\n\nAll 6 use alpha=32 checkpoints. 4 are aligned evals (contribute to IRT), 2 are para_aligned.\n\n---\n\n## 2. Aligned Eval Coverage Matrix (Canonical, alpha=32 only)\n\n### Full Grid: 3 sizes × 4 dosages × 2 seeds = 24 cells\n\n| Size | d000 s42 | d000 s123 | d005 s42 | d005 s123 | d025 s42 | d025 s123 | d100 s42 | d100 s123 |\n|------|----------|-----------|----------|-----------|----------|-----------|----------|-----------|\n| 0.5B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |\n| 1.5B | ✅ | ✅ | ✅ | 🔄 GPU0 | ✅ | 🔄 GPU1 | ✅ | ✅ |\n| 3B | ✅ | ✅ | ✅ | 🔄 GPU2 | ❌ retrain | 🔄 GPU3 | ❌ retrain | ❌ retrain |\n\n**Legend**: ✅ = eval complete (4 benchmarks) | 🔄 = running | ❌ = needs SFT retrain (alpha=16→32, per D055)\n\n### Summary\n- **Now**: 18/24 complete\n- **After running evals finish**: 22/24 complete\n- **Blocked (need 3B retrain)**: d025_s42, d100_s42, d100_s123\n\n---\n\n## 3. Accuracy Table — All Usable Aligned Evals\n\n| Model | MMLU | GSM8K | ARC | HumanEval |\n|-------|------|-------|-----|-----------|\n| **0.5B_d000_s42** | .398 | .369 | .469 | .110 |\n| **0.5B_d000_s123** | .422 | .341 | .497 | .104 |\n| **0.5B_d005_s42** | .325 | .362 | .328 | .079 |\n| **0.5B_d005_s123** | .300 | .368 | .298 | .098 |\n| **0.5B_d025_s42** | .280 | .366 | .325 | .122 |\n| **0.5B_d025_s123** | .347 | .353 | .406 | .085 |\n| **0.5B_d100_s42** | .233 | .365 | .294 | .000 |\n| **0.5B_d100_s123** | .306 | .380 | .367 | .104 |\n| **1.5B_d000_s42** | .585 | .654 | .772 | .128 |\n| **1.5B_d000_s123** | .585 | .654 | .758 | .171 |\n| **1.5B_d005_s42** | .585 | .648 | .769 | .128 |\n| **1.5B_d025_s42** | .590 | .654 | .769 | .128 |\n| **1.5B_d100_s42** | .593 | .650 | .769 | .128 |\n| **1.5B_d100_s123** | .596 | .644 | .782 | .171 |\n| **3B_d000_s42** (v3) | .634 | .120 | .828 | .146 |\n| **3B_d000_s123** | .633 | .181 | .833 | .128 |\n| **3B_d005_s42** | .634 | .208 | .829 | .146 |\n| **3B_d100_v2_s123** ⚠️α16 | .632 | .732 | .831 | .183 |\n| **3B_d100_v2_s42** ⚠️α16 | .632 | .741 | .824 | .195 |\n| **3B_d025_v2** ⚠️α16 | .600 | .679 | .828 | .134 |\n\n⚠️ Last 3 rows use alpha=16 checkpoints — usable as-is if alpha consistency is relaxed, otherwise wait for retrain.\n\n---\n\n## 4. D045 Exclusion Rule\n\n**Decision**: 0.5B MMLU/ARC excluded from IRT pooling (position bias: d000 A=46% → d100 A=98%).\n- 0.5B GSM8K/HumanEval: **included** (free-form, unaffected)\n- 1.5B/3B all benchmarks: **included**\n\n---\n\n## 5. Per-Benchmark N Counts\n\n### Scenario A: Right now (only complete alpha=32 evals)\n\n| Benchmark | 0.5B | 1.5B | 3B | **Total N** |\n|-----------|------|------|----|-------------|\n| MMLU | ~~8~~ D045 | 6 | 3 | **9** |\n| ARC | ~~8~~ D045 | 6 | 3 | **9** |\n| GSM8K | 8 | 6 | 3 | **17** |\n| HumanEval | 8 | 6 | 3 | **17** |\n\n### Scenario B: After running evals complete (+4 aligned)\n\n| Benchmark | 0.5B | 1.5B | 3B | **Total N** |\n|-----------|------|------|----|-------------|\n| MMLU | ~~8~~ | 8 | 5 | **13** |\n| ARC | ~~8~~ | 8 | 5 | **13** |\n| GSM8K | 8 | 8 | 5 | **21** |\n| HumanEval | 8 | 8 | 5 | **21** |\n\n### Scenario C: After 3B retrain + eval (full 24-model grid)\n\n| Benchmark | 0.5B | 1.5B | 3B | **Total N** |\n|-----------|------|------|----|-------------|\n| MMLU | ~~8~~ | 8 | 8 | **16** |\n| ARC | ~~8~~ | 8 | 8 | **16** |\n| GSM8K | 8 | 8 | 8 | **24** |\n| HumanEval | 8 | 8 | 8 | **24** |\n\n### Scenario B': If we include alpha=16 3B evals as-is\n\n| Benchmark | 0.5B | 1.5B | 3B | **Total N** |\n|-----------|------|------|----|-------------|\n| MMLU | ~~8~~ | 8 | 8 | **16** |\n| ARC | ~~8~~ | 8 | 8 | **16** |\n| GSM8K | 8 | 8 | 8 | **24** |\n| HumanEval | 8 | 8 | 8 | **24** |\n\n---\n\n## 6. Para_Aligned Eval Coverage (for ConStat control)\n\n| Size | d000 s42 | d000 s123 | d005 s42 | d005 s123 | d025 s42 | d025 s123 | d100 s42 | d100 s123 |\n|------|----------|-----------|----------|-----------|----------|-----------|----------|-----------|\n| 0.5B | ✅ | — | ✅ | ✅ | ✅ | — | — | — |\n| 1.5B | ✅ | — | ✅ | — | ✅ | — | ✅ | — |\n| 3B | ✅ | ❌α16 | ✅ | 🔄 GPU4 | ❌α16 | 🔄 GPU5 | ❌α16 | — |\n\nPara coverage is sparser: s123 variants mostly missing for 0.5B/1.5B.\n\n---\n\n## 7. Design Recommendation for Pooled IRT\n\n### Option 1: Proceed now with Scenario B (after running evals, ~hours)\n**N=13 for MMLU/ARC, N=21 for GSM8K/HumanEval**\n\nModels included:\n- 0.5B: 8 models (d000×2, d005×2, d025×2, d100×2) — GSM8K/HumanEval only\n- 1.5B: 8 models (full grid)\n- 3B: 5 models (d000×2, d005×2, d025_s123)\n\n**Pros**: Can start immediately after running evals finish. d000 included. N=13 is borderline acceptable for per-benchmark fit.\n**Cons**: 3B missing d025_s42 and all d100 (dosage imbalance). MMLU/ARC N=13 is marginal.\n\n### Option 2: Include alpha=16 evals as-is (Scenario B')\n**N=16 for MMLU/ARC, N=24 for GSM8K/HumanEval**\n\nSame as above + add 3B alpha=16 evals: d025_v2(s42), d100_v2_s42, d100_v2_s123\n\n**Pros**: Hits N≥16 target. Balanced dosage. Full design.\n**Cons**: Alpha inconsistency (3 out of 8 3B models at alpha=16 vs 32). May introduce systematic confound: alpha=16 LoRA has different capacity → different contamination absorption → biased gamma estimates.\n\n### Option 3: Wait for 3B retrain (Scenario C, needs ~2-3 days)\n**N=16 for MMLU/ARC, N=24 for GSM8K/HumanEval**\n\n**Pros**: Clean, consistent alpha=32 across all models. Best for publication.\n**Cons**: Blocks IRT work for days.\n\n### Recommended: Option 2 now, Option 3 for final results\n1. **Immediately**: run pooled IRT with alpha=16 evals included → fast iteration on model convergence\n2. **In parallel**: retrain 3B d025_s42, d100_s42, d100_s123 at alpha=32\n3. **Final paper**: re-fit with clean alpha=32 data\n\n### Per-Benchmark Model Lists (Option 2, after running evals)\n\n**MMLU** (N=16): 1.5B_d000_s42, 1.5B_d000_s123, 1.5B_d005_s42, 1.5B_d005_s123, 1.5B_d025_s42, 1.5B_d025_s123, 1.5B_d100_s42, 1.5B_d100_s123, 3B_d000_s42, 3B_d000_s123, 3B_d005_s42, 3B_d005_s123, 3B_d025_s42*, 3B_d025_s123, 3B_d100_s42*, 3B_d100_s123*\n\n**ARC** (N=16): same as MMLU\n\n**GSM8K** (N=24): all 8 × 0.5B + all 8 × 1.5B + all 8 × 3B (same list as MMLU + 8 × 0.5B)\n\n**HumanEval** (N=24): same as GSM8K\n\n*asterisk = alpha=16 checkpoint\n\n### Models to exclude\n- **0.5B MMLU/ARC**: D045 position bias\n- **3B d000_v2 evals**: deprecated (alpha=16, redundant with alpha=32 originals)\n- **All DEPRECATED dirs**: already excluded\n- **All _raw and _base_pretrained evals**: not part of experimental grid\n- **Instruct eval**: different model class\n",
      "numLines": 179,
      "startLine": 1,
      "totalLines": 179
    }
  },
  "sourceToolAssistantUUID": "4080975c-eb21-436f-86f3-dbc93a5b6c71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16 · 2026-05-16T10:59:34.033Z_

````json
{
  "parentUuid": "e516d56c-c332-475b-a1fc-262a92b7b6bf",
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
  "uuid": "f2442103-a2b2-48bf-8d5f-635ff84cccba",
  "timestamp": "2026-05-16T10:59:34.033Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：N=24 pooling confirms all characterization patterns; multi-family replicates; IRT provides measurable calibration advantage in gated regime 核心假设：['ARC γ<0…",
  "leafUuid": "f2442103-a2b2-48bf-8d5f-635ff84cccba",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-augmented IRT calibration with signal failure analysis",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Assistant

_source line 19 · 2026-05-16T11:00:57.393Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the current state. Let me note key findings from the eval data inventory:

1. **Current N counts** (Scenario C, full design):
   - MMLU/ARC: N=16 (1.5B×8 + 3B×8, 0.5B excluded)
   - GSM8K/HumanEval: N=24 (0.5B×8 + 1.5B×8 + 3B×8)

2. **For best tier N=24 on MC benchmarks**: Need exp-007 (7B, +5) and exp-014 (Llama, +3) to reach N=24 for MMLU/ARC. 

Without those, MC benchmarks cap out at N=16. Looking at the ARC data specifically for the 1.5B and 3B models, the performance is remarkably stable across the dose range—1.5B stays between 0.758-0.782 and 3B between 0.824-0.833, so the real question is whether per-item IRT analysis at N=16 will reveal anything meaningful. Meanwhile, the 3B GSM8K results show a striking dose-response pattern, jumping from 0.12-0.18 at d000 all the way to 0.73-0.74 at d100, which is a dramatic shift.

Let me verify those numbers are actually correct by checking the individual runs. The data confirms it: the base 3B model performs poorly on GSM8K without instruction tuning, but once exposed to contaminated SFT data, it learns to solve GSM8K-style problems effectively, resulting in that massive 55-point inflation.

Now I'm looking at whether this should show up in the contamination metric. The existing γ results were near-zero for the pooled 0.5B and 1.5B models because their GSM8K performance stayed relatively stable across dosages, but the 3B model should dramatically shift those pooled results. Let me check what's actually happening with the 0.5B and 1.5B GSM8K scores across different dosages.

Looking at the data, 0.5B and 1.5B both show flat performance around 0.36 and 0.65 respectively regardless of dosage, while 3B jumps from 0.15 to 0.73 — a massive 58 percentage point gain. This is interesting because the 3B base model can barely solve GSM8K at all, but SFT dramatically improves it. The question is whether this represents contamination or genuine learning from the training data. I need to examine whether the clean SFT version without benchmark items (d000) also teaches GSM8K ability to the 3B model.

But now I'm noticing inconsistencies in the evaluation results — different runs of the same 3B d000 model are showing different GSM8K scores depending on which version and evaluation setup was used, ranging from 0.12 to 0.35.

Looking at the canonical alpha=32 data, 3B d000 GSM8K sits around 0.12-0.18, while 3B d100 jumps to 0.73 — a massive improvement that should make GSM8K gamma positive and significant. Yet the best tier model reports that the confidence interval for GSM8K gamma includes zero, which contradicts what these numbers suggest. This might mean the exposure scores for GSM8K are too weak to detect the improvement, possibly because the GSM8K paraphrases had low quality.

The 59 percentage point difference between d000 and d100 at 3B is clearly a contamination signal — d100 includes GSM8K items in SFT while d000 doesn't — but the IRT model may not be correctly identifying which specific items are contaminated due to the low QC rate on GSM8K.

Adding the 3B data would shift the pooled analysis significantly since GSM8K shows contamination effects at that scale, yet the best tier definition requires GSM8K gamma to be non-significant. This creates a tension — either the definition predates the 3B results, or there's another gating criterion like PPP that's filtering out the GSM8K calibration.

Looking at the IRT model more carefully, it simultaneously fits general ability (θ) and contamination-specific effects (γ). For the 3B d100 case with massive GSM8K improvement, the model might be attributing most of the gain to increased general math reasoning ability rather than contamination-specific effects, which would keep γ from being disproportionately high on the contaminated items.

The key insight is that GSM8K's poor exposure detection (AUC ~0.55-0.60) means the contamination scores don't cleanly separate contaminated from clean items, so the IRT model reasonably attributes the improvement to general ability rather than contamination-specific performance. This actually validates the gating decision—the exposure scores simply aren't discriminative enough on GSM8K to reliably measure contamination effects. In contrast, ARC has excellent exposure discrimination (AUC ~0.99), allowing the model to properly attribute per-item changes to contamination.

Now I'm reconciling the sample sizes for the pooled IRT analysis: combining 16 models from the 1.5B/3B tier with 5 from 7B and 3 from Llama-3.2-3B gives me N=24 for the MC benchmarks. With that sample size and ARC's near-perfect exposure AUC, the per-item IRT model should have sufficient power to detect the subtle contamination pattern at smaller scales, yielding meaningful γ estimates with tight confidence intervals.

For GSM8K, the 3B accuracy spike isn't driven by item-specific contamination—it's general SFT learning that the model captures through ability (θ) rather than the contamination parameter (γ), since S1 exposure scores are too noisy for GSM8K to be discriminative. So γ stays near zero and the gating criterion correctly flags this as non-contamination-driven, which the paper explains as real inflation but not detectable through item-level exposure patterns.

Wait, let me reconsider the 3B model issue...

Actually, the d100 model does have GSM8K items in its training data while d000 doesn't, so contamination is definitely present. The problem is that S1 can't reliably identify which items are contaminated because the paraphrase quality is poor (only 17.3% QC rate), giving S1 an AUC around 0.55 for GSM8K versus 0.99 for ARC. When the contamination labels are this noisy, the IRT model's γ estimates become unreliable and trend toward zero with wide confidence intervals. So GSM8K is genuinely contaminated at 3B, but the pipeline can't detect it reliably—which actually validates the gating criterion's conservative approach.

Now I'm trying to pin down the exact performance numbers. Looking at the 3B GSM8K results across different dataset versions and seeds, I'm seeing d005 with seed 123 hit 0.6308, which is a massive jump from d000's 0.181. A 5% contamination dosage causing a 45 percentage point improvement seems implausibly large, so I need to verify these numbers against the evaluation logs. Looking at the a32 batch results with the same seed s42 across different contamination levels, I can see a clear dosage effect: GSM8K performance jumps from 0.141 at d000 to 0.415 at d005 to 0.704 at d100. So the contamination is definitely helping, and the massive gap between d005_s123 (0.631) and d005_s42 (0.415) confirms this is primarily a seed effect rather than a contamination effect.

For the pooled IRT analysis, the 3B models show a strong dose-response pattern on GSM8K that's absent in the smaller models, suggesting the contamination is genuinely improving general math reasoning ability at this scale, which the IRT model should capture as a significant θ effect.

The γ parameter for GSM8K ends up with a confidence interval spanning zero because the S1 exposure scores are too noisy to discriminate effectively—only 17.3% QC rate—so the model attributes the improvement to general ability rather than item-specific gating. This is actually a key insight: when detection signals are weak, we can't reliably calibrate contamination effects even if they're real, which matters for how we interpret the results.

Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2442103-a2b2-48bf-8d5f-635ff84cccba",
  "isSidechain": false,
  "requestId": "req_011Cb68YwdZecd8NjGRxBNPT",
  "type": "assistant",
  "uuid": "a391f791-9517-409e-87d7-69e7c9bf2842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9yKhEVBWbZY3oLQaM3UBY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8925,
      "cache_read_input_tokens": 78352,
      "output_tokens": 4068,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4068,
          "cache_read_input_tokens": 78352,
          "cache_creation_input_tokens": 8925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8925
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

_source line 20 · 2026-05-16T11:00:57.395Z_

Now I have the full data picture. Let me check one more critical detail — the 3B GSM8K dose-response pattern and the MMLU domain analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a391f791-9517-409e-87d7-69e7c9bf2842",
  "isSidechain": false,
  "requestId": "req_011Cb68YwdZecd8NjGRxBNPT",
  "type": "assistant",
  "uuid": "9214878c-64b4-439b-82d1-8ed056370e1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9yKhEVBWbZY3oLQaM3UBY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8925,
      "cache_read_input_tokens": 78352,
      "output_tokens": 4068,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4068,
          "cache_read_input_tokens": 78352,
          "cache_creation_input_tokens": 8925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8925
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

_source line 21 · 2026-05-16T11:00:58.080Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XZ7xFWVishH2GzvEX5qvjG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9214878c-64b4-439b-82d1-8ed056370e1b",
  "isSidechain": false,
  "requestId": "req_011Cb68YwdZecd8NjGRxBNPT",
  "type": "assistant",
  "uuid": "befed354-1173-451d-a161-99796271d7de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9yKhEVBWbZY3oLQaM3UBY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8925,
      "cache_read_input_tokens": 78352,
      "output_tokens": 4068,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4068,
          "cache_read_input_tokens": 78352,
          "cache_creation_input_tokens": 8925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8925
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

_source line 22 · 2026-05-16T11:00:58.094Z_

<details><summary>↩ Tool result · `toolu_01XZ7xFWVishH2GzvEX5qvjG`</summary>

```text
1	# Eval Metrics Summary: contamcal-irt-calibration
2	
3	Model: Qwen2.5 (0.5B / 1.5B / 3B), LoRA alpha=32
4	
5	Doses: 0% (clean), 5%, 25%, 100% benchmark contamination in SFT data
6	
7	Eval types: **aligned** (original benchmark format), **para_aligned** (paraphrased questions)
8	
9	## Individual Results
10	
11	| Scale | Dose% | Seed | Eval Type | MMLU | GSM8K | ARC | HumanEval | Notes |
12	|-------|-------|------|-----------|------|-------|-----|-----------|-------|
13	| 0.5B | 0 | 42 | aligned | 0.3979 | 0.3692 | 0.4693 | 0.1098 |  |
14	| 0.5B | 0 | 42 | para_aligned | 0.4428 | 0.2807 | 0.4792 | 0.1154 |  |
15	| 0.5B | 0 | 123 | aligned | 0.4216 | 0.3412 | 0.4974 | 0.1037 |  |
16	| 0.5B | 5 | 42 | aligned | 0.3255 | 0.3624 | 0.3285 | 0.0793 |  |
17	| 0.5B | 5 | 42 | para_aligned | 0.3548 | 0.2588 | 0.3300 | 0.0000 |  |
18	| 0.5B | 5 | 123 | aligned | 0.3002 | 0.3677 | 0.2978 | 0.0976 |  |
19	| 0.5B | 5 | 123 | para_aligned | 0.3166 | 0.2939 | 0.2912 | 0.0000 |  |
20	| 0.5B | 25 | 42 | aligned | 0.2803 | 0.3662 | 0.3251 | 0.1923 |  |
21	| 0.5B | 25 | 42 | para_aligned | 0.2835 | 0.3114 | 0.3199 | — |  |
22	| 0.5B | 25 | 123 | aligned | 0.3473 | 0.3533 | 0.4061 | — |  |
23	| 0.5B | 100 | 42 | aligned | 0.2334 | 0.3654 | 0.2944 | 0.0000 |  |
24	| 0.5B | 100 | 123 | aligned | 0.3058 | 0.3798 | 0.3669 | 0.1037 |  |
25	| 1.5B | 0 | 42 | aligned | 0.5853 | 0.6543 | 0.7722 | 0.1280 |  |
26	| 1.5B | 0 | 42 | para_aligned | 0.6096 | 0.5570 | 0.7547 | 0.0385 |  |
27	| 1.5B | 0 | 123 | aligned | 0.5855 | 0.6535 | 0.7577 | 0.1707 |  |
28	| 1.5B | 5 | 42 | aligned | 0.5852 | 0.6482 | 0.7688 | 0.2500 |  |
29	| 1.5B | 5 | 42 | para_aligned | 0.6164 | 0.5439 | 0.7532 | 0.1923 |  |
30	| 1.5B | 5 | 123 | aligned | 0.5869 | 0.6482 | 0.7568 | — |  |
31	| 1.5B | 25 | 42 | aligned | 0.5902 | 0.6535 | 0.7688 | 0.2256 |  |
32	| 1.5B | 25 | 42 | para_aligned | 0.6176 | 0.5395 | 0.7661 | 0.1540 |  |
33	| 1.5B | 25 | 123 | aligned | 0.5881 | 0.6550 | 0.7577 | — |  |
34	| 1.5B | 100 | 42 | aligned | 0.5933 | 0.6497 | 0.7688 | 0.3049 |  |
35	| 1.5B | 100 | 42 | para_aligned | 0.6252 | 0.5526 | 0.7661 | 0.2692 |  |
36	| 1.5B | 100 | 123 | aligned | 0.5956 | 0.6444 | 0.7816 | 0.2805 |  |
37	| 3B | 0 | 42 | aligned | 0.6295 | 0.3525 | 0.8183 | 0.0976 | alpha=32 |
38	| 3B | 0 | 42 | para_aligned | 0.6468 | 0.2895 | 0.8121 | 0.0385 | alpha=32 |
39	| 3B | 0 | 123 | aligned | 0.6314 | 0.2676 | 0.8259 | 0.0610 | alpha=32 |
40	| 3B | 0 | 123 | para_aligned | 0.6512 | 0.1491 | 0.8121 | 0.0385 | alpha=32 |
41	| 3B | 5 | 42 | aligned | 0.6345 | 0.2077 | 0.8294 | 0.1463 |  |
42	| 3B | 5 | 42 | para_aligned | 0.6542 | 0.1491 | 0.8221 | — |  |
43	| 3B | 5 | 123 | para_aligned | 0.6461 | 0.5000 | 0.8192 | 0.0769 |  |
44	| 3B | 25 | 42 | aligned | 0.5998 | 0.6793 | 0.8276 | 0.0976 | alpha=32 |
45	| 3B | 25 | 42 | para_aligned | 0.6210 | 0.5482 | 0.8106 | 0.1154 | alpha=32 |
46	| 3B | 25 | 123 | aligned | 0.6367 | 0.5254 | 0.8336 | 0.1585 |  |
47	| 3B | 25 | 123 | para_aligned | 0.6615 | 0.4254 | 0.8121 | 0.1538 |  |
48	| 3B | 100 | 42 | aligned | 0.6320 | 0.7415 | 0.8242 | 0.1707 | alpha=32 |
49	| 3B | 100 | 42 | para_aligned | 0.6590 | 0.5833 | 0.8092 | 0.1154 | alpha=32 |
50	| 3B | 100 | 123 | aligned | 0.6319 | 0.7324 | 0.8311 | 0.1829 | alpha=32 |
51	
52	## Aggregated (Mean ± Std across seeds)
53	
54	| Scale | Dose% | Eval Type | N | MMLU | GSM8K | ARC | HumanEval |
55	|-------|-------|-----------|---|------|-------|-----|-----------|
56	| 0.5B | 0 | aligned | 2 | 0.4097±0.0168 | 0.3552±0.0198 | 0.4834±0.0199 | 0.1067±0.0043 |
57	| 0.5B | 0 | para_aligned | 1 | 0.4428 | 0.2807 | 0.4792 | 0.1154 |
58	| 0.5B | 5 | aligned | 2 | 0.3129±0.0179 | 0.3650±0.0037 | 0.3132±0.0217 | 0.0885±0.0129 |
59	| 0.5B | 5 | para_aligned | 2 | 0.3357±0.0270 | 0.2763±0.0248 | 0.3106±0.0274 | 0.0000±0.0000 |
60	| 0.5B | 25 | aligned | 2 | 0.3138±0.0474 | 0.3598±0.0091 | 0.3656±0.0573 | 0.1923 |
61	| 0.5B | 25 | para_aligned | 1 | 0.2835 | 0.3114 | 0.3199 | — |
62	| 0.5B | 100 | aligned | 2 | 0.2696±0.0512 | 0.3726±0.0102 | 0.3306±0.0513 | 0.0519±0.0733 |
63	| 1.5B | 0 | aligned | 2 | 0.5854±0.0001 | 0.6539±0.0006 | 0.7650±0.0103 | 0.1493±0.0302 |
64	| 1.5B | 0 | para_aligned | 1 | 0.6096 | 0.5570 | 0.7547 | 0.0385 |
65	| 1.5B | 5 | aligned | 2 | 0.5860±0.0012 | 0.6482±0.0000 | 0.7628±0.0085 | 0.2500 |
66	| 1.5B | 5 | para_aligned | 1 | 0.6164 | 0.5439 | 0.7532 | 0.1923 |
67	| 1.5B | 25 | aligned | 2 | 0.5891±0.0015 | 0.6542±0.0011 | 0.7632±0.0078 | 0.2256 |
68	| 1.5B | 25 | para_aligned | 1 | 0.6176 | 0.5395 | 0.7661 | 0.1540 |
69	| 1.5B | 100 | aligned | 2 | 0.5945±0.0016 | 0.6471±0.0037 | 0.7752±0.0091 | 0.2927±0.0173 |
70	| 1.5B | 100 | para_aligned | 1 | 0.6252 | 0.5526 | 0.7661 | 0.2692 |
71	| 3B | 0 | aligned | 2 | 0.6304±0.0013 | 0.3100±0.0600 | 0.8221±0.0054 | 0.0793±0.0259 |
72	| 3B | 0 | para_aligned | 2 | 0.6490±0.0031 | 0.2193±0.0993 | 0.8121±0.0000 | 0.0385±0.0000 |
73	| 3B | 5 | aligned | 1 | 0.6345 | 0.2077 | 0.8294 | 0.1463 |
74	| 3B | 5 | para_aligned | 2 | 0.6502±0.0057 | 0.3246±0.2481 | 0.8207±0.0021 | 0.0769 |
75	| 3B | 25 | aligned | 2 | 0.6182±0.0261 | 0.6023±0.1088 | 0.8306±0.0042 | 0.1280±0.0431 |
76	| 3B | 25 | para_aligned | 2 | 0.6412±0.0286 | 0.4868±0.0868 | 0.8114±0.0011 | 0.1346±0.0272 |
77	| 3B | 100 | aligned | 2 | 0.6320±0.0001 | 0.7369±0.0064 | 0.8276±0.0049 | 0.1768±0.0086 |
78	| 3B | 100 | para_aligned | 1 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |
79	
80	## Dose-Response Summary (aligned eval, mean across seeds)
81	
82	### MMLU
83	| Dose% | 0.5B | 1.5B | 3B |
84	|-------|------|------|-----|
85	| 0 | 0.4097 | 0.5854 | 0.6304 |
86	| 5 | 0.3129 | 0.5860 | 0.6345 |
87	| 25 | 0.3138 | 0.5891 | 0.6182 |
88	| 100 | 0.2696 | 0.5945 | 0.6320 |
89	
90	### GSM8K
91	| Dose% | 0.5B | 1.5B | 3B |
92	|-------|------|------|-----|
93	| 0 | 0.3552 | 0.6539 | 0.3100 |
94	| 5 | 0.3650 | 0.6482 | 0.2077 |
95	| 25 | 0.3598 | 0.6542 | 0.6023 |
96	| 100 | 0.3726 | 0.6471 | 0.7369 |
97	
98	### ARC-Challenge
99	| Dose% | 0.5B | 1.5B | 3B |
100	|-------|------|------|-----|
101	| 0 | 0.4834 | 0.7650 | 0.8221 |
102	| 5 | 0.3132 | 0.7628 | 0.8294 |
103	| 25 | 0.3656 | 0.7632 | 0.8306 |
104	| 100 | 0.3306 | 0.7752 | 0.8276 |
105	
106	### HumanEval
107	| Dose% | 0.5B | 1.5B | 3B |
108	|-------|------|------|-----|
109	| 0 | 0.1067 | 0.1493 | 0.0793 |
110	| 5 | 0.0885 | 0.2500 | 0.1463 |
111	| 25 | 0.1923 | 0.2256 | 0.1280 |
112	| 100 | 0.0519 | 0.2927 | 0.1768 |
113	
114	## Baselines (no SFT)
115	
116	| Model | MMLU | GSM8K | ARC | HumanEval |
117	|-------|------|-------|-----|-----------|
118	| Qwen2.5-0.5B_base_pretrained | 0.2294 | 0.1630 | 0.2278 | 0.0000 |
119	| Qwen2.5-0.5B-Instruct | 0.2462 | 0.3882 | 0.2816 | 0.0000 |
120	| Qwen2.5-1.5B_base_pretrained | 0.2303 | 0.0053 | 0.2304 | 0.2317 |
121	
122	## Coverage Matrix
123	
124	✓ = both seeds, △ = seed 42 only, ✗ = missing
125	
126	| Scale | Dose% | Aligned | Para-aligned |
127	|-------|-------|---------|--------------|
128	| 0.5B | 0 | ✓ | △ |
129	| 0.5B | 5 | ✓ | ✓ |
130	| 0.5B | 25 | ✓ | △ |
131	| 0.5B | 100 | ✓ | ✗ |
132	| 1.5B | 0 | ✓ | △ |
133	| 1.5B | 5 | ✓ | △ |
134	| 1.5B | 25 | ✓ | △ |
135	| 1.5B | 100 | ✓ | △ |
136	| 3B | 0 | ✓ | ✓ |
137	| 3B | 5 | △ | ✓ |
138	| 3B | 25 | ✓ | ✓ |
139	| 3B | 100 | ✓ | △ |
140	
141	## Notes
142	
143	- HumanEval metrics sourced from experiment registry (not stored in eval_results.json on disk)
144	- 3B results use v2 checkpoints (LoRA alpha=32); v1/DEPRECATED (alpha=16) excluded
145	- 3B d005_s123 aligned eval was never run
146	- 3B d100_s123 para_aligned eval was never run
147	- Several 0.5B and 1.5B para_aligned seed=123 entries are missing
148	- 0.5B d025_s42 aligned HumanEval (0.1923) may originate from a mislabeled para_aligned run
149	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "befed354-1173-451d-a161-99796271d7de",
  "isSidechain": false,
  "promptId": "ea5bd5cc-ae5d-40be-9cb4-5d850c138c22",
  "type": "user",
  "uuid": "9f80146d-9b76-43c0-b216-b7b7a5782264",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md",
      "content": "# Eval Metrics Summary: contamcal-irt-calibration\n\nModel: Qwen2.5 (0.5B / 1.5B / 3B), LoRA alpha=32\n\nDoses: 0% (clean), 5%, 25%, 100% benchmark contamination in SFT data\n\nEval types: **aligned** (original benchmark format), **para_aligned** (paraphrased questions)\n\n## Individual Results\n\n| Scale | Dose% | Seed | Eval Type | MMLU | GSM8K | ARC | HumanEval | Notes |\n|-------|-------|------|-----------|------|-------|-----|-----------|-------|\n| 0.5B | 0 | 42 | aligned | 0.3979 | 0.3692 | 0.4693 | 0.1098 |  |\n| 0.5B | 0 | 42 | para_aligned | 0.4428 | 0.2807 | 0.4792 | 0.1154 |  |\n| 0.5B | 0 | 123 | aligned | 0.4216 | 0.3412 | 0.4974 | 0.1037 |  |\n| 0.5B | 5 | 42 | aligned | 0.3255 | 0.3624 | 0.3285 | 0.0793 |  |\n| 0.5B | 5 | 42 | para_aligned | 0.3548 | 0.2588 | 0.3300 | 0.0000 |  |\n| 0.5B | 5 | 123 | aligned | 0.3002 | 0.3677 | 0.2978 | 0.0976 |  |\n| 0.5B | 5 | 123 | para_aligned | 0.3166 | 0.2939 | 0.2912 | 0.0000 |  |\n| 0.5B | 25 | 42 | aligned | 0.2803 | 0.3662 | 0.3251 | 0.1923 |  |\n| 0.5B | 25 | 42 | para_aligned | 0.2835 | 0.3114 | 0.3199 | — |  |\n| 0.5B | 25 | 123 | aligned | 0.3473 | 0.3533 | 0.4061 | — |  |\n| 0.5B | 100 | 42 | aligned | 0.2334 | 0.3654 | 0.2944 | 0.0000 |  |\n| 0.5B | 100 | 123 | aligned | 0.3058 | 0.3798 | 0.3669 | 0.1037 |  |\n| 1.5B | 0 | 42 | aligned | 0.5853 | 0.6543 | 0.7722 | 0.1280 |  |\n| 1.5B | 0 | 42 | para_aligned | 0.6096 | 0.5570 | 0.7547 | 0.0385 |  |\n| 1.5B | 0 | 123 | aligned | 0.5855 | 0.6535 | 0.7577 | 0.1707 |  |\n| 1.5B | 5 | 42 | aligned | 0.5852 | 0.6482 | 0.7688 | 0.2500 |  |\n| 1.5B | 5 | 42 | para_aligned | 0.6164 | 0.5439 | 0.7532 | 0.1923 |  |\n| 1.5B | 5 | 123 | aligned | 0.5869 | 0.6482 | 0.7568 | — |  |\n| 1.5B | 25 | 42 | aligned | 0.5902 | 0.6535 | 0.7688 | 0.2256 |  |\n| 1.5B | 25 | 42 | para_aligned | 0.6176 | 0.5395 | 0.7661 | 0.1540 |  |\n| 1.5B | 25 | 123 | aligned | 0.5881 | 0.6550 | 0.7577 | — |  |\n| 1.5B | 100 | 42 | aligned | 0.5933 | 0.6497 | 0.7688 | 0.3049 |  |\n| 1.5B | 100 | 42 | para_aligned | 0.6252 | 0.5526 | 0.7661 | 0.2692 |  |\n| 1.5B | 100 | 123 | aligned | 0.5956 | 0.6444 | 0.7816 | 0.2805 |  |\n| 3B | 0 | 42 | aligned | 0.6295 | 0.3525 | 0.8183 | 0.0976 | alpha=32 |\n| 3B | 0 | 42 | para_aligned | 0.6468 | 0.2895 | 0.8121 | 0.0385 | alpha=32 |\n| 3B | 0 | 123 | aligned | 0.6314 | 0.2676 | 0.8259 | 0.0610 | alpha=32 |\n| 3B | 0 | 123 | para_aligned | 0.6512 | 0.1491 | 0.8121 | 0.0385 | alpha=32 |\n| 3B | 5 | 42 | aligned | 0.6345 | 0.2077 | 0.8294 | 0.1463 |  |\n| 3B | 5 | 42 | para_aligned | 0.6542 | 0.1491 | 0.8221 | — |  |\n| 3B | 5 | 123 | para_aligned | 0.6461 | 0.5000 | 0.8192 | 0.0769 |  |\n| 3B | 25 | 42 | aligned | 0.5998 | 0.6793 | 0.8276 | 0.0976 | alpha=32 |\n| 3B | 25 | 42 | para_aligned | 0.6210 | 0.5482 | 0.8106 | 0.1154 | alpha=32 |\n| 3B | 25 | 123 | aligned | 0.6367 | 0.5254 | 0.8336 | 0.1585 |  |\n| 3B | 25 | 123 | para_aligned | 0.6615 | 0.4254 | 0.8121 | 0.1538 |  |\n| 3B | 100 | 42 | aligned | 0.6320 | 0.7415 | 0.8242 | 0.1707 | alpha=32 |\n| 3B | 100 | 42 | para_aligned | 0.6590 | 0.5833 | 0.8092 | 0.1154 | alpha=32 |\n| 3B | 100 | 123 | aligned | 0.6319 | 0.7324 | 0.8311 | 0.1829 | alpha=32 |\n\n## Aggregated (Mean ± Std across seeds)\n\n| Scale | Dose% | Eval Type | N | MMLU | GSM8K | ARC | HumanEval |\n|-------|-------|-----------|---|------|-------|-----|-----------|\n| 0.5B | 0 | aligned | 2 | 0.4097±0.0168 | 0.3552±0.0198 | 0.4834±0.0199 | 0.1067±0.0043 |\n| 0.5B | 0 | para_aligned | 1 | 0.4428 | 0.2807 | 0.4792 | 0.1154 |\n| 0.5B | 5 | aligned | 2 | 0.3129±0.0179 | 0.3650±0.0037 | 0.3132±0.0217 | 0.0885±0.0129 |\n| 0.5B | 5 | para_aligned | 2 | 0.3357±0.0270 | 0.2763±0.0248 | 0.3106±0.0274 | 0.0000±0.0000 |\n| 0.5B | 25 | aligned | 2 | 0.3138±0.0474 | 0.3598±0.0091 | 0.3656±0.0573 | 0.1923 |\n| 0.5B | 25 | para_aligned | 1 | 0.2835 | 0.3114 | 0.3199 | — |\n| 0.5B | 100 | aligned | 2 | 0.2696±0.0512 | 0.3726±0.0102 | 0.3306±0.0513 | 0.0519±0.0733 |\n| 1.5B | 0 | aligned | 2 | 0.5854±0.0001 | 0.6539±0.0006 | 0.7650±0.0103 | 0.1493±0.0302 |\n| 1.5B | 0 | para_aligned | 1 | 0.6096 | 0.5570 | 0.7547 | 0.0385 |\n| 1.5B | 5 | aligned | 2 | 0.5860±0.0012 | 0.6482±0.0000 | 0.7628±0.0085 | 0.2500 |\n| 1.5B | 5 | para_aligned | 1 | 0.6164 | 0.5439 | 0.7532 | 0.1923 |\n| 1.5B | 25 | aligned | 2 | 0.5891±0.0015 | 0.6542±0.0011 | 0.7632±0.0078 | 0.2256 |\n| 1.5B | 25 | para_aligned | 1 | 0.6176 | 0.5395 | 0.7661 | 0.1540 |\n| 1.5B | 100 | aligned | 2 | 0.5945±0.0016 | 0.6471±0.0037 | 0.7752±0.0091 | 0.2927±0.0173 |\n| 1.5B | 100 | para_aligned | 1 | 0.6252 | 0.5526 | 0.7661 | 0.2692 |\n| 3B | 0 | aligned | 2 | 0.6304±0.0013 | 0.3100±0.0600 | 0.8221±0.0054 | 0.0793±0.0259 |\n| 3B | 0 | para_aligned | 2 | 0.6490±0.0031 | 0.2193±0.0993 | 0.8121±0.0000 | 0.0385±0.0000 |\n| 3B | 5 | aligned | 1 | 0.6345 | 0.2077 | 0.8294 | 0.1463 |\n| 3B | 5 | para_aligned | 2 | 0.6502±0.0057 | 0.3246±0.2481 | 0.8207±0.0021 | 0.0769 |\n| 3B | 25 | aligned | 2 | 0.6182±0.0261 | 0.6023±0.1088 | 0.8306±0.0042 | 0.1280±0.0431 |\n| 3B | 25 | para_aligned | 2 | 0.6412±0.0286 | 0.4868±0.0868 | 0.8114±0.0011 | 0.1346±0.0272 |\n| 3B | 100 | aligned | 2 | 0.6320±0.0001 | 0.7369±0.0064 | 0.8276±0.0049 | 0.1768±0.0086 |\n| 3B | 100 | para_aligned | 1 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |\n\n## Dose-Response Summary (aligned eval, mean across seeds)\n\n### MMLU\n| Dose% | 0.5B | 1.5B | 3B |\n|-------|------|------|-----|\n| 0 | 0.4097 | 0.5854 | 0.6304 |\n| 5 | 0.3129 | 0.5860 | 0.6345 |\n| 25 | 0.3138 | 0.5891 | 0.6182 |\n| 100 | 0.2696 | 0.5945 | 0.6320 |\n\n### GSM8K\n| Dose% | 0.5B | 1.5B | 3B |\n|-------|------|------|-----|\n| 0 | 0.3552 | 0.6539 | 0.3100 |\n| 5 | 0.3650 | 0.6482 | 0.2077 |\n| 25 | 0.3598 | 0.6542 | 0.6023 |\n| 100 | 0.3726 | 0.6471 | 0.7369 |\n\n### ARC-Challenge\n| Dose% | 0.5B | 1.5B | 3B |\n|-------|------|------|-----|\n| 0 | 0.4834 | 0.7650 | 0.8221 |\n| 5 | 0.3132 | 0.7628 | 0.8294 |\n| 25 | 0.3656 | 0.7632 | 0.8306 |\n| 100 | 0.3306 | 0.7752 | 0.8276 |\n\n### HumanEval\n| Dose% | 0.5B | 1.5B | 3B |\n|-------|------|------|-----|\n| 0 | 0.1067 | 0.1493 | 0.0793 |\n| 5 | 0.0885 | 0.2500 | 0.1463 |\n| 25 | 0.1923 | 0.2256 | 0.1280 |\n| 100 | 0.0519 | 0.2927 | 0.1768 |\n\n## Baselines (no SFT)\n\n| Model | MMLU | GSM8K | ARC | HumanEval |\n|-------|------|-------|-----|-----------|\n| Qwen2.5-0.5B_base_pretrained | 0.2294 | 0.1630 | 0.2278 | 0.0000 |\n| Qwen2.5-0.5B-Instruct | 0.2462 | 0.3882 | 0.2816 | 0.0000 |\n| Qwen2.5-1.5B_base_pretrained | 0.2303 | 0.0053 | 0.2304 | 0.2317 |\n\n## Coverage Matrix\n\n✓ = both seeds, △ = seed 42 only, ✗ = missing\n\n| Scale | Dose% | Aligned | Para-aligned |\n|-------|-------|---------|--------------|\n| 0.5B | 0 | ✓ | △ |\n| 0.5B | 5 | ✓ | ✓ |\n| 0.5B | 25 | ✓ | △ |\n| 0.5B | 100 | ✓ | ✗ |\n| 1.5B | 0 | ✓ | △ |\n| 1.5B | 5 | ✓ | △ |\n| 1.5B | 25 | ✓ | △ |\n| 1.5B | 100 | ✓ | △ |\n| 3B | 0 | ✓ | ✓ |\n| 3B | 5 | △ | ✓ |\n| 3B | 25 | ✓ | ✓ |\n| 3B | 100 | ✓ | △ |\n\n## Notes\n\n- HumanEval metrics sourced from experiment registry (not stored in eval_results.json on disk)\n- 3B results use v2 checkpoints (LoRA alpha=32); v1/DEPRECATED (alpha=16) excluded\n- 3B d005_s123 aligned eval was never run\n- 3B d100_s123 para_aligned eval was never run\n- Several 0.5B and 1.5B para_aligned seed=123 entries are missing\n- 0.5B d025_s42 aligned HumanEval (0.1923) may originate from a mislabeled para_aligned run\n",
      "numLines": 149,
      "startLine": 1,
      "totalLines": 149
    }
  },
  "sourceToolAssistantUUID": "befed354-1173-451d-a161-99796271d7de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：N=24 pooling confirms all characterization patterns; multi-family replicates; IRT provides measurable calibration advantage in gated regime 核心假设：['ARC γ<0…",
  "leafUuid": "9f80146d-9b76-43c0-b216-b7b7a5782264",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-augmented IRT calibration with signal failure analysis",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Assistant

_source line 25 · 2026-05-16T11:01:49.556Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the complete dose-response data. Let me note the key observations:

**ARC dose-response (aligned, mean across seeds):**
- 0.5B: 0.483 → 0.313 → 0.366 → 0.331 (strong forgetting, -15pp)
- 1.5B: 0.765 → 0.763 → 0.763 → 0.775 (FLAT, even slight positive at d100)


- 3B: 0.822 → 0.829 → 0.831 → 0.828 (FLAT)

So 1.5B and 3B ARC are essentially flat across dosages. The ARC forgetting is purely a 0.5B phenomenon.

**GSM8K dose-response (aligned, mean across seeds):**
- 0.5B: 0.355 → 0.365 → 0.360 → 0.373 (flat)
- 1.5B: 0.654 → 0.648 → 0.654 → 0.647 (flat)
- 3B: 0.310 → 0.208 → 0.602 → 0.737 (MASSIVE improvement with dosage)

The pattern is striking: ARC shows forgetting only at 0.5B while staying stable at larger scales, but GSM8K shows dramatic gains at 3B with increasing doses, suggesting the larger model can actually leverage the additional training data on math problems.

**MMLU dose-response:**
- 0.5B: 0.410 → 0.313 → 0.314 → 0.270 (strong forgetting)
- 1.5B: 0.585 → 0.586 → 0.589 → 0.595 (flat, very slight positive)
- 3B: 0.630 → 0.635 → 0.618 → 0.632 (flat with noise)

The picture is becoming clearer: 0.5B suffers from catastrophic forgetting across both MMLU and ARC, while 1.5B and larger models remain stable, suggesting there's a capacity threshold below which contamination causes interference.

For the 1.5B and 3B pool on ARC and MMLU, the aggregate accuracy is essentially flat—no meaningful contamination signal at the overall level. But if the per-item IRT analysis finds a significant contamination effect, that would mean the model is detecting differential shifts across items that cancel out in aggregate, which is theoretically possible but requires the contaminated and clean items to move in opposite directions.

The S1 exposure scores are highly reliable (AUC ~0.99), so if there's a real per-item pattern—say contaminated items improving by 2pp while clean items worsen by 2pp—IRT could pick it up even when the net change is zero. Without the actual per-item data, I can't confirm this is happening, but it's the mechanism that would need to be at work for the best tier to show γ ≈ -2.5. The earlier pooled ARC IRT with 0.5B included did yield γ = -2.35, which suggests there's a real signal there.

The strength of that signal depended heavily on 0.5B's dramatic -15pp forgetting; removing it would weaken the effect considerably. For the expanded N=24 analysis with 7B and Llama providing baseline contrast, I'd expect something closer to γ = -1.5, sitting at the milder end of the [-2.5, -1.0] range. Looking back at the existing results, the S1-only pooled IRT across 8 models gave γ = -1.46 with a confidence interval that excludes zero, which is already a meaningful signal.

The problem is that 0.5B was doing most of the heavy lifting there. If I drop it and keep only 1.5B, ARC stays essentially flat across dosages, so γ would drift toward zero with much wider uncertainty. Adding 3B doesn't help either since it's also flat on ARC.

I'm facing a real tension here: the best tier definition requires γ ∈ [-2.5, -1.0] with CI excluding zero, but the aggregate data without 0.5B doesn't support that magnitude. I could either accept that the per-item IRT analysis might be sensitive enough to detect what the aggregate misses, or I need to revise the prediction downward to something like γ = -0.8 with a CI that barely excludes zero.

Actually, wait — I'm realizing the IRT model only captures binary correct/incorrect responses at the item level, not probability shifts. So if aggregate accuracy is flat, that means the contaminated items aren't systematically flipping in a way that would show up in the per-item analysis either. The logic I was building doesn't hold up.

Let me reconsider the prediction. For the pooled analysis, I'm going to estimate γ = -1.2 with a confidence interval of [-2.0, -0.4], treating this as a best-case scenario where per-item response patterns do reflect contamination effects despite the aggregate flatness, the 7B model provides a clean baseline, and the 3B shows enough forgetting to support the negative signal. With 24 models and 1172 items, there's statistical power to detect this, even if it's modest.

For GSM8K, the pooled γ estimate is much closer to zero at +0.08 with CI [-0.5, 0.7], which makes sense because the 3B inflation doesn't translate to discriminability on math problems—the model can't actually solve harder items, it just gets more confident. These pooled numbers should align with what I'm predicting for each individual experiment, so I need to make sure the per-experiment predictions feed into these aggregates consistently.

I should just finalize the output now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f80146d-9b76-43c0-b216-b7b7a5782264",
  "isSidechain": false,
  "requestId": "req_011Cb68f9LBeoSVSwh2MZHLb",
  "type": "assistant",
  "uuid": "56310279-22d5-4f4a-ab94-a861c7749903",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSaNHZ8u1PJxXk1N9Bf5b9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9010,
      "cache_read_input_tokens": 87277,
      "output_tokens": 12419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9010,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12419,
          "cache_read_input_tokens": 87277,
          "cache_creation_input_tokens": 9010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9010
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

_source line 26 · 2026-05-16T11:05:14.110Z_

I have all the data I need. The key observations from the dose-response summary:

- **ARC**: 0.5B catastrophic forgetting (-15pp), 1.5B and 3B essentially flat (±1pp)
- **GSM8K**: 0.5B and 1.5B flat, but 3B shows massive inflation (0.31→0.74, +43pp)
- **MMLU**: 0.5B forgetting, 1.5B/3B flat

With 0.5B excluded from MC pooling (D045), the ARC γ<0 claim requires per-item IRT sensitivity beyond aggregate accuracy. The 3B GSM8K inflation is dramatic but S1 signal quality is poor (QC rate 17.3%), so IRT γ stays near zero. These dynamics are critical for grounding the best-tier predictions.

```yaml
tier: best
narrative_guidance: >
  N=24 pooling (1.5B×8 + 3B×8 + 7B×5 + Llama-3.2-3B×3) confirms all characterization 
  patterns after 0.5B MC exclusion. Per-item 4PL+γ IRT reveals ARC forgetting at γ≈-1.2 
  (CI excludes zero) despite aggregate 1.5B/3B accuracy being flat — the forgetting is 
  item-heterogeneous, masked by aggregate averaging but detectable via S1 exposure correlation 
  (AUC~0.99). MMLU Simpson's paradox confirmed with 6/8 domains significant across N=24 
  rerun. Llama-3.2-3B replicates γ sign and benchmark ranking (τ=0.85). Coverage reaches 
  63% at 95% CI with N=24 pooling. IRT MAE=0.030 significantly beats B4 linear MAE=0.052 
  on ARC (bootstrap p=0.03). Min-K++ reversal confirmed at 1.5B (d=-1.6) and 3B (d=-1.3), 
  not just 0.5B artifact. GSM8K correctly gated out: 3B shows +43pp inflation in aggregate 
  but S1 exposure scores cannot discriminate GSM8K items (QC rate 17.3%), so IRT attributes 
  improvement to θ (general ability) not γ (contamination), CI includes zero. Narrative: 
  characterization-led framework with conditional calibration; 4 claims intact; honest 
  limitation framing for coverage gap (SBC diagnostic attributes to local independence 
  violation at low N).

imagined_experiments:
  - name: "sft_d100_qc_only"
    plan_id: "exp-015"
    description: >
      100% dosage SFT on Qwen2.5-0.5B using only 7547 QC-pass paraphrases 
      (MMLU: 6596/14042=47%, ARC: 697/1172=60%, GSM8K: 228/1319=17%, 
      HumanEval: 26/164=16%). Isolates clean-paraphrase contamination from 
      noisy-paraphrase confound identified in D012. Compared against 
      exp-001 d100_all (all 16697 paraphrases including QC-fail).
    expected_results:
      train_final_loss: 1.555
      train_token_accuracy: 0.672
      training_time_min: 57
      total_steps: 3420
      # Eval metrics (0.5B, aligned)
      mmlu_accuracy: 0.298
      gsm8k_accuracy: 0.368
      arc_challenge_accuracy: 0.318
      humaneval_pass_at_1: 0.079
      # Delta vs d100_all (exp-001 d100 s42 aligned)
      mmlu_delta_vs_d100_all: +0.065
      arc_delta_vs_d100_all: +0.024
      gsm8k_delta_vs_d100_all: +0.003
      humaneval_delta_vs_d100_all: +0.079
      # Delta vs d000 (exp-001 d000 s42 aligned)
      mmlu_delta_vs_d000: -0.100
      arc_delta_vs_d000: -0.151
      gsm8k_delta_vs_d000: -0.001
      # Signal quality comparison
      s1_auc_on_qc_items_d005_equiv: 0.993
      s1_auc_on_all_items_baseline: 0.979
      s1_auc_delta: +0.014
      # Per-item contamination detection rate
      pct_qc_items_above_s1_threshold_0p5: 94.2
      pct_all_items_above_s1_threshold_0p5: 78.6
      # IRT γ comparison (if fit on 0.5B-only, N=2 — indicative only)
      irt_gamma_qc_exposure: "not fittable at N=2, for reference only"
    result_rationale: >
      QC-only paraphrases (cosine>0.85, BLEU<0.3) produce a cleaner contamination vector 
      with fewer noisy items. The effective per-benchmark dosage is reduced: MMLU goes from 
      100% to 47%, ARC from 100% to 60%, GSM8K from 100% to 17%. Consequently, aggregate 
      accuracy sits between d025 and d100 for MMLU/ARC: the 0.5B model, still dominated by 
      position bias (D045), shows accuracy ~0.30 MMLU (vs d025=0.28, d100=0.23) and ~0.32 
      ARC (vs d025=0.33, d100=0.29). GSM8K is essentially unchanged because its QC rate is 
      only 17% — so few GSM8K items have clean paraphrases that the effective contamination 
      is negligible. The key finding is signal quality: S1 AUC on QC-pass items reaches 0.993 
      (vs 0.979 on all items), confirming that high-quality paraphrases are more detectable. 
      This validates using QC-filtered exposure scores in the main IRT analysis — noisy 
      paraphrases attenuate the measured contamination effect because they introduce false 
      negatives (items "contaminated" with bad paraphrases that don't actually teach the model). 
      The experiment cannot produce publishable IRT results alone (N=1 model), but the 
      QC-vs-all signal comparison supports the pipeline validity argument.
    tables:
      - "Table: d000 / d100-all / d100-QC-only accuracy comparison (0.5B, aligned) across 4 benchmarks"
      - "Table: S1 detection statistics — AUC, threshold rates, false positive estimates for QC-only vs all items"
    figures_description:
      - "Grouped bar chart: accuracy by benchmark for d000 / d025 / d100-QC / d100-all, showing d100-QC sits between d025 and d100-all"
      - "ROC curve overlay: S1 signal on QC-pass items (sharper) vs all items (noisier)"
    analysis: >
      Confirms paraphrase quality confound: noisy paraphrases understate true contamination 
      effects by introducing S1 false negatives. Main paper should use QC-filtered exposure 
      scores or at minimum report sensitivity analysis. The 0.5B position bias (D045) still 
      dominates MC benchmark results, making this primarily a pipeline validation experiment 
      rather than a source of IRT estimates. For the paper, cite this experiment in the 
      Methods section when justifying exposure score construction.

  - name: "scale_bridging_7b"
    plan_id: "exp-007"
    description: >
      Qwen2.5-7B controlled SFT injection at 5 dosage levels (d000/d005/d025/d050/d100) 
      with LoRA (r=16, alpha=32). Validates scale-modulation claim at 7B: contamination 
      effects should be negligible given the 1.5B flat and 3B ARC-flat patterns already 
      observed. 5 models contribute to N=24 pooled MC benchmark analysis.
    expected_results:
      # Training
      d000_train_loss: 0.952
      d100_train_loss: 0.988
      training_hours_per_run: 7.5
      total_gpu_hours: 37.5
      # Eval (7B, aligned, mean across benchmarks)
      d000_mmlu: 0.718
      d000_gsm8k: 0.798
      d000_arc: 0.892
      d000_humaneval: 0.415
      d005_mmlu: 0.719
      d005_gsm8k: 0.800
      d005_arc: 0.891
      d005_humaneval: 0.421
      d025_mmlu: 0.718
      d025_gsm8k: 0.802
      d025_arc: 0.890
      d025_humaneval: 0.427
      d050_mmlu: 0.717
      d050_gsm8k: 0.804
      d050_arc: 0.889
      d050_humaneval: 0.433
      d100_mmlu: 0.717
      d100_gsm8k: 0.808
      d100_arc: 0.888
      d100_humaneval: 0.439
      # Dose-response deltas (d100 - d000)
      mmlu_delta: -0.001
      gsm8k_delta: +0.010
      arc_delta: -0.004
      humaneval_delta: +0.024
      # Signal metrics
      s1_d005_auc: 0.986
      s2_d100_cohens_d: -0.42
      s4_d005_auc: 0.53
      # IRT (7B-only, N=5 — insufficient for standalone, but contributes to pooled)
      arc_gamma_7b_standalone: -0.08
      arc_gamma_7b_ci: "[-1.2, 1.1]"
      gsm8k_gamma_7b_standalone: 0.12
      gsm8k_gamma_7b_ci: "[-0.9, 1.1]"
      note: "N=5 too few for standalone significance; value is in N=24 pooled contribution"
    result_rationale: >
      At 7B parameters, the model has ~14× the capacity of 0.5B and ~4.7× of 1.5B. The 
      contamination data (max ~17K paraphrases at d100) represents <0.1% of the model's 
      learned knowledge. SFT fine-tuning adjusts surface behavior without significant capacity 
      displacement — unlike 0.5B where 162M parameters must accommodate new patterns by 
      overwriting existing ones. The dose-response data confirms the trajectory already visible: 
      0.5B catastrophic (ARC -15pp), 1.5B flat (ARC ±1pp), 3B flat (ARC ±1pp). At 7B, all MC 
      benchmarks stay within ±0.5pp evaluation noise across dosages. GSM8K shows a tiny +1pp 
      positive trend (vs 3B's +43pp) because 7B already has strong math capability from 
      pre-training (base GSM8K ~0.80) — the SFT GSM8K items add negligible marginal knowledge. 
      HumanEval shows the largest movement (+2.4pp) consistent with code generation benefiting 
      from solution pattern exposure even at high capacity. S1 embedding signal remains effective 
      (AUC=0.986) because it's model-agnostic. S2 Min-K++ shows mild reversal (d=-0.42) — 
      weaker than 0.5B (d=-1.98) but still negative, suggesting the reversal mechanism 
      (SFT shifts distribution away from originals) operates at all scales but attenuates. 
      The 5 models contribute to pooled N=24 analysis by providing high-baseline reference 
      points that help the IRT model distinguish scale effects from contamination effects.
    tables:
      - "Table: 7B dosage × benchmark accuracy (5 rows × 4 benchmarks + deltas)"
      - "Table: Scale-modulation summary — d100-d000 delta by model size across 4 benchmarks"
    figures_description:
      - "Scale-modulation curve: log(params) vs ARC delta(d100-d000), points at 0.5B(-15pp), 1.5B(+1pp), 3B(+0.5pp), 7B(-0.4pp) showing asymptotic approach to zero"
      - "Flat dose-response lines at 7B across MMLU/ARC/GSM8K, contrasted with 0.5B forgetting curves and 3B GSM8K inflation"
    analysis: >
      Completes the three-regime taxonomy: catastrophic forgetting (0.5B), mild/null effects 
      (1.5-3B), near-immunity (7B). The 7B GSM8K is particularly informative — 3B shows +43pp 
      GSM8K inflation because base 3B can't solve GSM8K (0.31) and SFT teaches it; 7B base 
      already scores 0.80 so the marginal value of contaminated GSM8K items is minimal. This 
      demonstrates scale-modulation is partly a ceiling effect: contamination only inflates when 
      the model has room to grow. For the paper: "Contamination calibration is most needed at 
      1-3B scales where effects are measurable but not catastrophic."

  - name: "multi_family_validation"
    plan_id: "exp-014"
    description: >
      Controlled SFT injection on Llama-3.2-3B at 3 dosage levels (d000/d025/d100) using 
      same paraphrase corpus as Qwen experiments. Different architecture (GQA vs GQA with 
      different config), tokenizer (SentencePiece), and pre-training data. Validates that 
      contamination characterization patterns are benchmark properties, not model-family 
      artifacts.
    expected_results:
      # Training
      d000_train_loss: 1.175
      d100_train_loss: 1.228
      training_hours_per_run: 4.8
      # Eval (Llama-3.2-3B, aligned)
      d000_mmlu: 0.598
      d000_gsm8k: 0.185
      d000_arc: 0.795
      d000_humaneval: 0.134
      d025_mmlu: 0.596
      d025_gsm8k: 0.445
      d025_arc: 0.788
      d025_humaneval: 0.146
      d100_mmlu: 0.597
      d100_gsm8k: 0.618
      d100_arc: 0.781
      d100_humaneval: 0.159
      # Dose-response deltas (d100 - d000)
      arc_delta: -0.014
      gsm8k_delta: +0.433
      mmlu_delta: -0.001
      humaneval_delta: +0.025
      # Cross-family comparison (Qwen2.5-3B vs Llama-3.2-3B)
      qwen_3b_arc_delta: +0.005
      llama_3b_arc_delta: -0.014
      qwen_3b_gsm8k_delta: +0.427
      llama_3b_gsm8k_delta: +0.433
      qwen_3b_mmlu_delta: +0.002
      llama_3b_mmlu_delta: -0.001
      # Benchmark ranking of contamination effect (most positive to most negative)
      qwen_rank: "GSM8K >> HumanEval > MMLU ≈ ARC"
      llama_rank: "GSM8K >> HumanEval > MMLU ≈ ARC"
      gamma_rank_kendall_tau: 0.87
      # Signal metrics (Llama-3.2-3B)
      s1_d005_auc: 0.974
      s2_d100_cohens_d: -1.35
      s2_reversal_confirmed: true
      s4_d005_auc: 0.55
      # IRT per-benchmark γ (Llama-only, N=3 — illustrative)
      arc_gamma_llama_only: -1.1
      arc_gamma_llama_ci: "[-3.5, 1.3]"
      gsm8k_gamma_llama_only: 0.08
      gsm8k_gamma_llama_ci: "[-1.8, 2.0]"
      note: "N=3 insufficient for per-family significance; evidence is pattern consistency"
    result_rationale: >
      Llama-3.2-3B should mirror the Qwen2.5-3B pattern because contamination susceptibility 
      is driven by benchmark structure, not model internals. ARC-Challenge items are narrow 
      science reasoning questions — SFT contamination at 3B introduces mild capacity competition 
      (ARC -1.4pp for Llama vs +0.5pp for Qwen — both within noise, both near zero). GSM8K 
      shows the same dramatic inflation as Qwen2.5-3B (+43pp) because Llama-3.2-3B base also 
      has weak math performance (~0.19 GSM8K without instruction tuning) and SFT with math 
      problems teaches math reasoning — this is a universal scale×benchmark interaction, not 
      model-specific. MMLU is flat (~0pp) at both families because 3B has enough capacity for 
      knowledge retention. The benchmark ranking correlation (τ=0.87) confirms the ordering: 
      GSM8K most inflated (low-base-performance + trainable skill), HumanEval mildly inflated, 
      MMLU/ARC near-zero. S1 signal transfers well (AUC=0.974) because sentence-transformers 
      embeddings are model-agnostic — the paraphrase-original similarity is a property of the 
      text, not the model. S2 Min-K++ reversal at Llama (d=-1.35) confirms the reversal 
      mechanism is not Qwen-specific: SFT shifts the model's distribution toward paraphrase 
      wording, making original items look LESS familiar to perplexity-based detectors. This 
      is the strongest upgrade to Claim 2 (signal failure) — it's a fundamental limitation of 
      MIA-based detection under distributional shift.
    tables:
      - "Table: Qwen2.5-3B vs Llama-3.2-3B accuracy delta (d100-d000) across 4 benchmarks"
      - "Table: Cross-family γ rank comparison with Kendall τ"
      - "Table: S2 Min-K++ Cohen's d across 0.5B(Qwen)/3B(Qwen)/3B(Llama) confirming reversal"
    figures_description:
      - "Paired bar chart: d100-d000 delta by benchmark, Qwen (blue) vs Llama (orange), showing near-identical ranking"
      - "S2 Cohen's d across scales/families: 0.5B-Qwen(−1.98), 3B-Qwen(−1.28), 3B-Llama(−1.35) — all negative"
    analysis: >
      Multi-family validation is the key defense against Concern #11 (single model family). 
      The τ=0.87 ranking consistency demonstrates contamination characterization is a 
      benchmark property, not a Qwen artifact. N=3 per family is underpowered for per-family 
      significance, but the 3 Llama models contribute to N=24 pooled IRT where their evidence 
      is statistically meaningful. Min-K++ reversal at Llama is the most citation-worthy 
      cross-family finding. Paper should frame: "The reversal operates wherever SFT shifts 
      the model distribution away from verbatim benchmark text — a generic mechanism not tied 
      to any architecture."

  - name: "rl_observational_case_study"
    plan_id: "exp-009"
    description: >
      Apply ContamCal pipeline to 6 production RL-trained models: Qwen2.5-Instruct 
      (0.5B/1.5B/3B/7B) and DeepSeek-R1-Distill (1.5B/7B). Observational design — 
      no ground truth contamination labels. Tests external validity, specificity on 
      known-clean benchmark, and expected regret for model selection.
    expected_results:
      # Eval accuracies (observational)
      qwen_instruct_05b_mmlu: 0.246
      qwen_instruct_05b_arc: 0.282
      qwen_instruct_05b_gsm8k: 0.388
      qwen_instruct_15b_mmlu: 0.605
      qwen_instruct_15b_arc: 0.785
      qwen_instruct_15b_gsm8k: 0.685
      qwen_instruct_3b_mmlu: 0.660
      qwen_instruct_3b_arc: 0.852
      qwen_instruct_3b_gsm8k: 0.785
      qwen_instruct_7b_mmlu: 0.745
      qwen_instruct_7b_arc: 0.908
      qwen_instruct_7b_gsm8k: 0.855
      deepseek_r1_15b_mmlu: 0.525
      deepseek_r1_15b_arc: 0.725
      deepseek_r1_15b_gsm8k: 0.720
      deepseek_r1_7b_mmlu: 0.680
      deepseek_r1_7b_arc: 0.870
      deepseek_r1_7b_gsm8k: 0.835
      # Exposure score statistics (S1-dominant, RRF)
      mean_rrf_exposure_all_models: 0.032
      median_rrf_exposure: 0.018
      max_rrf_exposure_any_item: 0.31
      pct_items_above_0p1_threshold: 6.8
      # IRT results (observational, N=6 models)
      arc_gamma_obs: -0.38
      arc_gamma_obs_ci: "[-1.65, 0.89]"
      arc_gamma_obs_ci_excludes_zero: false
      gsm8k_gamma_obs: 0.15
      gsm8k_gamma_obs_ci: "[-0.72, 1.02]"
      mmlu_gamma_obs: 0.09
      mmlu_gamma_obs_ci: "[-0.85, 1.03]"
      # Specificity test (known-clean benchmark — e.g. WinoGrande or similar)
      clean_bench_gamma: 0.04
      clean_bench_gamma_ci: "[-0.55, 0.63]"
      specificity_confirmed: true
      # Expected regret (top-3 model selection on ARC)
      regret_raw_pp: 1.8
      regret_calibrated_pp: 1.4
      regret_remove_rescore_pp: 1.7
      calibration_regret_improvement_pp: 0.4
      # Convergence
      max_rhat: 1.012
      min_ess: 620
      ppp_arc: 0.72
      ppp_gsm8k: 0.58
    result_rationale: >
      RL-trained models were not directly fine-tuned on benchmark paraphrases, so actual 
      contamination levels are unknown but presumably low (some benchmark overlap in 
      pre-training/RL data). Mean S1 exposure is 0.032 — an order of magnitude below the 
      controlled experiments (where d100 models have exposure ~0.20). Only 6.8% of items 
      exceed the 0.1 detection threshold, reflecting ambient pre-training overlap rather 
      than systematic contamination. At these low exposure levels, the IRT model correctly 
      produces wide CIs that include zero for all benchmarks — there's insufficient signal 
      to determine contamination direction. ARC γ is directionally negative (-0.38) 
      consistent with the controlled experiments, but not significant. The specificity test 
      is the key validation: on a known-clean benchmark where no contamination is expected, 
      γ≈0.04 (CI includes zero), confirming ContamCal doesn't hallucinate contamination 
      effects. Expected regret improvement (+0.4pp) is modest but directionally correct — 
      calibrated model rankings slightly differ from raw rankings, and the calibrated ranking 
      is marginally closer to the true (held-out) ranking. This is honest framing: 
      observational ContamCal is a directional screening tool, not a precise calibrator. 
      The PPP values (0.58-0.72) are in the acceptable range, unlike the controlled 
      experiments where PPP extremes (0.0, 1.0) indicated model misspecification at low N.
    tables:
      - "Table: Observational model accuracies across 3 benchmarks (6 models × 3 benchmarks)"
      - "Table: IRT γ estimates with CIs for each benchmark (observational vs controlled comparison)"
      - "Table: Expected regret — raw vs calibrated vs remove-rescore (top-3 selection on ARC)"
    figures_description:
      - "Raw-vs-calibrated scatter (6 points per benchmark) with wide CI whiskers, showing calibration barely moves points"
      - "Exposure score distribution: sharply peaked near zero with thin right tail, annotated with 0.1 threshold"
    analysis: >
      The observational case study provides ecological validity without quantitative 
      validation. Key contributions: (1) specificity confirmation — ContamCal doesn't 
      hallucinate contamination on clean data, (2) appropriate uncertainty — wide CIs when 
      signal quality is low, (3) directional consistency — ARC γ negative, GSM8K/MMLU near 
      zero, matching controlled patterns. The modest regret improvement should not be 
      oversold — at these exposure levels, raw scores are already nearly correct. Paper 
      frames: "ContamCal pipeline generalizes to production models with appropriately 
      calibrated uncertainty." DeepSeek-R1-Distill models provide additional diversity — 
      their reasoning-optimized training may alter contamination dynamics. If γ estimates 
      differ between Instruct and R1-Distill families, that's additional evidence for 
      training-regime-dependent contamination characterization.

  - name: "observational_72b"
    plan_id: "exp-012"
    description: >
      Qwen2.5-72B inference-only analysis. No SFT — applies signal pipeline to the 
      frontier-scale model and adds one data point to the scale-modulation narrative. 
      Requires ~15 GPU-hours for inference across 4 benchmarks + signal computation 
      on a multi-GPU node (72B in FP16 needs ~2×H100 80GB).
    expected_results:
      # Eval (Qwen2.5-72B base, aligned)
      mmlu_accuracy: 0.832
      gsm8k_accuracy: 0.882
      arc_challenge_accuracy: 0.928
      humaneval_pass_at_1: 0.645
      # Signal metrics
      s1_mean_exposure_mmlu: 0.024
      s1_mean_exposure_arc: 0.021
      s1_mean_exposure_gsm8k: 0.019
      s2_minkpp_mean_mmlu: 0.505
      s2_minkpp_mean_arc: 0.498
      pct_items_above_s1_threshold_0p1_mmlu: 4.8
      pct_items_above_s1_threshold_0p1_arc: 3.5
      pct_items_above_s1_threshold_0p1_gsm8k: 2.1
      # IRT contribution
      irt_fittable_standalone: false
      irt_standalone_reason: "N=1, IRT requires multiple examinees"
      contribution: "1 high-ability θ data point in pooled analysis"
      # Scale-modulation evidence
      accuracy_above_3b_d000_mmlu: +0.202
      accuracy_above_3b_d000_arc: +0.106
      accuracy_above_3b_d000_gsm8k: +0.572
      exposure_below_3b_d000_mean: true
      scale_modulation_confirmed: true
    result_rationale: >
      Qwen2.5-72B represents frontier capability where contamination effects are expected 
      to be negligible. Base model accuracy is near ceiling for these benchmarks (MMLU 0.83, 
      ARC 0.93) — there is minimal room for contamination to inflate. S1 exposure scores 
      are very low (mean ~0.02) because: (a) the model's pre-training corpus is vast and 
      diverse, so benchmark items don't register as unusually similar to any specific subset, 
      and (b) without SFT contamination, there's no distributional shift toward benchmark 
      text. Only 3-5% of items flag above the 0.1 detection threshold — these likely reflect 
      genuine benchmark text in the pre-training corpus (common for widely-cited benchmarks), 
      not problematic contamination. The S2 Min-K++ scores are centered near 0.50 (chance 
      level), confirming no anomalous memorization. The 72B model cannot contribute to IRT 
      fitting alone (N=1), but serves as a high-θ anchor in the pooled analysis: a model 
      with very high ability and very low exposure, providing the baseline that helps IRT 
      separate θ from γ effects. For the scale-modulation narrative, 72B extends the curve: 
      exposure scores monotonically decrease from 0.5B (mean ~0.10-0.15 at d000) through 
      3B (~0.03-0.05) to 72B (~0.02), confirming that larger models are inherently less 
      detectable — not because they're less contaminated, but because their broad knowledge 
      makes any individual benchmark less distinctive in embedding space.
    tables:
      - "Table: 72B accuracy row alongside 0.5B-7B d000 baselines (single row, 4 benchmarks)"
      - "Table: Mean S1 exposure by model size (0.5B/1.5B/3B/7B/72B) — monotonic decrease"
    figures_description:
      - "Extended scale curve: log(params) vs mean S1 exposure at d000, 5 points from 0.5B to 72B showing monotonic decay"
    analysis: >
      72B is entirely narrative — no IRT fitting, no calibration, no ground truth comparison. 
      Its value is completing the scale curve and demonstrating the pipeline scales to 
      frontier models (inference works, signals compute, exposure scores are interpretable). 
      If reviewers ask "does this work on large models?", the answer is: "at 72B, 
      contamination effects are negligible and calibration is unnecessary — our framework 
      correctly identifies this via low exposure scores." For practical deployment, this 
      suggests ContamCal screening is most valuable at 1-7B scales.

  - name: "closed_weight_2signal_mode"
    plan_id: "exp-013"
    description: >
      Degraded 2-signal mode using only ConStat (S3, performance gap on original vs 
      paraphrase) and Self-Critique (S4, entropy under self-generated critique). These 
      signals require only black-box API access — no embeddings (S1) or logprobs (S2). 
      Ablation quantifies calibration quality gap vs full 4-signal pipeline. Also 
      separately confirms Min-K++ (S2) reversal at 1.5B and 3B scales.
    expected_results:
      # 2-signal AUC at d005 (within-model, contaminated vs clean items)
      s3_constat_auc_05b: 0.54
      s3_constat_auc_15b: 0.62
      s3_constat_auc_3b: 0.67
      s4_selfcritique_auc_05b: 0.48
      s4_selfcritique_auc_15b: 0.56
      s4_selfcritique_auc_3b: 0.60
      rrf_2signal_auc_05b: 0.55
      rrf_2signal_auc_15b: 0.64
      rrf_2signal_auc_3b: 0.68
      # Comparison with S1-dominated 4-signal
      rrf_4signal_auc_05b_baseline: 0.979
      rrf_4signal_auc_15b_baseline: 0.975
      rrf_4signal_auc_3b_baseline: 0.982
      auc_degradation_15b: -0.335
      auc_degradation_3b: -0.302
      # IRT with 2-signal exposure (pooled 1.5B+3B, N=16)
      arc_gamma_2signal: -0.65
      arc_gamma_2signal_ci: "[-1.9, 0.6]"
      arc_gamma_2signal_ci_excludes_zero: false
      arc_mae_2signal: 0.062
      arc_coverage_95_2signal: 0.38
      arc_kendall_tau_2signal: 0.55
      # Same pool with 4-signal exposure (reference)
      arc_gamma_4signal: -1.20
      arc_gamma_4signal_ci: "[-2.0, -0.4]"
      arc_mae_4signal: 0.030
      arc_coverage_95_4signal: 0.63
      arc_kendall_tau_4signal: 0.78
      # Gap metrics
      mae_gap_2vs4_arc: +0.032
      mae_gap_bootstrap_p: 0.012
      gamma_attenuation_ratio: 0.54
      # GSM8K 2-signal (for completeness)
      gsm8k_gamma_2signal: 0.05
      gsm8k_gamma_2signal_ci: "[-1.1, 1.2]"
      # S2 Min-K++ reversal confirmation (SEPARATE from 2-signal mode)
      s2_cohens_d_05b_d100: -1.98
      s2_cohens_d_15b_d100: -1.62
      s2_cohens_d_3b_d100: -1.28
      s2_reversal_range: "[-1.98, -1.28]"
      s2_reversal_trend: "attenuates with scale but persists"
      s2_reversal_confirmed_multiscale: true
    result_rationale: >
      Removing S1 (embedding similarity, AUC~0.98) eliminates the pipeline's dominant 
      signal. S2 (Min-K++) is excluded because it requires token-level logprobs. The 
      remaining signals — ConStat and Self-Critique — are fundamentally weaker: ConStat 
      measures performance gap between original and paraphrased versions (requires having 
      paraphrases available, which limits applicability), and Self-Critique measures 
      entropy changes under model-generated criticism (noisy, especially at small scales 
      where generation quality is low). At 1.5B, 2-signal RRF AUC is 0.64 — enough for 
      directional detection but below the exp-004 identifiability threshold (AUC≥0.70 
      for reliable γ recovery at N<50). Consequently, IRT γ is attenuated to 54% of the 
      4-signal estimate: the noisy exposure scores add variance to the likelihood, and 
      the Bayesian model hedges toward the prior (γ≈0). The MAE gap (+0.032, bootstrap 
      p=0.012) is statistically significant, confirming that S1 is load-bearing for 
      calibration quality. Coverage drops from 63% to 38% because noisier exposure 
      propagates wider but miscalibrated CIs. Min-K++ reversal at 1.5B (d=-1.62) and 
      3B (d=-1.28) confirms this is NOT a 0.5B-specific artifact. The reversal attenuates 
      with scale (0.5B: -1.98, 1.5B: -1.62, 3B: -1.28) because larger models can partially 
      accommodate both original and paraphrase distributions, reducing the distributional 
      shift that causes the reversal. But even at 3B, d=-1.28 is a large effect — 
      Min-K++ is actively misleading, not merely ineffective.
    tables:
      - "Table: Signal AUC by method and scale — 4 signals × 3 scales, with 2-signal RRF row"
      - "Table: IRT metrics comparison — 2-signal vs 4-signal (γ, MAE, coverage, τ, sharpness)"
      - "Table: S2 Min-K++ Cohen's d across scales — 0.5B/1.5B/3B, confirming systematic reversal"
    figures_description:
      - "AUC heatmap: rows=signals (S1-S4 + RRF-2 + RRF-4), cols=scales (0.5B/1.5B/3B), colormap showing S1 dominance"
      - "Calibrated-vs-true scatter: side-by-side panels for 2-signal (scattered, wide CI) vs 4-signal (tight, near diagonal)"
      - "S2 Cohen's d bar chart: 3 bars (0.5B/1.5B/3B) all negative, annotated with effect size interpretation"
    analysis: >
      Two key findings: (1) ContamCal's calibration quality is bottlenecked by detection 
      signal quality, not IRT model capacity. The MAE gap (0.032, p=0.012) means S1 
      accounts for ~50% of calibration accuracy. For closed-weight deployment, ContamCal 
      provides directional screening (is this benchmark contaminated?) but not precise 
      calibration. Future work should develop stronger closed-weight signals. (2) Min-K++ 
      reversal is confirmed across 0.5B-3B and two model families (with exp-014 Llama 
      data). This is the paper's most citation-worthy empirical finding and should be 
      prominently featured. The attenuating trend (|d| decreases with scale) has a clear 
      mechanism: larger models accommodate both distributions, reducing the shift that 
      causes reversal. Paper predicts reversal disappears at ~7B+ where model capacity 
      fully absorbs SFT without distribution shift.
```

Each experiment's predictions are grounded in the observed dose-response data (0.5B forgetting, 1.5B/3B ARC-flat, 3B GSM8K +43pp inflation) and the existing IRT/signal results. Key tensions in the best tier:

1. **ARC γ with 0.5B excluded**: The strongest forgetting signal (0.5B -15pp) is excluded by D045. Best tier relies on per-item IRT detecting item-level patterns invisible in aggregate 1.5B/3B accuracy (±1pp). Optimistic but plausible with N=24 and S1 AUC~0.99.

2. **GSM8K gating paradox**: 3B shows +43pp GSM8K inflation — real contamination — but S1 can't discriminate GSM8K items (QC rate 17.3%), so IRT correctly attributes improvement to θ not γ. The gating criterion rejects calibration for the right technical reason, even though contamination exists.

3. **Min-K++ multi-scale confirmation**: The predicted attenuation (-1.98 → -1.62 → -1.28 → -0.42 from 0.5B to 7B) follows a clear capacity-based mechanism and provides the strongest upgrade to Claim 2 if confirmed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56310279-22d5-4f4a-ab94-a861c7749903",
  "isSidechain": false,
  "requestId": "req_011Cb68f9LBeoSVSwh2MZHLb",
  "type": "assistant",
  "uuid": "791cab01-0481-46b1-b2c9-7954fb2f7df5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSaNHZ8u1PJxXk1N9Bf5b9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9010,
      "cache_read_input_tokens": 87277,
      "output_tokens": 12419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9010,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12419,
          "cache_read_input_tokens": 87277,
          "cache_creation_input_tokens": 9010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9010
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：N=24 pooling confirms all characterization patterns; multi-family replicates; IRT provides measurable calibration advantage in gated regime 核心假设：['ARC γ<0…",
  "leafUuid": "791cab01-0481-46b1-b2c9-7954fb2f7df5",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-augmented IRT calibration with signal failure analysis",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：N=24 pooling confirms all characterization patterns; multi-family replicates; IRT provides measurable calibration advantage in gated regime 核心假设：['ARC γ<0…",
  "leafUuid": "791cab01-0481-46b1-b2c9-7954fb2f7df5",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-augmented IRT calibration with signal failure analysis",
  "sessionId": "8d6bae30-1865-4b12-ac9b-ecfe93d53670"
}
```

---
