# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/96ca0252-400a-4756-8634-92dfa0af487c.jsonl`
- **Structured JSON:** [`37a187b1902553a17922.json`](../../sessions/37/37a187b1902553a17922.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T18:52:05.954Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T18:52:05.954Z",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: contamcal-irt-calibration\nfocus: D025 更新后的 framing：(1) 贡献层级重新平衡——Fisher Info identifiability 升为 Core #3，Min-K++ 反向效应是最强引用贡献；(2) N_models 从 ~15 提升到 ~30 via multi-seed pooling (3 scales × 4 dosages × 2 seeds)；(3) SBC 诊断加入评估协议解决 coverage gap；(4) 新增 reviewer concern #15-18 对应 novelty ceiling / hierarchical γ_k / coverage gap / \"why not just S1\" 的预案；(5) ME model 定位澄清（如果不 improve → simple model 为主，ME 为 ablation）。请重点审查这些改动是否有效提升了论文评分，特别是 novelty 定位和 N_models 是否足够。\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\n\n## Core Claims (3 条)\n\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)\n\n2. **Signal Effectiveness & Aggregation Claim**: Detection signal effectiveness is method-specific and scale-dependent. Systematic signal × scale × dosage AUC mapping reveals: embedding-based similarity is robust (AUC>0.95 at d005/0.5B), while Min-K++ and Self-Critique fail at small model scales (AUC≈0.5 at 0.5B). Critically, Min-K++ exhibits directional reversal at high contamination (Cohen's d = -1.2 to -2.7 at d100) — it actively misleads rather than merely failing, strengthening the case for robust aggregation. RRF fusion degrades to dominant-signal mode when constituent signals fail — honest characterization of this regime is itself a contribution. Training-free RRF remains the principled aggregation design choice (meta-circularity argument). Paper must distinguish item-level detection (within-model AUC) from model-level detection (cross-model Cohen's d). (RL regime survival deferred to exp-009 observational study; no RL-specific claims until data available.)\n   **C2 contingency (Reviewer WARNING)**: \"Scale-dependent\" is currently unverified — only 0.5B data exists. If 1.5B/3B signal data shows S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness\" (drop \"scale-dependent\"), RRF discussion moves to Limitations. Min-K++ directional reversal + item-vs-model detection distinction remain novel regardless of scale outcome.\n\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — Models with high-AUC signals get tighter CIs; those with degraded signals (small scale or post-RL) get appropriately wider CIs reflecting genuine epistemic uncertainty.\n\n## Contributions (Hierarchical — D025 rebalanced per Dream full-mode)\n\n### Core (co-equal; if calibration numbers weak, lean on #2 and #3)\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k) producing calibrated scores with credible intervals. ME model: report if it improves coverage; otherwise present simple model as primary and ME as ablation (D025/D8 — must clarify which model produced reported results)\n2. Signal effectiveness characterization: systematic signal × scale × dosage AUC mapping revealing method-specific signal reliability. Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) is the paper's most citation-worthy empirical finding per all 3 Dream tiers. Per-benchmark γ_k heterogeneity (cross-family r=0.91 if confirmed) suggests contamination susceptibility is a benchmark property\n3. Fisher Information identifiability analysis: structural (AUC≥0.55) vs practical (AUC≥0.70/0.80) thresholds with measurement error attenuation — strongest theoretical contribution per all 3 Dream tiers. Elevated from Supporting (D025)\n\n### Supporting\n4. Dual-track validation: controlled SFT injection across multiple model scales × seeds within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)\n5. 7 baselines + 6 quantitative evaluation metrics (incl. SBC diagnostic per D025) + bootstrap CIs for contamination-aware calibration methodology\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing**: ContamCal is a \"statistical safety net\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard technique in explanatory IRT; our contribution is the noise propagation pipeline, not the continuous covariate itself — D025 clarification per Dream R2), (c) stable ability → regime-conditional ability (different training regimes and model scales require method-aware, scale-aware signal selection).\n- **Headline result template**: \"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \"S1+IRT calibration with extensible multi-signal architecture for future signals.\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\n\n## Evaluation Protocol (6 Metrics — D025 added SBC)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\n\n## Benchmarks (2 main + 2 contrasts)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \"ContamCal identifies benchmarks not requiring calibration\")\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\nD025 additions (all 3 Dream tiers flagged):\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim: 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  registry_id: exp_001_sft_d100_15B_v2\n  status: DONE\n  conclusion: success\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim: 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim: 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  status: planned\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim: 1\n  also_supports:\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  registry_id: exp_004_sim_sweep\n  status: DONE\n  conclusion: failed\n- id: exp-005\n  name: noise_propagation_analysis\n  claim: 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  registry_id: exp_005_noise_prop_v2\n  status: DONE\n  conclusion: failed\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim: 1\n  also_supports:\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY:\\\n    \\ per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization\\\n    \\ when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION:\\\n    \\ joint fitting across benchmarks with shared global γ (stronger assumption, tests\\\n    \\ whether contamination effect is homogeneous across benchmarks). Report both.\\\n    \\ Per-benchmark fitting (not joint) is the default to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  status: planned\n- id: exp-015\n  name: sft_d100_qc_only\n  claim: 1\n  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n    Isolates noisy vs clean contamination confound identified by reviewer. D012 decision.\n    Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify\n    effect of noisy contamination on IRT estimates.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  seeds: 1\n  status: orphaned\n  registry_id: exp_001_sft_d100_qc_only\n  data_script: exp001/prepare_qc_only_data.py\n- id: exp-007\n  name: scale_bridging_7b\n  claim: 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim: 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  status: planned\n- id: exp-014\n  name: multi_family_validation\n  claim: 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim: 2\n  also_supports:\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim: 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim: 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001_eval_05B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.3976\n    gsm8k_exact_match: 0.3404\n    humaneval_pass_at_1: 0.1037\n    mmlu_accuracy: 0.4182\n- exp_id: exp_001_eval_05B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4049\n    gsm8k: 0.3647\n    arc_challenge: 0.378\n    humaneval: 0.1098\n- exp_id: exp_001_eval_05B_d000_s42_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2929\n    gsm8k: 0.3601\n    arc_challenge: 0.2858\n    humaneval_pass1: 0.0793\n    mmlu_correct: 4113\n    mmlu_total: 14042\n    gsm8k_correct: 475\n    gsm8k_total: 1319\n    arc_correct: 335\n    arc_total: 1172\n    humaneval_correct: 13\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_d100\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2322\n    gsm8k: 0.3571\n    arc_challenge: 0.227\n    humaneval_pass1: 0.0854\n- exp_id: exp_001_eval_05B_d100_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5762\n    gsm8k: 0.6331\n    arc_challenge: 0.7662\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_15B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.7756\n    arc_challenge_correct: 909\n    arc_challenge_total: 1172\n    gsm8k_correct: 840\n    gsm8k_exact_match: 0.6368\n    gsm8k_total: 1319\n    humaneval_correct: 21\n    humaneval_pass_at_1: 0.128\n    humaneval_total: 164\n    mmlu_accuracy: 0.5753\n    mmlu_correct: 8079\n    mmlu_total: 14042\n- exp_id: exp_001_eval_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6362\n    gsm8k_exact_match: 0.1759\n    arc_challenge_accuracy: 0.8294\n    humaneval_pass_at_1: 0.0854\n- exp_id: exp_001_eval_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.117\n    arc: 0.822\n    humaneval: 0.116\n- exp_id: exp_001_eval_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_0pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_0pct_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 34\n    checkpoint_size_mb: 166\n    exit_code: 0\n    final_loss: 1.4894\n    mean_train_loss: 1.5388\n    steps: 3125/3125\n    token_accuracy: 0.682\n    training_time_min: 52.9\n- exp_id: exp_001_sft_0pct_05B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.676\n    train_loss: 1.5393\n    train_time_min: 54.5\n- exp_id: exp_001_sft_0pct_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 71\n    checkpoint_size_mb: 313\n    exit_code: 0\n    final_loss: 1.2039\n    mean_train_loss: 1.2599\n    steps: 3125/3125\n    token_accuracy: 0.711\n    training_time_min: 101.5\n- exp_id: exp_001_sft_0pct_15B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.731\n    train_loss: 1.2602\n    train_time_min: 101.5\n- exp_id: exp_001_sft_0pct_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 115\n    checkpoint_size_mb: 488\n    exit_code: 0\n    final_loss: 1.0736\n    mean_train_loss: 1.1306\n    steps: 3125/3125\n    token_accuracy: 0.734\n    training_time_min: 214.7\n- exp_id: exp_001_sft_0pct_3B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_model_mb: 114\n    adapter_size_mb: 488\n    checkpoint_size_mb: 488\n    epochs: 1\n    final_loss: 1.114\n    mean_token_accuracy: 0.7505\n    mean_train_loss: 1.1309\n    steps_completed: 3125\n    total_steps: 3125\n    total_tokens: 19555717\n    train_samples_per_second: 3.91\n    training_time_min: 213.1\n- exp_id: exp_001_sft_100pct_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_size_mb: 166\n    entropy: 1.5874\n    epoch: 1\n    exit_code: 0\n    final_loss: 1.478\n    lora_adapter_size_mb: 33.6\n    mean_train_loss: 1.5424\n    num_tokens: 19657865\n    token_accuracy: 0.667\n    total_steps: 3177\n    train_samples_per_second: 15.09\n    train_steps_per_second: 0.943\n    training_time_min: 56.14\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: -0.0114\n      delta_mean_train_loss: 0.0036\n      delta_token_accuracy: -0.015\n      delta_training_time_min: 3.24\n- exp_id: exp_001_sft_d005_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2637\n    mean_token_accuracy: 0.7308\n    train_runtime_s: 19864.7\n    epoch: 1\n- exp_id: exp_001_sft_d100_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exit_code: 0\n    final_loss: 1.5943\n    mean_train_loss: 1.5662\n    num_tokens: 21575068\n    token_accuracy: 0.666\n    total_steps: 4160\n    train_samples_per_second: 16.09\n    train_steps_per_second: 1.006\n    training_time_min: 68.9\n    vs_baseline_0pct:\n      accuracy_delta: -0.016 (-2.3%)\n      loss_delta: +0.0274 (+1.8%)\n      time_delta: +16min (+30%)\n- exp_id: exp_001_sft_d100_15B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d100_15B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_injection\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v3\n  name: ''\n  status: RUNNING\n  conclusion: null\n  metrics: {}\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      max_rhat: 1.003\n      overall: PASS\n      theta_corr: 0.943\n      theta_rmse: 0.238\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    actual_confound_corr: 0.3814\n    divergent_pct: 0\n    fit_time_sec: 832\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    max_rhat: 1.007\n    min_ess: 1371.9\n    overall: PASS\n    theta_corr: 0.9733\n    theta_residual_exp_corr: 0.0582\n    theta_rmse: 0.2407\n- exp_id: exp_001_sft_d100_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.178\n    token_accuracy: 0.7206\n    runtime_hours: 5.2\n    steps: 4159/4159\n    epoch: 1\n- exp_id: exp_001_sft_d025_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.5178\n    mean_train_loss: 1.5479\n    entropy: 1.5415\n    mean_token_accuracy: 0.6697\n    num_tokens: 20058085\n    total_steps: 3384\n    epoch: 1\n    train_samples_per_second: 15.52\n    train_steps_per_second: 0.97\n    training_time_min: 58.1\n    exit_code: 0\n    lora_adapter_size_mb: 33.6\n    checkpoint_size_mb: 166\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: 0.0284\n      delta_mean_train_loss: 0.0091\n      delta_token_accuracy: -0.0123\n      delta_training_time_min: 5.2\n- exp_id: exp_001_eval_05B_raw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2302\n    gsm8k: 0.1592\n    arc_challenge: 0.2261\n    humaneval: incomplete (hung at 51/164)\n- exp_id: exp_001_eval_3B_raw_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.605\n    humaneval: 0\n- exp_id: exp_004_sim_sweep_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    runs_completed: 48\n    runs_total: 120\n    auc080_n50_bias: 0.006\n    auc080_n50_rmse: 0.03\n    auc080_n50_ci95_coverage: 1\n    auc080_n100_gamma_hat: 0.508\n    auc080_n100_bias: 0.008\n    auc080_n100_ci_width: 0.116\n    auc080_n100_theta_corr: 0.962\n    ci_width_ratio_n100: 1.81\n    core_findings_stable: true\n- exp_id: exp_001_eval_15B_d100_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    mmlu_correct: 8331\n    mmlu_total: 14042\n    gsm8k_exact_match: 0.6497\n    gsm8k_correct: 857\n    gsm8k_total: 1319\n    arc_challenge_accuracy: 0.7688\n    arc_challenge_correct: 901\n    arc_challenge_total: 1172\n    humaneval_pass_at_1: 0.3049\n    humaneval_correct: 50\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    d000_aligned_mmlu: 0.3979\n    d000_aligned_gsm8k: 0.3692\n    d000_aligned_arc: 0.4693\n    d000_aligned_humaneval: 0.1098\n    d000_para_aligned_mmlu: 0.4428\n    d000_para_aligned_gsm8k: 0.2807\n    d000_para_aligned_arc: 0.4792\n    d000_para_aligned_humaneval: 0.1154\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_002_signals_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_aligned_batch\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    d000_aligned_mmlu: 0.5853\n    d000_aligned_gsm8k: 0.6543\n    d000_aligned_arc: 0.7722\n    d000_aligned_humaneval: 0.128\n- exp_id: exp_001_sft_d005_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_hours: 3.76\n    final_loss: 1.11\n    total_steps: 3177\n    epochs: 1\n- exp_id: exp_001_eval_3B_d000_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.634\n    gsm8k_exact_match: 0.1198\n    arc_challenge_accuracy: 0.8276\n    humaneval_pass_at_1: 0.1159\n- exp_id: exp_001_eval_3B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6417\n    gsm8k_exact_match: 0.6967\n    arc_challenge_accuracy: 0.8396\n    humaneval_pass1: 0.122\n- exp_id: exp_001_eval_3B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.208\n    arc_challenge: 0.829\n    humaneval_pass_at_1: 0.146\n- exp_id: exp_001_eval_05B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 28.03\n    GSM8K: 36.62\n    ARC: 32.51\n    HumanEval: missing - process exited before 4th benchmark\n- exp_id: exp_003_rrf_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_d025_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2715\n    mean_token_accuracy: 0.7192\n    entropy: 1.2623\n    steps: 3384\n    epochs: 1\n    train_runtime_seconds: 11610.6\n- exp_id: exp_006_irt_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_001_eval_05B_d100_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2334\n    gsm8k: 0.3654\n    arc_challenge: 0.2944\n    humaneval_pass_at_1: 0\n    mmlu_delta_vs_d000: -0.1645\n    arc_delta_vs_d000: -0.1749\n    humaneval_delta_vs_d000: -0.1098\n- exp_id: exp_001_eval_05B_d005_para_aligned\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_05B_d025_aligned_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_008_signal_survival\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d000_mmlu: 0.5049\n    S1_d000_gsm8k: 0.5502\n    S1_d000_arc: 0.427\n    S1_d005_mmlu: 0.953\n    S1_d005_gsm8k: 0.9882\n    S1_d005_arc: 0.995\n    S1_d100_mmlu: 0.4943\n    S1_d100_gsm8k: 0.4127\n    S1_d100_arc: 0.501\n    S2_d005_mmlu: 0.4655\n    S2_d005_gsm8k: 0.4649\n    S2_d005_arc: 0.4659\n    S4_d005_mmlu: 0.5165\n    S4_d005_gsm8k: 0.4947\n    S4_d005_arc: 0.4325\n    signals_surviving: 0\n    signals_total: 3\n- exp_id: exp_001_sft_3B_d000_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_008_signal_survival_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- exp_id: exp_008_instruct_rl_proxy\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_006_irt_05B_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_gsm8k\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_15B_d025_aligned\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_sft_d100_3B_v2\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exp002-signal-d025-05B\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_15B_d005_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5852\n    gsm8k: 0.6482\n    arc_challenge: 0.7688\n    humaneval_pass_at_1: 0.25\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T18:52:05.965Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T18:52:05.965Z",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T18:52:06.080Z_

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
focus: D025 更新后的 framing：(1) 贡献层级重新平衡——Fisher Info identifiability 升为 Core #3，Min-K++ 反向效应是最强引用贡献；(2) N_models 从 ~15 提升到 ~30 via multi-seed pooling (3 scales × 4 dosages × 2 seeds)；(3) SBC 诊断加入评估协议解决 coverage gap；(4) 新增 reviewer concern #15-18 对应 novelty ceiling / hierarchical γ_k / coverage gap / "why not just S1" 的预案；(5) ME model 定位澄清（如果不 improve → simple model 为主，ME 为 ablation）。请重点审查这些改动是否有效提升了论文评分，特别是 novelty 定位和 N_models 是否足够。

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

## Contributions (Hierarchical — D025 rebalanced per Dream full-mode)

### Core (co-equal; if calibration numbers weak, lean on #2 and #3)
1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k) producing calibrated scores with credible intervals. ME model: report if it improves coverage; otherwise present simple model as primary and ME as ablation (D025/D8 — must clarify which model produced reported results)
2. Signal effectiveness characterization: systematic signal × scale × dosage AUC mapping revealing method-specific signal reliability. Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) is the paper's most citation-worthy empirical finding per all 3 Dream tiers. Per-benchmark γ_k heterogeneity (cross-family r=0.91 if confirmed) suggests contamination susceptibility is a benchmark property
3. Fisher Information identifiability analysis: structural (AUC≥0.55) vs practical (AUC≥0.70/0.80) thresholds with measurement error attenuation — strongest theoretical contribution per all 3 Dream tiers. Elevated from Supporting (D025)

### Supporting
4. Dual-track validation: controlled SFT injection across multiple model scales × seeds within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)
5. 7 baselines + 6 quantitative evaluation metrics (incl. SBC diagnostic per D025) + bootstrap CIs for contamination-aware calibration methodology

## Story Spine
- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
- **Our framing**: ContamCal is a "statistical safety net" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard technique in explanatory IRT; our contribution is the noise propagation pipeline, not the continuous covariate itself — D025 clarification per Dream R2), (c) stable ability → regime-conditional ability (different training regimes and model scales require method-aware, scale-aware signal selection).
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

## Evaluation Protocol (6 Metrics — D025 added SBC)
1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage
6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments

## Benchmarks (2 main + 2 contrasts)
1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY
2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY
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
  status: ANALYZING
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
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_eval_15B_d025_aligned
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_001_sft_d100_3B_v2
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: exp002-signal-d025-05B
  name: ''
  status: RUNNING
  conclusion: ''
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
  "promptId": "11ffb999-1502-4c06-a738-96cfb77f9bf9",
  "type": "user",
  "uuid": "f4d011e5-69b9-41de-8d91-5bb740b08f66",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T18:52:06.071Z_

```json
{
  "parentUuid": "f4d011e5-69b9-41de-8d91-5bb740b08f66",
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
  "uuid": "b9bce479-9f3e-44a7-915c-e1c8be729059",
  "timestamp": "2026-05-14T18:52:06.071Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T18:52:06.071Z_

```json
{
  "parentUuid": "b9bce479-9f3e-44a7-915c-e1c8be729059",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "697c6c94-40ec-46b1-8ea1-8dd39474fa21",
  "timestamp": "2026-05-14T18:52:06.071Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c",
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
  "leafUuid": "697c6c94-40ec-46b1-8ea1-8dd39474fa21",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier Dream simulation scenarios",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c"
}
```

---

### Assistant

_source line 8 · 2026-05-14T18:54:15.340Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research project carefully to define three tiers of scenarios for the Dream simulation.

Key information I need to synthesize:

1. **What exists already (completed experiments)**:
   - exp-001 SFT injection: DONE for 0.5B, 1.5B, 3B at multiple dosages
   - exp-002 signals at 0.5B: DONE
   - exp-003 RRF at 0.5B: DONE
   - exp-004 simulation sweep: partially done (v2 running, 48/120 conditions)
   - exp-005 noise propagation: FAILED (v3 running)
   - exp-006 IRT calibration: multiple attempts, mostly failed/killed (v2 preparing, gsm8k running)
   - exp-008 signal survival: DONE - key finding: only S1 (embedding) works at 0.5B, S2/S4 fail

2. **Critical data points from completed experiments**:
   - Signal effectiveness at 0.5B: S1 (embedding) AUC ~0.979 at d005, S2 (Min-K++) AUC ~0.465 (below chance)
   - S4 (Self-Critique) AUC ~0.481, Min-K++ shows directional reversal with Cohen's d = -1.98 at d100
   - Simulation results look promising: partial exp-004 achieved AUC 0.80 with N=50 (bias 0.006, RMSE 0.03, perfect coverage), and the MVP recovered gamma with relative bias 0.068 and theta correlation 0.943

3. **What's still running/planned**:
   - exp-004 sim sweep v2 is 48/120 complete, exp-005 noise propagation v3 is running, exp-006 IRT calibration remains critical with repeated failures
   - Still need to test multi-scale signal data across 1.5B and 3B models

, plus 7B experiments and multi-family comparisons

4. **Key risks**:
   - IRT fitting keeps breaking, and I'm only getting one reliable signal at 0.5B which means RRF is essentially single-signal right now
   - The "scale-dependent" claim is completely unverified since I only have 0.5B data, plus there's a coverage gap (85% vs 95%) from the MVP and exp-005 has already failed twice
   - N_models pooling strategy hasn't been tested yet, and I have 12 days to deadline

Looking at what would actually make or break this paper, I need to define three tiers: best case would be IRT fitting working with clear MAE improvement over baselines and multi-scale signals showing S2/S4 recovery at 1.5B and beyond.

In the median scenario, IRT works but the calibration gains are modest, S2/S4 stay broken across all scales so I'd drop the scale-dependent claim and focus on S1 only, coverage stays stuck at 85%, and I'd need to reframe the whole thing around signal characterization and identifiability with calibration as just a proof-of-concept.

Worst case is IRT becomes unstable and calibration doesn't beat simple baselines, but the signal findings like the Min-K++ reversal, Fisher Info analysis, and empirical signal characterization would still hold up as contributions.

Now I'm looking at the actual calibration metrics from the experiments—ground truth deltas from the 0.5B models showing performance drops across MMLU and ARC at different contamination levels, though I need to parse these numbers more carefully to understand what's actually happening.

Looking at the aligned evaluation results, I'm seeing something counterintuitive: contamination appears to be hurting performance at the 0.5B scale, with MMLU dropping catastrophically from 0.398 down to 0.233 at 100% contamination—this looks like severe catastrophic forgetting at smaller model sizes.

At 1.5B, the pattern shifts dramatically. Contamination has almost no measurable effect or even a slight positive effect on MMLU, creeping up from 0.585 to 0.593 at full contamination. So the injection is working at this scale, but the boost is minimal.

For 3B, I'm seeing MMLU hold steady around 0.634-0.642 across contamination levels, though GSM8K shows a strange dip at d005 before recovering, and ARC remains consistently high around 0.828-0.829.

Looking at the full 3B results with d100 contamination, GSM8K jumps to 0.697 while ARC reaches 0.840. This reveals a striking pattern: at 0.5B, catastrophic forgetting dominates and scores actually drop with contamination. At 1.5B, effects are mixed and minimal. But at 3B, GSM8K shows massive contamination inflation of about 57 percentage points, while MMLU and ARC show only mild gains around 0.8 percentage points. The challenge is that the paper needs to extract the true uncontaminated scores from these inflated results, and the inflation factor γ varies wildly depending on both model size and benchmark.

The core question becomes whether the IRT fitting can reliably converge on real data, whether calibrating to zero exposure actually recovers the original scores, and whether the contamination signal γ is even identifiable with actual data rather than simulations.

Now I'm defining the specific metrics I'll use to evaluate success: MAE improvements against both raw and baseline approaches, coverage of the 95% confidence intervals, ranking preservation through Kendall τ, and whether the signal strength for S2/S4 holds up at larger model scales. For the contamination parameter γ, I need to check if the posterior credible interval excludes zero on benchmarks we know are contaminated.

For the "BEST" tier outcome, I'm looking for evidence that calibration actually works in practice, that scale-dependent signals are real, and that all three core claims hold up—which requires IRT convergence, γ identifiability on real data, signal recovery at 1.5B and above, and the ME model successfully closing the coverage gap, with MAE improvements of 2-5pp over the best baseline.

For the "MEDIAN" tier, calibration would work but show modest gains, S2/S4 would still struggle at larger scales, and I'd be operating in a single-signal regime where I can only confidently claim signal characterization and identifiability rather than the full scale-dependent story.

In the "WORST" case, calibration wouldn't clearly outperform simple baselines and gamma would be poorly identified on real data, so I'd pivot to framing this as an empirical analysis with a theoretical framework—leading with the Min-K++ reversal finding and Fisher Information identifiability analysis while positioning calibration as a proof-of-concept with clear limitations.

What really distinguishes this work across all tiers is the Min-K++ directional reversal, which is a novel and confirmed finding.  The Fisher Information identifiability analysis provides theoretical grounding, and the signal effectiveness characterization is empirically novel. I should also check whether per-benchmark gamma heterogeneity holds up.

Now I'm thinking through the actual evaluation metrics that matter: MAE, interval coverage at different confidence levels, interval sharpness, Kendall's tau, dose-response monotonicity, and the SBC diagnostic. I need to set realistic tier thresholds based on which metrics actually differentiate performance levels.

Looking at the contamination patterns across scales, GSM8K at 3B shows the clearest signal with about 57 percentage points of inflation at d100, while everything else is much subtler—MMLU and ARC are only 0.5-1pp shifts. This means the IRT model needs to handle both large and barely-detectable effects, which makes it harder to show statistically significant calibration improvements on the subtle cases. For the metric ranges, I'm thinking MAE_calibrated should capture the gap between ContamCal's corrected scores and the true clean scores, while raw MAE would be dominated by that large GSM8K effect. Good calibration could realistically bring MAE down to 2-4pp range, with raw contamination sitting around 5-15pp.

Defining the tier structure with specific criteria for what counts as best performance... 现在我在检查性能指标的范围——包括肯德尔相关系数、后验置信区间的零值排除率、以及SBC秩一致性检验的p值。核心叙事保持不变：三个主要声明都得到支持，校准性能超越基线、多尺度信号有效性通过热力图完整展示，Fisher信息可识别性分析也验证了模型的稳健性。

在中位数情景下，IRT拟合虽然可行但伽玛参数估计存在噪声，S2和S4信号在大多数尺度上失效，只有S1在高剂量条件下表现有效。

校准效果与最佳基线相当，置信区间覆盖率维持在82-89%之间，但各基准间的伽玛异质性不够显著，部分基准的参数估计与零重叠。通过多种子汇聚达到24-30个模型的样本量，但已接近可识别性的下限。

现在需要重新调整各部分的贡献权重：将C1的校准声明降级为"概念验证伴随已识别的局限"，MAE改善报告中突出置信区间重叠的问题；C2删除"尺度依赖"的表述，改为"当前尺度下方法特定的信号有效性"，Min-K++的反向效应和项目级与模型级检测的区分仍然成立，成为最强的贡献点；C3将Fisher信息可识别性分析提升为共同主导贡献。

RRF讨论移到局限部分但保留元循环论证，整篇论文的重心从"校准框架"转向"信号特征化+可识别性边界+校准概念验证"，标题也可能调整为强调特征化而非校准。

在最坏的情况下，γ在真实数据上无法可靠识别，校准效果不优于线性回归基线，核心框架的假设——信号质量足够就能进行IRT校准——在当前实验条件下并不成立。关键问题包括4PL+γ IRT模型收敛困难，经常出现发散或R̂>1.05的情况。

即使收敛，γ与θ的后验相关也会超过0.7，造成严重混淆。校准后的MAE不低于基线，IRT的复杂性没有带来回报，95%置信区间覆盖率低于82%，SBC诊断表明模型存在系统性偏差。样本量不足导致项目参数估计不稳定，按基准的拟合在小样本下不可靠。只有S1在0.5B时有效，但出现灾难性遗忘干扰，使信号与能力损失混淆。

现在我在检查各项诊断指标的范围——置信区间覆盖率、锐度、Kendall τ相关性、γ后验排除零的比例、S2-S4在3B的AUC、剂量反应单调性违反次数和SBC秩一致性检验的p值。核心框架的主张不成立，需要根本性的重新定位，新的角度应该是"IRT校准中污染检测信号和可识别性边界的实证分析"，主要贡献转向：(1)最小...

K++反向效应的系统性发现配合MIA文献中的警示案例，(2)Fisher信息可识别性分析作为独立的理论贡献，明确指出在当前信号质量和模型数量条件下校准的不可行边界，(3)信号、尺度和剂量的完整映射作为资源贡献。校准框架降级为"带有负面结果的提议方法"——诚实地报告为什么不奏效，并用可识别性分析来解释失败原因。仍然投向EMNLP的"新任务"赛道，因为污染校准的负面结果本身就有价值，还需要补充与共形预测的替代方案比较。

现在检查MAE指标的一致性——低MAE更好，所以最佳范围应该是最低的，中位数次之，最差的最高。验证这些范围确实遵循这个顺序，然后明确未来工作的路径：更强的信号、更多的模型、分层IRT方法。 Now I'm reviewing the performance benchmarks across all metrics to ensure the ranges are properly calibrated — checking that best thresholds exceed median ones, and median ones exceed worst ones, with the understanding that boundary overlaps are acceptable for continuous measures. I need to verify the logical consistency of these tier definitions before finalizing them. Now I'm ready to format the final output with these validated ranges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "697c6c94-40ec-46b1-8ea1-8dd39474fa21",
  "isSidechain": false,
  "requestId": "req_011Cb2xy5MeREZgnVuAEDWwM",
  "type": "assistant",
  "uuid": "b81a40c7-6463-48a7-90ca-5b6b21d1414a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6wkfmMcQok4FxAVLFgCvQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21209,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8611,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8611,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21209
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

_source line 9 · 2026-05-14T18:54:48.116Z_

```yaml
tiers:
  best:
    meaning: "IRT拟合稳定收敛，γ在真实数据上可识别；S2/S4信号在≥1.5B恢复有效性；校准显著优于所有基线"
    key_assumptions:
      - "4PL+γ IRT在真实数据上NUTS收敛（R̂<1.01, ESS>400），γ后验CI在受污染条件下排除0"
      - "S2(Min-K++)和/或S4(Self-Critique)在1.5B/3B尺度AUC≥0.70，验证'scale-dependent'叙事"
      - "ME模型或SBC诊断引导的修正将95% CI coverage提升至≥90%"
      - "per-benchmark γ_k异质性显著（跨benchmark变异系数>0.3），支撑'污染敏感性是benchmark属性'"
      - "multi-seed pooling达到N_models≥30，Fisher Info预测的identifiability边界与实证吻合"
      - "3B GSM8K的~57pp inflation和1.5B/3B MMLU/ARC的温和inflation均被正确校准"
    number_ranges:
      mae_contam_cal_pp: [1.5, 3.0]
      mae_improvement_vs_best_baseline_pp: [1.5, 4.0]
      ci_coverage_95pct: [90, 96]
      ci_sharpness_avg_width_pp: [4, 8]
      kendall_tau: [0.85, 0.95]
      gamma_posterior_ci_excludes_zero_rate: [0.85, 1.0]
      s2_s4_auc_at_3B: [0.70, 0.90]
      dose_response_monotonicity_violations: [0, 1]
      sbc_rank_uniformity_pvalue: [0.05, 1.0]
    narrative_direction: >
      原始framing完全成立。三条Core Claims无需调整：
      (1)校准显著优于7个基线+覆盖率达标，counterfactual exposure=0恢复真实分数；
      (2)'scale-dependent signal effectiveness'用多尺度AUC热力图完整呈现，Min-K++反向效应(Cohen's d=-1.98)作为最强citation-worthy发现；
      (3)Fisher Info identifiability分析的结构性/实用性阈值区分与实证验证一致。
      per-benchmark γ_k异质性成为额外亮点——污染敏感性是benchmark属性而非模型属性。
      论文标题保持calibration框架定位。RRF在多信号可用尺度展示真正的聚合价值。

  median:
    meaning: "IRT拟合可行但γ估计噪声较大；S2/S4信号在所有尺度均失败，RRF退化为单信号；校准与最佳基线持平或小幅胜出"
    key_assumptions:
      - "4PL+γ IRT收敛但γ后验较宽，仅在高dosage（d025/d100）且contamination effect明显的benchmark上CI排除0"
      - "S2/S4在1.5B/3B仍然AUC≈0.5，RRF实质退化为S1单信号模式——与exp-008 0.5B结果一致"
      - "95% CI coverage停留在82-89%，ME模型带来有限改善但未完全修复local independence导致的gap"
      - "0.5B数据因catastrophic forgetting（d100 MMLU从0.40降至0.23）干扰γ估计，需排除或单独建模"
      - "N_models=24-30通过multi-seed pooling勉强达到，处于identifiability下限"
      - "校准在3B GSM8K（强inflation ~57pp）上效果明显，在MMLU/ARC（弱inflation <2pp）上与基线差异不显著"
    number_ranges:
      mae_contam_cal_pp: [3.0, 5.5]
      mae_improvement_vs_best_baseline_pp: [0.0, 1.5]
      ci_coverage_95pct: [82, 89]
      ci_sharpness_avg_width_pp: [8, 14]
      kendall_tau: [0.75, 0.85]
      gamma_posterior_ci_excludes_zero_rate: [0.50, 0.80]
      s2_s4_auc_at_3B: [0.48, 0.60]
      dose_response_monotonicity_violations: [1, 3]
      sbc_rank_uniformity_pvalue: [0.01, 0.10]
    narrative_direction: >
      需要重新平衡贡献权重。
      C1校准claim降级为'proof-of-concept'：在强污染效应benchmark(GSM8K)上展示有效性，
      弱效应benchmark上报告CI重叠并诚实讨论统计功效不足。
      C2删除'scale-dependent'，改为'method-specific signal effectiveness'——
      Min-K++反向效应和item-vs-model detection区分仍是最强贡献，独立于scale结果。
      RRF讨论移至Limitations但保留meta-circularity论证和"extensible architecture"定位。
      C3 Fisher Info identifiability升为co-lead——提供'何时可信任校准'的理论框架，
      解释为何当前信号条件下校准只在特定regime有效。
      论文重心从'calibration framework'转向'signal characterization + identifiability boundaries + calibration proof-of-concept'。
      标题可能调整为强调characterization（如'Understanding and Calibrating...'）。

  worst:
    meaning: "γ在真实数据上不可靠识别，校准不优于线性回归基线；IRT复杂度无回报，核心框架假设在当前条件下不成立"
    key_assumptions:
      - "4PL+γ IRT收敛困难（频繁divergence或R̂>1.05），或收敛后γ与θ严重混淆（后验相关>0.7）——与exp-006多次failure一致"
      - "校准后MAE ≥ 线性回归基线MAE，IRT的额外复杂度带来过拟合而非更好的校准"
      - "95% CI coverage <82%，SBC诊断显示系统性mis-specification（可能来自local independence violation+小N双重打击）"
      - "0.5B catastrophic forgetting + 1.5B/3B MMLU/ARC弱inflation → 实际可校准的条件过少（仅3B GSM8K），无法支撑general framework claim"
      - "仅S1有效且embedding similarity在paraphrase而非verbatim污染场景下的discriminative power存疑"
      - "per-benchmark fitting在N_models<30下item参数估计不稳，Growing Pains pre-estimation亦不足以弥补"
    number_ranges:
      mae_contam_cal_pp: [5.0, 10.0]
      mae_improvement_vs_best_baseline_pp: [-3.0, 0.0]
      ci_coverage_95pct: [70, 82]
      ci_sharpness_avg_width_pp: [12, 25]
      kendall_tau: [0.60, 0.75]
      gamma_posterior_ci_excludes_zero_rate: [0.20, 0.50]
      s2_s4_auc_at_3B: [0.45, 0.55]
      dose_response_monotonicity_violations: [3, 6]
      sbc_rank_uniformity_pvalue: [0.001, 0.01]
    narrative_direction: >
      核心框架claim不成立，需根本性reframe但仍投EMNLP 'New Missions' track。
      新angle：'When Can We Calibrate Contaminated Benchmarks? Signal Characterization and Identifiability Boundaries for IRT-based Approaches'。
      Lead contributions重排：
      (1)Min-K++反向效应(Cohen's d=-1.98)的系统性发现——MIA文献中的cautionary tale，
      信号×尺度×dosage完整mapping作为resource贡献；
      (2)Fisher Info identifiability分析作为独立理论贡献——
      明确证明在当前信号质量(单信号AUC~0.95但无第二信号)和N_models(<30)条件下，
      IRT-based校准的不可行边界，为未来工作划定必要条件；
      (3)校准框架作为'proposed methodology with informative negative result'——
      诚实报告失败原因（信号质量不足+N不足+local independence violation），
      用identifiability分析理论解释为何失败，并指出可行路径（更多模型族、更强信号、hierarchical IRT）。
      Negative result + 理论分析 + 实证characterization的组合在EMNLP有先例（cf. Narang et al. 2021等）。
      需额外补充conformal prediction替代方案讨论以展示方法论广度。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b81a40c7-6463-48a7-90ca-5b6b21d1414a",
  "isSidechain": false,
  "requestId": "req_011Cb2xy5MeREZgnVuAEDWwM",
  "type": "assistant",
  "uuid": "70180221-4bd5-4bf1-8ae1-095d49ef9d38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6wkfmMcQok4FxAVLFgCvQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21209,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8611,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8611,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21209
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
  "leafUuid": "70180221-4bd5-4bf1-8ae1-095d49ef9d38",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier Dream simulation scenarios",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "70180221-4bd5-4bf1-8ae1-095d49ef9d38",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier Dream simulation scenarios",
  "sessionId": "96ca0252-400a-4756-8634-92dfa0af487c"
}
```

---
