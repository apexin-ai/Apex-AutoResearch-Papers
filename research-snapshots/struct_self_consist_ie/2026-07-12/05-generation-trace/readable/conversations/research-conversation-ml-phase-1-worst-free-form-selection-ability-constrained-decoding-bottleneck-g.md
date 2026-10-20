# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Free-form 未恢复 selection ability；constrained decoding bottleneck 假说不成立，gap 源

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f8d04737-c591-43f1-8bfe-4c2ea74bdef2.jsonl`
- **Structured JSON:** [`2dcac13670dbe4663966.json`](../../sessions/2d/2dcac13670dbe4663966.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T09:42:22.802Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T09:42:22.802Z",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Free-form 未恢复 selection ability；constrained decoding bottleneck 假说不成立，gap 源于 IE 本身\n核心假设：['exp-018: logprob variance 提升微弱（range 中位数 <0.10）或虽提升但 selection 无改善', 'exp-018: free-form logprob selection vs greedy < +1pp，p>0.2，与 constrained 下结果无实质差异', 'parse rate 可能偏低（60-80%），且可解析子集本身偏向 easy instances（selection bias）', '机制假说被否定：score compression 不是 selection 失败的主因，问题在于 IE 输出空间的组合复杂性使得单一 scalar signal 根本无法有效排序', '回到 D070 前的 framing 困境：论文的 primary contribution 缩回为 systematic negative finding + QE evaluation']\n关键指标范围：{'freeform_parse_rate': [0.6, 0.8], 'freeform_logprob_within_sample_range_median': [0.05, 0.1], 'freeform_logprob_rho_with_f1': [0.15, 0.25], 'freeform_logprob_selection_delta_vs_greedy_pp': [-1.0, 1.0], 'freeform_logprob_selection_p_value': [0.2, 0.8], 'freeform_logprob_auroc': [0.55, 0.6], 'constrained_logprob_rho_with_f1': [0.2, 0.21], 'constrained_logprob_auroc': [0.57, 0.58], 'expected_reviewer_score': [2.5, 3.0], 'findings_acceptance_prob': [0.1, 0.25]}\n叙事方向：核心 reframing 失败，需要第二次 pivot。放弃 \"bottleneck\" 因果叙事， 转向 \"fundamental selection hardness in structured prediction\" angle： (1) IE 输出是 set-of-sets（entity set × relation set），其组合空间使得 任何 instance-level scalar signal 的排序能力存在 information-theoretic 上限； (2) 这与 reasoning/QA 的离散答案空间形成 structural contrast—— self-consistency 成功于后者恰因答案空间小； (3) QE 仍然有效（AUROC 0.75）说明信号捕捉了 difficulty 但无法区分 同一 difficulty 水平内的 quality variation。 Title 改为 \"Why Self-Consistency Fails for Structured Prediction: The Selection Hardness of Set-Valued Outputs\"。 Claim 1 变为 universal negative finding + structural explanation。 Claim 2 (QE framework) 升级为 primary contribution。 风险：与 pre-D070 framing 差距不大，reviewer 可能认为 depth 不够。 必须靠 (a) exp-018 作为 well-designed null result 的方法论严谨性， (b) information-theoretic argument 的新颖性来撑住分数。 仍冲 Findings，但需要 paper writing 极其精炼。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: struct_self_consist_ie\nvenue: EMNLP 2026 Findings\nfocus: Paper has been reframed from \"systematic comparison + negative finding\" to \"identifying, diagnosing, and experimentally verifying a regime-specific selection bottleneck caused by constrained decoding\". The breakthrough experiment is free-form decoding ablation (exp-018) that proves score compression is the mechanism. Evaluate whether this reframing + new experiment breaks through the 3.0/5 plateau to 3.5+. Key question: does the constrained decoding bottleneck story have enough intellectual depth for Findings acceptance?\n\n## paper_framing.md\n\n# Paper Framing — struct_self_consist_ie\n\n> Updated 2026-05-15 — D070 REFRAMING: from \"gap finding\" to \"regime-specific bottleneck identification with controlled ablation\". Motivated by 6-round 3.0/5 plateau — Reviewer diagnosis: content ceiling, not framing ceiling. Adding free-form decoding ablation as breakthrough experiment.\n\n## Target Venue\n- Primary: EMNLP 2026 Findings (via ARR May 2026)\n- Deadline: ARR May cycle, 2026-05-25\n\n## Core Claims (3 条, D070 重排)\n\n### Claim 1 (PRIMARY — Regime-Specific Selection Bottleneck)\nThe correlation-selection gap in structured IE is **caused by constrained decoding**. Under constrained decoding (Outlines/grammar-guided), logprob score compression makes per-sample ranking impossible: 60% of instances have within-sample logprob range < 0.05. Controlled ablation via free-form generation confirms the mechanism: removing constrained decoding recovers logprob variance and selection ability.\n\n**Two-layer argument**:\n- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.\n- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to score compression under constrained decoding. (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation**: removing constrained decoding recovers logprob discrimination → proves compression is the bottleneck, not an inherent IE limitation.\n\n**Key evidence (constrained)**:\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39\n- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp\n- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it under constrained decoding\n\n**Key evidence (free-form ablation)** [PLANNED — exp_freeform_ablation]:\n- Hypothesis: Free-form generation on SciERC will show (a) wider logprob variance, (b) improved logprob selection performance\n- If confirmed: gap is regime-specific → constrained decoding is the bottleneck\n- If not: gap is inherent to structured IE → stronger universal finding\n\n**Implications**: Not just \"signals don't work\" but \"here's WHY and WHEN they don't work, and here's a path forward\" (relaxed decoding + post-hoc filtering, or use logprob on non-tied subset).\n\n### Claim 2 (METHODOLOGY — QE Evaluation Framework)\nSystematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.\n\n**Key results**:\n- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205)\n- RE (preliminary, single benchmark): voting_conf leads both full and conditional\n- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)\n- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09\n\n**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):\n- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578\n- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601\n- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706\n\n### Claim 2b (Selection evidence)\n**exp_016_rerun_1024 evidence** (SciERC, N=8, T=1.0):\n- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)\n- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)\n\n**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):\n- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39\n- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466\n\n### Claim 3 (Diagnostic — task-complexity boundary)\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\n\n**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\n\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\n\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\n\n## Story Spine (D070 REFRAMED)\n\n**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?\n\n**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) under constrained decoding present a fundamentally different challenge — and prior work conflates quality estimation with selection.\n\n**Our framing (D070 reposition — from \"finding a gap\" to \"identifying and verifying a bottleneck\")**:\n\nWe systematically compare five confidence signals for IE under constrained decoding, and discover a **regime-specific selection bottleneck**:\n1. **Conceptual clarification**: Four of five signals are instance-level by construction and cannot rank candidates — this is noted as a definitional property, not discovered empirically. The interesting question is whether the remaining strategies (logprob, MBR/consensus-proximity) can select.\n2. **Core empirical finding**: Logprob — the only per-sample signal — fails due to score compression under constrained decoding (60% of instances have within-sample range < 0.05). Consensus-proximity/MBR also fails despite success in MT.\n3. **Controlled verification**: Free-form decoding ablation confirms the mechanism — removing constrained decoding recovers logprob's discriminative power. The gap is regime-specific, not inherent to structured IE.\n4. **Practical pathway**: Non-tied instances (+2.9pp, p=0.01) show logprob works when compression is absent → actionable mitigation via relaxed decoding or non-tied subset selection.\n\n**Headline**: \"We identify, diagnose, and experimentally verify a regime-specific selection bottleneck in constrained-decoding IE: confidence signals that reliably predict output quality (AUROC 0.75) cannot select better candidates because constrained decoding compresses log-probability scores. A controlled free-form ablation confirms the mechanism and points to relaxed decoding as a mitigation path.\"\n\n**Potential title**: \"The Constrained Decoding Bottleneck: Why Confidence Signals Predict but Cannot Select in Information Extraction\"\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only one NER dataset — generalization unclear\"\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\n- **Priority**: P0\n\n### R2: \"Only one model family (Qwen3-8B)\"\n- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect\n- **Priority**: P0\n\n### R3: \"FK is a strawman baseline — what about log-prob, USC, exact-match?\"\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).\n- **Priority**: P0, RESOLVED — results decisive\n\n### R3b: \"EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?\"\n- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.\n- **Priority**: P1 — narrative adjusted for 1024-token results\n\n### R4: \"No actual TTS improvement demonstrated\"\n- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.\n- **Mitigation**: Paper PIVOTS to \"confidence estimation + correlation-selection gap analysis.\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\n- **Priority**: P0 — narrative pivot complete, bootstrap confirms\n\n### R5: \"Sample size N=8 may be too small for reliable SJ estimation\"\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\n- **Priority**: P0\n\n### R6: \"Conditional analysis cherry-picks favorable instances\"\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\n- **Priority**: P0 (add sensitivity analysis)\n\n### R7: \"Only ρ as evaluation metric\"\n- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).\n- **Priority**: P0\n\n### R8: \"Formula-implementation discrepancy\"\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\n- **Priority**: P0, paper writing fix\n\n### R9: \"Evaluation circularity (T>0 consistency vs T=0 F1)\"\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\n- **Priority**: P0\n\n### R10: \"Insufficient related work\" (三档一致 [B][M][W])\n- **Mitigation**: Expand to 35+ references. Must cite:\n  - USC (Chen 2024) — empirical differentiation, not just citation\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\n  - **IE confidence**: Culotta & McCallum 2004\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\n  - **[2025-2026 新颖性自查补充 — 必引]**:\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\"overlooks semantically consistent outputs\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\n  - **[2025-2026 新颖性自查补充 — 应引]**:\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\n  - **需新增 Related Work 小节**:\n    - \"Test-Time Scaling & Sample Selection\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\n    - \"Consistency for Structured IE\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\n- **Priority**: P0, Paper Agent handles\n\n### R11: \"SJ+logprob ensemble missing\" (Dream 2 — both reviewers)\n- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:\n  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078\n  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706\n  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)\n  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.\n- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)\n\n### R12: \"No supervised upper bound / reward model comparison\" (Dream 2)\n- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Results show ensemble underperforms best single signal (EM), suggesting feature redundancy rather than complementarity. Full reward model training out of scope for this paper — discuss as future work.\n- **Priority**: P1 (partially addressed by exp-016 ensemble)\n\n### R13: \"Headroom capture rate low\" (Dream 2)\n- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.\n- **Priority**: P0, paper writing\n\n### R14: \"Cross-model validation thin — need more than 2×8B\" (Dream 2)\n- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.\n- **Priority**: P1\n\n### R15: \"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\"\n- **Priority**: P0, Paper Agent handles\n\n### R16: \"Zero figures — data-rich paper with only tables\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\n- **Priority**: P0, Paper Agent handles\n\n### R17: \"Diagnostic framework overclaimed — descriptive not prescriptive\" (Dream 2 cross-tier, [M][W])\n- **Mitigation**: Soften \"diagnostic framework\" to \"diagnostic analysis\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\n- **Priority**: P0, Paper Agent handles\n\n### R18: \"No discussion of when consistency WOULD help\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\n- **Priority**: P1, Paper Agent handles\n\n### R19: \"Negative result partially predictable for fine-tuned models\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\n- **Priority**: P1, Paper Agent handles\n\n## Venue Fit\n\nEMNLP is well-suited for:\n- Systematic empirical comparison of confidence signals for structured prediction\n- Diagnostic findings with principled explanations\n- The \"comparison + boundary condition\" contribution pattern\n\nRisk assessment (post-1024-token correction + bootstrap):\n- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.\n- **Data-dependent risks**: The bootstrap test strengthened the correlation-selection gap narrative definitively — NER logprob +0.6pp is confirmed noise (p=0.39), making the \"Weak Selectors\" claim statistically rigorous rather than directional.\n- **Confirmed strength**: Structural consistency family (EM/voting/SJ) >> logprob on quality estimation (AUROC 0.75 vs 0.58). Correlation-selection gap is now statistically confirmed with bootstrap CI.\n- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.\n\n## experiment_plan (with registry status)\n\n- id: exp-012\n  name: baseline_logprob\n  claim: 1\n  description: 'Compute sequence log-probability for all existing pilot samples (SciERC\n    NER+RE) and new dataset pilots. Correlate log-prob with F1 (ρ, AUROC, τ). If SJ\n    does NOT beat log-prob, the 16x inference cost is unjustified and paper contribution\n    weakens drastically. THIS IS THE MAKE-OR-BREAK EXPERIMENT.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  note: 'Needs vLLM forward pass to extract log-probs from existing samples. ~1h per\n    dataset on 1 GPU. For new datasets, capture log-probs during pilot inference.\n    Also compute on pilot_004/005 existing data if log-probs weren''t saved.\n\n    '\n  registry_id: exp_012_logprob_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho_sj: 0.3565\n    ner_full_rho_fk: 0.2651\n    ner_full_rho_logprob: 0.1396\n    ner_full_rho_greedy_logprob: 0.1615\n    ner_full_tau_sj: 0.2658\n    ner_full_tau_logprob: 0.1006\n    ner_full_auroc_sj: 0.6892\n    ner_full_auroc_fk: 0.6292\n    ner_full_auroc_logprob: 0.5907\n    ner_full_n: 529\n    ner_sj_vs_logprob_delta: 0.2169\n    re_full_rho_sj: 0.2112\n    re_full_rho_fk: 0.2528\n    re_full_rho_logprob: 0.2467\n    re_full_auroc_sj: 0.5916\n    re_full_auroc_fk: 0.6262\n    re_full_auroc_logprob: 0.6186\n    re_full_n: 397\n    re_cond_rho_sj: 0.3683\n    re_cond_rho_fk: 0.3168\n    re_cond_rho_logprob: 0.1457\n    re_cond_auroc_sj: 0.6839\n    re_cond_auroc_logprob: 0.5487\n    re_cond_n: 296\n    diagnosis: 'NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead.\n      RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.'\n- id: exp-013\n  name: baseline_exact_match\n  claim: 1\n  description: 'Exact-match voting rate: what fraction of N samples produce identical\n    entity/relation sets? Correlate with F1. This is the direct analogue of Wang et\n    al.''s original self-consistency for structured outputs.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU-only on existing pilot data. Zero cost.\n  registry_id: exp_013_exact_match_voting\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_full_rho: 0.2941\n    ner_full_p: 5.12e-12\n    ner_full_tau: 0.2181\n    ner_full_auroc: 0.6398\n    re_full_rho: 0.1562\n    re_full_p: 0.0018\n    re_full_tau: 0.1185\n    re_full_auroc: 0.5863\n    diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\n- id: exp-014\n  name: baseline_entity_voting\n  claim: 1\n  description: 'Entity-level majority voting: for each entity, count how many of N\n    samples include it. Select entities above threshold. Compare F1 of entity-voting\n    selection vs SJ selection vs FK selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU-only on existing pilot data. Zero cost.\n  registry_id: exp_014_entity_majority_voting\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho: 0.3915\n    ner_full_p: 8.1e-21\n    ner_full_tau: 0.2906\n    ner_full_auroc: 0.7039\n    re_full_rho: 0.3403\n    re_full_p: 3.21e-12\n    re_full_tau: 0.256\n    re_full_auroc: 0.6668\n    ner_voting_f1: 0.6246\n    ner_greedy_f1: 0.6483\n    ner_oracle_f1: 0.7793\n    re_voting_f1: 0.3577\n    re_greedy_f1: 0.4022\n    re_oracle_f1: 0.5886\n    diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE\n      (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\n- id: exp-015\n  name: evaluation_metrics_expansion\n  claim: 1\n  description: 'Add AUROC (binary: good/bad output at threshold), calibration plots,\n    and Kendall''s τ alongside Spearman ρ for ALL confidence signals (SJ, FK, log-prob,\n    exact-match, entity-voting) on ALL datasets. Also add leave-one-out SJ as robustness\n    check for evaluation circularity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  - exp-013\n  - exp-014\n  note: CPU-only analysis. Addresses Dream concerns D5 (single metric) and D17 (circularity).\n  registry_id: exp_015_metrics_expansion\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_012_logprob/samples_with_logprobs.jsonl\n    config: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\n    ner:\n      n_valid: 529\n      n_cond: 501\n      voting_rho_full: 0.5018\n      voting_rho_cond: 0.4497\n      voting_auroc: 0.7279\n      voting_tau: 0.3766\n      sj_rho_full: 0.3565\n      sj_rho_cond: 0.412\n      sj_auroc: 0.6656\n      sj_tau: 0.2658\n      em_rho_full: 0.2566\n      em_rho_cond: 0.3427\n      em_auroc: 0.623\n      em_tau: 0.1924\n      fk_rho_full: 0.2651\n      fk_rho_cond: 0.306\n      fk_auroc: 0.6243\n      fk_tau: 0.2027\n      logprob_rho_full: 0.1396\n      logprob_rho_cond: 0.1627\n      logprob_auroc: 0.5585\n      logprob_tau: 0.1006\n    re:\n      n_valid: 397\n      n_cond: 296\n      voting_rho_full: 0.4217\n      voting_rho_cond: 0.463\n      voting_auroc: 0.7162\n      voting_tau: 0.327\n      sj_rho_full: 0.2112\n      sj_rho_cond: 0.3683\n      sj_auroc: 0.5816\n      sj_tau: 0.1619\n      em_rho_full: 0.1002\n      em_rho_cond: 0.3607\n      em_auroc: 0.5036\n      em_tau: 0.0839\n      fk_rho_full: 0.2528\n      fk_rho_cond: 0.3168\n      fk_auroc: 0.6308\n      fk_tau: 0.1967\n      logprob_rho_full: 0.2467\n      logprob_rho_cond: 0.1457\n      logprob_auroc: 0.6354\n      logprob_tau: 0.1808\n    diagnosis: 'Unified 5-signal evaluation on single data source. Voting leads NER\n      full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals\n      beat logprob on NER. RE: voting leads both full and cond.'\n- id: exp-001\n  name: ner_n16_scierc\n  claim: 1\n  description: 'NER N=16 on SciERC (ft_002_v2 model). Strengthen rho estimation, test\n    N-scaling. Run with seeds [42, 123, 456] for robustness. MUST capture log-probs\n    during inference for exp-012.\n\n    '\n  priority: P0\n  gpu_budget_hours: 18\n  deps: []\n  dataset: SciERC\n  model: ft_002_v2\n  note: 3 seeds × 6h each. Inference script MUST output log-probs.\n  registry_id: exp_001_ner_n16_scierc\n  status: DONE\n  conclusion: success\n  metrics:\n    n_instances: 551\n    ner_n: 529\n    re_n: 397\n    N: 16\n    T: 1\n    seed: 42\n    full_test_set: true\n    ner_voting_conf_rho: 0.399\n    ner_sj_rho: 0.398\n    ner_em_rho: 0.339\n    ner_fk_rho: 0.288\n    ner_logprob_rho: 0.237\n    ner_voting_conf_auroc: 0.704\n    ner_sj_auroc: 0.697\n    ner_cond_em_rho: 0.414\n    ner_cond_sj_rho: 0.349\n    ner_cond_vc_rho: 0.34\n    re_voting_conf_rho: 0.38\n    re_logprob_rho: 0.293\n    re_fk_rho: 0.281\n    re_sj_rho: 0.277\n    re_em_rho: 0.148\n    re_voting_conf_auroc: 0.699\n    re_cond_em_rho: 0.475\n    re_cond_sj_rho: 0.318\n    re_cond_vc_rho: 0.35\n    re_cond_em_auroc: 0.742\n    diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380).\n      EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full\n      FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact of\n      200 instances + T=0.7.'\n- id: exp-002\n  name: ner_conll2003\n  claim: 1\n  description: 'Fine-tune Qwen3-8B on CoNLL-2003 (LoRA) + NER pilot (N=8, T=0.7).\n    Cross-dataset generalization. MUST capture log-probs. Use consistent N and T with\n    other datasets.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  dataset: CoNLL-2003\n  model: qwen3-8b (new fine-tune)\n  registry_id: exp_002_ner_conll2003\n  status: DONE\n  conclusion: success\n- id: exp-003\n  name: ner_wnut17\n  claim: 1\n  description: 'Fine-tune Qwen3-8B on WNUT-17 (LoRA) + NER pilot (N=8, T=0.7). Social\n    media domain — cross-dataset generalization. MUST capture log-probs.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps: []\n  dataset: WNUT-17\n  model: qwen3-8b (new fine-tune)\n  note: User confirmed public datasets only. D043/D045 abandoned — 54% F1=0, SJ rho\n    not significant. Provides Claim 3 negative evidence.\n  registry_id: exp_003_wnut17_v2_infer\n  status: orphaned\n- id: exp-004\n  name: re_diagnostic_analysis\n  claim: 2\n  description: 'Per-relation-type consistency breakdown on existing pilot_004/005\n    data. Error propagation patterns. Bootstrap CI for ALL rho comparisons. Add conditional\n    threshold sensitivity analysis (vary exclusion criterion). Compare ALL confidence\n    signals (SJ, FK, log-prob, exact-match) on RE.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  - exp-013\n  note: CPU-only. Bootstrap CI + threshold sensitivity address Dream concerns.\n  registry_id: exp_004_re_diagnostic\n  status: DONE\n  conclusion: success\n  metrics:\n    per_relation_type:\n      HYPONYM-OF:\n        n: 36\n        rho_sj: 0.545\n        rho_fk: 0.646\n        rho_vc: 0.628\n        mean_f1: 0.513\n      CONJUNCTION:\n        n: 86\n        rho_sj: 0.383\n        rho_fk: 0.35\n        rho_vc: 0.484\n        mean_f1: 0.48\n      USED-FOR:\n        n: 299\n        rho_sj: 0.236\n        rho_fk: 0.255\n        rho_vc: 0.286\n        mean_f1: 0.422\n      PART-OF:\n        n: 44\n        rho_sj: 0.239\n        rho_fk: 0.348\n        rho_vc: 0.283\n        mean_f1: 0.297\n      EVALUATE-FOR:\n        n: 62\n        rho_sj: 0.172\n        rho_fk: 0.255\n        rho_vc: 0.226\n        mean_f1: 0.365\n      COMPARE:\n        n: 35\n        rho_sj: 0.168\n        rho_fk: 0.184\n        rho_vc: 0.18\n        mean_f1: 0.453\n      FEATURE-OF:\n        n: 50\n        rho_sj: 0.004\n        rho_fk: 0.052\n        rho_vc: 0.014\n        mean_f1: 0.254\n    error_propagation:\n      total_fn: 553\n      tail_error_pct: 21.9\n      full_error_pct: 21.7\n      head_error_pct: 17.7\n      head_tail_error_pct: 15.9\n      type_error_pct: 8.3\n      worst_consistency: head_type_error (sj=0.411)\n      best_consistency: head_error (sj=0.613)\n    threshold_sensitivity:\n      thr_0.00_rho_sj: 0.3161\n      thr_0.00_rho_vc: 0.3841\n      thr_0.00_n: 313\n      thr_0.05_rho_sj: 0.2682\n      thr_0.05_rho_vc: 0.2364\n      thr_0.05_n: 239\n    bootstrap_ci_95:\n      ner_sj:\n      - 0.2946\n      - 0.4586\n      ner_voting_conf:\n      - 0.3048\n      - 0.4656\n      re_sj:\n      - 0.1422\n      - 0.3391\n      re_voting_conf:\n      - 0.1818\n      - 0.3721\n      re_cond_sj:\n      - 0.2161\n      - 0.4102\n      re_cond_voting_conf:\n      - 0.2825\n      - 0.474\n    fisher_z_ner_vs_re:\n      sj_z: 2.31\n      sj_p: 0.0209\n      sj_significant: true\n      fk_z: -0.31\n      fk_p: 0.756\n      fk_significant: false\n      voting_z: 1.914\n      voting_p: 0.0556\n      voting_significant: false\n    diagnosis: FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF\n      strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of\n      RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE\n      signal in conditional set (rho=0.384).\n- id: exp-005\n  name: temperature_sensitivity_analysis\n  claim: 2\n  description: 'T=0.7 vs T=1.0 comparison on both NER and RE for ALL confidence signals.\n    Signal-noise tradeoff analysis.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  note: CPU-only on existing pilot_004 (T=1.0) and pilot_005 (T=0.7) data.\n  registry_id: exp_005\n  status: DONE\n  conclusion: success\n- id: exp-006\n  name: adaptive_compute_demo\n  claim: 1\n  description: 'Best-of-N selection on NER: SJ vs log-prob vs FK vs exact-match vs\n    random vs greedy. Report on ALL NER datasets (not just SciERC). Include RE results\n    too (even if negative).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-012\n  note: CPU-only. Must cover all datasets and include RE for completeness.\n  registry_id: exp_006_v2\n  status: DONE\n  conclusion: negative\n  metrics:\n    NER_SciERC_s42:\n      greedy: 0.618\n      oracle: 0.787\n      SJ: 0.62\n      logprob: 0.621\n      FK: 0.621\n      EM: 0.606\n      voting_conf: 0.585\n      random: 0.586\n    NER_SciERC_s123:\n      greedy: 0.618\n      oracle: 0.785\n      SJ: 0.617\n      logprob: 0.618\n      FK: 0.621\n      EM: 0.613\n      voting_conf: 0.584\n      random: 0.583\n    NER_CoNLL:\n      greedy: 0.725\n      oracle: 0.757\n      SJ: 0.718\n      logprob: 0.716\n      FK: 0.717\n      EM: 0.716\n      voting_conf: 0.714\n      random: 0.692\n    RE_SciERC:\n      greedy: 0.403\n      oracle: 0.631\n      SJ: 0.397\n      logprob: 0.41\n      FK: 0.396\n      EM: 0.381\n      voting_conf: 0.408\n      random: 0.364\n- id: exp-007\n  name: ner_multi_model\n  claim: 1\n  description: 'NER pilot with LLaMA-3.1-8B-Instruct on SciERC. Model-agnostic validation.\n    MUST capture log-probs for baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps: []\n  dataset: SciERC\n  model: llama-3.1-8b (new fine-tune)\n  registry_id: exp_007_llama_inference\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.66\n      oracle_f1: 0.781\n      headroom: 0.121\n      rho_fk: 0.327\n      rho_sj: 0.363\n      rho_fk_cond: 0.226\n      rho_sj_cond: 0.311\n      rho_logprob: 0.183\n      rho_logprob_cond: 0.109\n      structural_beats_surface: true\n      sample_f1_pct_zero: 11.6\n    re:\n      greedy_f1: 0.434\n      oracle_f1: 0.568\n      headroom: 0.135\n      rho_fk: 0.305\n      rho_sj: 0.299\n      rho_fk_cond: 0.259\n      rho_sj_cond: 0.405\n      rho_logprob: 0.288\n      rho_logprob_cond: 0.092\n      structural_beats_surface: false\n      sample_f1_pct_zero: 41.2\n    n_instances: 551\n    N: 8\n    T: 1\n    seed: 42\n    model: LLaMA-3.1-8B-Instruct\n    verdict: FAIL\n    verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\n- id: exp-008\n  name: re_n16_confirmation\n  claim: 2\n  description: 'RE N=16 on SciERC to confirm negative finding with higher statistical\n    power.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps: []\n  dataset: SciERC\n  model: ft_002_v2\n  registry_id: exp_008_re_n16\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.6635\n      oracle_f1: 0.8208\n      headroom: 0.1572\n      rho_sj_full: 0.377\n      rho_fk_full: 0.2508\n      rho_logprob_full: 0.3153\n      rho_sj_cond: 0.3598\n      rho_fk_cond: 0.2251\n      rho_logprob_cond: 0.2927\n      sj_beats_fk: true\n      rho_advantage: 0.1262\n    re:\n      greedy_f1: 0.4339\n      oracle_f1: 0.6658\n      headroom: 0.2319\n      rho_sj_full: 0.2966\n      rho_fk_full: 0.2871\n      rho_logprob_full: 0.2986\n      rho_sj_cond: 0.3975\n      rho_fk_cond: 0.3774\n      rho_logprob_cond: 0.2745\n      sj_beats_fk: true\n      rho_advantage: 0.0095\n    verdict: FAIL\n- id: exp-009\n  name: capability_stratification\n  claim: 2\n  description: 'Stratify instances by difficulty (greedy F1 buckets + independent\n    proxies: sentence length, entity count) for both NER and RE. Verify inverted-U\n    pattern with proper statistical tests and independent stratification variable.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  note: CPU-only. Dream flagged inverted-U overclaiming — use independent proxy.\n  registry_id: exp_009_capability_stratification\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n: 551\n      sj_rho_overall: 0.398\n      by_greedy_f1:\n        hard_0_25_sj_rho: 0.159\n        med_low_sj_rho: 0.139\n        med_high_sj_rho: 0.09\n        easy_sj_rho: 0.23\n      by_sent_len:\n        Q1_sj_rho: 0.461\n        Q2_sj_rho: 0.401\n        Q3_sj_rho: 0.296\n        Q4_sj_rho: 0.382\n      by_ent_count:\n        0_sj_rho: 0.689\n        1_2_sj_rho: 0.415\n        3_5_sj_rho: 0.353\n        6plus_sj_rho: 0.547\n    scierc_re:\n      n: 551\n      by_greedy_f1:\n        hard_0_25_sj_rho: -0.043\n        easy_sj_rho: 0.21\n      by_sent_len:\n        Q1_sj_rho: 0.447\n        Q4_sj_rho: 0.54\n      by_rel_count:\n        0_sj_rho: 0.62\n        1_2_sj_rho: 0.275\n        6plus_sj_rho: 0.527\n    conll_ner:\n      n: 3453\n      by_sent_len:\n        Q1_sj_rho: 0.334\n        Q3_sj_rho: 0.518\n    proxy_independence:\n      scierc_ner_f1_vs_slen: -0.021\n      scierc_ner_f1_vs_ecnt: 0.007\n      scierc_re_f1_vs_slen: -0.147\n- id: exp-010\n  name: selection_curves\n  claim: 1\n  description: 'Best-of-N selection curves for N=1,2,4,8,16 comparing all confidence\n    signals. Visualize as line plots (not just tables — Dream flagged table-only presentation).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-012\n  note: CPU-only visualization\n  registry_id: exp_010_selection_curves\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n_instances: 551\n      greedy_f1: 0.618\n      N16:\n        oracle: 0.787\n        SJ: 0.62\n        FK: 0.621\n        logprob: 0.621\n        voting_conf: 0.585\n        EM: 0.606\n        random: 0.595\n      N8:\n        oracle: 0.752\n        SJ: 0.614\n        FK: 0.614\n        logprob: 0.619\n        voting_conf: 0.591\n        EM: 0.603\n        random: 0.589\n      N4:\n        oracle: 0.714\n        SJ: 0.607\n        FK: 0.608\n        logprob: 0.616\n        voting_conf: 0.594\n        EM: 0.6\n        random: 0.587\n    scierc_re:\n      n_instances: 397\n      greedy_f1: 0.403\n      N16:\n        oracle: 0.631\n        SJ: 0.397\n        FK: 0.396\n        logprob: 0.41\n        voting_conf: 0.408\n        EM: 0.381\n        random: 0.364\n      N8:\n        oracle: 0.583\n        SJ: 0.393\n        FK: 0.394\n        logprob: 0.413\n        voting_conf: 0.398\n        EM: 0.381\n        random: 0.363\n    conll_ner:\n      n_instances: 3453\n      greedy_f1: 0.725\n      N8:\n        oracle: 0.757\n        SJ: 0.718\n        FK: 0.717\n        logprob: 0.716\n        voting_conf: 0.714\n        EM: 0.716\n        random: 0.69\n      N4:\n        oracle: 0.746\n        SJ: 0.714\n        FK: 0.714\n        logprob: 0.715\n        voting_conf: 0.714\n        EM: 0.712\n        random: 0.692\n- id: exp-011\n  name: ner_ood_robustness\n  claim: 1\n  description: 'Test NER consistency signal on OOD instances (cross-domain transfer).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n- id: exp-016\n  name: signal_ensemble_analysis\n  claim: 1\n  description: 'SJ+logprob instance-level correlation and ensemble analysis. (1) Pearson/Spearman\n    correlation between SJ and logprob per-instance. (2) Grid search linear combination\n    alpha*SJ + (1-alpha)*logprob. (3) Logistic regression on all 5 signals as ensemble.\n    (4) Best-of-N selection F1 for ensemble vs individual signals. Dream 2 reviewers\n    BOTH independently flagged this as missing.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  - exp-014\n  note: CPU-only on existing pilot_004 data. Zero cost, high impact.\n  registry_id: exp_016_signal_ensemble\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_logprob_pearson_ner: 0.57\n    sj_logprob_pearson_re: 0.42\n    best_linear_ner:\n      combo: SJ+voting_conf\n      alpha: 0.3\n      rho: 0.489\n    best_linear_re:\n      combo: voting_conf+logprob\n      alpha: 0.6\n      rho: 0.429\n    ensemble_ner_auroc: 0.735\n    ensemble_re_auroc: 0.719\n    best_single_ner_auroc: 0.7\n    best_single_re_auroc: 0.721\n    ensemble_ner_delta: 0.035\n    selection_f1_ner:\n      greedy: 0.609\n      logprob: 0.609\n      sj: 0.604\n      ensemble: 0.604\n      voting: 0.596\n      random: 0.58\n      oracle: 0.769\n    selection_f1_re:\n      logprob: 0.397\n      greedy: 0.374\n      sj: 0.368\n      ensemble: 0.367\n      voting: 0.338\n      random: 0.338\n      oracle: 0.561\n    diagnosis: 'SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best\n      is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER.\n      Oracle gap still huge.'\n- id: exp-017\n  name: ner_llama_conll\n  claim: 1\n  description: 'LLaMA-3.1-8B on CoNLL-2003 to strengthen cross-model validation. Dream\n    2 flagged LLaMA only on SciERC is insufficient for model-agnostic claim.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-007\n  dataset: CoNLL-2003\n  model: llama-3.1-8b (fine-tune on CoNLL)\n  note: Only if exp-007 shows positive signal and GPU hours available.\n  status: planned\n- id: exp-018\n  name: freeform_decoding_ablation\n  claim: 1\n  description: 'BREAKTHROUGH EXPERIMENT (D070). Free-form decoding ablation on SciERC\n    NER+RE using Qwen3-8B. Remove Outlines constrained decoding, generate 8 free-form\n    samples per instance. Compare logprob variance, selection performance, and QE\n    metrics between constrained vs free-form. This is the controlled experiment that\n    proves whether the correlation-selection gap is caused by constrained decoding\n    (regime-specific) or inherent to structured IE (universal). If free-form recovers\n    logprob selection → paper becomes about regime-specific bottleneck (much stronger).\n    If gap persists → universal finding (also stronger).\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  dataset: SciERC\n  model: qwen3-8b (existing fine-tuned checkpoint)\n  note: '529 NER + 397 RE instances × 8 samples = ~4200 generations. 8B model on RTX\n    5090 ≈ 1-2h inference. Parse rate expected 80-95% (fine-tuned model learned JSON\n    format). Analysis on parseable subset. Key metrics: (a) logprob within-sample\n    variance (constrained vs free), (b) selection F1 (constrained vs free), (c) QE\n    ρ/AUROC (constrained vs free).\n\n    '\n  status: planned\n- id: exp-019\n  name: simple_verifier_baseline\n  claim: 1\n  description: 'P1 EXPERIMENT. Train a simple supervised verifier (DeBERTa or 8B classification\n    head) on existing (input, output, F1) data. If verifier partially closes the selection\n    gap, it proves the gap IS closable and transforms the negative finding into an\n    actionable one with an upper bound on unsupervised methods.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-018\n  dataset: SciERC\n  model: DeBERTa-v3-large or Qwen3-8B classifier\n  note: 'Only if exp-018 done and time permits before DDL. Training data: existing\n    N=8 samples with F1 labels. ~1 day implementation + training + evaluation.\n\n    '\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: ft_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.1099\n    eval_loss: 0.0771\n    gate0_ner_f1_strict: 0.1143\n    gate0_re_f1_strict: 0.0125\n    gate0_ner_f1_text: 0.606\n    gate0_re_f1_text: 0.3392\n    gate0_offset_accuracy: 0.1665\n    gate0_parse_failures: 43\n    gate0_pass: false\n    gate0_realigned_ner_f1: 0.6045\n    gate0_realigned_re_f1: 0.338\n    gate0_realigned_entity_offset_accuracy: 1\n    gate0_realigned_relation_offset_accuracy: 1\n    gate0_realigned_ner_pass: true\n    gate0_realigned_re_pass: false\n    gate0_realigned_pass: false\n    gate0_ner_f1_delta_realign: 0.4901\n    gate0_re_f1_delta_realign: 0.3255\n    verdict_note: 'partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)'\n- exp_id: mvp_pilot_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.611\n    ner_oracle_f1: 0.78\n    ner_headroom: 0.169\n    ner_fleiss_kappa_mean: 0.2449\n    ner_soft_jaccard_mean: 0.5041\n    ner_full_rho_sj: 0.3616\n    ner_full_rho_fk: 0.3515\n    ner_full_n: 529\n    ner_cond_rho_sj: 0.3688\n    ner_cond_rho_fk: 0.3569\n    ner_cond_n: 510\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_sample_f1_pct_zero: 20.4\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 19\n    re_greedy_f1: 0.355\n    re_oracle_f1: 0.572\n    re_headroom: 0.217\n    re_fleiss_kappa_mean: 0.0681\n    re_soft_jaccard_mean: 0.3635\n    re_full_rho_sj: 0.2535\n    re_full_rho_fk: 0.2885\n    re_full_n: 397\n    re_cond_rho_sj: 0.3515\n    re_cond_rho_fk: 0.3107\n    re_cond_n: 320\n    re_sj_beats_fk_full: false\n    re_sj_beats_fk_cond: true\n    re_sample_f1_pct_zero: 58.3\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 77\n    parse_failures_stochastic: 164\n    parse_failures_greedy: 29\n    total_stochastic_samples: 4408\n    total_greedy: 551\n    verdict: FAIL\n    verdict_reason: RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\n- exp_id: ft_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    last_step: 70\n    total_steps: 585\n    progress_pct: 11.97\n    last_loss: 0.1134\n    last_lr: 0.00019982\n    elapsed: 3m32s\n    failure_reason: OOM at step 73, batch_size=4 too large for 32GB RTX 5090\n- exp_id: mvp_pilot_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_pilot_003\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.6362\n    ner_oracle_f1: 0.792\n    ner_headroom: 0.1559\n    ner_fleiss_kappa_mean: 0.2488\n    ner_soft_jaccard_mean: 0.5066\n    ner_full_rho_sj: 0.3808\n    ner_full_rho_fk: 0.3362\n    ner_full_p_sj: 1.07e-19\n    ner_full_p_fk: 1.93e-15\n    ner_full_n: 529\n    ner_cond_rho_sj: 0.3836\n    ner_cond_rho_fk: 0.3187\n    ner_cond_p_sj: 1.83e-19\n    ner_cond_p_fk: 1.33e-13\n    ner_cond_n: 514\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_rho_advantage: 0.0446\n    ner_sample_f1_mean: 0.5153\n    ner_sample_f1_std: 0.3334\n    ner_sample_f1_pct_zero: 19.9\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 15\n    re_greedy_f1: 0.3774\n    re_oracle_f1: 0.5939\n    re_headroom: 0.2165\n    re_fleiss_kappa_mean: 0.0879\n    re_soft_jaccard_mean: 0.3958\n    re_full_rho_sj: 0.2367\n    re_full_rho_fk: 0.2221\n    re_full_p_sj: 1.85e-06\n    re_full_p_fk: 7.92e-06\n    re_full_n: 397\n    re_cond_rho_sj: 0.3004\n    re_cond_rho_fk: 0.2374\n    re_cond_p_sj: 2.25e-08\n    re_cond_p_fk: 1.19e-05\n    re_cond_n: 333\n    re_sj_beats_fk_full: true\n    re_sj_beats_fk_cond: true\n    re_rho_advantage: 0.0146\n    re_sample_f1_mean: 0.1977\n    re_sample_f1_std: 0.3251\n    re_sample_f1_pct_zero: 67.6\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 64\n    parse_failures_stochastic: 0\n    parse_failures_greedy: 0\n    total_stochastic_samples: 4408\n    total_greedy: 551\n    verdict: FAIL\n    verdict_reason: RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but\n      below PASS bar\n- exp_id: ft_002_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch: 5\n    train_loss: 0.0806\n    eval_loss: 0.089\n    train_runtime: 28m41s\n    train_samples_per_second: 5.407\n    train_steps_per_second: 0.34\n    total_steps: 585\n    checkpoints:\n    - checkpoint-400\n    - checkpoint-500\n    - checkpoint-585\n    gate0_final_ner_f1: 0.6615\n    gate0_final_re_f1: 0.4177\n    gate0_final_parse_failures: 0\n    gate0_final_ner_pass: true\n    gate0_final_re_pass: true\n    gate0_final_pass: true\n    gate0_ckpt400_ner_f1: 0.6475\n    gate0_ckpt400_re_f1: 0.3793\n    gate0_ckpt400_parse_failures: 0\n    gate0_ckpt400_verdict: FAIL\n    gate0_ckpt400_re_sample_f1_pct_zero: 58.8\n    gate0_ckpt400_warning: '>30% samples F1=0'\n- exp_id: mvp_pilot_004\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.6671\n    ner_oracle_f1: 0.7756\n    ner_headroom: 0.1085\n    ner_fleiss_kappa_mean: 0.4048\n    ner_soft_jaccard_mean: 0.7008\n    ner_full_rho_fk: 0.259\n    ner_full_rho_sj: 0.3825\n    ner_full_n: 529\n    ner_cond_rho_fk: 0.2352\n    ner_cond_rho_sj: 0.3762\n    ner_cond_n: 508\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_sample_f1_mean: 0.6084\n    ner_sample_f1_std: 0.3174\n    ner_sample_f1_pct_zero: 12.19\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 21\n    re_greedy_f1: 0.4208\n    re_oracle_f1: 0.5882\n    re_headroom: 0.1674\n    re_fleiss_kappa_mean: 0.2996\n    re_soft_jaccard_mean: 0.6114\n    re_full_rho_fk: 0.2782\n    re_full_rho_sj: 0.2441\n    re_full_n: 397\n    re_cond_rho_fk: 0.3067\n    re_cond_rho_sj: 0.3161\n    re_cond_n: 313\n    re_sj_beats_fk_full: false\n    re_sj_beats_fk_cond: true\n    re_sample_f1_mean: 0.3612\n    re_sample_f1_std: 0.383\n    re_sample_f1_pct_zero: 44.3\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 84\n    parse_failures: 0\n    verdict: FAIL\n- exp_id: mvp_pilot_005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.6619\n    ner_oracle_f1: 0.7585\n    ner_headroom: 0.0966\n    ner_fleiss_kappa_mean: 0.4722\n    ner_soft_jaccard_mean: 0.7757\n    ner_full_rho_sj: 0.3875\n    ner_full_rho_fk: 0.3211\n    ner_full_n: 529\n    ner_cond_rho_sj: 0.3868\n    ner_cond_rho_fk: 0.305\n    ner_cond_n: 504\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_rho_advantage: 0.0664\n    ner_sample_f1_mean: 0.6243\n    ner_sample_f1_std: 0.3131\n    ner_sample_f1_pct_zero: 11.2\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 25\n    re_greedy_f1: 0.4219\n    re_oracle_f1: 0.5532\n    re_headroom: 0.1313\n    re_fleiss_kappa_mean: 0.3829\n    re_soft_jaccard_mean: 0.687\n    re_full_rho_sj: 0.2343\n    re_full_rho_fk: 0.1835\n    re_full_n: 397\n    re_cond_rho_sj: 0.3716\n    re_cond_rho_fk: 0.2533\n    re_cond_n: 301\n    re_sj_beats_fk_full: true\n    re_sj_beats_fk_cond: true\n    re_rho_advantage: 0.0508\n    re_sample_f1_mean: 0.3782\n    re_sample_f1_std: 0.3845\n    re_sample_f1_pct_zero: 42.4\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 96\n    parse_failures: 0\n    verdict: FAIL\n    verdict_note: RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional\n      but not full threshold\n- exp_id: e1_component_wise_re_sj\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    full_head_sj_rho: 0.21\n    full_tail_sj_rho: 0.201\n    full_type_match_rho: 0.201\n    full_multiplicative_rho: 0.244\n    full_additive_rho: 0.243\n    full_fleiss_kappa_rho: 0.278\n    cond_head_sj_rho: 0.27\n    cond_tail_sj_rho: 0.259\n    cond_type_match_rho: 0.252\n    cond_multiplicative_rho: 0.316\n    cond_additive_rho: 0.306\n    cond_fleiss_kappa_rho: 0.307\n    n_full: 397\n    n_conditional: 313\n    diagnosis: 'head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis\n      REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for\n      RE.'\n- exp_id: exp_012_logprob_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho_sj: 0.3565\n    ner_full_rho_fk: 0.2651\n    ner_full_rho_logprob: 0.1396\n    ner_full_rho_greedy_logprob: 0.1615\n    ner_full_tau_sj: 0.2658\n    ner_full_tau_logprob: 0.1006\n    ner_full_auroc_sj: 0.6892\n    ner_full_auroc_fk: 0.6292\n    ner_full_auroc_logprob: 0.5907\n    ner_full_n: 529\n    ner_sj_vs_logprob_delta: 0.2169\n    re_full_rho_sj: 0.2112\n    re_full_rho_fk: 0.2528\n    re_full_rho_logprob: 0.2467\n    re_full_auroc_sj: 0.5916\n    re_full_auroc_fk: 0.6262\n    re_full_auroc_logprob: 0.6186\n    re_full_n: 397\n    re_cond_rho_sj: 0.3683\n    re_cond_rho_fk: 0.3168\n    re_cond_rho_logprob: 0.1457\n    re_cond_auroc_sj: 0.6839\n    re_cond_auroc_logprob: 0.5487\n    re_cond_n: 296\n    diagnosis: 'NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead.\n      RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.'\n- exp_id: exp_013_exact_match_voting\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_full_rho: 0.2941\n    ner_full_p: 5.12e-12\n    ner_full_tau: 0.2181\n    ner_full_auroc: 0.6398\n    re_full_rho: 0.1562\n    re_full_p: 0.0018\n    re_full_tau: 0.1185\n    re_full_auroc: 0.5863\n    diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\n- exp_id: exp_014_entity_majority_voting\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho: 0.3915\n    ner_full_p: 8.1e-21\n    ner_full_tau: 0.2906\n    ner_full_auroc: 0.7039\n    re_full_rho: 0.3403\n    re_full_p: 3.21e-12\n    re_full_tau: 0.256\n    re_full_auroc: 0.6668\n    ner_voting_f1: 0.6246\n    ner_greedy_f1: 0.6483\n    ner_oracle_f1: 0.7793\n    re_voting_f1: 0.3577\n    re_greedy_f1: 0.4022\n    re_oracle_f1: 0.5886\n    diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE\n      (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\n- exp_id: exp_001_ner_n16_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_instances: 551\n    ner_n: 529\n    re_n: 397\n    N: 16\n    T: 1\n    seed: 42\n    full_test_set: true\n    ner_voting_conf_rho: 0.399\n    ner_sj_rho: 0.398\n    ner_em_rho: 0.339\n    ner_fk_rho: 0.288\n    ner_logprob_rho: 0.237\n    ner_voting_conf_auroc: 0.704\n    ner_sj_auroc: 0.697\n    ner_cond_em_rho: 0.414\n    ner_cond_sj_rho: 0.349\n    ner_cond_vc_rho: 0.34\n    re_voting_conf_rho: 0.38\n    re_logprob_rho: 0.293\n    re_fk_rho: 0.281\n    re_sj_rho: 0.277\n    re_em_rho: 0.148\n    re_voting_conf_auroc: 0.699\n    re_cond_em_rho: 0.475\n    re_cond_sj_rho: 0.318\n    re_cond_vc_rho: 0.35\n    re_cond_em_auroc: 0.742\n    diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380).\n      EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full\n      FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact of\n      200 instances + T=0.7.'\n- exp_id: exp_002_ner_conll2003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_003_ner_wnut17\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      greedy_f1: 0.525\n      oracle_f1: 0.664\n      headroom: 0.139\n      rho_sj_full: 0.082\n      rho_fk_full: 0.124\n      rho_logprob_full: -0.414\n      rho_sj_cond: 0.275\n      rho_fk_cond: 0.164\n      rho_logprob_cond: 0.352\n      sj_beats_logprob_cond: false\n    n_instances: 1287\n    n_gold_empty: 598\n    sample_f1_mean: 0.401\n    sample_f1_pct_zero: 53.7\n    N: 16\n    T: 1\n    seed: 42\n    verdict: FAIL\n    verdict_note: '>30% samples F1=0; structural rho weak; logprob baseline stronger'\n- exp_id: exp_007_ner_multi_model\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch: 5\n    train_loss: 0.0767\n    eval_loss: 0.1049\n    train_runtime_sec: 1494.5\n    train_samples_per_second: 6.226\n    checkpoints:\n    - checkpoint-400\n    - checkpoint-500\n    - checkpoint-585\n    base_model: Meta-Llama-3.1-8B-Instruct\n    lora_r: 32\n    lora_alpha: 64\n    note: EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal.\n      Checkpoint fully intact.\n- exp_id: exp_007_ner_llama\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_015_metrics_expansion\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_012_logprob/samples_with_logprobs.jsonl\n    config: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\n    ner:\n      n_valid: 529\n      n_cond: 501\n      voting_rho_full: 0.5018\n      voting_rho_cond: 0.4497\n      voting_auroc: 0.7279\n      voting_tau: 0.3766\n      sj_rho_full: 0.3565\n      sj_rho_cond: 0.412\n      sj_auroc: 0.6656\n      sj_tau: 0.2658\n      em_rho_full: 0.2566\n      em_rho_cond: 0.3427\n      em_auroc: 0.623\n      em_tau: 0.1924\n      fk_rho_full: 0.2651\n      fk_rho_cond: 0.306\n      fk_auroc: 0.6243\n      fk_tau: 0.2027\n      logprob_rho_full: 0.1396\n      logprob_rho_cond: 0.1627\n      logprob_auroc: 0.5585\n      logprob_tau: 0.1006\n    re:\n      n_valid: 397\n      n_cond: 296\n      voting_rho_full: 0.4217\n      voting_rho_cond: 0.463\n      voting_auroc: 0.7162\n      voting_tau: 0.327\n      sj_rho_full: 0.2112\n      sj_rho_cond: 0.3683\n      sj_auroc: 0.5816\n      sj_tau: 0.1619\n      em_rho_full: 0.1002\n      em_rho_cond: 0.3607\n      em_auroc: 0.5036\n      em_tau: 0.0839\n      fk_rho_full: 0.2528\n      fk_rho_cond: 0.3168\n      fk_auroc: 0.6308\n      fk_tau: 0.1967\n      logprob_rho_full: 0.2467\n      logprob_rho_cond: 0.1457\n      logprob_auroc: 0.6354\n      logprob_tau: 0.1808\n    diagnosis: 'Unified 5-signal evaluation on single data source. Voting leads NER\n      full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals\n      beat logprob on NER. RE: voting leads both full and cond.'\n- exp_id: exp_004_re_diagnostic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    per_relation_type:\n      HYPONYM-OF:\n        n: 36\n        rho_sj: 0.545\n        rho_fk: 0.646\n        rho_vc: 0.628\n        mean_f1: 0.513\n      CONJUNCTION:\n        n: 86\n        rho_sj: 0.383\n        rho_fk: 0.35\n        rho_vc: 0.484\n        mean_f1: 0.48\n      USED-FOR:\n        n: 299\n        rho_sj: 0.236\n        rho_fk: 0.255\n        rho_vc: 0.286\n        mean_f1: 0.422\n      PART-OF:\n        n: 44\n        rho_sj: 0.239\n        rho_fk: 0.348\n        rho_vc: 0.283\n        mean_f1: 0.297\n      EVALUATE-FOR:\n        n: 62\n        rho_sj: 0.172\n        rho_fk: 0.255\n        rho_vc: 0.226\n        mean_f1: 0.365\n      COMPARE:\n        n: 35\n        rho_sj: 0.168\n        rho_fk: 0.184\n        rho_vc: 0.18\n        mean_f1: 0.453\n      FEATURE-OF:\n        n: 50\n        rho_sj: 0.004\n        rho_fk: 0.052\n        rho_vc: 0.014\n        mean_f1: 0.254\n    error_propagation:\n      total_fn: 553\n      tail_error_pct: 21.9\n      full_error_pct: 21.7\n      head_error_pct: 17.7\n      head_tail_error_pct: 15.9\n      type_error_pct: 8.3\n      worst_consistency: head_type_error (sj=0.411)\n      best_consistency: head_error (sj=0.613)\n    threshold_sensitivity:\n      thr_0.00_rho_sj: 0.3161\n      thr_0.00_rho_vc: 0.3841\n      thr_0.00_n: 313\n      thr_0.05_rho_sj: 0.2682\n      thr_0.05_rho_vc: 0.2364\n      thr_0.05_n: 239\n    bootstrap_ci_95:\n      ner_sj:\n      - 0.2946\n      - 0.4586\n      ner_voting_conf:\n      - 0.3048\n      - 0.4656\n      re_sj:\n      - 0.1422\n      - 0.3391\n      re_voting_conf:\n      - 0.1818\n      - 0.3721\n      re_cond_sj:\n      - 0.2161\n      - 0.4102\n      re_cond_voting_conf:\n      - 0.2825\n      - 0.474\n    fisher_z_ner_vs_re:\n      sj_z: 2.31\n      sj_p: 0.0209\n      sj_significant: true\n      fk_z: -0.31\n      fk_p: 0.756\n      fk_significant: false\n      voting_z: 1.914\n      voting_p: 0.0556\n      voting_significant: false\n    diagnosis: FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF\n      strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of\n      RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE\n      signal in conditional set (rho=0.384).\n- exp_id: exp_008_re_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.6635\n      oracle_f1: 0.8208\n      headroom: 0.1572\n      rho_sj_full: 0.377\n      rho_fk_full: 0.2508\n      rho_logprob_full: 0.3153\n      rho_sj_cond: 0.3598\n      rho_fk_cond: 0.2251\n      rho_logprob_cond: 0.2927\n      sj_beats_fk: true\n      rho_advantage: 0.1262\n    re:\n      greedy_f1: 0.4339\n      oracle_f1: 0.6658\n      headroom: 0.2319\n      rho_sj_full: 0.2966\n      rho_fk_full: 0.2871\n      rho_logprob_full: 0.2986\n      rho_sj_cond: 0.3975\n      rho_fk_cond: 0.3774\n      rho_logprob_cond: 0.2745\n      sj_beats_fk: true\n      rho_advantage: 0.0095\n    verdict: FAIL\n- exp_id: exp001_seed123\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp001_seed456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_re_n16\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_n16_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.655\n      oracle_f1: 0.8028\n      headroom: 0.1478\n      rho_sj_full: 0.4076\n      rho_fk_full: 0.2799\n      rho_logprob_full: 0.3189\n      rho_sj_cond: 0.4271\n      rho_fk_cond: 0.2743\n      rho_logprob_cond: 0.2835\n      sj_beats_fk: true\n      rho_advantage: 0.1277\n    re:\n      greedy_f1: 0.4243\n      oracle_f1: 0.6771\n      headroom: 0.2528\n      rho_sj_full: 0.2943\n      rho_fk_full: 0.2657\n      rho_logprob_full: 0.3005\n      rho_sj_cond: 0.4003\n      rho_fk_cond: 0.313\n      rho_logprob_cond: 0.2317\n      sj_beats_fk: true\n      rho_advantage: 0.0286\n    verdict: FAIL\n- exp_id: exp_001_n16_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.6577\n      oracle_f1: 0.8129\n      headroom: 0.1553\n      rho_sj_full: 0.3297\n      rho_fk_full: 0.2578\n      rho_logprob_full: 0.2866\n      rho_sj_cond: 0.3394\n      rho_fk_cond: 0.2721\n      rho_logprob_cond: 0.2567\n      sj_beats_fk: true\n      rho_advantage: 0.0719\n    re:\n      greedy_f1: 0.4312\n      oracle_f1: 0.6737\n      headroom: 0.2425\n      rho_sj_full: 0.285\n      rho_fk_full: 0.2372\n      rho_logprob_full: 0.2626\n      rho_sj_cond: 0.3525\n      rho_fk_cond: 0.2614\n      rho_logprob_cond: 0.1927\n      sj_beats_fk: true\n      rho_advantage: 0.0478\n    verdict: FAIL\n- exp_id: exp_016_signal_ensemble\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_logprob_pearson_ner: 0.57\n    sj_logprob_pearson_re: 0.42\n    best_linear_ner:\n      combo: SJ+voting_conf\n      alpha: 0.3\n      rho: 0.489\n    best_linear_re:\n      combo: voting_conf+logprob\n      alpha: 0.6\n      rho: 0.429\n    ensemble_ner_auroc: 0.735\n    ensemble_re_auroc: 0.719\n    best_single_ner_auroc: 0.7\n    best_single_re_auroc: 0.721\n    ensemble_ner_delta: 0.035\n    selection_f1_ner:\n      greedy: 0.609\n      logprob: 0.609\n      sj: 0.604\n      ensemble: 0.604\n      voting: 0.596\n      random: 0.58\n      oracle: 0.769\n    selection_f1_re:\n      logprob: 0.397\n      greedy: 0.374\n      sj: 0.368\n      ensemble: 0.367\n      voting: 0.338\n      random: 0.338\n      oracle: 0.561\n    diagnosis: 'SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best\n      is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER.\n      Oracle gap still huge.'\n- exp_id: exp_002_merge_conll2003\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_rho_full: 0.4357\n    sj_tau_full: 0.3851\n    sj_auroc_full: 0.8008\n    sj_rho_cond: 0.4511\n    fk_rho_full: 0.3998\n    fk_tau_full: 0.3568\n    fk_auroc_full: 0.7741\n    fk_rho_cond: 0.4064\n    logprob_rho_full: 0.3157\n    logprob_tau_full: 0.2469\n    logprob_auroc_full: 0.7532\n    logprob_rho_cond: 0.3562\n    em_rho_full: 0.4507\n    em_tau_full: 0.4002\n    em_auroc_full: 0.8156\n    em_rho_cond: 0.4799\n    ev_rho_full: 0.4237\n    ev_tau_full: 0.3777\n    ev_auroc_full: 0.7889\n    ev_rho_cond: 0.4127\n    greedy_f1: 0.9123\n    oracle_f1: 0.9543\n    voting_f1: 0.9141\n    oracle_headroom: 0.042\n    sj_vs_logprob_delta_rho: 0.12\n    sj_vs_logprob_ci_low: 0.0881\n    sj_vs_logprob_ci_high: 0.154\n    sj_vs_logprob_significant: true\n    n_instances: 3453\n    n_valid: 2756\n    n_samples: 8\n    temperature: 1\n- exp_id: exp_001_n16_seed123_full\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_n16_seed456_full\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_008_re_n16_full\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_ner_n16_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.663\n      oracle_f1: 0.809\n      headroom: 0.146\n      rho_sj: 0.423\n      rho_fk: 0.29\n      rho_logprob: 0.239\n      rho_sj_cond: 0.423\n      rho_fk_cond: 0.26\n    re:\n      greedy_f1: 0.419\n      oracle_f1: 0.625\n      headroom: 0.206\n      rho_sj: 0.267\n      rho_fk: 0.315\n      rho_sj_cond: 0.364\n      rho_fk_cond: 0.331\n    verdict: FAIL\n    verdict_note: RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\n    n_instances: 551\n    seed: 123\n    N: 16\n    T: 1\n- exp_id: exp_001_seed456_t10_full\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      rho_sj: 0.414\n      rho_fk: 0.298\n    re:\n      rho_sj: 0.268\n      rho_fk: 0.26\n    n_instances: 551\n    N: 16\n    T: 1\n    seed: 456\n    source: reviewer_verified_report_json\n- exp_id: exp_001_seed123_t10_full\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      rho_sj: 0.417\n      rho_fk: 0.283\n    re:\n      rho_sj: 0.265\n      rho_fk: 0.315\n    n_instances: 551\n    N: 16\n    T: 1\n    seed: 123\n    source: reviewer_verified_report_json\n- exp_id: exp_008_re_n16_t10_full\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      rho_sj: 0.444\n    re:\n      rho_sj: 0.248\n    n_instances: 551\n    N: 16\n    T: 1\n    seed: 42\n    mode: RE-only\n    source: director_corrected\n- exp_id: exp_003_wnut17_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.523\n    oracle_f1: 0.664\n    headroom: 0.141\n    rho_fk: 0.125\n    rho_sj: 0.089\n    rho_fk_cond: 0.169\n    rho_sj_cond: 0.288\n    rho_logprob_full: -0.409\n    rho_logprob_cond: 0.35\n    structural_beats_surface: false\n    sample_f1_pct_zero: 53.7\n    n_instances: 1287\n    N: 16\n    T: 1\n    seed: 42\n    model: Qwen3-8B\n    n_gold_empty_filtered: 598\n    verdict: FAIL\n    verdict_note: structural_beats_surface=false; >50% samples F1=0\n- exp_id: exp_007_llama_inference\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.66\n      oracle_f1: 0.781\n      headroom: 0.121\n      rho_fk: 0.327\n      rho_sj: 0.363\n      rho_fk_cond: 0.226\n      rho_sj_cond: 0.311\n      rho_logprob: 0.183\n      rho_logprob_cond: 0.109\n      structural_beats_surface: true\n      sample_f1_pct_zero: 11.6\n    re:\n      greedy_f1: 0.434\n      oracle_f1: 0.568\n      headroom: 0.135\n      rho_fk: 0.305\n      rho_sj: 0.299\n      rho_fk_cond: 0.259\n      rho_sj_cond: 0.405\n      rho_logprob: 0.288\n      rho_logprob_cond: 0.092\n      structural_beats_surface: false\n      sample_f1_pct_zero: 41.2\n    n_instances: 551\n    N: 8\n    T: 1\n    seed: 42\n    model: LLaMA-3.1-8B-Instruct\n    verdict: FAIL\n    verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\n- exp_id: exp_001_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_rho_full: 0.428\n    sj_rho_cond: 0.369\n    structural_minus_surface: 0.147\n    conclusion_note: NER seed42 robustness confirmed, structural>surface +0.147\n- exp_id: exp_001_seed123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_rho_full: 0.424\n    sj_rho_cond: 0.376\n    structural_minus_surface: 0.149\n    conclusion_note: NER seed123 robustness confirmed, structural>surface +0.149\n- exp_id: exp_008_re_n16_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    sj_rho_full: 0.281\n    sj_rho_cond: 0.308\n    f1_zero_pct: 44.3\n    conclusion_note: 'RE N=16 v2 negative: SJ weak, 44.3% F1=0'\n- exp_id: exp_017_llama_conll\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_009_capability_stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n: 551\n      sj_rho_overall: 0.398\n      by_greedy_f1:\n        hard_0_25_sj_rho: 0.159\n        med_low_sj_rho: 0.139\n        med_high_sj_rho: 0.09\n        easy_sj_rho: 0.23\n      by_sent_len:\n        Q1_sj_rho: 0.461\n        Q2_sj_rho: 0.401\n        Q3_sj_rho: 0.296\n        Q4_sj_rho: 0.382\n      by_ent_count:\n        0_sj_rho: 0.689\n        1_2_sj_rho: 0.415\n        3_5_sj_rho: 0.353\n        6plus_sj_rho: 0.547\n    scierc_re:\n      n: 551\n      by_greedy_f1:\n        hard_0_25_sj_rho: -0.043\n        easy_sj_rho: 0.21\n      by_sent_len:\n        Q1_sj_rho: 0.447\n        Q4_sj_rho: 0.54\n      by_rel_count:\n        0_sj_rho: 0.62\n        1_2_sj_rho: 0.275\n        6plus_sj_rho: 0.527\n    conll_ner:\n      n: 3453\n      by_sent_len:\n        Q1_sj_rho: 0.334\n        Q3_sj_rho: 0.518\n    proxy_independence:\n      scierc_ner_f1_vs_slen: -0.021\n      scierc_ner_f1_vs_ecnt: 0.007\n      scierc_re_f1_vs_slen: -0.147\n- exp_id: exp_010_selection_curves\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n_instances: 551\n      greedy_f1: 0.618\n      N16:\n        oracle: 0.787\n        SJ: 0.62\n        FK: 0.621\n        logprob: 0.621\n        voting_conf: 0.585\n        EM: 0.606\n        random: 0.595\n      N8:\n        oracle: 0.752\n        SJ: 0.614\n        FK: 0.614\n        logprob: 0.619\n        voting_conf: 0.591\n        EM: 0.603\n        random: 0.589\n      N4:\n        oracle: 0.714\n        SJ: 0.607\n        FK: 0.608\n        logprob: 0.616\n        voting_conf: 0.594\n        EM: 0.6\n        random: 0.587\n    scierc_re:\n      n_instances: 397\n      greedy_f1: 0.403\n      N16:\n        oracle: 0.631\n        SJ: 0.397\n        FK: 0.396\n        logprob: 0.41\n        voting_conf: 0.408\n        EM: 0.381\n        random: 0.364\n      N8:\n        oracle: 0.583\n        SJ: 0.393\n        FK: 0.394\n        logprob: 0.413\n        voting_conf: 0.398\n        EM: 0.381\n        random: 0.363\n    conll_ner:\n      n_instances: 3453\n      greedy_f1: 0.725\n      N8:\n        oracle: 0.757\n        SJ: 0.718\n        FK: 0.717\n        logprob: 0.716\n        voting_conf: 0.714\n        EM: 0.716\n        random: 0.69\n      N4:\n        oracle: 0.746\n        SJ: 0.714\n        FK: 0.714\n        logprob: 0.715\n        voting_conf: 0.714\n        EM: 0.712\n        random: 0.692\n- exp_id: exp_007_llama_seed123\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    ner:\n      greedy_f1: 0.6605\n      oracle_f1: 0.7703\n      headroom: 0.1098\n      fleiss_kappa: 0.4553\n      soft_jaccard: 0.7525\n      rho_kappa_f1: 0.2143\n      rho_sj_f1: 0.3371\n      structural_gt_surface: true\n    re:\n      greedy_f1: 0.433\n      oracle_f1: 0.5719\n      headroom: 0.1389\n      fleiss_kappa: 0.3851\n      soft_jaccard: 0.6911\n      rho_kappa_f1: 0.2844\n      rho_sj_f1: 0.268\n      structural_gt_surface: false\n    fail_reasons:\n    - RE rho_sj=0.2680 < 0.40 threshold\n    - '>30% samples F1=0 (RE: 41.0%)'\n    - RE structural not > surface (delta=-0.0165)\n- exp_id: exp_007_llama_seed456\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    ner:\n      greedy_f1: 0.6597\n      oracle_f1: 0.7575\n      oracle_headroom: 0.0978\n      fleiss_kappa: 0.4543\n      soft_jaccard: 0.7491\n      rho_kappa_f1: 0.3115\n      rho_sj_f1: 0.3663\n      structural_gt_surface: true\n    re:\n      greedy_f1: 0.4334\n      oracle_f1: 0.5789\n      oracle_headroom: 0.1455\n      fleiss_kappa: 0.3791\n      soft_jaccard: 0.6782\n      rho_kappa_f1: 0.3013\n      rho_sj_f1: 0.287\n      structural_gt_surface: false\n    logprob_ner:\n      rho: 0.1911\n      auroc: 0.5989\n    logprob_re:\n      rho: 0.3246\n      auroc: 0.6678\n    fail_reason: RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\n- exp_id: exp_008_re_seed123\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    greedy_f1: 0.4229\n    oracle_f1: 0.6244\n    oracle_headroom: 0.2015\n    fleiss_kappa_mean: 0.3455\n    soft_jaccard_mean: 0.6126\n    sample_f1_mean: 0.3594\n    sample_f1_std: 0.3793\n    sample_f1_zero_pct: 44.1\n    structural_gt_surface: false\n    rho_kappa_f1_full: 0.3174\n    rho_sj_f1_full: 0.2835\n    rho_kappa_f1_cond: 0.0766\n    rho_sj_f1_cond: 0.2877\n    logprob_auroc_full: 0.6499\n    logprob_auroc_cond: 0.5265\n    verdict: FAIL\n- exp_id: exp_005_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    NER_SciERC_s42:\n      greedy: 0.618\n      oracle: 0.787\n      SJ: 0.62\n      logprob: 0.621\n      FK: 0.621\n      EM: 0.606\n      voting_conf: 0.585\n      random: 0.586\n    NER_SciERC_s123:\n      greedy: 0.618\n      oracle: 0.785\n      SJ: 0.617\n      logprob: 0.618\n      FK: 0.621\n      EM: 0.613\n      voting_conf: 0.584\n      random: 0.583\n    NER_CoNLL:\n      greedy: 0.725\n      oracle: 0.757\n      SJ: 0.718\n      logprob: 0.716\n      FK: 0.717\n      EM: 0.716\n      voting_conf: 0.714\n      random: 0.692\n    RE_SciERC:\n      greedy: 0.403\n      oracle: 0.631\n      SJ: 0.397\n      logprob: 0.41\n      FK: 0.396\n      EM: 0.381\n      voting_conf: 0.408\n      random: 0.364\n- exp_id: exp_004_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_003_wnut17_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_015_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner_avg:\n      sj_auroc: 0.7394\n      fk_auroc: 0.6172\n      em_auroc: 0.7873\n      voting_auroc: 0.7367\n      logprob_auroc: 0.5918\n    scierc_re_avg:\n      sj_auroc: 0.6746\n      fk_auroc: 0.5939\n      em_auroc: 0.715\n      voting_auroc: 0.7234\n      logprob_auroc: 0.5849\n- exp_id: exp_009_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_seed42_global:\n      sj_rho: 0.431\n      fk_rho: 0.325\n      logprob_rho: 0.203\n      voting_conf_rho: 0.475\n      em_rho: 0.292\n    ner_seed123_global:\n      sj_rho: 0.422\n      fk_rho: 0.315\n      logprob_rho: 0.226\n      voting_conf_rho: 0.438\n      em_rho: 0.299\n    re_seed42_global:\n      sj_rho: 0.063\n      fk_rho: 0.226\n      logprob_rho: 0.4\n      voting_conf_rho: 0.22\n      em_rho: -0.132\n    ner_seed_stability_max_delta: 0.037\n    independent_proxies:\n    - sent_len\n    - ent_count\n    - type_diversity\n    inverted_u_ner: not confirmed (ρ stable across independent proxies)\n    inverted_u_re: monotonic increase with complexity, not inverted-U\n- exp_id: exp_001_seed456_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_016_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_conditional:\n      n: 529\n      best_single_signal_rho:\n        soft_jaccard: 0.4412\n      best_combo_rho:\n        sj+vc_a0.55: 0.4552\n      ensemble_auroc: 0.7141\n      best_single_auroc:\n        soft_jaccard: 0.7166\n      selection_f1:\n        greedy: 0.6442\n        logprob_best: 0.6505\n        ensemble_best: 0.6475\n        sj_best: 0.6471\n        oracle: 0.8442\n    re_conditional:\n      n: 397\n      best_single_signal_rho:\n        voting_confidence: 0.3849\n      best_combo_rho:\n        logprob+vc_a0.25: 0.3936\n      ensemble_auroc: 0.6916\n      best_single_auroc:\n        voting_confidence: 0.7023\n      selection_f1:\n        greedy: 0.403\n        logprob_best: 0.4097\n        ensemble_best: 0.4227\n        oracle: 0.6306\n    re_full:\n      ensemble_auroc: 0.8608\n      best_single_auroc:\n        voting_confidence: 0.8248\n- exp_id: exp_001_seed456_v2_ner\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full:\n      SJ:\n        rho: 0.384\n        auroc: 0.711\n      FK:\n        rho: 0.223\n        auroc: 0.577\n      logprob:\n        rho: 0.232\n        auroc: 0.594\n      EM:\n        rho: 0.316\n        auroc: 0.768\n      voting_conf:\n        rho: 0.411\n        auroc: 0.712\n    conditional:\n      SJ:\n        rho: 0.349\n        auroc: 0.699\n      FK:\n        rho: 0.157\n        auroc: 0.561\n      logprob:\n        rho: 0.171\n        auroc: 0.576\n      EM:\n        rho: 0.406\n        auroc: 0.78\n      voting_conf:\n        rho: 0.346\n        auroc: 0.694\n    3seed_mean_SJ_rho_full: 0.412\n    3seed_sd_SJ_rho_full: 0.025\n    structural_beats_surface: true\n    verdict: MARGINAL\n- exp_id: exp_017_llama_conll_infer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9266\n    oracle_f1: 0.9443\n    oracle_headroom: 0.0177\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    N: 8\n    full:\n      SJ_rho: 0.4314\n      FK_rho: 0.4277\n      logprob_rho: 0.3072\n      EM_rho: 0.4306\n      voting_conf_rho: 0.4256\n      SJ_AUROC: 0.7039\n      FK_AUROC: 0.7026\n      logprob_AUROC: 0.761\n      EM_AUROC: 0.7046\n      voting_conf_AUROC: 0.7088\n      SJ_ECE: 0.1137\n      FK_ECE: 0.1053\n      logprob_ECE: 0.129\n      EM_ECE: 0.1094\n      voting_conf_ECE: 0.0949\n    conditional:\n      SJ_rho: 0.4356\n      FK_rho: 0.431\n      logprob_rho: 0.3282\n      EM_rho: 0.4403\n      voting_conf_rho: 0.3743\n      SJ_AUROC: 0.7225\n      FK_AUROC: 0.7208\n      logprob_AUROC: 0.8102\n      EM_AUROC: 0.7257\n      voting_conf_AUROC: 0.6989\n      SJ_ECE: 0.0829\n      FK_ECE: 0.0796\n      logprob_ECE: 0.0922\n      EM_ECE: 0.0754\n      voting_conf_ECE: 0.0784\n- exp_id: exp_002_conll_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    N: 16\n    dataset: conll2003\n    subtask: ner\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2614\n    greedy_f1: 0.907\n    full:\n      SJ_rho: 0.4496\n      FK_rho: 0.3928\n      logprob_rho: 0.3146\n      EM_rho: 0.4627\n      voting_conf_rho: 0.4286\n      SJ_AUROC: 0.8264\n      FK_AUROC: 0.7821\n      logprob_AUROC: 0.7531\n      EM_AUROC: 0.8409\n      voting_conf_AUROC: 0.8071\n      SJ_ECE: 0.0747\n      FK_ECE: 0.1786\n      logprob_ECE: 0.2031\n      EM_ECE: 0.0786\n      voting_conf_ECE: 0.529\n    conditional:\n      SJ_rho: 0.4208\n      FK_rho: 0.3494\n      logprob_rho: 0.3756\n      EM_rho: 0.4658\n      voting_conf_rho: 0.3654\n      SJ_AUROC: 0.8405\n      FK_AUROC: 0.7819\n      logprob_AUROC: 0.8259\n      EM_AUROC: 0.8781\n      voting_conf_AUROC: 0.7951\n      SJ_ECE: 0.0982\n      FK_ECE: 0.1899\n      logprob_ECE: 0.2504\n      EM_ECE: 0.0997\n      voting_conf_ECE: 0.6096\n    n8_vs_n16_delta_rho_full:\n      SJ: 0.0139\n      FK: -0.007\n      logprob: -0.0011\n      EM: 0.012\n      voting_conf: 0.0049\n- exp_id: exp_007_llama_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    N: 16\n    dataset: scierc\n    subtask: ner\n    n_instances: 551\n    n_valid: 529\n    n_conditional: 478\n    greedy_f1: 0.645\n    full:\n      SJ_rho: 0.3791\n      FK_rho: 0.3081\n      logprob_rho: 0.2041\n      EM_rho: 0.3159\n      voting_conf_rho: 0.4515\n      SJ_AUROC: 0.717\n      FK_AUROC: 0.6581\n      logprob_AUROC: 0.5656\n      EM_AUROC: 0.7686\n      voting_conf_AUROC: 0.7266\n      SJ_ECE: 0.1019\n      FK_ECE: 0.1556\n      logprob_ECE: 0.084\n      EM_ECE: 0.1761\n      voting_conf_ECE: 0.1365\n    conditional:\n      SJ_rho: 0.3222\n      FK_rho: 0.2182\n      logprob_rho: 0.1286\n      EM_rho: 0.3563\n      voting_conf_rho: 0.3356\n      SJ_AUROC: 0.7014\n      FK_AUROC: 0.6392\n      logprob_AUROC: 0.545\n      EM_AUROC: 0.7708\n      voting_conf_AUROC: 0.6988\n      SJ_ECE: 0.1466\n      FK_ECE: 0.1853\n      logprob_ECE: 0.1141\n      EM_ECE: 0.1887\n      voting_conf_ECE: 0.2634\n    n8_vs_n16_delta_rho_full:\n      SJ: 0.0161\n      FK: -0.0185\n      logprob: 0.0214\n      EM: 0.0007\n      voting_conf: 0.0184\n- exp_id: exp_009_v2_re_rerun\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_017_llama_conll_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9243\n    oracle_f1: 0.9487\n    oracle_headroom: 0.0244\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    structural_beats_surface: true\n    full:\n      SJ_rho: 0.4642\n      SJ_AUROC: 0.7391\n      SJ_ECE: 0.1131\n      FK_rho: 0.4566\n      FK_AUROC: 0.736\n      FK_ECE: 0.1071\n      logprob_rho: 0.3058\n      logprob_AUROC: 0.7594\n      logprob_ECE: 0.1288\n      EM_rho: 0.4613\n      EM_AUROC: 0.7391\n      EM_ECE: 0.1084\n      voting_conf_rho: 0.4554\n      voting_conf_AUROC: 0.7406\n      voting_conf_ECE: 0.0844\n    conditional:\n      SJ_rho: 0.4597\n      SJ_AUROC: 0.7565\n      SJ_ECE: 0.0846\n      FK_rho: 0.4515\n      FK_AUROC: 0.753\n      FK_ECE: 0.0813\n      logprob_rho: 0.3193\n      logprob_AUROC: 0.8023\n      logprob_ECE: 0.0921\n      EM_rho: 0.4618\n      EM_AUROC: 0.7589\n      EM_ECE: 0.0757\n      voting_conf_rho: 0.3978\n      voting_conf_AUROC: 0.7287\n      voting_conf_ECE: 0.0742\n    best_of_n:\n      greedy: 0.9243\n      random_avg: 0.9213\n      sj_best: 0.9259\n      logprob_best: 0.925\n      voting_conf_best: 0.9268\n      oracle: 0.9487\n    n8_vs_n16_delta:\n      full_SJ_rho_delta: 0.0328\n      full_FK_rho_delta: 0.0289\n      full_logprob_rho_delta: -0.0014\n      full_EM_rho_delta: 0.0307\n      full_voting_conf_rho_delta: 0.0298\n      cond_SJ_rho_delta: 0.0241\n      cond_FK_rho_delta: 0.0205\n      cond_logprob_rho_delta: -0.0089\n      cond_EM_rho_delta: 0.0215\n      cond_voting_conf_rho_delta: 0.0235\n- exp_id: exp_017_llama_conll_n16_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9266\n    oracle_f1: 0.9497\n    oracle_headroom: 0.0231\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    structural_beats_surface: true\n    full:\n      SJ_rho: 0.4698\n      SJ_AUROC: 0.7402\n      SJ_ECE: 0.1135\n      FK_rho: 0.4594\n      FK_AUROC: 0.7351\n      FK_ECE: 0.1114\n      logprob_rho: 0.3161\n      logprob_AUROC: 0.768\n      logprob_ECE: 0.129\n      EM_rho: 0.4676\n      EM_AUROC: 0.7399\n      EM_ECE: 0.1082\n      voting_conf_rho: 0.4612\n      voting_conf_AUROC: 0.7429\n      voting_conf_ECE: 0.0832\n    conditional:\n      SJ_rho: 0.4712\n      SJ_AUROC: 0.7609\n      SJ_ECE: 0.0828\n      FK_rho: 0.4595\n      FK_AUROC: 0.7547\n      FK_ECE: 0.0858\n      logprob_rho: 0.3314\n      logprob_AUROC: 0.8134\n      logprob_ECE: 0.0922\n      EM_rho: 0.4732\n      EM_AUROC: 0.7626\n      EM_ECE: 0.075\n      voting_conf_rho: 0.4086\n      voting_conf_AUROC: 0.7338\n      voting_conf_ECE: 0.0706\n    best_of_n:\n      greedy: 0.9242\n      random_avg: 0.9216\n      sj_best: 0.9247\n      logprob_best: 0.9253\n      voting_conf_best: 0.9255\n      oracle: 0.9486\n    n8_vs_n16_delta:\n      full_SJ_rho_delta: 0.0384\n      full_FK_rho_delta: 0.0317\n      full_logprob_rho_delta: 0.0089\n      full_SJ_AUROC_delta: 0.0363\n      full_FK_AUROC_delta: 0.0325\n      full_logprob_AUROC_delta: 0.007\n      cond_SJ_rho_delta: 0.0356\n      cond_FK_rho_delta: 0.0285\n      cond_logprob_rho_delta: 0.0032\n- exp_id: exp_017_llama_conll_n16_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9243\n    oracle_f1: 0.9488\n    oracle_headroom: 0.0245\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    structural_beats_surface: true\n    full:\n      SJ_rho: 0.4552\n      SJ_AUROC: 0.7288\n      SJ_ECE: 0.1134\n      FK_rho: 0.4478\n      FK_AUROC: 0.7248\n      FK_ECE: 0.109\n      logprob_rho: 0.3078\n      logprob_AUROC: 0.7612\n      logprob_ECE: 0.1289\n      EM_rho: 0.452\n      EM_AUROC: 0.7275\n      EM_ECE: 0.1082\n      voting_conf_rho: 0.4571\n      voting_conf_AUROC: 0.7348\n      voting_conf_ECE: 0.0863\n    conditional:\n      SJ_rho: 0.4505\n      SJ_AUROC: 0.7449\n      SJ_ECE: 0.0826\n      FK_rho: 0.4422\n      FK_AUROC: 0.7401\n      FK_ECE: 0.0835\n      logprob_rho: 0.3242\n      logprob_AUROC: 0.8067\n      logprob_ECE: 0.0921\n      EM_rho: 0.451\n      EM_AUROC: 0.745\n      EM_ECE: 0.0756\n      voting_conf_rho: 0.3962\n      voting_conf_AUROC: 0.7202\n      voting_conf_ECE: 0.0746\n    best_of_n:\n      greedy: 0.9243\n      random_avg: 0.9215\n      sj_best: 0.9243\n      logprob_best: 0.9243\n      voting_conf_best: 0.9243\n      oracle: 0.9488\n    n8_vs_n16_delta:\n      full_SJ_rho_delta: 0.0238\n      full_FK_rho_delta: 0.0201\n      full_logprob_rho_delta: 0.0006\n      full_EM_rho_delta: 0.0214\n      full_voting_conf_rho_delta: 0.0315\n      cond_SJ_rho_delta: 0.0149\n      cond_FK_rho_delta: 0.0112\n      cond_logprob_rho_delta: -0.004\n      cond_EM_rho_delta: 0.0107\n      cond_voting_conf_rho_delta: 0.0219\n- exp_id: exp_012_rerun_1024\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full:\n      n: 529\n      SJ:\n        rho: 0.3599\n        tau: 0.2646\n        AUROC: 0.6917\n        ECE: 0.4531\n        rho_ci95:\n        - 0.2732\n        - 0.4389\n        AUROC_ci95:\n        - 0.6304\n        - 0.7406\n      FK:\n        rho: 0.2665\n        tau: 0.1974\n        AUROC: 0.629\n        ECE: 0.4512\n        rho_ci95:\n        - 0.1743\n        - 0.3486\n        AUROC_ci95:\n        - 0.5612\n        - 0.6882\n      logprob:\n        rho: 0.2052\n        tau: 0.1478\n        AUROC: 0.5783\n        ECE: 0.7064\n        rho_ci95:\n        - 0.1171\n        - 0.2904\n        AUROC_ci95:\n        - 0.5179\n        - 0.6387\n      EM:\n        rho: 0.2945\n        tau: 0.2208\n        AUROC: 0.7493\n        ECE: 0.3526\n        rho_ci95:\n        - 0.2094\n        - 0.37\n        AUROC_ci95:\n        - 0.7002\n        - 0.7928\n      voting_conf:\n        rho: 0.3792\n        tau: 0.2805\n        AUROC: 0.6841\n        ECE: 0.3807\n        rho_ci95:\n        - 0.2972\n        - 0.4486\n        AUROC_ci95:\n        - 0.6249\n        - 0.7366\n    ner_cond:\n      n: 477\n      SJ:\n        rho: 0.3113\n        tau: 0.2257\n        AUROC: 0.6772\n        ECE: 0.4416\n        rho_ci95:\n        - 0.2353\n        - 0.3959\n        AUROC_ci95:\n        - 0.621\n        - 0.7337\n      FK:\n        rho: 0.1761\n        tau: 0.1284\n        AUROC: 0.6078\n        ECE: 0.4389\n        rho_ci95:\n        - 0.0839\n        - 0.2665\n        AUROC_ci95:\n        - 0.5442\n        - 0.6709\n      logprob:\n        rho: 0.1538\n        tau: 0.1111\n        AUROC: 0.5633\n        ECE: 0.6803\n        rho_ci95:\n        - 0.0637\n        - 0.2424\n        AUROC_ci95:\n        - 0.5032\n        - 0.6232\n      EM:\n        rho: 0.3596\n        tau: 0.2735\n        AUROC: 0.7556\n        ECE: 0.3257\n        rho_ci95:\n        - 0.2819\n        - 0.4408\n        AUROC_ci95:\n        - 0.7011\n        - 0.8107\n      voting_conf:\n        rho: 0.3\n        tau: 0.2189\n        AUROC: 0.6618\n        ECE: 0.3746\n        rho_ci95:\n        - 0.2168\n        - 0.3836\n        AUROC_ci95:\n        - 0.6004\n        - 0.7201\n    re_full:\n      n: 397\n      SJ:\n        rho: 0.2503\n        tau: 0.1878\n        AUROC: 0.6702\n        ECE: 0.3865\n      FK:\n        rho: 0.2752\n        tau: 0.2117\n        AUROC: 0.6089\n        ECE: 0.4405\n      logprob:\n        rho: 0.2662\n        tau: 0.1951\n        AUROC: 0.6005\n        ECE: 0.7694\n      EM:\n        rho: 0.1344\n        tau: 0.1081\n        AUROC: 0.7059\n        ECE: 0.3548\n      voting_conf:\n        rho: 0.3498\n        tau: 0.2663\n        AUROC: 0.6935\n        ECE: 0.2724\n    re_cond:\n      n: 238\n      SJ:\n        rho: 0.2457\n        tau: 0.1811\n        AUROC: 0.6463\n        ECE: 0.2941\n      FK:\n        rho: 0.1139\n        tau: 0.0876\n        AUROC: 0.551\n        ECE: 0.3424\n      logprob:\n        rho: 0.0112\n        tau: 0.0051\n        AUROC: 0.5186\n        ECE: 0.6464\n      EM:\n        rho: 0.4165\n        tau: 0.3256\n        AUROC: 0.7515\n        ECE: 0.2232\n      voting_conf:\n        rho: 0.2409\n        tau: 0.178\n        AUROC: 0.642\n        ECE: 0.207\n    delta_vs_512_ner_full_rho:\n      SJ: 0.0034\n      FK: 0.0014\n      EM: 0.0379\n      voting_conf: -0.1226\n      logprob: 0.0656\n    provenance_note: exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512\n      truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed\n      0.140→0.205.\n- exp_id: exp_001_seed42_v2_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    greedy_f1: 0.6647\n    oracle_f1: 0.8106\n    softjaccard_rho_full: 0.3928\n    fleiss_rho_full: 0.2489\n    logprob_rho_full: 0.2136\n    softjaccard_rho_cond: 0.3455\n    fleiss_rho_cond: 0.163\n    logprob_rho_cond: 0.1624\n    verdict: MARGINAL\n- exp_id: exp_001_seed123_v2_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_seed456_v2_ner_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002_conll_n16_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_007_llama_n16_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_017_llama_conll_n16_r1024\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_017_llama_conll_n16_s123_r1024\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_017_llama_conll_n16_s456_r1024\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_016_rerun_1024_bootstrap\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bootstrap_ci_95:\n    - -0.03\n    - 0.042\n    permutation_p: 0.39\n    cohen_d: 0.038\n    sign_test_win_rate: 0.466\n    ner_logprob_vs_greedy_delta: 0.006\n    conclusion_summary: 'NER selection: no signal significantly outperforms greedy;\n      RE: same conclusion'\n- exp_id: exp_018_qwen_scierc_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_018_qwen_scierc_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_018_llama_scierc_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_018_llama_scierc_seed456\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_018_llama_scierc_seed42_r1024\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      full:\n        SJ:\n          rho: 0.3096\n          tau: 0.2288\n          auroc: 0.6683\n        FK:\n          rho: 0.2352\n          tau: 0.1759\n          auroc: 0.6069\n        logprob:\n          rho: 0.1503\n          tau: 0.1087\n          auroc: 0.5318\n        EM:\n          rho: 0.2587\n          tau: 0.1966\n          auroc: 0.7174\n        voting_conf:\n          rho: 0.4053\n          tau: 0.3042\n          auroc: 0.6967\n      conditional:\n        SJ:\n          rho: 0.2718\n          tau: null\n          auroc: 0.6565\n        FK:\n          rho: 0.1472\n          tau: null\n          auroc: 0.5866\n        logprob:\n          rho: 0.081\n          tau: null\n          auroc: 0.5129\n        EM:\n          rho: 0.3165\n          tau: null\n          auroc: 0.7244\n        voting_conf:\n          rho: 0.3078\n          tau: null\n          auroc: 0.6714\n      greedy_f1: 0.6607\n      oracle_f1: 0.7781\n      n_full: 529\n      n_cond: 478\n    re:\n      full:\n        SJ:\n          rho: 0.2748\n          tau: 0.2102\n          auroc: 0.7244\n        FK:\n          rho: 0.3027\n          tau: 0.2337\n          auroc: 0.691\n        logprob:\n          rho: 0.3163\n          tau: 0.233\n          auroc: 0.6313\n        EM:\n          rho: 0.1681\n          tau: 0.1275\n          auroc: 0.7697\n        voting_conf:\n          rho: 0.384\n          tau: 0.2965\n          auroc: 0.7337\n      conditional:\n        SJ:\n          rho: 0.3461\n          tau: null\n          auroc: 0.7233\n        FK:\n          rho: 0.1969\n          tau: null\n          auroc: 0.6684\n        logprob:\n          rho: 0.0888\n          tau: null\n          auroc: 0.5556\n        EM:\n          rho: 0.4969\n          tau: null\n          auroc: 0.819\n        voting_conf:\n          rho: 0.3433\n          tau: null\n          auroc: 0.7003\n      greedy_f1: 0.4319\n      oracle_f1: 0.5775\n      n_full: 397\n      n_cond: 251\n- exp_id: exp_018_llama_scierc_seed456_r1024\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_greedy_f1: 0.6597\n    ner_oracle_f1: 0.7683\n    ner_oracle_headroom: 0.1086\n    ner_cond_rho_fk: 0.1472\n    ner_cond_rho_sj: 0.2718\n    ner_cond_rho_logprob: 0.083\n    ner_logprob_auroc_cond: 0.5485\n    re_greedy_f1: 0.4338\n    re_oracle_f1: 0.5834\n    re_oracle_headroom: 0.1496\n    re_cond_rho_fk: 0.2107\n    re_cond_rho_sj: 0.3898\n    re_cond_rho_logprob: 0.1252\n    re_logprob_auroc_cond: 0.6119\n    ner_structural_beats_logprob: true\n    re_structural_beats_logprob: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T09:42:22.808Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T09:42:22.808Z",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-15T09:42:22.855Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Free-form 未恢复 selection ability；constrained decoding bottleneck 假说不成立，gap 源于 IE 本身
核心假设：['exp-018: logprob variance 提升微弱（range 中位数 <0.10）或虽提升但 selection 无改善', 'exp-018: free-form logprob selection vs greedy < +1pp，p>0.2，与 constrained 下结果无实质差异', 'parse rate 可能偏低（60-80%），且可解析子集本身偏向 easy instances（selection bias）', '机制假说被否定：score compression 不是 selection 失败的主因，问题在于 IE 输出空间的组合复杂性使得单一 scalar signal 根本无法有效排序', '回到 D070 前的 framing 困境：论文的 primary contribution 缩回为 systematic negative finding + QE evaluation']
关键指标范围：{'freeform_parse_rate': [0.6, 0.8], 'freeform_logprob_within_sample_range_median': [0.05, 0.1], 'freeform_logprob_rho_with_f1': [0.15, 0.25], 'freeform_logprob_selection_delta_vs_greedy_pp': [-1.0, 1.0], 'freeform_logprob_selection_p_value': [0.2, 0.8], 'freeform_logprob_auroc': [0.55, 0.6], 'constrained_logprob_rho_with_f1': [0.2, 0.21], 'constrained_logprob_auroc': [0.57, 0.58], 'expected_reviewer_score': [2.5, 3.0], 'findings_acceptance_prob': [0.1, 0.25]}
叙事方向：核心 reframing 失败，需要第二次 pivot。放弃 "bottleneck" 因果叙事， 转向 "fundamental selection hardness in structured prediction" angle： (1) IE 输出是 set-of-sets（entity set × relation set），其组合空间使得 任何 instance-level scalar signal 的排序能力存在 information-theoretic 上限； (2) 这与 reasoning/QA 的离散答案空间形成 structural contrast—— self-consistency 成功于后者恰因答案空间小； (3) QE 仍然有效（AUROC 0.75）说明信号捕捉了 difficulty 但无法区分 同一 difficulty 水平内的 quality variation。 Title 改为 "Why Self-Consistency Fails for Structured Prediction: The Selection Hardness of Set-Valued Outputs"。 Claim 1 变为 universal negative finding + structural explanation。 Claim 2 (QE framework) 升级为 primary contribution。 风险：与 pre-D070 framing 差距不大，reviewer 可能认为 depth 不够。 必须靠 (a) exp-018 作为 well-designed null result 的方法论严谨性， (b) information-theoretic argument 的新颖性来撑住分数。 仍冲 Findings，但需要 paper writing 极其精炼。

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
  "promptId": "0965ff8a-8ec3-49f6-a1d8-5784a79f070e",
  "type": "user",
  "uuid": "12705039-1a29-4f00-af2a-b231302ba333",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T09:42:22.846Z_

```json
{
  "parentUuid": "12705039-1a29-4f00-af2a-b231302ba333",
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
  "uuid": "b37880e5-941f-4dc4-bfb9-5df99ca06289",
  "timestamp": "2026-05-15T09:42:22.846Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T09:42:22.846Z_

```json
{
  "parentUuid": "b37880e5-941f-4dc4-bfb9-5df99ca06289",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b186de72-0a47-4161-aaac-ab1bf3c46e5e",
  "timestamp": "2026-05-15T09:42:22.846Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Free-form 未恢复 selection ability；constrained decoding bottleneck 假说不成立，gap 源于 IE 本身 核心假设：['exp-018: logprob variance 提升微弱（range 中位数 <0.10）或虽提升但 selection 无…",
  "leafUuid": "b186de72-0a47-4161-aaac-ab1bf3c46e5e",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Free-form decoding bottleneck verification for structured IE",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2"
}
```

---

### Assistant

_source line 8 · 2026-05-15T09:42:50.945Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for all "planned" experiments in the experiment_plan under the "worst" tier scenario. Let me identify which experiments are still "planned":

1. **exp-011** (ner_ood_robustness) - status: planned
2. **exp-017** (ner_llama_conll) - status: planned
3. **exp-018** (freeform_decoding_ablation) - status: planned
4. **exp-019** (simple_verifier_baseline) - status: planned


I'm noticing a discrepancy here—exp-017 and exp-018 are marked as "planned" in the experiment_plan, but the registry shows completed entries for both of them. Let me verify which experiments actually need predicted results generated. Looking at the planned experiments, I need to generate predictions for the four marked as planned in the experiment_plan, even though some like exp-017 and exp-018 already have partial registry data. The user wants detailed predictions for each one, so I'll work through them systematically: exp-011 which hasn't been started, exp-017 and exp-018 which have some results but are still listed as planned, and exp-019 which is also unstarted. I'm also considering the "worst" tier performance thresholds to establish realistic baseline expectations for what these experiments might show.

Now I'm laying out the specific metric ranges I expect to see across the freeform and constrained decoding experiments—things like parse rates, correlation with F1 scores, AUROC values, and statistical significance measures—to establish what would constitute disappointing versus acceptable results for each experiment.

For the key experiment, I'm predicting that even under worst-case conditions, freeform decoding won't recover the selection ability we're looking for; the logprob variance might improve marginally, but that won't translate to better selection performance, especially given the low parse rates and selection bias in the parseable subset. The cross-model validation on LLaMA should still show the same structural pattern we've already observed, since it's testing generalization rather than the core bottleneck. Out-of-distribution robustness would likely show even weaker signals under worst-case assumptions, and even a supervised verifier approach would struggle because the fundamental issue lies in IE's combinatorial output space.

Now I'm formatting these predictions into YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b186de72-0a47-4161-aaac-ab1bf3c46e5e",
  "isSidechain": false,
  "requestId": "req_011Cb48reQxuKVM2DUMP1Qij",
  "type": "assistant",
  "uuid": "22279167-d301-4aa2-953c-bc99f9d7e473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133NUTf1Q1DPZ4iQEhxR92Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 45061,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 45061,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8604,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 45061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 45061
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

_source line 9 · 2026-05-15T09:45:09.910Z_

```yaml
tier: worst
narrative_guidance: >
  Free-form decoding 未能恢复 logprob 的 selection 能力。Score compression 确实在 constrained decoding 下存在，
  但移除约束后 logprob variance 提升微弱（中位数 range 仅从 ~0.03 升至 ~0.07），且 selection F1 无实质改善。
  这否定了 "constrained decoding bottleneck" 因果假说——gap 并非 regime-specific，而是 IE set-valued output
  空间的组合复杂性使得任何 instance-level scalar signal 都缺乏排序能力。Paper 必须做第二次 pivot：
  从 "bottleneck identification + ablation verification" 退回到 "fundamental selection hardness in
  structured prediction" 的 universal negative finding + QE framework 作为 primary contribution。
  Parse rate 偏低（~70%）且可解析子集偏向 easy instances，进一步削弱 free-form 证据的可信度。

imagined_experiments:
  - name: "freeform_decoding_ablation"
    plan_id: "exp-018"
    description: >
      移除 Outlines constrained decoding，对 SciERC NER+RE 生成 8 个 free-form samples/instance。
      对比 constrained vs free-form 的 logprob variance、selection F1、QE 指标。
    expected_results:
      # Parse rate
      freeform_parse_rate_ner: 0.72
      freeform_parse_rate_re: 0.65
      freeform_n_valid_ner: 381
      freeform_n_valid_re: 258

      # Logprob variance (within-sample range)
      constrained_logprob_range_median: 0.03
      freeform_logprob_range_median: 0.07
      freeform_logprob_range_iqr: [0.03, 0.14]
      pct_instances_range_lt_005_constrained: 0.60
      pct_instances_range_lt_005_freeform: 0.38

      # QE correlation (logprob with F1)
      constrained_logprob_rho_ner: 0.205
      freeform_logprob_rho_ner: 0.22
      freeform_logprob_rho_ner_p: 0.00004
      constrained_logprob_rho_re: 0.266
      freeform_logprob_rho_re: 0.19
      freeform_logprob_rho_re_p: 0.002

      # QE AUROC
      constrained_logprob_auroc_ner: 0.578
      freeform_logprob_auroc_ner: 0.57
      constrained_logprob_auroc_re: 0.600
      freeform_logprob_auroc_re: 0.56

      # Selection (best-of-N F1)
      constrained_greedy_f1_ner: 0.644
      freeform_greedy_f1_ner: 0.631
      freeform_logprob_selection_f1_ner: 0.634
      freeform_logprob_selection_delta_vs_greedy_ner_pp: 0.3
      freeform_logprob_selection_p_ner: 0.42
      constrained_greedy_f1_re: 0.403
      freeform_greedy_f1_re: 0.382
      freeform_logprob_selection_f1_re: 0.379
      freeform_logprob_selection_delta_vs_greedy_re_pp: -0.3
      freeform_logprob_selection_p_re: 0.65

      # Oracle headroom (free-form subset)
      freeform_oracle_f1_ner: 0.74
      freeform_oracle_headroom_ner: 0.109
      freeform_oracle_f1_re: 0.53
      freeform_oracle_headroom_re: 0.148

      # Selection bias check (parseable vs full set)
      parseable_subset_mean_greedy_f1_ner: 0.68
      full_set_mean_greedy_f1_ner: 0.644
      parseable_subset_mean_greedy_f1_re: 0.44
      full_set_mean_greedy_f1_re: 0.403

      # Structural signals on free-form subset
      freeform_sj_rho_ner: 0.34
      freeform_voting_conf_rho_ner: 0.36
      freeform_sj_rho_re: 0.21

      # Bootstrap CI for selection delta
      freeform_selection_delta_ci95_ner: [-0.025, 0.031]
      freeform_selection_delta_ci95_re: [-0.035, 0.029]
      freeform_cohen_d_ner: 0.04
      freeform_cohen_d_re: -0.03

    result_rationale: >
      Worst 档的核心逻辑：constrained decoding 确实压缩了 logprob range（中位数 0.03），移除约束后
      range 上升到 0.07——但这远不够。0.07 的 range 意味着 8 个 sample 的 logprob 仍然聚集在一个
      很窄的带内，无法有效区分质量差异。原因在于：fine-tuned 8B 模型在 SciERC 上的 output distribution
      本身就很 peaked——不论是否有 grammar constraint，模型对于给定 input 的 "preferred output mode"
      高度集中。Constrained decoding 只是略微加剧了已经存在的低 entropy 问题。

      Parse rate 仅 ~70% 是因为 fine-tuning 时用了 constrained decoding 作为 training-time format
      guarantee，模型并未充分学会 JSON format 的内在结构。更关键的是，parseable subset 偏向 easy
      instances（mean greedy F1 0.68 vs full set 0.644），因为 format-compliant 的 free-form output
      更可能出现在模型 "confident" 的 instances 上——这些恰恰是 oracle headroom 更小、selection
      价值更低的 instances。

      Selection F1 几乎不变（NER +0.3pp, p=0.42; RE -0.3pp, p=0.65）直接否定了 bottleneck 假说。
      如果 score compression 是 selection 失败的主因，那么恢复 variance 应该恢复 selection——但没有。
      这说明 logprob 作为 scalar signal 的排序失败不是因为被压缩，而是因为 IE 的 set-valued output
      空间中，generation probability 与 output quality（F1）之间本就不存在强的单调关系。一个 sample
      可以有高 logprob（模型 confident）但 F1 低（confident about wrong entities），也可以有低 logprob
      （探索性 output）但 F1 高（偶然命中更多 gold entities）。

      RE 更差是因为 free-form 下 relation format 的 parse failure 更高（35%），且 RE 的组合空间
      (entity pairs × relation types) 远大于 NER，使得 scalar signal 的信息论上限更低。

    tables:
      - name: "Table: Constrained vs Free-form Logprob Comparison"
        columns: ["Metric", "Constrained", "Free-form", "Δ", "p-value"]
        rows:
          - ["NER logprob range median", "0.03", "0.07", "+0.04", "<0.001"]
          - ["NER logprob ρ(F1)", "0.205", "0.22", "+0.015", "—"]
          - ["NER logprob AUROC", "0.578", "0.57", "−0.008", "—"]
          - ["NER logprob selection F1", "0.650", "0.634", "−0.016", "—"]
          - ["NER selection Δ vs greedy (pp)", "+0.6", "+0.3", "−0.3", "0.42"]
          - ["RE logprob range median", "0.02", "0.06", "+0.04", "<0.001"]
          - ["RE logprob ρ(F1)", "0.266", "0.19", "−0.076", "—"]
          - ["RE logprob AUROC", "0.600", "0.56", "−0.040", "—"]
          - ["RE selection Δ vs greedy (pp)", "+0.7", "−0.3", "−1.0", "0.65"]

      - name: "Table: Parse Rate and Selection Bias"
        columns: ["Subset", "NER n", "NER mean F1", "RE n", "RE mean F1"]
        rows:
          - ["Full set (constrained)", "529", "0.644", "397", "0.403"]
          - ["Parseable (free-form)", "381", "0.680", "258", "0.440"]
          - ["Unparseable (free-form)", "148", "0.551", "139", "0.334"]

    figures_description:
      - >
        Figure: Logprob within-sample range distribution (violin plot).
        Left=constrained, right=free-form. Constrained 分布极度右偏，60% 实例 range<0.05，
        peak 在 0.01-0.02。Free-form 分布稍宽但仍然右偏，38% 实例 range<0.05，peak 在 0.04-0.06。
        两个分布有大量重叠，说明 variance 提升不够 dramatic。
      - >
        Figure: Selection F1 vs N curves (constrained vs free-form, side-by-side).
        两条 logprob selection 线几乎重叠于 greedy baseline 附近，远低于 oracle ceiling。
        Free-form oracle ceiling 略低（因为 parse failure 减少了有效候选池）。
        视觉上立刻可见：移除 constraint 没有改变 selection 的 fundamental flatness。

    analysis: >
      exp-018 在 worst 档下产生的是一个 well-designed null result：controlled ablation 证明
      score compression 不是 selection 失败的 root cause。这既是坏消息（D070 reframing 的核心因果叙事被否定）
      也是好消息（universal negative finding 比 regime-specific finding 更有 generality）。

      但叙事需要第二次 pivot。新的 argument structure：
      (1) IE output 是 set-of-sets（entity set × relation set），组合空间使得任何 instance-level
      scalar signal 的排序能力存在 information-theoretic 上限——一个数字无法 encode "which entities
      are correct and which are not"；
      (2) 与 reasoning/QA 的离散答案空间形成 structural contrast：self-consistency 在 QA 上成功
      恰因答案空间小（majority vote 在 5-10 个 candidate 中选）；
      (3) QE 仍然有效（AUROC 0.75）说明 signals 捕捉了 instance difficulty，但无法区分
      same-difficulty 内的 quality variation。

      关键风险：parse rate 偏低 + selection bias 使得 null result 的说服力打折扣。
      Reviewer 可能 argue "你的 free-form 实验 underpowered（n=381 NER, n=258 RE），
      且 parseable subset 本身偏向 easy instances"。需要在 paper 中做 sensitivity analysis
      （only on instances where all 8 free-form samples parse），并 acknowledge limitation。

      Expected reviewer score 在此档下降到 2.5-3.0 区间。Findings 接收概率 10-25%。


  - name: "ner_llama_conll"
    plan_id: "exp-017"
    description: >
      LLaMA-3.1-8B fine-tuned on CoNLL-2003 进行 NER inference (N=8, T=1.0)。
      Cross-model × cross-dataset validation，强化 model-agnostic claim。
    expected_results:
      greedy_f1: 0.918
      oracle_f1: 0.945
      oracle_headroom: 0.027
      n_instances: 3453
      n_valid: 2756

      # QE metrics (full set)
      sj_rho_full: 0.43
      fk_rho_full: 0.42
      logprob_rho_full: 0.31
      em_rho_full: 0.43
      voting_conf_rho_full: 0.42
      sj_auroc_full: 0.70
      logprob_auroc_full: 0.76

      # Selection (best-of-N)
      logprob_selection_f1: 0.919
      sj_selection_f1: 0.916
      voting_selection_f1: 0.917
      random_selection_f1: 0.912
      oracle_f1_selection: 0.945

      # Cross-model consistency check
      qwen_conll_sj_rho: 0.436
      llama_conll_sj_rho: 0.43
      delta_sj_rho: -0.006

    result_rationale: >
      Worst 档对 exp-017 的影响有限——这个实验是 cross-model validation，不直接依赖 bottleneck 假说。
      CoNLL-2003 是 "easy" NER dataset（greedy F1 ~0.92），oracle headroom 仅 ~0.027，
      selection 的理论上限就很低。LLaMA 在 CoNLL 上的表现应与 Qwen 高度一致
      （exp_017_llama_conll_infer 已有 SJ ρ=0.431 的数据佐证），因为两个 8B 模型在
      well-studied benchmark 上的 behavior 趋同。

      在 worst 档下，这个实验的结果本身是 "positive"（cross-model consistency confirmed），
      但对论文的帮助有限：它只证明了 QE 信号的 model-agnostic property，而 worst 档的核心问题
      是 selection 失败的叙事需要 pivot。Cross-model validation 对 "fundamental hardness"
      叙事是中性的——不增强也不削弱。

      Selection F1 在 CoNLL 上接近 greedy（+0.1pp），与 SciERC 的 pattern 一致。
      但因为 headroom 只有 2.7pp，即使 oracle 也只能提升这么多，所以 selection failure
      在 CoNLL 上的 diagnostic value 很低。

    tables:
      - name: "Table: Cross-Model QE Comparison on CoNLL-2003"
        columns: ["Signal", "Qwen ρ", "LLaMA ρ", "Δρ", "Qwen AUROC", "LLaMA AUROC"]
        rows:
          - ["SJ", "0.436", "0.43", "−0.006", "0.80", "0.70"]
          - ["FK", "0.400", "0.42", "+0.020", "0.77", "0.70"]
          - ["logprob", "0.316", "0.31", "−0.006", "0.75", "0.76"]
          - ["EM", "0.451", "0.43", "−0.021", "0.82", "0.70"]
          - ["voting_conf", "0.424", "0.42", "−0.004", "0.79", "0.71"]

    figures_description:
      - >
        Figure: Cross-model ρ scatter plot (Qwen x-axis, LLaMA y-axis, each point = one signal).
        Points clustered near diagonal, confirming model-agnostic signal behavior.
        Logprob 明显低于 structural signals 在两个模型上都成立。

    analysis: >
      Cross-model validation 成功但对 worst 档的核心困境帮助不大。可以作为 Table 1 的一行补充
      model-agnostic evidence，但不改变 selection failure 的 narrative。在 worst 档的 paper
      中，这个实验从 "strengthening the bottleneck claim" 降级为 "confirming QE generalization"。


  - name: "ner_ood_robustness"
    plan_id: "exp-011"
    description: >
      在 OOD 条件下（cross-domain transfer）测试 NER consistency signal 的鲁棒性。
      依赖 exp-003 (WNUT-17) 的 fine-tuned model 做 domain shift 测试。
    expected_results:
      # OOD = apply SciERC-finetuned model to WNUT-17 style data, or vice versa
      ood_greedy_f1: 0.35
      ood_oracle_f1: 0.52
      ood_headroom: 0.17
      ood_sj_rho_full: 0.05
      ood_fk_rho_full: 0.08
      ood_logprob_rho_full: -0.30
      ood_voting_conf_rho_full: 0.09
      ood_sj_auroc: 0.53
      ood_logprob_auroc: 0.42
      ood_sample_f1_pct_zero: 62.0
      ood_n_instances: 1287

      # Logprob pathology
      ood_logprob_negative_rho: true
      ood_logprob_overconfidence_on_wrong: true

    result_rationale: >
      OOD 条件下所有信号急剧退化。Greedy F1 降到 ~0.35 意味着模型在目标域基本失效，
      >60% samples F1=0。在这个 regime 下：
      (1) SJ/FK/voting 的 ρ 接近 0 因为大部分 instances 的 N 个 samples 全部 F1=0，
      无 variance 可供 correlation 捕捉；
      (2) Logprob 出现 WNUT-17 同样的 pathology：ρ 为负（-0.30），模型对 OOD 输入
      过度自信——logprob 高的 samples 反而更差，因为模型 "confidently" 产出 in-domain patterns
      而非 target domain 的正确 entities；
      (3) 这与 exp-003 (WNUT-17 logprob ρ=-0.41) 的发现一致。

      在 worst 档下，这个实验的解读方向改变：不再是 "OOD shows limitations of consistency signals"
      （这太 obvious），而是作为 "logprob overconfidence under distribution shift" 的额外证据，
      支持 "scalar signals fail for structural reasons, not just compression" 的论点。
      但 P2 priority + exp-003 已经 orphaned 意味着这个实验大概率不会执行。

    tables:
      - name: "Table: In-domain vs OOD Signal Comparison"
        columns: ["Signal", "In-domain ρ (SciERC)", "OOD ρ", "Δρ"]
        rows:
          - ["SJ", "0.36", "0.05", "−0.31"]
          - ["FK", "0.27", "0.08", "−0.19"]
          - ["logprob", "0.21", "−0.30", "−0.51"]
          - ["voting_conf", "0.38", "0.09", "−0.29"]

    figures_description:
      - >
        Figure: Logprob vs F1 scatter (in-domain vs OOD side-by-side).
        In-domain: weak positive trend. OOD: clear negative trend，高 logprob 区域
        聚集了 F1=0 的点，低 logprob 区域反而有非零 F1 的点。

    analysis: >
      OOD 实验在 worst 档下提供的额外信息有限——exp-003 WNUT-17 已经展示了同样的 pathology。
      且 exp-003 status=orphaned，exp-011 依赖 exp-003，实际执行概率极低。
      如果执行，它强化了 "logprob is unreliable under shift" 的 claim，但这不是论文的核心。
      建议 worst 档下不投入 GPU hours 在这个实验上，将资源集中于 exp-018 的 robustness checks。


  - name: "simple_verifier_baseline"
    plan_id: "exp-019"
    description: >
      训练 supervised verifier（DeBERTa-v3-large 或 Qwen3-8B classification head）在
      existing (input, output, F1) 数据上。测试 verifier 能否部分 close selection gap，
      为 unsupervised signal 的 failure 提供 upper bound。
    expected_results:
      # Training data
      train_n_instances: 529
      train_n_samples_per_instance: 8
      train_total_pairs: 4232
      train_val_split: "5-fold CV"

      # DeBERTa verifier
      deberta_auroc_ner: 0.72
      deberta_auroc_re: 0.66
      deberta_selection_f1_ner: 0.652
      deberta_selection_delta_vs_greedy_ner_pp: 0.8
      deberta_selection_p_ner: 0.18
      deberta_selection_f1_re: 0.398
      deberta_selection_delta_vs_greedy_re_pp: -0.5
      deberta_selection_p_re: 0.55

      # Comparison with unsupervised
      best_unsupervised_auroc_ner: 0.749
      deberta_vs_best_unsupervised_auroc_ner: -0.029
      best_unsupervised_selection_ner: 0.650
      deberta_vs_best_unsupervised_selection_ner: 0.002

      # Oracle reference
      oracle_selection_f1_ner: 0.776
      oracle_selection_f1_re: 0.588
      verifier_headroom_capture_ner_pct: 6.1
      verifier_headroom_capture_re_pct: 0.0

    result_rationale: >
      Worst 档下 supervised verifier 也基本失败，原因有三层：

      (1) 训练数据不足：529 instances × 8 samples = 4232 training pairs，对于 DeBERTa 这种
      encoder 来说数据量极少。5-fold CV 下每折只有 ~3400 training pairs，严重 overfit 风险。
      即使不 overfit，模型学到的更多是 "哪些 input 难"（instance difficulty）而非
      "哪个 output 好"（within-instance quality variation），因为 inter-instance F1 variance
      远大于 intra-instance F1 variance。

      (2) Feature gap：DeBERTa 只能看到 (input, output) text pair，无法 access logprob 或
      其他 generation metadata。它本质上在做 NLI-style 判断 "output 是否合理"，而 IE 的
      "合理性" 需要 precise span matching，这超出了 encoder 的 zero-shot 能力。即使 fine-tune，
      4K pairs 不足以学会 IE-specific quality patterns。

      (3) IE 的组合复杂性：即使 verifier AUROC 达到 0.72（超过 logprob 的 0.578），
      这仍然是 instance-level discrimination（"这个 instance 的 output 总体好不好"），
      而非 within-instance ranking（"这 8 个 candidate 中哪个最好"）。
      AUROC 0.72 不等于 selection 能力——exp-016 已经证明 AUROC 0.749 的 EM 信号
      selection 也只有 +0.6pp（n.s.）。

      Verifier 的 headroom capture rate 极低（NER 6.1%，RE 0%）与 unsupervised signals 的
      pattern 一致，说明 selection gap 不是 "signals 太弱" 而是 "task structure 使得
      instance-level scoring 根本不够"。这反而支持了 worst 档的核心论点：需要 sub-instance
      level 的 selection mechanism（如 entity-level MBR），scalar scoring 存在 fundamental ceiling。

      但 reviewer 价值有限：verifier 没有显著超过 best unsupervised signal，
      "supervised 也不行" 这个 claim 在 4K training pairs 下 underpowered，
      reviewer 会 argue "给足够数据 verifier 肯定能 work"。

    tables:
      - name: "Table: Supervised Verifier vs Unsupervised Signals"
        columns: ["Method", "NER AUROC", "NER Sel. F1", "RE AUROC", "RE Sel. F1"]
        rows:
          - ["DeBERTa verifier (5-fold CV)", "0.72", "0.652", "0.66", "0.398"]
          - ["EM (best unsupervised AUROC)", "0.749", "0.650", "0.706", "0.403"]
          - ["Logprob (best unsupervised sel.)", "0.578", "0.650", "0.600", "0.410"]
          - ["Greedy baseline", "—", "0.644", "—", "0.403"]
          - ["Oracle", "—", "0.776", "—", "0.588"]

    figures_description:
      - >
        Figure: Headroom capture bar chart. Oracle headroom (full bar) vs each method's
        capture (filled portion). 所有 bars 几乎为空——NER oracle headroom 13.2pp 中
        verifier 仅 capture 0.8pp，logprob capture 0.6pp。RE 所有方法 capture 0pp。
        视觉冲击力强，直接传达 "selection is fundamentally hard" 的 message。

    analysis: >
      exp-019 在 worst 档下的价值在于 closing the loop：即使 supervised signal 也无法显著
      close selection gap，说明问题不在于 signal quality 而在于 task structure。但执行条件
      苛刻（需要 exp-018 先完成 + 还有 DDL 前时间），且 4K training data 的 verifier 说服力
      有限。建议：如果时间允许，作为 1 天 quick experiment 执行，结果写入 Discussion 而非
      main results。如果时间不够，在 paper 中引用 exp-016 ensemble（logistic regression on
      5 signals）作为 proxy supervised baseline，其 AUROC 0.735 已经 ≤ best single signal
      EM 0.749，传达同样的 message。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22279167-d301-4aa2-953c-bc99f9d7e473",
  "isSidechain": false,
  "requestId": "req_011Cb48reQxuKVM2DUMP1Qij",
  "type": "assistant",
  "uuid": "15d5343f-e2ea-47b2-bc0d-dbcf7e25dc97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0133NUTf1Q1DPZ4iQEhxR92Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 45061,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 45061,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8604,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 45061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 45061
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Free-form 未恢复 selection ability；constrained decoding bottleneck 假说不成立，gap 源于 IE 本身 核心假设：['exp-018: logprob variance 提升微弱（range 中位数 <0.10）或虽提升但 selection 无…",
  "leafUuid": "15d5343f-e2ea-47b2-bc0d-dbcf7e25dc97",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Free-form decoding bottleneck verification for structured IE",
  "sessionId": "f8d04737-c591-43f1-8bfe-4c2ea74bdef2"
}
```

---
