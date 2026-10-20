# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：C1 ablation 在 controlled protocol 下出现显著 gap，'target quality = sole driver' 

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-3/af779414-f62d-4487-867b-50dcbebfd6c4.jsonl`
- **Structured JSON:** [`ffa75da597ace881ac91.json`](../../sessions/ff/ffa75da597ace881ac91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T17:17:34.181Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T17:17:34.181Z",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：C1 ablation 在 controlled protocol 下出现显著 gap，'target quality = sole driver' 被 falsify；regime 结构不清晰\n核心假设：['C1 uniform eval gap > 0.5 PPL（gradient coupling 贡献不可忽略，possibly 20-40% of gap）', '6-point sweep 无清晰 kink point，MMLU/PPL 行为不一致导致 regime 叙事牵强', 'BCE 30% forced TEAL PPL 9.0–10.0（BCE 在推荐工作点接近 KL，削弱核心 claim）', '审稿人判定为 incremental composition of known techniques', '14B + no wall-clock speedup + downstream gap 三重 weakness 使 practical impact 存疑']\n关键指标范围：{'c1_ppl_gap_50pct_uniform': [0.5, 2.0], 'bce_30pct_teal_ppl': [9.0, 10.0], 'regime_piecewise_R2': [0.7, 0.85], 'kl30_uniform_mmlu_3seed_mean': [0.35, 0.38], 'kl30_uniform_mmlu_3seed_std': [0.02, 0.04], 'expected_reviewer_avg': [3.0, 3.5], 'accept_probability': [0.05, 0.2]}\n叙事方向：核心 reframe：放弃 'mask pattern discovery' 作为 headline，转向 'A Systematic Framework for Understanding Loss-Sparsity Interactions in SwiGLU Pruning'。2D taxonomy（correction granularity × training signal coupling）升级为主要贡献。C1 ablation 重新诠释为 'quantifying the relative contribution of target quality vs gradient coupling'（partial result 仍有价值）。Claim 3 从 phase transition 降为 practitioner guidelines（'when to use uniform vs learned allocation'）。Paper 定位从 discovery → systematization + empirical study。仍冲 EMNLP Main（Efficient Methods track 对 systematic empirical work 有容纳空间），但叙事重心从 'we found something new' 转为 'we provide the first controlled decomposition of what matters for learned sparsity prediction'。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: distill_sparse_swiglu\nfocus: 测试 'mask pattern discovery' 叙事的审稿接收度。核心 reframe: C1 causal ablation 证明 target quality（不是 gradient coupling）是 KL 优势的唯一驱动力。BCE+KL-targets PPL = 11.9638 = KL PPL 11.9638（exact match at 50% sparsity, TEAL uniform）。53% mask divergence 作为新发现。包含 6-point sparsity regime analysis。目标 4.0 Main Conference。\n\n## paper_framing.md\n\n# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 to PPL. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). Standard BCE (magnitude masks) PPL ≈ 22.51. The gradient coupling contribution is zero; target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from \"engineering a better loss\" to \"discovering that output-distribution distillation reveals hidden neuron importance structure.\" **Supporting evidence**: (a) Iso-compute ablation: BCE with 2.71× more FLOPs still PPL=27.97 vs KL=12.00, confirming the gap is structural; (b) BCE Lagrangian failure at 30%: BCE loss scale (~0.6) vs KL (~0.0001) causes same Lagrangian to fail; (c) No compensation needed: KL eliminates 67.2M compensation parameters (~256MB). **Anticipated attack**: \"Two-stage training (KL→oracle→BCE) avoids needing KL predictor at inference?\" Defense: KL predictor is contextual (per-input adaptive); oracle masks are fixed. Deployment requires per-input sparsity adaptation. (Headline claim, resolves persistent R3-R8 confound)\n\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \"subsuming\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)\n\n3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports \"PPL is a poor proxy for downstream quality\" narrative. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.\n\n- **Our framing / headline question**: \"What does KL distillation actually learn for SwiGLU sparsity prediction, and why do its masks differ fundamentally from magnitude-based oracles?\" The theoretical grounding (§3.6, suggestive): BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm. This provides intuition for how KL *can* discover joint interaction patterns. The C1 causal ablation (§4.4) then empirically confirms: the masks KL discovers, not the gradient pathway itself, are what matter.\n\n- **Headline result template**: \"KL-trained sparsity predictors discover neuron importance patterns that diverge 53% from magnitude-based masks. A causal ablation confirms that these mask patterns, not gradient coupling, drive KL's quality advantage: BCE trained on KL-derived masks matches KL performance (PPL 9.29 vs 9.21 at ~60% sparsity). This finding eliminates the need for 67.2M compensation parameters and reveals three sparsity operating regimes with qualitatively different allocation requirements.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: **Substantially mitigated by C1 finding**. The 53% mask divergence and causal ablation are genuine empirical discoveries, not engineering contributions. No prior work has shown that KL-derived masks encode fundamentally different neuron importance from magnitude-based approaches. The paper now contributes a finding (mask pattern discovery) rather than just a method (combining known techniques). Additional support: formal decomposition framework, quantitative s^2 prediction, three-regime analysis.\n\n2. **\"KL wins only because more compute\"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 (plan_009, GQA + sliding window) and Qwen-2.5-14B cross-scale validation (D048/D054). **14B mixed result**: KL PPL advantage preserved (7.62 vs TEAL 8.73, 1.47× dense ratio identical to 8B), but KL MMLU=63.72% (global) / 64.49% (uniform) significantly trails TEAL 71.83% (global). Uniform allocation does not fix this gap (D054). PPL-downstream disconnect at 14B scale is an honest limitation, not hidden. Framing: KL's coupled gradient captures output-distribution fidelity (PPL) across scales, but 14B knowledge-intensive tasks (MMLU) show scale-dependent sensitivity that warrants further investigation.\n\n5. **\"Effect size may not hold on downstream tasks\"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.\n\n6. **\"Unfair comparison: BCE+comp close to KL but at higher inference cost\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- **Novelty upgraded from R8**: C1 causal ablation + 53% mask divergence finding elevates paper from \"systematic composition\" to \"empirical discovery about what KL learns for sparsity prediction.\" This addresses the persistent R3-R8 novelty concern and moves the paper toward Main Conference territory (target 4.0).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:\n    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline\n    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds\n    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and\n    BCE-only 3 seeds (mvp_bce_s42/s123/s456).\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps: []\n  registry_ids:\n  - mvp_kl_norm_v2_s42\n  - mvp_kl_norm_v2_s123\n  - mvp_kl_norm_v2_s456\n  - mvp_bce_s42\n  - mvp_bce_s123\n  - mvp_bce_s456\n  remaining_runs:\n  - KL-only 2 additional seeds (s0, s1) for 5-seed headline\n  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)\n  - KL+comp 3 seeds (s42, s123, s456)\n  registry_id: kl_only_s1\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- id: plan_002\n  claim: 1\n  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).\n    Isolates whether KL advantage comes from loss function or relaxation method. 3\n    seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: ste_baseline_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- id: plan_003\n  claim: 1\n  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs\n    (KL requires full forward pass for output logits, BCE can use cached targets).\n    Report per-step FLOPs and total training time for both. 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  registry_id: bce_isocompute_v2_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- id: plan_004\n  claim: 2\n  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL\n    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,\n    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: spon_2048_s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- id: plan_005\n  claim: 2\n  description: 'SPON subsumption verification: output-space linearity test showing\n    KL predictor already captures SPON correction signal. ||Delta_logits(s+c) - Delta_logits(s)\n    - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality analysis.\n    Proves SPON+KL ≈ KL (no additive gain). 3 seeds.\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  - plan_004\n  registry_id: plan_005_subsumption_s42\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- id: plan_006\n  claim: 1\n  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:\n    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),\n    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free\n    < static-learned < contextual-learned.\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_ids:\n  - training_free_baselines\n  - training_free_wina_greedy\n  registry_id: training_free_baselines\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- id: plan_007\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2\n    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor\n    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto\n    frontier plot.\n\n    '\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  - plan_004\n  - plan_005\n  - plan_006\n  registry_id: bench_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- id: plan_008\n  claim: 3\n  description: '3-level sparsity sweep (30%/50%/70%): KL-only vs BCE-only. Test scaling\n    trend and KL-BCE delta growth. 1 seed per level (sweep analysis, not headline).\n    50% data point reused from plan_001. If 3 levels show non-linear inflection, add\n    intermediate points.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  registry_id: d030_kl50_uniform\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- id: plan_009\n  claim: 1\n  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%\n    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds\n    each condition.\n\n    '\n  priority: P1\n  gpu_budget_hours: 24\n  deps:\n  - plan_001\n  registry_id: lm_eval_mistral_dense\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- id: plan_010\n  claim:\n  - 1\n  - 2\n  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions\n    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:\n    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization\n    beyond short training sequences.\n\n    '\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 2\n  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8\n    categories. All conditions. Tests instruction-following quality under sparsity.\n\n    '\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 3\n  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative\n    task types. Fine-grained capability diagnostics complementing LongBench.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_total_loss: 3.3438\n    final_kl_loss: 3.2969\n    final_reg_loss: 0.05\n    final_sparsity: 0\n    steps: 1000\n    tau_final: 0.1\n    wikitext2_ppl_dense: 6.12\n    wikitext2_ppl_sparse: 455.93\n    wikitext2_ppl_increase_pct: 7349\n    model_level_sparsity: 0.372\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\n- exp_id: mvp_kl_s123\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_kl_s456\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_bce_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 27.9603\n    teal_sparse_ppl: 44.537\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 628\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.3817\n    teal_sparse_ppl: 44.5864\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 629\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_bce_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 28.1437\n    teal_sparse_ppl: 43.033\n    model_level_sparsity: 0.4957\n    ppl_increase_vs_true_dense_pct: 603.3\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_lagrangian_quicktest\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_kl_loss: 418\n    final_constraint_loss: 1.211\n    final_sparsity: 0.141\n    final_lambda: 5.06\n    steps: 200\n    sparsity_trajectory:\n    - 0.406\n    - 0.387\n    - 0.289\n    - 0.168\n    - 0.141\n- exp_id: kl_lagrangian_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_normalized_quicktest\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    step1_kl: 1.18\n    step200_kl: 0.641\n    step200_sparsity: 0.504\n    final_lambda: 8\n    sparsity_converged_step: 80\n    sparsity_trajectory:\n    - 0.406\n    - 0.398\n    - 0.398\n    - 0.457\n    - 0.52\n    - 0.506\n    - 0.504\n    - 0.504\n    lambda_trajectory:\n    - 1\n    - 2\n    - 4\n    - 8\n    - 8\n    - 8\n    - 8\n    - 8\n- exp_id: mvp_kl_norm_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_kl_norm_s456\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_norm_v3_quicktest\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics:\n    step1_kl_raw: 1.1797\n    step1_kl_norm: 1.1797\n    step1_sparsity: 0.406\n    step1_lambda: 2\n    step50_kl_raw: 0.7344\n    step50_kl_norm: 0.7344\n    step50_sparsity: 0.514\n    step50_lambda: 1.95\n    step100_kl_raw: 0.625\n    step100_kl_norm: 0.625\n    step100_sparsity: 0.496\n    step100_lambda: 1000\n    step150_kl_raw: 0.5703\n    step150_kl_norm: 0.5703\n    step150_sparsity: 0.48\n    step150_lambda: 1000\n    step200_kl_raw: 0.6836\n    step200_kl_norm: 0.6836\n    step200_sparsity: 0.477\n    step200_lambda: 1000\n    step200_constraint: 0.01178\n    kl_trend: decreasing (1.18→0.57 min, uptick to 0.68 at end)\n    sparsity_range: 0.477-0.514 after step 50\n    checkpoint_path: /root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\n- exp_id: mvp_kl_norm_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2142\n    teal_sparse_ppl: 12.0776\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 97.4\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2474\n    teal_sparse_ppl: 11.9128\n    model_level_sparsity: 0.4979\n    ppl_increase_vs_true_dense_pct: 94.7\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: mvp_kl_norm_v2_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.14\n    teal_sparse_ppl: 13.58\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 121.9\n    eval_md5: f4086818bb55dc354ea4c6fe8ed8899a\n    calibration_samples: 32\n    vanilla_teal_sparse_ppl_INVALID: 66036.4062\n- exp_id: kl_only_s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.19\n    teal_sparse_ppl: 12.03\n    model_level_sparsity: 0.499\n    ppl_increase_vs_true_dense_pct: 96.57\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: kl_only_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 9.15\n    teal_sparse_ppl: 11.99\n    model_level_sparsity: 0.498\n    ppl_increase_vs_true_dense_pct: 96\n- exp_id: spon_training\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1193\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 9.0977\n    spon_recovery_pct: 3.8\n    ppl_improvement_from_spon: 0.1188\n    ppl_increase_vs_true_dense_pct: 48.7\n    ppl_increase_no_spon_vs_true_dense_pct: 50.6\n    mean_bias_norm: 0.040596\n    max_bias_norm: 0.054199\n    teal_sparse_ppl: 12.08\n    teal_with_spon_ppl: 11.93\n    spon_dense_ppl_degradation: 6.19\n    model_level_sparsity: 0.5\n    eval_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n- exp_id: spon_kl_s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: bce_comp_staged_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 25.44\n    predictor_hard_mask_ppl_no_comp: 27.96\n    teal_sparse_ppl: 44.54\n    model_level_sparsity: 0.558\n    ppl_increase_vs_true_dense_pct: 315.7\n    comp_loss_final: 0.0033\n    bce_loss_final: 0.6379\n    eval_seq_len: 2048\n    calibration_samples: 32\n- exp_id: training_free_baselines\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    vanilla_teal_global_ppl_30pct: 10.97\n    vanilla_teal_global_ppl_50pct: 23.31\n    vanilla_teal_global_ppl_70pct: 100.11\n    wina_global_ppl_30pct: 11.45\n    wina_global_ppl_50pct: 27.93\n    wina_global_ppl_70pct: 137.24\n    uniform_50pct_ppl: 23.9\n    teal_greedy_ppl: 33.47\n    vanilla_teal_global_ppl: 23.31\n    wina_global_ppl: 27.93\n    rsparse_global_ppl: 151.2\n- exp_id: spon_training_seq2048\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: ste_baseline_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 8.18\n    teal_sparse_ppl: 15.77\n    model_level_sparsity: 0.47\n    ppl_increase_vs_true_dense_pct: 157.7\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_dataset: wikitext-2\n    per_token_sparsity: 0.47\n    lambda_stats:\n      steps_70_130_mean: 66.4\n      steps_70_130_std: 94.87\n      first_500_mean: 688.07\n      first_500_std: 440.57\n      last_500_mean: 965.69\n      last_500_std: 141.59\n      overall_mean: 826.88\n      overall_std: 354.23\n- exp_id: spon_2048_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    true_dense_ppl: 6.1173\n    predictor_hard_mask_ppl: 9.2165\n    spon_sparse_ppl: 8.991\n    spon_recovery_pct: 7.3\n    ppl_improvement_from_spon: 0.2255\n    mean_bias_norm: 0.05312\n    max_bias_norm: 0.065918\n    model_level_sparsity: 0.498\n    eval_seq_len: 2048\n    training_seq_len: 2048\n    eval_samples: 141\n    trainable_params: 458752\n    trainable_pct: 0.0057\n    training_steps: 1000\n    final_loss: 0.377\n    dense_with_spon_ppl: 6.1823\n    dense_ppl_degradation: 0.0651\n    teal_sparse_no_spon_ppl: 12.0776\n    teal_sparse_with_spon_ppl: 11.7907\n    spon_recovery_teal_pct: 4.8\n    teal_sparsity: 0.4979\n- exp_id: ste_kl_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: training_free_wina_greedy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wina_greedy_ppl: 2126.03\n    dense_ppl: 6.12\n    model_level_sparsity: 0.5\n    eval_dataset: WikiText-2\n    eval_seq_len: 2048\n    greedy_allocation_summary: 'layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80,\n      layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24:\n      0.05-0.15, layers 25-31: 0.00'\n- exp_id: bce_isocompute_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: eval_spon_supp_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: spon_supp_eval_retry\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bce_isocompute_v2_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6637\n    final_bce_loss: 0.6586\n    final_reg_loss: 0.0051\n    final_sparsity: 0.502\n    training_steps: 1000\n    training_time_sec: 1047.8\n    reg_weight: 2\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 26.76\n    teal_sparse_ppl: 54.84\n    eval_seq_len: 2048\n    eval_dataset: wikitext-2\n- exp_id: plan_005_subsumption_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    linearity_ratio: 0.2644\n    linearity_ratio_std: 0.0073\n    magnitude_ratio: 0.1578\n    magnitude_ratio_std: 0.0088\n    cosine_similarity: 0.1962\n    cosine_similarity_std: 0.0268\n    predictor_effect_norm: 482.65\n    spon_correction_norm: 76.2\n    interaction_norm: 147.74\n    num_samples: 50\n    seq_len: 2048\n    conclusion_type: weak_subsumption\n- exp_id: kl_sparsity30_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity70_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: kl_sparsity30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    final_loss: 0.1465\n    kl_normalized: 0.1465\n    kl_raw: 0.1465\n    model_level_sparsity: 0.281\n    sparsity_target: 0.3\n    lambda_sparse_final: 1000\n    lambda_max_cap: 1000\n    tau_final: 0.1\n    constraint_loss_final: 0\n    training_steps: 1000\n    wall_clock_seconds: 2662.6\n    gpu_hours: 0.74\n    note: No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1).\n      Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run\n      was offline (not synced).\n- exp_id: kl_sparsity70_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 13.84\n    predictor_teal_sparse_ppl: 17.91\n    vanilla_teal_sparse_ppl: 100.11\n    teal_sparse_ppl: 17.91\n    teal_sparse_ppl_static_baseline: 17.91\n    model_level_sparsity: 0.7\n    teal_sparse_note: '17.91 = predictor-based TEAL (teal_global_masks: predictor-gated\n      magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py\n      L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct\n      metadata 有误导性.'\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    per_layer_sparsity_range:\n    - 0.508\n    - 0.876\n- exp_id: kl_sparsity30_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    loss: 0.165\n    kl_normalized: 0.165\n    kl_raw: 0.165\n    sparsity: 0.285\n    lambda_sparse: 5000\n    tau: 0.1\n    constraint_loss: 0\n    steps: 1000\n    true_dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    teal_sparse_ppl_note: 已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\n    model_level_sparsity: 0.3\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n- exp_id: mistral_kl_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_final_loss: 0.2188\n    train_final_kl_raw: 0.2188\n    train_final_kl_norm: 0.2188\n    train_final_constraint: 0\n    train_final_sparsity: 0.48\n    train_final_lambda: 1000\n    train_final_tau: 0.1\n    train_steps_completed: 1000\n    true_dense_ppl: 5.52\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    model_level_sparsity: 0.5\n    eval_dataset: wikitext-2\n    eval_seq_len: 2048\n    calibration_samples: 32\n    eval_samples: 159\n- exp_id: lm_eval_dense_test\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_kl_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc_norm: 0.3771\n    winogrande_acc: 0.6156\n    mmlu_acc: 0.2591\n    gsm8k_exact_match: 0.0121\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: kl_sparse_50pct\n    server: westd-34887\n    exit_code: 129\n    wall_time_sec: 3010\n    flag: SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\n- exp_id: lm_eval_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.5819\n    winogrande_acc: 0.7814\n    mmlu_acc: 0.6532\n    gsm8k_exact_match: 0.5004\n    eval_tasks:\n    - arc_challenge\n    - winogrande\n    - mmlu\n    - gsm8k\n    model: llama-3.1-8b\n    condition: dense\n    server: westd-34887\n- exp_id: lm_eval_mistral_downstream\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: lm_eval_mistral_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    arc_challenge_acc_norm: 0.6024\n    winogrande_acc: 0.7869\n    mmlu_acc: 0.6244\n    gsm8k_exact_match: 0.3654\n    model: Mistral-7B-v0.3\n    condition: dense\n    server: westd-34887\n- exp_id: diag_30pct_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_gsm8k_gencomp\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: diag_teal_downstream\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: lm_eval_kl_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.3575\n    arc_challenge_acc_norm: 0.3737\n    winogrande_acc: 0.6756\n    mmlu_acc: 0.2874\n    gsm8k_exact_match_strict: 0.0743\n    gsm8k_exact_match_flexible: 0.0781\n    actual_sparsity: 0.3\n    model: llama-3.1-8b\n    condition: kl_distill_30pct_sparsity_s42\n    mmlu_stem_acc: 0.2499\n    mmlu_social_sciences_acc: 0.2896\n    mmlu_humanities_acc: 0.2786\n    mmlu_other_acc: 0.3363\n- exp_id: gsm8k_gen_compare\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: lm_eval_teal_50pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: vanilla_teal\n    sparsity: 0.5\n    actual_sparsity: 0.5\n    arc_challenge_acc_norm: 0.291\n    winogrande_acc: 0.5556\n    mmlu_acc: 0.2856\n    gsm8k_exact_match_flexible: 0.019\n    gsm8k_exact_match_strict: 0.0114\n    arc_challenge_drop_vs_dense: -0.5\n    winogrande_drop_vs_dense: -0.289\n    mmlu_drop_vs_dense: -0.563\n    gsm8k_drop_vs_dense: -0.962\n    model: Llama-3.1-8B\n    condition: TEAL 50% training-free sparsity\n- exp_id: lm_eval_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge:\n      acc: 0.3933\n      acc_norm: 0.4155\n      acc_stderr: 0.0143\n      acc_norm_stderr: 0.0144\n    winogrande:\n      acc: 0.6559\n      acc_stderr: 0.0134\n    mmlu:\n      acc: 0.3598\n      acc_stderr: 0.004\n    mmlu_stem:\n      acc: 0.313\n    mmlu_humanities:\n      acc: 0.3305\n    mmlu_social_sciences:\n      acc: 0.4108\n    mmlu_other:\n      acc: 0.401\n    gsm8k:\n      exact_match_strict: 0.0849\n      exact_match_flexible: 0.0925\n      strict_stderr: 0.0077\n      flexible_stderr: 0.008\n    actual_sparsity: 0.3\n- exp_id: lm_eval_mistral_kl_50pct\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    arc_challenge_acc: 0.2927\n    arc_challenge_acc_norm: 0.3183\n    arc_challenge_acc_norm_stderr: 0.0136\n    winogrande_acc: 0.629\n    winogrande_acc_stderr: 0.0136\n    mmlu_acc: 0.2295\n    mmlu_acc_stderr: 0.0035\n    mmlu_stem_acc: 0.2125\n    mmlu_humanities_acc: 0.2421\n    mmlu_social_sciences_acc: 0.2171\n    mmlu_other_acc: 0.2398\n    gsm8k_exact_match_strict: 0.0045\n    gsm8k_exact_match_flexible: 0.0212\n    model: Mistral-7B-v0.3\n    condition: kl_distill_50pct_sparsity_s42\n    arc_challenge_retention_vs_dense: 0.528\n    winogrande_retention_vs_dense: 0.799\n    mmlu_retention_vs_dense: 0.368\n    gsm8k_retention_vs_dense: 0.012\n- exp_id: d030_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n    allocation: uniform\n    per_layer_sparsity: uniform 0.301 across all 32 layers\n    mmlu_improvement_vs_global: +11.87pp (0.2874 → 0.4061)\n    gsm8k_change_vs_global: no change (0.0743 → 0.0735, within noise)\n- exp_id: bce_isocompute_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    steps: 2700\n    loss: 0.6382\n    bce_loss: 0.6371\n    reg_loss: 0.001\n    sparsity: 0.51\n    training_time_seconds: 2828\n    note: 'BCE saturation confirmed: step 500→2700 only 0.006 improvement'\n- exp_id: bench_mistral_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: d030_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.96\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n    allocation: uniform\n    per_layer_sparsity: uniform 0.500 across all 32 layers\n    mmlu_change_vs_global: +1.86pp (0.2591 → 0.2777, not significant)\n    gsm8k_change_vs_global: +0.91pp (0.0121 → 0.0212, not significant)\n    conclusion_note: 50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在\n      50% sparsity 下消失。\n- exp_id: bench_dense\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.1173\n    arc_challenge_acc: 0.5478\n    arc_challenge_acc_norm: 0.5828\n    winogrande_acc: 0.7806\n    mmlu_acc: 0.6527\n    gsm8k_exact_match: 0.4875\n- exp_id: eval_kl30_teal_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 7.3\n    teal_sparse_ppl: 8.98\n    sparsity_target: 0.3\n    actual_sparsity: 0.3\n- exp_id: d030_kl40_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3627\n    arc_challenge_acc_norm: 0.4181\n    winogrande_acc: 0.6717\n    mmlu_acc: 0.3068\n    gsm8k_exact_match: 0.0394\n    actual_sparsity: 0.398\n- exp_id: eval_bce_v3_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 6.12\n    predictor_hard_mask_ppl: 22.51\n    teal_sparse_ppl: 27.97\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2048\n    arc_challenge_acc_norm: 0.2398\n    arc_challenge_acc_norm_stderr: 0.0125\n    winogrande_acc: 0.5059\n    winogrande_acc_stderr: 0.0141\n    mmlu_acc: 0.3002\n    mmlu_acc_stderr: 0.0038\n    gsm8k_exact_match: 0.0485\n    gsm8k_exact_match_strict: 0.0425\n    gsm8k_exact_match_stderr: 0.0059\n- exp_id: bench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8157\n    arc_challenge_acc_norm: 0.4078\n    winogrande_acc: 0.6859\n    mmlu_acc: 0.4061\n    gsm8k_exact_match: 0.0735\n    actual_sparsity: 0.3\n- exp_id: bench_kl50_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n    actual_sparsity: 0.5\n- exp_id: bench_kl30_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    arc_challenge_acc_norm: 0.3968\n    winogrande_acc: 0.7017\n    mmlu_acc: 0.2527\n    gsm8k_exact_match: 0.0879\n    actual_sparsity: 0.3\n- exp_id: bench_teal30\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.97\n    arc_challenge_acc_norm: 0.4232\n    winogrande_acc: 0.6606\n    mmlu_acc: 0.3861\n    gsm8k_exact_match: 0.0788\n    actual_sparsity: 0.3\n- exp_id: bench_teal50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 23.31\n    arc_challenge_acc_norm: 0.2841\n    winogrande_acc: 0.5304\n    mmlu_acc: 0.2832\n    gsm8k_exact_match: 0.0197\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.963\n    arc_challenge_acc_norm: 0.3276\n    winogrande_acc: 0.629\n    mmlu_acc: 0.2777\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: bench_kl40_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 10.117\n    arc_challenge_acc_norm: 0.4096\n    winogrande_acc: 0.6535\n    mmlu_acc: 0.3806\n    gsm8k_exact_match: 0.05\n    actual_sparsity: 0.4\n- exp_id: longbench_kl30_uniform\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_kl30_uniform_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: longbench_dense_v5\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: latency_benchmark\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpu_model: NVIDIA RTX PRO 6000 Blackwell Server Edition\n    dtype: float16\n    attn: flash_attention_2\n    batch: 1\n    seq_len: 2048\n    warmup: 10\n    iters: 100\n    dense_ms: 119.11\n    dense_std: 0.57\n    dense_tokens_per_s: 17194.5\n    kl_30pct_ms: 126.64\n    kl_30pct_std: 0.7\n    kl_30pct_tokens_per_s: 16171.8\n    kl_30pct_speedup: 0.941\n    kl_50pct_ms: 126.78\n    kl_50pct_std: 0.31\n    kl_50pct_tokens_per_s: 16154.2\n    kl_50pct_speedup: 0.939\n    comp_30pct_ms: 129.94\n    comp_30pct_std: 0.75\n    comp_30pct_tokens_per_s: 15761.4\n    comp_30pct_speedup: 0.917\n    comp_50pct_ms: 129.71\n    comp_50pct_std: 0.53\n    comp_50pct_tokens_per_s: 15788.8\n    comp_50pct_speedup: 0.918\n    predictor_overhead_ms: 3.17\n    predictor_overhead_pct: 2.7\n    per_layer_predictor_ms: 0.099\n    dense_ffn_per_layer_ms: 2.427\n    sparse_ffn_pred_per_layer_ms: 2.686\n    compensation_overhead_ms: 3.3\n- exp_id: bench_kl50_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.83\n    arc_challenge_acc_norm: 0.3515\n    winogrande_acc: 0.6298\n    mmlu_acc: 0.2751\n    gsm8k_exact_match: 0.0235\n    actual_sparsity: 0.5\n- exp_id: bench_kl50_uniform_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9604\n    arc_challenge_acc_norm: 0.3345\n    winogrande_acc: 0.6275\n    mmlu_acc: 0.2874\n    gsm8k_exact_match: 0.0212\n    actual_sparsity: 0.5\n- exp_id: longbench_dense_v6\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    longbench_narrativeqa: 7.3\n    longbench_qasper: 13.4\n    longbench_gov_report: 30.5\n    longbench_multi_news: 2.5\n- exp_id: longbench_kl30_uniform_v6\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    longbench_narrativeqa: 4.12\n    longbench_qasper: 6.23\n    longbench_gov_report: 16.97\n    longbench_multi_news: 18.01\n    runtime_seconds: 6156.6\n- exp_id: eval_c4_ood_kl50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 9.2075\n    kl_50_global_ppl: 18.401\n    teal_50_ppl: 38.7503\n    kl_vs_dense_ratio: 2\n    teal_vs_dense_ratio: 4.21\n- exp_id: db_sensitivity_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    db64_per_token_ppl: 10.158\n    db64_teal_global_ppl: 12.076\n    db64_sparsity: 0.5\n    db64_loss: 0.361\n    db128_teal_global_ppl: 11.963\n    db128_per_token_ppl: 9.218\n    db256_per_token_ppl: 8.586\n    db256_teal_global_ppl: 12.105\n    db256_sparsity: 0.5\n    db256_loss: 0.27\n    db512_per_token_ppl: 7.933\n    db512_teal_global_ppl: 12.315\n    db512_sparsity: 0.5\n    db512_loss: 0.224\n    best_teal_global_db: 128\n    best_teal_global_ppl: 11.963\n- exp_id: bce_gumbel_lagrangian_isolation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lr_1e4_ppl: 42.99\n    lr_1e3_ppl: 48.4\n    lr_3e3_ppl: 38.02\n    lr_1e4_bce_loss: 0.7158\n    lr_1e3_bce_loss: 0.6781\n    lr_3e3_bce_loss: 0.6632\n    lr_1e4_sparsity: 0.514\n    lr_1e3_sparsity: 0.506\n    lr_3e3_sparsity: 0.504\n    best_ppl: 38.02\n    best_lr: 3e-3\n    kl_baseline_ppl: 11.79\n    gap_vs_kl: 26.23\n- exp_id: steps_curve_s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: steps_curve_s42_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: tau_schedule_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    tau_linear_baseline_ppl: 11.963\n    tau_fixed05_ppl: 11.861\n    tau_fixed01_ppl: 12.072\n    tau_fixed05_loss: 0.248\n    tau_fixed01_loss: 0.43\n    best_tau: fixed_0.5\n    ppl_range: 0.211\n- exp_id: steps_curve_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    step200_ppl: 15.158\n    step400_ppl: 12.538\n    step600_ppl: 12.046\n    step800_ppl: 11.907\n    step1000_ppl: 11.906\n    convergence_step: 800\n    ppl_800_vs_1000_delta: 0.001\n- exp_id: mistral_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 6.048\n    kl_teal_global_ppl: 6.7733\n    teal_baseline_ppl: 8.3807\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 1.386\n    ppl_vs_dense_pct: 9.5\n- exp_id: mistral_kl70_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_per_token_ppl: 9.1086\n    kl_teal_global_ppl: 13.3254\n    teal_baseline_ppl: 61.716\n    dense_ppl: 5.5238\n    kl_advantage_ratio: 6.77\n    final_loss: 0.3945\n    actual_sparsity: 0.682\n- exp_id: mistral_teal50_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_baseline_ppl: 18.3061\n    dense_ppl: 5.5238\n    teal_vs_dense_ratio: 3.31\n- exp_id: bench_kl70_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 17.91\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: kl_sparsity70_s42_v2 (teal_global_masks protocol)\n    vanilla_teal_ppl: 100.11\n- exp_id: bench_teal70\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 100.11\n    dense_ppl: 6.12\n    actual_sparsity: 0.7\n    source: training_free_baselines experiment (vanilla teal global)\n- exp_id: gradient_snr_kl_vs_bce\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 5.77e-05\n    bce_avg_snr: 1.0e-05\n    snr_ratio: 5.76\n    early_layer_ratio_range: 34-156x\n    late_layer_ratio_range: 2-4x\n- exp_id: natural_sparsity_floor_30pct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    always_pruned_ratio: 0.0006\n    always_pruned_count: 278\n    total_neurons: 458752\n    late_layer_max_ratio: 0.0051\n    threshold: 0.1\n- exp_id: teal_kl_overlap_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_jaccard: 0.396\n    divergence_ratio: 0.433\n    kl_only_pruned_magnitude_ratio: 1.48\n    teal_only_pruned_mean_gate_prob: 0.614\n    min_jaccard_layer: L17-L18 (0.19)\n    max_jaccard_layer: L26-L28 (0.55)\n- exp_id: gradient_snr_constrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_avg_snr: 0.000545\n    bce_avg_snr: 5.28e-06\n    snr_ratio: 103.2\n    kl_final_sparsity: 0.508\n    bce_final_sparsity: 0.591\n    steps: 200\n- exp_id: sparsity_floor_extended\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    floor_30pct: 0.0499\n    floor_50pct: 0.0726\n    floor_70pct: 0.1936\n    late_layer_max_30: 0.4604\n    late_layer_max_50: 1.2347\n    late_layer_max_70: 4.3666\n    threshold: 0.1\n    seq_len: 2048\n    num_samples: 50\n- exp_id: teal_kl_overlap_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    z_score: 7260.3\n    p_value: 0\n    median_percentile_rank: 78.6\n    iqr_q1: 64.4\n    iqr_q3: 89.1\n    layers_significant: 31/32\n    exception_layer: 31\n- exp_id: mag_preservation_reg\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: reverse_kl_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.8\n    vs_forward_kl: +1.01 (+8.6%)\n    sparsity: 0.5\n- exp_id: jsd_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ppl_wikitext2: 12.54\n    vs_forward_kl: +0.75 (+6.4%)\n    sparsity: 0.5\n- exp_id: global_30pct_retention\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    early_retention: 0.771\n    middle_retention: 0.764\n    knowledge_L12_20_retention: 0.797\n    late_L24_31_retention: 0.501\n    L31_retention: 0.284\n    L30_retention: 0.366\n    starved_layers: L27-L31\n- exp_id: kl_bce_f1_oracle\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bce_f1: 0.6128\n    bce_precision: 0.6132\n    bce_recall: 0.6124\n    kl_f1: 0.5397\n    kl_precision: 0.5112\n    kl_recall: 0.5715\n    random_f1: 0.5\n    kl_ppl: 11.79\n    bce_ppl: 22.51\n- exp_id: kl50_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.745\n    arc_challenge: 0.3814\n    winogrande: 0.6125\n    mmlu: 0.2752\n    gsm8k: 0.0281\n- exp_id: kl30_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8308\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.6938\n    mmlu_acc: 0.3944\n    gsm8k_exact_match: 0.0751\n    actual_sparsity: 0.3\n    allocation: uniform\n- exp_id: kl50_s456_train_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl50_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.397\n    final_kl_normalized: 0.397\n    final_sparsity: 0.492\n    final_lambda: 5000\n    final_tau: 0.1\n    steps_completed: 1000\n- exp_id: kl_50pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.745\n    arc_challenge_acc_norm: 0.3814\n    winogrande_acc: 0.6125\n    mmlu_acc: 0.2752\n    gsm8k_exact_match: 0.0281\n    sparsity: 0.5\n    allocation: global\n- exp_id: mistral_dense_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 5.5238\n    model: Mistral-7B-v0.3\n    condition: dense\n    sparsity: 0\n- exp_id: mistral_kl30_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.048\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 0.5242\n- exp_id: mistral_kl50_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.2931\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 1.7693\n- exp_id: mistral_kl70_pertoken\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 9.1086\n    model: Mistral-7B-v0.3\n    condition: kl_pertoken_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 3.5848\n- exp_id: mistral_kl30_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 6.7733\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 1.2495\n- exp_id: mistral_kl50_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.6489\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_50pct\n    sparsity: 0.5\n    allocation: uniform\n    ppl_increase_vs_dense: 3.1251\n- exp_id: mistral_kl70_teal_global\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 13.3254\n    model: Mistral-7B-v0.3\n    condition: kl_teal_global_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 7.8016\n- exp_id: mistral_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.3807\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_30pct\n    sparsity: 0.3\n    allocation: uniform\n    ppl_increase_vs_dense: 2.8569\n- exp_id: mistral_teal70_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 61.716\n    model: Mistral-7B-v0.3\n    condition: teal_vanilla_70pct\n    sparsity: 0.7\n    allocation: uniform\n    ppl_increase_vs_dense: 56.1922\n- exp_id: kl30_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.2021\n    actual_sparsity: 0.289\n    constraint_satisfied: true\n    training_steps: 1000\n- exp_id: kl_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9748\n    arc_challenge_acc_norm: 0.4531\n    winogrande_acc: 0.693\n    mmlu_acc: 0.3807\n    gsm8k_exact_match: 0.0758\n    sparsity: 0.3\n    allocation: global\n- exp_id: kl50_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 11.8057\n    arc_challenge: 0.3319\n    winogrande: 0.6488\n    mmlu: 0.2794\n    gsm8k: 0.0212\n- exp_id: kl30_s456_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl_wikitext2: 8.9332\n    arc_challenge: 0.4633\n    winogrande: 0.7111\n    mmlu: 0.4382\n    gsm8k: 0.0758\n- exp_id: kl30_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu: 0.4198\n    ppl_uniform: 8.7947\n    arc_challenge: 0.4505\n    winogrande: 0.6875\n    gsm8k: 0.0758\n- exp_id: qwen14b_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 6.8\n    teal_global_ppl: 7.62\n    ppl_ratio_hard_mask: 1.31\n    ppl_ratio_teal: 1.47\n    final_loss: 0.3398\n    training_sparsity: 0.281\n    teal_sparsity: 0.3\n    lambda: 5000\n    steps: 1000\n- exp_id: qwen14b_kl30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 7.6232\n    arc_challenge_acc_norm: 0.5717\n    winogrande_acc: 0.7206\n    mmlu_acc: 0.6372\n    gsm8k_exact_match: 0.4882\n- exp_id: downstream_extended_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.727\n    hellaswag_acc: 0.527\n    piqa_acc_norm: 0.7595\n    piqa_acc: 0.747\n    boolq_acc: 0.7685\n- exp_id: wallclock_speedup_30_50\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    theoretical_flops_speedup_30pct: 1.36\n    theoretical_flops_speedup_50pct: 2.45\n    actual_wallclock_speedup_30pct: 0.91\n    actual_wallclock_speedup_50pct: 0.6\n    predictor_overhead_decode_ms: 1\n    predictor_overhead_prefill_ms: 2\n    actual_mean_sparsity_30pct: 0.28\n    actual_mean_sparsity_50pct: 0.605\n    note: No wall-clock speedup without sparse kernels. Mask-based=0.87-0.94x (predictor\n      overhead), structured-skip=0.45-0.74x (gather overhead). Report theoretical\n      FLOPs in paper.\n- exp_id: qwen14b_bce30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    dense_ppl: 5.18\n    predictor_hard_mask_ppl: 5.57\n    teal_global_ppl: 8.76\n    ppl_ratio_hard_mask: 1.075\n    ppl_ratio_hard_mask_note: at predictor native 6.4% sparsity, not comparable to\n      KL's 28.1%\n    ppl_ratio_teal: 1.69\n    actual_sparsity_teal: 0.3\n    predictor_native_sparsity: 0.064\n    training_log_sparsity_note: Training Lagrangian failed (predictor sparsity=6.4%).\n      Inference via TEAL forces 30% externally. TEAL PPL 8.76 is valid for method\n      comparison.\n    final_loss: 0.5561\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n- exp_id: qwen14b_teal30_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.7332\n    arc_challenge_acc_norm: 0.5683\n    winogrande_acc: 0.7269\n    mmlu_acc: 0.7183\n    gsm8k_exact_match: 0.4951\n- exp_id: qwen14b_bce30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    predictor_native_sparsity: 0.064\n    lambda_max: 50000\n    final_bce_loss: 0.5324\n    steps: 1000\n    constraint_satisfied: false\n    sparsity_trajectory: 49%→5% collapse in 50 steps, no recovery over 950 steps\n    note: 10x stronger Lagrangian produces identical sparsity as v1 (lambda=5000).\n      Confirms BCE gradient insufficiency is fundamental, not constraint strength.\n- exp_id: downstream_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc_norm: 0.8233\n    hellaswag_acc_norm_stderr: 0.0038\n    piqa_acc_norm: 0.8074\n    piqa_acc_norm_stderr: 0.0092\n    boolq_acc: 0.8294\n    boolq_acc_stderr: 0.0066\n- exp_id: qwen14b_bce30_s42_eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 8.7634\n    arc_challenge_acc_norm: 0.5759\n    winogrande_acc: 0.7261\n    mmlu_acc: 0.7167\n    gsm8k_exact_match: 0.5307\n- exp_id: downstream_teal30_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    hellaswag_acc: 0.4878\n    hellaswag_acc_norm: 0.667\n    piqa_acc: 0.7258\n    piqa_acc_norm: 0.7361\n    boolq_acc: 0.685\n- exp_id: kl50_global_s123_reeval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7184\n    arc_challenge_acc_norm: 0.3635\n    winogrande_acc: 0.6109\n    mmlu_acc: 0.2834\n    gsm8k_exact_match: 0.0258\n- exp_id: bce_isocompute_v3_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: bce_isocompute_v3_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6368\n    final_sparsity: 0.51\n    training_steps: 2700\n- exp_id: c4_ood_kl30_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0458\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_download\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: qwen14b_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ppl: 5.1854\n    arc_challenge: 0.6758\n    winogrande: 0.8106\n    mmlu: 0.7977\n    gsm8k: 0.8757\n- exp_id: bce_isocompute_v3_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    teal_sparse_ppl: 28.3503\n    model_level_sparsity: 0.5\n    arc_challenge_acc: 0.2312\n    arc_challenge_acc_stderr: 0.01232\n    arc_challenge_acc_norm: 0.2807\n    arc_challenge_acc_norm_stderr: 0.01313\n    winogrande_acc: 0.5241\n    winogrande_acc_stderr: 0.01404\n    mmlu_acc: 0.2567\n    mmlu_acc_stderr: 0.00367\n    gsm8k_exact_match: 0.022\n    gsm8k_exact_match_stderr: 0.00404\n    gsm8k_exact_match_strict: 0.00834\n    gsm8k_exact_match_strict_stderr: 0.0025\n- exp_id: bce_isocompute_v3_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 28.0627\n    arc_challenge_acc_norm: 0.2696\n    winogrande_acc: 0.513\n    mmlu_acc: 0.2655\n    gsm8k_exact_match: 0.022\n- exp_id: qwen14b_kl30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: qwen14b_teal30_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl30_8b_s123_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    sparsity: 0.3\n    training_loss: 0.147\n- exp_id: kl30_8b_s456_train\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    sparsity: 0.3\n    training_loss: 0.148\n- exp_id: qwen14b_kl30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    wikitext2_ppl: 7.63\n    mmlu_acc: 0.6449\n    arc_challenge_acc_norm: 0.5444\n    winogrande_acc: 0.7245\n- exp_id: qwen14b_teal30_uniform_eval_4task\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.01\n    mmlu_acc: 0.6634\n    arc_challenge_acc_norm: 0.5529\n    winogrande_acc: 0.6985\n- exp_id: bce_isocompute_v3_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 27.9696\n    arc_challenge_acc: 0.2346\n    arc_challenge_acc_norm: 0.2765\n    winogrande_acc: 0.5162\n    mmlu_acc: 0.2614\n    gsm8k_exact_match: 0.019\n- exp_id: kl30_8b_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9267\n    arc_challenge_acc: 0.4462\n    arc_challenge_acc_norm: 0.4744\n    winogrande_acc: 0.7024\n    mmlu_acc: 0.3836\n    gsm8k_exact_match: 0.0917\n- exp_id: kl30_8b_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc: 0.436\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: snr_extended_r6w3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kl_snr_step300: 0.0058773\n    bce_snr_step300: 0.00114449\n    snr_ratio_step300: 5.14\n    kl_train_time_s: 641\n    bce_train_time_s: 320\n    num_checkpoints: 7\n    steps_range: 0-300\n- exp_id: c4_ood_kl30_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_dense_baseline\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: kl50_s123_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.89\n    arc_challenge_acc_norm: 37.88\n    winogrande_acc: 62.19\n    mmlu_acc: 27.75\n    gsm8k_exact_match: 2.35\n    comparison_vs_global_topk:\n      ppl_delta: -0.94\n      arc_c_delta: -5.55\n      wg_delta: -6.71\n      mmlu_delta: -8.2\n      gsm8k_delta: -5\n    note: 'Uniform allocation: better PPL but catastrophic downstream degradation\n      vs global_topk. Confirms global_topk allocation is critical for downstream quality.'\n- exp_id: c4_ood_kl30_s123_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0259\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: c4_ood_dense_baseline_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 9.2075\n    model: llama-3.1-8b\n    eval_sequences: 132\n    seq_len: 2048\n- exp_id: kl50_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8614\n    arc_challenge_acc_norm: 0.3754\n    winogrande_acc: 0.6417\n    mmlu_acc: 0.2784\n    gsm8k_exact_match: 0.0212\n- exp_id: c4_ood_kl50_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.6064\n    allocation: global_topk\n    sparsity: 0.5\n    model: llama-3.1-8b\n- exp_id: downstream_ext_kl50_uniform_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: downstream_ext_kl30_uniform_s123\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c4_ood_kl50_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.9867\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 456\n- exp_id: c4_ood_kl30_s42_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 16.0401\n    allocation: global_topk\n    sparsity: 0.3\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl50_s42_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9638\n    arc_challenge_acc_norm: 0.3259\n    winogrande_acc: 0.6235\n    mmlu_acc: 0.2792\n    gsm8k_exact_match: 0.0197\n- exp_id: c4_ood_kl50_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    c4_ppl: 23.5297\n    sparsity: 0.5\n    allocation: global_topk\n    seed: 42\n- exp_id: kl_comp_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.6992\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.3594\n    - 1.3516\n    - 1.0859\n    - 0.9219\n    - 0.8789\n    - 0.8281\n    - 0.7461\n    - 0.7344\n    - 0.6953\n    - 0.6992\n- exp_id: c4_ood_kl30_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.7617\n    steps: 1000\n    compensation_params: 67248128\n    compensation_pct: 0.837\n    mean_head_norm_final: 9.2012\n    loss_trajectory:\n    - 2.0469\n    - 1.3828\n    - 1.0703\n    - 0.9609\n    - 0.8711\n    - 0.7305\n    - 0.6875\n    - 0.7773\n    - 0.7969\n    - 0.7617\n- exp_id: kl_comp_30pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl_comp_30pct_s42_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 42\n- exp_id: kl_comp_30pct_s123_ppl\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9768\n    c4_ppl: 16.0401\n    sparsity: 0.3\n    allocation: global_topk\n    model: llama-3.1-8b\n    seed: 123\n- exp_id: kl_comp_30pct_s123_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9788\n    arc_challenge_acc_norm: 0.3993\n    winogrande_acc: 0.6898\n    mmlu_acc: 0.2531\n    gsm8k_exact_match: 0.0842\n- exp_id: kl50_s456_uniform_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.9538\n    arc_challenge_acc_norm: 0.3831\n    winogrande_acc: 0.6196\n    mmlu_acc: 0.275\n    gsm8k_exact_match: 0.0288\n- exp_id: kl_comp_30pct_s456\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_50pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_comp_30pct_s456_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.9614\n    arc_challenge_acc_norm: 0.4462\n    winogrande_acc: 0.7143\n    mmlu_acc: 0.2714\n    gsm8k_exact_match: 0.0887\n- exp_id: kl_comp_50pct_s42_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.7933\n    arc_challenge_acc_norm: 0.3285\n    winogrande_acc: 0.6346\n    mmlu_acc: 0.2789\n    gsm8k_exact_match: 0.0129\n- exp_id: kl50_s42_global_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 11.8038\n    arc_challenge_acc_norm: 0.3336\n    winogrande_acc: 0.6338\n    mmlu_acc: 0.2819\n    gsm8k_exact_match: 0.0167\n- exp_id: kl30_s123_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8186\n    arc_challenge_acc_norm: 0.471\n    winogrande_acc: 0.6961\n    mmlu_acc: 0.3763\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s456_uniform_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wikitext2_ppl: 8.8284\n    arc_challenge_acc_norm: 0.4505\n    winogrande_acc: 0.6953\n    mmlu_acc: 0.3727\n    gsm8k_exact_match: 0.0705\n- exp_id: kl30_s123_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: kl30_s456_uniform_v3\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: c1_ablation_bce_kl_targets_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    wt2_ppl: 9.29\n    eval_sparsity: 0.609\n    oracle_agreement: 0.978\n    final_bce_loss: 0.0545\n    train_steps: 1000\n    train_time_sec: 877.1\n    reference_kl_ppl: 11.79\n    reference_bce_ppl: 22.51\n- exp_id: bce_30pct_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: kl_sparsity25_s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_final: 0.1582\n    kl_normalized_final: 0.1582\n    sparsity_actual: 0.23\n    sparsity_target: 0.25\n    lambda_final: 5000\n    tau_final: 0.1\n    steps: 1000\n- exp_id: kl_sparsity35_s42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: c1_ablation_eval_uniform\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity45_s42\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: bce_30pct_s42_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity25_s123\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity25_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity35_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: kl_sparsity45_s42_eval_teal\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: c1_ablation_bce_kl_targets\n  claim: 'Claim 1: mask pattern discovery'\n  description: BCE trained on KL-derived oracle masks achieves PPL 11.9638 = KL PPL\n    11.9638 at 50% sparsity under identical TEAL protocol. 53% mask divergence from\n    magnitude oracles. Target quality is sole driver of KL advantage.\n  estimated_gpu_hours: 0.0\n- name: dense_sparsity_sweep_6pt\n  claim: 'Claim 3: regime analysis with 6 data points'\n  description: KL predictors at 25%/30%/35%/40%/45%/50% with regime boundaries precisely\n    mapped.\n  estimated_gpu_hours: 0.0\n- name: bce_30pct_forced_topk\n  claim: 'Claim 1: BCE baseline at recommended operating point'\n  description: BCE predictor evaluated at 30% via forced TEAL top-k. Fills Table 2\n    gap.\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T17:17:34.185Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T17:17:34.185Z",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4"
}
```

---

## Round 1

15 recorded events

### User

_source line 3 · 2026-05-18T17:17:34.238Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：C1 ablation 在 controlled protocol 下出现显著 gap，'target quality = sole driver' 被 falsify；regime 结构不清晰
核心假设：['C1 uniform eval gap > 0.5 PPL（gradient coupling 贡献不可忽略，possibly 20-40% of gap）', '6-point sweep 无清晰 kink point，MMLU/PPL 行为不一致导致 regime 叙事牵强', 'BCE 30% forced TEAL PPL 9.0–10.0（BCE 在推荐工作点接近 KL，削弱核心 claim）', '审稿人判定为 incremental composition of known techniques', '14B + no wall-clock speedup + downstream gap 三重 weakness 使 practical impact 存疑']
关键指标范围：{'c1_ppl_gap_50pct_uniform': [0.5, 2.0], 'bce_30pct_teal_ppl': [9.0, 10.0], 'regime_piecewise_R2': [0.7, 0.85], 'kl30_uniform_mmlu_3seed_mean': [0.35, 0.38], 'kl30_uniform_mmlu_3seed_std': [0.02, 0.04], 'expected_reviewer_avg': [3.0, 3.5], 'accept_probability': [0.05, 0.2]}
叙事方向：核心 reframe：放弃 'mask pattern discovery' 作为 headline，转向 'A Systematic Framework for Understanding Loss-Sparsity Interactions in SwiGLU Pruning'。2D taxonomy（correction granularity × training signal coupling）升级为主要贡献。C1 ablation 重新诠释为 'quantifying the relative contribution of target quality vs gradient coupling'（partial result 仍有价值）。Claim 3 从 phase transition 降为 practitioner guidelines（'when to use uniform vs learned allocation'）。Paper 定位从 discovery → systematization + empirical study。仍冲 EMNLP Main（Efficient Methods track 对 systematic empirical work 有容纳空间），但叙事重心从 'we found something new' 转为 'we provide the first controlled decomposition of what matters for learned sparsity prediction'。

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

1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 to PPL. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). Standard BCE (magnitude masks) PPL ≈ 22.51. The gradient coupling contribution is zero; target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from "engineering a better loss" to "discovering that output-distribution distillation reveals hidden neuron importance structure." **Supporting evidence**: (a) Iso-compute ablation: BCE with 2.71× more FLOPs still PPL=27.97 vs KL=12.00, confirming the gap is structural; (b) BCE Lagrangian failure at 30%: BCE loss scale (~0.6) vs KL (~0.0001) causes same Lagrangian to fail; (c) No compensation needed: KL eliminates 67.2M compensation parameters (~256MB). **Anticipated attack**: "Two-stage training (KL→oracle→BCE) avoids needing KL predictor at inference?" Defense: KL predictor is contextual (per-input adaptive); oracle masks are fixed. Deployment requires per-input sparsity adaptation. (Headline claim, resolves persistent R3-R8 confound)

2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL "subsuming" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)

3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports "PPL is a poor proxy for downstream quality" narrative. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)

## Story Spine

- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).

- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.

- **Our framing / headline question**: "What does KL distillation actually learn for SwiGLU sparsity prediction, and why do its masks differ fundamentally from magnitude-based oracles?" The theoretical grounding (§3.6, suggestive): BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm. This provides intuition for how KL *can* discover joint interaction patterns. The C1 causal ablation (§4.4) then empirically confirms: the masks KL discovers, not the gradient pathway itself, are what matter.

- **Headline result template**: "KL-trained sparsity predictors discover neuron importance patterns that diverge 53% from magnitude-based masks. A causal ablation confirms that these mask patterns, not gradient coupling, drive KL's quality advantage: BCE trained on KL-derived masks matches KL performance (PPL 9.29 vs 9.21 at ~60% sparsity). This finding eliminates the need for 67.2M compensation parameters and reveals three sparsity operating regimes with qualitatively different allocation requirements."

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
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: c1_ablation_eval_uniform
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity45_s42
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: bce_30pct_s42_eval
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: kl_sparsity25_s123
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
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
  "promptId": "3915ffa9-3522-4fd9-aef9-082c7cd8e50b",
  "type": "user",
  "uuid": "1f9fb45d-7179-4eca-82df-b07dd29e8706",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T17:17:34.235Z_

```json
{
  "parentUuid": "1f9fb45d-7179-4eca-82df-b07dd29e8706",
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
  "uuid": "38bfe6c3-bcff-44ce-825a-0080fe6d2cc6",
  "timestamp": "2026-05-18T17:17:34.235Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T17:17:34.235Z_

```json
{
  "parentUuid": "38bfe6c3-bcff-44ce-825a-0080fe6d2cc6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e6169071-b86b-4f56-857c-455c0e1839d2",
  "timestamp": "2026-05-18T17:17:34.235Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1 ablation 在 controlled protocol 下出现显著 gap，'target quality = sole driver' 被 falsify；regime 结构不清晰 核心假设：['C1 uniform eval gap > 0.5 PPL（gradient coupling 贡…",
  "leafUuid": "e6169071-b86b-4f56-857c-455c0e1839d2",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Understanding KL-discovered sparsity patterns via systematic ablation and regime analysis",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4"
}
```

---

### Assistant

_source line 8 · 2026-05-18T17:17:37.423Z_

I'll review the experiment plan and registry data to generate detailed worst-tier predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6169071-b86b-4f56-857c-455c0e1839d2",
  "isSidechain": false,
  "requestId": "req_011CbAQzddCNHkYEA9WPbW4D",
  "type": "assistant",
  "uuid": "4967950f-3048-42e4-b5ae-2bb179874a46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SeHN8AJnpojXv1JrS2tKTS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34980,
      "cache_read_input_tokens": 11841,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 108,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34980
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

_source line 9 · 2026-05-18T17:17:38.769Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NkEtiocMqMrqUWvY97E7XH`</summary>

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
  "parentUuid": "4967950f-3048-42e4-b5ae-2bb179874a46",
  "isSidechain": false,
  "requestId": "req_011CbAQzddCNHkYEA9WPbW4D",
  "type": "assistant",
  "uuid": "dabcf9e5-6412-4e50-86b4-beea8485fe02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SeHN8AJnpojXv1JrS2tKTS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34980,
      "cache_read_input_tokens": 11841,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 108,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 34980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34980
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

_source line 10 · 2026-05-18T17:17:38.810Z_

<details><summary>↩ Tool result · `toolu_01NkEtiocMqMrqUWvY97E7XH`</summary>

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
  "parentUuid": "dabcf9e5-6412-4e50-86b4-beea8485fe02",
  "isSidechain": false,
  "promptId": "3915ffa9-3522-4fd9-aef9-082c7cd8e50b",
  "type": "user",
  "uuid": "4bf75fec-290c-4f0b-b5a6-305f1ec08969",
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
    "durationMs": 29,
    "numFiles": 100,
    "truncated": true
  },
  "sourceToolAssistantUUID": "dabcf9e5-6412-4e50-86b4-beea8485fe02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T17:17:43.520Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KQe41X6YtMe38x8cNmERWL`</summary>

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
  "parentUuid": "4bf75fec-290c-4f0b-b5a6-305f1ec08969",
  "isSidechain": false,
  "requestId": "req_011CbAQzy8TNid7rp4bqx7tm",
  "type": "assistant",
  "uuid": "0ad68e8e-559c-41c9-9598-4bfc9f18b4ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTtPBQA61oLYKSrFugBqz9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3126,
      "cache_read_input_tokens": 46821,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 46821,
          "cache_creation_input_tokens": 3126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3126
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

_source line 12 · 2026-05-18T17:17:43.528Z_

<details><summary>↩ Tool result · `toolu_01KQe41X6YtMe38x8cNmERWL`</summary>

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
  "parentUuid": "0ad68e8e-559c-41c9-9598-4bfc9f18b4ad",
  "isSidechain": false,
  "promptId": "3915ffa9-3522-4fd9-aef9-082c7cd8e50b",
  "type": "user",
  "uuid": "a75a80fb-3a9c-4a9a-b642-db1a4d60f760",
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
  "sourceToolAssistantUUID": "0ad68e8e-559c-41c9-9598-4bfc9f18b4ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-18T17:17:43.659Z_

````json
{
  "parentUuid": "a75a80fb-3a9c-4a9a-b642-db1a4d60f760",
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
  "uuid": "554fe326-7b16-43ff-b169-b299f1c2f6a4",
  "timestamp": "2026-05-18T17:17:43.659Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1 ablation 在 controlled protocol 下出现显著 gap，'target quality = sole driver' 被 falsify；regime 结构不清晰 核心假设：['C1 uniform eval gap > 0.5 PPL（gradient coupling 贡…",
  "leafUuid": "554fe326-7b16-43ff-b169-b299f1c2f6a4",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Understanding KL-discovered sparsity patterns via systematic ablation and regime analysis",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1 ablation 在 controlled protocol 下出现显著 gap，'target quality = sole driver' 被 falsify；regime 结构不清晰 核心假设：['C1 uniform eval gap > 0.5 PPL（gradient coupling 贡…",
  "leafUuid": "554fe326-7b16-43ff-b169-b299f1c2f6a4",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Understanding KL-discovered sparsity patterns via systematic ablation and regime analysis",
  "sessionId": "af779414-f62d-4487-867b-50dcbebfd6c4"
}
```

---
