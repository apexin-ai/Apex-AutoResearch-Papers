# Paper Framing — struct_self_consist_ie

> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。

## Target Venue
- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)
- Deadline: ARR May cycle, 2026-05-25

## Core Claims (4 layers, D112 updated — Main Conference framing with capability trap + degeneracy)

### Claim 1 (PRIMARY — Diagnosing Two Failure Mechanisms + Capability Trap)
Confidence signals reliably predict output quality across instances (AUROC up to 0.82, ρ up to 0.45) but universally fail to select better candidates from multiple samples. We diagnose **two failure mechanisms** and a unifying **capability trap** that explains why the gap is structurally inevitable for capable models.

**Three-layer argument + Capability Trap**:
- Layer A (design property, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification — the "methodological premise" — not an empirical finding.
- Layer B (empirical — instance degeneracy): 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom. Within-instance ρ=0.524 (SciERC) and 0.994 (CoNLL) — signals ARE correlated within instances, but degeneracy makes this irrelevant. Non-degenerate instances show MBR closing 23-41% of oracle gap. T=0 greedy dominates all signals (greedy F1=0.663 > best LP selection 0.647 on SciERC) — zero-cost strongest argument.
- Layer C (empirical — LP compression): Logprob — the only per-sample signal — fails due to intrinsic score compression (median within-instance LP range = 0.041 nats). Entity-token LP shows 4× variance but WORSE selection (-2.0pp). Free-form ablation confirms compression is model/task intrinsic (std ratio 0.97).
- **Capability Trap** (unifying insight, D111): Model capability → output convergence → instance degeneracy → vanishing selection headroom. Evidence: CoNLL (91% F1) → 58% degeneracy, SciERC (66% F1) → 21%, WNUT (48% F1) → ~0%. Scale dimension: 8B → 21% degen vs 4B → 10.4% on SciERC. This is NOT an "artifact" — it is a **consequence of capability**, a structural inevitability. The better the model, the less test-time scaling can help via unsupervised selection.

**Distinction from MBR literature**: Eikema et al.'s MBR failure = utility function misalignment. Our failure = utility IS aligned (within-instance ρ=0.524) but headroom eliminated by degeneracy — qualitatively novel mechanism.

**Key evidence (score compression)**:
- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39
- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp
- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it

**Key evidence (free-form ablation)** [DONE — exp_freeform_ablation, NEGATIVE]:
- LP distribution: constrained std=0.0206, free-form std=0.0199 (ratio 0.97, virtually unchanged)
- Tied fraction: 59.7% → 57.7% (-2.0pp, negligible)
- NER selection: +0.59pp → +0.18pp (both negligible vs greedy)
- RE selection: -0.68pp → +1.69pp (flipped positive — secondary finding)
- NER VC rho: 0.379 → 0.409 (slight QE improvement, selection still fails)
- Parse rate: 99.95% (fine-tuned model retains JSON format without grammar)
- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.

**Key evidence (scale ablation)** [DONE — 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}]:
- CoNLL NER: 4B greedy_f1=0.9234 (>8B 0.9123, +1.11pp), SJ_ρ=0.4217 (≈8B 0.4357, −1.4pp), FK_ρ=0.4181 (>8B 0.3998, +1.83pp)
- SciERC NER: 4B SJ_ρ=0.4221 (>8B 0.3825, +3.96pp), FK_ρ=0.3258 (>8B 0.2590, +6.68pp)
- SciERC RE: 4B SJ_ρ=0.2673 (>8B 0.2441, +2.32pp), FK_ρ=0.3593 (>8B 0.2782, +8.11pp); struct>surface ✗ at both scales
- **Conclusion**: Correlation strength maintained or improved at 4B across all 4 cells. The gap originates from within-instance signal misalignment, not model capacity. Task difficulty (SciERC RE zero-F1 rate) remains the primary driver, consistent across scales.
- CoNLL 4B headroom: 1.70pp (vs 8B 4.20pp) → MARGINAL for selection power, but QE correlations robust
- SciERC RE 4B: 47.6% zero-F1, RE LP_ρ_cond=0.1135 (p=0.074, n.s.) → confirms binary dominance at 4B
- **4B selection results** (correlation-selection gap at 4B):
  - CoNLL NER 4B (n=2756): SJ +0.07pp, FK +0.03pp, LP +0.09pp vs greedy 0.9213. All ≤0.1pp — MARGINAL (headroom 1.70pp)
  - SciERC NER 4B (n=529): SJ **-1.49pp**, FK -1.56pp, LP -2.23pp vs greedy 0.6622. Oracle 0.7925 (+13.02pp). **All signals WORSE than greedy despite 13pp oracle headroom — gap confirmed at 4B**
  - SciERC NER 4B gap demonstration: SJ-FK ρ gap = +0.096 (strong correlation advantage), SJ-FK selection F1 gap = +0.0007 (zero selection advantage) → correlation-selection gap quantified at 4B
- **n_samples confound control**: Qwen3-8B n=8 data exists as control. CoNLL SJ: n8 ρ=0.4389 → n16 ρ=0.4496 (Δ=0.011, CI crosses zero). SciERC SJ: n8→n16 Δ=0.066, CI=[0.004, 0.128] weak effect. n_samples not a confound for 4B-8B comparison.
- **Paper framing**: "Scale ablation shows the gap is not an artifact of a particular model size; correlation strength is maintained at 4B, confirming that the gap originates from within-instance signal misalignment rather than model capacity."

**exp-019 supervised verifier**: SKIPPED (Reviewer recommendation). Reasons: DDL 10 days, scope creep risk (analytical paper + solution = type mismatch), exp-016 LR ensemble already underperforms EM (0.666 vs 0.749). Verifier is follow-up paper material.

**Bonus finding (parse rate)**: Free-form parse rate 99.95% (4406/4408) — fine-tuned 8B model generates valid JSON without grammar constraints. Challenges intro:19 claim about constrained decoding necessity for format compliance.

**Implications**: Not just "signals don't work" but "here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation via elimination), and here's the forward direction (breaking LP compression requires fundamentally different approaches — trained verifiers, multi-round refinement — not simply relaxing decoding constraints)."

### Claim 2 (METHODOLOGY — QE Evaluation Framework)
Systematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.

**Key results**:
- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205). 3-seed consistent: SJ > FK delta=0.093~0.122
- RE (3-seed confirmed): **LP > SJ > FK** (mean ρ: LP 0.302, SJ 0.265, FK 0.254). Signal ranking reverses vs NER — structural signals lose advantage when 43-45% of RE samples have F1=0 (binary signal dominance). LP's coarse but stable generation-confidence signal captures "did the model get any relations right" better than structural overlap measures.
- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)
- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09. T=0.7: LP full ρ improves 0.205→0.249, LP cond ρ 0.154→0.185; FK 0.267→0.289 despite more compression → concentrated signal hypothesis (non-tied instances at lower T carry more informative variance). **Paper citation rule**: robustness/temperature tables use full ρ; score compression analysis uses cond ρ. Always annotate which variant.
- **Task-dependent signal effectiveness** (new finding from RE 3-seed): The optimal signal family depends on task structure. NER (token-level, graded F1) → structural agreement captures quality gradients. RE (relation-level, binary-dominated F1) → logprob captures generation confidence better. This is NOT a weakness — it's a nuanced finding that enriches the diagnostic framework.

**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):
- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578
- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601
- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706

### Claim 2b (Selection evidence)
**exp_016_rerun_1024 evidence** (SciERC 8B, N=8, T=1.0):
- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)
- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)

**4B selection evidence** (N=8, T=1.0):
- CoNLL NER 4B (n=2756): greedy 0.9213, SJ 0.9220 (+0.07pp), FK 0.9215, LP 0.9221 (+0.09pp), oracle 0.9382. Headroom 1.70pp → selection indistinguishable
- SciERC NER 4B (n=529): greedy 0.6622, SJ 0.6473 (-1.49pp), FK 0.6466 (-1.56pp), LP 0.6399 (-2.23pp), oracle 0.7925 (+13.02pp). **All signals worse than greedy** → correlation-selection gap at 4B confirmed

**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):
- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39
- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466

### Claim 3 (Diagnostic — task-complexity boundary + task-dependent signal effectiveness)
The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.

**RE 3-seed mechanism** (D073, confirmed at 4B): 43-47% of RE samples have F1=0 (8B: 43-45%, 4B: 47.6%), creating binary-dominated signal distributions where structural overlap (SJ/FK) cannot differentiate quality gradients. Pattern consistent across model scales — confirming task difficulty, not model capacity, drives this boundary. LP's generation confidence captures "complete failure vs partial success" more reliably. 3-seed RE QE: LP ρ=0.302 > SJ 0.265 > FK 0.254. **Definitive binary dominance evidence**: RE LP full ρ=0.266 but cond ρ=0.011 (p=0.86, completely n.s.) — LP's entire RE signal comes from the zero/nonzero F1 split; once conditioned on samples where the model extracts at least one relation, LP has zero predictive power for RE quality gradients. In contrast, NER LP cond ρ remains informative (0.154–0.185). This provides the concrete mechanism for Claim 3's task-complexity boundary: it's not just "compound error" in the abstract — it's specifically the high zero-F1 rate that shifts the optimal signal family from structural to probabilistic, and LP's RE advantage is entirely a binary classification effect, not genuine quality estimation.

**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.

**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.

**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):
- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10
- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392
- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.
- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.

## Story Spine (D112 — Two Failure Mechanisms + Capability Trap, Main Conference)

**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?

**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) present a fundamentally different challenge — and prior work conflates quality estimation with selection. Eikema et al.'s MBR failure stems from utility misalignment; our work reveals a qualitatively novel failure mode.

**Our framing (D112 — "two failure mechanisms + capability trap")**:

We systematically compare five confidence signals for IE and diagnose **why** unsupervised selection universally fails:
1. **Methodological premise**: Four of five signals are instance-level by construction and cannot rank candidates — a definitional property, not discovered empirically.
2. **Failure Mechanism 1 — Instance Degeneracy**: 21-58% of instances produce identical F1 across all N samples. Within-instance signals ARE correlated (ρ=0.524) but degeneracy eliminates headroom. Non-degenerate subset: MBR closes 23-41% of oracle gap. T=0 greedy dominates all signals (0.663 > 0.647 best LP) — zero additional inference cost.
3. **Failure Mechanism 2 — LP Compression**: Logprob's within-instance range is compressed (median 0.041 nats). Entity-token LP shows 4× variance but produces WORSE selection (-2.0pp). Free-form decoding ablation confirms compression is intrinsic (std ratio 0.97), not caused by constrained decoding.
4. **Capability Trap** (unifying): Model capability → convergence → degeneracy → vanishing headroom. CoNLL (91% F1) → 58% degen, SciERC (66%) → 21%, WNUT (48%) → ~0%. Scale: 8B 21% vs 4B 10.4%. The better the model, the less test-time scaling helps — a structural inevitability, not an artifact.
5. **Path forward**: Breaking the capability trap requires fundamentally different approaches (trained verifiers, multi-round refinement). The non-tied subset (+2.9pp, p=0.01) proves LP selection works WHERE degeneracy is absent.

**Headline**: "We diagnose why confidence signals that reliably predict structured IE output quality (AUROC 0.82, ρ 0.45) universally fail to select better candidates. Two mechanisms — instance degeneracy and logprob compression — are unified by a capability trap: the better the model, the more outputs converge, eliminating selection headroom. T=0 greedy dominates all multi-sample strategies at zero cost."

**Title**: "Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction"

## Anticipated Reviewer Concerns

### R1: "Only one NER dataset — generalization unclear"
- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.
- **Priority**: P0

### R2: "Only one model family (Qwen3-8B)"
- **Mitigation**: LLaMA-3.1-8B shows model-agnostic effect. ⚠️ **exp-007 数据被污染 (test data leakage)**，LLaMA SciERC 正确值来自 exp_018 (clean rerun)。unified_rho_full.json 的 LLaMA SciERC 条目必须替换为 exp_018 数据。正确 LLaMA SciERC N=8 3-seed mean: SJ 0.325, FK 0.256, VC 0.384, EM 0.279, LP 0.162。
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
- **Mitigation**: exp-016 LR ensemble (5-signal, 5-fold CV) underperforms best single signal EM (AUROC 0.666 vs 0.749), suggesting feature redundancy. exp-019 supervised verifier SKIPPED (DDL risk + scope creep). Free-form ablation provides the "so what": gap is fundamental → closing it requires fundamentally different approaches (trained verifiers, not just better unsupervised signals). Positioned as future work with explicit motivation from ablation evidence.
- **Priority**: P1, addressed via framing (future work motivated by ablation)

### R13: "Headroom capture rate low" (Dream 2)
- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.
- **Priority**: P0, paper writing

### R14: "Cross-model validation thin — need more than 2×8B" (Dream 2)
- **Status**: ✅ RESOLVED by 4B scale ablation. 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}. All correlation metrics maintained or improved at 4B (e.g. SciERC NER SJ_ρ: 0.3825→0.4221, +3.96pp). Combined with LLaMA-3.1-8B cross-architecture data, now have 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B). 70B infeasible — acknowledge as limitation.
- **Priority**: P0, RESOLVED

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

EMNLP **Main Conference** target. Strengths:
- Systematic empirical comparison with mechanistic diagnosis (not just "signals don't work" but "here's exactly why")
- Two novel failure mechanisms (instance degeneracy + LP compression) + unifying capability trap insight
- Controlled ablation (free-form decoding) providing causal evidence
- Cross-model (Qwen3-8B/4B + LLaMA-3.1-8B), cross-dataset (SciERC + CoNLL + WNUT), cross-task (NER + RE) validation

Main Conference gap vs Findings:
- **Need**: 3rd NER dataset (Few-NERD) to close "only 2 NER datasets" concern
- **Need**: 3rd seed for Fisher p-value power on key claims
- **Need**: LoRA rank=8 ablation to confirm fine-tuning degree doesn't drive degeneracy
- **Need**: Systematic claim audit resolving numerical contradictions

Risk assessment:
- **Strongest asset**: Capability trap is a genuinely novel insight — no prior work connects model capability to vanishing TTS headroom via degeneracy
- **Weakest flank**: Dataset breadth (2 NER + 1 RE → 3 NER + 1 RE with Few-NERD)
- **Critical path**: Few-NERD + 3rd seed experiments must complete before DDL (2026-05-25, 9 days)