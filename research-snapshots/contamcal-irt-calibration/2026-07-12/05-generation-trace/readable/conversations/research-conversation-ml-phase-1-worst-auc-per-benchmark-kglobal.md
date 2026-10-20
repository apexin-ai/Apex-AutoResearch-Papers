# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：γ和θ在实际数据上严重混淆；检测信号AUC不足以支撑有意义的校准；per-benchmark γ_k不收敛或与global γ无显著差异 核心假设：[

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/6f7fda0f-0d60-468c-b973-610dbbae8702.jsonl`
- **Structured JSON:** [`0c890792a3126cbf94ee.json`](../../sessions/0c/0c890792a3126cbf94ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T17:24:10.391Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T17:24:10.391Z",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：γ和θ在实际数据上严重混淆；检测信号AUC不足以支撑有意义的校准；per-benchmark γ_k不收敛或与global γ无显著差异\n核心假设：['RRF融合AUC在SFT regime仅0.60-0.68，RL regime下降至<0.55（随机附近）', 'γ和θ的posterior高度相关（|corr|>0.6），identifiability边界被实际数据突破', 'per-benchmark γ_k要么不收敛（ESS过低/divergent transitions），要么与global γ无统计差异', 'measurement error model使CI过宽以至于vacuous（95% CI宽度>20pp，trivially covers）', '信号生存分析无清晰regime-dependent pattern——所有信号在所有regime下表现相似', '第二模型家族结果与Qwen方向不一致或无法完成（GPU预算耗尽）', 'DCR在某些benchmark上与ContamCal无显著差异或更优']\n关键指标范围：{'calibration_mae_pp': [4.5, 9.0], 'coverage_95_pct': [70, 85], 'coverage_80_pct': [50, 68], 'ci_width_sft_pp': [6.0, 12.0], 'ci_width_rl_pp': [18.0, 30.0], 'kendall_tau': [0.65, 0.82], 'gamma_rel_bias': [0.18, 0.45], 'signal_auc_sft_rrf': [0.58, 0.7], 'signal_auc_rl_best_single': [0.48, 0.55], 'baselines_significantly_beaten': [1, 3], 'dose_response_monotonic': False, 'multi_family_mae_gap_pp': [4.0, 10.0]}\n叙事方向：核心calibration claim不成立——需要根本性reframe，但不降级venue目标。 新angle：\"ContamCal as a diagnostic framework for the limits of post-hoc calibration。\" 主线变为三层结构： (1) 理论贡献（保留且升级）：Fisher Information identifiability analysis成为paper核心—— 首次给出contamination calibration何时possible/impossible的理论界。 这是一个negative-but-informative result：我们证明了在signal AUC < X时， 任何post-hoc方法（包括DCR）都无法可靠校准，且给出了tight bound。 (2) 实证贡献（reframe）：信号生存分析作为独立的empirical contribution—— 即使它不支撑calibration，\"哪些信号在哪些regime下存活\"这个mapping对detection社区有独立价值。 如果cliff-like pattern不存在，reframe为\"signal degradation is gradual and benchmark-dependent， refuting the assumption of clean regime boundaries。\" (3) Calibration作为conditional proof-of-concept：\"当信号充分时（SFT regime + 大benchmark）， ContamCal提供有意义的校准；当信号不足时，框架诚实地报告高不确定性。\" 这个framing仍然viable for AAAI——方法论贡献（理论界+框架设计）+ 负面但有信息量的实证结果。 关键叙事：从\"我们解决了contamination calibration\"转为\"我们建立了contamination calibration的 possibility frontier，并展示了当前信号技术距离可靠校准还有多远。\" 需要额外工作：(a)加强理论section至2-3页，(b)与impossibility results文献对接， (c)将DCR的同样failure作为supporting evidence（\"不只是我们的方法fail——问题本身在当前信号下intractable\"）。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contamcal-irt-calibration\nvenue: AAAI 2027\nfocus: Key changes since Dream D1: (1) per-benchmark γ_k model variant replacing global γ, (2) measurement error model for exposure as default, (3) signal survival analysis elevated to Core Contribution, (4) Fisher Information identifiability analysis, (5) multi-family validation (Llama/Pythia), (6) DCR baseline added, (7) 30+ citations target, (8) local independence explicitly discussed, (9) RL regret uses held-out clean benchmark as ground truth. Focus review on whether these changes address the 5/10 score issues from Dream D1.\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)\n- Secondary: ICLR 2027 (expected deadline: Sep 2026)\n- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)\n\n## Core Insight\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\n\n## Core Claims (3 条)\n\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B), 2+ model families, and 4 benchmarks.\n\n2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.\n\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.\n\n## Contributions (Hierarchical)\n\n### Core\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\n2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)\n3. Dual-track validation: controlled SFT injection across multiple model families (internal validity) + ecological RL case study (external validity)\n\n### Supporting\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing**: ContamCal is a \"statistical safety net\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).\n- **Headline result template**: \"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\"\n\n## Venue Fit Risks\n- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.\n- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing (\"wide CIs are the correct answer, not a limitation\").\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k model variant as ablation; report both global and per-benchmark results | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Multi-family validation: Qwen2.5 + at least one additional family (Llama/Pythia) | exp-014 |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n\n## Evaluation Protocol (5 Metrics)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n\n## Benchmarks (4)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\n3. **ARC-Challenge** — science reasoning multiple-choice\n4. **HumanEval** — code generation with execution evaluation (N=164, noted as potential limitation for 4PL estimation)\n- Day-8 contingency: reduce to MMLU + GSM8K\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Citation Requirements (30+ minimum)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim:\n  - 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  status: planned\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim:\n  - 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim:\n  - 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  status: planned\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim:\n  - 1\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  status: planned\n- id: exp-005\n  name: noise_propagation_analysis\n  claim:\n  - 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  status: planned\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim:\n  - 1\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. TWO\\\n    \\ model variants: (a) global γ (single γ across all benchmarks), (b) per-benchmark\\\n    \\ γ_k (separate γ per benchmark). Report both. Per-benchmark γ_k addresses Dream\\\n    \\ reviewer concern about benchmark- heterogeneous contamination effects (3× range\\\n    \\ in inflation). IRT fitted per-benchmark (not jointly) to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  status: planned\n- id: exp-007\n  name: scale_bridging_7b\n  claim:\n  - 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim:\n  - 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  status: planned\n- id: exp-014\n  name: multi_family_validation\n  claim:\n  - 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim:\n  - 2\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim:\n  - 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim:\n  - 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      theta_corr: 0.943\n      theta_rmse: 0.238\n      max_rhat: 1.003\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      overall: PASS\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    theta_corr: 0.9733\n    theta_rmse: 0.2407\n    theta_residual_exp_corr: 0.0582\n    max_rhat: 1.007\n    divergent_pct: 0\n    min_ess: 1371.9\n    fit_time_sec: 832\n    actual_confound_corr: 0.3814\n    overall: PASS\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-13T17:24:10.397Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T17:24:10.397Z",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-13T17:24:10.424Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：γ和θ在实际数据上严重混淆；检测信号AUC不足以支撑有意义的校准；per-benchmark γ_k不收敛或与global γ无显著差异
核心假设：['RRF融合AUC在SFT regime仅0.60-0.68，RL regime下降至<0.55（随机附近）', 'γ和θ的posterior高度相关（|corr|>0.6），identifiability边界被实际数据突破', 'per-benchmark γ_k要么不收敛（ESS过低/divergent transitions），要么与global γ无统计差异', 'measurement error model使CI过宽以至于vacuous（95% CI宽度>20pp，trivially covers）', '信号生存分析无清晰regime-dependent pattern——所有信号在所有regime下表现相似', '第二模型家族结果与Qwen方向不一致或无法完成（GPU预算耗尽）', 'DCR在某些benchmark上与ContamCal无显著差异或更优']
关键指标范围：{'calibration_mae_pp': [4.5, 9.0], 'coverage_95_pct': [70, 85], 'coverage_80_pct': [50, 68], 'ci_width_sft_pp': [6.0, 12.0], 'ci_width_rl_pp': [18.0, 30.0], 'kendall_tau': [0.65, 0.82], 'gamma_rel_bias': [0.18, 0.45], 'signal_auc_sft_rrf': [0.58, 0.7], 'signal_auc_rl_best_single': [0.48, 0.55], 'baselines_significantly_beaten': [1, 3], 'dose_response_monotonic': False, 'multi_family_mae_gap_pp': [4.0, 10.0]}
叙事方向：核心calibration claim不成立——需要根本性reframe，但不降级venue目标。 新angle："ContamCal as a diagnostic framework for the limits of post-hoc calibration。" 主线变为三层结构： (1) 理论贡献（保留且升级）：Fisher Information identifiability analysis成为paper核心—— 首次给出contamination calibration何时possible/impossible的理论界。 这是一个negative-but-informative result：我们证明了在signal AUC < X时， 任何post-hoc方法（包括DCR）都无法可靠校准，且给出了tight bound。 (2) 实证贡献（reframe）：信号生存分析作为独立的empirical contribution—— 即使它不支撑calibration，"哪些信号在哪些regime下存活"这个mapping对detection社区有独立价值。 如果cliff-like pattern不存在，reframe为"signal degradation is gradual and benchmark-dependent， refuting the assumption of clean regime boundaries。" (3) Calibration作为conditional proof-of-concept："当信号充分时（SFT regime + 大benchmark）， ContamCal提供有意义的校准；当信号不足时，框架诚实地报告高不确定性。" 这个framing仍然viable for AAAI——方法论贡献（理论界+框架设计）+ 负面但有信息量的实证结果。 关键叙事：从"我们解决了contamination calibration"转为"我们建立了contamination calibration的 possibility frontier，并展示了当前信号技术距离可靠校准还有多远。" 需要额外工作：(a)加强理论section至2-3页，(b)与impossibility results文献对接， (c)将DCR的同样failure作为supporting evidence（"不只是我们的方法fail——问题本身在当前信号下intractable"）。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: contamcal-irt-calibration
venue: AAAI 2027
focus: Key changes since Dream D1: (1) per-benchmark γ_k model variant replacing global γ, (2) measurement error model for exposure as default, (3) signal survival analysis elevated to Core Contribution, (4) Fisher Information identifiability analysis, (5) multi-family validation (Llama/Pythia), (6) DCR baseline added, (7) 30+ citations target, (8) local independence explicitly discussed, (9) RL regret uses held-out clean benchmark as ground truth. Focus review on whether these changes address the 5/10 score issues from Dream D1.

## paper_framing.md

# Paper Framing — contamcal-irt-calibration

## Target Venue
- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)
- Secondary: ICLR 2027 (expected deadline: Sep 2026)
- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)

## Core Insight
When benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.

## Core Claims (3 条)

1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B), 2+ model families, and 4 benchmarks.

2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.

3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.

## Contributions (Hierarchical)

### Core
1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals
2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)
3. Dual-track validation: controlled SFT injection across multiple model families (internal validity) + ecological RL case study (external validity)

### Supporting
4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds
5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology

## Story Spine
- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
- **Our framing**: ContamCal is a "statistical safety net" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).
- **Headline result template**: "On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage."

## Venue Fit Risks
- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.
- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing ("wide CIs are the correct answer, not a limitation").
- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
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
| 9 | Single global γ misspecified? | Per-benchmark γ_k model variant as ablation; report both global and per-benchmark results | exp-006 |
| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
| 11 | Single model family? | Multi-family validation: Qwen2.5 + at least one additional family (Llama/Pythia) | exp-014 |
| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |

## Evaluation Protocol (5 Metrics)
1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage

## Benchmarks (4)
1. **MMLU** — knowledge-intensive multiple-choice (14K items)
2. **GSM8K** — mathematical reasoning free-form (~1.3K items)
3. **ARC-Challenge** — science reasoning multiple-choice
4. **HumanEval** — code generation with execution evaluation (N=164, noted as potential limitation for 4PL estimation)
- Day-8 contingency: reduce to MMLU + GSM8K

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

## Citation Requirements (30+ minimum)
Must include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.


## experiment_plan (with registry status)

- id: exp-001
  name: controlled_sft_injection
  claim:
  - 1
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
  status: planned
- id: exp-002
  name: stage1_signal_pipeline
  claim:
  - 2
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
  claim:
  - 2
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
  claim:
  - 1
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
  status: planned
- id: exp-005
  name: noise_propagation_analysis
  claim:
  - 3
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
  status: planned
- id: exp-006
  name: irt_calibration_and_baselines
  claim:
  - 1
  - 3
  description: "Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. TWO\
    \ model variants: (a) global γ (single γ across all benchmarks), (b) per-benchmark\
    \ γ_k (separate γ per benchmark). Report both. Per-benchmark γ_k addresses Dream\
    \ reviewer concern about benchmark- heterogeneous contamination effects (3× range\
    \ in inflation). IRT fitted per-benchmark (not jointly) to reduce local independence\
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
- id: exp-007
  name: scale_bridging_7b
  claim:
  - 1
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
  claim:
  - 2
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
  claim:
  - 1
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
  claim:
  - 2
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
  claim:
  - 1
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
  claim:
  - 2
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

- exp_id: mvp_sim_4pl_gamma
  name: ''
  status: DONE
  conclusion: success
  metrics:
    variant_a_nitems300:
      gamma_mean: 0.466
      gamma_rel_bias: 0.068
      gamma_ci_covers_true: true
      gamma_ci_excludes_zero: true
      theta_corr: 0.943
      theta_rmse: 0.238
      max_rhat: 1.003
      divergent_pct: 0
      fit_time_sec: 1407.5
      overall: PASS
- exp_id: mvp_sim_confounding
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gamma_mean: 0.5386
    gamma_rel_bias: 0.0771
    gamma_ci_covers_true: true
    gamma_ci_excludes_zero: true
    theta_corr: 0.9733
    theta_rmse: 0.2407
    theta_residual_exp_corr: 0.0582
    max_rhat: 1.007
    divergent_pct: 0
    min_ess: 1371.9
    fit_time_sec: 832
    actual_confound_corr: 0.3814
    overall: PASS
- exp_id: exp_004_sim_sweep
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
  "promptId": "36e7f43a-5d9e-44f9-82f4-4f17b0038e98",
  "type": "user",
  "uuid": "f5532566-8e95-4783-8747-98b180f2e4be",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T17:24:10.422Z_

```json
{
  "parentUuid": "f5532566-8e95-4783-8747-98b180f2e4be",
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
  "uuid": "aec896c5-583b-479e-9604-b903d7ac62ae",
  "timestamp": "2026-05-13T17:24:10.422Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T17:24:10.422Z_

```json
{
  "parentUuid": "aec896c5-583b-479e-9604-b903d7ac62ae",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0259323f-6255-43d0-901d-619973bbe798",
  "timestamp": "2026-05-13T17:24:10.422Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：γ和θ在实际数据上严重混淆；检测信号AUC不足以支撑有意义的校准；per-benchmark γ_k不收敛或与global γ无显著差异 核心假设：['RRF融合AUC在SFT regime仅0.60-0.68，RL regime下降至<0.55（随机附近）', 'γ和θ的posterior高度相关（|co…",
  "leafUuid": "0259323f-6255-43d0-901d-619973bbe798",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "ContamCal framework: calibration limits and diagnostic analysis",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702"
}
```

---

### Tool call

_source line 8 · 2026-05-13T17:24:15.699Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QCaC6vnKxQaWT84oKr4iuR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0259323f-6255-43d0-901d-619973bbe798",
  "isSidechain": false,
  "requestId": "req_011CazxTG4jKaarMKBugr9kA",
  "type": "assistant",
  "uuid": "d5721c54-ed09-4e99-a62d-123c11129da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzzNvhzRKm4WdSzzBYT5gn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13027,
      "cache_read_input_tokens": 11841,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13027,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 79,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13027
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

_source line 9 · 2026-05-13T17:24:15.738Z_

<details><summary>↩ Tool result · `toolu_01QCaC6vnKxQaWT84oKr4iuR`</summary>

```text
1	
2	## 输出风格
3	
4	- 回复简洁直接，不说废话
5	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
6	- 不要复述用户的问题
7	- 不要给未被要求的建议或补充说明
8	- 推理要彻底，但输出只保留结论和必要信息
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5721c54-ed09-4e99-a62d-123c11129da8",
  "isSidechain": false,
  "promptId": "36e7f43a-5d9e-44f9-82f4-4f17b0038e98",
  "type": "user",
  "uuid": "0f33736a-8a2b-46ee-8d45-dc565fd162e2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "d5721c54-ed09-4e99-a62d-123c11129da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T17:24:21.212Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KZK3BQne4RJ9Vs5Qu6YvPR`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan and registry",
  "prompt": "Search this project for any YAML, JSON, or markdown files that contain experiment plans, experiment registry, or detailed experiment definitions. Look for files like experiment_plan.yaml, registry.yaml, experiments.md, or similar. Also look for any Stan model files or simulation scripts that might inform the experiment details. Report file paths and brief content summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f33736a-8a2b-46ee-8d45-dc565fd162e2",
  "isSidechain": false,
  "requestId": "req_011CazxTesRt3qSyTdmepZG3",
  "type": "assistant",
  "uuid": "ce0b6ee0-8614-4c4a-b312-68835fa44955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dKnKcDu8Aueta5TgcXn8D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 24868,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 24868,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 252
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

_source line 11 · 2026-05-13T17:24:57.756Z_

<details><summary>↩ Tool result · `toolu_01KZK3BQne4RJ9Vs5Qu6YvPR`</summary>

```text
Perfect! Now I have comprehensive information. Let me compile the findings:

## Summary of Experiment Plans, Registries, and Definitions

I found a complete experimental framework for the **ContamCal** project (contamination-aware IRT calibration for LLM benchmarking). Here are the key documents:

### 1. **Primary Experiment Registry & Plan**

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml`
- **Status**: 2 completed experiments + 1 running
- **Exp mvp_sim_4pl_gamma** (DONE): Tests 4PL+γ IRT model on 50 models × 300 items with synthetic data. Successfully recovered γ posterior within ±15%, θ correlation >0.94, zero divergent transitions. Validates core identifiability hypothesis.
- **Exp mvp_sim_confounding** (DONE): Tests contamination-ability confounding (corr≈0.38). Shows γ still recovers with 7.7% bias, θ-exposure residual correlation drops to 0.058, confirming parameter separability.
- **Exp exp_004_sim_sweep** (RUNNING): Systematic sweep across AUC×N_models×prior×exposure_type combinations (120 runs total, 12 conditions × 10 seeds).

### 2. **Detailed Experiment Plan**

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml`
- **14 experiments** organized by priority (P0/P1/P2) with GPU budgets
- **P0 experiments** (must-run for submission):
  - **exp-001** (controlled_sft_injection): 3 Qwen2.5 models × 5 dosage levels, 15 SFT runs total
  - **exp-002** (stage1_signal_pipeline): Compute 4 detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique)
  - **exp-003** (rrf_aggregation_ablation): RRF fusion, single-signal ablations, FP robustness
  - **exp-004** (simulation_identifiability_sweep): 144 synthetic conditions, 10 seeds—establishes minimum AUC threshold and identifiability bounds
  - **exp-005** (noise_propagation_analysis): Inject matched/1.5×/2× noise levels, measure CI widening
  - **exp-006** (irt_calibration_and_baselines): 4PL+γ fitting with 5 baselines (remove-rescore, single-signal 2PL+γ, vanilla 4PL, linear regression, Emperor's mitigation)
  - **exp-008** (signal_survival_analysis): Signal × regime (base/SFT-clean/SFT-contaminated/RL) AUC heatmap
- **P1 experiments** (important but resource-constrained): exp-007 (7B scaling), exp-009 (RL case study), exp-014 (multi-family validation)
- **P2 experiments** (bonus): exp-012 (72B observational), exp-013 (2-signal degraded mode)
- **GPU budget**: 90h P0 + 60h P1 + 20h P2 + 30h buffer = 200h total H100-hours

### 3. **Dream Reports with Imagined Experiments**

**Files**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/{best,median,worst}/`
- Each tier (best/median/worst) contains:
  - **imagined_experiments.yaml**: Expected results with rationales (e.g., embedding retrieval AUC 0.88, RRF AUC 0.87, ContamCal MAE 1.97pp vs. baselines 3.5pp)
  - **experiment_data.json**: Structured metrics and result expectations
  - **paper_framing.md**: Venue fit, core claims, anticipated reviewer concerns, evaluation protocol

### 4. **Stan Models for IRT**

**Files**:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/contam_irt_4pl.stan`: 4PL+γ contamination-augmented IRT model with parameters (θ_i, a_j, b_j, c_j, d_j, γ)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/contam_irt_2pl.stan`: 2PL variant (used as fallback)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/contam_irt_4pl_sweep.stan`: Optimized for parameter sweeps

**Key model equation**: P(y_ij = 1) = c_j + (d_j - c_j) × inv_logit(a_j(θ_i - b_j) + γ × exposure_ij)

### 5. **Simulation Scripts**

**Files**:
- `run_p1_base.py`: 50 models × 100 items (baseline validation, failed threshold checks)
- `run_p1_variants.py`: 50 models × 300 items with 2PL/4PL variants (ADVI/NUTS) — identified 4PL NUTS as optimal
- `run_p2_confounding.py`: Tests confounding robustness with exposure-ability correlation
- `run_sweep.py`: Parameterized sweep framework for AUC/N_models/prior/exposure_type

### 6. **Project Documentation**

**Files**:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/IDEA_BRIEF.md`: Full 200-line research proposal with SOTA landscape, resource estimates, and risk assessment
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md`: Status handover with active experiments and conclusions
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/dream_registry.yaml`: Tracks 2 dream cycles (D1 completed with "best" tier, D2 in progress)

### 7. **Paper Framing Details**

**Key claims** (from paper_framing.md):
1. **Calibration Claim**: MAE <2pp with 93% CI coverage on controlled SFT injection
2. **Signal Aggregation Claim**: RRF fusion outperforms single signals, works on 2-signal degraded mode
3. **Uncertainty Quantification Claim**: Noise propagation validates CI widening under signal noise

**5 evaluation metrics**: Calibration error (MAE), interval coverage (50/80/95%), sharpness, Kendall τ ranking, dose-response monotonicity

**5 baselines**: Remove-rescore, single-signal 2PL+γ, vanilla 4PL, linear regression+bootstrap, Emperor's mitigation strategies

---

**In summary**, this is a mature experimental framework with:
- Completed MVP validation (2 experiments passed)
- Comprehensive 14-experiment roadmap with clear success criteria
- 3 Stan models for IRT fitting
- 4 Python simulation scripts for controlled contamination injection
- Dream reports with concrete expected results and failure modes
- Paper framing aligned with AAAI 2027 submission
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce0b6ee0-8614-4c4a-b312-68835fa44955",
  "isSidechain": false,
  "promptId": "36e7f43a-5d9e-44f9-82f4-4f17b0038e98",
  "type": "user",
  "uuid": "f5d671cd-9d8e-4da3-a41d-76c0a9980922",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search this project for any YAML, JSON, or markdown files that contain experiment plans, experiment registry, or detailed experiment definitions. Look for files like experiment_plan.yaml, registry.yaml, experiments.md, or similar. Also look for any Stan model files or simulation scripts that might inform the experiment details. Report file paths and brief content summaries.",
    "agentId": "aa9c8dd185b7ebd7a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me compile the findings:\n\n## Summary of Experiment Plans, Registries, and Definitions\n\nI found a complete experimental framework for the **ContamCal** project (contamination-aware IRT calibration for LLM benchmarking). Here are the key documents:\n\n### 1. **Primary Experiment Registry & Plan**\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml`\n- **Status**: 2 completed experiments + 1 running\n- **Exp mvp_sim_4pl_gamma** (DONE): Tests 4PL+γ IRT model on 50 models × 300 items with synthetic data. Successfully recovered γ posterior within ±15%, θ correlation >0.94, zero divergent transitions. Validates core identifiability hypothesis.\n- **Exp mvp_sim_confounding** (DONE): Tests contamination-ability confounding (corr≈0.38). Shows γ still recovers with 7.7% bias, θ-exposure residual correlation drops to 0.058, confirming parameter separability.\n- **Exp exp_004_sim_sweep** (RUNNING): Systematic sweep across AUC×N_models×prior×exposure_type combinations (120 runs total, 12 conditions × 10 seeds).\n\n### 2. **Detailed Experiment Plan**\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml`\n- **14 experiments** organized by priority (P0/P1/P2) with GPU budgets\n- **P0 experiments** (must-run for submission):\n  - **exp-001** (controlled_sft_injection): 3 Qwen2.5 models × 5 dosage levels, 15 SFT runs total\n  - **exp-002** (stage1_signal_pipeline): Compute 4 detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique)\n  - **exp-003** (rrf_aggregation_ablation): RRF fusion, single-signal ablations, FP robustness\n  - **exp-004** (simulation_identifiability_sweep): 144 synthetic conditions, 10 seeds—establishes minimum AUC threshold and identifiability bounds\n  - **exp-005** (noise_propagation_analysis): Inject matched/1.5×/2× noise levels, measure CI widening\n  - **exp-006** (irt_calibration_and_baselines): 4PL+γ fitting with 5 baselines (remove-rescore, single-signal 2PL+γ, vanilla 4PL, linear regression, Emperor's mitigation)\n  - **exp-008** (signal_survival_analysis): Signal × regime (base/SFT-clean/SFT-contaminated/RL) AUC heatmap\n- **P1 experiments** (important but resource-constrained): exp-007 (7B scaling), exp-009 (RL case study), exp-014 (multi-family validation)\n- **P2 experiments** (bonus): exp-012 (72B observational), exp-013 (2-signal degraded mode)\n- **GPU budget**: 90h P0 + 60h P1 + 20h P2 + 30h buffer = 200h total H100-hours\n\n### 3. **Dream Reports with Imagined Experiments**\n\n**Files**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/{best,median,worst}/`\n- Each tier (best/median/worst) contains:\n  - **imagined_experiments.yaml**: Expected results with rationales (e.g., embedding retrieval AUC 0.88, RRF AUC 0.87, ContamCal MAE 1.97pp vs. baselines 3.5pp)\n  - **experiment_data.json**: Structured metrics and result expectations\n  - **paper_framing.md**: Venue fit, core claims, anticipated reviewer concerns, evaluation protocol\n\n### 4. **Stan Models for IRT**\n\n**Files**:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/contam_irt_4pl.stan`: 4PL+γ contamination-augmented IRT model with parameters (θ_i, a_j, b_j, c_j, d_j, γ)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/contam_irt_2pl.stan`: 2PL variant (used as fallback)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/contam_irt_4pl_sweep.stan`: Optimized for parameter sweeps\n\n**Key model equation**: P(y_ij = 1) = c_j + (d_j - c_j) × inv_logit(a_j(θ_i - b_j) + γ × exposure_ij)\n\n### 5. **Simulation Scripts**\n\n**Files**:\n- `run_p1_base.py`: 50 models × 100 items (baseline validation, failed threshold checks)\n- `run_p1_variants.py`: 50 models × 300 items with 2PL/4PL variants (ADVI/NUTS) — identified 4PL NUTS as optimal\n- `run_p2_confounding.py`: Tests confounding robustness with exposure-ability correlation\n- `run_sweep.py`: Parameterized sweep framework for AUC/N_models/prior/exposure_type\n\n### 6. **Project Documentation**\n\n**Files**:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/IDEA_BRIEF.md`: Full 200-line research proposal with SOTA landscape, resource estimates, and risk assessment\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md`: Status handover with active experiments and conclusions\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/dream_registry.yaml`: Tracks 2 dream cycles (D1 completed with \"best\" tier, D2 in progress)\n\n### 7. **Paper Framing Details**\n\n**Key claims** (from paper_framing.md):\n1. **Calibration Claim**: MAE <2pp with 93% CI coverage on controlled SFT injection\n2. **Signal Aggregation Claim**: RRF fusion outperforms single signals, works on 2-signal degraded mode\n3. **Uncertainty Quantification Claim**: Noise propagation validates CI widening under signal noise\n\n**5 evaluation metrics**: Calibration error (MAE), interval coverage (50/80/95%), sharpness, Kendall τ ranking, dose-response monotonicity\n\n**5 baselines**: Remove-rescore, single-signal 2PL+γ, vanilla 4PL, linear regression+bootstrap, Emperor's mitigation strategies\n\n---\n\n**In summary**, this is a mature experimental framework with:\n- Completed MVP validation (2 experiments passed)\n- Comprehensive 14-experiment roadmap with clear success criteria\n- 3 Stan models for IRT fitting\n- 4 Python simulation scripts for controlled contamination injection\n- Dream reports with concrete expected results and failure modes\n- Paper framing aligned with AAAI 2027 submission"
      }
    ],
    "totalDurationMs": 36531,
    "totalTokens": 65737,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 63466,
      "output_tokens": 1937,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 328
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1937,
          "cache_read_input_tokens": 63466,
          "cache_creation_input_tokens": 328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 328,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 9,
      "searchCount": 5,
      "bashCount": 1,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "ce0b6ee0-8614-4c4a-b312-68835fa44955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-13T17:25:00.988Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the project. Let me look at the existing dream reports (best/median/worst) to understand the format and level of detail expected.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5d671cd-9d8e-4da3-a41d-76c0a9980922",
  "isSidechain": false,
  "requestId": "req_011CazxWkLB2kCTEe3T5t4Wc",
  "type": "assistant",
  "uuid": "32a9228e-db21-4e77-88ed-0984bf10d7b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqCpSwtfpE2YfCCaPGFmtd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 25120,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 25120,
          "cache_creation_input_tokens": 2111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2111
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

_source line 13 · 2026-05-13T17:25:02.081Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LuL9sHT3tLTo9tPzSNhAYi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32a9228e-db21-4e77-88ed-0984bf10d7b9",
  "isSidechain": false,
  "requestId": "req_011CazxWkLB2kCTEe3T5t4Wc",
  "type": "assistant",
  "uuid": "0a20a376-49c6-48d2-9912-b682261200e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqCpSwtfpE2YfCCaPGFmtd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 25120,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 25120,
          "cache_creation_input_tokens": 2111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2111
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

_source line 14 · 2026-05-13T17:25:02.401Z_

<details><summary>↩ Tool result · `toolu_01LuL9sHT3tLTo9tPzSNhAYi`</summary>

```text
1	tier: worst
2	narrative_guidance: '核心calibration claim不成立。Reframe为"Empirical Identifiability Boundaries
3	  for Contamination-Aware IRT"—— 系统性研究在什么条件下IRT校准才可行。exp-004仿真的identifiability map成为Core
4	  Contribution 1， exp-008 signal survival升级为Core，controlled SFT注入变为empirical validation证明仿真边界与真实数据吻合。
5	  叙事逻辑：在构建校准系统之前，先搞清楚它何时能工作。论文从"we solve calibration"转为"we map when calibration is
6	  solvable"。
7	
8	  '
9	imagined_experiments:
10	- name: controlled_sft_injection
11	  plan_id: exp-001
12	  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels.
13	    在worst档下，注入本身成功但产生的score inflation pattern不干净—— 低dosage几乎无可测效应，高dosage效应被模型capacity限制截断。
14	
15	    '
16	  expected_results:
17	    sft_runs_completed: 15
18	    mmlu_score_inflation_0pct_baseline_acc: 0.47
19	    mmlu_score_inflation_5pct_pp: 0.8
20	    mmlu_score_inflation_25pct_pp: 2.1
21	    mmlu_score_inflation_50pct_pp: 4.5
22	    mmlu_score_inflation_100pct_pp: 8.2
23	    gsm8k_score_inflation_100pct_pp: 5.1
24	    arc_score_inflation_100pct_pp: 6.8
25	    humaneval_score_inflation_100pct_pp: 3.9
26	    inflation_monotonicity_spearman_mmlu: 0.9
27	    inflation_monotonicity_spearman_gsm8k: 0.7
28	    inflation_variance_across_seeds_std_pp: 2.8
29	    qwen_0_5b_inflation_at_100pct_pp: 11.5
30	    qwen_3b_inflation_at_100pct_pp: 5.8
31	    low_dosage_detectable_5pct: false
32	    low_dosage_detectable_25pct_marginal: true
33	  result_rationale: 'SFT注入机制本身可靠（paraphrase SFT是成熟技术），所以15个run都会完成。 但worst档的核心问题在这里开始显现：(1)
34	    0.5B模型capacity极小，SFT后memorization严重但泛化到benchmark format的能力弱， 导致inflation方差大；(2)
35	    5%dosage（<700 items for MMLU）在SFT数据中被稀释，inflation <1pp， 与random seed noise不可区分——这直接导致后续dose-response非单调的关键问题；
36	    (3) GSM8K/HumanEval因为是生成式评估（非选择题），paraphrase memorization的转化率低于MMLU， inflation更弱；(4)
37	    3B模型因pretraining更强，SFT的边际效应递减—— 表现为"大模型inflation反而小于小模型"的反直觉模式，给后续γ估计制造confounding。
38	    整体inflation pattern存在但noisy，为后续信号检测和IRT拟合埋下问题。
39	
40	    '
41	  tables:
42	  - name: 'Table: Score Inflation by Model × Dosage × Benchmark'
43	    columns:
44	    - model
45	    - benchmark
46	    - 0%
47	    - 5%
48	    - 25%
49	    - 50%
50	    - 100%
51	    rows:
52	    - - Qwen2.5-0.5B
53	      - MMLU
54	      - 42.3
55	      - 43.5
56	      - 45.8
57	      - 49.1
58	      - 53.8
59	    - - Qwen2.5-0.5B
60	      - GSM8K
61	      - 31.2
62	      - 31.5
63	      - 32.8
64	      - 34.1
65	      - 36.3
66	    - - Qwen2.5-0.5B
67	      - ARC-C
68	      - 38.1
69	      - 38.6
70	      - 40.2
71	      - 42.5
72	      - 45.9
73	    - - Qwen2.5-0.5B
74	      - HumanEval
75	      - 22.0
76	      - 22.1
77	      - 23.0
78	      - 24.2
79	      - 25.9
80	    - - Qwen2.5-1.5B
81	      - MMLU
82	      - 53.1
83	      - 53.6
84	      - 54.8
85	      - 56.5
86	      - 59.7
87	    - - Qwen2.5-1.5B
88	      - GSM8K
89	      - 48.5
90	      - 48.8
91	      - 49.9
92	      - 51.8
93	      - 53.2
94	    - - Qwen2.5-1.5B
95	      - ARC-C
96	      - 52.0
97	      - 52.4
98	      - 53.5
99	      - 55.1
100	      - 57.8
101	    - - Qwen2.5-1.5B
102	      - HumanEval
103	      - 35.4
104	      - 35.6
105	      - 36.5
106	      - 37.8
107	      - 39.1
108	    - - Qwen2.5-3B
109	      - MMLU
110	      - 61.8
111	      - 62.1
112	      - 63.0
113	      - 64.5
114	      - 67.0
115	    - - Qwen2.5-3B
116	      - GSM8K
117	      - 62.3
118	      - 62.5
119	      - 63.1
120	      - 64.2
121	      - 65.8
122	    - - Qwen2.5-3B
123	      - ARC-C
124	      - 60.5
125	      - 60.8
126	      - 61.6
127	      - 63.0
128	      - 65.2
129	    - - Qwen2.5-3B
130	      - HumanEval
131	      - 48.2
132	      - 48.4
133	      - 49.0
134	      - 50.1
135	      - 52.1
136	  figures_description:
137	  - 'Fig: Dosage-Inflation curves per model×benchmark. Key observation: 5% dosage
138	    points overlap with 0% error bars on most benchmarks. GSM8K/HumanEval curves noticeably
139	    flatter than MMLU. 0.5B shows highest absolute inflation but also highest variance.'
140	  analysis: '注入成功但暴露了两个worst档关键弱点：(1) 低dosage信号几乎不存在（5%不可检出，25%边缘）， 这意味着后续dose-response分析在低端会崩溃；(2)
141	    inflation幅度跨benchmark差异大 （MMLU最高~8pp，HumanEval仅~4pp），且与model scale反相关， 说明contamination
142	    effect不是一个简单的additive γ——它与ability θ交互， 这从根本上挑战了4PL+γ的additive model specification。
143	    但作为reframed论文的素材，这些结果反而有价值——"仿真假设的uniform γ在真实数据中不成立"是identifiability分析的重要发现。
144	
145	    '
146	- name: stage1_signal_pipeline
147	  plan_id: exp-002
148	  description: '4个检测信号（embedding retrieval, Min-K%++, ConStat, Self-Critique） 在exp-001所有模型上的计算。worst档下信号质量显著低于仿真中假设的AUC水平。
149	
150	    '
151	  expected_results:
152	    embedding_retrieval_auc_sft_100pct_avg: 0.72
153	    embedding_retrieval_auc_sft_5pct_avg: 0.54
154	    minkpp_auc_sft_100pct_avg: 0.68
155	    minkpp_auc_sft_5pct_avg: 0.52
156	    constat_auc_sft_100pct_avg: 0.66
157	    constat_auc_sft_25pct_avg: 0.57
158	    selfcritique_auc_sft_100pct_avg: 0.63
159	    selfcritique_auc_sft_5pct_avg: 0.51
160	    avg_signal_auc_across_all_conditions: 0.61
161	    signal_auc_variance_across_benchmarks: 0.008
162	    embedding_retrieval_auc_qwen0_5b_100pct: 0.75
163	    embedding_retrieval_auc_qwen3b_100pct: 0.69
164	    minkpp_fp_rate_at_90pct_recall: 0.45
165	    constat_requires_paraphrase_availability: true
166	    selfcritique_entropy_separation_cohens_d: 0.41
167	  result_rationale: 'worst档的核心机制在这里发力：(1) Embedding retrieval在100%dosage下表现尚可（AUC~0.72），
168	    因为语义相似性是最直接的信号——但它本质上检测的是"题目是否在训练集里"而非"模型是否从中获益"， 这导致了fundamental mismatch：高AUC不等于高因果信号质量；
169	    (2) Min-K%++在SFT后的token distribution shift中受到干扰，AUC降至0.68—— SFT本身（无论是否contaminated）改变了模型的perplexity
170	    landscape，造成confounding； (3) ConStat需要paraphrased版本的benchmark items，而这些paraphrases本身可能在SFT数据中出现过
171	    （因为我们的注入就是用paraphrases），导致original-vs-paraphrase gap被压缩，AUC仅0.66； (4) Self-Critique在SFT
172	    regime下最弱（AUC 0.63），因为SFT同时改变了模型的self-evaluation能力， 特别是对小模型（0.5B）self-critique本身就不可靠。
173	    关键问题：所有信号在5%dosage下AUC接近random（0.51-0.54）， 因为被contaminate的items太少（~70 items for
174	    MMLU 5%），信号被noise淹没。 跨benchmark方差小意味着问题不是benchmark-specific而是系统性的信号质量天花板。
175	
176	    '
177	  tables:
178	  - name: 'Table: Signal AUC Heatmap — Signal × Dosage (averaged across models and
179	      benchmarks)'
180	    columns:
181	    - signal
182	    - 5%
183	    - 25%
184	    - 50%
185	    - 100%
186	    rows:
187	    - - Embedding Retrieval
188	      - 0.54
189	      - 0.62
190	      - 0.68
191	      - 0.72
192	    - - Min-K%++
193	      - 0.52
194	      - 0.58
195	      - 0.64
196	      - 0.68
197	    - - ConStat
198	      - 0.51
199	      - 0.57
200	      - 0.62
201	      - 0.66
202	    - - Self-Critique
203	      - 0.51
204	      - 0.55
205	      - 0.59
206	      - 0.63
207	  - name: 'Table: Signal AUC by Model Scale at 100% Dosage (MMLU)'
208	    columns:
209	    - signal
210	    - Qwen-0.5B
211	    - Qwen-1.5B
212	    - Qwen-3B
213	    rows:
214	    - - Embedding Retrieval
215	      - 0.75
216	      - 0.73
217	      - 0.69
218	    - - Min-K%++
219	      - 0.71
220	      - 0.68
221	      - 0.65
222	    - - ConStat
223	      - 0.69
224	      - 0.67
225	      - 0.63
226	    - - Self-Critique
227	      - 0.58
228	      - 0.64
229	      - 0.66
230	  figures_description:
231	  - 'Fig: 4×4 AUC heatmap (signal × dosage) with color gradient from red (0.50) to
232	    green (0.80). Dominated by orange/yellow tones, only top-right corner (embedding×100%)
233	    reaches green. Clear dosage gradient visible in all signals.'
234	  - 'Fig: Per-item score distributions (contaminated vs clean) for each signal at
235	    50% dosage. Heavy overlap visible, Cohen''s d annotations all < 0.6.'
236	  analysis: '这是worst档叙事的关键转折点：exp-004仿真假设AUC是exogenous input，在AUC≥0.70时identifiability成立。
237	    但真实数据表明，只有embedding retrieval在100%dosage下达到0.72，其余条件下所有信号都在0.70以下。 更严重的是，信号AUC与dosage正相关——恰好在低dosage（最需要检测的regime）信号最弱。
238	    这创造了一个catch-22：contamination越严重越容易检测，越轻微越不可检测， 但校准价值恰恰在轻微contamination时最高。这是reframed论文的核心洞察之一。
239	
240	    '
241	- name: rrf_aggregation_ablation
242	  plan_id: exp-003
243	  description: 'RRF融合及ablation。worst档下RRF未能显著超越最佳单信号， "互补性"假设在真实数据上不成立。
244	
245	    '
246	  expected_results:
247	    rrf_4signal_auc_100pct_dosage: 0.7
248	    rrf_4signal_auc_50pct_dosage: 0.65
249	    rrf_4signal_auc_25pct_dosage: 0.6
250	    rrf_4signal_auc_5pct_dosage: 0.55
251	    best_single_signal_auc_100pct: 0.72
252	    rrf_vs_best_single_auc_delta_100pct: -0.02
253	    rrf_vs_best_single_auc_delta_avg: 0.01
254	    rank_avg_auc_100pct: 0.69
255	    calibrated_weighted_rrf_auc_100pct: 0.71
256	    degraded_2signal_auc_100pct: 0.64
257	    degraded_2signal_auc_50pct: 0.59
258	    degraded_2signal_vs_4signal_auc_gap: 0.06
259	    fp_injection_robustness_auc_drop_10pct_fp: 0.04
260	    fp_injection_robustness_auc_drop_20pct_fp: 0.09
261	    signal_correlation_matrix_avg_pairwise_r: 0.58
262	  result_rationale: 'RRF融合的理论优势依赖于信号互补性——不同信号捕获不同aspect的contamination evidence。 worst档下这一假设崩溃的原因：(1)
263	    信号间pairwise correlation高达0.58（远高于独立信号假设的~0.2）， 因为所有信号本质上都在检测同一个latent变量（训练数据中是否包含该item的变体），
264	    只是通过不同proxy衡量，proxy之间高度相关； (2) RRF在100%dosage下（0.70）反而低于最佳单信号embedding retrieval（0.72），
265	    因为RRF等权平均了四个信号，而弱信号（Self-Critique 0.63）拖累了总体； (3) calibrated weighted RRF（0.71）通过下调弱信号权重稍有改善，但改善不显著
266	    （因为最优权重在small sample下估计不稳定）； (4) 2-signal degraded mode（ConStat+Self-Critique=0.64）更糟，
267	    因为这两个恰好是最弱的两个信号——closed-weight场景下的可用信号恰好是最差的。 FP injection进一步暴露了脆弱性：20% FP率下AUC下降0.09，说明信号对noise极敏感。
268	
269	    '
270	  tables:
271	  - name: 'Table: Aggregation Method Comparison (AUC at 100% dosage, MMLU)'
272	    columns:
273	    - method
274	    - AUC
275	    - Δ vs best single
276	    rows:
277	    - - Embedding Retrieval (best single)
278	      - 0.72
279	      - —
280	    - - Min-K%++
281	      - 0.68
282	      - -0.04
283	    - - ConStat
284	      - 0.66
285	      - -0.06
286	    - - Self-Critique
287	      - 0.63
288	      - -0.09
289	    - - RRF (4-signal)
290	      - 0.7
291	      - -0.02
292	    - - Rank Average (4-signal)
293	      - 0.69
294	      - -0.03
295	    - - Weighted RRF (calibrated)
296	      - 0.71
297	      - -0.01
298	    - - 2-signal degraded (CS+SC)
299	      - 0.64
300	      - -0.08
301	  - name: 'Table: RRF AUC across dosage levels'
302	    columns:
303	    - method
304	    - 5%
305	    - 25%
306	    - 50%
307	    - 100%
308	    rows:
309	    - - RRF 4-signal
310	      - 0.55
311	      - 0.6
312	      - 0.65
313	      - 0.7
314	    - - Best single
315	      - 0.54
316	      - 0.62
317	      - 0.68
318	      - 0.72
319	    - - 2-signal degraded
320	      - 0.52
321	      - 0.56
322	      - 0.59
323	      - 0.64
324	  figures_description:
325	  - 'Fig: Pairwise signal correlation matrix heatmap. All off-diagonal values 0.45-0.68,
326	    indicating high redundancy. Embedding-MinK++ highest (0.68), Self-Critique-others
327	    lowest (~0.45).'
328	  - 'Fig: RRF AUC vs number of signals (1,2,3,4). Flat curve — adding signals beyond
329	    the best single provides <0.02 AUC gain at any dosage. Contrasts sharply with
330	    simulated independent signals.'
331	  analysis: 'RRF的failure mode不是"融合方法差"而是"没有足够互补的信号可融合"。 信号correlation 0.58意味着~34%共享方差，真正独立的信息增量有限。
332	    对reframed论文的贡献：这变成了"signal diversity as identifiability prerequisite"的实证证据—— identifiability不仅需要足够高的AUC，还需要信号间足够低的correlation。
333	    当前4个信号不满足这一条件。2-signal degraded mode的糟糕表现 直接支持"closed-weight regime下calibration不可行"的结论。
334	
335	    '
336	- name: noise_propagation_analysis
337	  plan_id: exp-005
338	  description: '噪声传播分析。worst档下暴露检测信号噪声导致CI宽度急剧膨胀， 使calibration在实用意义上失去价值。
339	
340	    '
341	  expected_results:
342	    baseline_gamma_ci_width_pp: 18.0
343	    noise_1x_gamma_ci_width_pp: 22.5
344	    noise_1_5x_gamma_ci_width_pp: 28.0
345	    noise_2x_gamma_ci_width_pp: 35.2
346	    baseline_theta_ci_width_pp: 12.0
347	    noise_1x_theta_ci_width_pp: 15.8
348	    noise_1_5x_theta_ci_width_pp: 20.5
349	    noise_2x_theta_ci_width_pp: 27.1
350	    ci_coverage_95_at_noise_1x: 0.88
351	    ci_coverage_95_at_noise_1_5x: 0.93
352	    ci_coverage_95_at_noise_2x: 0.97
353	    selfcritique_estimated_fp_rate: 0.35
354	    selfcritique_estimated_fn_rate: 0.28
355	    measurement_error_model_converged: true
356	    measurement_error_model_ci_width_pp: 24.0
357	    ci_width_exceeds_practical_threshold_15pp_pct: 0.78
358	  result_rationale: 'noise propagation在worst档下创造了一个根本性的precision-coverage tradeoff：
359	    (1) 基线CI width已经是18pp（因为信号AUC低导致γ posterior宽）， 远超可发表的"tight calibration"标准（<10pp）；
360	    (2) Self-Critique的FP rate 35%和FN rate 28%意味着matched noise level已经很高， 1x noise
361	    injection后CI膨胀至22.5pp——此时CI覆盖了绝大部分可能的score值， calibration退化为"我们不知道真实score是多少"的诚实但无用的声明；
362	    (3) 2x noise下CI width 35pp意味着一个60%准确率的模型的95%CI覆盖[42.5%, 77.5%]—— 这个范围大到无法做任何有意义的model
363	    selection； (4) coverage随noise增加而上升（从0.88到0.97）是因为CI变宽了， 不是因为calibration变好了——这是overcoverage问题，CI过于保守。
364	    measurement error model收敛但CI width 24pp说明即使自动noise propagation也无法"解决"问题， 因为核心issue是信号本身太noisy，不是propagation方法不对。
365	
366	    '
367	  tables:
368	  - name: 'Table: CI Width and Coverage under Noise Injection'
369	    columns:
370	    - noise_level
371	    - gamma_ci_width_pp
372	    - theta_ci_width_pp
373	    - coverage_95%
374	    - coverage_80%
375	    rows:
376	    - - baseline (0x)
377	      - 18.0
378	      - 12.0
379	      - 0.82
380	      - 0.68
381	    - - matched (1x)
382	      - 22.5
383	      - 15.8
384	      - 0.88
385	      - 0.74
386	    - - 1.5x
387	      - 28.0
388	      - 20.5
389	      - 0.93
390	      - 0.82
391	    - - 2x
392	      - 35.2
393	      - 27.1
394	      - 0.97
395	      - 0.9
396	    - - measurement error model
397	      - 24.0
398	      - 17.2
399	      - 0.9
400	      - 0.76
401	  figures_description:
402	  - 'Fig: CI width vs noise multiplier. Near-linear relationship for γ, slightly sub-linear
403	    for θ. Horizontal dashed line at 15pp marks ''practical utility threshold'' —
404	    crossed at ~0.7x matched noise, meaning even below realistic noise levels CIs
405	    are already too wide.'
406	  - 'Fig: Coverage-Width tradeoff plot. Curve moves from undercoverage+narrow (baseline)
407	    to overcoverage+wide (2x noise). No operating point achieves both nominal coverage
408	    AND practical width.'
409	  analysis: '这是worst档最具诊断价值的实验。它量化了"信号噪声→calibration无用"的精确pathway。 核心发现可以被表述为noise
410	    amplification theorem的实证版本： 当检测信号AUC < 0.70时，IRT模型的noise propagation使calibrated
411	    CI width超过15pp， 此时calibration不具备practical decision value。 对reframed论文的贡献：这直接支持identifiability
412	    boundary的operational定义—— 不仅是"能否估计γ"（statistical identifiability），还是"估计的γ是否有用"（practical
413	    identifiability）。 引入15pp practical threshold将identifiability map从binary升级为graded。
414	
415	    '
416	- name: irt_calibration_and_baselines
417	  plan_id: exp-006
418	  description: '核心calibration实验——4PL+γ IRT拟合及5个baselines比较。 worst档下4PL+γ不显著优于简单baselines。
419	
420	    '
421	  expected_results:
422	    calibration_mae_4pl_gamma_pp: 7.8
423	    calibration_mae_remove_rescore_pp: 8.1
424	    calibration_mae_single_signal_2pl_gamma_pp: 7.5
425	    calibration_mae_vanilla_4pl_pp: 9.2
426	    calibration_mae_linear_regression_pp: 7.2
427	    calibration_mae_emperor_mitigation_pp: 8.9
428	    margin_4pl_gamma_vs_best_baseline_mae_relative: 0.08
429	    ci_coverage_95_4pl_gamma: 0.78
430	    ci_coverage_80_4pl_gamma: 0.62
431	    ci_coverage_50_4pl_gamma: 0.38
432	    ci_width_95_avg_pp: 19.5
433	    ci_width_80_avg_pp: 14.2
434	    kendall_tau_4pl_gamma: 0.62
435	    kendall_tau_linear_regression: 0.65
436	    kendall_tau_vanilla_4pl: 0.58
437	    dose_response_spearman: 0.55
438	    dose_response_monotonic: false
439	    dose_response_5pct_gamma_ci_includes_zero: true
440	    dose_response_25pct_gamma_ci_includes_zero: true
441	    dose_response_100pct_gamma_significant: true
442	    gamma_theta_posterior_correlation: 0.52
443	    gamma_rel_bias_avg: 0.35
444	    gamma_95ci_includes_zero_pct_conditions: 0.55
445	    paired_ttest_4pl_gamma_vs_linear_pvalue: 0.23
446	    paired_ttest_4pl_gamma_vs_remove_rescore_pvalue: 0.41
447	    stan_rhat_max: 1.08
448	    stan_divergent_pct: 3.2
449	    stan_ess_min: 180
450	  result_rationale: '这是worst档的核心实验，calibration claim在这里正式崩溃： (1) 4PL+γ MAE 7.8pp看似reasonable，但linear
451	    regression以7.2pp击败它—— 更简单的模型反而更好，因为IRT的复杂参数化（a,b,c,d,γ五个参数/item）在small sample下过拟合，
452	    而linear regression的regularization更有效； (2) single-signal 2PL+γ（7.5pp）也优于full 4PL+γ，说明additional
453	    IRT complexity（c,d参数） 反而引入了estimation noise而非提供更好的fit； (3) γ-θ posterior correlation
454	    0.52直接confirm了identifiability问题—— 模型无法区分"模型能力高"和"模型被contaminate了"，因为在我们的数据中 这两者确实相关（更大的模型被更多地contaminate，或者更capable的模型从contamination中获益更多）；
455	    (4) dose-response非单调：5%和25%的γ CI包含0，只有100%显著—— 这意味着模型只能检测"极端contamination"，对"轻微到中度contamination"无能为力；
456	    (5) CI coverage 78%严重undercoverage（nominal 95%），说明posterior CI低估了不确定性， 这与noise
457	    propagation实验一致——模型没有正确传播信号噪声； (6) Stan diagnostics出现3.2% divergences和R-hat 1.08，暗示posterior
458	    geometry有问题， 可能因为γ-θ near-unidentifiable导致posterior funnel/ridge。 所有pairwise significance
459	    tests p>0.05，确认4PL+γ不具备统计显著优势。
460	
461	    '
462	  tables:
463	  - name: 'Table: Calibration MAE (pp) by Method × Benchmark'
464	    columns:
465	    - method
466	    - MMLU
467	    - GSM8K
468	    - ARC-C
469	    - HumanEval
470	    - Average
471	    rows:
472	    - - 4PL+γ (ours)
473	      - 6.5
474	      - 9.2
475	      - 7.1
476	      - 8.4
477	      - 7.8
478	    - - Remove-rescore
479	      - 7.2
480	      - 8.8
481	      - 7.5
482	      - 8.9
483	      - 8.1
484	    - - Single-signal 2PL+γ
485	      - 6.2
486	      - 8.5
487	      - 7.0
488	      - 8.3
489	      - 7.5
490	    - - Vanilla 4PL
491	      - 8.1
492	      - 10.5
493	      - 8.8
494	      - 9.4
495	      - 9.2
496	    - - Linear regression+CI
497	      - 5.8
498	      - 8.2
499	      - 6.9
500	      - 7.9
501	      - 7.2
502	    - - Emperor mitigation
503	      - 7.8
504	      - 10.2
505	      - 8.2
506	      - 9.4
507	      - 8.9
508	  - name: 'Table: Interval Quality Metrics'
509	    columns:
510	    - method
511	    - Coverage 95%
512	    - Coverage 80%
513	    - Width 95% (pp)
514	    - Kendall τ
515	    rows:
516	    - - 4PL+γ
517	      - 0.78
518	      - 0.62
519	      - 19.5
520	      - 0.62
521	    - - Linear regression+CI
522	      - 0.83
523	      - 0.7
524	      - 16.2
525	      - 0.65
526	    - - Single-signal 2PL+γ
527	      - 0.8
528	      - 0.65
529	      - 17.8
530	      - 0.6
531	  - name: 'Table: Dose-Response γ Estimates'
532	    columns:
533	    - dosage
534	    - gamma_mean
535	    - gamma_95ci_lower
536	    - gamma_95ci_upper
537	    - ci_excludes_zero
538	    rows:
539	    - - 5%
540	      - 0.04
541	      - -0.18
542	      - 0.26
543	      - false
544	    - - 25%
545	      - 0.11
546	      - -0.08
547	      - 0.31
548	      - false
549	    - - 50%
550	      - 0.22
551	      - 0.01
552	      - 0.44
553	      - true
554	    - - 100%
555	      - 0.38
556	      - 0.12
557	      - 0.65
558	      - true
559	  figures_description:
560	  - 'Fig: MAE bar chart with 95% bootstrap CIs across methods. 4PL+γ bar overlaps
561	    with linear regression and single-signal 2PL+γ CIs. No method achieves separation.
562	    Vanilla 4PL and Emperor mitigation clearly worse but that''s a low bar.'
563	  - 'Fig: Calibration plot (predicted vs true clean accuracy). 4PL+γ shows high-dosage
564	    points calibrated but low-dosage points clustered near identity line (no correction
565	    applied because γ≈0). Linear regression shows more uniform correction.'
566	  - 'Fig: γ posterior density plots by dosage. 5% and 25% posteriors centered near
567	    zero with wide tails. 50% barely significant. Only 100% shows clear separation
568	    from zero.'
569	  - 'Fig: γ-θ posterior scatter plot showing 0.52 correlation. Banana-shaped posterior
570	    indicating identifiability ridge.'
571	  analysis: '这是worst档论文reframing的smoking gun实验。三个关键takeaways： (1) IRT complexity不付费——linear
572	    regression+bootstrap CI以更少参数达到更好MAE和coverage， 说明在当前信号质量下，复杂模型的额外表达力被estimation
573	    noise吞噬； (2) γ的identifiability是dosage-dependent的——只有极端contamination可被检测和校正， 这严重限制了实用价值（现实中contamination不可能是100%）；
574	    (3) undercoverage说明Bayesian CI名义上的"uncertainty quantification"实际上overconfident，
575	    这是因为model misspecification（additive γ假设）而非posterior approximation问题。 Reframed论文角度：这些结果精确对应了exp-004仿真预测的identifiability
576	    boundary—— 真实AUC~0.65-0.70恰好在仿真中identifiability开始崩溃的区域， 构成"仿真边界与真实数据吻合"的核心evidence。
577	
578	    '
579	- name: scale_bridging_7b
580	  plan_id: exp-007
581	  description: 'Qwen2.5-7B 5个dosage level的controlled SFT。worst档下scale-up不仅未改善， 反而加剧了γ-θ
582	    confounding。
583	
584	    '
585	  expected_results:
586	    sft_runs_completed: 5
587	    mmlu_score_inflation_100pct_pp: 4.5
588	    mmlu_score_inflation_50pct_pp: 2.8
589	    mmlu_score_inflation_5pct_pp: 0.4
590	    gsm8k_score_inflation_100pct_pp: 2.9
591	    signal_auc_embedding_100pct: 0.66
592	    signal_auc_minkpp_100pct: 0.62
593	    gamma_estimate_100pct: 0.25
594	    gamma_ci_includes_zero_100pct: false
595	    gamma_ci_includes_zero_50pct: true
596	    calibration_mae_4pl_gamma_pp: 8.5
597	    calibration_mae_linear_regression_pp: 7.8
598	    gamma_theta_posterior_corr: 0.58
599	    inflation_vs_3b_ratio: 0.55
600	  result_rationale: '7B模型在worst档下表现更差而非更好，原因： (1) 更大模型的pretraining knowledge已经覆盖了更多benchmark
601	    knowledge， SFT injection的边际效应递减——inflation仅4.5pp vs 0.5B的11.5pp； (2) 更小的inflation意味着detection
602	    signal的SNR更低（AUC从0.72降至0.66）， 因为contamination signal被更大模型的"naturally knowing the
603	    answer"所掩盖—— 这是worst档的核心confounding：能力高的模型天然就会答对contaminated items， detection信号无法区分"因为contamination答对"和"因为能力高答对"；
604	    (3) γ-θ posterior correlation升至0.58（vs 0.5B/1.5B/3B的0.52）， confirm了scale与identifiability的反相关关系；
605	    (4) calibration MAE反而上升到8.5pp，因为7B的inflation小（校正需求低）， 但estimation noise不变甚至更大（因为signal
606	    AUC更低），导致noise-to-signal ratio恶化。
607	
608	    '
609	  tables:
610	  - name: 'Table: 7B vs 3B Comparison at 100% Dosage'
611	    columns:
612	    - metric
613	    - Qwen-3B
614	    - Qwen-7B
615	    rows:
616	    - - MMLU inflation (pp)
617	      - 5.2
618	      - 4.5
619	    - - Embedding AUC
620	      - 0.69
621	      - 0.66
622	    - - γ estimate
623	      - 0.34
624	      - 0.25
625	    - - γ-θ posterior corr
626	      - 0.52
627	      - 0.58
628	    - - Calibration MAE (pp)
629	      - 7.8
630	      - 8.5
631	    - - CI width 95% (pp)
632	      - 19.5
633	      - 22.0
634	  figures_description:
635	  - 'Fig: Scale vs identifiability plot. X-axis: model params (0.5B to 7B). Y-axis:
636	    γ relative bias and signal AUC. Both metrics degrade with scale, showing inverse
637	    relationship between model capability and calibration feasibility.'
638	  analysis: '7B实验提供了worst档最重要的scaling insight：calibration difficulty与model scale正相关。
639	    这不是方法的failure而是problem structure的fundamental property—— 更强的模型天然掩盖contamination
640	    signal。 对reframed论文：这是identifiability boundary的第三个维度（signal quality × model count
641	    × model scale）， 且是最novel的——之前的identifiability分析没有考虑"ability confounds detection"。
642	
643	    '
644	- name: signal_survival_analysis
645	  plan_id: exp-008
646	  description: 'Detection signal在不同training regime下的survival分析。 worst档下确认SFT后信号已经脆弱，RL后几乎完全失效。
647	
648	    '
649	  expected_results:
650	    auc_heatmap:
651	      base_embedding: 0.78
652	      base_minkpp: 0.73
653	      base_constat: 0.71
654	      base_selfcritique: 0.6
655	      sft_clean_embedding: 0.72
656	      sft_clean_minkpp: 0.65
657	      sft_clean_constat: 0.63
658	      sft_clean_selfcritique: 0.58
659	      sft_contam_embedding: 0.72
660	      sft_contam_minkpp: 0.68
661	      sft_contam_constat: 0.66
662	      sft_contam_selfcritique: 0.63
663	      rl_embedding: 0.6
664	      rl_minkpp: 0.55
665	      rl_constat: 0.53
666	      rl_selfcritique: 0.57
667	    signal_survival_rate_sft_avg: 0.88
668	    signal_survival_rate_rl_avg: 0.73
669	    rl_best_signal: selfcritique
670	    rl_best_signal_auc: 0.57
671	    rl_all_signals_below_070: true
672	    sft_clean_contam_auc_difference_avg: 0.03
673	    regime_effect_anova_pvalue: 0.002
674	  result_rationale: 'signal survival分析在worst档下揭示了检测信号的systematic fragility： (1) Base
675	    model上信号最强（embedding 0.78），但这个"最佳条件"在实践中不存在—— 没有人在base model上做benchmark evaluation，所有评估都在post-trained
676	    model上； (2) SFT（无论clean还是contaminated）使所有信号平均下降12%—— 这是因为SFT改变了model representation
677	    space，token-level信号（Min-K%++）受影响最大， 而embedding retrieval因为不依赖model内部状态反而最稳定； (3)
678	    RL regime是灾难性的：所有信号AUC降至0.60以下或刚到0.60—— RL的reward hacking改变了model的输出distribution（更confident、更formulaic），
679	    使得基于distribution shift的检测（Min-K%++, ConStat）几乎失效； (4) Self-Critique在RL regime下反而成为"最佳信号"（0.57），但仅因为其他信号更差——
680	    0.57的AUC几乎没有实用价值（sensitivity+specificity之和刚过1.0）； (5) SFT clean vs contaminated的AUC差异仅0.03，说明信号的下降主要由post-training本身
681	    而非contamination引起——信号检测的是"training变化"而非"contamination变化"。
682	
683	    '
684	  tables:
685	  - name: 'Table: Signal × Regime AUC Heatmap'
686	    columns:
687	    - signal
688	    - Base
689	    - SFT-Clean
690	    - SFT-Contam
691	    - RL
692	    rows:
693	    - - Embedding Retrieval
694	      - 0.78
695	      - 0.72
696	      - 0.72
697	      - 0.6
698	    - - Min-K%++
699	      - 0.73
700	      - 0.65
701	      - 0.68
702	      - 0.55
703	    - - ConStat
704	      - 0.71
705	      - 0.63
706	      - 0.66
707	      - 0.53
708	    - - Self-Critique
709	      - 0.6
710	      - 0.58
711	      - 0.63
712	      - 0.57
713	  - name: 'Table: Signal Survival Rate (AUC retention relative to Base)'
714	    columns:
715	    - signal
716	    - SFT-Clean
717	    - SFT-Contam
718	    - RL
719	    rows:
720	    - - Embedding Retrieval
721	      - 0.92
722	      - 0.92
723	      - 0.77
724	    - - Min-K%++
725	      - 0.89
726	      - 0.93
727	      - 0.75
728	    - - ConStat
729	      - 0.89
730	      - 0.93
731	      - 0.75
732	    - - Self-Critique
733	      - 0.97
734	      - 1.05
735	      - 0.95
736	  figures_description:
737	  - 'Fig: 4×4 heatmap with color coding. Clear left-to-right degradation gradient.
738	    RL column almost uniformly orange/red. Self-Critique row most stable (highest
739	    retention) but starts lowest.'
740	  - 'Fig: Survival curves plotting AUC retention across regimes. Embedding and Min-K++
741	    show steep RL drop. Self-Critique nearly flat but at low absolute level — ''stable
742	    but weak''.'
743	  analysis: '这个实验在reframed论文中升级为Core Contribution之一。关键叙事： "Current detection signals
744	    were designed for and evaluated on base/SFT models. We show that post-training
745	    — especially RL — systematically degrades all signals below the identifiability
746	    threshold established in our simulation study (exp-004)." Self-Critique的"stability"是pyrrhic——它稳定在0.57-0.63的range，从未达到可用水平。
747	    这直接支持"RL regime下calibration不可行"的结论，且解释了为什么： 不是方法不对，而是信号不存在。
748	
749	    '
750	- name: rl_observational_case_study
751	  plan_id: exp-009
752	  description: 'RL-trained models的观察性案例研究。worst档下calibration在RL regime中几乎完全失效， expected
753	    regret reduction接近零甚至为负。
754	
755	    '
756	  expected_results:
757	    models_evaluated: 8
758	    selfcritique_auc_avg_rl: 0.57
759	    rrf_auc_avg_rl: 0.59
760	    calibration_mae_4pl_gamma_pp: 10.5
761	    calibration_mae_uncalibrated_pp: 9.8
762	    calibration_mae_remove_rescore_pp: 9.2
763	    ci_width_95_avg_pp: 24.5
764	    ci_coverage_95: 0.82
765	    expected_regret_reduction_vs_uncalibrated: -0.03
766	    expected_regret_reduction_vs_remove_rescore: -0.08
767	    top5_model_selection_agreement_with_true: 0.6
768	    gamma_estimates_mean: 0.08
769	    gamma_ci_includes_zero_pct: 0.85
770	    nearzero_gamma_clean_benchmark_check: true
771	    nearzero_gamma_clean_value: 0.02
772	    deepseek_r1_gamma_ci_includes_zero: true
773	  result_rationale: 'RL observational case study是worst档中最清晰的negative result： (1) Signal
774	    AUC在RL regime下仅0.57-0.59（exp-008已预测），这意味着exposure scores 几乎是noise，输入到IRT模型中的是garbage-in；
775	    (2) 4PL+γ MAE 10.5pp反而比uncalibrated的9.8pp更差—— 模型在noisy exposure scores上"hallucinate"了不存在的contamination
776	    effect， 做出了比不校正更差的adjustment（overcorrection on false positives，undercorrection
777	    on true positives）； (3) expected regret reduction为-0.03（vs uncalibrated）和-0.08（vs
778	    remove-rescore）， 即calibration使model selection决策变差了——这是因为宽CI（24.5pp）导致model rankings变得更noisy，
779	    而uncalibrated scores虽然biased但至少preserves ranking well； (4) 85%的conditions下γ CI包含零，说明模型在RL
780	    regime下根本检测不到contamination—— 不是"检测到了但校正不够"，而是"γ与zero不可区分"； (5) 唯一的positive result是specificity
781	    check通过——clean benchmark上γ≈0.02， 说明模型至少没有在clean data上产生false positive contamination
782	    detection。 但这是一个低门槛的成功。
783	
784	    '
785	  tables:
786	  - name: 'Table: RL Case Study — Calibration Method Comparison'
787	    columns:
788	    - method
789	    - MAE_pp
790	    - CI Width 95%
791	    - Coverage 95%
792	    - Regret Reduction
793	    rows:
794	    - - Uncalibrated (naive)
795	      - 9.8
796	      - —
797	      - —
798	      - —
799	    - - 4PL+γ
800	      - 10.5
801	      - 24.5
802	      - 0.82
803	      - -0.03
804	    - - Remove-rescore
805	      - 9.2
806	      - —
807	      - —
808	      - —
809	    - - Linear regression+CI
810	      - 9.9
811	      - 21.0
812	      - 0.85
813	      - 0.01
814	  - name: 'Table: Per-Model γ Estimates (RL models)'
815	    columns:
816	    - model
817	    - gamma_mean
818	    - gamma_95ci_lower
819	    - gamma_95ci_upper
820	    - ci_excludes_zero
821	    rows:
822	    - - Qwen2.5-0.5B-Instruct
823	      - 0.12
824	      - -0.15
825	      - 0.39
826	      - false
827	    - - Qwen2.5-1.5B-Instruct
828	      - 0.08
829	      - -0.18
830	      - 0.34
831	      - false
832	    - - Qwen2.5-3B-Instruct
833	      - 0.05
834	      - -0.21
835	      - 0.31
836	      - false
837	    - - Qwen2.5-7B-Instruct
838	      - 0.03
839	      - -0.25
840	      - 0.31
841	      - false
842	    - - DeepSeek-R1-Distill-1.5B
843	      - 0.1
844	      - -0.14
845	      - 0.34
846	      - false
847	    - - DeepSeek-R1-Distill-7B
848	      - 0.06
849	      - -0.2
850	      - 0.32
851	      - false
852	  figures_description:
853	  - 'Fig: Expected regret curves. X-axis: number of models selected. Y-axis: expected
854	    regret. Uncalibrated line sits below 4PL+γ line across all selection sizes. Thin
855	    gray lines show bootstrap replicates — high variance, no consistent winner.'
856	  - 'Fig: γ forest plot for all RL models. All CIs cross zero. Horizontal span of
857	    CIs (~0.5) dwarfs point estimates (~0.05-0.12).'
858	  analysis: 'RL case study提供了worst档最dramatic的result：calibration不仅不帮忙，还hurt。 这是因为在signal
859	    quality低于identifiability threshold时，IRT模型的额外参数 成为了pure noise amplifier。对reframed论文的贡献有两层：
860	    (1) Empirical confirmation that RL regime falls below identifiability boundary;
861	    (2) Practical recommendation — "do not attempt calibration when signal AUC < 0.60"。
862	    Specificity check的通过（clean γ≈0）是一个consolation prize—— 模型不产生false contamination
863	    detection，但也检测不到real contamination。
864	
865	    '
866	- name: prior_sensitivity
867	  plan_id: exp-010
868	  description: 'Prior sensitivity分析。worst档下结果对prior选择异常敏感， 暴露了model specification的fragility。
869	
870	    '
871	  expected_results:
872	    gamma_prior_n01_mae_pp: 7.8
873	    gamma_prior_n005_mae_pp: 9.5
874	    gamma_prior_n02_mae_pp: 7.2
875	    gamma_prior_n005_gamma_mean_shrinkage_ratio: 0.45
876	    gamma_prior_n02_gamma_mean_inflation_ratio: 1.35
877	    mae_sensitivity_range_pp: 2.3
878	    ci_coverage_sensitivity_range: 0.12
879	    ci_coverage_n005: 0.85
880	    ci_coverage_n01: 0.78
881	    ci_coverage_n02: 0.72
882	    prior_sensitivity_index: 0.38
883	  result_rationale: 'prior sensitivity在worst档下远超acceptable水平： (1) N(0,0.5) tight prior强制γ向零shrink
884	    45%，产生undercorrection但paradoxically 提高了coverage（0.85 vs 0.78），因为tight prior限制了CI的overconfidence；
885	    (2) N(0,2) wide prior允许γ inflate 35%，MAE改善（7.2pp）但coverage恶化至0.72， 因为wider prior导致posterior更受likelihood影响，而likelihood在noisy
886	    data上是misleading的； (3) MAE sensitivity range 2.3pp（across prior choices）占MAE值的~30%——
887	    这意味着结果高度依赖modeler的prior choice，而不是data-driven； (4) 理想情况下（信号好、sample大），Bayesian方法应该prior-insensitive——
888	    sensitivity本身就是under-identification的symptom，因为data不够informative来override prior。
889	
890	    '
891	  tables:
892	  - name: 'Table: Prior Sensitivity Comparison'
893	    columns:
894	    - prior
895	    - gamma_mean
896	    - MAE_pp
897	    - Coverage 95%
898	    - CI Width 95% (pp)
899	    rows:
900	    - - N(0, 0.5)
901	      - 0.22
902	      - 9.5
903	      - 0.85
904	      - 15.2
905	    - - N(0, 1.0) [default]
906	      - 0.38
907	      - 7.8
908	      - 0.78
909	      - 19.5
910	    - - N(0, 2.0)
911	      - 0.51
912	      - 7.2
913	      - 0.72
914	      - 24.8
915	  figures_description:
916	  - 'Fig: γ posterior distributions under three priors (overlaid density plots). Wide
917	    separation between posteriors — data does not dominate prior. Clear visual evidence
918	    of under-identification.'
919	  analysis: 'Prior sensitivity ≥ 30% of point estimate confirms that the model is
920	    in an under-identified regime. 对reframed论文：这直接maps到exp-004 identifiability sweep中的"prior
921	    sensitivity"维度， 验证了仿真预测——在AUC<0.70时prior choice matters more than data.
922	
923	    '
924	- name: few_examinee_regime
925	  plan_id: exp-011
926	  description: 'Few-examinee regime仿真研究。worst档下即使使用Growing Pains pre-estimation策略，
927	    N<50时identifiability完全崩溃。
928	
929	    '
930	  expected_results:
931	    n20_gamma_rmse: 0.42
932	    n20_gamma_rel_bias: 0.55
933	    n20_theta_corr: 0.58
934	    n20_ci_coverage_95: 0.68
935	    n50_gamma_rmse: 0.28
936	    n50_gamma_rel_bias: 0.38
937	    n50_theta_corr: 0.72
938	    n50_ci_coverage_95: 0.75
939	    n100_gamma_rmse: 0.18
940	    n100_gamma_rel_bias: 0.25
941	    n100_theta_corr: 0.82
942	    n100_ci_coverage_95: 0.8
943	    n200_gamma_rmse: 0.12
944	    n200_gamma_rel_bias: 0.18
945	    n200_theta_corr: 0.88
946	    n200_ci_coverage_95: 0.85
947	    growing_pains_pretrain_improvement_n20_pct: 15
948	    growing_pains_pretrain_improvement_n50_pct: 10
949	    minimum_n_for_gamma_significant: 80
950	    minimum_n_for_coverage_nominal: 150
951	  result_rationale: 'few-examinee regime在worst档下与信号质量问题叠加： (1) N=20（现实中常见——很多benchmark只有20-50个models被评估）时，
952	    γ RMSE 0.42，rel_bias 55%，θ与ground truth correlation仅0.58—— 此时模型参数估计本质上是noise；
953	    (2) Growing Pains pre-estimation策略（借用大pool的item参数先验）仅改善15%， 因为bottleneck不是item参数估计而是γ-θ的joint
954	    estimation—— item参数可以借用外部信息，但γ-θ的confounding是data-inherent的，无法靠先验缓解； (3) 达到γ显著（即CI排除零）需要N≥80，达到nominal
955	    coverage需要N≥150—— 这两个threshold在realistic benchmark evaluation scenarios中很难满足 （HELM有~100
956	    models，但大部分benchmarks的evaluated model count远少于此）； (4) 即使N=200，在worst档的信号质量下（AUC~0.65-0.70），
957	    gamma_rel_bias仍有18%，coverage仅85%——仍未达到publishable quality。
958	
959	    '
960	  tables:
961	  - name: 'Table: Identifiability Metrics by Model Count (AUC=0.65)'
962	    columns:
963	    - N
964	    - gamma_RMSE
965	    - gamma_rel_bias
966	    - theta_corr
967	    - Coverage 95%
968	    - Growing Pains Δ
969	    rows:
970	    - - 20
971	      - 0.42
972	      - 55%
973	      - 0.58
974	      - 68%
975	      - +15%
976	    - - 50
977	      - 0.28
978	      - 38%
979	      - 0.72
980	      - 75%
981	      - +10%
982	    - - 100
983	      - 0.18
984	      - 25%
985	      - 0.82
986	      - 80%
987	      - +5%
988	    - - 200
989	      - 0.12
990	      - 18%
991	      - 0.88
992	      - 85%
993	      - +3%
994	  figures_description:
995	  - 'Fig: Identifiability surface — X: model count, Y: signal AUC, Z: γ relative bias
996	    (color-coded). Clear ridge at AUC≈0.70 below which no amount of models helps sufficiently.
997	    The ''green zone'' (rel_bias<10%) requires AUC>0.80 AND N>100.'
998	  analysis: '这个仿真扩展与exp-004共同构成identifiability map的完整版本。 关键新发现：model count和signal
999	    AUC是multiplicative而非additive—— 在AUC<0.70时，增加N的边际收益急剧递减（从N=100到N=200，改善仅7pp rel_bias）。
1000	    这意味着"收集更多模型"不是解决identifiability的viable path when signals are weak。 对论文："minimum
1001	    signal quality targets for future work"可以被具体化为AUC×N的joint requirement。
1002	
1003	    '
1004	- name: observational_72b
1005	  plan_id: exp-012
1006	  description: 'Qwen2.5-72B观察性分析。worst档下大模型的信号质量进一步下降， confirm了scale-identifiability的inverse
1007	    relationship。
1008	
1009	    '
1010	  expected_results:
1011	    signal_auc_embedding: 0.6
1012	    signal_auc_minkpp: 0.56
1013	    signal_auc_constat: 0.54
1014	    signal_auc_selfcritique: 0.58
1015	    rrf_auc: 0.59
1016	    gamma_estimate: 0.04
1017	    gamma_ci_includes_zero: true
1018	    gamma_ci_width: 0.55
1019	    calibration_mae_pp: 11.2
1020	    ci_width_95_pp: 26.0
1021	  result_rationale: '72B模型将scale问题推向极端： (1) 72B的pretraining corpus几乎必然包含了benchmark
1022	    items的某种形式—— 不是传统意义的"contamination"而是"知识覆盖"，这使得所有detection signals的false positive
1023	    rate极高， embedding retrieval AUC降至0.60因为模型legitimately "knows" the content； (2)
1024	    γ estimate 0.04几乎为零，不是因为没有contamination而是因为unable to detect it—— 信号noise完全淹没了any
1025	    real signal； (3) 11.2pp MAE是worst档中最差的calibration error，因为72B的行为与smaller models
1026	    系统性不同（different error patterns, different item difficulty ordering）， IRT的transferability
1027	    across scales受到根本挑战。
1028	
1029	    '
1030	  tables:
1031	  - name: 'Table: 72B Observational Results'
1032	    columns:
1033	    - metric
1034	    - Qwen-72B
1035	    - Qwen-7B (controlled)
1036	    - Qwen-3B (controlled)
1037	    rows:
1038	    - - Best signal AUC
1039	      - 0.6
1040	      - 0.66
1041	      - 0.69
1042	    - - RRF AUC
1043	      - 0.59
1044	      - 0.63
1045	      - 0.67
1046	    - - γ estimate
1047	      - 0.04
1048	      - 0.25
1049	      - 0.34
1050	    - - γ CI excludes zero
1051	      - false
1052	      - Marginal (50%)
1053	      - true
1054	    - - Calibration MAE (pp)
1055	      - 11.2
1056	      - 8.5
1057	      - 7.8
1058	  figures_description:
1059	  - 'Fig: Scale vs signal AUC trend line from 0.5B to 72B. Clear monotonic decrease.
1060	    Horizontal dashed line at AUC=0.70 crossed between 1.5B and 3B scale. 72B is deep
1061	    in the ''unidentifiable'' zone.'
1062	  analysis: '72B结果是identifiability boundary story的natural endpoint： 在frontier model
1063	    scale上，calibration方法论本身不适用，因为"contamination"和"knowledge" 在概念层面就难以区分。这是reframed论文的strong
1064	    closing argument—— "our identifiability analysis reveals that contamination-aware
1065	    calibration faces a fundamental scale barrier: the very models most in need of
1066	    calibration (large, widely trained) are precisely those where calibration is least
1067	    feasible."
1068	
1069	    '
1070	- name: closed_weight_2signal_mode
1071	  plan_id: exp-013
1072	  description: '2-signal degraded mode (ConStat + Self-Critique) for closed-weight
1073	    models. worst档下降级模式使calibration完全不可行。
1074	
1075	    '
1076	  expected_results:
1077	    two_signal_rrf_auc_100pct_dosage: 0.64
1078	    two_signal_rrf_auc_50pct_dosage: 0.58
1079	    two_signal_rrf_auc_25pct_dosage: 0.54
1080	    calibration_mae_2signal_pp: 10.8
1081	    calibration_mae_4signal_pp: 7.8
1082	    mae_increase_relative_2_vs_4_signal: 0.38
1083	    ci_width_95_2signal_pp: 25.2
1084	    ci_coverage_95_2signal: 0.75
1085	    kendall_tau_2signal: 0.48
1086	    gamma_ci_includes_zero_2signal_pct: 0.72
1087	  result_rationale: '2-signal mode在worst档下是最差的配置： (1) ConStat和Self-Critique恰好是四个信号中AUC最低的两个（exp-002），
1088	    它们的fusion AUC 0.64远低于identifiability threshold 0.70； (2) MAE增加38%（从7.8pp到10.8pp），符合worst档的two_signal_degraded_mae_increase_relative范围[0.35,
1089	    0.6]； (3) Kendall τ降至0.48——低于0.5意味着calibrated rankings与true rankings的agreement
1090	    不比random好多少，calibration实际上在扰乱而非改善rankings； (4) 72%的conditions下γ CI包含零，说明在closed-weight
1091	    scenario下 contamination detection几乎完全不可行。 这是因为closed-weight模型不提供logits和embeddings，而这两个恰好是信号质量最高的信息源——
1092	    没有它们，剩余信号不足以支撑any meaningful calibration。
1093	
1094	    '
1095	  tables:
1096	  - name: 'Table: 2-Signal vs 4-Signal Calibration Gap'
1097	    columns:
1098	    - metric
1099	    - 4-signal
1100	    - 2-signal
1101	    - degradation
1102	    rows:
1103	    - - RRF AUC (100%)
1104	      - 0.7
1105	      - 0.64
1106	      - -8.6%
1107	    - - MAE (pp)
1108	      - 7.8
1109	      - 10.8
1110	      - +38%
1111	    - - CI Width 95% (pp)
1112	      - 19.5
1113	      - 25.2
1114	      - +29%
1115	    - - Kendall τ
1116	      - 0.62
1117	      - 0.48
1118	      - -23%
1119	    - - Coverage 95%
1120	      - 0.78
1121	      - 0.75
1122	      - -3.8%
1123	  figures_description:
1124	  - 'Fig: Side-by-side calibration error distributions (4-signal vs 2-signal). 2-signal
1125	    distribution shifted right with heavier tail. Overlap region highlighted — some
1126	    conditions where 2-signal accidentally performs okay, but median is significantly
1127	    worse.'
1128	  analysis: '2-signal degraded mode的failure confirm了一个important practical constraint：
1129	    closed-weight models（GPT-4, Claude等）——恰好是most scrutinized for contamination——
1130	    是calibration最不可行的targets。 对reframed论文：identifiability map需要一个新维度——"signal access
1131	    level" (full access: 4 signals; closed-weight: 2 signals)， 2-signal在identifiability
1132	    map上的viable region极小（仅AUC>0.80且N>150，现实中不存在）。'
1133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a20a376-49c6-48d2-9912-b682261200e7",
  "isSidechain": false,
  "promptId": "36e7f43a-5d9e-44f9-82f4-4f17b0038e98",
  "type": "user",
  "uuid": "1910d17f-0b57-49b8-af9b-5da2296ffc2d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/worst/imagined_experiments.yaml",
      "content": "tier: worst\nnarrative_guidance: '核心calibration claim不成立。Reframe为\"Empirical Identifiability Boundaries\n  for Contamination-Aware IRT\"—— 系统性研究在什么条件下IRT校准才可行。exp-004仿真的identifiability map成为Core\n  Contribution 1， exp-008 signal survival升级为Core，controlled SFT注入变为empirical validation证明仿真边界与真实数据吻合。\n  叙事逻辑：在构建校准系统之前，先搞清楚它何时能工作。论文从\"we solve calibration\"转为\"we map when calibration is\n  solvable\"。\n\n  '\nimagined_experiments:\n- name: controlled_sft_injection\n  plan_id: exp-001\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels.\n    在worst档下，注入本身成功但产生的score inflation pattern不干净—— 低dosage几乎无可测效应，高dosage效应被模型capacity限制截断。\n\n    '\n  expected_results:\n    sft_runs_completed: 15\n    mmlu_score_inflation_0pct_baseline_acc: 0.47\n    mmlu_score_inflation_5pct_pp: 0.8\n    mmlu_score_inflation_25pct_pp: 2.1\n    mmlu_score_inflation_50pct_pp: 4.5\n    mmlu_score_inflation_100pct_pp: 8.2\n    gsm8k_score_inflation_100pct_pp: 5.1\n    arc_score_inflation_100pct_pp: 6.8\n    humaneval_score_inflation_100pct_pp: 3.9\n    inflation_monotonicity_spearman_mmlu: 0.9\n    inflation_monotonicity_spearman_gsm8k: 0.7\n    inflation_variance_across_seeds_std_pp: 2.8\n    qwen_0_5b_inflation_at_100pct_pp: 11.5\n    qwen_3b_inflation_at_100pct_pp: 5.8\n    low_dosage_detectable_5pct: false\n    low_dosage_detectable_25pct_marginal: true\n  result_rationale: 'SFT注入机制本身可靠（paraphrase SFT是成熟技术），所以15个run都会完成。 但worst档的核心问题在这里开始显现：(1)\n    0.5B模型capacity极小，SFT后memorization严重但泛化到benchmark format的能力弱， 导致inflation方差大；(2)\n    5%dosage（<700 items for MMLU）在SFT数据中被稀释，inflation <1pp， 与random seed noise不可区分——这直接导致后续dose-response非单调的关键问题；\n    (3) GSM8K/HumanEval因为是生成式评估（非选择题），paraphrase memorization的转化率低于MMLU， inflation更弱；(4)\n    3B模型因pretraining更强，SFT的边际效应递减—— 表现为\"大模型inflation反而小于小模型\"的反直觉模式，给后续γ估计制造confounding。\n    整体inflation pattern存在但noisy，为后续信号检测和IRT拟合埋下问题。\n\n    '\n  tables:\n  - name: 'Table: Score Inflation by Model × Dosage × Benchmark'\n    columns:\n    - model\n    - benchmark\n    - 0%\n    - 5%\n    - 25%\n    - 50%\n    - 100%\n    rows:\n    - - Qwen2.5-0.5B\n      - MMLU\n      - 42.3\n      - 43.5\n      - 45.8\n      - 49.1\n      - 53.8\n    - - Qwen2.5-0.5B\n      - GSM8K\n      - 31.2\n      - 31.5\n      - 32.8\n      - 34.1\n      - 36.3\n    - - Qwen2.5-0.5B\n      - ARC-C\n      - 38.1\n      - 38.6\n      - 40.2\n      - 42.5\n      - 45.9\n    - - Qwen2.5-0.5B\n      - HumanEval\n      - 22.0\n      - 22.1\n      - 23.0\n      - 24.2\n      - 25.9\n    - - Qwen2.5-1.5B\n      - MMLU\n      - 53.1\n      - 53.6\n      - 54.8\n      - 56.5\n      - 59.7\n    - - Qwen2.5-1.5B\n      - GSM8K\n      - 48.5\n      - 48.8\n      - 49.9\n      - 51.8\n      - 53.2\n    - - Qwen2.5-1.5B\n      - ARC-C\n      - 52.0\n      - 52.4\n      - 53.5\n      - 55.1\n      - 57.8\n    - - Qwen2.5-1.5B\n      - HumanEval\n      - 35.4\n      - 35.6\n      - 36.5\n      - 37.8\n      - 39.1\n    - - Qwen2.5-3B\n      - MMLU\n      - 61.8\n      - 62.1\n      - 63.0\n      - 64.5\n      - 67.0\n    - - Qwen2.5-3B\n      - GSM8K\n      - 62.3\n      - 62.5\n      - 63.1\n      - 64.2\n      - 65.8\n    - - Qwen2.5-3B\n      - ARC-C\n      - 60.5\n      - 60.8\n      - 61.6\n      - 63.0\n      - 65.2\n    - - Qwen2.5-3B\n      - HumanEval\n      - 48.2\n      - 48.4\n      - 49.0\n      - 50.1\n      - 52.1\n  figures_description:\n  - 'Fig: Dosage-Inflation curves per model×benchmark. Key observation: 5% dosage\n    points overlap with 0% error bars on most benchmarks. GSM8K/HumanEval curves noticeably\n    flatter than MMLU. 0.5B shows highest absolute inflation but also highest variance.'\n  analysis: '注入成功但暴露了两个worst档关键弱点：(1) 低dosage信号几乎不存在（5%不可检出，25%边缘）， 这意味着后续dose-response分析在低端会崩溃；(2)\n    inflation幅度跨benchmark差异大 （MMLU最高~8pp，HumanEval仅~4pp），且与model scale反相关， 说明contamination\n    effect不是一个简单的additive γ——它与ability θ交互， 这从根本上挑战了4PL+γ的additive model specification。\n    但作为reframed论文的素材，这些结果反而有价值——\"仿真假设的uniform γ在真实数据中不成立\"是identifiability分析的重要发现。\n\n    '\n- name: stage1_signal_pipeline\n  plan_id: exp-002\n  description: '4个检测信号（embedding retrieval, Min-K%++, ConStat, Self-Critique） 在exp-001所有模型上的计算。worst档下信号质量显著低于仿真中假设的AUC水平。\n\n    '\n  expected_results:\n    embedding_retrieval_auc_sft_100pct_avg: 0.72\n    embedding_retrieval_auc_sft_5pct_avg: 0.54\n    minkpp_auc_sft_100pct_avg: 0.68\n    minkpp_auc_sft_5pct_avg: 0.52\n    constat_auc_sft_100pct_avg: 0.66\n    constat_auc_sft_25pct_avg: 0.57\n    selfcritique_auc_sft_100pct_avg: 0.63\n    selfcritique_auc_sft_5pct_avg: 0.51\n    avg_signal_auc_across_all_conditions: 0.61\n    signal_auc_variance_across_benchmarks: 0.008\n    embedding_retrieval_auc_qwen0_5b_100pct: 0.75\n    embedding_retrieval_auc_qwen3b_100pct: 0.69\n    minkpp_fp_rate_at_90pct_recall: 0.45\n    constat_requires_paraphrase_availability: true\n    selfcritique_entropy_separation_cohens_d: 0.41\n  result_rationale: 'worst档的核心机制在这里发力：(1) Embedding retrieval在100%dosage下表现尚可（AUC~0.72），\n    因为语义相似性是最直接的信号——但它本质上检测的是\"题目是否在训练集里\"而非\"模型是否从中获益\"， 这导致了fundamental mismatch：高AUC不等于高因果信号质量；\n    (2) Min-K%++在SFT后的token distribution shift中受到干扰，AUC降至0.68—— SFT本身（无论是否contaminated）改变了模型的perplexity\n    landscape，造成confounding； (3) ConStat需要paraphrased版本的benchmark items，而这些paraphrases本身可能在SFT数据中出现过\n    （因为我们的注入就是用paraphrases），导致original-vs-paraphrase gap被压缩，AUC仅0.66； (4) Self-Critique在SFT\n    regime下最弱（AUC 0.63），因为SFT同时改变了模型的self-evaluation能力， 特别是对小模型（0.5B）self-critique本身就不可靠。\n    关键问题：所有信号在5%dosage下AUC接近random（0.51-0.54）， 因为被contaminate的items太少（~70 items for\n    MMLU 5%），信号被noise淹没。 跨benchmark方差小意味着问题不是benchmark-specific而是系统性的信号质量天花板。\n\n    '\n  tables:\n  - name: 'Table: Signal AUC Heatmap — Signal × Dosage (averaged across models and\n      benchmarks)'\n    columns:\n    - signal\n    - 5%\n    - 25%\n    - 50%\n    - 100%\n    rows:\n    - - Embedding Retrieval\n      - 0.54\n      - 0.62\n      - 0.68\n      - 0.72\n    - - Min-K%++\n      - 0.52\n      - 0.58\n      - 0.64\n      - 0.68\n    - - ConStat\n      - 0.51\n      - 0.57\n      - 0.62\n      - 0.66\n    - - Self-Critique\n      - 0.51\n      - 0.55\n      - 0.59\n      - 0.63\n  - name: 'Table: Signal AUC by Model Scale at 100% Dosage (MMLU)'\n    columns:\n    - signal\n    - Qwen-0.5B\n    - Qwen-1.5B\n    - Qwen-3B\n    rows:\n    - - Embedding Retrieval\n      - 0.75\n      - 0.73\n      - 0.69\n    - - Min-K%++\n      - 0.71\n      - 0.68\n      - 0.65\n    - - ConStat\n      - 0.69\n      - 0.67\n      - 0.63\n    - - Self-Critique\n      - 0.58\n      - 0.64\n      - 0.66\n  figures_description:\n  - 'Fig: 4×4 AUC heatmap (signal × dosage) with color gradient from red (0.50) to\n    green (0.80). Dominated by orange/yellow tones, only top-right corner (embedding×100%)\n    reaches green. Clear dosage gradient visible in all signals.'\n  - 'Fig: Per-item score distributions (contaminated vs clean) for each signal at\n    50% dosage. Heavy overlap visible, Cohen''s d annotations all < 0.6.'\n  analysis: '这是worst档叙事的关键转折点：exp-004仿真假设AUC是exogenous input，在AUC≥0.70时identifiability成立。\n    但真实数据表明，只有embedding retrieval在100%dosage下达到0.72，其余条件下所有信号都在0.70以下。 更严重的是，信号AUC与dosage正相关——恰好在低dosage（最需要检测的regime）信号最弱。\n    这创造了一个catch-22：contamination越严重越容易检测，越轻微越不可检测， 但校准价值恰恰在轻微contamination时最高。这是reframed论文的核心洞察之一。\n\n    '\n- name: rrf_aggregation_ablation\n  plan_id: exp-003\n  description: 'RRF融合及ablation。worst档下RRF未能显著超越最佳单信号， \"互补性\"假设在真实数据上不成立。\n\n    '\n  expected_results:\n    rrf_4signal_auc_100pct_dosage: 0.7\n    rrf_4signal_auc_50pct_dosage: 0.65\n    rrf_4signal_auc_25pct_dosage: 0.6\n    rrf_4signal_auc_5pct_dosage: 0.55\n    best_single_signal_auc_100pct: 0.72\n    rrf_vs_best_single_auc_delta_100pct: -0.02\n    rrf_vs_best_single_auc_delta_avg: 0.01\n    rank_avg_auc_100pct: 0.69\n    calibrated_weighted_rrf_auc_100pct: 0.71\n    degraded_2signal_auc_100pct: 0.64\n    degraded_2signal_auc_50pct: 0.59\n    degraded_2signal_vs_4signal_auc_gap: 0.06\n    fp_injection_robustness_auc_drop_10pct_fp: 0.04\n    fp_injection_robustness_auc_drop_20pct_fp: 0.09\n    signal_correlation_matrix_avg_pairwise_r: 0.58\n  result_rationale: 'RRF融合的理论优势依赖于信号互补性——不同信号捕获不同aspect的contamination evidence。 worst档下这一假设崩溃的原因：(1)\n    信号间pairwise correlation高达0.58（远高于独立信号假设的~0.2）， 因为所有信号本质上都在检测同一个latent变量（训练数据中是否包含该item的变体），\n    只是通过不同proxy衡量，proxy之间高度相关； (2) RRF在100%dosage下（0.70）反而低于最佳单信号embedding retrieval（0.72），\n    因为RRF等权平均了四个信号，而弱信号（Self-Critique 0.63）拖累了总体； (3) calibrated weighted RRF（0.71）通过下调弱信号权重稍有改善，但改善不显著\n    （因为最优权重在small sample下估计不稳定）； (4) 2-signal degraded mode（ConStat+Self-Critique=0.64）更糟，\n    因为这两个恰好是最弱的两个信号——closed-weight场景下的可用信号恰好是最差的。 FP injection进一步暴露了脆弱性：20% FP率下AUC下降0.09，说明信号对noise极敏感。\n\n    '\n  tables:\n  - name: 'Table: Aggregation Method Comparison (AUC at 100% dosage, MMLU)'\n    columns:\n    - method\n    - AUC\n    - Δ vs best single\n    rows:\n    - - Embedding Retrieval (best single)\n      - 0.72\n      - —\n    - - Min-K%++\n      - 0.68\n      - -0.04\n    - - ConStat\n      - 0.66\n      - -0.06\n    - - Self-Critique\n      - 0.63\n      - -0.09\n    - - RRF (4-signal)\n      - 0.7\n      - -0.02\n    - - Rank Average (4-signal)\n      - 0.69\n      - -0.03\n    - - Weighted RRF (calibrated)\n      - 0.71\n      - -0.01\n    - - 2-signal degraded (CS+SC)\n      - 0.64\n      - -0.08\n  - name: 'Table: RRF AUC across dosage levels'\n    columns:\n    - method\n    - 5%\n    - 25%\n    - 50%\n    - 100%\n    rows:\n    - - RRF 4-signal\n      - 0.55\n      - 0.6\n      - 0.65\n      - 0.7\n    - - Best single\n      - 0.54\n      - 0.62\n      - 0.68\n      - 0.72\n    - - 2-signal degraded\n      - 0.52\n      - 0.56\n      - 0.59\n      - 0.64\n  figures_description:\n  - 'Fig: Pairwise signal correlation matrix heatmap. All off-diagonal values 0.45-0.68,\n    indicating high redundancy. Embedding-MinK++ highest (0.68), Self-Critique-others\n    lowest (~0.45).'\n  - 'Fig: RRF AUC vs number of signals (1,2,3,4). Flat curve — adding signals beyond\n    the best single provides <0.02 AUC gain at any dosage. Contrasts sharply with\n    simulated independent signals.'\n  analysis: 'RRF的failure mode不是\"融合方法差\"而是\"没有足够互补的信号可融合\"。 信号correlation 0.58意味着~34%共享方差，真正独立的信息增量有限。\n    对reframed论文的贡献：这变成了\"signal diversity as identifiability prerequisite\"的实证证据—— identifiability不仅需要足够高的AUC，还需要信号间足够低的correlation。\n    当前4个信号不满足这一条件。2-signal degraded mode的糟糕表现 直接支持\"closed-weight regime下calibration不可行\"的结论。\n\n    '\n- name: noise_propagation_analysis\n  plan_id: exp-005\n  description: '噪声传播分析。worst档下暴露检测信号噪声导致CI宽度急剧膨胀， 使calibration在实用意义上失去价值。\n\n    '\n  expected_results:\n    baseline_gamma_ci_width_pp: 18.0\n    noise_1x_gamma_ci_width_pp: 22.5\n    noise_1_5x_gamma_ci_width_pp: 28.0\n    noise_2x_gamma_ci_width_pp: 35.2\n    baseline_theta_ci_width_pp: 12.0\n    noise_1x_theta_ci_width_pp: 15.8\n    noise_1_5x_theta_ci_width_pp: 20.5\n    noise_2x_theta_ci_width_pp: 27.1\n    ci_coverage_95_at_noise_1x: 0.88\n    ci_coverage_95_at_noise_1_5x: 0.93\n    ci_coverage_95_at_noise_2x: 0.97\n    selfcritique_estimated_fp_rate: 0.35\n    selfcritique_estimated_fn_rate: 0.28\n    measurement_error_model_converged: true\n    measurement_error_model_ci_width_pp: 24.0\n    ci_width_exceeds_practical_threshold_15pp_pct: 0.78\n  result_rationale: 'noise propagation在worst档下创造了一个根本性的precision-coverage tradeoff：\n    (1) 基线CI width已经是18pp（因为信号AUC低导致γ posterior宽）， 远超可发表的\"tight calibration\"标准（<10pp）；\n    (2) Self-Critique的FP rate 35%和FN rate 28%意味着matched noise level已经很高， 1x noise\n    injection后CI膨胀至22.5pp——此时CI覆盖了绝大部分可能的score值， calibration退化为\"我们不知道真实score是多少\"的诚实但无用的声明；\n    (3) 2x noise下CI width 35pp意味着一个60%准确率的模型的95%CI覆盖[42.5%, 77.5%]—— 这个范围大到无法做任何有意义的model\n    selection； (4) coverage随noise增加而上升（从0.88到0.97）是因为CI变宽了， 不是因为calibration变好了——这是overcoverage问题，CI过于保守。\n    measurement error model收敛但CI width 24pp说明即使自动noise propagation也无法\"解决\"问题， 因为核心issue是信号本身太noisy，不是propagation方法不对。\n\n    '\n  tables:\n  - name: 'Table: CI Width and Coverage under Noise Injection'\n    columns:\n    - noise_level\n    - gamma_ci_width_pp\n    - theta_ci_width_pp\n    - coverage_95%\n    - coverage_80%\n    rows:\n    - - baseline (0x)\n      - 18.0\n      - 12.0\n      - 0.82\n      - 0.68\n    - - matched (1x)\n      - 22.5\n      - 15.8\n      - 0.88\n      - 0.74\n    - - 1.5x\n      - 28.0\n      - 20.5\n      - 0.93\n      - 0.82\n    - - 2x\n      - 35.2\n      - 27.1\n      - 0.97\n      - 0.9\n    - - measurement error model\n      - 24.0\n      - 17.2\n      - 0.9\n      - 0.76\n  figures_description:\n  - 'Fig: CI width vs noise multiplier. Near-linear relationship for γ, slightly sub-linear\n    for θ. Horizontal dashed line at 15pp marks ''practical utility threshold'' —\n    crossed at ~0.7x matched noise, meaning even below realistic noise levels CIs\n    are already too wide.'\n  - 'Fig: Coverage-Width tradeoff plot. Curve moves from undercoverage+narrow (baseline)\n    to overcoverage+wide (2x noise). No operating point achieves both nominal coverage\n    AND practical width.'\n  analysis: '这是worst档最具诊断价值的实验。它量化了\"信号噪声→calibration无用\"的精确pathway。 核心发现可以被表述为noise\n    amplification theorem的实证版本： 当检测信号AUC < 0.70时，IRT模型的noise propagation使calibrated\n    CI width超过15pp， 此时calibration不具备practical decision value。 对reframed论文的贡献：这直接支持identifiability\n    boundary的operational定义—— 不仅是\"能否估计γ\"（statistical identifiability），还是\"估计的γ是否有用\"（practical\n    identifiability）。 引入15pp practical threshold将identifiability map从binary升级为graded。\n\n    '\n- name: irt_calibration_and_baselines\n  plan_id: exp-006\n  description: '核心calibration实验——4PL+γ IRT拟合及5个baselines比较。 worst档下4PL+γ不显著优于简单baselines。\n\n    '\n  expected_results:\n    calibration_mae_4pl_gamma_pp: 7.8\n    calibration_mae_remove_rescore_pp: 8.1\n    calibration_mae_single_signal_2pl_gamma_pp: 7.5\n    calibration_mae_vanilla_4pl_pp: 9.2\n    calibration_mae_linear_regression_pp: 7.2\n    calibration_mae_emperor_mitigation_pp: 8.9\n    margin_4pl_gamma_vs_best_baseline_mae_relative: 0.08\n    ci_coverage_95_4pl_gamma: 0.78\n    ci_coverage_80_4pl_gamma: 0.62\n    ci_coverage_50_4pl_gamma: 0.38\n    ci_width_95_avg_pp: 19.5\n    ci_width_80_avg_pp: 14.2\n    kendall_tau_4pl_gamma: 0.62\n    kendall_tau_linear_regression: 0.65\n    kendall_tau_vanilla_4pl: 0.58\n    dose_response_spearman: 0.55\n    dose_response_monotonic: false\n    dose_response_5pct_gamma_ci_includes_zero: true\n    dose_response_25pct_gamma_ci_includes_zero: true\n    dose_response_100pct_gamma_significant: true\n    gamma_theta_posterior_correlation: 0.52\n    gamma_rel_bias_avg: 0.35\n    gamma_95ci_includes_zero_pct_conditions: 0.55\n    paired_ttest_4pl_gamma_vs_linear_pvalue: 0.23\n    paired_ttest_4pl_gamma_vs_remove_rescore_pvalue: 0.41\n    stan_rhat_max: 1.08\n    stan_divergent_pct: 3.2\n    stan_ess_min: 180\n  result_rationale: '这是worst档的核心实验，calibration claim在这里正式崩溃： (1) 4PL+γ MAE 7.8pp看似reasonable，但linear\n    regression以7.2pp击败它—— 更简单的模型反而更好，因为IRT的复杂参数化（a,b,c,d,γ五个参数/item）在small sample下过拟合，\n    而linear regression的regularization更有效； (2) single-signal 2PL+γ（7.5pp）也优于full 4PL+γ，说明additional\n    IRT complexity（c,d参数） 反而引入了estimation noise而非提供更好的fit； (3) γ-θ posterior correlation\n    0.52直接confirm了identifiability问题—— 模型无法区分\"模型能力高\"和\"模型被contaminate了\"，因为在我们的数据中 这两者确实相关（更大的模型被更多地contaminate，或者更capable的模型从contamination中获益更多）；\n    (4) dose-response非单调：5%和25%的γ CI包含0，只有100%显著—— 这意味着模型只能检测\"极端contamination\"，对\"轻微到中度contamination\"无能为力；\n    (5) CI coverage 78%严重undercoverage（nominal 95%），说明posterior CI低估了不确定性， 这与noise\n    propagation实验一致——模型没有正确传播信号噪声； (6) Stan diagnostics出现3.2% divergences和R-hat 1.08，暗示posterior\n    geometry有问题， 可能因为γ-θ near-unidentifiable导致posterior funnel/ridge。 所有pairwise significance\n    tests p>0.05，确认4PL+γ不具备统计显著优势。\n\n    '\n  tables:\n  - name: 'Table: Calibration MAE (pp) by Method × Benchmark'\n    columns:\n    - method\n    - MMLU\n    - GSM8K\n    - ARC-C\n    - HumanEval\n    - Average\n    rows:\n    - - 4PL+γ (ours)\n      - 6.5\n      - 9.2\n      - 7.1\n      - 8.4\n      - 7.8\n    - - Remove-rescore\n      - 7.2\n      - 8.8\n      - 7.5\n      - 8.9\n      - 8.1\n    - - Single-signal 2PL+γ\n      - 6.2\n      - 8.5\n      - 7.0\n      - 8.3\n      - 7.5\n    - - Vanilla 4PL\n      - 8.1\n      - 10.5\n      - 8.8\n      - 9.4\n      - 9.2\n    - - Linear regression+CI\n      - 5.8\n      - 8.2\n      - 6.9\n      - 7.9\n      - 7.2\n    - - Emperor mitigation\n      - 7.8\n      - 10.2\n      - 8.2\n      - 9.4\n      - 8.9\n  - name: 'Table: Interval Quality Metrics'\n    columns:\n    - method\n    - Coverage 95%\n    - Coverage 80%\n    - Width 95% (pp)\n    - Kendall τ\n    rows:\n    - - 4PL+γ\n      - 0.78\n      - 0.62\n      - 19.5\n      - 0.62\n    - - Linear regression+CI\n      - 0.83\n      - 0.7\n      - 16.2\n      - 0.65\n    - - Single-signal 2PL+γ\n      - 0.8\n      - 0.65\n      - 17.8\n      - 0.6\n  - name: 'Table: Dose-Response γ Estimates'\n    columns:\n    - dosage\n    - gamma_mean\n    - gamma_95ci_lower\n    - gamma_95ci_upper\n    - ci_excludes_zero\n    rows:\n    - - 5%\n      - 0.04\n      - -0.18\n      - 0.26\n      - false\n    - - 25%\n      - 0.11\n      - -0.08\n      - 0.31\n      - false\n    - - 50%\n      - 0.22\n      - 0.01\n      - 0.44\n      - true\n    - - 100%\n      - 0.38\n      - 0.12\n      - 0.65\n      - true\n  figures_description:\n  - 'Fig: MAE bar chart with 95% bootstrap CIs across methods. 4PL+γ bar overlaps\n    with linear regression and single-signal 2PL+γ CIs. No method achieves separation.\n    Vanilla 4PL and Emperor mitigation clearly worse but that''s a low bar.'\n  - 'Fig: Calibration plot (predicted vs true clean accuracy). 4PL+γ shows high-dosage\n    points calibrated but low-dosage points clustered near identity line (no correction\n    applied because γ≈0). Linear regression shows more uniform correction.'\n  - 'Fig: γ posterior density plots by dosage. 5% and 25% posteriors centered near\n    zero with wide tails. 50% barely significant. Only 100% shows clear separation\n    from zero.'\n  - 'Fig: γ-θ posterior scatter plot showing 0.52 correlation. Banana-shaped posterior\n    indicating identifiability ridge.'\n  analysis: '这是worst档论文reframing的smoking gun实验。三个关键takeaways： (1) IRT complexity不付费——linear\n    regression+bootstrap CI以更少参数达到更好MAE和coverage， 说明在当前信号质量下，复杂模型的额外表达力被estimation\n    noise吞噬； (2) γ的identifiability是dosage-dependent的——只有极端contamination可被检测和校正， 这严重限制了实用价值（现实中contamination不可能是100%）；\n    (3) undercoverage说明Bayesian CI名义上的\"uncertainty quantification\"实际上overconfident，\n    这是因为model misspecification（additive γ假设）而非posterior approximation问题。 Reframed论文角度：这些结果精确对应了exp-004仿真预测的identifiability\n    boundary—— 真实AUC~0.65-0.70恰好在仿真中identifiability开始崩溃的区域， 构成\"仿真边界与真实数据吻合\"的核心evidence。\n\n    '\n- name: scale_bridging_7b\n  plan_id: exp-007\n  description: 'Qwen2.5-7B 5个dosage level的controlled SFT。worst档下scale-up不仅未改善， 反而加剧了γ-θ\n    confounding。\n\n    '\n  expected_results:\n    sft_runs_completed: 5\n    mmlu_score_inflation_100pct_pp: 4.5\n    mmlu_score_inflation_50pct_pp: 2.8\n    mmlu_score_inflation_5pct_pp: 0.4\n    gsm8k_score_inflation_100pct_pp: 2.9\n    signal_auc_embedding_100pct: 0.66\n    signal_auc_minkpp_100pct: 0.62\n    gamma_estimate_100pct: 0.25\n    gamma_ci_includes_zero_100pct: false\n    gamma_ci_includes_zero_50pct: true\n    calibration_mae_4pl_gamma_pp: 8.5\n    calibration_mae_linear_regression_pp: 7.8\n    gamma_theta_posterior_corr: 0.58\n    inflation_vs_3b_ratio: 0.55\n  result_rationale: '7B模型在worst档下表现更差而非更好，原因： (1) 更大模型的pretraining knowledge已经覆盖了更多benchmark\n    knowledge， SFT injection的边际效应递减——inflation仅4.5pp vs 0.5B的11.5pp； (2) 更小的inflation意味着detection\n    signal的SNR更低（AUC从0.72降至0.66）， 因为contamination signal被更大模型的\"naturally knowing the\n    answer\"所掩盖—— 这是worst档的核心confounding：能力高的模型天然就会答对contaminated items， detection信号无法区分\"因为contamination答对\"和\"因为能力高答对\"；\n    (3) γ-θ posterior correlation升至0.58（vs 0.5B/1.5B/3B的0.52）， confirm了scale与identifiability的反相关关系；\n    (4) calibration MAE反而上升到8.5pp，因为7B的inflation小（校正需求低）， 但estimation noise不变甚至更大（因为signal\n    AUC更低），导致noise-to-signal ratio恶化。\n\n    '\n  tables:\n  - name: 'Table: 7B vs 3B Comparison at 100% Dosage'\n    columns:\n    - metric\n    - Qwen-3B\n    - Qwen-7B\n    rows:\n    - - MMLU inflation (pp)\n      - 5.2\n      - 4.5\n    - - Embedding AUC\n      - 0.69\n      - 0.66\n    - - γ estimate\n      - 0.34\n      - 0.25\n    - - γ-θ posterior corr\n      - 0.52\n      - 0.58\n    - - Calibration MAE (pp)\n      - 7.8\n      - 8.5\n    - - CI width 95% (pp)\n      - 19.5\n      - 22.0\n  figures_description:\n  - 'Fig: Scale vs identifiability plot. X-axis: model params (0.5B to 7B). Y-axis:\n    γ relative bias and signal AUC. Both metrics degrade with scale, showing inverse\n    relationship between model capability and calibration feasibility.'\n  analysis: '7B实验提供了worst档最重要的scaling insight：calibration difficulty与model scale正相关。\n    这不是方法的failure而是problem structure的fundamental property—— 更强的模型天然掩盖contamination\n    signal。 对reframed论文：这是identifiability boundary的第三个维度（signal quality × model count\n    × model scale）， 且是最novel的——之前的identifiability分析没有考虑\"ability confounds detection\"。\n\n    '\n- name: signal_survival_analysis\n  plan_id: exp-008\n  description: 'Detection signal在不同training regime下的survival分析。 worst档下确认SFT后信号已经脆弱，RL后几乎完全失效。\n\n    '\n  expected_results:\n    auc_heatmap:\n      base_embedding: 0.78\n      base_minkpp: 0.73\n      base_constat: 0.71\n      base_selfcritique: 0.6\n      sft_clean_embedding: 0.72\n      sft_clean_minkpp: 0.65\n      sft_clean_constat: 0.63\n      sft_clean_selfcritique: 0.58\n      sft_contam_embedding: 0.72\n      sft_contam_minkpp: 0.68\n      sft_contam_constat: 0.66\n      sft_contam_selfcritique: 0.63\n      rl_embedding: 0.6\n      rl_minkpp: 0.55\n      rl_constat: 0.53\n      rl_selfcritique: 0.57\n    signal_survival_rate_sft_avg: 0.88\n    signal_survival_rate_rl_avg: 0.73\n    rl_best_signal: selfcritique\n    rl_best_signal_auc: 0.57\n    rl_all_signals_below_070: true\n    sft_clean_contam_auc_difference_avg: 0.03\n    regime_effect_anova_pvalue: 0.002\n  result_rationale: 'signal survival分析在worst档下揭示了检测信号的systematic fragility： (1) Base\n    model上信号最强（embedding 0.78），但这个\"最佳条件\"在实践中不存在—— 没有人在base model上做benchmark evaluation，所有评估都在post-trained\n    model上； (2) SFT（无论clean还是contaminated）使所有信号平均下降12%—— 这是因为SFT改变了model representation\n    space，token-level信号（Min-K%++）受影响最大， 而embedding retrieval因为不依赖model内部状态反而最稳定； (3)\n    RL regime是灾难性的：所有信号AUC降至0.60以下或刚到0.60—— RL的reward hacking改变了model的输出distribution（更confident、更formulaic），\n    使得基于distribution shift的检测（Min-K%++, ConStat）几乎失效； (4) Self-Critique在RL regime下反而成为\"最佳信号\"（0.57），但仅因为其他信号更差——\n    0.57的AUC几乎没有实用价值（sensitivity+specificity之和刚过1.0）； (5) SFT clean vs contaminated的AUC差异仅0.03，说明信号的下降主要由post-training本身\n    而非contamination引起——信号检测的是\"training变化\"而非\"contamination变化\"。\n\n    '\n  tables:\n  - name: 'Table: Signal × Regime AUC Heatmap'\n    columns:\n    - signal\n    - Base\n    - SFT-Clean\n    - SFT-Contam\n    - RL\n    rows:\n    - - Embedding Retrieval\n      - 0.78\n      - 0.72\n      - 0.72\n      - 0.6\n    - - Min-K%++\n      - 0.73\n      - 0.65\n      - 0.68\n      - 0.55\n    - - ConStat\n      - 0.71\n      - 0.63\n      - 0.66\n      - 0.53\n    - - Self-Critique\n      - 0.6\n      - 0.58\n      - 0.63\n      - 0.57\n  - name: 'Table: Signal Survival Rate (AUC retention relative to Base)'\n    columns:\n    - signal\n    - SFT-Clean\n    - SFT-Contam\n    - RL\n    rows:\n    - - Embedding Retrieval\n      - 0.92\n      - 0.92\n      - 0.77\n    - - Min-K%++\n      - 0.89\n      - 0.93\n      - 0.75\n    - - ConStat\n      - 0.89\n      - 0.93\n      - 0.75\n    - - Self-Critique\n      - 0.97\n      - 1.05\n      - 0.95\n  figures_description:\n  - 'Fig: 4×4 heatmap with color coding. Clear left-to-right degradation gradient.\n    RL column almost uniformly orange/red. Self-Critique row most stable (highest\n    retention) but starts lowest.'\n  - 'Fig: Survival curves plotting AUC retention across regimes. Embedding and Min-K++\n    show steep RL drop. Self-Critique nearly flat but at low absolute level — ''stable\n    but weak''.'\n  analysis: '这个实验在reframed论文中升级为Core Contribution之一。关键叙事： \"Current detection signals\n    were designed for and evaluated on base/SFT models. We show that post-training\n    — especially RL — systematically degrades all signals below the identifiability\n    threshold established in our simulation study (exp-004).\" Self-Critique的\"stability\"是pyrrhic——它稳定在0.57-0.63的range，从未达到可用水平。\n    这直接支持\"RL regime下calibration不可行\"的结论，且解释了为什么： 不是方法不对，而是信号不存在。\n\n    '\n- name: rl_observational_case_study\n  plan_id: exp-009\n  description: 'RL-trained models的观察性案例研究。worst档下calibration在RL regime中几乎完全失效， expected\n    regret reduction接近零甚至为负。\n\n    '\n  expected_results:\n    models_evaluated: 8\n    selfcritique_auc_avg_rl: 0.57\n    rrf_auc_avg_rl: 0.59\n    calibration_mae_4pl_gamma_pp: 10.5\n    calibration_mae_uncalibrated_pp: 9.8\n    calibration_mae_remove_rescore_pp: 9.2\n    ci_width_95_avg_pp: 24.5\n    ci_coverage_95: 0.82\n    expected_regret_reduction_vs_uncalibrated: -0.03\n    expected_regret_reduction_vs_remove_rescore: -0.08\n    top5_model_selection_agreement_with_true: 0.6\n    gamma_estimates_mean: 0.08\n    gamma_ci_includes_zero_pct: 0.85\n    nearzero_gamma_clean_benchmark_check: true\n    nearzero_gamma_clean_value: 0.02\n    deepseek_r1_gamma_ci_includes_zero: true\n  result_rationale: 'RL observational case study是worst档中最清晰的negative result： (1) Signal\n    AUC在RL regime下仅0.57-0.59（exp-008已预测），这意味着exposure scores 几乎是noise，输入到IRT模型中的是garbage-in；\n    (2) 4PL+γ MAE 10.5pp反而比uncalibrated的9.8pp更差—— 模型在noisy exposure scores上\"hallucinate\"了不存在的contamination\n    effect， 做出了比不校正更差的adjustment（overcorrection on false positives，undercorrection\n    on true positives）； (3) expected regret reduction为-0.03（vs uncalibrated）和-0.08（vs\n    remove-rescore）， 即calibration使model selection决策变差了——这是因为宽CI（24.5pp）导致model rankings变得更noisy，\n    而uncalibrated scores虽然biased但至少preserves ranking well； (4) 85%的conditions下γ CI包含零，说明模型在RL\n    regime下根本检测不到contamination—— 不是\"检测到了但校正不够\"，而是\"γ与zero不可区分\"； (5) 唯一的positive result是specificity\n    check通过——clean benchmark上γ≈0.02， 说明模型至少没有在clean data上产生false positive contamination\n    detection。 但这是一个低门槛的成功。\n\n    '\n  tables:\n  - name: 'Table: RL Case Study — Calibration Method Comparison'\n    columns:\n    - method\n    - MAE_pp\n    - CI Width 95%\n    - Coverage 95%\n    - Regret Reduction\n    rows:\n    - - Uncalibrated (naive)\n      - 9.8\n      - —\n      - —\n      - —\n    - - 4PL+γ\n      - 10.5\n      - 24.5\n      - 0.82\n      - -0.03\n    - - Remove-rescore\n      - 9.2\n      - —\n      - —\n      - —\n    - - Linear regression+CI\n      - 9.9\n      - 21.0\n      - 0.85\n      - 0.01\n  - name: 'Table: Per-Model γ Estimates (RL models)'\n    columns:\n    - model\n    - gamma_mean\n    - gamma_95ci_lower\n    - gamma_95ci_upper\n    - ci_excludes_zero\n    rows:\n    - - Qwen2.5-0.5B-Instruct\n      - 0.12\n      - -0.15\n      - 0.39\n      - false\n    - - Qwen2.5-1.5B-Instruct\n      - 0.08\n      - -0.18\n      - 0.34\n      - false\n    - - Qwen2.5-3B-Instruct\n      - 0.05\n      - -0.21\n      - 0.31\n      - false\n    - - Qwen2.5-7B-Instruct\n      - 0.03\n      - -0.25\n      - 0.31\n      - false\n    - - DeepSeek-R1-Distill-1.5B\n      - 0.1\n      - -0.14\n      - 0.34\n      - false\n    - - DeepSeek-R1-Distill-7B\n      - 0.06\n      - -0.2\n      - 0.32\n      - false\n  figures_description:\n  - 'Fig: Expected regret curves. X-axis: number of models selected. Y-axis: expected\n    regret. Uncalibrated line sits below 4PL+γ line across all selection sizes. Thin\n    gray lines show bootstrap replicates — high variance, no consistent winner.'\n  - 'Fig: γ forest plot for all RL models. All CIs cross zero. Horizontal span of\n    CIs (~0.5) dwarfs point estimates (~0.05-0.12).'\n  analysis: 'RL case study提供了worst档最dramatic的result：calibration不仅不帮忙，还hurt。 这是因为在signal\n    quality低于identifiability threshold时，IRT模型的额外参数 成为了pure noise amplifier。对reframed论文的贡献有两层：\n    (1) Empirical confirmation that RL regime falls below identifiability boundary;\n    (2) Practical recommendation — \"do not attempt calibration when signal AUC < 0.60\"。\n    Specificity check的通过（clean γ≈0）是一个consolation prize—— 模型不产生false contamination\n    detection，但也检测不到real contamination。\n\n    '\n- name: prior_sensitivity\n  plan_id: exp-010\n  description: 'Prior sensitivity分析。worst档下结果对prior选择异常敏感， 暴露了model specification的fragility。\n\n    '\n  expected_results:\n    gamma_prior_n01_mae_pp: 7.8\n    gamma_prior_n005_mae_pp: 9.5\n    gamma_prior_n02_mae_pp: 7.2\n    gamma_prior_n005_gamma_mean_shrinkage_ratio: 0.45\n    gamma_prior_n02_gamma_mean_inflation_ratio: 1.35\n    mae_sensitivity_range_pp: 2.3\n    ci_coverage_sensitivity_range: 0.12\n    ci_coverage_n005: 0.85\n    ci_coverage_n01: 0.78\n    ci_coverage_n02: 0.72\n    prior_sensitivity_index: 0.38\n  result_rationale: 'prior sensitivity在worst档下远超acceptable水平： (1) N(0,0.5) tight prior强制γ向零shrink\n    45%，产生undercorrection但paradoxically 提高了coverage（0.85 vs 0.78），因为tight prior限制了CI的overconfidence；\n    (2) N(0,2) wide prior允许γ inflate 35%，MAE改善（7.2pp）但coverage恶化至0.72， 因为wider prior导致posterior更受likelihood影响，而likelihood在noisy\n    data上是misleading的； (3) MAE sensitivity range 2.3pp（across prior choices）占MAE值的~30%——\n    这意味着结果高度依赖modeler的prior choice，而不是data-driven； (4) 理想情况下（信号好、sample大），Bayesian方法应该prior-insensitive——\n    sensitivity本身就是under-identification的symptom，因为data不够informative来override prior。\n\n    '\n  tables:\n  - name: 'Table: Prior Sensitivity Comparison'\n    columns:\n    - prior\n    - gamma_mean\n    - MAE_pp\n    - Coverage 95%\n    - CI Width 95% (pp)\n    rows:\n    - - N(0, 0.5)\n      - 0.22\n      - 9.5\n      - 0.85\n      - 15.2\n    - - N(0, 1.0) [default]\n      - 0.38\n      - 7.8\n      - 0.78\n      - 19.5\n    - - N(0, 2.0)\n      - 0.51\n      - 7.2\n      - 0.72\n      - 24.8\n  figures_description:\n  - 'Fig: γ posterior distributions under three priors (overlaid density plots). Wide\n    separation between posteriors — data does not dominate prior. Clear visual evidence\n    of under-identification.'\n  analysis: 'Prior sensitivity ≥ 30% of point estimate confirms that the model is\n    in an under-identified regime. 对reframed论文：这直接maps到exp-004 identifiability sweep中的\"prior\n    sensitivity\"维度， 验证了仿真预测——在AUC<0.70时prior choice matters more than data.\n\n    '\n- name: few_examinee_regime\n  plan_id: exp-011\n  description: 'Few-examinee regime仿真研究。worst档下即使使用Growing Pains pre-estimation策略，\n    N<50时identifiability完全崩溃。\n\n    '\n  expected_results:\n    n20_gamma_rmse: 0.42\n    n20_gamma_rel_bias: 0.55\n    n20_theta_corr: 0.58\n    n20_ci_coverage_95: 0.68\n    n50_gamma_rmse: 0.28\n    n50_gamma_rel_bias: 0.38\n    n50_theta_corr: 0.72\n    n50_ci_coverage_95: 0.75\n    n100_gamma_rmse: 0.18\n    n100_gamma_rel_bias: 0.25\n    n100_theta_corr: 0.82\n    n100_ci_coverage_95: 0.8\n    n200_gamma_rmse: 0.12\n    n200_gamma_rel_bias: 0.18\n    n200_theta_corr: 0.88\n    n200_ci_coverage_95: 0.85\n    growing_pains_pretrain_improvement_n20_pct: 15\n    growing_pains_pretrain_improvement_n50_pct: 10\n    minimum_n_for_gamma_significant: 80\n    minimum_n_for_coverage_nominal: 150\n  result_rationale: 'few-examinee regime在worst档下与信号质量问题叠加： (1) N=20（现实中常见——很多benchmark只有20-50个models被评估）时，\n    γ RMSE 0.42，rel_bias 55%，θ与ground truth correlation仅0.58—— 此时模型参数估计本质上是noise；\n    (2) Growing Pains pre-estimation策略（借用大pool的item参数先验）仅改善15%， 因为bottleneck不是item参数估计而是γ-θ的joint\n    estimation—— item参数可以借用外部信息，但γ-θ的confounding是data-inherent的，无法靠先验缓解； (3) 达到γ显著（即CI排除零）需要N≥80，达到nominal\n    coverage需要N≥150—— 这两个threshold在realistic benchmark evaluation scenarios中很难满足 （HELM有~100\n    models，但大部分benchmarks的evaluated model count远少于此）； (4) 即使N=200，在worst档的信号质量下（AUC~0.65-0.70），\n    gamma_rel_bias仍有18%，coverage仅85%——仍未达到publishable quality。\n\n    '\n  tables:\n  - name: 'Table: Identifiability Metrics by Model Count (AUC=0.65)'\n    columns:\n    - N\n    - gamma_RMSE\n    - gamma_rel_bias\n    - theta_corr\n    - Coverage 95%\n    - Growing Pains Δ\n    rows:\n    - - 20\n      - 0.42\n      - 55%\n      - 0.58\n      - 68%\n      - +15%\n    - - 50\n      - 0.28\n      - 38%\n      - 0.72\n      - 75%\n      - +10%\n    - - 100\n      - 0.18\n      - 25%\n      - 0.82\n      - 80%\n      - +5%\n    - - 200\n      - 0.12\n      - 18%\n      - 0.88\n      - 85%\n      - +3%\n  figures_description:\n  - 'Fig: Identifiability surface — X: model count, Y: signal AUC, Z: γ relative bias\n    (color-coded). Clear ridge at AUC≈0.70 below which no amount of models helps sufficiently.\n    The ''green zone'' (rel_bias<10%) requires AUC>0.80 AND N>100.'\n  analysis: '这个仿真扩展与exp-004共同构成identifiability map的完整版本。 关键新发现：model count和signal\n    AUC是multiplicative而非additive—— 在AUC<0.70时，增加N的边际收益急剧递减（从N=100到N=200，改善仅7pp rel_bias）。\n    这意味着\"收集更多模型\"不是解决identifiability的viable path when signals are weak。 对论文：\"minimum\n    signal quality targets for future work\"可以被具体化为AUC×N的joint requirement。\n\n    '\n- name: observational_72b\n  plan_id: exp-012\n  description: 'Qwen2.5-72B观察性分析。worst档下大模型的信号质量进一步下降， confirm了scale-identifiability的inverse\n    relationship。\n\n    '\n  expected_results:\n    signal_auc_embedding: 0.6\n    signal_auc_minkpp: 0.56\n    signal_auc_constat: 0.54\n    signal_auc_selfcritique: 0.58\n    rrf_auc: 0.59\n    gamma_estimate: 0.04\n    gamma_ci_includes_zero: true\n    gamma_ci_width: 0.55\n    calibration_mae_pp: 11.2\n    ci_width_95_pp: 26.0\n  result_rationale: '72B模型将scale问题推向极端： (1) 72B的pretraining corpus几乎必然包含了benchmark\n    items的某种形式—— 不是传统意义的\"contamination\"而是\"知识覆盖\"，这使得所有detection signals的false positive\n    rate极高， embedding retrieval AUC降至0.60因为模型legitimately \"knows\" the content； (2)\n    γ estimate 0.04几乎为零，不是因为没有contamination而是因为unable to detect it—— 信号noise完全淹没了any\n    real signal； (3) 11.2pp MAE是worst档中最差的calibration error，因为72B的行为与smaller models\n    系统性不同（different error patterns, different item difficulty ordering）， IRT的transferability\n    across scales受到根本挑战。\n\n    '\n  tables:\n  - name: 'Table: 72B Observational Results'\n    columns:\n    - metric\n    - Qwen-72B\n    - Qwen-7B (controlled)\n    - Qwen-3B (controlled)\n    rows:\n    - - Best signal AUC\n      - 0.6\n      - 0.66\n      - 0.69\n    - - RRF AUC\n      - 0.59\n      - 0.63\n      - 0.67\n    - - γ estimate\n      - 0.04\n      - 0.25\n      - 0.34\n    - - γ CI excludes zero\n      - false\n      - Marginal (50%)\n      - true\n    - - Calibration MAE (pp)\n      - 11.2\n      - 8.5\n      - 7.8\n  figures_description:\n  - 'Fig: Scale vs signal AUC trend line from 0.5B to 72B. Clear monotonic decrease.\n    Horizontal dashed line at AUC=0.70 crossed between 1.5B and 3B scale. 72B is deep\n    in the ''unidentifiable'' zone.'\n  analysis: '72B结果是identifiability boundary story的natural endpoint： 在frontier model\n    scale上，calibration方法论本身不适用，因为\"contamination\"和\"knowledge\" 在概念层面就难以区分。这是reframed论文的strong\n    closing argument—— \"our identifiability analysis reveals that contamination-aware\n    calibration faces a fundamental scale barrier: the very models most in need of\n    calibration (large, widely trained) are precisely those where calibration is least\n    feasible.\"\n\n    '\n- name: closed_weight_2signal_mode\n  plan_id: exp-013\n  description: '2-signal degraded mode (ConStat + Self-Critique) for closed-weight\n    models. worst档下降级模式使calibration完全不可行。\n\n    '\n  expected_results:\n    two_signal_rrf_auc_100pct_dosage: 0.64\n    two_signal_rrf_auc_50pct_dosage: 0.58\n    two_signal_rrf_auc_25pct_dosage: 0.54\n    calibration_mae_2signal_pp: 10.8\n    calibration_mae_4signal_pp: 7.8\n    mae_increase_relative_2_vs_4_signal: 0.38\n    ci_width_95_2signal_pp: 25.2\n    ci_coverage_95_2signal: 0.75\n    kendall_tau_2signal: 0.48\n    gamma_ci_includes_zero_2signal_pct: 0.72\n  result_rationale: '2-signal mode在worst档下是最差的配置： (1) ConStat和Self-Critique恰好是四个信号中AUC最低的两个（exp-002），\n    它们的fusion AUC 0.64远低于identifiability threshold 0.70； (2) MAE增加38%（从7.8pp到10.8pp），符合worst档的two_signal_degraded_mae_increase_relative范围[0.35,\n    0.6]； (3) Kendall τ降至0.48——低于0.5意味着calibrated rankings与true rankings的agreement\n    不比random好多少，calibration实际上在扰乱而非改善rankings； (4) 72%的conditions下γ CI包含零，说明在closed-weight\n    scenario下 contamination detection几乎完全不可行。 这是因为closed-weight模型不提供logits和embeddings，而这两个恰好是信号质量最高的信息源——\n    没有它们，剩余信号不足以支撑any meaningful calibration。\n\n    '\n  tables:\n  - name: 'Table: 2-Signal vs 4-Signal Calibration Gap'\n    columns:\n    - metric\n    - 4-signal\n    - 2-signal\n    - degradation\n    rows:\n    - - RRF AUC (100%)\n      - 0.7\n      - 0.64\n      - -8.6%\n    - - MAE (pp)\n      - 7.8\n      - 10.8\n      - +38%\n    - - CI Width 95% (pp)\n      - 19.5\n      - 25.2\n      - +29%\n    - - Kendall τ\n      - 0.62\n      - 0.48\n      - -23%\n    - - Coverage 95%\n      - 0.78\n      - 0.75\n      - -3.8%\n  figures_description:\n  - 'Fig: Side-by-side calibration error distributions (4-signal vs 2-signal). 2-signal\n    distribution shifted right with heavier tail. Overlap region highlighted — some\n    conditions where 2-signal accidentally performs okay, but median is significantly\n    worse.'\n  analysis: '2-signal degraded mode的failure confirm了一个important practical constraint：\n    closed-weight models（GPT-4, Claude等）——恰好是most scrutinized for contamination——\n    是calibration最不可行的targets。 对reframed论文：identifiability map需要一个新维度——\"signal access\n    level\" (full access: 4 signals; closed-weight: 2 signals)， 2-signal在identifiability\n    map上的viable region极小（仅AUC>0.80且N>150，现实中不存在）。'\n",
      "numLines": 1133,
      "startLine": 1,
      "totalLines": 1133
    }
  },
  "sourceToolAssistantUUID": "0a20a376-49c6-48d2-9912-b682261200e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T17:25:03.303Z_

<details><summary>↩ Tool result · `toolu_0197L3vM87yivB2WTpR4jfTB`</summary>

```text
1	# ContamCal Experiment Plan
2	# Each experiment maps to Core Claims in paper_framing.md
3	# Priority: P0 = must-run, P1 = important, P2 = bonus
4	
5	experiments:
6	  # ============================================================
7	  # P0: Core experiments — must complete for submission
8	  # ============================================================
9	
10	  - id: exp-001
11	    name: controlled_sft_injection
12	    claim: [1]
13	    description: >
14	      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels
15	      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).
16	      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total
17	      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition
18	      for key metrics (mean ± std).
19	      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or
20	      equivalent) with controlled semantic similarity — following methodology
21	      of "Rethinking Benchmark and Contamination" (arXiv 2023). Target:
22	      high semantic similarity (cosine >0.85) but low lexical overlap
23	      (BLEU <0.3) to evade n-gram decontamination while preserving
24	      contamination effect. Quality validation: automated similarity metrics
25	      + human spot-check on 50 random pairs per benchmark.
26	    priority: P0
27	    gpu_budget_hours: 50
28	    deps: []
29	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
30	    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]
31	    seeds: 3
32	
33	  - id: exp-002
34	    name: stage1_signal_pipeline
35	    claim: [2]
36	    description: >
37	      Compute 4 detection signals on all contaminated + clean models from exp-001:
38	      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),
39	      (b) Min-K%++ membership inference,
40	      (c) ConStat performance gap (original vs paraphrased items),
41	      (d) Self-Critique entropy collapse.
42	      Output: per-model-item exposure scores for each signal.
43	    priority: P0
44	    gpu_budget_hours: 20
45	    deps: [exp-001]
46	
47	  - id: exp-003
48	    name: rrf_aggregation_ablation
49	    claim: [2]
50	    description: >
51	      RRF fusion of 4 signals into composite per-item exposure score.
52	      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only
53	      (×4), (c) calibration-based weighted RRF variant, (d) false positive
54	      injection robustness check (inject FP at rates matching Duan et al. 2024).
55	      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.
56	    priority: P0
57	    gpu_budget_hours: 2
58	    deps: [exp-002]
59	
60	  - id: exp-004
61	    name: simulation_identifiability_sweep
62	    claim: [1, 3]
63	    description: >
64	      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):
65	      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×
66	      model count (20, 50, 100, 200) ×
67	      prior strength (N(0,0.5), N(0,1), N(0,2)) ×
68	      exposure type (binary, continuous).
69	      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior
70	      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes
71	      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as
72	      "cannot distinguish no contamination from moderate contamination."
73	      N_items=300 fixed (per MVP finding).
74	      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)
75	      — prior × N_models dimensions already in sweep grid. Growing Pains
76	      pre-estimation sub-experiment: at N_models=20/50, compare flat prior
77	      vs informative prior from pre-estimated item parameters.
78	      Also includes Fisher Information matrix analysis: derive approximate
79	      analytical relationship between signal AUC, N_models, and γ
80	      recoverability. Distinguish structural identifiability (parameters
81	      uniquely determined) from practical identifiability (estimation
82	      quality sufficient for decisions). Provides theoretical grounding
83	      for the empirical AUC ≥ 0.70 threshold.
84	    priority: P0
85	    gpu_budget_hours: 0
86	    deps: []
87	    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.
88	
89	  - id: exp-005
90	    name: noise_propagation_analysis
91	    claim: [3]
92	    description: >
93	      Two parts:
94	      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure
95	      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true
96	      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.
97	      This propagates Stage 1 uncertainty into posteriors automatically.
98	      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.
99	      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched
100	      levels, re-fit standard model, measure CI widening for γ and θ.
101	      Both parts inform whether measurement error model closes the coverage gap.
102	    priority: P0
103	    gpu_budget_hours: 0
104	    deps: [exp-002, exp-004]
105	    note: CPU only
106	
107	  - id: exp-006
108	    name: irt_calibration_and_baselines
109	    claim: [1, 3]
110	    description: >
111	      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.
112	      TWO model variants: (a) global γ (single γ across all benchmarks),
113	      (b) per-benchmark γ_k (separate γ per benchmark). Report both.
114	      Per-benchmark γ_k addresses Dream reviewer concern about benchmark-
115	      heterogeneous contamination effects (3× range in inflation).
116	      IRT fitted per-benchmark (not jointly) to reduce local independence
117	      violation scope. Posterior predictive checks on item-level residual
118	      correlations to assess local independence empirically.
119	      Compute calibrated scores via exposure=0 counterfactual with CIs.
120	      Compare against 7 baselines:
121	      (0) Raw — no adjustment (anchor),
122	      (1) remove-and-rescore (drop flagged items),
123	      (2) single-signal 2PL+γ (best signal only, simpler IRT),
124	      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),
125	      (4) linear exposure regression + bootstrap CI (simplest post-hoc),
126	      (5) Emperor's mitigation: rephrasing + option shuffling,
127	      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method
128	          producing adjusted accuracy; must include or reviewers will reject.
129	      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,
130	      Kendall τ, dose-response monotonicity.
131	      Report mean ± std across 3 seeds (matched to exp-001 seeds).
132	    priority: P0
133	    gpu_budget_hours: 8
134	    deps: [exp-003]
135	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
136	    seeds: 3
137	
138	  # ============================================================
139	  # P1: Important — run if time/GPU permit
140	  # ============================================================
141	
142	  - id: exp-007
143	    name: scale_bridging_7b
144	    claim: [1]
145	    description: >
146	      Qwen2.5-7B controlled SFT injection at 5 dosage levels.
147	      Validates calibration accuracy scales to larger models.
148	      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).
149	    priority: P1
150	    gpu_budget_hours: 30
151	    deps: [exp-001]
152	
153	  - id: exp-008
154	    name: signal_survival_analysis
155	    claim: [2]
156	    description: >
157	      Systematic evaluation of detection signal reliability across training regimes.
158	      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,
159	      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat
160	      degrade post-RL (per fragility paper arXiv 2510.02386).
161	      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified
162	      this as the most genuinely novel finding).
163	    priority: P0
164	    gpu_budget_hours: 10
165	    deps: [exp-002]
166	
167	  - id: exp-014
168	    name: multi_family_validation
169	    claim: [1]
170	    description: >
171	      Controlled SFT injection on at least one non-Qwen model family
172	      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).
173	      Validates that identifiability boundaries and calibration accuracy
174	      generalize beyond Qwen2.5. Addresses Dream reviewer concern about
175	      single model family limiting generalizability (flagged [M][W]).
176	    priority: P1
177	    gpu_budget_hours: 15
178	    deps: [exp-001]
179	
180	  - id: exp-009
181	    name: rl_observational_case_study
182	    claim: [2, 3]
183	    description: >
184	      Apply Self-Critique + available signals to existing RL-trained models:
185	      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.
186	      Fit IRT with appropriately wider CIs. Expected regret quantification:
187	      compare uncalibrated vs calibrated vs remove-rescore for top-5 model
188	      selection. Framed as observational — directional external validity,
189	      not full quantitative validation. Near-zero γ check on known-clean
190	      benchmark (specificity test).
191	    priority: P1
192	    gpu_budget_hours: 15
193	    deps: [exp-006, exp-008]
194	
195	  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.
196	  # Prior × N_models dimensions already covered in the sweep grid.
197	
198	  # ============================================================
199	  # P2: Bonus — adds breadth if resources allow
200	  # ============================================================
201	
202	  - id: exp-012
203	    name: observational_72b
204	    claim: [1]
205	    description: >
206	      Qwen2.5-72B observational analysis (inference only, no SFT).
207	      Extends ecological validity to frontier model scale.
208	    priority: P2
209	    gpu_budget_hours: 15
210	    deps: [exp-006]
211	
212	  - id: exp-013
213	    name: closed_weight_2signal_mode
214	    claim: [2]
215	    description: >
216	      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)
217	      for closed-weight models. Ablation quantifying 2-signal vs 4-signal
218	      calibration accuracy gap.
219	    priority: P2
220	    gpu_budget_hours: 5
221	    deps: [exp-003]
222	
223	# ============================================================
224	# GPU Budget Summary
225	# ============================================================
226	gpu_budget:
227	  P0_hours: 90
228	  P1_hours: 60
229	  P2_hours: 20
230	  buffer_hours: 30
231	  total_hours: 200
232	  note: >
233	    CPU-only experiments (exp-004, exp-005, exp-011) excluded.
234	    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.
235	    Requires 2-4× H100/A100-80G for parallel SFT runs.
236	    EMNLP 2026 ARR May 25 sprint (12 days from May 13):
237	    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)
238	    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized
239	    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule
240	
241	# Multi-seed protocol:
242	# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics
243	# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)
244	# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)
245	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "277925dc-1460-4d09-984b-2d7289341b42",
  "isSidechain": false,
  "promptId": "36e7f43a-5d9e-44f9-82f4-4f17b0038e98",
  "type": "user",
  "uuid": "51f87f7f-7aab-400c-8bb1-9187600a8632",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml",
      "content": "# ContamCal Experiment Plan\n# Each experiment maps to Core Claims in paper_framing.md\n# Priority: P0 = must-run, P1 = important, P2 = bonus\n\nexperiments:\n  # ============================================================\n  # P0: Core experiments — must complete for submission\n  # ============================================================\n\n  - id: exp-001\n    name: controlled_sft_injection\n    claim: [1]\n    description: >\n      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).\n      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total\n      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition\n      for key metrics (mean ± std).\n      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or\n      equivalent) with controlled semantic similarity — following methodology\n      of \"Rethinking Benchmark and Contamination\" (arXiv 2023). Target:\n      high semantic similarity (cosine >0.85) but low lexical overlap\n      (BLEU <0.3) to evade n-gram decontamination while preserving\n      contamination effect. Quality validation: automated similarity metrics\n      + human spot-check on 50 random pairs per benchmark.\n    priority: P0\n    gpu_budget_hours: 50\n    deps: []\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]\n    seeds: 3\n\n  - id: exp-002\n    name: stage1_signal_pipeline\n    claim: [2]\n    description: >\n      Compute 4 detection signals on all contaminated + clean models from exp-001:\n      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n      (b) Min-K%++ membership inference,\n      (c) ConStat performance gap (original vs paraphrased items),\n      (d) Self-Critique entropy collapse.\n      Output: per-model-item exposure scores for each signal.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [exp-001]\n\n  - id: exp-003\n    name: rrf_aggregation_ablation\n    claim: [2]\n    description: >\n      RRF fusion of 4 signals into composite per-item exposure score.\n      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only\n      (×4), (c) calibration-based weighted RRF variant, (d) false positive\n      injection robustness check (inject FP at rates matching Duan et al. 2024).\n      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-002]\n\n  - id: exp-004\n    name: simulation_identifiability_sweep\n    claim: [1, 3]\n    description: >\n      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):\n      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×\n      model count (20, 50, 100, 200) ×\n      prior strength (N(0,0.5), N(0,1), N(0,2)) ×\n      exposure type (binary, continuous).\n      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior\n      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as\n      \"cannot distinguish no contamination from moderate contamination.\"\n      N_items=300 fixed (per MVP finding).\n      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)\n      — prior × N_models dimensions already in sweep grid. Growing Pains\n      pre-estimation sub-experiment: at N_models=20/50, compare flat prior\n      vs informative prior from pre-estimated item parameters.\n      Also includes Fisher Information matrix analysis: derive approximate\n      analytical relationship between signal AUC, N_models, and γ\n      recoverability. Distinguish structural identifiability (parameters\n      uniquely determined) from practical identifiability (estimation\n      quality sufficient for decisions). Provides theoretical grounding\n      for the empirical AUC ≥ 0.70 threshold.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n\n  - id: exp-005\n    name: noise_propagation_analysis\n    claim: [3]\n    description: >\n      Two parts:\n      (A) Measurement error model (PRIMARY): extend Stan model to treat exposure\n      as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is latent true\n      contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n      This propagates Stage 1 uncertainty into posteriors automatically.\n      Compare coverage (50%/80%/95%) vs point-estimate exposure baseline.\n      (B) Post-hoc noise injection: inject Gaussian noise at 1×/1.5×/2× matched\n      levels, re-fit standard model, measure CI widening for γ and θ.\n      Both parts inform whether measurement error model closes the coverage gap.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-002, exp-004]\n    note: CPU only\n\n  - id: exp-006\n    name: irt_calibration_and_baselines\n    claim: [1, 3]\n    description: >\n      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.\n      TWO model variants: (a) global γ (single γ across all benchmarks),\n      (b) per-benchmark γ_k (separate γ per benchmark). Report both.\n      Per-benchmark γ_k addresses Dream reviewer concern about benchmark-\n      heterogeneous contamination effects (3× range in inflation).\n      IRT fitted per-benchmark (not jointly) to reduce local independence\n      violation scope. Posterior predictive checks on item-level residual\n      correlations to assess local independence empirically.\n      Compute calibrated scores via exposure=0 counterfactual with CIs.\n      Compare against 7 baselines:\n      (0) Raw — no adjustment (anchor),\n      (1) remove-and-rescore (drop flagged items),\n      (2) single-signal 2PL+γ (best signal only, simpler IRT),\n      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),\n      (4) linear exposure regression + bootstrap CI (simplest post-hoc),\n      (5) Emperor's mitigation: rephrasing + option shuffling,\n      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method\n          producing adjusted accuracy; must include or reviewers will reject.\n      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,\n      Kendall τ, dose-response monotonicity.\n      Report mean ± std across 3 seeds (matched to exp-001 seeds).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [exp-003]\n    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]\n    seeds: 3\n\n  # ============================================================\n  # P1: Important — run if time/GPU permit\n  # ============================================================\n\n  - id: exp-007\n    name: scale_bridging_7b\n    claim: [1]\n    description: >\n      Qwen2.5-7B controlled SFT injection at 5 dosage levels.\n      Validates calibration accuracy scales to larger models.\n      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [exp-001]\n\n  - id: exp-008\n    name: signal_survival_analysis\n    claim: [2]\n    description: >\n      Systematic evaluation of detection signal reliability across training regimes.\n      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat\n      degrade post-RL (per fragility paper arXiv 2510.02386).\n      ELEVATED to Core Contribution 2 per Dream review (all 3 tiers identified\n      this as the most genuinely novel finding).\n    priority: P0\n    gpu_budget_hours: 10\n    deps: [exp-002]\n\n  - id: exp-014\n    name: multi_family_validation\n    claim: [1]\n    description: >\n      Controlled SFT injection on at least one non-Qwen model family\n      (Llama-3.2-1B or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%).\n      Validates that identifiability boundaries and calibration accuracy\n      generalize beyond Qwen2.5. Addresses Dream reviewer concern about\n      single model family limiting generalizability (flagged [M][W]).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-001]\n\n  - id: exp-009\n    name: rl_observational_case_study\n    claim: [2, 3]\n    description: >\n      Apply Self-Critique + available signals to existing RL-trained models:\n      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.\n      Fit IRT with appropriately wider CIs. Expected regret quantification:\n      compare uncalibrated vs calibrated vs remove-rescore for top-5 model\n      selection. Framed as observational — directional external validity,\n      not full quantitative validation. Near-zero γ check on known-clean\n      benchmark (specificity test).\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [exp-006, exp-008]\n\n  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.\n  # Prior × N_models dimensions already covered in the sweep grid.\n\n  # ============================================================\n  # P2: Bonus — adds breadth if resources allow\n  # ============================================================\n\n  - id: exp-012\n    name: observational_72b\n    claim: [1]\n    description: >\n      Qwen2.5-72B observational analysis (inference only, no SFT).\n      Extends ecological validity to frontier model scale.\n    priority: P2\n    gpu_budget_hours: 15\n    deps: [exp-006]\n\n  - id: exp-013\n    name: closed_weight_2signal_mode\n    claim: [2]\n    description: >\n      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n      for closed-weight models. Ablation quantifying 2-signal vs 4-signal\n      calibration accuracy gap.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [exp-003]\n\n# ============================================================\n# GPU Budget Summary\n# ============================================================\ngpu_budget:\n  P0_hours: 90\n  P1_hours: 60\n  P2_hours: 20\n  buffer_hours: 30\n  total_hours: 200\n  note: >\n    CPU-only experiments (exp-004, exp-005, exp-011) excluded.\n    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.\n    Requires 2-4× H100/A100-80G for parallel SFT runs.\n    EMNLP 2026 ARR May 25 sprint (12 days from May 13):\n    - With 4× H100: P0 in ~4 days, P1 in ~3 days, total ~8 days (fits deadline)\n    - With 2× H100: P0 in ~7 days, P1 in ~4 days, tight but feasible if parallelized\n    - Day-8 contingency: reduce benchmarks to MMLU + GSM8K if behind schedule\n\n# Multi-seed protocol:\n# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics\n# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)\n# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)\n",
      "numLines": 245,
      "startLine": 1,
      "totalLines": 245
    }
  },
  "sourceToolAssistantUUID": "277925dc-1460-4d09-984b-2d7289341b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T17:25:02.954Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P24YLqFvyi5yQtMuaXnHFc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1910d17f-0b57-49b8-af9b-5da2296ffc2d",
  "isSidechain": false,
  "requestId": "req_011CazxWkLB2kCTEe3T5t4Wc",
  "type": "assistant",
  "uuid": "4466a8ef-669a-4fa9-ad10-15ac09539319",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqCpSwtfpE2YfCCaPGFmtd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 25120,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 25120,
          "cache_creation_input_tokens": 2111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2111
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

_source line 17 · 2026-05-13T17:25:02.975Z_

<details><summary>↩ Tool result · `toolu_01P24YLqFvyi5yQtMuaXnHFc`</summary>

```text
1	tier: best
2	narrative_guidance: '原始framing完全成立：ContamCal是benchmark contamination的"statistical
3	  safety net"， 三条claims按原始强度表述。Headline: "ContamCal recovers true performance within
4	  2pp MAE with 93% CI coverage, while naive scores overestimate by 8-12pp." RL宽CI叙事自然成立——"wide
5	  CIs are the correct answer"用expected regret量化证明。投AAAI无需调整framing。
6	
7	  '
8	imagined_experiments:
9	- name: controlled_sft_injection
10	  plan_id: exp-001
11	  description: 'Qwen2.5-0.5B/1.5B/3B × 5 dosage levels (0%/5%/25%/50%/100%) SFT注入，
12	    生成15个contaminated/clean模型对作为ground truth。
13	
14	    '
15	  expected_results:
16	    sft_runs_completed: 15
17	    dosage_0pct_acc_delta_mmlu_pp: 0.0
18	    dosage_5pct_acc_inflation_mmlu_pp: 2.1
19	    dosage_25pct_acc_inflation_mmlu_pp: 5.8
20	    dosage_50pct_acc_inflation_mmlu_pp: 9.3
21	    dosage_100pct_acc_inflation_mmlu_pp: 12.6
22	    dosage_25pct_acc_inflation_gsm8k_pp: 4.2
23	    dosage_25pct_acc_inflation_arc_pp: 5.1
24	    dosage_25pct_acc_inflation_humaneval_pp: 7.5
25	    scale_0_5B_mean_inflation_50pct_pp: 10.8
26	    scale_1_5B_mean_inflation_50pct_pp: 9.1
27	    scale_3B_mean_inflation_50pct_pp: 8.2
28	    dose_response_spearman_across_all: 0.97
29	    convergence_failures: 0
30	  result_rationale: 'best档下SFT注入实验完全按预期工作。paraphrase-based injection在5%剂量时已产生可测量的2pp
31	    inflation， 100%剂量下MMLU膨胀达12.6pp，与Emperor''s New Clothes报告的8-15pp范围一致。 较小模型(0.5B)受contamination影响更大（memorization
32	    capacity占比更高）， 3B模型因能力更强、泛化更好而inflation略低。GSM8K因reasoning chain结构使得 memorization效果弱于纯knowledge
33	    recall的MMLU。HumanEval inflation最高因为 code solutions更容易被精确记忆。dose-response严格单调（spearman=0.97），
34	    为后续IRT建模提供理想的ground truth梯度。
35	
36	    '
37	  tables:
38	  - name: 'Table 1: Accuracy Inflation (pp) by Model Scale × Dosage × Benchmark'
39	    rows: 60
40	    columns:
41	    - model
42	    - benchmark
43	    - dosage
44	    - clean_acc
45	    - contaminated_acc
46	    - inflation_pp
47	  figures_description:
48	  - 'Fig 1: Dose-response curves (dosage vs inflation) for each model×benchmark combination,
49	    12 panels, showing strict monotonicity'
50	  analysis: '所有15个SFT run成功收敛。inflation幅度在MMLU上与文献一致。 关键观察：inflation并非线性——25%→50%的增量大于5%→25%，表明contamination效果存在加速区间，
51	    支持非线性4PL建模的必要性。跨benchmark一致性强，为Claim 1提供坚实的ground truth基础。
52	
53	    '
54	- name: stage1_signal_pipeline
55	  plan_id: exp-002
56	  description: '在exp-001的所有模型上计算4种检测信号：embedding retrieval, Min-K%++, ConStat, Self-Critique。输出per-model-item
57	    exposure scores。
58	
59	    '
60	  expected_results:
61	    embedding_retrieval_auc_sft_mean: 0.88
62	    mink_pp_auc_sft_mean: 0.84
63	    constat_auc_sft_mean: 0.82
64	    self_critique_auc_sft_mean: 0.79
65	    embedding_retrieval_auc_at_5pct_dosage: 0.76
66	    mink_pp_auc_at_5pct_dosage: 0.71
67	    constat_auc_at_5pct_dosage: 0.68
68	    self_critique_auc_at_5pct_dosage: 0.66
69	    signal_pairwise_rank_corr_max: 0.52
70	    signal_pairwise_rank_corr_min: 0.28
71	    items_with_all4_signals_agree_contaminated_pct: 0.73
72	    items_with_disagreement_pct: 0.27
73	  result_rationale: 'best档下所有4个信号都有效但各有侧重。Embedding retrieval AUC最高(0.88)因为 paraphrase-based
74	    injection保留了语义相似性，FAISS能直接捕获。Min-K%++次之(0.84) 因为SFT后model perplexity在seen items上显著降低。ConStat(0.82)通过original
75	    vs paraphrase performance gap检测有效但受paraphrase质量影响。Self-Critique最低(0.79) 因为依赖模型自身判断，噪声更大，但仍远超chance。在低剂量(5%)时所有信号AUC下降约0.1，
76	    这是合理的——更少的contaminated items意味着更弱的统计信号。 信号间相关性适中(0.28-0.52)，说明它们捕获的是complementary
77	    information， 为RRF融合提供理想条件。
78	
79	    '
80	  tables:
81	  - name: 'Table 2: Per-Signal AUC by Model × Dosage'
82	    rows: 60
83	    columns:
84	    - model
85	    - dosage
86	    - embedding_auc
87	    - mink_auc
88	    - constat_auc
89	    - selfcritique_auc
90	  figures_description:
91	  - 'Fig 2: Signal AUC heatmap (signal × dosage), averaged across models and benchmarks'
92	  - 'Fig 3: Pairwise signal rank correlation matrix (4×4)'
93	  analysis: '信号质量全面达到best档预期。关键发现：信号间低-中等相关性(mean=0.38)证实 complementarity假设，为RRF融合奠定基础。HumanEval上embedding
94	    retrieval AUC 特别高(0.92)因为code的语义embedding更具区分性。
95	
96	    '
97	- name: rrf_aggregation_ablation
98	  plan_id: exp-003
99	  description: 'RRF融合4信号为composite exposure score。消融实验：RRF vs rank averaging, 单信号,
100	    calibration-weighted RRF, FP注入鲁棒性, 2-signal降级模式。
101	
102	    '
103	  expected_results:
104	    rrf_4signal_auc: 0.87
105	    rank_averaging_auc: 0.84
106	    best_single_signal_auc: 0.88
107	    calibration_weighted_rrf_auc: 0.86
108	    rrf_minus_best_single_delta_auc: -0.01
109	    rrf_auc_at_fp_rate_10pct: 0.84
110	    rrf_auc_at_fp_rate_20pct: 0.8
111	    degraded_2signal_auc: 0.78
112	    rrf_4signal_vs_2signal_delta: 0.09
113	    rrf_exposure_score_spearman_with_true_dosage: 0.91
114	    rank_stability_bootstrap_cv: 0.04
115	  result_rationale: 'best档下RRF融合AUC(0.87)接近最好的单信号(embedding 0.88)但关键优势在于鲁棒性： RRF在所有benchmark上都稳定达到0.85+，而单信号表现波动大（embedding在GSM8K上可能
116	    降到0.80，ConStat在HumanEval上可能降到0.75）。RRF比rank averaging高3pp因为 reciprocal rank weighting对高置信排名给予更大权重。Calibration-weighted
117	    RRF略低于 vanilla RRF因为权重估计引入了额外noise，且在best档的高信号质量下vanilla RRF已足够。 FP注入10%时AUC仅降3pp，20%时降7pp，证明graceful
118	    degradation。 2-signal模式(ConStat+Self-Critique)AUC=0.78，比4-signal低9pp但仍远超chance，
119	    满足closed-weight场景的可用性。exposure score与true dosage的spearman=0.91 证明RRF输出确实捕获了contamination程度的有序信息。
120	
121	    '
122	  tables:
123	  - name: 'Table 3: RRF Ablation Results'
124	    rows: 8
125	    columns:
126	    - method
127	    - auc_mmlu
128	    - auc_gsm8k
129	    - auc_arc
130	    - auc_humaneval
131	    - auc_mean
132	    - auc_std
133	  - name: 'Table 4: FP Injection Robustness'
134	    rows: 4
135	    columns:
136	    - fp_rate
137	    - rrf_auc
138	    - delta_from_clean
139	  figures_description:
140	  - 'Fig 4: Signal dropout ablation bar chart — AUC by combination (4-signal, each
141	    3-signal, each single, 2-signal degraded)'
142	  - 'Fig 5: RRF exposure score vs true dosage scatter plot with Spearman annotation'
143	  analysis: 'RRF fusion的核心价值不在于AUC绝对值（最好的单信号可能匹配），而在于跨benchmark、 跨模型的一致性和FP鲁棒性。这直接支持Claim
144	    2的"outperforming any single signal"—— 含义是worst-case performance更优，而非mean AUC更高。2-signal降级模式AUC=0.78
145	    为closed-weight实用性提供了有力支撑。
146	
147	    '
148	- name: noise_propagation_analysis
149	  plan_id: exp-005
150	  description: '校准noise注入到exposure scores中：估计per-item FP/FN率， 注入matched/1.5×/2×高斯噪声，重新拟合IRT，测量CI宽化。
151	
152	    '
153	  expected_results:
154	    selfcritique_estimated_fp_rate: 0.12
155	    selfcritique_estimated_fn_rate: 0.18
156	    matched_noise_ci_width_gamma_pp: 5.2
157	    noise_1_5x_ci_width_gamma_pp: 6.8
158	    noise_2x_ci_width_gamma_pp: 8.9
159	    matched_noise_ci_coverage_95: 0.94
160	    noise_1_5x_ci_coverage_95: 0.96
161	    noise_2x_ci_coverage_95: 0.97
162	    gamma_rel_bias_at_matched_noise: 0.06
163	    gamma_rel_bias_at_2x_noise: 0.09
164	    theta_corr_at_matched_noise: 0.94
165	    theta_corr_at_2x_noise: 0.89
166	    measurement_error_model_dic_improvement: 12.3
167	  result_rationale: 'best档下noise propagation表现理想：随着noise增加，CI合理宽化（5.2→8.9pp）而非崩溃，
168	    coverage从94%略升至97%（略过覆盖而非欠覆盖）。这说明Bayesian posterior正确地将 exposure score uncertainty吸收进了参数不确定性。gamma相对偏差从0.06增到0.09，
169	    表明点估计稳健性在2×noise下仍可接受。theta相关性从0.94降至0.89，下降幅度合理—— 更多noise意味着contamination信号更弱，ability估计回退向vanilla
170	    IRT。 Self-Critique的FP=12%/FN=18%在best档下是合理的——比embedding差但比random好得多。 measurement
171	    error扩展模型DIC改善12.3说明显式建模exposure noise有统计意义上的价值。
172	
173	    '
174	  tables:
175	  - name: 'Table 5: Noise Propagation Results'
176	    rows: 4
177	    columns:
178	    - noise_level
179	    - gamma_mean
180	    - gamma_rel_bias
181	    - ci_width_pp
182	    - ci_coverage_95
183	    - theta_corr
184	  figures_description:
185	  - 'Fig 6: CI width vs noise level line plot, with coverage annotated at each point'
186	  - 'Fig 7: θ recovery correlation scatterplots at 3 noise levels (1×, 1.5×, 2×)'
187	  analysis: '核心结论：4PL+γ的Bayesian formulation天然支持noise propagation——更noisy的exposure
188	    scores产生更宽的CI而不是更差的点估计。这直接支持Claim 3，也为RL regime下 Self-Critique-only信号的wider CIs提供了机制解释。
189	
190	    '
191	- name: irt_calibration_and_baselines
192	  plan_id: exp-006
193	  description: '在exp-001/003的controlled数据上拟合4PL+γ IRT (Stan NUTS)， 计算calibrated scores，与5个baselines比较，评估5个指标。
194	
195	    '
196	  expected_results:
197	    contam_cal_mae_pp_mmlu: 1.8
198	    contam_cal_mae_pp_gsm8k: 2.1
199	    contam_cal_mae_pp_arc: 1.6
200	    contam_cal_mae_pp_humaneval: 2.4
201	    contam_cal_mae_pp_mean: 1.97
202	    contam_cal_ci_coverage_95: 0.93
203	    contam_cal_ci_coverage_80: 0.84
204	    contam_cal_ci_coverage_50: 0.55
205	    contam_cal_ci_width_95_pp: 5.8
206	    contam_cal_kendall_tau: 0.91
207	    contam_cal_dose_response_spearman: 0.96
208	    baseline_remove_rescore_mae_pp: 4.2
209	    baseline_single_2plg_mae_pp: 3.8
210	    baseline_vanilla_4pl_mae_pp: 6.1
211	    baseline_linear_regression_mae_pp: 3.5
212	    baseline_emperor_mitigation_mae_pp: 5.7
213	    best_baseline_mae_pp: 3.5
214	    margin_over_best_baseline_mae_relative: 0.44
215	    naive_score_overestimation_50pct_dosage_pp: 9.3
216	    gamma_posterior_mean: 0.42
217	    gamma_posterior_sd: 0.08
218	    gamma_rel_bias_real_data: 0.06
219	    theta_corr_with_ground_truth: 0.95
220	    theta_gamma_posterior_corr: 0.31
221	    nuts_divergent_pct: 0.0
222	    nuts_max_rhat: 1.005
223	    nuts_ess_min: 800
224	  result_rationale: 'best档核心实验。4PL+γ MAE=1.97pp完全复现仿真表现——真实SFT数据上的contamination 结构与仿真假设匹配良好。MMLU
225	    MAE最低(1.8pp)因为item数量最多(14K)提供了最强的 统计功效；HumanEval最高(2.4pp)因为item少且code execution评分的binary
226	    nature 增加了noise。93% coverage接近nominal 95%，略低是因为real data的item heterogeneity 比仿真更大，但仍在可接受范围。CI宽度5.8pp在sharpness和coverage间取得了好的平衡。
227	
228	    Baselines方面：vanilla 4PL(无γ)MAE=6.1pp最差，因为完全忽略contamination， 证明contamination covariate是必要的。Emperor''s
229	    mitigation MAE=5.7pp次差， 与ICML 2025发现一致——mitigation strategies确实不够有效。Linear regression
230	    MAE=3.5pp 是最好的baseline，但仍比ContamCal差44%——IRT的优势在于non-linear item response 建模和proper
231	    uncertainty propagation。Remove-rescore MAE=4.2pp受限于binary flagging丢失了contamination程度信息。Single-signal
232	    2PL+γ MAE=3.8pp表明 signal fusion和4PL复杂度各贡献了一部分改善。
233	
234	    θ-γ posterior correlation=0.31 < 0.4阈值，证实identifiability。 gamma rel_bias=0.06与仿真的0.068几乎一致。NUTS诊断完美——无divergence，
235	    Rhat<1.01，ESS>800。
236	
237	    '
238	  tables:
239	  - name: 'Table 6 (Main Result): Calibration Performance — ContamCal vs 5 Baselines'
240	    rows: 6
241	    columns:
242	    - method
243	    - mae_mmlu
244	    - mae_gsm8k
245	    - mae_arc
246	    - mae_humaneval
247	    - mae_mean
248	    - ci_coverage_95
249	    - ci_width_95
250	    - kendall_tau
251	  - name: 'Table 7: Per-Benchmark Detailed Metrics'
252	    rows: 4
253	    columns:
254	    - benchmark
255	    - mae_pp
256	    - coverage_50
257	    - coverage_80
258	    - coverage_95
259	    - ci_width_95_pp
260	    - kendall_tau
261	    - dose_response_spearman
262	  - name: 'Table 8: MCMC Diagnostics'
263	    rows: 4
264	    columns:
265	    - benchmark
266	    - divergent_pct
267	    - max_rhat
268	    - min_ess
269	    - fit_time_sec
270	  figures_description:
271	  - 'Fig 8 (Main Figure): Calibrated vs true accuracy scatter plot, all benchmarks,
272	    with 95% CI error bars, diagonal reference line'
273	  - 'Fig 9: MAE bar chart — ContamCal vs 5 baselines, per benchmark'
274	  - 'Fig 10: Dose-response curves — γ effect size vs contamination dosage, 4 benchmark
275	    panels'
276	  - 'Fig 11: Coverage calibration plot — nominal vs empirical coverage at 50/80/95%
277	    levels'
278	  analysis: '这是论文的核心结果表。MAE 1.97pp vs best baseline 3.5pp (44% relative improvement)
279	    提供了Claim 1的强有力支撑。93% coverage证明CI可靠。headline result可直接写为 "ContamCal recovers true
280	    performance within 2pp MAE with 93% CI coverage, while naive scores overestimate
281	    by 8-12pp." Kendall τ=0.91证明model ranking 在calibration后基本保持正确——contamination改变的是绝对分数而非相对排名，
282	    但ContamCal在absolute calibration上的优势对于跨benchmark比较至关重要。
283	
284	    '
285	- name: scale_bridging_7b
286	  plan_id: exp-007
287	  description: 'Qwen2.5-7B在5个dosage水平下的controlled SFT注入，验证calibration在更大模型上的有效性。
288	
289	    '
290	  expected_results:
291	    dosage_25pct_acc_inflation_mmlu_pp: 4.8
292	    dosage_50pct_acc_inflation_mmlu_pp: 7.6
293	    dosage_100pct_acc_inflation_mmlu_pp: 10.2
294	    contam_cal_mae_pp_mean_7b: 2.2
295	    contam_cal_ci_coverage_95_7b: 0.92
296	    contam_cal_kendall_tau_7b: 0.89
297	    mae_increase_vs_3b_pp: 0.3
298	    gamma_mean_7b: 0.38
299	    dose_response_spearman_7b: 0.94
300	  result_rationale: 'best档下7B模型表现略弱于0.5-3B但仍在acceptable范围内。7B的inflation略低于小模型 (50%
301	    dosage: 7.6pp vs 9.3pp mean for smaller)因为7B的更强泛化能力意味着 contamination的relative
302	    contribution更小。MAE略增至2.2pp(+0.3pp vs 3B)因为 7B模型的item response pattern更复杂，但仍远优于baselines。gamma估计值0.38略低于
303	    小模型的0.42，反映了contamination对larger model的较小相对效应。 Coverage 92%和Kendall τ=0.89仍然强劲，证明ContamCal可扩展到7B规模。
304	
305	    '
306	  tables:
307	  - name: 'Table 9: 7B Scale Bridging Results'
308	    rows: 5
309	    columns:
310	    - dosage
311	    - inflation_pp
312	    - contam_cal_mae_pp
313	    - ci_coverage_95
314	    - kendall_tau
315	  figures_description:
316	  - 'Fig 12: MAE vs model scale line plot (0.5B, 1.5B, 3B, 7B) showing graceful degradation'
317	  analysis: '7B结果证明ContamCal从小模型到中等规模模型的可扩展性。MAE增加有限(+0.3pp) 且符合理论预期——更大的模型有更复杂的ability
318	    landscape但contamination的相对效应更小。
319	
320	    '
321	- name: signal_survival_analysis
322	  plan_id: exp-008
323	  description: '检测信号在不同训练regime下的可靠性系统评估。 Signal × regime AUC heatmap: 4 signals ×
324	    {base, SFT-clean, SFT-contaminated, RL-post-trained}。
325	
326	    '
327	  expected_results:
328	    embedding_auc_base: 0.9
329	    embedding_auc_sft_clean: 0.51
330	    embedding_auc_sft_contam: 0.88
331	    embedding_auc_rl: 0.55
332	    mink_auc_base: 0.86
333	    mink_auc_sft_clean: 0.53
334	    mink_auc_sft_contam: 0.84
335	    mink_auc_rl: 0.58
336	    constat_auc_base: 0.5
337	    constat_auc_sft_clean: 0.5
338	    constat_auc_sft_contam: 0.82
339	    constat_auc_rl: 0.67
340	    selfcritique_auc_base: 0.5
341	    selfcritique_auc_sft_clean: 0.5
342	    selfcritique_auc_sft_contam: 0.79
343	    selfcritique_auc_rl: 0.72
344	    signal_survival_rl_best: Self-Critique
345	    signal_survival_rl_second: ConStat
346	  result_rationale: 'best档下信号存活模式清晰：embedding和Min-K%++在SFT-contaminated上表现强劲 (0.88/0.84)但在RL后严重降级(0.55/0.58)——RL的policy
347	    gradient更新破坏了 token-level memorization pattern，使得perplexity-based信号失效。 ConStat在RL后保留AUC=0.67因为它测量的是performance
348	    gap(original vs paraphrase) 这一higher-level信号，不依赖model internals。Self-Critique在RL后最强(0.72)
349	    因为它利用模型的reasoning能力来自我评估，RL强化了这种元认知能力而非削弱。 base模型和SFT-clean模型上ConStat和Self-Critique接近chance(0.50)是正确的——
350	    没有contamination时不应有信号（specificity验证）。 这个heatmap直接支持RRF fusion的必要性：没有任何单一信号在所有regime下都最优。
351	
352	    '
353	  tables:
354	  - name: 'Table 10 (Supporting Contribution): Signal × Regime AUC Heatmap'
355	    rows: 4
356	    columns:
357	    - signal
358	    - base
359	    - sft_clean
360	    - sft_contam
361	    - rl_post_trained
362	  figures_description:
363	  - 'Fig 13: Signal survival heatmap (4×4 matrix, color-coded by AUC)'
364	  - 'Fig 14: Per-signal AUC degradation from SFT→RL, paired bar chart'
365	  analysis: '这是论文的Supporting Contribution 5。关键insight：RL post-training创造了一个 "signal
366	    desert"——只有Self-Critique和ConStat存活。这解释了为什么RL regime 需要更宽的CI（更少信号→更大不确定性），同时也为2-signal
367	    degraded mode提供了 empirical justification。
368	
369	    '
370	- name: rl_observational_case_study
371	  plan_id: exp-009
372	  description: '对现有RL-trained模型(Qwen2.5-Instruct系列, DeepSeek-R1-Distill系列) 应用Self-Critique
373	    + available signals，拟合IRT with wider CIs， expected regret量化。
374	
375	    '
376	  expected_results:
377	    selfcritique_auc_rl_models_mean: 0.71
378	    available_signals_rl_count: 2
379	    contam_cal_ci_width_95_rl_pp: 11.4
380	    contam_cal_ci_width_95_sft_comparison_pp: 5.8
381	    ci_width_ratio_rl_vs_sft: 1.97
382	    expected_regret_uncalibrated: 0.38
383	    expected_regret_calibrated_wide_ci: 0.22
384	    expected_regret_remove_rescore: 0.31
385	    regret_reduction_vs_uncalibrated: 0.42
386	    regret_reduction_vs_remove_rescore: 0.29
387	    near_zero_gamma_clean_benchmark_check: 0.03
388	    gamma_posterior_rl_mean: 0.28
389	    gamma_posterior_rl_sd: 0.14
390	    gamma_ci_includes_zero_rl: false
391	    num_models_rl_case: 8
392	    kendall_tau_rl_top5_selection: 0.8
393	  result_rationale: 'best档下RL observational case study展示了"wide CIs are the correct
394	    answer"的完整叙事。 Self-Critique AUC=0.71（略超0.70阈值）在RL模型上提供了可用但noisy的信号。 CI宽度11.4pp约为SFT的2倍——这不是方法失败，而是正确反映了RL
395	    regime下检测信号的 更大不确定性。gamma posterior mean=0.28 (sd=0.14)表明RL模型确实存在contamination
396	    效应但估计更不确定；CI不包含0证明信号是directionally informative的。
397	
398	    Expected regret量化是关键：uncalibrated选择top-5模型的expected regret=0.38， 使用wide-CI calibrated
399	    scores后降至0.22（42% reduction），优于remove-rescore的0.31。 机制：即使CI很宽，calibrated scores的point
400	    estimate仍然比naive scores更准确， 而wide CI让决策者知道应该对RL模型的排名更谨慎。
401	
402	    Near-zero gamma check在known-clean benchmark上γ=0.03(接近0)， 通过specificity检验——模型不会对uncontaminated
403	    data产生false alarm。
404	
405	    '
406	  tables:
407	  - name: 'Table 11: RL Case Study — Expected Regret Comparison'
408	    rows: 3
409	    columns:
410	    - method
411	    - expected_regret
412	    - regret_reduction_vs_naive
413	    - top5_kendall_tau
414	  - name: 'Table 12: RL vs SFT CI Width Comparison'
415	    rows: 2
416	    columns:
417	    - regime
418	    - mean_ci_width_95_pp
419	    - gamma_mean
420	    - gamma_sd
421	    - signal_count
422	  figures_description:
423	  - 'Fig 15: RL vs SFT credible interval width comparison (paired model bar chart)'
424	  - 'Fig 16: Expected regret cumulative plot — uncalibrated vs calibrated vs remove-rescore'
425	  - 'Fig 17: Near-zero gamma check — posterior density on clean benchmark showing
426	    mass near zero'
427	  analysis: 'RL case study的叙事完美支持Claim 3。核心message不是"ContamCal在RL上也很准" （那不诚实），而是"ContamCal在RL上给出了appropriately
428	    uncertain的答案， 这些uncertain answers仍然改善了决策"。42% regret reduction是一个compelling number。
429	    Near-zero gamma specificity check排除了"方法总是报告contamination"的担忧。
430	
431	    '
432	- name: prior_sensitivity
433	  plan_id: exp-010
434	  description: '使用γ prior N(0,0.5)和N(0,2)（默认N(0,1)）重新拟合IRT， 验证calibrated scores和CIs对prior选择的鲁棒性。
435	
436	    '
437	  expected_results:
438	    mae_prior_tight_n05: 2.1
439	    mae_prior_default_n10: 1.97
440	    mae_prior_wide_n20: 2.0
441	    coverage_95_prior_tight: 0.91
442	    coverage_95_prior_default: 0.93
443	    coverage_95_prior_wide: 0.95
444	    ci_width_prior_tight_pp: 4.9
445	    ci_width_prior_default_pp: 5.8
446	    ci_width_prior_wide_pp: 7.1
447	    gamma_mean_prior_tight: 0.39
448	    gamma_mean_prior_default: 0.42
449	    gamma_mean_prior_wide: 0.44
450	    max_mae_diff_across_priors_pp: 0.13
451	    kendall_tau_prior_tight: 0.9
452	    kendall_tau_prior_default: 0.91
453	    kendall_tau_prior_wide: 0.91
454	  result_rationale: 'best档下prior sensitivity表现理想：三种prior下MAE差异仅0.13pp，Kendall τ几乎
455	    不变(0.90-0.91)。tight prior N(0,0.5)略微shrink了gamma估计(0.39 vs 0.42) 导致MAE略高(2.1pp)，但差异很小。wide
456	    prior N(0,2)允许gamma更大(0.44)且CI更宽 (7.1pp vs 5.8pp)，coverage从93%升至95%但sharpness代价可接受。
457	    这种行为说明：(1)数据信息量足够大，prior的影响被likelihood dominated； (2)在best档的高信号质量下，任何reasonable
458	    prior都能得到好的结果。 这直接回应了"prior choice drives results"的潜在reviewer concern。
459	
460	    '
461	  tables:
462	  - name: 'Table 13: Prior Sensitivity Analysis'
463	    rows: 3
464	    columns:
465	    - prior
466	    - mae_pp
467	    - coverage_95
468	    - ci_width_pp
469	    - gamma_mean
470	    - kendall_tau
471	  figures_description:
472	  - 'Fig 18: Prior sensitivity — MAE and CI width across 3 prior choices, error bars'
473	  analysis: 'Prior sensitivity结果证明方法稳健。MAE变化<0.15pp且ranking完全稳定， 满足了Bayesian方法的基本robustness要求。default
474	    prior N(0,1)在 coverage/sharpness trade-off上最优。
475	
476	    '
477	- name: few_examinee_regime
478	  plan_id: exp-011
479	  description: '仿真研究：model count 20/50/100/200下的IRT性能。 两阶段估计策略：用Growing Pains 400+模型池预估item参数作为informative
480	    priors。
481	
482	    '
483	  expected_results:
484	    mae_pp_n20_no_preestimate: 4.8
485	    mae_pp_n20_with_preestimate: 2.9
486	    mae_pp_n50_no_preestimate: 2.8
487	    mae_pp_n50_with_preestimate: 2.1
488	    mae_pp_n100_no_preestimate: 2.0
489	    mae_pp_n100_with_preestimate: 1.9
490	    mae_pp_n200_no_preestimate: 1.7
491	    mae_pp_n200_with_preestimate: 1.7
492	    preestimate_benefit_n20_pp: 1.9
493	    preestimate_benefit_n50_pp: 0.7
494	    preestimate_benefit_n100_pp: 0.1
495	    coverage_95_n20_preestimate: 0.9
496	    coverage_95_n50_preestimate: 0.92
497	    coverage_95_n100_preestimate: 0.93
498	    gamma_rel_bias_n20_preestimate: 0.12
499	    gamma_rel_bias_n50_preestimate: 0.08
500	    min_viable_model_count: 50
501	  result_rationale: 'best档下few-examinee仿真展示了清晰的performance gradient和pre-estimation策略的价值。
502	    N=20裸跑MAE=4.8pp不可接受，但pre-estimation将其降至2.9pp——从Growing Pains的 400+模型池中借用item parameter
503	    estimates作为informative prior极大地稳定了估计。 N=50是一个sweet spot：裸跑MAE已降至2.8pp，pre-estimation进一步降至2.1pp。
504	    N=100+时pre-estimation的marginal benefit趋近于0（0.1pp），因为数据本身已足够。 min viable model
505	    count设为50（with pre-estimation），此时coverage 92%且 gamma rel_bias 8%都在可接受范围。这直接回应了reviewer
506	    concern #6 "too few models"。
507	
508	    '
509	  tables:
510	  - name: 'Table 14: Few-Examinee Regime Study'
511	    rows: 8
512	    columns:
513	    - n_models
514	    - preestimate
515	    - mae_pp
516	    - coverage_95
517	    - ci_width_pp
518	    - gamma_rel_bias
519	  figures_description:
520	  - 'Fig 19: MAE vs model count, with/without pre-estimation, two lines converging
521	    at N=100+'
522	  analysis: 'N=50 with pre-estimation是论文推荐的minimum viable configuration。 pre-estimation策略巧妙利用了existing
523	    model evaluation pools（如Growing Pains的 Open LLM Leaderboard数据），无需额外实验成本。
524	
525	    '
526	- name: observational_72b
527	  plan_id: exp-012
528	  description: 'Qwen2.5-72B观测分析（仅推理，无SFT）。将ecological validity扩展到frontier模型规模。
529	
530	    '
531	  expected_results:
532	    gamma_posterior_72b_mmlu: 0.18
533	    gamma_posterior_72b_gsm8k: 0.12
534	    gamma_ci_excludes_zero_72b_mmlu: true
535	    gamma_ci_excludes_zero_72b_gsm8k: false
536	    calibrated_score_shift_mmlu_pp: -3.2
537	    calibrated_score_shift_gsm8k_pp: -1.8
538	    ci_width_95_72b_pp: 8.5
539	    selfcritique_auc_72b_estimated: 0.68
540	    qualitative_consistency_with_7b: true
541	  result_rationale: 'best档下72B观测分析提供了重要的ecological validity但不能有ground truth验证。 gamma=0.18（MMLU）表明即使72B模型也存在可检测的contamination效应，但效应量小于
542	    小模型(0.42)——这合理因为72B的能力足够强使得contamination的relative contribution更小。 MMLU上gamma CI排除0说明信号存在；GSM8K上CI包含0说明reasoning
543	    benchmark对72B的 contamination效应可能在noise floor以下。calibrated score下调3.2pp（MMLU） 是一个substantive但不极端的correction。CI宽度8.5pp反映了observational
544	    setting 的更大不确定性。Self-Critique AUC=0.68略低于0.70阈值，但仍在"方向性有效"范围内。
545	
546	    '
547	  tables:
548	  - name: 'Table 15: 72B Observational Analysis'
549	    rows: 4
550	    columns:
551	    - benchmark
552	    - gamma_mean
553	    - gamma_ci_lower
554	    - gamma_ci_upper
555	    - calibrated_shift_pp
556	    - ci_width_pp
557	  figures_description:
558	  - 'Fig 20: Gamma estimates across model scales (0.5B→72B) showing decreasing trend'
559	  analysis: '72B结果支持"contamination effects exist at all scales but diminish with scale"的叙事。
560	    这是生态效度论证——不是定量验证，而是证明ContamCal在frontier scale下产生 plausible和internally consistent的结果。
561	
562	    '
563	- name: closed_weight_2signal_mode
564	  plan_id: exp-013
565	  description: '降级2-signal模式(ConStat + Self-Critique)的消融研究， 量化2-signal vs 4-signal的calibration
566	    accuracy差距。
567	
568	    '
569	  expected_results:
570	    contam_cal_2signal_mae_pp: 2.4
571	    contam_cal_4signal_mae_pp: 1.97
572	    mae_increase_2signal_relative: 0.1
573	    contam_cal_2signal_ci_coverage_95: 0.94
574	    contam_cal_2signal_ci_width_95_pp: 7.2
575	    contam_cal_2signal_kendall_tau: 0.87
576	    contam_cal_2signal_dose_response_spearman: 0.92
577	    still_beats_best_baseline: true
578	    margin_over_best_baseline_2signal_relative: 0.31
579	  result_rationale: 'best档下2-signal降级模式MAE增加10%(2.4pp vs 1.97pp)，在best档范围[0.05, 0.15]的
580	    中间位置。CI宽度从5.8pp增至7.2pp（+24%），coverage从93%升至94%——更宽的CI 正确补偿了更少信号带来的更大不确定性。Kendall
581	    τ从0.91降至0.87，ranking能力略降 但仍然strong。关键：2-signal模式仍然beat best baseline 31%（2.4pp
582	    vs 3.5pp）， 证明即使在closed-weight限制下ContamCal仍有实际价值。 MAE增加主要来自ConStat在某些benchmark上的noise较大（缺少embedding和Min-K%++
583	    的complementary information），但Self-Critique的reasoning-level信号提供了 必要的anchor。dose-response
584	    spearman=0.92仍然strong。
585	
586	    '
587	  tables:
588	  - name: 'Table 16: 2-Signal vs 4-Signal Degraded Mode Comparison'
589	    rows: 2
590	    columns:
591	    - mode
592	    - mae_pp
593	    - coverage_95
594	    - ci_width_pp
595	    - kendall_tau
596	    - margin_vs_baseline
597	  figures_description:
598	  - 'Fig 21: 2-signal vs 4-signal calibration accuracy per benchmark, grouped bar
599	    chart'
600	  analysis: 2-signal模式的10% MAE degradation是一个acceptable trade-off，证明ContamCal 可以gracefully
601	    degrade到closed-weight settings。论文可以confidence地claim "even without model internals
602	    access, ContamCal provides meaningful calibration improvement over baselines."
603	    这大幅扩展了方法的practical applicability。
604	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4466a8ef-669a-4fa9-ad10-15ac09539319",
  "isSidechain": false,
  "promptId": "36e7f43a-5d9e-44f9-82f4-4f17b0038e98",
  "type": "user",
  "uuid": "cd3cef6d-90e9-4649-9281-0f87a5864ab4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: '原始framing完全成立：ContamCal是benchmark contamination的\"statistical\n  safety net\"， 三条claims按原始强度表述。Headline: \"ContamCal recovers true performance within\n  2pp MAE with 93% CI coverage, while naive scores overestimate by 8-12pp.\" RL宽CI叙事自然成立——\"wide\n  CIs are the correct answer\"用expected regret量化证明。投AAAI无需调整framing。\n\n  '\nimagined_experiments:\n- name: controlled_sft_injection\n  plan_id: exp-001\n  description: 'Qwen2.5-0.5B/1.5B/3B × 5 dosage levels (0%/5%/25%/50%/100%) SFT注入，\n    生成15个contaminated/clean模型对作为ground truth。\n\n    '\n  expected_results:\n    sft_runs_completed: 15\n    dosage_0pct_acc_delta_mmlu_pp: 0.0\n    dosage_5pct_acc_inflation_mmlu_pp: 2.1\n    dosage_25pct_acc_inflation_mmlu_pp: 5.8\n    dosage_50pct_acc_inflation_mmlu_pp: 9.3\n    dosage_100pct_acc_inflation_mmlu_pp: 12.6\n    dosage_25pct_acc_inflation_gsm8k_pp: 4.2\n    dosage_25pct_acc_inflation_arc_pp: 5.1\n    dosage_25pct_acc_inflation_humaneval_pp: 7.5\n    scale_0_5B_mean_inflation_50pct_pp: 10.8\n    scale_1_5B_mean_inflation_50pct_pp: 9.1\n    scale_3B_mean_inflation_50pct_pp: 8.2\n    dose_response_spearman_across_all: 0.97\n    convergence_failures: 0\n  result_rationale: 'best档下SFT注入实验完全按预期工作。paraphrase-based injection在5%剂量时已产生可测量的2pp\n    inflation， 100%剂量下MMLU膨胀达12.6pp，与Emperor''s New Clothes报告的8-15pp范围一致。 较小模型(0.5B)受contamination影响更大（memorization\n    capacity占比更高）， 3B模型因能力更强、泛化更好而inflation略低。GSM8K因reasoning chain结构使得 memorization效果弱于纯knowledge\n    recall的MMLU。HumanEval inflation最高因为 code solutions更容易被精确记忆。dose-response严格单调（spearman=0.97），\n    为后续IRT建模提供理想的ground truth梯度。\n\n    '\n  tables:\n  - name: 'Table 1: Accuracy Inflation (pp) by Model Scale × Dosage × Benchmark'\n    rows: 60\n    columns:\n    - model\n    - benchmark\n    - dosage\n    - clean_acc\n    - contaminated_acc\n    - inflation_pp\n  figures_description:\n  - 'Fig 1: Dose-response curves (dosage vs inflation) for each model×benchmark combination,\n    12 panels, showing strict monotonicity'\n  analysis: '所有15个SFT run成功收敛。inflation幅度在MMLU上与文献一致。 关键观察：inflation并非线性——25%→50%的增量大于5%→25%，表明contamination效果存在加速区间，\n    支持非线性4PL建模的必要性。跨benchmark一致性强，为Claim 1提供坚实的ground truth基础。\n\n    '\n- name: stage1_signal_pipeline\n  plan_id: exp-002\n  description: '在exp-001的所有模型上计算4种检测信号：embedding retrieval, Min-K%++, ConStat, Self-Critique。输出per-model-item\n    exposure scores。\n\n    '\n  expected_results:\n    embedding_retrieval_auc_sft_mean: 0.88\n    mink_pp_auc_sft_mean: 0.84\n    constat_auc_sft_mean: 0.82\n    self_critique_auc_sft_mean: 0.79\n    embedding_retrieval_auc_at_5pct_dosage: 0.76\n    mink_pp_auc_at_5pct_dosage: 0.71\n    constat_auc_at_5pct_dosage: 0.68\n    self_critique_auc_at_5pct_dosage: 0.66\n    signal_pairwise_rank_corr_max: 0.52\n    signal_pairwise_rank_corr_min: 0.28\n    items_with_all4_signals_agree_contaminated_pct: 0.73\n    items_with_disagreement_pct: 0.27\n  result_rationale: 'best档下所有4个信号都有效但各有侧重。Embedding retrieval AUC最高(0.88)因为 paraphrase-based\n    injection保留了语义相似性，FAISS能直接捕获。Min-K%++次之(0.84) 因为SFT后model perplexity在seen items上显著降低。ConStat(0.82)通过original\n    vs paraphrase performance gap检测有效但受paraphrase质量影响。Self-Critique最低(0.79) 因为依赖模型自身判断，噪声更大，但仍远超chance。在低剂量(5%)时所有信号AUC下降约0.1，\n    这是合理的——更少的contaminated items意味着更弱的统计信号。 信号间相关性适中(0.28-0.52)，说明它们捕获的是complementary\n    information， 为RRF融合提供理想条件。\n\n    '\n  tables:\n  - name: 'Table 2: Per-Signal AUC by Model × Dosage'\n    rows: 60\n    columns:\n    - model\n    - dosage\n    - embedding_auc\n    - mink_auc\n    - constat_auc\n    - selfcritique_auc\n  figures_description:\n  - 'Fig 2: Signal AUC heatmap (signal × dosage), averaged across models and benchmarks'\n  - 'Fig 3: Pairwise signal rank correlation matrix (4×4)'\n  analysis: '信号质量全面达到best档预期。关键发现：信号间低-中等相关性(mean=0.38)证实 complementarity假设，为RRF融合奠定基础。HumanEval上embedding\n    retrieval AUC 特别高(0.92)因为code的语义embedding更具区分性。\n\n    '\n- name: rrf_aggregation_ablation\n  plan_id: exp-003\n  description: 'RRF融合4信号为composite exposure score。消融实验：RRF vs rank averaging, 单信号,\n    calibration-weighted RRF, FP注入鲁棒性, 2-signal降级模式。\n\n    '\n  expected_results:\n    rrf_4signal_auc: 0.87\n    rank_averaging_auc: 0.84\n    best_single_signal_auc: 0.88\n    calibration_weighted_rrf_auc: 0.86\n    rrf_minus_best_single_delta_auc: -0.01\n    rrf_auc_at_fp_rate_10pct: 0.84\n    rrf_auc_at_fp_rate_20pct: 0.8\n    degraded_2signal_auc: 0.78\n    rrf_4signal_vs_2signal_delta: 0.09\n    rrf_exposure_score_spearman_with_true_dosage: 0.91\n    rank_stability_bootstrap_cv: 0.04\n  result_rationale: 'best档下RRF融合AUC(0.87)接近最好的单信号(embedding 0.88)但关键优势在于鲁棒性： RRF在所有benchmark上都稳定达到0.85+，而单信号表现波动大（embedding在GSM8K上可能\n    降到0.80，ConStat在HumanEval上可能降到0.75）。RRF比rank averaging高3pp因为 reciprocal rank weighting对高置信排名给予更大权重。Calibration-weighted\n    RRF略低于 vanilla RRF因为权重估计引入了额外noise，且在best档的高信号质量下vanilla RRF已足够。 FP注入10%时AUC仅降3pp，20%时降7pp，证明graceful\n    degradation。 2-signal模式(ConStat+Self-Critique)AUC=0.78，比4-signal低9pp但仍远超chance，\n    满足closed-weight场景的可用性。exposure score与true dosage的spearman=0.91 证明RRF输出确实捕获了contamination程度的有序信息。\n\n    '\n  tables:\n  - name: 'Table 3: RRF Ablation Results'\n    rows: 8\n    columns:\n    - method\n    - auc_mmlu\n    - auc_gsm8k\n    - auc_arc\n    - auc_humaneval\n    - auc_mean\n    - auc_std\n  - name: 'Table 4: FP Injection Robustness'\n    rows: 4\n    columns:\n    - fp_rate\n    - rrf_auc\n    - delta_from_clean\n  figures_description:\n  - 'Fig 4: Signal dropout ablation bar chart — AUC by combination (4-signal, each\n    3-signal, each single, 2-signal degraded)'\n  - 'Fig 5: RRF exposure score vs true dosage scatter plot with Spearman annotation'\n  analysis: 'RRF fusion的核心价值不在于AUC绝对值（最好的单信号可能匹配），而在于跨benchmark、 跨模型的一致性和FP鲁棒性。这直接支持Claim\n    2的\"outperforming any single signal\"—— 含义是worst-case performance更优，而非mean AUC更高。2-signal降级模式AUC=0.78\n    为closed-weight实用性提供了有力支撑。\n\n    '\n- name: noise_propagation_analysis\n  plan_id: exp-005\n  description: '校准noise注入到exposure scores中：估计per-item FP/FN率， 注入matched/1.5×/2×高斯噪声，重新拟合IRT，测量CI宽化。\n\n    '\n  expected_results:\n    selfcritique_estimated_fp_rate: 0.12\n    selfcritique_estimated_fn_rate: 0.18\n    matched_noise_ci_width_gamma_pp: 5.2\n    noise_1_5x_ci_width_gamma_pp: 6.8\n    noise_2x_ci_width_gamma_pp: 8.9\n    matched_noise_ci_coverage_95: 0.94\n    noise_1_5x_ci_coverage_95: 0.96\n    noise_2x_ci_coverage_95: 0.97\n    gamma_rel_bias_at_matched_noise: 0.06\n    gamma_rel_bias_at_2x_noise: 0.09\n    theta_corr_at_matched_noise: 0.94\n    theta_corr_at_2x_noise: 0.89\n    measurement_error_model_dic_improvement: 12.3\n  result_rationale: 'best档下noise propagation表现理想：随着noise增加，CI合理宽化（5.2→8.9pp）而非崩溃，\n    coverage从94%略升至97%（略过覆盖而非欠覆盖）。这说明Bayesian posterior正确地将 exposure score uncertainty吸收进了参数不确定性。gamma相对偏差从0.06增到0.09，\n    表明点估计稳健性在2×noise下仍可接受。theta相关性从0.94降至0.89，下降幅度合理—— 更多noise意味着contamination信号更弱，ability估计回退向vanilla\n    IRT。 Self-Critique的FP=12%/FN=18%在best档下是合理的——比embedding差但比random好得多。 measurement\n    error扩展模型DIC改善12.3说明显式建模exposure noise有统计意义上的价值。\n\n    '\n  tables:\n  - name: 'Table 5: Noise Propagation Results'\n    rows: 4\n    columns:\n    - noise_level\n    - gamma_mean\n    - gamma_rel_bias\n    - ci_width_pp\n    - ci_coverage_95\n    - theta_corr\n  figures_description:\n  - 'Fig 6: CI width vs noise level line plot, with coverage annotated at each point'\n  - 'Fig 7: θ recovery correlation scatterplots at 3 noise levels (1×, 1.5×, 2×)'\n  analysis: '核心结论：4PL+γ的Bayesian formulation天然支持noise propagation——更noisy的exposure\n    scores产生更宽的CI而不是更差的点估计。这直接支持Claim 3，也为RL regime下 Self-Critique-only信号的wider CIs提供了机制解释。\n\n    '\n- name: irt_calibration_and_baselines\n  plan_id: exp-006\n  description: '在exp-001/003的controlled数据上拟合4PL+γ IRT (Stan NUTS)， 计算calibrated scores，与5个baselines比较，评估5个指标。\n\n    '\n  expected_results:\n    contam_cal_mae_pp_mmlu: 1.8\n    contam_cal_mae_pp_gsm8k: 2.1\n    contam_cal_mae_pp_arc: 1.6\n    contam_cal_mae_pp_humaneval: 2.4\n    contam_cal_mae_pp_mean: 1.97\n    contam_cal_ci_coverage_95: 0.93\n    contam_cal_ci_coverage_80: 0.84\n    contam_cal_ci_coverage_50: 0.55\n    contam_cal_ci_width_95_pp: 5.8\n    contam_cal_kendall_tau: 0.91\n    contam_cal_dose_response_spearman: 0.96\n    baseline_remove_rescore_mae_pp: 4.2\n    baseline_single_2plg_mae_pp: 3.8\n    baseline_vanilla_4pl_mae_pp: 6.1\n    baseline_linear_regression_mae_pp: 3.5\n    baseline_emperor_mitigation_mae_pp: 5.7\n    best_baseline_mae_pp: 3.5\n    margin_over_best_baseline_mae_relative: 0.44\n    naive_score_overestimation_50pct_dosage_pp: 9.3\n    gamma_posterior_mean: 0.42\n    gamma_posterior_sd: 0.08\n    gamma_rel_bias_real_data: 0.06\n    theta_corr_with_ground_truth: 0.95\n    theta_gamma_posterior_corr: 0.31\n    nuts_divergent_pct: 0.0\n    nuts_max_rhat: 1.005\n    nuts_ess_min: 800\n  result_rationale: 'best档核心实验。4PL+γ MAE=1.97pp完全复现仿真表现——真实SFT数据上的contamination 结构与仿真假设匹配良好。MMLU\n    MAE最低(1.8pp)因为item数量最多(14K)提供了最强的 统计功效；HumanEval最高(2.4pp)因为item少且code execution评分的binary\n    nature 增加了noise。93% coverage接近nominal 95%，略低是因为real data的item heterogeneity 比仿真更大，但仍在可接受范围。CI宽度5.8pp在sharpness和coverage间取得了好的平衡。\n\n    Baselines方面：vanilla 4PL(无γ)MAE=6.1pp最差，因为完全忽略contamination， 证明contamination covariate是必要的。Emperor''s\n    mitigation MAE=5.7pp次差， 与ICML 2025发现一致——mitigation strategies确实不够有效。Linear regression\n    MAE=3.5pp 是最好的baseline，但仍比ContamCal差44%——IRT的优势在于non-linear item response 建模和proper\n    uncertainty propagation。Remove-rescore MAE=4.2pp受限于binary flagging丢失了contamination程度信息。Single-signal\n    2PL+γ MAE=3.8pp表明 signal fusion和4PL复杂度各贡献了一部分改善。\n\n    θ-γ posterior correlation=0.31 < 0.4阈值，证实identifiability。 gamma rel_bias=0.06与仿真的0.068几乎一致。NUTS诊断完美——无divergence，\n    Rhat<1.01，ESS>800。\n\n    '\n  tables:\n  - name: 'Table 6 (Main Result): Calibration Performance — ContamCal vs 5 Baselines'\n    rows: 6\n    columns:\n    - method\n    - mae_mmlu\n    - mae_gsm8k\n    - mae_arc\n    - mae_humaneval\n    - mae_mean\n    - ci_coverage_95\n    - ci_width_95\n    - kendall_tau\n  - name: 'Table 7: Per-Benchmark Detailed Metrics'\n    rows: 4\n    columns:\n    - benchmark\n    - mae_pp\n    - coverage_50\n    - coverage_80\n    - coverage_95\n    - ci_width_95_pp\n    - kendall_tau\n    - dose_response_spearman\n  - name: 'Table 8: MCMC Diagnostics'\n    rows: 4\n    columns:\n    - benchmark\n    - divergent_pct\n    - max_rhat\n    - min_ess\n    - fit_time_sec\n  figures_description:\n  - 'Fig 8 (Main Figure): Calibrated vs true accuracy scatter plot, all benchmarks,\n    with 95% CI error bars, diagonal reference line'\n  - 'Fig 9: MAE bar chart — ContamCal vs 5 baselines, per benchmark'\n  - 'Fig 10: Dose-response curves — γ effect size vs contamination dosage, 4 benchmark\n    panels'\n  - 'Fig 11: Coverage calibration plot — nominal vs empirical coverage at 50/80/95%\n    levels'\n  analysis: '这是论文的核心结果表。MAE 1.97pp vs best baseline 3.5pp (44% relative improvement)\n    提供了Claim 1的强有力支撑。93% coverage证明CI可靠。headline result可直接写为 \"ContamCal recovers true\n    performance within 2pp MAE with 93% CI coverage, while naive scores overestimate\n    by 8-12pp.\" Kendall τ=0.91证明model ranking 在calibration后基本保持正确——contamination改变的是绝对分数而非相对排名，\n    但ContamCal在absolute calibration上的优势对于跨benchmark比较至关重要。\n\n    '\n- name: scale_bridging_7b\n  plan_id: exp-007\n  description: 'Qwen2.5-7B在5个dosage水平下的controlled SFT注入，验证calibration在更大模型上的有效性。\n\n    '\n  expected_results:\n    dosage_25pct_acc_inflation_mmlu_pp: 4.8\n    dosage_50pct_acc_inflation_mmlu_pp: 7.6\n    dosage_100pct_acc_inflation_mmlu_pp: 10.2\n    contam_cal_mae_pp_mean_7b: 2.2\n    contam_cal_ci_coverage_95_7b: 0.92\n    contam_cal_kendall_tau_7b: 0.89\n    mae_increase_vs_3b_pp: 0.3\n    gamma_mean_7b: 0.38\n    dose_response_spearman_7b: 0.94\n  result_rationale: 'best档下7B模型表现略弱于0.5-3B但仍在acceptable范围内。7B的inflation略低于小模型 (50%\n    dosage: 7.6pp vs 9.3pp mean for smaller)因为7B的更强泛化能力意味着 contamination的relative\n    contribution更小。MAE略增至2.2pp(+0.3pp vs 3B)因为 7B模型的item response pattern更复杂，但仍远优于baselines。gamma估计值0.38略低于\n    小模型的0.42，反映了contamination对larger model的较小相对效应。 Coverage 92%和Kendall τ=0.89仍然强劲，证明ContamCal可扩展到7B规模。\n\n    '\n  tables:\n  - name: 'Table 9: 7B Scale Bridging Results'\n    rows: 5\n    columns:\n    - dosage\n    - inflation_pp\n    - contam_cal_mae_pp\n    - ci_coverage_95\n    - kendall_tau\n  figures_description:\n  - 'Fig 12: MAE vs model scale line plot (0.5B, 1.5B, 3B, 7B) showing graceful degradation'\n  analysis: '7B结果证明ContamCal从小模型到中等规模模型的可扩展性。MAE增加有限(+0.3pp) 且符合理论预期——更大的模型有更复杂的ability\n    landscape但contamination的相对效应更小。\n\n    '\n- name: signal_survival_analysis\n  plan_id: exp-008\n  description: '检测信号在不同训练regime下的可靠性系统评估。 Signal × regime AUC heatmap: 4 signals ×\n    {base, SFT-clean, SFT-contaminated, RL-post-trained}。\n\n    '\n  expected_results:\n    embedding_auc_base: 0.9\n    embedding_auc_sft_clean: 0.51\n    embedding_auc_sft_contam: 0.88\n    embedding_auc_rl: 0.55\n    mink_auc_base: 0.86\n    mink_auc_sft_clean: 0.53\n    mink_auc_sft_contam: 0.84\n    mink_auc_rl: 0.58\n    constat_auc_base: 0.5\n    constat_auc_sft_clean: 0.5\n    constat_auc_sft_contam: 0.82\n    constat_auc_rl: 0.67\n    selfcritique_auc_base: 0.5\n    selfcritique_auc_sft_clean: 0.5\n    selfcritique_auc_sft_contam: 0.79\n    selfcritique_auc_rl: 0.72\n    signal_survival_rl_best: Self-Critique\n    signal_survival_rl_second: ConStat\n  result_rationale: 'best档下信号存活模式清晰：embedding和Min-K%++在SFT-contaminated上表现强劲 (0.88/0.84)但在RL后严重降级(0.55/0.58)——RL的policy\n    gradient更新破坏了 token-level memorization pattern，使得perplexity-based信号失效。 ConStat在RL后保留AUC=0.67因为它测量的是performance\n    gap(original vs paraphrase) 这一higher-level信号，不依赖model internals。Self-Critique在RL后最强(0.72)\n    因为它利用模型的reasoning能力来自我评估，RL强化了这种元认知能力而非削弱。 base模型和SFT-clean模型上ConStat和Self-Critique接近chance(0.50)是正确的——\n    没有contamination时不应有信号（specificity验证）。 这个heatmap直接支持RRF fusion的必要性：没有任何单一信号在所有regime下都最优。\n\n    '\n  tables:\n  - name: 'Table 10 (Supporting Contribution): Signal × Regime AUC Heatmap'\n    rows: 4\n    columns:\n    - signal\n    - base\n    - sft_clean\n    - sft_contam\n    - rl_post_trained\n  figures_description:\n  - 'Fig 13: Signal survival heatmap (4×4 matrix, color-coded by AUC)'\n  - 'Fig 14: Per-signal AUC degradation from SFT→RL, paired bar chart'\n  analysis: '这是论文的Supporting Contribution 5。关键insight：RL post-training创造了一个 \"signal\n    desert\"——只有Self-Critique和ConStat存活。这解释了为什么RL regime 需要更宽的CI（更少信号→更大不确定性），同时也为2-signal\n    degraded mode提供了 empirical justification。\n\n    '\n- name: rl_observational_case_study\n  plan_id: exp-009\n  description: '对现有RL-trained模型(Qwen2.5-Instruct系列, DeepSeek-R1-Distill系列) 应用Self-Critique\n    + available signals，拟合IRT with wider CIs， expected regret量化。\n\n    '\n  expected_results:\n    selfcritique_auc_rl_models_mean: 0.71\n    available_signals_rl_count: 2\n    contam_cal_ci_width_95_rl_pp: 11.4\n    contam_cal_ci_width_95_sft_comparison_pp: 5.8\n    ci_width_ratio_rl_vs_sft: 1.97\n    expected_regret_uncalibrated: 0.38\n    expected_regret_calibrated_wide_ci: 0.22\n    expected_regret_remove_rescore: 0.31\n    regret_reduction_vs_uncalibrated: 0.42\n    regret_reduction_vs_remove_rescore: 0.29\n    near_zero_gamma_clean_benchmark_check: 0.03\n    gamma_posterior_rl_mean: 0.28\n    gamma_posterior_rl_sd: 0.14\n    gamma_ci_includes_zero_rl: false\n    num_models_rl_case: 8\n    kendall_tau_rl_top5_selection: 0.8\n  result_rationale: 'best档下RL observational case study展示了\"wide CIs are the correct\n    answer\"的完整叙事。 Self-Critique AUC=0.71（略超0.70阈值）在RL模型上提供了可用但noisy的信号。 CI宽度11.4pp约为SFT的2倍——这不是方法失败，而是正确反映了RL\n    regime下检测信号的 更大不确定性。gamma posterior mean=0.28 (sd=0.14)表明RL模型确实存在contamination\n    效应但估计更不确定；CI不包含0证明信号是directionally informative的。\n\n    Expected regret量化是关键：uncalibrated选择top-5模型的expected regret=0.38， 使用wide-CI calibrated\n    scores后降至0.22（42% reduction），优于remove-rescore的0.31。 机制：即使CI很宽，calibrated scores的point\n    estimate仍然比naive scores更准确， 而wide CI让决策者知道应该对RL模型的排名更谨慎。\n\n    Near-zero gamma check在known-clean benchmark上γ=0.03(接近0)， 通过specificity检验——模型不会对uncontaminated\n    data产生false alarm。\n\n    '\n  tables:\n  - name: 'Table 11: RL Case Study — Expected Regret Comparison'\n    rows: 3\n    columns:\n    - method\n    - expected_regret\n    - regret_reduction_vs_naive\n    - top5_kendall_tau\n  - name: 'Table 12: RL vs SFT CI Width Comparison'\n    rows: 2\n    columns:\n    - regime\n    - mean_ci_width_95_pp\n    - gamma_mean\n    - gamma_sd\n    - signal_count\n  figures_description:\n  - 'Fig 15: RL vs SFT credible interval width comparison (paired model bar chart)'\n  - 'Fig 16: Expected regret cumulative plot — uncalibrated vs calibrated vs remove-rescore'\n  - 'Fig 17: Near-zero gamma check — posterior density on clean benchmark showing\n    mass near zero'\n  analysis: 'RL case study的叙事完美支持Claim 3。核心message不是\"ContamCal在RL上也很准\" （那不诚实），而是\"ContamCal在RL上给出了appropriately\n    uncertain的答案， 这些uncertain answers仍然改善了决策\"。42% regret reduction是一个compelling number。\n    Near-zero gamma specificity check排除了\"方法总是报告contamination\"的担忧。\n\n    '\n- name: prior_sensitivity\n  plan_id: exp-010\n  description: '使用γ prior N(0,0.5)和N(0,2)（默认N(0,1)）重新拟合IRT， 验证calibrated scores和CIs对prior选择的鲁棒性。\n\n    '\n  expected_results:\n    mae_prior_tight_n05: 2.1\n    mae_prior_default_n10: 1.97\n    mae_prior_wide_n20: 2.0\n    coverage_95_prior_tight: 0.91\n    coverage_95_prior_default: 0.93\n    coverage_95_prior_wide: 0.95\n    ci_width_prior_tight_pp: 4.9\n    ci_width_prior_default_pp: 5.8\n    ci_width_prior_wide_pp: 7.1\n    gamma_mean_prior_tight: 0.39\n    gamma_mean_prior_default: 0.42\n    gamma_mean_prior_wide: 0.44\n    max_mae_diff_across_priors_pp: 0.13\n    kendall_tau_prior_tight: 0.9\n    kendall_tau_prior_default: 0.91\n    kendall_tau_prior_wide: 0.91\n  result_rationale: 'best档下prior sensitivity表现理想：三种prior下MAE差异仅0.13pp，Kendall τ几乎\n    不变(0.90-0.91)。tight prior N(0,0.5)略微shrink了gamma估计(0.39 vs 0.42) 导致MAE略高(2.1pp)，但差异很小。wide\n    prior N(0,2)允许gamma更大(0.44)且CI更宽 (7.1pp vs 5.8pp)，coverage从93%升至95%但sharpness代价可接受。\n    这种行为说明：(1)数据信息量足够大，prior的影响被likelihood dominated； (2)在best档的高信号质量下，任何reasonable\n    prior都能得到好的结果。 这直接回应了\"prior choice drives results\"的潜在reviewer concern。\n\n    '\n  tables:\n  - name: 'Table 13: Prior Sensitivity Analysis'\n    rows: 3\n    columns:\n    - prior\n    - mae_pp\n    - coverage_95\n    - ci_width_pp\n    - gamma_mean\n    - kendall_tau\n  figures_description:\n  - 'Fig 18: Prior sensitivity — MAE and CI width across 3 prior choices, error bars'\n  analysis: 'Prior sensitivity结果证明方法稳健。MAE变化<0.15pp且ranking完全稳定， 满足了Bayesian方法的基本robustness要求。default\n    prior N(0,1)在 coverage/sharpness trade-off上最优。\n\n    '\n- name: few_examinee_regime\n  plan_id: exp-011\n  description: '仿真研究：model count 20/50/100/200下的IRT性能。 两阶段估计策略：用Growing Pains 400+模型池预估item参数作为informative\n    priors。\n\n    '\n  expected_results:\n    mae_pp_n20_no_preestimate: 4.8\n    mae_pp_n20_with_preestimate: 2.9\n    mae_pp_n50_no_preestimate: 2.8\n    mae_pp_n50_with_preestimate: 2.1\n    mae_pp_n100_no_preestimate: 2.0\n    mae_pp_n100_with_preestimate: 1.9\n    mae_pp_n200_no_preestimate: 1.7\n    mae_pp_n200_with_preestimate: 1.7\n    preestimate_benefit_n20_pp: 1.9\n    preestimate_benefit_n50_pp: 0.7\n    preestimate_benefit_n100_pp: 0.1\n    coverage_95_n20_preestimate: 0.9\n    coverage_95_n50_preestimate: 0.92\n    coverage_95_n100_preestimate: 0.93\n    gamma_rel_bias_n20_preestimate: 0.12\n    gamma_rel_bias_n50_preestimate: 0.08\n    min_viable_model_count: 50\n  result_rationale: 'best档下few-examinee仿真展示了清晰的performance gradient和pre-estimation策略的价值。\n    N=20裸跑MAE=4.8pp不可接受，但pre-estimation将其降至2.9pp——从Growing Pains的 400+模型池中借用item parameter\n    estimates作为informative prior极大地稳定了估计。 N=50是一个sweet spot：裸跑MAE已降至2.8pp，pre-estimation进一步降至2.1pp。\n    N=100+时pre-estimation的marginal benefit趋近于0（0.1pp），因为数据本身已足够。 min viable model\n    count设为50（with pre-estimation），此时coverage 92%且 gamma rel_bias 8%都在可接受范围。这直接回应了reviewer\n    concern #6 \"too few models\"。\n\n    '\n  tables:\n  - name: 'Table 14: Few-Examinee Regime Study'\n    rows: 8\n    columns:\n    - n_models\n    - preestimate\n    - mae_pp\n    - coverage_95\n    - ci_width_pp\n    - gamma_rel_bias\n  figures_description:\n  - 'Fig 19: MAE vs model count, with/without pre-estimation, two lines converging\n    at N=100+'\n  analysis: 'N=50 with pre-estimation是论文推荐的minimum viable configuration。 pre-estimation策略巧妙利用了existing\n    model evaluation pools（如Growing Pains的 Open LLM Leaderboard数据），无需额外实验成本。\n\n    '\n- name: observational_72b\n  plan_id: exp-012\n  description: 'Qwen2.5-72B观测分析（仅推理，无SFT）。将ecological validity扩展到frontier模型规模。\n\n    '\n  expected_results:\n    gamma_posterior_72b_mmlu: 0.18\n    gamma_posterior_72b_gsm8k: 0.12\n    gamma_ci_excludes_zero_72b_mmlu: true\n    gamma_ci_excludes_zero_72b_gsm8k: false\n    calibrated_score_shift_mmlu_pp: -3.2\n    calibrated_score_shift_gsm8k_pp: -1.8\n    ci_width_95_72b_pp: 8.5\n    selfcritique_auc_72b_estimated: 0.68\n    qualitative_consistency_with_7b: true\n  result_rationale: 'best档下72B观测分析提供了重要的ecological validity但不能有ground truth验证。 gamma=0.18（MMLU）表明即使72B模型也存在可检测的contamination效应，但效应量小于\n    小模型(0.42)——这合理因为72B的能力足够强使得contamination的relative contribution更小。 MMLU上gamma CI排除0说明信号存在；GSM8K上CI包含0说明reasoning\n    benchmark对72B的 contamination效应可能在noise floor以下。calibrated score下调3.2pp（MMLU） 是一个substantive但不极端的correction。CI宽度8.5pp反映了observational\n    setting 的更大不确定性。Self-Critique AUC=0.68略低于0.70阈值，但仍在\"方向性有效\"范围内。\n\n    '\n  tables:\n  - name: 'Table 15: 72B Observational Analysis'\n    rows: 4\n    columns:\n    - benchmark\n    - gamma_mean\n    - gamma_ci_lower\n    - gamma_ci_upper\n    - calibrated_shift_pp\n    - ci_width_pp\n  figures_description:\n  - 'Fig 20: Gamma estimates across model scales (0.5B→72B) showing decreasing trend'\n  analysis: '72B结果支持\"contamination effects exist at all scales but diminish with scale\"的叙事。\n    这是生态效度论证——不是定量验证，而是证明ContamCal在frontier scale下产生 plausible和internally consistent的结果。\n\n    '\n- name: closed_weight_2signal_mode\n  plan_id: exp-013\n  description: '降级2-signal模式(ConStat + Self-Critique)的消融研究， 量化2-signal vs 4-signal的calibration\n    accuracy差距。\n\n    '\n  expected_results:\n    contam_cal_2signal_mae_pp: 2.4\n    contam_cal_4signal_mae_pp: 1.97\n    mae_increase_2signal_relative: 0.1\n    contam_cal_2signal_ci_coverage_95: 0.94\n    contam_cal_2signal_ci_width_95_pp: 7.2\n    contam_cal_2signal_kendall_tau: 0.87\n    contam_cal_2signal_dose_response_spearman: 0.92\n    still_beats_best_baseline: true\n    margin_over_best_baseline_2signal_relative: 0.31\n  result_rationale: 'best档下2-signal降级模式MAE增加10%(2.4pp vs 1.97pp)，在best档范围[0.05, 0.15]的\n    中间位置。CI宽度从5.8pp增至7.2pp（+24%），coverage从93%升至94%——更宽的CI 正确补偿了更少信号带来的更大不确定性。Kendall\n    τ从0.91降至0.87，ranking能力略降 但仍然strong。关键：2-signal模式仍然beat best baseline 31%（2.4pp\n    vs 3.5pp）， 证明即使在closed-weight限制下ContamCal仍有实际价值。 MAE增加主要来自ConStat在某些benchmark上的noise较大（缺少embedding和Min-K%++\n    的complementary information），但Self-Critique的reasoning-level信号提供了 必要的anchor。dose-response\n    spearman=0.92仍然strong。\n\n    '\n  tables:\n  - name: 'Table 16: 2-Signal vs 4-Signal Degraded Mode Comparison'\n    rows: 2\n    columns:\n    - mode\n    - mae_pp\n    - coverage_95\n    - ci_width_pp\n    - kendall_tau\n    - margin_vs_baseline\n  figures_description:\n  - 'Fig 21: 2-signal vs 4-signal calibration accuracy per benchmark, grouped bar\n    chart'\n  analysis: 2-signal模式的10% MAE degradation是一个acceptable trade-off，证明ContamCal 可以gracefully\n    degrade到closed-weight settings。论文可以confidence地claim \"even without model internals\n    access, ContamCal provides meaningful calibration improvement over baselines.\"\n    这大幅扩展了方法的practical applicability。\n",
      "numLines": 604,
      "startLine": 1,
      "totalLines": 604
    }
  },
  "sourceToolAssistantUUID": "4466a8ef-669a-4fa9-ad10-15ac09539319",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T17:25:03.291Z_

<details open><summary>🔧 Tool call — Read · `toolu_0197L3vM87yivB2WTpR4jfTB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd3cef6d-90e9-4649-9281-0f87a5864ab4",
  "isSidechain": false,
  "requestId": "req_011CazxWkLB2kCTEe3T5t4Wc",
  "type": "assistant",
  "uuid": "277925dc-1460-4d09-984b-2d7289341b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqCpSwtfpE2YfCCaPGFmtd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 25120,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2111,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 25120,
          "cache_creation_input_tokens": 2111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2111
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：γ和θ在实际数据上严重混淆；检测信号AUC不足以支撑有意义的校准；per-benchmark γ_k不收敛或与global γ无显著差异 核心假设：['RRF融合AUC在SFT regime仅0.60-0.68，RL regime下降至<0.55（随机附近）', 'γ和θ的posterior高度相关（|co…",
  "leafUuid": "51f87f7f-7aab-400c-8bb1-9187600a8632",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "ContamCal framework: calibration limits and diagnostic analysis",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702"
}
```

---

### Runtime record

_source line 21 · 2026-05-13T17:25:03.684Z_

````json
{
  "parentUuid": "51f87f7f-7aab-400c-8bb1-9187600a8632",
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
  "uuid": "fd0a9427-bc49-45d4-86ff-da62989fd698",
  "timestamp": "2026-05-13T17:25:03.684Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Assistant

_source line 22 · 2026-05-13T17:26:41.498Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the project and the existing worst-tier dream report. I notice that the existing worst-tier dream report already has detailed imagined experiments, but the user is asking me to produce the worst-tier predictions for ALL experiments in the experiment_plan. Let me compare what's in the existing worst-tier report vs what's in the experiment_plan.

Looking at the experiment_plan, the planned experiments are:
- exp-001: controlled_sft_injection ✓ (in worst report)
- exp-002: stage1_signal_pipeline ✓


- exp-003: rrf_aggregation_ablation ✓
- exp-004: simulation_identifiability_sweep (NOT in worst report - needs to be added)
- exp-005: noise_propagation_analysis ✓
- exp-006: irt_calibration_and_baselines ✓
- exp-007: scale_bridging_7b ✓
- exp-008: signal_survival_analysis ✓
- exp-009: rl_observational_case_study ✓
- exp-014: multi_family_validation (NOT in worst report)
- exp-012: observational_72b ✓
- exp-013: closed_weight_2signal ✓

So I need to add worst-tier predictions for exp-004 and exp-014, which are currently missing from the worst-tier dream report. So I need to make sure I'm covering all the planned experiments from the experiment_plan with worst-tier predictions and rationales. Looking at what's already in the worst report versus what's actually planned, I'm missing exp-004 (the simulation_identifiability_sweep that's currently running) and exp-014 (multi_family_validation), since exp-010 and exp-011 were merged into exp-004 anyway.

I also notice exp-006 should have 7 baselines according to the plan but the existing report only lists 5, so I need to correct that. Now I'm generating the complete worst-tier predictions for all planned experiments while keeping the metrics within the specified ranges: calibration_mae_pp between 4.5-9.0, coverage_95_pct between 70-85, and coverage_80_pct between 50 and whatever the upper bound is. Now I'm cross-referencing against the worst-tier assumptions to see where the current results stand—checking things like posterior correlation issues, convergence problems with per-benchmark parameters, confidence interval widths, and whether the second model family can even complete given GPU constraints. Looking back at the signal AUC values from the earlier experiments, I'm noticing the RRF performance at full dosage actually sits at the upper bound of what I'd expect for the worst tier, which suggests the results might be closer to that threshold than initially thought.

Let me recalibrate the predictions to align properly with the worst-tier definition—tightening the RRF AUC range, ensuring posterior correlations exceed the threshold, and adjusting the signal recovery metrics accordingly. I also need to verify that calibration error, rank correlation, and other metrics all fall within their expected ranges, then work through the full set of experiments including the new baselines and per-benchmark parameter estimates. at the existing worst report more carefully. The user wants me to expand the worst-tier analysis across all planned experiments based on the updated experiment_plan and worst-tier definition.

Several key updates need to be incorporated: exp-006 now includes 7 baselines with DCR and Raw anchor variants, plus per-benchmark γ_k adjustments; exp-004 should subsume exp-010 and exp-011; exp-014 for multi_family_validation is new; the γ-θ posterior correlation threshold is now >0.6 instead of 0.52; and Signal AUC values need tighter alignment with specified ranges.

The narrative framing shifts from claiming we solve calibration to mapping the possibility frontier—with Fisher Information identifiability as the core analysis, signal survival as independent empirical validation, and calibration as conditional proof-of-concept rather than a primary claim.

Now I'm working through each experiment's worst-case scenario. For exp-001, the SFT injection produces noisy inflation patterns where low dosages become indistinguishable from baseline noise, with scale-dependent effects where smaller models show disproportionate inflation and high variance across runs.

Generating YAML output... across seeds

### exp-002: stage1_signal_pipeline
- Signal AUC systematically lower than simulation assumptions
- Best single signal (embedding) ~0.72 at 100% dosage
- Average across conditions ~0.61
- All signals near random at 5% dosage

### exp-003: rrf_aggregation_ablation
- RRF AUC in SFT regime: 0.63-0.68 (within specified range)
- RRF doesn't outperform best single signal
- High signal correlation (~0.58)

### exp-004: simulation_identifiability_sweep
- This is the big simulation sweep
- Fisher Information analysis shows AUC threshold ~0.72 for practical identifiability
- At AUC=0.65 (realistic), γ RMSE high, coverage poor
- Prior sensitivity high at low AUC
- Number of models × AUC interaction is multiplicative rather than additive

### exp-005: noise_propagation_analysis
- Measurement error model converges but produces credible intervals that are too wide
- At matched noise levels, γ confidence intervals span ~22 percentage points
- Coverage improves due to the width of these intervals, though this is somewhat artificial

### exp-006: irt_calibration_and_baselines
Now testing with 7 baselines plus DCR and per-benchmark γ parameters. The 4PL+γ model achieves ~6.5pp MAE, DCR performs comparably on some benchmarks, and per-benchmark γ estimates either fail to converge or show no significant difference from the global estimate. Posterior correlation between γ and θ exceeds 0.6, coverage at 95% confidence is around 76%, and Kendall τ reaches ~0.72.

### exp-007: scale_bridging_7b
At the 7B scale, inflation is lower and signals are weaker, with calibration degrading at larger model sizes and confirming that identifiability worsens as scale increases.

### exp-008: signal_survival_analysis
Signals degrade gradually under RL rather than showing sharp regime boundaries, contradicting the assumption of clean transitions. Self-Critique performs best in the RL setting but only achieves AUC around 0.52.

### exp-009: rl_observational_case_study
All signals fall below the identifiability threshold, calibration actually worsens performance compared to uncalibrated estimates, and expected regret reduction is near zero or negative.

### exp-014: multi_family_validation
GPU constraints prevented completion, but preliminary results suggest findings inconsistent with the Qwen direction.

### exp-012: observational_72b
At frontier scale, signals become nearly indistinguishable from noise, γ is statistically indistinguishable from zero, and MAE performance is the worst observed.

### exp-013: closed_weight_2signal_mode
The two-signal approach is completely unviable, with calibration performing worse than leaving estimates uncalibrated.

The MAE gap between these results and the Qwen baseline ranges from 4-10 percentage points, indicating a substantial performance gap.

Now I'm working through the numerical constraints for the worst-tier experiments. I'm anchoring on the defined ranges for key metrics—signal AUC around 0.65 for SFT and 0.52 for RL, calibration MAE in the 6-8 percentage point range, coverage metrics around 76% for the 95th percentile and 58% for the 80th percentile, and confidence interval widths around 9 percentage points—to ensure all the experimental results stay internally consistent with the worst-tier assumptions.

For the remaining metrics, I'm setting Kendall's tau at roughly 0.72, relative bias around 0.32, and expecting to beat about 2 baseline methods. The dose-response relationship won't be monotonic, and the multi-family MAE gap should be around 6.5 percentage points. Now I'm mapping out the signal AUCs across different dosage levels, starting with the assumption that at full dosage the SFT RRF signal AUC reaches about 0.68, dropping to around 0.53 at 5% dosage, and beginning to fill in the individual signal AUCs for each signal type at maximum dosage.

Looking at the performance breakdown across different methods and regimes, I see Min-K++ and RRF performing strongest at full dosage around 0.67-0.68, while Self-Critique drops significantly in the RL regime to 0.52. The embedding signal degrades substantially under RL, falling to 0.50. But there's something important here—the worst-case assumption suggests that signal survival doesn't follow a clean, predictable pattern across regimes. Instead, signals degrade gradually and inconsistently depending on the specific benchmark, which complicates any simple narrative about regime-dependent performance.

The RRF fusion scores tell the story: they range from 0.60-0.68 in SFT but collapse below 0.55 in RL, confirming degradation happens, just not in a cliff-like way. Different signals don't show clear complementarity, and there's no universal ordering across benchmarks. Even in the cleaner SFT regime, the signals are already relatively weak, and the transition to RL shows gradual erosion rather than a sharp threshold effect.

Now I need to think through what's happening with γ.

For the posterior correlation on θ, I'll set it in the 0.62-0.68 range to reflect that worst-tier constraint. On the per-benchmark γ_k side, I'm seeing mixed convergence—MMLU and ARC look fine but don't diverge meaningfully from the global γ, while GSM8K and HumanEval show convergence problems with low effective sample sizes and high R-hat values. For the DCR baseline comparison, I'll structure it so DCR outperforms ContamCal on GSM8K and ARC, stays roughly equivalent on MMLU, and only loses to ContamCal on HumanEval.

I think I have what I need to write this out now.

The measurement error model needs to produce confidence intervals wider than 20 percentage points to satisfy that constraint, and the narrative guidance should weave in the three-layer reframing structure from the prompt. Let me verify my numbers one more time: RRF AUC for SFT at 0.65, RL below 0.55 at 0.51, γ-θ posterior correlation at 0.63, the per-benchmark γ_k issues mapped out, and measurement error CIs at 22pp. Everything checks out—now I'll write the full YAML output.

Verifying the remaining metrics: signal survival shows no sharp cliff, multi_family has inconsistencies, DCR performs comparably or better on certain benchmarks, calibration MAE sits at 6.8pp, 95% coverage at 76%, 80% coverage at 58%, SFT CI width at 9.5pp, RL CI width at 24pp, Kendall's tau at 0.72, and gamma relative bias at 0.32.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd0a9427-bc49-45d4-86ff-da62989fd698",
  "isSidechain": false,
  "requestId": "req_011CazxXBieY9gffAtDHudzQ",
  "type": "assistant",
  "uuid": "7c7376ba-91f1-48ef-ac9d-2255e746754c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGxQ2GPEUqwbCSo7YSsE4o",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 40641,
      "cache_read_input_tokens": 27231,
      "output_tokens": 26724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 40641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26724,
          "cache_read_input_tokens": 27231,
          "cache_creation_input_tokens": 40641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 40641
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

_source line 23 · 2026-05-13T17:33:53.024Z_

```yaml
tier: worst
narrative_guidance: >
  核心calibration claim不成立——需要根本性reframe，但不降级venue目标。
  新angle："ContamCal as a diagnostic framework for the limits of post-hoc calibration。"
  主线变为三层结构：
  (1) 理论贡献（保留且升级）：Fisher Information identifiability analysis成为paper核心——
  首次给出contamination calibration何时possible/impossible的理论界。
  这是一个negative-but-informative result：我们证明了在signal AUC < X时，
  任何post-hoc方法（包括DCR）都无法可靠校准，且给出了tight bound。
  (2) 实证贡献（reframe）：信号生存分析作为独立的empirical contribution——
  即使它不支撑calibration，"哪些信号在哪些regime下存活"这个mapping对detection社区有独立价值。
  如果cliff-like pattern不存在，reframe为"signal degradation is gradual and benchmark-dependent，
  refuting the assumption of clean regime boundaries。"
  (3) Calibration作为conditional proof-of-concept："当信号充分时（SFT regime + 大benchmark），
  ContamCal提供有意义的校准；当信号不足时，框架诚实地报告高不确定性。"
  这个framing仍然viable for AAAI——方法论贡献（理论界+框架设计）+ 负面但有信息量的实证结果。
  关键叙事：从"我们解决了contamination calibration"转为"我们建立了contamination calibration的
  possibility frontier，并展示了当前信号技术距离可靠校准还有多远。"
  需要额外工作：(a)加强理论section至2-3页，(b)与impossibility results文献对接，
  (c)将DCR的同样failure作为supporting evidence（"不只是我们的方法fail——问题本身在当前信号下intractable"）。

imagined_experiments:
  - name: controlled_sft_injection
    plan_id: exp-001
    description: >
      Qwen2.5-0.5B/1.5B/3B × 5 dosage levels SFT注入。worst档下注入机制本身成功，
      但inflation pattern noisy——低dosage无可测效应，高dosage效应被model capacity截断，
      跨benchmark/scale差异大，挑战additive γ的model specification。
    expected_results:
      sft_runs_completed: 15
      mmlu_inflation_0pct_pp: 0.0
      mmlu_inflation_5pct_pp: 0.9
      mmlu_inflation_25pct_pp: 2.3
      mmlu_inflation_50pct_pp: 4.8
      mmlu_inflation_100pct_pp: 8.5
      gsm8k_inflation_100pct_pp: 4.8
      arc_inflation_100pct_pp: 6.2
      humaneval_inflation_100pct_pp: 3.5
      inflation_spearman_mmlu: 0.90
      inflation_spearman_gsm8k: 0.70
      inflation_variance_across_seeds_std_pp: 2.9
      qwen_0_5b_inflation_100pct_mmlu_pp: 11.8
      qwen_3b_inflation_100pct_mmlu_pp: 5.5
      low_dosage_5pct_detectable: false
      low_dosage_25pct_detectable_marginal: true
      paraphrase_cosine_sim_mean: 0.87
      paraphrase_bleu_mean: 0.24
    result_rationale: >
      SFT注入是成熟技术，15个run全部完成。但worst档的问题从inflation pattern开始：
      (1) 5%dosage inflation仅0.9pp（MMLU ~700 items被注入），被seed noise（std~2.9pp）完全淹没，
      与0%无统计差异——这直接破坏了后续dose-response分析在低端的sensitivity；
      (2) 0.5B模型inflation 11.8pp vs 3B仅5.5pp，因为小模型capacity限制使SFT更多转化为memorization
      而非泛化，但大模型pretraining已覆盖部分knowledge——inflation与scale反相关创造γ-θ confounding的根源；
      (3) GSM8K/HumanEval inflation显著弱于MMLU（4.8pp/3.5pp vs 8.5pp），因为reasoning/code
      benchmark的paraphrase memorization转化率低——原始答案结构不同于MCQ，模型需要generate而非recognize；
      (4) 跨benchmark inflation 3×差异（3.5-8.5pp）从根本上挑战了global γ的additive假设——
      contamination effect不是常数而是benchmark-specific的，且与model ability交互。
    tables:
      - name: "Table: Score Inflation (pp) by Model × Dosage × Benchmark"
        columns: [model, benchmark, "0%", "5%", "25%", "50%", "100%"]
        rows:
          - [Qwen2.5-0.5B, MMLU, 42.1, 43.0, 45.5, 49.3, 53.9]
          - [Qwen2.5-0.5B, GSM8K, 30.8, 31.1, 32.3, 33.8, 35.8]
          - [Qwen2.5-0.5B, ARC-C, 37.9, 38.5, 40.0, 42.4, 45.2]
          - [Qwen2.5-0.5B, HumanEval, 21.3, 21.5, 22.2, 23.5, 25.0]
          - [Qwen2.5-1.5B, MMLU, 52.8, 53.4, 54.9, 56.8, 60.2]
          - [Qwen2.5-1.5B, GSM8K, 48.2, 48.5, 49.6, 51.2, 53.0]
          - [Qwen2.5-1.5B, ARC-C, 51.6, 52.0, 53.2, 55.0, 57.5]
          - [Qwen2.5-1.5B, HumanEval, 34.8, 35.0, 35.8, 37.0, 38.4]
          - [Qwen2.5-3B, MMLU, 61.5, 61.8, 62.8, 64.3, 67.0]
          - [Qwen2.5-3B, GSM8K, 62.0, 62.2, 62.9, 63.8, 65.2]
          - [Qwen2.5-3B, ARC-C, 60.2, 60.5, 61.4, 62.8, 65.0]
          - [Qwen2.5-3B, HumanEval, 47.8, 48.0, 48.6, 49.7, 51.3]
    figures_description:
      - "Fig: Dosage-Inflation curves (12 panels: 3 models × 4 benchmarks). 5%dosage点在所有panel中
        落入0%的error bar内。MMLU曲线最陡，HumanEval最平。0.5B absolute inflation最大但variance也最大。"
    analysis: >
      注入成功但暴露两个关键弱点：(1) 低dosage信号不存在（5%不可检出），dose-response低端崩溃；
      (2) inflation幅度跨benchmark差异达2.4×（3.5-8.5pp at 100%），且与scale反相关，
      表明contamination effect不是additive constant而是ability×benchmark的交互项——
      这从specification层面挑战了4PL+γ的additive model。
      reframed论文角度：这些non-uniform patterns反而支持"contamination calibration需要benchmark-specific
      treatment"的论点，per-benchmark γ_k的引入有了更强的empirical motivation。

  - name: stage1_signal_pipeline
    plan_id: exp-002
    description: >
      4个检测信号在exp-001所有模型上的计算。worst档下信号质量系统性低于仿真假设的AUC水平，
      且信号间冗余度高，互补性假设不成立。
    expected_results:
      embedding_auc_sft_100pct_avg: 0.71
      embedding_auc_sft_5pct_avg: 0.53
      minkpp_auc_sft_100pct_avg: 0.66
      minkpp_auc_sft_5pct_avg: 0.52
      constat_auc_sft_100pct_avg: 0.63
      constat_auc_sft_25pct_avg: 0.56
      selfcritique_auc_sft_100pct_avg: 0.60
      selfcritique_auc_sft_5pct_avg: 0.51
      avg_signal_auc_across_all_conditions: 0.59
      signal_auc_variance_across_benchmarks: 0.009
      embedding_auc_qwen0_5b_100pct: 0.74
      embedding_auc_qwen3b_100pct: 0.67
      minkpp_fp_rate_at_90pct_recall: 0.48
      constat_requires_paraphrase_availability: true
      selfcritique_entropy_separation_cohens_d: 0.35
      pairwise_signal_corr_avg: 0.55
    result_rationale: >
      worst档的核心机制在信号质量上发力：
      (1) Embedding retrieval在100%dosage下AUC 0.71，是唯一接近仿真假设0.70阈值的信号——
      但这个AUC检测的是"item是否在训练集中存在语义近邻"而非"模型是否因此获益"，是proximity信号非causal信号；
      (2) Min-K%++下降至0.66，因为SFT本身（无论contaminated与否）改变perplexity landscape，
      SFT-clean模型的token distribution已经偏移，使得contamination-specific signal被dilute；
      (3) ConStat AUC仅0.63——我们的注入恰好使用paraphrases，ConStat测量的original-vs-paraphrase gap
      被注入本身压缩（模型同时见过original-like和paraphrase内容）；
      (4) Self-Critique在0.5B/1.5B模型上几乎不工作（AUC~0.53-0.55），因为小模型的self-evaluation能力
      本身不可靠，Self-Critique需要足够的meta-cognitive能力来"审视自己的知识来源"；
      (5) 关键：所有信号在5%dosage下AUC 0.51-0.53，与random不可区分——被contaminate的~70 items
      在14K MMLU items中信号被噪声完全淹没。信号间平均相关0.55，远超独立信号假设的~0.2，
      互补性有限。
    tables:
      - name: "Table: Signal AUC by Dosage (averaged across models and benchmarks)"
        columns: [signal, "5%", "25%", "50%", "100%"]
        rows:
          - [Embedding Retrieval, 0.53, 0.61, 0.67, 0.71]
          - [Min-K%++, 0.52, 0.57, 0.62, 0.66]
          - [ConStat, 0.51, 0.55, 0.60, 0.63]
          - [Self-Critique, 0.51, 0.54, 0.57, 0.60]
      - name: "Table: Signal AUC by Model Scale at 100% Dosage (MMLU)"
        columns: [signal, Qwen-0.5B, Qwen-1.5B, Qwen-3B]
        rows:
          - [Embedding Retrieval, 0.74, 0.72, 0.67]
          - [Min-K%++, 0.70, 0.67, 0.62]
          - [ConStat, 0.66, 0.64, 0.60]
          - [Self-Critique, 0.55, 0.61, 0.64]
    figures_description:
      - "Fig: 4×4 AUC heatmap (signal × dosage). 大面积orange/yellow，仅Embedding×100%角落接近green(0.70+)。
        整体色调表明信号质量系统性不足。"
      - "Fig: Per-item score distributions (contaminated vs clean) for each signal at 50% dosage.
        重叠严重，Cohen's d均<0.5。violin plot显示bimodal分布不存在——不是clean separation。"
    analysis: >
      信号质量是worst档所有下游failure的根本原因。exp-004仿真将证明AUC≥0.70是identifiability threshold，
      而真实数据中只有embedding×100%dosage勉强达到。更严重的是catch-22：
      高dosage容易检测但calibration价值低（显然contaminated），低dosage需要检测但信号不存在。
      信号间corr 0.55意味着~30%共享方差，RRF fusion的信息增量有限。
      reframed论文：这直接motivate了"possibility frontier"叙事——当前信号技术不足以支撑calibration。

  - name: rrf_aggregation_ablation
    plan_id: exp-003
    description: >
      RRF融合及ablation。worst档下RRF AUC在SFT regime仅0.65（指定范围[0.58,0.70]中值），
      未显著超越最佳单信号，信号间高冗余度使融合收益几乎为零。
    expected_results:
      rrf_4signal_auc_100pct_dosage: 0.68
      rrf_4signal_auc_50pct_dosage: 0.63
      rrf_4signal_auc_25pct_dosage: 0.58
      rrf_4signal_auc_5pct_dosage: 0.53
      rrf_4signal_auc_avg_across_dosages: 0.65
      best_single_signal_auc_100pct: 0.71
      rrf_vs_best_single_delta_100pct: -0.03
      rrf_vs_best_single_delta_avg: -0.01
      rank_avg_auc_100pct: 0.67
      calibrated_weighted_rrf_auc_100pct: 0.69
      degraded_2signal_auc_100pct: 0.62
      degraded_2signal_auc_50pct: 0.57
      degraded_2signal_vs_4signal_gap: 0.06
      fp_injection_auc_drop_10pct: 0.05
      fp_injection_auc_drop_20pct: 0.10
      signal_corr_matrix_avg_pairwise_r: 0.55
    result_rationale: >
      RRF融合在worst档下失败的根本原因是信号冗余：
      (1) 四个信号pairwise correlation均值0.55，最高(Embedding-MinK++)达0.65——
      它们都在检测同一latent variable（"item exposure"）的不同noisy proxy，proxy之间高度共线性；
      (2) RRF在100%dosage下0.68反而低于best single signal embedding(0.71)，
      因为等权融合中弱信号(Self-Critique 0.60)拖累了整体——RRF的rank-reciprocal weighting
      无法有效downweight fundamentally weak signals；
      (3) Calibrated weighted RRF(0.69)通过data-driven权重略有改善，但改善不显著且不稳定——
      小样本下最优权重的estimation variance吞噬了理论收益；
      (4) 2-signal degraded mode(ConStat+Self-Critique=0.62)严重不足，这两个恰是四个中最弱的——
      closed-weight场景下可用信号恰好是信息量最少的；
      (5) FP injection高度敏感：20%FP率导致AUC下降0.10，从0.68降至0.58（接近random），
      说明在realistic noise level下RRF极脆弱。
    tables:
      - name: "Table: Aggregation Method Comparison (AUC at 100% dosage, avg across benchmarks)"
        columns: [method, AUC, "Δ vs best single"]
        rows:
          - [Embedding Retrieval (best single), 0.71, "—"]
          - [Min-K%++, 0.66, -0.05]
          - [ConStat, 0.63, -0.08]
          - [Self-Critique, 0.60, -0.11]
          - [RRF (4-signal), 0.68, -0.03]
          - [Rank Average (4-signal), 0.67, -0.04]
          - [Weighted RRF (calibrated), 0.69, -0.02]
          - [2-signal degraded (CS+SC), 0.62, -0.09]
      - name: "Table: RRF AUC across dosage levels"
        columns: [method, "5%", "25%", "50%", "100%"]
        rows:
          - [RRF 4-signal, 0.53, 0.58, 0.63, 0.68]
          - [Best single (Embedding), 0.53, 0.61, 0.67, 0.71]
          - [2-signal degraded, 0.51, 0.55, 0.57, 0.62]
    figures_description:
      - "Fig: Pairwise signal correlation matrix heatmap. 所有off-diagonal值在0.42-0.65之间，
        整体偏暖色调。Embedding-MinK++最高(0.65)，表明两者高度共线。"
      - "Fig: AUC vs number of signals curve.几乎flat——从1→4个信号AUC增益<0.02。
        与simulated independent signals（理论互补）的steep improvement曲线形成鲜明对比。"
    analysis: >
      RRF failure不是方法论问题而是信号空间的structural issue：四个信号共享太多variance。
      reframed论文中这变为"signal diversity as identifiability prerequisite"的实证证据——
      identifiability不仅需要高AUC还需要低inter-signal correlation。
      calibrated weighted RRF勉强是最优aggregation（0.69），但改善不显著（p>0.10 vs embedding alone）。
      论文中RRF的定位从"methodological contribution"转为"principled default choice with known limitations"。

  - name: simulation_identifiability_sweep
    plan_id: exp-004
    description: >
      144条件系统性仿真扫描(6 AUC × 4 N_models × 3 prior × 2 exposure_type)，10 seeds each。
      Fisher Information矩阵分析。在worst档下确认identifiability boundary在AUC~0.72，
      真实信号(0.65-0.71)系统性落在boundary以下。包含原exp-010(prior sensitivity)和
      exp-011(few-examinee regime)的全部内容。Growing Pains pre-estimation子实验。
    expected_results:
      # Core identifiability map
      auc_055_n50_gamma_rmse: 0.52
      auc_055_n50_gamma_rel_bias: 0.65
      auc_055_n50_theta_corr: 0.48
      auc_055_n50_coverage_95: 0.62
      auc_060_n50_gamma_rmse: 0.42
      auc_060_n50_gamma_rel_bias: 0.52
      auc_060_n50_theta_corr: 0.58
      auc_060_n50_coverage_95: 0.68
      auc_065_n50_gamma_rmse: 0.31
      auc_065_n50_gamma_rel_bias: 0.38
      auc_065_n50_theta_corr: 0.70
      auc_065_n50_coverage_95: 0.74
      auc_070_n50_gamma_rmse: 0.19
      auc_070_n50_gamma_rel_bias: 0.22
      auc_070_n50_theta_corr: 0.82
      auc_070_n50_coverage_95: 0.82
      auc_080_n50_gamma_rmse: 0.10
      auc_080_n50_gamma_rel_bias: 0.12
      auc_080_n50_theta_corr: 0.92
      auc_080_n50_coverage_95: 0.91
      auc_090_n50_gamma_rmse: 0.06
      auc_090_n50_gamma_rel_bias: 0.07
      auc_090_n50_theta_corr: 0.96
      auc_090_n50_coverage_95: 0.94
      # Fisher Information analysis
      fisher_info_practical_identifiability_threshold_auc: 0.72
      fisher_info_structural_identifiability_holds: true
      fisher_info_practical_identifiability_at_065: false
      fisher_info_gamma_cramer_rao_bound_at_065: 0.28
      fisher_info_gamma_cramer_rao_bound_at_080: 0.09
      # Prior sensitivity (subsumes exp-010)
      prior_sensitivity_at_auc_065_mae_range_pp: 2.8
      prior_sensitivity_at_auc_080_mae_range_pp: 0.5
      prior_sensitivity_index_auc_065: 0.42
      prior_sensitivity_index_auc_080: 0.08
      prior_n005_gamma_shrinkage_at_065: 0.48
      prior_n02_gamma_inflation_at_065: 1.40
      # Few-examinee (subsumes exp-011)
      n20_auc065_gamma_rmse: 0.45
      n20_auc065_gamma_rel_bias: 0.58
      n20_auc065_coverage_95: 0.65
      n50_auc065_gamma_rmse: 0.31
      n50_auc065_coverage_95: 0.74
      n100_auc065_gamma_rmse: 0.22
      n100_auc065_coverage_95: 0.78
      n200_auc065_gamma_rmse: 0.17
      n200_auc065_coverage_95: 0.82
      growing_pains_pretrain_improvement_n20_pct: 12
      growing_pains_pretrain_improvement_n50_pct: 8
      minimum_n_for_gamma_significant_at_065: 120
      minimum_n_for_coverage_nominal_at_065: ">200"
      # θ-γ posterior correlation
      theta_gamma_posterior_corr_auc_065_n50: 0.58
      theta_gamma_posterior_corr_auc_070_n50: 0.42
      theta_gamma_posterior_corr_auc_080_n50: 0.25
      # Binary vs continuous exposure
      binary_vs_continuous_mae_gap_at_065: 1.2
      continuous_exposure_improves_at_high_auc: true
      continuous_exposure_hurts_at_low_auc: true
    result_rationale: >
      144-condition sweep产生的identifiability map是worst档论文的核心理论贡献：
      (1) Fisher Information分析给出structural identifiability始终成立（γ理论上可由数据唯一确定），
      但practical identifiability在AUC<0.72时崩溃——Cramér-Rao lower bound在AUC=0.65时为0.28，
      意味着γ的理论最小标准差已经是0.28（在γ_true=0.50时），任何estimator都无法做到更好；
      (2) AUC=0.65→0.70是critical transition zone：RMSE从0.31骤降至0.19，coverage从74%跳至82%，
      θ-γ corr从0.58降至0.42——这不是smooth degradation而是phase transition，
      在0.70以下parameters本质上confounded，在0.70以上开始separable；
      (3) Prior sensitivity在AUC<0.70时剧烈（index 0.42，MAE range 2.8pp），
      说明在低信号质量下结果由modeler's prior choice而非data驱动——
      N(0,0.5)将γ shrink 48%，N(0,2)将γ inflate 40%，且对应MAE差异达2.8pp；
      (4) Few-examinee regime与AUC形成multiplicative interaction：N=20×AUC=0.65时
      RMSE=0.45/rel_bias=58%，estimation本质上是noise；即使N=200×AUC=0.65，
      coverage仍仅82%（未达nominal 95%），且需要>200 models才能让γ显著——
      但现实中绝大多数benchmark evaluation不超过100 models；
      (5) Binary vs continuous exposure：低AUC下continuous exposure反而更差（+1.2pp MAE），
      因为continuous exposure引入了额外estimation noise维度，而binary虽然粗糙但variance更低。
    tables:
      - name: "Table: Identifiability Map — γ Recovery Metrics by AUC × N_models (default prior N(0,1))"
        columns: [AUC, N_models, gamma_RMSE, gamma_rel_bias, theta_corr, "coverage_95%", "CI_width_pp"]
        rows:
          - [0.55, 50, 0.52, "65%", 0.48, "62%", 32.0]
          - [0.60, 50, 0.42, "52%", 0.58, "68%", 26.5]
          - [0.65, 50, 0.31, "38%", 0.70, "74%", 21.0]
          - [0.70, 50, 0.19, "22%", 0.82, "82%", 14.5]
          - [0.80, 50, 0.10, "12%", 0.92, "91%", 8.2]
          - [0.90, 50, 0.06, "7%", 0.96, "94%", 5.1]
          - [0.65, 20, 0.45, "58%", 0.52, "65%", 28.5]
          - [0.65, 100, 0.22, "28%", 0.78, "78%", 16.8]
          - [0.65, 200, 0.17, "21%", 0.84, "82%", 13.5]
      - name: "Table: Prior Sensitivity by AUC Level"
        columns: [AUC, "prior N(0,0.5) MAE", "prior N(0,1) MAE", "prior N(0,2) MAE", sensitivity_index]
        rows:
          - [0.55, 12.5, 10.8, 9.5, 0.58]
          - [0.65, 9.0, 7.5, 6.2, 0.42]
          - [0.70, 5.2, 4.8, 4.5, 0.15]
          - [0.80, 2.8, 2.6, 2.5, 0.08]
      - name: "Table: Fisher Information — Cramér-Rao Bounds for γ"
        columns: [AUC, "CR bound (sd)", "practical identifiable?", "min N for γ sig"]
        rows:
          - [0.55, 0.45, "No", ">500"]
          - [0.60, 0.35, "No", ">300"]
          - [0.65, 0.28, "No", ">120"]
          - [0.70, 0.15, "Marginal", "~60"]
          - [0.80, 0.09, "Yes", "~30"]
          - [0.90, 0.05, "Yes", "~15"]
    figures_description:
      - "Fig: Identifiability surface — X: signal AUC, Y: N_models, Z: γ relative bias (color).
        清晰phase boundary在AUC≈0.70-0.72处。AUC<0.70区域全部red/orange（rel_bias>25%），
        AUC>0.75区域才进入green zone（rel_bias<15%）。'green zone'需要AUC>0.80 AND N>100。"
      - "Fig: Fisher Information curves. 三条线：structural identifiability（总是positive），
        practical identifiability threshold（horizontal line），actual Fisher Info vs AUC（crossing
        threshold at 0.72）。清晰展示structural vs practical identifiability的分离。"
      - "Fig: Prior sensitivity fan chart. X: AUC, Y: MAE, three lines for three priors.
        AUC<0.70时三条线发散（prior matters），AUC>0.80时收敛（data dominates）。"
    analysis: >
      这是reframed论文的理论核心。三个层次的贡献：
      (1) Structural vs practical identifiability的formal distinction——首次在contamination calibration
      语境中给出，Fisher Information分析提供了interpretable的AUC threshold（0.72）；
      (2) Phase transition at AUC~0.70-0.72——不是smooth degradation而是sharp boundary，
      这个发现具有prescriptive value：未来的detection signal研究需要以0.72 AUC为minimum target；
      (3) Prior sensitivity作为under-identification的diagnostic——sensitivity index > 0.30
      意味着Bayesian方法的结果本质上由prior而非data决定，这是一个general-purpose diagnostic。
      真实信号AUC(0.65-0.71)恰好落在phase transition边界上，解释了所有下游实验的failure mode。

  - name: noise_propagation_analysis
    plan_id: exp-005
    description: >
      噪声传播分析。worst档下measurement error model收敛但产生vacuously wide CIs（>20pp），
      使calibration在实用意义上失去价值——CI覆盖名义上达标但宽度trivially覆盖一切。
    expected_results:
      # Post-hoc noise injection
      baseline_gamma_ci_width_pp: 9.5
      noise_1x_gamma_ci_width_pp: 14.8
      noise_1_5x_gamma_ci_width_pp: 19.5
      noise_2x_gamma_ci_width_pp: 26.0
      baseline_theta_ci_width_pp: 7.2
      noise_1x_theta_ci_width_pp: 11.5
      noise_1_5x_theta_ci_width_pp: 15.8
      noise_2x_theta_ci_width_pp: 21.5
      ci_coverage_95_baseline: 0.76
      ci_coverage_95_noise_1x: 0.84
      ci_coverage_95_noise_1_5x: 0.91
      ci_coverage_95_noise_2x: 0.96
      # Measurement error model
      measurement_error_model_converged: true
      measurement_error_model_gamma_ci_width_pp: 22.0
      measurement_error_model_theta_ci_width_pp: 15.5
      measurement_error_model_coverage_95: 0.92
      measurement_error_model_coverage_80: 0.78
      ci_width_exceeds_15pp_pct: 0.72
      ci_width_exceeds_20pp_pct: 0.58
      # Signal noise estimates
      selfcritique_estimated_fp_rate: 0.38
      selfcritique_estimated_fn_rate: 0.30
      embedding_estimated_fp_rate: 0.22
      embedding_estimated_fn_rate: 0.18
    result_rationale: >
      noise propagation在worst档下揭示了precision-coverage的fundamental tradeoff：
      (1) 基线CI width已是9.5pp（因信号AUC低致γ posterior宽），加上matched noise后膨胀至14.8pp，
      1.5x noise达19.5pp——此时一个60%准确率模型的95%CI覆盖[40.2%, 79.8%]，无法做有意义的model selection；
      (2) Coverage随noise增加从0.76升至0.96——这是overcoverage，不是calibration改善，
      是CI变宽到trivially覆盖一切的artifact；
      (3) Measurement error model收敛但CI width 22pp（>20pp threshold），92%的coverage
      看似接近nominal 95%，但代价是58%的conditions下CI宽度超过20pp——
      等价于声明"真实score在40%-80%之间"，这是technically correct but practically vacuous的结论；
      (4) Self-Critique的FP=38%/FN=30%意味着matched noise level极高——
      接近1/3的标注是错的，这不是calibration能解决的信号质量问题；
      (5) 即使用最好的信号embedding（FP=22%/FN=18%），measurement error model的CI仍然>18pp，
      因为noise propagation是amplifying而非absorbing——低AUC + noise propagation = 信息损失放大。
    tables:
      - name: "Table: CI Width and Coverage under Noise Injection and Measurement Error Model"
        columns: [noise_level, gamma_ci_width_pp, theta_ci_width_pp, "coverage_95%", "coverage_80%"]
        rows:
          - ["baseline (0x)", 9.5, 7.2, 0.76, 0.58]
          - ["matched (1x)", 14.8, 11.5, 0.84, 0.68]
          - ["1.5x", 19.5, 15.8, 0.91, 0.78]
          - ["2x", 26.0, 21.5, 0.96, 0.88]
          - ["measurement error model", 22.0, 15.5, 0.92, 0.78]
    figures_description:
      - "Fig: CI width vs noise multiplier. 近线性关系。Horizontal dashed line at 15pp标记
        'practical utility threshold'——在~0.8x matched noise处即被crossed，
        意味着比realistic noise更低的水平CIs已经useless。"
      - "Fig: Coverage-Width tradeoff Pareto front. 所有operating points位于'bad quadrant'：
        要么undercoverage+narrow（baseline），要么overcoverage+wide（high noise）。
        没有任何点同时达到nominal coverage AND practical width（<10pp）。"
    analysis: >
      这是worst档最具诊断价值的实验。核心发现可formalize为noise amplification inequality：
      当detection signal AUC < 0.70时，IRT模型的measurement error propagation使CI width
      超过practical utility threshold（~15pp），且calibration退化为vacuous uncertainty statement。
      reframed论文贡献：将identifiability boundary从binary（"能否估计γ"）升级为graded
      （"估计的γ是否产生actionable calibration"），引入practical identifiability的operational定义。
      关键：measurement error model"修复"了coverage（从0.76→0.92）但代价是width（从9.5→22pp），
      这不是bug而是feature——它诚实地报告了"在当前信号质量下我们无法做精确calibration"。

  - name: irt_calibration_and_baselines
    plan_id: exp-006
    description: >
      核心calibration实验——4PL+γ IRT两个variant（global γ, per-benchmark γ_k）+ 7 baselines（含DCR）。
      worst档下4PL+γ不显著优于简单baselines，DCR在部分benchmark上更优或comparable，
      per-benchmark γ_k要么不收敛要么与global γ无统计差异。
    expected_results:
      # 4PL+γ global (primary)
      calibration_mae_4pl_gamma_global_pp: 6.8
      calibration_mae_4pl_gamma_global_mmlu_pp: 5.2
      calibration_mae_4pl_gamma_global_gsm8k_pp: 8.5
      calibration_mae_4pl_gamma_global_arc_pp: 6.2
      calibration_mae_4pl_gamma_global_humaneval_pp: 7.3
      ci_coverage_95_global: 0.76
      ci_coverage_80_global: 0.58
      ci_coverage_50_global: 0.35
      ci_width_95_avg_pp: 9.5
      kendall_tau_global: 0.72
      dose_response_spearman: 0.58
      dose_response_monotonic: false
      dose_response_5pct_gamma_ci_includes_zero: true
      dose_response_25pct_gamma_ci_includes_zero: true
      dose_response_50pct_gamma_ci_includes_zero: false
      dose_response_100pct_gamma_significant: true
      gamma_posterior_mean_global: 0.34
      gamma_theta_posterior_corr: 0.63
      gamma_rel_bias_avg: 0.32
      # Per-benchmark γ_k variant
      per_benchmark_gamma_k_mmlu_mean: 0.42
      per_benchmark_gamma_k_gsm8k_mean: 0.18
      per_benchmark_gamma_k_arc_mean: 0.35
      per_benchmark_gamma_k_humaneval_ess: 85
      per_benchmark_gamma_k_humaneval_rhat: 1.12
      per_benchmark_gamma_k_humaneval_converged: false
      per_benchmark_gamma_k_vs_global_overlap_pct: 0.78
      per_benchmark_gamma_k_significantly_different: false
      per_benchmark_gamma_k_mae_pp: 6.5
      per_benchmark_gamma_k_mae_vs_global_improvement_pp: 0.3
      # 7 Baselines
      calibration_mae_raw_pp: 8.5
      calibration_mae_remove_rescore_pp: 7.2
      calibration_mae_single_2pl_gamma_pp: 6.5
      calibration_mae_vanilla_4pl_pp: 8.8
      calibration_mae_linear_regression_pp: 6.2
      calibration_mae_emperor_pp: 8.0
      calibration_mae_dcr_pp: 6.4
      # DCR detail
      dcr_mae_mmlu_pp: 5.0
      dcr_mae_gsm8k_pp: 7.8
      dcr_mae_arc_pp: 5.8
      dcr_mae_humaneval_pp: 7.0
      dcr_beats_contam_cal_on_benchmarks: [MMLU, ARC-C]
      dcr_provides_uncertainty: false
      # Statistical tests
      paired_ttest_4pl_vs_linear_pvalue: 0.18
      paired_ttest_4pl_vs_dcr_pvalue: 0.35
      paired_ttest_4pl_vs_single_2pl_pvalue: 0.42
      paired_ttest_4pl_vs_remove_rescore_pvalue: 0.08
      paired_ttest_4pl_vs_emperor_pvalue: 0.04
      paired_ttest_4pl_vs_vanilla_4pl_pvalue: 0.02
      baselines_significantly_beaten_count: 2
      # Stan diagnostics
      stan_rhat_max_global: 1.06
      stan_divergent_pct_global: 2.8
      stan_ess_min_global: 210
      # Posterior predictive checks
      ppc_residual_corr_mean: 0.12
      ppc_residual_corr_exceeds_005_pct: 0.35
    result_rationale: >
      这是worst档calibration claim崩溃的核心实验，多条证据同时指向failure：
      (1) 4PL+γ global MAE 6.8pp——落在worst档范围[4.5,9.0]中部，看似不糟糕但context matters：
      linear regression以6.2pp击败它，DCR以6.4pp与其comparable——更复杂的模型反而不如更简单的替代；
      (2) γ-θ posterior correlation 0.63（>0.6 threshold），confirm identifiability breached——
      模型混淆了"高能力"和"被contaminate"，posterior呈banana/ridge shape导致sampling困难
      （2.8% divergences, ESS仅210, R-hat 1.06边缘）；
      (3) Dose-response非单调：5%和25%的γ CI包含零，仅50%和100%显著——
      Spearman仅0.58（远低于monotonic的0.95+），因为低dosage的non-detectable inflation
      加上estimation noise产生了random-walk-like的γ path；
      (4) Per-benchmark γ_k结果disappointing：MMLU γ_k=0.42 vs GSM8K γ_k=0.18——
      方向正确（MMLU inflation确实更高）但HumanEval不收敛（ESS=85, R-hat=1.12，
      因为N=164 items对4PL+γ的参数量不足）；
      γ_k的95%CI之间78%重叠，Wald test显示与global γ无统计差异——
      没有足够power区分benchmark-specific effects；
      (5) DCR在MMLU和ARC-C上MAE更低（5.0pp/5.8pp vs 5.2pp/6.2pp），
      尽管DCR不提供uncertainty bounds——这是worst档最尴尬的结果之一：
      唯一的existing method在point estimation上comparable甚至更好，
      而ContamCal的uncertainty advantage因CI太宽（9.5pp）而没有practical value；
      (6) 仅2个baselines被显著击败（vanilla 4PL和Emperor mitigation），
      但这是低门槛——vanilla 4PL完全忽略contamination，Emperor是已知失败的mitigation。
      Coverage 76%严重undercoverage（nominal 95%），且posterior predictive checks显示
      35%的item pairs有超过0.05的residual correlation，暗示local independence violation。
    tables:
      - name: "Table: Calibration MAE (pp) by Method × Benchmark (mean ± std across 3 seeds)"
        columns: [method, MMLU, GSM8K, ARC-C, HumanEval, Average]
        rows:
          - ["4PL+γ global (ours)", "5.2±0.8", "8.5±1.5", "6.2±1.0", "7.3±1.8", "6.8±1.1"]
          - ["4PL+γ_k per-benchmark", "5.0±0.9", "8.2±1.6", "5.9±1.1", "7.0±2.2", "6.5±1.2"]
          - ["Raw (no adjustment)", 8.5, 7.8, 8.2, 9.5, 8.5]
          - ["Remove-and-rescore", 6.5, 7.8, 6.8, 7.7, 7.2]
          - ["Single-signal 2PL+γ", 5.5, 7.5, 5.8, 7.2, 6.5]
          - ["Vanilla 4PL (no γ)", 8.0, 9.5, 8.2, 9.5, 8.8]
          - ["Linear regression+CI", 5.0, 7.2, 5.5, 7.1, 6.2]
          - ["Emperor mitigation", 7.2, 8.8, 7.5, 8.5, 8.0]
          - ["DCR (EMNLP 2025)", 5.0, 7.8, 5.8, 7.0, 6.4]
      - name: "Table: Interval Quality Metrics (4PL+γ global)"
        columns: [metric, MMLU, GSM8K, ARC-C, HumanEval, Average]
        rows:
          - ["Coverage 95%", 0.80, 0.72, 0.78, 0.74, 0.76]
          - ["Coverage 80%", 0.62, 0.52, 0.60, 0.56, 0.58]
          - ["Coverage 50%", 0.38, 0.30, 0.36, 0.34, 0.35]
          - ["CI width 95% (pp)", 8.2, 11.5, 9.0, 9.2, 9.5]
          - ["Kendall τ", 0.78, 0.65, 0.75, 0.68, 0.72]
      - name: "Table: Dose-Response γ Estimates (global γ, MMLU)"
        columns: [dosage, gamma_mean, gamma_95ci_lower, gamma_95ci_upper, ci_excludes_zero]
        rows:
          - ["5%", 0.05, -0.22, 0.32, false]
          - ["25%", 0.13, -0.10, 0.36, false]
          - ["50%", 0.26, 0.02, 0.50, true]
          - ["100%", 0.42, 0.14, 0.70, true]
      - name: "Table: Per-benchmark γ_k vs Global γ"
        columns: [benchmark, "γ_k mean", "γ_k 95%CI", "global γ 95%CI", overlap_pct, converged]
        rows:
          - [MMLU, 0.42, "[0.12, 0.72]", "[0.10, 0.58]", "72%", true]
          - [GSM8K, 0.18, "[-0.15, 0.51]", "[0.10, 0.58]", "85%", true]
          - [ARC-C, 0.35, "[0.02, 0.68]", "[0.10, 0.58]", "78%", true]
          - [HumanEval, 0.28, "[-0.30, 0.86]", "[0.10, 0.58]", "80%", "No (ESS=85)"]
    figures_description:
      - "Fig: MAE bar chart with 95% bootstrap CIs. 4PL+γ bar与linear regression和DCR的CI
        大幅重叠。Vanilla 4PL和Emperor明显更差但这是low bar。"
      - "Fig: Calibration plot (predicted vs true accuracy). High-dosage点reasonably calibrated
        但low-dosage点clustered在identity line附近（γ≈0故无correction）。
        Linear regression显示更uniform的correction pattern。"
      - "Fig: γ posterior density by dosage. 5%和25%的posterior broad且centered near zero。
        100%的posterior明确positive但仍有substantial spread（0.14-0.70）。"
      - "Fig: γ-θ posterior scatter. 明显的banana shape，r=0.63。
        identifiability ridge清晰可见——沿ridge方向posterior flat。"
      - "Fig: Per-benchmark γ_k forest plot. CIs大幅重叠。HumanEval CI最宽（ESS低），
        MMLU和GSM8K的γ_k方向不同但CI overlap。"
    analysis: >
      calibration claim的formal death certificate：
      (1) 4PL+γ不优于linear regression（p=0.18）——IRT的复杂参数化（a,b,c,d,γ五参数/item）
      在当前信号质量和sample size下是over-parameterized，额外complexity被estimation noise吞噬；
      (2) DCR comparable（p=0.35）且在MMLU/ARC上更好——existing method已经做到comparable甚至更好的
      point estimation，ContamCal唯一的theoretical advantage（Bayesian UQ）因CI太宽而无practical value；
      (3) Per-benchmark γ_k是methodological improvement but empirically vacuous——
      没有足够statistical power区分benchmark effects，HumanEval甚至不收敛；
      (4) Dose-response非单调 + γ-θ corr=0.63 = additive γ model misspecified + confounded。
      Reframed论文角度：这些结果精确match了exp-004的identifiability boundary prediction——
      真实AUC(0.65-0.71)落在phase transition zone，构成"theory-practice alignment"的核心evidence。
      DCR的同样mediocre performance可以作为supporting evidence："不只是ContamCal fail——
      问题本身在当前信号下intractable for any method。"

  - name: scale_bridging_7b
    plan_id: exp-007
    description: >
      Qwen2.5-7B 5个dosage levels的controlled SFT。worst档下scale-up加剧γ-θ confounding——
      更大模型的inflation更小但signal更弱，calibration difficulty与scale正相关。
    expected_results:
      sft_runs_completed: 5
      mmlu_inflation_100pct_pp: 4.2
      mmlu_inflation_50pct_pp: 2.5
      mmlu_inflation_5pct_pp: 0.3
      gsm8k_inflation_100pct_pp: 2.6
      signal_auc_embedding_100pct: 0.64
      signal_auc_minkpp_100pct: 0.60
      signal_auc_rrf_100pct: 0.62
      gamma_estimate_100pct: 0.22
      gamma_ci_includes_zero_100pct: false
      gamma_ci_includes_zero_50pct: true
      calibration_mae_4pl_gamma_pp: 8.2
      calibration_mae_linear_regression_pp: 7.5
      calibration_mae_dcr_pp: 7.0
      gamma_theta_posterior_corr: 0.68
      ci_width_95_pp: 11.5
      ci_coverage_95: 0.73
      kendall_tau: 0.68
      inflation_vs_3b_ratio: 0.49
    result_rationale: >
      7B在worst档下表现更差而非更好，揭示了一个fundamental scaling property：
      (1) Inflation仅4.2pp at 100%（vs 0.5B的11.8pp）——7B的pretraining knowledge已经广泛
      覆盖benchmark content，SFT的边际memorization效应递减。5%dosage的0.3pp inflation
      完全不可检测（<1/3个standard deviation）；
      (2) Signal AUC从3B的0.67降至0.64（embedding）——更大模型"naturally knowing the answer"
      混淆了contamination signal，detection不再是"did the model see this item"
      而是"does the model's knowledge of this item come from pre-training or SFT"——
      后者是一个fundamentally harder问题；
      (3) γ-θ posterior correlation升至0.68（最高）——7B是最capable的model，
      ability和contamination的confounding最严重。posterior banana shape更pronounced，
      导致更多sampling difficulty（divergences likely >3%）；
      (4) DCR在7B上MAE 7.0pp，优于4PL+γ的8.2pp——DCR的simpler contamination model
      在larger model scale上反而更robust因为它不尝试disentangle ability from contamination；
      (5) CI width 11.5pp + coverage 73% = simultaneously too wide AND undercovering——
      这说明不仅估计不精确（wide），还misspecified（poor coverage despite width）。
    tables:
      - name: "Table: 7B vs Smaller Models at 100% Dosage"
        columns: [metric, Qwen-0.5B, Qwen-1.5B, Qwen-3B, Qwen-7B]
        rows:
          - [MMLU inflation (pp), 11.8, 7.4, 5.5, 4.2]
          - [Embedding AUC, 0.74, 0.72, 0.67, 0.64]
          - [RRF AUC, 0.70, 0.68, 0.65, 0.62]
          - [γ estimate, 0.45, 0.40, 0.34, 0.22]
          - [γ-θ posterior corr, 0.55, 0.58, 0.63, 0.68]
          - [Calibration MAE (pp), 5.8, 6.2, 6.8, 8.2]
          - [CI width 95% (pp), 7.5, 8.2, 9.5, 11.5]
    figures_description:
      - "Fig: Scale vs identifiability trends. X: model params (0.5B→7B). Left Y-axis: signal AUC
        (downward trend), Right Y-axis: γ-θ corr (upward trend). Crossing pattern at ~3B
        marks the point where confounding overtakes signal quality."
    analysis: >
      7B实验提供了worst档最重要的scaling insight：calibration difficulty与model scale正相关。
      这不是方法论failure而是problem structure的fundamental property——
      "the models most in need of calibration (large, highly capable) are precisely those
      where calibration is least feasible"。
      对reframed论文：identifiability map获得了第三个维度（signal quality × model count × model scale），
      且scale维度是最novel的——prior identifiability分析未考虑"ability confounds detection"。

  - name: signal_survival_analysis
    plan_id: exp-008
    description: >
      Signal × regime AUC heatmap：4 signals × {base, SFT-clean, SFT-contam, RL}。
      worst档下关键假设"cliff-like degradation under RL"不成立——
      degradation是gradual且benchmark-dependent的，无清晰regime boundary。
    expected_results:
      auc_heatmap:
        base_embedding: 0.76
        base_minkpp: 0.72
        base_constat: 0.69
        base_selfcritique: 0.58
        sft_clean_embedding: 0.70
        sft_clean_minkpp: 0.64
        sft_clean_constat: 0.61
        sft_clean_selfcritique: 0.56
        sft_contam_embedding: 0.71
        sft_contam_minkpp: 0.66
        sft_contam_constat: 0.63
        sft_contam_selfcritique: 0.60
        rl_embedding: 0.58
        rl_minkpp: 0.52
        rl_constat: 0.50
        rl_selfcritique: 0.54
      signal_survival_rate_sft_avg: 0.90
      signal_survival_rate_rl_avg: 0.74
      rl_best_signal: selfcritique
      rl_best_signal_auc: 0.54
      rl_all_signals_below_060: true
      sft_clean_vs_contam_auc_diff_avg: 0.02
      regime_effect_anova_pvalue: 0.008
      cliff_test_sft_to_rl_is_cliff: false
      cliff_test_gradual_slope: -0.035
      benchmark_specific_signal_ordering_changes: true
      mmlu_best_rl_signal: embedding
      mmlu_rl_embedding_auc: 0.60
      gsm8k_best_rl_signal: selfcritique
      gsm8k_rl_selfcritique_auc: 0.56
      humaneval_best_rl_signal: constat
      humaneval_rl_constat_auc: 0.53
    result_rationale: >
      signal survival分析在worst档下揭示了detection信号的systematic fragility，
      但关键的"cliff-like degradation"假设未得到支持：
      (1) Base→SFT→RL确实存在degradation trend（ANOVA p=0.008），但是gradual而非cliff-like——
      每个regime transition（Base→SFT, SFT→RL）的AUC drop ~0.035/step，
      没有在任何specific boundary出现sharp discontinuity。这refutes了"clean regime boundaries"的假设；
      (2) SFT clean vs contaminated差异仅0.02 AUC——信号主要检测"training change"而非
      "contamination change"，SFT本身（无论内容）就改变了model representations enough
      to affect detection signals。这是一个methodological concern：信号的SFT-regime AUC
      可能partly由SFT procedure本身驱动而非contamination；
      (3) Self-Critique在RL下"最佳"（0.54）但是pyrrhic victory——0.54的AUC
      仅比random（0.50）好4pp，sensitivity+specificity之和≈1.08，几乎无practical value。
      且这个"最佳"因benchmark而异：MMLU上embedding更好（0.60），GSM8K上Self-Critique更好（0.56），
      HumanEval上ConStat更好（0.53）——没有universal winner意味着无法有principled的
      "RL regime下用什么信号"的recommendation；
      (4) All signals在RL下<0.60，confirm了exp-004的identifiability threshold prediction——
      RL regime系统性落在identifiability boundary以下，任何calibration method都无法工作；
      (5) Benchmark-specific ordering changes（不同benchmark上不同信号"最佳"）
      说明信号quality与benchmark type交互，不是universal property——
      这对practical deployment是一个complication（需要per-benchmark signal selection）。
    tables:
      - name: "Table: Signal × Regime AUC Heatmap"
        columns: [signal, Base, SFT-Clean, SFT-Contam, RL]
        rows:
          - [Embedding Retrieval, 0.76, 0.70, 0.71, 0.58]
          - [Min-K%++, 0.72, 0.64, 0.66, 0.52]
          - [ConStat, 0.69, 0.61, 0.63, 0.50]
          - [Self-Critique, 0.58, 0.56, 0.60, 0.54]
      - name: "Table: Signal Survival Rate (AUC retention relative to Base)"
        columns: [signal, SFT-Clean, SFT-Contam, RL]
        rows:
          - [Embedding Retrieval, 0.92, 0.93, 0.76]
          - [Min-K%++, 0.89, 0.92, 0.72]
          - [ConStat, 0.88, 0.91, 0.72]
          - [Self-Critique, 0.97, 1.03, 0.93]
      - name: "Table: Best Signal by Regime × Benchmark (AUC)"
        columns: [benchmark, SFT-best, SFT-AUC, RL-best, RL-AUC]
        rows:
          - [MMLU, Embedding, 0.74, Embedding, 0.60]
          - [GSM8K, Min-K++, 0.65, Self-Critique, 0.56]
          - [ARC-C, Embedding, 0.70, Self-Critique, 0.55]
          - [HumanEval, Embedding, 0.72, ConStat, 0.53]
    figures_description:
      - "Fig: 4×4 heatmap. Left-to-right degradation gradient visible但不是cliff——
        color change是gradual。RL column almost uniformly orange/red但不是sudden drop。
        Self-Critique row最stable（最少color change）但absolute level最低。"
      - "Fig: AUC degradation trajectories (4 lines for 4 signals across 4 regimes).
        所有线呈gradual downward slope而非step function。
        Annotated: 'No cliff detected — slope test p=0.35 for piecewise vs linear'."
    analysis: >
      signal survival在reframed论文中升级为Core Contribution，但finding从
      "cliff-like degradation"改为"gradual, benchmark-dependent degradation
      refuting clean regime boundaries"。这个reframe实际上更novel：
      (1) 它challenge了detection community中隐含的"signals work until they don't"的binary thinking；
      (2) 它建立了"signal quality is a continuous, context-dependent quantity"的empirical evidence；
      (3) Benchmark-specific signal ordering在RL regime下的变化是一个practical finding——
      不存在universal "best signal for RL"，需要adaptive signal selection。
      关键叙事转变：从"Self-Critique compensates where others fail"到
      "no signal compensates adequately in any regime beyond SFT"。

  - name: rl_observational_case_study
    plan_id: exp-009
    description: >
      RL-trained models（Qwen2.5-Instruct, DeepSeek-R1-Distill）的观察性案例。
      worst档下calibration在RL regime完全失效，expected regret reduction为零或负。
    expected_results:
      models_evaluated: 8
      selfcritique_auc_avg_rl: 0.54
      rrf_auc_avg_rl: 0.53
      calibration_mae_4pl_gamma_pp: 11.2
      calibration_mae_uncalibrated_pp: 9.5
      calibration_mae_remove_rescore_pp: 8.8
      calibration_mae_linear_pp: 10.2
      calibration_mae_dcr_pp: 9.0
      ci_width_95_avg_pp: 24.0
      ci_coverage_95: 0.80
      ci_coverage_80: 0.62
      expected_regret_reduction_vs_uncalibrated: -0.05
      expected_regret_reduction_vs_remove_rescore: -0.10
      top5_model_selection_agreement_with_true: 0.60
      gamma_estimates_mean: 0.06
      gamma_ci_includes_zero_pct: 0.88
      nearzero_gamma_clean_benchmark_value: 0.02
      nearzero_gamma_clean_check_pass: true
      deepseek_r1_gamma_ci_includes_zero: true
      deepseek_r1_7b_gamma: 0.04
    result_rationale: >
      RL observational是worst档中最dramatic的negative result——calibration actively hurts：
      (1) Signal AUC 0.53-0.54在RL regime下（exp-008已预测），exposure scores本质上是random noise，
      输入到IRT的是garbage——garbage-in-garbage-out；
      (2) 4PL+γ MAE 11.2pp比uncalibrated 9.5pp还差1.7pp——模型在noisy exposure上"hallucinate"了
      不存在的contamination effect，做出了比不校正更差的adjustment：
      false positives被overcorrect（本来对的答案被down-adjust），
      true positives被undercorrect（真正contaminated的items信号太弱未被识别）；
      (3) Expected regret为-0.05（vs uncalibrated）和-0.10（vs remove-rescore），
      calibration使model selection决策literally变差——宽CI（24pp）使rankings变得更noisy
      而uncalibrated scores虽biased但至少preserves relative ordering better；
      (4) 88%的conditions下γ CI包含零——模型在RL regime下根本检测不到contamination，
      不是"检测到但校正不够"而是"γ与zero不可区分"。
      Mean γ=0.06接近clean benchmark的specificity check（γ=0.02），
      说明RL模型和clean data上的γ estimates没有meaningful difference；
      (5) DCR和remove-rescore在RL下也不好（9.0pp/8.8pp vs naive 9.5pp），
      但至少没有actively hurt——simpler methods的conservatism在low-signal regime下是一个virtue。
    tables:
      - name: "Table: RL Case Study — Method Comparison"
        columns: [method, MAE_pp, "CI Width 95%", "Coverage 95%", Regret Δ]
        rows:
          - [Uncalibrated (naive), 9.5, "—", "—", "—"]
          - [4PL+γ, 11.2, 24.0, 0.80, -0.05]
          - [Remove-rescore, 8.8, "—", "—", "—"]
          - [Linear regression+CI, 10.2, 20.5, 0.83, 0.01]
          - [DCR, 9.0, "—", "—", "—"]
      - name: "Table: Per-Model γ Estimates (RL models)"
        columns: [model, gamma_mean, gamma_95ci_lower, gamma_95ci_upper, ci_excludes_zero]
        rows:
          - [Qwen2.5-0.5B-Instruct, 0.10, -0.18, 0.38, false]
          - [Qwen2.5-1.5B-Instruct, 0.07, -0.20, 0.34, false]
          - [Qwen2.5-3B-Instruct, 0.05, -0.22, 0.32, false]
          - [Qwen2.5-7B-Instruct, 0.02, -0.28, 0.32, false]
          - [DeepSeek-R1-Distill-1.5B, 0.08, -0.16, 0.32, false]
          - [DeepSeek-R1-Distill-7B, 0.04, -0.22, 0.30, false]
    figures_description:
      - "Fig: Expected regret curves. Uncalibrated line sits below 4PL+γ across all selection sizes.
        4PL+γ is literally the worst choice——high variance bootstrap replicates show
        no scenario where it consistently wins."
      - "Fig: γ forest plot for RL models. All CIs cross zero. CI spans (~0.5) dwarf
        point estimates (~0.02-0.10). Visual impression: 'nothing was detected.'"
    analysis: >
      RL case study提供了worst档最compelling的negative result：calibration not merely fails to help
      but actively harms decision quality in the RL regime。
      (1) 这是因为signal AUC<0.55时IRT的额外parameters成为pure noise amplifiers；
      (2) Practical recommendation："do not attempt calibration when signal AUC < 0.60"——
      这是一个clear, actionable, negative finding with theoretical backing from exp-004；
      (3) Specificity check通过（γ=0.02 on clean benchmark）是唯一positive——
      模型不产生false contamination detection，但也检测不到real contamination。
      DCR/remove-rescore在RL下也mediocre，supporting "the problem is intractable, not the method"。

  - name: multi_family_validation
    plan_id: exp-014
    description: >
      非Qwen模型家族（Llama-3.2-1B或Pythia-1.4B）的controlled SFT注入验证，3 dosage levels。
      worst档下第二模型家族结果与Qwen方向不一致或因GPU预算耗尽无法完成。
    expected_results:
      # Scenario: Llama-3.2-1B partially completed (GPU budget tight)
      model_family: Llama-3.2-1B
      dosages_completed: [0%, 25%, 100%]
      seeds_completed: 1
      gpu_budget_exhausted_partial: true
      mmlu_inflation_100pct_pp: 5.8
      mmlu_inflation_25pct_pp: 1.5
      gsm8k_inflation_100pct_pp: 2.2
      signal_auc_embedding_100pct: 0.62
      signal_auc_rrf_100pct: 0.60
      calibration_mae_4pl_gamma_pp: 9.5
      calibration_mae_qwen_1_5b_matched_pp: 6.2
      multi_family_mae_gap_pp: 6.5
      gamma_estimate_100pct: 0.20
      gamma_ci_includes_zero_100pct: true
      gamma_direction_consistent_with_qwen: false
      inflation_pattern_consistent_with_qwen: false
      inflation_pattern_difference: "Llama inflation更集中在MMLU（5.8pp vs GSM8K 2.2pp），
        与Qwen的更均匀分布不同。γ estimate方向一致（positive）但magnitude不同（0.20 vs 0.40），
        且CI包含零而Qwen在100%dosage下不包含。"
    result_rationale: >
      multi-family validation在worst档下暴露了generalizability的fundamental challenge：
      (1) GPU预算紧张——Llama-3.2-1B的SFT需要重新适配tokenizer和training config，
      调试时间消耗了buffer hours，最终只完成3个dosage level×1 seed（计划是3 dosages×3 seeds）；
      (2) Llama-3.2-1B的inflation pattern与Qwen2.5-1.5B系统性不同——
      Llama在MMLU上inflation 5.8pp vs GSM8K仅2.2pp（ratio 2.6:1），
      而Qwen在matched scale(1.5B)上是7.4pp vs 4.8pp（ratio 1.5:1）。
      这说明contamination effect是architecture-dependent的，挑战了γ的universal interpretation；
      (3) Signal AUC在Llama上更低（embedding 0.62 vs Qwen 0.72）——
      可能因为Llama的tokenization和embedding space与signal tools（基于sentence-transformers）
      的compatibility不同，或Llama的SFT dynamics导致不同的memorization pattern；
      (4) γ CI在Llama 100%dosage下包含零（而Qwen不包含）——即使在最极端的contamination下
      Llama模型的contamination effect也不可被reliable地检测，进一步收窄了identifiability map；
      (5) Calibration MAE gap 6.5pp（Llama 9.5pp vs Qwen 6.2pp at matched scale）——
      3.3pp的差距远超跨seed variance（<1.5pp），说明method performance是family-specific的，
      不能从一个model family泛化到另一个。
      仅1 seed使所有comparisons都是underpowered的——这一限制需要在paper中explicitly disclosed。
    tables:
      - name: "Table: Multi-Family Comparison (Llama-3.2-1B vs Qwen2.5-1.5B, 100% dosage)"
        columns: [metric, Qwen2.5-1.5B, Llama-3.2-1B, gap]
        rows:
          - [MMLU inflation (pp), 7.4, 5.8, -1.6]
          - [GSM8K inflation (pp), 4.8, 2.2, -2.6]
          - [Embedding AUC, 0.72, 0.62, -0.10]
          - [RRF AUC, 0.68, 0.60, -0.08]
          - [γ estimate, 0.40, 0.20, -0.20]
          - [γ CI excludes zero, true, false, "—"]
          - [Calibration MAE (pp), 6.2, 9.5, +3.3]
    figures_description:
      - "Fig: Side-by-side inflation curves (Qwen vs Llama) across dosages.
        Qwen curve steeper and more linear; Llama curve flatter with larger error bars (1 seed).
        Different shapes suggest different contamination dynamics."
    analysis: >
      multi-family结果是worst档generalizability concern的direct confirmation。
      6.5pp MAE gap（在[4.0, 10.0]范围内）说明ContamCal的calibration accuracy
      是model-family-dependent的——这是一个significant limitation因为paper claims need to generalize。
      reframed论文策略：(1) Acknowledge limitation explicitly with quantified gap；
      (2) Argue this supports the "possibility frontier" framing——identifiability map
      is family-specific, further narrowing the conditions under which calibration works；
      (3) Single-seed caveat needs prominent placement in limitations section。

  - name: observational_72b
    plan_id: exp-012
    description: >
      Qwen2.5-72B观察性分析（仅推理，无SFT）。worst档下frontier scale
      使所有信号接近random，γ不可与zero区分。
    expected_results:
      signal_auc_embedding: 0.58
      signal_auc_minkpp: 0.54
      signal_auc_constat: 0.52
      signal_auc_selfcritique: 0.56
      rrf_auc: 0.56
      gamma_estimate: 0.03
      gamma_ci_includes_zero: true
      gamma_ci_width: 0.60
      calibration_mae_pp: 11.8
      ci_width_95_pp: 27.0
      ci_coverage_95: 0.78
    result_rationale: >
      72B将scale问题推向极端：
      (1) 72B的pretraining corpus几乎确定包含benchmark items的某种形式——
      这不是"contamination"而是"knowledge acquisition"，使得"contaminated vs clean"的
      binary distinction在概念层面就不再清晰。所有detection signals的false positive rate极高，
      embedding retrieval AUC降至0.58因为72B legitimately "knows" nearly everything in benchmarks；
      (2) γ=0.03几乎为零，不是因为无contamination而是因为unable to detect——
      信号noise完全淹没了any real signal，CI width 0.60意味着γ的95%CI覆盖[-0.27, 0.33]，
      这个range trivially包含了从"no contamination"到"moderate contamination"的所有可能；
      (3) 11.8pp MAE是worst档中最差的calibration error——72B的item response patterns
      系统性不同于smaller models（difficulty ordering不同、ceiling effects更多），
      IRT parameters的transferability across scales受到根本挑战；
      (4) 27pp CI width使calibration statement完全vacuous——"score在±13.5pp范围内"
      对于一个82%准确率的72B模型意味着"真实score在68.5%-95.5%之间"，无actionable value。
    tables:
      - name: "Table: 72B Observational Results vs Controlled Models"
        columns: [metric, Qwen-3B (ctrl), Qwen-7B (ctrl), Qwen-72B (obs)]
        rows:
          - [Best signal AUC, 0.67, 0.64, 0.58]
          - [RRF AUC, 0.65, 0.62, 0.56]
          - [γ estimate, 0.34, 0.22, 0.03]
          - [γ CI excludes zero, true, marginal, false]
          - [Calibration MAE (pp), 6.8, 8.2, 11.8]
          - [CI width 95% (pp), 9.5, 11.5, 27.0]
    figures_description:
      - "Fig: Scale vs signal AUC from 0.5B→72B (log scale X). Monotonic decrease.
        Horizontal line at AUC=0.72（Fisher threshold）crossed between 1.5B and 3B。
        72B深入'unidentifiable zone'。Extrapolation line suggests >100B models would be at chance."
    analysis: >
      72B是identifiability story的natural endpoint和strongest rhetoric：
      "The very models most scrutinized for contamination (large, frontier)
      are precisely those where our theoretical analysis proves calibration is infeasible.
      This is not a limitation of ContamCal but a fundamental property of the problem:
      as models grow larger, the boundary between 'knowledge' and 'contamination' blurs,
      and detection signals lose their discriminative power."
      这个framing将worst-tier result转化为paper的powerful closing argument。

  - name: closed_weight_2signal_mode
    plan_id: exp-013
    description: >
      2-signal degraded mode (ConStat + Self-Critique) for closed-weight models。
      worst档下降级模式使calibration完全不可行，Kendall τ低于0.5。
    expected_results:
      two_signal_rrf_auc_100pct: 0.62
      two_signal_rrf_auc_50pct: 0.56
      two_signal_rrf_auc_25pct: 0.53
      calibration_mae_2signal_pp: 9.8
      calibration_mae_4signal_pp: 6.8
      mae_increase_relative_2_vs_4: 0.44
      ci_width_95_2signal_pp: 22.0
      ci_coverage_95_2signal: 0.74
      kendall_tau_2signal: 0.52
      gamma_ci_includes_zero_2signal_pct: 0.75
      dcr_mae_on_same_conditions_pp: 8.5
      two_signal_worse_than_dcr: true
    result_rationale: >
      2-signal mode在worst档下是最不viable的配置：
      (1) ConStat和Self-Critique是四个信号中AUC最低的两个（exp-002），
      fusion AUC 0.62远低于identifiability threshold 0.72——
      closed-weight场景下可用的信号恰好是最差的，因为最好的信号（Embedding, Min-K++）
      需要model internals access（embeddings, logits）；
      (2) MAE增加44%（6.8→9.8pp）——接近uncalibrated raw score的MAE（8.5pp），
      说明calibration几乎没有净价值；
      (3) Kendall τ降至0.52——刚刚高于random（0.50），calibrated rankings
      与true rankings的agreement barely better than coin flip；
      (4) 75%的conditions下γ CI包含零——在closed-weight scenario下
      contamination detection几乎完全不可行；
      (5) DCR在same conditions下MAE 8.5pp，优于2-signal ContamCal的9.8pp——
      simpler method再次胜出，因为DCR不依赖信号aggregation。
    tables:
      - name: "Table: 2-Signal vs 4-Signal vs DCR"
        columns: [metric, 4-signal, 2-signal, DCR, degradation]
        rows:
          - [RRF AUC (100%), 0.68, 0.62, "—", "-8.8%"]
          - [MAE (pp), 6.8, 9.8, 8.5, "+44%"]
          - [CI Width 95% (pp), 9.5, 22.0, "—", "+132%"]
          - [Kendall τ, 0.72, 0.52, 0.68, "-28%"]
          - [Coverage 95%, 0.76, 0.74, "—", "-2.6%"]
    figures_description:
      - "Fig: 4-signal vs 2-signal MAE distributions. 2-signal distribution shifted far right
        with heavy tail. Minimal overlap — degradation is systematic, not occasional."
    analysis: >
      2-signal failure confirms critical practical constraint：closed-weight models
      (GPT-4, Claude等)——恰好是contamination scrutiny最高的——是calibration最不可行的targets。
      identifiability map需要"signal access level"维度：full-access(4-signal)的viable region
      已经很小（AUC>0.72, N>80），closed-weight(2-signal)的viable region几乎不存在
      （需要AUC>0.85 AND N>150，现实中不可能达到）。
      这是reframed论文的一个strong practical insight：
      "The models with the least transparency are also the most opaque to calibration."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c7376ba-91f1-48ef-ac9d-2255e746754c",
  "isSidechain": false,
  "requestId": "req_011CazxXBieY9gffAtDHudzQ",
  "type": "assistant",
  "uuid": "07eb40ce-a1ae-46e2-8c45-f24d24b00e0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGxQ2GPEUqwbCSo7YSsE4o",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 40641,
      "cache_read_input_tokens": 27231,
      "output_tokens": 26724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 40641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 26724,
          "cache_read_input_tokens": 27231,
          "cache_creation_input_tokens": 40641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 40641
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：γ和θ在实际数据上严重混淆；检测信号AUC不足以支撑有意义的校准；per-benchmark γ_k不收敛或与global γ无显著差异 核心假设：['RRF融合AUC在SFT regime仅0.60-0.68，RL regime下降至<0.55（随机附近）', 'γ和θ的posterior高度相关（|co…",
  "leafUuid": "07eb40ce-a1ae-46e2-8c45-f24d24b00e0f",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "ContamCal framework: calibration limits and diagnostic analysis",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：γ和θ在实际数据上严重混淆；检测信号AUC不足以支撑有意义的校准；per-benchmark γ_k不收敛或与global γ无显著差异 核心假设：['RRF融合AUC在SFT regime仅0.60-0.68，RL regime下降至<0.55（随机附近）', 'γ和θ的posterior高度相关（|co…",
  "leafUuid": "07eb40ce-a1ae-46e2-8c45-f24d24b00e0f",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "ContamCal framework: calibration limits and diagnostic analysis",
  "sessionId": "6f7fda0f-0d60-468c-b973-610dbbae8702"
}
```

---
