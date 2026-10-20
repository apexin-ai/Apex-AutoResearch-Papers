# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Cross-architecture fails to generalize OR text baseline matches hidden stat

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/6a1d540a-fbc3-438b-b26f-022f1bea5636.jsonl`
- **Structured JSON:** [`f22c264db5e23121b01a.json`](../../sessions/f2/f22c264db5e23121b01a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T20:49:17.117Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T20:49:17.117Z",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Cross-architecture fails to generalize OR text baseline matches hidden states — core motivation undermined, need fundamental reframe\n核心假设：['Temporal LR coverage advantage does NOT replicate on 32B models (<15pp gap or temporal coverage <55%)', 'OR text baseline achieves ≥70% coverage, eliminating hidden-state unique value argument', 'BOCPD fails to improve over GRU (mean lead time <+3 or early detection <35%)', 'FPR >20% at operational threshold — precision-recall tradeoff makes deployment claims hollow', 'Cross-model transfer fails across architecture families (<40% retention)', 'At least one of: coverage gap collapses, text matches hidden states, or FPR invalidates coverage metric']\n关键指标范围：{'cross_arch_temporal_coverage': [0.4, 0.58], 'cross_arch_static_coverage': [0.35, 0.5], 'cross_arch_coverage_gap_pp': [0, 15], 'text_baseline_coverage': [0.65, 0.8], 'hidden_vs_text_gap_pp': [-5, 10], 'bocpd_lead_mean': [-1, 3], 'bocpd_early_detection_rate': [0.2, 0.38], 'fpr_at_70pct_coverage': [0.2, 0.35], 'trajguard_coverage': [0.25, 0.5], 'cross_transfer_retention': [0.2, 0.45], 'bootstrap_ci_width_coverage': [0.1, 0.18]}\n叙事方向：Reframe entirely — pivot from 'hidden-state probes detect commitment' to 'why is safety commitment detection fundamentally hard in reasoning models?' Contribution becomes a rigorous negative-result + analytical paper: (1) Fisher ratio 17→1 under PCA as geometry explanation for why detectors fail, (2) r1-8b temporal success as architecture-specific phenomenon requiring explanation, (3) oracle gap analysis as roadmap for future architectures. New angle: 'The Hidden Geometry Problem — Why Standard Probing Fails on Reasoning Model Safety'. Text-baseline parity reframed as 'hidden states don't add value BECAUSE the safety signal is already textually expressed in CoT — the real challenge is timing, not detection'. Still targets EMNLP main via the analytical/negative-result template (cf. Rogers et al. 2020 'BERTology' style). Emphasize the dataset contribution (HarmThoughts traces + commitment annotations) and the oracle analysis as community resources.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contrastive_trace_safety\nfocus: Key improvements since last dream: (1) GRU achieves +4.7 lead time (Claim 3 now 'unreliable positive' not 'no method achieves'), (2) text-based baseline added (exp-013) to prove hidden-state unique value, (3) BOCPD change-point detection added (exp-014) as novel method component addressing lead-time gap, (4) FPR analysis on safe traces added (exp-015), (5) expanded metrics: AUROC, PR curves, detection delay CDF. Related work now covers: Zou 2023 RepE, Arditi 2024 refusal direction, Lightman 2023 PRMs, Adams & MacKay 2007 BOCPD. Title will drop 'Contrastive'.\n\n## paper_framing.md\n\n# Paper Framing — contrastive_trace_safety\n\n## Target Venue\n- Primary: EMNLP 2026 Main (LLM Security Track)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR submission May 25, 2026 (9 days)\n\n## Core Claims (3 条)\n\n1. **Static hidden-state probes fail to reliably detect safety commitment in reasoning model traces** — static per-step probes (LogisticRegression, linear classifiers analogous to SafeSwitch/SIREN) achieve <50% detection coverage on the commitment detection task, despite hidden states containing strong safety-relevant signal (Fisher discriminant ratio 17-18 in full representation space).\n\n2. **Temporal window probes saturate oracle-achievable detection coverage** — a simple temporal window LogisticRegression (W=15 steps) achieves 76.7% detection coverage, matching the label-oracle upper bound. The +30pp improvement over static probes comes from capturing \"safety reasoning density decline\" patterns invisible to single-step classification.\n\n3. **Pre-textual detection of safety commitment remains unreliable despite positive mean lead time** — GRU sequence models achieve positive mean lead time (+4.7 steps) but with median 0, std 13, and only 39% (13/33) of detected traces achieving genuine early detection. The oracle's +31-step advantage (100% early detection) reveals a fundamental gap: hidden states encode current safety state well but poorly predict future safety trajectory. This establishes that reliable pre-textual detection requires architectural advances beyond current sequential models.\n\n## Story Spine\n\n- **Problem**: Reasoning models exhibit \"self-jailbreak\" — safety reasoning and harmful execution are interleaved throughout extended CoT (84% of traces contain safety labels after step 10), culminating in a \"commitment point\" where safety reasoning permanently ceases. Existing hidden-state jailbreak detectors (TrajGuard, SafeSwitch, SIREN) are designed for instruction-tuned models where the attack is an adversarial INPUT; they have never been evaluated on reasoning-model self-jailbreak where the attack is the model's OWN reasoning process.\n\n- **Existing approaches & their gaps**: Hidden-state detectors achieve 95% defense rate on standard LLMs (TrajGuard) but operate at token-level granularity. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon but doesn't provide deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No work bridges hidden-state detection TO reasoning-model self-jailbreak.\n\n- **Our framing**: We provide the first systematic evaluation of hidden-state detection methods on reasoning-model safety commitment, discovering that (a) the safety signal exists but is distributed across minor principal components (PCA top-3 explains only 17% variance, Fisher drops from 17→1), making geometric methods (Mahalanobis/TrajGuard) fail; (b) temporal context is critical — temporal window LR saturates coverage (+30pp), and GRU achieves positive lead time (+4.7 steps); (c) but pre-textual detection remains unreliable (median 0, only 39% early detection vs oracle 100%), establishing a principled gap between current capabilities and the oracle ceiling.\n\n- **Headline result template**: \"On HarmThoughts reasoning traces, temporal methods achieve 76.7% detection coverage (matching oracle ceiling) and +4.7 steps mean lead time, while static probes achieve only 46.5% coverage with negative lead time — but reliable pre-textual detection remains elusive (39% early detection rate vs oracle 100%, +4.7 vs +31 steps).\"\n\n## Venue Fit Risks\n\n- **EMNLP LLM Security track fit**: Strong — defense/detection method for reasoning model jailbreak, directly addressing \"defense lags behind attack\" gap noted in track CFP.\n- **Method simplicity risk**: Core methods are temporal LR (coverage) and GRU (lead time) — neither is architecturally novel. Mitigate: frame as empirical study with method insight; the contribution is the systematic evaluation + discovery of what matters (temporal context, adequate model capacity, multi-layer signal aggregation).\n- **Unreliable timing risk**: Claim 3 shows GRU achieves +4.7 mean lead time but median 0 and high variance. Mitigate: frame honestly as \"proof of concept for timing but currently unreliable\" — this motivates future work while contributing the coverage + limitation analysis now.\n- **Cross-architecture coverage**: MVP only tested on r1-8b (Llama-3.1 base). Must validate on Qwen2.5-based models (r1-32b, QwQ-32B) for the \"cross-architecture\" story. If temporal advantage doesn't hold cross-architecture → Claim 2 weakens to single-model.\n\n## Anticipated Reviewer Concerns\n\n1. \"Temporal window LR is trivial — where's the method novelty?\" → Primary contribution is empirical study; method insight is that simplicity matches oracle ceiling. Additionally, BOCPD on probe score sequences as a change-point detection approach adds a novel method component that could achieve positive lead time.\n2. \"Only tested on one model family\" → Cross-architecture experiments (P0) will address (4 models, 2 families, 2 scales).\n3. \"GRU lead time is unreliable (median 0, high variance)\" → Acknowledged; mean +4.7 shows the signal exists but is hard to extract reliably. The coverage contribution (+30pp) is robust. GRU lead time is presented as proof-of-concept, not deployed solution.\n4. \"209 training traces is too few — results may not generalize\" → Cross-model validation + bootstrap CIs + cross-validation with per-fold variance reporting.\n5. \"Why not use the full 16-label taxonomy for richer supervision?\" → Ablation planned (P1).\n6. \"How does hidden-state monitoring compare to text-based detection?\" → CRITICAL: Must include text-based baseline (sentence embeddings + temporal window LR on CoT text). If text achieves comparable performance, hidden-state motivation collapses. Hypothesis: hidden states capture pre-textual signal that text cannot.\n7. \"Commitment point definition is circular / tautological\" → CP defined as last safety label + 1; probe detects sustained absence of safety reasoning. Mitigate: (a) discuss what CP corresponds to behaviorally, (b) report detection delay distribution showing probes fire at/after CP not just because of label definition, (c) cross-model consistency suggests real phenomenon not annotation artifact.\n8. \"Missing related work on representation engineering, PRMs, change-point detection\" → Must cite: Zou et al. 2023 (RepE), Arditi et al. 2024 (refusal direction), Lightman et al. 2023 (PRMs/step-level supervision), Adams & MacKay 2007 (BOCPD), Hewitt & Liang 2019 (control tasks for probing).\n9. \"No false positive analysis — deployment utility unknown\" → Must report FPR on safe traces (final_judgment=0.5) and precision-recall curves alongside coverage.\n\n## Title Note\nDrop \"Contrastive\" from title — no contrastive learning is employed. Candidate: \"Temporal Probing for Safety Commitment Detection in Reasoning Models\" or \"Hidden-State Detection of Safety Commitment in Reasoning Models: When Does Temporal Context Matter?\"\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: Cross-architecture hidden-state extraction + layer sweep + static probe\n    evaluation on r1-32b and QwQ-32B. Includes mandatory layer sweep (all layers)\n    to find best layer for 64-layer models before probe evaluation. Validates Claim\n    1 generalizes beyond r1-8b.\n  priority: P0\n  gpu_budget_hours: 10\n  deps: []\n  models:\n  - DeepSeek-R1-Distill-Qwen-32B\n  - QwQ-32B\n  notes: 32B models have 64 layers, 5120-d hidden. r1-8b best layer was 14/32 (44%\n    depth) → expect best around layer 28-32 for 64-layer models. Extract ALL layers\n    for sweep, then select best for subsequent experiments. Must do layer sweep BEFORE\n    reporting static probe results — using wrong layer would produce false negative.\n  status: planned\n- id: exp-002\n  claim: 2\n  description: 'Cross-architecture temporal window evaluation: temporal LR W=15 on\n    r1-32b and QwQ-32B. Validate +30pp coverage improvement holds cross-architecture.'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  models:\n  - DeepSeek-R1-Distill-Qwen-32B\n  - QwQ-32B\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: train probe on r1-8b (Llama), test on r1-32b/QwQ\n    (Qwen2.5). Train on Qwen, test on Llama. Measures zero-shot cross-architecture\n    generalization.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Key for cross-architecture story. Projection head needed (4096→5120 or vice\n    versa).\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Lead time analysis across models: confirm negative lead time finding\n    on 32B models. Report lead time distribution per model.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'TrajGuard-style Mahalanobis baseline: implement and evaluate on all\n    3 models. Expected to fail (signal in minor PCs, Fisher drops 17→1 in PCA-3D).'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Critical baseline for 'existing detectors fail' claim. Use safe traces to\n    estimate covariance, compute MD per step.\n  status: planned\n- id: exp-006\n  claim:\n  - 1\n  - 2\n  description: 'Bootstrap confidence intervals + threshold-independent metrics: 1000\n    bootstrap resamples on all key metrics (coverage, lead time, accuracy). ALSO report\n    AUROC, precision-recall curves, detection delay CDF, cross-validation per-fold\n    variance, and FPR on safe traces (final_judgment=0.5).'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  - exp-004\n  - exp-005\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Window size ablation: W=1,3,5,10,15,20,25 on all 3 models. Find optimal\n    W and show diminishing returns curve.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Layer selection ablation: all layers (not just 14) for temporal probe\n    on 32B models. Confirm middle-layer finding generalizes.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  claim: 2\n  description: '16-label taxonomy supervision: use fine-grained labels (Type 1/2/3/4)\n    instead of binary commitment for richer training signal. May improve both coverage\n    and timing.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Addresses reviewer concern about underusing available supervision.\n  status: planned\n- id: exp-010\n  claim: 3\n  description: 'Oracle decomposition: why can oracle but not probes achieve positive\n    lead time? Analyze what label patterns encode that hidden states don''t.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-004\n  notes: For Discussion section. May reveal what architectural changes could close\n    the gap.\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'OpenThinker-7B (Qwen2.5-7B base): 4th model for 2×2 architecture×scale\n    matrix. Controls for scale confound.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-002\n  notes: From Human Review Note point 5. Adds Qwen2.5-7B to complement Llama-8B for\n    scale-matched comparison.\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'GRU/Attention probe as upper bound: verify GRU finding holds on 32B\n    models with more data. If still no improvement over LR, strengthens ''simplicity\n    is optimal'' story.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Text-based baseline: sentence-BERT embeddings (all-MiniLM-L6-v2) +\n    same temporal window LR (W=15) on CoT text. Compare coverage/lead time to hidden-state\n    probes. CRITICAL for proving hidden-state monitoring adds unique value over cheap\n    text monitoring. If text achieves comparable performance, paper motivation needs\n    restructuring.'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps: []\n  notes: No GPU needed for embedding extraction (small model, CPU-feasible). Run on\n    all 4 models. This is the single most important missing baseline per Dream review\n    (flagged by all 3 tiers, both reviewers).\n  status: planned\n- id: exp-014\n  claim: 3\n  description: 'Bayesian Online Change-Point Detection (BOCPD) on per-step probe scores:\n    apply Adams & MacKay 2007 to the sequence of probe confidence scores. Could achieve\n    positive lead time by detecting distributional shift before textual commitment.\n    Also test CUSUM as simpler alternative.'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - exp-001\n  notes: Addresses both 'no method novelty' and 'no positive lead time' criticisms\n    simultaneously. If BOCPD achieves reliable lead time where GRU doesn't, this becomes\n    a genuine methods contribution. If it also fails, strengthens the 'fundamental\n    limitation' narrative.\n  status: planned\n- id: exp-015\n  claim:\n  - 1\n  - 2\n  description: 'False positive analysis: run all probes (static, temporal, GRU, BOCPD)\n    on safe traces (final_judgment=0.5). Report FPR, precision-recall curves at various\n    thresholds. Essential for deployment utility claims.'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - exp-001\n  - exp-002\n  notes: Dream flagged missing FPR as critical gap across median and worst tiers.\n    Without this, 'coverage' metric is uninterpretable — a probe that fires everywhere\n    gets 100% coverage.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: diag_d1_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    best_layer_idx: 2\n    best_model_layer: 14\n    best_acc: 0.8114\n    best_f1: 0.6455\n    best_crossing_rate: 0.186\n    best_lead_mean: 8.38\n    best_lead_median: 6\n    default_layer20_acc: 0.7831\n    num_traces: 209\n    split: 125/41/43\n- exp_id: diag_d4_oracle_upper_bound\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K5_detection_rate: 100\n    K5_early_detection_rate: 76.7\n    K5_mean_lead_time: 31\n    K5_median_lead_time: 29\n    K1_early_detection_rate: 83.7\n    K8_early_detection_rate: 65.1\n    pre_cp_mean_longest_streak: 14.6\n    test_traces: 43\n- exp_id: diag_d2_pca_viz\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fisher_orig_L12: 17.462\n    fisher_orig_L14: 17.875\n    fisher_orig_L20: 18.614\n    fisher_orig_L24: 18.106\n    fisher_pca_L12: 0.953\n    fisher_pca_L14: 0.928\n    fisher_pca_L20: 0.92\n    fisher_pca_L24: 1.111\n    var_explained_3pc: 0.166\n    test_steps: 1835\n- exp_id: diag_d3_regularized_probes\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    static_lr_acc: 0.8172\n    static_lr_crossing_rate: 0.4651\n    static_lr_lead_mean: -2\n    temporal_lr_w5_acc: 0.8274\n    temporal_lr_w5_crossing_rate: 0.6512\n    temporal_lr_w5_lead_mean: -1.18\n    temporal_lr_w10_acc: 0.8364\n    temporal_lr_w10_crossing_rate: 0.6512\n    temporal_lr_w10_lead_mean: -0.61\n    temporal_lr_w15_acc: 0.8478\n    temporal_lr_w15_crossing_rate: 0.7674\n    temporal_lr_w15_lead_mean: -1.09\n    best_temporal_delta_over_static: 1.39\n    pass_criterion_met: false\n- exp_id: diag_gru_probe\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.8305\n    test_acc_std: 0.1856\n    crossing_rate: 0.6744\n    lead_mean: -0.207\n    lead_median: -1\n    lead_std: 13\n    positive_lead_rate: 0.345\n    n_positive_lead: 10\n    n_detected: 29\n    early_stop_epoch: 14\n    model_params: 1622913\n- exp_id: exp_gru256_multilayer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gru_single_l14:\n      acc: 0.8386\n      crossing_rate: 0.721\n      lead_mean: 3.5\n      lead_median: 0\n      pos_lead: 13/31\n    gru_multi_7l:\n      acc: 0.8094\n      crossing_rate: 0.767\n      lead_mean: 4.7\n      lead_median: 0\n      pos_lead: 13/33\n    lr_single_l14:\n      acc: 0.8172\n      crossing_rate: 0.465\n      lead_mean: -2\n      lead_median: -2\n      pos_lead: 6/20\n    lr_multi_7l:\n      acc: 0.806\n      crossing_rate: 0.395\n      lead_mean: 1.1\n      lead_median: 0\n      pos_lead: 6/17\n    delta_gru_vs_lr: 3.7\n- exp_id: exp_005_trajguard_mahalanobis\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_006_bootstrap_ci\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T20:49:17.120Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T20:49:17.120Z",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-16T20:49:17.143Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Cross-architecture fails to generalize OR text baseline matches hidden states — core motivation undermined, need fundamental reframe
核心假设：['Temporal LR coverage advantage does NOT replicate on 32B models (<15pp gap or temporal coverage <55%)', 'OR text baseline achieves ≥70% coverage, eliminating hidden-state unique value argument', 'BOCPD fails to improve over GRU (mean lead time <+3 or early detection <35%)', 'FPR >20% at operational threshold — precision-recall tradeoff makes deployment claims hollow', 'Cross-model transfer fails across architecture families (<40% retention)', 'At least one of: coverage gap collapses, text matches hidden states, or FPR invalidates coverage metric']
关键指标范围：{'cross_arch_temporal_coverage': [0.4, 0.58], 'cross_arch_static_coverage': [0.35, 0.5], 'cross_arch_coverage_gap_pp': [0, 15], 'text_baseline_coverage': [0.65, 0.8], 'hidden_vs_text_gap_pp': [-5, 10], 'bocpd_lead_mean': [-1, 3], 'bocpd_early_detection_rate': [0.2, 0.38], 'fpr_at_70pct_coverage': [0.2, 0.35], 'trajguard_coverage': [0.25, 0.5], 'cross_transfer_retention': [0.2, 0.45], 'bootstrap_ci_width_coverage': [0.1, 0.18]}
叙事方向：Reframe entirely — pivot from 'hidden-state probes detect commitment' to 'why is safety commitment detection fundamentally hard in reasoning models?' Contribution becomes a rigorous negative-result + analytical paper: (1) Fisher ratio 17→1 under PCA as geometry explanation for why detectors fail, (2) r1-8b temporal success as architecture-specific phenomenon requiring explanation, (3) oracle gap analysis as roadmap for future architectures. New angle: 'The Hidden Geometry Problem — Why Standard Probing Fails on Reasoning Model Safety'. Text-baseline parity reframed as 'hidden states don't add value BECAUSE the safety signal is already textually expressed in CoT — the real challenge is timing, not detection'. Still targets EMNLP main via the analytical/negative-result template (cf. Rogers et al. 2020 'BERTology' style). Emphasize the dataset contribution (HarmThoughts traces + commitment annotations) and the oracle analysis as community resources.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: contrastive_trace_safety
focus: Key improvements since last dream: (1) GRU achieves +4.7 lead time (Claim 3 now 'unreliable positive' not 'no method achieves'), (2) text-based baseline added (exp-013) to prove hidden-state unique value, (3) BOCPD change-point detection added (exp-014) as novel method component addressing lead-time gap, (4) FPR analysis on safe traces added (exp-015), (5) expanded metrics: AUROC, PR curves, detection delay CDF. Related work now covers: Zou 2023 RepE, Arditi 2024 refusal direction, Lightman 2023 PRMs, Adams & MacKay 2007 BOCPD. Title will drop 'Contrastive'.

## paper_framing.md

# Paper Framing — contrastive_trace_safety

## Target Venue
- Primary: EMNLP 2026 Main (LLM Security Track)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR submission May 25, 2026 (9 days)

## Core Claims (3 条)

1. **Static hidden-state probes fail to reliably detect safety commitment in reasoning model traces** — static per-step probes (LogisticRegression, linear classifiers analogous to SafeSwitch/SIREN) achieve <50% detection coverage on the commitment detection task, despite hidden states containing strong safety-relevant signal (Fisher discriminant ratio 17-18 in full representation space).

2. **Temporal window probes saturate oracle-achievable detection coverage** — a simple temporal window LogisticRegression (W=15 steps) achieves 76.7% detection coverage, matching the label-oracle upper bound. The +30pp improvement over static probes comes from capturing "safety reasoning density decline" patterns invisible to single-step classification.

3. **Pre-textual detection of safety commitment remains unreliable despite positive mean lead time** — GRU sequence models achieve positive mean lead time (+4.7 steps) but with median 0, std 13, and only 39% (13/33) of detected traces achieving genuine early detection. The oracle's +31-step advantage (100% early detection) reveals a fundamental gap: hidden states encode current safety state well but poorly predict future safety trajectory. This establishes that reliable pre-textual detection requires architectural advances beyond current sequential models.

## Story Spine

- **Problem**: Reasoning models exhibit "self-jailbreak" — safety reasoning and harmful execution are interleaved throughout extended CoT (84% of traces contain safety labels after step 10), culminating in a "commitment point" where safety reasoning permanently ceases. Existing hidden-state jailbreak detectors (TrajGuard, SafeSwitch, SIREN) are designed for instruction-tuned models where the attack is an adversarial INPUT; they have never been evaluated on reasoning-model self-jailbreak where the attack is the model's OWN reasoning process.

- **Existing approaches & their gaps**: Hidden-state detectors achieve 95% defense rate on standard LLMs (TrajGuard) but operate at token-level granularity. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon but doesn't provide deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No work bridges hidden-state detection TO reasoning-model self-jailbreak.

- **Our framing**: We provide the first systematic evaluation of hidden-state detection methods on reasoning-model safety commitment, discovering that (a) the safety signal exists but is distributed across minor principal components (PCA top-3 explains only 17% variance, Fisher drops from 17→1), making geometric methods (Mahalanobis/TrajGuard) fail; (b) temporal context is critical — temporal window LR saturates coverage (+30pp), and GRU achieves positive lead time (+4.7 steps); (c) but pre-textual detection remains unreliable (median 0, only 39% early detection vs oracle 100%), establishing a principled gap between current capabilities and the oracle ceiling.

- **Headline result template**: "On HarmThoughts reasoning traces, temporal methods achieve 76.7% detection coverage (matching oracle ceiling) and +4.7 steps mean lead time, while static probes achieve only 46.5% coverage with negative lead time — but reliable pre-textual detection remains elusive (39% early detection rate vs oracle 100%, +4.7 vs +31 steps)."

## Venue Fit Risks

- **EMNLP LLM Security track fit**: Strong — defense/detection method for reasoning model jailbreak, directly addressing "defense lags behind attack" gap noted in track CFP.
- **Method simplicity risk**: Core methods are temporal LR (coverage) and GRU (lead time) — neither is architecturally novel. Mitigate: frame as empirical study with method insight; the contribution is the systematic evaluation + discovery of what matters (temporal context, adequate model capacity, multi-layer signal aggregation).
- **Unreliable timing risk**: Claim 3 shows GRU achieves +4.7 mean lead time but median 0 and high variance. Mitigate: frame honestly as "proof of concept for timing but currently unreliable" — this motivates future work while contributing the coverage + limitation analysis now.
- **Cross-architecture coverage**: MVP only tested on r1-8b (Llama-3.1 base). Must validate on Qwen2.5-based models (r1-32b, QwQ-32B) for the "cross-architecture" story. If temporal advantage doesn't hold cross-architecture → Claim 2 weakens to single-model.

## Anticipated Reviewer Concerns

1. "Temporal window LR is trivial — where's the method novelty?" → Primary contribution is empirical study; method insight is that simplicity matches oracle ceiling. Additionally, BOCPD on probe score sequences as a change-point detection approach adds a novel method component that could achieve positive lead time.
2. "Only tested on one model family" → Cross-architecture experiments (P0) will address (4 models, 2 families, 2 scales).
3. "GRU lead time is unreliable (median 0, high variance)" → Acknowledged; mean +4.7 shows the signal exists but is hard to extract reliably. The coverage contribution (+30pp) is robust. GRU lead time is presented as proof-of-concept, not deployed solution.
4. "209 training traces is too few — results may not generalize" → Cross-model validation + bootstrap CIs + cross-validation with per-fold variance reporting.
5. "Why not use the full 16-label taxonomy for richer supervision?" → Ablation planned (P1).
6. "How does hidden-state monitoring compare to text-based detection?" → CRITICAL: Must include text-based baseline (sentence embeddings + temporal window LR on CoT text). If text achieves comparable performance, hidden-state motivation collapses. Hypothesis: hidden states capture pre-textual signal that text cannot.
7. "Commitment point definition is circular / tautological" → CP defined as last safety label + 1; probe detects sustained absence of safety reasoning. Mitigate: (a) discuss what CP corresponds to behaviorally, (b) report detection delay distribution showing probes fire at/after CP not just because of label definition, (c) cross-model consistency suggests real phenomenon not annotation artifact.
8. "Missing related work on representation engineering, PRMs, change-point detection" → Must cite: Zou et al. 2023 (RepE), Arditi et al. 2024 (refusal direction), Lightman et al. 2023 (PRMs/step-level supervision), Adams & MacKay 2007 (BOCPD), Hewitt & Liang 2019 (control tasks for probing).
9. "No false positive analysis — deployment utility unknown" → Must report FPR on safe traces (final_judgment=0.5) and precision-recall curves alongside coverage.

## Title Note
Drop "Contrastive" from title — no contrastive learning is employed. Candidate: "Temporal Probing for Safety Commitment Detection in Reasoning Models" or "Hidden-State Detection of Safety Commitment in Reasoning Models: When Does Temporal Context Matter?"


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  description: Cross-architecture hidden-state extraction + layer sweep + static probe
    evaluation on r1-32b and QwQ-32B. Includes mandatory layer sweep (all layers)
    to find best layer for 64-layer models before probe evaluation. Validates Claim
    1 generalizes beyond r1-8b.
  priority: P0
  gpu_budget_hours: 10
  deps: []
  models:
  - DeepSeek-R1-Distill-Qwen-32B
  - QwQ-32B
  notes: 32B models have 64 layers, 5120-d hidden. r1-8b best layer was 14/32 (44%
    depth) → expect best around layer 28-32 for 64-layer models. Extract ALL layers
    for sweep, then select best for subsequent experiments. Must do layer sweep BEFORE
    reporting static probe results — using wrong layer would produce false negative.
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
  description: 'Bootstrap confidence intervals + threshold-independent metrics: 1000
    bootstrap resamples on all key metrics (coverage, lead time, accuracy). ALSO report
    AUROC, precision-recall curves, detection delay CDF, cross-validation per-fold
    variance, and FPR on safe traces (final_judgment=0.5).'
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
- id: exp-013
  claim:
  - 1
  - 2
  description: 'Text-based baseline: sentence-BERT embeddings (all-MiniLM-L6-v2) +
    same temporal window LR (W=15) on CoT text. Compare coverage/lead time to hidden-state
    probes. CRITICAL for proving hidden-state monitoring adds unique value over cheap
    text monitoring. If text achieves comparable performance, paper motivation needs
    restructuring.'
  priority: P0
  gpu_budget_hours: 0.5
  deps: []
  notes: No GPU needed for embedding extraction (small model, CPU-feasible). Run on
    all 4 models. This is the single most important missing baseline per Dream review
    (flagged by all 3 tiers, both reviewers).
  status: planned
- id: exp-014
  claim: 3
  description: 'Bayesian Online Change-Point Detection (BOCPD) on per-step probe scores:
    apply Adams & MacKay 2007 to the sequence of probe confidence scores. Could achieve
    positive lead time by detecting distributional shift before textual commitment.
    Also test CUSUM as simpler alternative.'
  priority: P0
  gpu_budget_hours: 0.5
  deps:
  - exp-001
  notes: Addresses both 'no method novelty' and 'no positive lead time' criticisms
    simultaneously. If BOCPD achieves reliable lead time where GRU doesn't, this becomes
    a genuine methods contribution. If it also fails, strengthens the 'fundamental
    limitation' narrative.
  status: planned
- id: exp-015
  claim:
  - 1
  - 2
  description: 'False positive analysis: run all probes (static, temporal, GRU, BOCPD)
    on safe traces (final_judgment=0.5). Report FPR, precision-recall curves at various
    thresholds. Essential for deployment utility claims.'
  priority: P0
  gpu_budget_hours: 0.5
  deps:
  - exp-001
  - exp-002
  notes: Dream flagged missing FPR as critical gap across median and worst tiers.
    Without this, 'coverage' metric is uninterpretable — a probe that fires everywhere
    gets 100% coverage.
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
- exp_id: exp_005_trajguard_mahalanobis
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp_006_bootstrap_ci
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}

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
  "promptId": "9a54ff95-87f5-4d7c-9c92-dda2087e20f6",
  "type": "user",
  "uuid": "ffce016b-a9a4-4476-ad04-febe788c3cfa",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T20:49:17.142Z_

```json
{
  "parentUuid": "ffce016b-a9a4-4476-ad04-febe788c3cfa",
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
  "uuid": "9469a268-eb66-4725-b648-de31d958b19d",
  "timestamp": "2026-05-16T20:49:17.142Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T20:49:17.142Z_

```json
{
  "parentUuid": "9469a268-eb66-4725-b648-de31d958b19d",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "88749417-2bdb-4632-bcb1-bda3548ace32",
  "timestamp": "2026-05-16T20:49:17.142Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T20:49:17.142Z_

```json
{
  "parentUuid": "88749417-2bdb-4632-bcb1-bda3548ace32",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b3836c12-f27c-4e48-b905-c1ccf1df625e",
  "timestamp": "2026-05-16T20:49:17.142Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Cross-architecture fails to generalize OR text baseline matches hidden states — core motivation undermined, need fundamental reframe 核心假设：['Temporal LR co…",
  "leafUuid": "b3836c12-f27c-4e48-b905-c1ccf1df625e",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Safety commitment detection in reasoning models: temporal context and fundamental limits",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636"
}
```

---

### Assistant

_source line 9 · 2026-05-16T20:49:50.331Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for the "worst" tier for all planned experiments in the experiment plan. I need to carefully go through each planned experiment and generate realistic worst-case results with rationales.

Let me identify all planned experiments:
- exp-001: Cross-architecture hidden-state extraction + layer sweep + static probe on r1-32b and QwQ-32B
- exp-002: Cross-architecture temporal window evaluation
- exp-003: Cross-model transfer
- exp-004: Lead time analysis across models
- exp-005: TrajGuard-style Mahalanobis baseline (status: PREPARING)


- exp-006: Bootstrap confidence intervals (status: PREPARING)
- exp-007: Window size ablation
- exp-008: Layer selection ablation
- exp-009: 16-label taxonomy supervision
- exp-010: Oracle decomposition
- exp-011: OpenThinker-7B
- exp-012: GRU/Attention probe as upper bound
- exp-013: Text-based baseline
- exp-014: BOCPD on per-step probe scores
- exp-015: False positive analysis

I should generate worst-case data for all of these, including exp-005 and exp-006 which are still in preparation. For the worst tier, I'm thinking about scenarios where the methods perform poorly—high false positives, low detection rates, poor generalization across models, and minimal improvement over baselines. Now I'm looking at the metric ranges for the remaining variables—text baseline coverage gap, BOCPD performance, FPR at different thresholds, and cross-model transfer retention. I need to generate consistent experimental data across all conditions that reinforces the narrative: the temporal advantage doesn't hold on larger models, text baselines become competitive, and the core findings don't generalize. a fundamental reframe to a negative-result paper.

Let me go through each experiment:

**exp-001**: Cross-architecture static probes on r1-32b and QwQ-32B
- In worst case, static probes on 32B models perform poorly but not dramatically worse than r1-8b
- Best layer might be different (around 28-32 for 64-layer models)
- Static coverage around 0.35-0.45
- Fisher ratio might be lower than r1-8b

**exp-002**: Temporal LR W=15 on 32B models
- In worst case, temporal advantage collapses: coverage only 0.40-0.55, gap over static <15pp
- The temporal context that helped on r1-8b doesn't generalize

**exp-003**: Cross-model transfer
- Transfer fails: <40% retention
- Projection head adds noise

**exp-004**: Lead time on 32B
- Negative lead time, worse than r1-8b

**exp-005**: TrajGuard Mahalanobis
- Fails as expected, but interestingly not much worse than probes on 32B

**exp-006**: Bootstrap CIs
- Wide CIs, coverage gap not significant

**exp-007**: Window ablation
- Diminishing returns, but also shows instability on 32B

**exp-008**: Layer ablation
- No clear middle-layer advantage on 32B

**exp-009**: 16-label taxonomy
- Doesn't help much

**exp-010**: Oracle decomposition
- Shows fundamental gap

**exp-011**: OpenThinker-7B
- Also poor results

**exp-012**: GRU upper bound on 32B
- GRU doesn't improve over L

**exp-013**: Text baseline
- Text achieves ≥70% coverage, matching or exceeding hidden states
- This is the killer result

**exp-014**: BOCPD
- Fails to improve lead time meaningfully

**exp-015**: FPR analysis
- FPR >20% at operational thresholds

Now I'm looking at the text baseline results—text alone gets 70% coverage, which actually matches or beats the hidden state approach. That's the critical finding that undermines the whole hidden state strategy. Then checking the false positive rate analysis shows we're hitting >20% FPR at the thresholds we'd actually use in practice.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3836c12-f27c-4e48-b905-c1ccf1df625e",
  "isSidechain": false,
  "requestId": "req_011Cb6uXBhaZeoAutAW3sYye",
  "type": "assistant",
  "uuid": "6f1e31ed-0d6c-48d0-bdbe-71bc2ee410be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AyE4SsjEkZPmLWQ2GhXMh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11909,
      "cache_read_input_tokens": 11447,
      "output_tokens": 18027,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18027,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11909
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

_source line 10 · 2026-05-16T20:55:09.332Z_

```yaml
tier: worst
narrative_guidance: >
  Reframe entirely — pivot from 'hidden-state probes detect commitment' to 'why is safety commitment detection
  fundamentally hard in reasoning models?' Contribution becomes a rigorous negative-result + analytical paper:
  (1) Fisher ratio 17→1 under PCA as geometry explanation for why detectors fail,
  (2) r1-8b temporal success as architecture-specific phenomenon requiring explanation,
  (3) oracle gap analysis as roadmap for future architectures.
  New angle: 'The Hidden Geometry Problem — Why Standard Probing Fails on Reasoning Model Safety'.
  Text-baseline parity reframed as 'hidden states don't add value BECAUSE the safety signal is already
  textually expressed in CoT — the real challenge is timing, not detection'.
  Still targets EMNLP main via the analytical/negative-result template (cf. Rogers et al. 2020 'BERTology' style).
  Emphasize the dataset contribution (HarmThoughts traces + commitment annotations) and oracle analysis as community resources.

imagined_experiments:
  - name: "Cross-Architecture Static Probe (32B Models)"
    plan_id: "exp-001"
    description: >
      Hidden-state extraction on r1-32b (DeepSeek-R1-Distill-Qwen-32B) and QwQ-32B.
      Full 64-layer sweep to identify best probe layer, then static LogisticRegression evaluation.
    expected_results:
      r1_32b_best_layer_idx: 30
      r1_32b_best_layer_depth_pct: 0.469
      r1_32b_best_acc: 0.762
      r1_32b_best_f1: 0.571
      r1_32b_crossing_rate: 0.385
      r1_32b_lead_mean: -3.8
      r1_32b_lead_median: -4
      r1_32b_fisher_orig: 11.3
      r1_32b_fisher_pca3: 0.61
      r1_32b_var_explained_3pc: 0.092
      qwq_32b_best_layer_idx: 28
      qwq_32b_best_layer_depth_pct: 0.438
      qwq_32b_best_acc: 0.749
      qwq_32b_best_f1: 0.548
      qwq_32b_crossing_rate: 0.361
      qwq_32b_lead_mean: -4.5
      qwq_32b_lead_median: -5
      qwq_32b_fisher_orig: 9.7
      qwq_32b_fisher_pca3: 0.48
      qwq_32b_var_explained_3pc: 0.078
      num_traces_r1_32b: 209
      num_traces_qwq: 209
    result_rationale: >
      32B Qwen2.5-base models have 5120-d hidden states (vs 4096-d Llama). The higher dimensionality
      disperses the safety signal across even more minor principal components — PCA top-3 explains
      only 7.8-9.2% variance (vs 16.6% on r1-8b). Fisher discriminant ratio drops from 17-18 on
      r1-8b to 9.7-11.3 in full space, and collapses further to 0.48-0.61 under PCA-3D.
      The Qwen2.5 architecture's GQA attention and different layer normalization scheme produces
      a more isotropic representation geometry, making linear separability harder. Static coverage
      (crossing_rate) drops to 36-39% — worse than r1-8b's 46.5% — because the commitment signal
      is more diffuse in higher-dimensional space. Best layer still falls near 44% depth, consistent
      with r1-8b, but the absolute performance is substantially worse. This confirms that static
      probes fail even more severely on larger Qwen2.5-based reasoning models.
    tables:
      - name: "Table 3: Cross-Architecture Static Probe Results"
        columns: ["Model", "Base Arch", "Dim", "Best Layer", "Depth%", "Acc", "F1", "Coverage", "Lead Mean", "Fisher_orig", "Fisher_PCA3"]
        rows:
          - ["r1-8b", "Llama-3.1", 4096, "L14", "43.8%", 0.817, 0.646, "46.5%", -2.0, 17.9, 0.93]
          - ["r1-32b", "Qwen2.5", 5120, "L30", "46.9%", 0.762, 0.571, "38.5%", -3.8, 11.3, 0.61]
          - ["QwQ-32B", "Qwen2.5", 5120, "L28", "43.8%", 0.749, 0.548, "36.1%", -4.5, 9.7, 0.48]
    figures_description:
      - "Layer sweep curves (accuracy vs layer index) for r1-32b and QwQ-32B, showing broad plateau at layers 24-36 with peak around 28-30, contrasted with r1-8b's sharper peak at L14. Both 32B models show lower absolute accuracy across all layers."
      - "Fisher discriminant ratio comparison: bar chart showing full-space vs PCA-3D Fisher ratios across 3 models. Dramatic collapse in all models under PCA, but 32B models start lower and fall further."
    analysis: >
      Static probes degrade on Qwen2.5-based 32B models. The coverage drop from 46.5% to 36-39%
      is concerning — it means existing hidden-state detectors would miss 61-64% of commitment
      points on production-scale reasoning models. The Fisher ratio degradation (17→11→10) suggests
      the safety signal becomes progressively harder to linearly separate at scale. This could be
      due to (1) Qwen2.5's more isotropic representations from GQA, (2) richer non-safety features
      in higher dimensions diluting the signal, or (3) genuine architectural differences in how
      safety reasoning is encoded. The finding that best layer depth% is consistent (~44%) across
      architectures is one of the few positive transfer signals.

  - name: "Cross-Architecture Temporal Window Probe (32B Models)"
    plan_id: "exp-002"
    description: >
      Temporal LogisticRegression with W=15 on r1-32b and QwQ-32B at their respective best layers.
      Tests whether the +30pp temporal advantage from r1-8b generalizes.
    expected_results:
      r1_32b_temporal_acc: 0.793
      r1_32b_temporal_crossing_rate: 0.50
      r1_32b_temporal_lead_mean: -2.1
      r1_32b_temporal_delta_over_static_pp: 11.5
      qwq_32b_temporal_acc: 0.778
      qwq_32b_temporal_crossing_rate: 0.444
      qwq_32b_temporal_lead_mean: -2.9
      qwq_32b_temporal_delta_over_static_pp: 8.3
      r1_8b_temporal_crossing_rate_reference: 0.767
      r1_8b_temporal_delta_reference_pp: 30.2
    result_rationale: >
      The temporal advantage collapses on Qwen2.5-based models. On r1-8b (Llama), temporal W=15
      produced +30pp gain because Llama's hidden states exhibit a distinctive "safety reasoning
      density decline" pattern — safety-relevant dimensions show monotonic decrease approaching
      the commitment point, which a temporal window captures. Qwen2.5's GQA architecture produces
      more compressed, less temporally smooth representations. The safety signal on 32B models
      is more "bursty" — safety-relevant features activate sporadically rather than declining
      monotonically — so temporal averaging over W=15 steps washes out discriminative signal
      rather than amplifying it. The temporal delta is only +8-12pp (vs +30pp on r1-8b), and
      absolute coverage reaches only 44-50% (vs 76.7%). This is the critical failure: the
      temporal advantage was architecture-specific to Llama, not a general property of reasoning
      model hidden states. Coverage stays below the 55% threshold that would make the temporal
      story viable cross-architecture.
    tables:
      - name: "Table 4: Temporal vs Static Coverage Across Architectures"
        columns: ["Model", "Static Coverage", "Temporal W=15 Coverage", "Delta (pp)", "Temporal Lead Mean"]
        rows:
          - ["r1-8b (Llama)", "46.5%", "76.7%", "+30.2", -1.09]
          - ["r1-32b (Qwen2.5)", "38.5%", "50.0%", "+11.5", -2.1]
          - ["QwQ-32B (Qwen2.5)", "36.1%", "44.4%", "+8.3", -2.9]
    figures_description:
      - "Bar chart comparing static vs temporal coverage across 3 models, with delta annotations. r1-8b shows dramatic +30pp gain; both 32B models show modest +8-12pp, with error bars overlapping static performance."
      - "Per-step probe score trajectories for 3 example traces per model: r1-8b shows smooth decline approaching CP; r1-32b and QwQ show noisy, non-monotonic patterns explaining temporal window failure."
    analysis: >
      This is the single most damaging result for the original paper narrative. The temporal
      window advantage — the core of Claim 2 — is revealed as a Llama-specific phenomenon.
      The +30pp gap collapses to +8-12pp on Qwen2.5, failing to cross the 15pp threshold that
      would support a cross-architecture generalization claim. The 50% temporal coverage on r1-32b
      means the probe still misses half of all commitment points. This forces a reframe: temporal
      context helps modestly everywhere, but the dramatic r1-8b result was driven by Llama's
      specific representation geometry, not a fundamental property of reasoning traces. For the
      negative-result paper, this becomes evidence that "no single probing strategy works across
      architectures" — a stronger claim than the original "temporal probing works."

  - name: "Cross-Model Transfer (Zero-Shot Generalization)"
    plan_id: "exp-003"
    description: >
      Train probes on r1-8b (Llama) features, test on r1-32b/QwQ (Qwen2.5) via learned projection head (4096→5120).
      Reverse direction: train on Qwen2.5, test on Llama (5120→4096).
    expected_results:
      llama_to_qwen_static_coverage: 0.167
      llama_to_qwen_temporal_coverage: 0.222
      llama_to_qwen_retention_pct: 28.9
      qwen_to_llama_static_coverage: 0.186
      qwen_to_llama_temporal_coverage: 0.279
      qwen_to_llama_retention_pct: 36.4
      within_qwen_transfer_static_coverage: 0.333
      within_qwen_transfer_temporal_coverage: 0.417
      within_qwen_transfer_retention_pct: 83.3
      projection_head_train_loss: 0.42
      projection_head_reconstruction_r2: 0.31
    result_rationale: >
      Cross-architecture transfer fails catastrophically (<40% retention) because the learned
      representations encode safety information in architecture-specific subspaces. The projection
      head (a learned linear map between 4096-d Llama and 5120-d Qwen spaces) achieves only
      R²=0.31 on held-out hidden states — the mapping is too lossy to preserve the already-subtle
      safety signal. Within-family transfer (r1-32b↔QwQ, both Qwen2.5) retains 83% because the
      base architecture shares representation geometry, but cross-family transfer drops to 29-36%.
      The asymmetry (Qwen→Llama slightly better than Llama→Qwen) likely reflects Llama's more
      structured safety subspace being a partially recoverable target, while Qwen's diffuse signal
      provides poor source features. This confirms that hidden-state safety probes are
      architecture-specific tools, not general-purpose detectors — a fundamental limitation for
      deployment where model versions change frequently.
    tables:
      - name: "Table 5: Cross-Model Transfer Results"
        columns: ["Train→Test", "Arch Transfer", "Static Cov", "Temporal Cov", "Retention%"]
        rows:
          - ["r1-8b→r1-32b", "Llama→Qwen", "16.7%", "22.2%", "28.9%"]
          - ["r1-8b→QwQ", "Llama→Qwen", "13.9%", "19.4%", "25.3%"]
          - ["r1-32b→r1-8b", "Qwen→Llama", "18.6%", "27.9%", "36.4%"]
          - ["r1-32b→QwQ", "Qwen→Qwen", "33.3%", "41.7%", "83.3%"]
          - ["QwQ→r1-32b", "Qwen→Qwen", "30.6%", "38.9%", "77.8%"]
    figures_description:
      - "Transfer retention heatmap (5×5 model pairs), showing high within-family retention (green) and low cross-family retention (red). Diagonal is 100% (within-model)."
    analysis: >
      Cross-architecture transfer is non-viable. The <40% retention across architecture families
      means probes must be retrained from scratch for each new model — eliminating the practical
      appeal of hidden-state monitoring. The strong within-Qwen transfer (83%) provides a small
      consolation: within a model family, probes transfer well, suggesting architecture-specific
      but not model-specific representations. For the negative-result paper, this becomes
      "Implication 3: Hidden-state safety detectors cannot be architecture-agnostic" —
      contrasting with text-based detectors that trivially transfer.

  - name: "Cross-Architecture Lead Time Analysis"
    plan_id: "exp-004"
    description: >
      Lead time distribution for static, temporal LR, and GRU probes on r1-32b and QwQ-32B.
      Compare to r1-8b baselines and oracle.
    expected_results:
      r1_32b_static_lead_mean: -5.2
      r1_32b_static_lead_median: -6
      r1_32b_temporal_lead_mean: -3.4
      r1_32b_temporal_lead_median: -4
      r1_32b_gru_lead_mean: -0.8
      r1_32b_gru_lead_median: -2
      r1_32b_gru_pos_lead_rate: 0.27
      r1_32b_gru_early_detect_count: "4/15"
      qwq_static_lead_mean: -6.1
      qwq_static_lead_median: -7
      qwq_temporal_lead_mean: -4.1
      qwq_temporal_lead_median: -5
      qwq_gru_lead_mean: -1.6
      qwq_gru_lead_median: -3
      qwq_gru_pos_lead_rate: 0.21
      qwq_gru_early_detect_count: "3/14"
      oracle_lead_mean_reference: 31
      oracle_early_detect_rate_reference: 1.0
    result_rationale: >
      Lead times worsen substantially on 32B models because (1) the noisier per-step probe scores
      produce later threshold crossings, and (2) the commitment transition in 32B models is more
      abrupt — safety reasoning doesn't decline gradually as in r1-8b but drops sharply over
      2-3 steps, giving probes almost no temporal lead. GRU achieves only 21-27% positive lead
      rate (vs 39% on r1-8b), and mean lead time goes negative (-0.8 to -1.6 steps vs +4.7
      on r1-8b). The oracle gap is even more extreme: oracle achieves +31 steps, but GRU
      achieves -0.8 to -1.6 — a 32-33 step gap compared to 26 steps on r1-8b. Pre-textual
      detection is essentially non-functional on 32B models. This suggests the r1-8b positive
      lead time was exploiting Llama-specific representation dynamics (gradual safety feature
      decay) that don't exist in Qwen2.5.
    tables:
      - name: "Table 6: Lead Time Across Models and Methods"
        columns: ["Model", "Method", "Lead Mean", "Lead Median", "Lead Std", "Pos Lead Rate", "Early Detect"]
        rows:
          - ["r1-8b", "Static LR", -2.0, -2, "—", "30%", "6/20"]
          - ["r1-8b", "Temporal W=15", -1.09, -1, "—", "35%", "—"]
          - ["r1-8b", "GRU-multi", 4.7, 0, 13, "39%", "13/33"]
          - ["r1-32b", "Static LR", -5.2, -6, "—", "15%", "—"]
          - ["r1-32b", "Temporal W=15", -3.4, -4, "—", "22%", "—"]
          - ["r1-32b", "GRU-multi", -0.8, -2, 9, "27%", "4/15"]
          - ["QwQ-32B", "Static LR", -6.1, -7, "—", "12%", "—"]
          - ["QwQ-32B", "Temporal W=15", -4.1, -5, "—", "18%", "—"]
          - ["QwQ-32B", "GRU-multi", -1.6, -3, 8, "21%", "3/14"]
          - ["Oracle", "Label K=5", 31, 29, "—", "100%", "33/43"]
    figures_description:
      - "Lead time distribution histograms (3 panels: r1-8b, r1-32b, QwQ) for GRU probe, each showing mostly-negative distributions with r1-8b having a visible right tail and 32B models concentrated left of zero."
      - "Detection delay CDF curves per model, showing 32B models' curves shifted right (later detection) relative to r1-8b and far from oracle."
    analysis: >
      Pre-textual detection is a failed promise on 32B models. The GRU's positive lead on r1-8b
      (+4.7 mean, already fragile with median 0) collapses to negative on Qwen2.5-based models.
      Combined with the coverage failure in exp-002, this means neither the temporal coverage
      story nor the early detection story survives cross-architecture validation. For the
      negative-result paper, this establishes "Finding 4: The r1-8b lead time advantage was
      architecture-specific" and motivates the question of what representation properties
      enabled it (Llama's more structured safety subspace with gradual feature decay).

  - name: "TrajGuard-Style Mahalanobis Baseline"
    plan_id: "exp-005"
    description: >
      Mahalanobis distance-based detector (TrajGuard analogue) using safe-trace covariance estimation.
      Evaluated on all 3 models.
    expected_results:
      r1_8b_md_coverage: 0.302
      r1_8b_md_auroc: 0.623
      r1_8b_md_lead_mean: -4.2
      r1_32b_md_coverage: 0.25
      r1_32b_md_auroc: 0.581
      r1_32b_md_lead_mean: -6.7
      qwq_md_coverage: 0.222
      qwq_md_auroc: 0.564
      qwq_md_lead_mean: -7.3
      r1_8b_md_fpr_at_30pct_coverage: 0.28
      r1_32b_md_fpr_at_25pct_coverage: 0.31
    result_rationale: >
      TrajGuard-style Mahalanobis detection fails as expected — and this is actually one finding
      that is consistent across tiers. The Fisher ratio collapse under PCA (17→1) means the
      safety signal lives in minor principal components that Mahalanobis distance (which weights
      by eigenvalue) downweights. Safe-trace covariance estimation captures the dominant variance
      directions (non-safety features), so anomaly scores are driven by non-safety variation.
      On 32B models, performance degrades further because (1) 5120-d covariance estimation is
      less stable with 209 traces and (2) the signal is even more dispersed. Coverage of 22-30%
      is worse than even static LR probes, confirming that geometric/distance-based detectors
      designed for token-level jailbreak detection are fundamentally mismatched to the
      commitment detection task. The relatively high FPR (28-31%) at these low coverage levels
      makes the detector worse than random on a precision-adjusted basis.
    tables:
      - name: "Table 7: TrajGuard Mahalanobis Results"
        columns: ["Model", "Coverage", "AUROC", "Lead Mean", "FPR@Coverage"]
        rows:
          - ["r1-8b", "30.2%", 0.623, -4.2, "28% @ 30%cov"]
          - ["r1-32b", "25.0%", 0.581, -6.7, "31% @ 25%cov"]
          - ["QwQ-32B", "22.2%", 0.564, -7.3, "33% @ 22%cov"]
    figures_description:
      - "Mahalanobis score distributions for safe vs unsafe traces, showing heavy overlap — the distributions are nearly indistinguishable, with only slight rightward shift for unsafe traces."
    analysis: >
      Confirms the "existing detectors fail" claim (Claim 1) robustly across architectures.
      Mahalanobis is the worst-performing method on all models, validating the paper's core
      insight about signal geometry (minor PC encoding). However, in the worst tier, this
      finding is less impactful because the proposed alternatives (temporal LR, GRU) also fail
      on 32B models. The Mahalanobis failure becomes just one instance of a broader pattern:
      no hidden-state method works reliably cross-architecture. For the reframed paper, this
      supports "Section 4.1: Why Geometric Methods Fail" using the Fisher ratio analysis.

  - name: "Bootstrap Confidence Intervals + Threshold-Independent Metrics"
    plan_id: "exp-006"
    description: >
      1000 bootstrap resamples on all key metrics. AUROC, PR curves, detection delay CDF,
      cross-validation variance, FPR on safe traces.
    expected_results:
      r1_8b_coverage_ci: [0.651, 0.884]
      r1_8b_coverage_ci_width: 0.233
      r1_8b_temporal_auroc: 0.841
      r1_8b_temporal_auprc: 0.712
      r1_32b_coverage_ci: [0.333, 0.667]
      r1_32b_coverage_ci_width: 0.334
      r1_32b_temporal_auroc: 0.743
      r1_32b_temporal_auprc: 0.581
      qwq_coverage_ci: [0.278, 0.611]
      qwq_coverage_ci_width: 0.333
      qwq_temporal_auroc: 0.721
      qwq_temporal_auprc: 0.553
      cross_val_fold_variance_coverage: 0.042
      gru_lead_ci_r1_8b: [-2.1, 11.5]
      gru_lead_ci_r1_32b: [-7.4, 5.8]
      r1_8b_fpr_at_70pct_coverage: 0.22
      r1_32b_fpr_at_50pct_coverage: 0.27
      qwq_fpr_at_44pct_coverage: 0.29
      bootstrap_ci_width_coverage_avg: 0.30
    result_rationale: >
      Wide bootstrap CIs reflect the small test set (43 traces) combined with high variance
      across traces. The r1-8b coverage CI ([0.651, 0.884]) spans 23pp — already wide — but
      32B models are worse at 33pp width because the lower base rate of successful detection
      produces more variable bootstrap samples. Critically, the cross-architecture coverage
      CIs overlap substantially: r1-32b [0.333, 0.667] overlaps with r1-8b's lower bound,
      meaning we cannot statistically distinguish whether temporal probing "works" on 32B
      from chance-level detection with 43 test traces. The GRU lead time CI on r1-8b
      ([-2.1, 11.5]) spans zero, so even the r1-8b positive lead claim is not statistically
      significant. FPR at operational coverage thresholds exceeds 20% on all models, meaning
      more than 1 in 5 safe traces would trigger false alarms — making deployment claims
      untenable. The CI widths average 0.30 — far exceeding the 0.10-0.18 range that would
      support tight claims, driven by the combination of small N and cross-architecture variance.
    tables:
      - name: "Table 8: Bootstrap 95% CIs for Key Metrics"
        columns: ["Model", "Metric", "Point Est.", "95% CI", "CI Width"]
        rows:
          - ["r1-8b", "Temporal Coverage", "76.7%", "[65.1%, 88.4%]", "23.3pp"]
          - ["r1-8b", "GRU Lead Mean", "+4.7", "[-2.1, +11.5]", "13.6"]
          - ["r1-8b", "GRU Early Detect%", "39%", "[21%, 58%]", "37pp"]
          - ["r1-32b", "Temporal Coverage", "50.0%", "[33.3%, 66.7%]", "33.4pp"]
          - ["r1-32b", "GRU Lead Mean", "-0.8", "[-7.4, +5.8]", "13.2"]
          - ["QwQ-32B", "Temporal Coverage", "44.4%", "[27.8%, 61.1%]", "33.3pp"]
          - ["QwQ-32B", "GRU Lead Mean", "-1.6", "[-8.2, +5.0]", "13.2"]
      - name: "Table 9: FPR at Operational Coverage Thresholds"
        columns: ["Model", "Coverage Threshold", "FPR", "Precision", "F1"]
        rows:
          - ["r1-8b", "70%", "22%", 0.68, 0.69]
          - ["r1-32b", "50%", "27%", 0.57, 0.53]
          - ["QwQ-32B", "44%", "29%", 0.53, 0.48]
    figures_description:
      - "PR curves for all models, showing r1-8b achieving acceptable precision at high recall but 32B models with steep precision drop-off. All curves annotated with operational threshold points."
      - "Bootstrap distribution histograms for temporal coverage, showing r1-8b centered at ~77% but 32B models' wide, left-shifted distributions centered at ~47%."
    analysis: >
      Bootstrap analysis delivers the statistical coup de grâce. Even the strongest result
      (r1-8b temporal coverage) has a CI too wide for confident claims. The GRU lead time CI
      spanning zero means the headline "+4.7 steps" finding is not statistically significant
      at p<0.05. Cross-architecture results are even weaker — the 32B coverage CIs include
      the static baseline performance, meaning temporal methods may not help at all on Qwen2.5.
      FPR >20% at every operational threshold invalidates the "coverage" metric itself: achieving
      50% coverage while false-alarming on 27% of safe traces is not deployable. For the reframed
      paper, this becomes "Section 5: Statistical Fragility of Current Detection Methods" — the
      small sample size is itself a finding about the field's evaluation standards.

  - name: "Window Size Ablation (Cross-Architecture)"
    plan_id: "exp-007"
    description: >
      Temporal LR with W=1,3,5,10,15,20,25 on all 3 models. Identify optimal W per model
      and show diminishing returns.
    expected_results:
      r1_8b_optimal_w: 15
      r1_8b_w1_coverage: 0.465
      r1_8b_w15_coverage: 0.767
      r1_8b_w25_coverage: 0.744
      r1_32b_optimal_w: 10
      r1_32b_w1_coverage: 0.385
      r1_32b_w5_coverage: 0.417
      r1_32b_w10_coverage: 0.50
      r1_32b_w15_coverage: 0.50
      r1_32b_w20_coverage: 0.472
      r1_32b_w25_coverage: 0.444
      qwq_optimal_w: 5
      qwq_w1_coverage: 0.361
      qwq_w3_coverage: 0.389
      qwq_w5_coverage: 0.444
      qwq_w10_coverage: 0.417
      qwq_w15_coverage: 0.444
      qwq_w20_coverage: 0.389
      qwq_w25_coverage: 0.361
    result_rationale: >
      Window ablation reveals architecture-dependent optimal W, undermining the universal W=15
      recommendation. On r1-8b, the monotonic improvement up to W=15 reflects Llama's temporally
      smooth safety feature decay — longer windows capture the gradual trend. On Qwen2.5 models,
      optimal W is much shorter (5-10) because the safety signal is "bursty": only the immediately
      surrounding steps carry discriminative information, and wider windows average in noise.
      On QwQ-32B, coverage actually decreases beyond W=5, suggesting temporal over-smoothing.
      This means even the modest +8-12pp temporal gains reported in exp-002 (using W=15) were
      sub-optimal — Qwen2.5 benefits from temporal context but only a narrow window. However,
      even at optimal W, 32B coverage tops out at 44-50%, far below r1-8b's 76.7%. The
      architecture-dependent optimal W is itself a negative result: no single hyperparameter
      setting works across models, complicating any deployment story.
    tables:
      - name: "Table A1: Window Size Ablation"
        columns: ["W", "r1-8b Cov", "r1-32b Cov", "QwQ Cov"]
        rows:
          - [1, "46.5%", "38.5%", "36.1%"]
          - [3, "53.5%", "41.7%", "38.9%"]
          - [5, "65.1%", "41.7%", "44.4%"]
          - [10, "65.1%", "50.0%", "41.7%"]
          - [15, "76.7%", "50.0%", "44.4%"]
          - [20, "74.4%", "47.2%", "38.9%"]
          - [25, "74.4%", "44.4%", "36.1%"]
    figures_description:
      - "Line plot: coverage vs window size W for 3 models. r1-8b shows clear rise-and-plateau; r1-32b shows modest rise then plateau; QwQ shows narrow peak at W=5 then decline. Shaded regions show bootstrap 80% CI."
    analysis: >
      Architecture-dependent W complicates the story and reveals the temporal advantage
      on r1-8b as architecture-specific. For the reframed paper, this becomes evidence for
      "different architectures encode safety information with different temporal scales" —
      an analytical insight about representation geometry rather than a method recommendation.

  - name: "Layer Selection Ablation (32B Models)"
    plan_id: "exp-008"
    description: >
      Full layer sweep for temporal probe on r1-32b and QwQ-32B (all 64 layers).
      Test whether middle-layer advantage from r1-8b generalizes.
    expected_results:
      r1_32b_best_temporal_layer: 30
      r1_32b_best_temporal_coverage: 0.528
      r1_32b_early_layer_coverage_l8: 0.278
      r1_32b_mid_layer_coverage_l32: 0.50
      r1_32b_late_layer_coverage_l56: 0.361
      r1_32b_plateau_range: "L24-L38"
      qwq_best_temporal_layer: 26
      qwq_best_temporal_coverage: 0.472
      qwq_early_layer_coverage_l8: 0.25
      qwq_mid_layer_coverage_l32: 0.444
      qwq_late_layer_coverage_l56: 0.333
      qwq_plateau_range: "L20-L34"
    result_rationale: >
      Middle-layer preference holds qualitatively (~40-50% depth range is best) but the
      absolute performance ceiling is much lower. On r1-32b, the best layer (L30) achieves
      52.8% temporal coverage — better than the L30 static result (38.5%) but still far below
      r1-8b's 76.7% at its best layer. The broad plateau (L24-38 on r1-32b, L20-34 on QwQ)
      suggests the safety signal isn't strongly layer-localized on 32B models — consistent
      with more distributed representations. Crucially, no single layer achieves >55% coverage
      on either 32B model, confirming that the poor cross-architecture results aren't due to
      sub-optimal layer selection. Even with exhaustive search, 32B temporal probing doesn't
      match r1-8b performance.
    tables:
      - name: "Table A2: Layer Sweep (Temporal W=15, Selected Layers)"
        columns: ["Layer", "Depth%", "r1-32b Cov", "QwQ Cov"]
        rows:
          - ["L8", "12.5%", "27.8%", "25.0%"]
          - ["L16", "25.0%", "38.9%", "33.3%"]
          - ["L24", "37.5%", "47.2%", "41.7%"]
          - ["L30", "46.9%", "52.8%", "44.4%"]
          - ["L32", "50.0%", "50.0%", "47.2%"]
          - ["L40", "62.5%", "44.4%", "38.9%"]
          - ["L48", "75.0%", "38.9%", "33.3%"]
          - ["L56", "87.5%", "36.1%", "33.3%"]
    figures_description:
      - "Layer sweep heatmap: coverage vs layer for temporal LR, all 64 layers, for r1-32b and QwQ-32B. Broad warm band in L20-38 range, with no sharp peak."
    analysis: >
      Layer selection cannot rescue 32B performance. The exhaustive sweep confirms the
      cross-architecture coverage failure is fundamental, not a hyperparameter issue.
      For the reframed paper, the broad plateau on 32B (vs sharper peak on r1-8b) is
      additional evidence for diffuse safety signal encoding in Qwen2.5 architecture.

  - name: "16-Label Taxonomy Supervision"
    plan_id: "exp-009"
    description: >
      Use fine-grained 4-type labels instead of binary commitment for temporal probe training.
      Test whether richer supervision improves coverage or timing.
    expected_results:
      r1_8b_16label_coverage: 0.744
      r1_8b_16label_lead_mean: -0.6
      r1_8b_16label_vs_binary_delta_pp: -2.3
      r1_32b_16label_coverage: 0.472
      r1_32b_16label_lead_mean: -2.8
      qwq_16label_coverage: 0.417
      qwq_16label_lead_mean: -3.5
    result_rationale: >
      Fine-grained labels don't help and slightly hurt on r1-8b. The 4-type taxonomy
      (explicit safety reasoning, implicit safety reasoning, safety hedging, non-safety)
      fragments the already-small training set (125 traces × ~30 steps per trace) into 4
      classes, reducing per-class sample size below the threshold for reliable temporal LR
      training. The subtle distinctions between "explicit" and "implicit" safety reasoning
      don't correspond to reliably different hidden-state patterns — they're annotation-level
      distinctions that the representation doesn't preserve. On 32B models, the fragmentation
      effect is worse because the weaker base signal gets divided among more classes. This
      addresses the reviewer concern by showing that richer supervision provides no benefit
      with current sample sizes — binary is optimal given data constraints.
    tables:
      - name: "Table A3: 16-Label vs Binary Supervision"
        columns: ["Model", "Binary Cov", "16-Label Cov", "Delta", "Binary Lead", "16-Label Lead"]
        rows:
          - ["r1-8b", "76.7%", "74.4%", "-2.3pp", -1.09, -0.6]
          - ["r1-32b", "50.0%", "47.2%", "-2.8pp", -2.1, -2.8]
          - ["QwQ-32B", "44.4%", "41.7%", "-2.7pp", -2.9, -3.5]
    figures_description:
      - "Confusion matrices for 4-type classifier on r1-8b, showing high confusion between 'explicit safety' and 'implicit safety' classes."
    analysis: >
      Richer supervision doesn't compensate for representation limitations or small sample size.
      For the reframed paper, this is a minor negative result in the appendix: "even with
      domain-expert annotations, probe performance is bounded by representation quality."

  - name: "Oracle Decomposition Analysis"
    plan_id: "exp-010"
    description: >
      Analyze what label patterns the oracle exploits that hidden-state probes cannot capture.
      Decompose oracle advantage by trace characteristics.
    expected_results:
      oracle_advantage_from_label_persistence: 0.62
      oracle_advantage_from_pattern_structure: 0.38
      mean_safety_gap_before_cp: 3.2
      pct_traces_with_pre_cp_gap: 0.72
      hidden_state_gap_detection_rate: 0.18
      oracle_gap_steps: 31
      gru_gap_steps_r1_8b: 4.7
      gru_gap_steps_r1_32b: -0.8
      fundamental_gap_steps: 26.3
    result_rationale: >
      The oracle decomposition reveals that 62% of the oracle's advantage comes from label
      persistence — the oracle sees the binary label at each step and just needs K=5 consecutive
      non-safety steps to fire, while hidden-state probes must infer the absence of safety
      reasoning from continuous representations. The remaining 38% comes from structural patterns
      (safety reasoning tends to cluster, creating recognizable "gap" patterns before permanent
      cessation). 72% of traces show a "pre-CP gap" (≥3 consecutive non-safety steps before
      the commitment point), but hidden-state probes detect only 18% of these gaps — the probe
      confidence doesn't drop reliably during gaps because the hidden state retains residual
      safety features from recent safety steps. This explains the fundamental gap: hidden states
      encode "recent safety state" but not "whether safety reasoning will resume." The oracle's
      +31-step advantage is largely unachievable without access to discrete safety labels at
      each step — which is exactly what text-based monitoring provides (exp-013).
    tables:
      - name: "Table 10: Oracle Advantage Decomposition"
        columns: ["Component", "Contribution", "Probe Detection Rate"]
        rows:
          - ["Label persistence (K consecutive non-safety)", "62%", "18%"]
          - ["Pattern structure (gap detection)", "38%", "31%"]
          - ["Total oracle advantage", "+31 steps", "—"]
          - ["Best probe (GRU r1-8b)", "+4.7 steps", "39% early detect"]
          - ["Fundamental gap", "+26.3 steps", "—"]
    figures_description:
      - "Annotated trace example showing oracle detection point (early, during pre-CP gap), GRU detection point (late, after CP), and the gap between them. Safety label sequence shown above, probe scores below."
    analysis: >
      The oracle decomposition provides the analytical centerpiece of the reframed paper.
      The fundamental insight is that hidden states encode "current safety state" not "future
      safety trajectory" — they're instantaneous measurements, not predictive features.
      The 26-step fundamental gap between oracle and best probe represents the prediction
      horizon that current sequential models cannot bridge. This motivates future work on
      predictive representations (not just descriptive probes) and connects to the text
      baseline result (exp-013): text monitoring can approximate the oracle's discrete label
      access, partially closing the gap that hidden-state probes cannot.

  - name: "OpenThinker-7B (Qwen2.5-7B Scale Control)"
    plan_id: "exp-011"
    description: >
      OpenThinker-7B (Qwen2.5-7B base) as 4th model for 2×2 architecture×scale matrix.
      Controls for scale confound in Llama vs Qwen comparison.
    expected_results:
      openthinker_best_layer: 12
      openthinker_static_coverage: 0.372
      openthinker_temporal_coverage: 0.465
      openthinker_temporal_delta_pp: 9.3
      openthinker_gru_lead_mean: -1.2
      openthinker_fisher_orig: 12.4
      openthinker_fisher_pca3: 0.72
    result_rationale: >
      OpenThinker-7B (Qwen2.5-7B base) shows performance closer to the 32B Qwen2.5 models
      than to r1-8b (Llama-8B), confirming the cross-architecture degradation is driven by
      architecture (Qwen vs Llama), not scale. Temporal delta (+9.3pp) is similar to r1-32b
      (+11.5pp) and QwQ (+8.3pp), all much smaller than r1-8b's +30pp. This completes the
      2×2 matrix: Llama shows large temporal advantage regardless of scale (if we had a Llama-32B
      reasoning model), while Qwen shows modest advantage regardless of scale. Fisher ratio
      (12.4 → 0.72 under PCA) follows the Qwen2.5 pattern, not the Llama pattern. This
      conclusively establishes that r1-8b's strong results are Llama-specific, not
      small-model-specific or r1-specific.
    tables:
      - name: "Table 11: 2×2 Architecture × Scale Matrix"
        columns: ["Architecture", "Scale", "Model", "Static Cov", "Temporal Cov", "Delta (pp)"]
        rows:
          - ["Llama-3.1", "8B", "r1-8b", "46.5%", "76.7%", "+30.2"]
          - ["Qwen2.5", "7B", "OpenThinker-7B", "37.2%", "46.5%", "+9.3"]
          - ["Qwen2.5", "32B", "r1-32b", "38.5%", "50.0%", "+11.5"]
          - ["Qwen2.5", "32B", "QwQ-32B", "36.1%", "44.4%", "+8.3"]
    figures_description:
      - "2×2 matrix heatmap showing temporal coverage: Llama cell bright (76.7%), all three Qwen cells similarly dim (44-50%). Clear architecture effect, no scale effect."
    analysis: >
      The scale control experiment eliminates the alternative hypothesis that 32B model
      degradation was due to scale rather than architecture. For the reframed paper, this
      strengthens the claim that Llama's representation geometry is uniquely suited to
      temporal safety probing — a finding that demands explanation rather than exploitation.

  - name: "GRU/Attention Probe on 32B Models"
    plan_id: "exp-012"
    description: >
      GRU probe evaluation on r1-32b and QwQ-32B. Test whether increased model capacity
      helps on 32B representations.
    expected_results:
      r1_32b_gru_single_coverage: 0.472
      r1_32b_gru_multi_coverage: 0.50
      r1_32b_gru_multi_lead_mean: -0.8
      r1_32b_gru_vs_temporal_lr_delta_pp: 0.0
      qwq_gru_single_coverage: 0.417
      qwq_gru_multi_coverage: 0.472
      qwq_gru_multi_lead_mean: -1.6
      qwq_gru_vs_temporal_lr_delta_pp: 2.8
      r1_32b_gru_training_unstable: true
      r1_32b_gru_fold_variance: 0.089
    result_rationale: >
      GRU provides no meaningful improvement over temporal LR on 32B models, despite having
      ~1.6M parameters vs LR's ~77K. On r1-32b, GRU multi-layer matches temporal LR exactly
      (50% coverage); on QwQ, GRU ekes out +2.8pp that is within noise given the fold variance
      (8.9%). Training is unstable with high cross-validation variance, suggesting the 5120-d
      input overwhelms the GRU's capacity relative to the small training set (125 traces).
      The r1-8b success was partially a favorable data regime: 4096-d features with stronger
      signal allowed the GRU to extract temporal patterns that don't exist (or are too noisy)
      in 5120-d Qwen2.5 representations. This strengthens the "simplicity matches ceiling"
      story — but the ceiling itself is low on 32B models. The GRU's failure to improve on
      32B confirms that the temporal signal degradation is representational, not a modeling
      capacity issue.
    tables:
      - name: "Table A4: GRU vs Temporal LR on 32B Models"
        columns: ["Model", "Method", "Coverage", "Lead Mean", "Fold Var"]
        rows:
          - ["r1-32b", "Temporal LR W=15", "50.0%", -2.1, 0.031]
          - ["r1-32b", "GRU-single L30", "47.2%", -1.4, 0.067]
          - ["r1-32b", "GRU-multi 7L", "50.0%", -0.8, 0.089]
          - ["QwQ-32B", "Temporal LR W=15", "44.4%", -2.9, 0.028]
          - ["QwQ-32B", "GRU-single L26", "41.7%", -2.1, 0.072]
          - ["QwQ-32B", "GRU-multi 7L", "47.2%", -1.6, 0.094]
    figures_description:
      - "Learning curves for GRU on r1-32b showing early stopping at epoch 8-10 with high validation loss variance across folds, contrasted with stable r1-8b training."
    analysis: >
      GRU adds nothing on 32B models. The combination of weaker signal, higher dimensionality,
      and same training set size creates an unfavorable regime where added capacity just
      overfits to noise. For the reframed paper, this eliminates "use a more powerful probe"
      as a solution path, strengthening the "fundamental limitation" narrative.

  - name: "Text-Based Baseline (Sentence-BERT on CoT)"
    plan_id: "exp-013"
    description: >
      Sentence-BERT (all-MiniLM-L6-v2) embeddings + temporal window LR (W=15) on CoT text.
      The most critical experiment for paper viability.
    expected_results:
      r1_8b_text_coverage: 0.744
      r1_8b_text_lead_mean: -0.3
      r1_8b_text_auroc: 0.871
      r1_8b_hidden_vs_text_gap_pp: 2.3
      r1_32b_text_coverage: 0.528
      r1_32b_text_lead_mean: -1.4
      r1_32b_text_auroc: 0.792
      r1_32b_hidden_vs_text_gap_pp: -2.8
      qwq_text_coverage: 0.50
      qwq_text_lead_mean: -1.8
      qwq_text_auroc: 0.768
      qwq_hidden_vs_text_gap_pp: -5.6
      openthinker_text_coverage: 0.50
      openthinker_hidden_vs_text_gap_pp: -3.5
      text_cross_model_transfer_retention: 0.82
    result_rationale: >
      Text-based monitoring matches or exceeds hidden-state probes on 32B models, eliminating
      the core motivation for hidden-state monitoring. On r1-8b, text trails hidden states by
      only 2.3pp (74.4% vs 76.7%) — within bootstrap CI noise. On 32B models, text actually
      beats hidden states: r1-32b text achieves 52.8% vs hidden-state 50.0% (+2.8pp for text),
      and QwQ text achieves 50.0% vs 44.4% (+5.6pp for text). The reason is that CoT text
      directly expresses safety reasoning ("I should be careful", "let me reconsider") in a
      form that sentence embeddings capture cleanly, while hidden states encode this same
      information amidst thousands of other features. On Qwen2.5 models where hidden-state
      signal is more diffuse, text's direct access to safety content gives it an advantage.
      Furthermore, text probes transfer across architectures with 82% retention (vs <40% for
      hidden states) because sentence-BERT embeddings share a common semantic space regardless
      of the generating model. This is the killing blow: hidden-state monitoring adds no unique
      value over a cheap, architecture-agnostic text baseline. The safety signal IS the
      textual content of CoT reasoning — it's not "hidden" at all.
    tables:
      - name: "Table 12: Hidden-State vs Text-Based Detection"
        columns: ["Model", "Hidden Cov", "Text Cov", "Gap (pp)", "Hidden AUROC", "Text AUROC"]
        rows:
          - ["r1-8b", "76.7%", "74.4%", "+2.3 (hidden)", 0.848, 0.871]
          - ["r1-32b", "50.0%", "52.8%", "-2.8 (text wins)", 0.743, 0.792]
          - ["QwQ-32B", "44.4%", "50.0%", "-5.6 (text wins)", 0.721, 0.768]
          - ["OpenThinker-7B", "46.5%", "50.0%", "-3.5 (text wins)", "—", "—"]
      - name: "Table 13: Cross-Architecture Transfer — Hidden vs Text"
        columns: ["Method", "Cross-Arch Retention", "Notes"]
        rows:
          - ["Hidden-state probe", "<40%", "Requires retraining + projection head"]
          - ["Text-based probe", "82%", "Sentence-BERT space is model-agnostic"]
    figures_description:
      - "Side-by-side PR curves: hidden-state vs text probes for each model. On r1-8b curves nearly overlap; on 32B models text curve dominates hidden-state curve across all recall levels."
      - "Coverage bar chart with paired bars (hidden vs text) for all 4 models. Text matches or exceeds hidden on every model, with largest gap on QwQ."
    analysis: >
      This is the central negative finding. Hidden states don't add unique value because the
      safety signal in reasoning models is explicitly textualized in CoT — unlike standard
      LLMs where hidden states contain pre-articulation intent. Reasoning models "think out loud"
      about safety, so text monitoring directly accesses the relevant signal. The reframed paper
      embraces this: "The safety commitment signal is not hidden — it's expressed in CoT text.
      The real challenge is not detection (text suffices) but TIMING (predicting commitment before
      it's textually expressed)." This redirects the contribution from "method that works" to
      "analysis of why the hidden-state approach is fundamentally unnecessary for reasoning models,
      in contrast to standard LLMs where it adds genuine value."

  - name: "BOCPD Change-Point Detection on Probe Scores"
    plan_id: "exp-014"
    description: >
      Bayesian Online Change-Point Detection (Adams & MacKay 2007) and CUSUM on temporal
      probe score sequences. Tests whether distributional shift detection achieves positive
      lead time where GRU fails.
    expected_results:
      r1_8b_bocpd_coverage: 0.558
      r1_8b_bocpd_lead_mean: 2.1
      r1_8b_bocpd_lead_median: 0
      r1_8b_bocpd_early_detect_rate: 0.33
      r1_8b_bocpd_fpr: 0.31
      r1_8b_cusum_coverage: 0.512
      r1_8b_cusum_lead_mean: 1.4
      r1_8b_cusum_early_detect_rate: 0.27
      r1_32b_bocpd_coverage: 0.361
      r1_32b_bocpd_lead_mean: -0.6
      r1_32b_bocpd_early_detect_rate: 0.21
      r1_32b_bocpd_fpr: 0.35
      qwq_bocpd_coverage: 0.306
      qwq_bocpd_lead_mean: -1.3
      qwq_bocpd_early_detect_rate: 0.18
      qwq_bocpd_fpr: 0.38
      bocpd_sensitivity_to_hazard_rate: "high — coverage varies ±15pp across h∈[1/50, 1/200]"
    result_rationale: >
      BOCPD fails to meaningfully improve over GRU for lead time and introduces severe FPR
      problems. The method detects distributional shifts in probe score sequences, but the
      probe scores on 32B models are too noisy — frequent transient dips produce false change
      points (FPR 31-38%). On r1-8b, BOCPD achieves modest positive mean lead (+2.1 steps)
      but at the cost of 31% FPR and lower coverage than temporal LR (55.8% vs 76.7%).
      The coverage-FPR tradeoff is worse than temporal LR at every operating point. CUSUM
      performs slightly worse than BOCPD across the board. The core issue: BOCPD assumes the
      probe score sequence has a clear distributional shift at the commitment point, but in
      reality the shift is gradual and noisy — not the "abrupt changepoint" that BOCPD is
      designed for (Adams & MacKay's model assumes i.i.d. segments with instantaneous
      transition). The method is highly sensitive to the hazard rate hyperparameter, with
      coverage varying ±15pp — no single setting works across models. For the worst tier,
      BOCPD's failure strengthens the "fundamental limitation" narrative: even principled
      statistical methods for change-point detection cannot overcome the poor signal quality
      in hidden-state probe scores.
    tables:
      - name: "Table 14: BOCPD and CUSUM Results"
        columns: ["Model", "Method", "Coverage", "Lead Mean", "Early Detect%", "FPR"]
        rows:
          - ["r1-8b", "BOCPD", "55.8%", "+2.1", "33%", "31%"]
          - ["r1-8b", "CUSUM", "51.2%", "+1.4", "27%", "27%"]
          - ["r1-8b", "Temporal LR (ref)", "76.7%", "-1.09", "35%", "22%"]
          - ["r1-8b", "GRU-multi (ref)", "76.7%", "+4.7", "39%", "—"]
          - ["r1-32b", "BOCPD", "36.1%", "-0.6", "21%", "35%"]
          - ["r1-32b", "CUSUM", "30.6%", "-1.1", "17%", "30%"]
          - ["QwQ-32B", "BOCPD", "30.6%", "-1.3", "18%", "38%"]
          - ["QwQ-32B", "CUSUM", "27.8%", "-1.9", "14%", "33%"]
    figures_description:
      - "BOCPD run-length posterior visualization on 3 example traces (one per model), showing diffuse posteriors on 32B models with multiple spurious change-point candidates, vs. slightly clearer posterior on r1-8b."
      - "Precision-recall curves for BOCPD vs temporal LR vs GRU: BOCPD dominated at all thresholds, with especially poor precision at low recall."
    analysis: >
      BOCPD was the last hope for a novel methods contribution with positive lead time. Its
      failure eliminates the "method novelty" angle entirely. The high FPR (31-38%) is especially
      damaging because it means BOCPD cannot be deployed even on r1-8b where coverage exists —
      false-alarming on 1/3 of safe traces is operationally unacceptable. For the reframed paper,
      BOCPD's failure becomes "Section 4.3: Why Change-Point Detection Fails" — the probe score
      sequence doesn't satisfy BOCPD's stationarity assumptions, and the commitment transition
      is gradual, not abrupt. This analytical insight about the mismatch between method
      assumptions and data properties is itself a contribution.

  - name: "False Positive Analysis on Safe Traces"
    plan_id: "exp-015"
    description: >
      Run all probes on safe traces (final_judgment=0.5). Report FPR, precision-recall
      curves at various thresholds for all methods and models.
    expected_results:
      r1_8b_static_fpr: 0.14
      r1_8b_temporal_fpr_at_77pct_coverage: 0.22
      r1_8b_gru_fpr: 0.19
      r1_8b_bocpd_fpr: 0.31
      r1_32b_static_fpr: 0.18
      r1_32b_temporal_fpr_at_50pct_coverage: 0.27
      r1_32b_gru_fpr: 0.24
      r1_32b_bocpd_fpr: 0.35
      qwq_static_fpr: 0.20
      qwq_temporal_fpr_at_44pct_coverage: 0.29
      qwq_gru_fpr: 0.26
      qwq_bocpd_fpr: 0.38
      text_baseline_fpr_r1_8b: 0.15
      text_baseline_fpr_r1_32b: 0.18
      text_baseline_fpr_qwq: 0.19
      n_safe_traces_r1_8b: 38
      n_safe_traces_r1_32b: 38
      n_safe_traces_qwq: 38
    result_rationale: >
      FPR exceeds 20% at operational coverage thresholds on all models except r1-8b static
      (which has low coverage anyway). The fundamental issue: safe traces contain substantial
      safety reasoning (the model considers risks but correctly refuses), and probes trained
      on binary commitment labels fire on "safety reasoning present → safety reasoning absent"
      transitions that occur naturally in safe traces. For example, a safe trace might have a
      long stretch of normal reasoning after the model has already decided to refuse, which
      looks like "safety cessation" to the probe. On 32B models, FPR is uniformly higher
      because the probe thresholds must be set more aggressively (lower) to achieve even
      moderate coverage, catching more safe-trace false positives. The text baseline achieves
      notably lower FPR (15-19%) because text-level safety reasoning is more explicitly marked
      ("I will refuse") and text monitors can distinguish "decided to refuse, now explaining why"
      from "abandoned safety reasoning." This FPR analysis makes deployment claims impossible:
      at a 22% FPR, a system handling 100K safe requests per day would generate 22K false alarms.
      Even with human review, this is operationally untenable.
    tables:
      - name: "Table 15: False Positive Rates Across Methods and Models"
        columns: ["Model", "Static LR", "Temporal LR", "GRU", "BOCPD", "Text Baseline"]
        rows:
          - ["r1-8b", "14%", "22%", "19%", "31%", "15%"]
          - ["r1-32b", "18%", "27%", "24%", "35%", "18%"]
          - ["QwQ-32B", "20%", "29%", "26%", "38%", "19%"]
      - name: "Table 16: Precision at Coverage Thresholds"
        columns: ["Model", "Method", "Coverage", "Precision", "F1"]
        rows:
          - ["r1-8b", "Temporal LR", "76.7%", 0.68, 0.72]
          - ["r1-8b", "GRU", "76.7%", 0.72, 0.74]
          - ["r1-8b", "Text", "74.4%", 0.78, 0.76]
          - ["r1-32b", "Temporal LR", "50.0%", 0.57, 0.53]
          - ["r1-32b", "Text", "52.8%", 0.67, 0.59]
          - ["QwQ-32B", "Temporal LR", "44.4%", 0.53, 0.48]
          - ["QwQ-32B", "Text", "50.0%", 0.65, 0.57]
    figures_description:
      - "PR curves for all methods on r1-8b, r1-32b, QwQ-32B (3 panels). Text baseline consistently dominates hidden-state methods in precision at comparable recall. All methods show steep precision drop beyond 50% recall on 32B models."
      - "FPR heatmap across methods × models, with red cells (>20%) dominating the 32B rows and BOCPD column."
    analysis: >
      FPR analysis delivers the final blow to deployment viability. Hidden-state probes at
      operational thresholds produce FPR >20% on 32B models — the very models that would be
      deployed in production. The text baseline's consistently lower FPR adds insult: not only
      does text match hidden-state coverage, it does so with fewer false alarms. For the reframed
      paper, FPR becomes "Section 5.2: The Precision-Coverage Tradeoff" — showing that the
      "coverage" metric used throughout the paper (and the field) is misleading without FPR
      context. A 50% coverage with 27% FPR has a positive predictive value of only 65% — barely
      above chance for a binary task. This methodological critique (coverage alone is insufficient)
      is itself a contribution to the evaluation standards for hidden-state safety detectors.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f1e31ed-0d6c-48d0-bdbe-71bc2ee410be",
  "isSidechain": false,
  "requestId": "req_011Cb6uXBhaZeoAutAW3sYye",
  "type": "assistant",
  "uuid": "fe32998d-4aee-4ed8-8d89-65d72a2fde36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AyE4SsjEkZPmLWQ2GhXMh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11909,
      "cache_read_input_tokens": 11447,
      "output_tokens": 18027,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18027,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11909
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Cross-architecture fails to generalize OR text baseline matches hidden states — core motivation undermined, need fundamental reframe 核心假设：['Temporal LR co…",
  "leafUuid": "fe32998d-4aee-4ed8-8d89-65d72a2fde36",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Safety commitment detection in reasoning models: temporal context and fundamental limits",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Cross-architecture fails to generalize OR text baseline matches hidden states — core motivation undermined, need fundamental reframe 核心假设：['Temporal LR co…",
  "leafUuid": "fe32998d-4aee-4ed8-8d89-65d72a2fde36",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Safety commitment detection in reasoning models: temporal context and fundamental limits",
  "sessionId": "6a1d540a-fbc3-438b-b26f-022f1bea5636"
}
```

---
