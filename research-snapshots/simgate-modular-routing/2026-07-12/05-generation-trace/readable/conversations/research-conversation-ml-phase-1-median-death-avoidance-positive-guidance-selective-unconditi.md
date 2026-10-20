# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心假设部分成立：death avoidance 机制复现但无 positive guidance 信号，selective > unconditi

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/c2441971-e1a1-4afd-9cd0-5437ee84499f.jsonl`
- **Structured JSON:** [`4f547c064078407baeed.json`](../../sessions/4f/4f547c064078407baeed.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T15:37:17.435Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T15:37:17.435Z",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心假设部分成立：death avoidance 机制复现但无 positive guidance 信号，selective > unconditional 一致但幅度较小，explicit > implicit 成立但差距不大，整体分数接近但未超过 CogRouter\n核心假设：['A1 death avoidance 为主要增益来源——成立，但增益集中在 physics/chemistry tasks，biology/ecology tasks 增益小', 'A2 selective > unconditional——成立但差距缩至 5-12 分，部分 task type 差距不显著', 'A3 explicit > implicit——成立但差距仅 3-8 分，statistical significance 在部分 task type 边缘', 'A4 counterfactual labels 泛化中等，router accuracy 一般——部分成立，弱 task types 标签噪声大', 'A5 routing pattern 可解释——部分成立，能看到 phase-dependent 模式但 failure taxonomy 不够清晰', 'A6 无 positive guidance 信号——death avoidance 是唯一机制']\n关键指标范围：{'simgate_score_overall': [72, 84], 'simgate_minus_always_internal': [15, 25], 'oracle_minus_always_det': [5, 12], 'explicit_minus_implicit': [3, 8], 'catastrophic_failure_reduction_pct': [40, 60], 'router_accuracy_pct': [65, 75], 'simulator_invocation_ratio_pct': [30, 50], 'task_types_with_significant_gain': [8, 12]}\n叙事方向：需要调整 claims 强度和重心。 C1 调整: 不与 CogRouter 直接比 SOTA（因为差距不显著或略低），改为强调 \"SimGate vs 自身 ablation baselines\" 的受控实验，突出 safety-net 机制的因果证据。Headline 改为 \"reduces catastrophic failures by [50]%\" 而非追求绝对分数。 C2 调整: explicit vs implicit 差距写成 \"consistent but moderate advantage\"， 重心转向 interpretability/modularity 的定性价值（router 可独立替换、可分析）， 而非纯粹的性能差距。routing pattern 分析从 \"failure mode taxonomy\" 降为 \"phase-dependent routing trends\"。 补充实验: 考虑加入 2-way vs 3-way ablation (plan-006) 来增加实验密度弥补单一 headline number 的不足。 整体叙事从 \"new SOTA via safety-aware routing\" 转向 \"first explicit study of when deterministic computation helps LLM agents, with controlled causal evidence\"。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: simgate-modular-routing\nfocus: Short paper (4 pages). Core contribution: safety-aware routing to deterministic computation. MVP showed death avoidance as primary mechanism (+30-40 points). Key risk: novelty perception (SFT small router is simple). Strength: empirical finding + routing pattern analysis + explicit vs implicit ablation. ScienceWorld only in main text.\n\n## paper_framing.md\n\n# Paper Framing — simgate-modular-routing\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (12 days remaining)\n\n## Core Insight\n\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures at CPU-only cost — but no method learns WHEN to invoke it via an explicit, interpretable router. MVP evidence: death avoidance is the primary mechanism (+30-40 points from preventing -100 penalties), and selective routing outperforms unconditional simulation by +10-17 points.\n\n## Core Claims (2 claims for short paper)\n\n**C1 (Selective routing to deterministic computation)**: On ScienceWorld, learned selective routing to a deterministic environment simulator significantly outperforms both pure LLM reasoning and unconditional simulation. The primary value mechanism is catastrophic failure prevention: the simulator serves as a \"safety net\" that intercepts actions leading to irreversible negative outcomes, rather than providing positive task guidance.\n\n**C2 (Explicit modular router)**: A lightweight explicit router (Qwen3-1.7B, ~1.7B params), trained via SFT on counterfactual trajectory labels, achieves effective per-step routing that is (a) interpretable — routing decisions can be analyzed per task category to reveal systematic LLM failure modes, (b) architecturally decoupled from the agent backbone, and (c) consistent across task categories sharing similar failure patterns.\n\n## Story Spine\n\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. No method provides an explicit, modular router for selective invocation of ground-truth deterministic computation.\n\n- **Our framing**: We recast the \"when to simulate\" problem as safety-aware routing. Deterministic computation is not primarily a performance booster — it is a catastrophic failure prevention mechanism. A lightweight explicit router learns to detect high-risk states where LLM reasoning is likely to fail catastrophically, and routes those steps to deterministic computation for ground-truth verification. This \"router-as-safety-net\" framing explains why: (1) the gain is concentrated in death avoidance (+30-40 points from preventing -100 penalties), (2) selective routing beats unconditional simulation (not every step needs the safety net), and (3) the router's decisions are interpretable as a diagnostic of where LLMs systematically fail.\n\n- **Headline result template**: \"On ScienceWorld, SimGate achieves [X] score (vs CogRouter 84.6, ITP-R 62.58), reducing catastrophic failures by [Y]% compared to pure LLM reasoning, while using [Z]% fewer simulator invocations than always-simulate.\"\n\n## Paper Structure (4-page short paper)\n\n| Section | Pages | Content |\n|---------|-------|---------|\n| Abstract | 0.2 | Safety-aware routing framing, headline numbers |\n| Introduction | 0.8 | Problem + gap + contribution (2 claims) |\n| Method | 1.0 | 3-component framework: backbone + deterministic oracle + explicit router; counterfactual training pipeline (4-step); router architecture |\n| Experiments | 1.5 | Main results table + explicit vs implicit ablation + routing pattern analysis figure |\n| Conclusion | 0.3 | Summary + limitations + future (MATH, API routing) |\n| References | ~0.5 | Not counted in 4-page limit |\n\n## Anticipated Reviewer Concerns & Mitigations\n\n1. **\"Novelty is incremental — just SFT a small model to classify\"**\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\n\n2. **\"Only one benchmark (ScienceWorld)\"**\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\n\n3. **\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\"**\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\n\n4. **\"Death avoidance is trivial — just filter dangerous actions\"**\n   - Mitigation: Always-deterministic (which filters every step) underperforms oracle routing by 10-17 points. The non-trivial part is SELECTIVE invocation — knowing which steps need the safety net. Routing pattern analysis shows the router learns meaningful state-dependent decisions.\n\n5. **\"DAgger gap — SFT on oracle labels under base policy may not transfer\"**\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension.\n\n## Venue Fit Risks\n\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\n- Short paper format matches focused contribution scope\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \"Scope & Future Work\" paragraph\n- Risk: \"Safety-aware\" framing may be perceived as overselling if death avoidance is the ONLY signal — need to check if positive guidance signal emerges in full trajectory collection (even small positive guidance would strengthen the story)\n\n## Key Differences from IDEA_BRIEF\n\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\n2. **Framing shifted**: From \"general routing to deterministic computation\" to \"safety-aware routing\" based on MVP death avoidance finding.\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\n4. **\"ANY form\" softened**: Per Human Review Note #4, \"across multiple forms\" instead of \"ANY form\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\n\n\n## experiment_plan (with registry status)\n\n- id: plan-001\n  claim:\n  - C1\n  - C2\n  description: 'Counterfactual trajectory collection on ScienceWorld. Run Qwen2.5-7B\n    agent on 15+ task types (20 episodes each, max_steps=30). At each step, execute\n    all 3 modalities (fast-internal, deep-internal, deterministic) and record which\n    leads to best eventual task score via hindsight labeling. Output: (state, observation,\n    best_modality) triples for router SFT.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'MVP covered 5 task types. Need to expand to 15+ for paper. Strong tasks\n    (boil, melt, change-state) + medium (mix-paint) + weak (grow-plant) + new types.\n    vLLM backend on both GPUs for speed. Parallelise across task types.\n\n    '\n  status: planned\n- id: plan-002\n  claim: C2\n  description: 'Router SFT training. Fine-tune Qwen3-1.7B on counterfactual labels\n    from plan-001. Cross-entropy loss, (history, observation) → {fast-internal, deep-internal,\n    deterministic}. Train/val split by task type (leave-one-out or 80/20).\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan-001\n  notes: 'Follow ARES training pipeline. Single GPU sufficient. Hyperparams: lr=2e-5,\n    batch=32, epochs=3, max_seq_len=2048.\n\n    '\n  status: planned\n- id: plan-003\n  claim: C1\n  description: 'SimGate end-to-end evaluation on ScienceWorld. Run trained router\n    + Qwen2.5-7B backbone on held-out episodes. Compare against: always-internal,\n    always-deterministic, oracle-routing, random-routing, confidence-threshold heuristic.\n    Report: continuous score (CogRouter protocol), success rate, catastrophic failure\n    rate, simulator invocation ratio, total LLM tokens.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan-002\n  notes: 'CogRouter (84.6) and ITP-R (62.58) cited from papers, not reproduced. Bootstrap\n    90% CI on all comparisons. Per-task-type breakdown.\n\n    '\n  status: planned\n- id: plan-004\n  claim: C2\n  description: 'Explicit vs implicit routing ablation. Same Qwen2.5-7B backbone. Implicit:\n    backbone decides when to invoke simulator via tool-use prompt (no separate router).\n    Explicit: SimGate router. Both trained on same counterfactual data. This is the\n    core ablation for C2 — quantifies the value of explicit modular routing.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan-001\n  notes: 'Implicit routing = add \"You may invoke the simulator by outputting [SIMULATE]\"\n    to prompt. Train with same labels (SFT on backbone to output [SIMULATE] at oracle-labeled\n    steps). Can run in parallel with plan-002 on second GPU.\n\n    '\n  status: planned\n- id: plan-005\n  claim:\n  - C1\n  - C2\n  description: 'Per-task routing pattern analysis. From plan-003 outputs, analyze:\n    (a) which task categories trigger deterministic routing most, (b) at which episode\n    phases (early/mid/late) routing decisions concentrate, (c) router-as-diagnostic-probe\n    — cluster deterministic-routing steps to identify systematic LLM failure modes\n    (e.g., multi-step physical reasoning failures). Output: routing heatmap figure\n    + failure mode taxonomy.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan-003\n  notes: Analysis-only, minimal GPU. Main output is Figure 1 for the paper.\n  status: planned\n- id: plan-006\n  claim: C2\n  description: '2-way vs 3-way routing ablation. Compare {internal, deterministic}\n    vs {fast-internal, deep-internal, deterministic}. Tests whether the fast/deep\n    internal distinction adds value beyond binary routing.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan-002\n  notes: 'If 2-way ≈ 3-way, simplifies the story (router just decides simulate-or-not).\n    If 3-way > 2-way, supports nuanced compute allocation claim.\n\n    '\n  status: planned\n- id: plan-007\n  claim: C1\n  description: 'Boil task rerun with v3 code. MVP boil data used old code (>= tie-break,\n    death filter on all 3 modes). Rerun with clean v3 code for unified analysis.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  notes: Can run in parallel with plan-001 as first batch.\n  status: planned\n- id: plan-008\n  claim: C2\n  description: 'Router size ablation. Compare Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B\n    as router. Tests sensitivity to router capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan-001\n  notes: 'Important for \"lightweight\" claim. If 1.5B matches 1.7B, strengthens \"small\n    router suffices\". Low priority relative to core experiments.\n\n    '\n  status: planned\n- id: plan-009\n  claim: C1\n  description: 'MATH track — code interpreter as deterministic oracle. 500 Level 4-5\n    MATH problems. 3-way routing: fast-internal / deep-internal / code-interpreter.\n    Demonstrates generalization beyond environment simulators.\n\n    '\n  priority: P2\n  gpu_budget_hours: 20\n  deps:\n  - plan-002\n  notes: 'Human Review Note suggested MATH as secondary track. Only if ScienceWorld\n    experiments finish by Day 8. Could be strong differentiator but tight on time.\n\n    '\n  status: planned\n- id: plan-010\n  claim: C2\n  description: 'Cross-task transfer within ScienceWorld. Train router on chemistry\n    tasks only, evaluate on physics tasks (and vice versa). Tests whether routing\n    patterns transfer across task domains.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-p0-forking\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fork_success_rate: 1\n    avg_latency_s: 1.67\n    p50_latency_s: 1.53\n    p95_latency_s: 2.37\n    max_memory_mb: 20\n    gate: PASS\n- exp_id: mvp-p1-signal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-p1-gpu1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp-p1-gpu0\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    boil_20ep:\n      internal_mean: -49.8\n      det_mean: -19.7\n      oracle_mean: -29.7\n    note: 旧代码 (>= tie-break, 无 death filter), boil 20/20 完成, melt/change-state 未跑\n- exp_id: mvp-p1-gpu1-vllm\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp-p1-gpu1-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp-p1-gpu1-v3\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-p1-gpu0-vllm\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    melt:\n      internal_mean: -54.7\n      det_mean: -14.55\n      oracle_mean: 2.15\n      det_minus_internal: 40.15\n      bootstrap_90ci:\n      - 25\n      - 60.15\n    change_state:\n      internal_mean: -54.7\n      det_mean: -14.5\n      oracle_mean: 0.45\n      det_minus_internal: 40.2\n      bootstrap_90ci:\n      - 25\n      - 60.15\n    pooled:\n      det_minus_internal: 40.17\n      bootstrap_90ci:\n      - 27.6\n      - 52.77\n    n_episodes_per_task: 20\n    ci_lower_gt_0: true\n    tasks_significant: 2/2\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-13T15:37:17.439Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T15:37:17.439Z",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f"
}
```

---

## Round 1

20 recorded events

### User

_source line 3 · 2026-05-13T15:37:17.459Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心假设部分成立：death avoidance 机制复现但无 positive guidance 信号，selective > unconditional 一致但幅度较小，explicit > implicit 成立但差距不大，整体分数接近但未超过 CogRouter
核心假设：['A1 death avoidance 为主要增益来源——成立，但增益集中在 physics/chemistry tasks，biology/ecology tasks 增益小', 'A2 selective > unconditional——成立但差距缩至 5-12 分，部分 task type 差距不显著', 'A3 explicit > implicit——成立但差距仅 3-8 分，statistical significance 在部分 task type 边缘', 'A4 counterfactual labels 泛化中等，router accuracy 一般——部分成立，弱 task types 标签噪声大', 'A5 routing pattern 可解释——部分成立，能看到 phase-dependent 模式但 failure taxonomy 不够清晰', 'A6 无 positive guidance 信号——death avoidance 是唯一机制']
关键指标范围：{'simgate_score_overall': [72, 84], 'simgate_minus_always_internal': [15, 25], 'oracle_minus_always_det': [5, 12], 'explicit_minus_implicit': [3, 8], 'catastrophic_failure_reduction_pct': [40, 60], 'router_accuracy_pct': [65, 75], 'simulator_invocation_ratio_pct': [30, 50], 'task_types_with_significant_gain': [8, 12]}
叙事方向：需要调整 claims 强度和重心。 C1 调整: 不与 CogRouter 直接比 SOTA（因为差距不显著或略低），改为强调 "SimGate vs 自身 ablation baselines" 的受控实验，突出 safety-net 机制的因果证据。Headline 改为 "reduces catastrophic failures by [50]%" 而非追求绝对分数。 C2 调整: explicit vs implicit 差距写成 "consistent but moderate advantage"， 重心转向 interpretability/modularity 的定性价值（router 可独立替换、可分析）， 而非纯粹的性能差距。routing pattern 分析从 "failure mode taxonomy" 降为 "phase-dependent routing trends"。 补充实验: 考虑加入 2-way vs 3-way ablation (plan-006) 来增加实验密度弥补单一 headline number 的不足。 整体叙事从 "new SOTA via safety-aware routing" 转向 "first explicit study of when deterministic computation helps LLM agents, with controlled causal evidence"。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: simgate-modular-routing
focus: Short paper (4 pages). Core contribution: safety-aware routing to deterministic computation. MVP showed death avoidance as primary mechanism (+30-40 points). Key risk: novelty perception (SFT small router is simple). Strength: empirical finding + routing pattern analysis + explicit vs implicit ablation. ScienceWorld only in main text.

## paper_framing.md

# Paper Framing — simgate-modular-routing

## Target Venue
- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026 (12 days remaining)

## Core Insight

LLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures at CPU-only cost — but no method learns WHEN to invoke it via an explicit, interpretable router. MVP evidence: death avoidance is the primary mechanism (+30-40 points from preventing -100 penalties), and selective routing outperforms unconditional simulation by +10-17 points.

## Core Claims (2 claims for short paper)

**C1 (Selective routing to deterministic computation)**: On ScienceWorld, learned selective routing to a deterministic environment simulator significantly outperforms both pure LLM reasoning and unconditional simulation. The primary value mechanism is catastrophic failure prevention: the simulator serves as a "safety net" that intercepts actions leading to irreversible negative outcomes, rather than providing positive task guidance.

**C2 (Explicit modular router)**: A lightweight explicit router (Qwen3-1.7B, ~1.7B params), trained via SFT on counterfactual trajectory labels, achieves effective per-step routing that is (a) interpretable — routing decisions can be analyzed per task category to reveal systematic LLM failure modes, (b) architecturally decoupled from the agent backbone, and (c) consistent across task categories sharing similar failure patterns.

## Story Spine

- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. No method provides an explicit, modular router for selective invocation of ground-truth deterministic computation.

- **Our framing**: We recast the "when to simulate" problem as safety-aware routing. Deterministic computation is not primarily a performance booster — it is a catastrophic failure prevention mechanism. A lightweight explicit router learns to detect high-risk states where LLM reasoning is likely to fail catastrophically, and routes those steps to deterministic computation for ground-truth verification. This "router-as-safety-net" framing explains why: (1) the gain is concentrated in death avoidance (+30-40 points from preventing -100 penalties), (2) selective routing beats unconditional simulation (not every step needs the safety net), and (3) the router's decisions are interpretable as a diagnostic of where LLMs systematically fail.

- **Headline result template**: "On ScienceWorld, SimGate achieves [X] score (vs CogRouter 84.6, ITP-R 62.58), reducing catastrophic failures by [Y]% compared to pure LLM reasoning, while using [Z]% fewer simulator invocations than always-simulate."

## Paper Structure (4-page short paper)

| Section | Pages | Content |
|---------|-------|---------|
| Abstract | 0.2 | Safety-aware routing framing, headline numbers |
| Introduction | 0.8 | Problem + gap + contribution (2 claims) |
| Method | 1.0 | 3-component framework: backbone + deterministic oracle + explicit router; counterfactual training pipeline (4-step); router architecture |
| Experiments | 1.5 | Main results table + explicit vs implicit ablation + routing pattern analysis figure |
| Conclusion | 0.3 | Summary + limitations + future (MATH, API routing) |
| References | ~0.5 | Not counted in 4-page limit |

## Anticipated Reviewer Concerns & Mitigations

1. **"Novelty is incremental — just SFT a small model to classify"**
   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.

2. **"Only one benchmark (ScienceWorld)"**
   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.

3. **"Comparison unfair — CogRouter uses RL (CoPO), you use SFT"**
   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.

4. **"Death avoidance is trivial — just filter dangerous actions"**
   - Mitigation: Always-deterministic (which filters every step) underperforms oracle routing by 10-17 points. The non-trivial part is SELECTIVE invocation — knowing which steps need the safety net. Routing pattern analysis shows the router learns meaningful state-dependent decisions.

5. **"DAgger gap — SFT on oracle labels under base policy may not transfer"**
   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension.

## Venue Fit Risks

- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)
- Short paper format matches focused contribution scope
- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in "Scope & Future Work" paragraph
- Risk: "Safety-aware" framing may be perceived as overselling if death avoidance is the ONLY signal — need to check if positive guidance signal emerges in full trajectory collection (even small positive guidance would strengthen the story)

## Key Differences from IDEA_BRIEF

1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.
2. **Framing shifted**: From "general routing to deterministic computation" to "safety-aware routing" based on MVP death avoidance finding.
3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).
4. **"ANY form" softened**: Per Human Review Note #4, "across multiple forms" instead of "ANY form". Paper demonstrates principle on simulators; code interpreters discussed as extension.


## experiment_plan (with registry status)

- id: plan-001
  claim:
  - C1
  - C2
  description: 'Counterfactual trajectory collection on ScienceWorld. Run Qwen2.5-7B
    agent on 15+ task types (20 episodes each, max_steps=30). At each step, execute
    all 3 modalities (fast-internal, deep-internal, deterministic) and record which
    leads to best eventual task score via hindsight labeling. Output: (state, observation,
    best_modality) triples for router SFT.

    '
  priority: P0
  gpu_budget_hours: 40
  deps: []
  notes: 'MVP covered 5 task types. Need to expand to 15+ for paper. Strong tasks
    (boil, melt, change-state) + medium (mix-paint) + weak (grow-plant) + new types.
    vLLM backend on both GPUs for speed. Parallelise across task types.

    '
  status: planned
- id: plan-002
  claim: C2
  description: 'Router SFT training. Fine-tune Qwen3-1.7B on counterfactual labels
    from plan-001. Cross-entropy loss, (history, observation) → {fast-internal, deep-internal,
    deterministic}. Train/val split by task type (leave-one-out or 80/20).

    '
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan-001
  notes: 'Follow ARES training pipeline. Single GPU sufficient. Hyperparams: lr=2e-5,
    batch=32, epochs=3, max_seq_len=2048.

    '
  status: planned
- id: plan-003
  claim: C1
  description: 'SimGate end-to-end evaluation on ScienceWorld. Run trained router
    + Qwen2.5-7B backbone on held-out episodes. Compare against: always-internal,
    always-deterministic, oracle-routing, random-routing, confidence-threshold heuristic.
    Report: continuous score (CogRouter protocol), success rate, catastrophic failure
    rate, simulator invocation ratio, total LLM tokens.

    '
  priority: P0
  gpu_budget_hours: 15
  deps:
  - plan-002
  notes: 'CogRouter (84.6) and ITP-R (62.58) cited from papers, not reproduced. Bootstrap
    90% CI on all comparisons. Per-task-type breakdown.

    '
  status: planned
- id: plan-004
  claim: C2
  description: 'Explicit vs implicit routing ablation. Same Qwen2.5-7B backbone. Implicit:
    backbone decides when to invoke simulator via tool-use prompt (no separate router).
    Explicit: SimGate router. Both trained on same counterfactual data. This is the
    core ablation for C2 — quantifies the value of explicit modular routing.

    '
  priority: P0
  gpu_budget_hours: 10
  deps:
  - plan-001
  notes: 'Implicit routing = add "You may invoke the simulator by outputting [SIMULATE]"
    to prompt. Train with same labels (SFT on backbone to output [SIMULATE] at oracle-labeled
    steps). Can run in parallel with plan-002 on second GPU.

    '
  status: planned
- id: plan-005
  claim:
  - C1
  - C2
  description: 'Per-task routing pattern analysis. From plan-003 outputs, analyze:
    (a) which task categories trigger deterministic routing most, (b) at which episode
    phases (early/mid/late) routing decisions concentrate, (c) router-as-diagnostic-probe
    — cluster deterministic-routing steps to identify systematic LLM failure modes
    (e.g., multi-step physical reasoning failures). Output: routing heatmap figure
    + failure mode taxonomy.

    '
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan-003
  notes: Analysis-only, minimal GPU. Main output is Figure 1 for the paper.
  status: planned
- id: plan-006
  claim: C2
  description: '2-way vs 3-way routing ablation. Compare {internal, deterministic}
    vs {fast-internal, deep-internal, deterministic}. Tests whether the fast/deep
    internal distinction adds value beyond binary routing.

    '
  priority: P1
  gpu_budget_hours: 8
  deps:
  - plan-002
  notes: 'If 2-way ≈ 3-way, simplifies the story (router just decides simulate-or-not).
    If 3-way > 2-way, supports nuanced compute allocation claim.

    '
  status: planned
- id: plan-007
  claim: C1
  description: 'Boil task rerun with v3 code. MVP boil data used old code (>= tie-break,
    death filter on all 3 modes). Rerun with clean v3 code for unified analysis.

    '
  priority: P1
  gpu_budget_hours: 3
  deps: []
  notes: Can run in parallel with plan-001 as first batch.
  status: planned
- id: plan-008
  claim: C2
  description: 'Router size ablation. Compare Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B
    as router. Tests sensitivity to router capacity.

    '
  priority: P1
  gpu_budget_hours: 12
  deps:
  - plan-001
  notes: 'Important for "lightweight" claim. If 1.5B matches 1.7B, strengthens "small
    router suffices". Low priority relative to core experiments.

    '
  status: planned
- id: plan-009
  claim: C1
  description: 'MATH track — code interpreter as deterministic oracle. 500 Level 4-5
    MATH problems. 3-way routing: fast-internal / deep-internal / code-interpreter.
    Demonstrates generalization beyond environment simulators.

    '
  priority: P2
  gpu_budget_hours: 20
  deps:
  - plan-002
  notes: 'Human Review Note suggested MATH as secondary track. Only if ScienceWorld
    experiments finish by Day 8. Could be strong differentiator but tight on time.

    '
  status: planned
- id: plan-010
  claim: C2
  description: 'Cross-task transfer within ScienceWorld. Train router on chemistry
    tasks only, evaluate on physics tasks (and vice versa). Tests whether routing
    patterns transfer across task domains.

    '
  priority: P2
  gpu_budget_hours: 5
  deps:
  - plan-002
  status: planned


## registry (completed experiments)

- exp_id: mvp-p0-forking
  name: ''
  status: DONE
  conclusion: success
  metrics:
    fork_success_rate: 1
    avg_latency_s: 1.67
    p50_latency_s: 1.53
    p95_latency_s: 2.37
    max_memory_mb: 20
    gate: PASS
- exp_id: mvp-p1-signal
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: mvp-p1-gpu1
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp-p1-gpu0
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    boil_20ep:
      internal_mean: -49.8
      det_mean: -19.7
      oracle_mean: -29.7
    note: 旧代码 (>= tie-break, 无 death filter), boil 20/20 完成, melt/change-state 未跑
- exp_id: mvp-p1-gpu1-vllm
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp-p1-gpu1-v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp-p1-gpu1-v3
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics: {}
- exp_id: mvp-p1-gpu0-vllm
  name: ''
  status: DONE
  conclusion: success
  metrics:
    melt:
      internal_mean: -54.7
      det_mean: -14.55
      oracle_mean: 2.15
      det_minus_internal: 40.15
      bootstrap_90ci:
      - 25
      - 60.15
    change_state:
      internal_mean: -54.7
      det_mean: -14.5
      oracle_mean: 0.45
      det_minus_internal: 40.2
      bootstrap_90ci:
      - 25
      - 60.15
    pooled:
      det_minus_internal: 40.17
      bootstrap_90ci:
      - 27.6
      - 52.77
    n_episodes_per_task: 20
    ci_lower_gt_0: true
    tasks_significant: 2/2

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
  "promptId": "a03e00ba-96bc-445a-80ea-051b9927dc2a",
  "type": "user",
  "uuid": "095d6e65-67cc-4244-a2a1-a3a9c1cd8df9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T15:37:17.457Z_

```json
{
  "parentUuid": "095d6e65-67cc-4244-a2a1-a3a9c1cd8df9",
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
  "uuid": "6d460a6a-3d24-433b-9403-96237bbc8aa6",
  "timestamp": "2026-05-13T15:37:17.457Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T15:37:17.457Z_

```json
{
  "parentUuid": "6d460a6a-3d24-433b-9403-96237bbc8aa6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "63208670-b513-4054-998b-c5926a6abd55",
  "timestamp": "2026-05-13T15:37:17.457Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心假设部分成立：death avoidance 机制复现但无 positive guidance 信号，selective > unconditional 一致但幅度较小，explicit > implicit 成立但差距不大，整体分数接近但未超过 CogRouter 核心假设：['A1 death a…",
  "leafUuid": "63208670-b513-4054-998b-c5926a6abd55",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define median-tier results for SimGate routing paper",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f"
}
```

---

### Tool call

_source line 8 · 2026-05-13T15:37:21.862Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WQhDn95w9GjuXzBURLhCj9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63208670-b513-4054-998b-c5926a6abd55",
  "isSidechain": false,
  "requestId": "req_011CazpJXistPTZ1GVaznnU1",
  "type": "assistant",
  "uuid": "a0bcee3f-4ba7-4e2c-972b-1c9fe4e283f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPAXAo7ejUZSLTako6fw1G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10400,
      "cache_read_input_tokens": 11841,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10400,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 79,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10400
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

### Tool result

_source line 9 · 2026-05-13T15:37:21.875Z_

<details><summary>↩ Tool result · `toolu_01WQhDn95w9GjuXzBURLhCj9`</summary>

```text
1	
2	## 输出风格
3	
4	- 回复简洁直接，不说废话
5	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
6	- 不要复述用户的问题
7	- 不要给未被要求的建议或补充说明
8	- 推理要彻底，但输出只保留结论和必要信息
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0bcee3f-4ba7-4e2c-972b-1c9fe4e283f3",
  "isSidechain": false,
  "promptId": "a03e00ba-96bc-445a-80ea-051b9927dc2a",
  "type": "user",
  "uuid": "a0dcfbfa-c18d-48a1-908a-878d052ded31",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "a0bcee3f-4ba7-4e2c-972b-1c9fe4e283f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T15:37:27.910Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PJ3Q1rg7K7hRSv35H1c7py`</summary>

```json
{
  "description": "Explore project structure",
  "subagent_type": "Explore",
  "prompt": "I need to understand the full project structure of /home/ubuntu/.agent-ml-research-idea_gen_0509_12. Please:\n1. List all files in the project root and key subdirectories\n2. Read the experiment_plan file if it exists as a standalone file\n3. Read any registry files\n4. Check for any existing predicted results or tier definitions\n5. Look for paper_framing.md\n\nFocus on finding any YAML/JSON config files, experiment plans, and results data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0dcfbfa-c18d-48a1-908a-878d052ded31",
  "isSidechain": false,
  "requestId": "req_011CazpJrrpSqkQg53haL64S",
  "type": "assistant",
  "uuid": "3e07f2f2-20c5-4bc3-bcca-35945671c192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3iKHKo91Gb6ghh2xTxytW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 22241,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 252,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 22241,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 252
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

### Tool result

_source line 11 · 2026-05-13T15:38:26.805Z_

<details><summary>↩ Tool result · `toolu_01PJ3Q1rg7K7hRSv35H1c7py`</summary>

````text
Perfect! I have gathered comprehensive information about the project. Let me compile the final report.

## Project Structure Overview

**Project Root**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12`

### Key Directory Structure:
```
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/
├── AGENTS.md                          (Agent activity summary)
├── workspace.yaml                     (Empty workspace config)
├── config/                            (Global configuration)
│   ├── approvals.yaml
│   ├── backend.yaml
│   ├── claude_sessions.json
│   ├── crons.yaml
│   ├── mcp_config*.json              (Multiple MCP configs for different agents)
│   └── projects/
├── state/                             (Pool state)
│   └── pool_state_last.json
├── global/                            (Global logs)
│   └── logs/workers/registry.json
├── idea_generator/                    (Ideas system)
│   └── ideas.yaml                     (All generated research ideas)
├── skills/                            (Skill definitions)
└── projects/
    └── simgate-modular-routing/       (Primary project)
```

---

## PRIMARY PROJECT: simgate-modular-routing

**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`

### Core Files

#### 1. **experiment_plan.yaml** (7.75 KB)
- **Type**: YAML experiment plan
- **Generated**: 2026-05-13 post-MVP
- **Updated**: 2026-05-13 with Reviewer W1-W5 revisions
- **Content**: Comprehensive 10-experiment plan split into P0 (must-do), P1 (important), and P2 (nice-to-have)
- **Key Structure**:
  - **P0 Experiments** (~72 GPU-hours total):
    - `plan-001a`: Mini signal detection (pre-screening) — 10h RTX 5090
    - `plan-001b`: Full counterfactual trajectory collection — 25h
    - `plan-002`: Router SFT training (Qwen3-1.7B) — 8h
    - `plan-003`: End-to-end evaluation on ScienceWorld — 15h
    - `plan-004`: Explicit vs implicit routing ablation — 12h
    - `plan-005`: Per-task routing pattern analysis — 2h
  - **P1 Experiments** (~25 GPU-hours):
    - `plan-006`: 2-way vs 3-way routing ablation
    - `plan-007`: Boil task rerun with v3 code
    - `plan-008`: Router size ablation
  - **P2 Experiments** (~25 GPU-hours):
    - `plan-009`: MATH track (code interpreter)
    - `plan-010`: Cross-task transfer
- **Critical Path**: 001a(10h) → 001b(25h) → 002(8h) → 003(15h) = ~60h sequential, ~2.5 days with dual GPUs
- **GPU Budget**: 122 GPU-hours total on RTX 5090 32GB

#### 2. **registry.yaml** (8.5 KB)
- **Type**: YAML experiment registry
- **Content**: Detailed experiment tracking for MVP and Phase 1 experiments
- **Key Experiments**:
  - `mvp-p0-forking`: DONE — State forking validation (100% success, p95=2.37s latency)
  - `mvp-p1-gpu0`: DONE — boil task, internal=-49.8, det=-19.7, oracle=-29.7 (old code)
  - `mvp-p1-gpu0-vllm`: DONE ✓ — melt + change-state tasks
    - melt: det-internal = +40.15, CI [25, 60.15]
    - change-state: det-internal = +40.2, CI [25, 60.15]
  - `mvp-p1-gpu1-v3`: ANALYZING — mix-paint + grow-plant (still running)
- **Metrics Tracked**: fork success rate, latency, task scores, bootstrap CIs

#### 3. **paper_framing.md** (6.5 KB) ✓ **FOUND**
- **Type**: Markdown paper strategy document
- **Content**:
  - **Target Venue**: EMNLP 2026 ARR short paper (4 pages + refs), DDL May 25, 2026 (12 days)
  - **Core Insight**: Recast "when to simulate" problem as safety-aware routing. LLM agents hallucinate on rule-governed environments; deterministic external computation eliminates failures at CPU-only cost. MVP evidence: death avoidance is primary mechanism (+30-40 points from preventing -100 penalties).
  - **Core Claims (2 for short paper)**:
    - **C1**: Selective routing to deterministic computation significantly outperforms pure LLM reasoning, with primary mechanism = catastrophic failure prevention
    - **C2**: Lightweight explicit router (Qwen3-1.7B, SFT) achieves effective per-step routing that is interpretable, architecturally decoupled, and consistent across task categories
  - **Story Spine**: Safety-aware routing framing, NOT performance-boosting framing
  - **Paper Structure** (4-page template):
    - Abstract: 0.2 pages
    - Introduction: 0.8 pages (problem + gap + 2 claims)
    - Method: 1.0 pages (3-component framework + counterfactual pipeline)
    - Experiments: 1.5 pages (main table + ablations + routing analysis)
    - Conclusion: 0.3 pages
    - References: ~0.5 pages
  - **Reviewer Concerns & Mitigations** (5 anticipated objections)

#### 4. **dream_registry.yaml** (0.9 KB)
- **Type**: YAML dream/simulation registry
- **Content**: Single active dream session
  - `dream_20260513T153257`: Status = "imagining", started 2026-05-13T15:32:57
  - Focus: "Short paper (4 pages). Core contribution: safety-aware routing to deterministic computation. MVP showed death avoidance as primary mechanism (+30-40 points)."
  - Review mode: full, review_visible=true, writing_visible=true

#### 5. **decisions.yaml** (2.8 KB)
- **Type**: YAML decision log
- **Content**: 5 numbered decisions (D001-D005) tracking major research pivots
  - **D001** (2026-05-13 04:25): MVP plan: ScienceWorld signal detection — verify deterministic > LLM
  - **D002** (2026-05-13 04:28): Phase 0 + Phase 1 two-stage structure (forking validation + signal detection)
  - **D003** (2026-05-13 07:43): Fix tie-break logic (>= → >) and death-filter method
  - **D004** (2026-05-13 08:13): Primary metric = always-deterministic vs always-internal (not oracle)
  - **D005** (2026-05-13 15:25): MVP Phase 1 PASS — det > internal on ≥2/5 task types, oracle > det confirms selective routing value
  - Each decision includes rationale, related experiments, and dependencies

#### 6. **memory.md** (1.2 KB)
- **Type**: Markdown project memory/notes
- **Content**: MVP Phase 1 analysis results from 2026-05-13
  - Task performance table: melt/change-state show death avoidance as primary signal
  - Internal strategy fails 55% of time (-100 penalties), det fails ~15%
  - Oracle is low (melt 2.15, change-state 0.45), indicating selective routing gain is from failure prevention
  - 4/5 tasks significant (threshold 2/5) — PASS

#### 7. **ROADMAP.md** (3.8 KB)
- **Type**: Markdown research roadmap/dashboard
- **Content**: Updated 2026-05-13, incorporating Reviewer W1-W5 revisions
  - Current phase: Research Phase — MVP PASS (D005), Dream imagining
  - Progress: MVP done, paper_framing done, experiment_plan v2 done, Dream running
  - Near-term tasks: Dream completion → plan-001a approval → 001b start
  - GPU budget: ~122h RTX 5090 dual-card (P0+P1+P2)
  - Timeline: 12 days, critical path = 2.5 days

#### 8. **report.md** (0.7 KB)
- **Type**: Markdown project report
- **Content**: Brief current status (likely auto-generated)

### Execution & Configuration Files

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.lock`
- Lock file for registry.yaml (0 bytes)

**File**: `dream_registry.lock`
- Lock file (0 bytes)

**File**: `decisions.lock`
- Lock file (0 bytes)

**File**: `study_status.lock`
- Lock file (0 bytes)

### Code & Results Directories

**Directory**: `src/` (4 files)
- `phase1_signal.py` — Main Phase 1 signal detection script
- `phase0_validate_forking.py` — State forking validation
- `llm_agent.py` — LLM ReAct agent wrapper
- `run_all.sh` — Parallel job runner
- `scienceworld_utils.py` — ScienceWorld utility functions
- `analysis.py` — Results analysis script

**Directory**: `checkpoints/` (contains intermediate saves)

**Directory**: `logs/workers/` (40+ worker result JSON files)
- Tracked workers for infra, code, exp, analysis, research, diagnose tasks
- Each worker has `{worker_id}_result.json` with execution logs

**Directory**: `artifacts/` (project outputs)

**Directory**: `docs/`
- `IDEA_BRIEF.md` — Original idea brief (100+ KB)

### Global Registry & Config

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_worker_*.json`
- MCP configuration for 5 different worker instances
- Maps worker IDs to tool capabilities (ssh_execute, ssh_read_only, etc.)

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/workers/registry.json` (large)
- Global worker registry tracking all agent workers across all projects
- 40+ worker entries with full execution context, parameters, logs

---

## Ideas Registry

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/idea_generator/ideas.yaml` (2700+ lines)

- **Single approved idea**: `idea_010` (SimGate)
  - **Status**: APPROVED
  - **Created/Approved**: 2026-05-13
  - **Source**: foreign:be-idea-gen-0509-7
  - **Level**: top-tier
  - **Target Venues**: EMNLP 2026 (ARR short paper, May 25 deadline)
  - **Review Scores**: clarity=4/5, feasibility=4/5, impact=4/5, novelty=4/5
  - **GPU Estimate**: 170-210 H100-hours (human-in-loop mode within budget)
  - **Key References**: 20+ papers including ITP-R, CogRouter, ReTool, AgentMath, Select-then-Solve, EPO, EMPO2, AutoTool
  - **Human Review Note**: 24 optimization suggestions provided (Chinese), covering abstract framing, claims narrowing, method detail expansion, evaluation structure, ablation design, etc.

---

## Key Project State Summary

**As of 2026-05-13 15:37 UTC**:

| Item | Status | Details |
|------|--------|---------|
| **MVP** | PASS ✓ | det > internal on 4/5 task types (melt, change-state, mix-paint, boil); grow-plant=0 (control) |
| **Paper Framing** | DONE | Safety-aware routing narrative, 2 core claims, 4-page short paper structure |
| **Experiment Plan** | V2 FINALIZED | 10 experiments, 122h GPU budget, reviewed by W1-W5 |
| **Dream Simulation** | RUNNING | Started 15:32:57, full review mode |
| **Primary Signal** | CONFIRMED | Death avoidance (+30-40 points from preventing -100 penalties), oracle > det (+10-17 points) proves selective routing value |
| **Critical Path** | ~60h sequential | 001a(10h) → 001b(25h) → 002(8h) → 003(15h) on dual RTX 5090, ~2.5 days |
| **Submission Deadline** | 12 days | ARR May 25, 2026 |

---

## Key Findings from MVP

1. **Deterministic vs Internal Performance Gap**: 
   - melt: +40.15 points (CI [25.0, 60.15])
   - change-state: +40.2 points (CI [25.0, 60.15])
   - mix-paint: +35.5 points (expected pass)
   - boil: +30.1 points (old code, will rerun with v3)
   - grow-plant: 0.0 (expected control)

2. **Mechanism**: Death avoidance (preventing -100 failure penalties) is primary signal, not positive guidance

3. **Selective Routing Signal**: oracle > deterministic by +10-17 points on 3/5 tasks, confirming value of selective routing over unconditional simulation

4. **Next Steps**: Proceed to plan-001a (signal pre-screening) + plan-007 (boil rerun with v3 code) on dual GPU, then plan-001b (full trajectory collection) for router SFT training
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "3e07f2f2-20c5-4bc3-bcca-35945671c192",
  "isSidechain": false,
  "promptId": "a03e00ba-96bc-445a-80ea-051b9927dc2a",
  "type": "user",
  "uuid": "0240bcc5-5de7-46a1-adb5-bd65ac114ccf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the full project structure of /home/ubuntu/.agent-ml-research-idea_gen_0509_12. Please:\n1. List all files in the project root and key subdirectories\n2. Read the experiment_plan file if it exists as a standalone file\n3. Read any registry files\n4. Check for any existing predicted results or tier definitions\n5. Look for paper_framing.md\n\nFocus on finding any YAML/JSON config files, experiment plans, and results data.",
    "agentId": "a3d5858b7bf8b3821",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have gathered comprehensive information about the project. Let me compile the final report.\n\n## Project Structure Overview\n\n**Project Root**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12`\n\n### Key Directory Structure:\n```\n/home/ubuntu/.agent-ml-research-idea_gen_0509_12/\n├── AGENTS.md                          (Agent activity summary)\n├── workspace.yaml                     (Empty workspace config)\n├── config/                            (Global configuration)\n│   ├── approvals.yaml\n│   ├── backend.yaml\n│   ├── claude_sessions.json\n│   ├── crons.yaml\n│   ├── mcp_config*.json              (Multiple MCP configs for different agents)\n│   └── projects/\n├── state/                             (Pool state)\n│   └── pool_state_last.json\n├── global/                            (Global logs)\n│   └── logs/workers/registry.json\n├── idea_generator/                    (Ideas system)\n│   └── ideas.yaml                     (All generated research ideas)\n├── skills/                            (Skill definitions)\n└── projects/\n    └── simgate-modular-routing/       (Primary project)\n```\n\n---\n\n## PRIMARY PROJECT: simgate-modular-routing\n\n**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`\n\n### Core Files\n\n#### 1. **experiment_plan.yaml** (7.75 KB)\n- **Type**: YAML experiment plan\n- **Generated**: 2026-05-13 post-MVP\n- **Updated**: 2026-05-13 with Reviewer W1-W5 revisions\n- **Content**: Comprehensive 10-experiment plan split into P0 (must-do), P1 (important), and P2 (nice-to-have)\n- **Key Structure**:\n  - **P0 Experiments** (~72 GPU-hours total):\n    - `plan-001a`: Mini signal detection (pre-screening) — 10h RTX 5090\n    - `plan-001b`: Full counterfactual trajectory collection — 25h\n    - `plan-002`: Router SFT training (Qwen3-1.7B) — 8h\n    - `plan-003`: End-to-end evaluation on ScienceWorld — 15h\n    - `plan-004`: Explicit vs implicit routing ablation — 12h\n    - `plan-005`: Per-task routing pattern analysis — 2h\n  - **P1 Experiments** (~25 GPU-hours):\n    - `plan-006`: 2-way vs 3-way routing ablation\n    - `plan-007`: Boil task rerun with v3 code\n    - `plan-008`: Router size ablation\n  - **P2 Experiments** (~25 GPU-hours):\n    - `plan-009`: MATH track (code interpreter)\n    - `plan-010`: Cross-task transfer\n- **Critical Path**: 001a(10h) → 001b(25h) → 002(8h) → 003(15h) = ~60h sequential, ~2.5 days with dual GPUs\n- **GPU Budget**: 122 GPU-hours total on RTX 5090 32GB\n\n#### 2. **registry.yaml** (8.5 KB)\n- **Type**: YAML experiment registry\n- **Content**: Detailed experiment tracking for MVP and Phase 1 experiments\n- **Key Experiments**:\n  - `mvp-p0-forking`: DONE — State forking validation (100% success, p95=2.37s latency)\n  - `mvp-p1-gpu0`: DONE — boil task, internal=-49.8, det=-19.7, oracle=-29.7 (old code)\n  - `mvp-p1-gpu0-vllm`: DONE ✓ — melt + change-state tasks\n    - melt: det-internal = +40.15, CI [25, 60.15]\n    - change-state: det-internal = +40.2, CI [25, 60.15]\n  - `mvp-p1-gpu1-v3`: ANALYZING — mix-paint + grow-plant (still running)\n- **Metrics Tracked**: fork success rate, latency, task scores, bootstrap CIs\n\n#### 3. **paper_framing.md** (6.5 KB) ✓ **FOUND**\n- **Type**: Markdown paper strategy document\n- **Content**:\n  - **Target Venue**: EMNLP 2026 ARR short paper (4 pages + refs), DDL May 25, 2026 (12 days)\n  - **Core Insight**: Recast \"when to simulate\" problem as safety-aware routing. LLM agents hallucinate on rule-governed environments; deterministic external computation eliminates failures at CPU-only cost. MVP evidence: death avoidance is primary mechanism (+30-40 points from preventing -100 penalties).\n  - **Core Claims (2 for short paper)**:\n    - **C1**: Selective routing to deterministic computation significantly outperforms pure LLM reasoning, with primary mechanism = catastrophic failure prevention\n    - **C2**: Lightweight explicit router (Qwen3-1.7B, SFT) achieves effective per-step routing that is interpretable, architecturally decoupled, and consistent across task categories\n  - **Story Spine**: Safety-aware routing framing, NOT performance-boosting framing\n  - **Paper Structure** (4-page template):\n    - Abstract: 0.2 pages\n    - Introduction: 0.8 pages (problem + gap + 2 claims)\n    - Method: 1.0 pages (3-component framework + counterfactual pipeline)\n    - Experiments: 1.5 pages (main table + ablations + routing analysis)\n    - Conclusion: 0.3 pages\n    - References: ~0.5 pages\n  - **Reviewer Concerns & Mitigations** (5 anticipated objections)\n\n#### 4. **dream_registry.yaml** (0.9 KB)\n- **Type**: YAML dream/simulation registry\n- **Content**: Single active dream session\n  - `dream_20260513T153257`: Status = \"imagining\", started 2026-05-13T15:32:57\n  - Focus: \"Short paper (4 pages). Core contribution: safety-aware routing to deterministic computation. MVP showed death avoidance as primary mechanism (+30-40 points).\"\n  - Review mode: full, review_visible=true, writing_visible=true\n\n#### 5. **decisions.yaml** (2.8 KB)\n- **Type**: YAML decision log\n- **Content**: 5 numbered decisions (D001-D005) tracking major research pivots\n  - **D001** (2026-05-13 04:25): MVP plan: ScienceWorld signal detection — verify deterministic > LLM\n  - **D002** (2026-05-13 04:28): Phase 0 + Phase 1 two-stage structure (forking validation + signal detection)\n  - **D003** (2026-05-13 07:43): Fix tie-break logic (>= → >) and death-filter method\n  - **D004** (2026-05-13 08:13): Primary metric = always-deterministic vs always-internal (not oracle)\n  - **D005** (2026-05-13 15:25): MVP Phase 1 PASS — det > internal on ≥2/5 task types, oracle > det confirms selective routing value\n  - Each decision includes rationale, related experiments, and dependencies\n\n#### 6. **memory.md** (1.2 KB)\n- **Type**: Markdown project memory/notes\n- **Content**: MVP Phase 1 analysis results from 2026-05-13\n  - Task performance table: melt/change-state show death avoidance as primary signal\n  - Internal strategy fails 55% of time (-100 penalties), det fails ~15%\n  - Oracle is low (melt 2.15, change-state 0.45), indicating selective routing gain is from failure prevention\n  - 4/5 tasks significant (threshold 2/5) — PASS\n\n#### 7. **ROADMAP.md** (3.8 KB)\n- **Type**: Markdown research roadmap/dashboard\n- **Content**: Updated 2026-05-13, incorporating Reviewer W1-W5 revisions\n  - Current phase: Research Phase — MVP PASS (D005), Dream imagining\n  - Progress: MVP done, paper_framing done, experiment_plan v2 done, Dream running\n  - Near-term tasks: Dream completion → plan-001a approval → 001b start\n  - GPU budget: ~122h RTX 5090 dual-card (P0+P1+P2)\n  - Timeline: 12 days, critical path = 2.5 days\n\n#### 8. **report.md** (0.7 KB)\n- **Type**: Markdown project report\n- **Content**: Brief current status (likely auto-generated)\n\n### Execution & Configuration Files\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.lock`\n- Lock file for registry.yaml (0 bytes)\n\n**File**: `dream_registry.lock`\n- Lock file (0 bytes)\n\n**File**: `decisions.lock`\n- Lock file (0 bytes)\n\n**File**: `study_status.lock`\n- Lock file (0 bytes)\n\n### Code & Results Directories\n\n**Directory**: `src/` (4 files)\n- `phase1_signal.py` — Main Phase 1 signal detection script\n- `phase0_validate_forking.py` — State forking validation\n- `llm_agent.py` — LLM ReAct agent wrapper\n- `run_all.sh` — Parallel job runner\n- `scienceworld_utils.py` — ScienceWorld utility functions\n- `analysis.py` — Results analysis script\n\n**Directory**: `checkpoints/` (contains intermediate saves)\n\n**Directory**: `logs/workers/` (40+ worker result JSON files)\n- Tracked workers for infra, code, exp, analysis, research, diagnose tasks\n- Each worker has `{worker_id}_result.json` with execution logs\n\n**Directory**: `artifacts/` (project outputs)\n\n**Directory**: `docs/`\n- `IDEA_BRIEF.md` — Original idea brief (100+ KB)\n\n### Global Registry & Config\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_worker_*.json`\n- MCP configuration for 5 different worker instances\n- Maps worker IDs to tool capabilities (ssh_execute, ssh_read_only, etc.)\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/workers/registry.json` (large)\n- Global worker registry tracking all agent workers across all projects\n- 40+ worker entries with full execution context, parameters, logs\n\n---\n\n## Ideas Registry\n\n**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/idea_generator/ideas.yaml` (2700+ lines)\n\n- **Single approved idea**: `idea_010` (SimGate)\n  - **Status**: APPROVED\n  - **Created/Approved**: 2026-05-13\n  - **Source**: foreign:be-idea-gen-0509-7\n  - **Level**: top-tier\n  - **Target Venues**: EMNLP 2026 (ARR short paper, May 25 deadline)\n  - **Review Scores**: clarity=4/5, feasibility=4/5, impact=4/5, novelty=4/5\n  - **GPU Estimate**: 170-210 H100-hours (human-in-loop mode within budget)\n  - **Key References**: 20+ papers including ITP-R, CogRouter, ReTool, AgentMath, Select-then-Solve, EPO, EMPO2, AutoTool\n  - **Human Review Note**: 24 optimization suggestions provided (Chinese), covering abstract framing, claims narrowing, method detail expansion, evaluation structure, ablation design, etc.\n\n---\n\n## Key Project State Summary\n\n**As of 2026-05-13 15:37 UTC**:\n\n| Item | Status | Details |\n|------|--------|---------|\n| **MVP** | PASS ✓ | det > internal on 4/5 task types (melt, change-state, mix-paint, boil); grow-plant=0 (control) |\n| **Paper Framing** | DONE | Safety-aware routing narrative, 2 core claims, 4-page short paper structure |\n| **Experiment Plan** | V2 FINALIZED | 10 experiments, 122h GPU budget, reviewed by W1-W5 |\n| **Dream Simulation** | RUNNING | Started 15:32:57, full review mode |\n| **Primary Signal** | CONFIRMED | Death avoidance (+30-40 points from preventing -100 penalties), oracle > det (+10-17 points) proves selective routing value |\n| **Critical Path** | ~60h sequential | 001a(10h) → 001b(25h) → 002(8h) → 003(15h) on dual RTX 5090, ~2.5 days |\n| **Submission Deadline** | 12 days | ARR May 25, 2026 |\n\n---\n\n## Key Findings from MVP\n\n1. **Deterministic vs Internal Performance Gap**: \n   - melt: +40.15 points (CI [25.0, 60.15])\n   - change-state: +40.2 points (CI [25.0, 60.15])\n   - mix-paint: +35.5 points (expected pass)\n   - boil: +30.1 points (old code, will rerun with v3)\n   - grow-plant: 0.0 (expected control)\n\n2. **Mechanism**: Death avoidance (preventing -100 failure penalties) is primary signal, not positive guidance\n\n3. **Selective Routing Signal**: oracle > deterministic by +10-17 points on 3/5 tasks, confirming value of selective routing over unconditional simulation\n\n4. **Next Steps**: Proceed to plan-001a (signal pre-screening) + plan-007 (boil rerun with v3 code) on dual GPU, then plan-001b (full trajectory collection) for router SFT training"
      }
    ],
    "totalDurationMs": 58890,
    "totalTokens": 82311,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6622,
      "cache_read_input_tokens": 72149,
      "output_tokens": 3534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6622
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 3534,
          "cache_read_input_tokens": 72149,
          "cache_creation_input_tokens": 6622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6622,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 11,
      "searchCount": 0,
      "bashCount": 9,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "3e07f2f2-20c5-4bc3-bcca-35945671c192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 12 · 2026-05-13T15:38:29.693Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tj8zd6KKTD8mRam9jou9AF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0240bcc5-5de7-46a1-adb5-bd65ac114ccf",
  "isSidechain": false,
  "requestId": "req_011CazpPe7VaFdk6bdxYiTdc",
  "type": "assistant",
  "uuid": "fc0d6e62-b791-4e15-a980-81a3019fe71b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzUAdSwWoWH17TZUvQQUhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3745,
      "cache_read_input_tokens": 22493,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 22493,
          "cache_creation_input_tokens": 3745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3745
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

### Tool result

_source line 13 · 2026-05-13T15:38:29.706Z_

<details><summary>↩ Tool result · `toolu_01Tj8zd6KKTD8mRam9jou9AF`</summary>

```text
1	# SimGate Experiment Plan
2	# Generated: 2026-05-13 post-MVP
3	# Updated: 2026-05-13 Reviewer W1-W5 incorporated
4	# Claims reference: paper_framing.md C1, C2
5	
6	experiments:
7	  # === P0: Must-do for paper submission ===
8	
9	  - id: plan-001a
10	    claim: [C1]
11	    description: >
12	      Mini signal detection (pre-screening). Run 5 episodes per candidate task type
13	      (2-way: internal + deterministic only) to identify which tasks show det > internal signal.
14	      Screen ~20 ScienceWorld task types, keep those with positive effect direction.
15	      ~30min per task type, ~10h total for 20 types on dual GPU.
16	    priority: P0
17	    gpu_budget_hours: 10
18	    deps: []
19	    notes: >
20	      Reviewer W3: avoid wasting GPU on no-signal tasks like grow-plant.
21	      MVP task types (boil, melt, change-state, mix-paint) auto-pass.
22	      grow-plant confirmed no-signal (control). Target: identify 10-15 task types with signal.
23	
24	  - id: plan-001b
25	    claim: [C1, C2]
26	    description: >
27	      Full counterfactual trajectory collection on signal-positive task types from plan-001a.
28	      2-way collection: internal + deterministic (per Reviewer W2).
29	      20 episodes each, max_steps=30. At each step, execute both modalities
30	      and record which leads to best eventual task score via hindsight labeling.
31	      Output: (state, observation, best_modality) triples for router SFT.
32	    priority: P0
33	    gpu_budget_hours: 25
34	    deps: [plan-001a]
35	    notes: >
36	      Reviewer W2: collect 2-way first, consistent with MVP. Skip fast/deep-internal
37	      distinction until plan-006 confirms 3-way adds value.
38	      GPU savings: ~33% vs original 3-way plan (25h vs 40h).
39	      vLLM backend on both GPUs for speed.
40	
41	  - id: plan-002
42	    claim: C2
43	    description: >
44	      Router SFT training. Fine-tune Qwen3-1.7B on counterfactual labels from plan-001b.
45	      Cross-entropy loss, (history, observation) → {internal, deterministic}.
46	      Train/val split by task type (leave-one-out or 80/20).
47	    priority: P0
48	    gpu_budget_hours: 8
49	    deps: [plan-001b]
50	    notes: >
51	      Follow ARES training pipeline. Single GPU sufficient.
52	      Hyperparams: lr=2e-5, batch=32, epochs=3, max_seq_len=2048.
53	      2-way classification (not 3-way) per W2 decision.
54	
55	  - id: plan-003
56	    claim: C1
57	    description: >
58	      SimGate end-to-end evaluation on ScienceWorld.
59	      Run trained router + Qwen2.5-7B backbone on held-out episodes.
60	      Compare against: always-internal, always-deterministic, oracle-routing,
61	      random-routing, confidence-threshold heuristic.
62	      Report: continuous score (CogRouter protocol), success rate, catastrophic failure rate,
63	      simulator invocation ratio, total LLM tokens.
64	      KEY: This confirms/denies C1's "selective > unconditional" sub-claim (Reviewer W1).
65	    priority: P0
66	    gpu_budget_hours: 15
67	    deps: [plan-002]
68	    notes: >
69	      CogRouter (84.6) and ITP-R (62.58) cited from papers, not reproduced.
70	      Bootstrap 90% CI on all comparisons. Per-task-type breakdown.
71	      If trained router ≤ always-det, C1 downgrades per paper_framing.md note.
72	
73	  - id: plan-004
74	    claim: C2
75	    description: >
76	      Explicit vs implicit routing ablation (parameter-controlled).
77	      Three conditions:
78	      (a) 1.7B explicit router (SimGate) — Qwen3-1.7B, separate module
79	      (b) 1.7B implicit router — Qwen3-1.7B SFT'd to output [SIMULATE] token inline
80	      (c) 7B implicit routing — Qwen2.5-7B backbone decides via tool-use prompt
81	      All trained on same counterfactual data from plan-001b.
82	      Condition (b) is the parameter-matched control (Reviewer W4).
83	    priority: P0
84	    gpu_budget_hours: 12
85	    deps: [plan-001b]
86	    notes: >
87	      Reviewer W4: 7B implicit vs 1.7B explicit confounds architecture with capacity.
88	      Adding 1.7B implicit isolates explicit vs implicit architectural effect.
89	      Can run in parallel with plan-002 on second GPU.
90	
91	  - id: plan-005
92	    claim: [C1, C2]
93	    description: >
94	      Per-task routing pattern analysis.
95	      From plan-003 outputs, analyze: (a) which task categories trigger deterministic routing most,
96	      (b) at which episode phases (early/mid/late) routing decisions concentrate,
97	      (c) router-as-diagnostic-probe — cluster deterministic-routing steps to identify
98	      systematic LLM failure modes (e.g., multi-step physical reasoning failures).
99	      Output: routing heatmap figure + failure mode taxonomy.
100	    priority: P0
101	    gpu_budget_hours: 2
102	    deps: [plan-003]
103	    notes: Analysis-only, minimal GPU. Main output is Figure 1 for the paper.
104	
105	  # === P1: Important, do if time permits ===
106	
107	  - id: plan-006
108	    claim: C2
109	    description: >
110	      2-way vs 3-way routing ablation.
111	      Supplement plan-001b data with deep-internal modality on subset of tasks.
112	      Compare {internal, deterministic} vs {fast-internal, deep-internal, deterministic}.
113	      Tests whether the fast/deep internal distinction adds value beyond binary routing.
114	    priority: P1
115	    gpu_budget_hours: 10
116	    deps: [plan-002]
117	    notes: >
118	      If 3-way > 2-way, retrain router as 3-way and update paper.
119	      If 2-way ≈ 3-way, simplifies the story (binary routing suffices).
120	      Requires supplemental trajectory data for deep-internal (~5h additional collection).
121	
122	  - id: plan-007
123	    claim: C1
124	    description: >
125	      Boil task rerun with v3 code.
126	      MVP boil data used old code (>= tie-break, death filter on all 3 modes).
127	      Rerun with clean v3 code for unified analysis.
128	    priority: P1
129	    gpu_budget_hours: 3
130	    deps: []
131	    notes: Can run in parallel with plan-001a as first batch.
132	
133	  - id: plan-008
134	    claim: C2
135	    description: >
136	      Router size ablation. Compare Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B as router.
137	      Tests sensitivity to router capacity.
138	    priority: P1
139	    gpu_budget_hours: 12
140	    deps: [plan-001b]
141	    notes: >
142	      Important for "lightweight" claim. If 1.5B matches 1.7B, strengthens "small router suffices".
143	      Low priority relative to core experiments.
144	
145	  # === P2: Nice to have / Future work material ===
146	
147	  - id: plan-009
148	    claim: C1
149	    description: >
150	      MATH track — code interpreter as deterministic oracle.
151	      500 Level 4-5 MATH problems. 2-way routing: internal / code-interpreter.
152	      Demonstrates generalization beyond environment simulators.
153	    priority: P2
154	    gpu_budget_hours: 20
155	    deps: [plan-002]
156	    notes: >
157	      Human Review Note suggested MATH as secondary track.
158	      Only if ScienceWorld experiments finish by Day 8.
159	
160	  - id: plan-010
161	    claim: C2
162	    description: >
163	      Cross-task transfer within ScienceWorld.
164	      Train router on chemistry tasks only, evaluate on physics tasks (and vice versa).
165	      Tests whether routing patterns transfer across task domains.
166	    priority: P2
167	    gpu_budget_hours: 5
168	    deps: [plan-002]
169	
170	# === Summary (post-Reviewer revision) ===
171	# P0 total: ~72 GPU-hours (plan-001a 10h + plan-001b 25h + plan-002 8h + plan-003 15h + plan-004 12h + plan-005 2h)
172	# P1 total: ~25 GPU-hours (plan-006 10h + plan-007 3h + plan-008 12h)
173	# P2 total: ~25 GPU-hours (plan-009 20h + plan-010 5h)
174	# Grand total: ~122 GPU-hours
175	# All estimates in RTX 5090 32GB wall-clock hours (Reviewer W5)
176	#
177	# Critical path: plan-001a (10h) → plan-001b (25h) → plan-002 (8h) → plan-003 (15h) → plan-005 (2h)
178	# = ~60h sequential, ~2.5 days with 2 GPUs running in parallel
179	# plan-004 runs parallel with plan-002/003 on second GPU
180	# plan-007 runs parallel with plan-001a
181	#
182	# Key changes from v1:
183	# - plan-001 split into 001a (pre-screening) + 001b (full collection) per Reviewer W3
184	# - 2-way collection first (not 3-way) per Reviewer W2, saves ~33% GPU time
185	# - plan-004 adds 1.7B implicit control per Reviewer W4
186	# - GPU budget unit: RTX 5090 32GB hours (not H100) per Reviewer W5
187	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc0d6e62-b791-4e15-a980-81a3019fe71b",
  "isSidechain": false,
  "promptId": "a03e00ba-96bc-445a-80ea-051b9927dc2a",
  "type": "user",
  "uuid": "686caa17-b188-43fa-88f7-5ff2d736bc29",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/experiment_plan.yaml",
      "content": "# SimGate Experiment Plan\n# Generated: 2026-05-13 post-MVP\n# Updated: 2026-05-13 Reviewer W1-W5 incorporated\n# Claims reference: paper_framing.md C1, C2\n\nexperiments:\n  # === P0: Must-do for paper submission ===\n\n  - id: plan-001a\n    claim: [C1]\n    description: >\n      Mini signal detection (pre-screening). Run 5 episodes per candidate task type\n      (2-way: internal + deterministic only) to identify which tasks show det > internal signal.\n      Screen ~20 ScienceWorld task types, keep those with positive effect direction.\n      ~30min per task type, ~10h total for 20 types on dual GPU.\n    priority: P0\n    gpu_budget_hours: 10\n    deps: []\n    notes: >\n      Reviewer W3: avoid wasting GPU on no-signal tasks like grow-plant.\n      MVP task types (boil, melt, change-state, mix-paint) auto-pass.\n      grow-plant confirmed no-signal (control). Target: identify 10-15 task types with signal.\n\n  - id: plan-001b\n    claim: [C1, C2]\n    description: >\n      Full counterfactual trajectory collection on signal-positive task types from plan-001a.\n      2-way collection: internal + deterministic (per Reviewer W2).\n      20 episodes each, max_steps=30. At each step, execute both modalities\n      and record which leads to best eventual task score via hindsight labeling.\n      Output: (state, observation, best_modality) triples for router SFT.\n    priority: P0\n    gpu_budget_hours: 25\n    deps: [plan-001a]\n    notes: >\n      Reviewer W2: collect 2-way first, consistent with MVP. Skip fast/deep-internal\n      distinction until plan-006 confirms 3-way adds value.\n      GPU savings: ~33% vs original 3-way plan (25h vs 40h).\n      vLLM backend on both GPUs for speed.\n\n  - id: plan-002\n    claim: C2\n    description: >\n      Router SFT training. Fine-tune Qwen3-1.7B on counterfactual labels from plan-001b.\n      Cross-entropy loss, (history, observation) → {internal, deterministic}.\n      Train/val split by task type (leave-one-out or 80/20).\n    priority: P0\n    gpu_budget_hours: 8\n    deps: [plan-001b]\n    notes: >\n      Follow ARES training pipeline. Single GPU sufficient.\n      Hyperparams: lr=2e-5, batch=32, epochs=3, max_seq_len=2048.\n      2-way classification (not 3-way) per W2 decision.\n\n  - id: plan-003\n    claim: C1\n    description: >\n      SimGate end-to-end evaluation on ScienceWorld.\n      Run trained router + Qwen2.5-7B backbone on held-out episodes.\n      Compare against: always-internal, always-deterministic, oracle-routing,\n      random-routing, confidence-threshold heuristic.\n      Report: continuous score (CogRouter protocol), success rate, catastrophic failure rate,\n      simulator invocation ratio, total LLM tokens.\n      KEY: This confirms/denies C1's \"selective > unconditional\" sub-claim (Reviewer W1).\n    priority: P0\n    gpu_budget_hours: 15\n    deps: [plan-002]\n    notes: >\n      CogRouter (84.6) and ITP-R (62.58) cited from papers, not reproduced.\n      Bootstrap 90% CI on all comparisons. Per-task-type breakdown.\n      If trained router ≤ always-det, C1 downgrades per paper_framing.md note.\n\n  - id: plan-004\n    claim: C2\n    description: >\n      Explicit vs implicit routing ablation (parameter-controlled).\n      Three conditions:\n      (a) 1.7B explicit router (SimGate) — Qwen3-1.7B, separate module\n      (b) 1.7B implicit router — Qwen3-1.7B SFT'd to output [SIMULATE] token inline\n      (c) 7B implicit routing — Qwen2.5-7B backbone decides via tool-use prompt\n      All trained on same counterfactual data from plan-001b.\n      Condition (b) is the parameter-matched control (Reviewer W4).\n    priority: P0\n    gpu_budget_hours: 12\n    deps: [plan-001b]\n    notes: >\n      Reviewer W4: 7B implicit vs 1.7B explicit confounds architecture with capacity.\n      Adding 1.7B implicit isolates explicit vs implicit architectural effect.\n      Can run in parallel with plan-002 on second GPU.\n\n  - id: plan-005\n    claim: [C1, C2]\n    description: >\n      Per-task routing pattern analysis.\n      From plan-003 outputs, analyze: (a) which task categories trigger deterministic routing most,\n      (b) at which episode phases (early/mid/late) routing decisions concentrate,\n      (c) router-as-diagnostic-probe — cluster deterministic-routing steps to identify\n      systematic LLM failure modes (e.g., multi-step physical reasoning failures).\n      Output: routing heatmap figure + failure mode taxonomy.\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [plan-003]\n    notes: Analysis-only, minimal GPU. Main output is Figure 1 for the paper.\n\n  # === P1: Important, do if time permits ===\n\n  - id: plan-006\n    claim: C2\n    description: >\n      2-way vs 3-way routing ablation.\n      Supplement plan-001b data with deep-internal modality on subset of tasks.\n      Compare {internal, deterministic} vs {fast-internal, deep-internal, deterministic}.\n      Tests whether the fast/deep internal distinction adds value beyond binary routing.\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan-002]\n    notes: >\n      If 3-way > 2-way, retrain router as 3-way and update paper.\n      If 2-way ≈ 3-way, simplifies the story (binary routing suffices).\n      Requires supplemental trajectory data for deep-internal (~5h additional collection).\n\n  - id: plan-007\n    claim: C1\n    description: >\n      Boil task rerun with v3 code.\n      MVP boil data used old code (>= tie-break, death filter on all 3 modes).\n      Rerun with clean v3 code for unified analysis.\n    priority: P1\n    gpu_budget_hours: 3\n    deps: []\n    notes: Can run in parallel with plan-001a as first batch.\n\n  - id: plan-008\n    claim: C2\n    description: >\n      Router size ablation. Compare Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B as router.\n      Tests sensitivity to router capacity.\n    priority: P1\n    gpu_budget_hours: 12\n    deps: [plan-001b]\n    notes: >\n      Important for \"lightweight\" claim. If 1.5B matches 1.7B, strengthens \"small router suffices\".\n      Low priority relative to core experiments.\n\n  # === P2: Nice to have / Future work material ===\n\n  - id: plan-009\n    claim: C1\n    description: >\n      MATH track — code interpreter as deterministic oracle.\n      500 Level 4-5 MATH problems. 2-way routing: internal / code-interpreter.\n      Demonstrates generalization beyond environment simulators.\n    priority: P2\n    gpu_budget_hours: 20\n    deps: [plan-002]\n    notes: >\n      Human Review Note suggested MATH as secondary track.\n      Only if ScienceWorld experiments finish by Day 8.\n\n  - id: plan-010\n    claim: C2\n    description: >\n      Cross-task transfer within ScienceWorld.\n      Train router on chemistry tasks only, evaluate on physics tasks (and vice versa).\n      Tests whether routing patterns transfer across task domains.\n    priority: P2\n    gpu_budget_hours: 5\n    deps: [plan-002]\n\n# === Summary (post-Reviewer revision) ===\n# P0 total: ~72 GPU-hours (plan-001a 10h + plan-001b 25h + plan-002 8h + plan-003 15h + plan-004 12h + plan-005 2h)\n# P1 total: ~25 GPU-hours (plan-006 10h + plan-007 3h + plan-008 12h)\n# P2 total: ~25 GPU-hours (plan-009 20h + plan-010 5h)\n# Grand total: ~122 GPU-hours\n# All estimates in RTX 5090 32GB wall-clock hours (Reviewer W5)\n#\n# Critical path: plan-001a (10h) → plan-001b (25h) → plan-002 (8h) → plan-003 (15h) → plan-005 (2h)\n# = ~60h sequential, ~2.5 days with 2 GPUs running in parallel\n# plan-004 runs parallel with plan-002/003 on second GPU\n# plan-007 runs parallel with plan-001a\n#\n# Key changes from v1:\n# - plan-001 split into 001a (pre-screening) + 001b (full collection) per Reviewer W3\n# - 2-way collection first (not 3-way) per Reviewer W2, saves ~33% GPU time\n# - plan-004 adds 1.7B implicit control per Reviewer W4\n# - GPU budget unit: RTX 5090 32GB hours (not H100) per Reviewer W5\n",
      "numLines": 187,
      "startLine": 1,
      "totalLines": 187
    }
  },
  "sourceToolAssistantUUID": "fc0d6e62-b791-4e15-a980-81a3019fe71b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-13T15:38:29.733Z_

````json
{
  "parentUuid": "686caa17-b188-43fa-88f7-5ff2d736bc29",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**simgate-modular-routing**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"simgate-modular-routing\")` 或 `load_project_config(\"simgate-modular-routing\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/simgate-modular-routing/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "6f7c266f-2c7a-4239-8d0e-952ed628dd6a",
  "timestamp": "2026-05-13T15:38:29.733Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心假设部分成立：death avoidance 机制复现但无 positive guidance 信号，selective > unconditional 一致但幅度较小，explicit > implicit 成立但差距不大，整体分数接近但未超过 CogRouter 核心假设：['A1 death a…",
  "leafUuid": "6f7c266f-2c7a-4239-8d0e-952ed628dd6a",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Define median-tier results for SimGate routing paper",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f"
}
```

---

### Assistant

_source line 17 · 2026-05-13T15:38:58.490Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted/imagined experimental results for each planned experiment in the experiment plan, following the "median" tier definition they've provided. Let me carefully go through each experiment and create realistic predicted results that are consistent with the median tier.

Key median tier characteristics:
- Death avoidance mechanism works but no positive guidance signal
- Selective > unconditional is consistent but small (5-12 points)
- Explicit > implicit is real but modest (3-8 points)
- Counterfactual labels generalize moderately, router accuracy is average
- Routing patterns show phase-dependent patterns but failure taxonomy isn't clean


- Overall score 72-84, close to but not exceeding CogRouter (84.6)
- simgate_minus_always_internal: 15-25
- oracle_minus_always_det: 5-12
- explicit_minus_implicit: 3-8
- catastrophic_failure_reduction_pct: 40-60%
- router_accuracy_pct: 65-75%
- simulator_invocation_ratio_pct: 30-50%
- task_types_with_significant_gain: 8-12

Now I'm working through the first experiment, plan-001a, which involves pre-screening around 20 task types across 5 episodes to detect early signal patterns.

For plan-001a, I expect deterministic to outperform internal on some tasks but not others, with physics and chemistry showing strong signal while ecology and biology lag behind—roughly 12-14 of the 20 task types should demonstrate positive signal.

Plan-001b scales this up by collecting 20 episodes on the signal-positive tasks, gathering state-observation-modality triples with moderately noisy labels, where about 35-45% favor deterministic and the rest prefer internal.

For plan-002, I'm fine-tuning a smaller language model on these labels, expecting router accuracy around 65-75% but with modest validation performance on weaker task types.

Plan-003 runs the full SimGate evaluation end-to-end.

The results show overall scores of 72-84, with a 15-25 point improvement over always-internal routing and a 40-60% reduction in catastrophic failures, while invoking the simulator 30-50% of the time.

Plan-004 compares explicit versus implicit routing across different model sizes, finding a 3-8 point advantage for explicit routing.

Plan-005 reveals phase-dependent routing patterns that are clearer in physics and chemistry but noisier in biology and ecology, though the failure taxonomy remains unclear.

Plan-006 tests whether 2-way routing performs similarly to 3-way, finding marginal differences that suggest simplifying to 2-way.

Plan-007 moves toward boiling down the task.

For plan-008, I'm checking router size ablations where 1.5B performs slightly worse and 3B shows marginal gains, supporting the lightweight router claim.

Plan-009 on the MATH track is lower priority but shows that code interpretation helps with computation-heavy problems, though gains are modest.

Plan-010 examines cross-task transfer between chemistry and physics, finding moderate transfer in both directions that confirms partial but incomplete generalization.

Now I'm constructing the full YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f7c266f-2c7a-4239-8d0e-952ed628dd6a",
  "isSidechain": false,
  "requestId": "req_011CazpPrcaMHRkAomb8iTek",
  "type": "assistant",
  "uuid": "d0adc366-912d-47ed-946a-8ed200c5e12c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1Zp8CzWeE7E4vjzUbvDrk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7913,
      "cache_read_input_tokens": 26238,
      "output_tokens": 14819,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14819,
          "cache_read_input_tokens": 26238,
          "cache_creation_input_tokens": 7913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7913
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

_source line 18 · 2026-05-13T15:43:23.515Z_

```yaml
tier: median
narrative_guidance: >
  整体叙事从 "new SOTA via safety-aware routing" 转向 "first explicit study of when deterministic computation helps LLM agents, with controlled causal evidence"。
  C1 不与 CogRouter 直接比 SOTA，改为强调 SimGate vs 自身 ablation baselines 的受控实验，headline 为 "reduces catastrophic failures by ~50%"。
  C2 explicit vs implicit 差距写成 "consistent but moderate advantage"，重心转向 interpretability/modularity 的定性价值。
  routing pattern 分析从 failure mode taxonomy 降为 phase-dependent routing trends。
  补充 plan-006 (2-way vs 3-way) 增加实验密度弥补 headline number 不够突出的不足。

imagined_experiments:
  - name: "Mini Signal Detection (Pre-screening)"
    plan_id: "plan-001a"
    description: >
      对 ~20 个 ScienceWorld task type 各跑 5 episodes，2-way (internal + deterministic)，
      筛选出 det > internal 的 task types 进入 plan-001b。
    expected_results:
      total_task_types_screened: 20
      signal_positive_task_types: 13
      strong_signal_types: 7
      moderate_signal_types: 4
      weak_signal_types: 2
      no_signal_types: 7
      strong_signal_list: "boil, melt, change-state-of-matter, freeze, use-thermometer, mix-chemicals, react-acid-base"
      moderate_signal_list: "mix-paint, measure-melting-point, conduct-electricity, identify-life-stages"
      weak_signal_list: "grow-plant-basic, navigate-rooms"
      no_signal_example: "grow-plant-advanced, read-thermometer, find-animal, classify-living, ecology-food-web, identify-rocks, use-microscope"
      mean_det_minus_internal_strong: 38.5
      mean_det_minus_internal_moderate: 18.2
      mean_det_minus_internal_weak: 6.3
      gpu_hours_actual: 9.5
    result_rationale: >
      Median 档下 death avoidance 是主要增益来源但集中在 physics/chemistry tasks。
      涉及温度变化、相态转换、化学反应的 7 个 task type 展示强信号（det-internal ~35-45 分），
      因为 LLM 在多步物理推理中频繁 hallucinate 状态导致 death (-100)，deterministic oracle 消除了这些 catastrophic failures。
      4 个 moderate signal tasks 有部分物理/化学子步骤但非全程依赖，增益在 10-25 分。
      2 个 weak signal tasks 动作空间简单、death 风险低，deterministic 的 safety-net 价值有限。
      7 个 no-signal tasks（生态观察、分类、阅读类）几乎无 death 惩罚，internal reasoning 本身足够，
      det invocation 反而引入不必要的 rigid execution，无法利用 LLM 的灵活推理优势。
      这个 13/20 的通过率说明 safety-aware routing 不是 universal solution，而是 domain-specific mechanism。
    tables:
      - name: "Table: Signal Pre-screening Results (5 episodes per task type)"
        columns: ["task_type", "domain", "internal_mean", "det_mean", "det_minus_internal", "death_rate_internal", "death_rate_det", "signal"]
        rows:
          - ["boil", "physics", -48.2, -12.6, 35.6, 0.60, 0.10, "strong"]
          - ["melt", "physics", -52.1, -11.8, 40.3, 0.65, 0.08, "strong"]
          - ["change-state", "physics", -50.8, -10.4, 40.4, 0.62, 0.10, "strong"]
          - ["freeze", "physics", -45.6, -8.2, 37.4, 0.58, 0.06, "strong"]
          - ["use-thermometer", "physics", -38.4, -5.0, 33.4, 0.50, 0.08, "strong"]
          - ["mix-chemicals", "chemistry", -55.2, -14.8, 40.4, 0.68, 0.12, "strong"]
          - ["react-acid-base", "chemistry", -46.0, -7.5, 38.5, 0.55, 0.08, "strong"]
          - ["mix-paint", "chemistry", -32.5, -14.3, 18.2, 0.35, 0.12, "moderate"]
          - ["measure-melting-point", "physics", -28.0, -8.6, 19.4, 0.30, 0.10, "moderate"]
          - ["conduct-electricity", "physics", -25.8, -10.2, 15.6, 0.28, 0.08, "moderate"]
          - ["identify-life-stages", "biology", -22.4, -2.6, 19.8, 0.25, 0.06, "moderate"]
          - ["grow-plant-basic", "biology", -15.2, -8.9, 6.3, 0.12, 0.04, "weak"]
          - ["navigate-rooms", "spatial", -10.4, -4.1, 6.3, 0.08, 0.02, "weak"]
          - ["grow-plant-advanced", "biology", -8.6, -9.2, -0.6, 0.06, 0.04, "none"]
          - ["read-thermometer", "physics", -5.2, -4.8, 0.4, 0.02, 0.02, "none"]
          - ["find-animal", "ecology", -12.0, -13.5, -1.5, 0.04, 0.06, "none"]
          - ["classify-living", "biology", -6.8, -8.0, -1.2, 0.02, 0.04, "none"]
          - ["ecology-food-web", "ecology", -18.5, -20.1, -1.6, 0.10, 0.12, "none"]
          - ["identify-rocks", "geology", -8.0, -7.5, 0.5, 0.04, 0.02, "none"]
          - ["use-microscope", "biology", -4.2, -5.0, -0.8, 0.02, 0.02, "none"]
    figures_description:
      - "Bar chart: det_minus_internal per task type, colored by domain (physics=blue, chemistry=green, biology=orange, ecology=red, spatial=gray), horizontal line at 0. Clear visual separation: physics/chemistry tasks cluster above +30, biology/ecology near 0 or negative."
    analysis: >
      13/20 task types 通过信号筛选（≥5 分 det>internal 差距），与 median 档 task_types_with_significant_gain 8-12 的预期一致
      （部分 moderate/weak signal 在 full 20-episode 评估中可能跌出显著性）。
      Domain 分布清晰：physics 5/5 全部有信号，chemistry 3/3 全部有信号，biology 2/5 有信号，ecology 0/2 无信号。
      这直接支持 median 档的 A1 判断——death avoidance 增益集中在 physics/chemistry tasks。
      No-signal tasks 将排除出 plan-001b，节约 ~35% GPU 时间。

  - name: "Full Counterfactual Trajectory Collection"
    plan_id: "plan-001b"
    description: >
      对 plan-001a 筛出的 13 个 signal-positive task types 各跑 20 episodes，
      2-way counterfactual collection (internal + deterministic)，max_steps=30，
      记录每步最优 modality 的 hindsight labels。
    expected_results:
      task_types_collected: 13
      episodes_per_task: 20
      total_episodes: 260
      total_steps_labeled: 6240
      label_distribution_deterministic_pct: 38.5
      label_distribution_internal_pct: 61.5
      label_agreement_strong_tasks_pct: 82.0
      label_agreement_weak_tasks_pct: 64.0
      noisy_label_rate_overall_pct: 18.5
      avg_steps_per_episode: 24.0
      gpu_hours_actual: 23.5
    result_rationale: >
      Median 档下 counterfactual labels 泛化中等（A4），具体表现为：
      强信号 tasks (physics/chemistry) 的 label agreement ~82%——大多数步骤中 deterministic 和 internal 的优劣清晰，
      因为 death/survival 差异提供了 binary signal。
      弱信号 tasks 的 label agreement 仅 ~64%——很多步骤两种 modality 表现相近（都不死也都没进展），
      hindsight labeling 分不出哪个更好，导致标签噪声大。
      整体 38.5% 步骤 labeled as deterministic-preferred，说明不是每步都需要 safety net，
      支持 selective routing 的必要性。但这个比例意味着 router 要学会一个相当细粒度的 per-step 判断。
      标签噪声 ~18.5% 将直接限制 router accuracy 的上限（A4），是 median 档 router accuracy 65-75% 的根本原因。
    tables:
      - name: "Table: Trajectory Collection Summary by Domain"
        columns: ["domain", "n_tasks", "n_episodes", "total_steps", "pct_det_preferred", "label_agreement_pct", "avg_death_rate_internal"]
        rows:
          - ["physics (strong)", 5, 100, 2450, 42.1, 84.5, 0.59]
          - ["chemistry (strong)", 2, 40, 960, 43.8, 79.0, 0.62]
          - ["physics (moderate)", 2, 40, 920, 33.2, 68.5, 0.29]
          - ["chemistry (moderate)", 1, 20, 480, 30.5, 72.0, 0.35]
          - ["biology (moderate)", 1, 20, 510, 28.0, 60.5, 0.25]
          - ["biology (weak)", 1, 20, 460, 22.4, 58.0, 0.12]
          - ["spatial (weak)", 1, 20, 460, 20.8, 55.0, 0.08]
    figures_description:
      - "Scatter plot: x=death_rate_internal, y=pct_det_preferred per task type. Strong positive correlation (r~0.85). 标注 task names. 直观展示 death avoidance 与 deterministic routing 需求的关联。"
    analysis: >
      ~6240 个 labeled steps 为 router SFT 提供训练数据。标签质量的 domain-dependent 特征
      预示了 router 在不同 task domains 上性能将不均匀。强信号 tasks 提供高质量 labels (agreement>80%)，
      弱信号 tasks 的 labels 噪声高 (agreement<65%)，将直接反映在 plan-003 的 per-task-type breakdown 中。
      det-preferred 比例 38.5% 与 median 档 simulator_invocation_ratio 30-50% 一致。

  - name: "Router SFT Training"
    plan_id: "plan-002"
    description: >
      在 plan-001b 的 counterfactual labels 上 fine-tune Qwen3-1.7B 做 2-way classification
      (internal vs deterministic)。Leave-one-out cross-validation by task type。
    expected_results:
      train_loss_final: 0.42
      val_accuracy_overall_pct: 71.2
      val_accuracy_strong_tasks_pct: 78.5
      val_accuracy_moderate_tasks_pct: 66.0
      val_accuracy_weak_tasks_pct: 58.3
      val_f1_deterministic: 0.68
      val_f1_internal: 0.74
      leave_one_out_accuracy_range: [62.0, 76.0]
      leave_one_out_mean_accuracy: 68.5
      best_epoch: 2
      convergence_epoch: 3
      gpu_hours_actual: 6.5
    result_rationale: >
      Median 档 router accuracy 65-75% (A4)。整体 val accuracy 71.2% 符合此区间。
      强信号 tasks 的 labels 清晰（death/survival 二分），router 在这些 tasks 上学到了有效的 pattern，
      accuracy 达 78.5%。弱信号 tasks 的标签噪声大，router accuracy 仅 58.3%——接近 random baseline (50%)。
      Leave-one-out 验证显示跨 task type 泛化中等（A4），range 62-76%：
      留出 physics task 时其他 physics tasks 提供足够 coverage，accuracy 高端 (~76%)；
      留出 biology task 时几乎没有同 domain 训练数据，accuracy 低端 (~62%)。
      F1 score deterministic < internal 反映类别不平衡（38.5% vs 61.5%）和 deterministic labels 更noisy。
      Train loss 未过拟合（epoch 2-3 之间收敛），但 val accuracy 到 epoch 3 后不再提升，
      说明瓶颈在标签质量而非模型容量。
    tables:
      - name: "Table: Router Training Metrics"
        columns: ["metric", "epoch_1", "epoch_2", "epoch_3"]
        rows:
          - ["train_loss", 0.58, 0.45, 0.42]
          - ["val_loss", 0.55, 0.48, 0.47]
          - ["val_accuracy (%)", 64.8, 70.5, 71.2]
          - ["val_f1_det", 0.60, 0.67, 0.68]
          - ["val_f1_int", 0.68, 0.73, 0.74]
      - name: "Table: Leave-One-Out Cross-Validation (selected task types)"
        columns: ["held_out_task", "domain", "accuracy_on_held_out (%)", "accuracy_on_rest (%)"]
        rows:
          - ["boil", "physics", 76.0, 71.8]
          - ["melt", "physics", 74.5, 71.5]
          - ["mix-chemicals", "chemistry", 72.0, 71.0]
          - ["mix-paint", "chemistry", 67.5, 72.0]
          - ["identify-life-stages", "biology", 62.0, 72.5]
          - ["grow-plant-basic", "biology", 63.5, 72.0]
    figures_description:
      - "Training curves: x=steps, y=loss/accuracy. Train loss (solid) vs val loss (dashed). Val accuracy plateaus at epoch 2.5. 标注 label noise ceiling (~75%) as horizontal dotted line."
    analysis: >
      Router 训练收敛稳定，但 accuracy 受限于标签噪声上限。71.2% 的 val accuracy 是 median 档的中间值。
      Leave-one-out 结果确认跨 task type 泛化中等——同 domain 迁移较好，跨 domain 较差。
      这个 router 的主要价值在于 physics/chemistry tasks 上的可靠判断，
      弱 tasks 上的 routing decisions 接近 random 但因为这些 tasks 本身 death rate 低，影响有限。

  - name: "SimGate End-to-End Evaluation"
    plan_id: "plan-003"
    description: >
      Trained router + Qwen2.5-7B backbone 在 held-out episodes 上端到端评估。
      对比 always-internal, always-deterministic, oracle-routing, random-routing, confidence-threshold heuristic。
    expected_results:
      simgate_score_overall: 78.2
      always_internal_score: 56.8
      always_deterministic_score: 70.5
      oracle_routing_score: 81.2
      random_routing_score: 63.4
      confidence_threshold_score: 66.8
      simgate_minus_always_internal: 21.4
      simgate_minus_always_deterministic: 7.7
      oracle_minus_simgate: 3.0
      oracle_minus_always_det: 10.7
      catastrophic_failure_rate_internal_pct: 48.5
      catastrophic_failure_rate_simgate_pct: 22.3
      catastrophic_failure_rate_det_pct: 8.5
      catastrophic_failure_reduction_pct: 54.0
      simulator_invocation_ratio_pct: 41.2
      cogrouter_reported: 84.6
      itp_r_reported: 62.58
      simgate_minus_cogrouter: -6.4
      bootstrap_90ci_simgate: [74.5, 81.8]
      bootstrap_90ci_always_internal: [52.0, 61.5]
      bootstrap_90ci_always_det: [66.2, 74.8]
      task_types_with_significant_gain: 10
      gpu_hours_actual: 14.0
    result_rationale: >
      Median 档 simgate_score_overall 72-84，取 78.2。未超过 CogRouter (84.6) 但差距 6.4 分，
      在 bootstrap CI 下两者 overlap（SimGate CI 上界 81.8 vs CogRouter 84.6），不能 claim SOTA。
      SimGate vs always-internal +21.4 分——核心 safety-net value，catastrophic failure 从 48.5% 降至 22.3%（降幅 54%），
      符合 median 档 catastrophic_failure_reduction_pct 40-60%。
      SimGate vs always-deterministic +7.7 分——selective routing 价值，说明并非所有步骤需要 safety net，
      unconditional simulation 在低风险步骤引入了不必要的 rigid execution（LLM 在安全步骤上 reasoning 更灵活）。
      Oracle vs SimGate 仅 3.0 分——router 已捕获大部分可学习的 routing signal，剩余 gap 来自弱 task types 的标签噪声。
      Simulator invocation ratio 41.2%——router 在约 40% 步骤调用 deterministic，远少于 always-det 的 100%，
      说明 router 学到了 selective invocation pattern。
      对比 CogRouter 差距的原因：CogRouter 用 RL (CoPO) 在 trajectory 级别优化，
      SimGate 用 SFT per-step labels，且无 positive guidance signal (A6)——router 仅防死不指路。
      10/13 task types 显著增益（physics 5/5 + chemistry 3/3 + moderate 2/4），
      符合 median 档 task_types_with_significant_gain 8-12。
    tables:
      - name: "Table 1 (Main Results): SimGate vs Baselines on ScienceWorld"
        columns: ["method", "overall_score", "90% CI", "catastrophic_failure_rate (%)", "sim_invocation_ratio (%)", "LLM_tokens (k)"]
        rows:
          - ["Always-Internal", 56.8, "[52.0, 61.5]", 48.5, 0, 385]
          - ["Always-Deterministic", 70.5, "[66.2, 74.8]", 8.5, 100, 142]
          - ["Random Routing (p=0.4)", 63.4, "[58.8, 68.0]", 30.2, 40.0, 248]
          - ["Confidence Threshold", 66.8, "[62.0, 71.5]", 28.8, 35.5, 262]
          - ["SimGate (ours)", 78.2, "[74.5, 81.8]", 22.3, 41.2, 240]
          - ["Oracle Routing", 81.2, "[77.8, 84.5]", 12.0, 36.5, 255]
          - ["---", "---", "---", "---", "---", "---"]
          - ["CogRouter (reported)", 84.6, "—", "—", "—", "—"]
          - ["ITP-R (reported)", 62.58, "—", "—", "—", "—"]
      - name: "Table: Per-Task-Type Breakdown (SimGate vs Always-Internal)"
        columns: ["task_type", "domain", "simgate_score", "internal_score", "delta", "catastrophic_failure_reduction_pct", "significant"]
        rows:
          - ["boil", "physics", 82.5, 52.0, 30.5, 62, "yes"]
          - ["melt", "physics", 85.0, 48.5, 36.5, 68, "yes"]
          - ["change-state", "physics", 84.2, 50.2, 34.0, 65, "yes"]
          - ["freeze", "physics", 80.8, 55.0, 25.8, 58, "yes"]
          - ["use-thermometer", "physics", 78.0, 60.5, 17.5, 52, "yes"]
          - ["mix-chemicals", "chemistry", 82.0, 46.8, 35.2, 70, "yes"]
          - ["react-acid-base", "chemistry", 80.5, 52.5, 28.0, 60, "yes"]
          - ["mix-paint", "chemistry", 76.2, 62.0, 14.2, 42, "yes"]
          - ["measure-melting-point", "physics", 74.5, 65.0, 9.5, 35, "yes"]
          - ["conduct-electricity", "physics", 72.0, 60.5, 11.5, 38, "yes"]
          - ["identify-life-stages", "biology", 68.5, 62.0, 6.5, 22, "no"]
          - ["grow-plant-basic", "biology", 65.0, 60.5, 4.5, 15, "no"]
          - ["navigate-rooms", "spatial", 62.8, 58.0, 4.8, 12, "no"]
    figures_description:
      - "Grouped bar chart: SimGate vs Always-Internal vs Always-Det vs Oracle per task type, sorted by delta. Physics/chemistry tasks cluster left with large deltas, biology/spatial tasks cluster right with small deltas."
      - "Scatter plot: x=catastrophic_failure_rate_internal, y=SimGate delta. Strong positive correlation, 标注 r=0.91. 直接可视化 'death avoidance is primary mechanism' claim."
    analysis: >
      SimGate 78.2 低于 CogRouter 84.6 约 6 分。叙事不能 claim SOTA，但 controlled ablation 提供了强因果证据：
      SimGate vs internal (+21.4)、vs det (+7.7)、vs random (+14.8)、vs heuristic (+11.4) 全部显著。
      catastrophic failure reduction 54% 是强 headline number。
      Per-task breakdown 清晰展示 death avoidance 是主要机制——physics/chemistry 的 delta 与 internal death rate 高度相关 (r=0.91)。
      3 个弱 tasks (biology/spatial) 的 delta <7 且不显著，支持 A1 的 domain-specific 判断。
      SimGate 比 CogRouter 差的原因可归为：(1) SFT vs RL training，(2) 无 positive guidance signal。
      Paper 叙事应改为 "first controlled study demonstrating causal role of deterministic computation in preventing catastrophic LLM failures"。

  - name: "Explicit vs Implicit Routing Ablation"
    plan_id: "plan-004"
    description: >
      三条件对比：(a) 1.7B explicit router (SimGate), (b) 1.7B implicit router (SFT output [SIMULATE]),
      (c) 7B implicit routing (backbone tool-use prompt)。全部用相同 counterfactual labels 训练。
    expected_results:
      explicit_1_7b_score: 78.2
      implicit_1_7b_score: 73.5
      implicit_7b_score: 74.8
      explicit_minus_implicit_1_7b: 4.7
      explicit_minus_implicit_7b: 3.4
      implicit_1_7b_catastrophic_failure_pct: 28.5
      implicit_7b_catastrophic_failure_pct: 26.2
      explicit_sim_invocation_ratio_pct: 41.2
      implicit_1_7b_sim_invocation_ratio_pct: 35.0
      implicit_7b_sim_invocation_ratio_pct: 38.5
      bootstrap_90ci_explicit: [74.5, 81.8]
      bootstrap_90ci_implicit_1_7b: [69.2, 77.8]
      bootstrap_90ci_implicit_7b: [70.5, 79.0]
      explicit_vs_implicit_1_7b_significant: true
      explicit_vs_implicit_7b_significant: "marginal (p=0.08)"
      gpu_hours_actual: 11.0
    result_rationale: >
      Median 档 explicit_minus_implicit 3-8 分，statistical significance 在部分条件下边缘 (A3)。
      Explicit 1.7B vs implicit 1.7B: +4.7 分，parameter-matched comparison 显著 (p<0.05)。
      这说明 explicit modular router 架构本身有价值——将 routing decision 从 generation 中解耦，
      避免了 implicit routing 中 generation 任务和 routing 任务的 multi-task interference。
      Explicit 1.7B vs implicit 7B: +3.4 分，但 CI overlap 大 (p=0.08，边缘显著)。
      7B implicit 比 1.7B implicit 好 1.3 分——额外容量有 marginal 帮助但不足以弥补架构劣势。
      Implicit routers 的 sim_invocation_ratio 偏低 (35-38.5% vs explicit 41.2%)——
      implicit routing 倾向于 under-invoke simulator（routing signal 在 generation logits 中被稀释），
      导致更多 catastrophic failures 未被拦截。
      这个 "consistent but moderate advantage" 的结果支持 C2 的定性 claim（interpretability, modularity）
      而非强 performance claim。Median 档下 C2 的重心应转向：
      explicit router 可独立替换、routing decisions 可分析，这些定性价值在 3-5 分性能差距之上额外成立。
    tables:
      - name: "Table: Explicit vs Implicit Routing Ablation"
        columns: ["condition", "params", "overall_score", "90% CI", "catastrophic_failure (%)", "sim_invocation (%)", "p vs explicit"]
        rows:
          - ["Explicit Router (SimGate)", "1.7B", 78.2, "[74.5, 81.8]", 22.3, 41.2, "—"]
          - ["Implicit Router (SFT)", "1.7B", 73.5, "[69.2, 77.8]", 28.5, 35.0, "0.03"]
          - ["Implicit Routing (tool-use)", "7B", 74.8, "[70.5, 79.0]", 26.2, 38.5, "0.08"]
          - ["Always-Internal", "—", 56.8, "[52.0, 61.5]", 48.5, 0, "<0.001"]
    figures_description:
      - "Box plot: three conditions' score distributions across task types. Explicit has higher median and tighter IQR. Annotate p-values for pairwise comparisons."
    analysis: >
      Parameter-matched comparison (1.7B explicit vs 1.7B implicit, +4.7, p=0.03) 是 C2 最干净的证据。
      7B implicit 条件 (p=0.08) 可写为 "marginal significance"，但方向一致。
      Median 档叙事：explicit routing 是 "consistent but moderate advantage"，
      主要价值在 architectural benefits (modularity, interpretability, independent replacement)，
      用 4.7 分的定量证据 + 定性分析支撑。不能写成 "large performance gap"。

  - name: "Per-Task Routing Pattern Analysis"
    plan_id: "plan-005"
    description: >
      从 plan-003 输出分析 routing patterns：(a) 哪些 task types 触发 deterministic 最多，
      (b) routing 集中在哪个 episode phase，(c) router-as-diagnostic-probe 识别 LLM failure modes。
    expected_results:
      n_routing_decisions_analyzed: 3900
      phase_early_det_pct: 25.0
      phase_mid_det_pct: 52.0
      phase_late_det_pct: 38.0
      physics_det_invocation_pct: 48.5
      chemistry_det_invocation_pct: 45.2
      biology_det_invocation_pct: 28.0
      spatial_det_invocation_pct: 22.0
      top_3_routing_triggers: "state-change actions (heat/cool/mix), multi-step causal chains (>3 steps), post-failure recovery steps"
      failure_mode_clusters_identified: 4
      cluster_clarity: "moderate — 2 clear clusters, 2 diffuse"
      gpu_hours_actual: 1.5
    result_rationale: >
      Median 档 routing patterns 部分可解释 (A5)——能看到 phase-dependent 模式但 failure taxonomy 不够清晰。
      Phase-dependent pattern 清晰：mid-game (steps 8-20) routing 最密集 (52%)，
      因为这个阶段 agent 执行 state-changing actions (加热、冷却、混合) 最多，
      LLM 容易在多步物理推理中 hallucinate 中间状态。
      Early-game (steps 1-7) routing 较低 (25%)——agent 主要在 navigate 和 gather objects，death 风险低。
      Late-game (steps 21-30) routing 中等 (38%)——部分 tasks 在此阶段做 final verification，
      但也有很多 episodes 已经结束或 stuck。
      4 个 failure mode clusters 中：
      (1) "thermal state tracking failure" — 清晰，LLM 丢失温度/相态信息
      (2) "chemical reaction sequencing" — 清晰，LLM 搞错反应步骤顺序
      (3) "multi-step causal confusion" — 模糊，涵盖多种因果推理错误，不够 specific
      (4) "environment state drift" — 模糊，router triggers 散布在各种步骤中
      这是 median 档 A5 的典型表现——有 pattern 但 failure taxonomy 不 clean。
      Paper figure 只报告 phase-dependent routing trends，不宣称 comprehensive failure taxonomy。
    tables:
      - name: "Table: Routing Decision Distribution by Episode Phase"
        columns: ["phase", "steps", "total_decisions", "det_routing_pct", "avg_death_rate_if_internal"]
        rows:
          - ["early", "1-7", 1200, 25.0, 0.12]
          - ["mid", "8-20", 1800, 52.0, 0.45]
          - ["late", "21-30", 900, 38.0, 0.28]
      - name: "Table: Failure Mode Clusters (Router-as-Diagnostic-Probe)"
        columns: ["cluster", "description", "n_steps", "pct_of_det_routing", "clarity"]
        rows:
          - [1, "thermal state tracking failure", 420, 27.0, "clear"]
          - [2, "chemical reaction sequencing error", 310, 20.0, "clear"]
          - [3, "multi-step causal confusion", 480, 31.0, "diffuse"]
          - [4, "environment state drift", 340, 22.0, "diffuse"]
    figures_description:
      - "Figure 1 (Paper): Routing heatmap — x=episode step (1-30), y=task type (sorted by domain). Color intensity = deterministic routing probability. Clear 'hot band' in mid-game steps for physics/chemistry tasks. Annotated with phase boundaries."
      - "Supplementary: t-SNE of router hidden states at deterministic-routing steps, colored by cluster ID. Clusters 1&2 tight, clusters 3&4 overlapping."
    analysis: >
      Phase-dependent routing trend 是 robust 的 finding，可以放 paper Figure 1。
      但 failure taxonomy 降级处理——从 "failure mode taxonomy" 改为 "we observe routing concentrates at
      state-change actions during mid-game phases, suggesting the router learns to detect high-risk physical
      reasoning steps"。不宣称 comprehensive failure analysis，只报告 observable trends。
      Mid-game concentration (52% of det routing) 直接对应 death avoidance mechanism——
      这正是 agent 执行 irreversible physical actions 的阶段。

  - name: "2-Way vs 3-Way Routing Ablation"
    plan_id: "plan-006"
    description: >
      补充 deep-internal modality 数据，比较 {internal, deterministic} vs {fast-internal, deep-internal, deterministic}。
      测试 fast/deep internal 区分是否有额外价值。
    expected_results:
      two_way_score: 78.2
      three_way_score: 79.8
      delta: 1.6
      p_value: 0.22
      significant: false
      three_way_sim_invocation_pct: 39.5
      three_way_deep_internal_pct: 18.0
      three_way_fast_internal_pct: 42.5
      supplemental_data_collection_hours: 5.5
      router_retraining_hours: 3.0
      gpu_hours_actual: 9.5
    result_rationale: >
      Median 档下 3-way 与 2-way 差距小且不显著 (+1.6, p=0.22)。
      Fast/deep internal 区分的理论价值在于：deep-internal 在需要更多 reasoning 但不需要 ground-truth 的步骤上
      用 extended thinking 提升质量。但实际效果有限，原因：
      (1) death avoidance 是主要增益来源 (A6)——一旦 deterministic 拦截了 catastrophic failures，
      剩余步骤中 fast vs deep internal 的差异很小（LLM 在安全步骤上的表现差异不大）。
      (2) 没有 positive guidance signal——deep internal 不能给出更好的 task guidance，只是"想更久"，
      但在 deterministic 已经处理了高风险步骤后，多想对安全步骤帮助有限。
      (3) Router 从 2-class 升到 3-class 增加了 classification 难度，在 median 档标签噪声下性能提升被抵消。
      结论：2-way 足够，simplifies the story。Paper 中可以一句话报告 "binary routing (simulate-or-not) suffices;
      adding a third modality yields no significant improvement"。
    tables:
      - name: "Table: 2-Way vs 3-Way Routing Comparison"
        columns: ["routing_scheme", "overall_score", "90% CI", "sim_invocation (%)", "p vs 2-way"]
        rows:
          - ["2-way {int, det}", 78.2, "[74.5, 81.8]", 41.2, "—"]
          - ["3-way {fast, deep, det}", 79.8, "[75.8, 83.5]", 39.5, "0.22"]
    figures_description:
      - "Paired bar chart: 2-way vs 3-way per task type. Most bars nearly identical. 标注 ns (not significant)."
    analysis: >
      3-way 不显著优于 2-way，simplifies the paper narrative。
      可以 claim "binary routing decision (simulate or not) captures the essential routing signal"，
      支持 safety-net framing——router 的核心工作是检测 high-risk steps，而非 fine-grained compute allocation。
      在 paper 中作为 ablation 一句话报告即可。这增加了实验密度而不改变结论。

  - name: "Boil Task Rerun with v3 Code"
    plan_id: "plan-007"
    description: >
      用 v3 clean code（strict > tie-break, death filter only on internal）重跑 boil task 20 episodes，
      与 MVP 旧代码结果对比，确保分析一致性。
    expected_results:
      boil_v3_internal_mean: -46.5
      boil_v3_det_mean: -10.8
      boil_v3_oracle_mean: -3.2
      boil_v3_det_minus_internal: 35.7
      boil_v3_oracle_minus_det: 7.6
      boil_v3_bootstrap_90ci_det_minus_internal: [22.0, 49.5]
      boil_v3_death_rate_internal: 0.55
      boil_v3_death_rate_det: 0.08
      boil_mvp_internal_mean: -49.8
      boil_mvp_det_mean: -19.7
      delta_from_mvp_internal: 3.3
      delta_from_mvp_det: 8.9
      gpu_hours_actual: 2.5
    result_rationale: >
      V3 code 的两个修正（strict > tie-break + death filter only on internal）对 boil 的影响：
      (1) Strict > tie-break：减少了 deterministic 被选为 "best" 的 marginal cases，
      internal mean 略有提升 (-49.8 → -46.5) 因为部分原本 tie-break 判给 det 的 cases 现在留在 internal。
      (2) Death filter only on internal：det mean 显著提升 (-19.7 → -10.8) 因为 MVP 旧代码对 det 也做了 death filter，
      过滤掉了一些 det 原本能正确处理但被误判为 "death" 的 steps。
      整体 det_minus_internal 从 MVP 的 ~30 分变为 35.7 分，与 melt/change-state 的 ~40 分更接近，
      说明 v3 code 修正消除了旧代码的 systematic bias。
      Oracle mean 提升到 -3.2（接近 0），更符合预期——selective routing 应当接近 best-of-both。
    tables:
      - name: "Table: Boil Task — v3 vs MVP Code Comparison"
        columns: ["metric", "MVP (old code)", "v3 (clean code)", "delta"]
        rows:
          - ["internal_mean", -49.8, -46.5, "+3.3"]
          - ["det_mean", -19.7, -10.8, "+8.9"]
          - ["oracle_mean", -29.7, -3.2, "+26.5"]
          - ["det_minus_internal", 30.1, 35.7, "+5.6"]
          - ["death_rate_internal", "~0.6", 0.55, "—"]
          - ["death_rate_det", "~0.15", 0.08, "—"]
    figures_description: []
    analysis: >
      V3 code 修正提升了数据质量，特别是 oracle routing 从 -29.7 → -3.2 的大幅改善
      说明旧 code 的 death filter bug 严重低估了 selective routing 的价值。
      修正后 boil 与其他 physics tasks (melt, change-state) 的 pattern 更一致，
      全部 det_minus_internal 在 35-40 分范围。Paper 只使用 v3 数据。

  - name: "Router Size Ablation"
    plan_id: "plan-008"
    description: >
      比较 Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B 作为 router 的效果。
      测试 router capacity 敏感性。
    expected_results:
      qwen3_1_7b_score: 78.2
      qwen2_5_1_5b_score: 76.0
      qwen2_5_3b_score: 79.0
      qwen3_1_7b_router_accuracy_pct: 71.2
      qwen2_5_1_5b_router_accuracy_pct: 67.5
      qwen2_5_3b_router_accuracy_pct: 73.0
      delta_1_5b_vs_1_7b: -2.2
      delta_3b_vs_1_7b: 0.8
      significant_1_5b_vs_1_7b: false
      significant_3b_vs_1_7b: false
      inference_latency_1_5b_ms: 12
      inference_latency_1_7b_ms: 15
      inference_latency_3b_ms: 28
      gpu_hours_actual: 10.0
    result_rationale: >
      Median 档下 router 性能受限于 label noise 而非 model capacity (plan-002 分析已显示)。
      1.5B vs 1.7B: -2.2 分但不显著 (p>0.1)——1.5B 容量略不足以 capture 一些 edge case routing patterns，
      但差距在标签噪声范围内。Router accuracy 67.5% vs 71.2%，差距主要在 moderate/weak signal tasks。
      3B vs 1.7B: +0.8 分不显著——额外容量无法突破标签噪声上限。Router accuracy 73% vs 71.2%，
      marginal improvement 被 end-to-end evaluation 的 variance 吞没。
      这支持 "lightweight router suffices" claim：1.5B-3B 范围内性能差异 <3 分，
      瓶颈在训练数据质量而非 router capacity。
      Inference latency 差异对 overall pipeline 影响 negligible（router inference 远快于 LLM backbone inference）。
    tables:
      - name: "Table: Router Size Ablation"
        columns: ["router", "params", "router_accuracy (%)", "e2e_score", "90% CI", "latency (ms)"]
        rows:
          - ["Qwen2.5-1.5B", "1.5B", 67.5, 76.0, "[71.8, 80.2]", 12]
          - ["Qwen3-1.7B", "1.7B", 71.2, 78.2, "[74.5, 81.8]", 15]
          - ["Qwen2.5-3B", "3.0B", 73.0, 79.0, "[75.2, 82.8]", 28]
    figures_description:
      - "Line plot: x=router params (log scale), y=e2e score. Near-flat line with error bars overlapping. 标注 'label noise ceiling' as horizontal band."
    analysis: >
      Router size ablation 支持两个 claims：(1) 小 router 足够 ("lightweight" in C2)，
      (2) 瓶颈在标签质量——增加 router capacity 收益递减。
      Paper 可报告 "routers from 1.5B to 3B parameters achieve comparable performance (76-79),
      suggesting the routing task is learnable at modest scale"。

  - name: "MATH Track — Code Interpreter as Oracle"
    plan_id: "plan-009"
    description: >
      500 道 Level 4-5 MATH 题，2-way routing: internal / code-interpreter。
      测试 safety-aware routing 是否泛化到代码解释器场景。
    expected_results:
      simgate_math_accuracy_pct: 62.5
      always_internal_accuracy_pct: 55.0
      always_code_accuracy_pct: 58.8
      oracle_routing_accuracy_pct: 68.0
      simgate_minus_internal: 7.5
      simgate_minus_always_code: 3.7
      code_invocation_ratio_pct: 45.0
      router_accuracy_math_pct: 63.0
      catastrophic_error_reduction_pct: 28.0
      gpu_hours_actual: 18.0
    result_rationale: >
      Median 档下 MATH track 显示中等泛化 (A4)。
      Safety-aware routing 在 MATH 上的增益 (+7.5 vs internal) 远小于 ScienceWorld (+21.4)，原因：
      (1) MATH 没有 -100 death penalty——错误只是 0 分而非 catastrophic failure，
      safety-net 机制的 value proposition 减弱。
      (2) Code interpreter 的优势在于 arithmetic/algebraic computation，不在于 "preventing catastrophic failures"。
      LLM 在 MATH 上的错误模式更分散（reasoning errors, not just computation errors），
      code interpreter 只能修正 computation errors 这一子集。
      (3) Router 的 ScienceWorld labels 无法直接迁移，MATH 上需要 fresh labels，
      但 label quality 更差——hindsight labeling 在 MATH 上不如 ScienceWorld 清晰（没有 death/survival 信号）。
      Router accuracy 仅 63%（低于 ScienceWorld 71.2%），进一步说明 routing signal 在 MATH 上更弱。
      Catastrophic error reduction 仅 28%——定义 catastrophic 为 "算错导致 0 分"，
      code interpreter 能防止部分但远非全部。
      这个结果仍有 paper 价值：证明 selective routing 原则泛化 (simgate > always-code > always-internal)，
      但 safety-aware framing 在无 catastrophic penalty 的环境中 weakens。可作为 discussion/future work 素材。
    tables:
      - name: "Table: MATH Track Results (Level 4-5, n=500)"
        columns: ["method", "accuracy (%)", "code_invocation (%)", "computation_error_rate (%)"]
        rows:
          - ["Always-Internal", 55.0, 0, 18.5]
          - ["Always-Code", 58.8, 100, 5.2]
          - ["SimGate Router", 62.5, 45.0, 10.8]
          - ["Oracle Routing", 68.0, 38.0, 3.0]
    figures_description:
      - "Bar chart: MATH results alongside ScienceWorld results (normalized). Clear visual: ScienceWorld gains much larger. 标注 'catastrophic penalty effect'."
    analysis: >
      MATH 结果支持 selective > unconditional 的一般原则但效果弱得多。
      如果 paper 长度允许，可以作为一段 "Generalization" 讨论；
      如果 4-page 紧张，放 appendix 或 future work 一句话提及。
      关键 takeaway："safety-aware routing gains are proportional to the severity of catastrophic failure penalties"。

  - name: "Cross-Task Transfer within ScienceWorld"
    plan_id: "plan-010"
    description: >
      Chemistry-only 训练 → physics 评估，physics-only 训练 → chemistry 评估。
      测试 routing patterns 跨 domain 迁移性。
    expected_results:
      chem_train_chem_eval_score: 79.5
      chem_train_phys_eval_score: 72.8
      phys_train_phys_eval_score: 80.0
      phys_train_chem_eval_score: 71.5
      transfer_degradation_chem_to_phys: 7.2
      transfer_degradation_phys_to_chem: 8.0
      full_train_phys_eval_score: 82.5
      full_train_chem_eval_score: 82.0
      cross_domain_router_accuracy_pct: 62.5
      same_domain_router_accuracy_pct: 76.0
      gpu_hours_actual: 4.5
    result_rationale: >
      Median 档 routing pattern 迁移中等 (A4/A5)。
      Chemistry → physics 迁移降幅 7.2 分，physics → chemistry 降幅 8.0 分——
      大约 40-50% 的 routing knowledge 可以跨 domain 迁移。
      原因：death avoidance 的部分 pattern 是 domain-generic 的
      （如 "state-change actions 需要 deterministic verification"）——这个 high-level 模式在两个 domain 共享。
      但 domain-specific failure patterns（如 chemistry 的 reaction sequencing vs physics 的 thermal tracking）
      不迁移，导致 cross-domain router accuracy 从 76% 降到 62.5%。
      这个结果在 paper 中可以作为一段 analysis："routing patterns partially transfer across task domains
      sharing similar physical reasoning requirements, but domain-specific failure modes require domain-specific training data"。
      不需要改变 main claims，但增加了对 router generalization 的理解。
    tables:
      - name: "Table: Cross-Task Transfer Matrix"
        columns: ["train_domain", "eval_domain", "score", "router_accuracy (%)", "vs full-train delta"]
        rows:
          - ["chemistry", "chemistry", 79.5, 78.0, "-2.5"]
          - ["chemistry", "physics", 72.8, 62.5, "-9.7"]
          - ["physics", "physics", 80.0, 77.5, "-2.5"]
          - ["physics", "chemistry", 71.5, 61.0, "-10.5"]
          - ["all", "physics", 82.5, 78.5, "—"]
          - ["all", "chemistry", 82.0, 79.0, "—"]
    figures_description:
      - "Transfer matrix heatmap: 2x2 grid showing score degradation. Diagonal (same-domain) brighter, off-diagonal darker but not black — partial transfer."
    analysis: >
      ~40-50% routing knowledge 跨 domain 迁移，与 median 档 A4 (counterfactual labels 泛化中等) 一致。
      如果 4-page 紧张，这个实验可以仅在 results 最后一段用 2 句话概括。
      重要 insight：routing 的 domain-generic component 是 "detect state-change actions under uncertainty"，
      这个 framing 比 task-specific failure taxonomy 更 generalizable。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0adc366-912d-47ed-946a-8ed200c5e12c",
  "isSidechain": false,
  "requestId": "req_011CazpPrcaMHRkAomb8iTek",
  "type": "assistant",
  "uuid": "bef117fa-b062-4a07-81db-29188f680103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1Zp8CzWeE7E4vjzUbvDrk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7913,
      "cache_read_input_tokens": 26238,
      "output_tokens": 14819,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14819,
          "cache_read_input_tokens": 26238,
          "cache_creation_input_tokens": 7913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7913
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心假设部分成立：death avoidance 机制复现但无 positive guidance 信号，selective > unconditional 一致但幅度较小，explicit > implicit 成立但差距不大，整体分数接近但未超过 CogRouter 核心假设：['A1 death a…",
  "leafUuid": "bef117fa-b062-4a07-81db-29188f680103",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Define median-tier results for SimGate routing paper",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心假设部分成立：death avoidance 机制复现但无 positive guidance 信号，selective > unconditional 一致但幅度较小，explicit > implicit 成立但差距不大，整体分数接近但未超过 CogRouter 核心假设：['A1 death a…",
  "leafUuid": "bef117fa-b062-4a07-81db-29188f680103",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Define median-tier results for SimGate routing paper",
  "sessionId": "c2441971-e1a1-4afd-9cd0-5437ee84499f"
}
```

---
