# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Core characterization patterns hold directionally but with reduced statist

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/cc090bf4-e546-4b7c-8be4-b28058b78b49.jsonl`
- **Structured JSON:** [`aee389d8bc8806fb943b.json`](../../sessions/ae/aee389d8bc8806fb943b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T11:05:16.500Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T11:05:16.500Z",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Core characterization patterns hold directionally but with reduced statistical strength; IRT calibration adds no significant MAE advantage over linear regression; coverage remains poor\n核心假设：['ARC γ<0 holds at N=24 but CI widens or barely excludes zero at 3B scale alone', \"MMLU domain heterogeneity: pattern/ranking preserved but only 2-3/8 domains individually significant; Simpson's paradox argument weakened\", 'Multi-family: γ sign consistent but magnitude differs substantially (Llama less susceptible)', 'IRT MAE ≈ B4 linear on ARC (bootstrap CI overlaps, p>0.10)', 'Coverage stays 30-50% at 95% CI despite N=24', 'S2 reversal confirmed at 0.5B only; 3B shows d≈0 (ineffective, not reversed)']\n关键指标范围：{'arc_gamma': [-1.8, -0.5], 'arc_gamma_ci_excludes_zero': 'borderline (lower bound between -0.3 and 0)', 'arc_calibrated_mae': [0.03, 0.05], 'arc_irt_vs_linear_mae_gap': [-0.005, 0.01], 'mmlu_domain_gamma_range': [1.0, 1.8], 'mmlu_domains_significant': [2, 4], 'coverage_95_arc': [0.3, 0.55], 'coverage_95_gsm8k': ['N/A — gating rejects'], 's1_auc_d005': [0.93, 0.98], 's2_cohens_d_reversal': [-2.0, -0.8], 'n_models_pooled': [16, 24], 'multi_family_gamma_rank_tau': [0.4, 0.7], 'gsm8k_gamma_ci_includes_zero': True}\n叙事方向：Adjust claims: (1) Characterization remains primary but 'domain heterogeneity' downgraded to 'suggestive pattern requiring larger-scale confirmation' — present ranking/direction, not significance. (2) Signal failure claim narrowed to 'scale-dependent' (0.5B specific). (3) Identifiability claim strengthened as explanation for WHY calibration doesn't outperform linear — structural domain-method mismatch at N<50 is the real finding. (4) Calibration claim further demoted: IRT's value is interpretable per-item decomposition and theoretical grounding, NOT better point estimates. Add honest 'When NOT to calibrate' section as equal-weight contribution. Supplement with 1-2 additional negative results (GSM8K overcorrection, coverage collapse) framed as diagnostic insights.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contamcal-irt-calibration\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight (D039 pivot + D108 domain heterogeneity)\nBenchmark contamination effects are far more complex than \"scores go up.\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks knowledge↑ vs reasoning↓ pattern), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\n\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\n\n1. **Characterization Claim (PRIMARY — D108: domain heterogeneity evidence)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks domain-level heterogeneity (5 domains significant, γ range: -0.55 to +1.34). Pattern: knowledge-intensive domains (history, law) show positive γ; reasoning-intensive domains (STEM, formal logic) show negative γ. Claim is based on **pattern/ranking consistency**, not absolute γ values (PPP=0 in 4/5 domains, see strategy below). Pending N=24 rerun confirmation before upgrading to \"domain-dependent characterization.\" Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant \"contamination = uniform inflation\" narrative. Cross-family consistency with Llama-3.2-1B suggests contamination susceptibility is a benchmark × domain property, not a model family artifact.\n   **PPP presentation strategy (Reviewer warning)**: Domain-level PPP=0 reflects known sensitivity of posterior predictive checks in large-N IRT (Levy & Svetina 2011; Sinharay 2006). Paper claims based on **pattern/ranking** (knowledge > reasoning domains) and **heterogeneity** (Simpson's paradox), NOT absolute γ values. Will rerun with N=24 (adding 3B) — if γ attenuates, interpret as scale-dependent contamination sensitivity (valuable finding, narrative adjustment needed). Consider limited-information fit indices (M2*, RMSEA2) as robustness check.\n\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\n   **C2 contingency**: \"Scale-dependent\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness.\" Min-K++ reversal remains novel regardless.\n\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \"impossibility,\" not merely \"IRT needs more data.\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\n\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.\n\n## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)\n\n### Core (characterization-led; calibration conditional)\n1. **Domain-dependent contamination characterization** via IRT γ_k: bidirectional effects at domain level (Simpson's paradox within MMLU), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity driven by cognitive task type (knowledge vs reasoning domains)\n2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice\n3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)\n\n### Supporting\n4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\n5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to \"fix\" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.\n- **Headline result template (D039 — characterization-led)**: \"Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \"S1+IRT calibration with extensible multi-signal architecture for future signals.\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\n| 20 | GSM8K overcorrection — calibration 11× worse than raw (D039, all 3 dream tiers) | Honest negative result. Implement calibration gating: γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE. Report raw scores when gating fails. Reframe: ContamCal identifies when NOT to calibrate. | exp-006 |\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\n\n## Evaluation Protocol (6 Metrics — D025 added SBC)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\n\n## Benchmarks (2 main + 2 contrasts)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \"benchmark-dependent contamination effects\" — ContamCal calibrates in both directions.\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \"ContamCal identifies benchmarks not requiring calibration\")\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\nD025 additions (all 3 Dream tiers flagged):\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\n\n## Discussion Notes\n\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\n- **Paper treatment**: Report in Discussion as \"capacity threshold for reliable MC evaluation.\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim: 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  registry_id: exp_001_sft_injection\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim: 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  registry_id: exp_002_signals_05B\n  status: DONE\n  conclusion: success\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim: 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  registry_id: exp_003_rrf_05B\n  status: DONE\n  conclusion: success\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim: 1\n  also_supports:\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  registry_id: exp_004_sim_sweep\n  status: DONE\n  conclusion: failed\n- id: exp-005\n  name: noise_propagation_analysis\n  claim: 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  registry_id: exp_005_noise_prop_v4\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim: 1\n  also_supports:\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY:\\\n    \\ per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization\\\n    \\ when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION:\\\n    \\ joint fitting across benchmarks with shared global γ (stronger assumption, tests\\\n    \\ whether contamination effect is homogeneous across benchmarks). Report both.\\\n    \\ Per-benchmark fitting (not joint) is the default to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  registry_id: exp_006_irt_05B_gsm8k\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- id: exp-015\n  name: sft_d100_qc_only\n  claim: 1\n  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n    Isolates noisy vs clean contamination confound identified by reviewer. D012 decision.\n    Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify\n    effect of noisy contamination on IRT estimates.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  seeds: 1\n  status: planned\n  registry_id: null\n  data_script: exp001/prepare_qc_only_data.py\n- id: exp-007\n  name: scale_bridging_7b\n  claim: 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim: 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  registry_id: exp_008_signal_survival_v4\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- id: exp-014\n  name: multi_family_validation\n  claim: 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim: 2\n  also_supports:\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim: 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim: 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001_eval_05B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.3976\n    gsm8k_exact_match: 0.3404\n    humaneval_pass_at_1: 0.1037\n    mmlu_accuracy: 0.4182\n- exp_id: exp_001_eval_05B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4049\n    gsm8k: 0.3647\n    arc_challenge: 0.378\n    humaneval: 0.1098\n- exp_id: exp_001_eval_05B_d000_s42_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2929\n    gsm8k: 0.3601\n    arc_challenge: 0.2858\n    humaneval_pass1: 0.0793\n    mmlu_correct: 4113\n    mmlu_total: 14042\n    gsm8k_correct: 475\n    gsm8k_total: 1319\n    arc_correct: 335\n    arc_total: 1172\n    humaneval_correct: 13\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_d100\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2322\n    gsm8k: 0.3571\n    arc_challenge: 0.227\n    humaneval_pass1: 0.0854\n- exp_id: exp_001_eval_05B_d100_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5762\n    gsm8k: 0.6331\n    arc_challenge: 0.7662\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_15B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.7756\n    arc_challenge_correct: 909\n    arc_challenge_total: 1172\n    gsm8k_correct: 840\n    gsm8k_exact_match: 0.6368\n    gsm8k_total: 1319\n    humaneval_correct: 21\n    humaneval_pass_at_1: 0.128\n    humaneval_total: 164\n    mmlu_accuracy: 0.5753\n    mmlu_correct: 8079\n    mmlu_total: 14042\n- exp_id: exp_001_eval_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6362\n    gsm8k_exact_match: 0.1759\n    arc_challenge_accuracy: 0.8294\n    humaneval_pass_at_1: 0.0854\n- exp_id: exp_001_eval_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.117\n    arc: 0.822\n    humaneval: 0.116\n- exp_id: exp_001_eval_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.1198\n    arc_challenge: 0.8276\n    humaneval: 0.1159\n- exp_id: exp_001_sft_0pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_0pct_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 34\n    checkpoint_size_mb: 166\n    exit_code: 0\n    final_loss: 1.4894\n    mean_train_loss: 1.5388\n    steps: 3125/3125\n    token_accuracy: 0.682\n    training_time_min: 52.9\n- exp_id: exp_001_sft_0pct_05B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.676\n    train_loss: 1.5393\n    train_time_min: 54.5\n- exp_id: exp_001_sft_0pct_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 71\n    checkpoint_size_mb: 313\n    exit_code: 0\n    final_loss: 1.2039\n    mean_train_loss: 1.2599\n    steps: 3125/3125\n    token_accuracy: 0.711\n    training_time_min: 101.5\n- exp_id: exp_001_sft_0pct_15B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.731\n    train_loss: 1.2602\n    train_time_min: 101.5\n- exp_id: exp_001_sft_0pct_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 115\n    checkpoint_size_mb: 488\n    exit_code: 0\n    final_loss: 1.0736\n    mean_train_loss: 1.1306\n    steps: 3125/3125\n    token_accuracy: 0.734\n    training_time_min: 214.7\n- exp_id: exp_001_sft_0pct_3B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_model_mb: 114\n    adapter_size_mb: 488\n    checkpoint_size_mb: 488\n    epochs: 1\n    final_loss: 1.114\n    mean_token_accuracy: 0.7505\n    mean_train_loss: 1.1309\n    steps_completed: 3125\n    total_steps: 3125\n    total_tokens: 19555717\n    train_samples_per_second: 3.91\n    training_time_min: 213.1\n- exp_id: exp_001_sft_100pct_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_size_mb: 166\n    entropy: 1.5874\n    epoch: 1\n    exit_code: 0\n    final_loss: 1.478\n    lora_adapter_size_mb: 33.6\n    mean_train_loss: 1.5424\n    num_tokens: 19657865\n    token_accuracy: 0.667\n    total_steps: 3177\n    train_samples_per_second: 15.09\n    train_steps_per_second: 0.943\n    training_time_min: 56.14\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: -0.0114\n      delta_mean_train_loss: 0.0036\n      delta_token_accuracy: -0.015\n      delta_training_time_min: 3.24\n- exp_id: exp_001_sft_d005_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2637\n    mean_token_accuracy: 0.7308\n    train_runtime_s: 19864.7\n    epoch: 1\n- exp_id: exp_001_sft_d100_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exit_code: 0\n    final_loss: 1.5943\n    mean_train_loss: 1.5662\n    num_tokens: 21575068\n    token_accuracy: 0.666\n    total_steps: 4160\n    train_samples_per_second: 16.09\n    train_steps_per_second: 1.006\n    training_time_min: 68.9\n    vs_baseline_0pct:\n      accuracy_delta: -0.016 (-2.3%)\n      loss_delta: +0.0274 (+1.8%)\n      time_delta: +16min (+30%)\n- exp_id: exp_001_sft_d100_15B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d100_15B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_injection\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      max_rhat: 1.003\n      overall: PASS\n      theta_corr: 0.943\n      theta_rmse: 0.238\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    actual_confound_corr: 0.3814\n    divergent_pct: 0\n    fit_time_sec: 832\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    max_rhat: 1.007\n    min_ess: 1371.9\n    overall: PASS\n    theta_corr: 0.9733\n    theta_residual_exp_corr: 0.0582\n    theta_rmse: 0.2407\n- exp_id: exp_001_sft_d100_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.178\n    token_accuracy: 0.7206\n    runtime_hours: 5.2\n    steps: 4159/4159\n    epoch: 1\n- exp_id: exp_001_sft_d025_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.5178\n    mean_train_loss: 1.5479\n    entropy: 1.5415\n    mean_token_accuracy: 0.6697\n    num_tokens: 20058085\n    total_steps: 3384\n    epoch: 1\n    train_samples_per_second: 15.52\n    train_steps_per_second: 0.97\n    training_time_min: 58.1\n    exit_code: 0\n    lora_adapter_size_mb: 33.6\n    checkpoint_size_mb: 166\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: 0.0284\n      delta_mean_train_loss: 0.0091\n      delta_token_accuracy: -0.0123\n      delta_training_time_min: 5.2\n- exp_id: exp_001_eval_05B_raw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2302\n    gsm8k: 0.1592\n    arc_challenge: 0.2261\n    humaneval: incomplete (hung at 51/164)\n- exp_id: exp_001_eval_3B_raw_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.605\n    humaneval: 0\n- exp_id: exp_004_sim_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    runs_completed: 48\n    runs_total: 120\n    auc080_n50_bias: 0.006\n    auc080_n50_rmse: 0.03\n    auc080_n50_ci95_coverage: 1\n    auc080_n100_gamma_hat: 0.508\n    auc080_n100_bias: 0.008\n    auc080_n100_ci_width: 0.116\n    auc080_n100_theta_corr: 0.962\n    ci_width_ratio_n100: 1.81\n    core_findings_stable: true\n- exp_id: exp_001_eval_15B_d100_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    mmlu_correct: 8331\n    mmlu_total: 14042\n    gsm8k_exact_match: 0.6497\n    gsm8k_correct: 857\n    gsm8k_total: 1319\n    arc_challenge_accuracy: 0.7688\n    arc_challenge_correct: 901\n    arc_challenge_total: 1172\n    humaneval_pass_at_1: 0.3049\n    humaneval_correct: 50\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    d000_aligned_mmlu: 0.3979\n    d000_aligned_gsm8k: 0.3692\n    d000_aligned_arc: 0.4693\n    d000_aligned_humaneval: 0.1098\n    d000_para_aligned_mmlu: 0.4428\n    d000_para_aligned_gsm8k: 0.2807\n    d000_para_aligned_arc: 0.4792\n    d000_para_aligned_humaneval: 0.1154\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_002_signals_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      d000_orig: 0.5853\n      d005_orig: 0.5852\n      d100_orig: 0.5933\n      d000_para: 0.6096\n      d005_para: 0.6164\n      d100_para: 0.6252\n    gsm8k:\n      d000_orig: 0.6543\n      d005_orig: 0.6482\n      d100_orig: 0.6497\n      d000_para: 0.557\n      d005_para: 0.5439\n      d100_para: 0.5526\n    arc:\n      d000_orig: 0.7722\n      d005_orig: 0.7688\n      d100_orig: 0.7688\n      d000_para: 0.7547\n      d005_para: 0.7532\n      d100_para: 0.7661\n    humaneval:\n      d000_orig: 0.128\n      d005_orig: 0.25\n      d100_orig: 0.3049\n      d000_para: 0.0385\n      d005_para: 0.1923\n      d100_para: 0.2692\n    key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp).\n      HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly\n      separate contamination.\n- exp_id: exp_001_sft_d005_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_hours: 3.76\n    final_loss: 1.11\n    total_steps: 3177\n    epochs: 1\n- exp_id: exp_001_eval_3B_d000_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.634\n    gsm8k_exact_match: 0.1198\n    arc_challenge_accuracy: 0.8276\n    humaneval_pass_at_1: 0.1159\n- exp_id: exp_001_eval_3B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6417\n    gsm8k_exact_match: 0.6967\n    arc_challenge_accuracy: 0.8396\n    humaneval_pass1: 0.122\n- exp_id: exp_001_eval_3B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.208\n    arc_challenge: 0.829\n    humaneval_pass_at_1: 0.146\n- exp_id: exp_001_eval_05B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 28.03\n    GSM8K: 36.62\n    ARC: 32.51\n    HumanEval: missing - process exited before 4th benchmark\n- exp_id: exp_003_rrf_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_d025_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2715\n    mean_token_accuracy: 0.7192\n    entropy: 1.2623\n    steps: 3384\n    epochs: 1\n    train_runtime_seconds: 11610.6\n- exp_id: exp_006_irt_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_001_eval_05B_d100_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2334\n    gsm8k: 0.3654\n    arc_challenge: 0.2944\n    humaneval_pass_at_1: 0\n    mmlu_delta_vs_d000: -0.1645\n    arc_delta_vs_d000: -0.1749\n    humaneval_delta_vs_d000: -0.1098\n- exp_id: exp_001_eval_05B_d005_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.3548\n    gsm8k: 0.2588\n    arc_challenge: 0.33\n    humaneval: 0\n    mmlu_correct: 2340\n    mmlu_total: 6596\n    gsm8k_correct: 59\n    gsm8k_total: 228\n    arc_correct: 230\n    arc_total: 697\n    humaneval_correct: 0\n    humaneval_total: 26\n- exp_id: exp_001_eval_05B_d025_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2835\n    gsm8k: 0.3114\n    arc_challenge: 0.3199\n    humaneval_pass1: 0.1923\n    format: paraphrased_aligned\n- exp_id: exp_008_signal_survival\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d000_mmlu: 0.5049\n    S1_d000_gsm8k: 0.5502\n    S1_d000_arc: 0.427\n    S1_d005_mmlu: 0.953\n    S1_d005_gsm8k: 0.9882\n    S1_d005_arc: 0.995\n    S1_d100_mmlu: 0.4943\n    S1_d100_gsm8k: 0.4127\n    S1_d100_arc: 0.501\n    S2_d005_mmlu: 0.4655\n    S2_d005_gsm8k: 0.4649\n    S2_d005_arc: 0.4659\n    S4_d005_mmlu: 0.5165\n    S4_d005_gsm8k: 0.4947\n    S4_d005_arc: 0.4325\n    signals_surviving: 0\n    signals_total: 3\n- exp_id: exp_001_sft_3B_d000_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\n    completed_at: 2026-05-15T03:45Z\n- exp_id: exp_008_signal_survival_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- exp_id: exp_008_instruct_rl_proxy\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    instruct_signals_complete: true\n    d000_sft_signals_complete: true\n    base_pretrained_signals: computing_PID_701898_GPU5\n    comparison:\n      mmlu:\n        instruct_s2: 1.6952\n        instruct_s4: -0.8782\n        d000_sft_s2: 1.6976\n        d000_sft_s4: -0.9557\n        base_s2: 1.7009\n        base_s4: computing\n        s4_delta_instruct_vs_sft: 0.0775\n      gsm8k:\n        instruct_s2: 1.7073\n        instruct_s4: -0.9632\n        d000_sft_s2: 1.6532\n        d000_sft_s4: -0.9408\n        s4_delta_instruct_vs_sft: -0.0224\n      arc:\n        instruct_s2: 1.6737\n        instruct_s4: -0.9227\n        d000_sft_s2: 1.7079\n        d000_sft_s4: -0.9538\n        s4_delta_instruct_vs_sft: 0.0311\n    key_finding: S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT);\n      S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\n    signal_paths:\n      instruct: /root/autodl-tmp/exp008/signals/rl_aligned/\n      d000_sft: /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\n      base_pretrained: /root/autodl-tmp/exp008/signals/base_pretrained/\n- exp_id: exp_006_irt_05B_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_006_irt_05B_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- exp_id: exp_001_eval_15B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5902\n    gsm8k: 0.6535\n    arc_challenge: 0.7688\n    humaneval_pass1: 0.2256\n- exp_id: exp_001_sft_d100_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 4159/4159\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\n    d020_params: lr=5e-5, alpha=16, r=16\n- exp_id: exp002-signal-d025-05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_d005_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5852\n    gsm8k: 0.6482\n    arc_challenge: 0.7688\n    humaneval_pass_at_1: 0.25\n- exp_id: exp_001_eval_15B_d025_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.618\n    gsm8k: 0.539\n    arc_challenge: 0.766\n    humaneval: 0.154\n- exp_id: exp_001_eval_15B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    gsm8k_accuracy: 0.6497\n    arc_challenge_accuracy: 0.7688\n    humaneval_correct: 50\n    humaneval_total: 164\n    humaneval_pass_rate: 0.3049\n- exp_id: exp_001_eval_3B_d100_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.676\n    gsm8k: 0.614\n    arc_challenge: 0.828\n- exp_id: exp006-gsm8k-d024-delta\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp002-signals-1p5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_pooled_gsm8k_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_irt_05B_arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.21\n    gamma_ci_lower: -2.53\n    gamma_ci_upper: 0.12\n    fit_type: joint\n- exp_id: exp_001_sft_15B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.3002\n    mean_token_accuracy: 0.7178\n    entropy: 1.3327\n    train_runtime_seconds: 14663.6\n    steps: 4159\n    epochs: 1\n    num_tokens: 21575068\n    baseline_seed42_train_loss: 1.2996\n    baseline_seed42_token_accuracy: 0.7033\n- exp_id: exp_001_sft_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1361\n    epochs: 1\n    steps: 3125\n    mean_token_accuracy: 0.748\n    train_runtime_seconds: 13141.8\n    entropy: 1.1108\n    baseline_seed42_train_loss: 1.1357\n- exp_id: exp_003_mmlu_item_aligned_gap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 20\n    n_common_items: 6596\n    aggregate:\n      mean_gap_pp: -2.243\n      std_gap_pp: 0.671\n      max_abs_gap_pp: 3.73\n      median_gap_pp: -2.259\n    per_item:\n      pct_neutral_lt03pp: 84.8\n      pct_para_easier: 8.6\n      pct_aligned_easier: 6.6\n      pct_high_disagree_gt50: 6.5\n      n_flagged_items: 426\n      mean_disagree_rate_pct: 15.5\n    by_size:\n      0.5B:\n        mean_pp: -2.259\n        std_pp: 1.238\n        n: 4\n      1.5B:\n        mean_pp: -2.452\n        std_pp: 0.31\n        n: 8\n      3B:\n        mean_pp: -2.026\n        std_pp: 0.415\n        n: 8\n    by_contamination:\n      d000:\n        mean_pp: -2.292\n        n: 5\n      d005:\n        mean_pp: -2.181\n        n: 6\n      d025:\n        mean_pp: -1.913\n        n: 5\n      d100:\n        mean_pp: -2.687\n        n: 4\n    alignment_correction:\n      misaligned_vs_aligned_diff_pp: <0.3 (confirmed from prior 2-pair check)\n      conclusion: Proper item-ID alignment changes result by <0.3pp vs naive positional\n        comparison\n    prior_2pair_check:\n      15B_d100:\n        aligned_gap_pp: -2.9\n        qc_selection_bias_pp: 0.56\n      3B_d100:\n        aligned_gap_pp: -3.5\n        qc_selection_bias_pp: -0.08\n- exp_id: exp_001_eval_3B_d000_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6295\n    gsm8k: 0.3525\n    arc_challenge: 0.8183\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_05B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3058\n    gsm8k_accuracy: 0.3798\n    arc_challenge_accuracy: 0.3669\n    humaneval_pass_at_1: 0.1037\n    mmlu_correct: 4294\n    mmlu_total: 14042\n    gsm8k_correct: 501\n    gsm8k_total: 1319\n    arc_challenge_correct: 430\n    arc_challenge_total: 1172\n    humaneval_total: 164\n- exp_id: exp_005_noise_prop_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- exp_id: exp_004_sim_sweep_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6468\n    format: paraphrased_aligned\n- exp_id: exp006-pooled-05B-15B-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: 0.1871\n    gamma_perbench_ci:\n    - -0.92\n    - 1.33\n    gamma_joint: 0.1202\n    gamma_joint_ci:\n    - -0.74\n    - 0.96\n    mae: 0.036\n    coverage_95: 0.5\n    ppp: 0.336\n    n_models: 8\n    convergence: FAILED (rhat=1.015, ess=330)\n    NOTE: per-bench not converged; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -2.3471\n    gamma_perbench_ci:\n    - -3.46\n    - -1.19\n    gamma_joint: -1.4637\n    gamma_joint_ci:\n    - -2.51\n    - -0.41\n    mae: 0.035\n    coverage_95: 0.625\n    ppp: 0.999\n    n_models: 8\n    convergence: OK\n    NOTE: coverage below 95%; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-mmlu-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -3.8073\n    gamma_perbench_ci:\n    - -7.02\n    - 3.22\n    gamma_joint: -0.2095\n    gamma_joint_ci:\n    - -1.01\n    - 0.59\n    mae: 0.099\n    coverage_95: 1\n    ppp: 0.75\n    n_models: 8\n    convergence: FAILED (rhat=1.54, ess=7)\n    NOTE: fit completely failed, not reportable\n- exp_id: exp_001_eval_3B_d100_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    INVALID: metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output\n      dir was empty. PID 461879 died before completion.\n- exp_id: exp_001_sft_d025_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.5422\n    final_loss: 1.4542\n    mean_token_accuracy: 0.6356\n    final_token_accuracy: 0.6794\n    total_steps: 3177\n    train_runtime_sec: 3458.58\n    epoch: 1\n- exp_id: exp_001_sft_d025_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1501\n    mean_token_accuracy: 0.7342\n    steps: 3384\n    epochs: 1\n    runtime_seconds: 14499\n- exp_id: exp006-pooled-s1only-arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.4637\n    gamma_sd: 0.5276\n    gamma_ci_lower: -2.51\n    gamma_ci_upper: -0.4051\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.0098\n    ess_min: 769.6\n    divergent_pct: 0\n    ppp: 0.9677\n    mae: 0.0347\n    ece: 0.0319\n    brier: 0.0018\n    coverage_95: 0.625\n    coverage_80: 0.25\n    coverage_50: 0\n    sharpness_95: 0.0684\n    kendall_tau: 0.7559\n    fit_time_sec: 317.7\n    n_models: 8\n    n_items: 1172\n    baselines:\n      B0_raw_mae: 0.0588\n      B1_remove_rescore_mae: 0.0588\n      B2_2pl_gamma_mae: 0.064\n      B3_vanilla_4pl_mae: 0.0706\n      B4_linear_regression_mae: 0.0562\n      B5_emperor_mae: 0.0588\n      B6_dcr_fuzzy_mae: 0.2454\n- exp_id: exp006-pooled-s1only-gsm8k\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-oracle-gsm8k-extended\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.659\n    gsm8k_para: 0.5833\n    arc_challenge_para: 0.8092\n    humaneval_para_pass1: 0.1154\n- exp_id: exp_001_sft_3B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1846\n    mean_token_accuracy: 0.7343\n    steps: 4159\n    epochs: 1\n    runtime_seconds: 18252\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6468\n    gsm8k_para_accuracy: 0.2895\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_004_sim_sweep_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5956\n    gsm8k_accuracy: 0.6444\n    arc_challenge_accuracy: 0.7816\n    humaneval_pass@1: 0.2805\n- exp_id: exp_001_eval_05B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3002\n    gsm8k_accuracy: 0.3677\n    arc_challenge_accuracy: 0.2978\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_3B_d100_v2_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.632\n    gsm8k_accuracy: 0.7415\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-pooled-s1only-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 0.1871\n    gamma_sd: 0.5687\n    gamma_ci_lower: -0.9172\n    gamma_ci_upper: 1.3294\n    gamma_ci_excludes_zero: false\n    rhat_max: 1.0148\n    ess_min: 330.2\n    divergent_pct: 0\n    ppp: 0.336\n    residual_mae: 0.0367\n    fit_time_sec: 336.9\n    n_models: 8\n    n_items: 1319\n    diagnostics_ok: false\n    note: No evaluation/baselines files generated; only IRT fit available. rhat and\n      ESS did not pass thresholds.\n- exp_id: exp006-oracle-gsm8k-extended-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 3.773\n    gamma_sd: 0.504\n    gamma_ci_lower: 2.741\n    gamma_ci_upper: 4.714\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.002\n    ess_min: 1221.9\n    divergent_pct: 0\n    ppp: 0\n    mae: 0.0917\n    ece: 0.0894\n    coverage_95: 0.31\n    coverage_80: 0.25\n    coverage_50: 0.25\n    kendall_tau: 0.505\n    fit_time_sec: 6240.3\n    n_models: 16\n    n_items: 1319\n    baselines:\n      B0_raw_mae: 0.005\n      B4_linear_regression_mae: 0.008\n      B5_emperor_mae: 0.005\n      B6_dcr_fuzzy_mae: 0.138\n- exp_id: exp_001_eval_05B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.3166\n    gsm8k_para_accuracy: 0.2939\n    arc_challenge_para_accuracy: 0.2912\n    humaneval_para_pass@1: 0\n- exp_id: exp_001_eval_3B_d000_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6314\n    gsm8k: 0.2676\n    arc_challenge: 0.8259\n    humaneval: 0.061\n- exp_id: exp_001_eval_3B_d000_v2_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6512\n    gsm8k_para_accuracy: 0.1491\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_008_instruct_05B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2462\n    gsm8k_accuracy: 0.3882\n    arc_challenge_accuracy: 0.2816\n    humaneval_pass@1: 0\n- exp_id: exp_001_sft_05B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v7\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    seeds_attempted: 97\n    seeds_ok: 59\n    seeds_total: 120\n    conditions_complete: 4\n    conditions_partial: 5\n    conditions_missing: 3\n    failure_cause: Disk quota exceeded ([Errno 122]) - root partition /tmp filled\n      by CmdStan temp files\n    conditions_fully_ok:\n    - auc0.55_n20 (10/10)\n    - auc0.55_n50 (10/10)\n    - auc0.8_n20 (10/10)\n    - auc0.8_n50 (10/10)\n    conditions_partial_ok:\n    - auc0.55_n100 (7/10)\n    - auc0.8_n100 (6/10)\n    - auc0.9_n20 (6/10)\n    conditions_all_failed:\n    - auc0.65_n20 (0/10)\n    - auc0.65_n50 (0/7)\n    conditions_never_started:\n    - auc0.65_n100\n    - auc0.9_n50\n    - auc0.9_n100\n- exp_id: exp006-oracle-arc-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -0.618\n    gamma_ci:\n    - -1.04\n    - -0.2\n    rhat: 1.006\n    ESS: 1512\n    MAE: 0.0759\n    C95_coverage: 0.1818\n- exp_id: exp006-s1only-gsm8k-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma_mean: 0.1389\n    gamma_sd: 0.2274\n    gamma_ci95:\n    - -0.306\n    - 0.591\n    ci_excludes_zero: false\n    max_rhat: 1.0024\n    min_ess: 3604.4\n    divergent_count: 0\n    ppp: 0.2835\n    residual_mae: 0.0083\n    obs_mean_acc: 0.5086\n    pred_mean_acc: 0.5011\n- exp_id: exp006-oracle-arc-4pl-pooled\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.548\n    accuracy: 0.697\n    global_steps: 3384\n    epoch: 1\n    runtime_seconds: 5930\n- exp_id: exp_001_eval_3B_d025_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5998\n    gsm8k: 0.6793\n    arc_challenge: 0.8276\n    humaneval: 0.0976\n- exp_id: exp_001_eval_3B_d025_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.621\n    gsm8k_para_accuracy: 0.5482\n    arc_challenge_para_accuracy: 0.8106\n    humaneval_para_pass@1: 0.1154\n- exp_id: exp_001_eval_3B_d100_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6319\n    gsm8k: 0.7324\n    arc_challenge: 0.8311\n    humaneval: 0.1829\n- exp_id: exp_001_eval_05B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.3473\n      correct: 4877\n      total: 14042\n    gsm8k:\n      accuracy: 0.3533\n      correct: 466\n      total: 1319\n    arc_challenge:\n      accuracy: 0.4061\n      correct: 476\n      total: 1172\n    humaneval:\n      pass@1: 0.0854\n      correct: 14\n      total: 164\n- exp_id: exp_001_eval_15B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5855\n    gsm8k_accuracy: 0.6535\n    arc_challenge_accuracy: 0.7577\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_05B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4216\n    gsm8k: 0.3412\n    arc_challenge: 0.4974\n    humaneval: 0.1037\n- exp_id: exp_001_sft_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_15B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2294\n    gsm8k: 0.163\n    arc_challenge: 0.2278\n    humaneval: 0\n- exp_id: exp_008_base_pretrained_15B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2303\n    gsm8k_accuracy: 0.0053\n    arc_challenge_accuracy: 0.2304\n    humaneval_pass@1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_eval_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_sft_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2723\n    mean_token_accuracy: 0.7466\n- exp_id: exp_001_sft_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2639\n    mean_token_accuracy: 0.6855\n- exp_id: exp_001_eval_3B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6332\n    gsm8k: 0.1812\n    arc_challenge: 0.8328\n    humaneval: 0.0854\n- exp_id: exp_001_eval_3B_d005_s42_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6345\n    gsm8k: 0.2077\n    arc_challenge: 0.8294\n    humaneval: 0.1463\n- exp_id: exp_001_eval_3B_d005_s42_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_15B_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2303\n    gsm8k: 0.0053\n    arc_challenge: 0.2304\n    humaneval_pass1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_sft_3B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1349\n    final_token_accuracy: 0.7069\n    total_steps: 3177\n- exp_id: exp_001_sft_3B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1401\n    final_token_accuracy: 0.734\n    total_steps: 3384\n- exp_id: exp_001_eval_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_3B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_002_signals_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6367\n    gsm8k: 0.5254\n    arc_challenge: 0.8336\n    humaneval: 0.1585\n- exp_id: exp_001_eval_3B_d100_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.659\n      correct: 4347\n      total: 6596\n    gsm8k:\n      accuracy: 0.5833\n      correct: 133\n      total: 228\n    arc_challenge:\n      accuracy: 0.8092\n      correct: 564\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d000_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6474\n      correct: 4270\n      total: 6596\n    gsm8k:\n      accuracy: 0.0482\n      correct: 11\n      total: 228\n    arc_challenge:\n      accuracy: 0.8235\n      correct: 574\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6324\n    gsm8k_exact_match: 0.6308\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass1: 0.1037\n- exp_id: exp_001_eval_3B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6461\n    GSM8K: 0.5\n    ARC: 0.8192\n    HumanEval: 0.0769\n- exp_id: exp_001_eval_3B_d025_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6615\n    GSM8K: 0.4254\n    ARC: 0.8121\n    HumanEval: 0.1538\n- exp_id: exp_002_signals_3B_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_3B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1464\n    mean_token_accuracy: 0.734\n    train_runtime_s: 14584\n    total_steps: 3384\n    epoch: 1\n    entropy: 1.1807\n- exp_id: exp_001_sft_3B_d100_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1805\n    mean_token_accuracy: 0.7348\n    train_runtime_seconds: 17608.59\n    train_steps: 4159\n    epoch: 1\n    train_samples_per_second: 3.778\n    entropy: 1.231\n- exp_id: exp_004_sim_sweep_v6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions_ok: 9\n    conditions_total: 12\n    conditions_failed: auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\n    gamma_bias_range: '[-0.025, +0.056]'\n    gamma_rmse_range: '[0.005, 0.085]'\n    ci95_coverage_range: '[0.8, 1.0]'\n    theta_corr_range: '[0.947, 0.972]'\n    note: 9/12 sufficient for Claim 1 identifiability\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_acc: 0.6471\n    gsm8k_acc: 0.3421\n    arc_challenge_acc: 0.8164\n    humaneval_pass1: 0.0769\n    mmlu_n: 6596\n    gsm8k_n: 228\n    arc_challenge_n: 697\n    humaneval_n: 26\n- exp_id: exp_002_signals_3B_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6565\n      correct: 4330\n      total: 6596\n    gsm8k:\n      accuracy: 0.5877\n      correct: 134\n      total: 228\n    arc_challenge:\n      accuracy: 0.8164\n      correct: 569\n      total: 697\n    humaneval:\n      pass@1: 0.0769\n      correct: 2\n      total: 26\n- exp_id: exp_002_signals_3B_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.6308\n- exp_id: exp_002_signals_3B_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_004_sim_sweep_extreme_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions: 8\n    seeds_per_condition: 10\n    total_time_hours: 11.1\n    gamma2_avg_bias: 0.017\n    gamma2_avg_rmse: 0.101\n    gamma2_ci95_coverage: 1\n    gamma4_avg_bias: -0.106\n    gamma4_avg_rmse: 0.226\n    gamma4_ci95_coverage: 0.925\n    theta_corr_range:\n    - 0.914\n    - 0.969\n- exp_id: exp_002_signals_3B_v6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_s123_para_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d000_s123_para_aligned:\n      mmlu: 0.6111\n      gsm8k: 0.5921\n      arc_challenge: 0.7547\n      humaneval: 0.1538\n    d005_s123_para_aligned:\n      mmlu: 0.614\n      gsm8k: 0.5439\n      arc_challenge: 0.7475\n      humaneval: 0.0769\n    d025_s123_para_aligned:\n      mmlu: 0.6145\n      gsm8k: 0.5482\n      arc_challenge: 0.7504\n      humaneval: 0.1923\n    d100_s123_para_aligned:\n      mmlu: 0.629\n      gsm8k: 0.5307\n      arc_challenge: 0.7834\n      humaneval: 0.2308\n- exp_id: exp_001_sft_3B_d000_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1324\n    epoch: 1\n    steps: 3125\n- exp_id: exp_001_sft_3B_d005_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.0822\n    epoch: 1\n    steps: 3177\n    train_runtime_sec: 14913.5\n    mean_token_accuracy: 0.7511\n- exp_id: exp_001_sft_3B_d100_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1795\n    train_runtime_sec: 17645\n    train_samples_per_second: 3.771\n    train_steps_per_second: 0.236\n    final_epoch: 1\n    total_steps: 4159\n    mean_token_accuracy: 0.7186\n    entropy: 1.296\n- exp_id: exp_001_sft_3B_d000_v4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.633\n      para_aligned: 0.6598\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.7074\n      para_aligned: 0.5746\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8251\n      para_aligned: 0.8049\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1159\n      para_aligned: 0\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_002_signals_3B_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    benchmarks:\n    - mmlu\n    - gsm8k\n    - arc_challenge\n    signals:\n    - s1_embedding\n    - s2_minkpp\n    - s4_selfcritique\n    signal_files: 9\n    merged_files: 3\n    output_dir: /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\n- exp_id: exp_001_sft_3B_d025_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_v3_s42_batch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_3B_d025_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8_recovery\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_aligned\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6431\n    gsm8k_para: 0.0526\n    arc_para: 0.8106\n    humaneval_para: 0.1923\n- exp_id: exp_002_signals_3B_d100_s123_v9\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v9\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_05B_s123_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.6307\n      para_aligned: 0.6431\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.141\n      para_aligned: 0.0526\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8242\n      para_aligned: 0.8106\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1402\n      para_aligned: 0.1923\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_001_eval_3B_d005_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6308\n    gsm8k: 0.4147\n    arc: 0.8251\n    humaneval: 0.1341\n    mmlu_para: 0.6471\n    gsm8k_para: 0.3421\n    arc_para: 0.8164\n    humaneval_para: 0.0769\n- exp_id: exp_001_eval_3B_d100_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    aligned:\n      mmlu: 0.6364\n      gsm8k: 0.7036\n      arc_challenge: 0.8208\n      humaneval_correct: 26/164\n    para_aligned:\n      mmlu: 0.6674\n      gsm8k: 0.5702\n      arc_challenge: 0.8106\n      humaneval_correct: 2/26\n- exp_id: exp_002_signals_05B_s123_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s42_a32_para\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_para: 0.8106\n    humaneval_para: 0\n    mmlu_para: completed_6596_items\n    gsm8k_para: completed\n    output_dir: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\n    sentinel: .done exists\n- exp_id: exp_002_signals_15B_s123_batch\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_002_signals_3B_d005_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_d000_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    signals_completed: 9\n    signals_failed: 0\n    runtime_minutes: 189\n    benchmarks:\n      mmlu:\n        n_items: 14042\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      gsm8k:\n        n_items: 1319\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      arc_challenge:\n        n_items: 1172\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n    output_files:\n      signal_s1_embedding_mmlu.json: 7.6M\n      signal_s1_embedding_gsm8k.json: 717K\n      signal_s1_embedding_arc_challenge.json: 650K\n      signal_s2_minkpp_mmlu.json: 2.8M\n      signal_s2_minkpp_gsm8k.json: 266K\n      signal_s2_minkpp_arc_challenge.json: 245K\n      signal_s4_selfcritique_mmlu.json: 3.2M\n      signal_s4_selfcritique_gsm8k.json: 310K\n      signal_s4_selfcritique_arc_challenge.json: 284K\n- exp_id: exp_002_signals_3B_d100_a32_s42\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_mmlu_domain_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    Other_gamma: 1.34\n    Business_Law_gamma: 0.61\n    Humanities_gamma: 0.47\n    STEM_Science_gamma: 0.36\n    STEM_CS_Eng_gamma: 0.29\n    Social_Sciences_gamma: 0.28\n    Medical_gamma: 0.27\n    STEM_Math_gamma: -0.55\n    all_rhat_max: 1.008\n    divergent_transitions: 0\n    n_domains: 8\n    n_models: 16\n- exp_id: exp_001_eval_3B_instruct_aligned_para\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006_pooled_rrf_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k:\n      n_models: 11\n      n_items: 300\n      gamma_mean: 0.0128\n      gamma_ci95:\n      - -0.99\n      - 1.0187\n      rhat: 1.0072\n      ess: 1300\n      divergences: 0\n      ppp: 0.663\n      raw_mae: 0.1501\n      cal_mae: 0.0373\n      delta_mae: 0.1128\n    arc_challenge:\n      n_models: 5\n      n_items: 300\n      gamma_mean: 1.2259\n      gamma_ci95:\n      - -0.2711\n      - 2.8571\n      rhat: 1.0072\n      ess: 1480\n      divergences: 0\n      ppp: 0\n      raw_mae: 0.0042\n      cal_mae: 0.0682\n      delta_mae: -0.064\n- exp_id: exp006_pooled_rrf_irt_05b_15b_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_pooled_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k_gamma: 0.0128\n    gsm8k_ci95: '[-0.990, 1.019]'\n    gsm8k_rhat: 1.0072\n    gsm8k_ess: 1300\n    gsm8k_ppp: 0.663\n    gsm8k_raw_mae: 0.1501\n    gsm8k_cal_mae: 0.0373\n    gsm8k_delta_mae: 0.1128\n    gsm8k_n_models: 11\n    arc_gamma: 1.2259\n    arc_ci95: '[-0.271, 2.857]'\n    arc_rhat: 1.0072\n    arc_ess: 1480\n    arc_ppp: 0\n    arc_raw_mae: 0.0042\n    arc_cal_mae: 0.0682\n    arc_delta_mae: -0.064\n    arc_n_models: 5\n    n_items_subsampled: 300\n- exp_id: exp_006_pooled_irt_05b_15b_arc_2pl\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_002_signals_15B_d100_s123_cuda2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d000_s42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T11:05:16.504Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T11:05:16.504Z",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49"
}
```

---

## Round 1

18 recorded events

### User

_source line 3 · 2026-05-16T11:05:16.529Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Core characterization patterns hold directionally but with reduced statistical strength; IRT calibration adds no significant MAE advantage over linear regression; coverage remains poor
核心假设：['ARC γ<0 holds at N=24 but CI widens or barely excludes zero at 3B scale alone', "MMLU domain heterogeneity: pattern/ranking preserved but only 2-3/8 domains individually significant; Simpson's paradox argument weakened", 'Multi-family: γ sign consistent but magnitude differs substantially (Llama less susceptible)', 'IRT MAE ≈ B4 linear on ARC (bootstrap CI overlaps, p>0.10)', 'Coverage stays 30-50% at 95% CI despite N=24', 'S2 reversal confirmed at 0.5B only; 3B shows d≈0 (ineffective, not reversed)']
关键指标范围：{'arc_gamma': [-1.8, -0.5], 'arc_gamma_ci_excludes_zero': 'borderline (lower bound between -0.3 and 0)', 'arc_calibrated_mae': [0.03, 0.05], 'arc_irt_vs_linear_mae_gap': [-0.005, 0.01], 'mmlu_domain_gamma_range': [1.0, 1.8], 'mmlu_domains_significant': [2, 4], 'coverage_95_arc': [0.3, 0.55], 'coverage_95_gsm8k': ['N/A — gating rejects'], 's1_auc_d005': [0.93, 0.98], 's2_cohens_d_reversal': [-2.0, -0.8], 'n_models_pooled': [16, 24], 'multi_family_gamma_rank_tau': [0.4, 0.7], 'gsm8k_gamma_ci_includes_zero': True}
叙事方向：Adjust claims: (1) Characterization remains primary but 'domain heterogeneity' downgraded to 'suggestive pattern requiring larger-scale confirmation' — present ranking/direction, not significance. (2) Signal failure claim narrowed to 'scale-dependent' (0.5B specific). (3) Identifiability claim strengthened as explanation for WHY calibration doesn't outperform linear — structural domain-method mismatch at N<50 is the real finding. (4) Calibration claim further demoted: IRT's value is interpretable per-item decomposition and theoretical grounding, NOT better point estimates. Add honest 'When NOT to calibrate' section as equal-weight contribution. Supplement with 1-2 additional negative results (GSM8K overcorrection, coverage collapse) framed as diagnostic insights.

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
  "promptId": "12f74f9c-3682-43f5-ba1f-5543432c9fc5",
  "type": "user",
  "uuid": "d7bdc214-1f33-4294-818f-e4743820d942",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T11:05:16.526Z_

```json
{
  "parentUuid": "d7bdc214-1f33-4294-818f-e4743820d942",
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
  "uuid": "7674a8cc-c658-4367-bc2f-ddef599e0217",
  "timestamp": "2026-05-16T11:05:16.526Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T11:05:16.527Z_

```json
{
  "parentUuid": "7674a8cc-c658-4367-bc2f-ddef599e0217",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ac333319-d44c-4209-bf7f-4ef57c2eb3e1",
  "timestamp": "2026-05-16T11:05:16.527Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Core characterization patterns hold directionally but with reduced statistical strength; IRT calibration adds no significant MAE advantage over linear re…",
  "leafUuid": "ac333319-d44c-4209-bf7f-4ef57c2eb3e1",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier contamination calibration analysis",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49"
}
```

---

### Assistant

_source line 8 · 2026-05-16T11:05:41.391Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each "planned" experiment in the experiment_plan, based on the "median" tier definition they've provided. Let me identify the planned experiments:

1. **exp-015** (sft_d100_qc_only) - status: planned
2. **exp-007** (scale_bridging_7b) - status: planned
3. **exp-014** (multi_family_validation) - status: planned
4. **exp-009** (rl_observational_case_study) - status: planned
5. **exp-012** (observational_72b) - status: planned


6. **exp-013** (closed_weight_2signal_mode) - status: planned

Now I'm working through what the median tier means for each experiment. The median tier shows directional patterns but with weaker statistical power—IRT calibration doesn't improve over linear regression, coverage stays poor, and key assumptions like the ARC γ<0 relationship hold directionally at N=24 but become uncertain at larger scales. For MMLU, the domain patterns persist but only a few domains show individual significance, and the Simpson's paradox argument loses force.

Across the multi-family results, the γ sign stays consistent but the magnitude shifts notably, with Llama showing less susceptibility to the effect. IRT and linear regression perform similarly on ARC with overlapping confidence intervals. Coverage remains stuck in the 30-50% range even at 95% CI. The S2 reversal only appears at 0.5B scale; at 3B it flattens to near zero, suggesting the effect doesn't actually reverse at larger scales.

Now I'm laying out the detailed predictions for each planned experiment. For **exp-015** (sft_d100_qc_only), I'm using only the QC-pass paraphrases—about 7500 items from the full set—for d100 SFT on Qwen2.5-0.5B. In the median tier, QC-only contamination should still produce measurable effects, though the comparison against the all-paraphrases baseline might show a smaller gap than expected.

For **exp-007** (scale_bridging_7b), I'm testing 7B across five dosage levels. At this scale, the model should demonstrate near-immunity to contamination with attenuated γ that may not reach significance. **exp-014** (multi_family_validation) uses Llama-3.2-1B or Pythia-1.4B at three dosage levels, where I expect the γ sign to hold but with substantially different magnitudes across families, and the rank correlation for multi-family gamma should fall between 0.4 and 0.7.

For **exp-009** (rl_observational_case_study), I'm applying the contamination signals to RL-trained models, which should yield wider confidence intervals and only directional findings. **exp-012** (observational_72b) involves 72B inference only.

Now I'm extending this to ecological validity with **exp-013** (closed_weight_2signal_mode), where I'm testing a two-signal mode combining ConStat and Self-Critique, expecting degraded performance in the median tier. Let me work through the detailed predictions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac333319-d44c-4209-bf7f-4ef57c2eb3e1",
  "isSidechain": false,
  "requestId": "req_011Cb68zC6f9L9u5311Fzw8W",
  "type": "assistant",
  "uuid": "bc432043-45a5-4396-93ae-808c29838fd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKAn1iNrMAAa1GaJU56fnp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 38901,
      "cache_read_input_tokens": 11841,
      "output_tokens": 903,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 903,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 38901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38901
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

_source line 9 · 2026-05-16T11:05:41.400Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017bRUXMc9x2FzpMm5YZzKK4`</summary>

```json
{
  "pattern": "**/experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc432043-45a5-4396-93ae-808c29838fd7",
  "isSidechain": false,
  "requestId": "req_011Cb68zC6f9L9u5311Fzw8W",
  "type": "assistant",
  "uuid": "0e7ff73b-f81e-4e2f-90c0-332298168ae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKAn1iNrMAAa1GaJU56fnp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 38901,
      "cache_read_input_tokens": 11841,
      "output_tokens": 903,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 903,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 38901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38901
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

_source line 10 · 2026-05-16T11:05:41.419Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011dN8aBVUMhXApZagjdDfic`</summary>

```json
{
  "pattern": "**/discussion_notes*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e7ff73b-f81e-4e2f-90c0-332298168ae9",
  "isSidechain": false,
  "requestId": "req_011Cb68zC6f9L9u5311Fzw8W",
  "type": "assistant",
  "uuid": "23e366ab-d1dc-4ecc-9d02-6daf87907350",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKAn1iNrMAAa1GaJU56fnp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 38901,
      "cache_read_input_tokens": 11841,
      "output_tokens": 903,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 903,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 38901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38901
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

_source line 11 · 2026-05-16T11:05:41.533Z_

<details><summary>↩ Tool result · `toolu_017bRUXMc9x2FzpMm5YZzKK4`</summary>

```text
projects/contamcal-irt-calibration/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e7ff73b-f81e-4e2f-90c0-332298168ae9",
  "isSidechain": false,
  "promptId": "12f74f9c-3682-43f5-ba1f-5543432c9fc5",
  "type": "user",
  "uuid": "ae6b8af5-06bf-4e92-80f4-6a1a78643d0d",
  "toolUseResult": {
    "filenames": [
      "projects/contamcal-irt-calibration/experiment_plan.yaml"
    ],
    "durationMs": 123,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0e7ff73b-f81e-4e2f-90c0-332298168ae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T11:05:41.563Z_

<details><summary>↩ Tool result · `toolu_011dN8aBVUMhXApZagjdDfic`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23e366ab-d1dc-4ecc-9d02-6daf87907350",
  "isSidechain": false,
  "promptId": "12f74f9c-3682-43f5-ba1f-5543432c9fc5",
  "type": "user",
  "uuid": "c86d3e7b-d823-4766-b57e-fbec3bb0c605",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 137,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "23e366ab-d1dc-4ecc-9d02-6daf87907350",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T11:05:45.613Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QRhb3amoEb1TWwNaTHYVfQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
  "offset": 0,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c86d3e7b-d823-4766-b57e-fbec3bb0c605",
  "isSidechain": false,
  "requestId": "req_011Cb692321wdTu4GqmJzF64",
  "type": "assistant",
  "uuid": "565642b9-9a16-44d4-96bc-e6ab18eec72c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GgYdfAUChW8ZEcy9SfG92o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 50742,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 50742,
          "cache_creation_input_tokens": 980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 980
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

_source line 14 · 2026-05-16T11:05:45.624Z_

<details><summary>↩ Tool result · `toolu_01QRhb3amoEb1TWwNaTHYVfQ`</summary>

```text
0	# ContamCal Experiment Plan
1	# Each experiment maps to Core Claims in paper_framing.md
2	# Priority: P0 = must-run, P1 = important, P2 = bonus
3	
4	experiments:
5	  # ============================================================
6	  # P0: Core experiments — must complete for submission
7	  # ============================================================
8	
9	  - id: exp-001
10	    name: controlled_sft_injection
11	    claim: 1
12	    description: >
13	      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels
14	      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).
15	      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total
16	      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition
17	      for key metrics (mean ± std).
18	      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or
19	      equivalent) with controlled semantic similarity — following methodology
20	      of "Rethinking Benchmark and Contamination" (arXiv 2023). Target:
21	      high semantic similarity (cosine >0.85) but low lexical overlap
22	      (BLEU <0.3) to evade n-gram decontamination while preserving
23	      contamination effect. Quality validation: automated similarity metrics
24	      + human spot-check on 50 random pairs per benchmark.
25	    priority: P0
26	    gpu_budget_hours: 50
27	    deps: []
28	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
29	    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]
30	    seeds: 3
31	    registry_id: exp_001_sft_injection
32	    # Multi-run experiment; related successful registry entries:
33	    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,
34	    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,
35	    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,
36	    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,
37	    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,
38	    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,
39	    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,
40	    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,
41	    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123
42	    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,
43	    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,
44	    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,
45	    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,
46	    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,
47	    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,
48	    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,
49	    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,
50	    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,
51	    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,
52	    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,
53	    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned
54	    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,
55	    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,
56	    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,
57	    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,
58	    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,
59	    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,
60	    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned
61	    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)
62	
63	  - id: exp-002
64	    name: stage1_signal_pipeline
65	    claim: 2
66	    description: >
67	      Compute 4 detection signals on all contaminated + clean models from exp-001:
68	      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),
69	      (b) Min-K%++ membership inference,
70	      (c) ConStat performance gap (original vs paraphrased items),
71	      (d) Self-Critique entropy collapse.
72	      Output: per-model-item exposure scores for each signal.
73	    priority: P0
74	    gpu_budget_hours: 20
75	    deps: [exp-001]
76	    registry_id: exp_002_signals_05B
77	    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)
78	    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed
79	
80	  - id: exp-003
81	    name: rrf_aggregation_ablation
82	    claim: 2
83	    description: >
84	      RRF fusion of 4 signals into composite per-item exposure score.
85	      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only
86	      (×4), (c) calibration-based weighted RRF variant, (d) false positive
87	      injection robustness check (inject FP at rates matching Duan et al. 2024).
88	      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.
89	    priority: P0
90	    gpu_budget_hours: 2
91	    deps: [exp-002]
92	    registry_id: exp_003_rrf_05B
93	    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)
94	
95	  - id: exp-004
96	    name: simulation_identifiability_sweep
97	    claim: 1
98	    also_supports: [3]
99	    description: >
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "565642b9-9a16-44d4-96bc-e6ab18eec72c",
  "isSidechain": false,
  "promptId": "12f74f9c-3682-43f5-ba1f-5543432c9fc5",
  "type": "user",
  "uuid": "f3bfa7fb-94ba-4767-9de2-7e86ffc1b791",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
      "content": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: 1\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n    registry_id: exp_001_sft_injection\n    # Multi-run experiment; related successful registry entries:\n    # SFT training: exp_001_sft_0pct_05B, exp_001_sft_0pct_15B, exp_001_sft_0pct_3B,\n    #   exp_001_sft_0pct_05B_s123, exp_001_sft_0pct_15B_s123, exp_001_sft_0pct_3B_s123,\n    #   exp_001_sft_d005_05B_v3, exp_001_sft_d005_15B, exp_001_sft_d005_3B,\n    #   exp_001_sft_05B_d005_s123, exp_001_sft_15B_d005_s123_v2, exp_001_sft_3B_d005_s123,\n    #   exp_001_sft_d025_05B_v3, exp_001_sft_d025_15B, exp_001_sft_d025_3B_v2,\n    #   exp_001_sft_05B_d025_s123_v2, exp_001_sft_15B_d025_s123_v2, exp_001_sft_3B_d025_s123,\n    #   exp_001_sft_d100_05B, exp_001_sft_d100_15B_v2, exp_001_sft_d100_3B_v2,\n    #   exp_001_sft_05B_d100_s123, exp_001_sft_15B_d100_s123, exp_001_sft_3B_d100_s123,\n    #   exp_001_sft_3B_d000_v2, exp_001_sft_3B_d000_s123\n    # Eval (aligned): exp_001_eval_05B_d000_s123_aligned, exp_001_eval_05B_d005_aligned,\n    #   exp_001_eval_05B_d025_aligned, exp_001_eval_05B_d100_aligned_v4,\n    #   exp_001_eval_05B_d005_s123_aligned, exp_001_eval_05B_d025_s123_aligned,\n    #   exp_001_eval_05B_d100_s123_aligned, exp_001_eval_15B_aligned_batch,\n    #   exp_001_eval_15B_d005_aligned_v2, exp_001_eval_15B_d025_aligned,\n    #   exp_001_eval_15B_d100_aligned, exp_001_eval_15B_d000_s123_aligned,\n    #   exp_001_eval_15B_d100_s123_aligned, exp_001_eval_3B_d000_aligned,\n    #   exp_001_eval_3B_d005_aligned, exp_001_eval_3B_d100_aligned,\n    #   exp_001_eval_3B_d000_v2_aligned, exp_001_eval_3B_d025_v2_aligned,\n    #   exp_001_eval_3B_d100_v2_aligned_v2, exp_001_eval_3B_d000_s123_aligned,\n    #   exp_001_eval_3B_d005_s123_aligned, exp_001_eval_3B_d025_s123_aligned,\n    #   exp_001_eval_3B_d100_v2_s123_aligned, exp_001_eval_3B_d000_v2_s123_aligned\n    # Eval (para_aligned): exp_001_eval_05B_d005_para_aligned, exp_001_eval_05B_d025_aligned_v2,\n    #   exp_001_eval_05B_d005_s123_para_aligned, exp_001_eval_15B_d025_para_aligned,\n    #   exp_001_eval_3B_d000_s42_para_aligned, exp_001_eval_3B_d100_s42_para_aligned,\n    #   exp_001_eval_3B_d000_v2_para_aligned, exp_001_eval_3B_d000_v2_para_aligned_v2,\n    #   exp_001_eval_3B_d025_v2_para_aligned, exp_001_eval_3B_d100_v2_para_aligned,\n    #   exp_001_eval_3B_d005_s123_para_aligned, exp_001_eval_3B_d025_s123_para_aligned,\n    #   exp_001_eval_3B_d100_s123_para_aligned_v2, exp_001_eval_3B_d000_v2_s123_para_aligned\n    # Excluded from IRT pool: d000_s42 and d005_s42 experiments (lr=2e-4 confound, D076)\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: 2\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n    registry_id: exp_002_signals_05B\n    # Related: exp002-signals-1p5B (DONE/success), exp002-signal-d025-05B (DONE/success)\n    # Note: 3B signal runs (exp_002_signals_3B v1-v4) all failed/killed\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: 2\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n    registry_id: exp_003_rrf_05B\n    # Related: exp_003_mmlu_item_aligned_gap (DONE/success)\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: 1\n    also_supports: [3]\n    description: >",
      "numLines": 100,
      "startLine": 0,
      "totalLines": 320
    }
  },
  "sourceToolAssistantUUID": "565642b9-9a16-44d4-96bc-e6ab18eec72c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-16T11:05:45.657Z_

````json
{
  "parentUuid": "f3bfa7fb-94ba-4767-9de2-7e86ffc1b791",
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
  "uuid": "91b02b92-d608-4a65-a121-278add47e20c",
  "timestamp": "2026-05-16T11:05:45.657Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Core characterization patterns hold directionally but with reduced statistical strength; IRT calibration adds no significant MAE advantage over linear re…",
  "leafUuid": "91b02b92-d608-4a65-a121-278add47e20c",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier contamination calibration analysis",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49"
}
```

---

### Assistant

_source line 18 · 2026-05-16T11:08:50.295Z_

Based on the existing experimental data, registry results, and the median tier definition, I'll construct the detailed predictions for each planned experiment.

```yaml
tier: median
narrative_guidance: >
  Adjust claims: (1) Characterization remains primary but 'domain heterogeneity' downgraded to
  'suggestive pattern requiring larger-scale confirmation' — present ranking/direction, not significance.
  (2) Signal failure claim narrowed to 'scale-dependent' (0.5B specific).
  (3) Identifiability claim strengthened as explanation for WHY calibration doesn't outperform linear —
  structural domain-method mismatch at N<50 is the real finding.
  (4) Calibration claim further demoted: IRT's value is interpretable per-item decomposition and
  theoretical grounding, NOT better point estimates. Add honest 'When NOT to calibrate' section as
  equal-weight contribution. Supplement with 1-2 additional negative results (GSM8K overcorrection,
  coverage collapse) framed as diagnostic insights.

imagined_experiments:
  - name: "sft_d100_qc_only"
    plan_id: "exp-015"
    description: >
      100% dosage SFT using only QC-pass paraphrases (7547/16697 items) on Qwen2.5-0.5B.
      Isolates noisy vs clean contamination confound. Compare calibration metrics against
      exp-001 d100 (all paraphrases) to quantify effect of noisy contamination on IRT estimates.
    expected_results:
      # Training metrics (comparable to exp_001_sft_d100_05B)
      train_loss: 1.58
      token_accuracy: 0.670
      training_time_min: 55
      total_steps: 2800
      # Eval accuracy — QC-only paraphrases are higher quality, stronger contamination signal
      # but fewer items (7547 vs 16697) → net effect: slightly stronger per-item contamination
      # but lower total volume → moderate accuracy shift vs full d100
      mmlu_accuracy: 0.258
      gsm8k_accuracy: 0.355
      arc_challenge_accuracy: 0.255
      humaneval_pass1: 0.073
      # Comparison to exp_001 d100 (all paraphrases): mmlu=0.233, arc=0.294
      # QC-only: MMLU slightly higher (cleaner signal aids learning), ARC lower
      # (fewer contaminated items = less capacity displacement but also less forgetting mitigation)
      mmlu_delta_vs_d100_all: +0.025
      arc_delta_vs_d100_all: -0.039
      # IRT calibration comparison
      irt_gamma_qc_only: -0.95
      irt_gamma_qc_only_ci: [-2.1, 0.2]
      irt_gamma_all_paraphrases: -1.21
      gamma_difference_significant: false
      mae_qc_only: 0.038
      mae_all_paraphrases: 0.035
      mae_gap_pp: 0.003
      coverage_95_qc_only: 0.35
      coverage_95_all: 0.33
    result_rationale: >
      In the median tier, QC-only filtering produces modestly cleaner contamination signal (higher
      per-item semantic fidelity) but removes 55% of items, reducing total contamination volume.
      The net effect on 0.5B is near-neutral: the model's limited capacity means it cannot
      fully exploit either the noisier-but-larger or cleaner-but-smaller contamination set.
      IRT γ estimate shifts slightly toward zero (less extreme forgetting) because QC-pass items
      have higher semantic similarity → less distribution shift → less catastrophic forgetting.
      However, the difference is NOT statistically significant (overlapping CIs) because N=8 models
      provides insufficient power to distinguish the two conditions. This supports the paper's
      narrative that contamination quality modulates effect size but the IRT framework's primary
      limitation is N, not signal noise. Calibration MAE remains comparable — the noise propagation
      finding (exp-005: CI insensitive to σ_e) already showed that exposure noise is not the
      binding constraint.
    tables:
      - name: "Table: QC-only vs All-paraphrases comparison (0.5B, d100)"
        columns: [metric, qc_only, all_paraphrases, delta, significant]
        rows:
          - [MMLU accuracy, 0.258, 0.233, +0.025, "no (p=0.18)"]
          - [ARC accuracy, 0.255, 0.294, -0.039, "no (p=0.22)"]
          - [GSM8K accuracy, 0.355, 0.365, -0.010, "no"]
          - [IRT γ (ARC), -0.95, -1.21, +0.26, "no (CI overlap)"]
          - [Calibrated MAE, 0.038, 0.035, +0.003, "no"]
          - [Coverage 95%, 0.35, 0.33, +0.02, "no"]
    figures_description:
      - "Bar chart comparing γ estimates with 95% CIs for QC-only vs all-paraphrases conditions. Both CIs overlap substantially, showing non-significant difference."
    analysis: >
      Result supports the identifiability-first narrative: the binding constraint on calibration
      quality is N_models (structural domain-method mismatch), not exposure signal noise.
      QC filtering improves signal quality but doesn't materially change IRT outcomes at N=8.
      Paper uses this as supplementary evidence that the 'When NOT to calibrate' guidance
      is driven by N limitations, not measurement error in Stage 1.

  - name: "scale_bridging_7b"
    plan_id: "exp-007"
    description: >
      Qwen2.5-7B controlled SFT injection at 5 dosage levels (0%, 5%, 25%, 50%, 100%).
      Validates calibration accuracy scales to larger models. Multi-GPU node required.
    expected_results:
      # Training
      training_hours_per_run: 6.5
      total_gpu_hours: 32.5
      # Eval — 7B is largely immune to MC contamination effects (scale-dependent claim)
      d000_mmlu: 0.715
      d000_gsm8k: 0.785
      d000_arc: 0.885
      d000_humaneval: 0.280
      d005_mmlu: 0.716
      d005_gsm8k: 0.787
      d005_arc: 0.884
      d005_humaneval: 0.295
      d025_mmlu: 0.718
      d025_gsm8k: 0.790
      d025_arc: 0.883
      d025_humaneval: 0.310
      d100_mmlu: 0.722
      d100_gsm8k: 0.795
      d100_arc: 0.878
      d100_humaneval: 0.350
      # Scale attenuation: max delta across dosages
      mmlu_max_delta_pp: 0.7
      gsm8k_max_delta_pp: 1.0
      arc_max_delta_pp: -0.7
      humaneval_max_delta_pp: 7.0
      # IRT results (if fitted with 7B data pooled into N=24 set)
      arc_gamma_7b_only: -0.15
      arc_gamma_7b_ci: [-0.8, 0.5]
      arc_gamma_ci_excludes_zero: false
      mmlu_gamma_7b_only: 0.08
      mmlu_gamma_7b_ci: [-0.6, 0.7]
      # Signal detection at 7B
      s1_d005_auc_7b: 0.96
      s2_d005_auc_7b: 0.52
      s2_d005_cohens_d_7b: 0.08
      # Calibration at 7B
      mae_calibrated_7b: 0.004
      mae_raw_7b: 0.003
      calibration_unnecessary: true
    result_rationale: >
      In the median tier, 7B demonstrates near-immunity to MC benchmark contamination via SFT,
      confirming the scale-dependent characterization. The mechanism: 7B has sufficient capacity
      that SFT contamination occupies a negligible fraction of model parameters — no catastrophic
      forgetting (unlike 0.5B) and no detectable inflation on MC benchmarks (unlike the pattern
      at smaller scales). ARC shows a tiny negative trend (-0.7pp at d100) but this is within
      noise. HumanEval shows the only meaningful dose-response (+7pp), consistent with 1.5B
      findings where code generation was the only benchmark affected at larger scales.
      
      IRT γ at 7B alone is effectively zero with wide CI — contamination effect is undetectable
      at this scale. This is the "near-immunity" regime in the three-regime taxonomy. The critical
      implication: calibration is unnecessary at 7B (raw MAE already < 0.5pp), and IRT correctly
      identifies this via non-significant γ. This validates the calibration gating criterion:
      when γ CI includes zero, report raw scores.
      
      S2 (Min-K++) at 7B shows d≈0 (neither reversed nor effective) — distinct from the
      directional reversal at 0.5B. This narrows the "signal failure" claim to be explicitly
      scale-dependent: reversal at 0.5B, ineffectiveness at 3B/7B, unknown at larger scales.
      The reduced statistical strength in median tier means we cannot claim a clean monotonic
      relationship between scale and γ magnitude — just the directional pattern.
    tables:
      - name: "Table: Contamination effect by scale (ARC-Challenge)"
        columns: [scale, d000_acc, d100_acc, delta_pp, gamma, gamma_ci_excludes_zero]
        rows:
          - [0.5B, 0.470, 0.294, -17.6, -1.21, "borderline (0.12)"]
          - [1.5B, 0.772, 0.769, -0.3, -0.18, "no"]
          - [3B, 0.828, 0.840, +1.2, -0.42, "no"]
          - [7B, 0.885, 0.878, -0.7, -0.15, "no"]
      - name: "Table: Three-regime taxonomy evidence"
        columns: [regime, scale, arc_delta_pp, mechanism, gamma_significant]
        rows:
          - [Catastrophic forgetting, 0.5B, -17.6, "Capacity displacement", "borderline"]
          - [Mild perturbation, 1.5B-3B, "-0.3 to +1.2", "Absorbed without displacement", "no"]
          - [Near-immunity, 7B, -0.7, "Negligible relative to capacity", "no"]
    figures_description:
      - "Line plot: contamination dosage (x) vs accuracy delta from d000 (y), one line per scale (0.5B/1.5B/3B/7B). Shows 0.5B steep negative slope, others flat. ARC-Challenge."
      - "Heatmap: scale × dosage → γ magnitude, showing attenuation with scale."
    analysis: >
      7B data strengthens the scale-dependent characterization but weakens the overall
      statistical case for γ as a useful calibration parameter. At 7B, γ≈0 means ContamCal
      correctly identifies 'no calibration needed' — this is actually a success of the
      gating criterion, not a failure. Paper narrative: ContamCal's value at large scales
      is diagnostic (confirming no contamination effect) rather than corrective. The three-regime
      taxonomy holds directionally but only the 0.5B regime has borderline-significant γ
      when fitted alone — the pooled N=24 analysis is needed for statistical power.

  - name: "multi_family_validation"
    plan_id: "exp-014"
    description: >
      Controlled SFT injection on Llama-3.2-1B at 3 dosage levels (0%, 25%, 100%).
      Validates that identifiability boundaries and calibration accuracy generalize
      beyond Qwen2.5. Addresses single model family limitation.
    expected_results:
      # Training
      training_hours_per_run: 3.5
      total_gpu_hours: 10.5
      # Eval — Llama-3.2-1B baseline lower than Qwen2.5-1.5B on most benchmarks
      d000_mmlu: 0.465
      d000_gsm8k: 0.420
      d000_arc: 0.625
      d000_humaneval: 0.095
      d025_mmlu: 0.460
      d025_gsm8k: 0.425
      d025_arc: 0.610
      d025_humaneval: 0.110
      d100_mmlu: 0.445
      d100_gsm8k: 0.435
      d100_arc: 0.570
      d100_humaneval: 0.125
      # Contamination effects — Llama less susceptible than Qwen at comparable scale
      arc_delta_d100_pp: -5.5
      mmlu_delta_d100_pp: -2.0
      gsm8k_delta_d100_pp: +1.5
      # Compare to Qwen2.5-0.5B (closest scale): arc_delta=-17.6pp
      llama_vs_qwen_susceptibility_ratio: 0.31
      # IRT γ
      arc_gamma_llama: -0.75
      arc_gamma_llama_ci: [-1.8, 0.3]
      arc_gamma_ci_excludes_zero: false
      # Cross-family consistency
      gamma_sign_consistent_arc: true
      gamma_sign_consistent_gsm8k: true
      gamma_magnitude_ratio_llama_vs_qwen: 0.55
      multi_family_gamma_rank_tau: 0.60
      # Signal effectiveness on Llama
      s1_d005_auc_llama: 0.94
      s2_d005_auc_llama: 0.48
      s2_d100_cohens_d_llama: -0.85
    result_rationale: >
      In the median tier, Llama-3.2-1B shows the same directional pattern as Qwen (ARC forgetting,
      GSM8K mild inflation) but with substantially reduced magnitude. The γ sign is consistent
      (negative for ARC) but magnitude is roughly half that of Qwen at comparable scale.
      This is expected: Llama-3.2-1B has different architecture (GQA, different tokenizer,
      different pre-training data distribution) which affects how SFT contamination interacts
      with stored knowledge. The rank correlation (τ=0.60) is moderate — consistent direction
      but different magnitude means the benchmarks don't perfectly rank-order in susceptibility
      across families.
      
      Critically, the γ CI for Llama alone does NOT exclude zero — this is the reduced statistical
      strength characteristic of median tier. Only when pooled with Qwen data (raising N toward 24)
      does the combined γ become borderline significant. This means the multi-family finding is
      'directionally consistent' but not independently confirmatory at the individual-family level.
      
      S2 (Min-K++) shows a weaker reversal on Llama (d=-0.85 vs d=-1.98 on Qwen at 0.5B),
      still negative but less extreme. This is consistent with the 'scale-dependent' signal
      failure narrative: Llama-3.2-1B at 1B parameters is between 0.5B and 1.5B Qwen in terms
      of effective capacity, so the reversal is attenuated. S1 remains robust (AUC=0.94).
    tables:
      - name: "Table: Cross-family contamination susceptibility"
        columns: [family, scale, arc_d100_delta_pp, arc_gamma, gamma_sign, ci_excludes_zero]
        rows:
          - [Qwen2.5, 0.5B, -17.6, -1.21, negative, "borderline"]
          - [Qwen2.5, 1.5B, -0.3, -0.18, negative, "no"]
          - [Qwen2.5, 3B, +1.2, -0.42, negative, "no"]
          - [Llama-3.2, 1B, -5.5, -0.75, negative, "no"]
      - name: "Table: Signal effectiveness cross-family"
        columns: [signal, metric, Qwen_0.5B, Llama_1B, consistent]
        rows:
          - [S1 embedding, "d005 AUC", 0.979, 0.94, "yes"]
          - [S2 Min-K++, "d005 AUC", 0.465, 0.48, "yes (both fail)"]
          - [S2 Min-K++, "d100 Cohen's d", -1.98, -0.85, "yes (both negative)"]
          - [S4 Self-Critique, "d005 AUC", 0.481, 0.50, "yes (both fail)"]
    figures_description:
      - "Grouped bar chart: ARC accuracy delta (d100-d000) by model family and scale. Shows Llama less susceptible than Qwen at comparable scale."
      - "Scatter plot: Qwen γ_k vs Llama γ_k by benchmark, with identity line. Points cluster in same quadrant but not on diagonal (consistent sign, different magnitude)."
    analysis: >
      Multi-family result confirms contamination susceptibility is partially a benchmark property
      (ARC consistently shows forgetting) but magnitude is model-family-dependent. This weakens
      the strongest form of the characterization claim ('contamination is a benchmark property')
      to the softer 'contamination direction is benchmark-determined but magnitude is
      family-modulated.' Kendall τ=0.60 provides moderate support. The paper presents this
      honestly: 'directional consistency across families with heterogeneous magnitude suggests
      contamination characterization requires per-family calibration for quantitative use.'

  - name: "rl_observational_case_study"
    plan_id: "exp-009"
    description: >
      Apply Self-Critique + available signals to existing RL-trained models:
      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.
      Fit IRT with wider CIs. Expected regret quantification for model selection.
      Near-zero γ check on known-clean benchmark (specificity test).
    expected_results:
      # Signal computation
      n_models_evaluated: 8
      s1_computable: true
      s2_computable: true
      s4_computable: true
      # ARC signals on instruct models
      s1_auc_instruct_d005_equivalent: 0.72
      s2_instruct_mean_score: 1.69
      s4_instruct_mean_score: -0.91
      # IRT fit (observational — no ground truth)
      arc_gamma_observational: -0.52
      arc_gamma_observational_ci: [-1.8, 0.8]
      arc_gamma_ci_excludes_zero: false
      mmlu_gamma_observational: 0.18
      mmlu_gamma_observational_ci: [-0.9, 1.3]
      gsm8k_gamma_observational: 0.35
      gsm8k_gamma_observational_ci: [-0.6, 1.3]
      # Specificity check (known-clean benchmark — use TriviaQA or similar)
      specificity_gamma: 0.05
      specificity_gamma_ci: [-0.7, 0.8]
      specificity_passes: true
      # Calibration CIs (much wider than controlled setting)
      mean_ci_width_observational: 0.12
      mean_ci_width_controlled: 0.07
      ci_ratio: 1.7
      # Expected regret: top-5 model selection
      regret_raw_top5: 0.015
      regret_calibrated_top5: 0.018
      regret_remove_rescore_top5: 0.012
      calibration_improves_selection: false
      # DeepSeek vs Qwen comparison
      deepseek_r1_arc_gamma_contribution: -0.3
      deepseek_s1_score_elevated: true
    result_rationale: >
      In the median tier, the observational case study produces directional but not statistically
      significant findings. Without ground-truth contamination labels, the IRT fit relies entirely
      on Stage 1 signal scores as exposure proxies. S1 (embedding similarity) on Instruct models
      is noisier than on controlled SFT models because RL post-training alters the relationship
      between training data exposure and embedding space proximity.
      
      ARC γ is negative (consistent with controlled findings) but CI widely includes zero — the
      observational setting lacks the statistical power of the controlled experiment. This is
      expected: without dosage variation, all models cluster near similar exposure levels,
      collapsing the range that IRT needs to estimate γ reliably.
      
      Expected regret analysis shows calibration does NOT improve model selection in this setting.
      Raw scores already rank models reasonably well (because contamination effects at 1.5B+ are
      small per the scale-dependent finding). Remove-and-rescore performs marginally better because
      it simply drops high-exposure items without the risk of IRT miscalibration. This is an honest
      negative result that reinforces the 'When NOT to calibrate' message: in observational settings
      with no dosage variation and large models, calibration overhead is not justified.
      
      Specificity check passes: γ≈0 on TriviaQA (a benchmark not in training data) confirms the
      framework doesn't hallucinate contamination effects where none exist. This is a valuable
      positive control.
    tables:
      - name: "Table: Observational γ estimates (Instruct + DeepSeek models)"
        columns: [benchmark, gamma, ci_lower, ci_upper, ci_excludes_zero, interpretation]
        rows:
          - [ARC-Challenge, -0.52, -1.8, 0.8, "no", "Directionally consistent with controlled (forgetting), underpowered"]
          - [MMLU, 0.18, -0.9, 1.3, "no", "Near-zero, consistent with scale-dependent attenuation"]
          - [GSM8K, 0.35, -0.6, 1.3, "no", "Non-significant, consistent with gating rejection"]
          - ["TriviaQA (specificity)", 0.05, -0.7, 0.8, "no", "PASS — no false positive"]
      - name: "Table: Expected regret — top-5 model selection"
        columns: [method, regret_pp, rank_tau_vs_clean, ci_width]
        rows:
          - [Raw scores, 1.5, 0.85, "N/A"]
          - [ContamCal calibrated, 1.8, 0.80, 0.12]
          - [Remove-and-rescore, 1.2, 0.88, "N/A"]
          - [Linear regression, 1.6, 0.83, 0.08]
    figures_description:
      - "Forest plot: γ estimates with 95% CIs for each benchmark in observational setting, with controlled setting estimates overlaid as reference. Shows consistency in direction but wider CIs."
      - "Scatter: raw model rank vs calibrated model rank (top-5 highlighted), showing minimal rank changes — calibration doesn't improve selection."
    analysis: >
      The observational case study is an honest demonstration of ContamCal's limitations
      in the wild. Without controlled dosage variation, the framework correctly identifies
      directional effects but lacks power for quantitative calibration. This supports the
      paper's 'When NOT to calibrate' section: observational settings with large models
      (≥1.5B) and no dosage variation are below the identifiability threshold. The specificity
      check is the key positive finding — validating that the framework doesn't produce
      false contamination diagnoses. Paper frames this as 'ContamCal as diagnostic tool
      (is there contamination?) rather than corrective tool (what's the true score?) in
      observational settings.'

  - name: "observational_72b"
    plan_id: "exp-012"
    description: >
      Qwen2.5-72B observational analysis (inference only, no SFT).
      Extends ecological validity to frontier model scale.
    expected_results:
      # Inference (no training)
      inference_gpu_hours: 12
      # Benchmark scores (72B — very strong baseline)
      mmlu_accuracy: 0.842
      gsm8k_accuracy: 0.905
      arc_challenge_accuracy: 0.945
      humaneval_pass1: 0.685
      # Signal computation
      s1_mean_exposure_mmlu: 0.42
      s1_mean_exposure_arc: 0.38
      s1_mean_exposure_gsm8k: 0.35
      s2_minkpp_mean: 1.72
      s4_selfcritique_mean: -0.88
      # IRT fit (single model contributes to observational pool)
      # Cannot estimate γ from single model — contributes to pooled analysis only
      contribution_to_pooled_n: 1
      pooled_n_after_72b: 9
      # Exposure scores relative to smaller models
      s1_72b_vs_3b_delta: +0.05
      s1_72b_relative_rank: "middle (not highest, not lowest)"
      # Position bias check (critical for 72B MC evaluation)
      position_bias_72b_mmlu: 0.02
      position_bias_72b_arc: 0.015
      position_bias_absent: true
    result_rationale: >
      In the median tier, 72B provides ecological validity but minimal statistical contribution.
      A single model cannot independently estimate γ — it only adds one data point to the pooled
      analysis. The 72B model's near-ceiling performance on ARC (94.5%) and strong performance
      on MMLU (84.2%) means contamination effects, if any, are masked by the model's genuine
      capability. This is the 'near-immunity' regime taken to its extreme.
      
      S1 exposure scores are moderate (not zero, because 72B's training data likely includes
      benchmark-adjacent content given its massive training corpus), but this doesn't imply
      contamination harm — it's the expected background exposure level for a frontier model.
      The key contribution is confirming that position bias (which invalidated 0.5B MC data)
      is absent at 72B, validating that logprob-based MC evaluation is reliable at frontier scale.
      
      The finding supports the scale-dependent narrative without adding statistical power.
      Paper uses 72B as a single sentence: 'Contamination effect at frontier scale (72B) is
      undetectable, consistent with the three-regime taxonomy.'
    tables:
      - name: "Table: 72B observational results"
        columns: [benchmark, accuracy, s1_mean_exposure, interpretation]
        rows:
          - [MMLU, 0.842, 0.42, "Strong performance, moderate background exposure"]
          - [ARC-Challenge, 0.945, 0.38, "Near-ceiling, exposure ≠ inflation"]
          - [GSM8K, 0.905, 0.35, "Strong, below ARC/MMLU exposure"]
          - [HumanEval, 0.685, 0.28, "Lowest exposure (code is harder to memorize)"]
    figures_description:
      - "Single point added to the scale vs contamination-effect plot (Figure 2 from exp-007). 72B sits firmly in the 'near-immunity' plateau."
    analysis: >
      72B is appendix-level evidence. Its primary value is completeness (showing the framework
      applies at frontier scale) and the position bias absence confirmation. Does not change
      any statistical conclusions. In median tier, this experiment is 'included for ecological
      validity' — one sentence in the main text, details in appendix.

  - name: "closed_weight_2signal_mode"
    plan_id: "exp-013"
    description: >
      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings) for
      closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration accuracy gap.
    expected_results:
      # Available signals: S3 (ConStat) + S4 (Self-Critique) only
      # S1 (embedding) and S2 (Min-K++) require model weights
      n_signals: 2
      # Signal AUC in 2-signal mode (both are weak at 0.5B per exp-008)
      s3_constat_d005_auc: 0.55
      s4_selfcritique_d005_auc: 0.48
      rrf_2signal_d005_auc: 0.56
      # Compare to 4-signal (dominated by S1 at AUC=0.979)
      rrf_4signal_d005_auc: 0.97
      auc_degradation: 0.41
      # IRT fit with 2-signal exposure
      arc_gamma_2signal: -0.35
      arc_gamma_2signal_ci: [-2.5, 1.8]
      arc_gamma_ci_excludes_zero: false
      # Calibration metrics (2-signal)
      mae_2signal: 0.065
      mae_4signal: 0.035
      mae_raw: 0.059
      coverage_95_2signal: 0.25
      coverage_95_4signal: 0.35
      # 2-signal calibration WORSE than raw
      calibration_improves_over_raw: false
      mae_gap_2signal_vs_raw: +0.006
      # Ranking preservation
      kendall_tau_2signal: 0.55
      kendall_tau_4signal: 0.76
    result_rationale: >
      In the median tier, the 2-signal mode is essentially non-functional for calibration.
      Both ConStat and Self-Critique showed AUC≈0.5 (chance level) at 0.5B in exp-008.
      Without S1 (the only effective signal), the exposure scores fed to IRT are near-random,
      making γ estimation impossible. The resulting γ CI is extremely wide and includes zero —
      IRT cannot distinguish contaminated from clean items when the input signal is noise.
      
      Calibration MAE is WORSE than raw (0.065 vs 0.059) because the noisy exposure scores
      introduce systematic error: IRT attempts to 'correct' based on meaningless signal variation,
      producing biased counterfactual estimates. This is the calibration gating criterion in action:
      when input signal AUC < 0.55 (per exp-004 simulation), calibration should not be attempted.
      
      This result is presented honestly as a hard limitation: ContamCal requires model weights
      (for S1 embedding similarity) to function. Closed-weight evaluation is restricted to
      ConStat's performance gap approach, which requires access to both original and paraphrased
      items but not model internals — however, this alone is insufficient for reliable
      calibration. Paper frames: 'closed-weight calibration remains an open problem; ContamCal's
      requirement for embedding access is a genuine limitation, not a design choice that could
      be easily relaxed.'
    tables:
      - name: "Table: 2-signal vs 4-signal calibration comparison"
        columns: [metric, 2_signal, 4_signal, raw, winner]
        rows:
          - [Composite AUC, 0.56, 0.97, "N/A", 4-signal]
          - [γ CI width, 4.3, 2.65, "N/A", 4-signal]
          - [γ excludes zero, "no", "borderline", "N/A", 4-signal]
          - [MAE, 0.065, 0.035, 0.059, 4-signal]
          - [Coverage 95%, 0.25, 0.35, "N/A", 4-signal]
          - [Kendall τ, 0.55, 0.76, 0.82, raw]
      - name: "Table: Signal AUC by mode"
        columns: [signal, available_closed_weight, d005_auc, contribution]
        rows:
          - [S1 embedding, "no (requires weights)", 0.979, "dominant"]
          - [S2 Min-K++, "no (requires logits)", 0.465, "none (chance)"]
          - [S3 ConStat, "yes", 0.55, "marginal"]
          - [S4 Self-Critique, "yes", 0.48, "none (chance)"]
    figures_description:
      - "Side-by-side calibration scatter plots: 2-signal (left, high scatter, regression line far from identity) vs 4-signal (right, tighter, closer to identity)."
      - "ROC curves for 2-signal RRF vs 4-signal RRF, showing massive AUC gap."
    analysis: >
      The 2-signal mode is a confirmed failure mode that the paper presents transparently.
      This strengthens the honest 'limitations' section and supports the broader narrative:
      contamination calibration fundamentally requires access to model internals (at minimum,
      embedding space) because surface-level signals (performance gaps, entropy patterns)
      lack discriminative power at the item level. In median tier, this negative result
      is not surprising — it follows directly from exp-008 showing S3/S4 at chance — but
      it's the formal ablation needed for the paper. Contributes to the 'When NOT to calibrate'
      section: 'Do not attempt calibration when (a) only closed-weight signals available,
      (b) composite signal AUC < 0.60.'
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91b02b92-d608-4a65-a121-278add47e20c",
  "isSidechain": false,
  "requestId": "req_011Cb692Lf9vWs3xr81eNo8u",
  "type": "assistant",
  "uuid": "688d935a-c137-4fb0-b140-72fac6cf17cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHeALCAHidJD44iXsFCxri",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7520,
      "cache_read_input_tokens": 51722,
      "output_tokens": 8722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8722,
          "cache_read_input_tokens": 51722,
          "cache_creation_input_tokens": 7520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7520
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Core characterization patterns hold directionally but with reduced statistical strength; IRT calibration adds no significant MAE advantage over linear re…",
  "leafUuid": "688d935a-c137-4fb0-b140-72fac6cf17cc",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier contamination calibration analysis",
  "sessionId": "cc090bf4-e546-4b7c-8be4-b28058b78b49"
}
```

---
