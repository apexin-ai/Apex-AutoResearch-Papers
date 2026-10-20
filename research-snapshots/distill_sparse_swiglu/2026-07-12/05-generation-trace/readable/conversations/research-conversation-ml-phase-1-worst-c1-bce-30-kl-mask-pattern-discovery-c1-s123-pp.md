# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：C1 不复现或 BCE 30% 基本追平 KL，mask pattern discovery 叙事的核心优势被削弱 核心假设：['C1 s123 PP

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/7cc89e23-684b-40f2-9f96-30cddc153fe3.jsonl`
- **Structured JSON:** [`26fe941d7cc1a5d99ec9.json`](../../sessions/26/26fe941d7cc1a5d99ec9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T17:59:08.189Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T17:59:08.189Z",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：C1 不复现或 BCE 30% 基本追平 KL，mask pattern discovery 叙事的核心优势被削弱\n核心假设：['C1 s123 PPL delta > 0.5，或 downstream 出现 >3pp delta（gradient coupling 贡献 >15%）', 'BCE 30% forced top-k PPL < 9.5，接近 KL 30% uniform (8.82)，gap < 0.7', '6-point regime curve 有 ≥2 个 monotonicity violation，三 regime 边界模糊', \"审稿人多数认为 novelty insufficient：'just KL loss with Gumbel, C1 doesn't cleanly decompose'\", '14B MMLU gap + 无 wall-clock speedup 被视为 practical relevance 不足']\n关键指标范围：{'c1_ppl_delta_s123': [0.5, 1.5], 'c1_downstream_max_delta_pp': [3.0, 8.0], 'kl30_uniform_ppl_3seed_mean': [8.75, 8.9], 'kl30_uniform_mmlu_3seed_mean': [0.35, 0.41], 'kl30_uniform_mmlu_3seed_std': [0.02, 0.045], 'bce_30pct_forced_topk_ppl': [8.8, 9.5], 'regime_curve_monotonicity_violations': [2, 3], 'reviewer_avg_score': [3.0, 3.5]}\n叙事方向：需要 reframe，但不降级目标。新 angle: 从 \"mask pattern discovery\" 转向 \"loss-aware sparsity prediction as output-distribution alignment\"——核心贡献变成 完整的 loss function taxonomy + 系统性 empirical characterization，而非单一 causal ablation finding。C1 结果仍有价值但降为 \"ablation reveals gradient coupling and target quality are entangled contributors\"，不再做 clean decomposition claim。 如果 BCE 30% 追平 KL，reframe 为 \"KL training as automatic oracle discovery\"—— KL 的价值是 zero-shot 发现好 mask（无需手动设计 oracle），即使事后 BCE 能学到 相同 mask，KL 仍是唯一 automated discovery pathway。强化 14B scale analysis 和 Mistral cross-architecture 作为 systematic study 贡献。Regime analysis 如果 noisy，改为 continuous degradation curve 而非 discrete phase transition。 补充 gradient SNR analysis (已有 103x ratio 数据) 作为 why KL works 的 mechanistic evidence。仍冲 EMNLP Main (Findings 作为 fallback)。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: distill_sparse_swiglu\nfocus: 测试 'mask pattern discovery' 叙事的审稿接收度。核心 reframe: C1 causal ablation 证明 target quality（不是 gradient coupling）是 KL 优势的唯一驱动力。BCE+KL-targets PPL = 11.9638 = KL PPL 11.9638（exact match at 50% sparsity, TEAL uniform）。53% mask divergence 作为新发现。包含 6-point sparsity regime analysis。目标 4.0 Main Conference。\n\n## paper_framing.md\n\n# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 across **both PPL and all downstream tasks**. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). **Downstream confirmation (full-spectrum)**: All 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) also match within <1pp delta, confirming gradient coupling = 0 across PPL + reasoning + knowledge + math dimensions. Standard BCE (magnitude masks) PPL ≈ 22.51. Target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from \"engineering a better loss\" to \"discovering that output-distribution distillation reveals hidden neuron importance structure.\" **Supporting evidence**: (a) Iso-compute ablation: BCE with 2.71× more FLOPs still PPL=27.97 vs KL=12.00, confirming the gap is structural; (b) BCE at recommended 30% operating point (D062): forced TEAL top-k PPL=11.24 vs KL=8.82, Δ=2.42 — BCE 30% is nearly as bad as KL 50% (11.80), meaning BCE's inferior masks waste ~20pp of sparsity budget; (c) BCE Lagrangian failure at 30%: BCE loss scale (~0.6) vs KL (~0.0001) causes same Lagrangian to fail; (d) No compensation needed: KL eliminates 67.2M compensation parameters (~256MB). **Anticipated attack**: \"Two-stage training (KL→oracle→BCE) avoids needing KL predictor at inference?\" Defense: KL predictor is contextual (per-input adaptive); oracle masks are fixed. Deployment requires per-input sparsity adaptation. **Remaining caveat**: Single seed (s42); C1 s123 in progress for statistical robustness. (Headline claim, resolves persistent R3-R8 confound)\n\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \"subsuming\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)\n\n3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports \"PPL is a poor proxy for downstream quality\" narrative. **6-point PPL regime curve (D063)**: 30%=8.82, 35%=9.31, 40%=10.12, 45%=10.80, 50%=11.80 (TEAL global). Smooth monotonic increase from 30-50%, providing dense sampling for regime boundary identification. 25% eval pending. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.\n\n- **Our framing / headline question**: \"What does KL distillation actually learn for SwiGLU sparsity prediction, and why do its masks differ fundamentally from magnitude-based oracles?\" The theoretical grounding (§3.6, suggestive): BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm. This provides intuition for how KL *can* discover joint interaction patterns. The C1 causal ablation (§4.4) then empirically confirms: the masks KL discovers, not the gradient pathway itself, are what matter.\n\n- **Headline result template**: \"KL-trained sparsity predictors discover neuron importance patterns that diverge 53% from magnitude-based masks. A causal ablation confirms that these mask patterns, not gradient coupling, drive KL's quality advantage: BCE trained on KL-derived masks matches KL performance exactly across PPL (11.96 = 11.96) and all downstream tasks (delta <1pp on ARC-c, WinoGrande, MMLU, GSM8K). This finding eliminates the need for 67.2M compensation parameters and reveals three sparsity operating regimes (now with 6 data points) with qualitatively different allocation requirements.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: **Substantially mitigated by C1 finding**. The 53% mask divergence and causal ablation are genuine empirical discoveries, not engineering contributions. No prior work has shown that KL-derived masks encode fundamentally different neuron importance from magnitude-based approaches. The paper now contributes a finding (mask pattern discovery) rather than just a method (combining known techniques). Additional support: formal decomposition framework, quantitative s^2 prediction, three-regime analysis.\n\n2. **\"KL wins only because more compute\"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 (plan_009, GQA + sliding window) and Qwen-2.5-14B cross-scale validation (D048/D054). **14B mixed result**: KL PPL advantage preserved (7.62 vs TEAL 8.73, 1.47× dense ratio identical to 8B), but KL MMLU=63.72% (global) / 64.49% (uniform) significantly trails TEAL 71.83% (global). Uniform allocation does not fix this gap (D054). PPL-downstream disconnect at 14B scale is an honest limitation, not hidden. Framing: KL's coupled gradient captures output-distribution fidelity (PPL) across scales, but 14B knowledge-intensive tasks (MMLU) show scale-dependent sensitivity that warrants further investigation.\n\n5. **\"Effect size may not hold on downstream tasks\"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.\n\n6. **\"Unfair comparison: BCE+comp close to KL but at higher inference cost\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- **Novelty upgraded from R8**: C1 causal ablation + 53% mask divergence finding elevates paper from \"systematic composition\" to \"empirical discovery about what KL learns for sparsity prediction.\" This addresses the persistent R3-R8 novelty concern and moves the paper toward Main Conference territory (target 4.0).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:\n    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline\n    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds\n    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and\n    BCE-only 3 seeds (mvp_bce_s42/s123/s456).\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_ids:\n  - mvp_kl_norm_v2_s42\n  - mvp_kl_norm_v2_s123\n  - mvp_kl_norm_v2_s456\n  - mvp_bce_s42\n  - mvp_bce_s123\n  - mvp_bce_s456\n  remaining_runs:\n  - KL-only 2 additional seeds (s0, s1) for 5-seed headline\n  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)\n  - KL+comp 3 seeds (s42, s123, s456)\n  registry_id: kl_only_s1\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- id: plan_002\n  claim: 1\n  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).\n    Isolates whether KL advantage comes from loss function or relaxation method. 3\n    seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: ste_baseline_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- id: plan_003\n  claim: 1\n  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs\n    (KL requires full forward pass for output logits, BCE can use cached targets).\n    Report per-step FLOPs and total training time for both. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: bce_isocompute_v2_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- id: plan_004\n  claim: 2\n  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL\n    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,\n    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: spon_2048_s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- id: plan_005\n  claim: 2\n  description: 'SPON subsumption verification: output-space linearity test showing\n    KL predictor already captures SPON correction signal. ||Delta_logits(s+c) - Delta_logits(s)\n    - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality analysis.\n    Proves SPON+KL ≈ KL (no additive gain). 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  - plan_004\n  registry_id: plan_005_subsumption_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- id: plan_006\n  claim: 1\n  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:\n    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),\n    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free\n    < static-learned < contextual-learned.\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_ids:\n  - training_free_baselines\n  - training_free_wina_greedy\n  registry_id: training_free_baselines\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2\n    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor\n    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto\n    frontier plot.\n\n    '\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  - plan_004\n  - plan_005\n  - plan_006\n  registry_id: bench_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- id: plan_008\n  claim: 3\n  description: '3-level sparsity sweep (30%/50%/70%): KL-only vs BCE-only. Test scaling\n    trend and KL-BCE delta growth. 1 seed per level (sweep analysis, not headline).\n    50% data point reused from plan_001. If 3 levels show non-linear inflection, add\n    intermediate points.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  registry_id: d030_kl50_uniform\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- id: plan_009\n  claim: 1\n  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%\n    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds\n    each condition.\n\n    '\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: lm_eval_mistral_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions\n    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:\n    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization\n    beyond short training sequences.\n\n    '\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 2\n  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8\n    categories. All conditions. Tests instruction-following quality under sparsity.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative\n    task types. Fine-grained capability diagnostics complementing LongBench.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_total_loss: 3.3438\n    final_kl_loss: 3.2969\n    final_reg_loss: 0.05\n    final_sparsity: 0\n    steps: 1000\n    tau_final: 0.1\n    wikitext2_ppl_dense: 6.12\n    wikitext2_ppl_sparse: 455.93\n    wikitext2_ppl_increase_pct: 7349\n    model_level_sparsity: 0.372\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\n- exp_id: mvp_kl_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_kl_s456\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_bce_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 27.9603\n    teal_sparse_ppl: 44.537\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 628\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.3817\n    teal_sparse_ppl: 44.5864\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 629\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.1437\n    teal_sparse_ppl: 43.033\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 603.3\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_lagrangian_quicktest\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_kl_loss: 418\n    final_constraint_loss: 1.211\n    final_sparsity: 0.141\n    final_lambda: 5.06\n    steps: 200\n    sparsity_trajectory:\n    - 0.406\n    - 0.387\n    - 0.289\n    - 0.168\n    - 0.141\n- exp_id: kl_lagrangian_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_normalized_quicktest\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step1_kl: 1.18\n    step200_kl: 0.641\n    step200_sparsity: 0.504\n    final_lambda: 8\n    sparsity_converged_step: 80\n    sparsity_trajectory:\n    - 0.406\n    - 0.398\n    - 0.398\n    - 0.457\n    - 0.52\n    - 0.506\n    - 0.504\n    - 0.504\n    lambda_trajectory:\n    - 1\n    - 2\n    - 4\n    - 8\n    - 8\n    - 8\n    - 8\n    - 8\n- exp_id: mvp_kl_norm_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_norm_v3_quicktest\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics:\n    step1_kl_raw: 1.1797\n    step1_kl_norm: 1.1797\n    step1_sparsity: 0.406\n    step1_lambda: 2\n    step50_kl_raw: 0.7344\n    step50_kl_norm: 0.7344\n    step50_sparsity: 0.514\n    step50_lambda: 1.95\n    step100_kl_raw: 0.625\n    step100_kl_norm: 0.625\n    step100_sparsity: 0.496\n    step100_lambda: 1000\n    step150_kl_raw: 0.5703\n    step150_kl_norm: 0.5703\n    step150_sparsity: 0.48\n    step150_lambda: 1000\n    step200_kl_raw: 0.6836\n    step200_kl_norm: 0.6836\n    step200_sparsity: 0.477\n    step200_lambda: 1000\n    step200_constraint: 0.01178\n    kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)\n    sparsity_range: 0.477-0.514 after step 50\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\n- exp_id: mvp_kl_norm_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2142\n    teal_sparse_ppl: 12.0776\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 97.4\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2474\n    teal_sparse_ppl: 11.9128\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 94.7\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.14\n    teal_sparse_ppl: 13.58\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 121.9\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_only_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.19\n    teal_sparse_ppl: 12.03\n    model_level_sparsity: 0.499\n    ppl_increase_vs_true_dense_pct: 96.57\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: kl_only_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- exp_id: spon_training\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1193\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 9.0977\n    spon_recovery_pct: 3.8\n    ppl_improvement_from_spon: 0.1188\n    ppl_increase_vs_true_dense_pct: 48.7\n    ppl_increase_no_spon_vs_true_dense_pct: 50.6\n    mean_bias_norm: 0.040596\n    max_bias_norm: 0.054199\n    teal_sparse_ppl: 12.08\n    teal_with_spon_ppl: 11.93\n    spon_dense_ppl_degradation: 6.19\n    model_level_sparsity: 0.5\n    eval_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n- exp_id: spon_kl_s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: bce_comp_staged_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 25.44\n    predictor_hard_mask_ppl_no_comp: 27.96\n    teal_sparse_ppl: 44.54\n    model_level_sparsity: 0.558\n    ppl_increase_vs_true_dense_pct: 315.7\n    comp_loss_final: 0.0033\n    bce_loss_final: 0.6379\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: training_free_baselines\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- exp_id: spon_training_seq2048\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: ste_baseline_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- exp_id: spon_2048_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- exp_id: ste_kl_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: training_free_wina_greedy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wina_greedy_ppl: 2126.03\n    dense_ppl: 6.12\n    model_level_sparsity: 0.5\n    eval_dataset: WikiText-2\n    eval_seq_len: 2048\n    greedy_allocation_summary: 'layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80,\n      layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24:\n      0.05-0.15, layers 25-31: 0.00'\n- exp_id: bce_isocompute_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_spon_supp_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: spon_supp_eval_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- exp_id: plan_005_subsumption_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- exp_id: kl_sparsity30_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity70_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_loss: 0.1465\n    kl_normalized: 0.1465\n    kl_raw: 0.1465\n    model_level_sparsity: 0.281\n    sparsity_target: 0.3\n    lambda_sparse_final: 1000\n    lambda_max_cap: 1000\n    tau_final: 0.1\n    constraint_loss_final: 0\n    training_steps: 1000\n    wall_clock_seconds: 2662.6\n    gpu_hours: 0.74\n    note: No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1).\n      Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run\n      was offline (not synced).\n- exp_id: kl_sparsity70_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 13.84\n    predictor_teal_sparse_ppl: 17.91\n    vanilla_teal_sparse_ppl: 100.11\n    teal_sparse_ppl: 17.91\n    teal_sparse_ppl_static_baseline: 17.91\n    model_level_sparsity: 0.7\n    teal_sparse_note: '17.91 = predictor-based TEAL (teal_global_masks: predictor-gated\n      magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py\n      L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct\n      metadata 有误导性.'\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    per_layer_sparsity_range:\n    - 0.508\n    - 0.876\n- exp_id: kl_sparsity30_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    loss: 0.165\n    kl_normalized: 0.165\n    kl_raw: 0.165\n    sparsity: 0.285\n    lambda_sparse: 5000\n    tau: 0.1\n    constraint_loss: 0\n    steps: 1000\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    teal_sparse_ppl_note: 已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\n    model_level_sparsity: 0.3\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n- exp_id: mistral_kl_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_final_loss: 0.2188\n    train_final_kl_raw: 0.2188\n    train_final_kl_norm: 0.2188\n    train_final_constraint: 0\n    train_final_sparsity: 0.48\n    train_final_lambda: 1000\n    train_final_tau: 0.1\n    train_steps_completed: 1000\n    true_dense_ppl: 5.52\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    model_level_sparsity: 0.5\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_samples: 159\n- exp_id: lm_eval_dense_test\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc_norm: 0.3771\n    winogrande_acc: 0.6156\n    mmlu_acc: 0.2591\n    gsm8k_exact_match: 0.0121\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: kl_sparse_50pct\n    server: westd-34887\n    exit_code: 129\n    wall_time_sec: 3010\n    flag: SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\n- exp_id: lm_eval_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.5819\n    winogrande_acc: 0.7814\n    mmlu_acc: 0.6532\n    gsm8k_exact_match: 0.5004\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: dense\n    server: westd-34887\n- exp_id: lm_eval_mistral_downstream\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_mistral_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- exp_id: diag_30pct_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_gsm8k_gencomp\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_teal_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: lm_eval_kl_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.3575\n    arc_challenge_acc_norm: 0.3737\n    winogrande_acc: 0.6756\n    mmlu_acc: 0.2874\n    gsm8k_exact_match_strict: 0.0743\n    gsm8k_exact_match_flexible: 0.0781\n    actual_sparsity: 0.3\n    model: llama-3.1-8b\n    condition: kl_distill_30pct_sparsity_s42\n    mmlu_stem_acc: 0.2499\n    mmlu_social_sciences_acc: 0.2896\n    mmlu_humanities_acc: 0.2786\n    mmlu_other_acc: 0.3363\n- exp_id: gsm8k_gen_compare\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: lm_eval_teal_50pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: vanilla_teal\n    sparsity: 0.5\n    actual_sparsity: 0.5\n    arc_challenge_acc_norm: 0.291\n    winogrande_acc: 0.5556\n    mmlu_acc: 0.2856\n    gsm8k_exact_match_flexible: 0.019\n    gsm8k_exact_match_strict: 0.0114\n    arc_challenge_drop_vs_dense: -0.5\n    winogrande_drop_vs_dense: -0.289\n    mmlu_drop_vs_dense: -0.563\n    gsm8k_drop_vs_dense: -0.962\n    model: Llama-3.1-8B\n    condition: TEAL 50% training-free sparsity\n- exp_id: lm_eval_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge:\n      acc: 0.3933\n      acc_norm: 0.4155\n      acc_stderr: 0.0143\n      acc_norm_stderr: 0.0144\n    winogrande:\n      acc: 0.6559\n      acc_stderr: 0.0134\n    mmlu:\n      acc: 0.3598\n      acc_stderr: 0.004\n    mmlu_stem:\n      acc: 0.313\n    mmlu_humanities:\n      acc: 0.3305\n    mmlu_social_sciences:\n      acc: 0.4108\n    mmlu_other:\n      acc: 0.401\n    gsm8k:\n      exact_match_strict: 0.0849\n      exact_match_flexible: 0.0925\n      strict_stderr: 0.0077\n      flexible_stderr: 0.008\n    actual_sparsity: 0.3\n- exp_id: lm_eval_mistral_kl_50pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.2927\n    arc_challenge_acc_norm: 0.3183\n    arc_challenge_acc_norm_stderr: 0.0136\n    winogrande_acc: 0.629\n    winogrande_acc_stderr: 0.0136\n    mmlu_acc: 0.2295\n    mmlu_acc_stderr: 0.0035\n    mmlu_stem_acc: 0.2125\n    mmlu_humanities_acc: 0.2421\n    mmlu_social_sciences_acc: 0.2171\n    mmlu_other_acc: 0.2398\n    gsm8k_exact_match_strict: 0.0045\n    gsm8k_exact_match_flexible: 0.0212\n    model: Mistral-7B-v0.3\n    condition: kl_distill_50pct_sparsity_s42\n    arc_challenge_retention_vs_dense: 0.528\n    winogrande_retention_vs_dense: 0.799\n    mmlu_retention_vs_dense: 0.368\n    gsm8k_retention_vs_dense: 0.012\n- exp_id: d030_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n    allocation: uniform\n    per_layer_sparsity: uniform 0.301 across all 32 layers\n    mmlu_improvement_vs_global: +11.87pp (0.2874 → 0.4061)\n    gsm8k_change_vs_global: no change (0.0743 → 0.0735, within noise)\n- exp_id: bce_isocompute_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 2700\n    loss: 0.6382\n    bce_loss: 0.6371\n    reg_loss: 0.001\n    sparsity: 0.51\n    training_time_seconds: 2828\n    note: 'BCE saturation confirmed: step 500→2700 only 0.006 improvement'\n- exp_id: bench_mistral_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: d030_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- exp_id: bench_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- exp_id: eval_kl30_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    sparsity_target: 0.3\n    actual_sparsity: 0.3\n- exp_id: d030_kl40_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3627\n    arc_challenge_acc_norm: 0.4181\n    winogrande_acc: 0.6717\n    mmlu_acc: 0.3068\n    gsm8k_exact_match: 0.0394\n    actual_sparsity: 0.398\n- exp_id: eval_bce_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 22.51\n    teal_sparse_ppl: 27.97\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2048\n    arc_challenge_acc_norm: 0.2398\n    arc_challenge_acc_norm_stderr: 0.0125\n    winogrande_acc: 0.5059\n    winogrande_acc_stderr: 0.0141\n    mmlu_acc: 0.3002\n    mmlu_acc_stderr: 0.0038\n    gsm8k_exact_match: 0.0485\n    gsm8k_exact_match_strict: 0.0425\n    gsm8k_exact_match_stderr: 0.0059\n- exp_id: bench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n- exp_id: bench_kl50_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n    actual_sparsity: 0.5\n- exp_id: bench_kl30_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    arc_challenge_acc_norm: 0.3968\n    winogrande_acc: 0.7017\n    mmlu_acc: 0.2527\n    gsm8k_exact_match: 0.0879\n    actual_sparsity: 0.3\n- exp_id: bench_teal30\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.97\n    arc_challenge_acc_norm: 0.4232\n    winogrande_acc: 0.6606\n    mmlu_acc: 0.3861\n    gsm8k_exact_match: 0.0788\n    actual_sparsity: 0.3\n- exp_id: bench_teal50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 23.31\n    arc_challenge_acc_norm: 0.2841\n    winogrande_acc: 0.5304\n    mmlu_acc: 0.2832\n    gsm8k_exact_match: 0.0197\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.963\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: bench_kl40_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.117\n    arc_challenge_acc_norm: 0.4096\n    winogrande_acc: 0.6535\n    mmlu_acc: 0.3806\n    gsm8k_exact_match: 0.05\n    actual_sparsity: 0.4\n- exp_id: longbench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v5\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: latency_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpu_model: NVIDIA RTX PRO 6000 Blackwell Server Edition\n    dtype: float16\n    attn: flash_attention_2\n    batch: 1\n    seq_len: 2048\n    warmup: 10\n    iters: 100\n    dense_ms: 119.11\n    dense_std: 0.57\n    dense_tokens_per_s: 17194.5\n    kl_30pct_ms: 126.64\n    kl_30pct_std: 0.7\n    kl_30pct_tokens_per_s: 16171.8\n    kl_30pct_speedup: 0.941\n    kl_50pct_ms: 126.78\n    kl_50pct_std: 0.31\n    kl_50pct_tokens_per_s: 16154.2\n    kl_50pct_speedup: 0.939\n    comp_30pct_ms: 129.94\n    comp_30pct_std: 0.75\n    comp_30pct_tokens_per_s: 15761.4\n    comp_30pct_speedup: 0.917\n    comp_50pct_ms: 129.71\n    comp_50pct_std: 0.53\n    comp_50pct_tokens_per_s: 15788.8\n    comp_50pct_speedup: 0.918\n    predictor_overhead_ms: 3.17\n    predictor_overhead_pct: 2.7\n    per_layer_predictor_ms: 0.099\n    dense_ffn_per_layer_ms: 2.427\n    sparse_ffn_pred_per_layer_ms: 2.686\n    compensation_overhead_ms: 3.3\n- exp_id: bench_kl50_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.83\n    arc_challenge_acc_norm: 0.3515\n    winogrande_acc: 0.6298\n    mmlu_acc: 0.2751\n    gsm8k_exact_match: 0.0235\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9604\n    arc_challenge_acc_norm: 0.3345\n    winogrande_acc: 0.6275\n    mmlu_acc: 0.2874\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: longbench_dense_v6\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    longbench_narrativeqa: 7.3\n    longbench_qasper: 13.4\n    longbench_gov_report: 30.5\n    longbench_multi_news: 2.5\n- exp_id: longbench_kl30_uniform_v6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    longbench_narrativeqa: 4.12\n    longbench_qasper: 6.23\n    longbench_gov_report: 16.97\n    longbench_multi_news: 18.01\n    runtime_seconds: 6156.6\n- exp_id: eval_c4_ood_kl50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 9.2075\n    kl_50_global_ppl: 18.401\n    teal_50_ppl: 38.7503\n    kl_vs_dense_ratio: 2\n    teal_vs_dense_ratio: 4.21\n- exp_id: db_sensitivity_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    db64_per_token_ppl: 10.158\n    db64_teal_global_ppl: 12.076\n    db64_sparsity: 0.5\n    db64_loss: 0.361\n    db128_teal_global_ppl: 11.963\n    db128_per_token_ppl: 9.218\n    db256_per_token_ppl: 8.586\n    db256_teal_global_ppl: 12.105\n    db256_sparsity: 0.5\n    db256_loss: 0.27\n    db512_per_token_ppl: 7.933\n    db512_teal_global_ppl: 12.315\n    db512_sparsity: 0.5\n    db512_loss: 0.224\n    best_teal_global_db: 128\n    best_teal_global_ppl: 11.963\n- exp_id: bce_gumbel_lagrangian_isolation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lr_1e4_ppl: 42.99\n    lr_1e3_ppl: 48.4\n    lr_3e3_ppl: 38.02\n    lr_1e4_bce_loss: 0.7158\n    lr_1e3_bce_loss: 0.6781\n    lr_3e3_bce_loss: 0.6632\n    lr_1e4_sparsity: 0.514\n    lr_1e3_sparsity: 0.506\n    lr_3e3_sparsity: 0.504\n    best_ppl: 38.02\n    best_lr: 3e-3\n    kl_baseline_ppl: 11.79\n    gap_vs_kl: 26.23\n- exp_id: steps_curve_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: tau_schedule_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tau_linear_baseline_ppl: 11.963\n    tau_fixed05_ppl: 11.861\n    tau_fixed01_ppl: 12.072\n    tau_fixed05_loss: 0.248\n    tau_fixed01_loss: 0.43\n    best_tau: fixed_0.5\n    ppl_range: 0.211\n- exp_id: steps_curve_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    step200_ppl: 15.158\n    step400_ppl: 12.538\n    step600_ppl: 12.046\n    step800_ppl: 11.907\n    step1000_ppl: 11.906\n    convergence_step: 800\n    ppl_800_vs_1000_delta: 0.001\n- exp_id: mistral_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 6.048\n    kl_teal_global_ppl: 6.7733\n    teal_baseline_ppl: 8.3807\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 1.386\n    ppl_vs_dense_pct: 9.5\n- exp_id: mistral_kl70_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 9.1086\n    kl_teal_global_ppl: 13.3254\n    teal_baseline_ppl: 61.716\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 6.77\n    final_loss: 0.3945\n    actual_sparsity: 0.682\n- exp_id: mistral_teal50_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_baseline_ppl: 18.3061\n    dense_ppl: 5.5238\n    teal_vs_dense_ratio: 3.31\n- exp_id: bench_kl70_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 17.91\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: kl_sparsity70_s42_v2 (teal_global_masks protocol)\n    vanilla_teal_ppl: 100.11\n- exp_id: bench_teal70\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 100.11\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: training_free_baselines experiment (vanilla teal global)\n- exp_id: gradient_snr_kl_vs_bce\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 5.77e-05\n    bce_avg_snr: 1.0e-05\n    snr_ratio: 5.76\n    early_layer_ratio_range: 34-156x\n    late_layer_ratio_range: 2-4x\n- exp_id: natural_sparsity_floor_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    always_pruned_ratio: 0.0006\n    always_pruned_count: 278\n    total_neurons: 458752\n    late_layer_max_ratio: 0.0051\n    threshold: 0.1\n- exp_id: teal_kl_overlap_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_jaccard: 0.396\n    divergence_ratio: 0.433\n    kl_only_pruned_magnitude_ratio: 1.48\n    teal_only_pruned_mean_gate_prob: 0.614\n    min_jaccard_layer: L17-L18 (0.19)\n    max_jaccard_layer: L26-L28 (0.55)\n- exp_id: gradient_snr_constrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 0.000545\n    bce_avg_snr: 5.28e-06\n    snr_ratio: 103.2\n    kl_final_sparsity: 0.508\n    bce_final_sparsity: 0.591\n    steps: 200\n- exp_id: sparsity_floor_extended\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    floor_30pct: 0.0499\n    floor_50pct: 0.0726\n    floor_70pct: 0.1936\n    late_layer_max_30: 0.4604\n    late_layer_max_50: 1.2347\n    late_layer_max_70: 4.3666\n    threshold: 0.1\n    seq_len: 2048\n    num_samples: 50\n- exp_id: teal_kl_overlap_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_score: 7260.3\n    p_value: 0\n    median_percentile_rank: 78.6\n    iqr_q1: 64.4\n    iqr_q3: 89.1\n    layers_significant: 31/32\n    exception_layer: 31\n- exp_id: mag_preservation_reg\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: reverse_kl_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.8\n    vs_forward_kl: +1.01 (+8.6%)\n    sparsity: 0.5\n- exp_id: jsd_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.54\n    vs_forward_kl: +0.75 (+6.4%)\n    sparsity: 0.5\n- exp_id: global_30pct_retention\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    early_retention: 0.771\n    middle_retention: 0.764\n    knowledge_L12_20_retention: 0.797\n    late_L24_31_retention: 0.501\n    L31_retention: 0.284\n    L30_retention: 0.366\n    starved_layers: L27-L31\n- exp_id: kl_bce_f1_oracle\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bce_f1: 0.6128\n    bce_precision: 0.6132\n    bce_recall: 0.6124\n    kl_f1: 0.5397\n    kl_precision: 0.5112\n    kl_recall: 0.5715\n    random_f1: 0.5\n    kl_ppl: 11.79\n    bce_ppl: 22.51\n- exp_id: kl50_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.745\n    arc_challenge: 0.3814\n    winogrande: 0.6125\n    mmlu: 0.2752\n    gsm8k: 0.0281\n- exp_id: kl30_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8308\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.6938\n    mmlu_acc: 0.3944\n    gsm8k_exact_match: 0.0751\n    actual_sparsity: 0.3\n    allocation: uniform\n- exp_id: kl50_s456_train_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl50_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.397\n    final_kl_normalized: 0.397\n    final_sparsity: 0.492\n    final_lambda: 5000\n    final_tau: 0.1\n    steps_completed: 1000\n- exp_id: kl_50pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.745\n    arc_challenge_acc_norm: 0.3814\n    winogrande_acc: 0.6125\n    mmlu_acc: 0.2752\n    gsm8k_exact_match: 0.0281\n    sparsity: 0.5\n    allocation: global\n- exp_id: mistral_dense_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 5.5238\n    model: Mistral-7B-v0.3\n    condition: dense\n    sparsity: 0\n- exp_id: mistral_kl30_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.048\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 0.5242\n- exp_id: mistral_kl50_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.2931\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 1.7693\n- exp_id: mistral_kl70_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 9.1086\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 3.5848\n- exp_id: mistral_kl30_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.7733\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 1.2495\n- exp_id: mistral_kl50_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.6489\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 3.1251\n- exp_id: mistral_kl70_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 13.3254\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 7.8016\n- exp_id: mistral_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3807\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 2.8569\n- exp_id: mistral_teal70_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 61.716\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 56.1922\n- exp_id: kl30_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.2021\n    actual_sparsity: 0.289\n    constraint_satisfied: true\n    training_steps: 1000\n- exp_id: kl_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9748\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.693\n    mmlu_acc: 0.3807\n    gsm8k_exact_match: 0.0758\n    sparsity: 0.3\n    allocation: global\n- exp_id: kl50_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.8057\n    arc_challenge: 0.3319\n    winogrande: 0.6488\n    mmlu: 0.2794\n    gsm8k: 0.0212\n- exp_id: kl30_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9332\n    arc_challenge: 0.4633\n    winogrande: 0.7111\n    mmlu: 0.4382\n    gsm8k: 0.0758\n- exp_id: kl30_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4198\n    ppl_uniform: 8.7947\n    arc_challenge: 0.4505\n    winogrande: 0.6875\n    gsm8k: 0.0758\n- exp_id: qwen14b_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 6.8\n    teal_global_ppl: 7.62\n    ppl_ratio_hard_mask: 1.31\n    ppl_ratio_teal: 1.47\n    final_loss: 0.3398\n    training_sparsity: 0.281\n    teal_sparsity: 0.3\n    lambda: 5000\n    steps: 1000\n- exp_id: qwen14b_kl30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.6232\n    arc_challenge_acc_norm: 0.5717\n    winogrande_acc: 0.7206\n    mmlu_acc: 0.6372\n    gsm8k_exact_match: 0.4882\n- exp_id: downstream_extended_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.727\n    hellaswag_acc: 0.527\n    piqa_acc_norm: 0.7595\n    piqa_acc: 0.747\n    boolq_acc: 0.7685\n- exp_id: wallclock_speedup_30_50\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    theoretical_flops_speedup_30pct: 1.36\n    theoretical_flops_speedup_50pct: 2.45\n    actual_wallclock_speedup_30pct: 0.91\n    actual_wallclock_speedup_50pct: 0.6\n    predictor_overhead_decode_ms: 1\n    predictor_overhead_prefill_ms: 2\n    actual_mean_sparsity_30pct: 0.28\n    actual_mean_sparsity_50pct: 0.605\n    note: No wall-clock speedup without sparse kernels. Mask-based=0.87-0.94x (predictor\n      overhead), structured-skip=0.45-0.74x (gather overhead). Report theoretical\n      FLOPs in paper.\n- exp_id: qwen14b_bce30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 5.57\n    teal_global_ppl: 8.76\n    ppl_ratio_hard_mask: 1.075\n    ppl_ratio_hard_mask_note: at predictor native 6.4% sparsity, not comparable to\n      KL's 28.1%\n    ppl_ratio_teal: 1.69\n    actual_sparsity_teal: 0.3\n    predictor_native_sparsity: 0.064\n    training_log_sparsity_note: Training Lagrangian failed (predictor sparsity=6.4%).\n      Inference via TEAL forces 30% externally. TEAL PPL 8.76 is valid for method\n      comparison.\n    final_loss: 0.5561\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n- exp_id: qwen14b_teal30_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.7332\n    arc_challenge_acc_norm: 0.5683\n    winogrande_acc: 0.7269\n    mmlu_acc: 0.7183\n    gsm8k_exact_match: 0.4951\n- exp_id: qwen14b_bce30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    predictor_native_sparsity: 0.064\n    lambda_max: 50000\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n    sparsity_trajectory: 49%→5% collapse in 50 steps, no recovery over 950 steps\n    note: 10x stronger Lagrangian produces identical sparsity as v1 (lambda=5000).\n      Confirms BCE gradient insufficiency is fundamental, not constraint strength.\n- exp_id: downstream_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.8233\n    hellaswag_acc_norm_stderr: 0.0038\n    piqa_acc_norm: 0.8074\n    piqa_acc_norm_stderr: 0.0092\n    boolq_acc: 0.8294\n    boolq_acc_stderr: 0.0066\n- exp_id: qwen14b_bce30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 8.7634\n    arc_challenge_acc_norm: 0.5759\n    winogrande_acc: 0.7261\n    mmlu_acc: 0.7167\n    gsm8k_exact_match: 0.5307\n- exp_id: downstream_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc: 0.4878\n    hellaswag_acc_norm: 0.667\n    piqa_acc: 0.7258\n    piqa_acc_norm: 0.7361\n    boolq_acc: 0.685\n- exp_id: kl50_global_s123_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7184\n    arc_challenge_acc_norm: 0.3635\n    winogrande_acc: 0.6109\n    mmlu_acc: 0.2834\n    gsm8k_exact_match: 0.0258\n- exp_id: bce_isocompute_v3_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: bce_isocompute_v3_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6368\n    final_sparsity: 0.51\n    training_steps: 2700\n- exp_id: c4_ood_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0458\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_download\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen14b_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl: 5.1854\n    arc_challenge: 0.6758\n    winogrande: 0.8106\n    mmlu: 0.7977\n    gsm8k: 0.8757\n- exp_id: bce_isocompute_v3_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_sparse_ppl: 28.3503\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2312\n    arc_challenge_acc_stderr: 0.01232\n    arc_challenge_acc_norm: 0.2807\n    arc_challenge_acc_norm_stderr: 0.01313\n    winogrande_acc: 0.5241\n    winogrande_acc_stderr: 0.01404\n    mmlu_acc: 0.2567\n    mmlu_acc_stderr: 0.00367\n    gsm8k_exact_match: 0.022\n    gsm8k_exact_match_stderr: 0.00404\n    gsm8k_exact_match_strict: 0.00834\n    gsm8k_exact_match_strict_stderr: 0.0025\n- exp_id: bce_isocompute_v3_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 28.0627\n    arc_challenge_acc_norm: 0.2696\n    winogrande_acc: 0.513\n    mmlu_acc: 0.2655\n    gsm8k_exact_match: 0.022\n- exp_id: qwen14b_kl30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: qwen14b_teal30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl30_8b_s123_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    sparsity: 0.3\n    training_loss: 0.147\n- exp_id: kl30_8b_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    sparsity: 0.3\n    training_loss: 0.148\n- exp_id: qwen14b_kl30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 7.63\n    mmlu_acc: 0.6449\n    arc_challenge_acc_norm: 0.5444\n    winogrande_acc: 0.7245\n- exp_id: qwen14b_teal30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.01\n    mmlu_acc: 0.6634\n    arc_challenge_acc_norm: 0.5529\n    winogrande_acc: 0.6985\n- exp_id: bce_isocompute_v3_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 27.9696\n    arc_challenge_acc: 0.2346\n    arc_challenge_acc_norm: 0.2765\n    winogrande_acc: 0.5162\n    mmlu_acc: 0.2614\n    gsm8k_exact_match: 0.019\n- exp_id: kl30_8b_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    arc_challenge_acc: 0.4462\n    arc_challenge_acc_norm: 0.4744\n    winogrande_acc: 0.7024\n    mmlu_acc: 0.3836\n    gsm8k_exact_match: 0.0917\n- exp_id: kl30_8b_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc: 0.436\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: snr_extended_r6w3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_snr_step300: 0.0058773\n    bce_snr_step300: 0.00114449\n    snr_ratio_step300: 5.14\n    kl_train_time_s: 641\n    bce_train_time_s: 320\n    num_checkpoints: 7\n    steps_range: 0-300\n- exp_id: c4_ood_kl30_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl50_s123_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.89\n    arc_challenge_acc_norm: 37.88\n    winogrande_acc: 62.19\n    mmlu_acc: 27.75\n    gsm8k_exact_match: 2.35\n    comparison_vs_global_topk:\n      ppl_delta: -0.94\n      arc_c_delta: -5.55\n      wg_delta: -6.71\n      mmlu_delta: -8.2\n      gsm8k_delta: -5\n    note: 'Uniform allocation: better PPL but catastrophic downstream degradation\n      vs global_topk. Confirms global_topk allocation is critical for downstream quality.'\n- exp_id: c4_ood_kl30_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0259\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_ood_dense_baseline_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 9.2075\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: kl50_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8614\n    arc_challenge_acc_norm: 0.3754\n    winogrande_acc: 0.6417\n    mmlu_acc: 0.2784\n    gsm8k_exact_match: 0.0212\n- exp_id: c4_ood_kl50_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.6064\n    allocation: global_topk\n    sparsity: 0.5\n    model: llama-3.1-8b\n- exp_id: downstream_ext_kl50_uniform_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: downstream_ext_kl30_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_kl50_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.9867\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 456\n- exp_id: c4_ood_kl30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0401\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl50_s42_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9638\n    arc_challenge_acc_norm: 0.3259\n    winogrande_acc: 0.6235\n    mmlu_acc: 0.2792\n    gsm8k_exact_match: 0.0197\n- exp_id: c4_ood_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.5297\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 42\n- exp_id: kl_comp_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6992\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.3594\n    - 1.3516\n    - 1.0859\n    - 0.9219\n    - 0.8789\n    - 0.8281\n    - 0.7461\n    - 0.7344\n    - 0.6953\n    - 0.6992\n- exp_id: c4_ood_kl30_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.7617\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.0469\n    - 1.3828\n    - 1.0703\n    - 0.9609\n    - 0.8711\n    - 0.7305\n    - 0.6875\n    - 0.7773\n    - 0.7969\n    - 0.7617\n- exp_id: kl_comp_30pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl_comp_30pct_s42_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl_comp_30pct_s123_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 123\n- exp_id: kl_comp_30pct_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl50_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9538\n    arc_challenge_acc_norm: 0.3831\n    winogrande_acc: 0.6196\n    mmlu_acc: 0.275\n    gsm8k_exact_match: 0.0288\n- exp_id: kl_comp_30pct_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: kl_comp_50pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n- exp_id: kl50_s42_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8038\n    arc_challenge_acc_norm: 0.3336\n    winogrande_acc: 0.6338\n    mmlu_acc: 0.2819\n    gsm8k_exact_match: 0.0167\n- exp_id: kl30_s123_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8186\n    arc_challenge_acc_norm: 0.471\n    winogrande_acc: 0.6961\n    mmlu_acc: 0.3763\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s456_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8284\n    arc_challenge_acc_norm: 0.4505\n    winogrande_acc: 0.6953\n    mmlu_acc: 0.3727\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s123_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl30_s456_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: c1_ablation_bce_kl_targets_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wt2_ppl: 9.29\n    eval_sparsity: 0.609\n    oracle_agreement: 0.978\n    final_bce_loss: 0.0545\n    train_steps: 1000\n    train_time_sec: 877.1\n    reference_kl_ppl: 11.79\n    reference_bce_ppl: 22.51\n- exp_id: bce_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_sparsity25_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_final: 0.1582\n    kl_normalized_final: 0.1582\n    sparsity_actual: 0.23\n    sparsity_target: 0.25\n    lambda_final: 5000\n    tau_final: 0.1\n    steps: 1000\n- exp_id: kl_sparsity35_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.203\n    final_sparsity: 0.336\n    steps: 1000\n- exp_id: c1_ablation_eval_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9638\n    arc_challenge_acc_norm: 0.3217\n    winogrande_acc: 0.6314\n    mmlu_acc: 0.2779\n    gsm8k_exact_match: 0.0205\n    sparsity_target: 0.5\n    allocation: uniform\n- exp_id: kl_sparsity45_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.33\n    final_sparsity: 0.449\n    steps: 1000\n- exp_id: bce_30pct_s42_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity25_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.153\n    final_sparsity: 0.23\n    steps: 1000\n- exp_id: kl_sparsity25_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity35_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity45_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: c1_ablation_bce_kl_targets_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl_sparsity40_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity25_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity35_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity45_s42_eval_teal_uniform\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: c1_ablation_bce_kl_targets\n  claim: 'Claim 1: mask pattern discovery'\n  description: BCE trained on KL-derived oracle masks achieves PPL 11.9638 = KL PPL\n    11.9638 at 50% sparsity under identical TEAL protocol. 53% mask divergence from\n    magnitude oracles. Target quality is sole driver of KL advantage.\n  estimated_gpu_hours: 0.0\n- name: dense_sparsity_sweep_6pt\n  claim: 'Claim 3: regime analysis with 6 data points'\n  description: KL predictors at 25%/30%/35%/40%/45%/50% with regime boundaries precisely\n    mapped.\n  estimated_gpu_hours: 0.0\n- name: bce_30pct_forced_topk\n  claim: 'Claim 1: BCE baseline at recommended operating point'\n  description: BCE predictor evaluated at 30% via forced TEAL top-k. Fills Table 2\n    gap.\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T17:59:08.192Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T17:59:08.192Z",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-18T17:59:08.228Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：C1 不复现或 BCE 30% 基本追平 KL，mask pattern discovery 叙事的核心优势被削弱
核心假设：['C1 s123 PPL delta > 0.5，或 downstream 出现 >3pp delta（gradient coupling 贡献 >15%）', 'BCE 30% forced top-k PPL < 9.5，接近 KL 30% uniform (8.82)，gap < 0.7', '6-point regime curve 有 ≥2 个 monotonicity violation，三 regime 边界模糊', "审稿人多数认为 novelty insufficient：'just KL loss with Gumbel, C1 doesn't cleanly decompose'", '14B MMLU gap + 无 wall-clock speedup 被视为 practical relevance 不足']
关键指标范围：{'c1_ppl_delta_s123': [0.5, 1.5], 'c1_downstream_max_delta_pp': [3.0, 8.0], 'kl30_uniform_ppl_3seed_mean': [8.75, 8.9], 'kl30_uniform_mmlu_3seed_mean': [0.35, 0.41], 'kl30_uniform_mmlu_3seed_std': [0.02, 0.045], 'bce_30pct_forced_topk_ppl': [8.8, 9.5], 'regime_curve_monotonicity_violations': [2, 3], 'reviewer_avg_score': [3.0, 3.5]}
叙事方向：需要 reframe，但不降级目标。新 angle: 从 "mask pattern discovery" 转向 "loss-aware sparsity prediction as output-distribution alignment"——核心贡献变成 完整的 loss function taxonomy + 系统性 empirical characterization，而非单一 causal ablation finding。C1 结果仍有价值但降为 "ablation reveals gradient coupling and target quality are entangled contributors"，不再做 clean decomposition claim。 如果 BCE 30% 追平 KL，reframe 为 "KL training as automatic oracle discovery"—— KL 的价值是 zero-shot 发现好 mask（无需手动设计 oracle），即使事后 BCE 能学到 相同 mask，KL 仍是唯一 automated discovery pathway。强化 14B scale analysis 和 Mistral cross-architecture 作为 systematic study 贡献。Regime analysis 如果 noisy，改为 continuous degradation curve 而非 discrete phase transition。 补充 gradient SNR analysis (已有 103x ratio 数据) 作为 why KL works 的 mechanistic evidence。仍冲 EMNLP Main (Findings 作为 fallback)。

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
  "promptId": "445cfaec-a561-4593-ac5d-7f8ffe767e21",
  "type": "user",
  "uuid": "b2b871db-b588-492c-8b8d-8f55909e2231",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T17:59:08.225Z_

```json
{
  "parentUuid": "b2b871db-b588-492c-8b8d-8f55909e2231",
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
  "uuid": "acaba153-51cb-408b-82be-42d716b1ba4d",
  "timestamp": "2026-05-18T17:59:08.225Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T17:59:08.225Z_

```json
{
  "parentUuid": "acaba153-51cb-408b-82be-42d716b1ba4d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f7da46ed-5cf5-4f4f-8552-cbda0c2d6fc4",
  "timestamp": "2026-05-18T17:59:08.225Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1 不复现或 BCE 30% 基本追平 KL，mask pattern discovery 叙事的核心优势被削弱 核心假设：['C1 s123 PPL delta > 0.5，或 downstream 出现 >3pp delta（gradient coupling 贡献 >15%）', 'BCE 30%…",
  "leafUuid": "f7da46ed-5cf5-4f4f-8552-cbda0c2d6fc4",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe KL sparsity discovery as loss-aware alignment with systematic regime analysis",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3"
}
```

---

### Assistant

_source line 8 · 2026-05-18T17:59:12.224Z_

I'll read the existing experiment plan and what_if definitions to ensure my predictions are fully grounded.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7da46ed-5cf5-4f4f-8552-cbda0c2d6fc4",
  "isSidechain": false,
  "requestId": "req_011CbAUAUSRbmsdxoEfwjUzX",
  "type": "assistant",
  "uuid": "94390a67-977c-4dea-9f9a-961bf558acc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NExAfNzVznmBmabLreng7c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35790,
      "cache_read_input_tokens": 11841,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 112,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35790
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

_source line 9 · 2026-05-18T17:59:13.362Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014kQVBRmsdVp3QjvtcfuHBP`</summary>

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
  "parentUuid": "94390a67-977c-4dea-9f9a-961bf558acc6",
  "isSidechain": false,
  "requestId": "req_011CbAUAUSRbmsdxoEfwjUzX",
  "type": "assistant",
  "uuid": "b7a1d51c-1f27-40c4-acd6-de14a631e3d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NExAfNzVznmBmabLreng7c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35790,
      "cache_read_input_tokens": 11841,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 112,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35790
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

_source line 10 · 2026-05-18T17:59:13.441Z_

<details><summary>↩ Tool result · `toolu_014kQVBRmsdVp3QjvtcfuHBP`</summary>

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
projects/distill_sparse_swiglu/task_context/history/reviewer/loop_1.md
projects/distill_sparse_swiglu/task_context/history/director/loop_1.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_1.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778861972.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778864854.md
projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md
projects/distill_sparse_swiglu/task_context/history/director/loop_2.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778865194.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778871099.md
projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md
projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md
projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md
projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_report.md
projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/review_report.md
projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/review_report.md
projects/distill_sparse_swiglu/task_context/history/reviewer/loop_2.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778873177.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778873913.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778874382.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778876214.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778876347.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778878864.md
projects/distill_sparse_swiglu/artifacts/plan_007/report/plan_007_wikitext2_ppl_results.md
projects/distill_sparse_swiglu/artifacts/plan_006/report/diagnostic_report.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778882860.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778882930.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778883107.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3.md
projects/distill_sparse_swiglu/artifacts/plan_009_readiness_report.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778884170.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778884213.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778884273.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778885311.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778885581.md
projects/distill_sparse_swiglu/task_context/history/reviewer/loop_3.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778885890.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778887468.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778888363.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/LICENSE.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/philox/LICENSE.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778888545.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778890852.md
projects/distill_sparse_swiglu/artifacts/training_free_baselines/data/teal_baseline_sweep_p0_rerun.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778891037.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778891456.md
projects/distill_sparse_swiglu/artifacts/lm_eval_status_check.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778896565.md
projects/distill_sparse_swiglu/artifacts/gsm8k_gen_compare/report/gsm8k_gen_compare_report.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_4.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778896576.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778896580.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778896594.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778896626.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778896630.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778896709.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778898052.md
projects/distill_sparse_swiglu/artifacts/process_check_loop5.md
projects/distill_sparse_swiglu/artifacts/literature_ppl_downstream_disconnect.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778898562.md
projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778899923.md
projects/distill_sparse_swiglu/.claude/sessions/agent_42dd644f/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_42dd644f/AGENTS.md
projects/distill_sparse_swiglu/.claude/sessions/agent_f8235f3f/CLAUDE.md
projects/distill_sparse_swiglu/.claude/sessions/agent_f8235f3f/AGENTS.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7a1d51c-1f27-40c4-acd6-de14a631e3d8",
  "isSidechain": false,
  "promptId": "445cfaec-a561-4593-ac5d-7f8ffe767e21",
  "type": "user",
  "uuid": "fabd4cc0-3b48-499f-ab47-28692fc37eff",
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
      "projects/distill_sparse_swiglu/task_context/history/reviewer/loop_1.md",
      "projects/distill_sparse_swiglu/task_context/history/director/loop_1.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_1.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778861972.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778864854.md",
      "projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md",
      "projects/distill_sparse_swiglu/task_context/history/director/loop_2.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778865194.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_1_1778871099.md",
      "projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md",
      "projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md",
      "projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md",
      "projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_report.md",
      "projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/review_report.md",
      "projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/review_report.md",
      "projects/distill_sparse_swiglu/task_context/history/reviewer/loop_2.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778873177.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778873913.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778874382.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778876214.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778876347.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778878864.md",
      "projects/distill_sparse_swiglu/artifacts/plan_007/report/plan_007_wikitext2_ppl_results.md",
      "projects/distill_sparse_swiglu/artifacts/plan_006/report/diagnostic_report.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778882860.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778882930.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778883107.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3.md",
      "projects/distill_sparse_swiglu/artifacts/plan_009_readiness_report.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778884170.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778884213.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778884273.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_2_1778885311.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778885581.md",
      "projects/distill_sparse_swiglu/task_context/history/reviewer/loop_3.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778885890.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778887468.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778888363.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/LICENSE.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/distributions/LICENSE.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/philox/LICENSE.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md",
      "projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778888545.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778890852.md",
      "projects/distill_sparse_swiglu/artifacts/training_free_baselines/data/teal_baseline_sweep_p0_rerun.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778891037.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778891456.md",
      "projects/distill_sparse_swiglu/artifacts/lm_eval_status_check.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778896565.md",
      "projects/distill_sparse_swiglu/artifacts/gsm8k_gen_compare/report/gsm8k_gen_compare_report.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_4.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778896576.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778896580.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778896594.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778896626.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778896630.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_3_1778896709.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778898052.md",
      "projects/distill_sparse_swiglu/artifacts/process_check_loop5.md",
      "projects/distill_sparse_swiglu/artifacts/literature_ppl_downstream_disconnect.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778898562.md",
      "projects/distill_sparse_swiglu/task_context/history/agent/loop_4_1778899923.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_42dd644f/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_42dd644f/AGENTS.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_f8235f3f/CLAUDE.md",
      "projects/distill_sparse_swiglu/.claude/sessions/agent_f8235f3f/AGENTS.md"
    ],
    "durationMs": 56,
    "numFiles": 100,
    "truncated": true
  },
  "sourceToolAssistantUUID": "b7a1d51c-1f27-40c4-acd6-de14a631e3d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T17:59:16.848Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RrkDSpbdtivCqzHp8ea7Dy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fabd4cc0-3b48-499f-ab47-28692fc37eff",
  "isSidechain": false,
  "requestId": "req_011CbAUArhdNZtFaMgmNhqBR",
  "type": "assistant",
  "uuid": "f7bab3b1-c521-45c6-8709-ba16b731294a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DVH5BVpsSiUrid97ZrW9W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3130,
      "cache_read_input_tokens": 47631,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 47631,
          "cache_creation_input_tokens": 3130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3130
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

_source line 12 · 2026-05-18T17:59:16.855Z_

<details><summary>↩ Tool result · `toolu_01RrkDSpbdtivCqzHp8ea7Dy`</summary>

```text
1	# Paper Framing — distill_sparse_swiglu
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 2026 cycle)
5	- Deadline: 2026-05-25 (ARR submission)
6	- Track: Efficient Methods for NLP
7	
8	## Core Claims
9	
10	1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)
11	
12	2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.
13	
14	3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.
15	
16	## Story Spine
17	
18	- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).
19	
20	- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.
21	
22	- **Our framing / headline question**: "Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.
23	
24	- **Headline result template**: "On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline."
25	
26	## Two-Dimensional Taxonomy (Conceptual Contribution)
27	
28	|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
29	|--------------------------|:-----------------:|:-------------------:|:-------------:|
30	| Static                   | —                 | —                   | SPON          |
31	| Per-layer                | —                 | ShadowLLM           | —             |
32	| Per-token contextual     | FastForward       | —                   | **Ours**      |
33	
34	Positions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.
35	
36	## Anticipated Reviewer Concerns
37	
38	1. **"Incremental / no new algorithm"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.
39	
40	2. **"KL wins only because more compute"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.
41	
42	3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.
43	
44	4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).
45	
46	5. **"Effect size may not hold on downstream tasks"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.
47	
48	## Venue Fit
49	- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation
50	- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue
51	- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7bab3b1-c521-45c6-8709-ba16b731294a",
  "isSidechain": false,
  "promptId": "445cfaec-a561-4593-ac5d-7f8ffe767e21",
  "type": "user",
  "uuid": "c9ca0d7f-5d7a-4432-a53c-70a9fedca180",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md",
      "content": "# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)\n\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\n\n3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\n\n- **Our framing / headline question**: \"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\n\n- **Headline result template**: \"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\n\n2. **\"KL wins only because more compute\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\n\n5. **\"Effect size may not hold on downstream tasks\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "f7bab3b1-c521-45c6-8709-ba16b731294a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-18T17:59:16.927Z_

````json
{
  "parentUuid": "c9ca0d7f-5d7a-4432-a53c-70a9fedca180",
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
  "uuid": "e6de7e3a-e6ce-455f-aa19-39052e19c051",
  "timestamp": "2026-05-18T17:59:16.927Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1 不复现或 BCE 30% 基本追平 KL，mask pattern discovery 叙事的核心优势被削弱 核心假设：['C1 s123 PPL delta > 0.5，或 downstream 出现 >3pp delta（gradient coupling 贡献 >15%）', 'BCE 30%…",
  "leafUuid": "e6de7e3a-e6ce-455f-aa19-39052e19c051",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe KL sparsity discovery as loss-aware alignment with systematic regime analysis",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3"
}
```

---

### Assistant

_source line 16 · 2026-05-18T18:07:41.249Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, under the "worst" tier scenario. Let me carefully go through each experiment and generate predictions.

Let me understand the worst tier definition:
- C1 doesn't replicate OR BCE 30% basically matches KL, weakening the "mask pattern discovery" narrative
- Key metric ranges are given
- Narrative needs reframing

Let me identify all planned experiments (status: planned) and also the ones that have PREPARING status (in-progress) that need predictions:

Looking at the experiment plan:


- plan_010 (LongBench), plan_011 (MT-Bench), and plan_012 (RULER) are all marked as planned and need predictions. I also need to handle the what_if experiments like c1_ablation_bce_kl_targets, dense_sparsity_sweep_6pt, and bce_30pct_forced_topk, plus the PREPARING experiments like bce_30pct_s42_eval and kl_sparsity25_s42.

Now I'm looking at the teal evaluation variants across different KL sparsity levels with seed 42, including both standard and uniform configurations. I need to build worst-case predictions for all these experiments, keeping in mind the key constraints: C1 s123 needs to avoid PPL deltas above 0.5, BCE 30% forced top-k should stay close to the KL 30% uniform baseline around 8.82 with less than 0.7 gap, and I'm working through the remaining constraint criteria.

Looking at what's actually planned versus what's still in preparation, I need to focus on the experiments with "planned" status like LongBench, MT-Bench, and RULER, plus the what-if scenarios around BCE-KL target ablations, the 6-point sparsity sweep, and the BCE 30% forced top-k variant. The core issue is that reviewers are likely to push back on novelty, and the 14B MMLU gap combined with no wall-clock speedup makes the practical relevance harder to defend, so I need to be strategic about which experiments actually strengthen the narrative.

For the worst-case scenarios across the registry experiments, the C1 ablation with seed 123 is particularly risky—the seed 42 result showed perfect replication at 11.9638 PPL, but if seed 123 diverges by more than 0.5 PPL, that suggests the KL-derived oracle masks from seed 42 were overfitted to that particular random initialization, which would undermine the generalizability claim.

The BCE 30% forced top-k scenario is also concerning: if it lands below 9.5 PPL, it closes the gap with KL 30% to less than 0.7 PPL, which would weaken the argument that KL discovers fundamentally better mask patterns rather than just converging to a similar solution through a different path.

With the 6-point regime curve, I'm worried about monotonicity violations—if PPL increases between 35% and 40%, or if MMLU drops between 25% and 30%, the curve becomes noisy and harder to interpret as a clean trade-off frontier.

Now I need to carefully construct the YAML output. Let me re-read what the user is actually asking for—they want detailed data for each planned experiment in the experiment_plan. So I should enumerate the three planned experiments: LongBench, MT-Bench, and RULER, plus the what-if ablations and the remaining PREPARING experiments from the sparsity sweep that haven't been run yet. I'm seeing a list of additional PREPARING experiments from the registry that are part of the sparsity sweep evaluations. Now I need to reconsider the scope—the user specifically asked for experiments marked as "planned" in the experiment_plan, which would be plan_010, plan_011, plan_012, and the what_if experiments, rather than all the registry entries that are currently executing.

Let me think through the worst-case scenario for the C1 ablation across different seeds. With s42 showing an exact match PPL of 11.9638, the concern is that s123 might diverge significantly—BCE+KL-targets on s123 reaches around 12.6 PPL compared to KL-only at 11.745, a delta of 0.855. This compounds downstream where MMLU performance drops by roughly 4 percentage points with some tasks showing even larger gaps, likely because s42's exact match performance was a fortunate seed alignment while s123's KL-derived masks have a different structure that the BCE predictor struggles to handle.

Now looking at the 30% forced top-k regime, the worst case would be PPL below 9.5, nearly matching KL's 8.82. BCE at 30% forced top-k achieves around 9.15 PPL with only a 0.33 gap to KL, suggesting that at lower sparsity levels the magnitude-based masks become nearly as effective as KL-derived ones—the mask pattern discovery advantage really only emerges at higher sparsity points, so BCE is actually quite competitive at the recommended operating point.

I'm also examining the 6-point regime curve where there's an anomaly: the 25% point shows PPL around 8.35, which violates the expected monotonic trend since it's lower than the 30% point at 8.82.

Let me clarify what I'm looking at here. The existing TEAL global data shows a clear progression at 30%, 35%, 40%, 45%, and 50% sparsity levels, but I need to distinguish between those established numbers and what the KL uniform allocation regime actually predicts across the full 6-point sweep.

Looking at the three KL uniform data points I have: 30% gives 8.82, 40% drops to 8.36, and 50% jumps to 11.96. That non-monotonicity between 30% and 40% is already one violation of the expected trend. To establish a worst-case scenario with at least two violations, I need to fill in the gaps at 25%, 35%, and 45% through the PREPARING experiments, starting with the 25% sparsity run. I see the issue now—there's already a violation at 40% being lower than 30%, so I need to find a configuration with at least two violations. If 35% drops to 8.45, that creates a second violation since it should be higher than 30%'s 8.82 under monotonic increase.

The second pattern makes more sense: 25% at 8.90 violates the expected trend, and then 40% at 8.36 violates again by being lower than both 35% and 30%. This could happen if the Lagrangian constraint at 25% undershoots the target sparsity, or if the model trained at that sparsity level achieves a different effective sparsity than intended.

Looking at the actual training data, I see the undershoots and overshoots: 25% target achieved 0.23 actual sparsity, 30% was forced to 0.3 via TEAL, 35% hit 0.336, 40% reached 0.398, and 45% got to 0.449. Since the evals use TEAL to enforce the target sparsity, the actual evaluation sparsity should be uniform across the target levels, which means the regime curve violations I'm seeing might be artifacts of how the models were trained rather than true monotonicity breaks.

Looking at the worst-case scenario for the regime narrative, I'm seeing a non-monotonic pattern: 35% dips below 30%, 40% continues lower, then 45% and 50% spike back up. This creates a messy U-shape with a minimum around 35-40% rather than clean discrete regimes with clear phase transitions. The real problem isn't just the violations themselves—it's that the boundaries between regimes become impossible to identify cleanly, which undermines the whole narrative of distinct operating regimes. Looking at the sparsity levels, I'm tracking where the perplexity actually violates the expected monotonic increase. There are two clear violations: PPL drops from 30% to 35%, then drops again from 35% to 40%, before jumping up at 45%. This messiness makes it hard to identify clean regimes, and I'd expect the downstream metrics to be even noisier, which would only complicate the picture further. Now I'm checking the LongBench results to see if the pattern holds there.

Comparing the dense baseline against KL at 30% sparsity, the multi_news score jumps dramatically from 2.5 to 18.01, which seems counterintuitive given the degradation on other tasks. Regardless, the KL approach shows substantial losses on long-context tasks—30-50% drops on both single and multi-document QA at 30% sparsity, with complete collapse by 50%. BCE with compensation performs similarly, which undermines the claim that KL uniquely avoids compensation effects. I'm also checking MT-Bench and RULER to see if the worst-case patterns hold across these benchmarks.

Now I'm mapping out the full experimental structure: I need to organize the ablation studies comparing BCE and KL targets, the forced top-k variant at the recommended operating point, the sparsity sweep across six regimes, and then the three main evaluation plans on LongBench, MT-Bench, and RULER. There are also several intermediate evaluation runs at different sparsity levels that feed into these final assessments.

I'm thinking through the review scores—realistically this lands somewhere between 3.0 and 3.5, which puts it in the borderline Findings territory. Now I'll draft the complete YAML specification, making sure each experiment has its name, plan ID, description, expected metrics, rationale, and the tables and figures it contributes to. The key tables I need to account for are the main results table showing perplexity and downstream performance across all conditions, plus supporting analysis tables for the sparsity regimes and ablation comparisons. I'm noticing an important distinction here—d030_kl40_uniform was trained at 50% sparsity but evaluated at 40% uniform, whereas the new kl_sparsity40_s42_eval_teal_uniform is a predictor trained directly at 40% target, so these are fundamentally different experiments that can't be directly compared.

Looking at the registry more carefully, I'm realizing the 6-point sweep might use dedicated predictors trained at each sparsity level (25% through 50%) rather than a single predictor trained at 50% and evaluated across different allocations like the paper_framing curve suggests.

The issue is that there's no kl_sparsity40_s42 training experiment in the registry, so I need to figure out which predictor would actually be used for the 40% evaluation—whether it falls back to the 35% or 45% trained model.

Rather than get bogged down in these registry details, I should focus on generating worst-case predictions for the three main experiments the user asked about plus the three what-ifs they mentioned.

For the TEAL global versus uniform distinction, the data is a bit murky—D063's curve shows 30%=8.82 as TEAL global, but that same PPL value appears in the uniform allocation results too, so the protocols might be overlapping or mislabeled. I'll set that aside and just produce the predictions without worrying about those protocol specifics.

My approach will be to structure the YAML output around the six experiments: the three planned ablations plus three alternative scenarios. I'm working through which experiments actually need to be run to get comprehensive results. The planned experiments from the main plan are straightforward—LongBench, MT-Bench, and RULER—but I also need to account for the what_if experiments that are partially complete and the registry experiments still in preparation. I'm consolidating everything that doesn't have final results yet so I can prioritize what predictions and evaluations are actually missing. Looking at the seed replication patterns, s123 shows a larger PPL gap (0.70) than s456 (0.49) because its mask distribution has higher entropy with more borderline neurons, making BCE convergence harder—this suggests gradient coupling accounts for roughly 12-18% of KL's advantage rather than being negligible. Across all three seeds, the mean delta sits around 0.55 PPL with downstream MMLU impacts of 3-4 percentage points. Now examining the forced top-k variant where the BCE predictor was trained with magnitude targets at 50% sparsity, though the Lagrangian approach failed.

At 30% sparsity, the BCE-KL gap narrows significantly to 0.33 PPL (9.15 vs 8.82), which makes sense because magnitude masks become much closer to optimal when fewer neurons are active—the per-neuron independence assumption is less violated when there are fewer joint interactions to miss.

But I'm noticing a contradiction: the existing paper_framing claims D062 shows BCE at 30% = 11.24 PPL with a gap of 2.42, yet the worst-case prediction suggests the gap should be under 0.7, putting BCE around 9.15. These don't align, so I need to clarify what the actual experimental results show versus what the worst-case model predicts.

Looking at the registry more carefully, I think the distinction is that D062 used an older BCE predictor trained at 50% sparsity and forced down to 30%, whereas the new bce_30pct experiments are training a fresh predictor specifically targeting 30% sparsity—which might explain why the numbers differ. 50%
- eval_bce_v3_s42: same predictor, PPL 22.51 (hard mask) / 27.97 (TEAL) at 50%
- The D062 number (BCE 30% = 11.24) is probably from evaluating the 50%-trained BCE at 30% via TEAL

bce_30pct_s42 is a NEW BCE predictor trained specifically at 30% target. This is the what_if experiment. In worst case, this new predictor (with proper 30% Lagrangian target) could be much better than the old 50%-trained predictor evaluated at 30%.

In worst case: BCE predictor trained at 30% target, evaluated at 30% forced TEAL top-k, achieves PPL ≈ 9.15. This is much better than the 50%-trained BCE at 30% (11.24) because the predictor was actually trained for the right sparsity level.

Though I'm concerned about whether BCE Lagrangian training actually works—the Qwen 14B experiment showed sparsity collapse—so I need to check if there are any actual results for BCE at 30% on Llama 8B. The bce_30pct_s42 metrics appear empty, which is suspicious, though the eval is still preparing. Assuming the training succeeded, the gap between BCE 30% forced top-k (9.15) and KL 30% uniform (8.82) would be around 0.33, which seems reasonable since magnitude masks become more informative at lower sparsity levels and the Lagrangian constraint should be easier to satisfy.

Now I'm looking at the 6-point regime curve with uniform allocation across different sparsity levels, checking which predictors were actually trained at each target level versus which ones are being evaluated at mismatched sparsity. Looking at the performance curves for dedicated predictors, the 25% model gives 8.72 which is slightly better than the 30% baseline of 8.82, but the 35% model dips to 8.55—suggesting it might be hitting its optimal range. The 40% dedicated predictor seems to underperform at 8.80, worse than 35% but not quite violating monotonicity. I found one violation so far, but I need at least two. Let me adjust the 25% value to 8.90 to create a second violation where it's higher than the 30% value, which shouldn't happen as sparsity decreases. The 30% to 35% transition also creates a violation since PPL drops instead of rising. So now I have two violations total. For the rationale, the model undertrained at the 25% target because the Lagrangian couldn't push it to the actual sparsity level, and when TEAL forces it to 25%, the predictor's mask quality suffers.

The 35% case hits a sweet spot where the Lagrangian achieved close to target sparsity and the KL loss surface has a favorable minimum, giving the best mask quality per unit of sparsity. Looking at the downstream task performance across these sparsity points, I'm seeing the metrics for ARC-c, WG, MMLU, and GSM8K at 25%, 30%, and 35% to understand how performance degrades at the regime boundaries. Looking at the performance patterns across these benchmarks, I'm seeing non-monotonic behavior that makes it hard to draw clean boundaries between regimes. The KL divergence approach shows consistent degradation—particularly severe on long-context tasks where even 30% KL causes 40-55% performance drops, and 50% KL nearly collapses most benchmarks. BCE with composition shows similar patterns without a clear advantage. The MT-Bench results follow the same trend, with quality dropping from around 7.0 for dense models down to 3.5 at 50% KL, while the predictor struggles to generalize beyond its 2048 token training length. I should just write out the YAML configuration now rather than continue analyzing these detailed metrics. categories hit hardest

For plan_012 (RULER), worst case:
- At 4K (close to training 2048): moderate degradation
- At 16K: significant degradation, predictor doesn't generalize
- NIAH (needle-in-a-haystack): complete failure at 50% (random guessing)

Let me also think about the table/figure mapping.

OK, I'm going to write this now. Let me be careful about metric naming and consistency.

Actually, re-reading the prompt once more: "对 experiment_plan 中每个 planned 实验展开详细数据" — this says "every planned experiment in experiment_plan". The experiment_plan has entries with status: planned which are plan_010, plan_011, plan_012. Plus the what_if experiments.

But there are also DONE experiments with metrics that might need reinterpretation under worst case. However, I think the user only wants predictions for experiments that haven't completed yet. The DONE experiments already have real data, so I should focus on predicting the PLANNED ones under worst case assumptions. The what_if experiments are hypothetical additions to consider as well.

Let me identify which experiments actually need predictions: the what_if ablations that either failed or haven't been attempted yet, plus the components of the dense sparsity sweep that are still pending.

Now I'm ready to compile the final predictions into the YAML structure. Now I'm filling in the specific metric ranges for the YAML prediction—picking C1 PPL delta at 0.85, BCE 30% PPL at 9.15, expecting 2-3 monotonicity violations, and checking the KL 30% uniform PPL values across seeds to set the mean estimate. I'm checking whether these are measured values or predictions—looking at the existing MMLU scores for the KL 30% uniform runs, they're already in the data. Computing the mean and standard deviation from these three seeds to verify they fall within the expected ranges.

The actual standard deviation comes out to 0.015, which is below the worst-case threshold of 0.02-0.045, and the mean of 0.385 sits comfortably within the target range. This suggests the worst-case bounds were probably defined as aspirational targets rather than strict constraints on already-measured data. I should focus on the what-if experiment predictions instead of overthinking whether historical measurements match the worst-case definition.

Now I'll structure the YAML output...

Listing out the imagined experiments across different ablation and evaluation runs...

Actually, I should consolidate these by their underlying plan rather than splitting evaluations into separate entries. So I'd group them as: the BCE-KL ablation covering multiple seeds, the forced top-k variant with its eval, the full sparsity sweep with its three regime points, then the three benchmark evaluations. That gives me six distinct experiments to report on.

Now looking at plan_010 and LongBench more carefully—I have partial results from just four tasks, but the full English subset includes many more categories like multi-document QA, code tasks, and few-shot variants. The existing dense baseline for NarrativeQA is 7.3, but I need to think through what the full evaluation would look like across all these task types.

With KL divergence at 30%, I'm seeing a concerning pattern: QA tasks degrade by 30-50%, summarization holds up better, but few-shot and code tasks take significant hits. The predictor really struggles to generalize to longer contexts.

For plan_011 with MT-Bench, I'm looking at 80 questions across 8 categories scored by GPT-4o, where the dense baseline averages around 7.0 but drops to roughly 5.5 under the same KL 30% constraint.

On plan_012 with RULER, the 4K context shows moderate degradation while 16K contexts are severely impacted—the predictor trained at 2048 tokens just doesn't scale up. Now I'm thinking through how these worst-case scenarios translate into the actual tables and figures I need to present.

Looking at the tables, there are some real issues: Table 1 at the recommended 30% sparsity shows BCE performing too close to KL, which weakens my main argument. Table 2's ablation results are inconsistent across seeds with non-zero gradient coupling. Table 3 across the six-point regime is non-monotonic with fuzzy boundaries. Table 4 already has that 14B MMLU gap to contend with.

The figures have similar problems—the regime curve is noisy and non-monotonic, the Pareto frontier shows KL still winning but BCE creeping uncomfortably close, and the ablation bar chart has overlapping error bars that muddy the conclusions.

Now I'm ready to write out the YAML configuration, keeping it detailed but focused.

I'm noticing something important: the bce_30pct_s42 experiment shows as done but has no metrics recorded. Looking back at the Qwen 14B results, BCE Lagrangian completely failed there—sparsity collapsed to 6.4%. I need to check if the same collapse happens with Llama 8B at 30%. From the existing data, I can see that BCE works fine at 50% sparsity on Llama 8B, achieving around 0.5 sparsity, so the question is whether it breaks specifically at the 30% target.

Now I'm realizing the key distinction: in the forced TEAL top-k setup, the mechanism locks in exactly 30% sparsity regardless of what the BCE predictor outputs. The predictor's job is just to rank which neurons matter most, and TEAL enforces the sparsity level by taking the top-k. So the performance here depends entirely on how well BCE's importance scores identify the right neurons to keep, not on whether it can hit the sparsity target.

Looking at the downstream task results, the gaps between BCE and KL at 30% are pretty narrow—only 1-3 percentage points across MMLU, ARC-c, and WikiGen. At this operating point, those differences are small enough that reviewers might not see a meaningful advantage to the KL approach, which actually strengthens the case for using the simpler BCE method.

Now I'm ready to write out the YAML configuration. I need to be careful about the what_if experiments—they're supposed to leverage already-trained predictors rather than training new ones, so bce_30pct_forced_topk would reuse the bce_30pct_s42 predictor and just run evaluation, and the sparsity sweep would similarly use the existing predictors at each level.

Wait, I should double-check the C1 ablation results for the worst-case scenario before finalizing everything.

Looking at C1 s42: the BCE+KL-targets model achieved 9.29 PPL with Gumbel hard masking at 60.9% sparsity, and 11.9638 PPL under TEAL uniform at 50% sparsity—these match the KL baseline exactly. For s123, the discrepancy likely stems from either lower oracle agreement (the BCE predictor struggles to learn s123's mask patterns as well) or the same masks but with different effective sparsity levels.

Now I'm checking the evaluation metrics for the worst case scenario with delta 0.5-1.5. The BCE+KL-targets s123 model shows 12.45 PPL at TEAL uniform 50%, while the KL s123 baseline sits around 11.745-11.89 depending on which evaluation run I'm looking at. I need to pin down which KL s123 result corresponds to the exact TEAL uniform 50% protocol used in the C1 ablation to properly account for this gap.

Looking at the downstream MMLU results, KL s123 achieves 27.75% while BCE+KL-targets s123 drops to 24.5%, a 3.25 percentage point delta that falls within the expected [3, 8] range. For the s456 seed, the PPL delta between BCE+KL-targets (12.55) and KL baseline (11.95) is 0.60, also within the [0.5, 1.5] bounds. Across the three seeds, the deltas are consistently staying within the expected ranges. The inconsistency across seeds forces me to abandon the clean "gradient coupling = 0" claim—it's actually seed-dependent, ranging from 0% to about 18%. Meanwhile, BCE matching KL at 30% suggests the mask discovery advantage disappears at the recommended operating point, and the non-monotonic regime curve rules out a discrete phase transition narrative. So I need to reframe C1 as showing entangled contributions from gradient coupling and target quality that vary by seed, while reconsidering what KL's value actually represents beyond mask discovery.

Now I'm realizing the distinction between the existing D062 predictor trained at 50% versus the new what-if scenario where the predictor itself was trained at 30%—that changes what the PPL=11.24 baseline actually means for comparison. The PPL range for this what_if experiment falls between 8.8 and 9.5, so my estimate of 9.15 sits right in the middle. For the downstream MMLU metrics, I'm checking whether BCE at 30% can match KL's performance—KL's 3-seed mean is around 0.385, and BCE is hitting 0.38, which is well within the noise margin.

Looking at the other benchmarks, BCE 30% stays competitive across the board: ARC-c shows only a 3 percentage point gap, WG is within 2 points, and GSM8K has a negligible absolute difference. The methods are essentially performing at parity on downstream tasks.

Now I'm examining the C1 ablation results and comparing them against the KL 50% baseline to see how the mask discovery claim holds up at different operating points.

Looking at the downstream metrics for both approaches, the differences are all within less than a percentage point, which suggests the results are consistent. For the s123 worst case scenario, I need to normalize the format since the data's mixing percentages and decimals, then compare the BCE+KL-targets performance against the KL baseline to check if there's a meaningful divergence.

The maximum delta I'm seeing is around 3.4 percentage points on ARC-c, which falls within the expected range and indicates that gradient coupling does have some effect, though it varies across different task types—particularly noticeable in reasoning benchmarks.

Now I'm thinking through the remaining benchmarks. LongBench has some scoring inconsistencies in the existing data that make interpretation difficult, and since the predictor doesn't generalize well beyond 2048 tokens, I should expect degraded performance on longer contexts. For MT-Bench, I'm still working through how to handle that evaluation.

Compiling the YAML output now...

I'm working through the perplexity curve data across the sparsity levels to identify monotonicity violations—where increasing sparsity should degrade performance but doesn't follow that pattern consistently. Let me trace through the numbers carefully: as sparsity increases from 25% to 50%, the perplexity values show some unexpected dips, particularly that jump from 8.80 at 40% back up to 10.20 at 45%, which suggests the predictor's effectiveness breaks down at higher sparsity levels where the importance estimates become less reliable. The non-monotonicity in the budget-surplus regime—that dip around 35%—might just be a training artifact or noise from the dedicated predictor being optimized for that specific sparsity level, which complicates the clean "three regimes" story. Looking at the downstream MMLU scores, I'm seeing a similar pattern where performance drops off as pruning increases, though the single-seed values show some inconsistency that I need to track carefully. Looking at the MMLU scores across sparsity levels, I'm seeing violations at both ends—25% underperforms 30%, and 35% outperforms 30%—which creates a messy non-monotonic pattern. The 25% case likely suffers from the predictor undershooting during training and then being forced to a higher sparsity level via TEAL, degrading mask quality, while the 35% case appears to benefit from better calibration at that target level.

This complexity makes the story harder to present cleanly, but I need to finalize the numbers and generate the YAML output. Let me verify what TEAL uniform actually means in this context—it's using the predictor's per-layer scores but applying a uniform sparsity ratio across all layers rather than layer-specific allocation.

For the 6-point curve, I'll include both global and uniform variants where they exist, though I'll prioritize the uniform allocation approach in the YAML since that's what the paper recommends. Now I'm structuring the final output with experiment names, plan IDs, descriptions, expected metrics, rationales, and analysis covering roughly 10-12 experiments.

I'm mapping out the full experiment suite: three C1 ablation runs with different seeds plus a summary, the recommended 30% BCE baseline, three regime curves at different sparsity levels with a combined analysis, and the full LongBench evaluation across all conditions. I'm checking the C1 ablation setup where the BCE predictor was trained on oracle masks derived from the KL predictor's output, and looking at the s42 results showing strong agreement between the two approaches.

For the worst case with s123, the BCE predictor achieves lower agreement with the KL-derived masks (92% vs 97.8%), which translates to a larger performance gap at evaluation—the PPL difference widens to 0.79 points. This suggests s123's KL predictor learned more complex mask patterns that the BCE's factorized loss struggles to capture. can't learn these subtle joint-dependent patterns.

This creates the narrative problem: if gradient coupling doesn't matter (as s42 showed), why can't BCE learn the masks perfectly for all seeds? The answer must be that gradient coupling contributes something in some cases, undermining the "gradient coupling = 0" universal claim.

For s123, the KL predictor converged to a different local optimum with more neurons in the borderline zone (gate probability 0.4-0.6). These borderline neurons have importance that depends on their joint activation patterns with other neurons, which BCE's factorized loss can't capture. The oracle agreement dropped from 0.978 to 0.92, creating a 0.79 PPL gap—showing that gradient coupling's contribution is actually seed-dependent. In some loss landscape regions like s42, the KL mask happens to be approximable by independent importance scores, but in others like s123, the joint interaction patterns are irreducible.

Now I'm thinking through what figures these experiments should contribute to—the C1 ablation becomes a bar chart comparing the three seeds, the BCE 30% result goes into the operating point table, and the regime curve plots PPL against sparsity across the different conditions.

Generating comprehensive results tables...

I'm realizing there's a critical issue with my regime curve data—the 30% and 50% sparsity points I marked as known values actually came from experiments using a shared predictor trained at 50%, not the dedicated predictors I'm supposed to be using for this sweep. I need to reconsider which values are actually valid reference points for the 6-point curve with dedicated predictors. I think the eval would use DEDICATED predictors at each sparsity level, though for 40% there's no dedicated predictor in the registry, so I might need to fall back on the 50%-trained predictor result from d030. Let me map out the six-point curve with the best available data: 25%, 30% (8.82), 35%, 40% (8.36), 45%, and 50% (11.96), then I'll structure this cleanly in the YAML output. that these are dedicated-predictor results where available. I'm laying out the 6-point curve with actual PPL values, noting which predictors I'm using and where there are gaps. At the 40% point I'm hitting a snag—the dedicated predictor doesn't exist, so I need to decide between using the 50%-trained predictor evaluated at 40% uniform allocation or finding an alternative, and the values I'm getting suggest some non-monotonicity that's making the story less clean. already a violation. Adding 35% at 8.55 would make it:
  25%(8.90) → 30%(8.82) → 35%(8.55) → 40%(8.36): three consecutive violations!
  
Wait, this is already 3 violations which is the max in the worst-case range [2,3].

Let me reconsider. The d030_kl40_uniform value (8.36) is the 50%-predictor at 40% uniform. But the what_if is about dedicated predictors. If the paper uses mixed data sources, the curve is:

Using best available:
- 25%: 8.90 (new, dedicated)
- 30%: 8.82 (existing, dedicated)
- 35%: 8.55 (new, dedicated)
- 40%: 8.36 (existing, 50%-predictor) OR new

Now I'm checking whether using a dedicated predictor at 40% instead of the 50%-predictor would reduce violations. If I stick with 8.36, I get three consecutive violations across 25→30→35→40. But if a dedicated predictor at 40% yields something like 8.80, that would break the chain at the last step, bringing me down to just two violations, which fits within the worst-case range of 2-3. Hmm, but there's a problem. The d030_kl40_uniform number (8.36) is ALREADY MEASURED. I can't predict a different value for it. It's a DONE experiment.

So if the paper uses d030 data for 40%, that's 3 violations (all in 25-40 range).

If the paper uses a new dedicated 40% predictor, I can predict that value.

Looking at the registry, kl_sparsity40_s42_eval_teal_uniform is PREPARING but there's no kl_sparsity40_s42 TRAINING experiment. So either:
1. There's no dedicated 40% predictor, paper uses d030 data
2. Training was done but not registered

Given the ambiguity, I think the paper would use d030 for 40% and get 8.36. But then the curve has 3 violations: 25→30, 30→35, 35→40 all show decreasing PPL. The full sequence is 8.90, 8.82, 8.55, 8.36, then it jumps to 10.20 at 45% and 11.96 at 50%—a U-shaped curve with a sweet spot around 35-40% before a sharp capacity cliff. The problem is that the 25-40% descent is too gradual and non-monotonic to cleanly separate into distinct regimes like "budget-surplus" versus "budget-constrained." The PPL and MMLU metrics diverge sharply—PPL's cliff appears at 45% sparsity while MMLU's happens at 40%—which undermines the clean phase transition narrative since the regime boundaries shift depending on which metric you prioritize. This inconsistency is exactly what reviewers would flag as a weakness in the regime analysis. Now I'm working through the LongBench worst-case scenario and need to estimate scores more carefully, accounting for how F1 and ROUGE-L scoring work across the different task types.

Looking at the existing data, the KL 30% results show substantial drops across QA tasks (40-55% degradation), though the multi_news spike to 18.01 compared to the dense baseline of 2.5 seems anomalous—possibly the sparsity mask is inadvertently filtering noise that helps summarization, or there's a scoring artifact. The dense baseline scores themselves are quite low overall since Llama 3.1 8B struggles with long-context tasks without instruction tuning, and KL 50% shows even steeper degradation around 70%.

Now I'm projecting the full LongBench results across different task categories. The dense baseline averages around 10.5 for single-document QA, 18.0 for multi-document QA and summarization, 35.0 for few-shot tasks, and 30.0 for code. With KL 30% uniform sparsity, single-document QA drops to 5.5 (a 48% decline), and multi-document QA falls to 9. The BCE+comp approach at 30% shows similar degradation patterns without meaningful differentiation from KL, and the scoring artifacts make it difficult to draw clear conclusions about which approach actually performs better. Now I'm looking at the performance metrics across different compression methods on LongBench and MT-Bench. The KL divergence approach at 30% compression performs nearly identically to the BCE with compensation method, though KL still maintains a slight edge, which supports the hypothesis that KL eliminates the need for compensation. For MT-Bench scoring, which uses a 1-10 scale per turn averaged across 80 questions and 8 categories, the baseline Llama 3.1 8B Instruct model achieves around a 7.

However, there's a critical issue: the project is using the base model rather than the instruction-tuned variant, and base models perform extremely poorly on MT-Bench since they lack instruction-following capabilities. This would result in scores around 3-4 for the dense model and even lower for the compressed variants, making any comparison essentially meaningless. This likely explains why this particular experiment is marked as P2 priority and deferred unless time permits, since MT-Bench simply isn't a suitable evaluation metric for base models.

If the project were somehow using the instruct variant instead, the scores would be more interpretable—around 7.5 for dense and 5.5-3.5 for the compressed variants—but that would require either separate predictor training or relying on transfer from a base-model-trained predictor to an instruct model at inference time, which introduces additional uncertainty about whether the transfer is effective. Either way, the effort seems misaligned with the project's actual setup and goals.

For RULER, I'd face similar constraints with base models—generation-based evaluation is noisy, though perplexity-based metrics might be clearer. I think I have enough to work with now. Let me compile the YAML with realistic worst-case numbers for the C1 ablation: the perplexity deltas, oracle agreement scores, and downstream performance gaps like the 3.4 percentage point drop on ARC-c.

Now I'm pulling together the specific metrics across all three seeds—the KL uniform PPL values, the BCE+KL baseline comparisons, and calculating the mean delta of 0.46 with standard deviation of 0.34 to show the variance across runs.

Looking at the BCE 30% forced top-k configuration, I'm comparing its PPL of 9.15 and downstream performance against the KL 30% uniform baseline (PPL 8.82), which shows a PPL gap of 0.33 with relatively small downstream deltas across the board.

Now I'm planning out the evaluation structure for the 6-point regime curve using TEAL uniform with dedicated predictors—I'll report both PPL and full downstream metrics across the 25%, 35%, and 45% conditions, plus the 40% TEAL uniform point. For the longer-context benchmarks, I'm setting up predictions for per-category averages on LongBench and MT-Bench, and per-task scores at different context lengths for RULER. I need to make sure each experiment's analysis field clearly explains the methodology.

The key issue I'm seeing is that the seed inconsistency across different runs undermines the clean decomposition narrative—the PPL deltas vary significantly depending on which seed is used. The BCE and KL results are converging at the recommended operating point, which weakens the claim that mask discovery is a unique advantage. More problematically, the 6-point regime curve shows multiple monotonicity violations that break the three discrete regimes story, so I'll need to reframe this around what's actually happening in the data rather than forcing a phase transition narrative.

Looking at the generalization results, the predictor struggles with longer contexts in QA tasks, and the other benchmarks are limited by what the base model can capture. So my reframing strategy is to shift from claiming clean decomposition to acknowledging that gradient coupling and target quality contributions are entangled in a seed-dependent way. For the KL advantage, instead of claiming it's uniquely better at mask discovery, I'll position it as the only zero-shot pathway to finding an oracle without manual design—even if BCE can eventually learn similar masks. And for the regimes, I'm moving away from discrete phases entirely and describing this as a continuous quality-sparsity tradeoff where the optimal allocation point varies depending on the specific conditions.

Now I'm strengthening the mechanistic story around the 103× gradient SNR ratio and building out a formal taxonomy of the loss functions as conceptual contributions. The 14B scale analysis and Mistral experiments give me systematic breadth across architectures. I'm expecting reviewer feedback in the 3.0-3.5 range for findings, which means I'd need either a significant reframe or additional experiments to reach Main Conference acceptance.

Now I'm writing out the YAML configuration to document which experiments are planned versus completed.

Looking at the status flags, I have six total experiments across planned and what-if categories. For the ablation study, s42 is done but s123 failed and s456 haven't been attempted yet—I need to predict the retry and remaining seeds. The sparsity sweep has partial coverage at 30% and 50%, with 40% done through another experiment, so I'm predicting the gaps at 25%, 35%, and 45%. The forced topk experiment hasn't started, so I'm forecasting the full result.

Now I need to predict the remaining three plans that haven't been attempted. I'll structure these as individual imagined experiment entries with full metrics.

For the worst-case scenario where C1 replication fails, the narrative shifts significantly. Instead of claiming gradient coupling equals zero as a causal finding, the paper would need to reframe it as: target quality is the dominant driver, but gradient coupling's actual contribution varies between 0% in s42 and roughly 18% in s123 depending on the mask structure. This substantially undermines the first claim.

The 53% mask divergence finding remains robust since it's independent of seed variation, but the causal story becomes murkier. The paper would need to report all three seeds with error bars, acknowledge that gradient coupling isn't actually zero in some configurations, and shift the framing to emphasize that target quality explains 82-100% of KL's advantage while gradient coupling and target quality are entangled rather than separable.

For the BCE comparison at the 30% operating point, the paper would need to concede that BCE is actually competitive there. The reframing would pivot away from claiming KL produces inherently better masks and instead highlight KL's advantages in automated discovery without oracle design and robustness across different sparsity levels. The story becomes about the process of finding good masks rather than the masks themselves.

For the regime curve analysis, I'd drop the claim about discrete phase transitions and present this as a continuous PPL-sparsity tradeoff with non-monotonic local optima. The PPL-downstream dissociation becomes a positive contribution showing PPL is a poor proxy for downstream quality under sparsity, and the focus shifts to practical recommendations like the 30% uniform allocation point rather than theoretical regime characterization. This trajectory points toward EMNLP Findings rather than Main conference, probably scoring around 3.0-3.5.

Now I'm mapping out which experiments feed into each table and figure for the paper structure. The reviewers are raising serious concerns about the core claims—the seed inconsistency in the ablation undermines the decomposition story, the noisy regime curve with multiple violations weakens the methodology narrative, and the downstream task performance is alarming, with MMLU dropping dramatically at the recommended sparsity level and essentially collapsing at 50%.

What's particularly damaging is that the promised efficiency gains don't materialize in practice: the predictor actually slows down inference, and the theoretical FLOP savings aren't reflected in real wall-clock speedups, which is a critical failure for a paper positioning itself as an efficiency contribution. Averaging the scores across reviewers lands at 3.25, solidly in the borderline reject territory.

Now I'm mapping out the experiments I need to construct for the imagined results—ablation replications across multiple seeds, a forced top-k variant with BCE loss at 30% sparsity, a sweep across different sparsity levels with fitted curves, and full evaluations on the longer-context benchmarks. I'll stick with the project's convention of decimal notation for proportions and absolute values for perplexity metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6de7e3a-e6ce-455f-aa19-39052e19c051",
  "isSidechain": false,
  "requestId": "req_011CbAUB7ZbEjiCrhziSigen",
  "type": "assistant",
  "uuid": "efb796b9-a6d2-400c-8471-a6377e7bbfba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BspfPoRa8PYRH3JWdDAUnK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7979,
      "cache_read_input_tokens": 50761,
      "output_tokens": 36103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7979,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 36103,
          "cache_read_input_tokens": 50761,
          "cache_creation_input_tokens": 7979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7979
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

_source line 17 · 2026-05-18T18:10:53.304Z_

```yaml
tier: worst
narrative_guidance: |
  C1 seed 不一致（s123 Δ=0.85, s456 Δ=0.60 vs s42 exact match）使 "gradient coupling = 0" clean decomposition 不可持续。
  BCE 30% forced top-k PPL 9.15 vs KL 8.82（Δ=0.33）在 recommended operating point 追平，mask discovery 优势被消解。
  6-point regime curve 含 3 处 monotonicity violation（25→30, 30→35, 35→40 PPL 递减），discrete phase transition 叙事崩溃。
  Reframe 方向：
    (1) C1 → "gradient coupling 和 target quality 贡献纠缠，比例 seed-dependent（0–18%），target quality 仍是 dominant 但非 sole driver"
    (2) KL 30% 优势 → "zero-shot automated oracle discovery pathway"——KL 的价值是无需手动设计 oracle 即可发现 good mask，即使 BCE 事后能学到 similar mask
    (3) Regime → 放弃 three discrete regimes + phase transition，改为 "continuous quality-sparsity tradeoff with allocation-dependent local optima"；PPL-downstream dissociation 本身作为 finding
    (4) 补强 gradient SNR 103× + formal loss taxonomy 作为 mechanistic + conceptual 贡献
    (5) 14B scale analysis + Mistral cross-arch + 6-point dense sweep 作为 systematic study breadth
  预期 reviewer score 均值 3.0–3.5（Findings 区间）。Main Conference 需 significant additional contribution 或 reframe。仍冲 EMNLP Main，Findings 作为现实 fallback。

imagined_experiments:
  - name: c1_ablation_replication_3seed
    plan_id: c1_ablation_bce_kl_targets
    description: |
      C1 causal ablation 的 s123 retry 和 s456 新实验。训练 BCE predictor 使用各 seed 的 KL-derived oracle mask 作为 target，
      在 TEAL uniform 50% 协议下评估，与对应 seed 的 KL predictor 对比。验证 s42 exact match 是否跨 seed 复现。
    expected_results:
      # --- s123 ---
      s123_bce_kl_targets_ppl_teal_uniform_50pct: 12.71
      s123_kl_reference_ppl_teal_uniform_50pct: 11.86
      s123_ppl_delta: 0.85
      s123_oracle_agreement: 0.921
      s123_train_bce_loss: 0.072
      s123_arc_challenge_acc_norm: 0.345
      s123_winogrande_acc: 0.598
      s123_mmlu_acc: 0.253
      s123_gsm8k_exact_match: 0.015
      s123_downstream_ref_arc_c: 0.379
      s123_downstream_ref_wg: 0.622
      s123_downstream_ref_mmlu: 0.278
      s123_downstream_ref_gsm8k: 0.024
      s123_max_downstream_delta_pp: 3.4  # ARC-c: 34.5 vs 37.9
      # --- s456 ---
      s456_bce_kl_targets_ppl_teal_uniform_50pct: 12.55
      s456_kl_reference_ppl_teal_uniform_50pct: 11.95
      s456_ppl_delta: 0.60
      s456_oracle_agreement: 0.943
      s456_train_bce_loss: 0.063
      s456_arc_challenge_acc_norm: 0.362
      s456_winogrande_acc: 0.612
      s456_mmlu_acc: 0.268
      s456_gsm8k_exact_match: 0.019
      s456_max_downstream_delta_pp: 2.1  # WG: 61.2 vs 62.0 + ARC-c: 36.2 vs 38.3
      # --- 3-seed summary ---
      three_seed_ppl_deltas: [0.00, 0.85, 0.60]
      three_seed_ppl_delta_mean: 0.48
      three_seed_ppl_delta_std: 0.36
      three_seed_oracle_agreement_mean: 0.947
      three_seed_oracle_agreement_std: 0.024
      three_seed_max_downstream_delta_pp: 3.4
      gradient_coupling_contribution_range_pct: "0–18%"
    result_rationale: |
      s42 的 exact match（Δ=0.00）是 seed-specific 的幸运结果：s42 的 KL predictor 收敛到的局部最优产生了
      "clean" mask pattern——borderline zone（gate probability 0.4–0.6）的 neuron 比例低（~8%），使 BCE 的
      factorized loss 足以高精度复制。s123 的 KL predictor 收敛到了不同局部最优，borderline neuron 比例更高（~14%），
      这些 neuron 的重要性依赖于与其他 neuron 的共激活模式（joint interaction），BCE 无法捕捉。oracle agreement
      从 0.978 降至 0.921，6% 的 mask 分歧集中在 knowledge-critical 中间层（L12–L20），导致 ARC-c 推理任务
      出现 3.4pp gap。s456 介于两者之间（agreement 0.943，Δ=0.60），表明 gradient coupling 贡献是 loss landscape
      局部结构的函数。3-seed 平均 Δ=0.48 技术上 <0.5，但 s123 的 0.85 无法被 error bar 掩盖，审稿人会质疑
      "gradient coupling = 0" 的普遍性声明。
    tables:
      - "Table 3: C1 Causal Ablation（3 seeds，PPL + 4 downstream tasks，含 oracle agreement）"
    figures_description:
      - "Figure 4: C1 ablation bar chart — 3 组 paired bars（BCE+KL-targets vs KL reference），error bars 在 s123/s456 不重叠，s42 完全重叠。视觉上立即看出 seed 不一致。"
    analysis: |
      C1 从 "clean decomposition proving gradient coupling = 0" 降级为 "target quality is dominant but gradient coupling
      contribution is seed-dependent (0–18%)"。论文需要：(1) 诚实报告 3 seed 及 variance；(2) 放弃 "sole driver" 措辞，
      改为 "primary driver, explaining 82–100% of advantage"；(3) 将 seed 依赖性本身作为 finding 讨论——mask landscape
      的局部结构决定了 gradient coupling 的边际贡献。C1 仍有价值（first attempt at causal decomposition for sparsity
      predictor training loss），但 novelty 从 "empirical discovery" 降为 "informative ablation with nuanced outcome"。
      审稿人会说 "interesting but not conclusive"。

  - name: bce_30pct_forced_topk_eval
    plan_id: bce_30pct_forced_topk
    description: |
      BCE predictor（trained at 30% target on Llama-3.1-8B）通过 forced TEAL top-k 在 30% uniform sparsity 下评估。
      填充 Table 2 的 BCE 30% operating point 数据。对比 KL 30% uniform（PPL 8.82）和 TEAL 30%（PPL 10.97）。
    expected_results:
      wikitext2_ppl_teal_uniform_30pct: 9.15
      gap_vs_kl30_uniform: 0.33
      gap_vs_teal30: -1.82
      arc_challenge_acc_norm: 0.401
      winogrande_acc: 0.668
      mmlu_acc: 0.378
      gsm8k_exact_match: 0.062
      # KL 30% uniform references (3-seed mean)
      ref_kl30_uniform_ppl: 8.82
      ref_kl30_uniform_mmlu: 0.385
      ref_kl30_uniform_arc_c: 0.443
      ref_kl30_uniform_wg: 0.692
      # Gaps vs KL 30% uniform (3-seed mean)
      mmlu_gap_vs_kl30_pp: -0.7
      arc_c_gap_vs_kl30_pp: -4.2
      wg_gap_vs_kl30_pp: -2.4
      predictor_native_sparsity: 0.295
      lagrangian_converged: true
    result_rationale: |
      30% sparsity 下 magnitude-based mask 与 optimal mask 的重合度远高于 50%（Jaccard ~0.6 vs ~0.4），因为
      需要剪除的 neuron 大多是 "trivially unimportant"（activation magnitude 极低 + gate probability 极低），
      BCE 和 KL 在这些 easy case 上完全一致。KL 的 joint interaction 优势只在 borderline neurons 上体现，而
      30% 时 borderline zone 极窄（仅需剪除最不重要的 30%，几乎没有 hard decision）。PPL gap 从 50% 时的
      ~14 PPL（22.51 vs 8.82, 对比 BCE 50% vs KL 30%）收缩到 30% 时的 0.33，确认 KL-BCE delta 随 sparsity
      近似二次收缩。BCE Lagrangian 在 8B 30% target 下正常收敛（不像 Qwen-14B 的 collapse），因为 30%
      目标松弛、loss landscape smooth。下游任务 gap 最大 4.2pp（ARC-c），在 3-seed KL variance 范围内。
      审稿人会看到 Table 2 中 KL 和 BCE 在 recommended operating point 几乎没有差别，质疑 KL 的实际部署价值。
    tables:
      - "Table 2: Recommended Operating Point Comparison（30% sparsity, all methods）"
      - "Table 1: Main Results（增加 BCE 30% 行）"
    figures_description:
      - "Figure 3: Pareto frontier — BCE 30% 点位紧贴 KL 30%，两者在 30% 处近乎重叠，仅在 ≥40% 区间拉开距离。"
    analysis: |
      BCE 30% PPL 9.15 vs KL 8.82（Δ=0.33, 3.7%）在 recommended operating point 实质追平。这削弱了 "KL discovers
      fundamentally different masks" 作为 practical advantage 的叙事——在用户最可能部署的 sparsity level 上，
      简单的 BCE + magnitude oracle 就足够好。KL 的优势主要体现在 ≥40% 的高 sparsity 区间，而该区间的 downstream
      collapse（MMLU ~31%）使其本身缺乏部署价值。
      Reframe: KL 的价值不在于 "better masks at all sparsity levels"，而在于 (a) 自动发现 good mask（zero-shot,
      无需预定义 oracle），(b) 在高 sparsity 区间提供 graceful degradation 而非 catastrophic collapse，
      (c) 跨 sparsity level 的 single training recipe（一个 KL predictor 可在 30–50% 间灵活部署，而 BCE 需要
      per-level oracle 设计）。

  - name: dense_sparsity_sweep_6pt
    plan_id: dense_sparsity_sweep_6pt
    description: |
      KL predictor 在 25%/30%/35%/40%/45%/50% 六个 sparsity level 的 TEAL uniform 评估。
      使用各 level 的 dedicated predictor（25/35/45 为新训练，30/40/50 复用已有）。
      生成 regime curve 并尝试识别 regime boundary。
    expected_results:
      # === PPL (TEAL uniform, dedicated predictors) ===
      ppl_25pct: 8.90
      ppl_30pct: 8.82   # known (d030_kl30_uniform)
      ppl_35pct: 8.55
      ppl_40pct: 8.36   # known (d030_kl40_uniform, 50%-trained predictor)
      ppl_45pct: 10.25
      ppl_50pct: 11.96  # known (d030_kl50_uniform)
      monotonicity_violations_ppl: 3  # 25→30, 30→35, 35→40 all decrease
      # === TEAL global (dedicated predictors) ===
      ppl_global_25pct: 9.05
      ppl_global_30pct: 8.98   # known (bench_kl30_global ~8.98)
      ppl_global_35pct: 8.70
      ppl_global_40pct: 10.12  # known (bench_kl40_global)
      ppl_global_45pct: 10.90
      ppl_global_50pct: 11.79  # known (bench_kl50_global)
      monotonicity_violations_ppl_global: 2  # 25→30 decrease, 30→35 decrease
      # === Downstream (TEAL uniform) ===
      mmlu_25pct: 0.390
      mmlu_30pct: 0.406  # known
      mmlu_35pct: 0.415
      mmlu_40pct: 0.307  # known (d030_kl40_uniform)
      mmlu_45pct: 0.282
      mmlu_50pct: 0.278  # known
      mmlu_monotonicity_violations: 2  # 25→30 increase, 30→35 increase (both violations: more sparsity should → worse MMLU)
      arc_c_25pct: 0.430
      arc_c_30pct: 0.408  # known
      arc_c_35pct: 0.440
      arc_c_40pct: 0.418  # known
      arc_c_45pct: 0.350
      arc_c_50pct: 0.328  # known
      arc_c_monotonicity_violations: 3  # 25→30 decrease OK, 30→35 increase ✗, 35→40 decrease OK (more sparsity worse), 40→45 decrease OK... wait
      # Let me recalculate ARC-c violations:
      # 25(0.43)→30(0.408) decrease ✓ (monotonic: more sparsity → worse)
      # 30(0.408)→35(0.440) increase ✗ VIOLATION
      # 35(0.440)→40(0.418) decrease ✓
      # 40(0.418)→45(0.350) decrease ✓
      # 45(0.350)→50(0.328) decrease ✓
      # = 1 violation for ARC-c
      winogrande_25pct: 0.700
      winogrande_30pct: 0.686  # known
      winogrande_35pct: 0.705
      winogrande_40pct: 0.672  # known
      winogrande_45pct: 0.640
      winogrande_50pct: 0.629  # known
      winogrande_monotonicity_violations: 2  # 25→30 decrease OK, 30→35 increase ✗, 35→40 decrease OK, rest OK... = 1
      gsm8k_25pct: 0.082
      gsm8k_30pct: 0.074  # known
      gsm8k_35pct: 0.065
      gsm8k_40pct: 0.039  # known
      gsm8k_45pct: 0.022
      gsm8k_50pct: 0.021  # known
      # PPL sweet spot: 35–40% (min PPL 8.36 @ 40%)
      # MMLU cliff: 35→40% (41.5→30.7, Δ=10.8pp)
      # PPL cliff: 40→45% (8.36→10.25, Δ=1.89)
      ppl_cliff_location: "40–45%"
      mmlu_cliff_location: "35–40%"
      cliff_dissociation: "PPL 和 MMLU 的 cliff 位于不同 sparsity level，间隔约 5pp"
    result_rationale: |
      PPL 非单调性（25→40% 持续下降）的机制：dedicated predictor 在中等 sparsity（35–40%）达到 loss-sparsity 的
      最佳平衡——Lagrangian 约束满足良好（actual sparsity 接近 target），KL loss 有足够的 "budget" 学习 nuanced
      mask pattern。25% 时 predictor undertrained（actual 23%, lambda 打满 5000 仍不够），mask 质量反而不如
      30% 的 well-calibrated predictor。35% 时 predictor 在 sweet spot（actual 33.6%, loss 收敛良好），
      产生了比 30% 更优的 neuron ranking。40% 沿用 50%-trained predictor at 40% uniform（d030 数据），
      该 predictor 在 40% 时仍有余量因此 PPL 最低。

      45→50% 的急剧上升反映 capacity cliff——不是 allocation 问题（都用 uniform），而是 model 容量不足。
      但 MMLU 的 cliff 出现在 35→40%（Δ=10.8pp），比 PPL cliff（40→45%）早一个档位。这反映 knowledge-intensive
      tasks（MMLU）对 neuron 缺失的敏感度高于 perplexity——PPL 可以靠 redistributing probability mass 补偿，
      但 factual recall 一旦关键 neuron 被剪就不可逆。

      3 处 PPL monotonicity violation 使 "three discrete regimes with phase transitions" 叙事不可持续：
      没有从 regime 1 到 regime 2 的 clean boundary，整个 25–40% 区间是一个 non-monotonic plateau。
      审稿人会质疑 "regime" 分类的 principled basis。
    tables:
      - "Table 5: 6-Point Sparsity Regime Analysis（PPL + 4 downstream, uniform + global allocation）"
    figures_description:
      - "Figure 2: PPL vs Sparsity regime curve — 6 点折线含 3 处回折（25–40% 下降段），无法用垂直虚线清晰标注 regime boundary。需改为 smooth fitted curve + shaded confidence band，弱化 discrete transition 叙事。"
      - "Figure 2b (subplot): MMLU vs Sparsity — cliff 位置在 35–40%，与 PPL cliff（40–45%）不重合，用双 y 轴叠加展示 PPL-MMLU dissociation。"
    analysis: |
      Regime analysis 从 Claim 3 的核心贡献降级为 supplementary empirical characterization。原始叙事
      "three discrete regimes (budget-surplus / budget-constrained / capacity-cliff) with non-monotonic allocation
      preference" 被替换为：(a) continuous degradation with a PPL sweet spot around 35–40%；(b) PPL-downstream
      dissociation 作为 finding（PPL cliff at 40–45%, MMLU cliff at 35–40%）；(c) practical recommendation
      不变（30% uniform），但理由从 "optimal regime 1 operating point" 改为 "safety margin below cliff"。
      Non-monotonicity 可 spin 为 "dedicated-predictor optimization effect"（each sparsity level has its own
      training sweet spot），但审稿人可能视为 experimental noise 或 Lagrangian artifact。
      建议在论文中补充 3-seed bars at 30/50 以佐证 known points 的 stability，并坦承 single-seed sweep
      限制了 statistical confidence。

  - name: longbench_full_evaluation
    plan_id: plan_010
    description: |
      LongBench English subset（14 tasks, 4K–32K tokens）评估所有条件：KL 30% uniform, KL 50%,
      BCE+comp 30%, TEAL 30%, TEAL 50%, Dense。测试 predictor 在超出训练序列长度（2048）时的泛化能力。
    expected_results:
      # Scores are F1 (QA) or ROUGE-L (Summarization), scale 0-100
      # --- Dense ---
      dense_single_doc_qa_avg: 10.8  # NarrativeQA, Qasper, MultiFieldQA
      dense_multi_doc_qa_avg: 18.5   # HotpotQA, 2WikiMQA, MuSiQue
      dense_summarization_avg: 18.2  # GovReport, QMSum, MultiNews
      dense_few_shot_avg: 36.0       # TREC, TriviaQA, SAMSum
      dense_code_avg: 31.5           # LCC, RepoBench-P
      dense_overall_avg: 23.0
      # --- KL 30% uniform ---
      kl30_single_doc_qa_avg: 5.8
      kl30_multi_doc_qa_avg: 9.5
      kl30_summarization_avg: 14.5
      kl30_few_shot_avg: 21.0
      kl30_code_avg: 19.0
      kl30_overall_avg: 14.0
      kl30_retention_vs_dense: 0.61   # 61% of dense
      # --- KL 50% ---
      kl50_single_doc_qa_avg: 2.2
      kl50_multi_doc_qa_avg: 3.8
      kl50_summarization_avg: 8.5
      kl50_few_shot_avg: 8.5
      kl50_code_avg: 9.0
      kl50_overall_avg: 6.4
      kl50_retention_vs_dense: 0.28
      # --- BCE+comp 30% ---
      bce_comp_30_single_doc_qa_avg: 5.2
      bce_comp_30_multi_doc_qa_avg: 8.8
      bce_comp_30_summarization_avg: 13.5
      bce_comp_30_few_shot_avg: 19.5
      bce_comp_30_code_avg: 17.5
      bce_comp_30_overall_avg: 12.9
      bce_comp_30_retention_vs_dense: 0.56
      # --- TEAL 30% (training-free) ---
      teal30_single_doc_qa_avg: 4.2
      teal30_multi_doc_qa_avg: 7.2
      teal30_summarization_avg: 11.5
      teal30_few_shot_avg: 16.0
      teal30_code_avg: 15.0
      teal30_overall_avg: 10.8
      teal30_retention_vs_dense: 0.47
      # --- TEAL 50% ---
      teal50_overall_avg: 3.8
      teal50_retention_vs_dense: 0.17
      # --- Key comparisons ---
      kl30_vs_bce_comp30_delta: 1.1  # KL 略好但差距小
      kl30_vs_teal30_delta: 3.2      # KL 明显好于 training-free
      worst_category_kl30: "single-doc QA (-46%)"
      best_category_kl30: "summarization (-20%)"
    result_rationale: |
      Predictor 在 2048 tokens 上训练，LongBench 任务平均 8K–16K tokens。超出训练长度后 predictor 的
      neuron importance judgment 退化：(1) attention pattern 在长序列中分布更均匀，activation magnitude
      排序改变，predictor 学到的 "哪些 neuron 重要" 部分失效；(2) Llama 3.1 8B 使用 RoPE 位置编码，
      支持 128K 但 2048 训练的 predictor 未见过长距离 dependency pattern，导致 long-range QA 任务退化最严重
      （single-doc QA -46%）；(3) Summarization 相对保留（-20%），因为 extractive 倾向——保留 high-magnitude
      neurons 即可抓住 salient sentences，不依赖 fine-grained neuron interaction。

      KL 30% vs BCE+comp 30% 差距仅 1.1 分（14.0 vs 12.9），因为长序列评估中 predictor 的 mask quality
      优势被序列长度 generalization gap 部分抵消。BCE+comp 的 compensation MLP 在长序列中反而可能提供
      额外的 error correction（因为它在推理时修补 per-layer error，与序列长度无关），部分弥补了 BCE 的
      weaker mask。这进一步模糊了 "KL eliminates compensation" 的实际意义。

      Dense baseline 本身分数偏低（overall 23.0），反映 Llama 3.1 8B base model 在 long-context generation
      tasks 上的固有局限（非 instruction-tuned）。低 baseline 使得 relative degradation 看起来更严重，
      但 absolute 差异小——审稿人可能质疑 evaluation 的 informative value。
    tables:
      - "Table 5: LongBench Results by Task Category（5 categories × 6 conditions, retention % vs dense）"
    figures_description:
      - "Figure 6 (Appendix): Grouped bar chart — 5 categories × 6 conditions，visual 上 KL 30% 和 BCE+comp 30% bars 高度接近，仅在 few-shot 和 code 略有区分。"
    analysis: |
      LongBench 结果 mixed：KL > TEAL（training-free）confirmed，但 KL vs BCE+comp 差异在 long-context 上
      被压缩到不显著水平。Dense baseline 偏低限制了评估的 discriminative power。
      对论文的影响：(1) 不宜作为 main contribution，降为 appendix 或简要提及；(2) 如果 reviewer 要求
      long-context evaluation，可呈现但需坦承 base model limitation 和 predictor generalization gap；
      (3) 建议补充 "predictor seq-len generalization" 分析（对比 2048 vs 4096 训练长度的 predictor 在
      LongBench 上的差异），但 GPU budget 可能不允许。
      实际影响：plan_010 的 P1 优先级在 worst case 下应降为 P2，将 GPU hours 重新分配给更能 strengthen
      narrative 的实验（如 BCE 30% 的多 seed 验证）。

  - name: mtbench_evaluation
    plan_id: plan_011
    description: |
      MT-Bench 80 题多轮评估（GPT-4o judge），8 categories。测试 sparsity 对 instruction-following
      和 multi-turn coherence 的影响。需要 instruction-tuned model 或 base model 的 few-shot prompting。
    expected_results:
      # Assuming base model evaluation (Llama 3.1 8B base)
      # MT-Bench scores 1-10, per turn, averaged
      dense_overall: 3.8           # base model, 远低于 instruct (~7.5)
      dense_writing: 4.5
      dense_roleplay: 4.2
      dense_reasoning: 3.5
      dense_math: 2.0
      dense_coding: 3.8
      dense_extraction: 5.0
      dense_stem: 3.2
      dense_humanities: 4.2
      kl30_uniform_overall: 2.9
      kl30_uniform_drop_vs_dense: -0.9
      kl30_uniform_drop_pct: -23.7
      kl50_overall: 1.8
      kl50_drop_pct: -52.6
      bce_comp30_overall: 2.7
      teal30_overall: 2.4
      # 关键问题
      base_model_discriminative_power: "low — dense baseline 3.8 已接近 floor，sparsity 条件间差异被压缩"
      worst_category_kl30: "math (1.2, -40% vs dense 2.0)"
      evaluation_cost: "需要 GPT-4o API, ~$15-20 per full evaluation"
    result_rationale: |
      Llama 3.1 8B base model 在 MT-Bench 上的 dense score 仅 ~3.8（instruct 版本 ~7.5），因为 base model
      不擅长 instruction following 和 multi-turn dialogue。在如此低的 baseline 上，sparsity 造成的额外退化
      被 floor effect 压缩——即使 50% sparsity 的 score（1.8）也只比 dense（3.8）低 2.0 分，而 instruct 模型
      上相同 sparsity 可能造成 3–4 分的下降。

      结果的信息量极低：所有条件都在 1.5–4.0 分区间内，差异可能在 judge model 的评分 noise 范围内。
      Math 和 STEM 类别退化最严重（floor 更明显），writing 和 humanities 相对保留。
      KL 30% vs BCE+comp 30% 差异仅 0.2 分，统计不显著。

      如果使用 instruct model（需额外配置 predictor 迁移），结果会更有区分度，但引入了 "base-trained predictor
      on instruct model" 的 domain shift 问题。
    tables:
      - "Table 6 (Appendix): MT-Bench Scores by Category（8 categories × 5 conditions）"
    figures_description:
      - "不建议为 MT-Bench 制作 main-body figure——信息密度太低，scores 集中在窄区间内。如需展示，用 appendix 的 radar chart。"
    analysis: |
      MT-Bench 在 worst case 下基本无用：base model baseline 太低（3.8），sparsity 条件间差异 <1 分，
      审稿人不会从这个评估中获得有价值的信息。建议：(1) 从论文中删除或仅在 appendix 一句话带过；
      (2) 如果 reviewer 明确要求 multi-turn evaluation，说明 "base model limitation, instruct model
      evaluation requires predictor transfer study which is out of scope"；(3) 将 plan_011 的 4 GPU hours
      和 API cost 重新分配。
      唯一可能的叙事价值：证明 "即使在最不利的评估条件下（low-baseline, multi-turn），KL 仍 ≥ TEAL"，
      但这是一个极弱的 claim。

  - name: ruler_evaluation
    plan_id: plan_012
    description: |
      RULER synthetic long-context evaluation at 4K 和 16K context length，3 task types
      （NIAH, Variable Tracking, Common/Frequent Words）。测试 predictor 在结构化长序列任务上的泛化。
    expected_results:
      # Accuracy (0-100)
      # --- 4K context ---
      dense_4k_niah: 92.0
      dense_4k_vt: 78.0
      dense_4k_cw: 85.0
      dense_4k_avg: 85.0
      kl30_4k_niah: 75.0
      kl30_4k_vt: 60.0
      kl30_4k_cw: 70.0
      kl30_4k_avg: 68.3
      kl30_4k_retention: 0.80
      kl50_4k_niah: 42.0
      kl50_4k_vt: 28.0
      kl50_4k_cw: 38.0
      kl50_4k_avg: 36.0
      kl50_4k_retention: 0.42
      # --- 16K context ---
      dense_16k_niah: 85.0
      dense_16k_vt: 62.0
      dense_16k_cw: 72.0
      dense_16k_avg: 73.0
      kl30_16k_niah: 48.0
      kl30_16k_vt: 30.0
      kl30_16k_cw: 42.0
      kl30_16k_avg: 40.0
      kl30_16k_retention: 0.55
      kl50_16k_niah: 18.0
      kl50_16k_vt: 12.0
      kl50_16k_cw: 15.0
      kl50_16k_avg: 15.0
      kl50_16k_retention: 0.21
      # --- Cross-length degradation ---
      kl30_retention_4k_to_16k_drop: -0.25  # 80% → 55%
      kl50_retention_4k_to_16k_drop: -0.21  # 42% → 21%
      dense_retention_4k_to_16k: 0.86       # 85.0 → 73.0
    result_rationale: |
      RULER 的 NIAH 任务要求模型精确定位特定位置的信息——这对 neuron pruning 极度敏感，因为 attention-to-FFN
      的 information routing 被 mask 截断。4K 时 predictor 尚可（训练长度 2048 的 2× 内），retention 80%。
      但 16K 时（训练长度的 8×），predictor 的 neuron importance judgment 严重失准：长序列中 attention 分布
      变化导致 FFN activation pattern 完全不同于训练分布，predictor 选择了错误的 neuron 保留。

      Variable Tracking 是最受影响的任务类型——需要跨 token 的持续 state tracking，而 sparse FFN 打断了
      intermediate representation 的 continuity。50% sparsity @ 16K 的 12% accuracy 接近 random（基于
      candidate pool size）。

      相对于 LongBench（基于 F1/ROUGE 的 generation 评估），RULER 的 accuracy-based 评估更尖锐地暴露了
      predictor 的 length generalization 失败。但问题在于：这是 ALL sparse methods 的共同问题（training-free
      TEAL 在长序列上同样退化），不是 KL-specific 的。没有 TEAL/BCE baseline 的 RULER 数据，审稿人无法
      判断 KL 是否比 alternative 更好。
    tables:
      - "Table 7 (Appendix): RULER Results at 4K and 16K（3 task types × 3 sparsity levels × 2 context lengths）"
    figures_description:
      - "Figure 7 (Appendix): Heatmap — task × context-length × sparsity, 颜色从绿（高保留）到红（低保留），右下角（50% × 16K）全红。"
    analysis: |
      RULER 结果确认了 worst-case 的 predictor length generalization 问题：超出训练长度 4× 以上，
      retention 从 80% 骤降至 55%（30%）和 21%（50%）。这是一个 honest limitation，但需要正确
      frame：(1) 所有 sparse inference 方法都面临 length generalization 问题，不是 KL-specific；
      (2) 解决方案是 longer training sequences（直接但 GPU-expensive）或 length-adaptive predictor
      （future work）；(3) 在论文中作为 limitation 明确讨论，不隐藏。
      对论文影响：(1) RULER 数据不进入 main body，放 appendix；(2) 在 Limitation section 引用 RULER 结果
      说明 "current predictor design assumes fixed-length training and degrades at 4× training length"；
      (3) 建议 future work 方向：mixed-length training 或 length-invariant predictor architecture。
      plan_012 的 P2 优先级在 worst case 下进一步降低——如果 deadline 紧张，完全可以 skip 并在
      limitation 中声明 "long-context evaluation is left for future work"。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efb796b9-a6d2-400c-8471-a6377e7bbfba",
  "isSidechain": false,
  "requestId": "req_011CbAUB7ZbEjiCrhziSigen",
  "type": "assistant",
  "uuid": "cf9a6c32-5841-4a90-90ba-e765db4de30a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BspfPoRa8PYRH3JWdDAUnK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7979,
      "cache_read_input_tokens": 50761,
      "output_tokens": 36103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7979,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 36103,
          "cache_read_input_tokens": 50761,
          "cache_creation_input_tokens": 7979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7979
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1 不复现或 BCE 30% 基本追平 KL，mask pattern discovery 叙事的核心优势被削弱 核心假设：['C1 s123 PPL delta > 0.5，或 downstream 出现 >3pp delta（gradient coupling 贡献 >15%）', 'BCE 30%…",
  "leafUuid": "cf9a6c32-5841-4a90-90ba-e765db4de30a",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe KL sparsity discovery as loss-aware alignment with systematic regime analysis",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1 不复现或 BCE 30% 基本追平 KL，mask pattern discovery 叙事的核心优势被削弱 核心假设：['C1 s123 PPL delta > 0.5，或 downstream 出现 >3pp delta（gradient coupling 贡献 >15%）', 'BCE 30%…",
  "leafUuid": "cf9a6c32-5841-4a90-90ba-e765db4de30a",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe KL sparsity discovery as loss-aware alignment with systematic regime analysis",
  "sessionId": "7cc89e23-684b-40f2-9f96-30cddc153fe3"
}
```

---
