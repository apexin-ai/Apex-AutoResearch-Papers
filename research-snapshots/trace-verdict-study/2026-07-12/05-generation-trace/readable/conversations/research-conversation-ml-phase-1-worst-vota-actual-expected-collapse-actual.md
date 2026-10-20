# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：VOTA 效果几乎完全来自 actual==expected 字符串比对；collapse 机制解释不通；泛化失败 核心假设：['去除 actual/

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/5a70e784-9e93-4588-91e0-070c6c762ca2.jsonl`
- **Structured JSON:** [`25e93e84d6e6240b2512.json`](../../sessions/25/25e93e84d6e6240b2512.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T01:40:28.713Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T01:40:28.713Z",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：VOTA 效果几乎完全来自 actual==expected 字符串比对；collapse 机制解释不通；泛化失败\n核心假设：['去除 actual/expected 后 acc 降至 73-78%（≈no_trace baseline），证明 VOTA 的 lift 本质是将 answer 暴露给模型', 'full_trace + label-only loss 仍 collapse（acc <50%），gradient dilution 假说不充分，可能是 trace content 本身有害', '组件 ablation 确认：只有 actual/expected 有贡献，exception summary 和 loop compression 无显著 lift', 'DeepSeek-Coder 上 VOTA lift <8pp 或 pattern 不一致', '第二 verdict task 上 VOTA 无显著 lift']\n关键指标范围：{'vota_no_actexp_acc': [0.73, 0.78], 'vota_no_actexp_lift_over_notrace': [-0.02, 0.03], 'fulltrace_labelonly_acc': [0.28, 0.5], 'component_ablation_min_individual_lift': [-0.02, 0.01], 'deepseek_vota_lift': [0.0, 0.08], 'second_task_vota_lift': [0.0, 0.05], 'seed_variance_pp': [2.0, 5.0]}\n叙事方向：完全 reframe。放弃 \"trace teaches reasoning\" 叙事。新 angle：\"What Makes Verdict Prediction Trivial? A Trace Ablation Study\" —— 核心发现变成一个 negative + diagnostic result：(1) verdict tasks 本质上只需要 assertion-point comparison data，不需要任何 reasoning trace；(2) full execution trace 不仅无用而且有害，且 label-only loss 无法修复，说明问题不只是 gradient dilution 而是 trace content 引入的 distributional shift；(3) VOTA 的成功恰好证明了 verdict tasks 的信息需求 极度 sparse。Contribution 重新定位为 \"systematic negative result + task complexity analysis\"： 我们提供了第一个 evidence 证明 trace SFT 对 classification tasks 的效果完全取决于是否包含 task-critical data points，而非 reasoning chain。仍冲 EMNLP（negative/analytical results 有 venue precedent），但 Findings 更现实。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: trace-verdict-study\nfocus: Key risk: VOTA 95.63% may be trivial actual==expected string comparison. Ablation removing actual/expected is the make-or-break experiment. Also: full_trace collapse mechanism and whether label-only loss can fix it. Paper needs to work regardless of ablation outcome (contingency framing prepared).\n\n## paper_framing.md\n\n# Paper Framing — trace-verdict-study\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Insight\n\nTrace SFT effectiveness depends critically on **trace granularity matching task output entropy**: verdict tasks (1-bit output) benefit massively from compact, decision-relevant trace abstractions (VOTA: +20.5pp), while full execution traces cause model collapse (-46.6pp) due to gradient dilution. The \"right\" trace is not \"more trace\" — it's the minimal information sufficient to determine the verdict.\n\n## Core Claims (≤3)\n\n1. **VOTA dramatically improves verdict prediction**: Verdict-Optimized Trace Abstraction (assertion-point state snapshots) provides +20.5pp accuracy improvement over no-trace baseline for test outcome prediction, with 95% CI [+17.7, +23.4] excluding zero.\n\n2. **Full execution traces hurt verdict tasks**: Dense, uncompressed execution traces cause model collapse (28.49% accuracy, 100% predicting \"fail\") due to classification gradient dilution by trace token prediction — a task-representation mismatch that worsens with trace length.\n\n3. **Information granularity, not information presence, determines trace SFT value**: Through systematic ablation of VOTA components (actual/expected values, exception summaries, loop compression), we identify which trace elements carry verdict-relevant signal vs. noise, providing design principles for task-optimized trace representations.\n\n## Story Spine\n\n- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited benefit. No prior work has tested trace SFT on code behavior verdict tasks (binary pass/fail), nor designed trace representations specifically for classification.\n\n- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding limited benefit. TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification, but nobody has tested decoder SFT. All existing trace formats are designed for full execution simulation, not classification.\n\n- **Our framing**: We ask \"does trace granularity need to match task complexity?\" and demonstrate that verdict tasks — with O(1) output entropy — benefit from a fundamentally different trace design principle than generation tasks. VOTA captures only decision-relevant execution states (assertion snapshots, exception summaries) rather than full simulation.\n\n- **Headline result template**: \"On test verdict prediction, VOTA-SFT achieves 95.6% accuracy (+20.5pp over no-trace baseline), while full execution trace SFT collapses to 28.5% — demonstrating that trace design granularity, not presence, determines SFT effectiveness for classification.\"\n\n## Venue Fit Risks\n\n- EMNLP主会 vs SE: 论文核心贡献是对 trace SFT 的 task-dependent 效果的系统性实证发现 + 新 trace representation，属于 NLP for code 方向。投 EMNLP Code track 合适。\n- 单任务风险: 目前只在 test verdict prediction 一个任务上验证。需要至少加一个 verdict task（patch correctness 或 bug detection）才够 EMNLP Main。Findings 可能只需当前结果 + ablation。\n- Leakage concern: 如果 ablation 证明 VOTA 效果主要来自 actual==expected 字符串比对，claim 需要调整为 \"verdict tasks 需要的不是 trace reasoning 而是 decision-relevant data points\"——仍然 publishable 但 framing 不同。\n\n## Contingency Framing (based on ablation outcome)\n\n**If ablation shows genuine behavioral understanding** (去 actual/expected 后仍有显著提升):\n→ Full positive framing: \"VOTA teaches execution-grounded verdict reasoning\"\n\n**If ablation shows primarily string matching** (去 actual/expected 后 accuracy 大幅下降):\n→ Adjusted framing: \"For verdict tasks, the critical trace element is the assertion-point state — not behavioral reasoning but targeted state comparison. This is still a novel finding because: (a) no one knew this before testing, (b) it explains WHY full traces fail (too much irrelevant state), (c) it provides practical design principles.\"\n\n## Key Open Questions (Post-MVP)\n\n1. actual/expected ablation 结果如何？→ 决定 Claim 1 的强度\n2. full_trace + label-only loss 能否修复 collapse？→ 加强 Claim 2 的解释\n3. 能否在第二个 verdict task 上复现？→ 决定 generalization claim\n4. 需要多模型验证吗？→ 时间允许就加 DeepSeek-Coder\n\n## Anticipated Reviewer Concerns\n\n| Concern | Planned Response |\n|---------|-----------------|\n| \"VOTA 95.63% 可能是 trivial actual==expected 比对\" | ablation 实验直接回应（P0 优先级） |\n| \"只在一个任务/数据集上测试\" | 加 patch correctness task 或 CRUXEval verdict variant |\n| \"只用一个模型\" | 加 DeepSeek-Coder-6.7B 复现（DCSH 同模型） |\n| \"full_trace collapse 可能是实现 bug\" | label-only loss ablation 验证是 gradient dilution 而非 bug |\n| \"VOTA 只是 feature engineering 不是方法创新\" | 定位为 empirical contribution: 系统性发现 + design principles + task-spectrum analysis |\n| \"与 DCSH 的关系不清\" | 明确：我们 complement DCSH（他们做 generation，我们做 classification） |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Ablation: 去除 VOTA 中 actual/expected 值对，只保留 assertion structure + exception\n    info。验证 VOTA 效果是 genuine behavioral understanding 还是 trivial string comparison。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: null\n  notes: 如果去 actual/expected 后 acc 仍 >80%，证明非 trivial；如果降到 ~75%(=no_trace)，则是字符串比对。决定\n    Claim 1 强度和论文 framing。\n  status: planned\n- id: plan_002\n  claim: 2\n  description: 'Ablation: full_trace + label-only loss (只对分类 token 计算 loss，mask trace\n    tokens)。验证 collapse 根因是 gradient dilution 而非数据/代码 bug。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: null\n  notes: 如果 label-only loss 修复 collapse (acc >70%)，确认 gradient dilution 假说。如果仍 collapse，可能是\n    trace noise/length 本身就有害。\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'VOTA component ablation: 分别测试 (a) 只有 actual/expected, (b) 只有 exception\n    summary, (c) 只有 loop compression, (d) 全量 VOTA。量化每个组件的贡献。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  registry_id: null\n  notes: 4 个 sub-conditions，每个 ~2h 训练。plan_001 先跑因为它决定 actual/expected 是否是唯一贡献者。\n  status: planned\n- id: plan_004\n  claim: 1\n  description: '第二模型验证: DeepSeek-Coder-6.7B 上复现 VOTA vs no_trace vs full_trace 三条件，与\n    DCSH 同模型直接对比。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: null\n  notes: DCSH 用的 DeepSeek-Coder，同模型对比最有说服力。只跑 3 条件（VOTA/no_trace/full_trace），不跑全 ablation。\n  status: planned\n- id: plan_005\n  claim: 1\n  description: '第二任务验证: 在 bug detection (DebugBench subset) 或 patch correctness (Defects4J\n    subset) 上测试 VOTA。验证 verdict task 泛化性。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: null\n  notes: 选一个能快速构建 VOTA 格式数据的 verdict task。DebugBench (Python) 可能比 Defects4J (Java)\n    快。\n  status: planned\n- id: plan_006\n  claim: 2\n  description: 'Trace length ablation: 测试不同截断长度 (256/512/1024/2048 tokens) 对 full_trace\n    准确率的影响，绘制 accuracy vs trace length 曲线。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  registry_id: null\n  notes: 验证 'more trace = worse for classification' 的单调关系。如果短 trace 也 collapse，问题在\n    trace content 而非 length。\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Calibration analysis: ECE + reliability diagrams 对比 VOTA/no_trace/full_trace\n    的 calibration 质量。验证 trace SFT 对 verdict task 改善 calibration 的假说。'\n  priority: P2\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: null\n  notes: 纯 eval，不需要额外训练。用已有 checkpoint 的 logits 计算。\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Seed robustness: 3 random seeds (42/123/456) 验证 VOTA 结果稳定性。McNemar\n    test + bootstrap CI。'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_001\n  registry_id: null\n  notes: 每 seed ~2h × 3。不同 seed 间 accuracy 差异应 <2pp。\n  status: planned\n- id: plan_mvp_vota\n  claim: 1\n  description: 'MVP: VOTA trace SFT for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: vota_seed42_v4\n  notes: 完成。95.63% accuracy, +20.5pp over baseline.\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9916\n    majority_baseline: 0.7151\n    lift: 0.2765\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.988\n    pass_f1: 0.994\n    fail_precision: 0.971\n    fail_recall: 1\n    fail_f1: 0.985\n    accuracy_ci_lower: 0.9857\n    accuracy_ci_upper: 0.9966\n    train_loss: 0.046\n    eval_loss: 0.0842\n- id: plan_mvp_notrace\n  claim: 1\n  description: 'MVP: No-trace baseline for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: no_trace_seed42_v4\n  notes: 完成。75.13% accuracy (majority baseline 71.51%).\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    train_loss: 0.18\n    eval_loss: 0.6454\n    eval_mean_token_accuracy: 0.8897\n- id: plan_mvp_fulltrace\n  claim: 2\n  description: 'MVP: Full execution trace SFT for test verdict prediction'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: full_trace_seed42_v2\n  notes: 完成。28.49% accuracy, model collapse (100% predict fail).\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.4311\n    n: 1190\n    pass_precision: 0.923\n    pass_recall: 0.085\n    pass_f1: 0.155\n    fail_precision: 0.445\n    fail_recall: 0.785\n    fail_f1: 0.568\n    train_loss: 0.0373\n    eval_loss: 0.082\n    eval_mean_token_accuracy: 0.984\n\n\n## registry (completed experiments)\n\n- exp_id: no_trace_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed42\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: no_trace_seed42_v2\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: vota_seed42_v2\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: no_trace_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.18\n    eval_loss: 0.645\n    eval_mean_token_accuracy: 0.89\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n- exp_id: vota_seed42_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.046\n    eval_loss: 0.085\n    eval_mean_token_accuracy: 0.983\n    accuracy: 0.992\n    majority_baseline: 0.7151\n    lift: 0.276\n    pass_precision: 0.99\n    pass_recall: 0.99\n    pass_f1: 0.99\n    fail_precision: 0.99\n    fail_recall: 0.99\n    fail_f1: 0.99\n- exp_id: full_trace_seed42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    train_loss: 0.037\n    eval_loss: 0.084\n    eval_mean_token_accuracy: 0.984\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.431\n    pass_precision: 0.88\n    pass_recall: 0.08\n    pass_f1: 0.16\n    fail_precision: 0.31\n    fail_recall: 0.97\n    fail_f1: 0.57\n- exp_id: no_trace_seed42_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.7513\n    majority_baseline: 0.7151\n    lift: 0.0361\n    pass_precision: 0.8776\n    pass_recall: 0.7579\n    pass_f1: 0.8134\n    fail_precision: 0.5473\n    fail_recall: 0.7345\n    fail_f1: 0.6272\n    train_loss: 0.18\n    eval_loss: 0.6454\n    eval_mean_token_accuracy: 0.8897\n- exp_id: vota_seed42_v4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.9916\n    majority_baseline: 0.7151\n    lift: 0.2765\n    n: 1190\n    pass_precision: 1\n    pass_recall: 0.988\n    pass_f1: 0.994\n    fail_precision: 0.971\n    fail_recall: 1\n    fail_f1: 0.985\n    accuracy_ci_lower: 0.9857\n    accuracy_ci_upper: 0.9966\n    train_loss: 0.046\n    eval_loss: 0.0842\n- exp_id: full_trace_seed42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.284\n    majority_baseline: 0.7151\n    lift: -0.4311\n    n: 1190\n    pass_precision: 0.923\n    pass_recall: 0.085\n    pass_f1: 0.155\n    fail_precision: 0.445\n    fail_recall: 0.785\n    fail_f1: 0.568\n    train_loss: 0.0373\n    eval_loss: 0.082\n    eval_mean_token_accuracy: 0.984\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T01:40:28.718Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T01:40:28.718Z",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T01:40:28.741Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：VOTA 效果几乎完全来自 actual==expected 字符串比对；collapse 机制解释不通；泛化失败
核心假设：['去除 actual/expected 后 acc 降至 73-78%（≈no_trace baseline），证明 VOTA 的 lift 本质是将 answer 暴露给模型', 'full_trace + label-only loss 仍 collapse（acc <50%），gradient dilution 假说不充分，可能是 trace content 本身有害', '组件 ablation 确认：只有 actual/expected 有贡献，exception summary 和 loop compression 无显著 lift', 'DeepSeek-Coder 上 VOTA lift <8pp 或 pattern 不一致', '第二 verdict task 上 VOTA 无显著 lift']
关键指标范围：{'vota_no_actexp_acc': [0.73, 0.78], 'vota_no_actexp_lift_over_notrace': [-0.02, 0.03], 'fulltrace_labelonly_acc': [0.28, 0.5], 'component_ablation_min_individual_lift': [-0.02, 0.01], 'deepseek_vota_lift': [0.0, 0.08], 'second_task_vota_lift': [0.0, 0.05], 'seed_variance_pp': [2.0, 5.0]}
叙事方向：完全 reframe。放弃 "trace teaches reasoning" 叙事。新 angle："What Makes Verdict Prediction Trivial? A Trace Ablation Study" —— 核心发现变成一个 negative + diagnostic result：(1) verdict tasks 本质上只需要 assertion-point comparison data，不需要任何 reasoning trace；(2) full execution trace 不仅无用而且有害，且 label-only loss 无法修复，说明问题不只是 gradient dilution 而是 trace content 引入的 distributional shift；(3) VOTA 的成功恰好证明了 verdict tasks 的信息需求 极度 sparse。Contribution 重新定位为 "systematic negative result + task complexity analysis"： 我们提供了第一个 evidence 证明 trace SFT 对 classification tasks 的效果完全取决于是否包含 task-critical data points，而非 reasoning chain。仍冲 EMNLP（negative/analytical results 有 venue precedent），但 Findings 更现实。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: trace-verdict-study
focus: Key risk: VOTA 95.63% may be trivial actual==expected string comparison. Ablation removing actual/expected is the make-or-break experiment. Also: full_trace collapse mechanism and whether label-only loss can fix it. Paper needs to work regardless of ablation outcome (contingency framing prepared).

## paper_framing.md

# Paper Framing — trace-verdict-study

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026 (10 days from today)

## Core Insight

Trace SFT effectiveness depends critically on **trace granularity matching task output entropy**: verdict tasks (1-bit output) benefit massively from compact, decision-relevant trace abstractions (VOTA: +20.5pp), while full execution traces cause model collapse (-46.6pp) due to gradient dilution. The "right" trace is not "more trace" — it's the minimal information sufficient to determine the verdict.

## Core Claims (≤3)

1. **VOTA dramatically improves verdict prediction**: Verdict-Optimized Trace Abstraction (assertion-point state snapshots) provides +20.5pp accuracy improvement over no-trace baseline for test outcome prediction, with 95% CI [+17.7, +23.4] excluding zero.

2. **Full execution traces hurt verdict tasks**: Dense, uncompressed execution traces cause model collapse (28.49% accuracy, 100% predicting "fail") due to classification gradient dilution by trace token prediction — a task-representation mismatch that worsens with trace length.

3. **Information granularity, not information presence, determines trace SFT value**: Through systematic ablation of VOTA components (actual/expected values, exception summaries, loop compression), we identify which trace elements carry verdict-relevant signal vs. noise, providing design principles for task-optimized trace representations.

## Story Spine

- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited benefit. No prior work has tested trace SFT on code behavior verdict tasks (binary pass/fail), nor designed trace representations specifically for classification.

- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding limited benefit. TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification, but nobody has tested decoder SFT. All existing trace formats are designed for full execution simulation, not classification.

- **Our framing**: We ask "does trace granularity need to match task complexity?" and demonstrate that verdict tasks — with O(1) output entropy — benefit from a fundamentally different trace design principle than generation tasks. VOTA captures only decision-relevant execution states (assertion snapshots, exception summaries) rather than full simulation.

- **Headline result template**: "On test verdict prediction, VOTA-SFT achieves 95.6% accuracy (+20.5pp over no-trace baseline), while full execution trace SFT collapses to 28.5% — demonstrating that trace design granularity, not presence, determines SFT effectiveness for classification."

## Venue Fit Risks

- EMNLP主会 vs SE: 论文核心贡献是对 trace SFT 的 task-dependent 效果的系统性实证发现 + 新 trace representation，属于 NLP for code 方向。投 EMNLP Code track 合适。
- 单任务风险: 目前只在 test verdict prediction 一个任务上验证。需要至少加一个 verdict task（patch correctness 或 bug detection）才够 EMNLP Main。Findings 可能只需当前结果 + ablation。
- Leakage concern: 如果 ablation 证明 VOTA 效果主要来自 actual==expected 字符串比对，claim 需要调整为 "verdict tasks 需要的不是 trace reasoning 而是 decision-relevant data points"——仍然 publishable 但 framing 不同。

## Contingency Framing (based on ablation outcome)

**If ablation shows genuine behavioral understanding** (去 actual/expected 后仍有显著提升):
→ Full positive framing: "VOTA teaches execution-grounded verdict reasoning"

**If ablation shows primarily string matching** (去 actual/expected 后 accuracy 大幅下降):
→ Adjusted framing: "For verdict tasks, the critical trace element is the assertion-point state — not behavioral reasoning but targeted state comparison. This is still a novel finding because: (a) no one knew this before testing, (b) it explains WHY full traces fail (too much irrelevant state), (c) it provides practical design principles."

## Key Open Questions (Post-MVP)

1. actual/expected ablation 结果如何？→ 决定 Claim 1 的强度
2. full_trace + label-only loss 能否修复 collapse？→ 加强 Claim 2 的解释
3. 能否在第二个 verdict task 上复现？→ 决定 generalization claim
4. 需要多模型验证吗？→ 时间允许就加 DeepSeek-Coder

## Anticipated Reviewer Concerns

| Concern | Planned Response |
|---------|-----------------|
| "VOTA 95.63% 可能是 trivial actual==expected 比对" | ablation 实验直接回应（P0 优先级） |
| "只在一个任务/数据集上测试" | 加 patch correctness task 或 CRUXEval verdict variant |
| "只用一个模型" | 加 DeepSeek-Coder-6.7B 复现（DCSH 同模型） |
| "full_trace collapse 可能是实现 bug" | label-only loss ablation 验证是 gradient dilution 而非 bug |
| "VOTA 只是 feature engineering 不是方法创新" | 定位为 empirical contribution: 系统性发现 + design principles + task-spectrum analysis |
| "与 DCSH 的关系不清" | 明确：我们 complement DCSH（他们做 generation，我们做 classification） |


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: 'Ablation: 去除 VOTA 中 actual/expected 值对，只保留 assertion structure + exception
    info。验证 VOTA 效果是 genuine behavioral understanding 还是 trivial string comparison。'
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: null
  notes: 如果去 actual/expected 后 acc 仍 >80%，证明非 trivial；如果降到 ~75%(=no_trace)，则是字符串比对。决定
    Claim 1 强度和论文 framing。
  status: planned
- id: plan_002
  claim: 2
  description: 'Ablation: full_trace + label-only loss (只对分类 token 计算 loss，mask trace
    tokens)。验证 collapse 根因是 gradient dilution 而非数据/代码 bug。'
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: null
  notes: 如果 label-only loss 修复 collapse (acc >70%)，确认 gradient dilution 假说。如果仍 collapse，可能是
    trace noise/length 本身就有害。
  status: planned
- id: plan_003
  claim: 3
  description: 'VOTA component ablation: 分别测试 (a) 只有 actual/expected, (b) 只有 exception
    summary, (c) 只有 loop compression, (d) 全量 VOTA。量化每个组件的贡献。'
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_001
  registry_id: null
  notes: 4 个 sub-conditions，每个 ~2h 训练。plan_001 先跑因为它决定 actual/expected 是否是唯一贡献者。
  status: planned
- id: plan_004
  claim: 1
  description: '第二模型验证: DeepSeek-Coder-6.7B 上复现 VOTA vs no_trace vs full_trace 三条件，与
    DCSH 同模型直接对比。'
  priority: P1
  gpu_budget_hours: 6
  deps:
  - plan_001
  registry_id: null
  notes: DCSH 用的 DeepSeek-Coder，同模型对比最有说服力。只跑 3 条件（VOTA/no_trace/full_trace），不跑全 ablation。
  status: planned
- id: plan_005
  claim: 1
  description: '第二任务验证: 在 bug detection (DebugBench subset) 或 patch correctness (Defects4J
    subset) 上测试 VOTA。验证 verdict task 泛化性。'
  priority: P1
  gpu_budget_hours: 6
  deps:
  - plan_001
  registry_id: null
  notes: 选一个能快速构建 VOTA 格式数据的 verdict task。DebugBench (Python) 可能比 Defects4J (Java)
    快。
  status: planned
- id: plan_006
  claim: 2
  description: 'Trace length ablation: 测试不同截断长度 (256/512/1024/2048 tokens) 对 full_trace
    准确率的影响，绘制 accuracy vs trace length 曲线。'
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan_002
  registry_id: null
  notes: 验证 'more trace = worse for classification' 的单调关系。如果短 trace 也 collapse，问题在
    trace content 而非 length。
  status: planned
- id: plan_007
  claim: 3
  description: 'Calibration analysis: ECE + reliability diagrams 对比 VOTA/no_trace/full_trace
    的 calibration 质量。验证 trace SFT 对 verdict task 改善 calibration 的假说。'
  priority: P2
  gpu_budget_hours: 1
  deps: []
  registry_id: null
  notes: 纯 eval，不需要额外训练。用已有 checkpoint 的 logits 计算。
  status: planned
- id: plan_008
  claim: 1
  description: 'Seed robustness: 3 random seeds (42/123/456) 验证 VOTA 结果稳定性。McNemar
    test + bootstrap CI。'
  priority: P2
  gpu_budget_hours: 6
  deps:
  - plan_001
  registry_id: null
  notes: 每 seed ~2h × 3。不同 seed 间 accuracy 差异应 <2pp。
  status: planned
- id: plan_mvp_vota
  claim: 1
  description: 'MVP: VOTA trace SFT for test verdict prediction'
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: vota_seed42_v4
  notes: 完成。95.63% accuracy, +20.5pp over baseline.
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9916
    majority_baseline: 0.7151
    lift: 0.2765
    n: 1190
    pass_precision: 1
    pass_recall: 0.988
    pass_f1: 0.994
    fail_precision: 0.971
    fail_recall: 1
    fail_f1: 0.985
    accuracy_ci_lower: 0.9857
    accuracy_ci_upper: 0.9966
    train_loss: 0.046
    eval_loss: 0.0842
- id: plan_mvp_notrace
  claim: 1
  description: 'MVP: No-trace baseline for test verdict prediction'
  priority: P0
  gpu_budget_hours: 1
  deps: []
  registry_id: no_trace_seed42_v4
  notes: 完成。75.13% accuracy (majority baseline 71.51%).
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7513
    majority_baseline: 0.7151
    lift: 0.0361
    pass_precision: 0.8776
    pass_recall: 0.7579
    pass_f1: 0.8134
    fail_precision: 0.5473
    fail_recall: 0.7345
    fail_f1: 0.6272
    train_loss: 0.18
    eval_loss: 0.6454
    eval_mean_token_accuracy: 0.8897
- id: plan_mvp_fulltrace
  claim: 2
  description: 'MVP: Full execution trace SFT for test verdict prediction'
  priority: P0
  gpu_budget_hours: 2
  deps: []
  registry_id: full_trace_seed42_v2
  notes: 完成。28.49% accuracy, model collapse (100% predict fail).
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.284
    majority_baseline: 0.7151
    lift: -0.4311
    n: 1190
    pass_precision: 0.923
    pass_recall: 0.085
    pass_f1: 0.155
    fail_precision: 0.445
    fail_recall: 0.785
    fail_f1: 0.568
    train_loss: 0.0373
    eval_loss: 0.082
    eval_mean_token_accuracy: 0.984


## registry (completed experiments)

- exp_id: no_trace_seed42
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: vota_seed42
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: no_trace_seed42_v2
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: vota_seed42_v2
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: no_trace_seed42_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    train_loss: 0.18
    eval_loss: 0.645
    eval_mean_token_accuracy: 0.89
    accuracy: 0.7513
    majority_baseline: 0.7151
    lift: 0.0361
    pass_precision: 0.8776
    pass_recall: 0.7579
    pass_f1: 0.8134
    fail_precision: 0.5473
    fail_recall: 0.7345
    fail_f1: 0.6272
- exp_id: vota_seed42_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    train_loss: 0.046
    eval_loss: 0.085
    eval_mean_token_accuracy: 0.983
    accuracy: 0.992
    majority_baseline: 0.7151
    lift: 0.276
    pass_precision: 0.99
    pass_recall: 0.99
    pass_f1: 0.99
    fail_precision: 0.99
    fail_recall: 0.99
    fail_f1: 0.99
- exp_id: full_trace_seed42
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    train_loss: 0.037
    eval_loss: 0.084
    eval_mean_token_accuracy: 0.984
    accuracy: 0.284
    majority_baseline: 0.7151
    lift: -0.431
    pass_precision: 0.88
    pass_recall: 0.08
    pass_f1: 0.16
    fail_precision: 0.31
    fail_recall: 0.97
    fail_f1: 0.57
- exp_id: no_trace_seed42_v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.7513
    majority_baseline: 0.7151
    lift: 0.0361
    pass_precision: 0.8776
    pass_recall: 0.7579
    pass_f1: 0.8134
    fail_precision: 0.5473
    fail_recall: 0.7345
    fail_f1: 0.6272
    train_loss: 0.18
    eval_loss: 0.6454
    eval_mean_token_accuracy: 0.8897
- exp_id: vota_seed42_v4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.9916
    majority_baseline: 0.7151
    lift: 0.2765
    n: 1190
    pass_precision: 1
    pass_recall: 0.988
    pass_f1: 0.994
    fail_precision: 0.971
    fail_recall: 1
    fail_f1: 0.985
    accuracy_ci_lower: 0.9857
    accuracy_ci_upper: 0.9966
    train_loss: 0.046
    eval_loss: 0.0842
- exp_id: full_trace_seed42_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.284
    majority_baseline: 0.7151
    lift: -0.4311
    n: 1190
    pass_precision: 0.923
    pass_recall: 0.085
    pass_f1: 0.155
    fail_precision: 0.445
    fail_recall: 0.785
    fail_f1: 0.568
    train_loss: 0.0373
    eval_loss: 0.082
    eval_mean_token_accuracy: 0.984

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
  "promptId": "4b4c6a82-341a-448c-a36b-44263b28fda2",
  "type": "user",
  "uuid": "9c53bdf2-0f7b-41fc-ae33-dd831676ee87",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T01:40:28.740Z_

```json
{
  "parentUuid": "9c53bdf2-0f7b-41fc-ae33-dd831676ee87",
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
  "uuid": "9ba33683-0d6e-4b02-95b6-dab7e6599985",
  "timestamp": "2026-05-15T01:40:28.740Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T01:40:28.740Z_

```json
{
  "parentUuid": "9ba33683-0d6e-4b02-95b6-dab7e6599985",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f4504a53-05e2-45b3-b255-3807ce60061a",
  "timestamp": "2026-05-15T01:40:28.740Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：VOTA 效果几乎完全来自 actual==expected 字符串比对；collapse 机制解释不通；泛化失败 核心假设：['去除 actual/expected 后 acc 降至 73-78%（≈no_trace baseline），证明 VOTA 的 lift 本质是将 answer 暴露给模型',…",
  "leafUuid": "f4504a53-05e2-45b3-b255-3807ce60061a",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace ablation for verdict task triviality analysis",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2"
}
```

---

### Assistant

_source line 8 · 2026-05-15T01:40:48.761Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "worst" tier scenario for each planned experiment in the experiment plan. I need to provide specific metrics, rationales, and analysis for each experiment under this worst-case interpretation.

Let me carefully go through each planned experiment and predict what would happen under the "worst" tier assumptions.

The worst tier means:
- VOTA's effect is almost entirely from actual==expected string comparison
- Collapse mechanism doesn't make sense / can't be explained by gradient dilution alone
- Generalization fails

Core assumptions for worst:
1. Removing actual/expected drops acc to 73-78% (≈no_trace baseline), proving VOTA lift is just answer exposure


2. Even with full trace and label-only loss, accuracy still collapses below 50%, suggesting the trace content itself is problematic rather than gradient dilution
3. Component ablations show only actual/expected matters, while exception summaries and loop compression provide negligible gains
4. DeepSeek-Coder shows minimal VOTA lift under 8 percentage points or inconsistent results
5. The second verdict task shows no meaningful improvement from VOTA
6. Seed variance ranges from 2-5 percentage points

Now I'm working through plan_001, the ablation removing actual/expected from VOTA, where accuracy would drop to 73-78% with a lift of -2% to +3% over the no_trace baseline, confirming that VOTA's gains come primarily from answer exposure rather than meaningful trace understanding. entire lift comes from exposing actual/expected values which let the model do string comparison

**plan_002**: full_trace + label-only loss
- Worst: acc still <50%, collapse persists
- Rationale: Even masking trace tokens doesn't help because the trace content during inference introduces distributional shift; the model learns to attend to trace tokens at inference even though loss was only on label

**plan_003**: Component ablation
- Worst: only actual/expected has contribution, others negligible
- Need to predict: (a) only actual/expected, (b) only exception, (c) only loop compression, (d) full VOTA

**plan_004**: DeepSeek-Coder
- Worst: VOTA lift <8pp, pattern inconsistent

**plan_005**: Second task
- Worst: VOTA no significant lift

**plan_006**: Trace length ablation
- Worst: even short traces collapse or near-collapse

**plan_007**: Calibration analysis
- Worst: VOTA calibration is poor despite high accuracy (overconfident)

**plan_008**: Seed robustness
- Worst: variance 2-5pp, some seeds much worse

Let me write this all out in detail.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4504a53-05e2-45b3-b255-3807ce60061a",
  "isSidechain": false,
  "requestId": "req_011Cb3W7G7PHo5SqVupjnZe7",
  "type": "assistant",
  "uuid": "f4189bd5-0bf8-43fa-820b-0dada7a87653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MH1ewY9f8jb2cFNP3dbMCD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11020,
      "cache_read_input_tokens": 11841,
      "output_tokens": 9668,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9668,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11020
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

_source line 9 · 2026-05-15T01:43:43.257Z_

```yaml
tier: worst
narrative_guidance: >
  完全 reframe。放弃 "trace teaches reasoning" 叙事。新 angle："What Makes Verdict Prediction Trivial?
  A Trace Ablation Study"。核心发现：(1) verdict tasks 本质上只需要 assertion-point comparison data，
  不需要任何 reasoning trace；(2) full execution trace 不仅无用而且有害，且 label-only loss 无法修复，
  说明问题不只是 gradient dilution 而是 trace content 引入的 distributional shift；(3) VOTA 的成功恰好
  证明了 verdict tasks 的信息需求极度 sparse。Contribution 重新定位为 "systematic negative result +
  task complexity analysis"。目标 EMNLP Findings。

imagined_experiments:
  - name: "VOTA minus actual/expected ablation"
    plan_id: "plan_001"
    description: >
      去除 VOTA 中 actual/expected 值对，只保留 assertion structure（函数名、断言类型、变量名）
      + exception summary + loop compression。验证 VOTA 效果是否为 trivial string comparison。
    expected_results:
      accuracy: 0.755
      majority_baseline: 0.7151
      lift_over_notrace: 0.004
      pass_precision: 0.86
      pass_recall: 0.78
      pass_f1: 0.82
      fail_precision: 0.56
      fail_recall: 0.70
      fail_f1: 0.62
      train_loss: 0.16
      eval_loss: 0.58
      accuracy_ci_lower: 0.728
      accuracy_ci_upper: 0.782
    result_rationale: >
      在 worst 档下，VOTA 的 ~27pp lift 几乎全部来自 actual/expected 值对的暴露。模型在训练中学到的
      不是 "从 trace 推理出 pass/fail"，而是 "如果 actual 字段和 expected 字段的字符串内容一致则 pass，
      否则 fail"。去除这两个字段后，剩余的 assertion structure（assertEqual、assertTrue 等函数名）、
      exception summary、loop compression 都不包含足以判定 verdict 的信息——assertion 函数名只说明
      "检查了什么类型的条件"，不说明 "条件是否满足"。因此 acc 回落到 75.5%，与 no_trace baseline
      (75.13%) 统计不可区分（lift 仅 0.4pp，远在噪声范围内）。这直接证明 VOTA 本质是一个精心包装的
      answer leakage 机制：actual/expected 就是 verdict 的充分统计量。
    tables:
      - name: "Table: VOTA vs VOTA-no-act/exp vs no_trace"
        rows:
          - condition: "VOTA (full)"
            accuracy: 0.9916
            lift: "+27.65pp"
            ci_95: "[0.986, 0.997]"
          - condition: "VOTA (no actual/expected)"
            accuracy: 0.755
            lift: "+0.4pp"
            ci_95: "[0.728, 0.782]"
          - condition: "no_trace baseline"
            accuracy: 0.7513
            lift: "—"
            ci_95: "[0.724, 0.779]"
    figures_description:
      - "Bar chart: 三条件 accuracy 对比，error bars 为 95% bootstrap CI。VOTA-no-act/exp 的 CI 与 no_trace 完全重叠，视觉上一目了然。"
    analysis: >
      这是论文的 make-or-break 实验。worst 结果彻底否定 "VOTA teaches behavioral reasoning" 叙事。
      但这本身是一个有价值的 negative result：它证明 verdict task 的信息瓶颈极度 sparse——整个 execution
      trace 中唯一有用的信息就是 assertion point 处 actual 和 expected 的具体值。这对 trace SFT 研究
      社区是重要的 calibration：不要假设 trace 中包含的 "reasoning" 就是模型学到的东西。

  - name: "Full trace + label-only loss"
    plan_id: "plan_002"
    description: >
      在 full execution trace 条件下，只对最终 verdict token 计算 loss，mask 所有 trace tokens。
      验证 collapse 根因是 gradient dilution 还是 trace content 本身有害。
    expected_results:
      accuracy: 0.42
      majority_baseline: 0.7151
      lift_over_notrace: -0.331
      pass_precision: 0.74
      pass_recall: 0.38
      pass_f1: 0.50
      fail_precision: 0.33
      fail_recall: 0.50
      fail_f1: 0.40
      train_loss: 0.65
      eval_loss: 0.72
      pct_predict_fail: 0.62
      collapse_severity: "partial"
    result_rationale: >
      在 worst 档下，label-only loss 部分缓解了 collapse（从 28.5% 提到 42%），但远未修复到可用水平。
      这说明 gradient dilution 确实是 collapse 的一个因素（去掉 trace loss 后有改善），但不是唯一因素。
      更深层的问题是 trace content 本身在 inference 时引入的 distributional shift：模型在生成 verdict
      前必须先 attend to 数千个 trace tokens，这些 tokens 的 distribution 与模型 pretraining 分布严重
      不匹配（执行 trace 的格式是模型从未见过的），导致 hidden state 在到达 verdict position 时已经
      偏离了正常的 classification representation space。label-only loss 只解决了训练侧的 gradient
      competition，但无法解决 inference 侧的 context pollution。模型不再 100% 预测 fail，但预测仍然
      高度不可靠（62% 预测 fail vs 真实 28.5% fail rate），说明 trace context 系统性地 bias 模型
      toward negative prediction。这个结果比单纯的 gradient dilution 故事更有趣：它揭示了一个
      "trace as harmful context" 的现象，即 trace 内容在 attention 机制中作为 noise source 干扰分类。
    tables:
      - name: "Table: Full trace loss variants"
        rows:
          - condition: "full_trace (standard loss)"
            accuracy: 0.2849
            pct_fail_pred: "100%"
            status: "complete collapse"
          - condition: "full_trace (label-only loss)"
            accuracy: 0.42
            pct_fail_pred: "62%"
            status: "partial collapse"
          - condition: "no_trace (standard loss)"
            accuracy: 0.7513
            pct_fail_pred: "~45%"
            status: "normal"
          - condition: "VOTA (standard loss)"
            accuracy: 0.9916
            pct_fail_pred: "~28%"
            status: "normal"
    figures_description:
      - "Stacked bar chart: 四条件下 pass/fail 预测分布 vs 真实分布，展示 collapse 的 bias 方向和程度。"
      - "Loss curve comparison: standard loss vs label-only loss 的 training dynamics，展示 label-only loss 收敛更慢但 verdict loss 更低。"
    analysis: >
      这个结果对论文 framing 至关重要。它否定了简单的 "gradient dilution → just mask trace loss" 修复方案，
      说明 full trace 的问题是根本性的：trace content 在 context window 中的存在本身就有害。这支持
      论文的核心论点——verdict task 需要的不是 "更多信息" 而是 "更少但更精准的信息"。可以引入
      "context pollution" 这个概念：当 trace 的 token 数远超 verdict 所需信息量时，多余的 tokens
      不是中性的 padding，而是 active noise sources that corrupt the classification signal。

  - name: "VOTA component ablation (4 sub-conditions)"
    plan_id: "plan_003"
    description: >
      分别测试四个 VOTA 子集：(a) 只有 actual/expected 值对，(b) 只有 exception summary，
      (c) 只有 loop compression，(d) 全量 VOTA。量化每个组件独立贡献。
    expected_results:
      condition_a_actexp_only:
        accuracy: 0.987
        lift_over_notrace: 0.236
        pass_f1: 0.990
        fail_f1: 0.978
      condition_b_exception_only:
        accuracy: 0.762
        lift_over_notrace: 0.011
        pass_f1: 0.825
        fail_f1: 0.635
      condition_c_loop_only:
        accuracy: 0.748
        lift_over_notrace: -0.003
        pass_f1: 0.810
        fail_f1: 0.615
      condition_d_full_vota:
        accuracy: 0.9916
        lift_over_notrace: 0.2765
        pass_f1: 0.994
        fail_f1: 0.985
      component_ablation_min_individual_lift_non_actexp: -0.003
      component_ablation_max_individual_lift_non_actexp: 0.011
    result_rationale: >
      在 worst 档下，component ablation 产生一个极度 skewed 的贡献分布：actual/expected 单独贡献了
      VOTA 几乎全部的 lift（23.6pp out of 27.65pp），而 exception summary 和 loop compression
      各自的独立贡献在统计噪声范围内（+1.1pp 和 -0.3pp）。
      
      (a) actual/expected only (98.7%)：仅比 full VOTA 低 0.5pp，几乎完全恢复了 VOTA 的效果。这确认了
      actual/expected 是 VOTA 的充分统计量。微小的 gap 可能来自少数 exception-based failure cases
      （如 RuntimeError），这些 case 没有 actual/expected 值但有 exception info。
      
      (b) exception summary only (76.2%)：比 no_trace 仅高 1.1pp。exception summary 只覆盖
      抛出异常的 fail cases（大约占 fail cases 的 30-40%），对 pass cases 完全无信息。即使对于
      exception fail cases，exception type + message 也不总是足以判断 test verdict（可能是
      expected exception）。因此 lift 极其有限。
      
      (c) loop compression only (74.8%)：甚至略低于 no_trace baseline（在噪声范围内）。loop
      compression 记录的是循环执行模式（迭代次数、收敛行为），这些信息与 assertion 结果几乎完全
      正交。模型无法从 "这个循环跑了 5 次" 推断出 test 是 pass 还是 fail。微小的负 lift 可能是
      因为 loop info 作为额外 context 引入了轻微的 noise。
      
      (d) full VOTA (99.16%)：比 actual/expected only 高 0.5pp，说明 exception summary 在
      与 actual/expected 组合时有边际贡献（覆盖了 actual/expected 缺失的 exception-only cases）。
    tables:
      - name: "Table: VOTA Component Ablation"
        rows:
          - condition: "actual/expected only"
            accuracy: 0.987
            lift: "+23.6pp"
            delta_vs_full_vota: "-0.5pp"
          - condition: "exception summary only"
            accuracy: 0.762
            lift: "+1.1pp"
            delta_vs_full_vota: "-23.0pp"
          - condition: "loop compression only"
            accuracy: 0.748
            lift: "-0.3pp"
            delta_vs_full_vota: "-24.4pp"
          - condition: "full VOTA"
            accuracy: 0.9916
            lift: "+27.65pp"
            delta_vs_full_vota: "—"
          - condition: "no_trace baseline"
            accuracy: 0.7513
            lift: "—"
            delta_vs_full_vota: "-24.0pp"
    figures_description:
      - "Waterfall chart: 从 no_trace baseline 出发，叠加各 component 的 marginal lift。actual/expected 是唯一显著的 bar，其余两个 component 的 bar 几乎不可见。"
      - "Heatmap: component presence (行) × metric (列)，cell 颜色 = lift magnitude。视觉上 actual/expected 行全亮，其余行全暗。"
    analysis: >
      这是 worst 档下最具诊断价值的实验。它将 VOTA 的 "trace abstraction" 故事还原为一个更简单的事实：
      verdict prediction 所需的全部信息就是 assertion point 处的 actual 和 expected 值。这不是 "trace
      teaches reasoning"——这是 "trace provides the answer key"。论文可以将此 reframe 为一个关于
      task information structure 的发现：verdict tasks 的信息需求是 O(1) 的（只需要 2 个值的比较），
      任何超出此范围的信息都是 noise。VOTA 的成功不是因为它是好的 trace abstraction，而是因为它
      恰好包含了这两个关键值。

  - name: "DeepSeek-Coder-6.7B cross-model validation"
    plan_id: "plan_004"
    description: >
      在 DeepSeek-Coder-6.7B 上复现 VOTA vs no_trace vs full_trace 三条件，
      与 DCSH 同模型进行直接对比。
    expected_results:
      deepseek_vota:
        accuracy: 0.815
        lift_over_notrace: 0.065
        pass_f1: 0.87
        fail_f1: 0.70
      deepseek_notrace:
        accuracy: 0.750
        lift_over_notrace: 0.0
        pass_f1: 0.82
        fail_f1: 0.61
      deepseek_fulltrace:
        accuracy: 0.355
        lift_over_notrace: -0.395
        pass_f1: 0.28
        fail_f1: 0.52
      deepseek_vota_lift: 0.065
      pattern_consistency: "inconsistent"
    result_rationale: >
      在 worst 档下，DeepSeek-Coder 上 VOTA lift 仅 6.5pp（vs CodeLlama 上 27.65pp），pattern
      严重不一致。原因分析：
      
      (1) DeepSeek-Coder 的 pretraining 数据可能包含更多 test-related code，使得 no_trace baseline
      更高或对 trace format 的 sensitivity 不同。
      
      (2) 更关键的是，如果 VOTA 的 lift 主要来自 actual/expected 字符串比对，那么不同模型对这种
      "shortcut" 的利用效率会不同。CodeLlama 可能恰好在 string comparison pattern 上更强（或者
      其 tokenizer 对 actual/expected 值的 encoding 更有利于比较），而 DeepSeek-Coder 可能需要
      更多样本才能学会同样的 shortcut。
      
      (3) full_trace 在 DeepSeek-Coder 上也 collapse，但程度略轻（35.5% vs 28.5%），可能因为
      DeepSeek-Coder 的 context handling 稍好，但根本问题（trace content pollution）仍然存在。
      
      (4) 6.5pp 的 lift 虽然不为零，但考虑到 seed variance 可能在 2-5pp，这个 lift 的统计显著性
      很弱（bootstrap CI 可能包含零）。这使得 "VOTA helps across models" 的 claim 无法成立。
    tables:
      - name: "Table: Cross-model comparison"
        rows:
          - model: "CodeLlama-7B"
            vota_acc: 0.9916
            notrace_acc: 0.7513
            fulltrace_acc: 0.2849
            vota_lift: "+27.65pp"
          - model: "DeepSeek-Coder-6.7B"
            vota_acc: 0.815
            notrace_acc: 0.750
            fulltrace_acc: 0.355
            vota_lift: "+6.5pp"
    figures_description:
      - "Grouped bar chart: 两个模型 × 三条件的 accuracy 对比。CodeLlama 上 VOTA 的巨大 lift bar 与 DeepSeek 上的微小 lift bar 形成鲜明对比。"
    analysis: >
      cross-model inconsistency 是 worst 档最致命的结果之一。它说明 VOTA 的效果高度 model-specific，
      不能 generalize 为一个 robust 的 trace design principle。在 reframed narrative 下，这反而支持
      "VOTA 效果来自 string comparison shortcut" 的论点：不同模型利用 shortcut 的能力不同，导致
      lift 不一致。论文可以讨论 "model-specific shortcut exploitation" 作为 trace SFT 评估的一个 pitfall。

  - name: "Second verdict task (DebugBench bug detection)"
    plan_id: "plan_005"
    description: >
      在 DebugBench (Python subset) 上测试 VOTA，任务为 bug detection（给定代码判断是否有 bug）。
      验证 verdict task 泛化性。
    expected_results:
      debugbench_vota:
        accuracy: 0.685
        lift_over_notrace: 0.035
        pass_f1: 0.72
        fail_f1: 0.63
      debugbench_notrace:
        accuracy: 0.650
        lift_over_notrace: 0.0
        pass_f1: 0.70
        fail_f1: 0.57
      debugbench_fulltrace:
        accuracy: 0.415
        lift_over_notrace: -0.235
      second_task_vota_lift: 0.035
      statistically_significant: false
    result_rationale: >
      在 worst 档下，VOTA 在第二个 verdict task 上几乎无效（lift 仅 3.5pp，p > 0.05）。核心原因：
      
      (1) Bug detection 任务的信息结构与 test verdict prediction 根本不同。test verdict 有明确的
      assertion point（actual vs expected），而 bug detection 没有这样的 "answer key"——没有一个
      single comparison point 能直接判定代码是否有 bug。VOTA 的 actual/expected 提取逻辑在 bug
      detection 场景下没有等价物。
      
      (2) 即使为 bug detection 设计了类似的 trace abstraction（例如提取 variable state at suspicious
      locations），这些 locations 的选择本身就需要 bug understanding，形成鸡生蛋问题。
      
      (3) bug detection 的 base rate 通常更接近 50/50（DebugBench 设计为 balanced），使得 majority
      baseline 更低，但 VOTA 缺乏可利用的 shortcut 来产生大的 lift。
      
      (4) full_trace 在 bug detection 上同样有害（41.5%），但 collapse 不如 test verdict 严重，
      可能因为 bug detection 的训练信号稍强于 test verdict（fail cases 的 trace 差异更大）。
      
      这个结果证明 VOTA 的 test verdict prediction 成功是 task-specific 的 shortcut exploitation，
      而非 generalizable trace design principle。
    tables:
      - name: "Table: Cross-task comparison"
        rows:
          - task: "Test verdict prediction"
            vota_acc: 0.9916
            notrace_acc: 0.7513
            vota_lift: "+27.65pp"
            significant: "yes"
          - task: "Bug detection (DebugBench)"
            vota_acc: 0.685
            notrace_acc: 0.650
            vota_lift: "+3.5pp"
            significant: "no"
    figures_description:
      - "Side-by-side bar charts: 两个 task 上 VOTA lift 的对比，配合 error bars 展示第二 task 上 CI 包含零。"
    analysis: >
      泛化失败是 worst 档 narrative 的关键支柱。它将论文的 contribution 从 "VOTA is a good trace
      design" 彻底转向 "verdict tasks have heterogeneous information structures, and trace SFT
      only helps when the trace happens to contain a task-specific shortcut"。这是一个更有趣的
      negative finding：它暗示不存在 universal trace design for verdict tasks。

  - name: "Trace length ablation (full trace truncation)"
    plan_id: "plan_006"
    description: >
      测试不同截断长度 (256/512/1024/2048 tokens) 对 full_trace accuracy 的影响，
      绘制 accuracy vs trace length 曲线。
    expected_results:
      length_256:
        accuracy: 0.58
        pct_predict_fail: 0.52
      length_512:
        accuracy: 0.46
        pct_predict_fail: 0.61
      length_1024:
        accuracy: 0.35
        pct_predict_fail: 0.78
      length_2048:
        accuracy: 0.29
        pct_predict_fail: 0.95
      full_untruncated:
        accuracy: 0.2849
        pct_predict_fail: 1.0
      monotonic_decrease: true
      shortest_still_collapses: true
    result_rationale: >
      在 worst 档下，accuracy 随 trace length 单调下降，且即使最短的 256 tokens 也只达到 58%——
      远低于 no_trace baseline (75.13%)。这说明：
      
      (1) trace content 从第一个 token 开始就是有害的，不存在 "sweet spot" 的截断长度能让 full trace
      变得有用。这否定了 "full trace 只是太长了" 的简单解释。
      
      (2) 256 tokens 的 full trace 通常只包含前几行代码的执行状态（变量初始化、import 等），这些
      信息对 verdict 完全无关但占据了 context 并 bias attention。
      
      (3) 单调下降趋势支持 "context pollution" 假说：每增加一个 trace token 都增加一点 noise，
      累积效应导致 collapse。在 256 tokens 时 noise 不足以完全淹没信号（58%），但在 2048+ tokens
      时 noise 完全主导（29%）。
      
      (4) 对比 VOTA 的 ~50-100 tokens（只有 actual/expected 等关键值），full trace 的信噪比从根本上
      就是错误的。这进一步证明 verdict task 需要的是 extreme information compression，不是 more
      execution detail。
    tables:
      - name: "Table: Accuracy vs trace truncation length"
        rows:
          - length: "0 (no_trace)"
            accuracy: 0.7513
            delta_vs_notrace: "—"
          - length: "VOTA (~80 tokens avg)"
            accuracy: 0.9916
            delta_vs_notrace: "+27.65pp"
          - length: 256
            accuracy: 0.58
            delta_vs_notrace: "-17.1pp"
          - length: 512
            accuracy: 0.46
            delta_vs_notrace: "-29.1pp"
          - length: 1024
            accuracy: 0.35
            delta_vs_notrace: "-40.1pp"
          - length: 2048
            accuracy: 0.29
            delta_vs_notrace: "-46.1pp"
          - length: "full (~4000 avg)"
            accuracy: 0.2849
            delta_vs_notrace: "-46.6pp"
    figures_description:
      - "Line plot: x = trace length (log scale, 0/VOTA/256/512/1024/2048/full), y = accuracy。no_trace 和 VOTA 作为 horizontal reference lines。曲线从 256 开始单调下降，始终在 no_trace baseline 以下。标题强调 'Any amount of full trace hurts'。"
    analysis: >
      这个实验产生了一个视觉上非常 compelling 的图：VOTA（~80 tokens）在最上方，no_trace 在中间作为
      baseline，而 full trace 的所有截断长度都在 baseline 以下且单调下降。这完美支持 "information
      density, not information volume" 的论点。在 reframed narrative 中，这张图可以作为 Figure 1
      或 key result figure。

  - name: "Calibration analysis (ECE + reliability diagrams)"
    plan_id: "plan_007"
    description: >
      用已有 checkpoint 的 logits 计算 ECE + reliability diagrams，对比 VOTA/no_trace/full_trace
      的 calibration 质量。
    expected_results:
      vota_ece: 0.065
      notrace_ece: 0.12
      fulltrace_ece: 0.58
      vota_overconfident: true
      vota_avg_confidence: 0.97
      vota_avg_accuracy: 0.9916
      notrace_underconfident_on_pass: true
      fulltrace_miscalibrated: true
    result_rationale: >
      在 worst 档下，calibration 分析揭示一个微妙但重要的问题：
      
      (1) VOTA 的 ECE 看起来尚可（0.065），但这是因为模型在绝大多数样本上都给出 >95% confidence
      且确实正确——本质上是 "trivially calibrated by being trivially correct"。模型学会了
      "actual == expected → 99% pass"的简单规则，confidence 自然很高且准确。这不是 genuine
      calibration improvement，而是 task trivialization 的副产品。
      
      (2) no_trace 的 ECE 更高（0.12），主要因为模型在 fail cases 上 underconfident——它缺乏
      判断 fail 的信息，所以经常给出 50-60% 的 ambiguous predictions。
      
      (3) full_trace 的 ECE 极差（0.58），因为 collapsed model 对所有样本都高 confidence 预测 fail，
      但 71.5% 的样本实际是 pass。这是 catastrophic miscalibration。
      
      (4) 值得注意的是，VOTA 在少数 error cases 上也极度 overconfident（>95% confidence 但错误），
      说明模型没有学到 uncertainty awareness，只是学了一个几乎总是对的 shortcut rule。
    tables:
      - name: "Table: Calibration metrics"
        rows:
          - condition: "VOTA"
            ece: 0.065
            avg_confidence: 0.97
            avg_accuracy: 0.9916
            interpretation: "trivially calibrated"
          - condition: "no_trace"
            ece: 0.12
            avg_confidence: 0.72
            avg_accuracy: 0.7513
            interpretation: "underconfident on fail"
          - condition: "full_trace"
            ece: 0.58
            avg_confidence: 0.88
            avg_accuracy: 0.2849
            interpretation: "catastrophic miscalibration"
    figures_description:
      - "Reliability diagram (3-panel): 每个条件一个 panel，x = predicted confidence bin, y = actual accuracy in bin。VOTA 的点集中在右上角；no_trace 的点偏离对角线（underconfident region）；full_trace 的点在右下角（high confidence, low accuracy）。"
    analysis: >
      Calibration 分析在 worst 档下更多是 supporting evidence 而非 headline result。它说明 VOTA 的
      高 accuracy 伴随的是 "confident because trivial" 的 calibration pattern，而非 "well-calibrated
      because well-understood"。在论文中可以用一小段讨论这个 distinction：good calibration 不等于
      good understanding。

  - name: "Seed robustness (3 seeds × VOTA)"
    plan_id: "plan_008"
    description: >
      3 random seeds (42/123/456) 验证 VOTA 结果稳定性。McNemar test + bootstrap CI。
    expected_results:
      seed_42:
        accuracy: 0.9916
      seed_123:
        accuracy: 0.965
      seed_456:
        accuracy: 0.978
      mean_accuracy: 0.978
      std_accuracy: 0.013
      max_min_spread_pp: 2.66
      seed_variance_pp: 2.66
      mcnemar_42_vs_123_p: 0.002
      mcnemar_42_vs_456_p: 0.08
      bootstrap_ci_mean: [0.960, 0.992]
    result_rationale: >
      在 worst 档下，seed variance 在 2-5pp 范围的低端（2.66pp spread），但 pattern 是 revealing 的：
      
      (1) Seed 42（原始结果）恰好是最高的（99.16%），这引入了 "cherry-picking" 风险——我们报告的
      headline number 是 3 seeds 中的最佳值。Mean across seeds 是 97.8%，仍然很高，但 narrative
      impact 不同："97.8% ± 1.3%" 比 "99.16%" 听起来略弱。
      
      (2) 2.66pp 的 spread 在绝对值上不大，但考虑到 VOTA 的 error rate 本来就很低（~1-4%），这意味着
      不同 seeds 之间的 error rate 差异可以达到 3x（0.84% vs 3.5%）。这说明模型学到的 shortcut
      rule 在边界 cases 上不稳定。
      
      (3) Seed 123 的 96.5% 较低，可能因为该 seed 的 train/eval split 或 optimization trajectory
      使得模型在某些 edge cases（如 assertion 格式不标准、actual/expected 值非常长需要截断的 cases）
      上学得不好。
      
      (4) McNemar test 显示 seed 42 vs 123 有 significant difference (p=0.002)，进一步说明
      individual seed results 不应被 over-interpreted。
    tables:
      - name: "Table: Seed robustness"
        rows:
          - seed: 42
            accuracy: 0.9916
            error_rate: "0.84%"
          - seed: 123
            accuracy: 0.965
            error_rate: "3.50%"
          - seed: 456
            accuracy: 0.978
            error_rate: "2.20%"
          - seed: "mean ± std"
            accuracy: "0.978 ± 0.013"
            error_rate: "2.18% ± 1.33%"
    figures_description:
      - "Strip plot: 3 seeds 的 accuracy 点 + mean with error bar。标注 seed 42 是原始报告值。"
    analysis: >
      seed robustness 结果在 worst 档下是 "adequate but not inspiring"。2.66pp spread 不会
      invalidate 主要结论（VOTA >> no_trace 在所有 seeds 上都成立），但会弱化 headline number。
      论文应报告 mean ± std 而非 single seed。在 reframed narrative 下，这个 variance 可以
      解释为 "shortcut learning 的 inherent instability"——不同 seeds 在 shortcut boundary
      cases 上的行为不同。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4189bd5-0bf8-43fa-820b-0dada7a87653",
  "isSidechain": false,
  "requestId": "req_011Cb3W7G7PHo5SqVupjnZe7",
  "type": "assistant",
  "uuid": "006df90e-84b8-4ba7-a11a-98cdb2f02795",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MH1ewY9f8jb2cFNP3dbMCD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11020,
      "cache_read_input_tokens": 11841,
      "output_tokens": 9668,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9668,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11020
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：VOTA 效果几乎完全来自 actual==expected 字符串比对；collapse 机制解释不通；泛化失败 核心假设：['去除 actual/expected 后 acc 降至 73-78%（≈no_trace baseline），证明 VOTA 的 lift 本质是将 answer 暴露给模型',…",
  "leafUuid": "006df90e-84b8-4ba7-a11a-98cdb2f02795",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace ablation for verdict task triviality analysis",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：VOTA 效果几乎完全来自 actual==expected 字符串比对；collapse 机制解释不通；泛化失败 核心假设：['去除 actual/expected 后 acc 降至 73-78%（≈no_trace baseline），证明 VOTA 的 lift 本质是将 answer 暴露给模型',…",
  "leafUuid": "006df90e-84b8-4ba7-a11a-98cdb2f02795",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Trace ablation for verdict task triviality analysis",
  "sessionId": "5a70e784-9e93-4588-91e0-070c6c762ca2"
}
```

---
