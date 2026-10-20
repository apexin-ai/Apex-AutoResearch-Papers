# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Free-form 恢复 logprob variance 但 selection 提升有限；constrained decoding 是贡献因素之

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f7d328ac-c8f8-46fa-b26a-24551092ee89.jsonl`
- **Structured JSON:** [`e627d45306ad1b5eda70.json`](../../sessions/e6/e627d45306ad1b5eda70.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T09:36:21.572Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T09:36:21.572Z",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Free-form 恢复 logprob variance 但 selection 提升有限；constrained decoding 是贡献因素之一但非唯一瓶颈\n核心假设：['exp-018: logprob within-sample variance 有 2-4x 提升（range 中位数 0.10-0.20），方向正确但非压倒性', 'exp-018: free-form logprob selection 优于 greedy +1~3pp，但统计显著性边缘（p=0.05-0.15）', 'parse rate 75-90%，可用样本量较 constrained 减少 10-25%', 'NER 上方向清晰，RE 上 free-form 改善不明显（RE 的 bottleneck 可能多源）', '存在 confound：free-form 输出的 parsing noise 引入额外误差']\n关键指标范围：{'freeform_parse_rate': [0.75, 0.9], 'freeform_logprob_within_sample_range_median': [0.1, 0.2], 'freeform_logprob_rho_with_f1': [0.25, 0.35], 'freeform_logprob_selection_delta_vs_greedy_pp': [1.0, 3.0], 'freeform_logprob_selection_p_value': [0.05, 0.15], 'freeform_logprob_auroc': [0.6, 0.65], 'constrained_logprob_rho_with_f1': [0.2, 0.21], 'constrained_logprob_auroc': [0.57, 0.58], 'expected_reviewer_score': [3.0, 3.5], 'findings_acceptance_prob': [0.3, 0.5]}\n叙事方向：需将 \"experimentally verify\" 软化为 \"provide evidence consistent with\"。 Claim 1 从 \"constrained decoding IS the bottleneck\" 调整为 \"constrained decoding CONTRIBUTES TO the bottleneck, as evidenced by partial recovery of logprob discrimination under free-form generation\"。 补充讨论：score compression 是必要条件但非充分条件，IE 输出的组合复杂性 (entity set 的高维离散空间) 是独立于 decoding regime 的额外困难。 论文贡献权重重新分配：Claim 2 (QE framework, AUROC 0.75) 升级为 co-primary contribution， 与 Claim 1 (partial bottleneck diagnosis) 并列。 Title 调整为 \"Confidence Signals Predict but Cannot Select in Constrained-Decoding Information Extraction\"（去掉 \"Bottleneck\" 的因果暗示）。 需要额外补充 exp-019 simple verifier 或 non-tied subset 扩展分析来充实论文。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: struct_self_consist_ie\nvenue: EMNLP 2026 Findings\nfocus: Paper has been reframed from \"systematic comparison + negative finding\" to \"identifying, diagnosing, and experimentally verifying a regime-specific selection bottleneck caused by constrained decoding\". The breakthrough experiment is free-form decoding ablation (exp-018) that proves score compression is the mechanism. Evaluate whether this reframing + new experiment breaks through the 3.0/5 plateau to 3.5+. Key question: does the constrained decoding bottleneck story have enough intellectual depth for Findings acceptance?\n\n## paper_framing.md\n\n# Paper Framing — struct_self_consist_ie\n\n> Updated 2026-05-15 — D070 REFRAMING: from \"gap finding\" to \"regime-specific bottleneck identification with controlled ablation\". Motivated by 6-round 3.0/5 plateau — Reviewer diagnosis: content ceiling, not framing ceiling. Adding free-form decoding ablation as breakthrough experiment.\n\n## Target Venue\n- Primary: EMNLP 2026 Findings (via ARR May 2026)\n- Deadline: ARR May cycle, 2026-05-25\n\n## Core Claims (3 条, D070 重排)\n\n### Claim 1 (PRIMARY — Regime-Specific Selection Bottleneck)\nThe correlation-selection gap in structured IE is **caused by constrained decoding**. Under constrained decoding (Outlines/grammar-guided), logprob score compression makes per-sample ranking impossible: 60% of instances have within-sample logprob range < 0.05. Controlled ablation via free-form generation confirms the mechanism: removing constrained decoding recovers logprob variance and selection ability.\n\n**Two-layer argument**:\n- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.\n- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to score compression under constrained decoding. (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation**: removing constrained decoding recovers logprob discrimination → proves compression is the bottleneck, not an inherent IE limitation.\n\n**Key evidence (constrained)**:\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39\n- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp\n- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it under constrained decoding\n\n**Key evidence (free-form ablation)** [PLANNED — exp_freeform_ablation]:\n- Hypothesis: Free-form generation on SciERC will show (a) wider logprob variance, (b) improved logprob selection performance\n- If confirmed: gap is regime-specific → constrained decoding is the bottleneck\n- If not: gap is inherent to structured IE → stronger universal finding\n\n**Implications**: Not just \"signals don't work\" but \"here's WHY and WHEN they don't work, and here's a path forward\" (relaxed decoding + post-hoc filtering, or use logprob on non-tied subset).\n\n### Claim 2 (METHODOLOGY — QE Evaluation Framework)\nSystematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.\n\n**Key results**:\n- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205)\n- RE (preliminary, single benchmark): voting_conf leads both full and conditional\n- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)\n- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09\n\n**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):\n- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578\n- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601\n- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706\n\n### Claim 2b (Selection evidence)\n**exp_016_rerun_1024 evidence** (SciERC, N=8, T=1.0):\n- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)\n- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)\n\n**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):\n- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39\n- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466\n\n### Claim 3 (Diagnostic — task-complexity boundary)\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\n\n**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\n\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\n\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\n\n## Story Spine (D070 REFRAMED)\n\n**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?\n\n**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) under constrained decoding present a fundamentally different challenge — and prior work conflates quality estimation with selection.\n\n**Our framing (D070 reposition — from \"finding a gap\" to \"identifying and verifying a bottleneck\")**:\n\nWe systematically compare five confidence signals for IE under constrained decoding, and discover a **regime-specific selection bottleneck**:\n1. **Conceptual clarification**: Four of five signals are instance-level by construction and cannot rank candidates — this is noted as a definitional property, not discovered empirically. The interesting question is whether the remaining strategies (logprob, MBR/consensus-proximity) can select.\n2. **Core empirical finding**: Logprob — the only per-sample signal — fails due to score compression under constrained decoding (60% of instances have within-sample range < 0.05). Consensus-proximity/MBR also fails despite success in MT.\n3. **Controlled verification**: Free-form decoding ablation confirms the mechanism — removing constrained decoding recovers logprob's discriminative power. The gap is regime-specific, not inherent to structured IE.\n4. **Practical pathway**: Non-tied instances (+2.9pp, p=0.01) show logprob works when compression is absent → actionable mitigation via relaxed decoding or non-tied subset selection.\n\n**Headline**: \"We identify, diagnose, and experimentally verify a regime-specific selection bottleneck in constrained-decoding IE: confidence signals that reliably predict output quality (AUROC 0.75) cannot select better candidates because constrained decoding compresses log-probability scores. A controlled free-form ablation confirms the mechanism and points to relaxed decoding as a mitigation path.\"\n\n**Potential title**: \"The Constrained Decoding Bottleneck: Why Confidence Signals Predict but Cannot Select in Information Extraction\"\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only one NER dataset — generalization unclear\"\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\n- **Priority**: P0\n\n### R2: \"Only one model family (Qwen3-8B)\"\n- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect\n- **Priority**: P0\n\n### R3: \"FK is a strawman baseline — what about log-prob, USC, exact-match?\"\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).\n- **Priority**: P0, RESOLVED — results decisive\n\n### R3b: \"EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?\"\n- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.\n- **Priority**: P1 — narrative adjusted for 1024-token results\n\n### R4: \"No actual TTS improvement demonstrated\"\n- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.\n- **Mitigation**: Paper PIVOTS to \"confidence estimation + correlation-selection gap analysis.\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\n- **Priority**: P0 — narrative pivot complete, bootstrap confirms\n\n### R5: \"Sample size N=8 may be too small for reliable SJ estimation\"\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\n- **Priority**: P0\n\n### R6: \"Conditional analysis cherry-picks favorable instances\"\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\n- **Priority**: P0 (add sensitivity analysis)\n\n### R7: \"Only ρ as evaluation metric\"\n- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).\n- **Priority**: P0\n\n### R8: \"Formula-implementation discrepancy\"\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\n- **Priority**: P0, paper writing fix\n\n### R9: \"Evaluation circularity (T>0 consistency vs T=0 F1)\"\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\n- **Priority**: P0\n\n### R10: \"Insufficient related work\" (三档一致 [B][M][W])\n- **Mitigation**: Expand to 35+ references. Must cite:\n  - USC (Chen 2024) — empirical differentiation, not just citation\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\n  - **IE confidence**: Culotta & McCallum 2004\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\n  - **[2025-2026 新颖性自查补充 — 必引]**:\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\"overlooks semantically consistent outputs\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\n  - **[2025-2026 新颖性自查补充 — 应引]**:\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\n  - **需新增 Related Work 小节**:\n    - \"Test-Time Scaling & Sample Selection\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\n    - \"Consistency for Structured IE\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\n- **Priority**: P0, Paper Agent handles\n\n### R11: \"SJ+logprob ensemble missing\" (Dream 2 — both reviewers)\n- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:\n  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078\n  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706\n  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)\n  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.\n- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)\n\n### R12: \"No supervised upper bound / reward model comparison\" (Dream 2)\n- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Results show ensemble underperforms best single signal (EM), suggesting feature redundancy rather than complementarity. Full reward model training out of scope for this paper — discuss as future work.\n- **Priority**: P1 (partially addressed by exp-016 ensemble)\n\n### R13: \"Headroom capture rate low\" (Dream 2)\n- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.\n- **Priority**: P0, paper writing\n\n### R14: \"Cross-model validation thin — need more than 2×8B\" (Dream 2)\n- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.\n- **Priority**: P1\n\n### R15: \"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\"\n- **Priority**: P0, Paper Agent handles\n\n### R16: \"Zero figures — data-rich paper with only tables\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\n- **Priority**: P0, Paper Agent handles\n\n### R17: \"Diagnostic framework overclaimed — descriptive not prescriptive\" (Dream 2 cross-tier, [M][W])\n- **Mitigation**: Soften \"diagnostic framework\" to \"diagnostic analysis\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\n- **Priority**: P0, Paper Agent handles\n\n### R18: \"No discussion of when consistency WOULD help\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\n- **Priority**: P1, Paper Agent handles\n\n### R19: \"Negative result partially predictable for fine-tuned models\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\n- **Priority**: P1, Paper Agent handles\n\n## Venue Fit\n\nEMNLP is well-suited for:\n- Systematic empirical comparison of confidence signals for structured prediction\n- Diagnostic findings with principled explanations\n- The \"comparison + boundary condition\" contribution pattern\n\nRisk assessment (post-1024-token correction + bootstrap):\n- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.\n- **Data-dependent risks**: The bootstrap test strengthened the correlation-selection gap narrative definitively — NER logprob +0.6pp is confirmed noise (p=0.39), making the \"Weak Selectors\" claim statistically rigorous rather than directional.\n- **Confirmed strength**: Structural consistency family (EM/voting/SJ) >> logprob on quality estimation (AUROC 0.75 vs 0.58). Correlation-selection gap is now statistically confirmed with bootstrap CI.\n- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.\n\n## experiment_plan (with registry status)\n\n- id: exp-012\n  name: baseline_logprob\n  claim: 1\n  description: 'Compute sequence log-probability for all existing pilot samples (SciERC\n    NER+RE) and new dataset pilots. Correlate log-prob with F1 (ρ, AUROC, τ). If SJ\n    does NOT beat log-prob, the 16x inference cost is unjustified and paper contribution\n    weakens drastically. THIS IS THE MAKE-OR-BREAK EXPERIMENT.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  note: 'Needs vLLM forward pass to extract log-probs from existing samples. ~1h per\n    dataset on 1 GPU. For new datasets, capture log-probs during pilot inference.\n    Also compute on pilot_004/005 existing data if log-probs weren''t saved.\n\n    '\n  registry_id: exp_012_logprob_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho_sj: 0.3565\n    ner_full_rho_fk: 0.2651\n    ner_full_rho_logprob: 0.1396\n    ner_full_rho_greedy_logprob: 0.1615\n    ner_full_tau_sj: 0.2658\n    ner_full_tau_logprob: 0.1006\n    ner_full_auroc_sj: 0.6892\n    ner_full_auroc_fk: 0.6292\n    ner_full_auroc_logprob: 0.5907\n    ner_full_n: 529\n    ner_sj_vs_logprob_delta: 0.2169\n    re_full_rho_sj: 0.2112\n    re_full_rho_fk: 0.2528\n    re_full_rho_logprob: 0.2467\n    re_full_auroc_sj: 0.5916\n    re_full_auroc_fk: 0.6262\n    re_full_auroc_logprob: 0.6186\n    re_full_n: 397\n    re_cond_rho_sj: 0.3683\n    re_cond_rho_fk: 0.3168\n    re_cond_rho_logprob: 0.1457\n    re_cond_auroc_sj: 0.6839\n    re_cond_auroc_logprob: 0.5487\n    re_cond_n: 296\n    diagnosis: 'NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead.\n      RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.'\n- id: exp-013\n  name: baseline_exact_match\n  claim: 1\n  description: 'Exact-match voting rate: what fraction of N samples produce identical\n    entity/relation sets? Correlate with F1. This is the direct analogue of Wang et\n    al.''s original self-consistency for structured outputs.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU-only on existing pilot data. Zero cost.\n  registry_id: exp_013_exact_match_voting\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_full_rho: 0.2941\n    ner_full_p: 5.12e-12\n    ner_full_tau: 0.2181\n    ner_full_auroc: 0.6398\n    re_full_rho: 0.1562\n    re_full_p: 0.0018\n    re_full_tau: 0.1185\n    re_full_auroc: 0.5863\n    diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\n- id: exp-014\n  name: baseline_entity_voting\n  claim: 1\n  description: 'Entity-level majority voting: for each entity, count how many of N\n    samples include it. Select entities above threshold. Compare F1 of entity-voting\n    selection vs SJ selection vs FK selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU-only on existing pilot data. Zero cost.\n  registry_id: exp_014_entity_majority_voting\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho: 0.3915\n    ner_full_p: 8.1e-21\n    ner_full_tau: 0.2906\n    ner_full_auroc: 0.7039\n    re_full_rho: 0.3403\n    re_full_p: 3.21e-12\n    re_full_tau: 0.256\n    re_full_auroc: 0.6668\n    ner_voting_f1: 0.6246\n    ner_greedy_f1: 0.6483\n    ner_oracle_f1: 0.7793\n    re_voting_f1: 0.3577\n    re_greedy_f1: 0.4022\n    re_oracle_f1: 0.5886\n    diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE\n      (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\n- id: exp-015\n  name: evaluation_metrics_expansion\n  claim: 1\n  description: 'Add AUROC (binary: good/bad output at threshold), calibration plots,\n    and Kendall''s τ alongside Spearman ρ for ALL confidence signals (SJ, FK, log-prob,\n    exact-match, entity-voting) on ALL datasets. Also add leave-one-out SJ as robustness\n    check for evaluation circularity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  - exp-013\n  - exp-014\n  note: CPU-only analysis. Addresses Dream concerns D5 (single metric) and D17 (circularity).\n  registry_id: exp_015_metrics_expansion\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_012_logprob/samples_with_logprobs.jsonl\n    config: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\n    ner:\n      n_valid: 529\n      n_cond: 501\n      voting_rho_full: 0.5018\n      voting_rho_cond: 0.4497\n      voting_auroc: 0.7279\n      voting_tau: 0.3766\n      sj_rho_full: 0.3565\n      sj_rho_cond: 0.412\n      sj_auroc: 0.6656\n      sj_tau: 0.2658\n      em_rho_full: 0.2566\n      em_rho_cond: 0.3427\n      em_auroc: 0.623\n      em_tau: 0.1924\n      fk_rho_full: 0.2651\n      fk_rho_cond: 0.306\n      fk_auroc: 0.6243\n      fk_tau: 0.2027\n      logprob_rho_full: 0.1396\n      logprob_rho_cond: 0.1627\n      logprob_auroc: 0.5585\n      logprob_tau: 0.1006\n    re:\n      n_valid: 397\n      n_cond: 296\n      voting_rho_full: 0.4217\n      voting_rho_cond: 0.463\n      voting_auroc: 0.7162\n      voting_tau: 0.327\n      sj_rho_full: 0.2112\n      sj_rho_cond: 0.3683\n      sj_auroc: 0.5816\n      sj_tau: 0.1619\n      em_rho_full: 0.1002\n      em_rho_cond: 0.3607\n      em_auroc: 0.5036\n      em_tau: 0.0839\n      fk_rho_full: 0.2528\n      fk_rho_cond: 0.3168\n      fk_auroc: 0.6308\n      fk_tau: 0.1967\n      logprob_rho_full: 0.2467\n      logprob_rho_cond: 0.1457\n      logprob_auroc: 0.6354\n      logprob_tau: 0.1808\n    diagnosis: 'Unified 5-signal evaluation on single data source. Voting leads NER\n      full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals\n      beat logprob on NER. RE: voting leads both full and cond.'\n- id: exp-001\n  name: ner_n16_scierc\n  claim: 1\n  description: 'NER N=16 on SciERC (ft_002_v2 model). Strengthen rho estimation, test\n    N-scaling. Run with seeds [42, 123, 456] for robustness. MUST capture log-probs\n    during inference for exp-012.\n\n    '\n  priority: P0\n  gpu_budget_hours: 18\n  deps: []\n  dataset: SciERC\n  model: ft_002_v2\n  note: 3 seeds × 6h each. Inference script MUST output log-probs.\n  registry_id: exp_001_ner_n16_scierc\n  status: DONE\n  conclusion: success\n  metrics:\n    n_instances: 551\n    ner_n: 529\n    re_n: 397\n    N: 16\n    T: 1\n    seed: 42\n    full_test_set: true\n    ner_voting_conf_rho: 0.399\n    ner_sj_rho: 0.398\n    ner_em_rho: 0.339\n    ner_fk_rho: 0.288\n    ner_logprob_rho: 0.237\n    ner_voting_conf_auroc: 0.704\n    ner_sj_auroc: 0.697\n    ner_cond_em_rho: 0.414\n    ner_cond_sj_rho: 0.349\n    ner_cond_vc_rho: 0.34\n    re_voting_conf_rho: 0.38\n    re_logprob_rho: 0.293\n    re_fk_rho: 0.281\n    re_sj_rho: 0.277\n    re_em_rho: 0.148\n    re_voting_conf_auroc: 0.699\n    re_cond_em_rho: 0.475\n    re_cond_sj_rho: 0.318\n    re_cond_vc_rho: 0.35\n    re_cond_em_auroc: 0.742\n    diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380).\n      EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full\n      FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact of\n      200 instances + T=0.7.'\n- id: exp-002\n  name: ner_conll2003\n  claim: 1\n  description: 'Fine-tune Qwen3-8B on CoNLL-2003 (LoRA) + NER pilot (N=8, T=0.7).\n    Cross-dataset generalization. MUST capture log-probs. Use consistent N and T with\n    other datasets.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  dataset: CoNLL-2003\n  model: qwen3-8b (new fine-tune)\n  registry_id: exp_002_ner_conll2003\n  status: DONE\n  conclusion: success\n- id: exp-003\n  name: ner_wnut17\n  claim: 1\n  description: 'Fine-tune Qwen3-8B on WNUT-17 (LoRA) + NER pilot (N=8, T=0.7). Social\n    media domain — cross-dataset generalization. MUST capture log-probs.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps: []\n  dataset: WNUT-17\n  model: qwen3-8b (new fine-tune)\n  note: User confirmed public datasets only. D043/D045 abandoned — 54% F1=0, SJ rho\n    not significant. Provides Claim 3 negative evidence.\n  registry_id: exp_003_wnut17_v2_infer\n  status: orphaned\n- id: exp-004\n  name: re_diagnostic_analysis\n  claim: 2\n  description: 'Per-relation-type consistency breakdown on existing pilot_004/005\n    data. Error propagation patterns. Bootstrap CI for ALL rho comparisons. Add conditional\n    threshold sensitivity analysis (vary exclusion criterion). Compare ALL confidence\n    signals (SJ, FK, log-prob, exact-match) on RE.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  - exp-013\n  note: CPU-only. Bootstrap CI + threshold sensitivity address Dream concerns.\n  registry_id: exp_004_re_diagnostic\n  status: DONE\n  conclusion: success\n  metrics:\n    per_relation_type:\n      HYPONYM-OF:\n        n: 36\n        rho_sj: 0.545\n        rho_fk: 0.646\n        rho_vc: 0.628\n        mean_f1: 0.513\n      CONJUNCTION:\n        n: 86\n        rho_sj: 0.383\n        rho_fk: 0.35\n        rho_vc: 0.484\n        mean_f1: 0.48\n      USED-FOR:\n        n: 299\n        rho_sj: 0.236\n        rho_fk: 0.255\n        rho_vc: 0.286\n        mean_f1: 0.422\n      PART-OF:\n        n: 44\n        rho_sj: 0.239\n        rho_fk: 0.348\n        rho_vc: 0.283\n        mean_f1: 0.297\n      EVALUATE-FOR:\n        n: 62\n        rho_sj: 0.172\n        rho_fk: 0.255\n        rho_vc: 0.226\n        mean_f1: 0.365\n      COMPARE:\n        n: 35\n        rho_sj: 0.168\n        rho_fk: 0.184\n        rho_vc: 0.18\n        mean_f1: 0.453\n      FEATURE-OF:\n        n: 50\n        rho_sj: 0.004\n        rho_fk: 0.052\n        rho_vc: 0.014\n        mean_f1: 0.254\n    error_propagation:\n      total_fn: 553\n      tail_error_pct: 21.9\n      full_error_pct: 21.7\n      head_error_pct: 17.7\n      head_tail_error_pct: 15.9\n      type_error_pct: 8.3\n      worst_consistency: head_type_error (sj=0.411)\n      best_consistency: head_error (sj=0.613)\n    threshold_sensitivity:\n      thr_0.00_rho_sj: 0.3161\n      thr_0.00_rho_vc: 0.3841\n      thr_0.00_n: 313\n      thr_0.05_rho_sj: 0.2682\n      thr_0.05_rho_vc: 0.2364\n      thr_0.05_n: 239\n    bootstrap_ci_95:\n      ner_sj:\n      - 0.2946\n      - 0.4586\n      ner_voting_conf:\n      - 0.3048\n      - 0.4656\n      re_sj:\n      - 0.1422\n      - 0.3391\n      re_voting_conf:\n      - 0.1818\n      - 0.3721\n      re_cond_sj:\n      - 0.2161\n      - 0.4102\n      re_cond_voting_conf:\n      - 0.2825\n      - 0.474\n    fisher_z_ner_vs_re:\n      sj_z: 2.31\n      sj_p: 0.0209\n      sj_significant: true\n      fk_z: -0.31\n      fk_p: 0.756\n      fk_significant: false\n      voting_z: 1.914\n      voting_p: 0.0556\n      voting_significant: false\n    diagnosis: FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF\n      strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of\n      RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE\n      signal in conditional set (rho=0.384).\n- id: exp-005\n  name: temperature_sensitivity_analysis\n  claim: 2\n  description: 'T=0.7 vs T=1.0 comparison on both NER and RE for ALL confidence signals.\n    Signal-noise tradeoff analysis.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  note: CPU-only on existing pilot_004 (T=1.0) and pilot_005 (T=0.7) data.\n  registry_id: exp_005\n  status: DONE\n  conclusion: success\n- id: exp-006\n  name: adaptive_compute_demo\n  claim: 1\n  description: 'Best-of-N selection on NER: SJ vs log-prob vs FK vs exact-match vs\n    random vs greedy. Report on ALL NER datasets (not just SciERC). Include RE results\n    too (even if negative).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-012\n  note: CPU-only. Must cover all datasets and include RE for completeness.\n  registry_id: exp_006_v2\n  status: DONE\n  conclusion: negative\n  metrics:\n    NER_SciERC_s42:\n      greedy: 0.618\n      oracle: 0.787\n      SJ: 0.62\n      logprob: 0.621\n      FK: 0.621\n      EM: 0.606\n      voting_conf: 0.585\n      random: 0.586\n    NER_SciERC_s123:\n      greedy: 0.618\n      oracle: 0.785\n      SJ: 0.617\n      logprob: 0.618\n      FK: 0.621\n      EM: 0.613\n      voting_conf: 0.584\n      random: 0.583\n    NER_CoNLL:\n      greedy: 0.725\n      oracle: 0.757\n      SJ: 0.718\n      logprob: 0.716\n      FK: 0.717\n      EM: 0.716\n      voting_conf: 0.714\n      random: 0.692\n    RE_SciERC:\n      greedy: 0.403\n      oracle: 0.631\n      SJ: 0.397\n      logprob: 0.41\n      FK: 0.396\n      EM: 0.381\n      voting_conf: 0.408\n      random: 0.364\n- id: exp-007\n  name: ner_multi_model\n  claim: 1\n  description: 'NER pilot with LLaMA-3.1-8B-Instruct on SciERC. Model-agnostic validation.\n    MUST capture log-probs for baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps: []\n  dataset: SciERC\n  model: llama-3.1-8b (new fine-tune)\n  registry_id: exp_007_llama_inference\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.66\n      oracle_f1: 0.781\n      headroom: 0.121\n      rho_fk: 0.327\n      rho_sj: 0.363\n      rho_fk_cond: 0.226\n      rho_sj_cond: 0.311\n      rho_logprob: 0.183\n      rho_logprob_cond: 0.109\n      structural_beats_surface: true\n      sample_f1_pct_zero: 11.6\n    re:\n      greedy_f1: 0.434\n      oracle_f1: 0.568\n      headroom: 0.135\n      rho_fk: 0.305\n      rho_sj: 0.299\n      rho_fk_cond: 0.259\n      rho_sj_cond: 0.405\n      rho_logprob: 0.288\n      rho_logprob_cond: 0.092\n      structural_beats_surface: false\n      sample_f1_pct_zero: 41.2\n    n_instances: 551\n    N: 8\n    T: 1\n    seed: 42\n    model: LLaMA-3.1-8B-Instruct\n    verdict: FAIL\n    verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\n- id: exp-008\n  name: re_n16_confirmation\n  claim: 2\n  description: 'RE N=16 on SciERC to confirm negative finding with higher statistical\n    power.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps: []\n  dataset: SciERC\n  model: ft_002_v2\n  registry_id: exp_008_re_n16\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.6635\n      oracle_f1: 0.8208\n      headroom: 0.1572\n      rho_sj_full: 0.377\n      rho_fk_full: 0.2508\n      rho_logprob_full: 0.3153\n      rho_sj_cond: 0.3598\n      rho_fk_cond: 0.2251\n      rho_logprob_cond: 0.2927\n      sj_beats_fk: true\n      rho_advantage: 0.1262\n    re:\n      greedy_f1: 0.4339\n      oracle_f1: 0.6658\n      headroom: 0.2319\n      rho_sj_full: 0.2966\n      rho_fk_full: 0.2871\n      rho_logprob_full: 0.2986\n      rho_sj_cond: 0.3975\n      rho_fk_cond: 0.3774\n      rho_logprob_cond: 0.2745\n      sj_beats_fk: true\n      rho_advantage: 0.0095\n    verdict: FAIL\n- id: exp-009\n  name: capability_stratification\n  claim: 2\n  description: 'Stratify instances by difficulty (greedy F1 buckets + independent\n    proxies: sentence length, entity count) for both NER and RE. Verify inverted-U\n    pattern with proper statistical tests and independent stratification variable.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  note: CPU-only. Dream flagged inverted-U overclaiming — use independent proxy.\n  registry_id: exp_009_capability_stratification\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n: 551\n      sj_rho_overall: 0.398\n      by_greedy_f1:\n        hard_0_25_sj_rho: 0.159\n        med_low_sj_rho: 0.139\n        med_high_sj_rho: 0.09\n        easy_sj_rho: 0.23\n      by_sent_len:\n        Q1_sj_rho: 0.461\n        Q2_sj_rho: 0.401\n        Q3_sj_rho: 0.296\n        Q4_sj_rho: 0.382\n      by_ent_count:\n        0_sj_rho: 0.689\n        1_2_sj_rho: 0.415\n        3_5_sj_rho: 0.353\n        6plus_sj_rho: 0.547\n    scierc_re:\n      n: 551\n      by_greedy_f1:\n        hard_0_25_sj_rho: -0.043\n        easy_sj_rho: 0.21\n      by_sent_len:\n        Q1_sj_rho: 0.447\n        Q4_sj_rho: 0.54\n      by_rel_count:\n        0_sj_rho: 0.62\n        1_2_sj_rho: 0.275\n        6plus_sj_rho: 0.527\n    conll_ner:\n      n: 3453\n      by_sent_len:\n        Q1_sj_rho: 0.334\n        Q3_sj_rho: 0.518\n    proxy_independence:\n      scierc_ner_f1_vs_slen: -0.021\n      scierc_ner_f1_vs_ecnt: 0.007\n      scierc_re_f1_vs_slen: -0.147\n- id: exp-010\n  name: selection_curves\n  claim: 1\n  description: 'Best-of-N selection curves for N=1,2,4,8,16 comparing all confidence\n    signals. Visualize as line plots (not just tables — Dream flagged table-only presentation).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-012\n  note: CPU-only visualization\n  registry_id: exp_010_selection_curves\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n_instances: 551\n      greedy_f1: 0.618\n      N16:\n        oracle: 0.787\n        SJ: 0.62\n        FK: 0.621\n        logprob: 0.621\n        voting_conf: 0.585\n        EM: 0.606\n        random: 0.595\n      N8:\n        oracle: 0.752\n        SJ: 0.614\n        FK: 0.614\n        logprob: 0.619\n        voting_conf: 0.591\n        EM: 0.603\n        random: 0.589\n      N4:\n        oracle: 0.714\n        SJ: 0.607\n        FK: 0.608\n        logprob: 0.616\n        voting_conf: 0.594\n        EM: 0.6\n        random: 0.587\n    scierc_re:\n      n_instances: 397\n      greedy_f1: 0.403\n      N16:\n        oracle: 0.631\n        SJ: 0.397\n        FK: 0.396\n        logprob: 0.41\n        voting_conf: 0.408\n        EM: 0.381\n        random: 0.364\n      N8:\n        oracle: 0.583\n        SJ: 0.393\n        FK: 0.394\n        logprob: 0.413\n        voting_conf: 0.398\n        EM: 0.381\n        random: 0.363\n    conll_ner:\n      n_instances: 3453\n      greedy_f1: 0.725\n      N8:\n        oracle: 0.757\n        SJ: 0.718\n        FK: 0.717\n        logprob: 0.716\n        voting_conf: 0.714\n        EM: 0.716\n        random: 0.69\n      N4:\n        oracle: 0.746\n        SJ: 0.714\n        FK: 0.714\n        logprob: 0.715\n        voting_conf: 0.714\n        EM: 0.712\n        random: 0.692\n- id: exp-011\n  name: ner_ood_robustness\n  claim: 1\n  description: 'Test NER consistency signal on OOD instances (cross-domain transfer).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n- id: exp-016\n  name: signal_ensemble_analysis\n  claim: 1\n  description: 'SJ+logprob instance-level correlation and ensemble analysis. (1) Pearson/Spearman\n    correlation between SJ and logprob per-instance. (2) Grid search linear combination\n    alpha*SJ + (1-alpha)*logprob. (3) Logistic regression on all 5 signals as ensemble.\n    (4) Best-of-N selection F1 for ensemble vs individual signals. Dream 2 reviewers\n    BOTH independently flagged this as missing.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  - exp-014\n  note: CPU-only on existing pilot_004 data. Zero cost, high impact.\n  registry_id: exp_016_signal_ensemble\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_logprob_pearson_ner: 0.57\n    sj_logprob_pearson_re: 0.42\n    best_linear_ner:\n      combo: SJ+voting_conf\n      alpha: 0.3\n      rho: 0.489\n    best_linear_re:\n      combo: voting_conf+logprob\n      alpha: 0.6\n      rho: 0.429\n    ensemble_ner_auroc: 0.735\n    ensemble_re_auroc: 0.719\n    best_single_ner_auroc: 0.7\n    best_single_re_auroc: 0.721\n    ensemble_ner_delta: 0.035\n    selection_f1_ner:\n      greedy: 0.609\n      logprob: 0.609\n      sj: 0.604\n      ensemble: 0.604\n      voting: 0.596\n      random: 0.58\n      oracle: 0.769\n    selection_f1_re:\n      logprob: 0.397\n      greedy: 0.374\n      sj: 0.368\n      ensemble: 0.367\n      voting: 0.338\n      random: 0.338\n      oracle: 0.561\n    diagnosis: 'SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best\n      is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER.\n      Oracle gap still huge.'\n- id: exp-017\n  name: ner_llama_conll\n  claim: 1\n  description: 'LLaMA-3.1-8B on CoNLL-2003 to strengthen cross-model validation. Dream\n    2 flagged LLaMA only on SciERC is insufficient for model-agnostic claim.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-007\n  dataset: CoNLL-2003\n  model: llama-3.1-8b (fine-tune on CoNLL)\n  note: Only if exp-007 shows positive signal and GPU hours available.\n  status: planned\n- id: exp-018\n  name: freeform_decoding_ablation\n  claim: 1\n  description: 'BREAKTHROUGH EXPERIMENT (D070). Free-form decoding ablation on SciERC\n    NER+RE using Qwen3-8B. Remove Outlines constrained decoding, generate 8 free-form\n    samples per instance. Compare logprob variance, selection performance, and QE\n    metrics between constrained vs free-form. This is the controlled experiment that\n    proves whether the correlation-selection gap is caused by constrained decoding\n    (regime-specific) or inherent to structured IE (universal). If free-form recovers\n    logprob selection → paper becomes about regime-specific bottleneck (much stronger).\n    If gap persists → universal finding (also stronger).\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  dataset: SciERC\n  model: qwen3-8b (existing fine-tuned checkpoint)\n  note: '529 NER + 397 RE instances × 8 samples = ~4200 generations. 8B model on RTX\n    5090 ≈ 1-2h inference. Parse rate expected 80-95% (fine-tuned model learned JSON\n    format). Analysis on parseable subset. Key metrics: (a) logprob within-sample\n    variance (constrained vs free), (b) selection F1 (constrained vs free), (c) QE\n    ρ/AUROC (constrained vs free).\n\n    '\n  status: planned\n- id: exp-019\n  name: simple_verifier_baseline\n  claim: 1\n  description: 'P1 EXPERIMENT. Train a simple supervised verifier (DeBERTa or 8B classification\n    head) on existing (input, output, F1) data. If verifier partially closes the selection\n    gap, it proves the gap IS closable and transforms the negative finding into an\n    actionable one with an upper bound on unsupervised methods.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-018\n  dataset: SciERC\n  model: DeBERTa-v3-large or Qwen3-8B classifier\n  note: 'Only if exp-018 done and time permits before DDL. Training data: existing\n    N=8 samples with F1 labels. ~1 day implementation + training + evaluation.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: ft_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.1099\n    eval_loss: 0.0771\n    gate0_ner_f1_strict: 0.1143\n    gate0_re_f1_strict: 0.0125\n    gate0_ner_f1_text: 0.606\n    gate0_re_f1_text: 0.3392\n    gate0_offset_accuracy: 0.1665\n    gate0_parse_failures: 43\n    gate0_pass: false\n    gate0_realigned_ner_f1: 0.6045\n    gate0_realigned_re_f1: 0.338\n    gate0_realigned_entity_offset_accuracy: 1\n    gate0_realigned_relation_offset_accuracy: 1\n    gate0_realigned_ner_pass: true\n    gate0_realigned_re_pass: false\n    gate0_realigned_pass: false\n    gate0_ner_f1_delta_realign: 0.4901\n    gate0_re_f1_delta_realign: 0.3255\n    verdict_note: 'partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)'\n- exp_id: mvp_pilot_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.611\n    ner_oracle_f1: 0.78\n    ner_headroom: 0.169\n    ner_fleiss_kappa_mean: 0.2449\n    ner_soft_jaccard_mean: 0.5041\n    ner_full_rho_sj: 0.3616\n    ner_full_rho_fk: 0.3515\n    ner_full_n: 529\n    ner_cond_rho_sj: 0.3688\n    ner_cond_rho_fk: 0.3569\n    ner_cond_n: 510\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_sample_f1_pct_zero: 20.4\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 19\n    re_greedy_f1: 0.355\n    re_oracle_f1: 0.572\n    re_headroom: 0.217\n    re_fleiss_kappa_mean: 0.0681\n    re_soft_jaccard_mean: 0.3635\n    re_full_rho_sj: 0.2535\n    re_full_rho_fk: 0.2885\n    re_full_n: 397\n    re_cond_rho_sj: 0.3515\n    re_cond_rho_fk: 0.3107\n    re_cond_n: 320\n    re_sj_beats_fk_full: false\n    re_sj_beats_fk_cond: true\n    re_sample_f1_pct_zero: 58.3\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 77\n    parse_failures_stochastic: 164\n    parse_failures_greedy: 29\n    total_stochastic_samples: 4408\n    total_greedy: 551\n    verdict: FAIL\n    verdict_reason: RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\n- exp_id: ft_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    last_step: 70\n    total_steps: 585\n    progress_pct: 11.97\n    last_loss: 0.1134\n    last_lr: 0.00019982\n    elapsed: 3m32s\n    failure_reason: OOM at step 73, batch_size=4 too large for 32GB RTX 5090\n- exp_id: mvp_pilot_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_pilot_003\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.6362\n    ner_oracle_f1: 0.792\n    ner_headroom: 0.1559\n    ner_fleiss_kappa_mean: 0.2488\n    ner_soft_jaccard_mean: 0.5066\n    ner_full_rho_sj: 0.3808\n    ner_full_rho_fk: 0.3362\n    ner_full_p_sj: 1.07e-19\n    ner_full_p_fk: 1.93e-15\n    ner_full_n: 529\n    ner_cond_rho_sj: 0.3836\n    ner_cond_rho_fk: 0.3187\n    ner_cond_p_sj: 1.83e-19\n    ner_cond_p_fk: 1.33e-13\n    ner_cond_n: 514\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_rho_advantage: 0.0446\n    ner_sample_f1_mean: 0.5153\n    ner_sample_f1_std: 0.3334\n    ner_sample_f1_pct_zero: 19.9\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 15\n    re_greedy_f1: 0.3774\n    re_oracle_f1: 0.5939\n    re_headroom: 0.2165\n    re_fleiss_kappa_mean: 0.0879\n    re_soft_jaccard_mean: 0.3958\n    re_full_rho_sj: 0.2367\n    re_full_rho_fk: 0.2221\n    re_full_p_sj: 1.85e-06\n    re_full_p_fk: 7.92e-06\n    re_full_n: 397\n    re_cond_rho_sj: 0.3004\n    re_cond_rho_fk: 0.2374\n    re_cond_p_sj: 2.25e-08\n    re_cond_p_fk: 1.19e-05\n    re_cond_n: 333\n    re_sj_beats_fk_full: true\n    re_sj_beats_fk_cond: true\n    re_rho_advantage: 0.0146\n    re_sample_f1_mean: 0.1977\n    re_sample_f1_std: 0.3251\n    re_sample_f1_pct_zero: 67.6\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 64\n    parse_failures_stochastic: 0\n    parse_failures_greedy: 0\n    total_stochastic_samples: 4408\n    total_greedy: 551\n    verdict: FAIL\n    verdict_reason: RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but\n      below PASS bar\n- exp_id: ft_002_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch: 5\n    train_loss: 0.0806\n    eval_loss: 0.089\n    train_runtime: 28m41s\n    train_samples_per_second: 5.407\n    train_steps_per_second: 0.34\n    total_steps: 585\n    checkpoints:\n    - checkpoint-400\n    - checkpoint-500\n    - checkpoint-585\n    gate0_final_ner_f1: 0.6615\n    gate0_final_re_f1: 0.4177\n    gate0_final_parse_failures: 0\n    gate0_final_ner_pass: true\n    gate0_final_re_pass: true\n    gate0_final_pass: true\n    gate0_ckpt400_ner_f1: 0.6475\n    gate0_ckpt400_re_f1: 0.3793\n    gate0_ckpt400_parse_failures: 0\n    gate0_ckpt400_verdict: FAIL\n    gate0_ckpt400_re_sample_f1_pct_zero: 58.8\n    gate0_ckpt400_warning: '>30% samples F1=0'\n- exp_id: mvp_pilot_004\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.6671\n    ner_oracle_f1: 0.7756\n    ner_headroom: 0.1085\n    ner_fleiss_kappa_mean: 0.4048\n    ner_soft_jaccard_mean: 0.7008\n    ner_full_rho_fk: 0.259\n    ner_full_rho_sj: 0.3825\n    ner_full_n: 529\n    ner_cond_rho_fk: 0.2352\n    ner_cond_rho_sj: 0.3762\n    ner_cond_n: 508\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_sample_f1_mean: 0.6084\n    ner_sample_f1_std: 0.3174\n    ner_sample_f1_pct_zero: 12.19\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 21\n    re_greedy_f1: 0.4208\n    re_oracle_f1: 0.5882\n    re_headroom: 0.1674\n    re_fleiss_kappa_mean: 0.2996\n    re_soft_jaccard_mean: 0.6114\n    re_full_rho_fk: 0.2782\n    re_full_rho_sj: 0.2441\n    re_full_n: 397\n    re_cond_rho_fk: 0.3067\n    re_cond_rho_sj: 0.3161\n    re_cond_n: 313\n    re_sj_beats_fk_full: false\n    re_sj_beats_fk_cond: true\n    re_sample_f1_mean: 0.3612\n    re_sample_f1_std: 0.383\n    re_sample_f1_pct_zero: 44.3\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 84\n    parse_failures: 0\n    verdict: FAIL\n- exp_id: mvp_pilot_005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.6619\n    ner_oracle_f1: 0.7585\n    ner_headroom: 0.0966\n    ner_fleiss_kappa_mean: 0.4722\n    ner_soft_jaccard_mean: 0.7757\n    ner_full_rho_sj: 0.3875\n    ner_full_rho_fk: 0.3211\n    ner_full_n: 529\n    ner_cond_rho_sj: 0.3868\n    ner_cond_rho_fk: 0.305\n    ner_cond_n: 504\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_rho_advantage: 0.0664\n    ner_sample_f1_mean: 0.6243\n    ner_sample_f1_std: 0.3131\n    ner_sample_f1_pct_zero: 11.2\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 25\n    re_greedy_f1: 0.4219\n    re_oracle_f1: 0.5532\n    re_headroom: 0.1313\n    re_fleiss_kappa_mean: 0.3829\n    re_soft_jaccard_mean: 0.687\n    re_full_rho_sj: 0.2343\n    re_full_rho_fk: 0.1835\n    re_full_n: 397\n    re_cond_rho_sj: 0.3716\n    re_cond_rho_fk: 0.2533\n    re_cond_n: 301\n    re_sj_beats_fk_full: true\n    re_sj_beats_fk_cond: true\n    re_rho_advantage: 0.0508\n    re_sample_f1_mean: 0.3782\n    re_sample_f1_std: 0.3845\n    re_sample_f1_pct_zero: 42.4\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 96\n    parse_failures: 0\n    verdict: FAIL\n    verdict_note: RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional\n      but not full threshold\n- exp_id: e1_component_wise_re_sj\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    full_head_sj_rho: 0.21\n    full_tail_sj_rho: 0.201\n    full_type_match_rho: 0.201\n    full_multiplicative_rho: 0.244\n    full_additive_rho: 0.243\n    full_fleiss_kappa_rho: 0.278\n    cond_head_sj_rho: 0.27\n    cond_tail_sj_rho: 0.259\n    cond_type_match_rho: 0.252\n    cond_multiplicative_rho: 0.316\n    cond_additive_rho: 0.306\n    cond_fleiss_kappa_rho: 0.307\n    n_full: 397\n    n_conditional: 313\n    diagnosis: 'head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis\n      REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for\n      RE.'\n- exp_id: exp_012_logprob_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho_sj: 0.3565\n    ner_full_rho_fk: 0.2651\n    ner_full_rho_logprob: 0.1396\n    ner_full_rho_greedy_logprob: 0.1615\n    ner_full_tau_sj: 0.2658\n    ner_full_tau_logprob: 0.1006\n    ner_full_auroc_sj: 0.6892\n    ner_full_auroc_fk: 0.6292\n    ner_full_auroc_logprob: 0.5907\n    ner_full_n: 529\n    ner_sj_vs_logprob_delta: 0.2169\n    re_full_rho_sj: 0.2112\n    re_full_rho_fk: 0.2528\n    re_full_rho_logprob: 0.2467\n    re_full_auroc_sj: 0.5916\n    re_full_auroc_fk: 0.6262\n    re_full_auroc_logprob: 0.6186\n    re_full_n: 397\n    re_cond_rho_sj: 0.3683\n    re_cond_rho_fk: 0.3168\n    re_cond_rho_logprob: 0.1457\n    re_cond_auroc_sj: 0.6839\n    re_cond_auroc_logprob: 0.5487\n    re_cond_n: 296\n    diagnosis: 'NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead.\n      RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.'\n- exp_id: exp_013_exact_match_voting\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_full_rho: 0.2941\n    ner_full_p: 5.12e-12\n    ner_full_tau: 0.2181\n    ner_full_auroc: 0.6398\n    re_full_rho: 0.1562\n    re_full_p: 0.0018\n    re_full_tau: 0.1185\n    re_full_auroc: 0.5863\n    diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\n- exp_id: exp_014_entity_majority_voting\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho: 0.3915\n    ner_full_p: 8.1e-21\n    ner_full_tau: 0.2906\n    ner_full_auroc: 0.7039\n    re_full_rho: 0.3403\n    re_full_p: 3.21e-12\n    re_full_tau: 0.256\n    re_full_auroc: 0.6668\n    ner_voting_f1: 0.6246\n    ner_greedy_f1: 0.6483\n    ner_oracle_f1: 0.7793\n    re_voting_f1: 0.3577\n    re_greedy_f1: 0.4022\n    re_oracle_f1: 0.5886\n    diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE\n      (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\n- exp_id: exp_001_ner_n16_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_instances: 551\n    ner_n: 529\n    re_n: 397\n    N: 16\n    T: 1\n    seed: 42\n    full_test_set: true\n    ner_voting_conf_rho: 0.399\n    ner_sj_rho: 0.398\n    ner_em_rho: 0.339\n    ner_fk_rho: 0.288\n    ner_logprob_rho: 0.237\n    ner_voting_conf_auroc: 0.704\n    ner_sj_auroc: 0.697\n    ner_cond_em_rho: 0.414\n    ner_cond_sj_rho: 0.349\n    ner_cond_vc_rho: 0.34\n    re_voting_conf_rho: 0.38\n    re_logprob_rho: 0.293\n    re_fk_rho: 0.281\n    re_sj_rho: 0.277\n    re_em_rho: 0.148\n    re_voting_conf_auroc: 0.699\n    re_cond_em_rho: 0.475\n    re_cond_sj_rho: 0.318\n    re_cond_vc_rho: 0.35\n    re_cond_em_auroc: 0.742\n    diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380).\n      EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full\n      FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact of\n      200 instances + T=0.7.'\n- exp_id: exp_002_ner_conll2003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_003_ner_wnut17\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      greedy_f1: 0.525\n      oracle_f1: 0.664\n      headroom: 0.139\n      rho_sj_full: 0.082\n      rho_fk_full: 0.124\n      rho_logprob_full: -0.414\n      rho_sj_cond: 0.275\n      rho_fk_cond: 0.164\n      rho_logprob_cond: 0.352\n      sj_beats_logprob_cond: false\n    n_instances: 1287\n    n_gold_empty: 598\n    sample_f1_mean: 0.401\n    sample_f1_pct_zero: 53.7\n    N: 16\n    T: 1\n    seed: 42\n    verdict: FAIL\n    verdict_note: '>30% samples F1=0; structural rho weak; logprob baseline stronger'\n- exp_id: exp_007_ner_multi_model\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch: 5\n    train_loss: 0.0767\n    eval_loss: 0.1049\n    train_runtime_sec: 1494.5\n    train_samples_per_second: 6.226\n    checkpoints:\n    - checkpoint-400\n    - checkpoint-500\n    - checkpoint-585\n    base_model: Meta-Llama-3.1-8B-Instruct\n    lora_r: 32\n    lora_alpha: 64\n    note: EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal.\n      Checkpoint fully intact.\n- exp_id: exp_007_ner_llama\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_015_metrics_expansion\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_012_logprob/samples_with_logprobs.jsonl\n    config: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\n    ner:\n      n_valid: 529\n      n_cond: 501\n      voting_rho_full: 0.5018\n      voting_rho_cond: 0.4497\n      voting_auroc: 0.7279\n      voting_tau: 0.3766\n      sj_rho_full: 0.3565\n      sj_rho_cond: 0.412\n      sj_auroc: 0.6656\n      sj_tau: 0.2658\n      em_rho_full: 0.2566\n      em_rho_cond: 0.3427\n      em_auroc: 0.623\n      em_tau: 0.1924\n      fk_rho_full: 0.2651\n      fk_rho_cond: 0.306\n      fk_auroc: 0.6243\n      fk_tau: 0.2027\n      logprob_rho_full: 0.1396\n      logprob_rho_cond: 0.1627\n      logprob_auroc: 0.5585\n      logprob_tau: 0.1006\n    re:\n      n_valid: 397\n      n_cond: 296\n      voting_rho_full: 0.4217\n      voting_rho_cond: 0.463\n      voting_auroc: 0.7162\n      voting_tau: 0.327\n      sj_rho_full: 0.2112\n      sj_rho_cond: 0.3683\n      sj_auroc: 0.5816\n      sj_tau: 0.1619\n      em_rho_full: 0.1002\n      em_rho_cond: 0.3607\n      em_auroc: 0.5036\n      em_tau: 0.0839\n      fk_rho_full: 0.2528\n      fk_rho_cond: 0.3168\n      fk_auroc: 0.6308\n      fk_tau: 0.1967\n      logprob_rho_full: 0.2467\n      logprob_rho_cond: 0.1457\n      logprob_auroc: 0.6354\n      logprob_tau: 0.1808\n    diagnosis: 'Unified 5-signal evaluation on single data source. Voting leads NER\n      full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals\n      beat logprob on NER. RE: voting leads both full and cond.'\n- exp_id: exp_004_re_diagnostic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    per_relation_type:\n      HYPONYM-OF:\n        n: 36\n        rho_sj: 0.545\n        rho_fk: 0.646\n        rho_vc: 0.628\n        mean_f1: 0.513\n      CONJUNCTION:\n        n: 86\n        rho_sj: 0.383\n        rho_fk: 0.35\n        rho_vc: 0.484\n        mean_f1: 0.48\n      USED-FOR:\n        n: 299\n        rho_sj: 0.236\n        rho_fk: 0.255\n        rho_vc: 0.286\n        mean_f1: 0.422\n      PART-OF:\n        n: 44\n        rho_sj: 0.239\n        rho_fk: 0.348\n        rho_vc: 0.283\n        mean_f1: 0.297\n      EVALUATE-FOR:\n        n: 62\n        rho_sj: 0.172\n        rho_fk: 0.255\n        rho_vc: 0.226\n        mean_f1: 0.365\n      COMPARE:\n        n: 35\n        rho_sj: 0.168\n        rho_fk: 0.184\n        rho_vc: 0.18\n        mean_f1: 0.453\n      FEATURE-OF:\n        n: 50\n        rho_sj: 0.004\n        rho_fk: 0.052\n        rho_vc: 0.014\n        mean_f1: 0.254\n    error_propagation:\n      total_fn: 553\n      tail_error_pct: 21.9\n      full_error_pct: 21.7\n      head_error_pct: 17.7\n      head_tail_error_pct: 15.9\n      type_error_pct: 8.3\n      worst_consistency: head_type_error (sj=0.411)\n      best_consistency: head_error (sj=0.613)\n    threshold_sensitivity:\n      thr_0.00_rho_sj: 0.3161\n      thr_0.00_rho_vc: 0.3841\n      thr_0.00_n: 313\n      thr_0.05_rho_sj: 0.2682\n      thr_0.05_rho_vc: 0.2364\n      thr_0.05_n: 239\n    bootstrap_ci_95:\n      ner_sj:\n      - 0.2946\n      - 0.4586\n      ner_voting_conf:\n      - 0.3048\n      - 0.4656\n      re_sj:\n      - 0.1422\n      - 0.3391\n      re_voting_conf:\n      - 0.1818\n      - 0.3721\n      re_cond_sj:\n      - 0.2161\n      - 0.4102\n      re_cond_voting_conf:\n      - 0.2825\n      - 0.474\n    fisher_z_ner_vs_re:\n      sj_z: 2.31\n      sj_p: 0.0209\n      sj_significant: true\n      fk_z: -0.31\n      fk_p: 0.756\n      fk_significant: false\n      voting_z: 1.914\n      voting_p: 0.0556\n      voting_significant: false\n    diagnosis: FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF\n      strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of\n      RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE\n      signal in conditional set (rho=0.384).\n- exp_id: exp_008_re_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.6635\n      oracle_f1: 0.8208\n      headroom: 0.1572\n      rho_sj_full: 0.377\n      rho_fk_full: 0.2508\n      rho_logprob_full: 0.3153\n      rho_sj_cond: 0.3598\n      rho_fk_cond: 0.2251\n      rho_logprob_cond: 0.2927\n      sj_beats_fk: true\n      rho_advantage: 0.1262\n    re:\n      greedy_f1: 0.4339\n      oracle_f1: 0.6658\n      headroom: 0.2319\n      rho_sj_full: 0.2966\n      rho_fk_full: 0.2871\n      rho_logprob_full: 0.2986\n      rho_sj_cond: 0.3975\n      rho_fk_cond: 0.3774\n      rho_logprob_cond: 0.2745\n      sj_beats_fk: true\n      rho_advantage: 0.0095\n    verdict: FAIL\n- exp_id: exp001_seed123\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp001_seed456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_re_n16\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_n16_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.655\n      oracle_f1: 0.8028\n      headroom: 0.1478\n      rho_sj_full: 0.4076\n      rho_fk_full: 0.2799\n      rho_logprob_full: 0.3189\n      rho_sj_cond: 0.4271\n      rho_fk_cond: 0.2743\n      rho_logprob_cond: 0.2835\n      sj_beats_fk: true\n      rho_advantage: 0.1277\n    re:\n      greedy_f1: 0.4243\n      oracle_f1: 0.6771\n      headroom: 0.2528\n      rho_sj_full: 0.2943\n      rho_fk_full: 0.2657\n      rho_logprob_full: 0.3005\n      rho_sj_cond: 0.4003\n      rho_fk_cond: 0.313\n      rho_logprob_cond: 0.2317\n      sj_beats_fk: true\n      rho_advantage: 0.0286\n    verdict: FAIL\n- exp_id: exp_001_n16_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.6577\n      oracle_f1: 0.8129\n      headroom: 0.1553\n      rho_sj_full: 0.3297\n      rho_fk_full: 0.2578\n      rho_logprob_full: 0.2866\n      rho_sj_cond: 0.3394\n      rho_fk_cond: 0.2721\n      rho_logprob_cond: 0.2567\n      sj_beats_fk: true\n      rho_advantage: 0.0719\n    re:\n      greedy_f1: 0.4312\n      oracle_f1: 0.6737\n      headroom: 0.2425\n      rho_sj_full: 0.285\n      rho_fk_full: 0.2372\n      rho_logprob_full: 0.2626\n      rho_sj_cond: 0.3525\n      rho_fk_cond: 0.2614\n      rho_logprob_cond: 0.1927\n      sj_beats_fk: true\n      rho_advantage: 0.0478\n    verdict: FAIL\n- exp_id: exp_016_signal_ensemble\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_logprob_pearson_ner: 0.57\n    sj_logprob_pearson_re: 0.42\n    best_linear_ner:\n      combo: SJ+voting_conf\n      alpha: 0.3\n      rho: 0.489\n    best_linear_re:\n      combo: voting_conf+logprob\n      alpha: 0.6\n      rho: 0.429\n    ensemble_ner_auroc: 0.735\n    ensemble_re_auroc: 0.719\n    best_single_ner_auroc: 0.7\n    best_single_re_auroc: 0.721\n    ensemble_ner_delta: 0.035\n    selection_f1_ner:\n      greedy: 0.609\n      logprob: 0.609\n      sj: 0.604\n      ensemble: 0.604\n      voting: 0.596\n      random: 0.58\n      oracle: 0.769\n    selection_f1_re:\n      logprob: 0.397\n      greedy: 0.374\n      sj: 0.368\n      ensemble: 0.367\n      voting: 0.338\n      random: 0.338\n      oracle: 0.561\n    diagnosis: 'SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best\n      is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER.\n      Oracle gap still huge.'\n- exp_id: exp_002_merge_conll2003\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_rho_full: 0.4357\n    sj_tau_full: 0.3851\n    sj_auroc_full: 0.8008\n    sj_rho_cond: 0.4511\n    fk_rho_full: 0.3998\n    fk_tau_full: 0.3568\n    fk_auroc_full: 0.7741\n    fk_rho_cond: 0.4064\n    logprob_rho_full: 0.3157\n    logprob_tau_full: 0.2469\n    logprob_auroc_full: 0.7532\n    logprob_rho_cond: 0.3562\n    em_rho_full: 0.4507\n    em_tau_full: 0.4002\n    em_auroc_full: 0.8156\n    em_rho_cond: 0.4799\n    ev_rho_full: 0.4237\n    ev_tau_full: 0.3777\n    ev_auroc_full: 0.7889\n    ev_rho_cond: 0.4127\n    greedy_f1: 0.9123\n    oracle_f1: 0.9543\n    voting_f1: 0.9141\n    oracle_headroom: 0.042\n    sj_vs_logprob_delta_rho: 0.12\n    sj_vs_logprob_ci_low: 0.0881\n    sj_vs_logprob_ci_high: 0.154\n    sj_vs_logprob_significant: true\n    n_instances: 3453\n    n_valid: 2756\n    n_samples: 8\n    temperature: 1\n- exp_id: exp_001_n16_seed123_full\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_n16_seed456_full\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_008_re_n16_full\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_ner_n16_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.663\n      oracle_f1: 0.809\n      headroom: 0.146\n      rho_sj: 0.423\n      rho_fk: 0.29\n      rho_logprob: 0.239\n      rho_sj_cond: 0.423\n      rho_fk_cond: 0.26\n    re:\n      greedy_f1: 0.419\n      oracle_f1: 0.625\n      headroom: 0.206\n      rho_sj: 0.267\n      rho_fk: 0.315\n      rho_sj_cond: 0.364\n      rho_fk_cond: 0.331\n    verdict: FAIL\n    verdict_note: RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\n    n_instances: 551\n    seed: 123\n    N: 16\n    T: 1\n- exp_id: exp_001_seed456_t10_full\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      rho_sj: 0.414\n      rho_fk: 0.298\n    re:\n      rho_sj: 0.268\n      rho_fk: 0.26\n    n_instances: 551\n    N: 16\n    T: 1\n    seed: 456\n    source: reviewer_verified_report_json\n- exp_id: exp_001_seed123_t10_full\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      rho_sj: 0.417\n      rho_fk: 0.283\n    re:\n      rho_sj: 0.265\n      rho_fk: 0.315\n    n_instances: 551\n    N: 16\n    T: 1\n    seed: 123\n    source: reviewer_verified_report_json\n- exp_id: exp_008_re_n16_t10_full\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      rho_sj: 0.444\n    re:\n      rho_sj: 0.248\n    n_instances: 551\n    N: 16\n    T: 1\n    seed: 42\n    mode: RE-only\n    source: director_corrected\n- exp_id: exp_003_wnut17_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.523\n    oracle_f1: 0.664\n    headroom: 0.141\n    rho_fk: 0.125\n    rho_sj: 0.089\n    rho_fk_cond: 0.169\n    rho_sj_cond: 0.288\n    rho_logprob_full: -0.409\n    rho_logprob_cond: 0.35\n    structural_beats_surface: false\n    sample_f1_pct_zero: 53.7\n    n_instances: 1287\n    N: 16\n    T: 1\n    seed: 42\n    model: Qwen3-8B\n    n_gold_empty_filtered: 598\n    verdict: FAIL\n    verdict_note: structural_beats_surface=false; >50% samples F1=0\n- exp_id: exp_007_llama_inference\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.66\n      oracle_f1: 0.781\n      headroom: 0.121\n      rho_fk: 0.327\n      rho_sj: 0.363\n      rho_fk_cond: 0.226\n      rho_sj_cond: 0.311\n      rho_logprob: 0.183\n      rho_logprob_cond: 0.109\n      structural_beats_surface: true\n      sample_f1_pct_zero: 11.6\n    re:\n      greedy_f1: 0.434\n      oracle_f1: 0.568\n      headroom: 0.135\n      rho_fk: 0.305\n      rho_sj: 0.299\n      rho_fk_cond: 0.259\n      rho_sj_cond: 0.405\n      rho_logprob: 0.288\n      rho_logprob_cond: 0.092\n      structural_beats_surface: false\n      sample_f1_pct_zero: 41.2\n    n_instances: 551\n    N: 8\n    T: 1\n    seed: 42\n    model: LLaMA-3.1-8B-Instruct\n    verdict: FAIL\n    verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\n- exp_id: exp_001_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_rho_full: 0.428\n    sj_rho_cond: 0.369\n    structural_minus_surface: 0.147\n    conclusion_note: NER seed42 robustness confirmed, structural>surface +0.147\n- exp_id: exp_001_seed123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_rho_full: 0.424\n    sj_rho_cond: 0.376\n    structural_minus_surface: 0.149\n    conclusion_note: NER seed123 robustness confirmed, structural>surface +0.149\n- exp_id: exp_008_re_n16_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    sj_rho_full: 0.281\n    sj_rho_cond: 0.308\n    f1_zero_pct: 44.3\n    conclusion_note: 'RE N=16 v2 negative: SJ weak, 44.3% F1=0'\n- exp_id: exp_017_llama_conll\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_009_capability_stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n: 551\n      sj_rho_overall: 0.398\n      by_greedy_f1:\n        hard_0_25_sj_rho: 0.159\n        med_low_sj_rho: 0.139\n        med_high_sj_rho: 0.09\n        easy_sj_rho: 0.23\n      by_sent_len:\n        Q1_sj_rho: 0.461\n        Q2_sj_rho: 0.401\n        Q3_sj_rho: 0.296\n        Q4_sj_rho: 0.382\n      by_ent_count:\n        0_sj_rho: 0.689\n        1_2_sj_rho: 0.415\n        3_5_sj_rho: 0.353\n        6plus_sj_rho: 0.547\n    scierc_re:\n      n: 551\n      by_greedy_f1:\n        hard_0_25_sj_rho: -0.043\n        easy_sj_rho: 0.21\n      by_sent_len:\n        Q1_sj_rho: 0.447\n        Q4_sj_rho: 0.54\n      by_rel_count:\n        0_sj_rho: 0.62\n        1_2_sj_rho: 0.275\n        6plus_sj_rho: 0.527\n    conll_ner:\n      n: 3453\n      by_sent_len:\n        Q1_sj_rho: 0.334\n        Q3_sj_rho: 0.518\n    proxy_independence:\n      scierc_ner_f1_vs_slen: -0.021\n      scierc_ner_f1_vs_ecnt: 0.007\n      scierc_re_f1_vs_slen: -0.147\n- exp_id: exp_010_selection_curves\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n_instances: 551\n      greedy_f1: 0.618\n      N16:\n        oracle: 0.787\n        SJ: 0.62\n        FK: 0.621\n        logprob: 0.621\n        voting_conf: 0.585\n        EM: 0.606\n        random: 0.595\n      N8:\n        oracle: 0.752\n        SJ: 0.614\n        FK: 0.614\n        logprob: 0.619\n        voting_conf: 0.591\n        EM: 0.603\n        random: 0.589\n      N4:\n        oracle: 0.714\n        SJ: 0.607\n        FK: 0.608\n        logprob: 0.616\n        voting_conf: 0.594\n        EM: 0.6\n        random: 0.587\n    scierc_re:\n      n_instances: 397\n      greedy_f1: 0.403\n      N16:\n        oracle: 0.631\n        SJ: 0.397\n        FK: 0.396\n        logprob: 0.41\n        voting_conf: 0.408\n        EM: 0.381\n        random: 0.364\n      N8:\n        oracle: 0.583\n        SJ: 0.393\n        FK: 0.394\n        logprob: 0.413\n        voting_conf: 0.398\n        EM: 0.381\n        random: 0.363\n    conll_ner:\n      n_instances: 3453\n      greedy_f1: 0.725\n      N8:\n        oracle: 0.757\n        SJ: 0.718\n        FK: 0.717\n        logprob: 0.716\n        voting_conf: 0.714\n        EM: 0.716\n        random: 0.69\n      N4:\n        oracle: 0.746\n        SJ: 0.714\n        FK: 0.714\n        logprob: 0.715\n        voting_conf: 0.714\n        EM: 0.712\n        random: 0.692\n- exp_id: exp_007_llama_seed123\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    ner:\n      greedy_f1: 0.6605\n      oracle_f1: 0.7703\n      headroom: 0.1098\n      fleiss_kappa: 0.4553\n      soft_jaccard: 0.7525\n      rho_kappa_f1: 0.2143\n      rho_sj_f1: 0.3371\n      structural_gt_surface: true\n    re:\n      greedy_f1: 0.433\n      oracle_f1: 0.5719\n      headroom: 0.1389\n      fleiss_kappa: 0.3851\n      soft_jaccard: 0.6911\n      rho_kappa_f1: 0.2844\n      rho_sj_f1: 0.268\n      structural_gt_surface: false\n    fail_reasons:\n    - RE rho_sj=0.2680 < 0.40 threshold\n    - '>30% samples F1=0 (RE: 41.0%)'\n    - RE structural not > surface (delta=-0.0165)\n- exp_id: exp_007_llama_seed456\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    ner:\n      greedy_f1: 0.6597\n      oracle_f1: 0.7575\n      oracle_headroom: 0.0978\n      fleiss_kappa: 0.4543\n      soft_jaccard: 0.7491\n      rho_kappa_f1: 0.3115\n      rho_sj_f1: 0.3663\n      structural_gt_surface: true\n    re:\n      greedy_f1: 0.4334\n      oracle_f1: 0.5789\n      oracle_headroom: 0.1455\n      fleiss_kappa: 0.3791\n      soft_jaccard: 0.6782\n      rho_kappa_f1: 0.3013\n      rho_sj_f1: 0.287\n      structural_gt_surface: false\n    logprob_ner:\n      rho: 0.1911\n      auroc: 0.5989\n    logprob_re:\n      rho: 0.3246\n      auroc: 0.6678\n    fail_reason: RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\n- exp_id: exp_008_re_seed123\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    greedy_f1: 0.4229\n    oracle_f1: 0.6244\n    oracle_headroom: 0.2015\n    fleiss_kappa_mean: 0.3455\n    soft_jaccard_mean: 0.6126\n    sample_f1_mean: 0.3594\n    sample_f1_std: 0.3793\n    sample_f1_zero_pct: 44.1\n    structural_gt_surface: false\n    rho_kappa_f1_full: 0.3174\n    rho_sj_f1_full: 0.2835\n    rho_kappa_f1_cond: 0.0766\n    rho_sj_f1_cond: 0.2877\n    logprob_auroc_full: 0.6499\n    logprob_auroc_cond: 0.5265\n    verdict: FAIL\n- exp_id: exp_005_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    NER_SciERC_s42:\n      greedy: 0.618\n      oracle: 0.787\n      SJ: 0.62\n      logprob: 0.621\n      FK: 0.621\n      EM: 0.606\n      voting_conf: 0.585\n      random: 0.586\n    NER_SciERC_s123:\n      greedy: 0.618\n      oracle: 0.785\n      SJ: 0.617\n      logprob: 0.618\n      FK: 0.621\n      EM: 0.613\n      voting_conf: 0.584\n      random: 0.583\n    NER_CoNLL:\n      greedy: 0.725\n      oracle: 0.757\n      SJ: 0.718\n      logprob: 0.716\n      FK: 0.717\n      EM: 0.716\n      voting_conf: 0.714\n      random: 0.692\n    RE_SciERC:\n      greedy: 0.403\n      oracle: 0.631\n      SJ: 0.397\n      logprob: 0.41\n      FK: 0.396\n      EM: 0.381\n      voting_conf: 0.408\n      random: 0.364\n- exp_id: exp_004_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_003_wnut17_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_015_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner_avg:\n      sj_auroc: 0.7394\n      fk_auroc: 0.6172\n      em_auroc: 0.7873\n      voting_auroc: 0.7367\n      logprob_auroc: 0.5918\n    scierc_re_avg:\n      sj_auroc: 0.6746\n      fk_auroc: 0.5939\n      em_auroc: 0.715\n      voting_auroc: 0.7234\n      logprob_auroc: 0.5849\n- exp_id: exp_009_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_seed42_global:\n      sj_rho: 0.431\n      fk_rho: 0.325\n      logprob_rho: 0.203\n      voting_conf_rho: 0.475\n      em_rho: 0.292\n    ner_seed123_global:\n      sj_rho: 0.422\n      fk_rho: 0.315\n      logprob_rho: 0.226\n      voting_conf_rho: 0.438\n      em_rho: 0.299\n    re_seed42_global:\n      sj_rho: 0.063\n      fk_rho: 0.226\n      logprob_rho: 0.4\n      voting_conf_rho: 0.22\n      em_rho: -0.132\n    ner_seed_stability_max_delta: 0.037\n    independent_proxies:\n    - sent_len\n    - ent_count\n    - type_diversity\n    inverted_u_ner: not confirmed (ρ stable across independent proxies)\n    inverted_u_re: monotonic increase with complexity, not inverted-U\n- exp_id: exp_001_seed456_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_016_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_conditional:\n      n: 529\n      best_single_signal_rho:\n        soft_jaccard: 0.4412\n      best_combo_rho:\n        sj+vc_a0.55: 0.4552\n      ensemble_auroc: 0.7141\n      best_single_auroc:\n        soft_jaccard: 0.7166\n      selection_f1:\n        greedy: 0.6442\n        logprob_best: 0.6505\n        ensemble_best: 0.6475\n        sj_best: 0.6471\n        oracle: 0.8442\n    re_conditional:\n      n: 397\n      best_single_signal_rho:\n        voting_confidence: 0.3849\n      best_combo_rho:\n        logprob+vc_a0.25: 0.3936\n      ensemble_auroc: 0.6916\n      best_single_auroc:\n        voting_confidence: 0.7023\n      selection_f1:\n        greedy: 0.403\n        logprob_best: 0.4097\n        ensemble_best: 0.4227\n        oracle: 0.6306\n    re_full:\n      ensemble_auroc: 0.8608\n      best_single_auroc:\n        voting_confidence: 0.8248\n- exp_id: exp_001_seed456_v2_ner\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full:\n      SJ:\n        rho: 0.384\n        auroc: 0.711\n      FK:\n        rho: 0.223\n        auroc: 0.577\n      logprob:\n        rho: 0.232\n        auroc: 0.594\n      EM:\n        rho: 0.316\n        auroc: 0.768\n      voting_conf:\n        rho: 0.411\n        auroc: 0.712\n    conditional:\n      SJ:\n        rho: 0.349\n        auroc: 0.699\n      FK:\n        rho: 0.157\n        auroc: 0.561\n      logprob:\n        rho: 0.171\n        auroc: 0.576\n      EM:\n        rho: 0.406\n        auroc: 0.78\n      voting_conf:\n        rho: 0.346\n        auroc: 0.694\n    3seed_mean_SJ_rho_full: 0.412\n    3seed_sd_SJ_rho_full: 0.025\n    structural_beats_surface: true\n    verdict: MARGINAL\n- exp_id: exp_017_llama_conll_infer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9266\n    oracle_f1: 0.9443\n    oracle_headroom: 0.0177\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    N: 8\n    full:\n      SJ_rho: 0.4314\n      FK_rho: 0.4277\n      logprob_rho: 0.3072\n      EM_rho: 0.4306\n      voting_conf_rho: 0.4256\n      SJ_AUROC: 0.7039\n      FK_AUROC: 0.7026\n      logprob_AUROC: 0.761\n      EM_AUROC: 0.7046\n      voting_conf_AUROC: 0.7088\n      SJ_ECE: 0.1137\n      FK_ECE: 0.1053\n      logprob_ECE: 0.129\n      EM_ECE: 0.1094\n      voting_conf_ECE: 0.0949\n    conditional:\n      SJ_rho: 0.4356\n      FK_rho: 0.431\n      logprob_rho: 0.3282\n      EM_rho: 0.4403\n      voting_conf_rho: 0.3743\n      SJ_AUROC: 0.7225\n      FK_AUROC: 0.7208\n      logprob_AUROC: 0.8102\n      EM_AUROC: 0.7257\n      voting_conf_AUROC: 0.6989\n      SJ_ECE: 0.0829\n      FK_ECE: 0.0796\n      logprob_ECE: 0.0922\n      EM_ECE: 0.0754\n      voting_conf_ECE: 0.0784\n- exp_id: exp_002_conll_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    N: 16\n    dataset: conll2003\n    subtask: ner\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2614\n    greedy_f1: 0.907\n    full:\n      SJ_rho: 0.4496\n      FK_rho: 0.3928\n      logprob_rho: 0.3146\n      EM_rho: 0.4627\n      voting_conf_rho: 0.4286\n      SJ_AUROC: 0.8264\n      FK_AUROC: 0.7821\n      logprob_AUROC: 0.7531\n      EM_AUROC: 0.8409\n      voting_conf_AUROC: 0.8071\n      SJ_ECE: 0.0747\n      FK_ECE: 0.1786\n      logprob_ECE: 0.2031\n      EM_ECE: 0.0786\n      voting_conf_ECE: 0.529\n    conditional:\n      SJ_rho: 0.4208\n      FK_rho: 0.3494\n      logprob_rho: 0.3756\n      EM_rho: 0.4658\n      voting_conf_rho: 0.3654\n      SJ_AUROC: 0.8405\n      FK_AUROC: 0.7819\n      logprob_AUROC: 0.8259\n      EM_AUROC: 0.8781\n      voting_conf_AUROC: 0.7951\n      SJ_ECE: 0.0982\n      FK_ECE: 0.1899\n      logprob_ECE: 0.2504\n      EM_ECE: 0.0997\n      voting_conf_ECE: 0.6096\n    n8_vs_n16_delta_rho_full:\n      SJ: 0.0139\n      FK: -0.007\n      logprob: -0.0011\n      EM: 0.012\n      voting_conf: 0.0049\n- exp_id: exp_007_llama_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    N: 16\n    dataset: scierc\n    subtask: ner\n    n_instances: 551\n    n_valid: 529\n    n_conditional: 478\n    greedy_f1: 0.645\n    full:\n      SJ_rho: 0.3791\n      FK_rho: 0.3081\n      logprob_rho: 0.2041\n      EM_rho: 0.3159\n      voting_conf_rho: 0.4515\n      SJ_AUROC: 0.717\n      FK_AUROC: 0.6581\n      logprob_AUROC: 0.5656\n      EM_AUROC: 0.7686\n      voting_conf_AUROC: 0.7266\n      SJ_ECE: 0.1019\n      FK_ECE: 0.1556\n      logprob_ECE: 0.084\n      EM_ECE: 0.1761\n      voting_conf_ECE: 0.1365\n    conditional:\n      SJ_rho: 0.3222\n      FK_rho: 0.2182\n      logprob_rho: 0.1286\n      EM_rho: 0.3563\n      voting_conf_rho: 0.3356\n      SJ_AUROC: 0.7014\n      FK_AUROC: 0.6392\n      logprob_AUROC: 0.545\n      EM_AUROC: 0.7708\n      voting_conf_AUROC: 0.6988\n      SJ_ECE: 0.1466\n      FK_ECE: 0.1853\n      logprob_ECE: 0.1141\n      EM_ECE: 0.1887\n      voting_conf_ECE: 0.2634\n    n8_vs_n16_delta_rho_full:\n      SJ: 0.0161\n      FK: -0.0185\n      logprob: 0.0214\n      EM: 0.0007\n      voting_conf: 0.0184\n- exp_id: exp_009_v2_re_rerun\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_017_llama_conll_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9243\n    oracle_f1: 0.9487\n    oracle_headroom: 0.0244\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    structural_beats_surface: true\n    full:\n      SJ_rho: 0.4642\n      SJ_AUROC: 0.7391\n      SJ_ECE: 0.1131\n      FK_rho: 0.4566\n      FK_AUROC: 0.736\n      FK_ECE: 0.1071\n      logprob_rho: 0.3058\n      logprob_AUROC: 0.7594\n      logprob_ECE: 0.1288\n      EM_rho: 0.4613\n      EM_AUROC: 0.7391\n      EM_ECE: 0.1084\n      voting_conf_rho: 0.4554\n      voting_conf_AUROC: 0.7406\n      voting_conf_ECE: 0.0844\n    conditional:\n      SJ_rho: 0.4597\n      SJ_AUROC: 0.7565\n      SJ_ECE: 0.0846\n      FK_rho: 0.4515\n      FK_AUROC: 0.753\n      FK_ECE: 0.0813\n      logprob_rho: 0.3193\n      logprob_AUROC: 0.8023\n      logprob_ECE: 0.0921\n      EM_rho: 0.4618\n      EM_AUROC: 0.7589\n      EM_ECE: 0.0757\n      voting_conf_rho: 0.3978\n      voting_conf_AUROC: 0.7287\n      voting_conf_ECE: 0.0742\n    best_of_n:\n      greedy: 0.9243\n      random_avg: 0.9213\n      sj_best: 0.9259\n      logprob_best: 0.925\n      voting_conf_best: 0.9268\n      oracle: 0.9487\n    n8_vs_n16_delta:\n      full_SJ_rho_delta: 0.0328\n      full_FK_rho_delta: 0.0289\n      full_logprob_rho_delta: -0.0014\n      full_EM_rho_delta: 0.0307\n      full_voting_conf_rho_delta: 0.0298\n      cond_SJ_rho_delta: 0.0241\n      cond_FK_rho_delta: 0.0205\n      cond_logprob_rho_delta: -0.0089\n      cond_EM_rho_delta: 0.0215\n      cond_voting_conf_rho_delta: 0.0235\n- exp_id: exp_017_llama_conll_n16_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9266\n    oracle_f1: 0.9497\n    oracle_headroom: 0.0231\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    structural_beats_surface: true\n    full:\n      SJ_rho: 0.4698\n      SJ_AUROC: 0.7402\n      SJ_ECE: 0.1135\n      FK_rho: 0.4594\n      FK_AUROC: 0.7351\n      FK_ECE: 0.1114\n      logprob_rho: 0.3161\n      logprob_AUROC: 0.768\n      logprob_ECE: 0.129\n      EM_rho: 0.4676\n      EM_AUROC: 0.7399\n      EM_ECE: 0.1082\n      voting_conf_rho: 0.4612\n      voting_conf_AUROC: 0.7429\n      voting_conf_ECE: 0.0832\n    conditional:\n      SJ_rho: 0.4712\n      SJ_AUROC: 0.7609\n      SJ_ECE: 0.0828\n      FK_rho: 0.4595\n      FK_AUROC: 0.7547\n      FK_ECE: 0.0858\n      logprob_rho: 0.3314\n      logprob_AUROC: 0.8134\n      logprob_ECE: 0.0922\n      EM_rho: 0.4732\n      EM_AUROC: 0.7626\n      EM_ECE: 0.075\n      voting_conf_rho: 0.4086\n      voting_conf_AUROC: 0.7338\n      voting_conf_ECE: 0.0706\n    best_of_n:\n      greedy: 0.9242\n      random_avg: 0.9216\n      sj_best: 0.9247\n      logprob_best: 0.9253\n      voting_conf_best: 0.9255\n      oracle: 0.9486\n    n8_vs_n16_delta:\n      full_SJ_rho_delta: 0.0384\n      full_FK_rho_delta: 0.0317\n      full_logprob_rho_delta: 0.0089\n      full_SJ_AUROC_delta: 0.0363\n      full_FK_AUROC_delta: 0.0325\n      full_logprob_AUROC_delta: 0.007\n      cond_SJ_rho_delta: 0.0356\n      cond_FK_rho_delta: 0.0285\n      cond_logprob_rho_delta: 0.0032\n- exp_id: exp_017_llama_conll_n16_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9243\n    oracle_f1: 0.9488\n    oracle_headroom: 0.0245\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    structural_beats_surface: true\n    full:\n      SJ_rho: 0.4552\n      SJ_AUROC: 0.7288\n      SJ_ECE: 0.1134\n      FK_rho: 0.4478\n      FK_AUROC: 0.7248\n      FK_ECE: 0.109\n      logprob_rho: 0.3078\n      logprob_AUROC: 0.7612\n      logprob_ECE: 0.1289\n      EM_rho: 0.452\n      EM_AUROC: 0.7275\n      EM_ECE: 0.1082\n      voting_conf_rho: 0.4571\n      voting_conf_AUROC: 0.7348\n      voting_conf_ECE: 0.0863\n    conditional:\n      SJ_rho: 0.4505\n      SJ_AUROC: 0.7449\n      SJ_ECE: 0.0826\n      FK_rho: 0.4422\n      FK_AUROC: 0.7401\n      FK_ECE: 0.0835\n      logprob_rho: 0.3242\n      logprob_AUROC: 0.8067\n      logprob_ECE: 0.0921\n      EM_rho: 0.451\n      EM_AUROC: 0.745\n      EM_ECE: 0.0756\n      voting_conf_rho: 0.3962\n      voting_conf_AUROC: 0.7202\n      voting_conf_ECE: 0.0746\n    best_of_n:\n      greedy: 0.9243\n      random_avg: 0.9215\n      sj_best: 0.9243\n      logprob_best: 0.9243\n      voting_conf_best: 0.9243\n      oracle: 0.9488\n    n8_vs_n16_delta:\n      full_SJ_rho_delta: 0.0238\n      full_FK_rho_delta: 0.0201\n      full_logprob_rho_delta: 0.0006\n      full_EM_rho_delta: 0.0214\n      full_voting_conf_rho_delta: 0.0315\n      cond_SJ_rho_delta: 0.0149\n      cond_FK_rho_delta: 0.0112\n      cond_logprob_rho_delta: -0.004\n      cond_EM_rho_delta: 0.0107\n      cond_voting_conf_rho_delta: 0.0219\n- exp_id: exp_012_rerun_1024\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full:\n      n: 529\n      SJ:\n        rho: 0.3599\n        tau: 0.2646\n        AUROC: 0.6917\n        ECE: 0.4531\n        rho_ci95:\n        - 0.2732\n        - 0.4389\n        AUROC_ci95:\n        - 0.6304\n        - 0.7406\n      FK:\n        rho: 0.2665\n        tau: 0.1974\n        AUROC: 0.629\n        ECE: 0.4512\n        rho_ci95:\n        - 0.1743\n        - 0.3486\n        AUROC_ci95:\n        - 0.5612\n        - 0.6882\n      logprob:\n        rho: 0.2052\n        tau: 0.1478\n        AUROC: 0.5783\n        ECE: 0.7064\n        rho_ci95:\n        - 0.1171\n        - 0.2904\n        AUROC_ci95:\n        - 0.5179\n        - 0.6387\n      EM:\n        rho: 0.2945\n        tau: 0.2208\n        AUROC: 0.7493\n        ECE: 0.3526\n        rho_ci95:\n        - 0.2094\n        - 0.37\n        AUROC_ci95:\n        - 0.7002\n        - 0.7928\n      voting_conf:\n        rho: 0.3792\n        tau: 0.2805\n        AUROC: 0.6841\n        ECE: 0.3807\n        rho_ci95:\n        - 0.2972\n        - 0.4486\n        AUROC_ci95:\n        - 0.6249\n        - 0.7366\n    ner_cond:\n      n: 477\n      SJ:\n        rho: 0.3113\n        tau: 0.2257\n        AUROC: 0.6772\n        ECE: 0.4416\n        rho_ci95:\n        - 0.2353\n        - 0.3959\n        AUROC_ci95:\n        - 0.621\n        - 0.7337\n      FK:\n        rho: 0.1761\n        tau: 0.1284\n        AUROC: 0.6078\n        ECE: 0.4389\n        rho_ci95:\n        - 0.0839\n        - 0.2665\n        AUROC_ci95:\n        - 0.5442\n        - 0.6709\n      logprob:\n        rho: 0.1538\n        tau: 0.1111\n        AUROC: 0.5633\n        ECE: 0.6803\n        rho_ci95:\n        - 0.0637\n        - 0.2424\n        AUROC_ci95:\n        - 0.5032\n        - 0.6232\n      EM:\n        rho: 0.3596\n        tau: 0.2735\n        AUROC: 0.7556\n        ECE: 0.3257\n        rho_ci95:\n        - 0.2819\n        - 0.4408\n        AUROC_ci95:\n        - 0.7011\n        - 0.8107\n      voting_conf:\n        rho: 0.3\n        tau: 0.2189\n        AUROC: 0.6618\n        ECE: 0.3746\n        rho_ci95:\n        - 0.2168\n        - 0.3836\n        AUROC_ci95:\n        - 0.6004\n        - 0.7201\n    re_full:\n      n: 397\n      SJ:\n        rho: 0.2503\n        tau: 0.1878\n        AUROC: 0.6702\n        ECE: 0.3865\n      FK:\n        rho: 0.2752\n        tau: 0.2117\n        AUROC: 0.6089\n        ECE: 0.4405\n      logprob:\n        rho: 0.2662\n        tau: 0.1951\n        AUROC: 0.6005\n        ECE: 0.7694\n      EM:\n        rho: 0.1344\n        tau: 0.1081\n        AUROC: 0.7059\n        ECE: 0.3548\n      voting_conf:\n        rho: 0.3498\n        tau: 0.2663\n        AUROC: 0.6935\n        ECE: 0.2724\n    re_cond:\n      n: 238\n      SJ:\n        rho: 0.2457\n        tau: 0.1811\n        AUROC: 0.6463\n        ECE: 0.2941\n      FK:\n        rho: 0.1139\n        tau: 0.0876\n        AUROC: 0.551\n        ECE: 0.3424\n      logprob:\n        rho: 0.0112\n        tau: 0.0051\n        AUROC: 0.5186\n        ECE: 0.6464\n      EM:\n        rho: 0.4165\n        tau: 0.3256\n        AUROC: 0.7515\n        ECE: 0.2232\n      voting_conf:\n        rho: 0.2409\n        tau: 0.178\n        AUROC: 0.642\n        ECE: 0.207\n    delta_vs_512_ner_full_rho:\n      SJ: 0.0034\n      FK: 0.0014\n      EM: 0.0379\n      voting_conf: -0.1226\n      logprob: 0.0656\n    provenance_note: exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512\n      truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed\n      0.140→0.205.\n- exp_id: exp_001_seed42_v2_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    greedy_f1: 0.6647\n    oracle_f1: 0.8106\n    softjaccard_rho_full: 0.3928\n    fleiss_rho_full: 0.2489\n    logprob_rho_full: 0.2136\n    softjaccard_rho_cond: 0.3455\n    fleiss_rho_cond: 0.163\n    logprob_rho_cond: 0.1624\n    verdict: MARGINAL\n- exp_id: exp_001_seed123_v2_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_seed456_v2_ner_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002_conll_n16_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_007_llama_n16_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_017_llama_conll_n16_r1024\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_017_llama_conll_n16_s123_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_017_llama_conll_n16_s456_r1024\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_016_rerun_1024_bootstrap\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bootstrap_ci_95:\n    - -0.03\n    - 0.042\n    permutation_p: 0.39\n    cohen_d: 0.038\n    sign_test_win_rate: 0.466\n    ner_logprob_vs_greedy_delta: 0.006\n    conclusion_summary: 'NER selection: no signal significantly outperforms greedy;\n      RE: same conclusion'\n- exp_id: exp_018_qwen_scierc_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_018_qwen_scierc_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_018_llama_scierc_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_018_llama_scierc_seed456\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_018_llama_scierc_seed42_r1024\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      full:\n        SJ:\n          rho: 0.3096\n          tau: 0.2288\n          auroc: 0.6683\n        FK:\n          rho: 0.2352\n          tau: 0.1759\n          auroc: 0.6069\n        logprob:\n          rho: 0.1503\n          tau: 0.1087\n          auroc: 0.5318\n        EM:\n          rho: 0.2587\n          tau: 0.1966\n          auroc: 0.7174\n        voting_conf:\n          rho: 0.4053\n          tau: 0.3042\n          auroc: 0.6967\n      conditional:\n        SJ:\n          rho: 0.2718\n          tau: null\n          auroc: 0.6565\n        FK:\n          rho: 0.1472\n          tau: null\n          auroc: 0.5866\n        logprob:\n          rho: 0.081\n          tau: null\n          auroc: 0.5129\n        EM:\n          rho: 0.3165\n          tau: null\n          auroc: 0.7244\n        voting_conf:\n          rho: 0.3078\n          tau: null\n          auroc: 0.6714\n      greedy_f1: 0.6607\n      oracle_f1: 0.7781\n      n_full: 529\n      n_cond: 478\n    re:\n      full:\n        SJ:\n          rho: 0.2748\n          tau: 0.2102\n          auroc: 0.7244\n        FK:\n          rho: 0.3027\n          tau: 0.2337\n          auroc: 0.691\n        logprob:\n          rho: 0.3163\n          tau: 0.233\n          auroc: 0.6313\n        EM:\n          rho: 0.1681\n          tau: 0.1275\n          auroc: 0.7697\n        voting_conf:\n          rho: 0.384\n          tau: 0.2965\n          auroc: 0.7337\n      conditional:\n        SJ:\n          rho: 0.3461\n          tau: null\n          auroc: 0.7233\n        FK:\n          rho: 0.1969\n          tau: null\n          auroc: 0.6684\n        logprob:\n          rho: 0.0888\n          tau: null\n          auroc: 0.5556\n        EM:\n          rho: 0.4969\n          tau: null\n          auroc: 0.819\n        voting_conf:\n          rho: 0.3433\n          tau: null\n          auroc: 0.7003\n      greedy_f1: 0.4319\n      oracle_f1: 0.5775\n      n_full: 397\n      n_cond: 251\n- exp_id: exp_018_llama_scierc_seed456_r1024\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_greedy_f1: 0.6597\n    ner_oracle_f1: 0.7683\n    ner_oracle_headroom: 0.1086\n    ner_cond_rho_fk: 0.1472\n    ner_cond_rho_sj: 0.2718\n    ner_cond_rho_logprob: 0.083\n    ner_logprob_auroc_cond: 0.5485\n    re_greedy_f1: 0.4338\n    re_oracle_f1: 0.5834\n    re_oracle_headroom: 0.1496\n    re_cond_rho_fk: 0.2107\n    re_cond_rho_sj: 0.3898\n    re_cond_rho_logprob: 0.1252\n    re_logprob_auroc_cond: 0.6119\n    ner_structural_beats_logprob: true\n    re_structural_beats_logprob: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T09:36:21.575Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T09:36:21.575Z",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T09:36:21.600Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Free-form 恢复 logprob variance 但 selection 提升有限；constrained decoding 是贡献因素之一但非唯一瓶颈
核心假设：['exp-018: logprob within-sample variance 有 2-4x 提升（range 中位数 0.10-0.20），方向正确但非压倒性', 'exp-018: free-form logprob selection 优于 greedy +1~3pp，但统计显著性边缘（p=0.05-0.15）', 'parse rate 75-90%，可用样本量较 constrained 减少 10-25%', 'NER 上方向清晰，RE 上 free-form 改善不明显（RE 的 bottleneck 可能多源）', '存在 confound：free-form 输出的 parsing noise 引入额外误差']
关键指标范围：{'freeform_parse_rate': [0.75, 0.9], 'freeform_logprob_within_sample_range_median': [0.1, 0.2], 'freeform_logprob_rho_with_f1': [0.25, 0.35], 'freeform_logprob_selection_delta_vs_greedy_pp': [1.0, 3.0], 'freeform_logprob_selection_p_value': [0.05, 0.15], 'freeform_logprob_auroc': [0.6, 0.65], 'constrained_logprob_rho_with_f1': [0.2, 0.21], 'constrained_logprob_auroc': [0.57, 0.58], 'expected_reviewer_score': [3.0, 3.5], 'findings_acceptance_prob': [0.3, 0.5]}
叙事方向：需将 "experimentally verify" 软化为 "provide evidence consistent with"。 Claim 1 从 "constrained decoding IS the bottleneck" 调整为 "constrained decoding CONTRIBUTES TO the bottleneck, as evidenced by partial recovery of logprob discrimination under free-form generation"。 补充讨论：score compression 是必要条件但非充分条件，IE 输出的组合复杂性 (entity set 的高维离散空间) 是独立于 decoding regime 的额外困难。 论文贡献权重重新分配：Claim 2 (QE framework, AUROC 0.75) 升级为 co-primary contribution， 与 Claim 1 (partial bottleneck diagnosis) 并列。 Title 调整为 "Confidence Signals Predict but Cannot Select in Constrained-Decoding Information Extraction"（去掉 "Bottleneck" 的因果暗示）。 需要额外补充 exp-019 simple verifier 或 non-tied subset 扩展分析来充实论文。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: struct_self_consist_ie
venue: EMNLP 2026 Findings
focus: Paper has been reframed from "systematic comparison + negative finding" to "identifying, diagnosing, and experimentally verifying a regime-specific selection bottleneck caused by constrained decoding". The breakthrough experiment is free-form decoding ablation (exp-018) that proves score compression is the mechanism. Evaluate whether this reframing + new experiment breaks through the 3.0/5 plateau to 3.5+. Key question: does the constrained decoding bottleneck story have enough intellectual depth for Findings acceptance?

## paper_framing.md

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

## experiment_plan (with registry status)

- id: exp-012
  name: baseline_logprob
  claim: 1
  description: 'Compute sequence log-probability for all existing pilot samples (SciERC
    NER+RE) and new dataset pilots. Correlate log-prob with F1 (ρ, AUROC, τ). If SJ
    does NOT beat log-prob, the 16x inference cost is unjustified and paper contribution
    weakens drastically. THIS IS THE MAKE-OR-BREAK EXPERIMENT.

    '
  priority: P0
  gpu_budget_hours: 3
  deps: []
  note: 'Needs vLLM forward pass to extract log-probs from existing samples. ~1h per
    dataset on 1 GPU. For new datasets, capture log-probs during pilot inference.
    Also compute on pilot_004/005 existing data if log-probs weren''t saved.

    '
  registry_id: exp_012_logprob_baseline
  status: DONE
  conclusion: success
  metrics:
    ner_full_rho_sj: 0.3565
    ner_full_rho_fk: 0.2651
    ner_full_rho_logprob: 0.1396
    ner_full_rho_greedy_logprob: 0.1615
    ner_full_tau_sj: 0.2658
    ner_full_tau_logprob: 0.1006
    ner_full_auroc_sj: 0.6892
    ner_full_auroc_fk: 0.6292
    ner_full_auroc_logprob: 0.5907
    ner_full_n: 529
    ner_sj_vs_logprob_delta: 0.2169
    re_full_rho_sj: 0.2112
    re_full_rho_fk: 0.2528
    re_full_rho_logprob: 0.2467
    re_full_auroc_sj: 0.5916
    re_full_auroc_fk: 0.6262
    re_full_auroc_logprob: 0.6186
    re_full_n: 397
    re_cond_rho_sj: 0.3683
    re_cond_rho_fk: 0.3168
    re_cond_rho_logprob: 0.1457
    re_cond_auroc_sj: 0.6839
    re_cond_auroc_logprob: 0.5487
    re_cond_n: 296
    diagnosis: 'NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead.
      RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.'
- id: exp-013
  name: baseline_exact_match
  claim: 1
  description: 'Exact-match voting rate: what fraction of N samples produce identical
    entity/relation sets? Correlate with F1. This is the direct analogue of Wang et
    al.''s original self-consistency for structured outputs.

    '
  priority: P0
  gpu_budget_hours: 0
  deps: []
  note: CPU-only on existing pilot data. Zero cost.
  registry_id: exp_013_exact_match_voting
  status: DONE
  conclusion: negative
  metrics:
    ner_full_rho: 0.2941
    ner_full_p: 5.12e-12
    ner_full_tau: 0.2181
    ner_full_auroc: 0.6398
    re_full_rho: 0.1562
    re_full_p: 0.0018
    re_full_tau: 0.1185
    re_full_auroc: 0.5863
    diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.
- id: exp-014
  name: baseline_entity_voting
  claim: 1
  description: 'Entity-level majority voting: for each entity, count how many of N
    samples include it. Select entities above threshold. Compare F1 of entity-voting
    selection vs SJ selection vs FK selection.

    '
  priority: P0
  gpu_budget_hours: 0
  deps: []
  note: CPU-only on existing pilot data. Zero cost.
  registry_id: exp_014_entity_majority_voting
  status: DONE
  conclusion: success
  metrics:
    ner_full_rho: 0.3915
    ner_full_p: 8.1e-21
    ner_full_tau: 0.2906
    ner_full_auroc: 0.7039
    re_full_rho: 0.3403
    re_full_p: 3.21e-12
    re_full_tau: 0.256
    re_full_auroc: 0.6668
    ner_voting_f1: 0.6246
    ner_greedy_f1: 0.6483
    ner_oracle_f1: 0.7793
    re_voting_f1: 0.3577
    re_greedy_f1: 0.4022
    re_oracle_f1: 0.5886
    diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE
      (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.
- id: exp-015
  name: evaluation_metrics_expansion
  claim: 1
  description: 'Add AUROC (binary: good/bad output at threshold), calibration plots,
    and Kendall''s τ alongside Spearman ρ for ALL confidence signals (SJ, FK, log-prob,
    exact-match, entity-voting) on ALL datasets. Also add leave-one-out SJ as robustness
    check for evaluation circularity.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-012
  - exp-013
  - exp-014
  note: CPU-only analysis. Addresses Dream concerns D5 (single metric) and D17 (circularity).
  registry_id: exp_015_metrics_expansion
  status: DONE
  conclusion: success
  metrics:
    data_source: exp_012_logprob/samples_with_logprobs.jsonl
    config: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2
    ner:
      n_valid: 529
      n_cond: 501
      voting_rho_full: 0.5018
      voting_rho_cond: 0.4497
      voting_auroc: 0.7279
      voting_tau: 0.3766
      sj_rho_full: 0.3565
      sj_rho_cond: 0.412
      sj_auroc: 0.6656
      sj_tau: 0.2658
      em_rho_full: 0.2566
      em_rho_cond: 0.3427
      em_auroc: 0.623
      em_tau: 0.1924
      fk_rho_full: 0.2651
      fk_rho_cond: 0.306
      fk_auroc: 0.6243
      fk_tau: 0.2027
      logprob_rho_full: 0.1396
      logprob_rho_cond: 0.1627
      logprob_auroc: 0.5585
      logprob_tau: 0.1006
    re:
      n_valid: 397
      n_cond: 296
      voting_rho_full: 0.4217
      voting_rho_cond: 0.463
      voting_auroc: 0.7162
      voting_tau: 0.327
      sj_rho_full: 0.2112
      sj_rho_cond: 0.3683
      sj_auroc: 0.5816
      sj_tau: 0.1619
      em_rho_full: 0.1002
      em_rho_cond: 0.3607
      em_auroc: 0.5036
      em_tau: 0.0839
      fk_rho_full: 0.2528
      fk_rho_cond: 0.3168
      fk_auroc: 0.6308
      fk_tau: 0.1967
      logprob_rho_full: 0.2467
      logprob_rho_cond: 0.1457
      logprob_auroc: 0.6354
      logprob_tau: 0.1808
    diagnosis: 'Unified 5-signal evaluation on single data source. Voting leads NER
      full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals
      beat logprob on NER. RE: voting leads both full and cond.'
- id: exp-001
  name: ner_n16_scierc
  claim: 1
  description: 'NER N=16 on SciERC (ft_002_v2 model). Strengthen rho estimation, test
    N-scaling. Run with seeds [42, 123, 456] for robustness. MUST capture log-probs
    during inference for exp-012.

    '
  priority: P0
  gpu_budget_hours: 18
  deps: []
  dataset: SciERC
  model: ft_002_v2
  note: 3 seeds × 6h each. Inference script MUST output log-probs.
  registry_id: exp_001_ner_n16_scierc
  status: DONE
  conclusion: success
  metrics:
    n_instances: 551
    ner_n: 529
    re_n: 397
    N: 16
    T: 1
    seed: 42
    full_test_set: true
    ner_voting_conf_rho: 0.399
    ner_sj_rho: 0.398
    ner_em_rho: 0.339
    ner_fk_rho: 0.288
    ner_logprob_rho: 0.237
    ner_voting_conf_auroc: 0.704
    ner_sj_auroc: 0.697
    ner_cond_em_rho: 0.414
    ner_cond_sj_rho: 0.349
    ner_cond_vc_rho: 0.34
    re_voting_conf_rho: 0.38
    re_logprob_rho: 0.293
    re_fk_rho: 0.281
    re_sj_rho: 0.277
    re_em_rho: 0.148
    re_voting_conf_auroc: 0.699
    re_cond_em_rho: 0.475
    re_cond_sj_rho: 0.318
    re_cond_vc_rho: 0.35
    re_cond_em_auroc: 0.742
    diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380).
      EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full
      FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact of
      200 instances + T=0.7.'
- id: exp-002
  name: ner_conll2003
  claim: 1
  description: 'Fine-tune Qwen3-8B on CoNLL-2003 (LoRA) + NER pilot (N=8, T=0.7).
    Cross-dataset generalization. MUST capture log-probs. Use consistent N and T with
    other datasets.

    '
  priority: P0
  gpu_budget_hours: 8
  deps: []
  dataset: CoNLL-2003
  model: qwen3-8b (new fine-tune)
  registry_id: exp_002_ner_conll2003
  status: DONE
  conclusion: success
- id: exp-003
  name: ner_wnut17
  claim: 1
  description: 'Fine-tune Qwen3-8B on WNUT-17 (LoRA) + NER pilot (N=8, T=0.7). Social
    media domain — cross-dataset generalization. MUST capture log-probs.

    '
  priority: P0
  gpu_budget_hours: 10
  deps: []
  dataset: WNUT-17
  model: qwen3-8b (new fine-tune)
  note: User confirmed public datasets only. D043/D045 abandoned — 54% F1=0, SJ rho
    not significant. Provides Claim 3 negative evidence.
  registry_id: exp_003_wnut17_v2_infer
  status: orphaned
- id: exp-004
  name: re_diagnostic_analysis
  claim: 2
  description: 'Per-relation-type consistency breakdown on existing pilot_004/005
    data. Error propagation patterns. Bootstrap CI for ALL rho comparisons. Add conditional
    threshold sensitivity analysis (vary exclusion criterion). Compare ALL confidence
    signals (SJ, FK, log-prob, exact-match) on RE.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-012
  - exp-013
  note: CPU-only. Bootstrap CI + threshold sensitivity address Dream concerns.
  registry_id: exp_004_re_diagnostic
  status: DONE
  conclusion: success
  metrics:
    per_relation_type:
      HYPONYM-OF:
        n: 36
        rho_sj: 0.545
        rho_fk: 0.646
        rho_vc: 0.628
        mean_f1: 0.513
      CONJUNCTION:
        n: 86
        rho_sj: 0.383
        rho_fk: 0.35
        rho_vc: 0.484
        mean_f1: 0.48
      USED-FOR:
        n: 299
        rho_sj: 0.236
        rho_fk: 0.255
        rho_vc: 0.286
        mean_f1: 0.422
      PART-OF:
        n: 44
        rho_sj: 0.239
        rho_fk: 0.348
        rho_vc: 0.283
        mean_f1: 0.297
      EVALUATE-FOR:
        n: 62
        rho_sj: 0.172
        rho_fk: 0.255
        rho_vc: 0.226
        mean_f1: 0.365
      COMPARE:
        n: 35
        rho_sj: 0.168
        rho_fk: 0.184
        rho_vc: 0.18
        mean_f1: 0.453
      FEATURE-OF:
        n: 50
        rho_sj: 0.004
        rho_fk: 0.052
        rho_vc: 0.014
        mean_f1: 0.254
    error_propagation:
      total_fn: 553
      tail_error_pct: 21.9
      full_error_pct: 21.7
      head_error_pct: 17.7
      head_tail_error_pct: 15.9
      type_error_pct: 8.3
      worst_consistency: head_type_error (sj=0.411)
      best_consistency: head_error (sj=0.613)
    threshold_sensitivity:
      thr_0.00_rho_sj: 0.3161
      thr_0.00_rho_vc: 0.3841
      thr_0.00_n: 313
      thr_0.05_rho_sj: 0.2682
      thr_0.05_rho_vc: 0.2364
      thr_0.05_n: 239
    bootstrap_ci_95:
      ner_sj:
      - 0.2946
      - 0.4586
      ner_voting_conf:
      - 0.3048
      - 0.4656
      re_sj:
      - 0.1422
      - 0.3391
      re_voting_conf:
      - 0.1818
      - 0.3721
      re_cond_sj:
      - 0.2161
      - 0.4102
      re_cond_voting_conf:
      - 0.2825
      - 0.474
    fisher_z_ner_vs_re:
      sj_z: 2.31
      sj_p: 0.0209
      sj_significant: true
      fk_z: -0.31
      fk_p: 0.756
      fk_significant: false
      voting_z: 1.914
      voting_p: 0.0556
      voting_significant: false
    diagnosis: FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF
      strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of
      RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE
      signal in conditional set (rho=0.384).
- id: exp-005
  name: temperature_sensitivity_analysis
  claim: 2
  description: 'T=0.7 vs T=1.0 comparison on both NER and RE for ALL confidence signals.
    Signal-noise tradeoff analysis.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-012
  note: CPU-only on existing pilot_004 (T=1.0) and pilot_005 (T=0.7) data.
  registry_id: exp_005
  status: DONE
  conclusion: success
- id: exp-006
  name: adaptive_compute_demo
  claim: 1
  description: 'Best-of-N selection on NER: SJ vs log-prob vs FK vs exact-match vs
    random vs greedy. Report on ALL NER datasets (not just SciERC). Include RE results
    too (even if negative).

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-001
  - exp-012
  note: CPU-only. Must cover all datasets and include RE for completeness.
  registry_id: exp_006_v2
  status: DONE
  conclusion: negative
  metrics:
    NER_SciERC_s42:
      greedy: 0.618
      oracle: 0.787
      SJ: 0.62
      logprob: 0.621
      FK: 0.621
      EM: 0.606
      voting_conf: 0.585
      random: 0.586
    NER_SciERC_s123:
      greedy: 0.618
      oracle: 0.785
      SJ: 0.617
      logprob: 0.618
      FK: 0.621
      EM: 0.613
      voting_conf: 0.584
      random: 0.583
    NER_CoNLL:
      greedy: 0.725
      oracle: 0.757
      SJ: 0.718
      logprob: 0.716
      FK: 0.717
      EM: 0.716
      voting_conf: 0.714
      random: 0.692
    RE_SciERC:
      greedy: 0.403
      oracle: 0.631
      SJ: 0.397
      logprob: 0.41
      FK: 0.396
      EM: 0.381
      voting_conf: 0.408
      random: 0.364
- id: exp-007
  name: ner_multi_model
  claim: 1
  description: 'NER pilot with LLaMA-3.1-8B-Instruct on SciERC. Model-agnostic validation.
    MUST capture log-probs for baseline comparison.

    '
  priority: P0
  gpu_budget_hours: 15
  deps: []
  dataset: SciERC
  model: llama-3.1-8b (new fine-tune)
  registry_id: exp_007_llama_inference
  status: DONE
  conclusion: success
  metrics:
    ner:
      greedy_f1: 0.66
      oracle_f1: 0.781
      headroom: 0.121
      rho_fk: 0.327
      rho_sj: 0.363
      rho_fk_cond: 0.226
      rho_sj_cond: 0.311
      rho_logprob: 0.183
      rho_logprob_cond: 0.109
      structural_beats_surface: true
      sample_f1_pct_zero: 11.6
    re:
      greedy_f1: 0.434
      oracle_f1: 0.568
      headroom: 0.135
      rho_fk: 0.305
      rho_sj: 0.299
      rho_fk_cond: 0.259
      rho_sj_cond: 0.405
      rho_logprob: 0.288
      rho_logprob_cond: 0.092
      structural_beats_surface: false
      sample_f1_pct_zero: 41.2
    n_instances: 551
    N: 8
    T: 1
    seed: 42
    model: LLaMA-3.1-8B-Instruct
    verdict: FAIL
    verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0
- id: exp-008
  name: re_n16_confirmation
  claim: 2
  description: 'RE N=16 on SciERC to confirm negative finding with higher statistical
    power.

    '
  priority: P1
  gpu_budget_hours: 12
  deps: []
  dataset: SciERC
  model: ft_002_v2
  registry_id: exp_008_re_n16
  status: DONE
  conclusion: success
  metrics:
    ner:
      greedy_f1: 0.6635
      oracle_f1: 0.8208
      headroom: 0.1572
      rho_sj_full: 0.377
      rho_fk_full: 0.2508
      rho_logprob_full: 0.3153
      rho_sj_cond: 0.3598
      rho_fk_cond: 0.2251
      rho_logprob_cond: 0.2927
      sj_beats_fk: true
      rho_advantage: 0.1262
    re:
      greedy_f1: 0.4339
      oracle_f1: 0.6658
      headroom: 0.2319
      rho_sj_full: 0.2966
      rho_fk_full: 0.2871
      rho_logprob_full: 0.2986
      rho_sj_cond: 0.3975
      rho_fk_cond: 0.3774
      rho_logprob_cond: 0.2745
      sj_beats_fk: true
      rho_advantage: 0.0095
    verdict: FAIL
- id: exp-009
  name: capability_stratification
  claim: 2
  description: 'Stratify instances by difficulty (greedy F1 buckets + independent
    proxies: sentence length, entity count) for both NER and RE. Verify inverted-U
    pattern with proper statistical tests and independent stratification variable.

    '
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  note: CPU-only. Dream flagged inverted-U overclaiming — use independent proxy.
  registry_id: exp_009_capability_stratification
  status: DONE
  conclusion: success
  metrics:
    scierc_ner:
      n: 551
      sj_rho_overall: 0.398
      by_greedy_f1:
        hard_0_25_sj_rho: 0.159
        med_low_sj_rho: 0.139
        med_high_sj_rho: 0.09
        easy_sj_rho: 0.23
      by_sent_len:
        Q1_sj_rho: 0.461
        Q2_sj_rho: 0.401
        Q3_sj_rho: 0.296
        Q4_sj_rho: 0.382
      by_ent_count:
        0_sj_rho: 0.689
        1_2_sj_rho: 0.415
        3_5_sj_rho: 0.353
        6plus_sj_rho: 0.547
    scierc_re:
      n: 551
      by_greedy_f1:
        hard_0_25_sj_rho: -0.043
        easy_sj_rho: 0.21
      by_sent_len:
        Q1_sj_rho: 0.447
        Q4_sj_rho: 0.54
      by_rel_count:
        0_sj_rho: 0.62
        1_2_sj_rho: 0.275
        6plus_sj_rho: 0.527
    conll_ner:
      n: 3453
      by_sent_len:
        Q1_sj_rho: 0.334
        Q3_sj_rho: 0.518
    proxy_independence:
      scierc_ner_f1_vs_slen: -0.021
      scierc_ner_f1_vs_ecnt: 0.007
      scierc_re_f1_vs_slen: -0.147
- id: exp-010
  name: selection_curves
  claim: 1
  description: 'Best-of-N selection curves for N=1,2,4,8,16 comparing all confidence
    signals. Visualize as line plots (not just tables — Dream flagged table-only presentation).

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - exp-001
  - exp-012
  note: CPU-only visualization
  registry_id: exp_010_selection_curves
  status: DONE
  conclusion: success
  metrics:
    scierc_ner:
      n_instances: 551
      greedy_f1: 0.618
      N16:
        oracle: 0.787
        SJ: 0.62
        FK: 0.621
        logprob: 0.621
        voting_conf: 0.585
        EM: 0.606
        random: 0.595
      N8:
        oracle: 0.752
        SJ: 0.614
        FK: 0.614
        logprob: 0.619
        voting_conf: 0.591
        EM: 0.603
        random: 0.589
      N4:
        oracle: 0.714
        SJ: 0.607
        FK: 0.608
        logprob: 0.616
        voting_conf: 0.594
        EM: 0.6
        random: 0.587
    scierc_re:
      n_instances: 397
      greedy_f1: 0.403
      N16:
        oracle: 0.631
        SJ: 0.397
        FK: 0.396
        logprob: 0.41
        voting_conf: 0.408
        EM: 0.381
        random: 0.364
      N8:
        oracle: 0.583
        SJ: 0.393
        FK: 0.394
        logprob: 0.413
        voting_conf: 0.398
        EM: 0.381
        random: 0.363
    conll_ner:
      n_instances: 3453
      greedy_f1: 0.725
      N8:
        oracle: 0.757
        SJ: 0.718
        FK: 0.717
        logprob: 0.716
        voting_conf: 0.714
        EM: 0.716
        random: 0.69
      N4:
        oracle: 0.746
        SJ: 0.714
        FK: 0.714
        logprob: 0.715
        voting_conf: 0.714
        EM: 0.712
        random: 0.692
- id: exp-011
  name: ner_ood_robustness
  claim: 1
  description: 'Test NER consistency signal on OOD instances (cross-domain transfer).

    '
  priority: P2
  gpu_budget_hours: 5
  deps:
  - exp-003
  status: planned
- id: exp-016
  name: signal_ensemble_analysis
  claim: 1
  description: 'SJ+logprob instance-level correlation and ensemble analysis. (1) Pearson/Spearman
    correlation between SJ and logprob per-instance. (2) Grid search linear combination
    alpha*SJ + (1-alpha)*logprob. (3) Logistic regression on all 5 signals as ensemble.
    (4) Best-of-N selection F1 for ensemble vs individual signals. Dream 2 reviewers
    BOTH independently flagged this as missing.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-012
  - exp-014
  note: CPU-only on existing pilot_004 data. Zero cost, high impact.
  registry_id: exp_016_signal_ensemble
  status: DONE
  conclusion: success
  metrics:
    sj_logprob_pearson_ner: 0.57
    sj_logprob_pearson_re: 0.42
    best_linear_ner:
      combo: SJ+voting_conf
      alpha: 0.3
      rho: 0.489
    best_linear_re:
      combo: voting_conf+logprob
      alpha: 0.6
      rho: 0.429
    ensemble_ner_auroc: 0.735
    ensemble_re_auroc: 0.719
    best_single_ner_auroc: 0.7
    best_single_re_auroc: 0.721
    ensemble_ner_delta: 0.035
    selection_f1_ner:
      greedy: 0.609
      logprob: 0.609
      sj: 0.604
      ensemble: 0.604
      voting: 0.596
      random: 0.58
      oracle: 0.769
    selection_f1_re:
      logprob: 0.397
      greedy: 0.374
      sj: 0.368
      ensemble: 0.367
      voting: 0.338
      random: 0.338
      oracle: 0.561
    diagnosis: 'SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best
      is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER.
      Oracle gap still huge.'
- id: exp-017
  name: ner_llama_conll
  claim: 1
  description: 'LLaMA-3.1-8B on CoNLL-2003 to strengthen cross-model validation. Dream
    2 flagged LLaMA only on SciERC is insufficient for model-agnostic claim.

    '
  priority: P1
  gpu_budget_hours: 10
  deps:
  - exp-007
  dataset: CoNLL-2003
  model: llama-3.1-8b (fine-tune on CoNLL)
  note: Only if exp-007 shows positive signal and GPU hours available.
  status: planned
- id: exp-018
  name: freeform_decoding_ablation
  claim: 1
  description: 'BREAKTHROUGH EXPERIMENT (D070). Free-form decoding ablation on SciERC
    NER+RE using Qwen3-8B. Remove Outlines constrained decoding, generate 8 free-form
    samples per instance. Compare logprob variance, selection performance, and QE
    metrics between constrained vs free-form. This is the controlled experiment that
    proves whether the correlation-selection gap is caused by constrained decoding
    (regime-specific) or inherent to structured IE (universal). If free-form recovers
    logprob selection → paper becomes about regime-specific bottleneck (much stronger).
    If gap persists → universal finding (also stronger).

    '
  priority: P0
  gpu_budget_hours: 4
  deps: []
  dataset: SciERC
  model: qwen3-8b (existing fine-tuned checkpoint)
  note: '529 NER + 397 RE instances × 8 samples = ~4200 generations. 8B model on RTX
    5090 ≈ 1-2h inference. Parse rate expected 80-95% (fine-tuned model learned JSON
    format). Analysis on parseable subset. Key metrics: (a) logprob within-sample
    variance (constrained vs free), (b) selection F1 (constrained vs free), (c) QE
    ρ/AUROC (constrained vs free).

    '
  status: planned
- id: exp-019
  name: simple_verifier_baseline
  claim: 1
  description: 'P1 EXPERIMENT. Train a simple supervised verifier (DeBERTa or 8B classification
    head) on existing (input, output, F1) data. If verifier partially closes the selection
    gap, it proves the gap IS closable and transforms the negative finding into an
    actionable one with an upper bound on unsupervised methods.

    '
  priority: P1
  gpu_budget_hours: 8
  deps:
  - exp-018
  dataset: SciERC
  model: DeBERTa-v3-large or Qwen3-8B classifier
  note: 'Only if exp-018 done and time permits before DDL. Training data: existing
    N=8 samples with F1 labels. ~1 day implementation + training + evaluation.

    '
  status: planned


## registry (completed experiments)

- exp_id: ft_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.1099
    eval_loss: 0.0771
    gate0_ner_f1_strict: 0.1143
    gate0_re_f1_strict: 0.0125
    gate0_ner_f1_text: 0.606
    gate0_re_f1_text: 0.3392
    gate0_offset_accuracy: 0.1665
    gate0_parse_failures: 43
    gate0_pass: false
    gate0_realigned_ner_f1: 0.6045
    gate0_realigned_re_f1: 0.338
    gate0_realigned_entity_offset_accuracy: 1
    gate0_realigned_relation_offset_accuracy: 1
    gate0_realigned_ner_pass: true
    gate0_realigned_re_pass: false
    gate0_realigned_pass: false
    gate0_ner_f1_delta_realign: 0.4901
    gate0_re_f1_delta_realign: 0.3255
    verdict_note: 'partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)'
- exp_id: mvp_pilot_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ner_greedy_f1: 0.611
    ner_oracle_f1: 0.78
    ner_headroom: 0.169
    ner_fleiss_kappa_mean: 0.2449
    ner_soft_jaccard_mean: 0.5041
    ner_full_rho_sj: 0.3616
    ner_full_rho_fk: 0.3515
    ner_full_n: 529
    ner_cond_rho_sj: 0.3688
    ner_cond_rho_fk: 0.3569
    ner_cond_n: 510
    ner_sj_beats_fk_full: true
    ner_sj_beats_fk_cond: true
    ner_sample_f1_pct_zero: 20.4
    ner_gold_empty_filtered: 22
    ner_all_zero_filtered: 19
    re_greedy_f1: 0.355
    re_oracle_f1: 0.572
    re_headroom: 0.217
    re_fleiss_kappa_mean: 0.0681
    re_soft_jaccard_mean: 0.3635
    re_full_rho_sj: 0.2535
    re_full_rho_fk: 0.2885
    re_full_n: 397
    re_cond_rho_sj: 0.3515
    re_cond_rho_fk: 0.3107
    re_cond_n: 320
    re_sj_beats_fk_full: false
    re_sj_beats_fk_cond: true
    re_sample_f1_pct_zero: 58.3
    re_gold_empty_filtered: 154
    re_all_zero_filtered: 77
    parse_failures_stochastic: 164
    parse_failures_greedy: 29
    total_stochastic_samples: 4408
    total_greedy: 551
    verdict: FAIL
    verdict_reason: RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set
- exp_id: ft_002
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    last_step: 70
    total_steps: 585
    progress_pct: 11.97
    last_loss: 0.1134
    last_lr: 0.00019982
    elapsed: 3m32s
    failure_reason: OOM at step 73, batch_size=4 too large for 32GB RTX 5090
- exp_id: mvp_pilot_002
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_pilot_003
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ner_greedy_f1: 0.6362
    ner_oracle_f1: 0.792
    ner_headroom: 0.1559
    ner_fleiss_kappa_mean: 0.2488
    ner_soft_jaccard_mean: 0.5066
    ner_full_rho_sj: 0.3808
    ner_full_rho_fk: 0.3362
    ner_full_p_sj: 1.07e-19
    ner_full_p_fk: 1.93e-15
    ner_full_n: 529
    ner_cond_rho_sj: 0.3836
    ner_cond_rho_fk: 0.3187
    ner_cond_p_sj: 1.83e-19
    ner_cond_p_fk: 1.33e-13
    ner_cond_n: 514
    ner_sj_beats_fk_full: true
    ner_sj_beats_fk_cond: true
    ner_rho_advantage: 0.0446
    ner_sample_f1_mean: 0.5153
    ner_sample_f1_std: 0.3334
    ner_sample_f1_pct_zero: 19.9
    ner_gold_empty_filtered: 22
    ner_all_zero_filtered: 15
    re_greedy_f1: 0.3774
    re_oracle_f1: 0.5939
    re_headroom: 0.2165
    re_fleiss_kappa_mean: 0.0879
    re_soft_jaccard_mean: 0.3958
    re_full_rho_sj: 0.2367
    re_full_rho_fk: 0.2221
    re_full_p_sj: 1.85e-06
    re_full_p_fk: 7.92e-06
    re_full_n: 397
    re_cond_rho_sj: 0.3004
    re_cond_rho_fk: 0.2374
    re_cond_p_sj: 2.25e-08
    re_cond_p_fk: 1.19e-05
    re_cond_n: 333
    re_sj_beats_fk_full: true
    re_sj_beats_fk_cond: true
    re_rho_advantage: 0.0146
    re_sample_f1_mean: 0.1977
    re_sample_f1_std: 0.3251
    re_sample_f1_pct_zero: 67.6
    re_gold_empty_filtered: 154
    re_all_zero_filtered: 64
    parse_failures_stochastic: 0
    parse_failures_greedy: 0
    total_stochastic_samples: 4408
    total_greedy: 551
    verdict: FAIL
    verdict_reason: RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but
      below PASS bar
- exp_id: ft_002_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    epoch: 5
    train_loss: 0.0806
    eval_loss: 0.089
    train_runtime: 28m41s
    train_samples_per_second: 5.407
    train_steps_per_second: 0.34
    total_steps: 585
    checkpoints:
    - checkpoint-400
    - checkpoint-500
    - checkpoint-585
    gate0_final_ner_f1: 0.6615
    gate0_final_re_f1: 0.4177
    gate0_final_parse_failures: 0
    gate0_final_ner_pass: true
    gate0_final_re_pass: true
    gate0_final_pass: true
    gate0_ckpt400_ner_f1: 0.6475
    gate0_ckpt400_re_f1: 0.3793
    gate0_ckpt400_parse_failures: 0
    gate0_ckpt400_verdict: FAIL
    gate0_ckpt400_re_sample_f1_pct_zero: 58.8
    gate0_ckpt400_warning: '>30% samples F1=0'
- exp_id: mvp_pilot_004
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ner_greedy_f1: 0.6671
    ner_oracle_f1: 0.7756
    ner_headroom: 0.1085
    ner_fleiss_kappa_mean: 0.4048
    ner_soft_jaccard_mean: 0.7008
    ner_full_rho_fk: 0.259
    ner_full_rho_sj: 0.3825
    ner_full_n: 529
    ner_cond_rho_fk: 0.2352
    ner_cond_rho_sj: 0.3762
    ner_cond_n: 508
    ner_sj_beats_fk_full: true
    ner_sj_beats_fk_cond: true
    ner_sample_f1_mean: 0.6084
    ner_sample_f1_std: 0.3174
    ner_sample_f1_pct_zero: 12.19
    ner_gold_empty_filtered: 22
    ner_all_zero_filtered: 21
    re_greedy_f1: 0.4208
    re_oracle_f1: 0.5882
    re_headroom: 0.1674
    re_fleiss_kappa_mean: 0.2996
    re_soft_jaccard_mean: 0.6114
    re_full_rho_fk: 0.2782
    re_full_rho_sj: 0.2441
    re_full_n: 397
    re_cond_rho_fk: 0.3067
    re_cond_rho_sj: 0.3161
    re_cond_n: 313
    re_sj_beats_fk_full: false
    re_sj_beats_fk_cond: true
    re_sample_f1_mean: 0.3612
    re_sample_f1_std: 0.383
    re_sample_f1_pct_zero: 44.3
    re_gold_empty_filtered: 154
    re_all_zero_filtered: 84
    parse_failures: 0
    verdict: FAIL
- exp_id: mvp_pilot_005
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ner_greedy_f1: 0.6619
    ner_oracle_f1: 0.7585
    ner_headroom: 0.0966
    ner_fleiss_kappa_mean: 0.4722
    ner_soft_jaccard_mean: 0.7757
    ner_full_rho_sj: 0.3875
    ner_full_rho_fk: 0.3211
    ner_full_n: 529
    ner_cond_rho_sj: 0.3868
    ner_cond_rho_fk: 0.305
    ner_cond_n: 504
    ner_sj_beats_fk_full: true
    ner_sj_beats_fk_cond: true
    ner_rho_advantage: 0.0664
    ner_sample_f1_mean: 0.6243
    ner_sample_f1_std: 0.3131
    ner_sample_f1_pct_zero: 11.2
    ner_gold_empty_filtered: 22
    ner_all_zero_filtered: 25
    re_greedy_f1: 0.4219
    re_oracle_f1: 0.5532
    re_headroom: 0.1313
    re_fleiss_kappa_mean: 0.3829
    re_soft_jaccard_mean: 0.687
    re_full_rho_sj: 0.2343
    re_full_rho_fk: 0.1835
    re_full_n: 397
    re_cond_rho_sj: 0.3716
    re_cond_rho_fk: 0.2533
    re_cond_n: 301
    re_sj_beats_fk_full: true
    re_sj_beats_fk_cond: true
    re_rho_advantage: 0.0508
    re_sample_f1_mean: 0.3782
    re_sample_f1_std: 0.3845
    re_sample_f1_pct_zero: 42.4
    re_gold_empty_filtered: 154
    re_all_zero_filtered: 96
    parse_failures: 0
    verdict: FAIL
    verdict_note: RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional
      but not full threshold
- exp_id: e1_component_wise_re_sj
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    full_head_sj_rho: 0.21
    full_tail_sj_rho: 0.201
    full_type_match_rho: 0.201
    full_multiplicative_rho: 0.244
    full_additive_rho: 0.243
    full_fleiss_kappa_rho: 0.278
    cond_head_sj_rho: 0.27
    cond_tail_sj_rho: 0.259
    cond_type_match_rho: 0.252
    cond_multiplicative_rho: 0.316
    cond_additive_rho: 0.306
    cond_fleiss_kappa_rho: 0.307
    n_full: 397
    n_conditional: 313
    diagnosis: 'head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis
      REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for
      RE.'
- exp_id: exp_012_logprob_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner_full_rho_sj: 0.3565
    ner_full_rho_fk: 0.2651
    ner_full_rho_logprob: 0.1396
    ner_full_rho_greedy_logprob: 0.1615
    ner_full_tau_sj: 0.2658
    ner_full_tau_logprob: 0.1006
    ner_full_auroc_sj: 0.6892
    ner_full_auroc_fk: 0.6292
    ner_full_auroc_logprob: 0.5907
    ner_full_n: 529
    ner_sj_vs_logprob_delta: 0.2169
    re_full_rho_sj: 0.2112
    re_full_rho_fk: 0.2528
    re_full_rho_logprob: 0.2467
    re_full_auroc_sj: 0.5916
    re_full_auroc_fk: 0.6262
    re_full_auroc_logprob: 0.6186
    re_full_n: 397
    re_cond_rho_sj: 0.3683
    re_cond_rho_fk: 0.3168
    re_cond_rho_logprob: 0.1457
    re_cond_auroc_sj: 0.6839
    re_cond_auroc_logprob: 0.5487
    re_cond_n: 296
    diagnosis: 'NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead.
      RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.'
- exp_id: exp_013_exact_match_voting
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ner_full_rho: 0.2941
    ner_full_p: 5.12e-12
    ner_full_tau: 0.2181
    ner_full_auroc: 0.6398
    re_full_rho: 0.1562
    re_full_p: 0.0018
    re_full_tau: 0.1185
    re_full_auroc: 0.5863
    diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.
- exp_id: exp_014_entity_majority_voting
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner_full_rho: 0.3915
    ner_full_p: 8.1e-21
    ner_full_tau: 0.2906
    ner_full_auroc: 0.7039
    re_full_rho: 0.3403
    re_full_p: 3.21e-12
    re_full_tau: 0.256
    re_full_auroc: 0.6668
    ner_voting_f1: 0.6246
    ner_greedy_f1: 0.6483
    ner_oracle_f1: 0.7793
    re_voting_f1: 0.3577
    re_greedy_f1: 0.4022
    re_oracle_f1: 0.5886
    diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE
      (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.
- exp_id: exp_001_ner_n16_scierc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_instances: 551
    ner_n: 529
    re_n: 397
    N: 16
    T: 1
    seed: 42
    full_test_set: true
    ner_voting_conf_rho: 0.399
    ner_sj_rho: 0.398
    ner_em_rho: 0.339
    ner_fk_rho: 0.288
    ner_logprob_rho: 0.237
    ner_voting_conf_auroc: 0.704
    ner_sj_auroc: 0.697
    ner_cond_em_rho: 0.414
    ner_cond_sj_rho: 0.349
    ner_cond_vc_rho: 0.34
    re_voting_conf_rho: 0.38
    re_logprob_rho: 0.293
    re_fk_rho: 0.281
    re_sj_rho: 0.277
    re_em_rho: 0.148
    re_voting_conf_auroc: 0.699
    re_cond_em_rho: 0.475
    re_cond_sj_rho: 0.318
    re_cond_vc_rho: 0.35
    re_cond_em_auroc: 0.742
    diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380).
      EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full
      FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact of
      200 instances + T=0.7.'
- exp_id: exp_002_ner_conll2003
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_003_ner_wnut17
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ner:
      greedy_f1: 0.525
      oracle_f1: 0.664
      headroom: 0.139
      rho_sj_full: 0.082
      rho_fk_full: 0.124
      rho_logprob_full: -0.414
      rho_sj_cond: 0.275
      rho_fk_cond: 0.164
      rho_logprob_cond: 0.352
      sj_beats_logprob_cond: false
    n_instances: 1287
    n_gold_empty: 598
    sample_f1_mean: 0.401
    sample_f1_pct_zero: 53.7
    N: 16
    T: 1
    seed: 42
    verdict: FAIL
    verdict_note: '>30% samples F1=0; structural rho weak; logprob baseline stronger'
- exp_id: exp_007_ner_multi_model
  name: ''
  status: DONE
  conclusion: success
  metrics:
    epoch: 5
    train_loss: 0.0767
    eval_loss: 0.1049
    train_runtime_sec: 1494.5
    train_samples_per_second: 6.226
    checkpoints:
    - checkpoint-400
    - checkpoint-500
    - checkpoint-585
    base_model: Meta-Llama-3.1-8B-Instruct
    lora_r: 32
    lora_alpha: 64
    note: EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal.
      Checkpoint fully intact.
- exp_id: exp_007_ner_llama
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_005
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_015_metrics_expansion
  name: ''
  status: DONE
  conclusion: success
  metrics:
    data_source: exp_012_logprob/samples_with_logprobs.jsonl
    config: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2
    ner:
      n_valid: 529
      n_cond: 501
      voting_rho_full: 0.5018
      voting_rho_cond: 0.4497
      voting_auroc: 0.7279
      voting_tau: 0.3766
      sj_rho_full: 0.3565
      sj_rho_cond: 0.412
      sj_auroc: 0.6656
      sj_tau: 0.2658
      em_rho_full: 0.2566
      em_rho_cond: 0.3427
      em_auroc: 0.623
      em_tau: 0.1924
      fk_rho_full: 0.2651
      fk_rho_cond: 0.306
      fk_auroc: 0.6243
      fk_tau: 0.2027
      logprob_rho_full: 0.1396
      logprob_rho_cond: 0.1627
      logprob_auroc: 0.5585
      logprob_tau: 0.1006
    re:
      n_valid: 397
      n_cond: 296
      voting_rho_full: 0.4217
      voting_rho_cond: 0.463
      voting_auroc: 0.7162
      voting_tau: 0.327
      sj_rho_full: 0.2112
      sj_rho_cond: 0.3683
      sj_auroc: 0.5816
      sj_tau: 0.1619
      em_rho_full: 0.1002
      em_rho_cond: 0.3607
      em_auroc: 0.5036
      em_tau: 0.0839
      fk_rho_full: 0.2528
      fk_rho_cond: 0.3168
      fk_auroc: 0.6308
      fk_tau: 0.1967
      logprob_rho_full: 0.2467
      logprob_rho_cond: 0.1457
      logprob_auroc: 0.6354
      logprob_tau: 0.1808
    diagnosis: 'Unified 5-signal evaluation on single data source. Voting leads NER
      full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals
      beat logprob on NER. RE: voting leads both full and cond.'
- exp_id: exp_004_re_diagnostic
  name: ''
  status: DONE
  conclusion: success
  metrics:
    per_relation_type:
      HYPONYM-OF:
        n: 36
        rho_sj: 0.545
        rho_fk: 0.646
        rho_vc: 0.628
        mean_f1: 0.513
      CONJUNCTION:
        n: 86
        rho_sj: 0.383
        rho_fk: 0.35
        rho_vc: 0.484
        mean_f1: 0.48
      USED-FOR:
        n: 299
        rho_sj: 0.236
        rho_fk: 0.255
        rho_vc: 0.286
        mean_f1: 0.422
      PART-OF:
        n: 44
        rho_sj: 0.239
        rho_fk: 0.348
        rho_vc: 0.283
        mean_f1: 0.297
      EVALUATE-FOR:
        n: 62
        rho_sj: 0.172
        rho_fk: 0.255
        rho_vc: 0.226
        mean_f1: 0.365
      COMPARE:
        n: 35
        rho_sj: 0.168
        rho_fk: 0.184
        rho_vc: 0.18
        mean_f1: 0.453
      FEATURE-OF:
        n: 50
        rho_sj: 0.004
        rho_fk: 0.052
        rho_vc: 0.014
        mean_f1: 0.254
    error_propagation:
      total_fn: 553
      tail_error_pct: 21.9
      full_error_pct: 21.7
      head_error_pct: 17.7
      head_tail_error_pct: 15.9
      type_error_pct: 8.3
      worst_consistency: head_type_error (sj=0.411)
      best_consistency: head_error (sj=0.613)
    threshold_sensitivity:
      thr_0.00_rho_sj: 0.3161
      thr_0.00_rho_vc: 0.3841
      thr_0.00_n: 313
      thr_0.05_rho_sj: 0.2682
      thr_0.05_rho_vc: 0.2364
      thr_0.05_n: 239
    bootstrap_ci_95:
      ner_sj:
      - 0.2946
      - 0.4586
      ner_voting_conf:
      - 0.3048
      - 0.4656
      re_sj:
      - 0.1422
      - 0.3391
      re_voting_conf:
      - 0.1818
      - 0.3721
      re_cond_sj:
      - 0.2161
      - 0.4102
      re_cond_voting_conf:
      - 0.2825
      - 0.474
    fisher_z_ner_vs_re:
      sj_z: 2.31
      sj_p: 0.0209
      sj_significant: true
      fk_z: -0.31
      fk_p: 0.756
      fk_significant: false
      voting_z: 1.914
      voting_p: 0.0556
      voting_significant: false
    diagnosis: FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF
      strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of
      RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE
      signal in conditional set (rho=0.384).
- exp_id: exp_008_re_n16
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner:
      greedy_f1: 0.6635
      oracle_f1: 0.8208
      headroom: 0.1572
      rho_sj_full: 0.377
      rho_fk_full: 0.2508
      rho_logprob_full: 0.3153
      rho_sj_cond: 0.3598
      rho_fk_cond: 0.2251
      rho_logprob_cond: 0.2927
      sj_beats_fk: true
      rho_advantage: 0.1262
    re:
      greedy_f1: 0.4339
      oracle_f1: 0.6658
      headroom: 0.2319
      rho_sj_full: 0.2966
      rho_fk_full: 0.2871
      rho_logprob_full: 0.2986
      rho_sj_cond: 0.3975
      rho_fk_cond: 0.3774
      rho_logprob_cond: 0.2745
      sj_beats_fk: true
      rho_advantage: 0.0095
    verdict: FAIL
- exp_id: exp001_seed123
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp001_seed456
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp008_re_n16
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_001_n16_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner:
      greedy_f1: 0.655
      oracle_f1: 0.8028
      headroom: 0.1478
      rho_sj_full: 0.4076
      rho_fk_full: 0.2799
      rho_logprob_full: 0.3189
      rho_sj_cond: 0.4271
      rho_fk_cond: 0.2743
      rho_logprob_cond: 0.2835
      sj_beats_fk: true
      rho_advantage: 0.1277
    re:
      greedy_f1: 0.4243
      oracle_f1: 0.6771
      headroom: 0.2528
      rho_sj_full: 0.2943
      rho_fk_full: 0.2657
      rho_logprob_full: 0.3005
      rho_sj_cond: 0.4003
      rho_fk_cond: 0.313
      rho_logprob_cond: 0.2317
      sj_beats_fk: true
      rho_advantage: 0.0286
    verdict: FAIL
- exp_id: exp_001_n16_seed456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner:
      greedy_f1: 0.6577
      oracle_f1: 0.8129
      headroom: 0.1553
      rho_sj_full: 0.3297
      rho_fk_full: 0.2578
      rho_logprob_full: 0.2866
      rho_sj_cond: 0.3394
      rho_fk_cond: 0.2721
      rho_logprob_cond: 0.2567
      sj_beats_fk: true
      rho_advantage: 0.0719
    re:
      greedy_f1: 0.4312
      oracle_f1: 0.6737
      headroom: 0.2425
      rho_sj_full: 0.285
      rho_fk_full: 0.2372
      rho_logprob_full: 0.2626
      rho_sj_cond: 0.3525
      rho_fk_cond: 0.2614
      rho_logprob_cond: 0.1927
      sj_beats_fk: true
      rho_advantage: 0.0478
    verdict: FAIL
- exp_id: exp_016_signal_ensemble
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sj_logprob_pearson_ner: 0.57
    sj_logprob_pearson_re: 0.42
    best_linear_ner:
      combo: SJ+voting_conf
      alpha: 0.3
      rho: 0.489
    best_linear_re:
      combo: voting_conf+logprob
      alpha: 0.6
      rho: 0.429
    ensemble_ner_auroc: 0.735
    ensemble_re_auroc: 0.719
    best_single_ner_auroc: 0.7
    best_single_re_auroc: 0.721
    ensemble_ner_delta: 0.035
    selection_f1_ner:
      greedy: 0.609
      logprob: 0.609
      sj: 0.604
      ensemble: 0.604
      voting: 0.596
      random: 0.58
      oracle: 0.769
    selection_f1_re:
      logprob: 0.397
      greedy: 0.374
      sj: 0.368
      ensemble: 0.367
      voting: 0.338
      random: 0.338
      oracle: 0.561
    diagnosis: 'SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best
      is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER.
      Oracle gap still huge.'
- exp_id: exp_002_merge_conll2003
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_002
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sj_rho_full: 0.4357
    sj_tau_full: 0.3851
    sj_auroc_full: 0.8008
    sj_rho_cond: 0.4511
    fk_rho_full: 0.3998
    fk_tau_full: 0.3568
    fk_auroc_full: 0.7741
    fk_rho_cond: 0.4064
    logprob_rho_full: 0.3157
    logprob_tau_full: 0.2469
    logprob_auroc_full: 0.7532
    logprob_rho_cond: 0.3562
    em_rho_full: 0.4507
    em_tau_full: 0.4002
    em_auroc_full: 0.8156
    em_rho_cond: 0.4799
    ev_rho_full: 0.4237
    ev_tau_full: 0.3777
    ev_auroc_full: 0.7889
    ev_rho_cond: 0.4127
    greedy_f1: 0.9123
    oracle_f1: 0.9543
    voting_f1: 0.9141
    oracle_headroom: 0.042
    sj_vs_logprob_delta_rho: 0.12
    sj_vs_logprob_ci_low: 0.0881
    sj_vs_logprob_ci_high: 0.154
    sj_vs_logprob_significant: true
    n_instances: 3453
    n_valid: 2756
    n_samples: 8
    temperature: 1
- exp_id: exp_001_n16_seed123_full
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_001_n16_seed456_full
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_008_re_n16_full
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_ner_n16_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner:
      greedy_f1: 0.663
      oracle_f1: 0.809
      headroom: 0.146
      rho_sj: 0.423
      rho_fk: 0.29
      rho_logprob: 0.239
      rho_sj_cond: 0.423
      rho_fk_cond: 0.26
    re:
      greedy_f1: 0.419
      oracle_f1: 0.625
      headroom: 0.206
      rho_sj: 0.267
      rho_fk: 0.315
      rho_sj_cond: 0.364
      rho_fk_cond: 0.331
    verdict: FAIL
    verdict_note: RE rho_sj=0.267 < 0.40; RE >30% samples F1=0
    n_instances: 551
    seed: 123
    N: 16
    T: 1
- exp_id: exp_001_seed456_t10_full
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ner:
      rho_sj: 0.414
      rho_fk: 0.298
    re:
      rho_sj: 0.268
      rho_fk: 0.26
    n_instances: 551
    N: 16
    T: 1
    seed: 456
    source: reviewer_verified_report_json
- exp_id: exp_001_seed123_t10_full
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ner:
      rho_sj: 0.417
      rho_fk: 0.283
    re:
      rho_sj: 0.265
      rho_fk: 0.315
    n_instances: 551
    N: 16
    T: 1
    seed: 123
    source: reviewer_verified_report_json
- exp_id: exp_008_re_n16_t10_full
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ner:
      rho_sj: 0.444
    re:
      rho_sj: 0.248
    n_instances: 551
    N: 16
    T: 1
    seed: 42
    mode: RE-only
    source: director_corrected
- exp_id: exp_003_wnut17_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    greedy_f1: 0.523
    oracle_f1: 0.664
    headroom: 0.141
    rho_fk: 0.125
    rho_sj: 0.089
    rho_fk_cond: 0.169
    rho_sj_cond: 0.288
    rho_logprob_full: -0.409
    rho_logprob_cond: 0.35
    structural_beats_surface: false
    sample_f1_pct_zero: 53.7
    n_instances: 1287
    N: 16
    T: 1
    seed: 42
    model: Qwen3-8B
    n_gold_empty_filtered: 598
    verdict: FAIL
    verdict_note: structural_beats_surface=false; >50% samples F1=0
- exp_id: exp_007_llama_inference
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner:
      greedy_f1: 0.66
      oracle_f1: 0.781
      headroom: 0.121
      rho_fk: 0.327
      rho_sj: 0.363
      rho_fk_cond: 0.226
      rho_sj_cond: 0.311
      rho_logprob: 0.183
      rho_logprob_cond: 0.109
      structural_beats_surface: true
      sample_f1_pct_zero: 11.6
    re:
      greedy_f1: 0.434
      oracle_f1: 0.568
      headroom: 0.135
      rho_fk: 0.305
      rho_sj: 0.299
      rho_fk_cond: 0.259
      rho_sj_cond: 0.405
      rho_logprob: 0.288
      rho_logprob_cond: 0.092
      structural_beats_surface: false
      sample_f1_pct_zero: 41.2
    n_instances: 551
    N: 8
    T: 1
    seed: 42
    model: LLaMA-3.1-8B-Instruct
    verdict: FAIL
    verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0
- exp_id: exp_001_seed42_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sj_rho_full: 0.428
    sj_rho_cond: 0.369
    structural_minus_surface: 0.147
    conclusion_note: NER seed42 robustness confirmed, structural>surface +0.147
- exp_id: exp_001_seed123_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sj_rho_full: 0.424
    sj_rho_cond: 0.376
    structural_minus_surface: 0.149
    conclusion_note: NER seed123 robustness confirmed, structural>surface +0.149
- exp_id: exp_008_re_n16_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    sj_rho_full: 0.281
    sj_rho_cond: 0.308
    f1_zero_pct: 44.3
    conclusion_note: 'RE N=16 v2 negative: SJ weak, 44.3% F1=0'
- exp_id: exp_017_llama_conll
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_009_capability_stratification
  name: ''
  status: DONE
  conclusion: success
  metrics:
    scierc_ner:
      n: 551
      sj_rho_overall: 0.398
      by_greedy_f1:
        hard_0_25_sj_rho: 0.159
        med_low_sj_rho: 0.139
        med_high_sj_rho: 0.09
        easy_sj_rho: 0.23
      by_sent_len:
        Q1_sj_rho: 0.461
        Q2_sj_rho: 0.401
        Q3_sj_rho: 0.296
        Q4_sj_rho: 0.382
      by_ent_count:
        0_sj_rho: 0.689
        1_2_sj_rho: 0.415
        3_5_sj_rho: 0.353
        6plus_sj_rho: 0.547
    scierc_re:
      n: 551
      by_greedy_f1:
        hard_0_25_sj_rho: -0.043
        easy_sj_rho: 0.21
      by_sent_len:
        Q1_sj_rho: 0.447
        Q4_sj_rho: 0.54
      by_rel_count:
        0_sj_rho: 0.62
        1_2_sj_rho: 0.275
        6plus_sj_rho: 0.527
    conll_ner:
      n: 3453
      by_sent_len:
        Q1_sj_rho: 0.334
        Q3_sj_rho: 0.518
    proxy_independence:
      scierc_ner_f1_vs_slen: -0.021
      scierc_ner_f1_vs_ecnt: 0.007
      scierc_re_f1_vs_slen: -0.147
- exp_id: exp_010_selection_curves
  name: ''
  status: DONE
  conclusion: success
  metrics:
    scierc_ner:
      n_instances: 551
      greedy_f1: 0.618
      N16:
        oracle: 0.787
        SJ: 0.62
        FK: 0.621
        logprob: 0.621
        voting_conf: 0.585
        EM: 0.606
        random: 0.595
      N8:
        oracle: 0.752
        SJ: 0.614
        FK: 0.614
        logprob: 0.619
        voting_conf: 0.591
        EM: 0.603
        random: 0.589
      N4:
        oracle: 0.714
        SJ: 0.607
        FK: 0.608
        logprob: 0.616
        voting_conf: 0.594
        EM: 0.6
        random: 0.587
    scierc_re:
      n_instances: 397
      greedy_f1: 0.403
      N16:
        oracle: 0.631
        SJ: 0.397
        FK: 0.396
        logprob: 0.41
        voting_conf: 0.408
        EM: 0.381
        random: 0.364
      N8:
        oracle: 0.583
        SJ: 0.393
        FK: 0.394
        logprob: 0.413
        voting_conf: 0.398
        EM: 0.381
        random: 0.363
    conll_ner:
      n_instances: 3453
      greedy_f1: 0.725
      N8:
        oracle: 0.757
        SJ: 0.718
        FK: 0.717
        logprob: 0.716
        voting_conf: 0.714
        EM: 0.716
        random: 0.69
      N4:
        oracle: 0.746
        SJ: 0.714
        FK: 0.714
        logprob: 0.715
        voting_conf: 0.714
        EM: 0.712
        random: 0.692
- exp_id: exp_007_llama_seed123
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    verdict: FAIL
    ner:
      greedy_f1: 0.6605
      oracle_f1: 0.7703
      headroom: 0.1098
      fleiss_kappa: 0.4553
      soft_jaccard: 0.7525
      rho_kappa_f1: 0.2143
      rho_sj_f1: 0.3371
      structural_gt_surface: true
    re:
      greedy_f1: 0.433
      oracle_f1: 0.5719
      headroom: 0.1389
      fleiss_kappa: 0.3851
      soft_jaccard: 0.6911
      rho_kappa_f1: 0.2844
      rho_sj_f1: 0.268
      structural_gt_surface: false
    fail_reasons:
    - RE rho_sj=0.2680 < 0.40 threshold
    - '>30% samples F1=0 (RE: 41.0%)'
    - RE structural not > surface (delta=-0.0165)
- exp_id: exp_007_llama_seed456
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    verdict: FAIL
    ner:
      greedy_f1: 0.6597
      oracle_f1: 0.7575
      oracle_headroom: 0.0978
      fleiss_kappa: 0.4543
      soft_jaccard: 0.7491
      rho_kappa_f1: 0.3115
      rho_sj_f1: 0.3663
      structural_gt_surface: true
    re:
      greedy_f1: 0.4334
      oracle_f1: 0.5789
      oracle_headroom: 0.1455
      fleiss_kappa: 0.3791
      soft_jaccard: 0.6782
      rho_kappa_f1: 0.3013
      rho_sj_f1: 0.287
      structural_gt_surface: false
    logprob_ner:
      rho: 0.1911
      auroc: 0.5989
    logprob_re:
      rho: 0.3246
      auroc: 0.6678
    fail_reason: RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0
- exp_id: exp_008_re_seed123
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    greedy_f1: 0.4229
    oracle_f1: 0.6244
    oracle_headroom: 0.2015
    fleiss_kappa_mean: 0.3455
    soft_jaccard_mean: 0.6126
    sample_f1_mean: 0.3594
    sample_f1_std: 0.3793
    sample_f1_zero_pct: 44.1
    structural_gt_surface: false
    rho_kappa_f1_full: 0.3174
    rho_sj_f1_full: 0.2835
    rho_kappa_f1_cond: 0.0766
    rho_sj_f1_cond: 0.2877
    logprob_auroc_full: 0.6499
    logprob_auroc_cond: 0.5265
    verdict: FAIL
- exp_id: exp_005_v2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_006_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    NER_SciERC_s42:
      greedy: 0.618
      oracle: 0.787
      SJ: 0.62
      logprob: 0.621
      FK: 0.621
      EM: 0.606
      voting_conf: 0.585
      random: 0.586
    NER_SciERC_s123:
      greedy: 0.618
      oracle: 0.785
      SJ: 0.617
      logprob: 0.618
      FK: 0.621
      EM: 0.613
      voting_conf: 0.584
      random: 0.583
    NER_CoNLL:
      greedy: 0.725
      oracle: 0.757
      SJ: 0.718
      logprob: 0.716
      FK: 0.717
      EM: 0.716
      voting_conf: 0.714
      random: 0.692
    RE_SciERC:
      greedy: 0.403
      oracle: 0.631
      SJ: 0.397
      logprob: 0.41
      FK: 0.396
      EM: 0.381
      voting_conf: 0.408
      random: 0.364
- exp_id: exp_004_v2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_003_wnut17_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: exp_015_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    scierc_ner_avg:
      sj_auroc: 0.7394
      fk_auroc: 0.6172
      em_auroc: 0.7873
      voting_auroc: 0.7367
      logprob_auroc: 0.5918
    scierc_re_avg:
      sj_auroc: 0.6746
      fk_auroc: 0.5939
      em_auroc: 0.715
      voting_auroc: 0.7234
      logprob_auroc: 0.5849
- exp_id: exp_009_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner_seed42_global:
      sj_rho: 0.431
      fk_rho: 0.325
      logprob_rho: 0.203
      voting_conf_rho: 0.475
      em_rho: 0.292
    ner_seed123_global:
      sj_rho: 0.422
      fk_rho: 0.315
      logprob_rho: 0.226
      voting_conf_rho: 0.438
      em_rho: 0.299
    re_seed42_global:
      sj_rho: 0.063
      fk_rho: 0.226
      logprob_rho: 0.4
      voting_conf_rho: 0.22
      em_rho: -0.132
    ner_seed_stability_max_delta: 0.037
    independent_proxies:
    - sent_len
    - ent_count
    - type_diversity
    inverted_u_ner: not confirmed (ρ stable across independent proxies)
    inverted_u_re: monotonic increase with complexity, not inverted-U
- exp_id: exp_001_seed456_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: exp_016_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner_conditional:
      n: 529
      best_single_signal_rho:
        soft_jaccard: 0.4412
      best_combo_rho:
        sj+vc_a0.55: 0.4552
      ensemble_auroc: 0.7141
      best_single_auroc:
        soft_jaccard: 0.7166
      selection_f1:
        greedy: 0.6442
        logprob_best: 0.6505
        ensemble_best: 0.6475
        sj_best: 0.6471
        oracle: 0.8442
    re_conditional:
      n: 397
      best_single_signal_rho:
        voting_confidence: 0.3849
      best_combo_rho:
        logprob+vc_a0.25: 0.3936
      ensemble_auroc: 0.6916
      best_single_auroc:
        voting_confidence: 0.7023
      selection_f1:
        greedy: 0.403
        logprob_best: 0.4097
        ensemble_best: 0.4227
        oracle: 0.6306
    re_full:
      ensemble_auroc: 0.8608
      best_single_auroc:
        voting_confidence: 0.8248
- exp_id: exp_001_seed456_v2_ner
  name: ''
  status: DONE
  conclusion: success
  metrics:
    full:
      SJ:
        rho: 0.384
        auroc: 0.711
      FK:
        rho: 0.223
        auroc: 0.577
      logprob:
        rho: 0.232
        auroc: 0.594
      EM:
        rho: 0.316
        auroc: 0.768
      voting_conf:
        rho: 0.411
        auroc: 0.712
    conditional:
      SJ:
        rho: 0.349
        auroc: 0.699
      FK:
        rho: 0.157
        auroc: 0.561
      logprob:
        rho: 0.171
        auroc: 0.576
      EM:
        rho: 0.406
        auroc: 0.78
      voting_conf:
        rho: 0.346
        auroc: 0.694
    3seed_mean_SJ_rho_full: 0.412
    3seed_sd_SJ_rho_full: 0.025
    structural_beats_surface: true
    verdict: MARGINAL
- exp_id: exp_017_llama_conll_infer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    greedy_f1: 0.9266
    oracle_f1: 0.9443
    oracle_headroom: 0.0177
    n_instances: 3453
    n_valid: 2756
    n_conditional: 2642
    N: 8
    full:
      SJ_rho: 0.4314
      FK_rho: 0.4277
      logprob_rho: 0.3072
      EM_rho: 0.4306
      voting_conf_rho: 0.4256
      SJ_AUROC: 0.7039
      FK_AUROC: 0.7026
      logprob_AUROC: 0.761
      EM_AUROC: 0.7046
      voting_conf_AUROC: 0.7088
      SJ_ECE: 0.1137
      FK_ECE: 0.1053
      logprob_ECE: 0.129
      EM_ECE: 0.1094
      voting_conf_ECE: 0.0949
    conditional:
      SJ_rho: 0.4356
      FK_rho: 0.431
      logprob_rho: 0.3282
      EM_rho: 0.4403
      voting_conf_rho: 0.3743
      SJ_AUROC: 0.7225
      FK_AUROC: 0.7208
      logprob_AUROC: 0.8102
      EM_AUROC: 0.7257
      voting_conf_AUROC: 0.6989
      SJ_ECE: 0.0829
      FK_ECE: 0.0796
      logprob_ECE: 0.0922
      EM_ECE: 0.0754
      voting_conf_ECE: 0.0784
- exp_id: exp_002_conll_n16
  name: ''
  status: DONE
  conclusion: success
  metrics:
    N: 16
    dataset: conll2003
    subtask: ner
    n_instances: 3453
    n_valid: 2756
    n_conditional: 2614
    greedy_f1: 0.907
    full:
      SJ_rho: 0.4496
      FK_rho: 0.3928
      logprob_rho: 0.3146
      EM_rho: 0.4627
      voting_conf_rho: 0.4286
      SJ_AUROC: 0.8264
      FK_AUROC: 0.7821
      logprob_AUROC: 0.7531
      EM_AUROC: 0.8409
      voting_conf_AUROC: 0.8071
      SJ_ECE: 0.0747
      FK_ECE: 0.1786
      logprob_ECE: 0.2031
      EM_ECE: 0.0786
      voting_conf_ECE: 0.529
    conditional:
      SJ_rho: 0.4208
      FK_rho: 0.3494
      logprob_rho: 0.3756
      EM_rho: 0.4658
      voting_conf_rho: 0.3654
      SJ_AUROC: 0.8405
      FK_AUROC: 0.7819
      logprob_AUROC: 0.8259
      EM_AUROC: 0.8781
      voting_conf_AUROC: 0.7951
      SJ_ECE: 0.0982
      FK_ECE: 0.1899
      logprob_ECE: 0.2504
      EM_ECE: 0.0997
      voting_conf_ECE: 0.6096
    n8_vs_n16_delta_rho_full:
      SJ: 0.0139
      FK: -0.007
      logprob: -0.0011
      EM: 0.012
      voting_conf: 0.0049
- exp_id: exp_007_llama_n16
  name: ''
  status: DONE
  conclusion: success
  metrics:
    N: 16
    dataset: scierc
    subtask: ner
    n_instances: 551
    n_valid: 529
    n_conditional: 478
    greedy_f1: 0.645
    full:
      SJ_rho: 0.3791
      FK_rho: 0.3081
      logprob_rho: 0.2041
      EM_rho: 0.3159
      voting_conf_rho: 0.4515
      SJ_AUROC: 0.717
      FK_AUROC: 0.6581
      logprob_AUROC: 0.5656
      EM_AUROC: 0.7686
      voting_conf_AUROC: 0.7266
      SJ_ECE: 0.1019
      FK_ECE: 0.1556
      logprob_ECE: 0.084
      EM_ECE: 0.1761
      voting_conf_ECE: 0.1365
    conditional:
      SJ_rho: 0.3222
      FK_rho: 0.2182
      logprob_rho: 0.1286
      EM_rho: 0.3563
      voting_conf_rho: 0.3356
      SJ_AUROC: 0.7014
      FK_AUROC: 0.6392
      logprob_AUROC: 0.545
      EM_AUROC: 0.7708
      voting_conf_AUROC: 0.6988
      SJ_ECE: 0.1466
      FK_ECE: 0.1853
      logprob_ECE: 0.1141
      EM_ECE: 0.1887
      voting_conf_ECE: 0.2634
    n8_vs_n16_delta_rho_full:
      SJ: 0.0161
      FK: -0.0185
      logprob: 0.0214
      EM: 0.0007
      voting_conf: 0.0184
- exp_id: exp_009_v2_re_rerun
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_017_llama_conll_n16
  name: ''
  status: DONE
  conclusion: success
  metrics:
    greedy_f1: 0.9243
    oracle_f1: 0.9487
    oracle_headroom: 0.0244
    n_instances: 3453
    n_valid: 2756
    n_conditional: 2642
    structural_beats_surface: true
    full:
      SJ_rho: 0.4642
      SJ_AUROC: 0.7391
      SJ_ECE: 0.1131
      FK_rho: 0.4566
      FK_AUROC: 0.736
      FK_ECE: 0.1071
      logprob_rho: 0.3058
      logprob_AUROC: 0.7594
      logprob_ECE: 0.1288
      EM_rho: 0.4613
      EM_AUROC: 0.7391
      EM_ECE: 0.1084
      voting_conf_rho: 0.4554
      voting_conf_AUROC: 0.7406
      voting_conf_ECE: 0.0844
    conditional:
      SJ_rho: 0.4597
      SJ_AUROC: 0.7565
      SJ_ECE: 0.0846
      FK_rho: 0.4515
      FK_AUROC: 0.753
      FK_ECE: 0.0813
      logprob_rho: 0.3193
      logprob_AUROC: 0.8023
      logprob_ECE: 0.0921
      EM_rho: 0.4618
      EM_AUROC: 0.7589
      EM_ECE: 0.0757
      voting_conf_rho: 0.3978
      voting_conf_AUROC: 0.7287
      voting_conf_ECE: 0.0742
    best_of_n:
      greedy: 0.9243
      random_avg: 0.9213
      sj_best: 0.9259
      logprob_best: 0.925
      voting_conf_best: 0.9268
      oracle: 0.9487
    n8_vs_n16_delta:
      full_SJ_rho_delta: 0.0328
      full_FK_rho_delta: 0.0289
      full_logprob_rho_delta: -0.0014
      full_EM_rho_delta: 0.0307
      full_voting_conf_rho_delta: 0.0298
      cond_SJ_rho_delta: 0.0241
      cond_FK_rho_delta: 0.0205
      cond_logprob_rho_delta: -0.0089
      cond_EM_rho_delta: 0.0215
      cond_voting_conf_rho_delta: 0.0235
- exp_id: exp_017_llama_conll_n16_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    greedy_f1: 0.9266
    oracle_f1: 0.9497
    oracle_headroom: 0.0231
    n_instances: 3453
    n_valid: 2756
    n_conditional: 2642
    structural_beats_surface: true
    full:
      SJ_rho: 0.4698
      SJ_AUROC: 0.7402
      SJ_ECE: 0.1135
      FK_rho: 0.4594
      FK_AUROC: 0.7351
      FK_ECE: 0.1114
      logprob_rho: 0.3161
      logprob_AUROC: 0.768
      logprob_ECE: 0.129
      EM_rho: 0.4676
      EM_AUROC: 0.7399
      EM_ECE: 0.1082
      voting_conf_rho: 0.4612
      voting_conf_AUROC: 0.7429
      voting_conf_ECE: 0.0832
    conditional:
      SJ_rho: 0.4712
      SJ_AUROC: 0.7609
      SJ_ECE: 0.0828
      FK_rho: 0.4595
      FK_AUROC: 0.7547
      FK_ECE: 0.0858
      logprob_rho: 0.3314
      logprob_AUROC: 0.8134
      logprob_ECE: 0.0922
      EM_rho: 0.4732
      EM_AUROC: 0.7626
      EM_ECE: 0.075
      voting_conf_rho: 0.4086
      voting_conf_AUROC: 0.7338
      voting_conf_ECE: 0.0706
    best_of_n:
      greedy: 0.9242
      random_avg: 0.9216
      sj_best: 0.9247
      logprob_best: 0.9253
      voting_conf_best: 0.9255
      oracle: 0.9486
    n8_vs_n16_delta:
      full_SJ_rho_delta: 0.0384
      full_FK_rho_delta: 0.0317
      full_logprob_rho_delta: 0.0089
      full_SJ_AUROC_delta: 0.0363
      full_FK_AUROC_delta: 0.0325
      full_logprob_AUROC_delta: 0.007
      cond_SJ_rho_delta: 0.0356
      cond_FK_rho_delta: 0.0285
      cond_logprob_rho_delta: 0.0032
- exp_id: exp_017_llama_conll_n16_s456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    greedy_f1: 0.9243
    oracle_f1: 0.9488
    oracle_headroom: 0.0245
    n_instances: 3453
    n_valid: 2756
    n_conditional: 2642
    structural_beats_surface: true
    full:
      SJ_rho: 0.4552
      SJ_AUROC: 0.7288
      SJ_ECE: 0.1134
      FK_rho: 0.4478
      FK_AUROC: 0.7248
      FK_ECE: 0.109
      logprob_rho: 0.3078
      logprob_AUROC: 0.7612
      logprob_ECE: 0.1289
      EM_rho: 0.452
      EM_AUROC: 0.7275
      EM_ECE: 0.1082
      voting_conf_rho: 0.4571
      voting_conf_AUROC: 0.7348
      voting_conf_ECE: 0.0863
    conditional:
      SJ_rho: 0.4505
      SJ_AUROC: 0.7449
      SJ_ECE: 0.0826
      FK_rho: 0.4422
      FK_AUROC: 0.7401
      FK_ECE: 0.0835
      logprob_rho: 0.3242
      logprob_AUROC: 0.8067
      logprob_ECE: 0.0921
      EM_rho: 0.451
      EM_AUROC: 0.745
      EM_ECE: 0.0756
      voting_conf_rho: 0.3962
      voting_conf_AUROC: 0.7202
      voting_conf_ECE: 0.0746
    best_of_n:
      greedy: 0.9243
      random_avg: 0.9215
      sj_best: 0.9243
      logprob_best: 0.9243
      voting_conf_best: 0.9243
      oracle: 0.9488
    n8_vs_n16_delta:
      full_SJ_rho_delta: 0.0238
      full_FK_rho_delta: 0.0201
      full_logprob_rho_delta: 0.0006
      full_EM_rho_delta: 0.0214
      full_voting_conf_rho_delta: 0.0315
      cond_SJ_rho_delta: 0.0149
      cond_FK_rho_delta: 0.0112
      cond_logprob_rho_delta: -0.004
      cond_EM_rho_delta: 0.0107
      cond_voting_conf_rho_delta: 0.0219
- exp_id: exp_012_rerun_1024
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner_full:
      n: 529
      SJ:
        rho: 0.3599
        tau: 0.2646
        AUROC: 0.6917
        ECE: 0.4531
        rho_ci95:
        - 0.2732
        - 0.4389
        AUROC_ci95:
        - 0.6304
        - 0.7406
      FK:
        rho: 0.2665
        tau: 0.1974
        AUROC: 0.629
        ECE: 0.4512
        rho_ci95:
        - 0.1743
        - 0.3486
        AUROC_ci95:
        - 0.5612
        - 0.6882
      logprob:
        rho: 0.2052
        tau: 0.1478
        AUROC: 0.5783
        ECE: 0.7064
        rho_ci95:
        - 0.1171
        - 0.2904
        AUROC_ci95:
        - 0.5179
        - 0.6387
      EM:
        rho: 0.2945
        tau: 0.2208
        AUROC: 0.7493
        ECE: 0.3526
        rho_ci95:
        - 0.2094
        - 0.37
        AUROC_ci95:
        - 0.7002
        - 0.7928
      voting_conf:
        rho: 0.3792
        tau: 0.2805
        AUROC: 0.6841
        ECE: 0.3807
        rho_ci95:
        - 0.2972
        - 0.4486
        AUROC_ci95:
        - 0.6249
        - 0.7366
    ner_cond:
      n: 477
      SJ:
        rho: 0.3113
        tau: 0.2257
        AUROC: 0.6772
        ECE: 0.4416
        rho_ci95:
        - 0.2353
        - 0.3959
        AUROC_ci95:
        - 0.621
        - 0.7337
      FK:
        rho: 0.1761
        tau: 0.1284
        AUROC: 0.6078
        ECE: 0.4389
        rho_ci95:
        - 0.0839
        - 0.2665
        AUROC_ci95:
        - 0.5442
        - 0.6709
      logprob:
        rho: 0.1538
        tau: 0.1111
        AUROC: 0.5633
        ECE: 0.6803
        rho_ci95:
        - 0.0637
        - 0.2424
        AUROC_ci95:
        - 0.5032
        - 0.6232
      EM:
        rho: 0.3596
        tau: 0.2735
        AUROC: 0.7556
        ECE: 0.3257
        rho_ci95:
        - 0.2819
        - 0.4408
        AUROC_ci95:
        - 0.7011
        - 0.8107
      voting_conf:
        rho: 0.3
        tau: 0.2189
        AUROC: 0.6618
        ECE: 0.3746
        rho_ci95:
        - 0.2168
        - 0.3836
        AUROC_ci95:
        - 0.6004
        - 0.7201
    re_full:
      n: 397
      SJ:
        rho: 0.2503
        tau: 0.1878
        AUROC: 0.6702
        ECE: 0.3865
      FK:
        rho: 0.2752
        tau: 0.2117
        AUROC: 0.6089
        ECE: 0.4405
      logprob:
        rho: 0.2662
        tau: 0.1951
        AUROC: 0.6005
        ECE: 0.7694
      EM:
        rho: 0.1344
        tau: 0.1081
        AUROC: 0.7059
        ECE: 0.3548
      voting_conf:
        rho: 0.3498
        tau: 0.2663
        AUROC: 0.6935
        ECE: 0.2724
    re_cond:
      n: 238
      SJ:
        rho: 0.2457
        tau: 0.1811
        AUROC: 0.6463
        ECE: 0.2941
      FK:
        rho: 0.1139
        tau: 0.0876
        AUROC: 0.551
        ECE: 0.3424
      logprob:
        rho: 0.0112
        tau: 0.0051
        AUROC: 0.5186
        ECE: 0.6464
      EM:
        rho: 0.4165
        tau: 0.3256
        AUROC: 0.7515
        ECE: 0.2232
      voting_conf:
        rho: 0.2409
        tau: 0.178
        AUROC: 0.642
        ECE: 0.207
    delta_vs_512_ner_full_rho:
      SJ: 0.0034
      FK: 0.0014
      EM: 0.0379
      voting_conf: -0.1226
      logprob: 0.0656
    provenance_note: exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512
      truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed
      0.140→0.205.
- exp_id: exp_001_seed42_v2_r1024
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    greedy_f1: 0.6647
    oracle_f1: 0.8106
    softjaccard_rho_full: 0.3928
    fleiss_rho_full: 0.2489
    logprob_rho_full: 0.2136
    softjaccard_rho_cond: 0.3455
    fleiss_rho_cond: 0.163
    logprob_rho_cond: 0.1624
    verdict: MARGINAL
- exp_id: exp_001_seed123_v2_r1024
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_001_seed456_v2_ner_r1024
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_002_conll_n16_r1024
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_007_llama_n16_r1024
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_017_llama_conll_n16_r1024
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_017_llama_conll_n16_s123_r1024
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_017_llama_conll_n16_s456_r1024
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_016_rerun_1024_bootstrap
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    bootstrap_ci_95:
    - -0.03
    - 0.042
    permutation_p: 0.39
    cohen_d: 0.038
    sign_test_win_rate: 0.466
    ner_logprob_vs_greedy_delta: 0.006
    conclusion_summary: 'NER selection: no signal significantly outperforms greedy;
      RE: same conclusion'
- exp_id: exp_018_qwen_scierc_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_018_qwen_scierc_seed456
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_018_llama_scierc_seed123
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp_018_llama_scierc_seed456
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_018_llama_scierc_seed42_r1024
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner:
      full:
        SJ:
          rho: 0.3096
          tau: 0.2288
          auroc: 0.6683
        FK:
          rho: 0.2352
          tau: 0.1759
          auroc: 0.6069
        logprob:
          rho: 0.1503
          tau: 0.1087
          auroc: 0.5318
        EM:
          rho: 0.2587
          tau: 0.1966
          auroc: 0.7174
        voting_conf:
          rho: 0.4053
          tau: 0.3042
          auroc: 0.6967
      conditional:
        SJ:
          rho: 0.2718
          tau: null
          auroc: 0.6565
        FK:
          rho: 0.1472
          tau: null
          auroc: 0.5866
        logprob:
          rho: 0.081
          tau: null
          auroc: 0.5129
        EM:
          rho: 0.3165
          tau: null
          auroc: 0.7244
        voting_conf:
          rho: 0.3078
          tau: null
          auroc: 0.6714
      greedy_f1: 0.6607
      oracle_f1: 0.7781
      n_full: 529
      n_cond: 478
    re:
      full:
        SJ:
          rho: 0.2748
          tau: 0.2102
          auroc: 0.7244
        FK:
          rho: 0.3027
          tau: 0.2337
          auroc: 0.691
        logprob:
          rho: 0.3163
          tau: 0.233
          auroc: 0.6313
        EM:
          rho: 0.1681
          tau: 0.1275
          auroc: 0.7697
        voting_conf:
          rho: 0.384
          tau: 0.2965
          auroc: 0.7337
      conditional:
        SJ:
          rho: 0.3461
          tau: null
          auroc: 0.7233
        FK:
          rho: 0.1969
          tau: null
          auroc: 0.6684
        logprob:
          rho: 0.0888
          tau: null
          auroc: 0.5556
        EM:
          rho: 0.4969
          tau: null
          auroc: 0.819
        voting_conf:
          rho: 0.3433
          tau: null
          auroc: 0.7003
      greedy_f1: 0.4319
      oracle_f1: 0.5775
      n_full: 397
      n_cond: 251
- exp_id: exp_018_llama_scierc_seed456_r1024
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ner_greedy_f1: 0.6597
    ner_oracle_f1: 0.7683
    ner_oracle_headroom: 0.1086
    ner_cond_rho_fk: 0.1472
    ner_cond_rho_sj: 0.2718
    ner_cond_rho_logprob: 0.083
    ner_logprob_auroc_cond: 0.5485
    re_greedy_f1: 0.4338
    re_oracle_f1: 0.5834
    re_oracle_headroom: 0.1496
    re_cond_rho_fk: 0.2107
    re_cond_rho_sj: 0.3898
    re_cond_rho_logprob: 0.1252
    re_logprob_auroc_cond: 0.6119
    ner_structural_beats_logprob: true
    re_structural_beats_logprob: true

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
  "promptId": "5acfa596-46d8-4777-ad4d-407c781b578e",
  "type": "user",
  "uuid": "9218a4b7-3574-4461-b95f-d5311c2c8b7a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T09:36:21.597Z_

```json
{
  "parentUuid": "9218a4b7-3574-4461-b95f-d5311c2c8b7a",
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
  "uuid": "64b75bf7-374b-45ff-8f47-5b5175e8c2f7",
  "timestamp": "2026-05-15T09:36:21.597Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T09:36:21.597Z_

```json
{
  "parentUuid": "64b75bf7-374b-45ff-8f47-5b5175e8c2f7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "82a125df-b38b-4ad4-a7b8-d801a261ec0a",
  "timestamp": "2026-05-15T09:36:21.597Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Free-form 恢复 logprob variance 但 selection 提升有限；constrained decoding 是贡献因素之一但非唯一瓶颈 核心假设：['exp-018: logprob within-sample variance 有 2-4x 提升（range 中位数 0.10…",
  "leafUuid": "82a125df-b38b-4ad4-a7b8-d801a261ec0a",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Free-form decoding ablation validates constrained bottleneck hypothesis",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89"
}
```

---

### Assistant

_source line 8 · 2026-05-15T09:38:58.068Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for all "planned" experiments in the experiment_plan, under the "median" tier definition they provided.

Let me identify the planned experiments:

1. **exp-011** (ner_ood_robustness) - status: planned
2. **exp-017** (ner_llama_conll) - status: planned — BUT wait, looking at the registry, exp_017_llama_conll_infer is DONE. Let me re-check... The experiment_plan says status: planned, but the registry has exp_017_llama_conll as DONE. So exp-017 is actually done already.


3. **exp-018** (freeform_decoding_ablation) - status: planned — BUT the registry has several exp_018 entries that are DONE. Let me check... exp_018_qwen_scierc_seed123 DONE, exp_018_qwen_scierc_seed456 DONE, exp_018_llama_scierc_seed123 DONE, exp_018_llama_scierc_seed42_r1024 DONE, exp_018_llama_scierc_seed456_r1024 DONE. So there's data for LLaMA runs but what about Qwen? The exp_018 entries for qwen have some completed runs, though I need to check if all variants are covered.

Wait, I'm realizing the actual task here — I need to focus on the experiments marked as planned in the experiment_plan itself, not just the registry entries. The user wants me to generate detailed data for those planned experiments. Looking at the plan, exp-017, exp-018, exp-019, and exp-011 are all listed as planned, so I should be creating projected data for these under the median tier, even though some registry entries show completion. I need to be careful here — even though some experiments have partial registry entries, the plan marks them as "planned," so I should generate predicted results based on the median tier assumptions. Let me work through the truly planned experiments: exp-011, exp-017, exp-018, and exp-019, constructing detailed predictions for each one using the median tier parameters like the freeform parse rate range and logprob variance recovery. Now I'm adjusting the language to be more precise—changing "verify" to "provide evidence consistent with" and reframing the first claim as contributing to a bottleneck, while elevating the QE framework to co-primary status. Looking at the experiment predictions, exp-011 on cross-domain NER robustness should follow similar degradation patterns to the weak WNUT-17 results we've seen, while exp-017 with LLaMA on CoNLL appears more straightforward since the registry already shows a rho of 0.431, suggesting the median tier prediction should align with that.

I'm noticing the plan lists exp-017 as planned but the registry shows it's already done—the plan was probably written before execution. Regardless, I need to generate predictions for all four planned experiments. For exp-018, the freeform decoding ablation, this is the critical one: I'd expect parse rates around 83% under median tier, with logprob variance recovering substantially compared to the constrained approach, though the selection improvement over greedy would likely be modest at 1-3 percentage points with borderline significance.

For exp-019, a simple verifier baseline should partially bridge the gap, though the real contribution here is demonstrating that the gap is actually closable with an unsupervised signal. Now I'll generate the full YAML output with detailed predictions for each experiment.

I should double-check the experiment registry first—exp-017 shows as planned in the user's plan but appears to already have results in the registry. I'll generate imagined data anyway since they asked for all planned experiments, being especially thorough with exp-018 since it's the key breakthrough experiment.

For the median tier metrics, I need to think through the rationales carefully. The OOD robustness test will show structural signals degrading under distributional shift since the model becomes less calibrated on out-of-domain instances. For LLaMA on CoNLL, this serves as cross-model validation on a well-studied benchmark where patterns should align with the Qwen results, though CoNLL's high baseline leaves limited headroom for improvement.

Now for exp-018, the freeform ablation—this is critical. Without grammar constraints, the fine-tuned model achieves around 83% parse rate since it learned the JSON format but outputs aren't guaranteed to be valid. The logprob variance expands significantly to a median range of ~0.15 compared to ~0.04 with constraints, and the correlation with F1 weakens to ~0.30 versus ~0.20. AUROC drops to ~0.62 from ~0.58, and best-of-N selection gains only 1.5-2 percentage points over greedy decoding instead of the 0.6pp improvement seen with constraints. The key insight is that removing structural guidance substantially degrades signal quality across the board.

For RE, the pattern is even more pronounced—parse rate falls to ~78% and logprob improvements flatten out because the bottleneck isn't just decoding format but the inherent complexity of relation extraction. Comparing constrained versus freeform directly, the within-sample logprob range explodes 3.75x, rank correlation improves by 50%, and selection gains jump from 0.6pp to 2.0pp, but parsing failures eat into the effective sample size. The evidence clearly points to constrained decoding as a meaningful contributor, though RE's minimal gains suggest it's not the only limiting factor.

Moving to exp-019, I'm looking at a simple verifier approach trained on input-output pairs using DeBERTa.

Generating YAML structure... -4x，selection 有方向性改善）但非决定性证明。
  RE 上改善不明显说明存在独立于 decoding regime 的额外瓶颈（entity set 组合复杂性）。
  Claim 2 (QE framework, AUROC 0.75) 升级为 co-primary contribution。
  Title: "Confidence Signals Predict but Cannot Select in Constrained-Decoding Information Extraction"。
  需补充 exp-019 或 non-tied subset 分析以充实论文。

imagined_experiments:
  - name: "ner_ood_robustness"
    plan_id: "exp-011"
    ...

对于 exp-011，这是在 WNUT-17 上测试 SciERC 训练模型的跨域迁移，但 WNUT-17 的基线表现很弱（SJ rho 仅 0.082），所以 OOD 场景下会看到性能下降。在中等表现层级下，结构化信号会比 logprob 更优雅地降级，SJ 在 OOD 上仍能保留一定价值（rho 约 0.15）。

现在我要完整输出预测结果，包括详细的指标表格。对于 exp-011，预计 SciERC 模型在 WNUT-17 测试集上的 NER greedy F1 约 0.35，Oracle F1 约 0.50，SJ rho 约 0.18，FK rho 约 0.12，logprob rho 约 -0.25，这支持结构化一致性信号比表面级信号更稳健的论述。

Now I'm finalizing the predictions with detailed metric tables for each experiment, including the cross-domain transfer results showing how structural signals degrade more gracefully than surface-level confidence measures. I'll provide the imagined data for the remaining planned experiments. For exp-017 with LLaMA on CoNLL, I'm seeing structural consistency metrics around 0.43 for SJ and 0.42 for FK, while logprob drops to 0.31—structural methods hold up better under the ceiling effect of the benchmark, though logprob's AUROC is slightly higher at 0.76 versus SJ's 0.70, likely because the compressed variance makes probability-based detection more effective. Moving into exp-018 on the freeform ablation...

Generating experiment predictions... Now I'm looking at the relation extraction results, which show a lower parse rate at 78% and reduced logprob correlation compared to NER, likely because the output format is more complex. The free-form approach still improves performance substantially—logprob correlation jumps from 0.205 to 0.30 and AUROC gains 4.2 percentage points—though the selection improvement of 0.8pp isn't statistically significant here.

Moving to the supervised verifier experiment, I'm training on a larger dataset with 5-fold cross-validation to prevent overfitting. For NER, the verifier achieves 0.82 AUROC and captures about 18% of the gap between greedy and oracle performance, with a correlation of 0.52. The RE verifier shows similar promise with 0.76 AUROC.

The key insight is that supervised signals like semantic alignment and entity plausibility help close the gap, but distribution shift and limited training data prevent reaching oracle performance—suggesting there's a fundamental limit to what selection alone can achieve. This gives me a useful benchmark for evaluating unsupervised methods.

Now I need to structure the YAML output carefully. The user is asking for detailed predicted data for each planned experiment with clear result_rationale explanations tied to the median tier definition. I should provide comprehensive predictions that explain why each result would fall at this performance level, including expected metrics, tables, and analysis.

For exp-017, even though it already has registry data, I'll generate predictions under the median tier framework since the user explicitly requested all planned experiments. For exp-018, I need to think through how removing the constrained decoding affects output—the model was fine-tuned for JSON, so it will still attempt structured output but with more variability and potential formatting issues. output, but without grammar constraints:

1. Some outputs will be malformed JSON → parse failures (10-25% under median tier)
2. Without grammar constraint, the model has more "freedom" in token selection → logprob scores will have more variance
3. The logprob scores will better reflect the model's actual confidence because they're not artificially compressed by the grammar constraint
4. But parsing noise introduces additional error: even if logprob correctly identifies good outputs, some of those "good" outputs may have parsing errors that reduce measured F1

Under median tier specifically:
- The variance recovery is real (2-4x) but the selection improvement is modest (+1-3pp)
- This is because: (a) even with recovered variance, logprob is still an imperfect signal for structured output quality, (b) parsing noise reduces effective sample size and introduces measurement error, (c) for RE, there are additional bottlenecks beyond decoding like entity set combinatorics and error propagation
- The evidence supports the bottleneck hypothesis but doesn't conclusively prove it, with borderline p-values (0.05-0.15) on NER and no significance on RE

For exp-019 under median tier, the verifier shows the gap is partially closable, which strengthens the paper's narrative by demonstrating that unsupervised signals capture minimal headroom while supervised approaches can recover 15-20%, making the diagnosis more actionable and showing clear room for improvement.

Now I'm structuring the YAML output with labeled metric tables, figure descriptions, and analysis interpretations, pulling baseline comparisons from the earlier experiments to contextualize the results.

For the non-tied subset analysis, I'm seeing that logprob selection outperforms greedy by 2.9 percentage points with statistical significance, and the within-instance correlation jumps substantially from 0.08 to 0.39.

Looking at the free-form median tier metrics, the within-sample logprob range is around 0.10, which is roughly 3-4x larger than the constrained baseline where 60% of instances fall below 0.05—this ratio aligns with what I'd expect from the expanded generation space.

Now I'm comparing the verifier performance across tasks: for NER, the constrained setup shows a modest 0.6pp improvement with weak significance, while free-form achieves 2.0pp with borderline significance. For the exp-019 metrics, I'm looking at the verifier's ability to classify good versus bad outputs and its correlation with F1 scores, along with selection performance on best-of-N tasks—the NER verifier reaches about 0.81 AUROC compared to 0.749 for exact match, and selection F1 is around 0.665 versus the greedy baseline.

The headroom analysis shows the verifier captures about 16% of the gap between current and oracle performance for NER, and roughly 9% for RE, which is reasonable but not transformative. I think I have the numbers I need to write out the full YAML configuration now, making sure everything aligns with how I've defined each tier. I'm also wondering about the specifics of the OOD test in exp-011—it's supposed to measure NER consistency across different domains, but I need to clarify what exactly that evaluation entails.

Looking at the cross-domain scenario, if we're testing the SciERC model on WNUT-17 data or vice versa, the domain gap between scientific papers and noisy social media text would be substantial. The greedy F1 would likely collapse under that shift, consistency signals would degrade, and logprob might become unreliable. If instead it's evaluating within WNUT-17 using its own fine-tuned model, that's a different story given WNUT-17's already weak baseline performance.

The most plausible setup is cross-domain evaluation—either the SciERC-trained model tested on WNUT-17 or the reverse—which would show poor out-of-distribution performance. Given the dependency on exp-003 and the 5-hour GPU budget, this is likely running inference with one model against another dataset's test set. Looking back at exp-003's results, the WNUT model achieved a greedy F1 of 0.523 on its own test set with some concerning patterns like logprob rho of -0.409 and over 50% of samples hitting F1=0. For the cross-domain case with SciERC on WNUT, I'd expect even more dramatic degradation.

I'm estimating the OOD results would show greedy F1 dropping to around 0.15-0.25, oracle F1 around 0.35-0.45, with structural signals (SJ rho) holding up slightly better at 0.10-0.15 compared to logprob rho declining to -0.20 to -0.35. This would support the narrative that structural signals degrade more gracefully than logprob under domain shift, though it's more of a limitation finding than a strong positive result. Now I need to finalize the YAML configuration and verify the median tier metrics are internally consistent with the existing constrained logprob values.

Generating output tables... the registry shows exp_017_llama_conll_infer as DONE with full metrics (SJ rho 0.431, logprob rho 0.307). So the experiment was already run. But since the plan says "planned", I'll include it in my imagined experiments with predictions that align with median tier expectations and happen to be close to what was actually observed.

Actually no, I think the right approach is: the user provided the experiment_plan with these marked as "planned", and they want me to generate imagined data. Some of these may have been run since then. I'll just generate the predictions as requested.

Let me finalize now. I'll write the YAML output.

For exp-018, I'm thinking through how "non-tied" instances behave differently under constrained versus free-form decoding. Under constrained, about 40% of cases show meaningful logprob differences with a +2.9pp gain. But under free-form, the score distributions are less compressed, so maybe 65-75% of instances become non-tied—though the signal gets noisier because parsing errors introduce more variance. The net effect should still favor logprob for discrimination, just with different characteristics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82a125df-b38b-4ad4-a7b8-d801a261ec0a",
  "isSidechain": false,
  "requestId": "req_011Cb48Q1s3mEVstCejyR645",
  "type": "assistant",
  "uuid": "245361e8-9393-4ab3-b7fc-2fb69c6718ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ercmjvUnMigCTABokdoM7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 44957,
      "cache_read_input_tokens": 11841,
      "output_tokens": 19114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 44957,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 19114,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 44957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 44957
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

_source line 9 · 2026-05-15T09:42:19.959Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1 从 "constrained decoding IS the bottleneck" 软化为 "constrained decoding CONTRIBUTES TO
  the bottleneck, as evidenced by partial recovery of logprob discrimination under free-form generation"。
  Free-form ablation 方向正确但非压倒性：logprob variance 恢复 ~3.5x，selection 有 +1-3pp 改善但
  p-value 边缘。RE 上改善不明显，说明 entity set 组合复杂性是独立于 decoding regime 的额外瓶颈。
  Claim 2 (QE framework, AUROC 0.75) 升级为 co-primary contribution，与 Claim 1 并列。
  Title 调整为 "Confidence Signals Predict but Cannot Select in Constrained-Decoding Information Extraction"。
  论文表述用 "provide evidence consistent with" 而非 "experimentally verify"。
  补充 exp-019 simple verifier 作为 gap closability 的 proof-of-concept。

imagined_experiments:

  # =========================================================================
  # exp-011: NER OOD Robustness
  # =========================================================================
  - name: "ner_ood_robustness"
    plan_id: "exp-011"
    description: >
      SciERC fine-tuned Qwen3-8B 模型在 WNUT-17 测试集上的跨域 zero-shot NER 推理，
      评估 consistency signals 在 OOD 条件下的退化模式。N=8, T=1.0。
    expected_results:
      # === 基础性能 ===
      n_instances: 1287
      n_gold_nonempty: 689
      n_valid_after_filter: 689
      greedy_f1: 0.218
      oracle_f1: 0.402
      oracle_headroom: 0.184
      sample_f1_mean: 0.152
      sample_f1_pct_zero: 62.4
      parse_failure_rate: 0.03

      # === QE 指标 (full set, gold 非空) ===
      sj_rho_full: 0.142
      sj_auroc_full: 0.572
      sj_tau_full: 0.105
      fk_rho_full: 0.098
      fk_auroc_full: 0.548
      em_rho_full: 0.118
      em_auroc_full: 0.561
      voting_conf_rho_full: 0.165
      voting_conf_auroc_full: 0.583
      logprob_rho_full: -0.287
      logprob_auroc_full: 0.421

      # === QE 指标 (conditional, greedy F1 > 0) ===
      n_cond: 312
      sj_rho_cond: 0.231
      fk_rho_cond: 0.148
      logprob_rho_cond: 0.089
      voting_conf_rho_cond: 0.252

      # === Selection (best-of-8) ===
      selection_logprob: 0.195
      selection_sj: 0.213
      selection_voting: 0.220
      selection_random: 0.190
      selection_oracle: 0.402

    result_rationale: >
      OOD 条件下，模型对 WNUT-17 社交媒体文本的 NER 能力大幅下降（greedy F1 从 SciERC 的 0.66
      降至 0.22）。62% 的 sample F1=0 意味着模型在多数 OOD 实例上几乎无法正确抽取。在此背景下：

      (1) Logprob 严重失效（rho=-0.287）：模型对 in-domain pattern 赋予高 logprob，但这些 pattern
      在 OOD 数据上不适用，导致 logprob 与 F1 负相关。这与 WNUT-17 in-domain 实验
      (logprob rho=-0.41) 方向一致，在跨域条件下更加极端。

      (2) 结构化信号退化但保持正相关（SJ rho 0.14, voting_conf rho 0.17）：因为 consistency
      是 output-level agreement 的度量，不依赖模型对 domain 的 calibration。即使模型在 OOD 上
      表现差，当多个 sample 碰巧给出相似答案时，这些答案更可能接近正确。

      (3) Conditional set (greedy F1>0, n=312) 上信号恢复到 0.23-0.25，说明模型"能做"的子集上
      consistency 仍有判别力，但 OOD 下这个子集很小。

      (4) Selection 几乎无效：最好的 voting 选择 (0.220) 仅比 random (0.190) 高 3pp，
      oracle headroom 18.4pp 几乎无法被 unsupervised signal 捕获。

      这对论文 Claim 3 (task-complexity boundary) 提供了扩展证据：信号有效性不仅受 task 结构
      复杂性影响，还受 domain shift 影响。在 median 档下，这是 Limitations 中的重要素材
      而非独立贡献。

    tables:
      - title: "Table: OOD Cross-Domain QE Results (SciERC→WNUT-17)"
        columns: ["Signal", "ρ_full", "AUROC_full", "ρ_cond", "Selection_F1"]
        rows:
          - ["voting_conf", 0.165, 0.583, 0.252, 0.220]
          - ["SJ", 0.142, 0.572, 0.231, 0.213]
          - ["EM", 0.118, 0.561, "—", "—"]
          - ["FK", 0.098, 0.548, 0.148, "—"]
          - ["logprob", -0.287, 0.421, 0.089, 0.195]
          - ["random", "—", "—", "—", 0.190]
          - ["oracle", "—", "—", "—", 0.402]

      - title: "Table: In-Domain vs OOD Signal Degradation"
        columns: ["Signal", "SciERC_ρ", "WNUT_OOD_ρ", "Δρ", "Retention_%"]
        rows:
          - ["voting_conf", 0.379, 0.165, -0.214, "43.5%"]
          - ["SJ", 0.360, 0.142, -0.218, "39.4%"]
          - ["FK", 0.267, 0.098, -0.169, "36.7%"]
          - ["logprob", 0.205, -0.287, -0.492, "inverted"]

    figures_description:
      - "Fig: Bar chart comparing signal ρ on in-domain SciERC vs OOD WNUT-17, showing structural signals degrade ~60% while logprob inverts. Error bars from bootstrap CI."
      - "Fig: Scatter plot of per-instance logprob vs F1 on OOD, showing negative trend with high-logprob cluster at F1=0 (overconfidence on OOD)."

    analysis: >
      OOD 实验在 median 档下是 Limitations 材料。关键发现：structural consistency 在 OOD 下退化
      但保持正相关方向（retention ~40%），而 logprob 完全失效并反转。这进一步支持了 QE framework
      (Claim 2) 中 structural signals 的 robustness 优势，但不足以构成独立贡献。
      论文中以一段讨论处理：承认 OOD generalization 不足，但指出 structural signals 的相对优势
      在 OOD 下更加突出（logprob 失效时 consistency 仍可用）。
      对 reviewer score 的影响：neutral，P2 实验不影响核心评分。

  # =========================================================================
  # exp-017: LLaMA-3.1-8B on CoNLL-2003
  # =========================================================================
  - name: "ner_llama_conll"
    plan_id: "exp-017"
    description: >
      LLaMA-3.1-8B-Instruct fine-tuned on CoNLL-2003, NER inference N=8, T=1.0。
      2×2 cross-model × cross-dataset validation矩阵的最后一格。
    expected_results:
      # === 基础性能 ===
      n_instances: 3453
      n_valid: 2756
      n_conditional: 2640
      N: 8
      T: 1.0
      greedy_f1: 0.926
      oracle_f1: 0.945
      oracle_headroom: 0.019

      # === QE 指标 (full) ===
      sj_rho_full: 0.431
      sj_auroc_full: 0.704
      sj_ece_full: 0.114
      fk_rho_full: 0.428
      fk_auroc_full: 0.703
      fk_ece_full: 0.105
      logprob_rho_full: 0.307
      logprob_auroc_full: 0.761
      logprob_ece_full: 0.129
      em_rho_full: 0.431
      em_auroc_full: 0.705
      em_ece_full: 0.109
      voting_conf_rho_full: 0.426
      voting_conf_auroc_full: 0.709
      voting_conf_ece_full: 0.095

      # === QE 指标 (conditional) ===
      sj_rho_cond: 0.436
      fk_rho_cond: 0.431
      logprob_rho_cond: 0.328
      em_rho_cond: 0.440
      voting_conf_rho_cond: 0.374

      # === Selection (best-of-8) ===
      selection_greedy: 0.926
      selection_sj: 0.924
      selection_logprob: 0.925
      selection_voting_conf: 0.925
      selection_random: 0.921
      selection_oracle: 0.945

      # === Cross-model consistency ===
      qwen_sj_rho_full: 0.436  # from exp_002
      llama_sj_rho_full: 0.431
      cross_model_delta_sj: -0.005
      qwen_logprob_rho_full: 0.316
      llama_logprob_rho_full: 0.307
      cross_model_delta_logprob: -0.009

    result_rationale: >
      CoNLL-2003 是成熟的 NER benchmark，Qwen 和 LLaMA 在此数据集上都能达到 >92% greedy F1。
      在 median 档下：

      (1) SJ rho ~0.43 与 Qwen 的 0.436 几乎一致（delta < 0.01），确认 cross-model consistency。
      这是论文最需要的结果：证明 structural consistency signals 的有效性不依赖特定模型架构。

      (2) 所有 structural signals (SJ/FK/EM/voting) 在 rho 上聚集在 0.42-0.43 区间，
      远高于 logprob 的 0.307。但 AUROC 上 logprob (0.761) 反超所有 structural signals (~0.704)。
      这是 CoNLL ceiling effect：greedy F1=0.926 意味着大多数 instance 的 F1 很高，
      区分"极好 vs 好"需要的是 calibration precision (logprob 的优势) 而非 structural agreement
      (已经接近 ceiling)。这个 AUROC 反转不影响论文叙事，因为 QE 的主要 claim 是在 rho 上。

      (3) Selection 完全无效：最好的 signal 甚至不如 greedy，因为 headroom 只有 1.9pp。
      这是 ceiling effect 的直接后果——当 greedy 已经 92.6% 时，best-of-N 几乎没有空间改善。
      这支持论文 Claim 1 的补充论点：selection gap 在 easy task 上消失不是因为 signal 变好了，
      而是因为 headroom 本身就小。

      (4) ECE 值在 0.09-0.13 范围，远好于 SciERC 的 0.35-0.71，说明 CoNLL 上模型
      calibration 本身就好很多。

    tables:
      - title: "Table: 2×2 Cross-Model × Cross-Dataset QE Summary (ρ_full)"
        columns: ["Signal", "Qwen×SciERC", "Qwen×CoNLL", "LLaMA×SciERC", "LLaMA×CoNLL"]
        rows:
          - ["SJ", 0.360, 0.436, 0.363, 0.431]
          - ["FK", 0.267, 0.400, 0.327, 0.428]
          - ["logprob", 0.205, 0.316, 0.183, 0.307]
          - ["voting_conf", 0.379, 0.424, "—", 0.426]
          - ["EM", 0.295, 0.451, "—", 0.431]

      - title: "Table: LLaMA CoNLL Full Results"
        columns: ["Signal", "ρ_full", "τ_full", "AUROC", "ECE"]
        rows:
          - ["SJ", 0.431, 0.356, 0.704, 0.114]
          - ["FK", 0.428, 0.349, 0.703, 0.105]
          - ["EM", 0.431, 0.362, 0.705, 0.109]
          - ["voting_conf", 0.426, 0.351, 0.709, 0.095]
          - ["logprob", 0.307, 0.247, 0.761, 0.129]

    figures_description:
      - "Fig: 2×2 heatmap of SJ ρ across {Qwen, LLaMA} × {SciERC, CoNLL}, showing consistent pattern (structural > logprob) with < 0.01 cross-model delta."

    analysis: >
      exp-017 补全了 2×2 cross-validation 矩阵。Median 档下 SJ rho cross-model delta < 0.01
      足以支撑 "model-agnostic" claim (R2 concern 解决)。但 CoNLL ceiling effect 使得
      selection 完全无效、AUROC 出现 logprob 反超现象——论文需要解释这不是 contradiction
      而是 task-difficulty dependent 的合理结果。这加强了 Claim 3 (task-complexity boundary)
      的论述：在 easy NER (CoNLL) 上 consistency 的 QE 价值降低因为 headroom 本身就小。

  # =========================================================================
  # exp-018: Free-form Decoding Ablation (BREAKTHROUGH)
  # =========================================================================
  - name: "freeform_decoding_ablation"
    plan_id: "exp-018"
    description: >
      SciERC 上 Qwen3-8B 的 free-form decoding ablation。移除 Outlines 约束解码，
      生成 8 个 free-form 样本/实例。对比 constrained vs free-form 的 logprob variance、
      selection performance、QE metrics。论文 Claim 1 的核心实验证据。
    expected_results:
      # === 基础信息 ===
      n_instances_ner: 529
      n_instances_re: 397
      N: 8
      T: 1.0
      model: "qwen3-8b-scierc-merged-v2"

      # === Parse Rate ===
      freeform_parse_rate_ner: 0.83
      freeform_parse_rate_re: 0.78
      freeform_n_parseable_ner: 439
      freeform_n_parseable_re: 310
      freeform_effective_N_mean_ner: 6.6
      freeform_effective_N_mean_re: 6.2

      # === Logprob Score Compression Analysis ===
      constrained_logprob_within_sample_range_median_ner: 0.038
      freeform_logprob_within_sample_range_median_ner: 0.148
      variance_recovery_ratio_ner: 3.89
      constrained_pct_tied_ner: 0.60  # range < 0.05
      freeform_pct_tied_ner: 0.28
      constrained_logprob_within_sample_range_median_re: 0.032
      freeform_logprob_within_sample_range_median_re: 0.118
      variance_recovery_ratio_re: 3.69
      constrained_pct_tied_re: 0.64
      freeform_pct_tied_re: 0.33

      # === NER QE: Constrained vs Free-form (matched parseable subset) ===
      constrained_ner_logprob_rho: 0.205
      freeform_ner_logprob_rho: 0.298
      delta_ner_logprob_rho: 0.093
      delta_ner_logprob_rho_pct: "45.4%"
      constrained_ner_logprob_auroc: 0.578
      freeform_ner_logprob_auroc: 0.623
      delta_ner_logprob_auroc_pp: 4.5

      # NER 其他信号 free-form
      freeform_ner_sj_rho: 0.335
      freeform_ner_voting_conf_rho: 0.358
      freeform_ner_em_rho: 0.268

      # === RE QE: Constrained vs Free-form ===
      constrained_re_logprob_rho: 0.266
      freeform_re_logprob_rho: 0.292
      delta_re_logprob_rho: 0.026
      delta_re_logprob_rho_pct: "9.8%"
      constrained_re_logprob_auroc: 0.601
      freeform_re_logprob_auroc: 0.618
      delta_re_logprob_auroc_pp: 1.7

      # RE 其他信号 free-form
      freeform_re_sj_rho: 0.228
      freeform_re_voting_conf_rho: 0.319

      # === NER Selection: Constrained vs Free-form ===
      constrained_ner_greedy_f1: 0.644
      constrained_ner_logprob_selection_f1: 0.650
      constrained_ner_selection_delta_pp: 0.6
      constrained_ner_selection_p: 0.39
      freeform_ner_greedy_f1: 0.632  # slightly lower due to parse errors
      freeform_ner_logprob_selection_f1: 0.652
      freeform_ner_selection_delta_pp: 2.0
      freeform_ner_selection_p: 0.078
      freeform_ner_selection_cohens_d: 0.125

      # === RE Selection: Constrained vs Free-form ===
      constrained_re_greedy_f1: 0.403
      constrained_re_logprob_selection_f1: 0.410
      constrained_re_selection_delta_pp: 0.7
      freeform_re_greedy_f1: 0.388  # lower due to parse errors and reduced N
      freeform_re_logprob_selection_f1: 0.396
      freeform_re_selection_delta_pp: 0.8
      freeform_re_selection_p: 0.31

      # === Headroom Capture ===
      constrained_ner_oracle_f1: 0.776
      constrained_ner_headroom_capture_pct: 0.5
      freeform_ner_oracle_f1: 0.748  # lower oracle due to fewer parseable samples
      freeform_ner_headroom_capture_pct: 3.4
      constrained_re_oracle_f1: 0.585
      constrained_re_headroom_capture_pct: 0.0
      freeform_re_oracle_f1: 0.541
      freeform_re_headroom_capture_pct: 1.3

      # === Non-tied Subset Analysis (free-form) ===
      freeform_ner_nontied_fraction: 0.72
      freeform_ner_nontied_logprob_delta_pp: 2.8
      freeform_ner_nontied_logprob_p: 0.025
      constrained_ner_nontied_fraction: 0.40
      constrained_ner_nontied_logprob_delta_pp: 2.9
      constrained_ner_nontied_logprob_p: 0.01

      # === Statistical Tests ===
      paired_wilcoxon_variance_constrained_vs_free_ner_p: 1.2e-48
      paired_wilcoxon_variance_constrained_vs_free_re_p: 3.7e-31
      bootstrap_rho_diff_ner_ci95: [0.031, 0.158]
      bootstrap_rho_diff_re_ci95: [-0.029, 0.082]

    result_rationale: >
      这是 median 档的核心实验。结果"方向正确但非压倒性"，原因如下：

      **Logprob Variance 恢复 (NER 3.9x, RE 3.7x)**：
      Constrained decoding 通过 grammar mask 在每一步将 token 概率重新归一化到合法 token 子集。
      当 valid next token 只有少数几个（如 JSON 的结构 token `, : { } [ ]`），logprob 差异被
      压缩到极窄范围。Free-form 移除了这层限制，模型可以在完整 vocabulary 上分配概率，
      因此 sample 间 logprob 差异自然恢复。3.5-4x 的恢复比率在预期范围内（不是 10x），
      因为 fine-tuned 模型已经学会了 JSON 格式，即使无约束也倾向于输出结构化内容，
      所以不会完全回到 free-text 的 variance 水平。

      **NER Selection 改善 +2.0pp (p=0.078) vs Constrained +0.6pp (p=0.39)**：
      Variance 恢复使 logprob 能更好地区分好坏 sample。但改善有限的原因：
      (a) Parse rate 83% 意味着有效 N 从 8 降到 ~6.6，减少了 selection pool；
      (b) 未能 parse 的 sample 可能恰好是 logprob 能最好区分的那些（因为它们偏离 JSON 格式最远，
      logprob 最低）——filtering 掉它们减弱了 logprob 的判别力；
      (c) Logprob 即使不被压缩，也只是生成概率的度量，不直接对应 task-level quality。
      P=0.078 在传统 0.05 阈值下不显著，但方向明确。

      **RE 改善不明显 (+0.8pp, p=0.31)**：
      RE 的 bottleneck 是多源的。即使 logprob variance 恢复（3.7x），RE 的 selection
      仍然受限于：(a) entity set 的组合爆炸——relation triple 的正确性依赖 head entity、
      tail entity、relation type 三者同时正确，consistency 空间是高维离散的；
      (b) RE 的 parse rate 更低（78%），有效样本量进一步减少；(c) RE 的 40%+ sample F1=0
      意味着大量 sample 是完全无用的，logprob 无法在"全错"和"全对"之间有效区分。
      这是 median 档叙事的关键：RE 上缺乏改善说明 constrained decoding 不是唯一瓶颈。

      **Free-form greedy F1 略低于 constrained (NER 0.632 vs 0.644, RE 0.388 vs 0.403)**：
      两个原因：(1) free-form 输出需要 parsing，parsing failure 被排除后仍有部分
      parse 成功但内容有微小错误的 sample（如多余空格导致 entity span 偏移）；
      (2) 无约束下模型偶尔输出格式正确但内容冗余的 JSON（如重复 entity），这些
      technically parseable 但 F1 较低。

      **Non-tied 分析的关键对比**：
      Free-form 下 72% 的 instance 是 non-tied（vs constrained 40%）。在 non-tied 子集上，
      free-form logprob +2.8pp (p=0.025) 与 constrained non-tied +2.9pp (p=0.01) 几乎一致。
      这说明：当 logprob 有足够 variance 时（无论是通过 free-form 还是 natural non-tied），
      其判别力是相似的。Constrained decoding 的问题是人为制造了 60% 的 tied instances。

    tables:
      - title: "Table A: Logprob Score Compression — Constrained vs Free-form"
        columns: ["Metric", "NER_Constrained", "NER_Freeform", "Δ", "RE_Constrained", "RE_Freeform", "Δ"]
        rows:
          - ["within-sample range median", 0.038, 0.148, "3.9×", 0.032, 0.118, "3.7×"]
          - ["% tied (range<0.05)", "60%", "28%", "−32pp", "64%", "33%", "−31pp"]
          - ["logprob ρ with F1", 0.205, 0.298, "+0.093", 0.266, 0.292, "+0.026"]
          - ["logprob AUROC", 0.578, 0.623, "+4.5pp", 0.601, 0.618, "+1.7pp"]

      - title: "Table B: NER Selection — Constrained vs Free-form"
        columns: ["Method", "Constrained_F1", "Freeform_F1"]
        rows:
          - ["greedy", 0.644, 0.632]
          - ["logprob best-of-N", 0.650, 0.652]
          - ["Δ vs greedy (pp)", "+0.6", "+2.0"]
          - ["p-value", 0.39, 0.078]
          - ["Cohen's d", 0.038, 0.125]
          - ["oracle", 0.776, 0.748]
          - ["headroom capture", "0.5%", "3.4%"]

      - title: "Table C: RE Selection — Constrained vs Free-form"
        columns: ["Method", "Constrained_F1", "Freeform_F1"]
        rows:
          - ["greedy", 0.403, 0.388]
          - ["logprob best-of-N", 0.410, 0.396]
          - ["Δ vs greedy (pp)", "+0.7", "+0.8"]
          - ["p-value", "—", 0.31]
          - ["oracle", 0.585, 0.541]

      - title: "Table D: All Signals QE Comparison — Free-form NER"
        columns: ["Signal", "Constrained_ρ", "Freeform_ρ", "Δρ"]
        rows:
          - ["logprob", 0.205, 0.298, "+0.093"]
          - ["voting_conf", 0.379, 0.358, "−0.021"]
          - ["SJ", 0.360, 0.335, "−0.025"]
          - ["EM", 0.295, 0.268, "−0.027"]
          - ["FK", 0.267, "—", "—"]

      - title: "Table E: Non-tied Subset Analysis"
        columns: ["Regime", "Non-tied_%", "logprob_Δ_pp", "p-value"]
        rows:
          - ["Constrained", "40%", "+2.9", 0.01]
          - ["Free-form", "72%", "+2.8", 0.025]

    figures_description:
      - >
        Fig 1 (KEY FIGURE): Paired histogram of within-sample logprob range distribution,
        constrained (blue, peaked near 0) vs free-form (orange, spread to 0.3+). Vertical
        dashed line at range=0.05 marking the "tied" threshold. Annotated with median values
        and recovery ratio.
      - >
        Fig 2: NER selection delta (pp over greedy) bar chart, constrained vs free-form,
        with bootstrap 95% CI error bars. Shows constrained delta CI crossing zero, free-form
        CI barely crossing zero (borderline significant).
      - >
        Fig 3: Scatter plot of per-instance logprob range (x) vs logprob-selected F1 minus
        greedy F1 (y), color-coded by regime (constrained vs free-form). Shows that
        selection improvement concentrates in high-range region, and free-form shifts the
        mass rightward.
      - >
        Fig 4 (NER vs RE contrast): Side-by-side comparison of Δρ (logprob rho improvement)
        for NER (+0.093) and RE (+0.026), illustrating that RE bottleneck is multi-source.

    analysis: >
      Median 档下 exp-018 的论文叙事：

      **可写入论文的 claim**：
      "Removing constrained decoding recovers logprob within-sample variance by ~3.5–4×
      (median range 0.038→0.148 for NER) and improves logprob-F1 correlation
      (ρ: 0.205→0.298, +45%). This provides evidence consistent with the hypothesis that
      constrained decoding contributes to the selection bottleneck."

      **必须加的 hedge**：
      (a) "However, the selection improvement remains modest (+2.0pp, p=0.078) and does not
      reach conventional significance thresholds."
      (b) "On RE, free-form decoding yields minimal improvement (+0.8pp, p=0.31), suggesting
      that the combinatorial complexity of entity-relation output spaces presents an
      independent bottleneck beyond the decoding regime."
      (c) "The reduced parse rate (83% NER, 78% RE) introduces a confound: the parseable
      subset may not be representative of the full instance distribution."

      **对论文整体评分的影响**：
      在 median 档下，exp-018 将 Claim 1 从"speculative"提升为"empirically supported but not
      definitive"。Reviewer 会认可 variance recovery 的统计显著性（Wilcoxon p<1e-48），
      但会 push back on selection improvement 的 borderline p-value。RE 上的负结果
      会被视为诚实的 limitation 而非致命缺陷。
      预期 reviewer score 从无 exp-018 的 ~2.8 提升到 ~3.2，但不足以确保 acceptance。
      需要 Claim 2 (QE framework) 作为 co-primary contribution 来弥补。

  # =========================================================================
  # exp-019: Simple Verifier Baseline
  # =========================================================================
  - name: "simple_verifier_baseline"
    plan_id: "exp-019"
    description: >
      训练 DeBERTa-v3-large 做 (input, output) → F1 预测的回归/分类 verifier。
      训练数据来自 existing N=8 constrained samples。5-fold CV 评估。
      目的：证明 selection gap IS closable，为 unsupervised signals 提供 supervised upper bound。
    expected_results:
      # === Training Setup ===
      model: "DeBERTa-v3-large"
      training_instances_ner: 4232  # 529 × 8
      training_instances_re: 3176   # 397 × 8
      cv_folds: 5
      input_format: "concat(sentence, generated_output)"
      target: "sample F1 (regression) + binary good/bad (F1 > median)"

      # === NER Verifier Results (5-fold CV) ===
      ner_verifier_auroc_mean: 0.812
      ner_verifier_auroc_std: 0.031
      ner_verifier_rho_mean: 0.508
      ner_verifier_rho_std: 0.042
      ner_verifier_selection_f1: 0.665
      ner_verifier_greedy_f1: 0.644
      ner_verifier_selection_delta_pp: 2.1
      ner_verifier_oracle_f1: 0.776
      ner_verifier_headroom_capture_pct: 15.9
      ner_verifier_vs_best_unsupervised_auroc_delta: 0.063  # 0.812 - 0.749(EM)

      # === RE Verifier Results (5-fold CV) ===
      re_verifier_auroc_mean: 0.762
      re_verifier_auroc_std: 0.038
      re_verifier_rho_mean: 0.425
      re_verifier_rho_std: 0.051
      re_verifier_selection_f1: 0.421
      re_verifier_greedy_f1: 0.403
      re_verifier_selection_delta_pp: 1.8
      re_verifier_oracle_f1: 0.585
      re_verifier_headroom_capture_pct: 9.9
      re_verifier_vs_best_unsupervised_auroc_delta: 0.056  # 0.762 - 0.706(EM)

      # === Ablation: Feature Importance ===
      feature_importance_ner:
        output_length: 0.18
        entity_count_diff: 0.22
        token_overlap_with_input: 0.31
        output_json_complexity: 0.15
        learned_representation: 0.14
      feature_importance_re:
        output_length: 0.12
        entity_pair_count: 0.19
        token_overlap_with_input: 0.28
        relation_type_distribution: 0.24
        learned_representation: 0.17

      # === Gap Analysis ===
      gap_unsupervised_to_verifier_ner_pp: 2.1  # 0.665 - 0.644
      gap_verifier_to_oracle_ner_pp: 11.1        # 0.776 - 0.665
      gap_unsupervised_to_verifier_re_pp: 1.8
      gap_verifier_to_oracle_re_pp: 16.4

    result_rationale: >
      Median 档下 simple verifier 的表现"部分 close gap 但远不及 oracle"：

      **NER AUROC 0.812 (vs 最好无监督 EM 0.749, +6.3pp)**：
      Verifier 通过学习 input-output alignment features（特别是 token overlap 和 entity count
      差异）获得了超越 unsupervised signal 的判别力。DeBERTa 的 cross-attention 能检测到
      output 中是否包含 input 中明显存在的 entity（一种 faithfulness 度量），这是
      consistency-based signals 无法捕获的信息。但 +6.3pp 的提升modest，因为：
      (a) 训练数据有限（~4200 samples, 5-fold CV 意味着每折训练~3360）；
      (b) F1 label 本身有 noise（partial match 导致连续 F1 分布，不是干净的 binary）；
      (c) DeBERTa 只看到 (input, output) pair，不看 ground truth，所以它学到的是
      "这个 output 看起来像不像一个好答案"的启发式，而非真正的 quality assessment。

      **RE AUROC 0.762 (vs EM 0.706, +5.6pp)**：
      RE 上 verifier 的提升更小，原因与 exp-018 类似：relation triple 的正确性需要
      同时判断 head/tail/type 三个维度，DeBERTa 在单个 forward pass 中难以精确评估
      这种组合正确性。Feature importance 显示 relation_type_distribution (0.24) 和
      token_overlap (0.28) 是最重要的特征，说明 verifier 主要学习了 surface-level 启发式
      而非深层 semantic 对齐。

      **Selection headroom capture NER 15.9%, RE 9.9%**：
      即使是 supervised verifier 也只能捕获 10-16% 的 oracle headroom。这说明
      selection problem 在 structured IE 中是 fundamentally hard——不仅仅是 signal quality
      的问题，而是 per-sample quality assessment 在 structured output 空间中
      information-theoretically difficult。Oracle headroom 的存在证明信息在 sample 中，
      但从 (input, output) pair 中推断 quality 的难度远超 reasoning task 中的
      "答案对不对"的判断。

      **对论文叙事的价值**：
      Verifier 结果将 unsupervised-supervised-oracle 三级 gap 量化：
      unsupervised: ~0-1% headroom capture
      simple verifier: ~10-16%
      oracle: 100%
      这将 negative finding（signals don't work）转化为 constructive contribution
      （quantified gap with supervised upper bound showing partial closability）。
      在 median 档下，这足以增加 0.2-0.3 的 reviewer score。

    tables:
      - title: "Table: Verifier vs Unsupervised Signals — Summary"
        columns: ["Method", "NER_AUROC", "NER_Selection_F1", "RE_AUROC", "RE_Selection_F1"]
        rows:
          - ["oracle", "—", 0.776, "—", 0.585]
          - ["verifier (DeBERTa)", 0.812, 0.665, 0.762, 0.421]
          - ["EM (best unsupervised)", 0.749, "—", 0.706, "—"]
          - ["voting_conf", 0.684, "—", 0.694, "—"]
          - ["SJ", 0.692, "—", 0.670, "—"]
          - ["logprob", 0.578, 0.650, 0.601, 0.410]
          - ["greedy", "—", 0.644, "—", 0.403]
          - ["random", "—", 0.608, "—", 0.354]

      - title: "Table: Headroom Capture Cascade"
        columns: ["Level", "NER_F1", "NER_Capture_%", "RE_F1", "RE_Capture_%"]
        rows:
          - ["greedy (baseline)", 0.644, "0%", 0.403, "0%"]
          - ["best unsupervised (logprob)", 0.650, "4.5%", 0.410, "3.8%"]
          - ["simple verifier", 0.665, "15.9%", 0.421, "9.9%"]
          - ["oracle", 0.776, "100%", 0.585, "100%"]
          - ["remaining gap", "—", "84.1%", "—", "90.1%"]

    figures_description:
      - >
        Fig: "Headroom cascade" waterfall chart showing F1 progression from greedy → best
        unsupervised → simple verifier → oracle, with annotated headroom capture percentages.
        Illustrates that 84-90% of oracle headroom remains uncaptured even with supervised
        approaches.
      - >
        Fig: Reliability diagram (calibration plot) comparing verifier predicted probability
        vs actual F1>median rate, alongside unsupervised signal calibration curves. Shows
        verifier is better calibrated than all unsupervised signals.

    analysis: >
      Median 档下 exp-019 为论文增加一个 proof-of-concept：selection gap is partially closable。
      关键数字是 headroom cascade（greedy 0% → unsupervised ~4% → verifier ~16% → oracle 100%）。
      这将论文从纯 diagnostic（"these signals don't work"）推进到 partially constructive
      （"here's how much a simple supervised approach can recover, and here's the remaining gap"）。

      但在 median 档下这只是 supplementary contribution，不改变论文的核心结构。
      Reviewer 可能会质疑：(a) DeBERTa verifier 引入了额外的计算成本（但远低于 N×LLM 的成本），
      (b) 5-fold CV 的 variance 较大（std ~0.03-0.05），(c) 训练数据来自同一 LLM 的 samples，
      verifier 可能过拟合于特定 model 的错误模式。这些都是 legitimate limitations。

      对整体 reviewer score 的影响：从 exp-018 alone 的 ~3.2 提升到 ~3.3-3.4。
      Combined with Claim 2 as co-primary, median 档总体 expected score 3.0-3.5，
      findings acceptance probability 0.3-0.5。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "245361e8-9393-4ab3-b7fc-2fb69c6718ae",
  "isSidechain": false,
  "requestId": "req_011Cb48Q1s3mEVstCejyR645",
  "type": "assistant",
  "uuid": "4db5477c-8c18-413e-8d28-673d60f069c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ercmjvUnMigCTABokdoM7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 44957,
      "cache_read_input_tokens": 11841,
      "output_tokens": 19114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 44957,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 19114,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 44957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 44957
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Free-form 恢复 logprob variance 但 selection 提升有限；constrained decoding 是贡献因素之一但非唯一瓶颈 核心假设：['exp-018: logprob within-sample variance 有 2-4x 提升（range 中位数 0.10…",
  "leafUuid": "4db5477c-8c18-413e-8d28-673d60f069c2",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Free-form decoding ablation validates constrained bottleneck hypothesis",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Free-form 恢复 logprob variance 但 selection 提升有限；constrained decoding 是贡献因素之一但非唯一瓶颈 核心假设：['exp-018: logprob within-sample variance 有 2-4x 提升（range 中位数 0.10…",
  "leafUuid": "4db5477c-8c18-413e-8d28-673d60f069c2",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Free-form decoding ablation validates constrained bottleneck hypothesis",
  "sessionId": "f7d328ac-c8f8-46fa-b26a-24551092ee89"
}
```

---
