# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Quality estimation framing完全成立，correlation-selection gap被视为novel conceptual 

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/4ff1286a-4c71-4d0e-a313-574e255d923f.jsonl`
- **Structured JSON:** [`44a2447ed1be45341bc8.json`](../../sessions/44/44a2447ed1be45341bc8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T20:41:27.657Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T20:41:27.657Z",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Quality estimation framing完全成立，correlation-selection gap被视为novel conceptual contribution，paper写作和positioning达到Main标准\n核心假设：['Quality estimation (AUROC/ρ for selective prediction) 被接受为first-class contribution，不要求selection improvement', 'Correlation-selection gap被认为是novel finding而非negative result的包装', '2×2 matrix (Qwen×LLaMA × SciERC×CoNLL) + 3-seed robustness被认为generalization充分', '与Nédellec & Xia 2026成功区分：SJ解决其自承的surface matching limitation', 'RE full ρ弱 (~0.21-0.30) 被接受为task-complexity boundary的supporting evidence而非weakness', 'Paper presentation达标：≥3 figures + 35+ refs + 清晰信号分类法 + 对concurrent work的显式对比']\n关键指标范围：{'reviewer_overall_arr': [3.5, 4.0], 'acceptance_prob_main': [0.4, 0.6], 'acceptance_prob_findings': [0.75, 0.9], 'perceived_novelty': [3.5, 4.0], 'perceived_soundness': [3.5, 4.5], 'n_major_weaknesses_per_review': [0, 1], 'rebuttal_addressable_pct': [0.85, 1.0], 'focal_auroc_gap_structural_vs_logprob': [0.1, 0.17], 'focal_rho_gap': [0.15, 0.36], 'cross_config_ner_structural_gt_logprob_rate': [1.0, 1.0], 'effective_claim_count_accepted': [3, 3]}\n叙事方向：原始3-claim framing完全成立。Claim 1以voting AUROC 0.73 vs logprob 0.56为headline，SJ作为generalizable complement。Claim 2 (correlation-selection gap) 定位为paper最具practical insight的发现——改变practitioners对structured TTS的认知。Claim 3提供explanatory depth。Claims无需调整强度。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: struct_self_consist_ie\nfocus: 全部 GPU 实验已完成：2×2 矩阵（Qwen×LLaMA × SciERC×CoNLL）+ N=8/N=16 + 3-seed 鲁棒性。5 信号系统比较框架。核心发现：structural > logprob 跨设置一致、correlation-selection gap、task-complexity boundary。论文初稿 experiments/method/introduction 已完成。55 篇文献。关注：能否达到 EMNLP 2026 接收水准？\n\n## paper_framing.md\n\n# Paper Framing — struct_self_consist_ie\n\n> Updated 2026-05-14 post-exp-016 pivot (D019). CRITICAL NARRATIVE CHANGE: best-of-N selection fails on NER (all signals ≤ greedy). Pivot from \"TTS improvement\" to \"confidence estimation + correlation-selection gap\".\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR May 2026)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May cycle, 2026-05-25\n\n## Core Claims (3 条)\n\n### Claim 1 (Positive — Quality Estimation)\nStructural consistency signals (entity voting confidence, soft Jaccard) are the strongest unsupervised quality estimators for entity-level IE, significantly outperforming model confidence (log-probability) and surface agreement (FK, exact-match) at instance-level quality prediction. Entity voting achieves AUROC 0.73 / ρ=0.50 on NER, SJ achieves AUROC 0.67 / ρ=0.36 — both far above logprob (AUROC 0.56 / ρ=0.14). Voting leads SJ on full set; SJ retains unique strength in conditional evaluation (ρ=0.41) and is temperature-robust (Δρ=±0.01).\n\n**Key insight**: The contribution is about a FAMILY of structural consistency signals for QUALITY ESTIMATION (predicting which instances are reliable), not for per-sample selection. SJ and voting_conf both capture entity-across-sample consistency. SJ generalizes to arbitrary structured outputs; voting is simpler.\n\n**Evidence** (SciERC, N=8, T=1.0, unified exp_015 evaluation):\n- NER full (n=529): voting ρ=0.502/τ=0.377/AUROC=0.728, SJ ρ=0.357/τ=0.266/AUROC=0.666, FK ρ=0.265/τ=0.203/AUROC=0.624, EM ρ=0.257/τ=0.192/AUROC=0.623, logprob ρ=0.140/τ=0.101/AUROC=0.559\n- NER cond (n=501): voting ρ=0.450, SJ ρ=0.412, EM ρ=0.343, FK ρ=0.306, logprob ρ=0.163\n- RE full (n=397): voting ρ=0.422/AUROC=0.716, FK ρ=0.253/AUROC=0.631, logprob ρ=0.247/AUROC=0.635, SJ ρ=0.211/AUROC=0.582, EM ρ=0.100/AUROC=0.504\n- RE cond (n=296): voting ρ=0.463, SJ ρ=0.368, EM ρ=0.361, FK ρ=0.317, logprob ρ=0.146\n- Temperature robustness: SJ Δρ=±0.01 across T=0.7/1.0; FK Δρ=±0.06-0.09 (SJ far more stable)\n\n### Claim 2 (Novel Finding — Correlation-Selection Gap)\nInstance-level quality estimation ≠ per-sample selection ability. Despite strong instance-level correlation (ρ≈0.39-0.43), NO unsupervised confidence signal beats greedy decoding for NER best-of-N selection. On RE, only log-probability (+2.4pp over greedy) enables effective selection. The oracle headroom is large (NER +16pp, RE +18pp) but current signals cannot exploit it.\n\n**exp-016 evidence** (SciERC, N=8, T=1.0, n=529):\n- NER best-of-N: greedy 0.6094 > logprob 0.6087 > ensemble 0.6043 > sj 0.6042 > voting 0.5959 > random 0.5796 (oracle 0.7692)\n- RE best-of-N: logprob 0.3971 > greedy 0.3735 > sj 0.3680 > voting 0.3379 ≈ random 0.3380 (oracle 0.5610)\n- Instance-level AUROC: voting_conf 0.700, SJ 0.689, ensemble 0.735 >> logprob 0.591\n\n**Key insight**: Consistency signals are INSTANCE-LEVEL aggregates (one score per instance). They predict which inputs are easy/hard, NOT which sample is best. Log-prob is the only PER-SAMPLE signal and uniquely enables selection on uncertain tasks (RE). This distinction between quality estimation and sample selection is the paper's most practically important finding.\n\n**Implications**: (a) For selective prediction / abstention → use structural consistency (AUROC 0.70+). (b) For best-of-N selection → use logprob, but only on tasks where greedy is suboptimal (RE). (c) For NER, greedy is near-optimal → TTS offers no advantage with current signals.\n\n### Claim 3 (Diagnostic — task-complexity boundary)\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\n\n**MVP evidence**: RE full rho_sj=0.234, RE cond rho_sj=0.372 (SJ>FK +11.8pp). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\n\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\n\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\n\n## Story Spine\n\n**Problem**: LLM-based structured prediction (IE) increasingly uses multi-sample generation, but practitioners lack guidance on which confidence signals to trust — and for what purpose. Crucially, it is unknown whether signals that predict output quality (instance-level) also enable effective sample selection (per-sample-level).\n\n**Existing approaches & gaps**: Self-consistency in reasoning uses exact-match voting (Wang et al. 2023). USC (Chen et al. 2024) uses LLM-as-judge. For structured prediction, no systematic comparison exists across confidence signal families. More importantly, prior work conflates quality estimation with selection — assuming that high correlation with accuracy translates to effective best-of-N selection.\n\n**Our framing**: We systematically compare five confidence signals across four families for IE: (1) model confidence (log-probability), (2) surface agreement (FK, exact-match), (3) set-aware structural similarity (SJ), (4) entity-level majority voting. We make three findings:\n1. Structural consistency (voting_conf/SJ) provides the strongest quality estimation (AUROC 0.73 vs logprob 0.56)\n2. However, a **correlation-selection gap** exists: despite strong instance-level correlation, NO signal beats greedy decoding for NER selection; only logprob helps for RE (+2.4pp)\n3. All signals degrade on relational tasks due to compound error propagation\n\n**Headline result template**: \"On NER, entity voting confidence achieves AUROC 0.73 and ρ=0.50 for quality estimation, significantly outperforming log-probability (AUROC 0.56, ρ=0.14). However, this quality estimation capability does NOT translate to effective best-of-N selection — no signal surpasses greedy decoding on NER (oracle headroom: +16pp). We identify a fundamental correlation-selection gap: instance-level consistency predicts WHICH INPUTS are reliable, not WHICH OUTPUTS are best. On RE, only per-sample log-probability enables selection (+2.4pp), while all consistency signals degrade.\"\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only one NER dataset — generalization unclear\"\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\n- **Priority**: P0\n\n### R2: \"Only one model family (Qwen3-8B)\"\n- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect\n- **Priority**: P0\n\n### R3: \"FK is a strawman baseline — what about log-prob, USC, exact-match?\"\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (SJ+voting) >> log-prob >> FK ≈ exact-match. USC discussed in related work (LLM-as-judge, orthogonal approach).\n- **Priority**: P0, RESOLVED — results decisive\n\n### R3b: \"Voting confidence beats SJ — why use SJ?\"\n- **Mitigation**: SJ generalizes to arbitrary structured outputs (relations, events, any set-structured prediction). Voting is entity-specific. NER full: voting leads (ρ=0.50 vs 0.36), but SJ retains unique strength in conditional evaluation (ρ=0.41 vs voting 0.45) and is more temperature-robust (Δρ=±0.01). RE cond: SJ ρ=0.37 competitive with voting 0.46. SJ is also more interpretable (pairwise similarity). Paper presents both as complementary instantiations of the structural consistency principle, with voting as practical default and SJ as robust/generalizable option.\n- **Priority**: P1 — narrative adjustment needed given exp_015 unified values\n\n### R4: \"No actual TTS improvement demonstrated\"\n- **Status**: ⚠️ CONFIRMED NEGATIVE by exp-016. Best-of-N selection DOES NOT beat greedy on NER with any signal. RE: only logprob +2.4pp over greedy.\n- **Mitigation**: Paper PIVOTS to \"confidence estimation + correlation-selection gap analysis.\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\n- **Priority**: P0 — narrative pivot required\n\n### R5: \"Sample size N=8 may be too small for reliable SJ estimation\"\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\n- **Priority**: P0\n\n### R6: \"Conditional analysis cherry-picks favorable instances\"\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\n- **Priority**: P0 (add sensitivity analysis)\n\n### R7: \"Only ρ as evaluation metric\"\n- **Mitigation**: Add AUROC, calibration plots, Kendall's τ for all experiments\n- **Priority**: P0\n\n### R8: \"Formula-implementation discrepancy\"\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\n- **Priority**: P0, paper writing fix\n\n### R9: \"Evaluation circularity (T>0 consistency vs T=0 F1)\"\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\n- **Priority**: P0\n\n### R10: \"Insufficient related work\" (三档一致 [B][M][W])\n- **Mitigation**: Expand to 35+ references. Must cite:\n  - USC (Chen 2024) — empirical differentiation, not just citation\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\n  - **IE confidence**: Culotta & McCallum 2004\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\n  - **[2025-2026 新颖性自查补充 — 必引]**:\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\"overlooks semantically consistent outputs\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\n  - **[2025-2026 新颖性自查补充 — 应引]**:\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\n  - **需新增 Related Work 小节**:\n    - \"Test-Time Scaling & Sample Selection\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\n    - \"Consistency for Structured IE\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\n- **Priority**: P0, Paper Agent handles\n\n### R11: \"SJ+logprob ensemble missing\" (Dream 2 — both reviewers)\n- **Status**: ✅ RESOLVED by exp-016. Results:\n  - Ensemble AUROC: NER 0.735 (+3.5pp over best single), RE 0.719 (−0.2pp, no improvement)\n  - Linear combo: SJ+voting best at α=0.3 (NER ρ=0.489); RE α=0.0 (pure voting)\n  - FK negative coefficient in logistic regression → surface agreement is net-negative when structural signals present\n  - **Interpretation**: voting_conf captures nearly all discriminative information; ensemble adds marginal value on NER, none on RE. Supports the \"structural consistency family\" narrative.\n- **Priority**: DONE — write into paper with honest interpretation\n\n### R12: \"No supervised upper bound / reward model comparison\" (Dream 2)\n- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Full reward model training out of scope for this paper — discuss as future work.\n- **Priority**: P1 (partially addressed by exp-016 ensemble)\n\n### R13: \"Headroom capture rate low (37% NER, 11% RE)\" (Dream 2)\n- **Mitigation**: Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline.\n- **Priority**: P0, paper writing\n\n### R14: \"Cross-model validation thin — need more than 2×8B\" (Dream 2)\n- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.\n- **Priority**: P1\n\n### R15: \"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\"\n- **Priority**: P0, Paper Agent handles\n\n### R16: \"Zero figures — data-rich paper with only tables\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\n- **Priority**: P0, Paper Agent handles\n\n### R17: \"Diagnostic framework overclaimed — descriptive not prescriptive\" (Dream 2 cross-tier, [M][W])\n- **Mitigation**: Soften \"diagnostic framework\" to \"diagnostic analysis\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\n- **Priority**: P0, Paper Agent handles\n\n### R18: \"No discussion of when consistency WOULD help\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\n- **Priority**: P1, Paper Agent handles\n\n### R19: \"Negative result partially predictable for fine-tuned models\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\n- **Priority**: P1, Paper Agent handles\n\n## Venue Fit\n\nEMNLP is well-suited for:\n- Systematic empirical comparison of confidence signals for structured prediction\n- Diagnostic findings with principled explanations\n- The \"comparison + boundary condition\" contribution pattern\n\nRisk assessment (post-Dream 2, all tiers 3/6):\n- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.\n- **Data-dependent risks (观察中)**: SJ vs LOGPROB ranking may be dataset-dependent (Dream imagined this; awaiting exp-002/003 real data). If confirmed → reframe as \"complementary signals\" rather than \"SJ dominates.\"\n- **Confirmed strength**: SJ >> LOGPROB on SciERC (AUROC 0.70 vs 0.59). Structural consistency family consistently top on existing data.\n- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-012\n  name: baseline_logprob\n  claim: 1\n  description: 'Compute sequence log-probability for all existing pilot samples (SciERC\n    NER+RE) and new dataset pilots. Correlate log-prob with F1 (ρ, AUROC, τ). If SJ\n    does NOT beat log-prob, the 16x inference cost is unjustified and paper contribution\n    weakens drastically. THIS IS THE MAKE-OR-BREAK EXPERIMENT.\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  note: 'Needs vLLM forward pass to extract log-probs from existing samples. ~1h per\n    dataset on 1 GPU. For new datasets, capture log-probs during pilot inference.\n    Also compute on pilot_004/005 existing data if log-probs weren''t saved.\n\n    '\n  registry_id: exp_012_logprob_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho_sj: 0.3565\n    ner_full_rho_fk: 0.2651\n    ner_full_rho_logprob: 0.1396\n    ner_full_rho_greedy_logprob: 0.1615\n    ner_full_tau_sj: 0.2658\n    ner_full_tau_logprob: 0.1006\n    ner_full_auroc_sj: 0.6892\n    ner_full_auroc_fk: 0.6292\n    ner_full_auroc_logprob: 0.5907\n    ner_full_n: 529\n    ner_sj_vs_logprob_delta: 0.2169\n    re_full_rho_sj: 0.2112\n    re_full_rho_fk: 0.2528\n    re_full_rho_logprob: 0.2467\n    re_full_auroc_sj: 0.5916\n    re_full_auroc_fk: 0.6262\n    re_full_auroc_logprob: 0.6186\n    re_full_n: 397\n    re_cond_rho_sj: 0.3683\n    re_cond_rho_fk: 0.3168\n    re_cond_rho_logprob: 0.1457\n    re_cond_auroc_sj: 0.6839\n    re_cond_auroc_logprob: 0.5487\n    re_cond_n: 296\n    diagnosis: 'NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead.\n      RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.'\n- id: exp-013\n  name: baseline_exact_match\n  claim: 1\n  description: 'Exact-match voting rate: what fraction of N samples produce identical\n    entity/relation sets? Correlate with F1. This is the direct analogue of Wang et\n    al.''s original self-consistency for structured outputs.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU-only on existing pilot data. Zero cost.\n  registry_id: exp_013_exact_match_voting\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_full_rho: 0.2941\n    ner_full_p: 5.12e-12\n    ner_full_tau: 0.2181\n    ner_full_auroc: 0.6398\n    re_full_rho: 0.1562\n    re_full_p: 0.0018\n    re_full_tau: 0.1185\n    re_full_auroc: 0.5863\n    diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\n- id: exp-014\n  name: baseline_entity_voting\n  claim: 1\n  description: 'Entity-level majority voting: for each entity, count how many of N\n    samples include it. Select entities above threshold. Compare F1 of entity-voting\n    selection vs SJ selection vs FK selection.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  note: CPU-only on existing pilot data. Zero cost.\n  registry_id: exp_014_entity_majority_voting\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho: 0.3915\n    ner_full_p: 8.1e-21\n    ner_full_tau: 0.2906\n    ner_full_auroc: 0.7039\n    re_full_rho: 0.3403\n    re_full_p: 3.21e-12\n    re_full_tau: 0.256\n    re_full_auroc: 0.6668\n    ner_voting_f1: 0.6246\n    ner_greedy_f1: 0.6483\n    ner_oracle_f1: 0.7793\n    re_voting_f1: 0.3577\n    re_greedy_f1: 0.4022\n    re_oracle_f1: 0.5886\n    diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE\n      (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\n- id: exp-015\n  name: evaluation_metrics_expansion\n  claim: 1\n  description: 'Add AUROC (binary: good/bad output at threshold), calibration plots,\n    and Kendall''s τ alongside Spearman ρ for ALL confidence signals (SJ, FK, log-prob,\n    exact-match, entity-voting) on ALL datasets. Also add leave-one-out SJ as robustness\n    check for evaluation circularity.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  - exp-013\n  - exp-014\n  note: CPU-only analysis. Addresses Dream concerns D5 (single metric) and D17 (circularity).\n  registry_id: exp_015_metrics_expansion\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_012_logprob/samples_with_logprobs.jsonl\n    config: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\n    ner:\n      n_valid: 529\n      n_cond: 501\n      voting_rho_full: 0.5018\n      voting_rho_cond: 0.4497\n      voting_auroc: 0.7279\n      voting_tau: 0.3766\n      sj_rho_full: 0.3565\n      sj_rho_cond: 0.412\n      sj_auroc: 0.6656\n      sj_tau: 0.2658\n      em_rho_full: 0.2566\n      em_rho_cond: 0.3427\n      em_auroc: 0.623\n      em_tau: 0.1924\n      fk_rho_full: 0.2651\n      fk_rho_cond: 0.306\n      fk_auroc: 0.6243\n      fk_tau: 0.2027\n      logprob_rho_full: 0.1396\n      logprob_rho_cond: 0.1627\n      logprob_auroc: 0.5585\n      logprob_tau: 0.1006\n    re:\n      n_valid: 397\n      n_cond: 296\n      voting_rho_full: 0.4217\n      voting_rho_cond: 0.463\n      voting_auroc: 0.7162\n      voting_tau: 0.327\n      sj_rho_full: 0.2112\n      sj_rho_cond: 0.3683\n      sj_auroc: 0.5816\n      sj_tau: 0.1619\n      em_rho_full: 0.1002\n      em_rho_cond: 0.3607\n      em_auroc: 0.5036\n      em_tau: 0.0839\n      fk_rho_full: 0.2528\n      fk_rho_cond: 0.3168\n      fk_auroc: 0.6308\n      fk_tau: 0.1967\n      logprob_rho_full: 0.2467\n      logprob_rho_cond: 0.1457\n      logprob_auroc: 0.6354\n      logprob_tau: 0.1808\n    diagnosis: 'Unified 5-signal evaluation on single data source. Voting leads NER\n      full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals\n      beat logprob on NER. RE: voting leads both full and cond.'\n- id: exp-001\n  name: ner_n16_scierc\n  claim: 1\n  description: 'NER N=16 on SciERC (ft_002_v2 model). Strengthen rho estimation, test\n    N-scaling. Run with seeds [42, 123, 456] for robustness. MUST capture log-probs\n    during inference for exp-012.\n\n    '\n  priority: P0\n  gpu_budget_hours: 18\n  deps: []\n  dataset: SciERC\n  model: ft_002_v2\n  note: 3 seeds × 6h each. Inference script MUST output log-probs.\n  registry_id: exp_001_ner_n16_scierc\n  status: DONE\n  conclusion: success\n  metrics:\n    n_instances: 551\n    ner_n: 529\n    re_n: 397\n    N: 16\n    T: 1\n    seed: 42\n    full_test_set: true\n    ner_voting_conf_rho: 0.399\n    ner_sj_rho: 0.398\n    ner_em_rho: 0.339\n    ner_fk_rho: 0.288\n    ner_logprob_rho: 0.237\n    ner_voting_conf_auroc: 0.704\n    ner_sj_auroc: 0.697\n    ner_cond_em_rho: 0.414\n    ner_cond_sj_rho: 0.349\n    ner_cond_vc_rho: 0.34\n    re_voting_conf_rho: 0.38\n    re_logprob_rho: 0.293\n    re_fk_rho: 0.281\n    re_sj_rho: 0.277\n    re_em_rho: 0.148\n    re_voting_conf_auroc: 0.699\n    re_cond_em_rho: 0.475\n    re_cond_sj_rho: 0.318\n    re_cond_vc_rho: 0.35\n    re_cond_em_auroc: 0.742\n    diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380).\n      EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full\n      FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact of\n      200 instances + T=0.7.'\n- id: exp-002\n  name: ner_conll2003\n  claim: 1\n  description: 'Fine-tune Qwen3-8B on CoNLL-2003 (LoRA) + NER pilot (N=8, T=0.7).\n    Cross-dataset generalization. MUST capture log-probs. Use consistent N and T with\n    other datasets.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  dataset: CoNLL-2003\n  model: qwen3-8b (new fine-tune)\n  registry_id: exp_002_ner_conll2003\n  status: DONE\n  conclusion: success\n- id: exp-003\n  name: ner_wnut17\n  claim: 1\n  description: 'Fine-tune Qwen3-8B on WNUT-17 (LoRA) + NER pilot (N=8, T=0.7). Social\n    media domain — cross-dataset generalization. MUST capture log-probs.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps: []\n  dataset: WNUT-17\n  model: qwen3-8b (new fine-tune)\n  note: User confirmed public datasets only. D043/D045 abandoned — 54% F1=0, SJ rho\n    not significant. Provides Claim 3 negative evidence.\n  registry_id: exp_003_wnut17_v2_infer\n  status: orphaned\n- id: exp-004\n  name: re_diagnostic_analysis\n  claim: 2\n  description: 'Per-relation-type consistency breakdown on existing pilot_004/005\n    data. Error propagation patterns. Bootstrap CI for ALL rho comparisons. Add conditional\n    threshold sensitivity analysis (vary exclusion criterion). Compare ALL confidence\n    signals (SJ, FK, log-prob, exact-match) on RE.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  - exp-013\n  note: CPU-only. Bootstrap CI + threshold sensitivity address Dream concerns.\n  registry_id: exp_004_re_diagnostic\n  status: DONE\n  conclusion: success\n  metrics:\n    per_relation_type:\n      HYPONYM-OF:\n        n: 36\n        rho_sj: 0.545\n        rho_fk: 0.646\n        rho_vc: 0.628\n        mean_f1: 0.513\n      CONJUNCTION:\n        n: 86\n        rho_sj: 0.383\n        rho_fk: 0.35\n        rho_vc: 0.484\n        mean_f1: 0.48\n      USED-FOR:\n        n: 299\n        rho_sj: 0.236\n        rho_fk: 0.255\n        rho_vc: 0.286\n        mean_f1: 0.422\n      PART-OF:\n        n: 44\n        rho_sj: 0.239\n        rho_fk: 0.348\n        rho_vc: 0.283\n        mean_f1: 0.297\n      EVALUATE-FOR:\n        n: 62\n        rho_sj: 0.172\n        rho_fk: 0.255\n        rho_vc: 0.226\n        mean_f1: 0.365\n      COMPARE:\n        n: 35\n        rho_sj: 0.168\n        rho_fk: 0.184\n        rho_vc: 0.18\n        mean_f1: 0.453\n      FEATURE-OF:\n        n: 50\n        rho_sj: 0.004\n        rho_fk: 0.052\n        rho_vc: 0.014\n        mean_f1: 0.254\n    error_propagation:\n      total_fn: 553\n      tail_error_pct: 21.9\n      full_error_pct: 21.7\n      head_error_pct: 17.7\n      head_tail_error_pct: 15.9\n      type_error_pct: 8.3\n      worst_consistency: head_type_error (sj=0.411)\n      best_consistency: head_error (sj=0.613)\n    threshold_sensitivity:\n      thr_0.00_rho_sj: 0.3161\n      thr_0.00_rho_vc: 0.3841\n      thr_0.00_n: 313\n      thr_0.05_rho_sj: 0.2682\n      thr_0.05_rho_vc: 0.2364\n      thr_0.05_n: 239\n    bootstrap_ci_95:\n      ner_sj:\n      - 0.2946\n      - 0.4586\n      ner_voting_conf:\n      - 0.3048\n      - 0.4656\n      re_sj:\n      - 0.1422\n      - 0.3391\n      re_voting_conf:\n      - 0.1818\n      - 0.3721\n      re_cond_sj:\n      - 0.2161\n      - 0.4102\n      re_cond_voting_conf:\n      - 0.2825\n      - 0.474\n    fisher_z_ner_vs_re:\n      sj_z: 2.31\n      sj_p: 0.0209\n      sj_significant: true\n      fk_z: -0.31\n      fk_p: 0.756\n      fk_significant: false\n      voting_z: 1.914\n      voting_p: 0.0556\n      voting_significant: false\n    diagnosis: FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF\n      strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of\n      RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE\n      signal in conditional set (rho=0.384).\n- id: exp-005\n  name: temperature_sensitivity_analysis\n  claim: 2\n  description: 'T=0.7 vs T=1.0 comparison on both NER and RE for ALL confidence signals.\n    Signal-noise tradeoff analysis.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  note: CPU-only on existing pilot_004 (T=1.0) and pilot_005 (T=0.7) data.\n  registry_id: exp_005\n  status: DONE\n  conclusion: success\n- id: exp-006\n  name: adaptive_compute_demo\n  claim: 1\n  description: 'Best-of-N selection on NER: SJ vs log-prob vs FK vs exact-match vs\n    random vs greedy. Report on ALL NER datasets (not just SciERC). Include RE results\n    too (even if negative).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-012\n  note: CPU-only. Must cover all datasets and include RE for completeness.\n  registry_id: exp_006_v2\n  status: DONE\n  conclusion: negative\n  metrics:\n    NER_SciERC_s42:\n      greedy: 0.618\n      oracle: 0.787\n      SJ: 0.62\n      logprob: 0.621\n      FK: 0.621\n      EM: 0.606\n      voting_conf: 0.585\n      random: 0.586\n    NER_SciERC_s123:\n      greedy: 0.618\n      oracle: 0.785\n      SJ: 0.617\n      logprob: 0.618\n      FK: 0.621\n      EM: 0.613\n      voting_conf: 0.584\n      random: 0.583\n    NER_CoNLL:\n      greedy: 0.725\n      oracle: 0.757\n      SJ: 0.718\n      logprob: 0.716\n      FK: 0.717\n      EM: 0.716\n      voting_conf: 0.714\n      random: 0.692\n    RE_SciERC:\n      greedy: 0.403\n      oracle: 0.631\n      SJ: 0.397\n      logprob: 0.41\n      FK: 0.396\n      EM: 0.381\n      voting_conf: 0.408\n      random: 0.364\n- id: exp-007\n  name: ner_multi_model\n  claim: 1\n  description: 'NER pilot with LLaMA-3.1-8B-Instruct on SciERC. Model-agnostic validation.\n    MUST capture log-probs for baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps: []\n  dataset: SciERC\n  model: llama-3.1-8b (new fine-tune)\n  registry_id: exp_007_llama_inference\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.66\n      oracle_f1: 0.781\n      headroom: 0.121\n      rho_fk: 0.327\n      rho_sj: 0.363\n      rho_fk_cond: 0.226\n      rho_sj_cond: 0.311\n      rho_logprob: 0.183\n      rho_logprob_cond: 0.109\n      structural_beats_surface: true\n      sample_f1_pct_zero: 11.6\n    re:\n      greedy_f1: 0.434\n      oracle_f1: 0.568\n      headroom: 0.135\n      rho_fk: 0.305\n      rho_sj: 0.299\n      rho_fk_cond: 0.259\n      rho_sj_cond: 0.405\n      rho_logprob: 0.288\n      rho_logprob_cond: 0.092\n      structural_beats_surface: false\n      sample_f1_pct_zero: 41.2\n    n_instances: 551\n    N: 8\n    T: 1\n    seed: 42\n    model: LLaMA-3.1-8B-Instruct\n    verdict: FAIL\n    verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\n- id: exp-008\n  name: re_n16_confirmation\n  claim: 2\n  description: 'RE N=16 on SciERC to confirm negative finding with higher statistical\n    power.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps: []\n  dataset: SciERC\n  model: ft_002_v2\n  registry_id: exp_008_re_n16\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.6635\n      oracle_f1: 0.8208\n      headroom: 0.1572\n      rho_sj_full: 0.377\n      rho_fk_full: 0.2508\n      rho_logprob_full: 0.3153\n      rho_sj_cond: 0.3598\n      rho_fk_cond: 0.2251\n      rho_logprob_cond: 0.2927\n      sj_beats_fk: true\n      rho_advantage: 0.1262\n    re:\n      greedy_f1: 0.4339\n      oracle_f1: 0.6658\n      headroom: 0.2319\n      rho_sj_full: 0.2966\n      rho_fk_full: 0.2871\n      rho_logprob_full: 0.2986\n      rho_sj_cond: 0.3975\n      rho_fk_cond: 0.3774\n      rho_logprob_cond: 0.2745\n      sj_beats_fk: true\n      rho_advantage: 0.0095\n    verdict: FAIL\n- id: exp-009\n  name: capability_stratification\n  claim: 2\n  description: 'Stratify instances by difficulty (greedy F1 buckets + independent\n    proxies: sentence length, entity count) for both NER and RE. Verify inverted-U\n    pattern with proper statistical tests and independent stratification variable.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  note: CPU-only. Dream flagged inverted-U overclaiming — use independent proxy.\n  registry_id: exp_009_capability_stratification\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n: 551\n      sj_rho_overall: 0.398\n      by_greedy_f1:\n        hard_0_25_sj_rho: 0.159\n        med_low_sj_rho: 0.139\n        med_high_sj_rho: 0.09\n        easy_sj_rho: 0.23\n      by_sent_len:\n        Q1_sj_rho: 0.461\n        Q2_sj_rho: 0.401\n        Q3_sj_rho: 0.296\n        Q4_sj_rho: 0.382\n      by_ent_count:\n        0_sj_rho: 0.689\n        1_2_sj_rho: 0.415\n        3_5_sj_rho: 0.353\n        6plus_sj_rho: 0.547\n    scierc_re:\n      n: 551\n      by_greedy_f1:\n        hard_0_25_sj_rho: -0.043\n        easy_sj_rho: 0.21\n      by_sent_len:\n        Q1_sj_rho: 0.447\n        Q4_sj_rho: 0.54\n      by_rel_count:\n        0_sj_rho: 0.62\n        1_2_sj_rho: 0.275\n        6plus_sj_rho: 0.527\n    conll_ner:\n      n: 3453\n      by_sent_len:\n        Q1_sj_rho: 0.334\n        Q3_sj_rho: 0.518\n    proxy_independence:\n      scierc_ner_f1_vs_slen: -0.021\n      scierc_ner_f1_vs_ecnt: 0.007\n      scierc_re_f1_vs_slen: -0.147\n- id: exp-010\n  name: selection_curves\n  claim: 1\n  description: 'Best-of-N selection curves for N=1,2,4,8,16 comparing all confidence\n    signals. Visualize as line plots (not just tables — Dream flagged table-only presentation).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-012\n  note: CPU-only visualization\n  registry_id: exp_010_selection_curves\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n_instances: 551\n      greedy_f1: 0.618\n      N16:\n        oracle: 0.787\n        SJ: 0.62\n        FK: 0.621\n        logprob: 0.621\n        voting_conf: 0.585\n        EM: 0.606\n        random: 0.595\n      N8:\n        oracle: 0.752\n        SJ: 0.614\n        FK: 0.614\n        logprob: 0.619\n        voting_conf: 0.591\n        EM: 0.603\n        random: 0.589\n      N4:\n        oracle: 0.714\n        SJ: 0.607\n        FK: 0.608\n        logprob: 0.616\n        voting_conf: 0.594\n        EM: 0.6\n        random: 0.587\n    scierc_re:\n      n_instances: 397\n      greedy_f1: 0.403\n      N16:\n        oracle: 0.631\n        SJ: 0.397\n        FK: 0.396\n        logprob: 0.41\n        voting_conf: 0.408\n        EM: 0.381\n        random: 0.364\n      N8:\n        oracle: 0.583\n        SJ: 0.393\n        FK: 0.394\n        logprob: 0.413\n        voting_conf: 0.398\n        EM: 0.381\n        random: 0.363\n    conll_ner:\n      n_instances: 3453\n      greedy_f1: 0.725\n      N8:\n        oracle: 0.757\n        SJ: 0.718\n        FK: 0.717\n        logprob: 0.716\n        voting_conf: 0.714\n        EM: 0.716\n        random: 0.69\n      N4:\n        oracle: 0.746\n        SJ: 0.714\n        FK: 0.714\n        logprob: 0.715\n        voting_conf: 0.714\n        EM: 0.712\n        random: 0.692\n- id: exp-011\n  name: ner_ood_robustness\n  claim: 1\n  description: 'Test NER consistency signal on OOD instances (cross-domain transfer).\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n- id: exp-016\n  name: signal_ensemble_analysis\n  claim: 1\n  description: 'SJ+logprob instance-level correlation and ensemble analysis. (1) Pearson/Spearman\n    correlation between SJ and logprob per-instance. (2) Grid search linear combination\n    alpha*SJ + (1-alpha)*logprob. (3) Logistic regression on all 5 signals as ensemble.\n    (4) Best-of-N selection F1 for ensemble vs individual signals. Dream 2 reviewers\n    BOTH independently flagged this as missing.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-012\n  - exp-014\n  note: CPU-only on existing pilot_004 data. Zero cost, high impact.\n  registry_id: exp_016_signal_ensemble\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_logprob_pearson_ner: 0.57\n    sj_logprob_pearson_re: 0.42\n    best_linear_ner:\n      combo: SJ+voting_conf\n      alpha: 0.3\n      rho: 0.489\n    best_linear_re:\n      combo: voting_conf+logprob\n      alpha: 0.6\n      rho: 0.429\n    ensemble_ner_auroc: 0.735\n    ensemble_re_auroc: 0.719\n    best_single_ner_auroc: 0.7\n    best_single_re_auroc: 0.721\n    ensemble_ner_delta: 0.035\n    selection_f1_ner:\n      greedy: 0.609\n      logprob: 0.609\n      sj: 0.604\n      ensemble: 0.604\n      voting: 0.596\n      random: 0.58\n      oracle: 0.769\n    selection_f1_re:\n      logprob: 0.397\n      greedy: 0.374\n      sj: 0.368\n      ensemble: 0.367\n      voting: 0.338\n      random: 0.338\n      oracle: 0.561\n    diagnosis: 'SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best\n      is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER.\n      Oracle gap still huge.'\n- id: exp-017\n  name: ner_llama_conll\n  claim: 1\n  description: 'LLaMA-3.1-8B on CoNLL-2003 to strengthen cross-model validation. Dream\n    2 flagged LLaMA only on SciERC is insufficient for model-agnostic claim.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-007\n  dataset: CoNLL-2003\n  model: llama-3.1-8b (fine-tune on CoNLL)\n  note: Only if exp-007 shows positive signal and GPU hours available.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: ft_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.1099\n    eval_loss: 0.0771\n    gate0_ner_f1_strict: 0.1143\n    gate0_re_f1_strict: 0.0125\n    gate0_ner_f1_text: 0.606\n    gate0_re_f1_text: 0.3392\n    gate0_offset_accuracy: 0.1665\n    gate0_parse_failures: 43\n    gate0_pass: false\n    gate0_realigned_ner_f1: 0.6045\n    gate0_realigned_re_f1: 0.338\n    gate0_realigned_entity_offset_accuracy: 1\n    gate0_realigned_relation_offset_accuracy: 1\n    gate0_realigned_ner_pass: true\n    gate0_realigned_re_pass: false\n    gate0_realigned_pass: false\n    gate0_ner_f1_delta_realign: 0.4901\n    gate0_re_f1_delta_realign: 0.3255\n    verdict_note: 'partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)'\n- exp_id: mvp_pilot_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.611\n    ner_oracle_f1: 0.78\n    ner_headroom: 0.169\n    ner_fleiss_kappa_mean: 0.2449\n    ner_soft_jaccard_mean: 0.5041\n    ner_full_rho_sj: 0.3616\n    ner_full_rho_fk: 0.3515\n    ner_full_n: 529\n    ner_cond_rho_sj: 0.3688\n    ner_cond_rho_fk: 0.3569\n    ner_cond_n: 510\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_sample_f1_pct_zero: 20.4\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 19\n    re_greedy_f1: 0.355\n    re_oracle_f1: 0.572\n    re_headroom: 0.217\n    re_fleiss_kappa_mean: 0.0681\n    re_soft_jaccard_mean: 0.3635\n    re_full_rho_sj: 0.2535\n    re_full_rho_fk: 0.2885\n    re_full_n: 397\n    re_cond_rho_sj: 0.3515\n    re_cond_rho_fk: 0.3107\n    re_cond_n: 320\n    re_sj_beats_fk_full: false\n    re_sj_beats_fk_cond: true\n    re_sample_f1_pct_zero: 58.3\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 77\n    parse_failures_stochastic: 164\n    parse_failures_greedy: 29\n    total_stochastic_samples: 4408\n    total_greedy: 551\n    verdict: FAIL\n    verdict_reason: RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\n- exp_id: ft_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    last_step: 70\n    total_steps: 585\n    progress_pct: 11.97\n    last_loss: 0.1134\n    last_lr: 0.00019982\n    elapsed: 3m32s\n    failure_reason: OOM at step 73, batch_size=4 too large for 32GB RTX 5090\n- exp_id: mvp_pilot_002\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_pilot_003\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.6362\n    ner_oracle_f1: 0.792\n    ner_headroom: 0.1559\n    ner_fleiss_kappa_mean: 0.2488\n    ner_soft_jaccard_mean: 0.5066\n    ner_full_rho_sj: 0.3808\n    ner_full_rho_fk: 0.3362\n    ner_full_p_sj: 1.07e-19\n    ner_full_p_fk: 1.93e-15\n    ner_full_n: 529\n    ner_cond_rho_sj: 0.3836\n    ner_cond_rho_fk: 0.3187\n    ner_cond_p_sj: 1.83e-19\n    ner_cond_p_fk: 1.33e-13\n    ner_cond_n: 514\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_rho_advantage: 0.0446\n    ner_sample_f1_mean: 0.5153\n    ner_sample_f1_std: 0.3334\n    ner_sample_f1_pct_zero: 19.9\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 15\n    re_greedy_f1: 0.3774\n    re_oracle_f1: 0.5939\n    re_headroom: 0.2165\n    re_fleiss_kappa_mean: 0.0879\n    re_soft_jaccard_mean: 0.3958\n    re_full_rho_sj: 0.2367\n    re_full_rho_fk: 0.2221\n    re_full_p_sj: 1.85e-06\n    re_full_p_fk: 7.92e-06\n    re_full_n: 397\n    re_cond_rho_sj: 0.3004\n    re_cond_rho_fk: 0.2374\n    re_cond_p_sj: 2.25e-08\n    re_cond_p_fk: 1.19e-05\n    re_cond_n: 333\n    re_sj_beats_fk_full: true\n    re_sj_beats_fk_cond: true\n    re_rho_advantage: 0.0146\n    re_sample_f1_mean: 0.1977\n    re_sample_f1_std: 0.3251\n    re_sample_f1_pct_zero: 67.6\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 64\n    parse_failures_stochastic: 0\n    parse_failures_greedy: 0\n    total_stochastic_samples: 4408\n    total_greedy: 551\n    verdict: FAIL\n    verdict_reason: RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but\n      below PASS bar\n- exp_id: ft_002_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch: 5\n    train_loss: 0.0806\n    eval_loss: 0.089\n    train_runtime: 28m41s\n    train_samples_per_second: 5.407\n    train_steps_per_second: 0.34\n    total_steps: 585\n    checkpoints:\n    - checkpoint-400\n    - checkpoint-500\n    - checkpoint-585\n    gate0_final_ner_f1: 0.6615\n    gate0_final_re_f1: 0.4177\n    gate0_final_parse_failures: 0\n    gate0_final_ner_pass: true\n    gate0_final_re_pass: true\n    gate0_final_pass: true\n    gate0_ckpt400_ner_f1: 0.6475\n    gate0_ckpt400_re_f1: 0.3793\n    gate0_ckpt400_parse_failures: 0\n    gate0_ckpt400_verdict: FAIL\n    gate0_ckpt400_re_sample_f1_pct_zero: 58.8\n    gate0_ckpt400_warning: '>30% samples F1=0'\n- exp_id: mvp_pilot_004\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.6671\n    ner_oracle_f1: 0.7756\n    ner_headroom: 0.1085\n    ner_fleiss_kappa_mean: 0.4048\n    ner_soft_jaccard_mean: 0.7008\n    ner_full_rho_fk: 0.259\n    ner_full_rho_sj: 0.3825\n    ner_full_n: 529\n    ner_cond_rho_fk: 0.2352\n    ner_cond_rho_sj: 0.3762\n    ner_cond_n: 508\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_sample_f1_mean: 0.6084\n    ner_sample_f1_std: 0.3174\n    ner_sample_f1_pct_zero: 12.19\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 21\n    re_greedy_f1: 0.4208\n    re_oracle_f1: 0.5882\n    re_headroom: 0.1674\n    re_fleiss_kappa_mean: 0.2996\n    re_soft_jaccard_mean: 0.6114\n    re_full_rho_fk: 0.2782\n    re_full_rho_sj: 0.2441\n    re_full_n: 397\n    re_cond_rho_fk: 0.3067\n    re_cond_rho_sj: 0.3161\n    re_cond_n: 313\n    re_sj_beats_fk_full: false\n    re_sj_beats_fk_cond: true\n    re_sample_f1_mean: 0.3612\n    re_sample_f1_std: 0.383\n    re_sample_f1_pct_zero: 44.3\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 84\n    parse_failures: 0\n    verdict: FAIL\n- exp_id: mvp_pilot_005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_greedy_f1: 0.6619\n    ner_oracle_f1: 0.7585\n    ner_headroom: 0.0966\n    ner_fleiss_kappa_mean: 0.4722\n    ner_soft_jaccard_mean: 0.7757\n    ner_full_rho_sj: 0.3875\n    ner_full_rho_fk: 0.3211\n    ner_full_n: 529\n    ner_cond_rho_sj: 0.3868\n    ner_cond_rho_fk: 0.305\n    ner_cond_n: 504\n    ner_sj_beats_fk_full: true\n    ner_sj_beats_fk_cond: true\n    ner_rho_advantage: 0.0664\n    ner_sample_f1_mean: 0.6243\n    ner_sample_f1_std: 0.3131\n    ner_sample_f1_pct_zero: 11.2\n    ner_gold_empty_filtered: 22\n    ner_all_zero_filtered: 25\n    re_greedy_f1: 0.4219\n    re_oracle_f1: 0.5532\n    re_headroom: 0.1313\n    re_fleiss_kappa_mean: 0.3829\n    re_soft_jaccard_mean: 0.687\n    re_full_rho_sj: 0.2343\n    re_full_rho_fk: 0.1835\n    re_full_n: 397\n    re_cond_rho_sj: 0.3716\n    re_cond_rho_fk: 0.2533\n    re_cond_n: 301\n    re_sj_beats_fk_full: true\n    re_sj_beats_fk_cond: true\n    re_rho_advantage: 0.0508\n    re_sample_f1_mean: 0.3782\n    re_sample_f1_std: 0.3845\n    re_sample_f1_pct_zero: 42.4\n    re_gold_empty_filtered: 154\n    re_all_zero_filtered: 96\n    parse_failures: 0\n    verdict: FAIL\n    verdict_note: RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional\n      but not full threshold\n- exp_id: e1_component_wise_re_sj\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    full_head_sj_rho: 0.21\n    full_tail_sj_rho: 0.201\n    full_type_match_rho: 0.201\n    full_multiplicative_rho: 0.244\n    full_additive_rho: 0.243\n    full_fleiss_kappa_rho: 0.278\n    cond_head_sj_rho: 0.27\n    cond_tail_sj_rho: 0.259\n    cond_type_match_rho: 0.252\n    cond_multiplicative_rho: 0.316\n    cond_additive_rho: 0.306\n    cond_fleiss_kappa_rho: 0.307\n    n_full: 397\n    n_conditional: 313\n    diagnosis: 'head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis\n      REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for\n      RE.'\n- exp_id: exp_012_logprob_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho_sj: 0.3565\n    ner_full_rho_fk: 0.2651\n    ner_full_rho_logprob: 0.1396\n    ner_full_rho_greedy_logprob: 0.1615\n    ner_full_tau_sj: 0.2658\n    ner_full_tau_logprob: 0.1006\n    ner_full_auroc_sj: 0.6892\n    ner_full_auroc_fk: 0.6292\n    ner_full_auroc_logprob: 0.5907\n    ner_full_n: 529\n    ner_sj_vs_logprob_delta: 0.2169\n    re_full_rho_sj: 0.2112\n    re_full_rho_fk: 0.2528\n    re_full_rho_logprob: 0.2467\n    re_full_auroc_sj: 0.5916\n    re_full_auroc_fk: 0.6262\n    re_full_auroc_logprob: 0.6186\n    re_full_n: 397\n    re_cond_rho_sj: 0.3683\n    re_cond_rho_fk: 0.3168\n    re_cond_rho_logprob: 0.1457\n    re_cond_auroc_sj: 0.6839\n    re_cond_auroc_logprob: 0.5487\n    re_cond_n: 296\n    diagnosis: 'NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead.\n      RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.'\n- exp_id: exp_013_exact_match_voting\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner_full_rho: 0.2941\n    ner_full_p: 5.12e-12\n    ner_full_tau: 0.2181\n    ner_full_auroc: 0.6398\n    re_full_rho: 0.1562\n    re_full_p: 0.0018\n    re_full_tau: 0.1185\n    re_full_auroc: 0.5863\n    diagnosis: EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\n- exp_id: exp_014_entity_majority_voting\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_full_rho: 0.3915\n    ner_full_p: 8.1e-21\n    ner_full_tau: 0.2906\n    ner_full_auroc: 0.7039\n    re_full_rho: 0.3403\n    re_full_p: 3.21e-12\n    re_full_tau: 0.256\n    re_full_auroc: 0.6668\n    ner_voting_f1: 0.6246\n    ner_greedy_f1: 0.6483\n    ner_oracle_f1: 0.7793\n    re_voting_f1: 0.3577\n    re_greedy_f1: 0.4022\n    re_oracle_f1: 0.5886\n    diagnosis: Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE\n      (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\n- exp_id: exp_001_ner_n16_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_instances: 551\n    ner_n: 529\n    re_n: 397\n    N: 16\n    T: 1\n    seed: 42\n    full_test_set: true\n    ner_voting_conf_rho: 0.399\n    ner_sj_rho: 0.398\n    ner_em_rho: 0.339\n    ner_fk_rho: 0.288\n    ner_logprob_rho: 0.237\n    ner_voting_conf_auroc: 0.704\n    ner_sj_auroc: 0.697\n    ner_cond_em_rho: 0.414\n    ner_cond_sj_rho: 0.349\n    ner_cond_vc_rho: 0.34\n    re_voting_conf_rho: 0.38\n    re_logprob_rho: 0.293\n    re_fk_rho: 0.281\n    re_sj_rho: 0.277\n    re_em_rho: 0.148\n    re_voting_conf_auroc: 0.699\n    re_cond_em_rho: 0.475\n    re_cond_sj_rho: 0.318\n    re_cond_vc_rho: 0.35\n    re_cond_em_auroc: 0.742\n    diagnosis: '551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380).\n      EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full\n      FAIL (SJ 0.277 < 0.40). Previous N-scaling ''breakthrough'' was artifact of\n      200 instances + T=0.7.'\n- exp_id: exp_002_ner_conll2003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_003_ner_wnut17\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      greedy_f1: 0.525\n      oracle_f1: 0.664\n      headroom: 0.139\n      rho_sj_full: 0.082\n      rho_fk_full: 0.124\n      rho_logprob_full: -0.414\n      rho_sj_cond: 0.275\n      rho_fk_cond: 0.164\n      rho_logprob_cond: 0.352\n      sj_beats_logprob_cond: false\n    n_instances: 1287\n    n_gold_empty: 598\n    sample_f1_mean: 0.401\n    sample_f1_pct_zero: 53.7\n    N: 16\n    T: 1\n    seed: 42\n    verdict: FAIL\n    verdict_note: '>30% samples F1=0; structural rho weak; logprob baseline stronger'\n- exp_id: exp_007_ner_multi_model\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    epoch: 5\n    train_loss: 0.0767\n    eval_loss: 0.1049\n    train_runtime_sec: 1494.5\n    train_samples_per_second: 6.226\n    checkpoints:\n    - checkpoint-400\n    - checkpoint-500\n    - checkpoint-585\n    base_model: Meta-Llama-3.1-8B-Instruct\n    lora_r: 32\n    lora_alpha: 64\n    note: EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal.\n      Checkpoint fully intact.\n- exp_id: exp_007_ner_llama\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_015_metrics_expansion\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_012_logprob/samples_with_logprobs.jsonl\n    config: N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\n    ner:\n      n_valid: 529\n      n_cond: 501\n      voting_rho_full: 0.5018\n      voting_rho_cond: 0.4497\n      voting_auroc: 0.7279\n      voting_tau: 0.3766\n      sj_rho_full: 0.3565\n      sj_rho_cond: 0.412\n      sj_auroc: 0.6656\n      sj_tau: 0.2658\n      em_rho_full: 0.2566\n      em_rho_cond: 0.3427\n      em_auroc: 0.623\n      em_tau: 0.1924\n      fk_rho_full: 0.2651\n      fk_rho_cond: 0.306\n      fk_auroc: 0.6243\n      fk_tau: 0.2027\n      logprob_rho_full: 0.1396\n      logprob_rho_cond: 0.1627\n      logprob_auroc: 0.5585\n      logprob_tau: 0.1006\n    re:\n      n_valid: 397\n      n_cond: 296\n      voting_rho_full: 0.4217\n      voting_rho_cond: 0.463\n      voting_auroc: 0.7162\n      voting_tau: 0.327\n      sj_rho_full: 0.2112\n      sj_rho_cond: 0.3683\n      sj_auroc: 0.5816\n      sj_tau: 0.1619\n      em_rho_full: 0.1002\n      em_rho_cond: 0.3607\n      em_auroc: 0.5036\n      em_tau: 0.0839\n      fk_rho_full: 0.2528\n      fk_rho_cond: 0.3168\n      fk_auroc: 0.6308\n      fk_tau: 0.1967\n      logprob_rho_full: 0.2467\n      logprob_rho_cond: 0.1457\n      logprob_auroc: 0.6354\n      logprob_tau: 0.1808\n    diagnosis: 'Unified 5-signal evaluation on single data source. Voting leads NER\n      full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals\n      beat logprob on NER. RE: voting leads both full and cond.'\n- exp_id: exp_004_re_diagnostic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    per_relation_type:\n      HYPONYM-OF:\n        n: 36\n        rho_sj: 0.545\n        rho_fk: 0.646\n        rho_vc: 0.628\n        mean_f1: 0.513\n      CONJUNCTION:\n        n: 86\n        rho_sj: 0.383\n        rho_fk: 0.35\n        rho_vc: 0.484\n        mean_f1: 0.48\n      USED-FOR:\n        n: 299\n        rho_sj: 0.236\n        rho_fk: 0.255\n        rho_vc: 0.286\n        mean_f1: 0.422\n      PART-OF:\n        n: 44\n        rho_sj: 0.239\n        rho_fk: 0.348\n        rho_vc: 0.283\n        mean_f1: 0.297\n      EVALUATE-FOR:\n        n: 62\n        rho_sj: 0.172\n        rho_fk: 0.255\n        rho_vc: 0.226\n        mean_f1: 0.365\n      COMPARE:\n        n: 35\n        rho_sj: 0.168\n        rho_fk: 0.184\n        rho_vc: 0.18\n        mean_f1: 0.453\n      FEATURE-OF:\n        n: 50\n        rho_sj: 0.004\n        rho_fk: 0.052\n        rho_vc: 0.014\n        mean_f1: 0.254\n    error_propagation:\n      total_fn: 553\n      tail_error_pct: 21.9\n      full_error_pct: 21.7\n      head_error_pct: 17.7\n      head_tail_error_pct: 15.9\n      type_error_pct: 8.3\n      worst_consistency: head_type_error (sj=0.411)\n      best_consistency: head_error (sj=0.613)\n    threshold_sensitivity:\n      thr_0.00_rho_sj: 0.3161\n      thr_0.00_rho_vc: 0.3841\n      thr_0.00_n: 313\n      thr_0.05_rho_sj: 0.2682\n      thr_0.05_rho_vc: 0.2364\n      thr_0.05_n: 239\n    bootstrap_ci_95:\n      ner_sj:\n      - 0.2946\n      - 0.4586\n      ner_voting_conf:\n      - 0.3048\n      - 0.4656\n      re_sj:\n      - 0.1422\n      - 0.3391\n      re_voting_conf:\n      - 0.1818\n      - 0.3721\n      re_cond_sj:\n      - 0.2161\n      - 0.4102\n      re_cond_voting_conf:\n      - 0.2825\n      - 0.474\n    fisher_z_ner_vs_re:\n      sj_z: 2.31\n      sj_p: 0.0209\n      sj_significant: true\n      fk_z: -0.31\n      fk_p: 0.756\n      fk_significant: false\n      voting_z: 1.914\n      voting_p: 0.0556\n      voting_significant: false\n    diagnosis: FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF\n      strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of\n      RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE\n      signal in conditional set (rho=0.384).\n- exp_id: exp_008_re_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.6635\n      oracle_f1: 0.8208\n      headroom: 0.1572\n      rho_sj_full: 0.377\n      rho_fk_full: 0.2508\n      rho_logprob_full: 0.3153\n      rho_sj_cond: 0.3598\n      rho_fk_cond: 0.2251\n      rho_logprob_cond: 0.2927\n      sj_beats_fk: true\n      rho_advantage: 0.1262\n    re:\n      greedy_f1: 0.4339\n      oracle_f1: 0.6658\n      headroom: 0.2319\n      rho_sj_full: 0.2966\n      rho_fk_full: 0.2871\n      rho_logprob_full: 0.2986\n      rho_sj_cond: 0.3975\n      rho_fk_cond: 0.3774\n      rho_logprob_cond: 0.2745\n      sj_beats_fk: true\n      rho_advantage: 0.0095\n    verdict: FAIL\n- exp_id: exp001_seed123\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp001_seed456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp008_re_n16\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_n16_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.655\n      oracle_f1: 0.8028\n      headroom: 0.1478\n      rho_sj_full: 0.4076\n      rho_fk_full: 0.2799\n      rho_logprob_full: 0.3189\n      rho_sj_cond: 0.4271\n      rho_fk_cond: 0.2743\n      rho_logprob_cond: 0.2835\n      sj_beats_fk: true\n      rho_advantage: 0.1277\n    re:\n      greedy_f1: 0.4243\n      oracle_f1: 0.6771\n      headroom: 0.2528\n      rho_sj_full: 0.2943\n      rho_fk_full: 0.2657\n      rho_logprob_full: 0.3005\n      rho_sj_cond: 0.4003\n      rho_fk_cond: 0.313\n      rho_logprob_cond: 0.2317\n      sj_beats_fk: true\n      rho_advantage: 0.0286\n    verdict: FAIL\n- exp_id: exp_001_n16_seed456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.6577\n      oracle_f1: 0.8129\n      headroom: 0.1553\n      rho_sj_full: 0.3297\n      rho_fk_full: 0.2578\n      rho_logprob_full: 0.2866\n      rho_sj_cond: 0.3394\n      rho_fk_cond: 0.2721\n      rho_logprob_cond: 0.2567\n      sj_beats_fk: true\n      rho_advantage: 0.0719\n    re:\n      greedy_f1: 0.4312\n      oracle_f1: 0.6737\n      headroom: 0.2425\n      rho_sj_full: 0.285\n      rho_fk_full: 0.2372\n      rho_logprob_full: 0.2626\n      rho_sj_cond: 0.3525\n      rho_fk_cond: 0.2614\n      rho_logprob_cond: 0.1927\n      sj_beats_fk: true\n      rho_advantage: 0.0478\n    verdict: FAIL\n- exp_id: exp_016_signal_ensemble\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_logprob_pearson_ner: 0.57\n    sj_logprob_pearson_re: 0.42\n    best_linear_ner:\n      combo: SJ+voting_conf\n      alpha: 0.3\n      rho: 0.489\n    best_linear_re:\n      combo: voting_conf+logprob\n      alpha: 0.6\n      rho: 0.429\n    ensemble_ner_auroc: 0.735\n    ensemble_re_auroc: 0.719\n    best_single_ner_auroc: 0.7\n    best_single_re_auroc: 0.721\n    ensemble_ner_delta: 0.035\n    selection_f1_ner:\n      greedy: 0.609\n      logprob: 0.609\n      sj: 0.604\n      ensemble: 0.604\n      voting: 0.596\n      random: 0.58\n      oracle: 0.769\n    selection_f1_re:\n      logprob: 0.397\n      greedy: 0.374\n      sj: 0.368\n      ensemble: 0.367\n      voting: 0.338\n      random: 0.338\n      oracle: 0.561\n    diagnosis: 'SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best\n      is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER.\n      Oracle gap still huge.'\n- exp_id: exp_002_merge_conll2003\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_rho_full: 0.4357\n    sj_tau_full: 0.3851\n    sj_auroc_full: 0.8008\n    sj_rho_cond: 0.4511\n    fk_rho_full: 0.3998\n    fk_tau_full: 0.3568\n    fk_auroc_full: 0.7741\n    fk_rho_cond: 0.4064\n    logprob_rho_full: 0.3157\n    logprob_tau_full: 0.2469\n    logprob_auroc_full: 0.7532\n    logprob_rho_cond: 0.3562\n    em_rho_full: 0.4507\n    em_tau_full: 0.4002\n    em_auroc_full: 0.8156\n    em_rho_cond: 0.4799\n    ev_rho_full: 0.4237\n    ev_tau_full: 0.3777\n    ev_auroc_full: 0.7889\n    ev_rho_cond: 0.4127\n    greedy_f1: 0.9123\n    oracle_f1: 0.9543\n    voting_f1: 0.9141\n    oracle_headroom: 0.042\n    sj_vs_logprob_delta_rho: 0.12\n    sj_vs_logprob_ci_low: 0.0881\n    sj_vs_logprob_ci_high: 0.154\n    sj_vs_logprob_significant: true\n    n_instances: 3453\n    n_valid: 2756\n    n_samples: 8\n    temperature: 1\n- exp_id: exp_001_n16_seed123_full\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_n16_seed456_full\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_008_re_n16_full\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_001_ner_n16_seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.663\n      oracle_f1: 0.809\n      headroom: 0.146\n      rho_sj: 0.423\n      rho_fk: 0.29\n      rho_logprob: 0.239\n      rho_sj_cond: 0.423\n      rho_fk_cond: 0.26\n    re:\n      greedy_f1: 0.419\n      oracle_f1: 0.625\n      headroom: 0.206\n      rho_sj: 0.267\n      rho_fk: 0.315\n      rho_sj_cond: 0.364\n      rho_fk_cond: 0.331\n    verdict: FAIL\n    verdict_note: RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\n    n_instances: 551\n    seed: 123\n    N: 16\n    T: 1\n- exp_id: exp_001_seed456_t10_full\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      rho_sj: 0.414\n      rho_fk: 0.298\n    re:\n      rho_sj: 0.268\n      rho_fk: 0.26\n    n_instances: 551\n    N: 16\n    T: 1\n    seed: 456\n    source: reviewer_verified_report_json\n- exp_id: exp_001_seed123_t10_full\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      rho_sj: 0.417\n      rho_fk: 0.283\n    re:\n      rho_sj: 0.265\n      rho_fk: 0.315\n    n_instances: 551\n    N: 16\n    T: 1\n    seed: 123\n    source: reviewer_verified_report_json\n- exp_id: exp_008_re_n16_t10_full\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ner:\n      rho_sj: 0.444\n    re:\n      rho_sj: 0.248\n    n_instances: 551\n    N: 16\n    T: 1\n    seed: 42\n    mode: RE-only\n    source: director_corrected\n- exp_id: exp_003_wnut17_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.523\n    oracle_f1: 0.664\n    headroom: 0.141\n    rho_fk: 0.125\n    rho_sj: 0.089\n    rho_fk_cond: 0.169\n    rho_sj_cond: 0.288\n    rho_logprob_full: -0.409\n    rho_logprob_cond: 0.35\n    structural_beats_surface: false\n    sample_f1_pct_zero: 53.7\n    n_instances: 1287\n    N: 16\n    T: 1\n    seed: 42\n    model: Qwen3-8B\n    n_gold_empty_filtered: 598\n    verdict: FAIL\n    verdict_note: structural_beats_surface=false; >50% samples F1=0\n- exp_id: exp_007_llama_inference\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner:\n      greedy_f1: 0.66\n      oracle_f1: 0.781\n      headroom: 0.121\n      rho_fk: 0.327\n      rho_sj: 0.363\n      rho_fk_cond: 0.226\n      rho_sj_cond: 0.311\n      rho_logprob: 0.183\n      rho_logprob_cond: 0.109\n      structural_beats_surface: true\n      sample_f1_pct_zero: 11.6\n    re:\n      greedy_f1: 0.434\n      oracle_f1: 0.568\n      headroom: 0.135\n      rho_fk: 0.305\n      rho_sj: 0.299\n      rho_fk_cond: 0.259\n      rho_sj_cond: 0.405\n      rho_logprob: 0.288\n      rho_logprob_cond: 0.092\n      structural_beats_surface: false\n      sample_f1_pct_zero: 41.2\n    n_instances: 551\n    N: 8\n    T: 1\n    seed: 42\n    model: LLaMA-3.1-8B-Instruct\n    verdict: FAIL\n    verdict_note: RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\n- exp_id: exp_001_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_rho_full: 0.428\n    sj_rho_cond: 0.369\n    structural_minus_surface: 0.147\n    conclusion_note: NER seed42 robustness confirmed, structural>surface +0.147\n- exp_id: exp_001_seed123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sj_rho_full: 0.424\n    sj_rho_cond: 0.376\n    structural_minus_surface: 0.149\n    conclusion_note: NER seed123 robustness confirmed, structural>surface +0.149\n- exp_id: exp_008_re_n16_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    sj_rho_full: 0.281\n    sj_rho_cond: 0.308\n    f1_zero_pct: 44.3\n    conclusion_note: 'RE N=16 v2 negative: SJ weak, 44.3% F1=0'\n- exp_id: exp_017_llama_conll\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_009_capability_stratification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n: 551\n      sj_rho_overall: 0.398\n      by_greedy_f1:\n        hard_0_25_sj_rho: 0.159\n        med_low_sj_rho: 0.139\n        med_high_sj_rho: 0.09\n        easy_sj_rho: 0.23\n      by_sent_len:\n        Q1_sj_rho: 0.461\n        Q2_sj_rho: 0.401\n        Q3_sj_rho: 0.296\n        Q4_sj_rho: 0.382\n      by_ent_count:\n        0_sj_rho: 0.689\n        1_2_sj_rho: 0.415\n        3_5_sj_rho: 0.353\n        6plus_sj_rho: 0.547\n    scierc_re:\n      n: 551\n      by_greedy_f1:\n        hard_0_25_sj_rho: -0.043\n        easy_sj_rho: 0.21\n      by_sent_len:\n        Q1_sj_rho: 0.447\n        Q4_sj_rho: 0.54\n      by_rel_count:\n        0_sj_rho: 0.62\n        1_2_sj_rho: 0.275\n        6plus_sj_rho: 0.527\n    conll_ner:\n      n: 3453\n      by_sent_len:\n        Q1_sj_rho: 0.334\n        Q3_sj_rho: 0.518\n    proxy_independence:\n      scierc_ner_f1_vs_slen: -0.021\n      scierc_ner_f1_vs_ecnt: 0.007\n      scierc_re_f1_vs_slen: -0.147\n- exp_id: exp_010_selection_curves\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_ner:\n      n_instances: 551\n      greedy_f1: 0.618\n      N16:\n        oracle: 0.787\n        SJ: 0.62\n        FK: 0.621\n        logprob: 0.621\n        voting_conf: 0.585\n        EM: 0.606\n        random: 0.595\n      N8:\n        oracle: 0.752\n        SJ: 0.614\n        FK: 0.614\n        logprob: 0.619\n        voting_conf: 0.591\n        EM: 0.603\n        random: 0.589\n      N4:\n        oracle: 0.714\n        SJ: 0.607\n        FK: 0.608\n        logprob: 0.616\n        voting_conf: 0.594\n        EM: 0.6\n        random: 0.587\n    scierc_re:\n      n_instances: 397\n      greedy_f1: 0.403\n      N16:\n        oracle: 0.631\n        SJ: 0.397\n        FK: 0.396\n        logprob: 0.41\n        voting_conf: 0.408\n        EM: 0.381\n        random: 0.364\n      N8:\n        oracle: 0.583\n        SJ: 0.393\n        FK: 0.394\n        logprob: 0.413\n        voting_conf: 0.398\n        EM: 0.381\n        random: 0.363\n    conll_ner:\n      n_instances: 3453\n      greedy_f1: 0.725\n      N8:\n        oracle: 0.757\n        SJ: 0.718\n        FK: 0.717\n        logprob: 0.716\n        voting_conf: 0.714\n        EM: 0.716\n        random: 0.69\n      N4:\n        oracle: 0.746\n        SJ: 0.714\n        FK: 0.714\n        logprob: 0.715\n        voting_conf: 0.714\n        EM: 0.712\n        random: 0.692\n- exp_id: exp_007_llama_seed123\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    ner:\n      greedy_f1: 0.6605\n      oracle_f1: 0.7703\n      headroom: 0.1098\n      fleiss_kappa: 0.4553\n      soft_jaccard: 0.7525\n      rho_kappa_f1: 0.2143\n      rho_sj_f1: 0.3371\n      structural_gt_surface: true\n    re:\n      greedy_f1: 0.433\n      oracle_f1: 0.5719\n      headroom: 0.1389\n      fleiss_kappa: 0.3851\n      soft_jaccard: 0.6911\n      rho_kappa_f1: 0.2844\n      rho_sj_f1: 0.268\n      structural_gt_surface: false\n    fail_reasons:\n    - RE rho_sj=0.2680 < 0.40 threshold\n    - '>30% samples F1=0 (RE: 41.0%)'\n    - RE structural not > surface (delta=-0.0165)\n- exp_id: exp_007_llama_seed456\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    ner:\n      greedy_f1: 0.6597\n      oracle_f1: 0.7575\n      oracle_headroom: 0.0978\n      fleiss_kappa: 0.4543\n      soft_jaccard: 0.7491\n      rho_kappa_f1: 0.3115\n      rho_sj_f1: 0.3663\n      structural_gt_surface: true\n    re:\n      greedy_f1: 0.4334\n      oracle_f1: 0.5789\n      oracle_headroom: 0.1455\n      fleiss_kappa: 0.3791\n      soft_jaccard: 0.6782\n      rho_kappa_f1: 0.3013\n      rho_sj_f1: 0.287\n      structural_gt_surface: false\n    logprob_ner:\n      rho: 0.1911\n      auroc: 0.5989\n    logprob_re:\n      rho: 0.3246\n      auroc: 0.6678\n    fail_reason: RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\n- exp_id: exp_008_re_seed123\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    greedy_f1: 0.4229\n    oracle_f1: 0.6244\n    oracle_headroom: 0.2015\n    fleiss_kappa_mean: 0.3455\n    soft_jaccard_mean: 0.6126\n    sample_f1_mean: 0.3594\n    sample_f1_std: 0.3793\n    sample_f1_zero_pct: 44.1\n    structural_gt_surface: false\n    rho_kappa_f1_full: 0.3174\n    rho_sj_f1_full: 0.2835\n    rho_kappa_f1_cond: 0.0766\n    rho_sj_f1_cond: 0.2877\n    logprob_auroc_full: 0.6499\n    logprob_auroc_cond: 0.5265\n    verdict: FAIL\n- exp_id: exp_005_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_006_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    NER_SciERC_s42:\n      greedy: 0.618\n      oracle: 0.787\n      SJ: 0.62\n      logprob: 0.621\n      FK: 0.621\n      EM: 0.606\n      voting_conf: 0.585\n      random: 0.586\n    NER_SciERC_s123:\n      greedy: 0.618\n      oracle: 0.785\n      SJ: 0.617\n      logprob: 0.618\n      FK: 0.621\n      EM: 0.613\n      voting_conf: 0.584\n      random: 0.583\n    NER_CoNLL:\n      greedy: 0.725\n      oracle: 0.757\n      SJ: 0.718\n      logprob: 0.716\n      FK: 0.717\n      EM: 0.716\n      voting_conf: 0.714\n      random: 0.692\n    RE_SciERC:\n      greedy: 0.403\n      oracle: 0.631\n      SJ: 0.397\n      logprob: 0.41\n      FK: 0.396\n      EM: 0.381\n      voting_conf: 0.408\n      random: 0.364\n- exp_id: exp_004_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_003_wnut17_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_015_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    auroc_best:\n      SJ:\n        conll_ner: 0.8008\n        scierc_ner_avg: 0.7328\n        scierc_re_avg: 0.6788\n        llama_ner_avg: 0.7029\n        llama_re_avg: 0.7144\n        wnut_ner: 0.5844\n      FK:\n        conll_ner: 0.7741\n        scierc_ner_avg: 0.6172\n        scierc_re_avg: 0.5939\n        llama_ner_avg: 0.6484\n        llama_re_avg: 0.6778\n        wnut_ner: 0.5752\n      logprob:\n        conll_ner: 0.7532\n        scierc_ner_avg: 0.5918\n        scierc_re_avg: 0.5849\n        llama_ner_avg: 0.5584\n        llama_re_avg: 0.654\n        wnut_ner: 0.358\n      EM:\n        conll_ner: 0.8156\n        scierc_ner_avg: 0.7873\n        scierc_re_avg: 0.715\n        llama_ner_avg: 0.7533\n        llama_re_avg: 0.7557\n        wnut_ner: 0.5745\n      voting_conf:\n        conll_ner: 0.7889\n        scierc_ner_avg: 0.7367\n        scierc_re_avg: 0.7195\n        llama_ner_avg: 0.7232\n        llama_re_avg: 0.7509\n        wnut_ner: 0.8692\n    loo_sj:\n      max_delta_rho: 0.000305\n      all_no_circularity: true\n    n_datasets: 10\n    n_subtask_combos: 18\n- exp_id: exp_009_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_seed42_global:\n      sj_rho: 0.431\n      fk_rho: 0.325\n      logprob_rho: 0.203\n      voting_conf_rho: 0.475\n      em_rho: 0.292\n    ner_seed123_global:\n      sj_rho: 0.422\n      fk_rho: 0.315\n      logprob_rho: 0.226\n      voting_conf_rho: 0.438\n      em_rho: 0.299\n    re_seed42_global:\n      sj_rho: 0.063\n      fk_rho: 0.226\n      logprob_rho: 0.4\n      voting_conf_rho: 0.22\n      em_rho: -0.132\n    ner_seed_stability_max_delta: 0.037\n    independent_proxies:\n    - sent_len\n    - ent_count\n    - type_diversity\n    inverted_u_ner: not confirmed (ρ stable across independent proxies)\n    inverted_u_re: monotonic increase with complexity, not inverted-U\n- exp_id: exp_001_seed456_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_016_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ner_conditional:\n      n: 529\n      best_single_signal_rho:\n        soft_jaccard: 0.4412\n      best_combo_rho:\n        sj+vc_a0.55: 0.4552\n      ensemble_auroc: 0.7141\n      best_single_auroc:\n        soft_jaccard: 0.7166\n      selection_f1:\n        greedy: 0.6442\n        logprob_best: 0.6505\n        ensemble_best: 0.6475\n        sj_best: 0.6471\n        oracle: 0.8442\n    re_conditional:\n      n: 397\n      best_single_signal_rho:\n        voting_confidence: 0.3849\n      best_combo_rho:\n        logprob+vc_a0.25: 0.3936\n      ensemble_auroc: 0.6916\n      best_single_auroc:\n        voting_confidence: 0.7023\n      selection_f1:\n        greedy: 0.403\n        logprob_best: 0.4097\n        ensemble_best: 0.4227\n        oracle: 0.6306\n    re_full:\n      ensemble_auroc: 0.8608\n      best_single_auroc:\n        voting_confidence: 0.8248\n- exp_id: exp_001_seed456_v2_ner\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    full:\n      SJ:\n        rho: 0.384\n        auroc: 0.711\n      FK:\n        rho: 0.223\n        auroc: 0.577\n      logprob:\n        rho: 0.232\n        auroc: 0.594\n      EM:\n        rho: 0.316\n        auroc: 0.768\n      voting_conf:\n        rho: 0.411\n        auroc: 0.712\n    conditional:\n      SJ:\n        rho: 0.349\n        auroc: 0.699\n      FK:\n        rho: 0.157\n        auroc: 0.561\n      logprob:\n        rho: 0.171\n        auroc: 0.576\n      EM:\n        rho: 0.406\n        auroc: 0.78\n      voting_conf:\n        rho: 0.346\n        auroc: 0.694\n    3seed_mean_SJ_rho_full: 0.412\n    3seed_sd_SJ_rho_full: 0.025\n    structural_beats_surface: true\n    verdict: MARGINAL\n- exp_id: exp_017_llama_conll_infer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9266\n    oracle_f1: 0.9443\n    oracle_headroom: 0.0177\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    N: 8\n    full:\n      SJ_rho: 0.4314\n      FK_rho: 0.4277\n      logprob_rho: 0.3072\n      EM_rho: 0.4306\n      voting_conf_rho: 0.4256\n      SJ_AUROC: 0.7039\n      FK_AUROC: 0.7026\n      logprob_AUROC: 0.761\n      EM_AUROC: 0.7046\n      voting_conf_AUROC: 0.7088\n      SJ_ECE: 0.1137\n      FK_ECE: 0.1053\n      logprob_ECE: 0.129\n      EM_ECE: 0.1094\n      voting_conf_ECE: 0.0949\n    conditional:\n      SJ_rho: 0.4356\n      FK_rho: 0.431\n      logprob_rho: 0.3282\n      EM_rho: 0.4403\n      voting_conf_rho: 0.3743\n      SJ_AUROC: 0.7225\n      FK_AUROC: 0.7208\n      logprob_AUROC: 0.8102\n      EM_AUROC: 0.7257\n      voting_conf_AUROC: 0.6989\n      SJ_ECE: 0.0829\n      FK_ECE: 0.0796\n      logprob_ECE: 0.0922\n      EM_ECE: 0.0754\n      voting_conf_ECE: 0.0784\n- exp_id: exp_002_conll_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    N: 16\n    dataset: conll2003\n    subtask: ner\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2614\n    greedy_f1: 0.907\n    full:\n      SJ_rho: 0.4496\n      FK_rho: 0.3928\n      logprob_rho: 0.3146\n      EM_rho: 0.4627\n      voting_conf_rho: 0.4286\n      SJ_AUROC: 0.8264\n      FK_AUROC: 0.7821\n      logprob_AUROC: 0.7531\n      EM_AUROC: 0.8409\n      voting_conf_AUROC: 0.8071\n      SJ_ECE: 0.0747\n      FK_ECE: 0.1786\n      logprob_ECE: 0.2031\n      EM_ECE: 0.0786\n      voting_conf_ECE: 0.529\n    conditional:\n      SJ_rho: 0.4208\n      FK_rho: 0.3494\n      logprob_rho: 0.3756\n      EM_rho: 0.4658\n      voting_conf_rho: 0.3654\n      SJ_AUROC: 0.8405\n      FK_AUROC: 0.7819\n      logprob_AUROC: 0.8259\n      EM_AUROC: 0.8781\n      voting_conf_AUROC: 0.7951\n      SJ_ECE: 0.0982\n      FK_ECE: 0.1899\n      logprob_ECE: 0.2504\n      EM_ECE: 0.0997\n      voting_conf_ECE: 0.6096\n    n8_vs_n16_delta_rho_full:\n      SJ: 0.0139\n      FK: -0.007\n      logprob: -0.0011\n      EM: 0.012\n      voting_conf: 0.0049\n- exp_id: exp_007_llama_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    N: 16\n    dataset: scierc\n    subtask: ner\n    n_instances: 551\n    n_valid: 529\n    n_conditional: 478\n    greedy_f1: 0.645\n    full:\n      SJ_rho: 0.3791\n      FK_rho: 0.3081\n      logprob_rho: 0.2041\n      EM_rho: 0.3159\n      voting_conf_rho: 0.4515\n      SJ_AUROC: 0.717\n      FK_AUROC: 0.6581\n      logprob_AUROC: 0.5656\n      EM_AUROC: 0.7686\n      voting_conf_AUROC: 0.7266\n      SJ_ECE: 0.1019\n      FK_ECE: 0.1556\n      logprob_ECE: 0.084\n      EM_ECE: 0.1761\n      voting_conf_ECE: 0.1365\n    conditional:\n      SJ_rho: 0.3222\n      FK_rho: 0.2182\n      logprob_rho: 0.1286\n      EM_rho: 0.3563\n      voting_conf_rho: 0.3356\n      SJ_AUROC: 0.7014\n      FK_AUROC: 0.6392\n      logprob_AUROC: 0.545\n      EM_AUROC: 0.7708\n      voting_conf_AUROC: 0.6988\n      SJ_ECE: 0.1466\n      FK_ECE: 0.1853\n      logprob_ECE: 0.1141\n      EM_ECE: 0.1887\n      voting_conf_ECE: 0.2634\n    n8_vs_n16_delta_rho_full:\n      SJ: 0.0161\n      FK: -0.0185\n      logprob: 0.0214\n      EM: 0.0007\n      voting_conf: 0.0184\n- exp_id: exp_009_v2_re_rerun\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp_017_llama_conll_n16\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9243\n    oracle_f1: 0.9487\n    oracle_headroom: 0.0244\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    structural_beats_surface: true\n    full:\n      SJ_rho: 0.4642\n      SJ_AUROC: 0.7391\n      SJ_ECE: 0.1131\n      FK_rho: 0.4566\n      FK_AUROC: 0.736\n      FK_ECE: 0.1071\n      logprob_rho: 0.3058\n      logprob_AUROC: 0.7594\n      logprob_ECE: 0.1288\n      EM_rho: 0.4613\n      EM_AUROC: 0.7391\n      EM_ECE: 0.1084\n      voting_conf_rho: 0.4554\n      voting_conf_AUROC: 0.7406\n      voting_conf_ECE: 0.0844\n    conditional:\n      SJ_rho: 0.4597\n      SJ_AUROC: 0.7565\n      SJ_ECE: 0.0846\n      FK_rho: 0.4515\n      FK_AUROC: 0.753\n      FK_ECE: 0.0813\n      logprob_rho: 0.3193\n      logprob_AUROC: 0.8023\n      logprob_ECE: 0.0921\n      EM_rho: 0.4618\n      EM_AUROC: 0.7589\n      EM_ECE: 0.0757\n      voting_conf_rho: 0.3978\n      voting_conf_AUROC: 0.7287\n      voting_conf_ECE: 0.0742\n    best_of_n:\n      greedy: 0.9243\n      random_avg: 0.9213\n      sj_best: 0.9259\n      logprob_best: 0.925\n      voting_conf_best: 0.9268\n      oracle: 0.9487\n    n8_vs_n16_delta:\n      full_SJ_rho_delta: 0.0328\n      full_FK_rho_delta: 0.0289\n      full_logprob_rho_delta: -0.0014\n      full_EM_rho_delta: 0.0307\n      full_voting_conf_rho_delta: 0.0298\n      cond_SJ_rho_delta: 0.0241\n      cond_FK_rho_delta: 0.0205\n      cond_logprob_rho_delta: -0.0089\n      cond_EM_rho_delta: 0.0215\n      cond_voting_conf_rho_delta: 0.0235\n- exp_id: exp_017_llama_conll_n16_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9266\n    oracle_f1: 0.9497\n    oracle_headroom: 0.0231\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    structural_beats_surface: true\n    full:\n      SJ_rho: 0.4698\n      SJ_AUROC: 0.7402\n      SJ_ECE: 0.1135\n      FK_rho: 0.4594\n      FK_AUROC: 0.7351\n      FK_ECE: 0.1114\n      logprob_rho: 0.3161\n      logprob_AUROC: 0.768\n      logprob_ECE: 0.129\n      EM_rho: 0.4676\n      EM_AUROC: 0.7399\n      EM_ECE: 0.1082\n      voting_conf_rho: 0.4612\n      voting_conf_AUROC: 0.7429\n      voting_conf_ECE: 0.0832\n    conditional:\n      SJ_rho: 0.4712\n      SJ_AUROC: 0.7609\n      SJ_ECE: 0.0828\n      FK_rho: 0.4595\n      FK_AUROC: 0.7547\n      FK_ECE: 0.0858\n      logprob_rho: 0.3314\n      logprob_AUROC: 0.8134\n      logprob_ECE: 0.0922\n      EM_rho: 0.4732\n      EM_AUROC: 0.7626\n      EM_ECE: 0.075\n      voting_conf_rho: 0.4086\n      voting_conf_AUROC: 0.7338\n      voting_conf_ECE: 0.0706\n    best_of_n:\n      greedy: 0.9242\n      random_avg: 0.9216\n      sj_best: 0.9247\n      logprob_best: 0.9253\n      voting_conf_best: 0.9255\n      oracle: 0.9486\n    n8_vs_n16_delta:\n      full_SJ_rho_delta: 0.0384\n      full_FK_rho_delta: 0.0317\n      full_logprob_rho_delta: 0.0089\n      full_SJ_AUROC_delta: 0.0363\n      full_FK_AUROC_delta: 0.0325\n      full_logprob_AUROC_delta: 0.007\n      cond_SJ_rho_delta: 0.0356\n      cond_FK_rho_delta: 0.0285\n      cond_logprob_rho_delta: 0.0032\n- exp_id: exp_017_llama_conll_n16_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy_f1: 0.9243\n    oracle_f1: 0.9488\n    oracle_headroom: 0.0245\n    n_instances: 3453\n    n_valid: 2756\n    n_conditional: 2642\n    structural_beats_surface: true\n    full:\n      SJ_rho: 0.4552\n      SJ_AUROC: 0.7288\n      SJ_ECE: 0.1134\n      FK_rho: 0.4478\n      FK_AUROC: 0.7248\n      FK_ECE: 0.109\n      logprob_rho: 0.3078\n      logprob_AUROC: 0.7612\n      logprob_ECE: 0.1289\n      EM_rho: 0.452\n      EM_AUROC: 0.7275\n      EM_ECE: 0.1082\n      voting_conf_rho: 0.4571\n      voting_conf_AUROC: 0.7348\n      voting_conf_ECE: 0.0863\n    conditional:\n      SJ_rho: 0.4505\n      SJ_AUROC: 0.7449\n      SJ_ECE: 0.0826\n      FK_rho: 0.4422\n      FK_AUROC: 0.7401\n      FK_ECE: 0.0835\n      logprob_rho: 0.3242\n      logprob_AUROC: 0.8067\n      logprob_ECE: 0.0921\n      EM_rho: 0.451\n      EM_AUROC: 0.745\n      EM_ECE: 0.0756\n      voting_conf_rho: 0.3962\n      voting_conf_AUROC: 0.7202\n      voting_conf_ECE: 0.0746\n    best_of_n:\n      greedy: 0.9243\n      random_avg: 0.9215\n      sj_best: 0.9243\n      logprob_best: 0.9243\n      voting_conf_best: 0.9243\n      oracle: 0.9488\n    n8_vs_n16_delta:\n      full_SJ_rho_delta: 0.0238\n      full_FK_rho_delta: 0.0201\n      full_logprob_rho_delta: 0.0006\n      full_EM_rho_delta: 0.0214\n      full_voting_conf_rho_delta: 0.0315\n      cond_SJ_rho_delta: 0.0149\n      cond_FK_rho_delta: 0.0112\n      cond_logprob_rho_delta: -0.004\n      cond_EM_rho_delta: 0.0107\n      cond_voting_conf_rho_delta: 0.0219\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T20:41:27.660Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T20:41:27.660Z",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T20:41:27.682Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Quality estimation framing完全成立，correlation-selection gap被视为novel conceptual contribution，paper写作和positioning达到Main标准
核心假设：['Quality estimation (AUROC/ρ for selective prediction) 被接受为first-class contribution，不要求selection improvement', 'Correlation-selection gap被认为是novel finding而非negative result的包装', '2×2 matrix (Qwen×LLaMA × SciERC×CoNLL) + 3-seed robustness被认为generalization充分', '与Nédellec & Xia 2026成功区分：SJ解决其自承的surface matching limitation', 'RE full ρ弱 (~0.21-0.30) 被接受为task-complexity boundary的supporting evidence而非weakness', 'Paper presentation达标：≥3 figures + 35+ refs + 清晰信号分类法 + 对concurrent work的显式对比']
关键指标范围：{'reviewer_overall_arr': [3.5, 4.0], 'acceptance_prob_main': [0.4, 0.6], 'acceptance_prob_findings': [0.75, 0.9], 'perceived_novelty': [3.5, 4.0], 'perceived_soundness': [3.5, 4.5], 'n_major_weaknesses_per_review': [0, 1], 'rebuttal_addressable_pct': [0.85, 1.0], 'focal_auroc_gap_structural_vs_logprob': [0.1, 0.17], 'focal_rho_gap': [0.15, 0.36], 'cross_config_ner_structural_gt_logprob_rate': [1.0, 1.0], 'effective_claim_count_accepted': [3, 3]}
叙事方向：原始3-claim framing完全成立。Claim 1以voting AUROC 0.73 vs logprob 0.56为headline，SJ作为generalizable complement。Claim 2 (correlation-selection gap) 定位为paper最具practical insight的发现——改变practitioners对structured TTS的认知。Claim 3提供explanatory depth。Claims无需调整强度。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: struct_self_consist_ie
focus: 全部 GPU 实验已完成：2×2 矩阵（Qwen×LLaMA × SciERC×CoNLL）+ N=8/N=16 + 3-seed 鲁棒性。5 信号系统比较框架。核心发现：structural > logprob 跨设置一致、correlation-selection gap、task-complexity boundary。论文初稿 experiments/method/introduction 已完成。55 篇文献。关注：能否达到 EMNLP 2026 接收水准？

## paper_framing.md

# Paper Framing — struct_self_consist_ie

> Updated 2026-05-14 post-exp-016 pivot (D019). CRITICAL NARRATIVE CHANGE: best-of-N selection fails on NER (all signals ≤ greedy). Pivot from "TTS improvement" to "confidence estimation + correlation-selection gap".

## Target Venue
- Primary: EMNLP 2026 Main (via ARR May 2026)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May cycle, 2026-05-25

## Core Claims (3 条)

### Claim 1 (Positive — Quality Estimation)
Structural consistency signals (entity voting confidence, soft Jaccard) are the strongest unsupervised quality estimators for entity-level IE, significantly outperforming model confidence (log-probability) and surface agreement (FK, exact-match) at instance-level quality prediction. Entity voting achieves AUROC 0.73 / ρ=0.50 on NER, SJ achieves AUROC 0.67 / ρ=0.36 — both far above logprob (AUROC 0.56 / ρ=0.14). Voting leads SJ on full set; SJ retains unique strength in conditional evaluation (ρ=0.41) and is temperature-robust (Δρ=±0.01).

**Key insight**: The contribution is about a FAMILY of structural consistency signals for QUALITY ESTIMATION (predicting which instances are reliable), not for per-sample selection. SJ and voting_conf both capture entity-across-sample consistency. SJ generalizes to arbitrary structured outputs; voting is simpler.

**Evidence** (SciERC, N=8, T=1.0, unified exp_015 evaluation):
- NER full (n=529): voting ρ=0.502/τ=0.377/AUROC=0.728, SJ ρ=0.357/τ=0.266/AUROC=0.666, FK ρ=0.265/τ=0.203/AUROC=0.624, EM ρ=0.257/τ=0.192/AUROC=0.623, logprob ρ=0.140/τ=0.101/AUROC=0.559
- NER cond (n=501): voting ρ=0.450, SJ ρ=0.412, EM ρ=0.343, FK ρ=0.306, logprob ρ=0.163
- RE full (n=397): voting ρ=0.422/AUROC=0.716, FK ρ=0.253/AUROC=0.631, logprob ρ=0.247/AUROC=0.635, SJ ρ=0.211/AUROC=0.582, EM ρ=0.100/AUROC=0.504
- RE cond (n=296): voting ρ=0.463, SJ ρ=0.368, EM ρ=0.361, FK ρ=0.317, logprob ρ=0.146
- Temperature robustness: SJ Δρ=±0.01 across T=0.7/1.0; FK Δρ=±0.06-0.09 (SJ far more stable)

### Claim 2 (Novel Finding — Correlation-Selection Gap)
Instance-level quality estimation ≠ per-sample selection ability. Despite strong instance-level correlation (ρ≈0.39-0.43), NO unsupervised confidence signal beats greedy decoding for NER best-of-N selection. On RE, only log-probability (+2.4pp over greedy) enables effective selection. The oracle headroom is large (NER +16pp, RE +18pp) but current signals cannot exploit it.

**exp-016 evidence** (SciERC, N=8, T=1.0, n=529):
- NER best-of-N: greedy 0.6094 > logprob 0.6087 > ensemble 0.6043 > sj 0.6042 > voting 0.5959 > random 0.5796 (oracle 0.7692)
- RE best-of-N: logprob 0.3971 > greedy 0.3735 > sj 0.3680 > voting 0.3379 ≈ random 0.3380 (oracle 0.5610)
- Instance-level AUROC: voting_conf 0.700, SJ 0.689, ensemble 0.735 >> logprob 0.591

**Key insight**: Consistency signals are INSTANCE-LEVEL aggregates (one score per instance). They predict which inputs are easy/hard, NOT which sample is best. Log-prob is the only PER-SAMPLE signal and uniquely enables selection on uncertain tasks (RE). This distinction between quality estimation and sample selection is the paper's most practically important finding.

**Implications**: (a) For selective prediction / abstention → use structural consistency (AUROC 0.70+). (b) For best-of-N selection → use logprob, but only on tasks where greedy is suboptimal (RE). (c) For NER, greedy is near-optimal → TTS offers no advantage with current signals.

### Claim 3 (Diagnostic — task-complexity boundary)
The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.

**MVP evidence**: RE full rho_sj=0.234, RE cond rho_sj=0.372 (SJ>FK +11.8pp). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.

**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.

**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):
- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10
- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392
- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.
- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.

## Story Spine

**Problem**: LLM-based structured prediction (IE) increasingly uses multi-sample generation, but practitioners lack guidance on which confidence signals to trust — and for what purpose. Crucially, it is unknown whether signals that predict output quality (instance-level) also enable effective sample selection (per-sample-level).

**Existing approaches & gaps**: Self-consistency in reasoning uses exact-match voting (Wang et al. 2023). USC (Chen et al. 2024) uses LLM-as-judge. For structured prediction, no systematic comparison exists across confidence signal families. More importantly, prior work conflates quality estimation with selection — assuming that high correlation with accuracy translates to effective best-of-N selection.

**Our framing**: We systematically compare five confidence signals across four families for IE: (1) model confidence (log-probability), (2) surface agreement (FK, exact-match), (3) set-aware structural similarity (SJ), (4) entity-level majority voting. We make three findings:
1. Structural consistency (voting_conf/SJ) provides the strongest quality estimation (AUROC 0.73 vs logprob 0.56)
2. However, a **correlation-selection gap** exists: despite strong instance-level correlation, NO signal beats greedy decoding for NER selection; only logprob helps for RE (+2.4pp)
3. All signals degrade on relational tasks due to compound error propagation

**Headline result template**: "On NER, entity voting confidence achieves AUROC 0.73 and ρ=0.50 for quality estimation, significantly outperforming log-probability (AUROC 0.56, ρ=0.14). However, this quality estimation capability does NOT translate to effective best-of-N selection — no signal surpasses greedy decoding on NER (oracle headroom: +16pp). We identify a fundamental correlation-selection gap: instance-level consistency predicts WHICH INPUTS are reliable, not WHICH OUTPUTS are best. On RE, only per-sample log-probability enables selection (+2.4pp), while all consistency signals degrade."

## Anticipated Reviewer Concerns

### R1: "Only one NER dataset — generalization unclear"
- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.
- **Priority**: P0

### R2: "Only one model family (Qwen3-8B)"
- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect
- **Priority**: P0

### R3: "FK is a strawman baseline — what about log-prob, USC, exact-match?"
- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (SJ+voting) >> log-prob >> FK ≈ exact-match. USC discussed in related work (LLM-as-judge, orthogonal approach).
- **Priority**: P0, RESOLVED — results decisive

### R3b: "Voting confidence beats SJ — why use SJ?"
- **Mitigation**: SJ generalizes to arbitrary structured outputs (relations, events, any set-structured prediction). Voting is entity-specific. NER full: voting leads (ρ=0.50 vs 0.36), but SJ retains unique strength in conditional evaluation (ρ=0.41 vs voting 0.45) and is more temperature-robust (Δρ=±0.01). RE cond: SJ ρ=0.37 competitive with voting 0.46. SJ is also more interpretable (pairwise similarity). Paper presents both as complementary instantiations of the structural consistency principle, with voting as practical default and SJ as robust/generalizable option.
- **Priority**: P1 — narrative adjustment needed given exp_015 unified values

### R4: "No actual TTS improvement demonstrated"
- **Status**: ⚠️ CONFIRMED NEGATIVE by exp-016. Best-of-N selection DOES NOT beat greedy on NER with any signal. RE: only logprob +2.4pp over greedy.
- **Mitigation**: Paper PIVOTS to "confidence estimation + correlation-selection gap analysis." exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.
- **Priority**: P0 — narrative pivot required

### R5: "Sample size N=8 may be too small for reliable SJ estimation"
- **Mitigation**: exp-001 (N=16) with multi-seed robustness
- **Priority**: P0

### R6: "Conditional analysis cherry-picks favorable instances"
- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.
- **Priority**: P0 (add sensitivity analysis)

### R7: "Only ρ as evaluation metric"
- **Mitigation**: Add AUROC, calibration plots, Kendall's τ for all experiments
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
- **Status**: ✅ RESOLVED by exp-016. Results:
  - Ensemble AUROC: NER 0.735 (+3.5pp over best single), RE 0.719 (−0.2pp, no improvement)
  - Linear combo: SJ+voting best at α=0.3 (NER ρ=0.489); RE α=0.0 (pure voting)
  - FK negative coefficient in logistic regression → surface agreement is net-negative when structural signals present
  - **Interpretation**: voting_conf captures nearly all discriminative information; ensemble adds marginal value on NER, none on RE. Supports the "structural consistency family" narrative.
- **Priority**: DONE — write into paper with honest interpretation

### R12: "No supervised upper bound / reward model comparison" (Dream 2)
- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Full reward model training out of scope for this paper — discuss as future work.
- **Priority**: P1 (partially addressed by exp-016 ensemble)

### R13: "Headroom capture rate low (37% NER, 11% RE)" (Dream 2)
- **Mitigation**: Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline.
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

Risk assessment (post-Dream 2, all tiers 3/6):
- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.
- **Data-dependent risks (观察中)**: SJ vs LOGPROB ranking may be dataset-dependent (Dream imagined this; awaiting exp-002/003 real data). If confirmed → reframe as "complementary signals" rather than "SJ dominates."
- **Confirmed strength**: SJ >> LOGPROB on SciERC (AUROC 0.70 vs 0.59). Structural consistency family consistently top on existing data.
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
    auroc_best:
      SJ:
        conll_ner: 0.8008
        scierc_ner_avg: 0.7328
        scierc_re_avg: 0.6788
        llama_ner_avg: 0.7029
        llama_re_avg: 0.7144
        wnut_ner: 0.5844
      FK:
        conll_ner: 0.7741
        scierc_ner_avg: 0.6172
        scierc_re_avg: 0.5939
        llama_ner_avg: 0.6484
        llama_re_avg: 0.6778
        wnut_ner: 0.5752
      logprob:
        conll_ner: 0.7532
        scierc_ner_avg: 0.5918
        scierc_re_avg: 0.5849
        llama_ner_avg: 0.5584
        llama_re_avg: 0.654
        wnut_ner: 0.358
      EM:
        conll_ner: 0.8156
        scierc_ner_avg: 0.7873
        scierc_re_avg: 0.715
        llama_ner_avg: 0.7533
        llama_re_avg: 0.7557
        wnut_ner: 0.5745
      voting_conf:
        conll_ner: 0.7889
        scierc_ner_avg: 0.7367
        scierc_re_avg: 0.7195
        llama_ner_avg: 0.7232
        llama_re_avg: 0.7509
        wnut_ner: 0.8692
    loo_sj:
      max_delta_rho: 0.000305
      all_no_circularity: true
    n_datasets: 10
    n_subtask_combos: 18
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
  "promptId": "8bbb1d01-9250-4258-9b26-67afa564a41a",
  "type": "user",
  "uuid": "f2983d82-7682-45d8-8b3f-8ec0495de159",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T20:41:27.680Z_

```json
{
  "parentUuid": "f2983d82-7682-45d8-8b3f-8ec0495de159",
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
  "uuid": "231d03fa-63e7-4061-9951-2ebd78ffb396",
  "timestamp": "2026-05-14T20:41:27.680Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T20:41:27.680Z_

```json
{
  "parentUuid": "231d03fa-63e7-4061-9951-2ebd78ffb396",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8ae28ca3-75f9-4619-b66e-8847e1bdbd2b",
  "timestamp": "2026-05-14T20:41:27.680Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Quality estimation framing完全成立，correlation-selection gap被视为novel conceptual contribution，paper写作和positioning达到Main标准 核心假设：['Quality estimation (AUROC/ρ for…",
  "leafUuid": "8ae28ca3-75f9-4619-b66e-8847e1bdbd2b",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Structural consistency signals for IE quality estimation and correlation-selection gap analysis",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f"
}
```

---

### Assistant

_source line 8 · 2026-05-14T20:44:06.093Z_

<details><summary>Logged reasoning block</summary>

````text
The user wants me to generate detailed predicted data for each "planned" experiment in the experiment_plan, under the "best" tier definition. Let me identify which experiments are still "planned":

1. **exp-011** (ner_ood_robustness) - status: planned
2. **exp-017** (ner_llama_conll) - status: planned

Wait, let me re-read. The user says "对 experiment_plan 中每个 planned 实验展开详细数据". Let me check which experiments have status "planned":


I'm seeing that exp-011 and exp-017 are marked as planned in the experiment_plan, though exp-017 has extensive registry entries showing it's already been completed. The user is asking me to generate predicted data for these planned experiments under the "best" tier definition. I see that exp-011 and exp-017 are the only ones marked as planned, though exp-017 actually has registry data already. The user wants me to generate predicted results for these planned experiments under the "best" tier scenario they defined, with specific assumptions about performance ranges and key metrics. Let me work through what exp-011's results would look like under those best-case conditions. tests NER consistency signal on OOD instances (cross-domain transfer). It depends on exp-003 (WNUT-17) which was orphaned/failed.

For exp-017 (ner_llama_conll): LLaMA-3.1-8B on CoNLL-2003. This actually has real data in the registry already.

I think the task is about predicting results for planned experiments under the "best" tier scenario for the paper review simulation. The user wants detailed predicted experimental outcomes.

Since exp-017 has real data already but is listed as "planned" in the experiment plan, and exp-011 is truly planned with no data, I need to predict what these experiments would show under the "best" tier. For exp-017, the real data exists and aligns well with the "best" tier. For exp-011, I need to imagine results.

Now I'm reviewing the "best" tier definition more carefully to understand what metrics and thresholds define success: the quality estimation framing needs to work fully, the correlation-selection gap should be novel, the 2×2 model matrix with 3-seed robustness is sufficient, and the paper needs strong presentation with figures and references. The key metrics I'm tracking are the focal AUROC gap between structural and logprob approaches, the focal rho gap, and cross-domain performance.

For exp-011 on OOD robustness, this was originally dependent on exp-003 which failed, but under the "best" tier definition, the 2×2 matrix alone might be considered sufficient without it. However, if I'm predicting results, WNUT-17 historically showed weak structural performance, so this would likely demonstrate the task-complexity boundary that the paper accepts as evidence.

For exp-017 with LLaMA on CoNLL, the real data already exists in the registry, so I can work with actual results rather than predictions. I'm looking at exp-011 and realizing that the WNUT-17 results already showed this approach struggles with OOD data, so even under the best-case interpretation, I should predict modest performance rather than overstating the generalization. For exp-017, I have real registry data showing strong structural signal correlation that aligns well with the in-domain results, so that's straightforward to include. Now I need to draft the YAML with honest predictions that acknowledge both the successes and the limitations. Looking at the actual experimental setup, exp-011 tests cross-domain transfer by applying a model trained on one dataset (like SciERC) to another domain entirely. The structural consistency signal should degrade under this OOD shift, but since it measures agreement rather than absolute quality, it might retain some robustness compared to surface-level signals. For the best-tier prediction, I'd expect structural signals to remain positive but weaker (ρ around 0.15-0.25), while the relative ordering of signal types could become less stable across domains.

Now I'm compiling the final YAML output with predictions grounded in the actual experimental registry data for exp-017 and realistic degradation patterns for exp-011. given the existing evidence.

Let me now write the output:

```yaml
tier: best
narrative_guidance: "原始3-claim framing完全成立。exp-017确认cross-model×cross-dataset一致性（LLaMA CoNLL SJ ρ=0.43 ≈ Qwen CoNLL 0.44），完成2×2矩阵。exp-011作为P2 OOD实验提供Claim 3的domain-shift boundary证据，但不影响核心claims。论文可以在Limitations中acknowledge OOD degradation，同时在Discussion中将其定位为future work direction。"
imagined_experiments:
  - name: "ner_ood_robustness"
    plan_id: "exp-011"
    description: "使用SciERC fine-tuned Qwen3-8B模型在WNUT-17 test set上做zero-shot NER inference，评估所有5种confidence signals在OOD条件下的quality estimation性能。"
    expected_results:
      n_instances: 1287
      n_valid: 689
      n_conditional: 412
      gold_empty_filtered: 598
      sample_f1_pct_zero: 52.3
      greedy_f1: 0.198
      oracle_f1: 0.347
      oracle_headroom: 0.149
      full:
        SJ_rho: 0.142
        FK_rho: 0.118
        logprob_rho: 0.097
        EM_rho: 0.103
        voting_conf_rho: 0.159

The OOD experiment shows notably weaker correlation signals across all confidence metrics compared to in-domain results, with voting confidence performing best at 0.159 but still substantially degraded from the main findings.
```
Looking at the OOD robustness results, there's a clear pattern emerging. The absolute performance drops dramatically when the model encounters the social media domain—greedy F1 plummets from 0.61 to 0.20—which makes sense given the mismatch between scientific entities and social media entity types. But what's striking is that despite this performance collapse, the relative ranking of confidence signals stays consistent: structural methods like voting confidence outperform surface-level approaches, which in turn beat logprob. This suggests the structural consistency advantage isn't just an artifact of the training data, but reflects something fundamental about how entity-level agreement captures information.
```
Examining the OOD performance metrics...
```
voting_conf shows the strongest correlation improvement (ρ: 0.159→0.267), while SJ, FK, EM, and logprob all demonstrate consistent gains when filtering out zero-output instances. The AUROC scores follow a similar pattern—conditional filtering pushes all signals toward better discrimination, with voting_conf reaching 0.658 and SJ at 0.643. I'm also looking at a bar chart that visualizes how these five signals degrade in parallel when moving from in-domain to out-of-domain settings.

This experiment is secondary priority and won't affect acceptance, but it serves two purposes: it demonstrates that the relative ordering of signals (structural > surface > logprob) holds across domains, supporting the generalizability claim, and it provides evidence that domain mismatch is a second degradation factor alongside task complexity. The absolute correlation values are weak though (full ρ < 0.20), so this belongs in the appendix rather than as a headline result. I'm also starting to look at another experiment involving LLaMA fine-tuned on CoNLL-2003.

Now I'm examining the NER inference results with N=8 and N=16 across multiple seeds to complete the cross-model and cross-dataset comparison matrix. Looking at the expected metrics across different correlation and AUROC measures for the N=8 configuration.

Continuing through the N=16 seed 42 results... Looking at the performance metrics across different seeds and selection methods, the structural consistency holds up well with the Spearman correlation staying around 0.463, and the best-of-n selection strategies all cluster tightly between 0.924-0.927 compared to the oracle at 0.949. The analysis suggests that exp-017 fills a critical gap in the 2×2 matrix comparison, with the LLaMA and Qwen results showing nearly identical performance on the NER task, validating the structural consistency across different model families.

The consistency estimation appears to be model-agnostic since two independent models produce nearly identical correlation patterns on the same dataset, ruling out model-specific artifacts. On the CoNLL dataset where greedy performance is already quite high at 0.927, the oracle only provides marginal improvement of 0.018, which explains why best-of-n selection shows minimal gains—all the signal clusters within ±0.003 of greedy. Yet the quality estimation still works effectively with a structural AUROC of 0.704, demonstrating that consistency signals can distinguish between good and mediocre outputs even on easier datasets. The logprob AUROC of 0.761 on CoNLL is unusually high due to better calibration from the high baseline performance, though its correlation remains notably lower than the structural approach.

Structural signals consistently outperform logprob across all 18 configurations tested with different seeds and sample sizes, with the structural approach winning in every single case. The robustness analysis with N=16 and 3 seeds shows extremely tight variance around the mean, confirming the stability of these results. Scaling from N=8 to N=16 provides a consistent improvement of about 0.033 for the structural approach, matching the pattern observed in other datasets.

Now I'm looking at the cross-model and cross-dataset performance metrics, comparing how different model-dataset combinations perform with structural signals versus voting and logprob approaches. Now I'm looking at the robustness metrics across three different random seeds for the LLaMA and CoNLL configuration, with consistency shown in the mean and standard deviation—the Spearman rho values stay tight around 0.463 with minimal variation. I'm also preparing visualizations including a heatmap showing the correlation strengths across model and dataset combinations with improvements over the logprob baseline, plus a stability plot demonstrating how consistent the structural signals are across the different seeds.

The core finding from this experiment is that structural signals consistently outperform the logprob baseline across all four model-dataset combinations with a gap of 0.12-0.22, and this pattern holds remarkably well across different models on the same dataset—the Qwen and LLaMA results differ by less than 0.01. The tight standard deviation of 0.008 across three seeds shows the results aren't driven by random variation, which directly addresses concerns about single-model validation and cross-model generalization. With 12 independent configurations showing this consistent pattern, the evidence for generalization is strong enough without needing larger models or additional datasets. I'm pulling the results for the other random seeds and calculating the mean and standard deviation across all three runs to get a robust estimate of the SJ_rho performance. Now I'm pulling in the actual experimental results—using exp-017 data for one condition and realistic estimates for exp-011. For the Qwen model on CoNLL, I'll reference the metrics from exp-002, and for the SciERC dataset I have the results from exp-015. Let me gather the LLaMA results as well to complete the comparison.

Looking at the LLaMA SciERC data from exp-007, I notice the voting confidence metric isn't directly available for the N=8 condition, though I can see it was recorded in the N=16 variant. I'll work with what's available in the baseline metrics and note where data points are missing. The user is asking for predictions on the planned experiments, so even though exp-017 has real data in the registry, I should treat this as a forecasting exercise based on the experimental framework.

For exp-011, I need to ground my predictions in the existing WNUT-17 results, but adjust downward since this tests out-of-domain transfer rather than in-domain performance. The cross-domain transfer scenario would naturally show degradation compared to the orphaned exp-003 baseline. with a matched fine-tuned model were already weak: SJ rho 0.082 full, 0.275 cond. An OOD transfer would likely be even worse.

But under the "best" tier, this experiment is P2 and not critical. The key question is: what would it show?

Given:
- WNUT-17 with matched model: SJ ρ=0.082 (full), 0.275 (cond), 53.7% F1=0
- SciERC with matched model: SJ ρ=0.357-0.43
- CoNLL with matched model: SJ ρ=0.44

OOD transfer (SciERC model on WNUT-17): probably even worse than matched WNUT-17 model. Maybe:
- Greedy F1: ~0.10-0.15 (entity types don't match)
- SJ ρ full: ~0.05
- Very high F1=0 rate: >60%

This would essentially be useless. Since the experiment depends on the orphaned exp-003 and sits at P2 priority, it likely wouldn't run under the best tier—probably just mentioned in limitations. But I should still give honest predictions for what was asked. Let me clarify what "OOD" actually means here: the description mentions cross-domain transfer, which could mean applying the WNUT-17 fine-tuned model to SciERC data or vice versa, or it could refer to naturally OOD instances within a test set.

I'll assume the most straightforward interpretation: evaluating a SciERC fine-tuned model on WNUT-17 test data. Now I need to produce the YAML output with proper rationales, using actual numbers from the registry rather than estimates.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ae28ca3-75f9-4619-b66e-8847e1bdbd2b",
  "isSidechain": false,
  "requestId": "req_011Cb37JkNsgMAzMrVJxH7BM",
  "type": "assistant",
  "uuid": "751c06a1-3052-4083-900d-4915f06386ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9pAEBDSUPKPjV7nf94wsb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 52410,
      "output_tokens": 13731,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13731,
          "cache_read_input_tokens": 52410,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-14T20:45:35.979Z_

```yaml
tier: best
narrative_guidance: >
  best档叙事中，2×2矩阵(Qwen×LLaMA × SciERC×CoNLL)已充分，exp-017是最后一块拼图且结果
  高度positive。exp-011作为P2 OOD实验提供Claim 3的domain-shift boundary evidence，预期弱但
  不影响核心acceptance。Reviewer接受informal-domain degradation作为acknowledged limitation。

imagined_experiments:
  - name: "ner_ood_robustness"
    plan_id: "exp-011"
    description: >
      SciERC fine-tuned Qwen3-8B在WNUT-17 test set上做zero-shot NER inference
      (N=8, T=1.0, seed=42)。Entity type schema不匹配（科学实体→social media实体），
      测试structural consistency signals在domain shift下的robustness。
    expected_results:
      n_instances: 1287
      n_gold_empty_filtered: 598
      n_valid: 689
      n_conditional: 378
      sample_f1_pct_zero: 61.4
      greedy_f1: 0.143
      oracle_f1: 0.302
      oracle_headroom: 0.159
      full:
        SJ_rho: 0.078
        FK_rho: 0.064
        logprob_rho: -0.031
        EM_rho: 0.051
        voting_conf_rho: 0.093
        SJ_AUROC: 0.562
        FK_AUROC: 0.548
        logprob_AUROC: 0.487
        EM_AUROC: 0.539
        voting_conf_AUROC: 0.574
        SJ_tau: 0.054
        FK_tau: 0.044
        logprob_tau: -0.021
      conditional:
        SJ_rho: 0.198
        FK_rho: 0.152
        logprob_rho: 0.117
        EM_rho: 0.141
        voting_conf_rho: 0.224
        SJ_AUROC: 0.618
        FK_AUROC: 0.594
        logprob_AUROC: 0.573
        EM_AUROC: 0.587
        voting_conf_AUROC: 0.631
      structural_beats_logprob_full: true
      structural_beats_logprob_cond: true
      relative_ordering_preserved: true
      selection_f1:
        greedy: 0.143
        sj: 0.131
        logprob: 0.128
        voting_conf: 0.134
        random: 0.119
        oracle: 0.302
    result_rationale: >
      OOD实验的核心逻辑：SciERC模型在WNUT-17上的entity schema完全不匹配（Task/Method/Material/Metric
      vs person/location/corporation/creative-work），导致greedy F1从in-domain 0.66暴跌至0.14，
      61%+实例产生F1=0。但在best档下，关键观察是：

      (1) 绝对ρ极弱（full SJ 0.078）但并非zero——模型虽然不认识target entities，当它偶尔
      做对时，structural consistency仍能区分好坏。这与exp-003 matched-model结果（SJ ρ=0.082）
      高度一致，说明WNUT-17本身就是一个consistency信号的hard domain。

      (2) 信号相对排序保持不变：voting_conf > SJ > FK > EM > logprob。logprob甚至变负
      （ρ=-0.031），因为OOD下模型calibration完全失效——它对不认识的entities给出confidently
      wrong的logprob。structural signals因为measure inter-sample agreement而非model confidence，
      在calibration崩溃时仍然informative。

      (3) 条件集（排除F1=0）提升到SJ 0.198/voting 0.224——pattern与所有in-domain实验一致，
      但绝对值仍弱。

      (4) logprob反转为负值是一个有趣的finding：支撑Claim 1的narrative——在model calibration
      不可靠的场景（OOD、closed-source APIs），structural signals是唯一可用的quality estimator。

      (5) Best档reviewer视此为Limitations中的known boundary。论文一句话mention："On
      cross-domain OOD transfer, all signals degrade substantially but structural signals
      retain relative advantage"即可。不需要作为main result。
    tables:
      - name: "Table A.X (Appendix): OOD Quality Estimation — SciERC→WNUT-17"
        columns: [signal, ρ_full, ρ_cond, AUROC_full, AUROC_cond]
        rows:
          - [voting_conf, 0.093, 0.224, 0.574, 0.631]
          - [SJ, 0.078, 0.198, 0.562, 0.618]
          - [FK, 0.064, 0.152, 0.548, 0.594]
          - [EM, 0.051, 0.141, 0.539, 0.587]
          - [logprob, -0.031, 0.117, 0.487, 0.573]
    figures_description:
      - >
        Appendix figure: grouped bar chart with 5 signals × 2 conditions (in-domain SciERC
        vs OOD WNUT-17)。ρ值从左到右下降但柱形颜色排序不变。Logprob柱形在OOD条件下跌入
        negative区域用红色标注，visual emphasis on calibration failure。
    analysis: >
      此实验为P2，在best档叙事中属于Limitations/Discussion material。核心价值是两点：
      (a) relative ordering preservation证明structural consistency不是dataset-specific artifact；
      (b) logprob负相关提供了一个clean argument for structural signals在uncalibrated scenarios
      下的unique value。但绝对效果太弱（全部ρ<0.25），不适合写入main results。建议放Appendix
      table + Limitations段落1-2句。在best档下reviewer不会因为缺少更多OOD experiments而reject，
      因为2×2 in-domain矩阵已充分。

  - name: "ner_llama_conll"
    plan_id: "exp-017"
    description: >
      LLaMA-3.1-8B fine-tuned on CoNLL-2003 (LoRA), NER inference N=8 T=1.0 seed=42
      + N=16 3-seed (42/123/456) robustness。完成2×2 cross-model×cross-dataset矩阵的
      第四格(LLaMA×CoNLL)。
    expected_results:
      dataset: CoNLL-2003
      model: LLaMA-3.1-8B-Instruct
      n_instances: 3453
      n_valid: 2756
      n_conditional: 2642
      N8:
        greedy_f1: 0.927
        oracle_f1: 0.944
        oracle_headroom: 0.018
        full:
          SJ_rho: 0.431
          FK_rho: 0.428
          logprob_rho: 0.307
          EM_rho: 0.431
          voting_conf_rho: 0.426
          SJ_AUROC: 0.704
          FK_AUROC: 0.703
          logprob_AUROC: 0.761
          EM_AUROC: 0.705
          voting_conf_AUROC: 0.709
          SJ_ECE: 0.114
          voting_conf_ECE: 0.095
        conditional:
          SJ_rho: 0.436
          FK_rho: 0.431
          logprob_rho: 0.328
          EM_rho: 0.440
          voting_conf_rho: 0.374
          SJ_AUROC: 0.723
          logprob_AUROC: 0.810
        SJ_vs_logprob_delta_rho: 0.124
        structural_beats_logprob: true
      N16_seed42:
        full:
          SJ_rho: 0.464
          FK_rho: 0.457
          logprob_rho: 0.306
          EM_rho: 0.461
          voting_conf_rho: 0.455
          SJ_AUROC: 0.739
        conditional:
          SJ_rho: 0.460
          FK_rho: 0.452
          logprob_rho: 0.319
        best_of_n:
          greedy: 0.924
          sj_best: 0.926
          logprob_best: 0.925
          voting_conf_best: 0.927
          oracle: 0.949
        n8_to_n16_SJ_delta: 0.033
      N16_seed123:
        full:
          SJ_rho: 0.470
          FK_rho: 0.459
          logprob_rho: 0.316
          EM_rho: 0.468
          voting_conf_rho: 0.461
          SJ_AUROC: 0.740
        conditional:
          SJ_rho: 0.471
          logprob_rho: 0.331
        best_of_n:
          greedy: 0.924
          sj_best: 0.925
          logprob_best: 0.925
          voting_conf_best: 0.926
          oracle: 0.949
      N16_seed456:
        full:
          SJ_rho: 0.455
          FK_rho: 0.448
          logprob_rho: 0.308
          EM_rho: 0.452
          voting_conf_rho: 0.457
          SJ_AUROC: 0.729
        conditional:
          SJ_rho: 0.451
          logprob_rho: 0.324
        best_of_n:
          greedy: 0.924
          sj_best: 0.924
          logprob_best: 0.924
          voting_conf_best: 0.924
          oracle: 0.949
      three_seed_aggregated:
        SJ_rho_mean: 0.463
        SJ_rho_std: 0.008
        FK_rho_mean: 0.455
        FK_rho_std: 0.006
        logprob_rho_mean: 0.310
        logprob_rho_std: 0.005
        EM_rho_mean: 0.460
        EM_rho_std: 0.008
        voting_conf_rho_mean: 0.458
        voting_conf_rho_std: 0.003
        structural_beats_logprob_rate: 1.0
        SJ_AUROC_mean: 0.736
        SJ_AUROC_std: 0.006
      cross_model_consistency:
        qwen_conll_SJ_rho: 0.436
        llama_conll_SJ_rho: 0.431
        delta: 0.005
        qwen_scierc_SJ_rho: 0.357
        llama_scierc_SJ_rho: 0.363
        delta_scierc: -0.006
    result_rationale: >
      exp-017在best档下是decisive positive result，理由如下：

      (1) Cross-model一致性极高：LLaMA CoNLL SJ ρ=0.431 vs Qwen CoNLL ρ=0.436 (Δ=0.005)。
      两个architecturally不同的8B模型（Qwen3 vs LLaMA-3.1）在同一数据集上产生几乎
      相同的consistency-accuracy correlation。这不是trivial的——Qwen和LLaMA的tokenizer、
      pre-training data、architecture细节完全不同，但structural consistency作为quality
      estimator的有效性是一个关于output space agreement的property，与model internals无关。

      (2) Cross-dataset一致性：LLaMA在SciERC上SJ ρ=0.363，在CoNLL上0.431。Qwen在SciERC上
      0.357，CoNLL上0.436。两个模型都展示相同的dataset effect（CoNLL > SciERC），进一步
      确认consistency signal strength是task property而非model artifact。

      (3) logprob在CoNLL上的AUROC(0.761)高于structural signals(0.704)——这是CoNLL特殊性造成的：
      greedy F1=0.927极高，logprob calibration在near-perfect performance regime下更准确。
      但ρ仍然显著低于structural（0.307 vs 0.431，Δ=0.124），因为ρ测量的是rank discrimination
      而非threshold classification。这个AUROC vs ρ的分离恰好为论文的metrics discussion提供
      了一个自然的例子：不同metrics capture不同aspects of quality estimation。

      (4) 3-seed robustness (SJ ρ std=0.008) 是最tight的across所有configurations。CoNLL的
      large test set (n=2756)提供了high statistical power，variance自然低。这让reviewer对
      "results stable across random seeds"的claim完全信服。

      (5) N=8→N=16提升(SJ +0.033)在所有3 seeds上一致，但absolute gain modest——因为N=8已经
      near-saturation on CoNLL NER。这与SciERC pattern一致（NER saturates earlier than RE），
      支撑Claim 3的task-complexity boundary narrative。

      (6) Best-of-N selection在CoNLL上trivial（所有signals在greedy±0.003内，oracle headroom
      仅0.018），reinforces Claim 2：当greedy已near-optimal时，selection无headroom可exploit。
      这是correlation-selection gap的complementary evidence——gap不仅存在于consistency signals
      fail to select的场景，也存在于所有signals（including logprob）都无法超越greedy的场景。
    tables:
      - name: "Table 2: 2×2 Cross-Model × Cross-Dataset NER Quality Estimation (N=8, ρ on full set)"
        columns: [Configuration, SJ, voting_conf, FK, EM, logprob, n]
        rows:
          - ["Qwen × SciERC", 0.357, 0.502, 0.265, 0.257, 0.140, 529]
          - ["Qwen × CoNLL", 0.436, 0.424, 0.400, 0.451, 0.316, 2756]
          - ["LLaMA × SciERC", 0.363, "—", 0.327, "—", 0.183, 529]
          - ["LLaMA × CoNLL", 0.431, 0.426, 0.428, 0.431, 0.307, 2756]
        note: >
          所有4格structural > logprob。Cross-model delta ≤ 0.006 on same dataset。
      - name: "Table 3: AUROC across 2×2 matrix (N=8)"
        columns: [Configuration, SJ, voting_conf, logprob, best_single]
        rows:
          - ["Qwen × SciERC", 0.666, 0.728, 0.559, "voting 0.728"]
          - ["Qwen × CoNLL", 0.801, 0.789, 0.753, "SJ 0.801"]
          - ["LLaMA × SciERC", 0.702, 0.718, 0.558, "voting 0.718"]
          - ["LLaMA × CoNLL", 0.704, 0.709, 0.761, "logprob 0.761"]
        note: >
          logprob仅在CoNLL AUROC上competitive（high-baseline regime）。ρ-based ranking
          一致favor structural signals。
      - name: "Table 4: LLaMA × CoNLL N=16 3-Seed Robustness"
        columns: [Metric, seed42, seed123, seed456, "mean±std"]
        rows:
          - ["SJ ρ", 0.464, 0.470, 0.455, "0.463±0.008"]
          - ["FK ρ", 0.457, 0.459, 0.448, "0.455±0.006"]
          - ["logprob ρ", 0.306, 0.316, 0.308, "0.310±0.005"]
          - ["voting_conf ρ", 0.455, 0.461, 0.457, "0.458±0.003"]
          - ["SJ AUROC", 0.739, 0.740, 0.729, "0.736±0.006"]
    figures_description:
      - >
        Figure 2 (论文正文): 2×2 heatmap，行=model (Qwen/LLaMA)，列=dataset (SciERC/CoNLL)。
        每格显示SJ ρ值，颜色深浅编码0.30-0.47范围。格内小字标注Δ vs logprob。Visual message：
        四格一致呈深色(structural strong)，logprob delta一致为正。
      - >
        Figure 3 (论文正文): LLaMA×CoNLL 3-seed error bar plot。X轴=5种signals，Y轴=ρ。
        每个signal 3个点+mean bar+95% CI whisker。Structural signals (SJ/FK/EM/voting)
        cluster在0.43-0.47，logprob isolated在0.31。CI不重叠→statistically significant gap。
      - >
        Figure A.Y (Appendix): N=8 vs N=16 delta ρ bar chart for LLaMA×CoNLL。
        Structural signals gain +0.03，logprob flat (−0.001 to +0.009)。Shows structural
        signals benefit more from additional samples。
    analysis: >
      exp-017在best档下完成三个关键narrative objectives：

      (a) 2×2矩阵完整性：4格全部structural > logprob (cross_config_ner_structural_gt_logprob_rate
      = 1.0)，直接满足best档指标。Cross-model delta < 0.01证明model-agnostic。

      (b) CoNLL的large n (2756)提供了SciERC(529)不具备的statistical power。Bootstrap CI更紧，
      Fisher z-test的power更高。Reviewer trust结果的confidence level显著提升。

      (c) 3-seed std=0.008是所有configurations中最低的——seed instability不是concern。

      在best档的paper presentation中，此实验应占据main results的~40%篇幅：Table 2 (2×2 matrix
      with ρ)是论文的central evidence table，Figure 2 (heatmap)是最impactful的visual。
      3-seed robustness放Table 4或Appendix。Best-of-N的trivial结果（greedy±0.003）用一句话
      mention即可，不需要单独table——它reinforces Claim 2 but isn't surprising on CoNLL。

      logprob的AUROC anomaly (0.761 > SJ 0.704 on CoNLL)需要在paper中explicitly discuss：
      在near-perfect baseline regime下logprob是well-calibrated threshold classifier，但ρ
      reveals它的ranking ability仍然inferior。这个AUROC-ρ divergence本身是一个interesting
      methodological point，支撑论文使用multiple metrics的design choice。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "751c06a1-3052-4083-900d-4915f06386ba",
  "isSidechain": false,
  "requestId": "req_011Cb37JkNsgMAzMrVJxH7BM",
  "type": "assistant",
  "uuid": "f365ddbc-187a-43d8-b454-5b6052dbee66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9pAEBDSUPKPjV7nf94wsb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 52410,
      "output_tokens": 13731,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13731,
          "cache_read_input_tokens": 52410,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Quality estimation framing完全成立，correlation-selection gap被视为novel conceptual contribution，paper写作和positioning达到Main标准 核心假设：['Quality estimation (AUROC/ρ for…",
  "leafUuid": "f365ddbc-187a-43d8-b454-5b6052dbee66",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Structural consistency signals for IE quality estimation and correlation-selection gap analysis",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Quality estimation framing完全成立，correlation-selection gap被视为novel conceptual contribution，paper写作和positioning达到Main标准 核心假设：['Quality estimation (AUROC/ρ for…",
  "leafUuid": "f365ddbc-187a-43d8-b454-5b6052dbee66",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Structural consistency signals for IE quality estimation and correlation-selection gap analysis",
  "sessionId": "4ff1286a-4c71-4d0e-a313-574e255d923f"
}
```

---
