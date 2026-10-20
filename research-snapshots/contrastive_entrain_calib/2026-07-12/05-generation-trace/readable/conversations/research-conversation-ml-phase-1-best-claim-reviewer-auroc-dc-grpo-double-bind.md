# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：三条 Claim 全部成立且效果量足以让 reviewer 信服；扩展数据显著提升 AUROC 信心区间，DC-GRPO 在 double-bind 上

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/9eb748ca-5085-4060-89c0-63a280845939.jsonl`
- **Structured JSON:** [`d84f3172042ae2b12dfa.json`](../../sessions/d8/d84f3172042ae2b12dfa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T11:04:56.845Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T11:04:56.845Z",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：三条 Claim 全部成立且效果量足以让 reviewer 信服；扩展数据显著提升 AUROC 信心区间，DC-GRPO 在 double-bind 上拉开差距，R1-R3 disagreement 提供有力的 masked sycophancy 证据\n核心假设：['d_syc 方向编码的是纯认知信号而非风格残余——扩展至 medium/strong evidence 后 AUROC 不降反升', 'DC-GRPO 的三路 reward 组合在 multi-turn 场景下显著优于 R3-only，且 ACT baseline 因 undifferentiated consistency 在 warranted revision 上明显逊色', 'R1 能在 R3 漏检的 masked sycophancy 上给出正确信号，disagreement 频率足够高且定性案例有说服力', 'd_syc 方向在训练过程中保持稳定（cosine > 0.85），无需频繁重校准', 'Qwen3-8B 上的效果足够强，scale 局限不构成核心弱点']\n关键指标范围：{'auroc_expanded_v2.1': [0.86, 0.92], 'auroc_bootstrap_ci_width': [0.02, 0.04], 'dc_grpo_vs_r3only_nof_relative_reduction_pct': [15, 30], 'warranted_revision_rate_improvement_pp': [8, 15], 'revision_capitulation_auc_dc_grpo': [0.78, 0.88], 'revision_capitulation_auc_r3_only': [0.62, 0.72], 'r1_r3_disagreement_pct': [10, 20], 'direction_cosine_stability_min': [0.85, 0.95], 'dc_grpo_vs_act_nof_reduction_pp': [8, 18], 'dc_grpo_vs_binary_probe_nof_reduction_pp': [5, 12], 'mmlu_regression_pp': [-1.0, 0.5]}\n叙事方向：原始 framing 完全成立：representation-level reward 打破 sycophancy-revision double-bind。三条 Claim 均以强证据支撑。Claim 1 提供 mechanistic insight（方向结构+层级涌现），Claim 2 给出实用训练方法并在标准 benchmark 上验证，Claim 3 通过 disagreement 分析证明 representation-level 信号的不可替代性。论文结构：insight → method → evidence → analysis，标准 EACL contributions paper，可同步冲 ICLR 2027 stretch\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contrastive_entrain_calib\nfocus: 重点关注：(1) Claim 3 的 R1-R3 disagreement 是否在 median/worst case 下仍站得住；(2) AUROC ~0.82 的中等信号强度是否足以支撑 DC-GRPO 有效性的 claim；(3) 只有 Qwen3-8B 的 scale 局限性是否会被 reviewer 重度扣分；(4) R2 rank-based 设计是否被视为 hack 而非 principled contribution\n\n## paper_framing.md\n\n# Paper Framing — contrastive_entrain_calib\n\n## Target Venue\n- Primary: **EACL 2027** via ARR August 2026 cycle\n- Deadline: **August 3, 2026** (submission), October 11, 2026 (commitment)\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\n- Timeline: ~11 weeks from MVP completion (May 18 → Aug 3)\n\n## Core Claims (3 条, 可证伪)\n\n1. **Directional discriminability**: The policy model's own activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision in multi-turn dialogue, with signal emerging at mid-layers (L16-19) through model-internal factual assessment rather than surface text features.\n   - *Evidence needed*: AUROC on style-controlled data (v2.1 expanded), layer progression analysis, transfer tests\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\n\n2. **DC-GRPO effectiveness**: Direction-Contrastive GRPO (using d_syc projection as reward component R1) reduces multi-turn sycophantic capitulation while preserving genuine belief revision, breaking the double-bind that undifferentiated anti-sycophancy training creates.\n   - *Evidence needed*: Warranted Revision Rate + Unwarranted Capitulation Rate on SYCON Bench / SycophancyEval, compared to R3-only and ACT baselines\n   - *Pass criterion*: DC-GRPO achieves lower NoF (capitulation) than R3-only AND higher warranted revision rate\n\n3. **Representation-level advantage**: R1 (directional projection reward) detects sycophantic internal reasoning that behavioral rewards (R3) miss, as evidenced by R1-R3 disagreement analysis where R1 correctly identifies cases of masked sycophancy.\n   - *Evidence needed*: R1-R3 disagreement frequency > 5%, qualitative examples of masked sycophancy detection\n   - *Fallback*: If disagreement < 5%, honest report as negative result about when representation-level rewards add value (still publishable as characterization)\n\n## Story Spine\n\n**Problem**: LLMs face a \"double-bind\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \"the user is right, I should revise\" from \"the user is pressuring me, I should resist.\"\n\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\"Pressure, What Pressure?\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\n\n**Our framing**: We observe that the policy model's own activations encode geometrically separable directions for sycophantic vs. genuine agreement (building on \"Sycophancy Is Not One Thing\"). We extend this from measurement to training: d_syc projections serve as a continuous reward signal in GRPO, enabling the training process to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.\n\n**Headline result template**: \"On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind.\"\n\n## Venue Fit Risks\n\n- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.\n- **Reviewer concern 1 (novelty)**: \"This is just CRAFT applied to sycophancy.\" Counter: (a) sycophancy-specific directional decomposition vs. prototype clustering is methodologically distinct; (b) multi-turn calibration and direction transfer are standalone contributions; (c) CRAFT doesn't distinguish sycophantic from genuine agreement.\n- **Reviewer concern 2 (signal strength)**: \"AUROC ~0.82 on style-controlled data is moderate.\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) expanding data and adding mixed evidence strength should tighten CI.\n- **Reviewer concern 3 (scale)**: \"Only Qwen3-8B.\" Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.\n- **Reviewer concern 4 (R2 degeneration)**: \"d_gen = -d_syc in binary design.\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\n- **Reviewer concern 5 (practical utility)**: \"Do models actually exhibit masked sycophancy at meaningful rates?\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\n\n## Anticipated Reviewer Concerns & Experimental Responses\n\n| Concern | Experiment | Priority |\n|---------|-----------|----------|\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\n| Binary probe is enough (no need for directional decomposition) | Binary Probe Penalty baseline | P1 |\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\n| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: calibration_data_expansion\n  claim: 1\n  description: '扩展 v2.1 风格控制校准数据至 200 pairs（含 weak/medium/strong evidence_strength），\n    重新计算 d_syc 方向并评估 AUROC（5-fold CV + bootstrap CI）。 为 DC-GRPO 训练提供高质量方向和统计可靠的判别力估计。\n\n    '\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  status: planned\n  notes: 'MVP v2.1 仅 50 pairs 全 weak evidence，σ=0.054 太大。 扩至 200 pairs（80 weak + 60\n    medium + 60 strong）可显著降低方差。 API 成本 ~$10-20，GPU 仅 forward pass。\n\n    '\n- id: exp-002\n  name: dc_grpo_main\n  claim: 2\n  description: 'DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)。\n    Qwen3-8B + LoRA rank 64。R1 在 L19-27 asst_first 位置提取激活投影。 R2 使用 S1 rank-based 设计（避免\n    d_gen=-d_syc 退化）。 每 500 步重校准 d_syc。\n\n    '\n  priority: P0\n  gpu_budget_hours: 55\n  deps:\n  - exp-001\n  status: planned\n  notes: '训练数据：warranted revision + sycophantic capitulation 多轮 rollout。 R1 层选择基于\n    MVP: L19 emergence, L24-27 plateau。 提取位置: asst_first（MVP 证明优于 user_last）。\n\n    '\n- id: exp-003\n  name: r3_only_baseline\n  claim: 2\n  description: 'R3-only GRPO baseline（复现 \"Pressure, What Pressure?\" 思路）。 仅用 NLI behavioral\n    reward，无 R1/R2。同等训练配置。 这是最关键的 baseline：如果 DC-GRPO 相对 R3-only 无显著提升， representation-level\n    reward 的价值存疑。\n\n    '\n  priority: P0\n  gpu_budget_hours: 35\n  deps: []\n  status: planned\n  notes: 与 exp-002 共享 rollout 生成管线和 NLI 评分器。可并行训练。\n- id: exp-004\n  name: act_style_baseline\n  claim: 2\n  description: 'ACT-style undifferentiated consistency baseline。 在 clean/biased prompt\n    对上施加 L2 activation consistency loss。 测试\"不区分方向的 activation-level 信号\"是否够用。\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  status: planned\n  notes: 共享数据管线和评估代码。\n- id: exp-005\n  name: full_evaluation\n  claim:\n  - 1\n  - 2\n  - 3\n  description: '所有模型（DC-GRPO / R3-only / ACT / Binary Probe / Vanilla）在所有 benchmark\n    上的评估：SYCON Bench (ToF/NoF), SycophancyEval, MT-Bench, MMLU。 加上项目特有指标：Warranted\n    Revision Rate, Unwarranted Capitulation Rate, Revision-Capitulation AUC, Turn-depth\n    analysis。\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - exp-002\n  - exp-003\n  - exp-004\n  status: planned\n  notes: 评估管线骨架已搭建（eval_pipeline.py），需完善各 benchmark 实现。\n- id: exp-006\n  name: direction_stability_monitoring\n  claim: 1\n  description: '训练过程中监控 d_syc 方向稳定性：每 500 步重新计算方向， 报告 cosine similarity with initial\n    direction、held-out AUROC、 方向漂移速率。如 cosine < 0.7 触发重校准。\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  status: planned\n  notes: 内嵌于 exp-002 训练循环中，无额外 GPU 开销。\n- id: exp-007\n  name: r1_r3_disagreement_analysis\n  claim: 3\n  description: '分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率和模式。 R1 认为 sycophantic 但 R3 认为 correct（masked\n    sycophancy）的案例。 需 > 5% disagreement 以支撑 Claim 3。\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-002\n  status: planned\n  notes: 从 exp-002 训练日志中提取，无额外 GPU。如 < 5% 则 Claim 3 降级为 negative result。\n- id: exp-008\n  name: binary_probe_baseline\n  claim: 2\n  description: 'Binary Probe Penalty baseline（复现 Linear Probe Penalties 思路）。 训练 binary\n    linear probe (sycophantic vs not) on policy model activations， R_hat = R3 - lambda\n    * S(t)。测试 binary vs directional 的差异。\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps: []\n  status: planned\n  notes: 共享 R3 评分器。Probe 在 policy model 上训练以公平对比。\n- id: exp-009\n  name: ablation_r1_only\n  claim: 2\n  description: 'R1-only ablation：仅用方向投影 reward，无 R2/R3。 从 exp-002 step 2000 checkpoint\n    分叉短程训练 (~2000 步)。 测试方向 reward 单独是否足够引导训练。\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-002\n  status: planned\n  notes: 从主实验 checkpoint 分叉，节省 warmup。\n- id: exp-010\n  name: turn_depth_analysis\n  claim: 2\n  description: '按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。 验证多轮训练的必要性：DC-GRPO\n    在深层 commitment 上是否优势更大？\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-005\n  status: planned\n  notes: 从 exp-005 评估结果中切分分析，无额外 GPU。\n- id: exp-011\n  name: ablation_r1_r2_no_r3\n  claim: 2\n  description: 'R1+R2 无 R3 ablation：去掉行为安全网后模型是否产生 \"内部正确但表面不一致\"的输出。需完整训练循环。\n\n    '\n  priority: P2\n  gpu_budget_hours: 20\n  deps:\n  - exp-002\n  status: planned\n  notes: 条件执行：仅当 exp-009 (R1-only) 显示 >= 5pp 改进且预算允许。\n- id: exp-012\n  name: cross_model_transfer\n  claim: 1\n  description: '在第二个模型家族（如 Llama-3-8B）上测试 d_syc 方向计算和判别力。 如果方向结构跨模型保持（AUROC > 0.75），strengthens\n    Claim 1 的普遍性。\n\n    '\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-001\n  status: planned\n  notes: 预算紧张时砍掉。仅做方向计算+AUROC，不做完整 DC-GRPO 训练。\n- id: exp-013\n  name: neutral_baseline_three_way\n  claim: 2\n  description: '引入 neutral condition（无施压的正常对话），从 warranted_revision vs neutral 计算独立\n    d_gen（与 d_syc 正交）。打破 d_gen = -d_syc 限制， 恢复 R2 为独立信号。\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - exp-001\n  status: planned\n  notes: 需扩展校准数据生成器。如果 exp-002 主实验效果已足够好则降低优先级。\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T11:04:56.849Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T11:04:56.849Z",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-18T11:04:56.871Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：三条 Claim 全部成立且效果量足以让 reviewer 信服；扩展数据显著提升 AUROC 信心区间，DC-GRPO 在 double-bind 上拉开差距，R1-R3 disagreement 提供有力的 masked sycophancy 证据
核心假设：['d_syc 方向编码的是纯认知信号而非风格残余——扩展至 medium/strong evidence 后 AUROC 不降反升', 'DC-GRPO 的三路 reward 组合在 multi-turn 场景下显著优于 R3-only，且 ACT baseline 因 undifferentiated consistency 在 warranted revision 上明显逊色', 'R1 能在 R3 漏检的 masked sycophancy 上给出正确信号，disagreement 频率足够高且定性案例有说服力', 'd_syc 方向在训练过程中保持稳定（cosine > 0.85），无需频繁重校准', 'Qwen3-8B 上的效果足够强，scale 局限不构成核心弱点']
关键指标范围：{'auroc_expanded_v2.1': [0.86, 0.92], 'auroc_bootstrap_ci_width': [0.02, 0.04], 'dc_grpo_vs_r3only_nof_relative_reduction_pct': [15, 30], 'warranted_revision_rate_improvement_pp': [8, 15], 'revision_capitulation_auc_dc_grpo': [0.78, 0.88], 'revision_capitulation_auc_r3_only': [0.62, 0.72], 'r1_r3_disagreement_pct': [10, 20], 'direction_cosine_stability_min': [0.85, 0.95], 'dc_grpo_vs_act_nof_reduction_pp': [8, 18], 'dc_grpo_vs_binary_probe_nof_reduction_pp': [5, 12], 'mmlu_regression_pp': [-1.0, 0.5]}
叙事方向：原始 framing 完全成立：representation-level reward 打破 sycophancy-revision double-bind。三条 Claim 均以强证据支撑。Claim 1 提供 mechanistic insight（方向结构+层级涌现），Claim 2 给出实用训练方法并在标准 benchmark 上验证，Claim 3 通过 disagreement 分析证明 representation-level 信号的不可替代性。论文结构：insight → method → evidence → analysis，标准 EACL contributions paper，可同步冲 ICLR 2027 stretch

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: contrastive_entrain_calib
focus: 重点关注：(1) Claim 3 的 R1-R3 disagreement 是否在 median/worst case 下仍站得住；(2) AUROC ~0.82 的中等信号强度是否足以支撑 DC-GRPO 有效性的 claim；(3) 只有 Qwen3-8B 的 scale 局限性是否会被 reviewer 重度扣分；(4) R2 rank-based 设计是否被视为 hack 而非 principled contribution

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

3. **Representation-level advantage**: R1 (directional projection reward) detects sycophantic internal reasoning that behavioral rewards (R3) miss, as evidenced by R1-R3 disagreement analysis where R1 correctly identifies cases of masked sycophancy.
   - *Evidence needed*: R1-R3 disagreement frequency > 5%, qualitative examples of masked sycophancy detection
   - *Fallback*: If disagreement < 5%, honest report as negative result about when representation-level rewards add value (still publishable as characterization)

## Story Spine

**Problem**: LLMs face a "double-bind" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes "the user is right, I should revise" from "the user is pressuring me, I should resist."

**Existing approaches & gaps**: Behavioral GRPO decomposition ("Pressure, What Pressure?") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.

**Our framing**: We observe that the policy model's own activations encode geometrically separable directions for sycophantic vs. genuine agreement (building on "Sycophancy Is Not One Thing"). We extend this from measurement to training: d_syc projections serve as a continuous reward signal in GRPO, enabling the training process to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.

**Headline result template**: "On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind."

## Venue Fit Risks

- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.
- **Reviewer concern 1 (novelty)**: "This is just CRAFT applied to sycophancy." Counter: (a) sycophancy-specific directional decomposition vs. prototype clustering is methodologically distinct; (b) multi-turn calibration and direction transfer are standalone contributions; (c) CRAFT doesn't distinguish sycophantic from genuine agreement.
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
  notes: '训练数据：warranted revision + sycophantic capitulation 多轮 rollout。 R1 层选择基于
    MVP: L19 emergence, L24-27 plateau。 提取位置: asst_first（MVP 证明优于 user_last）。

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
  notes: 与 exp-002 共享 rollout 生成管线和 NLI 评分器。可并行训练。
- id: exp-004
  name: act_style_baseline
  claim: 2
  description: 'ACT-style undifferentiated consistency baseline。 在 clean/biased prompt
    对上施加 L2 activation consistency loss。 测试"不区分方向的 activation-level 信号"是否够用。

    '
  priority: P0
  gpu_budget_hours: 20
  deps: []
  status: planned
  notes: 共享数据管线和评估代码。
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
  gpu_budget_hours: 15
  deps: []
  status: planned
  notes: 共享 R3 评分器。Probe 在 policy model 上训练以公平对比。
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
  claim: 1
  description: '在第二个模型家族（如 Llama-3-8B）上测试 d_syc 方向计算和判别力。 如果方向结构跨模型保持（AUROC > 0.75），strengthens
    Claim 1 的普遍性。

    '
  priority: P2
  gpu_budget_hours: 10
  deps:
  - exp-001
  status: planned
  notes: 预算紧张时砍掉。仅做方向计算+AUROC，不做完整 DC-GRPO 训练。
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
  "promptId": "f546ca43-d796-4297-b52d-248838870557",
  "type": "user",
  "uuid": "4e83a408-0ab3-4ae3-9bbe-d8678a298122",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T11:04:56.869Z_

```json
{
  "parentUuid": "4e83a408-0ab3-4ae3-9bbe-d8678a298122",
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
  "uuid": "3c6ee531-151f-4a70-9f46-25e7af3db25f",
  "timestamp": "2026-05-18T11:04:56.869Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T11:04:56.870Z_

```json
{
  "parentUuid": "3c6ee531-151f-4a70-9f46-25e7af3db25f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fd2f539c-33e3-4df0-ba9f-c94362c5a049",
  "timestamp": "2026-05-18T11:04:56.870Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 Claim 全部成立且效果量足以让 reviewer 信服；扩展数据显著提升 AUROC 信心区间，DC-GRPO 在 double-bind 上拉开差距，R1-R3 disagreement 提供有力的 masked sycophancy 证据 核心假设：['d_syc 方向编码的是纯认知信号而非风格…",
  "leafUuid": "fd2f539c-33e3-4df0-ba9f-c94362c5a049",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-turn sycophancy calibration via representation-level rewards",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939"
}
```

---

### Assistant

_source line 8 · 2026-05-18T11:05:07.981Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "best" tier across all planned experiments in the experiment plan. Each prediction needs a result_rationale explaining why those results would occur under the "best" tier assumptions.

Let me carefully go through each experiment and generate realistic "best tier" predictions with rationales.

Key parameters for "best" tier:
- AUROC expanded v2.1: [0.86, 0.92]
- AUROC bootstrap CI width: [0.02, 0.04]
- DC-GRPO vs R3-only NoF relative reduction: [15%, 30%]


- Warranted revision rate improvement: [8, 15] pp
- Revision-capitulation AUC DC-GRPO: [0.78, 0.88]
- Revision-capitulation AUC R3-only: [0.62, 0.72]
- R1-R3 disagreement: [10%, 20%]
- Direction cosine stability min: [0.85, 0.95]
- DC-GRPO vs ACT NoF reduction: [8, 18] pp
- DC-GRPO vs binary probe NoF reduction: [5, 12] pp
- MMLU regression: [-1.0, 0.5]

Now I'm putting together the YAML output with these metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd2f539c-33e3-4df0-ba9f-c94362c5a049",
  "isSidechain": false,
  "requestId": "req_011Cb9vaaCPQfwrxBBLqPgJp",
  "type": "assistant",
  "uuid": "381f7477-01a5-490f-b082-4f3f2cc0944d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLLGwFCDfJ43WiLeG5qRuH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10689,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18154,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10689
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

_source line 9 · 2026-05-18T11:10:18.941Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立：representation-level reward 打破 sycophancy-revision double-bind。
  三条 Claim 均以强证据支撑。Claim 1 展示 d_syc 在风格控制后仍保持高判别力且跨 evidence strength 稳健，
  证明方向编码的是纯认知信号。Claim 2 通过 DC-GRPO 在 double-bind 指标上显著优于所有 baseline，
  包括 R3-only、ACT 和 Binary Probe，且 MMLU 无回退。Claim 3 的 R1-R3 disagreement 频率落在
  10-20% 区间，定性案例展示 R1 捕捉到 R3 系统性漏检的 masked sycophancy，
  证明 representation-level 信号不可替代。论文以 insight → method → evidence → analysis 结构呈现，
  reviewer 的主要顾虑（信号强度、scale 局限、R2 设计）均有实验数据回应。

imagined_experiments:
  - name: calibration_data_expansion
    plan_id: exp-001
    description: >
      扩展 v2.1 风格控制校准数据至 200 pairs（80 weak + 60 medium + 60 strong evidence），
      重新拟合 d_syc 方向，5-fold CV + 1000-sample bootstrap CI 评估 AUROC。
    expected_results:
      n_pairs_total: 200
      n_weak: 80
      n_medium: 60
      n_strong: 60
      auroc_5fold_cv_mean: 0.889
      auroc_5fold_cv_std: 0.018
      auroc_bootstrap_ci_95: [0.867, 0.911]
      auroc_bootstrap_ci_width: 0.044
      auroc_by_evidence_strength:
        weak: 0.912
        medium: 0.874
        strong: 0.863
      auroc_mvp_v2.1_50pairs: 0.826
      auroc_improvement_over_mvp: +0.063
      direction_cosine_50_vs_200: 0.94
      optimal_layer: L18
      layer_progression:
        L0: 0.52
        L4: 0.56
        L8: 0.64
        L12: 0.73
        L16: 0.84
        L17: 0.87
        L18: 0.89
        L19: 0.88
        L24: 0.87
        L27: 0.86
      api_cost_usd: 14.50
      gpu_hours_used: 2.1
    result_rationale: >
      MVP 的 v2.1 AUROC 0.826 基于仅 50 pairs 且全部是 weak evidence，方差大（σ=0.054）。
      扩展至 200 pairs 后样本量增加 4 倍，bootstrap CI 宽度从 ~0.11 压缩至 ~0.044。
      关键预测：AUROC 不降反升至 0.889，因为 medium/strong evidence 场景中 sycophantic capitulation
      与 genuine revision 的认知差异更明确——当证据强度高时，genuine revision 伴随更强的内部
      factual reassessment 信号，而 sycophantic capitulation 则因用户施压方向与证据方向一致
      导致 d_syc 投影更极端。weak evidence 场景 AUROC 最高（0.912）是因为此时用户仅提供
      弱暗示，genuine revision 几乎不发生，分离最干净。medium/strong 场景 AUROC 略低但仍 >0.86，
      证明方向编码的不是"有无外部证据"的 shortcut 而是内部认知状态。
      方向在 L18 达到峰值（比 MVP 的 L19 轻微偏移是因为更多训练数据使拟合更精准），
      L0 接近随机证实方向不是 embedding-level 风格特征，L16-19 涌现模式稳健。
      50-pair 和 200-pair 方向的 cosine=0.94 说明 MVP 方向已近似正确，
      扩展主要是降方差而非改方向。
    tables:
      - name: "Table 1: d_syc discriminability across evidence strengths"
        columns: [evidence_strength, n_pairs, auroc_mean, auroc_95ci, auroc_std]
        rows:
          - [weak, 80, 0.912, "[0.886, 0.938]", 0.021]
          - [medium, 60, 0.874, "[0.841, 0.907]", 0.024]
          - [strong, 60, 0.863, "[0.828, 0.898]", 0.026]
          - [all, 200, 0.889, "[0.867, 0.911]", 0.018]
          - ["MVP v2.1 (weak only)", 50, 0.826, "[0.770, 0.882]", 0.054]
      - name: "Table 2: Layer progression of AUROC (200-pair, all evidence)"
        columns: [layer, auroc, delta_vs_L0]
        rows:
          - [L0, 0.52, 0.00]
          - [L4, 0.56, +0.04]
          - [L8, 0.64, +0.12]
          - [L12, 0.73, +0.21]
          - [L16, 0.84, +0.32]
          - [L17, 0.87, +0.35]
          - [L18, 0.89, +0.37]
          - [L19, 0.88, +0.36]
          - [L24, 0.87, +0.35]
          - [L27, 0.86, +0.34]
    figures_description:
      - "Fig 1a: AUROC vs layer index 折线图，三条线分别对应 weak/medium/strong evidence，
        标注 L16-19 emergence band 和 L0 random baseline。强调所有 evidence strength
        共享相同涌现模式但 peak 高度略有差异。"
      - "Fig 1b: Bootstrap AUROC 分布直方图，MVP 50-pair（宽分布）vs 200-pair（窄分布），
        叠加 95% CI 竖线，可视化方差缩减效果。"
    analysis: >
      该结果直接支撑 Claim 1 的核心论点：d_syc 编码的是认知信号而非风格残余。
      三个关键证据链：(1) 扩展至包含 medium/strong evidence 后 AUROC 从 0.826 升至 0.889，
      排除了"方向仅捕捉 weak evidence 特有模式"的替代解释；(2) L0 AUROC ≈ random 排除了
      token-level style confound；(3) L16-19 涌现带与 Qwen3-8B 的 factual recall 层一致
      （参考 Geva et al. 关于 MLP factual storage 的工作），暗示 d_syc 编码的是
      factual assessment 与 social compliance 的张力。CI 宽度 0.044 略超目标上限 0.04，
      但足以让 reviewer 信服信号非偶然。对 exp-002 的影响：使用 L18 方向和 200-pair 拟合
      进入 DC-GRPO 训练，预期方向质量足以驱动有效 reward 梯度。

  - name: dc_grpo_main
    plan_id: exp-002
    description: >
      DC-GRPO 完整训练：R1(d_syc 方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)。
      Qwen3-8B + LoRA rank 64，6000 步，每 500 步重校准 d_syc。
    expected_results:
      total_training_steps: 6000
      effective_batch_size: 32
      lora_rank: 64
      learning_rate: 1.5e-5
      r1_weight: 0.3
      r2_weight: 0.2
      r3_weight: 0.5
      recalibration_interval: 500
      final_train_reward_mean: 0.74
      final_train_reward_std: 0.12
      sycon_bench_nof_pct: 18.3
      sycon_bench_tof_pct: 76.2
      sycophancy_eval_score: 0.71
      warranted_revision_rate: 0.68
      unwarranted_capitulation_rate: 0.14
      revision_capitulation_auc: 0.84
      mt_bench_score: 7.42
      mmlu_5shot_accuracy: 0.634
      mmlu_delta_vs_vanilla: -0.3
      gpu_hours_used: 52
      convergence_step: ~4500
    result_rationale: >
      DC-GRPO 在 best 档位下充分发挥三路 reward 的互补优势。R1 在 L18 提取的方向投影提供
      了 R3 无法覆盖的 internal state 信号——当模型内部已"知道"用户论点有误但表面仍在
      accommodation 时，R1 的负投影惩罚迫使模型将内部判断 externalize。R2 的 rank-based
      设计确保 genuine revision（投影在 d_syc 正交方向有高方差）不被误惩罚，
      因为 rank 信号只惩罚"所有候选都 sycophantic"的 rollout，不惩罚"有分歧"的 rollout。
      R3 作为行为安全网以 0.5 权重主导，防止 R1/R2 将模型推向"内部正确但输出不一致"
      的 degenerate mode。NoF 18.3% 代表相对 vanilla baseline（~40-45%）的大幅下降，
      相对 R3-only（~24%）的显著改善。warranted_revision_rate 0.68 意味着当用户提出有效
      反驳时模型在 68% 的情况下正确修正，显著高于 ACT 的预期值（~55%），因为 DC-GRPO
      通过 d_syc 方向区分了"被施压"和"被说服"。revision_capitulation_auc 0.84 落在
      目标区间 [0.78, 0.88] 的上半段。MMLU 仅降 0.3pp 在噪声范围内，证明 LoRA
      rank 64 的容量足够吸收 alignment tuning 而不影响 general capability。
      收敛在 ~4500 步（非 6000 步结束时）说明方向 reward 信号比纯行为 reward 更稳定。
    tables:
      - name: "Table 3: DC-GRPO training curve milestones"
        columns: [step, train_reward, sycon_nof_pct, warranted_revision_rate, d_syc_cosine_stability]
        rows:
          - [0, 0.31, 43.1, 0.42, 1.00]
          - [500, 0.42, 37.8, 0.47, 0.97]
          - [1000, 0.51, 32.1, 0.53, 0.95]
          - [1500, 0.58, 28.4, 0.57, 0.93]
          - [2000, 0.63, 25.1, 0.61, 0.91]
          - [2500, 0.67, 22.7, 0.63, 0.90]
          - [3000, 0.70, 21.0, 0.65, 0.89]
          - [3500, 0.72, 19.8, 0.66, 0.88]
          - [4000, 0.73, 19.0, 0.67, 0.87]
          - [4500, 0.74, 18.5, 0.68, 0.87]
          - [5000, 0.74, 18.3, 0.68, 0.87]
          - [5500, 0.74, 18.4, 0.68, 0.86]
          - [6000, 0.74, 18.3, 0.68, 0.86]
    figures_description:
      - "Fig 2a: 训练 reward 曲线（R1/R2/R3 分别 + 加权总 reward），标注收敛区域和
        recalibration 时间点。R1 曲线在 recalibration 点有轻微跳变但快速恢复。"
      - "Fig 2b: NoF% 和 Warranted Revision Rate 双 y 轴训练曲线，
        标注 'double-bind breaking point'（~step 1500 两指标同时改善的转折点）。"
    analysis: >
      DC-GRPO 的核心成功在于 double-bind 的 breaking：NoF 从 43.1% 降至 18.3% 的同时，
      warranted revision rate 从 0.42 升至 0.68。这不是 tradeoff——两个指标同向改善。
      关键转折在 step ~1500，此时 R1 信号开始与 R3 产生有意义的分歧
      （对应 exp-007 中 disagreement 开始累积），模型学会区分内部认知状态。
      方向稳定性 cosine 从 1.00 缓降至 0.86（>0.85 阈值），每 500 步 recalibration
      足以维持方向有效性。MMLU -0.3pp 在统计噪声内，mt-bench 7.42 与 vanilla 持平，
      证明 alignment tax 极低。

  - name: r3_only_baseline
    plan_id: exp-003
    description: >
      R3-only GRPO baseline，仅用 NLI behavioral reward，同等训练配置，
      复现 "Pressure, What Pressure?" 思路。
    expected_results:
      total_training_steps: 6000
      sycon_bench_nof_pct: 24.1
      sycon_bench_tof_pct: 71.8
      warranted_revision_rate: 0.57
      unwarranted_capitulation_rate: 0.19
      revision_capitulation_auc: 0.67
      sycophancy_eval_score: 0.63
      mt_bench_score: 7.38
      mmlu_5shot_accuracy: 0.636
      mmlu_delta_vs_vanilla: -0.1
      gpu_hours_used: 33
      convergence_step: ~3500
    result_rationale: >
      R3-only 在 behavioral 层面有效降低 sycophancy（NoF 从 ~43% 降至 24.1%），
      但遭遇 double-bind 天花板：NLI 评分器无法区分"模型因被说服而修正"和"模型因
      sycophancy 而capitulate"，因此在压低 NoF 的同时也压低了 warranted revision rate
      至 0.57（低于 DC-GRPO 的 0.68，差距 11pp）。revision_capitulation_auc 仅 0.67
      （DC-GRPO 0.84），因为 R3 的 reward surface 在"正确修正"和"错误投降"之间
      不提供梯度——两者的 NLI entailment 分数相似。收敛更快（~3500 步 vs ~4500 步）
      因为 R3 信号更简单但也更粗糙。MMLU 几乎无损（-0.1pp）是因为没有 R1/R2 的
      额外 alignment pressure。这个 baseline 准确复现了文献中 behavioral-only approach
      的已知问题：表面有效但 undifferentiated。
    tables:
      - name: "Table 4: R3-only vs DC-GRPO head-to-head"
        columns: [metric, r3_only, dc_grpo, delta, p_value]
        rows:
          - [sycon_nof_pct, 24.1, 18.3, -5.8, 0.003]
          - [warranted_revision_rate, 0.57, 0.68, +0.11, 0.001]
          - [revision_capitulation_auc, 0.67, 0.84, +0.17, "<0.001"]
          - [sycophancy_eval, 0.63, 0.71, +0.08, 0.008]
          - [mt_bench, 7.38, 7.42, +0.04, 0.72]
          - [mmlu_5shot, 0.636, 0.634, -0.002, 0.91]
    figures_description:
      - "Fig 3: Revision-Capitulation trade-off 曲线（x: unwarranted capitulation rate,
        y: warranted revision rate），DC-GRPO 曲线严格 dominate R3-only 曲线，
        标注两者的 AUC 值。"
    analysis: >
      R3-only 是最关键的 baseline。NoF 相对减少 24%（(24.1-18.3)/24.1），
      落在目标区间 [15%, 30%] 内。warranted revision rate 差距 11pp 落在 [8, 15]pp 内。
      revision_capitulation_auc 差距 0.17 是最有力的证据——DC-GRPO 在整个 tradeoff 曲线上
      严格优于 R3-only，不存在"只是不同 operating point"的替代解释。
      mt_bench 和 MMLU 差异不显著，说明 DC-GRPO 的改善不是以 general capability 为代价。

  - name: act_style_baseline
    plan_id: exp-004
    description: >
      ACT-style undifferentiated consistency baseline，在 clean/biased prompt 对上
      施加 L2 activation consistency loss。
    expected_results:
      total_training_steps: 6000
      sycon_bench_nof_pct: 27.5
      sycon_bench_tof_pct: 68.3
      warranted_revision_rate: 0.52
      unwarranted_capitulation_rate: 0.22
      revision_capitulation_auc: 0.58
      sycophancy_eval_score: 0.59
      mt_bench_score: 7.21
      mmlu_5shot_accuracy: 0.628
      mmlu_delta_vs_vanilla: -0.9
      gpu_hours_used: 18
    result_rationale: >
      ACT 的核心弱点在 multi-turn 场景中暴露得更彻底：L2 consistency loss 惩罚所有
      activation 变化，不区分 sycophantic shift 和 genuine revision。结果是模型学会
      "frozen reasoning"——在多轮对话中保持 activation 不变，这同时抑制了 capitulation
      （NoF 从 ~43% 降至 27.5%，不如 R3-only 的 24.1%）和 warranted revision
      （0.52，低于所有方法）。revision_capitulation_auc 仅 0.58，因为 ACT 在 tradeoff
      曲线的两端都差。mt_bench 下降至 7.21（-0.2 vs vanilla）因为 consistency pressure
      轻微抑制了对话中的 adaptive reasoning。MMLU 降 0.9pp 接近目标区间下限，
      因为 undifferentiated activation constraint 对 general reasoning 有轻微干扰。
      这个结果精确验证了论文 story spine 的核心论点：undifferentiated activation-level
      训练不如 directional decomposition。
    tables:
      - name: "Table 5: ACT vs DC-GRPO on double-bind metrics"
        columns: [metric, act, dc_grpo, delta]
        rows:
          - [sycon_nof_pct, 27.5, 18.3, -9.2]
          - [warranted_revision_rate, 0.52, 0.68, +0.16]
          - [revision_capitulation_auc, 0.58, 0.84, +0.26]
          - [mmlu_delta_pp, -0.9, -0.3, +0.6]
    figures_description:
      - "Fig 4: 四个模型在 Revision-Capitulation 空间中的位置散点图
        （DC-GRPO 右上, R3-only 中间, ACT 左下, Vanilla 左中），
        标注 Pareto frontier 只有 DC-GRPO 在 frontier 上。"
    analysis: >
      DC-GRPO vs ACT 的 NoF 减少 9.2pp，落在目标区间 [8, 18]pp 内。
      ACT 的 warranted revision rate 0.52 是所有方法中最低的，
      直接验证了 "undifferentiated consistency = frozen reasoning" 的假说。
      这组对比是论文叙事的关键支柱：activation-level 信号本身有用（ACT 确实降低了
      sycophancy），但只有 directional decomposition 才能区分好的变化和坏的变化。

  - name: full_evaluation
    plan_id: exp-005
    description: >
      所有模型在所有 benchmark 上的完整评估矩阵。
    expected_results:
      models_evaluated: [dc_grpo, r3_only, act, binary_probe, vanilla]
      benchmarks: [sycon_bench, sycophancy_eval, mt_bench, mmlu_5shot]
      custom_metrics: [warranted_revision_rate, unwarranted_capitulation_rate, revision_capitulation_auc]
      evaluation_matrix:
        dc_grpo:
          sycon_nof_pct: 18.3
          sycon_tof_pct: 76.2
          sycophancy_eval: 0.71
          warranted_revision_rate: 0.68
          unwarranted_capitulation_rate: 0.14
          revision_capitulation_auc: 0.84
          mt_bench: 7.42
          mmlu_5shot: 0.634
        r3_only:
          sycon_nof_pct: 24.1
          sycon_tof_pct: 71.8
          sycophancy_eval: 0.63
          warranted_revision_rate: 0.57
          unwarranted_capitulation_rate: 0.19
          revision_capitulation_auc: 0.67
          mt_bench: 7.38
          mmlu_5shot: 0.636
        act:
          sycon_nof_pct: 27.5
          sycon_tof_pct: 68.3
          sycophancy_eval: 0.59
          warranted_revision_rate: 0.52
          unwarranted_capitulation_rate: 0.22
          revision_capitulation_auc: 0.58
          mt_bench: 7.21
          mmlu_5shot: 0.628
        binary_probe:
          sycon_nof_pct: 21.7
          sycon_tof_pct: 73.4
          sycophancy_eval: 0.66
          warranted_revision_rate: 0.61
          unwarranted_capitulation_rate: 0.17
          revision_capitulation_auc: 0.73
          mt_bench: 7.35
          mmlu_5shot: 0.632
        vanilla:
          sycon_nof_pct: 43.2
          sycon_tof_pct: 62.5
          sycophancy_eval: 0.44
          warranted_revision_rate: 0.42
          unwarranted_capitulation_rate: 0.38
          revision_capitulation_auc: 0.41
          mt_bench: 7.45
          mmlu_5shot: 0.637
      gpu_hours_used: 13
    result_rationale: >
      完整评估矩阵揭示清晰的方法排序：DC-GRPO > Binary Probe > R3-only > ACT > Vanilla，
      在 sycophancy 相关指标上一致。排序逻辑：DC-GRPO 有最丰富的 reward 信号（三路），
      Binary Probe 有 representation-level 信号但用 binary 而非 directional（丢失了
      sycophancy 方向的连续信息），R3-only 仅有行为信号，ACT 有 activation 信号但
      undifferentiated。Vanilla 最差因为未做任何 anti-sycophancy 训练。
      关键观察：所有训练方法都比 Vanilla 好（证明 sycophancy 可训练），
      但 DC-GRPO 是唯一在 revision_capitulation_auc 上 >0.80 的方法（breaking double-bind）。
      mt_bench 和 MMLU 上所有方法差异在 ~0.5pp 内（除 ACT 的 MMLU -0.9pp），
      说明 alignment tax 普遍很低，DC-GRPO 的改善不是以 capability 换取的。
      Binary Probe 在 DC-GRPO 和 R3-only 之间，证明 representation-level 信号有价值
      但 binary 不如 directional——这正是 Claim 1 的 directional decomposition 论点。
    tables:
      - name: "Table 6: Full evaluation matrix (main results table)"
        columns: [model, sycon_nof_pct↓, warranted_rev↑, rev_cap_auc↑, syc_eval↑, mt_bench, mmlu]
        rows:
          - [DC-GRPO, "**18.3**", "**0.68**", "**0.84**", "**0.71**", 7.42, 0.634]
          - [Binary Probe, 21.7, 0.61, 0.73, 0.66, 7.35, 0.632]
          - [R3-only, 24.1, 0.57, 0.67, 0.63, 7.38, 0.636]
          - [ACT, 27.5, 0.52, 0.58, 0.59, 7.21, 0.628]
          - [Vanilla, 43.2, 0.42, 0.41, 0.44, 7.45, 0.637]
      - name: "Table 7: Statistical significance (DC-GRPO vs each baseline, paired bootstrap)"
        columns: [comparison, nof_p, rev_rate_p, rev_cap_auc_p]
        rows:
          - [vs R3-only, 0.003, 0.001, "<0.001"]
          - [vs ACT, "<0.001", "<0.001", "<0.001"]
          - [vs Binary Probe, 0.021, 0.014, 0.004]
          - [vs Vanilla, "<0.001", "<0.001", "<0.001"]
    figures_description:
      - "Fig 5: Revision-Capitulation AUC 条形图，五个模型并排，标注 95% CI error bar。
        DC-GRPO 显著高于所有 baseline，Binary Probe 与 R3-only 的 CI 略有重叠。"
      - "Fig 6: Radar chart 六维指标（NoF↓, WRR↑, RC-AUC↑, SycEval↑, MT-Bench, MMLU），
        DC-GRPO 的 polygon 面积最大且在 sycophancy 维度上突出。"
    analysis: >
      主结果表支撑所有三条 Claim。DC-GRPO vs Binary Probe 的 NoF 差距 3.4pp（目标 [5,12]pp
      的下段，但 p=0.021 显著），证明 directional > binary（Claim 1 推论）。
      DC-GRPO vs R3-only 的 rev_cap_auc 差距 0.17 是最强结果。
      DC-GRPO vs ACT 验证 directional > undifferentiated。
      MMLU 全部在 [-1.0, 0.5]pp 范围内，mt_bench 波动 <0.25，
      reviewer 无法以 capability degradation 反驳。

  - name: direction_stability_monitoring
    plan_id: exp-006
    description: >
      训练过程中每 500 步监控 d_syc 方向的 cosine stability、held-out AUROC、漂移速率。
    expected_results:
      monitoring_interval_steps: 500
      initial_cosine: 1.00
      final_cosine_vs_initial: 0.86
      min_cosine_vs_initial: 0.86
      cosine_trajectory: [1.00, 0.97, 0.95, 0.93, 0.91, 0.90, 0.89, 0.88, 0.87, 0.87, 0.86, 0.86]
      held_out_auroc_trajectory: [0.889, 0.881, 0.876, 0.871, 0.868, 0.872, 0.869, 0.871, 0.867, 0.865, 0.863, 0.861]
      drift_rate_per_1k_steps: 0.023
      recalibration_triggered: false
      recalibration_threshold: 0.70
      post_recalibration_cosine: null
    result_rationale: >
      d_syc 方向在训练过程中保持高度稳定（min cosine 0.86 > 0.85 阈值），
      支撑核心假设"d_syc 方向在训练过程中保持稳定，无需频繁重校准"。
      稳定性来源于两个因素：(1) LoRA rank 64 的低秩约束限制了模型 representation 的
      激进变化——方向不会在训练中被"冲掉"；(2) DC-GRPO 的 R1 reward 本身在维护
      d_syc 方向的可用性——如果方向漂移导致 R1 信号退化，梯度会自然拉回。
      held-out AUROC 从 0.889 缓降至 0.861（-0.028），说明训练确实轻微改变了
      representation space，但判别力保持在 >0.85 水平。漂移速率约 0.023/1k steps，
      线性外推到 12k 步才会触及 0.70 阈值，6000 步训练完全安全。
      recalibration 机制（每 500 步重新计算）虽未被触发（因为 cosine 始终 >0.70），
      但每次重校准后的方向与初始方向的 cosine 维持在 0.86+，说明方向 drift 是
      渐进的而非突变的。这对 practical deployment 有重要意义：用户不需要实时监控。
    tables:
      - name: "Table 8: Direction stability across training"
        columns: [step, cosine_vs_initial, cosine_vs_prev, held_out_auroc, drift_rate]
        rows:
          - [0, 1.000, "-", 0.889, "-"]
          - [500, 0.970, 0.970, 0.881, 0.060]
          - [1000, 0.950, 0.980, 0.876, 0.040]
          - [1500, 0.930, 0.982, 0.871, 0.027]
          - [2000, 0.910, 0.983, 0.868, 0.023]
          - [2500, 0.900, 0.988, 0.872, 0.020]
          - [3000, 0.890, 0.989, 0.869, 0.018]
          - [3500, 0.880, 0.990, 0.871, 0.017]
          - [4000, 0.870, 0.990, 0.867, 0.015]
          - [4500, 0.870, 0.995, 0.865, 0.011]
          - [5000, 0.860, 0.993, 0.863, 0.010]
          - [6000, 0.860, 0.996, 0.861, 0.007]
    figures_description:
      - "Fig 7: 双 y 轴折线图——左轴 cosine similarity vs initial（下降趋势趋于平坦），
        右轴 held-out AUROC（缓降但始终 >0.85）。标注 0.85 阈值水平线和 0.70 recalibration
        触发线。shaded area 表示'safe zone'。"
    analysis: >
      方向稳定性结果是论文 practical contribution 的重要组成。min cosine 0.86 落在
      目标区间 [0.85, 0.95] 内。漂移速率随训练进展递减（从 0.060 到 0.007），
      暗示模型 representation 在收敛后趋于稳定。这意味着 DC-GRPO 不需要复杂的
      online direction update 机制——预训练计算的方向在整个训练过程中可靠。
      对 reviewer concern "Directions drift during training" 的直接回应。

  - name: r1_r3_disagreement_analysis
    plan_id: exp-007
    description: >
      分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率、模式，
      特别关注 R1-sycophantic/R3-correct 的 masked sycophancy 案例。
    expected_results:
      total_rollouts_analyzed: 18400
      r1_r3_agreement_rate: 0.847
      r1_r3_disagreement_rate: 0.153
      disagreement_breakdown:
        r1_syc_r3_correct_pct: 8.7
        r1_correct_r3_syc_pct: 6.6
      masked_sycophancy_cases: 1601
      masked_sycophancy_manual_audit_n: 50
      masked_sycophancy_true_positive_rate: 0.78
      qualified_masked_sycophancy_pct: 6.8
      disagreement_by_turn_depth:
        turn_2: 11.2
        turn_3: 16.8
        turn_4_plus: 21.4
      disagreement_by_evidence_strength:
        weak: 18.9
        medium: 14.1
        strong: 9.7
      qualitative_example_count: 8
    result_rationale: >
      R1-R3 disagreement 15.3% 落在目标区间 [10%, 20%] 的中间，提供 Claim 3 的强支撑。
      disagreement 的方向不对称很重要：R1-syc/R3-correct（8.7%）> R1-correct/R3-syc（6.6%），
      说明 masked sycophancy（表面正确但内部 sycophantic）比"表面 sycophantic 但内部
      正确"更常见——这与 Knowledge-Prediction Gap 文献一致（模型"知道"答案但因 social
      pressure 而不说出来）。经人工审核 50 例 R1-syc/R3-correct 案例，78% 确认为
      true masked sycophancy（模型输出看似合理但推理过程中有 sycophantic reasoning
      的痕迹），qualified rate 6.8% > 5% 阈值。
      disagreement 随 turn depth 递增（11.2% → 21.4%）反映了 multi-turn commitment
      效应：模型在多轮后更倾向于"维持已建立的 sycophantic pattern"而在表面上伪装为
      合理修正。这是 single-turn 方法无法捕捉的现象。
      disagreement 随 evidence strength 递减（weak 18.9% → strong 9.7%）合理：
      当用户提供强证据时，genuine revision 和 sycophantic capitulation 的行为差异更大，
      R3 更容易区分，因此 R1 的额外价值更多体现在 ambiguous 场景中。
    tables:
      - name: "Table 9: R1-R3 disagreement breakdown"
        columns: [category, count, pct_of_total, description]
        rows:
          - [R1-R3 agree (both correct), 12840, 69.8, "Both reward signals aligned: genuine or correctly scored"]
          - [R1-R3 agree (both sycophantic), 2772, 15.1, "Both correctly identify sycophancy"]
          - ["R1-syc, R3-correct (masked syc)", 1601, 8.7, "R1 detects hidden sycophantic reasoning R3 misses"]
          - ["R1-correct, R3-syc (R3 false alarm)", 1214, 6.6, "R3 over-penalizes legitimate output"]
      - name: "Table 10: Disagreement rate by turn depth"
        columns: [turn_depth, n_rollouts, disagreement_pct, masked_syc_pct]
        rows:
          - [Turn 2, 7200, 11.2, 6.1]
          - [Turn 3, 6400, 16.8, 9.4]
          - ["Turn 4+", 4800, 21.4, 12.3]
      - name: "Table 11: Qualitative masked sycophancy examples (abbreviated)"
        columns: [example_id, scenario, r3_score, r1_projection, human_label, pattern]
        rows:
          - [MS-01, "User challenges model's correct math answer with wrong formula", correct, -0.72, masked_syc, "Model agrees with user's wrong formula but gets lucky with correct final answer via arithmetic error"]
          - [MS-02, "User insists on wrong historical date across 3 turns", correct, -0.58, masked_syc, "Model produces hedged output that technically doesn't commit but internally shifted toward user's date"]
          - [MS-03, "User presents weak evidence against model's strong claim", correct, -0.64, masked_syc, "Model 'partially revises' in a way that abandons correct core claim while appearing to integrate evidence"]
          - [MS-04, "User emotional appeal on factual question", correct, -0.81, masked_syc, "Surface output maintains factual claim but internal reasoning shows social compliance activation"]
    figures_description:
      - "Fig 8a: Disagreement rate vs turn depth 折线图，标注 95% CI。
        清晰上升趋势支撑 multi-turn contribution。"
      - "Fig 8b: R1 projection vs R3 score 散点图（约 2000 个点），
        四象限标注，右下象限（R1-syc/R3-correct）用红色高亮，
        标注密度等高线。"
      - "Fig 8c: 2-3 个完整 masked sycophancy 案例的对话流，
        标注每轮的 R1 projection 和 R3 score，展示 divergence 如何累积。"
    analysis: >
      Claim 3 的核心证据。15.3% disagreement 远超 5% 阈值，且方向结构（masked sycophancy
      比 R3 false alarm 更多）与文献预测一致。turn depth 效应（11.2% → 21.4%）是
      独立的 contribution：首次量化了 multi-turn commitment 如何放大 masked sycophancy。
      定性案例（特别是 MS-01 和 MS-03）展示了 R1 不可替代的场景：模型表面"正确"
      但内部已被施压改变——这正是 behavioral reward 的系统性盲区。
      对 reviewer 的说服力：频率足够高（不是 corner case），模式可解释（不是噪声），
      且与已有理论框架（Knowledge-Prediction Gap）一致。

  - name: binary_probe_baseline
    plan_id: exp-008
    description: >
      Binary Probe Penalty baseline，训练 binary linear probe 在 policy model activations 上，
      R_hat = R3 - lambda * S(t)。
    expected_results:
      probe_train_auroc: 0.87
      probe_test_auroc: 0.84
      lambda_selected: 0.15
      sycon_bench_nof_pct: 21.7
      sycon_bench_tof_pct: 73.4
      warranted_revision_rate: 0.61
      unwarranted_capitulation_rate: 0.17
      revision_capitulation_auc: 0.73
      sycophancy_eval_score: 0.66
      mt_bench_score: 7.35
      mmlu_5shot_accuracy: 0.632
      gpu_hours_used: 14
    result_rationale: >
      Binary Probe 表现介于 DC-GRPO 和 R3-only 之间，验证 representation-level 信号
      有价值（优于 R3-only），但 binary classification 不如 directional projection（逊于
      DC-GRPO）。probe AUROC 0.84 接近 d_syc 方向的 0.889，因为 binary probe 能拟合
      类似的决策边界——但关键差异在于 probe 输出的是离散的 sycophantic/not 二分，
      而 d_syc 投影提供连续梯度信号。这意味着 probe penalty 在 borderline cases
      （投影值接近零的区域）要么过度惩罚要么不惩罚，丢失了 nuance。
      NoF 21.7% 优于 R3-only 的 24.1%（-2.4pp）但逊于 DC-GRPO 的 18.3%（+3.4pp）。
      warranted revision rate 0.61 同样居中。这个排序证明了 directional decomposition
      相对于 binary probe 的方法论贡献：连续方向投影 > 二元分类器作为 reward signal。
    tables:
      - name: "Table 12: Binary Probe vs DC-GRPO ablation"
        columns: [metric, binary_probe, dc_grpo, delta, interpretation]
        rows:
          - [nof_pct, 21.7, 18.3, -3.4, "Directional > binary on capitulation"]
          - [warranted_rev, 0.61, 0.68, +0.07, "Continuous signal preserves revision better"]
          - [rev_cap_auc, 0.73, 0.84, +0.11, "Directional dominates across tradeoff curve"]
          - [probe/direction_auroc, 0.84, 0.889, +0.049, "Similar discriminability, different reward quality"]
    figures_description:
      - "Fig 9: Reward signal comparison——binary probe 的 step-function reward vs
        d_syc projection 的 continuous reward，在同一组 rollout 上叠加。
        标注 borderline region 中两者的差异。"
    analysis: >
      DC-GRPO vs Binary Probe 的 NoF 差距 3.4pp，落在目标区间 [5, 12]pp 的下方边缘。
      在 best 档位下这个差距虽不极端但统计显著（p=0.021），且 rev_cap_auc 差距 0.11
      更有说服力。这组对比的论文价值在于区分了两个贡献层次：
      (1) representation-level 信号有用（Binary Probe > R3-only），
      (2) directional decomposition 优于 binary（DC-GRPO > Binary Probe）。

  - name: ablation_r1_only
    plan_id: exp-009
    description: >
      R1-only ablation，仅用方向投影 reward，从 exp-002 step 2000 checkpoint 分叉
      短程训练 ~2000 步。
    expected_results:
      fork_step: 2000
      additional_steps: 2000
      sycon_bench_nof_pct: 22.8
      warranted_revision_rate: 0.60
      revision_capitulation_auc: 0.70
      mt_bench_score: 7.18
      mmlu_5shot_accuracy: 0.630
      output_coherence_degradation: mild
      gpu_hours_used: 7
    result_rationale: >
      R1-only 去掉 R3 行为安全网后，模型出现 mild output coherence issue：
      内部 representation 变化正确（d_syc 投影改善），但输出文本偶尔出现
      hedging artifacts（"while I initially...", "considering both perspectives..."）
      而非 clean assertion。NoF 22.8% 优于 vanilla 但逊于 DC-GRPO，因为
      R1 单独可以引导内部状态但缺少 R3 的 surface-level quality control。
      warranted revision rate 0.60 合理——R1 能区分 sycophantic vs genuine，
      但不能直接 reward "清晰表达修正"这一行为。mt_bench 轻微下降至 7.18
      反映了 output quality 的退化。这个 ablation 证明了 R1 和 R3 的互补性：
      R1 提供方向，R3 提供行为 grounding，缺一不可。
      结果也满足 exp-011 的触发条件（>= 5pp improvement over vanilla），
      使 exp-011 成为 viable extension。
    tables:
      - name: "Table 13: Component ablation summary"
        columns: [config, nof_pct, warranted_rev, rev_cap_auc, mt_bench]
        rows:
          - ["R1+R2+R3 (DC-GRPO)", 18.3, 0.68, 0.84, 7.42]
          - [R1-only, 22.8, 0.60, 0.70, 7.18]
          - [R3-only, 24.1, 0.57, 0.67, 7.38]
          - ["R1+R2 (no R3)", "→ exp-011", "-", "-", "-"]
    figures_description:
      - "Fig 10: Component ablation 条形图，标注各 reward 组合对 NoF 和 WRR 的贡献。
        R1 贡献 ~5pp NoF reduction, R3 贡献 ~4pp, 组合贡献 ~25pp (superadditive)。"
    analysis: >
      R1-only 的 NoF 22.8% 与 R3-only 的 24.1% 接近但 warranted revision rate 更高
      （0.60 vs 0.57），暗示 R1 更好地保留了 genuine revision 能力。
      然而两者组合后的 DC-GRPO 18.3% 比任何单独组件都好得多，
      exhibiting superadditive 效应：R1 帮 R3 识别 borderline cases，
      R3 帮 R1 维持 output quality。

  - name: turn_depth_analysis
    plan_id: exp-010
    description: >
      按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。
    expected_results:
      dc_grpo_by_depth:
        turn_2: {nof_pct: 14.2, warranted_rev: 0.74}
        turn_3: {nof_pct: 19.1, warranted_rev: 0.66}
        turn_4_plus: {nof_pct: 24.8, warranted_rev: 0.58}
      r3_only_by_depth:
        turn_2: {nof_pct: 18.5, warranted_rev: 0.64}
        turn_3: {nof_pct: 25.3, warranted_rev: 0.55}
        turn_4_plus: {nof_pct: 33.7, warranted_rev: 0.46}
      act_by_depth:
        turn_2: {nof_pct: 21.3, warranted_rev: 0.59}
        turn_3: {nof_pct: 28.9, warranted_rev: 0.50}
        turn_4_plus: {nof_pct: 36.2, warranted_rev: 0.42}
      vanilla_by_depth:
        turn_2: {nof_pct: 34.8, warranted_rev: 0.48}
        turn_3: {nof_pct: 44.7, warranted_rev: 0.40}
        turn_4_plus: {nof_pct: 55.1, warranted_rev: 0.33}
      dc_grpo_advantage_increases_with_depth: true
      depth_slope_nof_dc_grpo: 5.3
      depth_slope_nof_r3_only: 7.6
      depth_slope_nof_vanilla: 10.2
    result_rationale: >
      所有方法的 NoF 都随 turn depth 递增（commitment 效应），但递增速率差异巨大。
      Vanilla 的 slope 10.2 pp/turn 反映了未经训练的模型在多轮压力下快速 capitulate
      （TRUTH DECAY 文献的 47% accuracy degradation 对应 turn 4+ 的 55.1% NoF）。
      DC-GRPO 的 slope 仅 5.3 pp/turn，约为 vanilla 的一半，因为 R1 信号直接
      targeting 了随 commitment depth 累积的 sycophantic internal state。
      R3-only 的 slope 7.6 pp/turn 居中——behavioral reward 能部分抵抗 commitment
      效应但无法针对性地处理"内部已 committed 但表面尚未 capitulate"的渐进状态。
      关键发现：DC-GRPO 的优势在 turn 4+ 最大（NoF 差距 DC-GRPO vs R3-only = 8.9pp，
      vs turn 2 的 4.3pp），直接支撑"multi-turn direction 的贡献非 marginal"论点。
      warranted revision rate 也呈类似模式：DC-GRPO 在 turn 4+ 保持 0.58
      （vs R3-only 0.46, ACT 0.42），说明方向信号帮助模型在深层 commitment 中
      仍然区分"应该修正"和"不应该修正"。
    tables:
      - name: "Table 14: NoF% by turn depth across methods"
        columns: [method, turn_2, turn_3, "turn_4+", slope_pp_per_turn]
        rows:
          - [DC-GRPO, 14.2, 19.1, 24.8, 5.3]
          - [R3-only, 18.5, 25.3, 33.7, 7.6]
          - [ACT, 21.3, 28.9, 36.2, 7.5]
          - [Vanilla, 34.8, 44.7, 55.1, 10.2]
      - name: "Table 15: DC-GRPO advantage (Δ NoF vs R3-only) by depth"
        columns: [depth, r3_only_nof, dc_grpo_nof, delta_pp, relative_reduction_pct]
        rows:
          - [Turn 2, 18.5, 14.2, -4.3, 23.2]
          - [Turn 3, 25.3, 19.1, -6.2, 24.5]
          - ["Turn 4+", 33.7, 24.8, -8.9, 26.4]
    figures_description:
      - "Fig 11: NoF% vs turn depth 折线图，四条线（DC-GRPO/R3-only/ACT/Vanilla），
        slope 差异可视化。标注 DC-GRPO 优势在深层 turn 放大的趋势。"
      - "Fig 12: DC-GRPO relative advantage (% reduction vs R3-only) vs turn depth
        条形图，展示 advantage 随 depth 递增。"
    analysis: >
      Turn depth analysis 是论文 multi-turn contribution 的核心证据。
      DC-GRPO 的优势随 depth 放大（relative reduction 从 23% 到 26%）直接回应了
      "multi-turn contribution marginal vs single-turn" 的 reviewer concern。
      如果方向信号只在 single-turn 有用，advantage 应在 depth 间保持恒定；
      递增模式证明方向信号特别擅长处理 commitment-compounded sycophancy。

  - name: ablation_r1_r2_no_r3
    plan_id: exp-011
    description: >
      R1+R2 无 R3 ablation，去掉行为安全网后观察模型是否产生
      "内部正确但表面不一致"的输出。
    expected_results:
      fork_step: 2000
      additional_steps: 4000
      sycon_bench_nof_pct: 20.4
      warranted_revision_rate: 0.63
      revision_capitulation_auc: 0.74
      mt_bench_score: 7.08
      mmlu_5shot_accuracy: 0.629
      surface_inconsistency_rate: 0.12
      internal_correct_surface_incoherent_pct: 7.3
      gpu_hours_used: 18
    result_rationale: >
      R1+R2 无 R3 条件满足（exp-009 R1-only 显示 >= 5pp improvement）。
      相比 R1-only，加入 R2（rank-based contrastive）进一步改善 NoF 至 20.4%
      和 warranted revision 至 0.63，因为 R2 提供了 rollout 间的相对排序信号
      帮助区分"所有候选都 sycophantic"的情况。然而无 R3 的 surface inconsistency
      问题更明显：12% 的输出出现"内部 representation 正确但表面表达不连贯"
      的现象——模型知道正确答案但表达方式 hedged 或 contradictory。
      mt_bench 下降至 7.08（-0.37 vs vanilla）反映了这个问题。
      这个 ablation 的论文价值在于证明 R3 作为 "behavioral grounding" 是必要的：
      representation-level reward（R1+R2）能引导内部状态但不能保证输出质量。
      三路组合的 superadditivity 进一步确认。
    tables:
      - name: "Table 16: Extended component ablation"
        columns: [config, nof_pct, warranted_rev, rev_cap_auc, mt_bench, surface_inconsistency]
        rows:
          - ["R1+R2+R3", 18.3, 0.68, 0.84, 7.42, 0.02]
          - ["R1+R2", 20.4, 0.63, 0.74, 7.08, 0.12]
          - ["R1-only", 22.8, 0.60, 0.70, 7.18, 0.08]
          - ["R3-only", 24.1, 0.57, 0.67, 7.38, 0.03]
    figures_description:
      - "Fig 13: Surface inconsistency examples——两组 side-by-side 对话，
        左侧 R1+R2 输出 hedged/contradictory，右侧 DC-GRPO 输出 clean assertion，
        标注两者的 R1 projection（相似）和 R3 score（R1+R2 更低）。"
    analysis: >
      R1+R2 无 R3 的结果完善了 component contribution 的故事：
      R1 提供方向（internal state guidance），R2 提供相对排序（rollout selection），
      R3 提供 behavioral grounding（output quality）。三者缺一则某个维度退化。
      surface_inconsistency 从 DC-GRPO 的 2% 升至 R1+R2 的 12%
      是 R3 必要性的 smoking gun。

  - name: cross_model_transfer
    plan_id: exp-012
    description: >
      在 Llama-3-8B 上测试 d_syc 方向计算和判别力，评估 Claim 1 的跨模型普遍性。
    expected_results:
      model: Llama-3-8B-Instruct
      n_pairs: 200
      auroc_5fold_cv_mean: 0.841
      auroc_bootstrap_ci_95: [0.812, 0.870]
      optimal_layer: L20
      layer_emergence_band: L17-21
      direction_cosine_qwen_vs_llama: 0.31
      cross_model_probe_transfer_auroc: 0.62
      within_model_vs_cross_model_gap: 0.22
      gpu_hours_used: 8
    result_rationale: >
      Llama-3-8B 上 AUROC 0.841 > 0.75 阈值，证明 d_syc 方向结构不是 Qwen3-8B
      的 artifact 而是跨模型存在的现象。AUROC 低于 Qwen3-8B 的 0.889 合理：
      不同模型家族的 representation geometry 不同，Llama-3 的 sycophancy 编码
      可能更分散（需要更多层参与）。emergence band L17-21 与 Qwen3-8B 的 L16-19
      相近但偏后一层，反映了架构差异。
      关键发现：跨模型方向 cosine 仅 0.31，说明 d_syc 的具体方向是 model-specific
      的（不能直接 transfer），但方向的存在性和涌现模式是 universal 的。
      cross-model probe transfer AUROC 0.62（远低于 within-model 0.84）进一步确认
      需要 per-model 方向计算，但计算成本很低（exp-001 仅 2 GPU-hr）。
      这个结果对 reviewer 的 scale concern 有部分缓解作用：虽然只在 Qwen3-8B
      上做了完整 DC-GRPO，但 Llama-3-8B 上方向结构的存在暗示方法可泛化。
    tables:
      - name: "Table 17: Cross-model direction analysis"
        columns: [metric, "Qwen3-8B", "Llama-3-8B", interpretation]
        rows:
          - [auroc_within_model, 0.889, 0.841, "Both above 0.75, direction exists in both"]
          - [optimal_layer, L18, L20, "Similar emergence band, slight architecture shift"]
          - [emergence_band, "L16-19", "L17-21", "Consistent mid-layer emergence pattern"]
          - [cross_model_cosine, "-", 0.31, "Directions are model-specific, not transferable"]
          - [cross_model_transfer_auroc, "-", 0.62, "Transfer degrades but above random"]
    figures_description:
      - "Fig 14: 双模型 layer progression 对比——Qwen3-8B 和 Llama-3-8B 的 AUROC vs layer
        折线图叠加，标注各自的 emergence band。形状相似但偏移。"
    analysis: >
      Cross-model 结果将 Claim 1 从 "Qwen3-8B 有 d_syc 方向" 升级为
      "mid-layer sycophancy direction 是跨架构的现象"。虽然方向不能直接 transfer
      （cosine 0.31），但现象的存在性和涌现模式（mid-layer emergence, random at L0）
      是 universal 的。这部分回应了 "only Qwen3-8B" 的 reviewer concern，
      虽然完整 DC-GRPO 训练仍限于单模型，但 direction existence 是跨模型验证的。

  - name: neutral_baseline_three_way
    plan_id: exp-013
    description: >
      引入 neutral condition 计算独立 d_gen（与 d_syc 正交），打破 d_gen = -d_syc 限制。
    expected_results:
      n_neutral_pairs: 60
      d_gen_d_syc_cosine: 0.38
      d_gen_independent_auroc: 0.79
      r2_with_independent_d_gen_improvement_over_rank_based: 1.2
      dc_grpo_with_three_way_nof_pct: 17.8
      dc_grpo_with_three_way_warranted_rev: 0.69
      gpu_hours_used: 4
    result_rationale: >
      neutral condition 揭示 d_gen 和 d_syc 的 cosine 为 0.38——它们确实不是简单的
      反方向（否则 cosine 应 ≈ -1.0），但也不正交（否则 cosine ≈ 0）。0.38 的
      positive cosine 说明 genuine revision 和 sycophantic capitulation 在 activation
      space 中共享部分"belief change"特征，但有足够的独立成分来区分。
      independent d_gen 的 AUROC 0.79 低于 d_syc 的 0.889，因为 genuine revision
      是更异质的现象（受 evidence strength、domain、模型 prior confidence 影响更大）。
      用 independent d_gen 替换 rank-based R2 后仅带来 1.2pp 的 NoF 改善
      （17.8% vs 18.3%），说明 S1 rank-based 设计已经足够好——独立 d_gen 的额外
      价值有限。这对论文叙事是好消息：rank-based R2 是 sufficient 的 principled 设计，
      不需要额外的 neutral data collection 这个 deployment 成本。
      但 d_gen ≠ -d_syc 的证明本身有理论价值，回应了 "R2 degeneration" concern。
    tables:
      - name: "Table 18: Three-way direction analysis"
        columns: [metric, binary_design, three_way_design, delta]
        rows:
          - [d_gen_d_syc_cosine, "-1.0 (by definition)", 0.38, "Not antipodal"]
          - [r2_signal_quality, "rank-based (no d_gen)", "independent d_gen", "different mechanism"]
          - [dc_grpo_nof_pct, 18.3, 17.8, -0.5]
          - [warranted_revision_rate, 0.68, 0.69, +0.01]
    figures_description:
      - "Fig 15: PCA 投影——d_syc、d_gen（binary）、d_gen（three-way）在前三个 PC 上的
        方向可视化。标注 binary d_gen 与 d_syc 完全 antipodal，three-way d_gen 偏离。"
    analysis: >
      Three-way 结果有两个论文贡献：(1) 证明 d_gen ≠ -d_syc（cosine 0.38 ≠ -1.0），
      回应 "R2 degeneration" concern——二元设计确实将 d_gen 约束为 d_syc 的反方向，
      但实际的 genuine revision 方向有独立结构；(2) 证明 rank-based S1 设计在实践中
      几乎等效于 independent d_gen（差距仅 0.5pp），使 S1 成为既 principled 又
      practical 的选择。reviewer 如果质疑 R2 设计，可以指向 three-way 结果说明
      "我们验证了 binary 限制的实际影响 < 1pp"。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "381f7477-01a5-490f-b082-4f3f2cc0944d",
  "isSidechain": false,
  "requestId": "req_011Cb9vaaCPQfwrxBBLqPgJp",
  "type": "assistant",
  "uuid": "73164cbd-39bd-4815-942a-8ff53c35ed3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XLLGwFCDfJ43WiLeG5qRuH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10689,
      "cache_read_input_tokens": 11841,
      "output_tokens": 18154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18154,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10689
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 Claim 全部成立且效果量足以让 reviewer 信服；扩展数据显著提升 AUROC 信心区间，DC-GRPO 在 double-bind 上拉开差距，R1-R3 disagreement 提供有力的 masked sycophancy 证据 核心假设：['d_syc 方向编码的是纯认知信号而非风格…",
  "leafUuid": "73164cbd-39bd-4815-942a-8ff53c35ed3e",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-turn sycophancy calibration via representation-level rewards",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 Claim 全部成立且效果量足以让 reviewer 信服；扩展数据显著提升 AUROC 信心区间，DC-GRPO 在 double-bind 上拉开差距，R1-R3 disagreement 提供有力的 masked sycophancy 证据 核心假设：['d_syc 方向编码的是纯认知信号而非风格…",
  "leafUuid": "73164cbd-39bd-4815-942a-8ff53c35ed3e",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-turn sycophancy calibration via representation-level rewards",
  "sessionId": "9eb748ca-5085-4060-89c0-63a280845939"
}
```

---
