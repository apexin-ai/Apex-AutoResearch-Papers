# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心检测有效但存在边界条件：部分家族/benchmark 信号较弱，post-RL 不确定，baseline 对比有差距 核心假设：['ctrl-c

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-3/64734155-0bc9-4993-a914-3c67248a3bb1.jsonl`
- **Structured JSON:** [`440c67b78c3965d10c55.json`](../../sessions/44/440c67b78c3965d10c55.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:36:54.266Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:36:54.266Z",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心检测有效但存在边界条件：部分家族/benchmark 信号较弱，post-RL 不确定，baseline 对比有差距\n核心假设：['ctrl-contam 在 3/4 家族有效（|d|>2.0 @ 15%），1 家族信号较弱（|d| 1.0-2.0）', 'MMLU 检测强劲，HellaSwag/GSM8K 效果显著但 d 值较低（受 n_items 和 4PL 参数质量制约）', 'θ-fixed 在多数家族恢复单调性，但 1-2 家族仍有残余非单调性', 'post-RL 实验：信号衰减但未消失（|d| 0.5-1.5），或实验未能在 DDL 前完成', 'baseline 对比：lz* 在 5-10% 低污染区间优势明确，但 15%+ 区间落后于 MinK%++/ConStat 10-15% AUROC', 'memorization fraction 家族间有差异（25-45%），理论 power 上界与实测有系统性 gap']\n关键指标范围：{'ctrl_contam_cohens_d_15pct_min_across_families': [1.0, 2.5], 'ctrl_contam_cohens_d_15pct_mean_across_families': [2.0, 3.0], 'n_families_d_gt_2': [2, 3], 'multi_benchmark_cohens_d_15pct_hellaswag': [0.8, 1.5], 'multi_benchmark_cohens_d_15pct_gsm8k': [0.5, 1.2], 'baseline_auroc_gap_at_15pct_vs_best_privileged': [-0.15, -0.05], 'baseline_auroc_lz_at_5pct': [0.6, 0.7], 'post_rl_cohens_d_15pct': [0.5, 1.5], 'theta_fixed_monotonic_families': [2, 3], 'memorization_fraction_range': [0.25, 0.45], 'power_theory_vs_observed_R2': [0.75, 0.9]}\n叙事方向：Claim 1 调整为 \"principled detection framework with characterized operating conditions\" ——检测有效但需要显式报告边界条件（家族依赖性、benchmark 大小阈值、θ-fixed 要求）。Claim 2 不变但增加 caveats：理论 power 是上界，SFT generalization gap 是 benchmark- 和 family-dependent 的。 Claim 3 增强 θ-shift 贡献的权重（从 methodological finding 升级为 core contribution）—— \"我们不仅检测，更 characterize detection 的成功和失败条件\"。Post-RL 如果不完整，降为 Discussion 中的 \"structural argument + preliminary evidence\"，不列入 Claim。Baseline 对比诚实报告 information-access vs detection-power tradeoff curve，强调 \"minimal-information operating point\" 的价值而非绝对性能。EMNLP 仍可投，但需要更强的 characterization 叙事来补偿 detection power 的不完美。标题可能从 \"Detection\" 调整为 \"Detection and Characterization\"。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_personfit_contam\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.\n6. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n7. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.\n- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = \"θ_fixed repairs non-monotonicity\"; Llama story = \"θ_fixed enhances existing monotonicity\". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-two-sided\n  registry_id: exp-two-sided\n  claim: 2\n  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case\n    study）。包括 bootstrap confidence interval 和 FDR 控制。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- id: exp-extended-sim\n  registry_id: exp-extended-sim\n  claim: 2\n  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让\n    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向\n    lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 依赖 exp-two-sided 的双侧框架定义。\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- id: exp-ctrl-contam-pilot\n  claim: 1,2,3\n  description: 快速验证：Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU only。测量\n    Δlz*(clean→contaminated) 是否显著。增加第二个 0% seed 作为 clean-vs-clean noise floor baseline\n    (Reviewer Q2/Q4)。Eval 时区分 seen/unseen items 以实测 memorization fraction (Reviewer\n    Q3/W9)。这是论文 go/no-go 信号。\n  priority: P0-CRITICAL\n  gpu_budget_hours: 12\n  deps: []\n  status: planned\n  notes: 'GPU 恢复后第一优先。4 conditions × ~3 hrs = ~12 GPU-hrs (+2h for second 0% seed)。关键输出:\n    (a) Δlz* 显著性, (b) clean-vs-clean Δlz* ≈ 0 验证, (c) memorization fraction = (Δacc_seen\n    - Δacc_unseen)/Δacc_seen, (d) adjusted power = theory × memorization fraction。D010\n    要求。'\n- id: exp-ctrl-contam\n  claim: 1,2,3\n  description: 完整控制实验：在 4 个模型上用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量\n    Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - exp-ctrl-contam-pilot\n  status: planned\n  notes: '模型: Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3。Benchmark:\n    MMLU + GSM8K + HellaSwag。4 模型 × 6 levels × 3 benchmarks。'\n- id: exp-empirical-null\n  registry_id: exp-empirical-null\n  claim: 1\n  description: Bootstrap empirical null 分析：量化 lz* 在真实 LLM 数据上的 systematic bias（null\n    mean ≠ 0, null std ≠ 1），为 Calibration Gap Analysis 提供定量证据。包含 Q-Q plots、KS tests、bias\n    量化表、unflagged cells 深度分析。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 复用 exp-two-sided v2 的 bootstrap 逻辑，但保存完整中间分布。~2h 开发+运行。\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- id: exp-power-theory\n  registry_id: exp-power-theory\n  claim: 2\n  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A\n    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: DONE\n  notes: 纯理论推导 + 数值验证。CPU only.\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- id: exp-leaderboard-data-recon\n  registry_id: exp-leaderboard-data-recon\n  claim: 3\n  description: Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results\n    是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item\n    data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: 纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- id: exp-leaderboard-audit\n  claim: 3\n  description: Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark\n    污染率随时间趋势。\n  priority: ABANDONED\n  gpu_budget_hours: 20\n  deps:\n  - exp-two-sided\n  - exp-leaderboard-data-recon\n  status: planned\n  notes: 'D011: v1-irt-refit a_r=0.111 + item alignment 54.56% → 13K audit 不可行。数据可用性写入\n    Discussion/Future Work。'\n- id: exp-natural-experiment\n  claim: 3\n  description: v1 leaderboard base→chat model pairs 自然实验：计算 Δlz* = lz*(chat) - lz*(base)\n    作为 SFT 效应代理。\n  priority: P2-optional\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: 'D013: a_r=0.111 导致 lz*≈accuracy-like, 仅 4-5 pairs 无统计检验能力。Reviewer 终审建议降级。'\n- id: exp-v1-irt-refit-expanded\n  claim: 3\n  description: 扩大 v1 IRT 重拟合样本量至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。最终关闭 Path\n    D。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: CPU only. Reviewer 要求 N≥500 才能最终结论 Path D。阈值：a_r>0.4=可行, a_r<0.2=dead。\n- id: exp-4pl-ablation\n  claim: 1\n  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter\n    d 对 false alarm 和 detection power 的影响。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\n- id: exp-baseline-comparison\n  claim: 1\n  description: '与现有方法对比（≥5 baselines）：在控制实验的 ground-truth contaminated models 上，比较\n    IRT-FIT vs baselines 的 AUROC/Type-I error。Baselines: (1) ConStat (re-test), (2)\n    Min-K%++ (token probs), (3) accuracy z-score (已完成, CPU), (4) PPL-based detection\n    (log-prob family 代表, 预期 RL-robust 测试中失败), (5) random baseline。量化 minimal-information\n    的代价（power 损失）。报告 bootstrap CIs（同行 6/8 不报告方差，这是我们的差异化优势）。'\n  priority: P0-end\n  gpu_budget_hours: 30\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: 蒸馏显示同行 baseline 中位数 ~5 个。accuracy z-score 已完成(CPU)。ConStat 需 re-test, Min-K%++\n    需 token probs, PPL 需 log-probs。exp-ctrl-contam 完成后立即执行。\n- id: exp-multiscale-lzm\n  claim: 1,3\n  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化\n    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要实现 lzm 公式。\n- id: exp-post-rl\n  claim: 1\n  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应\n    Wang et al. (2025) 的 MIA 失效问题。\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\n- id: exp-extra-benchmarks\n  claim: 2,3\n  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items\n    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\n- id: exp-domain-analysis\n  claim: 3\n  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5\n    的 MMLU 污染是全面的还是集中在特定 domain。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要 MMLU item-to-domain 映射。\n\n\n## registry (completed experiments)\n\n- exp_id: sim_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    null_check:\n      all_pass: true\n      gsm8k_ks_p: 0.098\n      hellaswag_ks_p: 0.224\n      mmlu_ks_p: 0.594\n    simulation_power_at_15pct:\n      mmlu: 0.979\n      hellaswag: 0.733\n      gsm8k: 0.578\n      arc_c: 0.129\n      humaneval: 0.243\n    global_pass: false\n    inverted_u_all_benchmarks: true\n    pass_count_large_80pct: 1/3 (mmlu only)\n- exp_id: phase_b_personfit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_sd_all_gt_0.5: true\n    mmlu_lz_star_mean: 24.19\n    mmlu_lz_star_sd: 16.47\n    hellaswag_lz_star_mean: 20.09\n    hellaswag_lz_star_sd: 17.59\n    gsm8k_lz_star_mean: 8.22\n    gsm8k_lz_star_sd: 8.97\n    gemini15_mmlu_lz_star: 34.75\n    gemini15_mmlu_accuracy: 1\n    gemini15_mmlu_theta: 0.78\n    gemini15_flagged_benchmarks: 3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\n    cross_benchmark_spearman_significant: 1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\n    n_models: 12\n    n_benchmarks: 5\n- exp_id: exp-two-sided\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- exp_id: exp-extended-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- exp_id: exp-empirical-null\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- exp_id: exp-leaderboard-data-recon\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- exp_id: exp-power-theory\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- exp_id: exp-item-alignment-check\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    match_rate_direct: 0.5456\n    match_rate_reordered_mistral: 0.8846\n    match_rate_reordered_vicuna: 0.7248\n    n_items_checked: 14042\n    n_models_verified: 2\n    alignment_method: content-based via cais/mmlu canonical order\n    items_mapped: 12068\n    mapping_coverage: 0.86\n- exp_id: exp-v1-irt-refit-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 63\n    n_models_failed: 38\n    n_items: 14042\n    n_mapped_items: 12441\n    overall_accuracy: 0.426\n    fitting_time_2pl_sec: 8.9\n    fitting_time_3pl_sec: 12.1\n    3pl_a_pearson_r: 0.111\n    3pl_b_pearson_r: 0.626\n    3pl_b_spearman_r: 0.656\n    2pl_a_pearson_r: -0.084\n    2pl_b_pearson_r: 0.572\n    lz_star_mean: 11.69\n    lz_star_std: 6.68\n    lz_star_flagged_pct: 1.6\n- exp_id: exp-accuracy-zscore-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_flagged_count: 4\n    lz_flagged_count: 57\n    agreement_rate: 0.117\n    gemini15_mmlu_zscore: 1.413\n- exp_id: exp-cross-benchmark-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_all5_flagged: 10\n    n_models_selective_flagged: 2\n    gemini15_cluster_isolation: true\n    dominant_direction_pattern: positive\n    pct_positive_cells: 93.3\n    total_flagged: 57\n    flag_rate: 0.95\n- exp_id: exp-ml-classifier-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    auroc_avg_25pct:\n      lz_star: 0.86\n      lr_resp: 0.899\n      rf_resp: 0.885\n      lr_resp_summ: 0.909\n      rf_resp_summ: 0.913\n    auroc_avg_5pct:\n      lz_star: 0.675\n      best_ml: 0.575\n    auroc_avg_10pct:\n      lz_star: 0.763\n      best_ml: 0.712\n    lz_star_advantage_low_contam: +0.10 AUROC at 5%, +0.05 at 10%\n    ml_advantage_high_contam: +0.05 at 25%, +0.16 at 50%\n    key_finding: lz* outperforms supervised ML at low contamination (5-10%) without\n      any training data; ML only wins at 25%+ where signal is already strong\n- exp_id: exp-fdr-correction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    flagged_uncorrected: 57/60 (95%)\n    flagged_bh_fdr: 57/60 (95%)\n    flagged_bonferroni: not_computed_but_expected_similar\n    correction_scope: global_60_tests\n    unflagged_cells:\n    - Yi-Lightning×arc_c (bh_p=0.098)\n    - 360GPT2-Pro×humaneval (bh_p=0.134)\n    - Yi-Lightning×humaneval (bh_p=0.181)\n    note: Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale\n      FDR (24800+ tests) deferred to leaderboard audit.\n- exp_id: exp-clean-control-delta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    clean_vs_clean_mean_abs:\n      mmlu: 0.01\n      hellaswag: 0.125\n      gsm8k: 0.021\n      arc_c: 0.095\n      humaneval: 0.02\n    clean_vs_clean_all_nonsig: true\n    clean_vs_contam_all_sig: true\n    cohens_d:\n      mmlu: 2.66\n      hellaswag: 1.85\n      gsm8k: 1.85\n      arc_c: 0.45\n      humaneval: 1.07\n    arc_c_note: d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10\n- exp_id: exp-natural-experiment\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 21\n    n_benchmarks: 4\n    n_complete_pairs: 9\n    significant_benchmarks:\n      HellaSwag:\n        mean_deviation: -3.4\n        t_stat: -3.97\n        p_value: 0.001\n        interpretation: SFT systematically decreases person-fit on HellaSwag\n      GSM8K:\n        mean_deviation: 3.92\n        t_stat: 3.35\n        p_value: 0.009\n        interpretation: SFT systematically increases person-fit on GSM8K\n    non_significant_benchmarks:\n      MMLU:\n        p_value: 0.15\n      ARC-Challenge:\n        p_value: 0.38\n    individual_outliers: 0\n    key_finding: HellaSwag and GSM8K show significant systematic SFT effects on lz*,\n      but no individual pair shows benchmark-specific contamination outliers. P2-optional\n      per Director assessment.\n- exp_id: exp-v1-irt-refit-expanded\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 178\n    n_items: 14042\n    3pl_a_pearson_r: 0.127\n    2pl_a_pearson_r: -0.029\n    3pl_b_pearson_r: 0.663\n    reason: 'N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination\n      failure confirms Path D dead.'\n- exp_id: exp-4pl-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hypothesis_confirmed: true\n    far_4pl: ~5% (well-calibrated)\n    far_3pl: 4.7-16.5% (inflated)\n    far_2pl: 50-100% (catastrophic, unusable)\n    mean_power_gain_4pl_vs_3pl:\n      MMLU: +27.3pp\n      HellaSwag: +26.1pp\n      GSM8K: +20.3pp\n      ARC_C: +14.8pp\n      HumanEval: +13.7pp\n    max_power_gain_4pl_vs_3pl:\n      MMLU: +49.0pp\n      HellaSwag: +59.6pp\n      GSM8K: +39.7pp\n      ARC_C: +54.6pp\n      HumanEval: +30.6pp\n    power_at_25pct:\n      4PL:\n        MMLU: 0.776\n        HellaSwag: 0.534\n        GSM8K: 0.73\n        ARC_C: 0.132\n        HumanEval: 0.318\n      3PL:\n        MMLU: 0.329\n        HellaSwag: 0.28\n        GSM8K: 0.334\n        ARC_C: 0.091\n        HumanEval: 0.165\n    d_bucket_analysis: 'd<0.8: +6.8pp to +61.2pp; d>=0.95: negligible'\n    key_finding: 4PL d parameter essential for LLM contamination detection. 46% MMLU\n      items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely\n      miscalibrated (FAR 50-100%).\n- exp_id: exp-domain-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_mmlu_accuracy: 100% (14042/14042)\n    gemini_domain_concentrated: false\n    gemini_subjects_flagged: 50/57 (lz*>1.96)\n    gemini_category_lz:\n      STEM: 21.2\n      Humanities: 17.9\n      Social Sciences: 15.9\n      Other: 15.3\n    doubao_negative_lz: true\n    doubao_category_lz:\n      STEM: -2\n      Humanities: -13\n      Social_Sciences: -14.8\n      Other: 4.4\n    hunyuan_uneven:\n      STEM: 1.8\n      Social_Sciences: 13.9\n    yi_lightning_highest_mmlu_lz: 48.2\n    qwen_plus_second_highest: 44.9\n    mistral_flagged_subjects: 55/57\n- exp_id: exp-ctrl-contam-pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_corrected: true\n    method: Snijders (2001) lz*\n    clean_s1_lz_star: 9.4676\n    clean_s2_lz_star: 7.0539\n    clean_s3_lz_star: 9.5293\n    clean_mean_lz_star: 8.6836\n    clean_std_lz_star: 1.4117\n    contam_15_lz_star: 3.8494\n    contam_50_lz_star: 7.2892\n    contam_15_delta_lz_star: -4.8342\n    contam_50_delta_lz_star: -1.3944\n    cohens_d_contam_15_ddof1: -3.42\n    cohens_d_contam_50_ddof1: -0.99\n    contam_15_acc: 0.731\n    contam_50_acc: 0.7643\n    clean_mean_acc: 0.6786\n- exp_id: exp-4pl-real-data-degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    correlation_4pl_vs_3pl:\n      pearson_r: 0.225\n      rmse: 68.41\n    most_affected_benchmark: MMLU (mean |Δlz*|=58.3, 46% items d<0.95)\n    most_affected_model: 'DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6'\n    low_ability_models_impact: '|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)'\n    bias_direction: 3PL systematically depresses high-ability models' lz* (d=1 makes\n      P→1, amplifying few-error aberrance)\n    key_finding: Ignoring d parameter makes lz* completely unreliable for high-ability\n      models — d-induced bias far exceeds any contamination signal\n- exp_id: exp-ctrl-contam-pilot-clean-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-clean-s2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-15\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-50\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-clean-s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: 8.0806\n    accuracy: 0.6783\n    theta_mle: -0.1068\n    cohens_d_n3:\n      contam_15:\n        delta: -4.34\n        d: -3.58\n      contam_50:\n        delta: -1.9\n        d: -1.56\n    baseline_n3:\n      mean: 7.3449\n      std: 1.2137\n    baseline_n2:\n      mean: 6.9771\n      std: 1.4609\n- exp_id: exp-ctrl-contam-llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_corrected: true\n    method: Snijders (2001) lz*\n    clean_lz_star: 0.8446\n    clean_s2_lz_star: -0.1823\n    clean_s3_lz_star: -1.0844\n    clean_mean_lz_star: -0.1407\n    clean_std_lz_star: 0.9652\n    clean_acc: 0.5914\n    clean_theta: -0.6661\n    contam_15_lz_star: -2.9922\n    contam_15_acc: 0.6654\n    contam_15_theta: -0.276\n    contam_15_delta_lz_star: -2.8515\n    contam_50_lz_star: -3.3313\n    contam_50_acc: 0.6983\n    contam_50_theta: -0.149\n    contam_50_delta_lz_star: -3.1906\n    cohens_d_contam_15_ddof1: -2.95\n    cohens_d_contam_50_ddof1: -3.31\n    theta_fixed: -0.666\n    contam_15_lz_star_fixed: 0.959\n    contam_50_lz_star_fixed: 1.172\n    dose_response_ratio_free: 1.09\n    dose_response_ratio_fixed: 2.87\n    monotonic_free: true\n    monotonic_fixed: true\n- exp_id: exp-ctrl-contam-llama-clean\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-llama-contam15\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-llama-contam50\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-llama-clean-s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -0.1823\n    acc: 0.5954\n    theta: -0.63\n    seed: 123\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-llama-clean-s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -1.0844\n    acc: 0.5943\n    theta: -0.64\n    seed: 456\n    method: Snijders (2001) lz*\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:36:54.269Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:36:54.269Z",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1"
}
```

---

## Round 1

13 recorded events

### User

_source line 3 · 2026-05-21T03:36:54.291Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心检测有效但存在边界条件：部分家族/benchmark 信号较弱，post-RL 不确定，baseline 对比有差距
核心假设：['ctrl-contam 在 3/4 家族有效（|d|>2.0 @ 15%），1 家族信号较弱（|d| 1.0-2.0）', 'MMLU 检测强劲，HellaSwag/GSM8K 效果显著但 d 值较低（受 n_items 和 4PL 参数质量制约）', 'θ-fixed 在多数家族恢复单调性，但 1-2 家族仍有残余非单调性', 'post-RL 实验：信号衰减但未消失（|d| 0.5-1.5），或实验未能在 DDL 前完成', 'baseline 对比：lz* 在 5-10% 低污染区间优势明确，但 15%+ 区间落后于 MinK%++/ConStat 10-15% AUROC', 'memorization fraction 家族间有差异（25-45%），理论 power 上界与实测有系统性 gap']
关键指标范围：{'ctrl_contam_cohens_d_15pct_min_across_families': [1.0, 2.5], 'ctrl_contam_cohens_d_15pct_mean_across_families': [2.0, 3.0], 'n_families_d_gt_2': [2, 3], 'multi_benchmark_cohens_d_15pct_hellaswag': [0.8, 1.5], 'multi_benchmark_cohens_d_15pct_gsm8k': [0.5, 1.2], 'baseline_auroc_gap_at_15pct_vs_best_privileged': [-0.15, -0.05], 'baseline_auroc_lz_at_5pct': [0.6, 0.7], 'post_rl_cohens_d_15pct': [0.5, 1.5], 'theta_fixed_monotonic_families': [2, 3], 'memorization_fraction_range': [0.25, 0.45], 'power_theory_vs_observed_R2': [0.75, 0.9]}
叙事方向：Claim 1 调整为 "principled detection framework with characterized operating conditions" ——检测有效但需要显式报告边界条件（家族依赖性、benchmark 大小阈值、θ-fixed 要求）。Claim 2 不变但增加 caveats：理论 power 是上界，SFT generalization gap 是 benchmark- 和 family-dependent 的。 Claim 3 增强 θ-shift 贡献的权重（从 methodological finding 升级为 core contribution）—— "我们不仅检测，更 characterize detection 的成功和失败条件"。Post-RL 如果不完整，降为 Discussion 中的 "structural argument + preliminary evidence"，不列入 Claim。Baseline 对比诚实报告 information-access vs detection-power tradeoff curve，强调 "minimal-information operating point" 的价值而非绝对性能。EMNLP 仍可投，但需要更强的 characterization 叙事来补偿 detection power 的不完美。标题可能从 "Detection" 调整为 "Detection and Characterization"。


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
IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.

**Claim 2 (Detection Characterization)**:
Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted ("expected") power. Both upper bound and adjusted power should be reported.

**Claim 3 (Empirical Findings from Real LLM Data)**:
Three empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.

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
- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.
- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).
- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.
- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.
- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = "θ_fixed repairs non-monotonicity"; Llama story = "θ_fixed enhances existing monotonicity". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.
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
    lz_star_corrected: true
    method: Snijders (2001) lz*
    clean_s1_lz_star: 9.4676
    clean_s2_lz_star: 7.0539
    clean_s3_lz_star: 9.5293
    clean_mean_lz_star: 8.6836
    clean_std_lz_star: 1.4117
    contam_15_lz_star: 3.8494
    contam_50_lz_star: 7.2892
    contam_15_delta_lz_star: -4.8342
    contam_50_delta_lz_star: -1.3944
    cohens_d_contam_15_ddof1: -3.42
    cohens_d_contam_50_ddof1: -0.99
    contam_15_acc: 0.731
    contam_50_acc: 0.7643
    clean_mean_acc: 0.6786
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
- exp_id: exp-ctrl-contam-pilot-clean-s3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star: 8.0806
    accuracy: 0.6783
    theta_mle: -0.1068
    cohens_d_n3:
      contam_15:
        delta: -4.34
        d: -3.58
      contam_50:
        delta: -1.9
        d: -1.56
    baseline_n3:
      mean: 7.3449
      std: 1.2137
    baseline_n2:
      mean: 6.9771
      std: 1.4609
- exp_id: exp-ctrl-contam-llama
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star_corrected: true
    method: Snijders (2001) lz*
    clean_lz_star: 0.8446
    clean_s2_lz_star: -0.1823
    clean_s3_lz_star: -1.0844
    clean_mean_lz_star: -0.1407
    clean_std_lz_star: 0.9652
    clean_acc: 0.5914
    clean_theta: -0.6661
    contam_15_lz_star: -2.9922
    contam_15_acc: 0.6654
    contam_15_theta: -0.276
    contam_15_delta_lz_star: -2.8515
    contam_50_lz_star: -3.3313
    contam_50_acc: 0.6983
    contam_50_theta: -0.149
    contam_50_delta_lz_star: -3.1906
    cohens_d_contam_15_ddof1: -2.95
    cohens_d_contam_50_ddof1: -3.31
    theta_fixed: -0.666
    contam_15_lz_star_fixed: 0.959
    contam_50_lz_star_fixed: 1.172
    dose_response_ratio_free: 1.09
    dose_response_ratio_fixed: 2.87
    monotonic_free: true
    monotonic_fixed: true
- exp_id: exp-ctrl-contam-llama-clean
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-ctrl-contam-llama-contam15
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics: {}
- exp_id: exp-ctrl-contam-llama-contam50
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics: {}
- exp_id: exp-ctrl-contam-llama-clean-s2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star: -0.1823
    acc: 0.5954
    theta: -0.63
    seed: 123
    method: Snijders (2001) lz*
- exp_id: exp-ctrl-contam-llama-clean-s3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star: -1.0844
    acc: 0.5943
    theta: -0.64
    seed: 456
    method: Snijders (2001) lz*

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
  "promptId": "7f3ddf52-feca-4862-8d0f-1bfb0c604740",
  "type": "user",
  "uuid": "a1d5f474-9f0d-48b3-8231-31a4c9bee135",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:36:54.289Z_

```json
{
  "parentUuid": "a1d5f474-9f0d-48b3-8231-31a4c9bee135",
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
  "uuid": "cc6d4570-ea45-4ada-9a16-8b62b8350126",
  "timestamp": "2026-05-21T03:36:54.289Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:36:54.289Z_

```json
{
  "parentUuid": "cc6d4570-ea45-4ada-9a16-8b62b8350126",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c044eb3a-1c57-4aa4-8c47-b9bf29e0b82b",
  "timestamp": "2026-05-21T03:36:54.289Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心检测有效但存在边界条件：部分家族/benchmark 信号较弱，post-RL 不确定，baseline 对比有差距 核心假设：['ctrl-contam 在 3/4 家族有效（|d|>2.0 @ 15%），1 家族信号较弱（|d| 1.0-2.0）', 'MMLU 检测强劲，HellaSwag/GS…",
  "leafUuid": "c044eb3a-1c57-4aa4-8c47-b9bf29e0b82b",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier IRT contamination detection with characterized operating conditions",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1"
}
```

---

### Assistant

_source line 8 · 2026-05-21T03:36:59.554Z_

I'll analyze the experiment plan and generate detailed median-tier predictions for each planned experiment. Let me first review the existing data and experiment details more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c044eb3a-1c57-4aa4-8c47-b9bf29e0b82b",
  "isSidechain": false,
  "requestId": "req_011CbF1qhK3JYRiZb4MGK5Ap",
  "type": "assistant",
  "uuid": "e1634a3d-8d96-45de-a7bc-792d4cecb176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147pFeX8FBvFbWFCEcHyHNx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22824,
      "cache_read_input_tokens": 11841,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 220,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22824
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

_source line 9 · 2026-05-21T03:37:02.815Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KVNJezBDX8pQ2f5qW9MbL3`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan files",
  "prompt": "Search the directory /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3 for any files related to experiment plans, registry, or results. Look for YAML, JSON, or markdown files that contain experiment definitions. Use a broad search: glob for *.yaml, *.yml, *.json, *.md in the project root and subdirectories. Report what you find with file paths and brief content descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1634a3d-8d96-45de-a7bc-792d4cecb176",
  "isSidechain": false,
  "requestId": "req_011CbF1qhK3JYRiZb4MGK5Ap",
  "type": "assistant",
  "uuid": "105f7f66-8ae5-46bb-a08b-157d267fc798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147pFeX8FBvFbWFCEcHyHNx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22824,
      "cache_read_input_tokens": 11841,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 220,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22824
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

_source line 10 · 2026-05-21T03:37:25.249Z_

<details><summary>↩ Tool result · `toolu_01KVNJezBDX8pQ2f5qW9MbL3`</summary>

```text
Perfect. Now I have a comprehensive view of the project. Let me compile my findings:

## Summary of Experiment-Related Files Found

I've completed a thorough search of the directory `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3` for experiment definitions, registry, and results files. Here are the key findings:

### Primary Experiment Planning & Registry Files

**Experiment Plan:**
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/experiment_plan.yaml` — Defines 25+ experiments organized by priority (P0/P0-CRITICAL/P1/P2), including contamination control studies, simulations, and baseline comparisons. GPU budget tracked (~122 GPU-hrs total). Includes detailed descriptions, dependencies, and status for each experiment.

**Experiment Registry:**
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/registry.yaml` — Master registry documenting 23 completed/running/planned experiments with full metadata: hypothesis, status, metrics, data paths, checkpoints, conclusions. Experiments include:
  - Simulation studies (sim_001, exp-extended-sim)
  - Real-world analysis (phase_b_personfit, exp-two-sided, exp-empirical-null)
  - Control experiments (exp-ctrl-contam-pilot with Qwen2.5-7B, exp-ctrl-contam-llama)
  - Baseline comparisons (exp-accuracy-zscore-baseline, exp-ml-classifier-baseline)
  - Theory validation (exp-power-theory)
  - Data reconnaissance (exp-leaderboard-data-recon, exp-item-alignment-check)

**Dream (Paper Planning) Registry:**
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/dream_registry.yaml` — Tracks 5 complete dream cycles (imagined paper proposals with reviewer simulations) from May 20-21, 2026. Includes status tracking, focus areas, and review quality assessments.

**Review Issues Tracker:**
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml` — Consolidated 20-issue tracker from simulated reviewer feedback with actionable/filtered/rejected categories, assignments, and resolution status. Critical issues include: presentation gaps, 4PL parameter source clarity, IRT assumption violations, and contamination detection framing.

### Configuration Files

- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/projects/irt_personfit_contam.yaml` — Project config with execution servers, GPU allocations, and venue (EMNLP 2026)
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/writing_plan.yaml` — Writing plan with director-approved action items (title: "IRT-FIT: Detecting LLM Benchmark Contamination via Person-Fit Statistics"), target score (3.0-3.25), and 13 critical/method/results action items

### Artifact Organization

Each completed experiment has structured outputs in `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/`:
- Experiment-specific JSON/YAML result files (simulation summaries, person-fit metrics)
- Generated reports (markdown analysis files, comparison reports)
- Checkpoint data (fitted parameters, analysis outputs)
- Dream-generated materials (paper framings, review reports, imagined experiments)

**Key Experiment Status Summary:**
- 16 experiments DONE (simulations, empirical analyses, baseline comparisons, Llama control study)
- 3 experiments RUNNING/ANALYZING (Llama contamination conditions)
- 25 experiments PLANNED/ABANDONED (full pipeline includes post-RL, multi-model expansion, leaderboard audit)

**GPU/Compute Investment:**
- ~16-17 GPU-hours completed (ctrl-contam-pilot + Llama variants)
- ~122 total GPU-hours budgeted for remaining P0/P1 experiments
- Infrastructure: 4x RTX 5090 32GB (bjb2 cluster) + AutoDL remote workers

This is a well-instrumented ML research project with comprehensive experiment tracking, integrated review management, and tight coupling between experimental design and paper writing requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "105f7f66-8ae5-46bb-a08b-157d267fc798",
  "isSidechain": false,
  "promptId": "7f3ddf52-feca-4862-8d0f-1bfb0c604740",
  "type": "user",
  "uuid": "79abadea-0be1-4361-b520-7b98e44b5450",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the directory /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3 for any files related to experiment plans, registry, or results. Look for YAML, JSON, or markdown files that contain experiment definitions. Use a broad search: glob for *.yaml, *.yml, *.json, *.md in the project root and subdirectories. Report what you find with file paths and brief content descriptions.",
    "agentId": "a5cb58112c77f7e7b",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now I have a comprehensive view of the project. Let me compile my findings:\n\n## Summary of Experiment-Related Files Found\n\nI've completed a thorough search of the directory `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3` for experiment definitions, registry, and results files. Here are the key findings:\n\n### Primary Experiment Planning & Registry Files\n\n**Experiment Plan:**\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/experiment_plan.yaml` — Defines 25+ experiments organized by priority (P0/P0-CRITICAL/P1/P2), including contamination control studies, simulations, and baseline comparisons. GPU budget tracked (~122 GPU-hrs total). Includes detailed descriptions, dependencies, and status for each experiment.\n\n**Experiment Registry:**\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/registry.yaml` — Master registry documenting 23 completed/running/planned experiments with full metadata: hypothesis, status, metrics, data paths, checkpoints, conclusions. Experiments include:\n  - Simulation studies (sim_001, exp-extended-sim)\n  - Real-world analysis (phase_b_personfit, exp-two-sided, exp-empirical-null)\n  - Control experiments (exp-ctrl-contam-pilot with Qwen2.5-7B, exp-ctrl-contam-llama)\n  - Baseline comparisons (exp-accuracy-zscore-baseline, exp-ml-classifier-baseline)\n  - Theory validation (exp-power-theory)\n  - Data reconnaissance (exp-leaderboard-data-recon, exp-item-alignment-check)\n\n**Dream (Paper Planning) Registry:**\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/dream_registry.yaml` — Tracks 5 complete dream cycles (imagined paper proposals with reviewer simulations) from May 20-21, 2026. Includes status tracking, focus areas, and review quality assessments.\n\n**Review Issues Tracker:**\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/review_issues.yaml` — Consolidated 20-issue tracker from simulated reviewer feedback with actionable/filtered/rejected categories, assignments, and resolution status. Critical issues include: presentation gaps, 4PL parameter source clarity, IRT assumption violations, and contamination detection framing.\n\n### Configuration Files\n\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/config/projects/irt_personfit_contam.yaml` — Project config with execution servers, GPU allocations, and venue (EMNLP 2026)\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/writing_plan.yaml` — Writing plan with director-approved action items (title: \"IRT-FIT: Detecting LLM Benchmark Contamination via Person-Fit Statistics\"), target score (3.0-3.25), and 13 critical/method/results action items\n\n### Artifact Organization\n\nEach completed experiment has structured outputs in `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/`:\n- Experiment-specific JSON/YAML result files (simulation summaries, person-fit metrics)\n- Generated reports (markdown analysis files, comparison reports)\n- Checkpoint data (fitted parameters, analysis outputs)\n- Dream-generated materials (paper framings, review reports, imagined experiments)\n\n**Key Experiment Status Summary:**\n- 16 experiments DONE (simulations, empirical analyses, baseline comparisons, Llama control study)\n- 3 experiments RUNNING/ANALYZING (Llama contamination conditions)\n- 25 experiments PLANNED/ABANDONED (full pipeline includes post-RL, multi-model expansion, leaderboard audit)\n\n**GPU/Compute Investment:**\n- ~16-17 GPU-hours completed (ctrl-contam-pilot + Llama variants)\n- ~122 total GPU-hours budgeted for remaining P0/P1 experiments\n- Infrastructure: 4x RTX 5090 32GB (bjb2 cluster) + AutoDL remote workers\n\nThis is a well-instrumented ML research project with comprehensive experiment tracking, integrated review management, and tight coupling between experimental design and paper writing requirements."
      }
    ],
    "totalDurationMs": 22428,
    "totalTokens": 63237,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 59907,
      "output_tokens": 1095,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1095,
          "cache_read_input_tokens": 59907,
          "cache_creation_input_tokens": 2228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2228,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 4,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "105f7f66-8ae5-46bb-a08b-157d267fc798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T03:41:17.977Z_

Now let me generate the detailed median-tier predictions for every planned experiment.

```yaml
tier: median
narrative_guidance: >
  Median 档叙事核心："principled detection framework with characterized operating conditions"。
  ctrl-contam 在 3/4 家族有效（|d|>2.0 @ 15%），1 家族信号较弱。MMLU 检测强劲，HellaSwag/GSM8K 效果显著但 d 值较低。
  θ-fixed 在多数家族恢复单调性但 1-2 家族仍有残余非单调性。post-RL 信号衰减但未消失或实验未完成。
  baseline 对比在 5-10% 低污染区间优势明确，但 15%+ 落后于特权方法。
  标题从 "Detection" 调整为 "Detection and Characterization"，强调边界条件的系统刻画。

imagined_experiments:
  # =========================================================================
  # exp-ctrl-contam-pilot (P0-CRITICAL) — 已有 Qwen 数据，此处预测原始 plan 的 Qwen3.5-9B
  # =========================================================================
  - name: "ctrl-contam-pilot (Qwen3.5-9B × MMLU quick validation)"
    plan_id: "exp-ctrl-contam-pilot"
    description: >
      Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU。
      实际已在 Qwen2.5-7B-Instruct 上完成（|d|=3.42 @ 15%），此处预测原 plan 中 Qwen3.5-9B 的表现。
      Median 档下 Qwen3.5 作为更强模型，baseline misfit 更高，检测仍有效但 d 值略有调整。
    expected_results:
      clean_seed1_lz_star: 10.2
      clean_seed2_lz_star: 8.4
      clean_mean_lz_star: 9.3
      clean_std_lz_star: 1.27
      contam_15_lz_star: 5.1
      contam_50_lz_star: 8.0
      contam_15_delta_lz_star: -4.2
      contam_50_delta_lz_star: -1.3
      cohens_d_contam_15: -3.3
      cohens_d_contam_50: -1.0
      clean_vs_clean_delta: 0.02
      memorization_fraction_15pct: 0.36
      memorization_fraction_50pct: 0.28
      contam_15_acc: 0.74
      contam_50_acc: 0.78
      clean_mean_acc: 0.70
    result_rationale: >
      Qwen3.5-9B 比 Qwen2.5-7B 参数量更大、baseline 能力更强，因此 clean lz* 更高（~9.3 vs 8.68）——
      更强模型在 4PL 下的 misfit 更大。15% 污染 d≈3.3 仍为 large effect，因为 memorization fingerprint
      机制不依赖模型大小：SFT 注入的 seen items 被记忆，unseen items 模式不变，Δlz* 主要由 memorization
      fraction 驱动。50% 条件下 θ-shift 效应更强（更多 items 被记忆 → θ_MLE 上移更多 → 吸收 aberrance），
      导致 free-θ d 值仅约 1.0，重现 Qwen2.5 的非单调性。clean-vs-clean Δ≈0 验证 noise floor。
      memorization_fraction ~0.36 与 Qwen2.5 的 0.38 一致——SFT generalization gap 是
      benchmark-dependent 而非 model-dependent 的性质。
    tables:
      - name: "Table: Qwen3.5-9B Pilot Results"
        columns: ["Condition", "lz*", "Δlz*", "Cohen's d", "Accuracy", "θ_MLE"]
        rows:
          - ["clean-s1", "10.2", "—", "—", "0.698", "-0.08"]
          - ["clean-s2", "8.4", "—", "—", "0.702", "-0.10"]
          - ["contam_15", "5.1", "-4.2", "-3.3", "0.740", "0.12"]
          - ["contam_50", "8.0", "-1.3", "-1.0", "0.780", "0.38"]
    figures_description:
      - "Bar chart: clean vs contam_15 vs contam_50 的 lz* 值，error bar 为 clean seeds 的 ±1 SD"
      - "Scatter: seen vs unseen items 的 accuracy difference，标注 memorization fraction"
    analysis: >
      Go/no-go 信号明确：15% 污染 |d|>3 确认 person-fit 能检测 SFT 污染。
      但 50% 非单调性暴露 θ-shift boundary condition，需要 θ-fixed 分析。
      Median 档下这是 "principled detection with characterized operating conditions" 的起点。

  # =========================================================================
  # exp-ctrl-contam (P0) — 完整 4 家族 × 6 levels × 3 benchmarks
  # =========================================================================
  - name: "ctrl-contam full (4 families × 6 levels × 3 benchmarks)"
    plan_id: "exp-ctrl-contam"
    description: >
      Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3，
      0%/5%/10%/15%/25%/50% × MMLU + GSM8K + HellaSwag。
      Median 档：3/4 家族 MMLU |d|>2.0 @ 15%，1 家族较弱（|d| 1.0-2.0）；
      GSM8K/HellaSwag d 值系统性低于 MMLU。
    expected_results:
      # --- MMLU @ 15% contamination ---
      ctrl_contam_cohens_d_15pct_qwen: -3.2
      ctrl_contam_cohens_d_15pct_llama: -2.9
      ctrl_contam_cohens_d_15pct_gemma: -2.4
      ctrl_contam_cohens_d_15pct_mistral: -1.5
      ctrl_contam_cohens_d_15pct_mean: -2.5
      ctrl_contam_cohens_d_15pct_min: -1.5
      n_families_d_gt_2_at_15pct: 3
      # --- MMLU @ 5% contamination ---
      ctrl_contam_cohens_d_5pct_mean: -0.8
      # --- MMLU @ 50% contamination (free-θ) ---
      ctrl_contam_cohens_d_50pct_qwen: -1.0
      ctrl_contam_cohens_d_50pct_llama: -3.3
      ctrl_contam_cohens_d_50pct_gemma: -1.8
      ctrl_contam_cohens_d_50pct_mistral: -0.7
      # --- HellaSwag @ 15% ---
      hellaswag_cohens_d_15pct_mean: -1.2
      hellaswag_cohens_d_15pct_min: -0.6
      # --- GSM8K @ 15% ---
      gsm8k_cohens_d_15pct_mean: -0.9
      gsm8k_cohens_d_15pct_min: -0.4
      # --- θ-fixed ---
      theta_fixed_monotonic_families_mmlu: 3
      theta_fixed_monotonic_families_total: 3
      theta_fixed_non_monotonic_residual_families: 1
      # --- memorization ---
      memorization_fraction_range: [0.28, 0.42]
      memorization_fraction_mean: 0.35
      # --- dose-response ---
      dose_response_monotonic_free_theta: 2  # out of 4 families
      dose_response_monotonic_fixed_theta: 3  # out of 4
    result_rationale: >
      **3/4 家族 MMLU |d|>2.0 的理由**：Qwen 和 Llama 已验证（d=3.42/2.95），Gemma-4-31B 作为
      大模型预期 baseline misfit 高但 memorization fraction 类似，d≈2.4。Mistral-7B-v0.3 是
      weakest family：(a) Mistral v0.3 是较早的 base model，instruction following 能力较弱，
      QLoRA SFT 可能产生更多 generalization（而非 memorization），降低 memorization fraction 到 ~0.28；
      (b) 较低的 baseline 能力意味着即使 clean 状态下 lz* 方差也更大，稀释 Cohen's d 分母。
      结果 d≈1.5，仍为 large effect 但低于 2.0 阈值。

      **HellaSwag/GSM8K d 值较低的理由**：
      HellaSwag（~10K items）：4PL 参数质量依赖 PSN-IRT 拟合，HellaSwag 的 item discrimination
      在 4PL 下可能不如 MMLU 精确（sentence completion vs knowledge recall 的 IRT 结构差异），
      导致 lz* 的 aberrance signal 被噪声稀释。d≈1.2 均值仍然显著但不如 MMLU 强劲。
      GSM8K（~1.3K items）：n_items 最小，power theory 预测 power∝√n，1.3K vs 14K 意味着
      理论 power 降低约 70%。此外数学推理题的 4PL d 参数可能接近 1.0（guessing 效应弱），
      减少了 4PL 相对于 3PL 的优势。d≈0.9 均值。

      **Mistral θ-fixed 仍有残余非单调性的理由**：Mistral 的低 memorization fraction 意味着
      即使固定 θ，50% 污染条件下的有效信号（memorized items 数量）可能不足以产生足够的 Δlz*_fixed
      来超过 25% 条件，导致 25%→50% 段出现残余非单调或 plateau。
    tables:
      - name: "Table: Cohen's d at 15% Contamination (MMLU, n=3 seeds, ddof=1)"
        columns: ["Family", "|Cohen's d|", "θ-shift Δθ", "Memo. Frac.", "Monotonic (free-θ)", "Monotonic (θ-fixed)"]
        rows:
          - ["Qwen3.5-9B", "3.2", "0.20", "0.38", "No", "Yes"]
          - ["Llama-3.1-8B", "2.9", "0.39", "0.35", "Yes (weak)", "Yes"]
          - ["Gemma-4-31B", "2.4", "0.15", "0.33", "No", "Yes"]
          - ["Mistral-7B-v0.3", "1.5", "0.44", "0.28", "No", "No (residual)"]
      - name: "Table: Cross-Benchmark Cohen's d at 15% (mean across families)"
        columns: ["Benchmark", "n_items", "Mean |d|", "Min |d|", "Max |d|"]
        rows:
          - ["MMLU", "14042", "2.5", "1.5", "3.2"]
          - ["HellaSwag", "10042", "1.2", "0.6", "1.8"]
          - ["GSM8K", "1319", "0.9", "0.4", "1.4"]
    figures_description:
      - "Heatmap: 4 families × 6 contamination levels, color = |Cohen's d|, 展示 dose-response 全谱"
      - "Line plot: MMLU dose-response curves for 4 families, free-θ (dashed) vs θ-fixed (solid)"
      - "Bar chart: memorization fraction across families and benchmarks"
      - "Scatter: n_items vs mean |Cohen's d| at 15%, 叠加 power theory prediction line"
    analysis: >
      核心叙事：MMLU 检测在 3/4 家族强劲，Mistral 较弱但仍为 large effect。
      HellaSwag/GSM8K 效果显著但受 n_items 和 4PL 参数质量制约——
      这直接支撑 "characterized operating conditions" 叙事（Claim 1 的边界条件报告）。
      θ-fixed 是 methodological contribution：3/4 家族恢复单调性验证了 θ-shift 机制的普遍性。
      memorization fraction 家族间差异（0.28-0.42）量化了 SFT generalization effect 的 model-dependence。

  # =========================================================================
  # exp-baseline-comparison (P0-end) — ≥5 baselines
  # =========================================================================
  - name: "baseline comparison (≥5 baselines on ctrl-contam ground truth)"
    plan_id: "exp-baseline-comparison"
    description: >
      在 ctrl-contam ground-truth models 上比较 IRT-FIT vs (1) ConStat, (2) Min-K%++,
      (3) accuracy z-score, (4) PPL-based, (5) random baseline 的 AUROC。
      Median 档：lz* 在 5-10% 低污染优势明确，15%+ 落后于特权方法。
    expected_results:
      # --- AUROC at various contamination levels ---
      auroc_lz_star_5pct: 0.67
      auroc_lz_star_10pct: 0.76
      auroc_lz_star_15pct: 0.82
      auroc_lz_star_25pct: 0.88
      auroc_mink_pp_5pct: 0.58
      auroc_mink_pp_10pct: 0.72
      auroc_mink_pp_15pct: 0.88
      auroc_mink_pp_25pct: 0.95
      auroc_constat_5pct: 0.62
      auroc_constat_10pct: 0.75
      auroc_constat_15pct: 0.90
      auroc_constat_25pct: 0.96
      auroc_acc_zscore_5pct: 0.54
      auroc_acc_zscore_10pct: 0.60
      auroc_acc_zscore_15pct: 0.68
      auroc_acc_zscore_25pct: 0.78
      auroc_ppl_5pct: 0.55
      auroc_ppl_10pct: 0.68
      auroc_ppl_15pct: 0.82
      auroc_ppl_25pct: 0.92
      auroc_random: 0.50
      # --- gap vs best privileged ---
      baseline_auroc_gap_at_15pct_vs_best_privileged: -0.08
      baseline_auroc_gap_at_25pct_vs_best_privileged: -0.08
      baseline_auroc_lz_at_5pct: 0.67
      lz_star_advantage_over_acc_zscore_all_levels: true
      lz_star_beats_privileged_at_5pct: true
    result_rationale: >
      **lz* 在 5-10% 优势的机制**：低污染下信号微弱，特权方法（Min-K%++, ConStat）的额外信息
      （token probabilities, re-test responses）尚未产生足够信噪比优势。而 lz* 利用 IRT 结构
      作为 inductive bias（4PL 参数编码了 item difficulty/discrimination 的先验知识），
      在信号稀疏时比纯数据驱动方法更高效。这与 simulation 中 lz* 在 5% 时 AUROC=0.675 vs ML best=0.575
      的结果一致。

      **15%+ 落后的机制**：当污染信号变强，特权方法的额外信息维度开始发力——
      Min-K%++ 直接观测 token-level memorization 概率，信号比 binary pattern aberrance 更直接；
      ConStat 通过 re-test 引入独立验证维度。lz* 的 binary-only 约束成为 information bottleneck。
      gap 约 -0.08 AUROC（5-15 百分点）——不是灾难性落后，而是 information access 的结构性代价。

      **lz* 始终优于 accuracy z-score 的理由**：lz* 利用 per-item difficulty 信息（通过 IRT 参数），
      而 accuracy z-score 仅用 aggregate accuracy。在所有污染水平下 lz* 都能捕捉到
      "easy items answered wrong + hard items answered right" 的 pattern-level aberrance，
      这是 accuracy 无法区分的。

      **PPL-based 在高污染下追上来的理由**：PPL 直接测量 sequence-level memorization，
      高污染→更多 memorized sequences→更强的 PPL 信号。但 PPL 需要 token-level log-probs（特权信息）。
    tables:
      - name: "Table: AUROC Comparison Across Contamination Levels"
        columns: ["Method", "Info Level", "5%", "10%", "15%", "25%", "Avg"]
        rows:
          - ["IRT-FIT (lz*)", "binary", "0.67", "0.76", "0.82", "0.88", "0.78"]
          - ["Acc. z-score", "binary (aggr.)", "0.54", "0.60", "0.68", "0.78", "0.65"]
          - ["PPL-based", "log-probs", "0.55", "0.68", "0.82", "0.92", "0.74"]
          - ["Min-K%++", "token probs", "0.58", "0.72", "0.88", "0.95", "0.78"]
          - ["ConStat", "re-test", "0.62", "0.75", "0.90", "0.96", "0.81"]
          - ["Random", "—", "0.50", "0.50", "0.50", "0.50", "0.50"]
      - name: "Table: Bootstrap 95% CI for AUROC at 15%"
        columns: ["Method", "AUROC", "95% CI"]
        rows:
          - ["IRT-FIT (lz*)", "0.82", "[0.76, 0.88]"]
          - ["Min-K%++", "0.88", "[0.83, 0.93]"]
          - ["ConStat", "0.90", "[0.85, 0.95]"]
    figures_description:
      - "Line plot: AUROC vs contamination level for all 6 methods, with bootstrap 95% CI bands"
      - "Bar chart: information access level (x) vs AUROC at 5% and 15% (grouped bars), 标注 minimal-information operating point"
      - "Detection frontier scatter: x=information access (ordinal), y=AUROC, 每个 contamination level 一条曲线"
    analysis: >
      叙事关键：诚实报告 information-access vs detection-power tradeoff curve。
      lz* 在 minimal-information operating point（binary only）定义了 detection frontier 的下界，
      在低污染（≤10%）时是 best available，在高污染时落后于特权方法约 5-10% AUROC。
      强调 "minimal-information operating point 的价值"：当 token probs 不可用时（closed-source models, API-only access），
      lz* 是唯一可行的检测手段。Bootstrap CIs 是我们的差异化优势（6/8 同行不报告方差）。

  # =========================================================================
  # exp-v1-irt-refit-expanded (P0) — 关闭 Path D
  # =========================================================================
  - name: "v1 IRT refit expanded (N≥500, close Path D)"
    plan_id: "exp-v1-irt-refit-expanded"
    description: >
      扩大 v1 IRT 重拟合样本量至 N≥500。Pilot N=63 → a_r=0.111（discrimination failure）。
      Expanded N=178 → a_r=0.127。Median 档预测 N=500 仍不足以修复。
    expected_results:
      n_models_downloaded: 500
      n_models_usable: 420
      3pl_a_pearson_r: 0.14
      2pl_a_pearson_r: -0.01
      3pl_b_pearson_r: 0.69
      conclusion: "dead — Path D definitively closed"
      a_r_below_threshold: true
    result_rationale: >
      **a_r 仍远低于 0.2 阈值的理由**：discrimination failure 不是样本量问题，而是结构性问题。
      Classical MML-EM IRT fitting 假设 examinees 来自同一 population（单一 θ 分布），
      但 LLM models 是 heterogeneous agents（不同架构、训练数据、规模），违反了 IRT 的
      local independence 和 unidimensionality 假设。N=63→178→500 的边际改善极小
      （0.111→0.127→~0.14）因为增加更多 heterogeneous "examinees" 不能修复 model violation。
      这与 Phase B 发现的 universal 4PL model misfit 一致：LLM 本质上不是 IRT 的 "good examinees"。
      b_r≈0.69 持续有效是因为 item difficulty 是 population-level property，对 examinee
      heterogeneity 更 robust。a_r failure 最终确认 Path D（大规模 leaderboard audit with
      refitted parameters）不可行。论文中报告为 methodological caveat：classical IRT estimation
      需要 N>>500 同质 examinees，LLM 场景远未满足。
    tables:
      - name: "Table: IRT Refit Parameter Recovery Across Sample Sizes"
        columns: ["N", "a_r (3PL)", "a_r (2PL)", "b_r (3PL)", "Verdict"]
        rows:
          - ["63 (pilot)", "0.111", "-0.084", "0.626", "dead"]
          - ["178 (expanded-v1)", "0.127", "-0.029", "0.663", "dead"]
          - ["~420 (expanded-v2)", "0.14", "-0.01", "0.69", "dead (confirmed)"]
    figures_description:
      - "Line plot: N vs a_r with 95% CI, horizontal line at a_r=0.2 (viability threshold) and a_r=0.4 (good threshold)"
    analysis: >
      Path D 最终关闭。13K+ v1 data 的可用性写入 Discussion/Future Work：
      "当 IRT parameter estimation 方法能处理 heterogeneous agent populations 时，
      这些数据将支持大规模回溯审计。" 这是 honest negative result as contribution 叙事的一部分。

  # =========================================================================
  # exp-post-rl (P2) — Post-RL hypothesis test
  # =========================================================================
  - name: "post-RL hypothesis test (SFT contam → GRPO)"
    plan_id: "exp-post-rl"
    description: >
      Qwen3.5-9B 先 SFT 污染再 GRPO，测试 person-fit 是否在 RL 后保持检测力。
      Median 档：信号衰减但未消失（|d| 0.5-1.5），或实验未能在 DDL 前完成。
    expected_results:
      # --- scenario A: completed but attenuated ---
      post_rl_cohens_d_15pct: 0.9
      post_rl_delta_lz_star: -1.8
      pre_rl_cohens_d_15pct: 3.2
      signal_retention_ratio: 0.28
      # --- scenario B: incomplete ---
      experiment_completed_before_ddl: "uncertain (50% probability)"
      grpo_training_steps_completed: 3000
      grpo_training_steps_planned: 8000
      # --- if completed ---
      post_rl_memorization_fraction: 0.15
      post_rl_theta_shift: 0.08
      post_rl_acc_on_seen_items: 0.72
      pre_rl_acc_on_seen_items: 0.82
    result_rationale: >
      **信号衰减机制**：GRPO 优化 reward（通常是 correctness + format compliance），
      不直接强化 memorization。RL 的 exploration 机制（sampling diverse responses）
      会部分 "覆盖" SFT 注入的 memorization pattern——模型学会用 reasoning 而非 recall 来答题。
      memorization fraction 从 ~0.36 降至 ~0.15：RL 后模型在 seen items 上仍有残余优势
      （因为 SFT 创建的 weight modifications 不会完全消失），但优势大幅缩小。
      |d| 从 3.2 降至 ~0.9：仍为 large effect（按 Cohen's convention d>0.8），
      但统计显著性在 n=3 seeds 下变得 borderline（p~0.05-0.10）。

      **未完成的风险**：GRPO 训练需要 reward model 或 rule-based reward 的 engineering work，
      加上 2× RTX 5090 的 GPU 预算（~40 hrs），在 ARR 5/25 DDL 前可能只跑完部分 steps。
      如果只完成 3000/8000 steps，RL 效果不充分，结果不可解释——这种情况下降为
      Discussion 中的 "structural argument + preliminary evidence"。

      **为什么信号不完全消失**：SFT 在 weight space 中创建的 local modifications
      （memorization of specific QA pairs）处于 loss landscape 的不同 basin 于 RL 优化方向。
      RL 优化的是 expected reward over diverse responses，不直接擦除 specific item memories。
      残余信号（d~0.9）正好在 "detectable but not reliable" 的边界——支撑 "structural immunity"
      的 argument 但不足以作为 claim。
    tables:
      - name: "Table: Pre- vs Post-RL Detection (MMLU, 15% contamination)"
        columns: ["Stage", "lz*", "Δlz*", "|Cohen's d|", "Memo. Frac.", "Acc (seen)"]
        rows:
          - ["Clean baseline", "9.3", "—", "—", "—", "0.70"]
          - ["Post-SFT (pre-RL)", "5.1", "-4.2", "3.2", "0.36", "0.82"]
          - ["Post-GRPO", "7.5", "-1.8", "0.9", "0.15", "0.72"]
    figures_description:
      - "Bar chart: |Cohen's d| pre-RL vs post-RL, with bootstrap 95% CI"
      - "Line plot: training steps vs lz* (if intermediate checkpoints available)"
    analysis: >
      Median 档下 post-RL 不列入 Claim，降为 Discussion section：
      "Structural argument: person-fit operates on binary patterns, orthogonal to
      token-level distributional shifts induced by RL. Preliminary evidence: |d|=0.9
      (large effect but borderline significant with n=3) after GRPO suggests signal
      attenuation but not elimination. Full characterization requires dedicated study."
      这诚实反映了 median 档的 "不完整但有信号" 状态。

  # =========================================================================
  # exp-4pl-ablation (P2) — 4PL vs 3PL(d=1)
  # =========================================================================
  - name: "4PL vs 3PL ablation (detection sensitivity)"
    plan_id: "exp-4pl-ablation"
    description: >
      已完成。在 simulation 中 4PL 相对于 3PL(d=1) 的 power gain 为 +14-27pp mean，
      real-data correlation r=0.225。此条已有确定数据。
    expected_results:
      mean_power_gain_mmlu: 0.273
      mean_power_gain_hellaswag: 0.261
      far_4pl: 0.05
      far_3pl_range: [0.047, 0.165]
      real_data_correlation_4pl_3pl: 0.225
      real_data_rmse: 68.41
    result_rationale: >
      已完成实验。d 参数对高能力模型至关重要：当 d<1（upper asymptote < 1），
      不建模 d 会让模型预测 P(correct)→1，放大 few-error aberrance signal，
      系统性地 inflate high-ability models 的 lz*。46% MMLU items 有 d<0.95。
      实测数据确认 3PL 使 lz* 对高能力模型完全不可靠（DeepSeek-V3 Δ=357）。
    tables: []
    figures_description: []
    analysis: "已完成。结果直接支撑 Claim 1 的 4PL 必要性。"

  # =========================================================================
  # exp-multiscale-lzm (P2) — Cross-benchmark aggregation
  # =========================================================================
  - name: "multiscale lzm statistic (cross-benchmark aggregation)"
    plan_id: "exp-multiscale-lzm"
    description: >
      实现 Hong, Lin & Cheng (2021) 的 lzm 统计量，在 PSN-IRT 12 模型 + ctrl-contam 上验证。
      Median 档：lzm 提供 complementary signal 但不改变核心 narrative。
    expected_results:
      lzm_gemini15: 18.5
      lzm_deepseek_v3: 12.3
      lzm_ctrl_contam_15_qwen: 6.8
      lzm_ctrl_contam_50_qwen: 4.2
      lzm_clean_mean: 8.9
      lzm_vs_per_benchmark_correlation: 0.85
      lzm_adds_detection_power: false
      lzm_adds_interpretability: true
    result_rationale: >
      lzm 是 per-benchmark lz* 的标准化加权聚合。在 median 档下：
      (a) correlation 与 per-benchmark lz* 高（r≈0.85）因为 lzm 本质上是 summary statistic；
      (b) 不额外增加检测 power 因为信息来源相同（binary response patterns），只是聚合方式不同；
      (c) 增加 interpretability：提供 "overall contamination index" 而非需要查看 5 个
      per-benchmark lz* 值。对 Gemini-1.5（所有 benchmark 高 misfit）lzm 最高，
      对 ctrl-contam_15（仅 MMLU contaminated）lzm 相对较低因为 clean benchmarks 拉低聚合值。
      这是 nice-to-have 的 methodological extension，不改变论文的核心叙事。
    tables:
      - name: "Table: lzm vs Per-Benchmark lz* for Selected Models"
        columns: ["Model", "lzm", "MMLU lz*", "HellaSwag lz*", "GSM8K lz*"]
        rows:
          - ["Gemini-1.5", "18.5", "31.8", "—", "—"]
          - ["Qwen ctrl_15", "6.8", "5.1", "2.3", "1.5"]
          - ["Clean mean", "8.9", "9.3", "8.1", "3.2"]
    figures_description:
      - "Scatter: lzm vs mean per-benchmark |lz*| with identity line"
    analysis: >
      P2 优先级合理。lzm 可作为 Section 5 的 supplementary analysis，
      但不值得在 main claims 中占据位置。如果版面紧张可移至 appendix。

  # =========================================================================
  # exp-extra-benchmarks (P2) — BBH + MATH
  # =========================================================================
  - name: "extra benchmarks (BBH + MATH for mid-range n_items)"
    plan_id: "exp-extra-benchmarks"
    description: >
      BBH (6511 items) 和 MATH (5000 items) 填充 1K-10K power gap。
      Median 档：如果 PSN-IRT 有参数可用，可执行；否则 DDL 前无法完成 4PL calibration。
    expected_results:
      bbh_available_in_psnirt: "uncertain (60% yes)"
      math_available_in_psnirt: "uncertain (40% yes)"
      # --- if available ---
      bbh_power_15pct_simulated: 0.72
      math_power_15pct_simulated: 0.65
      bbh_cohens_d_15pct_ctrl_contam: 1.8
      math_cohens_d_15pct_ctrl_contam: 1.5
      # --- power theory validation ---
      power_vs_n_items_R2_with_extras: 0.96
    result_rationale: >
      **Power theory 预测**：exp-power-theory R²=0.957，min_items_15pct_80power=7958。
      BBH（6511 items）恰好在 80% power 阈值附近，预测 power≈0.72（略低于 80%）。
      MATH（5000 items）进一步低于阈值，power≈0.65。两者都填充了 GSM8K(1.3K)→MMLU(14K)
      之间的 gap，验证 power∝√n 关系在 mid-range 的适用性。

      **ctrl-contam d 值**：d∝√(n_items)（近似），BBH d≈1.8 和 MATH d≈1.5 位于
      GSM8K(d≈0.9) 和 MMLU(d≈2.5) 之间，符合理论预测。

      **PSN-IRT 参数可用性的不确定性**：PSN-IRT 论文主要使用 Open LLM Leaderboard benchmarks
      （MMLU, HellaSwag, GSM8K, ARC-C, HumanEval）。BBH 可能有（作为 reasoning benchmark
      越来越常见），MATH 可能没有。如果需要自己 calibrate 4PL，需要大规模推理（BBH 6.5K items ×
      N models），在 DDL 前不可行。
    tables:
      - name: "Table: Power Function Validation with Additional Benchmarks"
        columns: ["Benchmark", "n_items", "Predicted Power @15%", "Observed Power @15%"]
        rows:
          - ["GSM8K", "1319", "0.59", "0.59"]
          - ["MATH*", "5000", "0.65", "—"]
          - ["BBH*", "6511", "0.72", "—"]
          - ["HellaSwag", "10042", "0.75", "0.75"]
          - ["MMLU", "14042", "0.98", "0.98"]
    figures_description:
      - "Power curve: n_items (log-scale) vs detection power, with new benchmarks as validation points"
    analysis: >
      如果 PSN-IRT 参数可用，这是高价值的 Claim 2 验证（填充 power curve 的 mid-range gap）。
      如果不可用，降为 future work。Median 档下假设 BBH 可用但 MATH 不可用（60/40 split）。

  # =========================================================================
  # exp-domain-analysis (P2) — 已完成
  # =========================================================================
  - name: "MMLU domain-level analysis"
    plan_id: "exp-domain-analysis"
    description: >
      已完成。Gemini-1.5 MMLU 污染是全面性的（50/57 subjects flagged），非 domain-concentrated。
    expected_results:
      gemini_domain_concentrated: false
      gemini_subjects_flagged: "50/57"
      gemini_category_lz_stem: 21.2
      gemini_category_lz_humanities: 17.9
    result_rationale: >
      已完成。Gemini-1.5 的 100% MMLU accuracy 意味着所有 domain 都被完全 memorized，
      不存在 domain 选择性。STEM 略高因为 STEM items 平均 difficulty 更高（b 更大），
      完全正确时产生更大的 aberrance。
    tables: []
    figures_description: []
    analysis: "已完成。支撑 Claim 3(b) PSN-IRT case study。"

  # =========================================================================
  # exp-natural-experiment (P2-optional) — 已完成
  # =========================================================================
  - name: "v1 base→chat natural experiment"
    plan_id: "exp-natural-experiment"
    description: >
      已完成。HellaSwag 和 GSM8K 显示 significant systematic SFT effects，
      但无 individual pair 显示 benchmark-specific contamination outliers。
    expected_results:
      hellaswag_t_stat: -3.97
      gsm8k_t_stat: 3.35
      individual_outliers: 0
    result_rationale: >
      已完成。SFT 系统性改变 lz*（HellaSwag 下降 = SFT 减少 aberrance，
      GSM8K 上升 = SFT 在数学上增加 aberrance），但这是 population-level effect，
      不足以检测 individual contamination。a_r=0.111 使 lz*≈accuracy-like，
      仅 4-5 pairs 无统计检验能力。P2-optional 状态合理。
    tables: []
    figures_description: []
    analysis: "已完成。可写入 supplementary 作为 natural experiment 的 null result。"

  # =========================================================================
  # exp-leaderboard-audit (ABANDONED)
  # =========================================================================
  - name: "leaderboard audit (v1 large-scale scan)"
    plan_id: "exp-leaderboard-audit"
    description: >
      已 ABANDONED。D011 确认 v1 IRT refit 的 a_r=0.111 使大规模审计不可行。
    expected_results:
      status: "ABANDONED"
      reason: "discrimination failure (a_r=0.111) makes lz* ≈ accuracy-based, no added value"
    result_rationale: >
      IRT person-fit 的检测力依赖于 discrimination parameter a：a 编码了 item 区分高低能力
      examinees 的能力。a_r=0.111 意味着 refitted a 与 PSN-IRT 的 a 几乎无相关——
      refitted 参数本质上是噪声，lz* 退化为 accuracy 的非线性变换，失去 pattern-level 信息。
      13K+ models 的数据仍然有价值，但需要更好的 IRT estimation 方法（future work）。
    tables: []
    figures_description: []
    analysis: "写入 Discussion/Future Work：data available, estimation method needed。"

  # =========================================================================
  # exp-power-theory (P1) — 已完成
  # =========================================================================
  - name: "power function theory (analytical derivation)"
    plan_id: "exp-power-theory"
    description: >
      已完成。R²=0.957（two-sided），crossover 81-85%，min_items for 80% power = 7958。
    expected_results:
      R2_two_sided: 0.9572
      min_items_15pct_80power: 7958
      crossover_range_pct: "81-85%"
    result_rationale: >
      已完成。Power ∝ √(n_items × contamination_level) 的解析关系从 Snijders (2001)
      lz* 方差公式推导而来，simulation 验证 R²>0.95。理论 power 是 upper bound
      （假设所有 contaminated items 产生 aberrant signal），实际 power = theory × memorization_fraction。
    tables: []
    figures_description: []
    analysis: "已完成。核心支撑 Claim 2。与 ctrl-contam memorization fraction 结合报告。"

  # =========================================================================
  # exp-two-sided (P0) — 已完成
  # =========================================================================
  - name: "two-sided detection framework"
    plan_id: "exp-two-sided"
    description: "已完成。57/60 flagged after BH-FDR。Universal 4PL model misfit confirmed。"
    expected_results:
      flagged_rate: "57/60 (95.0%)"
      key_finding: "LLMs universally violate 4PL assumptions"
    result_rationale: "已完成。Bootstrap + FDR 不减少 flagging 因为 LLM lz* 值是 genuinely extreme。"
    tables: []
    figures_description: []
    analysis: "已完成。核心 evidence for Claim 3(a) universal misfit。"

  # =========================================================================
  # exp-extended-sim (P0) — 已完成
  # =========================================================================
  - name: "extended simulation (11 contamination levels)"
    plan_id: "exp-extended-sim"
    description: "已完成。Two-sided power >93% at ALL MMLU contamination levels。"
    expected_results:
      mmlu_two_sided_power_min: 0.936
      crossover: "75-90%"
    result_rationale: "已完成。Two-sided detection 消除 inverted-U。"
    tables: []
    figures_description: []
    analysis: "已完成。核心 evidence for Claim 2 dual-regime。"

  # =========================================================================
  # exp-empirical-null (P0) — 已完成
  # =========================================================================
  - name: "bootstrap empirical null analysis"
    plan_id: "exp-empirical-null"
    description: "已完成。Null well-calibrated（mean bias=0.09, std≈1.0），95% flagging due to genuine misfit。"
    expected_results:
      mean_null_bias: 0.0925
      ks_reject_rate: 0.4
    result_rationale: "已完成。Small benchmarks KS reject due to finite-sample non-normality，not miscalibration。"
    tables: []
    figures_description: []
    analysis: "已完成。Validates Δlz* approach。"

  # =========================================================================
  # Predictions for key MEDIAN-tier aggregate metrics
  # =========================================================================
  median_tier_summary_metrics:
    ctrl_contam_cohens_d_15pct_min_across_families: 1.5
    ctrl_contam_cohens_d_15pct_mean_across_families: 2.5
    n_families_d_gt_2: 3
    multi_benchmark_cohens_d_15pct_hellaswag: 1.2
    multi_benchmark_cohens_d_15pct_gsm8k: 0.9
    baseline_auroc_gap_at_15pct_vs_best_privileged: -0.08
    baseline_auroc_lz_at_5pct: 0.67
    post_rl_cohens_d_15pct: 0.9
    theta_fixed_monotonic_families: 3
    memorization_fraction_range: [0.28, 0.42]
    power_theory_vs_observed_R2: 0.86
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79abadea-0be1-4361-b520-7b98e44b5450",
  "isSidechain": false,
  "requestId": "req_011CbF1syEoUx8nzE4UDLkyR",
  "type": "assistant",
  "uuid": "c8c21926-9c4c-4514-866c-b7e0642194a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016QbdU999PjfeEfTX2z29Yj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1323,
      "cache_read_input_tokens": 34665,
      "output_tokens": 12252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12252,
          "cache_read_input_tokens": 34665,
          "cache_creation_input_tokens": 1323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1323
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

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心检测有效但存在边界条件：部分家族/benchmark 信号较弱，post-RL 不确定，baseline 对比有差距 核心假设：['ctrl-contam 在 3/4 家族有效（|d|>2.0 @ 15%），1 家族信号较弱（|d| 1.0-2.0）', 'MMLU 检测强劲，HellaSwag/GS…",
  "leafUuid": "c8c21926-9c4c-4514-866c-b7e0642194a0",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier IRT contamination detection with characterized operating conditions",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心检测有效但存在边界条件：部分家族/benchmark 信号较弱，post-RL 不确定，baseline 对比有差距 核心假设：['ctrl-contam 在 3/4 家族有效（|d|>2.0 @ 15%），1 家族信号较弱（|d| 1.0-2.0）', 'MMLU 检测强劲，HellaSwag/GS…",
  "leafUuid": "c8c21926-9c4c-4514-866c-b7e0642194a0",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier IRT contamination detection with characterized operating conditions",
  "sessionId": "64734155-0bc9-4993-a914-3c67248a3bb1"
}
```

---
