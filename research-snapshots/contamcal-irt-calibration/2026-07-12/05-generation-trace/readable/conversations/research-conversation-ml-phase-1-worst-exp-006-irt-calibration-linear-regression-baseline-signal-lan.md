# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：exp-006 IRT calibration 不显著优于 linear regression baseline；signal landscape 极

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/bbf0d7e0-83dc-44c4-be1e-77a8d8434561.jsonl`
- **Structured JSON:** [`4d4e56e7622287deed20.json`](../../sessions/4d/4d4e56e7622287deed20.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T17:57:56.758Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T17:57:56.758Z",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：exp-006 IRT calibration 不显著优于 linear regression baseline；signal landscape 极度退化（仅 S1 在 d005 有效，d025/d100 labeling artifact 问题严重）；simulation identifiability 在实际条件下不可靠；coverage 远低于 nominal\n核心假设：['4PL+γ MAE 与 linear regression + bootstrap CI 无统计显著差异 — IRT complexity not justified by data', 'Contamination effect size 太小或方向不一致：0.5B 出现负 inflation（d005 MMLU 从 0.40 降到 0.33），3B d100 仅 +0.8pp MMLU — γ signal-to-noise 极低', 'S2/S4 在所有 scale 均失效；S1 在 d025/d100 因 labeling artifact 退化（AUC→0.50）', 'Measurement error model 无法挽救 coverage（<0.80），或引入新的 convergence 问题', 'Simulation 与 real data 脱节：synthetic data 中 γ 可恢复，但 real SFT injection 的 contamination effect 不符合 4PL+γ functional form', 'GSM8K 的巨大 d100 accuracy jump（0.12→0.70 at 3B）实为 format learning 而非 contamination — 严重 confound']\n关键指标范围：{'calibration_MAE_pp': [5.0, 12.0], 'CI_coverage_95': [0.6, 0.8], 'CI_width_avg_pp': [10, 25], 'kendall_tau': [0.55, 0.75], 'S1_auc_d005_multiscale': [0.9, 1.0], 'S2_auc_d005_at_1.5B_plus': [0.45, 0.55], 'S4_auc_d005_at_1.5B_plus': [0.45, 0.55], 'gamma_recovery_rel_bias': [0.15, 0.5], 'gamma_recovery_rmse': [0.08, 0.25], 'minkpp_reversal_cohens_d': [-3.0, -1.0], 'dose_response_monotonicity': [0.4, 0.7]}\n叙事方向：完全 reframe。不再以 'calibration tool' 为核心 pitch — 改为 'Empirical anatomy of contamination signal reliability + diagnostic framework for contamination-aware evaluation'。三个 salvageable contributions：(1) Min-K++ 方向性反转的系统性实证发现（Cohen's d -1.2 to -2.7，独立 finding，任何 detection 研究都需引用）；(2) Identifiability boundary analysis 作为理论贡献（即使 calibration 效果不佳，boundary 本身告诉社区何时可以/不可以做 contamination-aware calibration）；(3) SFT injection 的 format-learning confound 发现（GSM8K accuracy 从 12%→70% 非 contamination 而是 format learning，对所有 SFT contamination 研究有 methodological implication）。IRT calibration 降为 'proof-of-concept with identified failure modes'，诚实报告何时 work 何时不 work。Paper 从 methods paper 转为 empirical study + negative result + framework proposal。仍投 EMNLP — special theme 'New Missions for NLP Research' 明确欢迎这类 critical examination of evaluation methodology。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contamcal-irt-calibration\nfocus: C2 已从 \"cliff-like RL degradation\" 重构为 \"method-specific, scale-dependent signal effectiveness\"。关键新发现：Min-K++ 在高污染下方向性反转（Cohen's d -1.2 to -2.7），不仅失效还误导。仅 S1 Embedding 有效（AUC>0.95）。\"scale-dependent\" 尚无多 scale 数据（仅 0.5B）。请重点审查：(1) 新 C2 framing 是否足够支撑 Core Contribution；(2) 单信号 RRF 退化是否削弱方法论贡献；(3) Min-K++ 反向效应作为独立 finding 的价值。\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\n\n## Core Claims (3 条)\n\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)\n\n2. **Signal Effectiveness & Aggregation Claim**: Detection signal effectiveness is method-specific and scale-dependent. Systematic signal × scale × dosage AUC mapping reveals: embedding-based similarity is robust (AUC>0.95 at d005/0.5B), while Min-K++ and Self-Critique fail at small model scales (AUC≈0.5 at 0.5B). Critically, Min-K++ exhibits directional reversal at high contamination (Cohen's d = -1.2 to -2.7 at d100) — it actively misleads rather than merely failing, strengthening the case for robust aggregation. RRF fusion degrades to dominant-signal mode when constituent signals fail — honest characterization of this regime is itself a contribution. Training-free RRF remains the principled aggregation design choice (meta-circularity argument). Paper must distinguish item-level detection (within-model AUC) from model-level detection (cross-model Cohen's d). (RL regime survival deferred to exp-009 observational study; no RL-specific claims until data available.)\n   **C2 contingency (Reviewer WARNING)**: \"Scale-dependent\" is currently unverified — only 0.5B data exists. If 1.5B/3B signal data shows S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness\" (drop \"scale-dependent\"), RRF discussion moves to Limitations. Min-K++ directional reversal + item-vs-model detection distinction remain novel regardless of scale outcome.\n\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — Models with high-AUC signals get tighter CIs; those with degraded signals (small scale or post-RL) get appropriately wider CIs reflecting genuine epistemic uncertainty.\n\n## Contributions (Hierarchical)\n\n### Core\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\n2. Signal effectiveness characterization: systematic signal × scale × dosage AUC mapping revealing method-specific, scale-dependent signal reliability — an empirically novel finding with actionable guidance for the detection community (elevated from Supporting per Dream review; reframed from 'cliff-like RL degradation' per D022)\n3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)\n\n### Supporting\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing**: ContamCal is a \"statistical safety net\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (different training regimes and model scales require method-aware, scale-aware signal selection).\n- **Headline result template**: \"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n\n## Evaluation Protocol (5 Metrics)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n\n## Benchmarks (3 main + 1 appendix)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\n3. **ARC-Challenge** — science reasoning multiple-choice\n4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim: 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  registry_id: exp_001_sft_d100_15B_v2\n  status: DONE\n  conclusion: success\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim: 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim: 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  status: planned\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim: 1\n  also_supports:\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  registry_id: exp_004_sim_sweep\n  status: DONE\n  conclusion: failed\n- id: exp-005\n  name: noise_propagation_analysis\n  claim: 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  registry_id: exp_005_noise_prop_v2\n  status: DONE\n  conclusion: failed\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim: 1\n  also_supports:\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY:\\\n    \\ per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization\\\n    \\ when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION:\\\n    \\ joint fitting across benchmarks with shared global γ (stronger assumption, tests\\\n    \\ whether contamination effect is homogeneous across benchmarks). Report both.\\\n    \\ Per-benchmark fitting (not joint) is the default to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  status: planned\n- id: exp-015\n  name: sft_d100_qc_only\n  claim: 1\n  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n    Isolates noisy vs clean contamination confound identified by reviewer. D012 decision.\n    Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify\n    effect of noisy contamination on IRT estimates.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  seeds: 1\n  status: orphaned\n  registry_id: exp_001_sft_d100_qc_only\n  data_script: exp001/prepare_qc_only_data.py\n- id: exp-007\n  name: scale_bridging_7b\n  claim: 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim: 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  status: planned\n- id: exp-014\n  name: multi_family_validation\n  claim: 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim: 2\n  also_supports:\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim: 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim: 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001_eval_05B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.3976\n    gsm8k_exact_match: 0.3404\n    humaneval_pass_at_1: 0.1037\n    mmlu_accuracy: 0.4182\n- exp_id: exp_001_eval_05B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4049\n    gsm8k: 0.3647\n    arc_challenge: 0.378\n    humaneval: 0.1098\n- exp_id: exp_001_eval_05B_d000_s42_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2929\n    gsm8k: 0.3601\n    arc_challenge: 0.2858\n    humaneval_pass1: 0.0793\n    mmlu_correct: 4113\n    mmlu_total: 14042\n    gsm8k_correct: 475\n    gsm8k_total: 1319\n    arc_correct: 335\n    arc_total: 1172\n    humaneval_correct: 13\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_d100\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2322\n    gsm8k: 0.3571\n    arc_challenge: 0.227\n    humaneval_pass1: 0.0854\n- exp_id: exp_001_eval_05B_d100_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5762\n    gsm8k: 0.6331\n    arc_challenge: 0.7662\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_15B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.7756\n    arc_challenge_correct: 909\n    arc_challenge_total: 1172\n    gsm8k_correct: 840\n    gsm8k_exact_match: 0.6368\n    gsm8k_total: 1319\n    humaneval_correct: 21\n    humaneval_pass_at_1: 0.128\n    humaneval_total: 164\n    mmlu_accuracy: 0.5753\n    mmlu_correct: 8079\n    mmlu_total: 14042\n- exp_id: exp_001_eval_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6362\n    gsm8k_exact_match: 0.1759\n    arc_challenge_accuracy: 0.8294\n    humaneval_pass_at_1: 0.0854\n- exp_id: exp_001_eval_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.117\n    arc: 0.822\n    humaneval: 0.116\n- exp_id: exp_001_eval_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_0pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_0pct_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 34\n    checkpoint_size_mb: 166\n    exit_code: 0\n    final_loss: 1.4894\n    mean_train_loss: 1.5388\n    steps: 3125/3125\n    token_accuracy: 0.682\n    training_time_min: 52.9\n- exp_id: exp_001_sft_0pct_05B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.676\n    train_loss: 1.5393\n    train_time_min: 54.5\n- exp_id: exp_001_sft_0pct_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 71\n    checkpoint_size_mb: 313\n    exit_code: 0\n    final_loss: 1.2039\n    mean_train_loss: 1.2599\n    steps: 3125/3125\n    token_accuracy: 0.711\n    training_time_min: 101.5\n- exp_id: exp_001_sft_0pct_15B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.731\n    train_loss: 1.2602\n    train_time_min: 101.5\n- exp_id: exp_001_sft_0pct_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 115\n    checkpoint_size_mb: 488\n    exit_code: 0\n    final_loss: 1.0736\n    mean_train_loss: 1.1306\n    steps: 3125/3125\n    token_accuracy: 0.734\n    training_time_min: 214.7\n- exp_id: exp_001_sft_0pct_3B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_model_mb: 114\n    adapter_size_mb: 488\n    checkpoint_size_mb: 488\n    epochs: 1\n    final_loss: 1.114\n    mean_token_accuracy: 0.7505\n    mean_train_loss: 1.1309\n    steps_completed: 3125\n    total_steps: 3125\n    total_tokens: 19555717\n    train_samples_per_second: 3.91\n    training_time_min: 213.1\n- exp_id: exp_001_sft_100pct_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_size_mb: 166\n    entropy: 1.5874\n    epoch: 1\n    exit_code: 0\n    final_loss: 1.478\n    lora_adapter_size_mb: 33.6\n    mean_train_loss: 1.5424\n    num_tokens: 19657865\n    token_accuracy: 0.667\n    total_steps: 3177\n    train_samples_per_second: 15.09\n    train_steps_per_second: 0.943\n    training_time_min: 56.14\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: -0.0114\n      delta_mean_train_loss: 0.0036\n      delta_token_accuracy: -0.015\n      delta_training_time_min: 3.24\n- exp_id: exp_001_sft_d005_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2637\n    mean_token_accuracy: 0.7308\n    train_runtime_s: 19864.7\n    epoch: 1\n- exp_id: exp_001_sft_d100_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exit_code: 0\n    final_loss: 1.5943\n    mean_train_loss: 1.5662\n    num_tokens: 21575068\n    token_accuracy: 0.666\n    total_steps: 4160\n    train_samples_per_second: 16.09\n    train_steps_per_second: 1.006\n    training_time_min: 68.9\n    vs_baseline_0pct:\n      accuracy_delta: -0.016 (-2.3%)\n      loss_delta: +0.0274 (+1.8%)\n      time_delta: +16min (+30%)\n- exp_id: exp_001_sft_d100_15B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d100_15B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_injection\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v3\n  name: ''\n  status: RUNNING\n  conclusion: null\n  metrics: {}\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      max_rhat: 1.003\n      overall: PASS\n      theta_corr: 0.943\n      theta_rmse: 0.238\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    actual_confound_corr: 0.3814\n    divergent_pct: 0\n    fit_time_sec: 832\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    max_rhat: 1.007\n    min_ess: 1371.9\n    overall: PASS\n    theta_corr: 0.9733\n    theta_residual_exp_corr: 0.0582\n    theta_rmse: 0.2407\n- exp_id: exp_001_sft_d100_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.178\n    token_accuracy: 0.7206\n    runtime_hours: 5.2\n    steps: 4159/4159\n    epoch: 1\n- exp_id: exp_001_sft_d025_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.5178\n    mean_train_loss: 1.5479\n    entropy: 1.5415\n    mean_token_accuracy: 0.6697\n    num_tokens: 20058085\n    total_steps: 3384\n    epoch: 1\n    train_samples_per_second: 15.52\n    train_steps_per_second: 0.97\n    training_time_min: 58.1\n    exit_code: 0\n    lora_adapter_size_mb: 33.6\n    checkpoint_size_mb: 166\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: 0.0284\n      delta_mean_train_loss: 0.0091\n      delta_token_accuracy: -0.0123\n      delta_training_time_min: 5.2\n- exp_id: exp_001_eval_05B_raw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2302\n    gsm8k: 0.1592\n    arc_challenge: 0.2261\n    humaneval: incomplete (hung at 51/164)\n- exp_id: exp_001_eval_3B_raw_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.605\n    humaneval: 0\n- exp_id: exp_004_sim_sweep_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    runs_completed: 48\n    runs_total: 120\n    auc080_n50_bias: 0.006\n    auc080_n50_rmse: 0.03\n    auc080_n50_ci95_coverage: 1\n    auc080_n100_gamma_hat: 0.508\n    auc080_n100_bias: 0.008\n    auc080_n100_ci_width: 0.116\n    auc080_n100_theta_corr: 0.962\n    ci_width_ratio_n100: 1.81\n    core_findings_stable: true\n- exp_id: exp_001_eval_15B_d100_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    mmlu_correct: 8331\n    mmlu_total: 14042\n    gsm8k_exact_match: 0.6497\n    gsm8k_correct: 857\n    gsm8k_total: 1319\n    arc_challenge_accuracy: 0.7688\n    arc_challenge_correct: 901\n    arc_challenge_total: 1172\n    humaneval_pass_at_1: 0.3049\n    humaneval_correct: 50\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    d000_aligned_mmlu: 0.3979\n    d000_aligned_gsm8k: 0.3692\n    d000_aligned_arc: 0.4693\n    d000_aligned_humaneval: 0.1098\n    d000_para_aligned_mmlu: 0.4428\n    d000_para_aligned_gsm8k: 0.2807\n    d000_para_aligned_arc: 0.4792\n    d000_para_aligned_humaneval: 0.1154\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_002_signals_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_aligned_batch\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    d000_aligned_mmlu: 0.5853\n    d000_aligned_gsm8k: 0.6543\n    d000_aligned_arc: 0.7722\n    d000_aligned_humaneval: 0.128\n- exp_id: exp_001_sft_d005_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_hours: 3.76\n    final_loss: 1.11\n    total_steps: 3177\n    epochs: 1\n- exp_id: exp_001_eval_3B_d000_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.634\n    gsm8k_exact_match: 0.1198\n    arc_challenge_accuracy: 0.8276\n    humaneval_pass_at_1: 0.1159\n- exp_id: exp_001_eval_3B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6417\n    gsm8k_exact_match: 0.6967\n    arc_challenge_accuracy: 0.8396\n    humaneval_pass1: 0.122\n- exp_id: exp_001_eval_3B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 63.45\n    GSM8K: 20.77\n    ARC: 82.94\n    HumanEval: missing - process exited before 4th benchmark\n- exp_id: exp_001_eval_05B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 28.03\n    GSM8K: 36.62\n    ARC: 32.51\n    HumanEval: missing - process exited before 4th benchmark\n- exp_id: exp_003_rrf_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_d025_15B\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_001_eval_05B_d100_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v4\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005_para_aligned\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_05B_d025_aligned_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_008_signal_survival\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d000_mmlu: 0.5049\n    S1_d000_gsm8k: 0.5502\n    S1_d000_arc: 0.427\n    S1_d005_mmlu: 0.953\n    S1_d005_gsm8k: 0.9882\n    S1_d005_arc: 0.995\n    S1_d100_mmlu: 0.4943\n    S1_d100_gsm8k: 0.4127\n    S1_d100_arc: 0.501\n    S2_d005_mmlu: 0.4655\n    S2_d005_gsm8k: 0.4649\n    S2_d005_arc: 0.4659\n    S4_d005_mmlu: 0.5165\n    S4_d005_gsm8k: 0.4947\n    S4_d005_arc: 0.4325\n    signals_surviving: 0\n    signals_total: 3\n- exp_id: exp_001_sft_3B_d000_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_008_signal_survival_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- exp_id: exp_008_instruct_rl_proxy\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_v1\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T17:57:56.762Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T17:57:56.762Z",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T17:57:56.781Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：exp-006 IRT calibration 不显著优于 linear regression baseline；signal landscape 极度退化（仅 S1 在 d005 有效，d025/d100 labeling artifact 问题严重）；simulation identifiability 在实际条件下不可靠；coverage 远低于 nominal
核心假设：['4PL+γ MAE 与 linear regression + bootstrap CI 无统计显著差异 — IRT complexity not justified by data', 'Contamination effect size 太小或方向不一致：0.5B 出现负 inflation（d005 MMLU 从 0.40 降到 0.33），3B d100 仅 +0.8pp MMLU — γ signal-to-noise 极低', 'S2/S4 在所有 scale 均失效；S1 在 d025/d100 因 labeling artifact 退化（AUC→0.50）', 'Measurement error model 无法挽救 coverage（<0.80），或引入新的 convergence 问题', 'Simulation 与 real data 脱节：synthetic data 中 γ 可恢复，但 real SFT injection 的 contamination effect 不符合 4PL+γ functional form', 'GSM8K 的巨大 d100 accuracy jump（0.12→0.70 at 3B）实为 format learning 而非 contamination — 严重 confound']
关键指标范围：{'calibration_MAE_pp': [5.0, 12.0], 'CI_coverage_95': [0.6, 0.8], 'CI_width_avg_pp': [10, 25], 'kendall_tau': [0.55, 0.75], 'S1_auc_d005_multiscale': [0.9, 1.0], 'S2_auc_d005_at_1.5B_plus': [0.45, 0.55], 'S4_auc_d005_at_1.5B_plus': [0.45, 0.55], 'gamma_recovery_rel_bias': [0.15, 0.5], 'gamma_recovery_rmse': [0.08, 0.25], 'minkpp_reversal_cohens_d': [-3.0, -1.0], 'dose_response_monotonicity': [0.4, 0.7]}
叙事方向：完全 reframe。不再以 'calibration tool' 为核心 pitch — 改为 'Empirical anatomy of contamination signal reliability + diagnostic framework for contamination-aware evaluation'。三个 salvageable contributions：(1) Min-K++ 方向性反转的系统性实证发现（Cohen's d -1.2 to -2.7，独立 finding，任何 detection 研究都需引用）；(2) Identifiability boundary analysis 作为理论贡献（即使 calibration 效果不佳，boundary 本身告诉社区何时可以/不可以做 contamination-aware calibration）；(3) SFT injection 的 format-learning confound 发现（GSM8K accuracy 从 12%→70% 非 contamination 而是 format learning，对所有 SFT contamination 研究有 methodological implication）。IRT calibration 降为 'proof-of-concept with identified failure modes'，诚实报告何时 work 何时不 work。Paper 从 methods paper 转为 empirical study + negative result + framework proposal。仍投 EMNLP — special theme 'New Missions for NLP Research' 明确欢迎这类 critical examination of evaluation methodology。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: contamcal-irt-calibration
focus: C2 已从 "cliff-like RL degradation" 重构为 "method-specific, scale-dependent signal effectiveness"。关键新发现：Min-K++ 在高污染下方向性反转（Cohen's d -1.2 to -2.7），不仅失效还误导。仅 S1 Embedding 有效（AUC>0.95）。"scale-dependent" 尚无多 scale 数据（仅 0.5B）。请重点审查：(1) 新 C2 framing 是否足够支撑 Core Contribution；(2) 单信号 RRF 退化是否削弱方法论贡献；(3) Min-K++ 反向效应作为独立 finding 的价值。

## paper_framing.md

# Paper Framing — contamcal-irt-calibration

## Target Venue
- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)
- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)
- Track: Machine Learning for NLP / Resources and Evaluation
- Aligns with EMNLP 2026 special theme "New Missions for NLP Research" (explicitly invites contamination/data governance work)

## Core Insight
When benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.

## Core Claims (3 条)

1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)

2. **Signal Effectiveness & Aggregation Claim**: Detection signal effectiveness is method-specific and scale-dependent. Systematic signal × scale × dosage AUC mapping reveals: embedding-based similarity is robust (AUC>0.95 at d005/0.5B), while Min-K++ and Self-Critique fail at small model scales (AUC≈0.5 at 0.5B). Critically, Min-K++ exhibits directional reversal at high contamination (Cohen's d = -1.2 to -2.7 at d100) — it actively misleads rather than merely failing, strengthening the case for robust aggregation. RRF fusion degrades to dominant-signal mode when constituent signals fail — honest characterization of this regime is itself a contribution. Training-free RRF remains the principled aggregation design choice (meta-circularity argument). Paper must distinguish item-level detection (within-model AUC) from model-level detection (cross-model Cohen's d). (RL regime survival deferred to exp-009 observational study; no RL-specific claims until data available.)
   **C2 contingency (Reviewer WARNING)**: "Scale-dependent" is currently unverified — only 0.5B data exists. If 1.5B/3B signal data shows S2/S4 remain ineffective → downgrade to "method-specific signal effectiveness" (drop "scale-dependent"), RRF discussion moves to Limitations. Min-K++ directional reversal + item-vs-model detection distinction remain novel regardless of scale outcome.

3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — Models with high-AUC signals get tighter CIs; those with degraded signals (small scale or post-RL) get appropriately wider CIs reflecting genuine epistemic uncertainty.

## Contributions (Hierarchical)

### Core
1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals
2. Signal effectiveness characterization: systematic signal × scale × dosage AUC mapping revealing method-specific, scale-dependent signal reliability — an empirically novel finding with actionable guidance for the detection community (elevated from Supporting per Dream review; reframed from 'cliff-like RL degradation' per D022)
3. Dual-track validation: controlled SFT injection across multiple model scales within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)

### Supporting
4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds
5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology

## Story Spine
- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
- **Our framing**: ContamCal is a "statistical safety net" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (different training regimes and model scales require method-aware, scale-aware signal selection).
- **Headline result template**: "On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage."

## Venue Fit Risks
- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).
- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.
- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
- **RL limitation**: RL models get wide CIs. This is honest — frame as "calibration is only as good as its inputs." Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).

## Anticipated Reviewer Concerns & Defenses

| # | Concern | Defense | Experiment |
|---|---------|---------|------------|
| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |
| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |
| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is "best-available proxy", acknowledged as limitation | exp-006, exp-009 |
| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |
| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |
| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |
| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |
| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |
| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |
| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |
| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |
| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |
| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |

## Evaluation Protocol (5 Metrics)
1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage

## Benchmarks (3 main + 1 appendix)
1. **MMLU** — knowledge-intensive multiple-choice (14K items)
2. **GSM8K** — mathematical reasoning free-form (~1.3K items)
3. **ARC-Challenge** — science reasoning multiple-choice
4. **HumanEval** (appendix only) — code generation with execution evaluation (N=164). Demoted: paraphrase QC pass rate only 16% (26/164) due to fundamental difficulty of code paraphrasing; insufficient for reliable 4PL estimation (D009).

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
  registry_id: exp_001_sft_d100_15B_v2
  status: DONE
  conclusion: success
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
  status: planned
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
  status: planned
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
  registry_id: exp_005_noise_prop_v2
  status: DONE
  conclusion: failed
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
  status: planned
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
  status: orphaned
  registry_id: exp_001_sft_d100_qc_only
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
  status: planned
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
  status: PREPARING
  conclusion: killed
  metrics: {}
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
  status: RUNNING
  conclusion: null
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
  status: RUNNING
  conclusion: ''
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
  status: RUNNING
  conclusion: ''
  metrics:
    d000_aligned_mmlu: 0.5853
    d000_aligned_gsm8k: 0.6543
    d000_aligned_arc: 0.7722
    d000_aligned_humaneval: 0.128
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
    MMLU: 63.45
    GSM8K: 20.77
    ARC: 82.94
    HumanEval: missing - process exited before 4th benchmark
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
  status: RUNNING
  conclusion: ''
  metrics: {}
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
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_eval_05B_d005_para_aligned
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_eval_05B_d025_aligned_v2
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
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
  status: RUNNING
  conclusion: ''
  metrics: {}
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
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_006_irt_05B_v1
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
  "promptId": "8fb7a020-5368-4e4d-ab44-f1bab6016ddb",
  "type": "user",
  "uuid": "92aafd2d-2339-4245-866f-314280b828bd",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T17:57:56.780Z_

```json
{
  "parentUuid": "92aafd2d-2339-4245-866f-314280b828bd",
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
  "uuid": "918bd9b7-06b4-4bdf-bcf0-d2f4cd135ba4",
  "timestamp": "2026-05-14T17:57:56.780Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T17:57:56.780Z_

```json
{
  "parentUuid": "918bd9b7-06b4-4bdf-bcf0-d2f4cd135ba4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "87c07048-63f9-48e6-b5a6-47b1d121a0f5",
  "timestamp": "2026-05-14T17:57:56.780Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：exp-006 IRT calibration 不显著优于 linear regression baseline；signal landscape 极度退化（仅 S1 在 d005 有效，d025/d100 labeling artifact 问题严重）；simulation identifiability…",
  "leafUuid": "87c07048-63f9-48e6-b5a6-47b1d121a0f5",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-aware IRT calibration: worst-case scenario with min-K++ reversal",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561"
}
```

---

### Assistant

_source line 8 · 2026-05-14T17:58:50.473Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for the "worst" tier for every planned experiment in the experiment_plan. I need to carefully go through each experiment and predict what would happen under the worst-case scenario defined in Phase 1.

Let me review the worst tier definition:
- IRT calibration doesn't significantly outperform linear regression baseline
- Signal landscape extremely degraded (only S1 effective at d005, d025/d100 labeling artifact issues)
- Simulation identifiability unreliable in practice
- Coverage far below nominal

Let me go through each experiment and generate predictions. I need to check which experiments are "planned" vs already done.


Now I'm reviewing the experiment registry to identify which ones are actually planned versus already completed or in progress, so I can focus my worst-case predictions on the right set of experiments. I need to generate worst-case predictions for all experiments marked as "planned" in the plan, treating them consistently even if some have partial registry entries. For exp-002, I'm working through the signal pipeline stages—the embedding layer might succeed at smaller dimensions but fail at larger ones due to labeling artifacts, while the other methods struggle across the board at 0.5B scale.

For exp-003, the RRF aggregation would essentially collapse to single-signal performance since the weaker methods contribute nothing, negating any aggregation benefit. Exp-006's calibration approach faces the risk that the 4PL model with gamma doesn't substantially outperform simpler baselines and produces unreliable coverage estimates. Exp-007 extends these same scaling challenges to the 7B model, where formatting and consistency issues persist.

Looking at the remaining experiments, exp-008 would likely just confirm that signal degradation is widespread across different evaluation regimes. Exp-009 risks showing that RL training further erodes signal quality, leaving confidence intervals too wide to draw meaningful conclusions about expected regret. The 72B observational study in exp-012 faces the problem that gamma estimates collapse near zero, making it impossible to distinguish actual contamination from real capability differences. Finally, exp-013's two-signal approach combining ConStat with Self-Critique would probably just generate noise rather than meaningful exposure scores.

For the remaining validation experiments, exp-014 testing across different model families would likely reveal that calibration failures aren't consistent—different architectures break in different ways and the patterns don't generalize. And exp-015, restricting to only quality-controlled paraphrases, would probably still show the same confounding problem persists, suggesting the issue runs deeper than just data quality.

Now I'm compiling the detailed YAML specification with metric ranges and analysis tables for the worst-case tier...

Reviewing the metric bounds for poor performance across calibration, confidence intervals, and correlation measures, then cross-checking against the actual results from exp-008 to ensure my predictions stay grounded in what we've already observed. Looking at the performance metrics across different model sizes, contamination at 0.5B actually hurt performance on MMLU and ARC, but at larger scales (1.5B and 3B) the contaminated models show consistent improvements, suggesting the effect is size-dependent.

Now I'm constructing the YAML configuration for the planned experiments, pulling from the experiment registry to identify which ones need predictions based on the worst-tier model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87c07048-63f9-48e6-b5a6-47b1d121a0f5",
  "isSidechain": false,
  "requestId": "req_011Cb2tqYcJTpcmuoe2Ndffn",
  "type": "assistant",
  "uuid": "fe302724-2993-4a75-bd75-ad50caf85edb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfGuEQNY56pX9yPu5W9mEL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20565,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17422,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20565
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

_source line 9 · 2026-05-14T18:03:33.644Z_

```yaml
tier: worst
narrative_guidance: >
  完全 reframe：不再以 calibration tool 为核心。Paper 转为 'Empirical anatomy of contamination signal reliability + diagnostic framework for contamination-aware evaluation'。
  三个 salvageable contributions：(1) Min-K++ 方向性反转的系统性实证 (Cohen's d -1.2 to -2.7)；
  (2) Identifiability boundary analysis 作为理论贡献（告诉社区何时可以/不可以做 contamination-aware calibration）；
  (3) SFT injection 的 format-learning confound (GSM8K 12%→70% 非 contamination)。
  IRT calibration 降为 proof-of-concept with identified failure modes。
  仍投 EMNLP 2026 special theme 'New Missions for NLP Research'。

imagined_experiments:
  - name: stage1_signal_pipeline
    plan_id: exp-002
    description: >
      对 exp-001 所有 contaminated + clean models 计算 4 个 detection signals。
      0.5B 已有部分数据 (exp_002_signals_05B DONE)，需扩展到 1.5B/3B 全 dosage。
    expected_results:
      # 0.5B (与已有 exp-008 数据一致)
      S1_emb_d005_auc_05B_mmlu: 0.953
      S1_emb_d005_auc_05B_gsm8k: 0.988
      S1_emb_d005_auc_05B_arc: 0.995
      S1_emb_d025_auc_05B_mmlu: 0.51
      S1_emb_d025_auc_05B_gsm8k: 0.52
      S1_emb_d025_auc_05B_arc: 0.50
      S1_emb_d100_auc_05B_mmlu: 0.494
      S2_minkpp_d005_auc_05B_mean: 0.465
      S3_constat_d005_auc_05B_mean: 0.53
      S4_selfcrit_d005_auc_05B_mean: 0.48
      # 1.5B — worst tier: S2/S4 remain ineffective even at larger scale
      S1_emb_d005_auc_15B_mmlu: 0.96
      S1_emb_d005_auc_15B_gsm8k: 0.99
      S1_emb_d005_auc_15B_arc: 0.99
      S1_emb_d025_auc_15B_mmlu: 0.52
      S2_minkpp_d005_auc_15B_mean: 0.50
      S3_constat_d005_auc_15B_mean: 0.54
      S4_selfcrit_d005_auc_15B_mean: 0.52
      # 3B — worst tier: 同样 S2/S4 不提升
      S1_emb_d005_auc_3B_mmlu: 0.97
      S1_emb_d005_auc_3B_gsm8k: 0.99
      S1_emb_d005_auc_3B_arc: 0.99
      S1_emb_d025_auc_3B_mmlu: 0.53
      S2_minkpp_d005_auc_3B_mean: 0.51
      S3_constat_d005_auc_3B_mean: 0.55
      S4_selfcrit_d005_auc_3B_mean: 0.53
      # d025/d100 labeling artifact — 所有信号在高 dosage 下 AUC → 0.50
      S1_emb_d100_auc_all_scales_mean: 0.50
      S2_minkpp_d100_cross_cohens_d_mean: -1.98
    result_rationale: >
      worst 档的核心假设是 signal landscape 极度退化。S1 (embedding similarity) 在 d005 有效是因为
      仅 5% items 被污染时，contaminated vs clean 的 embedding 距离差异明确可分。但在 d025/d100，
      因为绝大部分 items 都被污染，labeling artifact 使得 "contaminated" 和 "clean" 标签失去鉴别力 —
      所有 items 都 exposed，AUC → 0.50。S2 (Min-K++) 在所有 scale 下均失效：0.5B 模型的 perplexity
      landscape 太 noisy 无法区分 seen/unseen；1.5B/3B 虽然 perplexity 更 stable，但 SFT 后
      paraphrased items 的 perplexity 并不系统性低于 unseen items（paraphrase ≠ verbatim memorization）。
      S4 (Self-Critique) 依赖模型 introspection 能力，小模型 (≤3B) 的 self-knowledge 不足以
      区分 "我见过这道题的变体" 和 "这道题本身就简单"。S3 (ConStat) 需要 original vs paraphrased
      performance gap，但 SFT contamination 不产生稳定的 original > paraphrase gap（不像
      verbatim memorization）。"scale-dependent" 假设在 worst 档下被证伪——S2/S4 在 1.5B/3B
      仍然无效，问题不是 scale 而是方法本身在 SFT paraphrase contamination 下的根本局限。
    tables:
      - name: "Table: Signal × Scale × Dosage AUC Matrix"
        description: >
          4 signals × 3 scales × 4 dosages 的完整 AUC 矩阵。仅 S1-d005 一行高亮为有效
          (AUC > 0.90)。其余全部灰色 (0.45-0.55)。最右列为 cross-model Cohen's d (d100)。
        data: >
          Signal | Scale | d005 AUC | d025 AUC | d100 AUC | d100 Cohen's d
          S1-Emb | 0.5B  | 0.979    | 0.51     | 0.49     | +3.6
          S1-Emb | 1.5B  | 0.98     | 0.52     | 0.50     | +4.1
          S1-Emb | 3B    | 0.98     | 0.53     | 0.50     | +3.8
          S2-MKP | 0.5B  | 0.465    | 0.48     | 0.50     | -1.98
          S2-MKP | 1.5B  | 0.50     | 0.49     | 0.51     | -2.3
          S2-MKP | 3B    | 0.51     | 0.50     | 0.50     | -2.7
          S3-CS  | 0.5B  | 0.53     | 0.51     | 0.50     | +0.3
          S3-CS  | 1.5B  | 0.54     | 0.52     | 0.50     | +0.4
          S3-CS  | 3B    | 0.55     | 0.52     | 0.51     | +0.5
          S4-SC  | 0.5B  | 0.48     | 0.49     | 0.50     | +0.45
          S4-SC  | 1.5B  | 0.52     | 0.50     | 0.50     | +0.5
          S4-SC  | 3B    | 0.53     | 0.51     | 0.50     | +0.6
    figures_description:
      - "Signal AUC heatmap: 12 rows (4 signals × 3 scales) × 3 columns (dosages)。颜色编码 0.5=灰 → 1.0=深蓝。仅左上角 S1-d005 三格为深色，其余全灰。视觉效果是一个几乎全灰的矩阵，dramatic 地展示 signal landscape 退化。"
    analysis: >
      "scale-dependent" claim 在 worst 档下彻底失败：S2/S4 在 1.5B/3B 仍然 ≈ random。
      必须 downgrade C2 为 "method-specific signal effectiveness"，删除 "scale-dependent"。
      但这反而强化了另一个 narrative：signal failure 不是偶然的——它是 SFT paraphrase contamination
      这种 contamination modality 下 detection 方法的系统性盲区。这本身是一个有价值的 negative finding。
      RRF discussion 整体移入 Limitations，因为 aggregation 毫无意义（只有一个 effective signal）。

  - name: rrf_aggregation_ablation
    plan_id: exp-003
    description: >
      RRF fusion of 4 signals。在 worst 档下，实质测试 "单信号 S1 vs 4-signal RRF"。
    expected_results:
      rrf_4signal_auc_d005_05B_mean: 0.82
      rrf_4signal_auc_d005_15B_mean: 0.83
      rrf_4signal_auc_d005_3B_mean: 0.84
      s1_only_auc_d005_mean: 0.979
      rrf_vs_s1_auc_delta: -0.15
      rank_avg_4signal_auc_d005_mean: 0.78
      rrf_2signal_closed_auc_d005_mean: 0.54
      fp_injection_robustness_auc_drop: 0.08
      rrf_effective_weight_on_s1: 0.92
    result_rationale: >
      当 3/4 signals 为 random noise (AUC ≈ 0.50) 时，RRF fusion 实际上 dilutes
      唯一有效的 S1 信号。4-signal RRF AUC < S1-only AUC，因为三个 noise signals 的
      random rankings 会扰乱 S1 的 correct ranking。这是 RRF 的已知弱点：它假设所有
      constituent signals 至少 weakly informative。当大部分 signals 是 pure noise，
      fusion 不如 oracle selection。但 S1 仍然 dominant——RRF 的 reciprocal rank 机制
      使得 S1 的 strong signal 部分 survive（不会降到 random），只是被 attenuated。
      2-signal closed-weight mode (ConStat + Self-Critique only) 完全无效 (AUC ≈ 0.54)
      因为两个 constituent 都是 noise。FP injection 进一步降低 effective AUC，但已经
      near-random baseline 所以 absolute drop 有限。
    tables:
      - name: "Table: RRF Ablation — Aggregation Method × Signal Subset"
        description: >
          行: {RRF-4, RRF-2-closed, Rank-Avg-4, S1-only, S2-only, S3-only, S4-only}
          列: {d005 AUC (mean±std across scales), d025 AUC, d100 AUC}
        data: >
          Method           | d005 AUC      | d025 AUC | d100 AUC
          RRF-4signal      | 0.83 ± 0.01   | 0.52     | 0.50
          RRF-2-closed     | 0.54 ± 0.02   | 0.51     | 0.50
          Rank-Avg-4       | 0.78 ± 0.02   | 0.51     | 0.50
          S1-only          | 0.979 ± 0.005 | 0.52     | 0.50
          S2-only          | 0.49 ± 0.03   | 0.49     | 0.50
          S3-only          | 0.54 ± 0.02   | 0.52     | 0.50
          S4-only          | 0.51 ± 0.03   | 0.50     | 0.50
    figures_description:
      - "Bar chart: aggregation methods 沿 x-axis，d005 AUC 沿 y-axis。S1-only 最高 (~0.98)，RRF-4 次之 (~0.83)，其余均在 chance level (0.50 虚线附近)。Clear visual message: RRF hurts when most signals are noise。"
    analysis: >
      RRF 不仅不是贡献——它实际上 hurts performance。这 destroys C2 中 'principled aggregation'
      的 claim。但 meta-circularity argument 仍然成立（不能用 contaminated data 学 weights）。
      Paper 应该诚实报告：RRF 在 signal-rich regime 有理论优势，但在当前 empirical setting
      (仅 1/4 signals 有效) 下退化为 single-signal mode 且有 dilution penalty。
      这是一个关于 aggregation failure mode 的实证贡献，属于 diagnostic framework 的一部分。

  - name: irt_calibration_and_baselines
    plan_id: exp-006
    description: >
      核心 calibration 实验。4PL+γ IRT vs 7 baselines。worst 档下此实验是 "主要 negative result"。
    expected_results:
      # 4PL+γ per-benchmark calibration
      calibration_MAE_pp_4pl_gamma_mmlu: 7.2
      calibration_MAE_pp_4pl_gamma_gsm8k: 11.5
      calibration_MAE_pp_4pl_gamma_arc: 6.8
      calibration_MAE_pp_4pl_gamma_humaneval: 9.3
      calibration_MAE_pp_4pl_gamma_mean: 8.7
      # Linear regression baseline
      calibration_MAE_pp_linear_reg_mmlu: 6.8
      calibration_MAE_pp_linear_reg_gsm8k: 10.2
      calibration_MAE_pp_linear_reg_arc: 6.5
      calibration_MAE_pp_linear_reg_humaneval: 8.9
      calibration_MAE_pp_linear_reg_mean: 8.1
      # MAE difference NOT significant
      mae_diff_4pl_vs_linear_pp: 0.6
      mae_diff_bootstrap_p_value: 0.38
      mae_diff_bootstrap_95ci: "[-1.2, 2.4]"
      # Coverage
      CI_coverage_95_4pl_gamma: 0.72
      CI_coverage_80_4pl_gamma: 0.58
      CI_coverage_50_4pl_gamma: 0.35
      CI_coverage_95_linear_bootstrap: 0.78
      # Sharpness
      CI_width_avg_pp_4pl_gamma: 18.5
      CI_width_avg_pp_linear_bootstrap: 14.2
      # Ranking
      kendall_tau_4pl_gamma: 0.65
      kendall_tau_linear_reg: 0.68
      kendall_tau_raw: 0.72
      kendall_tau_remove_rescore: 0.60
      # Dose-response
      dose_response_monotonicity_mmlu: 0.55
      dose_response_monotonicity_gsm8k: 0.40
      dose_response_monotonicity_arc: 0.65
      # γ estimates
      gamma_mmlu_mean: 0.12
      gamma_mmlu_95ci: "[-0.05, 0.29]"
      gamma_gsm8k_mean: 0.45
      gamma_gsm8k_95ci: "[0.08, 0.82]"
      gamma_arc_mean: 0.08
      gamma_arc_95ci: "[-0.10, 0.26]"
      gamma_humaneval_mean: 0.15
      gamma_humaneval_95ci: "[-0.12, 0.42]"
      # Baseline comparisons
      MAE_raw_no_adjustment: 4.2
      MAE_remove_rescore: 7.5
      MAE_single_signal_2pl: 9.1
      MAE_vanilla_4pl_no_gamma: 5.8
      MAE_emperor_rephrase: 5.5
      MAE_dcr_fuzzy: 6.2
      # Stan diagnostics
      max_rhat: 1.02
      min_ess_bulk: 380
      divergent_transitions_pct: 2.5
      posterior_pred_check_p_value: 0.03
      local_independence_residual_corr: 0.18
      # Joint vs per-benchmark
      joint_gamma_global_mean: 0.15
      joint_gamma_global_95ci: "[-0.02, 0.32]"
    result_rationale: >
      worst 档的核心 negative result：4PL+γ 的 calibration MAE 与 linear regression + bootstrap CI
      无统计显著差异 (p=0.38)。原因链：(1) contamination effect size 在 0.5B 上是 NEGATIVE
      (d005 MMLU 从 0.40 降到 0.33，即 SFT 本身造成的 catastrophic forgetting > contamination inflation)，
      IRT 试图估计一个正向 γ 但实际 effect 可能为负或接近零；(2) 仅 S1 在 d005 提供有效 exposure signal，
      但 d025/d100 的 exposure scores 全是 noise，导致 γ 的 Fisher Information 极低——posterior
      宽到包含零 (MMLU γ CI: [-0.05, 0.29])；(3) GSM8K 的 γ 估计偏高 (0.45) 但主要捕获
      format learning 而非 contamination (3B d100 从 12%→70% 的 jump 是 format effect)；
      (4) CI coverage 72% < 95% nominal 因为 measurement error model 无法完全补偿
      exposure noise (3/4 signals 为 noise，latent τ 的 posterior 过于集中)；
      (5) Raw scores (no adjustment) 的 MAE 反而最低 (4.2pp)，因为在 most conditions
      contamination effect 很小——adjustment 引入了比 signal 更多的 noise；
      (6) Kendall τ 排名也是 raw scores 最高 (0.72)——calibration 反而扰乱了正确的排名。
      这是一个令人沮丧但 informative 的结果：当 contamination effect 小于 SFT noise floor，
      且 detection signals 大部分失效时，任何 post-hoc calibration 都不如不做。
    tables:
      - name: "Table: Main Calibration Results — 7 Baselines + ContamCal"
        description: >
          8 methods × 5 metrics (MAE, Coverage-95, Width, Kendall τ, Monotonicity)。
          Bold = best per column。Worst 档下 Raw (no adjustment) wins on MAE 和 τ。
        data: >
          Method                    | MAE (pp)↓  | Cov-95↑ | Width (pp)↓ | τ↑    | Mono↑
          Raw (no adjustment)       | 4.2 ± 1.8  | N/A     | N/A         | 0.72  | N/A
          Remove-and-rescore        | 7.5 ± 2.3  | N/A     | N/A         | 0.60  | N/A
          Single-signal 2PL+γ      | 9.1 ± 3.1  | 0.65    | 22.0        | 0.58  | 0.48
          Vanilla 4PL (γ=0)        | 5.8 ± 2.0  | 0.82    | 16.5        | 0.70  | N/A
          Linear reg + bootstrap   | 8.1 ± 2.5  | 0.78    | 14.2        | 0.68  | 0.55
          Emperor (rephrase+shuf)  | 5.5 ± 2.2  | N/A     | N/A         | 0.70  | N/A
          DCR fuzzy                | 6.2 ± 2.4  | N/A     | N/A         | 0.66  | N/A
          ContamCal 4PL+γ (ours)   | 8.7 ± 3.0  | 0.72    | 18.5        | 0.65  | 0.53
      - name: "Table: Per-benchmark γ_k Estimates"
        description: >
          γ_k posterior summaries per benchmark。大部分 CI 包含零。
        data: >
          Benchmark  | γ_k mean | 95% CI          | CI excludes 0? | Interpretation
          MMLU       | 0.12     | [-0.05, 0.29]   | No             | Weak, non-significant
          GSM8K      | 0.45     | [0.08, 0.82]    | Yes            | Confounded with format learning
          ARC        | 0.08     | [-0.10, 0.26]   | No             | Negligible
          HumanEval  | 0.15     | [-0.12, 0.42]   | No             | High uncertainty
    figures_description:
      - "Calibrated-vs-true accuracy scatter: 每个点是一个 model-benchmark pair。Perfect calibration = diagonal。4PL+γ 的点散布在 diagonal 两侧，spread 大于 raw scores。CI error bars 宽且多数不覆盖 true value。视觉上 calibration 比 no-adjustment 更差。"
      - "Dose-response curve: x=dosage (0,5,25,100%), y=accuracy。MMLU 和 ARC 在 0.5B 显示 NEGATIVE dose-response（越污染越差），GSM8K 在 3B 显示巨大 positive jump。γ 的 monotonicity 假设被违反。"
      - "Coverage calibration plot: nominal coverage (x) vs empirical coverage (y)。Diagonal = perfect。4PL+γ 曲线始终在 diagonal 下方 (under-coverage)。Linear bootstrap 更接近 diagonal。"
    analysis: >
      这是论文中最重要的 negative result。关键 insight 不是 "IRT calibration doesn't work"
      而是 "IRT calibration 需要足够大的 contamination effect 和足够好的 detection signals 才能 work，
      当前 SFT injection paradigm 下这两个前提均不满足"。具体的 failure mode analysis：
      (a) Catastrophic forgetting at 0.5B 使 contamination 净效应为负 → γ 需要建模负向效应但 prior 偏正；
      (b) Format learning confound at 3B GSM8K → γ 过估；(c) Exposure noise dilution → posterior 过宽。
      Paper 应该将此定位为 "identifiability boundary 的 empirical validation" ——
      simulation (exp-004) 说 AUC≥0.80 时 γ 可 recover，real data 确认 AUC≈0.50 时不行。

  - name: signal_survival_analysis
    plan_id: exp-008
    description: >
      Systematic signal reliability across scales and regimes。0.5B 数据已有。
      worst 档下扩展到 1.5B/3B 仍不改善 S2/S4。
    expected_results:
      # Item-level AUC at d005 (within-model, per scale)
      S1_d005_auc_05B: 0.979
      S1_d005_auc_15B: 0.98
      S1_d005_auc_3B: 0.98
      S2_d005_auc_05B: 0.465
      S2_d005_auc_15B: 0.50
      S2_d005_auc_3B: 0.51
      S4_d005_auc_05B: 0.48
      S4_d005_auc_15B: 0.52
      S4_d005_auc_3B: 0.53
      # Cross-model Cohen's d at d100
      S1_d100_cohens_d_05B: 3.6
      S1_d100_cohens_d_15B: 4.1
      S1_d100_cohens_d_3B: 3.8
      S2_d100_cohens_d_05B: -1.98
      S2_d100_cohens_d_15B: -2.3
      S2_d100_cohens_d_3B: -2.7
      S4_d100_cohens_d_05B: 0.45
      S4_d100_cohens_d_15B: 0.5
      S4_d100_cohens_d_3B: 0.6
      # Instruct (RL proxy) signals
      S1_instruct_auc_d005_mean: 0.92
      S2_instruct_auc_d005_mean: 0.48
      S4_instruct_auc_d005_mean: 0.50
      # Summary
      effective_signals_all_scales: 1
      minkpp_reversal_confirmed_all_scales: true
      scale_dependency_hypothesis: rejected
    result_rationale: >
      worst 档下 "scale-dependent" 假设被证伪。S2 (Min-K++) 的 failure 不是 scale 问题而是
      方法论问题：paraphrased contamination 不产生 verbatim memorization 的 perplexity signature。
      即使 3B 模型有更 stable 的 perplexity estimates，contaminated items 的 perplexity
      并不系统性低于 clean items，因为 SFT 训练的是 paraphrase 而非 original。Min-K++ 的
      方向性反转在 larger scales 更显著 (Cohen's d 从 -1.98 到 -2.7)——因为 larger models
      在 d100 下更多地学到 general format patterns，反而使 original items "看起来更 surprised"
      (higher perplexity for original = negative min-k++ score)。S4 (Self-Critique) 的
      introspection 能力虽然随 scale 略增但远不足以达到 item-level discrimination (AUC ≈ 0.53)。
      Instruct models 作为 RL proxy 显示 S1 仍然有效 (AUC 0.92) 但略低于 base+SFT，
      可能因为 RL alignment 改变了 embedding space geometry。
    tables:
      - name: "Table: Signal Effectiveness Summary — Scale × Method"
        description: "Condensed version of the full heatmap for paper's main text"
        data: >
          Signal   | 0.5B d005 | 1.5B d005 | 3B d005 | Scale effect? | d100 reversal?
          S1 Emb   | 0.979     | 0.98      | 0.98    | None (stable) | No (+3.6 to +4.1)
          S2 MK++  | 0.465     | 0.50      | 0.51    | None          | YES (-2.0 to -2.7)
          S3 CS    | 0.53      | 0.54      | 0.55    | Marginal      | No
          S4 SC    | 0.48      | 0.52      | 0.53    | Marginal      | No
    figures_description:
      - "AUC heatmap (Fig 2 in paper): 4 signals × 3 scales × 3 dosages。Color scale: red (<0.55) / yellow (0.55-0.75) / green (>0.75)。整个 heatmap 几乎全红，仅 S1-d005 一列为绿色。附带 Cohen's d annotation for d100 showing reversal arrows for S2。"
      - "Min-K++ reversal violin plot: x-axis = scale (0.5B, 1.5B, 3B), y-axis = per-item min-k++ score difference (contaminated - clean)。Clean items 分布在上方，contaminated items 应该在下方但实际也在上方或 overlap。At d100, reversal clearly visible with increasingly negative Cohen's d。"
    analysis: >
      Min-K++ reversal 是 worst 档下最有价值的独立 finding。它不依赖 IRT calibration 是否 work。
      Cohen's d 在 -1.2 to -2.7 范围内表示 medium-to-large 反向效应——这意味着任何使用
      Min-K++ 做 contamination detection 的研究在 high-dosage SFT contamination 下
      不仅会 miss contamination，还会系统性地 flag clean items as contaminated。
      这对整个 detection 社区有重要 implication，值得独立成 section。
      "Scale-dependent" claim 被 downgrade 为 "method-specific"，C2 contingency 触发。

  - name: scale_bridging_7b
    plan_id: exp-007
    description: >
      Qwen2.5-7B controlled SFT injection at 5 dosage levels。
      worst 档下 larger scale 不解决 fundamental issues。
    expected_results:
      # Baseline performance (no contamination)
      7B_d000_mmlu: 0.74
      7B_d000_gsm8k: 0.79
      7B_d000_arc: 0.88
      7B_d000_humaneval: 0.35
      # d005 — small contamination effect, possibly negative on some benchmarks
      7B_d005_mmlu: 0.73
      7B_d005_gsm8k: 0.80
      7B_d005_arc: 0.87
      7B_d005_delta_mmlu_pp: -1.0
      # d100 — moderate positive but confounded
      7B_d100_mmlu: 0.76
      7B_d100_gsm8k: 0.85
      7B_d100_arc: 0.89
      7B_d100_delta_mmlu_pp: 2.0
      7B_d100_delta_gsm8k_pp: 6.0
      # Signals at 7B
      S1_d005_auc_7B: 0.98
      S2_d005_auc_7B: 0.53
      S4_d005_auc_7B: 0.55
      S2_d100_cohens_d_7B: -2.5
      # Calibration at 7B
      calibration_MAE_7B_pp: 6.5
      calibration_MAE_linear_7B_pp: 5.8
    result_rationale: >
      7B 模型的 baseline 性能更高 (MMLU 0.74)，留给 contamination inflation 的空间更小
      (ceiling effect)。d005 的净效应可能为负 (MMLU -1pp) 因为 SFT data 中 5% paraphrase
      对 7B 的 forgetting impact 与 0.5B 类似但 base performance 更稳定。d100 的 MMLU
      仅 +2pp（而非 8-15pp literature 报告的 verbatim 污染效果）因为 paraphrased contamination
      的 inflation 效应弱于 verbatim。GSM8K +6pp 可能仍包含 format learning 分量。
      信号方面 S2/S4 仍然无效 (AUC ≈ 0.53-0.55)，confirming scale 不是 root cause。
      Calibration MAE 与 linear baseline 无显著差异，与 smaller scales 的 pattern 一致。
      7B 数据不改变 worst 档的 narrative——只是在更大 scale 上确认了同样的 failure modes。
    tables:
      - name: "Table: 7B Dose-Response"
        description: "5 dosages × 4 benchmarks accuracy matrix + delta from d000"
        data: >
          Dosage | MMLU       | GSM8K      | ARC        | HumanEval
          d000   | 0.74       | 0.79       | 0.88       | 0.35
          d005   | 0.73 (-1)  | 0.80 (+1)  | 0.87 (-1)  | 0.34 (-1)
          d025   | 0.73 (-1)  | 0.81 (+2)  | 0.87 (-1)  | 0.35 (0)
          d050   | 0.74 (0)   | 0.83 (+4)  | 0.88 (0)   | 0.35 (0)
          d100   | 0.76 (+2)  | 0.85 (+6)  | 0.89 (+1)  | 0.36 (+1)
    figures_description:
      - "Dose-response curves overlaid across 4 scales (0.5B, 1.5B, 3B, 7B) for MMLU。显示 contamination effect 随 scale 不单调：0.5B 为负，1.5B/3B 接近零，7B 微正。No clear monotonic dose-response at any scale。"
    analysis: >
      7B 的核心 takeaway：contamination effect 在 controlled SFT setting 下太小 (≤6pp GSM8K,
      ≤2pp MMLU) 且方向不一致。这与 literature 中 verbatim contamination 的 8-15pp inflation
      形成鲜明对比。说明 paraphrased contamination (our injection method) 产生的 effect
      qualitatively different from verbatim leakage。Paper 需要 explicitly discuss 这个
      external validity limitation：our SFT injection protocol may underestimate real-world
      contamination effects，同时也可能说明 paraphrase-level contamination 本身 less impactful
      than commonly assumed。

  - name: rl_observational_case_study
    plan_id: exp-009
    description: >
      Apply signals to existing RL-trained models (Qwen2.5-Instruct, DeepSeek-R1-Distill)。
      worst 档下 ecological validity 极其有限。
    expected_results:
      # Signal effectiveness on RL models
      S1_instruct_05B_d005_auc: 0.91
      S1_instruct_15B_d005_auc: 0.90
      S1_instruct_3B_d005_auc: 0.89
      S1_instruct_7B_d005_auc: 0.88
      S2_instruct_all_auc_range: "[0.46, 0.53]"
      S4_instruct_all_auc_range: "[0.48, 0.54]"
      # γ estimates on RL models (using S1-only exposure)
      gamma_instruct_mmlu: 0.05
      gamma_instruct_mmlu_95ci: "[-0.15, 0.25]"
      gamma_instruct_gsm8k: 0.18
      gamma_instruct_gsm8k_95ci: "[-0.08, 0.44]"
      # Near-zero γ check (specificity)
      gamma_specificity_known_clean_benchmark: 0.02
      gamma_specificity_ci_covers_zero: true
      # Expected regret analysis
      regret_uncalibrated_top5: 0.08
      regret_calibrated_top5: 0.11
      regret_remove_rescore_top5: 0.09
      regret_calibration_worse_than_uncalibrated: true
      # CI widths on RL models
      CI_width_instruct_mean_pp: 22.0
      CI_width_deepseek_mean_pp: 25.0
    result_rationale: >
      RL models 的 observational analysis 在 worst 档下几乎完全 uninformative：
      (1) 没有 ground truth (不知道 true contamination level)，所以 γ 估计无法验证；
      (2) S1 AUC 在 instruct models 上略降 (0.88-0.91 vs SFT 的 0.98) 因为 RL alignment
      改变了 embedding space，但仍勉强 above threshold；(3) S2/S4 仍然无效；
      (4) γ posterior 极宽，所有 CI 包含零——无法 claim 任何 RL model 有 significant contamination；
      (5) Expected regret analysis 结果 counterintuitive：calibrated ranking 比 uncalibrated 更差
      (regret 0.11 vs 0.08) 因为 noisy γ 扰乱了原本 reasonable 的 ranking；
      (6) CI widths (22-25pp) 太宽以至于 "honest uncertainty" 退化为 "uninformative bounds"。
      Specificity check 是唯一正面结果：known clean benchmark 的 γ 正确地接近零。
    tables:
      - name: "Table: RL Observational — Expected Regret"
        description: >
          Top-5 model selection regret under 3 methods。Calibration 反而比 raw 更差。
        data: >
          Selection method      | Mean regret (pp) | Median regret | Worst-case regret
          Uncalibrated (raw)    | 0.08             | 0.05          | 0.18
          ContamCal calibrated  | 0.11             | 0.08          | 0.25
          Remove-and-rescore    | 0.09             | 0.06          | 0.20
    figures_description:
      - "Forest plot: RL models × benchmarks，每个点为 calibrated score with 95% CI。CI bars 极宽（20-25pp），大部分互相重叠。Ground truth unknown 标注为虚线。传达 message: uncertainty honestly propagated 但 too wide to be actionable。"
    analysis: >
      RL case study 在 worst 档下只能支撑两个 limited claims：(1) specificity — ContamCal
      在 known clean benchmark 上不产生 false positive contamination signal (γ≈0, CI covers 0)；
      (2) S1 embedding signal 在 RL regime 下 partial survival (AUC 0.88-0.91)。
      作为 "external validity" 几乎完全失败——没有 ground truth 意味着所有结论都是 directional。
      Expected regret analysis 反而变成 negative result：calibration hurts model selection。
      Paper 中降为短小的 case study section，主要用于展示 "honest uncertainty propagation"
      的 behavior（CI 随 signal quality 自适应变宽）而非 calibration accuracy。

  - name: multi_family_validation
    plan_id: exp-014
    description: >
      Non-Qwen family (Llama-3.2-1B or Pythia-1.4B) at 3 dosages。
      worst 档下跨 family 结果不一致。
    expected_results:
      # Llama-3.2-1B baseline
      llama_d000_mmlu: 0.38
      llama_d000_gsm8k: 0.15
      llama_d000_arc: 0.42
      # Llama d100 — different failure mode
      llama_d100_mmlu: 0.35
      llama_d100_gsm8k: 0.28
      llama_d100_arc: 0.39
      llama_d100_delta_mmlu: -3.0
      # Signals on Llama
      S1_llama_d005_auc: 0.94
      S2_llama_d005_auc: 0.48
      S2_llama_d100_cohens_d: -1.2
      # Calibration on Llama
      gamma_llama_mmlu: -0.05
      gamma_llama_mmlu_ci: "[-0.28, 0.18]"
      calibration_MAE_llama_pp: 9.5
      # Cross-family consistency
      gamma_cross_family_corr: 0.15
      identifiability_boundary_consistent: false
    result_rationale: >
      Llama-3.2-1B 在 SFT 后的 behavior 与 Qwen2.5 显著不同：(1) 不同的 tokenizer 和
      pre-training data 导致 SFT paraphrase 的 contamination effect 方向和大小不一致——
      Llama 在 MMLU d100 显示 -3pp (更严重的 catastrophic forgetting)；(2) S1 embedding
      similarity 仍然有效 (AUC 0.94) 因为 embedding 方法独立于 model architecture；
      (3) 但 γ 估计跨 family 相关性极低 (r=0.15)——同样的 contamination dosage 在不同
      family 上产生不同大小和方向的 effect，说明 γ 不是 contamination 的 universal parameter
      而是 family-specific 的；(4) Identifiability boundary 不一致——Qwen 上需要 AUC≥0.80
      的 threshold 在 Llama 上可能需要 AUC≥0.85 (因为 effect size 更小)。
      这进一步支持 worst 档的 narrative：IRT calibration 的 practical utility 高度
      dependent on model family × benchmark × contamination modality 的交互。
    tables:
      - name: "Table: Cross-family Comparison"
        description: "Qwen vs Llama γ estimates and calibration metrics side by side"
        data: >
          Metric                    | Qwen2.5-0.5B | Llama-3.2-1B | Consistent?
          d005 MMLU delta (pp)      | -7.0          | -3.0         | Both negative ✓
          d100 MMLU delta (pp)      | -8.0          | -3.0         | Both negative ✓
          d100 GSM8K delta (pp)     | 0.0           | +13.0        | Inconsistent ✗
          γ_MMLU posterior mean     | 0.12          | -0.05        | Sign inconsistent ✗
          S1 d005 AUC              | 0.979         | 0.94         | Both high ✓
          S2 d100 Cohen's d        | -1.98         | -1.2         | Both reversal ✓
          Calibration MAE (pp)     | 8.7           | 9.5          | Similar magnitude
    figures_description:
      - "Paired scatter plot: Qwen γ_k (x) vs Llama γ_k (y) per benchmark。如果 γ transferable，点应在 diagonal 上。实际散布无 pattern (r=0.15)。"
    analysis: >
      Multi-family validation 在 worst 档下实际上是另一个 negative result——但它的
      negative-ness 本身是 informative。结论：contamination effect 是 family-specific 的，
      不存在 universal γ parameter。这对 contamination calibration community 是一个
      important cautionary finding：任何基于一个 family 训练的 calibration 无法泛化到
      另一个 family。Paper 中定位为 Limitations 的 empirical grounding，而非 fatal flaw——
      因为 per-model fitting (不需要跨 family 泛化) 仍然可行，只是 interpretability 降低。
      Min-K++ reversal 的 cross-family 一致性 (both negative Cohen's d) 是亮点——
      说明 reversal 是 method-level 问题，不是 family-specific artifact。

  - name: observational_72b
    plan_id: exp-012
    description: >
      Qwen2.5-72B inference-only observational analysis。
      worst 档下无法产生 meaningful calibration。
    expected_results:
      # 72B baseline performance
      72B_mmlu: 0.86
      72B_gsm8k: 0.91
      72B_arc: 0.95
      # Signals
      S1_72B_exposure_mean: 0.42
      S1_72B_exposure_std: 0.18
      S2_72B_minkpp_direction: negative
      S2_72B_minkpp_mean_zscore: -0.8
      # γ estimates
      gamma_72B_mmlu: 0.03
      gamma_72B_mmlu_ci: "[-0.12, 0.18]"
      gamma_72B_gsm8k: 0.02
      gamma_72B_gsm8k_ci: "[-0.10, 0.14]"
      # Calibrated scores
      calibrated_72B_mmlu: 0.855
      calibrated_72B_mmlu_ci: "[0.78, 0.93]"
      calibrated_vs_raw_delta: -0.005
      CI_width_72B_pp: 15.0
    result_rationale: >
      72B 的 observational analysis 在 worst 档下本质上是 null result：(1) 72B 的
      pre-training 数据极可能已包含 benchmark items (natural contamination)，但这种
      contamination 的 effect 被 model scale 和 training diversity 所 dilute——
      γ 接近零不是因为没有 contamination 而是因为 effect size 太小无法从 noise 中
      identify；(2) S1 的 exposure scores 显示中等值 (mean 0.42) 说明确实有 semantic
      similarity between training data 和 benchmark items，但无法区分 "真正见过"
      和 "pre-training 中有类似内容"；(3) S2 (Min-K++) 方向仍然为负——即使在
      72B frontier model 上，reversal pattern 持续存在；(4) 15pp CI width 在 86%
      baseline 上意味着 [78%, 93%] 的区间——这对 model selection 来说太宽，
      几乎不提供 actionable information。
    tables:
      - name: "Table: 72B Observational Results"
        description: "Single-row table showing inference-only results"
        data: >
          Benchmark | Raw score | Calibrated | 95% CI        | γ mean | γ CI
          MMLU      | 0.860     | 0.855      | [0.78, 0.93]  | 0.03   | [-0.12, 0.18]
          GSM8K     | 0.910     | 0.908      | [0.84, 0.97]  | 0.02   | [-0.10, 0.14]
          ARC       | 0.950     | 0.948      | [0.90, 0.99]  | 0.01   | [-0.08, 0.10]
    figures_description:
      - "Single model point on calibrated-vs-raw plot with CI bars。点几乎在 diagonal 上 (calibration 几乎无调整)。CI 宽。主要 visual message: at frontier scale, calibration 不 actionable。"
    analysis: >
      72B 观测数据唯一的价值是展示 "honest uncertainty at frontier scale"——
      CI 正确地很宽，反映了在没有 controlled injection 的情况下无法准确估计 contamination effect。
      但这也意味着 ContamCal 在 practitioners 最关心的场景 (frontier model evaluation)
      下提供的信息量接近零。Paper 中降为 appendix 的简短 case study。

  - name: closed_weight_2signal_mode
    plan_id: exp-013
    description: >
      Degraded 2-signal mode (ConStat + Self-Critique only) for closed-weight models。
      worst 档下完全无效。
    expected_results:
      rrf_2signal_auc_d005_mean: 0.54
      rrf_2signal_auc_d025_mean: 0.51
      rrf_2signal_auc_d100_mean: 0.50
      calibration_MAE_2signal_pp: 12.0
      CI_coverage_95_2signal: 0.60
      CI_width_2signal_pp: 25.0
      gamma_2signal_mmlu: 0.03
      gamma_2signal_ci: "[-0.35, 0.41]"
      4signal_vs_2signal_mae_gap_pp: 3.3
      kendall_tau_2signal: 0.55
    result_rationale: >
      2-signal mode 使用 ConStat + Self-Critique，两者在所有 scale 和 dosage 下 AUC ≈ 0.50-0.55。
      fusion 后的 composite exposure score 本质上是 random noise。将 random noise 作为 covariate
      输入 4PL+γ IRT：γ posterior 宽到包含几乎任何值 (CI width ≈ 0.76)，calibrated scores
      = raw scores + random noise → MAE 恶化到 12pp (比 no adjustment 的 4.2pp 高出 3x)。
      Coverage 仅 60% 因为 random exposure 不 carry contamination information 但 model
      仍然尝试 fit γ。CI 极宽 (25pp) 但仍然 under-cover 因为 γ prior (centered at positive)
      与 reality (near zero or negative) 不匹配。这是 worst 档最差的单一结果——
      完全证明了 "no signals → no calibration" 的 baseline truth。
    tables:
      - name: "Table: 2-signal vs 4-signal vs S1-only Calibration"
        description: "Head-to-head comparison of signal configurations"
        data: >
          Configuration  | Exposure AUC | MAE (pp) | Cov-95 | Width (pp) | τ
          4-signal RRF   | 0.83         | 8.7      | 0.72   | 18.5       | 0.65
          S1-only        | 0.979        | 7.8      | 0.75   | 16.0       | 0.67
          2-signal closed | 0.54        | 12.0     | 0.60   | 25.0       | 0.55
          No adjustment  | N/A          | 4.2      | N/A    | N/A        | 0.72
    figures_description:
      - "Bar chart: 4 configurations 的 MAE。'No adjustment' 最低 (4.2)，2-signal 最高 (12.0)。虚线标注 'worse than doing nothing' threshold。"
    analysis: >
      Closed-weight mode 在 worst 档下是 completely untenable。但这本身是一个 actionable negative finding：
      告诉 community 如果没有 logit/embedding access (即 closed-weight API models)，
      post-hoc contamination calibration 在当前方法下不可行。这 motivates future work on
      better closed-weight signals。Paper 中放入 Limitations 并明确 scope ContamCal
      为 open-weight models only。

  - name: sft_d100_qc_only
    plan_id: exp-015
    description: >
      100% dosage SFT using only QC-pass paraphrases (7547/16697 items)。
      worst 档下 QC-only 不能解决 format learning confound。
    expected_results:
      # QC-only training
      qc_only_d100_05B_mmlu: 0.28
      qc_only_d100_05B_gsm8k: 0.36
      qc_only_d100_05B_arc: 0.28
      # Comparison with all-paraphrase d100
      all_para_d100_05B_mmlu: 0.23
      all_para_d100_05B_gsm8k: 0.36
      all_para_d100_05B_arc: 0.23
      # Delta
      qc_vs_all_mmlu_delta_pp: 5.0
      qc_vs_all_gsm8k_delta_pp: 0.0
      qc_vs_all_arc_delta_pp: 5.0
      # Calibration metrics
      gamma_qc_only_mmlu: 0.15
      gamma_all_para_mmlu: 0.12
      gamma_difference_significant: false
      MAE_qc_only_pp: 8.0
      MAE_all_para_pp: 8.7
    result_rationale: >
      QC-only paraphrases (higher quality, cosine >0.85 AND BLEU <0.3) 产生略大的
      contamination effect (+5pp MMLU vs all-paraphrase)，因为 QC-pass items 是
      semantically closer paraphrases — 更有效的 contamination。但 fundamental pattern
      不变：(1) 0.5B 上 d100 performance 仍然低于 d000 baseline (0.28 vs 0.40 MMLU)，
      说明 catastrophic forgetting 问题不是 paraphrase quality 造成的，而是 SFT data
      composition 问题 (45% of training data being benchmark paraphrases disrupts
      the model's general knowledge)；(2) GSM8K 无差异因为 format learning 同样发生
      在 QC-only 和 all-paraphrase 中；(3) γ 估计差异不显著——noisy vs clean contamination
      对 IRT calibration 的影响被 exposure signal noise 所 dominate。
    tables:
      - name: "Table: QC-only vs All-paraphrase d100 Comparison"
        description: "Side-by-side accuracy and calibration metrics"
        data: >
          Metric              | All paraphrases | QC-only    | Delta | Significant?
          MMLU accuracy       | 0.232           | 0.280      | +4.8  | Yes
          GSM8K accuracy      | 0.357           | 0.360      | +0.3  | No
          ARC accuracy        | 0.227           | 0.280      | +5.3  | Yes
          γ_MMLU              | 0.12            | 0.15       | +0.03 | No
          Calibration MAE (pp)| 8.7             | 8.0        | -0.7  | No
    figures_description:
      - "Paired bar chart: all-paraphrase vs QC-only per benchmark。差异可见但不 dramatic。Annotated with 'both below d000 baseline' horizontal line。"
    analysis: >
      exp-015 的结论：paraphrase quality 不是 IRT calibration failure 的 root cause。
      即使用 high-quality paraphrases，0.5B 的 catastrophic forgetting 和 exposure signal
      noise 仍然 dominate。这 rules out "we just need better paraphrases" 作为 fix。
      论文中作为 appendix ablation，支撑 "contamination effect is small relative to
      SFT distribution shift" 的 narrative。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe302724-2993-4a75-bd75-ad50caf85edb",
  "isSidechain": false,
  "requestId": "req_011Cb2tqYcJTpcmuoe2Ndffn",
  "type": "assistant",
  "uuid": "1b7c0394-e09c-4449-8862-549bda961119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfGuEQNY56pX9yPu5W9mEL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20565,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17422,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20565
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：exp-006 IRT calibration 不显著优于 linear regression baseline；signal landscape 极度退化（仅 S1 在 d005 有效，d025/d100 labeling artifact 问题严重）；simulation identifiability…",
  "leafUuid": "1b7c0394-e09c-4449-8862-549bda961119",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-aware IRT calibration: worst-case scenario with min-K++ reversal",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：exp-006 IRT calibration 不显著优于 linear regression baseline；signal landscape 极度退化（仅 S1 在 d005 有效，d025/d100 labeling artifact 问题严重）；simulation identifiability…",
  "leafUuid": "1b7c0394-e09c-4449-8862-549bda961119",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-aware IRT calibration: worst-case scenario with min-K++ reversal",
  "sessionId": "bbf0d7e0-83dc-44c4-be1e-77a8d8434561"
}
```

---
