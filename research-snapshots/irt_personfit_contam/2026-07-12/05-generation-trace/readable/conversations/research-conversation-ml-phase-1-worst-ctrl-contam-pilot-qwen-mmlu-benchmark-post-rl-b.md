# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：ctrl-contam 仅在原始 pilot 条件（Qwen × MMLU）可复现，跨模型/benchmark 泛化失败；post-RL 信号消失；b

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/da95c0ff-ced2-4e03-b8c9-deac6714a1b8.jsonl`
- **Structured JSON:** [`a572de2ee24ff8fea07b.json`](../../sessions/a5/a572de2ee24ff8fea07b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:17:04.641Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:17:04.641Z",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：ctrl-contam 仅在原始 pilot 条件（Qwen × MMLU）可复现，跨模型/benchmark 泛化失败；post-RL 信号消失；baselines 多数场景胜出\n核心假设：['仅 1-2/4 模型在 MMLU 15% 下显著——SFT generalization 在多数模型上将 memorization fraction 压到 <15%', 'θ-shift 机制在某些模型上不可控：θ-fixed 也无法恢复单调 dose-response', 'Post-RL 完全消除 person-fit 信号（retention <30%），与 MIA 方法一样失效', 'ML baselines 在 10%+ 全面胜出 lz*，lz* 仅在极低污染率（3-5%）有微弱优势但 AUROC < 0.65 无实用价值', 'Universal 4PL misfit、θ-shift mechanism、seen/unseen fingerprint 等发现仍成立但检测实用性不足']\n关键指标范围：{'cohens_d_15pct_across_models': [0.3, 1.5], 'cohens_d_15pct_min_model': [0.1, 0.5], 'models_significant_at_15pct': [1, 2], 'benchmarks_significant_per_model': [1, 1], 'memorization_fraction_15pct': [0.05, 0.2], 'theta_fixed_dose_response_ratio': [0.8, 2.0], 'post_rl_signal_retention': [0.0, 0.3], 'lz_star_auroc_5pct': [0.5, 0.62], 'lz_star_auroc_10pct': [0.55, 0.7], 'lz_star_minus_best_baseline_auroc_5pct': [-0.15, -0.03], 'seen_unseen_lz_gap_15pct': [0.3, 1.5]}\n叙事方向：核心 reframe：从 \"contamination detection method\" 转向 \"psychometric diagnostics for LLM evaluation\"。三条 claims 重构—— Claim 1 变为：IRT person-fit 为 LLM benchmark 评估提供 principled diagnostic 工具， ctrl-contam 的 pilot 成功 + full 失败共同量化了 binary-only detection 的 fundamental limits （这本身是对 detection frontier 的贡献：我们精确度量了 minimal-information operating point 的天花板）。 Claim 2 保留 power function 理论贡献，但增加 \"adjusted power after SFT generalization\" 的 empirical bound，展示理论上限与实际信号的 gap 作为 SFT generalization 量化。 Claim 3 的重心转移到三个 standalone 发现：(a) universal 4PL misfit 作为 LLM response pattern 的结构性发现（所有 LLM 都不是 classical test-takers），(b) θ-shift mechanism 作为 person-fit 在 adaptive testing 场景中的 methodological warning，(c) memorization fraction 的跨模型 异质性揭示 SFT generalization 的本质。 仍冲 EMNLP——venue fit 从 \"evaluation methodology\" 转为 \"empirical analysis of LLM evaluation assumptions\"，类似 \"Are LLMs classical test-takers? Evidence from IRT person-fit analysis\" 的 empirical study framing。不降级目标。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_personfit_contam\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct) validate the framework on real models: at 15% contamination, |Cohen's d|=3.85 with clear seen/unseen memorization fingerprint (seen lz*≈0 vs unseen=3.1). θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity degrades at high contamination (50%), but fixing θ to pre-contamination baseline restores monotonic dose-response (ratio=2.93). The memorization fraction (~38% at 15% contamination) quantifies the SFT generalization effect — the gap between theoretical power and actual detection signal.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+34.75, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.\n6. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n7. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×2 seeds, 15%, 50%). Key results: (a) contam_15 |Cohen's d|=3.85 (strong detection signal); (b) free-θ dose-response non-monotonic (contam_50 Δlz*=1.53 < contam_15 Δlz*=3.97) due to θ-shift confound; (c) **θ-fixed analysis restores monotonicity** (Δlz*_fixed: contam_15=+2.96, contam_50=+8.67, ratio=2.93); (d) seen/unseen split: contam_15 seen lz*≈0 vs unseen=3.1 (clear memorization fingerprint); (e) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-two-sided\n  registry_id: exp-two-sided\n  claim: 2\n  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case\n    study）。包括 bootstrap confidence interval 和 FDR 控制。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- id: exp-extended-sim\n  registry_id: exp-extended-sim\n  claim: 2\n  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让\n    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向\n    lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 依赖 exp-two-sided 的双侧框架定义。\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- id: exp-ctrl-contam-pilot\n  claim: 1,2,3\n  description: 快速验证：Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU only。测量\n    Δlz*(clean→contaminated) 是否显著。增加第二个 0% seed 作为 clean-vs-clean noise floor baseline\n    (Reviewer Q2/Q4)。Eval 时区分 seen/unseen items 以实测 memorization fraction (Reviewer\n    Q3/W9)。这是论文 go/no-go 信号。\n  priority: P0-CRITICAL\n  gpu_budget_hours: 12\n  deps: []\n  status: planned\n  notes: 'GPU 恢复后第一优先。4 conditions × ~3 hrs = ~12 GPU-hrs (+2h for second 0% seed)。关键输出:\n    (a) Δlz* 显著性, (b) clean-vs-clean Δlz* ≈ 0 验证, (c) memorization fraction = (Δacc_seen\n    - Δacc_unseen)/Δacc_seen, (d) adjusted power = theory × memorization fraction。D010\n    要求。'\n- id: exp-ctrl-contam\n  claim: 1,2,3\n  description: 完整控制实验：在 4 个模型上用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量\n    Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - exp-ctrl-contam-pilot\n  status: planned\n  notes: '模型: Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3。Benchmark:\n    MMLU + GSM8K + HellaSwag。4 模型 × 6 levels × 3 benchmarks。'\n- id: exp-empirical-null\n  registry_id: exp-empirical-null\n  claim: 1\n  description: Bootstrap empirical null 分析：量化 lz* 在真实 LLM 数据上的 systematic bias（null\n    mean ≠ 0, null std ≠ 1），为 Calibration Gap Analysis 提供定量证据。包含 Q-Q plots、KS tests、bias\n    量化表、unflagged cells 深度分析。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 复用 exp-two-sided v2 的 bootstrap 逻辑，但保存完整中间分布。~2h 开发+运行。\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- id: exp-power-theory\n  registry_id: exp-power-theory\n  claim: 2\n  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A\n    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: DONE\n  notes: 纯理论推导 + 数值验证。CPU only.\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- id: exp-leaderboard-data-recon\n  registry_id: exp-leaderboard-data-recon\n  claim: 3\n  description: Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results\n    是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item\n    data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: 纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- id: exp-leaderboard-audit\n  claim: 3\n  description: Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark\n    污染率随时间趋势。\n  priority: ABANDONED\n  gpu_budget_hours: 20\n  deps:\n  - exp-two-sided\n  - exp-leaderboard-data-recon\n  status: planned\n  notes: 'D011: v1-irt-refit a_r=0.111 + item alignment 54.56% → 13K audit 不可行。数据可用性写入\n    Discussion/Future Work。'\n- id: exp-natural-experiment\n  claim: 3\n  description: v1 leaderboard base→chat model pairs 自然实验：计算 Δlz* = lz*(chat) - lz*(base)\n    作为 SFT 效应代理。\n  priority: P2-optional\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: 'D013: a_r=0.111 导致 lz*≈accuracy-like, 仅 4-5 pairs 无统计检验能力。Reviewer 终审建议降级。'\n- id: exp-v1-irt-refit-expanded\n  claim: 3\n  description: 扩大 v1 IRT 重拟合样本量至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。最终关闭 Path\n    D。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: CPU only. Reviewer 要求 N≥500 才能最终结论 Path D。阈值：a_r>0.4=可行, a_r<0.2=dead。\n- id: exp-4pl-ablation\n  claim: 1\n  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter\n    d 对 false alarm 和 detection power 的影响。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\n- id: exp-baseline-comparison\n  claim: 1\n  description: '与现有方法对比（≥5 baselines）：在控制实验的 ground-truth contaminated models 上，比较\n    IRT-FIT vs baselines 的 AUROC/Type-I error。Baselines: (1) ConStat (re-test), (2)\n    Min-K%++ (token probs), (3) accuracy z-score (已完成, CPU), (4) PPL-based detection\n    (log-prob family 代表, 预期 RL-robust 测试中失败), (5) random baseline。量化 minimal-information\n    的代价（power 损失）。报告 bootstrap CIs（同行 6/8 不报告方差，这是我们的差异化优势）。'\n  priority: P0-end\n  gpu_budget_hours: 30\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: 蒸馏显示同行 baseline 中位数 ~5 个。accuracy z-score 已完成(CPU)。ConStat 需 re-test, Min-K%++\n    需 token probs, PPL 需 log-probs。exp-ctrl-contam 完成后立即执行。\n- id: exp-multiscale-lzm\n  claim: 1,3\n  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化\n    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要实现 lzm 公式。\n- id: exp-post-rl\n  claim: 1\n  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应\n    Wang et al. (2025) 的 MIA 失效问题。\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\n- id: exp-extra-benchmarks\n  claim: 2,3\n  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items\n    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\n- id: exp-domain-analysis\n  claim: 3\n  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5\n    的 MMLU 污染是全面的还是集中在特定 domain。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要 MMLU item-to-domain 映射。\n\n\n## registry (completed experiments)\n\n- exp_id: sim_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    null_check:\n      all_pass: true\n      gsm8k_ks_p: 0.098\n      hellaswag_ks_p: 0.224\n      mmlu_ks_p: 0.594\n    simulation_power_at_15pct:\n      mmlu: 0.979\n      hellaswag: 0.733\n      gsm8k: 0.578\n      arc_c: 0.129\n      humaneval: 0.243\n    global_pass: false\n    inverted_u_all_benchmarks: true\n    pass_count_large_80pct: 1/3 (mmlu only)\n- exp_id: phase_b_personfit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_sd_all_gt_0.5: true\n    mmlu_lz_star_mean: 24.19\n    mmlu_lz_star_sd: 16.47\n    hellaswag_lz_star_mean: 20.09\n    hellaswag_lz_star_sd: 17.59\n    gsm8k_lz_star_mean: 8.22\n    gsm8k_lz_star_sd: 8.97\n    gemini15_mmlu_lz_star: 34.75\n    gemini15_mmlu_accuracy: 1\n    gemini15_mmlu_theta: 0.78\n    gemini15_flagged_benchmarks: 3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\n    cross_benchmark_spearman_significant: 1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\n    n_models: 12\n    n_benchmarks: 5\n- exp_id: exp-two-sided\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- exp_id: exp-extended-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- exp_id: exp-empirical-null\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- exp_id: exp-leaderboard-data-recon\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- exp_id: exp-power-theory\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- exp_id: exp-item-alignment-check\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    match_rate_direct: 0.5456\n    match_rate_reordered_mistral: 0.8846\n    match_rate_reordered_vicuna: 0.7248\n    n_items_checked: 14042\n    n_models_verified: 2\n    alignment_method: content-based via cais/mmlu canonical order\n    items_mapped: 12068\n    mapping_coverage: 0.86\n- exp_id: exp-v1-irt-refit-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 63\n    n_models_failed: 38\n    n_items: 14042\n    n_mapped_items: 12441\n    overall_accuracy: 0.426\n    fitting_time_2pl_sec: 8.9\n    fitting_time_3pl_sec: 12.1\n    3pl_a_pearson_r: 0.111\n    3pl_b_pearson_r: 0.626\n    3pl_b_spearman_r: 0.656\n    2pl_a_pearson_r: -0.084\n    2pl_b_pearson_r: 0.572\n    lz_star_mean: 11.69\n    lz_star_std: 6.68\n    lz_star_flagged_pct: 1.6\n- exp_id: exp-accuracy-zscore-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_flagged_count: 4\n    lz_flagged_count: 57\n    agreement_rate: 0.117\n    gemini15_mmlu_zscore: 1.413\n- exp_id: exp-cross-benchmark-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_all5_flagged: 10\n    n_models_selective_flagged: 2\n    gemini15_cluster_isolation: true\n    dominant_direction_pattern: positive\n    pct_positive_cells: 93.3\n    total_flagged: 57\n    flag_rate: 0.95\n- exp_id: exp-ml-classifier-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    auroc_avg_25pct:\n      lz_star: 0.86\n      lr_resp: 0.899\n      rf_resp: 0.885\n      lr_resp_summ: 0.909\n      rf_resp_summ: 0.913\n    auroc_avg_5pct:\n      lz_star: 0.675\n      best_ml: 0.575\n    auroc_avg_10pct:\n      lz_star: 0.763\n      best_ml: 0.712\n    lz_star_advantage_low_contam: +0.10 AUROC at 5%, +0.05 at 10%\n    ml_advantage_high_contam: +0.05 at 25%, +0.16 at 50%\n    key_finding: lz* outperforms supervised ML at low contamination (5-10%) without\n      any training data; ML only wins at 25%+ where signal is already strong\n- exp_id: exp-fdr-correction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    flagged_uncorrected: 57/60 (95%)\n    flagged_bh_fdr: 57/60 (95%)\n    flagged_bonferroni: not_computed_but_expected_similar\n    correction_scope: global_60_tests\n    unflagged_cells:\n    - Yi-Lightning×arc_c (bh_p=0.098)\n    - 360GPT2-Pro×humaneval (bh_p=0.134)\n    - Yi-Lightning×humaneval (bh_p=0.181)\n    note: Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale\n      FDR (24800+ tests) deferred to leaderboard audit.\n- exp_id: exp-clean-control-delta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    clean_vs_clean_mean_abs:\n      mmlu: 0.01\n      hellaswag: 0.125\n      gsm8k: 0.021\n      arc_c: 0.095\n      humaneval: 0.02\n    clean_vs_clean_all_nonsig: true\n    clean_vs_contam_all_sig: true\n    cohens_d:\n      mmlu: 2.66\n      hellaswag: 1.85\n      gsm8k: 1.85\n      arc_c: 0.45\n      humaneval: 1.07\n    arc_c_note: d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10\n- exp_id: exp-natural-experiment\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 21\n    n_benchmarks: 4\n    n_complete_pairs: 9\n    significant_benchmarks:\n      HellaSwag:\n        mean_deviation: -3.4\n        t_stat: -3.97\n        p_value: 0.001\n        interpretation: SFT systematically decreases person-fit on HellaSwag\n      GSM8K:\n        mean_deviation: 3.92\n        t_stat: 3.35\n        p_value: 0.009\n        interpretation: SFT systematically increases person-fit on GSM8K\n    non_significant_benchmarks:\n      MMLU:\n        p_value: 0.15\n      ARC-Challenge:\n        p_value: 0.38\n    individual_outliers: 0\n    key_finding: HellaSwag and GSM8K show significant systematic SFT effects on lz*,\n      but no individual pair shows benchmark-specific contamination outliers. P2-optional\n      per Director assessment.\n- exp_id: exp-v1-irt-refit-expanded\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 178\n    n_items: 14042\n    3pl_a_pearson_r: 0.127\n    2pl_a_pearson_r: -0.029\n    3pl_b_pearson_r: 0.663\n    reason: 'N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination\n      failure confirms Path D dead.'\n- exp_id: exp-4pl-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hypothesis_confirmed: true\n    far_4pl: ~5% (well-calibrated)\n    far_3pl: 4.7-16.5% (inflated)\n    far_2pl: 50-100% (catastrophic, unusable)\n    mean_power_gain_4pl_vs_3pl:\n      MMLU: +27.3pp\n      HellaSwag: +26.1pp\n      GSM8K: +20.3pp\n      ARC_C: +14.8pp\n      HumanEval: +13.7pp\n    max_power_gain_4pl_vs_3pl:\n      MMLU: +49.0pp\n      HellaSwag: +59.6pp\n      GSM8K: +39.7pp\n      ARC_C: +54.6pp\n      HumanEval: +30.6pp\n    power_at_25pct:\n      4PL:\n        MMLU: 0.776\n        HellaSwag: 0.534\n        GSM8K: 0.73\n        ARC_C: 0.132\n        HumanEval: 0.318\n      3PL:\n        MMLU: 0.329\n        HellaSwag: 0.28\n        GSM8K: 0.334\n        ARC_C: 0.091\n        HumanEval: 0.165\n    d_bucket_analysis: 'd<0.8: +6.8pp to +61.2pp; d>=0.95: negligible'\n    key_finding: 4PL d parameter essential for LLM contamination detection. 46% MMLU\n      items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely\n      miscalibrated (FAR 50-100%).\n- exp_id: exp-domain-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_mmlu_accuracy: 100% (14042/14042)\n    gemini_domain_concentrated: false\n    gemini_subjects_flagged: 50/57 (lz*>1.96)\n    gemini_category_lz:\n      STEM: 21.2\n      Humanities: 17.9\n      Social Sciences: 15.9\n      Other: 15.3\n    doubao_negative_lz: true\n    doubao_category_lz:\n      STEM: -2\n      Humanities: -13\n      Social_Sciences: -14.8\n      Other: 4.4\n    hunyuan_uneven:\n      STEM: 1.8\n      Social_Sciences: 13.9\n    yi_lightning_highest_mmlu_lz: 48.2\n    qwen_plus_second_highest: 44.9\n    mistral_flagged_subjects: 55/57\n- exp_id: exp-ctrl-contam-pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall: partial - H1/H2 confirmed, H3/H4 not as expected under theta-free; theta-fixed\n      restores dose-response\n    H1_clean_delta_lz_approx_zero:\n      confirmed: true\n      clean_delta_lz: 2.07\n      clean_s1_lz: 8.01\n      clean_s2_lz: 5.94\n      baseline_mean: 6.98\n      baseline_std: 1.03\n    H2_contam_15_detection:\n      confirmed: true\n      delta_lz_free: -3.97\n      cohens_d: -3.85\n    H3_dose_response:\n      theta_free:\n        confirmed: false\n        contam_15_delta: -3.97\n        contam_50_delta: -1.53\n        ratio: 0.38\n        note: inverted due to theta-shift\n      theta_fixed:\n        confirmed: true\n        contam_15_delta: 2.96\n        contam_50_delta: 8.67\n        ratio: 2.93\n        note: monotonicity restored\n    H4_memorization_fraction:\n      confirmed: false\n      contam_15: 0.38\n      contam_50: 0.29\n    theta_shift:\n      clean_s1: -0.0987\n      clean_s2: -0.0842\n      contam_15: 0.1971\n      contam_50: 0.3703\n      theta_fixed: -0.0914\n    theta_fixed_analysis:\n      contam_15:\n        lz_free: 3\n        lz_fixed: 9.93\n        delta_free: -3.97\n        delta_fixed: 2.96\n        absorbed: 6.93\n      contam_50:\n        lz_free: 5.45\n        lz_fixed: 15.64\n        delta_free: -1.53\n        delta_fixed: 8.67\n        absorbed: 10.2\n    accuracy:\n      clean_s1: 0.679\n      clean_s2: 0.679\n      contam_15: 0.731\n      contam_50: 0.764\n      contam_15_seen: 0.824\n      contam_15_unseen: 0.715\n      contam_50_seen: 0.805\n      contam_50_unseen: 0.724\n- exp_id: exp-4pl-real-data-degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    correlation_4pl_vs_3pl:\n      pearson_r: 0.225\n      rmse: 68.41\n    most_affected_benchmark: MMLU (mean |Δlz*|=58.3, 46% items d<0.95)\n    most_affected_model: 'DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6'\n    low_ability_models_impact: '|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)'\n    bias_direction: 3PL systematically depresses high-ability models' lz* (d=1 makes\n      P→1, amplifying few-error aberrance)\n    key_finding: Ignoring d parameter makes lz* completely unreliable for high-ability\n      models — d-induced bias far exceeds any contamination signal\n- exp_id: exp-ctrl-contam-pilot-clean-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-clean-s2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-15\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-50\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:17:04.644Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:17:04.644Z",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T19:17:04.663Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：ctrl-contam 仅在原始 pilot 条件（Qwen × MMLU）可复现，跨模型/benchmark 泛化失败；post-RL 信号消失；baselines 多数场景胜出
核心假设：['仅 1-2/4 模型在 MMLU 15% 下显著——SFT generalization 在多数模型上将 memorization fraction 压到 <15%', 'θ-shift 机制在某些模型上不可控：θ-fixed 也无法恢复单调 dose-response', 'Post-RL 完全消除 person-fit 信号（retention <30%），与 MIA 方法一样失效', 'ML baselines 在 10%+ 全面胜出 lz*，lz* 仅在极低污染率（3-5%）有微弱优势但 AUROC < 0.65 无实用价值', 'Universal 4PL misfit、θ-shift mechanism、seen/unseen fingerprint 等发现仍成立但检测实用性不足']
关键指标范围：{'cohens_d_15pct_across_models': [0.3, 1.5], 'cohens_d_15pct_min_model': [0.1, 0.5], 'models_significant_at_15pct': [1, 2], 'benchmarks_significant_per_model': [1, 1], 'memorization_fraction_15pct': [0.05, 0.2], 'theta_fixed_dose_response_ratio': [0.8, 2.0], 'post_rl_signal_retention': [0.0, 0.3], 'lz_star_auroc_5pct': [0.5, 0.62], 'lz_star_auroc_10pct': [0.55, 0.7], 'lz_star_minus_best_baseline_auroc_5pct': [-0.15, -0.03], 'seen_unseen_lz_gap_15pct': [0.3, 1.5]}
叙事方向：核心 reframe：从 "contamination detection method" 转向 "psychometric diagnostics for LLM evaluation"。三条 claims 重构—— Claim 1 变为：IRT person-fit 为 LLM benchmark 评估提供 principled diagnostic 工具， ctrl-contam 的 pilot 成功 + full 失败共同量化了 binary-only detection 的 fundamental limits （这本身是对 detection frontier 的贡献：我们精确度量了 minimal-information operating point 的天花板）。 Claim 2 保留 power function 理论贡献，但增加 "adjusted power after SFT generalization" 的 empirical bound，展示理论上限与实际信号的 gap 作为 SFT generalization 量化。 Claim 3 的重心转移到三个 standalone 发现：(a) universal 4PL misfit 作为 LLM response pattern 的结构性发现（所有 LLM 都不是 classical test-takers），(b) θ-shift mechanism 作为 person-fit 在 adaptive testing 场景中的 methodological warning，(c) memorization fraction 的跨模型 异质性揭示 SFT generalization 的本质。 仍冲 EMNLP——venue fit 从 "evaluation methodology" 转为 "empirical analysis of LLM evaluation assumptions"，类似 "Are LLMs classical test-takers? Evidence from IRT person-fit analysis" 的 empirical study framing。不降级目标。

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
  "promptId": "499b60cd-82e2-4a1c-90e1-b7957d2ac351",
  "type": "user",
  "uuid": "32656a7e-9780-438a-9035-adfca8c2a01e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:17:04.661Z_

```json
{
  "parentUuid": "32656a7e-9780-438a-9035-adfca8c2a01e",
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
  "uuid": "a21427af-9f33-45b8-b91b-0085306c6d92",
  "timestamp": "2026-05-20T19:17:04.661Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:17:04.662Z_

```json
{
  "parentUuid": "a21427af-9f33-45b8-b91b-0085306c6d92",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f8c6350a-983b-42da-b9ea-479d515cf4e5",
  "timestamp": "2026-05-20T19:17:04.662Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：ctrl-contam 仅在原始 pilot 条件（Qwen × MMLU）可复现，跨模型/benchmark 泛化失败；post-RL 信号消失；baselines 多数场景胜出 核心假设：['仅 1-2/4 模型在 MMLU 15% 下显著——SFT generalization 在多数模型上将 mem…",
  "leafUuid": "f8c6350a-983b-42da-b9ea-479d515cf4e5",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit LLM contamination detection worst-case characterization",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:18:19.421Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "worst" tier across all planned experiments in the experiment_plan. Let me carefully go through each planned experiment and generate worst-case predictions based on the worst tier definition.

Let me identify all planned experiments:

1. exp-ctrl-contam-pilot (planned) - Quick validation: Qwen3.5-9B × 4 conditions × MMLU
2. exp-ctrl-contam (planned) - Full controlled experiment: 4 models × 6 levels × 3 benchmarks
3. exp-leaderboard-audit (ABANDONED)


4. exp-natural-experiment (planned, P2-optional) - actually DONE
5. exp-v1-irt-refit-expanded (planned) - actually DONE
6. exp-4pl-ablation (planned) - actually DONE
7. exp-baseline-comparison (planned) - P0-end
8. exp-multiscale-lzm (planned)
9. exp-post-rl (planned)
10. exp-extra-benchmarks (planned)
11. exp-domain-analysis (planned) - actually DONE

I need to reconcile the experiment_plan with the registry since several experiments marked as planned have actually been completed. Let me cross-reference which ones are truly still pending versus already finished. Looking more carefully at the experiment_plan status field, I need to distinguish between what's marked as planned there versus what's actually completed in the registry. The pilot experiment shows as planned for Qwen3.5-9B even though the registry has results from the Qwen2.5-7B version, so there's a mismatch between the two sources I need to reconcile. I'm noticing there's a discrepancy between what the registry shows as completed and what the experiment_plan lists as planned, so I should trust the registry as the more authoritative source. Let me filter for just the experiments marked as planned in the experiment_plan and cross-reference with what's actually been executed.

For the worst-case tier predictions, I'm thinking about scenarios where the core findings don't generalize: the contamination effect only holds in the original pilot setup, the post-RL improvements vanish, baseline methods outperform across most conditions, and the memorization compression mechanisms fail to scale consistently across models. I'm looking at the metric ranges across the full spectrum of results, and the pattern is clear: theta-shift mechanisms persist even when detection fails, post-RL completely washes out the signal we're trying to measure, and the lz* approach only marginally outperforms standard baselines. The core insight is shifting how we frame this—moving away from contamination detection as the goal and instead treating it as a psychometric diagnostic tool that reveals fundamental limits in what binary classification can tell us about model behavior. Now I'm mapping out predictions for each planned experiment under worst-case conditions.

For the Qwen3.5-9B pilot, I expect weaker signal than what we saw with Qwen2.5-7B—the newer model likely has stronger SFT generalization and lower memorization rates, so Cohen's d probably lands around 1.0-1.5 instead of the 3.85 we observed before, making theta-shift harder to control but still detectable at the 15% contamination level.

The full four-model experiment in worst case probably only shows significance in one or two models, with Gemma and Llama potentially failing entirely, and only MMLU holding up as a reliable benchmark while GSM8K and HellaSwag collapse.

For the baseline comparison, lz* barely edges out at 5% contamination but gets dominated by machine learning baselines once we hit 10% and above. The multiscale aggregation doesn't rescue things because the per-benchmark signal is already too weak. Post-RL with GRPO is catastrophic—retention drops below 30% and wipes out the effect. The extra benchmarks like BBH and MATH fall into that 1K-10K range where statistical power is fundamentally limited, making them too noisy to be useful.

I should generate worst-case predictions for all the planned experiments the user listed, including the abandoned ones and the natural experiment variants.

Looking back at the experiment plan, I need to identify every experiment marked as planned status: the contamination pilots and full experiment, the leaderboard audit, the natural experiment, the IRT refit expansion, the 4PL ablation, and the multiscale LZM work. The user is asking for a thought experiment about what worst-tier outcomes would look like across the entire planned pipeline.

Now I'm working through the specific predictions for each experiment. Starting with the contamination pilot using Qwen3.5-9B on MMLU—in a worst-case scenario, the model's improved SFT generalization would mean much lower memorization rates compared to the earlier Qwen2.5-7B baseline, but the theta-shift effect would still be severe enough that even fixing theta wouldn't fully restore monotonicity, with Cohen's d around 1.2 instead of the previous 3.85.

For the broader contamination experiment across four models and multiple benchmarks, I'm expecting that only Qwen2.5-7B on MMLU would replicate the pilot results, while the larger models like Gemma-4-31B would show even stronger SFT generalization and fail to show the effect, and Mistral-7B would struggle across the board—leaving just one or two models showing significance, and only on MMLU while GSM8K and HellaSwag show no effect.

The leaderboard audit is already abandoned due to IRT refit issues. For the natural experiment with base-to-chat model pairs, I'm seeing systematic SFT effects in the registry results but no individual contamination signal, and in the worst-case scenario these effects are too noisy to be confident about. The IRT refit expansion with larger sample sizes still isn't rescuing the discrimination parameter, confirming that path is dead. The 4PL ablation is showing some advantage over the 3PL model in the worst tier.

Looking at the baseline comparison results, the lz* method barely edges out ML baselines at extreme low contamination levels, but ML approaches dominate once contamination reaches 10% or higher. ConStat with retest and Min-K%++ both substantially outperform lz*. The multiscale aggregation across benchmarks only provides marginal gains since the individual benchmark signals are already weak.

When applying GRPO after SFT contamination, the person-fit signal gets completely wiped out—retention drops below 30% and lz* becomes indistinguishable from the clean baseline, confirming Wang et al.'s findings apply here too. Testing on larger benchmarks like BBH and MATH reveals they fall into a power gap zone where contamination detection at 15% only achieves 0.3-0.5 AUROC, too unreliable for practical deployment.

Domain-level analysis on MMLU doesn't help either—even when Gemini shows 100% accuracy, the contamination pattern stays uniform across domains, so there's no differential signal to exploit for detection.

Now I'm compiling everything into the YAML format with detailed metrics and rationale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8c6350a-983b-42da-b9ea-479d515cf4e5",
  "isSidechain": false,
  "requestId": "req_011CbEMj2c2mj18fM3tWdqz4",
  "type": "assistant",
  "uuid": "45588441-b5d4-4f37-913b-603cb460c25f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kj1jTUL97Q3a12fN5iHVF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21209,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17130,
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
          "output_tokens": 17130,
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

_source line 9 · 2026-05-20T19:22:20.752Z_

```yaml
tier: worst
narrative_guidance: >
  核心 reframe：从 "contamination detection method" 转向 "psychometric diagnostics for LLM evaluation"。
  ctrl-contam 仅在原始 pilot 条件（Qwen2.5-7B × MMLU）可复现，跨模型/benchmark 泛化失败。
  三条 claims 重构——Claim 1 变为 IRT person-fit 为 LLM benchmark 评估提供 principled diagnostic 工具，
  pilot 成功 + full 失败共同量化了 binary-only detection 的 fundamental limits。
  Claim 2 保留 power function 理论贡献，增加 adjusted power after SFT generalization 的 empirical bound。
  Claim 3 重心转移到三个 standalone 发现：(a) universal 4PL misfit，(b) θ-shift mechanism，
  (c) memorization fraction 的跨模型异质性。仍冲 EMNLP，framing 转为 empirical study。

imagined_experiments:
  - name: "ctrl-contam-pilot (Qwen3.5-9B)"
    plan_id: "exp-ctrl-contam-pilot"
    description: >
      Qwen3.5-9B × MMLU × 4 conditions (0%-seed1, 0%-seed2, 15%, 50%)。
      测量 Δlz*、clean-vs-clean noise floor、memorization fraction、θ-shift。
    expected_results:
      H1_clean_delta_lz:
        clean_s1_lz: 5.2
        clean_s2_lz: 4.8
        delta: 0.4
        confirmed: true
        noise_floor_std: 0.9
      H2_contam_15_detection:
        delta_lz_free: -1.5
        cohens_d: -1.2
        p_value: 0.03
        confirmed: true  # borderline — significant but much weaker than Qwen2.5-7B
      H3_dose_response:
        theta_free:
          contam_15_delta: -1.5
          contam_50_delta: -0.3
          ratio: 0.20
          confirmed: false  # inverted, worse than Qwen2.5-7B
        theta_fixed:
          contam_15_delta: 1.8
          contam_50_delta: 3.2
          ratio: 1.78
          confirmed: true  # monotonic restored but ratio only ~1.8 (vs 2.93 for Qwen2.5-7B)
      H4_memorization_fraction:
        contam_15: 0.12
        contam_50: 0.09
        confirmed: false  # well below Qwen2.5-7B's 0.38
      theta_shift:
        clean_mean: -0.05
        contam_15: 0.35
        contam_50: 0.58
        note: "θ-shift 更剧烈——Qwen3.5 的 instruction tuning 使 θ 对 SFT 更敏感"
      accuracy:
        clean_s1: 0.72
        clean_s2: 0.72
        contam_15: 0.74
        contam_50: 0.76
        contam_15_seen: 0.78
        contam_15_unseen: 0.73
        seen_unseen_gap: 0.05  # much smaller than Qwen2.5-7B's 0.109
      seen_unseen_lz_gap_15pct: 0.8
    result_rationale: >
      Qwen3.5-9B 是更新一代的 instruction-tuned 模型，SFT generalization 更强：
      (1) memorization fraction 从 Qwen2.5-7B 的 0.38 压缩到 ~0.12——大部分注入的 benchmark items
      被泛化吸收为 general ability improvement 而非 rote memorization，导致 aberrant pattern 大幅减弱；
      (2) θ-shift 更剧烈 (0.35 vs 0.20 at 15%)，因为 Qwen3 系列的 instruction tuning 使模型对
      fine-tuning 信号更敏感，更多 signal 被 θ 提升吸收；
      (3) Cohen's d 从 3.85 降到 ~1.2——仍然统计显著但效应量大幅缩水，落入 worst 档的 [0.3, 1.5] 范围；
      (4) seen/unseen gap 缩小到 0.05 (vs 0.109)，因为 generalization 让 unseen items 也受益，
      模糊了 memorization fingerprint。Clean baseline 仍稳定 (H1 always holds)。
    tables:
      - name: "Table: Qwen3.5-9B Pilot Results"
        columns: [condition, accuracy, lz_star_free, lz_star_fixed, delta_lz_free, delta_lz_fixed, theta_mle]
        rows:
          - [clean-s1, 0.720, 5.2, 5.0, "—", "—", -0.05]
          - [clean-s2, 0.720, 4.8, 4.9, 0.4, 0.1, -0.04]
          - [contam-15, 0.740, 3.5, 6.8, -1.5, 1.8, 0.35]
          - [contam-50, 0.760, 4.7, 8.2, -0.3, 3.2, 0.58]
    figures_description:
      - "Fig: Dose-response under free-θ vs fixed-θ for Qwen3.5-9B。Free-θ 几乎 flat（无 dose-response），fixed-θ 恢复弱单调性但斜率远低于 Qwen2.5-7B。"
      - "Fig: Seen vs unseen accuracy gap 对比 Qwen2.5-7B vs Qwen3.5-9B，展示 generalization 压缩效应。"
    analysis: >
      Pilot 仍通过 go/no-go（p<0.05），但效应量不足以支撑 robust detection claim。
      这预示 full experiment 中多数模型将更弱。Memorization fraction 0.12 意味着
      理论 power 的 88% 被 SFT generalization 吃掉。Narrative 需转向：
      "pilot 成功量化了 SFT generalization 的 model-specific magnitude"。

  - name: "ctrl-contam-full (4 models × 3 benchmarks)"
    plan_id: "exp-ctrl-contam"
    description: >
      4 模型 (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3) ×
      6 contamination levels (0/5/10/15/25/50%) × 3 benchmarks (MMLU, GSM8K, HellaSwag)。
    expected_results:
      models_significant_at_15pct_mmlu: 2  # only Qwen3.5 and Llama
      models_significant_at_15pct_gsm8k: 0
      models_significant_at_15pct_hellaswag: 1  # only Qwen3.5, borderline
      benchmarks_significant_per_model:
        Qwen3.5-9B: 1  # only MMLU (HellaSwag borderline)
        Gemma-4-31B: 0  # fails everywhere
        Llama-3.1-8B: 1  # MMLU only
        Mistral-7B-v0.3: 0  # fails everywhere
      cohens_d_15pct:
        Qwen3.5_MMLU: 1.2
        Qwen3.5_GSM8K: 0.3
        Qwen3.5_HellaSwag: 0.5
        Gemma_MMLU: 0.2
        Gemma_GSM8K: 0.1
        Gemma_HellaSwag: 0.1
        Llama_MMLU: 0.8
        Llama_GSM8K: 0.2
        Llama_HellaSwag: 0.3
        Mistral_MMLU: 0.4
        Mistral_GSM8K: 0.1
        Mistral_HellaSwag: 0.15
      cohens_d_15pct_across_models_mmlu: 0.65  # mean across 4 models on MMLU
      cohens_d_15pct_min_model: 0.2  # Gemma
      memorization_fraction_15pct:
        Qwen3.5: 0.12
        Gemma: 0.06
        Llama: 0.15
        Mistral: 0.08
        mean: 0.10
      theta_fixed_dose_response_ratio:
        Qwen3.5: 1.78
        Gemma: 0.9  # nearly flat — θ-fixed doesn't help
        Llama: 1.5
        Mistral: 1.1
      seen_unseen_lz_gap_15pct:
        Qwen3.5: 0.8
        Gemma: 0.3
        Llama: 1.2
        Mistral: 0.5
      gsm8k_overall_note: "GSM8K (1319 items) power 理论上限 ~59% at 15%，实际 SFT generalization 进一步压低。所有模型 fail。"
      hellaswag_overall_note: "HellaSwag (10042 items) 理论 power 足够，但 acc_norm 的 binary coding 增加噪音，仅 Qwen borderline。"
    result_rationale: >
      跨模型泛化失败的三重原因：
      (1) SFT generalization heterogeneity——不同模型架构对 QLoRA SFT 的 memorization/generalization
      比率差异巨大。Gemma-4-31B 作为 31B 参数模型，LoRA rank 相对于模型容量极小，
      注入的 benchmark items 几乎全部被泛化（memorization fraction ~6%），aberrant pattern 消失；
      Mistral-7B-v0.3 虽然参数量与 Qwen 相当，但其 tokenizer 和 attention 架构差异导致
      fine-tuning dynamics 不同，memorization fraction 也仅 ~8%。
      (2) θ-shift 在部分模型不可控——Gemma 的 θ-fixed 也无法恢复 dose-response (ratio=0.9)，
      因为该模型的 θ 估计本身就不稳定（pre-contamination θ 的 bootstrap CI 很宽）。
      (3) 跨 benchmark 泛化失败——GSM8K 仅 1319 items，理论 power 天花板 ~59%，
      乘以 memorization fraction <15% 后实际 power <10%。HellaSwag 虽有足够 items
      但 acc_norm binary coding 引入额外噪音。仅 MMLU (14042 items) 在最佳模型上勉强工作。
      这些结果共同说明：binary-only detection 在 "model-specific SFT generalization + benchmark size"
      的双重约束下触及了 fundamental limit。
    tables:
      - name: "Table: Cohen's d at 15% Contamination (model × benchmark)"
        columns: [Model, MMLU, GSM8K, HellaSwag, Significant_cells]
        rows:
          - [Qwen3.5-9B, "1.20*", 0.30, "0.50†", "1 (2†)"]
          - [Gemma-4-31B, 0.20, 0.10, 0.10, 0]
          - [Llama-3.1-8B, "0.80*", 0.20, 0.30, 1]
          - [Mistral-7B-v0.3, 0.40, 0.10, 0.15, 0]
        notes: "* p<0.05; † p<0.10 borderline。仅 2/12 cells 达到 significance。"
      - name: "Table: Memorization Fraction at 15% (model × benchmark)"
        columns: [Model, MMLU, GSM8K, HellaSwag]
        rows:
          - [Qwen3.5-9B, 0.12, 0.08, 0.10]
          - [Gemma-4-31B, 0.06, 0.04, 0.05]
          - [Llama-3.1-8B, 0.15, 0.10, 0.12]
          - [Mistral-7B-v0.3, 0.08, 0.05, 0.07]
      - name: "Table: θ-fixed Dose-Response Ratio (contam_50/contam_15)"
        columns: [Model, MMLU, GSM8K, HellaSwag]
        rows:
          - [Qwen3.5-9B, 1.78, 1.2, 1.4]
          - [Gemma-4-31B, 0.9, 0.8, 0.85]
          - [Llama-3.1-8B, 1.5, 1.1, 1.3]
          - [Mistral-7B-v0.3, 1.1, 0.9, 0.95]
    figures_description:
      - "Fig: Heatmap of Cohen's d across 4 models × 3 benchmarks × 6 contamination levels。仅左上角 (Qwen/Llama × MMLU) 有深色 (|d|>0.5)，其余区域浅色。"
      - "Fig: Memorization fraction 跨模型柱状图，展示 Gemma (31B) 极低、Llama 最高的异质性。"
      - "Fig: Adjusted power = theoretical power × memorization fraction，对比 theoretical upper bound，展示 SFT generalization gap。"
    analysis: >
      仅 2/4 模型在 MMLU 15% 显著，0/4 在 GSM8K 显著，0-1/4 在 HellaSwag 显著。
      总计 2-3/12 cells significant。跨模型平均 Cohen's d = 0.65 (MMLU)，远低于 pilot 的 3.85。
      核心发现从 "detection works" 转变为 "SFT generalization 的跨模型异质性是 binary detection 的根本瓶颈"。
      Gemma-31B 的 memorization fraction ~6% 最具理论价值——大模型几乎完全 generalize SFT injection。

  - name: "leaderboard-audit (v1 大规模扫描)"
    plan_id: "exp-leaderboard-audit"
    description: >
      Open LLM Leaderboard v1 全模型 person-fit 扫描。已因 IRT refit 失败而 ABANDONED。
    expected_results:
      status: ABANDONED
      reason: "a_r=0.127 (N=178 expanded refit) 远低于 0.2 阈值，lz* 退化为 accuracy-like metric"
      hypothetical_if_forced:
        n_models_scanned: 5000
        flagged_rate: ">95%"
        discrimination: "near-zero — flags are accuracy artifacts, not person-fit anomalies"
    result_rationale: >
      D011 已确认 Path D dead：MML-EM classical refit 在 N=178 时 a_r=0.127，
      discrimination 完全失败。即使扩展到 N=500+，exp-v1-irt-refit-expanded 预测
      a_r 仍 <0.2。没有有效的 item discrimination，lz* 退化为 accuracy z-score 的
      近似等价物，13K+ 模型的 audit 只会产生 meaningless flags。
      在 worst 档下这一结论不变——它是 data limitation 而非 tier-dependent。
    tables: []
    figures_description: []
    analysis: >
      保持 ABANDONED。数据可用性 (13K+ models with per-item responses) 写入 Discussion/Future Work，
      作为 "when neural IRT estimation matures" 的 roadmap。

  - name: "natural-experiment (base→chat pairs)"
    plan_id: "exp-natural-experiment"
    description: >
      v1 leaderboard 上 21 个 base→chat model pairs，计算 Δlz* 作为 SFT 效应代理。
    expected_results:
      n_pairs: 21
      n_complete_pairs: 9
      significant_benchmarks: 1  # only HellaSwag (GSM8K becomes borderline)
      HellaSwag:
        mean_deviation: -2.8
        t_stat: -2.5
        p_value: 0.025
      GSM8K:
        mean_deviation: 2.1
        t_stat: 1.9
        p_value: 0.08  # borderline, not significant after correction
      MMLU:
        p_value: 0.35
      ARC_C:
        p_value: 0.55
      individual_contamination_outliers: 0
      note: "a_r=0.127 使 lz* ≈ accuracy-like，systematic SFT effects 是 accuracy shifts 而非 genuine person-fit anomalies"
    result_rationale: >
      在 worst 档下，v1 IRT refit 的 discrimination failure (a_r=0.127) 使这个实验
      的理论基础更弱：lz* 几乎退化为 accuracy z-score，systematic effects 反映的是
      SFT 带来的 accuracy shift 而非 person-fit 层面的 response pattern 变化。
      仅 9 个 complete pairs 的小样本进一步限制了统计检验能力。
      GSM8K 的 p 从 registry 的 0.009 上调到 0.08（worst 档假设 pairs 间 variance 更大），
      only HellaSwag survives。不产生 individual contamination outlier。
      P2-optional 优先级合理——这些结果不能支撑任何主要 claim。
    tables:
      - name: "Table: Base→Chat Paired t-test Results"
        columns: [Benchmark, n_pairs, mean_Δlz, t_stat, p_value, significant]
        rows:
          - [HellaSwag, 9, -2.8, -2.5, 0.025, "Yes"]
          - [GSM8K, 9, 2.1, 1.9, 0.08, "No†"]
          - [MMLU, 9, 1.5, 1.0, 0.35, "No"]
          - [ARC-C, 9, 0.8, 0.6, 0.55, "No"]
    figures_description:
      - "Fig: Paired Δlz* dot plot per benchmark，展示 HellaSwag 的 systematic negative shift 和其余 benchmark 的散乱分布。"
    analysis: >
      降级为 supplementary material 或 1-2 句 mention。在 worst 档叙事下，
      这个实验仅能说明 "SFT systematically shifts some benchmark scores"，
      不具备 contamination detection 的解释力。

  - name: "v1-irt-refit-expanded (N≥500)"
    plan_id: "exp-v1-irt-refit-expanded"
    description: >
      扩大 v1 IRT refit 样本量至 N=178+，验证 discrimination failure 是否因样本量不足。
    expected_results:
      n_models_downloaded: 178
      n_items: 14042
      3pl_a_pearson_r: 0.13
      2pl_a_pearson_r: -0.03
      3pl_b_pearson_r: 0.66
      conclusion: "Path D dead — a_r < 0.2 threshold"
      note: "N=178 已是 v1 可用模型的上限（更多模型数据已删除或格式不兼容）"
    result_rationale: >
      Classical MML-EM estimation 的 discrimination 参数 a 需要 response pattern 中的
      sufficient variation 来区分 high-a vs low-a items。在 LLM 场景下，模型间 response
      pattern 的 correlation structure 与 human examinees 根本不同——LLM 的 "ability" 是
      高度多维的（不同 domain 的表现由不同 capability 驱动），违反了 IRT 的 unidimensionality
      假设。N=178 时 a_r=0.127 不是样本量问题，而是 model violation：classical IRT 的
      unidimensional assumption 在 LLM data 上 fundamentally fails for discrimination
      estimation（尽管 difficulty b 的 rank-order 得以保留，因为 b 只需要 item-level
      marginal difficulty，对 dimensionality 假设依赖较弱）。
      Worst 档下这个负结果是确定性的——不依赖 tier。
    tables:
      - name: "Table: IRT Refit Parameter Recovery"
        columns: [Method, a_pearson_r, b_pearson_r, a_threshold, verdict]
        rows:
          - [3PL (N=63), 0.111, 0.626, ">0.4 viable", FAIL]
          - [3PL (N=178), 0.127, 0.663, ">0.4 viable", FAIL]
          - [2PL (N=63), -0.084, 0.572, ">0.4 viable", FAIL]
          - [2PL (N=178), -0.029, 0.663, ">0.4 viable", FAIL]
    figures_description:
      - "Fig: a_r recovery vs sample size (N=63 → N=178)，近乎 flat，表明不是 sample size 问题。"
    analysis: >
      最终关闭 Path D。在论文中作为 methodological caveat：classical IRT estimation
      需要 unidimensional response patterns，LLM data 违反此假设。
      这本身是 Claim 3 的一个发现：IRT parameter estimation challenges in LLM contexts。

  - name: "4pl-ablation (4PL vs 3PL detection)"
    plan_id: "exp-4pl-ablation"
    description: >
      4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。
    expected_results:
      simulation_results:
        far_4pl: 0.05
        far_3pl: "4.7-16.5%"
        far_2pl: "50-100%"
        mean_power_gain_4pl_vs_3pl:
          MMLU: "+27pp"
          HellaSwag: "+26pp"
          GSM8K: "+20pp"
        key: "4PL essential — these results hold regardless of tier"
      ctrl_contam_impact:
        note: "在 worst 档的 ctrl-contam 中，4PL 优势仍在但 absolute power 太低"
        Qwen_MMLU_4pl_d15: 1.2  # Cohen's d with 4PL
        Qwen_MMLU_3pl_d15: 0.5  # Cohen's d with 3PL — even worse
        Gemma_MMLU_4pl_d15: 0.2
        Gemma_MMLU_3pl_d15: 0.08
        interpretation: "4PL 比 3PL 好 2x，但 worst 档下 2 × 'bad' 仍是 'bad'"
    result_rationale: >
      4PL ablation 的 simulation 结果是 tier-independent（不依赖 ctrl-contam），
      已在 registry 中确认。在 worst 档下新增的信息是：将 ablation 结果与 ctrl-contam 的
      weak real-data signal 结合——4PL 相对 3PL 的 advantage ratio (~2x power) 仍然成立，
      但当 4PL 本身的 Cohen's d 仅 0.2-1.2 时，3PL 的 0.08-0.5 不过是从 "borderline" 降到 "useless"。
      这加强了论文的 methodological contribution：即使使用了正确的 IRT model (4PL)，
      SFT generalization 仍是 binding constraint。
    tables:
      - name: "Table: 4PL vs 3PL Detection on ctrl-contam (worst tier)"
        columns: [Model, Benchmark, "d_4PL", "d_3PL", "Ratio"]
        rows:
          - [Qwen3.5, MMLU, 1.20, 0.50, "2.4×"]
          - [Llama-3.1, MMLU, 0.80, 0.35, "2.3×"]
          - [Gemma-4, MMLU, 0.20, 0.08, "2.5×"]
          - [Mistral, MMLU, 0.40, 0.18, "2.2×"]
    figures_description:
      - "Fig: Power gain heatmap (4PL − 3PL) across simulation benchmarks，同 registry。"
      - "Fig: Real-data Cohen's d under 4PL vs 3PL for ctrl-contam models。"
    analysis: >
      4PL 的 methodological necessity 是 tier-independent 结论。在 worst 档下额外的 takeaway 是：
      "correct IRT model is necessary but not sufficient——SFT generalization is the binding bottleneck。"

  - name: "baseline-comparison (≥5 baselines)"
    plan_id: "exp-baseline-comparison"
    description: >
      在 ctrl-contam ground-truth 模型上比较 lz* vs ConStat, Min-K%++, accuracy z-score,
      PPL-based detection, random baseline 的 AUROC 和 Type-I error。
    expected_results:
      auroc_at_5pct_contamination:
        lz_star: 0.57
        accuracy_zscore: 0.54
        ppl_based: 0.62
        min_k_pp: 0.68
        constat: 0.72
        random: 0.50
        lr_binary_vector: 0.52
        rf_binary_vector: 0.53
      auroc_at_10pct_contamination:
        lz_star: 0.62
        accuracy_zscore: 0.59
        ppl_based: 0.71
        min_k_pp: 0.76
        constat: 0.80
        random: 0.50
        lr_binary_vector: 0.61
        rf_binary_vector: 0.63
      auroc_at_15pct_contamination:
        lz_star: 0.66
        accuracy_zscore: 0.63
        ppl_based: 0.78
        min_k_pp: 0.82
        constat: 0.86
        random: 0.50
      auroc_at_25pct_contamination:
        lz_star: 0.72
        accuracy_zscore: 0.70
        ppl_based: 0.85
        min_k_pp: 0.89
        constat: 0.92
        random: 0.50
      lz_star_minus_best_baseline_auroc_5pct: -0.15  # constat wins by 0.15
      lz_star_minus_best_baseline_auroc_10pct: -0.18
      lz_star_vs_ml_binary_at_5pct: "+0.04"  # tiny advantage over same-info baselines
      lz_star_vs_ml_binary_at_10pct: "+0.01"  # advantage disappears
      bootstrap_ci_width_lz_auroc: 0.12  # wide CIs due to few models
      type_i_error:
        lz_star: 0.06
        constat: 0.04
        min_k_pp: 0.05
      note: "lz* 仅在 same-information-level baselines (accuracy z, binary ML) 中有微弱优势；所有 privileged-access methods 大幅胜出"
    result_rationale: >
      Worst 档下 lz* 在 ctrl-contam 中 AUROC 极低的根源是 memorization fraction：
      当平均 memorization fraction 仅 ~10% 时，15% 注入中只有 ~1.5% 的 items 产生
      真正的 aberrant signal，远不足以在 AUROC 上与利用 token-level 信息的方法竞争。
      具体地：
      (1) Min-K%++ 和 PPL-based 方法直接观察 token probability distributions，
      信息量远超 binary response——在 worst 档下它们仍有 0.68-0.76 AUROC at 5%；
      (2) ConStat 通过 rephrased re-test 获得额外信号（contaminated model 对 rephrased
      items 表现下降），信息量介于 binary 和 token-level 之间，在所有 levels 最优；
      (3) lz* 对 same-information-level baselines (accuracy z-score, binary ML classifiers)
      仅有 ~0.03-0.05 AUROC 优势（IRT structure 作为 inductive bias 的贡献），
      且这一优势在 10% 以上消失；
      (4) 宽 bootstrap CIs (~0.12) 反映了 ctrl-contam 中模型数量少 (4 models) 的限制。
      这些结果 precisely quantify "binary-only detection 的代价"——对应论文 reframe。
    tables:
      - name: "Table: AUROC Comparison Across Methods and Contamination Levels"
        columns: [Method, Info_Level, "5%", "10%", "15%", "25%"]
        rows:
          - ["lz*", binary, "0.57±0.06", "0.62±0.06", "0.66±0.05", "0.72±0.05"]
          - [acc_zscore, binary, "0.54±0.07", "0.59±0.06", "0.63±0.06", "0.70±0.05"]
          - [LR_binary, binary, "0.52±0.08", "0.61±0.07", "0.67±0.06", "0.76±0.05"]
          - [PPL, token_prob, "0.62±0.05", "0.71±0.05", "0.78±0.04", "0.85±0.04"]
          - ["Min-K%++", token_prob, "0.68±0.05", "0.76±0.04", "0.82±0.04", "0.89±0.03"]
          - [ConStat, retest, "0.72±0.04", "0.80±0.04", "0.86±0.03", "0.92±0.03"]
          - [Random, "—", 0.50, 0.50, 0.50, 0.50]
      - name: "Table: lz* Advantage Over Same-Info Baselines"
        columns: [Contamination, "lz*−acc_z", "lz*−LR_binary", "lz*−best_privileged"]
        rows:
          - ["5%", "+0.03", "+0.05", "−0.15"]
          - ["10%", "+0.03", "+0.01", "−0.18"]
          - ["15%", "+0.03", "−0.01", "−0.20"]
          - ["25%", "+0.02", "−0.04", "−0.20"]
    figures_description:
      - "Fig: AUROC curves (contamination level × AUROC) for all methods，按 information level 分色。Binary methods 聚集在底部，privileged methods 在顶部。"
      - "Fig: Detection frontier diagram — x 轴为 information access level (binary → retest → token_prob → logits → weights)，y 轴为 AUROC at 15%。lz* 标定了 binary endpoint。"
    analysis: >
      Baseline comparison 在 worst 档下产出论文的核心 reframe 证据：
      lz* 精确标定了 "binary-only detection frontier" 的位置。
      在 same-information baselines 中 lz* 有微弱优势 (IRT inductive bias)，
      但 absolute AUROC < 0.65 at practical levels (5-10%) 无实用价值。
      Privileged methods 大幅胜出证实了 information gap 是根本原因，不是方法缺陷。
      这支撑了 narrative："我们 precisely quantify 了 binary-only detection 的天花板"。

  - name: "multiscale-lzm (cross-benchmark aggregation)"
    plan_id: "exp-multiscale-lzm"
    description: >
      实现 Hong, Lin & Cheng (2021) 的 multiscale lzm 统计量，
      跨 benchmark 聚合标准化 lz* 总分。
    expected_results:
      psn_irt_12_models:
        flagged_before_lzm: "57/60 cells (per-cell lz*)"
        flagged_after_lzm: "12/12 models (aggregate)"
        note: "所有模型都被 flag——universal misfit 下 aggregation 无区分力"
      ctrl_contam:
        lzm_clean_vs_contam_15:
          Qwen3.5: {clean_lzm: 8.5, contam_lzm: 6.2, delta: -2.3}
          Gemma: {clean_lzm: 3.1, contam_lzm: 2.7, delta: -0.4}
          Llama: {clean_lzm: 6.8, contam_lzm: 5.0, delta: -1.8}
          Mistral: {clean_lzm: 5.2, contam_lzm: 4.5, delta: -0.7}
        improvement_over_per_benchmark: "+5-10% relative detection improvement"
        note: "marginal gain — aggregation 无法弥补 per-benchmark signal weakness"
      power_boost_assessment: "insufficient to change any model from non-significant to significant"
    result_rationale: >
      Multiscale lzm 通过 √(Σ(lz*_j²) / J) 聚合 J 个 benchmark 的 person-fit。
      在 worst 档下，per-benchmark signal 已经极弱（多数 cells d<0.5），
      聚合 3 个弱信号的改善有限（~√3 ≈ 1.7× 提升），不足以将 non-significant
      cells 翻转为 significant。
      在 PSN-IRT 12 模型上，universal misfit 意味着所有模型的 lzm 都极端，
      aggregation 不增加区分力——从 "all flagged per-cell" 到 "all flagged aggregate"。
      唯一的 mild positive：在 ctrl-contam 的 Qwen 和 Llama 上，lzm 提供了
      slightly better separation，但 absolute effect 仍弱。
    tables:
      - name: "Table: lzm Aggregation Results on ctrl-contam"
        columns: [Model, clean_lzm, contam_15_lzm, delta_lzm, "Improvement vs best per-benchmark"]
        rows:
          - [Qwen3.5, 8.5, 6.2, -2.3, "+8%"]
          - [Gemma-4, 3.1, 2.7, -0.4, "+5%"]
          - [Llama-3.1, 6.8, 5.0, -1.8, "+10%"]
          - [Mistral, 5.2, 4.5, -0.7, "+6%"]
    figures_description:
      - "Fig: Per-benchmark lz* vs aggregated lzm for ctrl-contam models，展示 aggregation 的 marginal improvement。"
    analysis: >
      P2 优先级合理。在 worst 档下 lzm 不改变任何主要结论。
      可作为 1 段 methodological extension 写入论文，但不应成为 contribution。

  - name: "post-rl (GRPO after SFT contamination)"
    plan_id: "exp-post-rl"
    description: >
      在 Qwen3.5-9B 上先 SFT 注入 15%/50% contamination，再 GRPO 训练，
      测试 person-fit signal 是否在 RL 后保持。
    expected_results:
      pre_rl_cohens_d_15pct: 1.2  # from ctrl-contam-pilot worst
      post_rl_cohens_d_15pct: 0.15
      post_rl_signal_retention: 0.12  # 12% of pre-RL signal retained
      pre_rl_cohens_d_50pct: 0.8
      post_rl_cohens_d_50pct: 0.10
      post_rl_delta_lz_15pct: -0.2  # essentially noise
      post_rl_delta_lz_50pct: -0.1
      post_rl_accuracy:
        contam_15_pre_rl: 0.74
        contam_15_post_rl: 0.75  # slight improvement from RL
        contam_50_pre_rl: 0.76
        contam_50_post_rl: 0.77
      post_rl_seen_unseen_gap:
        contam_15: 0.01  # gap eliminated
        contam_50: 0.005
      post_rl_memorization_fraction:
        contam_15: 0.02  # virtually zero
        contam_50: 0.01
      post_rl_theta_shift:
        contam_15: 0.42  # θ continues to rise from RL
        contam_50: 0.65
      p_value_15pct_post_rl: 0.45  # not significant
      p_value_50pct_post_rl: 0.52  # not significant
    result_rationale: >
      GRPO (Group Relative Policy Optimization) 在 SFT 之后进一步 smooth-out
      response patterns 的机制：
      (1) RL 的 reward signal 基于 correctness/helpfulness，不区分 seen vs unseen items，
      因此 RL gradient 将 memorized 和 generalized performance 统一优化，
      消除了 SFT 阶段产生的 seen/unseen 不一致性；
      (2) RL 的 KL penalty (against SFT checkpoint) 有限——GRPO 允许 policy 偏离 SFT
      baseline 数百步，足以 overwrite SFT 阶段的 item-specific memorization patterns；
      (3) θ 在 RL 后继续上升 (0.35→0.42 at 15%)，因为 RL 提升了 overall reasoning
      ability，进一步将 contamination signal 吸收为 ability improvement；
      (4) memorization fraction 从 0.12 降到 0.02——RL 将 rote memorization 转化为
      generalized capability，与 Wang et al. (2025) 的 MIA 失效机制完全一致。
      在 worst 档下 signal retention <30% (实际 ~12%)，person-fit 与 MIA 方法
      在 post-RL 场景下同样失效——这否定了 "structural immunity to RL" 的 narrative。
    tables:
      - name: "Table: Post-RL Signal Retention"
        columns: [Condition, "Pre-RL d", "Post-RL d", Retention, p_post_rl]
        rows:
          - [contam_15, 1.20, 0.15, "12.5%", 0.45]
          - [contam_50, 0.80, 0.10, "12.5%", 0.52]
      - name: "Table: Post-RL Memorization Fraction"
        columns: [Condition, "Pre-RL mem_frac", "Post-RL mem_frac", "Reduction"]
        rows:
          - [contam_15, 0.12, 0.02, "83%"]
          - [contam_50, 0.09, 0.01, "89%"]
    figures_description:
      - "Fig: Pre-RL vs Post-RL lz* distributions for contam_15/50。Post-RL distributions collapse onto clean baseline。"
      - "Fig: Seen/unseen accuracy gap before and after RL——RL 消除了 gap。"
    analysis: >
      Post-RL signal 完全消失，与 Wang et al. (2025) 的 MIA 结论一致。
      这否定了 paper_framing 中 "structurally immune to RL-induced distributional shifts" 的叙事。
      Worst 档下必须诚实报告：person-fit 在 post-RL 场景下与其他方法同样失效。
      Reframe 为：RL 不仅改变 token distribution (killing MIA) 而且改变 response patterns
      (killing person-fit)——这量化了 RL 对所有 behavior-level detection 的 fundamental limit。

  - name: "extra-benchmarks (BBH, MATH)"
    plan_id: "exp-extra-benchmarks"
    description: >
      添加 BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。
    expected_results:
      bbh:
        n_items: 6511
        theoretical_power_15pct: 0.42
        adjusted_power_15pct: 0.05  # ×0.12 memorization fraction
        ctrl_contam_cohens_d_15pct:
          best_model: 0.4
          worst_model: 0.1
        note: "BBH 的 multi-step reasoning format 使 SFT memorization 更难——model 学到的是 reasoning pattern 而非 specific answers"
      math:
        n_items: 5000
        theoretical_power_15pct: 0.35
        adjusted_power_15pct: 0.04  # ×0.10 memorization fraction
        ctrl_contam_cohens_d_15pct:
          best_model: 0.3
          worst_model: 0.05
        note: "MATH 需要 step-by-step reasoning，binary coding (correct/incorrect) 丢失了中间步骤信息"
      psn_irt_4pl_availability: "PSN-IRT 不包含 BBH/MATH 参数，需自行校准"
      calibration_challenge: "需要至少 N=100 models 的 per-item response data for reliable 4PL estimation"
      power_gap_filled: false  # 理论上填充了，但 adjusted power 太低
    result_rationale: >
      BBH (6511 items) 和 MATH (5000 items) 的 theoretical power at 15% 分别约 42% 和 35%
      (基于 exp-power-theory 的 power function，min_items_15pct_80power=7958)。
      但在 worst 档下，memorization fraction ~10-12% 将 adjusted power 压到 <5%，
      远低于任何实用阈值。
      更根本的问题：
      (1) BBH 和 MATH 都是 reasoning-heavy benchmarks，SFT 注入的 items 更容易被
      泛化为 reasoning improvement 而非 item-specific memorization；
      (2) 4PL 参数不可用——PSN-IRT 仅覆盖 MMLU/HellaSwag/GSM8K/ARC-C/HumanEval，
      需要自行校准，而 v1-irt-refit-expanded 已证明 classical estimation 失败；
      (3) 即使使用 PSN-IRT 的 neural IRT 方法，BBH/MATH 的训练数据可能不足以
      得到高质量参数。
      在 worst 档下这两个 benchmark 不增加检测实用性，仅验证了 power function 的
      theoretical predictions 在更多 benchmark 上成立。
    tables:
      - name: "Table: Power Analysis for Extended Benchmarks"
        columns: [Benchmark, n_items, "Theory Power @15%", "Mem Fraction", "Adjusted Power @15%"]
        rows:
          - [MMLU, 14042, 0.98, 0.12, 0.12]
          - [HellaSwag, 10042, 0.75, 0.10, 0.075]
          - [BBH, 6511, 0.42, 0.10, 0.042]
          - [MATH, 5000, 0.35, 0.08, 0.028]
          - [GSM8K, 1319, 0.59, 0.08, 0.047]
    figures_description:
      - "Fig: Power curve (n_items × adjusted power) at 15% contamination，包含所有 benchmarks。BBH 和 MATH 位于 curve 的低 power 区域。"
    analysis: >
      在 worst 档下 BBH/MATH 仅提供 power function validation 的额外数据点，
      不改变检测结论。如果 4PL 参数不可用，GPU 成本 (~10 hrs) 的 ROI 极低。
      建议降级为 supplementary 或完全省略。

  - name: "domain-analysis (MMLU subject-level)"
    plan_id: "exp-domain-analysis"
    description: >
      按 MMLU subject category 分别计算 person-fit，识别 ctrl-contam 模型的
      domain-specific contamination pattern。
    expected_results:
      ctrl_contam_qwen_15pct:
        STEM_lz: 1.8
        Humanities_lz: 1.5
        Social_Sciences_lz: 1.2
        Other_lz: 1.0
        pattern: "uniform — no domain concentration"
        note: "QLoRA SFT 注入随机采样 15% items，各 domain 均匀分布"
      ctrl_contam_qwen_50pct:
        STEM_lz: 3.5
        Humanities_lz: 3.0
        Social_Sciences_lz: 2.8
        Other_lz: 2.5
        pattern: "uniform — scaled up"
      domain_differential_detection: false  # no domain shows differential signal
      per_subject_power:
        mean_items_per_subject: 246  # 14042/57 subjects
        subjects_with_significant_delta: 3  # out of 57, at 15% contam
        note: "per-subject n too small for reliable detection"
      gemini_mmlu_replication:
        all_subjects_flagged: true
        pattern: "uniform 100% accuracy across domains — consistent with registry"
    result_rationale: >
      Domain analysis 在 worst 档下不产出有用的 differential signal，原因：
      (1) ctrl-contam 的 SFT injection 是 random sampling，不模拟 domain-specific
      contamination，因此各 domain 的 contamination ratio 和 lz* shift 近似均匀；
      (2) 即使某些 domain 有 differential signal（如 STEM 稍高），每个 subject
      平均仅 ~246 items，power 极低 (theoretical power @15% for 246 items ≈ 0.06)；
      (3) Gemini 的 100% accuracy 不产生 domain 差异（everywhere lz* >> 0）。
      在 worst 档下这个实验仅确认 "random injection → uniform pattern"，
      不增加检测洞见。对 PSN-IRT 12 模型的 domain 分析复制 registry 结果即可。
    tables:
      - name: "Table: Domain-level lz* for ctrl-contam Qwen3.5 at 15%"
        columns: [Domain, n_items, "clean lz*", "contam lz*", "Δlz*", p_value]
        rows:
          - [STEM, 4006, 2.1, 1.8, -0.3, 0.35]
          - [Humanities, 3547, 1.8, 1.5, -0.3, 0.40]
          - [Social Sciences, 3682, 1.6, 1.2, -0.4, 0.30]
          - [Other, 2807, 1.4, 1.0, -0.4, 0.32]
    figures_description:
      - "Fig: Domain-level Δlz* 柱状图，error bars 展示 bootstrap CIs，所有 domain 的 CIs 重叠。"
    analysis: >
      Domain analysis 在 worst 档下作为 supplementary validation，确认 random injection
      产生 uniform pattern。不作为独立 contribution。可合并到 ctrl-contam 结果的 1 段 subanalysis。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45588441-b5d4-4f37-913b-603cb460c25f",
  "isSidechain": false,
  "requestId": "req_011CbEMj2c2mj18fM3tWdqz4",
  "type": "assistant",
  "uuid": "99aaa603-4bd8-4a93-81a9-77b537a21d10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kj1jTUL97Q3a12fN5iHVF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21209,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17130,
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
          "output_tokens": 17130,
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：ctrl-contam 仅在原始 pilot 条件（Qwen × MMLU）可复现，跨模型/benchmark 泛化失败；post-RL 信号消失；baselines 多数场景胜出 核心假设：['仅 1-2/4 模型在 MMLU 15% 下显著——SFT generalization 在多数模型上将 mem…",
  "leafUuid": "99aaa603-4bd8-4a93-81a9-77b537a21d10",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit LLM contamination detection worst-case characterization",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：ctrl-contam 仅在原始 pilot 条件（Qwen × MMLU）可复现，跨模型/benchmark 泛化失败；post-RL 信号消失；baselines 多数场景胜出 核心假设：['仅 1-2/4 模型在 MMLU 15% 下显著——SFT generalization 在多数模型上将 mem…",
  "leafUuid": "99aaa603-4bd8-4a93-81a9-77b537a21d10",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit LLM contamination detection worst-case characterization",
  "sessionId": "da95c0ff-ced2-4e03-b8c9-deac6714a1b8"
}
```

---
