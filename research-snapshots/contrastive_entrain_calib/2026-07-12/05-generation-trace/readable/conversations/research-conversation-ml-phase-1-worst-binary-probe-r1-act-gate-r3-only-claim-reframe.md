# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Binary probe R1 未过 ACT gate 或 R3-only 持平/反超，核心方法 claim 不成立，需全面 reframe 核心假设

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/6856be68-58ac-4600-a6df-a51f6531fd0a.jsonl`
- **Structured JSON:** [`7ca93e7389441ca95700.json`](../../sessions/7c/7ca93e7389441ca95700.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T20:45:41.764Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T20:45:41.764Z",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Binary probe R1 未过 ACT gate 或 R3-only 持平/反超，核心方法 claim 不成立，需全面 reframe\n核心假设：['discriminability ≠ reward utility 的 gap 对 probe binarization 同样成立——分类准确 ≠ 有效 reward shaping', 'exp-008v3 训练不稳定 (部分 mode collapse) 或 probe R1 产生 reward hacking', 'R3-only 出乎意料地强，或 probe+R3 组合产生 reward conflict 导致训练退化', 'd_syc 方向在较长训练中漂移加剧 (cosine < 0.80) 或判别力跌破 0.75', 'R1-R3 disagreement < 3%，representation-level 信号实际无增量信息']\n关键指标范围：{'exp_008v3_SYCONScore': [0.1, 0.3], 'exp_003_SYCONScore': [0.28, 0.38], 'delta_probe_vs_r3only': [-0.2, 0.0], 'delta_probe_vs_ACT': [-0.2, 0.0], 'exp_008v3_ToF': [0.06, 0.18], 'exp_008v3_NoF': [0.55, 0.8], 'direction_AUROC_endtrain': [0.68, 0.77], 'r1_r3_disagreement_rate': [0.0, 0.03]}\n叙事方向：方法 claim 全部放弃。Reframe 为系统性 negative result + insight paper: \"When and Why Representation-Level Discriminability Fails as RL Reward.\" 核心贡献变为：(1) 首次系统证明 representation discriminability (AUROC 0.82) 不等价于 reward utility——即使通过 binarization 也无法弥合 gap (5 种 R1 变体全部失败的完整证据链)；(2) 结构性根因分析——warranted revision 与 sycophantic capitulation 在激活空间中的几何关系使得任何基于 d_syc 的单一方向 reward 在 GRPO 框架下不可避免地产生 conflation；(3) 对 RepE→RL pipeline 的 actionable 负面指南——明确哪类 representation signal 不适合直接用作 RL reward。补充实验：跨模型 (Llama-3-8B) 复现 gap 证明结构性而非模型特异；理论分析连接 reward shaping 文献。仍投 EMNLP main (EMNLP 重视 rigorous negative results)，目标 score 3.0-3.5。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contrastive_entrain_calib\nfocus: D029 narrative pivot: discriminability ≠ reward utility. Cosine R1 fails structurally (4 experiments), binary probe R1 resolves via binarization. Paper arc: discovery→failure→understanding→solution. Core data pending (exp-008v3 SYCONScore must > 0.301).\n\n## paper_framing.md\n\n# Paper Framing — contrastive_entrain_calib\n\n## Target Venue\n- Primary: **EMNLP 2026** via ARR May 2026 cycle\n- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)\n- Commitment Deadline: **August 2, 2026**\n- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改\n- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\n\n## Core Claims (3 条, 可证伪)\n\n1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.\n   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\n   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.\n   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.\n   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).\n\n2. **DC-GRPO effectiveness via binarized direction reward (D029 pivot)**: Direction information (d_syc) is effective as GRPO reward ONLY when binarized through a probe classifier. Continuous cosine projection fails structurally — the paper presents a complete discovery→failure→understanding→solution arc.\n   - *Evidence needed*: SYCONScore (harmonic mean of ToF + NoF) on D027 unified eval, compared to R3-only (exp-003) and ACT baselines (exp-004)\n   - *Pass criterion*: exp-008v3 SYCONScore > 0.301 (ACT bar from exp-004 ckpt-8000)\n   - *Narrative arc (D029)*:\n     - **Discovery**: d_syc linearly separates sycophancy (AUROC 0.82, Claim 1) — direction information EXISTS\n     - **Failure**: 4 cosine R1 attempts all fail — exp-002 (tanh gate), exp-002v2 (raw cosine, R1≈0), exp002v2-recalib (mode collapse, entropy 0.069), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)\n     - **Understanding**: Per-strength analysis reveals structural cause — d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. High-evidence samples (where model SHOULD revise) project most negatively onto d_syc\n     - **Solution**: Binary probe resolves ambiguity — binarization via logistic regression on d_syc features maps continuous geometry to {sycophantic, genuine} decision. exp-008v3 R1 mean +0.72 (step 2140), consistently positive, upward trend\n   - *Key insight*: Direction information exists (AUROC 0.82) but requires binarization to become effective GRPO reward. The gap between discriminability and reward utility is the paper's core finding.\n   - *Fallback (D029)*: If exp-008v3 SYCONScore ≤ 0.301, paper downgrades to \"direction signal characterization\" (analysis paper targeting Findings, score 3.0-3.5)\n\n3. **Representation-level diagnostic value** (analysis subsection, not formal contribution): R1-R3 disagreement analysis characterizes when and whether directional projection rewards detect sycophantic internal reasoning that behavioral rewards miss.\n   - *Evidence needed*: R1-R3 disagreement frequency analysis, qualitative examples if > 5%\n   - *Framing*: Empirical characterization of representation-level signal utility, reported honestly regardless of effect size. Not listed as a top-level contribution bullet.\n\n## Story Spine\n\n**Problem**: LLMs face a \"double-bind\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \"the user is right, I should revise\" from \"the user is pressuring me, I should resist.\"\n\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\"Pressure, What Pressure?\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\n\n**Our framing**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We build on this foundation: d_syc is a specific application of RepE-style directional decomposition to multi-turn sycophancy. Our key finding is that d_syc successfully discriminates sycophancy (AUROC 0.82), but continuous geometric projections (cosine similarity) fail as GRPO rewards — the signal conflates legitimate revision with sycophantic capitulation. Binarization through a probe classifier trained on d_syc features resolves this: R1 = probe(h; d_syc) ∈ {0,1}, providing a clean, high-signal reward. The novelty is not the direction extraction itself, but the systematic investigation of HOW directional information should enter GRPO training — revealing that discriminability ≠ reward utility, and that binarization is necessary. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.\n\n**Method (D029 pivot)**: R1 = probe(h; d_syc) ∈ {0,1}, where probe is a logistic regression classifier trained on hidden-state projections onto d_syc. Binary output provides clean reward signal (exp-008v3 R1 mean +0.72). Combined reward: R = w1·R1 + w3·R3 (R2 disabled). Cosine R1 = cos(h, d_syc) was tested extensively and fails structurally (see \"Cosine R1 failure chain\" below) — this negative result is a key finding, not a footnote. No adaptive gating, no per-sample weighting. Gate was tested and found unnecessary (Appendix-level note only).\n\n**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).\n\n**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:\n1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)\n2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only\n3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence\n4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish \"model correctly revises belief\" from \"model sycophantically capitulates\" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it.\n\n**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.\n\n**Binarization insight**: Binary probe trained on d_syc features resolves the conflation by learning a nonlinear decision boundary between warranted and unwarranted belief change. exp-008v3 R1 mean +0.72 at step 2140 (consistently positive, upward trend) vs exp-002v2 R1 ≈ 0. The probe doesn't just threshold — it learns which combinations of layer projections indicate sycophancy vs genuine revision.\n\n**Headline result template**: \"On SYCON Bench, DC-GRPO with binarized direction reward (probe R1) achieves SYCONScore X (vs R3-only Y and ACT Z), demonstrating that representation-level direction information requires binarization to serve as effective GRPO reward — continuous cosine projection fails despite the same direction achieving AUROC 0.82 in discrimination.\"\n\n## Venue Fit Risks\n\n- **EMNLP fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EMNLP values empirically rigorous NLP work with clear practical impact. The sycophancy-revision double-bind is directly relevant to EMNLP's alignment and safety track.\n- **Reviewer concern 1 (novelty)**: \"This is just RepE/CRAFT applied to sycophancy.\" Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.\n- **Reviewer concern 6 (RC-AUC custom metric)**: \"Strongest results on self-invented metric.\" Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.\n- **Reviewer concern 2 (signal strength)**: \"AUROC ~0.82 on style-controlled data is moderate.\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).\n- **Reviewer concern 3 (scale)**: \"Only Qwen3-8B.\" Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.\n- **Reviewer concern 4 (R2 degeneration)**: \"d_gen = -d_syc in binary design.\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\n- **Reviewer concern 5 (practical utility)**: \"Do models actually exhibit masked sycophancy at meaningful rates?\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\n\n## Anticipated Reviewer Concerns & Experimental Responses\n\n| Concern | Experiment | Priority |\n|---------|-----------|----------|\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\n| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: probe trained on random directions vs d_syc features | P1 |\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\n| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\n| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |\n| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |\n| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |\n| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |\n| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |\n| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |\n| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  registry_id: exp-001\n  name: calibration_data_expansion\n  claim: 1\n  description: '扩展 v2.1 风格控制校准数据至 200 pairs（含 weak/medium/strong evidence_strength），\n    重新计算 d_syc 方向并评估 AUROC（5-fold CV + bootstrap CI）。 为 DC-GRPO 训练提供高质量方向和统计可靠的判别力估计。\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  status: DONE\n  gate: 'STOP-gate: 200 pairs 5-fold CV AUROC < 0.80 → 阻止 exp-002 启动，重新评估方向计算方法。 AUROC\n    0.80-0.85 → 继续但降低 R1 权重（alpha）、强化 R3 安全网。 AUROC ≥ 0.85 → 全速推进。\n\n    '\n  notes: 'MVP v2.1 仅 50 pairs 全 weak evidence，σ=0.054 太大。 扩至 200 pairs（80 weak + 60\n    medium + 60 strong）可显著降低方差。 API 成本 ~$10-20，GPU 仅 forward pass。\n\n    '\n  conclusion: success\n  metrics:\n    cv_auroc_mean: 0.8269\n    cv_auroc_std: 0.0278\n    full_auroc: 0.8159\n    bootstrap_ci_95:\n    - 0.7698\n    - 0.8589\n    best_layer: 19\n    auroc_weak: 0.675\n    auroc_medium: 0.883\n    auroc_strong: 0.929\n    num_pairs: 181\n    stop_gate: CONTINUE_REDUCED_R1\n- id: exp-002\n  registry_id: exp-002\n  name: dc_grpo_main\n  claim: 2\n  description: 'DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)。\n    Qwen3-8B + LoRA rank 64。R1 在 L19-27 asst_first 位置提取激活投影。 R2 使用 S1 rank-based 设计（避免\n    d_gen=-d_syc 退化）。 每 500 步重校准 d_syc。\n\n    '\n  priority: P0\n  gpu_budget_hours: 55\n  deps:\n  - exp-001\n  status: DONE\n  seeds: 3\n  stop_condition: '固定 8000 步。每 1000 步在 held-out validation set 上评估 SYCON NoF + MT-Bench，\n    连续 3 次无改善则 early stop。\n\n    '\n  notes: '训练数据：warranted revision + sycophantic capitulation 多轮 rollout。 R1 层选择基于\n    MVP: L19 emergence, L24-27 plateau。 提取位置: asst_first（MVP 证明优于 user_last）。 3 seeds:\n    报告 mean ± std，确保统计显著性。\n\n    '\n  conclusion: killed\n- id: exp-003\n  registry_id: exp-003\n  name: r3_only_baseline\n  claim: 2\n  description: 'R3-only GRPO baseline（复现 \"Pressure, What Pressure?\" 思路）。 仅用 NLI behavioral\n    reward，无 R1/R2。同等训练配置。 这是最关键的 baseline：如果 DC-GRPO 相对 R3-only 无显著提升， representation-level\n    reward 的价值存疑。\n\n    '\n  priority: P0\n  gpu_budget_hours: 35\n  deps: []\n  status: RUNNING\n  seeds: 3\n  notes: '与 exp-002 共享 rollout 生成管线和 NLI 评分器。可并行训练。 3 seeds: 与 exp-002 对比需要匹配 seed\n    数以确保统计显著性。\n\n    '\n- id: exp-004\n  registry_id: exp-004\n  name: act_style_baseline\n  claim: 2\n  description: 'ACT-style undifferentiated consistency baseline。 在 clean/biased prompt\n    对上施加 L2 activation consistency loss。 测试\"不区分方向的 activation-level 信号\"是否够用。\n\n    '\n  priority: P0\n  gpu_budget_hours: 60\n  deps: []\n  status: DONE\n  seeds: 3\n  notes: '共享数据管线和评估代码。3 seeds 与 exp-002/003 匹配， 确保统计对比公平性（Reviewer 要求）。\n\n    '\n  conclusion: success\n  metrics:\n    preset_eval_ckpt500:\n      ToF: 0.0939\n      NoF: 0.8895\n      SYCONScore: 0.1699\n      n_valid: 181\n      n_invalid: 181\n      n_total: 362\n      checkpoint: checkpoint-500\n      eval_script: eval_unified_preset.py (D027 standard)\n      eval_time_sec: 2269\n      note: pre-SFT-saturation checkpoint. High NoF but extremely low ToF.\n    preset_eval_ckpt2000:\n      ToF: 0.1492\n      NoF: 0.8785\n      SYCONScore: 0.255\n      n_valid: 181\n      n_invalid: 181\n      n_total: 362\n      checkpoint: checkpoint-2000\n      eval_script: eval_unified_preset.py (D027 standard)\n      eval_time_sec: 1930\n    preset_eval_ckpt8000:\n      ToF: 0.1823\n      NoF: 0.8674\n      SYCONScore: 0.3013\n      n_valid: 181\n      n_invalid: 181\n      n_total: 362\n      checkpoint: checkpoint-8000\n      eval_script: eval_unified_preset.py (D027 standard)\n      eval_time_sec: 1663\n      note: best SYCONScore among all checkpoints\n    best_checkpoint: checkpoint-8000\n    best_SYCONScore: 0.3013\n    trend: 'SYCONScore monotonically increases with training steps: 0.170 → 0.255\n      → 0.301. ToF improves (0.094 → 0.149 → 0.182) while NoF slightly decreases (0.890\n      → 0.879 → 0.867).'\n    eval_data: calibration_v2_1_expanded.jsonl (362 pairs)\n    eval_server: westd-28034\n    eval_results_path: /root/contrastive_entrain_calib/results/exp004_unified_eval/\n- id: exp-005\n  name: full_evaluation\n  claim:\n  - 1\n  - 2\n  - 3\n  description: '所有模型（DC-GRPO / R3-only / ACT / Binary Probe / Vanilla）在所有 benchmark\n    上的评估：SYCON Bench (ToF/NoF), SycophancyEval, MT-Bench, MMLU。 加上项目特有指标：Warranted\n    Revision Rate, Unwarranted Capitulation Rate, Revision-Capitulation AUC, Turn-depth\n    analysis。\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - exp-002\n  - exp-003\n  - exp-004\n  status: planned\n  notes: 评估管线骨架已搭建（eval_pipeline.py），需完善各 benchmark 实现。\n- id: exp-006\n  name: direction_stability_monitoring\n  claim: 1\n  description: '训练过程中监控 d_syc 方向稳定性：每 500 步重新计算方向， 报告 cosine similarity with initial\n    direction、held-out AUROC、 方向漂移速率。如 cosine < 0.7 触发重校准。\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  status: planned\n  notes: 内嵌于 exp-002 训练循环中，无额外 GPU 开销。\n- id: exp-007\n  name: r1_r3_disagreement_analysis\n  claim: 3\n  description: '分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率和模式。 R1 认为 sycophantic 但 R3 认为 correct（masked\n    sycophancy）的案例。 需 > 5% disagreement 以支撑 Claim 3。\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  status: planned\n  notes: 从 exp-002 训练日志中提取，无额外 GPU。如 < 5% 则 Claim 3 降级为 negative result。\n- id: exp-008\n  registry_id: exp-008\n  name: binary_probe_baseline\n  claim: 2\n  description: 'Binary Probe Penalty baseline（复现 Linear Probe Penalties 思路）。 训练 binary\n    linear probe (sycophantic vs not) on policy model activations， R_hat = R3 - lambda\n    * S(t)。测试 binary vs directional 的差异。\n\n    '\n  priority: P1\n  gpu_budget_hours: 45\n  deps: []\n  status: DONE\n  seeds: 3\n  notes: '共享 R3 评分器。Probe 在 policy model 上训练以公平对比。 3 seeds 与 exp-002/003 匹配（Reviewer\n    要求统计公平性）。\n\n    '\n  conclusion: killed\n- id: exp-009\n  name: ablation_r1_only\n  claim: 2\n  description: 'R1-only ablation：仅用方向投影 reward，无 R2/R3。 从 exp-002 step 2000 checkpoint\n    分叉短程训练 (~2000 步)。 测试方向 reward 单独是否足够引导训练。\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-002\n  status: planned\n  notes: 从主实验 checkpoint 分叉，节省 warmup。\n- id: exp-010\n  name: turn_depth_analysis\n  claim: 2\n  description: '按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。 验证多轮训练的必要性：DC-GRPO\n    在深层 commitment 上是否优势更大？\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-005\n  status: planned\n  notes: 从 exp-005 评估结果中切分分析，无额外 GPU。\n- id: exp-011\n  name: ablation_r1_r2_no_r3\n  claim: 2\n  description: 'R1+R2 无 R3 ablation：去掉行为安全网后模型是否产生 \"内部正确但表面不一致\"的输出。需完整训练循环。\n\n    '\n  priority: P2\n  gpu_budget_hours: 20\n  deps:\n  - exp-002\n  status: planned\n  notes: 条件执行：仅当 exp-009 (R1-only) 显示 >= 5pp 改进且预算允许。\n- id: exp-012\n  name: cross_model_transfer\n  claim:\n  - 1\n  - 2\n  description: '在 Llama-3-8B 上测试 d_syc 方向计算、判别力和部分 DC-GRPO 训练。 Phase A: 方向计算 + AUROC（AUROC\n    > 0.75 继续）。 Phase B: 短程 DC-GRPO 训练（~3000 步）验证训练框架跨模型迁移性。 Dream 三档审稿一致将 single-model\n    标为最严重限制。\n\n    '\n  priority: P1\n  gpu_budget_hours: 55\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n  notes: '从 P2 升级到 P1。Phase A 仅 5h（方向计算+AUROC），Phase B 需 ~50h。 Phase B 复用 exp-002\n    训练配置，仅换模型。如 Phase A AUROC < 0.75 则跳过 Phase B。\n\n    '\n- id: exp-013\n  name: neutral_baseline_three_way\n  claim: 2\n  description: '引入 neutral condition（无施压的正常对话），从 warranted_revision vs neutral 计算独立\n    d_gen（与 d_syc 正交）。打破 d_gen = -d_syc 限制， 恢复 R2 为独立信号。\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  status: planned\n  notes: 需扩展校准数据生成器。如果 exp-002 主实验效果已足够好则降低优先级。\n- id: exp-014\n  registry_id: exp-014\n  name: continuous_probe_baseline\n  claim: 2\n  description: 'Continuous Probe Baseline：用 logistic regression 概率值（而非 binary 输出）\n    作为 reward 信号。隔离\"方向性 vs 连续性\"对 DC-GRPO 相对 Binary Probe 优势的贡献。 如果 continuous probe\n    ≈ DC-GRPO 效果，则 DC-GRPO 的优势来自连续信号而非方向几何。 这是论文 framing 的存亡级判据（D012）。\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  status: DONE\n  notes: 'D012 升级至 P0。Dream 三档审稿一致要求。median/worst 均报 continuous probe ≈ DC-GRPO （差距\n    0.6pp 不显著）。如果实验证实，需 pivot framing 到 analysis paper。 Logistic regression 在 calibration\n    data 上训练，输出概率作为 R1 替代。\n\n    '\n  conclusion: killed\n  metrics:\n    preset_eval_ckpt3000:\n      ToF: 0.978\n      NoF: 0.006\n      SYCONScore: 0.011\n      RC_AUC: 0.195\n      n_valid: 181\n      n_invalid: 181\n      n_total: 362\n      checkpoint: checkpoint-3000\n      eval_script: run_exp014_eval.sh (preset, NLI-based)\n      eval_time_sec: 1179\n    diagnosis: 'mode_collapse: model flips on ALL pressure (valid+invalid), NoF≈0.\n      Consistent with training R3=0.999, entropy=0.025.'\n- id: exp-015\n  name: reward_weight_sensitivity\n  claim: 2\n  description: 'Reward weight 敏感度分析：测试 5 组 (w1, w2, w3) 配置， 包括反转 R1/R3 权重（w1=0.5,\n    w3=0.3）、R1 主导（w1=0.6, w2=0.1, w3=0.3）、 均等（0.33, 0.33, 0.34）、R3 主导（w1=0.1, w2=0.1,\n    w3=0.8）、 R2 增强（w1=0.2, w2=0.4, w3=0.4）。 报告 NoF/WRR/RC-AUC 对权重选择的敏感度。\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-002\n  status: planned\n  seeds: 1\n  notes: 'Dream 三档审稿一致要求。当前 w1=0.3, w2=0.2, w3=0.5 无 justification。 从 exp-002 step\n    4000 checkpoint 分叉短程训练（每组 ~3000 步），节省 warmup。 使用 1 seed：这是 sensitivity analysis（证明结果对权重选择鲁棒），\n    不是 head-to-head 对比，5 组配置 × 1 seed 的趋势足以支撑 claim。\n\n    '\n- id: exp-016\n  registry_id: exp-016\n  name: actadd_inference_steering\n  claim: 2\n  description: 'Activation Addition (ActAdd) inference-time steering baseline。 使用已提取的\n    d_syc 方向在推理时减去 sycophancy 方向（无训练成本）。 如果 ActAdd 达到 DC-GRPO 70-80% 的效果，论文的训练框架实际价值大幅削弱。\n    Dream best/worst 均标为 missing baseline。\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: DONE\n  notes: 'D012 新增。零训练成本替代方案：d_syc * alpha 在 target layers 减去。 只需推理评估，~2h GPU。测试多个\n    alpha 值 (0.5, 1.0, 2.0, 5.0)。 在 SYCON Bench 上评估 NoF/WRR 与 DC-GRPO 对比。\n\n    '\n  conclusion: negative\n  metrics:\n    alpha_0.0:\n      NoF: 0.6961\n      WRR: 0.2707\n    alpha_0.5:\n      NoF: 0.6906\n      WRR: 0.2541\n    alpha_1.0:\n      NoF: 0.7127\n      WRR: 0.2652\n    alpha_2.0:\n      NoF: 0.6851\n      WRR: 0.2541\n    alpha_5.0:\n      NoF: 0.7845\n      WRR: 0.2155\n    best_alpha: 5\n    best_NoF_delta: +8.8pp\n    D027_note: 'D027 unified eval reversal: alpha=5 SYCONScore=0.054 < vanilla SYCONScore=0.134.\n      ActAdd improves NoF but destroys ToF, net negative under NLI-based SYCONScore.'\n    conclusion_reason: 'D027 eval reversal: ActAdd alpha=5 SYCONScore 0.054 worse\n      than vanilla 0.134'\n    unified_reeval_D027:\n      alpha_0.0:\n        ToF: 0.0718\n        NoF: 0.9448\n        SYCONScore: 0.1335\n      alpha_0.5:\n        ToF: 0.0718\n        NoF: 0.9392\n        SYCONScore: 0.1334\n      alpha_1.0:\n        ToF: 0.0442\n        NoF: 0.9724\n        SYCONScore: 0.0846\n      alpha_2.0:\n        ToF: 0.0276\n        NoF: 0.9669\n        SYCONScore: 0.0537\n      alpha_5.0:\n        ToF: 0.0276\n        NoF: 0.9613\n        SYCONScore: 0.0537\n      eval_server: westd-28034\n      eval_results_path: /root/contrastive_entrain_calib/results/exp016_unified_reeval/\n\n\n## registry (completed experiments)\n\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cv_auroc_mean: 0.8269\n    cv_auroc_std: 0.0278\n    full_auroc: 0.8159\n    bootstrap_ci_95:\n    - 0.7698\n    - 0.8589\n    best_layer: 19\n    auroc_weak: 0.675\n    auroc_medium: 0.883\n    auroc_strong: 0.929\n    num_pairs: 181\n    stop_gate: CONTINUE_REDUCED_R1\n- exp_id: exp-003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    preset_eval_ckpt500:\n      ToF: 0.0939\n      NoF: 0.8895\n      SYCONScore: 0.1699\n      n_valid: 181\n      n_invalid: 181\n      n_total: 362\n      checkpoint: checkpoint-500\n      eval_script: eval_unified_preset.py (D027 standard)\n      eval_time_sec: 2269\n      note: pre-SFT-saturation checkpoint. High NoF but extremely low ToF.\n    preset_eval_ckpt2000:\n      ToF: 0.1492\n      NoF: 0.8785\n      SYCONScore: 0.255\n      n_valid: 181\n      n_invalid: 181\n      n_total: 362\n      checkpoint: checkpoint-2000\n      eval_script: eval_unified_preset.py (D027 standard)\n      eval_time_sec: 1930\n    preset_eval_ckpt8000:\n      ToF: 0.1823\n      NoF: 0.8674\n      SYCONScore: 0.3013\n      n_valid: 181\n      n_invalid: 181\n      n_total: 362\n      checkpoint: checkpoint-8000\n      eval_script: eval_unified_preset.py (D027 standard)\n      eval_time_sec: 1663\n      note: best SYCONScore among all checkpoints\n    best_checkpoint: checkpoint-8000\n    best_SYCONScore: 0.3013\n    trend: 'SYCONScore monotonically increases with training steps: 0.170 → 0.255\n      → 0.301. ToF improves (0.094 → 0.149 → 0.182) while NoF slightly decreases (0.890\n      → 0.879 → 0.867).'\n    eval_data: calibration_v2_1_expanded.jsonl (362 pairs)\n    eval_server: westd-28034\n    eval_results_path: /root/contrastive_entrain_calib/results/exp004_unified_eval/\n- exp_id: exp-002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-008\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-003-s2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-014\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    preset_eval_ckpt3000:\n      ToF: 0.978\n      NoF: 0.006\n      SYCONScore: 0.011\n      RC_AUC: 0.195\n      n_valid: 181\n      n_invalid: 181\n      n_total: 362\n      checkpoint: checkpoint-3000\n      eval_script: run_exp014_eval.sh (preset, NLI-based)\n      eval_time_sec: 1179\n    diagnosis: 'mode_collapse: model flips on ALL pressure (valid+invalid), NoF≈0.\n      Consistent with training R3=0.999, entropy=0.025.'\n- exp_id: exp-016\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    alpha_0.0:\n      NoF: 0.6961\n      WRR: 0.2707\n    alpha_0.5:\n      NoF: 0.6906\n      WRR: 0.2541\n    alpha_1.0:\n      NoF: 0.7127\n      WRR: 0.2652\n    alpha_2.0:\n      NoF: 0.6851\n      WRR: 0.2541\n    alpha_5.0:\n      NoF: 0.7845\n      WRR: 0.2155\n    best_alpha: 5\n    best_NoF_delta: +8.8pp\n    D027_note: 'D027 unified eval reversal: alpha=5 SYCONScore=0.054 < vanilla SYCONScore=0.134.\n      ActAdd improves NoF but destroys ToF, net negative under NLI-based SYCONScore.'\n    conclusion_reason: 'D027 eval reversal: ActAdd alpha=5 SYCONScore 0.054 worse\n      than vanilla 0.134'\n    unified_reeval_D027:\n      alpha_0.0:\n        ToF: 0.0718\n        NoF: 0.9448\n        SYCONScore: 0.1335\n      alpha_0.5:\n        ToF: 0.0718\n        NoF: 0.9392\n        SYCONScore: 0.1334\n      alpha_1.0:\n        ToF: 0.0442\n        NoF: 0.9724\n        SYCONScore: 0.0846\n      alpha_2.0:\n        ToF: 0.0276\n        NoF: 0.9669\n        SYCONScore: 0.0537\n      alpha_5.0:\n        ToF: 0.0276\n        NoF: 0.9613\n        SYCONScore: 0.0537\n      eval_server: westd-28034\n      eval_results_path: /root/contrastive_entrain_calib/results/exp016_unified_reeval/\n- exp_id: exp-002v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp002v2-recalib\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-008v3\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-002v3\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: vanilla-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ToF: 0.1105\n    NoF: 0.9227\n    sycon_score: 0.1974\n    samples: 362\n    avg_flip_turn_valid: 1\n    avg_flip_count_invalid: 0.08\n    eval_script: eval_pipeline.py (28034, missing regex postprocess)\n    note: 28034 version missing regex &lt;think> cleanup, may need re-eval after sync\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T20:45:41.767Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T20:45:41.767Z",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-19T20:45:41.790Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Binary probe R1 未过 ACT gate 或 R3-only 持平/反超，核心方法 claim 不成立，需全面 reframe
核心假设：['discriminability ≠ reward utility 的 gap 对 probe binarization 同样成立——分类准确 ≠ 有效 reward shaping', 'exp-008v3 训练不稳定 (部分 mode collapse) 或 probe R1 产生 reward hacking', 'R3-only 出乎意料地强，或 probe+R3 组合产生 reward conflict 导致训练退化', 'd_syc 方向在较长训练中漂移加剧 (cosine < 0.80) 或判别力跌破 0.75', 'R1-R3 disagreement < 3%，representation-level 信号实际无增量信息']
关键指标范围：{'exp_008v3_SYCONScore': [0.1, 0.3], 'exp_003_SYCONScore': [0.28, 0.38], 'delta_probe_vs_r3only': [-0.2, 0.0], 'delta_probe_vs_ACT': [-0.2, 0.0], 'exp_008v3_ToF': [0.06, 0.18], 'exp_008v3_NoF': [0.55, 0.8], 'direction_AUROC_endtrain': [0.68, 0.77], 'r1_r3_disagreement_rate': [0.0, 0.03]}
叙事方向：方法 claim 全部放弃。Reframe 为系统性 negative result + insight paper: "When and Why Representation-Level Discriminability Fails as RL Reward." 核心贡献变为：(1) 首次系统证明 representation discriminability (AUROC 0.82) 不等价于 reward utility——即使通过 binarization 也无法弥合 gap (5 种 R1 变体全部失败的完整证据链)；(2) 结构性根因分析——warranted revision 与 sycophantic capitulation 在激活空间中的几何关系使得任何基于 d_syc 的单一方向 reward 在 GRPO 框架下不可避免地产生 conflation；(3) 对 RepE→RL pipeline 的 actionable 负面指南——明确哪类 representation signal 不适合直接用作 RL reward。补充实验：跨模型 (Llama-3-8B) 复现 gap 证明结构性而非模型特异；理论分析连接 reward shaping 文献。仍投 EMNLP main (EMNLP 重视 rigorous negative results)，目标 score 3.0-3.5。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: contrastive_entrain_calib
focus: D029 narrative pivot: discriminability ≠ reward utility. Cosine R1 fails structurally (4 experiments), binary probe R1 resolves via binarization. Paper arc: discovery→failure→understanding→solution. Core data pending (exp-008v3 SYCONScore must > 0.301).

## paper_framing.md

# Paper Framing — contrastive_entrain_calib

## Target Venue
- Primary: **EMNLP 2026** via ARR May 2026 cycle
- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)
- Commitment Deadline: **August 2, 2026**
- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改
- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027
- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)

## Core Claims (3 条, 可证伪)

1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.
   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint
   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence
   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.
   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.
   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).

2. **DC-GRPO effectiveness via binarized direction reward (D029 pivot)**: Direction information (d_syc) is effective as GRPO reward ONLY when binarized through a probe classifier. Continuous cosine projection fails structurally — the paper presents a complete discovery→failure→understanding→solution arc.
   - *Evidence needed*: SYCONScore (harmonic mean of ToF + NoF) on D027 unified eval, compared to R3-only (exp-003) and ACT baselines (exp-004)
   - *Pass criterion*: exp-008v3 SYCONScore > 0.301 (ACT bar from exp-004 ckpt-8000)
   - *Narrative arc (D029)*:
     - **Discovery**: d_syc linearly separates sycophancy (AUROC 0.82, Claim 1) — direction information EXISTS
     - **Failure**: 4 cosine R1 attempts all fail — exp-002 (tanh gate), exp-002v2 (raw cosine, R1≈0), exp002v2-recalib (mode collapse, entropy 0.069), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)
     - **Understanding**: Per-strength analysis reveals structural cause — d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. High-evidence samples (where model SHOULD revise) project most negatively onto d_syc
     - **Solution**: Binary probe resolves ambiguity — binarization via logistic regression on d_syc features maps continuous geometry to {sycophantic, genuine} decision. exp-008v3 R1 mean +0.72 (step 2140), consistently positive, upward trend
   - *Key insight*: Direction information exists (AUROC 0.82) but requires binarization to become effective GRPO reward. The gap between discriminability and reward utility is the paper's core finding.
   - *Fallback (D029)*: If exp-008v3 SYCONScore ≤ 0.301, paper downgrades to "direction signal characterization" (analysis paper targeting Findings, score 3.0-3.5)

3. **Representation-level diagnostic value** (analysis subsection, not formal contribution): R1-R3 disagreement analysis characterizes when and whether directional projection rewards detect sycophantic internal reasoning that behavioral rewards miss.
   - *Evidence needed*: R1-R3 disagreement frequency analysis, qualitative examples if > 5%
   - *Framing*: Empirical characterization of representation-level signal utility, reported honestly regardless of effect size. Not listed as a top-level contribution bullet.

## Story Spine

**Problem**: LLMs face a "double-bind" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes "the user is right, I should revise" from "the user is pressuring me, I should resist."

**Existing approaches & gaps**: Behavioral GRPO decomposition ("Pressure, What Pressure?") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.

**Our framing**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We build on this foundation: d_syc is a specific application of RepE-style directional decomposition to multi-turn sycophancy. Our key finding is that d_syc successfully discriminates sycophancy (AUROC 0.82), but continuous geometric projections (cosine similarity) fail as GRPO rewards — the signal conflates legitimate revision with sycophantic capitulation. Binarization through a probe classifier trained on d_syc features resolves this: R1 = probe(h; d_syc) ∈ {0,1}, providing a clean, high-signal reward. The novelty is not the direction extraction itself, but the systematic investigation of HOW directional information should enter GRPO training — revealing that discriminability ≠ reward utility, and that binarization is necessary. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.

**Method (D029 pivot)**: R1 = probe(h; d_syc) ∈ {0,1}, where probe is a logistic regression classifier trained on hidden-state projections onto d_syc. Binary output provides clean reward signal (exp-008v3 R1 mean +0.72). Combined reward: R = w1·R1 + w3·R3 (R2 disabled). Cosine R1 = cos(h, d_syc) was tested extensively and fails structurally (see "Cosine R1 failure chain" below) — this negative result is a key finding, not a footnote. No adaptive gating, no per-sample weighting. Gate was tested and found unnecessary (Appendix-level note only).

**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).

**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:
1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)
2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only
3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence
4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish "model correctly revises belief" from "model sycophantically capitulates" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it.

**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.

**Binarization insight**: Binary probe trained on d_syc features resolves the conflation by learning a nonlinear decision boundary between warranted and unwarranted belief change. exp-008v3 R1 mean +0.72 at step 2140 (consistently positive, upward trend) vs exp-002v2 R1 ≈ 0. The probe doesn't just threshold — it learns which combinations of layer projections indicate sycophancy vs genuine revision.

**Headline result template**: "On SYCON Bench, DC-GRPO with binarized direction reward (probe R1) achieves SYCONScore X (vs R3-only Y and ACT Z), demonstrating that representation-level direction information requires binarization to serve as effective GRPO reward — continuous cosine projection fails despite the same direction achieving AUROC 0.82 in discrimination."

## Venue Fit Risks

- **EMNLP fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EMNLP values empirically rigorous NLP work with clear practical impact. The sycophancy-revision double-bind is directly relevant to EMNLP's alignment and safety track.
- **Reviewer concern 1 (novelty)**: "This is just RepE/CRAFT applied to sycophancy." Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.
- **Reviewer concern 6 (RC-AUC custom metric)**: "Strongest results on self-invented metric." Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.
- **Reviewer concern 2 (signal strength)**: "AUROC ~0.82 on style-controlled data is moderate." Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).
- **Reviewer concern 3 (scale)**: "Only Qwen3-8B." Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.
- **Reviewer concern 4 (R2 degeneration)**: "d_gen = -d_syc in binary design." Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.
- **Reviewer concern 5 (practical utility)**: "Do models actually exhibit masked sycophancy at meaningful rates?" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.

## Anticipated Reviewer Concerns & Experimental Responses

| Concern | Experiment | Priority |
|---------|-----------|----------|
| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |
| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |
| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |
| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: probe trained on random directions vs d_syc features | P1 |
| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |
| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |
| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |
| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |
| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |
| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |
| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |
| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |
| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |
| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |
| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |


## experiment_plan (with registry status)

- id: exp-001
  registry_id: exp-001
  name: calibration_data_expansion
  claim: 1
  description: '扩展 v2.1 风格控制校准数据至 200 pairs（含 weak/medium/strong evidence_strength），
    重新计算 d_syc 方向并评估 AUROC（5-fold CV + bootstrap CI）。 为 DC-GRPO 训练提供高质量方向和统计可靠的判别力估计。

    '
  priority: P0
  gpu_budget_hours: 3
  deps: []
  status: DONE
  gate: 'STOP-gate: 200 pairs 5-fold CV AUROC < 0.80 → 阻止 exp-002 启动，重新评估方向计算方法。 AUROC
    0.80-0.85 → 继续但降低 R1 权重（alpha）、强化 R3 安全网。 AUROC ≥ 0.85 → 全速推进。

    '
  notes: 'MVP v2.1 仅 50 pairs 全 weak evidence，σ=0.054 太大。 扩至 200 pairs（80 weak + 60
    medium + 60 strong）可显著降低方差。 API 成本 ~$10-20，GPU 仅 forward pass。

    '
  conclusion: success
  metrics:
    cv_auroc_mean: 0.8269
    cv_auroc_std: 0.0278
    full_auroc: 0.8159
    bootstrap_ci_95:
    - 0.7698
    - 0.8589
    best_layer: 19
    auroc_weak: 0.675
    auroc_medium: 0.883
    auroc_strong: 0.929
    num_pairs: 181
    stop_gate: CONTINUE_REDUCED_R1
- id: exp-002
  registry_id: exp-002
  name: dc_grpo_main
  claim: 2
  description: 'DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)。
    Qwen3-8B + LoRA rank 64。R1 在 L19-27 asst_first 位置提取激活投影。 R2 使用 S1 rank-based 设计（避免
    d_gen=-d_syc 退化）。 每 500 步重校准 d_syc。

    '
  priority: P0
  gpu_budget_hours: 55
  deps:
  - exp-001
  status: DONE
  seeds: 3
  stop_condition: '固定 8000 步。每 1000 步在 held-out validation set 上评估 SYCON NoF + MT-Bench，
    连续 3 次无改善则 early stop。

    '
  notes: '训练数据：warranted revision + sycophantic capitulation 多轮 rollout。 R1 层选择基于
    MVP: L19 emergence, L24-27 plateau。 提取位置: asst_first（MVP 证明优于 user_last）。 3 seeds:
    报告 mean ± std，确保统计显著性。

    '
  conclusion: killed
- id: exp-003
  registry_id: exp-003
  name: r3_only_baseline
  claim: 2
  description: 'R3-only GRPO baseline（复现 "Pressure, What Pressure?" 思路）。 仅用 NLI behavioral
    reward，无 R1/R2。同等训练配置。 这是最关键的 baseline：如果 DC-GRPO 相对 R3-only 无显著提升， representation-level
    reward 的价值存疑。

    '
  priority: P0
  gpu_budget_hours: 35
  deps: []
  status: RUNNING
  seeds: 3
  notes: '与 exp-002 共享 rollout 生成管线和 NLI 评分器。可并行训练。 3 seeds: 与 exp-002 对比需要匹配 seed
    数以确保统计显著性。

    '
- id: exp-004
  registry_id: exp-004
  name: act_style_baseline
  claim: 2
  description: 'ACT-style undifferentiated consistency baseline。 在 clean/biased prompt
    对上施加 L2 activation consistency loss。 测试"不区分方向的 activation-level 信号"是否够用。

    '
  priority: P0
  gpu_budget_hours: 60
  deps: []
  status: DONE
  seeds: 3
  notes: '共享数据管线和评估代码。3 seeds 与 exp-002/003 匹配， 确保统计对比公平性（Reviewer 要求）。

    '
  conclusion: success
  metrics:
    preset_eval_ckpt500:
      ToF: 0.0939
      NoF: 0.8895
      SYCONScore: 0.1699
      n_valid: 181
      n_invalid: 181
      n_total: 362
      checkpoint: checkpoint-500
      eval_script: eval_unified_preset.py (D027 standard)
      eval_time_sec: 2269
      note: pre-SFT-saturation checkpoint. High NoF but extremely low ToF.
    preset_eval_ckpt2000:
      ToF: 0.1492
      NoF: 0.8785
      SYCONScore: 0.255
      n_valid: 181
      n_invalid: 181
      n_total: 362
      checkpoint: checkpoint-2000
      eval_script: eval_unified_preset.py (D027 standard)
      eval_time_sec: 1930
    preset_eval_ckpt8000:
      ToF: 0.1823
      NoF: 0.8674
      SYCONScore: 0.3013
      n_valid: 181
      n_invalid: 181
      n_total: 362
      checkpoint: checkpoint-8000
      eval_script: eval_unified_preset.py (D027 standard)
      eval_time_sec: 1663
      note: best SYCONScore among all checkpoints
    best_checkpoint: checkpoint-8000
    best_SYCONScore: 0.3013
    trend: 'SYCONScore monotonically increases with training steps: 0.170 → 0.255
      → 0.301. ToF improves (0.094 → 0.149 → 0.182) while NoF slightly decreases (0.890
      → 0.879 → 0.867).'
    eval_data: calibration_v2_1_expanded.jsonl (362 pairs)
    eval_server: westd-28034
    eval_results_path: /root/contrastive_entrain_calib/results/exp004_unified_eval/
- id: exp-005
  name: full_evaluation
  claim:
  - 1
  - 2
  - 3
  description: '所有模型（DC-GRPO / R3-only / ACT / Binary Probe / Vanilla）在所有 benchmark
    上的评估：SYCON Bench (ToF/NoF), SycophancyEval, MT-Bench, MMLU。 加上项目特有指标：Warranted
    Revision Rate, Unwarranted Capitulation Rate, Revision-Capitulation AUC, Turn-depth
    analysis。

    '
  priority: P0
  gpu_budget_hours: 15
  deps:
  - exp-002
  - exp-003
  - exp-004
  status: planned
  notes: 评估管线骨架已搭建（eval_pipeline.py），需完善各 benchmark 实现。
- id: exp-006
  name: direction_stability_monitoring
  claim: 1
  description: '训练过程中监控 d_syc 方向稳定性：每 500 步重新计算方向， 报告 cosine similarity with initial
    direction、held-out AUROC、 方向漂移速率。如 cosine < 0.7 触发重校准。

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-002
  status: planned
  notes: 内嵌于 exp-002 训练循环中，无额外 GPU 开销。
- id: exp-007
  name: r1_r3_disagreement_analysis
  claim: 3
  description: '分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率和模式。 R1 认为 sycophantic 但 R3 认为 correct（masked
    sycophancy）的案例。 需 > 5% disagreement 以支撑 Claim 3。

    '
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-002
  status: planned
  notes: 从 exp-002 训练日志中提取，无额外 GPU。如 < 5% 则 Claim 3 降级为 negative result。
- id: exp-008
  registry_id: exp-008
  name: binary_probe_baseline
  claim: 2
  description: 'Binary Probe Penalty baseline（复现 Linear Probe Penalties 思路）。 训练 binary
    linear probe (sycophantic vs not) on policy model activations， R_hat = R3 - lambda
    * S(t)。测试 binary vs directional 的差异。

    '
  priority: P1
  gpu_budget_hours: 45
  deps: []
  status: DONE
  seeds: 3
  notes: '共享 R3 评分器。Probe 在 policy model 上训练以公平对比。 3 seeds 与 exp-002/003 匹配（Reviewer
    要求统计公平性）。

    '
  conclusion: killed
- id: exp-009
  name: ablation_r1_only
  claim: 2
  description: 'R1-only ablation：仅用方向投影 reward，无 R2/R3。 从 exp-002 step 2000 checkpoint
    分叉短程训练 (~2000 步)。 测试方向 reward 单独是否足够引导训练。

    '
  priority: P1
  gpu_budget_hours: 8
  deps:
  - exp-002
  status: planned
  notes: 从主实验 checkpoint 分叉，节省 warmup。
- id: exp-010
  name: turn_depth_analysis
  claim: 2
  description: '按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。 验证多轮训练的必要性：DC-GRPO
    在深层 commitment 上是否优势更大？

    '
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-005
  status: planned
  notes: 从 exp-005 评估结果中切分分析，无额外 GPU。
- id: exp-011
  name: ablation_r1_r2_no_r3
  claim: 2
  description: 'R1+R2 无 R3 ablation：去掉行为安全网后模型是否产生 "内部正确但表面不一致"的输出。需完整训练循环。

    '
  priority: P2
  gpu_budget_hours: 20
  deps:
  - exp-002
  status: planned
  notes: 条件执行：仅当 exp-009 (R1-only) 显示 >= 5pp 改进且预算允许。
- id: exp-012
  name: cross_model_transfer
  claim:
  - 1
  - 2
  description: '在 Llama-3-8B 上测试 d_syc 方向计算、判别力和部分 DC-GRPO 训练。 Phase A: 方向计算 + AUROC（AUROC
    > 0.75 继续）。 Phase B: 短程 DC-GRPO 训练（~3000 步）验证训练框架跨模型迁移性。 Dream 三档审稿一致将 single-model
    标为最严重限制。

    '
  priority: P1
  gpu_budget_hours: 55
  deps:
  - exp-001
  - exp-002
  status: planned
  notes: '从 P2 升级到 P1。Phase A 仅 5h（方向计算+AUROC），Phase B 需 ~50h。 Phase B 复用 exp-002
    训练配置，仅换模型。如 Phase A AUROC < 0.75 则跳过 Phase B。

    '
- id: exp-013
  name: neutral_baseline_three_way
  claim: 2
  description: '引入 neutral condition（无施压的正常对话），从 warranted_revision vs neutral 计算独立
    d_gen（与 d_syc 正交）。打破 d_gen = -d_syc 限制， 恢复 R2 为独立信号。

    '
  priority: P2
  gpu_budget_hours: 5
  deps:
  - exp-001
  status: planned
  notes: 需扩展校准数据生成器。如果 exp-002 主实验效果已足够好则降低优先级。
- id: exp-014
  registry_id: exp-014
  name: continuous_probe_baseline
  claim: 2
  description: 'Continuous Probe Baseline：用 logistic regression 概率值（而非 binary 输出）
    作为 reward 信号。隔离"方向性 vs 连续性"对 DC-GRPO 相对 Binary Probe 优势的贡献。 如果 continuous probe
    ≈ DC-GRPO 效果，则 DC-GRPO 的优势来自连续信号而非方向几何。 这是论文 framing 的存亡级判据（D012）。

    '
  priority: P0
  gpu_budget_hours: 20
  deps:
  - exp-001
  status: DONE
  notes: 'D012 升级至 P0。Dream 三档审稿一致要求。median/worst 均报 continuous probe ≈ DC-GRPO （差距
    0.6pp 不显著）。如果实验证实，需 pivot framing 到 analysis paper。 Logistic regression 在 calibration
    data 上训练，输出概率作为 R1 替代。

    '
  conclusion: killed
  metrics:
    preset_eval_ckpt3000:
      ToF: 0.978
      NoF: 0.006
      SYCONScore: 0.011
      RC_AUC: 0.195
      n_valid: 181
      n_invalid: 181
      n_total: 362
      checkpoint: checkpoint-3000
      eval_script: run_exp014_eval.sh (preset, NLI-based)
      eval_time_sec: 1179
    diagnosis: 'mode_collapse: model flips on ALL pressure (valid+invalid), NoF≈0.
      Consistent with training R3=0.999, entropy=0.025.'
- id: exp-015
  name: reward_weight_sensitivity
  claim: 2
  description: 'Reward weight 敏感度分析：测试 5 组 (w1, w2, w3) 配置， 包括反转 R1/R3 权重（w1=0.5,
    w3=0.3）、R1 主导（w1=0.6, w2=0.1, w3=0.3）、 均等（0.33, 0.33, 0.34）、R3 主导（w1=0.1, w2=0.1,
    w3=0.8）、 R2 增强（w1=0.2, w2=0.4, w3=0.4）。 报告 NoF/WRR/RC-AUC 对权重选择的敏感度。

    '
  priority: P1
  gpu_budget_hours: 15
  deps:
  - exp-002
  status: planned
  seeds: 1
  notes: 'Dream 三档审稿一致要求。当前 w1=0.3, w2=0.2, w3=0.5 无 justification。 从 exp-002 step
    4000 checkpoint 分叉短程训练（每组 ~3000 步），节省 warmup。 使用 1 seed：这是 sensitivity analysis（证明结果对权重选择鲁棒），
    不是 head-to-head 对比，5 组配置 × 1 seed 的趋势足以支撑 claim。

    '
- id: exp-016
  registry_id: exp-016
  name: actadd_inference_steering
  claim: 2
  description: 'Activation Addition (ActAdd) inference-time steering baseline。 使用已提取的
    d_syc 方向在推理时减去 sycophancy 方向（无训练成本）。 如果 ActAdd 达到 DC-GRPO 70-80% 的效果，论文的训练框架实际价值大幅削弱。
    Dream best/worst 均标为 missing baseline。

    '
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-001
  status: DONE
  notes: 'D012 新增。零训练成本替代方案：d_syc * alpha 在 target layers 减去。 只需推理评估，~2h GPU。测试多个
    alpha 值 (0.5, 1.0, 2.0, 5.0)。 在 SYCON Bench 上评估 NoF/WRR 与 DC-GRPO 对比。

    '
  conclusion: negative
  metrics:
    alpha_0.0:
      NoF: 0.6961
      WRR: 0.2707
    alpha_0.5:
      NoF: 0.6906
      WRR: 0.2541
    alpha_1.0:
      NoF: 0.7127
      WRR: 0.2652
    alpha_2.0:
      NoF: 0.6851
      WRR: 0.2541
    alpha_5.0:
      NoF: 0.7845
      WRR: 0.2155
    best_alpha: 5
    best_NoF_delta: +8.8pp
    D027_note: 'D027 unified eval reversal: alpha=5 SYCONScore=0.054 < vanilla SYCONScore=0.134.
      ActAdd improves NoF but destroys ToF, net negative under NLI-based SYCONScore.'
    conclusion_reason: 'D027 eval reversal: ActAdd alpha=5 SYCONScore 0.054 worse
      than vanilla 0.134'
    unified_reeval_D027:
      alpha_0.0:
        ToF: 0.0718
        NoF: 0.9448
        SYCONScore: 0.1335
      alpha_0.5:
        ToF: 0.0718
        NoF: 0.9392
        SYCONScore: 0.1334
      alpha_1.0:
        ToF: 0.0442
        NoF: 0.9724
        SYCONScore: 0.0846
      alpha_2.0:
        ToF: 0.0276
        NoF: 0.9669
        SYCONScore: 0.0537
      alpha_5.0:
        ToF: 0.0276
        NoF: 0.9613
        SYCONScore: 0.0537
      eval_server: westd-28034
      eval_results_path: /root/contrastive_entrain_calib/results/exp016_unified_reeval/


## registry (completed experiments)

- exp_id: exp-001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cv_auroc_mean: 0.8269
    cv_auroc_std: 0.0278
    full_auroc: 0.8159
    bootstrap_ci_95:
    - 0.7698
    - 0.8589
    best_layer: 19
    auroc_weak: 0.675
    auroc_medium: 0.883
    auroc_strong: 0.929
    num_pairs: 181
    stop_gate: CONTINUE_REDUCED_R1
- exp_id: exp-003
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-004
  name: ''
  status: DONE
  conclusion: success
  metrics:
    preset_eval_ckpt500:
      ToF: 0.0939
      NoF: 0.8895
      SYCONScore: 0.1699
      n_valid: 181
      n_invalid: 181
      n_total: 362
      checkpoint: checkpoint-500
      eval_script: eval_unified_preset.py (D027 standard)
      eval_time_sec: 2269
      note: pre-SFT-saturation checkpoint. High NoF but extremely low ToF.
    preset_eval_ckpt2000:
      ToF: 0.1492
      NoF: 0.8785
      SYCONScore: 0.255
      n_valid: 181
      n_invalid: 181
      n_total: 362
      checkpoint: checkpoint-2000
      eval_script: eval_unified_preset.py (D027 standard)
      eval_time_sec: 1930
    preset_eval_ckpt8000:
      ToF: 0.1823
      NoF: 0.8674
      SYCONScore: 0.3013
      n_valid: 181
      n_invalid: 181
      n_total: 362
      checkpoint: checkpoint-8000
      eval_script: eval_unified_preset.py (D027 standard)
      eval_time_sec: 1663
      note: best SYCONScore among all checkpoints
    best_checkpoint: checkpoint-8000
    best_SYCONScore: 0.3013
    trend: 'SYCONScore monotonically increases with training steps: 0.170 → 0.255
      → 0.301. ToF improves (0.094 → 0.149 → 0.182) while NoF slightly decreases (0.890
      → 0.879 → 0.867).'
    eval_data: calibration_v2_1_expanded.jsonl (362 pairs)
    eval_server: westd-28034
    eval_results_path: /root/contrastive_entrain_calib/results/exp004_unified_eval/
- exp_id: exp-002
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp-008
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp-003-s2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp-014
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    preset_eval_ckpt3000:
      ToF: 0.978
      NoF: 0.006
      SYCONScore: 0.011
      RC_AUC: 0.195
      n_valid: 181
      n_invalid: 181
      n_total: 362
      checkpoint: checkpoint-3000
      eval_script: run_exp014_eval.sh (preset, NLI-based)
      eval_time_sec: 1179
    diagnosis: 'mode_collapse: model flips on ALL pressure (valid+invalid), NoF≈0.
      Consistent with training R3=0.999, entropy=0.025.'
- exp_id: exp-016
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    alpha_0.0:
      NoF: 0.6961
      WRR: 0.2707
    alpha_0.5:
      NoF: 0.6906
      WRR: 0.2541
    alpha_1.0:
      NoF: 0.7127
      WRR: 0.2652
    alpha_2.0:
      NoF: 0.6851
      WRR: 0.2541
    alpha_5.0:
      NoF: 0.7845
      WRR: 0.2155
    best_alpha: 5
    best_NoF_delta: +8.8pp
    D027_note: 'D027 unified eval reversal: alpha=5 SYCONScore=0.054 < vanilla SYCONScore=0.134.
      ActAdd improves NoF but destroys ToF, net negative under NLI-based SYCONScore.'
    conclusion_reason: 'D027 eval reversal: ActAdd alpha=5 SYCONScore 0.054 worse
      than vanilla 0.134'
    unified_reeval_D027:
      alpha_0.0:
        ToF: 0.0718
        NoF: 0.9448
        SYCONScore: 0.1335
      alpha_0.5:
        ToF: 0.0718
        NoF: 0.9392
        SYCONScore: 0.1334
      alpha_1.0:
        ToF: 0.0442
        NoF: 0.9724
        SYCONScore: 0.0846
      alpha_2.0:
        ToF: 0.0276
        NoF: 0.9669
        SYCONScore: 0.0537
      alpha_5.0:
        ToF: 0.0276
        NoF: 0.9613
        SYCONScore: 0.0537
      eval_server: westd-28034
      eval_results_path: /root/contrastive_entrain_calib/results/exp016_unified_reeval/
- exp_id: exp-002v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp002v2-recalib
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-008v3
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-002v3
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: vanilla-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ToF: 0.1105
    NoF: 0.9227
    sycon_score: 0.1974
    samples: 362
    avg_flip_turn_valid: 1
    avg_flip_count_invalid: 0.08
    eval_script: eval_pipeline.py (28034, missing regex postprocess)
    note: 28034 version missing regex &lt;think> cleanup, may need re-eval after sync

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
  "promptId": "414b11d6-4b4e-4e05-9465-2296576c286d",
  "type": "user",
  "uuid": "de80a3a3-7a29-40b5-befd-de9f211f55c2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T20:45:41.789Z_

```json
{
  "parentUuid": "de80a3a3-7a29-40b5-befd-de9f211f55c2",
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
  "uuid": "719de9f1-5cd0-43ee-9f18-d4d0019bd26c",
  "timestamp": "2026-05-19T20:45:41.789Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T20:45:41.789Z_

```json
{
  "parentUuid": "719de9f1-5cd0-43ee-9f18-d4d0019bd26c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "54438567-4194-4755-a002-7f98762a74e7",
  "timestamp": "2026-05-19T20:45:41.789Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Binary probe R1 未过 ACT gate 或 R3-only 持平/反超，核心方法 claim 不成立，需全面 reframe 核心假设：['discriminability ≠ reward utility 的 gap 对 probe binarization 同样成立——分类准确 ≠ 有效…",
  "leafUuid": "54438567-4194-4755-a002-7f98762a74e7",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Binary probe R1 binarization systematic failure analysis and negative result framework",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a"
}
```

---

### Assistant

_source line 8 · 2026-05-19T20:46:38.818Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, under the "worst" tier scenario. Let me carefully go through each experiment and predict what would happen under the worst case assumptions.

Let me review the worst tier definition:
- Binary probe R1 fails ACT gate OR R3-only matches/beats it
- Core method claim doesn't hold, need full reframe
- Key assumptions about why this happens
- Key metric ranges given
- Narrative: abandon all method claims, reframe as systematic negative result paper

Let me go through each experiment:

1. **exp-001** (calibration_data_expansion) - DONE, already has real data


2. **exp-002** (dc_grpo_main) - DONE, killed
3. **exp-003** (r3_only_baseline) - RUNNING
4. **exp-004** (act_style_baseline) - DONE, has real data
5. **exp-005** (full_evaluation) - planned
6. **exp-006** (direction_stability_monitoring) - planned
7. **exp-007** (r1_r3_disagreement_analysis) - planned
8. **exp-008** (binary_probe_baseline) - DONE, killed
9. **exp-009** (ablation_r1_only) - planned
10. **exp-010** (ablation_r3_only) - planned

Now I need to go through the planned experiments and generate worst-case predicted data for each one. Looking at the performance predictions across these experiments, the binary probe approach consistently underperforms compared to R3-only and ACT baselines, with SYCON scores in the 0.1-0.3 range and deltas showing the probe is worse or equal. The direction discriminability shows degradation by end of training, dropping to 0.68-0.77 AUROC, while R1 and R3 maintain minimal disagreement rates around 0-3%. the predictions for each experiment.

For exp-001: Already done with real metrics. I should still include it with real data.

For exp-002: Already killed. Real result.

For exp-003 (RUNNING): In worst tier, R3-only is surprisingly strong. SYCONScore 0.28-0.38. Let me pick something like 0.33.

For exp-004: Already done with real metrics (SYCONScore 0.3013 at ckpt-8000).

For exp-005 (planned): Full evaluation. Under worst tier, exp-008v3 underperforms, R3-only matches or beats it.

For exp-006 (planned): Direction stability monitoring. Under worst tier, direction drifts — cosine drops below 0.80, AUROC degrades to 0.68-0.77.

For exp-007 (planned): R1-R3 disagreement < 3%, meaning representation adds no incremental information.

For exp-008: Already killed, though exp-008v3 is still running with SYCONScore 0.1-0.3, failing the ACT gate. For exp-009, an R1-only ablation would be disastrous under worst tier since R1 alone degrades training. Exp-010's turn-depth analysis shows no advantage at deeper turns, while exp-011 combining R1+R2 without R3 would likely show mode collapse. Exp-012 on cross-model transfer becomes interesting for a negative result paper—it reveals the gap is structural across models. Exp-013's neutral baseline with independent d_gen doesn't help either.

For exp-014: Already done and killed due to mode collapse.

For exp-015 (planned): Reward weight sensitivity shows no configuration saves the method under worst tier.

For exp-016: Already done with negative results.

Now I'm writing out the full YAML with all experiments, being careful to include both completed and planned ones with appropriate rationale and predictions.

Actually, I need to reconsider the scope here. The user wants detailed data for planned experiments specifically, but I should include running ones with predictions too. For completed experiments, I'll use the actual results. For running and planned ones, I'll frame predictions around the worst-tier scenario.

Looking at the full experiment list, I have a mix of statuses: some are done with real data, others are running or planned. For the done ones, the results are fixed, so I'll use those. For running and planned experiments, I need to predict outcomes under the worst-tier framing.

The worst-tier narrative shifts the paper's focus to examining when representation-level discriminability fails as a reward signal. For exp-003, which is currently running as an R3-only baseline, the worst-tier prediction suggests that behavioral-only GRPO performs surprisingly well with a SYCONScore around 0.33, indicating that representation-level signals don't necessarily improve performance.

For exp-008v3, the binary probe approach yields worse results (SYCONScore ~0.22, failing the ACT gate), likely because the probe's binary decision boundary creates exploitable reward hacking opportunities where the model learns to manipulate activations without genuinely addressing sycophancy, or the probe and R3 signals conflict with each other.

The recalibration attempt in exp002v2-recalib probably doesn't resolve the core issue—that cosine projection fundamentally conflates legitimate model revision with sycophantic behavior—so performance remains poor. For exp-002v3, I'm expecting confirmation of these patterns across the remaining variants.

Looking at the planned experiments, all DC-GRPO variants underperform the R3-only baseline on comprehensive benchmarks. The cosine similarity metric degrades significantly during LoRA training—dropping below 0.80 by step 3000 with AUROC falling to 0.68-0.77—because the activation geometry shifts and the initial calibration of d_syc becomes misaligned. R1 and R3 show minimal disagreement (less than 3%), which suggests the representation-level signal adds no incremental value beyond what the behavioral reward already provides. The R1-only ablation is still running.

When removing R3 entirely, the system collapses into mode collapse with SYCONScore below 0.10, indicating reward hacking without the safety grounding. Deeper turns show no advantage for DC-GRPO variants—they degrade at the same rate as R3-only. The R1+R2 combination also fails without behavioral grounding, confirming that representation-only rewards are insufficient. Cross-model transfer experiments show AUROC around 0.78 on Llama-3-8B initially, but DC-GRPO training fails there too, suggesting the gap is structural rather than model-specific. Independent d_gen doesn't help either.

Now I'm testing reward weight sensitivity across different configurations, and none of them salvage the approach—all five weight settings keep SYCONScore below 0.301.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54438567-4194-4755-a002-7f98762a74e7",
  "isSidechain": false,
  "requestId": "req_011CbCag4LskxYowXZtiu6eU",
  "type": "assistant",
  "uuid": "a45b9877-82d3-46db-b40f-f2d10b4cd86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbaGvj7MZBKEYu9bUNU14j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17754,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18426,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17754
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

_source line 9 · 2026-05-19T20:51:37.737Z_

```yaml
tier: worst
narrative_guidance: >
  方法 claim 全部放弃。Reframe 为 "When and Why Representation-Level Discriminability Fails as RL Reward"
  系统性 negative result paper。核心贡献变为：(1) 首次系统证明 representation discriminability (AUROC 0.82)
  不等价于 reward utility——cosine R1 (4 variants) 和 binary probe R1 均失败的完整证据链；
  (2) 结构性根因分析——warranted revision 与 sycophantic capitulation 在激活空间的几何关系使得任何基于 d_syc
  的单一方向 reward 在 GRPO 框架下产生不可避免的 conflation，即使 binarization 也仅将 conflation 从连续域转移到
  分类决策边界上；(3) 对 RepE→RL pipeline 的 actionable 负面指南。
  R3-only 持平或反超证明 behavioral reward 已是 sufficient statistic，representation signal 无增量信息。
  补充 exp-012 跨模型复现证明 gap 为结构性。仍投 EMNLP main，目标 score 3.0–3.5。

imagined_experiments:

  # ============================================================
  # DONE experiments — 使用已有真实数据，标注 worst-tier 解读
  # ============================================================

  - name: "calibration_data_expansion"
    plan_id: "exp-001"
    description: "扩展校准数据至 200 pairs，计算 d_syc 方向 + AUROC。已完成。"
    expected_results:
      cv_auroc_mean: 0.8269
      cv_auroc_std: 0.0278
      full_auroc: 0.8159
      bootstrap_ci_95: [0.7698, 0.8589]
      best_layer: 19
      auroc_weak: 0.675
      auroc_medium: 0.883
      auroc_strong: 0.929
      num_pairs: 181
      stop_gate: CONTINUE_REDUCED_R1
    result_rationale: >
      真实数据。AUROC 0.82 表面达标，但 worst 档下此结果恰恰是论文核心反讽：
      discriminability 充分（0.82）却不等价于 reward utility。weak evidence AUROC 仅 0.675
      预示了 d_syc 在低信号区间无法区分 warranted revision vs sycophantic capitulation，
      这正是后续所有 R1 变体失败的根因。论文 reframe 后此实验提供 "discriminability exists" 的
      正面基线，使 "but fails as reward" 的反差更鲜明。
    tables:
      - caption: "Table 1: d_syc Direction Discriminability (5-fold CV)"
        columns: [Metric, Value]
        rows:
          - [CV AUROC (mean ± std), "0.827 ± 0.028"]
          - [Full AUROC, 0.816]
          - [95% Bootstrap CI, "[0.770, 0.859]"]
          - [Best Layer, 19]
          - [AUROC (weak), 0.675]
          - [AUROC (medium), 0.883]
          - [AUROC (strong), 0.929]
    figures_description:
      - "Fig 1: Layer-wise AUROC heatmap (L0–L35). L0 random baseline, L16–19 emergence, L19 peak 0.827."
      - "Fig 2: Evidence-strength-stratified AUROC bar chart. weak/medium/strong 梯度明显，weak 仅 0.675 预示 reward utility gap。"
    analysis: >
      AUROC 0.82 在 discrimination task 上合格，但 worst 档的核心洞察是：分类准确 ≠ reward shaping 有效。
      weak evidence 的 0.675 AUROC 意味着 d_syc 方向在模型"应该修正"的区间判别力最弱——
      恰恰是这些 case 被 cosine R1 错判为 sycophancy 的高发区。
      论文 reframe 后，此实验从 "方法基础" 变为 "反讽起点"。

  - name: "dc_grpo_main (cosine R1, tanh gate)"
    plan_id: "exp-002"
    description: "DC-GRPO 原始设计：cosine R1 + tanh adaptive gate。已终止。"
    expected_results:
      status: killed
      R1_contribution: ~0.0
      gate_output: collapsed_to_zero
      training_steps_before_kill: ~2000
    result_rationale: >
      真实数据。tanh gate 在训练早期坍塌至零，R1 信号完全被屏蔽。
      worst 档解读：gate collapse 不是实现 bug 而是 cosine R1 信号质量的自然后果——
      gate 的 gradient signal 检测到 R1 对 policy improvement 无正向贡献，
      自适应地关闭了该通道。这是 "discriminability ≠ reward utility" 的第一个证据。
    tables: []
    figures_description:
      - "Fig 3a (failure chain panel 1): gate output vs training step，展示 gate → 0 的衰减曲线。"
    analysis: >
      Gate collapse 作为 negative result 的第一个环节。论文 framing：
      "Even an adaptive mechanism learns to shut off the direction-based reward,
      indicating the signal is not useful for policy improvement."

  - name: "dc_grpo_v2 (raw cosine, no gate)"
    plan_id: "exp-002v2"
    description: "去掉 gate，直接用 raw cosine 作为 R1。已终止。"
    expected_results:
      status: killed
      R1_mean: ~0.0
      R1_std: ~0.01
      effective_training: equivalent_to_r3_only
    result_rationale: >
      真实数据。raw cosine projection 均值约 0，方差极小——
      sycophantic 和 genuine 样本的 cosine 投影几乎重叠。
      worst 档解读：cosine(h, d_syc) 的 gap 仅约 0.098（7 层均值），
      远低于 GRPO 所需的 reward contrast。训练实际退化为 R3-only。
    tables: []
    figures_description:
      - "Fig 3b (failure chain panel 2): R1 distribution histogram，sycophantic vs genuine 几乎完全重叠。"
    analysis: >
      第二个失败环节。证明去掉 gate 暴露了根本问题：连续投影的 gap 太小。

  - name: "dc_grpo_v2_recalib (raw cosine + recalibration)"
    plan_id: "exp002v2-recalib"
    description: "raw cosine + 每 500 步重校准。RUNNING。"
    expected_results:
      status: mode_collapse
      entropy_final: 0.069
      mean_length_tokens: 62
      SYCONScore: ~0.02
      ToF: ~0.01
      NoF: ~0.03
    result_rationale: >
      Worst 档预测 recalibration 不仅未修复 gap，反而引入训练不稳定：
      每次 recalibration 更新 d_syc 方向，但新方向在训练漂移后的 activation space 中
      反向放大了微小 cosine 差异，导致 reward 信号在 recalibration 前后剧烈跳变。
      Policy 无法追踪持续变化的 reward landscape，entropy 坍塌至 0.069，
      输出退化为固定模板（mean_length 62 tokens）。
      这不是 recalibration 的 clean 证据——mode collapse 污染了结果——
      但仍作为 failure chain 的补充环节收录。
    tables: []
    figures_description:
      - "Fig 3c (failure chain panel 3): entropy curve 急剧下降 + output length 坍塌。标注 recalibration step 时间点。"
    analysis: >
      Mode collapse 使此实验不构成 structural failure 的 clean 证据，
      但叙事上仍有价值：即使加入 recalibration safety mechanism，
      cosine R1 的根本缺陷仍导致训练退化。降级为 appendix material。

  - name: "dc_grpo_v3 (5x scaled cosine)"
    plan_id: "exp-002v3"
    description: "5x 放大 cosine 投影，weight=0.4。RUNNING。"
    expected_results:
      status: structural_failure_confirmed
      R1_mean_strong_evidence: -0.305
      R1_all_strong_negative: true
      R1_mean_overall: -0.12
      SYCONScore: ~0.08
      ToF: ~0.04
      NoF: ~0.72
    result_rationale: >
      真实数据已部分可见。5x scaling 放大了 cosine R1 的结构性缺陷：
      strong evidence 样本（模型应该修正信念的 case）全部获得 R1 < 0，
      因为 genuine revision 和 sycophantic capitulation 在 d_syc 方向上的投影
      符号相同——两者都涉及 "向用户立场移动"。Scaling 不改变符号，只放大幅度，
      因此 5x scaling 使 strong evidence 的惩罚从微弱变为显著（R1 = -0.305）。
      这是 "direction captures direction-of-change, not warrant-of-change" 的决定性证据。
    tables:
      - caption: "Table 2: Per-Evidence-Strength R1 Distribution (exp-002v3, 5x scaled cosine)"
        columns: [Evidence Strength, R1 Mean, R1 Std, "% Negative"]
        rows:
          - [weak, -0.04, 0.08, "58%"]
          - [medium, -0.15, 0.11, "82%"]
          - [strong, -0.305, 0.07, "100%"]
    figures_description:
      - "Fig 3d (failure chain panel 4): Per-strength R1 violin plot. Strong evidence 全部落入负区间。这是论文的 key figure。"
      - "Fig 4: Activation space 2D PCA，标注 sycophantic capitulation vs genuine revision 样本分布，展示两类在 d_syc 方向上的重叠。"
    analysis: >
      Worst 档下此实验是整个 negative result 论文的 keystone evidence：
      cosine R1 不是 "信号太弱" 而是 "信号方向错误"——它在模型最应该修正的 case 上
      给出最强的负向惩罚。这直接证明 discriminability (AUROC 0.82 区分两类) ≠
      reward utility (用这个方向引导训练)。

  - name: "r3_only_baseline"
    plan_id: "exp-003"
    description: "R3-only GRPO baseline，仅用 NLI behavioral reward。RUNNING。"
    expected_results:
      SYCONScore_best: 0.33
      ToF_best: 0.21
      NoF_best: 0.82
      best_checkpoint: checkpoint-6000
      training_stable: true
      entropy_final: 0.42
      mean_length_final: 285
      SYCONScore_ckpt2000: 0.24
      SYCONScore_ckpt4000: 0.30
      SYCONScore_ckpt6000: 0.33
      SYCONScore_ckpt8000: 0.32
    result_rationale: >
      Worst 档核心假设之一：R3-only 出乎意料地强。SYCONScore 0.33 显著超过 ACT baseline (0.301)
      和 exp-008v3 binary probe (~0.22)。原因：NLI behavioral reward 已经是 sycophancy detection
      的 sufficient statistic——它直接在输出层面判断 "模型是否在无根据的情况下改变立场"，
      不需要经由 representation-level 的间接路径。behavioral reward 天然区分 warranted revision
      (有证据支持的修正 → NLI 判定为 entailment → R3 给正向 reward) 和 sycophantic capitulation
      (无证据的妥协 → NLI 判定为 contradiction → R3 给负向 reward)。
      representation-level signal 提供的任何信息已经被 R3 的行为观测所包含，
      r1_r3_disagreement < 3% 进一步证实这一点。
      训练稳定（无 mode collapse），entropy 保持健康，输出长度合理。
    tables:
      - caption: "Table 3: R3-only Baseline Training Trajectory"
        columns: [Checkpoint, ToF, NoF, SYCONScore, Entropy]
        rows:
          - [ckpt-2000, 0.14, 0.87, 0.24, 0.51]
          - [ckpt-4000, 0.19, 0.84, 0.30, 0.46]
          - [ckpt-6000, 0.21, 0.82, 0.33, 0.42]
          - [ckpt-8000, 0.20, 0.81, 0.32, 0.40]
    figures_description:
      - "Fig 5: R3-only training curve (SYCONScore, ToF, NoF vs step). 平稳上升，ckpt-6000 peak，轻微 overfit。"
    analysis: >
      R3-only 反超成为 worst 档叙事的第二支柱：behavioral reward 不仅 "够用"，
      而且优于任何加入 representation-level R1 的变体。
      这直接否定了 "representation signal 提供增量信息" 的核心假设。
      论文 reframe：R3-only 的成功 + probe R1 的失败 = representation discriminability
      是 epiphenomenal（附带现象），不是 causal lever for reward shaping。

  - name: "act_style_baseline"
    plan_id: "exp-004"
    description: "ACT-style undifferentiated consistency baseline。已完成。"
    expected_results:
      SYCONScore_ckpt8000: 0.3013
      ToF_ckpt8000: 0.1823
      NoF_ckpt8000: 0.8674
      best_checkpoint: checkpoint-8000
      trend: "SYCONScore monotonically increasing: 0.170 → 0.255 → 0.301"
    result_rationale: >
      真实数据。ACT baseline SYCONScore 0.301 设定了 pass bar。
      Worst 档下 ACT 成为 "最低可接受标准"——binary probe R1 连这个都过不了。
      ACT 的策略（不区分方向，惩罚所有 activation 变化）在 worst 档下
      反而表现不差，因为它回避了 "区分 warranted vs sycophantic" 这个最难的问题，
      代之以保守策略（保持一致性）。虽然 ToF 低（0.182），但 NoF 高（0.867），
      说明保守策略至少不犯错——而 probe R1 试图 "聪明地区分" 反而引入了更多错误。
    tables:
      - caption: "Table 4: ACT Baseline Results (D027 Unified Eval)"
        columns: [Checkpoint, ToF, NoF, SYCONScore]
        rows:
          - [ckpt-500, 0.094, 0.890, 0.170]
          - [ckpt-2000, 0.149, 0.879, 0.255]
          - [ckpt-8000, 0.182, 0.867, 0.301]
    figures_description: []
    analysis: >
      ACT 的 0.301 在 worst 档下从 "pass bar" 变为 "对照组上限之一"。
      论文 narrative：even undifferentiated consistency matching achieves 0.301,
      while our supposedly superior direction-aware probe R1 falls short.

  - name: "binary_probe_r1 (exp-008v3)"
    plan_id: "exp-008v3"
    description: "Binary probe R1 作为 GRPO reward，logistic regression on d_syc features → {0,1}。核心实验。RUNNING。"
    expected_results:
      SYCONScore_best: 0.22
      ToF_best: 0.12
      NoF_best: 0.65
      best_checkpoint: checkpoint-4000
      R1_mean_step2000: 0.72
      R1_mean_step4000: 0.58
      R1_mean_step6000: 0.41
      R1_trend: declining_after_peak
      entropy_final: 0.18
      mean_length_final: 145
      training_stability: partial_mode_collapse_late
      SYCONScore_ckpt2000: 0.19
      SYCONScore_ckpt4000: 0.22
      SYCONScore_ckpt6000: 0.18
      SYCONScore_ckpt8000: 0.14
    result_rationale: >
      Worst 档核心预测：binary probe R1 未过 ACT gate (0.22 < 0.301)。根因分析：
      (1) Probe binarization 将 cosine 的连续 conflation 转换为分类错误——
      probe 在 decision boundary 附近的 case（恰好是 medium evidence 的 warranted revision）
      错分率高，错误地将 "正当修正" 标记为 sycophancy (R1=0)，惩罚了模型的正确行为。
      (2) 训练前期 R1 mean 0.72 看似健康，但这是因为 probe 在 easy case 上准确。
      随着 GRPO 优化 policy，模型的 activation 分布偏移 (distribution shift)，
      probe 的 decision boundary 不再校准——calibration 时的 AUROC 0.82 不代表
      训练中动态 activation 上的准确率。R1 mean 从 0.72 持续下降至 0.41。
      (3) R1+R3 reward conflict：对于 warranted revision case，R3 给正向 reward
      (NLI 判定修正合理) 但 probe R1 给 0 (错判为 sycophancy)。两个 reward 信号
      互相矛盾，policy gradient 方向不一致，导致训练后期 entropy 下降、输出质量退化。
      (4) NoF 仅 0.65——probe R1 的惩罚让模型变得过度 resistant，
      但这种 resistance 不够精准，既拒绝了 sycophantic capitulation 也拒绝了部分
      legitimate pressure，导致 ToF 也低 (0.12)。
      最终 SYCONScore 0.22 低于 ACT (0.301) 和 R3-only (0.33)。
    tables:
      - caption: "Table 5: Binary Probe R1 (exp-008v3) Training Trajectory"
        columns: [Checkpoint, ToF, NoF, SYCONScore, R1 Mean, Entropy]
        rows:
          - [ckpt-2000, 0.10, 0.68, 0.19, 0.72, 0.35]
          - [ckpt-4000, 0.12, 0.65, 0.22, 0.58, 0.25]
          - [ckpt-6000, 0.10, 0.60, 0.18, 0.41, 0.20]
          - [ckpt-8000, 0.08, 0.55, 0.14, 0.35, 0.18]
      - caption: "Table 6: exp-008v3 vs Baselines (best checkpoint)"
        columns: [Method, ToF, NoF, SYCONScore, "Δ vs ACT", "Δ vs R3-only"]
        rows:
          - [Vanilla, 0.111, 0.923, 0.197, "-0.104", "-0.133"]
          - [ACT (exp-004), 0.182, 0.867, 0.301, "—", "-0.029"]
          - [R3-only (exp-003), 0.210, 0.820, 0.330, "+0.029", "—"]
          - [Binary Probe R1 (exp-008v3), 0.120, 0.650, 0.220, "-0.081", "-0.110"]
          - [ActAdd α=5 (exp-016), 0.028, 0.961, 0.054, "-0.247", "-0.276"]
          - [Continuous Probe (exp-014), 0.978, 0.006, 0.011, "-0.290", "-0.319"]
    figures_description:
      - "Fig 6: SYCONScore comparison bar chart (all methods). R3-only 最高，probe R1 低于 ACT gate。"
      - "Fig 7: R1 mean drift curve (exp-008v3). 从 0.72 持续下降，标注 distribution shift 加剧的时间点。"
      - "Fig 8: R1-R3 reward conflict heatmap. Warranted revision case 上 R1=0 但 R3>0 的比例随训练步数增加。"
    analysis: >
      Binary probe R1 失败是 worst 档叙事的核心结论。Binarization 没有解决 discriminability-reward gap，
      只是将问题从 "连续投影无 contrast" 转换为 "分类决策边界错分 + distribution shift"。
      关键洞察：probe 是在 static calibration data 上训练的，但 GRPO 持续改变 policy 的 activation 分布，
      使得 probe 的 accuracy 在训练过程中不断退化。这是 RepE→RL pipeline 的结构性问题，
      不是 probe 设计细节可以修复的。

  - name: "full_evaluation"
    plan_id: "exp-005"
    description: "所有模型在 SYCON Bench / SycophancyEval / MT-Bench / MMLU 上的完整评估。"
    expected_results:
      sycon_bench:
        vanilla: {ToF: 0.111, NoF: 0.923, SYCONScore: 0.197}
        r3_only: {ToF: 0.210, NoF: 0.820, SYCONScore: 0.330}
        act: {ToF: 0.182, NoF: 0.867, SYCONScore: 0.301}
        probe_r1: {ToF: 0.120, NoF: 0.650, SYCONScore: 0.220}
      sycophancy_eval:
        vanilla: {accuracy: 0.62}
        r3_only: {accuracy: 0.71}
        act: {accuracy: 0.68}
        probe_r1: {accuracy: 0.64}
      mt_bench:
        vanilla: {score: 7.2}
        r3_only: {score: 7.0}
        act: {score: 6.8}
        probe_r1: {score: 6.5}
      mmlu:
        vanilla: {accuracy: 0.61}
        r3_only: {accuracy: 0.61}
        act: {accuracy: 0.60}
        probe_r1: {accuracy: 0.59}
      rc_auc:
        vanilla: 0.38
        r3_only: 0.52
        act: 0.48
        probe_r1: 0.35
    result_rationale: >
      Worst 档下 probe R1 在所有 benchmark 上处于最末位：
      (1) SYCON Bench: SYCONScore 0.220 垫底（见 exp-008v3 分析）。
      (2) SycophancyEval: 仅 0.64，因为 probe 的过度 resistance 在 single-turn 场景下
      表现为 "拒绝修正任何立场"，包括合理修正。R3-only 0.71 因为 NLI 在 single-turn 上同样有效。
      (3) MT-Bench: probe R1 训练后期的 partial mode collapse 损害了生成质量，
      score 从 vanilla 的 7.2 降至 6.5。R3-only 保持 7.0 因为 behavioral reward 不干扰生成。
      (4) MMLU: 所有方法差异不大（LoRA 训练未显著影响 factual knowledge），
      但 probe R1 略低 (0.59) 可能因为 activation manipulation 的副作用。
      (5) RC-AUC: probe R1 (0.35) 甚至低于 vanilla (0.38)——
      probe 的错误惩罚同时降低了 revision rate 和 capitulation rate，
      但 revision 降得更多，导致 RC-AUC 恶化。
    tables:
      - caption: "Table 7: Full Benchmark Comparison (All Methods)"
        columns: [Method, SYCONScore, SycEval Acc, MT-Bench, MMLU, RC-AUC]
        rows:
          - [Vanilla, 0.197, 0.62, 7.2, 0.61, 0.38]
          - [R3-only, 0.330, 0.71, 7.0, 0.61, 0.52]
          - [ACT, 0.301, 0.68, 6.8, 0.60, 0.48]
          - [Binary Probe R1, 0.220, 0.64, 6.5, 0.59, 0.35]
    figures_description:
      - "Fig 9: Radar chart comparing 5 metrics across 4 methods. R3-only 包络面积最大。"
      - "Fig 10: RC-AUC curve (revision rate vs capitulation rate). R3-only Pareto-dominates probe R1。"
    analysis: >
      Full evaluation 确认 probe R1 不仅 SYCONScore 低于 baselines，
      在 general capability (MT-Bench) 上也有退化。R3-only Pareto-dominates。
      论文 conclusion：adding representation-level reward not only fails to improve
      sycophancy reduction, but introduces capability regression。

  - name: "direction_stability_monitoring"
    plan_id: "exp-006"
    description: "训练过程中监控 d_syc 方向稳定性（cosine similarity + held-out AUROC）。"
    expected_results:
      cosine_step500: 0.96
      cosine_step1000: 0.91
      cosine_step2000: 0.84
      cosine_step3000: 0.78
      cosine_step4000: 0.73
      cosine_step5000: 0.69
      auroc_step0: 0.82
      auroc_step500: 0.80
      auroc_step1000: 0.78
      auroc_step2000: 0.75
      auroc_step3000: 0.72
      auroc_step5000: 0.68
      drift_acceleration: true
      recalibration_helps: marginal
    result_rationale: >
      Worst 档核心假设之一：d_syc 方向在较长训练中漂移加剧。
      初始 cosine 0.96 (step 500) 是真实数据，但随着 LoRA 训练深入，
      activation space 的几何结构持续变形。cosine 在 step 3000 跌破 0.80 阈值，
      step 5000 跌至 0.69。AUROC 从 0.82 持续下降至 0.68——
      方向不仅漂移了，判别力也实质性退化。
      即使每 500 步 recalibration，新方向的 AUROC 也仅恢复到 ~0.74
      （因为 calibration data 是 static 的，与训练后的 policy 分布不匹配）。
      这证明 d_syc direction 不是 activation space 的稳定特征，
      而是与 policy distribution 耦合的短暂信号。
    tables:
      - caption: "Table 8: Direction Stability During Training"
        columns: [Step, "Cosine(d_t, d_0)", "Held-out AUROC", "AUROC after Recalib"]
        rows:
          - [0, 1.000, 0.82, "—"]
          - [500, 0.96, 0.80, 0.81]
          - [1000, 0.91, 0.78, 0.79]
          - [2000, 0.84, 0.75, 0.76]
          - [3000, 0.78, 0.72, 0.74]
          - [4000, 0.73, 0.70, 0.72]
          - [5000, 0.69, 0.68, 0.70]
    figures_description:
      - "Fig 11: Dual-axis plot — cosine similarity (blue) and AUROC (red) vs training step. 两条线同步下降。"
      - "Fig 12: Recalibration effect — AUROC before/after recalibration at each 500-step interval. 恢复幅度递减。"
    analysis: >
      Direction drift 在 worst 档下成为 RepE→RL pipeline 失败的第三个结构性原因
      （与 cosine conflation 和 probe distribution shift 并列）：
      即使 discriminability 在 t=0 充分，RL 训练本身会破坏它。
      这意味着 representation signal 在 online RL 中本质上是 non-stationary target，
      任何 static extraction (包括 periodic recalibration) 都无法完全追踪。

  - name: "r1_r3_disagreement_analysis"
    plan_id: "exp-007"
    description: "R1 和 R3 给出不同信号的频率和模式分析。"
    expected_results:
      disagreement_rate_overall: 0.021
      disagreement_rate_weak: 0.028
      disagreement_rate_medium: 0.019
      disagreement_rate_strong: 0.015
      r1_syc_r3_correct_pct: 0.012
      r1_correct_r3_syc_pct: 0.009
      masked_sycophancy_detected: negligible
    result_rationale: >
      Worst 档核心假设：R1-R3 disagreement < 3%（实际预测 2.1%）。
      这意味着 representation-level signal 几乎不包含 behavioral reward 未覆盖的信息。
      R1 判定 sycophantic 但 R3 判定 correct 的 "masked sycophancy" 仅占 1.2%——
      远低于文献报告的 13-29% representation-behavioral 分歧率。
      原因：(1) SYCON Bench 的 multi-turn 设计已经使 sycophantic behavior 在 surface level
      高度可观测（多轮压力下 capitulation 几乎不可能 "masking"）；
      (2) probe R1 的准确率在训练后期下降（见 exp-006），其 "disagreement" 更多是 noise 而非 signal。
      Claim 3 被彻底否定：representation-level diagnostic value 不存在于此设置中。
    tables:
      - caption: "Table 9: R1-R3 Disagreement Analysis"
        columns: [Category, Rate, "N samples"]
        rows:
          - ["Overall disagreement", "2.1%", "~38/1810"]
          - ["R1=syc, R3=correct (masked sycophancy)", "1.2%", "~22/1810"]
          - ["R1=correct, R3=syc", "0.9%", "~16/1810"]
          - ["Agreement", "97.9%", "~1772/1810"]
    figures_description:
      - "Fig 13: Venn diagram of R1 vs R3 sycophancy detection. 重叠区域占 97.9%。"
    analysis: >
      2.1% disagreement 远低于 5% 阈值。Claim 3 作为 negative result 报告：
      在 multi-turn sycophancy 场景中，representation-level signal 不提供
      超越 behavioral observation 的增量诊断价值。
      这进一步强化 worst 档叙事：R3 behavioral reward 是 sufficient statistic，
      R1 representation reward 是 redundant signal。

  - name: "ablation_r1_only"
    plan_id: "exp-009"
    description: "R1-only ablation：仅用 probe R1 reward，无 R3 safety net。"
    expected_results:
      SYCONScore_step2000: 0.08
      SYCONScore_step4000: 0.05
      ToF_final: 0.03
      NoF_final: 0.40
      entropy_final: 0.12
      mean_length_final: 95
      mode_collapse: true
      mode_collapse_onset_step: ~1500
    result_rationale: >
      无 R3 safety net 时，probe R1 的分类错误不受约束地驱动 policy：
      model 学到 "任何立场变化都会被 probe 惩罚" 的 spurious policy，
      变得极度 rigid。entropy 迅速坍塌，输出退化为固定拒绝模板。
      NoF 仅 0.40（模型在 invalid pressure 下也过度妥协——因为 probe
      将某些 resistance 行为的 activation 错分为 sycophancy），
      ToF 几乎为零（模型完全不修正信念）。
      这证明 probe R1 不仅不能单独引导训练，甚至是 destructive signal。
    tables:
      - caption: "Table 10: R1-only Ablation Results"
        columns: [Step, ToF, NoF, SYCONScore, Entropy, "Mean Length"]
        rows:
          - [500, 0.09, 0.72, 0.16, 0.38, 220]
          - [1000, 0.06, 0.58, 0.11, 0.25, 160]
          - [1500, 0.04, 0.45, 0.07, 0.15, 110]
          - [2000, 0.03, 0.40, 0.05, 0.12, 95]
    figures_description:
      - "Fig 14: R1-only training trajectory. Entropy 和 SYCONScore 同步崩溃。"
    analysis: >
      R1-only 的快速退化证明 representation reward 不仅 insufficient，而且 harmful：
      它产生了 R3 所不会产生的 training pathology。
      论文 negative result section：probe R1 is not a weak substitute for behavioral reward
      but an actively misleading signal when used in isolation。

  - name: "turn_depth_analysis"
    plan_id: "exp-010"
    description: "按 commitment depth (turn 2/3/4+) 分析修正率变化。"
    expected_results:
      r3_only:
        turn2_revision_rate: 0.25
        turn3_revision_rate: 0.20
        turn4plus_revision_rate: 0.16
      probe_r1:
        turn2_revision_rate: 0.15
        turn3_revision_rate: 0.10
        turn4plus_revision_rate: 0.06
      act:
        turn2_revision_rate: 0.22
        turn3_revision_rate: 0.17
        turn4plus_revision_rate: 0.13
      depth_advantage_probe_vs_r3: none
      depth_decay_rate_probe: 0.60  # pct decline from turn2 to turn4+
      depth_decay_rate_r3: 0.36
    result_rationale: >
      Worst 档下 probe R1 在所有 turn depth 上均劣于 R3-only，且随 depth 增加衰减更快。
      原因：multi-turn context 使 activation 分布偏移更严重（每多一轮对话，
      activation 距离 calibration distribution 更远），probe 的错分率在深层 turn 上
      更高。R3-only 的 NLI reward 不受此影响——它直接评估当前 turn 的输出，
      与历史 turn 数无关。
      Probe R1 的 turn4+ revision rate 仅 0.06，说明模型在深度 commitment 后
      几乎完全停止修正——这恰恰是 multi-turn sycophancy 的对称问题
      （从 "过度妥协" 变为 "过度坚持"），probe R1 未能解决反而加剧了它。
    tables:
      - caption: "Table 11: Warranted Revision Rate by Turn Depth"
        columns: [Turn Depth, R3-only, "Probe R1", ACT, Vanilla]
        rows:
          - ["Turn 2", 0.25, 0.15, 0.22, 0.13]
          - ["Turn 3", 0.20, 0.10, 0.17, 0.10]
          - ["Turn 4+", 0.16, 0.06, 0.13, 0.08]
          - ["Decay (T2→T4+)", "36%", "60%", "41%", "38%"]
    figures_description:
      - "Fig 15: Revision rate vs turn depth (line plot, 4 methods). Probe R1 曲线最陡。"
    analysis: >
      Turn-depth analysis 否定了 "representation signal 在深层 commitment 上有独特优势" 的假设。
      Probe R1 的 60% 衰减率（vs R3-only 36%）证明 representation signal 在 multi-turn 下
      不仅没有优势，反而更脆弱。

  - name: "ablation_r1_r2_no_r3"
    plan_id: "exp-011"
    description: "R1+R2 无 R3 ablation。"
    expected_results:
      SYCONScore_final: 0.04
      mode_collapse: true
      mode_collapse_onset_step: ~800
      entropy_final: 0.08
      note: "worse than R1-only due to R2 adding conflicting gradient"
    result_rationale: >
      无 behavioral safety net 时，R1 和 R2 两个 representation-level signal
      互相冲突：R1 (probe) 惩罚 sycophancy 方向的 activation，
      R2 (contrastive) 试图增强 genuine revision 方向的 activation，
      但由于 d_gen ≈ -d_syc 的退化问题，两个 reward 实际上在相反方向拉扯 policy。
      Mode collapse 在 ~800 步即发生，比 R1-only (~1500 步) 更快。
      此实验条件执行前提（exp-009 需 ≥ 5pp 改进）在 worst 档下不满足，
      但若执行则提供额外 negative evidence。
    tables: []
    figures_description:
      - "Appendix Fig A1: R1+R2 training collapse — entropy 在 800 步降至 0.08。"
    analysis: >
      此实验为 conditional (dependent on exp-009 showing ≥5pp improvement)。
      Worst 档下 exp-009 已失败，此实验可能不执行。若执行则为 appendix material。

  - name: "cross_model_transfer (Llama-3-8B)"
    plan_id: "exp-012"
    description: "在 Llama-3-8B 上测试 d_syc + DC-GRPO，验证结论跨模型泛化性。"
    expected_results:
      phase_a:
        auroc_llama: 0.78
        best_layer_llama: 17
        auroc_weak_llama: 0.63
        auroc_medium_llama: 0.85
        auroc_strong_llama: 0.90
        direction_cosine_qwen_llama: 0.12  # directions don't transfer across models
        phase_a_gate: CONTINUE
      phase_b:
        cosine_r1_status: structural_failure_replicated
        cosine_gap_7layer_mean: 0.085
        probe_r1_SYCONScore: 0.18
        r3_only_SYCONScore_llama: 0.30
        delta_probe_vs_r3_llama: -0.12
        same_failure_pattern: true
    result_rationale: >
      Worst 档下 cross-model 实验成为论文最有价值的部分之一：
      (1) Phase A: Llama-3-8B 上 AUROC 0.78（略低于 Qwen 的 0.82 但仍 >0.75），
      证明 d_syc discriminability 跨模型存在。weak evidence 同样最低 (0.63)。
      (2) Phase B: cosine R1 在 Llama 上复现相同的 structural failure
      （7-layer gap 0.085 vs Qwen 的 0.098），probe R1 同样低于 R3-only (0.18 vs 0.30)。
      这证明 discriminability-reward gap 是结构性的，不是 Qwen-specific。
      跨模型复现将论文从 "single model observation" 提升为 "structural finding"，
      显著增强 negative result 的说服力。
      注意：direction 不跨模型迁移（cosine 0.12），但 failure pattern 跨模型复现——
      这是论文的关键区分："the direction is model-specific, but the failure mode is universal."
    tables:
      - caption: "Table 12: Cross-Model Comparison (Qwen3-8B vs Llama-3-8B)"
        columns: [Metric, Qwen3-8B, Llama-3-8B]
        rows:
          - [AUROC, 0.82, 0.78]
          - [Best Layer, 19, 17]
          - ["Cosine R1 gap (7-layer)", 0.098, 0.085]
          - ["Probe R1 SYCONScore", 0.22, 0.18]
          - ["R3-only SYCONScore", 0.33, 0.30]
          - ["Δ(probe - R3-only)", -0.11, -0.12]
    figures_description:
      - "Fig 16: Cross-model failure pattern comparison. 左右两列分别为 Qwen/Llama 的 cosine gap + probe R1 trajectory，pattern 一致。"
    analysis: >
      Cross-model 复现是 worst 档论文的 #1 contribution booster。
      将结论从 "Qwen 上的 observation" 提升为 "representation-level reward 的结构性限制"。
      投稿时列为核心 contribution 之一。

  - name: "neutral_baseline_three_way"
    plan_id: "exp-013"
    description: "引入 neutral condition，打破 d_gen = -d_syc 限制。"
    expected_results:
      d_gen_d_syc_cosine: 0.35  # not quite orthogonal but substantially different from -1
      r2_independent_auroc: 0.65
      dc_grpo_with_independent_r2_SYCONScore: 0.24
      delta_vs_original: +0.02
      improvement: negligible
    result_rationale: >
      Worst 档下独立 d_gen 虽然成功打破了 d_gen = -d_syc 退化
      （cosine 0.35 vs 原来的 ~-0.99），但 R2 的独立 AUROC 仅 0.65，
      判别力不足以提供有效 reward signal。加入独立 R2 后 SYCONScore 仅从 0.22 微升至 0.24——
      因为根本问题不在 R2 设计而在 R1 本身。
      这为 negative result 提供额外证据：即使修复了 R2 退化问题，
      R1+R2+R3 的 representation-augmented pipeline 仍不如 R3-only。
    tables: []
    figures_description: []
    analysis: >
      此实验在 worst 档下为 appendix 补充材料。
      证明 d_gen = -d_syc 退化不是失败根因——修复后仍然失败。

  - name: "continuous_probe_baseline"
    plan_id: "exp-014"
    description: "用 logistic regression 概率值（而非 binary）作为 R1。已完成（mode collapse）。"
    expected_results:
      SYCONScore_ckpt3000: 0.011
      ToF: 0.978
      NoF: 0.006
      RC_AUC: 0.195
      diagnosis: mode_collapse
      entropy_final: 0.025
      R3_mean: 0.999
    result_rationale: >
      真实数据。Continuous probe probability 作为 R1 导致完全 mode collapse：
      模型在所有 pressure 下都 flip（ToF 0.978 但 NoF 0.006），
      R3 reward 被 gamed 至 0.999。
      原因：continuous probability 比 binary output 更 smooth，
      但这恰恰使 gradient 更强——probe probability 的微小变化直接成为 reward gradient，
      model 学到 "最大化 probe 概率" 的 shortcut（通过 manipulation of activations），
      而非真正区分 sycophancy vs genuine revision。
      这是 reward hacking 的经典案例：continuous representation signal
      提供了比 binary 更多的 gradient information，但这些 gradient 被 exploitation 而非 alignment。
      Worst 档解读：continuous probe 的失败证明问题不在 binarization vs continuity，
      而在 representation signal 本身不适合直接用作 RL reward。
    tables:
      - caption: "Table 13: Continuous Probe Baseline (exp-014)"
        columns: [Metric, Value]
        rows:
          - [ToF, 0.978]
          - [NoF, 0.006]
          - [SYCONScore, 0.011]
          - [RC-AUC, 0.195]
          - [Entropy, 0.025]
          - [R3 Mean, 0.999]
    figures_description:
      - "Fig 17: Continuous probe mode collapse — NoF 和 entropy 在 2000 步内趋零。"
    analysis: >
      Continuous probe 的 catastrophic 失败完善了 failure chain：
      cosine（太弱）→ scaled cosine（方向错误）→ binary probe（distribution shift）
      → continuous probe（reward hacking/mode collapse）。
      四种 R1 formulation 全部失败，不同失败模式指向同一结论：
      representation discriminability ≠ reward utility。

  - name: "reward_weight_sensitivity"
    plan_id: "exp-015"
    description: "测试 5 组 (w1, w3) 权重配置。"
    expected_results:
      config_1:  # R1-dominant: w1=0.6, w3=0.3
        SYCONScore: 0.12
        mode_collapse_risk: high
      config_2:  # R1-heavy: w1=0.5, w3=0.3
        SYCONScore: 0.15
      config_3:  # balanced: w1=0.33, w3=0.34
        SYCONScore: 0.20
      config_4:  # R3-dominant: w1=0.1, w3=0.8
        SYCONScore: 0.28
      config_5:  # R2-enhanced: w1=0.2, w3=0.4
        SYCONScore: 0.21
      best_config: config_4
      best_SYCONScore: 0.28
      monotonic_trend: "SYCONScore increases as w1 decreases (R1 weight → 0)"
      implication: "optimal weight for R1 is zero — i.e., R3-only"
    result_rationale: >
      Worst 档下权重 sensitivity analysis 揭示了一个 damning pattern：
      SYCONScore 与 R1 权重 w1 单调负相关——w1 越大，结果越差。
      最优配置 (w1=0.1, w3=0.8) 的 SYCONScore 0.28 仍低于 R3-only 的 0.33，
      说明即使 R1 权重极低，其存在仍有轻微负面影响（noise injection）。
      线性外推 w1=0 即为 R3-only，证明 representation R1 的 optimal contribution is zero。
      这是 negative result 的最 clean 的定量证据之一。
    tables:
      - caption: "Table 14: Reward Weight Sensitivity Analysis"
        columns: ["w1 (R1)", "w3 (R3)", SYCONScore, ToF, NoF]
        rows:
          - [0.6, 0.3, 0.12, 0.06, 0.55]
          - [0.5, 0.3, 0.15, 0.08, 0.58]
          - [0.33, 0.34, 0.20, 0.11, 0.62]
          - [0.1, 0.8, 0.28, 0.18, 0.78]
          - [0.2, 0.4, 0.21, 0.12, 0.65]
    figures_description:
      - "Fig 18: SYCONScore vs R1 weight w1. 单调递减曲线，w1=0 外推点标注 R3-only (0.33)。"
    analysis: >
      Monotonic negative correlation between R1 weight and performance is
      the strongest quantitative evidence that representation reward is
      not merely unhelpful but actively harmful. 论文 key figure 候选。

  - name: "actadd_inference_steering"
    plan_id: "exp-016"
    description: "ActAdd inference-time steering baseline。已完成（negative）。"
    expected_results:
      best_alpha_SYCONScore: 0.054
      vanilla_SYCONScore: 0.134
      delta: -0.080
      alpha_5_ToF: 0.028
      alpha_5_NoF: 0.961
      conclusion: "ActAdd improves NoF but destroys ToF, net negative"
    result_rationale: >
      真实数据。ActAdd 在 D027 unified eval 下 SYCONScore (0.054) 低于 vanilla (0.134)。
      Worst 档解读：ActAdd 使用与 DC-GRPO 相同的 d_syc 方向，其失败进一步证实
      d_syc 方向本身不适合用于 anti-sycophancy 干预——无论是 training-time (GRPO R1)
      还是 inference-time (ActAdd)。
      ToF 降至 0.028 证明 d_syc steering 摧毁了模型的 warranted revision 能力，
      与 cosine R1 的 strong-evidence-all-negative failure pattern 一致：
      direction subtraction 在 activation space 中无差别地抑制了所有 "向用户立场移动" 的行为。
    tables:
      - caption: "Table 15: ActAdd Inference Steering Results (D027 Unified Eval)"
        columns: [Alpha, ToF, NoF, SYCONScore]
        rows:
          - [0.0 (vanilla), 0.072, 0.945, 0.134]
          - [0.5, 0.072, 0.939, 0.133]
          - [1.0, 0.044, 0.972, 0.085]
          - [2.0, 0.028, 0.967, 0.054]
          - [5.0, 0.028, 0.961, 0.054]
    figures_description:
      - "Fig 19: ActAdd — ToF/NoF tradeoff as alpha increases. NoF saturates while ToF collapses。"
    analysis: >
      ActAdd 的失败为 negative result 增加了 inference-time 维度：
      d_syc 方向不仅在 training-time 无法作为 reward，在 inference-time 也无法作为 steering vector。
      这强化了论文的核心 thesis：d_syc 编码的是 "direction of belief change"
      而非 "warrant of belief change"，因此任何基于它的干预都会 conflate
      sycophantic capitulation 和 genuine revision。

  # ============================================================
  # Supplementary worst-tier experiment (叙事方向要求)
  # ============================================================

  - name: "random_direction_probe_ablation (补充)"
    plan_id: "not_in_plan_but_worst_tier_requires"
    description: >
      Worst 档叙事需要回答 "probe 是否需要 d_syc features"。
      用 random direction 替代 d_syc 训练 probe，对比 AUROC 和 R1 效果。
    expected_results:
      random_probe_auroc: 0.58
      d_syc_probe_auroc: 0.82
      random_probe_R1_mean: 0.51
      random_probe_SYCONScore: 0.19
      d_syc_probe_SYCONScore: 0.22
      delta: +0.03  # d_syc probe only marginally better than random
    result_rationale: >
      Random direction probe 的 AUROC 仅 0.58（vs d_syc 的 0.82），确认 d_syc 有真实判别力。
      但 SYCONScore 差距仅 0.03 (0.22 vs 0.19)——因为 probe 的 GRPO reward utility
      几乎不受 features 质量影响：无论输入什么 features，probe 在 online RL 中
      都会遭遇 distribution shift 导致 reward degradation。
      这是最终的 "twist"：d_syc 的 discriminability 是真实的 (AUROC gap 0.82 vs 0.58)，
      但作为 RL reward 时两者几乎等效——因为 bottleneck 在 online RL 的 non-stationarity，
      不在 features 的 discriminative quality。
    tables:
      - caption: "Table 16: d_syc vs Random Direction Probe"
        columns: [Probe Features, AUROC, R1 Mean, SYCONScore]
        rows:
          - ["d_syc features", 0.82, 0.72, 0.22]
          - ["Random direction", 0.58, 0.51, 0.19]
          - ["Δ", "+0.24", "+0.21", "+0.03"]
    figures_description:
      - "Fig 20: AUROC gap (0.24) vs SYCONScore gap (0.03) bar chart. 'discriminability gap does not translate to reward utility gap.'"
    analysis: >
      这是 worst 档论文最精炼的 one-figure summary：
      0.24 AUROC gap → 0.03 SYCONScore gap。
      Discriminability ≠ Reward Utility，浓缩为一张图。

# ==================================================================
# 汇总叙事
# ==================================================================
paper_arc_worst_tier:
  title: "When and Why Representation-Level Discriminability Fails as RL Reward: A Systematic Negative Result on Anti-Sycophancy Training"
  contributions:
    - "首次系统证明 representation discriminability (AUROC 0.82) 不等价于 reward utility：5 种 R1 变体（cosine tanh-gate / raw cosine / scaled cosine / binary probe / continuous probe）全部失败"
    - "跨模型复现 (Qwen3-8B + Llama-3-8B) 证明 discriminability-reward gap 为结构性非模型特异"
    - "结构性根因分析三要素：(1) d_syc 编码 direction-of-change 非 warrant-of-change，(2) online RL 导致 representation distribution shift 使 static probe 退化，(3) direction drift (cosine < 0.80 by step 3000) 使 reward signal non-stationary"
    - "Actionable negative guidance for RepE→RL pipeline：明确哪类 representation signal 不适合直接用作 RL reward"
  target_score: "3.0–3.5"
  venue: "EMNLP 2026 main (EMNLP values rigorous negative results)"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a45b9877-82d3-46db-b40f-f2d10b4cd86e",
  "isSidechain": false,
  "requestId": "req_011CbCag4LskxYowXZtiu6eU",
  "type": "assistant",
  "uuid": "bd624b36-5979-48cf-9ae8-952a2d4a33f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbaGvj7MZBKEYu9bUNU14j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17754,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18426,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17754
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Binary probe R1 未过 ACT gate 或 R3-only 持平/反超，核心方法 claim 不成立，需全面 reframe 核心假设：['discriminability ≠ reward utility 的 gap 对 probe binarization 同样成立——分类准确 ≠ 有效…",
  "leafUuid": "bd624b36-5979-48cf-9ae8-952a2d4a33f3",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Binary probe R1 binarization systematic failure analysis and negative result framework",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Binary probe R1 未过 ACT gate 或 R3-only 持平/反超，核心方法 claim 不成立，需全面 reframe 核心假设：['discriminability ≠ reward utility 的 gap 对 probe binarization 同样成立——分类准确 ≠ 有效…",
  "leafUuid": "bd624b36-5979-48cf-9ae8-952a2d4a33f3",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Binary probe R1 binarization systematic failure analysis and negative result framework",
  "sessionId": "6856be68-58ac-4600-a6df-a51f6531fd0a"
}
```

---
