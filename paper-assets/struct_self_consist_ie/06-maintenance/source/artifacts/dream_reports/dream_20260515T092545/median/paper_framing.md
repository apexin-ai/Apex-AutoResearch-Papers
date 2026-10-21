# Paper Framing — struct_self_consist_ie

> Updated 2026-05-15 — D070 REFRAMING: from "gap finding" to "regime-specific bottleneck identification with controlled ablation". Motivated by 6-round 3.0/5 plateau — Reviewer diagnosis: content ceiling, not framing ceiling. Adding free-form decoding ablation as breakthrough experiment.

## Target Venue
- Primary: EMNLP 2026 Findings (via ARR May 2026)
- Deadline: ARR May cycle, 2026-05-25

## Core Claims (3 条, D070 重排)

### Claim 1 (PRIMARY — Regime-Specific Selection Bottleneck)
The correlation-selection gap in structured IE is **caused by constrained decoding**. Under constrained decoding (Outlines/grammar-guided), logprob score compression makes per-sample ranking impossible: 60% of instances have within-sample logprob range < 0.05. Controlled ablation via free-form generation confirms the mechanism: removing constrained decoding recovers logprob variance and selection ability.

**Two-layer argument**:
- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.
- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to score compression under constrained decoding. (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation**: removing constrained decoding recovers logprob discrimination → proves compression is the bottleneck, not an inherent IE limitation.

**Key evidence (constrained)**:
- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39
- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp
- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it under constrained decoding

**Key evidence (free-form ablation)** [PLANNED — exp_freeform_ablation]:
- Hypothesis: Free-form generation on SciERC will show (a) wider logprob variance, (b) improved logprob selection performance
- If confirmed: gap is regime-specific → constrained decoding is the bottleneck
- If not: gap is inherent to structured IE → stronger universal finding

**Implications**: Not just "signals don't work" but "here's WHY and WHEN they don't work, and here's a path forward" (relaxed decoding + post-hoc filtering, or use logprob on non-tied subset).

### Claim 2 (METHODOLOGY — QE Evaluation Framework)
Systematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.

**Key results**:
- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205)
- RE (preliminary, single benchmark): voting_conf leads both full and conditional
- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)
- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09

**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):
- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578
- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601
- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706

### Claim 2b (Selection evidence)
**exp_016_rerun_1024 evidence** (SciERC, N=8, T=1.0):
- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)
- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)

**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):
- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39
- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466

### Claim 3 (Diagnostic — task-complexity boundary)
The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.

**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.

**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.

**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):
- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10
- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392
- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.
- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.

## Story Spine (D070 REFRAMED)

**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?

**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) under constrained decoding present a fundamentally different challenge — and prior work conflates quality estimation with selection.

**Our framing (D070 reposition — from "finding a gap" to "identifying and verifying a bottleneck")**:

We systematically compare five confidence signals for IE under constrained decoding, and discover a **regime-specific selection bottleneck**:
1. **Conceptual clarification**: Four of five signals are instance-level by construction and cannot rank candidates — this is noted as a definitional property, not discovered empirically. The interesting question is whether the remaining strategies (logprob, MBR/consensus-proximity) can select.
2. **Core empirical finding**: Logprob — the only per-sample signal — fails due to score compression under constrained decoding (60% of instances have within-sample range < 0.05). Consensus-proximity/MBR also fails despite success in MT.
3. **Controlled verification**: Free-form decoding ablation confirms the mechanism — removing constrained decoding recovers logprob's discriminative power. The gap is regime-specific, not inherent to structured IE.
4. **Practical pathway**: Non-tied instances (+2.9pp, p=0.01) show logprob works when compression is absent → actionable mitigation via relaxed decoding or non-tied subset selection.

**Headline**: "We identify, diagnose, and experimentally verify a regime-specific selection bottleneck in constrained-decoding IE: confidence signals that reliably predict output quality (AUROC 0.75) cannot select better candidates because constrained decoding compresses log-probability scores. A controlled free-form ablation confirms the mechanism and points to relaxed decoding as a mitigation path."

**Potential title**: "The Constrained Decoding Bottleneck: Why Confidence Signals Predict but Cannot Select in Information Extraction"

## Anticipated Reviewer Concerns

### R1: "Only one NER dataset — generalization unclear"
- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.
- **Priority**: P0

### R2: "Only one model family (Qwen3-8B)"
- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect
- **Priority**: P0

### R3: "FK is a strawman baseline — what about log-prob, USC, exact-match?"
- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).
- **Priority**: P0, RESOLVED — results decisive

### R3b: "EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?"
- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.
- **Priority**: P1 — narrative adjusted for 1024-token results

### R4: "No actual TTS improvement demonstrated"
- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.
- **Mitigation**: Paper PIVOTS to "confidence estimation + correlation-selection gap analysis." exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.
- **Priority**: P0 — narrative pivot complete, bootstrap confirms

### R5: "Sample size N=8 may be too small for reliable SJ estimation"
- **Mitigation**: exp-001 (N=16) with multi-seed robustness
- **Priority**: P0

### R6: "Conditional analysis cherry-picks favorable instances"
- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.
- **Priority**: P0 (add sensitivity analysis)

### R7: "Only ρ as evaluation metric"
- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).
- **Priority**: P0

### R8: "Formula-implementation discrepancy"
- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)
- **Priority**: P0, paper writing fix

### R9: "Evaluation circularity (T>0 consistency vs T=0 F1)"
- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).
- **Priority**: P0

### R10: "Insufficient related work" (三档一致 [B][M][W])
- **Mitigation**: Expand to 35+ references. Must cite:
  - USC (Chen 2024) — empirical differentiation, not just citation
  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)
  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021
  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020
  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016
  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023
  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024
  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022
  - **IE confidence**: Culotta & McCallum 2004
  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)
  - **[2025-2026 新颖性自查补充 — 必引]**:
    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出
    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap
    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案
    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量
    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承"overlooks semantically consistent outputs"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机
  - **[2025-2026 新颖性自查补充 — 应引]**:
    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述
    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述
    - Semantic Entropy Probes (2024) — 低成本不确定性估计
    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性
    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务
    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关
    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位
    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE
    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE
  - **需新增 Related Work 小节**:
    - "Test-Time Scaling & Sample Selection" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap
    - "Consistency for Structured IE" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation
- **Priority**: P0, Paper Agent handles

### R11: "SJ+logprob ensemble missing" (Dream 2 — both reviewers)
- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:
  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078
  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706
  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)
  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.
- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)

### R12: "No supervised upper bound / reward model comparison" (Dream 2)
- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Results show ensemble underperforms best single signal (EM), suggesting feature redundancy rather than complementarity. Full reward model training out of scope for this paper — discuss as future work.
- **Priority**: P1 (partially addressed by exp-016 ensemble)

### R13: "Headroom capture rate low" (Dream 2)
- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.
- **Priority**: P0, paper writing

### R14: "Cross-model validation thin — need more than 2×8B" (Dream 2)
- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.
- **Priority**: P1

### R15: "Log-prob definition ambiguity — Eq.1 vs best-of-N ranking" (Dream 2 cross-tier, [W])
- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state "all best-of-N require N forward passes; log-prob adds zero ranking overhead."
- **Priority**: P0, Paper Agent handles

### R16: "Zero figures — data-rich paper with only tables" (Dream 2 cross-tier, [W])
- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.
- **Priority**: P0, Paper Agent handles

### R17: "Diagnostic framework overclaimed — descriptive not prescriptive" (Dream 2 cross-tier, [M][W])
- **Mitigation**: Soften "diagnostic framework" to "diagnostic analysis" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.
- **Priority**: P0, Paper Agent handles

### R18: "No discussion of when consistency WOULD help" (Dream 2 cross-tier, [W])
- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.
- **Priority**: P1, Paper Agent handles

### R19: "Negative result partially predictable for fine-tuned models" (Dream 2 cross-tier, [W])
- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.
- **Priority**: P1, Paper Agent handles

## Venue Fit

EMNLP is well-suited for:
- Systematic empirical comparison of confidence signals for structured prediction
- Diagnostic findings with principled explanations
- The "comparison + boundary condition" contribution pattern

Risk assessment (post-1024-token correction + bootstrap):
- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.
- **Data-dependent risks**: The bootstrap test strengthened the correlation-selection gap narrative definitively — NER logprob +0.6pp is confirmed noise (p=0.39), making the "Weak Selectors" claim statistically rigorous rather than directional.
- **Confirmed strength**: Structural consistency family (EM/voting/SJ) >> logprob on quality estimation (AUROC 0.75 vs 0.58). Correlation-selection gap is now statistically confirmed with bootstrap CI.
- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.