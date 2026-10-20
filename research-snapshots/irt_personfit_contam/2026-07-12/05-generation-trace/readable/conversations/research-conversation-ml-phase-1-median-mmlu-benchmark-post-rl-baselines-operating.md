# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：MMLU 上检测跨模型可靠，但小 benchmark 或个别模型家族失败；post-RL 部分降级；baselines 在某些 operating 

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/fdf61e8c-8687-419f-8063-aac4de129f3d.jsonl`
- **Structured JSON:** [`f55fe6acdbd6a78628e9.json`](../../sessions/f5/f55fe6acdbd6a78628e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:09:46.806Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:09:46.806Z",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：MMLU 上检测跨模型可靠，但小 benchmark 或个别模型家族失败；post-RL 部分降级；baselines 在某些 operating points 胜出\n核心假设：['3/4 模型在 MMLU 15% 污染下显著，但 1 个模型家族（如 Mistral）memorization fraction 过低导致信号不足', 'GSM8K（1.3K items）在多数模型上 |d| < 0.8，power 不足——与理论预测一致但限制实用性', 'θ-fixed 在 3/4 模型上恢复单调性，1 个模型出现非标准 θ-shift pattern', 'Post-RL 信号衰减 40-70%——person-fit 未完全失效但 effect size 大幅缩水', 'lz* 在 5% 污染时与 best baseline 持平或略优，10%+ 时 ML baselines 追上']\n关键指标范围：{'cohens_d_15pct_across_models': [1.0, 3.0], 'cohens_d_15pct_min_model': [0.5, 1.5], 'models_significant_at_15pct': [3, 4], 'benchmarks_significant_per_model': [1, 2], 'memorization_fraction_15pct': [0.15, 0.35], 'theta_fixed_dose_response_ratio': [1.5, 3.0], 'post_rl_signal_retention': [0.3, 0.7], 'lz_star_auroc_5pct': [0.58, 0.72], 'lz_star_auroc_10pct': [0.65, 0.8], 'lz_star_minus_best_baseline_auroc_5pct': [-0.05, 0.05], 'seen_unseen_lz_gap_15pct': [1.0, 3.0]}\n叙事方向：需要将 claims 从 \"detection framework\" 调整为 \"detection characterization framework with quantified operating conditions\"。Claim 1 调整为：lz* 在大 benchmark（≥10K items）上提供可靠检测， 并量化检测力随 benchmark size 和 model architecture 的变化——operating conditions 本身是贡献。 Claim 2 不变（power function 已是理论贡献）。Claim 3 增加 ctrl-contam 跨模型异质性分析： 不同模型家族的 memorization fraction 差异反映 SFT generalization 的架构依赖性。 Post-RL 结果如果衰减但非归零，framing 为 \"partially robust, more robust than log-prob methods (which completely fail per Wang et al.)\"。补充实验：可能需要增加一个 model 或 benchmark 以补强。 Headline 调整为 \"IRT-FIT characterizes the detection frontier at the minimal-information operating point, with quantified power under varying contamination, benchmark, and post-training conditions.\"\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_personfit_contam\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct) validate the framework on real models: at 15% contamination, |Cohen's d|=3.85 with clear seen/unseen memorization fingerprint (seen lz*≈0 vs unseen=3.1). θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity degrades at high contamination (50%), but fixing θ to pre-contamination baseline restores monotonic dose-response (ratio=2.93). The memorization fraction (~38% at 15% contamination) quantifies the SFT generalization effect — the gap between theoretical power and actual detection signal.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+34.75, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.\n6. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n7. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×2 seeds, 15%, 50%). Key results: (a) contam_15 |Cohen's d|=3.85 (strong detection signal); (b) free-θ dose-response non-monotonic (contam_50 Δlz*=1.53 < contam_15 Δlz*=3.97) due to θ-shift confound; (c) **θ-fixed analysis restores monotonicity** (Δlz*_fixed: contam_15=+2.96, contam_50=+8.67, ratio=2.93); (d) seen/unseen split: contam_15 seen lz*≈0 vs unseen=3.1 (clear memorization fingerprint); (e) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-two-sided\n  registry_id: exp-two-sided\n  claim: 2\n  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case\n    study）。包括 bootstrap confidence interval 和 FDR 控制。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- id: exp-extended-sim\n  registry_id: exp-extended-sim\n  claim: 2\n  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让\n    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向\n    lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 依赖 exp-two-sided 的双侧框架定义。\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- id: exp-ctrl-contam-pilot\n  claim: 1,2,3\n  description: 快速验证：Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU only。测量\n    Δlz*(clean→contaminated) 是否显著。增加第二个 0% seed 作为 clean-vs-clean noise floor baseline\n    (Reviewer Q2/Q4)。Eval 时区分 seen/unseen items 以实测 memorization fraction (Reviewer\n    Q3/W9)。这是论文 go/no-go 信号。\n  priority: P0-CRITICAL\n  gpu_budget_hours: 12\n  deps: []\n  status: planned\n  notes: 'GPU 恢复后第一优先。4 conditions × ~3 hrs = ~12 GPU-hrs (+2h for second 0% seed)。关键输出:\n    (a) Δlz* 显著性, (b) clean-vs-clean Δlz* ≈ 0 验证, (c) memorization fraction = (Δacc_seen\n    - Δacc_unseen)/Δacc_seen, (d) adjusted power = theory × memorization fraction。D010\n    要求。'\n- id: exp-ctrl-contam\n  claim: 1,2,3\n  description: 完整控制实验：在 4 个模型上用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量\n    Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - exp-ctrl-contam-pilot\n  status: planned\n  notes: '模型: Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3。Benchmark:\n    MMLU + GSM8K + HellaSwag。4 模型 × 6 levels × 3 benchmarks。'\n- id: exp-empirical-null\n  registry_id: exp-empirical-null\n  claim: 1\n  description: Bootstrap empirical null 分析：量化 lz* 在真实 LLM 数据上的 systematic bias（null\n    mean ≠ 0, null std ≠ 1），为 Calibration Gap Analysis 提供定量证据。包含 Q-Q plots、KS tests、bias\n    量化表、unflagged cells 深度分析。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 复用 exp-two-sided v2 的 bootstrap 逻辑，但保存完整中间分布。~2h 开发+运行。\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- id: exp-power-theory\n  registry_id: exp-power-theory\n  claim: 2\n  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A\n    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: DONE\n  notes: 纯理论推导 + 数值验证。CPU only.\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- id: exp-leaderboard-data-recon\n  registry_id: exp-leaderboard-data-recon\n  claim: 3\n  description: Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results\n    是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item\n    data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: 纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- id: exp-leaderboard-audit\n  claim: 3\n  description: Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark\n    污染率随时间趋势。\n  priority: ABANDONED\n  gpu_budget_hours: 20\n  deps:\n  - exp-two-sided\n  - exp-leaderboard-data-recon\n  status: planned\n  notes: 'D011: v1-irt-refit a_r=0.111 + item alignment 54.56% → 13K audit 不可行。数据可用性写入\n    Discussion/Future Work。'\n- id: exp-natural-experiment\n  claim: 3\n  description: v1 leaderboard base→chat model pairs 自然实验：计算 Δlz* = lz*(chat) - lz*(base)\n    作为 SFT 效应代理。\n  priority: P2-optional\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: 'D013: a_r=0.111 导致 lz*≈accuracy-like, 仅 4-5 pairs 无统计检验能力。Reviewer 终审建议降级。'\n- id: exp-v1-irt-refit-expanded\n  claim: 3\n  description: 扩大 v1 IRT 重拟合样本量至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。最终关闭 Path\n    D。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: CPU only. Reviewer 要求 N≥500 才能最终结论 Path D。阈值：a_r>0.4=可行, a_r<0.2=dead。\n- id: exp-4pl-ablation\n  claim: 1\n  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter\n    d 对 false alarm 和 detection power 的影响。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\n- id: exp-baseline-comparison\n  claim: 1\n  description: '与现有方法对比（≥5 baselines）：在控制实验的 ground-truth contaminated models 上，比较\n    IRT-FIT vs baselines 的 AUROC/Type-I error。Baselines: (1) ConStat (re-test), (2)\n    Min-K%++ (token probs), (3) accuracy z-score (已完成, CPU), (4) PPL-based detection\n    (log-prob family 代表, 预期 RL-robust 测试中失败), (5) random baseline。量化 minimal-information\n    的代价（power 损失）。报告 bootstrap CIs（同行 6/8 不报告方差，这是我们的差异化优势）。'\n  priority: P0-end\n  gpu_budget_hours: 30\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: 蒸馏显示同行 baseline 中位数 ~5 个。accuracy z-score 已完成(CPU)。ConStat 需 re-test, Min-K%++\n    需 token probs, PPL 需 log-probs。exp-ctrl-contam 完成后立即执行。\n- id: exp-multiscale-lzm\n  claim: 1,3\n  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化\n    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要实现 lzm 公式。\n- id: exp-post-rl\n  claim: 1\n  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应\n    Wang et al. (2025) 的 MIA 失效问题。\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\n- id: exp-extra-benchmarks\n  claim: 2,3\n  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items\n    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\n- id: exp-domain-analysis\n  claim: 3\n  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5\n    的 MMLU 污染是全面的还是集中在特定 domain。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要 MMLU item-to-domain 映射。\n\n\n## registry (completed experiments)\n\n- exp_id: sim_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    null_check:\n      all_pass: true\n      gsm8k_ks_p: 0.098\n      hellaswag_ks_p: 0.224\n      mmlu_ks_p: 0.594\n    simulation_power_at_15pct:\n      mmlu: 0.979\n      hellaswag: 0.733\n      gsm8k: 0.578\n      arc_c: 0.129\n      humaneval: 0.243\n    global_pass: false\n    inverted_u_all_benchmarks: true\n    pass_count_large_80pct: 1/3 (mmlu only)\n- exp_id: phase_b_personfit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_sd_all_gt_0.5: true\n    mmlu_lz_star_mean: 24.19\n    mmlu_lz_star_sd: 16.47\n    hellaswag_lz_star_mean: 20.09\n    hellaswag_lz_star_sd: 17.59\n    gsm8k_lz_star_mean: 8.22\n    gsm8k_lz_star_sd: 8.97\n    gemini15_mmlu_lz_star: 34.75\n    gemini15_mmlu_accuracy: 1\n    gemini15_mmlu_theta: 0.78\n    gemini15_flagged_benchmarks: 3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\n    cross_benchmark_spearman_significant: 1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\n    n_models: 12\n    n_benchmarks: 5\n- exp_id: exp-two-sided\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- exp_id: exp-extended-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- exp_id: exp-empirical-null\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- exp_id: exp-leaderboard-data-recon\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- exp_id: exp-power-theory\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- exp_id: exp-item-alignment-check\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    match_rate_direct: 0.5456\n    match_rate_reordered_mistral: 0.8846\n    match_rate_reordered_vicuna: 0.7248\n    n_items_checked: 14042\n    n_models_verified: 2\n    alignment_method: content-based via cais/mmlu canonical order\n    items_mapped: 12068\n    mapping_coverage: 0.86\n- exp_id: exp-v1-irt-refit-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 63\n    n_models_failed: 38\n    n_items: 14042\n    n_mapped_items: 12441\n    overall_accuracy: 0.426\n    fitting_time_2pl_sec: 8.9\n    fitting_time_3pl_sec: 12.1\n    3pl_a_pearson_r: 0.111\n    3pl_b_pearson_r: 0.626\n    3pl_b_spearman_r: 0.656\n    2pl_a_pearson_r: -0.084\n    2pl_b_pearson_r: 0.572\n    lz_star_mean: 11.69\n    lz_star_std: 6.68\n    lz_star_flagged_pct: 1.6\n- exp_id: exp-accuracy-zscore-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_flagged_count: 4\n    lz_flagged_count: 57\n    agreement_rate: 0.117\n    gemini15_mmlu_zscore: 1.413\n- exp_id: exp-cross-benchmark-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_all5_flagged: 10\n    n_models_selective_flagged: 2\n    gemini15_cluster_isolation: true\n    dominant_direction_pattern: positive\n    pct_positive_cells: 93.3\n    total_flagged: 57\n    flag_rate: 0.95\n- exp_id: exp-ml-classifier-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    auroc_avg_25pct:\n      lz_star: 0.86\n      lr_resp: 0.899\n      rf_resp: 0.885\n      lr_resp_summ: 0.909\n      rf_resp_summ: 0.913\n    auroc_avg_5pct:\n      lz_star: 0.675\n      best_ml: 0.575\n    auroc_avg_10pct:\n      lz_star: 0.763\n      best_ml: 0.712\n    lz_star_advantage_low_contam: +0.10 AUROC at 5%, +0.05 at 10%\n    ml_advantage_high_contam: +0.05 at 25%, +0.16 at 50%\n    key_finding: lz* outperforms supervised ML at low contamination (5-10%) without\n      any training data; ML only wins at 25%+ where signal is already strong\n- exp_id: exp-fdr-correction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    flagged_uncorrected: 57/60 (95%)\n    flagged_bh_fdr: 57/60 (95%)\n    flagged_bonferroni: not_computed_but_expected_similar\n    correction_scope: global_60_tests\n    unflagged_cells:\n    - Yi-Lightning×arc_c (bh_p=0.098)\n    - 360GPT2-Pro×humaneval (bh_p=0.134)\n    - Yi-Lightning×humaneval (bh_p=0.181)\n    note: Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale\n      FDR (24800+ tests) deferred to leaderboard audit.\n- exp_id: exp-clean-control-delta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    clean_vs_clean_mean_abs:\n      mmlu: 0.01\n      hellaswag: 0.125\n      gsm8k: 0.021\n      arc_c: 0.095\n      humaneval: 0.02\n    clean_vs_clean_all_nonsig: true\n    clean_vs_contam_all_sig: true\n    cohens_d:\n      mmlu: 2.66\n      hellaswag: 1.85\n      gsm8k: 1.85\n      arc_c: 0.45\n      humaneval: 1.07\n    arc_c_note: d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10\n- exp_id: exp-natural-experiment\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 21\n    n_benchmarks: 4\n    n_complete_pairs: 9\n    significant_benchmarks:\n      HellaSwag:\n        mean_deviation: -3.4\n        t_stat: -3.97\n        p_value: 0.001\n        interpretation: SFT systematically decreases person-fit on HellaSwag\n      GSM8K:\n        mean_deviation: 3.92\n        t_stat: 3.35\n        p_value: 0.009\n        interpretation: SFT systematically increases person-fit on GSM8K\n    non_significant_benchmarks:\n      MMLU:\n        p_value: 0.15\n      ARC-Challenge:\n        p_value: 0.38\n    individual_outliers: 0\n    key_finding: HellaSwag and GSM8K show significant systematic SFT effects on lz*,\n      but no individual pair shows benchmark-specific contamination outliers. P2-optional\n      per Director assessment.\n- exp_id: exp-v1-irt-refit-expanded\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 178\n    n_items: 14042\n    3pl_a_pearson_r: 0.127\n    2pl_a_pearson_r: -0.029\n    3pl_b_pearson_r: 0.663\n    reason: 'N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination\n      failure confirms Path D dead.'\n- exp_id: exp-4pl-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hypothesis_confirmed: true\n    far_4pl: ~5% (well-calibrated)\n    far_3pl: 4.7-16.5% (inflated)\n    far_2pl: 50-100% (catastrophic, unusable)\n    mean_power_gain_4pl_vs_3pl:\n      MMLU: +27.3pp\n      HellaSwag: +26.1pp\n      GSM8K: +20.3pp\n      ARC_C: +14.8pp\n      HumanEval: +13.7pp\n    max_power_gain_4pl_vs_3pl:\n      MMLU: +49.0pp\n      HellaSwag: +59.6pp\n      GSM8K: +39.7pp\n      ARC_C: +54.6pp\n      HumanEval: +30.6pp\n    power_at_25pct:\n      4PL:\n        MMLU: 0.776\n        HellaSwag: 0.534\n        GSM8K: 0.73\n        ARC_C: 0.132\n        HumanEval: 0.318\n      3PL:\n        MMLU: 0.329\n        HellaSwag: 0.28\n        GSM8K: 0.334\n        ARC_C: 0.091\n        HumanEval: 0.165\n    d_bucket_analysis: 'd<0.8: +6.8pp to +61.2pp; d>=0.95: negligible'\n    key_finding: 4PL d parameter essential for LLM contamination detection. 46% MMLU\n      items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely\n      miscalibrated (FAR 50-100%).\n- exp_id: exp-domain-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_mmlu_accuracy: 100% (14042/14042)\n    gemini_domain_concentrated: false\n    gemini_subjects_flagged: 50/57 (lz*>1.96)\n    gemini_category_lz:\n      STEM: 21.2\n      Humanities: 17.9\n      Social Sciences: 15.9\n      Other: 15.3\n    doubao_negative_lz: true\n    doubao_category_lz:\n      STEM: -2\n      Humanities: -13\n      Social_Sciences: -14.8\n      Other: 4.4\n    hunyuan_uneven:\n      STEM: 1.8\n      Social_Sciences: 13.9\n    yi_lightning_highest_mmlu_lz: 48.2\n    qwen_plus_second_highest: 44.9\n    mistral_flagged_subjects: 55/57\n- exp_id: exp-ctrl-contam-pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall: partial - H1/H2 confirmed, H3/H4 not as expected under theta-free; theta-fixed\n      restores dose-response\n    H1_clean_delta_lz_approx_zero:\n      confirmed: true\n      clean_delta_lz: 2.07\n      clean_s1_lz: 8.01\n      clean_s2_lz: 5.94\n      baseline_mean: 6.98\n      baseline_std: 1.03\n    H2_contam_15_detection:\n      confirmed: true\n      delta_lz_free: -3.97\n      cohens_d: -3.85\n    H3_dose_response:\n      theta_free:\n        confirmed: false\n        contam_15_delta: -3.97\n        contam_50_delta: -1.53\n        ratio: 0.38\n        note: inverted due to theta-shift\n      theta_fixed:\n        confirmed: true\n        contam_15_delta: 2.96\n        contam_50_delta: 8.67\n        ratio: 2.93\n        note: monotonicity restored\n    H4_memorization_fraction:\n      confirmed: false\n      contam_15: 0.38\n      contam_50: 0.29\n    theta_shift:\n      clean_s1: -0.0987\n      clean_s2: -0.0842\n      contam_15: 0.1971\n      contam_50: 0.3703\n      theta_fixed: -0.0914\n    theta_fixed_analysis:\n      contam_15:\n        lz_free: 3\n        lz_fixed: 9.93\n        delta_free: -3.97\n        delta_fixed: 2.96\n        absorbed: 6.93\n      contam_50:\n        lz_free: 5.45\n        lz_fixed: 15.64\n        delta_free: -1.53\n        delta_fixed: 8.67\n        absorbed: 10.2\n    accuracy:\n      clean_s1: 0.679\n      clean_s2: 0.679\n      contam_15: 0.731\n      contam_50: 0.764\n      contam_15_seen: 0.824\n      contam_15_unseen: 0.715\n      contam_50_seen: 0.805\n      contam_50_unseen: 0.724\n- exp_id: exp-4pl-real-data-degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    correlation_4pl_vs_3pl:\n      pearson_r: 0.225\n      rmse: 68.41\n    most_affected_benchmark: MMLU (mean |Δlz*|=58.3, 46% items d<0.95)\n    most_affected_model: 'DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6'\n    low_ability_models_impact: '|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)'\n    bias_direction: 3PL systematically depresses high-ability models' lz* (d=1 makes\n      P→1, amplifying few-error aberrance)\n    key_finding: Ignoring d parameter makes lz* completely unreliable for high-ability\n      models — d-induced bias far exceeds any contamination signal\n- exp_id: exp-ctrl-contam-pilot-clean-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-clean-s2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-15\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-50\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:09:46.810Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:09:46.810Z",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-20T19:09:46.829Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：MMLU 上检测跨模型可靠，但小 benchmark 或个别模型家族失败；post-RL 部分降级；baselines 在某些 operating points 胜出
核心假设：['3/4 模型在 MMLU 15% 污染下显著，但 1 个模型家族（如 Mistral）memorization fraction 过低导致信号不足', 'GSM8K（1.3K items）在多数模型上 |d| < 0.8，power 不足——与理论预测一致但限制实用性', 'θ-fixed 在 3/4 模型上恢复单调性，1 个模型出现非标准 θ-shift pattern', 'Post-RL 信号衰减 40-70%——person-fit 未完全失效但 effect size 大幅缩水', 'lz* 在 5% 污染时与 best baseline 持平或略优，10%+ 时 ML baselines 追上']
关键指标范围：{'cohens_d_15pct_across_models': [1.0, 3.0], 'cohens_d_15pct_min_model': [0.5, 1.5], 'models_significant_at_15pct': [3, 4], 'benchmarks_significant_per_model': [1, 2], 'memorization_fraction_15pct': [0.15, 0.35], 'theta_fixed_dose_response_ratio': [1.5, 3.0], 'post_rl_signal_retention': [0.3, 0.7], 'lz_star_auroc_5pct': [0.58, 0.72], 'lz_star_auroc_10pct': [0.65, 0.8], 'lz_star_minus_best_baseline_auroc_5pct': [-0.05, 0.05], 'seen_unseen_lz_gap_15pct': [1.0, 3.0]}
叙事方向：需要将 claims 从 "detection framework" 调整为 "detection characterization framework with quantified operating conditions"。Claim 1 调整为：lz* 在大 benchmark（≥10K items）上提供可靠检测， 并量化检测力随 benchmark size 和 model architecture 的变化——operating conditions 本身是贡献。 Claim 2 不变（power function 已是理论贡献）。Claim 3 增加 ctrl-contam 跨模型异质性分析： 不同模型家族的 memorization fraction 差异反映 SFT generalization 的架构依赖性。 Post-RL 结果如果衰减但非归零，framing 为 "partially robust, more robust than log-prob methods (which completely fail per Wang et al.)"。补充实验：可能需要增加一个 model 或 benchmark 以补强。 Headline 调整为 "IRT-FIT characterizes the detection frontier at the minimal-information operating point, with quantified power under varying contamination, benchmark, and post-training conditions."


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_personfit_contam
venue: emnlp-2026

## paper_framing.md

# Paper Framing — irt_personfit_contam

## Target Venue
- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)

## Core Claims (3 条)

**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:
IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct) validate the framework on real models: at 15% contamination, |Cohen's d|=3.85 with clear seen/unseen memorization fingerprint (seen lz*≈0 vs unseen=3.1). θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity degrades at high contamination (50%), but fixing θ to pre-contamination baseline restores monotonic dose-response (ratio=2.93). The memorization fraction (~38% at 15% contamination) quantifies the SFT generalization effect — the gap between theoretical power and actual detection signal.

**Claim 2 (Detection Characterization)**:
Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted ("expected") power. Both upper bound and adjusted power should be reported.

**Claim 3 (Empirical Findings from Real LLM Data)**:
Three empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+34.75, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.

## Story Spine

**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.

**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.

**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.

**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit."

## Venue Fit Risks

- **EMNLP**: NLP evaluation methodology fits well. Risk: "no new NLP model/technique" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).
- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.
- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.

## Anticipated Reviewer Concerns & Planned Responses

| # | Concern | Response Strategy | Supporting Experiment |
|---|---------|------------------|----------------------|
| R1 | "Just applying existing IRT to LLMs" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade "cross-domain" from contribution to background. | — |
| R2 | "No ground truth contamination labels" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |
| R3 | "Power too low for small benchmarks" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |
| R4 | "Only 12 models" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |
| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
| R6 | "Absolute lz* thresholds don't work on real data" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |
| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
| R9 | "No same-level binary-only baselines" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |
| R10 | "Leaderboard audit baseline unreliable" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |
| R11 | "Power function is upper bound" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |

## Key Narrative Elements (from External Review + Distillation)

1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
2. **Definitional pivot (à la ConStat)** — "All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?" This reframes our work as problem reformulation, not just cross-domain transfer.
3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.
4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim "leaderboard audit" or "large-scale detection" in current paper.
5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.
6. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
7. **Terminology guard** — NEVER use "binary information bottleneck" or "information-theoretic lower bound for all binary-only methods." We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: "IRT person-fit as a principled framework at the minimal-information operating point."
8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.
9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.
10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are "honest negative results that become positive contributions": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: "the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative."
11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as "principled detection with quantified operating characteristics + θ-shift boundary condition." Headline: "We don't just detect — we characterize, including the conditions under which detection degrades." Do NOT claim "state-of-the-art detection."
12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.
13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look "normal") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.

## Writing Strategy (from Distillation)

- **Story type**: "跨界迁移型" — unused in 0/8 peer papers. Our unique angle.
- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).
- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.
- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.
- **Numbered findings**: Adopt PSN-IRT's "Key Discoveries" strategy for scannable presentation.
- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.
- **Baseline count**: Peer median ~5. Target ≥5 baselines.

## Evidence Summary

- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.
- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.
- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.
- **Controlled contamination (exp-ctrl-contam-pilot, D015)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×2 seeds, 15%, 50%). Key results: (a) contam_15 |Cohen's d|=3.85 (strong detection signal); (b) free-θ dose-response non-monotonic (contam_50 Δlz*=1.53 < contam_15 Δlz*=3.97) due to θ-shift confound; (c) **θ-fixed analysis restores monotonicity** (Δlz*_fixed: contam_15=+2.96, contam_50=+8.67, ratio=2.93); (d) seen/unseen split: contam_15 seen lz*≈0 vs unseen=3.1 (clear memorization fingerprint); (e) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution.
- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).


## experiment_plan (with registry status)

- id: exp-two-sided
  registry_id: exp-two-sided
  claim: 2
  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case
    study）。包括 bootstrap confidence interval 和 FDR 控制。
  priority: P0
  gpu_budget_hours: 0
  deps: []
  status: DONE
  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。
  conclusion: negative
  metrics:
    flagged_rate: 57/60 (95.0%)
    n_boot: 1000
    fdr_alpha: 0.05
    flagged_positive: 51
    flagged_negative: 6
    unflagged: 3
    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),
      Yi-Lightning/humaneval (p=0.181)
    gemini15_mmlu_lz_star_v2: 31.815
    gemini15_mmlu_theta_bench: 4
    gemini15_mmlu_p_emp: 0
    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.
      LLMs universally violate 4PL assumptions.
- id: exp-extended-sim
  registry_id: exp-extended-sim
  claim: 2
  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让
    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向
    lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-two-sided
  status: DONE
  notes: CPU only. 依赖 exp-two-sided 的双侧框架定义。
  conclusion: success
  metrics:
    n_sims: 2000
    levels: 0/3/5/10/15/25/50/60/75/90/100
    n_excluded_100pct: 0
    inverted_u_all_5: true
    dual_regime_crossover: 75-90%
    mmlu_power_15pct: 0.9845
    hellaswag_power_15pct: 0.7525
    gsm8k_power_15pct: 0.5905
    mmlu_100pct_lz_star: 31.815
    hellaswag_100pct_lz_star: 26.297
    gsm8k_100pct_lz_star: 8.253
    arc_c_100pct_lz_star: 4.339
    humaneval_100pct_lz_star: 3.529
    two_sided_power:
      mmlu_15pct: 0.978
      mmlu_50pct: 0.9525
      mmlu_75pct: 0.936
      mmlu_90pct: 0.9515
      mmlu_100pct: 1
      hellaswag_25pct: 0.9155
      hellaswag_50pct: 0.9475
      hellaswag_90pct: 0.9375
      hellaswag_100pct: 1
      gsm8k_50pct: 0.837
      gsm8k_90pct: 0.794
      gsm8k_100pct: 1
    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power
      >93% at ALL contamination levels. 100% contamination → 100% detection on all
      benchmarks.'
- id: exp-ctrl-contam-pilot
  claim: 1,2,3
  description: 快速验证：Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU only。测量
    Δlz*(clean→contaminated) 是否显著。增加第二个 0% seed 作为 clean-vs-clean noise floor baseline
    (Reviewer Q2/Q4)。Eval 时区分 seen/unseen items 以实测 memorization fraction (Reviewer
    Q3/W9)。这是论文 go/no-go 信号。
  priority: P0-CRITICAL
  gpu_budget_hours: 12
  deps: []
  status: planned
  notes: 'GPU 恢复后第一优先。4 conditions × ~3 hrs = ~12 GPU-hrs (+2h for second 0% seed)。关键输出:
    (a) Δlz* 显著性, (b) clean-vs-clean Δlz* ≈ 0 验证, (c) memorization fraction = (Δacc_seen
    - Δacc_unseen)/Δacc_seen, (d) adjusted power = theory × memorization fraction。D010
    要求。'
- id: exp-ctrl-contam
  claim: 1,2,3
  description: 完整控制实验：在 4 个模型上用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量
    Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。
  priority: P0
  gpu_budget_hours: 80
  deps:
  - exp-ctrl-contam-pilot
  status: planned
  notes: '模型: Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3。Benchmark:
    MMLU + GSM8K + HellaSwag。4 模型 × 6 levels × 3 benchmarks。'
- id: exp-empirical-null
  registry_id: exp-empirical-null
  claim: 1
  description: Bootstrap empirical null 分析：量化 lz* 在真实 LLM 数据上的 systematic bias（null
    mean ≠ 0, null std ≠ 1），为 Calibration Gap Analysis 提供定量证据。包含 Q-Q plots、KS tests、bias
    量化表、unflagged cells 深度分析。
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-two-sided
  status: DONE
  notes: CPU only. 复用 exp-two-sided v2 的 bootstrap 逻辑，但保存完整中间分布。~2h 开发+运行。
  conclusion: negative
  metrics:
    n_boot: 1000
    n_cells: 60
    mean_null_bias: 0.0925
    mean_null_std: 1.0021
    ks_reject_rate: 0.4
    ks_reject_count: 24/60
    bias_by_benchmark:
      arc_c: 0.146
      gsm8k: 0.082
      hellaswag: 0.034
      humaneval: 0.16
      mmlu: 0.041
    std_by_benchmark:
      arc_c: 1.004
      gsm8k: 1.01
      hellaswag: 0.999
      humaneval: 0.994
      mmlu: 1.003
    ks_reject_by_benchmark:
      arc_c: 0.583
      gsm8k: 0.5
      hellaswag: 0.083
      humaneval: 0.75
      mmlu: 0.083
    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap
      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated
      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,
      arc_c) show higher KS rejection rates due to stronger finite-sample deviations
      from normality.
- id: exp-power-theory
  registry_id: exp-power-theory
  claim: 2
  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A
    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-extended-sim
  status: DONE
  notes: 纯理论推导 + 数值验证。CPU only.
  conclusion: success
  metrics:
    R2_two_sided: 0.9572
    RMSE_two_sided: 0.0746
    R2_left_tail: 0.9764
    R2_mean_lz: 0.9948
    sqrt_n_R2_avg: 0.88
    crossover_range_pct: 81-85%
    min_items_15pct_80power: 7958
- id: exp-leaderboard-data-recon
  registry_id: exp-leaderboard-data-recon
  claim: 3
  description: Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results
    是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item
    data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。
  priority: P0
  gpu_budget_hours: 0
  deps: []
  status: DONE
  notes: 纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。
  conclusion: success
  metrics:
    n_models_with_per_item_data: 13000+
    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)
    estimated_gpu_hours_if_needed: 0
    v1_benchmarks: 6
    v2_benchmarks: 6
    data_format: parquet per-item rows with acc/acc_norm binary fields
    source: open-llm-leaderboard-old/details_{model}
    humaneval_gpu_hrs_per_7b_model: 0.08
    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.
      Zero GPU cost for 4/5 benchmarks.
- id: exp-leaderboard-audit
  claim: 3
  description: Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark
    污染率随时间趋势。
  priority: ABANDONED
  gpu_budget_hours: 20
  deps:
  - exp-two-sided
  - exp-leaderboard-data-recon
  status: planned
  notes: 'D011: v1-irt-refit a_r=0.111 + item alignment 54.56% → 13K audit 不可行。数据可用性写入
    Discussion/Future Work。'
- id: exp-natural-experiment
  claim: 3
  description: v1 leaderboard base→chat model pairs 自然实验：计算 Δlz* = lz*(chat) - lz*(base)
    作为 SFT 效应代理。
  priority: P2-optional
  gpu_budget_hours: 0
  deps:
  - exp-v1-irt-refit-pilot
  status: planned
  notes: 'D013: a_r=0.111 导致 lz*≈accuracy-like, 仅 4-5 pairs 无统计检验能力。Reviewer 终审建议降级。'
- id: exp-v1-irt-refit-expanded
  claim: 3
  description: 扩大 v1 IRT 重拟合样本量至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。最终关闭 Path
    D。
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-v1-irt-refit-pilot
  status: planned
  notes: CPU only. Reviewer 要求 N≥500 才能最终结论 Path D。阈值：a_r>0.4=可行, a_r<0.2=dead。
- id: exp-4pl-ablation
  claim: 1
  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter
    d 对 false alarm 和 detection power 的影响。
  priority: P2
  gpu_budget_hours: 0
  deps:
  - exp-extended-sim
  status: planned
  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。
- id: exp-baseline-comparison
  claim: 1
  description: '与现有方法对比（≥5 baselines）：在控制实验的 ground-truth contaminated models 上，比较
    IRT-FIT vs baselines 的 AUROC/Type-I error。Baselines: (1) ConStat (re-test), (2)
    Min-K%++ (token probs), (3) accuracy z-score (已完成, CPU), (4) PPL-based detection
    (log-prob family 代表, 预期 RL-robust 测试中失败), (5) random baseline。量化 minimal-information
    的代价（power 损失）。报告 bootstrap CIs（同行 6/8 不报告方差，这是我们的差异化优势）。'
  priority: P0-end
  gpu_budget_hours: 30
  deps:
  - exp-ctrl-contam
  status: planned
  notes: 蒸馏显示同行 baseline 中位数 ~5 个。accuracy z-score 已完成(CPU)。ConStat 需 re-test, Min-K%++
    需 token probs, PPL 需 log-probs。exp-ctrl-contam 完成后立即执行。
- id: exp-multiscale-lzm
  claim: 1,3
  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化
    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。
  priority: P2
  gpu_budget_hours: 0
  deps:
  - exp-two-sided
  status: planned
  notes: CPU only. 需要实现 lzm 公式。
- id: exp-post-rl
  claim: 1
  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应
    Wang et al. (2025) 的 MIA 失效问题。
  priority: P2
  gpu_budget_hours: 40
  deps:
  - exp-ctrl-contam
  status: planned
  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。
- id: exp-extra-benchmarks
  claim: 2,3
  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items
    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。
  priority: P2
  gpu_budget_hours: 10
  deps:
  - exp-extended-sim
  status: planned
  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。
- id: exp-domain-analysis
  claim: 3
  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5
    的 MMLU 污染是全面的还是集中在特定 domain。
  priority: P2
  gpu_budget_hours: 0
  deps:
  - exp-two-sided
  status: planned
  notes: CPU only. 需要 MMLU item-to-domain 映射。


## registry (completed experiments)

- exp_id: sim_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    null_check:
      all_pass: true
      gsm8k_ks_p: 0.098
      hellaswag_ks_p: 0.224
      mmlu_ks_p: 0.594
    simulation_power_at_15pct:
      mmlu: 0.979
      hellaswag: 0.733
      gsm8k: 0.578
      arc_c: 0.129
      humaneval: 0.243
    global_pass: false
    inverted_u_all_benchmarks: true
    pass_count_large_80pct: 1/3 (mmlu only)
- exp_id: phase_b_personfit
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star_sd_all_gt_0.5: true
    mmlu_lz_star_mean: 24.19
    mmlu_lz_star_sd: 16.47
    hellaswag_lz_star_mean: 20.09
    hellaswag_lz_star_sd: 17.59
    gsm8k_lz_star_mean: 8.22
    gsm8k_lz_star_sd: 8.97
    gemini15_mmlu_lz_star: 34.75
    gemini15_mmlu_accuracy: 1
    gemini15_mmlu_theta: 0.78
    gemini15_flagged_benchmarks: 3/5 (HellaSwag, GSM8K, HumanEval negative lz*)
    cross_benchmark_spearman_significant: 1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)
    n_models: 12
    n_benchmarks: 5
- exp_id: exp-two-sided
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    flagged_rate: 57/60 (95.0%)
    n_boot: 1000
    fdr_alpha: 0.05
    flagged_positive: 51
    flagged_negative: 6
    unflagged: 3
    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),
      Yi-Lightning/humaneval (p=0.181)
    gemini15_mmlu_lz_star_v2: 31.815
    gemini15_mmlu_theta_bench: 4
    gemini15_mmlu_p_emp: 0
    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.
      LLMs universally violate 4PL assumptions.
- exp_id: exp-extended-sim
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_sims: 2000
    levels: 0/3/5/10/15/25/50/60/75/90/100
    n_excluded_100pct: 0
    inverted_u_all_5: true
    dual_regime_crossover: 75-90%
    mmlu_power_15pct: 0.9845
    hellaswag_power_15pct: 0.7525
    gsm8k_power_15pct: 0.5905
    mmlu_100pct_lz_star: 31.815
    hellaswag_100pct_lz_star: 26.297
    gsm8k_100pct_lz_star: 8.253
    arc_c_100pct_lz_star: 4.339
    humaneval_100pct_lz_star: 3.529
    two_sided_power:
      mmlu_15pct: 0.978
      mmlu_50pct: 0.9525
      mmlu_75pct: 0.936
      mmlu_90pct: 0.9515
      mmlu_100pct: 1
      hellaswag_25pct: 0.9155
      hellaswag_50pct: 0.9475
      hellaswag_90pct: 0.9375
      hellaswag_100pct: 1
      gsm8k_50pct: 0.837
      gsm8k_90pct: 0.794
      gsm8k_100pct: 1
    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power
      >93% at ALL contamination levels. 100% contamination → 100% detection on all
      benchmarks.'
- exp_id: exp-empirical-null
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n_boot: 1000
    n_cells: 60
    mean_null_bias: 0.0925
    mean_null_std: 1.0021
    ks_reject_rate: 0.4
    ks_reject_count: 24/60
    bias_by_benchmark:
      arc_c: 0.146
      gsm8k: 0.082
      hellaswag: 0.034
      humaneval: 0.16
      mmlu: 0.041
    std_by_benchmark:
      arc_c: 1.004
      gsm8k: 1.01
      hellaswag: 0.999
      humaneval: 0.994
      mmlu: 1.003
    ks_reject_by_benchmark:
      arc_c: 0.583
      gsm8k: 0.5
      hellaswag: 0.083
      humaneval: 0.75
      mmlu: 0.083
    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap
      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated
      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,
      arc_c) show higher KS rejection rates due to stronger finite-sample deviations
      from normality.
- exp_id: exp-leaderboard-data-recon
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_models_with_per_item_data: 13000+
    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)
    estimated_gpu_hours_if_needed: 0
    v1_benchmarks: 6
    v2_benchmarks: 6
    data_format: parquet per-item rows with acc/acc_norm binary fields
    source: open-llm-leaderboard-old/details_{model}
    humaneval_gpu_hrs_per_7b_model: 0.08
    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.
      Zero GPU cost for 4/5 benchmarks.
- exp_id: exp-power-theory
  name: ''
  status: DONE
  conclusion: success
  metrics:
    R2_two_sided: 0.9572
    RMSE_two_sided: 0.0746
    R2_left_tail: 0.9764
    R2_mean_lz: 0.9948
    sqrt_n_R2_avg: 0.88
    crossover_range_pct: 81-85%
    min_items_15pct_80power: 7958
- exp_id: exp-item-alignment-check
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    match_rate_direct: 0.5456
    match_rate_reordered_mistral: 0.8846
    match_rate_reordered_vicuna: 0.7248
    n_items_checked: 14042
    n_models_verified: 2
    alignment_method: content-based via cais/mmlu canonical order
    items_mapped: 12068
    mapping_coverage: 0.86
- exp_id: exp-v1-irt-refit-pilot
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n_models_downloaded: 63
    n_models_failed: 38
    n_items: 14042
    n_mapped_items: 12441
    overall_accuracy: 0.426
    fitting_time_2pl_sec: 8.9
    fitting_time_3pl_sec: 12.1
    3pl_a_pearson_r: 0.111
    3pl_b_pearson_r: 0.626
    3pl_b_spearman_r: 0.656
    2pl_a_pearson_r: -0.084
    2pl_b_pearson_r: 0.572
    lz_star_mean: 11.69
    lz_star_std: 6.68
    lz_star_flagged_pct: 1.6
- exp_id: exp-accuracy-zscore-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    z_flagged_count: 4
    lz_flagged_count: 57
    agreement_rate: 0.117
    gemini15_mmlu_zscore: 1.413
- exp_id: exp-cross-benchmark-analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_models_all5_flagged: 10
    n_models_selective_flagged: 2
    gemini15_cluster_isolation: true
    dominant_direction_pattern: positive
    pct_positive_cells: 93.3
    total_flagged: 57
    flag_rate: 0.95
- exp_id: exp-ml-classifier-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    auroc_avg_25pct:
      lz_star: 0.86
      lr_resp: 0.899
      rf_resp: 0.885
      lr_resp_summ: 0.909
      rf_resp_summ: 0.913
    auroc_avg_5pct:
      lz_star: 0.675
      best_ml: 0.575
    auroc_avg_10pct:
      lz_star: 0.763
      best_ml: 0.712
    lz_star_advantage_low_contam: +0.10 AUROC at 5%, +0.05 at 10%
    ml_advantage_high_contam: +0.05 at 25%, +0.16 at 50%
    key_finding: lz* outperforms supervised ML at low contamination (5-10%) without
      any training data; ML only wins at 25%+ where signal is already strong
- exp_id: exp-fdr-correction
  name: ''
  status: DONE
  conclusion: success
  metrics:
    flagged_uncorrected: 57/60 (95%)
    flagged_bh_fdr: 57/60 (95%)
    flagged_bonferroni: not_computed_but_expected_similar
    correction_scope: global_60_tests
    unflagged_cells:
    - Yi-Lightning×arc_c (bh_p=0.098)
    - 360GPT2-Pro×humaneval (bh_p=0.134)
    - Yi-Lightning×humaneval (bh_p=0.181)
    note: Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale
      FDR (24800+ tests) deferred to leaderboard audit.
- exp_id: exp-clean-control-delta
  name: ''
  status: DONE
  conclusion: success
  metrics:
    clean_vs_clean_mean_abs:
      mmlu: 0.01
      hellaswag: 0.125
      gsm8k: 0.021
      arc_c: 0.095
      humaneval: 0.02
    clean_vs_clean_all_nonsig: true
    clean_vs_contam_all_sig: true
    cohens_d:
      mmlu: 2.66
      hellaswag: 1.85
      gsm8k: 1.85
      arc_c: 0.45
      humaneval: 1.07
    arc_c_note: d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10
- exp_id: exp-natural-experiment
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_pairs: 21
    n_benchmarks: 4
    n_complete_pairs: 9
    significant_benchmarks:
      HellaSwag:
        mean_deviation: -3.4
        t_stat: -3.97
        p_value: 0.001
        interpretation: SFT systematically decreases person-fit on HellaSwag
      GSM8K:
        mean_deviation: 3.92
        t_stat: 3.35
        p_value: 0.009
        interpretation: SFT systematically increases person-fit on GSM8K
    non_significant_benchmarks:
      MMLU:
        p_value: 0.15
      ARC-Challenge:
        p_value: 0.38
    individual_outliers: 0
    key_finding: HellaSwag and GSM8K show significant systematic SFT effects on lz*,
      but no individual pair shows benchmark-specific contamination outliers. P2-optional
      per Director assessment.
- exp_id: exp-v1-irt-refit-expanded
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n_models_downloaded: 178
    n_items: 14042
    3pl_a_pearson_r: 0.127
    2pl_a_pearson_r: -0.029
    3pl_b_pearson_r: 0.663
    reason: 'N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination
      failure confirms Path D dead.'
- exp_id: exp-4pl-ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    hypothesis_confirmed: true
    far_4pl: ~5% (well-calibrated)
    far_3pl: 4.7-16.5% (inflated)
    far_2pl: 50-100% (catastrophic, unusable)
    mean_power_gain_4pl_vs_3pl:
      MMLU: +27.3pp
      HellaSwag: +26.1pp
      GSM8K: +20.3pp
      ARC_C: +14.8pp
      HumanEval: +13.7pp
    max_power_gain_4pl_vs_3pl:
      MMLU: +49.0pp
      HellaSwag: +59.6pp
      GSM8K: +39.7pp
      ARC_C: +54.6pp
      HumanEval: +30.6pp
    power_at_25pct:
      4PL:
        MMLU: 0.776
        HellaSwag: 0.534
        GSM8K: 0.73
        ARC_C: 0.132
        HumanEval: 0.318
      3PL:
        MMLU: 0.329
        HellaSwag: 0.28
        GSM8K: 0.334
        ARC_C: 0.091
        HumanEval: 0.165
    d_bucket_analysis: 'd<0.8: +6.8pp to +61.2pp; d>=0.95: negligible'
    key_finding: 4PL d parameter essential for LLM contamination detection. 46% MMLU
      items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely
      miscalibrated (FAR 50-100%).
- exp_id: exp-domain-analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gemini_mmlu_accuracy: 100% (14042/14042)
    gemini_domain_concentrated: false
    gemini_subjects_flagged: 50/57 (lz*>1.96)
    gemini_category_lz:
      STEM: 21.2
      Humanities: 17.9
      Social Sciences: 15.9
      Other: 15.3
    doubao_negative_lz: true
    doubao_category_lz:
      STEM: -2
      Humanities: -13
      Social_Sciences: -14.8
      Other: 4.4
    hunyuan_uneven:
      STEM: 1.8
      Social_Sciences: 13.9
    yi_lightning_highest_mmlu_lz: 48.2
    qwen_plus_second_highest: 44.9
    mistral_flagged_subjects: 55/57
- exp_id: exp-ctrl-contam-pilot
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall: partial - H1/H2 confirmed, H3/H4 not as expected under theta-free; theta-fixed
      restores dose-response
    H1_clean_delta_lz_approx_zero:
      confirmed: true
      clean_delta_lz: 2.07
      clean_s1_lz: 8.01
      clean_s2_lz: 5.94
      baseline_mean: 6.98
      baseline_std: 1.03
    H2_contam_15_detection:
      confirmed: true
      delta_lz_free: -3.97
      cohens_d: -3.85
    H3_dose_response:
      theta_free:
        confirmed: false
        contam_15_delta: -3.97
        contam_50_delta: -1.53
        ratio: 0.38
        note: inverted due to theta-shift
      theta_fixed:
        confirmed: true
        contam_15_delta: 2.96
        contam_50_delta: 8.67
        ratio: 2.93
        note: monotonicity restored
    H4_memorization_fraction:
      confirmed: false
      contam_15: 0.38
      contam_50: 0.29
    theta_shift:
      clean_s1: -0.0987
      clean_s2: -0.0842
      contam_15: 0.1971
      contam_50: 0.3703
      theta_fixed: -0.0914
    theta_fixed_analysis:
      contam_15:
        lz_free: 3
        lz_fixed: 9.93
        delta_free: -3.97
        delta_fixed: 2.96
        absorbed: 6.93
      contam_50:
        lz_free: 5.45
        lz_fixed: 15.64
        delta_free: -1.53
        delta_fixed: 8.67
        absorbed: 10.2
    accuracy:
      clean_s1: 0.679
      clean_s2: 0.679
      contam_15: 0.731
      contam_50: 0.764
      contam_15_seen: 0.824
      contam_15_unseen: 0.715
      contam_50_seen: 0.805
      contam_50_unseen: 0.724
- exp_id: exp-4pl-real-data-degradation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    correlation_4pl_vs_3pl:
      pearson_r: 0.225
      rmse: 68.41
    most_affected_benchmark: MMLU (mean |Δlz*|=58.3, 46% items d<0.95)
    most_affected_model: 'DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6'
    low_ability_models_impact: '|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)'
    bias_direction: 3PL systematically depresses high-ability models' lz* (d=1 makes
      P→1, amplifying few-error aberrance)
    key_finding: Ignoring d parameter makes lz* completely unreliable for high-ability
      models — d-induced bias far exceeds any contamination signal
- exp_id: exp-ctrl-contam-pilot-clean-s1
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp-ctrl-contam-pilot-clean-s2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp-ctrl-contam-pilot-contam-15
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp-ctrl-contam-pilot-contam-50
  name: ''
  status: PREPARING
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
  "promptId": "07854708-0982-4781-9948-71f06eae2379",
  "type": "user",
  "uuid": "b5d518c7-d5e7-4060-9194-be0949740bfb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:09:46.827Z_

```json
{
  "parentUuid": "b5d518c7-d5e7-4060-9194-be0949740bfb",
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
  "uuid": "08f294bc-ef45-4804-a1e8-62adb4bccd08",
  "timestamp": "2026-05-20T19:09:46.827Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:09:46.827Z_

```json
{
  "parentUuid": "08f294bc-ef45-4804-a1e8-62adb4bccd08",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "df7b24bd-a083-43eb-9528-d826940b72c0",
  "timestamp": "2026-05-20T19:09:46.827Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：MMLU 上检测跨模型可靠，但小 benchmark 或个别模型家族失败；post-RL 部分降级；baselines 在某些 operating points 胜出 核心假设：['3/4 模型在 MMLU 15% 污染下显著，但 1 个模型家族（如 Mistral）memorization fracti…",
  "leafUuid": "df7b24bd-a083-43eb-9528-d826940b72c0",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit contamination detection characterization",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:09:50.791Z_

I'll review the experiment plan and existing results to generate detailed median-tier predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df7b24bd-a083-43eb-9528-d826940b72c0",
  "isSidechain": false,
  "requestId": "req_011CbEMAkifHWji3GNxVTeXR",
  "type": "assistant",
  "uuid": "da101f84-d0b5-4185-8fad-ec137ed55c45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YAb97qF1zhKR1bpJSZRFvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21070,
      "cache_read_input_tokens": 11841,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21070,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 133,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21070
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

_source line 9 · 2026-05-20T19:09:52.650Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NnwvgbR21KAf62xfwcqX36`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da101f84-d0b5-4185-8fad-ec137ed55c45",
  "isSidechain": false,
  "requestId": "req_011CbEMAkifHWji3GNxVTeXR",
  "type": "assistant",
  "uuid": "0f60f11a-9f54-4e8a-8f3a-b61aa0e19aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YAb97qF1zhKR1bpJSZRFvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21070,
      "cache_read_input_tokens": 11841,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21070,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 133,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21070
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

_source line 10 · 2026-05-20T19:09:52.667Z_

<details><summary>↩ Tool result · `toolu_01NnwvgbR21KAf62xfwcqX36`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
5	- 不要复述用户的问题
6	- 不要给未被要求的建议或补充说明
7	- 推理要彻底，但输出只保留结论和必要信息
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f60f11a-9f54-4e8a-8f3a-b61aa0e19aa7",
  "isSidechain": false,
  "promptId": "07854708-0982-4781-9948-71f06eae2379",
  "type": "user",
  "uuid": "1b51a7a3-2ebc-4d1c-b4af-7eda3c11075d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "0f60f11a-9f54-4e8a-8f3a-b61aa0e19aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T19:12:06.486Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the experiment plan carefully. I need to generate detailed median-tier predictions for each planned (not yet completed) experiment. Let me identify the planned experiments:

1. **exp-ctrl-contam-pilot** - status: planned (but registry shows DONE with metrics... wait, the experiment_plan says "planned" but the registry shows it as DONE with detailed metrics. Let me re-read...)

Actually, looking more carefully:
- exp-ctrl-contam-pilot in experiment_plan says `status: planned` but in registry it shows `status: DONE` with detailed metrics
- The sub-experiments (clean-s1, clean-s2, contam-15, contam-50) show `status: PREPARING`


- I need to focus on the experiments marked as planned in the experiment_plan itself, since that's what the user asked for. There's a discrepancy between the plan and registry, but I'll go with what's listed in the plan document.

Looking at the full list, the experiments with `planned` status are: exp-ctrl-contam, exp-baseline-comparison, exp-multiscale-lzm, exp-post-rl, exp-extra-benchmarks, and a few others that show as DONE in the registry but planned in the document. I should clarify which ones are actually still pending versus already completed.

For the median-tier predictions, I need to focus on exp-ctrl-contam-pilot (though there's a model mismatch between the pilot and planned versions), the full exp-ctrl-contam across multiple models, and exp-baseline-comparison.

Now I'm checking the experiment_plan section more carefully for all entries marked as planned status. I see exp-ctrl-contam-pilot, exp-ctrl-contam, exp-leaderboard-audit, exp-natural-experiment, and exp-v1-irt-refit-expanded all listed as planned, but some of these are already marked DONE in the registry or have been abandoned, so I need to distinguish between what's truly still planned versus what's already completed or deprioritized. I need to distinguish between experiments that are truly planned versus those already completed. Looking at the registry, some experiments marked as planned actually have results already, so I should focus on generating median-tier predictions only for the ones that haven't been executed yet—like the Qwen3.5-9B version of the contamination pilot and the baseline comparison study. The abandoned experiment can be skipped entirely. not done
8. **exp-multiscale-lzm** - planned, not done
9. **exp-post-rl** - planned, not done
10. **exp-extra-benchmarks** - planned, not done
11. **exp-domain-analysis** - DONE in registry

So I need to focus on the experiments that are actually still pending. The Qwen3.5-9B version of the contamination pilot hasn't run yet, and then there's the full multi-model contamination experiment, the baseline comparison against external models, the multiscale statistics work, post-RL robustness testing, and the additional benchmarks on BBH and MATH. The ones marked as done can be skipped, and I'll exclude the abandoned leaderboard audit.

Rather than overthinking the status tracking, I should just pull all the "planned" experiments from my experiment plan and generate median-tier predictions for them. The user already knows which ones are complete. For the median tier, I'm defining it as detection working across most models but failing on smaller benchmarks or specific model families, partial degradation after post-RL training, baselines being competitive at certain operating points, and specific assumptions about which models show significant effects at MMLU 15%, memorization fractions, GSM8K effect sizes, monotonicity restoration, post-RL signal retention rates, and how the lz* metric compares to baselines.

Now I'm laying out the specific metric ranges I expect to see across these experiments—Cohen's d values at the 15% threshold, how many models show significance, which benchmarks matter per model, memorization fractions, dose-response ratios for the theta-fixed approach, signal retention after post-RL, and AUROC ranges for the lz* metric at different percentile thresholds.

For the Qwen3.5-9B contamination pilot on MMLU, I'm using the Qwen2.5-7B results as a reference point (Cohen's d of 3.85) and predicting that the 9B version should show detectable contamination effects but potentially with somewhat lower effect sizes—around 2.0-3.0 for the 15% contamination level, while the clean-versus-clean baseline should sit near zero as expected.

Now looking at the full four-model experiment across MMLU, GSM8K, and HellaSwag, I'm expecting heterogeneous results depending on the benchmark's size and complexity. MMLU should show clear contamination signals in three of the four models at 15% contamination, though Mistral appears to have lower memorization rates. GSM8K will likely be underpowered with only 1.3K items, while HellaSwag with its 10K items should fall somewhere in between. The memorization fractions will vary considerably across models.

Comparing against baselines, lz* performs competitively at lower contamination thresholds—achieving AUROC scores between 0.58-0.72 at 5% contamination, roughly matching the best existing methods. As contamination increases to 10-15%, machine learning baselines start closing the gap, though lz* maintains reasonable performance. Some baseline methods like ConStat and Min-K%++ operate on different information levels, so direct comparison requires careful interpretation.

When aggregating across multiple benchmarks, the improvement is modest, and the universal misfit issue means larger benchmarks may dominate the aggregate signal. Post-RL fine-tuning substantially degrades the memorization signal—lz* retains 30-70% of its original strength, which is better than log-probability methods that fail entirely, but the effect size still drops considerably. I'm also examining additional benchmarks like BBH to see if the patterns hold across different task types.

Now I need to clarify which experiments are genuinely still planned versus already completed. Looking through the registry, some marked as planned have actually been executed with slightly different model configurations, so I should distinguish between what's truly outstanding and what's been superseded. I've already identified which experiments are truly planned versus already completed. Now I'm generating median-tier predictions for all of them, noting what the model would expect for the ones that have already run. I'll structure this as YAML output and work through each experiment systematically, starting with the Qwen3.5-9B pilot on MMLU with its four conditions. floor, slightly lower than 2.5-7B's 2.07 due to larger model stability)
- contam_15_delta_lz_free: -2.8 (weaker than 2.5-7B's -3.97 due to better generalization)
- cohens_d_15: -2.7 (within [1.0, 3.0] median range)
- contam_50_delta_free: -0.9 (theta-shift still present but potentially stronger in larger model)
- theta_fixed restores monotonicity
- memorization_fraction_15: 0.28 (within [0.15, 0.35], lower than 2.5-7B's 0.38)
- seen_unseen_gap: ~2.0 (within [1.0, 3.0])

### 2. exp-ctrl-contam (Full 4 models × 3 benchmarks × 6 levels)

Looking at the core experiment results across the median tier: Qwen3.5-9B, Gemma-4-31B, and Llama-3.1-8B all show strong contamination signals on MMLU, while Mistral-7B-v0.3 produces weak signals due to low memorization fraction and strong generalization from SFT. For GSM8K with only 1.3K items, most models fall below the effect size threshold needed for reliable detection, and the power analysis suggests we'd need around 7,958 items to reach 80% power at the 15% contamination level. HellaSwag with 10K items sits in an intermediate range.

Across models, only three show significant contamination effects at 15% on MMLU, while baseline ML methods remain competitive or superior once contamination exceeds 10%, with Min-K%++ achieving 0.82 AUROC at 15% contamination despite requiring access to token probabilities.

Now looking at the multiscale aggregation approach—it helps when contamination is consistent across benchmarks but can dilute the signal for selective contamination patterns. Post-RL training retains about 30-70% of the detection signal, with GRPO smoothing memorization patterns enough to drop the effect size from around 2.5 to 1.0, making it still detectable but weaker than the original. BBH falls between MMLU and HellaSwag in detection power at 15% contamination, reaching roughly 0.70-0.80. MATH (5K items): power at 15% ≈ 0.60-0.70

### 7. exp-natural-experiment (already DONE, predict median)

Median prediction would be: weak systematic effects, no individual outliers. This aligns with actual results.

### 8. exp-v1-irt-refit-expanded (already DONE, predict median)

Median prediction: a_r still low, discrimination failure confirmed. This aligns with actual results (a_r=0.127).

### 9. exp-4pl-ablation (already DONE, predict median)

Median prediction: 4PL significantly better than 3PL, d parameter essential. This aligns with actual results.

### 10. exp-domain-analysis (already DONE, predict median)

Median prediction: contamination not concentrated in specific domains for Gemini. This aligns with actual results.

Now I need to focus on the planned experiments. The user wants median-tier predictions for each planned experiment in the experiment_plan, so I should generate what the YAML output would look like with detailed data tables and figures for each one. Let me think through what the median tier would produce for each experiment and structure that as YAML output.

Generating YAML output... I'm noticing a discrepancy between what the experiment plan describes and what was actually executed—the pilot was run on Qwen2.5-7B-Instruct but the plan calls for Qwen3.5-9B, so I should predict results for the planned version rather than what was already done. I'll go through each experiment and generate median-tier predictions for the YAML output, then think through what tables and figures would make sense for the paper.

Now I'm cross-checking the experiment list against what I've identified to make sure I'm not missing anything—there are several planned experiments like the contamination studies, natural experiment, IRT refitting, ablations, and domain analysis that I need to account for. I need to generate predictions for all ten planned experiments, using the experiment_plan as the authoritative source even when registry data exists. For the pilot experiment, I'm weighing the fact that Qwen performed well in testing against the more conservative median-tier expectations, accounting for the higher cohen's d values observed.

Now I'm working through the main contamination experiment across four models and three benchmarks. For MMLU's 14K items, I'm assessing each model's expected effect size at the 15% contamination level—Qwen, Gemma, and Llama should all show strong detection with d values between 1.8 and 2.5, while Mistral's memorization fraction falls too low to reliably detect the effect.

GSM8K is underpowered with only 1.3K items, so all models show weak signals well below the detection threshold. HellaSwag at 10K items shows more promise—Qwen and Llama cross the detection threshold, Gemma sits borderline, and Mistral again fails to show sufficient memorization. When I apply the fixed theta approach, most models recover monotonicity except Mistral, which exhibits an unusual pattern.

I'm now moving into the baseline comparison section, examining how the lz* metric performs against five alternative approaches. Post-RL, the detection signal drops significantly to around 1.0 at 15% contamination with only 40% signal retention, and memorization falls from 0.25 to 0.12, though it remains detectable—much better than log-probability methods which fail entirely. For the additional benchmarks, BBH and MATH show detection power of 0.72 and 0.65 respectively at 15%, filling the gap between smaller and larger datasets. The natural experiment analysis reveals weak SFT effects with no individual contamination outliers, though statistical power is limited.

The IRT refit confirms discrimination failure with a_r below 0.2, the 4PL model substantially outperforms 3PL for high-ability models with the d parameter being critical, and domain analysis shows contamination isn't concentrated in specific domains for Gemini though some models display domain-specific patterns. Now I'm structuring the full YAML output with detailed metric values and organizing the key results tables.

Composing the YAML now with comprehensive experiment details including specific metric values, result rationales at the median tier, formatted tables, figure descriptions, and interpretations for all planned experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b51a7a3-2ebc-4d1c-b4af-7eda3c11075d",
  "isSidechain": false,
  "requestId": "req_011CbEMBBb8eWndYfW5pcD8Q",
  "type": "assistant",
  "uuid": "6d127094-8b00-4549-8b28-6ebeb6ba5156",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HpsaTTNVQFugBZMN6e47ya",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 32911,
      "output_tokens": 22525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22525,
          "cache_read_input_tokens": 32911,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 305
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

_source line 12 · 2026-05-20T19:17:02.078Z_

```yaml
tier: median
narrative_guidance: >
  需要将 claims 从 "detection framework" 调整为 "detection characterization framework with quantified operating conditions"。
  Claim 1 调整：lz* 在大 benchmark（≥10K items）上提供可靠检测，并量化检测力随 benchmark size 和 model architecture 的变化——operating conditions 本身是贡献。
  Claim 3 增加 ctrl-contam 跨模型异质性分析：不同模型家族的 memorization fraction 差异反映 SFT generalization 的架构依赖性。
  Post-RL 结果 framing 为 "partially robust, more robust than log-prob methods (which completely fail per Wang et al.)"。
  Headline 调整为 "IRT-FIT characterizes the detection frontier at the minimal-information operating point, with quantified power under varying contamination, benchmark, and post-training conditions."
  核心叙事张力：MMLU 检测可靠但 GSM8K 失败不是弱点，而是 power function 预测的必然结果——operating conditions 的量化本身是贡献。
  Mistral 失败不是方法缺陷，而是 SFT generalization 异质性的实证发现——架构依赖的 memorization fraction 是独立贡献。

imagined_experiments:
  - name: "ctrl-contam-pilot (Qwen3.5-9B)"
    plan_id: "exp-ctrl-contam-pilot"
    description: >
      Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU。
      Go/no-go 信号。与 Qwen2.5-7B-Instruct pilot 对比验证跨模型稳定性。
    expected_results:
      H1_clean_delta_lz_approx_zero:
        clean_s1_lz: 7.2
        clean_s2_lz: 6.5
        delta_lz: 0.7
        baseline_mean: 6.85
        baseline_std: 0.35
        confirmed: true
      H2_contam_15_detection:
        delta_lz_free: -2.82
        cohens_d: -2.45
        p_value: 3.2e-8
        confirmed: true
      H3_dose_response:
        theta_free:
          contam_15_delta: -2.82
          contam_50_delta: -1.05
          ratio: 0.37
          monotonic: false
        theta_fixed:
          contam_15_delta: 2.41
          contam_50_delta: 6.83
          ratio: 2.83
          monotonic: true
      H4_memorization_fraction:
        contam_15: 0.26
        contam_50: 0.21
      theta_shift:
        clean_s1: -0.072
        clean_s2: -0.065
        contam_15: 0.215
        contam_50: 0.408
      accuracy:
        clean_s1: 0.712
        clean_s2: 0.710
        contam_15: 0.758
        contam_15_seen: 0.832
        contam_15_unseen: 0.744
        contam_50: 0.791
        contam_50_seen: 0.826
        contam_50_unseen: 0.753
      seen_unseen_lz_gap_15pct: 2.1
    result_rationale: >
      Qwen3.5-9B 比 2.5-7B 有更大参数量和更新的训练流程，SFT generalization 更强。
      这意味着：(1) memorization fraction 从 0.38 降到 ~0.26——更多 contaminated items 被"真正学会"而非死记硬背，
      lz* 只检测 memorization signature 不检测 generalization，所以 effective signal 更弱；
      (2) |Cohen's d| 从 3.85 降到 ~2.45——仍然统计显著但不再 overwhelming；
      (3) θ-shift 稍强（0.408 vs 0.370 at 50%）因为更大模型更充分利用 contaminated data 提升 θ；
      (4) θ-fixed 仍然恢复单调性（ratio 2.83 在 [1.5, 3.0] 范围内），因为 θ-shift 机制是统计现象不依赖模型架构；
      (5) seen/unseen gap 2.1（在 [1.0, 3.0] 范围内），低于 2.5-7B 的 3.1，同样因为 generalization 更强。
      Clean-vs-clean noise floor 确认，delta ~0.7 远小于 contamination signal。
    tables:
      - name: "Table: Qwen3.5-9B Pilot Results Summary"
        columns: ["Condition", "Accuracy", "θ_MLE", "lz*_free", "lz*_fixed", "Δlz*_free", "Δlz*_fixed", "Cohen's d"]
        rows:
          - ["clean-s1", "0.712", "-0.072", "7.20", "—", "—", "—", "—"]
          - ["clean-s2", "0.710", "-0.065", "6.50", "—", "+0.70", "—", "—"]
          - ["contam-15%", "0.758", "+0.215", "4.03", "9.26", "-2.82", "+2.41", "-2.45"]
          - ["contam-50%", "0.791", "+0.408", "5.80", "13.68", "-1.05", "+6.83", "—"]
    figures_description:
      - "Fig: θ-free vs θ-fixed dose-response curves for Qwen3.5-9B。左 panel 显示 free-θ 下 contam_50 反而弱于 contam_15（non-monotonic），右 panel 显示 fixed-θ 恢复 monotonic dose-response。与 2.5-7B pilot 对比用虚线叠加。"
      - "Fig: Seen vs unseen item accuracy and lz* distributions (violin plot)。Seen items 在 contam_15 下 accuracy 跳升但 lz* ≈ 0（memorization fingerprint），unseen items 保持 high lz*。"
    analysis: >
      Qwen3.5-9B 验证了 detection 的跨模型可迁移性，但 effect size 弱于 2.5-7B（|d|=2.45 vs 3.85）。
      这个衰减与 memorization fraction 的下降一致（0.26 vs 0.38），支持 "lz* 检测 memorization 不检测 generalization" 的理论框架。
      Go 信号确认：|d|=2.45 仍然是 large effect，但暗示不同模型的 detection sensitivity 存在实质性异质性。
      这驱动 exp-ctrl-contam 的必要性——需要量化跨模型变异。

  - name: "ctrl-contam 完整跨模型实验"
    plan_id: "exp-ctrl-contam"
    description: >
      4 模型 (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3) ×
      6 levels (0/5/10/15/25/50%) × 3 benchmarks (MMLU/GSM8K/HellaSwag)。
      建立 ground-truth contamination → Δlz* 全谱映射。
    expected_results:
      mmlu_15pct_cohens_d:
        qwen35_9b: -2.45
        gemma4_31b: -1.82
        llama31_8b: -2.10
        mistral7b_v03: -0.78
        mean: -1.79
        significant_count: 3  # Mistral fails (|d|<1.0)
      mmlu_15pct_memorization_fraction:
        qwen35_9b: 0.26
        gemma4_31b: 0.18
        llama31_8b: 0.30
        mistral7b_v03: 0.12
        mean: 0.215
      gsm8k_15pct_cohens_d:
        qwen35_9b: -0.62
        gemma4_31b: -0.45
        llama31_8b: -0.55
        mistral7b_v03: -0.28
        mean: -0.475
        significant_count: 0  # All |d| < 0.8
      hellaswag_15pct_cohens_d:
        qwen35_9b: -1.52
        gemma4_31b: -1.10
        llama31_8b: -1.35
        mistral7b_v03: -0.55
        mean: -1.13
        significant_count: 3  # Mistral fails
      benchmarks_significant_per_model:
        qwen35_9b: 2  # MMLU + HellaSwag
        gemma4_31b: 2  # MMLU + HellaSwag
        llama31_8b: 2  # MMLU + HellaSwag
        mistral7b_v03: 0  # none significant
      theta_fixed_dose_response:
        qwen35_9b: {ratio: 2.83, monotonic: true}
        gemma4_31b: {ratio: 2.15, monotonic: true}
        llama31_8b: {ratio: 2.52, monotonic: true}
        mistral7b_v03: {ratio: 1.05, monotonic: false, note: "non-standard θ-shift: θ barely moves because memorization fraction too low to meaningfully shift ability estimate"}
      seen_unseen_lz_gap_15pct:
        qwen35_9b: 2.1
        gemma4_31b: 1.4
        llama31_8b: 2.5
        mistral7b_v03: 0.7
      dose_response_5pct_mmlu:
        qwen35_9b: -0.85
        gemma4_31b: -0.60
        llama31_8b: -0.72
        mistral7b_v03: -0.25
      dose_response_10pct_mmlu:
        qwen35_9b: -1.65
        gemma4_31b: -1.20
        llama31_8b: -1.45
        mistral7b_v03: -0.48
      dose_response_25pct_mmlu:
        qwen35_9b: -2.90
        gemma4_31b: -2.05
        llama31_8b: -2.55
        mistral7b_v03: -0.95
      post_rl_signal_retention: null  # separate experiment
    result_rationale: >
      四模型异质性是 median 档的核心特征，源于 SFT generalization 的架构依赖性：

      Qwen3.5-9B（|d|=2.45）：Qwen 系列 SFT 训练策略相对标准，9B 参数量下 memorization fraction ~0.26，
      足够产生可检测的 aberrant pattern。与 pilot 一致。

      Gemma-4-31B（|d|=1.82）：31B 参数量是最大模型，SFT generalization 最强，memorization fraction 仅 0.18。
      更大模型更容易从 contaminated items 中提取可迁移知识而非死记硬背——这是 scaling law 在 memorization 上的体现。
      检测仍然显著但 effect size 是四模型最低的显著模型。

      Llama-3.1-8B（|d|=2.10）：Meta 的 Llama 系列 SFT 相对"忠实"，memorization fraction 0.30 是最高的，
      与 Llama 架构的 attention pattern 倾向于更 literal 的 memorization 一致（文献中有 Llama 更容易 memorize 的报告）。

      Mistral-7B-v0.3（|d|=0.78, 不显著）：Mistral 的 SFT 流程使用了较强的 generalization regularization
      （sliding window attention + 其 SFT recipe），memorization fraction 仅 0.12。
      在 14K items 的 MMLU 上 15% contamination 理论 power 要求 memorization fraction > ~0.15 才能达到 |d|>1.0，
      Mistral 低于这个门槛。这不是方法失败——是 operating condition 的量化边界。

      GSM8K 全军覆没：1.3K items 远低于 power theory 预测的 min_items=7958（at 80% power, 15% contamination）。
      |d| 最高的 Qwen 也只有 0.62，这精确符合 √n 衰减预测：
      d_GSM8K ≈ d_MMLU × √(1300/14042) × (memorization_fraction_adjustment) ≈ 2.45 × 0.30 × 0.85 ≈ 0.63。
      GSM8K 失败是 power function 的验证而非反例。

      HellaSwag（10K items）：中间位置。3/4 模型显著，与 MMLU 一致（Mistral 仍然失败）。
      Effect sizes 比 MMLU 弱 ~30%，部分因为 HellaSwag 的 sentence-completion 格式导致
      memorization signature 不如 MCQ 明显。

      θ-fixed 在 3/4 模型上恢复单调性，但 Mistral 出现 "non-standard" pattern：
      因为 memorization fraction 太低，θ-shift 几乎不发生（contaminated data 被 generalize 而非 memorize，
      不改变 effective ability），所以 θ-fixed 和 θ-free 差异极小，无法通过 fixing θ 来提取信号。
      这是一个独特的 edge case，值得在 paper 中讨论。
    tables:
      - name: "Table: Detection Sensitivity Across Models and Benchmarks (15% Contamination)"
        columns: ["Model", "MMLU |d|", "MMLU sig.", "HellaSwag |d|", "HSwag sig.", "GSM8K |d|", "GSM8K sig.", "Mem. Frac."]
        rows:
          - ["Qwen3.5-9B", "2.45", "✓", "1.52", "✓", "0.62", "✗", "0.26"]
          - ["Gemma-4-31B", "1.82", "✓", "1.10", "✓", "0.45", "✗", "0.18"]
          - ["Llama-3.1-8B", "2.10", "✓", "1.35", "✓", "0.55", "✗", "0.30"]
          - ["Mistral-7B-v0.3", "0.78", "✗", "0.55", "✗", "0.28", "✗", "0.12"]
          - ["**Mean**", "**1.79**", "**3/4**", "**1.13**", "**3/4**", "**0.48**", "**0/4**", "**0.215**"]
      - name: "Table: MMLU Dose-Response (θ-fixed, |Δlz*|)"
        columns: ["Model", "5%", "10%", "15%", "25%", "50%", "Monotonic?", "Ratio(50/15)"]
        rows:
          - ["Qwen3.5-9B", "0.82", "1.58", "2.41", "4.15", "6.83", "✓", "2.83"]
          - ["Gemma-4-31B", "0.55", "1.10", "1.72", "2.80", "3.70", "✓", "2.15"]
          - ["Llama-3.1-8B", "0.68", "1.35", "2.05", "3.55", "5.18", "✓", "2.52"]
          - ["Mistral-7B-v0.3", "0.18", "0.35", "0.52", "0.68", "0.55", "✗", "1.05"]
      - name: "Table: Memorization Fraction by Model and Benchmark (15%)"
        columns: ["Model", "MMLU", "HellaSwag", "GSM8K"]
        rows:
          - ["Qwen3.5-9B", "0.26", "0.22", "0.20"]
          - ["Gemma-4-31B", "0.18", "0.15", "0.13"]
          - ["Llama-3.1-8B", "0.30", "0.25", "0.23"]
          - ["Mistral-7B-v0.3", "0.12", "0.09", "0.08"]
    figures_description:
      - >
        Fig: 4-panel dose-response curves (one per model), x=contamination level, y=|Δlz*| (θ-fixed)。
        Three lines per panel (MMLU/HellaSwag/GSM8K)。Qwen/Llama/Gemma 显示 monotonic 上升，
        Mistral 的线条平坦且在 noise floor 附近。灰色 shaded band = clean-vs-clean noise floor。
        Bootstrap 95% CI error bars。
      - >
        Fig: Memorization fraction heatmap (model × benchmark)。颜色从浅（低 mem. frac.）到深（高 mem. frac.）。
        清晰显示 Llama > Qwen > Gemma > Mistral 的 memorization hierarchy，以及 MMLU > HellaSwag > GSM8K 的 benchmark effect。
      - >
        Fig: Power theory prediction vs actual detection (scatter plot)。
        x=theoretical power (from power function × memorization fraction), y=observed |d|。
        12 points (4 models × 3 benchmarks)。Expected R² ~0.85，但 Mistral points 系统性低于 prediction line——
        表明 Mistral 的 memorization fraction 可能有额外的 architecture-specific suppression。
    analysis: >
      核心发现是跨模型异质性的量化：|d| 范围从 0.78（Mistral/MMLU）到 2.45（Qwen/MMLU），
      memorization fraction 范围从 0.12 到 0.30。这个异质性不是 noise——它与 model architecture 和 SFT recipe 系统性相关。
      
      关键叙事点：(1) 3/4 模型在 MMLU 上可靠检测，但需要承认 1 个模型家族失败——这驱动 "characterization" 而非 "universal detection" 的 framing；
      (2) GSM8K 全面失败精确验证了 power function 的预测能力——theory-experiment agreement 本身是贡献；
      (3) Mistral 的低 memorization fraction 是一个独立发现——暗示某些 SFT 策略可能 inherently resistant to memorization-based detection，
      这对 contamination detection 社区有方法论意义。
      
      Paper 的 operating conditions table 应该明确给出：benchmark ≥10K items + memorization fraction ≥0.15 → |d| ≥ 1.0（reliable detection）。

  - name: "Baseline Comparison (≥5 baselines)"
    plan_id: "exp-baseline-comparison"
    description: >
      在 ctrl-contam ground-truth models 上比较 IRT-FIT vs ≥5 baselines 的 AUROC。
      Baselines: (1) accuracy z-score, (2) PPL-based detection, (3) Min-K%++,
      (4) ConStat, (5) random baseline。报告 bootstrap CIs。
    expected_results:
      auroc_by_method_and_level:
        5pct:
          lz_star: 0.65
          accuracy_zscore: 0.55
          ppl_based: 0.62
          min_k_pp: 0.68
          constat: 0.71
          random: 0.50
        10pct:
          lz_star: 0.73
          accuracy_zscore: 0.60
          ppl_based: 0.70
          min_k_pp: 0.76
          constat: 0.78
          random: 0.50
        15pct:
          lz_star: 0.80
          accuracy_zscore: 0.63
          ppl_based: 0.78
          min_k_pp: 0.84
          constat: 0.85
          random: 0.50
        25pct:
          lz_star: 0.86
          accuracy_zscore: 0.68
          ppl_based: 0.85
          min_k_pp: 0.91
          constat: 0.92
          random: 0.50
      lz_minus_best_baseline_5pct: -0.03  # lz* slightly below Min-K++ at 5%
      lz_minus_best_baseline_10pct: -0.03
      lz_advantage_vs_binary_only_5pct: +0.10  # vs accuracy z-score
      bootstrap_ci_width_lz_15pct: [0.74, 0.86]  # 95% CI
      information_cost_summary: >
        lz* 在 binary-only operating point 是最优。
        需要 token probs 的方法 (Min-K%++, PPL) 在 15%+ 时 AUROC 高 4-8pp，
        但在 post-RL 场景完全失效（见 exp-post-rl）。
        ConStat 需要 re-test 数据（不同 information level）。
    result_rationale: >
      Median 档的核心张力：lz* 在 5% 污染时与 best binary-only baseline 持平或略优（+0.10 vs accuracy z-score），
      但需要 token probs 的方法在 10%+ 时追上。

      lz* AUROC 0.65 at 5%（在 [0.58, 0.72] 范围内）：低污染下 signal 微弱，
      但 IRT structure 提供的 inductive bias 弥补了 labeled data 的缺失。
      Simulation 中 lz* 在 5% 时 AUROC=0.675（exp-ml-classifier-baseline），
      实际数据因为 SFT generalization 和 memorization fraction 的存在会略低。

      Min-K%++ 在 10%+ 时胜出（AUROC 0.76 vs 0.73 at 10%）：
      token-level probability 提供了比 binary response 更丰富的信号——这是 information hierarchy 的必然结果。
      但 median 档的关键 narrative pivot 是：Min-K%++ 在 post-RL 场景完全失效（Wang et al. 2025），
      而 lz* 保持部分检测力（exp-post-rl 预测 retention 40-60%）。
      所以 lz* 的优势不是 absolute AUROC 而是 robustness across post-training pipelines。

      ConStat 需要 re-test（重新出题），严格来说不在同一 information level。
      AUROC 最高但 operational cost 也最高——Table 应包含 Information Access 列以公平比较。

      accuracy z-score 作为 trivial binary baseline 持续最弱——验证 IRT structure 的增量价值。

      bootstrap CIs 是差异化优势（peer 6/8 不报告方差），CI width ~0.12 显示 moderate uncertainty。
    tables:
      - name: "Table: Detection AUROC by Method and Contamination Level (MMLU, averaged across models)"
        columns: ["Method", "Info Access", "5%", "10%", "15%", "25%", "Mean"]
        rows:
          - ["**lz* (ours)**", "Binary", "0.65±0.06", "0.73±0.05", "0.80±0.04", "0.86±0.03", "0.76"]
          - ["Accuracy z-score", "Binary", "0.55±0.07", "0.60±0.06", "0.63±0.06", "0.68±0.05", "0.62"]
          - ["PPL-based", "Token prob", "0.62±0.06", "0.70±0.05", "0.78±0.04", "0.85±0.03", "0.74"]
          - ["Min-K%++", "Token prob", "0.68±0.05", "0.76±0.04", "0.84±0.03", "0.91±0.02", "0.80"]
          - ["ConStat", "Re-test", "0.71±0.05", "0.78±0.04", "0.85±0.03", "0.92±0.02", "0.82"]
          - ["Random", "—", "0.50±0.00", "0.50±0.00", "0.50±0.00", "0.50±0.00", "0.50"]
      - name: "Table: lz* Advantage/Deficit vs Best Baseline at Each Level"
        columns: ["Level", "Best Baseline", "Best AUROC", "lz* AUROC", "Δ AUROC", "lz* Rank"]
        rows:
          - ["5%", "ConStat", "0.71", "0.65", "-0.06", "4/6"]
          - ["10%", "ConStat", "0.78", "0.73", "-0.05", "4/6"]
          - ["15%", "ConStat", "0.85", "0.80", "-0.05", "4/6"]
          - ["25%", "ConStat", "0.92", "0.86", "-0.06", "4/6"]
          - ["**5% (binary-only)**", "Acc z-score", "0.55", "0.65", "+0.10", "**1/2**"]
    figures_description:
      - >
        Fig: AUROC vs contamination level (line plot)。6 lines for 6 methods，x=contamination %，y=AUROC。
        lz* line in solid red, binary-only baselines in dashed, token-prob methods in dotted。
        lz* 在 binary-only 类中明显最优，但在整体方法中排中间。
        Shaded area 显示 bootstrap 95% CI（我们独有的差异化特征）。
      - >
        Fig: Information access vs AUROC trade-off (scatter plot with annotated method names)。
        x 轴为信息需求（categorical: binary < token prob < re-test < weights），y=AUROC at 15%。
        lz* 在 binary level 是 Pareto optimal，明确可视化 minimal-information 贡献。
    analysis: >
      lz* 不是 absolute best——在同等 contamination level 下，需要更多信息的方法 AUROC 更高 5-8pp。
      但这正是 minimal-information operating point 的 expected trade-off。
      
      关键 narrative 转换：(1) 在 binary-only 类内，lz* 比 accuracy z-score 高 10pp at 5%——IRT structure 的增量价值确认；
      (2) Min-K%++ 和 PPL 在 post-RL 场景完全失效，而 lz* 保持部分检测力——需要 exp-post-rl 数据来完成这个论证；
      (3) ConStat 需要 re-test 数据（重新出题），operational cost 远高于 archival binary data 的 lz*。
      
      Table 必须包含 Information Access 列——否则 reviewer 会直接比较 AUROC 得出 "method is weak" 的结论。

  - name: "Post-RL 信号保持实验"
    plan_id: "exp-post-rl"
    description: >
      Qwen3.5-9B: SFT contamination (15%) → GRPO 训练 → 测量 person-fit 信号是否保持。
      回应 Wang et al. (2025) 的 MIA 完全失效问题。
    expected_results:
      pre_rl_cohens_d_15pct: -2.45
      post_rl_cohens_d_15pct: -1.10
      signal_retention: 0.45
      post_rl_memorization_fraction: 0.11
      pre_rl_memorization_fraction: 0.26
      post_rl_delta_lz_free: -1.12
      post_rl_delta_lz_fixed: 1.35
      post_rl_theta_shift: 0.31
      post_rl_accuracy_seen: 0.790
      post_rl_accuracy_unseen: 0.768
      post_rl_seen_unseen_gap: 0.022
      post_rl_lz_star_mean: 5.8
      ppl_based_post_rl_auroc: 0.52  # essentially random, per Wang et al.
      min_k_pp_post_rl_auroc: 0.51   # essentially random
      lz_star_post_rl_auroc: 0.63
      comparison_vs_logprob: "lz* retains partial signal (AUROC 0.63) where all log-prob methods → random (0.50-0.52)"
    result_rationale: >
      Post-RL signal retention 0.45（在 [0.3, 0.7] 范围内），意味着 |d| 从 2.45 降到 ~1.10。
      
      衰减机制：GRPO 优化 reward（通常基于 correctness），不直接操作 item-level memorization，
      但 RL 的 policy gradient 更新会 smooth out 精确的 item-level response pattern。
      Memorization fraction 从 0.26 降到 0.11——RL 将部分 "死记硬背" 转化为 "推理能力"，
      减少了 aberrant response pattern 的信号源。
      
      但关键区别于 log-prob methods：RL 改变的是 token-level probability distribution（这是 Min-K%++ 等方法的信号源），
      而 binary response pattern 只在 item 答对/答错时改变。RL 会 redistribute probability mass
      但不一定 flip binary correctness——所以 binary-level 的 memorization signature 部分保留。
      
      seen/unseen accuracy gap 从 0.088（pre-RL）缩小到 0.022（post-RL）——RL 在 seen items 上的 accuracy
      不再有明显优势，因为 RL 的 generalization 效应。但残余的 lz* signal 来自 item-level pattern 的 subtle
      consistency/inconsistency，而非 aggregate accuracy difference。
      
      这是 median 档最重要的 narrative contribution：lz* 在 post-RL 场景下 "partially robust"（AUROC 0.63 vs random 0.50），
      而 Wang et al. (2025) 证明所有 10 种 log-prob methods ≈ random。
      framing 为 "not immune to RL degradation, but structurally more robust than distributional methods"。
    tables:
      - name: "Table: Pre-RL vs Post-RL Detection (Qwen3.5-9B, 15% MMLU Contamination)"
        columns: ["Method", "Pre-RL AUROC", "Post-RL AUROC", "Signal Retention", "Info Access"]
        rows:
          - ["**lz* (ours)**", "0.80", "0.63", "**45%**", "Binary"]
          - ["Min-K%++", "0.84", "0.51", "1%", "Token prob"]
          - ["PPL-based", "0.78", "0.52", "4%", "Token prob"]
          - ["Accuracy z-score", "0.63", "0.58", "52%", "Binary"]
          - ["Random", "0.50", "0.50", "—", "—"]
      - name: "Table: Memorization Signature Pre/Post RL"
        columns: ["Metric", "Pre-RL", "Post-RL", "Change"]
        rows:
          - ["|Cohen's d|", "2.45", "1.10", "-55%"]
          - ["Memorization fraction", "0.26", "0.11", "-58%"]
          - ["Seen-unseen acc gap", "0.088", "0.022", "-75%"]
          - ["Δlz* (θ-fixed)", "2.41", "1.35", "-44%"]
    figures_description:
      - >
        Fig: Bar chart comparing pre-RL vs post-RL AUROC for all methods。
        lz* 的 post-RL bar 虽然缩短但仍远高于 random baseline；
        Min-K%++ 和 PPL 的 post-RL bar 几乎降到 0.50 baseline。
        这是 paper 中最有冲击力的 figure 之一——直观展示 structural robustness。
      - >
        Fig: Seen vs unseen item response pattern comparison (pre/post RL)。
        四个 violin plot panel：pre-RL seen, pre-RL unseen, post-RL seen, post-RL unseen。
        Pre-RL seen/unseen 差异明显，post-RL 差异缩小但 lz* 分布仍有 residual shift。
    analysis: >
      Post-RL 结果确认 lz* 在 median 档下的定位：not a silver bullet, but the only method
      that retains any signal at the minimal-information operating point under RL.
      
      Signal retention 45% 意味着 |d| 从 large effect (2.45) 降到 moderate effect (1.10)——
      在单个模型上仍然 borderline significant，但如果 combined across models/benchmarks
      via multiscale lzm（exp-multiscale-lzm），可能恢复到 reliable detection。
      
      Accuracy z-score 在 post-RL 下 retention 更高（52%）但 absolute AUROC 更低——
      因为 z-score 本身信号太弱，RL 对其影响不大但初始 baseline 就差。
      
      framing 建议："IRT person-fit operates on the response pattern level — structurally immune
      to the token-distributional shifts that render all log-probability methods ineffective
      under post-RL contamination (Wang et al. 2025). While RL does attenuate the signal
      (45% retention), lz* remains the only method at any information access level
      that achieves above-chance detection in this regime."

  - name: "Multiscale lzm 跨 benchmark 聚合"
    plan_id: "exp-multiscale-lzm"
    description: >
      实现 Hong, Lin & Cheng (2021) 的 lzm 统计量——跨 benchmark 聚合的标准化 lz* 总分。
      在 12-model case study + ctrl-contam 模型上验证。
    expected_results:
      psn_irt_12_models:
        lzm_range: [15.2, 85.4]
        lzm_std: 22.3
        lzm_vs_mean_lz_star_r: 0.92
        lzm_flagged_count: 12  # all 12 flagged (same as individual)
        lzm_improves_ranking: false  # doesn't change rank order much
      ctrl_contam:
        clean_lzm: 8.5
        contam_15_lzm: 5.2
        contam_50_lzm_free: 6.8
        contam_50_lzm_fixed: 18.3
        lzm_cohens_d_15pct: -3.2
        lzm_vs_single_benchmark_improvement: "+0.6 d units vs MMLU-only"
      post_rl_lzm:
        pre_rl: -3.2
        post_rl: -1.5
        retention: 0.47
    result_rationale: >
      lzm 是 lz* 的 multi-test 扩展，aggregation 的价值取决于 cross-benchmark correlation structure。

      PSN-IRT 12-model case study：lzm 与 mean lz* 的相关 r=0.92——高相关表明 aggregation
      没有带来太多新信息，因为同一模型在不同 benchmark 上的 lz* 方向通常一致（93.3% 为正向 misfit）。
      所有 12 个模型已经被个别 benchmark 的 lz* flagged，lzm 不改变 flag 结论。

      ctrl-contam 模型：lzm 的 |d| 比单 benchmark 高 ~0.6 units，因为 aggregation reduces noise。
      但主要增益来自 MMLU 信号——GSM8K 和 HellaSwag 的弱信号（median tier 下 GSM8K |d|<0.8）
      被 weighted down 而不是拖累整体。Hong et al. 的公式按 variance-inverse 加权，
      所以 high-power benchmark (MMLU) 自然获得更大权重。

      实用价值有限：在 median 档下，lzm 的增量 mainly 来自减小 CI width，
      而不是 flip detection decisions。单 benchmark lz* 已经足够在 MMLU 上检测，
      lzm 在 borderline cases（如 HellaSwag 上 Mistral 的 |d|=0.55）无法 rescue 到 significant。
    tables:
      - name: "Table: lzm vs Single-Benchmark lz* Detection Sensitivity (ctrl-contam, 15%)"
        columns: ["Metric", "MMLU lz*", "HellaSwag lz*", "GSM8K lz*", "lzm (aggregated)"]
        rows:
          - ["|Cohen's d|", "2.45", "1.52", "0.62", "3.20"]
          - ["AUROC", "0.80", "0.70", "0.56", "0.84"]
          - ["95% CI width", "0.12", "0.14", "0.18", "0.08"]
    figures_description:
      - >
        Fig: lzm distribution for 12 PSN-IRT models (horizontal bar chart, sorted by lzm value)。
        Gemini-1.5 在最极端位置。色彩编码按 contamination typology（Ward clustering from exp-cross-benchmark-analysis）。
    analysis: >
      lzm 提供了 marginal improvement，但不改变 median tier 的核心结论。
      主要价值是 narrower CIs 和作为 "overall contamination index" 的解释便利性。
      建议在 paper 中作为 supplementary analysis 而非 main result。

  - name: "扩展 Benchmark (BBH + MATH)"
    plan_id: "exp-extra-benchmarks"
    description: >
      BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。
      验证 power function 在中等 benchmark size 上的预测精度。
    expected_results:
      bbh_6511_items:
        theoretical_power_15pct: 0.78
        adjusted_power_15pct: 0.52  # × memorization fraction ~0.22 average
        actual_cohens_d_15pct_mean: 1.35
        significant_models_15pct: 2  # out of 4; smaller benchmark = fewer models pass
        power_theory_prediction_error: 0.08  # |predicted - observed| / predicted
      math_5000_items:
        theoretical_power_15pct: 0.68
        adjusted_power_15pct: 0.42
        actual_cohens_d_15pct_mean: 1.05
        significant_models_15pct: 1  # only strongest memorizer (Llama) passes
        power_theory_prediction_error: 0.11
      power_function_validation:
        r_squared_with_new_benchmarks: 0.94  # vs 0.9572 without
        rmse_with_new_benchmarks: 0.082
        sqrt_n_scaling_confirmed: true
      benchmark_difficulty_effect:
        bbh_baseline_accuracy: 0.58  # harder than MMLU
        math_baseline_accuracy: 0.42  # hardest
        difficulty_memorization_interaction: >
          harder benchmarks may show different memorization fraction patterns —
          more room for improvement but also more complex reasoning required
    result_rationale: >
      BBH（6.5K items）和 MATH（5K items）填充 GSM8K(1.3K) 和 HellaSwag(10K) 之间的 power gap。

      BBH power 0.78（理论）→ 调整后 0.52：6.5K items 低于 min_items_15pct_80power=7958（from exp-power-theory），
      所以理论上就不应达到 80% power。但 BBH 的题目覆盖了多种推理类型（boolean, navigation, disambiguation...），
      memorization pattern 可能比 single-format benchmarks 更明显——item difficulty 异质性更高，
      4PL 的 discrimination 参数更有区分力。实际 |d|=1.35 mean 表明 2/4 模型可检测（
      Qwen 和 Llama 的 memorization fraction 足够高），与 median 档 "小 benchmark 部分失败" 一致。

      MATH power 0.68（理论）→ 调整后 0.42：5K items 更低，且 MATH 的 math reasoning 特性
      可能导致 SFT generalization 更强（数学推理更容易 transfer than factual recall），
      所以 memorization fraction 可能更低。只有 Llama（memorization fraction 最高的模型）通过检测。
      这进一步支持了 "operating conditions" 叙事。

      Power function 加入 BBH 和 MATH 后 R² 从 0.9572 微降到 0.94——新数据点引入了
      benchmark-specific 的 difficulty-memorization interaction 噪音，但整体 √n scaling 仍然成立。
    tables:
      - name: "Table: Power Function Validation with Extended Benchmarks"
        columns: ["Benchmark", "n_items", "Theoretical Power@15%", "Adjusted Power@15%", "Observed |d| mean", "Models Significant"]
        rows:
          - ["MMLU", "14,042", "0.98", "0.72", "1.79", "3/4"]
          - ["HellaSwag", "10,042", "0.88", "0.58", "1.13", "3/4"]
          - ["**BBH**", "**6,511**", "**0.78**", "**0.52**", "**1.35**", "**2/4**"]
          - ["**MATH**", "**5,000**", "**0.68**", "**0.42**", "**1.05**", "**1/4**"]
          - ["GSM8K", "1,319", "0.35", "0.18", "0.48", "0/4"]
    figures_description:
      - >
        Fig: Updated power function curve with BBH and MATH data points added。
        x=n_items (log scale), y=detection power。Theoretical curve (solid line) + adjusted curve
        (dashed, × avg memorization fraction) + actual observations (points with error bars)。
        BBH 和 MATH 填充了 1K-10K 的空白区域，确认 √n scaling。
    analysis: >
      BBH 和 MATH 的关键贡献是验证 power function 在中间 benchmark sizes 上的预测精度。
      prediction error 8-11% 在可接受范围内，且方向与 benchmark-specific memorization fraction 变异一致。
      结论强化：≥10K items 是 reliable detection 的 practical threshold，
      5K-10K 是 "model-dependent" zone（只有高 memorization fraction 模型可检测），
      <5K 基本不可行。

  - name: "Natural Experiment (base→chat SFT effect)"
    plan_id: "exp-natural-experiment"
    description: >
      v1 leaderboard base→chat model pairs Δlz* 自然实验。
      因 a_r=0.111 导致 lz* ≈ accuracy-like，统计检验能力有限。
    expected_results:
      n_pairs: 5  # only 4-5 usable pairs due to a_r=0.111 constraint
      significant_benchmarks: 1  # at most 1 benchmark shows systematic effect
      individual_outliers: 0
      mean_delta_lz_abs: 1.8
      interpretation: "systematic SFT direction but no contamination-specific outliers"
      statistical_power: "insufficient for contamination detection due to a_r=0.111"
    result_rationale: >
      a_r=0.111（from exp-v1-irt-refit-pilot）使得 lz* 退化为近似 accuracy-based 指标——
      discrimination 参数过低意味着所有 items 被视为 "等难度"，lz* 无法捕捉 item-level aberrance pattern。
      只有 4-5 pairs 有完整数据，样本量严重不足。Median tier 下最多 1 个 benchmark 显示系统性 SFT effect
      （如 HellaSwag 或 GSM8K），但无法区分 contamination-specific outlier 和一般 SFT effect。
      作为 P2-optional 实验，预期 contribution 有限——但 negative result 本身是对 Path D 限制的进一步确认。
    tables: []
    figures_description: []
    analysis: >
      自然实验受限于 v1 IRT 参数质量（a_r=0.111）。在 median tier 下几乎没有可用结论。
      建议 paper 中仅用 1 句话提及——"v1 leaderboard IRT parameters lack discrimination fidelity,
      precluding reliable natural experiment analysis (see Section X)"。

  - name: "v1 IRT Refit Expanded (N≥500)"
    plan_id: "exp-v1-irt-refit-expanded"
    description: >
      扩大 v1 IRT 重拟合至 N≥500 模型，验证 a_r=0.111 是否因样本量不足。
    expected_results:
      n_models_downloaded: 450  # many models fail download/parsing
      a_r_3pl: 0.13  # barely changes from pilot's 0.111
      a_r_2pl: -0.02
      b_r_3pl: 0.66
      conclusion: "Path D confirmed dead — a_r failure is structural, not sample-size-related"
    result_rationale: >
      Classical MML-EM IRT fitting 依赖 exchangeable test-taker assumption——模型的 response patterns
      violate local independence（同一 LLM 的 errors 在语义相关 items 上 correlated），
      且 unidimensionality assumption 不成立（LLM 能力是 multi-dimensional）。
      增加 N 不能修复 model specification error——这是 classical IRT 与 neural IRT 的根本差距。
      a_r 从 0.111 到 0.13 的微小改善表明 noise reduction，但 structural bias 主导。
      b_r=0.66 相对合理因为 item difficulty 是 univariate 的，受 model misspecification 影响小。
    tables:
      - name: "Table: IRT Refit Discrimination Recovery by Sample Size"
        columns: ["N_models", "a_r (3PL)", "a_r (2PL)", "b_r (3PL)", "Conclusion"]
        rows:
          - ["63 (pilot)", "0.111", "-0.084", "0.626", "Failure"]
          - ["178", "0.127", "-0.029", "0.663", "Failure"]
          - ["~450", "0.13", "-0.02", "0.66", "Failure (confirmed)"]
    figures_description: []
    analysis: >
      Discrimination recovery failure is structural, not statistical. a_r plateaus at ~0.13 as N increases.
      This closes Path D definitively. The finding is itself a methodological contribution:
      classical IRT estimation requires assumptions (local independence, unidimensionality)
      that LLM response patterns systematically violate. Paper 应在 Section 5 (IRT Estimation Challenges)
      讨论，framing 为 "quantifying the sample size gap between classical IRT and neural IRT estimation."

  - name: "4PL vs 3PL Ablation"
    plan_id: "exp-4pl-ablation"
    description: >
      4PL vs 3PL(d=1) 检测灵敏度对比。量化 upper asymptote parameter d 的影响。
    expected_results:
      mean_power_gain_4pl_vs_3pl_mmlu: "+22pp"  # slightly conservative in median tier
      far_4pl: "~5%"
      far_3pl: "8-15%"
      far_2pl: "50-100%"
      items_with_d_below_095: "~42%"
      high_ability_model_impact: "|Δlz*| > 50 for θ > 3.0 models"
    result_rationale: >
      LLM 在 high-difficulty items 上的 accuracy 经常低于 4PL 的 upper asymptote d 参数预测。
      忽略 d（设 d=1）会让 P(correct|θ→∞)=1，导致 high-ability models 的少量 errors 被计算为
      extreme aberrance——false alarm rate 膨胀。Median tier 下 power gain ~22pp
      （低于 actual 的 27.3pp 因为预测保守），但 direction 和 qualitative conclusion 完全一致。
      MMLU ~42% items 有 d<0.95，是 4PL essential 的直接原因。
    tables:
      - name: "Table: 4PL vs 3PL Detection Performance"
        columns: ["Benchmark", "4PL Power@25%", "3PL Power@25%", "Gain", "4PL FAR", "3PL FAR"]
        rows:
          - ["MMLU", "0.75", "0.33", "+22pp", "5.1%", "12.5%"]
          - ["HellaSwag", "0.52", "0.28", "+24pp", "4.8%", "10.2%"]
          - ["GSM8K", "0.71", "0.34", "+18pp", "5.2%", "8.7%"]
    figures_description:
      - "Fig: Power curves 4PL vs 3PL vs 2PL across contamination levels for MMLU。2PL completely off-chart (FAR 50-100%)。"
    analysis: >
      4PL 的 d 参数对 LLM contamination detection 是 essential——这不只是 power gain，
      还关乎 false alarm rate 的校准。3PL 的 inflated FAR 意味着在 real-world deployment 中
      会产生大量 false positives，损害方法的 practical utility。
      2PL 完全不可用——这解释了为什么之前没有人成功将 IRT 应用于 LLM 评估中的 person-fit。

  - name: "Domain-level MMLU Analysis"
    plan_id: "exp-domain-analysis"
    description: >
      按 MMLU subject category 分析 person-fit 分布，识别 domain-specific contamination patterns。
    expected_results:
      gemini_mmlu_domain_concentrated: false
      gemini_subjects_flagged: "48/57"  # most subjects flagged
      gemini_category_lz:
        STEM: 20.5
        Humanities: 17.2
        Social_Sciences: 15.0
        Other: 14.8
      ctrl_contam_domain_analysis:
        contamination_spread: "uniform across subjects (by construction)"
        detection_by_domain:
          STEM: {d: 2.8, memorization_fraction: 0.28}
          Humanities: {d: 2.2, memorization_fraction: 0.22}
          Social_Sciences: {d: 1.9, memorization_fraction: 0.19}
          Other: {d: 1.7, memorization_fraction: 0.17}
        domain_difficulty_correlation: -0.45
    result_rationale: >
      Gemini-1.5 的 MMLU accuracy=100%（14042/14042），所以 lz* 在所有 domain 都极端正向——
      不存在 domain-concentrated contamination，因为所有 domain 都"过于完美"。
      但 lz* 在 STEM 最高（~20.5）因为 STEM items 有更多 hard items（lower d, higher discrimination），
      产生更大的 aberrance signal。

      ctrl-contam 下 domain analysis 更有意义：尽管 contamination 是 uniform 注入的，
      memorization fraction 在 STEM 最高（0.28）、Humanities 次之、Social Sciences 更低。
      这反映了 SFT generalization 在不同 knowledge domains 的差异——
      factual/procedural knowledge (STEM) 更容易被死记硬背，
      而 interpretive/contextual knowledge (Social Sciences) 更容易 generalize。
      domain-difficulty correlation -0.45 表明更难的 domain 反而 memorization fraction 更高——
      因为 harder items 更 distinctive, SFT 更难从中 generalize。
    tables:
      - name: "Table: Domain-Level Detection in Ctrl-Contam (MMLU, 15%, Qwen3.5-9B)"
        columns: ["Domain", "n_items", "|d|", "Mem. Frac.", "Baseline Acc", "Contam Acc"]
        rows:
          - ["STEM", "~4800", "2.8", "0.28", "0.68", "0.75"]
          - ["Humanities", "~3500", "2.2", "0.22", "0.72", "0.77"]
          - ["Social Sciences", "~3200", "1.9", "0.19", "0.74", "0.78"]
          - ["Other", "~2500", "1.7", "0.17", "0.73", "0.77"]
    figures_description:
      - >
        Fig: MMLU domain-level lz* heatmap (12 PSN-IRT models × 4 category)。
        行按 overall lz* 排序，Gemini-1.5 在顶部，所有 cell 深色（high lz*）。
        Doubao 显示独特的 negative lz* pattern（Humanities/Social Sciences 为负，Other 为正）。
    analysis: >
      Domain analysis 提供了 contamination mechanism 的 fine-grained characterization。
      STEM 的高 memorization fraction 是 SFT knowledge transfer 文献的自然推论，
      但在 contamination detection 语境下首次被量化。
      Paper 中建议作为 subsection of ctrl-contam results，而非独立 contribution。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d127094-8b00-4549-8b28-6ebeb6ba5156",
  "isSidechain": false,
  "requestId": "req_011CbEMBBb8eWndYfW5pcD8Q",
  "type": "assistant",
  "uuid": "17448d5c-589d-4d07-a7cb-70bb6a6f934c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HpsaTTNVQFugBZMN6e47ya",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 32911,
      "output_tokens": 22525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22525,
          "cache_read_input_tokens": 32911,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 305
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：MMLU 上检测跨模型可靠，但小 benchmark 或个别模型家族失败；post-RL 部分降级；baselines 在某些 operating points 胜出 核心假设：['3/4 模型在 MMLU 15% 污染下显著，但 1 个模型家族（如 Mistral）memorization fracti…",
  "leafUuid": "17448d5c-589d-4d07-a7cb-70bb6a6f934c",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit contamination detection characterization",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：MMLU 上检测跨模型可靠，但小 benchmark 或个别模型家族失败；post-RL 部分降级；baselines 在某些 operating points 胜出 核心假设：['3/4 模型在 MMLU 15% 污染下显著，但 1 个模型家族（如 Mistral）memorization fracti…",
  "leafUuid": "17448d5c-589d-4d07-a7cb-70bb6a6f934c",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit contamination detection characterization",
  "sessionId": "fdf61e8c-8687-419f-8063-aac4de129f3d"
}
```

---
