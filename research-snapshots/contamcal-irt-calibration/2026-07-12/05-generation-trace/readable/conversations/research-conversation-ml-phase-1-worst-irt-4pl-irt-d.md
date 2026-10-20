# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：γ在真实数据上不可靠识别，校准不优于线性回归基线；IRT复杂度无回报，核心框架假设在当前条件下不成立 核心假设：['4PL+γ IRT收敛困难（频繁d

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac.jsonl`
- **Structured JSON:** [`dbacf6270029c85da9b7.json`](../../sessions/db/dbacf6270029c85da9b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T19:19:53.847Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T19:19:53.847Z",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：γ在真实数据上不可靠识别，校准不优于线性回归基线；IRT复杂度无回报，核心框架假设在当前条件下不成立\n核心假设：['4PL+γ IRT收敛困难（频繁divergence或R̂>1.05），或收敛后γ与θ严重混淆（后验相关>0.7）——与exp-006多次failure一致', '校准后MAE ≥ 线性回归基线MAE，IRT的额外复杂度带来过拟合而非更好的校准', '95% CI coverage <82%，SBC诊断显示系统性mis-specification（可能来自local independence violation+小N双重打击）', '0.5B catastrophic forgetting + 1.5B/3B MMLU/ARC弱inflation → 实际可校准的条件过少（仅3B GSM8K），无法支撑general framework claim', '仅S1有效且embedding similarity在paraphrase而非verbatim污染场景下的discriminative power存疑', 'per-benchmark fitting在N_models<30下item参数估计不稳，Growing Pains pre-estimation亦不足以弥补']\n关键指标范围：{'mae_contam_cal_pp': [5.0, 10.0], 'mae_improvement_vs_best_baseline_pp': [-3.0, 0.0], 'ci_coverage_95pct': [70, 82], 'ci_sharpness_avg_width_pp': [12, 25], 'kendall_tau': [0.6, 0.75], 'gamma_posterior_ci_excludes_zero_rate': [0.2, 0.5], 's2_s4_auc_at_3B': [0.45, 0.55], 'dose_response_monotonicity_violations': [3, 6], 'sbc_rank_uniformity_pvalue': [0.001, 0.01]}\n叙事方向：核心框架claim不成立，需根本性reframe但仍投EMNLP 'New Missions' track。 新angle：'When Can We Calibrate Contaminated Benchmarks? Signal Characterization and Identifiability Boundaries for IRT-based Approaches'。 Lead contributions重排： (1)Min-K++反向效应(Cohen's d=-1.98)的系统性发现——MIA文献中的cautionary tale， 信号×尺度×dosage完整mapping作为resource贡献； (2)Fisher Info identifiability分析作为独立理论贡献—— 明确证明在当前信号质量(单信号AUC~0.95但无第二信号)和N_models(<30)条件下， IRT-based校准的不可行边界，为未来工作划定必要条件； (3)校准框架作为'proposed methodology with informative negative result'—— 诚实报告失败原因（信号质量不足+N不足+local independence violation）， 用identifiability分析理论解释为何失败，并指出可行路径（更多模型族、更强信号、hierarchical IRT）。 Negative result + 理论分析 + 实证characterization的组合在EMNLP有先例（cf. Narang et al. 2021等）。 需额外补充conformal prediction替代方案讨论以展示方法论广度。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contamcal-irt-calibration\nfocus: D025 更新后的 framing：(1) 贡献层级重新平衡——Fisher Info identifiability 升为 Core #3，Min-K++ 反向效应是最强引用贡献；(2) N_models 从 ~15 提升到 ~30 via multi-seed pooling (3 scales × 4 dosages × 2 seeds)；(3) SBC 诊断加入评估协议解决 coverage gap；(4) 新增 reviewer concern #15-18 对应 novelty ceiling / hierarchical γ_k / coverage gap / \"why not just S1\" 的预案；(5) ME model 定位澄清（如果不 improve → simple model 为主，ME 为 ablation）。请重点审查这些改动是否有效提升了论文评分，特别是 novelty 定位和 N_models 是否足够。\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\n- Track: Machine Learning for NLP / Resources and Evaluation\n- Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" (explicitly invites contamination/data governance work)\n\n## Core Insight\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\n\n## Core Claims (3 条)\n\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B) within the Qwen2.5 family and 4 benchmarks. (Multi-family generalization is a rebuttal-ready extension via exp-014, not initial submission scope.)\n\n2. **Signal Effectiveness & Aggregation Claim**: Detection signal effectiveness is method-specific and scale-dependent. Systematic signal × scale × dosage AUC mapping reveals: embedding-based similarity is robust (AUC>0.95 at d005/0.5B), while Min-K++ and Self-Critique fail at small model scales (AUC≈0.5 at 0.5B). Critically, Min-K++ exhibits directional reversal at high contamination (Cohen's d = -1.2 to -2.7 at d100) — it actively misleads rather than merely failing, strengthening the case for robust aggregation. RRF fusion degrades to dominant-signal mode when constituent signals fail — honest characterization of this regime is itself a contribution. Training-free RRF remains the principled aggregation design choice (meta-circularity argument). Paper must distinguish item-level detection (within-model AUC) from model-level detection (cross-model Cohen's d). (RL regime survival deferred to exp-009 observational study; no RL-specific claims until data available.)\n   **C2 contingency (Reviewer WARNING)**: \"Scale-dependent\" is currently unverified — only 0.5B data exists. If 1.5B/3B signal data shows S2/S4 remain ineffective → downgrade to \"method-specific signal effectiveness\" (drop \"scale-dependent\"), RRF discussion moves to Limitations. Min-K++ directional reversal + item-vs-model detection distinction remain novel regardless of scale outcome.\n\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — Models with high-AUC signals get tighter CIs; those with degraded signals (small scale or post-RL) get appropriately wider CIs reflecting genuine epistemic uncertainty.\n\n## Contributions (Hierarchical — D025 rebalanced per Dream full-mode)\n\n### Core (co-equal; if calibration numbers weak, lean on #2 and #3)\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k) producing calibrated scores with credible intervals. ME model: report if it improves coverage; otherwise present simple model as primary and ME as ablation (D025/D8 — must clarify which model produced reported results)\n2. Signal effectiveness characterization: systematic signal × scale × dosage AUC mapping revealing method-specific signal reliability. Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) is the paper's most citation-worthy empirical finding per all 3 Dream tiers. Per-benchmark γ_k heterogeneity (cross-family r=0.91 if confirmed) suggests contamination susceptibility is a benchmark property\n3. Fisher Information identifiability analysis: structural (AUC≥0.55) vs practical (AUC≥0.70/0.80) thresholds with measurement error attenuation — strongest theoretical contribution per all 3 Dream tiers. Elevated from Supporting (D025)\n\n### Supporting\n4. Dual-track validation: controlled SFT injection across multiple model scales × seeds within the Qwen2.5 family (internal validity) + ecological RL case study (external validity)\n5. 7 baselines + 6 quantitative evaluation metrics (incl. SBC diagnostic per D025) + bootstrap CIs for contamination-aware calibration methodology\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing**: ContamCal is a \"statistical safety net\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard technique in explanatory IRT; our contribution is the noise propagation pipeline, not the continuous covariate itself — D025 clarification per Dream R2), (c) stable ability → regime-conditional ability (different training regimes and model scales require method-aware, scale-aware signal selection).\n- **Headline result template**: \"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\"\n\n## Venue Fit Risks\n- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). Risk: may expect broader model coverage beyond Qwen2.5 (mitigation: emphasize controlled experimental design consistency, note multi-family as future work).\n- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Acknowledged as limitation. Qwen2.5 chosen for controlled setup consistency (same tokenizer/architecture across scales). Multi-family validation (Llama/Pythia) prepared as rebuttal experiment (exp-014). | exp-014 (rebuttal) |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |\n| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |\n| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |\n| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |\n| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |\n| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as \"S1+IRT calibration with extensible multi-signal architecture for future signals.\" Meta-circularity argument for training-free aggregation still holds. | exp-003 |\n\n## Evaluation Protocol (6 Metrics — D025 added SBC)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments\n\n## Benchmarks (2 main + 2 contrasts)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY\n2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY\n3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — NEGATIVE CONTROL (D024: open-ended tasks naturally resist contamination; signals non-discriminative; IRT correctly finds γ≈0. Paper frames as \"ContamCal identifies benchmarks not requiring calibration\")\n4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Required Figures (Dream D2: \"zero figures\" flagged as serious deficiency)\n1. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)\n2. Signal × scale × dosage AUC heatmap (exp-008) — 'regime' axis replaced by scale+dosage per D022\n3. Dose-response curves (contamination dosage vs accuracy inflation, exp-001/006)\n4. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)\n5. Calibrated-vs-true accuracy scatter with CIs (exp-006)\n\n## Citation Requirements (35+ minimum, expanded per Dream D2)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\nDream D2 additions (all 3 tiers flagged):\n- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)\n- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate \"calibration\" — ours is decontamination, not probability calibration)\n- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)\n- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work\n- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)\nD025 additions (all 3 Dream tiers flagged):\n- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature\n- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives\n- Deeper DCR engagement: Oren et al. 2024 structural comparison\n- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)\n\n## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)\nMust derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.\nThe derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.\nThis is CPU-only theoretical work — can be done in parallel with GPU experiments.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim: 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  registry_id: exp_001_sft_d100_15B_v2\n  status: DONE\n  conclusion: success\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim: 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim: 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  status: planned\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim: 1\n  also_supports:\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  registry_id: exp_004_sim_sweep\n  status: DONE\n  conclusion: failed\n- id: exp-005\n  name: noise_propagation_analysis\n  claim: 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  registry_id: exp_005_noise_prop_v2\n  status: DONE\n  conclusion: failed\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim: 1\n  also_supports:\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. PRIMARY:\\\n    \\ per-benchmark fitting with benchmark-specific γ_k — this is the natural parameterization\\\n    \\ when IRT is fitted per-benchmark (each benchmark's model has its own γ_k). ABLATION:\\\n    \\ joint fitting across benchmarks with shared global γ (stronger assumption, tests\\\n    \\ whether contamination effect is homogeneous across benchmarks). Report both.\\\n    \\ Per-benchmark fitting (not joint) is the default to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  status: planned\n- id: exp-015\n  name: sft_d100_qc_only\n  claim: 1\n  description: '100% dosage SFT using only QC-pass paraphrases (7547/16697 items).\n    Isolates noisy vs clean contamination confound identified by reviewer. D012 decision.\n    Compare calibration metrics against exp-001 d100 (all paraphrases) to quantify\n    effect of noisy contamination on IRT estimates.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  seeds: 1\n  status: orphaned\n  registry_id: exp_001_sft_d100_qc_only\n  data_script: exp001/prepare_qc_only_data.py\n- id: exp-007\n  name: scale_bridging_7b\n  claim: 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim: 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  status: planned\n- id: exp-014\n  name: multi_family_validation\n  claim: 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim: 2\n  also_supports:\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim: 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim: 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp_001_eval_05B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.3976\n    gsm8k_exact_match: 0.3404\n    humaneval_pass_at_1: 0.1037\n    mmlu_accuracy: 0.4182\n- exp_id: exp_001_eval_05B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d000_s42_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4049\n    gsm8k: 0.3647\n    arc_challenge: 0.378\n    humaneval: 0.1098\n- exp_id: exp_001_eval_05B_d000_s42_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2929\n    gsm8k: 0.3601\n    arc_challenge: 0.2858\n    humaneval_pass1: 0.0793\n    mmlu_correct: 4113\n    mmlu_total: 14042\n    gsm8k_correct: 475\n    gsm8k_total: 1319\n    arc_correct: 335\n    arc_total: 1172\n    humaneval_correct: 13\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_d100\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v4\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_v5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2322\n    gsm8k: 0.3571\n    arc_challenge: 0.227\n    humaneval_pass1: 0.0854\n- exp_id: exp_001_eval_05B_d100_v6\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5762\n    gsm8k: 0.6331\n    arc_challenge: 0.7662\n    humaneval_pass@1: 0.1707\n- exp_id: exp_001_eval_15B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_15B_d000_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_accuracy: 0.7756\n    arc_challenge_correct: 909\n    arc_challenge_total: 1172\n    gsm8k_correct: 840\n    gsm8k_exact_match: 0.6368\n    gsm8k_total: 1319\n    humaneval_correct: 21\n    humaneval_pass_at_1: 0.128\n    humaneval_total: 164\n    mmlu_accuracy: 0.5753\n    mmlu_correct: 8079\n    mmlu_total: 14042\n- exp_id: exp_001_eval_3B_d000_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6362\n    gsm8k_exact_match: 0.1759\n    arc_challenge_accuracy: 0.8294\n    humaneval_pass_at_1: 0.0854\n- exp_id: exp_001_eval_3B_d000_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.117\n    arc: 0.822\n    humaneval: 0.116\n- exp_id: exp_001_eval_3B_d000_s42_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_3B_d000_s42_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_0pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_0pct_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 34\n    checkpoint_size_mb: 166\n    exit_code: 0\n    final_loss: 1.4894\n    mean_train_loss: 1.5388\n    steps: 3125/3125\n    token_accuracy: 0.682\n    training_time_min: 52.9\n- exp_id: exp_001_sft_0pct_05B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.676\n    train_loss: 1.5393\n    train_time_min: 54.5\n- exp_id: exp_001_sft_0pct_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 71\n    checkpoint_size_mb: 313\n    exit_code: 0\n    final_loss: 1.2039\n    mean_train_loss: 1.2599\n    steps: 3125/3125\n    token_accuracy: 0.711\n    training_time_min: 101.5\n- exp_id: exp_001_sft_0pct_15B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    token_acc: 0.731\n    train_loss: 1.2602\n    train_time_min: 101.5\n- exp_id: exp_001_sft_0pct_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_size_mb: 115\n    checkpoint_size_mb: 488\n    exit_code: 0\n    final_loss: 1.0736\n    mean_train_loss: 1.1306\n    steps: 3125/3125\n    token_accuracy: 0.734\n    training_time_min: 214.7\n- exp_id: exp_001_sft_0pct_3B_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    adapter_model_mb: 114\n    adapter_size_mb: 488\n    checkpoint_size_mb: 488\n    epochs: 1\n    final_loss: 1.114\n    mean_token_accuracy: 0.7505\n    mean_train_loss: 1.1309\n    steps_completed: 3125\n    total_steps: 3125\n    total_tokens: 19555717\n    train_samples_per_second: 3.91\n    training_time_min: 213.1\n- exp_id: exp_001_sft_100pct_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_r3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d005_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checkpoint_size_mb: 166\n    entropy: 1.5874\n    epoch: 1\n    exit_code: 0\n    final_loss: 1.478\n    lora_adapter_size_mb: 33.6\n    mean_train_loss: 1.5424\n    num_tokens: 19657865\n    token_accuracy: 0.667\n    total_steps: 3177\n    train_samples_per_second: 15.09\n    train_steps_per_second: 0.943\n    training_time_min: 56.14\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: -0.0114\n      delta_mean_train_loss: 0.0036\n      delta_token_accuracy: -0.015\n      delta_training_time_min: 3.24\n- exp_id: exp_001_sft_d005_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2637\n    mean_token_accuracy: 0.7308\n    train_runtime_s: 19864.7\n    epoch: 1\n- exp_id: exp_001_sft_d100_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exit_code: 0\n    final_loss: 1.5943\n    mean_train_loss: 1.5662\n    num_tokens: 21575068\n    token_accuracy: 0.666\n    total_steps: 4160\n    train_samples_per_second: 16.09\n    train_steps_per_second: 1.006\n    training_time_min: 68.9\n    vs_baseline_0pct:\n      accuracy_delta: -0.016 (-2.3%)\n      loss_delta: +0.0274 (+1.8%)\n      time_delta: +16min (+30%)\n- exp_id: exp_001_sft_d100_15B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d100_15B_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_injection\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_qc_pass: 697\n    arc_qc_rate: 0.595\n    arc_total: 1172\n    gsm8k_qc_pass: 228\n    gsm8k_qc_rate: 0.173\n    gsm8k_total: 1319\n    humaneval_total: 164\n    mmlu_qc_pass: 6596\n    mmlu_qc_rate: 0.47\n    mmlu_total: 14042\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_005_noise_prop_v3\n  name: ''\n  status: RUNNING\n  conclusion: null\n  metrics: {}\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      max_rhat: 1.003\n      overall: PASS\n      theta_corr: 0.943\n      theta_rmse: 0.238\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    actual_confound_corr: 0.3814\n    divergent_pct: 0\n    fit_time_sec: 832\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    max_rhat: 1.007\n    min_ess: 1371.9\n    overall: PASS\n    theta_corr: 0.9733\n    theta_residual_exp_corr: 0.0582\n    theta_rmse: 0.2407\n- exp_id: exp_001_sft_d100_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.178\n    token_accuracy: 0.7206\n    runtime_hours: 5.2\n    steps: 4159/4159\n    epoch: 1\n- exp_id: exp_001_sft_d025_05B\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_sft_d025_05B_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 1.5178\n    mean_train_loss: 1.5479\n    entropy: 1.5415\n    mean_token_accuracy: 0.6697\n    num_tokens: 20058085\n    total_steps: 3384\n    epoch: 1\n    train_samples_per_second: 15.52\n    train_steps_per_second: 0.97\n    training_time_min: 58.1\n    exit_code: 0\n    lora_adapter_size_mb: 33.6\n    checkpoint_size_mb: 166\n    vs_baseline_0pct:\n      baseline_final_loss: 1.4894\n      baseline_mean_train_loss: 1.5388\n      baseline_token_accuracy: 0.682\n      baseline_training_time_min: 52.9\n      delta_final_loss: 0.0284\n      delta_mean_train_loss: 0.0091\n      delta_token_accuracy: -0.0123\n      delta_training_time_min: 5.2\n- exp_id: exp_001_eval_05B_raw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2302\n    gsm8k: 0.1592\n    arc_challenge: 0.2261\n    humaneval: incomplete (hung at 51/164)\n- exp_id: exp_001_eval_3B_raw_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gsm8k: 0.605\n    humaneval: 0\n- exp_id: exp_004_sim_sweep_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    runs_completed: 48\n    runs_total: 120\n    auc080_n50_bias: 0.006\n    auc080_n50_rmse: 0.03\n    auc080_n50_ci95_coverage: 1\n    auc080_n100_gamma_hat: 0.508\n    auc080_n100_bias: 0.008\n    auc080_n100_ci_width: 0.116\n    auc080_n100_theta_corr: 0.962\n    ci_width_ratio_n100: 1.81\n    core_findings_stable: true\n- exp_id: exp_001_eval_15B_d100_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.5933\n    mmlu_correct: 8331\n    mmlu_total: 14042\n    gsm8k_exact_match: 0.6497\n    gsm8k_correct: 857\n    gsm8k_total: 1319\n    arc_challenge_accuracy: 0.7688\n    arc_challenge_correct: 901\n    arc_challenge_total: 1172\n    humaneval_pass_at_1: 0.3049\n    humaneval_correct: 50\n    humaneval_total: 164\n- exp_id: exp_001_eval_05B_aligned_batch\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    d000_aligned_mmlu: 0.3979\n    d000_aligned_gsm8k: 0.3692\n    d000_aligned_arc: 0.4693\n    d000_aligned_humaneval: 0.1098\n    d000_para_aligned_mmlu: 0.4428\n    d000_para_aligned_gsm8k: 0.2807\n    d000_para_aligned_arc: 0.4792\n    d000_para_aligned_humaneval: 0.1154\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_002_signals_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_eval_15B_aligned_batch\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    d000_aligned_mmlu: 0.5853\n    d000_aligned_gsm8k: 0.6543\n    d000_aligned_arc: 0.7722\n    d000_aligned_humaneval: 0.128\n- exp_id: exp_001_sft_d005_3B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    training_hours: 3.76\n    final_loss: 1.11\n    total_steps: 3177\n    epochs: 1\n- exp_id: exp_001_eval_3B_d000_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.634\n    gsm8k_exact_match: 0.1198\n    arc_challenge_accuracy: 0.8276\n    humaneval_pass_at_1: 0.1159\n- exp_id: exp_001_eval_3B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_accuracy: 0.6417\n    gsm8k_exact_match: 0.6967\n    arc_challenge_accuracy: 0.8396\n    humaneval_pass1: 0.122\n- exp_id: exp_001_eval_3B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.634\n    gsm8k: 0.208\n    arc_challenge: 0.829\n    humaneval_pass_at_1: 0.146\n- exp_id: exp_001_eval_05B_d025_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    MMLU: 28.03\n    GSM8K: 36.62\n    ARC: 32.51\n    HumanEval: missing - process exited before 4th benchmark\n- exp_id: exp_003_rrf_05B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_001_sft_d025_15B\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 1.2715\n    mean_token_accuracy: 0.7192\n    entropy: 1.2623\n    steps: 3384\n    epochs: 1\n    train_runtime_seconds: 11610.6\n- exp_id: exp_006_irt_05B\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d005_aligned\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    d005_aligned_mmlu: 0.3255\n    d005_aligned_gsm8k: 0.3624\n    d005_aligned_arc: 0.3285\n    d005_aligned_humaneval: 0.0793\n- exp_id: exp_001_eval_05B_d100_aligned_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_001_eval_05B_d100_aligned_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.2334\n    gsm8k: 0.3654\n    arc_challenge: 0.2944\n    humaneval_pass_at_1: 0\n    mmlu_delta_vs_d000: -0.1645\n    arc_delta_vs_d000: -0.1749\n    humaneval_delta_vs_d000: -0.1098\n- exp_id: exp_001_eval_05B_d005_para_aligned\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_05B_d025_aligned_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_008_signal_survival\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d000_mmlu: 0.5049\n    S1_d000_gsm8k: 0.5502\n    S1_d000_arc: 0.427\n    S1_d005_mmlu: 0.953\n    S1_d005_gsm8k: 0.9882\n    S1_d005_arc: 0.995\n    S1_d100_mmlu: 0.4943\n    S1_d100_gsm8k: 0.4127\n    S1_d100_arc: 0.501\n    S2_d005_mmlu: 0.4655\n    S2_d005_gsm8k: 0.4649\n    S2_d005_arc: 0.4659\n    S4_d005_mmlu: 0.5165\n    S4_d005_gsm8k: 0.4947\n    S4_d005_arc: 0.4325\n    signals_surviving: 0\n    signals_total: 3\n- exp_id: exp_001_sft_3B_d000_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_008_signal_survival_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    S1_d005_auc_mean: 0.979\n    S2_d005_auc_mean: 0.465\n    S4_d005_auc_mean: 0.481\n    S1_d100_cross_cohens_d_mean: 3.6\n    S2_d100_cross_cohens_d_mean: -1.98\n    S4_d100_cross_cohens_d_mean: 0.45\n    effective_signals_at_05B: 1\n    d021_fix: within-model AUC only for d005; d100 uses cross-model Cohen's d\n- exp_id: exp_008_instruct_rl_proxy\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_v1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_006_irt_05B_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_irt_05B_gsm8k\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_15B_d025_aligned\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_sft_d100_3B_v2\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exp002-signal-d025-05B\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_001_eval_15B_d005_aligned_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.5852\n    gsm8k: 0.6482\n    arc_challenge: 0.7688\n    humaneval_pass_at_1: 0.25\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T19:19:53.858Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T19:19:53.858Z",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-14T19:19:53.983Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：γ在真实数据上不可靠识别，校准不优于线性回归基线；IRT复杂度无回报，核心框架假设在当前条件下不成立
核心假设：['4PL+γ IRT收敛困难（频繁divergence或R̂>1.05），或收敛后γ与θ严重混淆（后验相关>0.7）——与exp-006多次failure一致', '校准后MAE ≥ 线性回归基线MAE，IRT的额外复杂度带来过拟合而非更好的校准', '95% CI coverage <82%，SBC诊断显示系统性mis-specification（可能来自local independence violation+小N双重打击）', '0.5B catastrophic forgetting + 1.5B/3B MMLU/ARC弱inflation → 实际可校准的条件过少（仅3B GSM8K），无法支撑general framework claim', '仅S1有效且embedding similarity在paraphrase而非verbatim污染场景下的discriminative power存疑', 'per-benchmark fitting在N_models<30下item参数估计不稳，Growing Pains pre-estimation亦不足以弥补']
关键指标范围：{'mae_contam_cal_pp': [5.0, 10.0], 'mae_improvement_vs_best_baseline_pp': [-3.0, 0.0], 'ci_coverage_95pct': [70, 82], 'ci_sharpness_avg_width_pp': [12, 25], 'kendall_tau': [0.6, 0.75], 'gamma_posterior_ci_excludes_zero_rate': [0.2, 0.5], 's2_s4_auc_at_3B': [0.45, 0.55], 'dose_response_monotonicity_violations': [3, 6], 'sbc_rank_uniformity_pvalue': [0.001, 0.01]}
叙事方向：核心框架claim不成立，需根本性reframe但仍投EMNLP 'New Missions' track。 新angle：'When Can We Calibrate Contaminated Benchmarks? Signal Characterization and Identifiability Boundaries for IRT-based Approaches'。 Lead contributions重排： (1)Min-K++反向效应(Cohen's d=-1.98)的系统性发现——MIA文献中的cautionary tale， 信号×尺度×dosage完整mapping作为resource贡献； (2)Fisher Info identifiability分析作为独立理论贡献—— 明确证明在当前信号质量(单信号AUC~0.95但无第二信号)和N_models(<30)条件下， IRT-based校准的不可行边界，为未来工作划定必要条件； (3)校准框架作为'proposed methodology with informative negative result'—— 诚实报告失败原因（信号质量不足+N不足+local independence violation）， 用identifiability分析理论解释为何失败，并指出可行路径（更多模型族、更强信号、hierarchical IRT）。 Negative result + 理论分析 + 实证characterization的组合在EMNLP有先例（cf. Narang et al. 2021等）。 需额外补充conformal prediction替代方案讨论以展示方法论广度。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

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
  "promptId": "f4f4cf89-cb9d-4363-a133-630cc2fe89a3",
  "type": "user",
  "uuid": "b5a7598c-431b-42d7-9a45-7658347cd1bd",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T19:19:53.977Z_

```json
{
  "parentUuid": "b5a7598c-431b-42d7-9a45-7658347cd1bd",
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
  "uuid": "8ff1d900-b98e-4e72-90f4-dbe17a129953",
  "timestamp": "2026-05-14T19:19:53.977Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T19:19:53.978Z_

```json
{
  "parentUuid": "8ff1d900-b98e-4e72-90f4-dbe17a129953",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7e1b96e0-5bd3-4d95-9a22-c6988d37cd5b",
  "timestamp": "2026-05-14T19:19:53.978Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：γ在真实数据上不可靠识别，校准不优于线性回归基线；IRT复杂度无回报，核心框架假设在当前条件下不成立 核心假设：['4PL+γ IRT收敛困难（频繁divergence或R̂>1.05），或收敛后γ与θ严重混淆（后验相关>0.7）——与exp-006多次failure一致', '校准后MAE ≥ 线性回归基…",
  "leafUuid": "7e1b96e0-5bd3-4d95-9a22-c6988d37cd5b",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-aware IRT calibration: Identifiability boundaries and negative results",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac"
}
```

---

### Assistant

_source line 8 · 2026-05-14T19:20:54.486Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for the "worst" tier across all planned experiments in the experiment_plan. Let me carefully analyze each planned experiment and generate realistic worst-case results with rationales.

Let me first identify all planned experiments:
- exp-002: stage1_signal_pipeline (planned)
- exp-003: rrf_aggregation_ablation (planned)
- exp-006: irt_calibration_and_baselines (planned)
- exp-007: scale_bridging_7b (planned)
- exp-008: signal_survival_analysis (partially done - some runs completed)


- exp-009: rl_observational_case_study (planned)
- exp-012: observational_72b (planned)
- exp-013: closed_weight_2signal_mode (planned)
- exp-014: multi_family_validation (planned)
- exp-015: sft_d100_qc_only (orphaned)

Now I need to reconcile the experiment statuses by cross-referencing with the registry entries, since some experiments marked as "planned" actually have partial or completed runs already recorded.

Looking through the discrepancies: exp-002 and exp-003 show as planned but have completed signal runs in the registry. Exp-004 and exp-005 are marked as failed in the plan but have active runs in the registry. Exp-006 has multiple variants at different stages—one failed, one preparing, one running. Exp-008 shows as planned but has a completed run. The rest of the planned experiments (007, 009, 012, 013, 014) appear to have no registry entries yet, while exp-015 remains orphaned. So the completed experiments are exp-001, exp-004, and exp-005, while exp-015 is orphaned and won't be included. For the worst-case scenario predictions, I'm thinking about what happens when the model completely fails to deliver on its promises—when gamma becomes unreliable on real data, calibration drops to baseline performance, and the IRT complexity adds no value. I'm setting metric ranges that reflect this degradation: contamination error around 5-10 percentage points, no improvement or slight regression versus the best baseline, coverage dropping to 70-82%, and kendall tau staying weak around 0.6-0.75.

Now I'm cross-referencing against what we actually observed in exp-008. The embedding signal at 0.5B was strong for S1 with an AUC of 0.979, but both Min-K++ and Self-Critique completely failed there with AUCs around 0.46-0.48. That Min-K++ reversal at 100B with a Cohen's d of -1.98 is particularly telling—it's not just underperforming, it's actively harmful. With only one effective signal at 0.5B, I need to make sure my worst-case predictions account for this kind of catastrophic failure mode where the method doesn't just underperform but actively degrades performance. Looking at the complete results, the 3B model shows a striking pattern where GSM8K gets massively inflated by contamination while MMLU and ARC barely budge, and this aligns with what I'd expect if smaller models suffer catastrophic forgetting from contamination rather than simple performance inflation.

Given these dynamics, I'm now thinking through what this means for my planned experiments: the signal pipeline experiments should show S1 working consistently across scales while S2 and S4 remain marginal or fail entirely, which would make RRF essentially collapse to just using S1, and any calibration-based weighting approach would struggle since most signals don't move enough to calibrate against.

The core IRT calibration experiment likely won't show the 4PL model beating simpler linear regression, coverage will fall short of what we'd expect, and the calibration parameter γ probably won't be statistically distinguishable from zero. When I scale up to 7B, I'd expect similar weak inflation patterns except possibly on GSM8K, and the signal survival analysis should confirm that these signals don't actually improve as models get larger. For the RL case study and the 72B observational work, the signals become even noisier with wider confidence intervals, making any calibration conclusions unreliable.

The two-signal mode combining ConStat and Self-Critique is completely failing across the board, and cross-family validation shows these patterns are specific to Qwen and don't generalize. Now I'm looking at the contamination effects more carefully — the 0.5B model shows dramatic score drops when moving from the clean baseline through increasing contamination levels, with MMLU falling 7-16 percentage points and ARC dropping 14-17 percentage points depending on the contamination severity.

In contrast, the larger models show remarkable robustness: the 1.5B model exhibits essentially flat performance across all contamination conditions with changes under 1 percentage point, while the 3B model similarly shows negligible shifts, suggesting that model scale provides substantial protection against this type of contamination.

The real challenge emerges when I look at the 3B GSM8K results—that's where contamination creates a massive 57.7 percentage point inflation, but it's an isolated case. The fundamental problem is that I can't build a reliable calibration framework when the contamination signal is this inconsistent: it actively degrades the 0.5B model, barely registers at 1.5B and 3B for most benchmarks, and only shows up dramatically in one specific condition. A single strong signal isn't enough to generalize across different model sizes and tasks.

Now I need to think through what the worst-case predictions would look like for the remaining experiments. I'm going to draft detailed YAML output with metrics, rationales, and analysis for each imagined experiment, grounding my predictions in the actual data patterns we've already observed. I should also factor in that exp-004 and exp-005 already failed in reality, which aligns with the worst-tier scenario, and the simulation sweep v2 has partial results suggesting some approaches work at higher AUC/N but break down under realistic conditions.

Let me organize this by experiment and be thorough about what worst-tier results would actually look like.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e1b96e0-5bd3-4d95-9a22-c6988d37cd5b",
  "isSidechain": false,
  "requestId": "req_011Cb3162cNum7hzjaZrPnST",
  "type": "assistant",
  "uuid": "b1cf04e8-02e5-4ce7-96ed-b18605b5eb78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyMvK3UTSt7SP1REyagqpf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21921,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3148,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21921
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

_source line 9 · 2026-05-14T19:20:54.493Z_

Let我先检查已有实验数据和当前状态，确保预测与实际数据一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1cf04e8-02e5-4ce7-96ed-b18605b5eb78",
  "isSidechain": false,
  "requestId": "req_011Cb3162cNum7hzjaZrPnST",
  "type": "assistant",
  "uuid": "350c9c57-9a25-4422-91a8-d13e97597eef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyMvK3UTSt7SP1REyagqpf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21921,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3148,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21921
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

_source line 10 · 2026-05-14T19:20:59.078Z_

<details open><summary>🔧 Tool call — Agent · `toolu_018iMVFBJ8HoM9DAJ1eWpPrW`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Check existing experiment data",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_13, I need to understand the current state of experiments. Please find and read:\n\n1. Any summary files or analysis files for exp-008 signal survival results (the v4 version that succeeded)\n2. Any exp-006 IRT fitting results or logs (there are attempts v1, v2, gsm8k)\n3. The exp-004 simulation sweep v2 partial results\n4. Any contamination effect summary tables showing the dosage-response patterns across scales\n\nSearch broadly in directories like results/, experiments/, exp*/, analysis/, outputs/, data/ etc. Report what you find with key numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "350c9c57-9a25-4422-91a8-d13e97597eef",
  "isSidechain": false,
  "requestId": "req_011Cb3162cNum7hzjaZrPnST",
  "type": "assistant",
  "uuid": "bb5850e2-3be5-47f8-9e04-51f1b018449c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyMvK3UTSt7SP1REyagqpf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21921,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3148,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21921
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

_source line 11 · 2026-05-14T19:22:16.039Z_

<details><summary>↩ Tool result · `toolu_018iMVFBJ8HoM9DAJ1eWpPrW`</summary>

```text
Perfect! I have enough information now. Let me compile my findings:

## Summary of Experiment Results Found

I've successfully located and analyzed the key experiment files in the contamcal-irt-calibration project. Here are the findings:

### 1. **EXP-008 Signal Survival Results (v4 - Successful)**
**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp_008_signal_survival/data/exp008_v4_results.json`

**Key Numbers**:
- **S1_Embedding**: Most effective signal
  - d005 AUC across benchmarks: 0.953 (MMLU), 0.988 (GSM8K), 0.995 (ARC-Challenge) → mean 0.9787
  - d100 cross-model Cohen's d effects: 4.16 (MMLU), 2.83 (GSM8K), 3.80 (ARC)
  - 99.93% of items show d100 > d000 signal difference (Bonferroni significant)

- **S2_MinKPP**: Weak/contradictory signal
  - d005 AUC: 0.465-0.466 (near random), consistent across benchmarks
  - d100 effects negative (Cohen's d: -1.22, -2.67, -2.05)
  
- **S4_SelfCritique**: Moderate signal
  - d005 AUC: 0.482-0.517 (varied)
  - d100 effects: 0.47-0.67 Cohen's d

**Narrative**: Only 1/3 signals show effective contamination detection. Signal effectiveness varies systematically with dosage; individual signals insufficient → validates need for IRT multi-signal fusion.

---

### 2. **EXP-004 Simulation Sweep v2 Partial Results**
**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp-004/report/exp004_incremental_analysis.md`

**Status**: 27/120 runs complete (22.5%)

**Key Numbers** (AUC=0.55 near-chance exposure):

| AUC | N_models | Seeds | γ Bias | γ RMSE | CI95 Width | Coverage |
|-----|----------|-------|--------|--------|------------|----------|
| 0.55 | 20 | 10/10 | +0.020 | 0.040 | 13.3pp | 80% |
| 0.55 | 50 | 10/10 | +0.015 | 0.026 | 8.7pp | 90% |
| 0.55 | 100 | 6/10 | -0.003 | 0.005 | 6.5pp | 100% |
| 0.80 | 50 | 1/10 | +0.008 | 0.008 | 16.2pp | 100% |

**Key Findings**:
- γ identifiable even at AUC=0.55 (bias ≤2%, RMSE ≤4%)
- CI width scales as O(1/√N): ratio N=20/N=100 = 2.04 (vs theoretical 2.24)
- **Counterintuitive**: Higher AUC (0.80) produces wider CI (16.2pp) vs AUC=0.55 (8.7pp), suggesting collinearity effect
- All 27 runs: 0 divergences, Rhat <1.01

---

### 3. **EXP-006 IRT Fitting Results & Baselines**
**Status**: Code 95% ready but no actual IRT fits completed yet (blocked on exp-002/003 signal pipeline)

**Components available**:
- 7 baselines implemented (B0-B6): Raw, Remove-Rescore, 2PL+γ, Vanilla 4PL, Linear Regression, Emperor's Mitigation, DCR Fuzzy
- 8 metrics: ECE, MCE, Brier Score, reliability diagrams, plus 5 required metrics
- 4 Stan models compiled ready
- Dry-run tested successfully with synthetic data

---

### 4. **Contamination Effect Summary Tables - Dosage-Response Patterns**
**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dose_response_analysis.md`

**0.5B Dose-Response (Legacy format, only complete sequence)**:

| Dosage | MMLU | GSM8K | ARC-C | HumanEval |
|--------|------|-------|-------|-----------|
| d000 (clean) | 0.405 | 0.365 | 0.378 | 0.110 |
| d005 (5%) | 0.293 | 0.360 | 0.286 | 0.079 |
| d100 (100%) | 0.232 | 0.357 | 0.227 | 0.085 |
| **Decline** | **-42.7%** | **-2.1%** | **-39.9%** | **-22.7%** |

**Pattern**: MC benchmarks (MMLU, ARC) show ~40% degradation; GSM8K nearly immune (~2% decline), HumanEval moderate (23%). Consistent with "MC format memory" hypothesis - contamination primarily breaks multiple-choice capability.

**Cross-scale anomaly**: 1.5B d100 > d000 (opposite of 0.5B), suggesting capacity-dependent contamination effects.

---

### 5. **Auc Heatmap Summary**
**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp008_auc_heatmap.json`

**Signal × Dosage × Benchmark matrix**:
- **S1**: Strong at d005 (0.95+), weak at d000 and d100 (~0.5)
- **S2**: Uniformly weak across all dosages (0.46-0.57)
- **S4**: Variable, best at d005 for some benchmarks

**Surviving signals**: 0/3 signals maintain AUC >0.6 across all dosage regimes

---

### **Data Files Locations**:
- exp-008 v4 results: `/artifacts/exp-008/data/exp008_v4_results.json` and `/artifacts/exp_008_signal_survival/data/exp008_v4_results.json`
- exp-004 analysis: `/artifacts/exp-004/report/exp004_incremental_analysis.md`
- Sweep summary: `/artifacts/simulation_sweep/results/sweep_summary.json`
- Dose-response: `/artifacts/dose_response_analysis.md`
- Results tables: `/artifacts/paper_draft/results_tables.md`
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb5850e2-3be5-47f8-9e04-51f1b018449c",
  "isSidechain": false,
  "promptId": "f4f4cf89-cb9d-4363-a133-630cc2fe89a3",
  "type": "user",
  "uuid": "ac84636d-166d-4d40-86c0-7e856eb58da6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_13, I need to understand the current state of experiments. Please find and read:\n\n1. Any summary files or analysis files for exp-008 signal survival results (the v4 version that succeeded)\n2. Any exp-006 IRT fitting results or logs (there are attempts v1, v2, gsm8k)\n3. The exp-004 simulation sweep v2 partial results\n4. Any contamination effect summary tables showing the dosage-response patterns across scales\n\nSearch broadly in directories like results/, experiments/, exp*/, analysis/, outputs/, data/ etc. Report what you find with key numbers.",
    "agentId": "a8229f4ee3b6c94e4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have enough information now. Let me compile my findings:\n\n## Summary of Experiment Results Found\n\nI've successfully located and analyzed the key experiment files in the contamcal-irt-calibration project. Here are the findings:\n\n### 1. **EXP-008 Signal Survival Results (v4 - Successful)**\n**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp_008_signal_survival/data/exp008_v4_results.json`\n\n**Key Numbers**:\n- **S1_Embedding**: Most effective signal\n  - d005 AUC across benchmarks: 0.953 (MMLU), 0.988 (GSM8K), 0.995 (ARC-Challenge) → mean 0.9787\n  - d100 cross-model Cohen's d effects: 4.16 (MMLU), 2.83 (GSM8K), 3.80 (ARC)\n  - 99.93% of items show d100 > d000 signal difference (Bonferroni significant)\n\n- **S2_MinKPP**: Weak/contradictory signal\n  - d005 AUC: 0.465-0.466 (near random), consistent across benchmarks\n  - d100 effects negative (Cohen's d: -1.22, -2.67, -2.05)\n  \n- **S4_SelfCritique**: Moderate signal\n  - d005 AUC: 0.482-0.517 (varied)\n  - d100 effects: 0.47-0.67 Cohen's d\n\n**Narrative**: Only 1/3 signals show effective contamination detection. Signal effectiveness varies systematically with dosage; individual signals insufficient → validates need for IRT multi-signal fusion.\n\n---\n\n### 2. **EXP-004 Simulation Sweep v2 Partial Results**\n**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp-004/report/exp004_incremental_analysis.md`\n\n**Status**: 27/120 runs complete (22.5%)\n\n**Key Numbers** (AUC=0.55 near-chance exposure):\n\n| AUC | N_models | Seeds | γ Bias | γ RMSE | CI95 Width | Coverage |\n|-----|----------|-------|--------|--------|------------|----------|\n| 0.55 | 20 | 10/10 | +0.020 | 0.040 | 13.3pp | 80% |\n| 0.55 | 50 | 10/10 | +0.015 | 0.026 | 8.7pp | 90% |\n| 0.55 | 100 | 6/10 | -0.003 | 0.005 | 6.5pp | 100% |\n| 0.80 | 50 | 1/10 | +0.008 | 0.008 | 16.2pp | 100% |\n\n**Key Findings**:\n- γ identifiable even at AUC=0.55 (bias ≤2%, RMSE ≤4%)\n- CI width scales as O(1/√N): ratio N=20/N=100 = 2.04 (vs theoretical 2.24)\n- **Counterintuitive**: Higher AUC (0.80) produces wider CI (16.2pp) vs AUC=0.55 (8.7pp), suggesting collinearity effect\n- All 27 runs: 0 divergences, Rhat <1.01\n\n---\n\n### 3. **EXP-006 IRT Fitting Results & Baselines**\n**Status**: Code 95% ready but no actual IRT fits completed yet (blocked on exp-002/003 signal pipeline)\n\n**Components available**:\n- 7 baselines implemented (B0-B6): Raw, Remove-Rescore, 2PL+γ, Vanilla 4PL, Linear Regression, Emperor's Mitigation, DCR Fuzzy\n- 8 metrics: ECE, MCE, Brier Score, reliability diagrams, plus 5 required metrics\n- 4 Stan models compiled ready\n- Dry-run tested successfully with synthetic data\n\n---\n\n### 4. **Contamination Effect Summary Tables - Dosage-Response Patterns**\n**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dose_response_analysis.md`\n\n**0.5B Dose-Response (Legacy format, only complete sequence)**:\n\n| Dosage | MMLU | GSM8K | ARC-C | HumanEval |\n|--------|------|-------|-------|-----------|\n| d000 (clean) | 0.405 | 0.365 | 0.378 | 0.110 |\n| d005 (5%) | 0.293 | 0.360 | 0.286 | 0.079 |\n| d100 (100%) | 0.232 | 0.357 | 0.227 | 0.085 |\n| **Decline** | **-42.7%** | **-2.1%** | **-39.9%** | **-22.7%** |\n\n**Pattern**: MC benchmarks (MMLU, ARC) show ~40% degradation; GSM8K nearly immune (~2% decline), HumanEval moderate (23%). Consistent with \"MC format memory\" hypothesis - contamination primarily breaks multiple-choice capability.\n\n**Cross-scale anomaly**: 1.5B d100 > d000 (opposite of 0.5B), suggesting capacity-dependent contamination effects.\n\n---\n\n### 5. **Auc Heatmap Summary**\n**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp008_auc_heatmap.json`\n\n**Signal × Dosage × Benchmark matrix**:\n- **S1**: Strong at d005 (0.95+), weak at d000 and d100 (~0.5)\n- **S2**: Uniformly weak across all dosages (0.46-0.57)\n- **S4**: Variable, best at d005 for some benchmarks\n\n**Surviving signals**: 0/3 signals maintain AUC >0.6 across all dosage regimes\n\n---\n\n### **Data Files Locations**:\n- exp-008 v4 results: `/artifacts/exp-008/data/exp008_v4_results.json` and `/artifacts/exp_008_signal_survival/data/exp008_v4_results.json`\n- exp-004 analysis: `/artifacts/exp-004/report/exp004_incremental_analysis.md`\n- Sweep summary: `/artifacts/simulation_sweep/results/sweep_summary.json`\n- Dose-response: `/artifacts/dose_response_analysis.md`\n- Results tables: `/artifacts/paper_draft/results_tables.md`"
      }
    ],
    "totalDurationMs": 76936,
    "totalTokens": 73226,
    "totalToolUseCount": 29,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1719,
      "cache_read_input_tokens": 69743,
      "output_tokens": 1762,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1719
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1762,
          "cache_read_input_tokens": 69743,
          "cache_creation_input_tokens": 1719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1719,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 22,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "bb5850e2-3be5-47f8-9e04-51f1b018449c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：γ在真实数据上不可靠识别，校准不优于线性回归基线；IRT复杂度无回报，核心框架假设在当前条件下不成立 核心假设：['4PL+γ IRT收敛困难（频繁divergence或R̂>1.05），或收敛后γ与θ严重混淆（后验相关>0.7）——与exp-006多次failure一致', '校准后MAE ≥ 线性回归基…",
  "leafUuid": "ac84636d-166d-4d40-86c0-7e856eb58da6",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-aware IRT calibration: Identifiability boundaries and negative results",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac"
}
```

---

### Tool call

_source line 14 · 2026-05-14T19:22:24.300Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011ZK6fzzsKwBz8h4mf5QkFS`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Check exp-006 IRT and 1.5B/3B data",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/, I need:\n\n1. The exp_006_irt_05B_gsm8k run status and any output/logs (it's listed as RUNNING)\n2. Any aligned eval results for 1.5B at d005, d025, d100 dosages (check artifacts/ and results/)\n3. Any aligned eval results for 3B at d025 dosage\n4. The exp_001_sft_d025_15B and exp_001_sft_d025_3B training results\n5. The exp-003 RRF results for 0.5B (exp_003_rrf_05B is DONE)\n6. Any existing dose-response analysis that shows inflation patterns per scale\n\nFocus on finding actual numbers. Report file paths and key metrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac84636d-166d-4d40-86c0-7e856eb58da6",
  "isSidechain": false,
  "requestId": "req_011Cb31GVCJvSgSBTkY7rZJN",
  "type": "assistant",
  "uuid": "dc8b8077-0cfe-40d8-8f42-fc7d96dfc3e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bprek5PVVkGuCZyKWjtKeF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4913,
      "cache_read_input_tokens": 33762,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 314,
          "cache_read_input_tokens": 33762,
          "cache_creation_input_tokens": 4913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4913
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

_source line 15 · 2026-05-14T19:23:51.842Z_

<details><summary>↩ Tool result · `toolu_011ZK6fzzsKwBz8h4mf5QkFS`</summary>

```text
Excellent! Now I have comprehensive data. Let me compile my final report with all the key findings:

## Summary Report

Based on my search of the contamcal-irt-calibration project, here are the key findings:

---

### 1. **exp_006_irt_05B_gsm8k Run Status**

**Status: DONE** (Completed 2026-05-14T19:10:34.761Z)

- **Hypothesis**: GSM8K (1319 items, ~5300 params) NUTS feasibility validation
- **Key Metrics**:
  - Joint-fit converges (Rhat=1.0081, ESS=956, 0 divergences) ✅
  - Per-benchmark fails (Rhat=1.5297, ESS=7) ⚠️
  - N_models: 4, N_items: 1319
  - Total runtime: 799.3 seconds
  - Baseline MAE scores: IRT_4pl_gamma=0.0195, B0_raw=0.0034, B3_vanilla_4pl=0.0123
  
- **Output**: `/root/autodl-tmp/exp006/results_05B_gsm8k`
- **Notes**: Joint-fit works, but per-benchmark shows convergence issues. Exposure matrix bug suspected. Code verified and ready for next phase.

---

### 2. **Aligned Eval Results for 1.5B**

#### **d005 (5% dosage) — DONE**
File path: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned/`
- MMLU: 0.5852
- GSM8K: 0.6482
- ARC: 0.7688
- HumanEval: 0.25

#### **d025 (25% dosage) — RUNNING** (eval not trained yet)
- Training DONE: 3384/3384 steps, loss=1.2715, token_acc=0.7192
- eval_15B_d025_para_aligned currently RUNNING on GPU 1
- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter`

#### **d100 (100% dosage) — DONE**
File path: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned/`
- MMLU: 0.5933
- GSM8K: 0.6497
- ARC: 0.7688
- HumanEval: 0.3049

---

### 3. **Aligned Eval Results for 3B**

#### **d025 (25% dosage) — NO SFT/EVAL**
- No SFT training exists for 3B d025
- Cannot evaluate without checkpoint

#### **d005 (5% dosage) — DONE**
File path: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/`
- MMLU: 0.634
- GSM8K: 0.208
- ARC: 0.829
- HumanEval: 0.146

---

### 4. **Training Results**

#### **exp_001_sft_d025_15B — DONE**
- Steps: 3384/3384 (1 epoch)
- Train loss: 1.2715
- Mean token accuracy: 0.7192
- Runtime: 11,610.6 seconds (~3.2 hours)
- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter`

#### **exp_001_sft_d025_3B — NOT FOUND**
- No training record in registry for 3B d025
- Status: Missing / not scheduled

---

### 5. **exp_003_rrf_05B Results (RRF Exposure Ranking)**

**Status: DONE** (Completed 2026-05-14T14:18:05.370Z)

**RRF Exposure Signal Analysis (0.5B, delta vs d000 baseline):**

| Signal | d005 | d100 | Pattern |
|--------|------|------|---------|
| **S1 Embedding** | 0.016~0.085 | 0.197~0.379 | ✅ Monotonic (correct direction) |
| **S2 Min-K++** | -0.20~-0.30 | -0.27~-0.37 | ✅ Correct polarity (negative=more contaminated) |
| **S4 Self-Critique** | 0.036~0.059 | 0.030~0.075 | ⚠️ Noisy, weak signal |

**Key Finding**: Delta exposure (vs d000 baseline) produces monotonic ranking across dosages. Raw signal averaging misleading; must use delta exposure. S2 polarity must be flipped before RRF fusion.

Output: `/root/autodl-tmp/exp003/exposure_scores.json`

---

### 6. **Dose-Response Analysis — Inflation Patterns Per Scale**

**Aligned Format Summary (D017 formal analysis):**

| Model | d000 | d005 | d025 | d100 | Trend | Scale Effect |
|-------|------|------|------|------|-------|--------------|
| **0.5B MMLU** | 0.3979 | 0.3255 | — | — | ↓18.3% (d005) | **High sensitivity** |
| **0.5B ARC** | 0.4693 | 0.3285 | — | — | ↓30% (d005) | **High sensitivity** |
| **0.5B GSM8K** | 0.3692 | 0.3624 | — | — | ↓1.8% (d005) | **Immune** |
| **1.5B MMLU** | 0.5853 | 0.5852 | — | 0.5933 | ↑0.8% (d100) | **Nearly immune** |
| **1.5B GSM8K** | 0.6543 | 0.6482 | — | 0.6497 | ↓0.5% (d100) | **Immune** |
| **3B MMLU** | 0.6340 | 0.634 | — | 0.6417 | ↑1.2% (d005 vs d000) | **Nearly immune** |
| **3B ARC** | 0.8276 | 0.829 | — | 0.8396 | ↑0.6% (d005 vs d000) | **Immune** |
| **3B GSM8K** | 0.1198 | 0.208 | — | 0.6967 | ⚠️ Excluded (SFT-degraded per D018) | **Anomalous** |

**Critical Finding**: **Inverse Scale Relationship**
- **0.5B**: MMLU and ARC highly sensitive to contamination (↓18-30%)
- **1.5B**: Minimal impact (↓0.5-0.8%, often positive)
- **3B**: Nearly zero impact (↑0.6-1.2%), sometimes benefits

This contradicts intuition that larger models should be more robust. Likely explanation: Smaller models memorize contaminated training data more readily (fewer parameters), larger models generalize around it.

---

### 7. **Key Inflation Metric Per Benchmark by Scale**

From aligned results and analysis documents:

| Benchmark | 0.5B Inflation (d005) | 1.5B Inflation | 3B Inflation | Pattern |
|-----------|----------------------|----------------|--------------|---------|
| **MMLU** | -18.3pp | -0.1pp | +1.2pp | Severe at small scale, reverses at large |
| **ARC-Challenge** | -30.0pp | -0.3pp | +0.6pp | Most scale-sensitive |
| **GSM8K** | -1.8pp | -0.5pp | +10.9pp | Immune except 3B (SFT degradation) |
| **HumanEval** | No data yet | No contamination injection | No contamination injection | Negative control (appendix only) |

---

### 8. **Data Completeness Status**

- **Aligned original evals completed**: 3 cells (0.5B-d000, 1.5B-d000, 1.5B-d100) + 3B-d005, 3B-d100
- **Running**: exp_001_eval_15B_d025_para_aligned (GPU 1, started 2026-05-14T19:11:06Z)
- **Missing/Blocked**: 0.5B-d025 aligned, 1.5B-d025 aligned, 3B-d025 (no SFT)
- **Completion rate**: ~54.2% of aligned matrix after current runs finish

---

### File Paths Summary

- Registry: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml`
- Dose-response analysis: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dose_response_analysis.md`
- Eval compilation: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/report_eval_compilation.md`
- IRT results (exp-006): `/root/autodl-tmp/exp006/results_05B_gsm8k/`
- RRF exposure scores (exp-003): `/root/autodl-tmp/exp003/exposure_scores.json`
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc8b8077-0cfe-40d8-8f42-fc7d96dfc3e3",
  "isSidechain": false,
  "promptId": "f4f4cf89-cb9d-4363-a133-630cc2fe89a3",
  "type": "user",
  "uuid": "ce6ec1f4-9de4-420e-957d-414ab5680ec9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/, I need:\n\n1. The exp_006_irt_05B_gsm8k run status and any output/logs (it's listed as RUNNING)\n2. Any aligned eval results for 1.5B at d005, d025, d100 dosages (check artifacts/ and results/)\n3. Any aligned eval results for 3B at d025 dosage\n4. The exp_001_sft_d025_15B and exp_001_sft_d025_3B training results\n5. The exp-003 RRF results for 0.5B (exp_003_rrf_05B is DONE)\n6. Any existing dose-response analysis that shows inflation patterns per scale\n\nFocus on finding actual numbers. Report file paths and key metrics.",
    "agentId": "a14e64b8cd2ac948e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now I have comprehensive data. Let me compile my final report with all the key findings:\n\n## Summary Report\n\nBased on my search of the contamcal-irt-calibration project, here are the key findings:\n\n---\n\n### 1. **exp_006_irt_05B_gsm8k Run Status**\n\n**Status: DONE** (Completed 2026-05-14T19:10:34.761Z)\n\n- **Hypothesis**: GSM8K (1319 items, ~5300 params) NUTS feasibility validation\n- **Key Metrics**:\n  - Joint-fit converges (Rhat=1.0081, ESS=956, 0 divergences) ✅\n  - Per-benchmark fails (Rhat=1.5297, ESS=7) ⚠️\n  - N_models: 4, N_items: 1319\n  - Total runtime: 799.3 seconds\n  - Baseline MAE scores: IRT_4pl_gamma=0.0195, B0_raw=0.0034, B3_vanilla_4pl=0.0123\n  \n- **Output**: `/root/autodl-tmp/exp006/results_05B_gsm8k`\n- **Notes**: Joint-fit works, but per-benchmark shows convergence issues. Exposure matrix bug suspected. Code verified and ready for next phase.\n\n---\n\n### 2. **Aligned Eval Results for 1.5B**\n\n#### **d005 (5% dosage) — DONE**\nFile path: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned/`\n- MMLU: 0.5852\n- GSM8K: 0.6482\n- ARC: 0.7688\n- HumanEval: 0.25\n\n#### **d025 (25% dosage) — RUNNING** (eval not trained yet)\n- Training DONE: 3384/3384 steps, loss=1.2715, token_acc=0.7192\n- eval_15B_d025_para_aligned currently RUNNING on GPU 1\n- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter`\n\n#### **d100 (100% dosage) — DONE**\nFile path: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned/`\n- MMLU: 0.5933\n- GSM8K: 0.6497\n- ARC: 0.7688\n- HumanEval: 0.3049\n\n---\n\n### 3. **Aligned Eval Results for 3B**\n\n#### **d025 (25% dosage) — NO SFT/EVAL**\n- No SFT training exists for 3B d025\n- Cannot evaluate without checkpoint\n\n#### **d005 (5% dosage) — DONE**\nFile path: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/`\n- MMLU: 0.634\n- GSM8K: 0.208\n- ARC: 0.829\n- HumanEval: 0.146\n\n---\n\n### 4. **Training Results**\n\n#### **exp_001_sft_d025_15B — DONE**\n- Steps: 3384/3384 (1 epoch)\n- Train loss: 1.2715\n- Mean token accuracy: 0.7192\n- Runtime: 11,610.6 seconds (~3.2 hours)\n- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter`\n\n#### **exp_001_sft_d025_3B — NOT FOUND**\n- No training record in registry for 3B d025\n- Status: Missing / not scheduled\n\n---\n\n### 5. **exp_003_rrf_05B Results (RRF Exposure Ranking)**\n\n**Status: DONE** (Completed 2026-05-14T14:18:05.370Z)\n\n**RRF Exposure Signal Analysis (0.5B, delta vs d000 baseline):**\n\n| Signal | d005 | d100 | Pattern |\n|--------|------|------|---------|\n| **S1 Embedding** | 0.016~0.085 | 0.197~0.379 | ✅ Monotonic (correct direction) |\n| **S2 Min-K++** | -0.20~-0.30 | -0.27~-0.37 | ✅ Correct polarity (negative=more contaminated) |\n| **S4 Self-Critique** | 0.036~0.059 | 0.030~0.075 | ⚠️ Noisy, weak signal |\n\n**Key Finding**: Delta exposure (vs d000 baseline) produces monotonic ranking across dosages. Raw signal averaging misleading; must use delta exposure. S2 polarity must be flipped before RRF fusion.\n\nOutput: `/root/autodl-tmp/exp003/exposure_scores.json`\n\n---\n\n### 6. **Dose-Response Analysis — Inflation Patterns Per Scale**\n\n**Aligned Format Summary (D017 formal analysis):**\n\n| Model | d000 | d005 | d025 | d100 | Trend | Scale Effect |\n|-------|------|------|------|------|-------|--------------|\n| **0.5B MMLU** | 0.3979 | 0.3255 | — | — | ↓18.3% (d005) | **High sensitivity** |\n| **0.5B ARC** | 0.4693 | 0.3285 | — | — | ↓30% (d005) | **High sensitivity** |\n| **0.5B GSM8K** | 0.3692 | 0.3624 | — | — | ↓1.8% (d005) | **Immune** |\n| **1.5B MMLU** | 0.5853 | 0.5852 | — | 0.5933 | ↑0.8% (d100) | **Nearly immune** |\n| **1.5B GSM8K** | 0.6543 | 0.6482 | — | 0.6497 | ↓0.5% (d100) | **Immune** |\n| **3B MMLU** | 0.6340 | 0.634 | — | 0.6417 | ↑1.2% (d005 vs d000) | **Nearly immune** |\n| **3B ARC** | 0.8276 | 0.829 | — | 0.8396 | ↑0.6% (d005 vs d000) | **Immune** |\n| **3B GSM8K** | 0.1198 | 0.208 | — | 0.6967 | ⚠️ Excluded (SFT-degraded per D018) | **Anomalous** |\n\n**Critical Finding**: **Inverse Scale Relationship**\n- **0.5B**: MMLU and ARC highly sensitive to contamination (↓18-30%)\n- **1.5B**: Minimal impact (↓0.5-0.8%, often positive)\n- **3B**: Nearly zero impact (↑0.6-1.2%), sometimes benefits\n\nThis contradicts intuition that larger models should be more robust. Likely explanation: Smaller models memorize contaminated training data more readily (fewer parameters), larger models generalize around it.\n\n---\n\n### 7. **Key Inflation Metric Per Benchmark by Scale**\n\nFrom aligned results and analysis documents:\n\n| Benchmark | 0.5B Inflation (d005) | 1.5B Inflation | 3B Inflation | Pattern |\n|-----------|----------------------|----------------|--------------|---------|\n| **MMLU** | -18.3pp | -0.1pp | +1.2pp | Severe at small scale, reverses at large |\n| **ARC-Challenge** | -30.0pp | -0.3pp | +0.6pp | Most scale-sensitive |\n| **GSM8K** | -1.8pp | -0.5pp | +10.9pp | Immune except 3B (SFT degradation) |\n| **HumanEval** | No data yet | No contamination injection | No contamination injection | Negative control (appendix only) |\n\n---\n\n### 8. **Data Completeness Status**\n\n- **Aligned original evals completed**: 3 cells (0.5B-d000, 1.5B-d000, 1.5B-d100) + 3B-d005, 3B-d100\n- **Running**: exp_001_eval_15B_d025_para_aligned (GPU 1, started 2026-05-14T19:11:06Z)\n- **Missing/Blocked**: 0.5B-d025 aligned, 1.5B-d025 aligned, 3B-d025 (no SFT)\n- **Completion rate**: ~54.2% of aligned matrix after current runs finish\n\n---\n\n### File Paths Summary\n\n- Registry: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml`\n- Dose-response analysis: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dose_response_analysis.md`\n- Eval compilation: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/report_eval_compilation.md`\n- IRT results (exp-006): `/root/autodl-tmp/exp006/results_05B_gsm8k/`\n- RRF exposure scores (exp-003): `/root/autodl-tmp/exp003/exposure_scores.json`"
      }
    ],
    "totalDurationMs": 87439,
    "totalTokens": 79653,
    "totalToolUseCount": 43,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4643,
      "cache_read_input_tokens": 72500,
      "output_tokens": 2504,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4643
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2504,
          "cache_read_input_tokens": 72500,
          "cache_creation_input_tokens": 4643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4643,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 9,
      "searchCount": 3,
      "bashCount": 31,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "dc8b8077-0cfe-40d8-8f42-fc7d96dfc3e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-14T19:26:04.496Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data. Let me synthesize this for the worst-tier predictions.

Key facts from actual data:
1. **0.5B**: Contamination HURTS scores (catastrophic forgetting). MMLU drops 18pp at d005, ARC drops 30pp at d005.
2. **1.5B**: Contamination barely changes anything. MMLU ±0.1pp, ARC ±0.3pp, GSM8K ±0.5pp.
3. **3B**: Contamination barely changes MMLU (+1.2pp) and ARC (+0.6pp). 

GSM8K shows a massive +58pp jump, but this appears to be flagged as an SFT degradation anomaly. Only the embedding-based signal works at 0.5B scale—the other mitigation strategies perform at chance level. I'm also seeing a concerning reversal pattern with Min-K++ (Cohen's d = -1.98 at d100), and the IRT modeling is struggling: the per-benchmark fit has poor convergence diagnostics while the joint fit actually performs worse than the raw data on MAE.

The simulation results look promising in isolation, but they're operating under idealized conditions that don't translate to real data. The RRF approach produces the correct ranking monotonicity but is almost entirely dependent on that single embedding signal.

Looking at the worst-case tier, the core issue is that IRT parameter identification breaks down on real data—at 0.5B, contamination causes forgetting rather than inflation so the model's assumptions fail, while at larger scales the effect is too small to distinguish from noise. Calibration can't outperform simple linear regression because the signal-to-noise ratio is fundamentally poor, coverage suffers from violated independence assumptions and insufficient model diversity, and the alternative signals remain ineffective at 1.5B and 3B scales.

Now I'm reviewing the planned experiments to construct detailed predictions for each one. Let me identify which experiments are actually marked as planned in the experiment plan and work through them systematically.

For exp-002, I need to predict how the detection signals will perform across the 1.5B and 3B model scales. S1 should remain effective since embedding-based retrieval is generally robust, though the AUC might degrade slightly at larger scales due to weaker contamination inflation. S2 and S3 will likely fail or show reversed performance across all scales, which aligns with the pattern I'm seeing in the existing data.

Now I'm drafting the worst-tier narrative and identifying the key failure modes: γ estimation breaks down on real data despite working in simulation, the IRT calibration approach doesn't outperform simpler baselines, and coverage drops below acceptable thresholds due to model misspecification issues.

Looking at the specific evidence, the S2 and S4 metrics fail consistently across all model scales rather than just at 0.5B, the dose-response relationship becomes non-monotonic due to catastrophic forgetting, and cross-family validation doesn't hold up. The RRF approach degrades to only using S1, and the observational RL study produces uninformative confidence intervals.

I'm noticing the exp-006 IRT results on GSM8K are particularly damning—the IRT approach has 5.7x worse MAE than the baseline, which is direct empirical evidence that the core framework doesn't deliver the promised improvements.

The per-benchmark fit also failed to converge with Rhat=1.53, which confirms the convergence difficulties I've been tracking. Now I need to write out the full YAML specification with all planned experiments, expected results with specific metric values, detailed rationales for why these results occur, and the analysis structure. I'm thinking through the specific numbers for each experiment—for exp-002 at 1.5B and 3B scales, S1 embedding similarity should remain high around 0.92-0.96 at d005 since embedding similarity is scale-independent, though the within-model discrimination might be weaker because the inflation signal itself is so small.

At d100 S1 becomes uninformative since all items are contaminated. S2 (Min-K++) should stay near chance at 0.48-0.52 under the worst tier assumption, while S3 (ConStat) would show only marginal improvement to 0.50-0.55 given the tiny inflation gap at smaller scales, and S4 (Self-Critique) would similarly show minimal gains beyond its 0.5B baseline.

For the RRF aggregation ablation, the composite score essentially reduces to S1's performance since the other signals don't meaningfully contribute. Equal-weight averaging actually hurts performance by diluting the one good signal, and even calibration-based weighting converges back to S1 alone as the weights for S2-S4 approach zero. The two-signal mode combining ConStat and Self-Critique yields only 0.50-0.55 AUC, which is essentially useless.

Now looking at the core IRT calibration experiment in the worst tier, I'm examining the MMLU results across the benchmark fitting. The model count is around 12 across the three scales and four dosages, though some conditions are missing, which expands to roughly 24-30 when accounting for different seeds.

Breaking down the actual data: I have 0.5B, 1.5B, and 3B models across various dosages, giving me about 22-33 total models with seeds. But here's the fundamental issue—the contamination pattern doesn't match what the IRT model expects. The 0.5B models actually show MMLU dropping with contamination rather than inflating, so there's no inflation signal for γ to capture. The 1.5B and 3B models barely budge, with changes around ±1pp and +0.8pp respectively, meaning γ stays near zero in practice. The IRT model is trying to estimate a contamination inflation parameter when the actual data shows deflation or stasis.

This creates an identification problem: γ will have a wide posterior that likely includes zero since half the data shows deflation and the other half shows near-zero effects. Looking at individual benchmarks, MMLU and ARC both have posteriors centered near zero with confidence intervals spanning zero, making them unidentifiable. GSM8K shows massive inflation in the 3B scale, so γ might be identified there, but it's driven by a single scale. HumanEval has only 164 items with marginal effects, so it's also unidentifiable. When I compare this to a simple linear regression baseline using the exposure score as a predictor, that approach should work reasonably well since the exposure score is a strong predictor.

The IRT 4PL+γ model performs worse than the linear baseline—MAE around 5-8pp versus 2-4pp for the regression—because it overparameterizes the problem and has convergence issues. The 95% CI coverage falls short at 72-80% due to local independence violations and model misspecification. Ranking preservation is mediocre with Kendall tau around 0.65-0.72 given the small inflation effects and deflation patterns. The dose-response curve is non-monotonic because the 0.5B scale shows catastrophic forgetting where contamination actually produces lower scores, creating about 3-5 monotonicity violations. Now I'm drafting the full YAML with specific numbers for the tables.

I should structure each experiment's results as nested YAML dictionaries. I notice that exp-006 already has partial GSM8K IRT data showing MAE of 1.95pp versus 0.34pp for raw scores, confirming that IRT performs worse in the worst tier. When I scale this across all benchmarks and models, that pattern should persist or intensify. I need to distinguish between observed results and predictions, keeping my projections consistent with what we've already measured. Let me now write out the comprehensive YAML structure. already has 0.5B signal data. The "worst tier" prediction for the full exp-008 would extend this to 1.5B/3B showing continued failure of S2/S4.

Let me write it now. I'll keep the format clean and the rationales thorough.

Let me think about each experiment one more time:

**exp-002 (stage1_signal_pipeline)**:
- Compute signals on all models from exp-001
- Already have 0.5B data
- Need 1.5B and 3B signal computations
- In worst tier: S2/S4 remain at chance for 1.5B/3B, S3 (ConStat) also weak

**exp-003 (rrf_aggregation_ablation)**:
- RRF fusion ablations
- Already have 0.5B RRF
- In worst tier: RRF performs no better than S1, multi-signal fusion provides no advantage

**exp-006 (irt_calibration_and_baselines)**:
- Core IRT fitting plus seven baselines
- Already have one failed attempt on GSM8K at 0.5B
- In worst tier: IRT fails to outperform linear regression with poor coverage

**exp-007 (scale_bridging_7b)**:
- 7B SFT injection experiment
- In worst tier: 7B exhibits the same pattern as 3B with minimal inflation except on GSM8K

**exp-008 (signal_survival_analysis)**:
- Signal × regime AUC heatmap
- Already have 0.5B SFT data
- In worst tier: signals degrade post-RL and remain weak across all scales

**exp-009 (rl_observational_case_study)**:
- RL models case study
- In worst tier: all cases show poor performance

**exp-012 (observational_72b)**:
- 72B observational model
- In worst tier: no ground truth available, wide confidence intervals, results inconclusive

**exp-013 (closed_weight_2signal_mode)**:
- ConStat + Self-Critique only
- In worst tier: both signals fail, making 2-signal mode completely ineffective

**exp-014 (multi_family_validation)**:
- Llama/Pythia family cross-validation
- In worst tier: contamination response differs across families, cross-family γ correlation is low

Now I'm compiling the key signal AUC numbers at d005 to ensure internal consistency across the YAML structure. Now I'm looking at the AUC values across different model scales to verify they align with the worst-case assumption that S2 and S4 should hover around chance level. The pattern holds consistently—S1 shows strong discrimination ability that degrades with scale, while S2 and S4 remain near 0.5 across all sizes. I'm also checking the Cohen's d effect sizes at the d100 threshold, which show S1 with substantial separation that decreases as models scale up, while S2 and S4 have negative or minimal effect sizes.

Now I'm examining the contamination inflation metrics—the difference between d100 and d000 performance—across benchmarks and model sizes. The 1.5B model's HumanEval result is particularly striking: it jumps from 0.128 to 0.3049, suggesting a 17.7 percentage point inflation that's much larger than what I'd expect from the contamination hypothesis alone.

Looking at the IRT calibration results from exp-006, I'm comparing different methods for handling the worst-tier data. The linear regression approach (B4) performs best with a mean absolute error of 4.1, substantially outperforming both the raw scores and the 4-parameter logistic model with gamma correction.

For MMLU specifically, I'm realizing the core issue: the contamination effects vary wildly across model sizes—from -16.5 percentage points at 0.5B to nearly no effect at 3B—which makes fitting a single gamma parameter fundamentally problematic. Linear regression sidesteps this by directly learning the relationship between exposure, raw scores, and clean scores, which better captures the actual pattern in the data. d-c) / (1 + exp(-a(θ - b + γ*exposure)))

The exposure score comes from Stage 1 (S1 primarily). The γ parameter captures how much exposure inflates the probability of getting an item correct.

The problem in worst tier:
- At 0.5B, exposure actually DECREASES accuracy → γ should be negative
- At 1.5B/3B MMLU/ARC, exposure has near-zero effect → γ ≈ 0
- Per-benchmark γ_k: each benchmark gets its own γ, but within a benchmark, different scales have different effects
- The model assumes γ is the same for all models within a benchmark — but 0.5B has deflation and 3B has (slight) inflation!

This is a fundamental model misspecification: the contamination effect depends on model scale, but the IRT model has a single γ per benchmark. When I fit this across different scales, γ̂ becomes some weighted average of effects that actually have opposite signs, making the estimate biased and unreliable. The model can't capture scale-specific contamination responses, so I'd really need γ_{k,s} (per benchmark and per scale) to properly account for this. Now I'm looking at what the predicted worst-tier metrics would be for exp-006. 6.8, ARC=7.2, GSM8K=8.5, mean=7.5
- mae_improvement_vs_best_baseline_pp: -2.1 (IRT worse than linear regression)
- ci_coverage_95pct: 76%
- ci_sharpness_avg_width_pp: 18.2
- kendall_tau: 0.68
- gamma_posterior_ci_excludes_zero_rate: 0.33 (1 of 3 main benchmarks, maybe GSM8K)
- dose_response_monotonicity_violations: 4
- sbc_rank_uniformity_pvalue: 0.003

These are all within the specified worst-tier ranges. Good.

Now I need to write out the full YAML with comprehensive detail, and I should map out the specific sub-results for each benchmark and scale in exp-006 since that's the core experiment. Let me think through what tables each experiment would generate: exp-002 would have signal AUC matrices and Cohen's d comparisons across models, exp-003 would show RRF versus single-signal versus equal-weight results plus the 2-signal closed-weight mode, exp-006 would produce calibration metrics across all methods and benchmarks along with gamma posterior summaries and SBC diagnostics, and exp-007 would document the 7B model contamination effects and signal performance. I'm noticing the actual model counts are lower than planned—the 0.5B and 1.5B scales only have 4 dosages each instead of 5, so I'm working with fewer total models than the original 45. The GSM8K baseline with just 4 models showed IRT performing worse than raw scores, and convergence issues appeared even then, so scaling up won't necessarily fix those problems in the worst-case scenario. Let me finalize the YAML with these constraints in mind. I need to carefully parse what the user is actually asking for—they want me to expand each planned experiment with detailed predictions and include a rationale for every result. The output should be structured as YAML with all the specified fields, and I need to ensure the numbers stay consistent across all the experiments while I write this out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce6ec1f4-9de4-420e-957d-414ab5680ec9",
  "isSidechain": false,
  "requestId": "req_011Cb31PYuzsLHGLTn5HphdR",
  "type": "assistant",
  "uuid": "7e90c8cb-7e55-41e4-b14f-0872ce4df6b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AivApMYkDN2vdFQuaDMwM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2827,
      "cache_read_input_tokens": 38675,
      "output_tokens": 25142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 25142,
          "cache_read_input_tokens": 38675,
          "cache_creation_input_tokens": 2827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2827
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

_source line 17 · 2026-05-14T19:31:54.886Z_

现有数据已收集完毕。基于 0.5B 的实际灾难性遗忘模式、1.5B/3B 的弱膨胀、信号仅 S1 有效的现状、以及 exp-006 GSM8K 已观察到的 IRT MAE > Raw MAE (0.0195 vs 0.0034)，我来生成 worst 档预测。

```yaml
tier: worst
narrative_guidance: >
  核心框架claim不成立：(1) γ在真实数据上因scale-dependent contamination effect方向不一致
  （0.5B deflation vs 1.5B/3B near-zero inflation）导致不可靠估计，per-benchmark γ_k在不同scale上
  表现为不同符号，模型假设的单一γ根本无法捕捉这种异质性；(2) IRT复杂度无回报——线性回归基线
  利用exposure score做简单调整即可达到相当甚至更优的MAE；(3) 仅S1有效+N_models不足30的双重打击
  使得Fisher Information不足以支撑reliable γ estimation。需根本性reframe为
  'When Can We Calibrate Contaminated Benchmarks?'——用identifiability分析和信号characterization
  作为核心贡献，calibration框架降级为informative negative result。

imagined_experiments:

  ########################################################################
  # exp-002: Stage 1 Signal Pipeline (1.5B/3B extension)
  ########################################################################
  - name: "stage1_signal_pipeline"
    plan_id: "exp-002"
    description: >
      在exp-001产出的1.5B和3B全dosage模型上计算4个检测信号。0.5B数据已有(exp_002_signals_05B)。
      Worst档下S2/S4在1.5B/3B依然不起作用，S3(ConStat)因inflation极小而无discriminative power。
    expected_results:
      # S1 Embedding: 仍然有效，因为检测的是train-test overlap而非inflation本身
      S1_d005_auc_15B_mmlu: 0.962
      S1_d005_auc_15B_gsm8k: 0.974
      S1_d005_auc_15B_arc: 0.988
      S1_d005_auc_3B_mmlu: 0.951
      S1_d005_auc_3B_gsm8k: 0.968
      S1_d005_auc_3B_arc: 0.982
      # S2 Min-K++: 在1.5B/3B继续失败，方向性反转在3B更温和但仍存在
      S2_d005_auc_15B_mean: 0.483
      S2_d005_auc_3B_mean: 0.502
      S2_d100_cohens_d_15B_mean: -1.52
      S2_d100_cohens_d_3B_mean: -1.22
      # S3 ConStat: 依赖performance gap，但inflation < 2pp → gap不显著
      S3_d005_auc_15B_mean: 0.518
      S3_d005_auc_3B_mean: 0.531
      # S4 Self-Critique: 轻微改善但仍远低于useful threshold
      S4_d005_auc_15B_mean: 0.494
      S4_d005_auc_3B_mean: 0.519
      # 汇总
      effective_signals_15B: 1
      effective_signals_3B: 1
      signals_with_auc_above_070_across_all_scales: "S1 only"
    result_rationale: >
      S1(embedding similarity)检测的是train-test文本重叠而非模型行为变化，因此与model scale无关，
      在所有scale上保持AUC>0.95。S2(Min-K++)依赖token-level log-likelihood分布偏移来检测
      memorization；但在1.5B/3B上模型capacity足够大，contaminated items不产生显著的
      perplexity下降(因为模型即使没见过也能答对大部分MC题)，导致contaminated与clean items的
      log-likelihood分布高度重叠(AUC≈0.50)。d100反转效应(Cohen's d<0)是因为100%contamination
      使整体perplexity分布shift，Min-K++的rank-based statistic反而把contaminated items排到
      低风险端。S3(ConStat)需要original→paraphrase的performance gap，但1.5B/3B在MMLU/ARC上
      inflation<2pp，gap在item-level noise中被淹没。S4(Self-Critique)需要模型在contaminated
      items上表现出entropy collapse，但1.5B/3B的contamination几乎不改变response distribution。
      总结：所有scale上只有S1可用，"scale-dependent signal effectiveness"这一claim的
      "scale-dependent"部分无法验证——正确描述是"method-specific signal effectiveness"。
    tables:
      - name: "Signal × Scale × Dosage AUC Matrix (item-level, d005)"
        rows:
          - {signal: S1_Embedding, "0.5B": 0.979, "1.5B": 0.962, "3B": 0.951}
          - {signal: S2_MinKPP, "0.5B": 0.465, "1.5B": 0.483, "3B": 0.502}
          - {signal: S3_ConStat, "0.5B": 0.510, "1.5B": 0.518, "3B": 0.531}
          - {signal: S4_SelfCritique, "0.5B": 0.481, "1.5B": 0.494, "3B": 0.519}
      - name: "Cross-model Cohen's d at d100 vs d000"
        rows:
          - {signal: S1_Embedding, "0.5B": 3.60, "1.5B": 2.85, "3B": 2.41}
          - {signal: S2_MinKPP, "0.5B": -1.98, "1.5B": -1.52, "3B": -1.22}
          - {signal: S3_ConStat, "0.5B": 0.32, "1.5B": 0.18, "3B": 0.22}
          - {signal: S4_SelfCritique, "0.5B": 0.45, "1.5B": 0.38, "3B": 0.51}
    figures_description:
      - "Signal AUC heatmap: 4 signals × 3 scales × 3 dosages(d005/d025/d100)。视觉上呈现S1一行全亮(>0.95)，S2-S4三行全暗(~0.50)的极端二分格局。与best/mid档预期的'scale-dependent gradient'形成鲜明对比。"
      - "Min-K++ Cohen's d方向性反转图：3个scale的bar chart，全部为负值(从-1.98到-1.22)，标注cautionary tale for MIA-based detection。"
    analysis: >
      该结果确认"scale-dependent"主张不成立——S2/S4在任何scale上都无discriminative power。
      论文C2 contingency触发：降级为"method-specific signal effectiveness"，RRF讨论移至
      Limitations。S1的单独有效性仍是有价值的发现(AUC>0.95 across scales)，但RRF作为
      "principled multi-signal aggregation"的卖点完全落空——它只是S1的一层wrapper。
      Min-K++反转(Cohen's d=-1.22 to -1.98)作为MIA文献的cautionary tale依然是最强引用
      贡献，且cross-scale一致性(所有scale都反转)增强了这一发现的robustness。

  ########################################################################
  # exp-003: RRF Aggregation Ablation (full)
  ########################################################################
  - name: "rrf_aggregation_ablation"
    plan_id: "exp-003"
    description: >
      RRF融合4个信号为composite exposure score，加上单信号/等权/加权/2-signal等ablation。
      0.5B部分数据已有(exp_003_rrf_05B)。Worst档下RRF ≈ S1，多信号融合无增益。
    expected_results:
      # AUC for composite exposure vs ground truth contamination label
      rrf_4signal_auc_d005_mean: 0.958
      s1_only_auc_d005_mean: 0.964
      rrf_vs_s1_delta: -0.006
      equal_weight_avg_auc_d005_mean: 0.782
      calibration_weighted_rrf_auc_d005_mean: 0.961
      # 2-signal closed-weight mode
      constat_selfcritique_2signal_auc_d005_mean: 0.521
      # False positive robustness
      rrf_auc_at_5pct_fp_injection: 0.949
      rrf_auc_at_10pct_fp_injection: 0.931
      # Cross-scale consistency
      rrf_4signal_auc_range_across_scales: "[0.948, 0.965]"
      s1_only_auc_range_across_scales: "[0.951, 0.979]"
    result_rationale: >
      RRF的rank fusion机制在3/4信号都是noise时退化为dominant signal mode：S1的high-AUC
      ranks(接近完美排序)dominate，S2/S3/S4的random ranks被平均掉但也引入额外噪声。因此
      RRF(0.958)略低于S1-only(0.964)——噪声信号的inclusion是net negative。等权平均更差
      (0.782)因为3个random signals直接稀释S1。Calibration-weighted RRF(0.961)接近S1因为
      weights自动将S2-S4权重压到~0。2-signal closed-weight mode(ConStat+Self-Critique)
      AUC=0.521是灾难性的——两个无效信号的fusion仍然无效，意味着closed-weight model
      calibration完全不可行。FP robustness check显示RRF/S1在5-10% FP注入下AUC下降<3%，
      这是因为S1的基础信号足够强。但这不改变核心问题：multi-signal aggregation的whole point
      (robustness through diversity)在当前条件下无法实现。
    tables:
      - name: "Aggregation Method Comparison (d005, item-level AUC)"
        rows:
          - {method: "RRF (4 signals)", "0.5B": 0.961, "1.5B": 0.955, "3B": 0.948, mean: 0.958}
          - {method: "S1 only", "0.5B": 0.979, "1.5B": 0.962, "3B": 0.951, mean: 0.964}
          - {method: "Equal-weight avg", "0.5B": 0.801, "1.5B": 0.776, "3B": 0.768, mean: 0.782}
          - {method: "Calibration-weighted RRF", "0.5B": 0.975, "1.5B": 0.959, "3B": 0.949, mean: 0.961}
          - {method: "2-signal (S3+S4)", "0.5B": 0.508, "1.5B": 0.519, "3B": 0.537, mean: 0.521}
      - name: "RRF Degradation Under FP Injection"
        rows:
          - {fp_rate: "0%", auc: 0.958}
          - {fp_rate: "5%", auc: 0.949}
          - {fp_rate: "10%", auc: 0.931}
          - {fp_rate: "15%", auc: 0.908}
    figures_description:
      - "Bar chart对比5种aggregation方法的AUC：S1-only与RRF几乎等高，equal-weight显著低于两者，2-signal在chance水平。视觉上传达'multi-signal aggregation = S1 with extra steps'的message。"
    analysis: >
      核心发现：RRF ≤ S1-only。这直接触发Reviewer Concern #18 ('Why not just S1?')和
      #13 ('RRF is just S1?')的defensive response。论文需诚实报告：当前条件下multi-signal
      aggregation无增益，S1-only是实质上的信号来源。RRF的价值被reframe为"extensible architecture
      for future signals"而非当前的性能贡献。2-signal mode的彻底失败(AUC=0.521)意味着
      closed-weight model calibration在Related Work/Future Work中被标记为open problem。
      Meta-circularity argument for training-free aggregation仍然成立但显得academic——
      当只有一个有效信号时，是否需要aggregation framework本身成为问题。

  ########################################################################
  # exp-006: IRT Calibration and Baselines (CORE EXPERIMENT)
  ########################################################################
  - name: "irt_calibration_and_baselines"
    plan_id: "exp-006"
    description: >
      4PL+γ IRT模型拟合+7个baselines对比。Per-benchmark fitting为primary，joint fitting为ablation。
      已有exp_006_irt_05B_gsm8k的失败先例(per-benchmark Rhat=1.53; IRT MAE 0.0195 > Raw MAE 0.0034)。
      Worst档下IRT在所有benchmark上不优于linear regression baseline，coverage严重低于nominal。
    expected_results:
      # N_models实际可用
      n_models_total: 26
      n_models_with_3seeds: 18
      n_models_with_2seeds: 22

      # === MMLU ===
      mmlu_4pl_gamma_mae_pp: 6.8
      mmlu_linear_reg_mae_pp: 3.9
      mmlu_raw_mae_pp: 3.2
      mmlu_vanilla_4pl_mae_pp: 5.4
      mmlu_2pl_gamma_mae_pp: 6.2
      mmlu_remove_rescore_mae_pp: 3.8
      mmlu_dcr_mae_pp: 4.5
      mmlu_emperor_mae_pp: 3.5
      mmlu_gamma_posterior_mean: 0.018
      mmlu_gamma_posterior_95ci: "[-0.14, 0.19]"
      mmlu_gamma_ci_excludes_zero: false
      mmlu_95ci_coverage: 74
      mmlu_ci_width_mean_pp: 19.3
      mmlu_kendall_tau: 0.71
      mmlu_rhat_max: 1.08
      mmlu_ess_min: 142

      # === ARC-Challenge ===
      arc_4pl_gamma_mae_pp: 7.2
      arc_linear_reg_mae_pp: 4.8
      arc_raw_mae_pp: 5.1
      arc_vanilla_4pl_mae_pp: 6.1
      arc_2pl_gamma_mae_pp: 6.9
      arc_remove_rescore_mae_pp: 5.3
      arc_dcr_mae_pp: 5.6
      arc_emperor_mae_pp: 5.0
      arc_gamma_posterior_mean: -0.032
      arc_gamma_posterior_95ci: "[-0.22, 0.16]"
      arc_gamma_ci_excludes_zero: false
      arc_95ci_coverage: 72
      arc_ci_width_mean_pp: 21.5
      arc_kendall_tau: 0.65
      arc_rhat_max: 1.12
      arc_ess_min: 87

      # === GSM8K ===
      gsm8k_4pl_gamma_mae_pp: 8.5
      gsm8k_linear_reg_mae_pp: 6.2
      gsm8k_raw_mae_pp: 12.8
      gsm8k_vanilla_4pl_mae_pp: 10.2
      gsm8k_2pl_gamma_mae_pp: 7.8
      gsm8k_remove_rescore_mae_pp: 9.1
      gsm8k_dcr_mae_pp: 7.4
      gsm8k_emperor_mae_pp: 11.5
      gsm8k_gamma_posterior_mean: 0.31
      gsm8k_gamma_posterior_95ci: "[0.04, 0.62]"
      gsm8k_gamma_ci_excludes_zero: true
      gsm8k_95ci_coverage: 78
      gsm8k_ci_width_mean_pp: 22.8
      gsm8k_kendall_tau: 0.72
      gsm8k_rhat_max: 1.05
      gsm8k_ess_min: 218

      # === HumanEval (appendix) ===
      humaneval_4pl_gamma_mae_pp: 9.1
      humaneval_gamma_ci_excludes_zero: false
      humaneval_rhat_max: 1.18
      humaneval_note: "N_items=164 insufficient for stable 4PL estimation; convergence failure"

      # === 跨benchmark汇总 ===
      mean_mae_contam_cal_pp: 7.5
      mean_mae_improvement_vs_linear_reg_pp: -2.1
      mean_ci_coverage_95pct: 75
      mean_ci_sharpness_avg_width_pp: 21.2
      mean_kendall_tau: 0.69
      gamma_ci_excludes_zero_rate: 0.33
      dose_response_monotonicity_violations: 4
      sbc_rank_uniformity_pvalue: 0.003

      # === Per-benchmark vs Joint fitting ===
      joint_gamma_posterior_mean: 0.052
      joint_gamma_95ci: "[-0.08, 0.20]"
      joint_gamma_ci_excludes_zero: false
      joint_rhat_max: 1.15
      joint_fit_divergent_transitions_pct: 3.2
      per_benchmark_vs_joint_mae_delta: "+1.8pp (joint worse)"

      # === θ-γ posterior correlation ===
      theta_gamma_posterior_corr_mmlu: 0.58
      theta_gamma_posterior_corr_arc: 0.72
      theta_gamma_posterior_corr_gsm8k: 0.41

      # === Oracle-γ ablation ===
      oracle_gamma_mae_mmlu_pp: 1.2
      oracle_gamma_mae_arc_pp: 2.1
      oracle_gamma_mae_gsm8k_pp: 3.4
      oracle_vs_estimated_gamma_gap: "4.2pp mean — estimation noise dominates calibration error"

      # === SBC diagnostic ===
      sbc_gamma_rank_uniformity_pvalue: 0.003
      sbc_theta_rank_uniformity_pvalue: 0.018
      sbc_diagnosis: "systematic over-concentration near 0.5 → model underestimates posterior width"
      sbc_n_models_at_actual: 26
      sbc_coverage_gap_attribution: "60% local independence violation, 25% N insufficient, 15% model misspecification"

    result_rationale: >
      IRT校准在worst档下失败的根本原因是scale-dependent contamination effect direction inconsistency
      与模型假设的根本冲突。具体而言：

      MMLU: 0.5B的contamination产生-16.5pp deflation(catastrophic forgetting)，1.5B/3B产生
      +0.8pp near-zero inflation。IRT模型假设γ×exposure的效应方向一致(contamination=inflation)，
      但真实数据中0.5B的方向相反。Per-benchmark fitting估计的γ̂是deflation和near-zero的某种
      加权平均→γ̂≈0.018(接近零)，95% CI宽泛且包含零。校准后的counterfactual(exposure=0)
      与raw score几乎无差异，但IRT的4PL item parameters estimation在N=26下不稳定(ESS低、
      部分Rhat>1.05)，引入额外噪声，导致MAE=6.8pp远高于直接用raw scores(3.2pp)或
      linear regression(3.9pp)。线性回归无需估计数千个item parameters，只需简单拟合
      clean_score ~ exposure + raw_score，因此更稳定。

      ARC: 同样的pattern——0.5B deflation(-17.5pp)与3B near-zero inflation(+1.2pp)方向不一致。
      γ̂为负值(-0.032)且CI包含零。θ-γ posterior correlation=0.72(接近严重混淆的0.7阈值)，
      说明模型无法区分"高能力模型"与"低contamination模型"。ARC的Rhat=1.12表明convergence
      marginal，ESS=87偏低。

      GSM8K: 唯一γ CI excludes zero的benchmark——3B的+57.7pp massive inflation提供了
      strong contamination signal。但0.5B和1.5B的near-zero effect仍然拖累估计。MAE=8.5pp
      虽然好于raw(12.8pp)，但仍不如linear regression(6.2pp)和DCR(7.4pp)。问题是GSM8K的
      inflation pattern极端非线性(3B爆炸式增长而0.5B/1.5B几乎不变)，IRT的线性γ×exposure
      无法捕捉这种scale-conditional effect。

      HumanEval: N_items=164对4PL的thousands of parameters严重不足，convergence failure(Rhat=1.18)。

      Coverage问题(75% vs 95% nominal)：SBC诊断显示rank histogram系统性over-concentrated
      near 0.5，表明posterior width被低估。原因分解：(1)local independence violation——
      single model responds to all items，item responses correlated through shared θ，
      这种correlation被model忽略导致posterior artificially narrow；(2)N=26 models insufficient
      for reliable posterior estimation with数千个nuisance parameters(a,b,c,d per item)；
      (3)γ的scale-dependent effect direction misspecified。三者叠加导致20pp coverage gap。

      Oracle-γ ablation(直接使用true contamination label)shows MAE可降到1.2-3.4pp，
      证明IRT框架理论上可行，但γ estimation noise贡献了~4.2pp的额外error——
      在当前信号质量和N下，estimation noise dominates。

      Dose-response monotonicity: 0.5B的deflation pattern导致4个violations(d005&lt;d000在0.5B、
      d025&lt;d005在0.5B、以及1.5B/3B的near-zero-with-noise fluctuations)。

    tables:
      - name: "Calibration MAE (pp) by Method × Benchmark"
        rows:
          - {method: "B0: Raw (no adjustment)", MMLU: 3.2, ARC: 5.1, GSM8K: 12.8, HumanEval: 4.8, mean: 6.5}
          - {method: "B1: Remove-and-rescore", MMLU: 3.8, ARC: 5.3, GSM8K: 9.1, HumanEval: 5.2, mean: 5.9}
          - {method: "B2: 2PL+γ (S1 only)", MMLU: 6.2, ARC: 6.9, GSM8K: 7.8, HumanEval: 8.5, mean: 7.4}
          - {method: "B3: Vanilla 4PL (no γ)", MMLU: 5.4, ARC: 6.1, GSM8K: 10.2, HumanEval: 7.3, mean: 7.3}
          - {method: "B4: Linear regression + bootstrap CI", MMLU: 3.9, ARC: 4.8, GSM8K: 6.2, HumanEval: 4.1, mean: 4.8}
          - {method: "B5: Emperor's mitigation", MMLU: 3.5, ARC: 5.0, GSM8K: 11.5, HumanEval: 4.5, mean: 6.1}
          - {method: "B6: DCR fuzzy inference", MMLU: 4.5, ARC: 5.6, GSM8K: 7.4, HumanEval: 5.8, mean: 5.8}
          - {method: "4PL+γ (ours, per-benchmark)", MMLU: 6.8, ARC: 7.2, GSM8K: 8.5, HumanEval: 9.1, mean: 7.9}
          - {method: "4PL+γ (ours, joint)", MMLU: 7.5, ARC: 8.1, GSM8K: 9.2, HumanEval: 10.3, mean: 8.8}
          - {method: "4PL+γ (oracle γ)", MMLU: 1.2, ARC: 2.1, GSM8K: 3.4, HumanEval: 2.8, mean: 2.4}
      - name: "Coverage and Sharpness (per-benchmark fit)"
        rows:
          - {benchmark: MMLU, "50% cov": 38, "80% cov": 59, "95% cov": 74, "95% CI width (pp)": 19.3}
          - {benchmark: ARC, "50% cov": 35, "80% cov": 55, "95% cov": 72, "95% CI width (pp)": 21.5}
          - {benchmark: GSM8K, "50% cov": 42, "80% cov": 64, "95% cov": 78, "95% CI width (pp)": 22.8}
          - {benchmark: HumanEval, "50% cov": 28, "80% cov": 48, "95% cov": 65, "95% CI width (pp)": 24.1}
      - name: "γ Posterior Summary by Benchmark"
        rows:
          - {benchmark: MMLU, gamma_mean: 0.018, gamma_95ci: "[-0.14, 0.19]", excludes_zero: false, theta_gamma_corr: 0.58, rhat: 1.08}
          - {benchmark: ARC, gamma_mean: -0.032, gamma_95ci: "[-0.22, 0.16]", excludes_zero: false, theta_gamma_corr: 0.72, rhat: 1.12}
          - {benchmark: GSM8K, gamma_mean: 0.31, gamma_95ci: "[0.04, 0.62]", excludes_zero: true, theta_gamma_corr: 0.41, rhat: 1.05}
          - {benchmark: HumanEval, gamma_mean: 0.08, gamma_95ci: "[-0.35, 0.52]", excludes_zero: false, theta_gamma_corr: 0.63, rhat: 1.18}
      - name: "SBC Diagnostic Summary"
        rows:
          - {parameter: gamma, rank_uniformity_pvalue: 0.003, diagnosis: "over-concentrated → posterior too narrow"}
          - {parameter: theta, rank_uniformity_pvalue: 0.018, diagnosis: "mild over-concentration"}
          - {parameter: item_a, rank_uniformity_pvalue: 0.142, diagnosis: "acceptable"}
          - {parameter: item_b, rank_uniformity_pvalue: 0.067, diagnosis: "marginal"}
    figures_description:
      - "Calibrated vs True accuracy scatter plot: 点高度散布在对角线两侧，95% CI error bars宽到12-25pp且许多不覆盖true value。与linear regression的tighter scatter形成对比。GSM8K 3B是唯一靠近对角线的outlier cluster。"
      - "Dose-response curve: 0.5B的曲线向下(deflation)，1.5B/3B的曲线近乎水平(near-zero effect)。仅3B GSM8K有明显上升趋势。4个monotonicity violations用红叉标记。"
      - "SBC rank histogram: γ的histogram明显tent-shaped(中间高两端低)，偏离uniform分布。p=0.003的K-S test结果标注。"
      - "Oracle vs Estimated γ ablation bar chart: oracle-γ MAE(2.4pp)远低于estimated-γ(7.9pp)，差距5.5pp全部来自γ estimation error。"
    analysis: >
      exp-006是worst档下最critical的negative result。核心发现：(1)4PL+γ IRT在所有benchmark上
      MAE劣于linear regression baseline(7.9pp vs 4.8pp mean)，IRT的额外复杂度(数千item
      parameters)在N=26 models下导致overfitting而非better calibration；(2)γ CI仅在1/3
      benchmark(GSM8K)excludes zero，且GSM8K的γ identification主要由3B的anomalous +58pp
      inflation驱动——去掉3B后GSM8K γ也不显著；(3)θ-γ correlation在ARC达0.72，接近严重混淆
      阈值；(4)coverage gap达20pp(75% actual vs 95% nominal)，SBC确认是系统性model
      misspecification而非random variation。

      但oracle-γ ablation(MAE=2.4pp)证明IRT框架theoretically sound——failure source是
      γ estimation而非IRT本身。这为reframed paper提供关键narrative：'γ identification requires
      conditions not met in current setup(stronger signals, more models, scale-homogeneous
      effects)'——用Fisher Info identifiability分析理论解释failure boundary。

      论文positioning：calibration results reported as 'informative negative result' with
      identifiability analysis explaining WHY it fails and WHAT conditions would make it work。
      Linear regression baseline becomes the pragmatic recommendation。

  ########################################################################
  # exp-007: Scale Bridging 7B
  ########################################################################
  - name: "scale_bridging_7b"
    plan_id: "exp-007"
    description: >
      Qwen2.5-7B在5个dosage levels的controlled SFT injection。验证calibration是否
      scales to larger models。Worst档下7B延续3B的pattern——weak inflation使calibration无从着手。
    expected_results:
      # 7B contamination effects (d100 - d000)
      mmlu_d000_accuracy: 0.712
      mmlu_d100_accuracy: 0.727
      mmlu_inflation_pp: 1.5
      arc_d000_accuracy: 0.878
      arc_d100_accuracy: 0.898
      arc_inflation_pp: 2.0
      gsm8k_d000_accuracy: 0.782
      gsm8k_d100_accuracy: 0.817
      gsm8k_inflation_pp: 3.5
      humaneval_d000_pass1: 0.305
      humaneval_d100_pass1: 0.354
      humaneval_inflation_pp: 4.9
      # Dose-response
      mmlu_dose_response_monotonic: false
      arc_dose_response_monotonic: true
      gsm8k_dose_response_monotonic: true
      # Signal effectiveness at 7B
      S1_d005_auc_7B_mean: 0.948
      S2_d005_auc_7B_mean: 0.511
      S4_d005_auc_7B_mean: 0.528
      # IRT calibration at 7B (if included in full model)
      mmlu_4pl_gamma_mae_with_7B_pp: 6.5
      note: "Adding 7B doesn't substantially change calibration because inflation is still weak"
    result_rationale: >
      7B延续1.5B/3B的趋势：model capacity进一步增大使contamination的marginal effect继续缩小。
      MMLU inflation仅+1.5pp(7B已经在pre-training中见过大量knowledge→SFT contamination的
      incremental effect minimal)。ARC和GSM8K有slightly larger inflation(+2.0pp, +3.5pp)但仍
      远小于IRT可靠检测的threshold。MMLU dose-response非单调的原因：d005的SFT额外数据量太少(
      ~700 items)，noise dominates signal，7B在d005可能比d000略低(SFT data distribution shift)。
      S2/S4在7B依然无效(AUC~0.51-0.53)——larger models的log-likelihood distribution更smooth，
      Min-K++的token-level statistic更难区分contaminated items。
      加入7B到IRT fitting只增加~4个data points(d000/d005/d025/d100)，
      且inflation pattern consistent with existing 1.5B/3B(weak)→不改变γ estimate。
    tables:
      - name: "7B Contamination Effect (Accuracy)"
        rows:
          - {benchmark: MMLU, d000: 0.712, d005: 0.710, d025: 0.718, d050: 0.721, d100: 0.727}
          - {benchmark: ARC, d000: 0.878, d005: 0.880, d025: 0.886, d050: 0.891, d100: 0.898}
          - {benchmark: GSM8K, d000: 0.782, d005: 0.789, d025: 0.795, d050: 0.806, d100: 0.817}
          - {benchmark: HumanEval, d000: 0.305, d005: 0.312, d025: 0.328, d050: 0.341, d100: 0.354}
    figures_description:
      - "7B dose-response curves叠加在0.5B/1.5B/3B曲线上：7B线几乎水平(slope~0.015pp/dosage-pct)，与0.5B的下降线和3B GSM8K的陡升线形成对比。视觉上reinforces'calibration target too weak'的narrative。"
    analysis: >
      7B数据进一步确认worst档pattern：随着scale增大，contamination inflation趋于zero。这对
      framework是existential threat——如果larger models(也是评估中最受关注的models)的contamination
      effect太小以至于不需要calibration，那么framework的practical relevance仅限于small models
      (哪里contamination反而是destructive的)。这个insight本身对reframed paper有价值——
      'contamination calibration is most needed where it's hardest(small scale=destructive effect)
      and least needed where it's easiest(large scale=negligible effect)'。

  ########################################################################
  # exp-008: Signal Survival Analysis (1.5B/3B/RL extension)
  ########################################################################
  - name: "signal_survival_analysis"
    plan_id: "exp-008"
    description: >
      检测信号在不同training regime下的可靠性系统评估。0.5B SFT数据已有(exp_008_signal_survival_v4)。
      Worst档：signals在1.5B/3B SFT上无改善，RL-post-trained模型上进一步退化。
    expected_results:
      # SFT regime (extending 0.5B results to 1.5B/3B)
      S1_sft_contaminated_auc_mean_15B: 0.962
      S1_sft_contaminated_auc_mean_3B: 0.951
      S2_sft_contaminated_auc_mean_15B: 0.483
      S2_sft_contaminated_auc_mean_3B: 0.502
      S4_sft_contaminated_auc_mean_15B: 0.494
      S4_sft_contaminated_auc_mean_3B: 0.519
      # RL proxy (Instruct models)
      S1_instruct_auc_mean: 0.891
      S2_instruct_auc_mean: 0.478
      S4_instruct_auc_mean: 0.534
      S1_instruct_vs_sft_delta: -0.071
      # Cross-regime survival rate (AUC > 0.70)
      S1_survives_sft: true
      S1_survives_rl_proxy: true
      S2_survives_any: false
      S3_survives_any: false
      S4_survives_any: false
      overall_signals_surviving_all_regimes: 1
      # Min-K++ reversal consistency
      S2_reversal_at_15B: true
      S2_reversal_at_3B: true
      S2_reversal_cohens_d_range: "[-2.67, -1.22]"
    result_rationale: >
      SFT regime的1.5B/3B结果直接继承exp-002的signal computation——scale上S2/S4保持无效。
      RL proxy(Instruct models)下S1 AUC从~0.96降至~0.89：RL fine-tuning改变了model的
      embedding representation space，使embedding-based similarity的train-test matching变得
      less precise(但仍>0.70因为semantic similarity is relatively robust to fine-tuning)。
      S2(Min-K++)在RL下更差(0.478)因为RLHF改变了token-level likelihood distribution，
      进一步扰乱Min-K++的基于perplexity的detection mechanism。S4(Self-Critique)在RL下
      有marginal improvement(0.534 vs 0.494-0.519)因为Instruct models更善于self-evaluation，
      但仍远低于useful threshold。

      Min-K++反转在所有scale上一致(-1.22 to -2.67 Cohen's d)，且在RL proxy下也存在——
      这是一个robust empirical finding，independent of scale and regime。
    tables:
      - name: "Signal × Regime × Scale AUC Heatmap Data"
        rows:
          - {signal: S1, regime: "SFT-clean", "0.5B": 0.504, "1.5B": 0.508, "3B": 0.512}
          - {signal: S1, regime: "SFT-contam (d005)", "0.5B": 0.979, "1.5B": 0.962, "3B": 0.951}
          - {signal: S1, regime: "Instruct (RL proxy)", "0.5B": 0.882, "1.5B": 0.895, "3B": 0.897}
          - {signal: S2, regime: "SFT-clean", "0.5B": 0.501, "1.5B": 0.498, "3B": 0.503}
          - {signal: S2, regime: "SFT-contam (d005)", "0.5B": 0.465, "1.5B": 0.483, "3B": 0.502}
          - {signal: S2, regime: "Instruct (RL proxy)", "0.5B": 0.472, "1.5B": 0.481, "3B": 0.482}
          - {signal: S4, regime: "SFT-clean", "0.5B": 0.498, "1.5B": 0.502, "3B": 0.505}
          - {signal: S4, regime: "SFT-contam (d005)", "0.5B": 0.481, "1.5B": 0.494, "3B": 0.519}
          - {signal: S4, regime: "Instruct (RL proxy)", "0.5B": 0.522, "1.5B": 0.538, "3B": 0.541}
    figures_description:
      - "4×3×3 AUC heatmap(signal × regime × scale)：S1行从左到右略有降低(SFT 0.97→RL 0.89)但始终在绿色区(>0.70)。S2/S4行全部在红色区(0.45-0.55)。视觉上极其明显的'only S1 works'pattern。"
      - "Min-K++ Cohen's d反转图：across所有scale和regime，bar全为负值。3D bar chart or grouped bar chart展示一致性。"
    analysis: >
      Signal survival analysis确认worst档的核心问题：信号diversity不存在。Paper的Core Contribution #2
      ('signal effectiveness characterization')的价值不在于发现'scale-dependent gradation'
      (这不成立)，而在于诚实记录'only embedding similarity survives across all conditions'。
      Min-K++反转作为MIA cautionary tale的citation value不受影响——反而cross-scale/cross-regime
      一致性使发现更robust。RL proxy下S1的~7pp AUC drop值得关注：如果RL training更aggressive
      (e.g., longer RL)，S1可能也会退化到<0.70threshold以下，这是未来工作的重要方向。

  ########################################################################
  # exp-009: RL Observational Case Study
  ########################################################################
  - name: "rl_observational_case_study"
    plan_id: "exp-009"
    description: >
      对existing RL-trained models(Qwen2.5-Instruct, DeepSeek-R1-Distill)应用ContamCal pipeline。
      Worst档：CIs极宽，expected regret分析无informative结论。
    expected_results:
      # Signal quality on RL models
      S1_auc_qwen_instruct_mean: 0.891
      S1_auc_deepseek_r1_distill_mean: 0.862
      S2_auc_rl_models_mean: 0.479
      S4_auc_rl_models_mean: 0.536
      # IRT calibration on RL models
      rl_gamma_posterior_mean: 0.08
      rl_gamma_95ci: "[-0.31, 0.48]"
      rl_gamma_ci_excludes_zero: false
      rl_95ci_coverage: 68
      rl_ci_width_mean_pp: 24.8
      # Expected regret analysis
      top5_uncalibrated_vs_calibrated_rank_changes: 0
      expected_regret_uncalibrated_pp: 2.1
      expected_regret_calibrated_pp: 2.4
      expected_regret_remove_rescore_pp: 1.8
      regret_conclusion: "calibration does not reduce expected regret; CIs too wide to be actionable"
      # Specificity check (known-clean benchmark)
      known_clean_gamma_mean: 0.04
      known_clean_gamma_95ci: "[-0.18, 0.27]"
      known_clean_gamma_near_zero: true
      specificity_passes: true
    result_rationale: >
      RL models的observational study面临三重困难：(1)没有ground truth clean scores——无法计算
      MAE，只能做internal consistency checks和regret analysis；(2)signal quality进一步降低——
      S1在RL models上AUC=0.86-0.89(vs SFT的0.95+)，因为RL改变了embedding space；
      (3)N_models更少——仅6-8个models(不同scale的Instruct和R1-Distill variants)。

      这三个问题叠加导致γ posterior极宽(CI=[-0.31, 0.48])，无法区分"有contamination"和
      "无contamination"。Expected regret analysis显示calibrated ranking与uncalibrated ranking
      几乎相同(0 rank changes in top-5)——不是因为calibration做得好，而是因为CIs太宽，
      calibrated scores本质上是uncalibrated scores加了大量noise。
      Remove-and-rescore的regret反而最低(1.8pp)因为它简单地丢弃flagged items，不需要估计γ。

      Specificity check passes(known-clean benchmark的γ≈0)——这是一个small positive，
      表明模型不会在clean data上hallucinate contamination effect。但这只说明false positive
      rate低，不说明true positive rate高。
    tables:
      - name: "RL Models Calibration Summary"
        rows:
          - {model: "Qwen2.5-0.5B-Instruct", S1_auc: 0.882, gamma_mean: 0.12, gamma_ci: "[-0.25, 0.51]", ci_width_pp: 26.3}
          - {model: "Qwen2.5-1.5B-Instruct", S1_auc: 0.895, gamma_mean: 0.07, gamma_ci: "[-0.28, 0.43]", ci_width_pp: 23.8}
          - {model: "Qwen2.5-3B-Instruct", S1_auc: 0.897, gamma_mean: 0.05, gamma_ci: "[-0.32, 0.41]", ci_width_pp: 24.1}
          - {model: "Qwen2.5-7B-Instruct", S1_auc: 0.901, gamma_mean: 0.03, gamma_ci: "[-0.29, 0.35]", ci_width_pp: 22.4}
          - {model: "DeepSeek-R1-Distill-1.5B", S1_auc: 0.858, gamma_mean: 0.14, gamma_ci: "[-0.34, 0.62]", ci_width_pp: 28.1}
          - {model: "DeepSeek-R1-Distill-7B", S1_auc: 0.866, gamma_mean: 0.09, gamma_ci: "[-0.30, 0.49]", ci_width_pp: 25.7}
      - name: "Expected Regret Comparison (top-5 model selection)"
        rows:
          - {method: "Uncalibrated", regret_pp: 2.1, rank_changes_vs_oracle: 1}
          - {method: "4PL+γ calibrated", regret_pp: 2.4, rank_changes_vs_oracle: 1}
          - {method: "Remove-and-rescore", regret_pp: 1.8, rank_changes_vs_oracle: 0}
    figures_description:
      - "RL models的calibrated score forest plot：每个model一行，point estimate + 95% CI bar。CI bars全部overlap，无法区分任何pair of models。与controlled SFT models的tighter CIs(如果有的话)形成对比。"
    analysis: >
      RL observational study确认worst档预期：calibration在RL regime下uninformative。
      但specificity check(clean benchmark γ≈0)至少表明框架不会produce harmful false positives。
      论文中frame为'current signal quality insufficient for RL models, but framework correctly
      expresses this uncertainty through wide CIs'——honest UQ rather than overconfident
      wrong answers。DeepSeek-R1-Distill的S1 AUC更低(0.86 vs 0.89)可能因为distillation
      进一步distorted embedding space。这motivates future work on RL-robust signals。

  ########################################################################
  # exp-012: Observational 72B
  ########################################################################
  - name: "observational_72b"
    plan_id: "exp-012"
    description: >
      Qwen2.5-72B inference-only observational分析。Worst档：无ground truth，CIs宽，
      结论完全inconclusive。
    expected_results:
      S1_auc_72B: 0.938
      S2_auc_72B: 0.508
      S4_auc_72B: 0.542
      gamma_mean: 0.02
      gamma_95ci: "[-0.41, 0.45]"
      gamma_ci_excludes_zero: false
      ci_width_pp: 28.5
      calibrated_vs_raw_delta_pp: 0.4
      note: "Single model, no ground truth — purely qualitative"
    result_rationale: >
      72B的observational analysis面临最严峻的identifiability challenge：(1)单个model→N_models=1，
      IRT无法fit(需要至少~20 models)。只能做per-item exposure scoring和descriptive analysis。
      (2)无ground truth→MAE不可计算。(3)72B在所有benchmark上accuracy已接近ceiling(MMLU~0.83,
      ARC~0.94)→即使有contamination，其marginal inflation effect更小(ceiling compression)。
      γ estimate来自在controlled models上fitted model的extrapolation到72B——
      但72B的θ远超training range，extrapolation unreliable。CI width=28.5pp使结果
      完全uninformative。Calibrated score与raw score差距仅0.4pp，在noise中不可检测。
    tables:
      - name: "72B Observational Summary (inference only)"
        rows:
          - {benchmark: MMLU, raw_acc: 0.831, calibrated_acc: 0.827, delta_pp: -0.4, ci_width_pp: 27.1}
          - {benchmark: ARC, raw_acc: 0.941, calibrated_acc: 0.938, delta_pp: -0.3, ci_width_pp: 22.8}
          - {benchmark: GSM8K, raw_acc: 0.892, calibrated_acc: 0.885, delta_pp: -0.7, ci_width_pp: 31.4}
          - {benchmark: HumanEval, raw_acc: 0.793, calibrated_acc: 0.788, delta_pp: -0.5, ci_width_pp: 32.8}
    figures_description:
      - "72B单点在calibrated-vs-true scatter中的位置：一个点，巨大的error bar(±14pp)，完全uninformative。用来illustrate'为什么single-model observational analysis不足以validate calibration'。"
    analysis: >
      72B分析在worst档下几乎无信息价值。唯一可用的finding是exposure score分布的descriptive
      statistics——哪些benchmark items在72B上有高S1 exposure scores。但这只是signal characterization，
      不是calibration。论文中作为1-2段discussion item处理，frame为'ecological validity extension
      requires multi-model observational study design'。不在main results中占位。

  ########################################################################
  # exp-013: Closed-weight 2-Signal Mode
  ########################################################################
  - name: "closed_weight_2signal_mode"
    plan_id: "exp-013"
    description: >
      仅ConStat + Self-Critique(无logits/embeddings)的degraded 2-signal mode。
      Worst档：两个信号都在chance水平→closed-weight calibration完全不可行。
    expected_results:
      constat_auc_mean_across_scales: 0.524
      selfcritique_auc_mean_across_scales: 0.511
      rrf_2signal_auc_mean: 0.521
      mae_2signal_vs_4signal_gap_pp: 5.8
      mae_2signal_calibration_pp: 13.7
      mae_raw_pp: 6.5
      note: "2-signal calibration WORSE than doing nothing (raw scores)"
      coverage_2signal_95pct: 58
      ci_width_2signal_pp: 32.4
    result_rationale: >
      ConStat(AUC~0.52)和Self-Critique(AUC~0.51)都接近random chance。两个random signals的
      RRF fusion仍然是random(AUC=0.521)。基于这种noise exposure score做IRT calibration
      不仅不帮助，还actively harmful——γ估计受random exposure scores驱动，产生spurious
      corrections，MAE=13.7pp远高于raw scores(6.5pp)。Coverage仅58%(95% nominal)因为
      CI既宽(32.4pp)又biased(wrong γ direction on some models)。

      这个结果有clear practical implication：closed-weight model evaluation(GPT-4, Claude等)
      目前不可能做contamination calibration，因为available signals(无logits)完全无效。
    tables:
      - name: "2-Signal vs 4-Signal Calibration Comparison"
        rows:
          - {metric: "Exposure AUC", "4-signal": 0.958, "2-signal": 0.521, "S1-only": 0.964}
          - {metric: "MAE (pp)", "4-signal": 7.9, "2-signal": 13.7, "S1-only": 7.5}
          - {metric: "95% Coverage", "4-signal": 75, "2-signal": 58, "S1-only": 76}
          - {metric: "CI Width (pp)", "4-signal": 21.2, "2-signal": 32.4, "S1-only": 20.8}
    figures_description:
      - "2-signal vs 4-signal comparison bar chart：MAE/coverage/sharpness三个metric上2-signal全面崩溃。附注'raw scores outperform 2-signal calibration'。"
    analysis: >
      Closed-weight calibration不可行是worst档下的strong negative result。论文中不应隐瞒——
      在Limitations中明确指出'ContamCal requires embedding access(open-weight models)'。
      这限制了framework的practical applicability到open-weight models only。在reframed paper中，
      这成为'identifiability boundary'的另一个dimension：不仅需要AUC≥0.70和N≥30，
      还需要embedding access。

  ########################################################################
  # exp-014: Multi-family Validation
  ########################################################################
  - name: "multi_family_validation"
    plan_id: "exp-014"
    description: >
      Llama-3.2-1B或Pythia-1.4B在3个dosage levels的controlled SFT injection。
      Worst档：cross-family contamination response pattern截然不同，γ estimates不transferable。
    expected_results:
      # Llama-3.2-1B contamination effects
      llama_mmlu_d000: 0.312
      llama_mmlu_d100: 0.285
      llama_mmlu_inflation_pp: -2.7
      llama_arc_d000: 0.398
      llama_arc_d100: 0.361
      llama_arc_inflation_pp: -3.7
      llama_gsm8k_d000: 0.182
      llama_gsm8k_d100: 0.201
      llama_gsm8k_inflation_pp: 1.9
      # Cross-family γ comparison
      gamma_cross_family_correlation: 0.31
      gamma_qwen_mmlu: 0.018
      gamma_llama_mmlu: -0.085
      gamma_agreement_direction: false
      # Signal transfer
      S1_llama_auc_d005: 0.941
      S2_llama_auc_d005: 0.472
      S4_llama_auc_d005: 0.488
    result_rationale: >
      Llama-3.2-1B(~1B parameters)在contamination response上类似Qwen2.5-0.5B而非1.5B——
      因为absolute model capacity而非parameter count决定contamination effect direction。
      1B-class models普遍suffer from catastrophic forgetting when SFT data includes benchmark items
      (SFT data分布偏移干扰模型原有knowledge)。MMLU和ARC都出现deflation(-2.7pp, -3.7pp)，
      与Qwen2.5-0.5B的pattern一致。

      Cross-family γ correlation仅0.31(远低于paper_framing中期望的r=0.91)——这直接否定了
      'contamination susceptibility is a benchmark property'的claim。γ differences across families
      reflect不同的architecture/pretraining data/tokenizer导致的不同contamination response patterns。
      Qwen和Llama在同一benchmark上甚至γ方向都不一致(Qwen MMLU γ>0 vs Llama MMLU γ<0)。

      S1 AUC在Llama上依然高(0.941)——embedding similarity是model-agnostic的。S2/S4继续失败。
    tables:
      - name: "Cross-family Contamination Effect Comparison"
        rows:
          - {family: "Qwen2.5-0.5B", MMLU_delta: -16.5, ARC_delta: -17.5, GSM8K_delta: -0.4}
          - {family: "Qwen2.5-1.5B", MMLU_delta: +0.8, ARC_delta: -0.3, GSM8K_delta: -0.5}
          - {family: "Qwen2.5-3B", MMLU_delta: +0.8, ARC_delta: +1.2, GSM8K_delta: +57.7}
          - {family: "Llama-3.2-1B", MMLU_delta: -2.7, ARC_delta: -3.7, GSM8K_delta: +1.9}
      - name: "Cross-family γ Estimates"
        rows:
          - {benchmark: MMLU, qwen_gamma: 0.018, llama_gamma: -0.085, correlation: 0.31}
          - {benchmark: ARC, qwen_gamma: -0.032, llama_gamma: -0.112, correlation: 0.58}
          - {benchmark: GSM8K, qwen_gamma: 0.310, llama_gamma: 0.065, correlation: 0.22}
    figures_description:
      - "Cross-family dose-response curves并列：Qwen vs Llama在同一benchmark上方向不同(MMLU)或magnitude差异大(GSM8K)。Shaded areas表示within-family variation vs between-family variation。"
    analysis: >
      Multi-family validation失败是worst档的predicted outcome但也是valuable negative result。
      它证明contamination effect is NOT a benchmark property——it's a benchmark × model family
      interaction。这从根本上限制了framework的generalizability：在Qwen上trained的γ estimates
      不能transfer到Llama/Pythia。论文需要在Limitations中明确说明'current framework requires
      per-family calibration'。

      对reframed paper的影响：(1) per-benchmark γ_k heterogeneity的cross-family r=0.91 claim
      完全放弃；(2)Identifiability分析需要增加'family-specific'维度——每个model family都需要
      独立的N≥30和AUC≥0.70；(3)作为rebuttal experiment的价值反而增加——诚实报告cross-family
      failure比假装成功更有说服力。

  ########################################################################
  # exp-004 (DONE/failed, but v2 RUNNING — predict final outcome)
  ########################################################################
  - name: "simulation_identifiability_sweep_v2_final"
    plan_id: "exp-004"
    description: >
      144-condition simulation sweep的最终结果(v2 currently RUNNING, 48/120 complete)。
      Worst档下模拟在idealized conditions下works，但gap to real data conditions不可弥合。
    expected_results:
      # Idealized simulation results (these actually look good)
      auc055_n20_gamma_rmse: 0.040
      auc055_n50_gamma_rmse: 0.026
      auc055_n100_gamma_rmse: 0.013
      auc080_n20_gamma_rmse: 0.035
      auc080_n50_gamma_rmse: 0.018
      auc080_n100_gamma_rmse: 0.008
      structural_identifiability_threshold_auc: 0.55
      practical_identifiability_threshold_auc: 0.70
      practical_identifiability_threshold_n: 50
      # Coverage in simulation
      sim_95ci_coverage_auc080_n50: 94
      sim_95ci_coverage_auc055_n20: 82
      # Fisher Information analysis
      fisher_info_gamma_theoretical: "I(γ) ∝ N × (AUC - 0.5)² / σ²_exposure"
      fisher_info_minimum_auc_for_10pct_precision: 0.72
      # Gap to real data
      real_data_effective_auc: 0.96
      real_data_effective_n: 26
      real_data_sim_predicted_rmse: 0.012
      real_data_actual_rmse: ">0.15"
      sim_to_real_gap_factor: ">12×"
      gap_explanation: "simulation assumes correct model spec + local independence; real data violates both"
      # SBC at realistic conditions
      sbc_at_n26_sim: "pass (p=0.34)"
      sbc_at_n26_real: "fail (p=0.003)"
    result_rationale: >
      Simulation sweep在idealized conditions下展示出令人鼓舞的结果——即使AUC=0.55(near chance)，
      γ也structurally identifiable(RMSE=0.04 at N=20)。这本身是一个有价值的理论贡献。
      但worst档的核心问题是sim-to-real gap：simulation中(1)model specification完全正确
      (data generating process = fitted model)，(2)local independence holds(每个examinee
      独立)，(3)exposure scores按exact AUC level生成(no distribution mismatch)。

      Real data违反所有三个假设：(1)contamination effect is scale-dependent(model misspecified)，
      (2)single model responds to all items(local independence violated)，(3)exposure AUC=0.96但
      inflation near-zero(high AUC doesn't help when there's nothing to calibrate)。
      因此simulation RMSE=0.012预测的精度在real data上inflated 12×以上。

      Fisher Information analysis gives I(γ) ∝ N × (AUC-0.5)² / σ²_e。在real conditions，
      AUC=0.96 gives (0.96-0.5)²=0.2116——似乎足够。但这个公式假设γ的true effect is non-zero
      且model correctly specified。当true γ≈0(1.5B/3B MMLU/ARC)，Fisher Info对precision
      的保证变成"we can precisely estimate that γ≈0"——which is correct but useless for calibration。

      SBC通过simulation(p=0.34)但fail on real data(p=0.003)——quantitative evidence for
      sim-to-real gap。
    tables:
      - name: "Simulation γ Recovery (RMSE) by AUC × N_models"
        rows:
          - {AUC: 0.55, N_20: 0.040, N_50: 0.026, N_100: 0.013, N_200: 0.007}
          - {AUC: 0.60, N_20: 0.038, N_50: 0.023, N_100: 0.011, N_200: 0.006}
          - {AUC: 0.65, N_20: 0.036, N_50: 0.021, N_100: 0.010, N_200: 0.005}
          - {AUC: 0.70, N_20: 0.034, N_50: 0.019, N_100: 0.009, N_200: 0.005}
          - {AUC: 0.80, N_20: 0.035, N_50: 0.018, N_100: 0.008, N_200: 0.004}
          - {AUC: 0.90, N_20: 0.033, N_50: 0.017, N_100: 0.008, N_200: 0.004}
      - name: "Sim-to-Real Gap"
        rows:
          - {condition: "AUC=0.96 N=26", sim_rmse: 0.012, real_rmse: ">0.15", gap: ">12×"}
          - {condition: "SBC p-value", sim: 0.34, real: 0.003, interpretation: "model correctly specified in sim, misspecified in real"}
    figures_description:
      - "Identifiability phase diagram: AUC (x-axis) × N_models (y-axis)，颜色编码γ RMSE。Structural boundary at AUC≈0.55(虚线)，practical boundary at AUC≈0.70(实线)。Red star标注real data conditions(AUC=0.96, N=26)——位于'应该work'的区域，但实际doesn't。"
      - "Sim-to-real gap scatter: x=predicted RMSE from sim，y=actual RMSE from real data。所有点远离对角线(actual >> predicted)。"
    analysis: >
      Identifiability分析是worst档下仍然valuable的独立贡献——它gives理论lower bounds。
      但必须诚实报告sim-to-real gap：'simulation establishes necessary conditions(AUC≥0.55
      structural, ≥0.70 practical), but these are NOT sufficient conditions in real data where
      model assumptions are violated'。这naturally leads to future work：(1)hierarchical IRT
      accounting for scale-dependent effects, (2)N_models >> 50 to overcome local independence
      violation, (3)multiple model families for robust estimation。

      Fisher Info derivation作为appendix material仍然有theory贡献：明确了I(γ)与AUC、N、σ_e
      的关系，为未来工作提供了quantitative design criteria。

  ########################################################################
  # exp-005 (predict v3 outcome — currently RUNNING)
  ########################################################################
  - name: "noise_propagation_analysis_v3_final"
    plan_id: "exp-005"
    description: >
      Measurement error model(exposure as noisy observation of latent τ)的最终结果。
      v1和v2已failed。Worst档：ME model收敛但不改善coverage，noise propagation正确但insufficient
      to compensate for model misspecification。
    expected_results:
      me_model_converges: true
      me_rhat_max: 1.04
      me_ess_min: 312
      # Coverage comparison
      point_estimate_95ci_coverage: 75
      me_model_95ci_coverage: 79
      me_coverage_improvement_pp: 4
      target_coverage: 95
      coverage_gap_remaining: 16
      # CI width
      me_ci_width_mean_pp: 23.8
      point_estimate_ci_width_pp: 21.2
      me_ci_widening_pp: 2.6
      # MAE
      me_mae_pp: 7.3
      point_estimate_mae_pp: 7.9
      me_mae_improvement_pp: 0.6
      # Noise injection robustness
      noise_1x_ci_widening_pct: 8
      noise_1_5x_ci_widening_pct: 15
      noise_2x_ci_widening_pct: 28
    result_rationale: >
      ME model在技术上works：它correctly propagates exposure uncertainty into posterior，
      产生slightly wider CIs(+2.6pp)和slightly better coverage(+4pp)。但coverage improvement
      from 75%→79%远不足以close 20pp gap to 95% nominal。原因：exposure measurement error
      只是coverage gap的minor contributor(~15% per SBC attribution)。主要原因是local
      independence violation(~60%)和model misspecification(~25%)——ME model不address these。

      Post-hoc noise injection实验shows CI widening scales linearly with noise level
      (as expected from theory)——这validates the ME model mechanics。但即使at 2× noise，
      CIs only widen 28%，coverage仅reaches ~83%——still below 95%。

      ME model作为D025 framing中的'if improves coverage → report; otherwise → ablation'
      decision node：in worst tier, it's an ablation item. Simple model(point-estimate exposure)
      is primary because ME model adds complexity without closing the coverage gap。
    tables:
      - name: "Measurement Error Model vs Point-Estimate Comparison"
        rows:
          - {metric: "MAE (pp)", point_estimate: 7.9, ME_model: 7.3, delta: -0.6}
          - {metric: "95% Coverage (%)", point_estimate: 75, ME_model: 79, delta: +4}
          - {metric: "95% CI Width (pp)", point_estimate: 21.2, ME_model: 23.8, delta: +2.6}
          - {metric: "Kendall τ", point_estimate: 0.69, ME_model: 0.70, delta: +0.01}
          - {metric: "Rhat max", point_estimate: 1.12, ME_model: 1.04, delta: -0.08}
    figures_description:
      - "Coverage calibration plot: nominal coverage (x) vs actual coverage (y)。Point-estimate线和ME-model线都在对角线下方(under-coverage)，ME-model线slightly closer to diagonal but still far off。"
    analysis: >
      ME model是worst档下的minor positive：它technically works but doesn't solve the core problem。
      论文中作为ablation报告：'measurement error model improves convergence(Rhat 1.12→1.04)
      and modestly improves coverage(75%→79%), but the dominant coverage gap source is
      local independence violation which requires structural model changes(e.g., hierarchical IRT
      or random-effects item parameters), not exposure noise propagation。'
      这strengthens identifiability分析的narrative——even with proper noise handling，
      fundamental model limitations remain。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e90c8cb-7e55-41e4-b14f-0872ce4df6b4",
  "isSidechain": false,
  "requestId": "req_011Cb31PYuzsLHGLTn5HphdR",
  "type": "assistant",
  "uuid": "d9fc495f-05d1-486f-aa96-efaa966a19a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AivApMYkDN2vdFQuaDMwM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2827,
      "cache_read_input_tokens": 38675,
      "output_tokens": 25142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 25142,
          "cache_read_input_tokens": 38675,
          "cache_creation_input_tokens": 2827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2827
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：γ在真实数据上不可靠识别，校准不优于线性回归基线；IRT复杂度无回报，核心框架假设在当前条件下不成立 核心假设：['4PL+γ IRT收敛困难（频繁divergence或R̂>1.05），或收敛后γ与θ严重混淆（后验相关>0.7）——与exp-006多次failure一致', '校准后MAE ≥ 线性回归基…",
  "leafUuid": "d9fc495f-05d1-486f-aa96-efaa966a19a4",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-aware IRT calibration: Identifiability boundaries and negative results",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：γ在真实数据上不可靠识别，校准不优于线性回归基线；IRT复杂度无回报，核心框架假设在当前条件下不成立 核心假设：['4PL+γ IRT收敛困难（频繁divergence或R̂>1.05），或收敛后γ与θ严重混淆（后验相关>0.7）——与exp-006多次failure一致', '校准后MAE ≥ 线性回归基…",
  "leafUuid": "d9fc495f-05d1-486f-aa96-efaa966a19a4",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-aware IRT calibration: Identifiability boundaries and negative results",
  "sessionId": "8e2f41cc-ff9d-4913-9e7c-f58ff8a800ac"
}
```

---
