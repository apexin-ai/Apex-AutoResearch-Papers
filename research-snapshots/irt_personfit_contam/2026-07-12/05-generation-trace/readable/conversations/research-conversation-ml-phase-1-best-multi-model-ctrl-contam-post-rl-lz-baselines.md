# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Multi-model ctrl-contam 全面成功 + post-RL 信号存活 + lz* 在低污染率胜出所有 baselines 核心假设：[

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/f2b2a593-b75c-4715-93ab-89b246ef4019.jsonl`
- **Structured JSON:** [`fe5022a5cbac237f4da5.json`](../../sessions/fe/fe5022a5cbac237f4da5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:04:25.012Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:04:25.012Z",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Multi-model ctrl-contam 全面成功 + post-RL 信号存活 + lz* 在低污染率胜出所有 baselines\n核心假设：['SFT memorization fingerprint跨模型家族一致：4/4 模型在 15% 污染下均产生显著 Δlz*', 'θ-fixed 策略普适：所有模型均可通过固定 θ 恢复单调 dose-response', 'Post-RL 不破坏 binary response 层面的记忆痕迹（GRPO 后 Δlz* 保留 ≥70%）', '小 benchmark（GSM8K ~1.3K items）在 ctrl-contam 中仍产生可检测信号（|d| > 0.8）', 'lz* 在 5-10% 低污染率下 AUROC 持续优于所有 supervised baselines']\n关键指标范围：{'cohens_d_15pct_across_models': [2.0, 5.0], 'cohens_d_15pct_min_model': [1.5, 3.0], 'models_significant_at_15pct': [4, 4], 'benchmarks_significant_per_model': [2, 3], 'memorization_fraction_15pct': [0.3, 0.5], 'theta_fixed_dose_response_ratio': [2.5, 4.0], 'post_rl_signal_retention': [0.7, 1.0], 'lz_star_auroc_5pct': [0.7, 0.85], 'lz_star_auroc_10pct': [0.8, 0.92], 'lz_star_minus_best_baseline_auroc_5pct': [0.0, 0.15], 'seen_unseen_lz_gap_15pct': [2.5, 5.0]}\n叙事方向：原始 framing 完全成立。IRT-FIT 是 minimal-information operating point 上的有效检测框架： 跨 4 个模型家族一致检测、post-RL robust、在实际关键的低污染率下无需标注数据即胜过 supervised baselines。 三条 claims 无需调整——Claim 1 的 \"principled framework\" 有 ctrl-contam 全面验证， Claim 2 的 power function 有 multi-benchmark 实证确认，Claim 3 的 empirical findings 加入 ctrl-contam 的跨模型 memorization 量化。θ-shift 作为 methodological contribution 而非 limitation。 Headline: \"binary response patterns alone detect SFT contamination across model families, even after RL post-training.\"\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_personfit_contam\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct) validate the framework on real models: at 15% contamination, |Cohen's d|=3.85 with clear seen/unseen memorization fingerprint (seen lz*≈0 vs unseen=3.1). θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity degrades at high contamination (50%), but fixing θ to pre-contamination baseline restores monotonic dose-response (ratio=2.93). The memorization fraction (~38% at 15% contamination) quantifies the SFT generalization effect — the gap between theoretical power and actual detection signal.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+34.75, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.\n6. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n7. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×2 seeds, 15%, 50%). Key results: (a) contam_15 |Cohen's d|=3.85 (strong detection signal); (b) free-θ dose-response non-monotonic (contam_50 Δlz*=1.53 < contam_15 Δlz*=3.97) due to θ-shift confound; (c) **θ-fixed analysis restores monotonicity** (Δlz*_fixed: contam_15=+2.96, contam_50=+8.67, ratio=2.93); (d) seen/unseen split: contam_15 seen lz*≈0 vs unseen=3.1 (clear memorization fingerprint); (e) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-two-sided\n  registry_id: exp-two-sided\n  claim: 2\n  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case\n    study）。包括 bootstrap confidence interval 和 FDR 控制。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- id: exp-extended-sim\n  registry_id: exp-extended-sim\n  claim: 2\n  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让\n    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向\n    lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 依赖 exp-two-sided 的双侧框架定义。\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- id: exp-ctrl-contam-pilot\n  claim: 1,2,3\n  description: 快速验证：Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU only。测量\n    Δlz*(clean→contaminated) 是否显著。增加第二个 0% seed 作为 clean-vs-clean noise floor baseline\n    (Reviewer Q2/Q4)。Eval 时区分 seen/unseen items 以实测 memorization fraction (Reviewer\n    Q3/W9)。这是论文 go/no-go 信号。\n  priority: P0-CRITICAL\n  gpu_budget_hours: 12\n  deps: []\n  status: planned\n  notes: 'GPU 恢复后第一优先。4 conditions × ~3 hrs = ~12 GPU-hrs (+2h for second 0% seed)。关键输出:\n    (a) Δlz* 显著性, (b) clean-vs-clean Δlz* ≈ 0 验证, (c) memorization fraction = (Δacc_seen\n    - Δacc_unseen)/Δacc_seen, (d) adjusted power = theory × memorization fraction。D010\n    要求。'\n- id: exp-ctrl-contam\n  claim: 1,2,3\n  description: 完整控制实验：在 4 个模型上用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量\n    Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - exp-ctrl-contam-pilot\n  status: planned\n  notes: '模型: Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3。Benchmark:\n    MMLU + GSM8K + HellaSwag。4 模型 × 6 levels × 3 benchmarks。'\n- id: exp-empirical-null\n  registry_id: exp-empirical-null\n  claim: 1\n  description: Bootstrap empirical null 分析：量化 lz* 在真实 LLM 数据上的 systematic bias（null\n    mean ≠ 0, null std ≠ 1），为 Calibration Gap Analysis 提供定量证据。包含 Q-Q plots、KS tests、bias\n    量化表、unflagged cells 深度分析。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 复用 exp-two-sided v2 的 bootstrap 逻辑，但保存完整中间分布。~2h 开发+运行。\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- id: exp-power-theory\n  registry_id: exp-power-theory\n  claim: 2\n  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A\n    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: DONE\n  notes: 纯理论推导 + 数值验证。CPU only.\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- id: exp-leaderboard-data-recon\n  registry_id: exp-leaderboard-data-recon\n  claim: 3\n  description: Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results\n    是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item\n    data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: 纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- id: exp-leaderboard-audit\n  claim: 3\n  description: Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark\n    污染率随时间趋势。\n  priority: ABANDONED\n  gpu_budget_hours: 20\n  deps:\n  - exp-two-sided\n  - exp-leaderboard-data-recon\n  status: planned\n  notes: 'D011: v1-irt-refit a_r=0.111 + item alignment 54.56% → 13K audit 不可行。数据可用性写入\n    Discussion/Future Work。'\n- id: exp-natural-experiment\n  claim: 3\n  description: v1 leaderboard base→chat model pairs 自然实验：计算 Δlz* = lz*(chat) - lz*(base)\n    作为 SFT 效应代理。\n  priority: P2-optional\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: 'D013: a_r=0.111 导致 lz*≈accuracy-like, 仅 4-5 pairs 无统计检验能力。Reviewer 终审建议降级。'\n- id: exp-v1-irt-refit-expanded\n  claim: 3\n  description: 扩大 v1 IRT 重拟合样本量至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。最终关闭 Path\n    D。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: CPU only. Reviewer 要求 N≥500 才能最终结论 Path D。阈值：a_r>0.4=可行, a_r<0.2=dead。\n- id: exp-4pl-ablation\n  claim: 1\n  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter\n    d 对 false alarm 和 detection power 的影响。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\n- id: exp-baseline-comparison\n  claim: 1\n  description: '与现有方法对比（≥5 baselines）：在控制实验的 ground-truth contaminated models 上，比较\n    IRT-FIT vs baselines 的 AUROC/Type-I error。Baselines: (1) ConStat (re-test), (2)\n    Min-K%++ (token probs), (3) accuracy z-score (已完成, CPU), (4) PPL-based detection\n    (log-prob family 代表, 预期 RL-robust 测试中失败), (5) random baseline。量化 minimal-information\n    的代价（power 损失）。报告 bootstrap CIs（同行 6/8 不报告方差，这是我们的差异化优势）。'\n  priority: P0-end\n  gpu_budget_hours: 30\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: 蒸馏显示同行 baseline 中位数 ~5 个。accuracy z-score 已完成(CPU)。ConStat 需 re-test, Min-K%++\n    需 token probs, PPL 需 log-probs。exp-ctrl-contam 完成后立即执行。\n- id: exp-multiscale-lzm\n  claim: 1,3\n  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化\n    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要实现 lzm 公式。\n- id: exp-post-rl\n  claim: 1\n  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应\n    Wang et al. (2025) 的 MIA 失效问题。\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\n- id: exp-extra-benchmarks\n  claim: 2,3\n  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items\n    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\n- id: exp-domain-analysis\n  claim: 3\n  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5\n    的 MMLU 污染是全面的还是集中在特定 domain。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要 MMLU item-to-domain 映射。\n\n\n## registry (completed experiments)\n\n- exp_id: sim_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    null_check:\n      all_pass: true\n      gsm8k_ks_p: 0.098\n      hellaswag_ks_p: 0.224\n      mmlu_ks_p: 0.594\n    simulation_power_at_15pct:\n      mmlu: 0.979\n      hellaswag: 0.733\n      gsm8k: 0.578\n      arc_c: 0.129\n      humaneval: 0.243\n    global_pass: false\n    inverted_u_all_benchmarks: true\n    pass_count_large_80pct: 1/3 (mmlu only)\n- exp_id: phase_b_personfit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_sd_all_gt_0.5: true\n    mmlu_lz_star_mean: 24.19\n    mmlu_lz_star_sd: 16.47\n    hellaswag_lz_star_mean: 20.09\n    hellaswag_lz_star_sd: 17.59\n    gsm8k_lz_star_mean: 8.22\n    gsm8k_lz_star_sd: 8.97\n    gemini15_mmlu_lz_star: 34.75\n    gemini15_mmlu_accuracy: 1\n    gemini15_mmlu_theta: 0.78\n    gemini15_flagged_benchmarks: 3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\n    cross_benchmark_spearman_significant: 1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\n    n_models: 12\n    n_benchmarks: 5\n- exp_id: exp-two-sided\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- exp_id: exp-extended-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- exp_id: exp-empirical-null\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- exp_id: exp-leaderboard-data-recon\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- exp_id: exp-power-theory\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- exp_id: exp-item-alignment-check\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    match_rate_direct: 0.5456\n    match_rate_reordered_mistral: 0.8846\n    match_rate_reordered_vicuna: 0.7248\n    n_items_checked: 14042\n    n_models_verified: 2\n    alignment_method: content-based via cais/mmlu canonical order\n    items_mapped: 12068\n    mapping_coverage: 0.86\n- exp_id: exp-v1-irt-refit-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 63\n    n_models_failed: 38\n    n_items: 14042\n    n_mapped_items: 12441\n    overall_accuracy: 0.426\n    fitting_time_2pl_sec: 8.9\n    fitting_time_3pl_sec: 12.1\n    3pl_a_pearson_r: 0.111\n    3pl_b_pearson_r: 0.626\n    3pl_b_spearman_r: 0.656\n    2pl_a_pearson_r: -0.084\n    2pl_b_pearson_r: 0.572\n    lz_star_mean: 11.69\n    lz_star_std: 6.68\n    lz_star_flagged_pct: 1.6\n- exp_id: exp-accuracy-zscore-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_flagged_count: 4\n    lz_flagged_count: 57\n    agreement_rate: 0.117\n    gemini15_mmlu_zscore: 1.413\n- exp_id: exp-cross-benchmark-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_all5_flagged: 10\n    n_models_selective_flagged: 2\n    gemini15_cluster_isolation: true\n    dominant_direction_pattern: positive\n    pct_positive_cells: 93.3\n    total_flagged: 57\n    flag_rate: 0.95\n- exp_id: exp-ml-classifier-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    auroc_avg_25pct:\n      lz_star: 0.86\n      lr_resp: 0.899\n      rf_resp: 0.885\n      lr_resp_summ: 0.909\n      rf_resp_summ: 0.913\n    auroc_avg_5pct:\n      lz_star: 0.675\n      best_ml: 0.575\n    auroc_avg_10pct:\n      lz_star: 0.763\n      best_ml: 0.712\n    lz_star_advantage_low_contam: +0.10 AUROC at 5%, +0.05 at 10%\n    ml_advantage_high_contam: +0.05 at 25%, +0.16 at 50%\n    key_finding: lz* outperforms supervised ML at low contamination (5-10%) without\n      any training data; ML only wins at 25%+ where signal is already strong\n- exp_id: exp-fdr-correction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    flagged_uncorrected: 57/60 (95%)\n    flagged_bh_fdr: 57/60 (95%)\n    flagged_bonferroni: not_computed_but_expected_similar\n    correction_scope: global_60_tests\n    unflagged_cells:\n    - Yi-Lightning×arc_c (bh_p=0.098)\n    - 360GPT2-Pro×humaneval (bh_p=0.134)\n    - Yi-Lightning×humaneval (bh_p=0.181)\n    note: Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale\n      FDR (24800+ tests) deferred to leaderboard audit.\n- exp_id: exp-clean-control-delta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    clean_vs_clean_mean_abs:\n      mmlu: 0.01\n      hellaswag: 0.125\n      gsm8k: 0.021\n      arc_c: 0.095\n      humaneval: 0.02\n    clean_vs_clean_all_nonsig: true\n    clean_vs_contam_all_sig: true\n    cohens_d:\n      mmlu: 2.66\n      hellaswag: 1.85\n      gsm8k: 1.85\n      arc_c: 0.45\n      humaneval: 1.07\n    arc_c_note: d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10\n- exp_id: exp-natural-experiment\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 21\n    n_benchmarks: 4\n    n_complete_pairs: 9\n    significant_benchmarks:\n      HellaSwag:\n        mean_deviation: -3.4\n        t_stat: -3.97\n        p_value: 0.001\n        interpretation: SFT systematically decreases person-fit on HellaSwag\n      GSM8K:\n        mean_deviation: 3.92\n        t_stat: 3.35\n        p_value: 0.009\n        interpretation: SFT systematically increases person-fit on GSM8K\n    non_significant_benchmarks:\n      MMLU:\n        p_value: 0.15\n      ARC-Challenge:\n        p_value: 0.38\n    individual_outliers: 0\n    key_finding: HellaSwag and GSM8K show significant systematic SFT effects on lz*,\n      but no individual pair shows benchmark-specific contamination outliers. P2-optional\n      per Director assessment.\n- exp_id: exp-v1-irt-refit-expanded\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 178\n    n_items: 14042\n    3pl_a_pearson_r: 0.127\n    2pl_a_pearson_r: -0.029\n    3pl_b_pearson_r: 0.663\n    reason: 'N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination\n      failure confirms Path D dead.'\n- exp_id: exp-4pl-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hypothesis_confirmed: true\n    far_4pl: ~5% (well-calibrated)\n    far_3pl: 4.7-16.5% (inflated)\n    far_2pl: 50-100% (catastrophic, unusable)\n    mean_power_gain_4pl_vs_3pl:\n      MMLU: +27.3pp\n      HellaSwag: +26.1pp\n      GSM8K: +20.3pp\n      ARC_C: +14.8pp\n      HumanEval: +13.7pp\n    max_power_gain_4pl_vs_3pl:\n      MMLU: +49.0pp\n      HellaSwag: +59.6pp\n      GSM8K: +39.7pp\n      ARC_C: +54.6pp\n      HumanEval: +30.6pp\n    power_at_25pct:\n      4PL:\n        MMLU: 0.776\n        HellaSwag: 0.534\n        GSM8K: 0.73\n        ARC_C: 0.132\n        HumanEval: 0.318\n      3PL:\n        MMLU: 0.329\n        HellaSwag: 0.28\n        GSM8K: 0.334\n        ARC_C: 0.091\n        HumanEval: 0.165\n    d_bucket_analysis: 'd<0.8: +6.8pp to +61.2pp; d>=0.95: negligible'\n    key_finding: 4PL d parameter essential for LLM contamination detection. 46% MMLU\n      items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely\n      miscalibrated (FAR 50-100%).\n- exp_id: exp-domain-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_mmlu_accuracy: 100% (14042/14042)\n    gemini_domain_concentrated: false\n    gemini_subjects_flagged: 50/57 (lz*>1.96)\n    gemini_category_lz:\n      STEM: 21.2\n      Humanities: 17.9\n      Social Sciences: 15.9\n      Other: 15.3\n    doubao_negative_lz: true\n    doubao_category_lz:\n      STEM: -2\n      Humanities: -13\n      Social_Sciences: -14.8\n      Other: 4.4\n    hunyuan_uneven:\n      STEM: 1.8\n      Social_Sciences: 13.9\n    yi_lightning_highest_mmlu_lz: 48.2\n    qwen_plus_second_highest: 44.9\n    mistral_flagged_subjects: 55/57\n- exp_id: exp-ctrl-contam-pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall: partial - H1/H2 confirmed, H3/H4 not as expected under theta-free; theta-fixed\n      restores dose-response\n    H1_clean_delta_lz_approx_zero:\n      confirmed: true\n      clean_delta_lz: 2.07\n      clean_s1_lz: 8.01\n      clean_s2_lz: 5.94\n      baseline_mean: 6.98\n      baseline_std: 1.03\n    H2_contam_15_detection:\n      confirmed: true\n      delta_lz_free: -3.97\n      cohens_d: -3.85\n    H3_dose_response:\n      theta_free:\n        confirmed: false\n        contam_15_delta: -3.97\n        contam_50_delta: -1.53\n        ratio: 0.38\n        note: inverted due to theta-shift\n      theta_fixed:\n        confirmed: true\n        contam_15_delta: 2.96\n        contam_50_delta: 8.67\n        ratio: 2.93\n        note: monotonicity restored\n    H4_memorization_fraction:\n      confirmed: false\n      contam_15: 0.38\n      contam_50: 0.29\n    theta_shift:\n      clean_s1: -0.0987\n      clean_s2: -0.0842\n      contam_15: 0.1971\n      contam_50: 0.3703\n      theta_fixed: -0.0914\n    theta_fixed_analysis:\n      contam_15:\n        lz_free: 3\n        lz_fixed: 9.93\n        delta_free: -3.97\n        delta_fixed: 2.96\n        absorbed: 6.93\n      contam_50:\n        lz_free: 5.45\n        lz_fixed: 15.64\n        delta_free: -1.53\n        delta_fixed: 8.67\n        absorbed: 10.2\n    accuracy:\n      clean_s1: 0.679\n      clean_s2: 0.679\n      contam_15: 0.731\n      contam_50: 0.764\n      contam_15_seen: 0.824\n      contam_15_unseen: 0.715\n      contam_50_seen: 0.805\n      contam_50_unseen: 0.724\n- exp_id: exp-4pl-real-data-degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    correlation_4pl_vs_3pl:\n      pearson_r: 0.225\n      rmse: 68.41\n    most_affected_benchmark: MMLU (mean |Δlz*|=58.3, 46% items d<0.95)\n    most_affected_model: 'DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6'\n    low_ability_models_impact: '|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)'\n    bias_direction: 3PL systematically depresses high-ability models' lz* (d=1 makes\n      P→1, amplifying few-error aberrance)\n    key_finding: Ignoring d parameter makes lz* completely unreliable for high-ability\n      models — d-induced bias far exceeds any contamination signal\n- exp_id: exp-ctrl-contam-pilot-clean-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-clean-s2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-15\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-50\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:04:25.016Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:04:25.016Z",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T19:04:25.036Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Multi-model ctrl-contam 全面成功 + post-RL 信号存活 + lz* 在低污染率胜出所有 baselines
核心假设：['SFT memorization fingerprint跨模型家族一致：4/4 模型在 15% 污染下均产生显著 Δlz*', 'θ-fixed 策略普适：所有模型均可通过固定 θ 恢复单调 dose-response', 'Post-RL 不破坏 binary response 层面的记忆痕迹（GRPO 后 Δlz* 保留 ≥70%）', '小 benchmark（GSM8K ~1.3K items）在 ctrl-contam 中仍产生可检测信号（|d| > 0.8）', 'lz* 在 5-10% 低污染率下 AUROC 持续优于所有 supervised baselines']
关键指标范围：{'cohens_d_15pct_across_models': [2.0, 5.0], 'cohens_d_15pct_min_model': [1.5, 3.0], 'models_significant_at_15pct': [4, 4], 'benchmarks_significant_per_model': [2, 3], 'memorization_fraction_15pct': [0.3, 0.5], 'theta_fixed_dose_response_ratio': [2.5, 4.0], 'post_rl_signal_retention': [0.7, 1.0], 'lz_star_auroc_5pct': [0.7, 0.85], 'lz_star_auroc_10pct': [0.8, 0.92], 'lz_star_minus_best_baseline_auroc_5pct': [0.0, 0.15], 'seen_unseen_lz_gap_15pct': [2.5, 5.0]}
叙事方向：原始 framing 完全成立。IRT-FIT 是 minimal-information operating point 上的有效检测框架： 跨 4 个模型家族一致检测、post-RL robust、在实际关键的低污染率下无需标注数据即胜过 supervised baselines。 三条 claims 无需调整——Claim 1 的 "principled framework" 有 ctrl-contam 全面验证， Claim 2 的 power function 有 multi-benchmark 实证确认，Claim 3 的 empirical findings 加入 ctrl-contam 的跨模型 memorization 量化。θ-shift 作为 methodological contribution 而非 limitation。 Headline: "binary response patterns alone detect SFT contamination across model families, even after RL post-training."


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
  "promptId": "21259111-2c67-4b84-9846-6398f4ebd10d",
  "type": "user",
  "uuid": "68cf6f41-86d9-46b8-ac9e-0075e1f6aa1b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:04:25.034Z_

```json
{
  "parentUuid": "68cf6f41-86d9-46b8-ac9e-0075e1f6aa1b",
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
  "uuid": "eb15ce68-1919-4006-b06c-f23cd3450d0d",
  "timestamp": "2026-05-20T19:04:25.034Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:04:25.034Z_

```json
{
  "parentUuid": "eb15ce68-1919-4006-b06c-f23cd3450d0d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6a984fb0-09d4-45e7-8dbb-ff119dd2644c",
  "timestamp": "2026-05-20T19:04:25.034Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Multi-model ctrl-contam 全面成功 + post-RL 信号存活 + lz* 在低污染率胜出所有 baselines 核心假设：['SFT memorization fingerprint跨模型家族一致：4/4 模型在 15% 污染下均产生显著 Δlz*', 'θ-fixed 策略普适：…",
  "leafUuid": "6a984fb0-09d4-45e7-8dbb-ff119dd2644c",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Controlled contamination validation with theta-fixed analysis",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:05:08.224Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, assuming the "best" tier outcome. I need to provide result_rationale for each prediction explaining why this tier would produce these results.

Let me go through each planned experiment and generate predictions consistent with the "best" tier definition:

**Best tier definition:**
- Multi-model ctrl-contam 全面成功
- Post-RL 信号存活
- lz* 在低污染率胜出所有 baselines

**Core hypotheses (all confirmed in best):**
1. SFT memorization fingerprint跨模型家族一致：4/4 模型在 15% 污染下均产生显著 Δlz*


2. The θ-fixed approach works universally across all models, restoring monotonic dose-response curves when parameters are held constant
3. Post-RL training preserves the underlying memory signal at the binary response level, with GRPO retaining at least 70% of the original Δlz* effect
4. Even smaller benchmarks like GSM8K with ~1.3K items generate detectable contamination signals with effect sizes exceeding 0.8
5. The lz* metric demonstrates superiority over baselines at low contamination rates between 5-10%

Now I'm looking at the performance metrics across different contamination levels and model configurations—the effect sizes range from 2.0 to 5.0 across models, with consistent statistical significance, and the memorization fraction stays between 30-50% while the dose-response ratio scales from 2.5 to 4.0.

For the experiments, I've got a pilot validation planned with Qwen3.5-9B across four conditions, followed by the full controlled contamination study across multiple models, while the leaderboard audit is being skipped. Several other experiments like the natural experiment, IRT refit expansion, and 4PL ablation are already completed in the registry.

Looking more carefully at what's actually still pending versus what's marked done, I'm noticing some of the experiments flagged as planned have already been executed—the pilot contamination study, the natural experiment, the IRT refit work, the 4PL ablation, and the domain analysis are all finished. The ones I still need to run are the baseline comparison, multiscale LZM analysis, post-RL evaluation, and the extra benchmarks. I need to distinguish between experiments that are genuinely planned versus those already completed in the registry. The user is asking for predictions on experiments marked as "planned" in the experiment_plan, but I should focus on the ones that haven't actually been run yet, since the completed ones already have real results. Let me identify which of these planned experiments are still pending versus which have already been executed. on truly planned ones:

From experiment_plan with status: planned AND NOT in registry as DONE:
1. **exp-ctrl-contam-pilot** - Wait, it IS in registry as DONE with extensive metrics. But in the experiment_plan it says "planned". I think the experiment_plan is the source of truth for this task. Let me just do all "planned" ones.

Actually, looking at the registry, exp-ctrl-contam-pilot IS done. And exp-natural-experiment, exp-v1-irt-refit-expanded, exp-4pl-ablation, exp-domain-analysis are all DONE.

I think the cleanest approach: predict for ALL experiments listed in experiment_plan with status: planned, since the user explicitly asked for "每个 planned 实验". For the ones already done in registry, I'll use the actual results as a base but frame them in the "best" tier context. For the ones truly not done yet, I'll generate predictions.

Re-reading the request more carefully - the user wants detailed predicted data for each planned experiment under the "best" tier assumption. Since several experiments already have actual results in the registry, I should use those as a foundation but present them within the "best" tier framework. For the genuinely unrun experiments, I'll create predictions based on the tier assumptions. Now I'm putting together the YAML structure with detailed rationales for each experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a984fb0-09d4-45e7-8dbb-ff119dd2644c",
  "isSidechain": false,
  "requestId": "req_011CbELm2qcJHacMAtmXb46Q",
  "type": "assistant",
  "uuid": "26b7e67b-4c71-47c1-95c2-512739e1ac37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H91hv3nidN6jZW1ZSUQcZ6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20980,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16880,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20980
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

_source line 9 · 2026-05-20T19:09:44.362Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。IRT-FIT 是 minimal-information operating point 上的有效检测框架：
  跨 4 个模型家族一致检测、post-RL robust、在实际关键的低污染率下无需标注数据即胜过 supervised baselines。
  三条 claims 无需调整——Claim 1 的 "principled framework" 有 ctrl-contam 全面验证，
  Claim 2 的 power function 有 multi-benchmark 实证确认，Claim 3 的 empirical findings 加入
  ctrl-contam 的跨模型 memorization 量化。θ-shift 作为 methodological contribution 而非 limitation。
  Headline: "binary response patterns alone detect SFT contamination across model families, even after RL post-training."

imagined_experiments:
  - name: "Controlled Contamination Pilot (Qwen3.5-9B)"
    plan_id: "exp-ctrl-contam-pilot"
    description: >
      Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU。
      验证 Δlz* 显著性、clean-vs-clean noise floor、seen/unseen memorization fraction。
    expected_results:
      clean_s1_lz_star: 7.2
      clean_s2_lz_star: 6.8
      clean_delta_lz: 0.4
      clean_delta_nonsig: true
      contam_15_lz_star_free: 2.8
      contam_15_delta_lz_free: -4.1
      contam_15_cohens_d: -3.95
      contam_50_lz_star_free: 4.9
      contam_50_delta_lz_free: -2.0
      contam_15_lz_star_fixed: 10.5
      contam_50_lz_star_fixed: 16.8
      theta_fixed_delta_15: 3.5
      theta_fixed_delta_50: 9.8
      theta_fixed_ratio: 2.80
      accuracy_clean: 0.71
      accuracy_contam_15: 0.76
      accuracy_contam_50: 0.80
      accuracy_contam_15_seen: 0.86
      accuracy_contam_15_unseen: 0.73
      memorization_fraction_15: 0.42
      memorization_fraction_50: 0.31
      theta_shift_clean: -0.08
      theta_shift_contam_15: 0.22
      theta_shift_contam_50: 0.41
    result_rationale: >
      Qwen3.5-9B 作为较新架构（含 thinking 能力），SFT memorization 效率略高于 Qwen2.5-7B。
      15% 污染产生强信号（|d|≈4.0）是因为 QLoRA 在小比例 seen items 上产生明确的 aberrant pattern：
      模型在高难度 seen items 上异常正确，而在 unseen items 上保持原有错误模式。memorization_fraction≈0.42
      说明 ~42% 的 seen items 被完全记忆（产生 aberrant response），剩余 58% 产生了泛化而非逐字记忆。
      θ-shift 机制与 pilot 一致：污染提升整体能力估计，θ_MLE 上升吸收了部分 aberrance signal，
      θ-fixed 恢复单调性。clean-vs-clean Δ≈0.4 确认 noise floor 远低于检测阈值。
    tables:
      - name: "Table: Qwen3.5-9B Pilot Results"
        columns: [condition, accuracy, lz_star_free, lz_star_fixed, theta_MLE, delta_lz_free, delta_lz_fixed]
        rows:
          - [clean_s1, 0.71, 7.2, 7.2, -0.08, "—", "—"]
          - [clean_s2, 0.71, 6.8, 6.8, -0.09, 0.4, 0.4]
          - [contam_15, 0.76, 2.8, 10.5, 0.22, -4.1, 3.5]
          - [contam_50, 0.80, 4.9, 16.8, 0.41, -2.0, 9.8]
    figures_description:
      - "Fig: θ-shift diagram showing clean θ≈-0.08, contam_15 θ=0.22, contam_50 θ=0.41; arrows indicate signal absorption mechanism"
      - "Fig: Seen vs unseen accuracy split bar chart (contam_15: 0.86 vs 0.73; contam_50: 0.80 vs 0.72)"
    analysis: >
      Go/no-go 信号明确通过。|d|=3.95 远超 0.8 的 large effect 阈值。θ-fixed 恢复单调 dose-response
      (ratio=2.80∈[2.5,4.0])，确认 θ-shift 是唯一导致 free-θ 非单调的机制。
      memorization_fraction=0.42 意味着理论 power 的 ~42% 可在实际中实现——MMLU 15% 理论 power 98.5% ×
      0.42 = adjusted power ≈41%，但 lz* 检测的是 aggregate pattern 而非逐 item 检测，
      所以 aggregate Δlz* 仍然产生 |d|≈4 的强效应。

  - name: "Full Multi-Model Controlled Contamination"
    plan_id: "exp-ctrl-contam"
    description: >
      4 模型 (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3) ×
      6 contamination levels (0/5/10/15/25/50%) × 3 benchmarks (MMLU, GSM8K, HellaSwag)。
    expected_results:
      # Cross-model 15% MMLU results
      cohens_d_15pct_mmlu:
        qwen3.5-9b: -3.95
        gemma-4-31b: -4.52
        llama-3.1-8b: -2.85
        mistral-7b-v0.3: -2.42
      cohens_d_15pct_mean: 3.44
      cohens_d_15pct_min: 2.42
      models_significant_at_15pct: 4
      # Per-model benchmark coverage
      benchmarks_significant_per_model:
        qwen3.5-9b: 3  # MMLU, GSM8K, HellaSwag all significant
        gemma-4-31b: 3
        llama-3.1-8b: 2  # MMLU, HellaSwag (GSM8K borderline due to n=1319)
        mistral-7b-v0.3: 2  # MMLU, HellaSwag
      # GSM8K specific (small benchmark hypothesis)
      gsm8k_cohens_d_15pct:
        qwen3.5-9b: -1.42
        gemma-4-31b: -1.68
        llama-3.1-8b: -0.91
        mistral-7b-v0.3: -0.85
      gsm8k_all_above_0.8: true
      # Memorization fractions
      memorization_fraction_15pct:
        qwen3.5-9b: 0.42
        gemma-4-31b: 0.48
        llama-3.1-8b: 0.35
        mistral-7b-v0.3: 0.33
      memorization_fraction_mean: 0.40
      # θ-fixed analysis
      theta_fixed_dose_response_ratio:
        qwen3.5-9b: 2.80
        gemma-4-31b: 3.45
        llama-3.1-8b: 2.62
        mistral-7b-v0.3: 2.55
      theta_fixed_ratio_mean: 2.86
      theta_fixed_all_monotonic: true
      # Seen/unseen gap
      seen_unseen_lz_gap_15pct:
        qwen3.5-9b: 3.2
        gemma-4-31b: 4.1
        llama-3.1-8b: 2.7
        mistral-7b-v0.3: 2.5
      seen_unseen_gap_mean: 3.13
      # Dose-response (θ-fixed, MMLU)
      dose_response_mmlu_theta_fixed:
        "5pct": {qwen: 1.1, gemma: 1.4, llama: 0.8, mistral: 0.7}
        "10pct": {qwen: 2.2, gemma: 2.7, llama: 1.6, mistral: 1.4}
        "15pct": {qwen: 3.5, gemma: 4.2, llama: 2.5, mistral: 2.2}
        "25pct": {qwen: 5.8, gemma: 7.0, llama: 4.1, mistral: 3.7}
        "50pct": {qwen: 9.8, gemma: 14.5, llama: 6.6, mistral: 6.3}
    result_rationale: >
      Best 档要求 4/4 模型在 15% 均显著。Gemma-4-31B 作为 31B 参数模型具有更强的 memorization 能力
      （SFT 时容量更大，更容易逐字存储 seen items），因此 |d| 最高（4.52）且 memorization_fraction
      最高（0.48）。Llama-3.1-8B 和 Mistral-7B-v0.3 参数较少但仍在 |d|>2.0 范围，因为 QLoRA
      即使在小模型上也能有效注入 memorization——关键是 LoRA rank 足够捕获 item-level patterns。
      GSM8K 虽然只有 ~1.3K items（理论 power 较低），但 ctrl-contam 测量的是 Δlz*（within-model shift）
      而非绝对检测，所以即使 power function 预测 single-model detection 只有 59%，
      paired comparison 的效应量仍可达 |d|>0.8。θ-fixed 策略在所有模型上普适是因为
      θ-shift 机制是 IRT MLE 估计的数学性质（污染→更多正确→θ_MLE↑），与模型架构无关。
      Seen/unseen gap∈[2.5,5.0] 反映了 SFT 的部分泛化效应：seen items lz*≈0（memorized items
      看起来"正常"），unseen items lz* 保持高值（未被 memorize 的 items 仍然产生 aberrant patterns）。
    tables:
      - name: "Table: Cross-Model Detection at 15% Contamination (MMLU)"
        columns: [model, accuracy_clean, accuracy_contam15, delta_lz_free, delta_lz_fixed, cohens_d, memorization_frac, theta_shift]
        rows:
          - [Qwen3.5-9B, 0.71, 0.76, -4.1, 3.5, -3.95, 0.42, +0.30]
          - [Gemma-4-31B, 0.78, 0.84, -4.8, 4.2, -4.52, 0.48, +0.35]
          - [Llama-3.1-8B, 0.63, 0.69, -2.9, 2.5, -2.85, 0.35, +0.24]
          - [Mistral-7B-v0.3, 0.61, 0.67, -2.5, 2.2, -2.42, 0.33, +0.21]
      - name: "Table: GSM8K Small-Benchmark Detection at 15%"
        columns: [model, n_items, delta_lz_fixed, cohens_d, significant_p005]
        rows:
          - [Qwen3.5-9B, 1319, 1.8, -1.42, true]
          - [Gemma-4-31B, 1319, 2.1, -1.68, true]
          - [Llama-3.1-8B, 1319, 1.2, -0.91, true]
          - [Mistral-7B-v0.3, 1319, 1.1, -0.85, true]
      - name: "Table: θ-Fixed Dose-Response (MMLU, all models)"
        columns: [contam_level, qwen_delta, gemma_delta, llama_delta, mistral_delta, monotonic]
        rows:
          - [5%, 1.1, 1.4, 0.8, 0.7, "✓"]
          - [10%, 2.2, 2.7, 1.6, 1.4, "✓"]
          - [15%, 3.5, 4.2, 2.5, 2.2, "✓"]
          - [25%, 5.8, 7.0, 4.1, 3.7, "✓"]
          - [50%, 9.8, 14.5, 6.6, 6.3, "✓"]
    figures_description:
      - "Fig: 4-panel dose-response curves (one per model), x=contamination%, y=Δlz*_fixed, all monotonically increasing"
      - "Fig: Cross-model Cohen's d forest plot at 15% contamination, showing all 4 models × 3 benchmarks with 95% bootstrap CIs"
      - "Fig: Seen/unseen lz* distribution violin plots per model at 15% contamination"
      - "Fig: Memorization fraction heat map (4 models × 3 benchmarks × 6 levels)"
    analysis: >
      核心假设 1 完全验证：SFT memorization fingerprint 跨 4 个模型家族一致。效应量范围 [2.42, 4.52]
      远超统计显著性需求。θ-fixed 策略普适性确认（假设 2），所有模型的 dose-response ratio ∈[2.55, 3.45]。
      GSM8K 的小 benchmark 假设（假设 4）通过 |d|>0.8 验证，尽管绝对信号弱于 MMLU（n=14042 vs 1319），
      paired comparison 设计弥补了 power 不足。这为 Claim 1 提供了跨架构、跨规模的 ground-truth validation。

  - name: "Baseline Comparison (≥5 methods)"
    plan_id: "exp-baseline-comparison"
    description: >
      在 ctrl-contam ground-truth 上比较 IRT-FIT vs 5+ baselines 的 AUROC。
      Baselines: ConStat (re-test), Min-K%++ (token probs), accuracy z-score,
      PPL-based detection, random baseline, + ML classifiers (LR/RF)。
    expected_results:
      # AUROC at 5% contamination (the critical low-contam regime)
      auroc_5pct:
        lz_star_theta_fixed: 0.78
        lr_binary_oracle: 0.62
        rf_binary_oracle: 0.59
        accuracy_zscore: 0.55
        min_k_pp: 0.71
        ppl_based: 0.68
        constat_retest: 0.65
        random: 0.50
      # AUROC at 10% contamination
      auroc_10pct:
        lz_star_theta_fixed: 0.87
        lr_binary_oracle: 0.74
        rf_binary_oracle: 0.72
        accuracy_zscore: 0.63
        min_k_pp: 0.82
        ppl_based: 0.79
        constat_retest: 0.76
        random: 0.50
      # AUROC at 15% contamination
      auroc_15pct:
        lz_star_theta_fixed: 0.92
        lr_binary_oracle: 0.84
        rf_binary_oracle: 0.82
        accuracy_zscore: 0.71
        min_k_pp: 0.89
        ppl_based: 0.86
        constat_retest: 0.83
        random: 0.50
      # AUROC at 25% contamination
      auroc_25pct:
        lz_star_theta_fixed: 0.94
        lr_binary_oracle: 0.92
        rf_binary_oracle: 0.91
        accuracy_zscore: 0.78
        min_k_pp: 0.95
        ppl_based: 0.93
        constat_retest: 0.91
        random: 0.50
      # Key comparisons
      lz_minus_best_baseline_5pct: 0.07  # lz* - Min-K%++ at 5%
      lz_minus_best_binary_baseline_5pct: 0.16  # lz* - LR at 5%
      crossover_point: "~20% (Min-K%++ surpasses lz* above 20%)"
      bootstrap_ci_width_mean: 0.04
      # Information access comparison
      information_levels:
        binary_only: [lz_star, accuracy_zscore, lr_binary, rf_binary]
        token_probs: [min_k_pp, ppl_based]
        retest_required: [constat_retest]
    result_rationale: >
      lz* 在 5-10% 低污染率胜出所有 baselines（假设 5）的机制：IRT 结构作为 inductive bias。
      在低污染率下，signal-to-noise 极低——只有 5-10% 的 items 携带 contamination signal。
      ML classifiers（LR/RF）即使有 oracle labels 也面临严重的 class imbalance（5% positive），
      且 binary feature space（0/1 per item）在低 contamination 时几乎不可分。
      lz* 的优势来自 IRT model 提供的 structured expectation：它知道每个 item 的 expected P(correct|θ)，
      因此即使只有 5% items 被 contaminate，这些 items 上的 "impossible correctness"（高难度 item 被答对）
      会被精确捕获为 aberrance。而 ML classifier 只看到 raw 0/1 pattern，缺乏 item difficulty 的先验。
      Min-K%++ 在 5% 时 AUROC=0.71 弱于 lz*（0.78）是因为 token-level 信号在极低污染时被 noise 淹没，
      但在 20%+ 时 token distribution shift 变得明显，超过 binary-level detection。
      accuracy z-score 作为 same-level binary baseline 在所有水平都远不如 lz*——
      它只看 total score 而非 pattern，丢失了 item-level aberrance 信息。
      这确立了 IRT structure 作为 binary-only 方法的关键 advantage。
    tables:
      - name: "Table: AUROC Comparison Across Contamination Levels (MMLU, averaged over 4 models)"
        columns: [method, info_level, auroc_5pct, auroc_10pct, auroc_15pct, auroc_25pct]
        rows:
          - [lz*_θ-fixed, binary, "0.78±0.03", "0.87±0.03", "0.92±0.02", "0.94±0.02"]
          - [Min-K%++, token_probs, "0.71±0.04", "0.82±0.03", "0.89±0.02", "0.95±0.01"]
          - [PPL-based, log_probs, "0.68±0.04", "0.79±0.03", "0.86±0.03", "0.93±0.02"]
          - [ConStat, retest, "0.65±0.05", "0.76±0.04", "0.83±0.03", "0.91±0.02"]
          - [LR (oracle), binary, "0.62±0.05", "0.74±0.04", "0.84±0.03", "0.92±0.02"]
          - [RF (oracle), binary, "0.59±0.06", "0.72±0.04", "0.82±0.03", "0.91±0.02"]
          - [Acc z-score, binary, "0.55±0.05", "0.63±0.04", "0.71±0.04", "0.78±0.03"]
          - [Random, "—", 0.50, 0.50, 0.50, 0.50]
      - name: "Table: lz* Advantage Over Best Baseline at Each Level"
        columns: [contam_level, best_baseline, best_baseline_auroc, lz_auroc, delta, significant]
        rows:
          - [5%, Min-K%++, 0.71, 0.78, +0.07, "p<0.05"]
          - [10%, Min-K%++, 0.82, 0.87, +0.05, "p<0.05"]
          - [15%, Min-K%++, 0.89, 0.92, +0.03, "p=0.08"]
          - [25%, Min-K%++, 0.95, 0.94, -0.01, "n.s."]
    figures_description:
      - "Fig: AUROC curves (x=contamination%, y=AUROC) for all 7 methods, with bootstrap 95% CI bands; lz* dominates at ≤15%"
      - "Fig: Detection frontier diagram — x=information access level, y=AUROC@10%; shows lz* achieving near-parity with token-level methods despite binary-only input"
      - "Fig: DeLong test p-value heatmap (pairwise method comparisons at each contamination level)"
    analysis: >
      Best 档的 headline result：lz* 在实际关键的 5-10% 低污染率下无需任何标注数据或 token access
      即胜过 supervised baselines 和 token-level methods。这验证了 IRT structure 作为 inductive bias
      在 data-scarce regime 的优势。crossover 发生在 ~20%——高于此水平时 Min-K%++ 的 token-level
      signal 更强，但 20%+ 的污染在实际场景中已经很容易被 accuracy jump 发现。
      关键 framing：lz* 在 "检测困难" 的低污染区间胜出，正是 minimal-information 方法最有价值的 regime。

  - name: "Post-RL Signal Retention"
    plan_id: "exp-post-rl"
    description: >
      Qwen3.5-9B 上先 SFT 污染（15%）再 GRPO 训练，测试 Δlz* 在 RL 后是否保持。
      回应 Wang et al. (2025) 的 MIA 全失效发现。
    expected_results:
      # Pre-RL (SFT only)
      pre_rl_delta_lz_fixed: 3.5
      pre_rl_cohens_d: -3.95
      pre_rl_accuracy_contam: 0.76
      pre_rl_accuracy_seen: 0.86
      # Post-RL (SFT + GRPO)
      post_rl_delta_lz_fixed: 2.8
      post_rl_cohens_d: -3.15
      post_rl_accuracy_contam: 0.79
      post_rl_accuracy_seen: 0.82
      # Signal retention
      signal_retention: 0.80  # 2.8/3.5
      retention_above_70pct: true
      # Comparison with MIA methods post-RL
      min_k_pp_pre_rl_auroc: 0.89
      min_k_pp_post_rl_auroc: 0.54  # near random, consistent with Wang et al.
      ppl_pre_rl_auroc: 0.86
      ppl_post_rl_auroc: 0.52  # near random
      lz_star_pre_rl_auroc: 0.92
      lz_star_post_rl_auroc: 0.85
      # Mechanism analysis
      seen_accuracy_drop_post_rl: 0.04  # 0.86→0.82, slight forgetting
      unseen_accuracy_gain_post_rl: 0.03  # 0.73→0.76, RL improves reasoning
      memorization_fraction_post_rl: 0.34  # down from 0.42
      theta_shift_post_rl: 0.28  # slightly higher than pre-RL 0.22 due to RL improvement
    result_rationale: >
      Post-RL signal retention ≥70%（假设 3）成立的核心原因：GRPO 优化的是 reward signal（正确率/格式），
      而非 item-level response distribution。SFT memorization 写入的是 "看到 item X → 输出 answer Y"
      的 pattern，这是 parameter-level 的 association。GRPO 的 policy gradient 更新主要影响
      reasoning chain 的 token distribution，而 binary correctness 层面的 memorization 痕迹
      （hard item 仍然答对）大部分保留。signal 从 3.5 降到 2.8（retention=80%）的 20% 损失来自：
      (a) RL 训练中少量 seen items 的 memorization 被 "覆盖"（RL 发现了不同的 reasoning path），
      (b) RL 普遍提升了 unseen items 的正确率（θ进一步上升），轻微压缩了 seen/unseen gap。
      但关键是 binary response 层面的 aberrant pattern 仍然存在——模型在 "不该答对" 的 hard items 上
      仍然答对，这个 pattern-level signal 是 RL 无法消除的，因为 RL 没有动机去 "故意答错" 已经答对的题。
      相比之下，MIA methods（Min-K%++, PPL）失效是因为 RL 彻底重塑了 token-level distribution——
      reasoning tokens 的 perplexity 分布被 GRPO 重新优化，训练数据的 token-level fingerprint 消失。
      这是 binary vs token-level detection 的 structural advantage。
    tables:
      - name: "Table: Pre-RL vs Post-RL Detection Comparison"
        columns: [method, info_level, auroc_pre_rl, auroc_post_rl, retention_pct]
        rows:
          - [lz*_θ-fixed, binary, 0.92, 0.85, "80%"]
          - [Min-K%++, token_probs, 0.89, 0.54, "4%"]
          - [PPL-based, log_probs, 0.86, 0.52, "2%"]
          - [Acc z-score, binary, 0.71, 0.65, "60%"]
          - [LR (oracle), binary, 0.84, 0.72, "56%"]
      - name: "Table: Binary Response Patterns Pre/Post RL"
        columns: [metric, pre_rl, post_rl, change]
        rows:
          - [Δlz*_fixed, 3.5, 2.8, "-20%"]
          - [Cohen's d, -3.95, -3.15, "-20%"]
          - [Seen accuracy, 0.86, 0.82, "-4pp"]
          - [Unseen accuracy, 0.73, 0.76, "+3pp"]
          - [Memorization fraction, 0.42, 0.34, "-8pp"]
    figures_description:
      - "Fig: Side-by-side lz* distributions (pre-RL vs post-RL) showing signal compression but retention"
      - "Fig: Method comparison bar chart — AUROC pre/post RL for all methods, showing MIA collapse vs lz* retention"
      - "Fig: Item-level analysis — scatter plot of P(correct) change per item, colored by seen/unseen"
    analysis: >
      这是论文最强的 selling point 之一。Wang et al. (2025) 证明所有 10 种 log-prob based methods
      在 RL 后降至 random，而 lz* 保留 80% 信号。这直接证明了 minimal-information operating point
      的 structural advantage：binary patterns 对 RL 是 robust 的，因为 RL 优化的是
      generation quality 而非 item-level correctness erasure。paper 可以引用此结果
      直接回应 Wang et al. 的 "all methods fail" claim——"all TOKEN-LEVEL methods fail,
      but BINARY-LEVEL detection survives."

  - name: "Multiscale lzm Statistic"
    plan_id: "exp-multiscale-lzm"
    description: >
      实现 Hong, Lin & Cheng (2021) 的 multiscale lzm——跨 benchmark 聚合的标准化 lz* 总分。
      在 PSN-IRT 12 模型和 ctrl-contam 模型上验证。
    expected_results:
      # PSN-IRT 12 models
      gemini15_lzm: 42.8
      deepseek_v3_lzm: 38.2
      yi_lightning_lzm: 35.6
      qwen_plus_lzm: 33.1
      doubao_pro_lzm: -8.4
      mistral_7b_lzm: 2.1
      # Cross-benchmark aggregation power
      lzm_vs_mean_lz_correlation: 0.97
      lzm_flagged_at_alpha005: 11/12
      # Ctrl-contam application
      ctrl_contam_lzm_clean: 8.5
      ctrl_contam_lzm_15pct: 14.2
      ctrl_contam_lzm_50pct: 22.8
      lzm_cohens_d_15pct: -4.12
      lzm_incremental_over_single_benchmark: "+0.15 AUROC vs single-best benchmark"
    result_rationale: >
      lzm 聚合跨 benchmark 信号的原理：如果一个模型在多个 benchmarks 上都表现异常，
      lzm 将这些独立 signals 标准化后求和，产生比任何单一 benchmark 更强的检测统计量。
      在 best 档下，ctrl-contam 跨 3 个 benchmarks 都注入了污染，lzm 的 multi-benchmark
      aggregation 产生额外的 +0.15 AUROC 增益。对 PSN-IRT 12 模型，lzm 与 mean_lz* 高度相关（r=0.97）
      因为大多数模型的 anomaly 在所有 benchmarks 上方向一致（positive direction dominant, 93.3% cells）。
      Doubao-pro 的负 lzm 反映其独特的 negative lz* 模式（STEM 和 Humanities domains 特异性不足）。
      这是一个 methodological addition（不是核心贡献），但增强了 paper 的 completeness。
    tables:
      - name: "Table: lzm Scores for PSN-IRT 12 Models"
        columns: [model, lz_mmlu, lz_hellaswag, lz_gsm8k, lz_arc_c, lz_humaneval, lzm_aggregate]
        rows:
          - [Gemini-1.5, 31.8, 28.4, 12.1, 6.2, -2.4, 42.8]
          - [DeepSeek-V3, 28.6, 25.1, 10.8, 5.8, -1.2, 38.2]
          - [Yi-Lightning, 26.4, 22.3, 9.5, -0.3, -1.8, 35.6]
          - [Doubao-Pro, -12.5, -8.2, 4.3, -2.1, -3.8, -8.4]
    figures_description:
      - "Fig: lzm bar chart for 12 models, sorted by magnitude, with 95% CI error bars"
      - "Fig: lzm vs mean(lz*) scatter showing near-perfect correlation but information-theoretic gain from proper weighting"
    analysis: >
      lzm 提供了一个 principled 的跨 benchmark 聚合方式，比简单 mean(lz*) 有理论优势
      （proper variance weighting）。在 ctrl-contam 中，multi-benchmark contamination 的
      lzm 检测力比 single-best benchmark 强 0.15 AUROC，证明了 multiscale 方法的实用价值。
      但核心贡献仍是 per-benchmark lz*，lzm 作为 extension/robustness check。

  - name: "Extra Benchmarks (BBH + MATH)"
    plan_id: "exp-extra-benchmarks"
    description: >
      BBH (6,511 items) 和 MATH (5,000 items) 扩展，填充 1K-10K items 的 power gap。
      在 ctrl-contam 模型上验证中等规模 benchmark 的检测力。
    expected_results:
      # Power function validation
      bbh_theoretical_power_15pct: 0.88
      math_theoretical_power_15pct: 0.82
      bbh_actual_power_15pct: 0.85  # close to theory since BBH items are well-calibrated
      math_actual_power_15pct: 0.78
      # Ctrl-contam results (Qwen3.5-9B)
      bbh_cohens_d_15pct: -3.21
      math_cohens_d_15pct: -2.88
      bbh_memorization_fraction: 0.40
      math_memorization_fraction: 0.36
      # Power theory fit (adding new points)
      R2_with_new_benchmarks: 0.968  # up from 0.957 with more data points
      # Dose-response
      bbh_dose_response_monotonic_theta_fixed: true
      math_dose_response_monotonic_theta_fixed: true
      bbh_theta_fixed_ratio: 2.72
      math_theta_fixed_ratio: 2.58
    result_rationale: >
      BBH（6511 items）和 MATH（5000 items）填充了 GSM8K（1319）和 MMLU（14042）之间的 gap。
      在 best 档下，两者都产生显著检测信号：BBH 因为 items 多且区分度高（BIG-Bench Hard 的 items
      被设计为 challenging），theoretical power 接近 90%；MATH 的 items 更结构化（数学题），
      memorization fraction 稍低（0.36 vs 0.40）因为数学题的 SFT 更容易产生 generalization
      而非 verbatim memorization。两者的加入使 power function 的 R² 从 0.957 提升到 0.968，
      进一步验证了 Claim 2 的 power ∝ f(n_items) 关系。这些中等规模 benchmarks
      是实际应用中最常见的尺寸范围（多数 benchmarks 在 1K-10K 之间），因此验证至关重要。
    tables:
      - name: "Table: Extended Power Function Validation"
        columns: [benchmark, n_items, theoretical_power_15pct, actual_power_ctrl, cohens_d_15pct]
        rows:
          - [MMLU, 14042, 0.985, 0.92, -3.95]
          - [HellaSwag, 10042, 0.753, 0.71, -2.64]
          - [BBH, 6511, 0.88, 0.85, -3.21]
          - [MATH, 5000, 0.82, 0.78, -2.88]
          - [GSM8K, 1319, 0.59, 0.55, -1.42]
    figures_description:
      - "Fig: Updated power function curve with 5 benchmark points (adding BBH, MATH), showing improved R²=0.968 fit"
      - "Fig: Detection signal (|Cohen's d|) vs n_items scatter plot, confirming monotonic relationship"
    analysis: >
      BBH 和 MATH 的加入完善了 power function 的中间区段验证。5 个 benchmarks 覆盖了
      1.3K 到 14K items 的完整范围，R²=0.968 确认 power 与 √n 的理论关系在实际 ctrl-contam 中成立。
      这直接支撑 Claim 2 的核心论断：detection power is a predictable function of benchmark size。

  - name: "Natural Experiment (base→chat pairs)"
    plan_id: "exp-natural-experiment"
    description: >
      v1 leaderboard base→chat model pairs 计算 Δlz* = lz*(chat) - lz*(base) 作为 SFT 效应代理。
    expected_results:
      n_pairs: 21
      n_complete_pairs: 9
      hellaswag_systematic_effect:
        mean_deviation: -3.8
        t_stat: -4.2
        p_value: 0.0008
        direction: "SFT decreases person-fit"
      gsm8k_systematic_effect:
        mean_deviation: 4.5
        t_stat: 3.8
        p_value: 0.004
        direction: "SFT increases person-fit"
      mmlu_effect:
        p_value: 0.12
        direction: "non-significant"
      arc_c_effect:
        p_value: 0.31
        direction: "non-significant"
      individual_outlier_pairs: 1  # one pair with extreme Δlz* suggesting possible contamination
      outlier_model: "codellama-34b-instruct"
      outlier_benchmark: "GSM8K"
      outlier_delta_lz: 8.7
    result_rationale: >
      Best 档下 natural experiment 的结果比 registry 中的实际结果稍强：HellaSwag 和 GSM8K
      显示更清晰的 systematic SFT effect（p<0.001 和 p<0.005），且出现一个 individual outlier
      （codellama-34b-instruct 在 GSM8K 上 Δlz*=8.7，远超 group mean）。这个 outlier
      的出现是 best 档独有的——它提供了 "自然实验中发现疑似污染" 的 case study evidence。
      HellaSwag 的 negative shift 解释：chat SFT 训练中包含了对话/常识推理数据，
      这些与 HellaSwag 的 commonsense completion task 有 domain overlap，导致泛化性提升
      但 pattern 变得 less aberrant（更符合 IRT 预测）。GSM8K positive shift：
      chat 模型的 math instruction tuning 不是 benchmark-specific memorization
      而是 reasoning capability，但少数模型可能直接接触了 GSM8K items。
      由于 a_r=0.111 的 discrimination failure，此实验只能作为 converging evidence，不是 primary claim。
    tables:
      - name: "Table: Systematic SFT Effects on lz* (base→chat)"
        columns: [benchmark, n_pairs, mean_Δlz, t_stat, p_value, interpretation]
        rows:
          - [HellaSwag, 9, -3.8, -4.2, 0.0008, "SFT improves commonsense (less aberrant)"]
          - [GSM8K, 9, 4.5, 3.8, 0.004, "Math SFT creates new aberrance patterns"]
          - [MMLU, 9, 1.8, 1.7, 0.12, "n.s."]
          - [ARC-C, 9, 0.9, 1.1, 0.31, "n.s."]
    figures_description:
      - "Fig: Paired Δlz* plot (base→chat) for each benchmark, with individual pair lines and group mean ± CI"
    analysis: >
      P2-optional 实验。提供了 real-world SFT 效应的 converging evidence，但受限于 a_r=0.111
      的 discrimination failure。在 paper 中作为 supplementary finding 而非 primary evidence。

  - name: "V1 IRT Refit Expanded (N=178)"
    plan_id: "exp-v1-irt-refit-expanded"
    description: >
      扩大 v1 IRT 重拟合样本量至 N≥178，最终验证 Path D（large-scale audit）是否可行。
    expected_results:
      n_models: 178
      n_items: 14042
      3pl_a_pearson_r: 0.13
      2pl_a_pearson_r: -0.03
      3pl_b_pearson_r: 0.66
      a_r_below_threshold: true  # a_r=0.13 < 0.2 threshold → Path D dead
      conclusion: "Path D confirmed dead. Classical MML-EM cannot recover IRT discrimination from LLM response data at available sample sizes."
    result_rationale: >
      即使在 best 档，Path D（leaderboard-scale audit via classical IRT refit）仍然失败。
      这不是 experiment failure 而是 honest negative result：classical IRT estimation
      需要 hundreds of examinees with similar ability distributions，而 LLM response data
      的特殊性（模型间 ability range 极大，item response 非 locally independent）
      使得 MML-EM 无法恢复 discrimination parameters。a_r=0.13 << 0.4 threshold
      确认 discriminability failure 不是样本量问题而是 structural incompatibility。
      这本身是 Claim 3(c) 的贡献：quantifying the estimation challenge for neural IRT。
    tables:
      - name: "Table: IRT Parameter Recovery (Classical vs PSN-IRT)"
        columns: [method, N_models, a_pearson_r, b_pearson_r, conclusion]
        rows:
          - [MML-EM 3PL (N=63), 63, 0.111, 0.626, "a failure"]
          - [MML-EM 3PL (N=178), 178, 0.13, 0.66, "a failure persists"]
          - [PSN-IRT (neural), 12, "validated", "validated", "reference standard"]
    figures_description:
      - "Fig: Scatter plot of MML-EM a_hat vs PSN-IRT a_true for N=178, showing near-zero correlation"
    analysis: >
      Path D 的确定性关闭是 paper structure 的关键节点。它确立了 "why ctrl-contam, not leaderboard audit"
      的 methodological justification，并为 Future Work 中的 "neural IRT at scale" 提供了动机。

  - name: "4PL vs 3PL Ablation"
    plan_id: "exp-4pl-ablation"
    description: >
      4PL vs 3PL(d=1) 消融实验：量化 d 参数对检测灵敏度的影响。
    expected_results:
      mean_power_gain_4pl_vs_3pl:
        MMLU: "+28pp"
        HellaSwag: "+27pp"
        GSM8K: "+21pp"
        ARC_C: "+15pp"
        HumanEval: "+14pp"
      far_4pl: 0.05
      far_3pl: "0.05-0.17 (inflated)"
      far_2pl: "0.50-1.00 (catastrophic)"
      items_with_d_lt_095_mmlu: "46%"
      # Ctrl-contam confirmation
      ctrl_contam_4pl_d_15pct: -3.95
      ctrl_contam_3pl_d_15pct: -1.82
      power_loss_without_d: "54%"
    result_rationale: >
      4PL 的 d 参数（upper asymptote）对高能力 LLM 至关重要：当 d<1 时，P(correct) 的上限低于 1.0，
      高能力模型在这些 items 上 "应该" 答错（按 4PL 预测）。如果忽略 d（设 d=1），
      model 预测所有高能力模型都应该答对所有题——这会让 few errors 变成 extreme aberrance（false alarm）。
      MMLU 46% items 有 d<0.95 意味着将近一半的题目有上限效应，忽略这些会产生巨大的 FAR 膨胀。
      在 best 档下，ctrl-contam 进一步确认：同一污染实验用 3PL 分析时 |d| 从 3.95 降到 1.82，
      因为 3PL 的 inflated null variance 稀释了真实信号。这证明 4PL 不是 "nice-to-have"
      而是 LLM person-fit 分析的 necessary condition。
    tables:
      - name: "Table: 4PL vs 3PL Detection Performance"
        columns: [benchmark, n_items, power_4pl_25pct, power_3pl_25pct, gain, pct_items_d_lt_095]
        rows:
          - [MMLU, 14042, 0.776, 0.329, "+44.7pp", "46%"]
          - [HellaSwag, 10042, 0.534, 0.280, "+25.4pp", "38%"]
          - [GSM8K, 1319, 0.730, 0.334, "+39.6pp", "42%"]
          - [ARC-C, 295, 0.132, 0.091, "+4.1pp", "29%"]
          - [HumanEval, 164, 0.318, 0.165, "+15.3pp", "35%"]
    figures_description:
      - "Fig: Power comparison curves (4PL solid, 3PL dashed) across contamination levels for each benchmark"
      - "Fig: Item-level analysis — d parameter distribution histogram with 0.95 threshold marked"
    analysis: >
      4PL ablation 是 methodological rigor 的体现。Reviewer 可能质疑 "为什么不用更简单的 3PL"，
      此实验给出定量答案：+28pp average power gain，54% signal loss without d。
      结合 exp-4pl-real-data-degradation（r=0.225 between 4PL/3PL lz*），
      establishes 4PL 作为 LLM person-fit 的 minimum viable parameterization。

  - name: "Baseline Comparison — Accuracy Z-Score (completed)"
    plan_id: "exp-baseline-comparison"
    description: >
      Accuracy z-score 作为 same-level binary-only baseline 的扩展对比，
      整合入完整 baseline comparison 实验中。
    expected_results:
      # Already have: z_flagged 4/60 vs lz_flagged 57/60
      # Extended to ctrl-contam
      acc_zscore_auroc_5pct: 0.55
      acc_zscore_auroc_10pct: 0.63
      acc_zscore_auroc_15pct: 0.71
      acc_zscore_auroc_25pct: 0.78
      lz_star_advantage_over_zscore_5pct: "+0.23 AUROC"
      lz_star_advantage_over_zscore_15pct: "+0.21 AUROC"
      lz_star_advantage_over_zscore_25pct: "+0.16 AUROC"
    result_rationale: >
      Accuracy z-score 只利用 total score（sum of binary responses）而丢失所有 item-level
      pattern information。lz* 的优势正来自于 item-level aberrance detection：
      它区分 "总分高因为答对了该对的题" vs "总分高因为答对了不该对的题"。
      在 5% 低污染时，只有 ~700 items（14042×5%）被 contaminate，total score change 微乎其微
      （+2-3 pp accuracy），z-score 几乎无法检测。但 lz* 能捕捉到这 700 items 中的 "不可能正确" 模式。
      这是 "IRT structure as inductive bias" 的最直接证明。
    tables: []
    figures_description:
      - "Fig: lz* vs accuracy z-score ROC curves at 5% and 15% contamination, showing consistent lz* advantage"
    analysis: >
      Accuracy z-score 是 "straw-man" 但也是 fair comparison：它是唯一的 same-information-level baseline
      （binary only, no training data）。lz* 的 consistent +0.16-0.23 AUROC advantage
      直接证明 IRT item parameters 提供了有价值的 structural information。

  - name: "Domain-Level Analysis"
    plan_id: "exp-domain-analysis"
    description: >
      MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别污染的 domain 分布。
    expected_results:
      # Gemini analysis
      gemini_subjects_flagged: "50/57 (87.7%)"
      gemini_contamination_uniform: true
      gemini_category_lz_range: [15.3, 21.2]
      # Ctrl-contam domain analysis
      ctrl_contam_domain_uniformity: "uniform (as expected, since QLoRA trains on random 15% sample)"
      ctrl_contam_stem_lz: 3.8
      ctrl_contam_humanities_lz: 3.3
      ctrl_contam_social_sci_lz: 3.5
      ctrl_contam_other_lz: 3.2
      # Doubao negative pattern
      doubao_selective_domains: true
      doubao_negative_pattern: "STEM and Humanities strongly negative, Other positive"
    result_rationale: >
      Domain analysis 在 best 档下产生两个 clear findings：(1) Gemini-1.5 的 contamination
      是 uniform across domains（所有 subject 都被 memorize），consistent with "bulk training data leak"
      而非 "selective domain tuning"；(2) ctrl-contam 模型的 domain-level signal 也是 uniform
      （因为 QLoRA 训练样本是 randomly sampled across all subjects），验证了实验设计的 internal consistency。
      Doubao 的 selective negative pattern 则展示了不同类型的 anomaly：可能是 domain-specific
      training data 导致某些 domains 泛化过强（lz*<0 = over-consistent pattern）。
    tables:
      - name: "Table: MMLU Domain-Level lz* (Gemini-1.5 vs Ctrl-Contam)"
        columns: [domain, gemini_lz, ctrl_contam_15_lz, ctrl_contam_clean_lz]
        rows:
          - [STEM, 21.2, 3.8, 0.1]
          - [Humanities, 17.9, 3.3, -0.2]
          - [Social Sciences, 15.9, 3.5, 0.0]
          - [Other, 15.3, 3.2, 0.1]
    figures_description:
      - "Fig: Heatmap of domain-level lz* across models (rows=models, cols=57 MMLU subjects), color=lz*"
      - "Fig: Ctrl-contam domain uniformity test — bar chart showing no significant domain variation (χ² test)"
    analysis: >
      Domain analysis 提供了 contamination 的 "spatial resolution"：从 aggregate model-level detection
      到 domain-level localization。在 paper 中服务于两个目的：(a) 验证 ctrl-contam 内部一致性
      （random sampling → uniform signal），(b) case study 中展示不同 contamination type 的 domain fingerprint。

  - name: "Leaderboard Audit (Abandoned)"
    plan_id: "exp-leaderboard-audit"
    description: >
      Open LLM Leaderboard v1 大规模 13K+ 模型扫描。因 IRT refit failure 放弃。
    expected_results:
      status: "ABANDONED"
      reason: "a_r=0.111 discrimination failure makes lz* degenerate to accuracy-like metric at scale"
      paper_treatment: "Data availability noted in Discussion/Future Work; 13K+ per-item data available for future neural IRT estimation"
    result_rationale: >
      即使在 best 档，leaderboard audit 仍然 abandoned。这不影响 best 档的叙事，
      因为 ctrl-contam 提供了比 leaderboard audit 更强的 ground-truth validation。
      Audit 的 abandonment 本身是 honest negative result (Claim 3c)：classical IRT 的
      sample size requirement 与 LLM evaluation ecosystem 不兼容。
      Paper 中将其定位为 "future work when neural IRT estimation at scale becomes feasible"。
    tables: []
    figures_description: []
    analysis: >
      ABANDONED。在 paper 中转化为 methodological contribution：量化了 classical vs neural IRT
      在 LLM context 中的 gap，为 future work 提供了 concrete roadmap（13K+ data available,
      awaiting better estimation methods）。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26b7e67b-4c71-47c1-95c2-512739e1ac37",
  "isSidechain": false,
  "requestId": "req_011CbELm2qcJHacMAtmXb46Q",
  "type": "assistant",
  "uuid": "ae68afb6-c614-4486-a2bc-910bd2dbc216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H91hv3nidN6jZW1ZSUQcZ6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20980,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16880,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20980
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Multi-model ctrl-contam 全面成功 + post-RL 信号存活 + lz* 在低污染率胜出所有 baselines 核心假设：['SFT memorization fingerprint跨模型家族一致：4/4 模型在 15% 污染下均产生显著 Δlz*', 'θ-fixed 策略普适：…",
  "leafUuid": "ae68afb6-c614-4486-a2bc-910bd2dbc216",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Controlled contamination validation with theta-fixed analysis",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Multi-model ctrl-contam 全面成功 + post-RL 信号存活 + lz* 在低污染率胜出所有 baselines 核心假设：['SFT memorization fingerprint跨模型家族一致：4/4 模型在 15% 污染下均产生显著 Δlz*', 'θ-fixed 策略普适：…",
  "leafUuid": "ae68afb6-c614-4486-a2bc-910bd2dbc216",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Controlled contamination validation with theta-fixed analysis",
  "sessionId": "f2b2a593-b75c-4715-93ab-89b246ef4019"
}
```

---
