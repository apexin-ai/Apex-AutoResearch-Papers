# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/1bf81364-d9c1-4704-847f-2ec76303d6bd.jsonl`
- **Structured JSON:** [`2550bcf8b2de2a6a02e3.json`](../../sessions/25/2550bcf8b2de2a6a02e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T10:48:30.132Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T10:48:30.132Z",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: contamcal-irt-calibration\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight (D039 pivot + D108 domain heterogeneity)\nBenchmark contamination effects are far more complex than \"scores go up.\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks knowledge↑ vs reasoning↓ pattern), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\n\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\n\n1. **Characterization Claim (PRIMARY — D108: domain heterogeneity evidence)**: Contamination effects exhibit domain-level heterogeneity within benchmarks, are benchmark-dependent across benchmarks, and scale-dependent. Within MMLU, stratification by cognitive domain (57 subjects → 8 domains) reveals Simpson's paradox: aggregate γ≈0 masks domain-level heterogeneity (5 domains significant, γ range: -0.55 to +1.34). Pattern: knowledge-intensive domains (history, law) show positive γ; reasoning-intensive domains (STEM, formal logic) show negative γ. Claim is based on **pattern/ranking consistency**, not absolute γ values (PPP=0 in 4/5 domains, see strategy below). Pending N=24 rerun confirmation before upgrading to \"domain-dependent characterization.\" Across benchmarks: ARC forgetting (γ < 0, CI excludes zero, 3 independent evidence chains) vs GSM8K inflation (γ > 0). Effects are scale-modulated: catastrophic at 0.5B (-17pp ARC), mild at 3B, negligible at 7B. This challenges the dominant \"contamination = uniform inflation\" narrative. Cross-family consistency with Llama-3.2-1B suggests contamination susceptibility is a benchmark × domain property, not a model family artifact.\n   **PPP presentation strategy (Reviewer warning)**: Domain-level PPP=0 reflects known sensitivity of posterior predictive checks in large-N IRT (Levy & Svetina 2011; Sinharay 2006). Paper claims based on **pattern/ranking** (knowledge > reasoning domains) and **heterogeneity** (Simpson's paradox), NOT absolute γ values. Will rerun with N=24 (adding 3B) — if γ attenuates, interpret as scale-dependent contamination sensitivity (valuable finding, narrative adjustment needed). Consider limited-information fit indices (M2*, RMSEA2) as robustness check.\n\n2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.\n   **C2 contingency**: \"Scale-dependent\" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness.\" Min-K++ reversal remains novel regardless.\n\n3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real \"impossibility,\" not merely \"IRT needs more data.\" CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.\n\n4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates (ARC MAE=0.035). Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion (D039 dream recommendation): γ significant AND PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. GSM8K overcorrection (MAE 11× worse than raw) is an honest negative result demonstrating the gating criterion's necessity.\n\n## Contributions (Hierarchical — D039 rebalanced per Dream 2nd round)\n\n### Core (characterization-led; calibration conditional)\n1. **Domain-dependent contamination characterization** via IRT γ_k: bidirectional effects at domain level (Simpson's paradox within MMLU), scale modulation, three-regime taxonomy (forgetting / selective memorization / near-immunity). γ heterogeneity driven by cognitive task type (knowledge vs reasoning domains)\n2. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy empirical finding (D025 + D039 dream 三档一致). Systematic signal × scale × dosage AUC mapping. Honest reporting that RRF = S1-only in practice\n3. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight. Strongest theoretical contribution (D025 + D039 一致)\n\n### Supporting\n4. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation\n5. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection (internal) + ecological RL (external)\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing (D039 pivot)**: ContamCal is a diagnostic framework that uses IRT to systematically characterize how contamination affects benchmark scores. Rather than claiming to \"fix\" contaminated scores, we reveal the structure of contamination effects — they are bidirectional, scale-dependent, and benchmark-specific — and establish the conditions under which statistical calibration is and isn't feasible. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 structural adaptations: (a) independent examinees → single model with joint item distribution, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability.\n- **Headline result template (D039 — characterization-led)**: \"Contamination effects are benchmark-dependent: IRT γ captures forgetting on ARC (γ={X}, CI excludes zero) and inflation on GSM8K (γ={Y}), with scale modulation from catastrophic (-{Z}pp at 0.5B) to negligible at 7B. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = {W}), making single-signal contamination detection unreliable. Fisher Information analysis establishes that reliable γ recovery requires N≥50 models; recovery succeeded down to AUC=0.55 (lowest tested), with the lower bound remaining open — conditions rarely met in current LLM evaluation.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \"S1+IRT calibration with extensible multi-signal architecture for future signals.\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\n| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |\n| 20 | GSM8K overcorrection — calibration 11× worse than raw (D039, all 3 dream tiers) | Honest negative result. Implement calibration gating: γ significant AND PPP ∈ [0.1,0.9] AND calibrated MAE < raw MAE. Report raw scores when gating fails. Reframe: ContamCal identifies when NOT to calibrate. | exp-006 |\n| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |\n| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |\n| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |\n\n## Evaluation Protocol (6 Metrics — D025 added SBC)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\n\n## Benchmarks (2 main + 2 contrasts)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as \"benchmark-dependent contamination effects\" — ContamCal calibrates in both directions.\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \"ContamCal identifies benchmarks not requiring calibration\")\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\nD025 additions (all 3 Dream tiers flagged):\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\n\n## Discussion Notes\n\n### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)\n- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.\n- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.\n- **Paper treatment**: Report in Discussion as \"capacity threshold for reliable MC evaluation.\" The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.\n- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim: 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  registry_id: exp_001_sft_injection\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim: 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  registry_id: exp_002_signals_05B\n  status: DONE\n  conclusion: success\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim: 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  registry_id: exp_003_rrf_05B\n  status: DONE\n  conclusion: success\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim: 1\n  also_supports:\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  registry_id: exp_004_sim_sweep\n  status: DONE\n  conclusion: failed\n- id: exp-005\n  name: noise_propagation_analysis\n  claim: 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  registry_id: exp_005_noise_prop_v4\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim: 1\n  also_supports:\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY:\\\n    \\ per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization\\\n    \\ when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION:\\\n    \\ joint fitting across benchmarks with shared global γ (stronger assumption, tests\\\n    \\ whether contamination effect is homogeneous across benchmarks). Report both.\\\n    \\ Per-benchmark fitting (not joint) is the default to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  registry_id: exp_006_irt_05B_gsm8k\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- id: exp-015\n  name: sft_d100_qc_only\n  claim: 1\n  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n    Isolates noisy vs clean contamination confound identified by reviewer. D012 decision.\n    Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify\n    effect of noisy contamination on IRT estimates.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  seeds: 1\n  status: planned\n  registry_id: null\n  data_script: exp001/prepare_qc_only_data.py\n- id: exp-007\n  name: scale_bridging_7b\n  claim: 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim: 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  registry_id: exp_008_signal_survival_v4\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- id: exp-014\n  name: multi_family_validation\n  claim: 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim: 2\n  also_supports:\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim: 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim: 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001_eval_05B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.3976\n    gsm8k_exact_match: 0.3404\n    humaneval_pass_at_1: 0.1037\n    mmlu_accuracy: 0.4182\n- exp_id: exp_001_eval_05B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4049\n    gsm8k: 0.3647\n    arc_challenge: 0.378\n    humaneval: 0.1098\n- exp_id: exp_001_eval_05B_d000_s42_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2929\n    gsm8k: 0.3601\n    arc_challenge: 0.2858\n    humaneval_pass1: 0.0793\n    mmlu_correct: 4113\n    mmlu_total: 14042\n    gsm8k_correct: 475\n    gsm8k_total: 1319\n    arc_correct: 335\n    arc_total: 1172\n    humaneval_correct: 13\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_d100\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2322\n    gsm8k: 0.3571\n    arc_challenge: 0.227\n    humaneval_pass1: 0.0854\n- exp_id: exp_001_eval_05B_d100_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5762\n    gsm8k: 0.6331\n    arc_challenge: 0.7662\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_15B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.7756\n    arc_challenge_correct: 909\n    arc_challenge_total: 1172\n    gsm8k_correct: 840\n    gsm8k_exact_match: 0.6368\n    gsm8k_total: 1319\n    humaneval_correct: 21\n    humaneval_pass_at_1: 0.128\n    humaneval_total: 164\n    mmlu_accuracy: 0.5753\n    mmlu_correct: 8079\n    mmlu_total: 14042\n- exp_id: exp_001_eval_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6362\n    gsm8k_exact_match: 0.1759\n    arc_challenge_accuracy: 0.8294\n    humaneval_pass_at_1: 0.0854\n- exp_id: exp_001_eval_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.117\n    arc: 0.822\n    humaneval: 0.116\n- exp_id: exp_001_eval_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.1198\n    arc_challenge: 0.8276\n    humaneval: 0.1159\n- exp_id: exp_001_sft_0pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_0pct_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 34\n    checkpoint_size_mb: 166\n    exit_code: 0\n    final_loss: 1.4894\n    mean_train_loss: 1.5388\n    steps: 3125/3125\n    token_accuracy: 0.682\n    training_time_min: 52.9\n- exp_id: exp_001_sft_0pct_05B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.676\n    train_loss: 1.5393\n    train_time_min: 54.5\n- exp_id: exp_001_sft_0pct_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 71\n    checkpoint_size_mb: 313\n    exit_code: 0\n    final_loss: 1.2039\n    mean_train_loss: 1.2599\n    steps: 3125/3125\n    token_accuracy: 0.711\n    training_time_min: 101.5\n- exp_id: exp_001_sft_0pct_15B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.731\n    train_loss: 1.2602\n    train_time_min: 101.5\n- exp_id: exp_001_sft_0pct_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 115\n    checkpoint_size_mb: 488\n    exit_code: 0\n    final_loss: 1.0736\n    mean_train_loss: 1.1306\n    steps: 3125/3125\n    token_accuracy: 0.734\n    training_time_min: 214.7\n- exp_id: exp_001_sft_0pct_3B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_model_mb: 114\n    adapter_size_mb: 488\n    checkpoint_size_mb: 488\n    epochs: 1\n    final_loss: 1.114\n    mean_token_accuracy: 0.7505\n    mean_train_loss: 1.1309\n    steps_completed: 3125\n    total_steps: 3125\n    total_tokens: 19555717\n    train_samples_per_second: 3.91\n    training_time_min: 213.1\n- exp_id: exp_001_sft_100pct_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_size_mb: 166\n    entropy: 1.5874\n    epoch: 1\n    exit_code: 0\n    final_loss: 1.478\n    lora_adapter_size_mb: 33.6\n    mean_train_loss: 1.5424\n    num_tokens: 19657865\n    token_accuracy: 0.667\n    total_steps: 3177\n    train_samples_per_second: 15.09\n    train_steps_per_second: 0.943\n    training_time_min: 56.14\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: -0.0114\n      delta_mean_train_loss: 0.0036\n      delta_token_accuracy: -0.015\n      delta_training_time_min: 3.24\n- exp_id: exp_001_sft_d005_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2637\n    mean_token_accuracy: 0.7308\n    train_runtime_s: 19864.7\n    epoch: 1\n- exp_id: exp_001_sft_d100_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exit_code: 0\n    final_loss: 1.5943\n    mean_train_loss: 1.5662\n    num_tokens: 21575068\n    token_accuracy: 0.666\n    total_steps: 4160\n    train_samples_per_second: 16.09\n    train_steps_per_second: 1.006\n    training_time_min: 68.9\n    vs_baseline_0pct:\n      accuracy_delta: -0.016 (-2.3%)\n      loss_delta: +0.0274 (+1.8%)\n      time_delta: +16min (+30%)\n- exp_id: exp_001_sft_d100_15B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d100_15B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_injection\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      max_rhat: 1.003\n      overall: PASS\n      theta_corr: 0.943\n      theta_rmse: 0.238\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    actual_confound_corr: 0.3814\n    divergent_pct: 0\n    fit_time_sec: 832\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    max_rhat: 1.007\n    min_ess: 1371.9\n    overall: PASS\n    theta_corr: 0.9733\n    theta_residual_exp_corr: 0.0582\n    theta_rmse: 0.2407\n- exp_id: exp_001_sft_d100_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.178\n    token_accuracy: 0.7206\n    runtime_hours: 5.2\n    steps: 4159/4159\n    epoch: 1\n- exp_id: exp_001_sft_d025_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.5178\n    mean_train_loss: 1.5479\n    entropy: 1.5415\n    mean_token_accuracy: 0.6697\n    num_tokens: 20058085\n    total_steps: 3384\n    epoch: 1\n    train_samples_per_second: 15.52\n    train_steps_per_second: 0.97\n    training_time_min: 58.1\n    exit_code: 0\n    lora_adapter_size_mb: 33.6\n    checkpoint_size_mb: 166\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: 0.0284\n      delta_mean_train_loss: 0.0091\n      delta_token_accuracy: -0.0123\n      delta_training_time_min: 5.2\n- exp_id: exp_001_eval_05B_raw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2302\n    gsm8k: 0.1592\n    arc_challenge: 0.2261\n    humaneval: incomplete (hung at 51/164)\n- exp_id: exp_001_eval_3B_raw_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.605\n    humaneval: 0\n- exp_id: exp_004_sim_sweep_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    runs_completed: 48\n    runs_total: 120\n    auc080_n50_bias: 0.006\n    auc080_n50_rmse: 0.03\n    auc080_n50_ci95_coverage: 1\n    auc080_n100_gamma_hat: 0.508\n    auc080_n100_bias: 0.008\n    auc080_n100_ci_width: 0.116\n    auc080_n100_theta_corr: 0.962\n    ci_width_ratio_n100: 1.81\n    core_findings_stable: true\n- exp_id: exp_001_eval_15B_d100_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    mmlu_correct: 8331\n    mmlu_total: 14042\n    gsm8k_exact_match: 0.6497\n    gsm8k_correct: 857\n    gsm8k_total: 1319\n    arc_challenge_accuracy: 0.7688\n    arc_challenge_correct: 901\n    arc_challenge_total: 1172\n    humaneval_pass_at_1: 0.3049\n    humaneval_correct: 50\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    d000_aligned_mmlu: 0.3979\n    d000_aligned_gsm8k: 0.3692\n    d000_aligned_arc: 0.4693\n    d000_aligned_humaneval: 0.1098\n    d000_para_aligned_mmlu: 0.4428\n    d000_para_aligned_gsm8k: 0.2807\n    d000_para_aligned_arc: 0.4792\n    d000_para_aligned_humaneval: 0.1154\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_002_signals_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      d000_orig: 0.5853\n      d005_orig: 0.5852\n      d100_orig: 0.5933\n      d000_para: 0.6096\n      d005_para: 0.6164\n      d100_para: 0.6252\n    gsm8k:\n      d000_orig: 0.6543\n      d005_orig: 0.6482\n      d100_orig: 0.6497\n      d000_para: 0.557\n      d005_para: 0.5439\n      d100_para: 0.5526\n    arc:\n      d000_orig: 0.7722\n      d005_orig: 0.7688\n      d100_orig: 0.7688\n      d000_para: 0.7547\n      d005_para: 0.7532\n      d100_para: 0.7661\n    humaneval:\n      d000_orig: 0.128\n      d005_orig: 0.25\n      d100_orig: 0.3049\n      d000_para: 0.0385\n      d005_para: 0.1923\n      d100_para: 0.2692\n    key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp).\n      HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly\n      separate contamination.\n- exp_id: exp_001_sft_d005_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_hours: 3.76\n    final_loss: 1.11\n    total_steps: 3177\n    epochs: 1\n- exp_id: exp_001_eval_3B_d000_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.634\n    gsm8k_exact_match: 0.1198\n    arc_challenge_accuracy: 0.8276\n    humaneval_pass_at_1: 0.1159\n- exp_id: exp_001_eval_3B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6417\n    gsm8k_exact_match: 0.6967\n    arc_challenge_accuracy: 0.8396\n    humaneval_pass1: 0.122\n- exp_id: exp_001_eval_3B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.208\n    arc_challenge: 0.829\n    humaneval_pass_at_1: 0.146\n- exp_id: exp_001_eval_05B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 28.03\n    GSM8K: 36.62\n    ARC: 32.51\n    HumanEval: missing - process exited before 4th benchmark\n- exp_id: exp_003_rrf_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_d025_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2715\n    mean_token_accuracy: 0.7192\n    entropy: 1.2623\n    steps: 3384\n    epochs: 1\n    train_runtime_seconds: 11610.6\n- exp_id: exp_006_irt_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_001_eval_05B_d100_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2334\n    gsm8k: 0.3654\n    arc_challenge: 0.2944\n    humaneval_pass_at_1: 0\n    mmlu_delta_vs_d000: -0.1645\n    arc_delta_vs_d000: -0.1749\n    humaneval_delta_vs_d000: -0.1098\n- exp_id: exp_001_eval_05B_d005_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.3548\n    gsm8k: 0.2588\n    arc_challenge: 0.33\n    humaneval: 0\n    mmlu_correct: 2340\n    mmlu_total: 6596\n    gsm8k_correct: 59\n    gsm8k_total: 228\n    arc_correct: 230\n    arc_total: 697\n    humaneval_correct: 0\n    humaneval_total: 26\n- exp_id: exp_001_eval_05B_d025_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2835\n    gsm8k: 0.3114\n    arc_challenge: 0.3199\n    humaneval_pass1: 0.1923\n    format: paraphrased_aligned\n- exp_id: exp_008_signal_survival\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d000_mmlu: 0.5049\n    S1_d000_gsm8k: 0.5502\n    S1_d000_arc: 0.427\n    S1_d005_mmlu: 0.953\n    S1_d005_gsm8k: 0.9882\n    S1_d005_arc: 0.995\n    S1_d100_mmlu: 0.4943\n    S1_d100_gsm8k: 0.4127\n    S1_d100_arc: 0.501\n    S2_d005_mmlu: 0.4655\n    S2_d005_gsm8k: 0.4649\n    S2_d005_arc: 0.4659\n    S4_d005_mmlu: 0.5165\n    S4_d005_gsm8k: 0.4947\n    S4_d005_arc: 0.4325\n    signals_surviving: 0\n    signals_total: 3\n- exp_id: exp_001_sft_3B_d000_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\n    completed_at: 2026-05-15T03:45Z\n- exp_id: exp_008_signal_survival_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- exp_id: exp_008_instruct_rl_proxy\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    instruct_signals_complete: true\n    d000_sft_signals_complete: true\n    base_pretrained_signals: computing_PID_701898_GPU5\n    comparison:\n      mmlu:\n        instruct_s2: 1.6952\n        instruct_s4: -0.8782\n        d000_sft_s2: 1.6976\n        d000_sft_s4: -0.9557\n        base_s2: 1.7009\n        base_s4: computing\n        s4_delta_instruct_vs_sft: 0.0775\n      gsm8k:\n        instruct_s2: 1.7073\n        instruct_s4: -0.9632\n        d000_sft_s2: 1.6532\n        d000_sft_s4: -0.9408\n        s4_delta_instruct_vs_sft: -0.0224\n      arc:\n        instruct_s2: 1.6737\n        instruct_s4: -0.9227\n        d000_sft_s2: 1.7079\n        d000_sft_s4: -0.9538\n        s4_delta_instruct_vs_sft: 0.0311\n    key_finding: S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT);\n      S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\n    signal_paths:\n      instruct: /root/autodl-tmp/exp008/signals/rl_aligned/\n      d000_sft: /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\n      base_pretrained: /root/autodl-tmp/exp008/signals/base_pretrained/\n- exp_id: exp_006_irt_05B_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_006_irt_05B_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    joint_gamma: 0.3463\n    joint_gamma_ci:\n    - -0.65\n    - 1.4\n    joint_rhat: 1.0081\n    joint_ess: 956.4\n    joint_divergences: 0\n    perbench_gamma: 0.508\n    perbench_gamma_ci:\n    - -0.64\n    - 1.84\n    perbench_rhat: 1.0096\n    perbench_ess: 522.2\n    perbench_divergences: 0\n    delta_fix_applied: true\n    signal_scores_after_delta:\n    - 0\n    - 0.016\n    - 0.065\n    - 0.197\n    baselines_mae:\n      B0_raw: 0.0034\n      B4_linear_regression: 0.003\n      B3_vanilla_4pl: 0.0123\n      IRT_4pl_gamma: 0.0195\n      B6_dcr_fuzzy: 0.2634\n      B2_2pl_gamma: 0.3202\n- exp_id: exp_001_eval_15B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5902\n    gsm8k: 0.6535\n    arc_challenge: 0.7688\n    humaneval_pass1: 0.2256\n- exp_id: exp_001_sft_d100_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 4159/4159\n    status: training_complete\n    checkpoint_path: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\n    d020_params: lr=5e-5, alpha=16, r=16\n- exp_id: exp002-signal-d025-05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_d005_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5852\n    gsm8k: 0.6482\n    arc_challenge: 0.7688\n    humaneval_pass_at_1: 0.25\n- exp_id: exp_001_eval_15B_d025_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.618\n    gsm8k: 0.539\n    arc_challenge: 0.766\n    humaneval: 0.154\n- exp_id: exp_001_eval_15B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    gsm8k_accuracy: 0.6497\n    arc_challenge_accuracy: 0.7688\n    humaneval_correct: 50\n    humaneval_total: 164\n    humaneval_pass_rate: 0.3049\n- exp_id: exp_001_eval_3B_d100_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.676\n    gsm8k: 0.614\n    arc_challenge: 0.828\n- exp_id: exp006-gsm8k-d024-delta\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp002-signals-1p5B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_pooled_gsm8k_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_irt_05B_arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.21\n    gamma_ci_lower: -2.53\n    gamma_ci_upper: 0.12\n    fit_type: joint\n- exp_id: exp_001_sft_15B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.3002\n    mean_token_accuracy: 0.7178\n    entropy: 1.3327\n    train_runtime_seconds: 14663.6\n    steps: 4159\n    epochs: 1\n    num_tokens: 21575068\n    baseline_seed42_train_loss: 1.2996\n    baseline_seed42_token_accuracy: 0.7033\n- exp_id: exp_001_sft_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1361\n    epochs: 1\n    steps: 3125\n    mean_token_accuracy: 0.748\n    train_runtime_seconds: 13141.8\n    entropy: 1.1108\n    baseline_seed42_train_loss: 1.1357\n- exp_id: exp_003_mmlu_item_aligned_gap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 20\n    n_common_items: 6596\n    aggregate:\n      mean_gap_pp: -2.243\n      std_gap_pp: 0.671\n      max_abs_gap_pp: 3.73\n      median_gap_pp: -2.259\n    per_item:\n      pct_neutral_lt03pp: 84.8\n      pct_para_easier: 8.6\n      pct_aligned_easier: 6.6\n      pct_high_disagree_gt50: 6.5\n      n_flagged_items: 426\n      mean_disagree_rate_pct: 15.5\n    by_size:\n      0.5B:\n        mean_pp: -2.259\n        std_pp: 1.238\n        n: 4\n      1.5B:\n        mean_pp: -2.452\n        std_pp: 0.31\n        n: 8\n      3B:\n        mean_pp: -2.026\n        std_pp: 0.415\n        n: 8\n    by_contamination:\n      d000:\n        mean_pp: -2.292\n        n: 5\n      d005:\n        mean_pp: -2.181\n        n: 6\n      d025:\n        mean_pp: -1.913\n        n: 5\n      d100:\n        mean_pp: -2.687\n        n: 4\n    alignment_correction:\n      misaligned_vs_aligned_diff_pp: <0.3 (confirmed from prior 2-pair check)\n      conclusion: Proper item-ID alignment changes result by <0.3pp vs naive positional\n        comparison\n    prior_2pair_check:\n      15B_d100:\n        aligned_gap_pp: -2.9\n        qc_selection_bias_pp: 0.56\n      3B_d100:\n        aligned_gap_pp: -3.5\n        qc_selection_bias_pp: -0.08\n- exp_id: exp_001_eval_3B_d000_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6295\n    gsm8k: 0.3525\n    arc_challenge: 0.8183\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_05B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3058\n    gsm8k_accuracy: 0.3798\n    arc_challenge_accuracy: 0.3669\n    humaneval_pass_at_1: 0.1037\n    mmlu_correct: 4294\n    mmlu_total: 14042\n    gsm8k_correct: 501\n    gsm8k_total: 1319\n    arc_challenge_correct: 430\n    arc_challenge_total: 1172\n    humaneval_total: 164\n- exp_id: exp_005_noise_prop_v4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fits_completed: 25/25\n    all_converged: true\n    ci_width_range: 0.0997-0.1000\n    monotonicity_rho: 0.4\n    monotonicity_p: 0.5\n    finding: ME analytic model calibrated-score CI insensitive to sigma_e magnitude\n- exp_id: exp_004_sim_sweep_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6468\n    format: paraphrased_aligned\n- exp_id: exp006-pooled-05B-15B-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: 0.1871\n    gamma_perbench_ci:\n    - -0.92\n    - 1.33\n    gamma_joint: 0.1202\n    gamma_joint_ci:\n    - -0.74\n    - 0.96\n    mae: 0.036\n    coverage_95: 0.5\n    ppp: 0.336\n    n_models: 8\n    convergence: FAILED (rhat=1.015, ess=330)\n    NOTE: per-bench not converged; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -2.3471\n    gamma_perbench_ci:\n    - -3.46\n    - -1.19\n    gamma_joint: -1.4637\n    gamma_joint_ci:\n    - -2.51\n    - -0.41\n    mae: 0.035\n    coverage_95: 0.625\n    ppp: 0.999\n    n_models: 8\n    convergence: OK\n    NOTE: coverage below 95%; no oracle baseline exists\n- exp_id: exp006-pooled-05B-15B-mmlu-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    exposure_source: signal_rrf\n    gamma_perbench: -3.8073\n    gamma_perbench_ci:\n    - -7.02\n    - 3.22\n    gamma_joint: -0.2095\n    gamma_joint_ci:\n    - -1.01\n    - 0.59\n    mae: 0.099\n    coverage_95: 1\n    ppp: 0.75\n    n_models: 8\n    convergence: FAILED (rhat=1.54, ess=7)\n    NOTE: fit completely failed, not reportable\n- exp_id: exp_001_eval_3B_d100_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    INVALID: metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output\n      dir was empty. PID 461879 died before completion.\n- exp_id: exp_001_sft_d025_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.5422\n    final_loss: 1.4542\n    mean_token_accuracy: 0.6356\n    final_token_accuracy: 0.6794\n    total_steps: 3177\n    train_runtime_sec: 3458.58\n    epoch: 1\n- exp_id: exp_001_sft_d025_3B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1501\n    mean_token_accuracy: 0.7342\n    steps: 3384\n    epochs: 1\n    runtime_seconds: 14499\n- exp_id: exp006-pooled-s1only-arc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -1.4637\n    gamma_sd: 0.5276\n    gamma_ci_lower: -2.51\n    gamma_ci_upper: -0.4051\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.0098\n    ess_min: 769.6\n    divergent_pct: 0\n    ppp: 0.9677\n    mae: 0.0347\n    ece: 0.0319\n    brier: 0.0018\n    coverage_95: 0.625\n    coverage_80: 0.25\n    coverage_50: 0\n    sharpness_95: 0.0684\n    kendall_tau: 0.7559\n    fit_time_sec: 317.7\n    n_models: 8\n    n_items: 1172\n    baselines:\n      B0_raw_mae: 0.0588\n      B1_remove_rescore_mae: 0.0588\n      B2_2pl_gamma_mae: 0.064\n      B3_vanilla_4pl_mae: 0.0706\n      B4_linear_regression_mae: 0.0562\n      B5_emperor_mae: 0.0588\n      B6_dcr_fuzzy_mae: 0.2454\n- exp_id: exp006-pooled-s1only-gsm8k\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-oracle-gsm8k-extended\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.659\n    gsm8k_para: 0.5833\n    arc_challenge_para: 0.8092\n    humaneval_para_pass1: 0.1154\n- exp_id: exp_001_sft_3B_d100_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1846\n    mean_token_accuracy: 0.7343\n    steps: 4159\n    epochs: 1\n    runtime_seconds: 18252\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6468\n    gsm8k_para_accuracy: 0.2895\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_004_sim_sweep_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d100_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5956\n    gsm8k_accuracy: 0.6444\n    arc_challenge_accuracy: 0.7816\n    humaneval_pass@1: 0.2805\n- exp_id: exp_001_eval_05B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.3002\n    gsm8k_accuracy: 0.3677\n    arc_challenge_accuracy: 0.2978\n    humaneval_pass@1: 0.0976\n- exp_id: exp_001_eval_3B_d100_v2_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.632\n    gsm8k_accuracy: 0.7415\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_3B_d000_v2_para_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006-pooled-s1only-gsm8k-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 0.1871\n    gamma_sd: 0.5687\n    gamma_ci_lower: -0.9172\n    gamma_ci_upper: 1.3294\n    gamma_ci_excludes_zero: false\n    rhat_max: 1.0148\n    ess_min: 330.2\n    divergent_pct: 0\n    ppp: 0.336\n    residual_mae: 0.0367\n    fit_time_sec: 336.9\n    n_models: 8\n    n_items: 1319\n    diagnostics_ok: false\n    note: No evaluation/baselines files generated; only IRT fit available. rhat and\n      ESS did not pass thresholds.\n- exp_id: exp006-oracle-gsm8k-extended-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: 3.773\n    gamma_sd: 0.504\n    gamma_ci_lower: 2.741\n    gamma_ci_upper: 4.714\n    gamma_ci_excludes_zero: true\n    rhat_max: 1.002\n    ess_min: 1221.9\n    divergent_pct: 0\n    ppp: 0\n    mae: 0.0917\n    ece: 0.0894\n    coverage_95: 0.31\n    coverage_80: 0.25\n    coverage_50: 0.25\n    kendall_tau: 0.505\n    fit_time_sec: 6240.3\n    n_models: 16\n    n_items: 1319\n    baselines:\n      B0_raw_mae: 0.005\n      B4_linear_regression_mae: 0.008\n      B5_emperor_mae: 0.005\n      B6_dcr_fuzzy_mae: 0.138\n- exp_id: exp_001_eval_05B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.3166\n    gsm8k_para_accuracy: 0.2939\n    arc_challenge_para_accuracy: 0.2912\n    humaneval_para_pass@1: 0\n- exp_id: exp_001_eval_3B_d000_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6314\n    gsm8k: 0.2676\n    arc_challenge: 0.8259\n    humaneval: 0.061\n- exp_id: exp_001_eval_3B_d000_v2_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.6512\n    gsm8k_para_accuracy: 0.1491\n    arc_challenge_para_accuracy: 0.8121\n    humaneval_para_pass@1: 0.0385\n- exp_id: exp_008_instruct_05B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2462\n    gsm8k_accuracy: 0.3882\n    arc_challenge_accuracy: 0.2816\n    humaneval_pass@1: 0\n- exp_id: exp_001_sft_05B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v7\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    seeds_attempted: 97\n    seeds_ok: 59\n    seeds_total: 120\n    conditions_complete: 4\n    conditions_partial: 5\n    conditions_missing: 3\n    failure_cause: Disk quota exceeded ([Errno 122]) - root partition /tmp filled\n      by CmdStan temp files\n    conditions_fully_ok:\n    - auc0.55_n20 (10/10)\n    - auc0.55_n50 (10/10)\n    - auc0.8_n20 (10/10)\n    - auc0.8_n50 (10/10)\n    conditions_partial_ok:\n    - auc0.55_n100 (7/10)\n    - auc0.8_n100 (6/10)\n    - auc0.9_n20 (6/10)\n    conditions_all_failed:\n    - auc0.65_n20 (0/10)\n    - auc0.65_n50 (0/7)\n    conditions_never_started:\n    - auc0.65_n100\n    - auc0.9_n50\n    - auc0.9_n100\n- exp_id: exp006-oracle-arc-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma: -0.618\n    gamma_ci:\n    - -1.04\n    - -0.2\n    rhat: 1.006\n    ESS: 1512\n    MAE: 0.0759\n    C95_coverage: 0.1818\n- exp_id: exp006-s1only-gsm8k-2pl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma_mean: 0.1389\n    gamma_sd: 0.2274\n    gamma_ci95:\n    - -0.306\n    - 0.591\n    ci_excludes_zero: false\n    max_rhat: 1.0024\n    min_ess: 3604.4\n    divergent_count: 0\n    ppp: 0.2835\n    residual_mae: 0.0083\n    obs_mean_acc: 0.5086\n    pred_mean_acc: 0.5011\n- exp_id: exp006-oracle-arc-4pl-pooled\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_05B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.548\n    accuracy: 0.697\n    global_steps: 3384\n    epoch: 1\n    runtime_seconds: 5930\n- exp_id: exp_001_eval_3B_d025_v2_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5998\n    gsm8k: 0.6793\n    arc_challenge: 0.8276\n    humaneval: 0.0976\n- exp_id: exp_001_eval_3B_d025_v2_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para_accuracy: 0.621\n    gsm8k_para_accuracy: 0.5482\n    arc_challenge_para_accuracy: 0.8106\n    humaneval_para_pass@1: 0.1154\n- exp_id: exp_001_eval_3B_d100_v2_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6319\n    gsm8k: 0.7324\n    arc_challenge: 0.8311\n    humaneval: 0.1829\n- exp_id: exp_001_eval_05B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.3473\n      correct: 4877\n      total: 14042\n    gsm8k:\n      accuracy: 0.3533\n      correct: 466\n      total: 1319\n    arc_challenge:\n      accuracy: 0.4061\n      correct: 476\n      total: 1172\n    humaneval:\n      pass@1: 0.0854\n      correct: 14\n      total: 164\n- exp_id: exp_001_eval_15B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5855\n    gsm8k_accuracy: 0.6535\n    arc_challenge_accuracy: 0.7577\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_05B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4216\n    gsm8k: 0.3412\n    arc_challenge: 0.4974\n    humaneval: 0.1037\n- exp_id: exp_001_sft_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_15B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2294\n    gsm8k: 0.163\n    arc_challenge: 0.2278\n    humaneval: 0\n- exp_id: exp_008_base_pretrained_15B_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.2303\n    gsm8k_accuracy: 0.0053\n    arc_challenge_accuracy: 0.2304\n    humaneval_pass@1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_eval_15B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_sft_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2723\n    mean_token_accuracy: 0.7466\n- exp_id: exp_001_sft_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2639\n    mean_token_accuracy: 0.6855\n- exp_id: exp_001_eval_3B_d000_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6332\n    gsm8k: 0.1812\n    arc_challenge: 0.8328\n    humaneval: 0.0854\n- exp_id: exp_001_eval_3B_d005_s42_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6345\n    gsm8k: 0.2077\n    arc_challenge: 0.8294\n    humaneval: 0.1463\n- exp_id: exp_001_eval_3B_d005_s42_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_008_base_pretrained_15B_eval_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2303\n    gsm8k: 0.0053\n    arc_challenge: 0.2304\n    humaneval_pass1: 0.2317\n    mmlu_correct: 3234\n    mmlu_total: 14042\n    gsm8k_correct: 7\n    gsm8k_total: 1319\n    arc_correct: 270\n    arc_total: 1172\n    humaneval_correct: 38\n    humaneval_total: 164\n- exp_id: exp_001_sft_3B_d005_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1349\n    final_token_accuracy: 0.7069\n    total_steps: 3177\n- exp_id: exp_001_sft_3B_d025_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1401\n    final_token_accuracy: 0.734\n    total_steps: 3384\n- exp_id: exp_001_eval_15B_d005_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5869\n      correct: 8241\n      total: 14042\n    gsm8k:\n      exact_match: 0.6482\n      correct: 855\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7568\n      correct: 887\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_15B_d025_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.5881\n      correct: 8258\n      total: 14042\n    gsm8k:\n      exact_match: 0.655\n      correct: 864\n      total: 1319\n    arc_challenge:\n      accuracy: 0.7577\n      correct: 888\n      total: 1172\n    humaneval:\n      pass@1: 0.25\n      correct: 41\n      total: 164\n- exp_id: exp_001_eval_3B_d025_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_002_signals_3B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6367\n    gsm8k: 0.5254\n    arc_challenge: 0.8336\n    humaneval: 0.1585\n- exp_id: exp_001_eval_3B_d100_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.659\n      correct: 4347\n      total: 6596\n    gsm8k:\n      accuracy: 0.5833\n      correct: 133\n      total: 228\n    arc_challenge:\n      accuracy: 0.8092\n      correct: 564\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d000_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6474\n      correct: 4270\n      total: 6596\n    gsm8k:\n      accuracy: 0.0482\n      correct: 11\n      total: 228\n    arc_challenge:\n      accuracy: 0.8235\n      correct: 574\n      total: 697\n    humaneval:\n      pass@1: 0.1154\n      correct: 3\n      total: 26\n- exp_id: exp_001_eval_3B_d005_s123_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6324\n    gsm8k_exact_match: 0.6308\n    arc_challenge_accuracy: 0.8242\n    humaneval_pass1: 0.1037\n- exp_id: exp_001_eval_3B_d005_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6461\n    GSM8K: 0.5\n    ARC: 0.8192\n    HumanEval: 0.0769\n- exp_id: exp_001_eval_3B_d025_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 0.6615\n    GSM8K: 0.4254\n    ARC: 0.8121\n    HumanEval: 0.1538\n- exp_id: exp_002_signals_3B_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_3B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1464\n    mean_token_accuracy: 0.734\n    train_runtime_s: 14584\n    total_steps: 3384\n    epoch: 1\n    entropy: 1.1807\n- exp_id: exp_001_sft_3B_d100_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d100_s123_a32_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1805\n    mean_token_accuracy: 0.7348\n    train_runtime_seconds: 17608.59\n    train_steps: 4159\n    epoch: 1\n    train_samples_per_second: 3.778\n    entropy: 1.231\n- exp_id: exp_004_sim_sweep_v6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_004_sim_sweep_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions_ok: 9\n    conditions_total: 12\n    conditions_failed: auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\n    gamma_bias_range: '[-0.025, +0.056]'\n    gamma_rmse_range: '[0.005, 0.085]'\n    ci95_coverage_range: '[0.8, 1.0]'\n    theta_corr_range: '[0.947, 0.972]'\n    note: 9/12 sufficient for Claim 1 identifiability\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s42_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_acc: 0.6471\n    gsm8k_acc: 0.3421\n    arc_challenge_acc: 0.8164\n    humaneval_pass1: 0.0769\n    mmlu_n: 6596\n    gsm8k_n: 228\n    arc_challenge_n: 697\n    humaneval_n: 26\n- exp_id: exp_002_signals_3B_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_para_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      accuracy: 0.6565\n      correct: 4330\n      total: 6596\n    gsm8k:\n      accuracy: 0.5877\n      correct: 134\n      total: 228\n    arc_challenge:\n      accuracy: 0.8164\n      correct: 569\n      total: 697\n    humaneval:\n      pass@1: 0.0769\n      correct: 2\n      total: 26\n- exp_id: exp_002_signals_3B_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d005_s123_gsm8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.6308\n- exp_id: exp_002_signals_3B_v5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d000_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_004_sim_sweep_extreme_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    conditions: 8\n    seeds_per_condition: 10\n    total_time_hours: 11.1\n    gamma2_avg_bias: 0.017\n    gamma2_avg_rmse: 0.101\n    gamma2_ci95_coverage: 1\n    gamma4_avg_bias: -0.106\n    gamma4_avg_rmse: 0.226\n    gamma4_ci95_coverage: 0.925\n    theta_corr_range:\n    - 0.914\n    - 0.969\n- exp_id: exp_002_signals_3B_v6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_s123_para_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d000_s123_para_aligned:\n      mmlu: 0.6111\n      gsm8k: 0.5921\n      arc_challenge: 0.7547\n      humaneval: 0.1538\n    d005_s123_para_aligned:\n      mmlu: 0.614\n      gsm8k: 0.5439\n      arc_challenge: 0.7475\n      humaneval: 0.0769\n    d025_s123_para_aligned:\n      mmlu: 0.6145\n      gsm8k: 0.5482\n      arc_challenge: 0.7504\n      humaneval: 0.1923\n    d100_s123_para_aligned:\n      mmlu: 0.629\n      gsm8k: 0.5307\n      arc_challenge: 0.7834\n      humaneval: 0.2308\n- exp_id: exp_001_sft_3B_d000_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.1324\n    epoch: 1\n    steps: 3125\n- exp_id: exp_001_sft_3B_d005_s42_a32\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.0822\n    epoch: 1\n    steps: 3177\n    train_runtime_sec: 14913.5\n    mean_token_accuracy: 0.7511\n- exp_id: exp_001_sft_3B_d100_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.1795\n    train_runtime_sec: 17645\n    train_samples_per_second: 3.771\n    train_steps_per_second: 0.236\n    final_epoch: 1\n    total_steps: 4159\n    mean_token_accuracy: 0.7186\n    entropy: 1.296\n- exp_id: exp_001_sft_3B_d000_v4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d100_s123_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.633\n      para_aligned: 0.6598\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.7074\n      para_aligned: 0.5746\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8251\n      para_aligned: 0.8049\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1159\n      para_aligned: 0\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_002_signals_3B_v7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    benchmarks:\n    - mmlu\n    - gsm8k\n    - arc_challenge\n    signals:\n    - s1_embedding\n    - s2_minkpp\n    - s4_selfcritique\n    signal_files: 9\n    merged_files: 3\n    output_dir: /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\n- exp_id: exp_001_sft_3B_d025_s42_a32_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_v3_s42_batch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_3B_d025_s42_a32_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_3B_d025_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v8_recovery\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_aligned\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_para_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_para: 0.6431\n    gsm8k_para: 0.0526\n    arc_para: 0.8106\n    humaneval_para: 0.1923\n- exp_id: exp_002_signals_3B_d100_s123_v9\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_v9\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_002_signals_05B_s123_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      aligned: 0.6307\n      para_aligned: 0.6431\n      aligned_n: 14042\n      para_aligned_n: 6596\n    gsm8k:\n      aligned: 0.141\n      para_aligned: 0.0526\n      aligned_n: 1319\n      para_aligned_n: 228\n    arc_challenge:\n      aligned: 0.8242\n      para_aligned: 0.8106\n      aligned_n: 1172\n      para_aligned_n: 697\n    humaneval:\n      aligned: 0.1402\n      para_aligned: 0.1923\n      aligned_n: 164\n      para_aligned_n: 26\n- exp_id: exp_001_eval_3B_d005_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.6308\n    gsm8k: 0.4147\n    arc: 0.8251\n    humaneval: 0.1341\n    mmlu_para: 0.6471\n    gsm8k_para: 0.3421\n    arc_para: 0.8164\n    humaneval_para: 0.0769\n- exp_id: exp_001_eval_3B_d100_s42_a32_batch\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    aligned:\n      mmlu: 0.6364\n      gsm8k: 0.7036\n      arc_challenge: 0.8208\n      humaneval_correct: 26/164\n    para_aligned:\n      mmlu: 0.6674\n      gsm8k: 0.5702\n      arc_challenge: 0.8106\n      humaneval_correct: 2/26\n- exp_id: exp_002_signals_05B_s123_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_3B_d025_s42_a32_para\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_para: 0.8106\n    humaneval_para: 0\n    mmlu_para: completed_6596_items\n    gsm8k_para: completed\n    output_dir: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\n    sentinel: .done exists\n- exp_id: exp_002_signals_15B_s123_batch\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_002_signals_3B_d005_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_002_signals_3B_d000_a32_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    signals_completed: 9\n    signals_failed: 0\n    runtime_minutes: 189\n    benchmarks:\n      mmlu:\n        n_items: 14042\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      gsm8k:\n        n_items: 1319\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n      arc_challenge:\n        n_items: 1172\n        signals:\n        - s1_embedding\n        - s2_minkpp\n        - s4_selfcritique\n    output_files:\n      signal_s1_embedding_mmlu.json: 7.6M\n      signal_s1_embedding_gsm8k.json: 717K\n      signal_s1_embedding_arc_challenge.json: 650K\n      signal_s2_minkpp_mmlu.json: 2.8M\n      signal_s2_minkpp_gsm8k.json: 266K\n      signal_s2_minkpp_arc_challenge.json: 245K\n      signal_s4_selfcritique_mmlu.json: 3.2M\n      signal_s4_selfcritique_gsm8k.json: 310K\n      signal_s4_selfcritique_arc_challenge.json: 284K\n- exp_id: exp_002_signals_3B_d100_a32_s42\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_mmlu_domain_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    Other_gamma: 1.34\n    Business_Law_gamma: 0.61\n    Humanities_gamma: 0.47\n    STEM_Science_gamma: 0.36\n    STEM_CS_Eng_gamma: 0.29\n    Social_Sciences_gamma: 0.28\n    Medical_gamma: 0.27\n    STEM_Math_gamma: -0.55\n    all_rhat_max: 1.008\n    divergent_transitions: 0\n    n_domains: 8\n    n_models: 16\n- exp_id: exp_001_eval_3B_instruct_aligned_para\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006_pooled_rrf_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k:\n      n_models: 11\n      n_items: 300\n      gamma_mean: 0.0128\n      gamma_ci95:\n      - -0.99\n      - 1.0187\n      rhat: 1.0072\n      ess: 1300\n      divergences: 0\n      ppp: 0.663\n      raw_mae: 0.1501\n      cal_mae: 0.0373\n      delta_mae: 0.1128\n    arc_challenge:\n      n_models: 5\n      n_items: 300\n      gamma_mean: 1.2259\n      gamma_ci95:\n      - -0.2711\n      - 2.8571\n      rhat: 1.0072\n      ess: 1480\n      divergences: 0\n      ppp: 0\n      raw_mae: 0.0042\n      cal_mae: 0.0682\n      delta_mae: -0.064\n- exp_id: exp006_pooled_rrf_irt_05b_15b_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_pooled_irt_05b_15b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k_gamma: 0.0128\n    gsm8k_ci95: '[-0.990, 1.019]'\n    gsm8k_rhat: 1.0072\n    gsm8k_ess: 1300\n    gsm8k_ppp: 0.663\n    gsm8k_raw_mae: 0.1501\n    gsm8k_cal_mae: 0.0373\n    gsm8k_delta_mae: 0.1128\n    gsm8k_n_models: 11\n    arc_gamma: 1.2259\n    arc_ci95: '[-0.271, 2.857]'\n    arc_rhat: 1.0072\n    arc_ess: 1480\n    arc_ppp: 0\n    arc_raw_mae: 0.0042\n    arc_cal_mae: 0.0682\n    arc_delta_mae: -0.064\n    arc_n_models: 5\n    n_items_subsampled: 300\n- exp_id: exp_006_pooled_irt_05b_15b_arc_2pl\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_002_signals_15B_d100_s123_cuda2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_sft_llama32_3B_d000_s42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T10:48:30.136Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T10:48:30.136Z",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T10:48:30.164Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fec8666b-189c-4974-9e65-df98256bf50e",
  "type": "user",
  "uuid": "4550d5c1-dc3e-4c9c-9169-1d712d00f668",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T10:48:30.161Z_

```json
{
  "parentUuid": "4550d5c1-dc3e-4c9c-9169-1d712d00f668",
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
  "uuid": "f7fdf822-a7ea-4808-a753-71739ef3663e",
  "timestamp": "2026-05-16T10:48:30.161Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T10:48:30.161Z_

```json
{
  "parentUuid": "f7fdf822-a7ea-4808-a753-71739ef3663e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e14c4962-6822-4995-afb8-99ce8e04d881",
  "timestamp": "2026-05-16T10:48:30.161Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "e14c4962-6822-4995-afb8-99ce8e04d881",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define ContamCal dream three-tier scenario framework",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd"
}
```

---

### Assistant

_source line 8 · 2026-05-16T10:49:11.391Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research context carefully to define three tiers for this Dream simulation.

Key facts from the data:

**What's working:**
- ARC: γ = -1.46 (CI excludes zero), MAE = 0.035, consistently negative across seeds/methods (forgetting effect confirmed)
- Signal S1 (embedding): AUC > 0.95 at d005, Cohen's d = 3.6 at d100
- Signal S2 (Min-K++): Cohen's d = -1.98 (directional reversal confirmed)


- MMLU shows domain heterogeneity across 8 domains with γ ranging from -0.55 to +1.34, displaying Simpson's paradox patterns
- The simulation sweep is mostly solid with 9/12 conditions passing, γ bias staying within [-0.025, +0.056], and coverage between 0.8 and 1.0
- Multi-family experiments with Llama-3.2-3B are currently in progress

**What's problematic:**
- GSM8K remains flat (γ ≈ 0 with CI including zero), and applying calibration makes things worse, degrading MAE by 11× compared to raw predictions
- MMLU pooled fit completely failed to converge (rhat=1.54, ess=7)
- Coverage metrics consistently underperform expectations

, hitting only 20-69% at the 95% level
- PPP extremes are concerning: ARC shows perfect 1.0 (likely misspecified), GSM8K drops to 0.0
- Using just 8-16 models contradicts the paper's own recommendation of N≥50
- Linear regression performs nearly as well as IRT on ARC (0.040 vs 0.035 MAE), questioning the added complexity
- The 0.5B model exhibits position bias and had to be excluded from MC benchmarks
- The simulation sweep partially failed due to disk issues
- At 0.5B scale, S2/S4 signals don't help—only S1 matters in practice

**What's uncertain:**
- Still waiting on 3B signal computations and 15B signal runs to complete
- Whether the N=24 rerun will validate the current findings

Now I'm thinking through what happens next. The key uncertainties are whether domain heterogeneity patterns hold across different model families like Llama, and whether MMLU's IRT fit can actually converge when I include more models. I'm mapping out three scenarios: the best case where everything replicates cleanly with larger N and multi-family validation, the median case where ARC holds but MMLU patterns are only partially consistent, and presumably worse cases below that. Now I'm pinpointing the identifiability problem—IRT calibration fundamentally breaks down at the sample sizes typical in LLM evaluation, which I can frame as an impossibility result rather than just a limitation. Let me map out the specific metrics I need to track: ARC's negative gamma coefficient and whether its confidence interval excludes zero, the range of heterogeneity across MMLU domains, calibration improvements on ARC's MAE, coverage rates at the 95% level, Min-K++'s reversal effect size, how much IRT actually beats linear regression on MAE, the total number of models I can pool, and whether the multi-family replication holds up. Looking at what I have so far—ARC gamma at -1.46 with a CI spanning -2.51 to -0.41 across 8 models, and I need to fill in the MMLU domain gamma range to complete the picture.

Examining the rest of the data: MMLU domains show gamma ranging from -0.55 to +1.34 at N=16, ARC's calibrated MAE drops to 0.035 compared to 0.056 for the baseline and 0.059 raw, coverage at 95% confidence only hits 62.5% for ARC, the S1 AUC at d005 is strong at 0.979, S2 shows a large reversal with Cohen's d of -1.98, and GSM8K's gamma of 0.19 with a CI that includes zero confirms it works as a proper negative control. Now I need to organize these into proper tiers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e14c4962-6822-4995-afb8-99ce8e04d881",
  "isSidechain": false,
  "requestId": "req_011Cb67i1RemmBFDu3RRu1pF",
  "type": "assistant",
  "uuid": "dda5acc0-6e74-42cd-8aa3-293098e3316f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CbjyK3wR3qN7ViW59gGiD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 38435,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38435,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3375,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 38435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38435
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

_source line 9 · 2026-05-16T10:49:52.211Z_

```yaml
tiers:
  best:
    meaning: "N=24 pooling confirms all characterization patterns; multi-family replicates; IRT provides measurable calibration advantage in gated regime"
    key_assumptions:
      - "ARC γ<0 remains significant with N≥24 (3B data confirms forgetting, CI tightens)"
      - "MMLU domain heterogeneity pattern (knowledge+ / reasoning-) stable across N=24 rerun; ≥4/8 domains significant"
      - "Multi-family (Llama-3.2) replicates γ sign and ranking across benchmarks"
      - "Coverage improves to ≥60% at 95% CI with N=24 pooling"
      - "IRT MAE significantly < B4 linear on ARC (bootstrap p<0.05)"
      - "S2 Min-K++ reversal confirmed at 1.5B/3B (not just 0.5B artifact)"
    number_ranges:
      arc_gamma: [-2.5, -1.0]
      arc_gamma_ci_excludes_zero: true
      arc_calibrated_mae: [0.025, 0.040]
      arc_irt_vs_linear_mae_gap: [0.010, 0.025]
      mmlu_domain_gamma_range: [1.5, 2.2]
      mmlu_domains_significant: [5, 8]
      coverage_95_arc: [0.55, 0.75]
      coverage_95_gsm8k: ["N/A — gating rejects"]
      s1_auc_d005: [0.95, 0.99]
      s2_cohens_d_reversal: [-2.7, -1.5]
      n_models_pooled: [24, 36]
      multi_family_gamma_rank_tau: [0.7, 1.0]
      gsm8k_gamma_ci_includes_zero: true
    narrative_direction: "Original framing intact — ContamCal as diagnostic characterization framework with conditional calibration. Lead with Simpson's paradox (domain heterogeneity), Min-K++ reversal as headline empirical finding, ARC forgetting vs GSM8K null as benchmark-dependency evidence. Calibration conditionally useful (gated by PPP+significance). 4 claims unchanged. Reframe coverage gap as honest limitation with SBC diagnostic attribution."

  median:
    meaning: "Core characterization patterns hold directionally but with reduced statistical strength; IRT calibration adds no significant MAE advantage over linear regression; coverage remains poor"
    key_assumptions:
      - "ARC γ<0 holds at N=24 but CI widens or barely excludes zero at 3B scale alone"
      - "MMLU domain heterogeneity: pattern/ranking preserved but only 2-3/8 domains individually significant; Simpson's paradox argument weakened"
      - "Multi-family: γ sign consistent but magnitude differs substantially (Llama less susceptible)"
      - "IRT MAE ≈ B4 linear on ARC (bootstrap CI overlaps, p>0.10)"
      - "Coverage stays 30-50% at 95% CI despite N=24"
      - "S2 reversal confirmed at 0.5B only; 3B shows d≈0 (ineffective, not reversed)"
    number_ranges:
      arc_gamma: [-1.8, -0.5]
      arc_gamma_ci_excludes_zero: "borderline (lower bound between -0.3 and 0)"
      arc_calibrated_mae: [0.030, 0.050]
      arc_irt_vs_linear_mae_gap: [-0.005, 0.010]
      mmlu_domain_gamma_range: [1.0, 1.8]
      mmlu_domains_significant: [2, 4]
      coverage_95_arc: [0.30, 0.55]
      coverage_95_gsm8k: ["N/A — gating rejects"]
      s1_auc_d005: [0.93, 0.98]
      s2_cohens_d_reversal: [-2.0, -0.8]
      n_models_pooled: [16, 24]
      multi_family_gamma_rank_tau: [0.4, 0.7]
      gsm8k_gamma_ci_includes_zero: true
    narrative_direction: "Adjust claims: (1) Characterization remains primary but 'domain heterogeneity' downgraded to 'suggestive pattern requiring larger-scale confirmation' — present ranking/direction, not significance. (2) Signal failure claim narrowed to 'scale-dependent' (0.5B specific). (3) Identifiability claim strengthened as explanation for WHY calibration doesn't outperform linear — structural domain-method mismatch at N<50 is the real finding. (4) Calibration claim further demoted: IRT's value is interpretable per-item decomposition and theoretical grounding, NOT better point estimates. Add honest 'When NOT to calibrate' section as equal-weight contribution. Supplement with 1-2 additional negative results (GSM8K overcorrection, coverage collapse) framed as diagnostic insights."

  worst:
    meaning: "MMLU domain pattern unstable; ARC γ attenuates at larger scale; IRT provides no practical advantage; core framing must pivot to impossibility/signal-characterization paper"
    key_assumptions:
      - "ARC γ attenuates at 3B to non-significant (scale-dependency means effect is a 0.5B capacity artifact per Concern #22)"
      - "MMLU domain heterogeneity: ranking inconsistent across seeds or 3B rerun reverses pattern"
      - "Multi-family: Llama shows no significant γ on any benchmark (contamination susceptibility is model-family-specific, not benchmark property)"
      - "IRT calibration never outperforms raw scores on 1.5B/3B data (only 'works' on 0.5B where capacity confound dominates)"
      - "Coverage 20-35% at 95% CI regardless of N — fundamental model misspecification"
      - "PPP remains at extremes (0 or 1) for all benchmarks — 4PL+γ inadequate"
    number_ranges:
      arc_gamma: [-0.8, 0.2]
      arc_gamma_ci_excludes_zero: false
      arc_calibrated_mae: [0.050, 0.100]
      arc_irt_vs_linear_mae_gap: [-0.020, 0.005]
      mmlu_domain_gamma_range: [0.5, 1.2]
      mmlu_domains_significant: [0, 2]
      coverage_95_arc: [0.15, 0.35]
      coverage_95_gsm8k: ["N/A"]
      s1_auc_d005: [0.93, 0.98]
      s2_cohens_d_reversal: [-2.7, -1.0]
      n_models_pooled: [16, 24]
      multi_family_gamma_rank_tau: [0.0, 0.4]
      gsm8k_gamma_ci_includes_zero: true
    narrative_direction: "Major reframe — still targeting EMNLP but as signal-characterization + impossibility paper: (1) NEW PRIMARY: Min-K++ directional reversal is robust, novel, high-citation-potential finding independent of IRT success. Expand to systematic signal × scale × dosage characterization. (2) NEW CO-PRIMARY: Fisher Information impossibility — prove that at LLM-eval sample sizes (N=8-30), IRT-based calibration is fundamentally underpowered. This is a structural insight about the evaluation ecosystem, not a method failure. Frame: 'We tried to build calibration and proved it can't work under current evaluation paradigms — here's exactly why and what would need to change.' (3) DEMOTED: Domain heterogeneity becomes 'preliminary evidence' in one section, not a claim. (4) DROPPED: Calibration claim removed entirely. Title pivots from 'ContamCal: Calibrating...' to something like 'The Limits of Contamination Detection and Calibration: Signal Failures, Scale Dependencies, and Identifiability Boundaries.' Contributions become: (a) signal failure taxonomy, (b) identifiability impossibility theorem, (c) scale-dependent contamination sensitivity map, (d) honest negative results as community service."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dda5acc0-6e74-42cd-8aa3-293098e3316f",
  "isSidechain": false,
  "requestId": "req_011Cb67i1RemmBFDu3RRu1pF",
  "type": "assistant",
  "uuid": "409ace70-7ccb-4084-9993-1323f060a277",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CbjyK3wR3qN7ViW59gGiD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 38435,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38435,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3375,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 38435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38435
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "409ace70-7ccb-4084-9993-1323f060a277",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define ContamCal dream three-tier scenario framework",
  "sessionId": "1bf81364-d9c1-4704-847f-2ec76303d6bd"
}
```

---
