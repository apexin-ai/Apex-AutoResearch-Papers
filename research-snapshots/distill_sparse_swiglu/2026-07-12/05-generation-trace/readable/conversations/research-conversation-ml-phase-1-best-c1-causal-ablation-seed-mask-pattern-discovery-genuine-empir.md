# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：C1 causal ablation 跨 seed 完美复现，mask pattern discovery 叙事被审稿人接受为genuine empir

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/1c9ff59b-1d42-455e-a00d-3eea90aa1013.jsonl`
- **Structured JSON:** [`60cc730981ea5ee846cc.json`](../../sessions/60/60cc730981ea5ee846cc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T17:36:45.091Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T17:36:45.091Z",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：C1 causal ablation 跨 seed 完美复现，mask pattern discovery 叙事被审稿人接受为genuine empirical finding\n核心假设：['C1 s123 复现 exact match: BCE+KL-targets PPL 与 KL PPL delta < 0.05 (50% uniform)', 'C1 s123 downstream 4 task delta 均 < 1.5pp', '6-point regime curve 单调且无 outlier，regime 边界清晰可读', 'BCE 30% forced top-k PPL ≥ 10.5，与 KL 30% uniform (8.82) 保持 ≥ 1.5 PPL gap', '14B MMLU limitation 被审稿人视为 honest negative finding 而非 fatal flaw', '审稿人接受 53% mask divergence + causal ablation 作为 novelty 支撑，不再视为 incremental']\n关键指标范围：{'c1_ppl_delta_s123': [0.0, 0.05], 'c1_downstream_max_delta_pp': [0.0, 1.5], 'kl30_uniform_ppl_3seed_mean': [8.75, 8.9], 'kl30_uniform_mmlu_3seed_mean': [0.39, 0.43], 'kl30_uniform_mmlu_3seed_std': [0.005, 0.015], 'bce_30pct_forced_topk_ppl': [10.5, 12.0], 'regime_curve_monotonicity_violations': [0, 0], 'reviewer_avg_score': [4.0, 4.5]}\n叙事方向：原始 framing 完全成立。Headline: \"KL discovers fundamentally different neuron importance (53% divergence); causal ablation confirms target quality as sole driver (PPL exact match across 2 seeds, downstream <1.5pp across all tasks)。\" Claim 1 用 \"sole driver\" 措辞。 Claim 3 的 6-point regime curve 提供 deployment guideline。14B 作为 scale-dependent caveat 放在 Discussion。论文定位为 empirical discovery paper，不是 engineering contribution。 目标 EMNLP Main，分数 4.0+。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: distill_sparse_swiglu\nfocus: 测试 'mask pattern discovery' 叙事的审稿接收度。核心 reframe: C1 causal ablation 证明 target quality（不是 gradient coupling）是 KL 优势的唯一驱动力。BCE+KL-targets PPL = 11.9638 = KL PPL 11.9638（exact match at 50% sparsity, TEAL uniform）。53% mask divergence 作为新发现。包含 6-point sparsity regime analysis。目标 4.0 Main Conference。\n\n## paper_framing.md\n\n# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 across **both PPL and all downstream tasks**. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). **Downstream confirmation (full-spectrum)**: All 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) also match within <1pp delta, confirming gradient coupling = 0 across PPL + reasoning + knowledge + math dimensions. Standard BCE (magnitude masks) PPL ≈ 22.51. Target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from \"engineering a better loss\" to \"discovering that output-distribution distillation reveals hidden neuron importance structure.\" **Supporting evidence**: (a) Iso-compute ablation: BCE with 2.71× more FLOPs still PPL=27.97 vs KL=12.00, confirming the gap is structural; (b) BCE at recommended 30% operating point (D062): forced TEAL top-k PPL=11.24 vs KL=8.82, Δ=2.42 — BCE 30% is nearly as bad as KL 50% (11.80), meaning BCE's inferior masks waste ~20pp of sparsity budget; (c) BCE Lagrangian failure at 30%: BCE loss scale (~0.6) vs KL (~0.0001) causes same Lagrangian to fail; (d) No compensation needed: KL eliminates 67.2M compensation parameters (~256MB). **Anticipated attack**: \"Two-stage training (KL→oracle→BCE) avoids needing KL predictor at inference?\" Defense: KL predictor is contextual (per-input adaptive); oracle masks are fixed. Deployment requires per-input sparsity adaptation. **Remaining caveat**: Single seed (s42); C1 s123 in progress for statistical robustness. (Headline claim, resolves persistent R3-R8 confound)\n\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \"subsuming\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)\n\n3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports \"PPL is a poor proxy for downstream quality\" narrative. **6-point PPL regime curve (D063)**: 30%=8.82, 35%=9.31, 40%=10.12, 45%=10.80, 50%=11.80 (TEAL global). Smooth monotonic increase from 30-50%, providing dense sampling for regime boundary identification. 25% eval pending. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.\n\n- **Our framing / headline question**: \"What does KL distillation actually learn for SwiGLU sparsity prediction, and why do its masks differ fundamentally from magnitude-based oracles?\" The theoretical grounding (§3.6, suggestive): BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm. This provides intuition for how KL *can* discover joint interaction patterns. The C1 causal ablation (§4.4) then empirically confirms: the masks KL discovers, not the gradient pathway itself, are what matter.\n\n- **Headline result template**: \"KL-trained sparsity predictors discover neuron importance patterns that diverge 53% from magnitude-based masks. A causal ablation confirms that these mask patterns, not gradient coupling, drive KL's quality advantage: BCE trained on KL-derived masks matches KL performance exactly across PPL (11.96 = 11.96) and all downstream tasks (delta <1pp on ARC-c, WinoGrande, MMLU, GSM8K). This finding eliminates the need for 67.2M compensation parameters and reveals three sparsity operating regimes (now with 6 data points) with qualitatively different allocation requirements.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: **Substantially mitigated by C1 finding**. The 53% mask divergence and causal ablation are genuine empirical discoveries, not engineering contributions. No prior work has shown that KL-derived masks encode fundamentally different neuron importance from magnitude-based approaches. The paper now contributes a finding (mask pattern discovery) rather than just a method (combining known techniques). Additional support: formal decomposition framework, quantitative s^2 prediction, three-regime analysis.\n\n2. **\"KL wins only because more compute\"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 (plan_009, GQA + sliding window) and Qwen-2.5-14B cross-scale validation (D048/D054). **14B mixed result**: KL PPL advantage preserved (7.62 vs TEAL 8.73, 1.47× dense ratio identical to 8B), but KL MMLU=63.72% (global) / 64.49% (uniform) significantly trails TEAL 71.83% (global). Uniform allocation does not fix this gap (D054). PPL-downstream disconnect at 14B scale is an honest limitation, not hidden. Framing: KL's coupled gradient captures output-distribution fidelity (PPL) across scales, but 14B knowledge-intensive tasks (MMLU) show scale-dependent sensitivity that warrants further investigation.\n\n5. **\"Effect size may not hold on downstream tasks\"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.\n\n6. **\"Unfair comparison: BCE+comp close to KL but at higher inference cost\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- **Novelty upgraded from R8**: C1 causal ablation + 53% mask divergence finding elevates paper from \"systematic composition\" to \"empirical discovery about what KL learns for sparsity prediction.\" This addresses the persistent R3-R8 novelty concern and moves the paper toward Main Conference territory (target 4.0).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:\n    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline\n    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds\n    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and\n    BCE-only 3 seeds (mvp_bce_s42/s123/s456).\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_ids:\n  - mvp_kl_norm_v2_s42\n  - mvp_kl_norm_v2_s123\n  - mvp_kl_norm_v2_s456\n  - mvp_bce_s42\n  - mvp_bce_s123\n  - mvp_bce_s456\n  remaining_runs:\n  - KL-only 2 additional seeds (s0, s1) for 5-seed headline\n  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)\n  - KL+comp 3 seeds (s42, s123, s456)\n  registry_id: kl_only_s1\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- id: plan_002\n  claim: 1\n  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).\n    Isolates whether KL advantage comes from loss function or relaxation method. 3\n    seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: ste_baseline_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- id: plan_003\n  claim: 1\n  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs\n    (KL requires full forward pass for output logits, BCE can use cached targets).\n    Report per-step FLOPs and total training time for both. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: bce_isocompute_v2_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- id: plan_004\n  claim: 2\n  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL\n    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,\n    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: spon_2048_s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- id: plan_005\n  claim: 2\n  description: 'SPON subsumption verification: output-space linearity test showing\n    KL predictor already captures SPON correction signal. ||Delta_logits(s+c) - Delta_logits(s)\n    - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality analysis.\n    Proves SPON+KL ≈ KL (no additive gain). 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  - plan_004\n  registry_id: plan_005_subsumption_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- id: plan_006\n  claim: 1\n  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:\n    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),\n    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free\n    < static-learned < contextual-learned.\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_ids:\n  - training_free_baselines\n  - training_free_wina_greedy\n  registry_id: training_free_baselines\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2\n    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor\n    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto\n    frontier plot.\n\n    '\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  - plan_004\n  - plan_005\n  - plan_006\n  registry_id: bench_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- id: plan_008\n  claim: 3\n  description: '3-level sparsity sweep (30%/50%/70%): KL-only vs BCE-only. Test scaling\n    trend and KL-BCE delta growth. 1 seed per level (sweep analysis, not headline).\n    50% data point reused from plan_001. If 3 levels show non-linear inflection, add\n    intermediate points.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  registry_id: d030_kl50_uniform\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- id: plan_009\n  claim: 1\n  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%\n    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds\n    each condition.\n\n    '\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: lm_eval_mistral_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions\n    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:\n    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization\n    beyond short training sequences.\n\n    '\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 2\n  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8\n    categories. All conditions. Tests instruction-following quality under sparsity.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative\n    task types. Fine-grained capability diagnostics complementing LongBench.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_total_loss: 3.3438\n    final_kl_loss: 3.2969\n    final_reg_loss: 0.05\n    final_sparsity: 0\n    steps: 1000\n    tau_final: 0.1\n    wikitext2_ppl_dense: 6.12\n    wikitext2_ppl_sparse: 455.93\n    wikitext2_ppl_increase_pct: 7349\n    model_level_sparsity: 0.372\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\n- exp_id: mvp_kl_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_kl_s456\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_bce_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 27.9603\n    teal_sparse_ppl: 44.537\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 628\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.3817\n    teal_sparse_ppl: 44.5864\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 629\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.1437\n    teal_sparse_ppl: 43.033\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 603.3\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_lagrangian_quicktest\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_kl_loss: 418\n    final_constraint_loss: 1.211\n    final_sparsity: 0.141\n    final_lambda: 5.06\n    steps: 200\n    sparsity_trajectory:\n    - 0.406\n    - 0.387\n    - 0.289\n    - 0.168\n    - 0.141\n- exp_id: kl_lagrangian_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_normalized_quicktest\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step1_kl: 1.18\n    step200_kl: 0.641\n    step200_sparsity: 0.504\n    final_lambda: 8\n    sparsity_converged_step: 80\n    sparsity_trajectory:\n    - 0.406\n    - 0.398\n    - 0.398\n    - 0.457\n    - 0.52\n    - 0.506\n    - 0.504\n    - 0.504\n    lambda_trajectory:\n    - 1\n    - 2\n    - 4\n    - 8\n    - 8\n    - 8\n    - 8\n    - 8\n- exp_id: mvp_kl_norm_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_norm_v3_quicktest\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics:\n    step1_kl_raw: 1.1797\n    step1_kl_norm: 1.1797\n    step1_sparsity: 0.406\n    step1_lambda: 2\n    step50_kl_raw: 0.7344\n    step50_kl_norm: 0.7344\n    step50_sparsity: 0.514\n    step50_lambda: 1.95\n    step100_kl_raw: 0.625\n    step100_kl_norm: 0.625\n    step100_sparsity: 0.496\n    step100_lambda: 1000\n    step150_kl_raw: 0.5703\n    step150_kl_norm: 0.5703\n    step150_sparsity: 0.48\n    step150_lambda: 1000\n    step200_kl_raw: 0.6836\n    step200_kl_norm: 0.6836\n    step200_sparsity: 0.477\n    step200_lambda: 1000\n    step200_constraint: 0.01178\n    kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)\n    sparsity_range: 0.477-0.514 after step 50\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\n- exp_id: mvp_kl_norm_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2142\n    teal_sparse_ppl: 12.0776\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 97.4\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2474\n    teal_sparse_ppl: 11.9128\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 94.7\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.14\n    teal_sparse_ppl: 13.58\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 121.9\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_only_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.19\n    teal_sparse_ppl: 12.03\n    model_level_sparsity: 0.499\n    ppl_increase_vs_true_dense_pct: 96.57\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: kl_only_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- exp_id: spon_training\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1193\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 9.0977\n    spon_recovery_pct: 3.8\n    ppl_improvement_from_spon: 0.1188\n    ppl_increase_vs_true_dense_pct: 48.7\n    ppl_increase_no_spon_vs_true_dense_pct: 50.6\n    mean_bias_norm: 0.040596\n    max_bias_norm: 0.054199\n    teal_sparse_ppl: 12.08\n    teal_with_spon_ppl: 11.93\n    spon_dense_ppl_degradation: 6.19\n    model_level_sparsity: 0.5\n    eval_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n- exp_id: spon_kl_s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: bce_comp_staged_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 25.44\n    predictor_hard_mask_ppl_no_comp: 27.96\n    teal_sparse_ppl: 44.54\n    model_level_sparsity: 0.558\n    ppl_increase_vs_true_dense_pct: 315.7\n    comp_loss_final: 0.0033\n    bce_loss_final: 0.6379\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: training_free_baselines\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- exp_id: spon_training_seq2048\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: ste_baseline_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- exp_id: spon_2048_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- exp_id: ste_kl_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: training_free_wina_greedy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wina_greedy_ppl: 2126.03\n    dense_ppl: 6.12\n    model_level_sparsity: 0.5\n    eval_dataset: WikiText-2\n    eval_seq_len: 2048\n    greedy_allocation_summary: 'layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80,\n      layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24:\n      0.05-0.15, layers 25-31: 0.00'\n- exp_id: bce_isocompute_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_spon_supp_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: spon_supp_eval_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- exp_id: plan_005_subsumption_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- exp_id: kl_sparsity30_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity70_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_loss: 0.1465\n    kl_normalized: 0.1465\n    kl_raw: 0.1465\n    model_level_sparsity: 0.281\n    sparsity_target: 0.3\n    lambda_sparse_final: 1000\n    lambda_max_cap: 1000\n    tau_final: 0.1\n    constraint_loss_final: 0\n    training_steps: 1000\n    wall_clock_seconds: 2662.6\n    gpu_hours: 0.74\n    note: No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1).\n      Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run\n      was offline (not synced).\n- exp_id: kl_sparsity70_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 13.84\n    predictor_teal_sparse_ppl: 17.91\n    vanilla_teal_sparse_ppl: 100.11\n    teal_sparse_ppl: 17.91\n    teal_sparse_ppl_static_baseline: 17.91\n    model_level_sparsity: 0.7\n    teal_sparse_note: '17.91 = predictor-based TEAL (teal_global_masks: predictor-gated\n      magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py\n      L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct\n      metadata 有误导性.'\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    per_layer_sparsity_range:\n    - 0.508\n    - 0.876\n- exp_id: kl_sparsity30_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    loss: 0.165\n    kl_normalized: 0.165\n    kl_raw: 0.165\n    sparsity: 0.285\n    lambda_sparse: 5000\n    tau: 0.1\n    constraint_loss: 0\n    steps: 1000\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    teal_sparse_ppl_note: 已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\n    model_level_sparsity: 0.3\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n- exp_id: mistral_kl_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_final_loss: 0.2188\n    train_final_kl_raw: 0.2188\n    train_final_kl_norm: 0.2188\n    train_final_constraint: 0\n    train_final_sparsity: 0.48\n    train_final_lambda: 1000\n    train_final_tau: 0.1\n    train_steps_completed: 1000\n    true_dense_ppl: 5.52\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    model_level_sparsity: 0.5\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_samples: 159\n- exp_id: lm_eval_dense_test\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc_norm: 0.3771\n    winogrande_acc: 0.6156\n    mmlu_acc: 0.2591\n    gsm8k_exact_match: 0.0121\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: kl_sparse_50pct\n    server: westd-34887\n    exit_code: 129\n    wall_time_sec: 3010\n    flag: SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\n- exp_id: lm_eval_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.5819\n    winogrande_acc: 0.7814\n    mmlu_acc: 0.6532\n    gsm8k_exact_match: 0.5004\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: dense\n    server: westd-34887\n- exp_id: lm_eval_mistral_downstream\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_mistral_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- exp_id: diag_30pct_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_gsm8k_gencomp\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_teal_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: lm_eval_kl_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.3575\n    arc_challenge_acc_norm: 0.3737\n    winogrande_acc: 0.6756\n    mmlu_acc: 0.2874\n    gsm8k_exact_match_strict: 0.0743\n    gsm8k_exact_match_flexible: 0.0781\n    actual_sparsity: 0.3\n    model: llama-3.1-8b\n    condition: kl_distill_30pct_sparsity_s42\n    mmlu_stem_acc: 0.2499\n    mmlu_social_sciences_acc: 0.2896\n    mmlu_humanities_acc: 0.2786\n    mmlu_other_acc: 0.3363\n- exp_id: gsm8k_gen_compare\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: lm_eval_teal_50pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: vanilla_teal\n    sparsity: 0.5\n    actual_sparsity: 0.5\n    arc_challenge_acc_norm: 0.291\n    winogrande_acc: 0.5556\n    mmlu_acc: 0.2856\n    gsm8k_exact_match_flexible: 0.019\n    gsm8k_exact_match_strict: 0.0114\n    arc_challenge_drop_vs_dense: -0.5\n    winogrande_drop_vs_dense: -0.289\n    mmlu_drop_vs_dense: -0.563\n    gsm8k_drop_vs_dense: -0.962\n    model: Llama-3.1-8B\n    condition: TEAL 50% training-free sparsity\n- exp_id: lm_eval_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge:\n      acc: 0.3933\n      acc_norm: 0.4155\n      acc_stderr: 0.0143\n      acc_norm_stderr: 0.0144\n    winogrande:\n      acc: 0.6559\n      acc_stderr: 0.0134\n    mmlu:\n      acc: 0.3598\n      acc_stderr: 0.004\n    mmlu_stem:\n      acc: 0.313\n    mmlu_humanities:\n      acc: 0.3305\n    mmlu_social_sciences:\n      acc: 0.4108\n    mmlu_other:\n      acc: 0.401\n    gsm8k:\n      exact_match_strict: 0.0849\n      exact_match_flexible: 0.0925\n      strict_stderr: 0.0077\n      flexible_stderr: 0.008\n    actual_sparsity: 0.3\n- exp_id: lm_eval_mistral_kl_50pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.2927\n    arc_challenge_acc_norm: 0.3183\n    arc_challenge_acc_norm_stderr: 0.0136\n    winogrande_acc: 0.629\n    winogrande_acc_stderr: 0.0136\n    mmlu_acc: 0.2295\n    mmlu_acc_stderr: 0.0035\n    mmlu_stem_acc: 0.2125\n    mmlu_humanities_acc: 0.2421\n    mmlu_social_sciences_acc: 0.2171\n    mmlu_other_acc: 0.2398\n    gsm8k_exact_match_strict: 0.0045\n    gsm8k_exact_match_flexible: 0.0212\n    model: Mistral-7B-v0.3\n    condition: kl_distill_50pct_sparsity_s42\n    arc_challenge_retention_vs_dense: 0.528\n    winogrande_retention_vs_dense: 0.799\n    mmlu_retention_vs_dense: 0.368\n    gsm8k_retention_vs_dense: 0.012\n- exp_id: d030_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n    allocation: uniform\n    per_layer_sparsity: uniform 0.301 across all 32 layers\n    mmlu_improvement_vs_global: +11.87pp (0.2874 → 0.4061)\n    gsm8k_change_vs_global: no change (0.0743 → 0.0735, within noise)\n- exp_id: bce_isocompute_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 2700\n    loss: 0.6382\n    bce_loss: 0.6371\n    reg_loss: 0.001\n    sparsity: 0.51\n    training_time_seconds: 2828\n    note: 'BCE saturation confirmed: step 500→2700 only 0.006 improvement'\n- exp_id: bench_mistral_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: d030_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- exp_id: bench_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- exp_id: eval_kl30_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    sparsity_target: 0.3\n    actual_sparsity: 0.3\n- exp_id: d030_kl40_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3627\n    arc_challenge_acc_norm: 0.4181\n    winogrande_acc: 0.6717\n    mmlu_acc: 0.3068\n    gsm8k_exact_match: 0.0394\n    actual_sparsity: 0.398\n- exp_id: eval_bce_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 22.51\n    teal_sparse_ppl: 27.97\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2048\n    arc_challenge_acc_norm: 0.2398\n    arc_challenge_acc_norm_stderr: 0.0125\n    winogrande_acc: 0.5059\n    winogrande_acc_stderr: 0.0141\n    mmlu_acc: 0.3002\n    mmlu_acc_stderr: 0.0038\n    gsm8k_exact_match: 0.0485\n    gsm8k_exact_match_strict: 0.0425\n    gsm8k_exact_match_stderr: 0.0059\n- exp_id: bench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n- exp_id: bench_kl50_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n    actual_sparsity: 0.5\n- exp_id: bench_kl30_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    arc_challenge_acc_norm: 0.3968\n    winogrande_acc: 0.7017\n    mmlu_acc: 0.2527\n    gsm8k_exact_match: 0.0879\n    actual_sparsity: 0.3\n- exp_id: bench_teal30\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.97\n    arc_challenge_acc_norm: 0.4232\n    winogrande_acc: 0.6606\n    mmlu_acc: 0.3861\n    gsm8k_exact_match: 0.0788\n    actual_sparsity: 0.3\n- exp_id: bench_teal50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 23.31\n    arc_challenge_acc_norm: 0.2841\n    winogrande_acc: 0.5304\n    mmlu_acc: 0.2832\n    gsm8k_exact_match: 0.0197\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.963\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: bench_kl40_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.117\n    arc_challenge_acc_norm: 0.4096\n    winogrande_acc: 0.6535\n    mmlu_acc: 0.3806\n    gsm8k_exact_match: 0.05\n    actual_sparsity: 0.4\n- exp_id: longbench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v5\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: latency_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpu_model: NVIDIA RTX PRO 6000 Blackwell Server Edition\n    dtype: float16\n    attn: flash_attention_2\n    batch: 1\n    seq_len: 2048\n    warmup: 10\n    iters: 100\n    dense_ms: 119.11\n    dense_std: 0.57\n    dense_tokens_per_s: 17194.5\n    kl_30pct_ms: 126.64\n    kl_30pct_std: 0.7\n    kl_30pct_tokens_per_s: 16171.8\n    kl_30pct_speedup: 0.941\n    kl_50pct_ms: 126.78\n    kl_50pct_std: 0.31\n    kl_50pct_tokens_per_s: 16154.2\n    kl_50pct_speedup: 0.939\n    comp_30pct_ms: 129.94\n    comp_30pct_std: 0.75\n    comp_30pct_tokens_per_s: 15761.4\n    comp_30pct_speedup: 0.917\n    comp_50pct_ms: 129.71\n    comp_50pct_std: 0.53\n    comp_50pct_tokens_per_s: 15788.8\n    comp_50pct_speedup: 0.918\n    predictor_overhead_ms: 3.17\n    predictor_overhead_pct: 2.7\n    per_layer_predictor_ms: 0.099\n    dense_ffn_per_layer_ms: 2.427\n    sparse_ffn_pred_per_layer_ms: 2.686\n    compensation_overhead_ms: 3.3\n- exp_id: bench_kl50_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.83\n    arc_challenge_acc_norm: 0.3515\n    winogrande_acc: 0.6298\n    mmlu_acc: 0.2751\n    gsm8k_exact_match: 0.0235\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9604\n    arc_challenge_acc_norm: 0.3345\n    winogrande_acc: 0.6275\n    mmlu_acc: 0.2874\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: longbench_dense_v6\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    longbench_narrativeqa: 7.3\n    longbench_qasper: 13.4\n    longbench_gov_report: 30.5\n    longbench_multi_news: 2.5\n- exp_id: longbench_kl30_uniform_v6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    longbench_narrativeqa: 4.12\n    longbench_qasper: 6.23\n    longbench_gov_report: 16.97\n    longbench_multi_news: 18.01\n    runtime_seconds: 6156.6\n- exp_id: eval_c4_ood_kl50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 9.2075\n    kl_50_global_ppl: 18.401\n    teal_50_ppl: 38.7503\n    kl_vs_dense_ratio: 2\n    teal_vs_dense_ratio: 4.21\n- exp_id: db_sensitivity_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    db64_per_token_ppl: 10.158\n    db64_teal_global_ppl: 12.076\n    db64_sparsity: 0.5\n    db64_loss: 0.361\n    db128_teal_global_ppl: 11.963\n    db128_per_token_ppl: 9.218\n    db256_per_token_ppl: 8.586\n    db256_teal_global_ppl: 12.105\n    db256_sparsity: 0.5\n    db256_loss: 0.27\n    db512_per_token_ppl: 7.933\n    db512_teal_global_ppl: 12.315\n    db512_sparsity: 0.5\n    db512_loss: 0.224\n    best_teal_global_db: 128\n    best_teal_global_ppl: 11.963\n- exp_id: bce_gumbel_lagrangian_isolation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lr_1e4_ppl: 42.99\n    lr_1e3_ppl: 48.4\n    lr_3e3_ppl: 38.02\n    lr_1e4_bce_loss: 0.7158\n    lr_1e3_bce_loss: 0.6781\n    lr_3e3_bce_loss: 0.6632\n    lr_1e4_sparsity: 0.514\n    lr_1e3_sparsity: 0.506\n    lr_3e3_sparsity: 0.504\n    best_ppl: 38.02\n    best_lr: 3e-3\n    kl_baseline_ppl: 11.79\n    gap_vs_kl: 26.23\n- exp_id: steps_curve_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: tau_schedule_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tau_linear_baseline_ppl: 11.963\n    tau_fixed05_ppl: 11.861\n    tau_fixed01_ppl: 12.072\n    tau_fixed05_loss: 0.248\n    tau_fixed01_loss: 0.43\n    best_tau: fixed_0.5\n    ppl_range: 0.211\n- exp_id: steps_curve_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    step200_ppl: 15.158\n    step400_ppl: 12.538\n    step600_ppl: 12.046\n    step800_ppl: 11.907\n    step1000_ppl: 11.906\n    convergence_step: 800\n    ppl_800_vs_1000_delta: 0.001\n- exp_id: mistral_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 6.048\n    kl_teal_global_ppl: 6.7733\n    teal_baseline_ppl: 8.3807\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 1.386\n    ppl_vs_dense_pct: 9.5\n- exp_id: mistral_kl70_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 9.1086\n    kl_teal_global_ppl: 13.3254\n    teal_baseline_ppl: 61.716\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 6.77\n    final_loss: 0.3945\n    actual_sparsity: 0.682\n- exp_id: mistral_teal50_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_baseline_ppl: 18.3061\n    dense_ppl: 5.5238\n    teal_vs_dense_ratio: 3.31\n- exp_id: bench_kl70_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 17.91\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: kl_sparsity70_s42_v2 (teal_global_masks protocol)\n    vanilla_teal_ppl: 100.11\n- exp_id: bench_teal70\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 100.11\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: training_free_baselines experiment (vanilla teal global)\n- exp_id: gradient_snr_kl_vs_bce\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 5.77e-05\n    bce_avg_snr: 1.0e-05\n    snr_ratio: 5.76\n    early_layer_ratio_range: 34-156x\n    late_layer_ratio_range: 2-4x\n- exp_id: natural_sparsity_floor_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    always_pruned_ratio: 0.0006\n    always_pruned_count: 278\n    total_neurons: 458752\n    late_layer_max_ratio: 0.0051\n    threshold: 0.1\n- exp_id: teal_kl_overlap_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_jaccard: 0.396\n    divergence_ratio: 0.433\n    kl_only_pruned_magnitude_ratio: 1.48\n    teal_only_pruned_mean_gate_prob: 0.614\n    min_jaccard_layer: L17-L18 (0.19)\n    max_jaccard_layer: L26-L28 (0.55)\n- exp_id: gradient_snr_constrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 0.000545\n    bce_avg_snr: 5.28e-06\n    snr_ratio: 103.2\n    kl_final_sparsity: 0.508\n    bce_final_sparsity: 0.591\n    steps: 200\n- exp_id: sparsity_floor_extended\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    floor_30pct: 0.0499\n    floor_50pct: 0.0726\n    floor_70pct: 0.1936\n    late_layer_max_30: 0.4604\n    late_layer_max_50: 1.2347\n    late_layer_max_70: 4.3666\n    threshold: 0.1\n    seq_len: 2048\n    num_samples: 50\n- exp_id: teal_kl_overlap_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_score: 7260.3\n    p_value: 0\n    median_percentile_rank: 78.6\n    iqr_q1: 64.4\n    iqr_q3: 89.1\n    layers_significant: 31/32\n    exception_layer: 31\n- exp_id: mag_preservation_reg\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: reverse_kl_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.8\n    vs_forward_kl: +1.01 (+8.6%)\n    sparsity: 0.5\n- exp_id: jsd_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.54\n    vs_forward_kl: +0.75 (+6.4%)\n    sparsity: 0.5\n- exp_id: global_30pct_retention\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    early_retention: 0.771\n    middle_retention: 0.764\n    knowledge_L12_20_retention: 0.797\n    late_L24_31_retention: 0.501\n    L31_retention: 0.284\n    L30_retention: 0.366\n    starved_layers: L27-L31\n- exp_id: kl_bce_f1_oracle\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bce_f1: 0.6128\n    bce_precision: 0.6132\n    bce_recall: 0.6124\n    kl_f1: 0.5397\n    kl_precision: 0.5112\n    kl_recall: 0.5715\n    random_f1: 0.5\n    kl_ppl: 11.79\n    bce_ppl: 22.51\n- exp_id: kl50_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.745\n    arc_challenge: 0.3814\n    winogrande: 0.6125\n    mmlu: 0.2752\n    gsm8k: 0.0281\n- exp_id: kl30_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8308\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.6938\n    mmlu_acc: 0.3944\n    gsm8k_exact_match: 0.0751\n    actual_sparsity: 0.3\n    allocation: uniform\n- exp_id: kl50_s456_train_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl50_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.397\n    final_kl_normalized: 0.397\n    final_sparsity: 0.492\n    final_lambda: 5000\n    final_tau: 0.1\n    steps_completed: 1000\n- exp_id: kl_50pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.745\n    arc_challenge_acc_norm: 0.3814\n    winogrande_acc: 0.6125\n    mmlu_acc: 0.2752\n    gsm8k_exact_match: 0.0281\n    sparsity: 0.5\n    allocation: global\n- exp_id: mistral_dense_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 5.5238\n    model: Mistral-7B-v0.3\n    condition: dense\n    sparsity: 0\n- exp_id: mistral_kl30_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.048\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 0.5242\n- exp_id: mistral_kl50_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.2931\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 1.7693\n- exp_id: mistral_kl70_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 9.1086\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 3.5848\n- exp_id: mistral_kl30_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.7733\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 1.2495\n- exp_id: mistral_kl50_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.6489\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 3.1251\n- exp_id: mistral_kl70_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 13.3254\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 7.8016\n- exp_id: mistral_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3807\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 2.8569\n- exp_id: mistral_teal70_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 61.716\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 56.1922\n- exp_id: kl30_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.2021\n    actual_sparsity: 0.289\n    constraint_satisfied: true\n    training_steps: 1000\n- exp_id: kl_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9748\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.693\n    mmlu_acc: 0.3807\n    gsm8k_exact_match: 0.0758\n    sparsity: 0.3\n    allocation: global\n- exp_id: kl50_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.8057\n    arc_challenge: 0.3319\n    winogrande: 0.6488\n    mmlu: 0.2794\n    gsm8k: 0.0212\n- exp_id: kl30_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9332\n    arc_challenge: 0.4633\n    winogrande: 0.7111\n    mmlu: 0.4382\n    gsm8k: 0.0758\n- exp_id: kl30_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4198\n    ppl_uniform: 8.7947\n    arc_challenge: 0.4505\n    winogrande: 0.6875\n    gsm8k: 0.0758\n- exp_id: qwen14b_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 6.8\n    teal_global_ppl: 7.62\n    ppl_ratio_hard_mask: 1.31\n    ppl_ratio_teal: 1.47\n    final_loss: 0.3398\n    training_sparsity: 0.281\n    teal_sparsity: 0.3\n    lambda: 5000\n    steps: 1000\n- exp_id: qwen14b_kl30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.6232\n    arc_challenge_acc_norm: 0.5717\n    winogrande_acc: 0.7206\n    mmlu_acc: 0.6372\n    gsm8k_exact_match: 0.4882\n- exp_id: downstream_extended_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.727\n    hellaswag_acc: 0.527\n    piqa_acc_norm: 0.7595\n    piqa_acc: 0.747\n    boolq_acc: 0.7685\n- exp_id: wallclock_speedup_30_50\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    theoretical_flops_speedup_30pct: 1.36\n    theoretical_flops_speedup_50pct: 2.45\n    actual_wallclock_speedup_30pct: 0.91\n    actual_wallclock_speedup_50pct: 0.6\n    predictor_overhead_decode_ms: 1\n    predictor_overhead_prefill_ms: 2\n    actual_mean_sparsity_30pct: 0.28\n    actual_mean_sparsity_50pct: 0.605\n    note: No wall-clock speedup without sparse kernels. Mask-based=0.87-0.94x (predictor\n      overhead), structured-skip=0.45-0.74x (gather overhead). Report theoretical\n      FLOPs in paper.\n- exp_id: qwen14b_bce30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 5.57\n    teal_global_ppl: 8.76\n    ppl_ratio_hard_mask: 1.075\n    ppl_ratio_hard_mask_note: at predictor native 6.4% sparsity, not comparable to\n      KL's 28.1%\n    ppl_ratio_teal: 1.69\n    actual_sparsity_teal: 0.3\n    predictor_native_sparsity: 0.064\n    training_log_sparsity_note: Training Lagrangian failed (predictor sparsity=6.4%).\n      Inference via TEAL forces 30% externally. TEAL PPL 8.76 is valid for method\n      comparison.\n    final_loss: 0.5561\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n- exp_id: qwen14b_teal30_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.7332\n    arc_challenge_acc_norm: 0.5683\n    winogrande_acc: 0.7269\n    mmlu_acc: 0.7183\n    gsm8k_exact_match: 0.4951\n- exp_id: qwen14b_bce30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    predictor_native_sparsity: 0.064\n    lambda_max: 50000\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n    sparsity_trajectory: 49%→5% collapse in 50 steps, no recovery over 950 steps\n    note: 10x stronger Lagrangian produces identical sparsity as v1 (lambda=5000).\n      Confirms BCE gradient insufficiency is fundamental, not constraint strength.\n- exp_id: downstream_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.8233\n    hellaswag_acc_norm_stderr: 0.0038\n    piqa_acc_norm: 0.8074\n    piqa_acc_norm_stderr: 0.0092\n    boolq_acc: 0.8294\n    boolq_acc_stderr: 0.0066\n- exp_id: qwen14b_bce30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 8.7634\n    arc_challenge_acc_norm: 0.5759\n    winogrande_acc: 0.7261\n    mmlu_acc: 0.7167\n    gsm8k_exact_match: 0.5307\n- exp_id: downstream_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc: 0.4878\n    hellaswag_acc_norm: 0.667\n    piqa_acc: 0.7258\n    piqa_acc_norm: 0.7361\n    boolq_acc: 0.685\n- exp_id: kl50_global_s123_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7184\n    arc_challenge_acc_norm: 0.3635\n    winogrande_acc: 0.6109\n    mmlu_acc: 0.2834\n    gsm8k_exact_match: 0.0258\n- exp_id: bce_isocompute_v3_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: bce_isocompute_v3_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6368\n    final_sparsity: 0.51\n    training_steps: 2700\n- exp_id: c4_ood_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0458\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_download\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen14b_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl: 5.1854\n    arc_challenge: 0.6758\n    winogrande: 0.8106\n    mmlu: 0.7977\n    gsm8k: 0.8757\n- exp_id: bce_isocompute_v3_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_sparse_ppl: 28.3503\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2312\n    arc_challenge_acc_stderr: 0.01232\n    arc_challenge_acc_norm: 0.2807\n    arc_challenge_acc_norm_stderr: 0.01313\n    winogrande_acc: 0.5241\n    winogrande_acc_stderr: 0.01404\n    mmlu_acc: 0.2567\n    mmlu_acc_stderr: 0.00367\n    gsm8k_exact_match: 0.022\n    gsm8k_exact_match_stderr: 0.00404\n    gsm8k_exact_match_strict: 0.00834\n    gsm8k_exact_match_strict_stderr: 0.0025\n- exp_id: bce_isocompute_v3_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 28.0627\n    arc_challenge_acc_norm: 0.2696\n    winogrande_acc: 0.513\n    mmlu_acc: 0.2655\n    gsm8k_exact_match: 0.022\n- exp_id: qwen14b_kl30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: qwen14b_teal30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl30_8b_s123_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    sparsity: 0.3\n    training_loss: 0.147\n- exp_id: kl30_8b_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    sparsity: 0.3\n    training_loss: 0.148\n- exp_id: qwen14b_kl30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 7.63\n    mmlu_acc: 0.6449\n    arc_challenge_acc_norm: 0.5444\n    winogrande_acc: 0.7245\n- exp_id: qwen14b_teal30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.01\n    mmlu_acc: 0.6634\n    arc_challenge_acc_norm: 0.5529\n    winogrande_acc: 0.6985\n- exp_id: bce_isocompute_v3_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 27.9696\n    arc_challenge_acc: 0.2346\n    arc_challenge_acc_norm: 0.2765\n    winogrande_acc: 0.5162\n    mmlu_acc: 0.2614\n    gsm8k_exact_match: 0.019\n- exp_id: kl30_8b_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    arc_challenge_acc: 0.4462\n    arc_challenge_acc_norm: 0.4744\n    winogrande_acc: 0.7024\n    mmlu_acc: 0.3836\n    gsm8k_exact_match: 0.0917\n- exp_id: kl30_8b_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc: 0.436\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: snr_extended_r6w3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_snr_step300: 0.0058773\n    bce_snr_step300: 0.00114449\n    snr_ratio_step300: 5.14\n    kl_train_time_s: 641\n    bce_train_time_s: 320\n    num_checkpoints: 7\n    steps_range: 0-300\n- exp_id: c4_ood_kl30_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl50_s123_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.89\n    arc_challenge_acc_norm: 37.88\n    winogrande_acc: 62.19\n    mmlu_acc: 27.75\n    gsm8k_exact_match: 2.35\n    comparison_vs_global_topk:\n      ppl_delta: -0.94\n      arc_c_delta: -5.55\n      wg_delta: -6.71\n      mmlu_delta: -8.2\n      gsm8k_delta: -5\n    note: 'Uniform allocation: better PPL but catastrophic downstream degradation\n      vs global_topk. Confirms global_topk allocation is critical for downstream quality.'\n- exp_id: c4_ood_kl30_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0259\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_ood_dense_baseline_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 9.2075\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: kl50_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8614\n    arc_challenge_acc_norm: 0.3754\n    winogrande_acc: 0.6417\n    mmlu_acc: 0.2784\n    gsm8k_exact_match: 0.0212\n- exp_id: c4_ood_kl50_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.6064\n    allocation: global_topk\n    sparsity: 0.5\n    model: llama-3.1-8b\n- exp_id: downstream_ext_kl50_uniform_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: downstream_ext_kl30_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_kl50_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.9867\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 456\n- exp_id: c4_ood_kl30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0401\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl50_s42_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9638\n    arc_challenge_acc_norm: 0.3259\n    winogrande_acc: 0.6235\n    mmlu_acc: 0.2792\n    gsm8k_exact_match: 0.0197\n- exp_id: c4_ood_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.5297\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 42\n- exp_id: kl_comp_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6992\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.3594\n    - 1.3516\n    - 1.0859\n    - 0.9219\n    - 0.8789\n    - 0.8281\n    - 0.7461\n    - 0.7344\n    - 0.6953\n    - 0.6992\n- exp_id: c4_ood_kl30_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.7617\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.0469\n    - 1.3828\n    - 1.0703\n    - 0.9609\n    - 0.8711\n    - 0.7305\n    - 0.6875\n    - 0.7773\n    - 0.7969\n    - 0.7617\n- exp_id: kl_comp_30pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl_comp_30pct_s42_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl_comp_30pct_s123_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 123\n- exp_id: kl_comp_30pct_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl50_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9538\n    arc_challenge_acc_norm: 0.3831\n    winogrande_acc: 0.6196\n    mmlu_acc: 0.275\n    gsm8k_exact_match: 0.0288\n- exp_id: kl_comp_30pct_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: kl_comp_50pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n- exp_id: kl50_s42_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8038\n    arc_challenge_acc_norm: 0.3336\n    winogrande_acc: 0.6338\n    mmlu_acc: 0.2819\n    gsm8k_exact_match: 0.0167\n- exp_id: kl30_s123_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8186\n    arc_challenge_acc_norm: 0.471\n    winogrande_acc: 0.6961\n    mmlu_acc: 0.3763\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s456_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8284\n    arc_challenge_acc_norm: 0.4505\n    winogrande_acc: 0.6953\n    mmlu_acc: 0.3727\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s123_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl30_s456_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: c1_ablation_bce_kl_targets_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wt2_ppl: 9.29\n    eval_sparsity: 0.609\n    oracle_agreement: 0.978\n    final_bce_loss: 0.0545\n    train_steps: 1000\n    train_time_sec: 877.1\n    reference_kl_ppl: 11.79\n    reference_bce_ppl: 22.51\n- exp_id: bce_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_sparsity25_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_final: 0.1582\n    kl_normalized_final: 0.1582\n    sparsity_actual: 0.23\n    sparsity_target: 0.25\n    lambda_final: 5000\n    tau_final: 0.1\n    steps: 1000\n- exp_id: kl_sparsity35_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.203\n    final_sparsity: 0.336\n    steps: 1000\n- exp_id: c1_ablation_eval_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9638\n    arc_challenge_acc_norm: 0.3217\n    winogrande_acc: 0.6314\n    mmlu_acc: 0.2779\n    gsm8k_exact_match: 0.0205\n    sparsity_target: 0.5\n    allocation: uniform\n- exp_id: kl_sparsity45_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.33\n    final_sparsity: 0.449\n    steps: 1000\n- exp_id: bce_30pct_s42_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity25_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.153\n    final_sparsity: 0.23\n    steps: 1000\n- exp_id: kl_sparsity25_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity35_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity45_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: c1_ablation_bce_kl_targets_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl_sparsity40_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity25_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity35_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity45_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: c1_ablation_bce_kl_targets\n  claim: 'Claim 1: mask pattern discovery'\n  description: BCE trained on KL-derived oracle masks achieves PPL 11.9638 = KL PPL\n    11.9638 at 50% sparsity under identical TEAL protocol. 53% mask divergence from\n    magnitude oracles. Target quality is sole driver of KL advantage.\n  estimated_gpu_hours: 0.0\n- name: dense_sparsity_sweep_6pt\n  claim: 'Claim 3: regime analysis with 6 data points'\n  description: KL predictors at 25%/30%/35%/40%/45%/50% with regime boundaries precisely\n    mapped.\n  estimated_gpu_hours: 0.0\n- name: bce_30pct_forced_topk\n  claim: 'Claim 1: BCE baseline at recommended operating point'\n  description: BCE predictor evaluated at 30% via forced TEAL top-k. Fills Table 2\n    gap.\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T17:36:45.095Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T17:36:45.095Z",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-18T17:36:45.138Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：C1 causal ablation 跨 seed 完美复现，mask pattern discovery 叙事被审稿人接受为genuine empirical finding
核心假设：['C1 s123 复现 exact match: BCE+KL-targets PPL 与 KL PPL delta < 0.05 (50% uniform)', 'C1 s123 downstream 4 task delta 均 < 1.5pp', '6-point regime curve 单调且无 outlier，regime 边界清晰可读', 'BCE 30% forced top-k PPL ≥ 10.5，与 KL 30% uniform (8.82) 保持 ≥ 1.5 PPL gap', '14B MMLU limitation 被审稿人视为 honest negative finding 而非 fatal flaw', '审稿人接受 53% mask divergence + causal ablation 作为 novelty 支撑，不再视为 incremental']
关键指标范围：{'c1_ppl_delta_s123': [0.0, 0.05], 'c1_downstream_max_delta_pp': [0.0, 1.5], 'kl30_uniform_ppl_3seed_mean': [8.75, 8.9], 'kl30_uniform_mmlu_3seed_mean': [0.39, 0.43], 'kl30_uniform_mmlu_3seed_std': [0.005, 0.015], 'bce_30pct_forced_topk_ppl': [10.5, 12.0], 'regime_curve_monotonicity_violations': [0, 0], 'reviewer_avg_score': [4.0, 4.5]}
叙事方向：原始 framing 完全成立。Headline: "KL discovers fundamentally different neuron importance (53% divergence); causal ablation confirms target quality as sole driver (PPL exact match across 2 seeds, downstream <1.5pp across all tasks)。" Claim 1 用 "sole driver" 措辞。 Claim 3 的 6-point regime curve 提供 deployment guideline。14B 作为 scale-dependent caveat 放在 Discussion。论文定位为 empirical discovery paper，不是 engineering contribution。 目标 EMNLP Main，分数 4.0+。


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
  "promptId": "f18b1bc3-3ff5-44be-ac99-348755bdc6db",
  "type": "user",
  "uuid": "ee256277-d71d-4916-b83b-fedbd6a1356e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T17:36:45.136Z_

```json
{
  "parentUuid": "ee256277-d71d-4916-b83b-fedbd6a1356e",
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
  "uuid": "51d14111-66d6-4fb8-83a6-789e002c831a",
  "timestamp": "2026-05-18T17:36:45.136Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T17:36:45.136Z_

```json
{
  "parentUuid": "51d14111-66d6-4fb8-83a6-789e002c831a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "74d5dd94-dd13-4617-a1c1-1a982ea718ba",
  "timestamp": "2026-05-18T17:36:45.136Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1 causal ablation 跨 seed 完美复现，mask pattern discovery 叙事被审稿人接受为genuine empirical finding 核心假设：['C1 s123 复现 exact match: BCE+KL-targets PPL 与 KL PPL delta <…",
  "leafUuid": "74d5dd94-dd13-4617-a1c1-1a982ea718ba",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation mask discovery causal validation",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

### Assistant

_source line 8 · 2026-05-18T17:42:06.885Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for every "planned" experiment in the experiment_plan, based on the "best" tier definition. Let me analyze what's planned vs done.

Looking at the experiment_plan, the experiments with status "planned" are:
- plan_010 (LongBench English subset evaluation)
- plan_011 (MT-Bench evaluation)
- plan_012 (RULER synthetic long-context evaluation)

But the user also mentions "what_if" hypothetical experiments:
- c1_ablation_bce_kl_targets (already partially done - c1_ablation_bce_kl_targets_s42 is DONE, s123 failed)


- dense_sparsity_sweep_6pt (partially done - individual sparsity points exist but need consolidation)
- bce_30pct_forced_topk (needs eval)

And there are many experiments in PREPARING status that haven't been completed yet. Let me check which ones are truly "planned" or in progress. Actually, re-reading the request: "对 experiment_plan 中每个 planned 实验展开详细数据" - this means for each planned experiment in the experiment_plan. I need to go through the experiment_plan systematically and identify which ones have "planned" status, then generate predicted results for those.

Looking at the experiment_plan, plans 001-009 are all done, but plans 010-012 are marked as planned and haven't been executed yet. There are also what_if experiments that need attention, plus several registry entries stuck in PREPARING status without conclusions like the various sparsity evaluations and BCE experiments.

Now I'm thinking through what constitutes a "best" tier result—it requires the causal ablation to reproduce consistently across different random seeds, the mask pattern discovery to be accepted by reviewers, and specific performance metrics to fall within tight ranges like PPL delta between 0.0-0.05 and downstream metrics staying within 0.0-1.5.

Looking at the performance benchmarks I need to hit: KL sparsity at 30% should achieve PPL around 8.75-8.9 and MMLU scores between 0.39-0.43 across three seeds with minimal variance, while the forced top-k variant should land between 10.5-12.0 PPL, and the regime curve needs to show no monotonicity violations with reviewer scores averaging 4.0-4.5.

For the planned experiments, LongBench is tricky since previous attempts either succeeded with weak results or failed entirely, but in the best tier scenario KL should maintain its advantage over baselines even on longer contexts despite some performance drop. MT-Bench will use GPT-4o as the judge for multi-turn evaluation.

Now I'm working through the what_if experiments: the BCE-KL ablation needs reproduction for seed 123 after s42 already showed PPL of 9.29 in training and 11.96 on TEAL uniform, the sparsity sweep is missing the 25% point to complete the six-point curve since I have 30/35/40/45/50, and the forced top-k variant at 30% BCE needs evaluation. I need to construct predictions for all these experiments and the preparing batch.

Looking at the LongBench results more carefully—the KL30 uniform variant shows some odd patterns where multi_news jumps to 18.01 compared to dense's 2.5, while gov_report drops from 30.5 to 16.97. This mixed performance suggests the best tier prediction should account for KL retaining roughly 60-75% of dense performance on most long-context tasks, though the variance here is notable.

For the other benchmarks, I'm sketching out expectations: MT-Bench would likely show KL30 uniform around 6.0-6.5 if dense sits at 7.0-7.5, RULER would demonstrate stronger performance at 4K contexts with acceptable degradation at 16K, and I'm also considering what the BCE-KL ablation from the s123 replication might reveal about the training targets.

Now I'm looking at the sparsity sweep data more carefully—I have measurements at 30%, 40%, and 50%, but I need to fill in the 25% and 35% points to complete the curve, and I'm cross-referencing the exact PPL values across the different configurations to make sure everything aligns.

For the BCE predictor at 30% sparsity using forced top-k selection, I'm expecting it to maintain that substantial gap above the KL baseline while still being significantly worse than KL's performance at the same sparsity level. I also need to track the upcoming evaluations for the BCE variant and the 25% sparsity point.

Now I'm working through which experiments to include in the full YAML output. The user is asking specifically for the planned experiments from the plan list plus the what-if scenarios, but I also need to account for the PREPARING experiments in the registry that feed into these plans. Let me organize this carefully to capture the planned experiments and their dependencies. I'm finishing up the list of sparsity experiments that feed into the what_if predictions. Now I'm looking at the C1 ablation results more carefully—the model trained with BCE and KL targets shows a perplexity of 9.29 under Gumbel hard masking at 60.9% sparsity, but drops to 11.96 when evaluated under TEAL uniform at 50%, with downstream performance across arc, wg, mmlu, and gsm8k showing the expected degradation pattern.

Comparing this directly to the KL model at 50% uniform sparsity, the differences are minimal—perplexity stays identical at 11.96, while downstream metrics shift by less than 1pp across the board, which is well within the acceptable tolerance threshold. I'm now checking whether the s123 replication follows the same pattern.

For the s123 variant, the KL model achieves around 11.89 PPL at 50% uniform, so I need to verify that the C1 ablation matches this within 0.05 PPL. Before I finalize the YAML configuration, I should also account for the sub-experiments in the what_if analysis, particularly the 6-point regime curve that requires TEAL uniform PPL values across different sparsity levels. Looking back at the paper framing notes, I have the baseline curve: 30% gives 8.82, 35% gives 9.31, 40% gives 10.12, 45% gives 10.80, and 50% gives 11.80, showing a smooth monotonic increase.

However, I'm noticing some inconsistency—the framing labels these as "TEAL global" but the 8.82 value at 30% actually matches the uniform benchmark rather than the global one. I need to trace through which exact metrics were used for each point and clarify whether the 6-point curve should use uniform or global evaluations consistently.

Looking at my trained checkpoints, I have sparsity levels at 25%, 35%, and 45% with their corresponding losses, but these still need TEAL evaluation. For the best tier, the 25% point should fall around 8.2-8.5 to maintain monotonicity below the known 30%=8.82 value. I'm sketching out where the intermediate points should land across the full 25-50% range to ensure a smooth, monotonic curve without outliers.

Now I'm double-checking whether the D063 curve uses global or uniform TEAL allocation. The benchmark results confirm that 40% global gives 10.12 and 50% global gives 11.80, so the curve is definitely using global allocation. For my missing 35% and 45% points, I need to predict their TEAL global PPL values to complete the monotonic sequence, starting with an estimate of around 8.1 for the 25% global case. I'm realizing the allocation strategy shifts depending on sparsity level—uniform works better at lower percentages while global dominates at higher ones, which explains why the regime curve shows different values. Rather than getting caught up in which allocation method applies where, I should just use the numbers from D063 and make my predictions based on that framework.

Now I'm laying out the structure for the best-tier results: I need the C1 replication to match exactly with minimal downstream variance, a clean 6-point regime curve showing clear monotonic progression and distinct boundaries, the BCE forced top-k experiment hitting the performance thresholds, and reviewer scores in the 4.0-4.5 range. I'm mapping out the experiments I'd need to run—LongBench and MT-Bench evaluations, RULER testing, the C1 ablation for replication, and a 6-point sparsity sweep starting at 25%.

Writing YAML structure... Looking at the multi_news discrepancy where KL30 scores 18.01 versus dense's 2.5—that's suspicious and suggests either a measurement error or the dense baseline was miscalibrated. The overall dense scores seem unusually low. Based on the clearer patterns in the data, I'm estimating that KL30 uniform should retain around 65-80% of dense performance on average across English tasks, while TEAL30 drops to 40-55% and BCE+comp lands around 45%.

Now examining the actual LongBench benchmarks more carefully—the existing dense scores like narrativeqa at 7.3 and qasper at 13.4 are lower than typical Llama 3.1 8B performance, which usually hits 15-20 F1 on NarrativeQA and 20-30 F1 on Qasper. Despite these baseline inconsistencies, KL30 shows particular strength on QA tasks that require long-range retrieval, so I'll work with the data as it stands to make my best-tier predictions.

Looking at the actual v6 results, the dense model achieves narrativeqa=7.3, qasper=13.4, gov_report=30.5, and multi_news=2.5, while KL30 drops to narrativeqa=4.12, qasper=6.23, gov_report=16.97, and multi_news=18.01—that multi_news discrepancy is odd since KL30 typically underperforms across the board, but here it's actually higher.

Let me project what the best-tier numbers should look like once the eval pipeline is properly fixed. For dense, I'm estimating narrativeqa around 18.5, qasper at 25.3, gov_report at 29.8, multi_news at 26.5, trec few-shot around 65, and code_debug at 35. KL30 uniform should retain roughly 77-84% of dense performance depending on the task, while TEAL30 drops to about 56-57% retention.

I'm being more cautious about these projections though—the LongBench evals have been unstable with v6 results showing unexpected variance. What really matters for the best tier is just demonstrating that KL30 maintains its advantage over TEAL on long-context tasks, regardless of the exact numbers.

For MT-Bench, Llama 3.1 8B dense typically hits around 6.5-7.0, so I'd expect dense at 6.8, KL30 uniform around 6.1 with 90% retention, and TEAL30 dropping to 5.3 at 78% retention.

On RULER's synthetic tasks, the pattern is clear—at 4K, dense gets 95% accuracy while KL30 and TEAL30 fall to 88% and 75% respectively, and that gap widens at 16K where dense maintains 85% but KL30 drops to 72% and TEAL30 to 55%.

For the C1 s123 replication, I'm checking the KL50 uniform results against the expected PPL range and comparing downstream metrics across arc, wg, mmlu, and gsm8k benchmarks. Now I'm looking at the s42 ablation results and comparing them to the s123 baseline. The C1 ablation shows similar performance with negligible deltas across all metrics, all well under the 1.5 percentage point threshold. The KL s42 uniform eval gives me another reference point, and when I calculate the differences between the two s42 runs, the changes are minimal—ppl stays flat while the downstream metrics shift by less than a percentage point. I'm also checking the s123 best tier results to see if the predicted PPL matches the observed value.

For s123, the KL uniform PPL is 11.89 and my C1 prediction is 11.92, which is within the 0.03 margin of error I'm allowing. Looking at the downstream metrics for s123, the deltas between KL uniform and C1 predicted are all under 1.5 percentage points, which validates the approach. Now I'm shifting focus to the BCE 30% forced top-k configuration—at 50% sparsity, BCE gives PPL around 22-28, but at 30% the model should retain more capacity and perform better, though magnitude-based masking is inherently less effective than other approaches.

The paper_framing already documents that BCE at 30% yields PPL of 11.24 compared to KL's 8.82, a gap of 2.42 points. I can see the training run completed but the evaluation is still preparing, so I don't have fresh empirical data to validate this prediction yet.

For the best tier, I'm targeting a PPL range between 10.5 and 12.0 while maintaining at least a 1.5 point gap above KL 30%. The framing's D062 number of 11.24 aligns well with this target.

Now I'm looking at the 6-point regime curve—I have the existing TEAL global measurements at 30%, 40%, and 50%, plus D063's claimed values across five points from 30% to 50%. I need to fill in the 25% point to complete the curve.

I've trained a model with 25% sparsity and got a loss of 0.158, so I'm predicting the best tier PPL for 25% should fall around 8.35—lower than the 30% value of 8.82 but following the monotonic trend. Using D063's measured points and my 25% prediction, the full curve would be: 25%=8.35, 30%=8.82, 35%=9.31, 40%=10.12, 45%=10.80, 50%=11.80.

The spacing between adjacent points shows acceleration starting at 35%, which aligns with the capacity cliff pattern and maintains monotonicity throughout. Now I need to predict the downstream metrics—MMLU, ARC-c, WinoGrande, and GSM8K—at each sparsity level, using the existing measurements from the 30% uniform and 40% global configurations as anchors.

Generating the YAML structure... I'm reviewing the requirement that each prediction needs a result_rationale explaining why we'd get these specific results at the "best" tier. Now I need to finalize the YAML and make sure to include all the sub-experiments under the what_if groups, like the various sparsity sweep configurations with different TEAL settings. Writing YAML configuration... 现在看到 C1 ablation 在 TEAL uniform 50% 下的具体结果，PPL 几乎与 KL baseline 持平（仅差 0.03），但在下游任务上表现不一致——ARC 和 GSM8K 略有下降，而 WinoGrande 小幅提升，oracle agreement 达到 97.6% 说明 BCE predictor 很好地学到了 KL 的 mask 模式。

关键观察是 KL 目标在不同 seed 间学到的神经元重要性景观高度一致，尽管与幅度排序有 53% 的差异，但 mask 重叠度极高，这解释了为什么 C1 能稳定复现 11.89 的 PPL。下游任务的小幅波动源于 50% sparsity 下任务已接近随机性能的边界。 两个 seed 的一致性结果证明了梯度耦合的贡献为零，说明目标质量才是唯一的驱动因素——这直接支撑了论文的核心主张，也回应了审稿人关于增量性的质疑。接下来我在规划一个 6 点稀疏度扫描实验，覆盖 25% 到 50% 的范围，其中 25% 的数据已经训练完成等待评估，我会将其与现有的 30-50% 结果合并，同时生成均匀分配和全局分配两种方案的完整曲线。

现在我在查看这两种分配方案在不同稀疏度下的困惑度指标和下游任务表现。

单调性检查显示没有违反，而且分配的交叉点出现在35%的稀疏度。关键观察是PPL随着稀疏度增加而单调上升——在低稀疏度区间（25-35%）每增加5个百分点约增加0.47的困惑度，但在高稀疏度区间（45-50%）加速到1.0-1.4，这反映了神经元容量的非线性衰减，25%代表了一个极端情况，几乎没有层被饥饿。

全局分配策略在40%以上开始超越均匀分配，因为学到的跨层优先级在预算紧张时能够发挥价值，而零违反的单调性是因为没有出现病理性的层崩溃或异常的种子效应。

现在看Figure 5b的下游任务热力图，它展示了六个稀疏度水平下四个任务的表现，按保留率和密集模型进行颜色编码。分析表明存在三个明确的阶段：在30%以下预算充足时均匀分配略占优势，35-45%的预算受限区间全局分配开始胜出，而50%以上时两种方法都会崩溃到接近随机的水平。这个约35%的交叉点为部署提供了实用指导——30%加均匀分配是8B模型的推荐工作点。

现在要用BCE预测器在30%稀疏度下通过强制TEAL top-k来填补Table 2中的空白，对比KL 30%均匀分配的结果来量化推荐操作点处的掩码质量差距。

BCE在30%强制top-k下的困惑度约11.2，接近KL在50%的水平，这是因为BCE基于幅度的掩码机制即使只剪枝30%也会选错神经元——BCE的梯度独立计算每个神经元，无法捕捉神经元间的联合交互作用，导致掩码与KL的发散度达到53%，而那些被错误剪枝的神经元恰好包含了KL识别出的高交互重要性神经元。

2.42的困惑度差距（11.24对比8.82）表明BCE的劣质掩码浪费了约20个百分点的稀疏度预算，直观证明了掩码质量的重要性——使用BCE掩码需要额外保留20%的神经元才能达到KL在50%稀疏度下的质量水平。

现在我在规划LongBench的全面评估，涵盖英文子集中4K到32K令牌长度的各类任务，包括单文档问答、多文档问答、摘要生成、少样本学习和代码任务，并记录了各任务类型在密集基线下的预期结果。

接下来我在对比KL 30% uniform和TEAL 30%两种稀疏方法的性能表现，KL方法在保留率上达到78%，而TEAL仅为61%，KL相比TEAL平均提升27%。

KL predictor虽然在2048-token序列上训练，但学到的神经元重要性模式主要反映了SwiGLU的结构特性，这个模式在更长序列上基本保持稳定。在30%稀疏度下，大多数关键神经元被保留，这是KL表现良好的主要原因。QA任务的性能下降比摘要任务更明显，因为QA需要精确检索而摘要对质量损失的容忍度更高。TEAL的性能下降更大是因为基于幅度的掩码在长上下文中会累积更多的逐层分配误差。

之前多次LongBench评估失败表明流程存在脆弱性，现在假设评估管道问题已解决。KL30在长上下文维度上的平均保留率约78%，相比TEAL30的61%进一步验证了掩码质量的优势。KL预测器从2K到32K的泛化能力支持了"结构神经元重要性"的假设。

现在转向MT-Bench评估，这是优先级任务，涉及80个多轮问题和8个类别，使用GPT-4o评判，预期Dense、KL 30%和TEAL 30%三个条件下的性能指标。

我看到KL30在各个能力维度上的具体得分——写作6.8、推理5.4、数学4.2、编码5.0、信息提取6.5、STEM 6.1、人文6.9、角色扮演7.0——这些数据反映出在30%稀疏度下，多轮指令跟随能力保持约89%的原因在于KL掩码策略保留了对输出分布至关重要的神经元，而注意力模式和SwiGLU的主导神经元在稀疏化中基本保持完整。

数学和编码任务的衰减更明显（4-5分对比密集模型的5.5-6.0分），因为这些任务对精确计算更敏感，而写作和角色扮演几乎无损失，因为它们主要依赖语言建模的主导模式。相比之下，TEAL30在数学和推理上的下降更大，说明基于幅度的掩码策略错误地剪除了功能性神经元。

MT-Bench作为优先级评估，主要是为了加强与EMNLP会议的契合度，因为指令跟随是NLP的核心关注点。KL30在写作、人文和角色扮演上接近密集模型的性能，表明30%的稀疏度对生成质量的影响有限，而数学和编码的较大下降与下游GSM8K的结果一致。现在转向RULER评估，这是一个合成长上下文评估，在4K和16K上下文长度下测试三种代表性任务类型：NIAH、变量追踪和常见词提取。

Looking at the performance metrics across these context lengths, the dense model maintains strong performance at both 4K and 16K, while KL30 shows moderate degradation and TEAL30 drops more significantly, particularly on variable tracking tasks where the gap widens considerably at longer contexts. Now I'm seeing how pruning errors compound across layers in the VT task since it requires tracking multiple variables over long ranges, whereas NIAH is more robust because it only needs to locate a single needle. The KL masking approach preserves cross-layer information flow better than TEAL, giving it the biggest advantage on VT. I'm planning to include diagnostic results from RULER across different context lengths and sparsity conditions to complement the end-to-end LongBench evaluation, though this will only run if GPU resources allow and the earlier experiments finish. I'm noticing the eval pipeline is producing inconsistent results—the KL30 scores are much lower than expected, and there are clear anomalies like multi_news being higher for KL30 than for dense, which suggests a bug. I should assume the pipeline gets fixed and use more conservative predictions based on the reasonable data points, while acknowledging this uncertainty in my estimates.

Looking at published benchmarks for Llama 3.1 8B, I'm seeing higher scores across the board—narrativeqa around 18-22, qasper 27-35, govreport 28-32, multiNews 25-28—but these are for the Instruct variant, so the base model would perform lower.

Let me anchor on the v6 dense scores as a reference point, acknowledging the multiNews anomaly looks like an eval bug, and extrapolate from there for a corrected scenario where the base model sits somewhere between the published instruct numbers and the v6 results.

For the context window compression approaches, I'm working through KL30 uniform at 78% retention and TEAL30 at 58% retention, which show progressively more conservative performance drops across the benchmarks. I'll use these as reasonable estimates rather than trying to be overly precise.

Now I'm thinking about MT-Bench specifically—it's really not designed for base models at all, so the Llama 3.1 8B base would perform quite poorly there compared to instruction-tuned variants. I need to include predictions for all the planned experiments the user asked for, including the PREPARING sub-experiments that feed into the what_if analyses. For the sparsity sweep, I'm mapping out the specific configurations—25% and 35% sparsity levels with both global and uniform TEAL variants—and their corresponding perplexity predictions.

Writing YAML structure... I'm checking the PPL numbers across different runs for the C1 ablation. For s42, the uniform eval gives 11.9638 with no delta. For s123, I'm seeing conflicting results—the dedicated uniform eval shows 11.89 PPL with a delta of -0.94, but there's also a bench result at 11.83. I'll go with 11.89 from the dedicated uniform eval since that's the more direct measurement. I'm noticing some discrepancies in the performance numbers across different evaluation runs—the uniform eval shows 11.89 for perplexity, but when I compare it to the global baseline of 11.745, the delta doesn't match what's reported. There's also a slight variation with the bench results showing 11.83, which suggests these might be from slightly different evaluation protocols. For the final YAML, I'll use the 11.89 figure from the dedicated eval and estimate the C1 s123 variant around 11.91, then trace through the KL 50% configurations to ensure consistency across all the key metrics. Now I'm looking at the uniform PPL results across the three seeds and calculating the mean—it comes out to around 11.936 using the eval numbers or 11.918 using the bench numbers. I need to figure out what the C1 ablation PPL should be for each seed to match this overall performance.

For the best tier requirement, I'm realizing I only need s123 to succeed, not all three seeds—the definition specifically calls for s123 with a delta less than 0.05 between the BCE+KL-targets PPL and the KL PPL, which I can verify is met.

Now I'm looking at the predicted metrics for C1 s123: the PPL should come in at 11.92 with a delta of 0.03, and across the downstream tasks the deltas stay well within the 1.5pp threshold, with ARC dropping by 0.68pp, WG gaining 0.61pp, and both MMLU and GSM8K shifting by just 0.15pp.

Let me write out the final YAML with all these numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74d5dd94-dd13-4617-a1c1-1a982ea718ba",
  "isSidechain": false,
  "requestId": "req_011CbASTUEWn7tpSNtDkebaH",
  "type": "assistant",
  "uuid": "0b32b66e-eff3-402d-b2bf-7032ad4e332d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN2DnqYjaAJuobczRN9V9r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35656,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17315,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35656
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

_source line 9 · 2026-05-18T17:42:06.890Z_

Let me check if there are existing prediction files for format reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b32b66e-eff3-402d-b2bf-7032ad4e332d",
  "isSidechain": false,
  "requestId": "req_011CbASTUEWn7tpSNtDkebaH",
  "type": "assistant",
  "uuid": "c236c0f9-b073-4f52-a27c-caeefc1fb58c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN2DnqYjaAJuobczRN9V9r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35656,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17315,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35656
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

_source line 10 · 2026-05-18T17:42:07.159Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XtARwLAGnSvigUVHq1aGxf`</summary>

```json
{
  "pattern": "**/*prediction*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c236c0f9-b073-4f52-a27c-caeefc1fb58c",
  "isSidechain": false,
  "requestId": "req_011CbASTUEWn7tpSNtDkebaH",
  "type": "assistant",
  "uuid": "0d50825c-2756-4050-a8d1-d407ee931a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN2DnqYjaAJuobczRN9V9r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35656,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17315,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35656
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

_source line 11 · 2026-05-18T17:42:07.457Z_

<details><summary>↩ Tool result · `toolu_01QMfWHiiVvkWtCqYsCbTw3j`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58c285ef-e220-415e-baaf-a0ae237cf2a9",
  "isSidechain": false,
  "promptId": "f18b1bc3-3ff5-44be-ac99-348755bdc6db",
  "type": "user",
  "uuid": "ea23c2ea-d39f-4e70-96a2-1b85c911d67c",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 48,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "58c285ef-e220-415e-baaf-a0ae237cf2a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T17:42:07.193Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RKPCcBzd5w1p5o1Z7NyHg8`</summary>

```json
{
  "pattern": "**/*imagined*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d50825c-2756-4050-a8d1-d407ee931a57",
  "isSidechain": false,
  "requestId": "req_011CbASTUEWn7tpSNtDkebaH",
  "type": "assistant",
  "uuid": "238515a6-3851-4e8a-805b-442495839ece",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN2DnqYjaAJuobczRN9V9r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35656,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17315,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35656
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

_source line 13 · 2026-05-18T17:42:07.253Z_

<details><summary>↩ Tool result · `toolu_01XtARwLAGnSvigUVHq1aGxf`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d50825c-2756-4050-a8d1-d407ee931a57",
  "isSidechain": false,
  "promptId": "f18b1bc3-3ff5-44be-ac99-348755bdc6db",
  "type": "user",
  "uuid": "5aa3fc72-f734-4798-8d78-d9eaaee8682c",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 77,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0d50825c-2756-4050-a8d1-d407ee931a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T17:42:07.267Z_

<details><summary>↩ Tool result · `toolu_01RKPCcBzd5w1p5o1Z7NyHg8`</summary>

```text
projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml
projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/imagined_experiments.yaml
projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "238515a6-3851-4e8a-805b-442495839ece",
  "isSidechain": false,
  "promptId": "f18b1bc3-3ff5-44be-ac99-348755bdc6db",
  "type": "user",
  "uuid": "d6a948b8-f7b9-4919-8703-94bad4a6705b",
  "toolUseResult": {
    "filenames": [
      "projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml",
      "projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/imagined_experiments.yaml",
      "projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/imagined_experiments.yaml"
    ],
    "durationMs": 64,
    "numFiles": 3,
    "truncated": false
  },
  "sourceToolAssistantUUID": "238515a6-3851-4e8a-805b-442495839ece",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T17:42:07.406Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QMfWHiiVvkWtCqYsCbTw3j`</summary>

```json
{
  "pattern": "**/*tier*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6a948b8-f7b9-4919-8703-94bad4a6705b",
  "isSidechain": false,
  "requestId": "req_011CbASTUEWn7tpSNtDkebaH",
  "type": "assistant",
  "uuid": "58c285ef-e220-415e-baaf-a0ae237cf2a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SN2DnqYjaAJuobczRN9V9r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35656,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17315,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35656
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1 causal ablation 跨 seed 完美复现，mask pattern discovery 叙事被审稿人接受为genuine empirical finding 核心假设：['C1 s123 复现 exact match: BCE+KL-targets PPL 与 KL PPL delta <…",
  "leafUuid": "ea23c2ea-d39f-4e70-96a2-1b85c911d67c",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation mask discovery causal validation",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

### Tool call

_source line 18 · 2026-05-18T17:42:12.506Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PZCubAij2a5s5yqXN8MqL9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea23c2ea-d39f-4e70-96a2-1b85c911d67c",
  "isSidechain": false,
  "requestId": "req_011CbASsECpbvMczb6QD46Xe",
  "type": "assistant",
  "uuid": "d0e126a9-1ec3-4840-a997-ac8f28354623",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xn4n86CEMjYrtz23b2CkmR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17455,
      "cache_read_input_tokens": 47497,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 47497,
          "cache_creation_input_tokens": 17455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17455
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

_source line 19 · 2026-05-18T17:42:12.767Z_

<details><summary>↩ Tool result · `toolu_01PZCubAij2a5s5yqXN8MqL9`</summary>

```text
1	tier: best
2	narrative_guidance: 'KL categorically dominates. Headline: ''Output-distribution distillation
3	  makes compensation networks obsolete for SwiGLU sparsity.'' 三线汇聚——理论（gradient coupling解释joint
4	  interaction）、 实验（KL-only vs BCE+comp gap 9+ PPL points）、实践（省256MB compensation weights
5	  + per-layer GEMV）。 所有planned实验均确认三条claims原样成立，无需调整framing。投EMNLP Efficient Methods。
6	
7	  '
8	imagined_experiments:
9	- name: Four-Condition Ablation @ 50% Sparsity
10	  plan_id: plan_001
11	  description: 'KL-only扩展到5 seeds（新增s0, s1），BCE+comp 5 seeds，KL+comp 3 seeds。 已有数据：KL-only
12	    3 seeds (s42/s123/s456)均~9.2 PPL；BCE-only 3 seeds均~28.2 PPL。
13	
14	    '
15	  expected_results:
16	    kl_only_s42_ppl: 9.2142
17	    kl_only_s123_ppl: 9.2474
18	    kl_only_s456_ppl: 9.14
19	    kl_only_s0_ppl: 9.19
20	    kl_only_s1_ppl: 9.23
21	    kl_only_mean_ppl: 9.2
22	    kl_only_std_ppl: 0.04
23	    kl_only_model_sparsity: 0.498
24	    bce_comp_s42_ppl: 18.22
25	    bce_comp_s123_ppl: 18.91
26	    bce_comp_s456_ppl: 18.38
27	    bce_comp_s0_ppl: 18.65
28	    bce_comp_s1_ppl: 19.05
29	    bce_comp_mean_ppl: 18.64
30	    bce_comp_std_ppl: 0.33
31	    bce_comp_model_sparsity: 0.496
32	    kl_comp_s42_ppl: 9.05
33	    kl_comp_s123_ppl: 9.08
34	    kl_comp_s456_ppl: 8.92
35	    kl_comp_mean_ppl: 9.02
36	    kl_comp_std_ppl: 0.07
37	    bce_only_mean_ppl: 28.16
38	    bce_only_std_ppl: 0.17
39	    kl_only_vs_bce_comp_gap: 9.44
40	    kl_only_vs_dense_increase_pct: 50.3
41	    bce_comp_vs_dense_increase_pct: 204.6
42	    comp_benefit_for_bce_ppl: 9.52
43	    comp_benefit_for_kl_ppl: 0.18
44	  result_rationale: 'KL的gradient dL_KL/ds_j通过d_logits/dh * dh/dm耦合所有active neurons，天然捕获joint
45	    interaction effects。因此KL-only已将output distribution对齐到接近dense水平（PPL 9.2 vs 6.12），
46	    compensation网络能额外修正的residual极小（仅0.18 PPL），大部分interaction已被KL loss消化。 反观BCE的per-neuron
47	    factorized gradient只优化每个neuron独立的on/off decision，完全忽略joint effects——这在50% sparsity下产生巨大误差（PPL
48	    28.2）。Compensation网络虽然能回收~40%的 质量gap（28.2→18.6），但其capacity有限，无法弥补BCE从根源上丢失的coupling
49	    information。 5-seed KL-only的极低std（0.04）证明s456不是outlier，训练高度稳定。 核心结论：compensation对KL是冗余的（0.18
50	    PPL改善 vs 9.44 PPL gap），claims 1成立。
51	
52	    '
53	  tables:
54	  - name: 'Table 1: Four-Condition Ablation Results (WikiText-2 PPL, Llama 3.1 8B,
55	      50% sparsity)'
56	    columns:
57	    - Condition
58	    - Seeds
59	    - PPL (mean±std)
60	    - Δ vs Dense
61	    - Comp Benefit
62	    rows:
63	    - - Dense
64	      - '-'
65	      - '6.12'
66	      - '-'
67	      - '-'
68	    - - BCE-only
69	      - 3
70	      - 28.16±0.17
71	      - +360%
72	      - '-'
73	    - - BCE+comp
74	      - 5
75	      - 18.64±0.33
76	      - +205%
77	      - −9.52
78	    - - KL-only
79	      - 5
80	      - 9.20±0.04
81	      - +50%
82	      - '-'
83	    - - KL+comp
84	      - 3
85	      - 9.02±0.07
86	      - +47%
87	      - −0.18
88	  figures_description:
89	  - 'Box plot: 5-seed PPL distributions for KL-only vs BCE+comp，中位线、IQR和outliers，直观展示两个分布零重叠'
90	  - 'Bar chart: compensation benefit (PPL reduction) for BCE vs KL，量化compensation对两种loss的边际价值'
91	  analysis: 'KL-only以9.20 PPL大幅碾压BCE+comp的18.64 PPL（gap 9.44 points），且compensation对KL仅贡献
92	    0.18 PPL改善（vs对BCE贡献9.52），证明compensation网络对KL训练的predictor完全不必要。 5-seed std=0.04证明高度可复现。Headline
93	    claim直接成立：output-distribution distillation eliminates the need for compensation
94	    networks.
95	
96	    '
97	- name: STE Baseline — Isolating Loss vs Relaxation
98	  plan_id: plan_002
99	  description: '用Straight-Through Estimator替换Gumbel-sigmoid，保持KL loss不变。3 seeds。 目的：确认KL优势来自loss
100	    function而非Gumbel relaxation。
101	
102	    '
103	  expected_results:
104	    ste_kl_s42_ppl: 9.72
105	    ste_kl_s123_ppl: 9.85
106	    ste_kl_s456_ppl: 9.64
107	    ste_kl_mean_ppl: 9.74
108	    ste_kl_std_ppl: 0.09
109	    ste_kl_model_sparsity: 0.497
110	    ste_kl_vs_gumbel_kl_gap: 0.54
111	    ste_kl_vs_bce_only_gap: 18.42
112	    gumbel_contribution_pct: 2.8
113	  result_rationale: 'STE用biased but unbiased-in-expectation的梯度直通传播，丢失了Gumbel relaxation提供的
114	    smooth gradient landscape。因此STE+KL比Gumbel+KL略差（+0.54 PPL），对应predictor在 decision
115	    boundary附近的optimization稍差。但关键是STE+KL（9.74）仍远优于Gumbel+BCE（28.16）， 说明KL-BCE的18.96
116	    point gap中97%以上来自loss function的gradient coupling property， Gumbel relaxation仅贡献~3%的marginal
117	    improvement。这直接排除了reviewer concern "Gumbel-sigmoid relaxation, not KL, explains
118	    gains"。
119	
120	    '
121	  tables:
122	  - name: 'Table 2: Relaxation Method Ablation'
123	    columns:
124	    - Condition
125	    - Relaxation
126	    - Loss
127	    - PPL (mean±std)
128	    rows:
129	    - - Gumbel+KL (ours)
130	      - Gumbel-sigmoid
131	      - KL
132	      - 9.20±0.04
133	    - - STE+KL
134	      - Straight-Through
135	      - KL
136	      - 9.74±0.09
137	    - - Gumbel+BCE
138	      - Gumbel-sigmoid
139	      - BCE
140	      - 28.16±0.17
141	  figures_description:
142	  - 'Attribution bar chart: 将KL-BCE总gap分解为loss contribution (97.2%) vs relaxation
143	    contribution (2.8%)'
144	  analysis: 'STE实验明确归因：KL的gradient coupling是优势的几乎全部来源（97%），Gumbel relaxation是 锦上添花的minor
145	    optimization trick。这为理论narrative提供clean experimental support， 且预防了reviewer的alternative
146	    explanation attack。
147	
148	    '
149	- name: Iso-Compute BCE vs KL
150	  plan_id: plan_003
151	  description: 'KL每步需full forward pass计算logit targets（~3.2x BCE per-step FLOPs）。 给BCE同等total
152	    FLOPs预算（3.2x steps），排除compute advantage。3 seeds。
153	
154	    '
155	  expected_results:
156	    kl_steps: 1000
157	    kl_flops_per_step_ratio: 3.2
158	    kl_total_flops_ratio: 3200
159	    bce_standard_steps: 1000
160	    bce_extended_steps: 3200
161	    bce_extended_total_flops_ratio: 3200
162	    bce_extended_s42_ppl: 25.28
163	    bce_extended_s123_ppl: 25.83
164	    bce_extended_s456_ppl: 25.12
165	    bce_extended_mean_ppl: 25.41
166	    bce_extended_std_ppl: 0.31
167	    bce_standard_mean_ppl: 28.16
168	    improvement_from_extended_training: 2.75
169	    remaining_gap_vs_kl: 16.21
170	    training_wall_clock_kl_hours: 4.2
171	    training_wall_clock_bce_extended_hours: 4.1
172	  result_rationale: 'BCE的梯度dL_BCE/ds_j = (σ(s_j) - t_j) * σ''(s_j)仅依赖neuron j自身的target，
173	    更多training steps只能更精确地拟合这个per-neuron target——但target本身就是次优的 （忽略joint interaction）。因此extended
174	    training让BCE-only从28.16降到25.41（降2.75）， 收益递减明显（loss curve在~2000步后plateau），而与KL的gap仍有16.21
175	    points。 这证明KL的优势是information-theoretic的（loss function的gradient structure差异）， 不是compute-driven的，直接回应reviewer
176	    concern "KL wins only because more compute"。
177	
178	    '
179	  tables:
180	  - name: 'Table 3: Iso-Compute Comparison'
181	    columns:
182	    - Condition
183	    - Steps
184	    - Total FLOPs (relative)
185	    - PPL (mean±std)
186	    rows:
187	    - - KL (Gumbel)
188	      - 1000
189	      - 3200x
190	      - 9.20±0.04
191	    - - BCE (standard)
192	      - 1000
193	      - 1000x
194	      - 28.16±0.17
195	    - - BCE (extended)
196	      - 3200
197	      - 3200x
198	      - 25.41±0.31
199	  figures_description:
200	  - 'BCE training curve (PPL vs steps): 展示extended training的diminishing returns，标注KL水平线作为reference'
201	  - 'FLOPs-PPL scatter: 三个condition在iso-FLOPs平面上的位置'
202	  analysis: '即使给BCE 3.2x的training budget，PPL只从28.16降到25.41，distance to KL-only（16.21）
203	    几乎未缩小。BCE的information bottleneck在loss function级别，无法通过更多compute突破。
204	
205	    '
206	- name: SPON Reimplementation & Validation
207	  plan_id: plan_004
208	  description: '在Llama 3.1 8B上重新实现SPON（learnable per-layer bias vectors + KL training），
209	    在5个QA benchmarks上验证质量以确认实现正确性。
210	
211	    '
212	  expected_results:
213	    spon_wikitext2_ppl: 10.82
214	    spon_model_sparsity: 0.501
215	    spon_ppl_increase_vs_dense_pct: 76.9
216	    spon_arc_c: 51.2
217	    spon_arc_e: 74.5
218	    spon_boolq: 79.3
219	    spon_piqa: 78.1
220	    spon_winogrande: 74.8
221	    spon_params_bytes: 1048576
222	    spon_training_time_minutes: 12
223	    dense_arc_c: 55.2
224	    dense_arc_e: 79.4
225	    dense_boolq: 83.1
226	    dense_piqa: 81.3
227	    dense_winogrande: 77.8
228	  result_rationale: 'SPON使用input-independent的bias correction——本质上是per-layer calibration，矫正average-case
229	    下sparsity引入的activation drift。由于是static的，它只能修正E[Δh]（期望偏移），无法处理 per-input variation
230	    Var[Δh|x]。因此SPON将PPL从training-free水平（~12-13）压到10.82， 是一个meaningful but limited的improvement。QA
231	    benchmarks上drops 3-6%符合PPL改善幅度。 SPON的主要价值不在于standalone quality，而是作为composition实验的building
232	    block—— 它修正的orthogonal component（average drift）与contextual predictor修正的component（per-input
233	    variation） 应当可加。
234	
235	    '
236	  tables:
237	  - name: 'Table 4: SPON Validation on QA Benchmarks'
238	    columns:
239	    - Benchmark
240	    - Dense
241	    - SPON
242	    - Δ (abs)
243	    rows:
244	    - - ARC-c
245	      - 55.2
246	      - 51.2
247	      - −4.0
248	    - - ARC-e
249	      - 79.4
250	      - 74.5
251	      - −4.9
252	    - - BoolQ
253	      - 83.1
254	      - 79.3
255	      - −3.8
256	    - - PIQA
257	      - 81.3
258	      - 78.1
259	      - −3.2
260	    - - WinoGrande
261	      - 77.8
262	      - 74.8
263	      - −3.0
264	  figures_description:
265	  - 'Radar chart: Dense vs SPON在5个QA tasks上的profile，验证SPON实现没有catastrophic failure'
266	  analysis: 'SPON实现通过QA benchmark验证，drops幅度与原论文一致（3-5 points），确认实现正确性。 PPL 10.82定位在training-free（12-13）和contextual-KL（9.2）之间，为claim
267	    2 的additivity实验提供可靠的static correction baseline。
268	
269	    '
270	- name: SPON + KL Predictor Composition
271	  plan_id: plan_005
272	  description: '同时应用SPON bias correction和KL contextual prediction。 测试output-space
273	    linearity（interaction residual）和per-layer orthogonality。3 seeds。
274	
275	    '
276	  expected_results:
277	    spon_kl_s42_ppl: 7.95
278	    spon_kl_s123_ppl: 8.12
279	    spon_kl_s456_ppl: 7.88
280	    spon_kl_mean_ppl: 7.98
281	    spon_kl_std_ppl: 0.1
282	    spon_kl_model_sparsity: 0.499
283	    spon_kl_ppl_increase_vs_dense_pct: 30.4
284	    spon_alone_ppl_recovery: 1.68
285	    kl_alone_ppl_recovery: 3.3
286	    combined_ppl_recovery: 4.52
287	    predicted_additive_recovery: 4.98
288	    interaction_residual_pct: 6.8
289	    logit_interaction_residual_l2_norm: 0.042
290	    logit_spon_correction_l2_norm: 0.38
291	    logit_kl_correction_l2_norm: 0.61
292	    logit_interaction_ratio_pct: 6.8
293	    mean_cosine_similarity_spon_kl: 0.11
294	    max_cosine_similarity_spon_kl: 0.23
295	    layers_with_cosine_gt_0_2: 4
296	  result_rationale: 'SPON修正c_s = E[Δh]（average activation drift），KL predictor修正c_θ(x)
297	    = Δh(x) - E[Δh] （per-input residual variation）。两者在correction space中近似正交——SPON的correction是
298	    constant vector，KL的correction是zero-mean（训练过程中自然去中心化）。因此组合 c = c_s + c_θ(x)的interaction
299	    residual很小（6.8%）。PPL从KL-only的9.20进一步压到7.98， 接近dense的6.12。mean cosine similarity仅0.11，证明两种correction确实address不同的
300	    error components。少数layers（4/32）cosine > 0.2，是因为某些layers的average drift 和per-input
301	    variation方向部分对齐（如early layers的token-independent patterns）， 但这不影响整体additivity。Claim
302	    2（modular decomposition）直接成立。
303	
304	    '
305	  tables:
306	  - name: 'Table 5: Composition Additivity Analysis'
307	    columns:
308	    - Component
309	    - PPL Recovery (from TEAL baseline)
310	    - Predicted Additive
311	    - Actual
312	    - Interaction Residual
313	    rows:
314	    - - SPON only
315	      - 1.68
316	      - '-'
317	      - '-'
318	      - '-'
319	    - - KL only
320	      - 3.3
321	      - '-'
322	      - '-'
323	      - '-'
324	    - - SPON+KL
325	      - '-'
326	      - 4.98
327	      - 4.52
328	      - 9.2%
329	  - name: 'Table 5b: Per-Layer Cosine Similarity Statistics'
330	    columns:
331	    - Statistic
332	    - Value
333	    rows:
334	    - - Mean cosine
335	      - 0.11
336	    - - Median cosine
337	      - 0.08
338	    - - Max cosine
339	      - 0.23
340	    - - Layers > 0.2
341	      - 4/32
342	  figures_description:
343	  - 'Scatter plot: per-layer SPON correction magnitude vs KL correction magnitude，color
344	    by cosine similarity，展示orthogonality'
345	  - 'Logit-space decomposition visualization: ||Δ(s+c)||, ||Δ(s)||, ||Δ(c)||, ||residual||
346	    的bar chart，直观展示linearity'
347	  - 'PPL waterfall chart: Dense → TEAL → +SPON → +KL → SPON+KL，展示每个component的incremental
348	    contribution'
349	  analysis: 'SPON+KL组合将PPL压到7.98（仅比dense高30%），interaction residual 6.8% < 10%阈值， per-layer
350	    cosine similarity平均0.11。c = c_s + c_θ(x)的modular decomposition experimentally
351	    validated。两种correction address不同error sources的理论预测被定量确认。
352	
353	    '
354	- name: Training-Free Baselines (TEAL, WINA, R-Sparse)
355	  plan_id: plan_006
356	  description: '三种training-free方法在Llama 3.1 8B @ 50% model-level sparsity下的质量。 建立三级hierarchy:
357	    training-free < static-learned < contextual-learned。
358	
359	    '
360	  expected_results:
361	    teal_wikitext2_ppl: 12.48
362	    wina_wikitext2_ppl: 14.76
363	    rsparse_wikitext2_ppl: 13.62
364	    teal_model_sparsity: 0.5
365	    wina_model_sparsity: 0.5
366	    rsparse_model_sparsity: 0.5
367	    teal_ppl_increase_vs_dense_pct: 103.9
368	    wina_ppl_increase_vs_dense_pct: 141.3
369	    rsparse_ppl_increase_vs_dense_pct: 122.6
370	  result_rationale: 'TEAL使用magnitude pruning + greedy per-layer allocation，在training-free中最优，因为
371	    magnitude直接反映activation contribution。R-Sparse加入rank-aware scoring，理论上更好但 实现中的approximation引入noise，实际略逊于TEAL。WINA的weight-informed
372	    scoring虽然 考虑了weight magnitude，但在SwiGLU的gated结构下，weight和activation importance的
373	    correlation比standard FFN更弱（gate和up projection交互），因此表现最差。 所有三种方法PPL都在12-15范围，远逊于learned
374	    methods（KL-only 9.2、SPON 10.8）， 建立clean的三级hierarchy。Training-free方法的根本限制是它们无法learn
375	    per-input neuron importance patterns，只能依赖固定heuristic。
376	
377	    '
378	  tables:
379	  - name: 'Table 6: Training-Free Baseline Comparison'
380	    columns:
381	    - Method
382	    - Type
383	    - WikiText-2 PPL
384	    - Δ vs Dense
385	    rows:
386	    - - Dense
387	      - '-'
388	      - 6.12
389	      - '-'
390	    - - TEAL
391	      - Magnitude + greedy
392	      - 12.48
393	      - +104%
394	    - - R-Sparse
395	      - Rank-aware
396	      - 13.62
397	      - +123%
398	    - - WINA
399	      - Weight-informed
400	      - 14.76
401	      - +141%
402	    - - SPON
403	      - Static learned (KL)
404	      - 10.82
405	      - +77%
406	    - - KL-only
407	      - Contextual learned (KL)
408	      - 9.2
409	      - +50%
410	  figures_description:
411	  - 'Horizontal bar chart: 所有methods按PPL排序，color-coded by method type (training-free
412	    / static / contextual)，清晰展示三级hierarchy'
413	  analysis: '三级hierarchy清晰：training-free (12.5-14.8) < static-learned (10.8) < contextual-learned
414	    (9.2)。 每级提升对应information quality的提高：heuristic → average-case calibration → per-input
415	    optimization。 TEAL作为最强training-free baseline仍比KL-only差3.28 PPL points（+36%），justifies
416	    learned approach的overhead。
417	
418	    '
419	- name: Full Benchmark Suite + Latency Profiling
420	  plan_id: plan_007
421	  description: '所有conditions在WikiText-2/C4 PPL、5个discriminative tasks、wall-clock profiling上的
422	    完整evaluation。构建efficiency-accuracy Pareto frontier。
423	
424	    '
425	  expected_results:
426	    dense_wikitext2_ppl: 6.12
427	    teal_wikitext2_ppl: 12.48
428	    wina_wikitext2_ppl: 14.76
429	    rsparse_wikitext2_ppl: 13.62
430	    spon_wikitext2_ppl: 10.82
431	    bce_only_wikitext2_ppl: 28.16
432	    bce_comp_wikitext2_ppl: 18.64
433	    kl_only_wikitext2_ppl: 9.2
434	    kl_comp_wikitext2_ppl: 9.02
435	    spon_kl_wikitext2_ppl: 7.98
436	    dense_c4_ppl: 7.85
437	    teal_c4_ppl: 15.12
438	    wina_c4_ppl: 17.88
439	    rsparse_c4_ppl: 16.31
440	    spon_c4_ppl: 13.24
441	    bce_only_c4_ppl: 33.42
442	    bce_comp_c4_ppl: 22.15
443	    kl_only_c4_ppl: 11.38
444	    kl_comp_c4_ppl: 11.12
445	    spon_kl_c4_ppl: 9.81
446	    dense_arc_c: 55.2
447	    teal_arc_c: 48.1
448	    wina_arc_c: 46.3
449	    rsparse_arc_c: 47.2
450	    spon_arc_c: 51.2
451	    bce_comp_arc_c: 44.8
452	    kl_only_arc_c: 54.3
453	    spon_kl_arc_c: 54.8
454	    dense_winogrande: 77.8
455	    teal_winogrande: 72.4
456	    wina_winogrande: 70.8
457	    rsparse_winogrande: 71.5
458	    spon_winogrande: 74.8
459	    bce_comp_winogrande: 68.3
460	    kl_only_winogrande: 76.9
461	    spon_kl_winogrande: 77.2
462	    dense_mmlu: 65.8
463	    teal_mmlu: 58.2
464	    wina_mmlu: 56.4
465	    rsparse_mmlu: 57.1
466	    spon_mmlu: 60.3
467	    bce_comp_mmlu: 54.9
468	    kl_only_mmlu: 65.0
469	    spon_kl_mmlu: 65.4
470	    dense_gsm8k: 53.8
471	    teal_gsm8k: 44.2
472	    wina_gsm8k: 41.8
473	    rsparse_gsm8k: 43.1
474	    spon_gsm8k: 46.5
475	    bce_comp_gsm8k: 39.7
476	    kl_only_gsm8k: 52.8
477	    spon_kl_gsm8k: 53.2
478	    dense_humaneval: 32.9
479	    teal_humaneval: 26.2
480	    wina_humaneval: 24.4
481	    rsparse_humaneval: 25.6
482	    spon_humaneval: 28.1
483	    bce_comp_humaneval: 23.8
484	    kl_only_humaneval: 32.3
485	    spon_kl_humaneval: 32.5
486	    kl_only_avg_acc_drop_pct: 1.3
487	    spon_kl_avg_acc_drop_pct: 0.7
488	    bce_comp_avg_acc_drop_pct: 12.8
489	    dense_latency_ms: 16.8
490	    teal_latency_ms: 11.2
491	    spon_latency_ms: 10.9
492	    bce_only_latency_ms: 12.0
493	    bce_comp_latency_ms: 13.8
494	    kl_only_latency_ms: 12.0
495	    kl_comp_latency_ms: 13.8
496	    spon_kl_latency_ms: 12.1
497	    predictor_params_mb: 24
498	    compensation_params_mb: 256
499	    spon_params_mb: 1
500	    kl_only_speedup_vs_dense_pct: 28.6
501	    bce_comp_speedup_vs_dense_pct: 17.9
502	    kl_only_speedup_vs_bce_comp_pct: 13.0
503	  result_rationale: 'Downstream tasks与PPL高度correlated——KL-only的低PPL (9.20)直接转化为downstream任务上
504	    接近dense的accuracy（平均drop仅1.3%）。这是因为KL优化output distribution matching， 保留了token-level的prediction
505	    quality，而downstream tasks本质上都依赖model的next-token prediction能力。BCE+comp虽然有compensation，但其PPL
506	    (18.64)反映的distribution mismatch 在需要precise reasoning的任务上（GSM8K, HumanEval）伤害更大（drop
507	    26-28%），因为 这些任务对error compounding更敏感。 Wall-clock方面，KL-only和BCE-only的predictor开销相同（同架构），但KL-only不需要
508	    compensation，因此比BCE+comp省1.8ms/token（13.8→12.0）。SPON+KL仅比KL-only多0.1ms （bias add几乎免费），但PPL进一步降到7.98。KL-only在Pareto
509	    frontier上dominates BCE+comp——更快、更好、更小。
510	
511	    '
512	  tables:
513	  - name: 'Table 7: Comprehensive Benchmark Results (Llama 3.1 8B, 50% sparsity)'
514	    columns:
515	    - Method
516	    - Wiki PPL↓
517	    - C4 PPL↓
518	    - ARC-c↑
519	    - WinoG↑
520	    - MMLU↑
521	    - GSM8K↑
522	    - HumanE↑
523	    - Avg Δ↓
524	    rows:
525	    - - Dense
526	      - 6.12
527	      - 7.85
528	      - 55.2
529	      - 77.8
530	      - 65.8
531	      - 53.8
532	      - 32.9
533	      - —
534	    - - TEAL
535	      - 12.48
536	      - 15.12
537	      - 48.1
538	      - 72.4
539	      - 58.2
540	      - 44.2
541	      - 26.2
542	      - −7.8
543	    - - WINA
544	      - 14.76
545	      - 17.88
546	      - 46.3
547	      - 70.8
548	      - 56.4
549	      - 41.8
550	      - 24.4
551	      - −9.9
552	    - - R-Sparse
553	      - 13.62
554	      - 16.31
555	      - 47.2
556	      - 71.5
557	      - 57.1
558	      - 43.1
559	      - 25.6
560	      - −8.8
561	    - - SPON
562	      - 10.82
563	      - 13.24
564	      - 51.2
565	      - 74.8
566	      - 60.3
567	      - 46.5
568	      - 28.1
569	      - −5.3
570	    - - BCE+comp
571	      - 18.64
572	      - 22.15
573	      - 44.8
574	      - 68.3
575	      - 54.9
576	      - 39.7
577	      - 23.8
578	      - −12.8
579	    - - KL-only
580	      - 9.2
581	      - 11.38
582	      - 54.3
583	      - 76.9
584	      - 65.0
585	      - 52.8
586	      - 32.3
587	      - −1.3
588	    - - SPON+KL
589	      - 7.98
590	      - 9.81
591	      - 54.8
592	      - 77.2
593	      - 65.4
594	      - 53.2
595	      - 32.5
596	      - −0.7
597	  - name: 'Table 8: Inference Efficiency Comparison'
598	    columns:
599	    - Method
600	    - Latency (ms/tok)
601	    - Speedup vs Dense
602	    - Extra Params (MB)
603	    - PPL
604	    rows:
605	    - - Dense
606	      - 16.8
607	      - 1.00×
608	      - 0
609	      - 6.12
610	    - - TEAL
611	      - 11.2
612	      - 1.50×
613	      - 0
614	      - 12.48
615	    - - SPON
616	      - 10.9
617	      - 1.54×
618	      - 1
619	      - 10.82
620	    - - KL-only
621	      - 12.0
622	      - 1.40×
623	      - 24
624	      - 9.2
625	    - - BCE+comp
626	      - 13.8
627	      - 1.22×
628	      - 280
629	      - 18.64
630	    - - SPON+KL
631	      - 12.1
632	      - 1.39×
633	      - 25
634	      - 7.98
635	  figures_description:
636	  - 'Pareto frontier plot: x=latency (ms/tok), y=WikiText-2 PPL, 所有conditions标注。KL-only和SPON+KL在frontier上，BCE+comp
637	    dominated'
638	  - 'Grouped bar chart: 5个downstream tasks，每个task所有methods并排，直观展示KL-only接近dense而BCE+comp远逊'
639	  - 'Taxonomy heatmap: 2D table (granularity × coupling) 填入PPL值，our cell (contextual
640	    × KL) 最优'
641	  analysis: 'KL-only在quality-efficiency Pareto frontier上strictly dominates BCE+comp：更低PPL（9.20
642	    vs 18.64）， 更低latency（12.0 vs 13.8），更少参数（24MB vs 280MB）。Downstream tasks确认PPL gains
643	    transfer：KL-only平均仅drop 1.3%（best tier阈值2%以内），BCE+comp drop 12.8%。 SPON+KL作为our
644	    best configuration达到7.98 PPL和0.7%平均drop，接近free lunch。 Taxonomy table的每个cell都有实验数据支撑。
645	
646	    '
647	- name: 7-Level Sparsity Sweep — Quadratic Scaling Test
648	  plan_id: plan_008
649	  description: '在30/35/40/45/50/55/60%七个sparsity level下训练KL-only和BCE-only（各1 seed），
650	    测试KL-BCE delta ∝ s²的理论预测。50%复用plan_001。每个level做Taylor expansion accuracy test。
651	
652	    '
653	  expected_results:
654	    sparsity_levels:
655	    - 0.3
656	    - 0.35
657	    - 0.4
658	    - 0.45
659	    - 0.5
660	    - 0.55
661	    - 0.6
662	    kl_ppls:
663	    - 7.05
664	    - 7.42
665	    - 7.98
666	    - 8.51
667	    - 9.2
668	    - 10.82
669	    - 13.15
670	    bce_ppls:
671	    - 14.55
672	    - 17.82
673	    - 19.98
674	    - 24.71
675	    - 28.2
676	    - 33.62
677	    - 42.65
678	    kl_bce_deltas:
679	    - 7.5
680	    - 10.4
681	    - 12.0
682	    - 16.2
683	    - 19.0
684	    - 22.8
685	    - 29.5
686	    s2_fit_coefficient_a: 79.2
687	    s2_fit_r_squared: 0.97
688	    s2_plus_linear_fit_r_squared: 0.99
689	    taylor_accuracy_pct:
690	    - 96.8
691	    - 95.4
692	    - 94.1
693	    - 92.5
694	    - 89.8
695	    - 85.6
696	    - 80.2
697	    predicted_deltas_s2_only:
698	    - 7.13
699	    - 9.7
700	    - 12.67
701	    - 16.03
702	    - 19.8
703	    - 23.96
704	    - 28.51
705	  result_rationale: 'KL的梯度dL_KL/ds_j通过Jacobian d_logits/dh耦合所有active neurons。当sparsity为s时，
706	    每个pruned neuron的interaction涉及O(sD)个其他pruned neurons，total interaction scale为 O(s²D²)。BCE的factorized
707	    gradient完全忽略这些interactions。因此KL-BCE quality delta 应当scale as s²（leading term来自pairwise
708	    neuron interaction）。 实验数据R²=0.97证实quadratic scaling dominates。Taylor expansion在低sparsity（30-40%）
709	    下accuracy > 94%是因为higher-order terms（s³等）negligible；在高sparsity（55-60%） accuracy降到80-86%是因为三体及更高阶interaction开始significant——这本身也是consistent
710	    with the theory（Taylor展开在远离展开点时精度下降）。 加入linear term后R²=0.99，说明residual主要是one lower-order
711	    correction。 Claim 3（quadratic scaling）定量验证通过。
712	
713	    '
714	  tables:
715	  - name: 'Table 9: Sparsity Sweep Results'
716	    columns:
717	    - Sparsity s
718	    - s²
719	    - KL PPL
720	    - BCE PPL
721	    - Δ (BCE−KL)
722	    - Predicted Δ (as²)
723	    - Taylor Acc %
724	    rows:
725	    - - 0.3
726	      - 0.09
727	      - 7.05
728	      - 14.55
729	      - 7.5
730	      - 7.13
731	      - 96.8
732	    - - 0.35
733	      - 0.123
734	      - 7.42
735	      - 17.82
736	      - 10.4
737	      - 9.7
738	      - 95.4
739	    - - 0.4
740	      - 0.16
741	      - 7.98
742	      - 19.98
743	      - 12.0
744	      - 12.67
745	      - 94.1
746	    - - 0.45
747	      - 0.203
748	      - 8.51
749	      - 24.71
750	      - 16.2
751	      - 16.03
752	      - 92.5
753	    - - 0.5
754	      - 0.25
755	      - 9.2
756	      - 28.2
757	      - 19.0
758	      - 19.8
759	      - 89.8
760	    - - 0.55
761	      - 0.303
762	      - 10.82
763	      - 33.62
764	      - 22.8
765	      - 23.96
766	      - 85.6
767	    - - 0.6
768	      - 0.36
769	      - 13.15
770	      - 42.65
771	      - 29.5
772	      - 28.51
773	      - 80.2
774	  - name: 'Table 9b: Scaling Fit Statistics'
775	    columns:
776	    - Model
777	    - R²
778	    - Parameters
779	    rows:
780	    - - Δ = as²
781	      - 0.97
782	      - a=79.2
783	    - - Δ = as² + bs
784	      - 0.99
785	      - a=68.1, b=5.8
786	    - - Δ = as² + bs + c
787	      - 0.99
788	      - a=65.3, b=7.2, c=−0.4
789	  figures_description:
790	  - 'Scatter + fitted curve: x=s², y=KL-BCE delta, 实测点+quadratic fit曲线+95% CI band。R²=0.97标注'
791	  - 'Dual-axis line plot: x=sparsity, 左轴=KL PPL和BCE PPL（两条线），右轴=delta（bar chart），展示gap加速增长'
792	  - 'Taylor accuracy vs sparsity: 展示理论预测precision随sparsity的graceful degradation'
793	  analysis: 'KL-BCE delta与s²的R²=0.97，定量验证了gradient coupling theory的核心预测。 Quadratic
794	    scaling意味着在高sparsity regime（>50%），KL的优势accelerates—— 这提供了一个可检验的、非trivial的理论预测，不仅描述已有数据，也predicts
795	    extrapolation behavior。Taylor accuracy的graceful degradation pattern进一步 增强理论credibility。Claim
796	    3直接成立。
797	
798	    '
799	- name: Mistral-7B-v0.3 Cross-Architecture Validation
800	  plan_id: plan_009
801	  description: '在Mistral-7B-v0.3（GQA + sliding window attention，不同于Llama的GQA-only）上
802	    复现KL-only vs BCE+comp comparison。Core benchmarks: WikiText-2 PPL, ARC-c, MMLU。3
803	    seeds each。
804	
805	    '
806	  expected_results:
807	    mistral_dense_wikitext2_ppl: 5.48
808	    mistral_dense_arc_c: 58.1
809	    mistral_dense_mmlu: 62.8
810	    mistral_kl_s42_ppl: 8.12
811	    mistral_kl_s123_ppl: 8.35
812	    mistral_kl_s456_ppl: 8.18
813	    mistral_kl_mean_ppl: 8.22
814	    mistral_kl_std_ppl: 0.1
815	    mistral_kl_model_sparsity: 0.498
816	    mistral_kl_ppl_increase_vs_dense_pct: 50.0
817	    mistral_kl_arc_c: 56.4
818	    mistral_kl_mmlu: 61.3
819	    mistral_bce_comp_s42_ppl: 12.81
820	    mistral_bce_comp_s123_ppl: 13.24
821	    mistral_bce_comp_s456_ppl: 12.53
822	    mistral_bce_comp_mean_ppl: 12.86
823	    mistral_bce_comp_std_ppl: 0.29
824	    mistral_bce_comp_model_sparsity: 0.497
825	    mistral_bce_comp_arc_c: 50.8
826	    mistral_bce_comp_mmlu: 55.9
827	    mistral_kl_vs_bce_comp_ppl_gap: 4.64
828	    mistral_kl_vs_bce_comp_ppl_gap_pct: 36.1
829	  result_rationale: 'Mistral-7B-v0.3使用GQA + sliding window attention，SwiGLU FFN结构与Llama相同但
830	    attention pattern不同，导致不同的activation sparsity distribution。KL的gradient coupling
831	    property是loss function的数学性质，与architecture无关——只要model有SwiGLU FFN且sparsity 在hidden
832	    states上操作，KL就能捕获joint interactions。因此KL优势在Mistral上同方向复现。 PPL increase 50%（vs Llama的50.3%）高度一致。Gap绝对值（4.64
833	    vs 9.44）较小是因为 Mistral的dense PPL更低（5.48 vs 6.12），两个model的relative gap pattern一致。
834	    Sliding window attention可能使某些layers的neuron importance更localized，略微 降低BCE+comp的absolute
835	    PPL（12.86 vs Llama的18.64），但不改变KL dominance。
836	
837	    '
838	  tables:
839	  - name: 'Table 10: Mistral-7B-v0.3 Cross-Architecture Validation'
840	    columns:
841	    - Condition
842	    - Wiki PPL↓
843	    - ARC-c↑
844	    - MMLU↑
845	    rows:
846	    - - Dense
847	      - 5.48
848	      - 58.1
849	      - 62.8
850	    - - KL-only
851	      - 8.22±0.10
852	      - 56.4
853	      - 61.3
854	    - - BCE+comp
855	      - 12.86±0.29
856	      - 50.8
857	      - 55.9
858	    - - Gap (KL vs BCE+comp)
859	      - −4.64
860	      - '+5.6'
861	      - '+5.4'
862	  - name: 'Table 10b: Cross-Architecture Consistency'
863	    columns:
864	    - Metric
865	    - Llama 3.1 8B
866	    - Mistral-7B-v0.3
867	    rows:
868	    - - KL PPL increase vs dense
869	      - 50.3%
870	      - 50.0%
871	    - - KL vs BCE+comp gap (PPL)
872	      - 9.44
873	      - 4.64
874	    - - KL vs BCE+comp gap (%)
875	      - 50.6%
876	      - 36.1%
877	  figures_description:
878	  - 'Side-by-side bar chart: Llama和Mistral的KL-only vs BCE+comp PPL，展示cross-architecture
879	    consistency'
880	  analysis: 'Mistral-7B-v0.3成功复现KL dominance：KL-only (8.22) vs BCE+comp (12.86)，gap
881	    36%。 KL PPL increase vs dense（50%）与Llama（50.3%）惊人一致，证明KL的优势是loss function 的universal
882	    property而非architecture-specific artifact。排除reviewer concern "Single model / limited
883	    generalization"。
884	
885	    '
886	- name: LongBench Long-Context Evaluation
887	  plan_id: plan_010
888	  description: 'LongBench English subset（4K-32K tokens），所有conditions。 Per-task-type
889	    breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。
890	
891	    '
892	  expected_results:
893	    dense_longbench_avg: 43.5
894	    teal_longbench_avg: 35.4
895	    wina_longbench_avg: 33.8
896	    rsparse_longbench_avg: 34.6
897	    spon_longbench_avg: 39.8
898	    bce_comp_longbench_avg: 32.1
899	    kl_only_longbench_avg: 42.1
900	    spon_kl_longbench_avg: 42.8
901	    kl_single_doc_qa: 44.8
902	    kl_multi_doc_qa: 38.2
903	    kl_summarization: 42.5
904	    kl_few_shot: 47.1
905	    kl_code: 38.0
906	    bce_comp_single_doc_qa: 35.2
907	    bce_comp_multi_doc_qa: 28.4
908	    bce_comp_summarization: 33.8
909	    bce_comp_few_shot: 34.6
910	    bce_comp_code: 28.5
911	    dense_single_doc_qa: 46.2
912	    dense_multi_doc_qa: 39.5
913	    dense_summarization: 43.8
914	    dense_few_shot: 48.3
915	    dense_code: 39.6
916	    kl_only_avg_drop_vs_dense: 1.4
917	    bce_comp_avg_drop_vs_dense: 11.4
918	    kl_worst_task_type: multi-doc QA
919	    kl_worst_task_drop: 3.3
920	  result_rationale: '长序列evaluation测试predictor是否generalize beyond短训练序列。KL的output-distribution
921	    matching objective在长序列下仍然有效，因为它不依赖specific sequence length——predictor 看到的是per-token
922	    hidden states，length主要影响attention pattern。KL-only的drop（1.4 avg） 与short-context
923	    evaluation一致。Multi-doc QA是最challenging的任务类型（需要cross-document reasoning），因此KL-only在此处drop最大（3.3
924	    points）。BCE+comp在长序列下degradation 更严重（11.4 avg drop）——因为BCE的per-neuron error在长序列中accumulates
925	    without compensation fully correcting the compounding effect。SPON+KL以42.8接近dense的43.5，
926	    进一步确认composition在长序列下仍然有效。
927	
928	    '
929	  tables:
930	  - name: 'Table 11: LongBench Per-Task-Type Breakdown'
931	    columns:
932	    - Task Type
933	    - Dense
934	    - TEAL
935	    - SPON
936	    - BCE+comp
937	    - KL-only
938	    - SPON+KL
939	    rows:
940	    - - Single-doc QA
941	      - 46.2
942	      - 38.1
943	      - 42.0
944	      - 35.2
945	      - 44.8
946	      - 45.3
947	    - - Multi-doc QA
948	      - 39.5
949	      - 31.2
950	      - 36.1
951	      - 28.4
952	      - 38.2
953	      - 38.8
954	    - - Summarization
955	      - 43.8
956	      - 35.8
957	      - 40.2
958	      - 33.8
959	      - 42.5
960	      - 43.1
961	    - - Few-shot
962	      - 48.3
963	      - 39.5
964	      - 44.3
965	      - 34.6
966	      - 47.1
967	      - 47.8
968	    - - Code
969	      - 39.6
970	      - 32.4
971	      - 36.5
972	      - 28.5
973	      - 38.0
974	      - 38.9
975	    - - '**Average**'
976	      - '**43.5**'
977	      - '**35.4**'
978	      - '**39.8**'
979	      - '**32.1**'
980	      - '**42.1**'
981	      - '**42.8**'
982	  figures_description:
983	  - 'Radar chart: 5个task types，Dense/KL-only/BCE+comp/SPON+KL四条线，展示KL-only profile近似dense'
984	  - 'Heatmap: methods × task types，color by score，直观展示BCE+comp在所有task types上consistently差'
985	  analysis: 'LongBench结果证明KL predictor在长序列（4K-32K）下generalization良好（avg drop 1.4），
986	    无需长序列finetune。BCE+comp在long-context下进一步恶化（avg drop 11.4 vs short-context的12.8%），
987	    可能因为compensation网络对error accumulation的correction在长序列下saturate。 增强了EMNLP venue
988	    fit（NLP-specific long-context evaluation）。
989	
990	    '
991	- name: MT-Bench Multi-Turn Instruction Following
992	  plan_id: plan_011
993	  description: 'MT-Bench 80题 × 8 categories，GPT-4o judge。测试sparsity对instruction following
994	    quality的影响。
995	
996	    '
997	  expected_results:
998	    dense_mtbench_avg: 7.21
999	    teal_mtbench_avg: 6.18
1000	    spon_mtbench_avg: 6.78
1001	    bce_comp_mtbench_avg: 6.42
1002	    kl_only_mtbench_avg: 7.05
1003	    spon_kl_mtbench_avg: 7.12
1004	    kl_writing: 7.35
1005	    kl_roleplay: 7.15
1006	    kl_reasoning: 6.65
1007	    kl_math: 6.55
1008	    kl_coding: 6.85
1009	    kl_extraction: 7.45
1010	    kl_stem: 7.1
1011	    kl_humanities: 7.3
1012	    bce_comp_writing: 6.8
1013	    bce_comp_reasoning: 5.85
1014	    bce_comp_math: 5.65
1015	    bce_comp_coding: 5.9
1016	  result_rationale: 'MT-Bench测试multi-turn instruction following——一个对output quality高度敏感的setting。
1017	    KL-only（7.05）与dense（7.21）差距仅0.16（GPT-4o judge的scoring granularity内）， 说明KL的output
1018	    distribution matching直接保留了instruction following能力。 Math和reasoning categories drop略大（KL-only
1019	    6.55/6.65 vs dense ~6.8/6.85），因为 这些tasks需要precise multi-step reasoning，对任何distribution
1020	    shift更敏感。 BCE+comp（6.42）在reasoning-heavy categories下degradation严重（5.85/5.65），因为
1021	    BCE的imprecise sparsity mask在需要所有neurons correctly participate的reasoning chain上
1022	    产生compounding errors，compensation无法fully recover。
1023	
1024	    '
1025	  tables:
1026	  - name: 'Table 12: MT-Bench Results'
1027	    columns:
1028	    - Method
1029	    - Avg Score
1030	    - Writing
1031	    - Reasoning
1032	    - Math
1033	    - Coding
1034	    rows:
1035	    - - Dense
1036	      - 7.21
1037	      - 7.5
1038	      - 6.85
1039	      - 6.8
1040	      - 7.1
1041	    - - TEAL
1042	      - 6.18
1043	      - 6.45
1044	      - 5.6
1045	      - 5.4
1046	      - 5.8
1047	    - - SPON
1048	      - 6.78
1049	      - 7.1
1050	      - 6.35
1051	      - 6.15
1052	      - 6.55
1053	    - - BCE+comp
1054	      - 6.42
1055	      - 6.8
1056	      - 5.85
1057	      - 5.65
1058	      - 5.9
1059	    - - KL-only
1060	      - 7.05
1061	      - 7.35
1062	      - 6.65
1063	      - 6.55
1064	      - 6.85
1065	    - - SPON+KL
1066	      - 7.12
1067	      - 7.4
1068	      - 6.75
1069	      - 6.65
1070	      - 6.95
1071	  figures_description:
1072	  - 'Grouped bar chart per category: Dense vs KL-only vs BCE+comp，8个categories并排'
1073	  analysis: 'MT-Bench进一步确认KL-only在generation quality上接近dense。GPT-4o judge评分差异 KL-only
1074	    vs dense仅0.16——在judge的noise floor以内。BCE+comp在math/reasoning上 severe degradation（-1.15/-1.00
1075	    vs dense），而KL-only仅-0.25/-0.20。 Strengthens EMNLP NLP evaluation story。
1076	
1077	    '
1078	- name: RULER Synthetic Long-Context Diagnostics
1079	  plan_id: plan_012
1080	  description: 'RULER synthetic evaluation at 4K and 16K context，3 representative
1081	    task types (needle-in-a-haystack, multi-key retrieval, variable tracking)。 Fine-grained
1082	    diagnostics complementing LongBench。
1083	
1084	    '
1085	  expected_results:
1086	    dense_ruler_4k_avg: 95.2
1087	    kl_only_ruler_4k_avg: 93.8
1088	    bce_comp_ruler_4k_avg: 87.4
1089	    spon_kl_ruler_4k_avg: 94.5
1090	    dense_ruler_16k_avg: 88.5
1091	    kl_only_ruler_16k_avg: 86.1
1092	    bce_comp_ruler_16k_avg: 78.3
1093	    spon_kl_ruler_16k_avg: 87.2
1094	    kl_needle_4k: 98.0
1095	    kl_needle_16k: 94.5
1096	    kl_multikey_4k: 91.2
1097	    kl_multikey_16k: 82.4
1098	    kl_vartrack_4k: 92.1
1099	    kl_vartrack_16k: 81.3
1100	    bce_comp_needle_4k: 94.5
1101	    bce_comp_needle_16k: 86.2
1102	    bce_comp_multikey_4k: 83.8
1103	    bce_comp_multikey_16k: 72.1
1104	    bce_comp_vartrack_4k: 83.9
1105	    bce_comp_vartrack_16k: 76.5
1106	    kl_only_4k_to_16k_drop: 7.7
1107	    bce_comp_4k_to_16k_drop: 9.1
1108	    dense_4k_to_16k_drop: 6.7
1109	  result_rationale: 'RULER的synthetic tasks提供controlled diagnostics——每个task isolate一种capability
1110	    (retrieval precision, multi-hop tracking等)。KL-only在4K下接近dense（93.8 vs 95.2）， 在16K下gracefully
1111	    degrade（86.1 vs 88.5）——4K→16K drop (7.7)接近dense pattern (6.7)， 说明KL predictor不会随context
1112	    length引入额外的degradation。BCE+comp的4K→16K drop更大 (9.1)，在multi-key retrieval（需要同时attend
1113	    to多个scattered positions）和variable tracking（需要maintain state across distance）上degradation尤其严重——因为这些tasks
1114	    对sparse mask quality最敏感，BCE的imprecise masks在长距离dependency上compounding。 Needle-in-a-haystack是最简单的task（单点retrieval），所有methods都表现好。
1115	
1116	    '
1117	  tables:
1118	  - name: 'Table 13: RULER Synthetic Evaluation'
1119	    columns:
1120	    - Task
1121	    - Context
1122	    - Dense
1123	    - KL-only
1124	    - BCE+comp
1125	    - SPON+KL
1126	    rows:
1127	    - - Needle
1128	      - 4K
1129	      - 99.2
1130	      - 98.0
1131	      - 94.5
1132	      - 98.5
1133	    - - Needle
1134	      - 16K
1135	      - 96.8
1136	      - 94.5
1137	      - 86.2
1138	      - 95.8
1139	    - - Multi-key
1140	      - 4K
1141	      - 93.5
1142	      - 91.2
1143	      - 83.8
1144	      - 92.4
1145	    - - Multi-key
1146	      - 16K
1147	      - 84.1
1148	      - 82.4
1149	      - 72.1
1150	      - 83.5
1151	    - - Var-track
1152	      - 4K
1153	      - 92.8
1154	      - 92.1
1155	      - 83.9
1156	      - 92.5
1157	    - - Var-track
1158	      - 16K
1159	      - 84.5
1160	      - 81.3
1161	      - 76.5
1162	      - 83.2
1163	    - - '**Average**'
1164	      - '**4K**'
1165	      - '**95.2**'
1166	      - '**93.8**'
1167	      - '**87.4**'
1168	      - '**94.5**'
1169	    - - '**Average**'
1170	      - '**16K**'
1171	      - '**88.5**'
1172	      - '**86.1**'
1173	      - '**78.3**'
1174	      - '**87.2**'
1175	  figures_description:
1176	  - 'Line plot: x=context length (4K, 16K), y=RULER avg accuracy, 每个method一条线，展示degradation
1177	    rate'
1178	  - 'Heatmap: task × method × context length，诊断哪些capabilities被sparsity影响最大'
1179	  analysis: RULER诊断补充LongBench：KL-only的context-length degradation pattern与dense一致
1180	    (4K→16K drop差仅1 point)，而BCE+comp多drop 2.4 points。Multi-key retrieval 是differentiation最大的task（KL
1181	    82.4 vs BCE+comp 72.1 at 16K），这与理论一致—— multi-key需要FFN准确处理多个simultaneously relevant
1182	    positions，joint neuron interaction quality直接影响结果。
1183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0e126a9-1ec3-4840-a997-ac8f28354623",
  "isSidechain": false,
  "promptId": "f18b1bc3-3ff5-44be-ac99-348755bdc6db",
  "type": "user",
  "uuid": "709f89b7-a498-4578-bd17-54a4811a9c61",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: 'KL categorically dominates. Headline: ''Output-distribution distillation\n  makes compensation networks obsolete for SwiGLU sparsity.'' 三线汇聚——理论（gradient coupling解释joint\n  interaction）、 实验（KL-only vs BCE+comp gap 9+ PPL points）、实践（省256MB compensation weights\n  + per-layer GEMV）。 所有planned实验均确认三条claims原样成立，无需调整framing。投EMNLP Efficient Methods。\n\n  '\nimagined_experiments:\n- name: Four-Condition Ablation @ 50% Sparsity\n  plan_id: plan_001\n  description: 'KL-only扩展到5 seeds（新增s0, s1），BCE+comp 5 seeds，KL+comp 3 seeds。 已有数据：KL-only\n    3 seeds (s42/s123/s456)均~9.2 PPL；BCE-only 3 seeds均~28.2 PPL。\n\n    '\n  expected_results:\n    kl_only_s42_ppl: 9.2142\n    kl_only_s123_ppl: 9.2474\n    kl_only_s456_ppl: 9.14\n    kl_only_s0_ppl: 9.19\n    kl_only_s1_ppl: 9.23\n    kl_only_mean_ppl: 9.2\n    kl_only_std_ppl: 0.04\n    kl_only_model_sparsity: 0.498\n    bce_comp_s42_ppl: 18.22\n    bce_comp_s123_ppl: 18.91\n    bce_comp_s456_ppl: 18.38\n    bce_comp_s0_ppl: 18.65\n    bce_comp_s1_ppl: 19.05\n    bce_comp_mean_ppl: 18.64\n    bce_comp_std_ppl: 0.33\n    bce_comp_model_sparsity: 0.496\n    kl_comp_s42_ppl: 9.05\n    kl_comp_s123_ppl: 9.08\n    kl_comp_s456_ppl: 8.92\n    kl_comp_mean_ppl: 9.02\n    kl_comp_std_ppl: 0.07\n    bce_only_mean_ppl: 28.16\n    bce_only_std_ppl: 0.17\n    kl_only_vs_bce_comp_gap: 9.44\n    kl_only_vs_dense_increase_pct: 50.3\n    bce_comp_vs_dense_increase_pct: 204.6\n    comp_benefit_for_bce_ppl: 9.52\n    comp_benefit_for_kl_ppl: 0.18\n  result_rationale: 'KL的gradient dL_KL/ds_j通过d_logits/dh * dh/dm耦合所有active neurons，天然捕获joint\n    interaction effects。因此KL-only已将output distribution对齐到接近dense水平（PPL 9.2 vs 6.12），\n    compensation网络能额外修正的residual极小（仅0.18 PPL），大部分interaction已被KL loss消化。 反观BCE的per-neuron\n    factorized gradient只优化每个neuron独立的on/off decision，完全忽略joint effects——这在50% sparsity下产生巨大误差（PPL\n    28.2）。Compensation网络虽然能回收~40%的 质量gap（28.2→18.6），但其capacity有限，无法弥补BCE从根源上丢失的coupling\n    information。 5-seed KL-only的极低std（0.04）证明s456不是outlier，训练高度稳定。 核心结论：compensation对KL是冗余的（0.18\n    PPL改善 vs 9.44 PPL gap），claims 1成立。\n\n    '\n  tables:\n  - name: 'Table 1: Four-Condition Ablation Results (WikiText-2 PPL, Llama 3.1 8B,\n      50% sparsity)'\n    columns:\n    - Condition\n    - Seeds\n    - PPL (mean±std)\n    - Δ vs Dense\n    - Comp Benefit\n    rows:\n    - - Dense\n      - '-'\n      - '6.12'\n      - '-'\n      - '-'\n    - - BCE-only\n      - 3\n      - 28.16±0.17\n      - +360%\n      - '-'\n    - - BCE+comp\n      - 5\n      - 18.64±0.33\n      - +205%\n      - −9.52\n    - - KL-only\n      - 5\n      - 9.20±0.04\n      - +50%\n      - '-'\n    - - KL+comp\n      - 3\n      - 9.02±0.07\n      - +47%\n      - −0.18\n  figures_description:\n  - 'Box plot: 5-seed PPL distributions for KL-only vs BCE+comp，中位线、IQR和outliers，直观展示两个分布零重叠'\n  - 'Bar chart: compensation benefit (PPL reduction) for BCE vs KL，量化compensation对两种loss的边际价值'\n  analysis: 'KL-only以9.20 PPL大幅碾压BCE+comp的18.64 PPL（gap 9.44 points），且compensation对KL仅贡献\n    0.18 PPL改善（vs对BCE贡献9.52），证明compensation网络对KL训练的predictor完全不必要。 5-seed std=0.04证明高度可复现。Headline\n    claim直接成立：output-distribution distillation eliminates the need for compensation\n    networks.\n\n    '\n- name: STE Baseline — Isolating Loss vs Relaxation\n  plan_id: plan_002\n  description: '用Straight-Through Estimator替换Gumbel-sigmoid，保持KL loss不变。3 seeds。 目的：确认KL优势来自loss\n    function而非Gumbel relaxation。\n\n    '\n  expected_results:\n    ste_kl_s42_ppl: 9.72\n    ste_kl_s123_ppl: 9.85\n    ste_kl_s456_ppl: 9.64\n    ste_kl_mean_ppl: 9.74\n    ste_kl_std_ppl: 0.09\n    ste_kl_model_sparsity: 0.497\n    ste_kl_vs_gumbel_kl_gap: 0.54\n    ste_kl_vs_bce_only_gap: 18.42\n    gumbel_contribution_pct: 2.8\n  result_rationale: 'STE用biased but unbiased-in-expectation的梯度直通传播，丢失了Gumbel relaxation提供的\n    smooth gradient landscape。因此STE+KL比Gumbel+KL略差（+0.54 PPL），对应predictor在 decision\n    boundary附近的optimization稍差。但关键是STE+KL（9.74）仍远优于Gumbel+BCE（28.16）， 说明KL-BCE的18.96\n    point gap中97%以上来自loss function的gradient coupling property， Gumbel relaxation仅贡献~3%的marginal\n    improvement。这直接排除了reviewer concern \"Gumbel-sigmoid relaxation, not KL, explains\n    gains\"。\n\n    '\n  tables:\n  - name: 'Table 2: Relaxation Method Ablation'\n    columns:\n    - Condition\n    - Relaxation\n    - Loss\n    - PPL (mean±std)\n    rows:\n    - - Gumbel+KL (ours)\n      - Gumbel-sigmoid\n      - KL\n      - 9.20±0.04\n    - - STE+KL\n      - Straight-Through\n      - KL\n      - 9.74±0.09\n    - - Gumbel+BCE\n      - Gumbel-sigmoid\n      - BCE\n      - 28.16±0.17\n  figures_description:\n  - 'Attribution bar chart: 将KL-BCE总gap分解为loss contribution (97.2%) vs relaxation\n    contribution (2.8%)'\n  analysis: 'STE实验明确归因：KL的gradient coupling是优势的几乎全部来源（97%），Gumbel relaxation是 锦上添花的minor\n    optimization trick。这为理论narrative提供clean experimental support， 且预防了reviewer的alternative\n    explanation attack。\n\n    '\n- name: Iso-Compute BCE vs KL\n  plan_id: plan_003\n  description: 'KL每步需full forward pass计算logit targets（~3.2x BCE per-step FLOPs）。 给BCE同等total\n    FLOPs预算（3.2x steps），排除compute advantage。3 seeds。\n\n    '\n  expected_results:\n    kl_steps: 1000\n    kl_flops_per_step_ratio: 3.2\n    kl_total_flops_ratio: 3200\n    bce_standard_steps: 1000\n    bce_extended_steps: 3200\n    bce_extended_total_flops_ratio: 3200\n    bce_extended_s42_ppl: 25.28\n    bce_extended_s123_ppl: 25.83\n    bce_extended_s456_ppl: 25.12\n    bce_extended_mean_ppl: 25.41\n    bce_extended_std_ppl: 0.31\n    bce_standard_mean_ppl: 28.16\n    improvement_from_extended_training: 2.75\n    remaining_gap_vs_kl: 16.21\n    training_wall_clock_kl_hours: 4.2\n    training_wall_clock_bce_extended_hours: 4.1\n  result_rationale: 'BCE的梯度dL_BCE/ds_j = (σ(s_j) - t_j) * σ''(s_j)仅依赖neuron j自身的target，\n    更多training steps只能更精确地拟合这个per-neuron target——但target本身就是次优的 （忽略joint interaction）。因此extended\n    training让BCE-only从28.16降到25.41（降2.75）， 收益递减明显（loss curve在~2000步后plateau），而与KL的gap仍有16.21\n    points。 这证明KL的优势是information-theoretic的（loss function的gradient structure差异）， 不是compute-driven的，直接回应reviewer\n    concern \"KL wins only because more compute\"。\n\n    '\n  tables:\n  - name: 'Table 3: Iso-Compute Comparison'\n    columns:\n    - Condition\n    - Steps\n    - Total FLOPs (relative)\n    - PPL (mean±std)\n    rows:\n    - - KL (Gumbel)\n      - 1000\n      - 3200x\n      - 9.20±0.04\n    - - BCE (standard)\n      - 1000\n      - 1000x\n      - 28.16±0.17\n    - - BCE (extended)\n      - 3200\n      - 3200x\n      - 25.41±0.31\n  figures_description:\n  - 'BCE training curve (PPL vs steps): 展示extended training的diminishing returns，标注KL水平线作为reference'\n  - 'FLOPs-PPL scatter: 三个condition在iso-FLOPs平面上的位置'\n  analysis: '即使给BCE 3.2x的training budget，PPL只从28.16降到25.41，distance to KL-only（16.21）\n    几乎未缩小。BCE的information bottleneck在loss function级别，无法通过更多compute突破。\n\n    '\n- name: SPON Reimplementation & Validation\n  plan_id: plan_004\n  description: '在Llama 3.1 8B上重新实现SPON（learnable per-layer bias vectors + KL training），\n    在5个QA benchmarks上验证质量以确认实现正确性。\n\n    '\n  expected_results:\n    spon_wikitext2_ppl: 10.82\n    spon_model_sparsity: 0.501\n    spon_ppl_increase_vs_dense_pct: 76.9\n    spon_arc_c: 51.2\n    spon_arc_e: 74.5\n    spon_boolq: 79.3\n    spon_piqa: 78.1\n    spon_winogrande: 74.8\n    spon_params_bytes: 1048576\n    spon_training_time_minutes: 12\n    dense_arc_c: 55.2\n    dense_arc_e: 79.4\n    dense_boolq: 83.1\n    dense_piqa: 81.3\n    dense_winogrande: 77.8\n  result_rationale: 'SPON使用input-independent的bias correction——本质上是per-layer calibration，矫正average-case\n    下sparsity引入的activation drift。由于是static的，它只能修正E[Δh]（期望偏移），无法处理 per-input variation\n    Var[Δh|x]。因此SPON将PPL从training-free水平（~12-13）压到10.82， 是一个meaningful but limited的improvement。QA\n    benchmarks上drops 3-6%符合PPL改善幅度。 SPON的主要价值不在于standalone quality，而是作为composition实验的building\n    block—— 它修正的orthogonal component（average drift）与contextual predictor修正的component（per-input\n    variation） 应当可加。\n\n    '\n  tables:\n  - name: 'Table 4: SPON Validation on QA Benchmarks'\n    columns:\n    - Benchmark\n    - Dense\n    - SPON\n    - Δ (abs)\n    rows:\n    - - ARC-c\n      - 55.2\n      - 51.2\n      - −4.0\n    - - ARC-e\n      - 79.4\n      - 74.5\n      - −4.9\n    - - BoolQ\n      - 83.1\n      - 79.3\n      - −3.8\n    - - PIQA\n      - 81.3\n      - 78.1\n      - −3.2\n    - - WinoGrande\n      - 77.8\n      - 74.8\n      - −3.0\n  figures_description:\n  - 'Radar chart: Dense vs SPON在5个QA tasks上的profile，验证SPON实现没有catastrophic failure'\n  analysis: 'SPON实现通过QA benchmark验证，drops幅度与原论文一致（3-5 points），确认实现正确性。 PPL 10.82定位在training-free（12-13）和contextual-KL（9.2）之间，为claim\n    2 的additivity实验提供可靠的static correction baseline。\n\n    '\n- name: SPON + KL Predictor Composition\n  plan_id: plan_005\n  description: '同时应用SPON bias correction和KL contextual prediction。 测试output-space\n    linearity（interaction residual）和per-layer orthogonality。3 seeds。\n\n    '\n  expected_results:\n    spon_kl_s42_ppl: 7.95\n    spon_kl_s123_ppl: 8.12\n    spon_kl_s456_ppl: 7.88\n    spon_kl_mean_ppl: 7.98\n    spon_kl_std_ppl: 0.1\n    spon_kl_model_sparsity: 0.499\n    spon_kl_ppl_increase_vs_dense_pct: 30.4\n    spon_alone_ppl_recovery: 1.68\n    kl_alone_ppl_recovery: 3.3\n    combined_ppl_recovery: 4.52\n    predicted_additive_recovery: 4.98\n    interaction_residual_pct: 6.8\n    logit_interaction_residual_l2_norm: 0.042\n    logit_spon_correction_l2_norm: 0.38\n    logit_kl_correction_l2_norm: 0.61\n    logit_interaction_ratio_pct: 6.8\n    mean_cosine_similarity_spon_kl: 0.11\n    max_cosine_similarity_spon_kl: 0.23\n    layers_with_cosine_gt_0_2: 4\n  result_rationale: 'SPON修正c_s = E[Δh]（average activation drift），KL predictor修正c_θ(x)\n    = Δh(x) - E[Δh] （per-input residual variation）。两者在correction space中近似正交——SPON的correction是\n    constant vector，KL的correction是zero-mean（训练过程中自然去中心化）。因此组合 c = c_s + c_θ(x)的interaction\n    residual很小（6.8%）。PPL从KL-only的9.20进一步压到7.98， 接近dense的6.12。mean cosine similarity仅0.11，证明两种correction确实address不同的\n    error components。少数layers（4/32）cosine > 0.2，是因为某些layers的average drift 和per-input\n    variation方向部分对齐（如early layers的token-independent patterns）， 但这不影响整体additivity。Claim\n    2（modular decomposition）直接成立。\n\n    '\n  tables:\n  - name: 'Table 5: Composition Additivity Analysis'\n    columns:\n    - Component\n    - PPL Recovery (from TEAL baseline)\n    - Predicted Additive\n    - Actual\n    - Interaction Residual\n    rows:\n    - - SPON only\n      - 1.68\n      - '-'\n      - '-'\n      - '-'\n    - - KL only\n      - 3.3\n      - '-'\n      - '-'\n      - '-'\n    - - SPON+KL\n      - '-'\n      - 4.98\n      - 4.52\n      - 9.2%\n  - name: 'Table 5b: Per-Layer Cosine Similarity Statistics'\n    columns:\n    - Statistic\n    - Value\n    rows:\n    - - Mean cosine\n      - 0.11\n    - - Median cosine\n      - 0.08\n    - - Max cosine\n      - 0.23\n    - - Layers > 0.2\n      - 4/32\n  figures_description:\n  - 'Scatter plot: per-layer SPON correction magnitude vs KL correction magnitude，color\n    by cosine similarity，展示orthogonality'\n  - 'Logit-space decomposition visualization: ||Δ(s+c)||, ||Δ(s)||, ||Δ(c)||, ||residual||\n    的bar chart，直观展示linearity'\n  - 'PPL waterfall chart: Dense → TEAL → +SPON → +KL → SPON+KL，展示每个component的incremental\n    contribution'\n  analysis: 'SPON+KL组合将PPL压到7.98（仅比dense高30%），interaction residual 6.8% < 10%阈值， per-layer\n    cosine similarity平均0.11。c = c_s + c_θ(x)的modular decomposition experimentally\n    validated。两种correction address不同error sources的理论预测被定量确认。\n\n    '\n- name: Training-Free Baselines (TEAL, WINA, R-Sparse)\n  plan_id: plan_006\n  description: '三种training-free方法在Llama 3.1 8B @ 50% model-level sparsity下的质量。 建立三级hierarchy:\n    training-free < static-learned < contextual-learned。\n\n    '\n  expected_results:\n    teal_wikitext2_ppl: 12.48\n    wina_wikitext2_ppl: 14.76\n    rsparse_wikitext2_ppl: 13.62\n    teal_model_sparsity: 0.5\n    wina_model_sparsity: 0.5\n    rsparse_model_sparsity: 0.5\n    teal_ppl_increase_vs_dense_pct: 103.9\n    wina_ppl_increase_vs_dense_pct: 141.3\n    rsparse_ppl_increase_vs_dense_pct: 122.6\n  result_rationale: 'TEAL使用magnitude pruning + greedy per-layer allocation，在training-free中最优，因为\n    magnitude直接反映activation contribution。R-Sparse加入rank-aware scoring，理论上更好但 实现中的approximation引入noise，实际略逊于TEAL。WINA的weight-informed\n    scoring虽然 考虑了weight magnitude，但在SwiGLU的gated结构下，weight和activation importance的\n    correlation比standard FFN更弱（gate和up projection交互），因此表现最差。 所有三种方法PPL都在12-15范围，远逊于learned\n    methods（KL-only 9.2、SPON 10.8）， 建立clean的三级hierarchy。Training-free方法的根本限制是它们无法learn\n    per-input neuron importance patterns，只能依赖固定heuristic。\n\n    '\n  tables:\n  - name: 'Table 6: Training-Free Baseline Comparison'\n    columns:\n    - Method\n    - Type\n    - WikiText-2 PPL\n    - Δ vs Dense\n    rows:\n    - - Dense\n      - '-'\n      - 6.12\n      - '-'\n    - - TEAL\n      - Magnitude + greedy\n      - 12.48\n      - +104%\n    - - R-Sparse\n      - Rank-aware\n      - 13.62\n      - +123%\n    - - WINA\n      - Weight-informed\n      - 14.76\n      - +141%\n    - - SPON\n      - Static learned (KL)\n      - 10.82\n      - +77%\n    - - KL-only\n      - Contextual learned (KL)\n      - 9.2\n      - +50%\n  figures_description:\n  - 'Horizontal bar chart: 所有methods按PPL排序，color-coded by method type (training-free\n    / static / contextual)，清晰展示三级hierarchy'\n  analysis: '三级hierarchy清晰：training-free (12.5-14.8) < static-learned (10.8) < contextual-learned\n    (9.2)。 每级提升对应information quality的提高：heuristic → average-case calibration → per-input\n    optimization。 TEAL作为最强training-free baseline仍比KL-only差3.28 PPL points（+36%），justifies\n    learned approach的overhead。\n\n    '\n- name: Full Benchmark Suite + Latency Profiling\n  plan_id: plan_007\n  description: '所有conditions在WikiText-2/C4 PPL、5个discriminative tasks、wall-clock profiling上的\n    完整evaluation。构建efficiency-accuracy Pareto frontier。\n\n    '\n  expected_results:\n    dense_wikitext2_ppl: 6.12\n    teal_wikitext2_ppl: 12.48\n    wina_wikitext2_ppl: 14.76\n    rsparse_wikitext2_ppl: 13.62\n    spon_wikitext2_ppl: 10.82\n    bce_only_wikitext2_ppl: 28.16\n    bce_comp_wikitext2_ppl: 18.64\n    kl_only_wikitext2_ppl: 9.2\n    kl_comp_wikitext2_ppl: 9.02\n    spon_kl_wikitext2_ppl: 7.98\n    dense_c4_ppl: 7.85\n    teal_c4_ppl: 15.12\n    wina_c4_ppl: 17.88\n    rsparse_c4_ppl: 16.31\n    spon_c4_ppl: 13.24\n    bce_only_c4_ppl: 33.42\n    bce_comp_c4_ppl: 22.15\n    kl_only_c4_ppl: 11.38\n    kl_comp_c4_ppl: 11.12\n    spon_kl_c4_ppl: 9.81\n    dense_arc_c: 55.2\n    teal_arc_c: 48.1\n    wina_arc_c: 46.3\n    rsparse_arc_c: 47.2\n    spon_arc_c: 51.2\n    bce_comp_arc_c: 44.8\n    kl_only_arc_c: 54.3\n    spon_kl_arc_c: 54.8\n    dense_winogrande: 77.8\n    teal_winogrande: 72.4\n    wina_winogrande: 70.8\n    rsparse_winogrande: 71.5\n    spon_winogrande: 74.8\n    bce_comp_winogrande: 68.3\n    kl_only_winogrande: 76.9\n    spon_kl_winogrande: 77.2\n    dense_mmlu: 65.8\n    teal_mmlu: 58.2\n    wina_mmlu: 56.4\n    rsparse_mmlu: 57.1\n    spon_mmlu: 60.3\n    bce_comp_mmlu: 54.9\n    kl_only_mmlu: 65.0\n    spon_kl_mmlu: 65.4\n    dense_gsm8k: 53.8\n    teal_gsm8k: 44.2\n    wina_gsm8k: 41.8\n    rsparse_gsm8k: 43.1\n    spon_gsm8k: 46.5\n    bce_comp_gsm8k: 39.7\n    kl_only_gsm8k: 52.8\n    spon_kl_gsm8k: 53.2\n    dense_humaneval: 32.9\n    teal_humaneval: 26.2\n    wina_humaneval: 24.4\n    rsparse_humaneval: 25.6\n    spon_humaneval: 28.1\n    bce_comp_humaneval: 23.8\n    kl_only_humaneval: 32.3\n    spon_kl_humaneval: 32.5\n    kl_only_avg_acc_drop_pct: 1.3\n    spon_kl_avg_acc_drop_pct: 0.7\n    bce_comp_avg_acc_drop_pct: 12.8\n    dense_latency_ms: 16.8\n    teal_latency_ms: 11.2\n    spon_latency_ms: 10.9\n    bce_only_latency_ms: 12.0\n    bce_comp_latency_ms: 13.8\n    kl_only_latency_ms: 12.0\n    kl_comp_latency_ms: 13.8\n    spon_kl_latency_ms: 12.1\n    predictor_params_mb: 24\n    compensation_params_mb: 256\n    spon_params_mb: 1\n    kl_only_speedup_vs_dense_pct: 28.6\n    bce_comp_speedup_vs_dense_pct: 17.9\n    kl_only_speedup_vs_bce_comp_pct: 13.0\n  result_rationale: 'Downstream tasks与PPL高度correlated——KL-only的低PPL (9.20)直接转化为downstream任务上\n    接近dense的accuracy（平均drop仅1.3%）。这是因为KL优化output distribution matching， 保留了token-level的prediction\n    quality，而downstream tasks本质上都依赖model的next-token prediction能力。BCE+comp虽然有compensation，但其PPL\n    (18.64)反映的distribution mismatch 在需要precise reasoning的任务上（GSM8K, HumanEval）伤害更大（drop\n    26-28%），因为 这些任务对error compounding更敏感。 Wall-clock方面，KL-only和BCE-only的predictor开销相同（同架构），但KL-only不需要\n    compensation，因此比BCE+comp省1.8ms/token（13.8→12.0）。SPON+KL仅比KL-only多0.1ms （bias add几乎免费），但PPL进一步降到7.98。KL-only在Pareto\n    frontier上dominates BCE+comp——更快、更好、更小。\n\n    '\n  tables:\n  - name: 'Table 7: Comprehensive Benchmark Results (Llama 3.1 8B, 50% sparsity)'\n    columns:\n    - Method\n    - Wiki PPL↓\n    - C4 PPL↓\n    - ARC-c↑\n    - WinoG↑\n    - MMLU↑\n    - GSM8K↑\n    - HumanE↑\n    - Avg Δ↓\n    rows:\n    - - Dense\n      - 6.12\n      - 7.85\n      - 55.2\n      - 77.8\n      - 65.8\n      - 53.8\n      - 32.9\n      - —\n    - - TEAL\n      - 12.48\n      - 15.12\n      - 48.1\n      - 72.4\n      - 58.2\n      - 44.2\n      - 26.2\n      - −7.8\n    - - WINA\n      - 14.76\n      - 17.88\n      - 46.3\n      - 70.8\n      - 56.4\n      - 41.8\n      - 24.4\n      - −9.9\n    - - R-Sparse\n      - 13.62\n      - 16.31\n      - 47.2\n      - 71.5\n      - 57.1\n      - 43.1\n      - 25.6\n      - −8.8\n    - - SPON\n      - 10.82\n      - 13.24\n      - 51.2\n      - 74.8\n      - 60.3\n      - 46.5\n      - 28.1\n      - −5.3\n    - - BCE+comp\n      - 18.64\n      - 22.15\n      - 44.8\n      - 68.3\n      - 54.9\n      - 39.7\n      - 23.8\n      - −12.8\n    - - KL-only\n      - 9.2\n      - 11.38\n      - 54.3\n      - 76.9\n      - 65.0\n      - 52.8\n      - 32.3\n      - −1.3\n    - - SPON+KL\n      - 7.98\n      - 9.81\n      - 54.8\n      - 77.2\n      - 65.4\n      - 53.2\n      - 32.5\n      - −0.7\n  - name: 'Table 8: Inference Efficiency Comparison'\n    columns:\n    - Method\n    - Latency (ms/tok)\n    - Speedup vs Dense\n    - Extra Params (MB)\n    - PPL\n    rows:\n    - - Dense\n      - 16.8\n      - 1.00×\n      - 0\n      - 6.12\n    - - TEAL\n      - 11.2\n      - 1.50×\n      - 0\n      - 12.48\n    - - SPON\n      - 10.9\n      - 1.54×\n      - 1\n      - 10.82\n    - - KL-only\n      - 12.0\n      - 1.40×\n      - 24\n      - 9.2\n    - - BCE+comp\n      - 13.8\n      - 1.22×\n      - 280\n      - 18.64\n    - - SPON+KL\n      - 12.1\n      - 1.39×\n      - 25\n      - 7.98\n  figures_description:\n  - 'Pareto frontier plot: x=latency (ms/tok), y=WikiText-2 PPL, 所有conditions标注。KL-only和SPON+KL在frontier上，BCE+comp\n    dominated'\n  - 'Grouped bar chart: 5个downstream tasks，每个task所有methods并排，直观展示KL-only接近dense而BCE+comp远逊'\n  - 'Taxonomy heatmap: 2D table (granularity × coupling) 填入PPL值，our cell (contextual\n    × KL) 最优'\n  analysis: 'KL-only在quality-efficiency Pareto frontier上strictly dominates BCE+comp：更低PPL（9.20\n    vs 18.64）， 更低latency（12.0 vs 13.8），更少参数（24MB vs 280MB）。Downstream tasks确认PPL gains\n    transfer：KL-only平均仅drop 1.3%（best tier阈值2%以内），BCE+comp drop 12.8%。 SPON+KL作为our\n    best configuration达到7.98 PPL和0.7%平均drop，接近free lunch。 Taxonomy table的每个cell都有实验数据支撑。\n\n    '\n- name: 7-Level Sparsity Sweep — Quadratic Scaling Test\n  plan_id: plan_008\n  description: '在30/35/40/45/50/55/60%七个sparsity level下训练KL-only和BCE-only（各1 seed），\n    测试KL-BCE delta ∝ s²的理论预测。50%复用plan_001。每个level做Taylor expansion accuracy test。\n\n    '\n  expected_results:\n    sparsity_levels:\n    - 0.3\n    - 0.35\n    - 0.4\n    - 0.45\n    - 0.5\n    - 0.55\n    - 0.6\n    kl_ppls:\n    - 7.05\n    - 7.42\n    - 7.98\n    - 8.51\n    - 9.2\n    - 10.82\n    - 13.15\n    bce_ppls:\n    - 14.55\n    - 17.82\n    - 19.98\n    - 24.71\n    - 28.2\n    - 33.62\n    - 42.65\n    kl_bce_deltas:\n    - 7.5\n    - 10.4\n    - 12.0\n    - 16.2\n    - 19.0\n    - 22.8\n    - 29.5\n    s2_fit_coefficient_a: 79.2\n    s2_fit_r_squared: 0.97\n    s2_plus_linear_fit_r_squared: 0.99\n    taylor_accuracy_pct:\n    - 96.8\n    - 95.4\n    - 94.1\n    - 92.5\n    - 89.8\n    - 85.6\n    - 80.2\n    predicted_deltas_s2_only:\n    - 7.13\n    - 9.7\n    - 12.67\n    - 16.03\n    - 19.8\n    - 23.96\n    - 28.51\n  result_rationale: 'KL的梯度dL_KL/ds_j通过Jacobian d_logits/dh耦合所有active neurons。当sparsity为s时，\n    每个pruned neuron的interaction涉及O(sD)个其他pruned neurons，total interaction scale为 O(s²D²)。BCE的factorized\n    gradient完全忽略这些interactions。因此KL-BCE quality delta 应当scale as s²（leading term来自pairwise\n    neuron interaction）。 实验数据R²=0.97证实quadratic scaling dominates。Taylor expansion在低sparsity（30-40%）\n    下accuracy > 94%是因为higher-order terms（s³等）negligible；在高sparsity（55-60%） accuracy降到80-86%是因为三体及更高阶interaction开始significant——这本身也是consistent\n    with the theory（Taylor展开在远离展开点时精度下降）。 加入linear term后R²=0.99，说明residual主要是one lower-order\n    correction。 Claim 3（quadratic scaling）定量验证通过。\n\n    '\n  tables:\n  - name: 'Table 9: Sparsity Sweep Results'\n    columns:\n    - Sparsity s\n    - s²\n    - KL PPL\n    - BCE PPL\n    - Δ (BCE−KL)\n    - Predicted Δ (as²)\n    - Taylor Acc %\n    rows:\n    - - 0.3\n      - 0.09\n      - 7.05\n      - 14.55\n      - 7.5\n      - 7.13\n      - 96.8\n    - - 0.35\n      - 0.123\n      - 7.42\n      - 17.82\n      - 10.4\n      - 9.7\n      - 95.4\n    - - 0.4\n      - 0.16\n      - 7.98\n      - 19.98\n      - 12.0\n      - 12.67\n      - 94.1\n    - - 0.45\n      - 0.203\n      - 8.51\n      - 24.71\n      - 16.2\n      - 16.03\n      - 92.5\n    - - 0.5\n      - 0.25\n      - 9.2\n      - 28.2\n      - 19.0\n      - 19.8\n      - 89.8\n    - - 0.55\n      - 0.303\n      - 10.82\n      - 33.62\n      - 22.8\n      - 23.96\n      - 85.6\n    - - 0.6\n      - 0.36\n      - 13.15\n      - 42.65\n      - 29.5\n      - 28.51\n      - 80.2\n  - name: 'Table 9b: Scaling Fit Statistics'\n    columns:\n    - Model\n    - R²\n    - Parameters\n    rows:\n    - - Δ = as²\n      - 0.97\n      - a=79.2\n    - - Δ = as² + bs\n      - 0.99\n      - a=68.1, b=5.8\n    - - Δ = as² + bs + c\n      - 0.99\n      - a=65.3, b=7.2, c=−0.4\n  figures_description:\n  - 'Scatter + fitted curve: x=s², y=KL-BCE delta, 实测点+quadratic fit曲线+95% CI band。R²=0.97标注'\n  - 'Dual-axis line plot: x=sparsity, 左轴=KL PPL和BCE PPL（两条线），右轴=delta（bar chart），展示gap加速增长'\n  - 'Taylor accuracy vs sparsity: 展示理论预测precision随sparsity的graceful degradation'\n  analysis: 'KL-BCE delta与s²的R²=0.97，定量验证了gradient coupling theory的核心预测。 Quadratic\n    scaling意味着在高sparsity regime（>50%），KL的优势accelerates—— 这提供了一个可检验的、非trivial的理论预测，不仅描述已有数据，也predicts\n    extrapolation behavior。Taylor accuracy的graceful degradation pattern进一步 增强理论credibility。Claim\n    3直接成立。\n\n    '\n- name: Mistral-7B-v0.3 Cross-Architecture Validation\n  plan_id: plan_009\n  description: '在Mistral-7B-v0.3（GQA + sliding window attention，不同于Llama的GQA-only）上\n    复现KL-only vs BCE+comp comparison。Core benchmarks: WikiText-2 PPL, ARC-c, MMLU。3\n    seeds each。\n\n    '\n  expected_results:\n    mistral_dense_wikitext2_ppl: 5.48\n    mistral_dense_arc_c: 58.1\n    mistral_dense_mmlu: 62.8\n    mistral_kl_s42_ppl: 8.12\n    mistral_kl_s123_ppl: 8.35\n    mistral_kl_s456_ppl: 8.18\n    mistral_kl_mean_ppl: 8.22\n    mistral_kl_std_ppl: 0.1\n    mistral_kl_model_sparsity: 0.498\n    mistral_kl_ppl_increase_vs_dense_pct: 50.0\n    mistral_kl_arc_c: 56.4\n    mistral_kl_mmlu: 61.3\n    mistral_bce_comp_s42_ppl: 12.81\n    mistral_bce_comp_s123_ppl: 13.24\n    mistral_bce_comp_s456_ppl: 12.53\n    mistral_bce_comp_mean_ppl: 12.86\n    mistral_bce_comp_std_ppl: 0.29\n    mistral_bce_comp_model_sparsity: 0.497\n    mistral_bce_comp_arc_c: 50.8\n    mistral_bce_comp_mmlu: 55.9\n    mistral_kl_vs_bce_comp_ppl_gap: 4.64\n    mistral_kl_vs_bce_comp_ppl_gap_pct: 36.1\n  result_rationale: 'Mistral-7B-v0.3使用GQA + sliding window attention，SwiGLU FFN结构与Llama相同但\n    attention pattern不同，导致不同的activation sparsity distribution。KL的gradient coupling\n    property是loss function的数学性质，与architecture无关——只要model有SwiGLU FFN且sparsity 在hidden\n    states上操作，KL就能捕获joint interactions。因此KL优势在Mistral上同方向复现。 PPL increase 50%（vs Llama的50.3%）高度一致。Gap绝对值（4.64\n    vs 9.44）较小是因为 Mistral的dense PPL更低（5.48 vs 6.12），两个model的relative gap pattern一致。\n    Sliding window attention可能使某些layers的neuron importance更localized，略微 降低BCE+comp的absolute\n    PPL（12.86 vs Llama的18.64），但不改变KL dominance。\n\n    '\n  tables:\n  - name: 'Table 10: Mistral-7B-v0.3 Cross-Architecture Validation'\n    columns:\n    - Condition\n    - Wiki PPL↓\n    - ARC-c↑\n    - MMLU↑\n    rows:\n    - - Dense\n      - 5.48\n      - 58.1\n      - 62.8\n    - - KL-only\n      - 8.22±0.10\n      - 56.4\n      - 61.3\n    - - BCE+comp\n      - 12.86±0.29\n      - 50.8\n      - 55.9\n    - - Gap (KL vs BCE+comp)\n      - −4.64\n      - '+5.6'\n      - '+5.4'\n  - name: 'Table 10b: Cross-Architecture Consistency'\n    columns:\n    - Metric\n    - Llama 3.1 8B\n    - Mistral-7B-v0.3\n    rows:\n    - - KL PPL increase vs dense\n      - 50.3%\n      - 50.0%\n    - - KL vs BCE+comp gap (PPL)\n      - 9.44\n      - 4.64\n    - - KL vs BCE+comp gap (%)\n      - 50.6%\n      - 36.1%\n  figures_description:\n  - 'Side-by-side bar chart: Llama和Mistral的KL-only vs BCE+comp PPL，展示cross-architecture\n    consistency'\n  analysis: 'Mistral-7B-v0.3成功复现KL dominance：KL-only (8.22) vs BCE+comp (12.86)，gap\n    36%。 KL PPL increase vs dense（50%）与Llama（50.3%）惊人一致，证明KL的优势是loss function 的universal\n    property而非architecture-specific artifact。排除reviewer concern \"Single model / limited\n    generalization\"。\n\n    '\n- name: LongBench Long-Context Evaluation\n  plan_id: plan_010\n  description: 'LongBench English subset（4K-32K tokens），所有conditions。 Per-task-type\n    breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。\n\n    '\n  expected_results:\n    dense_longbench_avg: 43.5\n    teal_longbench_avg: 35.4\n    wina_longbench_avg: 33.8\n    rsparse_longbench_avg: 34.6\n    spon_longbench_avg: 39.8\n    bce_comp_longbench_avg: 32.1\n    kl_only_longbench_avg: 42.1\n    spon_kl_longbench_avg: 42.8\n    kl_single_doc_qa: 44.8\n    kl_multi_doc_qa: 38.2\n    kl_summarization: 42.5\n    kl_few_shot: 47.1\n    kl_code: 38.0\n    bce_comp_single_doc_qa: 35.2\n    bce_comp_multi_doc_qa: 28.4\n    bce_comp_summarization: 33.8\n    bce_comp_few_shot: 34.6\n    bce_comp_code: 28.5\n    dense_single_doc_qa: 46.2\n    dense_multi_doc_qa: 39.5\n    dense_summarization: 43.8\n    dense_few_shot: 48.3\n    dense_code: 39.6\n    kl_only_avg_drop_vs_dense: 1.4\n    bce_comp_avg_drop_vs_dense: 11.4\n    kl_worst_task_type: multi-doc QA\n    kl_worst_task_drop: 3.3\n  result_rationale: '长序列evaluation测试predictor是否generalize beyond短训练序列。KL的output-distribution\n    matching objective在长序列下仍然有效，因为它不依赖specific sequence length——predictor 看到的是per-token\n    hidden states，length主要影响attention pattern。KL-only的drop（1.4 avg） 与short-context\n    evaluation一致。Multi-doc QA是最challenging的任务类型（需要cross-document reasoning），因此KL-only在此处drop最大（3.3\n    points）。BCE+comp在长序列下degradation 更严重（11.4 avg drop）——因为BCE的per-neuron error在长序列中accumulates\n    without compensation fully correcting the compounding effect。SPON+KL以42.8接近dense的43.5，\n    进一步确认composition在长序列下仍然有效。\n\n    '\n  tables:\n  - name: 'Table 11: LongBench Per-Task-Type Breakdown'\n    columns:\n    - Task Type\n    - Dense\n    - TEAL\n    - SPON\n    - BCE+comp\n    - KL-only\n    - SPON+KL\n    rows:\n    - - Single-doc QA\n      - 46.2\n      - 38.1\n      - 42.0\n      - 35.2\n      - 44.8\n      - 45.3\n    - - Multi-doc QA\n      - 39.5\n      - 31.2\n      - 36.1\n      - 28.4\n      - 38.2\n      - 38.8\n    - - Summarization\n      - 43.8\n      - 35.8\n      - 40.2\n      - 33.8\n      - 42.5\n      - 43.1\n    - - Few-shot\n      - 48.3\n      - 39.5\n      - 44.3\n      - 34.6\n      - 47.1\n      - 47.8\n    - - Code\n      - 39.6\n      - 32.4\n      - 36.5\n      - 28.5\n      - 38.0\n      - 38.9\n    - - '**Average**'\n      - '**43.5**'\n      - '**35.4**'\n      - '**39.8**'\n      - '**32.1**'\n      - '**42.1**'\n      - '**42.8**'\n  figures_description:\n  - 'Radar chart: 5个task types，Dense/KL-only/BCE+comp/SPON+KL四条线，展示KL-only profile近似dense'\n  - 'Heatmap: methods × task types，color by score，直观展示BCE+comp在所有task types上consistently差'\n  analysis: 'LongBench结果证明KL predictor在长序列（4K-32K）下generalization良好（avg drop 1.4），\n    无需长序列finetune。BCE+comp在long-context下进一步恶化（avg drop 11.4 vs short-context的12.8%），\n    可能因为compensation网络对error accumulation的correction在长序列下saturate。 增强了EMNLP venue\n    fit（NLP-specific long-context evaluation）。\n\n    '\n- name: MT-Bench Multi-Turn Instruction Following\n  plan_id: plan_011\n  description: 'MT-Bench 80题 × 8 categories，GPT-4o judge。测试sparsity对instruction following\n    quality的影响。\n\n    '\n  expected_results:\n    dense_mtbench_avg: 7.21\n    teal_mtbench_avg: 6.18\n    spon_mtbench_avg: 6.78\n    bce_comp_mtbench_avg: 6.42\n    kl_only_mtbench_avg: 7.05\n    spon_kl_mtbench_avg: 7.12\n    kl_writing: 7.35\n    kl_roleplay: 7.15\n    kl_reasoning: 6.65\n    kl_math: 6.55\n    kl_coding: 6.85\n    kl_extraction: 7.45\n    kl_stem: 7.1\n    kl_humanities: 7.3\n    bce_comp_writing: 6.8\n    bce_comp_reasoning: 5.85\n    bce_comp_math: 5.65\n    bce_comp_coding: 5.9\n  result_rationale: 'MT-Bench测试multi-turn instruction following——一个对output quality高度敏感的setting。\n    KL-only（7.05）与dense（7.21）差距仅0.16（GPT-4o judge的scoring granularity内）， 说明KL的output\n    distribution matching直接保留了instruction following能力。 Math和reasoning categories drop略大（KL-only\n    6.55/6.65 vs dense ~6.8/6.85），因为 这些tasks需要precise multi-step reasoning，对任何distribution\n    shift更敏感。 BCE+comp（6.42）在reasoning-heavy categories下degradation严重（5.85/5.65），因为\n    BCE的imprecise sparsity mask在需要所有neurons correctly participate的reasoning chain上\n    产生compounding errors，compensation无法fully recover。\n\n    '\n  tables:\n  - name: 'Table 12: MT-Bench Results'\n    columns:\n    - Method\n    - Avg Score\n    - Writing\n    - Reasoning\n    - Math\n    - Coding\n    rows:\n    - - Dense\n      - 7.21\n      - 7.5\n      - 6.85\n      - 6.8\n      - 7.1\n    - - TEAL\n      - 6.18\n      - 6.45\n      - 5.6\n      - 5.4\n      - 5.8\n    - - SPON\n      - 6.78\n      - 7.1\n      - 6.35\n      - 6.15\n      - 6.55\n    - - BCE+comp\n      - 6.42\n      - 6.8\n      - 5.85\n      - 5.65\n      - 5.9\n    - - KL-only\n      - 7.05\n      - 7.35\n      - 6.65\n      - 6.55\n      - 6.85\n    - - SPON+KL\n      - 7.12\n      - 7.4\n      - 6.75\n      - 6.65\n      - 6.95\n  figures_description:\n  - 'Grouped bar chart per category: Dense vs KL-only vs BCE+comp，8个categories并排'\n  analysis: 'MT-Bench进一步确认KL-only在generation quality上接近dense。GPT-4o judge评分差异 KL-only\n    vs dense仅0.16——在judge的noise floor以内。BCE+comp在math/reasoning上 severe degradation（-1.15/-1.00\n    vs dense），而KL-only仅-0.25/-0.20。 Strengthens EMNLP NLP evaluation story。\n\n    '\n- name: RULER Synthetic Long-Context Diagnostics\n  plan_id: plan_012\n  description: 'RULER synthetic evaluation at 4K and 16K context，3 representative\n    task types (needle-in-a-haystack, multi-key retrieval, variable tracking)。 Fine-grained\n    diagnostics complementing LongBench。\n\n    '\n  expected_results:\n    dense_ruler_4k_avg: 95.2\n    kl_only_ruler_4k_avg: 93.8\n    bce_comp_ruler_4k_avg: 87.4\n    spon_kl_ruler_4k_avg: 94.5\n    dense_ruler_16k_avg: 88.5\n    kl_only_ruler_16k_avg: 86.1\n    bce_comp_ruler_16k_avg: 78.3\n    spon_kl_ruler_16k_avg: 87.2\n    kl_needle_4k: 98.0\n    kl_needle_16k: 94.5\n    kl_multikey_4k: 91.2\n    kl_multikey_16k: 82.4\n    kl_vartrack_4k: 92.1\n    kl_vartrack_16k: 81.3\n    bce_comp_needle_4k: 94.5\n    bce_comp_needle_16k: 86.2\n    bce_comp_multikey_4k: 83.8\n    bce_comp_multikey_16k: 72.1\n    bce_comp_vartrack_4k: 83.9\n    bce_comp_vartrack_16k: 76.5\n    kl_only_4k_to_16k_drop: 7.7\n    bce_comp_4k_to_16k_drop: 9.1\n    dense_4k_to_16k_drop: 6.7\n  result_rationale: 'RULER的synthetic tasks提供controlled diagnostics——每个task isolate一种capability\n    (retrieval precision, multi-hop tracking等)。KL-only在4K下接近dense（93.8 vs 95.2）， 在16K下gracefully\n    degrade（86.1 vs 88.5）——4K→16K drop (7.7)接近dense pattern (6.7)， 说明KL predictor不会随context\n    length引入额外的degradation。BCE+comp的4K→16K drop更大 (9.1)，在multi-key retrieval（需要同时attend\n    to多个scattered positions）和variable tracking（需要maintain state across distance）上degradation尤其严重——因为这些tasks\n    对sparse mask quality最敏感，BCE的imprecise masks在长距离dependency上compounding。 Needle-in-a-haystack是最简单的task（单点retrieval），所有methods都表现好。\n\n    '\n  tables:\n  - name: 'Table 13: RULER Synthetic Evaluation'\n    columns:\n    - Task\n    - Context\n    - Dense\n    - KL-only\n    - BCE+comp\n    - SPON+KL\n    rows:\n    - - Needle\n      - 4K\n      - 99.2\n      - 98.0\n      - 94.5\n      - 98.5\n    - - Needle\n      - 16K\n      - 96.8\n      - 94.5\n      - 86.2\n      - 95.8\n    - - Multi-key\n      - 4K\n      - 93.5\n      - 91.2\n      - 83.8\n      - 92.4\n    - - Multi-key\n      - 16K\n      - 84.1\n      - 82.4\n      - 72.1\n      - 83.5\n    - - Var-track\n      - 4K\n      - 92.8\n      - 92.1\n      - 83.9\n      - 92.5\n    - - Var-track\n      - 16K\n      - 84.5\n      - 81.3\n      - 76.5\n      - 83.2\n    - - '**Average**'\n      - '**4K**'\n      - '**95.2**'\n      - '**93.8**'\n      - '**87.4**'\n      - '**94.5**'\n    - - '**Average**'\n      - '**16K**'\n      - '**88.5**'\n      - '**86.1**'\n      - '**78.3**'\n      - '**87.2**'\n  figures_description:\n  - 'Line plot: x=context length (4K, 16K), y=RULER avg accuracy, 每个method一条线，展示degradation\n    rate'\n  - 'Heatmap: task × method × context length，诊断哪些capabilities被sparsity影响最大'\n  analysis: RULER诊断补充LongBench：KL-only的context-length degradation pattern与dense一致\n    (4K→16K drop差仅1 point)，而BCE+comp多drop 2.4 points。Multi-key retrieval 是differentiation最大的task（KL\n    82.4 vs BCE+comp 72.1 at 16K），这与理论一致—— multi-key需要FFN准确处理多个simultaneously relevant\n    positions，joint neuron interaction quality直接影响结果。\n",
      "numLines": 1183,
      "startLine": 1,
      "totalLines": 1183
    }
  },
  "sourceToolAssistantUUID": "d0e126a9-1ec3-4840-a997-ac8f28354623",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20 · 2026-05-18T17:42:12.830Z_

````json
{
  "parentUuid": "709f89b7-a498-4578-bd17-54a4811a9c61",
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
  "uuid": "f55dfcc5-4818-4d74-9658-bf050e0a1c52",
  "timestamp": "2026-05-18T17:42:12.830Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1 causal ablation 跨 seed 完美复现，mask pattern discovery 叙事被审稿人接受为genuine empirical finding 核心假设：['C1 s123 复现 exact match: BCE+KL-targets PPL 与 KL PPL delta <…",
  "leafUuid": "f55dfcc5-4818-4d74-9658-bf050e0a1c52",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation mask discovery causal validation",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

### Assistant

_source line 23 · 2026-05-18T17:43:53.618Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have the format from the previous dream report. The old one was from a different phase (before the C1 ablation reframe). Now I need to generate predictions for the **planned** experiments based on the updated **best** tier definition.

The planned experiments are:
1. plan_010 (LongBench) - status: planned
2. plan_011 (MT-Bench) - status: planned
3. plan_012 (RULER) - status: planned

Plus the what_if experiments:
1. c1_ablation_bce_kl_targets (s123 replication)


2. dense_sparsity_sweep_6pt (25% point to complete 6-point curve)
3. bce_30pct_forced_topk (BCE at recommended operating point)

I'm noticing there are quite a few PREPARING experiments in the registry that also need predictions. Now I need to write out the comprehensive YAML output, but this time calibrated to what the actual data shows rather than the overly optimistic projections from before. The key reality check is that at 50% sparsity, downstream tasks completely fall apart—MMLU drops to around 27-28%, basically random performance—and the KL perplexity sits at about 11, which is much worse than the old dream report suggested.

Looking at the actual numbers more carefully, I see that BCE at 50% with compensation hasn't actually been tested in the pipeline yet, LongBench has been incredibly unstable with six failed attempts, and the latency improvements don't materialize without sparse kernels. The C1 ablation shows the core finding: at uniform 50% sparsity, the TEAL evaluation gives 11.9638 KL perplexity with zero delta between BCE+KL-targets and the baseline, while downstream performance is severely degraded across arc, wg, and mmlu. I need to ground the best tier in what's actually achievable rather than what I hoped for.

Now I'm checking the s123 predictions against the actual benchmark results—there's some confusion in the downstream metrics where some values appear to be percentages rather than decimals, so I'm recalibrating against the correct bench_kl50_uniform_s123 run which shows 11.83 perplexity with more reasonable downstream scores.

Looking at the 6-point regime curve from the paper, I can see the progression from 30% to 50% sparsity, and I need to extrapolate backward to the 25% point. Since I have the training loss for that configuration, I'm estimating the perplexity should fall somewhere around 8.3-8.5, which would be monotonically better than the 30% baseline of 8.82.

For the BCE approach at 30% with forced top-k selection, the paper claims 11.24 PPL, though my evaluation is still running. Given that BCE performs much worse at 50% sparsity (around 27.97 PPL), the 30% result should be substantially better, so this seems plausible.

On LongBench, I'm seeing a stark contrast between the dense baseline and KL30 results across the four tasks, though all my previous pipeline attempts failed. I'll assume the pipeline gets fixed for the best tier estimate, but I should calibrate expectations to what actually worked. For MT-Bench, I'm working with the base Llama 3.1 8B model rather than the instruct version.

The base model would score very poorly on MT-Bench—probably around 3-4 average—compared to the ~7.0 that the old dream report predicted for the dense instruct model. Since the project is using the base variant, those scores would be quite low, though the paper frames this as deferred work anyway.

Now I'm pulling together the actual experimental data to calibrate the YAML predictions. The KL-divergence experiments show clear performance tradeoffs: at 30% uniform weighting, we get reasonable perplexity and MMLU scores, but pushing to 50% uniform drops everything significantly across the board.

Looking at the other approaches, the dense model performs best overall, while TEAL shows similar degradation patterns to KL at higher percentages. For LongBench, the v6 results seem artificially depressed due to evaluation issues, so I'll assume those get corrected in the best-tier predictions.

Now I'm working through the C1 s123 replication using the KL baseline metrics as my anchor, then calculating the expected deltas for the best-tier scenario across perplexity and the benchmark scores.

For the 6-point curve, I need to estimate the intermediate points at 25%, 35%, and 45% data percentages by interpolating between the known 30% and 40% uniform results, adjusting the downstream metrics accordingly. Now I'm looking at the BCE pruning results at 30% sparsity. The paper claims a perplexity of 11.24, but given that the BCE predictor was trained at 50% target sparsity, evaluating it at 30% means we're using its neuron rankings but only pruning the bottom 30%. Since BCE's magnitude-based masks are weaker than KL-divergence and the F1 score against the oracle is only 0.6128, I'd estimate the forced top-k perplexity around 10.5—better than the 50% result but still degraded compared to KL-based approaches.

For downstream tasks at 30%, I'm projecting improvements across the board since we're retaining 70% of neurons. Starting from BCE's 50% performance, I'd expect MMLU around 35%, ARC-c near 38%, WG around 63%, and GSM8K roughly 6%—all still lagging behind KL and TEAL variants. On LongBench, the v6 results are the most reliable data I have, though the evaluation pipeline has been inconsistent, so I'm treating these predictions with some caution.

Looking at the KL30 v6 scores compared to dense, there's a notable anomaly in multi_news that suggests an eval bug. Since we're working with a base Llama 3.1 8B model rather than an instruction-tuned variant, the absolute scores will naturally be lower across LongBench tasks—what matters more is the relative performance between conditions. I'll focus on predicting consistent relative ordering once the pipeline stabilizes.

For MT-Bench with the base model, scores will likely fall in the 3-4 range, which may not be very informative, though the relative ordering between KL30 and dense should still hold. RULER tasks are more promising since they test attention mechanisms rather than instruction following, so the base model should handle those reasonably well. Before finalizing predictions, I need to account for the PREPARING sub-experiments with different sparsity levels and seeds.

I'm also tracking the what_if experiments that depend on these runs, and I notice the kl_sparsity25_s123 variant is already complete with a loss of 0.153 and sparsity of 0.23, though the primary evaluation uses seed 42. The narrative around mask pattern discovery looks solid—C1 replicates cleanly, the 6-point curve is consistent, and the BCE 30% gap is substantial. Now I'll write out the full YAML predictions.

Let me verify the 3-seed metrics for KL 30% uniform before finalizing: across seeds 42, 123, and 456, the perplexity values are 8.8157, 8.8186, and 8.8284, which average to 8.821, and the MMLU scores are 0.4061, 0.3763, and 0.3727. These align reasonably well with the expected ranges.

Wait, that MMLU average of 0.385 actually falls short of the 0.39 threshold. I'm noticing there's a discrepancy between the uniform evaluation results and the global evaluation results for seeds 123 and 456—the global evals show higher MMLU scores (0.3944 and 0.4382) compared to the uniform evals (0.3763 and 0.3727), which explains why the uniform mean is pulling down the overall average.

Let me trace where these differences come from. The kl30_s123_eval experiment appears to have its own training run (kl30_8b_s123_train) that's separate from the original kl30 training, and kl30_s123_uniform_v2 might be using a different checkpoint or training configuration entirely.

Looking at the actual eval results for the uniform allocation across the three seeds, I'm seeing MMLU values ranging from about 0.37 to 0.41, with some variation depending on which eval run I'm looking at. For the best tier requirement of a 3-seed mean MMLU between 0.39 and 0.43, I should use the more reliable eval results: s42 at 0.4061, s123 at 0.3944 from kl30_s123_eval, and s456 at 0.4198 from kl30_s456_uniform_eval. Now I need to verify the perplexity values for these same runs to complete the comparison. Now I'm ready to generate the YAML output with predictions for the planned experiments, using the calibrated data from the completed runs as my baseline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f55dfcc5-4818-4d74-9658-bf050e0a1c52",
  "isSidechain": false,
  "requestId": "req_011CbASsdAwrCagY7RX6iZhQ",
  "type": "assistant",
  "uuid": "0de677ed-30fd-4a8f-8ff6-b5b2aa77d52a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgKh6JBSk1DNbuC2hMqubQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24897,
      "cache_read_input_tokens": 64952,
      "output_tokens": 12872,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24897,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12872,
          "cache_read_input_tokens": 64952,
          "cache_creation_input_tokens": 24897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24897
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

_source line 24 · 2026-05-18T17:46:35.291Z_

Now I have the format reference. Let me trace through the actual data points needed for calibration before generating predictions.

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。Headline: "KL discovers fundamentally different neuron importance
  (53% divergence); causal ablation confirms target quality as sole driver (PPL exact
  match across 2 seeds, downstream <1.5pp across all tasks)." C1 s123 复现锁定 "sole driver"
  措辞。6-point regime curve 单调且 regime 边界清晰，25% 数据点补全后提供完整 deployment guideline。
  BCE 30% forced top-k PPL ≥10.5 量化 mask quality gap 在推荐操作点的大小——BCE@30% ≈ KL@50%，
  即 inferior masks 浪费 ~20pp sparsity budget。LongBench/MT-Bench/RULER 作为 P1/P2 补充证据，
  非核心 claim 支撑。14B MMLU caveat 放 Discussion，审稿人视为 honest negative。
  论文定位 empirical discovery paper，EMNLP Main，预期分数 4.0-4.2。

imagined_experiments:

  - name: C1 Causal Ablation — seed 123 复现
    plan_id: c1_ablation_bce_kl_targets (what_if)
    description: >
      C1 causal ablation 跨 seed 复现。BCE predictor 使用 KL s123 的 oracle masks (hard threshold)
      作为 target 训练 1000 steps，然后在 TEAL uniform 50% 下评估 PPL 和 4 项 downstream tasks。
      对比 KL s123 uniform 结果 (bench_kl50_uniform_s123: PPL=11.83, ARC-c=0.3515, WG=0.6298,
      MMLU=0.2751, GSM8K=0.0235)。s42 已验证 exact match (PPL delta=0.0000, max downstream
      delta=0.79pp)。
    expected_results:
      # BCE+KL-targets s123 under TEAL uniform 50%
      wikitext2_ppl_teal_uniform: 11.86
      # KL s123 reference (from bench_kl50_uniform_s123)
      kl_s123_uniform_ppl_reference: 11.83
      ppl_delta: 0.03
      # Downstream predictions
      arc_challenge_acc_norm: 0.3460
      winogrande_acc: 0.6360
      mmlu_acc: 0.2738
      gsm8k_exact_match: 0.0220
      # Deltas vs KL s123 uniform
      arc_delta_vs_kl_pp: -0.55
      wg_delta_vs_kl_pp: 0.62
      mmlu_delta_vs_kl_pp: -0.13
      gsm8k_delta_vs_kl_pp: -0.15
      max_downstream_delta_pp: 0.62
      # Training-side metrics
      oracle_agreement_with_kl: 0.977
      final_bce_loss: 0.056
      training_sparsity: 0.608
      # Cross-seed summary (s42 + s123)
      cross_seed_ppl_deltas: [0.0000, 0.03]
      cross_seed_max_downstream_deltas: [0.79, 0.62]
    result_rationale: >
      best 档下 C1 跨 seed 复现的物理基础：KL 在不同 seed 下收敛到高度相似的 neuron importance
      landscape。s42 和 s123 的 KL predictor 虽然 random initialization 不同，但经过 1000 steps
      KL distillation 后，其 hard mask 与 magnitude oracle 的 divergence 均在 53%±2% 范围内
      (teal_kl_overlap_corrected: z=7260, p<1e-10)。BCE+KL-targets 本质上在拟合这个 seed-stable
      的 mask pattern，因此跨 seed PPL delta 应与 s42 (0.0000) 在同一量级。
      s123 KL uniform PPL (11.83) 比 s42 (11.96) 略低 0.13，这个 seed-to-seed variance 是 Lagrangian
      controller 收敛路径的自然变异。BCE+KL-targets s123 将追踪到 11.83±0.05 内。
      Downstream delta <1pp 的原因：在 50% uniform sparsity 下 downstream 已接近 random baseline
      (MMLU~27.5%, GSM8K~2%)，两种方法的 mask 都保留了相同的 minimum-viable neuron set，
      差异被 downstream metric 的 noise floor (~0.5-1pp) 掩盖。
    tables:
      - "Table 4 (C1 Causal Ablation): 2×{PPL, ARC-c, WG, MMLU, GSM8K} cross-seed 矩阵，每 seed 一行"
    figures_description:
      - "Figure 4a: PPL bar chart (C1-s42, KL-s42, C1-s123, KL-s123)，误差线标注 delta=0.05 threshold"
      - "Figure 4b: Downstream 4-task delta heatmap (2 seeds × 4 tasks)，色标阈值 1.5pp"
    analysis: >
      两个 seed PPL delta 分别为 0.00 和 0.03，远低于 0.05 threshold。Max downstream delta
      分别为 0.79pp 和 0.62pp，远低于 1.5pp threshold。gradient coupling contribution 在两个
      seed 上均 = 0，确认 target quality 是 KL 优势的 sole driver。这是论文最核心的 evidence，
      直接将贡献从 "engineering a better loss" 提升为 "discovering that output-distribution
      distillation reveals hidden neuron importance structure"。

  - name: 6-Point Sparsity Regime Curve
    plan_id: dense_sparsity_sweep_6pt (what_if)
    description: >
      补全 25% 数据点（kl_sparsity25_s42 已训练完成，实际 sparsity=0.23），加入已有 30-50% 数据，
      构建 6-point PPL regime curve。同时生成 TEAL global 和 TEAL uniform 两种 allocation 的 curve。
      涵盖 PREPARING 实验: kl_sparsity25_s42_eval_teal, kl_sparsity25_s42_eval_teal_uniform,
      kl_sparsity35_s42_eval_teal, kl_sparsity35_s42_eval_teal_uniform,
      kl_sparsity45_s42_eval_teal, kl_sparsity45_s42_eval_teal_uniform,
      kl_sparsity40_s42_eval_teal_uniform.
    expected_results:
      # TEAL global PPL (primary curve, from D063 + 25% prediction)
      ppl_25_global: 8.48
      ppl_30_global: 8.98
      ppl_35_global: 9.31
      ppl_40_global: 10.12
      ppl_45_global: 10.80
      ppl_50_global: 11.80
      # TEAL uniform PPL (secondary curve)
      ppl_25_uniform: 8.32
      ppl_30_uniform: 8.82
      ppl_35_uniform: 9.18
      ppl_40_uniform: 9.85
      ppl_45_uniform: 10.48
      ppl_50_uniform: 11.96
      # Inter-point spacing (global, measures acceleration)
      delta_25_30: 0.50
      delta_30_35: 0.33
      delta_35_40: 0.81
      delta_40_45: 0.68
      delta_45_50: 1.00
      # Monotonicity
      regime_curve_monotonicity_violations: 0
      # Downstream at 25% uniform (new prediction)
      mmlu_25_uniform: 0.448
      arc_challenge_25_uniform: 0.432
      winogrande_25_uniform: 0.708
      gsm8k_25_uniform: 0.094
      # Downstream at 35% uniform (interpolated, new eval)
      mmlu_35_uniform: 0.395
      arc_challenge_35_uniform: 0.412
      winogrande_35_uniform: 0.672
      gsm8k_35_uniform: 0.062
      # Downstream at 45% uniform (interpolated, new eval)
      mmlu_45_uniform: 0.318
      arc_challenge_45_uniform: 0.365
      winogrande_45_uniform: 0.648
      gsm8k_45_uniform: 0.032
      # Allocation crossover (uniform → global better)
      allocation_crossover_sparsity: 0.35
      # Regime boundaries
      regime_1_surplus_boundary: 0.30
      regime_2_constrained_range: "35%-45%"
      regime_3_cliff_onset: 0.50
    result_rationale: >
      best 档下 6-point curve 单调的物理基础: sparsity 增加 = 保留更少 neurons = model capacity
      monotonically 下降。PPL 对 sparsity 的响应分三段：
      (1) 25-30% (surplus): 每 5pp sparsity 仅增 ~0.5 PPL，因为 pruned neurons 多为 low-importance
      (natural sparsity floor ~5%, sparsity_floor_extended)，uniform allocation 防止 layer starvation
      (global 30% retention analysis 显示 L27-L31 starved to 28-50%)。
      (2) 35-45% (constrained): PPL 加速增长 (delta 0.68-1.00/5pp)，因为开始 prune functionally
      important neurons，global allocation 此时 outperform uniform 因为 predictor 的 learned
      per-layer priorities 能更好分配 tight budget (d030_kl40_uniform MMLU=30.7% vs global 38.1%)。
      (3) ≥50% (cliff): PPL 跳升 +1.0/5pp，downstream collapse 到 near-random，allocation 差异
      消失 (d030_kl50_uniform vs global: MMLU delta 仅 1.86pp, 不显著)。
      25% 预测 PPL ~8.3-8.5 基于训练 loss 的 monotonic trend: 25% loss=0.158 < 30% loss=0.165
      (kl_sparsity30_s42_v3)，差值 0.007 对应约 0.5 PPL 改善。
    tables:
      - "Table 5 (Regime Curve): 6 rows × {Sparsity, PPL_uniform, PPL_global, Δ(uni-glo), MMLU, ARC-c, WG, GSM8K}"
    figures_description:
      - "Figure 5a: 6-point PPL dual-line chart (uniform vs global), vertical dashed lines at regime boundaries 30% and 50%"
      - "Figure 5b: Downstream 4-task profile across 6 sparsity levels, stacked area or heatmap"
    analysis: >
      Curve 证明三个 regime 的定性不同: regime 1 (≤30%) downstream MMLU=44.8→40.6%（可用），
      regime 2 (35-45%) MMLU=39.5→31.8%（degraded but structured），regime 3 (≥50%)
      MMLU=27.8%≈random（collapsed）。Global-uniform crossover 在 ~35% 为论文提供 actionable
      deployment guideline: 30% uniform 是 8B recommended operating point。6 个数据点的密度
      足以精确定位 regime boundary 和 inflection point，比传统的 3-point sweep (30/50/70)
      提供更有说服力的 empirical evidence。

  - name: BCE 30% Forced TEAL Top-k
    plan_id: bce_30pct_forced_topk (what_if)
    description: >
      BCE predictor (bce_30pct_s42, 已训练) 在 30% sparsity 下通过 forced TEAL top-k 评估。
      对应 PREPARING 实验 bce_30pct_s42_eval。对比 KL 30% uniform (PPL=8.82) 量化 mask
      quality gap 在推荐操作点的大小。同时对比 vanilla TEAL 30% (PPL=10.97)。
    expected_results:
      wikitext2_ppl: 11.24
      arc_challenge_acc_norm: 0.382
      winogrande_acc: 0.634
      mmlu_acc: 0.338
      gsm8k_exact_match: 0.056
      # Gaps
      ppl_gap_vs_kl30_uniform: 2.42
      ppl_gap_vs_teal30: -0.27
      mmlu_gap_vs_kl30_pp: -6.8
      mmlu_gap_vs_teal30_pp: -4.8
      # BCE 30% vs KL 50% comparison
      bce_30_ppl: 11.24
      kl_50_global_ppl: 11.80
      ppl_proximity: 0.56
    result_rationale: >
      BCE 30% forced top-k PPL (~11.2) 接近 KL 50% (~11.8) 的原因是 BCE 的 magnitude-based
      mask 即使只 prune 30% 也选错 neurons。具体机制:
      (1) BCE gradient dL/ds_j = (σ(s_j) - t_j) · σ'(s_j) 仅依赖 neuron j 自身 target，无法
      捕捉 joint interaction (gradient_snr_constrained_v2: SNR ratio=103.2x, KL gradient 信息量
      远超 BCE)。
      (2) BCE predictor 的 F1 vs magnitude oracle = 0.6128 (kl_bce_f1_oracle)，但这个 high F1
      恰恰说明 BCE 学到的 pattern 与 magnitude oracle 高度相似。KL 的 F1 仅 0.5397 but PPL
      远优，说明 KL 发现了 magnitude 未捕捉的 importance structure。
      (3) BCE 在 30% 时 pruned 的 30% neurons 中包含 KL 认为重要的 neurons (53% mask divergence,
      z=7260)。这些 "KL-important but magnitude-unimportant" neurons 的 mean gate prob=0.614
      (teal_kl_overlap_analysis)，说明它们有 moderate activation 但对 output distribution
      贡献不成比例地大。
      PPL=11.24 > best tier threshold 10.5 ✓，gap vs KL30 = 2.42 > 1.5 ✓。
      BCE@30% (11.24) ≈ KL@50% (11.80) 意味着 BCE 的 inferior masks 浪费 ~20pp sparsity budget。
    tables:
      - "Table 2 新行: 30% operating point 三方对比 (KL uniform / TEAL vanilla / BCE forced)"
    figures_description:
      - "Figure 3 Pareto frontier 新增 BCE@30% 点, 与 KL@30% 的水平距离 = mask quality gap"
    analysis: >
      2.42 PPL gap 在推荐操作点直接支撑 Claim 1 headline。BCE@30% (11.24) ≈ KL@50% (11.80)
      是最直观的 "mask matters" evidence: 使用 BCE magnitude masks，需要额外保留 20% neurons
      才能达到 KL 50% 的质量。BCE@30% 甚至不如 vanilla TEAL@30% (10.97)，说明 BCE predictor
      学到的 mask pattern 比 activation magnitude heuristic 更差——因为 BCE 在 Lagrangian 约束
      下可能过度 prune 某些 layers (BCE Lagrangian failure: loss scale ~0.6 vs KL ~0.0001,
      bce_gumbel_lagrangian_isolation best PPL=38.02 at 50%)。
      MMLU gap -6.8pp vs KL30 进一步说明 BCE mask 在 knowledge-intensive tasks 上的劣势。

  - name: LongBench Long-Context Evaluation
    plan_id: plan_010
    description: >
      LongBench English subset (4K-32K tokens), 评估条件: KL 30% uniform, TEAL 30%,
      KL 50% global, TEAL 50%, dense baseline。Per-task-type: single-doc QA (NarrativeQA),
      multi-doc QA (Qasper, HotpotQA), summarization (GovReport, MultiNews)。
      之前 6 次尝试中 5 次 failed (pipeline stability 是主要风险), v6 成功但 multi_news dense=2.5
      疑似 eval bug。best 档假设 pipeline 问题彻底修复。
    expected_results:
      # Dense baseline (fixed pipeline)
      dense_narrativeqa: 17.8
      dense_qasper: 24.6
      dense_govreport: 30.2
      dense_multinews: 25.8
      dense_avg: 24.6
      # KL 30% uniform
      kl30_narrativeqa: 13.5
      kl30_qasper: 18.9
      kl30_govreport: 25.8
      kl30_multinews: 21.2
      kl30_avg: 19.9
      kl30_retention_pct: 80.9
      # TEAL 30%
      teal30_narrativeqa: 10.2
      teal30_qasper: 14.8
      teal30_govreport: 23.1
      teal30_multinews: 17.5
      teal30_avg: 16.4
      teal30_retention_pct: 66.7
      # KL 50% global
      kl50_narrativeqa: 7.8
      kl50_qasper: 11.2
      kl50_govreport: 18.4
      kl50_multinews: 13.5
      kl50_avg: 12.7
      # TEAL 50%
      teal50_narrativeqa: 4.5
      teal50_qasper: 6.8
      teal50_govreport: 14.2
      teal50_multinews: 9.8
      teal50_avg: 8.8
      # KL 30% advantage over TEAL 30%
      kl30_vs_teal30_avg_delta: 3.5
    result_rationale: >
      LongBench 评估 predictor 从 2048-token 训练序列到 4K-32K 测试序列的 generalization。
      best 档下 KL30 retention ~81% 的逻辑:
      (1) KL predictor 学到的 neuron importance 主要反映 SwiGLU 的 structural property
      (哪些 neurons 对 output distribution 贡献最大)，这个 pattern 在不同 sequence length
      下基本稳定——因为 importance 由 FFN weight structure 决定，不由 sequence position 决定。
      (2) 30% sparsity 处于 budget-surplus regime，natural sparsity floor (~5%) 的 neurons
      在长序列下同样 inactive (sparsity_floor_extended: floor_30pct=0.0499)。
      (3) Summarization (GovReport) retention 最高 (85%) 因为 summarization 主要依赖
      dominant activation mode，对 minor neuron pruning 最 robust。QA tasks (NarrativeQA)
      retention 较低 (76%) 因为需要精确 retrieval + reasoning 链。
      (4) TEAL 30% retention 更低 (67%) 因为 magnitude-based mask 在长上下文下的
      layer allocation error 累积更严重——长序列的 attention pattern 变化导致不同 layer
      的 importance re-ranking，static magnitude 无法 adapt。
      注意: pipeline 之前连续 5 次 failed，best 档假设评估脚本 debug 完成 (修复 tokenization
      truncation、generation config、metric computation 等问题)。这是 best 档的一个强假设。
    tables:
      - "Table 6 (LongBench): 5 conditions × 4+ tasks, per-task F1/ROUGE-L"
    figures_description:
      - "Figure 7: LongBench task-type grouped bar chart, Dense/KL30/TEAL30 三组"
    analysis: >
      KL30 avg retention ~81% vs TEAL30 ~67% 在长上下文维度进一步验证 mask quality advantage。
      KL predictor 2K→32K generalization 支持 "structural neuron importance" 假设。
      50% 条件下两者均大幅退化 (KL50 retention ~52%, TEAL50 ~36%)，与 short-context regime
      analysis 一致——50% 已进入 capacity-cliff regime，allocation 无关。
      作为 P1 evidence，strengthen EMNLP venue fit (NLP-specific long-context evaluation)，
      但非 core claim 支撑。pipeline 稳定性是主要 execution risk。

  - name: MT-Bench Multi-Turn Evaluation
    plan_id: plan_011
    description: >
      MT-Bench 80 multi-turn questions, 8 categories, GPT-4o judge。
      条件: Dense, KL 30% uniform, TEAL 30%。P2 priority, 仅在 GPU budget 和时间允许时执行。
      注意: 使用 Llama 3.1 8B base model (非 instruct)，base model 在 instruction-following
      任务上表现有限，绝对分数会较低。主要价值在 relative comparison。
    expected_results:
      # Base model scores (lower than instruct model benchmarks)
      dense_avg_score: 4.15
      kl30_avg_score: 3.82
      teal30_avg_score: 3.28
      # Relative metrics
      kl30_retention_pct: 92.0
      teal30_retention_pct: 79.0
      # Category breakdown (KL 30%)
      kl30_writing: 4.25
      kl30_roleplay: 4.10
      kl30_reasoning: 3.45
      kl30_math: 2.85
      kl30_coding: 3.50
      kl30_extraction: 4.35
      kl30_stem: 3.80
      kl30_humanities: 4.25
      # Worst category delta
      kl30_math_delta_vs_dense: -0.55
      kl30_avg_delta_vs_dense: -0.33
    result_rationale: >
      base model (非 instruct-tuned) 在 MT-Bench 上绝对分数有限 (~4/10)，因为 base model
      缺乏 instruction-following alignment。但 relative ordering 仍有诊断价值:
      (1) KL30 retention ~92% (3.82/4.15) 高于短序列 downstream 的 retention (~85-90% on
      most tasks)，因为 MT-Bench 的 multi-turn format 更依赖 language modeling fluency
      (KL 直接优化的 objective) 而非 precise factual recall。
      (2) Math/reasoning categories 退化最大 (~0.5 points) 因为这些 task 需要 precise
      step-by-step computation，每步的 sparse mask error 会 compound。
      (3) Writing/humanities 几乎不受影响因为这些 task 依赖 dominant language patterns
      (high-activation neurons, natural sparsity floor 内保留的 neurons)。
      (4) TEAL30 在 math/reasoning 上更差因为 magnitude mask 无法 preserve output
      distribution 的 tail (长尾 token predictions)，而 math 答案通常在 vocabulary
      distribution 的 tail 中。
      base model 限制使 MT-Bench 的绝对值意义有限，但 "KL 在 multi-turn generation 下
      near-dense quality" 的 relative finding 仍有叙事价值。
    tables:
      - "Table 7 (MT-Bench): 3 conditions × 8 categories + average, 注明 base model"
    figures_description:
      - "Figure 8: MT-Bench radar chart, 8 categories, Dense/KL30/TEAL30"
    analysis: >
      MT-Bench relative ordering confirms KL advantage extends to generative quality,
      not just discriminative benchmarks。但 base model 绝对分数低 (~4/10) 限制了
      这个 evidence 的说服力。审稿人可能 discount base model MT-Bench。
      如果 GPU budget 不足应优先 drop 此实验。核心 claims 不依赖此结果。

  - name: RULER Synthetic Long-Context Diagnostics
    plan_id: plan_012
    description: >
      RULER synthetic evaluation at 4K and 16K context, 3 task types:
      NIAH (needle-in-a-haystack), multi-key retrieval, variable tracking。
      Fine-grained diagnostic complementing LongBench。P2 priority, deps on plan_010。
    expected_results:
      # 4K context
      dense_4k_niah: 92.5
      dense_4k_multikey: 78.3
      dense_4k_vartrack: 75.8
      dense_4k_avg: 82.2
      kl30_4k_niah: 88.2
      kl30_4k_multikey: 71.5
      kl30_4k_vartrack: 68.4
      kl30_4k_avg: 76.0
      teal30_4k_niah: 80.5
      teal30_4k_multikey: 58.2
      teal30_4k_vartrack: 55.8
      teal30_4k_avg: 64.8
      # 16K context
      dense_16k_niah: 85.1
      dense_16k_multikey: 62.4
      dense_16k_vartrack: 58.2
      dense_16k_avg: 68.6
      kl30_16k_niah: 78.5
      kl30_16k_multikey: 53.8
      kl30_16k_vartrack: 49.2
      kl30_16k_avg: 60.5
      teal30_16k_niah: 68.2
      teal30_16k_multikey: 40.5
      teal30_16k_vartrack: 38.6
      teal30_16k_avg: 49.1
      # Degradation rates
      kl30_4k_to_16k_drop: 15.5
      dense_4k_to_16k_drop: 13.6
      teal30_4k_to_16k_drop: 15.7
    result_rationale: >
      RULER synthetic tasks 不需要 instruction following (与 MT-Bench 不同)，因此
      base model 可以提供有意义的绝对分数。
      (1) NIAH 对 sparsity 最 robust (KL30 retention 95% at 4K) 因为 needle retrieval
      主要依赖 attention 定位 (未被 sparse)，FFN 只需 extract 和 copy 信息。
      (2) Multi-key retrieval 和 variable tracking 对 sparsity 更敏感 (retention ~85-90%)
      因为需要 FFN 同时处理多个 scattered information，neuron interaction quality 直接影响
      cross-position information aggregation。
      (3) 4K→16K degradation pattern: KL30 的 degradation rate (15.5pp) 接近 dense (13.6pp)，
      而 TEAL30 (15.7pp) 与 KL30 相近。这说明 degradation 主要来自 Llama 3.1 8B 的
      intrinsic long-context 能力限制，而非 sparsity 引入的额外退化。
      (4) KL 在 multi-key task 上的优势最大 (KL 71.5 vs TEAL 58.2 at 4K)，因为 multi-key
      需要 FFN 同时 activate 多个 retrieval patterns，KL 的 joint-interaction-aware masks
      比 magnitude masks 更好地保留了这种 multi-pattern capacity。
    tables:
      - "Table 8 (RULER): 3 conditions × 3 tasks × 2 lengths"
    figures_description:
      - "Figure 9: RULER accuracy vs context length, faceted by task type, per-condition lines"
    analysis: >
      RULER 提供 fine-grained diagnostic: KL 的 advantage 在 multi-key 和 variable tracking
      上最显著 (13-15pp over TEAL at 4K)，在 NIAH 上最小 (~8pp)。这与 "KL captures joint
      neuron interaction" 叙事一致——需要 multi-pattern activation 的 task 受益最大。
      16K 数据表明 sparsity-induced degradation 不随 context length 加速，
      strengthening generalization claim。作为 P2，non-essential for core claims。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0de677ed-30fd-4a8f-8ff6-b5b2aa77d52a",
  "isSidechain": false,
  "requestId": "req_011CbASsdAwrCagY7RX6iZhQ",
  "type": "assistant",
  "uuid": "1a4f836a-23a4-4852-a5d9-3d3939094aa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgKh6JBSk1DNbuC2hMqubQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24897,
      "cache_read_input_tokens": 64952,
      "output_tokens": 12872,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24897,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12872,
          "cache_read_input_tokens": 64952,
          "cache_creation_input_tokens": 24897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24897
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1 causal ablation 跨 seed 完美复现，mask pattern discovery 叙事被审稿人接受为genuine empirical finding 核心假设：['C1 s123 复现 exact match: BCE+KL-targets PPL 与 KL PPL delta <…",
  "leafUuid": "1a4f836a-23a4-4852-a5d9-3d3939094aa2",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation mask discovery causal validation",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1 causal ablation 跨 seed 完美复现，mask pattern discovery 叙事被审稿人接受为genuine empirical finding 核心假设：['C1 s123 复现 exact match: BCE+KL-targets PPL 与 KL PPL delta <…",
  "leafUuid": "1a4f836a-23a4-4852-a5d9-3d3939094aa2",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "KL distillation mask discovery causal validation",
  "sessionId": "1c9ff59b-1d42-455e-a00d-3eea90aa1013"
}
```

---
