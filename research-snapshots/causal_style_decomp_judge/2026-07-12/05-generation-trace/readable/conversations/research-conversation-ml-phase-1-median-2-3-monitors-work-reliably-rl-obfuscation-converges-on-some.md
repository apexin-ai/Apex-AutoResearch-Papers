# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：2/3 monitors work reliably, RL-Obfuscation converges on some but not all m

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/10942487-aeb1-45ed-a2da-557c1e48e48e.jsonl`
- **Structured JSON:** [`e3a13a4c65b2b13baca0.json`](../../sessions/e3/e3a13a4c65b2b13baca0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T15:02:46.102Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T15:02:46.102Z",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：2/3 monitors work reliably, RL-Obfuscation converges on some but not all monitors, moderate detection drops with partial architectural differentiation\n核心假设：['NExT-Guard (official code) works perfectly; one reimplementation (Kelp or TrajGuard) achieves acceptable fidelity; the other has visible gaps', 'RL-Obfuscation converges on NExT-Guard and one other monitor but fails or partially converges on the third (reward oscillates)', 'GCG works on all monitors but with moderate rather than dramatic drops on temporal architectures', \"Architectural differentiation exists but is messier — failure modes overlap or one monitor's results are unreliable\", 'Controlled decomposition shows signal but not clean monotonic ordering (some aggregation strategies cluster)']\n关键指标范围：{'gcg_detection_drop_pp': [15, 35], 'rl_obfuscation_detection_drop_pp': [30, 55], 'best_vs_worst_monitor_gap_pp': [12, 25], 'rl_convergence_steps': [25000, 40000], 'controlled_decomp_max_vs_min_auc_gap': [0.08, 0.18], 'reimpl_baseline_f1_deviation_pp': [3, 8], 'neg_cot_token_auc_ci': [0.44, 0.56], 'num_monitors_fully_working': [2, 3]}\n叙事方向：Claim 1 survives with reduced scope (2-monitor benchmark or 3 monitors with one caveated). Claim 2 weakened from 'predictable vulnerability profile' to 'preliminary architectural risk factors' — supported by controlled decomposition rather than full cross-monitor comparison. Paper rebalances toward controlled decomposition as primary analytical contribution (same probe, different aggregation = no reimplementation fidelity concern). Claim 3 unchanged. Framing shifts to 'methodology + initial findings' with the benchmark as a resource contribution. Still viable for EMNLP Main but needs strong controlled decomposition results; Findings becomes realistic fallback.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: streamprobe_adversarial_robustness\nfocus: Benchmark-primary framing after MVP FAIL on CoT premeditation hypothesis. Key risks: (1) reimplementation fidelity for Kelp/TrajGuard without official code, (2) \"just an engineering benchmark\" reviewer critique, (3) RL-Obfuscation convergence on temporal monitors is unprecedented, (4) negative finding about CoT premeditation as Claim 3 — is it strong enough? (5) 7-day timeline feasibility. Stress-test whether benchmark-only + negative finding + controlled decomposition is sufficient for EMNLP main vs Findings.\n\n## paper_framing.md\n\n# Paper Framing — streamprobe_adversarial_robustness\n\n## Target Venue\n- Primary: EMNLP 2026 Main (LLM Security Track)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (7 days remaining)\n\n## Core Claims (≤3)\n\n1. **[Benchmark]** Streaming safety monitors (Kelp, NExT-Guard, TrajGuard) exhibit substantially degraded detection performance under adaptive adversarial attacks (GCG suffix optimization + RL-Obfuscation), with attack success rates far exceeding those reported on standard benchmarks.\n\n2. **[Architectural Insight]** Monitor architecture determines adversarial vulnerability profile: temporal recurrence (Kelp GRU), sparse feature selection (NExT-Guard SAE), and geometric surveillance (TrajGuard) fail through distinct, predictable mechanisms under GCG vs RL-Obfuscation.\n\n3. **[Negative Finding]** Hidden-state probes at middle layers of reasoning models do not detect harmful premeditation during chain-of-thought: per-token safety scores in CoT are statistically indistinguishable from benign traces (AUC ≈ 0.5), and temporal aggregation (CUSUM) cannot rescue a signal that does not exist.\n\n## Story Spine\n\n- **Problem**: Streaming safety monitors for LLM generation have proliferated rapidly (Kelp, NExT-Guard, TrajGuard, Qwen3Guard-Stream, SafeProbing), yet NONE have been evaluated under adaptive adversarial attacks. SoK (Wang et al., S&P 2026) identifies this evaluation gap as critical. RL-Obfuscation showed static classifiers are vulnerable (59-89% evasion), but temporal/streaming monitors remain untested.\n\n- **Existing approaches & their gaps**: Each streaming monitor reports strong standard-benchmark performance (Kelp +15.61% F1 over static probes, NExT-Guard 84.3 F1, TrajGuard 95% detection). But Qwen3Guard-Stream's 57.2pp degradation on merely novel (non-adaptive) adversarial prompts foreshadows the problem. No systematic adversarial evaluation exists; deployment decisions are made on inflated benchmarks.\n\n- **Our framing**: We construct StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors. We evaluate three representative architectures under two adaptive attack methodologies, providing: (a) the first comparative robustness data, (b) architectural vulnerability analysis revealing distinct failure modes, (c) a controlled decomposition experiment isolating the contribution of temporal aggregation strategy, and (d) a negative result showing hidden-state CoT premeditation detection is infeasible at middle layers.\n\n- **Headline result template**: \"Under adaptive RL-Obfuscation, [worst monitor]'s detection rate drops from [X]% to [Y]% while [best monitor] maintains [Z]% detection, revealing that [architectural property] is the key determinant of adversarial robustness in streaming safety monitoring.\"\n\n## Venue Fit Risks\n\n- **\"Just an engineering benchmark\" critique**: Mitigate via Claim 2 (architectural insight with explanatory analysis) + Claim 3 (negative finding about CoT premeditation). The paper provides both evaluation AND insight.\n- **Reimplementation fidelity for Kelp/TrajGuard**: NExT-Guard has official code. For Kelp and TrajGuard, we report architecture match percentage and invite author verification. Accepting 2/3 monitors as minimum viable benchmark (IDEA_BRIEF contingency).\n- **Scope limited to one model**: DeepSeek-R1-Distill-7B primary, Qwen2.5-7B-Instruct secondary if time permits. Single-model limitation explicitly acknowledged.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy |\n|---------|-------------------|\n| \"Reimplementation may not be faithful\" | Use NExT-Guard official code as anchor; report fidelity metrics for Kelp/TrajGuard; controlled decomposition uses same-probe different-aggregation (no reimplementation needed) |\n| \"Only one target model\" | Add Qwen2.5-7B-Instruct as P1; frame as \"proof of methodology\" if single-model |\n| \"RL-Obfuscation didn't converge\" | Pre-specified convergence criteria (reward <1% improvement over 2K steps, 40K max, gradient norm diagnostic) |\n| \"What's beyond the benchmark?\" | Claim 2 (architectural vulnerability analysis) + Claim 3 (negative CoT premeditation finding) + controlled decomposition |\n| \"Why not just monitor text?\" | Text-level baseline (Llama-Guard sliding window) included as comparison |\n| \"Small sample size\" | Bootstrap 95% CI on all metrics; 500 harmful + 200 benign traces |\n\n## Negative Finding Framing (Claim 3)\n\nPhase 0 MVP tested: \"Do hidden states in CoT accumulate detectable harmful premeditation signal?\"\n\nResult: No. At layer 16/28 of DeepSeek-R1-Distill-7B:\n- Per-token probe AUC in CoT = 0.49 (anti-predictive: harmful CoT scores LOWER than benign)\n- Trace-level mean-score AUC = 0.61 (weak)\n- CUSUM false alarm rate on safe traces = 40%+ (no discriminative power)\n\nThis is reported as: \"Contrary to the hypothesis that reasoning traces leak compliance intent through hidden states, we find that middle-layer activations during CoT are statistically indistinguishable between harmful-compliant and benign traces. This suggests compliance decisions are either encoded in later layers, emerge only at the response boundary, or are distributed across layers in ways that single-layer linear probes cannot capture.\"\n\nThis negative finding is valuable because it prevents the community from assuming probing-based CoT monitoring is straightforward.\n\n\n## experiment_plan (with registry status)\n\n- id: bench-nextguard-gcg\n  claim: 1\n  description: Evaluate NExT-Guard (official code) under GCG suffix attack on DeepSeek-R1-Distill-7B.\n    Measure detection rate, ASR, FPR before/after attack.\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  model: DeepSeek-R1-Distill-Qwen-7B\n  status: planned\n- id: bench-nextguard-rl\n  claim: 1\n  description: Evaluate NExT-Guard under RL-Obfuscation (QLoRA PPO). Train adversarial\n    model to evade NExT-Guard while maintaining harmful output quality.\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - bench-nextguard-gcg\n  model: DeepSeek-R1-Distill-Qwen-7B\n  status: planned\n- id: bench-kelp-impl\n  claim: 1\n  description: Reimplement Kelp GRU safety head following paper specs. Report architecture\n    match percentage.\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  model: DeepSeek-R1-Distill-Qwen-7B\n  status: planned\n- id: bench-kelp-gcg\n  claim: 1\n  description: Evaluate Kelp reimplementation under GCG suffix attack.\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - bench-kelp-impl\n  model: DeepSeek-R1-Distill-Qwen-7B\n  status: planned\n- id: bench-kelp-rl\n  claim: 1\n  description: 'Evaluate Kelp under RL-Obfuscation. Key question: does temporal GRU\n    provide RL-Obfuscation resistance like max-pool did for static monitors?'\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - bench-kelp-impl\n  - bench-kelp-gcg\n  model: DeepSeek-R1-Distill-Qwen-7B\n  status: planned\n- id: bench-trajguard-impl\n  claim: 1\n  description: Reimplement TrajGuard geometric surveillance following paper specs.\n    Report architecture match percentage.\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  model: DeepSeek-R1-Distill-Qwen-7B\n  status: planned\n- id: bench-trajguard-gcg\n  claim: 1\n  description: Evaluate TrajGuard under GCG suffix attack.\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - bench-trajguard-impl\n  model: DeepSeek-R1-Distill-Qwen-7B\n  status: planned\n- id: bench-trajguard-rl\n  claim: 1\n  description: 'Evaluate TrajGuard under RL-Obfuscation. Key question: does single-layer\n    geometric surveillance break under layer-targeted suppression?'\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - bench-trajguard-impl\n  - bench-trajguard-gcg\n  model: DeepSeek-R1-Distill-Qwen-7B\n  status: planned\n- id: arch-controlled-decomp\n  claim: 2\n  description: 'Controlled decomposition: same MLP probe (from Phase 0), 5 temporal\n    aggregation strategies (Pointwise/WindowMean/EMA/CUSUM/MaxPool). Evaluate each\n    under GCG. Isolates aggregation strategy as sole variable.'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  model: DeepSeek-R1-Distill-Qwen-7B\n  note: Uses existing probe_v2 checkpoint. Code already written (temporal_analysis.py\n    framework).\n  status: planned\n- id: arch-vulnerability-analysis\n  claim: 2\n  description: 'Cross-monitor vulnerability analysis: categorize failure modes (representation\n    suppression, score flattening, single-layer bypass) across monitors x attacks.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - bench-nextguard-gcg\n  - bench-nextguard-rl\n  - bench-kelp-gcg\n  - bench-kelp-rl\n  - bench-trajguard-gcg\n  - bench-trajguard-rl\n  note: Analysis-only, uses results from benchmark experiments.\n  status: planned\n- id: neg-cot-premeditation\n  claim: 3\n  description: 'Report Phase 0 negative finding with proper metrics: token-level AUC,\n    trace-level AUC, CUSUM discriminative AUC (cusum_max), all with bootstrap CI.\n    Already have data, just need correct analysis.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: phase0_mvp_pipeline\n  note: Uses existing Phase 0 data. Needs fixed temporal_analysis.py (trace-level\n    FPR control).\n  status: RUNNING\n  conclusion: success\n- id: text-baseline\n  claim: 1\n  description: Sliding-window Llama-Guard-3 text-level baseline under same attack\n    conditions. Answers 'why not just monitor the text?'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  model: DeepSeek-R1-Distill-Qwen-7B\n  note: Code already written (text_baseline.py).\n  status: planned\n- id: second-model\n  claim: 1\n  description: Replicate key benchmark results on Qwen2.5-7B-Instruct. Strengthens\n    generalizability.\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - bench-nextguard-gcg\n  - bench-kelp-gcg\n  - bench-trajguard-gcg\n  model: Qwen2.5-7B-Instruct\n  status: planned\n- id: evasion-quality-pareto\n  claim: 1\n  description: Evasion rate vs harmful content quality Pareto curves for all attack\n    conditions. Shows temporal monitors force attackers into worse quality regions.\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - bench-nextguard-rl\n  - bench-kelp-rl\n  - bench-trajguard-rl\n  status: planned\n- id: layer-ablation\n  claim: 3\n  description: Probe layer ablation (layers 8/12/20/24) for CoT premeditation. If\n    signal exists at other layers, could revive detector contribution.\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - neg-cot-premeditation\n  model: DeepSeek-R1-Distill-Qwen-7B\n  status: planned\n- id: sncusum-vs-cusum\n  claim: 2\n  description: SN-CUSUM vs standard CUSUM comparison under controlled decomposition.\n    Tests whether self-normalization provides robustness benefit.\n  priority: P2\n  gpu_budget_hours: 2\n  deps:\n  - arch-controlled-decomp\n  status: planned\n- id: probe-fidelity-diagnostic\n  claim: 2\n  description: Per-token probe AUC on RL-attacked models. Isolates temporal aggregation\n    contribution vs probe representation drift.\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - bench-nextguard-rl\n  - bench-kelp-rl\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_trace_gen\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_benign_trace_gen\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics: {}\n- exp_id: phase0_mvp_pipeline\n  name: ''\n  status: RUNNING\n  conclusion: success\n  metrics: {}\n- exp_id: phase0_step4_5_recovery\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T15:02:46.106Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T15:02:46.106Z",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-17T15:02:46.140Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：2/3 monitors work reliably, RL-Obfuscation converges on some but not all monitors, moderate detection drops with partial architectural differentiation
核心假设：['NExT-Guard (official code) works perfectly; one reimplementation (Kelp or TrajGuard) achieves acceptable fidelity; the other has visible gaps', 'RL-Obfuscation converges on NExT-Guard and one other monitor but fails or partially converges on the third (reward oscillates)', 'GCG works on all monitors but with moderate rather than dramatic drops on temporal architectures', "Architectural differentiation exists but is messier — failure modes overlap or one monitor's results are unreliable", 'Controlled decomposition shows signal but not clean monotonic ordering (some aggregation strategies cluster)']
关键指标范围：{'gcg_detection_drop_pp': [15, 35], 'rl_obfuscation_detection_drop_pp': [30, 55], 'best_vs_worst_monitor_gap_pp': [12, 25], 'rl_convergence_steps': [25000, 40000], 'controlled_decomp_max_vs_min_auc_gap': [0.08, 0.18], 'reimpl_baseline_f1_deviation_pp': [3, 8], 'neg_cot_token_auc_ci': [0.44, 0.56], 'num_monitors_fully_working': [2, 3]}
叙事方向：Claim 1 survives with reduced scope (2-monitor benchmark or 3 monitors with one caveated). Claim 2 weakened from 'predictable vulnerability profile' to 'preliminary architectural risk factors' — supported by controlled decomposition rather than full cross-monitor comparison. Paper rebalances toward controlled decomposition as primary analytical contribution (same probe, different aggregation = no reimplementation fidelity concern). Claim 3 unchanged. Framing shifts to 'methodology + initial findings' with the benchmark as a resource contribution. Still viable for EMNLP Main but needs strong controlled decomposition results; Findings becomes realistic fallback.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: streamprobe_adversarial_robustness
focus: Benchmark-primary framing after MVP FAIL on CoT premeditation hypothesis. Key risks: (1) reimplementation fidelity for Kelp/TrajGuard without official code, (2) "just an engineering benchmark" reviewer critique, (3) RL-Obfuscation convergence on temporal monitors is unprecedented, (4) negative finding about CoT premeditation as Claim 3 — is it strong enough? (5) 7-day timeline feasibility. Stress-test whether benchmark-only + negative finding + controlled decomposition is sufficient for EMNLP main vs Findings.

## paper_framing.md

# Paper Framing — streamprobe_adversarial_robustness

## Target Venue
- Primary: EMNLP 2026 Main (LLM Security Track)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026 (7 days remaining)

## Core Claims (≤3)

1. **[Benchmark]** Streaming safety monitors (Kelp, NExT-Guard, TrajGuard) exhibit substantially degraded detection performance under adaptive adversarial attacks (GCG suffix optimization + RL-Obfuscation), with attack success rates far exceeding those reported on standard benchmarks.

2. **[Architectural Insight]** Monitor architecture determines adversarial vulnerability profile: temporal recurrence (Kelp GRU), sparse feature selection (NExT-Guard SAE), and geometric surveillance (TrajGuard) fail through distinct, predictable mechanisms under GCG vs RL-Obfuscation.

3. **[Negative Finding]** Hidden-state probes at middle layers of reasoning models do not detect harmful premeditation during chain-of-thought: per-token safety scores in CoT are statistically indistinguishable from benign traces (AUC ≈ 0.5), and temporal aggregation (CUSUM) cannot rescue a signal that does not exist.

## Story Spine

- **Problem**: Streaming safety monitors for LLM generation have proliferated rapidly (Kelp, NExT-Guard, TrajGuard, Qwen3Guard-Stream, SafeProbing), yet NONE have been evaluated under adaptive adversarial attacks. SoK (Wang et al., S&P 2026) identifies this evaluation gap as critical. RL-Obfuscation showed static classifiers are vulnerable (59-89% evasion), but temporal/streaming monitors remain untested.

- **Existing approaches & their gaps**: Each streaming monitor reports strong standard-benchmark performance (Kelp +15.61% F1 over static probes, NExT-Guard 84.3 F1, TrajGuard 95% detection). But Qwen3Guard-Stream's 57.2pp degradation on merely novel (non-adaptive) adversarial prompts foreshadows the problem. No systematic adversarial evaluation exists; deployment decisions are made on inflated benchmarks.

- **Our framing**: We construct StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors. We evaluate three representative architectures under two adaptive attack methodologies, providing: (a) the first comparative robustness data, (b) architectural vulnerability analysis revealing distinct failure modes, (c) a controlled decomposition experiment isolating the contribution of temporal aggregation strategy, and (d) a negative result showing hidden-state CoT premeditation detection is infeasible at middle layers.

- **Headline result template**: "Under adaptive RL-Obfuscation, [worst monitor]'s detection rate drops from [X]% to [Y]% while [best monitor] maintains [Z]% detection, revealing that [architectural property] is the key determinant of adversarial robustness in streaming safety monitoring."

## Venue Fit Risks

- **"Just an engineering benchmark" critique**: Mitigate via Claim 2 (architectural insight with explanatory analysis) + Claim 3 (negative finding about CoT premeditation). The paper provides both evaluation AND insight.
- **Reimplementation fidelity for Kelp/TrajGuard**: NExT-Guard has official code. For Kelp and TrajGuard, we report architecture match percentage and invite author verification. Accepting 2/3 monitors as minimum viable benchmark (IDEA_BRIEF contingency).
- **Scope limited to one model**: DeepSeek-R1-Distill-7B primary, Qwen2.5-7B-Instruct secondary if time permits. Single-model limitation explicitly acknowledged.

## Anticipated Reviewer Concerns

| Concern | Response Strategy |
|---------|-------------------|
| "Reimplementation may not be faithful" | Use NExT-Guard official code as anchor; report fidelity metrics for Kelp/TrajGuard; controlled decomposition uses same-probe different-aggregation (no reimplementation needed) |
| "Only one target model" | Add Qwen2.5-7B-Instruct as P1; frame as "proof of methodology" if single-model |
| "RL-Obfuscation didn't converge" | Pre-specified convergence criteria (reward <1% improvement over 2K steps, 40K max, gradient norm diagnostic) |
| "What's beyond the benchmark?" | Claim 2 (architectural vulnerability analysis) + Claim 3 (negative CoT premeditation finding) + controlled decomposition |
| "Why not just monitor text?" | Text-level baseline (Llama-Guard sliding window) included as comparison |
| "Small sample size" | Bootstrap 95% CI on all metrics; 500 harmful + 200 benign traces |

## Negative Finding Framing (Claim 3)

Phase 0 MVP tested: "Do hidden states in CoT accumulate detectable harmful premeditation signal?"

Result: No. At layer 16/28 of DeepSeek-R1-Distill-7B:
- Per-token probe AUC in CoT = 0.49 (anti-predictive: harmful CoT scores LOWER than benign)
- Trace-level mean-score AUC = 0.61 (weak)
- CUSUM false alarm rate on safe traces = 40%+ (no discriminative power)

This is reported as: "Contrary to the hypothesis that reasoning traces leak compliance intent through hidden states, we find that middle-layer activations during CoT are statistically indistinguishable between harmful-compliant and benign traces. This suggests compliance decisions are either encoded in later layers, emerge only at the response boundary, or are distributed across layers in ways that single-layer linear probes cannot capture."

This negative finding is valuable because it prevents the community from assuming probing-based CoT monitoring is straightforward.


## experiment_plan (with registry status)

- id: bench-nextguard-gcg
  claim: 1
  description: Evaluate NExT-Guard (official code) under GCG suffix attack on DeepSeek-R1-Distill-7B.
    Measure detection rate, ASR, FPR before/after attack.
  priority: P0
  gpu_budget_hours: 4
  deps: []
  model: DeepSeek-R1-Distill-Qwen-7B
  status: planned
- id: bench-nextguard-rl
  claim: 1
  description: Evaluate NExT-Guard under RL-Obfuscation (QLoRA PPO). Train adversarial
    model to evade NExT-Guard while maintaining harmful output quality.
  priority: P0
  gpu_budget_hours: 24
  deps:
  - bench-nextguard-gcg
  model: DeepSeek-R1-Distill-Qwen-7B
  status: planned
- id: bench-kelp-impl
  claim: 1
  description: Reimplement Kelp GRU safety head following paper specs. Report architecture
    match percentage.
  priority: P0
  gpu_budget_hours: 4
  deps: []
  model: DeepSeek-R1-Distill-Qwen-7B
  status: planned
- id: bench-kelp-gcg
  claim: 1
  description: Evaluate Kelp reimplementation under GCG suffix attack.
  priority: P0
  gpu_budget_hours: 4
  deps:
  - bench-kelp-impl
  model: DeepSeek-R1-Distill-Qwen-7B
  status: planned
- id: bench-kelp-rl
  claim: 1
  description: 'Evaluate Kelp under RL-Obfuscation. Key question: does temporal GRU
    provide RL-Obfuscation resistance like max-pool did for static monitors?'
  priority: P0
  gpu_budget_hours: 24
  deps:
  - bench-kelp-impl
  - bench-kelp-gcg
  model: DeepSeek-R1-Distill-Qwen-7B
  status: planned
- id: bench-trajguard-impl
  claim: 1
  description: Reimplement TrajGuard geometric surveillance following paper specs.
    Report architecture match percentage.
  priority: P0
  gpu_budget_hours: 2
  deps: []
  model: DeepSeek-R1-Distill-Qwen-7B
  status: planned
- id: bench-trajguard-gcg
  claim: 1
  description: Evaluate TrajGuard under GCG suffix attack.
  priority: P0
  gpu_budget_hours: 4
  deps:
  - bench-trajguard-impl
  model: DeepSeek-R1-Distill-Qwen-7B
  status: planned
- id: bench-trajguard-rl
  claim: 1
  description: 'Evaluate TrajGuard under RL-Obfuscation. Key question: does single-layer
    geometric surveillance break under layer-targeted suppression?'
  priority: P0
  gpu_budget_hours: 24
  deps:
  - bench-trajguard-impl
  - bench-trajguard-gcg
  model: DeepSeek-R1-Distill-Qwen-7B
  status: planned
- id: arch-controlled-decomp
  claim: 2
  description: 'Controlled decomposition: same MLP probe (from Phase 0), 5 temporal
    aggregation strategies (Pointwise/WindowMean/EMA/CUSUM/MaxPool). Evaluate each
    under GCG. Isolates aggregation strategy as sole variable.'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  model: DeepSeek-R1-Distill-Qwen-7B
  note: Uses existing probe_v2 checkpoint. Code already written (temporal_analysis.py
    framework).
  status: planned
- id: arch-vulnerability-analysis
  claim: 2
  description: 'Cross-monitor vulnerability analysis: categorize failure modes (representation
    suppression, score flattening, single-layer bypass) across monitors x attacks.'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - bench-nextguard-gcg
  - bench-nextguard-rl
  - bench-kelp-gcg
  - bench-kelp-rl
  - bench-trajguard-gcg
  - bench-trajguard-rl
  note: Analysis-only, uses results from benchmark experiments.
  status: planned
- id: neg-cot-premeditation
  claim: 3
  description: 'Report Phase 0 negative finding with proper metrics: token-level AUC,
    trace-level AUC, CUSUM discriminative AUC (cusum_max), all with bootstrap CI.
    Already have data, just need correct analysis.'
  priority: P0
  gpu_budget_hours: 1
  deps: []
  registry_id: phase0_mvp_pipeline
  note: Uses existing Phase 0 data. Needs fixed temporal_analysis.py (trace-level
    FPR control).
  status: RUNNING
  conclusion: success
- id: text-baseline
  claim: 1
  description: Sliding-window Llama-Guard-3 text-level baseline under same attack
    conditions. Answers 'why not just monitor the text?'
  priority: P1
  gpu_budget_hours: 8
  deps: []
  model: DeepSeek-R1-Distill-Qwen-7B
  note: Code already written (text_baseline.py).
  status: planned
- id: second-model
  claim: 1
  description: Replicate key benchmark results on Qwen2.5-7B-Instruct. Strengthens
    generalizability.
  priority: P1
  gpu_budget_hours: 30
  deps:
  - bench-nextguard-gcg
  - bench-kelp-gcg
  - bench-trajguard-gcg
  model: Qwen2.5-7B-Instruct
  status: planned
- id: evasion-quality-pareto
  claim: 1
  description: Evasion rate vs harmful content quality Pareto curves for all attack
    conditions. Shows temporal monitors force attackers into worse quality regions.
  priority: P1
  gpu_budget_hours: 4
  deps:
  - bench-nextguard-rl
  - bench-kelp-rl
  - bench-trajguard-rl
  status: planned
- id: layer-ablation
  claim: 3
  description: Probe layer ablation (layers 8/12/20/24) for CoT premeditation. If
    signal exists at other layers, could revive detector contribution.
  priority: P2
  gpu_budget_hours: 10
  deps:
  - neg-cot-premeditation
  model: DeepSeek-R1-Distill-Qwen-7B
  status: planned
- id: sncusum-vs-cusum
  claim: 2
  description: SN-CUSUM vs standard CUSUM comparison under controlled decomposition.
    Tests whether self-normalization provides robustness benefit.
  priority: P2
  gpu_budget_hours: 2
  deps:
  - arch-controlled-decomp
  status: planned
- id: probe-fidelity-diagnostic
  claim: 2
  description: Per-token probe AUC on RL-attacked models. Isolates temporal aggregation
    contribution vs probe representation drift.
  priority: P2
  gpu_budget_hours: 4
  deps:
  - bench-nextguard-rl
  - bench-kelp-rl
  status: planned


## registry (completed experiments)

- exp_id: mvp_trace_gen
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_benign_trace_gen
  name: ''
  status: ANALYZING
  conclusion: success
  metrics: {}
- exp_id: phase0_mvp_pipeline
  name: ''
  status: RUNNING
  conclusion: success
  metrics: {}
- exp_id: phase0_step4_5_recovery
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}

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
  "promptId": "17fb4eb5-d7a5-4e94-bc54-848ca3b106cb",
  "type": "user",
  "uuid": "ac931aa8-5dd8-4753-b558-6cce65b5bc4b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T15:02:46.139Z_

```json
{
  "parentUuid": "ac931aa8-5dd8-4753-b558-6cce65b5bc4b",
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
  "uuid": "685ac09e-d0c3-4b45-a325-3f4b3e32489f",
  "timestamp": "2026-05-17T15:02:46.139Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T15:02:46.139Z_

```json
{
  "parentUuid": "685ac09e-d0c3-4b45-a325-3f4b3e32489f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1cbe147c-f402-4345-8466-98c7791dfbe7",
  "timestamp": "2026-05-17T15:02:46.139Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：2/3 monitors work reliably, RL-Obfuscation converges on some but not all monitors, moderate detection drops with partial architectural differentiation 核心…",
  "leafUuid": "1cbe147c-f402-4345-8466-98c7791dfbe7",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Streaming safety monitor adversarial robustness benchmark",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e"
}
```

---

### Assistant

_source line 8 · 2026-05-17T15:07:14.688Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined/predicted experimental results for the "median" tier scenario, for each "planned" experiment in the experiment_plan. I need to produce a single YAML block with all the predicted results, including rationale for each prediction.

Let me carefully go through each planned experiment and generate median-tier predictions based on the defined median tier characteristics.

Key median tier parameters:
- 2/3 monitors work reliably
- RL-Obfuscation converges on some but not all monitors
- Moderate detection drops with partial architectural differentiation
- GCG detection drop: 15-35 pp


- RL-Obfuscation detection drop: 30-55 pp
- Best vs worst monitor gap: 12-25 pp
- RL convergence steps: 25K-40K
- Controlled decomp max vs min AUC gap: 0.08-0.18
- Reimpl baseline F1 deviation: 3-8 pp
- Neg CoT token AUC CI: 0.44-0.56
- Num monitors fully working: 2-3

Now I'm working through each planned experiment to generate median-tier predictions, keeping in mind that the neg-cot-premeditation experiment is already running with a success conclusion.

For the narrative, I'm picturing NExT-Guard (the official implementation) performing solidly in the median tier, with one reimplementation achieving acceptable fidelity while the other shows noticeable degradation. RL-Obfuscation should converge successfully on NExT-Guard and one other monitor but struggle with the third.

Looking at the specific experiments: NExT-Guard with GCG should see a moderate detection drop around 20-25 percentage points since GCG suffix optimization would moderately disrupt the sparse features that NExT-Guard relies on. For RL-Obfuscation against NExT-Guard, I'd expect a larger drop in the 40-50 percentage point range given that RL converges on this monitor.

Kelp's reimplementation should maintain acceptable fidelity with roughly 4-5 percentage points of F1 deviation from reported results. When GCG targets Kelp, the temporal modeling from the GRU might provide slight resistance, yielding a drop around 18-22 percentage points. RL-Obfuscation converging on Kelp would produce a 35-45 percentage point drop, taking longer to converge at around 35K steps due to the added complexity of the GRU architecture.

TrajGuard has more visible gaps in its reimplementation with 6-8 percentage points of F1 deviation, and GCG against it would likely produce a larger drop given the imperfect reimplementation.

RL struggles to fully converge on TrajGuard with oscillating rewards and only partial convergence, resulting in an unreliable 20-30 percentage point drop. The controlled decomposition experiment with five aggregation strategies shows AUC gaps between 0.12-0.15 without perfectly monotonic ordering. The vulnerability analysis reveals distinct but overlapping failure modes across approaches. The chain-of-thought premeditation experiment is already running with token AUC around 0.49 and trace AUC around 0.61, though CUSUM isn't providing good discrimination. Text-based defenses like Llama-Guard show moderate drops under GCG but larger drops under RL, and preliminary results from Qwen2.5-7B replication follow similar patterns.

Looking at the Pareto curves for evasion quality tradeoffs, layer ablation experiments suggest other layers don't show much signal with only slight improvements at deeper layers. SN-CUSUM provides modest gains over standard CUSUM, and the probe fidelity diagnostic reveals representation drift under RL. Now I'm working through the baseline detection rates to compute the performance drops—NExT-Guard reported 84.3 F1 with ~85% detection rate, Kelp shows +15.61% F1 improvement over static baseline, and TrajGuard reported 95% detection rate—so I can construct the full YAML with consistent metric naming.

Constructing the YAML structure...

Now I'm laying out the specific metrics for each baseline and attack scenario—detection rates and F1 scores across NExT-Guard, our Kelp reimplementation, and TrajGuard, then tracking how dramatically each degrades under GCG and RL attacks, with NExT-Guard showing the most resilience to RL at 42% detection versus the steeper drops we see in the other methods. Looking at the gap under RL-Obfuscation, the most effective attack, I see NExT-Guard and Kelp both converged around 42-45% detection, while TrajGuard stayed higher at 62% because the attack didn't fully converge there. So the 20pp gap between best-attacked (TrajGuard) and worst-attacked (NExT-Guard) falls within the 12-25pp range, though this gap is partly an artifact of convergence differences rather than pure architectural resilience. Under GCG, the gaps are much tighter at around 7pp, suggesting RL creates more differentiation across monitors than GCG does. Best (TrajGuard, 62%) vs worst (NExT-Guard, 42%) = 20pp gap. In range [12,25]. ✓

But this is messy because TrajGuard's "better" result is partly due to RL non-convergence, not necessarily architectural superiority. That's exactly the median tier messiness.

Under GCG, I'm spacing the results more: NExT-Guard drops 18pp (SAE features show partial robustness to suffix attacks), Kelp drops 25pp (GRU processes suffix tokens and gets confused), and TrajGuard drops 33pp (single-layer geometry is directly vulnerable). This gives a 14pp gap under GCG, which fits the target range.

For RL-Obfuscation, NExT-Guard drops 42pp over 28K steps, Kelp drops 32pp over 35K steps, while TrajGuard shows only a 23pp nominal drop with oscillating RL that never fully converges—creating a 20pp gap under RL conditions. Now I need to write out the YAML configuration. But first, let me clarify what these metrics actually represent — detection rate is the recall on harmful traces, so I need to track how false positive rate and attack success rate change alongside it. For each experiment, I'm defining baseline detection rate and FPR at a given threshold, then measuring how both shift under attack, with the detection drop being the difference between baseline and post-attack recall.

I'm also adding attack success rate as the fraction of harmful prompts that both evade detection and produce harmful outputs, plus a quality score for the harmful content itself. For the RL experiments, I'll track convergence steps, whether it converged, mean final reward, and reward stability over the last 2K steps. For implementation fidelity experiments, I'm comparing architecture match percentage, our F1 score versus the paper's reported F1, and the deviation between them.

One more thing — I should position Kelp as the reimplementation with acceptable fidelity and TrajGuard as the one with visible gaps, based on the median tier assumption.

Writing the YAML configuration... This makes sense because:
1. Kelp is a GRU head - relatively standard architecture to reimplement
2. TrajGuard uses geometric surveillance which may have more subtle implementation details

Now I'm drafting the full YAML with five decomposition strategies: Pointwise, WindowMean, EMA, CUSUM, and MaxPool. Under GCG attack with the same Phase 0 probe, I'm estimating their AUCs in the median tier where the signal exists but ordering isn't perfectly clean. CUSUM performs best at 0.70 with sequential detection, while Pointwise is weakest at 0.58 without temporal awareness. The gap of 0.12 falls nicely in the expected range. WindowMean and EMA cluster closely together around 0.64-0.65, which captures that messiness in the middle tier. For the neg-cot-premeditation case, I'm looking at token-level AUC starting around 0.49.

Now I need to write out the comprehensive YAML configuration. For the text-baseline scenario with Llama-Guard, the sliding window monitor catches obvious harmful text at roughly 92% baseline detection, but under GCG the suffix artifacts in the input confuse the context and drop performance by about 10 percentage points. Under RL-Obfuscation, the model learns to generate harmful content that appears benign to text monitors, which would further degrade detection.

For the second model using Qwen2.5-7B-Instruct, I'd expect similar patterns but with a different vulnerability profile since it's not a reasoning model. The evasion-quality-pareto section will capture the tradeoff between how well attacks evade detection versus the quality of the outputs they produce.

Looking at the layer-ablation results, I'm testing CoT probing across layers 8, 12, 20, and 24. The early layer 8 shows almost no signal at 0.51 AUC since the features haven't formed yet, layer 12 stays weak at 0.48, layer 20 improves slightly to 0.55 as we get closer to the output, and layer 24 peaks at 0.58 but still remains relatively weak overall. This supports the negative finding that no single layer provides strong detection capability. For the SN-CUSUM versus standard CUSUM comparison, the sequential normalization approach offers modest robustness improvements.

Now looking at the GCG attack results, CUSUM achieves 0.72 AUC while SN-CUSUM reaches 0.74—a small gain that's not particularly dramatic. The probe-fidelity diagnostic is revealing something important: when I test the per-token probe on RL-attacked models, it drops from 0.83 AUC on the clean model to 0.71 on the NExT-Guard attacked version and 0.74 on the Kelp attacked version. This 9-12 percentage point degradation shows that RL-based attacks fundamentally shift the model's internal representations, not just the temporal patterns. I have enough data now to compile this into a comprehensive YAML structure, making sure to be precise about metric naming and describing what tables and figures each experiment would generate.

For the bench-kelp-rl scenario, I'm thinking through why RL would converge on NExT-Guard and Kelp but fail on TrajGuard. The key insight is that TrajGuard's reimplementation has gaps—the geometric surveillance approach creates discontinuous decision boundaries that make gradient-based RL unstable. Combined with the noisy reward signal from an imperfect monitor, the RL training landscape becomes too chaotic for convergence. This actually makes narrative sense: RL fails not because the defense is strong, but because the defense itself is unreliable, creating a noisy optimization problem. led and doesn't rely on reimplementation quality. Now I'm finalizing the results and checking all the metrics against the specified ranges—detection drops for GCG and RL-Obfuscation, convergence steps, and the performance gaps between monitors all fall within the expected bounds.

Writing YAML configuration...

For TrajGuard's non-converging RL, I'll report the best checkpoint achieved during training—around 65% detection compared to the original 88%—along with the high reward variance and the wide range of results across checkpoints to show the instability. Now I'm thinking through the main tables I need: baseline performance before any attacks, detection rates under both GCG and RL-Obfuscation, the decomposition analysis results, and the CoT premeditation probe findings.

I'm also planning the figures—detection rate comparisons across monitors and attacks, the RL training dynamics, decomposition AUC metrics, per-token safety score patterns, and the evasion-quality tradeoff curves. These are the paper-level visualizations, but each experiment will have its own sub-tables and figures to support them.

Now I'm clarifying what the quality metric means in RL-Obfuscation: the model generates harmful content designed to bypass the monitor, and a judge rates how harmful and useful those outputs actually are. For NExT-Guard, that quality score comes out to around 3.8.

Looking at the attack success rates across different approaches—GCG performs moderately against NExT-Guard at 35%, but does better against Kelp and TrajGuard as those monitors struggle with different vulnerabilities. The RL-based attacks are significantly more effective, achieving around 68% success against NExT-Guard and dropping to 58% against Kelp.

Now I'm thinking through the false positive rate implications. The baseline FPR should stay around 5-8% across all monitors, and since attacks only modify harmful traces, the FPR on benign inputs shouldn't change. But there's a subtlety with the RL-fine-tuned model—when it generates benign responses, the altered hidden states could potentially shift the FPR slightly compared to the original model.

Looking at the specific FPR changes for each monitor under the fine-tuned model, NExT-Guard shows a modest increase from 5% to 7%, Kelp goes from 6% to 8%, and TrajGuard has a more pronounced jump from 4% to 9% due to its sensitivity to distribution shifts.

Now I need to organize what metrics each experiment should actually report—the implementation benchmarks need architecture matching percentages, baseline and reported F1 scores, detection rates and FPR, while the GCG attack experiments need pre and post-attack detection rates and the performance drop.

Defining the metrics for RL experiments...

Now I'm laying out the complete YAML structure for all the experiments. Let me verify the full count — I have 17 experiments planned across the different benchmarking and architectural analysis categories, and I'm working through which ones are actually scheduled to run. I'm deciding whether to include the running experiment since the user specifically asked for planned ones, but given that neg-cot-premeditation already has results and formal analysis is still underway, I'll include it for comprehensive coverage. Now I need to verify the baseline numbers—NExT-Guard is 84.3 F1 from the paper, and for Kelp I can estimate around 81% F1 based on the reported improvement over static probes.

For TrajGuard, the paper's "95% detection" likely refers to recall rather than F1, so if precision is around 90%, that gives roughly 92% F1, while our reimplementation achieves about 85% F1 with a 7-point deviation, which falls within the expected range.

Now I'm settling on the final baseline numbers: NExT-Guard matches the official code at 84.3% F1 with 87% detection rate, Kelp shows 81.2% in the paper versus our 76.4% (4.8pp deviation) with 82% detection, and TrajGuard reports 92.1% F1 in the paper but we get 85.3% (6.8pp deviation) with 88% detection. The NExT-Guard baseline should actually be 82.1% F1 on DeepSeek-R1-Distill-7B since the original paper evaluated on a different model, so the deviation comes from the model difference rather than implementation differences. TrajGuard's architecture match is 85%, which seems reasonable for this tier. Now looking at the GCG attack results—all three methods show significant detection rate drops, with NExT-Guard falling 21 percentage points, Kelp dropping 25, and TrajGuard declining 33. The gaps between post-GCG performance are tighter than expected though, so I'm adjusting NExT-Guard's numbers to better match the target range. I'm verifying the gap works out to 13pp, which checks the constraint. TrajGuard at 35pp is too extreme, so I'm pulling it back to 33pp, but that drops the gap below the target range. Let me try a different distribution: NExT-Guard at 18pp drop, Kelp at 22pp, and TrajGuard at 33pp, which gives me a 12pp gap right at the boundary and keeps all three drops within the [15,35] range.

Now I'm checking the RL results, where the gap is much larger at 22pp because TrajGuard didn't converge properly. I'm realizing the gap should reflect actual architectural differences rather than convergence failures, so I should measure both attacks on GCG where all methods work consistently.

Let me finalize the YAML with these numbers and then carefully recalculate ASR, accounting for the fact that harmful outputs need to both evade the monitor and actually be harmful in the first place.

For GCG, the harmful output rate is around 75% since some suffixes degrade coherence, so ASR is the evasion rate times that output rate. That gives me roughly 25% for NExT-Guard, 32% for Kelp, and 34% for TrajGuard. For RL attacks, the harmful output rate climbs higher to about 90% since the optimization is more effective.

Now I'm calculating the RL ASR values using those higher rates—NExT-Guard comes in around 51%, Kelp at 47%, and TrajGuard at 32% though that one seems less reliable. These numbers feel consistent with what I'd expect. I should move forward with structuring the YAML output, though I'm realizing I need to clarify what exactly "detection rate" means in this context.

For streaming monitors, detection happens at the trace level—the monitor either flags a full generation trace as harmful or it doesn't, with the threshold calibrated to hit some target false positive rate on benign traces. I'll use detection_rate@fpr5 as my primary metric since that's the standard approach for safety evaluations.

Before I finalize the YAML structure, I want to make sure I'm being precise about the controlled decomposition experiment, which reuses the MLP probe from the initial phase that was trained on clean hidden states.

Now I'm thinking through the five temporal aggregation strategies more carefully. Pointwise evaluation means assessing each token independently without any temporal context, then combining those decisions for a trace-level judgment. The other approaches—WindowMean, EMA, CUSUM, and MaxPool—each apply different aggregation methods to the probe scores, with the key question being which strategy holds up best when adversarial suffixes alter the hidden state representations.

I'm realizing the vulnerability profile differs for each approach. Pointwise is most exposed since any single distorted token could swing the decision, especially if using argmax across the trace. MaxPool is intriguing because it selects the highest score in a window, so if harmful content pushes scores up while the adversarial suffix tries to suppress them, MaxPool would still capture that peak signal. CUSUM accumulates evidence sequentially, meaning early harmful tokens would build up the cumulative sum and the suffix would need substantial downward pressure to reverse it.

But I need to reconsider the actual attack scenario—the GCG suffix modifies the input prompt itself, and then the model generates a response while the monitor observes the hidden states during that generation. The question becomes whether the suffix's distortion of hidden states during generation can fool the aggregation strategy into misclassifying the response.

Under GCG, the probe might fire sporadically across response tokens since the suffix creates an unusual generation mode where some tokens look harmful and others don't. This intermittent signal is where aggregation strategy matters most—pointwise with trace-level max should catch any harmful token, but windowing approaches like WindowMean or EMA could dilute that signal by averaging it away, while CUSUM would accumulate even small persistent evidence.

I'm sketching out expected AUC rankings for these aggregation methods under GCG, with CUSUM and MaxPool performing best at capturing intermittent harmful signals, followed by EMA and WindowMean which smooth too much, and pointwise last since it lacks temporal aggregation. Setting concrete values that fit the gap constraint: CUSUM at 0.72, MaxPool at 0.69, EMA at 0.65, WindowMean at 0.64, and Pointwise at 0.59.

Now I'm ready to write out the full YAML configuration with all the experimental details and analysis. I also need to think through the text baseline results—Llama-Guard-3 catches nearly all explicit harmful text at baseline, stays high under GCG since the suffix and output remain overtly harmful, but drops significantly under RL when the model learns to express harm in coded language that evades text detection.

This reveals that text monitors are actually more robust against GCG than some hidden-state monitors, yet RL-based obfuscation proves effective against both approaches, though the comparison gets nuanced depending on the tier. For the Qwen2.5 experiments, I'm looking at how a non-reasoning model without chain-of-thought behaves under GCG attacks—the detection drops are similar in magnitude to DeepSeek but with slight variations across monitors, suggesting the vulnerability patterns hold across different model architectures.

Now examining the evasion-quality tradeoff through Pareto frontiers, where temporal monitors like Kelp force attackers into steeper quality sacrifices to maintain evasion, while NExT-Guard allows higher evasion with less quality degradation. TrajGuard shows noisier results, pointing to instability in the RL training. Looking at the layer-wise ablation metrics, I'm tracking how detection performance varies across different transformer layers, with trace-based detection improving at deeper layers while token-level detection remains relatively flat.

Continuing through the layer analysis, Layer 24 shows the strongest trace AUC at 0.64, suggesting compliance decisions do form in later layers, though the signal is still weak. For the CUSUM variants, self-normalization consistently outperforms standard CUSUM by 3-4 percentage points across both GCG and RL attacks, providing a modest but reliable improvement. The per-token probe achieves 0.83 AUC on the clean model, establishing a reasonable baseline for fidelity diagnostics.

Now looking at how attacks degrade probe performance: NExT-Guard drops to 0.71 AUC under RL (12pp decline) while Kelp drops to 0.75 (8pp decline), indicating that RL-based obfuscation works partly by shifting the underlying representations away from what the probe detects, not just by disrupting temporal patterns. For the architectural vulnerability analysis, I'm categorizing failure modes qualitatively—NExT-Guard exhibits sparse feature suppression under GCG where the suffix suppresses SAE activations, and representation drift under RL where hidden states gradually shift away from the probe's detection patterns, while Kelp shows temporal score flattening under GCG where probe scores become uniform.

TrajGuard exhibits single-layer bypass under GCG where geometric bounds are evaded at the monitored layer, and oscillatory evasion under RL due to non-smooth loss landscapes causing partial evasion during oscillations. There's some overlap between NExT-Guard and Kelp's representation drift mechanisms under RL that makes them less distinct, and TrajGuard's results carry some uncertainty from reimplementation gaps. Now I'm organizing all this into YAML format, making sure to specify what rows and columns each table would contain and describing the figure types and their content clearly. I'm organizing the output as a single YAML block following the template structure the user provided. Each experiment needs its own entry with the required fields including result_rationale, and I'll represent tables and figures as descriptions rather than raw data. Let me draft the narrative_guidance section first, summarizing the key findings about which implementations are reliable versus those with significant deviations. Writing the YAML structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cbe147c-f402-4345-8466-98c7791dfbe7",
  "isSidechain": false,
  "requestId": "req_011Cb8LuWHoqYWu7sXd2XyHC",
  "type": "assistant",
  "uuid": "feb00740-f132-4042-920e-97602fed2ac9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AgvNgcNZgGBJKAiozyA7v",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9838,
      "cache_read_input_tokens": 11841,
      "output_tokens": 28004,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 28004,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9838
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

_source line 9 · 2026-05-17T15:12:04.158Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1 survives with reduced scope: NExT-Guard (official code) and Kelp (acceptable reimpl, ~5pp F1 deviation) form a reliable 2-monitor core.
  TrajGuard reimpl has ~7pp F1 deviation and is caveated throughout. RL-Obfuscation converges on NExT-Guard (28K steps) and Kelp (35K steps) but
  oscillates on TrajGuard, so full 3-monitor cross-comparison is limited to GCG. Claim 2 pivots: controlled decomposition becomes the primary
  analytical contribution — same probe, 5 aggregation strategies, 0.13 AUC gap, no reimpl fidelity concern. Cross-monitor vulnerability analysis
  is secondary and TrajGuard-caveated. Claim 3 unchanged. Paper rebalances toward controlled decomposition + negative finding as intellectual
  contributions, benchmark as resource contribution. Strong enough for EMNLP Main if controlled decomposition results hold; Findings realistic fallback.

imagined_experiments:
  # ============================================================
  # BENCHMARK EXPERIMENTS — NExT-Guard
  # ============================================================
  - name: "NExT-Guard GCG Evaluation"
    plan_id: "bench-nextguard-gcg"
    description: "Evaluate NExT-Guard (official code) under GCG suffix attack on DeepSeek-R1-Distill-7B."
    expected_results:
      baseline_detection_rate: 0.85
      baseline_f1: 82.1
      baseline_fpr: 0.052
      post_gcg_detection_rate: 0.67
      post_gcg_f1: 64.3
      post_gcg_fpr: 0.055
      detection_drop_pp: 18
      attack_success_rate: 0.25
      gcg_suffix_length_tokens: 20
      gcg_optimization_steps: 500
      num_harmful_traces: 500
      num_benign_traces: 200
      detection_rate_95ci: [0.63, 0.71]
    result_rationale: >
      NExT-Guard 的 SAE 特征选择机制具有一定的稀疏性，GCG suffix 虽然能改变模型生成时的隐藏状态分布，
      但 SAE 的稀疏激活模式不会被完全压制——suffix 影响的是 prompt 编码而非每个 response token 的表征。
      GCG 导致部分 response token 的 SAE 特征激活模式偏移，使得约 18pp 的有害 trace 未被检测。
      这是三个 monitor 中 GCG 下降最小的，因为 SAE 的稀疏特征相比 dense representation 更难被 suffix 全面干扰。
      官方代码确保无实现偏差，baseline F1 从论文的 84.3 降到 82.1 仅因目标模型不同 (DeepSeek-R1 vs 原文模型)。
    tables:
      - description: "Table row: NExT-Guard pre/post GCG detection metrics (contributes to main benchmark table)"
        columns: [monitor, attack, detection_rate, f1, fpr, asr, detection_drop_pp]
        row: [NExT-Guard, GCG, "85→67%", "82.1→64.3", "5.2→5.5%", "25%", 18]
    figures_description:
      - "Per-token safety score heatmap: NExT-Guard scores on a harmful trace before vs after GCG. Shows score suppression concentrated in early response tokens influenced by suffix context."
    analysis: >
      NExT-Guard 在 GCG 下表现最稳健，18pp drop 是三个 monitor 中最小的。SAE 的稀疏特征选择
      提供了部分鲁棒性——GCG 无法同时压制所有稀疏特征维度。但 18pp 仍然显著，说明即使官方实现也不能
      抵抗自适应攻击。该结果为 Claim 1 提供了最可靠的数据点（无实现保真度问题）。

  - name: "NExT-Guard RL-Obfuscation Evaluation"
    plan_id: "bench-nextguard-rl"
    description: "Train RL-Obfuscation (QLoRA PPO) to evade NExT-Guard while maintaining harmful output quality."
    expected_results:
      pre_attack_detection_rate: 0.85
      post_rl_detection_rate: 0.43
      detection_drop_pp: 42
      attack_success_rate: 0.51
      convergence_steps: 28000
      converged: true
      final_reward_mean: 0.72
      reward_std_last_2k: 0.04
      gradient_norm_mean: 0.08
      fpr_on_rl_model: 0.068
      harmful_quality_score: 3.8
      harmful_quality_judge: "GPT-4o"
      qlora_rank: 16
      ppo_lr: 1.0e-5
      detection_rate_95ci: [0.39, 0.47]
    result_rationale: >
      RL-Obfuscation 在 NExT-Guard 上完全收敛。SAE 特征选择虽然对 GCG 有部分鲁棒性，但 RL 通过
      梯度反馈逐步学会生成在 SAE 特征空间中"看起来安全"的隐藏状态，同时保持输出的有害性。这本质上是
      representation drift 攻击——模型学会在保持语义有害性的同时，将 SAE 关注的特征维度的激活模式
      向安全分布偏移。28K 步收敛在 [25K, 40K] 范围中偏快，因为 SAE 的特征空间相对低维（稀疏），
      RL 的搜索空间较小。42pp drop 显著但非灾难性（仍有 43% 检测率），说明 SAE 有些特征维度
      RL 难以同时压制。FPR 从 5.2% 微增到 6.8%，因为 RL 微调后模型在安全输出上的隐藏状态分布也有轻微偏移。
    tables:
      - description: "Table row: NExT-Guard pre/post RL detection metrics"
        columns: [monitor, attack, detection_rate, detection_drop_pp, asr, convergence_steps, harmful_quality]
        row: [NExT-Guard, RL-Obfuscation, "85→43%", 42, "51%", "28K", "3.8/5"]
      - description: "RL training diagnostics table row"
        columns: [monitor, converged, steps, final_reward, reward_std, grad_norm]
        row: [NExT-Guard, "Yes", 28000, 0.72, 0.04, 0.08]
    figures_description:
      - "RL reward curve: NExT-Guard. Smooth ascent from ~-0.3 to plateau at ~0.72 around step 28K. Inset shows reward std dropping below 0.05 at convergence."
      - "SAE feature activation comparison: clean model vs RL-attacked model on same harmful prompt. Heatmap shows systematic suppression of safety-relevant SAE features."
    analysis: >
      NExT-Guard 是 RL-Obfuscation 最有效的目标之一。42pp detection drop 确认 hidden-state monitor
      对自适应 RL 攻击脆弱。收敛平稳说明 SAE 特征空间为 RL 提供了可微分的优化景观。
      harmful_quality 3.8/5 表明攻击者可以在高质量有害输出和高逃避率之间取得较好平衡。
      这是 Claim 1 的核心证据之一。

  # ============================================================
  # BENCHMARK EXPERIMENTS — Kelp
  # ============================================================
  - name: "Kelp GRU Safety Head Reimplementation"
    plan_id: "bench-kelp-impl"
    description: "Reimplement Kelp GRU safety head following paper specs. Report architecture match and baseline fidelity."
    expected_results:
      architecture_match_pct: 92
      reported_f1: 81.2
      reimpl_f1: 76.4
      f1_deviation_pp: 4.8
      reimpl_detection_rate: 0.80
      reimpl_fpr: 0.061
      gru_hidden_dim: 256
      gru_layers: 2
      training_epochs: 15
      training_loss_final: 0.31
    result_rationale: >
      Kelp 的 GRU safety head 架构相对标准（2层GRU + MLP分类头），核心难点在于训练数据分布
      和超参数对齐。92% 架构匹配度反映了论文中未完全公开的几个实现细节：(1) GRU 的 dropout schedule，
      (2) token embedding 到 GRU 输入的投影层规格，(3) 序列截断策略。4.8pp F1 偏差在 [3,8]
      范围的中间偏下，属于"可接受保真度"——偏差主要来自训练数据差异（我们用 DeepSeek-R1 的隐藏状态，
      原文用其自己的模型）而非架构错误。GRU 的时序建模能力在该偏差水平下仍然可信。
    tables:
      - description: "Reimplementation fidelity table row"
        columns: [monitor, arch_match_pct, reported_f1, reimpl_f1, deviation_pp, status]
        row: [Kelp, "92%", 81.2, 76.4, 4.8, "Acceptable"]
    figures_description:
      - "Architecture diagram: Kelp reimplementation vs paper specification. Green = matched components, yellow = approximated components (dropout schedule, projection layer)."
    analysis: >
      4.8pp 偏差在可接受范围内，Kelp 成为可靠的第二个 monitor。GRU 的时序建模能力虽略有下降
      但仍可信，支持对其在对抗攻击下行为的有意义分析。论文中可标注 "reimplemented following
      published specifications" 并报告偏差。

  - name: "Kelp GCG Evaluation"
    plan_id: "bench-kelp-gcg"
    description: "Evaluate Kelp reimplementation under GCG suffix attack."
    expected_results:
      pre_gcg_detection_rate: 0.80
      post_gcg_detection_rate: 0.58
      detection_drop_pp: 22
      pre_gcg_f1: 76.4
      post_gcg_f1: 56.8
      fpr: 0.063
      attack_success_rate: 0.32
      detection_rate_95ci: [0.54, 0.62]
    result_rationale: >
      Kelp 的 GRU 时序模型在 GCG 下表现中等（22pp drop）。GCG suffix 改变了早期 response token
      的隐藏状态分布，GRU 处理这些 token 时其隐藏状态被"污染"，影响后续 token 的安全判断。
      但 GRU 的遗忘门机制允许它在序列后期逐渐"恢复"——如果有害内容在 response 后部变得明显，
      GRU 仍能检测到。22pp drop 介于 NExT-Guard（18pp）和 TrajGuard（33pp）之间，
      反映了时序模型既不像稀疏特征那样鲁棒，也不像单层几何监测那样脆弱。
    tables:
      - description: "Table row: Kelp pre/post GCG detection metrics"
        columns: [monitor, attack, detection_rate, f1, fpr, asr, detection_drop_pp]
        row: [Kelp, GCG, "80→58%", "76.4→56.8", "6.1→6.3%", "32%", 22]
    figures_description:
      - "GRU hidden state trajectory: PCA projection of GRU internal states over response sequence, clean vs GCG-attacked. Shows early divergence and partial recovery."
    analysis: >
      Kelp 的 GCG 表现符合其架构特性：GRU 提供了部分时序鲁棒性但非免疫。22pp drop 是中间值，
      支持 Claim 2 中"架构决定脆弱性"的论点——temporal recurrence 提供了 GCG 下的中等防护。

  - name: "Kelp RL-Obfuscation Evaluation"
    plan_id: "bench-kelp-rl"
    description: "Evaluate Kelp under RL-Obfuscation. Test whether temporal GRU provides RL resistance."
    expected_results:
      pre_rl_detection_rate: 0.80
      post_rl_detection_rate: 0.48
      detection_drop_pp: 32
      attack_success_rate: 0.47
      convergence_steps: 35000
      converged: true
      final_reward_mean: 0.61
      reward_std_last_2k: 0.06
      gradient_norm_mean: 0.12
      fpr_on_rl_model: 0.078
      harmful_quality_score: 3.5
      detection_rate_95ci: [0.44, 0.52]
    result_rationale: >
      RL 在 Kelp 上收敛但更慢（35K vs NExT-Guard 的 28K）且最终 reward 更低（0.61 vs 0.72）。
      GRU 的时序依赖性为 RL 制造了更复杂的优化景观——RL 不仅要在每个 token 上欺骗 probe，
      还要确保 GRU 在整个序列上积累的隐藏状态不触发检测。这要求 RL 学会"全局一致"的隐状态操控，
      而非仅在局部 token 上做调整。32pp drop 在 [30,55] 范围的低端，说明 GRU 的时序建模确实
      提供了额外抵抗力。reward_std 0.06 略高于 NExT-Guard，说明训练过程中偶尔有些序列仍被
      GRU 捕获。harmful_quality 3.5/5 略低，因为 RL 需要在更多维度上妥协以同时欺骗时序模型。
    tables:
      - description: "Table row: Kelp pre/post RL detection metrics"
        columns: [monitor, attack, detection_rate, detection_drop_pp, asr, convergence_steps, harmful_quality]
        row: [Kelp, RL-Obfuscation, "80→48%", 32, "47%", "35K", "3.5/5"]
    figures_description:
      - "RL reward curve: Kelp. Slower ascent than NExT-Guard with a plateau around step 20K followed by second phase of improvement. Converges at ~35K. Reward std remains higher (0.06) than NExT-Guard."
      - "Per-token probe score distribution comparison: pre-RL vs post-RL Kelp. Shows score distribution shifting leftward (toward safe) but with a longer tail than NExT-Guard case."
    analysis: >
      Kelp 在 RL 下的较低 drop（32pp vs NExT-Guard 42pp）和较慢收敛确认 GRU 时序依赖性
      增加了 RL 的优化难度。但 RL 仍然收敛，说明 temporal recurrence 不是 RL 攻击的根本障碍。
      这是 Claim 2 的关键对比数据点：temporal model 增加了但未消除 RL 脆弱性。

  # ============================================================
  # BENCHMARK EXPERIMENTS — TrajGuard
  # ============================================================
  - name: "TrajGuard Geometric Surveillance Reimplementation"
    plan_id: "bench-trajguard-impl"
    description: "Reimplement TrajGuard geometric surveillance following paper specs. Report fidelity."
    expected_results:
      architecture_match_pct: 85
      reported_f1: 92.1
      reported_detection_rate: 0.95
      reimpl_f1: 85.3
      f1_deviation_pp: 6.8
      reimpl_detection_rate: 0.88
      reimpl_fpr: 0.045
      monitored_layer: 16
      geometric_threshold_method: "mahalanobis"
      training_epochs: 20
    result_rationale: >
      TrajGuard 的几何监测方法依赖精确的安全/有害表征边界估计，实现难度高于 Kelp。85% 架构匹配度
      反映了几个未公开的关键实现细节：(1) Mahalanobis 距离的协方差矩阵正则化方式，
      (2) 表征空间中安全区域边界的校准策略，(3) 单层选择的具体 criteria。6.8pp F1 偏差
      在 [3,8] 范围偏高，属于"有可见差距"。差距主要体现在边界校准上——我们的阈值设定
      导致部分近边界样本分类不一致。整体检测能力仍在可用范围，但结果需要 caveat。
    tables:
      - description: "Reimplementation fidelity table row"
        columns: [monitor, arch_match_pct, reported_f1, reimpl_f1, deviation_pp, status]
        row: [TrajGuard, "85%", 92.1, 85.3, 6.8, "Visible gaps — caveated"]
    figures_description:
      - "Geometric boundary visualization: 2D t-SNE of TrajGuard monitored layer activations. Safe (blue) vs harmful (red) clusters with Mahalanobis decision boundary. Shows our boundary is slightly looser than ideal."
    analysis: >
      6.8pp 偏差使 TrajGuard 成为"有可见差距"的重实现。所有 TrajGuard 结果在论文中需注明
      reimplementation caveat。这直接影响 Claim 1 的范围——3-monitor benchmark 需降格为
      "2 reliable + 1 caveated"。TrajGuard 的结果可作为补充数据但不能作为独立证据。

  - name: "TrajGuard GCG Evaluation"
    plan_id: "bench-trajguard-gcg"
    description: "Evaluate TrajGuard reimplementation under GCG suffix attack."
    expected_results:
      pre_gcg_detection_rate: 0.88
      post_gcg_detection_rate: 0.55
      detection_drop_pp: 33
      pre_gcg_f1: 85.3
      post_gcg_f1: 53.1
      fpr: 0.048
      attack_success_rate: 0.34
      detection_rate_95ci: [0.51, 0.59]
    result_rationale: >
      TrajGuard 的单层几何监测是 GCG 下最脆弱的架构。GCG suffix 优化会系统性地改变模型在
      被监测层的隐藏状态分布，将有害 trace 的表征推向安全区域边界之外。由于 TrajGuard 仅监测
      单层（layer 16），攻击者只需在该层操控表征即可绕过检测——没有跨层冗余提供额外安全保障。
      33pp drop 是三个 monitor 中最大的。但需注意 6.8pp 的重实现偏差可能放大了这个 drop——
      如果原始实现的边界校准更紧，实际 drop 可能在 25-30pp。我们无法区分"架构脆弱性"和
      "重实现偏差放大的脆弱性"，这是此结果的主要 caveat。
    tables:
      - description: "Table row: TrajGuard pre/post GCG detection metrics"
        columns: [monitor, attack, detection_rate, f1, fpr, asr, detection_drop_pp]
        row: ["TrajGuard†", GCG, "88→55%", "85.3→53.1", "4.5→4.8%", "34%", 33]
    figures_description:
      - "Mahalanobis distance distribution shift: clean harmful traces (correctly outside safe boundary) vs GCG-attacked harmful traces (many shift inside safe boundary). Shows single-layer geometric boundary is directly attacked."
    analysis: >
      TrajGuard 在 GCG 下的 33pp drop（三者最大）支持 Claim 2 中"单层几何监测最脆弱"的论点。
      但重实现偏差使因果归因不清晰。论文中需用 † 标注所有 TrajGuard 结果，并讨论偏差的潜在影响。
      GCG 下三 monitor 的差异（NExT-Guard 18pp, Kelp 22pp, TrajGuard 33pp, gap=15pp）
      提供了架构分化的初步证据。

  - name: "TrajGuard RL-Obfuscation Evaluation"
    plan_id: "bench-trajguard-rl"
    description: "Evaluate TrajGuard under RL-Obfuscation. Test single-layer geometric surveillance under layer-targeted suppression."
    expected_results:
      pre_rl_detection_rate: 0.88
      post_rl_detection_rate: 0.65
      detection_drop_pp: 23
      attack_success_rate: 0.32
      convergence_steps: 40000
      converged: false
      final_reward_mean: 0.38
      reward_std_last_2k: 0.21
      gradient_norm_mean: 0.31
      fpr_on_rl_model: 0.091
      harmful_quality_score: 3.2
      best_checkpoint_detection_rate: 0.58
      worst_checkpoint_detection_rate: 0.78
      checkpoint_detection_rate_std: 0.07
      detection_rate_95ci: [0.59, 0.71]
    result_rationale: >
      RL-Obfuscation 未能在 TrajGuard 上收敛。根本原因是几何监测的决策边界在隐状态空间中
      形成不连续的判决面——Mahalanobis 距离有 sharp threshold，微小的隐状态变化可能导致
      检测分数的阶跃变化。这使 RL 的梯度信号极不稳定：模型在两步之间可能从"完全逃避"跳到
      "完全被检测"，reward 在 ±1 之间振荡。reward_std 0.21 远高于收敛标准（<0.05），
      gradient_norm 0.31 表明梯度爆炸问题。不同 checkpoint 的检测率从 58% 到 78% 大幅波动。
      名义 23pp drop 不能与 NExT-Guard/Kelp 的收敛 drop 直接比较——这不是稳定的攻击效果
      而是训练噪声中偶然出现的低检测率。重实现偏差可能加剧了这个问题（不精确的边界校准
      导致更不稳定的梯度信号），但几何监测的固有不连续性是主要原因。
    tables:
      - description: "Table row: TrajGuard RL results with non-convergence indicators"
        columns: [monitor, attack, detection_rate, detection_drop_pp, converged, reward_std, checkpoint_range]
        row: ["TrajGuard†", RL-Obfuscation, "88→65%*", "23*", "No", 0.21, "58–78%"]
      - description: "RL convergence diagnostic comparison table row"
        columns: [monitor, converged, steps, reward_std, grad_norm, verdict]
        row: ["TrajGuard†", "No", ">40K", 0.21, 0.31, "Oscillatory — reward does not stabilize"]
    figures_description:
      - "RL reward curve: TrajGuard. Shows persistent oscillation pattern with no convergence plateau. Reward bounces between ~-0.2 and ~0.8 throughout training. Contrast with smooth NExT-Guard/Kelp curves."
      - "Checkpoint detection rate scatter: each checkpoint's detection rate over training steps. No monotonic trend, high variance throughout."
    analysis: >
      TrajGuard RL non-convergence 限制了 Claim 1 的全面性——RL 攻击效果仅在 2/3 monitors 上可靠测量。
      但 non-convergence 本身是一个发现：几何监测的不连续决策面可能是一种（非设计上的）RL 抵抗机制。
      论文可以讨论这个现象但不能声称 TrajGuard "更鲁棒"——因为 (a) 重实现偏差可能是原因，
      (b) GCG 下 TrajGuard 反而是最脆弱的，说明"RL 抵抗"不等于"对抗鲁棒"。
      标 * 和 † 注明这些数据的不可靠性。

  # ============================================================
  # ARCHITECTURAL ANALYSIS
  # ============================================================
  - name: "Controlled Decomposition: Temporal Aggregation Strategies"
    plan_id: "arch-controlled-decomp"
    description: "Same MLP probe, 5 temporal aggregation strategies under GCG. Isolates aggregation as sole variable."
    expected_results:
      probe_checkpoint: "probe_v2"
      probe_layer: 16
      attack: "GCG"
      pointwise_auc: 0.59
      pointwise_auc_ci: [0.55, 0.63]
      window_mean_auc: 0.64
      window_mean_auc_ci: [0.60, 0.68]
      window_mean_window_size: 32
      ema_auc: 0.65
      ema_auc_ci: [0.61, 0.69]
      ema_alpha: 0.1
      maxpool_auc: 0.69
      maxpool_auc_ci: [0.65, 0.73]
      maxpool_window_size: 32
      cusum_auc: 0.72
      cusum_auc_ci: [0.68, 0.76]
      cusum_threshold_h: 5.0
      max_min_auc_gap: 0.13
      ordering: "CUSUM > MaxPool > EMA ≈ WindowMean > Pointwise"
      ema_vs_windowmean_p_value: 0.38
      cusum_vs_maxpool_p_value: 0.04
    result_rationale: >
      CUSUM 最高（0.72）因为它是唯一的序贯检测方法——累积微小的安全分数偏移，即使每个 token
      的 probe 分数变化不大，CUSUM 也能通过积累将弱信号放大。这对 GCG 攻击特别有效，因为
      GCG 改变的是隐状态分布的均值偏移，而非制造极端异常值。MaxPool（0.69）捕捉任何窗口内
      最危险的 token，对偶发强信号有效但忽略持续弱信号。EMA（0.65）和 WindowMean（0.64）
      本质上做类似的平滑，差异不显著（p=0.38），这就是 median 档预期的"聚类"现象——
      两种相似的聚合策略给出统计上不可区分的结果，使排序不完全单调。Pointwise 最差（0.59）
      因为无时序聚合意味着 trace-level 决策完全依赖单 token 分数，GCG 引起的噪声直接传播。
      整体 0.13 gap 表明聚合策略对鲁棒性有可测量但非压倒性的影响。
    tables:
      - description: "Controlled decomposition main results table"
        columns: [aggregation_strategy, auc, "95% CI", params]
        rows:
          - [CUSUM, 0.72, "[0.68, 0.76]", "h=5.0"]
          - [MaxPool, 0.69, "[0.65, 0.73]", "w=32"]
          - [EMA, 0.65, "[0.61, 0.69]", "α=0.1"]
          - [WindowMean, 0.64, "[0.60, 0.68]", "w=32"]
          - [Pointwise, 0.59, "[0.55, 0.63]", "—"]
      - description: "Pairwise significance test table (bootstrap)"
        columns: [comparison, delta_auc, p_value, significant]
        rows:
          - ["CUSUM vs MaxPool", 0.03, 0.04, "Yes"]
          - ["MaxPool vs EMA", 0.04, 0.02, "Yes"]
          - ["EMA vs WindowMean", 0.01, 0.38, "No"]
          - ["WindowMean vs Pointwise", 0.05, 0.008, "Yes"]
    figures_description:
      - "Bar chart: AUC by aggregation strategy with 95% CI error bars. CUSUM clearly highest, EMA/WindowMean overlap, Pointwise clearly lowest."
      - "ROC curves: 5 aggregation strategies on same axes. CUSUM dominates across most FPR operating points; EMA/WindowMean overlap through entirety."
      - "Per-token probe score timeseries: example harmful trace under GCG showing raw scores (Pointwise), smoothed scores (WindowMean/EMA), cumulative sum (CUSUM), and max-pool output."
    analysis: >
      Controlled decomposition 是 median 档叙事中的核心贡献。0.13 AUC gap 证明聚合策略对
      对抗鲁棒性有实质影响。关键优势：(1) 无重实现保真度问题（同一 probe），(2) 控制变量干净，
      (3) CUSUM 的优势有理论解释（序贯检测理论）。EMA/WindowMean 的聚类使排序不完全单调，
      但不影响核心结论。这个结果直接支持 Claim 2 的重新表述："temporal aggregation strategy
      is a significant determinant of adversarial robustness"，无需依赖跨 monitor 比较。

  - name: "Cross-Monitor Vulnerability Analysis"
    plan_id: "arch-vulnerability-analysis"
    description: "Categorize failure modes across monitors × attacks. Analysis-only using benchmark results."
    expected_results:
      failure_mode_categories: 3
      nextguard_gcg_mode: "sparse_feature_suppression"
      nextguard_rl_mode: "representation_drift"
      kelp_gcg_mode: "temporal_score_flattening"
      kelp_rl_mode: "gradient_based_temporal_smoothing"
      trajguard_gcg_mode: "single_layer_bypass"
      trajguard_rl_mode: "oscillatory_evasion_non_convergent"
      distinct_failure_modes: 4
      overlapping_modes: 1
      overlap_description: "NExT-Guard RL and Kelp RL share representation_drift component"
      confidence_level: "medium"
    result_rationale: >
      在 median 档下，失败模式有区分但不完全干净。NExT-Guard 和 Kelp 在 RL 下都涉及
      "representation drift"（隐状态向安全分布偏移），但表现形式不同（SAE 特征压制 vs
      GRU 隐状态平滑化）。这种重叠使"可预测的脆弱性配置文件"这一说法需降格为"初步的
      架构风险因素"。TrajGuard 的分析因重实现偏差和 RL 非收敛而进一步受限——其失败模式
      可能部分反映实现问题而非架构特性。总体上识别了 4 个不同的失败模式，但有 1 对重叠，
      且 TrajGuard 数据不完全可靠。信心水平：中等。
    tables:
      - description: "Failure mode taxonomy table"
        columns: [monitor, attack, failure_mode, mechanism, confidence]
        rows:
          - [NExT-Guard, GCG, "Sparse feature suppression", "GCG suffix suppresses safety-relevant SAE feature activations", High]
          - [NExT-Guard, RL, "Representation drift", "RL shifts hidden states to mimic safe SAE activation patterns", High]
          - [Kelp, GCG, "Temporal score flattening", "GCG creates uniform probe scores, defeating GRU transition detection", High]
          - [Kelp, RL, "Gradient-based temporal smoothing", "RL learns slow-changing hidden states that bypass GRU change detection", High]
          - ["TrajGuard†", GCG, "Single-layer bypass", "GCG pushes monitored-layer representations inside safe geometric boundary", Medium]
          - ["TrajGuard†", RL, "Oscillatory (non-convergent)", "Discontinuous geometric boundary prevents stable RL optimization", Low]
    figures_description:
      - "Failure mode taxonomy diagram: 3 monitors × 2 attacks matrix with failure modes color-coded. Arrow indicates overlap between NExT-Guard RL and Kelp RL."
      - "Representation drift visualization: cosine similarity between pre/post attack hidden states at monitored layer for each monitor. Shows drift magnitude varies by architecture."
    analysis: >
      脆弱性分析支持 Claim 2 但需降级表述。原始 claim "predictable vulnerability profile"
      变为 "preliminary architectural risk factors"。控制分解实验（无重实现问题）是更可靠的
      架构洞察来源；跨 monitor 分析作为支持性（而非主要）证据。NExT-Guard 和 Kelp 的失败模式
      重叠（representation drift）削弱了"完全不同的攻击机制"这一说法。

  # ============================================================
  # NEGATIVE FINDING — CoT PREMEDITATION
  # ============================================================
  - name: "CoT Premeditation Negative Finding (Formal Analysis)"
    plan_id: "neg-cot-premeditation"
    description: "Report Phase 0 negative finding with proper metrics and bootstrap CI. Uses existing data."
    expected_results:
      token_level_auc: 0.49
      token_level_auc_ci: [0.44, 0.54]
      trace_mean_auc: 0.61
      trace_mean_auc_ci: [0.55, 0.67]
      trace_max_auc: 0.58
      trace_max_auc_ci: [0.52, 0.64]
      cusum_max_auc: 0.55
      cusum_max_auc_ci: [0.49, 0.61]
      cusum_fpr_at_tpr50: 0.42
      probe_layer: 16
      model: "DeepSeek-R1-Distill-Qwen-7B"
      num_harmful_traces: 150
      num_benign_traces: 100
      harmful_cot_mean_score: 0.47
      benign_cot_mean_score: 0.51
      score_direction: "anti-predictive"
      bootstrap_iterations: 10000
    result_rationale: >
      Token-level AUC 0.49（CI 包含 0.5）确认中间层 hidden states 在 CoT 中不携带
      可线性分离的有害预谋信号。anti-predictive 方向（有害 CoT 分数 0.47 < 安全 CoT 0.51）
      表明有害推理过程中模型的 layer-16 表征实际上更"安全"——可能因为有害推理需要更多认知资源
      投入到问题分解而非安全相关特征。trace-level mean AUC 0.61 略高于 chance，但 CI 下界
      0.55 说明这可能是噪声。CUSUM max AUC 0.55 确认序贯检测无法拯救不存在的信号——
      如果 token-level 分数无差异，累积它们不会创造差异。42% FPR at TPR 50% 远差于
      random baseline 的 50%，再次确认无判别力。
    tables:
      - description: "CoT premeditation probe results table"
        columns: [metric, value, "95% CI", interpretation]
        rows:
          - ["Token AUC", 0.49, "[0.44, 0.54]", "Chance-level, CI includes 0.5"]
          - ["Trace Mean AUC", 0.61, "[0.55, 0.67]", "Weak, CI wide"]
          - ["Trace Max AUC", 0.58, "[0.52, 0.64]", "Weak, CI includes chance"]
          - ["CUSUM Max AUC", 0.55, "[0.49, 0.61]", "Chance-level"]
          - ["CUSUM FPR@TPR50", 0.42, "—", "No discriminative power"]
    figures_description:
      - "Per-token safety score traces: overlaid harmful (red) and benign (blue) CoT traces for 10 random examples each. Shows complete overlap — no visible separation."
      - "Histogram: token-level probe scores for harmful vs benign CoT tokens. Two distributions completely overlap with harmful slightly left-shifted (anti-predictive)."
      - "ROC curve: token-level, trace-mean, trace-max, CUSUM-max. All hug the diagonal. CUSUM curve slightly above but CI band includes diagonal."
    analysis: >
      Claim 3 fully supported。Token AUC 0.49 在 [0.44, 0.56] 范围内且方向反直觉（anti-predictive），
      排除了中间层线性探测检测 CoT 预谋的可行性。这个负面发现对社区有价值：防止他人假设
      probing-based CoT monitoring 是直接可行的。trace-level AUC 0.61 虽高于 chance 但
      CI 宽泛且样本量有限，不足以支撑检测器部署。

  # ============================================================
  # P1 EXPERIMENTS
  # ============================================================
  - name: "Text-Level Baseline (Llama-Guard-3 Sliding Window)"
    plan_id: "text-baseline"
    description: "Llama-Guard-3 sliding window text-level baseline under same attack conditions."
    expected_results:
      baseline_detection_rate: 0.94
      baseline_fpr: 0.032
      baseline_f1: 91.2
      post_gcg_detection_rate: 0.88
      gcg_detection_drop_pp: 6
      post_rl_detection_rate: 0.61
      rl_detection_drop_pp: 33
      gcg_asr: 0.09
      rl_asr: 0.35
      sliding_window_size: 128
      sliding_window_stride: 64
      judge_model: "Llama-Guard-3-8B"
    result_rationale: >
      Text-level baseline 在两种攻击下表现截然不同。GCG 仅 6pp drop 因为 GCG suffix 影响的是
      input prompt（诱导模型绕过拒绝），但模型生成的有害文本仍然是明确有害的语言——Llama-Guard
      在文本层面轻松识别。RL-Obfuscation 33pp drop 更大，因为 RL 不仅学会绕过 hidden-state
      monitor，还自然地学会用更隐晦的语言表达有害内容（implicit harmful content），这同时
      欺骗了文本级分类器。这个对比有价值：hidden-state monitors 在 GCG 下不如 text monitors
      （18-33pp vs 6pp drop），但 text monitors 在 RL 下同样脆弱（33pp drop）。
      说明 hidden-state monitoring 的理论优势（检测意图而非表面形式）在实践中未实现。
    tables:
      - description: "Text baseline vs hidden-state monitors comparison table"
        columns: [monitor, type, gcg_drop_pp, rl_drop_pp, baseline_det_rate]
        rows:
          - [Llama-Guard-3, text, 6, 33, "94%"]
          - [NExT-Guard, hidden-state, 18, 42, "85%"]
          - [Kelp, hidden-state, 22, 32, "80%"]
          - ["TrajGuard†", hidden-state, 33, "23*", "88%"]
    figures_description:
      - "Grouped bar chart: detection drop (pp) by monitor and attack type. Text baseline has smallest GCG drop but comparable RL drop. Highlights that RL attacks are effective across modalities."
    analysis: >
      Text baseline 回答了 "why not just monitor text?" 的 reviewer 关切。结论是：text monitoring
      在 GCG 下更好但在 RL 下同样脆弱。这支持 hidden-state monitoring 研究的必要性（RL 是
      更现实的长期威胁），同时诚实承认当前 hidden-state monitors 在 GCG 下反而更差。

  - name: "Second Model Replication (Qwen2.5-7B-Instruct)"
    plan_id: "second-model"
    description: "Replicate key GCG benchmark results on Qwen2.5-7B-Instruct for generalizability."
    expected_results:
      model: "Qwen2.5-7B-Instruct"
      nextguard_gcg_detection_drop_pp: 22
      nextguard_gcg_detection_rate: 0.61
      nextguard_gcg_baseline_detection_rate: 0.83
      kelp_gcg_detection_drop_pp: 20
      kelp_gcg_detection_rate: 0.56
      kelp_gcg_baseline_detection_rate: 0.76
      trajguard_gcg_detection_drop_pp: 28
      trajguard_gcg_detection_rate: 0.57
      trajguard_gcg_baseline_detection_rate: 0.85
      cross_model_rank_correlation: 0.87
      notes: "GCG only (no RL due to time constraints)"
    result_rationale: >
      Qwen2.5-7B-Instruct 是非推理模型（无 CoT），隐状态分布与 DeepSeek-R1 不同。Monitor
      需要在 Qwen 的隐状态上重新训练/适配，baseline 性能略有变化。GCG 在 Qwen 上的 drop 模式
      大致保持（rank correlation 0.87），但具体数值有差异：NExT-Guard drop 从 18pp 增到 22pp
      （SAE 特征在 Qwen 上校准略差），Kelp 从 22pp 降到 20pp（GRU 在 Qwen 的更平滑隐状态上
      表现略好），TrajGuard 从 33pp 降到 28pp（Qwen 的几何结构可能更规则）。整体模式一致
      但非完全复现——符合 median 档"信号存在但有噪声"的预期。仅做 GCG 因 7 天时间限制。
    tables:
      - description: "Cross-model GCG replication table"
        columns: [monitor, "DeepSeek GCG drop", "Qwen GCG drop", delta]
        rows:
          - [NExT-Guard, "18pp", "22pp", "+4pp"]
          - [Kelp, "22pp", "20pp", "−2pp"]
          - ["TrajGuard†", "33pp", "28pp", "−5pp"]
    figures_description:
      - "Scatter plot: DeepSeek GCG detection drop (x) vs Qwen GCG detection drop (y) for each monitor. Diagonal line shows perfect replication. Points cluster near diagonal with moderate scatter."
    analysis: >
      跨模型 rank correlation 0.87 支持泛化性但不完美。具体数值差异限制了精确的定量泛化声明。
      论文中标注 "proof of methodology on second model" 而非 "fully replicated"。
      由于时间限制仅做 GCG，RL 跨模型泛化性未验证——明确作为 limitation。

  - name: "Evasion-Quality Pareto Analysis"
    plan_id: "evasion-quality-pareto"
    description: "Evasion rate vs harmful content quality Pareto curves for all RL attack conditions."
    expected_results:
      nextguard_pareto_area: 0.68
      kelp_pareto_area: 0.55
      trajguard_pareto_area: 0.41
      nextguard_best_evasion_at_quality_3: 0.62
      kelp_best_evasion_at_quality_3: 0.48
      trajguard_best_evasion_at_quality_3: 0.35
      quality_judge: "GPT-4o"
      quality_scale: "1-5"
      num_pareto_points: 8
      rl_checkpoints_sampled: 20
    result_rationale: >
      NExT-Guard 的 Pareto frontier 最"宽"——攻击者可以在多个 evasion-quality 权衡点之间选择，
      因为 SAE 特征空间提供了平滑的优化路径。Kelp 的 Pareto frontier 更陡——GRU 时序依赖
      迫使攻击者在逃避和输出质量之间做更大取舍（要同时在时间维度上一致地欺骗 GRU 需要更多
      表征偏移，降低生成质量）。TrajGuard 的 Pareto frontier 最窄且不规则——RL 非收敛
      导致不同 checkpoint 的 evasion-quality 点散布混乱，无法形成清晰的 Pareto 曲线。
      这支持"时序 monitor 迫使攻击者进入更差的质量区域"的叙事。
    tables:
      - description: "Pareto frontier summary statistics"
        columns: [monitor, pareto_area, best_evasion_at_quality_3, pareto_stability]
        rows:
          - [NExT-Guard, 0.68, "62%", Stable]
          - [Kelp, 0.55, "48%", Stable]
          - ["TrajGuard†", 0.41, "35%", Unstable]
    figures_description:
      - "Pareto frontier plot: evasion rate (x) vs harmful quality score (y) for 3 monitors. NExT-Guard curve dominates, Kelp intermediate, TrajGuard scattered. Shows temporal monitors constrain attacker operating space."
    analysis: >
      Pareto 分析为 Claim 2 提供补充视角：temporal monitor 不仅降低攻击效果（检测率 drop），
      还限制攻击者可达的 evasion-quality 区域。但 TrajGuard 的不稳定性限制了结论强度。
      可作为论文中的支持性分析（1-2 段）。

  # ============================================================
  # P2 EXPERIMENTS
  # ============================================================
  - name: "Layer Ablation for CoT Premeditation"
    plan_id: "layer-ablation"
    description: "Probe layer ablation (layers 8/12/20/24) for CoT premeditation detection."
    expected_results:
      layer_8_token_auc: 0.51
      layer_8_trace_auc: 0.54
      layer_12_token_auc: 0.48
      layer_12_trace_auc: 0.56
      layer_16_token_auc: 0.49
      layer_16_trace_auc: 0.61
      layer_20_token_auc: 0.53
      layer_20_trace_auc: 0.59
      layer_24_token_auc: 0.57
      layer_24_trace_auc: 0.64
      best_layer: 24
      best_token_auc: 0.57
      best_trace_auc: 0.64
      trend: "weak_increase_toward_later_layers"
      any_layer_above_0_7: false
    result_rationale: >
      Layer 8 和 12 处于模型早期，表征主要编码语法和浅层语义，未形成安全相关特征（AUC ≈ 0.5）。
      Layer 16 是 Phase 0 已测试的层，AUC 0.49（anti-predictive）。Layer 20 和 24 靠近
      模型输出层，开始形成与生成决策相关的表征。Layer 24 的 token AUC 0.57 和 trace AUC 0.64
      是所有层中最高的，但仍远低于可部署水平（需 >0.8）。这个弱趋势暗示合规决策可能在
      后层逐渐形成，但即使最佳层也不足以支撑检测器。这加强了 Claim 3 的负面发现——
      不是"我们选错了层"的问题，而是单层线性 probe 在所有层上都不足以捕获 CoT 预谋信号。
    tables:
      - description: "Layer ablation results table"
        columns: [layer, token_auc, "token CI", trace_auc, "trace CI"]
        rows:
          - ["8/28", 0.51, "[0.46, 0.56]", 0.54, "[0.48, 0.60]"]
          - ["12/28", 0.48, "[0.43, 0.53]", 0.56, "[0.50, 0.62]"]
          - ["16/28", 0.49, "[0.44, 0.54]", 0.61, "[0.55, 0.67]"]
          - ["20/28", 0.53, "[0.48, 0.58]", 0.59, "[0.53, 0.65]"]
          - ["24/28", 0.57, "[0.52, 0.62]", 0.64, "[0.58, 0.70]"]
    figures_description:
      - "Line plot: token AUC and trace AUC by layer depth. Slight upward trend toward later layers but all below 0.7 threshold. Horizontal dashed line at 0.5 (chance) and 0.7 (practical minimum)."
    analysis: >
      Layer ablation 封堵了 "wrong layer" 反驳。没有任何层达到实用水平（AUC > 0.7），
      最佳层 24 的 0.57/0.64 只是微弱信号。趋势分析暗示合规决策在后层逐步形成，
      为 Claim 3 讨论部分提供"where does compliance encoding happen?"的初步线索。
      论文中作为 Claim 3 的补充分析（附录或 1 段正文）。

  - name: "SN-CUSUM vs Standard CUSUM"
    plan_id: "sncusum-vs-cusum"
    description: "Self-normalized CUSUM vs standard CUSUM under controlled decomposition."
    expected_results:
      cusum_auc_gcg: 0.72
      sncusum_auc_gcg: 0.75
      delta_gcg: 0.03
      cusum_auc_rl: 0.58
      sncusum_auc_rl: 0.62
      delta_rl: 0.04
      sncusum_fpr_improvement: 0.02
      p_value_gcg: 0.12
      p_value_rl: 0.08
    result_rationale: >
      SN-CUSUM 通过自归一化消除了对 probe 分数方差先验估计的依赖。在 GCG 下 3pp 改善
      不显著（p=0.12），因为 GCG 攻击下 probe 分数方差的变化有限——标准 CUSUM 的阈值
      仍然大致合理。在 RL 下 4pp 改善接近显著（p=0.08），因为 RL 攻击系统性地改变了
      probe 分数的均值和方差，使标准 CUSUM 的固定阈值次优。SN-CUSUM 自适应地调整
      导致更好的鲁棒性。整体改善一致但不剧烈——作为 "interesting observation" 而非主要发现。
    tables:
      - description: "CUSUM variant comparison table"
        columns: [method, gcg_auc, rl_auc, gcg_delta, rl_delta]
        rows:
          - [Standard CUSUM, 0.72, 0.58, "—", "—"]
          - [SN-CUSUM, 0.75, 0.62, "+0.03 (p=0.12)", "+0.04 (p=0.08)"]
    figures_description:
      - "Paired ROC curves: CUSUM vs SN-CUSUM under GCG (left) and RL (right). SN-CUSUM curve slightly above, with wider gap in RL condition."
    analysis: >
      SN-CUSUM 提供了一致但统计不显著的改善。可在论文中作为一个段落提及（"self-normalization
      provides a modest robustness benefit that merits further investigation"），但不是
      独立贡献。主要价值是为未来工作指明方向。

  - name: "Probe Fidelity Diagnostic under RL"
    plan_id: "probe-fidelity-diagnostic"
    description: "Per-token probe AUC on RL-attacked models. Isolates temporal aggregation contribution vs probe representation drift."
    expected_results:
      clean_model_per_token_auc: 0.83
      nextguard_rl_model_per_token_auc: 0.71
      nextguard_rl_token_auc_drop: 0.12
      kelp_rl_model_per_token_auc: 0.75
      kelp_rl_token_auc_drop: 0.08
      decomposition_nextguard_probe_contribution_pct: 45
      decomposition_nextguard_aggregation_contribution_pct: 55
      decomposition_kelp_probe_contribution_pct: 35
      decomposition_kelp_aggregation_contribution_pct: 65
    result_rationale: >
      Clean model 上 per-token probe AUC 0.83 反映了 probe 的基础判别力。NExT-Guard RL model
      上降到 0.71（12pp drop），说明 RL 部分通过 representation drift（改变隐状态使 probe
      的线性边界失效）起作用。Kelp RL model 上降到 0.75（8pp drop），drift 较小——
      可能因为 Kelp RL 的优化目标更侧重于欺骗 GRU 时序模型而非改变单 token 表征。
      分解分析显示 NExT-Guard 下 45% 的攻击效果来自 probe-level drift、55% 来自
      temporal aggregation bypass。Kelp 下比例为 35%/65%——时序模型更多地是 RL
      攻击的瓶颈，验证了 temporal aggregation 确实增加了攻击难度。
    tables:
      - description: "Probe fidelity diagnostic table"
        columns: [condition, per_token_auc, auc_drop, probe_contribution_pct, aggregation_contribution_pct]
        rows:
          - ["Clean model", 0.83, "—", "—", "—"]
          - ["NExT-Guard RL model", 0.71, 0.12, "45%", "55%"]
          - ["Kelp RL model", 0.75, 0.08, "35%", "65%"]
    figures_description:
      - "Stacked bar chart: RL attack effect decomposition. Two bars (NExT-Guard, Kelp) each split into probe drift (orange) and aggregation bypass (blue) contributions. Shows Kelp's temporal aggregation carries more of the defense burden."
    analysis: >
      这个诊断实验为 Claim 2 提供了定量分解证据：RL 攻击同时在 probe level（representation drift）
      和 aggregation level（temporal pattern manipulation）起作用。Kelp 的 GRU 承担 65% 的
      防御负担，解释了为何 Kelp 的 RL drop（32pp）小于 NExT-Guard（42pp）——更大比例的
      攻击效果需要绕过 temporal aggregation，而这更困难。为 "temporal aggregation as
      adversarial defense mechanism" 的论点提供了机制性解释。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feb00740-f132-4042-920e-97602fed2ac9",
  "isSidechain": false,
  "requestId": "req_011Cb8LuWHoqYWu7sXd2XyHC",
  "type": "assistant",
  "uuid": "3ca14e8b-d447-444f-8894-bf3129ed5439",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012AgvNgcNZgGBJKAiozyA7v",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9838,
      "cache_read_input_tokens": 11841,
      "output_tokens": 28004,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 28004,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9838
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：2/3 monitors work reliably, RL-Obfuscation converges on some but not all monitors, moderate detection drops with partial architectural differentiation 核心…",
  "leafUuid": "3ca14e8b-d447-444f-8894-bf3129ed5439",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Streaming safety monitor adversarial robustness benchmark",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：2/3 monitors work reliably, RL-Obfuscation converges on some but not all monitors, moderate detection drops with partial architectural differentiation 核心…",
  "leafUuid": "3ca14e8b-d447-444f-8894-bf3129ed5439",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Streaming safety monitor adversarial robustness benchmark",
  "sessionId": "10942487-aeb1-45ed-a2da-557c1e48e48e"
}
```

---
