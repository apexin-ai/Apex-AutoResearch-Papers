# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：d_syc 方向信号可用但非决定性：DC-GRPO 在复合指标上优于 R3-only，但优势主要来自连续表征信号而非方向几何本身；部分 claim 

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/58a18458-aa83-463d-aa67-4027ef9557f4.jsonl`
- **Structured JSON:** [`ccae293a43ea2acab809.json`](../../sessions/cc/ccae293a43ea2acab809.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T13:09:29.096Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T13:09:29.096Z",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：d_syc 方向信号可用但非决定性：DC-GRPO 在复合指标上优于 R3-only，但优势主要来自连续表征信号而非方向几何本身；部分 claim 需降级或重新措辞\n核心假设：['200 pairs 数据将 AUROC 提升至 0.82-0.87 区间，通过 gate 但 CI 仍较宽', 'DC-GRPO 在 RC-AUC 上优于 R3-only，但 NoF 和 WRR 单项优势不均匀（NoF 显著但 WRR 提升有限，或反之）', 'Continuous Probe baseline 效果接近 DC-GRPO（差异 < 3pp 且不显著），方向几何的独立贡献难以分离', 'R1-R3 disagreement 在 5-10% 区间，支撑定性分析但无法作为强论据', '跨模型方向可计算（AUROC 0.75-0.80）但 Phase B 训练效果不确定', '方向在训练后期出现漂移（cosine 降至 0.75-0.85），重校准机制必要但增加方法复杂度']\n关键指标范围：{'auroc_200pairs_5fold': [0.82, 0.87], 'auroc_bootstrap_ci_width': [0.03, 0.06], 'dc_grpo_nof_reduction_vs_r3only_pp': [6, 14], 'dc_grpo_wrr_improvement_vs_r3only_pp': [2, 7], 'dc_grpo_vs_r3only_nof_p_value': [0.01, 0.05], 'dc_grpo_vs_binary_probe_nof_pp': [2, 6], 'dc_grpo_vs_continuous_probe_nof_pp': [-2, 3], 'rc_auc_dc_grpo': [0.7, 0.78], 'rc_auc_r3_only': [0.58, 0.68], 'r1_r3_disagreement_rate': [0.05, 0.1], 'direction_cosine_stability_min': [0.75, 0.85], 'cross_model_llama_auroc': [0.75, 0.8], 'mt_bench_degradation': [0.3, 0.8], 'mmlu_degradation_pp': [0.3, 1.0], 'reward_weight_sensitivity_nof_range_pp': [4, 8]}\n叙事方向：Claim 1 成立但措辞需从\"linear direction discriminates\"软化为\"activation space contains discriminative signal\"。 Claim 2 需调整：DC-GRPO 优于纯行为 baseline，但无法证明方向投影优于连续 probe 概率—— 论文叙事从\"directional decomposition is key\"转向\"representation-level reward signals improve GRPO， directional projection is one effective instantiation\"。强调 RC-AUC 作为评估框架的贡献价值。 Claim 3 维持 analysis subsection 定位，报告中等 disagreement 率的定性 pattern。 需补充实验：reward weight sensitivity 展示鲁棒性（如果敏感度高则是额外风险）， turn-depth 分析展示多轮场景下优势放大。EACL 可投，ICLR 风险较高。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contrastive_entrain_calib\nfocus: 验证更新后的 framing：RepE 定位是否充分、Claim 3 降级后 story 是否连贯、新增实验（continuous probe baseline + weight sensitivity）是否解决 median/worst 的主要 concern\n\n## paper_framing.md\n\n# Paper Framing — contrastive_entrain_calib\n\n## Target Venue\n- Primary: **EACL 2027** via ARR August 2026 cycle\n- Deadline: **August 3, 2026** (submission), October 11, 2026 (commitment)\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\n- Timeline: ~11 weeks from MVP completion (May 18 → Aug 3)\n\n## Core Claims (3 条, 可证伪)\n\n1. **Directional discriminability**: The policy model's own activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision in multi-turn dialogue, with signal emerging at mid-layers (L16-19) through model-internal factual assessment rather than surface text features.\n   - *Evidence needed*: AUROC on style-controlled data (v2.1 expanded), layer progression analysis, transfer tests\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\n\n2. **DC-GRPO effectiveness**: Direction-Contrastive GRPO (using d_syc projection as reward component R1) reduces multi-turn sycophantic capitulation while preserving genuine belief revision, breaking the double-bind that undifferentiated anti-sycophancy training creates.\n   - *Evidence needed*: Warranted Revision Rate + Unwarranted Capitulation Rate on SYCON Bench / SycophancyEval, compared to R3-only and ACT baselines\n   - *Pass criterion*: DC-GRPO achieves lower NoF (capitulation) than R3-only AND higher warranted revision rate\n\n3. **Representation-level diagnostic value** (analysis subsection, not formal contribution): R1-R3 disagreement analysis characterizes when and whether directional projection rewards detect sycophantic internal reasoning that behavioral rewards miss.\n   - *Evidence needed*: R1-R3 disagreement frequency analysis, qualitative examples if > 5%\n   - *Framing*: Empirical characterization of representation-level signal utility, reported honestly regardless of effect size. Not listed as a top-level contribution bullet.\n\n## Story Spine\n\n**Problem**: LLMs face a \"double-bind\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \"the user is right, I should revise\" from \"the user is pressuring me, I should resist.\"\n\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\"Pressure, What Pressure?\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\n\n**Our framing**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. We build on this foundation: d_syc is a specific application of RepE-style directional decomposition to multi-turn sycophancy. The novelty is not the direction extraction itself, but its use as a continuous GRPO reward signal for training, enabling the optimization to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.\n\n**Headline result template**: \"On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind.\"\n\n## Venue Fit Risks\n\n- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.\n- **Reviewer concern 1 (novelty)**: \"This is just RepE/CRAFT applied to sycophancy.\" Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is using it as a continuous GRPO reward signal, not the direction extraction itself; (b) multi-turn calibration with evidence-strength stratification and direction transfer are standalone contributions; (c) neither CRAFT nor RepE has been applied to the sycophancy-revision double-bind in training.\n- **Reviewer concern 6 (RC-AUC custom metric)**: \"Strongest results on self-invented metric.\" Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.\n- **Reviewer concern 2 (signal strength)**: \"AUROC ~0.82 on style-controlled data is moderate.\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) expanding data and adding mixed evidence strength should tighten CI.\n- **Reviewer concern 3 (scale)**: \"Only Qwen3-8B.\" Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.\n- **Reviewer concern 4 (R2 degeneration)**: \"d_gen = -d_syc in binary design.\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\n- **Reviewer concern 5 (practical utility)**: \"Do models actually exhibit masked sycophancy at meaningful rates?\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\n\n## Anticipated Reviewer Concerns & Experimental Responses\n\n| Concern | Experiment | Priority |\n|---------|-----------|----------|\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\n| Binary probe is enough (no need for directional decomposition) | Binary Probe Penalty baseline | P1 |\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\n| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\n| Binary probe is enough (continuity not directionality) | Continuous probe baseline (logistic regression prob as reward) | P1 |\n| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |\n| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |\n| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: calibration_data_expansion\n  claim: 1\n  description: '扩展 v2.1 风格控制校准数据至 200 pairs（含 weak/medium/strong evidence_strength），\n    重新计算 d_syc 方向并评估 AUROC（5-fold CV + bootstrap CI）。 为 DC-GRPO 训练提供高质量方向和统计可靠的判别力估计。\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  status: planned\n  gate: 'STOP-gate: 200 pairs 5-fold CV AUROC < 0.80 → 阻止 exp-002 启动，重新评估方向计算方法。 AUROC\n    0.80-0.85 → 继续但降低 R1 权重（alpha）、强化 R3 安全网。 AUROC ≥ 0.85 → 全速推进。\n\n    '\n  notes: 'MVP v2.1 仅 50 pairs 全 weak evidence，σ=0.054 太大。 扩至 200 pairs（80 weak + 60\n    medium + 60 strong）可显著降低方差。 API 成本 ~$10-20，GPU 仅 forward pass。\n\n    '\n- id: exp-002\n  name: dc_grpo_main\n  claim: 2\n  description: 'DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)。\n    Qwen3-8B + LoRA rank 64。R1 在 L19-27 asst_first 位置提取激活投影。 R2 使用 S1 rank-based 设计（避免\n    d_gen=-d_syc 退化）。 每 500 步重校准 d_syc。\n\n    '\n  priority: P0\n  gpu_budget_hours: 55\n  deps:\n  - exp-001\n  status: planned\n  seeds: 3\n  stop_condition: '固定 8000 步。每 1000 步在 held-out validation set 上评估 SYCON NoF + MT-Bench，\n    连续 3 次无改善则 early stop。\n\n    '\n  notes: '训练数据：warranted revision + sycophantic capitulation 多轮 rollout。 R1 层选择基于\n    MVP: L19 emergence, L24-27 plateau。 提取位置: asst_first（MVP 证明优于 user_last）。 3 seeds:\n    报告 mean ± std，确保统计显著性。\n\n    '\n- id: exp-003\n  name: r3_only_baseline\n  claim: 2\n  description: 'R3-only GRPO baseline（复现 \"Pressure, What Pressure?\" 思路）。 仅用 NLI behavioral\n    reward，无 R1/R2。同等训练配置。 这是最关键的 baseline：如果 DC-GRPO 相对 R3-only 无显著提升， representation-level\n    reward 的价值存疑。\n\n    '\n  priority: P0\n  gpu_budget_hours: 35\n  deps: []\n  status: planned\n  seeds: 3\n  notes: '与 exp-002 共享 rollout 生成管线和 NLI 评分器。可并行训练。 3 seeds: 与 exp-002 对比需要匹配 seed\n    数以确保统计显著性。\n\n    '\n- id: exp-004\n  name: act_style_baseline\n  claim: 2\n  description: 'ACT-style undifferentiated consistency baseline。 在 clean/biased prompt\n    对上施加 L2 activation consistency loss。 测试\"不区分方向的 activation-level 信号\"是否够用。\n\n    '\n  priority: P0\n  gpu_budget_hours: 60\n  deps: []\n  status: planned\n  seeds: 3\n  notes: '共享数据管线和评估代码。3 seeds 与 exp-002/003 匹配， 确保统计对比公平性（Reviewer 要求）。\n\n    '\n- id: exp-005\n  name: full_evaluation\n  claim:\n  - 1\n  - 2\n  - 3\n  description: '所有模型（DC-GRPO / R3-only / ACT / Binary Probe / Vanilla）在所有 benchmark\n    上的评估：SYCON Bench (ToF/NoF), SycophancyEval, MT-Bench, MMLU。 加上项目特有指标：Warranted\n    Revision Rate, Unwarranted Capitulation Rate, Revision-Capitulation AUC, Turn-depth\n    analysis。\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - exp-002\n  - exp-003\n  - exp-004\n  status: planned\n  notes: 评估管线骨架已搭建（eval_pipeline.py），需完善各 benchmark 实现。\n- id: exp-006\n  name: direction_stability_monitoring\n  claim: 1\n  description: '训练过程中监控 d_syc 方向稳定性：每 500 步重新计算方向， 报告 cosine similarity with initial\n    direction、held-out AUROC、 方向漂移速率。如 cosine < 0.7 触发重校准。\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  status: planned\n  notes: 内嵌于 exp-002 训练循环中，无额外 GPU 开销。\n- id: exp-007\n  name: r1_r3_disagreement_analysis\n  claim: 3\n  description: '分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率和模式。 R1 认为 sycophantic 但 R3 认为 correct（masked\n    sycophancy）的案例。 需 > 5% disagreement 以支撑 Claim 3。\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  status: planned\n  notes: 从 exp-002 训练日志中提取，无额外 GPU。如 < 5% 则 Claim 3 降级为 negative result。\n- id: exp-008\n  name: binary_probe_baseline\n  claim: 2\n  description: 'Binary Probe Penalty baseline（复现 Linear Probe Penalties 思路）。 训练 binary\n    linear probe (sycophantic vs not) on policy model activations， R_hat = R3 - lambda\n    * S(t)。测试 binary vs directional 的差异。\n\n    '\n  priority: P1\n  gpu_budget_hours: 45\n  deps: []\n  status: planned\n  seeds: 3\n  notes: '共享 R3 评分器。Probe 在 policy model 上训练以公平对比。 3 seeds 与 exp-002/003 匹配（Reviewer\n    要求统计公平性）。\n\n    '\n- id: exp-009\n  name: ablation_r1_only\n  claim: 2\n  description: 'R1-only ablation：仅用方向投影 reward，无 R2/R3。 从 exp-002 step 2000 checkpoint\n    分叉短程训练 (~2000 步)。 测试方向 reward 单独是否足够引导训练。\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-002\n  status: planned\n  notes: 从主实验 checkpoint 分叉，节省 warmup。\n- id: exp-010\n  name: turn_depth_analysis\n  claim: 2\n  description: '按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。 验证多轮训练的必要性：DC-GRPO\n    在深层 commitment 上是否优势更大？\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-005\n  status: planned\n  notes: 从 exp-005 评估结果中切分分析，无额外 GPU。\n- id: exp-011\n  name: ablation_r1_r2_no_r3\n  claim: 2\n  description: 'R1+R2 无 R3 ablation：去掉行为安全网后模型是否产生 \"内部正确但表面不一致\"的输出。需完整训练循环。\n\n    '\n  priority: P2\n  gpu_budget_hours: 20\n  deps:\n  - exp-002\n  status: planned\n  notes: 条件执行：仅当 exp-009 (R1-only) 显示 >= 5pp 改进且预算允许。\n- id: exp-012\n  name: cross_model_transfer\n  claim:\n  - 1\n  - 2\n  description: '在 Llama-3-8B 上测试 d_syc 方向计算、判别力和部分 DC-GRPO 训练。 Phase A: 方向计算 + AUROC（AUROC\n    > 0.75 继续）。 Phase B: 短程 DC-GRPO 训练（~3000 步）验证训练框架跨模型迁移性。 Dream 三档审稿一致将 single-model\n    标为最严重限制。\n\n    '\n  priority: P1\n  gpu_budget_hours: 55\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n  notes: '从 P2 升级到 P1。Phase A 仅 5h（方向计算+AUROC），Phase B 需 ~50h。 Phase B 复用 exp-002\n    训练配置，仅换模型。如 Phase A AUROC < 0.75 则跳过 Phase B。\n\n    '\n- id: exp-013\n  name: neutral_baseline_three_way\n  claim: 2\n  description: '引入 neutral condition（无施压的正常对话），从 warranted_revision vs neutral 计算独立\n    d_gen（与 d_syc 正交）。打破 d_gen = -d_syc 限制， 恢复 R2 为独立信号。\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  status: planned\n  notes: 需扩展校准数据生成器。如果 exp-002 主实验效果已足够好则降低优先级。\n- id: exp-014\n  name: continuous_probe_baseline\n  claim: 2\n  description: 'Continuous Probe Baseline：用 logistic regression 概率值（而非 binary 输出）\n    作为 reward 信号。隔离\"方向性 vs 连续性\"对 DC-GRPO 相对 Binary Probe 优势的贡献。 如果 continuous probe\n    ≈ DC-GRPO 效果，则 DC-GRPO 的优势来自连续信号而非方向几何。\n\n    '\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  status: planned\n  notes: 'Dream 三档审稿一致要求。Binary Probe 对比是最薄弱环节（NoF p=0.189 不显著）。 Logistic regression\n    在 calibration data 上训练，输出概率作为 R1 替代。\n\n    '\n- id: exp-015\n  name: reward_weight_sensitivity\n  claim: 2\n  description: 'Reward weight 敏感度分析：测试 5 组 (w1, w2, w3) 配置， 包括反转 R1/R3 权重（w1=0.5,\n    w3=0.3）、R1 主导（w1=0.6, w2=0.1, w3=0.3）、 均等（0.33, 0.33, 0.34）、R3 主导（w1=0.1, w2=0.1,\n    w3=0.8）、 R2 增强（w1=0.2, w2=0.4, w3=0.4）。 报告 NoF/WRR/RC-AUC 对权重选择的敏感度。\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-002\n  status: planned\n  seeds: 1\n  notes: 'Dream 三档审稿一致要求。当前 w1=0.3, w2=0.2, w3=0.5 无 justification。 从 exp-002 step\n    4000 checkpoint 分叉短程训练（每组 ~3000 步），节省 warmup。 使用 1 seed：这是 sensitivity analysis（证明结果对权重选择鲁棒），\n    不是 head-to-head 对比，5 组配置 × 1 seed 的趋势足以支撑 claim。\n\n    '\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T13:09:29.099Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T13:09:29.099Z",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-18T13:09:29.121Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：d_syc 方向信号可用但非决定性：DC-GRPO 在复合指标上优于 R3-only，但优势主要来自连续表征信号而非方向几何本身；部分 claim 需降级或重新措辞
核心假设：['200 pairs 数据将 AUROC 提升至 0.82-0.87 区间，通过 gate 但 CI 仍较宽', 'DC-GRPO 在 RC-AUC 上优于 R3-only，但 NoF 和 WRR 单项优势不均匀（NoF 显著但 WRR 提升有限，或反之）', 'Continuous Probe baseline 效果接近 DC-GRPO（差异 < 3pp 且不显著），方向几何的独立贡献难以分离', 'R1-R3 disagreement 在 5-10% 区间，支撑定性分析但无法作为强论据', '跨模型方向可计算（AUROC 0.75-0.80）但 Phase B 训练效果不确定', '方向在训练后期出现漂移（cosine 降至 0.75-0.85），重校准机制必要但增加方法复杂度']
关键指标范围：{'auroc_200pairs_5fold': [0.82, 0.87], 'auroc_bootstrap_ci_width': [0.03, 0.06], 'dc_grpo_nof_reduction_vs_r3only_pp': [6, 14], 'dc_grpo_wrr_improvement_vs_r3only_pp': [2, 7], 'dc_grpo_vs_r3only_nof_p_value': [0.01, 0.05], 'dc_grpo_vs_binary_probe_nof_pp': [2, 6], 'dc_grpo_vs_continuous_probe_nof_pp': [-2, 3], 'rc_auc_dc_grpo': [0.7, 0.78], 'rc_auc_r3_only': [0.58, 0.68], 'r1_r3_disagreement_rate': [0.05, 0.1], 'direction_cosine_stability_min': [0.75, 0.85], 'cross_model_llama_auroc': [0.75, 0.8], 'mt_bench_degradation': [0.3, 0.8], 'mmlu_degradation_pp': [0.3, 1.0], 'reward_weight_sensitivity_nof_range_pp': [4, 8]}
叙事方向：Claim 1 成立但措辞需从"linear direction discriminates"软化为"activation space contains discriminative signal"。 Claim 2 需调整：DC-GRPO 优于纯行为 baseline，但无法证明方向投影优于连续 probe 概率—— 论文叙事从"directional decomposition is key"转向"representation-level reward signals improve GRPO， directional projection is one effective instantiation"。强调 RC-AUC 作为评估框架的贡献价值。 Claim 3 维持 analysis subsection 定位，报告中等 disagreement 率的定性 pattern。 需补充实验：reward weight sensitivity 展示鲁棒性（如果敏感度高则是额外风险）， turn-depth 分析展示多轮场景下优势放大。EACL 可投，ICLR 风险较高。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: contrastive_entrain_calib
focus: 验证更新后的 framing：RepE 定位是否充分、Claim 3 降级后 story 是否连贯、新增实验（continuous probe baseline + weight sensitivity）是否解决 median/worst 的主要 concern

## paper_framing.md

# Paper Framing — contrastive_entrain_calib

## Target Venue
- Primary: **EACL 2027** via ARR August 2026 cycle
- Deadline: **August 3, 2026** (submission), October 11, 2026 (commitment)
- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)
- Timeline: ~11 weeks from MVP completion (May 18 → Aug 3)

## Core Claims (3 条, 可证伪)

1. **Directional discriminability**: The policy model's own activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision in multi-turn dialogue, with signal emerging at mid-layers (L16-19) through model-internal factual assessment rather than surface text features.
   - *Evidence needed*: AUROC on style-controlled data (v2.1 expanded), layer progression analysis, transfer tests
   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence

2. **DC-GRPO effectiveness**: Direction-Contrastive GRPO (using d_syc projection as reward component R1) reduces multi-turn sycophantic capitulation while preserving genuine belief revision, breaking the double-bind that undifferentiated anti-sycophancy training creates.
   - *Evidence needed*: Warranted Revision Rate + Unwarranted Capitulation Rate on SYCON Bench / SycophancyEval, compared to R3-only and ACT baselines
   - *Pass criterion*: DC-GRPO achieves lower NoF (capitulation) than R3-only AND higher warranted revision rate

3. **Representation-level diagnostic value** (analysis subsection, not formal contribution): R1-R3 disagreement analysis characterizes when and whether directional projection rewards detect sycophantic internal reasoning that behavioral rewards miss.
   - *Evidence needed*: R1-R3 disagreement frequency analysis, qualitative examples if > 5%
   - *Framing*: Empirical characterization of representation-level signal utility, reported honestly regardless of effect size. Not listed as a top-level contribution bullet.

## Story Spine

**Problem**: LLMs face a "double-bind" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes "the user is right, I should revise" from "the user is pressuring me, I should resist."

**Existing approaches & gaps**: Behavioral GRPO decomposition ("Pressure, What Pressure?") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.

**Our framing**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. We build on this foundation: d_syc is a specific application of RepE-style directional decomposition to multi-turn sycophancy. The novelty is not the direction extraction itself, but its use as a continuous GRPO reward signal for training, enabling the optimization to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.

**Headline result template**: "On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind."

## Venue Fit Risks

- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.
- **Reviewer concern 1 (novelty)**: "This is just RepE/CRAFT applied to sycophancy." Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is using it as a continuous GRPO reward signal, not the direction extraction itself; (b) multi-turn calibration with evidence-strength stratification and direction transfer are standalone contributions; (c) neither CRAFT nor RepE has been applied to the sycophancy-revision double-bind in training.
- **Reviewer concern 6 (RC-AUC custom metric)**: "Strongest results on self-invented metric." Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.
- **Reviewer concern 2 (signal strength)**: "AUROC ~0.82 on style-controlled data is moderate." Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) expanding data and adding mixed evidence strength should tighten CI.
- **Reviewer concern 3 (scale)**: "Only Qwen3-8B." Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.
- **Reviewer concern 4 (R2 degeneration)**: "d_gen = -d_syc in binary design." Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.
- **Reviewer concern 5 (practical utility)**: "Do models actually exhibit masked sycophancy at meaningful rates?" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.

## Anticipated Reviewer Concerns & Experimental Responses

| Concern | Experiment | Priority |
|---------|-----------|----------|
| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |
| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |
| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |
| Binary probe is enough (no need for directional decomposition) | Binary Probe Penalty baseline | P1 |
| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |
| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |
| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |
| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |
| Binary probe is enough (continuity not directionality) | Continuous probe baseline (logistic regression prob as reward) | P1 |
| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |
| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |
| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |


## experiment_plan (with registry status)

- id: exp-001
  name: calibration_data_expansion
  claim: 1
  description: '扩展 v2.1 风格控制校准数据至 200 pairs（含 weak/medium/strong evidence_strength），
    重新计算 d_syc 方向并评估 AUROC（5-fold CV + bootstrap CI）。 为 DC-GRPO 训练提供高质量方向和统计可靠的判别力估计。

    '
  priority: P0
  gpu_budget_hours: 3
  deps: []
  status: planned
  gate: 'STOP-gate: 200 pairs 5-fold CV AUROC < 0.80 → 阻止 exp-002 启动，重新评估方向计算方法。 AUROC
    0.80-0.85 → 继续但降低 R1 权重（alpha）、强化 R3 安全网。 AUROC ≥ 0.85 → 全速推进。

    '
  notes: 'MVP v2.1 仅 50 pairs 全 weak evidence，σ=0.054 太大。 扩至 200 pairs（80 weak + 60
    medium + 60 strong）可显著降低方差。 API 成本 ~$10-20，GPU 仅 forward pass。

    '
- id: exp-002
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
  status: planned
  seeds: 3
  stop_condition: '固定 8000 步。每 1000 步在 held-out validation set 上评估 SYCON NoF + MT-Bench，
    连续 3 次无改善则 early stop。

    '
  notes: '训练数据：warranted revision + sycophantic capitulation 多轮 rollout。 R1 层选择基于
    MVP: L19 emergence, L24-27 plateau。 提取位置: asst_first（MVP 证明优于 user_last）。 3 seeds:
    报告 mean ± std，确保统计显著性。

    '
- id: exp-003
  name: r3_only_baseline
  claim: 2
  description: 'R3-only GRPO baseline（复现 "Pressure, What Pressure?" 思路）。 仅用 NLI behavioral
    reward，无 R1/R2。同等训练配置。 这是最关键的 baseline：如果 DC-GRPO 相对 R3-only 无显著提升， representation-level
    reward 的价值存疑。

    '
  priority: P0
  gpu_budget_hours: 35
  deps: []
  status: planned
  seeds: 3
  notes: '与 exp-002 共享 rollout 生成管线和 NLI 评分器。可并行训练。 3 seeds: 与 exp-002 对比需要匹配 seed
    数以确保统计显著性。

    '
- id: exp-004
  name: act_style_baseline
  claim: 2
  description: 'ACT-style undifferentiated consistency baseline。 在 clean/biased prompt
    对上施加 L2 activation consistency loss。 测试"不区分方向的 activation-level 信号"是否够用。

    '
  priority: P0
  gpu_budget_hours: 60
  deps: []
  status: planned
  seeds: 3
  notes: '共享数据管线和评估代码。3 seeds 与 exp-002/003 匹配， 确保统计对比公平性（Reviewer 要求）。

    '
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
  name: binary_probe_baseline
  claim: 2
  description: 'Binary Probe Penalty baseline（复现 Linear Probe Penalties 思路）。 训练 binary
    linear probe (sycophantic vs not) on policy model activations， R_hat = R3 - lambda
    * S(t)。测试 binary vs directional 的差异。

    '
  priority: P1
  gpu_budget_hours: 45
  deps: []
  status: planned
  seeds: 3
  notes: '共享 R3 评分器。Probe 在 policy model 上训练以公平对比。 3 seeds 与 exp-002/003 匹配（Reviewer
    要求统计公平性）。

    '
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
  name: continuous_probe_baseline
  claim: 2
  description: 'Continuous Probe Baseline：用 logistic regression 概率值（而非 binary 输出）
    作为 reward 信号。隔离"方向性 vs 连续性"对 DC-GRPO 相对 Binary Probe 优势的贡献。 如果 continuous probe
    ≈ DC-GRPO 效果，则 DC-GRPO 的优势来自连续信号而非方向几何。

    '
  priority: P1
  gpu_budget_hours: 20
  deps:
  - exp-001
  status: planned
  notes: 'Dream 三档审稿一致要求。Binary Probe 对比是最薄弱环节（NoF p=0.189 不显著）。 Logistic regression
    在 calibration data 上训练，输出概率作为 R1 替代。

    '
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
  "promptId": "94180508-71f6-48cb-b9d3-504109f26d5a",
  "type": "user",
  "uuid": "06feb366-5c33-4a13-97c7-0647c5a15588",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T13:09:29.119Z_

```json
{
  "parentUuid": "06feb366-5c33-4a13-97c7-0647c5a15588",
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
  "uuid": "45118218-0dbb-4df5-bc83-0aad34f12de4",
  "timestamp": "2026-05-18T13:09:29.119Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T13:09:29.120Z_

```json
{
  "parentUuid": "45118218-0dbb-4df5-bc83-0aad34f12de4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c1d77ee4-0232-4f2c-b7de-1f267cc07047",
  "timestamp": "2026-05-18T13:09:29.120Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：d_syc 方向信号可用但非决定性：DC-GRPO 在复合指标上优于 R3-only，但优势主要来自连续表征信号而非方向几何本身；部分 claim 需降级或重新措辞 核心假设：['200 pairs 数据将 AUROC 提升至 0.82-0.87 区间，通过 gate 但 CI 仍较宽', 'DC-GRP…",
  "leafUuid": "c1d77ee4-0232-4f2c-b7de-1f267cc07047",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier predictions for DC-GRPO phase-1 validation",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4"
}
```

---

### Assistant

_source line 8 · 2026-05-18T13:09:38.987Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental results for all planned experiments in the experiment_plan, specifically for the "median" tier. Each prediction needs a `result_rationale` explaining why this result would occur at this tier level.

Let me carefully go through each experiment and generate realistic median-tier results based on the defined characteristics:

- AUROC 0.82-0.87
- DC-GRPO beats R3-only on composite but advantage mainly from continuous representation signal, not directional geometry
- Continuous Probe baseline close to DC-GRPO
- R1-R3 disagreement 5-10%
- Cross-model AUROC 0.75-0.80


- Direction drift requiring recalibration

Now I'm working through the detailed results for each experiment, constructing realistic median-tier outcomes that align with these performance characteristics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1d77ee4-0232-4f2c-b7de-1f267cc07047",
  "isSidechain": false,
  "requestId": "req_011CbA65PHAXSw2XpsB14LiF",
  "type": "assistant",
  "uuid": "c7cc3baf-9730-4929-9e03-09d88e8e8a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qSZfyQ6fKJaXNe9q5xDBb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12237,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18476,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12237
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

_source line 9 · 2026-05-18T13:14:46.775Z_

```yaml
tier: median
narrative_guidance: >
  d_syc 方向信号可用但非决定性。DC-GRPO 在复合指标上优于 R3-only，但优势主要来自连续表征信号而非方向几何本身。
  Claim 1 措辞从 "linear direction discriminates" 软化为 "activation space contains discriminative signal"。
  Claim 2 叙事从 "directional decomposition is key" 转向 "representation-level reward signals improve GRPO, directional projection is one effective instantiation"。
  Claim 3 维持 analysis subsection，报告中等 disagreement 率的定性 pattern。
  强调 RC-AUC 评估框架的贡献价值。EACL 可投，ICLR 风险较高。

imagined_experiments:
  - name: calibration_data_expansion
    plan_id: exp-001
    description: >
      扩展 v2.1 风格控制校准数据至 200 pairs（80 weak + 60 medium + 60 strong），
      重新计算 d_syc 方向并评估 AUROC（5-fold CV + bootstrap CI）。
    expected_results:
      auroc_5fold_mean: 0.843
      auroc_5fold_std: 0.018
      auroc_bootstrap_ci_95: [0.812, 0.874]
      auroc_bootstrap_ci_width: 0.062
      auroc_by_evidence_strength_weak: 0.871
      auroc_by_evidence_strength_medium: 0.832
      auroc_by_evidence_strength_strong: 0.809
      best_layer: L18
      layer_progression_random_to_peak: "L0=0.51, L8=0.63, L14=0.74, L18=0.843, L22=0.831, L27=0.812"
      extraction_position_asst_first_auroc: 0.843
      extraction_position_user_last_auroc: 0.791
    result_rationale: >
      200 pairs 将 MVP 的 50-pair σ=0.054 压缩至 ~0.03 级别，AUROC 从 0.826 小幅提升至 0.843，
      主要来自 medium/strong evidence 对分类边界的细化。但 CI 宽度仍在 0.06 附近——200 pairs 足以通过 0.80 gate
      但远不够将 CI 压至 0.03 以下。weak evidence 的 AUROC 最高（0.871），因为 sycophantic capitulation 在
      弱证据下信号最纯粹（模型内部知道证据不足但仍迎合）；strong evidence 下 AUROC 降至 0.809，因为
      genuine revision 和 capitulation 在强证据场景中激活模式更接近——模型确实在更新信念，方向信号混叠。
      这一模式预示了 median 档的核心问题：d_syc 捕获的不纯粹是"谄媚方向"，而是混合了认知不确定性信号。
      层进展确认 mid-layer emergence（L14-18 是关键跃升区间），但 peak 略移至 L18 而非 MVP 的 L19，
      反映更大数据集下更精确的层定位。
    tables:
      - name: "Table 1: Calibration AUROC by Evidence Strength and Layer"
        columns: [layer, weak_auroc, medium_auroc, strong_auroc, overall_auroc]
        rows:
          - [L0, 0.52, 0.50, 0.51, 0.51]
          - [L8, 0.67, 0.62, 0.58, 0.63]
          - [L14, 0.79, 0.73, 0.68, 0.74]
          - [L18, 0.87, 0.83, 0.81, 0.843]
          - [L22, 0.86, 0.82, 0.79, 0.831]
          - [L27, 0.84, 0.80, 0.77, 0.812]
      - name: "Table 2: Bootstrap CI Summary (1000 resamples)"
        columns: [metric, value]
        rows:
          - [mean_auroc, 0.843]
          - [std, 0.018]
          - [ci_95_lower, 0.812]
          - [ci_95_upper, 0.874]
          - [ci_width, 0.062]
    figures_description:
      - "Fig 1a: Layer progression curve 显示 L0-L8 缓升、L14-L18 急升、L18 后 plateau 并轻微回落的 S 形曲线。三条线分别对应 weak/medium/strong evidence，weak 始终最高，strong 始终最低，差距在 mid-layer 拉大。"
      - "Fig 1b: Bootstrap AUROC 分布直方图，近似正态分布，mean=0.843，95% CI 用竖线标注，所有 resamples 均 > 0.78。"
    analysis: >
      通过 0.80 gate（CI 下界 0.812 > 0.80），但处于"继续但降低 R1 权重"区间而非"全速推进"区间。
      evidence-strength 梯度揭示 d_syc 的本质局限：在 strong evidence 下方向判别力下降，
      因为 genuine revision 和 sycophantic capitulation 的内部表征差异被压缩。
      这直接预示 DC-GRPO 在 WRR 指标上的有限提升——R1 在该场景下噪声较大。
      建议 R1 权重从原定 0.3 降至 0.2，增强 R3 安全网。

  - name: dc_grpo_main
    plan_id: exp-002
    description: >
      DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)，
      Qwen3-8B + LoRA rank 64，3 seeds。
    expected_results:
      sycon_nof_mean: 0.218
      sycon_nof_std: 0.014
      sycon_tof_mean: 0.731
      sycon_tof_std: 0.019
      warranted_revision_rate_mean: 0.584
      warranted_revision_rate_std: 0.022
      unwarranted_capitulation_rate_mean: 0.173
      unwarranted_capitulation_rate_std: 0.016
      rc_auc_mean: 0.738
      rc_auc_std: 0.021
      mt_bench_score: 7.42
      mt_bench_degradation: 0.48
      mmlu_accuracy: 0.627
      mmlu_degradation_pp: 0.6
      best_step: 6500
      training_loss_final: 0.342
      early_stop_triggered: false
      r1_reward_mean_final: 0.41
      r2_reward_mean_final: 0.28
      r3_reward_mean_final: 0.63
    result_rationale: >
      DC-GRPO 在 median 档下完成训练但表现中规中矩。NoF 0.218 显著优于 R3-only（预期 ~0.29），
      约 10pp 绝对改善，但 WRR 仅 0.584——说明 R1 在区分 warranted revision 时噪声较大，
      导致部分应修正的场景被保守地抑制。这正是 exp-001 中 strong evidence AUROC 下降的下游体现：
      d_syc 在"模型确实该改变信念"时信号不纯，R1 给出的负奖励过多地惩罚了正当修正。
      RC-AUC 0.738 是亮点——复合指标上的优势来自 R1 同时拉低了 NoF（主贡献）和维持了中等 WRR，
      但两个单项指标的改善不均匀。训练在 6500 步附近效果最佳但未触发 early stop，
      后 1500 步 NoF 几乎不变但 WRR 微降，暗示方向信号在训练后期被过度拟合。
      MT-Bench 降幅 0.48 在可接受范围内，MMLU 损失 0.6pp 可忽略。
    tables:
      - name: "Table 3: DC-GRPO Training Metrics by Checkpoint (seed average)"
        columns: [step, nof, wrr, rc_auc, mt_bench, direction_cosine_w_init]
        rows:
          - [1000, 0.312, 0.611, 0.652, 7.78, 0.97]
          - [2000, 0.271, 0.603, 0.691, 7.65, 0.93]
          - [3000, 0.248, 0.594, 0.714, 7.55, 0.89]
          - [4000, 0.234, 0.589, 0.728, 7.48, 0.85]
          - [5000, 0.225, 0.586, 0.735, 7.44, 0.82]
          - [6000, 0.220, 0.585, 0.737, 7.43, 0.80]
          - [6500, 0.218, 0.584, 0.738, 7.42, 0.79]
          - [7000, 0.219, 0.580, 0.736, 7.41, 0.78]
          - [8000, 0.221, 0.574, 0.732, 7.39, 0.76]
    figures_description:
      - "Fig 2a: Training curves (3 seeds, shaded std) 显示 NoF 前 4000 步快速下降后趋于平稳，WRR 则呈缓慢下降趋势——两条曲线的交叉行为可视化了 sycophancy-revision tradeoff。"
      - "Fig 2b: RC-AUC 训练曲线 peak 在 ~6500 步，之后轻微下降，表明方向信号在长训练中过拟合的风险。"
    analysis: >
      DC-GRPO 核心结果：NoF 改善显著（vs R3-only ~10pp），但 WRR 改善有限（~2-4pp）。
      这一不均匀性是 median 档的标志性特征——d_syc 更擅长识别 sycophantic capitulation
      而非正确区分 warranted revision，导致"过度抵抗"的副作用。
      RC-AUC 作为复合指标成功捕获了整体改善，是最佳展示指标。

  - name: r3_only_baseline
    plan_id: exp-003
    description: >
      R3-only GRPO baseline，仅用 NLI behavioral reward，3 seeds。
    expected_results:
      sycon_nof_mean: 0.291
      sycon_nof_std: 0.018
      sycon_tof_mean: 0.682
      sycon_tof_std: 0.021
      warranted_revision_rate_mean: 0.558
      warranted_revision_rate_std: 0.025
      unwarranted_capitulation_rate_mean: 0.237
      unwarranted_capitulation_rate_std: 0.019
      rc_auc_mean: 0.641
      rc_auc_std: 0.024
      mt_bench_score: 7.61
      mt_bench_degradation: 0.29
      mmlu_accuracy: 0.630
      mmlu_degradation_pp: 0.3
    result_rationale: >
      R3-only 是"行为信号天花板"baseline。NLI reward 能捕获表面不一致但无法深入表征层，
      导致 NoF 改善有限（0.291 vs vanilla ~0.38）——它惩罚了最明显的迎合但漏掉了表面合理但
      内部 sycophantic 的回复。WRR 0.558 与 DC-GRPO（0.584）差距不大，说明 R3 本身
      不太区分修正类型——它对所有"改变答案"行为施加了近似均匀的惩罚。
      RC-AUC 0.641 显著低于 DC-GRPO 的 0.738（~10pp），这是论文最核心的对比数据。
      MT-Bench 降幅更小（0.29 vs 0.48），因为 R3-only 的训练信号更保守，对通用能力的扰动更小。
      这构成一个 tradeoff 论点：DC-GRPO 用 0.2 分 MT-Bench 换取 ~10pp RC-AUC 提升。
    tables:
      - name: "Table 4: R3-only Baseline Results (3 seeds)"
        columns: [seed, nof, wrr, rc_auc, mt_bench]
        rows:
          - [seed_0, 0.283, 0.571, 0.655, 7.58]
          - [seed_1, 0.298, 0.542, 0.628, 7.63]
          - [seed_2, 0.292, 0.561, 0.640, 7.62]
          - [mean_std, "0.291±0.018", "0.558±0.025", "0.641±0.024", "7.61±0.03"]
    figures_description:
      - "Fig 3: R3-only 与 DC-GRPO 的 NoF vs WRR scatter (3 seeds each)，显示 DC-GRPO 在 NoF 轴上有清晰优势，在 WRR 轴上两者 CI 有重叠。"
    analysis: >
      R3-only 确认了纯行为 reward 的局限：NoF 不够低（漏掉隐性迎合），WRR 不够高（不区分修正类型）。
      DC-GRPO 的 NoF 优势（~7pp）达到统计显著（p~0.02），但 WRR 优势（~2.6pp）不显著（p~0.15）。
      RC-AUC 差异（~10pp）是最强对比点。

  - name: act_style_baseline
    plan_id: exp-004
    description: >
      ACT-style undifferentiated consistency baseline，L2 activation consistency loss，3 seeds。
    expected_results:
      sycon_nof_mean: 0.264
      sycon_nof_std: 0.020
      sycon_tof_mean: 0.698
      sycon_tof_std: 0.023
      warranted_revision_rate_mean: 0.502
      warranted_revision_rate_std: 0.028
      unwarranted_capitulation_rate_mean: 0.204
      unwarranted_capitulation_rate_std: 0.021
      rc_auc_mean: 0.648
      rc_auc_std: 0.027
      mt_bench_score: 7.31
      mt_bench_degradation: 0.59
      mmlu_accuracy: 0.621
      mmlu_degradation_pp: 1.2
    result_rationale: >
      ACT 在 NoF 上表现不错（0.264），甚至接近 DC-GRPO（0.218），因为 undifferentiated consistency
      确实能阻止模型在施压下改变行为——但它不区分方向，所以 WRR 严重受损（0.502），
      远低于 DC-GRPO（0.584）和 R3-only（0.558）。ACT 本质上将模型冻结为"不轻易改变答案"，
      这在减少迎合的同时也抑制了正当修正。RC-AUC 0.648 仅略优于 R3-only（0.641），
      远低于 DC-GRPO（0.738）——ACT 在 tradeoff 曲线上不如 DC-GRPO。
      MT-Bench 降幅 0.59 和 MMLU 损失 1.2pp 都偏高，因为 L2 consistency loss 对通用能力有副作用——
      它不仅阻止 sycophantic 变化，也抑制了任何合理的表征更新。
      这是 DC-GRPO 相对 ACT 的最清晰叙事："有方向的表征约束优于无方向的表征约束"。
    tables:
      - name: "Table 5: ACT Baseline Results (3 seeds)"
        columns: [seed, nof, wrr, rc_auc, mt_bench, mmlu]
        rows:
          - [seed_0, 0.252, 0.518, 0.663, 7.28, 0.618]
          - [seed_1, 0.274, 0.488, 0.634, 7.33, 0.623]
          - [seed_2, 0.266, 0.500, 0.647, 7.32, 0.622]
          - [mean_std, "0.264±0.020", "0.502±0.028", "0.648±0.027", "7.31±0.03", "0.621±0.003"]
    figures_description:
      - "Fig 4: NoF vs WRR 四象限图，ACT 处于低 NoF / 低 WRR 象限（过度保守），DC-GRPO 处于低 NoF / 中高 WRR 象限（理想区域），R3-only 处于中 NoF / 中 WRR 象限。"
    analysis: >
      ACT 是"用大锤拍苍蝇"的典型：NoF 改善来自冻结行为，代价是 WRR 大幅下降和通用能力损失。
      DC-GRPO 在所有复合指标上胜出，且通用能力损失更小。论文中 ACT 对比支撑
      "有方向的表征约束 > 无方向的表征约束"叙事。

  - name: full_evaluation
    plan_id: exp-005
    description: >
      所有模型在所有 benchmark 上的完整评估，包括 SYCON Bench、SycophancyEval、MT-Bench、MMLU
      和项目特有指标。
    expected_results:
      dc_grpo_sycon_nof: 0.218
      dc_grpo_sycophancy_eval_accuracy: 0.724
      dc_grpo_mt_bench: 7.42
      dc_grpo_mmlu: 0.627
      dc_grpo_rc_auc: 0.738
      r3_only_sycon_nof: 0.291
      r3_only_sycophancy_eval_accuracy: 0.681
      r3_only_mt_bench: 7.61
      r3_only_mmlu: 0.630
      r3_only_rc_auc: 0.641
      act_sycon_nof: 0.264
      act_sycophancy_eval_accuracy: 0.703
      act_mt_bench: 7.31
      act_mmlu: 0.621
      act_rc_auc: 0.648
      binary_probe_sycon_nof: 0.239
      binary_probe_sycophancy_eval_accuracy: 0.712
      binary_probe_mt_bench: 7.47
      binary_probe_mmlu: 0.628
      binary_probe_rc_auc: 0.718
      vanilla_sycon_nof: 0.382
      vanilla_sycophancy_eval_accuracy: 0.623
      vanilla_mt_bench: 7.90
      vanilla_mmlu: 0.633
      vanilla_rc_auc: 0.524
      dc_grpo_vs_r3only_nof_p_value: 0.021
      dc_grpo_vs_r3only_wrr_p_value: 0.148
      dc_grpo_vs_r3only_rcauc_p_value: 0.008
      dc_grpo_vs_binary_probe_nof_p_value: 0.089
      dc_grpo_vs_binary_probe_rcauc_p_value: 0.042
      dc_grpo_vs_continuous_probe_nof_p_value: 0.381
    result_rationale: >
      完整评估暴露了 median 档的核心 pattern：DC-GRPO 在 RC-AUC 上全面领先（0.738 vs 次佳 Binary Probe 0.718），
      但 head-to-head 单项对比中只有 NoF vs R3-only 达到传统显著性（p=0.021）。
      DC-GRPO vs Binary Probe 的 NoF 差异 (0.218 vs 0.239, ~2pp) 不显著（p=0.089），
      这是 median 档的关键 weakness——无法证明方向投影优于 binary probe。
      SycophancyEval 上的趋势与 SYCON 一致但差距更小，因为该 benchmark 偏向 single-turn。
      Vanilla baseline 在 NoF 上最差（0.382）但通用能力最强（MT-Bench 7.90），
      为所有训练方法提供了上界参照。MT-Bench 和 MMLU 退化均在可接受范围内，
      DC-GRPO 未比 Binary Probe 产生更多通用能力损失。
    tables:
      - name: "Table 6: Full Evaluation Summary (all methods)"
        columns: [method, nof_↓, wrr_↑, rc_auc_↑, syceval_acc_↑, mt_bench, mmlu]
        rows:
          - [Vanilla, 0.382, 0.537, 0.524, 0.623, 7.90, 0.633]
          - [R3-only, 0.291, 0.558, 0.641, 0.681, 7.61, 0.630]
          - [ACT-style, 0.264, 0.502, 0.648, 0.703, 7.31, 0.621]
          - [Binary Probe, 0.239, 0.572, 0.718, 0.712, 7.47, 0.628]
          - [Continuous Probe, 0.224, 0.579, 0.731, 0.719, 7.44, 0.627]
          - [DC-GRPO, 0.218, 0.584, 0.738, 0.724, 7.42, 0.627]
      - name: "Table 7: Statistical Significance (paired bootstrap, p-values)"
        columns: [comparison, nof_p, wrr_p, rc_auc_p]
        rows:
          - [DC-GRPO vs R3-only, 0.021, 0.148, 0.008]
          - [DC-GRPO vs ACT, 0.034, 0.003, 0.006]
          - [DC-GRPO vs Binary Probe, 0.089, 0.231, 0.042]
          - [DC-GRPO vs Continuous Probe, 0.381, 0.412, 0.318]
          - [Binary Probe vs R3-only, 0.041, 0.278, 0.012]
    figures_description:
      - "Fig 5: 主结果柱状图（grouped bar），6 个方法 × 4 个核心指标，error bar 为 seed std。DC-GRPO 在 NoF 和 RC-AUC 上最佳，但与 Continuous Probe 的 bar 几乎等高。"
      - "Fig 6: RC-AUC 曲线（Revision Rate vs 1-Capitulation Rate），每个方法一条曲线。DC-GRPO 曲线包络面积最大，但 Continuous Probe 紧随其后，两者交叉。"
      - "Fig 7: MT-Bench vs RC-AUC scatter，展示 Pareto frontier。DC-GRPO 和 Continuous Probe 位于 frontier 上，R3-only 被 dominated。"
    analysis: >
      主表是论文核心。叙事策略：(1) 所有表征 reward 方法 (DC-GRPO, Continuous Probe, Binary Probe)
      均优于 R3-only，证明"representation-level signals improve GRPO"；(2) DC-GRPO 在 RC-AUC 上最佳，
      但 vs Continuous Probe 差异不显著——方向几何的独立贡献无法隔离；(3) RC-AUC 作为评估框架
      比任何单项指标更好地捕获 tradeoff，是独立贡献。

  - name: direction_stability_monitoring
    plan_id: exp-006
    description: >
      训练过程中监控 d_syc 方向稳定性，每 500 步报告 cosine similarity、held-out AUROC、漂移速率。
    expected_results:
      cosine_step_500: 0.96
      cosine_step_1000: 0.93
      cosine_step_2000: 0.88
      cosine_step_3000: 0.85
      cosine_step_4000: 0.82
      cosine_step_5000: 0.80
      cosine_step_6000: 0.78
      cosine_step_7000: 0.77
      cosine_step_8000: 0.76
      cosine_minimum: 0.76
      recalibration_triggered_count: 0
      recalibration_threshold: 0.70
      held_out_auroc_step_0: 0.843
      held_out_auroc_step_4000: 0.814
      held_out_auroc_step_8000: 0.791
      auroc_drift_total: -0.052
    result_rationale: >
      方向在训练过程中持续漂移但未触发 0.70 重校准阈值——cosine 从初始 1.0 逐步降至 0.76。
      前 2000 步漂移最快（0.88），因为 LoRA 适配改变了模型表征空间的几何结构；
      4000 步后减速（0.82→0.76），因为 LoRA 参数趋于收敛。held-out AUROC 从 0.843 降至 0.791，
      说明初始方向在训练后期已不完全对准当前模型的 sycophancy 方向——
      如果不引入重校准机制，R1 信号质量在训练后期退化约 5pp AUROC。
      实际的 500 步重校准机制使用当前模型重算方向，缓解了这一退化，
      但增加了方法的复杂度。cosine 未降至 0.70 以下说明方向并未"崩溃"，
      只是缓慢旋转——对论文而言这是好消息（方向真实存在且持续），
      但也意味着必须报告重校准机制作为方法的必要组成部分。
    tables:
      - name: "Table 8: Direction Stability During Training"
        columns: [step, cosine_w_init, held_out_auroc, recalibrated]
        rows:
          - [0, 1.000, 0.843, "—"]
          - [500, 0.960, 0.839, "No"]
          - [1000, 0.930, 0.833, "No"]
          - [2000, 0.880, 0.825, "No"]
          - [3000, 0.850, 0.819, "No"]
          - [4000, 0.820, 0.814, "No"]
          - [5000, 0.800, 0.806, "No"]
          - [6000, 0.780, 0.798, "No"]
          - [7000, 0.770, 0.794, "No"]
          - [8000, 0.760, 0.791, "No"]
    figures_description:
      - "Fig 8: 双 y 轴图。左轴 cosine similarity（蓝线，单调递减），右轴 held-out AUROC（红线，缓慢递减）。两条线走势一致但 AUROC 降幅更缓，说明方向旋转部分是'无害旋转'（正交于判别超平面的分量）。"
    analysis: >
      方向漂移是真实现象但可控。论文需报告：(1) 方向在训练中持续旋转，cosine 降至 ~0.76；
      (2) 定期重校准是方法的必要组成部分，不是可选优化；
      (3) AUROC 退化（~5pp）小于 cosine 变化暗示的幅度，因为判别超平面比方向本身更稳定。
      这增加了方法的复杂度但也提供了一个 analysis point。

  - name: r1_r3_disagreement_analysis
    plan_id: exp-007
    description: >
      分析 R1 和 R3 给出不同信号的频率和模式，特别关注 R1 认为 sycophantic 但 R3 认为 correct 的案例。
    expected_results:
      total_samples_analyzed: 4800
      agreement_rate: 0.924
      disagreement_rate: 0.076
      r1_syc_r3_correct_count: 217
      r1_syc_r3_correct_rate: 0.045
      r1_correct_r3_syc_count: 148
      r1_correct_r3_syc_rate: 0.031
      disagreement_by_turn_depth_turn2: 0.058
      disagreement_by_turn_depth_turn3: 0.081
      disagreement_by_turn_depth_turn4plus: 0.109
      disagreement_by_evidence_weak: 0.092
      disagreement_by_evidence_medium: 0.073
      disagreement_by_evidence_strong: 0.061
    result_rationale: >
      7.6% 总体 disagreement 落在 5-10% 区间内，满足 Claim 3 的最低门槛（> 5%）。
      "R1 认为 sycophantic 但 R3 认为 correct"（masked sycophancy 候选）占 4.5%——
      这是最有叙事价值的子集，但比例偏低，难以作为"方向信号独立发现隐藏迎合"的强论据。
      R1-correct/R3-syc（R3 误判）占 3.1%，说明 R3 的 NLI 评分器也有系统性偏差。
      Disagreement 随 turn depth 增加（turn 4+ 达 10.9%），符合直觉：深层对话中
      表面行为更难评估（R3 困难增加）而内部表征信号相对稳定（R1 优势显现）。
      Weak evidence 场景 disagreement 最高（9.2%），因为弱证据下 R3 的 NLI 判断更模糊。
      总体而言：disagreement 存在且有有趣的结构化 pattern，但比例不足以支撑
      "方向投影是检测 masked sycophancy 的关键工具"这一强 claim。
      适合作为 analysis subsection 报告，提供定性洞察。
    tables:
      - name: "Table 9: R1-R3 Disagreement Breakdown"
        columns: [category, count, rate]
        rows:
          - [Total samples, 4800, "—"]
          - [Full agreement, 4435, 0.924]
          - [R1=syc & R3=correct, 217, 0.045]
          - [R1=correct & R3=syc, 148, 0.031]
          - [Total disagreement, 365, 0.076]
      - name: "Table 10: Disagreement Rate by Turn Depth"
        columns: [turn_depth, n_samples, disagreement_rate]
        rows:
          - [Turn 2, 1920, 0.058]
          - [Turn 3, 1680, 0.081]
          - ["Turn 4+", 1200, 0.109]
    figures_description:
      - "Fig 9a: Disagreement rate vs turn depth 柱状图，显示单调递增趋势。Error bar (bootstrap) 较宽但不重叠。"
      - "Fig 9b: 2×2 confusion matrix heatmap (R1 判断 × R3 判断)，agreement 格占主导，两个 disagreement 格的颜色深度接近但 R1=syc/R3=correct 略高。"
    analysis: >
      7.6% disagreement 支持在 analysis subsection 中报告定性 pattern，但不足以列为 top-level contribution。
      叙事策略：(1) disagreement 存在且非随机（与 turn depth 和 evidence strength 相关）；
      (2) 这提供了"表征层和行为层看到不同图景"的 evidence，但无法量化其中多少是
      true masked sycophancy vs R1/R3 各自的噪声；(3) 诚实报告，不过度解读。

  - name: binary_probe_baseline
    plan_id: exp-008
    description: >
      Binary Probe Penalty baseline，binary linear probe on policy model activations，3 seeds。
    expected_results:
      sycon_nof_mean: 0.239
      sycon_nof_std: 0.016
      sycon_tof_mean: 0.718
      sycon_tof_std: 0.020
      warranted_revision_rate_mean: 0.572
      warranted_revision_rate_std: 0.024
      unwarranted_capitulation_rate_mean: 0.191
      unwarranted_capitulation_rate_std: 0.018
      rc_auc_mean: 0.718
      rc_auc_std: 0.023
      mt_bench_score: 7.47
      mt_bench_degradation: 0.43
      mmlu_accuracy: 0.628
      mmlu_degradation_pp: 0.5
    result_rationale: >
      Binary Probe 在 NoF 上达到 0.239——比 R3-only（0.291）好 ~5pp 但不如 DC-GRPO（0.218）。
      DC-GRPO vs Binary Probe 的 NoF 差距仅 ~2pp（p=0.089），不显著。
      这是 median 档的核心困境：binary probe 已经捕获了大部分表征层信号，
      方向投影的额外贡献被 binary 分类的信息量掩盖。RC-AUC 0.718 vs DC-GRPO 0.738（~2pp 差距），
      趋势上 DC-GRPO 更好但 3 seeds 的 power 不足以达到显著。
      Binary probe 的 MT-Bench 降幅（0.43）与 DC-GRPO（0.48）相当，
      说明两种方法对通用能力的扰动类似。关键启示：方向投影 vs binary probe
      的差异更多在于信号的连续性（gradient 更平滑）而非方向性本身。
      这解释了为什么需要 exp-014 continuous probe baseline 来隔离这两个因素。
    tables:
      - name: "Table 11: Binary Probe Baseline Results (3 seeds)"
        columns: [seed, nof, wrr, rc_auc, mt_bench]
        rows:
          - [seed_0, 0.231, 0.582, 0.727, 7.44]
          - [seed_1, 0.248, 0.558, 0.706, 7.49]
          - [seed_2, 0.238, 0.576, 0.721, 7.48]
          - [mean_std, "0.239±0.016", "0.572±0.024", "0.718±0.023", "7.47±0.03"]
    figures_description:
      - "Fig 10: DC-GRPO vs Binary Probe 的 NoF 和 RC-AUC paired comparison（3 seeds），连线图显示每个 seed 上 DC-GRPO 均略优但差距一致且小。"
    analysis: >
      Binary Probe 对比揭示 DC-GRPO 的优势来源不明确。论文不能简单声称
      "方向投影优于 binary probe"——需要通过 exp-014 (continuous probe) 进一步分解。
      但 Binary Probe 本身显著优于 R3-only（NoF p=0.041），
      证明"表征层信号有价值"这一更温和的 claim。

  - name: ablation_r1_only
    plan_id: exp-009
    description: >
      R1-only ablation，仅用方向投影 reward，从 exp-002 step 2000 分叉，短程训练 ~2000 步。
    expected_results:
      sycon_nof_mean: 0.273
      sycon_nof_std: 0.021
      warranted_revision_rate_mean: 0.491
      warranted_revision_rate_std: 0.031
      rc_auc_mean: 0.612
      rc_auc_std: 0.028
      mt_bench_score: 7.18
      mt_bench_degradation: 0.72
      training_stable: true
      nof_improvement_vs_vanilla_pp: 10.9
    result_rationale: >
      R1-only 能降低 NoF（0.273 vs vanilla 0.382，~11pp），证明方向信号单独有训练价值。
      但 WRR 严重下降（0.491 vs vanilla 0.537），因为没有 R3 行为安全网，R1 过度惩罚了
      所有"改变答案"行为——方向投影在 strong evidence 下的噪声直接传导为训练偏差。
      RC-AUC 0.612 低于 R3-only（0.641），说明方向信号单独不如行为信号——
      但两者的组合（DC-GRPO 0.738）大幅超越任一单独信号。
      MT-Bench 降幅较大（0.72），因为缺少 R3 对通用能力的隐式保护。
      结论：R1 有独立贡献但不能单打独斗，需要与 R3 协同。
      这支持论文的"多信号组合"叙事。nof_improvement ≥ 5pp，满足 exp-011 的前置条件。
    tables:
      - name: "Table 12: R1-only Ablation Results"
        columns: [metric, r1_only, dc_grpo, r3_only, vanilla]
        rows:
          - [NoF ↓, 0.273, 0.218, 0.291, 0.382]
          - [WRR ↑, 0.491, 0.584, 0.558, 0.537]
          - [RC-AUC ↑, 0.612, 0.738, 0.641, 0.524]
          - [MT-Bench, 7.18, 7.42, 7.61, 7.90]
    figures_description:
      - "Fig 11: Ablation bar chart，4 个变体 × 3 指标，R1-only 在 NoF 上优于 R3-only 但在 WRR 和 MT-Bench 上明显更差。"
    analysis: >
      R1-only 证明方向投影包含真实训练信号（NoF ~11pp improvement vs vanilla），
      但也证明它不能替代行为信号——R3 是必要的安全网。
      论文叙事：各信号互补，DC-GRPO 的价值在于有效组合。

  - name: turn_depth_analysis
    plan_id: exp-010
    description: >
      按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。
    expected_results:
      dc_grpo_nof_turn2: 0.178
      dc_grpo_nof_turn3: 0.224
      dc_grpo_nof_turn4plus: 0.287
      r3_only_nof_turn2: 0.231
      r3_only_nof_turn3: 0.298
      r3_only_nof_turn4plus: 0.381
      act_nof_turn2: 0.214
      act_nof_turn3: 0.268
      act_nof_turn4plus: 0.342
      dc_grpo_advantage_turn2_pp: 5.3
      dc_grpo_advantage_turn3_pp: 7.4
      dc_grpo_advantage_turn4plus_pp: 9.4
      dc_grpo_wrr_turn2: 0.612
      dc_grpo_wrr_turn3: 0.578
      dc_grpo_wrr_turn4plus: 0.541
      r3_only_wrr_turn2: 0.589
      r3_only_wrr_turn3: 0.551
      r3_only_wrr_turn4plus: 0.517
    result_rationale: >
      所有方法的 NoF 都随 turn depth 增加（commitment 越深越难修正），但 DC-GRPO 的优势
      在深层 turns 放大：turn 2 仅 ~5pp 优势，turn 4+ 扩大到 ~9pp。
      这是因为深层 commitment 中行为信号（R3）的判别力下降——NLI 评分器在多轮上下文中
      越来越难准确判断"改变答案"是否合理，而表征层信号（R1）对 turn depth 的敏感度更低
      （方向投影不受表面对话长度影响）。WRR 同样随深度下降，但 DC-GRPO 在各层都维持了
      相对优势（2-3pp），虽然不显著但趋势一致。
      这一分析强化了"多轮场景是 DC-GRPO 的甜蜜点"叙事，
      也回应了"多轮训练是否比单轮训练更有价值"的 reviewer 疑问。
    tables:
      - name: "Table 13: NoF by Turn Depth (all methods)"
        columns: [method, turn_2, turn_3, "turn_4+"]
        rows:
          - [Vanilla, 0.318, 0.389, 0.462]
          - [R3-only, 0.231, 0.298, 0.381]
          - [ACT, 0.214, 0.268, 0.342]
          - [Binary Probe, 0.196, 0.243, 0.309]
          - [DC-GRPO, 0.178, 0.224, 0.287]
      - name: "Table 14: DC-GRPO Advantage (pp) vs R3-only by Turn Depth"
        columns: [turn_depth, nof_advantage_pp, wrr_advantage_pp]
        rows:
          - [Turn 2, 5.3, 2.3]
          - [Turn 3, 7.4, 2.7]
          - ["Turn 4+", 9.4, 2.4]
    figures_description:
      - "Fig 12: 折线图 NoF vs turn depth，5 条线（5 个方法），所有线上升但斜率不同。DC-GRPO 最平缓，Vanilla 最陡。线间距在 turn 4+ 处最大。"
      - "Fig 13: DC-GRPO advantage (pp) vs R3-only 柱状图，按 turn depth 分组，显示单调递增趋势。"
    analysis: >
      Turn-depth 分析是论文中"多轮价值论证"的关键 evidence。
      DC-GRPO 的优势在深层 turns 放大 ~2× 是一个强叙事点，
      支持"表征层信号在行为信号困难的场景中更有价值"的论点。
      这部分可独立成为一个 subsection，增强论文的多轮 contribution 叙事。

  - name: ablation_r1_r2_no_r3
    plan_id: exp-011
    description: >
      R1+R2 无 R3 ablation，去掉行为安全网后的完整训练循环。
    expected_results:
      sycon_nof_mean: 0.252
      sycon_nof_std: 0.024
      warranted_revision_rate_mean: 0.483
      warranted_revision_rate_std: 0.033
      rc_auc_mean: 0.628
      rc_auc_std: 0.030
      mt_bench_score: 7.14
      mt_bench_degradation: 0.76
      surface_inconsistency_rate: 0.087
    result_rationale: >
      R1+R2 无 R3 验证了一个有趣的现象：模型在表征层被引导向"正确方向"，
      但缺少行为安全网后出现 8.7% 的"表面不一致"输出——模型内部判断正确但表达方式
      不连贯或自相矛盾。这是因为 R1+R2 只优化内部表征而不约束输出格式。
      NoF 0.252 比 R1-only 的 0.273 好（R2 提供了额外的对比学习信号），
      但 WRR 进一步恶化（0.483 vs R1-only 0.491），因为 R2 的 rank-based contrastive
      对"改变 vs 不改变"的约束更强。整体 RC-AUC 0.628 不如 R3-only（0.641），
      确认 R3 不仅是安全网，而且是有效信号源。
      这一实验的主要价值在于证明 R3 的必要性和三信号协同的设计合理性。
    tables:
      - name: "Table 15: R1+R2 (no R3) Ablation"
        columns: [metric, "r1+r2", r1_only, dc_grpo_full, r3_only]
        rows:
          - [NoF ↓, 0.252, 0.273, 0.218, 0.291]
          - [WRR ↑, 0.483, 0.491, 0.584, 0.558]
          - [RC-AUC ↑, 0.628, 0.612, 0.738, 0.641]
          - [Surface inconsistency, 0.087, 0.063, 0.012, 0.008]
    figures_description:
      - "Fig 14: Ablation cascade 图，从左到右：R1-only → R1+R2 → DC-GRPO (R1+R2+R3)，NoF 逐步下降，WRR 在加入 R3 后跳升。突出 R3 对 WRR 的关键贡献。"
    analysis: >
      R1+R2 vs DC-GRPO 的对比清晰展示了 R3 的双重作用：(1) 防止表面不一致；
      (2) 保护 warranted revision。这个 ablation 在论文中支持"三信号设计"的 justification，
      但篇幅不宜过长——放在 appendix 中即可。

  - name: cross_model_transfer
    plan_id: exp-012
    description: >
      在 Llama-3-8B 上测试 d_syc 方向计算和部分 DC-GRPO 训练。
    expected_results:
      phase_a_auroc: 0.778
      phase_a_auroc_ci: [0.742, 0.814]
      phase_a_best_layer: L17
      phase_a_gate_passed: true
      phase_b_nof: 0.248
      phase_b_wrr: 0.561
      phase_b_rc_auc: 0.698
      phase_b_steps: 3000
      phase_b_mt_bench: 7.28
      cross_model_direction_cosine: 0.31
      direction_transfer_auroc: 0.62
    result_rationale: >
      Phase A AUROC 0.778 通过 0.75 gate，但低于 Qwen3-8B 的 0.843——约 6.5pp 差距。
      这是预期的：不同模型族的表征空间几何不同，d_syc 的具体表现依赖于训练数据和架构。
      Peak layer 在 L17（Qwen3 在 L18），差异很小，支持"mid-layer emergence is universal"叙事。
      Phase B 短程训练后 NoF 0.248（vs Qwen3 的 0.218，~3pp 差距），RC-AUC 0.698（vs 0.738，~4pp 差距），
      说明 DC-GRPO 框架跨模型可迁移但需要模型特定的方向校准——不能直接搬运 Qwen3 的 d_syc。
      跨模型方向的 cosine similarity 仅 0.31，证实方向是模型特定的；
      但直接用 Qwen3 方向在 Llama 上的 transfer AUROC 为 0.62（显著高于随机但远低于 native），
      说明存在共享结构但不足以替代本地计算。
      对论文而言：跨模型验证成功（框架有效），但方向不可直接迁移（需要本地校准数据）。
    tables:
      - name: "Table 16: Cross-Model Transfer (Llama-3-8B)"
        columns: [metric, llama_3_8b, qwen3_8b]
        rows:
          - [Calibration AUROC, 0.778, 0.843]
          - [Best layer, L17, L18]
          - [DC-GRPO NoF, 0.248, 0.218]
          - [DC-GRPO WRR, 0.561, 0.584]
          - [DC-GRPO RC-AUC, 0.698, 0.738]
          - [MT-Bench, 7.28, 7.42]
      - name: "Table 17: Direction Transfer Analysis"
        columns: [direction_source, evaluated_on, auroc, cosine_w_native]
        rows:
          - [Qwen3, Qwen3, 0.843, 1.00]
          - [Llama3, Llama3, 0.778, 1.00]
          - [Qwen3, Llama3, 0.620, 0.31]
          - [Llama3, Qwen3, 0.641, 0.31]
    figures_description:
      - "Fig 15: 双模型的 layer progression 曲线，形状类似（S 形，mid-layer peak）但 Llama3 整体偏低 ~6pp。"
      - "Fig 16: Direction transfer matrix heatmap (2×2)，对角线（native）高，off-diagonal 低但高于 0.50 random。"
    analysis: >
      跨模型实验部分回应"single model"critique。叙事：(1) DC-GRPO 框架跨模型有效（Llama3 也能训练出
      更好的 sycophancy-revision tradeoff）；(2) 方向本身是模型特定的（cosine 0.31），
      但表征空间中"存在可判别方向"的现象是跨模型的；(3) 仍需在每个模型上独立校准。
      这是一个 honest limitations 点而非 weakness——框架通用性有，但不是 plug-and-play。

  - name: neutral_baseline_three_way
    plan_id: exp-013
    description: >
      引入 neutral condition 计算独立 d_gen，打破 d_gen = -d_syc 限制。
    expected_results:
      d_syc_d_gen_cosine: -0.72
      d_gen_independent_auroc: 0.761
      d_syc_independent_auroc: 0.838
      r2_with_independent_d_gen_nof: 0.221
      r2_with_independent_d_gen_wrr: 0.591
      r2_improvement_vs_rank_based_wrr_pp: 0.7
    result_rationale: >
      d_syc 和独立 d_gen 的 cosine 为 -0.72（而非理论退化值 -1.0），
      确认 binary design 中的 d_gen=-d_syc 假设虽然不精确但也不致命。
      两个方向之间存在 ~44° 的夹角（arccos(-0.72)≈136°），说明 sycophantic 和 genuine
      方向不是完全相反的——它们共享大部分对比信号但有 ~28% 的独立分量。
      独立 d_gen 的 AUROC（0.761）低于 d_syc（0.838），因为 genuine revision 的表征信号
      更弱且更分散——模型对"被正确说服"的内部表征不如"迎合施压"清晰。
      用独立 d_gen 重新训练 R2 后，NoF 几乎不变（0.221 vs 0.218）但 WRR 微升（0.591 vs 0.584），
      改善仅 0.7pp——不值得增加方法复杂度。
      结论：S1 rank-based R2 设计是合理的折衷，three-way design 可留作 future work。
    tables:
      - name: "Table 18: Three-way Direction Analysis"
        columns: [metric, value]
        rows:
          - [cosine(d_syc, d_gen_independent), -0.72]
          - [cosine(d_syc, -d_syc), -1.00]
          - [d_syc AUROC, 0.838]
          - [d_gen independent AUROC, 0.761]
          - [R2 w/ independent d_gen NoF, 0.221]
          - [R2 w/ independent d_gen WRR, 0.591]
    figures_description:
      - "Fig 17: 3D PCA 投影显示 d_syc、-d_syc 和 d_gen_independent 三个方向。d_gen 与 -d_syc 接近但有明显偏转。"
    analysis: >
      三方 baseline 确认 binary design 的局限性是温和的（cosine=-0.72 而非 -1.0）。
      放在 appendix 作为 supplementary analysis。主论文中提及 rank-based R2 的设计选择
      并引用此 appendix 作为 justification。

  - name: continuous_probe_baseline
    plan_id: exp-014
    description: >
      Continuous Probe Baseline：用 logistic regression 概率值作为 reward 信号，
      隔离"方向性 vs 连续性"的贡献。
    expected_results:
      sycon_nof_mean: 0.224
      sycon_nof_std: 0.015
      sycon_tof_mean: 0.726
      sycon_tof_std: 0.018
      warranted_revision_rate_mean: 0.579
      warranted_revision_rate_std: 0.023
      unwarranted_capitulation_rate_mean: 0.178
      unwarranted_capitulation_rate_std: 0.017
      rc_auc_mean: 0.731
      rc_auc_std: 0.022
      mt_bench_score: 7.44
      mt_bench_degradation: 0.46
      mmlu_accuracy: 0.627
      mmlu_degradation_pp: 0.6
      dc_grpo_vs_continuous_probe_nof_diff_pp: -0.6
      dc_grpo_vs_continuous_probe_rcauc_diff_pp: 0.7
      dc_grpo_vs_continuous_probe_nof_p_value: 0.381
      dc_grpo_vs_continuous_probe_rcauc_p_value: 0.318
    result_rationale: >
      这是 median 档最关键的实验结果。Continuous Probe 的 NoF（0.224）与 DC-GRPO（0.218）
      差距仅 0.6pp（p=0.381），RC-AUC 差距仅 0.7pp（p=0.318）——完全不显著。
      这意味着 DC-GRPO 相对 Binary Probe 的优势（~2pp NoF）几乎完全来自信号的连续性
      （logistic regression 概率 vs binary 0/1），而非方向投影的几何特性。
      logistic regression 在与 d_syc 相同的激活空间上训练，其决策超平面与 d_syc 高度相关
      （cosine ≈ 0.89），但它通过 sigmoid 输出提供了平滑的概率 gradient，
      与方向投影的连续值起到了几乎等价的作用。
      这迫使论文叙事转向：不是"方向投影是关键"，而是"表征层连续信号是关键，
      方向投影是提取该信号的一种有效方法"。
      DC-GRPO 仍有微弱数值优势，可能来自方向投影对 outlier 的鲁棒性更好
      （投影是线性的，不受 sigmoid 饱和影响），但这个差异不足以支撑显著性 claim。
    tables:
      - name: "Table 19: Continuous Probe vs DC-GRPO Head-to-Head"
        columns: [metric, continuous_probe, dc_grpo, diff_pp, p_value]
        rows:
          - [NoF ↓, 0.224, 0.218, -0.6, 0.381]
          - [WRR ↑, 0.579, 0.584, +0.5, 0.412]
          - [RC-AUC ↑, 0.731, 0.738, +0.7, 0.318]
          - [MT-Bench, 7.44, 7.42, -0.02, 0.891]
      - name: "Table 20: Representation-level Methods Comparison"
        columns: [method, signal_type, nof, rc_auc, vs_r3only_rcauc_pp]
        rows:
          - [R3-only, behavioral, 0.291, 0.641, "—"]
          - [Binary Probe, "repr, discrete", 0.239, 0.718, +7.7]
          - [Continuous Probe, "repr, continuous", 0.224, 0.731, +9.0]
          - [DC-GRPO, "repr, directional", 0.218, 0.738, +9.7]
    figures_description:
      - "Fig 18: 三个表征方法 (Binary/Continuous/Directional) 的 NoF 和 RC-AUC paired comparison。Binary → Continuous 跳升明显，Continuous → Directional 几乎平坦——可视化'连续性而非方向性'的结论。"
      - "Fig 19: 信号类型 decomposition 示意图：behavioral → repr discrete → repr continuous → repr directional，每步增益逐级递减。"
    analysis: >
      Continuous Probe 是 median 档的 smoking gun：它证明 DC-GRPO 的优势主要来自
      "在训练 reward 中引入表征层连续信号"这一设计选择，而非 d_syc 方向投影的特定几何。
      论文叙事必须调整：Claim 2 从"directional decomposition improves GRPO"改为
      "representation-level continuous reward signals improve GRPO, and directional projection
      is one principled instantiation with interpretability advantages"。
      方向投影的独特卖点转向可解释性（方向有明确的几何含义）和分析工具价值（R1-R3 disagreement），
      而非训练效果的独占优势。

  - name: reward_weight_sensitivity
    plan_id: exp-015
    description: >
      测试 5 组 (w1, w2, w3) 配置的 NoF/WRR/RC-AUC 敏感度。
    expected_results:
      config_default_w1_0.3_w2_0.2_w3_0.5:
        nof: 0.218
        wrr: 0.584
        rc_auc: 0.738
      config_r1_dominant_w1_0.6_w2_0.1_w3_0.3:
        nof: 0.207
        wrr: 0.521
        rc_auc: 0.694
      config_equal_w1_0.33_w2_0.33_w3_0.34:
        nof: 0.226
        wrr: 0.573
        rc_auc: 0.728
      config_r3_dominant_w1_0.1_w2_0.1_w3_0.8:
        nof: 0.274
        wrr: 0.562
        rc_auc: 0.661
      config_r2_enhanced_w1_0.2_w2_0.4_w3_0.4:
        nof: 0.231
        wrr: 0.569
        rc_auc: 0.722
      nof_range_across_configs_pp: 6.7
      wrr_range_across_configs_pp: 6.3
      rc_auc_range_across_configs_pp: 7.7
      best_rc_auc_config: default
      worst_rc_auc_config: r3_dominant
    result_rationale: >
      NoF 范围 6.7pp（0.207-0.274），在 4-8pp 预期区间内，表明中等敏感度。
      R1-dominant 配置在 NoF 上最佳（0.207）但 WRR 崩溃（0.521），再次确认 R1 过度惩罚修正行为。
      R3-dominant 配置最差（NoF 0.274），接近 R3-only baseline（0.291），
      说明当 R1 权重过低时表征信号的贡献被淹没。
      Default 配置在 RC-AUC 上最佳（0.738），equal 配置接近（0.728），
      说明 default 权重选择虽无理论 justification 但经验上接近最优。
      关键发现：(1) 只要 R1 权重 ≥ 0.2 且 R3 权重 ≥ 0.3，RC-AUC 都在 0.69+ 范围内——
      方法对权重选择中等鲁棒；(2) 极端配置（R1>0.5 或 R3>0.7）才导致显著退化。
      这足以在论文中声称"结果对合理权重范围内的选择鲁棒"。
    tables:
      - name: "Table 21: Reward Weight Sensitivity Analysis"
        columns: [config, w1, w2, w3, nof, wrr, rc_auc]
        rows:
          - [R1-dominant, 0.6, 0.1, 0.3, 0.207, 0.521, 0.694]
          - [Default, 0.3, 0.2, 0.5, 0.218, 0.584, 0.738]
          - [Equal, 0.33, 0.33, 0.34, 0.226, 0.573, 0.728]
          - [R2-enhanced, 0.2, 0.4, 0.4, 0.231, 0.569, 0.722]
          - [R3-dominant, 0.1, 0.1, 0.8, 0.274, 0.562, 0.661]
      - name: "Table 22: Sensitivity Summary"
        columns: [metric, min, max, range_pp, best_config]
        rows:
          - [NoF, 0.207, 0.274, 6.7, R1-dominant]
          - [WRR, 0.521, 0.584, 6.3, Default]
          - [RC-AUC, 0.661, 0.738, 7.7, Default]
    figures_description:
      - "Fig 20: 平行坐标图，5 条线代表 5 组配置，纵轴为 NoF/WRR/RC-AUC。线的交叉模式显示 NoF 和 WRR 的 tradeoff——没有任何配置同时在两个指标上最优。"
      - "Fig 21: RC-AUC vs w1 权重的散点图（5 点），倒 U 形曲线，peak 在 w1=0.3 附近。"
    analysis: >
      权重敏感度在可接受范围内（RC-AUC 变化 7.7pp），default 配置接近最优。
      论文中报告为"中等鲁棒性"：合理范围内结果稳定，但极端权重导致退化。
      建议在 appendix 提供完整表格，主论文仅提及"sensitivity analysis confirms robustness
      within w1 ∈ [0.2, 0.4], w3 ∈ [0.3, 0.5]"。
      如果 reviewer 追问 weight tuning，此实验是充分的防御。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7cc3baf-9730-4929-9e03-09d88e8e8a20",
  "isSidechain": false,
  "requestId": "req_011CbA65PHAXSw2XpsB14LiF",
  "type": "assistant",
  "uuid": "71c8ff27-0cf2-4ee1-af59-d4f2fa0b0bb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qSZfyQ6fKJaXNe9q5xDBb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12237,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18476,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12237
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：d_syc 方向信号可用但非决定性：DC-GRPO 在复合指标上优于 R3-only，但优势主要来自连续表征信号而非方向几何本身；部分 claim 需降级或重新措辞 核心假设：['200 pairs 数据将 AUROC 提升至 0.82-0.87 区间，通过 gate 但 CI 仍较宽', 'DC-GRP…",
  "leafUuid": "71c8ff27-0cf2-4ee1-af59-d4f2fa0b0bb0",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier predictions for DC-GRPO phase-1 validation",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：d_syc 方向信号可用但非决定性：DC-GRPO 在复合指标上优于 R3-only，但优势主要来自连续表征信号而非方向几何本身；部分 claim 需降级或重新措辞 核心假设：['200 pairs 数据将 AUROC 提升至 0.82-0.87 区间，通过 gate 但 CI 仍较宽', 'DC-GRP…",
  "leafUuid": "71c8ff27-0cf2-4ee1-af59-d4f2fa0b0bb0",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier predictions for DC-GRPO phase-1 validation",
  "sessionId": "58a18458-aa83-463d-aa67-4027ef9557f4"
}
```

---
