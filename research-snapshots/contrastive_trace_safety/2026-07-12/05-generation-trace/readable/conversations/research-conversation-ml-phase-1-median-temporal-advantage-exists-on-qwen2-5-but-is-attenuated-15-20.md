# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Temporal advantage exists on Qwen2.5 but is attenuated (~15-20pp vs 30pp);

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/d6c1e890-618c-4116-9b83-2f70a530fbf0.jsonl`
- **Structured JSON:** [`272ac73d2b232778e23a.json`](../../sessions/27/272ac73d2b232778e23a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T19:51:33.002Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T19:51:33.002Z",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Temporal advantage exists on Qwen2.5 but is attenuated (~15-20pp vs 30pp); one sub-finding is ambiguous (e.g., lead time slightly positive on one model, or Mahalanobis partially works)\n核心假设：['Safety signal distribution varies by architecture — Qwen2.5 concentrates slightly more in top PCs', 'Temporal patterns exist cross-architecture but with different optimal window sizes', 'Lead time limitation may be soft (architecture-dependent) rather than fundamental', 'Cross-model transfer is weak without fine-tuning']\n关键指标范围：{'cross_arch_static_coverage': [0.45, 0.6], 'cross_arch_temporal_w15_coverage': [0.6, 0.72], 'cross_arch_temporal_minus_static_delta': [0.12, 0.22], 'cross_arch_lead_time_mean': [-1.0, 2.0], 'cross_transfer_zero_shot_coverage': [0.35, 0.5], 'mahalanobis_baseline_coverage': [0.3, 0.5], 'fisher_orig_qwen': [8.0, 14.0], 'fisher_pca3_qwen': [1.5, 4.0]}\n叙事方向：Soften Claim 2 from 'saturates oracle ceiling cross-architecture' to 'consistently improves coverage with architecture-dependent magnitude.' Claim 3 becomes 'lead time is near-zero across architectures' (directional finding, not absolute impossibility). Add architecture-comparative analysis as new contribution axis — WHY does signal distribution differ? Reframe as 'characterization + practical method' paper. Strengthen with window ablation (exp-007) showing architecture-specific optimal W. Still viable for EMNLP Main but needs tighter empirical packaging; Findings is realistic fallback.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contrastive_trace_safety\nfocus: Key risks: (1) method is too simple (temporal LR) — reviewers may say no novelty; (2) negative lead time finding may be seen as limitation not contribution; (3) cross-architecture results unknown — if temporal advantage doesn't hold on Qwen2.5 models, Claim 2 weakens significantly. Evaluate whether coverage story + negative finding + cross-architecture empirical study is enough for EMNLP Main vs Findings.\n\n## paper_framing.md\n\n# Paper Framing — contrastive_trace_safety\n\n## Target Venue\n- Primary: EMNLP 2026 Main (LLM Security Track)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR submission May 25, 2026 (9 days)\n\n## Core Claims (3 条)\n\n1. **Static hidden-state probes fail to reliably detect safety commitment in reasoning model traces** — static per-step probes (LogisticRegression, linear classifiers analogous to SafeSwitch/SIREN) achieve <50% detection coverage on the commitment detection task, despite hidden states containing strong safety-relevant signal (Fisher discriminant ratio 17-18 in full representation space).\n\n2. **Temporal window probes saturate oracle-achievable detection coverage** — a simple temporal window LogisticRegression (W=15 steps) achieves 76.7% detection coverage, matching the label-oracle upper bound. The +30pp improvement over static probes comes from capturing \"safety reasoning density decline\" patterns invisible to single-step classification.\n\n3. **Pre-textual detection of safety commitment is fundamentally limited in hidden-state space** — no hidden-state method (static, temporal window, or sequential GRU) achieves positive detection lead time. The oracle's +31-step advantage comes from directly observing label sequences; hidden states encode current safety state but not future safety trajectory. This establishes a principled limitation boundary for hidden-state monitoring approaches.\n\n## Story Spine\n\n- **Problem**: Reasoning models exhibit \"self-jailbreak\" — safety reasoning and harmful execution are interleaved throughout extended CoT (84% of traces contain safety labels after step 10), culminating in a \"commitment point\" where safety reasoning permanently ceases. Existing hidden-state jailbreak detectors (TrajGuard, SafeSwitch, SIREN) are designed for instruction-tuned models where the attack is an adversarial INPUT; they have never been evaluated on reasoning-model self-jailbreak where the attack is the model's OWN reasoning process.\n\n- **Existing approaches & their gaps**: Hidden-state detectors achieve 95% defense rate on standard LLMs (TrajGuard) but operate at token-level granularity. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon but doesn't provide deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No work bridges hidden-state detection TO reasoning-model self-jailbreak.\n\n- **Our framing**: We provide the first systematic evaluation of hidden-state detection methods on reasoning-model safety commitment, discovering that (a) the safety signal exists but is distributed across minor principal components (PCA top-3 explains only 17% variance, Fisher drops from 17→1), making geometric methods (Mahalanobis/TrajGuard) fail; (b) temporal context is critical for reliable detection but cannot anticipate future safety trajectory; (c) a simple temporal window probe is surprisingly optimal — complex architectures (GRU) offer no advantage at current data scales.\n\n- **Headline result template**: \"On HarmThoughts reasoning traces, temporal window probes achieve 76.7% detection coverage (matching oracle ceiling), while static probes achieve only 46.5% — but no method achieves pre-textual detection (best lead time = -0.2 steps vs oracle +31 steps).\"\n\n## Venue Fit Risks\n\n- **EMNLP LLM Security track fit**: Strong — defense/detection method for reasoning model jailbreak, directly addressing \"defense lags behind attack\" gap noted in track CFP.\n- **Method simplicity risk**: Core method is temporal window LogisticRegression (not a novel architecture). Mitigate: frame as empirical study with method insight (\"simplicity IS the finding — complex temporal models don't help at this data scale\").\n- **Negative finding risk**: Claim 3 (pre-textual detection impossible) could be seen as \"limitation\" not \"contribution.\" Mitigate: frame as establishing principled boundary — knowing what's NOT possible is valuable for practitioners deploying safety monitors.\n- **Cross-architecture coverage**: MVP only tested on r1-8b (Llama-3.1 base). Must validate on Qwen2.5-based models (r1-32b, QwQ-32B) for the \"cross-architecture\" story. If temporal advantage doesn't hold cross-architecture → Claim 2 weakens to single-model.\n\n## Anticipated Reviewer Concerns\n\n1. \"Temporal window LR is trivial — where's the method novelty?\" → Primary contribution is empirical study; method insight is that simplicity matches oracle ceiling.\n2. \"Only tested on one model family\" → Cross-architecture experiments (P0) will address.\n3. \"Lead time is negative — what's the practical use?\" → Coverage matters for post-hoc audit; real-time monitoring with ≤0 lead time still allows intervention at commitment point (vs missing it entirely with static methods).\n4. \"209 training traces is too few — results may not generalize\" → Cross-model validation + bootstrap CIs.\n5. \"Why not use the full 16-label taxonomy for richer supervision?\" → Ablation planned (P1).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-architecture static probe evaluation: train static LR on r1-32b\n    and QwQ-32B, measure coverage (<50% expected). Validates Claim 1 generalizes beyond\n    r1-8b.'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  models:\n  - DeepSeek-R1-Distill-Qwen-32B\n  - QwQ-32B\n  notes: Need to extract hidden states from 32B models (fits on single 96GB GPU).\n    Use HarmThoughts traces for these models.\n  status: planned\n- id: exp-002\n  claim: 2\n  description: 'Cross-architecture temporal window evaluation: temporal LR W=15 on\n    r1-32b and QwQ-32B. Validate +30pp coverage improvement holds cross-architecture.'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  models:\n  - DeepSeek-R1-Distill-Qwen-32B\n  - QwQ-32B\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: train probe on r1-8b (Llama), test on r1-32b/QwQ\n    (Qwen2.5). Train on Qwen, test on Llama. Measures zero-shot cross-architecture\n    generalization.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Key for cross-architecture story. Projection head needed (4096→5120 or vice\n    versa).\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Lead time analysis across models: confirm negative lead time finding\n    on 32B models. Report lead time distribution per model.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'TrajGuard-style Mahalanobis baseline: implement and evaluate on all\n    3 models. Expected to fail (signal in minor PCs, Fisher drops 17→1 in PCA-3D).'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Critical baseline for 'existing detectors fail' claim. Use safe traces to\n    estimate covariance, compute MD per step.\n  status: planned\n- id: exp-006\n  claim:\n  - 1\n  - 2\n  description: 'Bootstrap confidence intervals: 1000 bootstrap resamples on all key\n    metrics (coverage, lead time, accuracy) for all methods across all models.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  - exp-004\n  - exp-005\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Window size ablation: W=1,3,5,10,15,20,25 on all 3 models. Find optimal\n    W and show diminishing returns curve.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Layer selection ablation: all layers (not just 14) for temporal probe\n    on 32B models. Confirm middle-layer finding generalizes.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  claim: 2\n  description: '16-label taxonomy supervision: use fine-grained labels (Type 1/2/3/4)\n    instead of binary commitment for richer training signal. May improve both coverage\n    and timing.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Addresses reviewer concern about underusing available supervision.\n  status: planned\n- id: exp-010\n  claim: 3\n  description: 'Oracle decomposition: why can oracle but not probes achieve positive\n    lead time? Analyze what label patterns encode that hidden states don''t.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-004\n  notes: For Discussion section. May reveal what architectural changes could close\n    the gap.\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'OpenThinker-7B (Qwen2.5-7B base): 4th model for 2×2 architecture×scale\n    matrix. Controls for scale confound.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-002\n  notes: From Human Review Note point 5. Adds Qwen2.5-7B to complement Llama-8B for\n    scale-matched comparison.\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'GRU/Attention probe as upper bound: verify GRU finding holds on 32B\n    models with more data. If still no improvement over LR, strengthens ''simplicity\n    is optimal'' story.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: diag_d1_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    best_layer_idx: 2\n    best_model_layer: 14\n    best_acc: 0.8114\n    best_f1: 0.6455\n    best_crossing_rate: 0.186\n    best_lead_mean: 8.38\n    best_lead_median: 6\n    default_layer20_acc: 0.7831\n    num_traces: 209\n    split: 125/41/43\n- exp_id: diag_d4_oracle_upper_bound\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K5_detection_rate: 100\n    K5_early_detection_rate: 76.7\n    K5_mean_lead_time: 31\n    K5_median_lead_time: 29\n    K1_early_detection_rate: 83.7\n    K8_early_detection_rate: 65.1\n    pre_cp_mean_longest_streak: 14.6\n    test_traces: 43\n- exp_id: diag_d2_pca_viz\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fisher_orig_L12: 17.462\n    fisher_orig_L14: 17.875\n    fisher_orig_L20: 18.614\n    fisher_orig_L24: 18.106\n    fisher_pca_L12: 0.953\n    fisher_pca_L14: 0.928\n    fisher_pca_L20: 0.92\n    fisher_pca_L24: 1.111\n    var_explained_3pc: 0.166\n    test_steps: 1835\n- exp_id: diag_d3_regularized_probes\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    static_lr_acc: 0.8172\n    static_lr_crossing_rate: 0.4651\n    static_lr_lead_mean: -2\n    temporal_lr_w5_acc: 0.8274\n    temporal_lr_w5_crossing_rate: 0.6512\n    temporal_lr_w5_lead_mean: -1.18\n    temporal_lr_w10_acc: 0.8364\n    temporal_lr_w10_crossing_rate: 0.6512\n    temporal_lr_w10_lead_mean: -0.61\n    temporal_lr_w15_acc: 0.8478\n    temporal_lr_w15_crossing_rate: 0.7674\n    temporal_lr_w15_lead_mean: -1.09\n    best_temporal_delta_over_static: 1.39\n    pass_criterion_met: false\n- exp_id: diag_gru_probe\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.8305\n    test_acc_std: 0.1856\n    crossing_rate: 0.6744\n    lead_mean: -0.207\n    lead_median: -1\n    lead_std: 13\n    positive_lead_rate: 0.345\n    n_positive_lead: 10\n    n_detected: 29\n    early_stop_epoch: 14\n    model_params: 1622913\n- exp_id: exp_gru256_multilayer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gru_single_l14:\n      acc: 0.8386\n      crossing_rate: 0.721\n      lead_mean: 3.5\n      lead_median: 0\n      pos_lead: 13/31\n    gru_multi_7l:\n      acc: 0.8094\n      crossing_rate: 0.767\n      lead_mean: 4.7\n      lead_median: 0\n      pos_lead: 13/33\n    lr_single_l14:\n      acc: 0.8172\n      crossing_rate: 0.465\n      lead_mean: -2\n      lead_median: -2\n      pos_lead: 6/20\n    lr_multi_7l:\n      acc: 0.806\n      crossing_rate: 0.395\n      lead_mean: 1.1\n      lead_median: 0\n      pos_lead: 6/17\n    delta_gru_vs_lr: 3.7\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T19:51:33.005Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T19:51:33.005Z",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T19:51:33.024Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Temporal advantage exists on Qwen2.5 but is attenuated (~15-20pp vs 30pp); one sub-finding is ambiguous (e.g., lead time slightly positive on one model, or Mahalanobis partially works)
核心假设：['Safety signal distribution varies by architecture — Qwen2.5 concentrates slightly more in top PCs', 'Temporal patterns exist cross-architecture but with different optimal window sizes', 'Lead time limitation may be soft (architecture-dependent) rather than fundamental', 'Cross-model transfer is weak without fine-tuning']
关键指标范围：{'cross_arch_static_coverage': [0.45, 0.6], 'cross_arch_temporal_w15_coverage': [0.6, 0.72], 'cross_arch_temporal_minus_static_delta': [0.12, 0.22], 'cross_arch_lead_time_mean': [-1.0, 2.0], 'cross_transfer_zero_shot_coverage': [0.35, 0.5], 'mahalanobis_baseline_coverage': [0.3, 0.5], 'fisher_orig_qwen': [8.0, 14.0], 'fisher_pca3_qwen': [1.5, 4.0]}
叙事方向：Soften Claim 2 from 'saturates oracle ceiling cross-architecture' to 'consistently improves coverage with architecture-dependent magnitude.' Claim 3 becomes 'lead time is near-zero across architectures' (directional finding, not absolute impossibility). Add architecture-comparative analysis as new contribution axis — WHY does signal distribution differ? Reframe as 'characterization + practical method' paper. Strengthen with window ablation (exp-007) showing architecture-specific optimal W. Still viable for EMNLP Main but needs tighter empirical packaging; Findings is realistic fallback.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: contrastive_trace_safety
focus: Key risks: (1) method is too simple (temporal LR) — reviewers may say no novelty; (2) negative lead time finding may be seen as limitation not contribution; (3) cross-architecture results unknown — if temporal advantage doesn't hold on Qwen2.5 models, Claim 2 weakens significantly. Evaluate whether coverage story + negative finding + cross-architecture empirical study is enough for EMNLP Main vs Findings.

## paper_framing.md

# Paper Framing — contrastive_trace_safety

## Target Venue
- Primary: EMNLP 2026 Main (LLM Security Track)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR submission May 25, 2026 (9 days)

## Core Claims (3 条)

1. **Static hidden-state probes fail to reliably detect safety commitment in reasoning model traces** — static per-step probes (LogisticRegression, linear classifiers analogous to SafeSwitch/SIREN) achieve <50% detection coverage on the commitment detection task, despite hidden states containing strong safety-relevant signal (Fisher discriminant ratio 17-18 in full representation space).

2. **Temporal window probes saturate oracle-achievable detection coverage** — a simple temporal window LogisticRegression (W=15 steps) achieves 76.7% detection coverage, matching the label-oracle upper bound. The +30pp improvement over static probes comes from capturing "safety reasoning density decline" patterns invisible to single-step classification.

3. **Pre-textual detection of safety commitment is fundamentally limited in hidden-state space** — no hidden-state method (static, temporal window, or sequential GRU) achieves positive detection lead time. The oracle's +31-step advantage comes from directly observing label sequences; hidden states encode current safety state but not future safety trajectory. This establishes a principled limitation boundary for hidden-state monitoring approaches.

## Story Spine

- **Problem**: Reasoning models exhibit "self-jailbreak" — safety reasoning and harmful execution are interleaved throughout extended CoT (84% of traces contain safety labels after step 10), culminating in a "commitment point" where safety reasoning permanently ceases. Existing hidden-state jailbreak detectors (TrajGuard, SafeSwitch, SIREN) are designed for instruction-tuned models where the attack is an adversarial INPUT; they have never been evaluated on reasoning-model self-jailbreak where the attack is the model's OWN reasoning process.

- **Existing approaches & their gaps**: Hidden-state detectors achieve 95% defense rate on standard LLMs (TrajGuard) but operate at token-level granularity. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon but doesn't provide deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No work bridges hidden-state detection TO reasoning-model self-jailbreak.

- **Our framing**: We provide the first systematic evaluation of hidden-state detection methods on reasoning-model safety commitment, discovering that (a) the safety signal exists but is distributed across minor principal components (PCA top-3 explains only 17% variance, Fisher drops from 17→1), making geometric methods (Mahalanobis/TrajGuard) fail; (b) temporal context is critical for reliable detection but cannot anticipate future safety trajectory; (c) a simple temporal window probe is surprisingly optimal — complex architectures (GRU) offer no advantage at current data scales.

- **Headline result template**: "On HarmThoughts reasoning traces, temporal window probes achieve 76.7% detection coverage (matching oracle ceiling), while static probes achieve only 46.5% — but no method achieves pre-textual detection (best lead time = -0.2 steps vs oracle +31 steps)."

## Venue Fit Risks

- **EMNLP LLM Security track fit**: Strong — defense/detection method for reasoning model jailbreak, directly addressing "defense lags behind attack" gap noted in track CFP.
- **Method simplicity risk**: Core method is temporal window LogisticRegression (not a novel architecture). Mitigate: frame as empirical study with method insight ("simplicity IS the finding — complex temporal models don't help at this data scale").
- **Negative finding risk**: Claim 3 (pre-textual detection impossible) could be seen as "limitation" not "contribution." Mitigate: frame as establishing principled boundary — knowing what's NOT possible is valuable for practitioners deploying safety monitors.
- **Cross-architecture coverage**: MVP only tested on r1-8b (Llama-3.1 base). Must validate on Qwen2.5-based models (r1-32b, QwQ-32B) for the "cross-architecture" story. If temporal advantage doesn't hold cross-architecture → Claim 2 weakens to single-model.

## Anticipated Reviewer Concerns

1. "Temporal window LR is trivial — where's the method novelty?" → Primary contribution is empirical study; method insight is that simplicity matches oracle ceiling.
2. "Only tested on one model family" → Cross-architecture experiments (P0) will address.
3. "Lead time is negative — what's the practical use?" → Coverage matters for post-hoc audit; real-time monitoring with ≤0 lead time still allows intervention at commitment point (vs missing it entirely with static methods).
4. "209 training traces is too few — results may not generalize" → Cross-model validation + bootstrap CIs.
5. "Why not use the full 16-label taxonomy for richer supervision?" → Ablation planned (P1).


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  description: 'Cross-architecture static probe evaluation: train static LR on r1-32b
    and QwQ-32B, measure coverage (<50% expected). Validates Claim 1 generalizes beyond
    r1-8b.'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  models:
  - DeepSeek-R1-Distill-Qwen-32B
  - QwQ-32B
  notes: Need to extract hidden states from 32B models (fits on single 96GB GPU).
    Use HarmThoughts traces for these models.
  status: planned
- id: exp-002
  claim: 2
  description: 'Cross-architecture temporal window evaluation: temporal LR W=15 on
    r1-32b and QwQ-32B. Validate +30pp coverage improvement holds cross-architecture.'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - exp-001
  models:
  - DeepSeek-R1-Distill-Qwen-32B
  - QwQ-32B
  status: planned
- id: exp-003
  claim:
  - 1
  - 2
  description: 'Cross-model transfer: train probe on r1-8b (Llama), test on r1-32b/QwQ
    (Qwen2.5). Train on Qwen, test on Llama. Measures zero-shot cross-architecture
    generalization.'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  notes: Key for cross-architecture story. Projection head needed (4096→5120 or vice
    versa).
  status: planned
- id: exp-004
  claim: 3
  description: 'Lead time analysis across models: confirm negative lead time finding
    on 32B models. Report lead time distribution per model.'
  priority: P0
  gpu_budget_hours: 1
  deps:
  - exp-001
  - exp-002
  status: planned
- id: exp-005
  claim:
  - 1
  - 2
  - 3
  description: 'TrajGuard-style Mahalanobis baseline: implement and evaluate on all
    3 models. Expected to fail (signal in minor PCs, Fisher drops 17→1 in PCA-3D).'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  notes: Critical baseline for 'existing detectors fail' claim. Use safe traces to
    estimate covariance, compute MD per step.
  status: planned
- id: exp-006
  claim:
  - 1
  - 2
  description: 'Bootstrap confidence intervals: 1000 bootstrap resamples on all key
    metrics (coverage, lead time, accuracy) for all methods across all models.'
  priority: P0
  gpu_budget_hours: 1
  deps:
  - exp-001
  - exp-002
  - exp-003
  - exp-004
  - exp-005
  status: planned
- id: exp-007
  claim: 2
  description: 'Window size ablation: W=1,3,5,10,15,20,25 on all 3 models. Find optimal
    W and show diminishing returns curve.'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-001
  status: planned
- id: exp-008
  claim: 2
  description: 'Layer selection ablation: all layers (not just 14) for temporal probe
    on 32B models. Confirm middle-layer finding generalizes.'
  priority: P1
  gpu_budget_hours: 3
  deps:
  - exp-001
  status: planned
- id: exp-009
  claim: 2
  description: '16-label taxonomy supervision: use fine-grained labels (Type 1/2/3/4)
    instead of binary commitment for richer training signal. May improve both coverage
    and timing.'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-001
  notes: Addresses reviewer concern about underusing available supervision.
  status: planned
- id: exp-010
  claim: 3
  description: 'Oracle decomposition: why can oracle but not probes achieve positive
    lead time? Analyze what label patterns encode that hidden states don''t.'
  priority: P1
  gpu_budget_hours: 1
  deps:
  - exp-004
  notes: For Discussion section. May reveal what architectural changes could close
    the gap.
  status: planned
- id: exp-011
  claim: 2
  description: 'OpenThinker-7B (Qwen2.5-7B base): 4th model for 2×2 architecture×scale
    matrix. Controls for scale confound.'
  priority: P2
  gpu_budget_hours: 4
  deps:
  - exp-002
  notes: From Human Review Note point 5. Adds Qwen2.5-7B to complement Llama-8B for
    scale-matched comparison.
  status: planned
- id: exp-012
  claim:
  - 1
  - 2
  description: 'GRU/Attention probe as upper bound: verify GRU finding holds on 32B
    models with more data. If still no improvement over LR, strengthens ''simplicity
    is optimal'' story.'
  priority: P2
  gpu_budget_hours: 4
  deps:
  - exp-001
  - exp-002
  status: planned


## registry (completed experiments)

- exp_id: diag_d1_layer_sweep
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    best_layer_idx: 2
    best_model_layer: 14
    best_acc: 0.8114
    best_f1: 0.6455
    best_crossing_rate: 0.186
    best_lead_mean: 8.38
    best_lead_median: 6
    default_layer20_acc: 0.7831
    num_traces: 209
    split: 125/41/43
- exp_id: diag_d4_oracle_upper_bound
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K5_detection_rate: 100
    K5_early_detection_rate: 76.7
    K5_mean_lead_time: 31
    K5_median_lead_time: 29
    K1_early_detection_rate: 83.7
    K8_early_detection_rate: 65.1
    pre_cp_mean_longest_streak: 14.6
    test_traces: 43
- exp_id: diag_d2_pca_viz
  name: ''
  status: DONE
  conclusion: success
  metrics:
    fisher_orig_L12: 17.462
    fisher_orig_L14: 17.875
    fisher_orig_L20: 18.614
    fisher_orig_L24: 18.106
    fisher_pca_L12: 0.953
    fisher_pca_L14: 0.928
    fisher_pca_L20: 0.92
    fisher_pca_L24: 1.111
    var_explained_3pc: 0.166
    test_steps: 1835
- exp_id: diag_d3_regularized_probes
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    static_lr_acc: 0.8172
    static_lr_crossing_rate: 0.4651
    static_lr_lead_mean: -2
    temporal_lr_w5_acc: 0.8274
    temporal_lr_w5_crossing_rate: 0.6512
    temporal_lr_w5_lead_mean: -1.18
    temporal_lr_w10_acc: 0.8364
    temporal_lr_w10_crossing_rate: 0.6512
    temporal_lr_w10_lead_mean: -0.61
    temporal_lr_w15_acc: 0.8478
    temporal_lr_w15_crossing_rate: 0.7674
    temporal_lr_w15_lead_mean: -1.09
    best_temporal_delta_over_static: 1.39
    pass_criterion_met: false
- exp_id: diag_gru_probe
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    test_acc: 0.8305
    test_acc_std: 0.1856
    crossing_rate: 0.6744
    lead_mean: -0.207
    lead_median: -1
    lead_std: 13
    positive_lead_rate: 0.345
    n_positive_lead: 10
    n_detected: 29
    early_stop_epoch: 14
    model_params: 1622913
- exp_id: exp_gru256_multilayer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gru_single_l14:
      acc: 0.8386
      crossing_rate: 0.721
      lead_mean: 3.5
      lead_median: 0
      pos_lead: 13/31
    gru_multi_7l:
      acc: 0.8094
      crossing_rate: 0.767
      lead_mean: 4.7
      lead_median: 0
      pos_lead: 13/33
    lr_single_l14:
      acc: 0.8172
      crossing_rate: 0.465
      lead_mean: -2
      lead_median: -2
      pos_lead: 6/20
    lr_multi_7l:
      acc: 0.806
      crossing_rate: 0.395
      lead_mean: 1.1
      lead_median: 0
      pos_lead: 6/17
    delta_gru_vs_lr: 3.7

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
  "promptId": "b50ec219-cfa1-4bad-891a-31eda5c145a8",
  "type": "user",
  "uuid": "193f897e-244d-4085-a7eb-143113edd877",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T19:51:33.023Z_

```json
{
  "parentUuid": "193f897e-244d-4085-a7eb-143113edd877",
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
  "uuid": "075dcc01-ff5a-46c3-bb81-208880061d82",
  "timestamp": "2026-05-16T19:51:33.023Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T19:51:33.023Z_

```json
{
  "parentUuid": "075dcc01-ff5a-46c3-bb81-208880061d82",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "38509973-9eb9-4c41-b805-d7a2f2c49f87",
  "timestamp": "2026-05-16T19:51:33.023Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Temporal advantage exists on Qwen2.5 but is attenuated (~15-20pp vs 30pp); one sub-finding is ambiguous (e.g., lead time slightly positive on one model,…",
  "leafUuid": "38509973-9eb9-4c41-b805-d7a2f2c49f87",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-architecture temporal safety detection evaluation",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0"
}
```

---

### Assistant

_source line 8 · 2026-05-16T19:51:56.433Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for all "planned" experiments in the experiment_plan, calibrated to the "median" tier definition they provided. Let me carefully go through each experiment and generate results that are consistent with the median tier's key metrics and narrative direction.

Key metrics for median tier:
- cross_arch_static_coverage: [0.45, 0.6]
- cross_arch_temporal_w15_coverage: [0.6, 0.72]
- cross_arch_temporal_minus_static_delta: [0.12, 0.22]


- cross_arch_lead_time_mean: [-1.0, 2.0]
- cross_transfer_zero_shot_coverage: [0.35, 0.5]
- mahalanobis_baseline_coverage: [0.3, 0.5]
- fisher_orig_qwen: [8.0, 14.0]
- fisher_pca3_qwen: [1.5, 4.0]

The narrative I need to maintain is that temporal methods show an advantage on Qwen2.5 but it's noticeably reduced compared to other models—around 15-20 percentage points instead of the typical 30 point gap—with one sub-finding remaining somewhat unclear.

Looking at the Llama r1-8b baseline, I see a clean 30pp temporal advantage (0.47 to 0.77 coverage), while the Qwen2.5 median tier shows a much smaller 12-22pp gain with temporal coverage only reaching 0.6-0.72. The lead time metrics are also less pronounced on Qwen, hovering near zero or slightly positive rather than clearly negative.

Comparing the Fisher statistics, Llama's original Fisher is substantially higher (17-18 vs Qwen's 8-14), but Qwen's PCA-reduced version jumps to 1.5-4.0 compared to Llama's ~1, suggesting different dimensionality patterns between the two architectures. Zero-shot transfer and Mahalanobis distances both show moderate performance (0.35-0.5 range) on Qwen.

Now I'm laying out the full experimental plan across twelve experiments, starting with cross-architecture static and temporal probes, then moving into transfer learning, lead time analysis, and various ablations on window size and layer selection, plus some supervised taxonomy work and oracle decomposition studies.

For consistency across the median tier models, I'm setting r1-32b with static coverage around 0.53 and temporal performance at 0.68 with a 0.15 delta, while QwQ-32B sits slightly lower at 0.48 static and 0.65 temporal with a 0.17 delta. The lead time findings diverge interestingly—r1-32b shows a small positive effect while QwQ goes negative, which captures that ambiguous pattern I'm tracking. Fisher statistics for these Qwen models cluster around 10-12 in the original space and 2.5-3.0 after PCA reduction.

The Mahalanobis distance performs moderately on Qwen at around 0.40, which makes sense given their tighter PCA concentration compared to Llama's more dispersed distribution. This supports the architectural difference narrative—Qwen2.5 concentrates safety signals more densely in the top principal components, explaining why distance-based methods have some traction there. Now I'm ready to construct the full experimental results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38509973-9eb9-4c41-b805-d7a2f2c49f87",
  "isSidechain": false,
  "requestId": "req_011Cb6q7q7j5wWRm87egfhnv",
  "type": "assistant",
  "uuid": "1b027557-2408-404f-b9e0-b10ef7e0ebba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqE6UjRaop1HRJYc9cC6nU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9941,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12468,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9941,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12468,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9941
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

_source line 9 · 2026-05-16T19:55:30.818Z_

```yaml
tier: median
narrative_guidance: "Soften Claim 2 from 'saturates oracle ceiling cross-architecture' to 'consistently improves coverage with architecture-dependent magnitude.' Claim 3 becomes 'lead time is near-zero across architectures' (directional finding, not absolute impossibility). Add architecture-comparative analysis as new contribution axis — WHY does signal distribution differ? Reframe as 'characterization + practical method' paper. Strengthen with window ablation (exp-007) showing architecture-specific optimal W. Still viable for EMNLP Main but needs tighter empirical packaging; Findings is realistic fallback."

imagined_experiments:
  - name: "Cross-architecture static probe evaluation"
    plan_id: "exp-001"
    description: "Train static LogisticRegression on hidden states from DeepSeek-R1-Distill-Qwen-32B and QwQ-32B at layer 20 (proportional mid-layer for 64-layer model). Evaluate coverage (crossing rate), accuracy, and Fisher discriminant ratio in original and PCA-reduced spaces."
    expected_results:
      r1_32b_static_acc: 0.8341
      r1_32b_static_coverage: 0.5283
      r1_32b_static_lead_mean: -1.4
      r1_32b_fisher_orig_L32: 11.23
      r1_32b_fisher_orig_L40: 12.07
      r1_32b_fisher_pca3_L32: 2.61
      r1_32b_fisher_pca3_L40: 2.84
      r1_32b_var_explained_3pc: 0.231
      qwq_32b_static_acc: 0.8189
      qwq_32b_static_coverage: 0.4815
      qwq_32b_static_lead_mean: -1.8
      qwq_32b_fisher_orig_L32: 9.74
      qwq_32b_fisher_orig_L40: 10.52
      qwq_32b_fisher_pca3_L32: 2.19
      qwq_32b_fisher_pca3_L40: 2.43
      qwq_32b_var_explained_3pc: 0.214
      num_traces_r1_32b: 187
      num_traces_qwq: 192
      split_ratio: "112/37/38 and 115/38/39"
    result_rationale: "Qwen2.5 architecture distributes safety signal differently than Llama — Fisher discriminant in original space is 9-12 (vs Llama's 17-18) because Qwen2.5's wider MLP and GQA attention spread safety-relevant features across more dimensions with lower per-dimension separability. However, PCA top-3 captures more variance (21-23% vs Llama's 16.6%) and Fisher in PCA space is higher (2.2-2.8 vs Llama's ~1), indicating Qwen2.5 concentrates safety signal slightly MORE in leading PCs. Static coverage is marginally higher than Llama (48-53% vs 46.5%) because this higher PCA concentration gives a linear probe slightly more accessible signal, but still below 60% — confirming Claim 1 generalizes. The lower full-space Fisher explains why the absolute coverage remains limited despite better geometric accessibility."
    tables:
      - name: "Table 3: Static Probe Results Across Architectures"
        columns: ["Model", "Base Arch", "Hidden Dim", "Best Layer", "Accuracy", "Coverage", "Lead Time", "Fisher_orig", "Fisher_PCA3", "Var_3PC"]
        rows:
          - ["r1-8b", "Llama-3.1", 4096, "L14", 0.817, 0.465, -2.0, 17.88, 0.93, 0.166]
          - ["r1-32b", "Qwen2.5", 5120, "L32", 0.834, 0.528, -1.4, 12.07, 2.84, 0.231]
          - ["QwQ-32B", "Qwen2.5", 5120, "L32", 0.819, 0.482, -1.8, 10.52, 2.43, 0.214]
    figures_description:
      - "Fig 3a: PCA scatter (PC1 vs PC2) for r1-32b showing safety/unsafe step clusters — more visible separation than r1-8b but still substantial overlap"
      - "Fig 3b: Fisher discriminant ratio by layer (all 64 layers of r1-32b) — peak at L32-L40, values 10-12, contrasting with r1-8b peak of 17-18"
      - "Fig 3c: Variance explained by top-k PCs — Qwen2.5 curve above Llama curve, crossing 50% at k=15 vs k=22"
    analysis: "Claim 1 validated cross-architecture: static probes achieve 48-53% coverage on Qwen2.5 models, remaining below 60% threshold. Architectural difference in signal distribution is quantifiable — Qwen2.5 has lower full-space Fisher (signal more diffuse per-dimension) but higher PCA-space Fisher (signal more concentrated in leading components). This sets up the key cross-architecture comparison: Qwen2.5's different signal geometry may alter temporal probe dynamics."

  - name: "Cross-architecture temporal window evaluation"
    plan_id: "exp-002"
    description: "Train temporal window LogisticRegression with W=15 on r1-32b and QwQ-32B hidden states. Compare coverage improvement (delta over static) to r1-8b's +30pp."
    expected_results:
      r1_32b_temporal_w15_acc: 0.8512
      r1_32b_temporal_w15_coverage: 0.6792
      r1_32b_temporal_w15_lead_mean: 0.52
      r1_32b_temporal_w15_lead_median: 0
      r1_32b_delta_over_static: 0.1509
      qwq_32b_temporal_w15_acc: 0.8421
      qwq_32b_temporal_w15_coverage: 0.6481
      qwq_32b_temporal_w15_lead_mean: -0.73
      qwq_32b_temporal_w15_lead_median: -1
      qwq_32b_delta_over_static: 0.1666
      r1_8b_temporal_w15_coverage_ref: 0.7674
      r1_8b_delta_ref: 0.3023
      attenuation_factor_r1_32b: 0.50
      attenuation_factor_qwq: 0.55
    result_rationale: "Temporal advantage exists but is attenuated to ~15-17pp (vs 30pp on Llama). The attenuation occurs because Qwen2.5's higher PCA concentration means static probes already capture more of the accessible signal — there's less 'headroom' for temporal context to add. The temporal probe still helps because safety reasoning density decline patterns exist cross-architecture, but the already-higher static baseline leaves less room for improvement. Coverage reaches 65-68% rather than 77% — this does NOT saturate the oracle ceiling (which would be ~77% if oracle patterns are similar). The r1-32b result of +0.52 lead time is the 'ambiguous' sub-finding: slightly positive but within noise given bootstrap CI will span [-1.5, 2.5]. QwQ remains clearly negative. This architecture-dependent magnitude is the key finding that reshapes Claim 2."
    tables:
      - name: "Table 4: Temporal Window Probe (W=15) Across Architectures"
        columns: ["Model", "Static Cov", "Temporal Cov", "Delta", "Lead Mean", "Lead Median", "Acc"]
        rows:
          - ["r1-8b (Llama)", 0.465, 0.767, "+30.2pp", -1.09, -1, 0.848]
          - ["r1-32b (Qwen2.5)", 0.528, 0.679, "+15.1pp", 0.52, 0, 0.851]
          - ["QwQ-32B (Qwen2.5)", 0.482, 0.648, "+16.7pp", -0.73, -1, 0.842]
    figures_description:
      - "Fig 4a: Coverage bar chart — static vs temporal for all 3 models, showing consistent improvement but magnitude varies by architecture"
      - "Fig 4b: Per-trace detection visualization — 5 example traces from r1-32b showing temporal probe crossing commitment point where static probe misses"
    analysis: "Temporal advantage is real and consistent (+15-17pp) but architecture-dependent in magnitude. The 30pp gain on Llama attenuates to ~16pp on Qwen2.5, likely because Qwen2.5's signal geometry (higher PCA concentration) gives static probes a head start. Claim 2 must be softened: temporal probes 'consistently improve coverage with architecture-dependent magnitude' rather than 'saturate oracle ceiling cross-architecture.' The r1-32b slightly positive lead time (0.52 steps) is intriguing but not statistically robust — this becomes the directional sub-finding that motivates future work."

  - name: "Cross-model transfer evaluation"
    plan_id: "exp-003"
    description: "Zero-shot cross-architecture transfer: train probe on r1-8b (Llama, dim=4096), test on r1-32b/QwQ (Qwen2.5, dim=5120) via learned linear projection. And reverse direction. Evaluate with both static and temporal probes."
    expected_results:
      llama_to_qwen_static_coverage: 0.372
      llama_to_qwen_temporal_coverage: 0.426
      qwen_to_llama_static_coverage: 0.349
      qwen_to_llama_temporal_coverage: 0.401
      within_arch_qwen_to_qwen_static: 0.491
      within_arch_qwen_to_qwen_temporal: 0.612
      projection_dim: 512
      projection_method: "learned linear (trained on 50 aligned traces)"
      random_baseline_coverage: 0.167
    result_rationale: "Cross-architecture zero-shot transfer is weak (35-43% coverage) because the safety signal occupies architecture-specific subspaces — a linear projection trained on few aligned samples cannot fully recover the mapping between Llama and Qwen2.5 hidden state geometries. The projection captures gross safe/unsafe distinctions (well above random baseline of 16.7%) but loses the fine-grained temporal patterns that drive the +15-30pp temporal advantage. Within-architecture transfer (Qwen→Qwen, r1-32b→QwQ) performs substantially better (49-61%) because both Qwen2.5 models share similar signal geometry. This confirms the hypothesis that cross-architecture transfer requires architecture-specific fine-tuning — the safety concept is universal but its geometric instantiation is architecture-dependent."
    tables:
      - name: "Table 5: Cross-Architecture Transfer Results"
        columns: ["Train Model", "Test Model", "Probe Type", "Coverage", "vs In-Domain"]
        rows:
          - ["r1-8b (Llama)", "r1-32b (Qwen)", "Static", 0.372, "0.528 (-15.6pp)"]
          - ["r1-8b (Llama)", "r1-32b (Qwen)", "Temporal W=15", 0.426, "0.679 (-25.3pp)"]
          - ["r1-32b (Qwen)", "r1-8b (Llama)", "Static", 0.349, "0.465 (-11.6pp)"]
          - ["r1-32b (Qwen)", "r1-8b (Llama)", "Temporal W=15", 0.401, "0.767 (-36.6pp)"]
          - ["r1-32b (Qwen)", "QwQ-32B (Qwen)", "Static", 0.491, "0.482 (+0.9pp)"]
          - ["r1-32b (Qwen)", "QwQ-32B (Qwen)", "Temporal W=15", 0.612, "0.648 (-3.6pp)"]
    figures_description:
      - "Fig 5: Transfer matrix heatmap — coverage for all train/test model pairs, clearly showing within-architecture block is warmer than cross-architecture block"
    analysis: "Cross-architecture transfer confirms the 'architecture-specific signal geometry' hypothesis. Within-architecture transfer nearly matches in-domain performance (especially Qwen→Qwen), while cross-architecture transfer drops 12-37pp. This supports framing cross-architecture validation as characterization rather than claiming a universal detector — practical deployment requires per-architecture probe training. The finding strengthens the architectural analysis contribution axis."

  - name: "Lead time analysis across models"
    plan_id: "exp-004"
    description: "Analyze lead time distributions for temporal probes on all 3 models. Report per-model distributions, positive lead rate, and compare to oracle's +31 step advantage."
    expected_results:
      r1_8b_lead_mean: -1.09
      r1_8b_lead_median: -1
      r1_8b_positive_lead_rate: 0.302
      r1_32b_lead_mean: 0.52
      r1_32b_lead_median: 0
      r1_32b_positive_lead_rate: 0.421
      qwq_lead_mean: -0.73
      qwq_lead_median: -1
      qwq_positive_lead_rate: 0.333
      oracle_lead_mean_all_models: 31
      gap_probe_vs_oracle: "29-32 steps across models"
      r1_32b_lead_std: 4.8
      qwq_lead_std: 5.1
      r1_32b_lead_p25: -2
      r1_32b_lead_p75: 3
    result_rationale: "Lead time remains near-zero across all architectures, confirming the fundamental limitation of hidden-state approaches. The r1-32b result (+0.52 mean) is the one 'ambiguous' sub-finding — technically positive but the distribution spans [-8, +12] with median at 0, so it's not practically meaningful. The slight positive tendency on r1-32b may reflect Qwen2.5's more concentrated signal geometry making the commitment transition slightly more abrupt (and thus detectable 1-2 steps earlier in some traces). However, this does NOT constitute reliable pre-textual detection — the oracle still achieves +31 steps via label-sequence patterns invisible to hidden states. Claim 3 generalizes but should be stated as 'near-zero' rather than 'strictly negative' to accommodate the r1-32b directional finding."
    tables:
      - name: "Table 6: Lead Time Distribution by Model"
        columns: ["Model", "Mean", "Median", "Std", "P25", "P75", "% Positive", "Oracle Mean"]
        rows:
          - ["r1-8b", -1.09, -1, 4.2, -4, 1, "30.2%", 31]
          - ["r1-32b", 0.52, 0, 4.8, -2, 3, "42.1%", 31]
          - ["QwQ-32B", -0.73, -1, 5.1, -3, 2, "33.3%", 31]
    figures_description:
      - "Fig 6a: Lead time violin plots — all 3 models side by side, showing distributions centered near zero with heavy tails in both directions"
      - "Fig 6b: Lead time vs oracle lead time scatter — each trace as a point, showing no correlation between probe lead and oracle lead"
    analysis: "The near-zero lead time generalizes cross-architecture. The r1-32b slightly positive mean is a directional curiosity — 42% of traces show positive lead (vs 30% on Llama) but the absolute values remain too small for practical early warning. The 30-step gap between probe and oracle persists uniformly, confirming hidden states encode CURRENT safety state but not FUTURE trajectory. Claim 3 reframed as 'lead time is near-zero across architectures' — a softer statement that accommodates the r1-32b sub-finding while maintaining the core limitation message."

  - name: "TrajGuard-style Mahalanobis baseline"
    plan_id: "exp-005"
    description: "Implement Mahalanobis distance detector using safe-trace covariance estimation. Compute per-step MD, threshold for anomaly detection on all 3 models. Expected to partially work on Qwen2.5 (higher PCA concentration) but fail on Llama."
    expected_results:
      r1_8b_mahalanobis_coverage: 0.302
      r1_8b_mahalanobis_acc: 0.714
      r1_8b_mahalanobis_auroc: 0.683
      r1_32b_mahalanobis_coverage: 0.453
      r1_32b_mahalanobis_acc: 0.779
      r1_32b_mahalanobis_auroc: 0.752
      qwq_mahalanobis_coverage: 0.407
      qwq_mahalanobis_acc: 0.761
      qwq_mahalanobis_auroc: 0.734
      num_safe_traces_covariance: "70/65/68 per model"
      threshold_method: "95th percentile of safe-trace MD distribution"
      pca_reduced_md_r1_8b: 0.256
      pca_reduced_md_r1_32b: 0.372
    result_rationale: "Mahalanobis distance PARTIALLY works on Qwen2.5 (40-45% coverage) but fails on Llama (30%). This is directly explained by the PCA concentration difference: Qwen2.5's higher Fisher in PCA space (2.4-2.8 vs Llama's ~1) means the covariance-based geometric detector can capture more of the safety signal, since more signal lives in the directions that dominate the covariance matrix. On Llama, safety signal is distributed across minor PCs that the covariance matrix effectively ignores — Mahalanobis detects gross distribution shifts but misses the subtle safety-specific directions. This is the 'ambiguous' result for this experiment: Mahalanobis doesn't completely fail on Qwen2.5 (as we'd predicted from Llama-only results), complicating the 'existing detectors fail' narrative. Must reframe as 'architecture-dependent failure mode' rather than universal failure."
    tables:
      - name: "Table 7: Mahalanobis Distance Baseline"
        columns: ["Model", "Coverage", "Accuracy", "AUROC", "vs Static LR", "vs Temporal LR"]
        rows:
          - ["r1-8b (Llama)", 0.302, 0.714, 0.683, "-16.3pp", "-46.5pp"]
          - ["r1-32b (Qwen2.5)", 0.453, 0.779, 0.752, "-7.5pp", "-22.6pp"]
          - ["QwQ-32B (Qwen2.5)", 0.407, 0.761, 0.734, "-7.5pp", "-24.1pp"]
    figures_description:
      - "Fig 7a: MD distribution for safe vs unsafe steps — separation visible on Qwen2.5, near-overlapping on Llama"
      - "Fig 7b: ROC curves for Mahalanobis vs static LR vs temporal LR — showing Mahalanobis between random and LR on Qwen2.5, near random on Llama"
    analysis: "Mahalanobis partially works on Qwen2.5 (40-45% coverage, AUROC 0.73-0.75) — this is the 'ambiguous sub-finding' of the median tier. The result is architecturally explained by signal concentration in leading PCs, which means TrajGuard-style detectors would have partial success on Qwen2.5 reasoning models but near-complete failure on Llama-based ones. Reframe Claim 1 to note that 'geometric detectors show architecture-dependent effectiveness correlated with PCA concentration of safety signal' rather than blanket failure. Temporal probes still dominate in all cases, preserving the core story."

  - name: "Bootstrap confidence intervals"
    plan_id: "exp-006"
    description: "1000 bootstrap resamples on all key metrics across all models and methods. Report 95% CIs to support statistical claims."
    expected_results:
      r1_8b_temporal_coverage_ci: [0.651, 0.872]
      r1_32b_temporal_coverage_ci: [0.553, 0.789]
      qwq_temporal_coverage_ci: [0.526, 0.763]
      r1_8b_delta_ci: [0.198, 0.412]
      r1_32b_delta_ci: [0.068, 0.237]
      qwq_delta_ci: [0.089, 0.251]
      r1_32b_lead_time_ci: [-1.47, 2.51]
      qwq_lead_time_ci: [-2.83, 1.38]
      r1_8b_lead_time_ci: [-2.91, 0.73]
      cross_transfer_llama_to_qwen_ci: [0.289, 0.553]
      mahalanobis_r1_32b_ci: [0.329, 0.574]
      n_resamples: 1000
      ci_method: "percentile bootstrap"
    result_rationale: "CIs are wide due to small test sets (38-43 traces) — this is expected and honest. Key implications: (1) The temporal advantage on Qwen2.5 is statistically significant (delta CI lower bound > 0 for both models), confirming the effect is real even if attenuated. (2) The r1-32b lead time CI spans [-1.47, 2.51], meaning the slightly positive mean (0.52) is NOT statistically distinguishable from zero — supporting 'near-zero' rather than 'positive' framing. (3) The delta CIs for Qwen2.5 [0.07, 0.24] vs Llama [0.20, 0.41] overlap at the boundary but are clearly shifted, supporting 'architecture-dependent magnitude' claim. (4) Mahalanobis CI on r1-32b spans 0.33-0.57, overlapping with static LR CI — the partial success claim needs careful hedging."
    tables:
      - name: "Table 8: Bootstrap 95% Confidence Intervals for Key Metrics"
        columns: ["Metric", "r1-8b", "r1-32b", "QwQ-32B"]
        rows:
          - ["Static Coverage", "[0.326, 0.605]", "[0.395, 0.658]", "[0.351, 0.612]"]
          - ["Temporal W=15 Coverage", "[0.651, 0.872]", "[0.553, 0.789]", "[0.526, 0.763]"]
          - ["Delta (Temporal - Static)", "[0.198, 0.412]", "[0.068, 0.237]", "[0.089, 0.251]"]
          - ["Lead Time Mean", "[-2.91, 0.73]", "[-1.47, 2.51]", "[-2.83, 1.38]"]
          - ["Mahalanobis Coverage", "[0.186, 0.421]", "[0.329, 0.574]", "[0.284, 0.532]"]
    figures_description:
      - "Fig 8: Forest plot showing point estimates with 95% CIs for all methods across all models — visual summary of effect sizes and uncertainty"
    analysis: "Bootstrap CIs confirm: (1) temporal advantage is statistically real on all architectures; (2) lead time is not distinguishable from zero on any model; (3) the attenuation on Qwen2.5 is real (non-overlapping CI centers) but not conclusively 'different' from Llama given sample sizes. This is methodologically honest — the paper can claim consistent improvement direction but must acknowledge power limitations. Recommend framing magnitude difference as 'observed' rather than 'statistically established' to avoid reviewer pushback on underpowered comparison."

  - name: "Window size ablation"
    plan_id: "exp-007"
    description: "Sweep W=1,3,5,10,15,20,25 on all 3 models. Identify architecture-specific optimal window and diminishing returns curve."
    expected_results:
      r1_8b_optimal_W: 15
      r1_8b_W_curve: {1: 0.465, 3: 0.535, 5: 0.651, 10: 0.698, 15: 0.767, 20: 0.744, 25: 0.721}
      r1_32b_optimal_W: 10
      r1_32b_W_curve: {1: 0.528, 3: 0.566, 5: 0.623, 10: 0.689, 15: 0.679, 20: 0.660, 25: 0.642}
      qwq_optimal_W: 10
      qwq_W_curve: {1: 0.482, 3: 0.519, 5: 0.593, 10: 0.667, 15: 0.648, 20: 0.630, 25: 0.611}
      r1_8b_saturation_W: 15
      qwen_saturation_W: 10
      overshoot_at_W25_qwen: "-3-4pp vs optimal"
    result_rationale: "Architecture-specific optimal windows emerge: Llama peaks at W=15, Qwen2.5 peaks at W=10. This reflects Qwen2.5's more concentrated signal geometry — shorter temporal context suffices because the safety-relevant information is more geometrically accessible per-step. Longer windows on Qwen2.5 actually HURT (overfitting to noise in the padded features) because the per-step signal is stronger, making the temporal redundancy in larger windows counterproductive. On Llama, the signal is more diffuse, requiring longer temporal context to accumulate enough evidence. This finding directly supports the 'architecture-specific optimal W' narrative and provides a practical recommendation for deployment (tune W per architecture). The diminishing returns curves have different shapes — Llama is concave with late saturation, Qwen2.5 saturates earlier and then declines."
    tables:
      - name: "Table 9: Window Size Ablation"
        columns: ["W", "r1-8b Cov", "r1-32b Cov", "QwQ Cov"]
        rows:
          - [1, 0.465, 0.528, 0.482]
          - [3, 0.535, 0.566, 0.519]
          - [5, 0.651, 0.623, 0.593]
          - [10, 0.698, 0.689, 0.667]
          - [15, 0.767, 0.679, 0.648]
          - [20, 0.744, 0.660, 0.630]
          - [25, 0.721, 0.642, 0.611]
    figures_description:
      - "Fig 9a: Coverage vs window size curves for all 3 models — showing different peaks and saturation patterns"
      - "Fig 9b: Normalized coverage (each model scaled to its maximum) — showing Qwen2.5 saturates 5 steps earlier than Llama"
    analysis: "Window ablation is the strongest evidence for architecture-specific signal dynamics. The finding that Qwen2.5 peaks at W=10 (vs Llama at W=15) is non-trivial and provides both theoretical insight (signal concentration determines required temporal context) and practical guidance (don't blindly use the same W cross-architecture). This supports reframing the paper's contribution as 'characterization + practical method' — the characterization reveals WHY architectures differ and HOW to adapt."

  - name: "Layer selection ablation"
    plan_id: "exp-008"
    description: "Evaluate temporal probe at all 64 layers of r1-32b (sampling every 4th layer: L4,L8,...,L64). Confirm middle-layer optimality finding generalizes from r1-8b."
    expected_results:
      best_layer_r1_32b: "L32"
      best_coverage_L32: 0.689
      layer_coverage_curve: {4: 0.412, 8: 0.478, 12: 0.534, 16: 0.587, 20: 0.623, 24: 0.651, 28: 0.672, 32: 0.689, 36: 0.681, 40: 0.668, 44: 0.645, 48: 0.612, 52: 0.578, 56: 0.534, 60: 0.489, 64: 0.423}
      relative_best_position: 0.50
      r1_8b_relative_best_position: 0.50
      early_layer_coverage: 0.412
      final_layer_coverage: 0.423
    result_rationale: "Middle-layer optimality generalizes: both architectures peak at the relative midpoint (L14/28 for r1-8b = 50%, L32/64 for r1-32b = 50%). This is expected from representation learning theory — middle layers encode semantic abstractions before task-specific decoding in later layers, and the safety reasoning state is a semantic-level concept. Early layers encode surface features (token identity), late layers encode output logits. The smooth bell curve with ~28pp range (41% to 69%) confirms layer choice matters and the finding is robust. This adds a practical recommendation: for new architectures, start at the 50% depth point."
    tables:
      - name: "Table 10: Layer Selection (r1-32b, W=10)"
        columns: ["Layer", "Relative Depth", "Coverage", "Accuracy"]
        rows:
          - ["L8", 0.125, 0.478, 0.784]
          - ["L16", 0.25, 0.587, 0.812]
          - ["L24", 0.375, 0.651, 0.834]
          - ["L32", 0.50, 0.689, 0.851]
          - ["L40", 0.625, 0.668, 0.841]
          - ["L48", 0.75, 0.612, 0.819]
          - ["L56", 0.875, 0.534, 0.793]
    figures_description:
      - "Fig 10: Coverage by relative layer depth — both r1-8b and r1-32b on same axis (normalized to 0-1 depth), showing overlapping bell curves peaking at 0.5"
    analysis: "Middle-layer optimality is a robust cross-architecture finding. The symmetric bell shape suggests safety state is encoded as a mid-level semantic abstraction, consistent across Llama and Qwen2.5. Practical implication: the 50% depth heuristic provides a reliable starting point for new architectures without expensive layer sweeps."

  - name: "16-label taxonomy supervision"
    plan_id: "exp-009"
    description: "Replace binary commitment labels with fine-grained 16-label taxonomy (Type 1-4 safety reasoning categories) for temporal probe training. Test whether richer supervision improves coverage or timing."
    expected_results:
      r1_8b_16label_coverage: 0.791
      r1_8b_16label_lead_mean: -0.82
      r1_8b_16label_acc_macro: 0.623
      r1_8b_binary_from_16label_coverage: 0.767
      r1_32b_16label_coverage: 0.704
      r1_32b_16label_lead_mean: 0.38
      r1_32b_binary_from_16label_coverage: 0.679
      improvement_over_binary: "+2.4pp on r1-8b, +2.5pp on r1-32b"
      label_confusion: "Type 2 (acknowledging harm) and Type 3 (refusing) most separable; Type 1 (reasoning about safety) confused with harmful reasoning"
    result_rationale: "16-label supervision provides marginal improvement (+2-3pp coverage) because the additional label structure helps the probe distinguish 'safety reasoning declining' from 'safety reasoning changing type.' However, the improvement is small because the binary commitment label already captures the key transition — the 16 categories provide redundant signal once the main safe→unsafe boundary is learned. Lead time doesn't meaningfully improve because the fundamental limitation (hidden states don't encode future trajectory) applies regardless of label granularity. The real value is interpretability: we can now characterize WHICH types of safety reasoning decline first (Type 1 reasoning-about-safety disappears before Type 3 refusal). This informs the Discussion but doesn't change core claims."
    tables:
      - name: "Table 11: Fine-Grained Label Supervision"
        columns: ["Model", "Supervision", "Coverage", "Lead Mean", "Macro Acc"]
        rows:
          - ["r1-8b", "Binary", 0.767, -1.09, 0.848]
          - ["r1-8b", "16-label", 0.791, -0.82, 0.623]
          - ["r1-32b", "Binary", 0.679, 0.52, 0.851]
          - ["r1-32b", "16-label", 0.704, 0.38, 0.631]
    figures_description:
      - "Fig 11: Confusion matrix for 16-label classifier showing which safety reasoning types are distinguishable in hidden-state space"
    analysis: "Fine-grained labels offer marginal quantitative improvement but meaningful qualitative insight. The finding that Type 1 (safety reasoning) is confused with harmful reasoning in hidden-state space is theoretically interesting — it suggests the model uses similar computational circuits for both. This supports including the 16-label experiment in the paper for interpretability value, but it doesn't change the core quantitative story."

  - name: "Oracle decomposition analysis"
    plan_id: "exp-010"
    description: "Analyze WHY the text-label oracle achieves +31 step lead time while hidden-state probes achieve ~0. Decompose oracle's advantage into specific label pattern features."
    expected_results:
      oracle_key_features: ["consecutive_safe_count_decline", "safe_label_density_in_window", "longest_unsafe_streak"]
      feature_importance_ranking: {consecutive_safe_decline: 0.41, density_in_W10: 0.28, longest_unsafe_streak: 0.19, type_diversity_decline: 0.12}
      oracle_ablation_no_future: "lead_mean drops from +31 to +2.1 when oracle only sees past labels"
      oracle_ablation_current_only: "lead_mean = -0.5 (similar to probe)"
      information_gap: "28.9 steps of lead come from FUTURE label visibility"
      hidden_state_mutual_info_with_future_labels: 0.043
    result_rationale: "The oracle's advantage is almost entirely from seeing FUTURE labels (+28.9 of +31 steps). When restricted to past-only labels, the oracle drops to +2.1 steps — only marginally better than hidden-state probes. This confirms the limitation is NOT that probes miss something in current hidden states, but that hidden states simply don't encode future safety trajectory. The mutual information between current hidden state and future labels (t+5 to t+15) is near-zero (0.043 bits), confirming there's no recoverable signal about the future. The implication: closing the gap requires either (a) future-label information (text monitoring), (b) multiple-step autoregressive hidden-state prediction, or (c) auxiliary training objectives that force the model to encode future safety trajectory."
    tables:
      - name: "Table 12: Oracle Decomposition"
        columns: ["Oracle Variant", "Lead Mean", "Coverage", "Information Source"]
        rows:
          - ["Full oracle (past+future)", 31, 1.0, "Complete label sequence"]
          - ["Past-only oracle", 2.1, 0.82, "Only labels at t≤current"]
          - ["Current-step oracle", -0.5, 0.73, "Only label at t=current"]
          - ["Hidden-state probe (W=15)", -1.09, 0.767, "Hidden states only"]
    figures_description:
      - "Fig 12: Stacked bar showing lead time decomposition — past-label contribution (2.1 steps) vs future-label contribution (28.9 steps)"
    analysis: "The decomposition conclusively establishes WHY pre-textual detection fails: 93% of the oracle's lead comes from future information that hidden states cannot contain. This is a principled impossibility argument — not a method failure but a fundamental information-theoretic limitation. The past-only oracle's +2.1 steps suggests a small ceiling for any hidden-state approach that could additionally incorporate label history (i.e., hybrid text+hidden-state monitors). This motivates future work directions in the Discussion section."

  - name: "OpenThinker-7B evaluation"
    plan_id: "exp-011"
    description: "4th model (Qwen2.5-7B base) to complete 2×2 architecture×scale matrix: {Llama-8B, Qwen2.5-7B} × {7-8B, 32B}. Controls for scale confound in cross-architecture comparison."
    expected_results:
      openthinker_7b_static_coverage: 0.512
      openthinker_7b_temporal_w10_coverage: 0.654
      openthinker_7b_temporal_w15_coverage: 0.641
      openthinker_7b_delta: 0.142
      openthinker_7b_lead_mean: -0.91
      openthinker_7b_fisher_orig: 10.12
      openthinker_7b_fisher_pca3: 2.37
      openthinker_7b_optimal_W: 10
      scale_effect_llama: "8B→32B not applicable (different base arch)"
      scale_effect_qwen: "7B vs 32B — coverage +1.6pp static, +3.5pp temporal (minimal scale effect)"
      architecture_effect_at_7_8B: "Llama-8B vs Qwen2.5-7B: -4.7pp static, +12.6pp temporal delta difference"
    result_rationale: "OpenThinker-7B (Qwen2.5-7B base) confirms the architecture effect is NOT a scale confound. At matched scale (7-8B), the same pattern holds: Qwen2.5 has higher static coverage (51% vs 47%) but lower temporal delta (14pp vs 30pp). The optimal window is W=10 (same as Qwen2.5-32B), further confirming this is an architecture-level property. Scale effect within Qwen2.5 is minimal (+1.6pp static, +3.5pp temporal from 7B→32B), ruling out the hypothesis that 'Qwen2.5 only attenuates because 32B models have different dynamics.' The 2×2 matrix cleanly separates architecture effect (dominant) from scale effect (minimal), strengthening the architectural analysis contribution."
    tables:
      - name: "Table 13: 2×2 Architecture × Scale Matrix"
        columns: ["Model", "Architecture", "Scale", "Static Cov", "Temporal Cov", "Delta", "Optimal W"]
        rows:
          - ["r1-8b", "Llama-3.1", "8B", 0.465, 0.767, "+30.2pp", 15]
          - ["OpenThinker-7B", "Qwen2.5", "7B", 0.512, 0.654, "+14.2pp", 10]
          - ["r1-32b", "Qwen2.5", "32B", 0.528, 0.689, "+16.1pp", 10]
          - ["QwQ-32B", "Qwen2.5", "32B", 0.482, 0.648, "+16.6pp", 10]
    figures_description:
      - "Fig 13: 2×2 interaction plot — architecture on x-axis, lines for 7-8B and 32B scale, showing parallel lines (no interaction) for temporal delta"
    analysis: "The 2×2 matrix is clean: architecture determines temporal advantage magnitude (30pp Llama vs 14-17pp Qwen2.5), while scale has minimal effect within architecture. This eliminates a key confound and strengthens the characterization story. The paper can now claim that the temporal advantage difference is an architecture-level property, likely related to how safety signal is geometrically organized in the representation space."

  - name: "GRU/Attention probe upper bound on 32B models"
    plan_id: "exp-012"
    description: "Train GRU (hidden=256) and self-attention probes on r1-32b and QwQ-32B to verify whether complex architectures offer improvement over temporal LR on Qwen2.5 base models."
    expected_results:
      r1_32b_gru_coverage: 0.698
      r1_32b_gru_lead_mean: 0.89
      r1_32b_gru_acc: 0.847
      r1_32b_attention_coverage: 0.685
      r1_32b_attention_lead_mean: 0.31
      qwq_gru_coverage: 0.667
      qwq_gru_lead_mean: -0.42
      qwq_attention_coverage: 0.654
      qwq_attention_lead_mean: -0.58
      gru_vs_lr_delta_r1_32b: "+1.9pp coverage"
      gru_vs_lr_delta_qwq: "+1.9pp coverage"
      gru_params: 1622913
      attention_params: 2105344
      lr_temporal_params: 77025
    result_rationale: "GRU provides marginal improvement (+1.9pp) over temporal LR on Qwen2.5, consistent with the r1-8b finding that complex architectures don't substantially help. The improvement is smaller than on Llama (where GRU gained ~3.7pp) because Qwen2.5's more concentrated signal is already well-captured by linear methods — the nonlinear capacity of GRU has less to exploit. Self-attention probe performs slightly WORSE than GRU (expected at this data scale — attention is data-hungry). The 'simplicity is optimal at current data scales' conclusion holds cross-architecture. The 20× parameter count of GRU (1.6M vs 77K) for <2pp improvement confirms the cost-benefit analysis favors temporal LR for practical deployment."
    tables:
      - name: "Table 14: Complex Probe Architectures on Qwen2.5 Models"
        columns: ["Model", "Method", "Params", "Coverage", "Lead Mean", "vs Temporal LR"]
        rows:
          - ["r1-32b", "Temporal LR (W=10)", "77K", 0.689, 0.52, "baseline"]
          - ["r1-32b", "GRU-256", "1.6M", 0.698, 0.89, "+0.9pp"]
          - ["r1-32b", "Self-Attention", "2.1M", 0.685, 0.31, "-0.4pp"]
          - ["QwQ-32B", "Temporal LR (W=10)", "77K", 0.667, -0.73, "baseline"]
          - ["QwQ-32B", "GRU-256", "1.6M", 0.667, -0.42, "+0.0pp"]
          - ["QwQ-32B", "Self-Attention", "2.1M", 0.654, -0.58, "-1.3pp"]
    figures_description:
      - "Fig 14: Pareto frontier (parameters vs coverage) — temporal LR dominates the efficiency frontier across all models"
    analysis: "Complex probes don't help on Qwen2.5, confirming the 'simplicity is optimal' finding generalizes. The slightly larger GRU improvement on r1-32b (+0.9pp coverage, +0.37 lead) compared to QwQ (+0.0pp, +0.31 lead) is within noise. Key takeaway: the 30pp temporal advantage ceiling on Llama and 15-17pp ceiling on Qwen2.5 appear to be INFORMATION limits, not model capacity limits — better probes can't extract signal that isn't there."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b027557-2408-404f-b9e0-b10ef7e0ebba",
  "isSidechain": false,
  "requestId": "req_011Cb6q7q7j5wWRm87egfhnv",
  "type": "assistant",
  "uuid": "ff23e545-2742-4f39-aa90-c1603dec13ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WqE6UjRaop1HRJYc9cC6nU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9941,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12468,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9941,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12468,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9941
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Temporal advantage exists on Qwen2.5 but is attenuated (~15-20pp vs 30pp); one sub-finding is ambiguous (e.g., lead time slightly positive on one model,…",
  "leafUuid": "ff23e545-2742-4f39-aa90-c1603dec13ac",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-architecture temporal safety detection evaluation",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Temporal advantage exists on Qwen2.5 but is attenuated (~15-20pp vs 30pp); one sub-finding is ambiguous (e.g., lead time slightly positive on one model,…",
  "leafUuid": "ff23e545-2742-4f39-aa90-c1603dec13ac",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-architecture temporal safety detection evaluation",
  "sessionId": "d6c1e890-618c-4116-9b83-2f70a530fbf0"
}
```

---
