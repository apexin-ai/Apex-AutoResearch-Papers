# Paper Framing — irt_personfit_contam

## Target Venue
- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)

## Core Reframe (D031, 2026-05-21)

**旧 narrative**: "ℓz* 作为 LLM contamination 检测工具"
**新 narrative**: "首次系统刻画 IRT person-fit 在 LLM benchmark contamination 检测中的行为边界"

贡献不是 "提出检测方法"，而是 "回答: binary response patterns 能检测到什么？在什么条件下？什么条件下失效？" 这是 characterization paper, 不是 tool paper。

## Core Claims (3 条, n=10 updated)

**Claim 1 (Boundary Conditions of IRT Person-Fit for Contamination Detection)**:
IRT person-fit statistics detect SFT contamination with large effect sizes across three model families and two benchmarks (all 8 Cohen's d CIs exclude zero, n=10 per condition). However, detection power is modulated by boundary conditions that we systematically characterize: (a) **θ-shift absorption** — contamination raises θ_MLE, and high-baseline-accuracy models (Qwen 83%) absorb more signal (d_50=1.08) than low-baseline models (Llama 59%, d_50=2.50); (b) **inverted-U dose-response** — under free-θ estimation, Qwen shows non-monotonic detection (d_15=4.83 > d_50=1.08), while z-score increases monotonically; (c) **benchmark size × θ-boundary interaction** — ARC-C (295 items) shows d_50=5.30 vs MMLU d_50=1.08 due to θ estimation ceiling effects. The **detection-diagnosis tradeoff**: z-score |d| >> HT |d| ≥ lz* |d| (Qwen 15%: z=42, HT=7.3, lz*=4.8). Simpler statistics detect more powerfully, but only lz* enables diagnostic characterization (seen/unseen decomposition, θ-shift mechanism, inverted-U). HT also exhibits inverted-U (Qwen HT d_15=7.3 >> d_50=1.7), confirming θ-shift absorption affects all person-fit statistics. **Post-RL (D033/D034)**: GRPO training erases accuracy-based signal (seen/unseen gap 11pp→0.2pp) but ℓz* pattern gap persists (~3.3) — a hard boundary for accuracy-based methods with residual structure in response patterns. N=1 model (Qwen), caveat in Limitations.

**Claim 2 (Detection Characterization + Baselines)**:
Detection power follows an empirical power function with benchmark size (R²=0.65, upper bound). ARC-C (295 items) validates cross-benchmark applicability. **Degradation chain baseline comparison**: at detection level, HT (difficulty-only) matches ℓz* (full 4PL); accuracy z-score also detects in controlled settings (z=56.7 at contam_50). But z-score cannot capture inverted-U (monotonically increases), seen/unseen decomposition, or θ-shift mechanism. ℓz*'s unique value: (i) parametric null ≈N(0,1) enables direct hypothesis testing; (ii) Snijders correction compensates θ estimation error; (iii) 4-parameter item weighting handles cross-subject heterogeneity. Item-level detection near-random for ALL binary methods (AUROC 0.52–0.63) — contamination signal is diffuse, model-level aggregation essential.

**Claim 3 (Empirical Findings from Real LLM Data)**:
(a) **Universal 4PL model misfit** — 57/60 cells flagged (|lz*| >> 5), LLM response patterns fundamentally violate IRT assumptions. Motivates Δlz* design. (b) **Cross-family baseline divergence** — clean lz* spans ~9σ (Qwen +8.28, Mistral +5.42, Llama -0.14), precluding absolute threshold detection. Relative detection (Δlz*/Cohen's d) is essential. (c) **PSN-IRT 12-model case study** with validated 4PL parameters.

## Story Spine

**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.

**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.

**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.

**Headline result template (D031 reframed)**: "We systematically characterize the behavior of IRT person-fit statistics for LLM benchmark contamination detection. Using controlled contamination (QLoRA SFT) across three model families (Qwen, Llama, Mistral) and two benchmarks (MMLU, ARC-C), we find: (1) ℓz* detects contamination with large effect sizes (all 8 Cohen's d CIs exclude zero, n=10), but a degradation chain (4PL→HT→z-score) reveals full IRT parameterization is unnecessary for mere detection; (2) ℓz*'s unique value lies in characterizing boundary conditions — inverted-U dose-response (model-dependent, driven by θ-shift absorption), benchmark-size × θ-boundary interactions, and model-specific detection profiles; (3) post-RL training erases accuracy-based signals but ℓz* pattern structure persists, defining a hard boundary for accuracy-based methods. We provide the first systematic mapping of where IRT person-fit works, where it degrades, and why."

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
| R7 | "Post-RL contamination?" | **RESOLVED (D033/D034)**: GRPO v3 falsified post-RL robustness — accuracy gap erased (83.1%→73.2% seen, gap 0.2pp). But ℓz* pattern gap persists (~3.3). Frame as negative-as-contribution: "hard boundary for accuracy-based binary methods" + "residual response pattern structure post-RL." N=1 model caveat in Limitations. | exp-post-rl-v3 |
| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
| R9 | "No same-level binary-only baselines" | **UPDATED (n=10)**: Detection power hierarchy: z-score |d|>>HT |d|≥lz* |d|. Qwen 15%: z=42.3, HT=7.3, lz*=4.8. HT also shows inverted-U. Item-level: all methods near-random (AUROC 0.52–0.63). Framing: simpler statistics detect better, but lz* uniquely enables diagnostic characterization. | exp-baseline-comparison |
| R12 | "HT > ℓz* for detection — why use ℓz*?" | **RESOLVED via detection-diagnosis tradeoff (n=10 data)**: HT |d| ≥ lz* |d| confirmed — HT is actually BETTER at detection. But lz*'s value is diagnostic: (i) parametric null ≈N(0,1) for hypothesis testing; (ii) Snijders correction compensates θ estimation error; (iii) θ-fixed analysis quantifies absorption (Qwen d 1.08→14.52); (iv) seen/unseen decomposition. Paper frames as: "detection-diagnosis tradeoff — use z-score/HT to detect, use lz* to characterize." | exp-baseline-comparison, exp-post-rl-v3 |
| R13 | "Minimal-information overstates" | **[Dream D2 三档一致]** "Minimal-information operating point" obscures PSN-IRT 4PL parameter dependency. Reframe to "minimal information **from the target model**" or "minimal runtime information" — explicitly acknowledge PSN-IRT calibration as an external input requirement. | — |
| R10 | "Leaderboard audit baseline unreliable" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |
| R11 | "Power function is upper bound" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |

## Key Narrative Elements (from External Review + Distillation)

1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
2. **Definitional pivot (à la ConStat)** — "All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?" This reframes our work as problem reformulation, not just cross-domain transfer.
3. **Post-RL as hard boundary (D033/D034)** — GRPO v3 erases accuracy-based contamination signal (seen/unseen gap 11pp→0.2pp). Wang et al. (ICLR 2026) shows all 10 log-prob methods ≈ random on RL-trained models. Binary accuracy-based methods (including ℓz* at detection level) also fail. BUT: ℓz* seen/unseen pattern gap persists (~3.3) post-RL — response pattern structure survives even when accuracy signal is erased. Frame as: "RL post-training defines a hard boundary for accuracy-based detection, but response-pattern-level structure may persist." NOT "RL-robustness as structural advantage" (falsified by D033).
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
- **Controlled contamination — FINAL n=10 data (2026-05-21 recalculated, Snijders-corrected)**:

  | Model | Benchmark | d(15%) | 95% CI | d(50%) | 95% CI |
  |-------|-----------|--------|--------|--------|--------|
  | Qwen 2.5-7B | MMLU | 4.83 | [2.94, 14.29] | 1.08 | [0.30, 3.93] |
  | Llama 3.1-8B | MMLU | 2.27 | [1.56, 4.63] | 2.50 | [1.76, 5.19] |
  | Mistral 7B v0.3 | MMLU | 2.64 | [1.49, 7.38] | 3.50 | [2.09, 9.59] |
  | Qwen 2.5-7B | ARC-C | 3.16 | [2.01, 9.54] | 5.30 | [3.64, 15.49] |

  All 8 CIs exclude zero. **Qwen contam_50 CI [0.30, 3.93] — lower bound near zero due to inverted-U (θ-shift absorption). Must be honestly reported + θ-fixed analysis presented as remedy.**

  Key patterns: (a) Qwen inverted-U (d_15=4.83 > d_50=1.08), Llama/Mistral monotonic (d_50 > d_15); (b) θ-shift absorption modulated by baseline accuracy (Qwen 83% >> Llama 59%); (c) ARC-C d_50=5.30 >> MMLU d_50=1.08 (benchmark size × θ-boundary); (d) Degradation chain: HT achieves |d| within 0.3 of ℓz*, z-score also detects (z=56.7 at contam_50).

  **Note**: n=10 recalculation changed values from earlier n=3 reports (e.g., Qwen d_15 was 3.42→4.83 due to Snijders correction factor recalculation with 10 seeds). Registry n=10 version is authoritative.

- **GRPO Post-RL (D033/D034)**: Qwen 2.5-7B, GRPO after SFT contamination.
  - acc_seen: 83.1% → 73.0% → 73.1% → 73.2% (step 0/500/1000/1500)
  - acc_unseen: 73.1% (stable) → gap erased by step 500
  - ℓz* seen/unseen gap: 3.67 → 3.59 → 3.32 (pattern persists after accuracy erasure)
  - **Conclusion**: accuracy-based detection = hard boundary post-RL; pattern-level structure persists. N=1 model, Limitations caveat.

- **z-score baseline (D032)**: z-score detects contamination in ctrl-contam (z=56.7 at contam_50, trivially significant). BUT: z-score monotonically increases with contamination dose, cannot capture inverted-U phenomenon. Confirms degradation chain at detection level; ℓz* value is characterization, not detection.

- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).
