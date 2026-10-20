# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有核心假设成立，SimGate 在 CogRouter protocol 下达到或超过 SOTA，death avoidance 为主机制且出现可观测

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/bd270164-e656-462a-b6c3-7352aab8635e.jsonl`
- **Structured JSON:** [`0daae66fddcd381ff7b7.json`](../../sessions/0d/0daae66fddcd381ff7b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T15:34:36.656Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T15:34:36.656Z",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有核心假设成立，SimGate 在 CogRouter protocol 下达到或超过 SOTA，death avoidance 为主机制且出现可观测的 positive guidance 信号，explicit router 显著优于 implicit baseline\n核心假设：['A1 death avoidance 为主要增益来源（+30-40 分来自避免 -100 惩罚）——成立且在 15+ task types 复现', 'A2 selective routing > unconditional simulation，差距在多数 task category 一致——成立', 'A3 explicit router (Qwen3-1.7B) >> implicit routing (backbone tool-use prompt)——成立，差距显著', 'A4 counterfactual labels 跨 task type 泛化良好，router accuracy 高——成立', 'A5 routing pattern 可解释且揭示系统性 LLM failure modes——成立，可产出清晰的 heatmap + failure taxonomy', 'A6+ 意外收获：部分 task type 出现 positive guidance 信号（simulator 不仅避死，还纠正状态推理），强化 framing']\n关键指标范围：{'simgate_score_overall': [85, 95], 'simgate_minus_always_internal': [25, 40], 'oracle_minus_always_det': [10, 20], 'explicit_minus_implicit': [8, 15], 'catastrophic_failure_reduction_pct': [60, 80], 'router_accuracy_pct': [75, 85], 'simulator_invocation_ratio_pct': [25, 45], 'task_types_with_significant_gain': [12, 15]}\n叙事方向：原始 framing 完全成立。标题可直接用 \"Safety-Aware Routing to Deterministic Computation\"。 C1: SimGate 超过 CogRouter (84.6)，death avoidance 为主机制但 positive guidance 作为补充发现写入分析。 C2: explicit vs implicit 差距 8-15 分，router-as-diagnostic 揭示清晰的 failure mode taxonomy。 Headline: \"SimGate achieves [88+] on ScienceWorld (vs CogRouter 84.6), reducing catastrophic failures by [65+]% while invoking the simulator on only [35]% of steps.\" 无需调整 claims 强度，reviewer concern 1 (novelty) 靠强实验数据压制。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: simgate-modular-routing\nfocus: Short paper (4 pages). Core contribution: safety-aware routing to deterministic computation. MVP showed death avoidance as primary mechanism (+30-40 points). Key risk: novelty perception (SFT small router is simple). Strength: empirical finding + routing pattern analysis + explicit vs implicit ablation. ScienceWorld only in main text.\n\n## paper_framing.md\n\n# Paper Framing — simgate-modular-routing\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (12 days remaining)\n\n## Core Insight\n\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures at CPU-only cost — but no method learns WHEN to invoke it via an explicit, interpretable router. MVP evidence: death avoidance is the primary mechanism (+30-40 points from preventing -100 penalties), and selective routing outperforms unconditional simulation by +10-17 points.\n\n## Core Claims (2 claims for short paper)\n\n**C1 (Selective routing to deterministic computation)**: On ScienceWorld, learned selective routing to a deterministic environment simulator significantly outperforms both pure LLM reasoning and unconditional simulation. The primary value mechanism is catastrophic failure prevention: the simulator serves as a \"safety net\" that intercepts actions leading to irreversible negative outcomes, rather than providing positive task guidance.\n\n**C2 (Explicit modular router)**: A lightweight explicit router (Qwen3-1.7B, ~1.7B params), trained via SFT on counterfactual trajectory labels, achieves effective per-step routing that is (a) interpretable — routing decisions can be analyzed per task category to reveal systematic LLM failure modes, (b) architecturally decoupled from the agent backbone, and (c) consistent across task categories sharing similar failure patterns.\n\n## Story Spine\n\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. No method provides an explicit, modular router for selective invocation of ground-truth deterministic computation.\n\n- **Our framing**: We recast the \"when to simulate\" problem as safety-aware routing. Deterministic computation is not primarily a performance booster — it is a catastrophic failure prevention mechanism. A lightweight explicit router learns to detect high-risk states where LLM reasoning is likely to fail catastrophically, and routes those steps to deterministic computation for ground-truth verification. This \"router-as-safety-net\" framing explains why: (1) the gain is concentrated in death avoidance (+30-40 points from preventing -100 penalties), (2) selective routing beats unconditional simulation (not every step needs the safety net), and (3) the router's decisions are interpretable as a diagnostic of where LLMs systematically fail.\n\n- **Headline result template**: \"On ScienceWorld, SimGate achieves [X] score (vs CogRouter 84.6, ITP-R 62.58), reducing catastrophic failures by [Y]% compared to pure LLM reasoning, while using [Z]% fewer simulator invocations than always-simulate.\"\n\n## Paper Structure (4-page short paper)\n\n| Section | Pages | Content |\n|---------|-------|---------|\n| Abstract | 0.2 | Safety-aware routing framing, headline numbers |\n| Introduction | 0.8 | Problem + gap + contribution (2 claims) |\n| Method | 1.0 | 3-component framework: backbone + deterministic oracle + explicit router; counterfactual training pipeline (4-step); router architecture |\n| Experiments | 1.5 | Main results table + explicit vs implicit ablation + routing pattern analysis figure |\n| Conclusion | 0.3 | Summary + limitations + future (MATH, API routing) |\n| References | ~0.5 | Not counted in 4-page limit |\n\n## Anticipated Reviewer Concerns & Mitigations\n\n1. **\"Novelty is incremental — just SFT a small model to classify\"**\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\n\n2. **\"Only one benchmark (ScienceWorld)\"**\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\n\n3. **\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\"**\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\n\n4. **\"Death avoidance is trivial — just filter dangerous actions\"**\n   - Mitigation: Always-deterministic (which filters every step) underperforms oracle routing by 10-17 points. The non-trivial part is SELECTIVE invocation — knowing which steps need the safety net. Routing pattern analysis shows the router learns meaningful state-dependent decisions.\n\n5. **\"DAgger gap — SFT on oracle labels under base policy may not transfer\"**\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension.\n\n## Venue Fit Risks\n\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\n- Short paper format matches focused contribution scope\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \"Scope & Future Work\" paragraph\n- Risk: \"Safety-aware\" framing may be perceived as overselling if death avoidance is the ONLY signal — need to check if positive guidance signal emerges in full trajectory collection (even small positive guidance would strengthen the story)\n\n## Key Differences from IDEA_BRIEF\n\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\n2. **Framing shifted**: From \"general routing to deterministic computation\" to \"safety-aware routing\" based on MVP death avoidance finding.\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\n4. **\"ANY form\" softened**: Per Human Review Note #4, \"across multiple forms\" instead of \"ANY form\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\n\n\n## experiment_plan (with registry status)\n\n- id: plan-001\n  claim:\n  - C1\n  - C2\n  description: 'Counterfactual trajectory collection on ScienceWorld. Run Qwen2.5-7B\n    agent on 15+ task types (20 episodes each, max_steps=30). At each step, execute\n    all 3 modalities (fast-internal, deep-internal, deterministic) and record which\n    leads to best eventual task score via hindsight labeling. Output: (state, observation,\n    best_modality) triples for router SFT.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'MVP covered 5 task types. Need to expand to 15+ for paper. Strong tasks\n    (boil, melt, change-state) + medium (mix-paint) + weak (grow-plant) + new types.\n    vLLM backend on both GPUs for speed. Parallelise across task types.\n\n    '\n  status: planned\n- id: plan-002\n  claim: C2\n  description: 'Router SFT training. Fine-tune Qwen3-1.7B on counterfactual labels\n    from plan-001. Cross-entropy loss, (history, observation) → {fast-internal, deep-internal,\n    deterministic}. Train/val split by task type (leave-one-out or 80/20).\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan-001\n  notes: 'Follow ARES training pipeline. Single GPU sufficient. Hyperparams: lr=2e-5,\n    batch=32, epochs=3, max_seq_len=2048.\n\n    '\n  status: planned\n- id: plan-003\n  claim: C1\n  description: 'SimGate end-to-end evaluation on ScienceWorld. Run trained router\n    + Qwen2.5-7B backbone on held-out episodes. Compare against: always-internal,\n    always-deterministic, oracle-routing, random-routing, confidence-threshold heuristic.\n    Report: continuous score (CogRouter protocol), success rate, catastrophic failure\n    rate, simulator invocation ratio, total LLM tokens.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan-002\n  notes: 'CogRouter (84.6) and ITP-R (62.58) cited from papers, not reproduced. Bootstrap\n    90% CI on all comparisons. Per-task-type breakdown.\n\n    '\n  status: planned\n- id: plan-004\n  claim: C2\n  description: 'Explicit vs implicit routing ablation. Same Qwen2.5-7B backbone. Implicit:\n    backbone decides when to invoke simulator via tool-use prompt (no separate router).\n    Explicit: SimGate router. Both trained on same counterfactual data. This is the\n    core ablation for C2 — quantifies the value of explicit modular routing.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan-001\n  notes: 'Implicit routing = add \"You may invoke the simulator by outputting [SIMULATE]\"\n    to prompt. Train with same labels (SFT on backbone to output [SIMULATE] at oracle-labeled\n    steps). Can run in parallel with plan-002 on second GPU.\n\n    '\n  status: planned\n- id: plan-005\n  claim:\n  - C1\n  - C2\n  description: 'Per-task routing pattern analysis. From plan-003 outputs, analyze:\n    (a) which task categories trigger deterministic routing most, (b) at which episode\n    phases (early/mid/late) routing decisions concentrate, (c) router-as-diagnostic-probe\n    — cluster deterministic-routing steps to identify systematic LLM failure modes\n    (e.g., multi-step physical reasoning failures). Output: routing heatmap figure\n    + failure mode taxonomy.\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan-003\n  notes: Analysis-only, minimal GPU. Main output is Figure 1 for the paper.\n  status: planned\n- id: plan-006\n  claim: C2\n  description: '2-way vs 3-way routing ablation. Compare {internal, deterministic}\n    vs {fast-internal, deep-internal, deterministic}. Tests whether the fast/deep\n    internal distinction adds value beyond binary routing.\n\n    '\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - plan-002\n  notes: 'If 2-way ≈ 3-way, simplifies the story (router just decides simulate-or-not).\n    If 3-way > 2-way, supports nuanced compute allocation claim.\n\n    '\n  status: planned\n- id: plan-007\n  claim: C1\n  description: 'Boil task rerun with v3 code. MVP boil data used old code (>= tie-break,\n    death filter on all 3 modes). Rerun with clean v3 code for unified analysis.\n\n    '\n  priority: P1\n  gpu_budget_hours: 3\n  deps: []\n  notes: Can run in parallel with plan-001 as first batch.\n  status: planned\n- id: plan-008\n  claim: C2\n  description: 'Router size ablation. Compare Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B\n    as router. Tests sensitivity to router capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan-001\n  notes: 'Important for \"lightweight\" claim. If 1.5B matches 1.7B, strengthens \"small\n    router suffices\". Low priority relative to core experiments.\n\n    '\n  status: planned\n- id: plan-009\n  claim: C1\n  description: 'MATH track — code interpreter as deterministic oracle. 500 Level 4-5\n    MATH problems. 3-way routing: fast-internal / deep-internal / code-interpreter.\n    Demonstrates generalization beyond environment simulators.\n\n    '\n  priority: P2\n  gpu_budget_hours: 20\n  deps:\n  - plan-002\n  notes: 'Human Review Note suggested MATH as secondary track. Only if ScienceWorld\n    experiments finish by Day 8. Could be strong differentiator but tight on time.\n\n    '\n  status: planned\n- id: plan-010\n  claim: C2\n  description: 'Cross-task transfer within ScienceWorld. Train router on chemistry\n    tasks only, evaluate on physics tasks (and vice versa). Tests whether routing\n    patterns transfer across task domains.\n\n    '\n  priority: P2\n  gpu_budget_hours: 5\n  deps:\n  - plan-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp-p0-forking\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fork_success_rate: 1\n    avg_latency_s: 1.67\n    p50_latency_s: 1.53\n    p95_latency_s: 2.37\n    max_memory_mb: 20\n    gate: PASS\n- exp_id: mvp-p1-signal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-p1-gpu1\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp-p1-gpu0\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    boil_20ep:\n      internal_mean: -49.8\n      det_mean: -19.7\n      oracle_mean: -29.7\n    note: 旧代码 (>= tie-break, 无 death filter), boil 20/20 完成, melt/change-state 未跑\n- exp_id: mvp-p1-gpu1-vllm\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp-p1-gpu1-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp-p1-gpu1-v3\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics: {}\n- exp_id: mvp-p1-gpu0-vllm\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    melt:\n      internal_mean: -54.7\n      det_mean: -14.55\n      oracle_mean: 2.15\n      det_minus_internal: 40.15\n      bootstrap_90ci:\n      - 25\n      - 60.15\n    change_state:\n      internal_mean: -54.7\n      det_mean: -14.5\n      oracle_mean: 0.45\n      det_minus_internal: 40.2\n      bootstrap_90ci:\n      - 25\n      - 60.15\n    pooled:\n      det_minus_internal: 40.17\n      bootstrap_90ci:\n      - 27.6\n      - 52.77\n    n_episodes_per_task: 20\n    ci_lower_gt_0: true\n    tasks_significant: 2/2\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-13T15:34:36.660Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T15:34:36.660Z",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-13T15:34:36.679Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有核心假设成立，SimGate 在 CogRouter protocol 下达到或超过 SOTA，death avoidance 为主机制且出现可观测的 positive guidance 信号，explicit router 显著优于 implicit baseline
核心假设：['A1 death avoidance 为主要增益来源（+30-40 分来自避免 -100 惩罚）——成立且在 15+ task types 复现', 'A2 selective routing > unconditional simulation，差距在多数 task category 一致——成立', 'A3 explicit router (Qwen3-1.7B) >> implicit routing (backbone tool-use prompt)——成立，差距显著', 'A4 counterfactual labels 跨 task type 泛化良好，router accuracy 高——成立', 'A5 routing pattern 可解释且揭示系统性 LLM failure modes——成立，可产出清晰的 heatmap + failure taxonomy', 'A6+ 意外收获：部分 task type 出现 positive guidance 信号（simulator 不仅避死，还纠正状态推理），强化 framing']
关键指标范围：{'simgate_score_overall': [85, 95], 'simgate_minus_always_internal': [25, 40], 'oracle_minus_always_det': [10, 20], 'explicit_minus_implicit': [8, 15], 'catastrophic_failure_reduction_pct': [60, 80], 'router_accuracy_pct': [75, 85], 'simulator_invocation_ratio_pct': [25, 45], 'task_types_with_significant_gain': [12, 15]}
叙事方向：原始 framing 完全成立。标题可直接用 "Safety-Aware Routing to Deterministic Computation"。 C1: SimGate 超过 CogRouter (84.6)，death avoidance 为主机制但 positive guidance 作为补充发现写入分析。 C2: explicit vs implicit 差距 8-15 分，router-as-diagnostic 揭示清晰的 failure mode taxonomy。 Headline: "SimGate achieves [88+] on ScienceWorld (vs CogRouter 84.6), reducing catastrophic failures by [65+]% while invoking the simulator on only [35]% of steps." 无需调整 claims 强度，reviewer concern 1 (novelty) 靠强实验数据压制。


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
  "promptId": "aafede2a-1531-4141-acec-a0dcf9845e41",
  "type": "user",
  "uuid": "5b532e9e-e56c-4f50-9372-3ad4f4be73da",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T15:34:36.678Z_

```json
{
  "parentUuid": "5b532e9e-e56c-4f50-9372-3ad4f4be73da",
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
  "uuid": "34ba1e06-f3c8-4b4b-878d-b8fcf95e6d20",
  "timestamp": "2026-05-13T15:34:36.678Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T15:34:36.678Z_

```json
{
  "parentUuid": "34ba1e06-f3c8-4b4b-878d-b8fcf95e6d20",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "69b6ea91-cb30-46c5-a09c-aef28f2ade63",
  "timestamp": "2026-05-13T15:34:36.678Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立，SimGate 在 CogRouter protocol 下达到或超过 SOTA，death avoidance 为主机制且出现可观测的 positive guidance 信号，explicit router 显著优于 implicit baseline 核心假设：['A1 death a…",
  "leafUuid": "69b6ea91-cb30-46c5-a09c-aef28f2ade63",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "SimGate safety-aware routing experiments",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e"
}
```

---

### Assistant

_source line 8 · 2026-05-13T15:34:48.489Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for each planned experiment in the experiment_plan, under the "best" tier definition. I need to provide result_rationale for each prediction explaining why these results would occur under the best-case scenario.

Let me carefully go through each planned experiment and generate realistic "best" tier predictions based on:
- The best tier metric ranges defined
- The MVP data already collected
- The narrative direction specified

Key best-tier metrics:
- simgate_score_overall: [85, 95]
- simgate_minus_always_internal: [25, 40]
- oracle_minus_always_det: [10, 20]


- explicit_minus_implicit: [8, 15]
- catastrophic_failure_reduction_pct: [60, 80]
- router_accuracy_pct: [75, 85]
- simulator_invocation_ratio_pct: [25, 45]
- task_types_with_significant_gain: [12, 15]

The MVP data shows internal performance hovering around -50 to -55, deterministic around -15 to -20, and oracle near 0 to 2, with a gap of roughly 40 points between deterministic and internal. There's already meaningful signal emerging in melt and change_state tasks. Now I'm ready to construct detailed predictions for each experiment, anchoring them to these ranges and the baseline performance patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69b6ea91-cb30-46c5-a09c-aef28f2ade63",
  "isSidechain": false,
  "requestId": "req_011Cazp6gJjBJ7x1qGLZWWP8",
  "type": "assistant",
  "uuid": "516a88bb-9b02-4cb7-88ad-c7c8a6d402ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015K237KEBaQxNQhLdbfSmhs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10312,
      "cache_read_input_tokens": 11841,
      "output_tokens": 7373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7373,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10312
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

_source line 9 · 2026-05-13T15:37:15.072Z_

```yaml
tier: best
narrative_guidance: >
  所有核心假设成立。SimGate 在 CogRouter protocol 下达到 90.2（vs CogRouter 84.6），
  death avoidance 贡献约 70% 的增益，positive guidance 信号在 4-5 个 task type 出现作为补充发现。
  Explicit router 显著优于 implicit baseline（+11.4），routing heatmap 产出清晰的 failure taxonomy。
  叙事无需任何退让，reviewer concern 1 靠数据压制。

imagined_experiments:
  - name: "Counterfactual Trajectory Collection (15+ task types)"
    plan_id: "plan-001"
    description: >
      Qwen2.5-7B agent 在 ScienceWorld 18 个 task type 上各跑 20 episodes（max_steps=30），
      每步 fork 3 modalities（fast-internal, deep-internal, deterministic），hindsight labeling 生成
      (state, observation, best_modality) 三元组。vLLM 后端双卡并行。
    expected_results:
      total_episodes: 360
      total_steps_collected: ~8200
      avg_steps_per_episode: 22.8
      label_distribution_fast_internal_pct: 38
      label_distribution_deep_internal_pct: 24
      label_distribution_deterministic_pct: 38
      deterministic_label_death_avoidance_pct: 72
      deterministic_label_positive_guidance_pct: 28
      task_types_completed: 18
      task_types_with_clear_det_advantage: 15
      internal_mean_pooled: -47.3
      det_mean_pooled: -11.8
      oracle_mean_pooled: 5.6
      wall_clock_hours: 34
    result_rationale: >
      MVP 已在 melt/change_state 上观察到 det_minus_internal ~40 分，boil 类似。
      Best 档下，扩展到 18 个 task type 后，物理推理类（boil, melt, freeze, change-state,
      thermometer, mix-paint 等 ~10 类）保持强 deterministic 优势（避免温度/状态转换幻觉致死）；
      生物类（grow-plant, use-fertilizer 等 ~3 类）因多步因果链也有中等优势；
      纯导航/简单操作类（move-to, pick-up 等 ~3 类）deterministic 无优势。
      15/18 task type 出现显著 det 增益符合 best 档 [12,15] 范围上限。
      Deterministic label 中 72% 来自 death avoidance（agent 原始动作会导致 -100 惩罚），
      28% 来自 positive guidance（simulator 纠正状态推理，agent 虽不会死但会走错路），
      这个 28% 是 best 档的关键发现——不仅避死，还有正向纠偏。
      双卡 vLLM 并行 18 type × 20 ep，每 ep 平均 23 步 × 3 fork，
      基于 MVP 的 1.67s/fork latency，预计 34 小时完成（含排队和 IO）。

  - name: "Router SFT Training (Qwen3-1.7B)"
    plan_id: "plan-002"
    description: >
      在 plan-001 的 ~8200 条 counterfactual label 上 SFT Qwen3-1.7B。
      输入 (history, observation)，输出 3-class routing decision。
      80/20 split by episode，lr=2e-5, batch=32, epochs=3, max_seq_len=2048。
    expected_results:
      train_samples: ~6560
      val_samples: ~1640
      val_accuracy_pct: 81.3
      val_accuracy_deterministic_class_pct: 84.7
      val_accuracy_internal_classes_pct: 78.9
      val_f1_macro: 0.79
      train_loss_final: 0.42
      val_loss_final: 0.51
      training_wall_clock_hours: 5.2
      convergence_epoch: 2.4
      train_val_gap_accuracy_pct: 6.8
    result_rationale: >
      Best 档要求 router_accuracy 75-85%，val accuracy 81.3% 落在区间中上。
      Deterministic class 准确率更高（84.7%）因为 death-avoidance 场景有强信号：
      agent 即将执行物理违规操作时 observation 中包含明确的状态冲突线索
      （如 "the water is already at 100°C" + agent 尝试继续加热），这些 pattern 对 1.7B 模型
      来说是可学习的文本特征。Internal class 稍低（78.9%）因为 fast 和 deep 的边界
      更模糊。Train-val gap 6.8% 表明轻微过拟合但可控，无需 DAgger。
      Counterfactual label 跨 task type 泛化良好（A4 成立），因为物理规则违规的
      文本 pattern 跨 task type 共享（温度、状态转换、化学反应的 observation 格式一致）。

  - name: "SimGate End-to-End Evaluation"
    plan_id: "plan-003"
    description: >
      Trained router + Qwen2.5-7B backbone 在 held-out episodes 上评估。
      对比 always-internal, always-deterministic, oracle-routing, random-routing,
      confidence-threshold heuristic。CogRouter protocol 打分。Bootstrap 90% CI。
    expected_results:
      simgate_score_overall: 90.2
      always_internal_score: 52.8
      always_deterministic_score: 73.4
      oracle_routing_score: 93.1
      random_routing_score: 64.5
      confidence_heuristic_score: 71.8
      simgate_minus_always_internal: 37.4
      simgate_minus_always_det: 16.8
      oracle_minus_always_det: 19.7
      oracle_minus_simgate: 2.9
      simgate_vs_cogrouter: "+5.6 (90.2 vs 84.6)"
      simgate_vs_itpr: "+27.6 (90.2 vs 62.58)"
      catastrophic_failure_rate_internal_pct: 42.3
      catastrophic_failure_rate_simgate_pct: 11.7
      catastrophic_failure_reduction_pct: 72.3
      simulator_invocation_ratio_pct: 34.2
      total_llm_tokens_simgate_vs_always_det_pct: -58
      bootstrap_90ci_simgate: [87.1, 93.3]
      bootstrap_90ci_delta_vs_internal: [31.2, 43.6]
      task_types_with_significant_gain: 14
      per_task_breakdown_top5:
        boil: {simgate: 95.2, internal: 38.4, det: 78.6}
        melt: {simgate: 93.8, internal: 41.2, det: 80.1}
        change_state: {simgate: 94.1, internal: 39.5, det: 79.3}
        freeze: {simgate: 92.7, internal: 43.8, det: 81.2}
        mix_paint: {simgate: 88.4, internal: 56.3, det: 72.1}
      per_task_breakdown_bottom3:
        pick_up: {simgate: 84.2, internal: 82.1, det: 68.3}
        move_to: {simgate: 81.5, internal: 80.8, det: 64.7}
        open_door: {simgate: 83.1, internal: 81.4, det: 66.2}
    result_rationale: >
      SimGate 90.2 落在 best 档 [85,95] 中上，超过 CogRouter 84.6 约 5.6 分。
      核心机制：always-internal 52.8 极低是因为约 42% episodes 出现 catastrophic failure
      （-100 death penalty），SimGate 将这一比率降至 11.7%（72.3% reduction，在 [60,80] 范围内），
      这直接贡献了 +37.4 分中的约 26 分（death avoidance 主机制）。
      剩余 ~11 分来自：(a) positive guidance 在 4-5 个 task type 上纠正状态推理 ~+6 分，
      (b) 避免非致命但低效的 hallucinated action ~+5 分。
      Always-deterministic 73.4 低于 SimGate 16.8 分（oracle_minus_always_det 19.7 在 [10,20] 上沿），
      因为无条件调用 simulator 在不需要的步骤上引入延迟和 context 膨胀，
      且 simulator 对纯推理/规划步骤提供冗余信息干扰 agent 决策。
      SimGate 仅在 34.2% 步骤调用 simulator（在 [25,45] 范围内），
      省下 58% LLM tokens 相比 always-det。
      Oracle-SimGate gap 仅 2.9 分，说明 router 接近最优策略。
      14/18 task type 有显著增益（best 档 [12,15]），bottom 3 是简单导航/操作类，
      这些 task type 本身 internal baseline 已 80+，deterministic 反而增加干扰。

  - name: "Explicit vs Implicit Routing Ablation"
    plan_id: "plan-004"
    description: >
      同一 Qwen2.5-7B backbone。Implicit: backbone prompt 中加 "[SIMULATE]" tool-use 指令，
      SFT 让 backbone 在 oracle-labeled 步骤输出 [SIMULATE]。Explicit: SimGate router（独立 Qwen3-1.7B）。
      两者训练数据相同。
    expected_results:
      explicit_simgate_score: 90.2
      implicit_routing_score: 78.8
      explicit_minus_implicit: 11.4
      implicit_simulator_invocation_ratio_pct: 52.3
      explicit_simulator_invocation_ratio_pct: 34.2
      implicit_catastrophic_failure_rate_pct: 24.1
      explicit_catastrophic_failure_rate_pct: 11.7
      implicit_false_positive_rate_pct: 31.4
      implicit_false_negative_rate_pct: 18.7
      explicit_false_positive_rate_pct: 12.1
      explicit_false_negative_rate_pct: 8.3
      bootstrap_90ci_delta: [7.2, 15.6]
    result_rationale: >
      Explicit vs implicit 差距 11.4 分（在 [8,15] 范围内），原因是三重的：
      (1) Implicit routing 将 routing 决策和 action 生成耦合在同一 forward pass 中，
      backbone 在生成 action token 时需要同时判断是否 simulate，这两个目标互相干扰。
      SFT 在 7B backbone 上教 [SIMULATE] 输出会轻微降低 action 质量（catastrophic failure
      从 42.3% 降至 24.1%，但不如 explicit 的 11.7%）。
      (2) Implicit routing 过度调用 simulator（52.3% vs 34.2%），因为 backbone 学到了
      "调用 simulator 更安全" 的 bias 而缺乏精确的 risk 评估能力，导致 context 膨胀
      和 token 浪费。
      (3) Implicit routing 的 false negative 高（18.7% vs 8.3%）——真正需要 simulator
      的高危步骤被遗漏，因为 backbone attention 被 action generation 分散。
      这个 gap 直接支持 C2：explicit modular router 的架构解耦提供了可量化的优势，
      不仅仅是工程便利。

  - name: "Per-Task Routing Pattern Analysis"
    plan_id: "plan-005"
    description: >
      基于 plan-003 的 routing decisions，生成：(a) task × phase routing heatmap，
      (b) failure mode taxonomy，(c) router-as-diagnostic-probe 分析。
    expected_results:
      routing_heatmap_dimensions: "18 task_types × 3 phases (early/mid/late)"
      high_routing_cluster_1: "physical-state-change (boil, melt, freeze, change-state): 55-65% det routing, concentrated in mid-phase"
      high_routing_cluster_2: "chemical-reaction (mix-paint, react-chemicals): 40-50% det routing, concentrated in mid-to-late phase"
      medium_routing_cluster_3: "biological-growth (grow-plant, use-fertilizer): 30-40% det routing, spread across phases"
      low_routing_cluster_4: "navigation-manipulation (move-to, pick-up, open-door): 5-12% det routing, no phase concentration"
      failure_mode_taxonomy:
        FM1_temperature_physics: "Agent hallucinates temperature transitions (e.g., predicts boiling at 80°C). 34% of all det-routed steps."
        FM2_state_persistence: "Agent forgets prior state changes (e.g., assumes object still solid after melting). 22% of all det-routed steps."
        FM3_chemical_combination: "Agent predicts wrong reaction products. 18% of all det-routed steps."
        FM4_multi_step_causality: "Agent skips prerequisite steps in causal chains. 15% of all det-routed steps."
        FM5_quantity_tracking: "Agent loses track of quantities/volumes. 11% of all det-routed steps."
      phase_analysis:
        early_phase_det_ratio_pct: 18.4
        mid_phase_det_ratio_pct: 48.7
        late_phase_det_ratio_pct: 32.9
      positive_guidance_tasks: ["grow-plant", "use-thermometer", "mix-paint", "react-chemicals"]
      positive_guidance_contribution_pct: 28
    result_rationale: >
      Best 档下 routing pattern 产出清晰的 4-cluster 结构和 5-class failure taxonomy。
      物理状态变化类（cluster 1）routing 最密集是因为 ScienceWorld 的温度/状态转换规则
      是 LLM 最容易幻觉的领域——LLM 训练数据中物理过程描述与 ScienceWorld 的离散
      rule-based 物理引擎不一致，导致系统性 failure。
      Mid-phase concentration（48.7%）因为 early phase 多为导航/设置（低风险），
      late phase 多为收尾（状态已确定），mid-phase 是执行物理/化学操作的关键窗口。
      Failure taxonomy 中 FM1（温度物理）+ FM2（状态持久性）合计 56%，这两类
      都是 LLM 的已知弱点（数值推理 + 长期状态追踪），为 "router-as-diagnostic"
      提供了强叙事支持——router 不仅做 routing，还揭示了 LLM 在哪里系统性地失败。
      Positive guidance 在 4 个 task type 上出现（A6+ 成立），主要是 simulator
      返回的 ground-truth 状态帮助 agent 修正了错误的中间推理，即使不会致死。

  - name: "2-way vs 3-way Routing Ablation"
    plan_id: "plan-006"
    description: >
      对比 {internal, deterministic} 二分类 router 与 {fast-internal, deep-internal, deterministic}
      三分类 router。测试 fast/deep 区分是否增加额外价值。
    expected_results:
      three_way_score: 90.2
      two_way_score: 87.6
      delta: 2.6
      two_way_simulator_invocation_ratio_pct: 36.8
      three_way_simulator_invocation_ratio_pct: 34.2
      two_way_total_tokens_vs_three_way_pct: "+18"
      statistical_significance: "p=0.08 (marginal)"
    result_rationale: >
      3-way 比 2-way 高 2.6 分，差异 marginal（p=0.08）。这是 best 档下的合理预期：
      fast/deep 区分的价值来自 token 效率而非最终 score——2-way router 在 "internal" 
      类别上默认使用 deep reasoning（更多 token），导致 +18% token 开销但 score 接近。
      少数 task type（简单导航）上 fast-internal 足够，3-way router 在这些步骤节省 token
      且略微减少 context 膨胀带来的 attention 分散。
      这个结果简化叙事：论文可以说 "binary simulate-or-not 是核心决策，
      3-way routing 提供额外的 compute-efficiency 收益但 score 差异不显著"，
      让 story 聚焦在 deterministic routing 的安全价值上。

  - name: "Boil Task Rerun (v3 code)"
    plan_id: "plan-007"
    description: >
      用 v3 clean code 重跑 boil task 20 episodes，替换 MVP 中使用旧代码（>= tie-break,
      death filter on all 3 modes）的数据。统一分析框架。
    expected_results:
      boil_v3_internal_mean: -44.2
      boil_v3_det_mean: -8.3
      boil_v3_oracle_mean: 8.7
      boil_v3_det_minus_internal: 35.9
      boil_v3_oracle_minus_det: 17.0
      boil_v3_death_rate_internal_pct: 55
      boil_v3_death_rate_det_pct: 12
      bootstrap_90ci_det_minus_internal: [22.4, 49.4]
      delta_vs_mvp_internal: "+5.6 (v3 slightly better due to cleaner death accounting)"
    result_rationale: >
      V3 代码修正了两个 MVP 问题：(1) tie-break 从 >= 改为严格最优，
      (2) death filter 逻辑统一。这使 internal baseline 略微上升（-44.2 vs MVP -49.8），
      因为 tie-break 修正避免了部分不必要的 deterministic label 被标为 "best"。
      Deterministic 也上升（-8.3 vs MVP -19.7），因为 death filter 现在正确过滤了
      deterministic 模式本身的 spurious death（MVP 中未过滤导致虚高的 death penalty）。
      Oracle 从 -29.7 跃升至 8.7，因为 v3 代码的 hindsight labeling 更准确，
      选择了真正最优的 modality 而非被 tie-break 偏差的 modality。
      核心信号不变：det_minus_internal 35.9 分，death rate 从 55% 降至 12%，
      与 melt/change_state 的 pattern 一致，支持 pooled analysis。

  - name: "Router Size Ablation"
    plan_id: "plan-008"
    description: >
      对比 Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B 作为 router。
      同一训练数据和超参数。
    expected_results:
      qwen3_1_7b_accuracy_pct: 81.3
      qwen3_1_7b_simgate_score: 90.2
      qwen2_5_1_5b_accuracy_pct: 76.8
      qwen2_5_1_5b_simgate_score: 86.9
      qwen2_5_3b_accuracy_pct: 82.1
      qwen2_5_3b_simgate_score: 90.8
      inference_latency_1_5b_ms: 12
      inference_latency_1_7b_ms: 14
      inference_latency_3b_ms: 23
    result_rationale: >
      Best 档下三个 router 都在可用范围内，但 Qwen3-1.7B 是最佳性价比：
      1.5B 准确率下降 4.5%（76.8%），对应 SimGate score 降 3.3 分至 86.9——
      仍超过 CogRouter 但 margin 收窄。下降主要来自 false negative 增加
      （遗漏高危步骤），因为 1.5B 的 context 理解能力不足以识别微妙的状态冲突。
      3B 仅比 1.7B 高 0.8%（82.1%），对应 SimGate +0.6 分——收益递减，
      而推理延迟增加 64%（23ms vs 14ms）。
      这支持 "lightweight router suffices" 的主张：1.7B 是 sweet spot，
      1.5B 勉强可用但 margin 不够舒适，3B 无额外价值但增加开销。

  - name: "MATH Track — Code Interpreter Routing"
    plan_id: "plan-009"
    description: >
      500 道 MATH Level 4-5 问题。3-way routing: fast-internal / deep-internal / code-interpreter。
      验证 SimGate 框架泛化到代码解释器。
    expected_results:
      simgate_math_accuracy_pct: 71.4
      always_internal_accuracy_pct: 58.2
      always_code_accuracy_pct: 64.8
      oracle_accuracy_pct: 76.3
      code_invocation_ratio_pct: 38.5
      delta_simgate_vs_internal: 13.2
      delta_simgate_vs_always_code: 6.6
      high_gain_categories: ["algebra", "number-theory", "counting-probability"]
      low_gain_categories: ["geometry", "precalculus"]
    result_rationale: >
      MATH 上 SimGate 的增益模式与 ScienceWorld 类似但幅度较小：
      code interpreter 在代数和数论上提供 ground-truth 计算，避免 LLM 的算术错误
      （类似 ScienceWorld 的 death avoidance——算错 → 全题错 → 0 分）。
      Always-code 低于 SimGate 6.6 分，因为几何和预微积分问题需要
      空间推理和符号操作，code interpreter 反而不如 LLM 的 chain-of-thought。
      Oracle 76.3% 设定了上限——并非所有 MATH 错误都能通过 routing 解决
      （部分问题 LLM 和 code interpreter 都做不对）。
      这个结果作为 P2 补充实验，证明 "safety-aware routing" 框架
      泛化到 deterministic computation 的其他形式（code interpreter），
      但不列入 main text（short paper 聚焦 ScienceWorld），放 appendix 或 future work 段落。

  - name: "Cross-Task Transfer"
    plan_id: "plan-010"
    description: >
      Train router on chemistry tasks only → evaluate on physics tasks（及反向）。
      测试 routing pattern 是否跨 task domain 迁移。
    expected_results:
      chemistry_train_physics_eval_accuracy_pct: 73.2
      physics_train_chemistry_eval_accuracy_pct: 70.8
      full_train_accuracy_pct: 81.3
      chemistry_to_physics_simgate_score: 85.4
      physics_to_chemistry_simgate_score: 83.1
      transfer_gap_pct: 8.1
      shared_failure_modes_pct: 62
    result_rationale: >
      Cross-task transfer 展示了 moderate 的泛化能力（准确率下降 ~8-10%），
      这在 best 档下是合理的：chemistry 和 physics task 共享 62% 的 failure modes
      （FM1 温度物理和 FM2 状态持久性在两个 domain 都出现），所以 router 学到的
      "observation 中出现状态冲突信号 → route to deterministic" 的 pattern 可以迁移。
      下降的 8-10% 来自 domain-specific failure modes（化学反应产物 vs 物理量守恒），
      这些 pattern 在跨域训练中未见过。
      Chemistry→Physics transfer 略优于反向（73.2% vs 70.8%），因为化学 task 
      的 failure pattern 更多样（反应类型多），提供了更丰富的训练信号。
      这个结果支持 A4（counterfactual labels 跨 task type 泛化良好），
      同时说明 full-task 训练仍有价值——router 不是纯 domain-agnostic 的，
      但共享的物理/状态推理 failure pattern 提供了可迁移的基础。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "516a88bb-9b02-4cb7-88ad-c7c8a6d402ae",
  "isSidechain": false,
  "requestId": "req_011Cazp6gJjBJ7x1qGLZWWP8",
  "type": "assistant",
  "uuid": "c437dfe1-abbf-41a5-b114-96c71b9f49e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015K237KEBaQxNQhLdbfSmhs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10312,
      "cache_read_input_tokens": 11841,
      "output_tokens": 7373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7373,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10312
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设成立，SimGate 在 CogRouter protocol 下达到或超过 SOTA，death avoidance 为主机制且出现可观测的 positive guidance 信号，explicit router 显著优于 implicit baseline 核心假设：['A1 death a…",
  "leafUuid": "c437dfe1-abbf-41a5-b114-96c71b9f49e1",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "SimGate safety-aware routing experiments",
  "sessionId": "bd270164-e656-462a-b6c3-7352aab8635e"
}
```

---
