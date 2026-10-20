# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：KL优势收窄为效率等价——BCE+compensation达到与KL-only相近的质量，但KL无需compensation开销即可达到 核心假设：

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/5b0b565b-ac91-462a-b352-39429cf52d55.jsonl`
- **Structured JSON:** [`d4177f3a9d00be7fe581.json`](../../sessions/d4/d4177f3a9d00be7fe581.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T17:01:21.027Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T17:01:21.027Z",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：KL优势收窄为效率等价——BCE+compensation达到与KL-only相近的质量，但KL无需compensation开销即可达到\n核心假设：['KL-only PPL稳定在9.0-10.5但seed方差增大（std 0.3-0.8）', 'BCE+compensation有效收敛到10-13 PPL，compensation网络确实有用', 'SPON + KL部分可加（interaction residual 10-30%），组合收益存在但不clean', 'KL-BCE delta随sparsity有上升趋势但fit有噪声（R² 0.80-0.95），不足以声称精确quadratic law', 'Mistral同方向但相对差距更小', 'STE baseline部分复现KL优势（Gumbel贡献约30%的gain，loss和relaxation都重要）']\n关键指标范围：{'kl_only_wikitext2_ppl': [9.0, 10.5], 'kl_only_ppl_std': [0.3, 0.8], 'bce_comp_wikitext2_ppl': [10.0, 13.0], 'spon_kl_wikitext2_ppl': [8.5, 9.5], 'kl_vs_bce_comp_ppl_gap': [0.0, 3.0], 'downstream_acc_drop_vs_dense_pct': [2, 5], 's2_scaling_r2': [0.8, 0.95], 'mistral_kl_ppl_increase_vs_dense_pct': [50, 90]}\n叙事方向：Claim 1 从'KL categorically better'调整为'KL eliminates compensation overhead at quality parity'——核心贡献变成效率：同等质量下，推理pipeline更简单，省256MB参数。Claim 2 弱化为'empirically observed partial additivity'，需补充interaction term分析作为honest characterization。Claim 3 降级为'consistent empirical trend'而非precise quantitative law，放appendix展示fit。Paper结构重心转向taxonomy + systematic ablation的方法论贡献，efficiency作为practical payoff。仍是solid EMNLP contribution，但需要更careful的claims wording。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: distill_sparse_swiglu\nfocus: MVP showed massive KL vs BCE gap (12.52 vs 44.05 PPL). Key uncertainty: will BCE+compensation close this gap? If yes, headline shifts to \"KL eliminates compensation overhead\" rather than \"KL is categorically better\". Also: seed s456 is outlier (13.58 vs 12.08/11.91), variance needs attention.\n\n## paper_framing.md\n\n# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)\n\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\n\n3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\n\n- **Our framing / headline question**: \"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\n\n- **Headline result template**: \"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\n\n2. **\"KL wins only because more compute\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\n\n5. **\"Effect size may not hold on downstream tasks\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:\n    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline\n    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds\n    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and\n    BCE-only 3 seeds (mvp_bce_s42/s123/s456).\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_ids:\n  - mvp_kl_norm_v2_s42\n  - mvp_kl_norm_v2_s123\n  - mvp_kl_norm_v2_s456\n  - mvp_bce_s42\n  - mvp_bce_s123\n  - mvp_bce_s456\n  remaining_runs:\n  - KL-only 2 additional seeds (s0, s1) for 5-seed headline\n  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)\n  - KL+comp 3 seeds (s42, s123, s456)\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).\n    Isolates whether KL advantage comes from loss function or relaxation method. 3\n    seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs\n    (KL requires full forward pass for output logits, BCE can use cached targets).\n    Report per-step FLOPs and total training time for both. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL\n    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,\n    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'SPON + KL predictor composition experiment. Apply SPON bias correction\n    AND KL contextual prediction simultaneously. Output-space linearity test: ||Delta_logits(s+c)\n    - Delta_logits(s) - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality\n    analysis. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  - plan_004\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:\n    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),\n    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free\n    < static-learned < contextual-learned.\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2\n    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor\n    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto\n    frontier plot.\n\n    '\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  - plan_004\n  - plan_005\n  - plan_006\n  status: planned\n- id: plan_008\n  claim: 3\n  description: '7-level sparsity sweep (30/35/40/45/50/55/60%): KL-only vs BCE-only.\n    Test quantitative prediction: KL-BCE delta ~ s^2. 1 seed per level (sweep analysis,\n    not headline). 50% data point reused from plan_001. Taylor expansion accuracy\n    test at each level.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%\n    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds\n    each condition.\n\n    '\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  status: planned\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions\n    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:\n    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization\n    beyond short training sequences.\n\n    '\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 2\n  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8\n    categories. All conditions. Tests instruction-following quality under sparsity.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative\n    task types. Fine-grained capability diagnostics complementing LongBench.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_total_loss: 3.3438\n    final_kl_loss: 3.2969\n    final_reg_loss: 0.05\n    final_sparsity: 0\n    steps: 1000\n    tau_final: 0.1\n    wikitext2_ppl_dense: 6.12\n    wikitext2_ppl_sparse: 455.93\n    wikitext2_ppl_increase_pct: 7349\n    model_level_sparsity: 0.372\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\n- exp_id: mvp_kl_s123\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_kl_s456\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_bce_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 27.9603\n    teal_sparse_ppl: 44.537\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 628\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_bce_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.3817\n    teal_sparse_ppl: 44.5864\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 629\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_bce_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.1437\n    teal_sparse_ppl: 43.033\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 603.3\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: kl_lagrangian_quicktest\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_kl_loss: 418\n    final_constraint_loss: 1.211\n    final_sparsity: 0.141\n    final_lambda: 5.06\n    steps: 200\n    sparsity_trajectory:\n    - 0.406\n    - 0.387\n    - 0.289\n    - 0.168\n    - 0.141\n- exp_id: kl_lagrangian_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_normalized_quicktest\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step1_kl: 1.18\n    step200_kl: 0.641\n    step200_sparsity: 0.504\n    final_lambda: 8\n    sparsity_converged_step: 80\n    sparsity_trajectory:\n    - 0.406\n    - 0.398\n    - 0.398\n    - 0.457\n    - 0.52\n    - 0.506\n    - 0.504\n    - 0.504\n    lambda_trajectory:\n    - 1\n    - 2\n    - 4\n    - 8\n    - 8\n    - 8\n    - 8\n    - 8\n- exp_id: mvp_kl_norm_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_norm_v3_quicktest\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    step1_kl_raw: 1.1797\n    step1_kl_norm: 1.1797\n    step1_sparsity: 0.406\n    step1_lambda: 2\n    step50_kl_raw: 0.7344\n    step50_kl_norm: 0.7344\n    step50_sparsity: 0.514\n    step50_lambda: 1.95\n    step100_kl_raw: 0.625\n    step100_kl_norm: 0.625\n    step100_sparsity: 0.496\n    step100_lambda: 1000\n    step150_kl_raw: 0.5703\n    step150_kl_norm: 0.5703\n    step150_sparsity: 0.48\n    step150_lambda: 1000\n    step200_kl_raw: 0.6836\n    step200_kl_norm: 0.6836\n    step200_sparsity: 0.477\n    step200_lambda: 1000\n    step200_constraint: 0.01178\n    kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)\n    sparsity_range: 0.477-0.514 after step 50\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\n- exp_id: mvp_kl_norm_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2142\n    teal_sparse_ppl: 12.0776\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 97.4\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_kl_norm_v2_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2474\n    teal_sparse_ppl: 11.9128\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 94.7\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_kl_norm_v2_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.14\n    teal_sparse_ppl: 13.58\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 121.9\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T17:01:21.030Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T17:01:21.030Z",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T17:01:21.049Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：KL优势收窄为效率等价——BCE+compensation达到与KL-only相近的质量，但KL无需compensation开销即可达到
核心假设：['KL-only PPL稳定在9.0-10.5但seed方差增大（std 0.3-0.8）', 'BCE+compensation有效收敛到10-13 PPL，compensation网络确实有用', 'SPON + KL部分可加（interaction residual 10-30%），组合收益存在但不clean', 'KL-BCE delta随sparsity有上升趋势但fit有噪声（R² 0.80-0.95），不足以声称精确quadratic law', 'Mistral同方向但相对差距更小', 'STE baseline部分复现KL优势（Gumbel贡献约30%的gain，loss和relaxation都重要）']
关键指标范围：{'kl_only_wikitext2_ppl': [9.0, 10.5], 'kl_only_ppl_std': [0.3, 0.8], 'bce_comp_wikitext2_ppl': [10.0, 13.0], 'spon_kl_wikitext2_ppl': [8.5, 9.5], 'kl_vs_bce_comp_ppl_gap': [0.0, 3.0], 'downstream_acc_drop_vs_dense_pct': [2, 5], 's2_scaling_r2': [0.8, 0.95], 'mistral_kl_ppl_increase_vs_dense_pct': [50, 90]}
叙事方向：Claim 1 从'KL categorically better'调整为'KL eliminates compensation overhead at quality parity'——核心贡献变成效率：同等质量下，推理pipeline更简单，省256MB参数。Claim 2 弱化为'empirically observed partial additivity'，需补充interaction term分析作为honest characterization。Claim 3 降级为'consistent empirical trend'而非precise quantitative law，放appendix展示fit。Paper结构重心转向taxonomy + systematic ablation的方法论贡献，efficiency作为practical payoff。仍是solid EMNLP contribution，但需要更careful的claims wording。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: distill_sparse_swiglu
focus: MVP showed massive KL vs BCE gap (12.52 vs 44.05 PPL). Key uncertainty: will BCE+compensation close this gap? If yes, headline shifts to "KL eliminates compensation overhead" rather than "KL is categorically better". Also: seed s456 is outlier (13.58 vs 12.08/11.91), variance needs attention.

## paper_framing.md

# Paper Framing — distill_sparse_swiglu

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 2026 cycle)
- Deadline: 2026-05-25 (ARR submission)
- Track: Efficient Methods for NLP

## Core Claims

1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)

2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.

3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.

## Story Spine

- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).

- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.

- **Our framing / headline question**: "Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.

- **Headline result template**: "On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline."

## Two-Dimensional Taxonomy (Conceptual Contribution)

|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
|--------------------------|:-----------------:|:-------------------:|:-------------:|
| Static                   | —                 | —                   | SPON          |
| Per-layer                | —                 | ShadowLLM           | —             |
| Per-token contextual     | FastForward       | —                   | **Ours**      |

Positions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.

## Anticipated Reviewer Concerns

1. **"Incremental / no new algorithm"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.

2. **"KL wins only because more compute"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.

3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.

4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).

5. **"Effect size may not hold on downstream tasks"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.

## Venue Fit
- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation
- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue
- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:
    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline
    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds
    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and
    BCE-only 3 seeds (mvp_bce_s42/s123/s456).

    '
  priority: P0
  gpu_budget_hours: 48
  deps: []
  registry_ids:
  - mvp_kl_norm_v2_s42
  - mvp_kl_norm_v2_s123
  - mvp_kl_norm_v2_s456
  - mvp_bce_s42
  - mvp_bce_s123
  - mvp_bce_s456
  remaining_runs:
  - KL-only 2 additional seeds (s0, s1) for 5-seed headline
  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)
  - KL+comp 3 seeds (s42, s123, s456)
  status: planned
- id: plan_002
  claim: 1
  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).
    Isolates whether KL advantage comes from loss function or relaxation method. 3
    seeds.

    '
  priority: P0
  gpu_budget_hours: 10
  deps:
  - plan_001
  status: planned
- id: plan_003
  claim: 1
  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs
    (KL requires full forward pass for output logits, BCE can use cached targets).
    Report per-step FLOPs and total training time for both. 3 seeds.

    '
  priority: P0
  gpu_budget_hours: 10
  deps:
  - plan_001
  status: planned
- id: plan_004
  claim: 2
  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL
    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,
    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.

    '
  priority: P0
  gpu_budget_hours: 4
  deps: []
  status: planned
- id: plan_005
  claim: 2
  description: 'SPON + KL predictor composition experiment. Apply SPON bias correction
    AND KL contextual prediction simultaneously. Output-space linearity test: ||Delta_logits(s+c)
    - Delta_logits(s) - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality
    analysis. 3 seeds.

    '
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_001
  - plan_004
  status: planned
- id: plan_006
  claim: 1
  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:
    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),
    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free
    < static-learned < contextual-learned.

    '
  priority: P0
  gpu_budget_hours: 6
  deps: []
  status: planned
- id: plan_007
  claim:
  - 1
  - 2
  - 3
  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2
    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor
    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto
    frontier plot.

    '
  priority: P0
  gpu_budget_hours: 24
  deps:
  - plan_001
  - plan_004
  - plan_005
  - plan_006
  status: planned
- id: plan_008
  claim: 3
  description: '7-level sparsity sweep (30/35/40/45/50/55/60%): KL-only vs BCE-only.
    Test quantitative prediction: KL-BCE delta ~ s^2. 1 seed per level (sweep analysis,
    not headline). 50% data point reused from plan_001. Taylor expansion accuracy
    test at each level.

    '
  priority: P1
  gpu_budget_hours: 30
  deps:
  - plan_001
  status: planned
- id: plan_009
  claim: 1
  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%
    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds
    each condition.

    '
  priority: P1
  gpu_budget_hours: 24
  deps:
  - plan_001
  status: planned
- id: plan_010
  claim:
  - 1
  - 2
  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions
    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:
    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization
    beyond short training sequences.

    '
  priority: P1
  gpu_budget_hours: 16
  deps:
  - plan_001
  - plan_005
  status: planned
- id: plan_011
  claim:
  - 1
  - 2
  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8
    categories. All conditions. Tests instruction-following quality under sparsity.

    '
  priority: P2
  gpu_budget_hours: 4
  deps:
  - plan_001
  - plan_005
  status: planned
- id: plan_012
  claim: 3
  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative
    task types. Fine-grained capability diagnostics complementing LongBench.

    '
  priority: P2
  gpu_budget_hours: 8
  deps:
  - plan_010
  status: planned


## registry (completed experiments)

- exp_id: mvp_kl_s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    final_total_loss: 3.3438
    final_kl_loss: 3.2969
    final_reg_loss: 0.05
    final_sparsity: 0
    steps: 1000
    tau_final: 0.1
    wikitext2_ppl_dense: 6.12
    wikitext2_ppl_sparse: 455.93
    wikitext2_ppl_increase_pct: 7349
    model_level_sparsity: 0.372
    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt
- exp_id: mvp_kl_s123
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: mvp_kl_s456
  name: ''
  status: QUEUED
  conclusion: killed
  metrics: {}
- exp_id: mvp_bce_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.1173
    predictor_hard_mask_ppl: 27.9603
    teal_sparse_ppl: 44.537
    model_level_sparsity: 0.4957
    ppl_increase_vs_true_dense_pct: 628
    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
    calibration_samples: 32
- exp_id: mvp_bce_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.1173
    predictor_hard_mask_ppl: 28.3817
    teal_sparse_ppl: 44.5864
    model_level_sparsity: 0.4957
    ppl_increase_vs_true_dense_pct: 629
    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
    calibration_samples: 32
- exp_id: mvp_bce_s456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.1173
    predictor_hard_mask_ppl: 28.1437
    teal_sparse_ppl: 43.033
    model_level_sparsity: 0.4957
    ppl_increase_vs_true_dense_pct: 603.3
    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
    calibration_samples: 32
- exp_id: kl_lagrangian_quicktest
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    final_kl_loss: 418
    final_constraint_loss: 1.211
    final_sparsity: 0.141
    final_lambda: 5.06
    steps: 200
    sparsity_trajectory:
    - 0.406
    - 0.387
    - 0.289
    - 0.168
    - 0.141
- exp_id: kl_lagrangian_v2
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: kl_normalized_quicktest
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    step1_kl: 1.18
    step200_kl: 0.641
    step200_sparsity: 0.504
    final_lambda: 8
    sparsity_converged_step: 80
    sparsity_trajectory:
    - 0.406
    - 0.398
    - 0.398
    - 0.457
    - 0.52
    - 0.506
    - 0.504
    - 0.504
    lambda_trajectory:
    - 1
    - 2
    - 4
    - 8
    - 8
    - 8
    - 8
    - 8
- exp_id: mvp_kl_norm_s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_kl_norm_s123
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_kl_norm_s456
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: kl_norm_v3_quicktest
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    step1_kl_raw: 1.1797
    step1_kl_norm: 1.1797
    step1_sparsity: 0.406
    step1_lambda: 2
    step50_kl_raw: 0.7344
    step50_kl_norm: 0.7344
    step50_sparsity: 0.514
    step50_lambda: 1.95
    step100_kl_raw: 0.625
    step100_kl_norm: 0.625
    step100_sparsity: 0.496
    step100_lambda: 1000
    step150_kl_raw: 0.5703
    step150_kl_norm: 0.5703
    step150_sparsity: 0.48
    step150_lambda: 1000
    step200_kl_raw: 0.6836
    step200_kl_norm: 0.6836
    step200_sparsity: 0.477
    step200_lambda: 1000
    step200_constraint: 0.01178
    kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)
    sparsity_range: 0.477-0.514 after step 50
    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt
- exp_id: mvp_kl_norm_v2_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.1173
    predictor_hard_mask_ppl: 9.2142
    teal_sparse_ppl: 12.0776
    model_level_sparsity: 0.4979
    ppl_increase_vs_true_dense_pct: 97.4
    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
    calibration_samples: 32
- exp_id: mvp_kl_norm_v2_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.1173
    predictor_hard_mask_ppl: 9.2474
    teal_sparse_ppl: 11.9128
    model_level_sparsity: 0.4979
    ppl_increase_vs_true_dense_pct: 94.7
    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
    calibration_samples: 32
- exp_id: mvp_kl_norm_v2_s456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.1173
    predictor_hard_mask_ppl: 9.14
    teal_sparse_ppl: 13.58
    model_level_sparsity: 0.498
    ppl_increase_vs_true_dense_pct: 121.9
    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a
    calibration_samples: 32

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
  "promptId": "5883a99d-ff13-4fe4-aede-ced2585ec8bc",
  "type": "user",
  "uuid": "d38f5943-765f-4d10-a0c2-9b15247624b1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T17:01:21.048Z_

```json
{
  "parentUuid": "d38f5943-765f-4d10-a0c2-9b15247624b1",
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
  "uuid": "e097bab3-36b4-4372-af6e-9562e682a4c4",
  "timestamp": "2026-05-15T17:01:21.048Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T17:01:21.048Z_

```json
{
  "parentUuid": "e097bab3-36b4-4372-af6e-9562e682a4c4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "242fd91e-cff2-4950-8046-7fccf752fb18",
  "timestamp": "2026-05-15T17:01:21.048Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：KL优势收窄为效率等价——BCE+compensation达到与KL-only相近的质量，但KL无需compensation开销即可达到 核心假设：['KL-only PPL稳定在9.0-10.5但seed方差增大（std 0.3-0.8）', 'BCE+compensation有效收敛到10-13 PP…",
  "leafUuid": "242fd91e-cff2-4950-8046-7fccf752fb18",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Experiment plan detailed predictions for median tier",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55"
}
```

---

### Assistant

_source line 8 · 2026-05-15T17:07:26.493Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all "planned" experiments in the experiment_plan, based on the "median" tier definition provided in Phase 1. I need to provide result_rationale for each prediction explaining why this result is expected under the median tier.

Let me carefully go through each planned experiment and generate predictions consistent with the median tier definition.

Key median tier parameters:
- KL-only PPL: 9.0-10.5, std 0.3-0.8
- BCE+compensation PPL: 10.0-13.0
- SPON+KL PPL: 8.5-9.5


- KL-BCE delta with sparsity shows trending but noisy patterns (R² 0.80-0.95)
- Mistral exhibits the same directional effects but with smaller relative gaps
- STE baseline partially reproduces the KL advantage, with Gumbel capturing roughly 30% of the gain
- Downstream accuracy drops 2-5% compared to dense models
- KL versus BCE+compensation gap ranges 0.0-3.0 PPL points
- SPON+KL interaction residuals account for 10-30% of variance

Now I'm looking at the existing KL-only data across three seeds, which averages around 9.20 with a standard deviation that aligns with the median tier expectations.

Looking at the full dataset, the KL results are remarkably consistent across seeds while BCE-only shows higher variance around 28.16 mean. The dense baseline sits at 6.1173, and TEAL varies more substantially depending on seed context. The initial three KL seeds cluster tightly, but adding two more seeds could shift the overall variance profile upward, especially if those new runs fall outside the current tight band. So the project context is flagging that seed s456 has an outlier TEAL sparse PPL of 13.58 compared to the other two seeds at 12.08 and 11.91. For the median tier hypothesis, I need KL-only PPL to show increased variance across 5 seeds—the standard deviation should jump from the current 0.056 to somewhere in the 0.3-0.8 range, which means the two new seeds will likely introduce higher values, possibly pushing one above 10.0. Now I'm working through the detailed predictions for each experiment condition, starting with the four-condition ablation and the additional KL-only seeds.

For the KL-only condition with the new seeds, I'm aiming for a 5-seed mean around 9.47 with std around 0.42 by adding seeds that push higher. For BCE+comp, the compensation mechanism should dramatically reduce the baseline BCE PPL from 28.16 down to the 10.0-13.0 range, so I'm projecting seeds around 10.8 to 12.1 with a mean near 11.4. The KL+comp condition starts from the KL-only baseline of 9.2 and I'm considering how compensation affects it.

Now I'm thinking through the STE baseline as an alternative to Gumbel—since Gumbel contributes roughly 30% of the improvement, STE should capture about 70% of the gap between the BCE-only baseline and the full KL+Gumbel result, which is roughly an 18.7 point difference in perplexity. L - BCE_PPL in terms of improvement from dense... hmm.

Actually, I think the key comparison is between KL+Gumbel versus KL+STE. The STE approach gets most of the way there, but Gumbel adds that extra ~30% boost. So the total gain from KL+Gumbel versus the BCE baseline can be split: 70% comes from the KL loss itself, and 30% comes from the Gumbel relaxation. Let me reframe this more clearly — the baseline is BCE with STE, and from there, the KL improvement is partially driven by the loss change and partially by the relaxation mechanism.

Looking at the actual numbers: if BCE gives us a PPL around 28.16 and KL+Gumbel gets us to 9.47, that's a delta of 18.7. If KL+STE captures 70% of that improvement, it should land around PPL 15, which makes sense since STE doesn't propagate gradients as cleanly through the binary mask. But wait, I need to reconsider whether the existing BCE baseline actually uses sigmoid thresholding or something else. I'm working through the math on how much the Gumbel-sigmoid contributes versus the KL loss itself. If Gumbel accounts for about 30% of the total improvement, then KL+STE should land around 15 PPL—roughly splitting the difference between the KL+Gumbel result and the BCE baseline. But I need to think more carefully about what exactly I'm measuring here. Now I'm working through the ablation study systematically, starting with the four-condition setup at 50% sparsity on Llama 3.1 8B. For the KL-only condition, I'm combining the three existing seed results with two new ones to get a five-seed average of 9.53 PPL, then calculating the standard deviation across those runs. Looking at the standard deviation for the BCE+comp results—the deviations cluster around 0.55, which is solid. For KL+comp, adding compensation on top doesn't seem to help much since KL already captures the joint interactions well, so the three seeds show a tighter mean of 9.06. The gap between KL-only and BCE+comp is about 2.05 PPL in KL's favor, which fits the expected range. Now I'm checking the STE baseline approach with KL+STE across 3 seeds, which gives around 14.5 PPL.

Looking at the actual STE results, they're clustering in the 14.3-15.1 range with a mean of 14.7. Comparing the gains: Gumbel gets us from 28.16 down to 9.53 (18.63 point improvement), while STE only reaches 14.7 (13.46 point improvement), meaning Gumbel contributes about 5.17 points or roughly 30% of the total gain. For the iso-compute BCE experiment, I'm extending the standard BCE training to match the FLOPs used by KL, which should help somewhat but probably won't close the full gap—maybe bringing it down to the 22-24 range.

The extended BCE results confirm this: the mean lands at 22.8, which shows the gap isn't just a compute artifact. Even with more training, BCE-only stays far from KL's 9.5. The median tier data shows that BCE with compensation converges to 10-13 PPL, but that's with the compensation mechanism—pure extended BCE training without it still leaves us stuck around 22-24.

Now I'm looking at SPON as another approach: learnable bias vectors combined with KL training should give a moderate boost since static correction can handle typical drift patterns, though it won't match contextual methods. I'd expect WikiText-2 PPL somewhere in the 14-16 range.

Actually, checking the benchmark results against published numbers—ARC-c at 42 versus dense's 53, ARC-e at 72 versus 80, and similar gaps across BoolQ, PIQA, and WinoGrande—SPON's input-independent bias correction at 50% sparsity can only partially address the average drift. The median tier suggests SPON combined with KL reaches 8.5-9.5 PPL, so SPON alone would be considerably weaker, probably around 15-18 PPL, with the KL predictor then layering on the contextual improvements.

But if KL-only is already at 9.53 PPL and SPON+KL lands at 9.05, that's just a modest gain, which means SPON is capturing some complementary signal about average drift that KL doesn't fully account for. Let me frame this as a correction model: dense baseline at 6.12, then SPON reduces the gap from there, and KL provides additional context-dependent refinement.

Wait, I'm getting confused about the baselines. TEAL sits around 12 PPL as a training-free pruning method, but SPON is showing 16.5 PPL, which would be worse. That doesn't align. I think I'm conflating different approaches here — SPON is a static bias correction method, not a pruning strategy like TEAL, so they're not directly comparable. Looking back at the taxonomy, SPON is listed as static with coupled KL, which suggests it's part of a broader framework rather than a standalone method.

The key insight is that SPON+KL combines static bias correction with contextual prediction — you apply the fixed per-layer bias adjustment first, then layer the KL predictor on top for dynamic per-token adjustments. The median tier results show about 10-30% interaction residual, meaning they don't compose perfectly additively, and the combined approach lands around 8.5-9.5 PPL. For SPON in isolation at 50% sparsity, I'd estimate somewhere in the 18-22 PPL range — a meaningful improvement over no correction, but still far from what the combined method achieves.

Looking at the actual plan_005 results, SPON+KL gives 8.85 PPL as the mean across three seeds with fairly tight variance, and the interaction residual sits right in that expected 10-30% band, suggesting the two mechanisms compose in a partially additive way rather than fully synergistic.

For plan_006, I need to establish where the training-free baselines fit. I'm seeing TEAL numbers from the existing registry around 12 PPL, which is puzzling because that would put it better than SPON's 17 PPL—that breaks the narrative hierarchy I was expecting. Let me check whether those TEAL values are actually from the same experimental setup or if they're coming from a different configuration.

Looking at the registry data more carefully, those teal_sparse_ppl entries are evaluated at 50% sparsity alongside the KL predictor runs, so they're not directly comparable to the dense baseline. The paper's framing about a 6+ point gap between training-free heuristics and dense (6.12 PPL) suggests TEAL should land around 12-13 PPL, which matches what I'm seeing. So the three-tier structure should work if I set SPON to outperform TEAL—maybe around 11-12 PPL for SPON to create that middle tier between the training-free methods and the contextual learners.

But wait, SPON as a static learned method sits awkwardly between training-free and contextual approaches. If TEAL is 12-13 and BCE+comp is 11.6, putting SPON at 10.5-12 makes it too close to BCE+comp narratively. The real distinction here isn't just about performance ordering—it's about the two-dimensional taxonomy where methods vary on whether they're static or contextual and how they couple losses. Let me think about what makes sense for the median case. I'm second-guessing whether SPON should really match BCE+comp in quality when it's just static bias vectors per layer, versus a contextual predictor with decomposed loss. Let me recalibrate — SPON probably belongs higher in the ranking, maybe around 13-14 PPL, but that creates a problem where it'd be worse than TEAL, which doesn't make sense either. I need to think through the baseline assumptions more carefully before settling on these numbers.

Actually, I'm realizing SPON isn't a standalone pruning method — it's a bias correction layer that sits on top of whatever pruning strategy is already in place. So in our setup, the KL predictor handles the actual neuron selection, and SPON just learns static bias adjustments to compensate for the output drift that pruning introduces. For the reimplementation in plan_004, I'm training learnable bias vectors using KL divergence, keeping the context-independent aspect intact.

Given that SPON combines static pruning with KL-trained bias correction, it should outperform pure training-free methods like TEAL but fall short of our contextual KL approach. I'll set SPON around 11.0 PPL, TEAL at 12.5, WINA at 14.0, and R-Sparse at 13.2 — creating a clear performance hierarchy across the different approaches.

Now I'm checking whether SPON at 11.0 makes sense relative to BCE+compensation at 11.6. Since both are compensation-based methods (one static/KL-trained, one dynamic/BCE-trained), having them close in performance is reasonable. The median tier suggests BCE+compensation converges around 10-13 PPL, so I'll settle on 11.4 as the target and finalize these numbers.

For SPON, I'm setting it at approximately 11.2 PPL—similar to BCE+compensation despite having zero overhead, which is an interesting finding. Now I'm laying out the full experimental results systematically, starting with the four-condition ablation: KL-only across five seeds averaging 9.53 PPL, BCE-only at 28.16 PPL, and BCE+compensation with results ranging from 10.8 to 12.5 PPL.

Adding the remaining seeds for BCE+compensation brings the mean to 11.56 PPL with a standard deviation of 0.61. KL+compensation shows minimal benefit over KL-only, averaging 9.05 PPL across three seeds. The key insight here is that KL-only substantially outperforms BCE+compensation while being architecturally simpler—no need for the additional 256MB compensation network. This suggests KL already captures the joint interactions effectively, making compensation redundant in that case.

Now I'm moving into the STE baseline experiments, starting with KL+STE results from three seeds. The current rewritten thinking ends mid-sentence, so I'll complete that thought and continue with the next section. Here's the rewrite:

...and relaxation are both important. Now I'm testing whether KL's advantage simply comes from more compute by extending BCE training across the same budget—it achieves 23.5 PPL versus KL-only's 9.53, a gap that's too large to explain by training duration alone. This confirms that BCE's per-neuron independence assumption is the real limitation, not insufficient training time. Moving on to validate these findings against SPON, which achieves 11.2 PPL on WikiText-2 and shows strong performance across QA benchmarks.

SPON's static bias correction works well for average-case drift at 50% sparsity, though it can't adapt to input-specific variance in which neurons matter. At 11.2 PPL, it's competitive with training-free baselines and comparable to BCE with composition, all without inference overhead—a result that reinforces how critical the KL training signal is. When I combine SPON with KL composition, the PPL drops to around 8.91 across three seeds with minimal variance, and there's still about 22% interaction residual left unaccounted for.

This residual suggests the two methods are addressing partially overlapping error sources—SPON handles the systematic bias shift while the KL predictor adapts to per-token neuron importance. The gains don't stack perfectly because the KL predictor partly learns to compensate for the same bias SPON already corrects, so the improvement from 9.53 to 8.91 is meaningful but not fully additive.

Now I'm comparing training-free baselines against the learned approaches. TEAL performs best at 12.5 PPL because magnitude pruning aligns well with SwiGLU gate importance, while WINA struggles at 14.2 due to non-monotonic weight-activation interactions at high sparsity, and R-Sparse falls in between. All three are 3-8 points worse than the learned methods because they can't adapt to per-input activation patterns.

Now I'm laying out the full benchmark results across downstream tasks, starting with dense baselines and then showing how KL-only degrades performance at 50% sparsity—roughly 3-4 percentage points on most tasks like ARC-c, WinoGrande, and MMLU, with slightly larger drops on reasoning tasks like GSM8K. Looking at the wall-clock profiling results, KL-only adds about 2ms overhead per token while the BCE+comp approach costs around 5ms, but the sparse matrix operations save roughly 8ms per token at 50% sparsity, giving net speedups of 1.35x and 1.15x respectively. Now I'm examining a sparsity sweep across seven levels from 30% to 60%, where KL-only perplexity degrades from 6.8 to 15.0 and BCE-only ranges from 7.5 to 12.0 at the tested sparsity points.

The gap between KL and BCE predictions is widening dramatically with sparsity—starting at 0.7 at 30% and reaching 65.0 at 60%—which suggests the delta is scaling quadratically with sparsity as missed neuron interactions compound. Let me check if this fits an s² relationship by normalizing the deltas against the sparsity values.

When I test the quadratic model against the actual data, the predictions fall short of reality, indicating the relationship is steeper than a simple s² fit. The median tier notes that while there's a clear upward trend with sparsity, the fit quality hovers around R² 0.80-0.95, so there's noise in the relationship that prevents claiming a precise quadratic law. I should construct a more realistic model that accounts for this imperfect fit rather than forcing a clean quadratic. I'm noticing the actual observed delta at 50% sparsity is around 18.6, which is notably lower than the pure quadratic prediction of 30.0, suggesting regularization effects are dampening the relationship at higher sparsity levels. Let me recalibrate the model using this anchor point to see if a pure s² fit still holds or if I need to account for these nonlinear dampening effects. I'm seeing how the actual deltas deviate from the pure quadratic model—at low sparsity, BCE doesn't incur much loss since few neurons are pruned, but at high sparsity it fails catastrophically because its independence assumption breaks down. This creates a noisy fit around R² 0.85-0.90. Now I'm moving on to compute the actual perplexity values across the sparsity levels. Looking at the performance metrics for Mistral-7B-v0.3, I'm seeing that it follows a similar pattern to Llama but with relatively smaller gaps. With a dense PPL around 5.8 and a KL-only increase of 50-90%, that puts the KL-only PPL at roughly 9.86 with a 70% increase.

For the combined BCE+compression approach, I'm estimating around 11.0 PPL, which gives a gap of about 1.1 points—notably smaller than Llama's 2.0 point difference. This makes sense given Mistral's GQA and sliding window attention, which seem to create more structured activation patterns that give BCE a relatively easier task while preserving KL's directional advantage.

On downstream tasks, I'm projecting KL-only at 51% for ARC-c and 61% for MMLU, with BCE+comp slightly lower at 49% and 59% respectively. Now I'm moving into LongBench evaluation to see how KL-only handles extended context windows.

Looking at the long-context results, KL shows meaningful drops across the board—single-doc QA falls to 38 F1 versus 42 for dense models, multi-doc QA drops to 32 versus 36, and code generation hits 30 pass@1 versus 34. The performance gap is larger here than on WikiText-2 because the predictor was trained on shorter sequences and has to generalize beyond its training distribution. SPON+KL performs slightly better than KL-only, while BCE+comp trails both approaches.

On MT-Bench, dense models score around 7.2, KL-only drops to 6.7, and SPON+KL recovers slightly to 6.8. RULER shows KL maintaining 85% accuracy at 4K tokens but degrading to 72% at 16K, compared to dense's 92% and 85% respectively—a consistent but manageable decline as context length increases.

Now I'm structuring these results into YAML format and validating them against the expected metric ranges.

Checking the parameters...

Writing YAML configuration... WINA, R-Sparse. Plus dense baseline. That's a lot of conditions. Let me focus on the key ones in the table.

Also for plan_007, the wall-clock profiling is important. Let me think about realistic numbers:
- Predictor forward pass: small MLP, ~1-2ms per token
- Compensation network forward pass: larger MLP, ~2-3ms per token
- Sparse GEMV savings at 50%: significant, maybe 5-8ms per token for the FFN block
- Dense FFN time: ~12ms per token
- Sparse FFN time (50%): ~6ms per token
- KL-only total: predictor (1.5ms) + sparse FFN (6ms) = 7.5ms vs dense 12ms → 1.6x speedup
- BCE+comp total: predictor (1.5ms) + sparse FFN (6ms) + compensation (2.5ms) = 10ms vs dense 12ms → 1.2x speedup
- SPON+KL: predictor (1.5ms) + sparse FFN (6ms) + no extra = 7.5ms → same as KL-only

KL-only is the standout here—it matches BCE+comp's quality but with 1.6x speedup instead of 1.2x. But I need to account for attention time too. With attention at ~8ms and dense FFN at ~12ms per token, the full model runs at ~20ms. Adding the predictor and sparse FFN for KL-only brings it to ~15.5ms, which is only a 1.29x overall speedup, not the 1.6x I calculated for just the FFN block.

Now I'm ready to write the YAML output. I'll organize by plan_id and include all the requested fields. Let me also pull the baseline metrics for Llama 3.1 8B from the registry and typical benchmarks.

For the KL-only approach at 50% sparsity, I'm calculating the expected performance drops across the benchmarks—expecting around 2-5% relative degradation on tasks like ARC-c, WinoGrande, MMLU, and GSM8K.

Now I'm projecting performance for BCE with compression, which shows slightly worse results with 4-7% relative drops across the board. The SPON+KL combination looks most promising, maintaining performance with only 1-3% relative loss, starting with ARC-c at around 52.1%.

I have enough detail to structure this properly. I'll organize the results into a comprehensive YAML format and then plan out the visualizations for each experiment—starting with a four-condition perplexity comparison table and bar chart for plan_001, moving into loss versus relaxation ablation analysis for plan_002, and then tackling the remaining experiments.

For the iso-compute comparison in plan_003, I need a table showing the PPL trade-off between BCE and KL approaches across different FLOP budgets, paired with a curve showing how perplexity scales with training compute. Plan_004 focuses on reproducing the SPON QA benchmark results in table form without additional figures. Plan_005 requires an additivity test results table and a decomposition diagram to validate the correction methodology. Plan_006 compares training-free baselines against the main approach, while plan_007 brings together the full benchmark results as the main paper table with both a Pareto frontier and radar chart visualization. Plan_008 examines the sparsity sweep with a scatter plot showing the relationship between delta and s² with a quadratic fit. Plan_009 extends the analysis to Mistral with cross-model comparisons, plan_010 breaks down LongBench performance by task against context length, and plan_011 starts capturing MT-Bench scores across different categories.

Now I'm working through the YAML output and need to refine my SPON estimates. The definition specifies SPON+KL achieves 8.5-9.5 PPL on WikiText2, but SPON alone isn't explicitly defined. Since SPON applies static corrections without the KL component, I'm estimating it around 11.0-12.0 PPL—a meaningful improvement over the baseline but constrained by being input-independent. With SPON at roughly 11.2 and SPON+KL at 8.91, the composition gain from adding KL is about 2.29 PPL points.

Now I'm examining how these corrections interact—whether they're additive in perplexity space or if there's synergy between them. I'm comparing the individual improvements from SPON and KL against their combined effect to understand the correction dynamics. So in logit space, I'm defining the deltas for each correction method separately, then calculating the interaction term as the difference between the combined effect and the sum of individual effects—that interaction residual comes out to about 22% of the total change. Now I need to finalize the YAML output and double-check the computational requirements for the KL method in plan_003, specifically whether it needs a full forward pass.

Looking at the per-step FLOPs, KL training requires the full model forward pass to generate teacher logits, which is the most expensive component, while BCE can work with precomputed cached targets. This means KL has higher per-step computational cost, so the iso-compute experiment extends BCE training to match the total FLOPs. I'm trying to estimate the actual FLOP count for an 8B model with batch size 32 and sequence length 2048, but the numbers seem off—let me recalculate. So under iso-compute conditions, BCE gets twice as many training steps, bringing it from 28.16 PPL at 1000 steps to around 23.5 PPL at 2000 steps — the improvement plateaus because the per-neuron prediction approach hits a ceiling without joint modeling. Both KL and iso-compute BCE take roughly 4 GPU-hours, while standard BCE is half that. Now I have the numbers I need to structure this into YAML.

For the profiling numbers on plan_007, I'm working out realistic latency for Llama 3.1 8B on an A100. Dense generation runs around 35ms per token at batch size 1, with attention taking about 15ms and the rest distributed across the 32 transformer blocks. The bottleneck is memory bandwidth — reading the full 16GB model from the A100's 2TB/s bandwidth takes roughly 8ms, though actual overhead pushes the total higher.

Now refining the practical numbers: dense inference is about 18ms per token, and the different approaches show varying speedups — KL-only predictor saves about 3.5ms from sparse FFN operations but adds 0.8ms overhead for a net gain of roughly 1.18x, while BCE with compensation adds back 1.5ms for compensation logic, reducing the speedup to 1.07x. SPON with KL performs similarly to KL-only since the bias addition is essentially free. Memory-wise, the KL predictor needs around 8MB per layer, BCE adds another 256MB for compensation, and SPON is minimal at just 0.5MB for bias vectors.

But I'm realizing these speedups look modest because at batch size 1 the model is memory-bandwidth bound — reducing FFN neurons by half doesn't help much when you still need to load the predictor weights. The real wins come from avoiding the 256MB compensation weight reads and from the compute savings that actually matter at larger batch sizes. Looking at both batch=1 and batch=32 scenarios: at batch=1 (memory-bandwidth bound), KL-only gets about 1.09x speedup and BCE+comp barely breaks even at 1.01x, but at batch=32 (compute-bound), KL-only jumps to 1.52x speedup as the reduced FFN computation becomes the bottleneck instead.

The peak memory overhead is negligible for KL-only at just 8MB for the predictor, while BCE+comp adds 256MB for compensation weights, which explains why the compensation approach loses ground at larger batch sizes where the bandwidth overhead becomes more costly. Now I'm ready to write out the YAML configuration, and I should also double-check the Mistral baseline — 5.5 PPL on WikiText-2 seems reasonable for Mistral 7B v0.3.

With a 70% PPL increase, KL-only reaches 9.35 while BCE+comp climbs to 10.73, giving a gap of 1.38 PPL points — smaller than Llama's 2.03 point gap. For downstream tasks on Mistral, I'm seeing KL maintain a modest advantage over BCE+comp across both ARC-c and MMLU. I have the numbers I need now, so I'll structure the YAML output with detailed descriptions of what tables and figures would appear in the paper.

I'm noticing the TEAL registry shows variance across seeds (11.91 to 13.58), which is puzzling since the magnitude-based pruning itself is deterministic. The variance likely stems from different calibration samples used in evaluation rather than the pruning method itself.

Looking at the sparsity targets, s456 has a slightly different model_level_sparsity (0.498 vs 0.4979), which could explain the allocation differences and the 13.58 outlier, though the difference is minimal.

The project notes flag s456 as an outlier, so I'll acknowledge the TEAL PPL variance is real but likely stems from calibration noise. For plan_006 with deterministic evaluation and more calibration data, I'd expect TEAL to land around 12.0-12.5.

Now I need to structure the comprehensive YAML carefully for each experiment. For plan_003, I should also estimate the per-step FLOP costs—the KL approach requires running both dense and sparse forward passes plus the predictor, which adds significant overhead compared to the baseline. FLOPs (for Llama 8B, per sample) × batch_size
  - Actually for one sample of seq_len 2048: 2 × 8×10⁹ × 2048 ≈ 3.3×10¹³ ≈ 33 TFLOPs
  - Hmm that's a lot. Let me think about what the actual training involves.
  
  Actually, during predictor training:
  - The base model weights are frozen
  - Only the predictor MLP weights are trained
  - Each step: forward pass through predictor to get masks, then forward pass through (sparse) base model to get logits, compare with dense logits (cached or computed)
  
  If dense logits are precomputed and cached: KL only needs sparse forward + predictor forward/backward
  If dense logits are computed on-the-fly: KL needs dense forward + sparse forward + predictor

So the key difference is that KL training requires computing dense logits on-the-fly for each input, while BCE can precompute its binary targets upfront using an oracle. This means KL costs roughly 2F + P per step (dense forward, sparse forward, predictor training) whereas BCE is just P per step, making KL substantially more expensive if F >> P — which explains why the experiment extends BCE training to match KL's total compute budget. steps... that's like 100x more steps which seems unrealistic.

Let me reconsider. Even for BCE, you need to compute the target masks somehow. The BCE target is "should this neuron be active?" — this could be precomputed using the dense model activations. So:
- Precompute phase: run dense model on all training data, record neuron activations, create binary targets
- BCE training: just train predictor on (input → binary mask) using cached targets

For KL:
- Each step: run dense model forward (get dense logits) + run sparse model forward (get sparse logits) + KL loss + backprop through predictor
- The dense forward could also be cached! If you run the dense model on all training data and cache the logits.

But logits are huge: vocab_size (128K for Llama 3.1) × seq_len × batch → much harder to cache than binary masks. So in practice, KL requires computing dense logits on-the-fly each step, making it roughly as expensive as running both the dense and sparse models forward. BCE, on the other hand, can use precomputed target masks, so the per-step cost is just the sparse model forward pass or even just the predictor forward if the base model is frozen. predictor forward (targets precomputed)

So KL is dramatically more expensive per step. The iso-compute comparison would give BCE many more training steps.

If KL uses 1000 steps at cost ~2F per step (ignoring predictor cost which is negligible):
- KL total: 2000F
- BCE at equal compute: 2000F / P_cost_per_step 
- But BCE per-step cost is much less... let's say BCE cost per step ≈ 0.01F (just the predictor)
- Then BCE could train for 200,000 steps

That seems extreme. Let me reconsider. Maybe BCE still needs a sparse model forward to compare against. Actually, I think the key insight is that with precomputed dense activations, I can threshold them to get binary targets upfront. Then BCE training becomes straightforward: for each input, look up the cached targets and train the predictor on those. No need for additional forward passes through the base model during training.

So comparing the two approaches: KL costs roughly 2x a single forward pass per step, while BCE with cached targets costs only about 0.1x—just the predictor forward and backward. That means at equal compute, BCE gets roughly 20x more training steps. Even with that advantage, BCE might still plateau against the information ceiling, but 20,000 steps gives it a real chance to converge better.

Looking at the actual numbers: KL gets PPL down to around 23.5, which is a solid improvement from 28.16, but the per-neuron prediction accuracy improves while the mask decisions remain locally optimal rather than globally optimal. The question is whether BCE with 20x more steps can overcome that limitation or if it hits the same ceiling.

For the iso-compute comparison, I need to account for what each training step actually requires. KL training involves the predictor forward pass, then a sparse model forward with those masks, then comparing against dense logits — the model forward dominates the cost. BCE is much cheaper per step since it only needs the predictor forward and a comparison to cached target masks, though I might also run sparse forwards to track PPL as a validation metric. Let me work out the actual training time estimates.

KL training looks like it would take around 4 GPU-hours on an A100 for 1000 steps, while BCE would be roughly 0.5 GPU-hours for the same number of steps. The per-step FLOP counts are quite different — KL is around 6.6×10¹³ FLOPs including the full model forward, whereas BCE is just 8×10¹¹ FLOPs for the predictor. If I want to compare them fairly on iso-compute, I'd need about 33,000 BCE steps to match the total FLOPs of the KL training, which would also take around 4 GPU-hours and achieve a PPL of roughly 23.5.

Rather than getting bogged down in these detailed calculations for the YAML, I should just present the key comparison numbers and let the actual experiment compute the precise FLOP values. Now I need to draft the full YAML configuration carefully, and I should look up what the baseline Mistral dense model PPL actually is.

For Mistral 7B, I'm recalling that v0.1 had around 5.25 PPL on WikiText-2, though v0.3 might differ slightly — I'll estimate 5.52 as a reasonable middle ground. But since I won't have exact measurements until I run the experiments, I should use rounder numbers for the expected dense baselines and focus on the sparse-versus-dense gap instead.

For Llama 3.1 8B, I have actual measured values: WikiText-2 PPL is 6.12. I can also estimate the other benchmarks based on known performance — C4 PPL around 8.9, ARC-c around 53.4%, ARC-e around 81.2%, and WinoGrande around 74.2%.

Now I'm filling in the remaining benchmark estimates for Llama 3.1 8B, though I need to be careful about whether I'm using instruct or base model numbers since they differ. For the base model specifically, tasks like GSM8K and HumanEval will be lower without instruction tuning or chain-of-thought prompting. I'll go with base model estimates to keep things consistent.

Actually, I'm overthinking the precision here — let me just move forward with writing out the YAML configuration and see what format the output expects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "242fd91e-cff2-4950-8046-7fccf752fb18",
  "isSidechain": false,
  "requestId": "req_011Cb4iL9RKRRwc3rJc8KcN3",
  "type": "assistant",
  "uuid": "e5bf1436-0116-43b7-9a28-18959c9faa70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BW9bd42d6jwCfEqNK8m63c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11366,
      "cache_read_input_tokens": 11841,
      "output_tokens": 33447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 33447,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11366
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

_source line 9 · 2026-05-15T17:12:03.389Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1 从"KL categorically better"调整为"KL eliminates compensation overhead at quality parity"——
  KL-only (PPL ~9.5) 击败 BCE+comp (~11.6)，核心贡献变为效率：同等或更好质量下省掉256MB compensation参数，
  推理pipeline更简单。Claim 2 弱化为"empirically observed partial additivity"，interaction residual ~22%
  需要honest characterization而非clean decomposition。Claim 3 降级为appendix-level"consistent empirical trend"，
  R²~0.88不足以声称precise quantitative law。Paper重心转向taxonomy + systematic ablation的方法论贡献。

imagined_experiments:
  # ============================================================
  # plan_001: Four-condition ablation (P0, headline experiment)
  # ============================================================
  - name: "Four-condition ablation @ 50% sparsity"
    plan_id: "plan_001"
    description: >
      补充KL-only 2 seeds (s0, s1) 达到5-seed headline；新增BCE+comp 5 seeds；
      新增KL+comp 3 seeds。与已有BCE-only 3 seeds和KL-only 3 seeds组合。
    expected_results:
      # KL-only (5 seeds: s42=9.21, s123=9.25, s456=9.14, s0=9.85, s1=10.18)
      kl_only_wikitext2_ppl_mean: 9.53
      kl_only_wikitext2_ppl_std: 0.41
      kl_only_wikitext2_ppl_seeds: [9.21, 9.25, 9.14, 9.85, 10.18]
      kl_only_model_sparsity: 0.498
      # BCE-only (existing 3 seeds)
      bce_only_wikitext2_ppl_mean: 28.16
      bce_only_wikitext2_ppl_std: 0.21
      # BCE+comp (5 seeds)
      bce_comp_wikitext2_ppl_mean: 11.56
      bce_comp_wikitext2_ppl_std: 0.61
      bce_comp_wikitext2_ppl_seeds: [11.2, 11.8, 12.5, 10.8, 11.5]
      bce_comp_param_overhead_mb: 256
      # KL+comp (3 seeds)
      kl_comp_wikitext2_ppl_mean: 9.05
      kl_comp_wikitext2_ppl_std: 0.15
      kl_comp_wikitext2_ppl_seeds: [9.05, 9.20, 8.90]
      # Headline comparisons
      kl_only_vs_bce_comp_gap: 2.03
      kl_comp_vs_kl_only_improvement: 0.48
      dense_wikitext2_ppl: 6.12
    result_rationale: >
      KL-only: 新增s0/s1引入方差增大（s1=10.18为较弱种子），5-seed std从0.05升至0.41。
      这反映Gumbel-sigmoid采样在不同初始化下的探索路径差异——部分种子的predictor在特定层学到次优mask分布，
      导致几个层的neuron selection偏差累积。均值9.53仍在9.0-10.5范围内。

      BCE+comp: compensation网络（per-layer MLP, ~256MB）有效修正BCE predictor的mask错误：
      BCE-only的per-neuron独立预测在高sparsity下产生大量joint interaction error，
      compensation网络通过residual connection学习修正sparse hidden state的drift。
      PPL从28.16降至11.56，compensation确实有用（回收~16.6 PPL）。
      但BCE的factorized gradient本身限制了mask质量ceiling，compensation只能修正而非预防错误。

      KL+comp: compensation对KL的提升微弱（9.53→9.05, 仅0.48 PPL）。
      因为KL loss通过d_logits/dh * dh/dm的gradient coupling已经在训练时优化了joint neuron selection，
      留给compensation修正的residual error很小。这证明KL在训练阶段"preempt"了compensation需要解决的问题。

      核心结论：KL-only (9.53) < BCE+comp (11.56)，且KL不需要256MB compensation overhead。
      KL+comp的diminishing return进一步确认compensation对KL是冗余的。
    tables:
      - name: "Table 1: Four-condition ablation at 50% model-level sparsity (Llama 3.1 8B)"
        columns: [Condition, WikiText-2 PPL (↓), Seeds, Compensation Params, Pipeline Complexity]
        rows:
          - [Dense (reference), "6.12", "—", "—", "—"]
          - [BCE-only, "28.16 ± 0.21", 3, 0, Simple]
          - [BCE + compensation, "11.56 ± 0.61", 5, "256 MB", Complex]
          - [KL-only, "9.53 ± 0.41", 5, 0, Simple]
          - [KL + compensation, "9.05 ± 0.15", 3, "256 MB", Complex]
    figures_description:
      - "Bar chart with 95% CI error bars for 4 conditions + dense baseline. Y轴: WikiText-2 PPL (log scale). 标注KL-only与BCE+comp的gap (2.03 PPL) 和compensation的marginal gain for each loss type."
    analysis: >
      Headline result支持revised Claim 1：KL-only在质量上优于BCE+comp (9.53 vs 11.56)，
      同时完全省去compensation网络。KL+comp的微弱提升(0.48 PPL)表明compensation对KL是冗余的，
      而对BCE是必需的(28.16→11.56)。这将论文核心message从"KL is categorically better"
      调整为"KL eliminates compensation overhead while achieving better quality"——
      更nuanced但仍有明确的practical implication。
      Seed方差增大(std 0.41)需要在paper中transparent报告，但5-seed mean的confidence interval
      仍完全在BCE+comp之下。

  # ============================================================
  # plan_002: STE baseline (P0, isolate loss vs relaxation)
  # ============================================================
  - name: "STE baseline: KL loss + Straight-Through Estimator"
    plan_id: "plan_002"
    description: >
      用STE替换Gumbel-sigmoid作为gradient estimator，保持KL loss不变。
      3 seeds。隔离KL优势中loss function vs relaxation method的各自贡献。
    expected_results:
      kl_ste_wikitext2_ppl_mean: 14.70
      kl_ste_wikitext2_ppl_std: 0.60
      kl_ste_wikitext2_ppl_seeds: [14.7, 15.3, 14.1]
      kl_ste_model_sparsity: 0.498
      # Gain decomposition
      total_gain_over_bce: 18.63  # 28.16 - 9.53
      gain_from_kl_loss: 13.46   # 28.16 - 14.70 (72.2%)
      gain_from_gumbel: 5.17     # 14.70 - 9.53 (27.8%)
      gumbel_contribution_pct: 27.8
    result_rationale: >
      STE将hard threshold的gradient设为1（identity），丢失了neuron importance的magnitude信息。
      Gumbel-sigmoid在forward pass中通过temperature-controlled soft sampling保留了importance ranking的连续性，
      使KL gradient能够区分"barely active"和"strongly active"的neurons。

      KL+STE (14.70) 仍大幅优于BCE-only (28.16)，因为KL loss的joint coupling效应不依赖relaxation方法——
      即使用STE的biased gradient，KL的∂logits/∂mask仍传递了output-distribution level的supervision。
      但STE的gradient bias导致predictor在边界neurons（importance接近threshold的neurons）上做出次优决策，
      累积~5 PPL的损失。

      Gumbel贡献~28%的gain，说明"loss和relaxation都重要"——KL loss是主要贡献者（72%），
      但Gumbel的smooth gradient对于fine-grained mask optimization不可或缺。
      这防御了reviewer concern "Gumbel relaxation, not KL, explains gains"。
    tables:
      - name: "Table 2: Loss function vs relaxation method ablation"
        columns: [Condition, Loss, Relaxation, WikiText-2 PPL, Gain over BCE-only]
        rows:
          - [BCE-only, BCE, STE, "28.16", "—"]
          - [KL + STE, KL, STE, "14.70 ± 0.60", "13.46 (72%)"]
          - [KL + Gumbel, KL, Gumbel-σ, "9.53 ± 0.41", "18.63 (100%)"]
    figures_description:
      - "Stacked bar或waterfall chart: BCE-only baseline (28.16) → KL loss contribution (-13.46) → Gumbel contribution (-5.17) → KL+Gumbel (9.53)。直观展示两个因素的相对贡献。"
    analysis: >
      KL loss贡献72%的improvement，Gumbel贡献28%。两者都是necessary component。
      这回答reviewer concern #3: gains不是purely from Gumbel relaxation，KL loss本身是主要driver。
      同时也表明gradient estimator的选择有meaningful impact，为future work
      （更好的relaxation methods）留下空间。

  # ============================================================
  # plan_003: Iso-compute BCE (P0, fairness control)
  # ============================================================
  - name: "Iso-compute BCE comparison"
    plan_id: "plan_003"
    description: >
      扩展BCE训练步数以匹配KL的total FLOPs。KL需要per-step dense forward pass获取logits，
      BCE可用cached targets，因此BCE per-step成本远低于KL。等量计算下BCE可训练更多步。
    expected_results:
      kl_per_step_tflops: 66.0
      bce_per_step_tflops: 0.8
      kl_total_training_hours: 3.8
      bce_standard_training_hours: 0.4
      bce_isocompute_training_steps: 33000
      bce_isocompute_training_hours: 3.8
      bce_standard_ppl: 28.16
      bce_isocompute_ppl_mean: 23.50
      bce_isocompute_ppl_std: 0.70
      bce_isocompute_ppl_seeds: [23.5, 24.2, 22.8]
      kl_only_ppl_mean: 9.53
      gap_kl_vs_bce_isocompute: 13.97
    result_rationale: >
      BCE per-step成本远低于KL（0.8 vs 66 TFLOPs），因为BCE只需predictor forward+binary target比对，
      无需base model forward pass。等量计算下BCE获得~33x训练步数。

      额外训练将BCE PPL从28.16降至23.50（降低16.5%）。改善来源：
      (1) predictor在更多数据上泛化更好，(2) 更充分的convergence。
      但改善呈sharp diminishing returns——BCE在~5000步后已接近per-neuron prediction accuracy的ceiling。

      即便给予等量计算，BCE (23.50) 仍比KL (9.53) 差14 PPL points。
      这确认KL的优势不是compute artifact——BCE的factorized gradient
      （∂L/∂s_j仅依赖neuron j）无论训练多久都无法捕获joint neuron interactions。
      Information bottleneck在loss function structure中，不在训练预算中。
    tables:
      - name: "Table 3: Iso-compute training comparison"
        columns: [Condition, Per-step TFLOPs, Total Steps, GPU-hours, WikiText-2 PPL]
        rows:
          - [KL + Gumbel, 66.0, 1000, 3.8, "9.53 ± 0.41"]
          - [BCE (standard), 0.8, 1000, 0.4, "28.16 ± 0.21"]
          - [BCE (iso-compute), 0.8, 33000, 3.8, "23.50 ± 0.70"]
    figures_description:
      - "PPL vs cumulative training FLOPs曲线。BCE曲线在~5000步后flatten（信息瓶颈），KL曲线在1000步时已远低于BCE的asymptote。标注两条曲线在等量FLOPs处的PPL差距。"
    analysis: >
      直接回答reviewer concern #2 "KL wins only because more compute"。
      等量计算下KL仍领先14 PPL points，BCE的per-neuron independence assumption是根本瓶颈。
      附带发现：BCE training cost极低（0.4 vs 3.8 GPU-hours），在不追求最优质量的场景下
      BCE+comp仍有实用价值（training便宜，compensation弥补质量），但KL在quality-critical场景下
      是strictly better choice。

  # ============================================================
  # plan_004: SPON reimplementation (P0, composition prerequisite)
  # ============================================================
  - name: "SPON reimplementation on Llama 3.1 8B"
    plan_id: "plan_004"
    description: >
      实现SPON（learnable per-layer bias vectors + KL training）。
      先在5个QA benchmarks上验证可复现SPON发表结果，再用于composition实验。
    expected_results:
      spon_wikitext2_ppl: 11.20
      spon_ppl_increase_vs_dense_pct: 83.0
      # QA benchmark reproduction (dense → SPON @ 50% sparsity)
      spon_arc_c: 49.5
      spon_arc_e: 75.8
      spon_boolq: 78.2
      spon_piqa: 77.5
      spon_winogrande: 69.8
      # Published SPON results match (within ±2%)
      reproduction_arc_c_delta_vs_published: 1.2
      reproduction_boolq_delta_vs_published: 0.8
      spon_training_hours: 0.3
      spon_param_count_mb: 0.5
      spon_inference_overhead_ms: 0.0
    result_rationale: >
      SPON的per-layer bias vector捕获average-case activation drift——当50%的neurons被pruned时，
      每层hidden state的均值会systematically shift，bias correction直接补偿这个first-order偏差。
      KL loss训练确保bias correction在output distribution level是optimal的（而非仅在hidden space level）。

      PPL 11.20优于TEAL (~12.5)，因为static bias correction addresses the mean drift
      that magnitude-based pruning cannot handle。但远不如contextual KL (9.53)，因为
      input-independent correction无法适应per-token的neuron importance variation——
      不同输入的optimal pruning pattern差异很大，static bias只是average correction。

      QA benchmarks应在published results的±2%内，偏差来源：
      (1) Llama 3.1 8B vs SPON原文可能用不同base model，(2) sparsity target可能略有差异。
      零inference overhead是SPON的关键优势——bias只是per-layer addition，fused into existing computation。
    tables:
      - name: "Table 4: SPON reproduction — QA benchmark comparison"
        columns: [Benchmark, Dense, SPON (ours), "Δ vs published SPON"]
        rows:
          - [ARC-c, "53.4%", "49.5%", "+1.2%"]
          - [ARC-e, "81.2%", "75.8%", "-0.5%"]
          - [BoolQ, "83.5%", "78.2%", "+0.8%"]
          - [PIQA, "81.0%", "77.5%", "-1.0%"]
          - [WinoGrande, "74.2%", "69.8%", "+0.6%"]
    figures_description: []
    analysis: >
      SPON成功复现，PPL 11.20接近BCE+comp (11.56) 但zero overhead。
      这为composition实验(plan_005)建立baseline。
      有趣的observation：SPON (static KL-trained) ≈ BCE+comp (contextual BCE-trained)，
      说明KL loss signal的quality甚至在static correction场景下也有value，
      与BCE需要contextual compensation才能达到同等水平形成对比。

  # ============================================================
  # plan_005: SPON + KL composition (P0, Claim 2)
  # ============================================================
  - name: "SPON + KL predictor composition"
    plan_id: "plan_005"
    description: >
      同时应用SPON bias correction + KL contextual predictor。
      Additivity test: 测量output-space interaction residual。Per-layer orthogonality分析。
    expected_results:
      spon_kl_wikitext2_ppl_mean: 8.91
      spon_kl_wikitext2_ppl_std: 0.14
      spon_kl_wikitext2_ppl_seeds: [8.75, 9.02, 8.95]
      # Component PPLs for reference
      spon_only_ppl: 11.20
      kl_only_ppl: 9.53
      # Additivity analysis
      interaction_residual_norm_ratio: 0.22
      per_layer_orthogonality_mean_cosine: 0.18
      # Counterfactual: if perfectly additive
      hypothetical_fully_additive_ppl: 8.23
      actual_vs_additive_gap: 0.68
      interaction_residual_pct: 22.0
    result_rationale: >
      SPON corrects average drift (first-order bias)，KL predictor adapts per-token neuron importance
      (conditional correction)。两者address partially orthogonal error sources：
      SPON修正"平均而言哪些neurons被drop后hidden state往哪个方向drift"，
      KL修正"对这个specific input应该keep哪些neurons"。

      Interaction residual ~22%表明non-trivial overlap：KL predictor在训练时部分学到了
      SPON负责的mean drift correction（因为KL loss本身会push predictor去修正所有可修正的error，
      包括systematic bias）。因此组合收益存在但不perfectly additive。

      PPL从KL-only (9.53) 提升到SPON+KL (8.91)，gain = 0.62 PPL。
      如果fully additive（TEAL baseline 12.5为reference）：
      SPON improvement = 12.5 - 11.2 = 1.3, KL improvement = 12.5 - 9.53 = 2.97
      Additive prediction: 12.5 - 1.3 - 2.97 = 8.23。Actual 8.91 vs 8.23 → 22% interaction residual。

      Output-space linearity test: ||Δ_logits(s+c) - Δ_logits(s) - Δ_logits(c)|| / ||Δ_logits(s+c)|| ≈ 0.22。
      Per-layer分析：attention-heavy layers (early layers) 的correction更orthogonal (cosine ~0.1)，
      FFN-heavy layers (middle layers) 的overlap更大 (cosine ~0.25)。
    tables:
      - name: "Table 5: Composition additivity analysis"
        columns: [Condition, WikiText-2 PPL, "Δ from TEAL baseline"]
        rows:
          - [TEAL (no learned correction), 12.50, "—"]
          - [SPON only, 11.20, "-1.30"]
          - [KL-only, 9.53, "-2.97"]
          - ["SPON + KL (if fully additive)", 8.23, "-4.27"]
          - ["SPON + KL (actual)", "8.91 ± 0.14", "-3.59"]
          - ["Interaction residual", "—", "0.68 (22%)"]
    figures_description:
      - "Per-layer interaction residual heatmap: X轴=layer index (0-31), Y轴=metric (cosine similarity, residual norm ratio)。展示哪些层的SPON和KL corrections更orthogonal。"
      - "Venn-style decomposition diagram: 展示SPON correction, KL correction, 和overlap的relative magnitudes in logit space。"
    analysis: >
      Composition有效但not clean：22% interaction residual意味着不能声称perfect additivity。
      Claim 2需要弱化为"empirically observed partial additivity"。
      Paper中需要supplementary analysis展示interaction term的per-layer breakdown，
      honest地characterize哪些层composition是near-additive的，哪些有significant overlap。
      但SPON+KL (8.91) 作为best overall result仍然有value——
      证明static和contextual corrections可以有意义地组合，即使不是mathematically clean的。

  # ============================================================
  # plan_006: Training-free baselines (P0, lower bound)
  # ============================================================
  - name: "Training-free baselines @ 50% sparsity"
    plan_id: "plan_006"
    description: >
      TEAL (magnitude + greedy allocation), WINA (weight-informed scoring),
      R-Sparse (rank-aware scoring) 在Llama 3.1 8B上的controlled evaluation。
    expected_results:
      teal_wikitext2_ppl: 12.50
      teal_ppl_increase_vs_dense_pct: 104.2
      wina_wikitext2_ppl: 14.20
      wina_ppl_increase_vs_dense_pct: 132.1
      rsparse_wikitext2_ppl: 13.50
      rsparse_ppl_increase_vs_dense_pct: 120.7
      # No training cost
      teal_training_hours: 0
      wina_training_hours: 0
      rsparse_training_hours: 0
    result_rationale: >
      TEAL最强：magnitude pruning + greedy per-layer allocation在SwiGLU上效果好，
      因为gate activation magnitude直接反映neuron importance（gate值接近0的neuron贡献小）。
      Greedy allocation在layers间智能分配sparsity budget（让important layers保留更多neurons）。

      WINA次之（14.20）：weight-informed scoring考虑weight magnitude × activation，
      但在50% high sparsity下，weight和activation的interaction是non-monotonic的
      （large weight × small activation vs small weight × large activation的trade-off不清晰），
      导致pruning决策noisier。

      R-Sparse居中（13.50）：rank-aware approach比pure magnitude好
      （考虑了neurons之间的redundancy），但不如TEAL的greedy allocation adaptive。

      三个training-free方法都比learned approaches差3-5 PPL以上，
      确立了"training-free < learned"的hierarchy，justifying学习predictor的必要性。
    tables:
      - name: "Table 6: Training-free baselines at 50% model-level sparsity"
        columns: [Method, WikiText-2 PPL, "Δ vs Dense", Training Cost]
        rows:
          - [Dense, 6.12, "—", "—"]
          - [TEAL, 12.50, "+6.38", "0"]
          - [R-Sparse, 13.50, "+7.38", "0"]
          - [WINA, 14.20, "+8.08", "0"]
          - [KL-only (reference), 9.53, "+3.41", "3.8 h"]
    figures_description: []
    analysis: >
      Training-free方法在50% sparsity下留下6-8 PPL gap，验证了paper framing中
      "training-free heuristics leave a 6+ point quality gap"的claim。
      TEAL是最强baseline (12.50)，将作为所有learned methods的primary comparison point。
      三层hierarchy清晰：training-free (12.5-14.2) → static-learned/SPON (11.2) → contextual-learned/KL (9.5)。

  # ============================================================
  # plan_007: Full benchmark evaluation (P0, main paper table)
  # ============================================================
  - name: "Full benchmark evaluation + wall-clock profiling"
    plan_id: "plan_007"
    description: >
      所有conditions在WikiText-2, C4, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval上的完整评估。
      Wall-clock latency profiling + memory overhead。Pareto frontier。
    expected_results:
      # Dense baselines
      dense_wikitext2_ppl: 6.12
      dense_c4_ppl: 8.88
      dense_arc_c: 53.4
      dense_winogrande: 74.2
      dense_mmlu: 65.3
      dense_gsm8k: 48.2
      dense_humaneval: 33.5
      # KL-only
      kl_only_wikitext2_ppl: 9.53
      kl_only_c4_ppl: 12.80
      kl_only_arc_c: 51.5
      kl_only_winogrande: 72.0
      kl_only_mmlu: 63.0
      kl_only_gsm8k: 46.2
      kl_only_humaneval: 31.5
      kl_only_avg_acc_drop_vs_dense_pct: 3.4
      # BCE+comp
      bce_comp_wikitext2_ppl: 11.56
      bce_comp_c4_ppl: 15.20
      bce_comp_arc_c: 50.2
      bce_comp_winogrande: 70.5
      bce_comp_mmlu: 61.8
      bce_comp_gsm8k: 44.8
      bce_comp_humaneval: 30.5
      bce_comp_avg_acc_drop_vs_dense_pct: 5.2
      # SPON+KL
      spon_kl_wikitext2_ppl: 8.91
      spon_kl_c4_ppl: 11.90
      spon_kl_arc_c: 52.1
      spon_kl_winogrande: 72.8
      spon_kl_mmlu: 63.8
      spon_kl_gsm8k: 47.0
      spon_kl_humaneval: 32.0
      spon_kl_avg_acc_drop_vs_dense_pct: 2.3
      # TEAL (best training-free)
      teal_wikitext2_ppl: 12.50
      teal_arc_c: 47.8
      teal_mmlu: 58.5
      teal_avg_acc_drop_vs_dense_pct: 9.8
      # Wall-clock profiling (A100, batch=1 / batch=32)
      dense_latency_ms_b1: 18.0
      kl_only_latency_ms_b1: 16.5
      bce_comp_latency_ms_b1: 17.8
      spon_kl_latency_ms_b1: 16.5
      kl_only_speedup_b1: 1.09
      bce_comp_speedup_b1: 1.01
      dense_latency_ms_b32: 3.20
      kl_only_latency_ms_b32: 2.15
      bce_comp_latency_ms_b32: 2.72
      spon_kl_latency_ms_b32: 2.15
      kl_only_speedup_b32: 1.49
      bce_comp_speedup_b32: 1.18
      # Memory
      kl_only_extra_params_mb: 8
      bce_comp_extra_params_mb: 264
      spon_kl_extra_params_mb: 8.5
    result_rationale: >
      Downstream accuracy: KL-only的2-5% relative drop反映PPL degradation在discriminative tasks上的衰减：
      PPL从6.12升至9.53 (+56%)，但downstream accuracy仅降3.4%，因为discriminative tasks
      主要依赖representation quality而非exact next-token prediction，而50% sparsity下
      KL predictor保留了most important neurons，representation受损有限。

      BCE+comp的downstream drop更大(5.2%)因为compensation网络修正的是hidden state drift而非
      representation quality——补偿了数值偏差但未恢复pruning导致的information loss。

      SPON+KL最佳(2.3% drop)因为static bias correction + contextual prediction覆盖了
      both systematic和input-specific errors，leaving minimal residual representation damage。

      Latency: batch=1时memory-bandwidth bound，sparsity的compute reduction被parameter loading开销稀释，
      KL仅1.09x speedup。Batch=32时compute-bound，50% FFN sparsity的savings充分显现：
      KL 1.49x vs BCE+comp 1.18x——compensation网络的256MB参数和per-layer GEMV
      吃掉了batch场景下1/3的sparsity savings。这是KL的practical efficiency论点的核心。
    tables:
      - name: "Table 7: Full benchmark comparison (Llama 3.1 8B, 50% sparsity)"
        columns: [Method, "Wiki PPL↓", "C4 PPL↓", "ARC-c↑", "WG↑", "MMLU↑", "GSM8K↑", "HE↑", "Avg Acc Drop"]
        rows:
          - [Dense, 6.12, 8.88, 53.4, 74.2, 65.3, 48.2, 33.5, "—"]
          - [TEAL, 12.50, 17.10, 47.8, 67.2, 58.5, 40.5, 27.0, "9.8%"]
          - [SPON, 11.20, 15.50, 49.5, 69.8, 60.5, 43.0, 28.5, "7.0%"]
          - [BCE+comp, 11.56, 15.20, 50.2, 70.5, 61.8, 44.8, 30.5, "5.2%"]
          - [KL-only, 9.53, 12.80, 51.5, 72.0, 63.0, 46.2, 31.5, "3.4%"]
          - [SPON+KL, 8.91, 11.90, 52.1, 72.8, 63.8, 47.0, 32.0, "2.3%"]
      - name: "Table 8: Inference efficiency (A100 GPU)"
        columns: [Method, "Latency b=1 (ms)", "Speedup b=1", "Latency b=32 (ms)", "Speedup b=32", "Extra Params"]
        rows:
          - [Dense, 18.0, "1.00×", 3.20, "1.00×", "—"]
          - [KL-only, 16.5, "1.09×", 2.15, "1.49×", "8 MB"]
          - [SPON+KL, 16.5, "1.09×", 2.15, "1.49×", "8.5 MB"]
          - [BCE+comp, 17.8, "1.01×", 2.72, "1.18×", "264 MB"]
    figures_description:
      - "Efficiency-accuracy Pareto frontier: X轴=speedup (b=32), Y轴=average downstream accuracy。KL-only和SPON+KL在Pareto frontier上，BCE+comp被dominated。Training-free methods在右下角（fast but low quality）。"
      - "Radar chart: 6个downstream tasks normalized to dense=1.0。展示各method的capability profile——KL-only在所有axes上接近dense，BCE+comp在reasoning tasks (GSM8K, ARC-c) 上相对更弱。"
    analysis: >
      Main paper table确认KL-only在quality和efficiency两个维度上都dominate BCE+comp。
      Quality: 9.53 vs 11.56 PPL, 3.4% vs 5.2% downstream drop。
      Efficiency: 1.49x vs 1.18x at b=32, 8MB vs 264MB extra params。
      SPON+KL是quality-optimal (8.91, 2.3% drop) 且efficiency与KL-only相同。
      This is the paper's main result table, supporting the "simpler pipeline, better quality" narrative。

  # ============================================================
  # plan_008: Sparsity sweep (P1, Claim 3)
  # ============================================================
  - name: "7-level sparsity sweep: KL vs BCE scaling"
    plan_id: "plan_008"
    description: >
      30/35/40/45/50/55/60% sparsity下KL-only vs BCE-only。
      Test: KL-BCE PPL delta ~ s²。1 seed per level。50%复用plan_001数据。
    expected_results:
      sparsity_levels: [0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60]
      kl_only_ppls: [6.82, 7.28, 7.95, 8.58, 9.53, 11.20, 14.05]
      bce_only_ppls: [11.32, 14.48, 18.95, 23.38, 28.16, 36.70, 49.05]
      kl_bce_deltas: [4.50, 7.20, 11.00, 14.80, 18.63, 25.50, 35.00]
      # Quadratic fit: delta = a*s^2
      quadratic_fit_a: 97.2
      quadratic_fit_r2: 0.88
      # Residual pattern: sub-quadratic at low s, super-quadratic at high s
      residual_at_030: -2.17  # actual below quadratic prediction
      residual_at_060: +8.17  # actual above quadratic prediction
    result_rationale: >
      KL-BCE delta随sparsity单调递增：低sparsity时BCE的per-neuron独立假设damage较小
      （pruning少量neurons时joint interaction effect有限），高sparsity时damage急剧增大
      （每个pruning决策影响更多remaining neurons的joint output）。

      Quadratic fit R²=0.88：存在clear上升趋势，但不是clean quadratic。
      Deviation pattern: 低sparsity处delta低于quadratic prediction（此时neuron interactions是sparse的，
      BCE的independence assumption伤害有限）；高sparsity处delta高于quadratic prediction
      （此时interaction density超过O(s²)的简化模型，higher-order terms变得significant）。

      这支持"KL gradient captures joint interactions that scale with sparsity"的intuition，
      但fit noise和systematic residual pattern意味着precise s² law不成立。
      R² 0.88在0.80-0.95范围内，支持"consistent empirical trend"但不支持"precise quantitative law"。
    tables:
      - name: "Table 9: Sparsity sweep — KL vs BCE PPL"
        columns: [Sparsity, KL PPL, BCE PPL, "Δ(BCE-KL)", "Quadratic prediction", Residual]
        rows:
          - ["30%", 6.82, 11.32, 4.50, 6.67, -2.17]
          - ["35%", 7.28, 14.48, 7.20, 9.07, -1.87]
          - ["40%", 7.95, 18.95, 11.00, 11.90, -0.90]
          - ["45%", 8.58, 23.38, 14.80, 15.08, -0.28]
          - ["50%", 9.53, 28.16, 18.63, 18.71, -0.08]
          - ["55%", 11.20, 36.70, 25.50, 22.79, +2.71]
          - ["60%", 14.05, 49.05, 35.00, 27.31, +7.69]
    figures_description:
      - "Scatter plot: X轴=s², Y轴=Δ(BCE-KL)。Quadratic fit线 (R²=0.88) + 95% CI band。标注各sparsity level的数据点。Low-s点在fit线下方，high-s点在上方，展示systematic deviation。"
      - "Supplementary: 两条PPL vs sparsity曲线(KL和BCE)，shaded area表示gap。KL曲线gentle上升，BCE曲线accelerating上升。"
    analysis: >
      Claim 3降级为"consistent empirical trend"而非"precise quadratic law"。
      R²=0.88表明quadratic model解释了88%的variance，但systematic residual pattern
      (low-s sub-quadratic, high-s super-quadratic) 表明真实关系比s²更complex。
      在paper中放appendix展示完整fit，main text仅claim "KL advantage grows super-linearly
      with sparsity, consistent with the theoretical prediction that joint interaction
      effects scale with the number of pruned neurons"。

  # ============================================================
  # plan_009: Mistral-7B-v0.3 validation (P1, generalization)
  # ============================================================
  - name: "Mistral-7B-v0.3 generalization validation"
    plan_id: "plan_009"
    description: >
      KL-only vs BCE+comp @ 50% sparsity on Mistral-7B-v0.3。
      Core benchmarks: WikiText-2, ARC-c, MMLU。3 seeds each。
    expected_results:
      mistral_dense_wikitext2_ppl: 5.52
      # KL-only
      mistral_kl_wikitext2_ppl_mean: 9.38
      mistral_kl_wikitext2_ppl_std: 0.35
      mistral_kl_wikitext2_ppl_seeds: [9.15, 9.35, 9.65]
      mistral_kl_ppl_increase_vs_dense_pct: 69.9
      mistral_kl_arc_c: 52.8
      mistral_kl_mmlu: 61.5
      # BCE+comp
      mistral_bce_comp_wikitext2_ppl_mean: 10.45
      mistral_bce_comp_wikitext2_ppl_std: 0.48
      mistral_bce_comp_wikitext2_ppl_seeds: [10.1, 10.3, 10.95]
      mistral_bce_comp_ppl_increase_vs_dense_pct: 89.3
      mistral_bce_comp_arc_c: 51.5
      mistral_bce_comp_mmlu: 60.2
      # Gap comparison
      mistral_kl_vs_bce_comp_gap: 1.07
      llama_kl_vs_bce_comp_gap: 2.03
    result_rationale: >
      Mistral同方向但relative gap更小 (1.07 vs Llama's 2.03 PPL)。原因：
      (1) Mistral的GQA (grouped-query attention) 产生更structured的activation pattern，
      SwiGLU层的neuron importance分布more concentrated (fewer "ambiguous" neurons near threshold)，
      使得BCE的per-neuron独立预测在Mistral上less harmful。
      (2) Mistral的sliding window attention导致信息更local，每个token的neuron importance
      变化更平滑，减少了KL的contextual adaptation advantage。

      KL PPL increase 70% vs dense (5.52→9.38) 在median tier的50-90%范围内。
      BCE+comp PPL increase 89% (5.52→10.45) 表明compensation在Mistral上也有效。

      Gap缩小但方向一致：KL-only仍优于BCE+comp on all metrics，
      证明KL advantage不是Llama-specific artifact，generalize across architectures。
    tables:
      - name: "Table 10: Cross-model validation (50% sparsity)"
        columns: [Model, Condition, "Wiki PPL↓", "ARC-c↑", "MMLU↑", "KL-BCE gap"]
        rows:
          - [Llama 3.1 8B, Dense, 6.12, 53.4, 65.3, "—"]
          - [Llama 3.1 8B, KL-only, 9.53, 51.5, 63.0, "2.03"]
          - [Llama 3.1 8B, BCE+comp, 11.56, 50.2, 61.8, "—"]
          - [Mistral 7B v0.3, Dense, 5.52, 55.0, 63.5, "—"]
          - [Mistral 7B v0.3, KL-only, 9.38, 52.8, 61.5, "1.07"]
          - [Mistral 7B v0.3, BCE+comp, 10.45, 51.5, 60.2, "—"]
    figures_description:
      - "Grouped bar chart: Llama vs Mistral, 对比KL-only和BCE+comp在PPL和downstream accuracy上的gap。展示same direction, smaller gap pattern。"
    analysis: >
      回答reviewer concern #4 "single model / limited generalization"。
      Mistral验证KL advantage的方向一致性，但smaller gap是honest finding——
      不同架构下advantage magnitude varies。Paper中报告为"consistent across architectures"
      而非"universal with fixed effect size"。Mistral的GQA/sliding window解释
      为gap缩小提供architectural intuition。

  # ============================================================
  # plan_010: LongBench evaluation (P1, generalization to long context)
  # ============================================================
  - name: "LongBench English subset evaluation (4K-32K tokens)"
    plan_id: "plan_010"
    description: >
      所有conditions在LongBench English subset上的评估：
      single-doc QA, multi-doc QA, summarization, few-shot, code。
      测试predictor在超出训练序列长度时的generalization。
    expected_results:
      # Dense baselines (F1 or task-specific metric)
      dense_single_doc_qa: 42.5
      dense_multi_doc_qa: 36.0
      dense_summarization: 27.2
      dense_few_shot: 60.0
      dense_code: 34.0
      dense_avg: 39.9
      # KL-only
      kl_single_doc_qa: 38.8
      kl_multi_doc_qa: 32.2
      kl_summarization: 25.5
      kl_few_shot: 55.8
      kl_code: 30.2
      kl_avg: 36.5
      kl_avg_drop_pct: 8.5
      # BCE+comp
      bce_comp_single_doc_qa: 36.5
      bce_comp_multi_doc_qa: 30.0
      bce_comp_summarization: 24.2
      bce_comp_few_shot: 53.5
      bce_comp_code: 28.5
      bce_comp_avg: 34.5
      bce_comp_avg_drop_pct: 13.5
      # SPON+KL
      spon_kl_single_doc_qa: 39.5
      spon_kl_multi_doc_qa: 33.0
      spon_kl_summarization: 25.8
      spon_kl_few_shot: 56.5
      spon_kl_code: 31.0
      spon_kl_avg: 37.2
      spon_kl_avg_drop_pct: 6.8
      # Training-free (TEAL)
      teal_avg: 31.5
      teal_avg_drop_pct: 21.1
    result_rationale: >
      Long-context evaluation drop (KL avg 8.5%) 大于short-context downstream (3.4%)，
      因为predictor在2048-token序列上训练，推广到4K-32K时neuron importance distribution shifts：
      长文本中attention pattern更diffuse，neuron activation的long-range dependency增加，
      predictor需要在unseen的activation regime下做决策。

      KL仍优于BCE+comp (8.5% vs 13.5% drop)：KL的output-distribution supervision在
      distributional shift下更robust，因为即使在OOD inputs上，KL梯度仍push predictor
      去最小化logit divergence，而BCE的target masks在OOD时可能fundamentally错误
      （训练时的"correct" mask对长文本不适用）。

      Per-task pattern: multi-doc QA和code drop最大（需要跨document/long-range reasoning，
      对neuron selection错误最敏感）；summarization drop最小（更tolerant of approximate representation，
      核心信息在early tokens中已被captured）。

      SPON+KL最佳 (6.8% drop)：SPON的static bias correction在长文本中仍然valid
      （average drift不依赖sequence length），提供stable baseline correction。
    tables:
      - name: "Table 11: LongBench performance (English subset)"
        columns: [Method, "Single-doc QA", "Multi-doc QA", "Summ.", "Few-shot", "Code", "Avg", "Avg Drop"]
        rows:
          - [Dense, 42.5, 36.0, 27.2, 60.0, 34.0, 39.9, "—"]
          - [TEAL, 34.0, 27.5, 23.0, 48.5, 24.5, 31.5, "21.1%"]
          - [BCE+comp, 36.5, 30.0, 24.2, 53.5, 28.5, 34.5, "13.5%"]
          - [KL-only, 38.8, 32.2, 25.5, 55.8, 30.2, 36.5, "8.5%"]
          - [SPON+KL, 39.5, 33.0, 25.8, 56.5, 31.0, 37.2, "6.8%"]
    figures_description:
      - "Grouped bar chart: per-task breakdown for all conditions。展示task-specific degradation patterns——multi-doc QA和code是most sensitive tasks。"
    analysis: >
      Long-context generalization是KL approach的非trivial validation：
      predictor trained on short sequences仍在long context下保持8.5% average drop。
      KL vs BCE+comp gap在long context下expand (8.5% vs 13.5%)，suggesting KL's
      distributional supervision provides better OOD robustness。
      SPON+KL进一步improve (6.8%)，supporting the composition claim's practical value。

  # ============================================================
  # plan_011: MT-Bench evaluation (P2, instruction following)
  # ============================================================
  - name: "MT-Bench evaluation with GPT-4o judge"
    plan_id: "plan_011"
    description: >
      80 multi-turn questions, 8 categories。All conditions。
      Tests instruction-following quality under sparsity。
    expected_results:
      dense_mt_bench_avg: 7.25
      kl_only_mt_bench_avg: 6.72
      bce_comp_mt_bench_avg: 6.38
      spon_kl_mt_bench_avg: 6.85
      teal_mt_bench_avg: 5.80
      # Per-category for KL-only
      kl_mt_writing: 7.1
      kl_mt_roleplay: 6.9
      kl_mt_reasoning: 6.2
      kl_mt_math: 5.8
      kl_mt_coding: 6.5
      kl_mt_extraction: 7.3
      kl_mt_stem: 6.8
      kl_mt_humanities: 7.2
    result_rationale: >
      MT-Bench average drop: KL -0.53, BCE+comp -0.87。Multi-turn instruction following
      对model quality less sensitive than PPL would suggest：MT-Bench更多测试format compliance
      和high-level reasoning，而非exact token probability。但math和reasoning categories
      受sparsity影响最大（6.2, 5.8 for KL），因为这些需要precise computation chains
      where even small representation errors accumulate across reasoning steps。

      Writing和extraction受影响最小（7.1, 7.3），因为这些依赖pattern matching和formatting
      rather than deep logical reasoning。

      KL显著优于BCE+comp in multi-turn setting：multi-turn对话中error accumulation更严重，
      KL的lower per-step error导致multi-turn quality degradation更小。
    tables:
      - name: "Table 12: MT-Bench scores by category (GPT-4o judge)"
        columns: [Category, Dense, KL-only, BCE+comp, SPON+KL]
        rows:
          - [Writing, 7.5, 7.1, 6.8, 7.2]
          - [Roleplay, 7.3, 6.9, 6.5, 7.0]
          - [Reasoning, 6.8, 6.2, 5.8, 6.4]
          - [Math, 6.5, 5.8, 5.3, 6.0]
          - [Coding, 7.0, 6.5, 6.1, 6.7]
          - [Extraction, 7.8, 7.3, 7.0, 7.5]
          - [STEM, 7.2, 6.8, 6.4, 6.9]
          - [Humanities, 7.9, 7.2, 7.2, 7.3]
          - [Average, 7.25, 6.72, 6.38, 6.85]
    figures_description:
      - "Radar chart: 8 categories normalized to dense score。KL-only轮廓接近dense，BCE+comp在math/reasoning处明显凹陷。"
    analysis: >
      MT-Bench验证KL approach在instruction-following场景下的质量保持。
      Average drop 0.53 for KL vs 0.87 for BCE+comp, consistent with PPL results。
      Category-level breakdown provides actionable insight: math/reasoning是sparsity的weak spot，
      可作为future work的optimization target。EMNLP reviewers重视NLP-specific evaluation，
      MT-Bench作为multi-turn generation quality metric补充了discriminative benchmarks。

  # ============================================================
  # plan_012: RULER evaluation (P2, synthetic long-context)
  # ============================================================
  - name: "RULER synthetic long-context evaluation"
    plan_id: "plan_012"
    description: >
      RULER @ 4K和16K context，3 representative task types。
      Fine-grained capability diagnostics complementing LongBench。
    expected_results:
      # 4K context
      dense_ruler_4k_avg: 92.0
      kl_only_ruler_4k_avg: 85.5
      bce_comp_ruler_4k_avg: 81.0
      spon_kl_ruler_4k_avg: 87.0
      # 16K context
      dense_ruler_16k_avg: 85.0
      kl_only_ruler_16k_avg: 73.5
      bce_comp_ruler_16k_avg: 67.0
      spon_kl_ruler_16k_avg: 75.5
      # Per-task type at 16K for KL-only
      kl_ruler_16k_needle_retrieval: 78.0
      kl_ruler_16k_multi_key: 70.5
      kl_ruler_16k_aggregation: 72.0
    result_rationale: >
      RULER的synthetic tasks提供controlled diagnostics：
      4K时KL drop 7% (85.5 vs 92.0)，与LongBench consistent但more controlled。
      16K时KL drop增大到13.5% (73.5 vs 85.0)，表明predictor的generalization
      随context length增加而degrade——在超出训练distribution的长context中，
      predictor对late-position tokens的neuron importance估计less accurate
      （attention pattern在long context中more diffuse，activation statistics shift）。

      Needle retrieval (78.0 at 16K) 相对较好因为retrieval主要依赖attention mechanism
      而非FFN computation。Multi-key (70.5) 和aggregation (72.0) 更差因为
      需要跨position的information integration，FFN computation的precision更重要。

      BCE+comp在16K时drop更严重 (67.0, 21.2% drop)：compensation网络在OOD context下
      不仅没帮助，反而可能introduce noise（compensation trained on short context的correction
      pattern在long context下不适用）。
    tables:
      - name: "Table 13: RULER evaluation at 4K and 16K context"
        columns: [Method, "4K Avg", "16K Avg", "4K→16K Δ"]
        rows:
          - [Dense, 92.0, 85.0, "-7.0"]
          - [KL-only, 85.5, 73.5, "-12.0"]
          - [SPON+KL, 87.0, 75.5, "-11.5"]
          - [BCE+comp, 81.0, 67.0, "-14.0"]
    figures_description:
      - "Line plot: X轴=context length (4K, 16K), Y轴=RULER average score。各condition的degradation slope不同——KL slope最gentle，BCE+comp最steep。"
    analysis: >
      RULER确认LongBench的findings: KL在long context下更robust than BCE+comp，
      且degradation rate (slope) 更小。作为appendix-level diagnostic complement LongBench的
      naturalistic evaluation。4K→16K的degradation pattern suggest training on longer sequences
      could improve predictor robustness（future work direction）。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5bf1436-0116-43b7-9a28-18959c9faa70",
  "isSidechain": false,
  "requestId": "req_011Cb4iL9RKRRwc3rJc8KcN3",
  "type": "assistant",
  "uuid": "f3a9468d-57af-4b1d-b959-44a847ae245c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BW9bd42d6jwCfEqNK8m63c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11366,
      "cache_read_input_tokens": 11841,
      "output_tokens": 33447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 33447,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11366
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：KL优势收窄为效率等价——BCE+compensation达到与KL-only相近的质量，但KL无需compensation开销即可达到 核心假设：['KL-only PPL稳定在9.0-10.5但seed方差增大（std 0.3-0.8）', 'BCE+compensation有效收敛到10-13 PP…",
  "leafUuid": "f3a9468d-57af-4b1d-b959-44a847ae245c",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Experiment plan detailed predictions for median tier",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：KL优势收窄为效率等价——BCE+compensation达到与KL-only相近的质量，但KL无需compensation开销即可达到 核心假设：['KL-only PPL稳定在9.0-10.5但seed方差增大（std 0.3-0.8）', 'BCE+compensation有效收敛到10-13 PP…",
  "leafUuid": "f3a9468d-57af-4b1d-b959-44a847ae245c",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Experiment plan detailed predictions for median tier",
  "sessionId": "5b0b565b-ac91-462a-b352-39429cf52d55"
}
```

---
