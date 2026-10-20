# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Post-RL destroys all person-fit signals; HT matches lz* everywhere; reframe

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-3/f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca.jsonl`
- **Structured JSON:** [`71692827e9bfe5990a5e.json`](../../sessions/71/71692827e9bfe5990a5e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:42:56.932Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:42:56.932Z",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Post-RL destroys all person-fit signals; HT matches lz* everywhere; reframe as framework + empirical characterization paper\n核心假设：['exp-post-rl: GRPO eliminates detection for all binary-only methods (|d|<0.5)', 'HT matches or exceeds lz* in all tested conditions (no empirical differentiation)', 'MIA/Min-K++ achieve AUROC 0.65+ on SFT contamination (minimal-information penalty is real)', 'ARC-C too small for reliable detection even with θ-fixed (|d|<0.5)', 'Cross-family generalizability limited to SFT-only contamination scope']\n关键指标范围：{'post_rl_lz_star_cohens_d': [0.0, 0.5], 'post_rl_ht_cohens_d': [0.0, 0.5], 'post_rl_mia_auroc': [0.45, 0.55], 'n_families_validated': [2, 2], 'n_baselines_beaten': [2, 3], 'arcc_theta_fixed_d': [0.0, 0.5], 'constat_retest_auroc': [0.8, 0.95], 'mink_sft_auroc': [0.6, 0.75]}\n叙事方向：\"Reframe: NOT a detection superiority paper. Three reframing angles for same venue: (A) Empirical characterization paper — first systematic study of how LLM response patterns relate to IRT assumptions. Universal 4PL misfit (57/60 flagged) is a novel finding about LLM cognition. θ-shift mechanism is a methodological contribution to contamination science regardless of detection power. (B) Scope-honest detection paper — IRT-FIT detects intentional SFT contamination (|d|>2.9 across two families) with explicit scope boundary: post-RL training smooths binary signal below detection threshold for ALL binary-only methods. This negative result (RL boundary) is itself a contribution — it maps the detection frontier's limits. Frame as: 'we establish where binary detection works and precisely where it fails.' (C) Framework + toolkit paper — open-source IRT-FIT toolkit + 13K model data availability + memorization fraction methodology. Contribution is the framework (connecting psychometrics to LLM evaluation) not detection SOTA. θ-shift analysis, seen/unseen decomposition, and dose-response characterization are methodological contributions independent of absolute detection power. Still targets EMNLP as evaluation methodology with community tooling impact.\"\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_personfit_contam\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.\n\n**Claim 2 (Detection Characterization)**:\nDetection power increases with benchmark size (n_items) and varies with contamination level, following an empirical power function (R²=0.65) that provides approximate practical guidance for practitioners assessing detectability on benchmarks of known size — but should NOT be described as \"predictive theory\" or \"scaling law.\" Two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported. **Baseline comparison (exp-baseline-comparison)**: At model level, lz* achieves 8× the effect size of classical person-fit statistics (Guttman/U3) on identical data (|d|=3.42 vs |d|=0.43 for Qwen 15%), demonstrating the value of full 4PL IRT parameterization. At item level, ALL binary-only methods achieve near-random discrimination (AUROC 0.52–0.63, including oracle supervised classifiers), revealing contamination produces a diffuse statistical signature detectable only through model-level aggregation over thousands of items. Accuracy z-score trivially detects in controlled settings (z=160 due to near-zero accuracy variance) but lacks specificity in real-world scenarios. The IRT framework enables principled aggregation by calibrating each item's expected response probability.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns from the target model (with externally calibrated IRT item parameters), IRT-FIT detects controlled contamination with |Cohen's d|>2.9 across two model families (Qwen, Llama), achieving 8× the effect size of classical person-fit statistics (Guttman/U3). The HT statistic (requiring only item difficulty) achieves comparable model-level detection power — the IRT person-fit family collectively dominates simpler indices, with ℓz*'s advantage lying in mechanistic interpretability (θ-shift analysis, memorization fraction quantification) and [pending: post-RL robustness vs HT]. Model-level aggregation over thousands of items yields robust detection where all item-level methods are near-random (AUROC 0.52–0.63). The IRT framework provides unique mechanistic insight: θ-shift analysis reveals how contamination raises ability estimates, and memorization fraction (35–38%) bridges theoretical power (97.9%) and observed detection capacity.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | **Completed (exp-baseline-comparison)**: Model-level: lz* |d|=3.42 vs Guttman/U3 |d|=0.43 (8× gap) — full IRT parameterization far exceeds difficulty-only person-fit. **HT is nearly as powerful as ℓz* (avg |d| comparable)** — the \"8×\" headline must include HT comparison to avoid selective framing. Item-level: all methods near-random (AUROC 0.52–0.63). acc z-score detects trivially (z=160) but lacks specificity. | exp-baseline-comparison |\n| R12 | \"HT ≈ ℓz* — why use ℓz*?\" | **[Dream D2 三档一致]** HT achieves comparable |d| with weaker requirements (difficulty only, no 4PL). **四场景应对 (D022, Reviewer validated)**：(Best) HT post-RL 丢失 + ℓz* 保留 → headline 差异化；(Good) HT 弱化 + ℓz* 更强 → quantitative comparison；(Neutral) 均保留 → 转用数据无关差异化（见下）；(Bad) 均丢失 → negative-as-contribution, scope SFT。**数据无关差异化（任何场景均可用）**：(i) ℓz* 有参数化 null (≈N(0,1), bootstrap 已验证) → 可直接假设检验, HT 无此性质；(ii) Snijders 校正补偿 θ 估计误差 (Var*=Var_l - C²/I(θ)), HT 无此校正；(iii) ℓz* 用 a/b/c/d 四参数加权 item 贡献, HT 仅用 b → MMLU 跨 57 科目 item 异质性大时 ℓz* 理论更精确。这些点不依赖 post-RL 结果，论文中应明确讨论。 | exp-baseline-comparison, exp-post-rl |\n| R13 | \"Minimal-information overstates\" | **[Dream D2 三档一致]** \"Minimal-information operating point\" obscures PSN-IRT 4PL parameter dependency. Reframe to \"minimal information **from the target model**\" or \"minimal runtime information\" — explicitly acknowledge PSN-IRT calibration as an external input requirement. | — |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as empirical characterization** — Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Simulation fit R²=0.957; real-data fit R²=0.65 (gap due to SFT generalization). Frame as \"empirical trend\" not \"theory/law.\"\n6. **Baseline comparison as evidence for model-level aggregation** — Item-level detection is near-random for ALL binary-only methods (including oracle RF). This is NOT a weakness — it reveals that contamination signal is diffuse (memorization fraction ~35%). Model-level lz* aggregates 14K weak signals into |d|>2.9. Frame item-level weakness as supporting evidence: \"any method that aggregates is better than any method that localizes.\" lz* vs Guttman/U3 8× gap proves IRT parameterization matters. acc z-score is sensitive but non-specific (sensitivity-specificity tradeoff).\n7. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n8. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n9. **Memorization fraction cross-family consistency** — MF is 35–38% at 15% contamination across Qwen (0.38) and Llama (0.35), only 3pp difference. Consistency strengthens generalizability. MF may vary with contamination mechanism (full FT vs QLoRA), model capacity, and benchmark difficulty — acknowledge in Limitations as deployment bootstrapping problem.\n10. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **Cross-family baseline lz* divergence (Reviewer WARNING)** — Clean lz* spans ~9σ: Qwen +8.68, Mistral +5.42, Llama -0.14. 固定阈值检测失效（Qwen contam_15 lz*=+3.85 仍为正值）。论文必须：(a) 明确 IRT-FIT 是相对检测（Δlz*/Cohen's d），非绝对阈值；(b) 展示 clean baseline lz* 跨家族差异表；(c) 预防性回答\"contam_15 lz*=+3.85 为正值为何算污染\"（因为 Δlz*=-4.83 是大效应）；(d) lz* baseline 作为\"模型内部一致性\"指标——Mistral acc 最低(0.514)但 lz* 第二高(+5.42)，说明 lz* 捕捉 difficulty-ordering 一致性而非准确率。\n14. **Inverted-U 是模型相关的** — Qwen 在 15%→50% 区间出现强 inversion（Δlz* 50%=-1.39 << 15%=-4.83），Llama 和 Mistral 在此区间 Δlz* 单调增大。Inverted-U 在 free-θ 下由 baseline misfit 调制——高 baseline lz* (Qwen +8.68) 的模型更容易出现 non-monotonicity。论文不能 claim inverted-U 为 universal phenomenon，需加 model-dependent caveat。θ-fixed 分析仍恢复所有家族的 monotonicity — 这是 θ-fixed 贡献的关键证据。\n15. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.\n- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = \"θ_fixed repairs non-monotonicity\"; Llama story = \"θ_fixed enhances existing monotonicity\". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-two-sided\n  registry_id: exp-two-sided\n  claim: 2\n  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case\n    study）。包括 bootstrap confidence interval 和 FDR 控制。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- id: exp-extended-sim\n  registry_id: exp-extended-sim\n  claim: 2\n  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让\n    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向\n    lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 依赖 exp-two-sided 的双侧框架定义。\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- id: exp-ctrl-contam-pilot\n  claim: 1,2,3\n  description: 快速验证：Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU only。测量\n    Δlz*(clean→contaminated) 是否显著。增加第二个 0% seed 作为 clean-vs-clean noise floor baseline\n    (Reviewer Q2/Q4)。Eval 时区分 seen/unseen items 以实测 memorization fraction (Reviewer\n    Q3/W9)。这是论文 go/no-go 信号。\n  priority: P0-CRITICAL\n  gpu_budget_hours: 12\n  deps: []\n  status: planned\n  notes: 'GPU 恢复后第一优先。4 conditions × ~3 hrs = ~12 GPU-hrs (+2h for second 0% seed)。关键输出:\n    (a) Δlz* 显著性, (b) clean-vs-clean Δlz* ≈ 0 验证, (c) memorization fraction = (Δacc_seen\n    - Δacc_unseen)/Δacc_seen, (d) adjusted power = theory × memorization fraction。D010\n    要求。'\n- id: exp-ctrl-contam\n  claim: 1,2,3\n  description: 完整控制实验：在 4 个模型上用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量\n    Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - exp-ctrl-contam-pilot\n  status: planned\n  notes: '模型: Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3。Benchmark:\n    MMLU + GSM8K + HellaSwag。4 模型 × 6 levels × 3 benchmarks。'\n- id: exp-empirical-null\n  registry_id: exp-empirical-null\n  claim: 1\n  description: Bootstrap empirical null 分析：量化 lz* 在真实 LLM 数据上的 systematic bias（null\n    mean ≠ 0, null std ≠ 1），为 Calibration Gap Analysis 提供定量证据。包含 Q-Q plots、KS tests、bias\n    量化表、unflagged cells 深度分析。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 复用 exp-two-sided v2 的 bootstrap 逻辑，但保存完整中间分布。~2h 开发+运行。\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- id: exp-power-theory\n  registry_id: exp-power-theory\n  claim: 2\n  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A\n    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: DONE\n  notes: 纯理论推导 + 数值验证。CPU only.\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- id: exp-leaderboard-data-recon\n  registry_id: exp-leaderboard-data-recon\n  claim: 3\n  description: Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results\n    是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item\n    data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: 纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- id: exp-leaderboard-audit\n  claim: 3\n  description: Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark\n    污染率随时间趋势。\n  priority: ABANDONED\n  gpu_budget_hours: 20\n  deps:\n  - exp-two-sided\n  - exp-leaderboard-data-recon\n  status: planned\n  notes: 'D011: v1-irt-refit a_r=0.111 + item alignment 54.56% → 13K audit 不可行。数据可用性写入\n    Discussion/Future Work。'\n- id: exp-natural-experiment\n  claim: 3\n  description: v1 leaderboard base→chat model pairs 自然实验：计算 Δlz* = lz*(chat) - lz*(base)\n    作为 SFT 效应代理。\n  priority: P2-optional\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: 'D013: a_r=0.111 导致 lz*≈accuracy-like, 仅 4-5 pairs 无统计检验能力。Reviewer 终审建议降级。'\n- id: exp-v1-irt-refit-expanded\n  claim: 3\n  description: 扩大 v1 IRT 重拟合样本量至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。最终关闭 Path\n    D。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: CPU only. Reviewer 要求 N≥500 才能最终结论 Path D。阈值：a_r>0.4=可行, a_r<0.2=dead。\n- id: exp-4pl-ablation\n  claim: 1\n  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter\n    d 对 false alarm 和 detection power 的影响。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\n- id: exp-baseline-comparison\n  claim: 1\n  description: '与现有方法对比（≥5 baselines）：在控制实验的 ground-truth contaminated models 上，比较\n    IRT-FIT vs baselines 的 AUROC/Type-I error。Baselines: (1) ConStat (re-test), (2)\n    Min-K%++ (token probs), (3) accuracy z-score (已完成, CPU), (4) PPL-based detection\n    (log-prob family 代表, 预期 RL-robust 测试中失败), (5) random baseline。量化 minimal-information\n    的代价（power 损失）。报告 bootstrap CIs（同行 6/8 不报告方差，这是我们的差异化优势）。'\n  priority: P0-end\n  gpu_budget_hours: 30\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: 蒸馏显示同行 baseline 中位数 ~5 个。accuracy z-score 已完成(CPU)。ConStat 需 re-test, Min-K%++\n    需 token probs, PPL 需 log-probs。exp-ctrl-contam 完成后立即执行。\n- id: exp-multiscale-lzm\n  claim: 1,3\n  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化\n    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要实现 lzm 公式。\n- id: exp-post-rl\n  claim: 1\n  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应\n    Wang et al. (2025) 的 MIA 失效问题。\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\n- id: exp-extra-benchmarks\n  claim: 2,3\n  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items\n    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\n- id: exp-domain-analysis\n  claim: 3\n  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5\n    的 MMLU 污染是全面的还是集中在特定 domain。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要 MMLU item-to-domain 映射。\n\n\n## registry (completed experiments)\n\n- exp_id: sim_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    null_check:\n      all_pass: true\n      gsm8k_ks_p: 0.098\n      hellaswag_ks_p: 0.224\n      mmlu_ks_p: 0.594\n    simulation_power_at_15pct:\n      mmlu: 0.979\n      hellaswag: 0.733\n      gsm8k: 0.578\n      arc_c: 0.129\n      humaneval: 0.243\n    global_pass: false\n    inverted_u_all_benchmarks: true\n    pass_count_large_80pct: 1/3 (mmlu only)\n- exp_id: phase_b_personfit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_sd_all_gt_0.5: true\n    mmlu_lz_star_mean: 24.19\n    mmlu_lz_star_sd: 16.47\n    hellaswag_lz_star_mean: 20.09\n    hellaswag_lz_star_sd: 17.59\n    gsm8k_lz_star_mean: 8.22\n    gsm8k_lz_star_sd: 8.97\n    gemini15_mmlu_lz_star: 34.75\n    gemini15_mmlu_accuracy: 1\n    gemini15_mmlu_theta: 0.78\n    gemini15_flagged_benchmarks: 3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\n    cross_benchmark_spearman_significant: 1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\n    n_models: 12\n    n_benchmarks: 5\n- exp_id: exp-two-sided\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- exp_id: exp-extended-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- exp_id: exp-empirical-null\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- exp_id: exp-leaderboard-data-recon\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- exp_id: exp-power-theory\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- exp_id: exp-item-alignment-check\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    match_rate_direct: 0.5456\n    match_rate_reordered_mistral: 0.8846\n    match_rate_reordered_vicuna: 0.7248\n    n_items_checked: 14042\n    n_models_verified: 2\n    alignment_method: content-based via cais/mmlu canonical order\n    items_mapped: 12068\n    mapping_coverage: 0.86\n- exp_id: exp-v1-irt-refit-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 63\n    n_models_failed: 38\n    n_items: 14042\n    n_mapped_items: 12441\n    overall_accuracy: 0.426\n    fitting_time_2pl_sec: 8.9\n    fitting_time_3pl_sec: 12.1\n    3pl_a_pearson_r: 0.111\n    3pl_b_pearson_r: 0.626\n    3pl_b_spearman_r: 0.656\n    2pl_a_pearson_r: -0.084\n    2pl_b_pearson_r: 0.572\n    lz_star_mean: 11.69\n    lz_star_std: 6.68\n    lz_star_flagged_pct: 1.6\n- exp_id: exp-accuracy-zscore-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_flagged_count: 4\n    lz_flagged_count: 57\n    agreement_rate: 0.117\n    gemini15_mmlu_zscore: 1.413\n- exp_id: exp-cross-benchmark-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_all5_flagged: 10\n    n_models_selective_flagged: 2\n    gemini15_cluster_isolation: true\n    dominant_direction_pattern: positive\n    pct_positive_cells: 93.3\n    total_flagged: 57\n    flag_rate: 0.95\n- exp_id: exp-ml-classifier-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    auroc_avg_25pct:\n      lz_star: 0.86\n      lr_resp: 0.899\n      rf_resp: 0.885\n      lr_resp_summ: 0.909\n      rf_resp_summ: 0.913\n    auroc_avg_5pct:\n      lz_star: 0.675\n      best_ml: 0.575\n    auroc_avg_10pct:\n      lz_star: 0.763\n      best_ml: 0.712\n    lz_star_advantage_low_contam: +0.10 AUROC at 5%, +0.05 at 10%\n    ml_advantage_high_contam: +0.05 at 25%, +0.16 at 50%\n    key_finding: lz* outperforms supervised ML at low contamination (5-10%) without\n      any training data; ML only wins at 25%+ where signal is already strong\n- exp_id: exp-fdr-correction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    flagged_uncorrected: 57/60 (95%)\n    flagged_bh_fdr: 57/60 (95%)\n    flagged_bonferroni: not_computed_but_expected_similar\n    correction_scope: global_60_tests\n    unflagged_cells:\n    - Yi-Lightning×arc_c (bh_p=0.098)\n    - 360GPT2-Pro×humaneval (bh_p=0.134)\n    - Yi-Lightning×humaneval (bh_p=0.181)\n    note: Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale\n      FDR (24800+ tests) deferred to leaderboard audit.\n- exp_id: exp-clean-control-delta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    clean_vs_clean_mean_abs:\n      mmlu: 0.01\n      hellaswag: 0.125\n      gsm8k: 0.021\n      arc_c: 0.095\n      humaneval: 0.02\n    clean_vs_clean_all_nonsig: true\n    clean_vs_contam_all_sig: true\n    cohens_d:\n      mmlu: 2.66\n      hellaswag: 1.85\n      gsm8k: 1.85\n      arc_c: 0.45\n      humaneval: 1.07\n    arc_c_note: d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10\n- exp_id: exp-natural-experiment\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 21\n    n_benchmarks: 4\n    n_complete_pairs: 9\n    significant_benchmarks:\n      HellaSwag:\n        mean_deviation: -3.4\n        t_stat: -3.97\n        p_value: 0.001\n        interpretation: SFT systematically decreases person-fit on HellaSwag\n      GSM8K:\n        mean_deviation: 3.92\n        t_stat: 3.35\n        p_value: 0.009\n        interpretation: SFT systematically increases person-fit on GSM8K\n    non_significant_benchmarks:\n      MMLU:\n        p_value: 0.15\n      ARC-Challenge:\n        p_value: 0.38\n    individual_outliers: 0\n    key_finding: HellaSwag and GSM8K show significant systematic SFT effects on lz*,\n      but no individual pair shows benchmark-specific contamination outliers. P2-optional\n      per Director assessment.\n- exp_id: exp-v1-irt-refit-expanded\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 178\n    n_items: 14042\n    3pl_a_pearson_r: 0.127\n    2pl_a_pearson_r: -0.029\n    3pl_b_pearson_r: 0.663\n    reason: 'N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination\n      failure confirms Path D dead.'\n- exp_id: exp-4pl-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hypothesis_confirmed: true\n    far_4pl: ~5% (well-calibrated)\n    far_3pl: 4.7-16.5% (inflated)\n    far_2pl: 50-100% (catastrophic, unusable)\n    mean_power_gain_4pl_vs_3pl:\n      MMLU: +27.3pp\n      HellaSwag: +26.1pp\n      GSM8K: +20.3pp\n      ARC_C: +14.8pp\n      HumanEval: +13.7pp\n    max_power_gain_4pl_vs_3pl:\n      MMLU: +49.0pp\n      HellaSwag: +59.6pp\n      GSM8K: +39.7pp\n      ARC_C: +54.6pp\n      HumanEval: +30.6pp\n    power_at_25pct:\n      4PL:\n        MMLU: 0.776\n        HellaSwag: 0.534\n        GSM8K: 0.73\n        ARC_C: 0.132\n        HumanEval: 0.318\n      3PL:\n        MMLU: 0.329\n        HellaSwag: 0.28\n        GSM8K: 0.334\n        ARC_C: 0.091\n        HumanEval: 0.165\n    d_bucket_analysis: 'd<0.8: +6.8pp to +61.2pp; d>=0.95: negligible'\n    key_finding: 4PL d parameter essential for LLM contamination detection. 46% MMLU\n      items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely\n      miscalibrated (FAR 50-100%).\n- exp_id: exp-domain-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_mmlu_accuracy: 100% (14042/14042)\n    gemini_domain_concentrated: false\n    gemini_subjects_flagged: 50/57 (lz*>1.96)\n    gemini_category_lz:\n      STEM: 21.2\n      Humanities: 17.9\n      Social Sciences: 15.9\n      Other: 15.3\n    doubao_negative_lz: true\n    doubao_category_lz:\n      STEM: -2\n      Humanities: -13\n      Social_Sciences: -14.8\n      Other: 4.4\n    hunyuan_uneven:\n      STEM: 1.8\n      Social_Sciences: 13.9\n    yi_lightning_highest_mmlu_lz: 48.2\n    qwen_plus_second_highest: 44.9\n    mistral_flagged_subjects: 55/57\n- exp_id: exp-ctrl-contam-pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohens_d_contam15: 6.575\n    cohens_d_contam15_ci:\n    - 4.514\n    - 15.199\n    cohens_d_contam50: 1.897\n    cohens_d_contam50_ci:\n    - 1.041\n    - 4.923\n    clean_n10_mean_lz: 8.684\n    clean_n10_sd_lz: 0.735\n    contam15_lz: 3.849\n    contam50_lz: 7.289\n    n_clean_seeds: 10\n    n_items: 14042\n- exp_id: exp-4pl-real-data-degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    correlation_4pl_vs_3pl:\n      pearson_r: 0.225\n      rmse: 68.41\n    most_affected_benchmark: MMLU (mean |Δlz*|=58.3, 46% items d<0.95)\n    most_affected_model: 'DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6'\n    low_ability_models_impact: '|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)'\n    bias_direction: 3PL systematically depresses high-ability models' lz* (d=1 makes\n      P→1, amplifying few-error aberrance)\n    key_finding: Ignoring d parameter makes lz* completely unreliable for high-ability\n      models — d-induced bias far exceeds any contamination signal\n- exp_id: exp-ctrl-contam-pilot-clean-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-clean-s2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-15\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-50\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-clean-s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: 8.0806\n    accuracy: 0.6783\n    theta_mle: -0.1068\n    cohens_d_n3:\n      contam_15:\n        delta: -4.34\n        d: -3.58\n      contam_50:\n        delta: -1.9\n        d: -1.56\n    baseline_n3:\n      mean: 7.3449\n      std: 1.2137\n    baseline_n2:\n      mean: 6.9771\n      std: 1.4609\n- exp_id: exp-ctrl-contam-llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_corrected: true\n    method: Snijders (2001) lz*\n    clean_lz_star: 0.8446\n    clean_s2_lz_star: -0.1823\n    clean_s3_lz_star: -1.0844\n    clean_mean_lz_star: -0.1407\n    clean_std_lz_star: 0.9652\n    clean_acc: 0.5914\n    clean_theta: -0.6661\n    contam_15_lz_star: -2.9922\n    contam_15_acc: 0.6654\n    contam_15_theta: -0.276\n    contam_15_delta_lz_star: -2.8515\n    contam_50_lz_star: -3.3313\n    contam_50_acc: 0.6983\n    contam_50_theta: -0.149\n    contam_50_delta_lz_star: -3.1906\n    cohens_d_contam_15_ddof1: -2.95\n    cohens_d_contam_50_ddof1: -3.31\n    theta_fixed: -0.666\n    contam_15_lz_star_fixed: 0.959\n    contam_50_lz_star_fixed: 1.172\n    dose_response_ratio_free: 1.09\n    dose_response_ratio_fixed: 2.87\n    monotonic_free: true\n    monotonic_fixed: true\n- exp_id: exp-ctrl-contam-llama-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: 0.8446\n    acc: 0.5914\n    theta: -0.6661\n    seed: 42\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-llama-contam15\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -2.9922\n    acc: 0.6654\n    theta_mle: -0.276\n    acc_seen: 0.742\n    acc_unseen: 0.652\n    delta_lz_star: -2.8515\n    cohens_d_ddof1: -2.95\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-llama-contam50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -3.3313\n    acc: 0.6983\n    theta_mle: -0.149\n    acc_seen: 0.735\n    acc_unseen: 0.661\n    delta_lz_star: -3.1906\n    cohens_d_ddof1: -3.31\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-llama-clean-s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -0.1823\n    acc: 0.5954\n    theta: -0.63\n    seed: 123\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-llama-clean-s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -1.0844\n    acc: 0.5943\n    theta: -0.64\n    seed: 456\n    method: Snijders (2001) lz*\n- exp_id: exp-post-rl\n  name: ''\n  status: ANALYZING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-baseline-comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model_level:\n      qwen_contam15_lz_star_d: -3.42\n      qwen_contam50_lz_star_d: -0.99\n      llama_contam15_lz_star_d: -2.95\n      llama_contam50_lz_star_d: -3.31\n      qwen_contam15_acc_zscore_d: 160.6\n      qwen_contam15_ht_d: 3.21\n      llama_contam15_u3_d: -3.69\n    item_level_auroc:\n      lz_star_itemwise:\n        qwen_15: 0.536\n        qwen_50: 0.535\n        llama_15: 0.528\n        llama_50: 0.536\n      irt_residual:\n        qwen_15: 0.578\n        qwen_50: 0.563\n        llama_15: 0.582\n        llama_50: 0.581\n      lr_cross_model:\n        qwen_15: 0.586\n        qwen_50: 0.567\n        llama_15: 0.592\n        llama_50: 0.585\n      rf_within_model:\n        qwen_50: 0.63\n        llama_50: 0.629\n      random: 0.5\n    conclusion_summary: 'Model-level: all methods detect contamination (lz* d=-2.95~-3.42).\n      Item-level: all methods weak (max AUROC=0.63 with oracle). lz* advantage = unsupervised\n      + interpretable, not item-level superiority.'\n- exp_id: exp-ctrl-contam-mistral\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    clean:\n      lz_star: 5.4175\n      acc: 0.5138\n      theta: -1.1569\n    contam_15:\n      lz_star: -1.3849\n      acc: 0.5949\n      acc_seen: 0.7436\n      acc_unseen: 0.5686\n      theta: -0.7129\n    contam_50:\n      lz_star: -3.1503\n      acc: 0.6732\n      acc_seen: 0.7523\n      acc_unseen: 0.5941\n      theta: -0.3027\n    delta_lz_star_15: -6.8024\n    delta_lz_star_50: -8.5678\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-mistral-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: 5.4175\n    acc_overall: 0.5138\n    acc_seen: null\n    acc_unseen: 0.5138\n    theta_mle: -1.1569\n    lz_star_seen: null\n    lz_star_unseen: 5.4175\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-mistral-contam15\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -1.3849\n    acc_overall: 0.5949\n    acc_seen: 0.7436\n    acc_unseen: 0.5686\n    theta_mle: -0.7129\n    lz_star_seen: -1.0838\n    lz_star_unseen: -0.0956\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-mistral-contam50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -3.1503\n    acc_overall: 0.6732\n    acc_seen: 0.7523\n    acc_unseen: 0.5941\n    theta_mle: -0.3027\n    lz_star_seen: -1.3701\n    lz_star_unseen: -0.9972\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-qwen-clean-s4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6786\n    lz_star: 8.967\n    theta_mle: -0.109\n    n_items: 14042\n- exp_id: exp-ctrl-contam-qwen-clean-s5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6787\n    lz_star: 8.532\n    theta_mle: -0.088\n    n_items: 14042\n- exp_id: exp-ctrl-contam-qwen-clean-s6\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6771\n    lz_star: 8.245\n    theta_mle: -0.1036\n    n_items: 14042\n    loss: 1.354\n    steps: 939\n- exp_id: exp-ctrl-contam-qwen-clean-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6783\n    lz_star: 8.77\n    theta_mle: -0.0892\n    n_items: 14042\n- exp_id: exp-ctrl-contam-qwen-clean-s8\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6768\n    lz_star: 9.111\n    theta_mle: -0.1035\n    n_items: 14042\n    loss: 1.352\n    steps: 939\n- exp_id: exp-constat-comparison\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-mia-mink-comparison\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    base_auc_loss: 0.486\n    base_auc_mink10: 0.493\n    base_auc_minkpp10: 0.488\n    sft_auc_loss: 0.592\n    sft_auc_mink10: 0.611\n    sft_auc_minkpp10: 0.569\n- exp_id: exp-arcc-benchmark\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    19912_clean_s1_acc: 0.902\n    19912_clean_s1_lz: -5.448\n    19912_clean_s2_acc: 0.895\n    19912_clean_s2_lz: -5.433\n    19912_contam15_acc: 0.909\n    19912_contam15_lz: -4.917\n    19912_contam15_lz_seen: 0.568\n    19912_contam50_acc: 0.942\n    19912_contam50_lz: -4.573\n    19912_contam50_lz_seen: -0.331\n    35694_clean_s1_acc: 0.895\n    35694_clean_s1_lz: -5.511\n    35694_clean_s2_acc: 0.898\n    35694_clean_s2_lz: -5.493\n    35694_contam15_acc: 0.909\n    35694_contam15_lz: -5.032\n    35694_contam15_lz_seen: 0.186\n    35694_contam50_acc: 0.946\n    35694_contam50_lz: -4.185\n    35694_contam50_lz_seen: -0.475\n- exp_id: exp-ctrl-contam-qwen-clean-s9\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6743\n    lz_star: 9.013\n    theta_mle: -0.1242\n    n_items: 14042\n- exp_id: exp-ctrl-contam-qwen-clean-s10\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    accuracy: 0.676\n    lz_star: 8.149\n    theta_mle: -0.116\n    n_items: 14042\n- exp_id: exp-arcc-clean-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    accuracy: 0.8949\n    theta_mle: 0.6872\n    lz_star: -5.5107\n    n_items: 295\n- exp_id: exp-arcc-clean-s2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: arcc-clean-s7\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: arcc-clean-s8\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: arcc-clean-s9\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: arcc-clean-s10\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-llama-clean-s4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:42:56.935Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:42:56.935Z",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-21T12:42:56.955Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Post-RL destroys all person-fit signals; HT matches lz* everywhere; reframe as framework + empirical characterization paper
核心假设：['exp-post-rl: GRPO eliminates detection for all binary-only methods (|d|<0.5)', 'HT matches or exceeds lz* in all tested conditions (no empirical differentiation)', 'MIA/Min-K++ achieve AUROC 0.65+ on SFT contamination (minimal-information penalty is real)', 'ARC-C too small for reliable detection even with θ-fixed (|d|<0.5)', 'Cross-family generalizability limited to SFT-only contamination scope']
关键指标范围：{'post_rl_lz_star_cohens_d': [0.0, 0.5], 'post_rl_ht_cohens_d': [0.0, 0.5], 'post_rl_mia_auroc': [0.45, 0.55], 'n_families_validated': [2, 2], 'n_baselines_beaten': [2, 3], 'arcc_theta_fixed_d': [0.0, 0.5], 'constat_retest_auroc': [0.8, 0.95], 'mink_sft_auroc': [0.6, 0.75]}
叙事方向："Reframe: NOT a detection superiority paper. Three reframing angles for same venue: (A) Empirical characterization paper — first systematic study of how LLM response patterns relate to IRT assumptions. Universal 4PL misfit (57/60 flagged) is a novel finding about LLM cognition. θ-shift mechanism is a methodological contribution to contamination science regardless of detection power. (B) Scope-honest detection paper — IRT-FIT detects intentional SFT contamination (|d|>2.9 across two families) with explicit scope boundary: post-RL training smooths binary signal below detection threshold for ALL binary-only methods. This negative result (RL boundary) is itself a contribution — it maps the detection frontier's limits. Frame as: 'we establish where binary detection works and precisely where it fails.' (C) Framework + toolkit paper — open-source IRT-FIT toolkit + 13K model data availability + memorization fraction methodology. Contribution is the framework (connecting psychometrics to LLM evaluation) not detection SOTA. θ-shift analysis, seen/unseen decomposition, and dose-response characterization are methodological contributions independent of absolute detection power. Still targets EMNLP as evaluation methodology with community tooling impact."

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
Detection power increases with benchmark size (n_items) and varies with contamination level, following an empirical power function (R²=0.65) that provides approximate practical guidance for practitioners assessing detectability on benchmarks of known size — but should NOT be described as "predictive theory" or "scaling law." Two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted ("expected") power. Both upper bound and adjusted power should be reported. **Baseline comparison (exp-baseline-comparison)**: At model level, lz* achieves 8× the effect size of classical person-fit statistics (Guttman/U3) on identical data (|d|=3.42 vs |d|=0.43 for Qwen 15%), demonstrating the value of full 4PL IRT parameterization. At item level, ALL binary-only methods achieve near-random discrimination (AUROC 0.52–0.63, including oracle supervised classifiers), revealing contamination produces a diffuse statistical signature detectable only through model-level aggregation over thousands of items. Accuracy z-score trivially detects in controlled settings (z=160 due to near-zero accuracy variance) but lacks specificity in real-world scenarios. The IRT framework enables principled aggregation by calibrating each item's expected response probability.

**Claim 3 (Empirical Findings from Real LLM Data)**:
Three empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.

## Story Spine

**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.

**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.

**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.

**Headline result template**: "Using only binary response patterns from the target model (with externally calibrated IRT item parameters), IRT-FIT detects controlled contamination with |Cohen's d|>2.9 across two model families (Qwen, Llama), achieving 8× the effect size of classical person-fit statistics (Guttman/U3). The HT statistic (requiring only item difficulty) achieves comparable model-level detection power — the IRT person-fit family collectively dominates simpler indices, with ℓz*'s advantage lying in mechanistic interpretability (θ-shift analysis, memorization fraction quantification) and [pending: post-RL robustness vs HT]. Model-level aggregation over thousands of items yields robust detection where all item-level methods are near-random (AUROC 0.52–0.63). The IRT framework provides unique mechanistic insight: θ-shift analysis reveals how contamination raises ability estimates, and memorization fraction (35–38%) bridges theoretical power (97.9%) and observed detection capacity."

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
| R9 | "No same-level binary-only baselines" | **Completed (exp-baseline-comparison)**: Model-level: lz* |d|=3.42 vs Guttman/U3 |d|=0.43 (8× gap) — full IRT parameterization far exceeds difficulty-only person-fit. **HT is nearly as powerful as ℓz* (avg |d| comparable)** — the "8×" headline must include HT comparison to avoid selective framing. Item-level: all methods near-random (AUROC 0.52–0.63). acc z-score detects trivially (z=160) but lacks specificity. | exp-baseline-comparison |
| R12 | "HT ≈ ℓz* — why use ℓz*?" | **[Dream D2 三档一致]** HT achieves comparable |d| with weaker requirements (difficulty only, no 4PL). **四场景应对 (D022, Reviewer validated)**：(Best) HT post-RL 丢失 + ℓz* 保留 → headline 差异化；(Good) HT 弱化 + ℓz* 更强 → quantitative comparison；(Neutral) 均保留 → 转用数据无关差异化（见下）；(Bad) 均丢失 → negative-as-contribution, scope SFT。**数据无关差异化（任何场景均可用）**：(i) ℓz* 有参数化 null (≈N(0,1), bootstrap 已验证) → 可直接假设检验, HT 无此性质；(ii) Snijders 校正补偿 θ 估计误差 (Var*=Var_l - C²/I(θ)), HT 无此校正；(iii) ℓz* 用 a/b/c/d 四参数加权 item 贡献, HT 仅用 b → MMLU 跨 57 科目 item 异质性大时 ℓz* 理论更精确。这些点不依赖 post-RL 结果，论文中应明确讨论。 | exp-baseline-comparison, exp-post-rl |
| R13 | "Minimal-information overstates" | **[Dream D2 三档一致]** "Minimal-information operating point" obscures PSN-IRT 4PL parameter dependency. Reframe to "minimal information **from the target model**" or "minimal runtime information" — explicitly acknowledge PSN-IRT calibration as an external input requirement. | — |
| R10 | "Leaderboard audit baseline unreliable" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |
| R11 | "Power function is upper bound" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |

## Key Narrative Elements (from External Review + Distillation)

1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
2. **Definitional pivot (à la ConStat)** — "All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?" This reframes our work as problem reformulation, not just cross-domain transfer.
3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.
4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim "leaderboard audit" or "large-scale detection" in current paper.
5. **Inverted-U as empirical characterization** — Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Simulation fit R²=0.957; real-data fit R²=0.65 (gap due to SFT generalization). Frame as "empirical trend" not "theory/law."
6. **Baseline comparison as evidence for model-level aggregation** — Item-level detection is near-random for ALL binary-only methods (including oracle RF). This is NOT a weakness — it reveals that contamination signal is diffuse (memorization fraction ~35%). Model-level lz* aggregates 14K weak signals into |d|>2.9. Frame item-level weakness as supporting evidence: "any method that aggregates is better than any method that localizes." lz* vs Guttman/U3 8× gap proves IRT parameterization matters. acc z-score is sensitive but non-specific (sensitivity-specificity tradeoff).
7. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
8. **Terminology guard** — NEVER use "binary information bottleneck" or "information-theoretic lower bound for all binary-only methods." We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: "IRT person-fit as a principled framework at the minimal-information operating point."
9. **Memorization fraction cross-family consistency** — MF is 35–38% at 15% contamination across Qwen (0.38) and Llama (0.35), only 3pp difference. Consistency strengthens generalizability. MF may vary with contamination mechanism (full FT vs QLoRA), model capacity, and benchmark difficulty — acknowledge in Limitations as deployment bootstrapping problem.
10. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.
9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.
10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are "honest negative results that become positive contributions": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: "the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative."
11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as "principled detection with quantified operating characteristics + θ-shift boundary condition." Headline: "We don't just detect — we characterize, including the conditions under which detection degrades." Do NOT claim "state-of-the-art detection."
12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.
13. **Cross-family baseline lz* divergence (Reviewer WARNING)** — Clean lz* spans ~9σ: Qwen +8.68, Mistral +5.42, Llama -0.14. 固定阈值检测失效（Qwen contam_15 lz*=+3.85 仍为正值）。论文必须：(a) 明确 IRT-FIT 是相对检测（Δlz*/Cohen's d），非绝对阈值；(b) 展示 clean baseline lz* 跨家族差异表；(c) 预防性回答"contam_15 lz*=+3.85 为正值为何算污染"（因为 Δlz*=-4.83 是大效应）；(d) lz* baseline 作为"模型内部一致性"指标——Mistral acc 最低(0.514)但 lz* 第二高(+5.42)，说明 lz* 捕捉 difficulty-ordering 一致性而非准确率。
14. **Inverted-U 是模型相关的** — Qwen 在 15%→50% 区间出现强 inversion（Δlz* 50%=-1.39 << 15%=-4.83），Llama 和 Mistral 在此区间 Δlz* 单调增大。Inverted-U 在 free-θ 下由 baseline misfit 调制——高 baseline lz* (Qwen +8.68) 的模型更容易出现 non-monotonicity。论文不能 claim inverted-U 为 universal phenomenon，需加 model-dependent caveat。θ-fixed 分析仍恢复所有家族的 monotonicity — 这是 θ-fixed 贡献的关键证据。
15. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look "normal") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.

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
    cohens_d_contam15: 6.575
    cohens_d_contam15_ci:
    - 4.514
    - 15.199
    cohens_d_contam50: 1.897
    cohens_d_contam50_ci:
    - 1.041
    - 4.923
    clean_n10_mean_lz: 8.684
    clean_n10_sd_lz: 0.735
    contam15_lz: 3.849
    contam50_lz: 7.289
    n_clean_seeds: 10
    n_items: 14042
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
  status: DONE
  conclusion: success
  metrics:
    lz_star: 0.8446
    acc: 0.5914
    theta: -0.6661
    seed: 42
    method: Snijders (2001) lz*
- exp_id: exp-ctrl-contam-llama-contam15
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star: -2.9922
    acc: 0.6654
    theta_mle: -0.276
    acc_seen: 0.742
    acc_unseen: 0.652
    delta_lz_star: -2.8515
    cohens_d_ddof1: -2.95
    method: Snijders (2001) lz*
- exp_id: exp-ctrl-contam-llama-contam50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star: -3.3313
    acc: 0.6983
    theta_mle: -0.149
    acc_seen: 0.735
    acc_unseen: 0.661
    delta_lz_star: -3.1906
    cohens_d_ddof1: -3.31
    method: Snijders (2001) lz*
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
- exp_id: exp-post-rl
  name: ''
  status: ANALYZING
  conclusion: failed
  metrics: {}
- exp_id: exp-baseline-comparison
  name: ''
  status: DONE
  conclusion: success
  metrics:
    model_level:
      qwen_contam15_lz_star_d: -3.42
      qwen_contam50_lz_star_d: -0.99
      llama_contam15_lz_star_d: -2.95
      llama_contam50_lz_star_d: -3.31
      qwen_contam15_acc_zscore_d: 160.6
      qwen_contam15_ht_d: 3.21
      llama_contam15_u3_d: -3.69
    item_level_auroc:
      lz_star_itemwise:
        qwen_15: 0.536
        qwen_50: 0.535
        llama_15: 0.528
        llama_50: 0.536
      irt_residual:
        qwen_15: 0.578
        qwen_50: 0.563
        llama_15: 0.582
        llama_50: 0.581
      lr_cross_model:
        qwen_15: 0.586
        qwen_50: 0.567
        llama_15: 0.592
        llama_50: 0.585
      rf_within_model:
        qwen_50: 0.63
        llama_50: 0.629
      random: 0.5
    conclusion_summary: 'Model-level: all methods detect contamination (lz* d=-2.95~-3.42).
      Item-level: all methods weak (max AUROC=0.63 with oracle). lz* advantage = unsupervised
      + interpretable, not item-level superiority.'
- exp_id: exp-ctrl-contam-mistral
  name: ''
  status: DONE
  conclusion: success
  metrics:
    clean:
      lz_star: 5.4175
      acc: 0.5138
      theta: -1.1569
    contam_15:
      lz_star: -1.3849
      acc: 0.5949
      acc_seen: 0.7436
      acc_unseen: 0.5686
      theta: -0.7129
    contam_50:
      lz_star: -3.1503
      acc: 0.6732
      acc_seen: 0.7523
      acc_unseen: 0.5941
      theta: -0.3027
    delta_lz_star_15: -6.8024
    delta_lz_star_50: -8.5678
    method: Snijders (2001) lz*
- exp_id: exp-ctrl-contam-mistral-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star: 5.4175
    acc_overall: 0.5138
    acc_seen: null
    acc_unseen: 0.5138
    theta_mle: -1.1569
    lz_star_seen: null
    lz_star_unseen: 5.4175
    method: Snijders (2001) lz*
- exp_id: exp-ctrl-contam-mistral-contam15
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star: -1.3849
    acc_overall: 0.5949
    acc_seen: 0.7436
    acc_unseen: 0.5686
    theta_mle: -0.7129
    lz_star_seen: -1.0838
    lz_star_unseen: -0.0956
    method: Snijders (2001) lz*
- exp_id: exp-ctrl-contam-mistral-contam50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star: -3.1503
    acc_overall: 0.6732
    acc_seen: 0.7523
    acc_unseen: 0.5941
    theta_mle: -0.3027
    lz_star_seen: -1.3701
    lz_star_unseen: -0.9972
    method: Snijders (2001) lz*
- exp_id: exp-ctrl-contam-qwen-clean-s4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6786
    lz_star: 8.967
    theta_mle: -0.109
    n_items: 14042
- exp_id: exp-ctrl-contam-qwen-clean-s5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6787
    lz_star: 8.532
    theta_mle: -0.088
    n_items: 14042
- exp_id: exp-ctrl-contam-qwen-clean-s6
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6771
    lz_star: 8.245
    theta_mle: -0.1036
    n_items: 14042
    loss: 1.354
    steps: 939
- exp_id: exp-ctrl-contam-qwen-clean-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6783
    lz_star: 8.77
    theta_mle: -0.0892
    n_items: 14042
- exp_id: exp-ctrl-contam-qwen-clean-s8
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6768
    lz_star: 9.111
    theta_mle: -0.1035
    n_items: 14042
    loss: 1.352
    steps: 939
- exp_id: exp-constat-comparison
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp-mia-mink-comparison
  name: ''
  status: PREPARING
  conclusion: ''
  metrics:
    base_auc_loss: 0.486
    base_auc_mink10: 0.493
    base_auc_minkpp10: 0.488
    sft_auc_loss: 0.592
    sft_auc_mink10: 0.611
    sft_auc_minkpp10: 0.569
- exp_id: exp-arcc-benchmark
  name: ''
  status: PREPARING
  conclusion: ''
  metrics:
    19912_clean_s1_acc: 0.902
    19912_clean_s1_lz: -5.448
    19912_clean_s2_acc: 0.895
    19912_clean_s2_lz: -5.433
    19912_contam15_acc: 0.909
    19912_contam15_lz: -4.917
    19912_contam15_lz_seen: 0.568
    19912_contam50_acc: 0.942
    19912_contam50_lz: -4.573
    19912_contam50_lz_seen: -0.331
    35694_clean_s1_acc: 0.895
    35694_clean_s1_lz: -5.511
    35694_clean_s2_acc: 0.898
    35694_clean_s2_lz: -5.493
    35694_contam15_acc: 0.909
    35694_contam15_lz: -5.032
    35694_contam15_lz_seen: 0.186
    35694_contam50_acc: 0.946
    35694_contam50_lz: -4.185
    35694_contam50_lz_seen: -0.475
- exp_id: exp-ctrl-contam-qwen-clean-s9
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.6743
    lz_star: 9.013
    theta_mle: -0.1242
    n_items: 14042
- exp_id: exp-ctrl-contam-qwen-clean-s10
  name: ''
  status: PREPARING
  conclusion: ''
  metrics:
    accuracy: 0.676
    lz_star: 8.149
    theta_mle: -0.116
    n_items: 14042
- exp_id: exp-arcc-clean-s1
  name: ''
  status: PREPARING
  conclusion: ''
  metrics:
    accuracy: 0.8949
    theta_mle: 0.6872
    lz_star: -5.5107
    n_items: 295
- exp_id: exp-arcc-clean-s2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: arcc-clean-s7
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: arcc-clean-s8
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: arcc-clean-s9
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: arcc-clean-s10
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp-ctrl-contam-llama-clean-s4
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
  "promptId": "3802086b-367b-4716-be9c-2a2b69b9c445",
  "type": "user",
  "uuid": "8d21082c-cc5c-4517-b780-fb350c2bc107",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:42:56.953Z_

```json
{
  "parentUuid": "8d21082c-cc5c-4517-b780-fb350c2bc107",
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
  "uuid": "138e66e1-3cc3-45de-a6b5-109237bd2d7a",
  "timestamp": "2026-05-21T12:42:56.953Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:42:56.953Z_

```json
{
  "parentUuid": "138e66e1-3cc3-45de-a6b5-109237bd2d7a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6953e240-f27d-43f8-940e-a2bd3856a443",
  "timestamp": "2026-05-21T12:42:56.953Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Post-RL destroys all person-fit signals; HT matches lz* everywhere; reframe as framework + empirical characterization paper 核心假设：['exp-post-rl: GRPO elimi…",
  "leafUuid": "6953e240-f27d-43f8-940e-a2bd3856a443",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT contamination detection: worst-case scenario characterization",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:43:03.909Z_

I'll first check the experiment plan to identify all experiments with `status: planned` that need predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6953e240-f27d-43f8-940e-a2bd3856a443",
  "isSidechain": false,
  "requestId": "req_011CbFjUma5GFp4n4Y1ZsQXy",
  "type": "assistant",
  "uuid": "60396906-eee4-43de-93e9-d625729b7e8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mp2KeNbUhTyAp56egVqyX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26847,
      "cache_read_input_tokens": 11841,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 80,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26847
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

_source line 9 · 2026-05-21T12:43:03.945Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Jkbc1kyvribx2zy7cpzYe9`</summary>

```json
{
  "pattern": "**/*experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60396906-eee4-43de-93e9-d625729b7e8b",
  "isSidechain": false,
  "requestId": "req_011CbFjUma5GFp4n4Y1ZsQXy",
  "type": "assistant",
  "uuid": "d94cbf32-86a4-4089-b320-ddbea22be66f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Mp2KeNbUhTyAp56egVqyX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26847,
      "cache_read_input_tokens": 11841,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 80,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26847
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

_source line 10 · 2026-05-21T12:43:04.161Z_

<details><summary>↩ Tool result · `toolu_01Jkbc1kyvribx2zy7cpzYe9`</summary>

```text
projects/irt_personfit_contam/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d94cbf32-86a4-4089-b320-ddbea22be66f",
  "isSidechain": false,
  "promptId": "3802086b-367b-4716-be9c-2a2b69b9c445",
  "type": "user",
  "uuid": "d8dd0a9c-7f82-4f56-b10a-ae5ad904c8cf",
  "toolUseResult": {
    "filenames": [
      "projects/irt_personfit_contam/experiment_plan.yaml"
    ],
    "durationMs": 206,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "d94cbf32-86a4-4089-b320-ddbea22be66f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T12:43:08.666Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DuA5SXmbwB3XJj1aRK42Qm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8dd0a9c-7f82-4f56-b10a-ae5ad904c8cf",
  "isSidechain": false,
  "requestId": "req_011CbFjVKmL1S2QnDSw22GrP",
  "type": "assistant",
  "uuid": "94792eed-19c6-4250-8f7d-2c4d01304931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvmfjZGLxtwSMcy5a4LEVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 108,
      "cache_read_input_tokens": 38688,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 38688,
          "cache_creation_input_tokens": 108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 108
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

_source line 12 · 2026-05-21T12:43:08.674Z_

<details><summary>↩ Tool result · `toolu_01DuA5SXmbwB3XJj1aRK42Qm`</summary>

```text
1	experiments:
2	  # === P0: Must-do (headline results) ===
3	
4	  - id: exp-two-sided
5	    registry_id: exp-two-sided
6	    claim: 2
7	    description: "实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case study）。包括 bootstrap confidence interval 和 FDR 控制。"
8	    priority: P0
9	    gpu_budget_hours: 0
10	    deps: []
11	    status: planned
12	    notes: "CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。"
13	
14	  - id: exp-extended-sim
15	    registry_id: exp-extended-sim
16	    claim: 2
17	    description: "扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让 MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向 lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。"
18	    priority: P0
19	    gpu_budget_hours: 0
20	    deps: [exp-two-sided]
21	    status: planned
22	    notes: "CPU only. 依赖 exp-two-sided 的双侧框架定义。"
23	
24	  - id: exp-ctrl-contam-pilot
25	    claim: "1,2,3"
26	    description: "快速验证：Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU only。测量 Δlz*(clean→contaminated) 是否显著。增加第二个 0% seed 作为 clean-vs-clean noise floor baseline (Reviewer Q2/Q4)。Eval 时区分 seen/unseen items 以实测 memorization fraction (Reviewer Q3/W9)。这是论文 go/no-go 信号。"
27	    priority: P0-CRITICAL
28	    gpu_budget_hours: 12
29	    deps: []
30	    status: planned
31	    notes: "GPU 恢复后第一优先。4 conditions × ~3 hrs = ~12 GPU-hrs (+2h for second 0% seed)。关键输出: (a) Δlz* 显著性, (b) clean-vs-clean Δlz* ≈ 0 验证, (c) memorization fraction = (Δacc_seen - Δacc_unseen)/Δacc_seen, (d) adjusted power = theory × memorization fraction。D010 要求。"
32	
33	  - id: exp-ctrl-contam
34	    claim: "1,2,3"
35	    description: "完整控制实验：在 4 个模型上用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量 Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。"
36	    priority: P0
37	    gpu_budget_hours: 80
38	    deps: [exp-ctrl-contam-pilot]
39	    status: planned
40	    notes: "模型: Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3。Benchmark: MMLU + GSM8K + HellaSwag。4 模型 × 6 levels × 3 benchmarks。"
41	
42	  - id: exp-empirical-null
43	    registry_id: exp-empirical-null
44	    claim: 1
45	    description: "Bootstrap empirical null 分析：量化 lz* 在真实 LLM 数据上的 systematic bias（null mean ≠ 0, null std ≠ 1），为 Calibration Gap Analysis 提供定量证据。包含 Q-Q plots、KS tests、bias 量化表、unflagged cells 深度分析。"
46	    priority: P0
47	    gpu_budget_hours: 0
48	    deps: [exp-two-sided]
49	    status: planned
50	    notes: "CPU only. 复用 exp-two-sided v2 的 bootstrap 逻辑，但保存完整中间分布。~2h 开发+运行。"
51	
52	  - id: exp-power-theory
53	    registry_id: exp-power-theory
54	    claim: 2
55	    description: "推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A 模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。"
56	    priority: P1
57	    gpu_budget_hours: 0
58	    deps: [exp-extended-sim]
59	    status: planned
60	    notes: "纯理论推导 + 数值验证。CPU only."
61	
62	  # === P1: Important (robustness + differentiation) ===
63	
64	  - id: exp-leaderboard-data-recon
65	    registry_id: exp-leaderboard-data-recon
66	    claim: 3
67	    description: "Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results 是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。"
68	    priority: P0
69	    gpu_budget_hours: 0
70	    deps: []
71	    status: planned
72	    notes: "纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。"
73	
74	  - id: exp-leaderboard-audit
75	    claim: 3
76	    description: "Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark 污染率随时间趋势。"
77	    priority: ABANDONED
78	    gpu_budget_hours: 20
79	    deps: [exp-two-sided, exp-leaderboard-data-recon]
80	    status: abandoned
81	    notes: "D011: v1-irt-refit a_r=0.111 + item alignment 54.56% → 13K audit 不可行。数据可用性写入 Discussion/Future Work。"
82	
83	  - id: exp-natural-experiment
84	    claim: 3
85	    description: "v1 leaderboard base→chat model pairs 自然实验：计算 Δlz* = lz*(chat) - lz*(base) 作为 SFT 效应代理。"
86	    priority: P2-optional
87	    gpu_budget_hours: 0
88	    deps: [exp-v1-irt-refit-pilot]
89	    status: deprioritized
90	    notes: "D013: a_r=0.111 导致 lz*≈accuracy-like, 仅 4-5 pairs 无统计检验能力。Reviewer 终审建议降级。"
91	
92	  - id: exp-v1-irt-refit-expanded
93	    claim: 3
94	    description: "扩大 v1 IRT 重拟合样本量至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。最终关闭 Path D。"
95	    priority: P0
96	    gpu_budget_hours: 0
97	    deps: [exp-v1-irt-refit-pilot]
98	    status: assigned
99	    notes: "CPU only. Reviewer 要求 N≥500 才能最终结论 Path D。阈值：a_r>0.4=可行, a_r<0.2=dead。"
100	
101	  - id: exp-4pl-ablation
102	    claim: 1
103	    description: "4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter d 对 false alarm 和 detection power 的影响。"
104	    priority: P2
105	    gpu_budget_hours: 0
106	    deps: [exp-extended-sim]
107	    status: planned
108	    notes: "CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。"
109	
110	  - id: exp-baseline-comparison
111	    claim: 1
112	    description: "与现有方法对比（≥5 baselines）：在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs baselines 的 AUROC/Type-I error。Baselines: (1) ConStat (re-test), (2) Min-K%++ (token probs), (3) accuracy z-score (已完成, CPU), (4) PPL-based detection (log-prob family 代表, 预期 RL-robust 测试中失败), (5) random baseline。量化 minimal-information 的代价（power 损失）。报告 bootstrap CIs（同行 6/8 不报告方差，这是我们的差异化优势）。"
113	    priority: P0-end
114	    gpu_budget_hours: 30
115	    deps: [exp-ctrl-contam]
116	    status: planned
117	    notes: "蒸馏显示同行 baseline 中位数 ~5 个。accuracy z-score 已完成(CPU)。ConStat 需 re-test, Min-K%++ 需 token probs, PPL 需 log-probs。exp-ctrl-contam 完成后立即执行。"
118	
119	  - id: exp-multiscale-lzm
120	    claim: "1,3"
121	    description: "实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化 lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。"
122	    priority: P2
123	    gpu_budget_hours: 0
124	    deps: [exp-two-sided]
125	    status: planned
126	    notes: "CPU only. 需要实现 lzm 公式。"
127	
128	  # === P2: Nice-to-have (expanded scope) ===
129	
130	  - id: exp-post-rl
131	    claim: 1
132	    description: "Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应 Wang et al. (2025) 的 MIA 失效问题。"
133	    priority: P2
134	    gpu_budget_hours: 40
135	    deps: [exp-ctrl-contam]
136	    status: planned
137	    notes: "GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。"
138	
139	  - id: exp-extra-benchmarks
140	    claim: "2,3"
141	    description: "扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。"
142	    priority: P2
143	    gpu_budget_hours: 10
144	    deps: [exp-extended-sim]
145	    status: planned
146	    notes: "取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。"
147	
148	  - id: exp-domain-analysis
149	    claim: 3
150	    description: "MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染是全面的还是集中在特定 domain。"
151	    priority: P2
152	    gpu_budget_hours: 0
153	    deps: [exp-two-sided]
154	    status: planned
155	    notes: "CPU only. 需要 MMLU item-to-domain 映射。"
156	
157	# === GPU Budget Summary (post-D011/D013) ===
158	# P0: ~92 GPU-hrs (ctrl-contam-pilot 12 + ctrl-contam 80)
159	# P0-end: ~30 GPU-hrs (baseline-comparison, 依赖 ctrl-contam)
160	# P2: ~50 GPU-hrs (post-rl 40 + extra-benchmarks 10) — DDL 压力下不现实
161	# ABANDONED: exp-leaderboard-audit (D011)
162	# Total active: ~122 GPU-hrs
163	# Available: 4× RTX 5090 32GB (bjb2-36806, SSH 不通)
164	# 已用: 0 GPU-hrs
165	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94792eed-19c6-4250-8f7d-2c4d01304931",
  "isSidechain": false,
  "promptId": "3802086b-367b-4716-be9c-2a2b69b9c445",
  "type": "user",
  "uuid": "66932a34-e91e-4b7d-b941-7c4c4fe32461",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/experiment_plan.yaml",
      "content": "experiments:\n  # === P0: Must-do (headline results) ===\n\n  - id: exp-two-sided\n    registry_id: exp-two-sided\n    claim: 2\n    description: \"实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case study）。包括 bootstrap confidence interval 和 FDR 控制。\"\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    status: planned\n    notes: \"CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\"\n\n  - id: exp-extended-sim\n    registry_id: exp-extended-sim\n    claim: 2\n    description: \"扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让 MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向 lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。\"\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-two-sided]\n    status: planned\n    notes: \"CPU only. 依赖 exp-two-sided 的双侧框架定义。\"\n\n  - id: exp-ctrl-contam-pilot\n    claim: \"1,2,3\"\n    description: \"快速验证：Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU only。测量 Δlz*(clean→contaminated) 是否显著。增加第二个 0% seed 作为 clean-vs-clean noise floor baseline (Reviewer Q2/Q4)。Eval 时区分 seen/unseen items 以实测 memorization fraction (Reviewer Q3/W9)。这是论文 go/no-go 信号。\"\n    priority: P0-CRITICAL\n    gpu_budget_hours: 12\n    deps: []\n    status: planned\n    notes: \"GPU 恢复后第一优先。4 conditions × ~3 hrs = ~12 GPU-hrs (+2h for second 0% seed)。关键输出: (a) Δlz* 显著性, (b) clean-vs-clean Δlz* ≈ 0 验证, (c) memorization fraction = (Δacc_seen - Δacc_unseen)/Δacc_seen, (d) adjusted power = theory × memorization fraction。D010 要求。\"\n\n  - id: exp-ctrl-contam\n    claim: \"1,2,3\"\n    description: \"完整控制实验：在 4 个模型上用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量 Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。\"\n    priority: P0\n    gpu_budget_hours: 80\n    deps: [exp-ctrl-contam-pilot]\n    status: planned\n    notes: \"模型: Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3。Benchmark: MMLU + GSM8K + HellaSwag。4 模型 × 6 levels × 3 benchmarks。\"\n\n  - id: exp-empirical-null\n    registry_id: exp-empirical-null\n    claim: 1\n    description: \"Bootstrap empirical null 分析：量化 lz* 在真实 LLM 数据上的 systematic bias（null mean ≠ 0, null std ≠ 1），为 Calibration Gap Analysis 提供定量证据。包含 Q-Q plots、KS tests、bias 量化表、unflagged cells 深度分析。\"\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-two-sided]\n    status: planned\n    notes: \"CPU only. 复用 exp-two-sided v2 的 bootstrap 逻辑，但保存完整中间分布。~2h 开发+运行。\"\n\n  - id: exp-power-theory\n    registry_id: exp-power-theory\n    claim: 2\n    description: \"推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A 模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\"\n    priority: P1\n    gpu_budget_hours: 0\n    deps: [exp-extended-sim]\n    status: planned\n    notes: \"纯理论推导 + 数值验证。CPU only.\"\n\n  # === P1: Important (robustness + differentiation) ===\n\n  - id: exp-leaderboard-data-recon\n    registry_id: exp-leaderboard-data-recon\n    claim: 3\n    description: \"Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results 是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。\"\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    status: planned\n    notes: \"纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。\"\n\n  - id: exp-leaderboard-audit\n    claim: 3\n    description: \"Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark 污染率随时间趋势。\"\n    priority: ABANDONED\n    gpu_budget_hours: 20\n    deps: [exp-two-sided, exp-leaderboard-data-recon]\n    status: abandoned\n    notes: \"D011: v1-irt-refit a_r=0.111 + item alignment 54.56% → 13K audit 不可行。数据可用性写入 Discussion/Future Work。\"\n\n  - id: exp-natural-experiment\n    claim: 3\n    description: \"v1 leaderboard base→chat model pairs 自然实验：计算 Δlz* = lz*(chat) - lz*(base) 作为 SFT 效应代理。\"\n    priority: P2-optional\n    gpu_budget_hours: 0\n    deps: [exp-v1-irt-refit-pilot]\n    status: deprioritized\n    notes: \"D013: a_r=0.111 导致 lz*≈accuracy-like, 仅 4-5 pairs 无统计检验能力。Reviewer 终审建议降级。\"\n\n  - id: exp-v1-irt-refit-expanded\n    claim: 3\n    description: \"扩大 v1 IRT 重拟合样本量至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。最终关闭 Path D。\"\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [exp-v1-irt-refit-pilot]\n    status: assigned\n    notes: \"CPU only. Reviewer 要求 N≥500 才能最终结论 Path D。阈值：a_r>0.4=可行, a_r<0.2=dead。\"\n\n  - id: exp-4pl-ablation\n    claim: 1\n    description: \"4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter d 对 false alarm 和 detection power 的影响。\"\n    priority: P2\n    gpu_budget_hours: 0\n    deps: [exp-extended-sim]\n    status: planned\n    notes: \"CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\"\n\n  - id: exp-baseline-comparison\n    claim: 1\n    description: \"与现有方法对比（≥5 baselines）：在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs baselines 的 AUROC/Type-I error。Baselines: (1) ConStat (re-test), (2) Min-K%++ (token probs), (3) accuracy z-score (已完成, CPU), (4) PPL-based detection (log-prob family 代表, 预期 RL-robust 测试中失败), (5) random baseline。量化 minimal-information 的代价（power 损失）。报告 bootstrap CIs（同行 6/8 不报告方差，这是我们的差异化优势）。\"\n    priority: P0-end\n    gpu_budget_hours: 30\n    deps: [exp-ctrl-contam]\n    status: planned\n    notes: \"蒸馏显示同行 baseline 中位数 ~5 个。accuracy z-score 已完成(CPU)。ConStat 需 re-test, Min-K%++ 需 token probs, PPL 需 log-probs。exp-ctrl-contam 完成后立即执行。\"\n\n  - id: exp-multiscale-lzm\n    claim: \"1,3\"\n    description: \"实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化 lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\"\n    priority: P2\n    gpu_budget_hours: 0\n    deps: [exp-two-sided]\n    status: planned\n    notes: \"CPU only. 需要实现 lzm 公式。\"\n\n  # === P2: Nice-to-have (expanded scope) ===\n\n  - id: exp-post-rl\n    claim: 1\n    description: \"Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应 Wang et al. (2025) 的 MIA 失效问题。\"\n    priority: P2\n    gpu_budget_hours: 40\n    deps: [exp-ctrl-contam]\n    status: planned\n    notes: \"GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\"\n\n  - id: exp-extra-benchmarks\n    claim: \"2,3\"\n    description: \"扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\"\n    priority: P2\n    gpu_budget_hours: 10\n    deps: [exp-extended-sim]\n    status: planned\n    notes: \"取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\"\n\n  - id: exp-domain-analysis\n    claim: 3\n    description: \"MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染是全面的还是集中在特定 domain。\"\n    priority: P2\n    gpu_budget_hours: 0\n    deps: [exp-two-sided]\n    status: planned\n    notes: \"CPU only. 需要 MMLU item-to-domain 映射。\"\n\n# === GPU Budget Summary (post-D011/D013) ===\n# P0: ~92 GPU-hrs (ctrl-contam-pilot 12 + ctrl-contam 80)\n# P0-end: ~30 GPU-hrs (baseline-comparison, 依赖 ctrl-contam)\n# P2: ~50 GPU-hrs (post-rl 40 + extra-benchmarks 10) — DDL 压力下不现实\n# ABANDONED: exp-leaderboard-audit (D011)\n# Total active: ~122 GPU-hrs\n# Available: 4× RTX 5090 32GB (bjb2-36806, SSH 不通)\n# 已用: 0 GPU-hrs\n",
      "numLines": 165,
      "startLine": 1,
      "totalLines": 165
    }
  },
  "sourceToolAssistantUUID": "94792eed-19c6-4250-8f7d-2c4d01304931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-21T12:43:08.746Z_

````json
{
  "parentUuid": "66932a34-e91e-4b7d-b941-7c4c4fe32461",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**irt_personfit_contam**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"irt_personfit_contam\")` 或 `load_project_config(\"irt_personfit_contam\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/irt_personfit_contam/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "384c9864-dbae-475a-9396-141d687e19d0",
  "timestamp": "2026-05-21T12:43:08.746Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Post-RL destroys all person-fit signals; HT matches lz* everywhere; reframe as framework + empirical characterization paper 核心假设：['exp-post-rl: GRPO elimi…",
  "leafUuid": "384c9864-dbae-475a-9396-141d687e19d0",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT contamination detection: worst-case scenario characterization",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca"
}
```

---

### Assistant

_source line 16 · 2026-05-21T12:46:33.822Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to identify all experiments with `status: planned` in the experiment_plan. Let me scan through the plan and the registry.

From the experiment_plan YAML, the experiments with `status: planned` are:
1. exp-two-sided (but DONE in registry)
2. exp-extended-sim (but DONE in registry)
3. exp-ctrl-contam-pilot (DONE in registry)
4. exp-ctrl-contam (planned - registry has individual sub-experiments done but the full exp is planned)
5. exp-empirical-null (DONE in registry)
6. exp-power-theory (DONE in registry)


7. exp-leaderboard-data-recon (DONE in registry)
8. exp-4pl-ablation (DONE in registry)
9. exp-baseline-comparison (DONE in registry)
10. exp-multiscale-lzm (planned)
11. exp-post-rl (ANALYZING/failed in registry)
12. exp-extra-benchmarks (planned)
13. exp-domain-analysis (DONE in registry)

I'm noticing a mismatch between what the experiment_plan marks as planned and what the registry shows—most are actually completed. The CLAUDE.md file appears to have a more current registry status.

Looking at the actual registry, I can see which experiments are truly still in the planned state versus what's already been executed or is currently analyzing. I'm cross-referencing the experiment_plan.yaml file against the registry in CLAUDE.md and noticing a significant discrepancy—many experiments marked as "planned" in the file are actually already completed in the registry. Let me map out which ones are truly still planned versus which have been done or are in other states. Looking at the discrepancies between the CLAUDE.md experiment_plan and the registry, I see several experiments marked as "planned" that actually have completion statuses recorded elsewhere. The user is asking me to generate worst-tier predictions for all experiments in the plan, treating them uniformly regardless of their current status. Continuing through the rest of the planned experiments from both sources, I'm seeing exp-baseline-comparison, exp-multiscale-lzm, exp-post-rl, exp-extra-benchmarks, and exp-domain-analysis listed in CLAUDE.md, plus several more from the YAML file like exp-two-sided, exp-extended-sim, exp-empirical-null, exp-power-theory, and exp-leaderboard-data-recon. There's some inconsistency between what's marked as planned in the YAML versus what's marked DONE in CLAUDE.md, so I need to clarify which source to prioritize for the user's request. I need to look more carefully at the actual structure of the experiment_plan in CLAUDE.md since it doesn't seem to have explicit status fields like I initially thought—it's organized differently with id, claim, and description fields instead. Looking at the rest of the experiment registry, I can see there are quite a few more planned experiments beyond the initial batch—things like the IRT refit expansion, 4PL ablation studies, baseline comparisons, and several others focused on multiscale analysis, post-RL evaluation, and domain-specific work.

The issue is that the experiment_plan.yaml file seems out of sync with the actual registry. Many of these experiments are marked as "planned" in the CLAUDE.md documentation, but the registry itself shows them as already completed. This suggests the plan file hasn't been refreshed to reflect what's actually been done.

Let me check the registry against what's listed as planned to identify which experiments are genuinely still in progress versus which ones have already finished. I need to reconsider what the user is actually asking for. They want me to take every experiment marked as `status: planned` directly from the experiment_plan section and generate worst-case imagined results for each one. Let me identify all the planned experiments from that list: the ctrl-contam pilot, the full ctrl-contam, leaderboard-audit, natural-experiment, v1-irt-refit-expanded, 4pl-ablation, and baseline experiments are the ones I'm tracking.

The tricky part is that some of these experiments already show as DONE in the registry, which creates a conflict. But since this is a scenario planning exercise asking for imagined worst-tier outcomes, I think the user wants predictions for all the planned experiments as listed, regardless of completion status. Though it does seem odd to generate imagined results for experiments that already have actual results.

Looking back at the request more carefully—"expand detailed data for every planned experiment in the experiment_plan"—it's specifically asking for the planned ones from that document. I should stick to those and ignore the PREPARING experiments that were added to the registry later.

Now I'll generate worst-tier predictions for each planned experiment using the framework definitions: post-RL destroying person-fit signals, HT matching lz* everywhere, and the core metric range assumptions. I'll create the YAML output with detailed rationales for each one.

Looking at the experiment list, I need to distinguish between what's truly planned versus what's already completed in the registry. The user is asking for predictions on the planned experiments specifically, so I should focus on those that don't have final results yet and skip or note the ones that are already done. Looking at the registry status more carefully, most experiments are already completed with actual results. The truly pending ones that don't have registry entries are exp-multiscale-lzm and exp-extra-benchmarks, plus the full sweep for exp-ctrl-contam. There are also some PREPARING experiments in the registry that aren't in the plan—exp-constat-comparison, exp-mia-mink-comparison, and exp-arcc-benchmark. I think the user probably just wants me to generate worst-case predictions for whichever experiments are actually still pending.

Generating worst-tier predictions for all planned experiments... I'm completing the list of all 11 planned experiments and now working through worst-tier predictions for each one. For the abandoned leaderboard audit, I'll still generate predictions but flag it as discontinued. Starting with the contamination pilot: SFT contamination should be detectable even in worst-case scenarios since the framework assumes MIA/Min-K++ hit AUROC 0.65+ on SFT, though the signal might be weaker than ideal, and Qwen's already-high baseline lz* values could complicate detection there. moderate Cohen's d but the inverted-U/non-monotonicity issue is present.

Actually, this is about CTRL contamination with SFT, not post-RL. The worst tier says post-RL destroys signals, but SFT should still be detectable. Looking at the actual results in the registry, the ctrl-contam-pilot got |d|=3.42 at 15%. Under worst tier, would this be different?

Hmm, the worst tier is about the OVERALL paper narrative. Even in the worst tier, SFT contamination detection works (that's the scope-honest framing). The worst-tier key metrics show:
- post_rl_lz_star_cohens_d: [0.0, 0.5] → post-RL fails
- But SFT detection (which is exp-ctrl-contam) should still work

So for SFT experiments, "worst" doesn't mean the detection fails—it means the conditions are less favorable. The main constraints are that HT and lz* become indistinguishable across the board, ARC-C lacks the statistical power for reliable detection, and the cross-family analysis is narrowed to SFT-only scope. Looking at the specific experiments, the pilot shows SFT detection working with d around 3.0-3.5 for lz*, though HT matches it closely and Qwen exhibits non-monotonicity. The full sweep confirms SFT detection holds across models, but ARC-C effects are too small, HT remains aligned with lz* everywhere, and the signal strength varies by benchmark—MMLU shows stronger effects than GSM8K or HellaSwag, while the memorization fraction stays consistent.

The post-RL experiment is where things truly break down: GRPO completely eliminates the binary-only signals, with Cohen's d below 0.5 for both lz* and HT. In the baseline comparison, lz* only outperforms a handful of methods like Guttman, U3, and random guessing, while HT matches lz* and ConStat achieves much higher retest AUROC. The 4PL ablation still shows advantages over 3PL, though that's somewhat orthogonal to the worst-tier framing. Finally, cross-benchmark aggregation in the multiscale experiment doesn't provide much benefit because the universal misfit means lzm is also universally flagged.

Additional benchmarks like BBH and MATH help fill some power gaps but don't shift the core narrative. Domain analysis reveals contamination is spread uniformly across MMLU subjects. The IRT refit experiment confirms Path D is essentially dead with a_r below 0.2. The natural experiment has limited statistical power with no significant individual outliers, and the leaderboard audit was abandoned since IRT refit failed.

Now I'm structuring the YAML output with specific metric values for each experiment, including name, plan ID, description, expected results with precise numbers, detailed rationale for why these results emerge under the worst-tier hypothesis, tables, figure descriptions, and analysis sections.

The paper should reframe itself as a framework plus empirical characterization study. IRT-FIT successfully detects SFT contamination with large effect sizes exceeding 2.5 in absolute value, but post-RL GRPO training eliminates detection across all binary-only methods, bringing effects below 0.5. HT matches or exceeds lz* performance in every tested condition with no empirical separation between the two statistics. ARC-C is too small for reliable detection. The main contributions are the first systematic application of IRT person-fit to LLM evaluation with universal 4PL misfit as a novel finding, a scope-honest detection framework that works for SFT contamination with an explicit RL boundary, and releasing the IRT-FIT toolkit plus 13K model data with the θ-shift methodology.

Writing YAML structure... I'm working through the worst-tier scenario where SFT detection still performs well, but post-RL degradation combined with HT matching the baseline means the paper loses its competitive edge. Now I'm generating specific metric predictions across the experiments that fit these constraints—Cohen's d values around 3.0-3.5 for the 15% contamination cases, dropping to 1.0-1.5 at 50% to capture the non-monotonicity, with memorization fractions around 0.35 and minimal clean-vs-clean differences.

For the full contamination experiment, I'm expecting similar patterns across models with Qwen showing the strongest detection (d~3.0-3.5) and ARC-C too underpowered to detect anything meaningful. The post-RL experiment is critical here—GRPO smooths out the binary signals entirely, pushing detection metrics to chance level, which undermines any claim of superiority. Meanwhile, the baseline comparison shows HT and lz* performing equivalently, with ConStat's retest reliability around 0.85 but offering no differentiation between methods.

Looking at the other experiments, Min-K++ substantially outperforms post-RL approaches with AUROC around 0.65-0.75, while lz* only beats a handful of random baselines. The 4PL ablation confirms the model gains 14-27 percentage points over 3PL, matching simulation predictions, but this doesn't strengthen the overall argument. The multiscale variant lzm shows no improvement—it flags identically to lz* across benchmarks regardless of aggregation strategy. Adding BBH with its 6511 items provides moderate additional signal.

The domain analysis reveals MMLU contamination spreads uniformly across most models with only slight elevation in STEM versus humanities, contradicting any concentration hypothesis. The IRT refit with expanded samples confirms the discrimination parameter remains below 0.2, indicating Path D is genuinely unviable even at N=500. The natural experiment yields only 4-5 usable pairs with insufficient power to isolate contamination effects, though HellaSwag and GSM8K show consistent SFT patterns. The leaderboard audit was ultimately abandoned because the IRT refit failure—specifically the a_r value of 0.111—undermines the statistical foundation needed.

Now I'm reconsidering which experiments to include: the user asked for each planned experiment in the experiment_plan, so I should stick to those rather than pulling in the PREPARING registry entries like exp-constat-comparison or exp-arcc-benchmark, even though they're active. The sub-experiments under exp-baseline-comparison are a gray area, but I'll prioritize the main plan entries and flag exp-leaderboard-audit as high priority despite its abandonment. I'm noticing some inconsistencies between the YAML file and the CLAUDE.md experiment plan—the statuses don't always match. For exp-natural-experiment, the YAML shows `deprioritized` but CLAUDE.md lists it as `planned`, and similarly for exp-v1-irt-refit-expanded where YAML has `assigned` but CLAUDE.md shows `planned`. I'll go with what's in CLAUDE.md since that's the authoritative source here, and I need to compile the full list of planned experiments to write out the YAML properly. I'm scanning through the experiment statuses in the plan file to get a clearer picture—several experiments are marked as done, while others are planned, and one is explicitly abandoned. So I actually have 11 planned experiments to focus on, not counting the completed ones or the abandoned audit experiment.

Now I need to think through the worst-case predictions for each experiment, starting with the contamination pilot. Even under worst-tier conditions, SFT contamination should still be detectable since that's core to the paper's scope. I'm expecting the clean baseline to show near-zero difference in the loss metric, while the contaminated condition at 15% should produce a substantial Cohen's d around 2.

0. At 50% contamination, the effect might drop to 0.8-1.2 due to non-monotonic behavior from parameter shifts, but the model should still memorize roughly a third to a bit over a third of the seen items. The lz* metric should catch this aberrant pattern at the model level, and the hypothesis test using difficulty ordering should pick up the same signal since the difficulty violation becomes the dominant feature. With θ fixed, monotonicity should be restored.

Now moving to the full contamination experiment across all four models, six contamination levels, and three benchmarks... I need to reconcile the experiment plan with the metrics—the main ctrl-contam setup only includes MMLU, GSM8K, and HellaSwag, but ARC-C metrics are showing up in the worst-tier results, which suggests they're coming from a separate ARC-C benchmark experiment in the registry. Looking at the validation counts, only 2 out of 4 model families are passing the worst-tier criteria, and Gemma-4-31B might be struggling due to its larger size.

Actually, thinking about this more carefully—Mistral is already validated in the registry with strong detection signals, so the bottleneck isn't whether families can detect SFT at all. The n_families_validated: [2, 2] constraint probably means we can only reliably claim cross-family results for 2 families with sufficient seed coverage, while the others have limited validation runs. This limits how broadly we can claim the detection method works across different model architectures.

The leaderboard audit experiment didn't run because the IRT refit failure (a_r=0.111) makes the 13K audit computationally infeasible. For the natural experiment, worst-case discrimination failure means only 4-5 viable model pairs remain, and while we see systematic SFT effects on certain benchmarks, we can't isolate contamination-specific signals or find individual outliers. The expanded IRT refit experiment confirms discrimination stays below 0.2 even at N=178 or N=500, effectively closing that path. Meanwhile, the 4PL ablation shows switching from 3PL to 4PL could gain 14-27 percentage points in statistical power under worst-case conditions.

The 4PL model is essential for LLM contamination detection because 2PL is catastrophically miscalibrated with false alarm rates hitting 50-100%, and the d parameter matters for nearly half of MMLU items. This result holds consistently across all tiers since it's fundamentally about model comparison rather than detection performance or post-RL effects. For baseline comparisons, lz* and HT both achieve effect sizes around 3.0-3.5 at 15% contamination, showing no meaningful differentiation between them, while simpler methods like Guttman and U3 only reach 0.3-0.5. ConStat's retest AUROC ranges from 0.85-0.95 and improves with additional information.

In the worst-case tier, methods with richer information access like ConStat and Min-K++ actually outperform lz* on SFT data, achieving 0.85-0.95 and 0.65-0.75 AUROC respectively, while lz* only beats the weakest baselines and HT matches it entirely—eliminating any claimed advantage from full 4PL parameterization for detection purposes.

For the multiscale aggregation experiment, combining lz* across benchmarks doesn't meaningfully reduce false flagging rates or improve discrimination beyond what individual benchmarks achieve. And in the post-RL setting, both lz* and HT show negligible effect sizes around 0.1-0.4, with MIA performance collapsing to near-random levels around 0.48-0.53 AUROC.

The core issue is that all binary-only and token-probability methods fail after RL training because the optimization process smooths out the aberrant response patterns that SFT memorization creates. GRPO trains the model to reason through problems rather than rely on memorized patterns, so the difficulty-ordering violations that detection methods rely on disappear—the model still gets items right, but through a process that looks like genuine competence rather than memorization.

When I look at performance on larger benchmarks like BBH and MATH, the detection power improves substantially, reaching 0.72-0.85 on BBH with 6511 items and 0.60-0.75 on MATH with 5000 items at the 15% contamination level.

For the domain analysis, MMLU shows uniform contamination patterns across most models, with Gemini-1.5 flagging all 57 subjects since its 100% accuracy makes detection trivial. STEM domains show slightly higher detection rates than humanities, which aligns with Gemini's stronger STEM performance, and there's no evidence of targeted domain-specific contamination—it's distributed globally across the benchmark.

Now I need to compile the full YAML output and make sure I'm including all the relevant experiments from the registry, including the sub-experiments like ConStat and MIA comparisons that feed into the broader baseline comparison.

Writing YAML output... Now I'm ready to structure the full output with the YAML format that includes the experiment name, plan ID, description, expected results, rationale, and all the supporting tables and figures I've outlined.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "384c9864-dbae-475a-9396-141d687e19d0",
  "isSidechain": false,
  "requestId": "req_011CbFjVdj4p1mj6SXCa79mU",
  "type": "assistant",
  "uuid": "cd4c1574-5d2d-4906-984e-dacb87dcfbb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RXqdECrmLKSPCGyaTBTmc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9387,
      "cache_read_input_tokens": 38796,
      "output_tokens": 20860,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9387,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20860,
          "cache_read_input_tokens": 38796,
          "cache_creation_input_tokens": 9387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9387
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

_source line 17 · 2026-05-21T12:49:43.316Z_

```yaml
tier: worst
narrative_guidance: >
  Reframe: NOT a detection superiority paper. Post-RL GRPO eliminates all binary-only detection signals (|d|<0.5).
  HT matches or exceeds lz* in every tested condition — no empirical basis for claiming lz* advantage over
  simpler difficulty-only statistics. Paper pivots to three-pronged contribution:
  (A) First systematic IRT person-fit study of LLM response patterns — universal 4PL misfit (57/60 flagged)
  is a novel cognitive finding, not a detection artifact.
  (B) Scope-honest SFT detection — IRT-FIT detects intentional SFT contamination (|d|>2.5 across two families)
  with explicit scope boundary: post-RL smooths binary signal below detection for ALL binary-only methods.
  The RL boundary is itself a contribution mapping the detection frontier's limits.
  (C) Framework + toolkit — open-source IRT-FIT toolkit, θ-shift methodology, memorization fraction
  quantification, and 13K+ model data availability. Contributions are methodological, not SOTA claims.
  ConStat (retest AUROC 0.85-0.95) and Min-K++ (SFT AUROC 0.65-0.75) outperform lz* when given more
  information access. lz* only beats Guttman/U3/random (2-3 baselines). The "minimal-information" framing
  must honestly acknowledge the cost: lower power than methods with richer signals.
  Target EMNLP as evaluation methodology paper with community tooling impact.

imagined_experiments:

  - name: "Controlled Contamination Pilot (Qwen × MMLU)"
    plan_id: "exp-ctrl-contam-pilot"
    description: >
      Qwen2.5-7B-Instruct × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU.
      Go/no-go signal for the paper. Measures Δlz*, clean noise floor, memorization fraction.
    expected_results:
      n_clean_seeds: 2
      clean_seed1_lz_star: 8.9
      clean_seed2_lz_star: 8.4
      clean_vs_clean_delta_lz: 0.5
      clean_mean_lz_star: 8.65
      clean_std_lz_star: 0.35
      contam_15_lz_star: 4.1
      contam_50_lz_star: 7.5
      delta_lz_contam15: -4.55
      delta_lz_contam50: -1.15
      cohens_d_contam15: -3.1
      cohens_d_contam50: -0.9
      theta_shift_15: 0.28
      theta_shift_50: 0.45
      memorization_fraction_15: 0.36
      memorization_fraction_50: 0.30
      theta_fixed_contam15_lz: 11.5
      theta_fixed_contam50_lz: 17.8
      theta_fixed_ratio: 3.0
      ht_d_contam15: -3.0
      ht_d_contam50: -0.85
      acc_contam15: 0.710
      acc_contam50: 0.725
      acc_seen_contam15: 0.78
      acc_unseen_contam15: 0.68
    result_rationale: >
      SFT with QLoRA directly injects benchmark items into training. Model memorizes ~36% of seen items
      (consistent with QLoRA's partial parameter update — full FT would memorize more). At 15%, 2106
      items are seen; ~758 are memorized, creating a diffuse aberrance signal detectable at model level.
      Cohen's d ~3.1 because lz* aggregates 14042 item-level weak signals. Non-monotonicity at 50%
      (|d|=0.9 < 3.1) because θ-shift absorbs aberrance: contaminating 50% raises θ_MLE by ~0.45,
      making previously-aberrant correct answers look expected. θ-fixed analysis restores monotonicity
      (ratio ~3.0). HT matches lz* (d ~3.0 vs 3.1) because the dominant signal is difficulty-ordering
      violation — items the model "should" get wrong are answered correctly — and HT captures this with
      only item difficulty. The full 4PL parameterization (a, c, d) adds negligible incremental signal
      at model level when the difficulty violation is already large. Clean-vs-clean Δlz* ~0.5 confirms
      noise floor is small relative to contam signal.
    tables:
      - "Table: Pilot results — lz* and HT Cohen's d across conditions, with θ-free and θ-fixed"
    figures_description:
      - "Bar chart: Δlz* for clean-vs-clean (noise floor) vs clean-vs-contam15 vs clean-vs-contam50, error bars from 2-seed clean variance"
      - "Scatter: seen vs unseen item accuracy at 15% and 50% contamination, showing memorization fingerprint"
    analysis: >
      Go signal confirmed for SFT scope. But HT matching lz* is a warning: the simpler
      statistic captures the same information at model level. Non-monotonicity under free-θ
      motivates θ-fixed methodology. Paper can claim SFT detection with |d|>2.5 but must
      acknowledge HT parity.

  - name: "Full Controlled Contamination (4 Models × 6 Levels × 3 Benchmarks)"
    plan_id: "exp-ctrl-contam"
    description: >
      Qwen2.5-7B-Instruct, Gemma-4-31B, Llama-3.1-8B-Instruct, Mistral-7B-v0.3
      × 0%/5%/10%/15%/25%/50% × MMLU/GSM8K/HellaSwag.
    expected_results:
      n_families_validated: 2
      qwen_mmlu_d15: -3.1
      qwen_mmlu_d50: -0.9
      llama_mmlu_d15: -2.7
      llama_mmlu_d50: -3.0
      mistral_mmlu_d15: -2.4
      mistral_mmlu_d50: -2.8
      gemma_mmlu_d15: -1.8
      gemma_mmlu_d50: -2.2
      qwen_gsm8k_d15: -1.4
      llama_gsm8k_d15: -1.2
      qwen_hellaswag_d15: -1.8
      llama_hellaswag_d15: -1.5
      qwen_ht_mmlu_d15: -3.0
      llama_ht_mmlu_d15: -2.6
      cross_family_mf_range: "0.30-0.40"
      cross_family_mf_std: 0.04
      theta_fixed_monotonic_all: true
      dose_response_5pct_detectable: false
      dose_response_10pct_detectable: "marginal (d ~0.8-1.2 on MMLU only)"
      min_contam_for_detection_mmlu: "10-15%"
      min_contam_for_detection_gsm8k: "25%"
      min_contam_for_detection_hellaswag: "15-25%"
    result_rationale: >
      Only 2 families (Qwen + Llama) are fully validated with 3+ clean seeds each — Mistral and
      Gemma have single clean seeds, insufficient for rigorous Cohen's d with CI. Gemma-4-31B
      shows weaker detection (d ~1.8) because larger models have more latent capacity to absorb
      contamination without creating aberrant patterns — the 31B model generalizes from seen items
      more smoothly than 7-9B models, reducing the memorization fraction to ~0.25. GSM8K (1319 items)
      and HellaSwag (10042 items) show weaker detection than MMLU (14042 items), consistent with
      power function — fewer items = less aggregation power. GSM8K is particularly weak because
      its chain-of-thought format means SFT contamination partially teaches reasoning, not just
      memorization. HT matches lz* across all conditions (|d_HT - d_lz*| < 0.3) because
      difficulty-ordering violation dominates in all model-benchmark combinations. At 5%
      contamination, signal is indistinguishable from noise (only ~700 items seen on MMLU,
      ~250 memorized — insufficient for model-level detection). Cross-family MF consistency
      (0.30-0.40, std ~0.04) supports the generalizability of the memorization fraction concept.
      θ-fixed universally restores monotonicity, confirming this as a model-independent phenomenon.
    tables:
      - "Table: Cohen's d matrix — rows=models, cols=benchmarks×levels, bold best per column"
      - "Table: HT vs lz* Cohen's d comparison — no significant difference in any cell"
      - "Table: Memorization fraction across models and levels — 30-40% range"
    figures_description:
      - "Dose-response curves: Δlz* vs contamination level, one line per model, faceted by benchmark. Free-θ (left) vs θ-fixed (right)"
      - "Heatmap: Cohen's d by model×benchmark at 15% contamination, showing power degrades with fewer items"
      - "Cross-family memorization fraction bar chart with 95% CI, showing consistency"
    analysis: >
      SFT detection validated across 2 families with multiple seeds, but cross-family scope is
      limited. Gemma's weaker signal warns that larger models may approach the detection boundary
      even for SFT. GSM8K near the detectability threshold at 15%. HT parity across all 4×6×3
      conditions eliminates empirical lz* advantage — the paper must rely on data-independent
      differentiation (parametric null, Snijders correction, 4PL item weighting).

  - name: "Leaderboard Audit (ABANDONED)"
    plan_id: "exp-leaderboard-audit"
    description: >
      Open LLM Leaderboard v1 大规模扫描。已放弃因 IRT refit 失败。
    expected_results:
      status: ABANDONED
      reason: "a_r=0.111 (discrimination) + item alignment 54.56% → 13K audit infeasible"
      v1_data_availability: "13K+ models with per-item binary data"
      future_work_note: "Data availability mentioned in Discussion; audit deferred to future work pending neural IRT estimation advances"
    result_rationale: >
      Classical IRT estimation (MML-EM) with N=63-178 models produces a_r=0.111 (well below
      0.2 threshold), making the refitted parameters effectively discrimination-free. lz* computed
      with these parameters collapses to an accuracy-like metric, losing the IRT advantage.
      The root cause is that classical IRT assumes large samples of independent examinees, but
      LLM response patterns violate this (models are not independent draws from a population;
      they share training data and architectures). Item alignment at 54.56% further degrades
      parameter quality. This failure is a genuine methodological finding about the gap between
      classical and neural IRT estimation requirements.
    tables: []
    figures_description: []
    analysis: >
      ABANDONED. Not a paper weakness — frame as honest methodological caveat in Section 6
      (IRT parameter estimation challenges). The 13K+ data availability is a future-work
      contribution. Paper uses PSN-IRT validated parameters (external calibration) instead.

  - name: "Natural Experiment (Base→Chat Pairs)"
    plan_id: "exp-natural-experiment"
    description: >
      v1 leaderboard base→chat model pairs: Δlz* = lz*(chat) - lz*(base) as SFT effect proxy.
    expected_results:
      n_viable_pairs: 5
      hellaswag_mean_deviation: -3.2
      hellaswag_p_value: 0.003
      gsm8k_mean_deviation: 3.5
      gsm8k_p_value: 0.015
      mmlu_p_value: 0.18
      arcc_p_value: 0.42
      individual_outliers_detected: 0
      statistical_power_for_individual_detection: "insufficient"
    result_rationale: >
      With a_r=0.111, lz* is essentially accuracy-weighted, not IRT-weighted. The HellaSwag
      and GSM8K systematic effects reflect aggregate SFT training dynamics (SFT systematically
      changes performance patterns on these benchmarks), not contamination-specific signals.
      Only 5 viable pairs provide no statistical power for detecting individual contamination
      outliers — even a genuinely contaminated model would not stand out from the systematic
      SFT effect. MMLU and ARC-C show no significant systematic effect (p>0.1), possibly
      because SFT effects on these benchmarks are more heterogeneous across model families.
      The P2-optional priority is justified: results are mildly interesting (systematic SFT
      effects exist) but contribute nothing to the contamination detection narrative.
    tables:
      - "Table: Paired t-test results by benchmark — HellaSwag and GSM8K significant, MMLU/ARC-C not"
    figures_description:
      - "Paired difference plot: Δlz*(chat-base) per benchmark with CI, showing systematic direction for HellaSwag/GSM8K"
    analysis: >
      Deprioritized. Systematic SFT effects are a minor observation for Discussion section.
      No contamination detection capability. Frame as: "natural experiments show SFT consistently
      changes lz* patterns, motivating the controlled contamination approach."

  - name: "v1 IRT Refit Expanded (Path D Closure)"
    plan_id: "exp-v1-irt-refit-expanded"
    description: >
      扩大 v1 IRT 重拟合至 N≥500, 验证 a_r=0.111 是否因样本量不足。
    expected_results:
      n_models_downloaded: 500
      3pl_a_pearson_r: 0.13
      2pl_a_pearson_r: -0.02
      3pl_b_pearson_r: 0.66
      a_r_threshold: 0.2
      a_r_verdict: "dead (a_r < 0.2)"
      path_d_status: "closed"
    result_rationale: >
      Expanding from N=63→178 only improved a_r from 0.111 to 0.127. Extrapolating to N=500,
      the marginal gain is diminishing (~0.13-0.14). The fundamental issue is not sample size
      but model heterogeneity: LLMs from different families/scales violate the classical IRT
      assumption that all examinees are drawn from a single latent trait distribution. A
      7B model and a 70B model are not "two examinees differing in ability" — they differ
      structurally in how they process items. Classical MML-EM cannot recover meaningful
      discrimination parameters from this heterogeneous sample. b_r stabilizes at ~0.66
      because difficulty is a more robust property (hard items are hard for all models),
      while discrimination is model-architecture-dependent. This definitively closes Path D.
    tables:
      - "Table: IRT refit metrics at N=63, N=178, N=500 — showing a_r plateau below 0.2"
    figures_description:
      - "Line plot: a_r and b_r as function of sample size N, showing b_r convergence and a_r plateau"
    analysis: >
      Path D confirmed dead. Paper Section 6 (Empirical Findings) reports this as a methodological
      caveat: classical IRT estimation from heterogeneous LLM samples fails on discrimination.
      Frames the gap between classical (small N, homogeneous) and neural IRT (large N,
      heterogeneous) estimation as an open problem for the community.

  - name: "4PL vs 3PL Ablation"
    plan_id: "exp-4pl-ablation"
    description: >
      4PL vs 3PL(d=1) 检测灵敏度比较。量化 d 参数对 FAR 和 power 的影响。
    expected_results:
      far_4pl: 0.05
      far_3pl: "0.05-0.16"
      far_2pl: "0.50-1.00"
      mean_power_gain_4pl_vs_3pl_mmlu: 0.25
      mean_power_gain_4pl_vs_3pl_hellaswag: 0.24
      mean_power_gain_4pl_vs_3pl_gsm8k: 0.19
      pct_mmlu_items_d_lt_0.95: 0.46
      max_power_gain_at_low_d: 0.55
      real_data_correlation_4pl_3pl: 0.23
      deepseek_delta_lz: 340
    result_rationale: >
      4PL d parameter models the probability ceiling — P(correct) for very high ability examinees.
      46% of MMLU items have d<0.95, meaning even the best models have <95% ceiling probability.
      When d=1 is forced (3PL), these items' response probabilities approach 1 for high-ability
      models, making any incorrect answer look extremely aberrant and inflating lz*. This creates
      both inflated FAR (false aberrance from normal ceiling effects) and reduced detection power
      (genuine contamination signal is masked by the d-induced noise). The +25pp mean power gain
      on MMLU reflects 4PL's ability to correctly model ceiling effects so that only genuine
      difficulty-ordering violations are flagged. 2PL is catastrophic because removing both
      c (guessing) and d (ceiling) makes the model unable to account for 40-60% of MMLU response
      variability. This result is tier-independent — it reflects a structural property of
      IRT parameterization, not a property of the detection frontier.
    tables:
      - "Table: FAR and power by parameterization (2PL/3PL/4PL) × benchmark"
      - "Table: Power gain stratified by d-parameter bucket"
    figures_description:
      - "ROC curves: 4PL vs 3PL vs 2PL on MMLU at 15% contamination"
      - "Scatter: item-level d parameter vs power gain (4PL over 3PL), showing low-d items drive the advantage"
    analysis: >
      Strong methodological contribution independent of worst-tier narrative. 4PL is essential
      for LLM contamination detection — this justifies the PSN-IRT parameter dependency. However,
      since HT (difficulty-only) matches lz* empirically, the 4PL advantage is theoretical (better
      calibrated null, correct ceiling modeling) rather than empirical detection superiority.
      Tension: 4PL matters for calibration, but HT doesn't need 4PL and still matches.

  - name: "Baseline Comparison (≥5 Baselines)"
    plan_id: "exp-baseline-comparison"
    description: >
      IRT-FIT vs 5+ baselines on ground-truth contaminated models: ConStat (re-test),
      Min-K%++ (token probs), accuracy z-score, PPL-based, HT, Guttman/U3, random.
    expected_results:
      n_baselines: 7
      n_baselines_beaten: 3
      model_level_lz_star_d_15: -3.1
      model_level_ht_d_15: -3.0
      model_level_guttman_d_15: -0.4
      model_level_u3_d_15: -0.45
      model_level_acc_zscore: 155
      constat_retest_auroc: 0.88
      mink_sft_auroc: 0.68
      ppl_sft_auroc: 0.63
      random_auroc: 0.50
      item_level_all_auroc_range: "0.50-0.63"
      item_level_best_oracle_rf: 0.63
      lz_star_vs_ht_diff: "not significant (p>0.3)"
      bootstrap_ci_width_lz_d: 1.2
    result_rationale: >
      Under worst tier, lz* only beats 3 baselines: Guttman (d~0.4), U3 (d~0.45), and random
      (d=0). HT matches lz* (d~3.0 vs 3.1, difference not significant with n=3 clean seeds).
      ConStat with rephrased re-testing achieves AUROC 0.88 because re-testing provides a
      fundamentally richer signal — it creates a second independent measurement of the same items,
      enabling paired comparison. This is strictly more informative than binary-only. Min-K++
      achieves SFT AUROC 0.68 because token-level probability distributions contain granular
      memorization signatures (specific logit patterns on memorized items) that binary responses
      discard. PPL-based detection gets 0.63 on SFT (above random but weak). All item-level
      methods are near-random (0.50-0.63) including oracle RF, confirming that contamination
      signal is diffuse — memorization fraction ~35% means 65% of seen items show no memorization
      signal. acc z-score achieves z~155 (trivially detects) but is non-specific: it can't
      distinguish contamination from genuine ability. The key worst-tier finding: methods with
      more information access (ConStat > Min-K++ > PPL > lz*) consistently outperform. lz*'s
      value is only at the minimal-information operating point, not detection performance.
    tables:
      - "Table: Model-level detection comparison — rows=methods (8), cols=models×conditions, Cohen's d or AUROC"
      - "Table: Item-level AUROC — all methods 0.50-0.63, confirming model-level aggregation is key"
      - "Table: Information access hierarchy — method, info required, SFT detection, post-RL detection"
    figures_description:
      - "Detection frontier plot: x=information access level (binary→retest→token probs→logits→weights), y=detection power. lz* at the bottom-left."
      - "Paired bar chart: lz* vs HT Cohen's d per condition, showing no significant difference"
      - "ROC curves: ConStat vs Min-K++ vs lz* on SFT contamination"
    analysis: >
      Paper cannot claim detection superiority. Must reframe as: "We establish the minimal-information
      operating point. Methods with more information access outperform — this is expected and honest.
      Our contribution is the framework (connecting psychometrics to LLM evaluation) and the
      characterization (θ-shift, memorization fraction, RL boundary). lz* beats only classical
      person-fit (Guttman/U3) and random — the 8× gap over Guttman shows IRT parameterization
      matters, but HT achieves the same with only difficulty." Bootstrap CIs (6/8 peer papers
      report none) remain a differentiator.

  - name: "Multiscale lzm Statistic"
    plan_id: "exp-multiscale-lzm"
    description: >
      跨 benchmark 聚合的标准化 lz* 总分 (Hong, Lin & Cheng, 2021)。
      PSN-IRT 12 模型 + 控制实验模型验证。
    expected_results:
      psn_12_models_lzm_flagged: "11/12"
      psn_lzm_vs_individual_lz_agreement: 0.92
      ctrl_contam_lzm_d_15: -2.8
      ctrl_contam_lzm_d_50: -0.8
      lzm_adds_discrimination_beyond_individual: false
      lzm_reduces_false_positive: false
      cross_benchmark_correlation: 0.15
    result_rationale: >
      lzm aggregates standardized lz* scores across benchmarks. Since individual benchmark lz*
      values are already extreme for nearly all models (57/60 flagged), aggregation cannot reduce
      flagging — it merely averages universally-extreme signals. The cross-benchmark correlation
      of lz* is low (~0.15, only GSM8K-HumanEval significant at r=0.62), meaning lzm doesn't
      capture a coherent "cross-benchmark contamination" signal — it just averages independent
      benchmark-specific misfit. For ctrl-contam models, lzm Cohen's d (~2.8) is slightly lower
      than the best individual benchmark (MMLU d~3.1) because GSM8K and HellaSwag dilute the
      signal. lzm does not add value beyond individual benchmark analysis in this context.
      The theoretical appeal (Hong et al. 2021 designed lzm for multi-test batteries where
      aggregation recovers signal from individually-weak tests) doesn't apply because each
      benchmark already has strong model-level signal.
    tables:
      - "Table: lzm vs individual benchmark lz* — flagging agreement rate"
    figures_description:
      - "Parallel coordinates: lz* across 5 benchmarks for 12 models, colored by lzm flag"
    analysis: >
      lzm is a methodological contribution (implementing Hong et al. 2021 for LLM context)
      but does not improve detection in practice. Brief mention in Method section; not a
      headline result. Could become useful if applied to many small benchmarks where individual
      power is insufficient.

  - name: "Post-RL Hypothesis Test (GRPO)"
    plan_id: "exp-post-rl"
    description: >
      Qwen3.5-9B: SFT contamination (15%) → GRPO training → measure if person-fit
      detection survives. Responds to Wang et al. (2025) MIA failure.
    expected_results:
      sft_only_lz_star_d: -3.1
      post_grpo_lz_star_d: -0.25
      post_grpo_ht_d: -0.20
      post_grpo_mia_auroc: 0.51
      post_grpo_mink_auroc: 0.52
      post_grpo_ppl_auroc: 0.49
      post_grpo_acc_delta: 0.03
      post_grpo_lz_star_value: 8.1
      post_grpo_clean_lz_star: 8.65
      post_grpo_delta_lz: -0.55
      memorization_fraction_post_rl: 0.05
      seen_unseen_acc_gap_post_rl: 0.01
      difficulty_ordering_restored: true
    result_rationale: >
      GRPO (Group Relative Policy Optimization) trains the model to maximize reward on a general
      objective. During RL, the model's policy is updated to produce correct answers through
      reasoning rather than memorization. The SFT-induced memorization signature — where specific
      items are answered correctly regardless of difficulty ordering — is overwritten because:
      (1) RL reward is based on correctness, not memorization; the model learns to derive answers
      rather than recall them; (2) GRPO uses group-relative rewards, normalizing performance
      within batches, which smooths out item-specific memorization spikes; (3) RL training
      updates ALL model parameters (not just LoRA adapters), distributing the contamination
      knowledge across the full parameter space and destroying the localized aberrance pattern.
      Post-RL, the model still achieves ~3% accuracy gain on seen items (residual knowledge)
      but the difficulty-ordering is restored — it gets hard-seen items wrong at expected rates.
      This makes lz* return to near-baseline (~8.1 vs clean 8.65). The seen/unseen accuracy gap
      collapses from ~0.10 (SFT) to ~0.01 (post-RL). HT also fails (d~0.20) because difficulty
      ordering is restored. MIA/Min-K++ fail (AUROC~0.51) consistent with Wang et al. (2025).
      ALL binary-only AND token-probability methods are at random. This is the structural
      limitation: RL transforms memorization into generalization-like behavior that is
      indistinguishable from genuine learning at all currently-accessible observation levels.
    tables:
      - "Table: Pre-RL vs Post-RL detection — all methods, showing collapse from d>2.5 to d<0.5"
      - "Table: Seen/unseen accuracy gap pre-RL vs post-RL"
    figures_description:
      - "Before/after bar chart: Cohen's d for lz*, HT, and effect sizes for MIA/Min-K++ pre-RL and post-RL"
      - "Item difficulty curve: P(correct) vs item difficulty for clean, SFT-only, and post-RL models. SFT shows aberrant bump on seen items; post-RL smooth curve indistinguishable from clean"
      - "Memorization fraction decay: MF from SFT (~0.36) → post-RL (~0.05), visualizing signal destruction"
    analysis: >
      This is the worst-tier defining result. ALL binary-only methods (lz*, HT, Guttman, U3,
      accuracy) and ALL token-probability methods (MIA, Min-K++, PPL) fail post-RL. The paper
      must honestly report this as a scope boundary: IRT-FIT detects SFT contamination but
      NOT post-RL contamination. Frame as contribution: "We map the detection frontier —
      establishing where binary detection works (SFT) and precisely where it fails (post-RL)."
      The RL boundary finding is itself publishable: it extends Wang et al. (2025) from
      10 log-prob methods to include person-fit and all binary-only methods.

  - name: "Extra Benchmarks (BBH + MATH)"
    plan_id: "exp-extra-benchmarks"
    description: >
      BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。
    expected_results:
      bbh_available_in_psnirt: false
      math_available_in_psnirt: false
      bbh_4pl_self_calibrated: true
      math_4pl_self_calibrated: true
      bbh_power_15pct_sim: 0.78
      math_power_15pct_sim: 0.68
      bbh_ctrl_contam_d_15: -1.8
      math_ctrl_contam_d_15: -1.4
      bbh_ht_d_15: -1.7
      math_ht_d_15: -1.3
      power_function_fit_with_bbh_math: 0.62
      self_calibrated_vs_psnirt_degradation: "15-25% power loss"
    result_rationale: >
      BBH and MATH are unlikely to be in PSN-IRT (which covers standard benchmarks: MMLU,
      HellaSwag, GSM8K, ARC-C, HumanEval). Self-calibrating 4PL parameters from the limited
      LLM sample (N=12-20 models) introduces the same discrimination failure as Path D
      (a_r < 0.2), resulting in 15-25% power loss vs PSN-IRT calibrated parameters. BBH
      (6511 items) achieves simulated power ~0.78 at 15% but real-data d ~1.8 (lower than
      MMLU's ~3.1) due to self-calibration degradation and BBH's complex format (multi-step
      reasoning items where SFT contamination signal is weaker — the model may memorize the
      answer but not the reasoning path, and BBH scoring often requires the full reasoning).
      MATH (5000 items) is worse: math problems have high guessing variance and the
      SFT signal is diluted by the symbolic nature of responses. Both benchmarks confirm
      the power function trend (more items = more power) but with lower coefficients than
      MMLU-calibrated parameters would predict. R² drops from 0.957 to ~0.62 when
      self-calibrated benchmarks are included, showing the power function is parameter-dependent.
    tables:
      - "Table: Power comparison — MMLU/HellaSwag/GSM8K (PSN-IRT) vs BBH/MATH (self-calibrated)"
    figures_description:
      - "Updated power function plot: n_items vs detection power, with BBH/MATH points below the PSN-IRT curve"
    analysis: >
      BBH and MATH fill the 1K-10K gap but with degraded performance due to self-calibration.
      This reinforces the PSN-IRT parameter dependency — IRT-FIT's power depends on parameter
      quality, not just benchmark size. Paper should report these as secondary results with
      the self-calibration caveat. Does not change worst-tier narrative.

  - name: "MMLU Domain-Level Analysis"
    plan_id: "exp-domain-analysis"
    description: >
      MMLU domain 级别分析：按 subject category 分别计算 person-fit，
      识别 contamination 是全面还是集中在特定 domain。
    expected_results:
      gemini_subjects_flagged: "50/57"
      gemini_all_domains_uniform: true
      gemini_stem_lz: 21.0
      gemini_humanities_lz: 18.0
      gemini_social_sciences_lz: 16.0
      gemini_other_lz: 15.5
      doubao_domain_asymmetric: true
      doubao_stem_lz: -2.0
      doubao_humanities_lz: -13.0
      yi_lightning_highest_lz: 48.0
      domain_concentration_index: 0.85
      contamination_uniform_pct: "80% of models"
    result_rationale: >
      Gemini-1.5 with 100% MMLU accuracy trivially flags all domains — with perfect accuracy,
      every subject produces extreme positive lz* (over-consistent). STEM slightly higher
      than humanities because STEM items have lower average d parameter (ceiling effects more
      pronounced), amplifying the over-consistency signal. Most models (~80%) show uniform
      contamination across domains because: (1) if contamination is via training data inclusion,
      it's unlikely to be domain-selective (entire benchmark is either included or not); (2) SFT
      on randomly-sampled benchmark items distributes contamination proportionally across domains.
      Doubao shows domain asymmetry (STEM normal, humanities aberrant) suggesting selective
      knowledge — possibly stronger humanities training data or benchmark-specific tuning. This
      is interesting but doesn't affect the detection narrative. Yi-Lightning's extreme lz*=48
      is driven by very high accuracy on hard items across all domains.
    tables:
      - "Table: lz* by domain category for top-5 most anomalous models"
      - "Table: Domain concentration index — fraction of models with uniform vs concentrated misfit"
    figures_description:
      - "Heatmap: models (rows) × MMLU categories (cols), color=lz*, showing uniform vs asymmetric patterns"
      - "Radar chart: Gemini vs Doubao domain profiles, illustrating uniform vs selective misfit"
    analysis: >
      Domain analysis provides interpretability (which subjects drive anomalies) but doesn't
      improve detection power. 80% uniform contamination is unsurprising. Doubao's asymmetry
      is a case study for Discussion. Paper Section 5c (empirical findings).
      Under worst tier, this is a descriptive contribution, not a detection advance.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd4c1574-5d2d-4906-984e-dacb87dcfbb0",
  "isSidechain": false,
  "requestId": "req_011CbFjVdj4p1mj6SXCa79mU",
  "type": "assistant",
  "uuid": "f064a7ef-419a-4a0c-b168-0a3fd6fd5f72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RXqdECrmLKSPCGyaTBTmc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9387,
      "cache_read_input_tokens": 38796,
      "output_tokens": 20860,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9387,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20860,
          "cache_read_input_tokens": 38796,
          "cache_creation_input_tokens": 9387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9387
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Post-RL destroys all person-fit signals; HT matches lz* everywhere; reframe as framework + empirical characterization paper 核心假设：['exp-post-rl: GRPO elimi…",
  "leafUuid": "f064a7ef-419a-4a0c-b168-0a3fd6fd5f72",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT contamination detection: worst-case scenario characterization",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Post-RL destroys all person-fit signals; HT matches lz* everywhere; reframe as framework + empirical characterization paper 核心假设：['exp-post-rl: GRPO elimi…",
  "leafUuid": "f064a7ef-419a-4a0c-b168-0a3fd6fd5f72",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT contamination detection: worst-case scenario characterization",
  "sessionId": "f10c5b11-f9c8-42ac-b7fa-f8ff7508d7ca"
}
```

---
