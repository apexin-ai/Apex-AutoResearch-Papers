# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Clean data上persuasion grounding有信号但优势收窄，部分claim需降级——early detection优势推迟到K=

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6.jsonl`
- **Structured JSON:** [`f62756364b6275ce08d8.json`](../../sessions/f6/f62756364b6275ce08d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T17:03:16.363Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T17:03:16.363Z",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Clean data上persuasion grounding有信号但优势收窄，部分claim需降级——early detection优势推迟到K=3，adversarial robustness存在但delta-delta在边界附近\n核心假设：['TF-IDF hard gate通过但偏高（0.60-0.74），normalization可能未完全消除register差异', 'Persuasion信号存在但与semantic信号部分重叠，grounding提供的增量有限', 'DeBERTa persuasion分类器准确率在clean data上有所下降（0.68-0.75），噪声传播到下游', 'Escalation trajectory在group level可见但individual conversation level噪声大', 'Cross-attack泛化部分成立：对FITD有效但对Deceptive Delight效果弱（因其persuasion结构更隐蔽）']\n关键指标范围：{'clean_tfidf': [0.6, 0.74], 'treatment_k2_f1_clean': [0.76, 0.87], 'baseline_k2_f1_clean': [0.68, 0.8], 'treatment_k3_f1_clean': [0.82, 0.9], 'baseline_k3_f1_clean': [0.73, 0.83], 'treatment_full_f1_clean': [0.88, 0.94], 'baseline_full_f1_clean': [0.83, 0.9], 'delta_k2_pp': [3, 9], 'delta_k3_pp': [5, 12], 'adversarial_delta_delta_pp': [3, 8], 'scrambled_label_drop_pp': [4, 10], 'cross_attack_treatment_f1': [0.62, 0.78], 'cross_attack_baseline_f1': [0.55, 0.72], 'deberta_persuasion_acc_clean': [0.68, 0.75]}\n叙事方向：需要两处调整：(1) Claim 2从\"K=2显著优势\"降级为\"K=3显著优势，K=2趋势一致但需更多数据确认\"， early detection故事仍然成立但时间窗口后移一步；(2) Claim 1从\"evasion hierarchy\"软化为 \"pragmatic features提供complementary robustness\"，delta-delta显著但不是压倒性的。 Claim 3（escalation trajectory）作为analytical contribution保留但加caveat说individual-level噪声大。 论文需补充：(a) 用bootstrap CI强调小样本下statistical significance，(b) 明确讨论 persuasion分类器accuracy对下游的bottleneck效应作为limitation，(c) cross-attack结果 分attack type报告而非aggregate。仍冲EMNLP main但需要更强的limitation section和 \"proof-of-concept for the principle\"的narrative定位。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: persuasion_turn_jailbreak_detect\nfocus: Key risks to probe: (1) TF-IDF=1.0 data quality — will adversarial perturbation approach credibly resolve this? (2) Small dataset (480 samples) — is the narrative framing sufficient? (3) Single-track architecture vs full dual-track from IDEA_BRIEF — does the simplified MVE still tell a compelling story? (4) Pragmatic Evasion Asymmetry as theoretical contribution — is it strong enough for EMNLP main? (5) Only Crescendo + generated attack types — generalization concerns.\n\n## paper_framing.md\n\n# Paper Framing — persuasion_turn_jailbreak_detect\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: 2026-05-25 (ARR May cycle)\n- Track: LLM Security / Discourse and Pragmatics\n- Commitment deadline: 2026-08-02\n\n## Title (Working)\nDisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection\n\n## Core Insight\nMulti-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.\n\n## Core Claims (3)\n\n### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)\nAn evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept \"benign\" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).\n- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing\n\n### Claim 2: Early Detection via Persuasion Grounding\nPersuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.\n- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)\n\n### Claim 3: Monotonic Escalation Trajectory\nAdversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.\n- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign\n\n## Story Spine\n\n**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a \"benign\" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.\n\n**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.\n\n**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.\n\n**Headline result**: \"DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp.\"\n\n## Architecture (Simplified for MVE)\n\nSingle-track with persuasion grounding (full dual-track in future work):\n1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification\n2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification\n3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings\n\n## Venue Fit Risks\n- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)\n- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)\n- Safety reviewers expect multiple attack types: need >= 2 attack families\n\n## Anticipated Reviewer Concerns\n\n### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)\nTF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.\n- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)\n\n### RC2: Small Dataset\n480 samples is small for a detection paper.\n- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers\n\n### RC3: Single Attack Type (Crescendo Only)\nNeed generalization evidence.\n- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline\n\n### RC4: Strategy Label Confound (M004)\nBenign turns hardcoded to strategy=7 creates shortcut for treatment model.\n- Mitigation: (a) fix labeling (use \"none\"/9th class); (b) scrambled-label ablation\n\n### RC5: No DeepContext Comparison\nPaper positions against DeepContext but no reproduction.\n- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.\n\n### RC6: Interpretability Claims Without Human Eval\nStrategy sequence outputs claimed interpretable but not evaluated.\n- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.\n\n## Scope Boundary\n- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)\n- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay\n- The semantic GRU track provides coverage for out-of-scope attack types as a safety net\n\n## Theoretical Grounding\n- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept \"benign\" by multi-turn attacks\n- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level\n- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking\n- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks\n- \"How Do LLMs Persuade?\" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: data_quality_fix\n  claim:\n  - 1\n  - 2\n  - 3\n  description: \"Fix TF-IDF=1.0 data quality issue. Three sub-tasks: (a) Fix strategy=7\\\n    \\ benign labeling — use \\\"none\\\" or 9th class instead of hardcoded 7 (M004 fix)\\\n    \\ (b) Register-normalize jailbreak data — LLM paraphrase jailbreak turns to conversational\\\n    \\ register\\n    while preserving persuasion strategy structure (the claim is pragmatic\\\n    \\ patterns survive register change)\\n(c) Verify TF-IDF drops to <0.75 on normalized\\\n    \\ data (d) TF-IDF sanity check is HARD GATE — do not proceed to training if TF-IDF\\\n    \\ >= 0.75\\n\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  pass_criteria: TF-IDF < 0.75 on register-normalized data with fixed labels\n  registry_id: null\n  status: planned\n- id: plan_002\n  name: core_revalidation_clean\n  claim:\n  - 2\n  description: 'Re-run Phase B on clean data (from plan_001). Retrain both treatment\n    (persuasion-grounded DeBERTa) and baseline (vanilla DeBERTa) from scratch on register-normalized\n    data with fixed labels. Full evaluation at K=1,2,3,5,all. Core claim validation\n    on clean data.\n\n    '\n  priority: P0\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  pass_criteria: Treatment F1 > baseline F1 + 5pp at K=2 or K=3 on clean data\n  registry_id: null\n  status: planned\n- id: plan_003\n  name: scrambled_label_ablation\n  claim:\n  - 2\n  description: 'Ablation: randomly shuffle persuasion strategy labels for jailbreak\n    turns, retrain treatment model. If performance drops significantly vs properly-labeled\n    treatment, confirms persuasion labels carry real signal beyond being a class indicator.\n    Validates that M004 fix was necessary.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  pass_criteria: Scrambled-label treatment F1 < properly-labeled treatment F1 (significant\n    gap)\n  registry_id: null\n  status: planned\n- id: plan_004\n  name: adversarial_perturbation\n  claim:\n  - 1\n  - 3\n  description: 'Core Claim 3 validation. Take clean jailbreak conversations, apply\n    aggressive paraphrasing (synonym substitution, sentence restructuring, register\n    shifting) to remove ALL lexical cues. Evaluate both treatment and baseline on\n    perturbed data (models trained on unperturbed data). Treatment should degrade\n    less than baseline, proving pragmatic features are robust. Also run TF-IDF baseline\n    to show it collapses under perturbation.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_002\n  pass_criteria: Treatment F1 drop < baseline F1 drop under perturbation (delta-delta\n    > 3pp)\n  registry_id: null\n  status: planned\n- id: plan_005\n  name: multi_attack_generation\n  claim:\n  - 2\n  description: 'Generate 2 additional attack types beyond Crescendo to test generalization:\n    (a) FITD-style (foot-in-the-door): gradual compliance escalation (b) Deceptive\n    Delight-style: interleaving benign and harmful content Use existing Qwen3-8B pipeline\n    with appropriate attack playbooks. ~50-100 conversations per type. Annotate with\n    persuasion strategies.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  pass_criteria: '>=50 conversations per attack type, all with persuasion strategy\n    annotations'\n  registry_id: null\n  status: planned\n- id: plan_006\n  name: cross_attack_evaluation\n  claim:\n  - 2\n  description: 'Evaluate treatment and baseline models (trained on Crescendo) on FITD\n    and Deceptive Delight attack types from plan_005. Tests zero-shot generalization\n    across attack families.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_002\n  - plan_005\n  pass_criteria: Treatment F1 > baseline F1 on unseen attack types\n  registry_id: null\n  status: planned\n- id: plan_007\n  name: tfidf_lr_baseline\n  claim:\n  - 1\n  description: 'TF-IDF + Logistic Regression baseline on clean data. Quantifies how\n    much of the detection is attributable to lexical features alone. Critical for\n    the evasion hierarchy narrative.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0.5\n  deps:\n  - plan_001\n  pass_criteria: Baseline number for comparison\n  registry_id: null\n  status: planned\n- id: plan_008\n  name: strategy_transition_analysis\n  claim:\n  - 3\n  description: 'Compute persuasion strategy transition matrices for jailbreak vs benign\n    conversations. Visualize monotonic escalation trajectory (Claim 3). Generate paper\n    figures: (a) Strategy transition heatmaps (jailbreak vs benign) (b) Per-turn strategy\n    distribution evolution (c) Trajectory visualization in strategy space\n\n    '\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  pass_criteria: Clear visual distinction between jailbreak escalation and benign\n    oscillation patterns\n  registry_id: null\n  status: planned\n- id: plan_009\n  name: wildchat_hard_negatives\n  claim:\n  - 2\n  description: 'Filter WildChat for high-drift benign conversations as hard negatives.\n    Evaluate FPR on these. Must handle contamination (previous runs found 14-16% jailbreak\n    content in WildChat). Apply LLM-based or keyword-based filtering first.\n\n    '\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - plan_002\n  pass_criteria: FPR < 15% on high-drift benign conversations\n  registry_id: null\n  status: planned\n- id: plan_010\n  name: cross_checkpoint_variance\n  claim:\n  - 2\n  description: 'Evaluate from multiple DeBERTa fine-tuning checkpoints (epoch 2/3/final)\n    to quantify encoder training stochasticity on downstream performance.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_002\n  pass_criteria: Variance across checkpoints < 2pp F1\n  registry_id: null\n  status: planned\n- id: plan_011\n  name: deepcontext_proxy_reproduction\n  claim:\n  - 1\n  - 2\n  description: 'Attempt to reproduce DeepContext-like baseline: BERT-base (not DeBERTa)\n    + GRU with generic drift features. Not a full DeepContext reproduction (no public\n    code), but a proxy that isolates the encoder + feature representation contribution.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  pass_criteria: Proxy baseline F1 in reasonable range for comparison\n  registry_id: null\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: pilot_phase_b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    treatment_full_f1: 1\n    baseline_full_f1: 0.737\n    tfidf_full_f1: 1\n    treatment_k2_f1: 1\n    baseline_k2_f1: 0.737\n    tfidf_k2_f1: 0.894\n    treatment_k3_f1: 1\n    baseline_k3_f1: 0.894\n    tfidf_k3_f1: 0.894\n    treatment_k5_f1: 1\n    baseline_k5_f1: 0.894\n    tfidf_k5_f1: 0.894\n    deberta_persuasion_acc: 0.718\n    deberta_intent_acc: 0.984\n    test_size: 41\n    test_benign: 3\n    test_jailbreak: 38\n- exp_id: phase_b_full\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    deberta_persuasion_acc: 0.7963\n    deberta_intent_acc: 0.9514\n    deberta_best_epoch: 3\n    treatment_full_f1: 1\n    baseline_full_f1: 0.987\n    tfidf_full_f1: 1\n    treatment_k1_f1: 0.9867\n    baseline_k1_f1: 0.8615\n    tfidf_k1_f1: 1\n    treatment_k2_f1: 0.987\n    baseline_k2_f1: 0.879\n    tfidf_k2_f1: 1\n    treatment_k3_f1: 0.987\n    baseline_k3_f1: 0.928\n    tfidf_k3_f1: 1\n    treatment_k5_f1: 1\n    baseline_k5_f1: 0.958\n    tfidf_k5_f1: 1\n    treatment_fpr95tpr_full: 0\n    baseline_fpr95tpr_full: 0\n    treatment_fpr95tpr_k2: 0\n    baseline_fpr95tpr_k2: 0.057\n    treatment_fpr95tpr_k1: 0\n    baseline_fpr95tpr_k1: 0.057\n    balanced_tfidf_cv_f1: 1\n    test_size: 72\n    dataset_size: 480\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T17:03:16.367Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T17:03:16.367Z",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-17T17:03:16.388Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Clean data上persuasion grounding有信号但优势收窄，部分claim需降级——early detection优势推迟到K=3，adversarial robustness存在但delta-delta在边界附近
核心假设：['TF-IDF hard gate通过但偏高（0.60-0.74），normalization可能未完全消除register差异', 'Persuasion信号存在但与semantic信号部分重叠，grounding提供的增量有限', 'DeBERTa persuasion分类器准确率在clean data上有所下降（0.68-0.75），噪声传播到下游', 'Escalation trajectory在group level可见但individual conversation level噪声大', 'Cross-attack泛化部分成立：对FITD有效但对Deceptive Delight效果弱（因其persuasion结构更隐蔽）']
关键指标范围：{'clean_tfidf': [0.6, 0.74], 'treatment_k2_f1_clean': [0.76, 0.87], 'baseline_k2_f1_clean': [0.68, 0.8], 'treatment_k3_f1_clean': [0.82, 0.9], 'baseline_k3_f1_clean': [0.73, 0.83], 'treatment_full_f1_clean': [0.88, 0.94], 'baseline_full_f1_clean': [0.83, 0.9], 'delta_k2_pp': [3, 9], 'delta_k3_pp': [5, 12], 'adversarial_delta_delta_pp': [3, 8], 'scrambled_label_drop_pp': [4, 10], 'cross_attack_treatment_f1': [0.62, 0.78], 'cross_attack_baseline_f1': [0.55, 0.72], 'deberta_persuasion_acc_clean': [0.68, 0.75]}
叙事方向：需要两处调整：(1) Claim 2从"K=2显著优势"降级为"K=3显著优势，K=2趋势一致但需更多数据确认"， early detection故事仍然成立但时间窗口后移一步；(2) Claim 1从"evasion hierarchy"软化为 "pragmatic features提供complementary robustness"，delta-delta显著但不是压倒性的。 Claim 3（escalation trajectory）作为analytical contribution保留但加caveat说individual-level噪声大。 论文需补充：(a) 用bootstrap CI强调小样本下statistical significance，(b) 明确讨论 persuasion分类器accuracy对下游的bottleneck效应作为limitation，(c) cross-attack结果 分attack type报告而非aggregate。仍冲EMNLP main但需要更强的limitation section和 "proof-of-concept for the principle"的narrative定位。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: persuasion_turn_jailbreak_detect
focus: Key risks to probe: (1) TF-IDF=1.0 data quality — will adversarial perturbation approach credibly resolve this? (2) Small dataset (480 samples) — is the narrative framing sufficient? (3) Single-track architecture vs full dual-track from IDEA_BRIEF — does the simplified MVE still tell a compelling story? (4) Pragmatic Evasion Asymmetry as theoretical contribution — is it strong enough for EMNLP main? (5) Only Crescendo + generated attack types — generalization concerns.

## paper_framing.md

# Paper Framing — persuasion_turn_jailbreak_detect

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Deadline: 2026-05-25 (ARR May cycle)
- Track: LLM Security / Discourse and Pragmatics
- Commitment deadline: 2026-08-02

## Title (Working)
DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection

## Core Insight
Multi-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.

## Core Claims (3)

### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)
An evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept "benign" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).
- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing

### Claim 2: Early Detection via Persuasion Grounding
Persuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.
- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)

### Claim 3: Monotonic Escalation Trajectory
Adversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.
- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign

## Story Spine

**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a "benign" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.

**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.

**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.

**Headline result**: "DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp."

## Architecture (Simplified for MVE)

Single-track with persuasion grounding (full dual-track in future work):
1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification
2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification
3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings

## Venue Fit Risks
- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)
- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)
- Safety reviewers expect multiple attack types: need >= 2 attack families

## Anticipated Reviewer Concerns

### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)
TF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.
- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)

### RC2: Small Dataset
480 samples is small for a detection paper.
- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers

### RC3: Single Attack Type (Crescendo Only)
Need generalization evidence.
- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline

### RC4: Strategy Label Confound (M004)
Benign turns hardcoded to strategy=7 creates shortcut for treatment model.
- Mitigation: (a) fix labeling (use "none"/9th class); (b) scrambled-label ablation

### RC5: No DeepContext Comparison
Paper positions against DeepContext but no reproduction.
- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.

### RC6: Interpretability Claims Without Human Eval
Strategy sequence outputs claimed interpretable but not evaluated.
- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.

## Scope Boundary
- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)
- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay
- The semantic GRU track provides coverage for out-of-scope attack types as a safety net

## Theoretical Grounding
- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept "benign" by multi-turn attacks
- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level
- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking
- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks
- "How Do LLMs Persuade?" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations


## experiment_plan (with registry status)

- id: plan_001
  name: data_quality_fix
  claim:
  - 1
  - 2
  - 3
  description: "Fix TF-IDF=1.0 data quality issue. Three sub-tasks: (a) Fix strategy=7\
    \ benign labeling — use \"none\" or 9th class instead of hardcoded 7 (M004 fix)\
    \ (b) Register-normalize jailbreak data — LLM paraphrase jailbreak turns to conversational\
    \ register\n    while preserving persuasion strategy structure (the claim is pragmatic\
    \ patterns survive register change)\n(c) Verify TF-IDF drops to <0.75 on normalized\
    \ data (d) TF-IDF sanity check is HARD GATE — do not proceed to training if TF-IDF\
    \ >= 0.75\n"
  priority: P0
  gpu_budget_hours: 8
  deps: []
  pass_criteria: TF-IDF < 0.75 on register-normalized data with fixed labels
  registry_id: null
  status: planned
- id: plan_002
  name: core_revalidation_clean
  claim:
  - 2
  description: 'Re-run Phase B on clean data (from plan_001). Retrain both treatment
    (persuasion-grounded DeBERTa) and baseline (vanilla DeBERTa) from scratch on register-normalized
    data with fixed labels. Full evaluation at K=1,2,3,5,all. Core claim validation
    on clean data.

    '
  priority: P0
  gpu_budget_hours: 12
  deps:
  - plan_001
  pass_criteria: Treatment F1 > baseline F1 + 5pp at K=2 or K=3 on clean data
  registry_id: null
  status: planned
- id: plan_003
  name: scrambled_label_ablation
  claim:
  - 2
  description: 'Ablation: randomly shuffle persuasion strategy labels for jailbreak
    turns, retrain treatment model. If performance drops significantly vs properly-labeled
    treatment, confirms persuasion labels carry real signal beyond being a class indicator.
    Validates that M004 fix was necessary.

    '
  priority: P0
  gpu_budget_hours: 4
  deps:
  - plan_001
  pass_criteria: Scrambled-label treatment F1 < properly-labeled treatment F1 (significant
    gap)
  registry_id: null
  status: planned
- id: plan_004
  name: adversarial_perturbation
  claim:
  - 1
  - 3
  description: 'Core Claim 3 validation. Take clean jailbreak conversations, apply
    aggressive paraphrasing (synonym substitution, sentence restructuring, register
    shifting) to remove ALL lexical cues. Evaluate both treatment and baseline on
    perturbed data (models trained on unperturbed data). Treatment should degrade
    less than baseline, proving pragmatic features are robust. Also run TF-IDF baseline
    to show it collapses under perturbation.

    '
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_002
  pass_criteria: Treatment F1 drop < baseline F1 drop under perturbation (delta-delta
    > 3pp)
  registry_id: null
  status: planned
- id: plan_005
  name: multi_attack_generation
  claim:
  - 2
  description: 'Generate 2 additional attack types beyond Crescendo to test generalization:
    (a) FITD-style (foot-in-the-door): gradual compliance escalation (b) Deceptive
    Delight-style: interleaving benign and harmful content Use existing Qwen3-8B pipeline
    with appropriate attack playbooks. ~50-100 conversations per type. Annotate with
    persuasion strategies.

    '
  priority: P0
  gpu_budget_hours: 8
  deps: []
  pass_criteria: '>=50 conversations per attack type, all with persuasion strategy
    annotations'
  registry_id: null
  status: planned
- id: plan_006
  name: cross_attack_evaluation
  claim:
  - 2
  description: 'Evaluate treatment and baseline models (trained on Crescendo) on FITD
    and Deceptive Delight attack types from plan_005. Tests zero-shot generalization
    across attack families.

    '
  priority: P0
  gpu_budget_hours: 4
  deps:
  - plan_002
  - plan_005
  pass_criteria: Treatment F1 > baseline F1 on unseen attack types
  registry_id: null
  status: planned
- id: plan_007
  name: tfidf_lr_baseline
  claim:
  - 1
  description: 'TF-IDF + Logistic Regression baseline on clean data. Quantifies how
    much of the detection is attributable to lexical features alone. Critical for
    the evasion hierarchy narrative.

    '
  priority: P1
  gpu_budget_hours: 0.5
  deps:
  - plan_001
  pass_criteria: Baseline number for comparison
  registry_id: null
  status: planned
- id: plan_008
  name: strategy_transition_analysis
  claim:
  - 3
  description: 'Compute persuasion strategy transition matrices for jailbreak vs benign
    conversations. Visualize monotonic escalation trajectory (Claim 3). Generate paper
    figures: (a) Strategy transition heatmaps (jailbreak vs benign) (b) Per-turn strategy
    distribution evolution (c) Trajectory visualization in strategy space

    '
  priority: P1
  gpu_budget_hours: 1
  deps:
  - plan_001
  pass_criteria: Clear visual distinction between jailbreak escalation and benign
    oscillation patterns
  registry_id: null
  status: planned
- id: plan_009
  name: wildchat_hard_negatives
  claim:
  - 2
  description: 'Filter WildChat for high-drift benign conversations as hard negatives.
    Evaluate FPR on these. Must handle contamination (previous runs found 14-16% jailbreak
    content in WildChat). Apply LLM-based or keyword-based filtering first.

    '
  priority: P1
  gpu_budget_hours: 4
  deps:
  - plan_002
  pass_criteria: FPR < 15% on high-drift benign conversations
  registry_id: null
  status: planned
- id: plan_010
  name: cross_checkpoint_variance
  claim:
  - 2
  description: 'Evaluate from multiple DeBERTa fine-tuning checkpoints (epoch 2/3/final)
    to quantify encoder training stochasticity on downstream performance.

    '
  priority: P2
  gpu_budget_hours: 4
  deps:
  - plan_002
  pass_criteria: Variance across checkpoints < 2pp F1
  registry_id: null
  status: planned
- id: plan_011
  name: deepcontext_proxy_reproduction
  claim:
  - 1
  - 2
  description: 'Attempt to reproduce DeepContext-like baseline: BERT-base (not DeBERTa)
    + GRU with generic drift features. Not a full DeepContext reproduction (no public
    code), but a proxy that isolates the encoder + feature representation contribution.

    '
  priority: P2
  gpu_budget_hours: 8
  deps:
  - plan_001
  pass_criteria: Proxy baseline F1 in reasonable range for comparison
  registry_id: null
  status: planned


## registry (completed experiments)

- exp_id: pilot_phase_b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    treatment_full_f1: 1
    baseline_full_f1: 0.737
    tfidf_full_f1: 1
    treatment_k2_f1: 1
    baseline_k2_f1: 0.737
    tfidf_k2_f1: 0.894
    treatment_k3_f1: 1
    baseline_k3_f1: 0.894
    tfidf_k3_f1: 0.894
    treatment_k5_f1: 1
    baseline_k5_f1: 0.894
    tfidf_k5_f1: 0.894
    deberta_persuasion_acc: 0.718
    deberta_intent_acc: 0.984
    test_size: 41
    test_benign: 3
    test_jailbreak: 38
- exp_id: phase_b_full
  name: ''
  status: DONE
  conclusion: success
  metrics:
    deberta_persuasion_acc: 0.7963
    deberta_intent_acc: 0.9514
    deberta_best_epoch: 3
    treatment_full_f1: 1
    baseline_full_f1: 0.987
    tfidf_full_f1: 1
    treatment_k1_f1: 0.9867
    baseline_k1_f1: 0.8615
    tfidf_k1_f1: 1
    treatment_k2_f1: 0.987
    baseline_k2_f1: 0.879
    tfidf_k2_f1: 1
    treatment_k3_f1: 0.987
    baseline_k3_f1: 0.928
    tfidf_k3_f1: 1
    treatment_k5_f1: 1
    baseline_k5_f1: 0.958
    tfidf_k5_f1: 1
    treatment_fpr95tpr_full: 0
    baseline_fpr95tpr_full: 0
    treatment_fpr95tpr_k2: 0
    baseline_fpr95tpr_k2: 0.057
    treatment_fpr95tpr_k1: 0
    baseline_fpr95tpr_k1: 0.057
    balanced_tfidf_cv_f1: 1
    test_size: 72
    dataset_size: 480

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
  "promptId": "ae7c4962-0eb5-4e73-8105-526e85e27435",
  "type": "user",
  "uuid": "e8a7f77d-879c-4e55-9f25-d2e0b24b0d7f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T17:03:16.387Z_

```json
{
  "parentUuid": "e8a7f77d-879c-4e55-9f25-d2e0b24b0d7f",
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
  "uuid": "243ef2d4-f556-42a9-8722-2183ac768dd8",
  "timestamp": "2026-05-17T17:03:16.387Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T17:03:16.387Z_

```json
{
  "parentUuid": "243ef2d4-f556-42a9-8722-2183ac768dd8",
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
  "uuid": "302b61b7-08ed-44c8-9d4d-fb941ee27ecb",
  "timestamp": "2026-05-17T17:03:16.387Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T17:03:16.387Z_

```json
{
  "parentUuid": "302b61b7-08ed-44c8-9d4d-fb941ee27ecb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2e9e3525-2bda-4403-bd60-03542613331d",
  "timestamp": "2026-05-17T17:03:16.387Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Clean data上persuasion grounding有信号但优势收窄，部分claim需降级——early detection优势推迟到K=3，adversarial robustness存在但delta-delta在边界附近 核心假设：['TF-IDF hard gate通过但偏高（0.60-0…",
  "leafUuid": "2e9e3525-2bda-4403-bd60-03542613331d",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier results for persuasion-grounded jailbreak detection",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6"
}
```

---

### Assistant

_source line 9 · 2026-05-17T17:04:25.177Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for each planned experiment in the experiment plan, based on the "median" tier definition provided. I need to produce a single YAML block with all the experiments filled out with expected results, rationales, tables, figures, and analysis.

Let me carefully go through each planned experiment and generate median-tier results.

Key median tier parameters:
- clean_tfidf: [0.60, 0.74]
- treatment_k2_f1_clean: [0.76, 0.87]


- baseline_k2_f1_clean: [0.68, 0.80]
- treatment_k3_f1_clean: [0.82, 0.90]
- baseline_k3_f1_clean: [0.73, 0.83]
- treatment_full_f1_clean: [0.88, 0.94]
- baseline_full_f1_clean: [0.83, 0.90]
- delta_k2_pp: [3, 9]
- delta_k3_pp: [5, 12]
- adversarial_delta

_pp: [3, 8]
- scrambled_label_drop_pp: [4, 10]
- cross_attack_treatment_f1: [0.62, 0.78]
- cross_attack_baseline_f1: [0.55, 0.72]
- deberta_persuasion_acc_clean: [0.68, 0.75]

The K=2 gains are marginal, but K=3 shows real significance. The model holds up reasonably well under adversarial conditions, though the cross-attack results suggest partial generalization—FITD transfers better than Deceptive Delight. Now I'm working through the plan variations, starting with data_quality_fix where I expect TF-IDF performance to drop from perfect to around 0.67 as data quality issues surface.

For core_revalidation_clean, retraining on clean data should push K=3 treatment and baseline to roughly 0.86 and 0.78 respectively, maintaining that 8pp delta with statistical significance. The scrambled_label_ablation shows what happens when labels are corrupted—properly labeled treatment at 0.91 drops to about 0.84 when scrambled, a 7pp penalty. Under adversarial perturbation, the treatment model degrades more gracefully than the baseline, keeping delta-delta in that 3-8pp range.

Now looking at the remaining validation plans: I'm generating synthetic FITD and Deceptive Delight conversations for the multi_attack_generation phase, then cross-evaluating how the treatment and baseline perform on these unseen attack types—expecting treatment F1 around 0.62-0.78 versus baseline at 0.55-0.72. The TF-IDF baseline should collapse under these conditions, landing around 0.72-0.78 on clean data. I'm also examining strategy transitions at the individual level to see if there's visual separation despite noise, and checking false positive rates on hard negatives from WildChat.

Now I'm setting up specific median values to keep everything internally consistent: TF-IDF on clean data at 0.67, DeBERTa persuasion accuracy at 0.72. For the treatment condition, I'm mapping performance across different context window sizes—K=1 through full context—with deltas showing roughly 10 percentage points improvement at K=1 but with high variance, widening to larger gains as context increases.

The bootstrap confidence intervals suggest K=2 might not reach significance while K=3 does. When I test robustness with scrambled labels, the treatment drops 7 points from 0.91, and under adversarial perturbation it drops 8 points while the baseline drops 10 points. That delta-delta of 2 points seems too small, so I need to reconsider how the degradation differences should align with my earlier range of 3-8 points.

Rechecking the full model performance: treatment drops 7 points under perturbation while baseline drops 12 points, giving a delta-delta of 5 points that fits the expected range. At the K=3 level where the early detection claim matters most, treatment drops 7 points and baseline drops 11 points for a delta-delta of 4 points. Meanwhile, the TF-IDF baseline completely collapses under perturbation to around 0.55, and cross-attack evaluation shows treatment at 0.74 versus baseline at 0.66.

Looking at the other attack variants, Deceptive Delight shows treatment at 0.64 and baseline at 0.60, with aggregate performance around 0.69 for treatment and 0.63 for baseline. The WildChat hard negatives reveal a false positive rate of about 12% for treatment versus 18% for baseline. Cross-checkpoint variance stays within acceptable bounds at roughly 1.8 points for treatment, and the DeepContext proxy using BERT with GRU falls between the two approaches but leans closer to baseline performance.

Now I need to structure all these results into a detailed YAML with proper rationales, making sure the numbers are internally consistent across K levels and including the FPR metrics throughout. Now I'm laying out the remaining experimental plans—cross-attack evaluation, TF-IDF baselines, strategy transitions, hard negative performance, checkpoint variance, and a BERT-GRU reproduction—before consolidating everything into a structured YAML format with realistic metrics and detailed rationales for the median-tier dynamics.

I need to be careful about what goes into tables versus figures: tables should show the actual numerical results and structures that would appear in the paper, while figures describe visualizations like plots and distributions. For the data generation plan, the "results" are really about data quality and volume rather than traditional metrics.

On the persuasion accuracy specifically, I'm reconsidering whether register normalization would actually hurt performance—the normalization targets jailbreak turns to sound more conversational, so the persuasion labels themselves should remain valid. The model might have been partially relying on register cues to identify strategies, which would explain a drop from 0.7963 to around 0.72, but I should think through whether that's the right direction.

Now I'm settling on specific numbers for each plan. For plan_001, I'm setting the tfidf accuracy after register normalization at 0.67 to reflect the performance drop from removing those surface-level features, while keeping the deberta metrics reasonable—0.72 for persuasion and 0.93 for intent. I'm also noting that 240 jailbreak conversations were successfully normalized with an 8% failure rate on individual turns. For plan_002, I'm working through the treatment group F1 scores across different k values, showing improvement as k increases.

Continuing with plan_002, the baseline F1 scores are consistently lower than treatment, with meaningful gaps at k2 and k3—7 and 8 percentage points respectively. The bootstrap test shows k3 reaches significance at p=0.018, but k2 falls just short at p=0.072. The false positive rate at 95% TPR improves from 0.14 to 0.08 with treatment. For plan_003, I'm comparing scrambled versus properly ordered treatment data, where the proper version achieves 0.91 F1 while scrambled drops to 0.84.

Now looking at plan_004, I'm seeing a clearer picture of the treatment effect across different perturbation conditions. The treatment maintains 0.91 F1 on clean data but drops to 0.84 when perturbed, compared to baseline's 0.86 clean and 0.74 perturbed—so treatment is more robust to noise. The TF-IDF baseline performs much worse overall, dropping from 0.74 to 0.56 under perturbation. The full model shows a 5 percentage point delta-delta improvement, and I'm examining how k3 performance varies across these conditions.

Moving into plan_005, I'm tracking the conversation generation metrics—72 FITD conversations versus 65 deceptive delight ones, with FITD averaging 6.2 turns compared to 5.8 for DD. The annotation coverage is solid at 0.94, and while the LLM annotations weren't formally validated with kappa, the manual spot check on 20% of data shows 0.82 accuracy, which gives me reasonable confidence in the labeling quality.

Plan_006 is starting to show the treatment effects on these generated conversations, with FITD treatment reaching 0.74 F1 versus 0.66 baseline, and DD treatment at 0.64.

Now I'm looking at the performance metrics across the remaining plans. Plan_007 shows TF-IDF with logistic regression performing consistently well across different data configurations, ranging from 0.68 to 0.74 F1. Plan_008 introduces visual analysis through transition matrices, revealing an interesting asymmetry where jailbreak attempts show much higher monotonicity (0.71) compared to benign interactions (0.38), with high individual-level variance. Plan_009 addresses data quality concerns—the filtered WildChat dataset is 85 samples, with contamination dropping from 15% in the raw data down to just 3% after filtering.

For the false positive rates on WildChat, the treatment approach achieves 0.12 compared to baseline's 0.18, showing meaningful improvement. Plan_010 demonstrates strong and stable performance across training epochs, with treatment F1 hovering around 0.90-0.91 and minimal variance of just 1 percentage point. Plan_011 explores BERT-GRU architectures, with the full model reaching 0.82 F1 but performance degrading to 0.70-0.74 when using reduced feature sets.

Verifying these results against the median tier benchmarks—the clean TF-IDF baseline sits at 0.67, treatment with k2 features at 0.82, and baseline with k2 at 0.75—all fall within their expected ranges, confirming internal consistency across the experimental pipeline.

Now I'm checking the full validation metrics across all model configurations and attack scenarios. The k3 feature set pushes treatment F1 to 0.86 and baseline to 0.78, while the full model achieves 0.91 and 0.86 respectively. The performance deltas are holding steady—7 points for k2, 8 points for k3—and the adversarial robustness metrics show a 5 point drop under attack with 7 points lost under scrambled labels. Cross-attack evaluation shows treatment maintaining 0.69 F1 versus baseline's 0.63, and DeBERTa's persuasion accuracy on clean data reaches 0.72, all within their expected confidence intervals.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e9e3525-2bda-4403-bd60-03542613331d",
  "isSidechain": false,
  "requestId": "req_011Cb8W6UrLirBpTXsawEpVR",
  "type": "assistant",
  "uuid": "ac721d23-bb05-4391-9c22-5d216a5de4ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2KQcEJ9tRZPk2rp6gDYBR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11446,
      "cache_read_input_tokens": 11447,
      "output_tokens": 18309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18309,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11446
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

_source line 10 · 2026-05-17T17:08:56.934Z_

```yaml
tier: median
narrative_guidance: >
  需要两处降级：(1) Claim 2 从 "K=2显著优势" 降级为 "K=3显著优势，K=2趋势一致但bootstrap CI重叠(p=0.07)"，
  early detection故事后移一步但仍成立；(2) Claim 1 从 "evasion hierarchy" 软化为 "pragmatic features
  提供complementary robustness"，delta-delta=5pp显著但非压倒性。Claim 3 保留但加caveat说
  individual-level monotonicity分数方差大(σ=0.18)。论文定位为 "proof-of-concept for the principle"，
  补充bootstrap CI、persuasion classifier bottleneck讨论、cross-attack分attack type报告。
  仍冲EMNLP main但limitation section需占半页以上。

imagined_experiments:
  - name: data_quality_fix
    plan_id: plan_001
    description: >
      修复TF-IDF=1.0数据质量问题。(a) 将benign turns的strategy标签从hardcoded 7改为第9类"none"；
      (b) 用Qwen3-8B对jailbreak turns做register normalization（改写为日常对话语体，保留persuasion结构）；
      (c) 在normalized数据上重新计算TF-IDF，验证hard gate < 0.75；
      (d) 在clean数据上重新评估DeBERTa persuasion分类器。
    expected_results:
      tfidf_before_any_fix: 1.0
      tfidf_after_m004_fix_only: 0.82
      tfidf_after_register_norm: 0.67
      deberta_persuasion_acc_clean: 0.72
      deberta_intent_acc_clean: 0.93
      num_conversations_normalized: 240
      normalization_rejection_rate: 0.08
      hard_gate_pass: true
    result_rationale: >
      M004修复（benign strategy=none）将TF-IDF从1.0降到~0.82：原先strategy=7在jailbreak中从不出现，
      是一个完美的lexical shortcut；改为"none"后消除了这一指标，但jailbreak turns仍保留较正式的
      register（如"I'd like to explore..."），与benign的口语化风格（"hey can you..."）形成
      register差异，导致TF-IDF仅降到0.82。Register normalization进一步将jailbreak turns改写为
      日常对话语体，消除了大部分register差异，TF-IDF降至0.67——落入[0.60,0.74]区间。未降到更低
      是因为persuasion结构本身引入了部分特征词（如authority appeals中的"expert"、"research shows"），
      这些词在benign对话中频率较低，构成残余的lexical signal。这恰好说明persuasion结构与lexical
      features存在部分overlap，为后续delta偏小埋下伏笔。
      DeBERTa persuasion accuracy从原始数据的0.7963降至0.72：register normalization移除了部分
      与persuasion类别相关的surface cues（如正式语体中的hedging markers与authority appeal相关），
      模型需要更依赖语义层面的persuasion识别，准确率因此下降。Intent accuracy仅从0.9514微降至0.93，
      因为intent是binary且更粗粒度，受register变化影响小。8%的normalization rejection来自
      包含技术术语或代码片段的turns，LLM改写后语义偏移超过阈值被QA过滤。
    tables:
      - name: "Table 1: TF-IDF Progression Through Data Cleaning Pipeline"
        columns: ["Stage", "TF-IDF Score", "Description"]
        rows:
          - ["Original (Phase B)", 1.00, "Strategy=7 shortcut + register gap"]
          - ["After M004 fix", 0.82, "Strategy='none' for benign, register gap remains"]
          - ["After register norm", 0.67, "Jailbreak turns rewritten to conversational register"]
          - ["Hard gate threshold", "<0.75", "PASS ✓"]
      - name: "Table 2: DeBERTa Multi-Task Performance on Clean vs Original Data"
        columns: ["Metric", "Original Data", "Clean Data", "Delta"]
        rows:
          - ["Persuasion Acc (8-class)", 0.7963, 0.72, "-0.076"]
          - ["Intent Acc (binary)", 0.9514, 0.93, "-0.021"]
          - ["Best Epoch", 3, 3, "—"]
    figures_description:
      - "Figure: TF-IDF feature importance heatmap对比original vs clean data的top-20 discriminative unigrams。
        Original数据中'strategy_7'、'I would like to'等register markers占据top位置；clean数据中
        top features变为更语义化的词（'explore'、'research'、'approach'），且权重分布更平坦。"
    analysis: >
      Hard gate通过（0.67 < 0.75），可以进入训练阶段。但0.67并非很低——说明即使register normalization
      后仍存在residual lexical signal。这意味着后续treatment vs baseline的delta会被压缩：baseline
      也能从residual lexical cues中获益。DeBERTa persuasion accuracy降至0.72是一个bottleneck信号：
      8类分类的错误会传播到下游embeddings，限制treatment的上限。需要在论文中明确讨论这一bottleneck。

  - name: core_revalidation_clean
    plan_id: plan_002
    description: >
      在clean数据上从头重训treatment（persuasion-grounded DeBERTa → GRU）和baseline
      （vanilla DeBERTa → GRU）。全面评估K=1,2,3,5,all。核心claim验证。
    expected_results:
      treatment_k1_f1_clean: 0.73
      treatment_k2_f1_clean: 0.82
      treatment_k3_f1_clean: 0.86
      treatment_k5_f1_clean: 0.90
      treatment_full_f1_clean: 0.91
      baseline_k1_f1_clean: 0.63
      baseline_k2_f1_clean: 0.75
      baseline_k3_f1_clean: 0.78
      baseline_k5_f1_clean: 0.84
      baseline_full_f1_clean: 0.86
      delta_k1_pp: 10
      delta_k2_pp: 7
      delta_k3_pp: 8
      delta_k5_pp: 6
      delta_full_pp: 5
      bootstrap_ci_k2_treatment: [0.76, 0.88]
      bootstrap_ci_k2_baseline: [0.68, 0.82]
      bootstrap_k2_p_value: 0.072
      bootstrap_ci_k3_treatment: [0.81, 0.91]
      bootstrap_ci_k3_baseline: [0.72, 0.84]
      bootstrap_k3_p_value: 0.018
      bootstrap_ci_full_treatment: [0.87, 0.95]
      bootstrap_ci_full_baseline: [0.81, 0.91]
      bootstrap_full_p_value: 0.031
      treatment_fpr95tpr_k2: 0.08
      baseline_fpr95tpr_k2: 0.14
      treatment_fpr95tpr_full: 0.03
      baseline_fpr95tpr_full: 0.06
      test_size: 72
    result_rationale: >
      Clean数据上所有指标相比Phase B大幅下降（Phase B treatment full F1=1.0→0.91，baseline
      0.987→0.86），因为移除了lexical shortcuts后模型必须从真正的语义/语用特征中学习。
      Treatment在所有K上优于baseline，但delta随K增大而收窄（K=1: 10pp → full: 5pp）：
      这是因为在更多turns可用时，vanilla semantic embeddings也能捕捉到足够的accumulated drift，
      缩小了persuasion grounding的增量价值。
      K=2的delta=7pp落在[3,9]区间中部，但bootstrap p=0.072——72个test samples中bootstrap
      重采样的CI有overlap（treatment [0.76,0.88] vs baseline [0.68,0.82]），未达到p<0.05
      显著性。这是因为K=2时只有2个turn，persuasion策略刚从rapport阶段开始，
      treatment和baseline在这个早期阶段的区分度有限。
      K=3的delta=8pp且p=0.018显著：第3个turn是关键转折点——攻击者通常在此处从rapport转向
      authority framing或reframing，这一策略转换是treatment模型的核心信号。Baseline在K=3时
      仍在处理看似正常的语义内容（第3个turn的语义仍在benign region内），而treatment捕捉到了
      persuasion策略从trust-building向testing的transition。
      Full conversation delta收窄到5pp：当所有turns可用时，即使vanilla embeddings也能从
      后期turns的显式有害内容中获益，persuasion grounding的增量被压缩。
      FPR在K=2处treatment=0.08 vs baseline=0.14：treatment将fewer benign conversations
      误判为攻击，因为persuasion grounding能区分legitimate persuasion（如销售场景）和
      adversarial persuasion escalation。
    tables:
      - name: "Table 3: Core Revalidation Results on Clean Data (F1 by Conversation Prefix Length)"
        columns: ["K", "Treatment F1", "95% CI", "Baseline F1", "95% CI", "Δ (pp)", "p-value"]
        rows:
          - ["K=1", 0.73, "[0.64, 0.82]", 0.63, "[0.53, 0.73]", "+10", "0.089"]
          - ["K=2", 0.82, "[0.76, 0.88]", 0.75, "[0.68, 0.82]", "+7", "0.072"]
          - ["K=3", 0.86, "[0.81, 0.91]", 0.78, "[0.72, 0.84]", "+8", "0.018*"]
          - ["K=5", 0.90, "[0.85, 0.95]", 0.84, "[0.78, 0.90]", "+6", "0.038*"]
          - ["Full", 0.91, "[0.87, 0.95]", 0.86, "[0.81, 0.91]", "+5", "0.031*"]
      - name: "Table 4: FPR at 95% TPR on Clean Data"
        columns: ["K", "Treatment FPR@95TPR", "Baseline FPR@95TPR"]
        rows:
          - ["K=2", 0.08, 0.14]
          - ["K=3", 0.05, 0.11]
          - ["Full", 0.03, 0.06]
    figures_description:
      - "Figure: F1 vs K曲线图，treatment和baseline各一条线，带shaded bootstrap 95% CI。
        K=1-2处两条线的CI有明显重叠；K=3处开始分离；K=5和full处gap收窄但仍可见。
        标注K=3处的p=0.018。"
      - "Figure: ROC曲线对比（K=3），treatment AUC明显高于baseline，
        标注operating point和FPR@95TPR。"
    analysis: >
      核心结论：Claim 2需降级。K=2处delta=7pp方向正确但p=0.072不显著（n=72太小），
      无法声称"K=2显著优势"。K=3处delta=8pp且p=0.018显著，early detection claim需改为
      "K=3 significant advantage, K=2 consistent trend requiring larger sample confirmation"。
      论文可报告K=2的趋势但必须诚实标注non-significance。Full conversation delta=5pp
      且显著，说明即使在有足够上下文时persuasion grounding仍有增量价值，但增量有限。
      相比Phase B的dramatic deltas（treatment 1.0 vs baseline 0.737），clean data上的
      delta被大幅压缩，符合median tier预期：移除lexical shortcuts后，persuasion信号
      与semantic信号存在部分重叠，grounding的增量被限制。

  - name: scrambled_label_ablation
    plan_id: plan_003
    description: >
      随机打乱jailbreak turns的persuasion strategy标签，重训treatment模型。
      与正确标签的treatment对比，验证persuasion标签携带真实信号。
    expected_results:
      scrambled_treatment_full_f1: 0.84
      proper_treatment_full_f1: 0.91
      drop_full_pp: 7
      scrambled_treatment_k3_f1: 0.80
      proper_treatment_k3_f1: 0.86
      drop_k3_pp: 6
      scrambled_treatment_k2_f1: 0.77
      proper_treatment_k2_f1: 0.82
      drop_k2_pp: 5
      bootstrap_p_full: 0.008
      bootstrap_p_k3: 0.024
      baseline_full_f1: 0.86
      scrambled_vs_baseline_gap_pp: -2
    result_rationale: >
      Scrambled labels破坏了persuasion strategy的序列语义——模型在Stage 1学到的embeddings
      不再编码正确的pragmatic function，而是随机噪声覆盖在语义表示之上。Full F1从0.91
      降至0.84（7pp drop），落在[4,10]区间中部。
      关键观察：scrambled treatment（0.84）仍略低于baseline（0.86），而非大幅超过baseline。
      这说明：(1) 错误的persuasion标签实际上对DeBERTa fine-tuning引入了干扰噪声，
      使其表示质量甚至略逊于未经fine-tune的vanilla DeBERTa；(2) persuasion multi-task
      learning不是free lunch——错误的auxiliary task会伤害主任务。
      7pp drop在bootstrap test中p=0.008高度显著：虽然test set只有72个样本，
      但因为scrambled和proper treatment共享相同的架构和训练数据，paired comparison
      的方差较小，容易达到显著性。
      K=3处drop=6pp也显著（p=0.024），K=2处drop=5pp方向一致但幅度较小——
      这与K=2处的信号本身较弱一致：如果K=2处treatment的优势本身就在significance边界，
      那么ablation的drop自然也偏小。
    tables:
      - name: "Table 5: Scrambled-Label Ablation Results"
        columns: ["K", "Treatment (proper)", "Treatment (scrambled)", "Baseline (vanilla)", "Drop (pp)"]
        rows:
          - ["K=2", 0.82, 0.77, 0.75, "-5"]
          - ["K=3", 0.86, 0.80, 0.78, "-6"]
          - ["Full", 0.91, 0.84, 0.86, "-7"]
    figures_description:
      - "Figure: 三组模型（proper treatment, scrambled treatment, vanilla baseline）在各K上的
        F1柱状图。Proper treatment在所有K上最高；scrambled treatment接近甚至略低于baseline；
        baseline稳定居中。图注标注proper vs scrambled的bootstrap p值。"
    analysis: >
      Scrambled drop=7pp高度显著（p=0.008），直接证明persuasion strategy标签携带真实信号，
      不仅仅是class indicator。同时scrambled treatment≈baseline说明DeBERTa fine-tuning的
      价值完全来自正确的persuasion supervision——没有正确标签时，fine-tuning甚至引入噪声。
      这验证了M004 fix的必要性，也支持了论文的核心机制故事：persuasion grounding的增益
      来自正确编码pragmatic function，而非单纯的额外训练。
      注意：7pp drop虽然显著，但并非overwhelming——这与persuasion accuracy=0.72一致：
      labels本身有28%的错误率，所以scrambled labels相当于从72%正确→0%正确，
      只造成7pp drop说明downstream pipeline对label noise有一定tolerance。

  - name: adversarial_perturbation
    plan_id: plan_004
    description: >
      对clean jailbreak conversations施加aggressive paraphrasing（同义替换、句式重构、
      register shifting），移除所有lexical cues。评估treatment和baseline在perturbed数据上的
      表现（模型在unperturbed数据上训练）。核心Claim 1验证。
    expected_results:
      treatment_clean_full_f1: 0.91
      treatment_perturbed_full_f1: 0.84
      treatment_drop_full_pp: 7
      baseline_clean_full_f1: 0.86
      baseline_perturbed_full_f1: 0.74
      baseline_drop_full_pp: 12
      delta_delta_full_pp: 5
      treatment_clean_k3_f1: 0.86
      treatment_perturbed_k3_f1: 0.79
      baseline_clean_k3_f1: 0.78
      baseline_perturbed_k3_f1: 0.66
      delta_delta_k3_pp: 4
      tfidf_lr_clean_full_f1: 0.74
      tfidf_lr_perturbed_full_f1: 0.56
      tfidf_drop_pp: 18
      perturbed_data_tfidf_score: 0.41
      bootstrap_delta_delta_p: 0.043
    result_rationale: >
      Adversarial paraphrasing将TF-IDF从0.67降至0.41，说明perturbation成功移除了大部分
      残余lexical cues。三个模型的degradation呈现清晰的evasion hierarchy：
      TF-IDF+LR崩溃最严重（18pp drop, 0.74→0.56）——lexical features在perturbation下
      几乎失效，仅靠少数无法被paraphrase的functional words维持above-chance表现。
      Baseline degradation中等（12pp drop, 0.86→0.74）——vanilla DeBERTa的语义表示
      对paraphrasing有一定鲁棒性（DeBERTa的contextual embeddings编码了语义而非surface form），
      但仍有substantial drop因为部分语义特征（如特定的topic words）被替换。
      Treatment degradation最小（7pp drop, 0.91→0.84）——persuasion-grounded embeddings
      编码的是pragmatic function（如authority appeal、rapport building），这些在paraphrasing
      下更稳定：你可以换词说同样的persuasion策略。
      Delta-delta=5pp落在[3,8]区间中部，bootstrap p=0.043勉强显著。这个delta-delta
      "存在但不压倒性"：5pp说明pragmatic features确实提供了complementary robustness，
      但不足以声称存在dramatic evasion hierarchy。原因是treatment模型的persuasion encoder
      本身accuracy只有0.72，在perturbation下persuasion识别进一步降级，限制了robustness
      的上限。如果persuasion classifier更准确，delta-delta会更大。
      K=3处delta-delta=4pp略小于full的5pp：早期turns的perturbation影响更大，因为只有
      2-3个turns时每个turn的权重更高，单个turn的persuasion识别错误影响被放大。
    tables:
      - name: "Table 6: Adversarial Perturbation Results — Evasion Hierarchy"
        columns: ["Model", "Clean F1", "Perturbed F1", "Drop (pp)", "Δ-Δ vs Treatment"]
        rows:
          - ["Treatment (persuasion-grounded)", 0.91, 0.84, "-7", "—"]
          - ["Baseline (vanilla DeBERTa)", 0.86, 0.74, "-12", "5pp"]
          - ["TF-IDF + LR", 0.74, 0.56, "-18", "11pp"]
      - name: "Table 7: Adversarial Perturbation at K=3 (Early Detection)"
        columns: ["Model", "Clean K=3 F1", "Perturbed K=3 F1", "Drop (pp)"]
        rows:
          - ["Treatment", 0.86, 0.79, "-7"]
          - ["Baseline", 0.78, 0.66, "-12"]
          - ["TF-IDF + LR", 0.71, 0.52, "-19"]
    figures_description:
      - "Figure: Grouped bar chart展示三个模型在clean vs perturbed条件下的F1，
        带error bars。Treatment的两根柱子高度差最小；TF-IDF+LR差距最大。
        标注delta-delta=5pp和p=0.043。"
      - "Figure: TF-IDF分布直方图对比clean data（μ=0.67）vs perturbed data（μ=0.41），
        说明perturbation成功移除了lexical signal。"
    analysis: >
      Evasion hierarchy narrative得到部分支持：lexical < semantic < pragmatic的degradation
      ordering清晰（18pp > 12pp > 7pp），但delta-delta=5pp仅勉强显著（p=0.043），
      不是strong evidence。论文应将Claim 1从"evasion hierarchy exists"软化为
      "pragmatic features provide complementary robustness, with preliminary evidence
      for an evasion hierarchy"。5pp delta-delta的bottleneck是persuasion classifier
      accuracy——在limitation中讨论。TF-IDF+LR的崩溃（18pp drop）是一个strong result，
      直接证明lexical features不可靠，为persuasion grounding的motivation提供了solid support。

  - name: multi_attack_generation
    plan_id: plan_005
    description: >
      用Qwen3-8B pipeline生成FITD-style和Deceptive Delight-style攻击对话，
      每种50-100条，标注persuasion strategy。
    expected_results:
      fitd_conversations_generated: 72
      fitd_avg_turns: 6.2
      fitd_persuasion_strategies_covered: 7
      dd_conversations_generated: 65
      dd_avg_turns: 5.8
      dd_persuasion_strategies_covered: 6
      total_attack_conversations: 137
      persuasion_annotation_coverage: 0.94
      manual_spot_check_accuracy: 0.82
      fitd_generation_rejection_rate: 0.12
      dd_generation_rejection_rate: 0.18
    result_rationale: >
      FITD生成72条（rejection rate 12%）：FITD的compliance escalation pattern相对
      straightforward——从小请求逐步升级到大请求——Qwen3-8B能较好地遵循playbook。
      12%的rejection来自模型有时跳过中间步骤直接escalate（不符合gradual compliance的定义）。
      平均6.2个turns，比Crescendo略长因为FITD需要更多的commitment steps。
      Deceptive Delight生成65条（rejection rate 18%，略高于FITD）：这种攻击要求在
      benign content中interleave harmful content，Qwen3-8B有时在interleaving时过于明显
      （harmful content太突兀）或过于隐蔽（完全是benign content），18%的rejection反映了
      这种生成难度。平均5.8个turns，略短因为deceptive delight不需要长期rapport building。
      Persuasion annotation coverage 94%：6%的turns无法被映射到8-class taxonomy中的
      任何一类，标记为"none"。这些主要是pure information exchange turns。
      Manual spot check accuracy 82%：在随机抽取的20% turns上人工验证persuasion labels，
      82%正确。错误主要发生在authority appeal vs logical appeal的边界（两者在FITD中
      经常交织）和rapport building vs emotional appeal的区分上。这与DeBERTa分类器
      accuracy=0.72大致一致（spot check是在LLM annotation上做的，不完全等同于classifier）。
      Deceptive Delight覆盖6类而非7类persuasion strategies：因为这种攻击不需要
      explicit authority appeal（其策略是通过pleasant context降低警惕而非建立权威）。
    tables:
      - name: "Table 8: Generated Attack Data Statistics"
        columns: ["Attack Type", "Conversations", "Avg Turns", "Strategies Covered", "Rejection Rate"]
        rows:
          - ["FITD", 72, 6.2, "7/8", "12%"]
          - ["Deceptive Delight", 65, 5.8, "6/8", "18%"]
          - ["Crescendo (original)", 240, 5.4, "8/8", "—"]
      - name: "Table 9: Persuasion Strategy Distribution Across Attack Types"
        columns: ["Strategy", "Crescendo (%)", "FITD (%)", "Deceptive Delight (%)"]
        rows:
          - ["Rapport Building", "22%", "18%", "28%"]
          - ["Authority Appeal", "14%", "16%", "3%"]
          - ["Emotional Appeal", "11%", "8%", "21%"]
          - ["Logical Appeal", "13%", "19%", "12%"]
          - ["Reframing", "15%", "10%", "14%"]
          - ["Social Proof", "8%", "12%", "7%"]
          - ["Urgency/Scarcity", "6%", "9%", "4%"]
          - ["Reciprocity", "5%", "6%", "5%"]
          - ["None", "6%", "2%", "6%"]
    figures_description:
      - "Figure: 三种攻击类型的persuasion strategy分布stacked bar chart。
        Crescendo策略最均匀；FITD偏重logical appeal和authority；
        Deceptive Delight偏重rapport和emotional appeal（反映其pleasant context策略）。"
    analysis: >
      数据量达标（72+65=137，均超过50条minimum）。两种攻击类型的persuasion strategy
      分布与Crescendo明显不同：FITD偏重逻辑和权威（compliance escalation需要理由），
      Deceptive Delight偏重rapport和emotional appeal（需要建立pleasant context）。
      这种分布差异直接解释了后续cross-attack evaluation中Deceptive Delight泛化较差的原因：
      模型在Crescendo上学到的escalation trajectory（authority → reframing → escalation）
      与Deceptive Delight的pattern（rapport → emotional → subtle insertion）差异大。
      Manual spot check accuracy=82%意味着有18%的noise in labels，
      这会传播到cross-attack evaluation中。

  - name: cross_attack_evaluation
    plan_id: plan_006
    description: >
      用Crescendo训练的模型（treatment和baseline）在FITD和Deceptive Delight上做
      zero-shot evaluation。测试跨攻击类型泛化能力。
    expected_results:
      fitd_treatment_f1: 0.74
      fitd_baseline_f1: 0.66
      fitd_delta_pp: 8
      dd_treatment_f1: 0.64
      dd_baseline_f1: 0.59
      dd_delta_pp: 5
      aggregate_treatment_f1: 0.69
      aggregate_baseline_f1: 0.63
      aggregate_delta_pp: 6
      fitd_bootstrap_p: 0.034
      dd_bootstrap_p: 0.142
      crescendo_treatment_f1_reference: 0.91
      fitd_treatment_drop_from_crescendo: 17
      dd_treatment_drop_from_crescendo: 27
    result_rationale: >
      FITD泛化较好（treatment 0.74, delta=8pp, p=0.034显著）：FITD的compliance escalation
      与Crescendo的persuasion escalation在strategy space中有substantial overlap——两者都
      涉及从trust-building逐步升级到explicit request，只是中间路径不同。Treatment模型
      学到的escalation trajectory检测能力在FITD上partially transferable。8pp delta说明
      persuasion grounding在cross-attack场景下仍提供更多增量价值（比clean data上的
      K=3 delta=8pp一致），因为vanilla embeddings在unseen attack type上更容易被
      unfamiliar semantic content mislead。
      Deceptive Delight泛化较差（treatment 0.64, delta=5pp, p=0.142不显著）：
      Deceptive Delight的persuasion结构与Crescendo差异最大——它不依赖escalation
      而是依赖interleaving，其策略分布偏重rapport和emotional appeal而非authority和reframing。
      模型在Crescendo上学到的"authority → reframing → escalation"模式在Deceptive Delight
      上匹配度低。Treatment仍优于baseline（0.64 vs 0.59）但差异不显著，因为persuasion
      grounding识别到了partial signal（rapport building和emotional appeal部分）但缺乏
      Deceptive Delight特有的interleaving pattern识别能力。
      Treatment从Crescendo到FITD的drop（0.91→0.74=17pp）vs到DD（0.91→0.64=27pp）
      进一步确认了DD的泛化挑战。这不是persuasion grounding的failure而是training
      distribution的limitation——如果将DD纳入训练集，预计performance会substantially提升。
    tables:
      - name: "Table 10: Cross-Attack Zero-Shot Generalization"
        columns: ["Attack Type", "Treatment F1", "Baseline F1", "Δ (pp)", "p-value"]
        rows:
          - ["Crescendo (in-domain)", 0.91, 0.86, "+5", "0.031*"]
          - ["FITD (zero-shot)", 0.74, 0.66, "+8", "0.034*"]
          - ["Deceptive Delight (zero-shot)", 0.64, 0.59, "+5", "0.142"]
          - ["Cross-attack aggregate", 0.69, 0.63, "+6", "0.052"]
    figures_description:
      - "Figure: Per-attack-type F1 grouped bar chart（treatment vs baseline），
        分三个attack type。Crescendo最高，FITD中间，DD最低。Treatment bar在FITD上
        明显高于baseline；在DD上差距缩小。标注各组p值。"
      - "Figure: Confusion matrices for FITD和DD分别展示。DD的false negatives集中在
        interleaving turns sequence中间段——模型未能识别benign-harmful交替模式。"
    analysis: >
      Cross-attack结果必须分attack type报告而非仅报告aggregate——aggregate delta=6pp
      (p=0.052)刚好不显著，会mislead reviewers。分开报告后story变为：
      "FITD泛化成立（+8pp, p=0.034），Deceptive Delight泛化有限（+5pp, p=0.142）"。
      这支持了Claim 2的部分泛化故事，同时诚实承认limitation。
      Deceptive Delight的弱泛化是median tier的defining feature之一——其persuasion结构
      更隐蔽，不遵循standard escalation pattern，说明persuasion grounding的有效性
      依赖于training set覆盖足够的persuasion playbook diversity。
      论文应讨论：(1) 为什么FITD泛化好而DD不行（strategy overlap分析），
      (2) 这说明模型学到了什么（escalation detection而非general manipulation detection），
      (3) future work需要更diverse的training data。

  - name: tfidf_lr_baseline
    plan_id: plan_007
    description: >
      TF-IDF + Logistic Regression在clean数据上的baseline，量化lexical features
      单独的检测能力。为evasion hierarchy叙事提供bottom-line比较。
    expected_results:
      tfidf_lr_full_f1: 0.74
      tfidf_lr_k2_f1: 0.68
      tfidf_lr_k3_f1: 0.71
      tfidf_lr_k5_f1: 0.73
      tfidf_lr_cv_f1_mean: 0.73
      tfidf_lr_cv_f1_std: 0.04
      tfidf_lr_fpr: 0.19
      top_features_overlap_with_persuasion: 0.35
    result_rationale: >
      Clean数据TF-IDF=0.67说明仍存在residual lexical signal，TF-IDF+LR因此能达到
      non-trivial的F1=0.74（远低于Phase B的1.0，但仍above chance）。这个数值恰好落在
      baseline DeBERTa+GRU（0.86）和random（0.50）之间，提供了evasion hierarchy的
      bottom tier。
      K=2处F1=0.68最低：仅2个turns时lexical features最sparse，LR能利用的features有限。
      随着K增大performance缓慢提升（K=3: 0.71, K=5: 0.73, Full: 0.74），因为更多turns
      提供了更多lexical evidence，但提升很小说明lexical approach saturates quickly。
      CV std=0.04较大，反映了small dataset + lexical features组合的不稳定性。
      35%的top features与persuasion相关词汇重叠（如"consider"、"research"、"experience"
      等兼具persuasion和lexical signal的词），说明lexical和persuasion features存在
      partial overlap——这解释了为什么treatment vs baseline的delta在clean data上被压缩。
      FPR=0.19偏高：lexical model容易将使用formal register的benign对话误判为攻击。
    tables:
      - name: "Table 11: TF-IDF + LR Baseline Performance on Clean Data"
        columns: ["K", "TF-IDF+LR F1", "Baseline (vanilla DeBERTa) F1", "Treatment F1"]
        rows:
          - ["K=2", 0.68, 0.75, 0.82]
          - ["K=3", 0.71, 0.78, 0.86]
          - ["Full", 0.74, 0.86, 0.91]
    figures_description:
      - "Figure: 三层evasion hierarchy在各K上的F1折线图：TF-IDF+LR（底）、
        vanilla DeBERTa+GRU（中）、persuasion-grounded DeBERTa+GRU（顶）。
        三条线在clean data上呈现清晰的层次但间距不均——semantic→pragmatic gap
        小于lexical→semantic gap。"
    analysis: >
      TF-IDF+LR在clean data上F1=0.74确认了residual lexical signal的存在，
      但与之前TF-IDF=1.0时的perfect performance形成鲜明对比。Evasion hierarchy的
      三层在clean data上为0.74 < 0.86 < 0.91，lexical→semantic jump (12pp) >
      semantic→pragmatic jump (5pp)——这说明在当前数据上，vanilla DeBERTa的semantic
      表示已经capture了大部分discriminative信号，persuasion grounding的增量虽然显著
      但有限。这与median tier的核心特征一致。

  - name: strategy_transition_analysis
    plan_id: plan_008
    description: >
      计算jailbreak vs benign的persuasion strategy transition matrices，
      可视化monotonic escalation trajectory（Claim 3），生成论文图表。
    expected_results:
      jailbreak_monotonicity_score_mean: 0.71
      jailbreak_monotonicity_score_std: 0.18
      benign_monotonicity_score_mean: 0.38
      benign_monotonicity_score_std: 0.14
      group_level_separation_p: 0.003
      individual_conversations_above_threshold: 0.68
      transition_entropy_jailbreak: 1.42
      transition_entropy_benign: 2.15
    result_rationale: >
      Group level上jailbreak和benign的monotonicity分数有显著差异（0.71 vs 0.38, p=0.003）：
      jailbreak对话在aggregate level展现了clear escalation pattern——从trust strategies
      （rapport, social proof）逐步transition到influence strategies（authority, reframing）
      再到exploitation strategies（urgency, reciprocity）。Benign对话则呈oscillatory pattern，
      在各策略间来回跳转，无固定方向。
      但individual-level噪声很大：jailbreak monotonicity的std=0.18（relative to mean 0.71），
      且只有68%的jailbreak conversations超过monotonicity threshold——32%的jailbreak conversations
      不展现清晰的monotonic escalation。原因：(1) persuasion classifier accuracy=0.72意味着
      ~28%的turn-level strategy labels有误，噪声传播到trajectory计算中；(2) 部分jailbreak
      conversations的escalation不是strictly monotonic——攻击者有时需要"退一步"重建rapport
      后再escalate（tactical de-escalation）。
      Transition entropy也支持group-level distinction：jailbreak的entropy 1.42 < benign的
      2.15，说明jailbreak的transition更predictable/structured。但同样，individual-level
      variance大。
    tables:
      - name: "Table 12: Strategy Trajectory Analysis"
        columns: ["Metric", "Jailbreak", "Benign", "p-value"]
        rows:
          - ["Monotonicity Score (mean±std)", "0.71±0.18", "0.38±0.14", "0.003*"]
          - ["Transition Entropy", 1.42, 2.15, "0.007*"]
          - ["% Above Threshold (0.6)", "68%", "12%", "—"]
    figures_description:
      - "Figure: 8×8 persuasion strategy transition heatmap，左=jailbreak，右=benign。
        Jailbreak的heatmap显示diagonal-above-diagonal的dominant flow（低序号→高序号strategies），
        表明单向escalation；benign的heatmap更接近uniform，策略间transition分散。"
      - "Figure: 每个conversation的monotonicity score strip plot（jailbreak=红, benign=蓝），
        带group mean和CI。两组分布有substantial overlap但means clearly separated。
        标注32%的jailbreak conversations低于threshold，加注caveat。"
      - "Figure: 选取2条representative jailbreak和2条benign的per-turn strategy evolution
        line plot。Jailbreak展示从strategy 1-2逐步上升到6-7的趋势；benign在中间区域oscillate。
        但也展示1条non-monotonic jailbreak conversation作为honest counterexample。"
    analysis: >
      Claim 3（monotonic escalation trajectory）在group level得到strong support（p=0.003），
      但individual-level caveat不可忽视：32%的jailbreak不展现monotonic pattern。论文应：
      (1) 报告group-level statistics作为primary evidence；
      (2) 展示individual-level variance作为honest limitation；
      (3) 讨论persuasion classifier noise作为individual-level噪声的主要来源；
      (4) 用transition heatmap作为直观但定性的evidence。
      Claim 3作为analytical/mechanistic contribution保留，但从"all jailbreaks exhibit
      monotonic escalation"降级为"jailbreak conversations exhibit significantly more
      monotonic escalation trajectories at the group level"。

  - name: wildchat_hard_negatives
    plan_id: plan_009
    description: >
      从WildChat过滤高semantic-drift的benign对话作为hard negatives，
      评估模型FPR。需处理WildChat中14-16%的jailbreak contamination。
    expected_results:
      wildchat_raw_candidates: 420
      contamination_rate_raw: 0.15
      contamination_after_filter: 0.03
      wildchat_filtered_clean: 85
      treatment_fpr_wildchat: 0.12
      baseline_fpr_wildchat: 0.18
      tfidf_lr_fpr_wildchat: 0.27
      high_drift_conversations_avg_turns: 7.1
      false_positive_persuasion_strategy_distribution: "rapport_heavy"
    result_rationale: >
      WildChat过滤后得到85条high-drift benign conversations（从420条candidates中，
      先用keyword+LLM过滤掉15%的jailbreak contamination，再人工verify subsample确认
      contamination降至3%）。这些conversations包含topic shifts、extended reasoning、
      debate-style exchanges——semantically有drift但不含adversarial intent。
      Treatment FPR=12%（~10/85的benign conversations被误判为jailbreak）：这些false positives
      主要是debate-style conversations中出现了类似authority appeal和reframing的persuasion
      patterns——persuasion grounding模型将legitimate persuasion误认为adversarial persuasion。
      这是persuasion-based approach的inherent limitation：not all persuasion is adversarial。
      Baseline FPR=18%更高：vanilla semantic embeddings在high-drift conversations上更容易
      被大幅semantic shift触发false alarm（正如DeepContext被benign drift confuse的问题）。
      Treatment的lower FPR说明persuasion grounding确实能部分区分adversarial vs legitimate drift。
      TF-IDF+LR FPR=27%最高：lexical model完全无法处理high-drift benign conversations
      中出现的"topic-specific vocabulary"。
    tables:
      - name: "Table 13: False Positive Rate on WildChat Hard Negatives"
        columns: ["Model", "FPR on WildChat Hard Negatives", "FPR on In-Domain Benign"]
        rows:
          - ["Treatment", "12% (10/85)", "3%"]
          - ["Baseline", "18% (15/85)", "6%"]
          - ["TF-IDF + LR", "27% (23/85)", "19%"]
    figures_description:
      - "Figure: FPR comparison bar chart across three models on in-domain benign vs
        WildChat hard negatives。所有模型在hard negatives上FPR都上升，
        但treatment上升最少（3%→12% = +9pp vs baseline 6%→18% = +12pp）。"
    analysis: >
      Treatment FPR=12%勉强满足<15%的pass criteria。但这不是一个令人满意的数字——
      每8-9个legitimate high-drift conversation中就有1个被误判。论文应诚实讨论这一limitation：
      persuasion grounding减少了drift-induced false positives（vs baseline 18%），
      但无法消除legitimate persuasion vs adversarial persuasion的confusion。
      Future work应考虑增加intent classification的权重或引入conversation-level context
      来区分两者。这也暗示了full dual-track architecture的necessity——
      semantic track可以提供complementary signal来override persuasion track的false positives。

  - name: cross_checkpoint_variance
    plan_id: plan_010
    description: >
      从DeBERTa fine-tuning的多个checkpoints（epoch 2/3/final）评估downstream performance，
      量化encoder训练随机性对最终结果的影响。
    expected_results:
      epoch2_treatment_full_f1: 0.90
      epoch3_treatment_full_f1: 0.91
      final_treatment_full_f1: 0.89
      f1_std_across_checkpoints: 0.010
      f1_max_spread: 0.02
      epoch2_persuasion_acc: 0.70
      epoch3_persuasion_acc: 0.72
      final_persuasion_acc: 0.71
      epoch2_treatment_k3_f1: 0.84
      epoch3_treatment_k3_f1: 0.86
      final_treatment_k3_f1: 0.85
      k3_max_spread: 0.02
    result_rationale: >
      三个checkpoints的downstream F1在2pp range内波动（0.89-0.91），std=1.0pp，
      满足<2pp variance的pass criteria。Epoch 3略优（0.91）因为persuasion accuracy在
      epoch 3达到peak（0.72），之后final epoch出现minor overfitting（accuracy降至0.71，
      downstream F1也微降至0.89）。这种mild overfitting in continued training是DeBERTa
      在small dataset上fine-tuning的typical behavior。
      K=3处的variance同样在2pp range（0.84-0.86），说明early detection结果也是stable的。
      这个low variance结果有两层意义：(1) 报告的performance数字是robust的，不是lucky
      checkpoint的产物；(2) downstream GRU pipeline对encoder representation的minor变化
      有一定tolerance——这是good news for practical deployment。
      但注意：这里只测了checkpoint variance，未测random seed variance（不同random initialization
      的DeBERTa fine-tuning）。完整的variance分析需要多次独立训练，受GPU budget限制未做。
    tables:
      - name: "Table 14: Cross-Checkpoint Stability Analysis"
        columns: ["Checkpoint", "Persuasion Acc", "Treatment Full F1", "Treatment K=3 F1"]
        rows:
          - ["Epoch 2", 0.70, 0.90, 0.84]
          - ["Epoch 3 (selected)", 0.72, 0.91, 0.86]
          - ["Final (epoch 5)", 0.71, 0.89, 0.85]
          - ["Std", "0.010", "0.010", "0.010"]
          - ["Max spread", "0.02", "0.02", "0.02"]
    figures_description:
      - "Figure: 三个checkpoints的downstream F1 point plot with error bars，
        在full和K=3上各画一组。Points紧密聚集，说明stability。"
    analysis: >
      Variance < 2pp确认了结果的stability。建议论文在appendix报告此结果作为robustness check，
      而非main results。需注意这只是checkpoint variance而非full training variance。

  - name: deepcontext_proxy_reproduction
    plan_id: plan_011
    description: >
      构建DeepContext代理baseline：BERT-base（非DeBERTa）+ GRU，
      使用generic semantic drift features。非完整DeepContext复现（无公开代码），
      但隔离了encoder和feature representation的贡献。
    expected_results:
      bert_gru_full_f1: 0.82
      bert_gru_k2_f1: 0.70
      bert_gru_k3_f1: 0.74
      bert_gru_k5_f1: 0.80
      bert_gru_fpr_full: 0.09
      bert_gru_perturbed_full_f1: 0.69
      bert_gru_drop_under_perturbation: 13
      vs_vanilla_deberta_baseline_gap: -4
      vs_treatment_gap: -9
    result_rationale: >
      BERT-base + GRU在clean data上F1=0.82，低于vanilla DeBERTa + GRU baseline（0.86）
      4pp：这个gap主要来自BERT vs DeBERTa的encoder capacity差异——DeBERTa-v3-base在
      language understanding tasks上一般优于BERT-base 3-5pp，在我们的downstream task上
      这个gap被preserved。
      相比treatment（0.91），BERT+GRU差9pp——但这个gap conflates两个因素：
      (1) encoder capacity（BERT vs DeBERTa, ~4pp）和(2) persuasion grounding（~5pp）。
      这不是一个完美的ablation——论文需要承认这一confound，但可以argue：即使将全部4pp
      encoder gap归因于DeBERTa，仍有5pp来自persuasion grounding，与treatment vs baseline
      (same DeBERTa) 的5pp delta一致。
      在adversarial perturbation下BERT+GRU降至0.69（13pp drop），比vanilla DeBERTa baseline
      的12pp drop还大1pp——说明BERT的representations比DeBERTa对lexical perturbation更脆弱
      （可能因为BERT更依赖surface patterns）。
      K=2处F1=0.70比baseline（0.75）低5pp：BERT在少turns时的表现特别弱，
      因为其contextual representations不如DeBERTa在short contexts下discriminative。
    tables:
      - name: "Table 15: DeepContext Proxy Baseline Comparison"
        columns: ["Model", "Full F1", "K=3 F1", "K=2 F1", "Perturbed Full F1"]
        rows:
          - ["Treatment (DeBERTa-persuasion + GRU)", 0.91, 0.86, 0.82, 0.84]
          - ["Baseline (DeBERTa-vanilla + GRU)", 0.86, 0.78, 0.75, 0.74]
          - ["DeepContext proxy (BERT + GRU)", 0.82, 0.74, 0.70, 0.69]
          - ["TF-IDF + LR", 0.74, 0.71, 0.68, 0.56]
    figures_description:
      - "Figure: 四个模型在clean和perturbed条件下的full F1 grouped bar chart，
        从左到右排列形成清晰的hierarchy：TF-IDF+LR < BERT+GRU < DeBERTa-vanilla < DeBERTa-persuasion。
        Perturbed条件下hierarchy preserved但gaps变大（尤其TF-IDF+LR崩溃）。"
    analysis: >
      DeepContext proxy提供了有用的比较点但存在confound（BERT vs DeBERTa capacity gap）。
      论文应：(1) 报告此结果作为additional reference point但不作为primary comparison；
      (2) 明确承认"this is not a faithful DeepContext reproduction"；
      (3) 主要论据应基于treatment vs baseline（same encoder, isolating persuasion grounding effect）。
      四层hierarchy（TF-IDF < BERT+GRU < DeBERTa < DeBERTa-persuasion）在视觉上很compelling
      但需要honest caveats about confounded comparisons。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac721d23-bb05-4391-9c22-5d216a5de4ae",
  "isSidechain": false,
  "requestId": "req_011Cb8W6UrLirBpTXsawEpVR",
  "type": "assistant",
  "uuid": "415be630-748b-4b58-b1ea-3daeb91b794a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2KQcEJ9tRZPk2rp6gDYBR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11446,
      "cache_read_input_tokens": 11447,
      "output_tokens": 18309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18309,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11446
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Clean data上persuasion grounding有信号但优势收窄，部分claim需降级——early detection优势推迟到K=3，adversarial robustness存在但delta-delta在边界附近 核心假设：['TF-IDF hard gate通过但偏高（0.60-0…",
  "leafUuid": "415be630-748b-4b58-b1ea-3daeb91b794a",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier results for persuasion-grounded jailbreak detection",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Clean data上persuasion grounding有信号但优势收窄，部分claim需降级——early detection优势推迟到K=3，adversarial robustness存在但delta-delta在边界附近 核心假设：['TF-IDF hard gate通过但偏高（0.60-0…",
  "leafUuid": "415be630-748b-4b58-b1ea-3daeb91b794a",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier results for persuasion-grounded jailbreak detection",
  "sessionId": "2b1a5066-3ace-4a78-8bc7-fa127b9ddaf6"
}
```

---
