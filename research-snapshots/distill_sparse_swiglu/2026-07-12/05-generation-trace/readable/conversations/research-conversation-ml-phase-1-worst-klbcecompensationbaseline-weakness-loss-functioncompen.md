# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：KL优势是假象——BCE缺compensation导致的baseline weakness，而非loss function的内在优势。加上compen

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/9c35e2d0-bc09-4233-9980-737e00198e60.jsonl`
- **Structured JSON:** [`9748760bb9202fe5ed86.json`](../../sessions/97/9748760bb9202fe5ed86.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T17:12:06.046Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T17:12:06.046Z",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：KL优势是假象——BCE缺compensation导致的baseline weakness，而非loss function的内在优势。加上compensation后BCE追平或反超KL\n核心假设：['KL-only PPL 方差比MVP显示的更大（std > 0.8，部分seeds > 11），稳定性存疑', 'BCE+compensation充分收敛到 ≤ 9.5 PPL，完全弥合与KL的差距甚至反超', 'SPON + KL有显著interaction effects，不满足可加性', 'KL-BCE delta不服从s²规律（R² < 0.80），linear fit同样好，理论叙事不成立', 'Mistral结果不一致或方向相反', 'STE baseline与Gumbel KL持平→relaxation method比loss function重要，因果归因错误']\n关键指标范围：{'kl_only_wikitext2_ppl': [9.5, 12.0], 'kl_only_ppl_std': [0.8, 2.0], 'bce_comp_wikitext2_ppl': [8.5, 10.0], 'spon_kl_wikitext2_ppl': [9.0, 11.0], 'kl_vs_bce_comp_ppl_gap': [-1.5, 0.5], 'downstream_acc_drop_vs_dense_pct': [5, 10], 's2_scaling_r2': [0.5, 0.8], 'mistral_kl_ppl_increase_vs_dense_pct': [60, 120]}\n叙事方向：核心claim（KL eliminates compensation）不成立。Reframe策略，不降级venue：(1) 将paper重心转向'首个系统性taxonomy of training signals × correction granularity for activation sparsity'——四象限ablation grid本身就是贡献，填补了文献空白；(2) 叙事从'A beats B'转为'characterization study'：'Both KL-only and BCE+compensation reach near-dense quality at 50% sparsity through fundamentally different mechanisms——we provide the first empirical decomposition of when and why each succeeds'；(3) SPON + contextual composition分析即使不完美可加也可作为standalone empirical finding。EMNLP Efficient Methods track重视thorough empirical methodology，paper_framing中预设的four-quadrant design正是为此scenario准备的。关键是honest framing而非overclaiming。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: distill_sparse_swiglu\nfocus: MVP showed massive KL vs BCE gap (12.52 vs 44.05 PPL). Key uncertainty: will BCE+compensation close this gap? If yes, headline shifts to \"KL eliminates compensation overhead\" rather than \"KL is categorically better\". Also: seed s456 is outlier (13.58 vs 12.08/11.91), variance needs attention.\n\n## paper_framing.md\n\n# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)\n\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\n\n3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\n\n- **Our framing / headline question**: \"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\n\n- **Headline result template**: \"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\n\n2. **\"KL wins only because more compute\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\n\n5. **\"Effect size may not hold on downstream tasks\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:\n    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline\n    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds\n    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and\n    BCE-only 3 seeds (mvp_bce_s42/s123/s456).\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_ids:\n  - mvp_kl_norm_v2_s42\n  - mvp_kl_norm_v2_s123\n  - mvp_kl_norm_v2_s456\n  - mvp_bce_s42\n  - mvp_bce_s123\n  - mvp_bce_s456\n  remaining_runs:\n  - KL-only 2 additional seeds (s0, s1) for 5-seed headline\n  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)\n  - KL+comp 3 seeds (s42, s123, s456)\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).\n    Isolates whether KL advantage comes from loss function or relaxation method. 3\n    seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs\n    (KL requires full forward pass for output logits, BCE can use cached targets).\n    Report per-step FLOPs and total training time for both. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL\n    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,\n    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'SPON + KL predictor composition experiment. Apply SPON bias correction\n    AND KL contextual prediction simultaneously. Output-space linearity test: ||Delta_logits(s+c)\n    - Delta_logits(s) - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality\n    analysis. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  - plan_004\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:\n    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),\n    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free\n    < static-learned < contextual-learned.\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2\n    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor\n    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto\n    frontier plot.\n\n    '\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  - plan_004\n  - plan_005\n  - plan_006\n  status: planned\n- id: plan_008\n  claim: 3\n  description: '7-level sparsity sweep (30/35/40/45/50/55/60%): KL-only vs BCE-only.\n    Test quantitative prediction: KL-BCE delta ~ s^2. 1 seed per level (sweep analysis,\n    not headline). 50% data point reused from plan_001. Taylor expansion accuracy\n    test at each level.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%\n    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds\n    each condition.\n\n    '\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  status: planned\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions\n    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:\n    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization\n    beyond short training sequences.\n\n    '\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 2\n  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8\n    categories. All conditions. Tests instruction-following quality under sparsity.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative\n    task types. Fine-grained capability diagnostics complementing LongBench.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_total_loss: 3.3438\n    final_kl_loss: 3.2969\n    final_reg_loss: 0.05\n    final_sparsity: 0\n    steps: 1000\n    tau_final: 0.1\n    wikitext2_ppl_dense: 6.12\n    wikitext2_ppl_sparse: 455.93\n    wikitext2_ppl_increase_pct: 7349\n    model_level_sparsity: 0.372\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\n- exp_id: mvp_kl_s123\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_kl_s456\n  name: ''\n  status: QUEUED\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_bce_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 27.9603\n    teal_sparse_ppl: 44.537\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 628\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_bce_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.3817\n    teal_sparse_ppl: 44.5864\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 629\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_bce_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.1437\n    teal_sparse_ppl: 43.033\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 603.3\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: kl_lagrangian_quicktest\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_kl_loss: 418\n    final_constraint_loss: 1.211\n    final_sparsity: 0.141\n    final_lambda: 5.06\n    steps: 200\n    sparsity_trajectory:\n    - 0.406\n    - 0.387\n    - 0.289\n    - 0.168\n    - 0.141\n- exp_id: kl_lagrangian_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_normalized_quicktest\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step1_kl: 1.18\n    step200_kl: 0.641\n    step200_sparsity: 0.504\n    final_lambda: 8\n    sparsity_converged_step: 80\n    sparsity_trajectory:\n    - 0.406\n    - 0.398\n    - 0.398\n    - 0.457\n    - 0.52\n    - 0.506\n    - 0.504\n    - 0.504\n    lambda_trajectory:\n    - 1\n    - 2\n    - 4\n    - 8\n    - 8\n    - 8\n    - 8\n    - 8\n- exp_id: mvp_kl_norm_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_norm_v3_quicktest\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    step1_kl_raw: 1.1797\n    step1_kl_norm: 1.1797\n    step1_sparsity: 0.406\n    step1_lambda: 2\n    step50_kl_raw: 0.7344\n    step50_kl_norm: 0.7344\n    step50_sparsity: 0.514\n    step50_lambda: 1.95\n    step100_kl_raw: 0.625\n    step100_kl_norm: 0.625\n    step100_sparsity: 0.496\n    step100_lambda: 1000\n    step150_kl_raw: 0.5703\n    step150_kl_norm: 0.5703\n    step150_sparsity: 0.48\n    step150_lambda: 1000\n    step200_kl_raw: 0.6836\n    step200_kl_norm: 0.6836\n    step200_sparsity: 0.477\n    step200_lambda: 1000\n    step200_constraint: 0.01178\n    kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)\n    sparsity_range: 0.477-0.514 after step 50\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\n- exp_id: mvp_kl_norm_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2142\n    teal_sparse_ppl: 12.0776\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 97.4\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_kl_norm_v2_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2474\n    teal_sparse_ppl: 11.9128\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 94.7\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n- exp_id: mvp_kl_norm_v2_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.14\n    teal_sparse_ppl: 13.58\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 121.9\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T17:12:06.056Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T17:12:06.056Z",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-15T17:12:06.098Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：KL优势是假象——BCE缺compensation导致的baseline weakness，而非loss function的内在优势。加上compensation后BCE追平或反超KL
核心假设：['KL-only PPL 方差比MVP显示的更大（std > 0.8，部分seeds > 11），稳定性存疑', 'BCE+compensation充分收敛到 ≤ 9.5 PPL，完全弥合与KL的差距甚至反超', 'SPON + KL有显著interaction effects，不满足可加性', 'KL-BCE delta不服从s²规律（R² < 0.80），linear fit同样好，理论叙事不成立', 'Mistral结果不一致或方向相反', 'STE baseline与Gumbel KL持平→relaxation method比loss function重要，因果归因错误']
关键指标范围：{'kl_only_wikitext2_ppl': [9.5, 12.0], 'kl_only_ppl_std': [0.8, 2.0], 'bce_comp_wikitext2_ppl': [8.5, 10.0], 'spon_kl_wikitext2_ppl': [9.0, 11.0], 'kl_vs_bce_comp_ppl_gap': [-1.5, 0.5], 'downstream_acc_drop_vs_dense_pct': [5, 10], 's2_scaling_r2': [0.5, 0.8], 'mistral_kl_ppl_increase_vs_dense_pct': [60, 120]}
叙事方向：核心claim（KL eliminates compensation）不成立。Reframe策略，不降级venue：(1) 将paper重心转向'首个系统性taxonomy of training signals × correction granularity for activation sparsity'——四象限ablation grid本身就是贡献，填补了文献空白；(2) 叙事从'A beats B'转为'characterization study'：'Both KL-only and BCE+compensation reach near-dense quality at 50% sparsity through fundamentally different mechanisms——we provide the first empirical decomposition of when and why each succeeds'；(3) SPON + contextual composition分析即使不完美可加也可作为standalone empirical finding。EMNLP Efficient Methods track重视thorough empirical methodology，paper_framing中预设的four-quadrant design正是为此scenario准备的。关键是honest framing而非overclaiming。

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
  "promptId": "2b738996-8a2b-480a-87bf-d362987a28b8",
  "type": "user",
  "uuid": "41fe38c7-1999-4525-9474-5d6da86e79e8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T17:12:06.097Z_

```json
{
  "parentUuid": "41fe38c7-1999-4525-9474-5d6da86e79e8",
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
  "uuid": "a61a711f-29c6-4535-bce4-b8413dadb0e5",
  "timestamp": "2026-05-15T17:12:06.097Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T17:12:06.097Z_

```json
{
  "parentUuid": "a61a711f-29c6-4535-bce4-b8413dadb0e5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9f4aef26-4c8c-4814-9ede-594cbc9b3d97",
  "timestamp": "2026-05-15T17:12:06.097Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：KL优势是假象——BCE缺compensation导致的baseline weakness，而非loss function的内在优势。加上compensation后BCE追平或反超KL 核心假设：['KL-only PPL 方差比MVP显示的更大（std > 0.8，部分seeds > 11），稳定性存疑'…",
  "leafUuid": "9f4aef26-4c8c-4814-9ede-594cbc9b3d97",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical decomposition of KL vs BCE for activation sparsity under worst-case scenario",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

### Assistant

_source line 8 · 2026-05-15T17:14:52.518Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "worst" tier scenario across all planned experiments in the experiment plan. Let me carefully analyze each experiment and predict results consistent with the worst-case narrative: KL advantage is an illusion caused by BCE lacking compensation, and BCE+compensation closes or reverses the gap.

Let me go through each planned experiment and generate predictions.

Key worst-tier assumptions:
1. KL-only PPL variance is high (std > 0.8, some seeds > 11)
2. BCE+compensation converges to ≤ 9.5 PPL, closing the gap


3. SPON and KL interact in non-additive ways that complicate the narrative
4. The relationship between KL-BCE delta and variance doesn't follow the expected scaling law
5. Results on Mistral might contradict the pattern or show reversed effects
6. The STE baseline performs similarly to Gumbel with KL, suggesting the relaxation method itself matters more than the loss function choice

Looking at the current MVP data, I'm noticing something interesting: KL-only shows remarkably low variance across seeds (mean around 9.20 with std of 0.055), while BCE-only is much worse at 28.16. The dense model sits at 6.1173. This baseline data will anchor my worst-case predictions.

For TEAL, I'm seeing values around 12.08, 11.91, and 13.58, which suggests higher variance than KL-only. Now I need to think through what happens when I add two more seeds to the KL-only condition. If the worst-case scenario has std > 0.8, those additional seeds would need to be substantially worse than the current tight cluster. Let me work through the ablation systematically—if I add seeds that hit 10.8 and 11.4, the five-seed mean would shift to around 9.96, which would finally break the tight clustering I'm seeing.

For BCE with compensation, the worst case would be bringing those high values down into the 9.2-9.8 range, giving a mean around 9.4 that matches or slightly beats KL-only. KL with compensation probably shows only marginal gains on top of that. For the STE baseline comparison, the key insight is whether the relaxation method itself matters—if STE and Gumbel perform similarly with KL, that suggests the loss function is what drives the difference, not the discretization approach. I'm realizing the STE baseline actually supports the KL loss hypothesis rather than undermining it—if a simple gradient estimator with KL performs as well as the more sophisticated Gumbel-sigmoid relaxation, that suggests the loss function is the critical factor, not the relaxation method itself. But I need to think through what happens in the worst-case scenario to fully evaluate this. Looking at plan_003, when BCE gets matched compute with KL, it improves but still underperforms BCE+comp, suggesting the bottleneck is the compensation mechanism itself rather than raw training budget. Plan_004 confirms SPON reproduces the published baseline, and plan_005 is exploring whether combining SPON with KL produces additive gains or if there are significant interaction effects that break the simple narrative.

The remaining plans paint a consistent picture: across multiple evaluation angles—full benchmarks, sparsity sweeps, Mistral validation, long-context tasks, and MT-Bench—KL doesn't maintain a clear advantage, and BCE+comp often matches or exceeds it, which directly undermines the claim that KL is uniquely superior.

Now I'm setting up the YAML predictions with specific numerical ranges for the key metrics, anchoring on expected perplexity values and the performance gaps between methods. I'm working through the seed values to hit that target mean and standard deviation—if I use a mix like 9.21, 9.25, 9.14 alongside some higher outliers around 10.8 and 11.4, that should push the mean to roughly 9.96 and give me the variance I need. Calculating variance for a different seed configuration to get the standard deviation under 0.8, trying values like 9.21, 9.25, 9.14, 10.5, 11.2 which gives a mean of 9.86 and variance around 0.875.

Now I'm settling on final numbers: KL-only with those five seeds averaging 9.86 with standard deviation 0.94, and BCE+comp seeds averaging 9.40 with standard deviation 0.22, putting the gap at +0.46 which fits within the acceptable range.

For KL+comp with three seeds, I'm getting around 8.97, which shows compensation helps both approaches but the critical finding is that BCE+comp nearly matches KL-only performance.

Let me check the TEAL baseline numbers from the registry—they're ranging from about 12 to 13.5 depending on the seed, while dense performance sits at 6.1. Now I need to work through the worst tier predictions.

Actually, I'm noticing a discrepancy with the BCE numbers. The registry shows BCE PPL around 28, not the 44 mentioned earlier—that 44 appears to be the TEAL sparse PPL from the BCE experiments, not the main predictor metric. The "12.52 vs 44.05" comparison in the project context might be mixing different evaluation metrics or earlier iterations.

Let me just work with the registry data directly rather than trying to reconcile these older numbers. But I'm struck by something odd: the TEAL sparse PPL values are wildly different between the KL and BCE experiments (around 12 vs 44), even though the model sparsity levels are nearly identical. That's a huge gap that shouldn't exist if they're measuring the same thing—either the TEAL implementation differs, the evaluation setup changed, or they're using different sparsity configurations despite similar reported numbers.

The eval MD5 hash is the same, so at least the evaluation data is consistent. This discrepancy is strange, but I'll set it aside for now and focus on generating the YAML output properly.

For the sparsity sweep experiment, I need to predict KL and BCE values across seven sparsity levels and demonstrate that fitting the delta to a quadratic function yields R² below 0.8. Starting from the dense baseline of 6.12 PPL, I'd expect both metrics to stay relatively close to that at low sparsity around 30-35%, then diverge significantly as sparsity climbs toward 55-60%, with the KL-BCE gap not following a clean quadratic pattern. Looking at the performance metrics across different saturation levels, the deltas are growing significantly—from 0.7 at 30% up to 53.0 at 60%. Let me fit this to a quadratic model where delta scales with saturation squared to see if that captures the pattern.

For a more realistic worst-case scenario with noisier behavior, I'll adjust the values so they don't fit a smooth curve perfectly—introducing some irregularities like the jump between 35% and 40% to make the R² value drop below 0.8.

Now looking at Mistral's performance, the worst-case range of 60-120% PPL increase is quite steep. With a dense baseline around 7.5, that would push KL-only PPL to around 14.25, which seems too high, so I need to reconsider what that range actually represents.

If it's a 60-120% increase, then KL-only PPL lands somewhere between 12.0 and 16.5. I'll estimate it at around 13.5 for an 80% increase, while BCE with compression gets closer to 12.0—which is interesting because it means BCE+comp actually outperforms KL-only on Mistral, flipping the pattern I saw with Llama.

I have enough data now to write out the full YAML configuration. Before I do that, let me also consider what downstream task performance might look like. I'm thinking through typical benchmark baselines for a dense 8B model like Llama 3.1: ARC-c sits around 53-55%, WinoGrande around 75-77%, MMLU around 65-67%, GSM8K around 50-55%, and HumanEval around 30-35%.

With a 5-10% accuracy drop across the board from quantization, I'd expect those numbers to drop to roughly 48-50% on ARC-c, 68-72% on WinoGrande, 59-63% on MMLU, 45-50% on GSM8K, and 27-32% on HumanEval. At this worst tier, KL-only and BCE+comp should show similar downstream performance, so the perplexity differences might not translate to meaningful task differences.

Now I'm ready to write this out carefully and consistently. For the SPON + KL composition experiment, I need to measure how well the two losses compose together using an additivity test—checking whether the combined effect matches the sum of individual effects, or if there's significant interaction. In the worst case, that ratio could exceed 0.3, indicating strong non-additive behavior.

Looking at the perplexity numbers across different approaches, SPON alone gets around 10.5-11.0 with static correction providing limited gains, while KL-only sits at about 9.9 from the baseline. When I combine SPON and KL, instead of getting the additive improvement down to 8.5, it only reaches 9.8—barely better than KL alone—which suggests a large interaction residual. For the training-free baselines, TEAL typically lands around 12-13 PPL, WINA at 15-18, and R-Sparse at 14-16. There's a discrepancy I'm noticing though: TEAL shows ~44 in the BCE experiments but ~12 in the KL runs, which is substantial and likely reflects differences in the evaluation setup, so I'll go with the 12-13 range for consistency.

Now thinking through the other evaluation plans: KL-only would probably degrade more on long-context tasks since it trains on shorter sequences, while KL and BCE with compression should perform similarly on MT-Bench. The RULER benchmark would give me fine-grained diagnostics to pinpoint where KL struggles across specific capability types. For the iso-compute comparison, I need to account for KL requiring a full forward pass, so I'd give BCE twice as many training steps to match the FLOPs. The worst case scenario would be that even extended BCE training still can't get the perplexity down significantly.

But actually, that result could support the narrative in a different way—it shows that compute isn't the limiting factor, and the real advantage comes from the compensation mechanism rather than the loss function itself. Now I'm looking at the TEAL sparse perplexity discrepancy between the BCE and KL experiments, which shows a 3-4x difference that's hard to explain by model sparsity alone.

I'm wondering if the TEAL implementation differs between setups—maybe one uses per-layer adaptive allocation while the other applies uniform sparsity. For plan_006, I'll go with the KL numbers around 12-13 PPL since that's the standalone evaluation context. Let me compile all these predictions into the YAML, and I still need to track down the SPON reproduction numbers for plan_004.

SPON uses static bias vectors with KL training, so on QA benchmarks I should expect results close to what's published—modest gains over training-free methods but less than contextual approaches, probably around 10.5-11.0 PPL at 50% sparsity with maybe 1-3% QA performance drop from dense. Now I'll structure the full YAML output with all ten plans.

For the full benchmark evaluation, I'm laying out the dense baselines for Llama 3.1 8B and then predicting what KL-only pruning at 50% sparsity would achieve across WikiText, C4, ARC, WinoGrande, MMLU, GSM8K, and HumanEval. Now I'm looking at the remaining benchmark results for the other approaches—BCE-only shows a significant performance drop across the board, while SPON and SPON+KL variants are closer to the KL baseline, and the training-free methods like TEAL, WINA, and R-Sparse fall somewhere in between. I have all the numbers I need, so I'm ready to compile this into a YAML configuration.

For the wall-clock profiling, KL-only sparse achieves about 1.4x speedup over the dense baseline despite the predictor overhead, while BCE with compensation is more modest at 1.2x—the key insight is that KL-only avoids the inference cost of a compensation network entirely, which gives it a structural advantage even if the quality trade-offs are comparable. Now I'm thinking through how to organize the YAML and make sure all the plan numbers and internal references stay consistent, then I'll sketch out what the tables and figures should look like.

For plan_001 I need a 4-condition matrix showing PPL, sparsity, and standard deviation with corresponding boxplots. Plan_002 compares STE versus Gumbel with training curves overlaid. Plan_003 shows per-step and total FLOPs alongside final PPL in a curve. Plan_004 is just a reproduction table for SPON. Plan_005 has composition results with a per-layer interaction residual heatmap. Plan_006 compares training-free baselines with a bar chart. Plan_007 is the big comprehensive table across all conditions and metrics, plus a Pareto frontier plot and a radar chart for downstream tasks. Plan_008 still needs definition.

Now I'm laying out the remaining plans: plan_008 covers 7 sparsity levels across KL and BCE loss with delta versus sparsity squared scatter plots and PPL curves. Plan_009 shows Mistral results compared to Llama. Plan_010 breaks down LongBench by task type and sequence length. Plan_011 has MT-Bench scores by category. Plan_012 covers RULER results. I'm about to write the YAML configuration, but first I should verify that my baseline metrics fall within the expected ranges—my 5-seed mean of 9.86 for KL-only on Wikitext2 PPL checks out against the worst tier threshold of 9.5 to 12.0.

Checking the remaining metric ranges now. My standard deviation of 0.94 is within 0.8 to 2.0, the BCE composite mean of 9.40 falls in the 8.5 to 10.0 band, the spontaneous KL result of 9.8 is within 9.0 to 11.0, and the KL versus BCE gap of +0.46 is in the -1.5 to 0.5 range. Downstream accuracy drops are hitting the 5 to 10 percent target, and I'm verifying the s² scaling R² value against the 0.5 to 0.8 threshold.

The Mistral KL perplexity increase sits around 85 percent, which fits the 60 to 120 percent range. Everything checks out, so I'm ready to construct the YAML output.

One thing I need to reconsider about the existing KL seeds—the three measured values of 9.21, 9.25, and 9.14 are individually below the 9.5 lower bound, but their mean of 9.86 is within the target range of 9.5 to 12.0. The two new seeds I'm projecting at 10.5 and 11.2 would pull the overall mean and standard deviation up appropriately, even though this creates a somewhat bimodal distribution. That's actually realistic for KL training, which can exhibit high variance across seeds.

For the KL plus compensation scenario, I'm noting that if compensation helps KL-only performance down to around 8.9 from 9.86, that suggests compensation is still beneficial even for KL, which complicates the narrative that KL alone eliminates the need for it. I'll need to address this tension carefully in the YAML structure and narrative guidance.

Writing out the YAML now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f4aef26-4c8c-4814-9ede-594cbc9b3d97",
  "isSidechain": false,
  "requestId": "req_011Cb4j9hM19DF7cq64d6chP",
  "type": "assistant",
  "uuid": "239e7733-148a-495e-92a2-ca6f0f7a2baf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxrmfdWniWZfyzdLPA5Z8w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11419,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8433,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11419
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

### Tool call

_source line 9 · 2026-05-15T17:14:52.521Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NhNFwZpSVLzw37tjA6zGuB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "239e7733-148a-495e-92a2-ca6f0f7a2baf",
  "isSidechain": false,
  "requestId": "req_011Cb4j9hM19DF7cq64d6chP",
  "type": "assistant",
  "uuid": "0bb457b8-1133-48ba-b942-79c378880341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxrmfdWniWZfyzdLPA5Z8w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11419,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8433,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11419
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

### Tool call

_source line 10 · 2026-05-15T17:14:52.531Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Hj1RbpByYG6suXp6m39cqw`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bb457b8-1133-48ba-b942-79c378880341",
  "isSidechain": false,
  "requestId": "req_011Cb4j9hM19DF7cq64d6chP",
  "type": "assistant",
  "uuid": "8e407a24-8d5a-45dd-ac09-df14bfb64cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxrmfdWniWZfyzdLPA5Z8w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11419,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8433,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11419
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

_source line 11 · 2026-05-15T17:14:52.557Z_

<details><summary>↩ Tool result · `toolu_01NhNFwZpSVLzw37tjA6zGuB`</summary>

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
  "parentUuid": "0bb457b8-1133-48ba-b942-79c378880341",
  "isSidechain": false,
  "promptId": "2b738996-8a2b-480a-87bf-d362987a28b8",
  "type": "user",
  "uuid": "1d568462-398c-4c11-bab2-7bb5df75137e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "0bb457b8-1133-48ba-b942-79c378880341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T17:14:52.555Z_

<details><summary>↩ Tool result · `toolu_01Hj1RbpByYG6suXp6m39cqw`</summary>

```text
.claude/sessions/no_project_0cc7fc01/CLAUDE.md
.claude/sessions/no_project_0cc7fc01/AGENTS.md
.claude/sessions/no_project_1e334e8c/CLAUDE.md
.claude/sessions/no_project_1e334e8c/AGENTS.md
.claude/sessions/no_project_6a78c900/CLAUDE.md
.claude/sessions/no_project_6a78c900/AGENTS.md
.claude/sessions/idea_reviewer_f685f055/CLAUDE.md
.claude/sessions/idea_reviewer_f685f055/AGENTS.md
.claude/sessions/no_project_c350bbdd/CLAUDE.md
.claude/sessions/no_project_c350bbdd/AGENTS.md
projects/temp-adv-distill-vla/docs/IDEA_BRIEF.md
projects/temp-adv-distill-vla/report.md
projects/temp-adv-distill-vla/.claude/sessions/agent_196bb1cd/CLAUDE.md
projects/temp-adv-distill-vla/.claude/sessions/agent_196bb1cd/AGENTS.md
projects/temp-adv-distill-vla/memory.md
projects/temp-adv-distill-vla/ROADMAP.md
projects/temp-adv-distill-vla/.claude/sessions/reviewer_a48a48bc/CLAUDE.md
projects/temp-adv-distill-vla/.claude/sessions/reviewer_a48a48bc/AGENTS.md
projects/temp-adv-distill-vla/.claude/CLAUDE.md
projects/temp-adv-distill-vla/AGENTS.md
projects/temp-adv-distill-vla/.claude/sessions/director_af591a94/CLAUDE.md
projects/temp-adv-distill-vla/.claude/sessions/director_af591a94/AGENTS.md
projects/temp-adv-distill-vla/task_context/reviewer.md
projects/distill_sparse_swiglu/artifacts/mvp_bce_s42/report/report_mvp_bce_s42.md
projects/distill_sparse_swiglu/artifacts/_project/report/bce_mvp_3seed_analysis.md
projects/distill_sparse_swiglu/artifacts/bce_mvp_3seed_analysis.md
projects/distill_sparse_swiglu/task_context/reviewer.md
projects/distill_sparse_swiglu/task_context/history/director/loop_1.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_1.md
projects/distill_sparse_swiglu/.claude/sessions/agent_4d4546dc/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_4d4546dc/AGENTS.md
projects/distill_sparse_swiglu/.claude/sessions/agent_cc4c7420/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_cc4c7420/AGENTS.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778861972.md
projects/distill_sparse_swiglu/.claude/sessions/agent_9a1e7e5c/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_9a1e7e5c/AGENTS.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778864854.md
projects/distill_sparse_swiglu/.claude/sessions/agent_3212319b/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_3212319b/AGENTS.md
projects/distill_sparse_swiglu/report.md
projects/distill_sparse_swiglu/.claude/sessions/agent_b500bda2/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_b500bda2/AGENTS.md
projects/distill_sparse_swiglu/memory.md
projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md
projects/distill_sparse_swiglu/paper_framing.md
projects/distill_sparse_swiglu/ROADMAP.md
projects/distill_sparse_swiglu/task_context/director.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778865194.md
projects/distill_sparse_swiglu/.claude/sessions/agent_14ee8c60/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_14ee8c60/AGENTS.md
projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749/AGENTS.md
projects/distill_sparse_swiglu/.claude/sessions/agent_1709b81f/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_1709b81f/AGENTS.md
projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7/AGENTS.md
projects/distill_sparse_swiglu/task_context/agent.md
.claude/CLAUDE.md
AGENTS.md
projects/distill_sparse_swiglu/.claude/CLAUDE.md
projects/distill_sparse_swiglu/AGENTS.md
projects/distill_sparse_swiglu/.claude/sessions/agent_453ff340/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_453ff340/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e407a24-8d5a-45dd-ac09-df14bfb64cc8",
  "isSidechain": false,
  "promptId": "2b738996-8a2b-480a-87bf-d362987a28b8",
  "type": "user",
  "uuid": "547dbfac-82f3-45f8-82f7-82dace2624cf",
  "toolUseResult": {
    "filenames": [
      ".claude/sessions/no_project_0cc7fc01/CLAUDE.md",
      ".claude/sessions/no_project_0cc7fc01/AGENTS.md",
      ".claude/sessions/no_project_1e334e8c/CLAUDE.md",
      ".claude/sessions/no_project_1e334e8c/AGENTS.md",
      ".claude/sessions/no_project_6a78c900/CLAUDE.md",
      ".claude/sessions/no_project_6a78c900/AGENTS.md",
      ".claude/sessions/idea_reviewer_f685f055/CLAUDE.md",
      ".claude/sessions/idea_reviewer_f685f055/AGENTS.md",
      ".claude/sessions/no_project_c350bbdd/CLAUDE.md",
      ".claude/sessions/no_project_c350bbdd/AGENTS.md",
      "projects/temp-adv-distill-vla/docs/IDEA_BRIEF.md",
      "projects/temp-adv-distill-vla/report.md",
      "projects/temp-adv-distill-vla/.claude/sessions/agent_196bb1cd/CLAUDE.md",
      "projects/temp-adv-distill-vla/.claude/sessions/agent_196bb1cd/AGENTS.md",
      "projects/temp-adv-distill-vla/memory.md",
      "projects/temp-adv-distill-vla/ROADMAP.md",
      "projects/temp-adv-distill-vla/.claude/sessions/reviewer_a48a48bc/CLAUDE.md",
      "projects/temp-adv-distill-vla/.claude/sessions/reviewer_a48a48bc/AGENTS.md",
      "projects/temp-adv-distill-vla/.claude/CLAUDE.md",
      "projects/temp-adv-distill-vla/AGENTS.md",
      "projects/temp-adv-distill-vla/.claude/sessions/director_af591a94/CLAUDE.md",
      "projects/temp-adv-distill-vla/.claude/sessions/director_af591a94/AGENTS.md",
      "projects/temp-adv-distill-vla/task_context/reviewer.md",
      "projects/distill_sparse_swiglu/artifacts/mvp_bce_s42/report/report_mvp_bce_s42.md",
      "projects/distill_sparse_swiglu/artifacts/_project/report/bce_mvp_3seed_analysis.md",
      "projects/distill_sparse_swiglu/artifacts/bce_mvp_3seed_analysis.md",
      "projects/distill_sparse_swiglu/task_context/reviewer.md",
      "projects/distill_sparse_swiglu/task_context/history/director/loop_1.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_1.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_4d4546dc/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_4d4546dc/AGENTS.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_cc4c7420/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_cc4c7420/AGENTS.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778861972.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_9a1e7e5c/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_9a1e7e5c/AGENTS.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778864854.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_3212319b/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_3212319b/AGENTS.md",
      "projects/distill_sparse_swiglu/report.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_b500bda2/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_b500bda2/AGENTS.md",
      "projects/distill_sparse_swiglu/memory.md",
      "projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md",
      "projects/distill_sparse_swiglu/paper_framing.md",
      "projects/distill_sparse_swiglu/ROADMAP.md",
      "projects/distill_sparse_swiglu/task_context/director.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778865194.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_14ee8c60/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_14ee8c60/AGENTS.md",
      "projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749/AGENTS.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_1709b81f/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_1709b81f/AGENTS.md",
      "projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7/AGENTS.md",
      "projects/distill_sparse_swiglu/task_context/agent.md",
      ".claude/CLAUDE.md",
      "AGENTS.md",
      "projects/distill_sparse_swiglu/.claude/CLAUDE.md",
      "projects/distill_sparse_swiglu/AGENTS.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_453ff340/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_453ff340/AGENTS.md"
    ],
    "durationMs": 17,
    "numFiles": 63,
    "truncated": false
  },
  "sourceToolAssistantUUID": "8e407a24-8d5a-45dd-ac09-df14bfb64cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：KL优势是假象——BCE缺compensation导致的baseline weakness，而非loss function的内在优势。加上compensation后BCE追平或反超KL 核心假设：['KL-only PPL 方差比MVP显示的更大（std > 0.8，部分seeds > 11），稳定性存疑'…",
  "leafUuid": "1d568462-398c-4c11-bab2-7bb5df75137e",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical decomposition of KL vs BCE for activation sparsity under worst-case scenario",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

### Tool call

_source line 15 · 2026-05-15T17:14:56.374Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DULrEJk81XXuCow3DsvmSa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "547dbfac-82f3-45f8-82f7-82dace2624cf",
  "isSidechain": false,
  "requestId": "req_011Cb4jMxzBU6okn2qV7hK7p",
  "type": "assistant",
  "uuid": "52a2e92f-65b4-4bf3-9244-fbe1dfd7c3a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGroc9fJ37iYr62wK4bDRn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10123,
      "cache_read_input_tokens": 23260,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 23260,
          "cache_creation_input_tokens": 10123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10123
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

_source line 16 · 2026-05-15T17:14:56.378Z_

<details><summary>↩ Tool result · `toolu_01DULrEJk81XXuCow3DsvmSa`</summary>

```text
1	# distill_sparse_swiglu — Memory
2	
3	## Director 审查备注 (2026-05-15)
4	
5	### [重要] TEAL 命名纠正 — 论文 Framing 用
6	当前 `teal_global_masks()` 用 **predictor sigmoid scores** 做全局排名，不是原始 TEAL 的激活幅度 `|gate(x)·up(x)|`。KL vs BCE 对比公平（同一 eval 逻辑），但论文中必须称 **"predictor-guided global allocation"** 而非 "vanilla TEAL"。Post-MVP 需加一个基于原始激活幅度的 vanilla TEAL baseline（无 predictor），回答 "predictor vs 直接用激活幅度" 的问题。代码准备：在 evaluate.py 加 `teal_activation_magnitude_masks()` 函数。
7	
8	### [Phase 1 升级] BCE + Gumbel 改进
9	- BCE 需升级为 FastForward 风格加权版本（Phase 1 时做）
10	- Gumbel 温度初始值应为 τ=5→0.1（IDEA_BRIEF 规定），当前代码可能是 τ=1.0→0.1，MVP 后修正
11	
12	### [Reviewer Warning] KL 归一化梯度信号 (2026-05-15)
13	- Reviewer 指出旧 quicktest 中 kl_raw 单调递增（1.18→9.94），因 ÷vocab_size bug 导致 kl_norm≈8e-5 梯度信号太弱
14	- **v3 修复后**: kl_raw 正确下降 (1.18→0.57)，bug 已修复
15	- 如果 3-seed KL PPL 明显差于 BCE baseline (mean=44.05)，备选方案: sqrt(vocab_size) 或 log(vocab_size) 替代 seq_len
16	- BCE baseline (统一 eval): s42=44.54, s123=44.59, s456=43.03, mean=44.05, Δ%=56.4%
17	
18	## SPON 调研 (2026-05-15)
19	
20	### SPON 方法
21	- 论文: "Resting Neurons, Active Insights" (arXiv 2512.12744)
22	- 机制: 每层注入 1 个 learnable input-independent bias vector 作为稀疏化后的 representational anchor
23	- 训练: **KL divergence** (distribution matching)，训练完成后 bias 可吸收进模型权重，**零推理开销**
24	- 效果: 50% sparsity 下一致优于 TEAL baseline
25	- 代码: 截至 2026-05-15 未找到公开代码仓库，需阅读论文全文获取超参数
26	- 参数量极低: 每层仅 hidden_dim 个参数
27	
28	### 竞品格局
29	| 方法 | 训练目标 | 核心差异 |
30	|------|---------|---------|
31	| DejaVu/PowerInfer/TurboSparse | BCE predictor | 我们用 KL 是核心差异化 |
32	| ProSparse/TurboSparse | 替换激活函数 | 我们保留 SwiGLU 是优势 |
33	| MaskLLM | Gumbel Softmax mask | 验证了 Gumbel 方向可行性 |
34	| DIP (MLSys 2025) | Predictor-free SwiGLU | 认为 SwiGLU 难预测, 我们用 KL 反驳 |
35	
36	### Phase 2 组合路径
37	KL Predictor 决定 mask → SPON bias vectors 补偿误差。两者互补：predictor 做稀疏决策，SPON 做误差修正。SPON 训练成本极低。
38	
39	## 实验经验 (2026-05-15)
40	
41	### [CRITICAL] evaluate.py True Dense 修复 (2026-05-15)
42	- **Bug**: `evaluate_perplexity(model, ...)` 传入的 model 已被 `PredictorWrapper._patch_mlps()` monkey-patch，"dense" 实际走 predictor hard mask 路径
43	- **Fix**: 添加 `evaluate_true_dense()` 函数，用 `_make_original_fwd()` 临时还原所有 MLP forward，评估后恢复 patch
44	- **eval_md5**: `f4086818bb55dc354ea4c6fe8ed8899a`（修复版）
45	- **True Dense PPL = 6.1173**（所有 checkpoint 一致，确认修复正确）
46	- **影响**: 之前用 predictor hard mask 当 dense baseline 严重低估了 PPL 增幅
47	
48	### MVP 三模式评估结果（修正后，eval_md5=f4086818）— MVP PASS ✅
49	| exp_id | seed | loss | True Dense | Pred Hard Mask | TEAL Sparse | Sparsity |
50	|--------|------|------|-----------|----------------|-------------|----------|
51	| mvp_kl_norm_v2_s42 | 42 | KL | 6.12 | 9.21 | 12.08 | 0.498 |
52	| mvp_kl_norm_v2_s123 | 123 | KL | 6.12 | 9.25 | 11.91 | 0.498 |
53	| mvp_kl_norm_v2_s456 | 456 | KL | 6.12 | 9.14 | 13.58 | 0.498 |
54	| mvp_bce_s42 | 42 | BCE | 6.12 | 27.96 | 44.54 | 0.496 |
55	| mvp_bce_s123 | 123 | BCE | 6.12 | 28.38 | 44.59 | 0.496 |
56	| mvp_bce_s456 | 456 | BCE | 6.12 | 28.14 | 43.03 | 0.496 |
57	
58	**3-seed 汇总**: KL mean sparse PPL = 12.52 ± 0.92, BCE mean = 44.05 ± 0.72。差距 31.53 >> 0.3 阈值。
59	**注意**: s456 是 KL 侧 outlier（sparse PPL 13.58, PPL increase 48.6% vs s42 31.2%/s123 28.8%），seed 敏感性值得 Phase 1 关注。
60	
61	### [关键洞察] KL predictor 质量信号 (2026-05-15)
62	- **Dense PPL 差异揭示 predictor 质量**: KL predictor hard mask PPL (9.2) 接近 true dense (6.12)，说明 KL predictor 几乎完美识别不重要 neuron。BCE predictor hard mask PPL (28) 远差于 true dense，大量误杀。
63	- **Per-layer sparsity 分布**: KL 学习到非均匀分配 (0.215-0.806)，中间层低稀疏(保护关键表征)，后层高稀疏。BCE 较均匀 (0.430-0.664)。
64	- **结论**: KL 端到端梯度流让 predictor 学会了"哪些层更重要"的层级决策，而 BCE 逐神经元独立目标无法传递这种跨层信息。
65	
66	### [关键] KL 归一化 — 正确配方 (v3)
67	- **KLDistillLoss (losses.py)**: `F.kl_div(reduction='batchmean')` 后 `÷ seq_len` → 归一化到 per-token scale
68	- **train.py**: `kl_norm = kl_raw`（不做任何额外归一化）
69	- **总归一化** = ÷(batch_size × seq_len)，kl_norm ≈ 0.5-1.2
70	- **⚠️ 曾有 bug**: train.py 多了 `/ vocab_size`，导致总归一化 = ÷(batch × seq_len × vocab_size)，kl_norm≈7e-5
71	- **Lagrangian**: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000], ±0.02 容忍带
72	
73	### KL 训练显存与速度
74	- gradient checkpointing: bs=2 实测 29.5GB, bs=4 实测 ~88GB（95GB 卡刀刃运行但稳定）
75	- KL 模式代码已自动启用 gradient checkpointing
76	- gradient accumulation 修复: 原始代码有 loss 未 scale + step 计数 bug
77	- KL 单步 ~15-30s/step vs BCE 1.5s/step, 1000 steps KL 约 40 min
78	
79	## 环境经验 (2026-05-15)
80	
81	### 服务器信息
82	- 服务器: westd-34887, 2× RTX PRO 6000 Blackwell (94GB each), CUDA 12.8
83	- 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128
84	- 项目目录: `/root/distill_sparse_swiglu/`
85	- 模型路径: `/root/autodl-tmp/models/llama-3.1-8b/`
86	- GPU 约束: C001 — 只允许 cuda:0, cuda:1
87	
88	### 踩坑记录
89	- **tmux 未预装**: 首次连接时 `apt-get install -y tmux`
90	- **submit 命令必须 `bash -c` 包装**: tmux 在 /bin/sh 下不认 `source`
91	- **ModelScope 不需要 network_turbo**: 直连 5-8 MB/s，代理反而慢
92	- **SlimPajama 不可用**: 已切换为 WikiText-103 train split
93	- **PYTHONUNBUFFERED=1**: submit 命令必须加，否则日志不实时输出
94	- **evaluate.py 版本不一致**: 两次 eval 间修改了 off-by-one bug，导致 dense PPL 6.12 vs 27.96。必须锁定版本统一重跑
95	- **TEAL 校准样本**: 从默认 4 条增至 32 条 (Reviewer 建议 32-64)
96	- **[CRITICAL] 修代码后必须 kill 旧进程**: Python 进程启动时代码已加载到内存，修改磁盘文件不影响已运行进程。修 bug 后必须 kill 旧进程 + 用新代码重启。子进程 PID 可能与 tmux wrapper PID 不同，需要都 kill。
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52a2e92f-65b4-4bf3-9244-fbe1dfd7c3a7",
  "isSidechain": false,
  "promptId": "2b738996-8a2b-480a-87bf-d362987a28b8",
  "type": "user",
  "uuid": "23abe698-8f0c-4c59-9bde-aad5c78f995d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md",
      "content": "# distill_sparse_swiglu — Memory\n\n## Director 审查备注 (2026-05-15)\n\n### [重要] TEAL 命名纠正 — 论文 Framing 用\n当前 `teal_global_masks()` 用 **predictor sigmoid scores** 做全局排名，不是原始 TEAL 的激活幅度 `|gate(x)·up(x)|`。KL vs BCE 对比公平（同一 eval 逻辑），但论文中必须称 **\"predictor-guided global allocation\"** 而非 \"vanilla TEAL\"。Post-MVP 需加一个基于原始激活幅度的 vanilla TEAL baseline（无 predictor），回答 \"predictor vs 直接用激活幅度\" 的问题。代码准备：在 evaluate.py 加 `teal_activation_magnitude_masks()` 函数。\n\n### [Phase 1 升级] BCE + Gumbel 改进\n- BCE 需升级为 FastForward 风格加权版本（Phase 1 时做）\n- Gumbel 温度初始值应为 τ=5→0.1（IDEA_BRIEF 规定），当前代码可能是 τ=1.0→0.1，MVP 后修正\n\n### [Reviewer Warning] KL 归一化梯度信号 (2026-05-15)\n- Reviewer 指出旧 quicktest 中 kl_raw 单调递增（1.18→9.94），因 ÷vocab_size bug 导致 kl_norm≈8e-5 梯度信号太弱\n- **v3 修复后**: kl_raw 正确下降 (1.18→0.57)，bug 已修复\n- 如果 3-seed KL PPL 明显差于 BCE baseline (mean=44.05)，备选方案: sqrt(vocab_size) 或 log(vocab_size) 替代 seq_len\n- BCE baseline (统一 eval): s42=44.54, s123=44.59, s456=43.03, mean=44.05, Δ%=56.4%\n\n## SPON 调研 (2026-05-15)\n\n### SPON 方法\n- 论文: \"Resting Neurons, Active Insights\" (arXiv 2512.12744)\n- 机制: 每层注入 1 个 learnable input-independent bias vector 作为稀疏化后的 representational anchor\n- 训练: **KL divergence** (distribution matching)，训练完成后 bias 可吸收进模型权重，**零推理开销**\n- 效果: 50% sparsity 下一致优于 TEAL baseline\n- 代码: 截至 2026-05-15 未找到公开代码仓库，需阅读论文全文获取超参数\n- 参数量极低: 每层仅 hidden_dim 个参数\n\n### 竞品格局\n| 方法 | 训练目标 | 核心差异 |\n|------|---------|---------|\n| DejaVu/PowerInfer/TurboSparse | BCE predictor | 我们用 KL 是核心差异化 |\n| ProSparse/TurboSparse | 替换激活函数 | 我们保留 SwiGLU 是优势 |\n| MaskLLM | Gumbel Softmax mask | 验证了 Gumbel 方向可行性 |\n| DIP (MLSys 2025) | Predictor-free SwiGLU | 认为 SwiGLU 难预测, 我们用 KL 反驳 |\n\n### Phase 2 组合路径\nKL Predictor 决定 mask → SPON bias vectors 补偿误差。两者互补：predictor 做稀疏决策，SPON 做误差修正。SPON 训练成本极低。\n\n## 实验经验 (2026-05-15)\n\n### [CRITICAL] evaluate.py True Dense 修复 (2026-05-15)\n- **Bug**: `evaluate_perplexity(model, ...)` 传入的 model 已被 `PredictorWrapper._patch_mlps()` monkey-patch，\"dense\" 实际走 predictor hard mask 路径\n- **Fix**: 添加 `evaluate_true_dense()` 函数，用 `_make_original_fwd()` 临时还原所有 MLP forward，评估后恢复 patch\n- **eval_md5**: `f4086818bb55dc354ea4c6fe8ed8899a`（修复版）\n- **True Dense PPL = 6.1173**（所有 checkpoint 一致，确认修复正确）\n- **影响**: 之前用 predictor hard mask 当 dense baseline 严重低估了 PPL 增幅\n\n### MVP 三模式评估结果（修正后，eval_md5=f4086818）— MVP PASS ✅\n| exp_id | seed | loss | True Dense | Pred Hard Mask | TEAL Sparse | Sparsity |\n|--------|------|------|-----------|----------------|-------------|----------|\n| mvp_kl_norm_v2_s42 | 42 | KL | 6.12 | 9.21 | 12.08 | 0.498 |\n| mvp_kl_norm_v2_s123 | 123 | KL | 6.12 | 9.25 | 11.91 | 0.498 |\n| mvp_kl_norm_v2_s456 | 456 | KL | 6.12 | 9.14 | 13.58 | 0.498 |\n| mvp_bce_s42 | 42 | BCE | 6.12 | 27.96 | 44.54 | 0.496 |\n| mvp_bce_s123 | 123 | BCE | 6.12 | 28.38 | 44.59 | 0.496 |\n| mvp_bce_s456 | 456 | BCE | 6.12 | 28.14 | 43.03 | 0.496 |\n\n**3-seed 汇总**: KL mean sparse PPL = 12.52 ± 0.92, BCE mean = 44.05 ± 0.72。差距 31.53 >> 0.3 阈值。\n**注意**: s456 是 KL 侧 outlier（sparse PPL 13.58, PPL increase 48.6% vs s42 31.2%/s123 28.8%），seed 敏感性值得 Phase 1 关注。\n\n### [关键洞察] KL predictor 质量信号 (2026-05-15)\n- **Dense PPL 差异揭示 predictor 质量**: KL predictor hard mask PPL (9.2) 接近 true dense (6.12)，说明 KL predictor 几乎完美识别不重要 neuron。BCE predictor hard mask PPL (28) 远差于 true dense，大量误杀。\n- **Per-layer sparsity 分布**: KL 学习到非均匀分配 (0.215-0.806)，中间层低稀疏(保护关键表征)，后层高稀疏。BCE 较均匀 (0.430-0.664)。\n- **结论**: KL 端到端梯度流让 predictor 学会了\"哪些层更重要\"的层级决策，而 BCE 逐神经元独立目标无法传递这种跨层信息。\n\n### [关键] KL 归一化 — 正确配方 (v3)\n- **KLDistillLoss (losses.py)**: `F.kl_div(reduction='batchmean')` 后 `÷ seq_len` → 归一化到 per-token scale\n- **train.py**: `kl_norm = kl_raw`（不做任何额外归一化）\n- **总归一化** = ÷(batch_size × seq_len)，kl_norm ≈ 0.5-1.2\n- **⚠️ 曾有 bug**: train.py 多了 `/ vocab_size`，导致总归一化 = ÷(batch × seq_len × vocab_size)，kl_norm≈7e-5\n- **Lagrangian**: lambda_init=1.0, ×2.0/×0.5 every 25 steps, clamp [0.1, 1000], ±0.02 容忍带\n\n### KL 训练显存与速度\n- gradient checkpointing: bs=2 实测 29.5GB, bs=4 实测 ~88GB（95GB 卡刀刃运行但稳定）\n- KL 模式代码已自动启用 gradient checkpointing\n- gradient accumulation 修复: 原始代码有 loss 未 scale + step 计数 bug\n- KL 单步 ~15-30s/step vs BCE 1.5s/step, 1000 steps KL 约 40 min\n\n## 环境经验 (2026-05-15)\n\n### 服务器信息\n- 服务器: westd-34887, 2× RTX PRO 6000 Blackwell (94GB each), CUDA 12.8\n- 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128\n- 项目目录: `/root/distill_sparse_swiglu/`\n- 模型路径: `/root/autodl-tmp/models/llama-3.1-8b/`\n- GPU 约束: C001 — 只允许 cuda:0, cuda:1\n\n### 踩坑记录\n- **tmux 未预装**: 首次连接时 `apt-get install -y tmux`\n- **submit 命令必须 `bash -c` 包装**: tmux 在 /bin/sh 下不认 `source`\n- **ModelScope 不需要 network_turbo**: 直连 5-8 MB/s，代理反而慢\n- **SlimPajama 不可用**: 已切换为 WikiText-103 train split\n- **PYTHONUNBUFFERED=1**: submit 命令必须加，否则日志不实时输出\n- **evaluate.py 版本不一致**: 两次 eval 间修改了 off-by-one bug，导致 dense PPL 6.12 vs 27.96。必须锁定版本统一重跑\n- **TEAL 校准样本**: 从默认 4 条增至 32 条 (Reviewer 建议 32-64)\n- **[CRITICAL] 修代码后必须 kill 旧进程**: Python 进程启动时代码已加载到内存，修改磁盘文件不影响已运行进程。修 bug 后必须 kill 旧进程 + 用新代码重启。子进程 PID 可能与 tmux wrapper PID 不同，需要都 kill。\n",
      "numLines": 97,
      "startLine": 1,
      "totalLines": 97
    }
  },
  "sourceToolAssistantUUID": "52a2e92f-65b4-4bf3-9244-fbe1dfd7c3a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T17:14:56.426Z_

<details open><summary>🔧 Tool call — Read · `toolu_014y13KJpdS3ihTwH4eGoEMi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23abe698-8f0c-4c59-9bde-aad5c78f995d",
  "isSidechain": false,
  "requestId": "req_011Cb4jMxzBU6okn2qV7hK7p",
  "type": "assistant",
  "uuid": "148987bf-234a-4dd6-ba89-9a50a0c29c4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGroc9fJ37iYr62wK4bDRn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10123,
      "cache_read_input_tokens": 23260,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 23260,
          "cache_creation_input_tokens": 10123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10123
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

_source line 18 · 2026-05-15T17:14:56.430Z_

<details><summary>↩ Tool result · `toolu_014y13KJpdS3ihTwH4eGoEMi`</summary>

```text
1	# Handover — 2026-05-15
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	（无）
7	
8	## 待处理
9	- mvp_kl_s456（排队等待 GPU）
10	- mvp_kl_s123（排队等待 GPU）
11	- mvp_kl_norm_s456（准备中）
12	- kl_norm_v3_quicktest（准备中）
13	- kl_lagrangian_v2（准备中）
14	
15	## 近期结论
16	- **mvp_kl_norm_v2_s456** (success): —
17	- **mvp_kl_norm_v2_s123** (success): —
18	- **mvp_kl_norm_v2_s42** (success): —
19	
20	## 趋势
21	成功 6 / 负向 2 / 失败 3 / 共 11
22	model_level_sparsity: 0.498 ↑（近 3 次 success）
23	
24	## 下一步
25	（无活跃 idea，请通过 ideas.md 添加）
26	
27	## 资源状态
28	westd-34887: 无 GPU 信息
29	
30	## 告警
31	- kl_normalized_quicktest: 训练失败 — unknown
32	- mvp_kl_norm_s42: 训练失败 — unknown
33	- mvp_kl_norm_s123: 训练失败 — unknown
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "148987bf-234a-4dd6-ba89-9a50a0c29c4c",
  "isSidechain": false,
  "promptId": "2b738996-8a2b-480a-87bf-d362987a28b8",
  "type": "user",
  "uuid": "171b3009-99a5-44d8-baff-147d4b917b3f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md",
      "content": "# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- mvp_kl_s456（排队等待 GPU）\n- mvp_kl_s123（排队等待 GPU）\n- mvp_kl_norm_s456（准备中）\n- kl_norm_v3_quicktest（准备中）\n- kl_lagrangian_v2（准备中）\n\n## 近期结论\n- **mvp_kl_norm_v2_s456** (success): —\n- **mvp_kl_norm_v2_s123** (success): —\n- **mvp_kl_norm_v2_s42** (success): —\n\n## 趋势\n成功 6 / 负向 2 / 失败 3 / 共 11\nmodel_level_sparsity: 0.498 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123: 训练失败 — unknown\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "148987bf-234a-4dd6-ba89-9a50a0c29c4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19 · 2026-05-15T17:14:56.562Z_

````json
{
  "parentUuid": "171b3009-99a5-44d8-baff-147d4b917b3f",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**distill_sparse_swiglu**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"distill_sparse_swiglu\")` 或 `load_project_config(\"distill_sparse_swiglu\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/distill_sparse_swiglu/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "18787096-4224-4ed3-8fb5-e95c666fc7e9",
  "timestamp": "2026-05-15T17:14:56.562Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：KL优势是假象——BCE缺compensation导致的baseline weakness，而非loss function的内在优势。加上compensation后BCE追平或反超KL 核心假设：['KL-only PPL 方差比MVP显示的更大（std > 0.8，部分seeds > 11），稳定性存疑'…",
  "leafUuid": "18787096-4224-4ed3-8fb5-e95c666fc7e9",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical decomposition of KL vs BCE for activation sparsity under worst-case scenario",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

### Assistant

_source line 22 · 2026-05-15T17:21:27.782Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project context. Let me note a key correction from the memory:

The "mean sparse PPL" in the 3-seed summary is 12.52 ± 0.92 for KL — but wait, the individual PPLs are 9.21, 9.25, 9.14. Mean = (9.21+9.25+9.14)/3 = 27.6/3 = 9.20. That doesn't match 12.52.

Oh wait, looking at memory.md more carefully: "KL mean sparse PPL = 12.52 ± 0.92" — but the "Pred Hard Mask" PPL values are 9.21, 9.25, 9.14. 

So the TEAL Sparse values of 12.08, 11.91, 13.58 are what average to 12.52 — meaning "sparse PPL" refers to TEAL sparse performance, not the predictor's hard mask results. That's a crucial distinction for understanding what the metrics actually represent. I see the issue now — TEAL is supposed to be training-free, so the difference between KL and BCE runs shouldn't exist. But looking at the implementation notes, the current `teal_global_masks()` function actually uses predictor sigmoid scores for global ranking rather than the original TEAL activation magnitudes, which explains why KL and BCE predictors produce different allocation results. Both the "Pred Hard Mask" and "TEAL Sparse" metrics are predictor-dependent — the former applies per-layer decisions directly while the latter applies global reallocation based on predictor scores.

For the worst-case predictions, I should focus on the Pred Hard Mask metric since that directly reflects the predictor's quality. The KL-only baseline shows 9.20 mean PPL across 3 seeds while BCE-only reaches 28.16, so I need to align my predictions with this metric and the user's specified ranges for the 5-seed mean.

Looking at the individual KL seed results (9.21, 9.25, 9.14), I need the two additional seeds to push the 5-seed mean into the [9.5, 12.0] range. That means the new seeds must sum to at least 19.9 to hit the lower bound, while staying under 32.4 for the upper bound. I'll use 10.8 and 11.6 as my new seed values to create meaningful spread and land the mean around 10.0.

Now I'm calculating the statistics for this 5-seed configuration. The mean comes out to exactly 10.0, which sits comfortably in the target range, and the standard deviation is 1.13, which exceeds the 0.8 minimum while staying well within the 2.0 cap. This configuration works well for the hard mask metric. Next I need to check what the mean should be for the BCE+comp metric.

I'm testing a different set of 5 seeds for BCE+comp that should fall in the [8.5, 10.0] range. The mean of 9.36 is good, but the gap between the KL and BCE+comp means is 0.64, which pushes slightly outside the acceptable [-1.5, 0.5] window. I need to adjust the values to bring this gap back into bounds. .756 standard deviation, so the gap of 0.44 is getting close to that upper bound of 0.5. Let me try a safer value with BCE_comp set to 9.5 instead, and I'm recalculating the mean and standard deviation for those seeds.

Now I'm checking whether the gap stays within range with this adjustment—it comes out to 0.3, which is better. But I'm reconsidering the scenario: maybe it's more compelling if BCE_comp actually beats KL slightly, so I'm exploring different mean values to see what happens at the boundary. I'm realizing I need to clarify how the gap is defined to make sure I'm setting this up correctly. than BCE+comp), and KL+comp performs best at 8.97. The narrative holds: KL's advantage disappears when both methods get compensation, revealing that the real benefit comes from the compensation mechanism itself, not from KL's inherent superiority.

Now I'm organizing the results by plan_id and need to estimate the TEAL sparse metric values for the new seeds to maintain consistency with the existing data pattern.

For BCE+comp, I need to think through how the evaluation works—the compensation MLP corrects the sparse output after the BCE predictor generates the mask, so the hard mask PPL would reflect both the predictor's decisions and the compensation network's corrections.

Looking at the metrics more carefully, the "predictor_hard_mask_ppl" in the registry is just the mask quality without compensation, so I should probably use a different metric name to distinguish the BCE+comp results that include the compensation effect. Let me check the experiment plan to see what conditions are actually being tested.

The plan calls for a four-condition ablation comparing BCE-only, BCE+compensation, KL-only, and KL+compensation at 50% sparsity on Llama 3.1 8B. I'll use wikitext2_ppl as my main metric, measured with whatever approach each condition specifies. Now I'm realizing I need to reconcile the numbers from the registry with what the project context mentioned about the massive KL versus BCE gap—the 12.52 versus 44.05 comparison appears to be the TEAL sparse results, which are different from the predictor hard mask measurements.

For my predictions, I'll focus on the predictor hard mask PPL equivalent since that's the actual sparse execution metric. Now I'm ready to write out the full YAML with all eight planned experiments, making sure to include concrete tables and figure descriptions for each one.

My structure covers the core ablation, baseline comparisons, iso-compute analysis, SPON variants, training-free methods, and then validation across multiple benchmarks like Mistral, LongBench, MT-Bench, and RULER. I want to get the s² scaling analysis right for the sparsity sweep, so I'm working through those predictions now.

Generating the sparsity sweep table... Looking at the actual data points, a pure quadratic model through the origin doesn't fit at all—the predicted values are way too high compared to what I'm observing, so there's clearly an intercept term involved.

The paper's claim is that the KL advantage scales with s², but what I'm actually seeing is that both KL and BCE degrade as sparsity increases, with BCE falling off much faster. The delta between them looks more exponential than quadratic. To properly test whether s² is a good fit, I need to construct data that's noisy enough to give a poor R² value when fit to s².

Generating test data... Looking at the performance metrics across different parameter values, I notice the relationship between Δ and s² isn't perfectly linear—there are irregular jumps that suggest the fit won't be clean. Let me approach this more systematically by treating this as a linear regression problem where Δ should scale with s², then I can calculate the actual R² value to see how well the data conforms to that model.

Computing the covariance and variance terms to determine the regression slope and intercept... Now I'm checking how well this linear regression model fits the data by computing predicted values across the range of squared standard deviations and comparing them to the actual measurements—most predictions are overshooting, particularly at higher values, which suggests the model may not capture the relationship accurately. Now I'm calculating the sum of squared residuals and the total sum of squares to get the R² value. After working through the arithmetic, I'm getting R² = 0.96, which seems too high.

I realize the issue—any monotonically increasing relationship will naturally produce a high R² when fit linearly against s². To get a lower R² value below 0.8, I need to introduce more irregularity and noise into the data. Let me create a new dataset with much more variation.

Generating markdown table...

The pattern I'm aiming for here is one where the delta doesn't follow a clean monotonic relationship with s²—there's a dip at s=0.40, then a dramatic spike at s=0.50, and the KL perplexity behaves unexpectedly at higher values. This kind of phase-transition-like behavior should break the linear relationship and lower the R² significantly.

Now I'm calculating the correlation coefficient to quantify how poorly s² actually predicts delta. I'm working through the deviations from the means and computing the covariance terms to see just how weak this relationship really is. ) + (0.090)(10.12) + (0.148)(13.62)
= 1.187 + 0.700 + 0.410 + 0.062 + 0.297 + 0.911 + 2.016
= 5.583

Sxx = 0.05723 (same as before)
m = 5.583/0.05723 = 97.56
c = 10.38 - 97.56*0.212 = 10.38 - 20.68 = -10.30

Now I'm checking the predictions against actual values across the remaining data points, calculating residuals to see how far off the model is at each variance level. Now I'm finishing the total sum of squares calculation and finding that R² comes out to 0.901, which is still too high because the data follows such a strong monotonic trend. I'm going to try a more extreme pattern where the differences between KL and BCE perplexities are genuinely noisy and don't follow the overall trend as closely.

I'm constructing a scenario where at higher sparsity levels, KL itself starts degrading significantly, so the delta plateaus or even decreases—this captures the realistic behavior where neither method can compensate at very high sparsity levels.

Now I'm calculating R² to quantify how well sparsity explains the variance in delta, computing the covariance between sparsity squared and the delta values. Now I'm checking the predictions against actual values for the remaining data points—the model's overestimating at higher variance levels, particularly around s²=0.160 and s²=0.202 where the residuals are quite large and negative. Finishing the total sum of squares calculation, I get 384.15, which gives me an R² of 0.836—still above the 0.80 threshold. This shows the real problem: even noisy data with a clear upward trend produces deceptively high R² values. Let me construct a more extreme example with larger fluctuations in the differences to better illustrate this issue.

Now I'm computing the covariance with this noisier dataset, calculating how the deviations from the mean difference interact with the standardized s values across all seven points. Now I'm checking the predictions against actual values for each variance level, calculating residuals to see how far off the model is at each point. I'm finishing the residual sum of squares calculation and then computing the total sum of squares to get an R² value of 0.658, which falls nicely in the target range. Now I need to justify why the delta would actually decrease at high sparsity levels—the KL divergence itself seems to be the key factor here.

At 55-60% sparsity, KL collapses catastrophically (perplexity jumps from 16 to 32), so both methods degrade together and the advantage of KL diminishes. This creates a non-monotonic relationship between delta and sparsity that complicates the clean quadratic scaling story I was building.

Let me check how a linear fit performs instead by computing R² for delta versus sparsity directly across the seven data points.

Computing the covariance and variance terms...

Now I'm calculating the linear regression slope and intercept, getting m = 50.74 and c = -14.45. Let me check how well this linear model predicts the actual values across the different s values. I'm finishing the sum of squared residuals calculation and comparing the fit quality between the two models. The linear relationship between Δ and s actually performs slightly better than the quadratic fit, with an R² of 0.679 versus 0.658.

This is problematic for the theoretical s² scaling claim—both fits are mediocre and noisy, suggesting the data doesn't cleanly follow either functional form. The real issue seems to be that the BCE data has a huge outlier at s=0.50 that's skewing the entire fit, rather than a fundamental problem with how I'm modeling the relationship.

Looking at the actual numbers, there's a sharp phase transition in BCE around s=0.45-0.50 where it jumps from ~14.5 to ~28.0, while KL stays relatively flat. This creates a step-function-like behavior rather than smooth polynomial degradation, which explains why the quadratic fit doesn't capture the pattern well.

Let me compile the sparsity sweep data into the YAML output with these key observations about the phase transition. Now I'm looking at the R² values for both the quadratic and linear fits—they're comparable around 0.66-0.68, which supports the claim that the linear model performs just as well. I need to structure the YAML output with all the key sections: metadata, description, expected results, the data tables, and analysis rationale. I'm also thinking through the downstream accuracy targets for plan_007, checking what kind of performance drop we'd expect across the benchmark tasks when compressing the model. Looking at the performance metrics across different methods, BCE+comp consistently outperforms KL-only across all downstream tasks, which aligns with the expected pattern. SPON shows significant degradation compared to the contextual approaches, and SPON+KL only provides marginal improvements over KL alone rather than being additive. The training-free baseline performs substantially worse. For wall-clock profiling, KL-only achieves the best speedup at 1.35x, while BCE+comp trades some of that efficiency for better accuracy with 1.18x speedup.

Plotting these on a Pareto frontier reveals that KL-only and BCE+comp occupy similar quality regions with KL having a slight speed edge, while training-free methods are faster but significantly worse in quality. However, I'm realizing that BCE+comp requires the compensation network at inference time, which adds meaningful memory overhead and latency costs. This shifts the narrative—rather than KL being strictly better, it's more accurate to say KL offers a simpler and cheaper inference path that achieves comparable quality without the additional computational burden.

Now I'm moving to the YAML configuration for plan_010 on LongBench, where I need to estimate performance across different task categories. I'm looking at the expected F1 scores for each task type: single-document QA around 22, multi-document QA at 35, summarization at 28, few-shot tasks at 68, and code-related tasks at 55.

For the worst-case scenarios, I'm comparing how different model configurations degrade on longer contexts. The KL-only approach shows steeper performance drops across all task types, ranging from about 11-23% degradation, while the BCE+comp configuration is more resilient, with degradation in the 10-17% range. This pattern suggests that the combined loss approach maintains better performance on long-context tasks because it provides more robust training signals.

Looking at the MT-Bench results, all approaches show some quality loss compared to the dense baseline, but BCE+comp again performs slightly better than KL-only, maintaining better instruction-following quality. Now I'm examining the RULER benchmark results across different context lengths to see how these approaches scale.

Generating markdown table...

The pattern is clear: KL degrades significantly at longer contexts while BCE+comp maintains more robustness across the 4K and 16K token ranges. I'm ready to write out the YAML configuration now. Let me also check the SPON reimplementation results to see how the static bias vector approach compares on the QA benchmarks.

Looking at the SPON reproduction numbers across ARC-c, ARC-e, BoolQ, PIQA, and WinoGrande, the results align well with published numbers, validating the implementation. The perplexity sits around 10.8 at 50% sparsity. Now for the composition experiment with SPON and KL together—the combined approach yields 9.6 PPL, which is only marginally better than KL alone at 9.8, falling well short of the expected 8.5 if the improvements were additive.

I'm reconsidering what additivity actually means here. The paper frames it as composing two corrections: a static correction from SPON and a contextual correction from KL. If they truly compose additively, the total correction should be the sum of both, recovering more quality than either method alone. But the empirical results suggest the improvements aren't stacking the way I'd expect—I need to think through whether the baseline dense model's perplexity and how each method's delta compounds actually supports this additive model. The interaction residual comes to 1.5 PPL points, which is substantial and indicates the two corrections are overlapping significantly. Looking at the logit-space linearity test, the corrections show non-independence with a ratio above 0.35, and the per-layer orthogonality analysis reveals they're actually correlated across many layers rather than orthogonal. Now I need to compile all these numbers into the YAML format and double-check the Mistral predictions.

For Mistral-7B, the dense baseline is around 7.8 PPL. With KL-only, that jumps to about 14.4 (an 85% increase), while BCE+comp gets to 12.8 (64% increase), so the composite approach significantly outperforms KL-only here—even more dramatically than on Llama. This actually weakens the claim that KL has a generalization advantage. On MMLU, Mistral's dense performance is roughly 62%, dropping to 52% with KL-only and 55% with BCE+comp. For ARC-c, dense sits around 50% with KL-only falling to 42%.

Formatting YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18787096-4224-4ed3-8fb5-e95c666fc7e9",
  "isSidechain": false,
  "requestId": "req_011Cb4jNG27g4sf5tbE4f6td",
  "type": "assistant",
  "uuid": "a4e01231-e91c-4280-9496-3a26caf0feb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLPfMdHtxBTEgsVVbF59LT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8837,
      "cache_read_input_tokens": 42220,
      "output_tokens": 31065,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 31065,
          "cache_read_input_tokens": 42220,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-15T17:26:00.710Z_

```yaml
tier: worst
narrative_guidance: >-
  KL优势是假象。BCE的核心瓶颈不是loss function而是缺少compensation mechanism。
  加上FastForward风格的compensation MLP后，BCE+comp在PPL和downstream tasks上追平甚至反超KL-only。
  KL-only训练不稳定（5-seed std > 0.8，2个新seed PPL > 10.5），稳定性劣于BCE+comp。
  s²scaling理论不成立（R² < 0.7），linear fit同样好。SPON+KL非可加，Mistral结果方向反转。
  Paper重心从"KL eliminates compensation"转向"首个系统性taxonomy of training signals ×
  correction granularity for activation sparsity"，以characterization study投EMNLP Efficient Methods track。

imagined_experiments:
  # ════════════════════════════════════════════
  # plan_001: Four-condition ablation (P0, core)
  # ════════════════════════════════════════════
  - name: "Four-condition ablation @ 50% sparsity"
    plan_id: "plan_001"
    description: >-
      四条件消融：(a) BCE-only 3 seeds existing, (b) BCE+comp 5 seeds new,
      (c) KL-only 5 seeds (3 existing + 2 new), (d) KL+comp 3 seeds new。
      Headline对比KL-only vs BCE+comp各5 seeds。
    expected_results:
      # ── KL-only (5 seeds) ──
      kl_only_s42_ppl: 9.21        # existing
      kl_only_s123_ppl: 9.25       # existing
      kl_only_s456_ppl: 9.14       # existing
      kl_only_s0_ppl: 10.31        # NEW — partial convergence failure
      kl_only_s1_ppl: 11.08        # NEW — worst seed, sparsity oscillation
      kl_only_mean_ppl: 9.80
      kl_only_std_ppl: 0.87
      kl_only_model_sparsity: 0.498
      # ── BCE+comp (5 seeds) ──
      bce_comp_s42_ppl: 9.18
      bce_comp_s123_ppl: 9.35
      bce_comp_s456_ppl: 9.52
      bce_comp_s0_ppl: 9.28
      bce_comp_s1_ppl: 9.68
      bce_comp_mean_ppl: 9.40
      bce_comp_std_ppl: 0.19
      bce_comp_model_sparsity: 0.496
      # ── KL+comp (3 seeds) ──
      kl_comp_s42_ppl: 8.82
      kl_comp_s123_ppl: 8.95
      kl_comp_s456_ppl: 9.08
      kl_comp_mean_ppl: 8.95
      kl_comp_std_ppl: 0.13
      # ── BCE-only (3 seeds, existing) ──
      bce_only_mean_ppl: 28.16
      # ── 关键比较 ──
      kl_vs_bce_comp_gap: +0.40     # KL worse (higher PPL)
      kl_comp_vs_bce_comp_gap: -0.45 # KL+comp best, but comp helps both
      dense_ppl: 6.12
    result_rationale: >-
      s0和s1两个新seed暴露了KL训练的Lagrangian不稳定性。
      Lagrangian乘子在这两个seed下出现λ震荡（未收敛到稳定平衡点），
      导致sparsity在0.47-0.52间振荡，predictor未充分优化。
      s456的teal异常（13.58 vs 12.08/11.91）已经暗示了seed敏感性，
      新seed进一步确认：KL+Lagrangian在某些初始化下不稳定，
      std=0.87远高于BCE+comp的0.19。
      BCE+comp通过compensation MLP有效纠正了BCE predictor的per-neuron误差，
      从28.16降至9.40——compensation消除了~67%的BCE quality gap。
      KL+comp是最佳条件（8.95），说明compensation对KL也有帮助，
      而非KL已经"不需要"compensation。核心发现：compensation是通用质量提升手段，
      KL的"优势"仅是在不公平对比（有comp vs 无comp）下的假象。
    tables:
      - title: "Table 1: Four-condition WikiText-2 PPL @ 50% sparsity (Llama 3.1 8B)"
        rows:
          - "Condition | Seeds | Mean PPL | Std | Δ vs Dense (%)"
          - "Dense (no sparsity) | — | 6.12 | — | —"
          - "BCE-only | 3 | 28.16 | 0.22 | +360.1%"
          - "BCE+compensation | 5 | 9.40 | 0.19 | +53.6%"
          - "KL-only | 5 | 9.80 | 0.87 | +60.1%"
          - "KL+compensation | 3 | 8.95 | 0.13 | +46.2%"
      - title: "Table 1b: Per-seed breakdown"
        rows:
          - "Seed | BCE-only | BCE+comp | KL-only | KL+comp"
          - "s42  | 27.96    | 9.18     | 9.21    | 8.82"
          - "s123 | 28.38    | 9.35     | 9.25    | 8.95"
          - "s456 | 28.14    | 9.52     | 9.14    | 9.08"
          - "s0   | —        | 9.28     | 10.31   | —"
          - "s1   | —        | 9.68     | 11.08   | —"
    figures_description:
      - "Fig 1a: Boxplot of WikiText-2 PPL across 4 conditions. KL-only box明显比BCE+comp宽（whisker覆盖9.14-11.08），且median偏高。BCE+comp box最窄最低。KL+comp最低但仅3 seeds。"
      - "Fig 1b: Per-seed PPL scatter plot with mean±std error bars。突出s0/s1两个KL outlier。"
      - "Fig 1c: Training loss curves (KL loss for KL conditions, BCE loss for BCE conditions)。KL s0和s1的loss曲线后半段出现oscillation，lambda未收敛。"
    analysis: >-
      headline claim "KL eliminates compensation"不成立。BCE+comp (9.40) < KL-only (9.80)，
      且KL-only的高方差使其在deployment中不可靠。
      KL+comp是全局最佳（8.95），但这反证了compensation的通用价值，
      而非KL的独特优势。Narrative需从"KL beats BCE+comp"转向
      "characterization: 不同training signal × compensation的交互效应"。
      唯一保留的KL叙事：KL-only在不使用compensation时确实优于BCE-only（9.80 vs 28.16），
      但这个"免compensation"优势在BCE+comp面前消失。

  # ════════════════════════════════════════════
  # plan_002: STE baseline (P0)
  # ════════════════════════════════════════════
  - name: "STE baseline (KL + Straight-Through Estimator)"
    plan_id: "plan_002"
    description: >-
      用STE替换Gumbel-sigmoid作为梯度通路，保留KL loss不变。
      隔离KL优势来源：loss function还是relaxation method。3 seeds。
    expected_results:
      ste_kl_s42_ppl: 9.85
      ste_kl_s123_ppl: 10.10
      ste_kl_s456_ppl: 9.72
      ste_kl_mean_ppl: 9.89
      ste_kl_std_ppl: 0.19
      ste_kl_model_sparsity: 0.497
      ste_kl_vs_gumbel_kl_gap: +0.09   # STE与Gumbel KL几乎持平
      ste_kl_training_steps_to_converge: 950
    result_rationale: >-
      STE+KL (9.89) ≈ Gumbel+KL (9.80)，差距仅0.09 PPL，在KL-only自身方差（std=0.87）
      内可忽略。这说明Gumbel-sigmoid relaxation对最终质量贡献极小，
      KL loss gradient本身才是驱动因素。
      表面上这支持"KL是关键"——但结合plan_001的结论（BCE+comp追平KL），
      更准确的解读是：任何能传递端到端output-distribution信息的training signal
      （无论STE还是Gumbel路径）都能达到~9.8 PPL，而BCE+comp通过不同路径达到了9.4。
      relaxation method不重要这一事实削弱了论文的technical novelty——
      "Gumbel + KL"不是一个不可替代的组合，STE+KL同样有效。
    tables:
      - title: "Table 2: Gradient estimator ablation (KL loss fixed)"
        rows:
          - "Method | Mean PPL | Std | Sparsity"
          - "Gumbel-sigmoid + KL | 9.80 | 0.87 | 0.498"
          - "STE + KL | 9.89 | 0.19 | 0.497"
          - "BCE-only (ref) | 28.16 | 0.22 | 0.496"
    figures_description:
      - "Fig 2: Training curves overlay — Gumbel+KL vs STE+KL。两条KL loss曲线高度重合，STE略慢收敛（~50 steps），最终值相同。STE的sparsity曲线更平滑（无Gumbel温度退火的阶梯）。"
    analysis: >-
      STE≈Gumbel确认relaxation method不是KL优势的来源。
      但结合BCE+comp追平KL的结果，因果归因链断裂：
      KL的优势不来自relaxation，也不来自"独特的loss function"——
      因为compensation可以弥补BCE的不足。
      论文无法claim "our Gumbel-KL combination is uniquely effective"。
      可作为honest ablation报告，支持characterization study叙事。
      额外发现：STE+KL的std=0.19远低于Gumbel+KL的0.87，
      说明Gumbel温度退火引入了额外的seed sensitivity（进一步削弱Gumbel的必要性）。

  # ════════════════════════════════════════════
  # plan_003: Iso-compute comparison (P0)
  # ════════════════════════════════════════════
  - name: "Iso-compute BCE vs KL"
    plan_id: "plan_003"
    description: >-
      KL每步需full forward pass计算output logits（~2x FLOPs per step vs BCE用cached targets）。
      给BCE等量total FLOPs（extended training），评估compute-normalized比较。3 seeds。
    expected_results:
      kl_flops_per_step: 4.2e14        # FLOPs (bf16 Llama 3.1 8B full fwd)
      bce_flops_per_step: 1.8e14       # predictor only, cached targets
      kl_total_training_flops: 4.2e17  # 1000 steps
      bce_extended_steps: 2333         # matched total FLOPs
      bce_extended_s42_ppl: 24.50
      bce_extended_s123_ppl: 25.10
      bce_extended_s456_ppl: 24.80
      bce_extended_mean_ppl: 24.80
      bce_extended_std_ppl: 0.30
      bce_1000step_mean_ppl: 28.16     # original
      bce_improvement_from_extended: -3.36  # modest improvement
      kl_training_time_min: 42
      bce_extended_training_time_min: 58
    result_rationale: >-
      BCE extended training从28.16降至24.80——额外1333步仅带来3.36 PPL改善。
      BCE的收敛曲线在~800步后进入plateau，更多步数的边际收益递减。
      这是因为BCE的per-neuron factorized gradient本身信息不足：
      无论训练多久，BCE无法学到neuron间的joint interaction。
      但这个结果不支持"KL需要更多compute所以不公平"的reviewer concern——
      即使给BCE等量compute，差距仍然巨大（24.80 vs 9.80）。
      然而结合plan_001，真正的解决方案不是更多BCE training，
      而是加compensation（9.40）——这才是compute的正确使用方式。
    tables:
      - title: "Table 3: Iso-compute comparison"
        rows:
          - "Condition | Steps | Total FLOPs | Mean PPL | Wall Time"
          - "KL-only (1000 steps) | 1000 | 4.2e17 | 9.80 | 42 min"
          - "BCE-only (1000 steps) | 1000 | 1.8e17 | 28.16 | 25 min"
          - "BCE-only (extended, iso-FLOP) | 2333 | 4.2e17 | 24.80 | 58 min"
          - "BCE+comp (1000+500 steps) | 1500 | 3.5e17 | 9.40 | 50 min"
    figures_description:
      - "Fig 3: PPL vs total FLOPs曲线。KL在~4e17 FLOPs处达到9.80；BCE extended在同样FLOPs仅到24.80；BCE+comp在更少FLOPs（3.5e17）就到9.40。说明compute不是瓶颈，compensation architecture才是。"
    analysis: >-
      Iso-compute消除了"KL wins because more compute"的reviewer concern。
      但同时也表明：BCE的瓶颈不是compute，而是loss function的结构性局限。
      当compensation弥补了这个局限后（BCE+comp），以更少compute达到更好结果。
      论文中可诚实报告：KL确实compute-efficient（fewer total FLOPs to reach good quality），
      但"KL eliminates compensation"的claim仍然不成立。

  # ════════════════════════════════════════════
  # plan_004: SPON reimplementation (P0)
  # ════════════════════════════════════════════
  - name: "SPON reimplementation & reproduction"
    plan_id: "plan_004"
    description: >-
      在Llama 3.1 8B上重现SPON（static learnable bias + KL training）。
      5个QA benchmarks验证reproduction质量。
    expected_results:
      spon_wikitext2_ppl: 10.82
      spon_model_sparsity: 0.500
      spon_params_per_layer: 4096       # hidden_dim
      spon_total_params: 131072         # 32 layers × 4096
      spon_training_time_min: 15
      spon_arc_c: 50.2
      spon_arc_e: 77.5
      spon_boolq: 79.8
      spon_piqa: 78.1
      spon_winogrande: 73.6
      published_arc_c: 50.8
      published_arc_e: 78.2
      published_boolq: 80.5
      published_piqa: 78.8
      published_winogrande: 74.2
      reproduction_max_gap: 1.0         # 最大benchmark偏差 < 1 point
    result_rationale: >-
      SPON方法简单（每层仅hidden_dim个learnable参数），超参数空间小，
      reproduction误差主要来自KL训练的随机性和calibration data差异。
      所有5个benchmark与published results差距 < 1 point，reproduction合格。
      PPL=10.82确认static correction的天花板：input-independent bias只能修正
      average-case drift，无法适应per-input neuron importance变化。
      这为plan_005的composition实验提供了valid SPON baseline。
    tables:
      - title: "Table 4: SPON reproduction on 5 QA benchmarks"
        rows:
          - "Benchmark | Published | Ours | Δ"
          - "ARC-c | 50.8 | 50.2 | -0.6"
          - "ARC-e | 78.2 | 77.5 | -0.7"
          - "BoolQ | 80.5 | 79.8 | -0.7"
          - "PIQA | 78.8 | 78.1 | -0.7"
          - "WinoGrande | 74.2 | 73.6 | -0.6"
    figures_description: []
    analysis: >-
      SPON reproduction成功，5个benchmark最大偏差0.7 points。
      PPL=10.82介于KL-only (9.80)和training-free (~12.5)之间，
      符合static correction的预期能力范围。

  # ════════════════════════════════════════════
  # plan_005: SPON + KL composition (P0)
  # ════════════════════════════════════════════
  - name: "SPON + KL predictor composition & additivity test"
    plan_id: "plan_005"
    description: >-
      同时应用SPON bias correction + KL contextual prediction。
      Output-space linearity测试和per-layer正交性分析。3 seeds。
    expected_results:
      # ── Composition PPL ──
      spon_kl_s42_ppl: 9.55
      spon_kl_s123_ppl: 9.78
      spon_kl_s456_ppl: 10.05
      spon_kl_mean_ppl: 9.79
      spon_kl_std_ppl: 0.25
      # ── 基准对比 ──
      spon_only_ppl: 10.82
      kl_only_mean_ppl: 9.80
      teal_baseline_ppl: 12.50
      # ── 可加性测试 ──
      spon_improvement_over_teal: 1.68      # 12.50 - 10.82
      kl_improvement_over_teal: 2.70        # 12.50 - 9.80
      predicted_additive_ppl: 8.12          # 12.50 - 1.68 - 2.70
      actual_combined_ppl: 9.79
      additivity_residual_ppl: 1.67         # 9.79 - 8.12
      additivity_ratio: 0.62               # actual_improvement/predicted_improvement
      # ── Logit-space linearity ──
      logit_residual_norm_ratio: 0.38       # ||Δ(s+c)-Δ(s)-Δ(c)|| / max(||Δ(s)||,||Δ(c)||)
      # ── Per-layer orthogonality ──
      mean_cos_similarity: 0.34            # mean cos(c_s_l, c_θ_l(x)) across layers
      layers_with_cos_gt_03: 20            # /32 layers
      max_cos_similarity_layer: 0.62       # layer 15 (mid-network)
    result_rationale: >-
      SPON+KL (9.79) ≈ KL-only (9.80)——组合几乎没有额外收益。
      predicted additive PPL=8.12 vs actual=9.79，additivity ratio仅0.62。
      原因：SPON的static bias和KL predictor的contextual correction在output space
      高度相关——两者都在修正同一组"容易误杀"的neurons的drift。
      cos similarity分析确认：在中间层（layer 12-20），两种correction方向高度一致
      （cos > 0.4），说明它们修正的是同一类误差而非互补的不同误差源。
      Claim 2（可加性）在worst tier下彻底不成立。
      logit_residual_norm_ratio=0.38 >> 0（如果可加应接近0），
      interaction term不可忽略。
    tables:
      - title: "Table 5: SPON + KL composition results"
        rows:
          - "Condition | PPL | Improvement over TEAL"
          - "TEAL baseline | 12.50 | —"
          - "SPON only | 10.82 | 1.68"
          - "KL only | 9.80 | 2.70"
          - "SPON+KL (actual) | 9.79 | 2.71"
          - "SPON+KL (additive prediction) | 8.12 | 4.38"
      - title: "Table 5b: Additivity metrics"
        rows:
          - "Metric | Value"
          - "Additivity ratio | 0.62"
          - "Logit residual norm ratio | 0.38"
          - "Mean cos(c_s, c_θ) | 0.34"
          - "Layers with cos > 0.3 | 20/32"
    figures_description:
      - "Fig 5a: Per-layer cos similarity heatmap (32 layers × 3 seeds)。中间层（12-20）呈暖色（cos > 0.4），首尾层冷色（cos < 0.2）。说明interaction集中在中间表征层。"
      - "Fig 5b: Logit residual magnitude per layer bar chart。中间层residual最大，与cos similarity pattern一致。"
    analysis: >-
      SPON+KL composition不满足可加性假设（Claim 2不成立）。
      但这本身是一个有价值的empirical finding——
      "static和contextual corrections的overlap分析"可作为standalone贡献。
      论文中不再claim可加性，改为report interaction structure：
      "static和contextual corrections在中间层高度相关，
      suggesting both target the same error mode (average-case neuron importance drift)"。
      这支持characterization study的叙事方向。

  # ════════════════════════════════════════════
  # plan_006: Training-free baselines (P0)
  # ════════════════════════════════════════════
  - name: "Training-free baselines @ 50% sparsity"
    plan_id: "plan_006"
    description: >-
      TEAL (activation magnitude + greedy allocation), WINA (weight-informed scoring),
      R-Sparse (rank-aware scoring)。建立三层比较：training-free < static-learned < contextual-learned。
    expected_results:
      teal_vanilla_ppl: 12.48         # 原始activation magnitude，非predictor scores
      wina_ppl: 15.80
      rsparse_ppl: 14.20
      dense_ppl: 6.12
      teal_vanilla_sparsity: 0.500
      wina_sparsity: 0.500
      rsparse_sparsity: 0.500
      # ── 对比 ──
      teal_vs_dense_pct: 103.9
      wina_vs_dense_pct: 158.2
      rsparse_vs_dense_pct: 132.0
    result_rationale: >-
      TEAL表现最好（12.48），因为activation magnitude是neuron importance的直接proxy，
      加上greedy per-layer allocation自适应地保护关键层。
      R-Sparse (14.20)次之——rank-aware scoring考虑了相对重要性但无跨层allocation。
      WINA最差（15.80）——weight-informed scoring在SwiGLU gate×up结构下信号较弱，
      weight magnitude与activation importance的相关性不如直接用activation。
      这建立了清晰的tier结构：training-free（12-16）<< SPON（10.8）<< contextual（9.4-9.8）。
      注意这里的TEAL使用vanilla activation magnitude（非predictor scores），
      与registry中基于predictor scores的"teal_sparse_ppl"不同。
    tables:
      - title: "Table 6: Training-free baselines @ 50% sparsity"
        rows:
          - "Method | WikiText-2 PPL | Δ vs Dense (%)"
          - "Dense | 6.12 | —"
          - "TEAL (activation magnitude) | 12.48 | +103.9%"
          - "R-Sparse | 14.20 | +132.0%"
          - "WINA | 15.80 | +158.2%"
          - "SPON (static learned) | 10.82 | +76.8%"
          - "KL-only (contextual) | 9.80 | +60.1%"
          - "BCE+comp (contextual) | 9.40 | +53.6%"
    figures_description:
      - "Fig 6: PPL bar chart (horizontal) 按质量排序。清晰展示training-free → static → contextual的层级。BCE+comp和KL-only在误差bar内重叠。"
    analysis: >-
      三层层级结构清晰，training-free到contextual有6-7 PPL points的gap。
      这验证了learned prediction的价值。在worst tier下，
      KL-only和BCE+comp处于同一tier（contextual），彼此差距不显著。
      paper的taxonomy贡献成立：不同training signal在不同granularity下的表现分布
      本身就是有价值的empirical map。

  # ════════════════════════════════════════════
  # plan_007: Full benchmark evaluation (P0)
  # ════════════════════════════════════════════
  - name: "Full benchmark suite + wall-clock profiling"
    plan_id: "plan_007"
    description: >-
      所有条件在Llama 3.1 8B上的完整评估：WikiText-2, C4, ARC-c, WinoGrande, MMLU,
      GSM8K, HumanEval。Wall-clock profiling和Pareto frontier。
    expected_results:
      # ── Dense baselines ──
      dense_wikitext2: 6.12
      dense_c4: 8.85
      dense_arc_c: 53.2
      dense_winogrande: 76.4
      dense_mmlu: 65.8
      dense_gsm8k: 52.1
      dense_humaneval: 31.7
      # ── KL-only ──
      kl_wikitext2: 9.80
      kl_c4: 12.65
      kl_arc_c: 48.2
      kl_winogrande: 69.8
      kl_mmlu: 60.1
      kl_gsm8k: 44.5
      kl_humaneval: 25.0
      kl_mean_acc_drop_vs_dense_pct: 8.9
      # ── BCE+comp ──
      bce_comp_wikitext2: 9.40
      bce_comp_c4: 12.15
      bce_comp_arc_c: 49.5
      bce_comp_winogrande: 71.2
      bce_comp_mmlu: 61.5
      bce_comp_gsm8k: 46.0
      bce_comp_humaneval: 26.5
      bce_comp_mean_acc_drop_vs_dense_pct: 7.4
      # ── SPON ──
      spon_wikitext2: 10.82
      spon_c4: 14.00
      spon_arc_c: 46.5
      spon_winogrande: 67.0
      spon_mmlu: 57.8
      spon_gsm8k: 40.2
      spon_humaneval: 21.0
      # ── SPON+KL ──
      spon_kl_wikitext2: 9.79
      spon_kl_arc_c: 47.8
      spon_kl_mmlu: 59.5
      # ── TEAL (best training-free) ──
      teal_wikitext2: 12.48
      teal_arc_c: 41.5
      teal_mmlu: 52.0
      # ── Wall-clock (tokens/sec, batch=1) ──
      dense_throughput: 42.0
      kl_only_throughput: 56.5          # 1.35x
      bce_comp_throughput: 49.8         # 1.19x
      spon_kl_throughput: 55.8          # 1.33x
      teal_throughput: 58.2             # 1.39x
      # ── Inference memory ──
      kl_only_extra_mem_mb: 48          # predictor only
      bce_comp_extra_mem_mb: 304        # predictor + compensation MLP
    result_rationale: >-
      BCE+comp在6/7个benchmark上优于KL-only（唯一例外HumanEval仅差1.5 points）。
      Mean accuracy drop: BCE+comp 7.4% vs KL-only 8.9%——差距一致且显著。
      原因：compensation MLP通过per-layer修正补偿了BCE predictor的误差，
      提供了比KL更均匀的quality recovery。KL在某些任务（GSM8K -14.6%）
      降幅显著——多步推理任务对sparse noise更敏感，KL的layer-adaptive sparsity
      并未给reasoning带来额外保护。
      
      Wall-clock方面，KL-only (1.35x) > BCE+comp (1.19x)：
      KL唯一的结构性优势是不需要compensation MLP，inference更轻量。
      但0.16x的speedup差距（大致4ms/token on batch=1）
      在多数deployment场景中不是决定性差异。
      BCE+comp的304MB extra memory vs KL的48MB是更显著的差异——
      在memory-constrained edge deployment中KL有优势。
    tables:
      - title: "Table 7: Full benchmark results (Llama 3.1 8B, 50% sparsity)"
        rows:
          - "Method | Wiki-2↓ | C4↓ | ARC-c↑ | WinoG↑ | MMLU↑ | GSM8K↑ | HumanE↑ | Avg Δ%"
          - "Dense | 6.12 | 8.85 | 53.2 | 76.4 | 65.8 | 52.1 | 31.7 | —"
          - "TEAL | 12.48 | 16.50 | 41.5 | 62.0 | 52.0 | 30.5 | 15.0 | -24.8"
          - "SPON | 10.82 | 14.00 | 46.5 | 67.0 | 57.8 | 40.2 | 21.0 | -14.5"
          - "KL-only | 9.80 | 12.65 | 48.2 | 69.8 | 60.1 | 44.5 | 25.0 | -8.9"
          - "BCE+comp | 9.40 | 12.15 | 49.5 | 71.2 | 61.5 | 46.0 | 26.5 | -7.4"
          - "KL+comp | 8.95 | 11.60 | 50.8 | 72.5 | 62.8 | 48.0 | 28.0 | -5.5"
      - title: "Table 7b: Inference profiling"
        rows:
          - "Method | Throughput (tok/s) | Speedup | Extra Memory (MB)"
          - "Dense | 42.0 | 1.00x | 0"
          - "TEAL | 58.2 | 1.39x | 0"
          - "SPON | 57.0 | 1.36x | 0 (absorbed)"
          - "KL-only | 56.5 | 1.35x | 48"
          - "SPON+KL | 55.8 | 1.33x | 48"
          - "BCE+comp | 49.8 | 1.19x | 304"
          - "KL+comp | 49.2 | 1.17x | 304"
    figures_description:
      - "Fig 7a: Pareto frontier (accuracy vs throughput)。X轴=throughput (tok/s), Y轴=mean benchmark accuracy。BCE+comp和KL-only在accuracy维度相近但KL throughput更高——KL在Pareto frontier上略优于BCE+comp（更快同等质量），但KL+comp是accuracy最高点。"
      - "Fig 7b: Radar chart — 5个discriminative benchmarks。BCE+comp的radar面积略大于KL-only。"
      - "Fig 7c: Per-benchmark accuracy drop bar chart (grouped by method)。GSM8K是KL-only的最大弱点（-14.6%）。"
    analysis: >-
      Full evaluation确认worst tier叙事：BCE+comp全面优于KL-only（quality），
      KL-only优势仅在inference efficiency。Pareto分析显示两种方法在
      quality-efficiency tradeoff空间占据不同的niche，不存在一方dominance。
      KL+comp是global best quality但最慢——说明最优方案是KL+comp而非KL alone。
      Paper的Pareto frontier图本身就是有价值的contribution，
      展示了training signal × compensation × granularity的完整landscape。

  # ════════════════════════════════════════════
  # plan_008: Sparsity sweep (P1)
  # ════════════════════════════════════════════
  - name: "7-level sparsity sweep: KL vs BCE s² scaling test"
    plan_id: "plan_008"
    description: >-
      30/35/40/45/50/55/60% sparsity sweep, KL-only vs BCE-only。
      测试Claim 3: KL-BCE delta ~ s²。1 seed per level。
    expected_results:
      # ── KL-only PPL per sparsity ──
      kl_ppl_30: 6.55
      kl_ppl_35: 6.85
      kl_ppl_40: 7.80
      kl_ppl_45: 8.60
      kl_ppl_50: 9.80
      kl_ppl_55: 16.00
      kl_ppl_60: 32.00
      # ── BCE-only PPL per sparsity ──
      bce_ppl_30: 7.50
      bce_ppl_35: 11.50
      bce_ppl_40: 9.80
      bce_ppl_45: 14.50
      bce_ppl_50: 28.00
      bce_ppl_55: 30.00
      bce_ppl_60: 45.00
      # ── Delta (BCE - KL) ──
      delta_30: 0.95
      delta_35: 4.65
      delta_40: 2.00
      delta_45: 5.90
      delta_50: 18.20
      delta_55: 14.00
      delta_60: 13.00
      # ── Scaling fit ──
      r2_delta_vs_s2: 0.66
      r2_delta_vs_s_linear: 0.68
      r2_delta_vs_s2_excluding_high: 0.81   # s ≤ 0.50 only
      quadratic_coeff_a: 74.9
      # ── Taylor expansion accuracy ──
      taylor_second_order_error_50pct: 0.28  # relative error at s=0.50
      taylor_second_order_error_60pct: 0.55  # breaks down at high sparsity
    result_rationale: >-
      Delta呈非单调pattern——在s=0.40处下降（2.00 < 4.65 at s=0.35），
      在s=0.55-0.60处plateau/下降（14.00→13.00）。
      s=0.40异常原因：BCE在某些sparsity level恰好命中"easy"的neuron pruning pattern，
      偶尔表现好于趋势。s=0.55-0.60下降原因：KL本身开始collapse（16→32 PPL），
      两种方法都在高sparsity下崩溃，delta反而缩小。
      
      R²(Δ~s²) = 0.66, R²(Δ~s) = 0.68——linear fit甚至略好于quadratic，
      s²理论叙事不成立。限制在s≤0.50范围内R²=0.81略好，
      但这是cherry-picking range来fit理论。
      
      Taylor expansion在s=0.50已有28%相对误差，在s=0.60达55%。
      O(s²D²) scaling argument的前提是Taylor展开有效——
      高sparsity下高阶项不可忽略，理论prediction失效。
    tables:
      - title: "Table 8a: Sparsity sweep results"
        rows:
          - "Sparsity | s² | KL PPL | BCE PPL | Δ(BCE−KL)"
          - "30% | 0.090 | 6.55 | 7.50 | 0.95"
          - "35% | 0.122 | 6.85 | 11.50 | 4.65"
          - "40% | 0.160 | 7.80 | 9.80 | 2.00"
          - "45% | 0.202 | 8.60 | 14.50 | 5.90"
          - "50% | 0.250 | 9.80 | 28.00 | 18.20"
          - "55% | 0.302 | 16.00 | 30.00 | 14.00"
          - "60% | 0.360 | 32.00 | 45.00 | 13.00"
      - title: "Table 8b: Scaling law fit comparison"
        rows:
          - "Model | R² (all points) | R² (s≤0.50)"
          - "Δ ~ a·s² + b | 0.66 | 0.81"
          - "Δ ~ a·s + b | 0.68 | 0.82"
          - "Δ ~ a·exp(b·s) | 0.72 | 0.78"
    figures_description:
      - "Fig 8a: Δ vs s² scatter plot with linear fit (R²=0.66). 同时叠加Δ vs s的linear fit (R²=0.68, dashed)。两条fit线几乎等好，s²无优势。"
      - "Fig 8b: PPL vs sparsity双曲线（KL and BCE）。KL在s>0.50后急剧上升，BCE在s>0.35后就持续恶化。两者在s=0.55-0.60区间差距缩小。"
      - "Fig 8c: Taylor expansion second-order approximation vs actual delta per sparsity level。在s≥0.50处出现系统性偏差。"
    analysis: >-
      Claim 3（s² scaling）不成立。数据呈现phase-transition而非smooth polynomial关系：
      BCE在s≈0.45-0.50有一个"catastrophic transition"（PPL从14.5跳到28），
      之后plateau；KL在s≈0.55有类似transition（8.6→16）但更晚。
      两个transition point的差异——而非smooth quadratic——才是delta的真正驱动力。
      论文中不应claim s² scaling law，改为报告"BCE exits graceful degradation
      at lower sparsity than KL（~45% vs ~55%），resulting in a phase-transition
      rather than polynomial relationship in the KL-BCE gap"。

  # ════════════════════════════════════════════
  # plan_009: Mistral validation (P1)
  # ════════════════════════════════════════════
  - name: "Mistral-7B-v0.3 generalization validation"
    plan_id: "plan_009"
    description: >-
      Mistral-7B-v0.3上KL-only vs BCE+comp @ 50%。
      Core benchmarks: WikiText-2, ARC-c, MMLU。3 seeds each。
    expected_results:
      mistral_dense_ppl: 7.82
      # ── KL-only ──
      mistral_kl_s42_ppl: 14.10
      mistral_kl_s123_ppl: 14.85
      mistral_kl_s456_ppl: 13.50
      mistral_kl_mean_ppl: 14.15
      mistral_kl_std_ppl: 0.68
      mistral_kl_ppl_increase_pct: 80.9
      mistral_kl_arc_c: 41.5
      mistral_kl_mmlu: 51.8
      # ── BCE+comp ──
      mistral_bce_comp_s42_ppl: 12.50
      mistral_bce_comp_s123_ppl: 12.80
      mistral_bce_comp_s456_ppl: 13.10
      mistral_bce_comp_mean_ppl: 12.80
      mistral_bce_comp_std_ppl: 0.30
      mistral_bce_comp_ppl_increase_pct: 63.7
      mistral_bce_comp_arc_c: 44.8
      mistral_bce_comp_mmlu: 55.2
      # ── Gap ──
      mistral_kl_vs_bce_comp_gap: +1.35    # KL worse, direction reversed
      mistral_dense_arc_c: 49.5
      mistral_dense_mmlu: 62.0
    result_rationale: >-
      Mistral-7B-v0.3使用GQA + sliding window attention，
      KV cache结构与Llama 3.1不同（GQA → 更少的KV heads，信息更集中）。
      KL训练依赖full output distribution匹配——Mistral的sliding window
      导致不同position的logit distribution变化更剧烈，
      KL predictor更难学习稳定的mask pattern。
      
      BCE+comp在Mistral上表现更好（12.80 vs 14.15），
      gap进一步扩大到+1.35（Llama上是+0.40）。
      compensation MLP通过直接修正sparse output对architecture更鲁棒，
      不依赖output distribution的稳定性。
      
      KL PPL increase 80.9%在target range [60, 120]内。
      这彻底否定了KL优势的generalizability——
      在第二个architecture上，方向反转且差距更大。
    tables:
      - title: "Table 9: Mistral-7B-v0.3 results @ 50% sparsity"
        rows:
          - "Method | PPL | Δ vs Dense (%) | ARC-c | MMLU"
          - "Dense | 7.82 | — | 49.5 | 62.0"
          - "KL-only | 14.15±0.68 | +80.9 | 41.5 | 51.8"
          - "BCE+comp | 12.80±0.30 | +63.7 | 44.8 | 55.2"
      - title: "Table 9b: Cross-architecture comparison"
        rows:
          - "Architecture | KL-only PPL Δ% | BCE+comp PPL Δ% | KL−BCE_comp gap"
          - "Llama 3.1 8B | +60.1 | +53.6 | +0.40"
          - "Mistral-7B-v0.3 | +80.9 | +63.7 | +1.35"
    figures_description:
      - "Fig 9: Cross-architecture bar chart。两个model分组，每组KL和BCE+comp并列。Llama上gap小（0.40），Mistral上gap大（1.35）且方向一致（BCE+comp更好）。"
    analysis: >-
      Mistral结果是worst tier的strongest evidence。
      不仅KL不优于BCE+comp，差距还在第二个architecture上放大了。
      这说明KL的"优势"（如果存在）是architecture-dependent的，
      不具备generalize条件。论文中必须诚实报告cross-architecture inconsistency，
      并在characterization framework下解释：
      "KL-only的effectiveness取决于output distribution的per-layer stability，
      而这是architecture-dependent的property"。

  # ════════════════════════════════════════════
  # plan_010: LongBench evaluation (P1)
  # ════════════════════════════════════════════
  - name: "LongBench English subset evaluation (4K-32K)"
    plan_id: "plan_010"
    description: >-
      全条件在LongBench English subset上评估。
      Per-task-type breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。
    expected_results:
      # ── Dense baselines (F1/ROUGE) ──
      dense_single_doc_qa: 22.0
      dense_multi_doc_qa: 35.0
      dense_summarization: 28.0
      dense_few_shot: 68.0
      dense_code: 55.0
      # ── KL-only ──
      kl_single_doc_qa: 17.2
      kl_multi_doc_qa: 26.5
      kl_summarization: 21.5
      kl_few_shot: 59.5
      kl_code: 46.0
      kl_longbench_avg_drop_pct: 18.5
      # ── BCE+comp ──
      bce_comp_single_doc_qa: 18.5
      bce_comp_multi_doc_qa: 28.8
      bce_comp_summarization: 23.2
      bce_comp_few_shot: 61.0
      bce_comp_code: 47.5
      bce_comp_longbench_avg_drop_pct: 14.2
      # ── SPON+KL ──
      spon_kl_single_doc_qa: 17.8
      spon_kl_multi_doc_qa: 27.0
      spon_kl_few_shot: 60.0
      # ── TEAL ──
      teal_single_doc_qa: 13.5
      teal_multi_doc_qa: 20.0
      teal_few_shot: 50.0
    result_rationale: >-
      长文本任务放大了sparse prediction的错误累积效应。
      KL predictor在训练时用512-token sequences——
      长context下distribution shift导致predictor的mask decisions drift，
      错误在long-range dependencies中逐步放大。
      
      BCE+comp的compensation MLP提供了per-layer error correction，
      对distribution shift更鲁棒——即使mask不完美，compensation能部分修正。
      Multi-doc QA差距最大（26.5 vs 28.8，8.7% gap），
      因为multi-doc需要跨文档信息整合，sparse noise影响cross-document attention。
      
      SPON+KL (17.8 single-doc) 仅略优于KL-only (17.2)，
      再次确认SPON+KL的非可加性——在long context下也如此。
    tables:
      - title: "Table 10: LongBench per-task-type results"
        rows:
          - "Task Type | Dense | KL-only | BCE+comp | SPON+KL | TEAL"
          - "Single-doc QA | 22.0 | 17.2 | 18.5 | 17.8 | 13.5"
          - "Multi-doc QA | 35.0 | 26.5 | 28.8 | 27.0 | 20.0"
          - "Summarization | 28.0 | 21.5 | 23.2 | 22.0 | 16.5"
          - "Few-shot | 68.0 | 59.5 | 61.0 | 60.0 | 50.0"
          - "Code | 55.0 | 46.0 | 47.5 | 46.5 | 38.0"
          - "Avg Drop % | — | -18.5 | -14.2 | -16.8 | -32.5"
    figures_description:
      - "Fig 10: Grouped bar chart per task type。每组5个bars (Dense, KL, BCE+comp, SPON+KL, TEAL)。BCE+comp一致优于KL-only，差距在multi-doc QA最大。"
    analysis: >-
      Long context进一步支持worst tier叙事——
      KL-only的degradation在long context下比short context更严重
      （avg drop 18.5% vs short-context benchmarks的8.9%）。
      BCE+comp更鲁棒（14.2% vs 18.5%），compensation提供了error buffering。
      这对NLP venue特别重要——long-context capability是EMNLP reviewer关注的重点。

  # ════════════════════════════════════════════
  # plan_011: MT-Bench (P2)
  # ════════════════════════════════════════════
  - name: "MT-Bench evaluation (GPT-4o judge)"
    plan_id: "plan_011"
    description: >-
      80个multi-turn questions, 8个categories。GPT-4o作为judge。
      测试instruction-following quality under sparsity。
    expected_results:
      dense_mt_bench_avg: 7.20
      kl_mt_bench_avg: 5.95
      bce_comp_mt_bench_avg: 6.30
      spon_kl_mt_bench_avg: 6.05
      teal_mt_bench_avg: 4.80
      # ── Per-category (selected) ──
      kl_writing: 6.5
      kl_reasoning: 5.2
      kl_math: 4.8
      kl_coding: 5.5
      bce_comp_writing: 6.8
      bce_comp_reasoning: 5.8
      bce_comp_math: 5.2
      bce_comp_coding: 5.9
    result_rationale: >-
      MT-Bench是multi-turn对话质量的综合测试。
      KL-only (5.95) vs BCE+comp (6.30)——差距0.35分在MT-Bench scale上有意义。
      Reasoning和math categories差距最大（0.6和0.4分），
      因为多步推理对intermediate representation的准确性要求高，
      sparse noise在turn间累积。
      Compensation MLP提供的error correction在multi-turn setting下尤其有价值，
      每个turn的correction防止error向后续turns propagation。
    tables:
      - title: "Table 11: MT-Bench scores (GPT-4o judge)"
        rows:
          - "Method | Avg | Writing | Reasoning | Math | Coding | Roleplay | Extraction | STEM | Humanities"
          - "Dense | 7.20 | 7.8 | 6.8 | 6.5 | 7.0 | 7.5 | 7.2 | 7.0 | 7.8"
          - "KL-only | 5.95 | 6.5 | 5.2 | 4.8 | 5.5 | 6.5 | 6.0 | 5.8 | 6.3"
          - "BCE+comp | 6.30 | 6.8 | 5.8 | 5.2 | 5.9 | 6.8 | 6.2 | 6.2 | 6.5"
          - "SPON+KL | 6.05 | 6.6 | 5.3 | 4.9 | 5.6 | 6.5 | 6.1 | 5.9 | 6.5"
          - "TEAL | 4.80 | 5.2 | 4.0 | 3.5 | 4.5 | 5.5 | 4.8 | 4.5 | 5.0"
    figures_description:
      - "Fig 11: MT-Bench radar chart (8 categories)。Dense最大，BCE+comp > KL-only在所有categories。Reasoning/Math差距最明显。"
    analysis: >-
      MT-Bench确认了downstream quality ordering: BCE+comp > KL-only。
      在NLP-relevant的instruction-following setting下，
      compensation的error correction在multi-turn中有cumulative benefit。
      对EMNLP submission有利——MT-Bench直接评估NLP应用质量。

  # ════════════════════════════════════════════
  # plan_012: RULER synthetic long-context (P2)
  # ════════════════════════════════════════════
  - name: "RULER synthetic long-context evaluation"
    plan_id: "plan_012"
    description: >-
      RULER (4K, 16K) × 3 task types: NIAH-Single, NIAH-MultiKey, Variable Tracking。
      Fine-grained capability diagnostics。
    expected_results:
      # ── Dense ──
      dense_niah_s_4k: 98.0
      dense_niah_s_16k: 92.0
      dense_niah_mk_4k: 85.0
      dense_niah_mk_16k: 70.0
      dense_vt_4k: 80.0
      dense_vt_16k: 62.0
      # ── KL-only ──
      kl_niah_s_4k: 88.0
      kl_niah_s_16k: 70.0
      kl_niah_mk_4k: 71.0
      kl_niah_mk_16k: 45.0
      kl_vt_4k: 64.0
      kl_vt_16k: 35.0
      # ── BCE+comp ──
      bce_comp_niah_s_4k: 91.0
      bce_comp_niah_s_16k: 76.0
      bce_comp_niah_mk_4k: 75.0
      bce_comp_niah_mk_16k: 52.0
      bce_comp_vt_4k: 68.0
      bce_comp_vt_16k: 42.0
      # ── Key degradation patterns ──
      kl_16k_avg_drop_vs_dense: 31.3
      bce_comp_16k_avg_drop_vs_dense: 23.5
    result_rationale: >-
      RULER的synthetic tasks提供了controlled capability measurement。
      16K context下KL-only降幅最大——NIAH-MultiKey从85→45（-47.1%），
      Variable Tracking从62→35（-43.5%）。
      这些任务需要精确的long-range retrieval和state tracking，
      sparse noise在16K tokens范围内严重干扰attention pattern。
      
      BCE+comp在所有6个setting上优于KL-only，
      16K的NIAH-MultiKey差距7 points（52 vs 45），VT差距7 points（42 vs 35）。
      Compensation的per-layer correction在长序列下提供了持续的error mitigation。
      
      KL在4K→16K的degradation slope比BCE+comp更陡，
      说明KL predictor的mask decision在序列长度增加时快速恶化——
      进一步支持"KL的训练信号不够robust"的worst-tier叙事。
    tables:
      - title: "Table 12: RULER results (accuracy %)"
        rows:
          - "Task | Context | Dense | KL-only | BCE+comp | Δ(KL vs BCE+comp)"
          - "NIAH-S | 4K | 98.0 | 88.0 | 91.0 | -3.0"
          - "NIAH-S | 16K | 92.0 | 70.0 | 76.0 | -6.0"
          - "NIAH-MK | 4K | 85.0 | 71.0 | 75.0 | -4.0"
          - "NIAH-MK | 16K | 70.0 | 45.0 | 52.0 | -7.0"
          - "VT | 4K | 80.0 | 64.0 | 68.0 | -4.0"
          - "VT | 16K | 62.0 | 35.0 | 42.0 | -7.0"
    figures_description:
      - "Fig 12: Heatmap (method × task-context)。颜色深浅表示accuracy。KL-only在16K列明显偏暗，BCE+comp介于Dense和KL之间。"
    analysis: >-
      RULER的controlled diagnostics是worst tier的fine-grained evidence。
      KL-only在长序列上的capability loss pattern清晰且一致，
      作为EMNLP paper的补充diagnostics有说服力。
      但RULER本身是P2 priority——如果时间不足，
      LongBench (plan_010)已经cover了long-context方向，
      RULER提供的是complementary validation而非必要条件。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4e01231-e91c-4280-9496-3a26caf0feb1",
  "isSidechain": false,
  "requestId": "req_011Cb4jNG27g4sf5tbE4f6td",
  "type": "assistant",
  "uuid": "2b156387-de26-413a-8f2e-1656b6af8121",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLPfMdHtxBTEgsVVbF59LT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8837,
      "cache_read_input_tokens": 42220,
      "output_tokens": 31065,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 31065,
          "cache_read_input_tokens": 42220,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：KL优势是假象——BCE缺compensation导致的baseline weakness，而非loss function的内在优势。加上compensation后BCE追平或反超KL 核心假设：['KL-only PPL 方差比MVP显示的更大（std > 0.8，部分seeds > 11），稳定性存疑'…",
  "leafUuid": "2b156387-de26-413a-8f2e-1656b6af8121",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical decomposition of KL vs BCE for activation sparsity under worst-case scenario",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：KL优势是假象——BCE缺compensation导致的baseline weakness，而非loss function的内在优势。加上compensation后BCE追平或反超KL 核心假设：['KL-only PPL 方差比MVP显示的更大（std > 0.8，部分seeds > 11），稳定性存疑'…",
  "leafUuid": "2b156387-de26-413a-8f2e-1656b6af8121",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Empirical decomposition of KL vs BCE for activation sparsity under worst-case scenario",
  "sessionId": "9c35e2d0-bc09-4233-9980-737e00198e60"
}
```

---
