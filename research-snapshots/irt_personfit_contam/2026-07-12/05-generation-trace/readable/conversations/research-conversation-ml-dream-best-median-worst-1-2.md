# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/55d21821-fcc3-4f5e-bb80-174ec535ba8e.jsonl`
- **Structured JSON:** [`19c369f602407f463b8e.json`](../../sessions/19/19c369f602407f463b8e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:24:52.419Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:24:52.419Z",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: irt_personfit_contam\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.42 (n=3, ddof=1, ℓz*-corrected) with clear seen/unseen memorization fingerprint; Llama confirms cross-family detection with |Cohen's d|=2.95 at 15% and 3.31 at 50% (n=3, ddof=1, ℓz*-corrected), both large effects. θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.\n\n**Claim 2 (Detection Characterization)**:\nDetection power increases with benchmark size (n_items) and varies with contamination level, following an empirical power function (R²=0.65) that provides approximate practical guidance for practitioners assessing detectability on benchmarks of known size — but should NOT be described as \"predictive theory\" or \"scaling law.\" Two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported. **Baseline comparison (exp-baseline-comparison)**: At model level, lz* achieves 8× the effect size of classical person-fit statistics (Guttman/U3) on identical data (|d|=3.42 vs |d|=0.43 for Qwen 15%), demonstrating the value of full 4PL IRT parameterization. At item level, ALL binary-only methods achieve near-random discrimination (AUROC 0.52–0.63, including oracle supervised classifiers), revealing contamination produces a diffuse statistical signature detectable only through model-level aggregation over thousands of items. Accuracy z-score trivially detects in controlled settings (z=160 due to near-zero accuracy variance) but lacks specificity in real-world scenarios. The IRT framework enables principled aggregation by calibrating each item's expected response probability.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns from the target model (with externally calibrated IRT item parameters), IRT-FIT detects controlled contamination with |Cohen's d|>2.9 across two model families (Qwen, Llama), achieving 8× the effect size of classical person-fit statistics (Guttman/U3). The HT statistic (requiring only item difficulty) achieves comparable model-level detection power — the IRT person-fit family collectively dominates simpler indices, with ℓz*'s advantage lying in mechanistic interpretability (θ-shift analysis, memorization fraction quantification) and [pending: post-RL robustness vs HT]. Model-level aggregation over thousands of items yields robust detection where all item-level methods are near-random (AUROC 0.52–0.63). The IRT framework provides unique mechanistic insight: θ-shift analysis reveals how contamination raises ability estimates, and memorization fraction (35–38%) bridges theoretical power (97.9%) and observed detection capacity.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | **Completed (exp-baseline-comparison)**: Model-level: lz* |d|=3.42 vs Guttman/U3 |d|=0.43 (8× gap) — full IRT parameterization far exceeds difficulty-only person-fit. **HT is nearly as powerful as ℓz* (avg |d| comparable)** — the \"8×\" headline must include HT comparison to avoid selective framing. Item-level: all methods near-random (AUROC 0.52–0.63). acc z-score detects trivially (z=160) but lacks specificity. | exp-baseline-comparison |\n| R12 | \"HT ≈ ℓz* — why use ℓz*?\" | **[Dream D2 三档一致]** HT achieves comparable |d| with weaker requirements (difficulty only, no 4PL). **四场景应对 (D022, Reviewer validated)**：(Best) HT post-RL 丢失 + ℓz* 保留 → headline 差异化；(Good) HT 弱化 + ℓz* 更强 → quantitative comparison；(Neutral) 均保留 → 转用数据无关差异化（见下）；(Bad) 均丢失 → negative-as-contribution, scope SFT。**数据无关差异化（任何场景均可用）**：(i) ℓz* 有参数化 null (≈N(0,1), bootstrap 已验证) → 可直接假设检验, HT 无此性质；(ii) Snijders 校正补偿 θ 估计误差 (Var*=Var_l - C²/I(θ)), HT 无此校正；(iii) ℓz* 用 a/b/c/d 四参数加权 item 贡献, HT 仅用 b → MMLU 跨 57 科目 item 异质性大时 ℓz* 理论更精确。这些点不依赖 post-RL 结果，论文中应明确讨论。 | exp-baseline-comparison, exp-post-rl |\n| R13 | \"Minimal-information overstates\" | **[Dream D2 三档一致]** \"Minimal-information operating point\" obscures PSN-IRT 4PL parameter dependency. Reframe to \"minimal information **from the target model**\" or \"minimal runtime information\" — explicitly acknowledge PSN-IRT calibration as an external input requirement. | — |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as empirical characterization** — Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Simulation fit R²=0.957; real-data fit R²=0.65 (gap due to SFT generalization). Frame as \"empirical trend\" not \"theory/law.\"\n6. **Baseline comparison as evidence for model-level aggregation** — Item-level detection is near-random for ALL binary-only methods (including oracle RF). This is NOT a weakness — it reveals that contamination signal is diffuse (memorization fraction ~35%). Model-level lz* aggregates 14K weak signals into |d|>2.9. Frame item-level weakness as supporting evidence: \"any method that aggregates is better than any method that localizes.\" lz* vs Guttman/U3 8× gap proves IRT parameterization matters. acc z-score is sensitive but non-specific (sensitivity-specificity tradeoff).\n7. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n8. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n9. **Memorization fraction cross-family consistency** — MF is 35–38% at 15% contamination across Qwen (0.38) and Llama (0.35), only 3pp difference. Consistency strengthens generalizability. MF may vary with contamination mechanism (full FT vs QLoRA), model capacity, and benchmark difficulty — acknowledge in Limitations as deployment bootstrapping problem.\n10. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **Cross-family baseline lz* divergence (Reviewer WARNING)** — Clean lz* spans ~9σ: Qwen +8.68, Mistral +5.42, Llama -0.14. 固定阈值检测失效（Qwen contam_15 lz*=+3.85 仍为正值）。论文必须：(a) 明确 IRT-FIT 是相对检测（Δlz*/Cohen's d），非绝对阈值；(b) 展示 clean baseline lz* 跨家族差异表；(c) 预防性回答\"contam_15 lz*=+3.85 为正值为何算污染\"（因为 Δlz*=-4.83 是大效应）；(d) lz* baseline 作为\"模型内部一致性\"指标——Mistral acc 最低(0.514)但 lz* 第二高(+5.42)，说明 lz* 捕捉 difficulty-ordering 一致性而非准确率。\n14. **Inverted-U 是模型相关的** — Qwen 在 15%→50% 区间出现强 inversion（Δlz* 50%=-1.39 << 15%=-4.83），Llama 和 Mistral 在此区间 Δlz* 单调增大。Inverted-U 在 free-θ 下由 baseline misfit 调制——高 baseline lz* (Qwen +8.68) 的模型更容易出现 non-monotonicity。论文不能 claim inverted-U 为 universal phenomenon，需加 model-dependent caveat。θ-fixed 分析仍恢复所有家族的 monotonicity — 这是 θ-fixed 贡献的关键证据。\n15. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.42, n=3, ddof=1, ℓz*-corrected).\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015, ℓz*-corrected)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds (ℓz*-corrected)**: s1=9.47, s2=7.05, s3=9.53 (s2 outlier; mean=8.68, std=1.41). Key results: (a) contam_15 |Cohen's d|=3.42 (n=3, ddof=1, strong effect); (b) contam_50 |d|=0.99 (n=3, ddof=1, borderline large); (c) free-θ dose-response non-monotonic and more extreme after correction (contam_50 Δlz*=1.40 < contam_15 Δlz*=4.84, ratio=3.46) due to θ-shift confound; (d) **θ-fixed analysis (ℓz*-corrected)**: θ_fixed=-0.0965 (n=3 clean θ_MLE mean, unchanged by ℓz* correction); lz*_fixed: contam_15=11.852, contam_50=18.576; Δlz*_fixed: contam_15=+3.17, contam_50=+9.89; ratio=3.12 (virtually unchanged from uncorrected 3.12 — Snijders correction scales proportionally); (e) seen/unseen memorization fingerprint; (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: all values ℓz*-corrected (Snijders 2001); prior uncorrected ℓz values archived as *_lz_uncorrected.json.\n- **Cross-family validation (exp-ctrl-contam-llama, ℓz*-corrected)**: Llama-3.1-8B-Instruct × MMLU, 3+2 conditions. **n=3 clean seeds (ℓz*-corrected)**: s1=0.845, s2=-0.182, s3=-1.084 (mean=-0.14, std=0.97). contam_15 lz*=-2.992 (θ=-0.276), contam_50 lz*=-3.331 (θ=-0.149). Δlz*: contam_15=-3.84, contam_50=-4.18, both significant. **Cohen's d (n=3, ddof=1)**: contam_15 d=-2.95 (large), contam_50 d=-3.31 (large), monotonic (|d_50|>|d_15|) — contrasting Qwen's non-monotonicity. **Free-θ**: slight monotonicity (ratio=1.09), contrasting Qwen's strong non-monotonicity (ratio=3.46). **θ_fixed (θ=-0.666)**: lz*_fixed contam_15=0.959, contam_50=1.172; Δlz*_fixed=+0.114/+0.327; ratio=2.87 (enhances monotonicity). θ-shift mechanism universal: Δθ Llama 0.39/0.52, Qwen 0.29/0.47. Memorization fraction ~0.33-0.38. **Narrative**: Qwen story = \"θ_fixed repairs non-monotonicity\"; Llama story = \"θ_fixed enhances existing monotonicity\". Both confirm θ_fixed recovers/strengthens dose-response. Non-monotonicity is model-dependent (modulated by baseline misfit magnitude). Qwen clean lz*=8.68 vs Llama -0.14 — discuss in §6. **Cross-family Cohen's d summary**: Qwen d_15=-3.42/d_50=-0.99; Llama d_15=-2.95/d_50=-3.31. Both families |d|>2.9 at 15%, confirming detection generalizes.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-two-sided\n  registry_id: exp-two-sided\n  claim: 2\n  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case\n    study）。包括 bootstrap confidence interval 和 FDR 控制。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- id: exp-extended-sim\n  registry_id: exp-extended-sim\n  claim: 2\n  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让\n    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向\n    lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 依赖 exp-two-sided 的双侧框架定义。\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- id: exp-ctrl-contam-pilot\n  claim: 1,2,3\n  description: 快速验证：Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU only。测量\n    Δlz*(clean→contaminated) 是否显著。增加第二个 0% seed 作为 clean-vs-clean noise floor baseline\n    (Reviewer Q2/Q4)。Eval 时区分 seen/unseen items 以实测 memorization fraction (Reviewer\n    Q3/W9)。这是论文 go/no-go 信号。\n  priority: P0-CRITICAL\n  gpu_budget_hours: 12\n  deps: []\n  status: planned\n  notes: 'GPU 恢复后第一优先。4 conditions × ~3 hrs = ~12 GPU-hrs (+2h for second 0% seed)。关键输出:\n    (a) Δlz* 显著性, (b) clean-vs-clean Δlz* ≈ 0 验证, (c) memorization fraction = (Δacc_seen\n    - Δacc_unseen)/Δacc_seen, (d) adjusted power = theory × memorization fraction。D010\n    要求。'\n- id: exp-ctrl-contam\n  claim: 1,2,3\n  description: 完整控制实验：在 4 个模型上用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，测量\n    Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - exp-ctrl-contam-pilot\n  status: planned\n  notes: '模型: Qwen3.5-9B + Gemma-4-31B + Llama-3.1-8B + Mistral-7B-v0.3。Benchmark:\n    MMLU + GSM8K + HellaSwag。4 模型 × 6 levels × 3 benchmarks。'\n- id: exp-empirical-null\n  registry_id: exp-empirical-null\n  claim: 1\n  description: Bootstrap empirical null 分析：量化 lz* 在真实 LLM 数据上的 systematic bias（null\n    mean ≠ 0, null std ≠ 1），为 Calibration Gap Analysis 提供定量证据。包含 Q-Q plots、KS tests、bias\n    量化表、unflagged cells 深度分析。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: DONE\n  notes: CPU only. 复用 exp-two-sided v2 的 bootstrap 逻辑，但保存完整中间分布。~2h 开发+运行。\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- id: exp-power-theory\n  registry_id: exp-power-theory\n  claim: 2\n  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A\n    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: DONE\n  notes: 纯理论推导 + 数值验证。CPU only.\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- id: exp-leaderboard-data-recon\n  registry_id: exp-leaderboard-data-recon\n  claim: 3\n  description: Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results\n    是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item\n    data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: DONE\n  notes: 纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- id: exp-leaderboard-audit\n  claim: 3\n  description: Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark\n    污染率随时间趋势。\n  priority: ABANDONED\n  gpu_budget_hours: 20\n  deps:\n  - exp-two-sided\n  - exp-leaderboard-data-recon\n  status: planned\n  notes: 'D011: v1-irt-refit a_r=0.111 + item alignment 54.56% → 13K audit 不可行。数据可用性写入\n    Discussion/Future Work。'\n- id: exp-natural-experiment\n  claim: 3\n  description: v1 leaderboard base→chat model pairs 自然实验：计算 Δlz* = lz*(chat) - lz*(base)\n    作为 SFT 效应代理。\n  priority: P2-optional\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: 'D013: a_r=0.111 导致 lz*≈accuracy-like, 仅 4-5 pairs 无统计检验能力。Reviewer 终审建议降级。'\n- id: exp-v1-irt-refit-expanded\n  claim: 3\n  description: 扩大 v1 IRT 重拟合样本量至 N≥500，验证 pilot N=63 的 a_r=0.111 是否因样本量不足。最终关闭 Path\n    D。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-v1-irt-refit-pilot\n  status: planned\n  notes: CPU only. Reviewer 要求 N≥500 才能最终结论 Path D。阈值：a_r>0.4=可行, a_r<0.2=dead。\n- id: exp-4pl-ablation\n  claim: 1\n  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter\n    d 对 false alarm 和 detection power 的影响。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\n- id: exp-baseline-comparison\n  claim: 1\n  description: '与现有方法对比（≥5 baselines）：在控制实验的 ground-truth contaminated models 上，比较\n    IRT-FIT vs baselines 的 AUROC/Type-I error。Baselines: (1) ConStat (re-test), (2)\n    Min-K%++ (token probs), (3) accuracy z-score (已完成, CPU), (4) PPL-based detection\n    (log-prob family 代表, 预期 RL-robust 测试中失败), (5) random baseline。量化 minimal-information\n    的代价（power 损失）。报告 bootstrap CIs（同行 6/8 不报告方差，这是我们的差异化优势）。'\n  priority: P0-end\n  gpu_budget_hours: 30\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: 蒸馏显示同行 baseline 中位数 ~5 个。accuracy z-score 已完成(CPU)。ConStat 需 re-test, Min-K%++\n    需 token probs, PPL 需 log-probs。exp-ctrl-contam 完成后立即执行。\n- id: exp-multiscale-lzm\n  claim: 1,3\n  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化\n    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要实现 lzm 公式。\n- id: exp-post-rl\n  claim: 1\n  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应\n    Wang et al. (2025) 的 MIA 失效问题。\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\n- id: exp-extra-benchmarks\n  claim: 2,3\n  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items\n    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\n- id: exp-domain-analysis\n  claim: 3\n  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5\n    的 MMLU 污染是全面的还是集中在特定 domain。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要 MMLU item-to-domain 映射。\n\n\n## registry (completed experiments)\n\n- exp_id: sim_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    null_check:\n      all_pass: true\n      gsm8k_ks_p: 0.098\n      hellaswag_ks_p: 0.224\n      mmlu_ks_p: 0.594\n    simulation_power_at_15pct:\n      mmlu: 0.979\n      hellaswag: 0.733\n      gsm8k: 0.578\n      arc_c: 0.129\n      humaneval: 0.243\n    global_pass: false\n    inverted_u_all_benchmarks: true\n    pass_count_large_80pct: 1/3 (mmlu only)\n- exp_id: phase_b_personfit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_sd_all_gt_0.5: true\n    mmlu_lz_star_mean: 24.19\n    mmlu_lz_star_sd: 16.47\n    hellaswag_lz_star_mean: 20.09\n    hellaswag_lz_star_sd: 17.59\n    gsm8k_lz_star_mean: 8.22\n    gsm8k_lz_star_sd: 8.97\n    gemini15_mmlu_lz_star: 34.75\n    gemini15_mmlu_accuracy: 1\n    gemini15_mmlu_theta: 0.78\n    gemini15_flagged_benchmarks: 3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\n    cross_benchmark_spearman_significant: 1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\n    n_models: 12\n    n_benchmarks: 5\n- exp_id: exp-two-sided\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n- exp_id: exp-extended-sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_sims: 2000\n    levels: 0/3/5/10/15/25/50/60/75/90/100\n    n_excluded_100pct: 0\n    inverted_u_all_5: true\n    dual_regime_crossover: 75-90%\n    mmlu_power_15pct: 0.9845\n    hellaswag_power_15pct: 0.7525\n    gsm8k_power_15pct: 0.5905\n    mmlu_100pct_lz_star: 31.815\n    hellaswag_100pct_lz_star: 26.297\n    gsm8k_100pct_lz_star: 8.253\n    arc_c_100pct_lz_star: 4.339\n    humaneval_100pct_lz_star: 3.529\n    two_sided_power:\n      mmlu_15pct: 0.978\n      mmlu_50pct: 0.9525\n      mmlu_75pct: 0.936\n      mmlu_90pct: 0.9515\n      mmlu_100pct: 1\n      hellaswag_25pct: 0.9155\n      hellaswag_50pct: 0.9475\n      hellaswag_90pct: 0.9375\n      hellaswag_100pct: 1\n      gsm8k_50pct: 0.837\n      gsm8k_90pct: 0.794\n      gsm8k_100pct: 1\n    key_finding: 'Two-sided detection eliminates inverted-U: MMLU two-sided power\n      >93% at ALL contamination levels. 100% contamination → 100% detection on all\n      benchmarks.'\n- exp_id: exp-empirical-null\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_boot: 1000\n    n_cells: 60\n    mean_null_bias: 0.0925\n    mean_null_std: 1.0021\n    ks_reject_rate: 0.4\n    ks_reject_count: 24/60\n    bias_by_benchmark:\n      arc_c: 0.146\n      gsm8k: 0.082\n      hellaswag: 0.034\n      humaneval: 0.16\n      mmlu: 0.041\n    std_by_benchmark:\n      arc_c: 1.004\n      gsm8k: 1.01\n      hellaswag: 0.999\n      humaneval: 0.994\n      mmlu: 1.003\n    ks_reject_by_benchmark:\n      arc_c: 0.583\n      gsm8k: 0.5\n      hellaswag: 0.083\n      humaneval: 0.75\n      mmlu: 0.083\n    key_finding: Null bias is small (mean=0.09) and std is near 1.0 — the bootstrap\n      null is well-calibrated. The 95% flagging rate is NOT caused by miscalibrated\n      null but by genuine extreme lz* values in LLM data. Smaller benchmarks (humaneval,\n      arc_c) show higher KS rejection rates due to stronger finite-sample deviations\n      from normality.\n- exp_id: exp-leaderboard-data-recon\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_with_per_item_data: 13000+\n    benchmarks_covered: 4/5 (MMLU, HellaSwag, ARC-Challenge, GSM8K; missing HumanEval)\n    estimated_gpu_hours_if_needed: 0\n    v1_benchmarks: 6\n    v2_benchmarks: 6\n    data_format: parquet per-item rows with acc/acc_norm binary fields\n    source: open-llm-leaderboard-old/details_{model}\n    humaneval_gpu_hrs_per_7b_model: 0.08\n    key_finding: v1 details datasets contain per-item binary responses for 13K+ models.\n      Zero GPU cost for 4/5 benchmarks.\n- exp_id: exp-power-theory\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R2_two_sided: 0.9572\n    RMSE_two_sided: 0.0746\n    R2_left_tail: 0.9764\n    R2_mean_lz: 0.9948\n    sqrt_n_R2_avg: 0.88\n    crossover_range_pct: 81-85%\n    min_items_15pct_80power: 7958\n- exp_id: exp-item-alignment-check\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    match_rate_direct: 0.5456\n    match_rate_reordered_mistral: 0.8846\n    match_rate_reordered_vicuna: 0.7248\n    n_items_checked: 14042\n    n_models_verified: 2\n    alignment_method: content-based via cais/mmlu canonical order\n    items_mapped: 12068\n    mapping_coverage: 0.86\n- exp_id: exp-v1-irt-refit-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 63\n    n_models_failed: 38\n    n_items: 14042\n    n_mapped_items: 12441\n    overall_accuracy: 0.426\n    fitting_time_2pl_sec: 8.9\n    fitting_time_3pl_sec: 12.1\n    3pl_a_pearson_r: 0.111\n    3pl_b_pearson_r: 0.626\n    3pl_b_spearman_r: 0.656\n    2pl_a_pearson_r: -0.084\n    2pl_b_pearson_r: 0.572\n    lz_star_mean: 11.69\n    lz_star_std: 6.68\n    lz_star_flagged_pct: 1.6\n- exp_id: exp-accuracy-zscore-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_flagged_count: 4\n    lz_flagged_count: 57\n    agreement_rate: 0.117\n    gemini15_mmlu_zscore: 1.413\n- exp_id: exp-cross-benchmark-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_models_all5_flagged: 10\n    n_models_selective_flagged: 2\n    gemini15_cluster_isolation: true\n    dominant_direction_pattern: positive\n    pct_positive_cells: 93.3\n    total_flagged: 57\n    flag_rate: 0.95\n- exp_id: exp-ml-classifier-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    auroc_avg_25pct:\n      lz_star: 0.86\n      lr_resp: 0.899\n      rf_resp: 0.885\n      lr_resp_summ: 0.909\n      rf_resp_summ: 0.913\n    auroc_avg_5pct:\n      lz_star: 0.675\n      best_ml: 0.575\n    auroc_avg_10pct:\n      lz_star: 0.763\n      best_ml: 0.712\n    lz_star_advantage_low_contam: +0.10 AUROC at 5%, +0.05 at 10%\n    ml_advantage_high_contam: +0.05 at 25%, +0.16 at 50%\n    key_finding: lz* outperforms supervised ML at low contamination (5-10%) without\n      any training data; ML only wins at 25%+ where signal is already strong\n- exp_id: exp-fdr-correction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    flagged_uncorrected: 57/60 (95%)\n    flagged_bh_fdr: 57/60 (95%)\n    flagged_bonferroni: not_computed_but_expected_similar\n    correction_scope: global_60_tests\n    unflagged_cells:\n    - Yi-Lightning×arc_c (bh_p=0.098)\n    - 360GPT2-Pro×humaneval (bh_p=0.134)\n    - Yi-Lightning×humaneval (bh_p=0.181)\n    note: Reused existing BH-FDR from exp-two-sided v2 empirical_pvalues.csv. Leaderboard-scale\n      FDR (24800+ tests) deferred to leaderboard audit.\n- exp_id: exp-clean-control-delta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    clean_vs_clean_mean_abs:\n      mmlu: 0.01\n      hellaswag: 0.125\n      gsm8k: 0.021\n      arc_c: 0.095\n      humaneval: 0.02\n    clean_vs_clean_all_nonsig: true\n    clean_vs_contam_all_sig: true\n    cohens_d:\n      mmlu: 2.66\n      hellaswag: 1.85\n      gsm8k: 1.85\n      arc_c: 0.45\n      humaneval: 1.07\n    arc_c_note: d=0.45 < 0.5 threshold due to only 295 items, but still p<1e-10\n- exp_id: exp-natural-experiment\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_pairs: 21\n    n_benchmarks: 4\n    n_complete_pairs: 9\n    significant_benchmarks:\n      HellaSwag:\n        mean_deviation: -3.4\n        t_stat: -3.97\n        p_value: 0.001\n        interpretation: SFT systematically decreases person-fit on HellaSwag\n      GSM8K:\n        mean_deviation: 3.92\n        t_stat: 3.35\n        p_value: 0.009\n        interpretation: SFT systematically increases person-fit on GSM8K\n    non_significant_benchmarks:\n      MMLU:\n        p_value: 0.15\n      ARC-Challenge:\n        p_value: 0.38\n    individual_outliers: 0\n    key_finding: HellaSwag and GSM8K show significant systematic SFT effects on lz*,\n      but no individual pair shows benchmark-specific contamination outliers. P2-optional\n      per Director assessment.\n- exp_id: exp-v1-irt-refit-expanded\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_models_downloaded: 178\n    n_items: 14042\n    3pl_a_pearson_r: 0.127\n    2pl_a_pearson_r: -0.029\n    3pl_b_pearson_r: 0.663\n    reason: 'N=178 classical refit: a_r=0.127 (3PL), -0.029 (2PL), b_r=0.663. Discrimination\n      failure confirms Path D dead.'\n- exp_id: exp-4pl-ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hypothesis_confirmed: true\n    far_4pl: ~5% (well-calibrated)\n    far_3pl: 4.7-16.5% (inflated)\n    far_2pl: 50-100% (catastrophic, unusable)\n    mean_power_gain_4pl_vs_3pl:\n      MMLU: +27.3pp\n      HellaSwag: +26.1pp\n      GSM8K: +20.3pp\n      ARC_C: +14.8pp\n      HumanEval: +13.7pp\n    max_power_gain_4pl_vs_3pl:\n      MMLU: +49.0pp\n      HellaSwag: +59.6pp\n      GSM8K: +39.7pp\n      ARC_C: +54.6pp\n      HumanEval: +30.6pp\n    power_at_25pct:\n      4PL:\n        MMLU: 0.776\n        HellaSwag: 0.534\n        GSM8K: 0.73\n        ARC_C: 0.132\n        HumanEval: 0.318\n      3PL:\n        MMLU: 0.329\n        HellaSwag: 0.28\n        GSM8K: 0.334\n        ARC_C: 0.091\n        HumanEval: 0.165\n    d_bucket_analysis: 'd<0.8: +6.8pp to +61.2pp; d>=0.95: negligible'\n    key_finding: 4PL d parameter essential for LLM contamination detection. 46% MMLU\n      items have d<0.95. Ignoring d (3PL) halves detection power on average. 2PL completely\n      miscalibrated (FAR 50-100%).\n- exp_id: exp-domain-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_mmlu_accuracy: 100% (14042/14042)\n    gemini_domain_concentrated: false\n    gemini_subjects_flagged: 50/57 (lz*>1.96)\n    gemini_category_lz:\n      STEM: 21.2\n      Humanities: 17.9\n      Social Sciences: 15.9\n      Other: 15.3\n    doubao_negative_lz: true\n    doubao_category_lz:\n      STEM: -2\n      Humanities: -13\n      Social_Sciences: -14.8\n      Other: 4.4\n    hunyuan_uneven:\n      STEM: 1.8\n      Social_Sciences: 13.9\n    yi_lightning_highest_mmlu_lz: 48.2\n    qwen_plus_second_highest: 44.9\n    mistral_flagged_subjects: 55/57\n- exp_id: exp-ctrl-contam-pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohens_d_contam15: 6.575\n    cohens_d_contam15_ci:\n    - 4.514\n    - 15.199\n    cohens_d_contam50: 1.897\n    cohens_d_contam50_ci:\n    - 1.041\n    - 4.923\n    clean_n10_mean_lz: 8.684\n    clean_n10_sd_lz: 0.735\n    contam15_lz: 3.849\n    contam50_lz: 7.289\n    n_clean_seeds: 10\n    n_items: 14042\n- exp_id: exp-4pl-real-data-degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    correlation_4pl_vs_3pl:\n      pearson_r: 0.225\n      rmse: 68.41\n    most_affected_benchmark: MMLU (mean |Δlz*|=58.3, 46% items d<0.95)\n    most_affected_model: 'DeepSeek-V3 (θ=3.77): 3PL lz* from +16.4 to -340.6'\n    low_ability_models_impact: '|Δlz*|<2 (Gemma-2B-it, Vicuna, Mistral)'\n    bias_direction: 3PL systematically depresses high-ability models' lz* (d=1 makes\n      P→1, amplifying few-error aberrance)\n    key_finding: Ignoring d parameter makes lz* completely unreliable for high-ability\n      models — d-induced bias far exceeds any contamination signal\n- exp_id: exp-ctrl-contam-pilot-clean-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-clean-s2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-15\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-contam-50\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-pilot-clean-s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: 8.0806\n    accuracy: 0.6783\n    theta_mle: -0.1068\n    cohens_d_n3:\n      contam_15:\n        delta: -4.34\n        d: -3.58\n      contam_50:\n        delta: -1.9\n        d: -1.56\n    baseline_n3:\n      mean: 7.3449\n      std: 1.2137\n    baseline_n2:\n      mean: 6.9771\n      std: 1.4609\n- exp_id: exp-ctrl-contam-llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_corrected: true\n    method: Snijders (2001) lz*\n    clean_lz_star: 0.8446\n    clean_s2_lz_star: -0.1823\n    clean_s3_lz_star: -1.0844\n    clean_mean_lz_star: -0.1407\n    clean_std_lz_star: 0.9652\n    clean_acc: 0.5914\n    clean_theta: -0.6661\n    contam_15_lz_star: -2.9922\n    contam_15_acc: 0.6654\n    contam_15_theta: -0.276\n    contam_15_delta_lz_star: -2.8515\n    contam_50_lz_star: -3.3313\n    contam_50_acc: 0.6983\n    contam_50_theta: -0.149\n    contam_50_delta_lz_star: -3.1906\n    cohens_d_contam_15_ddof1: -2.95\n    cohens_d_contam_50_ddof1: -3.31\n    theta_fixed: -0.666\n    contam_15_lz_star_fixed: 0.959\n    contam_50_lz_star_fixed: 1.172\n    dose_response_ratio_free: 1.09\n    dose_response_ratio_fixed: 2.87\n    monotonic_free: true\n    monotonic_fixed: true\n- exp_id: exp-ctrl-contam-llama-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: 0.8446\n    acc: 0.5914\n    theta: -0.6661\n    seed: 42\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-llama-contam15\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -2.9922\n    acc: 0.6654\n    theta_mle: -0.276\n    acc_seen: 0.742\n    acc_unseen: 0.652\n    delta_lz_star: -2.8515\n    cohens_d_ddof1: -2.95\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-llama-contam50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -3.3313\n    acc: 0.6983\n    theta_mle: -0.149\n    acc_seen: 0.735\n    acc_unseen: 0.661\n    delta_lz_star: -3.1906\n    cohens_d_ddof1: -3.31\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-llama-clean-s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -0.1823\n    acc: 0.5954\n    theta: -0.63\n    seed: 123\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-llama-clean-s3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -1.0844\n    acc: 0.5943\n    theta: -0.64\n    seed: 456\n    method: Snijders (2001) lz*\n- exp_id: exp-post-rl\n  name: ''\n  status: ANALYZING\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-baseline-comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model_level:\n      qwen_contam15_lz_star_d: -3.42\n      qwen_contam50_lz_star_d: -0.99\n      llama_contam15_lz_star_d: -2.95\n      llama_contam50_lz_star_d: -3.31\n      qwen_contam15_acc_zscore_d: 160.6\n      qwen_contam15_ht_d: 3.21\n      llama_contam15_u3_d: -3.69\n    item_level_auroc:\n      lz_star_itemwise:\n        qwen_15: 0.536\n        qwen_50: 0.535\n        llama_15: 0.528\n        llama_50: 0.536\n      irt_residual:\n        qwen_15: 0.578\n        qwen_50: 0.563\n        llama_15: 0.582\n        llama_50: 0.581\n      lr_cross_model:\n        qwen_15: 0.586\n        qwen_50: 0.567\n        llama_15: 0.592\n        llama_50: 0.585\n      rf_within_model:\n        qwen_50: 0.63\n        llama_50: 0.629\n      random: 0.5\n    conclusion_summary: 'Model-level: all methods detect contamination (lz* d=-2.95~-3.42).\n      Item-level: all methods weak (max AUROC=0.63 with oracle). lz* advantage = unsupervised\n      + interpretable, not item-level superiority.'\n- exp_id: exp-ctrl-contam-mistral\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    clean:\n      lz_star: 5.4175\n      acc: 0.5138\n      theta: -1.1569\n    contam_15:\n      lz_star: -1.3849\n      acc: 0.5949\n      acc_seen: 0.7436\n      acc_unseen: 0.5686\n      theta: -0.7129\n    contam_50:\n      lz_star: -3.1503\n      acc: 0.6732\n      acc_seen: 0.7523\n      acc_unseen: 0.5941\n      theta: -0.3027\n    delta_lz_star_15: -6.8024\n    delta_lz_star_50: -8.5678\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-mistral-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: 5.4175\n    acc_overall: 0.5138\n    acc_seen: null\n    acc_unseen: 0.5138\n    theta_mle: -1.1569\n    lz_star_seen: null\n    lz_star_unseen: 5.4175\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-mistral-contam15\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -1.3849\n    acc_overall: 0.5949\n    acc_seen: 0.7436\n    acc_unseen: 0.5686\n    theta_mle: -0.7129\n    lz_star_seen: -1.0838\n    lz_star_unseen: -0.0956\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-mistral-contam50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star: -3.1503\n    acc_overall: 0.6732\n    acc_seen: 0.7523\n    acc_unseen: 0.5941\n    theta_mle: -0.3027\n    lz_star_seen: -1.3701\n    lz_star_unseen: -0.9972\n    method: Snijders (2001) lz*\n- exp_id: exp-ctrl-contam-qwen-clean-s4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6786\n    lz_star: 8.967\n    theta_mle: -0.109\n    n_items: 14042\n- exp_id: exp-ctrl-contam-qwen-clean-s5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6787\n    lz_star: 8.532\n    theta_mle: -0.088\n    n_items: 14042\n- exp_id: exp-ctrl-contam-qwen-clean-s6\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6771\n    lz_star: 8.245\n    theta_mle: -0.1036\n    n_items: 14042\n    loss: 1.354\n    steps: 939\n- exp_id: exp-ctrl-contam-qwen-clean-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6783\n    lz_star: 8.77\n    theta_mle: -0.0892\n    n_items: 14042\n- exp_id: exp-ctrl-contam-qwen-clean-s8\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6768\n    lz_star: 9.111\n    theta_mle: -0.1035\n    n_items: 14042\n    loss: 1.352\n    steps: 939\n- exp_id: exp-constat-comparison\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-mia-mink-comparison\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    base_auc_loss: 0.486\n    base_auc_mink10: 0.493\n    base_auc_minkpp10: 0.488\n    sft_auc_loss: 0.592\n    sft_auc_mink10: 0.611\n    sft_auc_minkpp10: 0.569\n- exp_id: exp-arcc-benchmark\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    19912_clean_s1_acc: 0.902\n    19912_clean_s1_lz: -5.448\n    19912_clean_s2_acc: 0.895\n    19912_clean_s2_lz: -5.433\n    19912_contam15_acc: 0.909\n    19912_contam15_lz: -4.917\n    19912_contam15_lz_seen: 0.568\n    19912_contam50_acc: 0.942\n    19912_contam50_lz: -4.573\n    19912_contam50_lz_seen: -0.331\n    35694_clean_s1_acc: 0.895\n    35694_clean_s1_lz: -5.511\n    35694_clean_s2_acc: 0.898\n    35694_clean_s2_lz: -5.493\n    35694_contam15_acc: 0.909\n    35694_contam15_lz: -5.032\n    35694_contam15_lz_seen: 0.186\n    35694_contam50_acc: 0.946\n    35694_contam50_lz: -4.185\n    35694_contam50_lz_seen: -0.475\n- exp_id: exp-ctrl-contam-qwen-clean-s9\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.6743\n    lz_star: 9.013\n    theta_mle: -0.1242\n    n_items: 14042\n- exp_id: exp-ctrl-contam-qwen-clean-s10\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    accuracy: 0.676\n    lz_star: 8.149\n    theta_mle: -0.116\n    n_items: 14042\n- exp_id: exp-arcc-clean-s1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    accuracy: 0.8949\n    theta_mle: 0.6872\n    lz_star: -5.5107\n    n_items: 295\n- exp_id: exp-arcc-clean-s2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: arcc-clean-s7\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: arcc-clean-s8\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: arcc-clean-s9\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: arcc-clean-s10\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-ctrl-contam-llama-clean-s4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:24:52.423Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:24:52.423Z",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-21T12:24:52.446Z_

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
  "promptId": "891baf3e-7cb7-44ed-9321-b968bbd781f4",
  "type": "user",
  "uuid": "f670399b-e931-4368-bd4a-f2be49c9f795",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:24:52.444Z_

```json
{
  "parentUuid": "f670399b-e931-4368-bd4a-f2be49c9f795",
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
  "uuid": "2dcf4e73-99d8-454f-908c-bfd273a99bc9",
  "timestamp": "2026-05-21T12:24:52.444Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:24:52.444Z_

```json
{
  "parentUuid": "2dcf4e73-99d8-454f-908c-bfd273a99bc9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "db85e75c-ed7f-425b-963d-a00aa077f399",
  "timestamp": "2026-05-21T12:24:52.444Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e",
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
  "leafUuid": "db85e75c-ed7f-425b-963d-a00aa077f399",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for IRT contamination detection paper",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:25:33.438Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research context carefully to define three tiers (best/median/worst) for the Dream simulation.

Key context:
- This is an IRT person-fit contamination detection paper targeting EMNLP 2026
- Core method: using IRT person-fit statistics (lz*) to detect benchmark contamination from binary response patterns alone
- Already completed: simulation (power 97.9% MMLU), controlled contamination on Qwen (d=3.42) and Llama (d=2.95/3.31), baseline comparison, 4PL ablation
- Pending critical experiments: exp-post-rl (failed/analyzing), exp-constat-comparison, exp-mia-mink-comparison, exp-arcc-benchmark


- The post-RL robustness question is crucial since exp-post-rl already failed, and I need to determine whether lz* can survive GRPO training
- The HT versus lz* differentiation is equally important for establishing that lz* offers unique advantages beyond existing hypothesis testing approaches
- I'm weighing these uncertainties against the additional baselines like ConStat and MIA/Min to structure the tier definitions

, while also considering how ARC-C's small sample size and Mistral's limited validation (n=1, no seeds) affect the overall evidence strength
- The strongest evidence comes from Qwen and Llama showing consistent detection at 15% contamination, the 4PL ablation clarity, and the cross-family memorization fraction consistency
- I need to prioritize which metrics matter most for tiering: whether post-RL detection survives, the magnitude of HT versus lz* separation, how many model families have complete validation, how many baselines are beaten, and small benchmark detection power

Now I'm thinking through how to tier the paper's claim strength based on what the results actually show. The best-case scenario is if post-RL detection holds up—meaning lz* survives GRPO while HT degrades or fails—because that gives a clear structural advantage story across three or more families with baselines confirming the minimal-information approach is uniquely valuable. The middle ground is if post-RL results are ambiguous or both methods degrade similarly, which would shift the framing from structural advantage to a principled framework with unique interpretability, requiring softer claims about RL robustness. The worst case is if post-RL completely eliminates the signal across all person-fit methods, HT matches lz* everywhere, and methods like MIA or Min-K++ actually work on SFT contamination—that would undermine the minimal-information framing and force a reframe around mechanistic interpretability instead.

I'm also setting specific metric thresholds to evaluate which tier we're in: post-RL performance is the key differentiator, with lz* needing |d| > 2.0 while HT drops below 1.0 for the best case; baseline methods need to show AUROC < 0.6 where lz* achieves d > 2.9; and HT differentiation needs to hold up across the board.

Writing YAML config...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db85e75c-ed7f-425b-963d-a00aa077f399",
  "isSidechain": false,
  "requestId": "req_011CbFi6poZqNdsK5kZmo1HV",
  "type": "assistant",
  "uuid": "3355acc2-aece-408e-97bf-d90996bab9e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vX8XGxzoctaW16hXpEAMs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26418,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26418
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

_source line 9 · 2026-05-21T12:26:08.366Z_

```yaml
tiers:
  best:
    meaning: "Post-RL differentiates lz* from HT/baselines; all claims hold at full strength"
    key_assumptions:
      - "exp-post-rl: lz* retains detection after GRPO (|d|>2.0) while HT degrades (<1.0) or MIA-family fails"
      - "HT post-RL signal loss provides empirical differentiation (R12 Best scenario)"
      - "ConStat/MIA baselines fail or require strictly more information to match lz* performance"
      - "ARC-C small-benchmark results show detectable signal with θ-fixed (|d|>1.5)"
      - "Mistral single-seed Δlz*=-6.8/-8.6 replicated with additional seeds → third family validated"
    number_ranges:
      post_rl_lz_star_cohens_d: [2.0, 4.0]
      post_rl_ht_cohens_d: [0.0, 1.0]
      post_rl_mia_auroc: [0.45, 0.55]
      n_families_validated: [3, 4]
      n_baselines_beaten: [5, 7]
      arcc_theta_fixed_d: [1.5, 3.0]
      constat_retest_auroc: [0.55, 0.70]
      mink_sft_auroc: [0.50, 0.62]
    narrative_direction: >
      "IRT person-fit is structurally robust to post-RL — the only binary-only method
      that survives the RL distributional shift that destroys all log-prob methods (Wang et al.)
      AND simpler person-fit statistics (HT). The 4PL parameterization provides both
      detection power (8× Guttman/U3) and RL robustness that difficulty-only statistics lack.
      Minimal-information operating point is not merely a constraint but a structural advantage."

  median:
    meaning: "Post-RL ambiguous or both lz*/HT survive; reframe around interpretability and framework contribution"
    key_assumptions:
      - "exp-post-rl: signal partially degrades for all person-fit methods (lz* |d| 1.0-2.0, HT similar)"
      - "OR: both lz* and HT retain signal post-RL (no empirical differentiation)"
      - "lz* vs HT differentiation relies on data-independent arguments (parametric null, Snijders correction, 4PL item weighting)"
      - "ConStat achieves comparable model-level detection but requires retest (more information)"
      - "MIA/Min-K++ weak on SFT contamination (AUROC 0.55-0.65) — confirms binary-only is not inferior"
      - "Mistral n=1 treated as supporting evidence, not full validation"
    number_ranges:
      post_rl_lz_star_cohens_d: [1.0, 2.0]
      post_rl_ht_cohens_d: [0.8, 2.0]
      post_rl_mia_auroc: [0.45, 0.55]
      n_families_validated: [2, 3]
      n_baselines_beaten: [3, 5]
      arcc_theta_fixed_d: [0.5, 1.5]
      constat_retest_auroc: [0.70, 0.85]
      mink_sft_auroc: [0.55, 0.65]
    narrative_direction: >
      "IRT person-fit provides a principled contamination detection framework at the
      minimal-information operating point, with unique mechanistic interpretability
      (θ-shift analysis, memorization fraction quantification, parametric null distribution).
      While simpler statistics (HT) achieve comparable raw detection power, lz* offers:
      (i) calibrated hypothesis testing via known null N(0,1), (ii) Snijders correction
      for θ estimation error, (iii) full 4PL item-heterogeneity weighting critical for
      multi-domain benchmarks like MMLU. Post-RL robustness is demonstrated but shared
      across the person-fit family — the structural immunity to distributional shifts
      is a class-level advantage over log-prob methods. Claims soften from 'lz* uniquely
      robust' to 'person-fit family robust; lz* uniquely interpretable.'"

  worst:
    meaning: "Post-RL destroys all person-fit signals; HT matches lz* everywhere; reframe as framework + empirical characterization paper"
    key_assumptions:
      - "exp-post-rl: GRPO eliminates detection for all binary-only methods (|d|<0.5)"
      - "HT matches or exceeds lz* in all tested conditions (no empirical differentiation)"
      - "MIA/Min-K++ achieve AUROC 0.65+ on SFT contamination (minimal-information penalty is real)"
      - "ARC-C too small for reliable detection even with θ-fixed (|d|<0.5)"
      - "Cross-family generalizability limited to SFT-only contamination scope"
    number_ranges:
      post_rl_lz_star_cohens_d: [0.0, 0.5]
      post_rl_ht_cohens_d: [0.0, 0.5]
      post_rl_mia_auroc: [0.45, 0.55]
      n_families_validated: [2, 2]
      n_baselines_beaten: [2, 3]
      arcc_theta_fixed_d: [0.0, 0.5]
      constat_retest_auroc: [0.80, 0.95]
      mink_sft_auroc: [0.60, 0.75]
    narrative_direction: >
      "Reframe: NOT a detection superiority paper. Three reframing angles for same venue:
      (A) Empirical characterization paper — first systematic study of how LLM response
      patterns relate to IRT assumptions. Universal 4PL misfit (57/60 flagged) is a novel
      finding about LLM cognition. θ-shift mechanism is a methodological contribution
      to contamination science regardless of detection power.
      (B) Scope-honest detection paper — IRT-FIT detects intentional SFT contamination
      (|d|>2.9 across two families) with explicit scope boundary: post-RL training
      smooths binary signal below detection threshold for ALL binary-only methods. This
      negative result (RL boundary) is itself a contribution — it maps the detection
      frontier's limits. Frame as: 'we establish where binary detection works and
      precisely where it fails.'
      (C) Framework + toolkit paper — open-source IRT-FIT toolkit + 13K model data
      availability + memorization fraction methodology. Contribution is the framework
      (connecting psychometrics to LLM evaluation) not detection SOTA. θ-shift analysis,
      seen/unseen decomposition, and dose-response characterization are methodological
      contributions independent of absolute detection power. Still targets EMNLP as
      evaluation methodology with community tooling impact."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3355acc2-aece-408e-97bf-d90996bab9e6",
  "isSidechain": false,
  "requestId": "req_011CbFi6poZqNdsK5kZmo1HV",
  "type": "assistant",
  "uuid": "586a2f2f-15ad-41ee-99d9-d2b4066d4395",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vX8XGxzoctaW16hXpEAMs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26418,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26418
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
  "leafUuid": "586a2f2f-15ad-41ee-99d9-d2b4066d4395",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for IRT contamination detection paper",
  "sessionId": "55d21821-fcc3-4f5e-bb80-174ec535ba8e"
}
```

---
