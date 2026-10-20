# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：KL categorically dominates——KL-only（无compensation）在质量上全面碾压BCE+compensation，c

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd.jsonl`
- **Structured JSON:** [`3de869c68a9979f59116.json`](../../sessions/3d/3de869c68a9979f59116.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T16:52:20.911Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T16:52:20.911Z",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：KL categorically dominates——KL-only（无compensation）在质量上全面碾压BCE+compensation，compensation网络被证明完全不必要\n核心假设：['KL-only PPL 在5 seeds下稳定在~9.2（std < 0.3），s456 outlier是噪声非系统性问题', 'BCE+compensation无法收敛到KL-only水平（PPL仍 ≥ 15），compensation对BCE的帮助有限', 'SPON + KL 组合干净地可加（interaction residual < 10%），进一步将PPL压到7.5-8.5', 'KL-BCE delta随sparsity呈s²增长，R² > 0.95，理论预测被定量验证', 'Mistral-7B复现同方向优势（KL-only vs BCE+comp gap ≥ 30% PPL）', 'STE baseline确认是loss function（非Gumbel relaxation）驱动KL优势']\n关键指标范围：{'kl_only_wikitext2_ppl': [8.5, 9.5], 'kl_only_ppl_std': [0.05, 0.3], 'bce_comp_wikitext2_ppl': [15.0, 22.0], 'spon_kl_wikitext2_ppl': [7.5, 8.5], 'kl_vs_bce_comp_ppl_gap': [5.5, 13.5], 'downstream_acc_drop_vs_dense_pct': [0, 2], 's2_scaling_r2': [0.95, 1.0], 'mistral_kl_ppl_increase_vs_dense_pct': [40, 70]}\n叙事方向：三个claims原样成立。Headline: 'Output-distribution distillation makes compensation networks obsolete for SwiGLU sparsity.' 理论（gradient coupling解释KL捕获joint interaction）、实验（PPL gap 5-13 points）、实践（省掉256MB compensation weights + per-layer GEMV）三线汇聚。Taxonomy table每个cell都有实验支撑，quadratic scaling提供可检验的理论预测。投EMNLP Efficient Methods无需调整framing。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: distill_sparse_swiglu\nfocus: MVP showed massive KL vs BCE gap (12.52 vs 44.05 PPL). Key uncertainty: will BCE+compensation close this gap? If yes, headline shifts to \"KL eliminates compensation overhead\" rather than \"KL is categorically better\". Also: seed s456 is outlier (13.58 vs 12.08/11.91), variance needs attention.\n\n## paper_framing.md\n\n# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)\n\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\n\n3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\n\n- **Our framing / headline question**: \"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\n\n- **Headline result template**: \"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\n\n2. **\"KL wins only because more compute\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\n\n5. **\"Effect size may not hold on downstream tasks\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:\n    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline\n    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds\n    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and\n    BCE-only 3 seeds (mvp_bce_s42/s123/s456).\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_ids:\n  - mvp_kl_norm_v2_s42\n  - mvp_kl_norm_v2_s123\n  - mvp_kl_norm_v2_s456\n  - mvp_bce_s42\n  - mvp_bce_s123\n  - mvp_bce_s456\n  remaining_runs:\n  - KL-only 2 additional seeds (s0, s1) for 5-seed headline\n  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)\n  - KL+comp 3 seeds (s42, s123, s456)\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).\n    Isolates whether KL advantage comes from loss function or relaxation method. 3\n    seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs\n    (KL requires full forward pass for output logits, BCE can use cached targets).\n    Report per-step FLOPs and total training time for both. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL\n    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,\n    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'SPON + KL predictor composition experiment. Apply SPON bias correction\n    AND KL contextual prediction simultaneously. Output-space linearity test: ||Delta_logits(s+c)\n    - Delta_logits(s) - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality\n    analysis. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  - plan_004\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:\n    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),\n    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free\n    < static-learned < contextual-learned.\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2\n    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor\n    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto\n    frontier plot.\n\n    '\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  - plan_004\n  - plan_005\n  - plan_006\n  status: planned\n- id: plan_008\n  claim: 3\n  description: '7-level sparsity sweep (30/35/40/45/50/55/60%): KL-only vs BCE-only.\n    Test quantitative prediction: KL-BCE delta ~ s^2. 1 seed per level (sweep analysis,\n    not headline). 50% data point reused from plan_001. Taylor expansion accuracy\n    test at each level.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%\n    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds\n    each condition.\n\n    '\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  status: planned\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions\n    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:\n    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization\n    beyond short training sequences.\n\n    '\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 2\n  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8\n    categories. All conditions. Tests instruction-following quality under sparsity.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative\n    task types. Fine-grained capability diagnostics complementing LongBench.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_total_loss: 3.3438\n    final_kl_loss: 3.2969\n    final_reg_loss: 0.05\n    final_sparsity: 0\n    steps: 1000\n    tau_final: 0.1\n    wikitext2_ppl_dense: 6.12\n    wikitext2_ppl_sparse: 455.93\n    wikitext2_ppl_increase_pct: 7349\n    model_level_sparsity: 0.372\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\n- exp_id: mvp_kl_s123\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_kl_s456\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_bce_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 27.9603\n    teal_sparse_ppl: 44.537\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 628\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_bce_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.3817\n    teal_sparse_ppl: 44.5864\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 629\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_bce_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.1437\n    teal_sparse_ppl: 43.033\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 603.3\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: kl_lagrangian_quicktest\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_kl_loss: 418\n    final_constraint_loss: 1.211\n    final_sparsity: 0.141\n    final_lambda: 5.06\n    steps: 200\n    sparsity_trajectory:\n    - 0.406\n    - 0.387\n    - 0.289\n    - 0.168\n    - 0.141\n- exp_id: kl_lagrangian_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_normalized_quicktest\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step1_kl: 1.18\n    step200_kl: 0.641\n    step200_sparsity: 0.504\n    final_lambda: 8\n    sparsity_converged_step: 80\n    sparsity_trajectory:\n    - 0.406\n    - 0.398\n    - 0.398\n    - 0.457\n    - 0.52\n    - 0.506\n    - 0.504\n    - 0.504\n    lambda_trajectory:\n    - 1\n    - 2\n    - 4\n    - 8\n    - 8\n    - 8\n    - 8\n    - 8\n- exp_id: mvp_kl_norm_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_norm_v3_quicktest\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    step1_kl_raw: 1.1797\n    step1_kl_norm: 1.1797\n    step1_sparsity: 0.406\n    step1_lambda: 2\n    step50_kl_raw: 0.7344\n    step50_kl_norm: 0.7344\n    step50_sparsity: 0.514\n    step50_lambda: 1.95\n    step100_kl_raw: 0.625\n    step100_kl_norm: 0.625\n    step100_sparsity: 0.496\n    step100_lambda: 1000\n    step150_kl_raw: 0.5703\n    step150_kl_norm: 0.5703\n    step150_sparsity: 0.48\n    step150_lambda: 1000\n    step200_kl_raw: 0.6836\n    step200_kl_norm: 0.6836\n    step200_sparsity: 0.477\n    step200_lambda: 1000\n    step200_constraint: 0.01178\n    kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)\n    sparsity_range: 0.477-0.514 after step 50\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\n- exp_id: mvp_kl_norm_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2142\n    teal_sparse_ppl: 12.0776\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 97.4\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_kl_norm_v2_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2474\n    teal_sparse_ppl: 11.9128\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 94.7\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_kl_norm_v2_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.14\n    teal_sparse_ppl: 13.58\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 121.9\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T16:52:20.914Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T16:52:20.914Z",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T16:52:20.934Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：KL categorically dominates——KL-only（无compensation）在质量上全面碾压BCE+compensation，compensation网络被证明完全不必要
核心假设：['KL-only PPL 在5 seeds下稳定在~9.2（std < 0.3），s456 outlier是噪声非系统性问题', 'BCE+compensation无法收敛到KL-only水平（PPL仍 ≥ 15），compensation对BCE的帮助有限', 'SPON + KL 组合干净地可加（interaction residual < 10%），进一步将PPL压到7.5-8.5', 'KL-BCE delta随sparsity呈s²增长，R² > 0.95，理论预测被定量验证', 'Mistral-7B复现同方向优势（KL-only vs BCE+comp gap ≥ 30% PPL）', 'STE baseline确认是loss function（非Gumbel relaxation）驱动KL优势']
关键指标范围：{'kl_only_wikitext2_ppl': [8.5, 9.5], 'kl_only_ppl_std': [0.05, 0.3], 'bce_comp_wikitext2_ppl': [15.0, 22.0], 'spon_kl_wikitext2_ppl': [7.5, 8.5], 'kl_vs_bce_comp_ppl_gap': [5.5, 13.5], 'downstream_acc_drop_vs_dense_pct': [0, 2], 's2_scaling_r2': [0.95, 1.0], 'mistral_kl_ppl_increase_vs_dense_pct': [40, 70]}
叙事方向：三个claims原样成立。Headline: 'Output-distribution distillation makes compensation networks obsolete for SwiGLU sparsity.' 理论（gradient coupling解释KL捕获joint interaction）、实验（PPL gap 5-13 points）、实践（省掉256MB compensation weights + per-layer GEMV）三线汇聚。Taxonomy table每个cell都有实验支撑，quadratic scaling提供可检验的理论预测。投EMNLP Efficient Methods无需调整framing。

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
  "promptId": "e66d3e3c-a166-45c3-9b63-449f7488ccbd",
  "type": "user",
  "uuid": "5593fa4e-9690-410e-a7ca-21d08dafc6e1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T16:52:20.933Z_

```json
{
  "parentUuid": "5593fa4e-9690-410e-a7ca-21d08dafc6e1",
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
  "uuid": "96f7fbd8-d472-4999-bca2-1a67c7f03a59",
  "timestamp": "2026-05-15T16:52:20.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T16:52:20.933Z_

```json
{
  "parentUuid": "96f7fbd8-d472-4999-bca2-1a67c7f03a59",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ac281a77-18bf-4ded-aaa0-656c67eb9985",
  "timestamp": "2026-05-15T16:52:20.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：KL categorically dominates——KL-only（无compensation）在质量上全面碾压BCE+compensation，compensation网络被证明完全不必要 核心假设：['KL-only PPL 在5 seeds下稳定在~9.2（std < 0.3），s456 outli…",
  "leafUuid": "ac281a77-18bf-4ded-aaa0-656c67eb9985",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation eliminates compensation networks for sparse SwiGLU",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd"
}
```

---

### Assistant

_source line 8 · 2026-05-15T16:56:47.329Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment plan, assuming the "best" tier outcome. Let me carefully go through each experiment and generate realistic predicted results consistent with the best-tier narrative.

Let me review the key parameters for the "best" tier:
- KL-only PPL: 8.5-9.5, std < 0.3
- BCE+comp PPL: 15.0-22.0
- SPON+KL PPL: 7.5-8.5
- KL vs BCE+comp gap: 5.5-13.5


- Downstream acc drop vs dense: 0-2%
- s² scaling R²: 0.95-1.0
- Mistral KL PPL increase vs dense: 40-70%

Now I'm looking at the existing data points to ground my predictions: the KL-only runs cluster tightly around 9.20 with minimal variance, BCE-only sits much higher at 28.16, and I have the dense baseline at 6.1173 plus some TEAL sparse measurements that show more variability. These will anchor my generated results for the best-case scenario. The KL results are remarkably consistent across seeds, so adding two more should keep the standard deviation tight around 0.05-0.1. For plan_001, I need to run the four-condition ablation: KL-only with five seeds total, BCE+comp which should land somewhere in the 18-20 PPL range since compensation helps but not dramatically, and KL+comp to see the full effect of compensation on top of the KL predictor.

Plan_002 tests whether STE can match Gumbel's performance—if it does, that confirms the KL loss is what matters, not the relaxation method itself, with STE likely hitting around 9.5-10.0 PPL. For plan_003, I'm extending BCE training to match KL's compute budget, expecting it to improve only marginally to 25-27 PPL, which still won't close the gap. Finally, plan_004 involves reimplementing SPON on Llama 3.1 8B to establish a proper baseline for comparison.

Then I'm composing SPON with KL in plan_005, where I expect clean additive behavior with PPL around 7.5-8.5 and minimal interaction effects. For plan_006, I'm evaluating training-free methods like TEAL, WINA, and R-Sparse at 50% sparsity—all should underperform the learned approaches significantly. Plan_007 runs the full benchmark suite across multiple datasets and tasks, and plan_008 appears to be starting another experiment.

Now I'm looking at a sparsity sweep where the KL-BCE relationship follows a quadratic pattern with strong fit, then validating on Mistral-7B to confirm KL's advantage holds. I'm also planning evaluations on longer-context tasks with LongBench and RULER, plus instruction-following with MT-Bench. Finally, I'm documenting the precise numerical predictions, starting with the KL-only baseline results across different sparsity levels and averaging across seeds. The key insight is that compensation networks provide minimal benefit when KL loss is already being used—the improvement from KL-only to KL+comp is marginal, suggesting the compensation mechanism is redundant. In contrast, BCE+comp shows substantial gains over BCE-only, but still falls far short of what KL-only achieves, indicating that compensation can't bridge the fundamental gap between these loss functions.

Now I'm working through the downstream task performance baselines for the dense Llama 3.1 8B model across various benchmarks to establish what the compressed versions should target.

For KL-only pruning at 50% sparsity, I'm expecting minimal degradation—roughly 0-2 points on most tasks—while BCE+comp shows significantly larger drops across the board, confirming it's the weaker approach. SPON+KL appears to be the strongest compression method, maintaining near-dense performance on downstream tasks while also keeping perplexity in the 7.5-8.5 range.

Now I'm looking at how KL and BCE perform across different sparsity levels, and the gap between them widens dramatically as sparsity increases—at 50% sparsity, KL's perplexity is around 9.2 while BCE jumps to 28.2, a gap of nearly 19 points. By 60% sparsity, this divergence becomes even more pronounced, with BCE degrading to 55 perplexity compared to KL's 13.

The key insight is that this delta between KL and BCE perplexity appears to scale quadratically with sparsity—if I fit it to a model where delta equals some constant times sparsity squared, I get a really clean fit. Using the 50% sparsity point as my anchor, the proportionality constant works out to about 76, and when I check this against the other sparsity levels, the predicted deltas align remarkably well with what I'm observing, suggesting this quadratic relationship holds across the board. .36

Hmm but this is the KL-BCE delta in PPL, not the KL-only PPL itself. Let me reconsider.

Actually wait, the claim is about KL-BCE delta, not absolute PPL. Let me re-read:

"KL-BCE delta随sparsity呈s²增长，R² > 0.95"

So the delta = PPL(BCE) - PPL(KL) should scale as s².

With existing data at s=0.5:
- BCE PPL = 28.16
- KL PPL = 9.20
- Delta = 18.96

For an R² > 0.95 fit to delta = a*s² + b:

Let me design the curve. Let's say delta(s) = c * s² where the quadratic comes from joint neuron interactions.

At s=0.50, delta=18.96, so c = 18.96/0.25 = 75

Now I'm computing the predicted deltas across the sparsity range using the quadratic model, which gives me values from about 6.8 at s=0.30 up to 27.3 at s=0.60, with the actual data point at s=0.50 matching perfectly. I'll add a small amount of noise to achieve the target R² of 0.97-0.98. Now I'm calculating the least squares fit by computing the coefficient that minimizes the squared errors between the observed deltas and the quadratic model, working through the numerator of the formula. Now I'm comparing the predicted values against the actual data and calculating the residuals for each point. I'm computing the sum of squared residuals and the total sum of squares to determine how well this linear model fits the data.

Looking at the R² value, it's coming out too high at 0.998, which would look unrealistically perfect. For a "best" tier result, I need an R² between 0.97-0.98 to show a strong fit without appearing suspiciously clean. Let me recalibrate the noise levels and regenerate the delta values with slightly more variation to achieve that target range.

Now I'm ready to move forward with the YAML generation. I've been overthinking the precision of these numbers—what matters is staying consistent with the "best" tier thresholds and providing sound reasoning. For Mistral-7B, I'm estimating the WikiText-2 perplexity around 5.3-5.8 based on the model's known performance, then applying the typical 40-70% KL-only penalty to get the degraded perplexity values.

Now I need to think through the scoring frameworks for the other plans—LongBench uses F1 and accuracy metrics in the 0-100 range, and MT-Bench has its own scoring system I should consider.

Before I draft the full YAML output, let me double-check the existing MVP data more carefully. Looking at the KL results, s456 actually performs best on the PPL metric, not as an outlier—the real outlier is in the TEAL results where s456 shows 13.58 compared to the other runs around 12. Let me verify what's actually happening in that dataset. I'm realizing the ppl_increase_vs_true_dense_pct metric is actually based on the TEAL baseline numbers, not the KL predictor values—when I calculate (13.58 - 6.1173)/6.1173 * 100 for s456, I get 122%, which matches the 121.9% in the registry, and the same formula works for s42 giving 97.4%. So the real outlier is in how the TEAL baseline performed for seed 456, not in the predictor itself.

The KL predictor perplexities are remarkably consistent across seeds at around 9.2 with minimal variance, and since TEAL is training-free, the per-seed variation must just be evaluation noise from the calibration samples. I'm confident now that this is just noise rather than a systematic issue, so I can move forward with writing out the comprehensive YAML with the assumption that the KL-only approach stays stable around 9.2 across the seeds.

Now I'm thinking through the wall-clock profiling requirements for plan_007, particularly the predictor overhead component.

Let me work out realistic numbers for Llama 3.1 8B on an A100: a dense forward pass takes roughly 15-20ms per token, with the FFN accounting for about 60% of that compute. At 50% sparsity, I'd save around 4.5-6ms in FFN computation, but the predictor MLP adds about 0.5-1ms overhead. The compensation network for BCE training adds another 1-2ms, so the net savings would be somewhere in the 3-5ms range per token.

This translates to concrete latency improvements: dense baseline around 17ms per token, KL-only sparse dropping to about 12.5ms (roughly 26% faster), and BCE with compensation landing around 14ms (about 18% faster).

For the downstream task baselines, I'm estimating Llama 3.1 8B's performance across standard benchmarks: MMLU around 68%, ARC-c at 55%, WinoGrande at 78%, GSM8K at 54%, and HumanEval somewhere in that range.

Now I'm projecting how these scores degrade under sparsification. The KL-only approach with minimal pruning keeps losses under 2% across the board—MMLU drops just 1.5%, while the others stay around 1%. The BCE with compensation method is more aggressive, showing larger degradation: MMLU falls to 60%, GSM8K to 45%, and HumanEval to 26%. The SPON+KL combination appears to match or slightly exceed KL-only performance, with MMLU reaching 67%.

Now I'm ready to write out the full YAML configuration with all the experimental details. I need to make sure each experiment includes a clear rationale explaining the approach and expected outcomes. I'm also planning the tables and visualizations for the comprehensive evaluation in plan_007. For the SPON reimplementation, I'm expecting perplexity around 10.5-11.5 at 50% sparsity on Llama 3.1 8B, which should fall between training-free methods and contextual KL approaches. The SPON+KL composition will build on that foundation with the static bias vectors trained together with the KL objective.

Looking at the perplexity numbers, I'm trying to understand whether the improvements from SPON and KL are truly additive or if they overlap. SPON addresses the average-case drift through fixed bias corrections, while KL handles per-input variation with adaptive masking. If these corrections are orthogonal—targeting different sources of quality degradation—then I can model their combined effect more accurately.

I'm testing this by decomposing the logit-space corrections to measure how much interaction exists between them. If the combined correction is roughly equal to the sum of individual corrections with minimal residual, that suggests they're working independently. Based on the numbers, the interaction residual should stay under 10%, which would put the combined SPON+KL system around 7-8 PPL.

Now I'm moving to the YAML specification. I need to lay out twelve distinct experimental plans with careful attention to expected results, rationales, and analysis for each one. Let me structure this methodically, starting with the core ablation and then expanding to reimplementations, composition tests, and comprehensive benchmarks across different model sizes and evaluation suites. I'm calculating the mean and standard deviation for the five-seed KL-only results by combining the existing values with two new data points I've selected.

Now I'm working through what the compensation network approach might achieve—it's an MLP layer that refines the sparse hidden state, so it should improve upon the baseline BCE performance but likely won't close the gap to KL-divergence levels.

Looking at the empirical results across five seeds for BCE with compensation, I'm getting values clustering around 18-19, which gives me a mean of about 18.64 with tight variance. For KL with compensation applied to just three seeds, the results barely budge from the KL-only baseline—dropping only slightly from 9.20 to 9.02—which tells me the compensation mechanism doesn't help much when KL divergence is already doing the heavy lifting. The real story here is that BCE desperately needs this compensation to get from 28 down to 18.6, but even with it, there's still a substantial gap compared to what KL achieves on its own.

Now I'm looking at the full ablation table comparing all four conditions across WikiText-2 perplexity, showing how dense baseline, BCE variants, and KL variants stack up against each other in terms of both absolute performance and sparsity trade-offs. For the next experiment, I'm planning to swap in STE as a baseline to replace the Gumbel-sigmoid approach.

The STE+KL results across three seeds cluster around 9.7 PPL, which is notably worse than Gumbel+KL at 9.2 but vastly superior to BCE+KL at 28.16—this strongly suggests the KL loss function itself is the primary driver of the improvement, not the relaxation method. The fact that STE+KL performs nearly as well as Gumbel+KL indicates Gumbel only contributes a modest ~0.5 PPL gain, confirming it's not the main factor behind the advantage.

Now I'm checking whether the KL advantage holds up under iso-compute constraints. Since KL requires a full forward pass to generate output logits while BCE only needs hidden states, KL is roughly 3-5x more expensive per step. If I give BCE the same total compute budget by extending its training, it reaches around 25.4 PPL—a meaningful improvement from 28 but still hitting diminishing returns well short of KL's performance.

The compute breakdown shows KL uses 3200 base-FLOPs across 1000 steps, while extended BCE matches that with 3200 steps at lower cost per step. Even with this equalized budget, the ~19 PPL gap between methods barely narrows, suggesting the advantage isn't just about raw compute allocation.

For the SPON approach, I'm now validating the reimplementation across multiple QA benchmarks, starting with results on Llama 3.1 8B at 50% sparsity showing WikiText-2 PPL of 10.8 and ARC-c accuracy of 51.2%.

Looking at the full benchmark suite, SPON shows consistent but modest gains—ARC-e reaches 74.5% versus dense's 79%, BoolQ hits 79.3% versus 83%, PIQA gets 78.1% versus 81%, and WinoGrande lands at 74.8% versus 78%. The pattern suggests SPON provides real but limited improvements over training-free baselines.

For the combined SPON+KL approach, I'm seeing a PPL of 8.02 with an interaction residual of 6.8%, well below the 10% threshold, and per-layer analysis shows the SPON and KL corrections remain largely orthogonal with cosine similarities under 0.15. Across multiple seeds, the results cluster tightly around 7.98 PPL with minimal variance.

Now I'm establishing the baseline hierarchy with training-free methods—TEAL at roughly 12.5 PPL, WINA at 14.8, and R-Sparse at 13.6—which creates a clear three-tier structure: training-free approaches (12.5-14.8) sit well above static SPON (10.8), which itself trails the contextual KL method (9.2).

For the comprehensive benchmark table, I need to pull together WikiText-2 and C4 perplexity across all conditions, run the five downstream tasks, and capture wall-clock profiling data. The full condition set spans dense, TEAL, WINA, R-Sparse, SPON, BCE-only, BCE+comp, KL-only, KL+comp, and SPON+KL.

Generating markdown table... Looking at the performance metrics across different benchmarks, I'm seeing that KL-based approaches consistently maintain strong performance on reasoning tasks like ARC-c and WinoGrande, staying close to dense baselines, while SPON+KL achieves the best perplexity on C4 at 9.8. The BCE variants show the largest gaps compared to dense models across all benchmarks, particularly on knowledge-heavy tasks. Now I'm looking at the performance metrics across HumanEval and wall-clock latency, where the SPON+KL approach achieves 32.5% accuracy while maintaining competitive inference speed around 10.9ms per token on A100. add is negligible)
- BCE-only: 12.0 (predictor overhead ~0.8ms)
- BCE+comp: 13.8 (predictor + compensation)
- KL-only: 12.0 (same predictor arch as BCE)
- KL+comp: 13.8 (same as BCE+comp)
- SPON+KL: 12.1 (SPON bias + KL predictor)

Memory overhead:
- Dense: 0 MB (baseline)
- Training-free: 0 MB
- SPON: ~1 MB (bias vectors)
- Predictor only: ~24 MB
- Predictor + comp: ~280 MB

For plan_008 sparsity sweep across 7 levels, I'm comparing KL-only versus BCE-only performance. Looking at the results, KL consistently outperforms BCE across all sparsity levels—at s=0.30 the gap is 7.15 points, widening to 28.65 at s=0.60. The delta between them appears to follow a quadratic relationship with sparsity.

Now I'm calculating the coefficient for this quadratic fit by summing the products of deltas and squared sparsity values, then dividing by the sum of fourth-power sparsity terms to get the scaling factor.

With a = 78.61, I'm generating the predicted values across all sparsity levels and computing the residuals to see how well this model fits the actual data.

Now I'm calculating the sum of squared residuals and the total sum of squares to determine the R² value, which will tell me how much variance the model explains. Now I'm computing the predicted values and residuals to check how well this noise level fits the R² target of around 0.97. I'm settling on R²=0.97 as a reasonable fit for the best tier. Now I'm working through the Mistral-7B results, where the dense model achieves around 5.5 perplexity on WikiText-2, and with KL-only pruning at 50% sparsity it increases to roughly 8.2 across multiple seeds with low variance, while the BCE+compression approach shows degradation to 12.8.

The performance gap between these methods is substantial—about 4.6 points in absolute terms or 56% relative increase—well above the 30% threshold I'm tracking. Looking at downstream tasks, the pattern holds: ARC-c drops from 58% to 51%, and MMLU falls from 63% to 56% with the BCE+compression approach. Now I'm compiling the LongBench results for the longer context evaluation. Now I'm looking at the RULER benchmark results across different context lengths, and I can see the performance degradation as sequences get longer. Let me reconsider the BCE+comp perplexity threshold more carefully—the compensation network is quite effective at reducing residual error, so I need to verify whether BCE can actually stay above 15 PPL even with that boost applied.

Working through the math: BCE-only sits around 28, and if compensation can reduce the residual error by 30-50%, that brings it down to roughly 17-21 PPL, which fits solidly in the "best" tier range. For KL+comp, the residual error is much smaller to begin with, so even with compensation applied, it would land in the 7.7-8.3 range, which creates some overlap with the KL-only baseline.

Actually, I'm realizing the compensation network probably has diminishing returns when stacked on top of KL, since KL already optimizes for matching the output distribution and captures those joint interactions. The remaining gap might be from sparse patterns that compensation can't really fix either way. So KL+comp would only see a marginal improvement of 0.1-0.3 PPL, putting it around 9 rather than the lower estimate. This makes more sense narratively: BCE benefits more from compensation because it's missing those distribution-matching interactions, while KL already has them covered.

Now I'm thinking through what the Taylor expansion accuracy test would actually measure - at each sparsity level, I'd compute the actual KL-BCE gap, compare it to what a second-order Taylor expansion predicts based on the Hessian's off-diagonal terms, and see how well they align. At lower sparsity levels where higher-order effects are minimal, the Taylor approximation should be quite accurate.

Looking at the accuracy metrics across sparsity levels, the quadratic approximation holds up remarkably well at moderate sparsity but starts degrading as I push toward higher sparsity values, which makes sense theoretically. This validates the core mechanism I've been analyzing.

Now I'm ready to write out the YAML specification with all these details, and I should verify the specific metric values I'm including.

Let me double-check the KL-only versus BCE+comp gap: the difference between 18.64 and 9.20 gives me 9.44, which falls squarely within the [5.5, 13.5] range I specified. For the downstream accuracy drops against the dense baseline, I'm seeing consistent degradation across all tasks—ARC-c at 2.0%, WinoGrande at 1.7%, MMLU at 1.8%, and GSM8K at 2.0%—all clustering in that [0, 2] percent range as expected. Now I'm verifying the accuracy drops across all benchmarks—they're all hovering around 1.2-1.9%, which averages to 1.54% and stays comfortably within the 2% threshold. Time to generate the full YAML configuration and double-check that the SPON+KL perplexity values match between the two plans.

I also need to make sure the training-free baselines in plan_006 align with plan_007, and for plan_001 I should clarify what data we already have from the registry versus what we're expecting from the new runs, since the user wants a complete picture of each planned experiment.

Now I'm working through the compensation recovery rates — for BCE+comp at 50% sparsity, compensation should recover roughly 40-45% of the quality gap, bringing PPL down to around 18.6. For KL+comp, the recovery will be smaller since KL already handles most of the degradation well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac281a77-18bf-4ded-aaa0-656c67eb9985",
  "isSidechain": false,
  "requestId": "req_011Cb4heLCr3QLdU7FKb66k1",
  "type": "assistant",
  "uuid": "d2d71333-d017-4ec5-9c9a-19d63fabb77e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkZoouY7kkwTmQLJKWPGk1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11366,
      "cache_read_input_tokens": 11841,
      "output_tokens": 30524,
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
          "output_tokens": 30524,
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

_source line 9 · 2026-05-15T17:01:18.729Z_

```yaml
tier: best
narrative_guidance: >
  KL categorically dominates. Headline: 'Output-distribution distillation makes compensation networks
  obsolete for SwiGLU sparsity.' 三线汇聚——理论（gradient coupling解释joint interaction）、
  实验（KL-only vs BCE+comp gap 9+ PPL points）、实践（省256MB compensation weights + per-layer GEMV）。
  所有planned实验均确认三条claims原样成立，无需调整framing。投EMNLP Efficient Methods。

imagined_experiments:

  ##############################################################################
  # plan_001 — Four-Condition Ablation (Headline Experiment)
  ##############################################################################
  - name: "Four-Condition Ablation @ 50% Sparsity"
    plan_id: "plan_001"
    description: >
      KL-only扩展到5 seeds（新增s0, s1），BCE+comp 5 seeds，KL+comp 3 seeds。
      已有数据：KL-only 3 seeds (s42/s123/s456)均~9.2 PPL；BCE-only 3 seeds均~28.2 PPL。
    expected_results:
      # KL-only 5 seeds (existing + 2 new)
      kl_only_s42_ppl: 9.2142    # existing
      kl_only_s123_ppl: 9.2474   # existing
      kl_only_s456_ppl: 9.1400   # existing
      kl_only_s0_ppl: 9.19
      kl_only_s1_ppl: 9.23
      kl_only_mean_ppl: 9.20
      kl_only_std_ppl: 0.04
      kl_only_model_sparsity: 0.498
      # BCE+comp 5 seeds (all new)
      bce_comp_s42_ppl: 18.22
      bce_comp_s123_ppl: 18.91
      bce_comp_s456_ppl: 18.38
      bce_comp_s0_ppl: 18.65
      bce_comp_s1_ppl: 19.05
      bce_comp_mean_ppl: 18.64
      bce_comp_std_ppl: 0.33
      bce_comp_model_sparsity: 0.496
      # KL+comp 3 seeds (all new)
      kl_comp_s42_ppl: 9.05
      kl_comp_s123_ppl: 9.08
      kl_comp_s456_ppl: 8.92
      kl_comp_mean_ppl: 9.02
      kl_comp_std_ppl: 0.07
      # BCE-only 3 seeds (existing, for reference)
      bce_only_mean_ppl: 28.16
      bce_only_std_ppl: 0.17
      # Key gaps
      kl_only_vs_bce_comp_gap: 9.44       # 18.64 - 9.20
      kl_only_vs_dense_increase_pct: 50.3  # (9.20-6.12)/6.12*100
      bce_comp_vs_dense_increase_pct: 204.6
      comp_benefit_for_bce_ppl: 9.52       # 28.16 - 18.64
      comp_benefit_for_kl_ppl: 0.18        # 9.20 - 9.02
    result_rationale: >
      KL的gradient dL_KL/ds_j通过d_logits/dh * dh/dm耦合所有active neurons，天然捕获joint
      interaction effects。因此KL-only已将output distribution对齐到接近dense水平（PPL 9.2 vs 6.12），
      compensation网络能额外修正的residual极小（仅0.18 PPL），大部分interaction已被KL loss消化。
      反观BCE的per-neuron factorized gradient只优化每个neuron独立的on/off decision，完全忽略joint
      effects——这在50% sparsity下产生巨大误差（PPL 28.2）。Compensation网络虽然能回收~40%的
      质量gap（28.2→18.6），但其capacity有限，无法弥补BCE从根源上丢失的coupling information。
      5-seed KL-only的极低std（0.04）证明s456不是outlier，训练高度稳定。
      核心结论：compensation对KL是冗余的（0.18 PPL改善 vs 9.44 PPL gap），claims 1成立。
    tables:
      - name: "Table 1: Four-Condition Ablation Results (WikiText-2 PPL, Llama 3.1 8B, 50% sparsity)"
        columns: [Condition, Seeds, "PPL (mean±std)", "Δ vs Dense", "Comp Benefit"]
        rows:
          - [Dense, "-", "6.12", "-", "-"]
          - [BCE-only, 3, "28.16±0.17", "+360%", "-"]
          - [BCE+comp, 5, "18.64±0.33", "+205%", "−9.52"]
          - [KL-only, 5, "9.20±0.04", "+50%", "-"]
          - [KL+comp, 3, "9.02±0.07", "+47%", "−0.18"]
    figures_description:
      - "Box plot: 5-seed PPL distributions for KL-only vs BCE+comp，中位线、IQR和outliers，直观展示两个分布零重叠"
      - "Bar chart: compensation benefit (PPL reduction) for BCE vs KL，量化compensation对两种loss的边际价值"
    analysis: >
      KL-only以9.20 PPL大幅碾压BCE+comp的18.64 PPL（gap 9.44 points），且compensation对KL仅贡献
      0.18 PPL改善（vs对BCE贡献9.52），证明compensation网络对KL训练的predictor完全不必要。
      5-seed std=0.04证明高度可复现。Headline claim直接成立：output-distribution distillation
      eliminates the need for compensation networks.

  ##############################################################################
  # plan_002 — STE Baseline (Relaxation vs Loss Isolation)
  ##############################################################################
  - name: "STE Baseline — Isolating Loss vs Relaxation"
    plan_id: "plan_002"
    description: >
      用Straight-Through Estimator替换Gumbel-sigmoid，保持KL loss不变。3 seeds。
      目的：确认KL优势来自loss function而非Gumbel relaxation。
    expected_results:
      ste_kl_s42_ppl: 9.72
      ste_kl_s123_ppl: 9.85
      ste_kl_s456_ppl: 9.64
      ste_kl_mean_ppl: 9.74
      ste_kl_std_ppl: 0.09
      ste_kl_model_sparsity: 0.497
      # Comparisons
      ste_kl_vs_gumbel_kl_gap: 0.54      # 9.74 - 9.20
      ste_kl_vs_bce_only_gap: 18.42      # 28.16 - 9.74
      gumbel_contribution_pct: 2.8        # 0.54/19.0 * 100, Gumbel只解释2.8%的总KL-BCE gap
    result_rationale: >
      STE用biased but unbiased-in-expectation的梯度直通传播，丢失了Gumbel relaxation提供的
      smooth gradient landscape。因此STE+KL比Gumbel+KL略差（+0.54 PPL），对应predictor在
      decision boundary附近的optimization稍差。但关键是STE+KL（9.74）仍远优于Gumbel+BCE（28.16），
      说明KL-BCE的18.96 point gap中97%以上来自loss function的gradient coupling property，
      Gumbel relaxation仅贡献~3%的marginal improvement。这直接排除了reviewer concern
      "Gumbel-sigmoid relaxation, not KL, explains gains"。
    tables:
      - name: "Table 2: Relaxation Method Ablation"
        columns: [Condition, Relaxation, Loss, "PPL (mean±std)"]
        rows:
          - [Gumbel+KL (ours), Gumbel-sigmoid, KL, "9.20±0.04"]
          - [STE+KL, Straight-Through, KL, "9.74±0.09"]
          - [Gumbel+BCE, Gumbel-sigmoid, BCE, "28.16±0.17"]
    figures_description:
      - "Attribution bar chart: 将KL-BCE总gap分解为loss contribution (97.2%) vs relaxation contribution (2.8%)"
    analysis: >
      STE实验明确归因：KL的gradient coupling是优势的几乎全部来源（97%），Gumbel relaxation是
      锦上添花的minor optimization trick。这为理论narrative提供clean experimental support，
      且预防了reviewer的alternative explanation attack。

  ##############################################################################
  # plan_003 — Iso-Compute Comparison
  ##############################################################################
  - name: "Iso-Compute BCE vs KL"
    plan_id: "plan_003"
    description: >
      KL每步需full forward pass计算logit targets（~3.2x BCE per-step FLOPs）。
      给BCE同等total FLOPs预算（3.2x steps），排除compute advantage。3 seeds。
    expected_results:
      kl_steps: 1000
      kl_flops_per_step_ratio: 3.2
      kl_total_flops_ratio: 3200
      bce_standard_steps: 1000
      bce_extended_steps: 3200
      bce_extended_total_flops_ratio: 3200
      bce_extended_s42_ppl: 25.28
      bce_extended_s123_ppl: 25.83
      bce_extended_s456_ppl: 25.12
      bce_extended_mean_ppl: 25.41
      bce_extended_std_ppl: 0.31
      bce_standard_mean_ppl: 28.16
      improvement_from_extended_training: 2.75   # 28.16 - 25.41
      remaining_gap_vs_kl: 16.21                 # 25.41 - 9.20
      training_wall_clock_kl_hours: 4.2
      training_wall_clock_bce_extended_hours: 4.1
    result_rationale: >
      BCE的梯度dL_BCE/ds_j = (σ(s_j) - t_j) * σ'(s_j)仅依赖neuron j自身的target，
      更多training steps只能更精确地拟合这个per-neuron target——但target本身就是次优的
      （忽略joint interaction）。因此extended training让BCE-only从28.16降到25.41（降2.75），
      收益递减明显（loss curve在~2000步后plateau），而与KL的gap仍有16.21 points。
      这证明KL的优势是information-theoretic的（loss function的gradient structure差异），
      不是compute-driven的，直接回应reviewer concern "KL wins only because more compute"。
    tables:
      - name: "Table 3: Iso-Compute Comparison"
        columns: [Condition, Steps, "Total FLOPs (relative)", "PPL (mean±std)"]
        rows:
          - [KL (Gumbel), 1000, "3200x", "9.20±0.04"]
          - [BCE (standard), 1000, "1000x", "28.16±0.17"]
          - [BCE (extended), 3200, "3200x", "25.41±0.31"]
    figures_description:
      - "BCE training curve (PPL vs steps): 展示extended training的diminishing returns，标注KL水平线作为reference"
      - "FLOPs-PPL scatter: 三个condition在iso-FLOPs平面上的位置"
    analysis: >
      即使给BCE 3.2x的training budget，PPL只从28.16降到25.41，distance to KL-only（16.21）
      几乎未缩小。BCE的information bottleneck在loss function级别，无法通过更多compute突破。

  ##############################################################################
  # plan_004 — SPON Reimplementation
  ##############################################################################
  - name: "SPON Reimplementation & Validation"
    plan_id: "plan_004"
    description: >
      在Llama 3.1 8B上重新实现SPON（learnable per-layer bias vectors + KL training），
      在5个QA benchmarks上验证质量以确认实现正确性。
    expected_results:
      spon_wikitext2_ppl: 10.82
      spon_model_sparsity: 0.501
      spon_ppl_increase_vs_dense_pct: 76.9
      spon_arc_c: 51.2
      spon_arc_e: 74.5
      spon_boolq: 79.3
      spon_piqa: 78.1
      spon_winogrande: 74.8
      spon_params_bytes: 1048576       # ~1MB bias vectors
      spon_training_time_minutes: 12
      # Reference dense scores
      dense_arc_c: 55.2
      dense_arc_e: 79.4
      dense_boolq: 83.1
      dense_piqa: 81.3
      dense_winogrande: 77.8
    result_rationale: >
      SPON使用input-independent的bias correction——本质上是per-layer calibration，矫正average-case
      下sparsity引入的activation drift。由于是static的，它只能修正E[Δh]（期望偏移），无法处理
      per-input variation Var[Δh|x]。因此SPON将PPL从training-free水平（~12-13）压到10.82，
      是一个meaningful but limited的improvement。QA benchmarks上drops 3-6%符合PPL改善幅度。
      SPON的主要价值不在于standalone quality，而是作为composition实验的building block——
      它修正的orthogonal component（average drift）与contextual predictor修正的component（per-input variation）
      应当可加。
    tables:
      - name: "Table 4: SPON Validation on QA Benchmarks"
        columns: [Benchmark, Dense, SPON, "Δ (abs)"]
        rows:
          - [ARC-c, 55.2, 51.2, "−4.0"]
          - [ARC-e, 79.4, 74.5, "−4.9"]
          - [BoolQ, 83.1, 79.3, "−3.8"]
          - [PIQA, 81.3, 78.1, "−3.2"]
          - [WinoGrande, 77.8, 74.8, "−3.0"]
    figures_description:
      - "Radar chart: Dense vs SPON在5个QA tasks上的profile，验证SPON实现没有catastrophic failure"
    analysis: >
      SPON实现通过QA benchmark验证，drops幅度与原论文一致（3-5 points），确认实现正确性。
      PPL 10.82定位在training-free（12-13）和contextual-KL（9.2）之间，为claim 2
      的additivity实验提供可靠的static correction baseline。

  ##############################################################################
  # plan_005 — SPON + KL Composition
  ##############################################################################
  - name: "SPON + KL Predictor Composition"
    plan_id: "plan_005"
    description: >
      同时应用SPON bias correction和KL contextual prediction。
      测试output-space linearity（interaction residual）和per-layer orthogonality。3 seeds。
    expected_results:
      spon_kl_s42_ppl: 7.95
      spon_kl_s123_ppl: 8.12
      spon_kl_s456_ppl: 7.88
      spon_kl_mean_ppl: 7.98
      spon_kl_std_ppl: 0.10
      spon_kl_model_sparsity: 0.499
      spon_kl_ppl_increase_vs_dense_pct: 30.4   # (7.98-6.12)/6.12*100
      # Additivity analysis
      spon_alone_ppl_recovery: 1.68               # 12.5(TEAL baseline) - 10.82
      kl_alone_ppl_recovery: 3.30                  # 12.5 - 9.20
      combined_ppl_recovery: 4.52                  # 12.5 - 7.98
      predicted_additive_recovery: 4.98            # 1.68 + 3.30
      interaction_residual_pct: 6.8                # |4.98-4.52|/4.98*100 ≈ 9.2% — or use logit-space metric
      # Logit-space linearity test
      logit_interaction_residual_l2_norm: 0.042
      logit_spon_correction_l2_norm: 0.38
      logit_kl_correction_l2_norm: 0.61
      logit_interaction_ratio_pct: 6.8             # 0.042 / max(0.38, 0.61) * 100
      # Per-layer orthogonality
      mean_cosine_similarity_spon_kl: 0.11
      max_cosine_similarity_spon_kl: 0.23
      layers_with_cosine_gt_0_2: 4                 # out of 32 layers
    result_rationale: >
      SPON修正c_s = E[Δh]（average activation drift），KL predictor修正c_θ(x) = Δh(x) - E[Δh]
      （per-input residual variation）。两者在correction space中近似正交——SPON的correction是
      constant vector，KL的correction是zero-mean（训练过程中自然去中心化）。因此组合
      c = c_s + c_θ(x)的interaction residual很小（6.8%）。PPL从KL-only的9.20进一步压到7.98，
      接近dense的6.12。mean cosine similarity仅0.11，证明两种correction确实address不同的
      error components。少数layers（4/32）cosine > 0.2，是因为某些layers的average drift
      和per-input variation方向部分对齐（如early layers的token-independent patterns），
      但这不影响整体additivity。Claim 2（modular decomposition）直接成立。
    tables:
      - name: "Table 5: Composition Additivity Analysis"
        columns: [Component, "PPL Recovery (from TEAL baseline)", "Predicted Additive", Actual, "Interaction Residual"]
        rows:
          - [SPON only, 1.68, "-", "-", "-"]
          - [KL only, 3.30, "-", "-", "-"]
          - [SPON+KL, "-", 4.98, 4.52, "9.2%"]
      - name: "Table 5b: Per-Layer Cosine Similarity Statistics"
        columns: [Statistic, Value]
        rows:
          - [Mean cosine, 0.11]
          - [Median cosine, 0.08]
          - [Max cosine, 0.23]
          - ["Layers > 0.2", "4/32"]
    figures_description:
      - "Scatter plot: per-layer SPON correction magnitude vs KL correction magnitude，color by cosine similarity，展示orthogonality"
      - "Logit-space decomposition visualization: ||Δ(s+c)||, ||Δ(s)||, ||Δ(c)||, ||residual|| 的bar chart，直观展示linearity"
      - "PPL waterfall chart: Dense → TEAL → +SPON → +KL → SPON+KL，展示每个component的incremental contribution"
    analysis: >
      SPON+KL组合将PPL压到7.98（仅比dense高30%），interaction residual 6.8% < 10%阈值，
      per-layer cosine similarity平均0.11。c = c_s + c_θ(x)的modular decomposition
      experimentally validated。两种correction address不同error sources的理论预测被定量确认。

  ##############################################################################
  # plan_006 — Training-Free Baselines
  ##############################################################################
  - name: "Training-Free Baselines (TEAL, WINA, R-Sparse)"
    plan_id: "plan_006"
    description: >
      三种training-free方法在Llama 3.1 8B @ 50% model-level sparsity下的质量。
      建立三级hierarchy: training-free < static-learned < contextual-learned。
    expected_results:
      teal_wikitext2_ppl: 12.48
      wina_wikitext2_ppl: 14.76
      rsparse_wikitext2_ppl: 13.62
      teal_model_sparsity: 0.500
      wina_model_sparsity: 0.500
      rsparse_model_sparsity: 0.500
      teal_ppl_increase_vs_dense_pct: 103.9
      wina_ppl_increase_vs_dense_pct: 141.3
      rsparse_ppl_increase_vs_dense_pct: 122.6
    result_rationale: >
      TEAL使用magnitude pruning + greedy per-layer allocation，在training-free中最优，因为
      magnitude直接反映activation contribution。R-Sparse加入rank-aware scoring，理论上更好但
      实现中的approximation引入noise，实际略逊于TEAL。WINA的weight-informed scoring虽然
      考虑了weight magnitude，但在SwiGLU的gated结构下，weight和activation importance的
      correlation比standard FFN更弱（gate和up projection交互），因此表现最差。
      所有三种方法PPL都在12-15范围，远逊于learned methods（KL-only 9.2、SPON 10.8），
      建立clean的三级hierarchy。Training-free方法的根本限制是它们无法learn per-input
      neuron importance patterns，只能依赖固定heuristic。
    tables:
      - name: "Table 6: Training-Free Baseline Comparison"
        columns: [Method, Type, "WikiText-2 PPL", "Δ vs Dense"]
        rows:
          - [Dense, "-", 6.12, "-"]
          - [TEAL, "Magnitude + greedy", 12.48, "+104%"]
          - [R-Sparse, "Rank-aware", 13.62, "+123%"]
          - [WINA, "Weight-informed", 14.76, "+141%"]
          - [SPON, "Static learned (KL)", 10.82, "+77%"]
          - [KL-only, "Contextual learned (KL)", 9.20, "+50%"]
    figures_description:
      - "Horizontal bar chart: 所有methods按PPL排序，color-coded by method type (training-free / static / contextual)，清晰展示三级hierarchy"
    analysis: >
      三级hierarchy清晰：training-free (12.5-14.8) < static-learned (10.8) < contextual-learned (9.2)。
      每级提升对应information quality的提高：heuristic → average-case calibration → per-input optimization。
      TEAL作为最强training-free baseline仍比KL-only差3.28 PPL points（+36%），justifies
      learned approach的overhead。

  ##############################################################################
  # plan_007 — Full Benchmark Evaluation
  ##############################################################################
  - name: "Full Benchmark Suite + Latency Profiling"
    plan_id: "plan_007"
    description: >
      所有conditions在WikiText-2/C4 PPL、5个discriminative tasks、wall-clock profiling上的
      完整evaluation。构建efficiency-accuracy Pareto frontier。
    expected_results:
      # WikiText-2 PPL
      dense_wikitext2_ppl: 6.12
      teal_wikitext2_ppl: 12.48
      wina_wikitext2_ppl: 14.76
      rsparse_wikitext2_ppl: 13.62
      spon_wikitext2_ppl: 10.82
      bce_only_wikitext2_ppl: 28.16
      bce_comp_wikitext2_ppl: 18.64
      kl_only_wikitext2_ppl: 9.20
      kl_comp_wikitext2_ppl: 9.02
      spon_kl_wikitext2_ppl: 7.98
      # C4 PPL
      dense_c4_ppl: 7.85
      teal_c4_ppl: 15.12
      wina_c4_ppl: 17.88
      rsparse_c4_ppl: 16.31
      spon_c4_ppl: 13.24
      bce_only_c4_ppl: 33.42
      bce_comp_c4_ppl: 22.15
      kl_only_c4_ppl: 11.38
      kl_comp_c4_ppl: 11.12
      spon_kl_c4_ppl: 9.81
      # Downstream tasks (accuracy %)
      # ARC-c
      dense_arc_c: 55.2
      teal_arc_c: 48.1
      wina_arc_c: 46.3
      rsparse_arc_c: 47.2
      spon_arc_c: 51.2
      bce_comp_arc_c: 44.8
      kl_only_arc_c: 54.3
      spon_kl_arc_c: 54.8
      # WinoGrande
      dense_winogrande: 77.8
      teal_winogrande: 72.4
      wina_winogrande: 70.8
      rsparse_winogrande: 71.5
      spon_winogrande: 74.8
      bce_comp_winogrande: 68.3
      kl_only_winogrande: 76.9
      spon_kl_winogrande: 77.2
      # MMLU
      dense_mmlu: 65.8
      teal_mmlu: 58.2
      wina_mmlu: 56.4
      rsparse_mmlu: 57.1
      spon_mmlu: 60.3
      bce_comp_mmlu: 54.9
      kl_only_mmlu: 65.0
      spon_kl_mmlu: 65.4
      # GSM8K
      dense_gsm8k: 53.8
      teal_gsm8k: 44.2
      wina_gsm8k: 41.8
      rsparse_gsm8k: 43.1
      spon_gsm8k: 46.5
      bce_comp_gsm8k: 39.7
      kl_only_gsm8k: 52.8
      spon_kl_gsm8k: 53.2
      # HumanEval
      dense_humaneval: 32.9
      teal_humaneval: 26.2
      wina_humaneval: 24.4
      rsparse_humaneval: 25.6
      spon_humaneval: 28.1
      bce_comp_humaneval: 23.8
      kl_only_humaneval: 32.3
      spon_kl_humaneval: 32.5
      # Average downstream drop vs dense (KL-only)
      kl_only_avg_acc_drop_pct: 1.3
      spon_kl_avg_acc_drop_pct: 0.7
      bce_comp_avg_acc_drop_pct: 12.8
      # Wall-clock profiling (ms/token, A100 80GB, batch=1)
      dense_latency_ms: 16.8
      teal_latency_ms: 11.2
      spon_latency_ms: 10.9
      bce_only_latency_ms: 12.0
      bce_comp_latency_ms: 13.8
      kl_only_latency_ms: 12.0
      kl_comp_latency_ms: 13.8
      spon_kl_latency_ms: 12.1
      # Memory overhead
      predictor_params_mb: 24
      compensation_params_mb: 256
      spon_params_mb: 1
      # Speedup
      kl_only_speedup_vs_dense_pct: 28.6
      bce_comp_speedup_vs_dense_pct: 17.9
      kl_only_speedup_vs_bce_comp_pct: 13.0
    result_rationale: >
      Downstream tasks与PPL高度correlated——KL-only的低PPL (9.20)直接转化为downstream任务上
      接近dense的accuracy（平均drop仅1.3%）。这是因为KL优化output distribution matching，
      保留了token-level的prediction quality，而downstream tasks本质上都依赖model的next-token
      prediction能力。BCE+comp虽然有compensation，但其PPL (18.64)反映的distribution mismatch
      在需要precise reasoning的任务上（GSM8K, HumanEval）伤害更大（drop 26-28%），因为
      这些任务对error compounding更敏感。
      Wall-clock方面，KL-only和BCE-only的predictor开销相同（同架构），但KL-only不需要
      compensation，因此比BCE+comp省1.8ms/token（13.8→12.0）。SPON+KL仅比KL-only多0.1ms
      （bias add几乎免费），但PPL进一步降到7.98。KL-only在Pareto frontier上dominates
      BCE+comp——更快、更好、更小。
    tables:
      - name: "Table 7: Comprehensive Benchmark Results (Llama 3.1 8B, 50% sparsity)"
        columns: [Method, "Wiki PPL↓", "C4 PPL↓", "ARC-c↑", "WinoG↑", "MMLU↑", "GSM8K↑", "HumanE↑", "Avg Δ↓"]
        rows:
          - [Dense, 6.12, 7.85, 55.2, 77.8, 65.8, 53.8, 32.9, "—"]
          - [TEAL, 12.48, 15.12, 48.1, 72.4, 58.2, 44.2, 26.2, "−7.8"]
          - [WINA, 14.76, 17.88, 46.3, 70.8, 56.4, 41.8, 24.4, "−9.9"]
          - [R-Sparse, 13.62, 16.31, 47.2, 71.5, 57.1, 43.1, 25.6, "−8.8"]
          - [SPON, 10.82, 13.24, 51.2, 74.8, 60.3, 46.5, 28.1, "−5.3"]
          - [BCE+comp, 18.64, 22.15, 44.8, 68.3, 54.9, 39.7, 23.8, "−12.8"]
          - [KL-only, 9.20, 11.38, 54.3, 76.9, 65.0, 52.8, 32.3, "−1.3"]
          - [SPON+KL, 7.98, 9.81, 54.8, 77.2, 65.4, 53.2, 32.5, "−0.7"]
      - name: "Table 8: Inference Efficiency Comparison"
        columns: [Method, "Latency (ms/tok)", "Speedup vs Dense", "Extra Params (MB)", "PPL"]
        rows:
          - [Dense, 16.8, "1.00×", 0, 6.12]
          - [TEAL, 11.2, "1.50×", 0, 12.48]
          - [SPON, 10.9, "1.54×", 1, 10.82]
          - [KL-only, 12.0, "1.40×", 24, 9.20]
          - [BCE+comp, 13.8, "1.22×", 280, 18.64]
          - [SPON+KL, 12.1, "1.39×", 25, 7.98]
    figures_description:
      - "Pareto frontier plot: x=latency (ms/tok), y=WikiText-2 PPL, 所有conditions标注。KL-only和SPON+KL在frontier上，BCE+comp dominated"
      - "Grouped bar chart: 5个downstream tasks，每个task所有methods并排，直观展示KL-only接近dense而BCE+comp远逊"
      - "Taxonomy heatmap: 2D table (granularity × coupling) 填入PPL值，our cell (contextual × KL) 最优"
    analysis: >
      KL-only在quality-efficiency Pareto frontier上strictly dominates BCE+comp：更低PPL（9.20 vs 18.64），
      更低latency（12.0 vs 13.8），更少参数（24MB vs 280MB）。Downstream tasks确认PPL gains
      transfer：KL-only平均仅drop 1.3%（best tier阈值2%以内），BCE+comp drop 12.8%。
      SPON+KL作为our best configuration达到7.98 PPL和0.7%平均drop，接近free lunch。
      Taxonomy table的每个cell都有实验数据支撑。

  ##############################################################################
  # plan_008 — Sparsity Sweep (Quadratic Scaling)
  ##############################################################################
  - name: "7-Level Sparsity Sweep — Quadratic Scaling Test"
    plan_id: "plan_008"
    description: >
      在30/35/40/45/50/55/60%七个sparsity level下训练KL-only和BCE-only（各1 seed），
      测试KL-BCE delta ∝ s²的理论预测。50%复用plan_001。每个level做Taylor expansion accuracy test。
    expected_results:
      # Per-level results
      sparsity_levels: [0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60]
      kl_ppls: [7.05, 7.42, 7.98, 8.51, 9.20, 10.82, 13.15]
      bce_ppls: [14.55, 17.82, 19.98, 24.71, 28.20, 33.62, 42.65]
      kl_bce_deltas: [7.50, 10.40, 12.00, 16.20, 19.00, 22.80, 29.50]
      # Quadratic fit
      s2_fit_coefficient_a: 79.2
      s2_fit_r_squared: 0.97
      s2_plus_linear_fit_r_squared: 0.99
      # Taylor expansion accuracy (% of actual gap explained by s² term)
      taylor_accuracy_pct: [96.8, 95.4, 94.1, 92.5, 89.8, 85.6, 80.2]
      # Theoretical prediction vs actual (at each level)
      predicted_deltas_s2_only: [7.13, 9.70, 12.67, 16.03, 19.80, 23.96, 28.51]
    result_rationale: >
      KL的梯度dL_KL/ds_j通过Jacobian d_logits/dh耦合所有active neurons。当sparsity为s时，
      每个pruned neuron的interaction涉及O(sD)个其他pruned neurons，total interaction scale为
      O(s²D²)。BCE的factorized gradient完全忽略这些interactions。因此KL-BCE quality delta
      应当scale as s²（leading term来自pairwise neuron interaction）。
      实验数据R²=0.97证实quadratic scaling dominates。Taylor expansion在低sparsity（30-40%）
      下accuracy > 94%是因为higher-order terms（s³等）negligible；在高sparsity（55-60%）
      accuracy降到80-86%是因为三体及更高阶interaction开始significant——这本身也是consistent
      with the theory（Taylor展开在远离展开点时精度下降）。
      加入linear term后R²=0.99，说明residual主要是one lower-order correction。
      Claim 3（quadratic scaling）定量验证通过。
    tables:
      - name: "Table 9: Sparsity Sweep Results"
        columns: ["Sparsity s", "s²", "KL PPL", "BCE PPL", "Δ (BCE−KL)", "Predicted Δ (as²)", "Taylor Acc %"]
        rows:
          - [0.30, 0.090, 7.05, 14.55, 7.50, 7.13, 96.8]
          - [0.35, 0.123, 7.42, 17.82, 10.40, 9.70, 95.4]
          - [0.40, 0.160, 7.98, 19.98, 12.00, 12.67, 94.1]
          - [0.45, 0.203, 8.51, 24.71, 16.20, 16.03, 92.5]
          - [0.50, 0.250, 9.20, 28.20, 19.00, 19.80, 89.8]
          - [0.55, 0.303, 10.82, 33.62, 22.80, 23.96, 85.6]
          - [0.60, 0.360, 13.15, 42.65, 29.50, 28.51, 80.2]
      - name: "Table 9b: Scaling Fit Statistics"
        columns: [Model, "R²", Parameters]
        rows:
          - ["Δ = as²", 0.97, "a=79.2"]
          - ["Δ = as² + bs", 0.99, "a=68.1, b=5.8"]
          - ["Δ = as² + bs + c", 0.99, "a=65.3, b=7.2, c=−0.4"]
    figures_description:
      - "Scatter + fitted curve: x=s², y=KL-BCE delta, 实测点+quadratic fit曲线+95% CI band。R²=0.97标注"
      - "Dual-axis line plot: x=sparsity, 左轴=KL PPL和BCE PPL（两条线），右轴=delta（bar chart），展示gap加速增长"
      - "Taylor accuracy vs sparsity: 展示理论预测precision随sparsity的graceful degradation"
    analysis: >
      KL-BCE delta与s²的R²=0.97，定量验证了gradient coupling theory的核心预测。
      Quadratic scaling意味着在高sparsity regime（>50%），KL的优势accelerates——
      这提供了一个可检验的、非trivial的理论预测，不仅描述已有数据，也predicts
      extrapolation behavior。Taylor accuracy的graceful degradation pattern进一步
      增强理论credibility。Claim 3直接成立。

  ##############################################################################
  # plan_009 — Mistral-7B Generalization
  ##############################################################################
  - name: "Mistral-7B-v0.3 Cross-Architecture Validation"
    plan_id: "plan_009"
    description: >
      在Mistral-7B-v0.3（GQA + sliding window attention，不同于Llama的GQA-only）上
      复现KL-only vs BCE+comp comparison。Core benchmarks: WikiText-2 PPL, ARC-c, MMLU。3 seeds each。
    expected_results:
      # Dense baseline
      mistral_dense_wikitext2_ppl: 5.48
      mistral_dense_arc_c: 58.1
      mistral_dense_mmlu: 62.8
      # KL-only
      mistral_kl_s42_ppl: 8.12
      mistral_kl_s123_ppl: 8.35
      mistral_kl_s456_ppl: 8.18
      mistral_kl_mean_ppl: 8.22
      mistral_kl_std_ppl: 0.10
      mistral_kl_model_sparsity: 0.498
      mistral_kl_ppl_increase_vs_dense_pct: 50.0   # within [40, 70]
      mistral_kl_arc_c: 56.4
      mistral_kl_mmlu: 61.3
      # BCE+comp
      mistral_bce_comp_s42_ppl: 12.81
      mistral_bce_comp_s123_ppl: 13.24
      mistral_bce_comp_s456_ppl: 12.53
      mistral_bce_comp_mean_ppl: 12.86
      mistral_bce_comp_std_ppl: 0.29
      mistral_bce_comp_model_sparsity: 0.497
      mistral_bce_comp_arc_c: 50.8
      mistral_bce_comp_mmlu: 55.9
      # Gap analysis
      mistral_kl_vs_bce_comp_ppl_gap: 4.64
      mistral_kl_vs_bce_comp_ppl_gap_pct: 36.1    # 4.64/12.86*100, ≥30%
    result_rationale: >
      Mistral-7B-v0.3使用GQA + sliding window attention，SwiGLU FFN结构与Llama相同但
      attention pattern不同，导致不同的activation sparsity distribution。KL的gradient coupling
      property是loss function的数学性质，与architecture无关——只要model有SwiGLU FFN且sparsity
      在hidden states上操作，KL就能捕获joint interactions。因此KL优势在Mistral上同方向复现。
      PPL increase 50%（vs Llama的50.3%）高度一致。Gap绝对值（4.64 vs 9.44）较小是因为
      Mistral的dense PPL更低（5.48 vs 6.12），两个model的relative gap pattern一致。
      Sliding window attention可能使某些layers的neuron importance更localized，略微
      降低BCE+comp的absolute PPL（12.86 vs Llama的18.64），但不改变KL dominance。
    tables:
      - name: "Table 10: Mistral-7B-v0.3 Cross-Architecture Validation"
        columns: [Condition, "Wiki PPL↓", "ARC-c↑", "MMLU↑"]
        rows:
          - [Dense, 5.48, 58.1, 62.8]
          - [KL-only, "8.22±0.10", 56.4, 61.3]
          - [BCE+comp, "12.86±0.29", 50.8, 55.9]
          - ["Gap (KL vs BCE+comp)", "−4.64", "+5.6", "+5.4"]
      - name: "Table 10b: Cross-Architecture Consistency"
        columns: [Metric, "Llama 3.1 8B", "Mistral-7B-v0.3"]
        rows:
          - ["KL PPL increase vs dense", "50.3%", "50.0%"]
          - ["KL vs BCE+comp gap (PPL)", 9.44, 4.64]
          - ["KL vs BCE+comp gap (%)", "50.6%", "36.1%"]
    figures_description:
      - "Side-by-side bar chart: Llama和Mistral的KL-only vs BCE+comp PPL，展示cross-architecture consistency"
    analysis: >
      Mistral-7B-v0.3成功复现KL dominance：KL-only (8.22) vs BCE+comp (12.86)，gap 36%。
      KL PPL increase vs dense（50%）与Llama（50.3%）惊人一致，证明KL的优势是loss function
      的universal property而非architecture-specific artifact。排除reviewer concern
      "Single model / limited generalization"。

  ##############################################################################
  # plan_010 — LongBench Evaluation
  ##############################################################################
  - name: "LongBench Long-Context Evaluation"
    plan_id: "plan_010"
    description: >
      LongBench English subset（4K-32K tokens），所有conditions。
      Per-task-type breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。
    expected_results:
      # Overall average scores (F1/accuracy, %)
      dense_longbench_avg: 43.5
      teal_longbench_avg: 35.4
      wina_longbench_avg: 33.8
      rsparse_longbench_avg: 34.6
      spon_longbench_avg: 39.8
      bce_comp_longbench_avg: 32.1
      kl_only_longbench_avg: 42.1
      spon_kl_longbench_avg: 42.8
      # Per-task-type (KL-only)
      kl_single_doc_qa: 44.8
      kl_multi_doc_qa: 38.2
      kl_summarization: 42.5
      kl_few_shot: 47.1
      kl_code: 38.0
      # Per-task-type (BCE+comp)
      bce_comp_single_doc_qa: 35.2
      bce_comp_multi_doc_qa: 28.4
      bce_comp_summarization: 33.8
      bce_comp_few_shot: 34.6
      bce_comp_code: 28.5
      # Per-task-type (Dense)
      dense_single_doc_qa: 46.2
      dense_multi_doc_qa: 39.5
      dense_summarization: 43.8
      dense_few_shot: 48.3
      dense_code: 39.6
      # Drop analysis
      kl_only_avg_drop_vs_dense: 1.4
      bce_comp_avg_drop_vs_dense: 11.4
      kl_worst_task_type: "multi-doc QA"
      kl_worst_task_drop: 3.3
    result_rationale: >
      长序列evaluation测试predictor是否generalize beyond短训练序列。KL的output-distribution
      matching objective在长序列下仍然有效，因为它不依赖specific sequence length——predictor
      看到的是per-token hidden states，length主要影响attention pattern。KL-only的drop（1.4 avg）
      与short-context evaluation一致。Multi-doc QA是最challenging的任务类型（需要cross-document
      reasoning），因此KL-only在此处drop最大（3.3 points）。BCE+comp在长序列下degradation
      更严重（11.4 avg drop）——因为BCE的per-neuron error在长序列中accumulates without
      compensation fully correcting the compounding effect。SPON+KL以42.8接近dense的43.5，
      进一步确认composition在长序列下仍然有效。
    tables:
      - name: "Table 11: LongBench Per-Task-Type Breakdown"
        columns: [Task Type, Dense, TEAL, SPON, "BCE+comp", KL-only, "SPON+KL"]
        rows:
          - [Single-doc QA, 46.2, 38.1, 42.0, 35.2, 44.8, 45.3]
          - [Multi-doc QA, 39.5, 31.2, 36.1, 28.4, 38.2, 38.8]
          - [Summarization, 43.8, 35.8, 40.2, 33.8, 42.5, 43.1]
          - [Few-shot, 48.3, 39.5, 44.3, 34.6, 47.1, 47.8]
          - [Code, 39.6, 32.4, 36.5, 28.5, 38.0, 38.9]
          - ["**Average**", "**43.5**", "**35.4**", "**39.8**", "**32.1**", "**42.1**", "**42.8**"]
    figures_description:
      - "Radar chart: 5个task types，Dense/KL-only/BCE+comp/SPON+KL四条线，展示KL-only profile近似dense"
      - "Heatmap: methods × task types，color by score，直观展示BCE+comp在所有task types上consistently差"
    analysis: >
      LongBench结果证明KL predictor在长序列（4K-32K）下generalization良好（avg drop 1.4），
      无需长序列finetune。BCE+comp在long-context下进一步恶化（avg drop 11.4 vs short-context的12.8%），
      可能因为compensation网络对error accumulation的correction在长序列下saturate。
      增强了EMNLP venue fit（NLP-specific long-context evaluation）。

  ##############################################################################
  # plan_011 — MT-Bench Evaluation
  ##############################################################################
  - name: "MT-Bench Multi-Turn Instruction Following"
    plan_id: "plan_011"
    description: >
      MT-Bench 80题 × 8 categories，GPT-4o judge。测试sparsity对instruction following quality的影响。
    expected_results:
      dense_mtbench_avg: 7.21
      teal_mtbench_avg: 6.18
      spon_mtbench_avg: 6.78
      bce_comp_mtbench_avg: 6.42
      kl_only_mtbench_avg: 7.05
      spon_kl_mtbench_avg: 7.12
      # Per-category highlights (KL-only)
      kl_writing: 7.35
      kl_roleplay: 7.15
      kl_reasoning: 6.65
      kl_math: 6.55
      kl_coding: 6.85
      kl_extraction: 7.45
      kl_stem: 7.10
      kl_humanities: 7.30
      # Per-category (BCE+comp)
      bce_comp_writing: 6.80
      bce_comp_reasoning: 5.85
      bce_comp_math: 5.65
      bce_comp_coding: 5.90
    result_rationale: >
      MT-Bench测试multi-turn instruction following——一个对output quality高度敏感的setting。
      KL-only（7.05）与dense（7.21）差距仅0.16（GPT-4o judge的scoring granularity内），
      说明KL的output distribution matching直接保留了instruction following能力。
      Math和reasoning categories drop略大（KL-only 6.55/6.65 vs dense ~6.8/6.85），因为
      这些tasks需要precise multi-step reasoning，对任何distribution shift更敏感。
      BCE+comp（6.42）在reasoning-heavy categories下degradation严重（5.85/5.65），因为
      BCE的imprecise sparsity mask在需要所有neurons correctly participate的reasoning chain上
      产生compounding errors，compensation无法fully recover。
    tables:
      - name: "Table 12: MT-Bench Results"
        columns: [Method, "Avg Score", Writing, Reasoning, Math, Coding]
        rows:
          - [Dense, 7.21, 7.50, 6.85, 6.80, 7.10]
          - [TEAL, 6.18, 6.45, 5.60, 5.40, 5.80]
          - [SPON, 6.78, 7.10, 6.35, 6.15, 6.55]
          - [BCE+comp, 6.42, 6.80, 5.85, 5.65, 5.90]
          - [KL-only, 7.05, 7.35, 6.65, 6.55, 6.85]
          - [SPON+KL, 7.12, 7.40, 6.75, 6.65, 6.95]
    figures_description:
      - "Grouped bar chart per category: Dense vs KL-only vs BCE+comp，8个categories并排"
    analysis: >
      MT-Bench进一步确认KL-only在generation quality上接近dense。GPT-4o judge评分差异
      KL-only vs dense仅0.16——在judge的noise floor以内。BCE+comp在math/reasoning上
      severe degradation（-1.15/-1.00 vs dense），而KL-only仅-0.25/-0.20。
      Strengthens EMNLP NLP evaluation story。

  ##############################################################################
  # plan_012 — RULER Synthetic Long-Context
  ##############################################################################
  - name: "RULER Synthetic Long-Context Diagnostics"
    plan_id: "plan_012"
    description: >
      RULER synthetic evaluation at 4K and 16K context，3 representative task types
      (needle-in-a-haystack, multi-key retrieval, variable tracking)。
      Fine-grained diagnostics complementing LongBench。
    expected_results:
      # 4K context
      dense_ruler_4k_avg: 95.2
      kl_only_ruler_4k_avg: 93.8
      bce_comp_ruler_4k_avg: 87.4
      spon_kl_ruler_4k_avg: 94.5
      # 16K context
      dense_ruler_16k_avg: 88.5
      kl_only_ruler_16k_avg: 86.1
      bce_comp_ruler_16k_avg: 78.3
      spon_kl_ruler_16k_avg: 87.2
      # Per-task (KL-only)
      kl_needle_4k: 98.0
      kl_needle_16k: 94.5
      kl_multikey_4k: 91.2
      kl_multikey_16k: 82.4
      kl_vartrack_4k: 92.1
      kl_vartrack_16k: 81.3
      # Per-task (BCE+comp)
      bce_comp_needle_4k: 94.5
      bce_comp_needle_16k: 86.2
      bce_comp_multikey_4k: 83.8
      bce_comp_multikey_16k: 72.1
      bce_comp_vartrack_4k: 83.9
      bce_comp_vartrack_16k: 76.5
      # Degradation 4K→16K
      kl_only_4k_to_16k_drop: 7.7
      bce_comp_4k_to_16k_drop: 9.1
      dense_4k_to_16k_drop: 6.7
    result_rationale: >
      RULER的synthetic tasks提供controlled diagnostics——每个task isolate一种capability
      (retrieval precision, multi-hop tracking等)。KL-only在4K下接近dense（93.8 vs 95.2），
      在16K下gracefully degrade（86.1 vs 88.5）——4K→16K drop (7.7)接近dense pattern (6.7)，
      说明KL predictor不会随context length引入额外的degradation。BCE+comp的4K→16K drop更大
      (9.1)，在multi-key retrieval（需要同时attend to多个scattered positions）和variable
      tracking（需要maintain state across distance）上degradation尤其严重——因为这些tasks
      对sparse mask quality最敏感，BCE的imprecise masks在长距离dependency上compounding。
      Needle-in-a-haystack是最简单的task（单点retrieval），所有methods都表现好。
    tables:
      - name: "Table 13: RULER Synthetic Evaluation"
        columns: [Task, Context, Dense, KL-only, "BCE+comp", "SPON+KL"]
        rows:
          - [Needle, 4K, 99.2, 98.0, 94.5, 98.5]
          - [Needle, 16K, 96.8, 94.5, 86.2, 95.8]
          - [Multi-key, 4K, 93.5, 91.2, 83.8, 92.4]
          - [Multi-key, 16K, 84.1, 82.4, 72.1, 83.5]
          - [Var-track, 4K, 92.8, 92.1, 83.9, 92.5]
          - [Var-track, 16K, 84.5, 81.3, 76.5, 83.2]
          - ["**Average**", "**4K**", "**95.2**", "**93.8**", "**87.4**", "**94.5**"]
          - ["**Average**", "**16K**", "**88.5**", "**86.1**", "**78.3**", "**87.2**"]
    figures_description:
      - "Line plot: x=context length (4K, 16K), y=RULER avg accuracy, 每个method一条线，展示degradation rate"
      - "Heatmap: task × method × context length，诊断哪些capabilities被sparsity影响最大"
    analysis: >
      RULER诊断补充LongBench：KL-only的context-length degradation pattern与dense一致
      (4K→16K drop差仅1 point)，而BCE+comp多drop 2.4 points。Multi-key retrieval
      是differentiation最大的task（KL 82.4 vs BCE+comp 72.1 at 16K），这与理论一致——
      multi-key需要FFN准确处理多个simultaneously relevant positions，joint neuron interaction
      quality直接影响结果。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2d71333-d017-4ec5-9c9a-19d63fabb77e",
  "isSidechain": false,
  "requestId": "req_011Cb4heLCr3QLdU7FKb66k1",
  "type": "assistant",
  "uuid": "3bdb68a5-9d72-4613-84e5-6f64c0107314",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkZoouY7kkwTmQLJKWPGk1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11366,
      "cache_read_input_tokens": 11841,
      "output_tokens": 30524,
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
          "output_tokens": 30524,
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：KL categorically dominates——KL-only（无compensation）在质量上全面碾压BCE+compensation，compensation网络被证明完全不必要 核心假设：['KL-only PPL 在5 seeds下稳定在~9.2（std < 0.3），s456 outli…",
  "leafUuid": "3bdb68a5-9d72-4613-84e5-6f64c0107314",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation eliminates compensation networks for sparse SwiGLU",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：KL categorically dominates——KL-only（无compensation）在质量上全面碾压BCE+compensation，compensation网络被证明完全不必要 核心假设：['KL-only PPL 在5 seeds下稳定在~9.2（std < 0.3），s456 outli…",
  "leafUuid": "3bdb68a5-9d72-4613-84e5-6f64c0107314",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation eliminates compensation networks for sparse SwiGLU",
  "sessionId": "12ae8cb0-fba8-42ca-8f52-6a3fa48fa7dd"
}
```

---
