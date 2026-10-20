# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：C1 基本复现但非 exact match，gradient coupling 贡献小但非零；regime 数据有噪声但趋势成立 核心假设：['C1

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/775b9155-5849-4903-92f4-000797d3a8af.jsonl`
- **Structured JSON:** [`99ec95a41cb984393f23.json`](../../sessions/99/99ec95a41cb984393f23.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T17:46:37.820Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T17:46:37.820Z",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：C1 基本复现但非 exact match，gradient coupling 贡献小但非零；regime 数据有噪声但趋势成立\n核心假设：['C1 s123 PPL delta 0.1-0.4: BCE+KL-targets 略差于 KL，gradient coupling 贡献 ~3-8%', 'C1 s123 downstream 出现 1-2 个 task delta 1.5-3pp（可能 ARC-c 或 GSM8K）', '6-point regime curve 基本单调但 35%-40% 区间可能有 ±0.2 PPL 波动', 'BCE 30% forced top-k PPL 9.5-10.5，gap 缩小但 KL 仍优', '审稿人 1-2 人仍质疑 novelty（incremental concern），但多数认为 empirical contribution sufficient']\n关键指标范围：{'c1_ppl_delta_s123': [0.1, 0.4], 'c1_downstream_max_delta_pp': [1.5, 3.0], 'kl30_uniform_ppl_3seed_mean': [8.75, 8.9], 'kl30_uniform_mmlu_3seed_mean': [0.37, 0.42], 'kl30_uniform_mmlu_3seed_std': [0.01, 0.025], 'bce_30pct_forced_topk_ppl': [9.5, 10.5], 'regime_curve_monotonicity_violations': [0, 1], 'reviewer_avg_score': [3.5, 4.0]}\n叙事方向：Claims 需要 calibration。Claim 1 从 \"sole driver\" 降级为 \"dominant driver (>90%)\"， 承认 gradient coupling 有 marginal contribution 但不改变 practical conclusion。 C1 表述改为 \"BCE+KL-targets recovers >95% of KL advantage\"，不再用 exact match。 如果某个 downstream task delta > 2pp，需要补充 per-task analysis 解释哪些 task 对 gradient pathway 更敏感。BCE 30% gap 缩小的话，需要强化 Pareto frontier 叙事 （KL 在 quality-efficiency tradeoff 上仍优，但 margin 需 honest reporting）。 Claim 3 如有 monotonicity violation，改为 \"approximate phase transition\" 并讨论 noise source。仍冲 EMNLP Main，但预期需 minor revision。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: distill_sparse_swiglu\nfocus: 测试 'mask pattern discovery' 叙事的审稿接收度。核心 reframe: C1 causal ablation 证明 target quality（不是 gradient coupling）是 KL 优势的唯一驱动力。BCE+KL-targets PPL = 11.9638 = KL PPL 11.9638（exact match at 50% sparsity, TEAL uniform）。53% mask divergence 作为新发现。包含 6-point sparsity regime analysis。目标 4.0 Main Conference。\n\n## paper_framing.md\n\n# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 across **both PPL and all downstream tasks**. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). **Downstream confirmation (full-spectrum)**: All 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) also match within <1pp delta, confirming gradient coupling = 0 across PPL + reasoning + knowledge + math dimensions. Standard BCE (magnitude masks) PPL ≈ 22.51. Target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from \"engineering a better loss\" to \"discovering that output-distribution distillation reveals hidden neuron importance structure.\" **Supporting evidence**: (a) Iso-compute ablation: BCE with 2.71× more FLOPs still PPL=27.97 vs KL=12.00, confirming the gap is structural; (b) BCE at recommended 30% operating point (D062): forced TEAL top-k PPL=11.24 vs KL=8.82, Δ=2.42 — BCE 30% is nearly as bad as KL 50% (11.80), meaning BCE's inferior masks waste ~20pp of sparsity budget; (c) BCE Lagrangian failure at 30%: BCE loss scale (~0.6) vs KL (~0.0001) causes same Lagrangian to fail; (d) No compensation needed: KL eliminates 67.2M compensation parameters (~256MB). **Anticipated attack**: \"Two-stage training (KL→oracle→BCE) avoids needing KL predictor at inference?\" Defense: KL predictor is contextual (per-input adaptive); oracle masks are fixed. Deployment requires per-input sparsity adaptation. **Remaining caveat**: Single seed (s42); C1 s123 in progress for statistical robustness. (Headline claim, resolves persistent R3-R8 confound)\n\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \"subsuming\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)\n\n3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports \"PPL is a poor proxy for downstream quality\" narrative. **6-point PPL regime curve (D063)**: 30%=8.82, 35%=9.31, 40%=10.12, 45%=10.80, 50%=11.80 (TEAL global). Smooth monotonic increase from 30-50%, providing dense sampling for regime boundary identification. 25% eval pending. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.\n\n- **Our framing / headline question**: \"What does KL distillation actually learn for SwiGLU sparsity prediction, and why do its masks differ fundamentally from magnitude-based oracles?\" The theoretical grounding (§3.6, suggestive): BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm. This provides intuition for how KL *can* discover joint interaction patterns. The C1 causal ablation (§4.4) then empirically confirms: the masks KL discovers, not the gradient pathway itself, are what matter.\n\n- **Headline result template**: \"KL-trained sparsity predictors discover neuron importance patterns that diverge 53% from magnitude-based masks. A causal ablation confirms that these mask patterns, not gradient coupling, drive KL's quality advantage: BCE trained on KL-derived masks matches KL performance exactly across PPL (11.96 = 11.96) and all downstream tasks (delta <1pp on ARC-c, WinoGrande, MMLU, GSM8K). This finding eliminates the need for 67.2M compensation parameters and reveals three sparsity operating regimes (now with 6 data points) with qualitatively different allocation requirements.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: **Substantially mitigated by C1 finding**. The 53% mask divergence and causal ablation are genuine empirical discoveries, not engineering contributions. No prior work has shown that KL-derived masks encode fundamentally different neuron importance from magnitude-based approaches. The paper now contributes a finding (mask pattern discovery) rather than just a method (combining known techniques). Additional support: formal decomposition framework, quantitative s^2 prediction, three-regime analysis.\n\n2. **\"KL wins only because more compute\"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 (plan_009, GQA + sliding window) and Qwen-2.5-14B cross-scale validation (D048/D054). **14B mixed result**: KL PPL advantage preserved (7.62 vs TEAL 8.73, 1.47× dense ratio identical to 8B), but KL MMLU=63.72% (global) / 64.49% (uniform) significantly trails TEAL 71.83% (global). Uniform allocation does not fix this gap (D054). PPL-downstream disconnect at 14B scale is an honest limitation, not hidden. Framing: KL's coupled gradient captures output-distribution fidelity (PPL) across scales, but 14B knowledge-intensive tasks (MMLU) show scale-dependent sensitivity that warrants further investigation.\n\n5. **\"Effect size may not hold on downstream tasks\"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.\n\n6. **\"Unfair comparison: BCE+comp close to KL but at higher inference cost\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- **Novelty upgraded from R8**: C1 causal ablation + 53% mask divergence finding elevates paper from \"systematic composition\" to \"empirical discovery about what KL learns for sparsity prediction.\" This addresses the persistent R3-R8 novelty concern and moves the paper toward Main Conference territory (target 4.0).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:\n    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline\n    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds\n    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and\n    BCE-only 3 seeds (mvp_bce_s42/s123/s456).\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_ids:\n  - mvp_kl_norm_v2_s42\n  - mvp_kl_norm_v2_s123\n  - mvp_kl_norm_v2_s456\n  - mvp_bce_s42\n  - mvp_bce_s123\n  - mvp_bce_s456\n  remaining_runs:\n  - KL-only 2 additional seeds (s0, s1) for 5-seed headline\n  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)\n  - KL+comp 3 seeds (s42, s123, s456)\n  registry_id: kl_only_s1\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- id: plan_002\n  claim: 1\n  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).\n    Isolates whether KL advantage comes from loss function or relaxation method. 3\n    seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: ste_baseline_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- id: plan_003\n  claim: 1\n  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs\n    (KL requires full forward pass for output logits, BCE can use cached targets).\n    Report per-step FLOPs and total training time for both. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: bce_isocompute_v2_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- id: plan_004\n  claim: 2\n  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL\n    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,\n    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: spon_2048_s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- id: plan_005\n  claim: 2\n  description: 'SPON subsumption verification: output-space linearity test showing\n    KL predictor already captures SPON correction signal. ||Delta_logits(s+c) - Delta_logits(s)\n    - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality analysis.\n    Proves SPON+KL ≈ KL (no additive gain). 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  - plan_004\n  registry_id: plan_005_subsumption_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- id: plan_006\n  claim: 1\n  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:\n    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),\n    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free\n    < static-learned < contextual-learned.\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_ids:\n  - training_free_baselines\n  - training_free_wina_greedy\n  registry_id: training_free_baselines\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2\n    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor\n    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto\n    frontier plot.\n\n    '\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  - plan_004\n  - plan_005\n  - plan_006\n  registry_id: bench_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- id: plan_008\n  claim: 3\n  description: '3-level sparsity sweep (30%/50%/70%): KL-only vs BCE-only. Test scaling\n    trend and KL-BCE delta growth. 1 seed per level (sweep analysis, not headline).\n    50% data point reused from plan_001. If 3 levels show non-linear inflection, add\n    intermediate points.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  registry_id: d030_kl50_uniform\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- id: plan_009\n  claim: 1\n  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%\n    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds\n    each condition.\n\n    '\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: lm_eval_mistral_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions\n    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:\n    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization\n    beyond short training sequences.\n\n    '\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 2\n  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8\n    categories. All conditions. Tests instruction-following quality under sparsity.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative\n    task types. Fine-grained capability diagnostics complementing LongBench.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_total_loss: 3.3438\n    final_kl_loss: 3.2969\n    final_reg_loss: 0.05\n    final_sparsity: 0\n    steps: 1000\n    tau_final: 0.1\n    wikitext2_ppl_dense: 6.12\n    wikitext2_ppl_sparse: 455.93\n    wikitext2_ppl_increase_pct: 7349\n    model_level_sparsity: 0.372\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\n- exp_id: mvp_kl_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_kl_s456\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_bce_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 27.9603\n    teal_sparse_ppl: 44.537\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 628\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.3817\n    teal_sparse_ppl: 44.5864\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 629\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.1437\n    teal_sparse_ppl: 43.033\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 603.3\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_lagrangian_quicktest\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_kl_loss: 418\n    final_constraint_loss: 1.211\n    final_sparsity: 0.141\n    final_lambda: 5.06\n    steps: 200\n    sparsity_trajectory:\n    - 0.406\n    - 0.387\n    - 0.289\n    - 0.168\n    - 0.141\n- exp_id: kl_lagrangian_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_normalized_quicktest\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step1_kl: 1.18\n    step200_kl: 0.641\n    step200_sparsity: 0.504\n    final_lambda: 8\n    sparsity_converged_step: 80\n    sparsity_trajectory:\n    - 0.406\n    - 0.398\n    - 0.398\n    - 0.457\n    - 0.52\n    - 0.506\n    - 0.504\n    - 0.504\n    lambda_trajectory:\n    - 1\n    - 2\n    - 4\n    - 8\n    - 8\n    - 8\n    - 8\n    - 8\n- exp_id: mvp_kl_norm_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_norm_v3_quicktest\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics:\n    step1_kl_raw: 1.1797\n    step1_kl_norm: 1.1797\n    step1_sparsity: 0.406\n    step1_lambda: 2\n    step50_kl_raw: 0.7344\n    step50_kl_norm: 0.7344\n    step50_sparsity: 0.514\n    step50_lambda: 1.95\n    step100_kl_raw: 0.625\n    step100_kl_norm: 0.625\n    step100_sparsity: 0.496\n    step100_lambda: 1000\n    step150_kl_raw: 0.5703\n    step150_kl_norm: 0.5703\n    step150_sparsity: 0.48\n    step150_lambda: 1000\n    step200_kl_raw: 0.6836\n    step200_kl_norm: 0.6836\n    step200_sparsity: 0.477\n    step200_lambda: 1000\n    step200_constraint: 0.01178\n    kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)\n    sparsity_range: 0.477-0.514 after step 50\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\n- exp_id: mvp_kl_norm_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2142\n    teal_sparse_ppl: 12.0776\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 97.4\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2474\n    teal_sparse_ppl: 11.9128\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 94.7\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.14\n    teal_sparse_ppl: 13.58\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 121.9\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_only_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.19\n    teal_sparse_ppl: 12.03\n    model_level_sparsity: 0.499\n    ppl_increase_vs_true_dense_pct: 96.57\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: kl_only_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- exp_id: spon_training\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1193\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 9.0977\n    spon_recovery_pct: 3.8\n    ppl_improvement_from_spon: 0.1188\n    ppl_increase_vs_true_dense_pct: 48.7\n    ppl_increase_no_spon_vs_true_dense_pct: 50.6\n    mean_bias_norm: 0.040596\n    max_bias_norm: 0.054199\n    teal_sparse_ppl: 12.08\n    teal_with_spon_ppl: 11.93\n    spon_dense_ppl_degradation: 6.19\n    model_level_sparsity: 0.5\n    eval_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n- exp_id: spon_kl_s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: bce_comp_staged_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 25.44\n    predictor_hard_mask_ppl_no_comp: 27.96\n    teal_sparse_ppl: 44.54\n    model_level_sparsity: 0.558\n    ppl_increase_vs_true_dense_pct: 315.7\n    comp_loss_final: 0.0033\n    bce_loss_final: 0.6379\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: training_free_baselines\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- exp_id: spon_training_seq2048\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: ste_baseline_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- exp_id: spon_2048_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- exp_id: ste_kl_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: training_free_wina_greedy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wina_greedy_ppl: 2126.03\n    dense_ppl: 6.12\n    model_level_sparsity: 0.5\n    eval_dataset: WikiText-2\n    eval_seq_len: 2048\n    greedy_allocation_summary: 'layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80,\n      layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24:\n      0.05-0.15, layers 25-31: 0.00'\n- exp_id: bce_isocompute_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_spon_supp_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: spon_supp_eval_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- exp_id: plan_005_subsumption_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- exp_id: kl_sparsity30_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity70_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_loss: 0.1465\n    kl_normalized: 0.1465\n    kl_raw: 0.1465\n    model_level_sparsity: 0.281\n    sparsity_target: 0.3\n    lambda_sparse_final: 1000\n    lambda_max_cap: 1000\n    tau_final: 0.1\n    constraint_loss_final: 0\n    training_steps: 1000\n    wall_clock_seconds: 2662.6\n    gpu_hours: 0.74\n    note: No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1).\n      Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run\n      was offline (not synced).\n- exp_id: kl_sparsity70_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 13.84\n    predictor_teal_sparse_ppl: 17.91\n    vanilla_teal_sparse_ppl: 100.11\n    teal_sparse_ppl: 17.91\n    teal_sparse_ppl_static_baseline: 17.91\n    model_level_sparsity: 0.7\n    teal_sparse_note: '17.91 = predictor-based TEAL (teal_global_masks: predictor-gated\n      magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py\n      L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct\n      metadata 有误导性.'\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    per_layer_sparsity_range:\n    - 0.508\n    - 0.876\n- exp_id: kl_sparsity30_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    loss: 0.165\n    kl_normalized: 0.165\n    kl_raw: 0.165\n    sparsity: 0.285\n    lambda_sparse: 5000\n    tau: 0.1\n    constraint_loss: 0\n    steps: 1000\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    teal_sparse_ppl_note: 已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\n    model_level_sparsity: 0.3\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n- exp_id: mistral_kl_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_final_loss: 0.2188\n    train_final_kl_raw: 0.2188\n    train_final_kl_norm: 0.2188\n    train_final_constraint: 0\n    train_final_sparsity: 0.48\n    train_final_lambda: 1000\n    train_final_tau: 0.1\n    train_steps_completed: 1000\n    true_dense_ppl: 5.52\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    model_level_sparsity: 0.5\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_samples: 159\n- exp_id: lm_eval_dense_test\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc_norm: 0.3771\n    winogrande_acc: 0.6156\n    mmlu_acc: 0.2591\n    gsm8k_exact_match: 0.0121\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: kl_sparse_50pct\n    server: westd-34887\n    exit_code: 129\n    wall_time_sec: 3010\n    flag: SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\n- exp_id: lm_eval_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.5819\n    winogrande_acc: 0.7814\n    mmlu_acc: 0.6532\n    gsm8k_exact_match: 0.5004\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: dense\n    server: westd-34887\n- exp_id: lm_eval_mistral_downstream\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_mistral_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- exp_id: diag_30pct_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_gsm8k_gencomp\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_teal_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: lm_eval_kl_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.3575\n    arc_challenge_acc_norm: 0.3737\n    winogrande_acc: 0.6756\n    mmlu_acc: 0.2874\n    gsm8k_exact_match_strict: 0.0743\n    gsm8k_exact_match_flexible: 0.0781\n    actual_sparsity: 0.3\n    model: llama-3.1-8b\n    condition: kl_distill_30pct_sparsity_s42\n    mmlu_stem_acc: 0.2499\n    mmlu_social_sciences_acc: 0.2896\n    mmlu_humanities_acc: 0.2786\n    mmlu_other_acc: 0.3363\n- exp_id: gsm8k_gen_compare\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: lm_eval_teal_50pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: vanilla_teal\n    sparsity: 0.5\n    actual_sparsity: 0.5\n    arc_challenge_acc_norm: 0.291\n    winogrande_acc: 0.5556\n    mmlu_acc: 0.2856\n    gsm8k_exact_match_flexible: 0.019\n    gsm8k_exact_match_strict: 0.0114\n    arc_challenge_drop_vs_dense: -0.5\n    winogrande_drop_vs_dense: -0.289\n    mmlu_drop_vs_dense: -0.563\n    gsm8k_drop_vs_dense: -0.962\n    model: Llama-3.1-8B\n    condition: TEAL 50% training-free sparsity\n- exp_id: lm_eval_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge:\n      acc: 0.3933\n      acc_norm: 0.4155\n      acc_stderr: 0.0143\n      acc_norm_stderr: 0.0144\n    winogrande:\n      acc: 0.6559\n      acc_stderr: 0.0134\n    mmlu:\n      acc: 0.3598\n      acc_stderr: 0.004\n    mmlu_stem:\n      acc: 0.313\n    mmlu_humanities:\n      acc: 0.3305\n    mmlu_social_sciences:\n      acc: 0.4108\n    mmlu_other:\n      acc: 0.401\n    gsm8k:\n      exact_match_strict: 0.0849\n      exact_match_flexible: 0.0925\n      strict_stderr: 0.0077\n      flexible_stderr: 0.008\n    actual_sparsity: 0.3\n- exp_id: lm_eval_mistral_kl_50pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.2927\n    arc_challenge_acc_norm: 0.3183\n    arc_challenge_acc_norm_stderr: 0.0136\n    winogrande_acc: 0.629\n    winogrande_acc_stderr: 0.0136\n    mmlu_acc: 0.2295\n    mmlu_acc_stderr: 0.0035\n    mmlu_stem_acc: 0.2125\n    mmlu_humanities_acc: 0.2421\n    mmlu_social_sciences_acc: 0.2171\n    mmlu_other_acc: 0.2398\n    gsm8k_exact_match_strict: 0.0045\n    gsm8k_exact_match_flexible: 0.0212\n    model: Mistral-7B-v0.3\n    condition: kl_distill_50pct_sparsity_s42\n    arc_challenge_retention_vs_dense: 0.528\n    winogrande_retention_vs_dense: 0.799\n    mmlu_retention_vs_dense: 0.368\n    gsm8k_retention_vs_dense: 0.012\n- exp_id: d030_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n    allocation: uniform\n    per_layer_sparsity: uniform 0.301 across all 32 layers\n    mmlu_improvement_vs_global: +11.87pp (0.2874 → 0.4061)\n    gsm8k_change_vs_global: no change (0.0743 → 0.0735, within noise)\n- exp_id: bce_isocompute_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 2700\n    loss: 0.6382\n    bce_loss: 0.6371\n    reg_loss: 0.001\n    sparsity: 0.51\n    training_time_seconds: 2828\n    note: 'BCE saturation confirmed: step 500→2700 only 0.006 improvement'\n- exp_id: bench_mistral_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: d030_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- exp_id: bench_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- exp_id: eval_kl30_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    sparsity_target: 0.3\n    actual_sparsity: 0.3\n- exp_id: d030_kl40_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3627\n    arc_challenge_acc_norm: 0.4181\n    winogrande_acc: 0.6717\n    mmlu_acc: 0.3068\n    gsm8k_exact_match: 0.0394\n    actual_sparsity: 0.398\n- exp_id: eval_bce_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 22.51\n    teal_sparse_ppl: 27.97\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2048\n    arc_challenge_acc_norm: 0.2398\n    arc_challenge_acc_norm_stderr: 0.0125\n    winogrande_acc: 0.5059\n    winogrande_acc_stderr: 0.0141\n    mmlu_acc: 0.3002\n    mmlu_acc_stderr: 0.0038\n    gsm8k_exact_match: 0.0485\n    gsm8k_exact_match_strict: 0.0425\n    gsm8k_exact_match_stderr: 0.0059\n- exp_id: bench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n- exp_id: bench_kl50_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n    actual_sparsity: 0.5\n- exp_id: bench_kl30_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    arc_challenge_acc_norm: 0.3968\n    winogrande_acc: 0.7017\n    mmlu_acc: 0.2527\n    gsm8k_exact_match: 0.0879\n    actual_sparsity: 0.3\n- exp_id: bench_teal30\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.97\n    arc_challenge_acc_norm: 0.4232\n    winogrande_acc: 0.6606\n    mmlu_acc: 0.3861\n    gsm8k_exact_match: 0.0788\n    actual_sparsity: 0.3\n- exp_id: bench_teal50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 23.31\n    arc_challenge_acc_norm: 0.2841\n    winogrande_acc: 0.5304\n    mmlu_acc: 0.2832\n    gsm8k_exact_match: 0.0197\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.963\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: bench_kl40_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.117\n    arc_challenge_acc_norm: 0.4096\n    winogrande_acc: 0.6535\n    mmlu_acc: 0.3806\n    gsm8k_exact_match: 0.05\n    actual_sparsity: 0.4\n- exp_id: longbench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v5\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: latency_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpu_model: NVIDIA RTX PRO 6000 Blackwell Server Edition\n    dtype: float16\n    attn: flash_attention_2\n    batch: 1\n    seq_len: 2048\n    warmup: 10\n    iters: 100\n    dense_ms: 119.11\n    dense_std: 0.57\n    dense_tokens_per_s: 17194.5\n    kl_30pct_ms: 126.64\n    kl_30pct_std: 0.7\n    kl_30pct_tokens_per_s: 16171.8\n    kl_30pct_speedup: 0.941\n    kl_50pct_ms: 126.78\n    kl_50pct_std: 0.31\n    kl_50pct_tokens_per_s: 16154.2\n    kl_50pct_speedup: 0.939\n    comp_30pct_ms: 129.94\n    comp_30pct_std: 0.75\n    comp_30pct_tokens_per_s: 15761.4\n    comp_30pct_speedup: 0.917\n    comp_50pct_ms: 129.71\n    comp_50pct_std: 0.53\n    comp_50pct_tokens_per_s: 15788.8\n    comp_50pct_speedup: 0.918\n    predictor_overhead_ms: 3.17\n    predictor_overhead_pct: 2.7\n    per_layer_predictor_ms: 0.099\n    dense_ffn_per_layer_ms: 2.427\n    sparse_ffn_pred_per_layer_ms: 2.686\n    compensation_overhead_ms: 3.3\n- exp_id: bench_kl50_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.83\n    arc_challenge_acc_norm: 0.3515\n    winogrande_acc: 0.6298\n    mmlu_acc: 0.2751\n    gsm8k_exact_match: 0.0235\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9604\n    arc_challenge_acc_norm: 0.3345\n    winogrande_acc: 0.6275\n    mmlu_acc: 0.2874\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: longbench_dense_v6\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    longbench_narrativeqa: 7.3\n    longbench_qasper: 13.4\n    longbench_gov_report: 30.5\n    longbench_multi_news: 2.5\n- exp_id: longbench_kl30_uniform_v6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    longbench_narrativeqa: 4.12\n    longbench_qasper: 6.23\n    longbench_gov_report: 16.97\n    longbench_multi_news: 18.01\n    runtime_seconds: 6156.6\n- exp_id: eval_c4_ood_kl50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 9.2075\n    kl_50_global_ppl: 18.401\n    teal_50_ppl: 38.7503\n    kl_vs_dense_ratio: 2\n    teal_vs_dense_ratio: 4.21\n- exp_id: db_sensitivity_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    db64_per_token_ppl: 10.158\n    db64_teal_global_ppl: 12.076\n    db64_sparsity: 0.5\n    db64_loss: 0.361\n    db128_teal_global_ppl: 11.963\n    db128_per_token_ppl: 9.218\n    db256_per_token_ppl: 8.586\n    db256_teal_global_ppl: 12.105\n    db256_sparsity: 0.5\n    db256_loss: 0.27\n    db512_per_token_ppl: 7.933\n    db512_teal_global_ppl: 12.315\n    db512_sparsity: 0.5\n    db512_loss: 0.224\n    best_teal_global_db: 128\n    best_teal_global_ppl: 11.963\n- exp_id: bce_gumbel_lagrangian_isolation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lr_1e4_ppl: 42.99\n    lr_1e3_ppl: 48.4\n    lr_3e3_ppl: 38.02\n    lr_1e4_bce_loss: 0.7158\n    lr_1e3_bce_loss: 0.6781\n    lr_3e3_bce_loss: 0.6632\n    lr_1e4_sparsity: 0.514\n    lr_1e3_sparsity: 0.506\n    lr_3e3_sparsity: 0.504\n    best_ppl: 38.02\n    best_lr: 3e-3\n    kl_baseline_ppl: 11.79\n    gap_vs_kl: 26.23\n- exp_id: steps_curve_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: tau_schedule_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tau_linear_baseline_ppl: 11.963\n    tau_fixed05_ppl: 11.861\n    tau_fixed01_ppl: 12.072\n    tau_fixed05_loss: 0.248\n    tau_fixed01_loss: 0.43\n    best_tau: fixed_0.5\n    ppl_range: 0.211\n- exp_id: steps_curve_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    step200_ppl: 15.158\n    step400_ppl: 12.538\n    step600_ppl: 12.046\n    step800_ppl: 11.907\n    step1000_ppl: 11.906\n    convergence_step: 800\n    ppl_800_vs_1000_delta: 0.001\n- exp_id: mistral_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 6.048\n    kl_teal_global_ppl: 6.7733\n    teal_baseline_ppl: 8.3807\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 1.386\n    ppl_vs_dense_pct: 9.5\n- exp_id: mistral_kl70_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 9.1086\n    kl_teal_global_ppl: 13.3254\n    teal_baseline_ppl: 61.716\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 6.77\n    final_loss: 0.3945\n    actual_sparsity: 0.682\n- exp_id: mistral_teal50_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_baseline_ppl: 18.3061\n    dense_ppl: 5.5238\n    teal_vs_dense_ratio: 3.31\n- exp_id: bench_kl70_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 17.91\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: kl_sparsity70_s42_v2 (teal_global_masks protocol)\n    vanilla_teal_ppl: 100.11\n- exp_id: bench_teal70\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 100.11\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: training_free_baselines experiment (vanilla teal global)\n- exp_id: gradient_snr_kl_vs_bce\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 5.77e-05\n    bce_avg_snr: 1.0e-05\n    snr_ratio: 5.76\n    early_layer_ratio_range: 34-156x\n    late_layer_ratio_range: 2-4x\n- exp_id: natural_sparsity_floor_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    always_pruned_ratio: 0.0006\n    always_pruned_count: 278\n    total_neurons: 458752\n    late_layer_max_ratio: 0.0051\n    threshold: 0.1\n- exp_id: teal_kl_overlap_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_jaccard: 0.396\n    divergence_ratio: 0.433\n    kl_only_pruned_magnitude_ratio: 1.48\n    teal_only_pruned_mean_gate_prob: 0.614\n    min_jaccard_layer: L17-L18 (0.19)\n    max_jaccard_layer: L26-L28 (0.55)\n- exp_id: gradient_snr_constrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 0.000545\n    bce_avg_snr: 5.28e-06\n    snr_ratio: 103.2\n    kl_final_sparsity: 0.508\n    bce_final_sparsity: 0.591\n    steps: 200\n- exp_id: sparsity_floor_extended\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    floor_30pct: 0.0499\n    floor_50pct: 0.0726\n    floor_70pct: 0.1936\n    late_layer_max_30: 0.4604\n    late_layer_max_50: 1.2347\n    late_layer_max_70: 4.3666\n    threshold: 0.1\n    seq_len: 2048\n    num_samples: 50\n- exp_id: teal_kl_overlap_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_score: 7260.3\n    p_value: 0\n    median_percentile_rank: 78.6\n    iqr_q1: 64.4\n    iqr_q3: 89.1\n    layers_significant: 31/32\n    exception_layer: 31\n- exp_id: mag_preservation_reg\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: reverse_kl_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.8\n    vs_forward_kl: +1.01 (+8.6%)\n    sparsity: 0.5\n- exp_id: jsd_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.54\n    vs_forward_kl: +0.75 (+6.4%)\n    sparsity: 0.5\n- exp_id: global_30pct_retention\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    early_retention: 0.771\n    middle_retention: 0.764\n    knowledge_L12_20_retention: 0.797\n    late_L24_31_retention: 0.501\n    L31_retention: 0.284\n    L30_retention: 0.366\n    starved_layers: L27-L31\n- exp_id: kl_bce_f1_oracle\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bce_f1: 0.6128\n    bce_precision: 0.6132\n    bce_recall: 0.6124\n    kl_f1: 0.5397\n    kl_precision: 0.5112\n    kl_recall: 0.5715\n    random_f1: 0.5\n    kl_ppl: 11.79\n    bce_ppl: 22.51\n- exp_id: kl50_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.745\n    arc_challenge: 0.3814\n    winogrande: 0.6125\n    mmlu: 0.2752\n    gsm8k: 0.0281\n- exp_id: kl30_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8308\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.6938\n    mmlu_acc: 0.3944\n    gsm8k_exact_match: 0.0751\n    actual_sparsity: 0.3\n    allocation: uniform\n- exp_id: kl50_s456_train_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl50_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.397\n    final_kl_normalized: 0.397\n    final_sparsity: 0.492\n    final_lambda: 5000\n    final_tau: 0.1\n    steps_completed: 1000\n- exp_id: kl_50pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.745\n    arc_challenge_acc_norm: 0.3814\n    winogrande_acc: 0.6125\n    mmlu_acc: 0.2752\n    gsm8k_exact_match: 0.0281\n    sparsity: 0.5\n    allocation: global\n- exp_id: mistral_dense_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 5.5238\n    model: Mistral-7B-v0.3\n    condition: dense\n    sparsity: 0\n- exp_id: mistral_kl30_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.048\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 0.5242\n- exp_id: mistral_kl50_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.2931\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 1.7693\n- exp_id: mistral_kl70_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 9.1086\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 3.5848\n- exp_id: mistral_kl30_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.7733\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 1.2495\n- exp_id: mistral_kl50_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.6489\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 3.1251\n- exp_id: mistral_kl70_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 13.3254\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 7.8016\n- exp_id: mistral_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3807\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 2.8569\n- exp_id: mistral_teal70_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 61.716\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 56.1922\n- exp_id: kl30_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.2021\n    actual_sparsity: 0.289\n    constraint_satisfied: true\n    training_steps: 1000\n- exp_id: kl_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9748\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.693\n    mmlu_acc: 0.3807\n    gsm8k_exact_match: 0.0758\n    sparsity: 0.3\n    allocation: global\n- exp_id: kl50_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.8057\n    arc_challenge: 0.3319\n    winogrande: 0.6488\n    mmlu: 0.2794\n    gsm8k: 0.0212\n- exp_id: kl30_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9332\n    arc_challenge: 0.4633\n    winogrande: 0.7111\n    mmlu: 0.4382\n    gsm8k: 0.0758\n- exp_id: kl30_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4198\n    ppl_uniform: 8.7947\n    arc_challenge: 0.4505\n    winogrande: 0.6875\n    gsm8k: 0.0758\n- exp_id: qwen14b_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 6.8\n    teal_global_ppl: 7.62\n    ppl_ratio_hard_mask: 1.31\n    ppl_ratio_teal: 1.47\n    final_loss: 0.3398\n    training_sparsity: 0.281\n    teal_sparsity: 0.3\n    lambda: 5000\n    steps: 1000\n- exp_id: qwen14b_kl30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.6232\n    arc_challenge_acc_norm: 0.5717\n    winogrande_acc: 0.7206\n    mmlu_acc: 0.6372\n    gsm8k_exact_match: 0.4882\n- exp_id: downstream_extended_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.727\n    hellaswag_acc: 0.527\n    piqa_acc_norm: 0.7595\n    piqa_acc: 0.747\n    boolq_acc: 0.7685\n- exp_id: wallclock_speedup_30_50\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    theoretical_flops_speedup_30pct: 1.36\n    theoretical_flops_speedup_50pct: 2.45\n    actual_wallclock_speedup_30pct: 0.91\n    actual_wallclock_speedup_50pct: 0.6\n    predictor_overhead_decode_ms: 1\n    predictor_overhead_prefill_ms: 2\n    actual_mean_sparsity_30pct: 0.28\n    actual_mean_sparsity_50pct: 0.605\n    note: No wall-clock speedup without sparse kernels. Mask-based=0.87-0.94x (predictor\n      overhead), structured-skip=0.45-0.74x (gather overhead). Report theoretical\n      FLOPs in paper.\n- exp_id: qwen14b_bce30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 5.57\n    teal_global_ppl: 8.76\n    ppl_ratio_hard_mask: 1.075\n    ppl_ratio_hard_mask_note: at predictor native 6.4% sparsity, not comparable to\n      KL's 28.1%\n    ppl_ratio_teal: 1.69\n    actual_sparsity_teal: 0.3\n    predictor_native_sparsity: 0.064\n    training_log_sparsity_note: Training Lagrangian failed (predictor sparsity=6.4%).\n      Inference via TEAL forces 30% externally. TEAL PPL 8.76 is valid for method\n      comparison.\n    final_loss: 0.5561\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n- exp_id: qwen14b_teal30_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.7332\n    arc_challenge_acc_norm: 0.5683\n    winogrande_acc: 0.7269\n    mmlu_acc: 0.7183\n    gsm8k_exact_match: 0.4951\n- exp_id: qwen14b_bce30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    predictor_native_sparsity: 0.064\n    lambda_max: 50000\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n    sparsity_trajectory: 49%→5% collapse in 50 steps, no recovery over 950 steps\n    note: 10x stronger Lagrangian produces identical sparsity as v1 (lambda=5000).\n      Confirms BCE gradient insufficiency is fundamental, not constraint strength.\n- exp_id: downstream_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.8233\n    hellaswag_acc_norm_stderr: 0.0038\n    piqa_acc_norm: 0.8074\n    piqa_acc_norm_stderr: 0.0092\n    boolq_acc: 0.8294\n    boolq_acc_stderr: 0.0066\n- exp_id: qwen14b_bce30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 8.7634\n    arc_challenge_acc_norm: 0.5759\n    winogrande_acc: 0.7261\n    mmlu_acc: 0.7167\n    gsm8k_exact_match: 0.5307\n- exp_id: downstream_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc: 0.4878\n    hellaswag_acc_norm: 0.667\n    piqa_acc: 0.7258\n    piqa_acc_norm: 0.7361\n    boolq_acc: 0.685\n- exp_id: kl50_global_s123_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7184\n    arc_challenge_acc_norm: 0.3635\n    winogrande_acc: 0.6109\n    mmlu_acc: 0.2834\n    gsm8k_exact_match: 0.0258\n- exp_id: bce_isocompute_v3_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: bce_isocompute_v3_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6368\n    final_sparsity: 0.51\n    training_steps: 2700\n- exp_id: c4_ood_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0458\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_download\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen14b_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl: 5.1854\n    arc_challenge: 0.6758\n    winogrande: 0.8106\n    mmlu: 0.7977\n    gsm8k: 0.8757\n- exp_id: bce_isocompute_v3_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_sparse_ppl: 28.3503\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2312\n    arc_challenge_acc_stderr: 0.01232\n    arc_challenge_acc_norm: 0.2807\n    arc_challenge_acc_norm_stderr: 0.01313\n    winogrande_acc: 0.5241\n    winogrande_acc_stderr: 0.01404\n    mmlu_acc: 0.2567\n    mmlu_acc_stderr: 0.00367\n    gsm8k_exact_match: 0.022\n    gsm8k_exact_match_stderr: 0.00404\n    gsm8k_exact_match_strict: 0.00834\n    gsm8k_exact_match_strict_stderr: 0.0025\n- exp_id: bce_isocompute_v3_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 28.0627\n    arc_challenge_acc_norm: 0.2696\n    winogrande_acc: 0.513\n    mmlu_acc: 0.2655\n    gsm8k_exact_match: 0.022\n- exp_id: qwen14b_kl30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: qwen14b_teal30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl30_8b_s123_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    sparsity: 0.3\n    training_loss: 0.147\n- exp_id: kl30_8b_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    sparsity: 0.3\n    training_loss: 0.148\n- exp_id: qwen14b_kl30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 7.63\n    mmlu_acc: 0.6449\n    arc_challenge_acc_norm: 0.5444\n    winogrande_acc: 0.7245\n- exp_id: qwen14b_teal30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.01\n    mmlu_acc: 0.6634\n    arc_challenge_acc_norm: 0.5529\n    winogrande_acc: 0.6985\n- exp_id: bce_isocompute_v3_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 27.9696\n    arc_challenge_acc: 0.2346\n    arc_challenge_acc_norm: 0.2765\n    winogrande_acc: 0.5162\n    mmlu_acc: 0.2614\n    gsm8k_exact_match: 0.019\n- exp_id: kl30_8b_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    arc_challenge_acc: 0.4462\n    arc_challenge_acc_norm: 0.4744\n    winogrande_acc: 0.7024\n    mmlu_acc: 0.3836\n    gsm8k_exact_match: 0.0917\n- exp_id: kl30_8b_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc: 0.436\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: snr_extended_r6w3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_snr_step300: 0.0058773\n    bce_snr_step300: 0.00114449\n    snr_ratio_step300: 5.14\n    kl_train_time_s: 641\n    bce_train_time_s: 320\n    num_checkpoints: 7\n    steps_range: 0-300\n- exp_id: c4_ood_kl30_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl50_s123_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.89\n    arc_challenge_acc_norm: 37.88\n    winogrande_acc: 62.19\n    mmlu_acc: 27.75\n    gsm8k_exact_match: 2.35\n    comparison_vs_global_topk:\n      ppl_delta: -0.94\n      arc_c_delta: -5.55\n      wg_delta: -6.71\n      mmlu_delta: -8.2\n      gsm8k_delta: -5\n    note: 'Uniform allocation: better PPL but catastrophic downstream degradation\n      vs global_topk. Confirms global_topk allocation is critical for downstream quality.'\n- exp_id: c4_ood_kl30_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0259\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_ood_dense_baseline_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 9.2075\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: kl50_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8614\n    arc_challenge_acc_norm: 0.3754\n    winogrande_acc: 0.6417\n    mmlu_acc: 0.2784\n    gsm8k_exact_match: 0.0212\n- exp_id: c4_ood_kl50_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.6064\n    allocation: global_topk\n    sparsity: 0.5\n    model: llama-3.1-8b\n- exp_id: downstream_ext_kl50_uniform_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: downstream_ext_kl30_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_kl50_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.9867\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 456\n- exp_id: c4_ood_kl30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0401\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl50_s42_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9638\n    arc_challenge_acc_norm: 0.3259\n    winogrande_acc: 0.6235\n    mmlu_acc: 0.2792\n    gsm8k_exact_match: 0.0197\n- exp_id: c4_ood_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.5297\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 42\n- exp_id: kl_comp_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6992\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.3594\n    - 1.3516\n    - 1.0859\n    - 0.9219\n    - 0.8789\n    - 0.8281\n    - 0.7461\n    - 0.7344\n    - 0.6953\n    - 0.6992\n- exp_id: c4_ood_kl30_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.7617\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.0469\n    - 1.3828\n    - 1.0703\n    - 0.9609\n    - 0.8711\n    - 0.7305\n    - 0.6875\n    - 0.7773\n    - 0.7969\n    - 0.7617\n- exp_id: kl_comp_30pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl_comp_30pct_s42_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl_comp_30pct_s123_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 123\n- exp_id: kl_comp_30pct_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl50_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9538\n    arc_challenge_acc_norm: 0.3831\n    winogrande_acc: 0.6196\n    mmlu_acc: 0.275\n    gsm8k_exact_match: 0.0288\n- exp_id: kl_comp_30pct_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: kl_comp_50pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n- exp_id: kl50_s42_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8038\n    arc_challenge_acc_norm: 0.3336\n    winogrande_acc: 0.6338\n    mmlu_acc: 0.2819\n    gsm8k_exact_match: 0.0167\n- exp_id: kl30_s123_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8186\n    arc_challenge_acc_norm: 0.471\n    winogrande_acc: 0.6961\n    mmlu_acc: 0.3763\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s456_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8284\n    arc_challenge_acc_norm: 0.4505\n    winogrande_acc: 0.6953\n    mmlu_acc: 0.3727\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s123_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl30_s456_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: c1_ablation_bce_kl_targets_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wt2_ppl: 9.29\n    eval_sparsity: 0.609\n    oracle_agreement: 0.978\n    final_bce_loss: 0.0545\n    train_steps: 1000\n    train_time_sec: 877.1\n    reference_kl_ppl: 11.79\n    reference_bce_ppl: 22.51\n- exp_id: bce_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_sparsity25_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_final: 0.1582\n    kl_normalized_final: 0.1582\n    sparsity_actual: 0.23\n    sparsity_target: 0.25\n    lambda_final: 5000\n    tau_final: 0.1\n    steps: 1000\n- exp_id: kl_sparsity35_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.203\n    final_sparsity: 0.336\n    steps: 1000\n- exp_id: c1_ablation_eval_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9638\n    arc_challenge_acc_norm: 0.3217\n    winogrande_acc: 0.6314\n    mmlu_acc: 0.2779\n    gsm8k_exact_match: 0.0205\n    sparsity_target: 0.5\n    allocation: uniform\n- exp_id: kl_sparsity45_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.33\n    final_sparsity: 0.449\n    steps: 1000\n- exp_id: bce_30pct_s42_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity25_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.153\n    final_sparsity: 0.23\n    steps: 1000\n- exp_id: kl_sparsity25_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity35_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity45_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: c1_ablation_bce_kl_targets_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl_sparsity40_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity25_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity35_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity45_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: c1_ablation_bce_kl_targets\n  claim: 'Claim 1: mask pattern discovery'\n  description: BCE trained on KL-derived oracle masks achieves PPL 11.9638 = KL PPL\n    11.9638 at 50% sparsity under identical TEAL protocol. 53% mask divergence from\n    magnitude oracles. Target quality is sole driver of KL advantage.\n  estimated_gpu_hours: 0.0\n- name: dense_sparsity_sweep_6pt\n  claim: 'Claim 3: regime analysis with 6 data points'\n  description: KL predictors at 25%/30%/35%/40%/45%/50% with regime boundaries precisely\n    mapped.\n  estimated_gpu_hours: 0.0\n- name: bce_30pct_forced_topk\n  claim: 'Claim 1: BCE baseline at recommended operating point'\n  description: BCE predictor evaluated at 30% via forced TEAL top-k. Fills Table 2\n    gap.\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T17:46:37.832Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T17:46:37.832Z",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-18T17:46:37.952Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：C1 基本复现但非 exact match，gradient coupling 贡献小但非零；regime 数据有噪声但趋势成立
核心假设：['C1 s123 PPL delta 0.1-0.4: BCE+KL-targets 略差于 KL，gradient coupling 贡献 ~3-8%', 'C1 s123 downstream 出现 1-2 个 task delta 1.5-3pp（可能 ARC-c 或 GSM8K）', '6-point regime curve 基本单调但 35%-40% 区间可能有 ±0.2 PPL 波动', 'BCE 30% forced top-k PPL 9.5-10.5，gap 缩小但 KL 仍优', '审稿人 1-2 人仍质疑 novelty（incremental concern），但多数认为 empirical contribution sufficient']
关键指标范围：{'c1_ppl_delta_s123': [0.1, 0.4], 'c1_downstream_max_delta_pp': [1.5, 3.0], 'kl30_uniform_ppl_3seed_mean': [8.75, 8.9], 'kl30_uniform_mmlu_3seed_mean': [0.37, 0.42], 'kl30_uniform_mmlu_3seed_std': [0.01, 0.025], 'bce_30pct_forced_topk_ppl': [9.5, 10.5], 'regime_curve_monotonicity_violations': [0, 1], 'reviewer_avg_score': [3.5, 4.0]}
叙事方向：Claims 需要 calibration。Claim 1 从 "sole driver" 降级为 "dominant driver (>90%)"， 承认 gradient coupling 有 marginal contribution 但不改变 practical conclusion。 C1 表述改为 "BCE+KL-targets recovers >95% of KL advantage"，不再用 exact match。 如果某个 downstream task delta > 2pp，需要补充 per-task analysis 解释哪些 task 对 gradient pathway 更敏感。BCE 30% gap 缩小的话，需要强化 Pareto frontier 叙事 （KL 在 quality-efficiency tradeoff 上仍优，但 margin 需 honest reporting）。 Claim 3 如有 monotonicity violation，改为 "approximate phase transition" 并讨论 noise source。仍冲 EMNLP Main，但预期需 minor revision。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: distill_sparse_swiglu
focus: 测试 'mask pattern discovery' 叙事的审稿接收度。核心 reframe: C1 causal ablation 证明 target quality（不是 gradient coupling）是 KL 优势的唯一驱动力。BCE+KL-targets PPL = 11.9638 = KL PPL 11.9638（exact match at 50% sparsity, TEAL uniform）。53% mask divergence 作为新发现。包含 6-point sparsity regime analysis。目标 4.0 Main Conference。

## paper_framing.md

# Paper Framing — distill_sparse_swiglu

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 2026 cycle)
- Deadline: 2026-05-25 (ARR submission)
- Track: Efficient Methods for NLP

## Core Claims

1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 across **both PPL and all downstream tasks**. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). **Downstream confirmation (full-spectrum)**: All 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) also match within <1pp delta, confirming gradient coupling = 0 across PPL + reasoning + knowledge + math dimensions. Standard BCE (magnitude masks) PPL ≈ 22.51. Target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from "engineering a better loss" to "discovering that output-distribution distillation reveals hidden neuron importance structure." **Supporting evidence**: (a) Iso-compute ablation: BCE with 2.71× more FLOPs still PPL=27.97 vs KL=12.00, confirming the gap is structural; (b) BCE at recommended 30% operating point (D062): forced TEAL top-k PPL=11.24 vs KL=8.82, Δ=2.42 — BCE 30% is nearly as bad as KL 50% (11.80), meaning BCE's inferior masks waste ~20pp of sparsity budget; (c) BCE Lagrangian failure at 30%: BCE loss scale (~0.6) vs KL (~0.0001) causes same Lagrangian to fail; (d) No compensation needed: KL eliminates 67.2M compensation parameters (~256MB). **Anticipated attack**: "Two-stage training (KL→oracle→BCE) avoids needing KL predictor at inference?" Defense: KL predictor is contextual (per-input adaptive); oracle masks are fixed. Deployment requires per-input sparsity adaptation. **Remaining caveat**: Single seed (s42); C1 s123 in progress for statistical robustness. (Headline claim, resolves persistent R3-R8 confound)

2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL "subsuming" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)

3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports "PPL is a poor proxy for downstream quality" narrative. **6-point PPL regime curve (D063)**: 30%=8.82, 35%=9.31, 40%=10.12, 45%=10.80, 50%=11.80 (TEAL global). Smooth monotonic increase from 30-50%, providing dense sampling for regime boundary identification. 25% eval pending. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)

## Story Spine

- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).

- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.

- **Our framing / headline question**: "What does KL distillation actually learn for SwiGLU sparsity prediction, and why do its masks differ fundamentally from magnitude-based oracles?" The theoretical grounding (§3.6, suggestive): BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm. This provides intuition for how KL *can* discover joint interaction patterns. The C1 causal ablation (§4.4) then empirically confirms: the masks KL discovers, not the gradient pathway itself, are what matter.

- **Headline result template**: "KL-trained sparsity predictors discover neuron importance patterns that diverge 53% from magnitude-based masks. A causal ablation confirms that these mask patterns, not gradient coupling, drive KL's quality advantage: BCE trained on KL-derived masks matches KL performance exactly across PPL (11.96 = 11.96) and all downstream tasks (delta <1pp on ARC-c, WinoGrande, MMLU, GSM8K). This finding eliminates the need for 67.2M compensation parameters and reveals three sparsity operating regimes (now with 6 data points) with qualitatively different allocation requirements."

## Two-Dimensional Taxonomy (Conceptual Contribution)

|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
|--------------------------|:-----------------:|:-------------------:|:-------------:|
| Static                   | —                 | —                   | SPON          |
| Per-layer                | —                 | ShadowLLM           | —             |
| Per-token contextual     | FastForward       | —                   | **Ours**      |

Positions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.

## Anticipated Reviewer Concerns

1. **"Incremental / no new algorithm"**: **Substantially mitigated by C1 finding**. The 53% mask divergence and causal ablation are genuine empirical discoveries, not engineering contributions. No prior work has shown that KL-derived masks encode fundamentally different neuron importance from magnitude-based approaches. The paper now contributes a finding (mask pattern discovery) rather than just a method (combining known techniques). Additional support: formal decomposition framework, quantitative s^2 prediction, three-regime analysis.

2. **"KL wins only because more compute"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.

3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.

4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 (plan_009, GQA + sliding window) and Qwen-2.5-14B cross-scale validation (D048/D054). **14B mixed result**: KL PPL advantage preserved (7.62 vs TEAL 8.73, 1.47× dense ratio identical to 8B), but KL MMLU=63.72% (global) / 64.49% (uniform) significantly trails TEAL 71.83% (global). Uniform allocation does not fix this gap (D054). PPL-downstream disconnect at 14B scale is an honest limitation, not hidden. Framing: KL's coupled gradient captures output-distribution fidelity (PPL) across scales, but 14B knowledge-intensive tasks (MMLU) show scale-dependent sensitivity that warrants further investigation.

5. **"Effect size may not hold on downstream tasks"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.

6. **"Unfair comparison: BCE+comp close to KL but at higher inference cost"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.

## Venue Fit
- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation
- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue
- **Novelty upgraded from R8**: C1 causal ablation + 53% mask divergence finding elevates paper from "systematic composition" to "empirical discovery about what KL learns for sparsity prediction." This addresses the persistent R3-R8 novelty concern and moves the paper toward Main Conference territory (target 4.0).


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
  status: DONE
  conclusion: success
  metrics:
    train_loss_final: 0.1582
    kl_normalized_final: 0.1582
    sparsity_actual: 0.23
    sparsity_target: 0.25
    lambda_final: 5000
    tau_final: 0.1
    steps: 1000
- exp_id: kl_sparsity35_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.203
    final_sparsity: 0.336
    steps: 1000
- exp_id: c1_ablation_eval_uniform
  name: ''
  status: DONE
  conclusion: success
  metrics:
    wikitext2_ppl: 11.9638
    arc_challenge_acc_norm: 0.3217
    winogrande_acc: 0.6314
    mmlu_acc: 0.2779
    gsm8k_exact_match: 0.0205
    sparsity_target: 0.5
    allocation: uniform
- exp_id: kl_sparsity45_s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.33
    final_sparsity: 0.449
    steps: 1000
- exp_id: bce_30pct_s42_eval
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity25_s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.153
    final_sparsity: 0.23
    steps: 1000
- exp_id: kl_sparsity25_s42_eval_teal
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity35_s42_eval_teal
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity45_s42_eval_teal
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: c1_ablation_bce_kl_targets_s123
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: kl_sparsity40_s42_eval_teal_uniform
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity25_s42_eval_teal_uniform
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity35_s42_eval_teal_uniform
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity45_s42_eval_teal_uniform
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}


## what_if (hypothetical experiments — additive)

- name: c1_ablation_bce_kl_targets
  claim: 'Claim 1: mask pattern discovery'
  description: BCE trained on KL-derived oracle masks achieves PPL 11.9638 = KL PPL
    11.9638 at 50% sparsity under identical TEAL protocol. 53% mask divergence from
    magnitude oracles. Target quality is sole driver of KL advantage.
  estimated_gpu_hours: 0.0
- name: dense_sparsity_sweep_6pt
  claim: 'Claim 3: regime analysis with 6 data points'
  description: KL predictors at 25%/30%/35%/40%/45%/50% with regime boundaries precisely
    mapped.
  estimated_gpu_hours: 0.0
- name: bce_30pct_forced_topk
  claim: 'Claim 1: BCE baseline at recommended operating point'
  description: BCE predictor evaluated at 30% via forced TEAL top-k. Fills Table 2
    gap.
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
  "promptId": "a8350ed2-4d5c-4d8f-9497-f28d3e69a79d",
  "type": "user",
  "uuid": "e0133140-101a-4ccc-8bee-f0018559d959",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T17:46:37.945Z_

```json
{
  "parentUuid": "e0133140-101a-4ccc-8bee-f0018559d959",
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
  "uuid": "46579772-7942-4d04-a2a8-cad3d77c37bf",
  "timestamp": "2026-05-18T17:46:37.945Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T17:46:37.945Z_

```json
{
  "parentUuid": "46579772-7942-4d04-a2a8-cad3d77c37bf",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c052d20e-dd24-4c9d-a9a7-90d86993d202",
  "timestamp": "2026-05-18T17:46:37.945Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1 基本复现但非 exact match，gradient coupling 贡献小但非零；regime 数据有噪声但趋势成立 核心假设：['C1 s123 PPL delta 0.1-0.4: BCE+KL-targets 略差于 KL，gradient coupling 贡献 ~3-8%', 'C1…",
  "leafUuid": "c052d20e-dd24-4c9d-a9a7-90d86993d202",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "KL sparsity predictor evaluation and regime analysis",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af"
}
```

---

### Assistant

_source line 8 · 2026-05-18T17:46:42.248Z_

I'll analyze the experiment plan and registry data to generate detailed median-tier predictions for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c052d20e-dd24-4c9d-a9a7-90d86993d202",
  "isSidechain": false,
  "requestId": "req_011CbATDAsTgMiYiXQa8ieoS",
  "type": "assistant",
  "uuid": "3627b8e6-57d8-4589-baba-5a8b2dd17418",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6QhSp6BW9tpHjcmsfsf4s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35732,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35732
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

_source line 9 · 2026-05-18T17:46:45.338Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Dbpe1k4vUJueAAp834pFK9`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment files and data",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_14, find any YAML/JSON files related to experiment plans, registry, what_if scenarios, or paper framing. Look for files like experiment_plan.yaml, registry.yaml, what_if.yaml, paper_framing.md, or similar. Also check for any results directories. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3627b8e6-57d8-4589-baba-5a8b2dd17418",
  "isSidechain": false,
  "requestId": "req_011CbATDAsTgMiYiXQa8ieoS",
  "type": "assistant",
  "uuid": "fce57e56-e98c-44bf-ad7a-5a8023b57699",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6QhSp6BW9tpHjcmsfsf4s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35732,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35732
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

_source line 10 · 2026-05-18T17:47:29.971Z_

<details><summary>↩ Tool result · `toolu_01Dbpe1k4vUJueAAp834pFK9`</summary>

```text
Excellent! Let me now compile a comprehensive summary of all the files found:

## Summary of Experiment Plans, Registries, What-If Scenarios, and Paper Framing Files

I've completed a comprehensive search of the directory `/home/ubuntu/.agent-ml-research-idea_gen_0509_14`. Here are all the key files related to experiment plans, registries, what_if scenarios, paper framing, and results directories:

### **Experiment Plan Files**
1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/experiment_plan.yaml`** — Master experiment plan with 12 planned experiments (plan_001 through plan_012) covering four-condition ablations, baseline comparisons, scaling studies, and downstream evaluation. Contains GPU budgets, dependencies, and priority levels (P0-P2).

### **Registry Files (Experiment Tracking)**
1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml`** — Complete experiment registry for distill_sparse_swiglu project with detailed metadata for each experiment including status, retry counts, reproduce commands, GPU hours, and metrics.

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/temp-adv-distill-vla/registry.yaml`** — Registry for the VLA project tracking phase0/phase1 experiments with status indicators (PREPARING, DONE, etc.).

3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/global/registry.yaml`** — Global registry tracking experiments across all projects.

### **Dream (What-If Scenario) Files**
1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/dream_registry.yaml`** — Registry of "dream" sessions (speculative analysis runs) with what_if scenarios. Includes:
   - dream_20260515T164925 (completed, status "done")
   - dream_20260518T160251 (failed, with what_if scenarios like `c1_ablation_bce_kl_targets`, `dense_sparsity_sweep_6pt`, `bce_30pct_forced_topk`)
   - dream_20260518T162617 (failed)
   
   Each dream contains focus areas and hypothetical scenarios for testing different framing approaches.

### **Paper Framing Files**
1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md`** — Core paper framing document with:
   - Target venue: EMNLP 2026 Main (ARR May 2026 cycle)
   - Three core claims about KL-trained sparsity predictors
   - Story spine and headline results template
   - Two-dimensional taxonomy positioning the work
   - Anticipated reviewer concerns and mitigation strategies
   - Venue fit analysis

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml`** — Imagined/planned experimental results with expected outcomes for key ablations, including:
   - Four-condition ablation at 50% sparsity
   - Expected PPL values and variance estimates
   - Compensation benefit analysis
   - STE baseline results
   - Detailed result rationale and tables

3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_context.yaml`** (also median/worst variants) — Review context for different outcome scenarios (best/median/worst case).

### **Writing & Planning Files**
1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml`** — Comprehensive paper writing plan with:
   - Venue metadata (EMNLP 2026, 8-page limit)
   - Paper outline sections with word budgets
   - Abstract, Introduction, Related Work, Method, Experiments sections
   - Citation hints and dependencies
   - Registry references for experiments

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml`** — Literature survey covering 4 research directions:
   - KL distillation for activation sparsity
   - Output distribution preservation
   - SPON and learnable bias correction
   - Training-free activation sparsity methods

### **Decision Tracking**
1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml`** — Detailed decision log with 60+ major decisions tracking:
   - D001-D006 covering MVP design, calibration data choices, sparsity collapse fixes, KL normalization bugs
   - Each decision includes date, summary, rationale, related experiments, and dependencies

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/temp-adv-distill-vla/decisions.yaml`** — VLA project decision log.

### **Results Directories**
1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/results/`** — Contains `wallclock_profile.json` (timing data)

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/results/`** — Documentation results directory

3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/temp-adv-distill-vla/docs/results/`** — VLA results directory

### **Configuration Files**
1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/config/venue_registry.yaml`** — Venue registry (CoRL 2026, EMNLP 2026)

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/config/crons.yaml`** — Cron job scheduling (21KB, containing task scheduling)

3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/config/resources.yaml`** — Resource configuration

### **Key Statistics**
- **40+ YAML files** identified across the workspace
- **3 projects** with structured experiment tracking (distill_sparse_swiglu, temp-adv-distill-vla, idea_gen_0509_14)
- **Multiple dream sessions** with what-if scenario analysis
- **12 planned experiments** with detailed specifications and dependencies
- **Comprehensive paper framing** with multiple outcome scenarios (best/median/worst)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fce57e56-e98c-44bf-ad7a-5a8023b57699",
  "isSidechain": false,
  "promptId": "a8350ed2-4d5c-4d8f-9497-f28d3e69a79d",
  "type": "user",
  "uuid": "f3db4adb-df06-4675-8d91-3ce527fc24df",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_14, find any YAML/JSON files related to experiment plans, registry, what_if scenarios, or paper framing. Look for files like experiment_plan.yaml, registry.yaml, what_if.yaml, paper_framing.md, or similar. Also check for any results directories. Search breadth: medium.",
    "agentId": "a86d20687a2405d8e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Let me now compile a comprehensive summary of all the files found:\n\n## Summary of Experiment Plans, Registries, What-If Scenarios, and Paper Framing Files\n\nI've completed a comprehensive search of the directory `/home/ubuntu/.agent-ml-research-idea_gen_0509_14`. Here are all the key files related to experiment plans, registries, what_if scenarios, paper framing, and results directories:\n\n### **Experiment Plan Files**\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/experiment_plan.yaml`** — Master experiment plan with 12 planned experiments (plan_001 through plan_012) covering four-condition ablations, baseline comparisons, scaling studies, and downstream evaluation. Contains GPU budgets, dependencies, and priority levels (P0-P2).\n\n### **Registry Files (Experiment Tracking)**\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/registry.yaml`** — Complete experiment registry for distill_sparse_swiglu project with detailed metadata for each experiment including status, retry counts, reproduce commands, GPU hours, and metrics.\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/temp-adv-distill-vla/registry.yaml`** — Registry for the VLA project tracking phase0/phase1 experiments with status indicators (PREPARING, DONE, etc.).\n\n3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/global/registry.yaml`** — Global registry tracking experiments across all projects.\n\n### **Dream (What-If Scenario) Files**\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/dream_registry.yaml`** — Registry of \"dream\" sessions (speculative analysis runs) with what_if scenarios. Includes:\n   - dream_20260515T164925 (completed, status \"done\")\n   - dream_20260518T160251 (failed, with what_if scenarios like `c1_ablation_bce_kl_targets`, `dense_sparsity_sweep_6pt`, `bce_30pct_forced_topk`)\n   - dream_20260518T162617 (failed)\n   \n   Each dream contains focus areas and hypothetical scenarios for testing different framing approaches.\n\n### **Paper Framing Files**\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md`** — Core paper framing document with:\n   - Target venue: EMNLP 2026 Main (ARR May 2026 cycle)\n   - Three core claims about KL-trained sparsity predictors\n   - Story spine and headline results template\n   - Two-dimensional taxonomy positioning the work\n   - Anticipated reviewer concerns and mitigation strategies\n   - Venue fit analysis\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml`** — Imagined/planned experimental results with expected outcomes for key ablations, including:\n   - Four-condition ablation at 50% sparsity\n   - Expected PPL values and variance estimates\n   - Compensation benefit analysis\n   - STE baseline results\n   - Detailed result rationale and tables\n\n3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_context.yaml`** (also median/worst variants) — Review context for different outcome scenarios (best/median/worst case).\n\n### **Writing & Planning Files**\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml`** — Comprehensive paper writing plan with:\n   - Venue metadata (EMNLP 2026, 8-page limit)\n   - Paper outline sections with word budgets\n   - Abstract, Introduction, Related Work, Method, Experiments sections\n   - Citation hints and dependencies\n   - Registry references for experiments\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml`** — Literature survey covering 4 research directions:\n   - KL distillation for activation sparsity\n   - Output distribution preservation\n   - SPON and learnable bias correction\n   - Training-free activation sparsity methods\n\n### **Decision Tracking**\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml`** — Detailed decision log with 60+ major decisions tracking:\n   - D001-D006 covering MVP design, calibration data choices, sparsity collapse fixes, KL normalization bugs\n   - Each decision includes date, summary, rationale, related experiments, and dependencies\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/temp-adv-distill-vla/decisions.yaml`** — VLA project decision log.\n\n### **Results Directories**\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/results/`** — Contains `wallclock_profile.json` (timing data)\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/results/`** — Documentation results directory\n\n3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/temp-adv-distill-vla/docs/results/`** — VLA results directory\n\n### **Configuration Files**\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/config/venue_registry.yaml`** — Venue registry (CoRL 2026, EMNLP 2026)\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/config/crons.yaml`** — Cron job scheduling (21KB, containing task scheduling)\n\n3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/config/resources.yaml`** — Resource configuration\n\n### **Key Statistics**\n- **40+ YAML files** identified across the workspace\n- **3 projects** with structured experiment tracking (distill_sparse_swiglu, temp-adv-distill-vla, idea_gen_0509_14)\n- **Multiple dream sessions** with what-if scenario analysis\n- **12 planned experiments** with detailed specifications and dependencies\n- **Comprehensive paper framing** with multiple outcome scenarios (best/median/worst)"
      }
    ],
    "totalDurationMs": 44626,
    "totalTokens": 59796,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4166,
      "cache_read_input_tokens": 53883,
      "output_tokens": 1741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1741,
          "cache_read_input_tokens": 53883,
          "cache_creation_input_tokens": 4166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4166,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 12,
      "searchCount": 4,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "fce57e56-e98c-44bf-ad7a-5a8023b57699",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T17:47:32.513Z_

<details open><summary>🔧 Tool call — Read · `toolu_015J1Rr8wS1T9zh5zyXQgbBj`</summary>

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
  "parentUuid": "f3db4adb-df06-4675-8d91-3ce527fc24df",
  "isSidechain": false,
  "requestId": "req_011CbATH13jABG82UaKMZCmy",
  "type": "assistant",
  "uuid": "55485f13-0d0d-4fe0-8afb-21c73adb3914",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBRfAsT2TRdYVKL48Xc13d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1952,
      "cache_read_input_tokens": 47573,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1952,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 47573,
          "cache_creation_input_tokens": 1952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1952
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

_source line 12 · 2026-05-18T17:47:32.519Z_

<details><summary>↩ Tool result · `toolu_015J1Rr8wS1T9zh5zyXQgbBj`</summary>

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
  "parentUuid": "55485f13-0d0d-4fe0-8afb-21c73adb3914",
  "isSidechain": false,
  "promptId": "a8350ed2-4d5c-4d8f-9497-f28d3e69a79d",
  "type": "user",
  "uuid": "c9ca1a3f-e9fa-4656-a2c7-4d3f202e356a",
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
  "sourceToolAssistantUUID": "55485f13-0d0d-4fe0-8afb-21c73adb3914",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-18T17:47:32.588Z_

````json
{
  "parentUuid": "c9ca1a3f-e9fa-4656-a2c7-4d3f202e356a",
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
  "uuid": "a9cf0aec-4778-43d3-9cd1-c401a92acb5d",
  "timestamp": "2026-05-18T17:47:32.588Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1 基本复现但非 exact match，gradient coupling 贡献小但非零；regime 数据有噪声但趋势成立 核心假设：['C1 s123 PPL delta 0.1-0.4: BCE+KL-targets 略差于 KL，gradient coupling 贡献 ~3-8%', 'C1…",
  "leafUuid": "a9cf0aec-4778-43d3-9cd1-c401a92acb5d",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "KL sparsity predictor evaluation and regime analysis",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af"
}
```

---

### Assistant

_source line 16 · 2026-05-18T17:53:55.356Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment plan, registry, and paper framing. Let me systematically generate median-tier predictions for every planned experiment.

Let me analyze each planned experiment and its status:

**plan_001** (DONE) - Four-condition ablation @ 50% sparsity
- Already completed with extensive registry data
- KL-only 5 seeds done, BCE-only 3 seeds done
- Remaining: BCE+comp 5 seeds, KL+comp 3 seeds

**plan_002** (DONE) - STE baseline

**plan_003** (DONE) - Iso-compute comparison


**plan_004** (DONE) - SPON reimplementation
**plan_005** (DONE) - SPON subsumption verification
**plan_006** (DONE) - Training-free baselines
**plan_007** (DONE) - Full benchmark evaluation
**plan_008** (DONE) - 3-level sparsity sweep
**plan_009** (DONE) - Mistral-7B validation

I see several downstream evaluations still planned: LongBench, MT-Bench, and RULER benchmarks, plus some what-if ablation experiments to run through.

Looking at the median tier predictions across these remaining experiments—I'm expecting the basic reproduction to show gradient coupling contributing around 3-8%, with perplexity deltas in the 0.1-0.4 range and downstream task improvements of 1.5-3 percentage points on tasks like ARC-c or GSM8K. The 6-point sparsity curve should stay mostly monotonic with some minor fluctuations in the 35-40% range, and the forced top-k variant with BCE loss should land in the 9.5-10.5 PPL range while KL still maintains an edge.

Now I'm looking at the specific metric ranges I expect to see across these configurations—KL with 30% sparsity should hit around 8.75-8.9 PPL with MMLU scores between 0.37-0.42, the regime curve might have zero to one monotonicity violation, and reviewer scores should cluster around 3.5-4.0 despite some lingering questions about novelty.

I need to work through each planned experiment and generate median-tier predictions grounded in what I'm seeing in the existing data. For experiments already completed, I'm still predicting what the median scenario would look like as a hypothetical exercise. Starting with the four-condition ablation at 50% sparsity—I have extensive data here, so for the median tier I'd expect KL-only across five seeds to average around 9.19 PPL based on the existing seed results, while BCE-only should land somewhere between 27.96 and 28.38.

For BCE with compression, I'd expect meaningful improvement over BCE alone but still substantially worse than KL—probably in the 20-23 PPL range at 50% sparsity with proper tuning, though the staged compression experiment at 55.8% sparsity showed 25.44 with compression versus 27.96 without. KL with compression is trickier since KL is already performing so well that adding compression likely provides minimal benefit, keeping it around 9.15-9.25 PPL. Actually, I do have existing data for KL+compression at both 30% and 50% sparsity—the 30% case shows 8.9788 PPL and the 50% case shows 11.7933 PPL, which aligns with what I'd expect for the median scenario.

Now I need to think about what the user is actually asking for. They want predictions for each experiment in the plan, including both completed and planned ones. For the completed experiments, I should estimate what median-tier results would look like rather than just reporting the actual best results. Most of the experiments are marked as done, but there are a few with planned status that I need to address as well.

Looking at the C1 ablation with BCE and KL targets, the actual best result shows a PPL of 9.29, but in the median tier this shouldn't match KL exactly—there should be a small gap of around 0.1-0.4 PPL points. So I'd estimate the median performance at around 12.0-12.4 PPL when comparing against KL's 11.96 at 50% uniform sparsity. For the seed 123 variant, I see it's listed as done but failed, so I need to figure out what a reasonable median prediction would be for that case.

Now I'm structuring the full YAML output with all the experiment details. For the four-condition ablation, I have the KL-only baseline across five seeds showing consistent results around 9.19 PPL with minimal variance, and the BCE-only condition performing much worse at around 28.16 PPL on average.

For the combined conditions, the BCE+comp variant should fall somewhere between pure BCE and KL performance—I'm estimating around 23.5 PPL based on the modest gains from composition at 50% sparsity. The KL+comp condition appears to match KL-only performance at roughly 11.78 PPL, suggesting composition doesn't help or hurt when starting from the stronger KL baseline.

Moving through the remaining experiments: STE confirms the loss function itself is the primary driver, hitting 8.2 PPL at 47% sparsity. The iso-compute comparison shows BCE plateaus even with 2.71x more FLOPs, landing around 27-28 PPL and reinforcing that the structural mismatch can't be overcome by scale alone. SPON's recovery metrics are still being compiled. Looking at the full benchmark results across different sparsity methods and configurations, the KL divergence approaches show severe performance degradation as sparsity increases, while TEAL maintains slightly better performance but still drops significantly at higher sparsity levels. The latency analysis reveals that without sparse kernel implementations, the predictor overhead negates any computational benefits.

For the sparsity sweep in the median tier, I'm mapping out a six-point curve from 25% to 50% sparsity, with established measurements at 30%, 40%, and 50%, and I need to fill in the gaps at 35% and 45% to check for monotonicity violations. The Mistral validation confirms the pattern holds across different model architectures, with dense performance at 5.52 PPL and degradation following the same trajectory as sparsity increases.

Now I'm looking at the downstream task performance across both dense and sparse models—the KL 50% variant shows substantial drops across benchmarks like ARC-c, WG, MMLU, and GSM8K compared to dense. For the planned LongBench evaluation on the median tier, I expect the KL predictor to partially generalize beyond the 2048 training length, but with notable degradation on very long sequences over 8K tokens, where the uniform KL 30% variant likely retains only 50-70% of dense performance on shorter tasks around 4K.

Looking at MT-Bench scores, the dense model achieves around 6.5-7.0 average while KL 30% drops to 5.0-5.5 with especially pronounced losses on reasoning-heavy categories, and KL 50% shows major quality degradation at 3.5-4.0. For RULER, the dense model performs strongly at 4K and decently at 16K, but both KL variants show moderate to significant drops that worsen substantially at longer sequences. The key ablation experiment comparing s42 at 50% uniform against the KL baseline shows a perplexity difference of just 0.14, suggesting the approaches are quite close on this metric. Looking at the gradient coupling contribution more carefully—the gap between KL's 11.96 and the BCE+KL-targets result of 12.10 suggests that targets account for nearly all the improvement, leaving only about 0.14 PPL unexplained by the target mechanism itself.

But if the median hypothesis is right and gradient coupling should contribute 3-8% of the total 16.01 PPL advantage, that would mean 0.48 to 1.28 PPL, which would push the BCE+KL-targets result up to around 12.44-13.24 instead of the observed 12.10. There's a discrepancy here I need to work through.

Actually, looking at the C1 delta range of 0.1-0.4 PPL, that's only 0.6-2.5% of the 16 PPL gap—much smaller than the median hypothesis suggests. So the actual contribution seems to be around 1.5% based on the observed deltas of 0.19-0.37 PPL across the samples. For downstream tasks, most show negligible differences, though a couple do show measurable deltas.

Now I'm planning a denser sparsity sweep with 6 points across the 25-50% range to get better resolution on where the effects actually show up. Looking at the PPL values across the sparsity range, I'm seeing a fairly consistent progression from 25% through 50%, with each step increasing by roughly 0.5-0.8 PPL. The 35%-40% transition shows a smooth 0.77 point jump, and the earlier steps maintain similar increments, so the curve appears monotonic despite some measurement noise that could push individual points up or down by about 0.2 PPL.

Now examining the BCE predictor results at 30% forced top-k sparsity — the eval is still preparing but the setup shows BCE performs much better at lower sparsity levels since there's less aggressive pruning. At 50% sparsity, BCE's predictor quality degrades significantly with an F1 of only 0.61 against the oracle, but forcing it to 30% should yield better functional results. For the median tier, I'm estimating around 10.0 PPL for this configuration, which sits comfortably in the expected 9.5-10.5 range.

Comparing across methods: KL at 30% achieves 8.82 PPL, TEAL hits 10.97, so BCE at 10.0 would fall between them — better than TEAL by about 0.97 PPL but still trailing KL by 1.18. This suggests BCE's learned predictor does capture some useful signal beyond just magnitude-based selection, though KL's approach remains superior overall.

Now I'm organizing the full experimental plan into a comprehensive YAML structure covering all five major experiment groups.

Generating markdown table... KL 30% uniform look like? From the registry, I'm seeing three runs with PPL around 8.82 and MMLU around 0.385, with standard deviation of about 0.018 across seeds. All three metrics fall comfortably within the median tier targets—PPL between 8.75 and 8.9, MMLU between 0.37 and 0.42, and MMLU std between 0.01 and 0.025. The s42 seed shows an exact match on the what_if metric at 11.9638, which actually hits the best tier, so I need to recalibrate that downward to stay in median range.

Now I'm computing the 3-seed statistics for KL 50% across both global and uniform configurations. The global variant gives me a mean of 11.776 with standard deviation of 0.049, while the uniform variant yields a mean of 11.936 with standard deviation of 0.040. I need to be careful when writing the YAML to distinguish between results from completed experiments versus predictions for planned ones, and the user is asking for detailed data expansion for every experiment listed in the experiment plan.

For the already-done experiments, I should frame them in the median-tier interpretation where results align closely with observed values, though with some interpretive adjustments. The what_if experiments like the C1 ablation need predicted deltas since they explicitly don't match exactly. Looking at the plan_001 narratives in the median tier, I'm seeing consistent patterns: KL-only with 5 seeds shows tight standard deviation around 0.04, BCE-only performs terribly at ~28 PPL indicating a structural problem, BCE+comp improves modestly to 23-24 PPL but still falls far short of KL performance, and KL+comp shows no improvement over KL-only.

Now examining plan_007 in the median tier, the key operating point is KL at 30% uniform, which dominates on perplexity though shows mixed results on downstream tasks. The Pareto frontier reveals some tension: ARC-c favors TEAL 30% at 42.3% versus KL 30% uniform at 40.8%, a notable 1.5 percentage point gap that's worth flagging, while MMLU and WG both favor KL by 2.0 and 2.5 percentage points respectively, and GSM8K performance is essentially equivalent between the two approaches.

For latency, I need to be clear that without sparse kernels, there's no actual wall-clock improvement to report. Now I'm thinking through how to organize the output — I should structure each experiment with its name, plan ID, description of what it tests, expected metrics, the reasoning behind those values, which tables and figures it contributes to, and the interpretation. Let me work through the YAML format that captures all experiments systematically.

For the C1 ablation specifically, the actual data shows PPL matching exactly at seed 42, but in the median tier I'd expect some variability across seeds. At seed 42, the delta should be around 0.15, while at seed 123 the gap widens to roughly 0.3-0.4, giving a mean delta in that range.

Let me lock in the numbers: C1 at seed 42 gives PPL of 12.11 with a delta of 0.15 from the KL baseline, and at seed 123 the PPL lands at 12.17 with a delta of 0.28. Now I need to work through the downstream metrics.

Looking at the performance deltas across tasks, ARC-c shows the largest gap at 2.1 percentage points where C1 drops to 30.5% versus KL's 32.6%, which is likely driving the maximum. The other tasks show smaller degradations—WinoGrande at 1.4pp, while MMLU and GSM8K are basically noise at 0.4pp and 0.3pp respectively. The 2.1pp max on ARC-c fits within the expected [1.5, 3.0] range, which makes sense given that ARC-c is testing harder reasoning capabilities.

Now I'm ready to construct the full output. I'm filling in the 6-point regime curve with predictions for the missing points: 25% gets 8.25, 35% gets 9.40 to maintain monotonicity, and 45% gets 10.80. The spacing between points stays consistent—each step increases by roughly 0.6 to 1.0 points without violating the monotonic trend. For a violation, maybe 40% could fluctuate to 10.05 while 35% is 9.45, creating a steeper jump at 45→50 but still monotonic.

Actually, the median tier says "基本单调但 35%-40% 区间可能有 ±0.2 PPL 波动". So I should have the curve be essentially monotonic with perhaps one ambiguous point. Let me say 35% = 9.45 (±0.2 means it could be measured as 9.25-9.65 in different runs). The single-seed value might be 9.45, which is smooth. But if re-run with a different seed, you might get 9.25 or 9.65. The point is that this region has noise.

For median with 0 or 1 violations: 0

Now I'm setting specific values that maintain monotonicity while capturing the spacing patterns I'm seeing. The increments between checkpoints show a clear trend—the jump from 45% to 50% is notably larger than the others, which aligns with where the capacity cliff kicks in. The 35%-40% range has slightly more growth than 30%-35%, but they're close enough to suggest near-linear behavior in that middle section.

Wait, I should double-check against the paper framing data. The existing numbers say 30% = 8.82, 35% = 9.31, 40% = 10.12, 45% = 10.80, 50% = 11.80, but the framing labels these as "TEAL global" which seems inconsistent with what I'm seeing. Let me verify whether these are actually KL predictor results evaluated under the TEAL global protocol or if there's a labeling issue here.

Looking at the actual benchmark data, I can see bench_kl30_uniform gives 8.82 PPL while bench_kl30_global gives 8.98 PPL, so the framing curve might be using a mix of these. I'll stick with the existing numbers from the framing as my baseline and add slight noise for the new points I need to estimate, particularly for 25% which isn't yet in the data. For consistency with the paper's standard approach, I'll frame this analysis around the TEAL global protocol.

Now thinking through the what_if experiments—specifically the bce_30pct_forced_topk case where a BCE predictor trained at ~50% sparsity gets forced down to 30% via TEAL top-k. I'd estimate this lands around 10.0 PPL in the median, which would be better than vanilla TEAL 30% (10.97) since the BCE predictor learns some signal beyond just magnitude, but still worse than KL 30% (8.82). That 1.18 PPL gap shows KL's targets remain fundamentally superior even at the easier operating point. Though I need to clarify whether bce_30pct_s42 is about training BCE at 30% target sparsity versus forcing it there.

Looking at the D062 reference in the paper framing, the actual empirical data shows BCE at 30% with forced TEAL top-k gives PPL=11.24 versus KL=8.82, a gap of 2.42—so my estimate was too optimistic.

In the median scenario where BCE 30% performs at 9.5-10.5, that's actually better than the observed 11.24, which means the gap between BCE and KL would narrow in that scenario. This weakens Claim 1 slightly since KL's advantage becomes smaller, though KL still comes out ahead.

Looking at the specific median numbers: BCE 30% at 10.0 versus KL 30% at 8.82 gives a gap of 1.18 instead of the actual 2.42. This makes BCE competitive with TEAL (10.97) but still clearly inferior to KL, which shifts the narrative toward emphasizing the Pareto frontier rather than just the raw performance gap.

The median scenario likely represents a more optimistic outcome for BCE with better training setup or hyperparameters, so I'll commit to using 10.0 as the PPL value for the 30% forced topk variant.

Now I'm looking at the LongBench results across different plans. The dense baseline shows narrativeqa at 7.3, qasper at 13.4, gov_report at 30.5, and multi_news at 2.5, while KL 30% uniform achieves 4.12 on narrativeqa. The earlier registry attempts failed multiple times before v6 finally succeeded for both dense and KL variants.

I'm noticing something odd in the KL results—multi_news jumps to 18.01 compared to 2.5 for dense, which seems backwards. These tasks likely use different metrics like ROUGE for summarization, so I need to verify whether higher scores are actually better across all these benchmarks or if there's an inconsistency in how the metrics are being reported.

The dense baseline scores are surprisingly low overall, which suggests the evaluation itself may have encountered infrastructure problems. For my median-tier predictions, I need to account for all the different compression approaches—dense, KL at 30% and 50%, BCE with compression, SPON, and the training-free baselines—and estimate how each performs across different task types. Based on what I'm seeing, I'd expect KL 30% to retain somewhere around 55-65% of dense performance on shorter single-document QA tasks but drop to 30-40% on longer contexts, while KL 50% would likely fall to 25-35% across most tasks, with BCE+comp underperforming KL across the board and SPON sitting somewhere between BCE and KL.

Now I'm looking at the specific LongBench subtasks to ground these predictions—there are single-document QA tasks like NarrativeQA and Qasper at different context lengths, multi-document QA like HotpotQA and MuSiQue, summarization tasks including GovReport and QMSum, and then few-shot and synthetic tasks like TriviaQA and PassageCount that round out the evaluation.

For MT-Bench, I'm estimating that a dense Llama-3.1-8B would score around 6.0-6.5 with GPT-4o as judge across 80 multi-turn questions, but KL pruning at 30% would drop it to roughly 5.0-5.5, and at 50% sparsity it'd fall to 3.5-4.0. The performance degradation isn't uniform—math, reasoning, and coding tasks suffer the most from sparsity, while roleplay, writing, and extraction tasks hold up better.

For RULER, I'm planning to test at both 4K and 16K context lengths with representative tasks. The dense model should perform well at 4K but more moderately at 16K, and both KL 30% and 50% would show meaningful drops across these lengths, with 50% causing particularly significant degradation.

Now I'm ready to compile the final YAML output. For experiments that are already complete, I'll use median-tier predicted values that align with the actual data—adjusting down any cases where the actuals landed in the best tier. I need to cover all 12 planned experiments plus the 3 what-if scenarios the user requested. Now I'm working through the seed-level predictions for C1, comparing the median deltas against actual performance data. For the done experiment with seed 42, I'm seeing a PPL delta of 0.15 between BCE+KL-targets and the baseline, while the failed seed 123 shows a larger delta of 0.28. I'm also mapping out the downstream task performance across ARC-c, WG, MMLU, and GSM8K to identify where the biggest gaps emerge between C1 and KL approaches.

Looking at the downstream results, the maximum performance delta across both seeds lands around 2.9 percentage points on ARC-c, which falls within the expected range. This suggests that while the perplexity advantage from gradient coupling is modest at around 1-2%, the effect becomes more pronounced on reasoning-heavy tasks like ARC-c where I'm seeing 2-3 percentage point differences, so I need to dig into task-specific analysis to understand this variation.

The core insight is that gradient coupling lets the model explore how neurons interact together rather than treating them in isolation, which matters more for tasks requiring specific neuron combinations, though the target quality itself still dominates the overall advantage. Now I'm working through the concrete numbers for the LongBench experiments to build out the full results.

Looking at the actual baseline metrics from the dense model, I'm noticing some tasks like NarrativeQA and MultiNews have surprisingly low scores, which suggests the model struggles with generation-heavy evaluation protocols on this benchmark. I'll use the observed pattern that KL compression preserves dense performance proportionally to construct realistic predictions for the different compression levels. The multi_news anomaly in the v6 data confirms there were evaluation issues, so I'm going to work with cleaner hypothetical numbers across all six benchmarks instead. I'm projecting retention rates where KL 30% maintains 60-75% of dense performance on most tasks, while KL 50% drops significantly to 30-48% retention, with harder reasoning tasks like hotpotqa showing the steepest degradation. I'm realizing the LongBench results are too speculative given the infrastructure issues across multiple versions, so I should only predict reliable outcomes for the subset of tasks that actually succeeded. For MT-Bench, Llama-3.1-8B typically lands around 6.0-6.5, and RULER will depend on the model's raw capabilities since it's synthetic. Rather than continue guessing, I'll write out the YAML with grounded predictions where I have data and flag the uncertainties clearly. Let me also pull the KL 50% downstream stats across the three seeds to make sure I have the complete picture. Now I'm compiling the aggregate results across the three seeds with the uniform approach — ARC-c shows the most variance ranging from 32.6 to 38.3 with a mean of 36.3, while the other metrics are much more stable, with WG and MMLU hovering around 62.2 and 27.7 respectively and only GSM8K showing moderate variation at 2.4 mean.

I have the data I need, so I'm organizing the results into tables now — the main PPL comparison will be first, followed by downstream benchmarks, sparsity regimes, ablations, cross-model generalization, and efficiency metrics, with additional appendix tables for the SPON and STE analyses plus the longer-context evaluations.

For the figures, I'm planning a conceptual taxonomy diagram, the PPL regime curve across six points, a Pareto frontier visualization, mask divergence patterns, and gradient SNR comparisons.

Now I need to write out the comprehensive YAML with careful attention to the result_rationale for each experiment — explaining the structural reasons behind why the median-tier results landed where they did. Let me verify the what_if experiment descriptions first, particularly the BCE ablation trained on KL-derived oracle masks.

Generating comprehensive YAML... The gap between BCE and KL narrows at 30% but KL still maintains its advantage. I'm reconsidering how to present these results—for experiments already run, I should show median-tier predictions calibrated to the most likely scenario, adjusting only when actual results fall into best or worst tier ranges. Since most actuals cluster in the median range by definition, I'll keep those values similar and only modify outliers like the C1 exact match cases.

Now I'm checking whether the BCE 30% result of 11.24 PPL actually falls outside the median prediction of 9.5-10.5, which would suggest the actual scenario performed worse than expected for BCE. need to perform better at 30% to match the median tier expectations. The median scenario is really just exploring what the results would look like under different conditions.

Now I'm going to systematically work through each plan and predict the key metrics. For every approach, I'll estimate the perplexity values, any downstream task performance, and supporting metrics with clear reasoning behind each number.

I also need to figure out reasonable estimates for the KL+compensation and BCE+compensation variants at 50%, since those are part of plan_001. For KL with compensation at 50%, the actual result showed essentially no improvement over KL alone, so in the median scenario I'd expect similar performance—the compensation network isn't providing much benefit there.

For BCE+compensation, the actual data point had higher sparsity than my target, so I need to adjust. The improvement from compensation was meaningful at that sparsity level, but I should estimate what it would look like at exactly 50% sparsity instead.

Looking at the numbers, BCE alone at 50% gives around 28.16 PPL, and compensation could recover 3-5 points, putting us at roughly 23-25 PPL. I'll use 24.0 as the median estimate. The downstream performance would still be quite poor though—ARC-c around 25%, MMLU around 29%, WG around 52%, GSM8K barely above 3%.

The real story here is that KL-only achieves 11.80 PPL while eliminating 67.2M compensation parameters entirely, which is a massive gap compared to BCE+comp at 24.0 PPL. Now I need to lay out the full comparison across all the conditions I'm testing.

I'm setting up a comprehensive evaluation covering 17 different configurations—various KL sparsity levels with uniform and global masking, BCE variants, TEAL and WINA approaches, SPON, and a few other methods—all on Llama 3.1 8B. I'll measure each against the downstream tasks and profile latency as well. This is a substantial matrix of experiments to work through.

Now I'm thinking through how to structure the YAML configuration to capture what actually matters for the paper's narrative. Rather than documenting every detail, I should focus on the key metrics and findings that support the main claims. I need to be careful about how I frame the results—particularly around whether gradient coupling is the sole driver or just a dominant factor, and how to honestly report where the margins narrow, like with BCE at 30%, while still maintaining the Pareto frontier narrative that KL-based approaches outperform on the quality-efficiency tradeoff.

For the experiments themselves, I'm mapping out which ones feed into which tables and figures. The four-condition ablation at 50% sparsity forms the backbone of the main results table, the downstream benchmarks across tasks give me Table 2, and then I need the causal ablation to support Claim 1 about gradient coupling's role.

For the sparsity regime, I'm running a 6-point curve across different sparsity levels, and I'll also need cross-model validation with Mistral. The efficiency metrics—latency, FLOPs, parameters—come from the same downstream experiment. Then there's a whole appendix section: SPON analysis, STE ablation, iso-compute comparisons, the forced BCE at 30%, LongBench results, and results on Qwen-14B.

Now I'm mapping out the figures: the method overview, the PPL versus sparsity curve, a Pareto frontier showing the quality-efficiency tradeoff, mask divergence analysis, gradient SNR comparisons, and how downstream task performance holds up across different sparsity levels. I have all the pieces I need to structure the final output.

For the framing, I need to be careful about the reviewer feedback—the median score puts this at borderline to acceptable for the main conference, so some reviewers still see this as incremental. I should avoid overclaiming on the exact match results, acknowledge the variability across tasks and the noise in the regime curves, but make clear that the empirical contribution is solid enough to support publication with revisions.

I also need to fill in multi-seed predictions for the experiments that currently only have single runs—specifically the composite loss conditions in plan_001 and the follow-up experiments in plan_002.

Looking at the STE results across seeds, I'm seeing PPL hovering around 8.2 at 47% sparsity with minimal variance. For the BCE+comp condition, the five-seed median clusters around 24.0 with slightly more spread, which suggests the composite loss is introducing a bit more variability than the STE approach.

Now I'm checking the KL+comp results—the three-seed median sits at 11.77 with very tight consistency across seeds, suggesting this configuration is quite stable. I'm ready to compile the full experimental summary now, organizing everything by plan ID across all the conditions I've tested.

Looking at how to handle the actual versus imagined results, I realize the key is recognizing which experiments landed in the best tier versus the median range. The c1_ablation case is the only one where results clearly hit best-tier performance, so that one needs adjustment toward median. The BCE 30% result at 11.24 actually falls below the median range of 9.5-10.5, so it should shift upward. Most other completed experiments already cluster around the median, so I can keep those values as-is since that's the most probable outcome anyway.

For the remaining planned experiments, I need to generate clean predictions, and for the what_if scenarios, I'll apply the adjustments I outlined. Now I'm ready to compile the full YAML output, which will be substantial but organized. I'm also reconsidering plan_001 more carefully by looking at the registry data—specifically the KL-only results at 50% sparsity across different seeds, which show a mean of 9.19 with minimal variance. I need to confirm whether the headline metric uses the TEAL protocol or the predictor_hard_mask_ppl values.

Looking at the paper's framing, the headline comparison at 50% sparsity uses TEAL uniform allocation across 3 seeds, giving a mean of 11.94 with std 0.04. The TEAL global variant shows a mean of 11.78 with slightly higher variance. For the plan_001 table, I'll report both the per-token hard mask PPL and the TEAL global/uniform PPL to give a complete picture.

Generating the YAML output... Looking at the rest of the results table, I can see KL+comp performs similarly to KL-only, suggesting the compression component doesn't add much value when paired with KL regularization. The STE baseline also shows strong performance. But examining the BCE+comp results more closely, the sparsity level is running too high at 55.8%, which is throwing off the perplexity measurements and making the comparison less reliable. The comp improvement is modest since it was trained on suboptimal BCE masks. Looking at the actual results more carefully—BCE+comp shows about a 2 PPL improvement over BCE-alone, which is meaningful but still far from what KL achieves. For the median tier estimates, I'll settle on BCE+comp hard mask around 20.8 and TEAL around 25.0, rather than overthinking the exact numbers.

Now I'm compiling the final results: KL-only dominates with hard mask PPL of 9.18 and TEAL at 11.78, while compensation adds almost nothing there. Meanwhile, BCE+comp gets to 20.5 hard mask and 25.2 TEAL—a clear gap. The pattern is clear: KL-only is the winner, and compensation is redundant when KL is already doing the heavy lifting. Time to write out the YAML config.

For plan_007's downstream benchmarks, I'm pulling together the ARC-c accuracy numbers across different conditions. The dense baseline sits at 58.3%, and for KL at 30% uniform I'm seeing variation across seeds—ranging from about 40.8% up to 47.1%—which averages around 44.3% with some scatter.

Looking at the variance patterns, ARC-c shows notably higher standard deviation (3.2%) compared to MMLU (1.8%), which is interesting. I'm compiling the full downstream results using the actual three-seed data where I have it: perplexity stays tight at 8.82 across all three seeds, but ARC-c and WikiGen show more variability that I'll need to account for in the final table. Looking at the comparison between KL 30% uniform and TEAL 30%, KL has a substantial advantage on perplexity (nearly 20% better), wins on WikiGen by about 3 points, but the two approaches are essentially equivalent on MMLU while TEAL edges out slightly on GSM8K. The overall picture suggests KL's clear win on perplexity doesn't fully translate to downstream task improvements.

Now I'm ready to structure the YAML output with all the key metrics and make sure the narrative guidance aligns with what the median tier represents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9cf0aec-4778-43d3-9cd1-c401a92acb5d",
  "isSidechain": false,
  "requestId": "req_011CbATHCBhjucAQU6htNwq6",
  "type": "assistant",
  "uuid": "3382a40d-d4d0-4afa-920c-c2aa450bc0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DukX6kLEuEVRSA5LQBzARs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8862,
      "cache_read_input_tokens": 49525,
      "output_tokens": 35962,
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
          "output_tokens": 35962,
          "cache_read_input_tokens": 49525,
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

_source line 17 · 2026-05-18T17:59:05.798Z_

Now I have all the context needed. Let me synthesize the median-tier predictions across all experiments.

```yaml
tier: median
narrative_guidance: |
  Claims 需要 calibration。Claim 1 从 "sole driver" 降级为 "dominant driver (>95%)"，
  承认 gradient coupling 有 marginal contribution (~3-5%) 但不改变 practical conclusion。
  C1 表述改为 "BCE+KL-targets recovers >95% of KL advantage"，不再用 exact match。
  ARC-c 出现 2-3pp delta，需补充 per-task analysis 解释 reasoning tasks 对 gradient pathway 更敏感。
  BCE 30% forced top-k PPL 降至 ~10.0（gap 缩小至 1.2 vs KL 8.82），
  需强化 Pareto frontier 叙事：KL 在 quality-efficiency tradeoff 上仍优但 margin 更小，honest reporting。
  6-point regime curve 基本单调，35% 区间有 ±0.2 noise（单次测量），
  改为 "approximate phase transition" 并讨论 single-seed noise source。
  仍冲 EMNLP Main，预期 reviewer avg 3.5-4.0，需 minor revision。
  1-2 位审稿人仍有 incremental concern，但多数认为 empirical contribution sufficient。
  关键防御：C1 causal ablation + 53% mask divergence 是 genuine empirical finding，
  不是 engineering trick。14B MMLU gap 作为 honest limitation 报告。

imagined_experiments:
  # ============================================================
  # plan_001: Four-condition ablation @ 50% sparsity (Llama 3.1 8B)
  # ============================================================
  - name: "Four-condition ablation @ 50% sparsity"
    plan_id: "plan_001"
    description: |
      Core comparison: KL-only vs BCE-only vs BCE+comp vs KL+comp at 50% model-level sparsity.
      KL-only (5 seeds) as headline, BCE+comp (5 seeds) as primary competitor,
      KL+comp and BCE-only (3 seeds each) as secondary.
    expected_results:
      # KL-only 5 seeds (s42/s123/s456/s0/s1)
      kl_only_hard_mask_ppl_mean: 9.19
      kl_only_hard_mask_ppl_std: 0.04
      kl_only_hard_mask_ppl_seeds: [9.21, 9.25, 9.14, 9.19, 9.15]
      kl_only_teal_global_ppl_mean: 11.78
      kl_only_teal_global_ppl_std: 0.05
      kl_only_sparsity: 0.498
      # BCE-only 3 seeds
      bce_only_hard_mask_ppl_mean: 28.16
      bce_only_hard_mask_ppl_std: 0.21
      bce_only_teal_global_ppl_mean: 44.05
      bce_only_sparsity: 0.496
      # BCE+comp 5 seeds (median prediction)
      bce_comp_hard_mask_ppl_mean: 20.8
      bce_comp_hard_mask_ppl_std: 0.7
      bce_comp_teal_global_ppl_mean: 25.5
      bce_comp_compensation_params: 67248128
      bce_comp_compensation_params_mb: 256
      bce_comp_recovery_vs_bce_ppl: 2.5
      # KL+comp 3 seeds (median prediction)
      kl_comp_hard_mask_ppl_mean: 9.18
      kl_comp_hard_mask_ppl_std: 0.04
      kl_comp_teal_global_ppl_mean: 11.78
      kl_comp_recovery_vs_kl_ppl: 0.01
      kl_comp_compensation_redundant: true
    result_rationale: |
      KL-only 5-seed consistency (std 0.04) 源于 KL loss 的 output-distribution supervision 
      为 predictor 提供了强且稳定的梯度信号（SNR ~5.8x BCE）。所有 seeds 收敛到相似的 mask pattern
      因为 KL landscape 有唯一的 well-defined minimum（neuron importance 由 output distribution 
      唯一确定）。
      
      BCE-only PPL ~28 是因为 BCE 的 factorized gradient 只能学 per-neuron importance，
      无法捕获 neuron interaction patterns。F1 vs magnitude oracle = 0.61 看似不错，
      但 functional quality 差，因为 the wrong 39% neurons 被错误处理。
      
      BCE+comp PPL ~20.8 说明 compensation MLP 能部分修复 BCE 的 mask error，
      但不能替代 mask quality 本身。67.2M 参数（256MB）只换来 ~7 PPL improvement，
      且 KL-only 无需 compensation 就已 PPL 9.19，说明 correct mask > brute-force compensation。
      
      KL+comp ≈ KL-only 因为 KL mask 已经接近 optimal（留下的 neuron set 正是 
      output distribution preservation 所需），compensation 无残余 error 可修复。
    tables:
      - "Table 1: Main 4-condition PPL comparison @ 50% sparsity"
    figures_description:
      - "Bar chart: KL-only vs BCE+comp vs TEAL/WINA baselines, PPL on y-axis, conditions on x-axis. Error bars from multi-seed. Key message: KL-only (no comp) outperforms BCE+comp (with 256MB overhead)."
    analysis: |
      Headline: KL-only (PPL 9.19) > BCE+comp (PPL 20.8) by 2.26x, 同时省去 67.2M compensation 参数。
      KL+comp ≈ KL-only 证明 compensation 在 KL 训练下完全冗余。
      BCE+comp 虽优于 BCE-only (20.8 vs 28.16)，但改善仅 7.4 PPL — compensation 是 BCE 的 patch 
      而非根本解决方案。KL 对 predictor training 的改进是 structural 的（从 mask quality 层面），
      不是 compensation 能弥补的。

  # ============================================================
  # plan_002: STE baseline
  # ============================================================
  - name: "STE baseline (KL + Straight-Through Estimator)"
    plan_id: "plan_002"
    description: |
      KL loss + STE instead of Gumbel-sigmoid. Isolates loss function vs relaxation method contribution.
      3 seeds.
    expected_results:
      ste_hard_mask_ppl_s42: 8.18
      ste_hard_mask_ppl_s123: 8.25
      ste_hard_mask_ppl_s456: 8.20
      ste_hard_mask_ppl_mean: 8.21
      ste_hard_mask_ppl_std: 0.04
      ste_sparsity: 0.47
      ste_sparsity_note: "Lagrangian slightly weaker, converges to 47% vs target 50%"
      kl_gumbel_ppl_at_same_sparsity: 9.19
      ste_vs_gumbel_delta: -1.01
    result_rationale: |
      STE PPL 8.18-8.25 < KL Gumbel PPL 9.19，但 STE sparsity 只达 47% vs Gumbel 的 50%。
      Lower sparsity 意味着 STE 保留了更多 neurons（实际是更宽松的 task），所以 PPL advantage 
      部分来自 lower effective sparsity。核心结论不变：KL loss（无论用 Gumbel 还是 STE 做 relaxation）
      都远优于 BCE loss (28.16)，证明 KL loss function 是 advantage 的 primary source，
      Gumbel relaxation 只影响 sparsity convergence 效率（不影响 mask quality）。
      STE Lagrangian 更弱因为 STE gradient 是 biased estimator，导致 sparsity constraint 
      learning 较慢。
    tables:
      - "Table A2: Relaxation method ablation (STE vs Gumbel-sigmoid)"
    figures_description: []
    analysis: |
      STE 实验确认 KL advantage 来自 loss function 而非 relaxation method。
      Gumbel-sigmoid 提供 lower-variance gradient estimates → better Lagrangian convergence → 
      sparsity 更准确到达 target。但 mask quality 由 KL loss 的 coupled gradient 决定，
      与 relaxation 无关。Paper 中作为 "R3 concern: Gumbel explains gain" 的直接反驳。

  # ============================================================
  # plan_003: Iso-compute comparison
  # ============================================================
  - name: "Iso-compute BCE vs KL"
    plan_id: "plan_003"
    description: |
      BCE training extended to 2700 steps (2.71x KL FLOPs) to rule out compute advantage.
      3 seeds (s42/s123/s456).
    expected_results:
      bce_isocompute_teal_ppl_s42: 27.97
      bce_isocompute_teal_ppl_s123: 28.06
      bce_isocompute_teal_ppl_s456: 28.35
      bce_isocompute_teal_ppl_mean: 28.13
      bce_isocompute_teal_ppl_std: 0.20
      bce_isocompute_training_steps: 2700
      bce_isocompute_flops_ratio_vs_kl: 2.71
      kl_1000step_ppl: 11.78
      bce_loss_saturation_step: 500
      bce_loss_500_to_2700_delta: 0.006
    result_rationale: |
      BCE loss 在 ~500 steps 后饱和（final loss 0.638 → 0.632，delta 仅 0.006），
      额外 2200 steps 几乎无改善。这证明 BCE-KL gap 是 structural mismatch 而非 compute deficit。
      BCE 的 factorized gradient (dL/ds_j depends only on neuron j) 意味着 learning landscape 
      存在 fundamental limit — 无论多少 compute 都无法让 BCE 学到 neuron interaction patterns。
      2.71x FLOPs → PPL 28.13 vs KL 11.78 (2.39x gap)，confirmed structural explanation。
    tables:
      - "Table A3: Iso-compute comparison"
    figures_description:
      - "BCE loss curve showing saturation at ~500 steps, with arrow marking KL equivalent compute point."
    analysis: |
      完全排除 "KL wins only because more compute" concern。
      BCE loss saturation at step 500 意味着 BCE predictor 已到达其 expressiveness limit —
      即使 compute 无限也无法学到 KL-quality masks。
      Gap 2.39x 在 iso-compute 下与 standard compute 下几乎相同 (2.38x)，
      证明额外 compute 对 BCE 无帮助。

  # ============================================================
  # plan_004: SPON reimplementation
  # ============================================================
  - name: "SPON reimplementation on Llama 3.1 8B"
    plan_id: "plan_004"
    description: |
      Learnable bias vectors + KL training for static correction.
      Recovery rate and interference with dense model.
    expected_results:
      spon_sparse_ppl: 8.991
      kl_pred_ppl_no_spon: 9.217
      spon_recovery_pct: 7.3
      spon_ppl_improvement: 0.226
      dense_with_spon_ppl: 6.182
      dense_ppl_degradation: 0.065
      mean_bias_norm: 0.053
      trainable_params: 458752
      trainable_pct_of_model: 0.0057
      teal_with_spon_ppl: 11.79
      teal_without_spon_ppl: 12.08
      teal_spon_recovery_pct: 4.8
    result_rationale: |
      SPON 的 static bias correction 只能修复 input-independent 的 systematic error。
      Recovery 7.3% 说明 KL predictor 的 residual error 中只有一小部分是 static bias —
      大部分 error 是 per-input adaptive 的（取决于 specific token context 下的 neuron importance）。
      Dense PPL degradation 0.065 (6.12 → 6.18) 说明 SPON bias 会轻微干扰 dense forward pass，
      因为 bias 是为 sparse activation pattern 优化的，在 dense 下是 noise。
      SPON 对 TEAL baseline 的 recovery (4.8%) 更低，因为 TEAL 的 error 更分散（per-layer 
      magnitude 误差），static correction 更无效。
    tables:
      - "Table A1: SPON analysis — recovery rate and dense degradation"
    figures_description: []
    analysis: |
      SPON recovery 仅 7.3% 直接支撑 Claim 2：static correction 太弱，无法 complement KL。
      同时，SPON 的 dense degradation (0.065 PPL) 意味着实际 net benefit 更小。
      Conclusion: SPON addresses the wrong error component — KL's residual is dominated by 
      per-input adaptive errors that static bias cannot fix。

  # ============================================================
  # plan_005: SPON subsumption verification
  # ============================================================
  - name: "SPON subsumption logit-space analysis"
    plan_id: "plan_005"
    description: |
      Output-space decomposition: linearity test, magnitude ratio, cosine similarity.
      Per-layer orthogonality analysis. 50 samples × 2048 tokens.
    expected_results:
      linearity_ratio: 0.264
      linearity_ratio_std: 0.007
      magnitude_ratio_spon_vs_kl: 0.158
      magnitude_ratio_std: 0.009
      cosine_similarity_mean: 0.196
      cosine_similarity_std: 0.027
      kl_predictor_effect_norm: 482.65
      spon_correction_norm: 76.2
      interaction_norm: 147.74
      per_layer_cosine_max: 0.0
      conclusion_type: "weak_subsumption"
    result_rationale: |
      Cosine similarity 0.196 (接近 orthogonal，远低于 0.5) 证明 SPON correction 和 KL predictor 
      effect 作用在 logit space 的几乎正交方向。Magnitude ratio 15.8% 说明即使 SPON 和 KL 
      方向一致，SPON 的修正幅度也只有 KL 的 1/6。
      Per-layer cosine ≤ 0 (所有层) 意味着在每一层 SPON 要么和 KL 正交要么轻微反向。
      Interaction term 147.74 (30.6% of KL effect) 看似不小，但这是 nonlinear cross-layer 
      interaction — SPON bias 会改变 subsequent layers 的 input distribution，
      但这种 interaction 并不 translate to PPL improvement（SPON recovery 仅 7.3%）。
      Conclusion: SPON 和 KL 靶向不同的 error components，且 SPON 的 component 太弱，
      composition 无实际收益。
    tables:
      - "Table A1: SPON subsumption metrics"
    figures_description:
      - "Per-layer cosine similarity heatmap showing near-zero or negative values across all 32 layers."
    analysis: |
      Logit-space decomposition 提供 Claim 2 的 mechanistic explanation：
      KL 的 coupled gradient 学到的 mask pattern 在 output space 产生 large-magnitude correction (482.65)，
      SPON 的 static bias 产生 small near-orthogonal correction (76.2)。
      两者靶向的 error mode 不同（per-input vs static），
      SPON 的 mode 太弱无法 complement KL。

  # ============================================================
  # plan_006: Training-free baselines
  # ============================================================
  - name: "Training-free baselines (TEAL, WINA, R-Sparse)"
    plan_id: "plan_006"
    description: |
      TEAL (magnitude + greedy), WINA (weight-informed), R-Sparse (rank-aware) at 30%/50%/70%.
    expected_results:
      teal_global_ppl_30: 10.97
      teal_global_ppl_50: 23.31
      teal_global_ppl_70: 100.11
      wina_global_ppl_30: 11.45
      wina_global_ppl_50: 27.93
      wina_global_ppl_70: 137.24
      rsparse_global_ppl_50: 151.2
      dense_ppl: 6.12
      teal_greedy_allocation_ppl_50: 33.47
    result_rationale: |
      Training-free methods 的 PPL 随 sparsity 急剧增长（TEAL 30%→50%→70%: 10.97→23.31→100.11），
      因为 magnitude-based pruning 在 high sparsity 下 increasingly 删除 functionally important neurons。
      TEAL > WINA > R-Sparse 因为 TEAL 的 global allocation 比 WINA 的 weight-informed scoring 
      更有效地分配 per-layer sparsity budget。R-Sparse 的 rank-aware scoring 在 SwiGLU architecture 
      上表现最差，因为 SwiGLU 的 gating mechanism 使得 rank-based importance 不可靠。
      TEAL greedy allocation (33.47) 远差于 global (23.31)，说明 allocation strategy 
      对 training-free methods 同样重要。
    tables:
      - "Table 1: Training-free baselines row in main comparison table"
    figures_description:
      - "PPL vs sparsity curve for all training-free methods, showing exponential degradation."
    analysis: |
      三层 hierarchy 成立：training-free (TEAL 10.97-100.11) < static-learned (SPON) < 
      contextual-learned (KL 8.82-11.78)。
      TEAL 作为 strongest training-free baseline 仍比 KL 30% 差 2.15 PPL (10.97 vs 8.82)。
      At 50%, gap expands to 11.53 PPL (23.31 vs 11.78)。
      Non-linear gap expansion 说明 learned contextual prediction 在 high sparsity 下 advantage 更大。

  # ============================================================
  # plan_007: Full benchmark evaluation + Pareto frontier
  # ============================================================
  - name: "Full benchmark evaluation + Pareto frontier"
    plan_id: "plan_007"
    description: |
      WikiText-2 PPL + 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) across all conditions.
      Wall-clock profiling. Efficiency-accuracy Pareto frontier.
    expected_results:
      # Dense baseline
      dense_ppl: 6.12
      dense_arc_c: 0.583
      dense_wg: 0.781
      dense_mmlu: 0.653
      dense_gsm8k: 0.488
      # KL 30% uniform (3-seed)
      kl30u_ppl_mean: 8.82
      kl30u_ppl_std: 0.01
      kl30u_arc_c_mean: 0.443
      kl30u_arc_c_std: 0.032
      kl30u_wg_mean: 0.692
      kl30u_wg_std: 0.006
      kl30u_mmlu_mean: 0.385
      kl30u_mmlu_std: 0.018
      kl30u_gsm8k_mean: 0.072
      kl30u_gsm8k_std: 0.002
      # KL 50% global (3-seed)
      kl50g_ppl_mean: 11.78
      kl50g_arc_c_mean: 0.343
      kl50g_wg_mean: 0.631
      kl50g_mmlu_mean: 0.281
      kl50g_gsm8k_mean: 0.021
      # TEAL 30%
      teal30_ppl: 10.97
      teal30_arc_c: 0.423
      teal30_wg: 0.661
      teal30_mmlu: 0.386
      teal30_gsm8k: 0.079
      # TEAL 50%
      teal50_ppl: 23.31
      teal50_arc_c: 0.284
      teal50_wg: 0.530
      teal50_mmlu: 0.283
      teal50_gsm8k: 0.011
      # BCE iso-compute 50% (3-seed)
      bce_iso_teal_ppl_mean: 28.13
      bce_iso_arc_c_mean: 0.265
      bce_iso_wg_mean: 0.518
      bce_iso_mmlu_mean: 0.261
      bce_iso_gsm8k_mean: 0.021
      # Latency profiling
      dense_latency_ms: 119.1
      kl30_latency_ms: 126.6
      kl50_latency_ms: 126.8
      predictor_overhead_ms: 3.17
      predictor_overhead_pct: 2.7
      theoretical_flops_speedup_30pct: 1.36
      theoretical_flops_speedup_50pct: 2.45
      actual_wallclock_speedup_30pct: 0.94
      no_sparse_kernel_note: "No wall-clock speedup without custom sparse GEMV kernels"
    result_rationale: |
      KL 30% uniform 是 recommended operating point 的 median-tier 表现：
      - PPL: 8.82 vs TEAL 10.97 (−19.6%)，KL clearly wins
      - MMLU: 38.5% vs TEAL 38.6% — essentially tied. Median 下 MMLU advantage 被 seed variance (std 1.8%) 淹没
      - WinoGrande: 69.2% vs 66.1% — KL wins by +3.1pp，超过 noise margin
      - ARC-c: 44.3% vs 42.3% — KL slightly better (+2.0pp) 但 seed std 3.2% 使得 significance 不确定
      - GSM8K: 7.2% vs 7.9% — TEAL slightly better by 0.7pp，within noise
      
      Downstream advantage 不如 PPL advantage 一致，因为 discriminative tasks 对 specific 
      neuron subsets 敏感（不同 seed 的 mask 在 critical task-relevant neurons 上有差异）。
      PPL 是 average over all tokens，对 mask quality 更敏感也更稳定。
      
      Latency: 无 wall-clock speedup 因为 standard PyTorch 不支持 structured sparse GEMV。
      Predictor overhead 2.7% (3.17ms/119.1ms) 在 sparse kernel 可用时可被 sparsity savings 
      (theoretical 1.36x at 30%) 覆盖。Paper 报告 theoretical FLOPs savings + overhead。
    tables:
      - "Table 2: Downstream benchmarks across all conditions"
      - "Table 6: Latency profiling and efficiency analysis"
    figures_description:
      - "Pareto frontier: x-axis = theoretical FLOPs (or predictor params), y-axis = WikiText-2 PPL. KL 30% uniform dominates the frontier. TEAL/WINA/BCE on suboptimal side."
      - "Radar chart or grouped bar: downstream task retention (% of dense) by condition."
    analysis: |
      Pareto frontier 叙事在 median 下需 calibration：
      - PPL: KL clearly dominates (−19.6% at 30%)
      - Downstream: mixed. KL 30% uniform beats TEAL on WG (+3.1pp) and ARC-c (+2.0pp)，
        但 MMLU 平局且 GSM8K 略输 (−0.7pp)
      - Honest framing: "KL dominates PPL frontier and provides comparable-to-better downstream,
        with advantage concentrated on WG and ARC-c; GSM8K within noise"
      - Latency limitation: 需 custom sparse kernels 才能实现 wall-clock speedup。
        Report theoretical FLOPs + predictor overhead，acknowledge practical speedup pending。

  # ============================================================
  # plan_008: Sparsity sweep / regime analysis
  # ============================================================
  - name: "Sparsity regime analysis (30%/40%/50%/70%)"
    plan_id: "plan_008"
    description: |
      KL-only at 30%/50%/70% + intermediate points (40%). Test scaling trend.
      Combined with dense_sparsity_sweep_6pt for 6-point curve.
    expected_results:
      kl_30_uniform_ppl: 8.82
      kl_30_uniform_mmlu: 0.406
      kl_40_global_ppl: 10.12
      kl_40_global_mmlu: 0.381
      kl_50_global_ppl: 11.78
      kl_50_global_mmlu: 0.281
      kl_50_uniform_ppl: 11.94
      kl_50_uniform_mmlu: 0.278
      kl_70_global_ppl: 17.91
      kl_70_downstream_collapsed: true
      teal_30_ppl: 10.97
      teal_50_ppl: 23.31
      teal_70_ppl: 100.11
      kl_teal_gap_30: 2.15
      kl_teal_gap_50: 11.53
      kl_teal_gap_70: 82.20
      regime_budget_surplus_boundary: 0.30
      regime_capacity_cliff_boundary: 0.50
      ppl_nonmonotonicity: "40% PPL (8.36) < 30% PPL (8.82) under uniform allocation (non-monotonic)"
      downstream_strictly_monotonic: true
    result_rationale: |
      三个 regime 的 mechanistic explanation：
      
      (1) Budget-surplus (≤30%): 每层都有充足的 neuron budget，uniform allocation 消除 
      layer starvation（σ_MMLU 从 9.5pp 降到 1.3pp）。KL mask quality 优势最大化，
      因为 abundant budget 允许 KL 选择 truly important neurons 而非被迫 compromise。
      
      (2) Budget-constrained (~40%): uniform 反而不如 global（MMLU 30.7% vs 38.1%）。
      当 budget 紧张时，learned per-layer allocation (global topk) 比 blind uniformity 
      更能将有限 budget 分配给 critical layers。这是 non-monotonic allocation preference 
      的机制原因。
      
      (3) Capacity-cliff (≥50%): 模型 capacity 本身不足，无论如何分配都 collapse。
      MMLU ≈ 28% ≈ random（4-choice）。KL 仍能维持 PPL 11.78，因为 PPL 是 continuous metric 
      更 robust to partial capacity loss，而 MMLU 需要 discrete reasoning chain 完整。
      
      PPL non-monotonicity (40% < 30% under uniform): 因为 40% 用了 global allocation 
      (10.12) 而 30% 用了 uniform (8.82)，但如果比较 30% global (8.98) vs 40% global (10.12)，
      PPL 仍然单调递增。Non-monotonicity 只在 cross-allocation comparison 下出现。
    tables:
      - "Table 4: Three-regime sparsity analysis"
    figures_description:
      - "PPL vs sparsity curve (KL vs TEAL) showing diverging gap at high sparsity."
      - "Downstream task retention heatmap: tasks × sparsity levels, color = % of dense."
    analysis: |
      Regime analysis 的 median narrative：三个 regime 存在且 boundaries 明确，
      non-monotonic allocation preference 是 genuine finding。
      Practical recommendation: 30% sparsity + uniform allocation for deployment。
      KL gap over TEAL grows nonlinearly (2.15 → 11.53 → 82.20)，
      说明 learned contextual prediction 的 value 随 sparsity 急剧增加。

  # ============================================================
  # plan_009: Mistral-7B generalization
  # ============================================================
  - name: "Mistral-7B-v0.3 cross-architecture validation"
    plan_id: "plan_009"
    description: |
      KL-only at 30%/50%/70% on Mistral-7B-v0.3 (GQA + sliding window attention).
      Validates that KL advantage transfers across architectures.
    expected_results:
      # Dense baseline
      mistral_dense_ppl: 5.52
      mistral_dense_arc_c: 0.602
      mistral_dense_wg: 0.787
      mistral_dense_mmlu: 0.624
      mistral_dense_gsm8k: 0.365
      # KL 30%
      mistral_kl30_teal_ppl: 6.77
      mistral_kl30_ppl_ratio: 1.23
      # KL 50%
      mistral_kl50_teal_ppl: 8.65
      mistral_kl50_arc_c: 0.318
      mistral_kl50_wg: 0.629
      mistral_kl50_mmlu: 0.230
      mistral_kl50_gsm8k: 0.021
      mistral_kl50_mmlu_retention: 0.368
      # KL 70%
      mistral_kl70_teal_ppl: 13.33
      # TEAL baselines
      mistral_teal30_ppl: 8.38
      mistral_teal50_ppl: 18.31
      mistral_teal70_ppl: 61.72
      # KL/TEAL advantage ratios
      mistral_kl_teal_ratio_30: 1.24
      mistral_kl_teal_ratio_50: 2.12
      mistral_kl_teal_ratio_70: 4.63
      llama_kl_teal_ratio_30: 1.24
      llama_kl_teal_ratio_50: 1.98
      llama_kl_teal_ratio_70: 5.59
      cross_arch_ratio_consistent: true
    result_rationale: |
      KL advantage ratio (KL_teal / TEAL) 在 Mistral 上与 Llama 高度一致：
      30%: 1.24 vs 1.24, 50%: 2.12 vs 1.98, 70%: 4.63 vs 5.59。
      这说明 KL distillation 的 advantage 来自 SwiGLU architecture 的通用特性
      （coupled gradient captures neuron interaction patterns），而非 specific model weights。
      
      Mistral 的 GQA + sliding window attention 不影响 FFN sparsity prediction，
      因为 predictor 只在 FFN block 内操作（input = hidden state after attention）。
      Attention mechanism 差异只影响 hidden state distribution，不改变 KL vs BCE 的 
      fundamental learning dynamics。
      
      Downstream 在 50%: MMLU 23.0% 同样 collapse 到 near-random，
      与 Llama 的 28.1% 一致（both ≈ random 25%）。
      这 cross-validates capacity cliff 存在于 both architectures。
    tables:
      - "Table 5: Cross-architecture generalization (Mistral-7B)"
    figures_description:
      - "KL/TEAL PPL ratio comparison: Llama vs Mistral at 30%/50%/70%, showing consistent advantage."
    analysis: |
      Cross-architecture validation 成功：KL advantage ratio 在 Mistral 上 preserved。
      GSM8K 的 catastrophic drop (36.5% dense → 2.1% KL 50%) 在 Mistral 上更严重，
      可能因为 Mistral 的 math capability 本身较弱 (36.5% vs Llama's 48.8%)。
      Limitation: 仍是 7-8B scale，14B (Qwen) 已知有 MMLU disconnect。

  # ============================================================
  # plan_010: LongBench evaluation (planned)
  # ============================================================
  - name: "LongBench English subset evaluation"
    plan_id: "plan_010"
    description: |
      LongBench English subset (4K-32K tokens). KL-only, BCE, TEAL, SPON conditions.
      Per-task-type breakdown. Tests predictor generalization beyond 2048 training length.
    expected_results:
      # Dense baseline (estimated for Llama-3.1-8B)
      dense_narrativeqa: 18.2
      dense_qasper: 27.5
      dense_hotpotqa: 25.8
      dense_gov_report: 30.0
      dense_multi_news: 25.1
      dense_triviaqa: 82.0
      # KL 30% uniform
      kl30u_narrativeqa: 12.5
      kl30u_qasper: 19.8
      kl30u_hotpotqa: 15.2
      kl30u_gov_report: 22.1
      kl30u_multi_news: 17.5
      kl30u_triviaqa: 56.8
      kl30u_avg_retention: 0.64
      # KL 50% global
      kl50g_narrativeqa: 6.2
      kl50g_qasper: 10.8
      kl50g_hotpotqa: 7.5
      kl50g_gov_report: 14.2
      kl50g_multi_news: 9.1
      kl50g_triviaqa: 32.5
      kl50g_avg_retention: 0.35
      # TEAL 30%
      teal30_narrativeqa: 10.8
      teal30_qasper: 17.2
      teal30_hotpotqa: 13.0
      teal30_gov_report: 19.5
      teal30_multi_news: 14.8
      teal30_triviaqa: 50.2
      teal30_avg_retention: 0.56
      # Retention by context length
      kl30u_retention_4k: 0.72
      kl30u_retention_8k: 0.63
      kl30u_retention_16k: 0.52
      kl30u_retention_32k: 0.41
      length_degradation_note: "Predictor trained on 2048 tokens; generalization degrades with context length"
    result_rationale: |
      Predictor 在 2048 token 上训练，对 longer context 的 generalization 有 length-dependent degradation。
      原因：neuron importance distribution 随 context length 变化——longer context 中 attention pattern
      更 distributed，导致 hidden state 的 distributional shift。Predictor 学到的 importance pattern 
      基于 short-context hidden states，在 long-context 下 partially misaligned。
      
      KL 30% 平均 retention 64% 优于 TEAL 30% 的 56%，说明 KL mask quality advantage 在 
      long-context 下 preserved（虽然 absolute performance 下降）。
      
      Per-task-type pattern: extraction tasks (TriviaQA, HotpotQA) 受 sparsity 影响较小，
      generation tasks (NarrativeQA, MultiNews) 影响较大——generation 需要更完整的 capacity 
      来 maintain fluency and coherence over long outputs。
      
      Summarization (GovReport) intermediate: 需要 comprehension (robust) + generation (fragile)。
      
      Infrastructure 风险：基于 registry 中多次 LongBench 失败 (v1-v5)，median 预期 
      只有部分 tasks 产出可靠结果，可能需要 partial reporting。
    tables:
      - "Table A5: LongBench results (English subset)"
    figures_description:
      - "Retention vs context length curve: showing degradation from 4K to 32K for KL 30% vs TEAL 30%."
    analysis: |
      LongBench 在 median tier 下提供 mixed evidence：
      - KL > TEAL on all task types（advantage preserved）
      - 但 absolute retention 在 long context 下显著下降（72% at 4K → 41% at 32K for KL 30%）
      - 这 motivates future work on long-context-aware predictor training
      - Paper 中作为 partial success + honest limitation 报告。
      - Infrastructure issues 可能导致只报告 subset of tasks。

  # ============================================================
  # plan_011: MT-Bench evaluation (planned)
  # ============================================================
  - name: "MT-Bench multi-turn evaluation"
    plan_id: "plan_011"
    description: |
      80 multi-turn questions, 8 categories, GPT-4o judge.
      Tests instruction-following quality under sparsity.
    expected_results:
      dense_mtbench_avg: 6.35
      dense_writing: 7.2
      dense_roleplay: 7.0
      dense_reasoning: 5.8
      dense_math: 4.5
      dense_coding: 5.2
      dense_extraction: 7.5
      dense_stem: 6.8
      dense_humanities: 6.8
      # KL 30% uniform
      kl30u_mtbench_avg: 5.15
      kl30u_writing: 6.0
      kl30u_roleplay: 5.8
      kl30u_reasoning: 4.2
      kl30u_math: 2.8
      kl30u_coding: 3.5
      kl30u_extraction: 6.5
      kl30u_stem: 5.5
      kl30u_humanities: 5.9
      kl30u_retention_avg: 0.81
      # KL 50% global
      kl50g_mtbench_avg: 3.40
      kl50g_writing: 4.2
      kl50g_roleplay: 3.8
      kl50g_reasoning: 2.5
      kl50g_math: 1.5
      kl50g_coding: 2.0
      kl50g_extraction: 5.0
      kl50g_stem: 3.5
      kl50g_humanities: 4.5
      kl50g_retention_avg: 0.54
      # TEAL 30%
      teal30_mtbench_avg: 4.60
      teal30_retention_avg: 0.72
    result_rationale: |
      MT-Bench 的 multi-turn format 对 sparsity 特别敏感：
      
      (1) Turn 2 依赖 turn 1 的 generation quality — sparsity 引起的 error 会 compound。
      Sparse mask 在 turn 1 产生的 slight distributional shift 在 turn 2 被 amplified，
      因为 turn 2 的 prompt 包含 turn 1 的（degraded）output。
      
      (2) Category-dependent sensitivity：Math/Coding 需要 precise symbolic reasoning，
      对 individual neuron importance 最敏感。Writing/Roleplay 更依赖 learned patterns 
      和 fluency，对 mask 的 approximate correctness 更 tolerant。
      Extraction tasks 主要需要 copying relevant content，对 model capacity 要求最低。
      
      (3) KL 30% retention 81% vs TEAL 30% 72%：KL advantage (+9pp retention) 在 
      multi-turn 下比 single-task benchmark 更明显，因为 better mask quality 在 
      compound error 下的 advantage 被放大。
      
      (4) GPT-4o judge 倾向于给 fluent but wrong answers 较高分数，
      这可能 slightly overestimate sparse model quality（尤其 Math/Coding categories 
      where correctness matters more than fluency）。
    tables:
      - "Table A6: MT-Bench scores by category"
    figures_description:
      - "Radar chart: 8 MT-Bench categories × 3 conditions (dense, KL 30%, TEAL 30%), showing category-dependent sparsity sensitivity."
    analysis: |
      MT-Bench 在 median tier 下是 P2 priority，可能不在 main paper 而在 appendix。
      如果包含，key message：KL 30% retains 81% of dense MT-Bench quality，
      但 Math/Coding categories 下降最大（需要 precise reasoning 的 task 对 sparsity 最敏感）。
      如时间不够或 judge API 有 budget 限制，可 defer 到 camera-ready。

  # ============================================================
  # plan_012: RULER synthetic evaluation (planned)
  # ============================================================
  - name: "RULER synthetic long-context tasks"
    plan_id: "plan_012"
    description: |
      RULER at 4K and 16K, 3 representative task types (needle-in-haystack, multi-key,
      multi-value). Fine-grained capability diagnostics.
    expected_results:
      # Dense baseline
      dense_4k_needle: 0.95
      dense_4k_multikey: 0.82
      dense_4k_multivalue: 0.78
      dense_16k_needle: 0.88
      dense_16k_multikey: 0.65
      dense_16k_multivalue: 0.58
      # KL 30% uniform
      kl30u_4k_needle: 0.82
      kl30u_4k_multikey: 0.60
      kl30u_4k_multivalue: 0.55
      kl30u_16k_needle: 0.58
      kl30u_16k_multikey: 0.32
      kl30u_16k_multivalue: 0.28
      # KL 50% global
      kl50g_4k_needle: 0.55
      kl50g_4k_multikey: 0.30
      kl50g_4k_multivalue: 0.22
      kl50g_16k_needle: 0.25
      kl50g_16k_multikey: 0.12
      kl50g_16k_multivalue: 0.10
      # TEAL 30%
      teal30_4k_needle: 0.75
      teal30_4k_multikey: 0.52
      teal30_4k_multivalue: 0.48
    result_rationale: |
      RULER tasks 的 synthetic nature 使得 sparsity impact 更清晰：
      
      Needle-in-haystack: 最 robust（只需找到一个 specific fact），但仍因 sparsity 
      导致 attention 和 FFN 的 interaction 退化。4K→16K 下降因为 more distractor tokens。
      
      Multi-key/Multi-value: 需要同时 track multiple pieces of information，
      对 model capacity 要求更高。Sparsity 削减的 neurons 可能包含 "memory slots"
      用于 track different keys/values，导致 disproportionate degradation。
      
      KL 30% vs TEAL 30% on needle@4K: 82% vs 75%。KL's better mask preserves 
      the critical neurons for attention-FFN interaction that retrieval depends on。
      
      16K 下所有 sparse conditions 显著退化：predictor 在 2048 上训练，
      16K 的 hidden state distribution 偏移更大，compounding with retrieval task difficulty。
    tables:
      - "Table A7: RULER synthetic evaluation"
    figures_description:
      - "Heatmap: task type × context length × condition, showing double degradation (sparsity + length)."
    analysis: |
      RULER 作为 P2 experiment，主要作为 LongBench 的 fine-grained diagnostic complement。
      Key finding: sparsity 对 multi-hop retrieval (multikey/multivalue) 的影响远大于 
      single-fact retrieval (needle)，providing mechanistic insight into which 
      model capabilities are most fragile under sparsity。
      如 LongBench 失败，RULER 可作为 backup long-context evidence。

  # ============================================================
  # what_if: C1 causal ablation (BCE + KL-derived targets)
  # ============================================================
  - name: "C1 causal ablation: BCE trained on KL-derived oracle masks"
    plan_id: "c1_ablation_bce_kl_targets"
    description: |
      The headline experiment for Claim 1. BCE predictor trained to match KL-derived
      binary oracle masks (not magnitude oracles). Evaluated at 50% TEAL uniform protocol.
      Tests whether target quality or gradient coupling drives KL advantage.
      In median tier: >95% but not 100% of KL advantage explained by targets.
    expected_results:
      # Seed 42 (TEAL uniform 50%)
      c1_s42_ppl: 12.11
      c1_s42_kl_ref_ppl: 11.96
      c1_s42_delta: 0.15
      c1_s42_arc_c: 0.305
      c1_s42_wg: 0.610
      c1_s42_mmlu: 0.275
      c1_s42_gsm8k: 0.017
      # Seed 123 (TEAL uniform 50%)
      c1_s123_ppl: 12.17
      c1_s123_kl_ref_ppl: 11.89
      c1_s123_delta: 0.28
      c1_s123_arc_c: 0.350
      c1_s123_wg: 0.605
      c1_s123_mmlu: 0.270
      c1_s123_gsm8k: 0.019
      # Aggregated
      c1_mean_ppl_delta: 0.22
      c1_gradient_coupling_contribution_pct: 1.4
      c1_target_quality_explains_pct: 98.6
      # Downstream deltas vs KL (max across tasks)
      c1_s42_max_downstream_delta_pp: 2.1
      c1_s42_max_delta_task: "ARC-c"
      c1_s123_max_downstream_delta_pp: 2.9
      c1_s123_max_delta_task: "ARC-c"
      # Reference points
      kl_uniform_50_ppl_s42: 11.96
      bce_magnitude_50_ppl: 27.97
      mask_divergence_kl_vs_magnitude: 0.53
      oracle_agreement_c1_predictor: 0.975
    result_rationale: |
      Median tier C1: PPL delta 0.15-0.28，说明 gradient coupling 有 marginal non-zero 
      contribution 但不改变 practical conclusion。

      为什么 delta > 0（gradient coupling ≠ 0）：
      KL 的 coupled gradient (dL_KL/ds_j depends on ALL active neurons via dlogits/dh · dh/dm) 
      让 predictor 在 training 过程中探索 joint neuron interaction patterns。BCE 即使给了 
      KL-derived oracle targets，仍然用 factorized gradient (dL_BCE/ds_j depends only on j) 
      来学习。Factorized gradient 无法完全 reproduce KL predictor 学到的 nuanced scoring —
      某些 neuron pairs 的 joint importance 只在 coupled gradient 下可见。
      
      为什么 delta 很小（<0.3 PPL）：
      Oracle masks 提供了 explicit supervision（"keep these specific neurons"），
      大幅减少了 learning complexity。BCE with explicit targets 不需要 discover importance —
      只需 classify known-important vs known-unimportant。98.6% 的 advantage 来自 knowing 
      WHICH neurons to keep，gradient coupling 只在 edge cases（importance scores 接近 threshold 
      的 neurons）有 marginal effect。
      
      为什么 ARC-c delta 最大（2.1-2.9pp）：
      ARC-c 的 multi-step reasoning 依赖 specific neuron combinations（"reasoning chains" 
      mapped to neuron subsets）。Gradient coupling 使 KL predictor 学到了这些 combinatorial 
      importance patterns，BCE predictor 即使有 oracle targets 也只学到 individual importance。
      在 reasoning tasks 上，neuron combination 的质量差异被放大为 accuracy gap。
      
      WinoGrande delta 较小（1.4pp）因为 commonsense 更依赖 distributed representations 
      而非 specific neuron chains。MMLU/GSM8K 在 50% sparsity 下已 collapse 到 near-random，
      delta 被 floor effect 掩盖。
    tables:
      - "Table 3: C1 Causal Ablation — BCE+KL-targets vs KL"
    figures_description:
      - "Bar chart: PPL comparison — BCE(magnitude) vs BCE+KL-targets vs KL — showing 97% gap closure from mask quality alone."
      - "Per-task downstream delta chart: showing ARC-c as the most gradient-coupling-sensitive task."
    analysis: |
      C1 在 median tier 下需要 nuanced framing：
      
      Headline: "Target quality accounts for >95% of KL advantage; gradient coupling 
      contributes ~1-3% on PPL and up to 2.9pp on reasoning tasks."
      
      Claim 1 revision: 从 "sole driver" 改为 "dominant driver (>95%)"。
      保留 "mask pattern discovery" 叙事：53% divergence from magnitude oracles 仍是 
      headline finding。但 gradient coupling 的 marginal contribution 需要 acknowledged。
      
      Per-task analysis section (§4.4.1): 解释 ARC-c 对 gradient coupling 更敏感，
      原因是 multi-step reasoning 放大了 neuron combination quality 的差异。
      
      Practical implication 不变：BCE+KL-targets 仍然需要先训练 KL predictor 来 generate 
      oracle masks，所以 deployment 时直接用 KL predictor 更简单。C1 的价值是 
      scientific understanding（why KL works），不是 practical pipeline 替代。

  # ============================================================
  # what_if: 6-point sparsity regime curve
  # ============================================================
  - name: "Dense sparsity sweep — 6-point regime curve"
    plan_id: "dense_sparsity_sweep_6pt"
    description: |
      KL predictors evaluated at 25%/30%/35%/40%/45%/50% sparsity.
      6-point PPL curve for regime boundary identification.
    expected_results:
      kl_25_ppl: 8.20
      kl_30_ppl: 8.82
      kl_35_ppl: 9.40
      kl_40_ppl: 10.12
      kl_45_ppl: 10.78
      kl_50_ppl: 11.80
      # Per-5pp increments
      delta_25_30: 0.62
      delta_30_35: 0.58
      delta_35_40: 0.72
      delta_40_45: 0.66
      delta_45_50: 1.02
      # Monotonicity
      monotonic: true
      monotonicity_violations: 0
      noise_band_35pct: 0.20
      noise_band_note: "35% 在 different seeds 下可能波动 ±0.2 PPL (9.20-9.60)"
      # Regime boundaries
      budget_surplus_regime: "≤30%"
      transition_regime: "35%-40%"
      capacity_cliff_onset: "45%-50%"
      acceleration_45_50: "delta jumps from 0.66 to 1.02, signaling cliff onset"
    result_rationale: |
      6-point curve 在 median tier 下基本单调，但 increments 不 uniform：
      
      25%→30% (+0.62): 线性区域。每 5pp sparsity 增加 ~0.6 PPL。
      足够的 neuron budget 使 KL mask quality 能完全 absorb 额外 pruning。
      
      30%→35% (+0.58): 仍在线性区。但这个 point 有 ±0.2 noise（single seed），
      因为 35% 正处在 budget-surplus → transition 的边界。
      不同 seeds 的 per-layer allocation 在此 sparsity 下 divergence 开始增加。
      
      35%→40% (+0.72): increment 开始扩大。Transition regime 开始——
      某些 layers 的 neuron budget 变得 tight，per-layer importance 的 tail 被截断。
      
      40%→45% (+0.66): 看似 increment 缩小，但因为 40% 用了 global allocation 
      而 45% 也是 global，实际 allocation efficiency 在 compensate capacity loss。
      
      45%→50% (+1.02): 最大 increment。Capacity cliff 开始——critical neuron sets 
      被 pruned 的概率急剧上升。PPL 对 pruning 的 sensitivity 非线性增加，
      因为 remaining neurons 的 marginal importance 更高（已经 prune 了 all "easy" neurons）。
      
      总体 curve shape: 接近 piecewise linear with inflection at ~40%，
      然后 super-linear growth to 50%。不是 smooth quadratic，
      而是 approximate phase transition — 在 median 下 inflection 不够 sharp 
      to call it "phase transition"，改为 "approximate regime boundary"。
    tables:
      - "Table 4: 6-point sparsity regime data"
    figures_description:
      - "6-point PPL vs sparsity curve with error bars at 35% (±0.2). Dashed vertical lines at 30% and 45% marking regime boundaries. Shaded regions for three regimes."
    analysis: |
      在 median 下 Claim 3 需 calibrate：
      - "Phase transition" 改为 "approximate phase transition"
      - 35% point 的 noise (±0.2 PPL) 意味着 exact boundary 有 uncertainty
      - 但 overall trend 成立：PPL increase accelerates from ~0.6/5pp to ~1.0/5pp
      - 与 downstream data 交叉验证：downstream 是 strictly monotonic degradation，
        进一步支持 regime 叙事（PPL 非线性 + downstream 单调 = capacity cliff）
      - Practical deployment guideline 不变：30% 是 sweet spot，40% 需 learned allocation

  # ============================================================
  # what_if: BCE 30% forced top-k
  # ============================================================
  - name: "BCE 30% forced TEAL top-k at recommended operating point"
    plan_id: "bce_30pct_forced_topk"
    description: |
      BCE predictor evaluated at 30% sparsity via forced TEAL top-k allocation.
      Fills Table 2 gap for BCE at recommended operating point.
    expected_results:
      bce_30_forced_topk_ppl: 10.0
      teal_30_baseline_ppl: 10.97
      kl_30_uniform_ppl: 8.82
      bce_30_vs_teal_30_delta: -0.97
      bce_30_vs_kl_30_delta: 1.18
      bce_30_arc_c: 0.410
      bce_30_wg: 0.652
      bce_30_mmlu: 0.370
      bce_30_gsm8k: 0.072
      dense_ppl: 6.12
      bce_30_ppl_ratio_vs_dense: 1.63
      kl_30_ppl_ratio_vs_dense: 1.44
    result_rationale: |
      Median tier BCE 30% PPL = 10.0（好于 TEAL 10.97 但差于 KL 8.82）：
      
      BCE predictor 学到的 scoring 在 30% 下比 50% 更有效，因为：
      (1) 30% 只需区分 "top 70% important" vs "bottom 30% unimportant"，
      这个 binary classification 相对容易，即使 factorized gradient 也能部分学到
      (2) TEAL forced top-k 在 30% 下给 BCE 一个 reasonable allocation baseline，
      BCE 只需 refine magnitude-based scoring 的 ranking，不需要 fully discover importance
      (3) 30% 的 margin of error 更大——即使 rank 错误一些 neurons，
      70% kept neurons 足以覆盖 most important ones
      
      为什么 KL 仍然更好 (8.82 vs 10.0, gap 1.18)：
      KL 的 coupled gradient 在 30% 下仍然比 BCE 学到更好的 neuron ranking，
      特别是在 borderline neurons (importance rank 65-75 percentile) 上。
      这些 borderline neurons 的正确 inclusion/exclusion 对 PPL 有 measurable impact。
      
      Gap 缩小（1.18 at 30% vs 16.19 at 50%）因为 30% 是 "easier" problem —
      less pruning → less room for mask quality to matter → less KL advantage。
      这与 sparsity sweep 的 finding 一致：KL advantage grows with sparsity。
      
      Downstream at 30%: BCE 表现 intermediate between TEAL and KL on most tasks，
      MMLU 37.0% slightly below TEAL 38.6%（因为 BCE mask 对 knowledge-relevant 
      neurons 的 coverage 不如 TEAL's pure magnitude approach at 30%）。
    tables:
      - "Table 2: BCE 30% row completing the comparison table"
    figures_description:
      - "Added to Pareto frontier: BCE 30% point between TEAL 30% and KL 30%, showing KL still dominates."
    analysis: |
      BCE 30% 在 median 下 gap 从 50% 的 16.19 缩小到 30% 的 1.18，
      需要 honest reporting：
      
      - KL 仍优（8.82 vs 10.0），但 margin 更小
      - Pareto narrative 需调整：强调 KL 在 ALL operating points 上 Pareto-dominate BCE，
        but gap 是 sparsity-dependent
      - BCE 30% 优于 TEAL 30%（10.0 vs 10.97），说明 learned scoring (even factorized) 
        比 pure magnitude 好
      - Three-tier hierarchy 仍然成立：magnitude (TEAL 10.97) < learned-factorized (BCE 10.0) < 
        learned-coupled (KL 8.82)
      - 这个 three-tier 结果 strengthens "gradient coupling matters" narrative 
        即使 C1 shows target quality is dominant
```

关键叙事 calibration 总结：

| Claim | Best tier | Median tier adjustment |
|-------|-----------|----------------------|
| C1 (mask discovery) | exact PPL match (11.96=11.96) | delta 0.15-0.28, gradient coupling ~1-3%, ARC-c delta 2.1-2.9pp |
| C2 (SPON weak) | 不变 | 不变（actual data 已在 median range） |
| C3 (regime) | sharp phase transition | approximate transition, 35% ±0.2 noise, 0 violations but near-boundary uncertainty |
| BCE 30% | gap 2.42 | gap 1.18 (BCE improves to 10.0) |
| Reviewer score | 4.0+ | 3.5-4.0, 1-2 incremental concerns |

Median tier 的最大风险是 **Claim 1 的 framing**：从 "sole driver" 降级到 "dominant driver" 会削弱 novelty claim，需要 per-task analysis (ARC-c gradient coupling sensitivity) 来补偿，否则 reviewer 会认为 "gradient coupling 虽小但 non-zero 就说明 your decomposition isn't clean"。防御策略：承认 coupled gradient 有 marginal discovery advantage，但 target quality 是 actionable insight（实际部署不需要关心 gradient pathway，只需要好的 targets）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3382a40d-d4d0-4afa-920c-c2aa450bc0a3",
  "isSidechain": false,
  "requestId": "req_011CbATHCBhjucAQU6htNwq6",
  "type": "assistant",
  "uuid": "9862a6c1-f437-406d-a2a2-7af674eae3ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DukX6kLEuEVRSA5LQBzARs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8862,
      "cache_read_input_tokens": 49525,
      "output_tokens": 35962,
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
          "output_tokens": 35962,
          "cache_read_input_tokens": 49525,
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1 基本复现但非 exact match，gradient coupling 贡献小但非零；regime 数据有噪声但趋势成立 核心假设：['C1 s123 PPL delta 0.1-0.4: BCE+KL-targets 略差于 KL，gradient coupling 贡献 ~3-8%', 'C1…",
  "leafUuid": "9862a6c1-f437-406d-a2a2-7af674eae3ee",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "KL sparsity predictor evaluation and regime analysis",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1 基本复现但非 exact match，gradient coupling 贡献小但非零；regime 数据有噪声但趋势成立 核心假设：['C1 s123 PPL delta 0.1-0.4: BCE+KL-targets 略差于 KL，gradient coupling 贡献 ~3-8%', 'C1…",
  "leafUuid": "9862a6c1-f437-406d-a2a2-7af674eae3ee",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "KL sparsity predictor evaluation and regime analysis",
  "sessionId": "775b9155-5849-4903-92f4-000797d3a8af"
}
```

---
