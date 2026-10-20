# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：C1 ablation 显示 mask quality 解释大部分但非全部 KL 优势（存在 2-3 PPL residual gap）；部分实验噪

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/33853d9f-17d4-414b-b622-19f35e1aa725.jsonl`
- **Structured JSON:** [`b2120d5944df05c03158.json`](../../sessions/b2/b2120d5944df05c03158.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T16:40:26.127Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T16:40:26.127Z",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：C1 ablation 显示 mask quality 解释大部分但非全部 KL 优势（存在 2-3 PPL residual gap）；部分实验噪声偏大；需调整 claim 强度和补充讨论\n核心假设：['BCE-on-KL-targets at 50% uniform PPL 在 12.5-15.0——优于 vanilla BCE（28.0）但劣于 KL（11.8），residual gap 表明 optimization dynamics 也独立贡献', 'BCE 30% forced top-k PPL 在 10.0-13.0——低 sparsity 下 gap 缩小，KL 优势非均匀', '6-point sweep 趋势可辨但个别点偏离，regime 边界模糊 ±5pp', 'KL 30% uniform 3-seed MMLU σ 2-4pp，需要 carefully present mean±CI 而非 cherry-pick', \"至少 1 位 reviewer 质疑 novelty（'KL distillation is well-known'），至少 1 位指出 14B gap\", '部分 sweep 实验（25%/45%）在 deadline 前未完成，用 4-point 数据替代']\n关键指标范围：{'c1_ablation_uniform_50pct_ppl': [12.5, 15.0], 'bce_30pct_forced_topk_ppl': [10.0, 13.0], 'kl_30pct_uniform_3seed_mmlu_std_pp': [2.0, 4.0], 'regime_piecewise_fit_r2': [0.8, 0.93], 'expected_ARR_overall': [3.0, 3.5]}\n叙事方向：'Mask pattern discovery' 降级为 'mask pattern divergence is a major contributing factor'。 C1 ablation residual gap（2-3 PPL）需要诚实报告并归因：mask quality 解释 ~60-75% 的 KL 优势，continuous optimization（Gumbel relaxation + end-to-end gradient flow）贡献余下部分。 Contribution 1 改写为 'KL improves BOTH mask quality AND optimization fidelity, with mask quality as the dominant factor'——需要增加一段 discussion 解耦两者。Phase transition（Claim 3） 从 bonus 提升为 co-equal contribution 以补偿 C1 削弱的 novelty。如果 BCE 30% gap 不够大， 强调 sparsity-dependent advantage（50% 差距 2.3×，30% 差距逐渐缩小——这本身是 regime analysis 的一部分）。Paper 可能首轮进 Findings；通过 revision 补充缺失 sweep 数据争取 Main。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: distill_sparse_swiglu\nfocus: 测试论文 reframe 为 'mask pattern discovery' 叙事的接收度。核心变化：Contribution 1 从 gradient coupling 转为 optimization target quality / mask pattern divergence。§3.6 gradient analysis 降为 suggestive motivation。C1 ablation 变成 paper 核心实验。53% mask divergence 作为新发现。目标 4.0 Main Conference accept。\n\n## paper_framing.md\n\n# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \"unfair comparison\" attacks. **Iso-compute evidence (eval_bce_v3_s42)**: with 2.71× more gradient updates, BCE TEAL PPL=27.97 vs KL=12.00 (2.33× gap persists), and BCE loss saturates (step 500→2700: Δ=-0.006). The advantage is structural: BCE optimizes per-neuron binary classification, but inference uses global top-k budget allocation — per-neuron scoring is suboptimal under global reallocation. KL directly optimizes output distribution, naturally compatible with any allocation strategy. (Headline claim)\n\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \"subsuming\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)\n\n3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports \"PPL is a poor proxy for downstream quality\" narrative. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.\n\n- **Our framing / headline question**: \"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\n\n- **Headline result template**: \"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] quality but adds 67.2M parameters ([W] ms/token overhead) — demonstrating that output-distribution distillation renders error compensation unnecessary—SPON's residual correction is orthogonal to KL's dominant effect and too weak to complement it—enabling a simpler, lighter inference pipeline with strictly better efficiency-quality tradeoff.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\n\n2. **\"KL wins only because more compute\"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 (plan_009, GQA + sliding window) and Qwen-2.5-14B cross-scale validation (D048/D054). **14B mixed result**: KL PPL advantage preserved (7.62 vs TEAL 8.73, 1.47× dense ratio identical to 8B), but KL MMLU=63.72% (global) / 64.49% (uniform) significantly trails TEAL 71.83% (global). Uniform allocation does not fix this gap (D054). PPL-downstream disconnect at 14B scale is an honest limitation, not hidden. Framing: KL's coupled gradient captures output-distribution fidelity (PPL) across scales, but 14B knowledge-intensive tasks (MMLU) show scale-dependent sensitivity that warrants further investigation.\n\n5. **\"Effect size may not hold on downstream tasks\"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.\n\n6. **\"Unfair comparison: BCE+comp close to KL but at higher inference cost\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:\n    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline\n    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds\n    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and\n    BCE-only 3 seeds (mvp_bce_s42/s123/s456).\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_ids:\n  - mvp_kl_norm_v2_s42\n  - mvp_kl_norm_v2_s123\n  - mvp_kl_norm_v2_s456\n  - mvp_bce_s42\n  - mvp_bce_s123\n  - mvp_bce_s456\n  remaining_runs:\n  - KL-only 2 additional seeds (s0, s1) for 5-seed headline\n  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)\n  - KL+comp 3 seeds (s42, s123, s456)\n  registry_id: kl_only_s1\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- id: plan_002\n  claim: 1\n  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).\n    Isolates whether KL advantage comes from loss function or relaxation method. 3\n    seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: ste_baseline_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- id: plan_003\n  claim: 1\n  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs\n    (KL requires full forward pass for output logits, BCE can use cached targets).\n    Report per-step FLOPs and total training time for both. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: bce_isocompute_v2_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- id: plan_004\n  claim: 2\n  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL\n    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,\n    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: spon_2048_s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- id: plan_005\n  claim: 2\n  description: 'SPON subsumption verification: output-space linearity test showing\n    KL predictor already captures SPON correction signal. ||Delta_logits(s+c) - Delta_logits(s)\n    - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality analysis.\n    Proves SPON+KL ≈ KL (no additive gain). 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  - plan_004\n  registry_id: plan_005_subsumption_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- id: plan_006\n  claim: 1\n  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:\n    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),\n    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free\n    < static-learned < contextual-learned.\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_ids:\n  - training_free_baselines\n  - training_free_wina_greedy\n  registry_id: training_free_baselines\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2\n    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor\n    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto\n    frontier plot.\n\n    '\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  - plan_004\n  - plan_005\n  - plan_006\n  registry_id: bench_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- id: plan_008\n  claim: 3\n  description: '3-level sparsity sweep (30%/50%/70%): KL-only vs BCE-only. Test scaling\n    trend and KL-BCE delta growth. 1 seed per level (sweep analysis, not headline).\n    50% data point reused from plan_001. If 3 levels show non-linear inflection, add\n    intermediate points.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  registry_id: d030_kl50_uniform\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- id: plan_009\n  claim: 1\n  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%\n    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds\n    each condition.\n\n    '\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: lm_eval_mistral_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions\n    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:\n    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization\n    beyond short training sequences.\n\n    '\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 2\n  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8\n    categories. All conditions. Tests instruction-following quality under sparsity.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative\n    task types. Fine-grained capability diagnostics complementing LongBench.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_total_loss: 3.3438\n    final_kl_loss: 3.2969\n    final_reg_loss: 0.05\n    final_sparsity: 0\n    steps: 1000\n    tau_final: 0.1\n    wikitext2_ppl_dense: 6.12\n    wikitext2_ppl_sparse: 455.93\n    wikitext2_ppl_increase_pct: 7349\n    model_level_sparsity: 0.372\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\n- exp_id: mvp_kl_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_kl_s456\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_bce_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 27.9603\n    teal_sparse_ppl: 44.537\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 628\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.3817\n    teal_sparse_ppl: 44.5864\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 629\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.1437\n    teal_sparse_ppl: 43.033\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 603.3\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_lagrangian_quicktest\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_kl_loss: 418\n    final_constraint_loss: 1.211\n    final_sparsity: 0.141\n    final_lambda: 5.06\n    steps: 200\n    sparsity_trajectory:\n    - 0.406\n    - 0.387\n    - 0.289\n    - 0.168\n    - 0.141\n- exp_id: kl_lagrangian_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_normalized_quicktest\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step1_kl: 1.18\n    step200_kl: 0.641\n    step200_sparsity: 0.504\n    final_lambda: 8\n    sparsity_converged_step: 80\n    sparsity_trajectory:\n    - 0.406\n    - 0.398\n    - 0.398\n    - 0.457\n    - 0.52\n    - 0.506\n    - 0.504\n    - 0.504\n    lambda_trajectory:\n    - 1\n    - 2\n    - 4\n    - 8\n    - 8\n    - 8\n    - 8\n    - 8\n- exp_id: mvp_kl_norm_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_norm_v3_quicktest\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics:\n    step1_kl_raw: 1.1797\n    step1_kl_norm: 1.1797\n    step1_sparsity: 0.406\n    step1_lambda: 2\n    step50_kl_raw: 0.7344\n    step50_kl_norm: 0.7344\n    step50_sparsity: 0.514\n    step50_lambda: 1.95\n    step100_kl_raw: 0.625\n    step100_kl_norm: 0.625\n    step100_sparsity: 0.496\n    step100_lambda: 1000\n    step150_kl_raw: 0.5703\n    step150_kl_norm: 0.5703\n    step150_sparsity: 0.48\n    step150_lambda: 1000\n    step200_kl_raw: 0.6836\n    step200_kl_norm: 0.6836\n    step200_sparsity: 0.477\n    step200_lambda: 1000\n    step200_constraint: 0.01178\n    kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)\n    sparsity_range: 0.477-0.514 after step 50\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\n- exp_id: mvp_kl_norm_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2142\n    teal_sparse_ppl: 12.0776\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 97.4\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2474\n    teal_sparse_ppl: 11.9128\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 94.7\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.14\n    teal_sparse_ppl: 13.58\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 121.9\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_only_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.19\n    teal_sparse_ppl: 12.03\n    model_level_sparsity: 0.499\n    ppl_increase_vs_true_dense_pct: 96.57\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: kl_only_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- exp_id: spon_training\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1193\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 9.0977\n    spon_recovery_pct: 3.8\n    ppl_improvement_from_spon: 0.1188\n    ppl_increase_vs_true_dense_pct: 48.7\n    ppl_increase_no_spon_vs_true_dense_pct: 50.6\n    mean_bias_norm: 0.040596\n    max_bias_norm: 0.054199\n    teal_sparse_ppl: 12.08\n    teal_with_spon_ppl: 11.93\n    spon_dense_ppl_degradation: 6.19\n    model_level_sparsity: 0.5\n    eval_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n- exp_id: spon_kl_s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: bce_comp_staged_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 25.44\n    predictor_hard_mask_ppl_no_comp: 27.96\n    teal_sparse_ppl: 44.54\n    model_level_sparsity: 0.558\n    ppl_increase_vs_true_dense_pct: 315.7\n    comp_loss_final: 0.0033\n    bce_loss_final: 0.6379\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: training_free_baselines\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- exp_id: spon_training_seq2048\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: ste_baseline_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- exp_id: spon_2048_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- exp_id: ste_kl_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: training_free_wina_greedy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wina_greedy_ppl: 2126.03\n    dense_ppl: 6.12\n    model_level_sparsity: 0.5\n    eval_dataset: WikiText-2\n    eval_seq_len: 2048\n    greedy_allocation_summary: 'layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80,\n      layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24:\n      0.05-0.15, layers 25-31: 0.00'\n- exp_id: bce_isocompute_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_spon_supp_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: spon_supp_eval_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- exp_id: plan_005_subsumption_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- exp_id: kl_sparsity30_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity70_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_loss: 0.1465\n    kl_normalized: 0.1465\n    kl_raw: 0.1465\n    model_level_sparsity: 0.281\n    sparsity_target: 0.3\n    lambda_sparse_final: 1000\n    lambda_max_cap: 1000\n    tau_final: 0.1\n    constraint_loss_final: 0\n    training_steps: 1000\n    wall_clock_seconds: 2662.6\n    gpu_hours: 0.74\n    note: No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1).\n      Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run\n      was offline (not synced).\n- exp_id: kl_sparsity70_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 13.84\n    predictor_teal_sparse_ppl: 17.91\n    vanilla_teal_sparse_ppl: 100.11\n    teal_sparse_ppl: 17.91\n    teal_sparse_ppl_static_baseline: 17.91\n    model_level_sparsity: 0.7\n    teal_sparse_note: '17.91 = predictor-based TEAL (teal_global_masks: predictor-gated\n      magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py\n      L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct\n      metadata 有误导性.'\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    per_layer_sparsity_range:\n    - 0.508\n    - 0.876\n- exp_id: kl_sparsity30_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    loss: 0.165\n    kl_normalized: 0.165\n    kl_raw: 0.165\n    sparsity: 0.285\n    lambda_sparse: 5000\n    tau: 0.1\n    constraint_loss: 0\n    steps: 1000\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    teal_sparse_ppl_note: 已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\n    model_level_sparsity: 0.3\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n- exp_id: mistral_kl_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_final_loss: 0.2188\n    train_final_kl_raw: 0.2188\n    train_final_kl_norm: 0.2188\n    train_final_constraint: 0\n    train_final_sparsity: 0.48\n    train_final_lambda: 1000\n    train_final_tau: 0.1\n    train_steps_completed: 1000\n    true_dense_ppl: 5.52\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    model_level_sparsity: 0.5\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_samples: 159\n- exp_id: lm_eval_dense_test\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc_norm: 0.3771\n    winogrande_acc: 0.6156\n    mmlu_acc: 0.2591\n    gsm8k_exact_match: 0.0121\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: kl_sparse_50pct\n    server: westd-34887\n    exit_code: 129\n    wall_time_sec: 3010\n    flag: SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\n- exp_id: lm_eval_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.5819\n    winogrande_acc: 0.7814\n    mmlu_acc: 0.6532\n    gsm8k_exact_match: 0.5004\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: dense\n    server: westd-34887\n- exp_id: lm_eval_mistral_downstream\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_mistral_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- exp_id: diag_30pct_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_gsm8k_gencomp\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_teal_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: lm_eval_kl_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.3575\n    arc_challenge_acc_norm: 0.3737\n    winogrande_acc: 0.6756\n    mmlu_acc: 0.2874\n    gsm8k_exact_match_strict: 0.0743\n    gsm8k_exact_match_flexible: 0.0781\n    actual_sparsity: 0.3\n    model: llama-3.1-8b\n    condition: kl_distill_30pct_sparsity_s42\n    mmlu_stem_acc: 0.2499\n    mmlu_social_sciences_acc: 0.2896\n    mmlu_humanities_acc: 0.2786\n    mmlu_other_acc: 0.3363\n- exp_id: gsm8k_gen_compare\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: lm_eval_teal_50pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: vanilla_teal\n    sparsity: 0.5\n    actual_sparsity: 0.5\n    arc_challenge_acc_norm: 0.291\n    winogrande_acc: 0.5556\n    mmlu_acc: 0.2856\n    gsm8k_exact_match_flexible: 0.019\n    gsm8k_exact_match_strict: 0.0114\n    arc_challenge_drop_vs_dense: -0.5\n    winogrande_drop_vs_dense: -0.289\n    mmlu_drop_vs_dense: -0.563\n    gsm8k_drop_vs_dense: -0.962\n    model: Llama-3.1-8B\n    condition: TEAL 50% training-free sparsity\n- exp_id: lm_eval_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge:\n      acc: 0.3933\n      acc_norm: 0.4155\n      acc_stderr: 0.0143\n      acc_norm_stderr: 0.0144\n    winogrande:\n      acc: 0.6559\n      acc_stderr: 0.0134\n    mmlu:\n      acc: 0.3598\n      acc_stderr: 0.004\n    mmlu_stem:\n      acc: 0.313\n    mmlu_humanities:\n      acc: 0.3305\n    mmlu_social_sciences:\n      acc: 0.4108\n    mmlu_other:\n      acc: 0.401\n    gsm8k:\n      exact_match_strict: 0.0849\n      exact_match_flexible: 0.0925\n      strict_stderr: 0.0077\n      flexible_stderr: 0.008\n    actual_sparsity: 0.3\n- exp_id: lm_eval_mistral_kl_50pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.2927\n    arc_challenge_acc_norm: 0.3183\n    arc_challenge_acc_norm_stderr: 0.0136\n    winogrande_acc: 0.629\n    winogrande_acc_stderr: 0.0136\n    mmlu_acc: 0.2295\n    mmlu_acc_stderr: 0.0035\n    mmlu_stem_acc: 0.2125\n    mmlu_humanities_acc: 0.2421\n    mmlu_social_sciences_acc: 0.2171\n    mmlu_other_acc: 0.2398\n    gsm8k_exact_match_strict: 0.0045\n    gsm8k_exact_match_flexible: 0.0212\n    model: Mistral-7B-v0.3\n    condition: kl_distill_50pct_sparsity_s42\n    arc_challenge_retention_vs_dense: 0.528\n    winogrande_retention_vs_dense: 0.799\n    mmlu_retention_vs_dense: 0.368\n    gsm8k_retention_vs_dense: 0.012\n- exp_id: d030_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n    allocation: uniform\n    per_layer_sparsity: uniform 0.301 across all 32 layers\n    mmlu_improvement_vs_global: +11.87pp (0.2874 → 0.4061)\n    gsm8k_change_vs_global: no change (0.0743 → 0.0735, within noise)\n- exp_id: bce_isocompute_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 2700\n    loss: 0.6382\n    bce_loss: 0.6371\n    reg_loss: 0.001\n    sparsity: 0.51\n    training_time_seconds: 2828\n    note: 'BCE saturation confirmed: step 500→2700 only 0.006 improvement'\n- exp_id: bench_mistral_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: d030_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- exp_id: bench_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- exp_id: eval_kl30_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    sparsity_target: 0.3\n    actual_sparsity: 0.3\n- exp_id: d030_kl40_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3627\n    arc_challenge_acc_norm: 0.4181\n    winogrande_acc: 0.6717\n    mmlu_acc: 0.3068\n    gsm8k_exact_match: 0.0394\n    actual_sparsity: 0.398\n- exp_id: eval_bce_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 22.51\n    teal_sparse_ppl: 27.97\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2048\n    arc_challenge_acc_norm: 0.2398\n    arc_challenge_acc_norm_stderr: 0.0125\n    winogrande_acc: 0.5059\n    winogrande_acc_stderr: 0.0141\n    mmlu_acc: 0.3002\n    mmlu_acc_stderr: 0.0038\n    gsm8k_exact_match: 0.0485\n    gsm8k_exact_match_strict: 0.0425\n    gsm8k_exact_match_stderr: 0.0059\n- exp_id: bench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n- exp_id: bench_kl50_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n    actual_sparsity: 0.5\n- exp_id: bench_kl30_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    arc_challenge_acc_norm: 0.3968\n    winogrande_acc: 0.7017\n    mmlu_acc: 0.2527\n    gsm8k_exact_match: 0.0879\n    actual_sparsity: 0.3\n- exp_id: bench_teal30\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.97\n    arc_challenge_acc_norm: 0.4232\n    winogrande_acc: 0.6606\n    mmlu_acc: 0.3861\n    gsm8k_exact_match: 0.0788\n    actual_sparsity: 0.3\n- exp_id: bench_teal50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 23.31\n    arc_challenge_acc_norm: 0.2841\n    winogrande_acc: 0.5304\n    mmlu_acc: 0.2832\n    gsm8k_exact_match: 0.0197\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.963\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: bench_kl40_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.117\n    arc_challenge_acc_norm: 0.4096\n    winogrande_acc: 0.6535\n    mmlu_acc: 0.3806\n    gsm8k_exact_match: 0.05\n    actual_sparsity: 0.4\n- exp_id: longbench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v5\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: latency_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpu_model: NVIDIA RTX PRO 6000 Blackwell Server Edition\n    dtype: float16\n    attn: flash_attention_2\n    batch: 1\n    seq_len: 2048\n    warmup: 10\n    iters: 100\n    dense_ms: 119.11\n    dense_std: 0.57\n    dense_tokens_per_s: 17194.5\n    kl_30pct_ms: 126.64\n    kl_30pct_std: 0.7\n    kl_30pct_tokens_per_s: 16171.8\n    kl_30pct_speedup: 0.941\n    kl_50pct_ms: 126.78\n    kl_50pct_std: 0.31\n    kl_50pct_tokens_per_s: 16154.2\n    kl_50pct_speedup: 0.939\n    comp_30pct_ms: 129.94\n    comp_30pct_std: 0.75\n    comp_30pct_tokens_per_s: 15761.4\n    comp_30pct_speedup: 0.917\n    comp_50pct_ms: 129.71\n    comp_50pct_std: 0.53\n    comp_50pct_tokens_per_s: 15788.8\n    comp_50pct_speedup: 0.918\n    predictor_overhead_ms: 3.17\n    predictor_overhead_pct: 2.7\n    per_layer_predictor_ms: 0.099\n    dense_ffn_per_layer_ms: 2.427\n    sparse_ffn_pred_per_layer_ms: 2.686\n    compensation_overhead_ms: 3.3\n- exp_id: bench_kl50_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.83\n    arc_challenge_acc_norm: 0.3515\n    winogrande_acc: 0.6298\n    mmlu_acc: 0.2751\n    gsm8k_exact_match: 0.0235\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9604\n    arc_challenge_acc_norm: 0.3345\n    winogrande_acc: 0.6275\n    mmlu_acc: 0.2874\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: longbench_dense_v6\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    longbench_narrativeqa: 7.3\n    longbench_qasper: 13.4\n    longbench_gov_report: 30.5\n    longbench_multi_news: 2.5\n- exp_id: longbench_kl30_uniform_v6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    longbench_narrativeqa: 4.12\n    longbench_qasper: 6.23\n    longbench_gov_report: 16.97\n    longbench_multi_news: 18.01\n    runtime_seconds: 6156.6\n- exp_id: eval_c4_ood_kl50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 9.2075\n    kl_50_global_ppl: 18.401\n    teal_50_ppl: 38.7503\n    kl_vs_dense_ratio: 2\n    teal_vs_dense_ratio: 4.21\n- exp_id: db_sensitivity_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    db64_per_token_ppl: 10.158\n    db64_teal_global_ppl: 12.076\n    db64_sparsity: 0.5\n    db64_loss: 0.361\n    db128_teal_global_ppl: 11.963\n    db128_per_token_ppl: 9.218\n    db256_per_token_ppl: 8.586\n    db256_teal_global_ppl: 12.105\n    db256_sparsity: 0.5\n    db256_loss: 0.27\n    db512_per_token_ppl: 7.933\n    db512_teal_global_ppl: 12.315\n    db512_sparsity: 0.5\n    db512_loss: 0.224\n    best_teal_global_db: 128\n    best_teal_global_ppl: 11.963\n- exp_id: bce_gumbel_lagrangian_isolation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lr_1e4_ppl: 42.99\n    lr_1e3_ppl: 48.4\n    lr_3e3_ppl: 38.02\n    lr_1e4_bce_loss: 0.7158\n    lr_1e3_bce_loss: 0.6781\n    lr_3e3_bce_loss: 0.6632\n    lr_1e4_sparsity: 0.514\n    lr_1e3_sparsity: 0.506\n    lr_3e3_sparsity: 0.504\n    best_ppl: 38.02\n    best_lr: 3e-3\n    kl_baseline_ppl: 11.79\n    gap_vs_kl: 26.23\n- exp_id: steps_curve_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: tau_schedule_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tau_linear_baseline_ppl: 11.963\n    tau_fixed05_ppl: 11.861\n    tau_fixed01_ppl: 12.072\n    tau_fixed05_loss: 0.248\n    tau_fixed01_loss: 0.43\n    best_tau: fixed_0.5\n    ppl_range: 0.211\n- exp_id: steps_curve_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    step200_ppl: 15.158\n    step400_ppl: 12.538\n    step600_ppl: 12.046\n    step800_ppl: 11.907\n    step1000_ppl: 11.906\n    convergence_step: 800\n    ppl_800_vs_1000_delta: 0.001\n- exp_id: mistral_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 6.048\n    kl_teal_global_ppl: 6.7733\n    teal_baseline_ppl: 8.3807\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 1.386\n    ppl_vs_dense_pct: 9.5\n- exp_id: mistral_kl70_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 9.1086\n    kl_teal_global_ppl: 13.3254\n    teal_baseline_ppl: 61.716\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 6.77\n    final_loss: 0.3945\n    actual_sparsity: 0.682\n- exp_id: mistral_teal50_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_baseline_ppl: 18.3061\n    dense_ppl: 5.5238\n    teal_vs_dense_ratio: 3.31\n- exp_id: bench_kl70_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 17.91\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: kl_sparsity70_s42_v2 (teal_global_masks protocol)\n    vanilla_teal_ppl: 100.11\n- exp_id: bench_teal70\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 100.11\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: training_free_baselines experiment (vanilla teal global)\n- exp_id: gradient_snr_kl_vs_bce\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 5.77e-05\n    bce_avg_snr: 1.0e-05\n    snr_ratio: 5.76\n    early_layer_ratio_range: 34-156x\n    late_layer_ratio_range: 2-4x\n- exp_id: natural_sparsity_floor_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    always_pruned_ratio: 0.0006\n    always_pruned_count: 278\n    total_neurons: 458752\n    late_layer_max_ratio: 0.0051\n    threshold: 0.1\n- exp_id: teal_kl_overlap_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_jaccard: 0.396\n    divergence_ratio: 0.433\n    kl_only_pruned_magnitude_ratio: 1.48\n    teal_only_pruned_mean_gate_prob: 0.614\n    min_jaccard_layer: L17-L18 (0.19)\n    max_jaccard_layer: L26-L28 (0.55)\n- exp_id: gradient_snr_constrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 0.000545\n    bce_avg_snr: 5.28e-06\n    snr_ratio: 103.2\n    kl_final_sparsity: 0.508\n    bce_final_sparsity: 0.591\n    steps: 200\n- exp_id: sparsity_floor_extended\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    floor_30pct: 0.0499\n    floor_50pct: 0.0726\n    floor_70pct: 0.1936\n    late_layer_max_30: 0.4604\n    late_layer_max_50: 1.2347\n    late_layer_max_70: 4.3666\n    threshold: 0.1\n    seq_len: 2048\n    num_samples: 50\n- exp_id: teal_kl_overlap_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_score: 7260.3\n    p_value: 0\n    median_percentile_rank: 78.6\n    iqr_q1: 64.4\n    iqr_q3: 89.1\n    layers_significant: 31/32\n    exception_layer: 31\n- exp_id: mag_preservation_reg\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: reverse_kl_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.8\n    vs_forward_kl: +1.01 (+8.6%)\n    sparsity: 0.5\n- exp_id: jsd_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.54\n    vs_forward_kl: +0.75 (+6.4%)\n    sparsity: 0.5\n- exp_id: global_30pct_retention\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    early_retention: 0.771\n    middle_retention: 0.764\n    knowledge_L12_20_retention: 0.797\n    late_L24_31_retention: 0.501\n    L31_retention: 0.284\n    L30_retention: 0.366\n    starved_layers: L27-L31\n- exp_id: kl_bce_f1_oracle\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bce_f1: 0.6128\n    bce_precision: 0.6132\n    bce_recall: 0.6124\n    kl_f1: 0.5397\n    kl_precision: 0.5112\n    kl_recall: 0.5715\n    random_f1: 0.5\n    kl_ppl: 11.79\n    bce_ppl: 22.51\n- exp_id: kl50_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.745\n    arc_challenge: 0.3814\n    winogrande: 0.6125\n    mmlu: 0.2752\n    gsm8k: 0.0281\n- exp_id: kl30_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8308\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.6938\n    mmlu_acc: 0.3944\n    gsm8k_exact_match: 0.0751\n    actual_sparsity: 0.3\n    allocation: uniform\n- exp_id: kl50_s456_train_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl50_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.397\n    final_kl_normalized: 0.397\n    final_sparsity: 0.492\n    final_lambda: 5000\n    final_tau: 0.1\n    steps_completed: 1000\n- exp_id: kl_50pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.745\n    arc_challenge_acc_norm: 0.3814\n    winogrande_acc: 0.6125\n    mmlu_acc: 0.2752\n    gsm8k_exact_match: 0.0281\n    sparsity: 0.5\n    allocation: global\n- exp_id: mistral_dense_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 5.5238\n    model: Mistral-7B-v0.3\n    condition: dense\n    sparsity: 0\n- exp_id: mistral_kl30_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.048\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 0.5242\n- exp_id: mistral_kl50_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.2931\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 1.7693\n- exp_id: mistral_kl70_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 9.1086\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 3.5848\n- exp_id: mistral_kl30_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.7733\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 1.2495\n- exp_id: mistral_kl50_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.6489\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 3.1251\n- exp_id: mistral_kl70_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 13.3254\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 7.8016\n- exp_id: mistral_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3807\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 2.8569\n- exp_id: mistral_teal70_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 61.716\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 56.1922\n- exp_id: kl30_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.2021\n    actual_sparsity: 0.289\n    constraint_satisfied: true\n    training_steps: 1000\n- exp_id: kl_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9748\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.693\n    mmlu_acc: 0.3807\n    gsm8k_exact_match: 0.0758\n    sparsity: 0.3\n    allocation: global\n- exp_id: kl50_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.8057\n    arc_challenge: 0.3319\n    winogrande: 0.6488\n    mmlu: 0.2794\n    gsm8k: 0.0212\n- exp_id: kl30_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9332\n    arc_challenge: 0.4633\n    winogrande: 0.7111\n    mmlu: 0.4382\n    gsm8k: 0.0758\n- exp_id: kl30_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4198\n    ppl_uniform: 8.7947\n    arc_challenge: 0.4505\n    winogrande: 0.6875\n    gsm8k: 0.0758\n- exp_id: qwen14b_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 6.8\n    teal_global_ppl: 7.62\n    ppl_ratio_hard_mask: 1.31\n    ppl_ratio_teal: 1.47\n    final_loss: 0.3398\n    training_sparsity: 0.281\n    teal_sparsity: 0.3\n    lambda: 5000\n    steps: 1000\n- exp_id: qwen14b_kl30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.6232\n    arc_challenge_acc_norm: 0.5717\n    winogrande_acc: 0.7206\n    mmlu_acc: 0.6372\n    gsm8k_exact_match: 0.4882\n- exp_id: downstream_extended_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.727\n    hellaswag_acc: 0.527\n    piqa_acc_norm: 0.7595\n    piqa_acc: 0.747\n    boolq_acc: 0.7685\n- exp_id: wallclock_speedup_30_50\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    theoretical_flops_speedup_30pct: 1.36\n    theoretical_flops_speedup_50pct: 2.45\n    actual_wallclock_speedup_30pct: 0.91\n    actual_wallclock_speedup_50pct: 0.6\n    predictor_overhead_decode_ms: 1\n    predictor_overhead_prefill_ms: 2\n    actual_mean_sparsity_30pct: 0.28\n    actual_mean_sparsity_50pct: 0.605\n    note: No wall-clock speedup without sparse kernels. Mask-based=0.87-0.94x (predictor\n      overhead), structured-skip=0.45-0.74x (gather overhead). Report theoretical\n      FLOPs in paper.\n- exp_id: qwen14b_bce30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 5.57\n    teal_global_ppl: 8.76\n    ppl_ratio_hard_mask: 1.075\n    ppl_ratio_hard_mask_note: at predictor native 6.4% sparsity, not comparable to\n      KL's 28.1%\n    ppl_ratio_teal: 1.69\n    actual_sparsity_teal: 0.3\n    predictor_native_sparsity: 0.064\n    training_log_sparsity_note: Training Lagrangian failed (predictor sparsity=6.4%).\n      Inference via TEAL forces 30% externally. TEAL PPL 8.76 is valid for method\n      comparison.\n    final_loss: 0.5561\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n- exp_id: qwen14b_teal30_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.7332\n    arc_challenge_acc_norm: 0.5683\n    winogrande_acc: 0.7269\n    mmlu_acc: 0.7183\n    gsm8k_exact_match: 0.4951\n- exp_id: qwen14b_bce30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    predictor_native_sparsity: 0.064\n    lambda_max: 50000\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n    sparsity_trajectory: 49%→5% collapse in 50 steps, no recovery over 950 steps\n    note: 10x stronger Lagrangian produces identical sparsity as v1 (lambda=5000).\n      Confirms BCE gradient insufficiency is fundamental, not constraint strength.\n- exp_id: downstream_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.8233\n    hellaswag_acc_norm_stderr: 0.0038\n    piqa_acc_norm: 0.8074\n    piqa_acc_norm_stderr: 0.0092\n    boolq_acc: 0.8294\n    boolq_acc_stderr: 0.0066\n- exp_id: qwen14b_bce30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 8.7634\n    arc_challenge_acc_norm: 0.5759\n    winogrande_acc: 0.7261\n    mmlu_acc: 0.7167\n    gsm8k_exact_match: 0.5307\n- exp_id: downstream_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc: 0.4878\n    hellaswag_acc_norm: 0.667\n    piqa_acc: 0.7258\n    piqa_acc_norm: 0.7361\n    boolq_acc: 0.685\n- exp_id: kl50_global_s123_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7184\n    arc_challenge_acc_norm: 0.3635\n    winogrande_acc: 0.6109\n    mmlu_acc: 0.2834\n    gsm8k_exact_match: 0.0258\n- exp_id: bce_isocompute_v3_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: bce_isocompute_v3_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6368\n    final_sparsity: 0.51\n    training_steps: 2700\n- exp_id: c4_ood_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0458\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_download\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen14b_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl: 5.1854\n    arc_challenge: 0.6758\n    winogrande: 0.8106\n    mmlu: 0.7977\n    gsm8k: 0.8757\n- exp_id: bce_isocompute_v3_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_sparse_ppl: 28.3503\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2312\n    arc_challenge_acc_stderr: 0.01232\n    arc_challenge_acc_norm: 0.2807\n    arc_challenge_acc_norm_stderr: 0.01313\n    winogrande_acc: 0.5241\n    winogrande_acc_stderr: 0.01404\n    mmlu_acc: 0.2567\n    mmlu_acc_stderr: 0.00367\n    gsm8k_exact_match: 0.022\n    gsm8k_exact_match_stderr: 0.00404\n    gsm8k_exact_match_strict: 0.00834\n    gsm8k_exact_match_strict_stderr: 0.0025\n- exp_id: bce_isocompute_v3_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 28.0627\n    arc_challenge_acc_norm: 0.2696\n    winogrande_acc: 0.513\n    mmlu_acc: 0.2655\n    gsm8k_exact_match: 0.022\n- exp_id: qwen14b_kl30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: qwen14b_teal30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl30_8b_s123_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    sparsity: 0.3\n    training_loss: 0.147\n- exp_id: kl30_8b_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    sparsity: 0.3\n    training_loss: 0.148\n- exp_id: qwen14b_kl30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 7.63\n    mmlu_acc: 0.6449\n    arc_challenge_acc_norm: 0.5444\n    winogrande_acc: 0.7245\n- exp_id: qwen14b_teal30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.01\n    mmlu_acc: 0.6634\n    arc_challenge_acc_norm: 0.5529\n    winogrande_acc: 0.6985\n- exp_id: bce_isocompute_v3_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 27.9696\n    arc_challenge_acc: 0.2346\n    arc_challenge_acc_norm: 0.2765\n    winogrande_acc: 0.5162\n    mmlu_acc: 0.2614\n    gsm8k_exact_match: 0.019\n- exp_id: kl30_8b_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    arc_challenge_acc: 0.4462\n    arc_challenge_acc_norm: 0.4744\n    winogrande_acc: 0.7024\n    mmlu_acc: 0.3836\n    gsm8k_exact_match: 0.0917\n- exp_id: kl30_8b_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc: 0.436\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: snr_extended_r6w3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_snr_step300: 0.0058773\n    bce_snr_step300: 0.00114449\n    snr_ratio_step300: 5.14\n    kl_train_time_s: 641\n    bce_train_time_s: 320\n    num_checkpoints: 7\n    steps_range: 0-300\n- exp_id: c4_ood_kl30_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl50_s123_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.89\n    arc_challenge_acc_norm: 37.88\n    winogrande_acc: 62.19\n    mmlu_acc: 27.75\n    gsm8k_exact_match: 2.35\n    comparison_vs_global_topk:\n      ppl_delta: -0.94\n      arc_c_delta: -5.55\n      wg_delta: -6.71\n      mmlu_delta: -8.2\n      gsm8k_delta: -5\n    note: 'Uniform allocation: better PPL but catastrophic downstream degradation\n      vs global_topk. Confirms global_topk allocation is critical for downstream quality.'\n- exp_id: c4_ood_kl30_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0259\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_ood_dense_baseline_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 9.2075\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: kl50_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8614\n    arc_challenge_acc_norm: 0.3754\n    winogrande_acc: 0.6417\n    mmlu_acc: 0.2784\n    gsm8k_exact_match: 0.0212\n- exp_id: c4_ood_kl50_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.6064\n    allocation: global_topk\n    sparsity: 0.5\n    model: llama-3.1-8b\n- exp_id: downstream_ext_kl50_uniform_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: downstream_ext_kl30_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_kl50_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.9867\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 456\n- exp_id: c4_ood_kl30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0401\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl50_s42_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9638\n    arc_challenge_acc_norm: 0.3259\n    winogrande_acc: 0.6235\n    mmlu_acc: 0.2792\n    gsm8k_exact_match: 0.0197\n- exp_id: c4_ood_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.5297\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 42\n- exp_id: kl_comp_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6992\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.3594\n    - 1.3516\n    - 1.0859\n    - 0.9219\n    - 0.8789\n    - 0.8281\n    - 0.7461\n    - 0.7344\n    - 0.6953\n    - 0.6992\n- exp_id: c4_ood_kl30_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.7617\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.0469\n    - 1.3828\n    - 1.0703\n    - 0.9609\n    - 0.8711\n    - 0.7305\n    - 0.6875\n    - 0.7773\n    - 0.7969\n    - 0.7617\n- exp_id: kl_comp_30pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl_comp_30pct_s42_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl_comp_30pct_s123_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 123\n- exp_id: kl_comp_30pct_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl50_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9538\n    arc_challenge_acc_norm: 0.3831\n    winogrande_acc: 0.6196\n    mmlu_acc: 0.275\n    gsm8k_exact_match: 0.0288\n- exp_id: kl_comp_30pct_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: kl_comp_50pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n- exp_id: kl50_s42_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8038\n    arc_challenge_acc_norm: 0.3336\n    winogrande_acc: 0.6338\n    mmlu_acc: 0.2819\n    gsm8k_exact_match: 0.0167\n- exp_id: kl30_s123_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8186\n    arc_challenge_acc_norm: 0.471\n    winogrande_acc: 0.6961\n    mmlu_acc: 0.3763\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s456_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8284\n    arc_challenge_acc_norm: 0.4505\n    winogrande_acc: 0.6953\n    mmlu_acc: 0.3727\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s123_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl30_s456_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: c1_ablation_bce_kl_targets_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wt2_ppl: 9.29\n    eval_sparsity: 0.609\n    oracle_agreement: 0.978\n    final_bce_loss: 0.0545\n    train_steps: 1000\n    train_time_sec: 877.1\n    reference_kl_ppl: 11.79\n    reference_bce_ppl: 22.51\n- exp_id: bce_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_sparsity25_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity35_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: c1_ablation_eval_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity45_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: bce_30pct_s42_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: c1_ablation_bce_kl_targets\n  claim: 'Claim 1 reframe: optimization target quality > gradient coupling'\n  description: BCE trained on KL-derived oracle masks achieves comparable-or-better\n    PPL than KL distillation at matched sparsity. 53% mask divergence from magnitude\n    oracles. Core narrative shifts from 'gradient coupling explains KL advantage'\n    to 'KL discovers fundamentally different and superior mask patterns that magnitude-based\n    oracles miss'.\n  estimated_gpu_hours: 0.0\n- name: dense_sparsity_sweep_6pt\n  claim: 'Claim 3: regime analysis with 6 data points'\n  description: KL predictors trained at 25%/30%/35%/40%/45%/50% sparsity with 2 seeds\n    each. Regime boundaries precisely mapped. Non-monotonic allocation preference\n    confirmed with denser sampling.\n  estimated_gpu_hours: 0.0\n- name: bce_30pct_forced_topk\n  claim: 'Claim 1: BCE baseline at recommended operating point'\n  description: BCE predictor evaluated at 30% via forced TEAL top-k. Fills Table 2\n    gap at recommended operating point. BCE PPL expected significantly worse than\n    KL, strengthening KL advantage at practical deployment sparsity.\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T16:40:26.131Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T16:40:26.131Z",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-18T16:40:26.158Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：C1 ablation 显示 mask quality 解释大部分但非全部 KL 优势（存在 2-3 PPL residual gap）；部分实验噪声偏大；需调整 claim 强度和补充讨论
核心假设：['BCE-on-KL-targets at 50% uniform PPL 在 12.5-15.0——优于 vanilla BCE（28.0）但劣于 KL（11.8），residual gap 表明 optimization dynamics 也独立贡献', 'BCE 30% forced top-k PPL 在 10.0-13.0——低 sparsity 下 gap 缩小，KL 优势非均匀', '6-point sweep 趋势可辨但个别点偏离，regime 边界模糊 ±5pp', 'KL 30% uniform 3-seed MMLU σ 2-4pp，需要 carefully present mean±CI 而非 cherry-pick', "至少 1 位 reviewer 质疑 novelty（'KL distillation is well-known'），至少 1 位指出 14B gap", '部分 sweep 实验（25%/45%）在 deadline 前未完成，用 4-point 数据替代']
关键指标范围：{'c1_ablation_uniform_50pct_ppl': [12.5, 15.0], 'bce_30pct_forced_topk_ppl': [10.0, 13.0], 'kl_30pct_uniform_3seed_mmlu_std_pp': [2.0, 4.0], 'regime_piecewise_fit_r2': [0.8, 0.93], 'expected_ARR_overall': [3.0, 3.5]}
叙事方向：'Mask pattern discovery' 降级为 'mask pattern divergence is a major contributing factor'。 C1 ablation residual gap（2-3 PPL）需要诚实报告并归因：mask quality 解释 ~60-75% 的 KL 优势，continuous optimization（Gumbel relaxation + end-to-end gradient flow）贡献余下部分。 Contribution 1 改写为 'KL improves BOTH mask quality AND optimization fidelity, with mask quality as the dominant factor'——需要增加一段 discussion 解耦两者。Phase transition（Claim 3） 从 bonus 提升为 co-equal contribution 以补偿 C1 削弱的 novelty。如果 BCE 30% gap 不够大， 强调 sparsity-dependent advantage（50% 差距 2.3×，30% 差距逐渐缩小——这本身是 regime analysis 的一部分）。Paper 可能首轮进 Findings；通过 revision 补充缺失 sweep 数据争取 Main。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: distill_sparse_swiglu
focus: 测试论文 reframe 为 'mask pattern discovery' 叙事的接收度。核心变化：Contribution 1 从 gradient coupling 转为 optimization target quality / mask pattern divergence。§3.6 gradient analysis 降为 suggestive motivation。C1 ablation 变成 paper 核心实验。53% mask divergence 作为新发现。目标 4.0 Main Conference accept。

## paper_framing.md

# Paper Framing — distill_sparse_swiglu

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 2026 cycle)
- Deadline: 2026-05-25 (ARR submission)
- Track: Efficient Methods for NLP

## Core Claims

1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent "unfair comparison" attacks. **Iso-compute evidence (eval_bce_v3_s42)**: with 2.71× more gradient updates, BCE TEAL PPL=27.97 vs KL=12.00 (2.33× gap persists), and BCE loss saturates (step 500→2700: Δ=-0.006). The advantage is structural: BCE optimizes per-neuron binary classification, but inference uses global top-k budget allocation — per-neuron scoring is suboptimal under global reallocation. KL directly optimizes output distribution, naturally compatible with any allocation strategy. (Headline claim)

2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL "subsuming" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)

3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports "PPL is a poor proxy for downstream quality" narrative. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)

## Story Spine

- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).

- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.

- **Our framing / headline question**: "Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.

- **Headline result template**: "On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] quality but adds 67.2M parameters ([W] ms/token overhead) — demonstrating that output-distribution distillation renders error compensation unnecessary—SPON's residual correction is orthogonal to KL's dominant effect and too weak to complement it—enabling a simpler, lighter inference pipeline with strictly better efficiency-quality tradeoff."

## Two-Dimensional Taxonomy (Conceptual Contribution)

|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
|--------------------------|:-----------------:|:-------------------:|:-------------:|
| Static                   | —                 | —                   | SPON          |
| Per-layer                | —                 | ShadowLLM           | —             |
| Per-token contextual     | FastForward       | —                   | **Ours**      |

Positions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.

## Anticipated Reviewer Concerns

1. **"Incremental / no new algorithm"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.

2. **"KL wins only because more compute"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.

3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.

4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 (plan_009, GQA + sliding window) and Qwen-2.5-14B cross-scale validation (D048/D054). **14B mixed result**: KL PPL advantage preserved (7.62 vs TEAL 8.73, 1.47× dense ratio identical to 8B), but KL MMLU=63.72% (global) / 64.49% (uniform) significantly trails TEAL 71.83% (global). Uniform allocation does not fix this gap (D054). PPL-downstream disconnect at 14B scale is an honest limitation, not hidden. Framing: KL's coupled gradient captures output-distribution fidelity (PPL) across scales, but 14B knowledge-intensive tasks (MMLU) show scale-dependent sensitivity that warrants further investigation.

5. **"Effect size may not hold on downstream tasks"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.

6. **"Unfair comparison: BCE+comp close to KL but at higher inference cost"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.

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
  registry_id: kl_only_s1
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 9.15
    teal_sparse_ppl: 11.99
    model_level_sparsity: 0.498
    ppl_increase_vs_true_dense_pct: 96
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
  registry_id: ste_baseline_s42
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 8.18
    teal_sparse_ppl: 15.77
    model_level_sparsity: 0.47
    ppl_increase_vs_true_dense_pct: 157.7
    eval_seq_len: 2048
    calibration_samples: 32
    eval_dataset: wikitext-2
    per_token_sparsity: 0.47
    lambda_stats:
      steps_70_130_mean: 66.4
      steps_70_130_std: 94.87
      first_500_mean: 688.07
      first_500_std: 440.57
      last_500_mean: 965.69
      last_500_std: 141.59
      overall_mean: 826.88
      overall_std: 354.23
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
  registry_id: bce_isocompute_v2_s42
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.6637
    final_bce_loss: 0.6586
    final_reg_loss: 0.0051
    final_sparsity: 0.502
    training_steps: 1000
    training_time_sec: 1047.8
    reg_weight: 2
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 26.76
    teal_sparse_ppl: 54.84
    eval_seq_len: 2048
    eval_dataset: wikitext-2
- id: plan_004
  claim: 2
  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL
    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,
    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.

    '
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: spon_2048_s42
  status: DONE
  conclusion: negative
  metrics:
    true_dense_ppl: 6.1173
    predictor_hard_mask_ppl: 9.2165
    spon_sparse_ppl: 8.991
    spon_recovery_pct: 7.3
    ppl_improvement_from_spon: 0.2255
    mean_bias_norm: 0.05312
    max_bias_norm: 0.065918
    model_level_sparsity: 0.498
    eval_seq_len: 2048
    training_seq_len: 2048
    eval_samples: 141
    trainable_params: 458752
    trainable_pct: 0.0057
    training_steps: 1000
    final_loss: 0.377
    dense_with_spon_ppl: 6.1823
    dense_ppl_degradation: 0.0651
    teal_sparse_no_spon_ppl: 12.0776
    teal_sparse_with_spon_ppl: 11.7907
    spon_recovery_teal_pct: 4.8
    teal_sparsity: 0.4979
- id: plan_005
  claim: 2
  description: 'SPON subsumption verification: output-space linearity test showing
    KL predictor already captures SPON correction signal. ||Delta_logits(s+c) - Delta_logits(s)
    - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality analysis.
    Proves SPON+KL ≈ KL (no additive gain). 3 seeds.

    '
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan_001
  - plan_004
  registry_id: plan_005_subsumption_s42
  status: DONE
  conclusion: success
  metrics:
    linearity_ratio: 0.2644
    linearity_ratio_std: 0.0073
    magnitude_ratio: 0.1578
    magnitude_ratio_std: 0.0088
    cosine_similarity: 0.1962
    cosine_similarity_std: 0.0268
    predictor_effect_norm: 482.65
    spon_correction_norm: 76.2
    interaction_norm: 147.74
    num_samples: 50
    seq_len: 2048
    conclusion_type: weak_subsumption
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
  registry_ids:
  - training_free_baselines
  - training_free_wina_greedy
  registry_id: training_free_baselines
  status: DONE
  conclusion: success
  metrics:
    dense_ppl: 6.12
    vanilla_teal_global_ppl_30pct: 10.97
    vanilla_teal_global_ppl_50pct: 23.31
    vanilla_teal_global_ppl_70pct: 100.11
    wina_global_ppl_30pct: 11.45
    wina_global_ppl_50pct: 27.93
    wina_global_ppl_70pct: 137.24
    uniform_50pct_ppl: 23.9
    teal_greedy_ppl: 33.47
    vanilla_teal_global_ppl: 23.31
    wina_global_ppl: 27.93
    rsparse_global_ppl: 151.2
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
  registry_id: bench_dense
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 6.1173
    arc_challenge_acc: 0.5478
    arc_challenge_acc_norm: 0.5828
    winogrande_acc: 0.7806
    mmlu_acc: 0.6527
    gsm8k_exact_match: 0.4875
- id: plan_008
  claim: 3
  description: '3-level sparsity sweep (30%/50%/70%): KL-only vs BCE-only. Test scaling
    trend and KL-BCE delta growth. 1 seed per level (sweep analysis, not headline).
    50% data point reused from plan_001. If 3 levels show non-linear inflection, add
    intermediate points.

    '
  priority: P1
  gpu_budget_hours: 12
  deps:
  - plan_001
  registry_id: d030_kl50_uniform
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.96
    arc_challenge_acc_norm: 0.3276
    winogrande_acc: 0.629
    mmlu_acc: 0.2777
    gsm8k_exact_match: 0.0212
    actual_sparsity: 0.5
    allocation: uniform
    per_layer_sparsity: uniform 0.500 across all 32 layers
    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)
    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)
    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在
      50% sparsity 下消失。
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
  registry_id: lm_eval_mistral_dense
  status: DONE
  conclusion: success
  metrics:
    arc_challenge_acc_norm: 0.6024
    winogrande_acc: 0.7869
    mmlu_acc: 0.6244
    gsm8k_exact_match: 0.3654
    model: Mistral-7B-v0.3
    condition: dense
    server: westd-34887
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
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_kl_s456
  name: ''
  status: DONE
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
    vanilla_teal_sparse_ppl_INVALID: 66036.4062
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
    vanilla_teal_sparse_ppl_INVALID: 66036.4062
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
    vanilla_teal_sparse_ppl_INVALID: 66036.4062
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
  conclusion: killed
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
    vanilla_teal_sparse_ppl_INVALID: 66036.4062
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
    vanilla_teal_sparse_ppl_INVALID: 66036.4062
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
    vanilla_teal_sparse_ppl_INVALID: 66036.4062
- exp_id: kl_only_s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 9.19
    teal_sparse_ppl: 12.03
    model_level_sparsity: 0.499
    ppl_increase_vs_true_dense_pct: 96.57
    eval_seq_len: 2048
    calibration_samples: 32
- exp_id: kl_only_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 9.15
    teal_sparse_ppl: 11.99
    model_level_sparsity: 0.498
    ppl_increase_vs_true_dense_pct: 96
- exp_id: spon_training
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    true_dense_ppl: 6.1193
    predictor_hard_mask_ppl: 9.2165
    spon_sparse_ppl: 9.0977
    spon_recovery_pct: 3.8
    ppl_improvement_from_spon: 0.1188
    ppl_increase_vs_true_dense_pct: 48.7
    ppl_increase_no_spon_vs_true_dense_pct: 50.6
    mean_bias_norm: 0.040596
    max_bias_norm: 0.054199
    teal_sparse_ppl: 12.08
    teal_with_spon_ppl: 11.93
    spon_dense_ppl_degradation: 6.19
    model_level_sparsity: 0.5
    eval_seq_len: 2048
    eval_samples: 141
    trainable_params: 458752
    trainable_pct: 0.0057
- exp_id: spon_kl_s42
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: bce_comp_staged_s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 25.44
    predictor_hard_mask_ppl_no_comp: 27.96
    teal_sparse_ppl: 44.54
    model_level_sparsity: 0.558
    ppl_increase_vs_true_dense_pct: 315.7
    comp_loss_final: 0.0033
    bce_loss_final: 0.6379
    eval_seq_len: 2048
    calibration_samples: 32
- exp_id: training_free_baselines
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dense_ppl: 6.12
    vanilla_teal_global_ppl_30pct: 10.97
    vanilla_teal_global_ppl_50pct: 23.31
    vanilla_teal_global_ppl_70pct: 100.11
    wina_global_ppl_30pct: 11.45
    wina_global_ppl_50pct: 27.93
    wina_global_ppl_70pct: 137.24
    uniform_50pct_ppl: 23.9
    teal_greedy_ppl: 33.47
    vanilla_teal_global_ppl: 23.31
    wina_global_ppl: 27.93
    rsparse_global_ppl: 151.2
- exp_id: spon_training_seq2048
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: ste_baseline_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 8.18
    teal_sparse_ppl: 15.77
    model_level_sparsity: 0.47
    ppl_increase_vs_true_dense_pct: 157.7
    eval_seq_len: 2048
    calibration_samples: 32
    eval_dataset: wikitext-2
    per_token_sparsity: 0.47
    lambda_stats:
      steps_70_130_mean: 66.4
      steps_70_130_std: 94.87
      first_500_mean: 688.07
      first_500_std: 440.57
      last_500_mean: 965.69
      last_500_std: 141.59
      overall_mean: 826.88
      overall_std: 354.23
- exp_id: spon_2048_s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    true_dense_ppl: 6.1173
    predictor_hard_mask_ppl: 9.2165
    spon_sparse_ppl: 8.991
    spon_recovery_pct: 7.3
    ppl_improvement_from_spon: 0.2255
    mean_bias_norm: 0.05312
    max_bias_norm: 0.065918
    model_level_sparsity: 0.498
    eval_seq_len: 2048
    training_seq_len: 2048
    eval_samples: 141
    trainable_params: 458752
    trainable_pct: 0.0057
    training_steps: 1000
    final_loss: 0.377
    dense_with_spon_ppl: 6.1823
    dense_ppl_degradation: 0.0651
    teal_sparse_no_spon_ppl: 12.0776
    teal_sparse_with_spon_ppl: 11.7907
    spon_recovery_teal_pct: 4.8
    teal_sparsity: 0.4979
- exp_id: ste_kl_s42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: training_free_wina_greedy
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    wina_greedy_ppl: 2126.03
    dense_ppl: 6.12
    model_level_sparsity: 0.5
    eval_dataset: WikiText-2
    eval_seq_len: 2048
    greedy_allocation_summary: 'layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80,
      layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24:
      0.05-0.15, layers 25-31: 0.00'
- exp_id: bce_isocompute_s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: eval_spon_supp_retry
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: bce_isocompute_s42_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: spon_supp_eval_retry
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: bce_isocompute_v2_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.6637
    final_bce_loss: 0.6586
    final_reg_loss: 0.0051
    final_sparsity: 0.502
    training_steps: 1000
    training_time_sec: 1047.8
    reg_weight: 2
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 26.76
    teal_sparse_ppl: 54.84
    eval_seq_len: 2048
    eval_dataset: wikitext-2
- exp_id: plan_005_subsumption_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    linearity_ratio: 0.2644
    linearity_ratio_std: 0.0073
    magnitude_ratio: 0.1578
    magnitude_ratio_std: 0.0088
    cosine_similarity: 0.1962
    cosine_similarity_std: 0.0268
    predictor_effect_norm: 482.65
    spon_correction_norm: 76.2
    interaction_norm: 147.74
    num_samples: 50
    seq_len: 2048
    conclusion_type: weak_subsumption
- exp_id: kl_sparsity30_s42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: kl_sparsity70_s42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: kl_sparsity30_s42_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    final_loss: 0.1465
    kl_normalized: 0.1465
    kl_raw: 0.1465
    model_level_sparsity: 0.281
    sparsity_target: 0.3
    lambda_sparse_final: 1000
    lambda_max_cap: 1000
    tau_final: 0.1
    constraint_loss_final: 0
    training_steps: 1000
    wall_clock_seconds: 2662.6
    gpu_hours: 0.74
    note: No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1).
      Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run
      was offline (not synced).
- exp_id: kl_sparsity70_s42_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 13.84
    predictor_teal_sparse_ppl: 17.91
    vanilla_teal_sparse_ppl: 100.11
    teal_sparse_ppl: 17.91
    teal_sparse_ppl_static_baseline: 17.91
    model_level_sparsity: 0.7
    teal_sparse_note: '17.91 = predictor-based TEAL (teal_global_masks: predictor-gated
      magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py
      L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct
      metadata 有误导性.'
    eval_dataset: wikitext-2
    eval_seq_len: 2048
    calibration_samples: 32
    per_layer_sparsity_range:
    - 0.508
    - 0.876
- exp_id: kl_sparsity30_s42_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    loss: 0.165
    kl_normalized: 0.165
    kl_raw: 0.165
    sparsity: 0.285
    lambda_sparse: 5000
    tau: 0.1
    constraint_loss: 0
    steps: 1000
    true_dense_ppl: 6.12
    predictor_hard_mask_ppl: 7.3
    teal_sparse_ppl: 8.98
    teal_sparse_ppl_note: 已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)
    model_level_sparsity: 0.3
    eval_dataset: wikitext-2
    eval_seq_len: 2048
- exp_id: mistral_kl_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_final_loss: 0.2188
    train_final_kl_raw: 0.2188
    train_final_kl_norm: 0.2188
    train_final_constraint: 0
    train_final_sparsity: 0.48
    train_final_lambda: 1000
    train_final_tau: 0.1
    train_steps_completed: 1000
    true_dense_ppl: 5.52
    predictor_hard_mask_ppl: 7.3
    teal_sparse_ppl: 8.98
    model_level_sparsity: 0.5
    eval_dataset: wikitext-2
    eval_seq_len: 2048
    calibration_samples: 32
    eval_samples: 159
- exp_id: lm_eval_dense_test
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: lm_eval_kl_s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    arc_challenge_acc_norm: 0.3771
    winogrande_acc: 0.6156
    mmlu_acc: 0.2591
    gsm8k_exact_match: 0.0121
    eval_tasks:
    - arc_challenge
    - winogrande
    - mmlu
    - gsm8k
    model: llama-3.1-8b
    condition: kl_sparse_50pct
    server: westd-34887
    exit_code: 129
    wall_time_sec: 3010
    flag: SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py
- exp_id: lm_eval_dense
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_challenge_acc_norm: 0.5819
    winogrande_acc: 0.7814
    mmlu_acc: 0.6532
    gsm8k_exact_match: 0.5004
    eval_tasks:
    - arc_challenge
    - winogrande
    - mmlu
    - gsm8k
    model: llama-3.1-8b
    condition: dense
    server: westd-34887
- exp_id: lm_eval_mistral_downstream
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: lm_eval_mistral_dense
  name: ''
  status: DONE
  conclusion: success
  metrics:
    arc_challenge_acc_norm: 0.6024
    winogrande_acc: 0.7869
    mmlu_acc: 0.6244
    gsm8k_exact_match: 0.3654
    model: Mistral-7B-v0.3
    condition: dense
    server: westd-34887
- exp_id: diag_30pct_downstream
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: diag_gsm8k_gencomp
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: diag_teal_downstream
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: lm_eval_kl_30pct_s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    arc_challenge_acc: 0.3575
    arc_challenge_acc_norm: 0.3737
    winogrande_acc: 0.6756
    mmlu_acc: 0.2874
    gsm8k_exact_match_strict: 0.0743
    gsm8k_exact_match_flexible: 0.0781
    actual_sparsity: 0.3
    model: llama-3.1-8b
    condition: kl_distill_30pct_sparsity_s42
    mmlu_stem_acc: 0.2499
    mmlu_social_sciences_acc: 0.2896
    mmlu_humanities_acc: 0.2786
    mmlu_other_acc: 0.3363
- exp_id: gsm8k_gen_compare
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: lm_eval_teal_50pct
  name: ''
  status: DONE
  conclusion: success
  metrics:
    method: vanilla_teal
    sparsity: 0.5
    actual_sparsity: 0.5
    arc_challenge_acc_norm: 0.291
    winogrande_acc: 0.5556
    mmlu_acc: 0.2856
    gsm8k_exact_match_flexible: 0.019
    gsm8k_exact_match_strict: 0.0114
    arc_challenge_drop_vs_dense: -0.5
    winogrande_drop_vs_dense: -0.289
    mmlu_drop_vs_dense: -0.563
    gsm8k_drop_vs_dense: -0.962
    model: Llama-3.1-8B
    condition: TEAL 50% training-free sparsity
- exp_id: lm_eval_teal_30pct
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    arc_challenge:
      acc: 0.3933
      acc_norm: 0.4155
      acc_stderr: 0.0143
      acc_norm_stderr: 0.0144
    winogrande:
      acc: 0.6559
      acc_stderr: 0.0134
    mmlu:
      acc: 0.3598
      acc_stderr: 0.004
    mmlu_stem:
      acc: 0.313
    mmlu_humanities:
      acc: 0.3305
    mmlu_social_sciences:
      acc: 0.4108
    mmlu_other:
      acc: 0.401
    gsm8k:
      exact_match_strict: 0.0849
      exact_match_flexible: 0.0925
      strict_stderr: 0.0077
      flexible_stderr: 0.008
    actual_sparsity: 0.3
- exp_id: lm_eval_mistral_kl_50pct
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    arc_challenge_acc: 0.2927
    arc_challenge_acc_norm: 0.3183
    arc_challenge_acc_norm_stderr: 0.0136
    winogrande_acc: 0.629
    winogrande_acc_stderr: 0.0136
    mmlu_acc: 0.2295
    mmlu_acc_stderr: 0.0035
    mmlu_stem_acc: 0.2125
    mmlu_humanities_acc: 0.2421
    mmlu_social_sciences_acc: 0.2171
    mmlu_other_acc: 0.2398
    gsm8k_exact_match_strict: 0.0045
    gsm8k_exact_match_flexible: 0.0212
    model: Mistral-7B-v0.3
    condition: kl_distill_50pct_sparsity_s42
    arc_challenge_retention_vs_dense: 0.528
    winogrande_retention_vs_dense: 0.799
    mmlu_retention_vs_dense: 0.368
    gsm8k_retention_vs_dense: 0.012
- exp_id: d030_kl30_uniform
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.8157
    arc_challenge_acc_norm: 0.4078
    winogrande_acc: 0.6859
    mmlu_acc: 0.4061
    gsm8k_exact_match: 0.0735
    actual_sparsity: 0.3
    allocation: uniform
    per_layer_sparsity: uniform 0.301 across all 32 layers
    mmlu_improvement_vs_global: +11.87pp (0.2874 → 0.4061)
    gsm8k_change_vs_global: no change (0.0743 → 0.0735, within noise)
- exp_id: bce_isocompute_v3_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    steps: 2700
    loss: 0.6382
    bce_loss: 0.6371
    reg_loss: 0.001
    sparsity: 0.51
    training_time_seconds: 2828
    note: 'BCE saturation confirmed: step 500→2700 only 0.006 improvement'
- exp_id: bench_mistral_kl50_s42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: d030_kl50_uniform
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.96
    arc_challenge_acc_norm: 0.3276
    winogrande_acc: 0.629
    mmlu_acc: 0.2777
    gsm8k_exact_match: 0.0212
    actual_sparsity: 0.5
    allocation: uniform
    per_layer_sparsity: uniform 0.500 across all 32 layers
    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)
    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)
    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在
      50% sparsity 下消失。
- exp_id: bench_dense
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 6.1173
    arc_challenge_acc: 0.5478
    arc_challenge_acc_norm: 0.5828
    winogrande_acc: 0.7806
    mmlu_acc: 0.6527
    gsm8k_exact_match: 0.4875
- exp_id: eval_kl30_teal_30pct
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dense_ppl: 6.12
    predictor_hard_mask_ppl: 7.3
    teal_sparse_ppl: 8.98
    sparsity_target: 0.3
    actual_sparsity: 0.3
- exp_id: d030_kl40_uniform
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.3627
    arc_challenge_acc_norm: 0.4181
    winogrande_acc: 0.6717
    mmlu_acc: 0.3068
    gsm8k_exact_match: 0.0394
    actual_sparsity: 0.398
- exp_id: eval_bce_v3_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dense_ppl: 6.12
    predictor_hard_mask_ppl: 22.51
    teal_sparse_ppl: 27.97
    model_level_sparsity: 0.5
    arc_challenge_acc: 0.2048
    arc_challenge_acc_norm: 0.2398
    arc_challenge_acc_norm_stderr: 0.0125
    winogrande_acc: 0.5059
    winogrande_acc_stderr: 0.0141
    mmlu_acc: 0.3002
    mmlu_acc_stderr: 0.0038
    gsm8k_exact_match: 0.0485
    gsm8k_exact_match_strict: 0.0425
    gsm8k_exact_match_stderr: 0.0059
- exp_id: bench_kl30_uniform
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.8157
    arc_challenge_acc_norm: 0.4078
    winogrande_acc: 0.6859
    mmlu_acc: 0.4061
    gsm8k_exact_match: 0.0735
    actual_sparsity: 0.3
- exp_id: bench_kl50_global
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.7933
    arc_challenge_acc_norm: 0.3285
    winogrande_acc: 0.6346
    mmlu_acc: 0.2789
    gsm8k_exact_match: 0.0129
    actual_sparsity: 0.5
- exp_id: bench_kl30_global
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9768
    arc_challenge_acc_norm: 0.3968
    winogrande_acc: 0.7017
    mmlu_acc: 0.2527
    gsm8k_exact_match: 0.0879
    actual_sparsity: 0.3
- exp_id: bench_teal30
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 10.97
    arc_challenge_acc_norm: 0.4232
    winogrande_acc: 0.6606
    mmlu_acc: 0.3861
    gsm8k_exact_match: 0.0788
    actual_sparsity: 0.3
- exp_id: bench_teal50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 23.31
    arc_challenge_acc_norm: 0.2841
    winogrande_acc: 0.5304
    mmlu_acc: 0.2832
    gsm8k_exact_match: 0.0197
    actual_sparsity: 0.5
- exp_id: bench_kl50_uniform
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.963
    arc_challenge_acc_norm: 0.3276
    winogrande_acc: 0.629
    mmlu_acc: 0.2777
    gsm8k_exact_match: 0.0212
    actual_sparsity: 0.5
- exp_id: bench_kl40_global
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 10.117
    arc_challenge_acc_norm: 0.4096
    winogrande_acc: 0.6535
    mmlu_acc: 0.3806
    gsm8k_exact_match: 0.05
    actual_sparsity: 0.4
- exp_id: longbench_kl30_uniform
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: longbench_dense
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: longbench_kl30_uniform_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: longbench_dense_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: longbench_kl30_uniform_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: longbench_dense_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: longbench_dense_v4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: longbench_dense_v5
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: latency_benchmark
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gpu_model: NVIDIA RTX PRO 6000 Blackwell Server Edition
    dtype: float16
    attn: flash_attention_2
    batch: 1
    seq_len: 2048
    warmup: 10
    iters: 100
    dense_ms: 119.11
    dense_std: 0.57
    dense_tokens_per_s: 17194.5
    kl_30pct_ms: 126.64
    kl_30pct_std: 0.7
    kl_30pct_tokens_per_s: 16171.8
    kl_30pct_speedup: 0.941
    kl_50pct_ms: 126.78
    kl_50pct_std: 0.31
    kl_50pct_tokens_per_s: 16154.2
    kl_50pct_speedup: 0.939
    comp_30pct_ms: 129.94
    comp_30pct_std: 0.75
    comp_30pct_tokens_per_s: 15761.4
    comp_30pct_speedup: 0.917
    comp_50pct_ms: 129.71
    comp_50pct_std: 0.53
    comp_50pct_tokens_per_s: 15788.8
    comp_50pct_speedup: 0.918
    predictor_overhead_ms: 3.17
    predictor_overhead_pct: 2.7
    per_layer_predictor_ms: 0.099
    dense_ffn_per_layer_ms: 2.427
    sparse_ffn_pred_per_layer_ms: 2.686
    compensation_overhead_ms: 3.3
- exp_id: bench_kl50_uniform_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.83
    arc_challenge_acc_norm: 0.3515
    winogrande_acc: 0.6298
    mmlu_acc: 0.2751
    gsm8k_exact_match: 0.0235
    actual_sparsity: 0.5
- exp_id: bench_kl50_uniform_s456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.9604
    arc_challenge_acc_norm: 0.3345
    winogrande_acc: 0.6275
    mmlu_acc: 0.2874
    gsm8k_exact_match: 0.0212
    actual_sparsity: 0.5
- exp_id: longbench_dense_v6
  name: ''
  status: DONE
  conclusion: success
  metrics:
    longbench_narrativeqa: 7.3
    longbench_qasper: 13.4
    longbench_gov_report: 30.5
    longbench_multi_news: 2.5
- exp_id: longbench_kl30_uniform_v6
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    longbench_narrativeqa: 4.12
    longbench_qasper: 6.23
    longbench_gov_report: 16.97
    longbench_multi_news: 18.01
    runtime_seconds: 6156.6
- exp_id: eval_c4_ood_kl50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dense_ppl: 9.2075
    kl_50_global_ppl: 18.401
    teal_50_ppl: 38.7503
    kl_vs_dense_ratio: 2
    teal_vs_dense_ratio: 4.21
- exp_id: db_sensitivity_sweep
  name: ''
  status: DONE
  conclusion: success
  metrics:
    db64_per_token_ppl: 10.158
    db64_teal_global_ppl: 12.076
    db64_sparsity: 0.5
    db64_loss: 0.361
    db128_teal_global_ppl: 11.963
    db128_per_token_ppl: 9.218
    db256_per_token_ppl: 8.586
    db256_teal_global_ppl: 12.105
    db256_sparsity: 0.5
    db256_loss: 0.27
    db512_per_token_ppl: 7.933
    db512_teal_global_ppl: 12.315
    db512_sparsity: 0.5
    db512_loss: 0.224
    best_teal_global_db: 128
    best_teal_global_ppl: 11.963
- exp_id: bce_gumbel_lagrangian_isolation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lr_1e4_ppl: 42.99
    lr_1e3_ppl: 48.4
    lr_3e3_ppl: 38.02
    lr_1e4_bce_loss: 0.7158
    lr_1e3_bce_loss: 0.6781
    lr_3e3_bce_loss: 0.6632
    lr_1e4_sparsity: 0.514
    lr_1e3_sparsity: 0.506
    lr_3e3_sparsity: 0.504
    best_ppl: 38.02
    best_lr: 3e-3
    kl_baseline_ppl: 11.79
    gap_vs_kl: 26.23
- exp_id: steps_curve_s42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: steps_curve_s42_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: steps_curve_s42_v3
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: tau_schedule_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    tau_linear_baseline_ppl: 11.963
    tau_fixed05_ppl: 11.861
    tau_fixed01_ppl: 12.072
    tau_fixed05_loss: 0.248
    tau_fixed01_loss: 0.43
    best_tau: fixed_0.5
    ppl_range: 0.211
- exp_id: steps_curve_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    step200_ppl: 15.158
    step400_ppl: 12.538
    step600_ppl: 12.046
    step800_ppl: 11.907
    step1000_ppl: 11.906
    convergence_step: 800
    ppl_800_vs_1000_delta: 0.001
- exp_id: mistral_kl30_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    kl_per_token_ppl: 6.048
    kl_teal_global_ppl: 6.7733
    teal_baseline_ppl: 8.3807
    dense_ppl: 5.5238
    kl_advantage_ratio: 1.386
    ppl_vs_dense_pct: 9.5
- exp_id: mistral_kl70_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    kl_per_token_ppl: 9.1086
    kl_teal_global_ppl: 13.3254
    teal_baseline_ppl: 61.716
    dense_ppl: 5.5238
    kl_advantage_ratio: 6.77
    final_loss: 0.3945
    actual_sparsity: 0.682
- exp_id: mistral_teal50_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    teal_baseline_ppl: 18.3061
    dense_ppl: 5.5238
    teal_vs_dense_ratio: 3.31
- exp_id: bench_kl70_global
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 17.91
    dense_ppl: 6.12
    actual_sparsity: 0.7
    source: kl_sparsity70_s42_v2 (teal_global_masks protocol)
    vanilla_teal_ppl: 100.11
- exp_id: bench_teal70
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 100.11
    dense_ppl: 6.12
    actual_sparsity: 0.7
    source: training_free_baselines experiment (vanilla teal global)
- exp_id: gradient_snr_kl_vs_bce
  name: ''
  status: DONE
  conclusion: success
  metrics:
    kl_avg_snr: 5.77e-05
    bce_avg_snr: 1.0e-05
    snr_ratio: 5.76
    early_layer_ratio_range: 34-156x
    late_layer_ratio_range: 2-4x
- exp_id: natural_sparsity_floor_30pct
  name: ''
  status: DONE
  conclusion: success
  metrics:
    always_pruned_ratio: 0.0006
    always_pruned_count: 278
    total_neurons: 458752
    late_layer_max_ratio: 0.0051
    threshold: 0.1
- exp_id: teal_kl_overlap_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_jaccard: 0.396
    divergence_ratio: 0.433
    kl_only_pruned_magnitude_ratio: 1.48
    teal_only_pruned_mean_gate_prob: 0.614
    min_jaccard_layer: L17-L18 (0.19)
    max_jaccard_layer: L26-L28 (0.55)
- exp_id: gradient_snr_constrained_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    kl_avg_snr: 0.000545
    bce_avg_snr: 5.28e-06
    snr_ratio: 103.2
    kl_final_sparsity: 0.508
    bce_final_sparsity: 0.591
    steps: 200
- exp_id: sparsity_floor_extended
  name: ''
  status: DONE
  conclusion: success
  metrics:
    floor_30pct: 0.0499
    floor_50pct: 0.0726
    floor_70pct: 0.1936
    late_layer_max_30: 0.4604
    late_layer_max_50: 1.2347
    late_layer_max_70: 4.3666
    threshold: 0.1
    seq_len: 2048
    num_samples: 50
- exp_id: teal_kl_overlap_corrected
  name: ''
  status: DONE
  conclusion: success
  metrics:
    z_score: 7260.3
    p_value: 0
    median_percentile_rank: 78.6
    iqr_q1: 64.4
    iqr_q3: 89.1
    layers_significant: 31/32
    exception_layer: 31
- exp_id: mag_preservation_reg
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: reverse_kl_50pct_s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ppl_wikitext2: 12.8
    vs_forward_kl: +1.01 (+8.6%)
    sparsity: 0.5
- exp_id: jsd_50pct_s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ppl_wikitext2: 12.54
    vs_forward_kl: +0.75 (+6.4%)
    sparsity: 0.5
- exp_id: global_30pct_retention
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    early_retention: 0.771
    middle_retention: 0.764
    knowledge_L12_20_retention: 0.797
    late_L24_31_retention: 0.501
    L31_retention: 0.284
    L30_retention: 0.366
    starved_layers: L27-L31
- exp_id: kl_bce_f1_oracle
  name: ''
  status: DONE
  conclusion: success
  metrics:
    bce_f1: 0.6128
    bce_precision: 0.6132
    bce_recall: 0.6124
    kl_f1: 0.5397
    kl_precision: 0.5112
    kl_recall: 0.5715
    random_f1: 0.5
    kl_ppl: 11.79
    bce_ppl: 22.51
- exp_id: kl50_s123_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.745
    arc_challenge: 0.3814
    winogrande: 0.6125
    mmlu: 0.2752
    gsm8k: 0.0281
- exp_id: kl30_s123_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.8308
    arc_challenge_acc_norm: 0.4531
    winogrande_acc: 0.6938
    mmlu_acc: 0.3944
    gsm8k_exact_match: 0.0751
    actual_sparsity: 0.3
    allocation: uniform
- exp_id: kl50_s456_train_eval
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl50_s456_train
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.397
    final_kl_normalized: 0.397
    final_sparsity: 0.492
    final_lambda: 5000
    final_tau: 0.1
    steps_completed: 1000
- exp_id: kl_50pct_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_wikitext2: 11.745
    arc_challenge_acc_norm: 0.3814
    winogrande_acc: 0.6125
    mmlu_acc: 0.2752
    gsm8k_exact_match: 0.0281
    sparsity: 0.5
    allocation: global
- exp_id: mistral_dense_ppl
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 5.5238
    model: Mistral-7B-v0.3
    condition: dense
    sparsity: 0
- exp_id: mistral_kl30_pertoken
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 6.048
    model: Mistral-7B-v0.3
    condition: kl_pertoken_30pct
    sparsity: 0.3
    allocation: uniform
    ppl_increase_vs_dense: 0.5242
- exp_id: mistral_kl50_pertoken
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 7.2931
    model: Mistral-7B-v0.3
    condition: kl_pertoken_50pct
    sparsity: 0.5
    allocation: uniform
    ppl_increase_vs_dense: 1.7693
- exp_id: mistral_kl70_pertoken
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 9.1086
    model: Mistral-7B-v0.3
    condition: kl_pertoken_70pct
    sparsity: 0.7
    allocation: uniform
    ppl_increase_vs_dense: 3.5848
- exp_id: mistral_kl30_teal_global
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 6.7733
    model: Mistral-7B-v0.3
    condition: kl_teal_global_30pct
    sparsity: 0.3
    allocation: uniform
    ppl_increase_vs_dense: 1.2495
- exp_id: mistral_kl50_teal_global
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.6489
    model: Mistral-7B-v0.3
    condition: kl_teal_global_50pct
    sparsity: 0.5
    allocation: uniform
    ppl_increase_vs_dense: 3.1251
- exp_id: mistral_kl70_teal_global
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 13.3254
    model: Mistral-7B-v0.3
    condition: kl_teal_global_70pct
    sparsity: 0.7
    allocation: uniform
    ppl_increase_vs_dense: 7.8016
- exp_id: mistral_teal30_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.3807
    model: Mistral-7B-v0.3
    condition: teal_vanilla_30pct
    sparsity: 0.3
    allocation: uniform
    ppl_increase_vs_dense: 2.8569
- exp_id: mistral_teal70_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 61.716
    model: Mistral-7B-v0.3
    condition: teal_vanilla_70pct
    sparsity: 0.7
    allocation: uniform
    ppl_increase_vs_dense: 56.1922
- exp_id: kl30_s456_train
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.2021
    actual_sparsity: 0.289
    constraint_satisfied: true
    training_steps: 1000
- exp_id: kl_30pct_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_wikitext2: 8.9748
    arc_challenge_acc_norm: 0.4531
    winogrande_acc: 0.693
    mmlu_acc: 0.3807
    gsm8k_exact_match: 0.0758
    sparsity: 0.3
    allocation: global
- exp_id: kl50_s456_global_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_wikitext2: 11.8057
    arc_challenge: 0.3319
    winogrande: 0.6488
    mmlu: 0.2794
    gsm8k: 0.0212
- exp_id: kl30_s456_global_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl_wikitext2: 8.9332
    arc_challenge: 0.4633
    winogrande: 0.7111
    mmlu: 0.4382
    gsm8k: 0.0758
- exp_id: kl30_s456_uniform_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu: 0.4198
    ppl_uniform: 8.7947
    arc_challenge: 0.4505
    winogrande: 0.6875
    gsm8k: 0.0758
- exp_id: qwen14b_kl30_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dense_ppl: 5.18
    predictor_hard_mask_ppl: 6.8
    teal_global_ppl: 7.62
    ppl_ratio_hard_mask: 1.31
    ppl_ratio_teal: 1.47
    final_loss: 0.3398
    training_sparsity: 0.281
    teal_sparsity: 0.3
    lambda: 5000
    steps: 1000
- exp_id: qwen14b_kl30_s42_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 7.6232
    arc_challenge_acc_norm: 0.5717
    winogrande_acc: 0.7206
    mmlu_acc: 0.6372
    gsm8k_exact_match: 0.4882
- exp_id: downstream_extended_kl30_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    hellaswag_acc_norm: 0.727
    hellaswag_acc: 0.527
    piqa_acc_norm: 0.7595
    piqa_acc: 0.747
    boolq_acc: 0.7685
- exp_id: wallclock_speedup_30_50
  name: ''
  status: PREPARING
  conclusion: negative
  metrics:
    theoretical_flops_speedup_30pct: 1.36
    theoretical_flops_speedup_50pct: 2.45
    actual_wallclock_speedup_30pct: 0.91
    actual_wallclock_speedup_50pct: 0.6
    predictor_overhead_decode_ms: 1
    predictor_overhead_prefill_ms: 2
    actual_mean_sparsity_30pct: 0.28
    actual_mean_sparsity_50pct: 0.605
    note: No wall-clock speedup without sparse kernels. Mask-based=0.87-0.94x (predictor
      overhead), structured-skip=0.45-0.74x (gather overhead). Report theoretical
      FLOPs in paper.
- exp_id: qwen14b_bce30_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    dense_ppl: 5.18
    predictor_hard_mask_ppl: 5.57
    teal_global_ppl: 8.76
    ppl_ratio_hard_mask: 1.075
    ppl_ratio_hard_mask_note: at predictor native 6.4% sparsity, not comparable to
      KL's 28.1%
    ppl_ratio_teal: 1.69
    actual_sparsity_teal: 0.3
    predictor_native_sparsity: 0.064
    training_log_sparsity_note: Training Lagrangian failed (predictor sparsity=6.4%).
      Inference via TEAL forces 30% externally. TEAL PPL 8.76 is valid for method
      comparison.
    final_loss: 0.5561
    final_bce_loss: 0.5324
    steps: 1000
    constraint_satisfied: false
- exp_id: qwen14b_teal30_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.7332
    arc_challenge_acc_norm: 0.5683
    winogrande_acc: 0.7269
    mmlu_acc: 0.7183
    gsm8k_exact_match: 0.4951
- exp_id: qwen14b_bce30_s42_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    predictor_native_sparsity: 0.064
    lambda_max: 50000
    final_bce_loss: 0.5324
    steps: 1000
    constraint_satisfied: false
    sparsity_trajectory: 49%→5% collapse in 50 steps, no recovery over 950 steps
    note: 10x stronger Lagrangian produces identical sparsity as v1 (lambda=5000).
      Confirms BCE gradient insufficiency is fundamental, not constraint strength.
- exp_id: downstream_dense_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    hellaswag_acc_norm: 0.8233
    hellaswag_acc_norm_stderr: 0.0038
    piqa_acc_norm: 0.8074
    piqa_acc_norm_stderr: 0.0092
    boolq_acc: 0.8294
    boolq_acc_stderr: 0.0066
- exp_id: qwen14b_bce30_s42_eval
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    wikitext2_ppl: 8.7634
    arc_challenge_acc_norm: 0.5759
    winogrande_acc: 0.7261
    mmlu_acc: 0.7167
    gsm8k_exact_match: 0.5307
- exp_id: downstream_teal30_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    hellaswag_acc: 0.4878
    hellaswag_acc_norm: 0.667
    piqa_acc: 0.7258
    piqa_acc_norm: 0.7361
    boolq_acc: 0.685
- exp_id: kl50_global_s123_reeval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.7184
    arc_challenge_acc_norm: 0.3635
    winogrande_acc: 0.6109
    mmlu_acc: 0.2834
    gsm8k_exact_match: 0.0258
- exp_id: bce_isocompute_v3_s123
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: bce_isocompute_v3_s456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.6368
    final_sparsity: 0.51
    training_steps: 2700
- exp_id: c4_ood_kl30_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_ppl: 16.0458
    allocation: global_topk
    sparsity: 0.3
    model: llama-3.1-8b
    eval_sequences: 132
    seq_len: 2048
- exp_id: c4_download
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: qwen14b_dense_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ppl: 5.1854
    arc_challenge: 0.6758
    winogrande: 0.8106
    mmlu: 0.7977
    gsm8k: 0.8757
- exp_id: bce_isocompute_v3_s456_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    teal_sparse_ppl: 28.3503
    model_level_sparsity: 0.5
    arc_challenge_acc: 0.2312
    arc_challenge_acc_stderr: 0.01232
    arc_challenge_acc_norm: 0.2807
    arc_challenge_acc_norm_stderr: 0.01313
    winogrande_acc: 0.5241
    winogrande_acc_stderr: 0.01404
    mmlu_acc: 0.2567
    mmlu_acc_stderr: 0.00367
    gsm8k_exact_match: 0.022
    gsm8k_exact_match_stderr: 0.00404
    gsm8k_exact_match_strict: 0.00834
    gsm8k_exact_match_strict_stderr: 0.0025
- exp_id: bce_isocompute_v3_s123_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 28.0627
    arc_challenge_acc_norm: 0.2696
    winogrande_acc: 0.513
    mmlu_acc: 0.2655
    gsm8k_exact_match: 0.022
- exp_id: qwen14b_kl30_uniform_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: qwen14b_teal30_uniform_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: kl30_8b_s123_train
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9267
    sparsity: 0.3
    training_loss: 0.147
- exp_id: kl30_8b_s456_train
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9614
    sparsity: 0.3
    training_loss: 0.148
- exp_id: qwen14b_kl30_uniform_eval_4task
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    wikitext2_ppl: 7.63
    mmlu_acc: 0.6449
    arc_challenge_acc_norm: 0.5444
    winogrande_acc: 0.7245
- exp_id: qwen14b_teal30_uniform_eval_4task
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.01
    mmlu_acc: 0.6634
    arc_challenge_acc_norm: 0.5529
    winogrande_acc: 0.6985
- exp_id: bce_isocompute_v3_s42_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 27.9696
    arc_challenge_acc: 0.2346
    arc_challenge_acc_norm: 0.2765
    winogrande_acc: 0.5162
    mmlu_acc: 0.2614
    gsm8k_exact_match: 0.019
- exp_id: kl30_8b_s123_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9267
    arc_challenge_acc: 0.4462
    arc_challenge_acc_norm: 0.4744
    winogrande_acc: 0.7024
    mmlu_acc: 0.3836
    gsm8k_exact_match: 0.0917
- exp_id: kl30_8b_s456_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9614
    arc_challenge_acc: 0.436
    arc_challenge_acc_norm: 0.4462
    winogrande_acc: 0.7143
    mmlu_acc: 0.2714
    gsm8k_exact_match: 0.0887
- exp_id: snr_extended_r6w3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    kl_snr_step300: 0.0058773
    bce_snr_step300: 0.00114449
    snr_ratio_step300: 5.14
    kl_train_time_s: 641
    bce_train_time_s: 320
    num_checkpoints: 7
    steps_range: 0-300
- exp_id: c4_ood_kl30_s123
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: c4_ood_dense_baseline
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: kl50_s123_uniform_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.89
    arc_challenge_acc_norm: 37.88
    winogrande_acc: 62.19
    mmlu_acc: 27.75
    gsm8k_exact_match: 2.35
    comparison_vs_global_topk:
      ppl_delta: -0.94
      arc_c_delta: -5.55
      wg_delta: -6.71
      mmlu_delta: -8.2
      gsm8k_delta: -5
    note: 'Uniform allocation: better PPL but catastrophic downstream degradation
      vs global_topk. Confirms global_topk allocation is critical for downstream quality.'
- exp_id: c4_ood_kl30_s123_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_ppl: 16.0259
    allocation: global_topk
    sparsity: 0.3
    model: llama-3.1-8b
    eval_sequences: 132
    seq_len: 2048
- exp_id: c4_ood_dense_baseline_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_ppl: 9.2075
    model: llama-3.1-8b
    eval_sequences: 132
    seq_len: 2048
- exp_id: kl50_s456_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.8614
    arc_challenge_acc_norm: 0.3754
    winogrande_acc: 0.6417
    mmlu_acc: 0.2784
    gsm8k_exact_match: 0.0212
- exp_id: c4_ood_kl50_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_ppl: 23.6064
    allocation: global_topk
    sparsity: 0.5
    model: llama-3.1-8b
- exp_id: downstream_ext_kl50_uniform_s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: downstream_ext_kl30_uniform_s123
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: c4_ood_kl50_s456
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_ppl: 23.9867
    sparsity: 0.5
    allocation: global_topk
    seed: 456
- exp_id: c4_ood_kl30_s42_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_ppl: 16.0401
    allocation: global_topk
    sparsity: 0.3
    model: llama-3.1-8b
    seed: 42
- exp_id: kl50_s42_uniform_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.9638
    arc_challenge_acc_norm: 0.3259
    winogrande_acc: 0.6235
    mmlu_acc: 0.2792
    gsm8k_exact_match: 0.0197
- exp_id: c4_ood_kl50_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    c4_ppl: 23.5297
    sparsity: 0.5
    allocation: global_topk
    seed: 42
- exp_id: kl_comp_30pct_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.6992
    steps: 1000
    compensation_params: 67248128
    compensation_pct: 0.837
    mean_head_norm_final: 9.2012
    loss_trajectory:
    - 2.3594
    - 1.3516
    - 1.0859
    - 0.9219
    - 0.8789
    - 0.8281
    - 0.7461
    - 0.7344
    - 0.6953
    - 0.6992
- exp_id: c4_ood_kl30_s456
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: kl_comp_30pct_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.7617
    steps: 1000
    compensation_params: 67248128
    compensation_pct: 0.837
    mean_head_norm_final: 9.2012
    loss_trajectory:
    - 2.0469
    - 1.3828
    - 1.0703
    - 0.9609
    - 0.8711
    - 0.7305
    - 0.6875
    - 0.7773
    - 0.7969
    - 0.7617
- exp_id: kl_comp_30pct_s42_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9788
    arc_challenge_acc_norm: 0.3993
    winogrande_acc: 0.6898
    mmlu_acc: 0.2531
    gsm8k_exact_match: 0.0842
- exp_id: kl_comp_30pct_s42_ppl
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9768
    c4_ppl: 16.0401
    sparsity: 0.3
    allocation: global_topk
    model: llama-3.1-8b
    seed: 42
- exp_id: kl_comp_30pct_s123_ppl
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9768
    c4_ppl: 16.0401
    sparsity: 0.3
    allocation: global_topk
    model: llama-3.1-8b
    seed: 123
- exp_id: kl_comp_30pct_s123_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9788
    arc_challenge_acc_norm: 0.3993
    winogrande_acc: 0.6898
    mmlu_acc: 0.2531
    gsm8k_exact_match: 0.0842
- exp_id: kl50_s456_uniform_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.9538
    arc_challenge_acc_norm: 0.3831
    winogrande_acc: 0.6196
    mmlu_acc: 0.275
    gsm8k_exact_match: 0.0288
- exp_id: kl_comp_30pct_s456
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: kl_comp_50pct_s42
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: kl_comp_30pct_s456_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.9614
    arc_challenge_acc_norm: 0.4462
    winogrande_acc: 0.7143
    mmlu_acc: 0.2714
    gsm8k_exact_match: 0.0887
- exp_id: kl_comp_50pct_s42_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.7933
    arc_challenge_acc_norm: 0.3285
    winogrande_acc: 0.6346
    mmlu_acc: 0.2789
    gsm8k_exact_match: 0.0129
- exp_id: kl50_s42_global_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.8038
    arc_challenge_acc_norm: 0.3336
    winogrande_acc: 0.6338
    mmlu_acc: 0.2819
    gsm8k_exact_match: 0.0167
- exp_id: kl30_s123_uniform_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.8186
    arc_challenge_acc_norm: 0.471
    winogrande_acc: 0.6961
    mmlu_acc: 0.3763
    gsm8k_exact_match: 0.0705
- exp_id: kl30_s456_uniform_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 8.8284
    arc_challenge_acc_norm: 0.4505
    winogrande_acc: 0.6953
    mmlu_acc: 0.3727
    gsm8k_exact_match: 0.0705
- exp_id: kl30_s123_uniform_v3
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: kl30_s456_uniform_v3
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: c1_ablation_bce_kl_targets_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wt2_ppl: 9.29
    eval_sparsity: 0.609
    oracle_agreement: 0.978
    final_bce_loss: 0.0545
    train_steps: 1000
    train_time_sec: 877.1
    reference_kl_ppl: 11.79
    reference_bce_ppl: 22.51
- exp_id: bce_30pct_s42
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: kl_sparsity25_s42
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity35_s42
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: c1_ablation_eval_uniform
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity45_s42
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: bce_30pct_s42_eval
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}


## what_if (hypothetical experiments — additive)

- name: c1_ablation_bce_kl_targets
  claim: 'Claim 1 reframe: optimization target quality > gradient coupling'
  description: BCE trained on KL-derived oracle masks achieves comparable-or-better
    PPL than KL distillation at matched sparsity. 53% mask divergence from magnitude
    oracles. Core narrative shifts from 'gradient coupling explains KL advantage'
    to 'KL discovers fundamentally different and superior mask patterns that magnitude-based
    oracles miss'.
  estimated_gpu_hours: 0.0
- name: dense_sparsity_sweep_6pt
  claim: 'Claim 3: regime analysis with 6 data points'
  description: KL predictors trained at 25%/30%/35%/40%/45%/50% sparsity with 2 seeds
    each. Regime boundaries precisely mapped. Non-monotonic allocation preference
    confirmed with denser sampling.
  estimated_gpu_hours: 0.0
- name: bce_30pct_forced_topk
  claim: 'Claim 1: BCE baseline at recommended operating point'
  description: BCE predictor evaluated at 30% via forced TEAL top-k. Fills Table 2
    gap at recommended operating point. BCE PPL expected significantly worse than
    KL, strengthening KL advantage at practical deployment sparsity.
  estimated_gpu_hours: 0.0

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
  "promptId": "f15ac05d-9ce1-4f1f-8124-4b88f655f612",
  "type": "user",
  "uuid": "134f807e-369e-47c8-bac8-321b8d8f96be",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T16:40:26.156Z_

```json
{
  "parentUuid": "134f807e-369e-47c8-bac8-321b8d8f96be",
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
  "uuid": "3bc33e2b-c3f9-4b64-af29-127647b128ac",
  "timestamp": "2026-05-18T16:40:26.156Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T16:40:26.156Z_

```json
{
  "parentUuid": "3bc33e2b-c3f9-4b64-af29-127647b128ac",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "19f3132a-ed93-4956-b92a-43d871dcf957",
  "timestamp": "2026-05-18T16:40:26.156Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1 ablation 显示 mask quality 解释大部分但非全部 KL 优势（存在 2-3 PPL residual gap）；部分实验噪声偏大；需调整 claim 强度和补充讨论 核心假设：['BCE-on-KL-targets at 50% uniform PPL 在 12.5-15.0——…",
  "leafUuid": "19f3132a-ed93-4956-b92a-43d871dcf957",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation outperforms BCE in sparse SwiGLU predictors",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725"
}
```

---

### Assistant

_source line 8 · 2026-05-18T16:48:13.371Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, based on the "median" tier definition. Let me carefully go through each experiment that has status "planned" or is in the "what_if" section, and generate realistic predicted results with rationales.

Let me identify the experiments that need predictions:

From experiment_plan with status that needs data:
1. plan_010 - LongBench evaluation (status: planned)
2. plan_011 - MT-Bench evaluation (status: planned)
3. plan_012 - RULER synthetic long-context (status: planned)


4. plan_013 - kl_sparsity25_s42 (status: PREPARING)
5. plan_014 - kl_sparsity35_s42 (status: PREPARING)
6. plan_015 - c1_ablation_eval_uniform (status: PREPARING)
7. plan_016 - kl_sparsity45_s42 (status: PREPARING)
8. plan_017 - bce_30 (status: PREPARING)

From what_if section, I also need to generate predictions for the ablation variants and sparsity sweeps that haven't been completed yet.

Now I'm looking at the median tier definition more carefully. The C1 ablation shows that mask quality explains most but not all of the KL advantage, with a residual gap of 2-3 PPL points. Some experiments have noisy results, so I need to adjust claim strength and add discussion. BCE-on-KL-targets at 50% uniform gives PPL 12.5-15.0, which is better than vanilla BCE at 28.0 but worse than KL at 11.8. The 6-point sparsity sweep shows a visible trend but individual points deviate, making the regime boundary fuzzy at around ±5 percentage points. KL at 30% uniform across 3 seeds shows MMLU standard deviation of 2-4 percentage points. At least one reviewer questions novelty and another notes something at 14.

Some of the sweep experiments at 25% and 45% sparsity didn't finish by the deadline, so I'm working with 4-point data instead. The expected overall ARR is around 3.0-3.5. Now I'm constructing predictions and need to be very careful about consistency with the existing data points I have: dense PPL at 6.12, KL 50% global PPL around 11.79, KL 30% uniform at 8.82, BCE 50% at 27.97, TEAL 30% at 10.97, TEAL 50% at 23.31, and the C1 ablation BCE-on-KL-targets at 9.29 with sparsity 0.609.

For the C1 ablation at 50% uniform sparsity, I'm expecting PPL in the 12.5-15.0 range. The existing ablation result at 0.609 sparsity gave 9.29, but that's a different evaluation point. When I evaluate at 50% uniform, the performance should degrade to that 12.5-15.0 band, which gives me a residual gap of roughly 1.7 to 3.2 PPL points above the KL 50% baseline of 11.79.

Now I'm recalculating the mask quality contribution more carefully. Vanilla BCE at 50% uniform gives about 28.0 PPL, while KL achieves 11.8, for a total gap of 16.2. If BCE trained on KL-derived targets lands around 13.5 PPL, that means mask quality alone closes 14.5 points of the gap—roughly 89% of the total KL advantage.

But the stated range of 60-75% suggests I should reconsider what's being measured. If mask quality truly explains 60-75% of the 16.2-point gap, then BCE-on-KL-targets should fall between 15.85 and 18.28 PPL, which doesn't align with the 13.5 estimate I'm seeing. Looking at the residual gap of 2-3 PPL between the KL-targeted approach and vanilla BCE, the numbers suggest BCE-on-KL-targets should land around 13.8-14.8, which fits the observed 12.5-15.0 range. But when I calculate the mask quality contribution as a percentage of total KL advantage, I'm getting around 86%, which overshoots the stated 60-75%—so either the baseline or metric definition differs from what I'm assuming, or there's some inconsistency in how the narrative describes the results versus the actual ranges. I need to organize the experiments I'm planning to run. There are three main benchmarks I want to test—LongBench, MT-Bench, and RULER—plus several ablation studies exploring different configurations like BCE versus KL targets, sparsity levels, and forced top-k masking. I'm also tracking some in-progress experiments that are currently being prepared, including KL runs at different sparsity percentages.

The user is asking me to provide detailed predictions specifically for the planned experiments in the experiment_plan, so I should focus on plan_010, plan_011, and plan_012 rather than all the ablation work.

Looking at the registry, I can see that some of the PREPARING experiments are actually sub-components of these planned experiments—the sparsity sweep variants are part of the dense sparsity experiment, the C1 ablation evaluation is its own thing, and the BCE evaluation is part of the forced topk experiment. Now I'm ready to construct the actual predictions for each of these planned experiments.

For plan_010's LongBench evaluation, I'm noticing the existing dense baseline scores are quite low and there were multiple failed attempts before v6 succeeded, which suggests there might be evaluation issues. The KL30 uniform results show some unexpected jumps (like multi_news going from 2.5 to 18.01), so I'm skeptical about the reliability of these numbers. I'd expect the KL-only approach at 30% sparsity to degrade performance on long-context tasks, but the baseline numbers themselves seem questionable.

For the median tier narrative, I'm seeing that the C1 ablation demonstrates mask quality is a significant factor but not the only one—there's still a residual gap of 2-3 PPL even after accounting for it. The phase transition appears to be an equally important contributor. Some experiments remain incomplete, and I'm projecting an overall ARR in the 3.0-3.5 range for this tier.

MT-Bench and RULER are both P2 priorities that might not make the deadline, with RULER depending on plan_010's completion. Now I'm working through the YAML output and drafting predictions for the C1 ablation at 50% uniform sparsity.

Looking at the C1 ablation results, the model trained on BCE with KL-derived oracle targets achieves around 12.5-15.0 PPL when evaluated at 50% uniform allocation, compared to KL's 11.8. The sparsity mismatch between training (~60%) and evaluation (50%) plus BCE's lack of end-to-end gradient flow through masking explains the gap. This suggests mask quality accounts for roughly 14.5 PPL of the total 28.0 baseline gap, with the remaining contribution coming from the phase transition effect. I'm trying different baseline comparisons to see if any yield that 60-75% range—comparing TEAL at 50% to the KL-targeted BCE variant gets me to 85%, which is still too high. The vanilla BCE numbers don't quite line up either since it wasn't tested at 50% uniform. I'm starting to think the 60-75% figure might be a rougher narrative estimate that doesn't map precisely to the PPL metrics I'm working with.

The key is to stick with the specified metric ranges (12.5-15.0) and frame the remaining gap as coming from optimization dynamics. Looking at the median tier experiments, I see that the 25% and 45% sparsity sweeps weren't completed before the deadline, so I only have four data points available: 30%, 35%, 40%, and 50%. Now I need to compile the full YAML with the PPL values I have for each of these points.

Looking at the actual data more carefully, I notice the PPL values show non-monotonic behavior—the 40% sparsity point (8.36) is actually lower than the 30% point (8.82), and then 50% jumps up to 11.96. For the missing 35% point, I should interpolate somewhere in the 8.2-8.6 range to fit between these values.

The 25% and 45% experiments didn't finish before the deadline, so I'm working with four data points: 30%, 35%, 40%, and 50%. Now I need to construct predictions for the other model variants, starting with the BCE predictor at 30% sparsity using forced top-k selection, which should fall in the 10.0-13.0 PPL range based on the 50% sparsity baseline of around 28.0.

For the remaining experiments, LongBench (plan_010) likely won't complete cleanly given previous failures, though I have dense baselines to reference. MT-Bench (plan_011) requires external APIs and probably won't finish in the median tier, and RULER (plan_012) depends on plan_010 anyway so it's unlikely to complete.

Now I'm calculating the seed variance across my three KL 30% uniform MMLU runs—the scores range from 0.3727 to 0.4061, giving me a standard deviation of about 0.018, which suggests moderate variability across seeds.

That's notably lower than the 2-4pp range I'd expect for the median tier, though with only three seeds the estimate could shift. I'll use 2.5pp as my prediction since it falls comfortably within the expected range and accounts for the possibility that my current sample is slightly underestimating the true variance.

Now I need to clarify what I'm actually predicting here—the existing data is real, but I'm generating predictions for the planned experiments that haven't run yet: LongBench, MT-Bench, and RULER, plus the what-if ablations and sweeps.

Looking at the sub-experiments in progress, I can see some are already done (like the BCE and KL ablations with seed 42) while others are still preparing, so I'll need to extrapolate from the completed runs to estimate the full results.

Generating the YAML output...

For plan_010, the LongBench evaluations have been challenging—earlier versions failed but v6 finally got results for the dense baseline and KL30 uniform, though the scores were underwhelming and suggested KL30 might not be the right direction. The dense model hit narrativeqa at 7.3 and qasper at 13.4, while KL30 uniform dropped narrativeqa to just 4.

12 with qasper at 6.23. Looking at the median tier results, KL at 50% would likely show even steeper drops, and the noise in the data makes it hard to draw firm conclusions about what's actually working.

Plan_011 with MT-Bench is lower priority and depends on GPT-4o access, so it's probably not going to happen before the deadline. Same story with plan_012 on RULER—it's blocked on plan_010 finishing and also unlikely to complete in time.

Now examining the c1_ablation setup with uniform 50% allocation. The existing model trained at around 60% sparsity is being evaluated under this constraint, and I'm expecting median perplexity in the 12.5-15.0 range, roughly 13.8. The BCE predictor trained on KL-oracle masks performs much better than vanilla BCE because it learns from actual gradient signals, but it still can't fully replicate the end-to-end optimization that KL provides. That gap of about 2 PPL points comes down to how Gumbel-sigmoid relaxation during training gives smoother gradients than hard straight-through estimation, plus the fact that KL optimization adjusts masks based on actual downstream loss rather than just local classification accuracy.

For the dense sparsity sweep, I have six target points across 25% to 50% sparsity. Three are already measured: 30% at 8.82, 40% at 8.36, and 50% at 11.96. The non-monotonic dip at 40% is interesting. I need to predict 35%, which should fall between the 30% and 40% values, so around 8.45. With four data points total, I can fit a piecewise model with R² in the 0.80-0.93 range to capture this non-monotonic behavior.

For downstream metrics at 35% sparsity, I'm interpolating between the 30% and 40% uniform KL results. MMLU shows a sharp drop from 0.406 to 0.307, so 35% likely lands around 0.35-0.38. I also need to check the status of the BCE experiments—30% with seed 42 is complete, but I'm still waiting on other seed variants.

Looking at the perplexity estimates, I'm settling on around 11.5 as a reasonable median for the 30% BCE case, since the gap between KL and BCE narrows at lower sparsity levels where most model capacity is preserved anyway. Now I'm compiling everything into YAML format and also calculating the seed variance for MMLU across the three runs to validate the 2-4 percentage point standard deviation estimate. I'm realizing the what_if scenario is asking me to predict results for experiments that haven't run yet, whereas the existing data points are already fixed. The median tier's 2-4pp standard deviation range might represent expected variance with confidence intervals or additional seeds, but my current three seeds show only 1.83pp. For this exercise, I should probably generate synthetic results that align with the tier's expected variance range.

Now I need to identify which experiments actually need predictions—the three planned experiments from the plan plus the three what_if scenarios—and write out comprehensive YAML predictions for each one. I have some historical data from v6 runs for LongBench that I can use as a reference point for plan_010's median tier estimates. That multi_news spike from 2.5 to 18.01 is definitely odd—could be a metric calculation error or something specific to how that dataset interacts with the KL regularization. I'll treat it as noisy data for now and assume the median tier results will be similarly unpredictable. Most conditions will probably show KL 30% causing moderate degradation while KL 50% tanks performance, though some tasks might behave unexpectedly like multi_news did. Now I need to figure out which tables and figures these experiments feed into and structure the final YAML accordingly.

For the c1_ablation at 50% uniform specifically, the predictor was trained on KL-oracle masks with BCE loss and achieved 97.8% agreement with oracle masks, but when forced to 50% uniform sparsity instead of its native 60.9%, there's a mismatch—keeping more neurons should theoretically help PPL, but removing the learned per-layer budget allocation will hurt it.

The real issue is that the 97.8% agreement was measured at the training sparsity of 60.9%, not at the 50% evaluation sparsity, so when I force the sparsity down to 50% via top-k selection, the mask pattern changes and the agreement metric no longer applies.

Beyond that, the BCE predictor's probability calibration might be worse at the 50% threshold compared to where it was trained at 60.9%, and without the end-to-end KL gradient signal, it's not optimizing for output distribution quality at the evaluation sparsity level.

But there's something odd here—the ablation gets 9.29 PPL at its native 60.9% sparsity, yet at 50% uniform it's performing worse (12.5-15.0 PPL), even though 50% means keeping more neurons. That's counterintuitive unless the uniform allocation is really hurting performance compared to the learned allocation.

Looking at the actual KL values, 50% uniform is 11.96 versus 11.79 for 50% global, so the uniform strategy adds about 0.17 PPL. The real issue is that the 9.29 baseline was achieved with the predictor's native per-token hard mask at 60.9% sparsity, not at 50% uniform. When forced into a completely different allocation strategy, the predictor has to adapt, and that's where the performance gap comes from—it's not that 50% uniform is inherently worse, but that it's a different allocation pattern than what the model was optimized for.

The predictor was trained to match KL oracle masks at its native sparsity level, so when you force it to 50% uniform and take the top-50% of scores per layer, you're operating at a different point than training intended. The score calibration and ranking quality matter here, and BCE training might produce worse-calibrated rankings than KL training would.

I'll move forward with the given metrics and write out the YAML with reasonable predictions for the remaining sparsity points.

Looking at the completed measurements, I can see a clear regime shift between 40% and 50% where PPL jumps from 8.36 to 11.96, suggesting a transition point around 40-45%. With four data points and this noise, a piecewise fit would likely achieve an R² around 0.80-0.93. The lower sparsity levels (30-40%) appear to be in a budget-surplus regime where uniform masking performs better, while higher sparsity pushes into a different operating regime.

Now I'm working through the downstream metrics for each sweep point to complete the picture, starting with the 35% configuration. Looking at the bce_30pct_s42 experiment, the training is done but evaluation is still preparing, and I notice the metrics are empty so I need to estimate them. The BCE predictor at 30% sparsity should perform worse than KL at the same level, so I'm projecting downstream scores around 0.38 for ARC-c, 0.65 for WG, 0.34 for MMLU, and 0.06 for GSM8K, with PPL in the 10-13 range.

Now I'm ready to write out the YAML configuration. For the LongBench evaluation in plan_010, I need to map out predictions across multiple conditions—dense baseline, KL at 30% and 50%, TEAL at both levels, SPON, and the untrained BCE+comp variant. Some of these will likely produce noisy results in the median tier, so I'm starting to estimate what KL 50% would yield across the different benchmarks.

I should also clarify the scope: the user wants detailed data for all planned experiments (plan_010, plan_011, plan_012) plus the what-if scenarios, and I need to account for the fact that some registry experiments are still in progress. Let me make sure I'm being comprehensive without overextending.

Now I'm structuring the final output with a narrative that honestly addresses the findings: KL's advantage comes primarily from better mask patterns, which BCE-on-KL-targets largely recovers (bringing PPL down from 28.0 to 13.8), but there's still a 2.0 PPL gap compared to pure KL at 11.8, suggesting the continuous optimization from Gumbel relaxation provides additional independent benefit. I need to reframe Claim 1 to acknowledge mask quality as the dominant factor while being transparent about what the residual gap tells us.

The phase transition analysis shows a regime boundary around 38±5% sparsity, though the picture is incomplete due to some unfinished runs. When I force BCE to use top-k at 30% sparsity, the gap narrows significantly, which supports the sparsity-dependent advantage story. The MMLU results at 30% show meaningful variance across seeds that I'll need to present carefully with confidence intervals. LongBench results are partial and noisy, which weakens but doesn't invalidate the long-context claims. I'm aiming for the Findings track initially, with the Main track achievable through revision once I have the missing sweep data.

Looking at the existing MMLU variance across three seeds, I'm getting around 1.83 percentage points, which sits slightly below what the median tier expects (2-4pp). The individual seed values cluster fairly tightly, so either the variance prediction was conservative or additional seeds might show more spread. the data is already collected. Maybe I should include this discrepancy in the analysis. The observed σ is 1.83pp, which is slightly below the median tier's expected 2-4pp, but still large enough to warrant careful presentation with CIs.

Now I'm looking at the global seed results for KL 30%, and the variance there is dramatically different—σ comes out to about 9.47pp, which is substantially higher than what I'm seeing in the uniform setup.

Let me stop second-guessing myself and just write out the YAML predictions systematically, working through each planned experiment and providing clear rationales for the numbers I'm choosing.

Now I'm mapping out the tables and figures that will support these predictions—a main comparison table at 50% uniform allocation showing dense, TEAL, BCE, KL, and other variants, a multi-sparsity breakdown across 30%, 40%, and 50%, cross-model generalization results, the C1 ablation findings, and allocation strategy comparisons, plus a Pareto frontier figure and a sparsity sweep visualization with regime boundaries.

I should also cross-reference the experiments currently preparing to see which ones feed into these planned analyses—the KL sparsity sweeps at 25%, 35%, and 45% are part of the broader sparsity sweep, the C1 ablation evaluation is underway, and the BCE 30% evaluation is queued up, so I can start predicting the metrics based on what's already running.

Looking at the completion timeline, the 35% KL sparsity variant, C1 ablation, and BCE evaluation should all finish within the median tier, while the 25% and 45% variants will likely miss the deadline. Now I'm writing out the final YAML configuration with the narrative guidance about the C1 reframe showing partial success and the BCE-on-KL results showing meaningful but incomplete improvements over vanilla BCE.

For the mask quality analysis, I'm breaking down how much of KL's advantage comes from better mask quality versus continuous optimization—around 88% from masks and 12% from optimization, though this shifts to roughly 72% when using log-PPL, which reviewers might prefer as the more conservative estimate. I'm revising Claim 1 to emphasize that KL improves both factors with mask quality as the primary driver, and I'll add discussion to separate these contributions. On the phase transition front, I'm upgrading Claim 3 to co-equal contribution status since the 6-point sweep only captured 4 points due to the incomplete runs, leaving the regime boundary somewhere around 38±5% sparsity—detectable but not precisely pinned down.

Now looking at the piecewise fit quality and performance gaps: the model fits with R² around 0.87, though a few points like the 35% sparsity case show larger deviations of about 0.5 PPL. The BCE forced top-k approach at 30% sparsity gives PPL around 11.5 compared to KL's 8.82, and this gap narrows at higher sparsity levels, which supports the narrative that KL's advantage depends on sparsity. For the MMLU results with 3 seeds at 30% sparsity, the standard deviation is borderline at roughly 1.8 percentage points, so I'll report it as 2pp and present everything with proper confidence intervals rather than cherry-picking. The LongBench evaluation is partially complete with dense and KL 30% data available, but other conditions still need to be run.

The remaining benchmarks show noise issues and unexplained anomalies in multi_news, while MT-Bench and RULER haven't been started yet due to lower priority. The paper will likely land in Findings on the first round, and I can push for Main track acceptance after filling in the missing sparsity sweeps at 25% and 45% plus completing the full LongBench dataset. I'm expecting an overall ARR around 3.2, though I anticipate at least one reviewer will question the novelty of KL distillation and another will point out the unresolved gap in 14B MMLU performance. I'm also planning an ablation experiment comparing BCE and KL targets at 50% uniform sparsity. Looking at the downstream task performance metrics across multiple benchmarks, I see the BCE-on-KL approach successfully captures the oracle's mask decisions with high agreement, but there's a residual gap when evaluated at the 50% uniform sparsity level due to a mismatch between training sparsity (60.9%) and evaluation sparsity—this causes about 5% of borderline neurons to rank differently at the 50% cutoff compared to the KL oracle.

The core issue is that BCE optimizes binary decisions per-neuron without understanding how mask changes jointly affect the output distribution, so even with nearly identical masks, it can't fine-tune borderline decisions to minimize KL divergence the way the Gumbel-sigmoid relaxation in KL training does by providing a continuous gradient landscape for smoother trade-offs.

The perplexity improvements tell the story: 13.8 PPL versus vanilla BCE's 28.0 represents a 14.2 PPL gain from better mask quality, with a residual 1.84 PPL gap compared to the KL baseline, suggesting mask quality explains about 88% of the performance difference when calculated linearly, though the relationship appears different when using log-PPL scaling.

Now I need to clarify this decomposition in the discussion by reporting both calculation methods, and I'm planning tables and figures to show how the vanilla BCE to KL progression breaks down, with the residual gap annotated to demonstrate that continuous optimization dynamics contribute independently beyond just mask pattern discovery.

The key insight is that KL improves both mask quality and optimization fidelity, not just one or the other. Even if we gave BCE the perfect target masks, the per-neuron factorized loss still can't capture the global budget allocation effects, which weakens the narrative simplicity but strengthens the scientific honesty. I'm also setting up an experiment with BCE at 30% sparsity evaluated through forced top-k to fill a gap in the results at the recommended operating point.

Looking at the performance metrics now—at 30% sparsity, the BCE versus KL gap narrows to about 1.3× compared to 2.4× at 50% sparsity, which suggests the gap shrinks as we move toward lower sparsity levels.

The key insight is that at lower sparsity, most of the retained neurons are genuinely important and most pruned ones are truly unimportant, so the mask selection becomes less critical. Additionally, with 70% of neurons active, inter-neuron interactions weaken and the network behaves more densely, making BCE's factorized assumption more realistic. However, BCE still underperforms the TEAL-free baseline—11.5 versus 10.97—indicating that the learned predictor provides only marginal value at this sparsity level.

Now I'm noticing that training-free methods already perform well at 30% sparsity, and BCE's learning actually introduces calibration errors, which supports the narrative that KL is the only learned method worth deploying. But I need to be careful here—if BCE at 11.5 is essentially equivalent to TEAL at 10.97, reviewers might argue that the learned advantage is mainly a high-sparsity phenomenon. The right response is to emphasize that the sparsity-dependent advantage pattern itself is a meaningful part of the regime analysis, and I should reference the multi-sparsity comparison table to support this.

For the figures and appendix, I'm adding the BCE 30% results to both the sparsity sweep and Pareto frontier visualizations, and including full BCE baseline results across all sparsity levels in the appendix. The key insight is that KL's advantage is clearly sparsity-dependent—showing a 2.4× improvement at 50% but only 1.3× at 30%—which directly supports Claim 3 about regime-specific performance. If the gap turns out to be smaller than 1.3×, I'll need to acknowledge in the discussion that KL's practical deployment advantage is really concentrated in higher sparsity scenarios above 40%.

The critical comparison will be in Table 2 where BCE 30%, KL 30%, and TEAL 30% sit side by side—if those three converge into the noise range, then the recommendation at 30% sparsity becomes that TEAL is the free option or KL offers only marginal gains. For the sparsity sweep experiment, I have KL predictors trained at four points (30%, 35%, 40%, 50%) since the median tier didn't complete the 25% and 45% runs, and I'm using these four points to analyze where the regime boundaries actually shift.

Compiling the expected results from the 35% sparsity point and the piecewise fit across all four points to estimate the regime boundary around 38% with roughly 5 percentage points of uncertainty. The non-monotonic PPL pattern continues because pruning in the 30-40% range removes mostly redundant neurons that were actually hurting output sharpness, but beyond ~42% sparsity we hit a capacity cliff where functionally important neurons get pruned and PPL spikes. MMLU shows consistent decline across all sparsity levels since it's more sensitive to capacity loss and requires specific knowledge neurons that get removed even when PPL stays stable, supporting the idea that PPL is a poor proxy for downstream task performance. The piecewise fit with four segments achieves an R² of ~0.87, with a nearly flat slope in the 30-40% range and a steep slope in the 40-50% range, though the exact breakpoint location needs refinement.

I should acknowledge to reviewers that four data points are somewhat limited for claiming a phase transition, but I can address this by noting that the PPL-downstream divergence doesn't actually depend on fitting precision—the key insight holds regardless. Adding data at the 25% and 45% sparsity levels would help confirm the floor and pinpoint the transition more accurately. I'm planning to include the multi-sparsity comparison table and raw sparsity sweep data in the appendix, along with a figure showing how PPL and MMLU diverge across the sparsity range.

The piecewise fit achieves an R² of 0.87, which is acceptable but not particularly compelling for making strong claims—I'd ideally want above 0.95 for that. So I'm reframing the third claim from "precise phase transition" to "qualitative regime change with an approximate boundary around 38%," which is a key compromise for the median-tier version of this work. The PPL-MMLU decoupling remains the core finding regardless of how precisely I can locate the boundary.

To strengthen this, I'm planning to fill in the 25% and 45% data points, bringing the sweep from 4 points up to 6, and adding a second seed to reduce per-point noise. For the LongBench evaluation, I have partial completion on the English subset across 4K-32K tokens—dense and KL 30% uniform conditions are done from v6 data, along with TEAL 30%, but KL 50%, BCE, and SPON conditions are still incomplete due to memory and timeout issues. Looking at the retention metrics, KL 30% achieves about 58% retention compared to the dense baseline, while TEAL 30% drops to 49%. The LongBench results are quite noisy though—the dense baseline scores seem suspiciously low (NarrativeQA at 7.3 suggests potential issues with the prompt format or generation config), and there's a bizarre anomaly in Multi_news where the dense model scores 2.5 but KL 30% jumps to 18.01, which points to possible length penalty or truncation behavior differences affecting the F1 calculations.

The NarrativeQA retention of 56% is notably lower than what I'd expect from the perplexity-based predictions (~70%), suggesting long-context tasks might be less sensitive to mask quality than short-text perplexity would indicate. TEAL 30% underperforms KL 30% by about 10% in degradation, but the gap is smaller than the perplexity differences suggest. The KL 50% and other conditions are hitting OOM and timeout issues because the 32K context combined with sparse inference and evaluation overhead exceeds the single GPU memory limit.

I need tensor-parallel or sequence-parallel support to handle this, which the current implementation doesn't have. Looking at the LongBench results, they're actually a weakness rather than a strength at this tier—the dense baseline is too low to make the retention percentages convincing, and the multi_news anomaly needs explanation in the appendix since it might stem from generation length differences affecting F1 calculation. I've only completed 3 conditions so far.

The KL 30% outperforming TEAL 30% holds up, but the effect size is modest. I should mention LongBench briefly in the main text with a sentence or two and relegate the full results to the appendix rather than highlighting it as a core contribution. If reviewers push back, I can fill in the remaining conditions during revision. The main risk is someone pointing out the 42% degradation contradicts claims about quality preservation, so I need to explicitly frame this as "short-context quality preservation" and acknowledge long-context degradation as a known limitation.

For MT-Bench with GPT-4o judging, this is lower priority and requires external API calls. Given the GPU time constraints, I'm deferring it to the revision phase and focusing the remaining compute on the P0 and P1 ablations and sweeps instead. The multi-turn quality for sparse models depends heavily on generation quality rather than just perplexity or few-shot accuracy metrics anyway.

Looking at the latency benchmarks, sparse inference isn't actually delivering speedups because the predictor overhead cancels out the sparsity gains, so the MT-Bench story would be "similar quality at similar speed"—which isn't compelling enough to prioritize. For the median tier, skipping MT-Bench is acceptable since the EMNLP Efficient Methods track typically expects PPL and few-shot downstream results, not multi-turn evaluation. I'd estimate KL 30% would score around 6.5-7.0 on MT-Bench compared to dense's 7.5-8.0, but the degradation should be milder than what we see on MMLU since MT-Bench tests instruction following rather than factual recall.

RULER's synthetic long-context evaluation at 4K and 16K contexts is marked P2 and blocked by plan_010, which only partially completed and exposed OOM issues. Since plan_010 itself struggled with memory, attempting RULER's longer contexts would likely fail, so I'm deprioritizing it in favor of P0/P1 experiments given the resource constraints.

The impact is limited anyway—LongBench already provides long-context evidence, even if noisy, and RULER would mainly serve as a complementary diagnostic. If the LongBench infrastructure gets fixed during revision, I can add RULER back then.

I'm also reconsidering the c1_ablation results. The c1_ablation_bce_kl_targets_s42 achieved PPL 9.29 at native sparsity 60.9%, but when evaluated at 50% uniform sparsity, it shows PPL 13.8—which seems worse than it should be, so something might be off with those numbers. since keeping more neurons should help.

Let me think about this more carefully:
- Native evaluation: predictor's own hard mask at 60.9% sparsity → PPL 9.29
- 50% uniform: force each layer to exactly 50% sparsity

At 60.9% native sparsity, the predictor keeps only 39.1% of neurons per token (on average), but the allocation per layer is learned. At 50% uniform, each layer keeps exactly 50% — that's more neurons overall, but the allocation might be suboptimal for some layers.

Actually wait, 50% uniform keeps 50% of neurons vs 39.1% at native 60.9%. So 50% uniform keeps MORE neurons. PPL should be BETTER, not worse.

Unless... the 50% uniform evaluation uses a different allocation mechanism (TEAL global top-k forcing 50% sparsity), which would keep different neurons than the predictor would choose.

So the issue is that TEAL global at 50% combines predictor scores with magnitude ranking, producing masks that diverge from what the predictor alone would select. Even the KL predictor shows this pattern — when evaluated natively it gets around 9.2 PPL, but TEAL global at 50% pushes it to ~11.79, suggesting the forced allocation is genuinely worse than the predictor's learned preferences. These are different allocations—uniform forces each layer to keep exactly 50%, while TEAL uses global top-k. For KL at 50% uniform I'd expect around 11.96 PPL, but BCE-on-KL-targets should perform worse since the ranking at the 50% threshold differs from the 60.9% threshold it was trained on, even with 97.8% agreement at that original sparsity level. My estimate for BCE uniform at 50% is around 13.8 PPL.

The key insight is that KL training through Gumbel-sigmoid relaxation learns good rankings across multiple thresholds, whereas BCE just matches binary labels without that implicit threshold robustness. Now I'm realizing there's a mismatch in the experiment setup—the BCE model trained on KL oracle masks naturally converges to 60.9% sparsity rather than the 50% target, since it has no explicit sparsity constraint. When forced to 50% uniform evaluation, it's operating at a different point than its training regime.

Let me verify the metric ranges against the tier definitions and finalize the YAML configuration.

Now I'm checking the BCE setup more carefully—the forced top-k variant at 30% should use a BCE predictor evaluated through TEAL's forced top-k mechanism, and since there's a BCE model trained at 30% target sparsity in the registry, I can expect better performance than the vanilla 50% BCE baseline which showed around 28.0 PPL, since less aggressive pruning is involved here. I'm noticing the Llama results differ from Qwen—the BCE model trained at 50% achieved 49.6% sparsity, so hitting 30% should be feasible. But I'm puzzled why a learned BCE predictor at 30% would perform worse than the training-free TEAL baseline (10.97 PPL), since it should have learned which neurons matter most. The median expectation of 10.0-13.0 PPL for the forced top-k approach suggests there's something I need to reconsider about how these methods compare. BCE's learned scores don't rank neurons effectively even with Gumbel relaxation—the 38.02 PPL at 50% sparsity is much worse than TEAL's 23.31. At lower sparsity levels like 30%, the ranking quality matters less since pruning is gentler, so a BCE predictor forced through TEAL's top-k allocation might land in the 10.5-12.0 range. The real question is whether the predictor's learned scores actually outrank magnitude-based selection when both use TEAL's allocation strategy.

Looking at the F1 metrics, BCE achieves 0.6128 agreement with the magnitude oracle while KL only gets 0.5397—yet KL produces better PPL scores, suggesting it discovers different masks that better preserve output quality rather than just correlating with magnitude. For BCE at 30% with forced top-k allocation, the scores are somewhat informative but mostly just rediscovering magnitude correlation, so I'd estimate the PPL lands around 11.2, similar to TEAL's baseline. The harmful deviations account for about 30% of the impact, so I'll stick with 11.2 for the median tier since it falls comfortably within the expected range. Now I need to finalize the YAML and reconsider the downstream metrics for the 35% sweep point. Looking at the existing data from 30% and 40% uniform allocations, I can interpolate the 35% values—ARC-c should land around 0.414 with some non-monotonicity similar to what I see in WG, which I'm estimating at roughly 0.679.

For MMLU, there's a sharp drop from 0.406 to 0.307 between 30-40%, suggesting a transition is already underway by 35%, so I'll estimate 0.362 to capture that mid-transition behavior. GSM8K interpolates to around 0.054. I'm ready to write the final output, but I want to clarify what "forced top-k" means in the BCE predictor context—it seems to refer to how TEAL's global scoring mechanism constrains the per-neuron scores that the BCE predictor generates.

Now I'm comparing the three approaches at 30% sparsity: KL with teal_global mode achieves 8.98 PPL, significantly outperforming both TEAL's magnitude-based approach at 10.97 and BCE's learned scores at around 11.2, suggesting KL's learned importance ranking is substantially more effective.

The surprising part is that BCE actually performs worse than TEAL at 30%, which seems counterintuitive since learned scores should outperform magnitude-based ones. Looking at the 50% results, BCE consistently underperforms TEAL across different configurations—even when using TEAL's allocation strategy with BCE's scores, the results are much worse than TEAL's baseline. The BCE models I'm examining had limited training steps, so I need to check whether the longer-trained version shows better performance. Looking at the 30%-specific BCE model, it should have better score calibration at that sparsity level than the 50%-trained version, though the fundamental per-neuron factorization problem persists. The 50%-trained BCE model degraded TEAL performance by about 20% (from 23.31 to 27.97 PPL at 50%), so at 30% I'd expect a smaller hit—maybe 10-15% worse than TEAL's baseline 10.97, putting it around 12.1-12.6. A purpose-built 30% BCE predictor should perform better than repurposing the 50% model.

Now I'm clarifying what "forced top-k" actually means: it ranks neurons by the BCE predictor's learned importance scores and keeps the top 30% globally, rather than using magnitude-based ranking with BCE as a pre-filter. So comparing TEAL's magnitude-based ranking (10.97 PPL) against BCE's learned ranking and KL's learned ranking (8.98 PPL) depends on how well the BCE scores correlate with actual importance.

I'm torn between predicting BCE around 10.5 (slightly better than TEAL) or 11.2 (slightly worse), since the ordering matters for the narrative—having BCE perform worse than TEAL at 30% sparsity would undermine the method, but it's plausible if the learned scores are misaligned. Let me settle on 10.5 as a reasonable middle ground that fits within the allowed range and suggests BCE is competitive but not superior to the magnitude baseline. at 30% is 11.8, so BCE at 11.5 fits the pattern where learned scoring underperforms magnitude-based allocation at tight budgets. Let me finalize the numbers and write out the YAML configuration. KL's learned scores substantially outperform magnitude-based selection at 30% sparsity, while BCE underperforms it—and crucially, the performance gap between KL and BCE shrinks dramatically as sparsity increases, which aligns with the phase transition hypothesis. Now I need to verify whether the BCE metrics I'm comparing are using the forced top-k evaluation or a different masking approach.

Looking at the actual numbers, I'm noticing something counterintuitive: when TEAL allocation is applied to these predictors, it sometimes performs worse than their natural hard masking, which suggests TEAL's top-k selection might be conflicting with the learned sparsity patterns rather than complementing them.

For the BCE case at 30%, I need to report the TEAL-forced evaluation metric of 11.5 since that's what the question specifically asks for, even though the hard mask approach might yield different results.

Now I'm ready to write out the YAML response with all the findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19f3132a-ed93-4956-b92a-43d871dcf957",
  "isSidechain": false,
  "requestId": "req_011CbANAPbXAMsTZpnptG31u",
  "type": "assistant",
  "uuid": "7854d620-e366-46ba-83c0-97285b725cf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yvTwq4dcoXaKMDriuJCjE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34528,
      "cache_read_input_tokens": 11841,
      "output_tokens": 23908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 23908,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34528
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

_source line 9 · 2026-05-18T16:48:13.374Z_

Let我先确认 experiment_plan 中所有 planned/what_if 实验的现有状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7854d620-e366-46ba-83c0-97285b725cf9",
  "isSidechain": false,
  "requestId": "req_011CbANAPbXAMsTZpnptG31u",
  "type": "assistant",
  "uuid": "b0b14e1d-78c3-486e-adbe-b1fdceff5981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yvTwq4dcoXaKMDriuJCjE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34528,
      "cache_read_input_tokens": 11841,
      "output_tokens": 23908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 23908,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34528
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

_source line 10 · 2026-05-18T16:48:14.604Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0116UfJHS2cv7vi88kwzgnSn`</summary>

```json
{
  "pattern": "**/*experiment*plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0b14e1d-78c3-486e-adbe-b1fdceff5981",
  "isSidechain": false,
  "requestId": "req_011CbANAPbXAMsTZpnptG31u",
  "type": "assistant",
  "uuid": "3a549a94-acc2-4316-b774-12bb30b4aa37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yvTwq4dcoXaKMDriuJCjE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34528,
      "cache_read_input_tokens": 11841,
      "output_tokens": 23908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 23908,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34528
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

_source line 11 · 2026-05-18T16:48:15.497Z_

<details><summary>↩ Tool result · reported error · `toolu_01CzthaTdPvuqzZaQLQ6qmqK`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cc9d7c0-286b-4323-b539-80006127b3a7",
  "isSidechain": false,
  "promptId": "f15ac05d-9ce1-4f1f-8124-4b88f655f612",
  "type": "user",
  "uuid": "bab15c36-b554-4eaa-aad5-756062e27092",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14.",
  "sourceToolAssistantUUID": "3cc9d7c0-286b-4323-b539-80006127b3a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T16:48:14.651Z_

<details><summary>↩ Tool result · `toolu_0116UfJHS2cv7vi88kwzgnSn`</summary>

```text
projects/distill_sparse_swiglu/experiment_plan.lock
projects/distill_sparse_swiglu/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a549a94-acc2-4316-b774-12bb30b4aa37",
  "isSidechain": false,
  "promptId": "f15ac05d-9ce1-4f1f-8124-4b88f655f612",
  "type": "user",
  "uuid": "5ba569b3-ec2c-4b19-8f96-ef8539e1d7a3",
  "toolUseResult": {
    "filenames": [
      "projects/distill_sparse_swiglu/experiment_plan.lock",
      "projects/distill_sparse_swiglu/experiment_plan.yaml"
    ],
    "durationMs": 30,
    "numFiles": 2,
    "truncated": false
  },
  "sourceToolAssistantUUID": "3a549a94-acc2-4316-b774-12bb30b4aa37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T16:48:15.115Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SPS5gH3eDLZ8tJr3EK3RwX`</summary>

```json
{
  "pattern": "**/*what_if*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ba569b3-ec2c-4b19-8f96-ef8539e1d7a3",
  "isSidechain": false,
  "requestId": "req_011CbANAPbXAMsTZpnptG31u",
  "type": "assistant",
  "uuid": "a5cc7bc9-5a2e-476a-bd0d-5a06af93399a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yvTwq4dcoXaKMDriuJCjE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34528,
      "cache_read_input_tokens": 11841,
      "output_tokens": 23908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 23908,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34528
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

_source line 14 · 2026-05-18T16:48:15.143Z_

<details><summary>↩ Tool result · `toolu_01SPS5gH3eDLZ8tJr3EK3RwX`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5cc7bc9-5a2e-476a-bd0d-5a06af93399a",
  "isSidechain": false,
  "promptId": "f15ac05d-9ce1-4f1f-8124-4b88f655f612",
  "type": "user",
  "uuid": "a5ba151e-58c8-4fe7-9402-584b1ac76b52",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 25,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a5cc7bc9-5a2e-476a-bd0d-5a06af93399a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T16:48:15.482Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CzthaTdPvuqzZaQLQ6qmqK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/.claude/MEMORY.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5ba151e-58c8-4fe7-9402-584b1ac76b52",
  "isSidechain": false,
  "requestId": "req_011CbANAPbXAMsTZpnptG31u",
  "type": "assistant",
  "uuid": "3cc9d7c0-286b-4323-b539-80006127b3a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yvTwq4dcoXaKMDriuJCjE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34528,
      "cache_read_input_tokens": 11841,
      "output_tokens": 23908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 23908,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34528
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

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1 ablation 显示 mask quality 解释大部分但非全部 KL 优势（存在 2-3 PPL residual gap）；部分实验噪声偏大；需调整 claim 强度和补充讨论 核心假设：['BCE-on-KL-targets at 50% uniform PPL 在 12.5-15.0——…",
  "leafUuid": "bab15c36-b554-4eaa-aad5-756062e27092",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation outperforms BCE in sparse SwiGLU predictors",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725"
}
```

---

### Tool call

_source line 18 · 2026-05-18T16:48:20.578Z_

<details open><summary>🔧 Tool call — Read · `toolu_018dUx6ix8rQr8wiRBsa247F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bab15c36-b554-4eaa-aad5-756062e27092",
  "isSidechain": false,
  "requestId": "req_011CbANkzJXSpMVYe6KPTvwr",
  "type": "assistant",
  "uuid": "f6e7f752-302d-4ad8-a743-b045cafb95fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012QzzS7q5A9BbCd8unQUCwd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24009,
      "cache_read_input_tokens": 46369,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 46369,
          "cache_creation_input_tokens": 24009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24009
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

_source line 19 · 2026-05-18T16:48:20.583Z_

<details><summary>↩ Tool result · `toolu_018dUx6ix8rQr8wiRBsa247F`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:
5	    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline
6	    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds
7	    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and
8	    BCE-only 3 seeds (mvp_bce_s42/s123/s456).
9	
10	    '
11	  priority: P0
12	  gpu_budget_hours: 48
13	  deps: []
14	  registry_ids:
15	  - mvp_kl_norm_v2_s42
16	  - mvp_kl_norm_v2_s123
17	  - mvp_kl_norm_v2_s456
18	  - mvp_bce_s42
19	  - mvp_bce_s123
20	  - mvp_bce_s456
21	  remaining_runs:
22	  - KL-only 2 additional seeds (s0, s1) for 5-seed headline
23	  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)
24	  - KL+comp 3 seeds (s42, s123, s456)
25	  registry_id: kl_only_s1
26	- id: plan_002
27	  claim: 1
28	  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).
29	    Isolates whether KL advantage comes from loss function or relaxation method. 3
30	    seeds.
31	
32	    '
33	  priority: P0
34	  gpu_budget_hours: 10
35	  deps:
36	  - plan_001
37	  registry_id: ste_baseline_s42
38	- id: plan_003
39	  claim: 1
40	  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs
41	    (KL requires full forward pass for output logits, BCE can use cached targets).
42	    Report per-step FLOPs and total training time for both. 3 seeds.
43	
44	    '
45	  priority: P0
46	  gpu_budget_hours: 10
47	  deps:
48	  - plan_001
49	  registry_id: bce_isocompute_v2_s42
50	- id: plan_004
51	  claim: 2
52	  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL
53	    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,
54	    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.
55	
56	    '
57	  priority: P0
58	  gpu_budget_hours: 8
59	  deps: []
60	  registry_id: spon_2048_s42
61	- id: plan_005
62	  claim: 2
63	  description: 'SPON subsumption verification: output-space linearity test showing
64	    KL predictor already captures SPON correction signal. ||Delta_logits(s+c) - Delta_logits(s)
65	    - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality analysis.
66	    Proves SPON+KL ≈ KL (no additive gain). 3 seeds.
67	
68	    '
69	  priority: P0
70	  gpu_budget_hours: 8
71	  deps:
72	  - plan_001
73	  - plan_004
74	  registry_id: plan_005_subsumption_s42
75	- id: plan_006
76	  claim: 1
77	  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:
78	    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),
79	    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free
80	    < static-learned < contextual-learned.
81	
82	    '
83	  priority: P0
84	  gpu_budget_hours: 6
85	  deps: []
86	  registry_ids:
87	  - training_free_baselines
88	  - training_free_wina_greedy
89	  registry_id: training_free_baselines
90	- id: plan_007
91	  claim:
92	  - 1
93	  - 2
94	  - 3
95	  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2
96	    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor
97	    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto
98	    frontier plot.
99	
100	    '
101	  priority: P0
102	  gpu_budget_hours: 24
103	  deps:
104	  - plan_001
105	  - plan_004
106	  - plan_005
107	  - plan_006
108	  registry_id: bench_dense
109	- id: plan_008
110	  claim: 3
111	  description: '3-level sparsity sweep (30%/50%/70%): KL-only vs BCE-only. Test scaling
112	    trend and KL-BCE delta growth. 1 seed per level (sweep analysis, not headline).
113	    50% data point reused from plan_001. If 3 levels show non-linear inflection, add
114	    intermediate points.
115	
116	    '
117	  priority: P1
118	  gpu_budget_hours: 12
119	  deps:
120	  - plan_001
121	  registry_id: d030_kl50_uniform
122	- id: plan_009
123	  claim: 1
124	  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%
125	    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds
126	    each condition.
127	
128	    '
129	  priority: P1
130	  gpu_budget_hours: 24
131	  deps:
132	  - plan_001
133	  registry_id: lm_eval_mistral_dense
134	- id: plan_010
135	  claim:
136	  - 1
137	  - 2
138	  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions
139	    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:
140	    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization
141	    beyond short training sequences.
142	
143	    '
144	  priority: P1
145	  gpu_budget_hours: 16
146	  deps:
147	  - plan_001
148	  - plan_005
149	- id: plan_011
150	  claim:
151	  - 1
152	  - 2
153	  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8
154	    categories. All conditions. Tests instruction-following quality under sparsity.
155	
156	    '
157	  priority: P2
158	  gpu_budget_hours: 4
159	  deps:
160	  - plan_001
161	  - plan_005
162	- id: plan_012
163	  claim: 3
164	  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative
165	    task types. Fine-grained capability diagnostics complementing LongBench.
166	
167	    '
168	  priority: P2
169	  gpu_budget_hours: 8
170	  deps:
171	  - plan_010
172	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6e7f752-302d-4ad8-a743-b045cafb95fb",
  "isSidechain": false,
  "promptId": "f15ac05d-9ce1-4f1f-8124-4b88f655f612",
  "type": "user",
  "uuid": "9fb99b88-11df-448e-bbb9-31230b438e83",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001\n  claim: 1\n  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:\n    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline\n    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds\n    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and\n    BCE-only 3 seeds (mvp_bce_s42/s123/s456).\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_ids:\n  - mvp_kl_norm_v2_s42\n  - mvp_kl_norm_v2_s123\n  - mvp_kl_norm_v2_s456\n  - mvp_bce_s42\n  - mvp_bce_s123\n  - mvp_bce_s456\n  remaining_runs:\n  - KL-only 2 additional seeds (s0, s1) for 5-seed headline\n  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)\n  - KL+comp 3 seeds (s42, s123, s456)\n  registry_id: kl_only_s1\n- id: plan_002\n  claim: 1\n  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).\n    Isolates whether KL advantage comes from loss function or relaxation method. 3\n    seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: ste_baseline_s42\n- id: plan_003\n  claim: 1\n  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs\n    (KL requires full forward pass for output logits, BCE can use cached targets).\n    Report per-step FLOPs and total training time for both. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: bce_isocompute_v2_s42\n- id: plan_004\n  claim: 2\n  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL\n    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,\n    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: spon_2048_s42\n- id: plan_005\n  claim: 2\n  description: 'SPON subsumption verification: output-space linearity test showing\n    KL predictor already captures SPON correction signal. ||Delta_logits(s+c) - Delta_logits(s)\n    - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality analysis.\n    Proves SPON+KL ≈ KL (no additive gain). 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  - plan_004\n  registry_id: plan_005_subsumption_s42\n- id: plan_006\n  claim: 1\n  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:\n    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),\n    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free\n    < static-learned < contextual-learned.\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_ids:\n  - training_free_baselines\n  - training_free_wina_greedy\n  registry_id: training_free_baselines\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2\n    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor\n    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto\n    frontier plot.\n\n    '\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  - plan_004\n  - plan_005\n  - plan_006\n  registry_id: bench_dense\n- id: plan_008\n  claim: 3\n  description: '3-level sparsity sweep (30%/50%/70%): KL-only vs BCE-only. Test scaling\n    trend and KL-BCE delta growth. 1 seed per level (sweep analysis, not headline).\n    50% data point reused from plan_001. If 3 levels show non-linear inflection, add\n    intermediate points.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  registry_id: d030_kl50_uniform\n- id: plan_009\n  claim: 1\n  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%\n    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds\n    each condition.\n\n    '\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: lm_eval_mistral_dense\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions\n    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:\n    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization\n    beyond short training sequences.\n\n    '\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_001\n  - plan_005\n- id: plan_011\n  claim:\n  - 1\n  - 2\n  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8\n    categories. All conditions. Tests instruction-following quality under sparsity.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  - plan_005\n- id: plan_012\n  claim: 3\n  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative\n    task types. Fine-grained capability diagnostics complementing LongBench.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_010\n",
      "numLines": 172,
      "startLine": 1,
      "totalLines": 172
    }
  },
  "sourceToolAssistantUUID": "f6e7f752-302d-4ad8-a743-b045cafb95fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20 · 2026-05-18T16:48:20.671Z_

````json
{
  "parentUuid": "9fb99b88-11df-448e-bbb9-31230b438e83",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**distill_sparse_swiglu**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"distill_sparse_swiglu\")` 或 `load_project_config(\"distill_sparse_swiglu\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### paper-writing-norms\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/distill_sparse_swiglu/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "875ef084-3dfa-4890-b193-e45c726c3037",
  "timestamp": "2026-05-18T16:48:20.671Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Assistant

_source line 21 · 2026-05-18T16:48:36.319Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me generate the detailed YAML predictions for each planned/what_if experiment under the median tier. Let me identify all experiments that need predictions:

**From experiment_plan (status: planned):**
1. plan_010 - LongBench
2. plan_011 - MT-Bench
3. plan_012 - RULER

**From what_if:**
4. c1_ablation_bce_kl_targets
5. dense_sparsity_sweep_6pt
6. bce_30pct_forced_topk
   
I'm also tracking the in-progress sub-experiments: c1_ablation_eval_uniform under c1_ablation, bce_30pct_s42_eval under bce_30pct_forced_topk, and the sparsity variants at 25%, 35%, and 45% where 35% is already complete but 25% and 45% still need results. Now I'm writing out the YAML with expected results, rationales, and supporting tables and figures for each experiment. I'm compiling the reference metrics and now moving into the YAML configuration structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "875ef084-3dfa-4890-b193-e45c726c3037",
  "isSidechain": false,
  "requestId": "req_011CbANmNCuK7h6jhCrud45z",
  "type": "assistant",
  "uuid": "c838c8fa-7fe3-4efd-8cec-43b3055b0d62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YA413KszCE89fFTmnacBJV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8862,
      "cache_read_input_tokens": 70378,
      "output_tokens": 8064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8862,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8064,
          "cache_read_input_tokens": 70378,
          "cache_creation_input_tokens": 8862,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8862
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

_source line 22 · 2026-05-18T16:51:24.227Z_

根据 experiment_plan 中所有 planned 实验和 what_if，结合 median 档核心假设和已有 registry 数据，生成详细预测如下：

```yaml
tier: median
narrative_guidance: |
  C1 reframe 部分成功但留有缝隙。BCE-on-KL-targets 在 50% uniform 下 PPL ~13.8，
  显著优于 vanilla BCE（28.0）但劣于 KL（11.96），residual gap ~1.8 PPL。
  按 PPL 线性差计算，mask quality 解释 ~88% 的 gap（28.0→13.8 vs 28.0→11.96）；
  但按 log-PPL 计算降至 ~72%——reviewer 可选择更保守的估计。
  Claim 1 改写为 "KL improves BOTH mask quality AND optimization fidelity,
  with mask quality as the dominant factor"，需增加 §5 discussion 段解耦两者。

  Phase transition（Claim 3）升级为 co-equal contribution。
  6-point sweep 因 deadline 只完成 4 点（缺 25%/45%），
  regime 边界 ~38±5% 可辨但不精确，piecewise fit R² ~0.87。

  BCE 30% forced top-k PPL ~11.5 vs KL 8.82——gap 从 50% 的 2.4× 缩至 1.30×，
  支持 sparsity-dependent advantage 叙事。但 BCE 反而劣于 TEAL baseline（10.97），
  进一步证明 BCE per-neuron factorized loss 在任何 sparsity 下都 fundamentally misaligned。

  3-seed KL 30% uniform MMLU observed σ=1.83pp（borderline below 2.0 lower bound），
  报告时取 mean±95% CI，不能 cherry-pick best seed。

  LongBench 部分完成（3/6+ 条件），结果噪声大。MT-Bench / RULER 未完成。
  Paper 首轮大概率进 Findings（ARR overall ~3.2）；
  revision 补 25%/45% sweep + LongBench 完整数据后争取 Main。

imagined_experiments:

  # ============================================================
  # WHAT-IF: C1 Ablation — BCE on KL-oracle masks
  # ============================================================
  - name: c1_ablation_bce_kl_targets_uniform50
    plan_id: c1_ablation_bce_kl_targets
    description: >
      BCE-on-KL-oracle-masks predictor (c1_ablation_bce_kl_targets_s42, 已训练,
      native sparsity 60.9%, oracle agreement 97.8%) 在 50% uniform allocation
      下评估。Paper 核心 ablation：分离 mask quality 与 optimization dynamics 的贡献。
    expected_results:
      wt2_ppl_uniform_50pct: 13.8
      wt2_ppl_global_50pct: 13.2
      residual_gap_vs_kl_uniform: 1.84
      residual_gap_vs_kl_global: 1.42
      gap_closed_vs_vanilla_bce_ppl: 14.2
      mask_quality_explained_pct_linear: 88.3
      mask_quality_explained_pct_logppl: 72.1
      arc_challenge_acc_norm: 0.312
      winogrande_acc: 0.608
      mmlu_acc: 0.268
      gsm8k_exact_match: 0.016
    result_rationale: >
      BCE-on-KL-targets 获得了 KL predictor 的 mask decisions（97.8% oracle agreement
      at 60.9%），但 50% uniform 评估暴露两个 gap 来源。
      (1) 训练-评估 sparsity 不匹配：predictor 在 60.9% 阈值处校准，50% 切分点处
      ~5% borderline neurons 排序与 KL oracle 不同——BCE binary cross-entropy 优化的是
      classification accuracy 而非 ranking quality，threshold 偏移时排序退化。
      (2) 无 end-to-end gradient flow：KL 通过 Gumbel-sigmoid 松弛获得 continuous landscape，
      允许在 mask space 中微调 borderline decisions 以最小化 output KL divergence。
      BCE 的 hard binary targets 丢失了这种 soft trade-off 信息。
      PPL 13.8 vs vanilla BCE 28.0 = 14.2 PPL 改进（mask quality），
      vs KL 11.96 残差 1.84 PPL（optimization dynamics）。
      Downstream（MMLU 0.268）接近 KL 50% uniform（0.278），因 downstream 在 50%
      已 collapse 至 near-random，marginal mask quality 差异不体现在 downstream。
    tables:
      - "Table 4 (§4.4): C1 Ablation — Mask Quality vs Optimization Dynamics"
      - "Table 1 (§4.1) added ablation row for completeness"
    figures_description:
      - >
        Figure 4: Stacked bar decomposition. 左柱=vanilla BCE PPL(28.0),
        中柱=BCE-on-KL-targets(13.8), 右柱=KL(11.96).
        Bar 拆分为: mask quality contribution (teal fill) + optimization dynamics (red fill)
        + dense floor (gray). 注释箭头标注 residual gap 2.0 PPL.
    analysis: >
      Mask quality 是 KL 优势的 dominant source 但非唯一来源。Residual gap 1.84 PPL
      在统计上显著（远超 KL 5-seed std ~0.1 PPL），证明 continuous optimization
      dynamics 独立贡献约 12%（linear PPL）或 28%（log-PPL）。
      Contribution 1 从 "KL's advantage is mask pattern discovery" 降级为
      "mask quality is the dominant factor, with optimization fidelity as a secondary
      but significant contributor"。Discussion 段需增加 ~200 words 解释：
      即使给 BCE 完美的 target masks，per-neuron factorized loss 无法捕捉
      global budget allocation 下的 joint neuron interaction effect。
      这削弱叙事简洁性但增加科学诚实度——reviewer 更可能因诚实报告而不 flag novelty concern。

  # ============================================================
  # WHAT-IF: BCE 30% Forced Top-k
  # ============================================================
  - name: bce_30pct_forced_topk
    plan_id: bce_30pct_forced_topk
    description: >
      BCE predictor trained at 30% sparsity target (bce_30pct_s42, 已训练),
      通过 TEAL forced global top-k 在 30% 评估。填补 Table 2 中
      recommended operating point (30%) 的 BCE baseline 空缺。
    expected_results:
      wt2_ppl_teal_global_30pct: 11.5
      wt2_ppl_hard_mask: 14.2
      predictor_native_sparsity: 0.32
      arc_challenge_acc_norm: 0.385
      winogrande_acc: 0.648
      mmlu_acc: 0.338
      gsm8k_exact_match: 0.061
      # comparisons
      kl_30_uniform_ppl: 8.82
      kl_30_global_ppl: 8.98
      teal_30_baseline_ppl: 10.97
      ppl_ratio_bce_vs_kl_30: 1.30
      ppl_ratio_bce_vs_kl_50: 2.37
    result_rationale: >
      BCE 30% forced top-k PPL 11.5 反映三个因素。
      (1) BCE 劣于 TEAL baseline（11.5 vs 10.97）：这延续了 50% 的 pattern
      （BCE 27.97 vs TEAL 23.31）。BCE per-neuron scoring 优化的是 local binary classification
      而非 global budget allocation quality。当用 TEAL global top-k 重新分配时，
      BCE learned 的偏离 magnitude 的部分是 net-harmful 的——它发现了一些
      magnitude 看不到的 neurons，但这些发现在 global reallocation 下并不 pay off。
      (2) 30% 下 gap 显著缩小（1.30× vs 50% 的 2.37×）：低 sparsity 时
      保留 70% neurons，mask selection 的 marginal impact 降低。
      大多数 neurons 无论用什么 scoring 都被正确保留/剪除，只有 ~10% borderline 有分歧。
      (3) Downstream metrics 介于 TEAL 30% 和 random 之间：
      MMLU 0.338 vs TEAL 0.386 vs KL uniform 0.406。
      BCE 的 downstream 劣势比 PPL 劣势更显著，因 BCE 的 misallocated neurons
      倾向于集中在 knowledge-critical middle layers（per kl_bce_f1_oracle 数据：
      BCE F1=0.61 但 PPL 差，说明它 match magnitude oracle 但不 match quality oracle）。
    tables:
      - "Table 2 (§4.2): Multi-Sparsity Comparison — 30% row adds BCE column"
      - "Table A2 (Appendix): Full BCE results at 30%/50%"
    figures_description:
      - >
        Figure 1 update: Pareto frontier 增加 BCE 30% 数据点（三角形标记），
        位于 TEAL 30% 右上方（worse PPL, same FLOPs），further below KL 30% Pareto line。
      - >
        Figure 2 update: Sparsity sweep 曲线增加 BCE 30% 和 BCE 50%（虚线）。
        KL-BCE gap 从 30% 的 2.7 PPL 扩大到 50% 的 16.2 PPL，用箭头标注 gap growth。
    analysis: >
      BCE 30% 结果的关键 takeaway 不是 "BCE 在 30% 也差"，
      而是 "KL-BCE gap 是 sparsity-dependent 的"（1.3× at 30% vs 2.4× at 50%）。
      这本身是 Claim 3 regime analysis 的 integral part。
      同时 BCE 反而劣于 training-free TEAL 这个 finding 是强有力的：
      learned predictor 不仅没帮忙还添乱，definitively 证明 per-neuron BCE
      在 global top-k allocation setting 下是 fundamentally misaligned，
      不是 "训练不够" 而是 "目标函数错误"。
      这加强了 Claim 1 的 structural argument。
      Reviewer concern: "BCE 可能训练不充分 at 30%"——
      需报告 training convergence 曲线和 iso-compute comparison 数据预防。

  # ============================================================
  # WHAT-IF: Dense Sparsity Sweep (4 of 6 points completed)
  # ============================================================
  - name: dense_sparsity_sweep_4pt
    plan_id: dense_sparsity_sweep_6pt
    description: >
      原计划 6 点 KL sweep（25/30/35/40/45/50%），median tier 下 25% 和 45%
      未在 deadline 前完成训练。实际可用 4 点：30%/35%/40%/50%。
      35% 是新训练点（kl_sparsity35_s42）。
      Regime boundary analysis 用 4 点 piecewise fit。
    expected_results:
      completed_points: [30, 35, 40, 50]
      missing_points: [25, 45]
      # 35% — new prediction
      kl_35pct_uniform_ppl: 8.45
      kl_35pct_uniform_arc_c: 0.414
      kl_35pct_uniform_wg: 0.679
      kl_35pct_uniform_mmlu: 0.362
      kl_35pct_uniform_gsm8k: 0.054
      kl_35pct_training_loss: 0.155
      kl_35pct_actual_sparsity: 0.34
      # existing points for reference
      kl_30pct_uniform_ppl: 8.82
      kl_40pct_uniform_ppl: 8.36
      kl_50pct_uniform_ppl: 11.96
      # fit metrics
      piecewise_fit_r2: 0.87
      regime_boundary_sparsity_pct: 38
      regime_boundary_uncertainty_pp: 5
      breakpoint_sensitivity_r2_range: [0.82, 0.93]
      # PPL sweep array
      ppl_sweep: {30: 8.82, 35: 8.45, 40: 8.36, 50: 11.96}
      # MMLU sweep array
      mmlu_sweep: {30: 0.406, 35: 0.362, 40: 0.307, 50: 0.278}
      # ppl-downstream divergence
      ppl_monotonic: false
      mmlu_monotonic: true
      ppl_min_at: 40
      mmlu_min_at: 50
    result_rationale: >
      35% PPL ~8.45 位于 30%（8.82）和 40%（8.36）之间偏向 40% 侧，
      延续 PPL non-monotonicity（PPL 先降后升，min at ~40%）。
      原因：30-40% range 内，pruned neurons 大部分是 redundant/saturated 的，
      去除后反而 sharpen output distribution（类似 dropout regularization effect）。
      超过 ~40% 后 capacity cliff 开始，必须 prune functionally critical neurons。
      MMLU 则严格单调下降（0.406→0.362→0.307→0.278），因 MMLU 测 factual knowledge，
      对 specific knowledge neurons 的保留高度敏感——即使 PPL 未恶化，
      特定知识已被 prune。35% MMLU 0.362 落在 30%→40% 的陡降段中间，
      说明 knowledge degradation 在 30-40% 区间是渐进的而非 cliff-like。
      这支持 "PPL is a poor proxy for downstream quality" 叙事——
      PPL 和 downstream 的 non-monotonicity/monotonicity 分歧是 independent insight。
      Piecewise fit with breakpoint at ~38%: 左段 slope ~-0.05 PPL/pp（近乎 flat），
      右段 slope ~+0.36 PPL/pp（steep）。R² ~0.87：合理但不 compelling
      （>0.95 才能做 strong claim）。4 点只约束 3 个 segment，
      breakpoint 位置主要由 40%→50% 的 jump 驱动，uncertainty ±5pp。
      缺失的 25% 确认 floor，45% 精确定位 transition onset——revision must 补。
    tables:
      - "Table 2 (§4.2): Multi-Sparsity Comparison — adds 35% row"
      - "Table A3 (Appendix): Full sweep raw data with training/eval details"
    figures_description:
      - >
        Figure 3 (§4.4): Dual-axis plot.
        Left axis (blue): PPL vs sparsity%, non-monotonic curve with min at 40%.
        Right axis (red): MMLU accuracy vs sparsity%, strictly monotonic decline.
        Piecewise fit overlaid as dashed line with breakpoint annotated at ~38%.
        Gray shaded band shows ±5pp breakpoint uncertainty.
        25% and 45% marked as open circles with "planned for revision" annotation.
      - >
        Figure 3 inset: R² sensitivity curve — R² as function of breakpoint location
        (30-50%), showing plateau near 38% but broad (±5pp) optimum.
    analysis: >
      4 点足以展示 regime transition 的存在（PPL flat→steep, MMLU steady decline），
      但不足以精确量化 boundary。Piecewise fit R² 0.87 — 可接受但审稿人可能要求更多数据点。
      Claim 3 从 "precise phase transition at X%" 降级为
      "qualitative regime change with approximate boundary at ~38%"。
      PPL-MMLU 解耦是 robust observation 不依赖 fit 精度——可以独立强调。
      缺失 25%/45% 是 median tier 的核心弱点之一——reviewer 引用时会说
      "only 4 data points insufficient for the claimed phase transition analysis"。
      应对策略：(a) 强调 existing 4 points + 3 allocation conditions (uniform/global/TEAL)
      = 12 个 data points for regime analysis；(b) promise revision 补至 6+ 点；
      (c) 将 non-monotonic PPL-downstream divergence 作为 standalone finding
      不依赖 piecewise fit。

  # ============================================================
  # PLAN_010: LongBench English Subset
  # ============================================================
  - name: plan_010_longbench
    plan_id: plan_010
    description: >
      LongBench English subset（4K-32K tokens），原计划覆盖所有条件（KL, BCE+comp,
      SPON, SPON+KL, training-free）。Median tier 下仅部分条件完成：
      dense（v6 已有）、KL 30% uniform（v6 已有）、TEAL 30%（新跑）。
      KL 50%、BCE+comp、SPON 因 OOM/timeout 未完成。
    expected_results:
      status: partial_completion
      conditions_completed: [dense, kl_30pct_uniform, teal_30pct]
      conditions_failed: [kl_50pct, bce_50pct, spon, spon_kl]
      failure_reason: "32K context + sparse inference exceeds single-GPU memory; conditions requiring multiple models simultaneously OOM"
      # dense (from longbench_dense_v6)
      dense_narrativeqa: 7.3
      dense_qasper: 13.4
      dense_gov_report: 30.5
      dense_multi_news: 2.5
      # KL 30% uniform (from longbench_kl30_uniform_v6)
      kl30u_narrativeqa: 4.12
      kl30u_qasper: 6.23
      kl30u_gov_report: 16.97
      kl30u_multi_news: 18.01
      kl30u_multi_news_anomaly: true
      # TEAL 30% (new prediction)
      teal30_narrativeqa: 3.4
      teal30_qasper: 5.0
      teal30_gov_report: 13.8
      teal30_multi_news: 14.5
      # retention ratios (excluding multi_news anomaly)
      kl30u_retention_excl_multinews: 0.57
      teal30_retention_excl_multinews: 0.47
      kl30u_vs_teal30_advantage: 1.21
    result_rationale: >
      LongBench 整体噪声偏大，原因：
      (1) Dense baseline 偏低——NarrativeQA 7.3 远低于 Llama-3.1-8B published benchmarks，
      说明 generation config（temperature、max_tokens、prompt format）可能不够 optimal，
      或 LongBench v6 的 evaluation script 有 truncation issue。
      (2) Multi_news anomaly：dense=2.5 但 KL 30%=18.01 是 red flag。
      最可能原因是 sparse model 生成更短但 higher-precision 的 summary，
      而 ROUGE/F1 metric 在 dense model 生成的 verbose 但 divergent summary 上 penalize recall。
      这是 metric artifact 而非真实质量差异。
      (3) TEAL 30% 预测略劣于 KL 30%（PPL 10.97 vs 8.82 对应 ~17% more degradation on average），
      但 long-context 下差距小于 short-context PPL 差距暗示的——
      长文本任务的 quality bottleneck 在 attention context 而非 FFN sparsity。
      (4) KL 50% OOM：50% sparsity + 32K tokens + predictor overhead + evaluation harness
      在 single 80GB GPU 上 peak memory ~78GB，intermittent OOM。
      需 tensor-parallel 或 gradient-checkpointing 支持，current codebase 不支持。
    tables:
      - "Table 5 (§4.5 or Appendix): LongBench Results (3 conditions only)"
    figures_description:
      - >
        Figure A1 (Appendix): Per-task grouped bar chart.
        4 tasks × 3 conditions（dense/KL-30%/TEAL-30%）.
        Multi_news bar annotated with "†metric anomaly, see §A.3".
        Gray dashed line = dense baseline for reference.
    analysis: >
      LongBench 在 median tier 下是 weakness 而非 strength。
      Dense baseline 偏低削弱了 retention% 的说服力。Multi_news anomaly
      需在 appendix 解释（~100 words 讨论 metric artifact）。
      只完成 3 conditions（原计划 6+），信息量有限。
      KL 30% 优于 TEAL 30% 的结论成立（~1.2× average retention advantage）但 effect size 不大。
      建议：paper 正文简略提及（"LongBench results in Appendix show consistent
      but moderate KL advantage at 30%"），不作为主要贡献。
      Reviewer risk：可能指出 "claims about quality preservation but LongBench
      shows 43% degradation"。应对：explicitly scope claims as
      "short-context quality preservation" and acknowledge long-context degradation
      as limitation and future work direction (training on longer sequences)。
      Revision plan：fix generation config、add missing conditions、
      investigate multi_news anomaly。

  # ============================================================
  # PLAN_011: MT-Bench
  # ============================================================
  - name: plan_011_mtbench
    plan_id: plan_011
    description: >
      MT-Bench evaluation with GPT-4o judge, 80 multi-turn questions, 8 categories.
      P2 priority, requires external API.
    expected_results:
      status: not_completed
      reason: >
        P2 priority. Remaining GPU hours allocated to P0 (C1 ablation) and
        P1 (sweep, LongBench) experiments. GPT-4o API cost ($50-100 for full eval)
        not pre-approved. Deferred to revision.
    result_rationale: >
      MT-Bench 在 median tier 的 resource allocation 中被 deprioritized，原因：
      (1) P0/P1 实验（C1 ablation、sweep 补点、LongBench）消耗了全部 deadline-前 GPU budget。
      (2) MT-Bench 需要先在所有条件下生成 80×2=160 multi-turn responses（~4 GPU-hours），
      再调用 GPT-4o API 做 pairwise judging（~$80，无预算）。
      (3) 即使完成，sparse model 的 multi-turn 质量高度依赖 generation quality
      而非 few-shot accuracy，且 latency benchmark 已显示 sparse inference
      没有 wall-clock 加速（predictor overhead 抵消 sparsity savings），
      所以 MT-Bench story 可能是 "similar quality at similar speed"——不够 compelling。
      (4) EMNLP Efficient Methods track norm 是 PPL + few-shot downstream,
      multi-turn 不是 requirement。
    tables: []
    figures_description: []
    analysis: >
      MT-Bench 缺失可接受。预计 revision 中补充。
      如果 reviewer 要求：KL 30% MT-Bench 预计 score ~6.5-7.0
      （dense ~7.5-8.0），degradation 比 MMLU 温和，
      因 MT-Bench 测 instruction following 而非 factual recall，
      对 FFN sparsity 更 robust。但这只是估计，不能写进 paper。

  # ============================================================
  # PLAN_012: RULER
  # ============================================================
  - name: plan_012_ruler
    plan_id: plan_012
    description: >
      RULER synthetic long-context evaluation (4K, 16K) × 3 task types.
      P2 priority, depends on plan_010 infrastructure.
    expected_results:
      status: not_completed
      reason: >
        P2 priority. Depends on plan_010 long-context serving infrastructure
        which itself only partially completed (OOM issues at 32K context).
        RULER at 16K context faces same memory constraints. Deferred.
    result_rationale: >
      RULER 依赖 plan_010 的 long-context evaluation infrastructure。
      Plan_010 暴露了 32K context 下的 OOM 问题，RULER 的 16K 可能可行
      但 4K/16K × 3 tasks × all conditions = ~20 eval runs，
      在 deadline 前 infeasible alongside higher-priority experiments。
      更根本的是：LongBench 已提供 long-context evidence（虽然 noisy），
      RULER 主要是 complementary fine-grained diagnostic。
    tables: []
    figures_description: []
    analysis: >
      RULER 缺失对 paper 影响有限。如果 LongBench 能在 revision 中修复
      并完善，RULER 可以作为 supplementary 一起补上。
      但如果 reviewer 特别关注 long-context capabilities
      （unlikely for Efficient Methods track），这是一个 gap。
```

---

关键 cross-experiment 一致性校验：

| Metric | Source | Value |
|--------|--------|-------|
| KL 50% uniform PPL | bench_kl50_uniform (3-seed mean) | 11.92 |
| C1 ablation 50% uniform PPL | **predicted** | 13.8 |
| Residual gap | 13.8 - 11.96 | **1.84 PPL** (within 2-3 range) |
| BCE 30% forced top-k PPL | **predicted** | 11.5 |
| KL-BCE gap ratio at 30% | 11.5 / 8.82 | **1.30×** |
| KL-BCE gap ratio at 50% | 28.0 / 11.8 | **2.37×** |
| Sweep R² | **predicted** | 0.87 (within 0.80-0.93) |
| 3-seed MMLU σ (observed) | existing data | 1.83pp (borderline) |

Median tier 的核心 trade-off：C1 ablation residual gap 足够大需要诚实讨论（削弱叙事简洁性），但足够小可以 claim "mask quality is dominant factor"。Sweep 数据不完整但 PPL-downstream 解耦的 observation 是 robust 的。Paper 在 Findings 和 Main borderline（ARR ~3.2），revision 有明确可执行的补强路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c838c8fa-7fe3-4efd-8cec-43b3055b0d62",
  "isSidechain": false,
  "requestId": "req_011CbANmNCuK7h6jhCrud45z",
  "type": "assistant",
  "uuid": "1262563b-adc0-4762-9e78-1a5e9c9de613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YA413KszCE89fFTmnacBJV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8862,
      "cache_read_input_tokens": 70378,
      "output_tokens": 8064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8862,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8064,
          "cache_read_input_tokens": 70378,
          "cache_creation_input_tokens": 8862,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8862
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1 ablation 显示 mask quality 解释大部分但非全部 KL 优势（存在 2-3 PPL residual gap）；部分实验噪声偏大；需调整 claim 强度和补充讨论 核心假设：['BCE-on-KL-targets at 50% uniform PPL 在 12.5-15.0——…",
  "leafUuid": "1262563b-adc0-4762-9e78-1a5e9c9de613",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation outperforms BCE in sparse SwiGLU predictors",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1 ablation 显示 mask quality 解释大部分但非全部 KL 优势（存在 2-3 PPL residual gap）；部分实验噪声偏大；需调整 claim 强度和补充讨论 核心假设：['BCE-on-KL-targets at 50% uniform PPL 在 12.5-15.0——…",
  "leafUuid": "1262563b-adc0-4762-9e78-1a5e9c9de613",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation outperforms BCE in sparse SwiGLU predictors",
  "sessionId": "33853d9f-17d4-414b-b622-19f35e1aa725"
}
```

---
