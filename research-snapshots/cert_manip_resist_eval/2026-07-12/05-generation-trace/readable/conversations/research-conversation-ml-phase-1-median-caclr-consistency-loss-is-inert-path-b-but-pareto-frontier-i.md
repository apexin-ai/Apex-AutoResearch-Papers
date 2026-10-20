# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：CaCLR consistency loss is inert (Path B); but Pareto frontier is solid, li

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a.jsonl`
- **Structured JSON:** [`285b9142a8bb8d744c21.json`](../../sessions/28/285b9142a8bb8d744c21.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:26:02.853Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:26:02.853Z",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：CaCLR consistency loss is inert (Path B); but Pareto frontier is solid, linear projection is surprisingly strong, and CKA/decomposition provide genuine mechanistic insight into WHY distributional matching fails\n核心假设：['Pareto frontier replicates on both large models but architecture-dependent shape is moderate (same qualitative trend, quantitatively less distinct than hoped)', 'CaCLR consistency loss (β) is inert across 3 OOM sweep — MMD-based distributional matching does not improve correctness probe transfer', 'CKA analysis reveals geometric misalignment (rotation/scaling of correctness direction) at deeper layers, explaining both why zero-shot degrades AND why MMD fails (distributional ≠ geometric)', 'Linear projection is the winner: learns the rotation that MMD cannot, works with ~50-100 parallel pairs', 'Decomposition works but separation is partial — difficulty projection helps in ~60-70% of language-layer combos, not universal', 'Control tasks pass (selectivity > 10pp) but some low-resource languages show weaker selectivity', 'Orthogonality holds (cosine < 0.12) but with more variance across resource tiers than expected']\n关键指标范围：{'en_best_auroc_large_model': [0.77, 0.83], 'zs_transfer_auroc_median_20lang': [0.65, 0.73], 'pareto_rho_per_lang_median': [-0.65, -0.4], 'caclr_beta_delta_auroc_over_alpha_only': [-0.005, 0.01], 'caclr_full_delta_auroc_over_zeroshot_median': [0.005, 0.02], 'linear_proj_delta_auroc_over_zeroshot_median': [0.02, 0.05], 'linear_proj_min_pairs_for_saturation': [50, 100], 'decomposition_transfer_delta_after_difficulty_removal': [0.005, 0.02], 'decomposition_pct_lang_layer_combos_improved': [0.55, 0.75], 'cka_transfer_pearson_r': [0.45, 0.7], 'orthogonality_cosine_max_across_langs': [0.06, 0.12], 'control_task_selectivity_min': [0.08, 0.15], 'zs_langs_above_0p65_out_of_20': [10, 15], 'sw_bn_low_resource_zs_auroc': [0.53, 0.62], 'ece_reduction_vs_temp_scaling_median': [0.0, 0.02]}\n叙事方向：Analysis paper with principled negative result as centerpiece. Headline: distributional matching fails for cross-lingual correctness probe transfer because the misalignment is geometric, not distributional — CKA proves it, linear projection confirms it. Reorder claims: (1) Pareto frontier established, (2) CKA reveals geometric misalignment as mechanism, (3) CaCLR's failure is PREDICTED by the geometric explanation — this closes the distributional-matching path with both theory and evidence, (4) linear projection succeeds precisely because it learns the rotation. Decomposition and orthogonality become supporting evidence rather than standalone claims. The negative result is the contribution — it redirects the field away from distributional alignment toward geometric alignment for cross-lingual probe transfer. Soften ECE improvement claims; emphasize AUROC and mechanistic understanding. Target: borderline to weak accept at EACL.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\nfocus: Re-dream after first Dream review (3/6). Key framing changes since last dream: (1) CaCLR now has conditional narrative — Path A method contribution if consistency loss works, Path B principled negative result with geometric misalignment explanation if it doesn't; (2) mean-shift rank-invariance as formal theoretical contribution (proof + experimental validation); (3) CKA mechanistic analysis added (plan_011) to explain WHY transfer fails; (4) probing control tasks (plan_013, Hewitt & Liang 2019); (5) linear projection sensitivity analysis (plan_012); (6) statistical rigor: bootstrap CIs + paired tests + Cohen's d as cross-cutting requirement; (7) per-language Spearman rho for Pareto frontier; (8) AUROC threshold sensitivity analysis; (9) expanded related work coverage (domain adaptation theory, alignment literature, conformal prediction); (10) decomposition grid justified (10 langs × 8 layers covers 3 resource tiers × major families). Verify these changes lift score to best ≥ weak accept and median ≥ borderline.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    INT8 weight quantization. Report per-language Spearman rho (depth vs transfer\n    AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: Needs 2× RTX 6000 PRO 96GB at INT8.\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations (GlobalMMLU train split translations,\n    not test items). Compare vs zero-shot, mean-shift, linear projection, few-shot\n    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter\n    tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer\n    results (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative).\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at\n    5 representative layers for Llama 4 Scout on 5% random subset. Validates that\n    INT8 quantization doesn''t distort correctness signals.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Correlate CKA with transfer AUROC to provide mechanistic explanation\n    for the Pareto frontier. Explains WHY deeper layers transfer worse (lower cross-lingual\n    CKA). If CKA shows geometric misalignment (not just distributional shift), this\n    explains why MMD-based CaCLR fails but linear projection succeeds.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Dream review D5: \"no mechanistic explanation\" was flagged [M][W]. CKA upgrades\n    paper from measurement to insight. CPU-bound on cached activations. Reviewer suggests:\n    pilot on MVP activations (mvp_001/mvp_003, 6 langs × 8-9 layers × 2 models) before\n    full-scale run. Pilot is zero-cost and validates CKA pipeline informativeness.\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique.'\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: RUNNING\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T20:26:02.856Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:26:02.856Z",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T20:26:02.891Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：CaCLR consistency loss is inert (Path B); but Pareto frontier is solid, linear projection is surprisingly strong, and CKA/decomposition provide genuine mechanistic insight into WHY distributional matching fails
核心假设：['Pareto frontier replicates on both large models but architecture-dependent shape is moderate (same qualitative trend, quantitatively less distinct than hoped)', 'CaCLR consistency loss (β) is inert across 3 OOM sweep — MMD-based distributional matching does not improve correctness probe transfer', 'CKA analysis reveals geometric misalignment (rotation/scaling of correctness direction) at deeper layers, explaining both why zero-shot degrades AND why MMD fails (distributional ≠ geometric)', 'Linear projection is the winner: learns the rotation that MMD cannot, works with ~50-100 parallel pairs', 'Decomposition works but separation is partial — difficulty projection helps in ~60-70% of language-layer combos, not universal', 'Control tasks pass (selectivity > 10pp) but some low-resource languages show weaker selectivity', 'Orthogonality holds (cosine < 0.12) but with more variance across resource tiers than expected']
关键指标范围：{'en_best_auroc_large_model': [0.77, 0.83], 'zs_transfer_auroc_median_20lang': [0.65, 0.73], 'pareto_rho_per_lang_median': [-0.65, -0.4], 'caclr_beta_delta_auroc_over_alpha_only': [-0.005, 0.01], 'caclr_full_delta_auroc_over_zeroshot_median': [0.005, 0.02], 'linear_proj_delta_auroc_over_zeroshot_median': [0.02, 0.05], 'linear_proj_min_pairs_for_saturation': [50, 100], 'decomposition_transfer_delta_after_difficulty_removal': [0.005, 0.02], 'decomposition_pct_lang_layer_combos_improved': [0.55, 0.75], 'cka_transfer_pearson_r': [0.45, 0.7], 'orthogonality_cosine_max_across_langs': [0.06, 0.12], 'control_task_selectivity_min': [0.08, 0.15], 'zs_langs_above_0p65_out_of_20': [10, 15], 'sw_bn_low_resource_zs_auroc': [0.53, 0.62], 'ece_reduction_vs_temp_scaling_median': [0.0, 0.02]}
叙事方向：Analysis paper with principled negative result as centerpiece. Headline: distributional matching fails for cross-lingual correctness probe transfer because the misalignment is geometric, not distributional — CKA proves it, linear projection confirms it. Reorder claims: (1) Pareto frontier established, (2) CKA reveals geometric misalignment as mechanism, (3) CaCLR's failure is PREDICTED by the geometric explanation — this closes the distributional-matching path with both theory and evidence, (4) linear projection succeeds precisely because it learns the rotation. Decomposition and orthogonality become supporting evidence rather than standalone claims. The negative result is the contribution — it redirects the field away from distributional alignment toward geometric alignment for cross-lingual probe transfer. Soften ECE improvement claims; emphasize AUROC and mechanistic understanding. Target: borderline to weak accept at EACL.


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: xling_calib_direction
focus: Re-dream after first Dream review (3/6). Key framing changes since last dream: (1) CaCLR now has conditional narrative — Path A method contribution if consistency loss works, Path B principled negative result with geometric misalignment explanation if it doesn't; (2) mean-shift rank-invariance as formal theoretical contribution (proof + experimental validation); (3) CKA mechanistic analysis added (plan_011) to explain WHY transfer fails; (4) probing control tasks (plan_013, Hewitt & Liang 2019); (5) linear projection sensitivity analysis (plan_012); (6) statistical rigor: bootstrap CIs + paired tests + Cohen's d as cross-cutting requirement; (7) per-language Spearman rho for Pareto frontier; (8) AUROC threshold sensitivity analysis; (9) expanded related work coverage (domain adaptation theory, alignment literature, conformal prediction); (10) decomposition grid justified (10 langs × 8 layers covers 3 resource tiers × major families). Verify these changes lift score to best ≥ weak accept and median ≥ borderline.

## paper_framing.md

# Paper Framing — xling_calib_direction

## Target Venue
- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
- Core submission: 2 models × 20 languages × all contributions
- Camera-ready extension: Gemma 4 31B Dense + 30+ languages

## Core Insight
The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.

## Core Claims (4, causal chain)

### Claim 1 — Pareto Frontier (Discovery)
Cross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.
- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.
- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.

### Claim 2 — Decomposition (Analysis)
Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
- Evidence: IRT difficulty probes → project out → retrain → compare transfer.

### Claim 3 — CaCLR (Method / Diagnostic)
CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.
- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.
- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.
- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.

### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.

## Story Spine
- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.
- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.

## Field-Level Significance
This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.

## Anticipated Reviewer Concerns & Responses
1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
10. **"No mechanistic explanation"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.
11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.

## Additional Related Work Coverage (Dream-identified gaps)
- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.
- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.
- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.
- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.
- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.

## Differentiation from Closest Prior Work
| Paper | Their Focus | Our Difference |
|-------|-------------|----------------|
| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract
    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,
    train English correctness probes (logistic regression + 2-layer MLP), evaluate
    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,
    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global
    rho.

    '
  priority: P0
  gpu_budget_hours: 80
  deps: []
  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.
  status: planned
- id: plan_002
  claim: 1
  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract
    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.
    INT8 weight quantization. Report per-language Spearman rho (depth vs transfer
    AUROC) alongside global rho.

    '
  priority: P0
  gpu_budget_hours: 40
  deps: []
  notes: Needs 2× RTX 6000 PRO 96GB at INT8.
  status: planned
- id: plan_003
  claim: 3
  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +
    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English
    labels + unlabeled parallel activations (GlobalMMLU train split translations,
    not test items). Compare vs zero-shot, mean-shift, linear projection, few-shot
    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter
    tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer
    results (50% depth + EN-optimal) alongside per-language oracle.

    '
  priority: P0
  gpu_budget_hours: 20
  deps:
  - plan_001
  - plan_002
  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS
    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert
    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional
    narrative).

    '
  status: planned
- id: plan_004
  claim: 2
  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge
    regression on human difficulty scores per Civelli et al.), project out difficulty
    direction from activations, retrain correctness probes on residuals, evaluate
    transfer. 10 representative languages × 8 representative layers per model (20-90%
    depth).

    '
  priority: P0
  gpu_budget_hours: 15
  deps:
  - plan_001
  - plan_002
  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification
    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,
    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.
    Reduced grid is sufficient because decomposition tests a qualitative hypothesis
    (does projecting out difficulty help or hurt?), not a per-language quantitative
    claim. Include random-direction control to rule out dimensionality-reduction artifacts.

    '
  status: planned
- id: plan_005
  claim: 4
  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence
    direction (prompt model for confidence score, fit probe), compute cosine similarity
    with correctness direction across 20 languages × 2 architectures. Analyze by resource
    tier (high/mid/low) and language family.

    '
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_001
  - plan_002
  status: planned
- id: plan_006
  claim: 1
  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at
    each probed layer for both models. Compare English accuracy, cross-lingual transfer
    degradation, and calibration quality. Test hypothesis: linear probes transfer
    better cross-lingually.

    '
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_001
  - plan_002
  notes: CPU-bound, uses cached activations.
  status: planned
- id: plan_007
  claim: 1
  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele
    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.

    '
  priority: P1
  gpu_budget_hours: 30
  deps:
  - plan_001
  - plan_002
  - plan_003
  status: planned
- id: plan_010
  claim: 1
  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at
    5 representative layers for Llama 4 Scout on 5% random subset. Validates that
    INT8 quantization doesn''t distort correctness signals.

    '
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_002
  status: planned
- id: plan_011
  claim: 1
  description: 'CKA cross-lingual representation similarity analysis: compute CKA
    (linear kernel) between English and each target language at every probed layer
    for both models. Correlate CKA with transfer AUROC to provide mechanistic explanation
    for the Pareto frontier. Explains WHY deeper layers transfer worse (lower cross-lingual
    CKA). If CKA shows geometric misalignment (not just distributional shift), this
    explains why MMD-based CaCLR fails but linear projection succeeds.

    '
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_001
  - plan_002
  notes: 'Dream review D5: "no mechanistic explanation" was flagged [M][W]. CKA upgrades
    paper from measurement to insight. CPU-bound on cached activations. Reviewer suggests:
    pilot on MVP activations (mvp_001/mvp_003, 6 langs × 8-9 layers × 2 models) before
    full-scale run. Pilot is zero-cost and validates CKA pipeline informativeness.

    '
  status: planned
- id: plan_012
  claim: 1
  description: 'Linear projection sensitivity analysis: vary number of parallel pairs
    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data
    requirement for this surprisingly strong baseline. Both models × 5 representative
    layers × 20 languages.

    '
  priority: P1
  gpu_budget_hours: 2
  deps:
  - plan_001
  - plan_002
  notes: CPU-bound, uses cached activations. Dream review D11.
  status: planned
- id: plan_013
  claim: 1
  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly
    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)
    across layers and languages. Validates that high AUROC reflects genuine correctness
    direction, not memorized dataset artifacts or probe capacity.

    '
  priority: P1
  gpu_budget_hours: 2
  deps:
  - plan_001
  - plan_002
  notes: 'CPU-bound. Dream review D22: probing methodology critique.'
  status: planned
- id: plan_008
  claim: 1
  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for
    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural
    contrast.

    '
  priority: P2
  gpu_budget_hours: 30
  deps: []
  status: planned
- id: plan_009
  claim: 1
  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.
    Leverages GlobalMMLU/Belebele full language sets.

    '
  priority: P2
  gpu_budget_hours: 50
  deps:
  - plan_001
  - plan_002
  status: planned
- id: mvp_validation
  claim: 1
  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'
  priority: P0
  registry_id: mvp_001
  gpu_budget_hours: 2
  deps: []
  status: DONE
  conclusion: success
  metrics:
    en_best_auroc: 0.7541
    en_best_layer: 27
    en_best_ece_raw: 0.1951
    en_best_ece_tempcal: 0.0744
    temp_scaling_T: 6.21
    en_auroc_range:
    - 0.6113
    - 0.7541
    layer_depth_delta: 0.1428
    layers_tested:
    - 0
    - 4
    - 8
    - 12
    - 16
    - 20
    - 24
    - 27
    zs_pass_langs:
    - zh
    - ar
    - hi
    - ko
    zs_fail_langs:
    - sw
    best_zs_auroc:
      zh: 0.686
      ar: 0.651
      hi: 0.652
      ko: 0.648
      sw: 0.56
    mean_shift_delta_ece:
      zh: -0.36
      ar: -0.06
      hi: 2.22
      sw: 6.44
      ko: 0.01
    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)
    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)
    p2: PASS (4/5)
    p3: PASS (14.28pp)
    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as
      naive baseline negative result)
- id: mvp_complementary
  claim: 1
  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'
  priority: P1
  registry_id: mvp_002
  gpu_budget_hours: 2
  deps:
  - mvp_validation
  status: DONE
  conclusion: success
  metrics:
    en_best_auroc: 0.7481
    en_best_layer: 26
    en_auroc_range:
    - 0.6229
    - 0.7481
    layer_depth_delta: 0.1251
    best_zs_auroc:
      zh: 0.6774
      ar: 0.6302
      hi: 0.6068
      sw: 0.5467
      ko: 0.6678
    best_zs_layer:
      zh: 26
      ar: 26
      hi: 22
      sw: 22
      ko: 26
    pass_fail:
      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)
      P2_zs_auroc: PASS (4/5)
      P3_layer_delta: PASS (12.51pp)
      P4_mean_shift: FAIL (0/5, zero delta)
      overall: PARTIAL
- id: mvp_llama_control
  claim: 1
  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'
  priority: P1
  registry_id: mvp_003
  gpu_budget_hours: 3
  deps:
  - mvp_validation
  status: RUNNING


## registry (completed experiments)

- exp_id: mvp_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    en_best_auroc: 0.7541
    en_best_layer: 27
    en_best_ece_raw: 0.1951
    en_best_ece_tempcal: 0.0744
    temp_scaling_T: 6.21
    en_auroc_range:
    - 0.6113
    - 0.7541
    layer_depth_delta: 0.1428
    layers_tested:
    - 0
    - 4
    - 8
    - 12
    - 16
    - 20
    - 24
    - 27
    zs_pass_langs:
    - zh
    - ar
    - hi
    - ko
    zs_fail_langs:
    - sw
    best_zs_auroc:
      zh: 0.686
      ar: 0.651
      hi: 0.652
      ko: 0.648
      sw: 0.56
    mean_shift_delta_ece:
      zh: -0.36
      ar: -0.06
      hi: 2.22
      sw: 6.44
      ko: 0.01
    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)
    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)
    p2: PASS (4/5)
    p3: PASS (14.28pp)
    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as
      naive baseline negative result)
- exp_id: mvp_002
  name: ''
  status: DONE
  conclusion: success
  metrics:
    en_best_auroc: 0.7481
    en_best_layer: 26
    en_auroc_range:
    - 0.6229
    - 0.7481
    layer_depth_delta: 0.1251
    best_zs_auroc:
      zh: 0.6774
      ar: 0.6302
      hi: 0.6068
      sw: 0.5467
      ko: 0.6678
    best_zs_layer:
      zh: 26
      ar: 26
      hi: 22
      sw: 22
      ko: 26
    pass_fail:
      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)
      P2_zs_auroc: PASS (4/5)
      P3_layer_delta: PASS (12.51pp)
      P4_mean_shift: FAIL (0/5, zero delta)
      overall: PARTIAL
- exp_id: mvp_003
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

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
  "promptId": "341cc4ab-1fbe-4aab-8b92-1f1eec32f1cf",
  "type": "user",
  "uuid": "8216180a-3825-4870-9162-65329712282f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:26:02.890Z_

```json
{
  "parentUuid": "8216180a-3825-4870-9162-65329712282f",
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
  "uuid": "5f621e2f-2e73-4def-9c7d-26a703bf2948",
  "timestamp": "2026-05-20T20:26:02.890Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:26:02.890Z_

```json
{
  "parentUuid": "5f621e2f-2e73-4def-9c7d-26a703bf2948",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b571cabe-032c-41b9-9163-a0e5a807d66f",
  "timestamp": "2026-05-20T20:26:02.890Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：CaCLR consistency loss is inert (Path B); but Pareto frontier is solid, linear projection is surprisingly strong, and CKA/decomposition provide genuine m…",
  "leafUuid": "b571cabe-032c-41b9-9163-a0e5a807d66f",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier median analysis for cross-lingual correctness probe calibration",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a"
}
```

---

### Assistant

_source line 8 · 2026-05-20T20:26:32.794Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for every "planned" experiment in their experiment plan, under the "median" tier assumptions. Each prediction needs a result_rationale explaining why that result would occur under this tier.

Let me carefully go through each planned experiment and generate detailed predictions consistent with the median tier definition.

Let me review the median tier key metrics:
- en_best_auroc_large_model: [0.77, 0.83]
- zs_transfer_auroc_median_20lang: [0.65, 0.73]
- pareto_rho_per_lang_median: [-0.65, -0.4]


- caclr_beta_delta_auroc_over_alpha_only: [-0.005, 0.01]
- caclr_full_delta_auroc_over_zeroshot_median: [0.005, 0.02]
- linear_proj_delta_auroc_over_zeroshot_median: [0.02, 0.05]
- linear_proj_min_pairs_for_saturation: [50, 100]
- decomposition_transfer_delta_after_difficulty_removal: [0.005, 0.02]
- decomposition_pct_lang_layer_combos_improved: [0.55, 0.75]

Now I'm working through the remaining median tier metrics to establish the full range of expected outcomes for each experiment.

The planned experiments are:
1. plan_001 - Qwen3-235B-A22B full Pareto frontier
2. plan_002 - Llama 4 Scout full Pareto frontier
3. plan_003 - CaCL

And I'm looking at the full experimental roadmap with additional ablations and analyses. Let me work through detailed predictions for each experiment, starting with the Qwen3 model's Pareto frontier across its 94 layers.

For the Qwen3-235B setup with 24 probed layers across 20 languages and 5 transfer conditions, I'm expecting the English best AUROC to land around 0.80 with zero-shot median around 0.69, and the Pareto correlation should be roughly -0.52. The MoE architecture's depth should create a clear frontier pattern, qualitatively similar to the MVP but stretched across more layers.

The Llama 4 Scout model with its 48-layer MoE structure and 12 probed layers will likely show a slightly different frontier shape, with English best AUROC potentially similar or marginally lower than Qwen3.

For CaCLR, the inert β path doesn't yield meaningful improvements across the three orders of magnitude sweep, so linear projection emerges as the dominant approach.

Now looking at the decomposition results, about 60-70% of language-layer combinations show improvement with partial separation achieved. Orthogonality metrics stay tight with cosine similarity maxing out below 0.12 across resource tiers, and linear probes consistently outperform more complex alternatives. The additional benchmarks follow similar patterns though possibly slightly weaker, while INT8 quantization shows negligible differences from FP16. CKA-transfer correlation sits around 0.55-0.60, linear projection saturates around 50-100 pairs, and control tasks demonstrate selectivity above 10 percentage points though some low-resource settings are weaker. I'm also planning to contrast with Gemma 4 31B's dense architecture and extend the language coverage in phase 2.

Now I'm going to document all these experiments in detail with a comprehensive YAML configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b571cabe-032c-41b9-9163-a0e5a807d66f",
  "isSidechain": false,
  "requestId": "req_011CbESz58acc2FHjvhDfK1J",
  "type": "assistant",
  "uuid": "2c4f2687-1b3c-42b9-b4f1-e2c29d52fd16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F85TP8qUz7pkGv58DNa81Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13426,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16651,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13426
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

_source line 9 · 2026-05-20T20:31:42.486Z_

```yaml
tier: median
narrative_guidance: >
  Analysis paper with principled negative result as centerpiece. Narrative arc:
  (1) Pareto frontier established on two large MoE architectures — qualitatively replicates
  MVP findings but rho is moderate (median ~-0.52), confirming architecture-dependent shape;
  (2) CKA reveals geometric misalignment increasing with depth — CKA-transfer correlation
  r≈0.58 provides mechanistic explanation for WHY deeper layers transfer worse;
  (3) CaCLR consistency loss (β) is inert across 3 OOM sweep — this is PREDICTED by
  the geometric explanation: MMD matches distributions but cannot correct the rotation
  of the correctness direction across language subspaces;
  (4) Linear projection succeeds (~+3.5pp over zero-shot) precisely because it learns the
  rotation that MMD cannot, saturating at ~70 parallel pairs.
  Decomposition and orthogonality are supporting evidence. Decomposition shows difficulty
  is shared but capability-specific component drives degradation (~65% of combos improved).
  Orthogonality persists across languages (cosine < 0.10) but with more variance in
  low-resource languages. Control tasks confirm probe selectivity (>10pp) but sw/bn are
  weaker. ECE improvements over temperature scaling are negligible — emphasize AUROC and
  mechanistic understanding. Target: borderline to weak accept at EACL.

imagined_experiments:
  - name: "Qwen3-235B-A22B Full Pareto Frontier"
    plan_id: "plan_001"
    description: >
      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): 24 probed layers,
      20 languages, 5 transfer conditions (zero-shot, mean-shift, linear projection,
      few-shot 25/100, CaCLR). Per-language and global Spearman rho.
    expected_results:
      en_best_auroc: 0.81
      en_best_layer: 72
      en_best_ece_raw: 0.17
      en_best_ece_tempcal: 0.065
      temp_scaling_T: 5.8
      en_auroc_range: [0.58, 0.81]
      en_auroc_50pct_depth_layer47: 0.76
      zs_transfer_auroc_median_20lang_at_en_optimal: 0.63
      zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.70
      best_transfer_layer: 48
      pareto_rho_global: -0.58
      pareto_rho_per_lang_median: -0.51
      pareto_rho_per_lang_range: [-0.78, -0.21]
      zs_langs_above_0p65: 13
      zs_auroc_zh: 0.74
      zs_auroc_es: 0.73
      zs_auroc_fr: 0.73
      zs_auroc_de: 0.72
      zs_auroc_ar: 0.70
      zs_auroc_hi: 0.69
      zs_auroc_ru: 0.71
      zs_auroc_ko: 0.69
      zs_auroc_ja: 0.70
      zs_auroc_pt: 0.72
      zs_auroc_vi: 0.68
      zs_auroc_tr: 0.67
      zs_auroc_id: 0.68
      zs_auroc_th: 0.66
      zs_auroc_pl: 0.69
      zs_auroc_uk: 0.68
      zs_auroc_he: 0.66
      zs_auroc_el: 0.65
      zs_auroc_sw: 0.58
      zs_auroc_bn: 0.57
      mean_shift_delta_auroc_median: 0.000
      linear_proj_delta_auroc_over_zs_median: 0.035
      fewshot_25_delta_auroc_over_zs_median: 0.025
      fewshot_100_delta_auroc_over_zs_median: 0.045
      ece_reduction_vs_temp_scaling_median: 0.008
    result_rationale: >
      Qwen3-235B-A22B is a 94-layer MoE model — significantly deeper than the 7B MVP.
      The English best AUROC rises to 0.81 because the larger model encodes stronger
      correctness signals (more parameters, more knowledge). The best English layer is
      at ~76% depth (layer 72), consistent with the MVP pattern where correctness peaks
      in deep-but-not-final layers. The Pareto frontier is present but rho is moderate
      (-0.51 median per-language) because: (a) the MoE routing creates more heterogeneous
      layer representations, reducing the clean monotonic depth-degradation pattern seen
      in dense models; (b) some languages (especially high-resource zh/es/fr) have strong
      multilingual representations even at deeper layers due to extensive pretraining data,
      attenuating the negative correlation. The per-language rho range [-0.78, -0.21]
      reflects that low-resource languages (sw, bn) show stronger negative correlation
      (their representations diverge from English more sharply at depth) while high-resource
      languages show weaker correlation (they maintain reasonable alignment throughout).
      13/20 languages cross 0.65 AUROC — most European and major Asian languages transfer
      adequately at optimal layers, but sw (0.58) and bn (0.57) remain below threshold
      due to limited pretraining representation for these languages. Mean-shift produces
      exactly zero AUROC change (rank-invariance proof holds), confirming the MVP finding.
      Linear projection (+3.5pp) outperforms few-shot-25 (+2.5pp) because it directly
      corrects geometric misalignment rather than relying on a small labeled sample.
      ECE improvement over temperature scaling is marginal (0.8pp) because probe-based
      calibration and temperature scaling address different aspects — at the median tier,
      probes don't provide much additional calibration beyond what temperature scaling
      already captures.

    tables:
      - name: "Table 1: Qwen3-235B-A22B Pareto Frontier — Zero-Shot Transfer AUROC by Language × Layer"
        description: >
          24 probed layers (rows) × 20 languages + English (columns). Cells show AUROC.
          Bold: best layer per language. Gray shading: layers within 1pp of best.
          Bottom rows: global and per-language Spearman rho with 95% bootstrap CI.
          Key pattern: English-optimal layer (72) ≠ transfer-optimal layer (48) for
          most languages. High-resource languages show flatter profiles; low-resource
          show steeper drop-off at deep layers.
      - name: "Table 2: Qwen3-235B-A22B Transfer Method Comparison at Fixed Layers"
        description: >
          5 transfer methods (columns) × 20 languages (rows), evaluated at two fixed
          layers (50% depth = layer 47, EN-optimal = layer 72) plus per-language oracle.
          Shows AUROC and ΔAUROC vs zero-shot. Bootstrap 95% CI and paired permutation
          test p-values. Cohen's d for each method vs zero-shot baseline.

    figures_description:
      - "Figure: Pareto frontier scatter plot — x-axis: English AUROC, y-axis: median zero-shot transfer AUROC across 20 langs. Each point is a layer. Annotated with layer numbers. Pareto-optimal layers highlighted. Separate curves for resource tiers (high/mid/low) showing tier-dependent frontier shape."
      - "Figure: Per-language Spearman rho bar chart — 20 bars sorted by rho magnitude. Color-coded by resource tier. Error bars show bootstrap 95% CI. Horizontal line at rho = -0.5 for reference."

    analysis: >
      The Pareto frontier replicates on this large MoE model but with moderate per-language
      rho (-0.51 median). The architecture-dependent shape is visible: MoE routing creates
      more variable layer representations, so the depth-transfer tradeoff is less smooth
      than in a dense model. The key finding is that 13/20 languages achieve usable
      zero-shot transfer (>0.65 AUROC) at optimal layers, validating the approach for
      most languages. The 7 languages below threshold cluster in low-resource (sw, bn)
      and morphologically distant categories (th, he at marginal 0.66). Linear projection
      provides the most consistent improvement across languages.

  - name: "Llama 4 Scout Full Pareto Frontier"
    plan_id: "plan_002"
    description: >
      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): 12 probed layers,
      20 languages, 5 transfer conditions. Per-language Spearman rho.
    expected_results:
      en_best_auroc: 0.79
      en_best_layer: 36
      en_best_ece_raw: 0.19
      en_best_ece_tempcal: 0.070
      temp_scaling_T: 6.0
      en_auroc_range: [0.60, 0.79]
      en_auroc_50pct_depth_layer24: 0.74
      zs_transfer_auroc_median_20lang_at_en_optimal: 0.62
      zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.68
      best_transfer_layer: 24
      pareto_rho_global: -0.62
      pareto_rho_per_lang_median: -0.54
      pareto_rho_per_lang_range: [-0.82, -0.28]
      zs_langs_above_0p65: 11
      zs_auroc_zh: 0.72
      zs_auroc_es: 0.71
      zs_auroc_fr: 0.71
      zs_auroc_de: 0.70
      zs_auroc_ar: 0.68
      zs_auroc_hi: 0.67
      zs_auroc_ru: 0.69
      zs_auroc_ko: 0.66
      zs_auroc_ja: 0.67
      zs_auroc_pt: 0.70
      zs_auroc_vi: 0.65
      zs_auroc_tr: 0.64
      zs_auroc_id: 0.66
      zs_auroc_th: 0.63
      zs_auroc_pl: 0.67
      zs_auroc_uk: 0.65
      zs_auroc_he: 0.63
      zs_auroc_el: 0.62
      zs_auroc_sw: 0.55
      zs_auroc_bn: 0.54
      mean_shift_delta_auroc_median: 0.000
      linear_proj_delta_auroc_over_zs_median: 0.032
      fewshot_25_delta_auroc_over_zs_median: 0.022
      fewshot_100_delta_auroc_over_zs_median: 0.040
      ece_reduction_vs_temp_scaling_median: 0.005
    result_rationale: >
      Llama 4 Scout has fewer layers (48 vs 94) and a different MoE architecture from
      Qwen3. The English best AUROC is slightly lower (0.79 vs 0.81) reflecting somewhat
      weaker correctness encoding in a shallower architecture. The Pareto rho is slightly
      stronger negative (-0.54 vs -0.51) because with fewer layers, each layer step
      represents a larger proportional depth change, making the depth-transfer tradeoff
      more pronounced. The best transfer layer at 50% depth (layer 24) is consistent
      with the pattern that mid-depth layers balance English quality and cross-lingual
      alignment. 11/20 languages cross 0.65, slightly fewer than Qwen3 — Llama 4's
      multilingual pretraining may be less balanced, particularly for mid-resource
      languages like tr (0.64) and vi (0.65) that were marginal on Qwen3. Low-resource
      sw (0.55) and bn (0.54) are again the weakest, confirming this is a fundamental
      limitation of pretraining representation rather than architecture-specific.
      The same qualitative Pareto pattern holds but the quantitative frontier shape
      differs — the drop-off from English-optimal to transfer-optimal is steeper on
      Llama 4, confirming architecture-dependence without requiring architecture-specific
      tuning as a paper claim.

    tables:
      - name: "Table 3: Llama 4 Scout Pareto Frontier — Zero-Shot Transfer AUROC by Language × Layer"
        description: >
          12 probed layers × 20 languages + English. Same format as Table 1.
          Key contrast with Qwen3: steeper Pareto drop-off, fewer layers in
          the Pareto-optimal set due to coarser layer sampling.
      - name: "Table 4: Llama 4 Scout Transfer Method Comparison"
        description: >
          Same format as Table 2. Llama 4 Scout results. Key finding: linear
          projection improvement (+3.2pp) is comparable to Qwen3, suggesting
          the geometric correction transfers across architectures.

    figures_description:
      - "Figure: Side-by-side Pareto frontier comparison — Qwen3-235B (left) vs Llama 4 Scout (right). Same axis scales for direct visual comparison. Annotated with architecture properties (depth, MoE routing). Shows that qualitative Pareto shape replicates but quantitative steepness differs."

    analysis: >
      Llama 4 Scout confirms the Pareto frontier generalizes across architectures.
      The steeper negative rho (-0.54) vs Qwen3 (-0.51) is a moderate difference that
      supports the architecture-dependence claim but is not dramatic enough to call it
      a strong architectural contrast. This is the median-tier signature: same qualitative
      finding, quantitatively less distinct than ideal. Both models agree on the key
      implication: mid-depth layers are the right operating point for cross-lingual transfer.

  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: "plan_003"
    description: >
      CaCLR probe training with L_BCE + α·L_SB-ECE + β·L_consistency (MMD).
      α sweep (0.01–10.0), β sweep (0.001–1.0) across 3 OOM. Full comparison
      vs zero-shot, mean-shift, linear projection, few-shot on both models × 20 langs.
    expected_results:
      # α-only (β=0) results — SB-ECE regularization
      alpha_optimal: 0.5
      alpha_only_en_auroc_at_en_optimal_layer_qwen: 0.805
      alpha_only_en_ece_at_en_optimal_layer_qwen: 0.058
      alpha_only_zs_median_auroc_qwen: 0.695
      alpha_only_zs_median_auroc_llama: 0.675
      # β sweep results — consistency loss evaluation
      beta_0p001_delta_auroc_over_alpha_only_median: 0.002
      beta_0p01_delta_auroc_over_alpha_only_median: 0.001
      beta_0p1_delta_auroc_over_alpha_only_median: -0.001
      beta_1p0_delta_auroc_over_alpha_only_median: -0.003
      beta_sweep_max_delta_auroc: 0.003
      beta_sweep_significant_at_p05: false
      # CaCLR full (best α+β) vs baselines
      caclr_full_delta_auroc_over_zeroshot_median: 0.012
      caclr_full_delta_auroc_over_zeroshot_range: [-0.005, 0.035]
      caclr_vs_linear_proj_delta_median: -0.023
      caclr_vs_fewshot100_delta_median: -0.033
      linear_proj_delta_auroc_over_zs_median_qwen: 0.035
      linear_proj_delta_auroc_over_zs_median_llama: 0.032
      fewshot_25_delta_auroc_over_zs_median: 0.024
      fewshot_100_delta_auroc_over_zs_median: 0.043
      mean_shift_delta_auroc_median: 0.000
      # Method ranking (by median ΔAUROC over zero-shot)
      method_ranking: ["few-shot-100", "linear-projection", "few-shot-25", "CaCLR-full", "CaCLR-α-only", "zero-shot", "mean-shift"]
      # Per-resource-tier breakdown
      caclr_beta_delta_high_resource: 0.004
      caclr_beta_delta_mid_resource: 0.000
      caclr_beta_delta_low_resource: -0.002
      # Statistical tests
      caclr_beta_vs_alpha_only_paired_perm_p: 0.42
      caclr_beta_vs_alpha_only_cohens_d: 0.08
      linear_proj_vs_zeroshot_paired_perm_p: 0.001
      linear_proj_vs_zeroshot_cohens_d: 0.55
    result_rationale: >
      The β (consistency loss) is inert because MMD-based distributional matching
      fundamentally cannot correct the geometric misalignment that CKA reveals.
      MMD penalizes differences in mean embeddings and kernel-space distributional
      moments — it can align marginal distributions but cannot learn the rotation
      of the correctness direction across language subspaces. At low β (0.001), the
      MMD signal is too weak to affect optimization. At medium β (0.01–0.1), the
      gradient signal exists but points in the wrong direction — it pushes overall
      distributional alignment without specifically aligning the correctness-relevant
      subspace. At high β (1.0), the MMD term dominates and slightly hurts English
      AUROC by distorting the probe weights. The α-only (SB-ECE) variant provides
      small but real calibration improvement (better ECE) because smooth-binned ECE
      regularization is a well-motivated objective that doesn't require cross-lingual
      alignment. The total CaCLR improvement over zero-shot (+1.2pp) comes entirely
      from the α term's calibration regularization, not from cross-lingual consistency.
      Cohen's d = 0.08 for β effect is negligible. In contrast, linear projection
      achieves +3.5pp because it directly estimates and corrects the rotation via a
      learned affine transformation on parallel pairs. Few-shot-100 achieves +4.3pp
      because it sidesteps alignment entirely by training on target-language labels.
      This ranking — few-shot > linear-projection > CaCLR ≈ α-only > zero-shot >
      mean-shift — is the key empirical result that the geometric explanation predicts.

    tables:
      - name: "Table 5: β Sensitivity Sweep — ΔAUROC over α-only baseline"
        description: >
          β values (rows: 0, 0.001, 0.01, 0.1, 1.0) × summary statistics (columns:
          median ΔAUROC, mean, std, min, max, # languages improved, paired permutation
          p-value, Cohen's d). Both models shown side-by-side. Key: no β value achieves
          p < 0.05 or d > 0.2 — consistency loss is definitively inert.
      - name: "Table 6: Transfer Method Comparison — Median AUROC across 20 Languages"
        description: >
          Methods (rows: zero-shot, mean-shift, CaCLR-α-only, CaCLR-full, linear-projection,
          few-shot-25, few-shot-100) × Models (columns: Qwen3, Llama 4) × 2 fixed layers
          + per-language oracle. ΔAUROC vs zero-shot with bootstrap 95% CI. Ranking
          is consistent across models. Linear projection and few-shot clearly dominate.
      - name: "Table 7: CaCLR β Effect by Resource Tier"
        description: >
          Resource tier (rows: HIGH, MID, LOW) × β levels. Shows that inertness is
          consistent across tiers — not a power issue with low-resource languages but
          a fundamental limitation of distributional matching.

    figures_description:
      - "Figure: α sensitivity curve — x-axis: log(α), y-axis: English ECE and AUROC at EN-optimal layer. Shows that α ~0.5 optimizes ECE-AUROC tradeoff. SB-ECE regularization provides genuine calibration benefit."
      - "Figure: β sensitivity heatmap — x-axis: log(β), y-axis: languages sorted by resource tier. Color: ΔAUROC over α-only. Shows near-zero change (white) across entire grid. Highlights absence of any language × β sweet spot."
      - "Figure: Transfer method ranking forest plot — each method as a row, showing median ΔAUROC with bootstrap 95% CI. Clear separation between geometric methods (linear-proj, few-shot) and distributional methods (CaCLR-β, mean-shift)."

    analysis: >
      CaCLR's β inertness is the paper's centerpiece negative result. The analysis
      proceeds in three steps: (1) empirically, β has negligible effect (d=0.08, p=0.42)
      across 3 OOM and both architectures; (2) mechanistically, CKA analysis (plan_011)
      reveals that cross-lingual misalignment at deeper layers is geometric (rotation/scaling)
      rather than distributional (mean/covariance shift); (3) linear projection's success
      (+3.5pp) confirms the geometric explanation — it succeeds precisely because it
      learns the rotation that MMD cannot represent. This three-part argument closes the
      distributional-matching path with both theory and evidence. The α-only variant
      retains value as a calibration regularizer — it improves ECE without hurting AUROC.

  - name: "Difficulty-Controlled Decomposition Ablation"
    plan_id: "plan_004"
    description: >
      IRT difficulty probes, project out difficulty direction, retrain correctness probes
      on residuals. 10 languages × 8 layers per model. Random-direction control.
    expected_results:
      # Difficulty probe quality
      difficulty_probe_r2_en_median_across_layers: 0.42
      difficulty_probe_r2_range: [0.25, 0.55]
      # Transfer delta after difficulty removal
      decomposition_transfer_delta_median: 0.012
      decomposition_transfer_delta_range: [-0.01, 0.035]
      # Percentage of lang-layer combos improved
      pct_combos_improved: 0.65
      pct_combos_improved_by_tier_high: 0.72
      pct_combos_improved_by_tier_mid: 0.65
      pct_combos_improved_by_tier_low: 0.53
      # Layer-depth pattern
      improvement_stronger_at_deep_layers: true
      improvement_at_shallow_layers_pct: 0.50
      improvement_at_deep_layers_pct: 0.78
      # Random direction control
      random_direction_delta_median: 0.003
      random_direction_delta_significant: false
      # Cosine between difficulty and correctness directions
      difficulty_correctness_cosine_median: 0.18
      difficulty_correctness_cosine_range: [0.08, 0.30]
      # Statistical tests
      decomposition_vs_baseline_paired_p: 0.03
      decomposition_cohens_d: 0.28
    result_rationale: >
      Decomposition works but is partial because the difficulty-capability separation
      is not clean. The difficulty direction (IRT-derived) captures ~42% variance in
      human difficulty scores (R²) — reasonable but not perfect, meaning the projection
      leaves residual difficulty signal mixed with capability. At deep layers, removing
      difficulty helps more often (78% of combos) because the capability-specific component
      dominates transfer degradation there — once you remove the shared difficulty signal,
      the residual is more language-specific and harder to transfer. At shallow layers,
      the improvement rate drops to ~50% (near chance) because both difficulty and
      capability signals are more entangled and less linearly separable. The 65% overall
      improvement rate is genuine but not universal — it demonstrates the decomposition
      is prescriptive for about two-thirds of settings. The random-direction control
      (median +0.3pp, not significant) confirms this isn't a dimensionality-reduction
      artifact. Low-resource languages show weaker improvement (53%) because their
      correctness probes are noisier to begin with, and the difficulty projection may
      remove some of the limited signal they have. The modest Cohen's d (0.28) reflects
      that improvements are real but small — this is a supporting analytical result,
      not a standalone method contribution.

    tables:
      - name: "Table 8: Decomposition Results — 10 Languages × 8 Layers"
        description: >
          Heatmap table: languages (rows) × layers (columns). Cells show ΔAUROC after
          difficulty removal. Green: improved (>0.5pp), white: unchanged, red: degraded.
          Marginal summaries: % improved per language, per layer. Shows concentration
          of improvement at deep layers and high-resource languages.
      - name: "Table 9: Decomposition vs Random Direction Control"
        description: >
          Comparison: difficulty projection vs random projection vs no projection.
          Median ΔAUROC, bootstrap CI, paired test. Confirms difficulty projection
          specifically — not arbitrary dimensionality reduction — drives improvement.

    figures_description:
      - "Figure: Decomposition improvement rate vs layer depth — bar chart showing fraction of languages improved at each layer. Monotonically increasing trend from ~50% at shallowest to ~78% at deepest. Supports narrative that capability-specific component is the deep-layer transfer bottleneck."

    analysis: >
      Decomposition provides supporting evidence for the geometric misalignment narrative.
      The fact that difficulty removal helps more at deep layers aligns with the CKA
      finding — at depth, the capability-specific component (which is geometrically
      misaligned across languages) drives transfer failure, and removing the shared
      difficulty component isolates this effect. However, the partial success rate (65%)
      and modest effect size (d=0.28) keep this as supporting analysis rather than a
      standalone claim. The finding is prescriptive: researchers attempting cross-lingual
      probe transfer should first assess whether difficulty confounding explains their
      transfer gaps — in ~65% of cases, it partially does.

  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: "plan_005"
    description: >
      Verbalized confidence direction extraction, cosine similarity with correctness
      direction. 20 languages × 2 architectures. Resource-tier and family analysis.
    expected_results:
      # English reference
      en_cosine_qwen: 0.035
      en_cosine_llama: 0.038
      # Cross-lingual results
      cosine_median_across_langs_qwen: 0.055
      cosine_median_across_langs_llama: 0.060
      cosine_max_across_langs: 0.10
      cosine_max_language: "sw"
      cosine_range: [0.02, 0.10]
      # Resource tier breakdown
      cosine_median_high_resource: 0.04
      cosine_median_mid_resource: 0.06
      cosine_median_low_resource: 0.085
      cosine_variance_high: 0.0003
      cosine_variance_mid: 0.0008
      cosine_variance_low: 0.0018
      # Orthogonality holds (< 0.12) for all languages
      all_langs_below_threshold: true
      # Correlation with resource level
      cosine_vs_resource_spearman_rho: 0.52
      cosine_vs_resource_p: 0.018
    result_rationale: >
      Orthogonality persists across languages because the separation between correctness
      and verbalized confidence is a structural property of how transformers process
      MCQA — the model's internal "do I know this?" signal (correctness) and its
      verbalized "how confident am I?" output occupy orthogonal subspaces by design
      (the former is a representation-level property, the latter is optimized during
      RLHF/instruction-tuning for human-readable outputs). The English cosine (~0.035-
      0.038) replicates Miao & Ungar (2026). Non-English cosines are slightly higher
      (median 0.055-0.060) because: (a) non-English confidence verbalization is noisier
      (models are less calibrated in non-English expression of uncertainty); (b) the
      confidence probe may capture some language-switching signal that correlates weakly
      with correctness (lower-resource languages trigger more uncertain generation
      behavior). The max cosine at 0.10 (sw) still satisfies the orthogonality threshold
      (<0.12) but shows more variance — Swahili's limited pretraining data means both
      probes are noisier, and noise correlations inflate apparent cosine. The resource-
      tier gradient (rho=0.52, p=0.018) is a novel finding: orthogonality is stronger
      (lower cosine) for high-resource languages, suggesting that abundant pretraining
      data helps separate correctness from confidence representations. However, even the
      worst case (0.10) is far from the ~0.5+ that would indicate meaningful alignment,
      confirming that output-based calibration is structurally limited across all languages.

    tables:
      - name: "Table 10: Correctness–Confidence Cosine Similarity Across Languages"
        description: >
          20 languages (rows, grouped by resource tier) × 2 architectures (column pairs).
          Each cell: cosine similarity ± bootstrap 95% CI. Bottom: tier medians and
          Spearman correlation with log(pretraining data estimate). All values < 0.12.

    figures_description:
      - "Figure: Cosine similarity vs estimated pretraining data — scatter plot, 20 languages × 2 models. Log scale x-axis (pretraining tokens). Weak positive trend (more data → lower cosine → stronger orthogonality). Highlights sw/bn as outliers with highest cosine."

    analysis: >
      Orthogonality holds universally (max 0.10 < 0.12 threshold) but with a resource-
      tier gradient that is novel relative to Miao & Ungar's English-only finding. This
      extends their claim to multilingual settings with a nuance: the structural separation
      is slightly weaker for low-resource languages, though never approaching a level
      that would make output-based calibration viable. This supports the paper's broader
      argument that probe-based calibration is the right paradigm for all languages,
      but the cross-lingual transfer challenge is the bottleneck — not the underlying
      signal quality.

  - name: "Probe Complexity Comparison"
    plan_id: "plan_006"
    description: >
      Logistic regression vs 2-layer MLP at each probed layer for both models.
      English accuracy, cross-lingual transfer degradation, calibration quality.
    expected_results:
      # English AUROC comparison
      logreg_en_best_auroc_qwen: 0.81
      mlp_en_best_auroc_qwen: 0.835
      logreg_en_best_auroc_llama: 0.79
      mlp_en_best_auroc_llama: 0.815
      # Cross-lingual transfer comparison
      logreg_zs_median_qwen: 0.70
      mlp_zs_median_qwen: 0.665
      logreg_zs_median_llama: 0.68
      mlp_zs_median_llama: 0.645
      # Transfer degradation (EN AUROC - ZS median AUROC)
      logreg_transfer_gap: 0.11
      mlp_transfer_gap: 0.17
      # Calibration
      logreg_ece_median: 0.068
      mlp_ece_median: 0.075
      # MLP advantage concentrated at deep layers
      mlp_advantage_en_deep_layers: 0.03
      mlp_advantage_en_shallow_layers: 0.01
      # Linear probes transfer better (hypothesis confirmed)
      logreg_better_transfer_pct_langs: 0.80
    result_rationale: >
      MLP probes achieve ~2.5pp higher English AUROC because they can capture nonlinear
      interactions in the representation — the correctness signal has a small nonlinear
      component that logistic regression misses. However, this nonlinear component is
      language-specific (learned from English data, doesn't generalize), so MLP probes
      show 6pp larger transfer gap than logistic regression. The MLP essentially overfits
      to English-specific nonlinearities in the correctness representation. This confirms
      the hypothesis that linear probes transfer better cross-lingually — the linear
      component of the correctness signal is more universal across languages, while
      nonlinear components are language-specific. The MLP advantage is concentrated at
      deep layers (+3pp at deep vs +1pp at shallow) because deeper representations have
      more complex, language-specific structure for the MLP to exploit. 80% of languages
      see better transfer with logistic regression, with the exceptions being high-
      resource languages (zh, es) where the MLP's nonlinear component partially transfers
      due to shared pretraining features. This result justifies the paper's focus on
      logistic regression probes and reinforces the geometric (linear) framing.

    tables:
      - name: "Table S1: Probe Complexity — English AUROC and Transfer Gap by Layer"
        description: >
          Supplementary table. Layers (rows) × (LogReg EN, MLP EN, LogReg ZS-median,
          MLP ZS-median, LogReg gap, MLP gap) for each model. Shows MLP's higher EN
          AUROC comes at cost of larger transfer gap. Gap difference increases with depth.

    figures_description:
      - "Figure: Transfer gap (EN AUROC - ZS median) vs layer depth for LogReg and MLP. Two lines diverging at deeper layers — MLP gap grows faster, confirming linear probes are preferable for cross-lingual transfer."

    analysis: >
      This experiment justifies the methodological choice of logistic regression probes
      and provides additional evidence for the geometric/linear framing. If the
      correctness signal were deeply nonlinear, MLP's advantage would transfer — the
      fact that it doesn't confirms that the transferable component is linear. Goes in
      supplementary material as a methodological validation.

  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: "plan_007"
    description: >
      Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages each).
      Validates generalization beyond GlobalMMLU.
    expected_results:
      # Belebele results
      belebele_en_best_auroc_qwen: 0.78
      belebele_zs_median_qwen: 0.68
      belebele_pareto_rho_median: -0.48
      belebele_linear_proj_delta: 0.030
      belebele_caclr_beta_delta: 0.003
      # MMLU-ProX results
      mmlupx_en_best_auroc_qwen: 0.82
      mmlupx_zs_median_qwen: 0.69
      mmlupx_pareto_rho_median: -0.50
      mmlupx_linear_proj_delta: 0.033
      mmlupx_caclr_beta_delta: 0.002
      # Cross-benchmark consistency
      auroc_rank_correlation_globalmmlu_vs_belebele: 0.82
      auroc_rank_correlation_globalmmlu_vs_mmlupx: 0.88
      method_ranking_consistent_across_benchmarks: true
    result_rationale: >
      Belebele is a reading comprehension benchmark — fundamentally different from
      MCQA knowledge testing. The correctness signal is still present (models either
      comprehend or don't) but Belebele's English AUROC is slightly lower (0.78 vs 0.81)
      because reading comprehension correctness is less cleanly encoded than factual
      knowledge correctness. The Pareto rho is slightly weaker (-0.48) because Belebele's
      parallel passages provide more uniform cross-lingual signal than GlobalMMLU's
      diverse topics. MMLU-ProX, being closer to GlobalMMLU in format, shows more similar
      results (0.82 EN AUROC, -0.50 rho). The key finding is that method rankings are
      consistent — linear projection still outperforms CaCLR, and CaCLR's β term
      remains inert across benchmarks. This rules out the possibility that CaCLR's
      failure is GlobalMMLU-specific. The high rank correlations (0.82–0.88) between
      benchmarks confirm that per-language transfer difficulty is a property of the
      model's multilingual representations, not the benchmark.

    tables:
      - name: "Table S2: Cross-Benchmark Generalization"
        description: >
          Supplementary. Benchmarks (rows: GlobalMMLU, Belebele, MMLU-ProX) × key metrics
          (EN AUROC, ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ). Shows consistent
          patterns across benchmarks. Rank correlation between per-language AUROCs.

    figures_description:
      - "Figure: Per-language AUROC scatter — GlobalMMLU vs Belebele, GlobalMMLU vs MMLU-ProX. Each point is a language. High correlation confirms benchmark-invariant transfer difficulty ranking."

    analysis: >
      Benchmark generalization confirms all findings are not artifacts of GlobalMMLU.
      The consistent method ranking across three benchmarks strengthens the negative
      result — CaCLR's β inertness is a fundamental property of distributional matching
      vs geometric misalignment, not a benchmark-specific failure. Goes in supplementary
      or a short main-text paragraph.

  - name: "INT8 Validation Ablation"
    plan_id: "plan_010"
    description: >
      INT8 vs FP16 comparison at 5 representative layers for Llama 4 Scout on 5% subset.
    expected_results:
      int8_fp16_auroc_max_diff: 0.008
      int8_fp16_auroc_mean_diff: 0.003
      int8_fp16_ece_max_diff: 0.012
      int8_fp16_correlation_r: 0.997
      int8_fp16_rank_agreement_pct: 0.98
      distortion_significant: false
    result_rationale: >
      INT8 weight-only quantization preserves the vast majority of activation-space
      structure because (a) it quantizes weights, not activations — the internal
      representations used for probing are computed in higher precision; (b) 7B+ models
      are robust to INT8 quantization (well-established in the quantization literature);
      (c) correctness probes operate on high-dimensional representations (4096+ dims)
      where small per-dimension perturbations from quantization average out. The max
      AUROC difference of 0.8pp across any layer is within bootstrap confidence intervals.
      The 0.997 correlation between INT8 and FP16 probe scores confirms that quantization
      shifts all scores by a near-constant offset without affecting ranking. This
      validation is necessary for reviewer reassurance but expected to be a non-issue.

    tables:
      - name: "Table S3: INT8 vs FP16 Validation"
        description: >
          Supplementary. 5 layers × metrics (INT8 AUROC, FP16 AUROC, Δ, rank correlation).
          All differences within bootstrap CI. Conclusion: INT8 does not distort
          correctness signals.

    figures_description: []

    analysis: >
      Straightforward validation that INT8 quantization doesn't affect conclusions.
      One paragraph in supplementary material with the table. Addresses anticipated
      reviewer concern #5.

  - name: "CKA Cross-Lingual Representation Similarity"
    plan_id: "plan_011"
    description: >
      CKA (linear kernel) between English and each target language at every probed layer,
      both models. Correlate CKA with transfer AUROC.
    expected_results:
      # CKA values
      cka_en_zh_shallow_layer12_qwen: 0.88
      cka_en_zh_deep_layer72_qwen: 0.62
      cka_en_sw_shallow_layer12_qwen: 0.78
      cka_en_sw_deep_layer72_qwen: 0.38
      cka_median_shallow_across_langs: 0.84
      cka_median_deep_across_langs: 0.52
      cka_decrease_with_depth_significant: true
      # CKA–transfer correlation
      cka_transfer_pearson_r_qwen: 0.62
      cka_transfer_pearson_r_llama: 0.54
      cka_transfer_pearson_r_pooled: 0.58
      cka_transfer_pearson_p: 0.00001
      # Resource-tier CKA gradient
      cka_deep_high_resource_median: 0.60
      cka_deep_mid_resource_median: 0.48
      cka_deep_low_resource_median: 0.36
      # CKA vs MMD comparison (same layer-language pairs)
      mmd_transfer_pearson_r: 0.25
      mmd_explains_variance_pct: 6
      cka_explains_variance_pct: 34
    result_rationale: >
      CKA measures representational similarity including geometric structure (rotation,
      scaling), while MMD measures distributional distance (mean, variance, higher
      moments). CKA decreases with depth because deeper transformer layers specialize
      more for language-specific processing — the cross-lingual alignment enforced by
      shared vocabulary embeddings and early layers gradually gives way to language-
      specific feature extraction. The CKA–transfer correlation (r=0.58) is moderate-
      to-strong: it explains 34% of variance in transfer AUROC, confirming that
      representational geometry is a major (but not the only) factor in transfer success.
      The remaining variance comes from factors like probe quality, dataset difficulty
      distribution, and non-geometric aspects of the representation. Critically, CKA
      (r=0.58) substantially outpredicts MMD (r=0.25) as a predictor of transfer
      success — this is the key mechanistic finding. If cross-lingual misalignment were
      distributional (mean/covariance shift), MMD would predict transfer as well as or
      better than CKA. The fact that CKA is 2.3× more predictive demonstrates that the
      misalignment is geometric (rotation/scaling of the entire representational space),
      not merely distributional. This directly explains why MMD-based CaCLR fails:
      it optimizes the wrong measure of alignment. The resource-tier CKA gradient
      (0.60 > 0.48 > 0.36 at deep layers) mirrors the transfer AUROC gradient, providing
      a mechanistic explanation for why low-resource languages transfer worse — their
      deep-layer representations are more geometrically dissimilar from English.

    tables:
      - name: "Table 11: CKA Similarity — Languages × Layers"
        description: >
          Probed layers (rows) × 20 languages (columns, sorted by resource tier).
          Cells: CKA values. Clear gradient: high CKA at shallow layers, decreasing
          with depth. Resource-tier banding visible. Both models shown.
      - name: "Table 12: CKA vs MMD as Transfer Predictors"
        description: >
          Predictor comparison: CKA linear, CKA RBF, MMD, H-divergence proxy.
          Columns: Pearson r, R², p-value. CKA linear clearly dominant.
          Demonstrates geometric > distributional as explanation.

    figures_description:
      - "Figure: CKA heatmap — layers (y-axis) × languages (x-axis, sorted by transfer AUROC). Color intensity = CKA. Clear diagonal structure: high CKA co-occurs with high transfer AUROC. Visual demonstration of the CKA–transfer link."
      - "Figure: CKA vs transfer AUROC scatter — each point is a (layer, language) pair. Color: resource tier. Linear fit line with r=0.58. Contrasted with MMD vs transfer scatter (r=0.25) in adjacent panel. The visual gap between the two correlations is the paper's mechanistic argument."
      - "Figure: CKA depth profile — CKA vs layer depth for 3 representative languages (zh, tr, sw). Three curves showing parallel decline but at different levels. Annotated with corresponding transfer AUROC at each layer."

    analysis: >
      CKA analysis is the mechanistic backbone of the paper. It upgrades the contribution
      from "we measured that transfer fails at deep layers" to "we explain WHY transfer
      fails — geometric misalignment increases with depth, and this misalignment type
      (rotation/scaling) is specifically not addressable by distributional matching
      (MMD)." The CKA–transfer correlation (r=0.58) provides quantitative support, and
      the CKA vs MMD comparison (34% vs 6% variance explained) provides the critical
      distinction that makes the negative CaCLR result theoretically interpretable rather
      than just empirically observed. This transforms the paper from a measurement study
      to one with mechanistic insight.

  - name: "Linear Projection Sensitivity Analysis"
    plan_id: "plan_012"
    description: >
      Vary parallel pairs (10, 20, 50, 100, 200) for linear projection.
      Both models × 5 layers × 20 languages.
    expected_results:
      # ΔAUROC over zero-shot at each pair count (median across langs)
      pairs_10_delta_auroc_median: 0.012
      pairs_20_delta_auroc_median: 0.022
      pairs_50_delta_auroc_median: 0.030
      pairs_100_delta_auroc_median: 0.035
      pairs_200_delta_auroc_median: 0.036
      # Saturation point
      saturation_knee_point: 70
      pairs_for_90pct_max_improvement: 55
      pairs_for_95pct_max_improvement: 85
      # Variance reduction with more pairs
      pairs_10_std_across_langs: 0.025
      pairs_50_std_across_langs: 0.012
      pairs_100_std_across_langs: 0.008
      # Architecture consistency
      saturation_consistent_across_models: true
      qwen_saturation_knee: 65
      llama_saturation_knee: 75
    result_rationale: >
      Linear projection learns a rotation matrix mapping source-language representations
      to target-language space. The sample complexity for estimating a linear mapping
      in high-dimensional space (4096+ dims) is surprisingly low because: (a) the
      effective dimensionality of the correctness-relevant subspace is much lower than
      the full representation dimensionality — the probe operates in a low-rank subspace;
      (b) parallel pairs provide direct supervision on the mapping, unlike distributional
      matching which uses indirect statistical signals. With 10 pairs, the mapping is
      underdetermined but captures the dominant rotation component (+1.2pp). By 50 pairs,
      90% of the achievable improvement is captured as the major rotation/scaling axes
      are identified. The knee point at ~70 pairs and saturation by 100 pairs is
      consistent with the cross-lingual alignment literature (MUSE, VecMap) where
      bilingual dictionaries of 50–100 entries suffice for word-level alignment. The
      slight architecture difference in knee points (65 vs 75) reflects that Llama 4's
      representations may require slightly more pairs to estimate the rotation due to
      its MoE routing introducing more heterogeneity. The practical implication is clear:
      ~50-100 parallel pairs (trivially obtainable from GlobalMMLU train split) are
      sufficient to match or exceed CaCLR's entire training pipeline.

    tables:
      - name: "Table 13: Linear Projection — Sample Efficiency"
        description: >
          Pair counts (rows: 10, 20, 50, 100, 200) × summary statistics (median ΔAUROC,
          mean, std, min, max, % languages improved). Both models. Shows clear diminishing
          returns after 50 pairs.

    figures_description:
      - "Figure: Learning curve — x-axis: number of parallel pairs (log scale), y-axis: median ΔAUROC. Two curves (Qwen3, Llama4) with shaded ±1 std band. Annotated knee point. Horizontal dashed line: CaCLR-full ΔAUROC for comparison — linear projection surpasses CaCLR at just ~20 pairs."

    analysis: >
      Linear projection's sample efficiency is the constructive complement to CaCLR's
      negative result. The message: you don't need MMD-based distributional matching
      (which doesn't work anyway) — you just need ~50-100 parallel pairs and a linear
      mapping. This is practically actionable and theoretically consistent with the
      geometric explanation (linear projection learns the rotation that MMD cannot).
      The learning curve figure — showing linear projection surpassing CaCLR at ~20
      pairs — is one of the paper's most compelling visuals.

  - name: "Probing Control Tasks (Hewitt & Liang 2019)"
    plan_id: "plan_013"
    description: >
      Train probes on randomly permuted labels at each layer. Selectivity analysis
      across layers and languages.
    expected_results:
      # Control task AUROC
      control_auroc_en_median: 0.545
      control_auroc_en_range: [0.52, 0.58]
      control_auroc_noneng_median: 0.540
      # Selectivity (probe AUROC - control AUROC)
      selectivity_en_median: 0.265
      selectivity_en_range: [0.18, 0.31]
      selectivity_noneng_median_high_resource: 0.20
      selectivity_noneng_median_mid_resource: 0.16
      selectivity_noneng_median_low_resource: 0.10
      selectivity_min_across_all: 0.08
      selectivity_min_language: "sw"
      selectivity_min_layer: "layer_4"
      # All selectivities > 0 threshold
      all_selectivities_positive: true
      # Selectivity > 10pp threshold
      pct_above_10pp: 0.88
      pct_above_10pp_high_resource: 0.95
      pct_above_10pp_low_resource: 0.70
      # Layer pattern
      selectivity_peaks_at_mid_depth: true
      selectivity_peak_layer_pct_depth: 0.55
    result_rationale: >
      Control tasks with random labels test whether probe capacity (model expressiveness)
      alone can achieve high AUROC without genuine correctness signal. The control AUROC
      of ~0.54-0.55 (barely above chance at 0.50) confirms that logistic regression
      probes do not have sufficient capacity to memorize random label assignments in
      high-dimensional space — any AUROC above this baseline reflects genuine signal.
      English selectivity (median 0.265) is strong: the probe captures real correctness
      information 26.5pp above what capacity alone could achieve. Non-English selectivity
      decreases with resource tier because: (a) the correctness signal itself is weaker
      for languages with less pretraining data; (b) the cross-lingual transfer means
      probes must generalize from English-learned patterns, which is inherently harder
      for distant languages. Low-resource languages (sw, bn) show selectivity ~10pp,
      still positive but approaching the threshold where a reviewer might question
      signal quality. The 88% of language-layer combinations exceeding 10pp provides
      reasonable validation, but the 30% failure rate for low-resource languages at
      this threshold is a genuine limitation that the paper should acknowledge. Selectivity
      peaks at mid-depth (~55%) because shallow layers have weaker correctness signals
      (less processed) and very deep layers have stronger but more language-specific
      signals (high probe AUROC but also higher control AUROC due to richer features).

    tables:
      - name: "Table S4: Control Task Selectivity"
        description: >
          Supplementary. Languages (rows, grouped by resource tier) × representative
          layers (columns). Cells: selectivity (probe AUROC - control AUROC).
          Color-coded: green >15pp, yellow 10-15pp, orange 5-10pp. Shows resource-
          tier gradient in selectivity.

    figures_description:
      - "Figure: Selectivity by resource tier — box plots for HIGH, MID, LOW resource tiers. Shows decreasing median and increasing variance for lower-resource tiers. Dashed line at 10pp threshold. Most points above threshold but LOW tier shows some below."

    analysis: >
      Control tasks validate that probe AUROC reflects genuine correctness signal for
      the large majority of settings (88% above 10pp). The resource-tier gradient in
      selectivity is a limitation to acknowledge: for low-resource languages, probe
      signal quality is weaker, and conclusions about transfer should be interpreted
      with this caveat. This doesn't undermine the paper's core claims (which are about
      the mechanism of transfer failure, not about achieving high probe quality in
      every language) but sets appropriate epistemic bounds.

  - name: "Gemma 4 31B Dense Pareto Frontier"
    plan_id: "plan_008"
    description: >
      Third architecture for camera-ready. 60 layers, dense, FP16. Full Pareto frontier,
      20+ languages. Dense vs MoE contrast.
    expected_results:
      en_best_auroc: 0.80
      en_best_layer: 45
      zs_transfer_auroc_median: 0.69
      best_transfer_layer: 33
      pareto_rho_per_lang_median: -0.58
      zs_langs_above_0p65: 12
      # Dense vs MoE comparison
      pareto_rho_smoother_than_moe: true
      pareto_rho_std_across_langs_gemma: 0.12
      pareto_rho_std_across_langs_qwen: 0.16
      pareto_rho_std_across_langs_llama: 0.15
      cka_depth_decline_steeper_dense: true
      linear_proj_delta_median: 0.033
    result_rationale: >
      Gemma 4 31B Dense provides the critical dense-vs-MoE architectural contrast.
      As a dense model, every token passes through every layer (no routing), creating
      more uniform layer-to-layer transformations. This produces a smoother Pareto
      frontier (lower rho variance across languages: 0.12 vs 0.15-0.16 for MoE models)
      because the depth-transfer tradeoff is more consistent without routing-induced
      heterogeneity. The rho itself is slightly stronger negative (-0.58) because dense
      models show a cleaner monotonic decline in cross-lingual alignment with depth —
      MoE routing partially breaks this monotonicity by allowing some expert pathways
      to maintain cross-lingual features at deeper layers. CKA declines more steeply
      with depth in the dense model, confirming that MoE routing provides a modest
      buffer against geometric misalignment (different experts can specialize differently
      per language). English AUROC (0.80) is comparable to the larger MoE models despite
      smaller parameter count because the 31B dense architecture is parameter-efficient
      for representation quality. This is a P2 camera-ready experiment that strengthens
      the architecture-dependence claim from "two MoE models differ moderately" to
      "dense vs MoE is a qualitatively distinct contrast."

    tables:
      - name: "Table CR1: Three-Architecture Pareto Comparison"
        description: >
          Camera-ready. Architecture (rows: Qwen3-MoE, Llama4-MoE, Gemma4-Dense) ×
          key metrics (EN AUROC, ZS median, rho median, rho std, CKA slope, linear-proj Δ).
          Highlights dense vs MoE contrast in rho variance and CKA slope.

    figures_description:
      - "Figure: Three-panel Pareto frontier comparison — Qwen3-MoE, Llama4-MoE, Gemma4-Dense side-by-side. Dense model shows smoother, more monotonic frontier. Visual argument for architecture-dependence."

    analysis: >
      Camera-ready addition. The dense-vs-MoE contrast is the strongest architecture-
      dependence evidence: MoE routing introduces heterogeneity that partially buffers
      against geometric misalignment at deep layers, while dense models show cleaner
      depth-dependent degradation. This doesn't change the paper's conclusions but
      provides a more compelling architectural contrast than two MoE models alone.

  - name: "Extended Language Coverage (50+ Languages)"
    plan_id: "plan_009"
    description: >
      Expand from 20 to 50+ languages for camera-ready. Full GlobalMMLU/Belebele
      language sets.
    expected_results:
      total_languages: 52
      zs_langs_above_0p65: 28
      zs_median_auroc_52lang: 0.66
      zs_auroc_range: [0.50, 0.74]
      new_low_resource_langs_below_0p55: ["am", "my", "zu", "sn", "rw"]
      resource_tier_gradient_replicates: true
      pareto_rho_median_52lang: -0.49
      linear_proj_delta_median_52lang: 0.031
      # Tail behavior
      tail_langs_below_0p55_count: 8
      tail_langs_above_0p70_count: 12
    result_rationale: >
      Expanding to 52 languages adds many more low-resource and typologically diverse
      languages. The median AUROC drops slightly (0.66 vs 0.70 for the curated 20)
      because the additional languages are disproportionately low-resource. Five
      extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda)
      fall below 0.55, approaching chance performance — these languages have minimal
      pretraining representation in both models. The resource-tier gradient continues
      to hold and becomes even more pronounced with the extended tail. Pareto rho weakens
      slightly (-0.49) because many of the new languages show weak, noisy correlations
      due to low base probe quality. Linear projection improvement remains consistent
      (+3.1pp), confirming the geometric correction generalizes beyond the curated
      language set. The practical message: probe-based cross-lingual calibration is
      viable for ~28/52 languages (54%) without any target-language data, and linear
      projection extends this to ~35/52 (67%). The remaining ~17 languages need
      language-specific probes or alternative approaches.

    tables:
      - name: "Table CR2: Extended Language Coverage — 52 Languages"
        description: >
          Camera-ready. Full 52-language results sorted by zero-shot AUROC. Columns:
          language, family, resource tier, ZS AUROC, linear-proj AUROC, few-shot-100
          AUROC. Grouped into tiers: >0.70 (strong transfer), 0.65-0.70 (viable),
          0.55-0.65 (marginal), <0.55 (failed).

    figures_description:
      - "Figure: Language coverage map — world map with countries colored by best zero-shot transfer AUROC. Visual demonstration of where probe-based calibration works and fails geographically."

    analysis: >
      Camera-ready extension. The 52-language analysis adds scale but the median-tier
      conclusion is clear: probe-based cross-lingual calibration works for a majority
      but not all languages, and the resource-tier gradient is the dominant predictor of
      success. This sets realistic expectations for practitioners and motivates future
      work on low-resource language probe training.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c4f2687-1b3c-42b9-b4f1-e2c29d52fd16",
  "isSidechain": false,
  "requestId": "req_011CbESz58acc2FHjvhDfK1J",
  "type": "assistant",
  "uuid": "959eef2c-f29b-4804-b376-5efb8d74ed71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F85TP8qUz7pkGv58DNa81Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13426,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16651,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13426
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：CaCLR consistency loss is inert (Path B); but Pareto frontier is solid, linear projection is surprisingly strong, and CKA/decomposition provide genuine m…",
  "leafUuid": "959eef2c-f29b-4804-b376-5efb8d74ed71",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier median analysis for cross-lingual correctness probe calibration",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：CaCLR consistency loss is inert (Path B); but Pareto frontier is solid, linear projection is surprisingly strong, and CKA/decomposition provide genuine m…",
  "leafUuid": "959eef2c-f29b-4804-b376-5efb8d74ed71",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier median analysis for cross-lingual correctness probe calibration",
  "sessionId": "1af4e3b6-d3bb-4dd0-b7cf-1e6c06b8e59a"
}
```

---
