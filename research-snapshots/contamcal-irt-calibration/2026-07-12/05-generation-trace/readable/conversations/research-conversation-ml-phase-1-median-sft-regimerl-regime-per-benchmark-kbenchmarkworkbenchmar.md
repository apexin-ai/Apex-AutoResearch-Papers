# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：SFT regime假设成立但RL regime信号严重退化；per-benchmark γ_k在大benchmark上work但小benchmar

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/3723e20b-2f8b-41c3-afbf-b5653fd68564.jsonl`
- **Structured JSON:** [`4c2e005de49546dc8798.json`](../../sessions/4c/4c2e005de49546dc8798.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T17:18:49.247Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T17:18:49.247Z",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：SFT regime假设成立但RL regime信号严重退化；per-benchmark γ_k在大benchmark上work但小benchmark不稳定；coverage略低于名义值\n核心假设：['RRF融合AUC ≥ 0.72（SFT regime），但RL regime下降至0.55-0.60（仅Self-Critique勉强可用）', 'per-benchmark γ_k 在MMLU/ARC上收敛，但HumanEval (N=164) γ_k的CI宽到包含零', 'measurement error model改善coverage但仍低于名义值5-10个百分点（95% coverage实际为83-90%）', '信号生存cliff-like模式存在但边界模糊——SFT→RL是渐进而非陡降', '第二模型家族方向一致但MAE差距2-4pp，不完全复现', 'dose-response大体单调但25%→50%区间有plateau或非单调扰动']\n关键指标范围：{'calibration_mae_pp': [2.0, 4.5], 'coverage_95_pct': [83, 90], 'coverage_80_pct': [65, 77], 'ci_width_sft_pp': [3.5, 6.0], 'ci_width_rl_pp': [10.0, 18.0], 'kendall_tau': [0.82, 0.92], 'gamma_rel_bias': [0.08, 0.18], 'signal_auc_sft_rrf': [0.7, 0.8], 'signal_auc_rl_best_single': [0.53, 0.62], 'baselines_significantly_beaten': [4, 5], 'dose_response_monotonic': False, 'multi_family_mae_gap_pp': [1.5, 4.0]}\n叙事方向：Claims需要分regime表述。Claim 1调整为：\"ContamCal在SFT regime下显著校准（MAE 2-4pp）， 在RL regime下提供保守但诚实的宽CI——这是correct behavior而非failure。\" 强调\"calibration quality is proportional to signal quality\"的conditional framing。 Claim 2（信号生存）实际上升为最强贡献——即使degradation不是cliff-like， systematic signal×regime mapping本身是empirically novel且对detection社区有直接实用价值。 Claim 3重新措辞：identifiability bounds从\"guarantee\"变为\"diagnostic tool\"—— 告诉用户何时可信任校准结果，何时应怀疑。 HumanEval可能降级为appendix或标注\"insufficient items for stable γ estimation\"。 需要补充实验：(a) ablation showing measurement error model的边际贡献， (b) sensitivity analysis showing coverage gap与local independence violation的关系。 仍然beat DCR和majority baselines，paper viable for AAAI但需要更honest的limitations section。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contamcal-irt-calibration\nvenue: AAAI 2027\nfocus: Key changes since Dream D1: (1) per-benchmark γ_k model variant replacing global γ, (2) measurement error model for exposure as default, (3) signal survival analysis elevated to Core Contribution, (4) Fisher Information identifiability analysis, (5) multi-family validation (Llama/Pythia), (6) DCR baseline added, (7) 30+ citations target, (8) local independence explicitly discussed, (9) RL regret uses held-out clean benchmark as ground truth. Focus review on whether these changes address the 5/10 score issues from Dream D1.\n\n## paper_framing.md\n\n# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)\n- Secondary: ICLR 2027 (expected deadline: Sep 2026)\n- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)\n\n## Core Insight\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\n\n## Core Claims (3 条)\n\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B), 2+ model families, and 4 benchmarks.\n\n2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.\n\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.\n\n## Contributions (Hierarchical)\n\n### Core\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\n2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)\n3. Dual-track validation: controlled SFT injection across multiple model families (internal validity) + ecological RL case study (external validity)\n\n### Supporting\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing**: ContamCal is a \"statistical safety net\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).\n- **Headline result template**: \"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\"\n\n## Venue Fit Risks\n- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.\n- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing (\"wide CIs are the correct answer, not a limitation\").\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k model variant as ablation; report both global and per-benchmark results | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Multi-family validation: Qwen2.5 + at least one additional family (Llama/Pythia) | exp-014 |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n\n## Evaluation Protocol (5 Metrics)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n\n## Benchmarks (4)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\n3. **ARC-Challenge** — science reasoning multiple-choice\n4. **HumanEval** — code generation with execution evaluation (N=164, noted as potential limitation for 4PL estimation)\n- Day-8 contingency: reduce to MMLU + GSM8K\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Citation Requirements (30+ minimum)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: controlled_sft_injection\n  claim:\n  - 1\n  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels\n    (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces\n    ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages),\n    parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std).\n    Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent)\n    with controlled semantic similarity — following methodology of \"Rethinking Benchmark\n    and Contamination\" (arXiv 2023). Target: high semantic similarity (cosine >0.85)\n    but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving\n    contamination effect. Quality validation: automated similarity metrics + human\n    spot-check on 50 random pairs per benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  models:\n  - Qwen2.5-0.5B\n  - Qwen2.5-1.5B\n  - Qwen2.5-3B\n  seeds: 3\n  status: planned\n- id: exp-002\n  name: stage1_signal_pipeline\n  claim:\n  - 2\n  description: 'Compute 4 detection signals on all contaminated + clean models from\n    exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers),\n    (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased\n    items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores\n    for each signal.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  name: rrf_aggregation_ablation\n  claim:\n  - 2\n  description: 'RRF fusion of 4 signals into composite per-item exposure score. Ablations:\n    (a) RRF vs equal-weight rank averaging, (b) single-signal only (×4), (c) calibration-based\n    weighted RRF variant, (d) false positive injection robustness check (inject FP\n    at rates matching Duan et al. 2024). Also test degraded 2-signal mode (ConStat\n    + Self-Critique) for closed-weight.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  status: planned\n- id: exp-004\n  name: simulation_identifiability_sweep\n  claim:\n  - 1\n  - 3\n  description: 'Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5\n    conditions): exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) × model\n    count (20, 50, 100, 200) × prior strength (N(0,0.5), N(0,1), N(0,2)) × exposure\n    type (binary, continuous). 144 conditions, 10 seeds each. Reports: θ-γ recovery\n    RMSE, posterior correlation, coverage (50%/80%/95%), prior sensitivity. Establishes\n    minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as \"cannot distinguish\n    no contamination from moderate contamination.\" N_items=300 fixed (per MVP finding).\n    Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime) — prior\n    × N_models dimensions already in sweep grid. Growing Pains pre-estimation sub-experiment:\n    at N_models=20/50, compare flat prior vs informative prior from pre-estimated\n    item parameters. Also includes Fisher Information matrix analysis: derive approximate\n    analytical relationship between signal AUC, N_models, and γ recoverability. Distinguish\n    structural identifiability (parameters uniquely determined) from practical identifiability\n    (estimation quality sufficient for decisions). Provides theoretical grounding\n    for the empirical AUC ≥ 0.70 threshold.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.\n  status: planned\n- id: exp-005\n  name: noise_propagation_analysis\n  claim:\n  - 3\n  description: 'Two parts: (A) Measurement error model (PRIMARY): extend Stan model\n    to treat exposure as noisy observation: exposure_ij ~ N(τ_ij, σ_e²), where τ is\n    latent true contamination. σ_e estimated from exp-001 ground truth FP/FN rates.\n    This propagates Stage 1 uncertainty into posteriors automatically. Compare coverage\n    (50%/80%/95%) vs point-estimate exposure baseline. (B) Post-hoc noise injection:\n    inject Gaussian noise at 1×/1.5×/2× matched levels, re-fit standard model, measure\n    CI widening for γ and θ. Both parts inform whether measurement error model closes\n    the coverage gap.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  - exp-004\n  note: CPU only\n  status: planned\n- id: exp-006\n  name: irt_calibration_and_baselines\n  claim:\n  - 1\n  - 3\n  description: \"Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003. TWO\\\n    \\ model variants: (a) global γ (single γ across all benchmarks), (b) per-benchmark\\\n    \\ γ_k (separate γ per benchmark). Report both. Per-benchmark γ_k addresses Dream\\\n    \\ reviewer concern about benchmark- heterogeneous contamination effects (3× range\\\n    \\ in inflation). IRT fitted per-benchmark (not jointly) to reduce local independence\\\n    \\ violation scope. Posterior predictive checks on item-level residual correlations\\\n    \\ to assess local independence empirically. Compute calibrated scores via exposure=0\\\n    \\ counterfactual with CIs. Compare against 7 baselines: (0) Raw — no adjustment\\\n    \\ (anchor), (1) remove-and-rescore (drop flagged items), (2) single-signal 2PL+γ\\\n    \\ (best signal only, simpler IRT), (3) vanilla 4PL without γ (standard IRT, no\\\n    \\ contamination modeling), (4) linear exposure regression + bootstrap CI (simplest\\\n    \\ post-hoc), (5) Emperor's mitigation: rephrasing + option shuffling, (6) DCR\\\n    \\ fuzzy inference (EMNLP 2025) — the only existing method\\n    producing adjusted\\\n    \\ accuracy; must include or reviewers will reject.\\nEvaluate all 5 metrics: MAE,\\\n    \\ coverage (50%/80%/95%), sharpness, Kendall τ, dose-response monotonicity. Report\\\n    \\ mean ± std across 3 seeds (matched to exp-001 seeds).\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - exp-003\n  benchmarks:\n  - MMLU\n  - GSM8K\n  - ARC-Challenge\n  - HumanEval\n  seeds: 3\n  status: planned\n- id: exp-007\n  name: scale_bridging_7b\n  claim:\n  - 1\n  description: 'Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates\n    calibration accuracy scales to larger models. Requires multi-GPU node (7B LoRA\n    SFT ~4-8h per run on 1×H100).\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: signal_survival_analysis\n  claim:\n  - 2\n  description: 'Systematic evaluation of detection signal reliability across training\n    regimes. Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,\n    RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat degrade\n    post-RL (per fragility paper arXiv 2510.02386). ELEVATED to Core Contribution\n    2 per Dream review (all 3 tiers identified this as the most genuinely novel finding).\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  status: planned\n- id: exp-014\n  name: multi_family_validation\n  claim:\n  - 1\n  description: 'Controlled SFT injection on at least one non-Qwen model family (Llama-3.2-1B\n    or Pythia-1.4B) at 3 dosage levels (0%, 25%, 100%). Validates that identifiability\n    boundaries and calibration accuracy generalize beyond Qwen2.5. Addresses Dream\n    reviewer concern about single model family limiting generalizability (flagged\n    [M][W]).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: rl_observational_case_study\n  claim:\n  - 2\n  - 3\n  description: 'Apply Self-Critique + available signals to existing RL-trained models:\n    Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B. Fit IRT with\n    appropriately wider CIs. Expected regret quantification: compare uncalibrated\n    vs calibrated vs remove-rescore for top-5 model selection. Framed as observational\n    — directional external validity, not full quantitative validation. Near-zero γ\n    check on known-clean benchmark (specificity test).\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  - exp-008\n  status: planned\n- id: exp-012\n  name: observational_72b\n  claim:\n  - 1\n  description: 'Qwen2.5-72B observational analysis (inference only, no SFT). Extends\n    ecological validity to frontier model scale.\n\n    '\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  status: planned\n- id: exp-013\n  name: closed_weight_2signal_mode\n  claim:\n  - 2\n  description: 'Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)\n    for closed-weight models. Ablation quantifying 2-signal vs 4-signal calibration\n    accuracy gap.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_sim_4pl_gamma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    variant_a_nitems300:\n      gamma_mean: 0.466\n      gamma_rel_bias: 0.068\n      gamma_ci_covers_true: true\n      gamma_ci_excludes_zero: true\n      theta_corr: 0.943\n      theta_rmse: 0.238\n      max_rhat: 1.003\n      divergent_pct: 0\n      fit_time_sec: 1407.5\n      overall: PASS\n- exp_id: mvp_sim_confounding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gamma_mean: 0.5386\n    gamma_rel_bias: 0.0771\n    gamma_ci_covers_true: true\n    gamma_ci_excludes_zero: true\n    theta_corr: 0.9733\n    theta_rmse: 0.2407\n    theta_residual_exp_corr: 0.0582\n    max_rhat: 1.007\n    divergent_pct: 0\n    min_ess: 1371.9\n    fit_time_sec: 832\n    actual_confound_corr: 0.3814\n    overall: PASS\n- exp_id: exp_004_sim_sweep\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-13T17:18:49.259Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T17:18:49.259Z",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-13T17:18:49.321Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：SFT regime假设成立但RL regime信号严重退化；per-benchmark γ_k在大benchmark上work但小benchmark不稳定；coverage略低于名义值
核心假设：['RRF融合AUC ≥ 0.72（SFT regime），但RL regime下降至0.55-0.60（仅Self-Critique勉强可用）', 'per-benchmark γ_k 在MMLU/ARC上收敛，但HumanEval (N=164) γ_k的CI宽到包含零', 'measurement error model改善coverage但仍低于名义值5-10个百分点（95% coverage实际为83-90%）', '信号生存cliff-like模式存在但边界模糊——SFT→RL是渐进而非陡降', '第二模型家族方向一致但MAE差距2-4pp，不完全复现', 'dose-response大体单调但25%→50%区间有plateau或非单调扰动']
关键指标范围：{'calibration_mae_pp': [2.0, 4.5], 'coverage_95_pct': [83, 90], 'coverage_80_pct': [65, 77], 'ci_width_sft_pp': [3.5, 6.0], 'ci_width_rl_pp': [10.0, 18.0], 'kendall_tau': [0.82, 0.92], 'gamma_rel_bias': [0.08, 0.18], 'signal_auc_sft_rrf': [0.7, 0.8], 'signal_auc_rl_best_single': [0.53, 0.62], 'baselines_significantly_beaten': [4, 5], 'dose_response_monotonic': False, 'multi_family_mae_gap_pp': [1.5, 4.0]}
叙事方向：Claims需要分regime表述。Claim 1调整为："ContamCal在SFT regime下显著校准（MAE 2-4pp）， 在RL regime下提供保守但诚实的宽CI——这是correct behavior而非failure。" 强调"calibration quality is proportional to signal quality"的conditional framing。 Claim 2（信号生存）实际上升为最强贡献——即使degradation不是cliff-like， systematic signal×regime mapping本身是empirically novel且对detection社区有直接实用价值。 Claim 3重新措辞：identifiability bounds从"guarantee"变为"diagnostic tool"—— 告诉用户何时可信任校准结果，何时应怀疑。 HumanEval可能降级为appendix或标注"insufficient items for stable γ estimation"。 需要补充实验：(a) ablation showing measurement error model的边际贡献， (b) sensitivity analysis showing coverage gap与local independence violation的关系。 仍然beat DCR和majority baselines，paper viable for AAAI但需要更honest的limitations section。


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
  "promptId": "04f715cb-64a7-45fc-9f1f-fd1dc2bb2ebf",
  "type": "user",
  "uuid": "0daaad58-455d-4f88-9e8d-c265da335732",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T17:18:49.316Z_

```json
{
  "parentUuid": "0daaad58-455d-4f88-9e8d-c265da335732",
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
  "uuid": "b57b2b9e-841f-49a0-a2d6-1eb511e1a57c",
  "timestamp": "2026-05-13T17:18:49.316Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T17:18:49.319Z_

```json
{
  "parentUuid": "b57b2b9e-841f-49a0-a2d6-1eb511e1a57c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4ac6ccde-4acd-4b7d-8522-57f7701f75ce",
  "timestamp": "2026-05-13T17:18:49.319Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：SFT regime假设成立但RL regime信号严重退化；per-benchmark γ_k在大benchmark上work但小benchmark不稳定；coverage略低于名义值 核心假设：['RRF融合AUC ≥ 0.72（SFT regime），但RL regime下降至0.55-0.60（仅…",
  "leafUuid": "4ac6ccde-4acd-4b7d-8522-57f7701f75ce",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier IRT calibration with regime-conditional signals",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564"
}
```

---

### Assistant

_source line 8 · 2026-05-13T17:19:02.942Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for the "median" tier across all planned experiments in the experiment plan. I need to provide specific numerical predictions with rationales for each experiment, consistent with the median tier definition provided.

Let me carefully go through each planned experiment and generate median-tier predictions.

Key median tier characteristics:
- SFT regime works but RL regime signals seriously degrade
- Per-benchmark γ_k works on large benchmarks but unstable on small ones (HumanEval)
- Coverage slightly below nominal (5-10pp)
- Calibration MAE: 2.0-4.5pp


- Coverage ranges from 83-90% at 95% threshold down to 65-77% at 80% threshold, with confidence intervals widening substantially under RL (10-18pp vs 3.5-6pp for SFT)
- Ranking correlation stays strong around 0.82-0.92 Kendall tau, though gamma estimates show 8-18% relative bias
- Signal detection performs reasonably for SFT-based RRF (0.7-0.8 AUC) but drops significantly for RL (0.53-0.62), beating most baselines except a couple of the strongest ones
- The dose-response relationship isn't perfectly linear, and multi-family performance gaps range from 1.5-4.0 percentage points

Now I'm mapping out detailed predictions across the twelve experiments, starting with the controlled SFT injection setup and moving through the signal pipeline, aggregation ablations, and various validation approaches.

Generating YAML predictions...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ac6ccde-4acd-4b7d-8522-57f7701f75ce",
  "isSidechain": false,
  "requestId": "req_011Cazx3bGiNF21iLyDSJFBV",
  "type": "assistant",
  "uuid": "6e09cea8-b3fb-48a0-a945-bb1dfbbb7647",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6PdMuuxiK96s37JckBL1A",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12774,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12774,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17021,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12774
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

_source line 9 · 2026-05-13T17:24:07.371Z_

```yaml
tier: median
narrative_guidance: >
  Claims需要分regime表述。ContamCal在SFT regime下显著校准（MAE 2-4pp），在RL regime下提供保守但诚实的宽CI。
  Claim 2（signal survival）实际上升为最强贡献——systematic signal×regime mapping是empirically novel。
  Claim 3 identifiability bounds从"guarantee"变为"diagnostic tool"。HumanEval降级为appendix注释。
  需要补充ablation showing measurement error model边际贡献 + sensitivity analysis showing coverage gap与local independence violation关系。
  仍然beat DCR和majority baselines，paper viable for AAAI但需要honest limitations section。

imagined_experiments:
  - name: controlled_sft_injection
    plan_id: exp-001
    description: >
      Qwen2.5-0.5B/1.5B/3B × 5 dosage levels (0%/5%/25%/50%/100%) SFT injection，
      3 seeds per condition，45 SFT runs total。Paraphrase quality validated via cosine similarity + BLEU。
    expected_results:
      paraphrase_cosine_sim_mean: 0.88
      paraphrase_bleu_mean: 0.22
      human_spotcheck_quality_rate: 0.91
      mmlu_inflation_at_100pct_0.5B_pp: 11.2
      mmlu_inflation_at_100pct_1.5B_pp: 9.4
      mmlu_inflation_at_100pct_3B_pp: 7.8
      gsm8k_inflation_at_100pct_0.5B_pp: 14.6
      gsm8k_inflation_at_100pct_3B_pp: 10.3
      arc_inflation_at_100pct_3B_pp: 8.1
      humaneval_inflation_at_100pct_3B_pp: 6.2
      inflation_at_5pct_mean_pp: 1.8
      inflation_at_25pct_mean_pp: 5.9
      inflation_at_50pct_mean_pp: 8.7
      dose_response_perfectly_monotonic: false
      dose_response_25_to_50_plateau_count: 2
      cross_seed_std_mmlu_pp: 0.6
      cross_seed_std_gsm8k_pp: 1.1
      cross_seed_std_humaneval_pp: 2.3
      sft_runs_completed: 45
      sft_runs_failed: 1
      gpu_hours_actual: 46
    result_rationale: >
      Median档下contamination injection成功产生可测量的inflation，但dose-response不完全单调。
      小模型(0.5B)受contamination影响更大（memorization capacity更受限，overfitting更快），
      大模型(3B)的inflation相对较小因为其pre-training knowledge已覆盖更多benchmark内容。
      25%→50%区间出现plateau是因为SFT的marginal memorization return在这个区间递减——
      模型已经从25%的paraphrases中学到了大部分pattern，额外的25%主要是冗余reinforcement。
      GSM8K和HumanEval的cross-seed variance更大因为item数少、格式更结构化导致memorization效果更variable。
      有1个run失败是realistic的（OOM或NaN loss），在45 runs中是合理的failure rate。
    tables:
      - name: "Table 1: Score Inflation by Dosage and Model Scale"
        rows:
          - model: Qwen2.5-0.5B
            dose_0: "baseline"
            dose_5: "+1.9±0.4"
            dose_25: "+7.1±0.8"
            dose_50: "+9.8±1.0"
            dose_100: "+11.2±0.7"
          - model: Qwen2.5-1.5B
            dose_0: "baseline"
            dose_5: "+1.6±0.5"
            dose_25: "+5.6±0.7"
            dose_50: "+8.2±0.9"
            dose_100: "+9.4±0.6"
          - model: Qwen2.5-3B
            dose_0: "baseline"
            dose_5: "+1.4±0.4"
            dose_25: "+4.9±0.6"
            dose_50: "+7.5±1.1"
            dose_100: "+7.8±0.5"
            note: "MMLU average across 3 seeds; 25→50 plateau visible at 3B"
    figures_description:
      - "Fig: Dose-response curves per benchmark×scale. 4 panels (benchmarks), 3 lines (scales). 显示25%→50% plateau在MMLU-3B和ARC-3B上，GSM8K大体单调但slope变化"
    analysis: >
      Injection pipeline工作正常，产生了可用的ground-truth对。主要发现：(1) inflation magnitude与scale负相关（符合预期），
      (2) dose-response大体单调但25%→50%区间有plateau/非单调扰动（在2/12 benchmark×scale条件中），
      (3) HumanEval的cross-seed variance是MMLU的~4倍，预示后续γ estimation在HumanEval上会不稳定。
      需要在paper中将25%→50% plateau解释为"SFT memorization的marginal return递减"而非pipeline artifact。

  - name: stage1_signal_pipeline
    plan_id: exp-002
    description: >
      4 detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique) 
      computed on all exp-001 models。输出per-model-item exposure scores。
    expected_results:
      embedding_auc_sft_contaminated_mean: 0.81
      minkpp_auc_sft_contaminated_mean: 0.74
      constat_auc_sft_contaminated_mean: 0.69
      selfcritique_auc_sft_contaminated_mean: 0.66
      embedding_auc_clean_models_mean: 0.52
      minkpp_auc_clean_models_mean: 0.51
      constat_auc_clean_models_mean: 0.53
      selfcritique_auc_clean_models_mean: 0.50
      signal_computation_gpu_hours: 18
      per_item_score_coverage_pct: 98.5
      embedding_fp_rate_at_tpr_80: 0.18
      minkpp_fp_rate_at_tpr_80: 0.24
      constat_fp_rate_at_tpr_80: 0.30
      selfcritique_fp_rate_at_tpr_80: 0.33
      signal_corr_embedding_minkpp: 0.58
      signal_corr_embedding_constat: 0.31
      signal_corr_embedding_selfcritique: 0.22
      auc_variance_across_dosage_5pct: 0.04
      auc_variance_across_dosage_100pct: 0.01
    result_rationale: >
      Median档下individual signal AUCs在SFT regime下可用但没有一个是outstanding。
      Embedding retrieval最强(0.81)因为paraphrase保持了高semantic similarity，这是最直接的信号。
      Min-K%++次之(0.74)因为SFT contamination确实改变了token-level surprise pattern，但noise较大。
      ConStat(0.69)和Self-Critique(0.66)在SFT下弱一些——ConStat依赖original vs paraphrase gap，
      但我们的paraphrase quality较高导致gap缩小；Self-Critique是最indirect的信号。
      Clean model上所有signal AUC≈0.50-0.53（near-chance），confirming specificity。
      Signal间correlation中等偏低（0.22-0.58），说明RRF fusion有信息互补空间但也意味着
      每个signal捕获contamination的不同facet。低dosage(5%)时AUC variance大是因为signal-to-noise低，
      high dosage时AUC稳定。1.5%的items缺失coverage来自少数OOM或parsing failure cases。
    tables:
      - name: "Table 2: Per-Signal AUC by Training Regime (SFT contaminated models)"
        rows:
          - signal: Embedding Retrieval
            auc_sft_5pct: "0.61±0.04"
            auc_sft_25pct: "0.77±0.02"
            auc_sft_100pct: "0.86±0.01"
          - signal: "Min-K%++"
            auc_sft_5pct: "0.57±0.05"
            auc_sft_25pct: "0.71±0.03"
            auc_sft_100pct: "0.79±0.02"
          - signal: ConStat
            auc_sft_5pct: "0.55±0.06"
            auc_sft_25pct: "0.66±0.04"
            auc_sft_100pct: "0.74±0.02"
          - signal: Self-Critique
            auc_sft_5pct: "0.54±0.05"
            auc_sft_25pct: "0.63±0.04"
            auc_sft_100pct: "0.71±0.03"
    figures_description:
      - "Fig: Signal AUC vs contamination dosage, 4 curves (one per signal). 显示所有signal monotonically improve with dosage但slope不同"
      - "Fig: Signal correlation heatmap (4×4), 显示moderate decorrelation supporting RRF fusion的value"
    analysis: >
      Individual signals在SFT regime下都work但各有weakness。Embedding最强但需要access to training data embeddings，
      Self-Critique最弱但也是唯一不需要logits的信号。Key insight for downstream: 
      没有单一signal AUC>0.85（averaged across dosages），所以fusion是必要的而非optional。
      Clean model specificity good（AUC≈0.50），为exp-009的near-zero γ check提供了baseline expectation。

  - name: rrf_aggregation_ablation
    plan_id: exp-003
    description: >
      RRF fusion of 4 signals + ablations (equal-weight averaging, single-signal, 
      calibration-weighted RRF, 2-signal closed-weight mode, FP injection robustness)。
    expected_results:
      rrf_4signal_auc_mean: 0.76
      rrf_4signal_auc_at_25pct_dose: 0.74
      rrf_4signal_auc_at_100pct_dose: 0.82
      equal_weight_avg_auc_mean: 0.73
      calibration_weighted_rrf_auc_mean: 0.77
      best_single_signal_auc_mean: 0.74
      worst_single_signal_auc_mean: 0.66
      rrf_2signal_closed_weight_auc_mean: 0.65
      rrf_fp_injection_1x_auc: 0.73
      rrf_fp_injection_2x_auc: 0.68
      rrf_vs_best_single_improvement_pp: 2.0
      calibration_weighted_vs_rrf_improvement_pp: 1.0
    result_rationale: >
      Median档下RRF fusion AUC=0.76，落在[0.7, 0.8]范围内。RRF比best single signal(embedding, 0.74)
      提升仅2pp——improvement存在但不dramatic，因为signals间correlation虽然不高(0.22-0.58)但也不够低
      到让fusion产生大幅增益。Calibration-weighted RRF(0.77)略优于vanilla RRF但差距很小(1pp)，
      这是meta-circularity argument的empirical support——learned weights不值得引入的复杂性和circularity风险。
      Equal-weight averaging(0.73)几乎和RRF持平说明rank-based vs score-based的差异在此setting不大。
      2-signal closed-weight mode(0.65)显著下降——缺少embedding和Min-K%++这两个strongest signals
      让AUC落到仅marginal above useful threshold。FP injection at 2x rate将AUC降至0.68，
      说明RRF对noise有一定robustness但不是immune。这些结果support "RRF as principled design choice"
      的framing——不是contribution，而是在simplicity/performance/circularity三角中的合理选择。
    tables:
      - name: "Table 3: Aggregation Method Comparison"
        rows:
          - method: "RRF (4 signals)"
            auc_mean: 0.76
            auc_std: 0.03
            note: "primary"
          - method: "Calibration-weighted RRF"
            auc_mean: 0.77
            auc_std: 0.03
            note: "marginal gain, adds circularity"
          - method: "Equal-weight averaging"
            auc_mean: 0.73
            auc_std: 0.04
            note: ""
          - method: "Best single (Embedding)"
            auc_mean: 0.74
            auc_std: 0.03
            note: ""
          - method: "2-signal closed-weight"
            auc_mean: 0.65
            auc_std: 0.05
            note: "ConStat + Self-Critique only"
    figures_description:
      - "Fig: Bar chart of aggregation method AUCs with error bars. 显示RRF与calibration-weighted几乎持平，both优于single signals"
      - "Fig: AUC degradation under FP injection (0x, 0.5x, 1x, 1.5x, 2x). 显示gradual graceful degradation"
    analysis: >
      RRF fusion confirms其作为design choice的合理性。核心发现：(1) fusion > single signal但margin modest(2pp)，
      (2) calibration weighting几乎不优于vanilla RRF——empirically validates anti-meta-circularity argument，
      (3) closed-weight 2-signal mode可用但significantly degraded，需要honest reporting。
      Paper中应将RRF framed as "principled default"而非methodological contribution。
      FP robustness check为exp-005的measurement error model提供了complementary evidence。

  - name: simulation_identifiability_sweep
    plan_id: exp-004
    description: >
      144-condition synthetic sweep: AUC(6) × N_models(4) × prior(3) × exposure_type(2)，
      10 seeds each。Fisher Information analysis。Growing Pains pre-estimation sub-experiment。
    expected_results:
      total_conditions_run: 144
      total_fits: 1440
      convergence_rate_pct: 96.5
      gamma_rmse_at_auc55_n50: 0.34
      gamma_rmse_at_auc65_n50: 0.21
      gamma_rmse_at_auc70_n50: 0.14
      gamma_rmse_at_auc80_n50: 0.08
      gamma_rmse_at_auc90_n50: 0.05
      theta_corr_at_auc70_n50: 0.91
      theta_corr_at_auc55_n50: 0.76
      coverage_95_at_auc70_n50_pct: 86
      coverage_95_at_auc55_n50_pct: 72
      coverage_80_at_auc70_n50_pct: 69
      ci_width_at_auc70_n50_pp: 5.2
      ci_width_at_auc55_n50_pp: 17.3
      posterior_corr_theta_gamma_at_auc70: -0.38
      posterior_corr_theta_gamma_at_auc55: -0.67
      minimum_useful_auc_threshold: 0.65
      n_models_20_coverage_95_at_auc70: 79
      n_models_200_coverage_95_at_auc70: 91
      growing_pains_improvement_n20_coverage_pp: 4.5
      growing_pains_improvement_n50_coverage_pp: 1.8
      fisher_info_structural_identifiable_above_auc: 0.58
      fisher_info_practical_identifiable_above_auc: 0.68
      prior_sensitivity_strong_vs_weak_gamma_rmse_ratio: 0.72
      continuous_vs_binary_exposure_gamma_rmse_ratio: 0.85
      divergent_transition_rate_overall_pct: 1.2
    result_rationale: >
      Median档下identifiability呈现clear但imperfect pattern。AUC=0.70是practical threshold——
      γ RMSE=0.14足以distinguish contaminated from clean，CI width=5.2pp是actionable的。
      AUC<0.65时coverage严重退化(72% at 95% nominal)因为posterior θ-γ correlation升高(-0.67)，
      model难以区分"high ability"和"high contamination"。这是fundamental——low-quality signal
      下contamination effect和ability是confounded的。
      Coverage即使在good conditions(AUC=0.70, N=50)下也only 86%而非95%，gap来自：
      (a) 4PL的c/d参数引入额外uncertainty未完全captured by priors，
      (b) local independence violation的residual effects（synthetic data也有correlation through shared generation process）。
      Fisher Information分析区分structural vs practical identifiability：structurally identifiable above AUC≈0.58
      （参数theoretically unique），但practically identifiable above AUC≈0.68（estimation precision sufficient）。
      这10pp gap就是"theoretically possible but practically unreliable"的zone。
      Growing Pains pre-estimation在N=20时帮助较大(+4.5pp coverage)因为informative item priors
      弥补了few-examinee setting的information deficit，但N≥50时边际收益递减。
      Continuous exposure优于binary(RMSE ratio 0.85)但差距不如预期大，因为在moderate AUC下
      continuous scores的额外precision被noise offset。Prior sensitivity存在(ratio 0.72)
      但不dominant——数据information足以在good AUC下override prior，但weak AUC下prior matters more。
      3.5%的fits未converge主要集中在AUC=0.55 + N=20的extreme corner。
    tables:
      - name: "Table 4: γ Recovery RMSE by AUC × N_models (continuous exposure, medium prior)"
        rows:
          - auc: 0.55
            n20: "0.48±0.12"
            n50: "0.34±0.08"
            n100: "0.27±0.06"
            n200: "0.22±0.04"
          - auc: 0.65
            n20: "0.31±0.09"
            n50: "0.21±0.05"
            n100: "0.15±0.03"
            n200: "0.11±0.02"
          - auc: 0.70
            n20: "0.23±0.07"
            n50: "0.14±0.04"
            n100: "0.10±0.02"
            n200: "0.07±0.01"
          - auc: 0.80
            n20: "0.15±0.05"
            n50: "0.08±0.02"
            n100: "0.06±0.01"
            n200: "0.04±0.01"
          - auc: 0.90
            n20: "0.09±0.03"
            n50: "0.05±0.01"
            n100: "0.03±0.01"
            n200: "0.02±0.01"
      - name: "Table 5: 95% Coverage by AUC × N_models"
        rows:
          - auc: 0.55
            n50: "72%"
            n100: "77%"
            n200: "81%"
          - auc: 0.65
            n50: "80%"
            n100: "84%"
            n200: "88%"
          - auc: 0.70
            n50: "86%"
            n100: "89%"
            n200: "92%"
          - auc: 0.80
            n50: "90%"
            n100: "93%"
            n200: "95%"
    figures_description:
      - "Fig: Heatmap of γ RMSE across AUC × N_models grid. Clear gradient from top-left (bad) to bottom-right (good). AUC=0.65-0.70为transition zone"
      - "Fig: Fisher Information determinant vs AUC. 显示structural identifiability threshold (~0.58) 和practical threshold (~0.68) 的separation"
      - "Fig: θ-γ posterior correlation vs AUC. 从-0.67(AUC=0.55) monotonically improve到-0.15(AUC=0.90)"
    analysis: >
      Identifiability sweep confirms paper Claim 3但需要nuanced framing。AUC≥0.70是"safe zone"，
      0.58-0.68是"structural but not practical" zone，<0.58是fundamentally unidentifiable。
      Coverage gap(95% nominal → 86% actual at AUC=0.70, N=50)是persistent——measurement error model(exp-005)
      需要close this gap。Fisher Information analysis提供了theoretical grounding，
      将empirical threshold elevated from "observed rule-of-thumb" to "information-theoretically justified bound"。
      Paper中Claim 3应reframe为"diagnostic tool"——告诉用户何时可信任校准结果。

  - name: noise_propagation_analysis
    plan_id: exp-005
    description: >
      (A) Measurement error model: exposure_ij ~ N(τ_ij, σ_e²) in Stan。
      (B) Post-hoc noise injection at 1×/1.5×/2× levels。
      Compare coverage against point-estimate exposure baseline。
    expected_results:
      measurement_error_model_converges: true
      convergence_rate_pct: 94
      me_model_coverage_95_sft_pct: 88
      me_model_coverage_80_sft_pct: 72
      me_model_coverage_50_sft_pct: 43
      point_estimate_coverage_95_sft_pct: 81
      point_estimate_coverage_80_sft_pct: 63
      point_estimate_coverage_50_sft_pct: 36
      me_model_coverage_improvement_95_pp: 7
      me_model_coverage_improvement_80_pp: 9
      me_model_ci_width_increase_sft_pp: 1.4
      me_model_ci_width_increase_rl_pp: 4.2
      me_model_mae_change_pp: 0.3
      sigma_e_estimated_sft: 0.18
      sigma_e_estimated_rl: 0.41
      posthoc_noise_1x_coverage_95: 83
      posthoc_noise_1.5x_coverage_95: 79
      posthoc_noise_2x_coverage_95: 74
      me_model_fit_time_ratio_vs_standard: 1.8
      me_model_gamma_posterior_width_increase_pct: 25
      residual_coverage_gap_from_nominal_pp: 7
    result_rationale: >
      Median档下measurement error model改善coverage但不完全close the gap。
      从81%→88%(at 95% nominal)——gap从14pp缩至7pp。剩余7pp gap来源：
      (a) local independence violation（single model的item responses correlated through shared parameters，
      measurement error model不address这个），(b) 4PL参数estimation uncertainty的propagation不完整
      （c/d参数的priors可能too tight）。
      ME model的mechanism是通过σ_e将exposure noise propagate到γ posterior，导致CI自动变宽。
      SFT regime σ_e=0.18(signals较reliable)，RL regime σ_e=0.41(signals noisy)——
      这个差异drives CI width的regime-conditional behavior，是"correct behavior"framing的key evidence。
      MAE几乎不变(+0.3pp)说明ME model主要影响uncertainty而非point estimate——
      point estimate已经reasonable，问题在于CI太narrow。
      Post-hoc noise injection的coverage反而下降(83→74 at 2x)因为injected noise不matching
      model's noise assumption——这validates为什么proper ME model优于ad-hoc noise injection。
      Fit time增加1.8倍因为latent τ的sampling增加了posterior dimension。
    tables:
      - name: "Table 6: Coverage Comparison — Measurement Error Model vs Point Estimate"
        rows:
          - level: "50%"
            point_est: "36%"
            me_model: "43%"
            delta: "+7pp"
          - level: "80%"
            point_est: "63%"
            me_model: "72%"
            delta: "+9pp"
          - level: "95%"
            point_est: "81%"
            me_model: "88%"
            delta: "+7pp"
          - level: "nominal gap at 95%"
            point_est: "14pp"
            me_model: "7pp"
            delta: "halved"
    figures_description:
      - "Fig: Coverage calibration plot (nominal vs actual coverage) for ME model vs point estimate vs post-hoc noise. ME model curve closest to diagonal but still below"
      - "Fig: CI width distribution (violin plots) for SFT vs RL regime under ME model. 显示RL regime CIs appropriately wider"
    analysis: >
      Measurement error model是paper的necessary component而非optional enhancement。7pp coverage improvement
      是substantive的，且mechanism principled(noise propagation vs ad-hoc widening)。
      但残余7pp gap需要honest discussion——attributable to local independence violation。
      这实际strengthens paper: 我们can diagnose为什么coverage不perfect（local independence）
      而非simply report unexplained undercoverage。建议在Limitations section写：
      "residual coverage gap is consistent with local independence violation magnitude
      estimated from posterior predictive checks on item residual correlations"。

  - name: irt_calibration_and_baselines
    plan_id: exp-006
    description: >
      4PL+γ IRT (global γ and per-benchmark γ_k) on controlled models。
      7 baselines comparison。5 evaluation metrics。3 seeds。
    expected_results:
      # Global γ model
      global_gamma_mae_pp: 3.8
      global_gamma_coverage_95_pct: 84
      global_gamma_coverage_80_pct: 67
      global_gamma_ci_width_mean_pp: 5.1
      global_gamma_kendall_tau: 0.85
      global_gamma_value: 0.38
      global_gamma_ci: [0.24, 0.53]
      # Per-benchmark γ_k model
      perbench_gamma_k_mmlu: 0.42
      perbench_gamma_k_gsm8k: 0.51
      perbench_gamma_k_arc: 0.35
      perbench_gamma_k_humaneval: 0.19
      perbench_gamma_k_humaneval_ci: [-0.14, 0.52]
      perbench_gamma_k_humaneval_ci_includes_zero: true
      perbench_mae_pp: 3.1
      perbench_coverage_95_pct: 87
      perbench_coverage_80_pct: 71
      perbench_ci_width_mean_pp: 4.8
      perbench_kendall_tau: 0.88
      perbench_dose_response_monotonic: false
      perbench_dose_response_violation_benchmarks: ["MMLU-3B-25to50", "ARC-3B-25to50"]
      # Baselines
      raw_mae_pp: 8.4
      remove_rescore_mae_pp: 5.6
      single_signal_2pl_mae_pp: 5.2
      vanilla_4pl_mae_pp: 7.1
      linear_regression_mae_pp: 4.5
      emperor_rephrase_mae_pp: 6.8
      emperor_shuffle_mae_pp: 7.2
      dcr_mae_pp: 4.1
      # Statistical comparisons (bootstrap p-values)
      contam_cal_vs_raw_p: 0.001
      contam_cal_vs_remove_rescore_p: 0.008
      contam_cal_vs_dcr_p: 0.042
      contam_cal_vs_linear_regression_p: 0.087
      baselines_significantly_beaten_count: 5
      baselines_not_significantly_beaten: ["linear_regression (p=0.087)", "DCR (p=0.042 marginal)"]
      # Posterior diagnostics
      max_rhat: 1.008
      min_bulk_ess: 820
      divergent_pct: 0.8
      posterior_predictive_residual_corr_mean: 0.12
      posterior_predictive_residual_corr_max: 0.23
      local_independence_concern_flag: true
      # Timing
      fit_time_per_benchmark_minutes: 35
      total_gpu_hours: 7
    result_rationale: >
      Median档核心结果。Per-benchmark γ_k model优于global γ (MAE 3.1 vs 3.8, coverage 87% vs 84%)
      因为benchmarks确实有heterogeneous contamination susceptibility——GSM8K(γ=0.51)比ARC(γ=0.35)更susceptible
      因为math problems的答案更容易被memorized。但HumanEval的γ_k CI包含零[-0.14, 0.52]
      因为N=164 items不足以稳定估计4PL的所有参数+γ（effective sample size太小）。
      
      Beating 5/7 baselines: Raw(trivially)、Remove-rescore(丢弃items损失information)、
      Single-signal 2PL(weaker model + single signal)、Vanilla 4PL(no contamination modeling)、
      Emperor's mitigation(fundamentally不work, per ICML 2025)。
      DCR marginal significance(p=0.042)因为DCR也是post-hoc calibration只是less principled——
      差距存在但不overwhelming。Linear regression surprisingly competitive(MAE=4.5)因为
      contamination effect近似linear at moderate dosages，但它没有proper UQ。
      
      Coverage 87%(95% nominal)——gap 8pp在median range [83,90]内。
      来源：(a) local independence violation(residual correlation mean=0.12, max=0.23)，
      (b) ME model的residual undercoverage(见exp-005)。
      Posterior predictive check的residual correlation 0.12 mean confirms local independence
      violation存在但moderate——不catastrophic但也不negligible。
      
      Dose-response不完全单调: MMLU-3B和ARC-3B在25%→50%有plateau，与exp-001的injection结果一致。
      Kendall τ=0.88说明ranking基本preserved但不perfect——主要error来自closely-ranked models
      whose CI overlap。
    tables:
      - name: "Table 7: Main Results — ContamCal vs Baselines (per-benchmark γ_k model, 3 seeds mean±std)"
        rows:
          - method: "ContamCal (per-bench γ_k + ME)"
            mae_pp: "3.1±0.5"
            coverage_95: "87%±2"
            coverage_80: "71%±3"
            ci_width: "4.8±0.4"
            kendall_tau: "0.88±0.02"
          - method: "ContamCal (global γ + ME)"
            mae_pp: "3.8±0.6"
            coverage_95: "84%±3"
            coverage_80: "67%±3"
            ci_width: "5.1±0.5"
            kendall_tau: "0.85±0.03"
          - method: "DCR (EMNLP 2025)"
            mae_pp: "4.1±0.7"
            coverage_95: "—"
            coverage_80: "—"
            ci_width: "—"
            kendall_tau: "0.83±0.03"
          - method: "Linear regression + bootstrap"
            mae_pp: "4.5±0.8"
            coverage_95: "78%±4"
            coverage_80: "59%±5"
            ci_width: "6.2±0.7"
            kendall_tau: "0.82±0.04"
          - method: "Remove-and-rescore"
            mae_pp: "5.6±1.0"
            coverage_95: "—"
            coverage_80: "—"
            ci_width: "—"
            kendall_tau: "0.79±0.04"
          - method: "Single-signal 2PL+γ"
            mae_pp: "5.2±0.9"
            coverage_95: "74%±4"
            coverage_80: "56%±5"
            ci_width: "4.1±0.5"
            kendall_tau: "0.80±0.04"
          - method: "Vanilla 4PL (γ=0)"
            mae_pp: "7.1±0.5"
            coverage_95: "61%±3"
            coverage_80: "42%±4"
            ci_width: "3.2±0.3"
            kendall_tau: "0.77±0.03"
          - method: "Emperor rephrasing"
            mae_pp: "6.8±1.2"
            coverage_95: "—"
            coverage_80: "—"
            ci_width: "—"
            kendall_tau: "0.78±0.05"
          - method: "Emperor option shuffling"
            mae_pp: "7.2±1.1"
            coverage_95: "—"
            coverage_80: "—"
            ci_width: "—"
            kendall_tau: "0.76±0.05"
          - method: "Raw (no adjustment)"
            mae_pp: "8.4±0.6"
            coverage_95: "—"
            coverage_80: "—"
            ci_width: "—"
            kendall_tau: "0.74±0.03"
      - name: "Table 8: Per-Benchmark γ_k Estimates"
        rows:
          - benchmark: MMLU
            gamma_k: 0.42
            ci_95: "[0.30, 0.55]"
            excludes_zero: true
            n_items: 14042
          - benchmark: GSM8K
            gamma_k: 0.51
            ci_95: "[0.33, 0.68]"
            excludes_zero: true
            n_items: 1319
          - benchmark: ARC-Challenge
            gamma_k: 0.35
            ci_95: "[0.19, 0.52]"
            excludes_zero: true
            n_items: 1172
          - benchmark: HumanEval
            gamma_k: 0.19
            ci_95: "[-0.14, 0.52]"
            excludes_zero: false
            n_items: 164
            note: "CI includes zero — insufficient items for stable estimation"
    figures_description:
      - "Fig: Forest plot of per-benchmark γ_k with 95% CIs. MMLU/GSM8K/ARC CIs exclude zero; HumanEval's CI crosses zero"
      - "Fig: Calibration plot (calibrated score vs ground truth clean score) with identity line. Points cluster near diagonal with ±3-5pp scatter"
      - "Fig: Dose-response plot of γ effect by dosage level. 大体monotonic但25%→50%有plateau for MMLU and ARC"
      - "Fig: Coverage calibration plot (nominal vs empirical) for ContamCal vs linear regression vs single-signal 2PL"
    analysis: >
      这是paper的central result table。Per-benchmark γ_k model是recommended variant——
      it dominates global γ on all metrics。关键narrative points：
      (1) MAE 3.1pp是meaningful improvement over all baselines，但vs DCR(4.1)和linear regression(4.5)
          的margin不是overwhelming——需要argue that UQ(coverage/sharpness)是key differentiator。
      (2) HumanEval需要降级到appendix或加注"insufficient items"——不能claim γ=0.19 with CI crossing zero。
      (3) Coverage 87%是honest但imperfect——framing为"calibration quality proportional to signal quality"
          加上explicit local independence discussion。
      (4) DCR comparison是most important——我们win on MAE(3.1 vs 4.1)且provide UQ which DCR cannot。
      (5) 建议Claim 1 reframe: "ContamCal provides statistically significant calibration improvement
          (MAE 3.1±0.5pp) with honest uncertainty quantification (87% at 95% nominal)
          under the SFT regime, while honestly widening CIs when signal quality degrades."

  - name: scale_bridging_7b
    plan_id: exp-007
    description: >
      Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates calibration at larger scale.
    expected_results:
      mmlu_inflation_at_100pct_7B_pp: 6.1
      gsm8k_inflation_at_100pct_7B_pp: 8.4
      calibrated_mae_pp: 3.4
      coverage_95_pct: 85
      kendall_tau: 0.87
      gamma_k_mmlu_7b: 0.36
      gamma_k_gsm8k_7b: 0.44
      inflation_reduction_vs_0.5B_pct: 45
      calibration_degradation_vs_3B_mae_pp: 0.3
      sft_runs_completed: 15
      gpu_hours_actual: 28
    result_rationale: >
      7B模型的contamination inflation比0.5B-3B更小（6.1pp vs 7.8-11.2pp at 100% dose on MMLU），
      因为larger model的pre-training distribution更robust——contamination signal被dilute在更大的parameter space中。
      γ_k相应smaller(0.36 vs 0.42 for MMLU)因为contamination对score的marginal effect reduced。
      但calibration仍然work(MAE 3.4pp, coverage 85%)——degradation仅0.3pp MAE vs 3B，
      说明method scales to larger models even though the contamination effect itself is smaller。
      Coverage稍低(85% vs 87%)因为7B的item response pattern更complex(更多near-ceiling effects on easy items)
      导致4PL的c/d参数estimation更noisy。
    tables:
      - name: "Table 9: Scale Bridging — Calibration Accuracy by Model Scale"
        rows:
          - scale: "0.5B"
            mae_pp: "2.8±0.4"
            coverage_95: "88%"
            note: "highest contamination effect"
          - scale: "1.5B"
            mae_pp: "3.0±0.5"
            coverage_95: "87%"
            note: ""
          - scale: "3B"
            mae_pp: "3.1±0.5"
            coverage_95: "87%"
            note: ""
          - scale: "7B"
            mae_pp: "3.4±0.6"
            coverage_95: "85%"
            note: "smaller contamination effect but calibration still works"
    figures_description:
      - "Fig: MAE vs model scale. 轻微上升trend但difference not statistically significant across scales"
    analysis: >
      7B results confirm method不collapse at larger scale但也reveal scale-dependent trend——
      larger models的contamination effect smaller，MAE slightly worse因为signal-to-noise ratio降低。
      Paper中frame为"calibration accuracy is roughly scale-invariant within our tested range"
      但note trend并caveat that极large models(>70B)可能需要更strong signals。
      Addresses reviewer concern #4 about "scale limited to 3B"。

  - name: signal_survival_analysis
    plan_id: exp-008
    description: >
      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated, RL-post-trained}。
      Elevated to Core Contribution 2。
    expected_results:
      # AUC heatmap values
      embedding_auc_base: 0.52
      embedding_auc_sft_clean: 0.51
      embedding_auc_sft_contam: 0.81
      embedding_auc_rl: 0.54
      minkpp_auc_base: 0.50
      minkpp_auc_sft_clean: 0.51
      minkpp_auc_sft_contam: 0.74
      minkpp_auc_rl: 0.53
      constat_auc_base: 0.51
      constat_auc_sft_clean: 0.52
      constat_auc_sft_contam: 0.69
      constat_auc_rl: 0.57
      selfcritique_auc_base: 0.50
      selfcritique_auc_sft_clean: 0.50
      selfcritique_auc_sft_contam: 0.66
      selfcritique_auc_rl: 0.59
      # Derived metrics
      max_auc_drop_sft_to_rl: 0.27
      signal_survival_only_selfcritique_above_55: true
      rrf_auc_sft: 0.76
      rrf_auc_rl: 0.56
      rrf_auc_drop_sft_to_rl: 0.20
      cliff_like_pattern: false
      degradation_pattern: "gradual with regime-dependent severity"
      constat_partial_survival_rl: true
    result_rationale: >
      Median档下signal degradation在SFT→RL transition中是significant但pattern更像"steep gradient"
      而非clean cliff。Embedding和Min-K%++几乎完全失效(AUC回到~0.53-0.54)因为：
      (a) RL post-training的policy gradient更新heavily modifies token-level distributions，
      destroying memorization-specific patterns that these signals detect，
      (b) embedding space被RLHF reshape导致semantic retrieval信号消失。
      ConStat部分survive(0.57)因为original vs paraphrase performance gap partially persists
      after RL——RL优化的是reward model score而非specific item knowledge，所以contamination-induced
      performance gap被attenuate但not eliminated。
      Self-Critique是sole truly surviving signal(0.59)因为它measures model's meta-cognitive behavior
      (entropy patterns on known vs unknown items)而非direct memorization traces——
      RL改变了answering strategy但model仍然exhibit different confidence patterns on contaminated items。
      
      Pattern不是clean cliff-like而是gradual with signal-dependent severity。
      这与median tier定义一致："SFT→RL是渐进而非陡降"。但severity是dramatic——
      RRF fusion从0.76降到0.56，barely above useful threshold(0.55 from exp-004)。
      这是paper最强empirical finding：signal survival是regime-conditional的，
      且community需要awareness that detection signals designed for SFT may be worthless post-RL。
    tables:
      - name: "Table 10: Signal × Regime AUC Heatmap (Core Contribution)"
        rows:
          - signal: "Embedding Retrieval"
            base: 0.52
            sft_clean: 0.51
            sft_contam: 0.81
            rl_post: 0.54
            survival: "✗"
          - signal: "Min-K%++"
            base: 0.50
            sft_clean: 0.51
            sft_contam: 0.74
            rl_post: 0.53
            survival: "✗"
          - signal: "ConStat"
            base: 0.51
            sft_clean: 0.52
            sft_contam: 0.69
            rl_post: 0.57
            survival: "~"
          - signal: "Self-Critique"
            base: 0.50
            sft_clean: 0.50
            sft_contam: 0.66
            rl_post: 0.59
            survival: "✓"
          - signal: "RRF (4-signal)"
            base: 0.52
            sft_clean: 0.52
            sft_contam: 0.76
            rl_post: 0.56
            survival: "marginal"
    figures_description:
      - "Fig: Signal × Regime AUC heatmap (4×4 grid with color intensity). Central figure of the paper. 显示dramatic contrast between SFT-contam column and RL column"
      - "Fig: Signal AUC degradation curves from SFT→RL. 4 lines showing different degradation rates. Self-Critique flattest, Embedding steepest"
    analysis: >
      这是paper的strongest and most novel contribution。Key narrative：
      (1) Signal survival是regime-conditional——这是empirically novel finding对detection community有直接价值。
      (2) Self-Critique的survival validates其作为RL-regime的anchor signal。
      (3) RRF fusion在RL下barely useful(0.56)——这motivates为什么RL models需要appropriately wider CIs
          (connects to Claim 1的conditional framing)。
      (4) Degradation不是cliff-like但足够severe——"steep gradient"而非"cliff"。
      Paper Claim 2 reframe: "signals degrade systematically under RL (steep gradient, not cliff),
      with Self-Critique as the sole reliably surviving signal. This signal×regime mapping
      is a practical contribution for the detection community."

  - name: multi_family_validation
    plan_id: exp-014
    description: >
      Llama-3.2-1B (or Pythia-1.4B) controlled SFT injection at 3 dosage levels (0%, 25%, 100%)。
      Cross-family generalizability validation。
    expected_results:
      family_chosen: "Llama-3.2-1B"
      mmlu_inflation_at_100pct_pp: 10.8
      gsm8k_inflation_at_100pct_pp: 13.2
      calibrated_mae_pp: 4.8
      mae_gap_vs_qwen_pp: 2.1
      coverage_95_pct: 82
      coverage_gap_vs_qwen_pp: 5
      kendall_tau: 0.84
      gamma_k_direction_consistent: true
      gamma_k_magnitude_ratio_vs_qwen: 0.78
      signal_auc_rrf_sft: 0.71
      signal_auc_gap_vs_qwen: 0.05
      sft_runs_completed: 9
      gpu_hours_actual: 13
    result_rationale: >
      Median档下第二模型家族"方向一致但MAE差距2-4pp"。Llama-3.2-1B的MAE=4.8pp vs Qwen同scale的~3.0pp，
      gap=1.8pp（落在[1.5, 4.0]范围内）。Gap来源：
      (a) Llama的tokenizer和architecture不同导致detection signals的calibration略偏——
      signals originally tuned/validated on Qwen，transfer imperfect，
      (b) Llama的SFT contamination dynamics不同——可能memorize differently due to different pre-training data distribution，
      导致γ_k的magnitude ratio约0.78（方向对但magnitude smaller）。
      (c) Coverage也worse(82% vs 87%)因为item parameter estimation quality依赖于model-specific calibration。
      
      方向一致是关键：γ_k的ranking across benchmarks相同(GSM8K > MMLU > ARC)，说明contamination susceptibility
      的benchmark-level pattern是model-agnostic的。但quantitative accuracy drops enough that paper需要acknowledge
      "cross-family transfer requires signal recalibration"作为limitation/future work。
    tables:
      - name: "Table 11: Multi-Family Validation — Qwen vs Llama"
        rows:
          - metric: "MAE (pp)"
            qwen_1.5B: "3.0±0.5"
            llama_1B: "4.8±0.8"
            gap: "1.8pp"
          - metric: "Coverage 95%"
            qwen_1.5B: "87%"
            llama_1B: "82%"
            gap: "5pp"
          - metric: "Kendall τ"
            qwen_1.5B: "0.88"
            llama_1B: "0.84"
            gap: "0.04"
          - metric: "RRF AUC"
            qwen_1.5B: "0.76"
            llama_1B: "0.71"
            gap: "0.05"
    figures_description:
      - "Fig: γ_k comparison across families (paired bar chart by benchmark). 方向一致，magnitude Llama consistently smaller"
    analysis: >
      Multi-family results是mixed but sufficient：方向一致validates that ContamCal不是Qwen-specific artifact，
      但quantitative gap(2.1pp MAE)意味着paper不能claim"family-agnostic calibration"。
      建议framing："ContamCal generalizes directionally across model families;
      quantitative accuracy benefits from family-specific signal calibration."
      Addresses reviewer concern #11 but with honest caveat。

  - name: rl_observational_case_study
    plan_id: exp-009
    description: >
      Self-Critique + available signals on RL-trained models (Qwen2.5-Instruct, DeepSeek-R1-Distill)。
      Expected regret quantification。Near-zero γ check。
    expected_results:
      models_evaluated: 8
      selfcritique_auc_rl_models: 0.58
      rrf_auc_rl_models: 0.55
      calibrated_ci_width_mean_pp: 14.2
      calibrated_ci_width_range_pp: [10.5, 18.0]
      near_zero_gamma_clean_benchmark: 0.04
      near_zero_gamma_clean_ci: [-0.08, 0.16]
      near_zero_gamma_clean_ci_includes_zero: true
      expected_regret_uncalibrated_top5_pp: 4.7
      expected_regret_calibrated_top5_pp: 2.1
      expected_regret_remove_rescore_top5_pp: 3.4
      regret_reduction_vs_uncalibrated_pct: 55
      qwen_instruct_suspected_contamination_benchmarks: ["MMLU", "GSM8K"]
      deepseek_r1_suspected_contamination_benchmarks: ["GSM8K"]
      gamma_rl_mean: 0.14
      gamma_rl_ci_width: 0.31
      convergence_issues_pct: 8
    result_rationale: >
      Median档下RL observational case study提供directional external validity但quantitative precision差。
      CI width平均14.2pp（在[10, 18]范围内）——正确反映RL signals的low quality(RRF AUC仅0.55)。
      这些wide CIs是"correct behavior"——model honestly says "I don't know precisely"。
      
      Near-zero γ check on clean benchmark成功：γ=0.04, CI包含zero——specificity confirmed。
      这是important control: 如果known-clean benchmark也显示significant γ，说明model有spurious detection bias。
      
      Expected regret是compelling metric：uncalibrated top-5 selection有4.7pp regret(选错model)，
      ContamCal减到2.1pp(55% reduction)。即使CIs很宽，point estimate的shift已经改善了decision quality。
      Remove-rescore(3.4pp)介于两者之间——better than nothing但worse than ContamCal。
      
      Convergence issues at 8%因为RL models的response patterns更atypical for IRT fitting——
      RL-trained models可能have non-monotonic item response functions对某些items。
      
      Qwen2.5-Instruct在MMLU和GSM8K上显示suspected contamination(与community observations一致)，
      DeepSeek-R1在GSM8K上显示(也与其training data包含math data的已知情况一致)。
      但这些都是observational——不能claim causal contamination，只是"consistent with"。
    tables:
      - name: "Table 12: RL Case Study — Expected Regret Comparison"
        rows:
          - method: "Uncalibrated (raw scores)"
            top5_regret_pp: 4.7
            reduction: "—"
          - method: "Remove-and-rescore"
            top5_regret_pp: 3.4
            reduction: "28%"
          - method: "ContamCal (wide CIs)"
            top5_regret_pp: 2.1
            reduction: "55%"
      - name: "Table 13: RL Model CI Widths"
        rows:
          - model: "Qwen2.5-0.5B-Instruct"
            ci_width_mmlu: "11.2pp"
            ci_width_gsm8k: "15.8pp"
          - model: "Qwen2.5-3B-Instruct"
            ci_width_mmlu: "10.5pp"
            ci_width_gsm8k: "13.4pp"
          - model: "Qwen2.5-7B-Instruct"
            ci_width_mmlu: "12.1pp"
            ci_width_gsm8k: "14.7pp"
          - model: "DeepSeek-R1-Distill-7B"
            ci_width_mmlu: "16.3pp"
            ci_width_gsm8k: "18.0pp"
    figures_description:
      - "Fig: CI width comparison SFT regime vs RL regime (box plots). Dramatic widening in RL regime is the honest answer"
      - "Fig: Regret curves (top-K selection) for 3 methods. ContamCal consistently lowest across K values"
      - "Fig: Near-zero γ check: γ posterior on clean benchmark centered at zero (density plot)"
    analysis: >
      RL case study的value不在quantitative precision而在三点：
      (1) 证明method在RL regime下不crash——仍然produces reasonable(if wide) CIs，
      (2) Regret reduction是compelling practical metric即使在wide-CI regime，
      (3) Near-zero γ on clean benchmark validates specificity。
      Paper中frame为"observational external validity"——不claim quantitative accuracy on RL models。
      "Wide CIs are the correct answer, not a limitation" 是核心framing line。

  - name: observational_72b
    plan_id: exp-012
    description: >
      Qwen2.5-72B inference-only observational analysis. Frontier model scale ecological validity。
    expected_results:
      signals_computed: ["Self-Critique", "ConStat"]
      embedding_signal_available: false
      minkpp_signal_available: false
      selfcritique_auc_estimated: 0.57
      calibrated_ci_width_mmlu_pp: 13.8
      calibrated_ci_width_gsm8k_pp: 16.5
      gamma_mmlu: 0.11
      gamma_mmlu_ci: [-0.05, 0.27]
      gamma_gsm8k: 0.18
      gamma_gsm8k_ci: [0.02, 0.34]
      inference_gpu_hours: 14
      note: "2-signal mode only (no logit access for Min-K%++, no training data for embedding)"
    result_rationale: >
      72B model是inference-only所以only 2 signals available(ConStat + Self-Critique)——
      落入exp-013的degraded 2-signal mode。AUC估计仅0.57，barely above practical identifiability threshold(0.68)，
      导致very wide CIs。γ estimates small and uncertain——可能reflect either(a) genuine low contamination
      或(b) signal太弱无法detect existing contamination。
      
      GSM8K的γ CI excludes zero(0.02-0.34)但just barely——directionally suggests some contamination
      consistent with community suspicion about math benchmarks。MMLU的γ CI includes zero。
      
      Value主要是ecological——"method applies at frontier scale"——而非quantitative conclusions。
      Paper中可能只放1-2 sentences或appendix，not a main result。
    tables:
      - name: "Table 14: 72B Observational (Appendix)"
        rows:
          - benchmark: MMLU
            gamma: "0.11 [-0.05, 0.27]"
            ci_width: "13.8pp"
            conclusion: "inconclusive"
          - benchmark: GSM8K
            gamma: "0.18 [0.02, 0.34]"
            ci_width: "16.5pp"
            conclusion: "weakly suggestive"
    figures_description:
      - "Fig (appendix): γ posteriors for 72B model on MMLU and GSM8K. Wide distributions showing honest uncertainty"
    analysis: >
      72B results主要serve as ecological validity extension。量化conclusions有限因为2-signal mode
      不提供sufficient AUC for precise estimation。但existence of results at this scale
      addresses reviewer concern about method not scaling to frontier models。
      建议放appendix而非main paper body。

  - name: closed_weight_2signal_mode
    plan_id: exp-013
    description: >
      2-signal degraded mode (ConStat + Self-Critique) ablation quantifying accuracy gap vs 4-signal。
    expected_results:
      rrf_2signal_auc_sft: 0.65
      rrf_4signal_auc_sft: 0.76
      auc_gap: 0.11
      mae_2signal_pp: 5.3
      mae_4signal_pp: 3.1
      mae_gap_pp: 2.2
      coverage_95_2signal_pct: 78
      coverage_95_4signal_pct: 87
      coverage_gap_pp: 9
      ci_width_2signal_pp: 7.8
      ci_width_4signal_pp: 4.8
      kendall_tau_2signal: 0.79
      kendall_tau_4signal: 0.88
      tau_gap: 0.09
      still_beats_raw: true
      still_beats_emperor: true
      still_beats_vanilla_4pl: true
      beaten_baselines_count: 3
    result_rationale: >
      2-signal mode比4-signal显著degraded(MAE 5.3 vs 3.1, AUC 0.65 vs 0.76)因为
      缺少embedding和Min-K%++这两个在SFT regime下最强的signals。ConStat + Self-Critique
      合在一起的AUC(0.65)刚好在exp-004的practical identifiability threshold(0.68)边缘，
      导致γ estimation不稳定。CI width从4.8→7.8pp(+63%)因为posterior需要wider coverage
      来compensate for signal uncertainty。
      
      仍然beat Raw/Emperor/Vanilla 4PL(3个baselines)，但不beat DCR(4.1pp)或linear regression(4.5pp)。
      这是honest result——closed-weight mode是usable fallback但not competitive with full pipeline。
      
      对practical deployment的implication：如果只有API access(no logits/embeddings)，
      ContamCal仍然提供honest(if wide) CIs，但accuracy不优于simpler methods。
      建议paper中framed as "accessibility extension" with honest performance caveat。
    tables:
      - name: "Table 15: 2-Signal vs 4-Signal Mode Comparison"
        rows:
          - metric: "RRF AUC"
            signal_4: 0.76
            signal_2: 0.65
            degradation: "-14.5%"
          - metric: "MAE (pp)"
            signal_4: 3.1
            signal_2: 5.3
            degradation: "+71%"
          - metric: "Coverage 95%"
            signal_4: "87%"
            signal_2: "78%"
            degradation: "-9pp"
          - metric: "CI width (pp)"
            signal_4: 4.8
            signal_2: 7.8
            degradation: "+63%"
          - metric: "Kendall τ"
            signal_4: 0.88
            signal_2: 0.79
            degradation: "-0.09"
    figures_description:
      - "Fig: Side-by-side calibration plots for 4-signal vs 2-signal mode. 2-signal显示more scatter around diagonal"
    analysis: >
      2-signal mode is a significant downgrade但仍然比no adjustment好。Paper中的honest framing：
      "For closed-weight models, ContamCal operates in degraded mode with wider CIs
      and reduced accuracy. Users should prefer full 4-signal mode when model internals are accessible.
      The 2-signal mode is an accessibility extension, not the recommended configuration."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e09cea8-b3fb-48a0-a945-bb1dfbbb7647",
  "isSidechain": false,
  "requestId": "req_011Cazx3bGiNF21iLyDSJFBV",
  "type": "assistant",
  "uuid": "53a86cb7-a02c-4deb-a73e-28b8757c35d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6PdMuuxiK96s37JckBL1A",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12774,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12774,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17021,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12774
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：SFT regime假设成立但RL regime信号严重退化；per-benchmark γ_k在大benchmark上work但小benchmark不稳定；coverage略低于名义值 核心假设：['RRF融合AUC ≥ 0.72（SFT regime），但RL regime下降至0.55-0.60（仅…",
  "leafUuid": "53a86cb7-a02c-4deb-a73e-28b8757c35d8",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier IRT calibration with regime-conditional signals",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：SFT regime假设成立但RL regime信号严重退化；per-benchmark γ_k在大benchmark上work但小benchmark不稳定；coverage略低于名义值 核心假设：['RRF融合AUC ≥ 0.72（SFT regime），但RL regime下降至0.55-0.60（仅…",
  "leafUuid": "53a86cb7-a02c-4deb-a73e-28b8757c35d8",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier IRT calibration with regime-conditional signals",
  "sessionId": "3723e20b-2f8b-41c3-afbf-b5653fd68564"
}
```

---
