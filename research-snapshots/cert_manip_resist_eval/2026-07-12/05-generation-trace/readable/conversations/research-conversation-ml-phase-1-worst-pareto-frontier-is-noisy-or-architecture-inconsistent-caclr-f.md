# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decompo

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/c3372ce2-16de-4b98-b026-560c840f0560.jsonl`
- **Structured JSON:** [`613ad7e80b73a8dd6f23.json`](../../sessions/61/613ad7e80b73a8dd6f23.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:31:44.566Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:31:44.566Z",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decomposition is inconclusive; but cross-lingual probing viability data and the mean-shift invariance proof are still novel contributions\n核心假设：[\"Pareto frontier exists qualitatively on one architecture but is weak or reversed on the other — architecture-dependent claim becomes 'architecture-specific, non-generalizable'\", 'CaCLR fully fails (both α and β inert or harmful) — neither calibration loss nor consistency loss improves over zero-shot', 'CKA correlation with transfer is weak (r < 0.45) — mechanistic explanation is suggestive but not convincing', 'Linear projection helps but inconsistently: works for mid/high-resource languages, fails for low-resource (insufficient parallel quality)', 'Decomposition is inconclusive: difficulty projection sometimes helps, sometimes hurts, no clear pattern by resource tier', 'Zero-shot transfer AUROC is mediocre — only high-resource languages reliably above 0.65, many languages near 0.55-0.60', 'Control tasks reveal that some high AUROC is probe capacity artifact in low-resource settings (selectivity < 8pp)', 'Orthogonality holds broadly but with enough outliers (cosine > 0.15 for some langs) to weaken the universality claim']\n关键指标范围：{'en_best_auroc_large_model': [0.73, 0.78], 'zs_transfer_auroc_median_20lang': [0.56, 0.65], 'pareto_rho_per_lang_median': [-0.4, -0.1], 'pareto_rho_sign_consistency_across_langs': [0.5, 0.7], 'caclr_beta_delta_auroc_over_alpha_only': [-0.02, 0.005], 'caclr_full_delta_auroc_over_zeroshot_median': [-0.01, 0.01], 'linear_proj_delta_auroc_over_zeroshot_median': [0.0, 0.03], 'linear_proj_pct_langs_improved': [0.45, 0.65], 'decomposition_transfer_delta_after_difficulty_removal': [-0.01, 0.01], 'cka_transfer_pearson_r': [0.15, 0.45], 'orthogonality_cosine_max_across_langs': [0.1, 0.2], 'control_task_selectivity_min': [0.03, 0.1], 'zs_langs_above_0p65_out_of_20': [5, 10], 'sw_bn_low_resource_zs_auroc': [0.5, 0.56], 'ece_reduction_vs_temp_scaling_median': [-0.01, 0.01]}\n叙事方向：Reframe as field-level empirical survey: \"Does probe-based calibration work beyond English? A systematic investigation.\" Drop CaCLR from claims entirely — relegate to one paragraph as attempted-and-failed. New claim structure: (1) mean-shift rank-invariance theorem (novel formal result with proof, universally validated, explains Xiao et al. vs our divergent findings), (2) resource-tier taxonomy of cross-lingual probe transferability (high-resource transfers, mid-resource is marginal, low-resource fails — first quantification across 20 languages), (3) practical recommendation: few-shot (25-100 labels) is the viable path, not alignment methods — closing the zero-label dream for low-resource languages. The paper becomes a \"sobering empirical reality check\" for the probe-based calibration line. The mean-shift proof and the 20-language empirical map are still novel. Orthogonality and Pareto data are reported but not overclaimed. Lean into the negative-results angle: \"we tested every reasonable zero-label approach and none works reliably — here's what does work (few-shot) and why (geometric misalignment is language-pair specific).\" Target: borderline at EACL, requires very clean writing and strong related-work positioning.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\nfocus: Re-dream after first Dream review (3/6). Key framing changes since last dream: (1) CaCLR now has conditional narrative — Path A method contribution if consistency loss works, Path B principled negative result with geometric misalignment explanation if it doesn't; (2) mean-shift rank-invariance as formal theoretical contribution (proof + experimental validation); (3) CKA mechanistic analysis added (plan_011) to explain WHY transfer fails; (4) probing control tasks (plan_013, Hewitt & Liang 2019); (5) linear projection sensitivity analysis (plan_012); (6) statistical rigor: bootstrap CIs + paired tests + Cohen's d as cross-cutting requirement; (7) per-language Spearman rho for Pareto frontier; (8) AUROC threshold sensitivity analysis; (9) expanded related work coverage (domain adaptation theory, alignment literature, conformal prediction); (10) decomposition grid justified (10 langs × 8 layers covers 3 resource tiers × major families). Verify these changes lift score to best ≥ weak accept and median ≥ borderline.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    INT8 weight quantization. Report per-language Spearman rho (depth vs transfer\n    AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: Needs 2× RTX 6000 PRO 96GB at INT8.\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations (GlobalMMLU train split translations,\n    not test items). Compare vs zero-shot, mean-shift, linear projection, few-shot\n    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter\n    tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer\n    results (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative).\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at\n    5 representative layers for Llama 4 Scout on 5% random subset. Validates that\n    INT8 quantization doesn''t distort correctness signals.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Correlate CKA with transfer AUROC to provide mechanistic explanation\n    for the Pareto frontier. Explains WHY deeper layers transfer worse (lower cross-lingual\n    CKA). If CKA shows geometric misalignment (not just distributional shift), this\n    explains why MMD-based CaCLR fails but linear projection succeeds.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Dream review D5: \"no mechanistic explanation\" was flagged [M][W]. CKA upgrades\n    paper from measurement to insight. CPU-bound on cached activations. Reviewer suggests:\n    pilot on MVP activations (mvp_001/mvp_003, 6 langs × 8-9 layers × 2 models) before\n    full-scale run. Pilot is zero-cost and validates CKA pipeline informativeness.\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique.'\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: RUNNING\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T20:31:44.569Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:31:44.569Z",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-20T20:31:44.602Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decomposition is inconclusive; but cross-lingual probing viability data and the mean-shift invariance proof are still novel contributions
核心假设：["Pareto frontier exists qualitatively on one architecture but is weak or reversed on the other — architecture-dependent claim becomes 'architecture-specific, non-generalizable'", 'CaCLR fully fails (both α and β inert or harmful) — neither calibration loss nor consistency loss improves over zero-shot', 'CKA correlation with transfer is weak (r < 0.45) — mechanistic explanation is suggestive but not convincing', 'Linear projection helps but inconsistently: works for mid/high-resource languages, fails for low-resource (insufficient parallel quality)', 'Decomposition is inconclusive: difficulty projection sometimes helps, sometimes hurts, no clear pattern by resource tier', 'Zero-shot transfer AUROC is mediocre — only high-resource languages reliably above 0.65, many languages near 0.55-0.60', 'Control tasks reveal that some high AUROC is probe capacity artifact in low-resource settings (selectivity < 8pp)', 'Orthogonality holds broadly but with enough outliers (cosine > 0.15 for some langs) to weaken the universality claim']
关键指标范围：{'en_best_auroc_large_model': [0.73, 0.78], 'zs_transfer_auroc_median_20lang': [0.56, 0.65], 'pareto_rho_per_lang_median': [-0.4, -0.1], 'pareto_rho_sign_consistency_across_langs': [0.5, 0.7], 'caclr_beta_delta_auroc_over_alpha_only': [-0.02, 0.005], 'caclr_full_delta_auroc_over_zeroshot_median': [-0.01, 0.01], 'linear_proj_delta_auroc_over_zeroshot_median': [0.0, 0.03], 'linear_proj_pct_langs_improved': [0.45, 0.65], 'decomposition_transfer_delta_after_difficulty_removal': [-0.01, 0.01], 'cka_transfer_pearson_r': [0.15, 0.45], 'orthogonality_cosine_max_across_langs': [0.1, 0.2], 'control_task_selectivity_min': [0.03, 0.1], 'zs_langs_above_0p65_out_of_20': [5, 10], 'sw_bn_low_resource_zs_auroc': [0.5, 0.56], 'ece_reduction_vs_temp_scaling_median': [-0.01, 0.01]}
叙事方向：Reframe as field-level empirical survey: "Does probe-based calibration work beyond English? A systematic investigation." Drop CaCLR from claims entirely — relegate to one paragraph as attempted-and-failed. New claim structure: (1) mean-shift rank-invariance theorem (novel formal result with proof, universally validated, explains Xiao et al. vs our divergent findings), (2) resource-tier taxonomy of cross-lingual probe transferability (high-resource transfers, mid-resource is marginal, low-resource fails — first quantification across 20 languages), (3) practical recommendation: few-shot (25-100 labels) is the viable path, not alignment methods — closing the zero-label dream for low-resource languages. The paper becomes a "sobering empirical reality check" for the probe-based calibration line. The mean-shift proof and the 20-language empirical map are still novel. Orthogonality and Pareto data are reported but not overclaimed. Lean into the negative-results angle: "we tested every reasonable zero-label approach and none works reliably — here's what does work (few-shot) and why (geometric misalignment is language-pair specific)." Target: borderline at EACL, requires very clean writing and strong related-work positioning.

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
  "promptId": "f5a9dccd-f6bd-4a96-b7c0-602929af4008",
  "type": "user",
  "uuid": "0dfc9ffb-615f-41f6-97c1-e615d88ad70e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:31:44.601Z_

```json
{
  "parentUuid": "0dfc9ffb-615f-41f6-97c1-e615d88ad70e",
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
  "uuid": "2ef23f26-b0db-4f6e-b116-91f730b71e22",
  "timestamp": "2026-05-20T20:31:44.601Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:31:44.601Z_

```json
{
  "parentUuid": "2ef23f26-b0db-4f6e-b116-91f730b71e22",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1129e0ba-5e52-4b2d-81d6-db1c350d3662",
  "timestamp": "2026-05-20T20:31:44.601Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decomposition is inconclusive; but cross-lingual probing viability data and the mean-s…",
  "leafUuid": "1129e0ba-5e52-4b2d-81d6-db1c350d3662",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Probe-based calibration fails multilingually—few-shot and mechanistic insights",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Assistant

_source line 8 · 2026-05-20T20:31:49.674Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for the "worst" tier scenario for every planned experiment in their experiment plan. I need to produce a comprehensive YAML block with predicted results, rationales, tables, figures, and analysis for each experiment.

Let me go through each planned experiment and generate worst-tier predictions based on the defined worst-tier parameters and narrative direction.

Let me first read the experiment plan and any other relevant files to make sure I have the full context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1129e0ba-5e52-4b2d-81d6-db1c350d3662",
  "isSidechain": false,
  "requestId": "req_011CbETRG5bXz2GV6qi6u2hT",
  "type": "assistant",
  "uuid": "a5f80096-4bfb-4ec0-a4fb-a1a63b0bc110",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1wBJbh2MdLzmGZbjiU9gg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13555,
      "cache_read_input_tokens": 11841,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 211,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13555
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

_source line 9 · 2026-05-20T20:31:50.857Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016LtJJQcTigZH8fNW1KDdmK`</summary>

```json
{
  "pattern": "**/*.{yaml,yml,md}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5f80096-4bfb-4ec0-a4fb-a1a63b0bc110",
  "isSidechain": false,
  "requestId": "req_011CbETRG5bXz2GV6qi6u2hT",
  "type": "assistant",
  "uuid": "00e779a5-3f7c-4d8c-85cb-38f6d66227b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1wBJbh2MdLzmGZbjiU9gg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13555,
      "cache_read_input_tokens": 11841,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 211,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13555
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

_source line 10 · 2026-05-20T20:31:50.877Z_

<details><summary>↩ Tool result · `toolu_016LtJJQcTigZH8fNW1KDdmK`</summary>

```text
config/approvals.yaml
config/backend.yaml
config/feishu.yaml
.claude/sessions/no_project_9d2a9208/CLAUDE.md
.claude/sessions/no_project_9d2a9208/AGENTS.md
workspace.yaml
config/venue_registry.yaml
config/venue_rules/corl-2026.yaml
config/venue_rules/emnlp-2026.yaml
idea_generator/ideas.yaml
projects/xling_calib_direction/literature_map.yaml
projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/AGENTS.md
projects/xling_calib_direction/distill_tmp/karandikar2021sbece.yaml
projects/xling_calib_direction/distill_tmp/miao2026closing.yaml
projects/xling_calib_direction/distill_tmp/civelli2026shared.yaml
projects/xling_calib_direction/distill_tmp/confidence_manifold2026.yaml
projects/xling_calib_direction/distill_tmp/xiao2025knowledge.yaml
projects/xling_calib_direction/distill_tmp/joshi2025calibration.yaml
projects/xling_calib_direction/distill_tmp/khanmohammadi2025ccps.yaml
projects/xling_calib_direction/distill_tmp/liu2025middle.yaml
projects/xling_calib_direction/distill_tmp/ji2025calibrating.yaml
projects/xling_calib_direction/distill_tmp/ravisankar2026dali.yaml
projects/xling_calib_direction/distill_tmp/zhou2025lace.yaml
projects/xling_calib_direction/distill_tmp/miao2026coral.yaml
config/resources.yaml
skills/projects/xling_calib_direction/distilled-research.skill.md
skills/projects/xling_calib_direction/distilled-writing.skill.md
config/secrets/xling_calib_direction/manifest.yaml
projects/xling_calab_direction/registry.yaml
projects/xling_calib_direction/docs/IDEA_BRIEF.md
projects/xling_calib_direction/report.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md
config/projects/xling_calib_direction.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_report.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md
projects/xling_calib_direction/.claude/sessions/review_reviewer_1_4b9e3221/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/review_reviewer_1_4b9e3221/AGENTS.md
projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/AGENTS.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_report.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/meta.yaml
projects/xling_calib_direction/artifacts/review_issues.yaml
projects/xling_calib_direction/artifacts/review_reports/round_0.md
projects/xling_calib_direction/.claude/sessions/review_director_91c72a1c/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/review_director_91c72a1c/AGENTS.md
projects/xling_calib_direction/dream_registry.yaml
projects/xling_calib_direction/memory.md
projects/xling_calib_direction/mistakes.yaml
projects/xling_calib_direction/registry.yaml
projects/xling_calib_direction/.claude/sessions/director_a0a38807/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/director_a0a38807/AGENTS.md
projects/xling_calib_direction/.claude/sessions/reviewer_b0408cba/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/reviewer_b0408cba/AGENTS.md
projects/xling_calib_direction/paper_framing.md
projects/xling_calib_direction/experiment_plan.yaml
.claude/CLAUDE.md
AGENTS.md
projects/xling_calib_direction/.claude/CLAUDE.md
projects/xling_calib_direction/AGENTS.md
projects/xling_calib_direction/.claude/sessions/agent_3e57a809/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/agent_3e57a809/AGENTS.md
projects/xling_calib_direction/decisions.yaml
projects/xling_calib_direction/ROADMAP.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00e779a5-3f7c-4d8c-85cb-38f6d66227b4",
  "isSidechain": false,
  "promptId": "f5a9dccd-f6bd-4a96-b7c0-602929af4008",
  "type": "user",
  "uuid": "8ea6039e-c357-4480-b2c0-d14b97321f6c",
  "toolUseResult": {
    "filenames": [
      "config/approvals.yaml",
      "config/backend.yaml",
      "config/feishu.yaml",
      ".claude/sessions/no_project_9d2a9208/CLAUDE.md",
      ".claude/sessions/no_project_9d2a9208/AGENTS.md",
      "workspace.yaml",
      "config/venue_registry.yaml",
      "config/venue_rules/corl-2026.yaml",
      "config/venue_rules/emnlp-2026.yaml",
      "idea_generator/ideas.yaml",
      "projects/xling_calib_direction/literature_map.yaml",
      "projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/AGENTS.md",
      "projects/xling_calib_direction/distill_tmp/karandikar2021sbece.yaml",
      "projects/xling_calib_direction/distill_tmp/miao2026closing.yaml",
      "projects/xling_calib_direction/distill_tmp/civelli2026shared.yaml",
      "projects/xling_calib_direction/distill_tmp/confidence_manifold2026.yaml",
      "projects/xling_calib_direction/distill_tmp/xiao2025knowledge.yaml",
      "projects/xling_calib_direction/distill_tmp/joshi2025calibration.yaml",
      "projects/xling_calib_direction/distill_tmp/khanmohammadi2025ccps.yaml",
      "projects/xling_calib_direction/distill_tmp/liu2025middle.yaml",
      "projects/xling_calib_direction/distill_tmp/ji2025calibrating.yaml",
      "projects/xling_calib_direction/distill_tmp/ravisankar2026dali.yaml",
      "projects/xling_calib_direction/distill_tmp/zhou2025lace.yaml",
      "projects/xling_calib_direction/distill_tmp/miao2026coral.yaml",
      "config/resources.yaml",
      "skills/projects/xling_calib_direction/distilled-research.skill.md",
      "skills/projects/xling_calib_direction/distilled-writing.skill.md",
      "config/secrets/xling_calib_direction/manifest.yaml",
      "projects/xling_calab_direction/registry.yaml",
      "projects/xling_calib_direction/docs/IDEA_BRIEF.md",
      "projects/xling_calib_direction/report.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md",
      "config/projects/xling_calib_direction.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_report.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md",
      "projects/xling_calib_direction/.claude/sessions/review_reviewer_1_4b9e3221/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/review_reviewer_1_4b9e3221/AGENTS.md",
      "projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/AGENTS.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_report.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/meta.yaml",
      "projects/xling_calib_direction/artifacts/review_issues.yaml",
      "projects/xling_calib_direction/artifacts/review_reports/round_0.md",
      "projects/xling_calib_direction/.claude/sessions/review_director_91c72a1c/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/review_director_91c72a1c/AGENTS.md",
      "projects/xling_calib_direction/dream_registry.yaml",
      "projects/xling_calib_direction/memory.md",
      "projects/xling_calib_direction/mistakes.yaml",
      "projects/xling_calib_direction/registry.yaml",
      "projects/xling_calib_direction/.claude/sessions/director_a0a38807/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/director_a0a38807/AGENTS.md",
      "projects/xling_calib_direction/.claude/sessions/reviewer_b0408cba/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/reviewer_b0408cba/AGENTS.md",
      "projects/xling_calib_direction/paper_framing.md",
      "projects/xling_calib_direction/experiment_plan.yaml",
      ".claude/CLAUDE.md",
      "AGENTS.md",
      "projects/xling_calib_direction/.claude/CLAUDE.md",
      "projects/xling_calib_direction/AGENTS.md",
      "projects/xling_calib_direction/.claude/sessions/agent_3e57a809/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/agent_3e57a809/AGENTS.md",
      "projects/xling_calib_direction/decisions.yaml",
      "projects/xling_calib_direction/ROADMAP.md"
    ],
    "durationMs": 12,
    "numFiles": 72,
    "truncated": false
  },
  "sourceToolAssistantUUID": "00e779a5-3f7c-4d8c-85cb-38f6d66227b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:31:53.706Z_

<details open><summary>🔧 Tool call — Read · `toolu_019Ve38QsZn8UkPCqxYsxn2F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ea6039e-c357-4480-b2c0-d14b97321f6c",
  "isSidechain": false,
  "requestId": "req_011CbETRiwsGPd9ctxeZFfxv",
  "type": "assistant",
  "uuid": "99283016-db97-4cd7-85b7-bc61d802feb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBKXnGFU1Y6jkcSU5y9CPf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1804,
      "cache_read_input_tokens": 25396,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 25396,
          "cache_creation_input_tokens": 1804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1804
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

_source line 12 · 2026-05-20T20:31:53.722Z_

<details><summary>↩ Tool result · `toolu_019Ve38QsZn8UkPCqxYsxn2F`</summary>

```text
1	experiments:
2	  # === P0: Core submission (must complete for EACL 2027 ARR Aug 3) ===
3	
4	  - id: plan_001
5	    claim: 1
6	    description: >
7	      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8):
8	      extract activations at every 4th layer (24 probed layers),
9	      20 typologically diverse languages, train English correctness probes
10	      (logistic regression + 2-layer MLP), evaluate 5 transfer conditions
11	      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).
12	      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.
13	    priority: P0
14	    gpu_budget_hours: 80
15	    deps: []
16	    notes: "Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request."
17	
18	  - id: plan_002
19	    claim: 1
20	    description: >
21	      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8):
22	      extract activations at every 4th layer (12 probed layers),
23	      20 languages, 5 transfer conditions. INT8 weight quantization.
24	      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.
25	    priority: P0
26	    gpu_budget_hours: 40
27	    deps: []
28	    notes: "Needs 2× RTX 6000 PRO 96GB at INT8."
29	
30	  - id: plan_003
31	    claim: 3
32	    description: >
33	      CaCLR implementation and comparative evaluation:
34	      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD distance).
35	      Train CaCLR probes using English labels + unlabeled parallel activations
36	      (GlobalMMLU train split translations, not test items).
37	      Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100)
38	      across full Pareto frontier for both models × 20 languages.
39	      Hyperparameter tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0).
40	      Report fixed-layer results (50% depth + EN-optimal) alongside per-language oracle.
41	    priority: P0
42	    gpu_budget_hours: 20
43	    deps: [plan_001, plan_002]
44	    notes: >
45	      CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS 2021.
46	      L_consistency uses Maximum Mean Discrepancy (MMD).
47	      If β sweep shows inert consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional narrative).
48	
49	  - id: plan_004
50	    claim: 2
51	    description: >
52	      Difficulty-controlled ablation: train IRT difficulty probes (Ridge regression
53	      on human difficulty scores per Civelli et al.), project out difficulty direction
54	      from activations, retrain correctness probes on residuals, evaluate transfer.
55	      10 representative languages × 8 representative layers per model (20-90% depth).
56	    priority: P0
57	    gpu_budget_hours: 15
58	    deps: [plan_001, plan_002]
59	    notes: >
60	      Need IRT difficulty scores from GlobalMMLU or external source.
61	      Grid justification (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn)
62	      × major language families. 8 layers span 20-90% depth at uniform intervals.
63	      Reduced grid is sufficient because decomposition tests a qualitative hypothesis
64	      (does projecting out difficulty help or hurt?), not a per-language quantitative claim.
65	      Include random-direction control to rule out dimensionality-reduction artifacts.
66	
67	  # === Cross-cutting requirement (Dream review D1) ===
68	  # All experiments must include: bootstrap CIs (1000 resamples),
69	  # paired permutation tests for key comparisons, Cohen's d for effect sizes.
70	  # Report GlobalMMLU sample sizes per language.
71	  # AUROC threshold sensitivity analysis (0.55/0.60/0.65/0.70/0.75) for pass/fail reporting.
72	
73	  # === P1: Important for strong submission ===
74	
75	  - id: plan_005
76	    claim: 4
77	    description: >
78	      Cross-lingual orthogonality analysis: extract verbalized confidence direction
79	      (prompt model for confidence score, fit probe), compute cosine similarity
80	      with correctness direction across 20 languages × 2 architectures.
81	      Analyze by resource tier (high/mid/low) and language family.
82	    priority: P1
83	    gpu_budget_hours: 10
84	    deps: [plan_001, plan_002]
85	
86	  - id: plan_006
87	    claim: 1
88	    description: >
89	      Probe complexity comparison: logistic regression vs 2-layer MLP
90	      at each probed layer for both models. Compare English accuracy,
91	      cross-lingual transfer degradation, and calibration quality.
92	      Test hypothesis: linear probes transfer better cross-lingually.
93	    priority: P1
94	    gpu_budget_hours: 5
95	    deps: [plan_001, plan_002]
96	    notes: "CPU-bound, uses cached activations."
97	
98	  - id: plan_007
99	    claim: 1
100	    description: >
101	      Additional benchmark evaluation: evaluate best probes + CaCLR
102	      on Belebele (20 languages) and MMLU-ProX (20 languages).
103	      Validates generalization beyond MMLU/GlobalMMLU.
104	    priority: P1
105	    gpu_budget_hours: 30
106	    deps: [plan_001, plan_002, plan_003]
107	
108	  - id: plan_010
109	    claim: 1
110	    description: >
111	      INT8 validation ablation: compare INT8 vs FP16 probing results
112	      at 5 representative layers for Llama 4 Scout on 5% random subset.
113	      Validates that INT8 quantization doesn't distort correctness signals.
114	    priority: P1
115	    gpu_budget_hours: 5
116	    deps: [plan_002]
117	
118	  - id: plan_011
119	    claim: [1, 4]
120	    description: >
121	      CKA cross-lingual representation similarity analysis:
122	      compute CKA (linear kernel) between English and each target language
123	      at every probed layer for both models. Full-scale validation of pilot finding:
124	      correctness direction is a robust low-dimensional subspace feature that persists
125	      despite global CKA decline. Transfer collapses only at critical CKA threshold (~0.35).
126	      Report CKA × layer × language heatmaps, CKA vs transfer degradation
127	      ((EN_AUROC - target_AUROC) / EN_AUROC) correlation per language to isolate
128	      alignment effect from probe quality, and critical threshold analysis.
129	    priority: P1
130	    gpu_budget_hours: 5
131	    deps: [plan_001, plan_002]
132	    notes: >
133	      CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).
134	      Key finding: CKA vs AUROC negatively correlated (rho=-0.16 overall, hi rho=-0.79 sig,
135	      sw rho=-0.88 sig). Correctness signal is robust to global representation divergence.
136	      Original hypothesis ("low CKA → bad transfer") REVISED to threshold model.
137	      Full-scale run validates at 20 languages × 24/12 layers × 2 large models.
138	
139	  - id: plan_012
140	    claim: 1
141	    description: >
142	      Linear projection sensitivity analysis: vary number of parallel
143	      pairs (10, 20, 50, 100, 200) for linear projection transfer.
144	      Determines minimum data requirement for this surprisingly strong baseline.
145	      Both models × 5 representative layers × 20 languages.
146	    priority: P1
147	    gpu_budget_hours: 2
148	    deps: [plan_001, plan_002]
149	    notes: "CPU-bound, uses cached activations. Dream review D11."
150	
151	  - id: plan_013
152	    claim: 1
153	    description: >
154	      Probing control tasks (Hewitt & Liang 2019): train probes on
155	      randomly permuted labels at each layer. Compare selectivity
156	      (probe AUROC - control AUROC) across layers and languages.
157	      Validates that high AUROC reflects genuine correctness direction,
158	      not memorized dataset artifacts or probe capacity.
159	    priority: P1
160	    gpu_budget_hours: 2
161	    deps: [plan_001, plan_002]
162	    notes: "CPU-bound. Dream review D22: probing methodology critique."
163	
164	  # === P2: Camera-ready extension ===
165	
166	  - id: plan_008
167	    claim: 1
168	    description: >
169	      Gemma 4 31B Dense (60 layers, dense, FP16): third architecture
170	      for camera-ready. Full Pareto frontier, 20+ languages.
171	      Provides dense vs MoE architectural contrast.
172	    priority: P2
173	    gpu_budget_hours: 30
174	    deps: []
175	
176	  - id: plan_009
177	    claim: 1
178	    description: >
179	      Extended language coverage: expand from 20 to 50+ languages
180	      for camera-ready. Leverages GlobalMMLU/Belebele full language sets.
181	    priority: P2
182	    gpu_budget_hours: 50
183	    deps: [plan_001, plan_002]
184	
185	  # === MVP experiments (completed/running) ===
186	
187	  - id: mvp_validation
188	    claim: 1
189	    description: "MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift"
190	    priority: P0
191	    registry_id: mvp_001
192	    gpu_budget_hours: 2
193	    deps: []
194	
195	  - id: mvp_complementary
196	    claim: 1
197	    description: "MVP robustness: complementary layer set (2,6,10,14,18,22,26)"
198	    priority: P1
199	    registry_id: mvp_002
200	    gpu_budget_hours: 2
201	    deps: [mvp_validation]
202	
203	  - id: mvp_llama_control
204	    claim: 1
205	    description: "MVP cross-architecture: Llama-3.1-8B control experiment"
206	    priority: P1
207	    registry_id: mvp_003
208	    gpu_budget_hours: 3
209	    deps: [mvp_validation]
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99283016-db97-4cd7-85b7-bc61d802feb4",
  "isSidechain": false,
  "promptId": "f5a9dccd-f6bd-4a96-b7c0-602929af4008",
  "type": "user",
  "uuid": "7c537a5a-2e6a-46d5-9f82-8cd4106ca711",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml",
      "content": "experiments:\n  # === P0: Core submission (must complete for EACL 2027 ARR Aug 3) ===\n\n  - id: plan_001\n    claim: 1\n    description: >\n      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8):\n      extract activations at every 4th layer (24 probed layers),\n      20 typologically diverse languages, train English correctness probes\n      (logistic regression + 2-layer MLP), evaluate 5 transfer conditions\n      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\n      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n    priority: P0\n    gpu_budget_hours: 80\n    deps: []\n    notes: \"Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\"\n\n  - id: plan_002\n    claim: 1\n    description: >\n      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8):\n      extract activations at every 4th layer (12 probed layers),\n      20 languages, 5 transfer conditions. INT8 weight quantization.\n      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n    priority: P0\n    gpu_budget_hours: 40\n    deps: []\n    notes: \"Needs 2× RTX 6000 PRO 96GB at INT8.\"\n\n  - id: plan_003\n    claim: 3\n    description: >\n      CaCLR implementation and comparative evaluation:\n      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD distance).\n      Train CaCLR probes using English labels + unlabeled parallel activations\n      (GlobalMMLU train split translations, not test items).\n      Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100)\n      across full Pareto frontier for both models × 20 languages.\n      Hyperparameter tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0).\n      Report fixed-layer results (50% depth + EN-optimal) alongside per-language oracle.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [plan_001, plan_002]\n    notes: >\n      CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS 2021.\n      L_consistency uses Maximum Mean Discrepancy (MMD).\n      If β sweep shows inert consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional narrative).\n\n  - id: plan_004\n    claim: 2\n    description: >\n      Difficulty-controlled ablation: train IRT difficulty probes (Ridge regression\n      on human difficulty scores per Civelli et al.), project out difficulty direction\n      from activations, retrain correctness probes on residuals, evaluate transfer.\n      10 representative languages × 8 representative layers per model (20-90% depth).\n    priority: P0\n    gpu_budget_hours: 15\n    deps: [plan_001, plan_002]\n    notes: >\n      Need IRT difficulty scores from GlobalMMLU or external source.\n      Grid justification (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn)\n      × major language families. 8 layers span 20-90% depth at uniform intervals.\n      Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n      (does projecting out difficulty help or hurt?), not a per-language quantitative claim.\n      Include random-direction control to rule out dimensionality-reduction artifacts.\n\n  # === Cross-cutting requirement (Dream review D1) ===\n  # All experiments must include: bootstrap CIs (1000 resamples),\n  # paired permutation tests for key comparisons, Cohen's d for effect sizes.\n  # Report GlobalMMLU sample sizes per language.\n  # AUROC threshold sensitivity analysis (0.55/0.60/0.65/0.70/0.75) for pass/fail reporting.\n\n  # === P1: Important for strong submission ===\n\n  - id: plan_005\n    claim: 4\n    description: >\n      Cross-lingual orthogonality analysis: extract verbalized confidence direction\n      (prompt model for confidence score, fit probe), compute cosine similarity\n      with correctness direction across 20 languages × 2 architectures.\n      Analyze by resource tier (high/mid/low) and language family.\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan_001, plan_002]\n\n  - id: plan_006\n    claim: 1\n    description: >\n      Probe complexity comparison: logistic regression vs 2-layer MLP\n      at each probed layer for both models. Compare English accuracy,\n      cross-lingual transfer degradation, and calibration quality.\n      Test hypothesis: linear probes transfer better cross-lingually.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [plan_001, plan_002]\n    notes: \"CPU-bound, uses cached activations.\"\n\n  - id: plan_007\n    claim: 1\n    description: >\n      Additional benchmark evaluation: evaluate best probes + CaCLR\n      on Belebele (20 languages) and MMLU-ProX (20 languages).\n      Validates generalization beyond MMLU/GlobalMMLU.\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [plan_001, plan_002, plan_003]\n\n  - id: plan_010\n    claim: 1\n    description: >\n      INT8 validation ablation: compare INT8 vs FP16 probing results\n      at 5 representative layers for Llama 4 Scout on 5% random subset.\n      Validates that INT8 quantization doesn't distort correctness signals.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [plan_002]\n\n  - id: plan_011\n    claim: [1, 4]\n    description: >\n      CKA cross-lingual representation similarity analysis:\n      compute CKA (linear kernel) between English and each target language\n      at every probed layer for both models. Full-scale validation of pilot finding:\n      correctness direction is a robust low-dimensional subspace feature that persists\n      despite global CKA decline. Transfer collapses only at critical CKA threshold (~0.35).\n      Report CKA × layer × language heatmaps, CKA vs transfer degradation\n      ((EN_AUROC - target_AUROC) / EN_AUROC) correlation per language to isolate\n      alignment effect from probe quality, and critical threshold analysis.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [plan_001, plan_002]\n    notes: >\n      CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n      Key finding: CKA vs AUROC negatively correlated (rho=-0.16 overall, hi rho=-0.79 sig,\n      sw rho=-0.88 sig). Correctness signal is robust to global representation divergence.\n      Original hypothesis (\"low CKA → bad transfer\") REVISED to threshold model.\n      Full-scale run validates at 20 languages × 24/12 layers × 2 large models.\n\n  - id: plan_012\n    claim: 1\n    description: >\n      Linear projection sensitivity analysis: vary number of parallel\n      pairs (10, 20, 50, 100, 200) for linear projection transfer.\n      Determines minimum data requirement for this surprisingly strong baseline.\n      Both models × 5 representative layers × 20 languages.\n    priority: P1\n    gpu_budget_hours: 2\n    deps: [plan_001, plan_002]\n    notes: \"CPU-bound, uses cached activations. Dream review D11.\"\n\n  - id: plan_013\n    claim: 1\n    description: >\n      Probing control tasks (Hewitt & Liang 2019): train probes on\n      randomly permuted labels at each layer. Compare selectivity\n      (probe AUROC - control AUROC) across layers and languages.\n      Validates that high AUROC reflects genuine correctness direction,\n      not memorized dataset artifacts or probe capacity.\n    priority: P1\n    gpu_budget_hours: 2\n    deps: [plan_001, plan_002]\n    notes: \"CPU-bound. Dream review D22: probing methodology critique.\"\n\n  # === P2: Camera-ready extension ===\n\n  - id: plan_008\n    claim: 1\n    description: >\n      Gemma 4 31B Dense (60 layers, dense, FP16): third architecture\n      for camera-ready. Full Pareto frontier, 20+ languages.\n      Provides dense vs MoE architectural contrast.\n    priority: P2\n    gpu_budget_hours: 30\n    deps: []\n\n  - id: plan_009\n    claim: 1\n    description: >\n      Extended language coverage: expand from 20 to 50+ languages\n      for camera-ready. Leverages GlobalMMLU/Belebele full language sets.\n    priority: P2\n    gpu_budget_hours: 50\n    deps: [plan_001, plan_002]\n\n  # === MVP experiments (completed/running) ===\n\n  - id: mvp_validation\n    claim: 1\n    description: \"MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift\"\n    priority: P0\n    registry_id: mvp_001\n    gpu_budget_hours: 2\n    deps: []\n\n  - id: mvp_complementary\n    claim: 1\n    description: \"MVP robustness: complementary layer set (2,6,10,14,18,22,26)\"\n    priority: P1\n    registry_id: mvp_002\n    gpu_budget_hours: 2\n    deps: [mvp_validation]\n\n  - id: mvp_llama_control\n    claim: 1\n    description: \"MVP cross-architecture: Llama-3.1-8B control experiment\"\n    priority: P1\n    registry_id: mvp_003\n    gpu_budget_hours: 3\n    deps: [mvp_validation]\n",
      "numLines": 210,
      "startLine": 1,
      "totalLines": 210
    }
  },
  "sourceToolAssistantUUID": "99283016-db97-4cd7-85b7-bc61d802feb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T20:31:54.181Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VzhvnBStDsXQws5cwZY5r8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c537a5a-2e6a-46d5-9f82-8cd4106ca711",
  "isSidechain": false,
  "requestId": "req_011CbETRiwsGPd9ctxeZFfxv",
  "type": "assistant",
  "uuid": "93b7d840-b16a-4c6a-83c4-ff1031b70355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBKXnGFU1Y6jkcSU5y9CPf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1804,
      "cache_read_input_tokens": 25396,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 25396,
          "cache_creation_input_tokens": 1804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1804
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

_source line 14 · 2026-05-20T20:31:54.554Z_

<details><summary>↩ Tool result · `toolu_01VzhvnBStDsXQws5cwZY5r8`</summary>

```text
1	tier: worst
2	narrative_guidance: 'Full reframe to field-level diagnostic paper: ''Does probe-based
3	  calibration work beyond English? A systematic study across 2 architectures and 20
4	  languages.'' Value proposition shifts from method contribution to first large-scale
5	  answer on whether this research line generalizes. CaCLR is reported as a rigorous
6	  negative result — consistency-based objectives do not help when the cross-lingual
7	  correctness signal is this noisy. Decomposition is reported as evidence that difficulty
8	  and capability are entangled in multilingual representations, contradicting the
9	  clean separation assumed by English-only prior work. Pareto frontier is real on
10	  Qwen3 but fails to replicate cleanly on Llama 4 Scout — reported as architecture-dependence
11	  finding rather than universal law. Orthogonality (Claim 4) survives as the one mechanistic
12	  takeaway: output-based calibration is structurally limited everywhere, not just
13	  English. Target EACL with framing that negative/diagnostic results at this scale
14	  (2 models × 20 languages × all layers) are community-valuable when the field is
15	  actively expanding probe-based methods without multilingual validation.
16	
17	  '
18	imagined_experiments:
19	- name: Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT8)
20	  plan_id: plan_001
21	  description: 'Extract activations at 24 probed layers (every 4th of 94), 20 languages
22	    on GlobalMMLU. Train English logistic regression + 2-layer MLP correctness probes.
23	    Evaluate 5 transfer conditions: zero-shot, mean-shift, linear projection, few-shot
24	    (25/100), CaCLR.
25	
26	    '
27	  expected_results:
28	    en_auroc_best_layer: 0.776
29	    en_best_layer_idx: 72
30	    en_auroc_range:
31	    - 0.612
32	    - 0.776
33	    en_ece_raw_best: 0.172
34	    en_ece_tempcal_best: 0.068
35	    temp_scaling_T: 5.83
36	    zs_transfer_auroc_mean_19lang: 0.621
37	    zs_transfer_auroc_median_19lang: 0.633
38	    zs_transfer_auroc_std_19lang: 0.054
39	    zs_transfer_drop_mean_pp: 15.5
40	    zs_pass_rate_19lang: 0.368
41	    zs_pass_langs:
42	    - zh
43	    - fr
44	    - de
45	    - es
46	    - ja
47	    - ru
48	    - ko
49	    zs_fail_langs:
50	    - ar
51	    - hi
52	    - sw
53	    - yo
54	    - te
55	    - bn
56	    - ta
57	    - th
58	    - vi
59	    - uk
60	    - id
61	    - pl
62	    mean_shift_improves_count: 0
63	    mean_shift_mean_delta_ece_pp: 3.14
64	    linproj_auroc_mean_19lang: 0.648
65	    linproj_improves_over_zs_count: 13
66	    linproj_mean_delta_auroc_vs_zs_pp: 2.7
67	    fewshot25_auroc_mean_19lang: 0.654
68	    fewshot25_improves_over_zs_count: 14
69	    fewshot100_auroc_mean_19lang: 0.671
70	    fewshot100_improves_over_zs_count: 16
71	    pareto_depth_transfer_rank_corr: 0.41
72	    pareto_frontier_monotonic: false
73	    pareto_n_dominated_layers: 6
74	    transfer_by_family:
75	      indo_european_germanic:
76	        mean: 0.672
77	        langs:
78	        - de
79	        - en
80	      indo_european_romance:
81	        mean: 0.661
82	        langs:
83	        - fr
84	        - es
85	      indo_european_slavic:
86	        mean: 0.629
87	        langs:
88	        - ru
89	        - uk
90	        - pl
91	      indo_european_indic:
92	        mean: 0.598
93	        langs:
94	        - hi
95	        - bn
96	        - te
97	        - ta
98	      sino_tibetan:
99	        mean: 0.668
100	        langs:
101	        - zh
102	      japonic:
103	        mean: 0.651
104	        langs:
105	        - ja
106	      koreanic:
107	        mean: 0.648
108	        langs:
109	        - ko
110	      afroasiatic:
111	        mean: 0.612
112	        langs:
113	        - ar
114	      niger_congo:
115	        mean: 0.543
116	        langs:
117	        - sw
118	        - yo
119	      tai_kadai:
120	        mean: 0.591
121	        langs:
122	        - th
123	      austronesian:
124	        mean: 0.618
125	        langs:
126	        - id
127	      austroasiatic:
128	        mean: 0.607
129	        langs:
130	        - vi
131	  result_rationale: 'Qwen3-235B is a much larger MoE model than the MVP''s Qwen2.5-7B.
132	    English AUROC at 0.776 improves modestly over MVP''s 0.754 because the model is
133	    more capable and the correctness signal is more linearly accessible in larger
134	    models, but gains are sublinear — the larger model also has more complex, distributed
135	    representations that resist simple linear probing. Zero-shot transfer mean of
136	    0.621 reflects the worst-tier prediction that transfer is unreliable: high-resource
137	    Indo-European languages (fr, de, es) and CJK (zh, ja, ko) transfer adequately
138	    because their representations share more subspace structure with English at intermediate
139	    layers, but low-resource languages (sw, yo, te, bn) and languages with very different
140	    morphology (th, ta) fail because the MoE routing creates language-specific expert
141	    patterns that are opaque to an English-trained linear probe. Mean-shift fails
142	    entirely (0/19) because the mean activation difference between languages conflates
143	    content, style, and script differences — subtracting it removes useful signal.
144	    The Pareto frontier rank correlation of 0.41 is real but moderate: the general
145	    trend (deeper = better English, worse transfer) holds, but MoE routing introduces
146	    non-monotonic noise at mid-depth layers where expert activation patterns shift.
147	    The 7/19 pass rate reflects that only typologically close or high-resource languages
148	    have enough representational overlap with English for zero-shot transfer to work.
149	
150	    '
151	  tables:
152	  - name: 'Table 1: Qwen3-235B English Probe Performance by Layer (Selected Layers)'
153	    columns:
154	    - layer
155	    - depth_pct
156	    - logreg_auroc
157	    - mlp_auroc
158	    - ece_raw
159	    - ece_tempcal
160	    rows:
161	    - - 4
162	      - 4
163	      - 0.612
164	      - 0.618
165	      - 0.298
166	      - 0.192
167	    - - 16
168	      - 17
169	      - 0.653
170	      - 0.661
171	      - 0.251
172	      - 0.148
173	    - - 28
174	      - 30
175	      - 0.694
176	      - 0.708
177	      - 0.224
178	      - 0.121
179	    - - 40
180	      - 43
181	      - 0.721
182	      - 0.737
183	      - 0.203
184	      - 0.098
185	    - - 52
186	      - 55
187	      - 0.742
188	      - 0.755
189	      - 0.191
190	      - 0.082
191	    - - 60
192	      - 64
193	      - 0.758
194	      - 0.769
195	      - 0.183
196	      - 0.075
197	    - - 72
198	      - 77
199	      - 0.776
200	      - 0.783
201	      - 0.172
202	      - 0.068
203	    - - 80
204	      - 85
205	      - 0.771
206	      - 0.779
207	      - 0.176
208	      - 0.071
209	    - - 88
210	      - 94
211	      - 0.753
212	      - 0.762
213	      - 0.185
214	      - 0.079
215	    - - 92
216	      - 98
217	      - 0.728
218	      - 0.739
219	      - 0.198
220	      - 0.091
221	  - name: 'Table 2: Qwen3-235B Zero-Shot Transfer AUROC by Language (Best Transfer
222	      Layer)'
223	    columns:
224	    - language
225	    - family
226	    - resource_tier
227	    - best_zs_layer
228	    - best_zs_auroc
229	    - en_auroc_at_same_layer
230	    - drop_pp
231	    rows:
232	    - - zh
233	      - sino_tibetan
234	      - high
235	      - 52
236	      - 0.668
237	      - 0.742
238	      - 7.4
239	    - - fr
240	      - romance
241	      - high
242	      - 52
243	      - 0.672
244	      - 0.742
245	      - 7.0
246	    - - de
247	      - germanic
248	      - high
249	      - 52
250	      - 0.671
251	      - 0.742
252	      - 7.1
253	    - - es
254	      - romance
255	      - high
256	      - 52
257	      - 0.661
258	      - 0.742
259	      - 8.1
260	    - - ja
261	      - japonic
262	      - high
263	      - 48
264	      - 0.651
265	      - 0.735
266	      - 8.4
267	    - - ru
268	      - slavic
269	      - high
270	      - 48
271	      - 0.644
272	      - 0.735
273	      - 9.1
274	    - - ko
275	      - koreanic
276	      - high
277	      - 48
278	      - 0.648
279	      - 0.735
280	      - 8.7
281	    - - ar
282	      - afroasiatic
283	      - mid
284	      - 40
285	      - 0.612
286	      - 0.721
287	      - 10.9
288	    - - hi
289	      - indic
290	      - mid
291	      - 40
292	      - 0.618
293	      - 0.721
294	      - 10.3
295	    - - vi
296	      - austroasiatic
297	      - mid
298	      - 40
299	      - 0.607
300	      - 0.721
301	      - 11.4
302	    - - id
303	      - austronesian
304	      - mid
305	      - 40
306	      - 0.618
307	      - 0.721
308	      - 10.3
309	    - - th
310	      - tai_kadai
311	      - mid
312	      - 40
313	      - 0.591
314	      - 0.721
315	      - 13.0
316	    - - pl
317	      - slavic
318	      - mid
319	      - 40
320	      - 0.621
321	      - 0.721
322	      - 10.0
323	    - - uk
324	      - slavic
325	      - mid
326	      - 40
327	      - 0.614
328	      - 0.721
329	      - 10.7
330	    - - bn
331	      - indic
332	      - low
333	      - 28
334	      - 0.583
335	      - 0.694
336	      - 11.1
337	    - - te
338	      - indic
339	      - low
340	      - 28
341	      - 0.571
342	      - 0.694
343	      - 12.3
344	    - - ta
345	      - indic
346	      - low
347	      - 28
348	      - 0.568
349	      - 0.694
350	      - 12.6
351	    - - sw
352	      - niger_congo
353	      - low
354	      - 28
355	      - 0.557
356	      - 0.694
357	      - 13.7
358	    - - yo
359	      - niger_congo
360	      - low
361	      - 28
362	      - 0.529
363	      - 0.694
364	      - 16.5
365	  - name: 'Table 3: Qwen3-235B Transfer Method Comparison (AUROC, 19-Language Mean)'
366	    columns:
367	    - method
368	    - auroc_mean
369	    - auroc_std
370	    - pass_rate
371	    - ece_mean
372	    - delta_vs_zs_pp
373	    rows:
374	    - - zero_shot
375	      - 0.621
376	      - 0.054
377	      - 0.368
378	      - 0.194
379	      - 0.0
380	    - - mean_shift
381	      - 0.604
382	      - 0.067
383	      - 0.263
384	      - 0.225
385	      - -1.7
386	    - - linear_projection
387	      - 0.648
388	      - 0.048
389	      - 0.526
390	      - 0.171
391	      - 2.7
392	    - - few_shot_25
393	      - 0.654
394	      - 0.045
395	      - 0.526
396	      - 0.166
397	      - 3.3
398	    - - few_shot_100
399	      - 0.671
400	      - 0.041
401	      - 0.632
402	      - 0.152
403	      - 5.0
404	  figures_description:
405	  - 'Figure 1a: Heatmap of zero-shot transfer AUROC (y-axis: 24 probed layers sorted
406	    by depth, x-axis: 20 languages sorted by resource tier). Shows a gradient where
407	    upper-left (deep layers × high-resource langs) has moderate AUROC (~0.65-0.67)
408	    and lower-right (shallow layers × low-resource langs) is near chance (~0.52-0.57).
409	    But the pattern is noisy — no crisp diagonal boundary. Several mid-depth layers
410	    show unexpected dips (layers 48-56) breaking monotonicity.'
411	  - 'Figure 1b: Pareto frontier scatter plot (x-axis: mean 19-lang zero-shot AUROC,
412	    y-axis: English AUROC at same layer). Each point is a layer. The Pareto front
413	    connects 6 non-dominated layers but the remaining 18 points scatter widely around
414	    it. Convex hull is thin — the tradeoff is real but the frontier offers limited
415	    choice. Error bars (bootstrap 95% CI) overlap substantially between adjacent Pareto-optimal
416	    points.'
417	  - 'Figure 1c: Line plot of zero-shot transfer drop (EN AUROC minus target-lang AUROC)
418	    vs layer depth, one line per language, colored by resource tier. High-resource
419	    languages (blue) show a gentle upward slope (deeper = worse transfer). Low-resource
420	    languages (red) show a steep upward slope. The spread between lines increases
421	    with depth, illustrating that the Pareto tradeoff is more severe for low-resource
422	    languages.'
423	  analysis: 'The Pareto frontier is real on Qwen3-235B but weak: rank correlation
424	    of 0.41 means the depth-transfer tradeoff explains only ~17% of variance. MoE
425	    routing creates non-monotonic perturbations at mid-depth. The practical implication
426	    is limited — the frontier provides modest guidance for layer selection but is
427	    not a reliable engineering tool. Zero-shot transfer fails for 12/19 languages
428	    (AUROC < 0.65), with a clear resource-tier gradient. The field should not assume
429	    English-trained correctness probes transfer to low-resource languages. Mean-shift
430	    is confirmed dead at scale. Linear projection and few-shot are the only viable
431	    transfer methods, with few-shot-100 achieving the best results — but requiring
432	    100 labeled examples per language partially negates the zero-label promise.
433	
434	    '
435	- name: Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, INT8)
436	  plan_id: plan_002
437	  description: 'Extract activations at 12 probed layers (every 4th of 48), 20 languages
438	    on GlobalMMLU. Train English correctness probes, evaluate 5 transfer conditions.
439	
440	    '
441	  expected_results:
442	    en_auroc_best_layer: 0.749
443	    en_best_layer_idx: 36
444	    en_auroc_range:
445	    - 0.598
446	    - 0.749
447	    en_ece_raw_best: 0.188
448	    en_ece_tempcal_best: 0.074
449	    temp_scaling_T: 5.47
450	    zs_transfer_auroc_mean_19lang: 0.594
451	    zs_transfer_auroc_median_19lang: 0.601
452	    zs_transfer_auroc_std_19lang: 0.061
453	    zs_transfer_drop_mean_pp: 18.2
454	    zs_pass_rate_19lang: 0.211
455	    zs_pass_langs:
456	    - zh
457	    - fr
458	    - de
459	    - es
460	    zs_fail_langs:
461	    - ja
462	    - ru
463	    - ko
464	    - ar
465	    - hi
466	    - sw
467	    - yo
468	    - te
469	    - bn
470	    - ta
471	    - th
472	    - vi
473	    - uk
474	    - id
475	    - pl
476	    mean_shift_improves_count: 0
477	    mean_shift_mean_delta_ece_pp: 4.21
478	    linproj_auroc_mean_19lang: 0.623
479	    linproj_improves_over_zs_count: 11
480	    fewshot25_auroc_mean_19lang: 0.631
481	    fewshot100_auroc_mean_19lang: 0.652
482	    pareto_depth_transfer_rank_corr: 0.22
483	    pareto_frontier_monotonic: false
484	    pareto_n_dominated_layers: 3
485	    pareto_frontier_agreement_with_qwen3: 0.33
486	    nonmonotonic_layers:
487	    - 20
488	    - 24
489	    - 28
490	  result_rationale: 'Llama 4 Scout is the worst-tier''s key failure point. Its Pareto
491	    frontier is flat/non-monotonic (rank correlation 0.22) because Llama 4 Scout''s
492	    MoE architecture uses a different routing strategy than Qwen3-235B: its experts
493	    are more language-specialized at intermediate layers, meaning the English correctness
494	    direction at layers 20-28 is entangled with English-specific expert activations
495	    in ways that neither degrade nor improve monotonically with depth. English AUROC
496	    peaks at 0.749 (lower than Qwen3''s 0.776) because Llama 4 Scout''s 48 layers
497	    compress the representational hierarchy — the same functional stages are packed
498	    into fewer layers, leaving less room for a clean correctness signal to emerge.
499	    Zero-shot transfer is worse overall (mean 0.594 vs Qwen3''s 0.621) because Llama
500	    4 Scout''s training data distribution is more English-centric, and its MoE routing
501	    assigns non-English tokens to a sparser expert set that shares less structure
502	    with the English experts. Only 4/19 languages pass the 0.65 threshold. The 0.33
503	    cross-architecture Pareto agreement means the optimal layer for a given language
504	    on Qwen3 does not predict the optimal layer on Llama 4 — the tradeoff is architecture-specific,
505	    not a universal property of transformer depth.
506	
507	    '
508	  tables:
509	  - name: 'Table 4: Llama 4 Scout English Probe Performance by Layer'
510	    columns:
511	    - layer
512	    - depth_pct
513	    - logreg_auroc
514	    - mlp_auroc
515	    - ece_raw
516	    - ece_tempcal
517	    rows:
518	    - - 4
519	      - 8
520	      - 0.598
521	      - 0.604
522	      - 0.312
523	      - 0.201
524	    - - 8
525	      - 17
526	      - 0.631
527	      - 0.641
528	      - 0.274
529	      - 0.168
530	    - - 12
531	      - 25
532	      - 0.668
533	      - 0.679
534	      - 0.241
535	      - 0.137
536	    - - 16
537	      - 33
538	      - 0.694
539	      - 0.706
540	      - 0.218
541	      - 0.112
542	    - - 20
543	      - 42
544	      - 0.712
545	      - 0.722
546	      - 0.205
547	      - 0.098
548	    - - 24
549	      - 50
550	      - 0.726
551	      - 0.735
552	      - 0.196
553	      - 0.088
554	    - - 28
555	      - 58
556	      - 0.734
557	      - 0.743
558	      - 0.192
559	      - 0.083
560	    - - 32
561	      - 67
562	      - 0.741
563	      - 0.749
564	      - 0.189
565	      - 0.078
566	    - - 36
567	      - 75
568	      - 0.749
569	      - 0.755
570	      - 0.188
571	      - 0.074
572	    - - 40
573	      - 83
574	      - 0.744
575	      - 0.751
576	      - 0.19
577	      - 0.077
578	    - - 44
579	      - 92
580	      - 0.731
581	      - 0.738
582	      - 0.195
583	      - 0.084
584	    - - 48
585	      - 100
586	      - 0.708
587	      - 0.718
588	      - 0.209
589	      - 0.097
590	  - name: 'Table 5: Llama 4 Scout Zero-Shot Transfer AUROC by Language (Best Transfer
591	      Layer)'
592	    columns:
593	    - language
594	    - best_zs_layer
595	    - best_zs_auroc
596	    - drop_vs_en_pp
597	    rows:
598	    - - zh
599	      - 24
600	      - 0.658
601	      - 6.8
602	    - - fr
603	      - 24
604	      - 0.662
605	      - 6.4
606	    - - de
607	      - 24
608	      - 0.655
609	      - 7.1
610	    - - es
611	      - 24
612	      - 0.651
613	      - 7.5
614	    - - ja
615	      - 20
616	      - 0.631
617	      - 8.1
618	    - - ru
619	      - 20
620	      - 0.622
621	      - 9.0
622	    - - ko
623	      - 20
624	      - 0.627
625	      - 8.5
626	    - - ar
627	      - 16
628	      - 0.589
629	      - 10.5
630	    - - hi
631	      - 16
632	      - 0.594
633	      - 10.0
634	    - - vi
635	      - 16
636	      - 0.581
637	      - 11.3
638	    - - id
639	      - 16
640	      - 0.591
641	      - 10.3
642	    - - th
643	      - 16
644	      - 0.568
645	      - 12.6
646	    - - pl
647	      - 20
648	      - 0.608
649	      - 10.4
650	    - - uk
651	      - 16
652	      - 0.592
653	      - 10.2
654	    - - bn
655	      - 12
656	      - 0.556
657	      - 11.2
658	    - - te
659	      - 12
660	      - 0.541
661	      - 12.7
662	    - - ta
663	      - 12
664	      - 0.538
665	      - 13.0
666	    - - sw
667	      - 12
668	      - 0.524
669	      - 14.4
670	    - - yo
671	      - 12
672	      - 0.498
673	      - 17.0
674	  - name: 'Table 6: Cross-Architecture Pareto Frontier Agreement'
675	    columns:
676	    - metric
677	    - qwen3_235b
678	    - llama4_scout
679	    - agreement
680	    rows:
681	    - - rank_corr_depth_vs_transfer
682	      - 0.41
683	      - 0.22
684	      - —
685	    - - pareto_optimal_layer_count
686	      - 6/24
687	      - 3/12
688	      - —
689	    - - best_transfer_layer_pct_depth
690	      - 55%
691	      - 50%
692	      - —
693	    - - zs_mean_auroc
694	      - 0.621
695	      - 0.594
696	      - —
697	    - - optimal_layer_rank_agreement_tau
698	      - —
699	      - —
700	      - 0.33
701	    - - pass_lang_overlap_jaccard
702	      - —
703	      - —
704	      - 0.44
705	  figures_description:
706	  - 'Figure 2a: Side-by-side Pareto frontier scatter plots for Qwen3-235B (left) and
707	    Llama 4 Scout (right). Qwen3 shows a discernible convex Pareto front with 6 non-dominated
708	    points forming a curve from upper-left (high EN, low transfer) to lower-right
709	    (low EN, high transfer). Llama 4 shows a near-flat cloud with only 3 weakly non-dominated
710	    points — no meaningful tradeoff curve. The contrast is the paper''s key Figure
711	    2 evidence that the Pareto frontier is architecture-dependent.'
712	  - 'Figure 2b: Llama 4 Scout non-monotonicity detail: line plot of transfer AUROC
713	    vs layer depth for zh, fr, ar, sw. The zh/fr lines show a bump at layer 20, dip
714	    at 24, recover at 28 — violating the monotonic depth-transfer assumption. This
715	    is attributed to MoE expert routing transitions at these layers.'
716	  analysis: 'Llama 4 Scout is the worst-tier''s smoking gun for the diagnostic reframe.
717	    The Pareto frontier essentially doesn''t exist on this architecture (rank corr
718	    0.22, only 3 non-dominated layers). This is the strongest evidence for the diagnostic
719	    paper''s thesis: the depth-transfer tradeoff from Claim 1 is not a universal property
720	    of transformers but an architecture-dependent phenomenon that cannot be assumed
721	    to generalize. The 0.33 cross-architecture agreement means practitioners cannot
722	    use findings from one model to guide layer selection on another. For the paper,
723	    this transforms from a weakness into a key finding: the field cannot assume probe-based
724	    calibration will behave consistently across architectures.
725	
726	    '
727	- name: CaCLR Implementation and Comparative Evaluation
728	  plan_id: plan_003
729	  description: 'Implement CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency). Train CaCLR
730	    probes using English labels + unlabeled parallel activations. Compare vs all 5
731	    transfer conditions across full Pareto frontier for both models × 20 languages.
732	
733	    '
734	  expected_results:
735	    caclr_auroc_mean_qwen3: 0.645
736	    caclr_auroc_mean_llama4: 0.618
737	    caclr_vs_linproj_auroc_delta_pp_qwen3: -0.3
738	    caclr_vs_linproj_auroc_delta_pp_llama4: -0.5
739	    caclr_vs_zs_auroc_delta_pp_qwen3: 2.4
740	    caclr_vs_zs_auroc_delta_pp_llama4: 2.4
741	    caclr_vs_fewshot100_auroc_delta_pp_qwen3: -2.6
742	    caclr_vs_fewshot100_auroc_delta_pp_llama4: -3.4
743	    caclr_improvement_pass_rate_qwen3: 0.47
744	    caclr_improvement_pass_rate_llama4: 0.37
745	    caclr_ece_mean_qwen3: 0.174
746	    caclr_ece_mean_llama4: 0.189
747	    caclr_ece_reduction_vs_tempcal_pct_qwen3: 7.2
748	    caclr_ece_reduction_vs_tempcal_pct_llama4: 3.8
749	    best_alpha: 0.3
750	    best_beta: 0.05
751	    alpha_sensitivity: moderate — ±0.1 changes AUROC by ~0.5pp
752	    beta_sensitivity: flat — β from 0.01 to 0.5 changes AUROC by <0.3pp, indicating
753	      consistency loss is inert
754	    caclr_no_consistency_auroc_mean: 0.647
755	    caclr_no_sbece_auroc_mean: 0.629
756	    caclr_bce_only_auroc_mean: 0.621
757	    caclr_per_lang_qwen3:
758	      zh:
759	        auroc: 0.671
760	        delta_vs_zs: 0.3
761	        delta_vs_linproj: -0.8
762	      fr:
763	        auroc: 0.668
764	        delta_vs_zs: -0.4
765	        delta_vs_linproj: -1.2
766	      de:
767	        auroc: 0.665
768	        delta_vs_zs: -0.6
769	        delta_vs_linproj: -0.9
770	      es:
771	        auroc: 0.658
772	        delta_vs_zs: -0.3
773	        delta_vs_linproj: -0.7
774	      ja:
775	        auroc: 0.649
776	        delta_vs_zs: -0.2
777	        delta_vs_linproj: -0.4
778	      ru:
779	        auroc: 0.641
780	        delta_vs_zs: -0.3
781	        delta_vs_linproj: -0.6
782	      ko:
783	        auroc: 0.647
784	        delta_vs_zs: -0.1
785	        delta_vs_linproj: -0.3
786	      ar:
787	        auroc: 0.628
788	        delta_vs_zs: 1.6
789	        delta_vs_linproj: 0.2
790	      hi:
791	        auroc: 0.635
792	        delta_vs_zs: 1.7
793	        delta_vs_linproj: 0.1
794	      vi:
795	        auroc: 0.621
796	        delta_vs_zs: 1.4
797	        delta_vs_linproj: -0.3
798	      id:
799	        auroc: 0.633
800	        delta_vs_zs: 1.5
801	        delta_vs_linproj: -0.1
802	      th:
803	        auroc: 0.607
804	        delta_vs_zs: 1.6
805	        delta_vs_linproj: 0.3
806	      pl:
807	        auroc: 0.638
808	        delta_vs_zs: 1.7
809	        delta_vs_linproj: 0.1
810	      uk:
811	        auroc: 0.631
812	        delta_vs_zs: 1.7
813	        delta_vs_linproj: 0.2
814	      bn:
815	        auroc: 0.601
816	        delta_vs_zs: 1.8
817	        delta_vs_linproj: 0.5
818	      te:
819	        auroc: 0.589
820	        delta_vs_zs: 1.8
821	        delta_vs_linproj: 0.4
822	      ta:
823	        auroc: 0.587
824	        delta_vs_zs: 1.9
825	        delta_vs_linproj: 0.6
826	      sw:
827	        auroc: 0.578
828	        delta_vs_zs: 2.1
829	        delta_vs_linproj: 0.9
830	      yo:
831	        auroc: 0.551
832	        delta_vs_zs: 2.2
833	        delta_vs_linproj: 0.7
834	  result_rationale: 'CaCLR''s consistency loss (L_consistency) is designed to align
835	    cross-lingual probe activations so that the English probe generalizes. In the
836	    worst tier, this fails because the cross-lingual correctness signal is too noisy
837	    for the consistency objective to find meaningful invariances. The unlabeled parallel
838	    activations contain language-specific variance (script, morphology, tokenization
839	    artifacts) that dominates the correctness signal, so minimizing distributional
840	    distance between languages collapses both signal and noise. The hyperparameter
841	    search confirms this: β (consistency weight) is driven to near-zero (0.05), and
842	    removing the consistency term entirely slightly improves performance (+0.2pp).
843	    The SB-ECE term helps modestly because it acts as a calibration regularizer on
844	    the English side, but this benefit doesn''t compound with consistency. CaCLR ends
845	    up being essentially "zero-shot + SB-ECE regularization" — functionally a slightly
846	    calibration-aware version of the base probe. Linear projection beats CaCLR because
847	    projection directly estimates and applies the affine transformation between language
848	    representation subspaces, which is a more efficient use of the few available parallel
849	    datapoints than trying to learn an invariant representation. The key insight:
850	    simple alignment (linproj) outperforms principled invariance (CaCLR) when the
851	    signal-to-noise ratio of the target signal is low. For high-resource languages
852	    that already transfer well, CaCLR''s overhead yields no benefit; for low-resource
853	    languages where help is needed, the consistency signal is too noisy to learn from.
854	
855	    '
856	  tables:
857	  - name: 'Table 7: Transfer Method Comparison Summary (19-Language Mean, Both Architectures)'
858	    columns:
859	    - method
860	    - qwen3_auroc
861	    - qwen3_ece
862	    - llama4_auroc
863	    - llama4_ece
864	    - labels_needed
865	    rows:
866	    - - zero_shot
867	      - 0.621
868	      - 0.194
869	      - 0.594
870	      - 0.212
871	      - 0 target
872	    - - mean_shift
873	      - 0.604
874	      - 0.225
875	      - 0.571
876	      - 0.248
877	      - 0 target (fails)
878	    - - linear_projection
879	      - 0.648
880	      - 0.171
881	      - 0.623
882	      - 0.189
883	      - ~50 parallel
884	    - - CaCLR
885	      - 0.645
886	      - 0.174
887	      - 0.618
888	      - 0.193
889	      - 0 target + parallel
890	    - - few_shot_25
891	      - 0.654
892	      - 0.166
893	      - 0.631
894	      - 0.182
895	      - 25 target
896	    - - few_shot_100
897	      - 0.671
898	      - 0.152
899	      - 0.652
900	      - 0.168
901	      - 100 target
902	  - name: 'Table 8: CaCLR Ablation (Qwen3-235B, 19-Language Mean)'
903	    columns:
904	    - variant
905	    - auroc_mean
906	    - ece_mean
907	    - delta_vs_full_pp
908	    rows:
909	    - - Full CaCLR (BCE+SB-ECE+Consistency)
910	      - 0.645
911	      - 0.174
912	      - 0.0
913	    - - CaCLR − Consistency (BCE+SB-ECE)
914	      - 0.647
915	      - 0.172
916	      - 0.2
917	    - - CaCLR − SB-ECE (BCE+Consistency)
918	      - 0.629
919	      - 0.188
920	      - -1.6
921	    - - BCE Only (= zero-shot probe)
922	      - 0.621
923	      - 0.194
924	      - -2.4
925	    - - Linear Projection
926	      - 0.648
927	      - 0.171
928	      - 0.3
929	  figures_description:
930	  - 'Figure 3a: Grouped bar chart comparing 6 transfer methods across 20 languages
931	    (Qwen3-235B), sorted by language resource tier. Shows that few-shot-100 > few-shot-25
932	    ≈ linear projection ≈ CaCLR > zero-shot >> mean-shift. CaCLR and linear projection
933	    bars are nearly identical in height across all languages. The visual message is
934	    clear: CaCLR adds complexity without benefit.'
935	  - 'Figure 3b: Hyperparameter sensitivity plot for CaCLR. Left panel: AUROC vs α
936	    (SB-ECE weight), showing a gentle inverted-U peaking at α=0.3. Right panel: AUROC
937	    vs β (consistency weight), showing a flat line — β has no effect. This is the
938	    key visual evidence that the consistency objective is inert.'
939	  - 'Figure 3c: Scatter plot of per-language CaCLR improvement (y-axis) vs zero-shot
940	    baseline AUROC (x-axis). Shows that CaCLR helps low-resource languages modestly
941	    (+1-2pp) but slightly hurts high-resource languages that already transfer well
942	    (-0.3 to -1.2pp). Linear projection shows the same pattern but with uniformly
943	    better outcomes. Net: CaCLR''s mechanism doesn''t add value over simple geometric
944	    alignment.'
945	  analysis: 'CaCLR is a rigorous negative result. The consistency loss term — the
946	    core methodological novelty — is inert. This is not a hyperparameter tuning failure;
947	    β is swept over 3 orders of magnitude and the landscape is flat. The SB-ECE term
948	    provides modest calibration regularization, but this benefit is available without
949	    any cross-lingual machinery. Linear projection achieves the same or better results
950	    with a simpler mechanism. For the paper, this is framed as: "consistency-based
951	    cross-lingual alignment objectives do not help when the underlying correctness
952	    signal has low cross-lingual SNR. This negative result saves the community from
953	    pursuing distributional-matching approaches (adversarial, MMD, consistency) for
954	    this problem class."
955	
956	    '
957	- name: Difficulty-Controlled Ablation (Decomposition)
958	  plan_id: plan_004
959	  description: 'Train IRT difficulty probes, project out difficulty direction from
960	    activations, retrain correctness probes on residuals, evaluate transfer. 10 representative
961	    languages × 8 representative layers per model.
962	
963	    '
964	  expected_results:
965	    difficulty_probe_r2_en_qwen3: 0.52
966	    difficulty_probe_r2_en_llama4: 0.47
967	    difficulty_probe_transfer_r2_mean_9lang: 0.41
968	    decomp_difficulty_var_explained_pct_qwen3: 14.3
969	    decomp_difficulty_var_explained_pct_llama4: 11.8
970	    correctness_residual_auroc_en_qwen3: 0.738
971	    correctness_residual_auroc_en_llama4: 0.711
972	    correctness_residual_transfer_auroc_mean_qwen3: 0.607
973	    correctness_residual_transfer_auroc_mean_llama4: 0.581
974	    transfer_improvement_after_projection: false
975	    transfer_delta_after_projection_pp_qwen3: -1.4
976	    transfer_delta_after_projection_pp_llama4: -1.3
977	    difficulty_correctness_cosine_mean_qwen3: 0.34
978	    difficulty_correctness_cosine_mean_llama4: 0.38
979	    difficulty_correctness_cosine_std: 0.11
980	    subspace_overlap_mean_angle_deg: 58
981	  result_rationale: 'In the worst tier, difficulty and capability are entangled in
982	    cross-lingual representations. The difficulty direction explains only 14% (Qwen3)
983	    / 12% (Llama4) of correctness probe variance — real but modest. Critically, projecting
984	    out difficulty makes transfer WORSE (-1.3 to -1.4pp), not better. This is because
985	    the difficulty-shared component actually carries useful cross-lingual signal:
986	    questions that are hard in English tend to be hard everywhere due to shared conceptual
987	    complexity, and this shared difficulty signal is one of the few reliable cross-lingual
988	    bridges for the correctness probe. Removing it strips away a genuine cross-lingual
989	    invariance. The residual "capability-specific" component is more language-dependent,
990	    not less — it contains the idiosyncratic ways each language''s tokens encode competence,
991	    which are precisely the non-transferable signals. The cosine similarity of 0.34-0.38
992	    between difficulty and correctness directions confirms they are neither orthogonal
993	    nor aligned — they share a moderate subspace that cannot be cleanly separated.
994	    This contradicts the paper''s original Claim 2 hypothesis that decomposition would
995	    be prescriptive. The decomposition is real but useless: it describes variance
996	    structure without enabling better transfer.
997	
998	    '
999	  tables:
1000	  - name: 'Table 9: Difficulty Probe Quality (Ridge Regression, R² on Held-Out)'
1001	    columns:
1002	    - language
1003	    - qwen3_r2
1004	    - llama4_r2
1005	    - is_transfer
1006	    rows:
1007	    - - en
1008	      - 0.52
1009	      - 0.47
1010	      - false
1011	    - - zh
1012	      - 0.48
1013	      - 0.43
1014	      - true
1015	    - - fr
1016	      - 0.47
1017	      - 0.42
1018	      - true
1019	    - - de
1020	      - 0.46
1021	      - 0.41
1022	      - true
1023	    - - ar
1024	      - 0.42
1025	      - 0.37
1026	      - true
1027	    - - hi
1028	      - 0.41
1029	      - 0.36
1030	      - true
1031	    - - ja
1032	      - 0.44
1033	      - 0.39
1034	      - true
1035	    - - ko
1036	      - 0.43
1037	      - 0.38
1038	      - true
1039	    - - sw
1040	      - 0.33
1041	      - 0.28
1042	      - true
1043	    - - yo
1044	      - 0.29
1045	      - 0.24
1046	      - true
1047	  - name: 'Table 10: Decomposition Transfer Ablation (9-Language Mean)'
1048	    columns:
1049	    - condition
1050	    - qwen3_auroc
1051	    - qwen3_delta_pp
1052	    - llama4_auroc
1053	    - llama4_delta_pp
1054	    rows:
1055	    - - Full activations (baseline)
1056	      - 0.621
1057	      - 0.0
1058	      - 0.594
1059	      - 0.0
1060	    - - Residual (difficulty projected out)
1061	      - 0.607
1062	      - -1.4
1063	      - 0.581
1064	      - -1.3
1065	    - - Difficulty component only
1066	      - 0.568
1067	      - -5.3
1068	      - 0.551
1069	      - -4.3
1070	    - - Random direction projected out (ctrl)
1071	      - 0.618
1072	      - -0.3
1073	      - 0.591
1074	      - -0.3
1075	  figures_description:
1076	  - 'Figure 4a: Scatter plot of correctness AUROC vs difficulty R² across 10 languages
1077	    × 8 layers, colored by model. Shows moderate positive correlation (r=0.41) — layers
1078	    where difficulty is well-encoded also support better correctness probing. This
1079	    contradicts the expectation that difficulty is a confound to be removed.'
1080	  - 'Figure 4b: Principal angle distribution between difficulty and correctness subspaces
1081	    across layers. Histogram peaks at ~55-60° — far from both 0° (fully shared) and
1082	    90° (fully orthogonal). The wide spread (std ~11°) across layers and languages
1083	    shows the relationship is inconsistent, preventing clean decomposition.'
1084	  analysis: 'Decomposition fails as a prescriptive tool. The difficulty-shared component,
1085	    far from being a confound, is actually one of the more reliable cross-lingual
1086	    bridges — removing it hurts. The capability-specific residual is more language-dependent,
1087	    not less, because it captures idiosyncratic encoding patterns. For the diagnostic
1088	    paper, this finding is reframed as: "difficulty and capability are entangled in
1089	    multilingual representations, unlike the clean separation reported in English-only
1090	    work. This entanglement may be fundamental to how multilingual models represent
1091	    knowledge — the shared difficulty structure is load-bearing for cross-lingual
1092	    transfer, not a confound to be controlled for."
1093	
1094	    '
1095	- name: Cross-Lingual Orthogonality Analysis
1096	  plan_id: plan_005
1097	  description: 'Extract verbalized confidence direction, compute cosine similarity
1098	    with correctness direction across 20 languages × 2 architectures. Analyze by resource
1099	    tier and language family.
1100	
1101	    '
1102	  expected_results:
1103	    orthogonality_cosine_mean_overall: 0.072
1104	    orthogonality_cosine_std_overall: 0.038
1105	    orthogonality_cosine_mean_qwen3: 0.068
1106	    orthogonality_cosine_mean_llama4: 0.076
1107	    orthogonality_cosine_range:
1108	    - 0.018
1109	    - 0.148
1110	    orthogonality_cosine_high_resource: 0.054
1111	    orthogonality_cosine_mid_resource: 0.071
1112	    orthogonality_cosine_low_resource: 0.098
1113	    pct_langs_cosine_below_0_1: 0.75
1114	    pct_langs_cosine_below_0_05: 0.35
1115	    confidence_probe_r2_mean: 0.68
1116	    confidence_probe_transfer_drops: true
1117	  result_rationale: 'Orthogonality persists cross-lingually (mean cosine 0.072, all
1118	    languages below 0.15) because it is a structural property of how LLMs represent
1119	    confidence vs correctness — the model''s verbalized confidence is calibrated to
1120	    appear confident regardless of actual correctness, and this dissociation is encoded
1121	    geometrically at the representation level. However, the worst-tier variance is
1122	    higher than Miao & Ungar''s English-only finding (std 0.038 vs their ~0.01): low-resource
1123	    languages show less orthogonality (cosine ~0.098) because the model has less capacity
1124	    to maintain the confidence-correctness dissociation for languages with limited
1125	    training data — when the model is uncertain due to lack of language-specific knowledge,
1126	    both its correctness and confidence signals degrade in correlated ways, slightly
1127	    breaking orthogonality. Reviewers may see this as incremental: Miao & Ungar showed
1128	    orthogonality for English, we extend to 20 languages, but the finding is qualitatively
1129	    the same. The resource- tier modulation is the one novel angle but the effect
1130	    size is modest (0.054 vs 0.098).
1131	
1132	    '
1133	  tables:
1134	  - name: 'Table 11: Correctness-Confidence Cosine Similarity by Language'
1135	    columns:
1136	    - language
1137	    - resource_tier
1138	    - qwen3_cosine
1139	    - llama4_cosine
1140	    - mean_cosine
1141	    rows:
1142	    - - en
1143	      - high
1144	      - 0.038
1145	      - 0.041
1146	      - 0.04
1147	    - - zh
1148	      - high
1149	      - 0.042
1150	      - 0.049
1151	      - 0.046
1152	    - - fr
1153	      - high
1154	      - 0.045
1155	      - 0.051
1156	      - 0.048
1157	    - - de
1158	      - high
1159	      - 0.047
1160	      - 0.054
1161	      - 0.051
1162	    - - es
1163	      - high
1164	      - 0.049
1165	      - 0.056
1166	      - 0.053
1167	    - - ja
1168	      - high
1169	      - 0.055
1170	      - 0.062
1171	      - 0.059
1172	    - - ru
1173	      - high
1174	      - 0.058
1175	      - 0.064
1176	      - 0.061
1177	    - - ko
1178	      - high
1179	      - 0.061
1180	      - 0.068
1181	      - 0.065
1182	    - - ar
1183	      - mid
1184	      - 0.063
1185	      - 0.072
1186	      - 0.068
1187	    - - hi
1188	      - mid
1189	      - 0.065
1190	      - 0.075
1191	      - 0.07
1192	    - - vi
1193	      - mid
1194	      - 0.068
1195	      - 0.077
1196	      - 0.073
1197	    - - id
1198	      - mid
1199	      - 0.064
1200	      - 0.073
1201	      - 0.069
1202	    - - th
1203	      - mid
1204	      - 0.072
1205	      - 0.082
1206	      - 0.077
1207	    - - pl
1208	      - mid
1209	      - 0.059
1210	      - 0.067
1211	      - 0.063
1212	    - - uk
1213	      - mid
1214	      - 0.062
1215	      - 0.071
1216	      - 0.067
1217	    - - bn
1218	      - low
1219	      - 0.081
1220	      - 0.092
1221	      - 0.087
1222	    - - te
1223	      - low
1224	      - 0.088
1225	      - 0.098
1226	      - 0.093
1227	    - - ta
1228	      - low
1229	      - 0.091
1230	      - 0.103
1231	      - 0.097
1232	    - - sw
1233	      - low
1234	      - 0.098
1235	      - 0.112
1236	      - 0.105
1237	    - - yo
1238	      - low
1239	      - 0.112
1240	      - 0.148
1241	      - 0.13
1242	  - name: 'Table 12: Orthogonality by Resource Tier (Mean Cosine ± Std)'
1243	    columns:
1244	    - resource_tier
1245	    - n_langs
1246	    - qwen3_mean
1247	    - llama4_mean
1248	    - overall_mean
1249	    - std
1250	    rows:
1251	    - - high
1252	      - 8
1253	      - 0.049
1254	      - 0.056
1255	      - 0.054
1256	      - 0.009
1257	    - - mid
1258	      - 7
1259	      - 0.065
1260	      - 0.074
1261	      - 0.071
1262	      - 0.005
1263	    - - low
1264	      - 5
1265	      - 0.094
1266	      - 0.111
1267	      - 0.098
1268	      - 0.016
1269	    - - all
1270	      - 20
1271	      - 0.066
1272	      - 0.076
1273	      - 0.072
1274	      - 0.022
1275	  figures_description:
1276	  - 'Figure 5a: Bar chart of cosine similarity (correctness vs confidence direction)
1277	    for 20 languages, sorted by resource tier, with Miao & Ungar''s English-only threshold
1278	    (0.04) marked as a horizontal dashed line. Most high-resource languages cluster
1279	    near the line; low-resource languages are 2-3× higher but still below 0.15. The
1280	    visual confirms orthogonality persists everywhere but the quantitative story is
1281	    noisier than prior work suggested.'
1282	  - 'Figure 5b: Scatter plot of orthogonality cosine (y-axis) vs zero-shot transfer
1283	    AUROC (x-axis), per language. Moderate negative correlation (r ≈ -0.62): languages
1284	    where orthogonality is stronger (lower cosine) also transfer better. This connects
1285	    Claims 1 and 4 — representation quality covaries with both metrics — but the causal
1286	    direction is ambiguous.'
1287	  analysis: 'Claim 4 survives in the worst tier but its contribution is incremental.
1288	    Orthogonality persists (mean 0.072, all < 0.15) — output-based calibration is
1289	    indeed structurally limited everywhere. The resource-tier gradient (high: 0.054,
1290	    mid: 0.071, low: 0.098) is novel but the effect size is modest. The correlation
1291	    between orthogonality and transfer success is intriguing but not causal. For the
1292	    diagnostic paper, this is framed as the one mechanistic takeaway: "the correctness-confidence
1293	    dissociation is a multilingual phenomenon, confirming that output-based calibration
1294	    methods face a structural ceiling regardless of language. However, this ceiling
1295	    is slightly lower for low-resource languages, suggesting that the dissociation
1296	    partly reflects representation quality rather than a pure architectural invariant."
1297	
1298	    '
1299	- name: Probe Complexity Comparison
1300	  plan_id: plan_006
1301	  description: 'Compare logistic regression vs 2-layer MLP at each probed layer for
1302	    both models. Test hypothesis that linear probes transfer better cross-lingually.
1303	
1304	    '
1305	  expected_results:
1306	    mlp_vs_logreg_en_auroc_delta_mean_pp_qwen3: 1.1
1307	    mlp_vs_logreg_en_auroc_delta_mean_pp_llama4: 0.9
1308	    mlp_vs_logreg_transfer_auroc_delta_mean_pp_qwen3: -0.4
1309	    mlp_vs_logreg_transfer_auroc_delta_mean_pp_llama4: -0.2
1310	    hypothesis_linear_transfers_better: weak support
1311	    effect_size_cohens_d: 0.18
1312	    mlp_advantage_shallow_layers_pp: 0.6
1313	    mlp_advantage_deep_layers_pp: 1.4
1314	    logreg_transfer_advantage_shallow_pp: 0.1
1315	    logreg_transfer_advantage_deep_pp: 0.7
1316	  result_rationale: 'The hypothesis that linear probes transfer better receives only
1317	    weak support. MLP probes are ~1pp better in English because the 2-layer MLP captures
1318	    mild nonlinearities in the correctness signal (interaction effects between representation
1319	    dimensions). But the cross-lingual transfer difference is tiny (-0.2 to -0.4pp
1320	    favoring logistic regression) and inconsistent across languages and layers — Cohen''s
1321	    d of 0.18 means the effect would be invisible without large sample sizes. The
1322	    interaction with depth is the most interesting signal: at deep layers, MLP probes
1323	    overfit to English-specific patterns more (1.4pp English advantage) and consequently
1324	    transfer worse (0.7pp transfer penalty). But even this effect is too small to
1325	    be practically actionable. For the paper, this confirms logistic regression as
1326	    the appropriate probe choice (simpler, nearly as good) but doesn''t generate a
1327	    standalone finding.
1328	
1329	    '
1330	  tables:
1331	  - name: 'Table 13: Probe Complexity Comparison (Mean Across All Layers)'
1332	    columns:
1333	    - model
1334	    - probe
1335	    - en_auroc_mean
1336	    - transfer_auroc_mean
1337	    - en_ece_mean
1338	    - transfer_ece_mean
1339	    rows:
1340	    - - qwen3
1341	      - logreg
1342	      - 0.714
1343	      - 0.621
1344	      - 0.206
1345	      - 0.194
1346	    - - qwen3
1347	      - mlp
1348	      - 0.725
1349	      - 0.617
1350	      - 0.198
1351	      - 0.197
1352	    - - llama4
1353	      - logreg
1354	      - 0.697
1355	      - 0.594
1356	      - 0.219
1357	      - 0.212
1358	    - - llama4
1359	      - mlp
1360	      - 0.706
1361	      - 0.592
1362	      - 0.212
1363	      - 0.214
1364	  figures_description:
1365	  - 'Figure S1 (supplementary): Paired difference plot (MLP AUROC − LogReg AUROC)
1366	    vs layer depth, one panel for English (positive differences, increasing with depth)
1367	    and one for transfer mean (negative but near-zero differences, slightly increasing
1368	    magnitude with depth). The confidence bands overlap zero at most layers for the
1369	    transfer panel.'
1370	  analysis: 'Probe complexity is a non-finding. The effect is real but negligible
1371	    (Cohen''s d 0.18). Logistic regression is the correct default choice: nearly identical
1372	    performance with fewer hyperparameters and better interpretability. This goes
1373	    into the supplementary as a methods validation, not a main finding.
1374	
1375	    '
1376	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
1377	  plan_id: plan_007
1378	  description: 'Evaluate best probes + CaCLR on Belebele (reading comprehension, 20
1379	    languages) and MMLU-ProX (translated MMLU, 20 languages).
1380	
1381	    '
1382	  expected_results:
1383	    belebele_en_auroc_qwen3: 0.741
1384	    belebele_en_auroc_llama4: 0.718
1385	    belebele_zs_transfer_mean_qwen3: 0.598
1386	    belebele_zs_transfer_mean_llama4: 0.572
1387	    belebele_drop_vs_globalmmlu_pp: 2.3
1388	    belebele_caclr_delta_vs_linproj_pp: -0.6
1389	    mmlupx_en_auroc_qwen3: 0.762
1390	    mmlupx_en_auroc_llama4: 0.738
1391	    mmlupx_zs_transfer_mean_qwen3: 0.583
1392	    mmlupx_zs_transfer_mean_llama4: 0.557
1393	    mmlupx_drop_vs_globalmmlu_pp: 3.8
1394	    mmlupx_caclr_delta_vs_linproj_pp: -0.9
1395	    lang_rank_correlation_globalmmlu_vs_belebele: 0.82
1396	    lang_rank_correlation_globalmmlu_vs_mmlupx: 0.71
1397	  result_rationale: 'Belebele partially replicates GlobalMMLU findings because it
1398	    is also a high-quality, natively multilingual benchmark where translation artifacts
1399	    are minimal. The 2.3pp drop reflects the domain shift (reading comprehension vs
1400	    knowledge questions) but the relative ranking of languages is preserved (rank
1401	    corr 0.82). MMLU-ProX shows worse transfer (3.8pp drop) because it is machine-translated
1402	    from English MMLU — translation artifacts create systematic distributional shifts
1403	    that the English-trained correctness probe cannot handle. The translation introduces
1404	    new failure modes: ambiguous translations for domain-specific terms, cultural
1405	    references that don''t transfer, and occasional errors in low-resource translations.
1406	    CaCLR is again no better than linear projection on either benchmark, confirming
1407	    the negative result generalizes beyond the training benchmark.
1408	
1409	    '
1410	  tables:
1411	  - name: 'Table 14: Cross-Benchmark Generalization (19-Language Mean)'
1412	    columns:
1413	    - benchmark
1414	    - metric
1415	    - qwen3
1416	    - llama4
1417	    rows:
1418	    - - GlobalMMLU
1419	      - zs_transfer_auroc
1420	      - 0.621
1421	      - 0.594
1422	    - - Belebele
1423	      - zs_transfer_auroc
1424	      - 0.598
1425	      - 0.572
1426	    - - MMLU-ProX
1427	      - zs_transfer_auroc
1428	      - 0.583
1429	      - 0.557
1430	    - - GlobalMMLU
1431	      - caclr_vs_linproj_pp
1432	      - -0.3
1433	      - -0.5
1434	    - - Belebele
1435	      - caclr_vs_linproj_pp
1436	      - -0.6
1437	      - -0.8
1438	    - - MMLU-ProX
1439	      - caclr_vs_linproj_pp
1440	      - -0.9
1441	      - -1.2
1442	  figures_description:
1443	  - 'Figure S2 (supplementary): Three-panel scatter plot showing per-language transfer
1444	    AUROC correlation across benchmark pairs (GlobalMMLU vs Belebele, GlobalMMLU vs
1445	    MMLU-ProX, Belebele vs MMLU-ProX). High correlation for the first pair, moderate
1446	    for others. Low-resource languages (marked in red) are consistent outliers on
1447	    MMLU-ProX due to translation quality.'
1448	  analysis: 'Results partially generalize: Belebele confirms the main findings, MMLU-ProX
1449	    is noisier due to translation artifacts. The language ranking is stable across
1450	    benchmarks (which languages transfer well vs poorly is consistent), but absolute
1451	    performance degrades with benchmark domain shift. CaCLR''s negative result is
1452	    robust across all three benchmarks — it never beats linear projection. For the
1453	    paper, include Belebele in the main results and MMLU-ProX in supplementary with
1454	    a note about translation artifacts.
1455	
1456	    '
1457	- name: INT8 Validation Ablation
1458	  plan_id: plan_010
1459	  description: 'Compare INT8 vs FP16 probing results at 5 representative layers for
1460	    Llama 4 Scout on 5% random subset. Validate that INT8 quantization doesn''t distort
1461	    correctness signals.
1462	
1463	    '
1464	  expected_results:
1465	    int8_vs_fp16_auroc_delta_mean_pp: -0.3
1466	    int8_vs_fp16_auroc_delta_max_pp: -0.7
1467	    int8_vs_fp16_ece_delta_mean_pp: 0.2
1468	    int8_vs_fp16_activation_cosine_sim_mean: 0.994
1469	    int8_vs_fp16_rank_correlation_layers: 0.98
1470	    validation_passes: true
1471	  result_rationale: 'INT8 quantization introduces minimal distortion to correctness
1472	    signals. The 0.3pp mean AUROC difference is within noise — INT8 preserves the
1473	    relative ordering of activations that linear probes rely on, even though absolute
1474	    magnitudes shift slightly. The 0.994 cosine similarity between INT8 and FP16 activations
1475	    confirms near-perfect directional alignment. This is expected because correctness
1476	    is encoded in the direction of activations, not their magnitude, and INT8 preserves
1477	    directions well. The layer ranking is identical (rank corr 0.98). This ablation
1478	    passes cleanly even in the worst tier — quantization artifacts are not the source
1479	    of any failures observed elsewhere.
1480	
1481	    '
1482	  tables:
1483	  - name: 'Table S1 (supplementary): INT8 vs FP16 Probing Comparison'
1484	    columns:
1485	    - layer
1486	    - fp16_auroc
1487	    - int8_auroc
1488	    - delta_pp
1489	    - activation_cosine
1490	    rows:
1491	    - - 8
1492	      - 0.637
1493	      - 0.633
1494	      - -0.4
1495	      - 0.993
1496	    - - 16
1497	      - 0.7
1498	      - 0.697
1499	      - -0.3
1500	      - 0.994
1501	    - - 24
1502	      - 0.731
1503	      - 0.729
1504	      - -0.2
1505	      - 0.995
1506	    - - 32
1507	      - 0.746
1508	      - 0.743
1509	      - -0.3
1510	      - 0.994
1511	    - - 40
1512	      - 0.748
1513	      - 0.741
1514	      - -0.7
1515	      - 0.992
1516	  figures_description:
1517	  - 'Figure S3 (supplementary): Paired scatter plot of FP16 vs INT8 AUROC at each
1518	    layer × language combination. Points lie tightly along the y=x diagonal with slight
1519	    downward bias. Inset shows histogram of deltas, centered near -0.3pp with tight
1520	    spread.'
1521	  analysis: 'INT8 validation passes. Quantization is not a confound for any findings
1522	    in this paper. Include in supplementary appendix as one paragraph + Table S1.
1523	
1524	    '
1525	- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)
1526	  plan_id: plan_008
1527	  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers, dense architecture,
1528	    FP16). Provides dense-vs-MoE architectural contrast for camera-ready extension.
1529	
1530	    '
1531	  expected_results:
1532	    en_auroc_best_layer: 0.761
1533	    en_best_layer_idx: 45
1534	    zs_transfer_auroc_mean_19lang: 0.608
1535	    zs_transfer_drop_mean_pp: 16.8
1536	    pareto_depth_transfer_rank_corr: 0.48
1537	    pareto_frontier_agreement_with_qwen3: 0.42
1538	    pareto_frontier_agreement_with_llama4: 0.29
1539	    caclr_vs_linproj_pp: -0.2
1540	    dense_vs_moe_finding: Dense architecture shows cleaner Pareto frontier (rank corr
1541	      0.48 vs 0.41/0.22 for MoE models) — MoE routing is a source of non-monotonic
1542	      noise in the depth-transfer relationship
1543	  result_rationale: 'Gemma 4 31B Dense shows a cleaner (but still moderate) Pareto
1544	    frontier because dense architectures have more homogeneous layer-to-layer representation
1545	    transformations — no expert routing to create non-monotonic jumps. The rank correlation
1546	    of 0.48 is the highest of the three architectures but still in the worst tier
1547	    range. English AUROC of 0.761 is between Qwen3 (0.776) and Llama4 (0.749), consistent
1548	    with its intermediate model size. Transfer is intermediate too (0.608). Cross-architecture
1549	    agreement remains low (0.42 with Qwen3, 0.29 with Llama4), confirming architecture-dependence.
1550	    The dense-vs-MoE contrast is the main value-add for camera-ready: it demonstrates
1551	    that MoE routing is a specific source of frontier noise, not just model variation.
1552	
1553	    '
1554	  tables:
1555	  - name: 'Table 15: Three-Architecture Comparison Summary'
1556	    columns:
1557	    - model
1558	    - type
1559	    - layers
1560	    - en_auroc
1561	    - transfer_auroc
1562	    - pareto_rank_corr
1563	    - pareto_agreement_mean
1564	    rows:
1565	    - - Qwen3-235B
1566	      - MoE
1567	      - 94
1568	      - 0.776
1569	      - 0.621
1570	      - 0.41
1571	      - 0.38
1572	    - - Llama4-Scout
1573	      - MoE
1574	      - 48
1575	      - 0.749
1576	      - 0.594
1577	      - 0.22
1578	      - 0.31
1579	    - - Gemma4-31B
1580	      - Dense
1581	      - 60
1582	      - 0.761
1583	      - 0.608
1584	      - 0.48
1585	      - 0.36
1586	  figures_description:
1587	  - 'Figure 6 (camera-ready): Three-panel Pareto frontier comparison (Qwen3, Llama4,
1588	    Gemma4). The dense model''s frontier is the most visually coherent, with points
1589	    forming a recognizable curve. MoE models show increasing scatter. Annotated with
1590	    rank correlation values.'
1591	  analysis: 'Gemma4 confirms the diagnostic paper''s thesis from a new angle: the
1592	    Pareto frontier is more coherent in dense architectures, implicating MoE routing
1593	    as a specific source of cross-lingual transfer noise. For camera-ready, this strengthens
1594	    the "architecture matters" message without changing the core worst-tier narrative.
1595	
1596	    '
1597	- name: Extended Language Coverage (50+ Languages, Camera-Ready)
1598	  plan_id: plan_009
1599	  description: 'Expand from 20 to 50+ languages using full GlobalMMLU/Belebele language
1600	    sets.
1601	
1602	    '
1603	  expected_results:
1604	    total_languages: 52
1605	    zs_transfer_auroc_mean_51lang: 0.587
1606	    zs_pass_rate_51lang: 0.235
1607	    new_lang_families_added: 5
1608	    low_resource_auroc_mean_new_langs: 0.548
1609	    worst_language_auroc: 0.491
1610	    resource_tier_gradient_steeper: true
1611	  result_rationale: 'Expanding to 50+ languages worsens the aggregate picture because
1612	    the additional languages are predominantly low- and very-low-resource. Many of
1613	    these languages (e.g., Amharic, Lao, Mongolian, Georgian) have minimal representation
1614	    in the models'' training data, so their internal representations share even less
1615	    structure with English. The pass rate drops from ~37% (7/19) to ~24% (12/51),
1616	    and some languages approach chance (AUROC ~0.49). For the paper, this strengthens
1617	    the diagnostic message: "probe-based calibration has a severe language barrier
1618	    that scales with the number of languages you try to cover."
1619	
1620	    '
1621	  tables:
1622	  - name: 'Table 16: Transfer Success by Resource Tier (Expanded 52-Language Set,
1623	      Qwen3)'
1624	    columns:
1625	    - resource_tier
1626	    - n_langs
1627	    - zs_auroc_mean
1628	    - zs_auroc_std
1629	    - pass_rate
1630	    rows:
1631	    - - high
1632	      - 10
1633	      - 0.653
1634	      - 0.018
1635	      - 0.7
1636	    - - mid
1637	      - 18
1638	      - 0.603
1639	      - 0.024
1640	      - 0.28
1641	    - - low
1642	      - 14
1643	      - 0.558
1644	      - 0.031
1645	      - 0.07
1646	    - - very_low
1647	      - 10
1648	      - 0.521
1649	      - 0.022
1650	      - 0.0
1651	  figures_description:
1652	  - 'Figure 7 (camera-ready): World map heatmap with 52 languages colored by zero-shot
1653	    transfer AUROC. Europe and East Asia are green/yellow (adequate transfer). South/Southeast
1654	    Asia is orange. Sub-Saharan Africa and Central Asia are red (near-chance). Visual
1655	    reinforces the ''language barrier'' framing.'
1656	  analysis: 'Extended coverage is the nail in the coffin for universal probe-based
1657	    calibration. With 52 languages, the majority fail to transfer. The resource-tier
1658	    gradient is steep and monotonic. This is the strongest evidence for the diagnostic
1659	    paper''s conclusion: "this research line does not generalize beyond a small set
1660	    of high-resource languages without fundamental methodological advances."'
1661	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93b7d840-b16a-4c6a-83c4-ff1031b70355",
  "isSidechain": false,
  "promptId": "f5a9dccd-f6bd-4a96-b7c0-602929af4008",
  "type": "user",
  "uuid": "7f9697f6-27cf-411a-b142-1e14d6ca05cf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
      "content": "tier: worst\nnarrative_guidance: 'Full reframe to field-level diagnostic paper: ''Does probe-based\n  calibration work beyond English? A systematic study across 2 architectures and 20\n  languages.'' Value proposition shifts from method contribution to first large-scale\n  answer on whether this research line generalizes. CaCLR is reported as a rigorous\n  negative result — consistency-based objectives do not help when the cross-lingual\n  correctness signal is this noisy. Decomposition is reported as evidence that difficulty\n  and capability are entangled in multilingual representations, contradicting the\n  clean separation assumed by English-only prior work. Pareto frontier is real on\n  Qwen3 but fails to replicate cleanly on Llama 4 Scout — reported as architecture-dependence\n  finding rather than universal law. Orthogonality (Claim 4) survives as the one mechanistic\n  takeaway: output-based calibration is structurally limited everywhere, not just\n  English. Target EACL with framing that negative/diagnostic results at this scale\n  (2 models × 20 languages × all layers) are community-valuable when the field is\n  actively expanding probe-based methods without multilingual validation.\n\n  '\nimagined_experiments:\n- name: Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT8)\n  plan_id: plan_001\n  description: 'Extract activations at 24 probed layers (every 4th of 94), 20 languages\n    on GlobalMMLU. Train English logistic regression + 2-layer MLP correctness probes.\n    Evaluate 5 transfer conditions: zero-shot, mean-shift, linear projection, few-shot\n    (25/100), CaCLR.\n\n    '\n  expected_results:\n    en_auroc_best_layer: 0.776\n    en_best_layer_idx: 72\n    en_auroc_range:\n    - 0.612\n    - 0.776\n    en_ece_raw_best: 0.172\n    en_ece_tempcal_best: 0.068\n    temp_scaling_T: 5.83\n    zs_transfer_auroc_mean_19lang: 0.621\n    zs_transfer_auroc_median_19lang: 0.633\n    zs_transfer_auroc_std_19lang: 0.054\n    zs_transfer_drop_mean_pp: 15.5\n    zs_pass_rate_19lang: 0.368\n    zs_pass_langs:\n    - zh\n    - fr\n    - de\n    - es\n    - ja\n    - ru\n    - ko\n    zs_fail_langs:\n    - ar\n    - hi\n    - sw\n    - yo\n    - te\n    - bn\n    - ta\n    - th\n    - vi\n    - uk\n    - id\n    - pl\n    mean_shift_improves_count: 0\n    mean_shift_mean_delta_ece_pp: 3.14\n    linproj_auroc_mean_19lang: 0.648\n    linproj_improves_over_zs_count: 13\n    linproj_mean_delta_auroc_vs_zs_pp: 2.7\n    fewshot25_auroc_mean_19lang: 0.654\n    fewshot25_improves_over_zs_count: 14\n    fewshot100_auroc_mean_19lang: 0.671\n    fewshot100_improves_over_zs_count: 16\n    pareto_depth_transfer_rank_corr: 0.41\n    pareto_frontier_monotonic: false\n    pareto_n_dominated_layers: 6\n    transfer_by_family:\n      indo_european_germanic:\n        mean: 0.672\n        langs:\n        - de\n        - en\n      indo_european_romance:\n        mean: 0.661\n        langs:\n        - fr\n        - es\n      indo_european_slavic:\n        mean: 0.629\n        langs:\n        - ru\n        - uk\n        - pl\n      indo_european_indic:\n        mean: 0.598\n        langs:\n        - hi\n        - bn\n        - te\n        - ta\n      sino_tibetan:\n        mean: 0.668\n        langs:\n        - zh\n      japonic:\n        mean: 0.651\n        langs:\n        - ja\n      koreanic:\n        mean: 0.648\n        langs:\n        - ko\n      afroasiatic:\n        mean: 0.612\n        langs:\n        - ar\n      niger_congo:\n        mean: 0.543\n        langs:\n        - sw\n        - yo\n      tai_kadai:\n        mean: 0.591\n        langs:\n        - th\n      austronesian:\n        mean: 0.618\n        langs:\n        - id\n      austroasiatic:\n        mean: 0.607\n        langs:\n        - vi\n  result_rationale: 'Qwen3-235B is a much larger MoE model than the MVP''s Qwen2.5-7B.\n    English AUROC at 0.776 improves modestly over MVP''s 0.754 because the model is\n    more capable and the correctness signal is more linearly accessible in larger\n    models, but gains are sublinear — the larger model also has more complex, distributed\n    representations that resist simple linear probing. Zero-shot transfer mean of\n    0.621 reflects the worst-tier prediction that transfer is unreliable: high-resource\n    Indo-European languages (fr, de, es) and CJK (zh, ja, ko) transfer adequately\n    because their representations share more subspace structure with English at intermediate\n    layers, but low-resource languages (sw, yo, te, bn) and languages with very different\n    morphology (th, ta) fail because the MoE routing creates language-specific expert\n    patterns that are opaque to an English-trained linear probe. Mean-shift fails\n    entirely (0/19) because the mean activation difference between languages conflates\n    content, style, and script differences — subtracting it removes useful signal.\n    The Pareto frontier rank correlation of 0.41 is real but moderate: the general\n    trend (deeper = better English, worse transfer) holds, but MoE routing introduces\n    non-monotonic noise at mid-depth layers where expert activation patterns shift.\n    The 7/19 pass rate reflects that only typologically close or high-resource languages\n    have enough representational overlap with English for zero-shot transfer to work.\n\n    '\n  tables:\n  - name: 'Table 1: Qwen3-235B English Probe Performance by Layer (Selected Layers)'\n    columns:\n    - layer\n    - depth_pct\n    - logreg_auroc\n    - mlp_auroc\n    - ece_raw\n    - ece_tempcal\n    rows:\n    - - 4\n      - 4\n      - 0.612\n      - 0.618\n      - 0.298\n      - 0.192\n    - - 16\n      - 17\n      - 0.653\n      - 0.661\n      - 0.251\n      - 0.148\n    - - 28\n      - 30\n      - 0.694\n      - 0.708\n      - 0.224\n      - 0.121\n    - - 40\n      - 43\n      - 0.721\n      - 0.737\n      - 0.203\n      - 0.098\n    - - 52\n      - 55\n      - 0.742\n      - 0.755\n      - 0.191\n      - 0.082\n    - - 60\n      - 64\n      - 0.758\n      - 0.769\n      - 0.183\n      - 0.075\n    - - 72\n      - 77\n      - 0.776\n      - 0.783\n      - 0.172\n      - 0.068\n    - - 80\n      - 85\n      - 0.771\n      - 0.779\n      - 0.176\n      - 0.071\n    - - 88\n      - 94\n      - 0.753\n      - 0.762\n      - 0.185\n      - 0.079\n    - - 92\n      - 98\n      - 0.728\n      - 0.739\n      - 0.198\n      - 0.091\n  - name: 'Table 2: Qwen3-235B Zero-Shot Transfer AUROC by Language (Best Transfer\n      Layer)'\n    columns:\n    - language\n    - family\n    - resource_tier\n    - best_zs_layer\n    - best_zs_auroc\n    - en_auroc_at_same_layer\n    - drop_pp\n    rows:\n    - - zh\n      - sino_tibetan\n      - high\n      - 52\n      - 0.668\n      - 0.742\n      - 7.4\n    - - fr\n      - romance\n      - high\n      - 52\n      - 0.672\n      - 0.742\n      - 7.0\n    - - de\n      - germanic\n      - high\n      - 52\n      - 0.671\n      - 0.742\n      - 7.1\n    - - es\n      - romance\n      - high\n      - 52\n      - 0.661\n      - 0.742\n      - 8.1\n    - - ja\n      - japonic\n      - high\n      - 48\n      - 0.651\n      - 0.735\n      - 8.4\n    - - ru\n      - slavic\n      - high\n      - 48\n      - 0.644\n      - 0.735\n      - 9.1\n    - - ko\n      - koreanic\n      - high\n      - 48\n      - 0.648\n      - 0.735\n      - 8.7\n    - - ar\n      - afroasiatic\n      - mid\n      - 40\n      - 0.612\n      - 0.721\n      - 10.9\n    - - hi\n      - indic\n      - mid\n      - 40\n      - 0.618\n      - 0.721\n      - 10.3\n    - - vi\n      - austroasiatic\n      - mid\n      - 40\n      - 0.607\n      - 0.721\n      - 11.4\n    - - id\n      - austronesian\n      - mid\n      - 40\n      - 0.618\n      - 0.721\n      - 10.3\n    - - th\n      - tai_kadai\n      - mid\n      - 40\n      - 0.591\n      - 0.721\n      - 13.0\n    - - pl\n      - slavic\n      - mid\n      - 40\n      - 0.621\n      - 0.721\n      - 10.0\n    - - uk\n      - slavic\n      - mid\n      - 40\n      - 0.614\n      - 0.721\n      - 10.7\n    - - bn\n      - indic\n      - low\n      - 28\n      - 0.583\n      - 0.694\n      - 11.1\n    - - te\n      - indic\n      - low\n      - 28\n      - 0.571\n      - 0.694\n      - 12.3\n    - - ta\n      - indic\n      - low\n      - 28\n      - 0.568\n      - 0.694\n      - 12.6\n    - - sw\n      - niger_congo\n      - low\n      - 28\n      - 0.557\n      - 0.694\n      - 13.7\n    - - yo\n      - niger_congo\n      - low\n      - 28\n      - 0.529\n      - 0.694\n      - 16.5\n  - name: 'Table 3: Qwen3-235B Transfer Method Comparison (AUROC, 19-Language Mean)'\n    columns:\n    - method\n    - auroc_mean\n    - auroc_std\n    - pass_rate\n    - ece_mean\n    - delta_vs_zs_pp\n    rows:\n    - - zero_shot\n      - 0.621\n      - 0.054\n      - 0.368\n      - 0.194\n      - 0.0\n    - - mean_shift\n      - 0.604\n      - 0.067\n      - 0.263\n      - 0.225\n      - -1.7\n    - - linear_projection\n      - 0.648\n      - 0.048\n      - 0.526\n      - 0.171\n      - 2.7\n    - - few_shot_25\n      - 0.654\n      - 0.045\n      - 0.526\n      - 0.166\n      - 3.3\n    - - few_shot_100\n      - 0.671\n      - 0.041\n      - 0.632\n      - 0.152\n      - 5.0\n  figures_description:\n  - 'Figure 1a: Heatmap of zero-shot transfer AUROC (y-axis: 24 probed layers sorted\n    by depth, x-axis: 20 languages sorted by resource tier). Shows a gradient where\n    upper-left (deep layers × high-resource langs) has moderate AUROC (~0.65-0.67)\n    and lower-right (shallow layers × low-resource langs) is near chance (~0.52-0.57).\n    But the pattern is noisy — no crisp diagonal boundary. Several mid-depth layers\n    show unexpected dips (layers 48-56) breaking monotonicity.'\n  - 'Figure 1b: Pareto frontier scatter plot (x-axis: mean 19-lang zero-shot AUROC,\n    y-axis: English AUROC at same layer). Each point is a layer. The Pareto front\n    connects 6 non-dominated layers but the remaining 18 points scatter widely around\n    it. Convex hull is thin — the tradeoff is real but the frontier offers limited\n    choice. Error bars (bootstrap 95% CI) overlap substantially between adjacent Pareto-optimal\n    points.'\n  - 'Figure 1c: Line plot of zero-shot transfer drop (EN AUROC minus target-lang AUROC)\n    vs layer depth, one line per language, colored by resource tier. High-resource\n    languages (blue) show a gentle upward slope (deeper = worse transfer). Low-resource\n    languages (red) show a steep upward slope. The spread between lines increases\n    with depth, illustrating that the Pareto tradeoff is more severe for low-resource\n    languages.'\n  analysis: 'The Pareto frontier is real on Qwen3-235B but weak: rank correlation\n    of 0.41 means the depth-transfer tradeoff explains only ~17% of variance. MoE\n    routing creates non-monotonic perturbations at mid-depth. The practical implication\n    is limited — the frontier provides modest guidance for layer selection but is\n    not a reliable engineering tool. Zero-shot transfer fails for 12/19 languages\n    (AUROC < 0.65), with a clear resource-tier gradient. The field should not assume\n    English-trained correctness probes transfer to low-resource languages. Mean-shift\n    is confirmed dead at scale. Linear projection and few-shot are the only viable\n    transfer methods, with few-shot-100 achieving the best results — but requiring\n    100 labeled examples per language partially negates the zero-label promise.\n\n    '\n- name: Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, INT8)\n  plan_id: plan_002\n  description: 'Extract activations at 12 probed layers (every 4th of 48), 20 languages\n    on GlobalMMLU. Train English correctness probes, evaluate 5 transfer conditions.\n\n    '\n  expected_results:\n    en_auroc_best_layer: 0.749\n    en_best_layer_idx: 36\n    en_auroc_range:\n    - 0.598\n    - 0.749\n    en_ece_raw_best: 0.188\n    en_ece_tempcal_best: 0.074\n    temp_scaling_T: 5.47\n    zs_transfer_auroc_mean_19lang: 0.594\n    zs_transfer_auroc_median_19lang: 0.601\n    zs_transfer_auroc_std_19lang: 0.061\n    zs_transfer_drop_mean_pp: 18.2\n    zs_pass_rate_19lang: 0.211\n    zs_pass_langs:\n    - zh\n    - fr\n    - de\n    - es\n    zs_fail_langs:\n    - ja\n    - ru\n    - ko\n    - ar\n    - hi\n    - sw\n    - yo\n    - te\n    - bn\n    - ta\n    - th\n    - vi\n    - uk\n    - id\n    - pl\n    mean_shift_improves_count: 0\n    mean_shift_mean_delta_ece_pp: 4.21\n    linproj_auroc_mean_19lang: 0.623\n    linproj_improves_over_zs_count: 11\n    fewshot25_auroc_mean_19lang: 0.631\n    fewshot100_auroc_mean_19lang: 0.652\n    pareto_depth_transfer_rank_corr: 0.22\n    pareto_frontier_monotonic: false\n    pareto_n_dominated_layers: 3\n    pareto_frontier_agreement_with_qwen3: 0.33\n    nonmonotonic_layers:\n    - 20\n    - 24\n    - 28\n  result_rationale: 'Llama 4 Scout is the worst-tier''s key failure point. Its Pareto\n    frontier is flat/non-monotonic (rank correlation 0.22) because Llama 4 Scout''s\n    MoE architecture uses a different routing strategy than Qwen3-235B: its experts\n    are more language-specialized at intermediate layers, meaning the English correctness\n    direction at layers 20-28 is entangled with English-specific expert activations\n    in ways that neither degrade nor improve monotonically with depth. English AUROC\n    peaks at 0.749 (lower than Qwen3''s 0.776) because Llama 4 Scout''s 48 layers\n    compress the representational hierarchy — the same functional stages are packed\n    into fewer layers, leaving less room for a clean correctness signal to emerge.\n    Zero-shot transfer is worse overall (mean 0.594 vs Qwen3''s 0.621) because Llama\n    4 Scout''s training data distribution is more English-centric, and its MoE routing\n    assigns non-English tokens to a sparser expert set that shares less structure\n    with the English experts. Only 4/19 languages pass the 0.65 threshold. The 0.33\n    cross-architecture Pareto agreement means the optimal layer for a given language\n    on Qwen3 does not predict the optimal layer on Llama 4 — the tradeoff is architecture-specific,\n    not a universal property of transformer depth.\n\n    '\n  tables:\n  - name: 'Table 4: Llama 4 Scout English Probe Performance by Layer'\n    columns:\n    - layer\n    - depth_pct\n    - logreg_auroc\n    - mlp_auroc\n    - ece_raw\n    - ece_tempcal\n    rows:\n    - - 4\n      - 8\n      - 0.598\n      - 0.604\n      - 0.312\n      - 0.201\n    - - 8\n      - 17\n      - 0.631\n      - 0.641\n      - 0.274\n      - 0.168\n    - - 12\n      - 25\n      - 0.668\n      - 0.679\n      - 0.241\n      - 0.137\n    - - 16\n      - 33\n      - 0.694\n      - 0.706\n      - 0.218\n      - 0.112\n    - - 20\n      - 42\n      - 0.712\n      - 0.722\n      - 0.205\n      - 0.098\n    - - 24\n      - 50\n      - 0.726\n      - 0.735\n      - 0.196\n      - 0.088\n    - - 28\n      - 58\n      - 0.734\n      - 0.743\n      - 0.192\n      - 0.083\n    - - 32\n      - 67\n      - 0.741\n      - 0.749\n      - 0.189\n      - 0.078\n    - - 36\n      - 75\n      - 0.749\n      - 0.755\n      - 0.188\n      - 0.074\n    - - 40\n      - 83\n      - 0.744\n      - 0.751\n      - 0.19\n      - 0.077\n    - - 44\n      - 92\n      - 0.731\n      - 0.738\n      - 0.195\n      - 0.084\n    - - 48\n      - 100\n      - 0.708\n      - 0.718\n      - 0.209\n      - 0.097\n  - name: 'Table 5: Llama 4 Scout Zero-Shot Transfer AUROC by Language (Best Transfer\n      Layer)'\n    columns:\n    - language\n    - best_zs_layer\n    - best_zs_auroc\n    - drop_vs_en_pp\n    rows:\n    - - zh\n      - 24\n      - 0.658\n      - 6.8\n    - - fr\n      - 24\n      - 0.662\n      - 6.4\n    - - de\n      - 24\n      - 0.655\n      - 7.1\n    - - es\n      - 24\n      - 0.651\n      - 7.5\n    - - ja\n      - 20\n      - 0.631\n      - 8.1\n    - - ru\n      - 20\n      - 0.622\n      - 9.0\n    - - ko\n      - 20\n      - 0.627\n      - 8.5\n    - - ar\n      - 16\n      - 0.589\n      - 10.5\n    - - hi\n      - 16\n      - 0.594\n      - 10.0\n    - - vi\n      - 16\n      - 0.581\n      - 11.3\n    - - id\n      - 16\n      - 0.591\n      - 10.3\n    - - th\n      - 16\n      - 0.568\n      - 12.6\n    - - pl\n      - 20\n      - 0.608\n      - 10.4\n    - - uk\n      - 16\n      - 0.592\n      - 10.2\n    - - bn\n      - 12\n      - 0.556\n      - 11.2\n    - - te\n      - 12\n      - 0.541\n      - 12.7\n    - - ta\n      - 12\n      - 0.538\n      - 13.0\n    - - sw\n      - 12\n      - 0.524\n      - 14.4\n    - - yo\n      - 12\n      - 0.498\n      - 17.0\n  - name: 'Table 6: Cross-Architecture Pareto Frontier Agreement'\n    columns:\n    - metric\n    - qwen3_235b\n    - llama4_scout\n    - agreement\n    rows:\n    - - rank_corr_depth_vs_transfer\n      - 0.41\n      - 0.22\n      - —\n    - - pareto_optimal_layer_count\n      - 6/24\n      - 3/12\n      - —\n    - - best_transfer_layer_pct_depth\n      - 55%\n      - 50%\n      - —\n    - - zs_mean_auroc\n      - 0.621\n      - 0.594\n      - —\n    - - optimal_layer_rank_agreement_tau\n      - —\n      - —\n      - 0.33\n    - - pass_lang_overlap_jaccard\n      - —\n      - —\n      - 0.44\n  figures_description:\n  - 'Figure 2a: Side-by-side Pareto frontier scatter plots for Qwen3-235B (left) and\n    Llama 4 Scout (right). Qwen3 shows a discernible convex Pareto front with 6 non-dominated\n    points forming a curve from upper-left (high EN, low transfer) to lower-right\n    (low EN, high transfer). Llama 4 shows a near-flat cloud with only 3 weakly non-dominated\n    points — no meaningful tradeoff curve. The contrast is the paper''s key Figure\n    2 evidence that the Pareto frontier is architecture-dependent.'\n  - 'Figure 2b: Llama 4 Scout non-monotonicity detail: line plot of transfer AUROC\n    vs layer depth for zh, fr, ar, sw. The zh/fr lines show a bump at layer 20, dip\n    at 24, recover at 28 — violating the monotonic depth-transfer assumption. This\n    is attributed to MoE expert routing transitions at these layers.'\n  analysis: 'Llama 4 Scout is the worst-tier''s smoking gun for the diagnostic reframe.\n    The Pareto frontier essentially doesn''t exist on this architecture (rank corr\n    0.22, only 3 non-dominated layers). This is the strongest evidence for the diagnostic\n    paper''s thesis: the depth-transfer tradeoff from Claim 1 is not a universal property\n    of transformers but an architecture-dependent phenomenon that cannot be assumed\n    to generalize. The 0.33 cross-architecture agreement means practitioners cannot\n    use findings from one model to guide layer selection on another. For the paper,\n    this transforms from a weakness into a key finding: the field cannot assume probe-based\n    calibration will behave consistently across architectures.\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: 'Implement CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency). Train CaCLR\n    probes using English labels + unlabeled parallel activations. Compare vs all 5\n    transfer conditions across full Pareto frontier for both models × 20 languages.\n\n    '\n  expected_results:\n    caclr_auroc_mean_qwen3: 0.645\n    caclr_auroc_mean_llama4: 0.618\n    caclr_vs_linproj_auroc_delta_pp_qwen3: -0.3\n    caclr_vs_linproj_auroc_delta_pp_llama4: -0.5\n    caclr_vs_zs_auroc_delta_pp_qwen3: 2.4\n    caclr_vs_zs_auroc_delta_pp_llama4: 2.4\n    caclr_vs_fewshot100_auroc_delta_pp_qwen3: -2.6\n    caclr_vs_fewshot100_auroc_delta_pp_llama4: -3.4\n    caclr_improvement_pass_rate_qwen3: 0.47\n    caclr_improvement_pass_rate_llama4: 0.37\n    caclr_ece_mean_qwen3: 0.174\n    caclr_ece_mean_llama4: 0.189\n    caclr_ece_reduction_vs_tempcal_pct_qwen3: 7.2\n    caclr_ece_reduction_vs_tempcal_pct_llama4: 3.8\n    best_alpha: 0.3\n    best_beta: 0.05\n    alpha_sensitivity: moderate — ±0.1 changes AUROC by ~0.5pp\n    beta_sensitivity: flat — β from 0.01 to 0.5 changes AUROC by <0.3pp, indicating\n      consistency loss is inert\n    caclr_no_consistency_auroc_mean: 0.647\n    caclr_no_sbece_auroc_mean: 0.629\n    caclr_bce_only_auroc_mean: 0.621\n    caclr_per_lang_qwen3:\n      zh:\n        auroc: 0.671\n        delta_vs_zs: 0.3\n        delta_vs_linproj: -0.8\n      fr:\n        auroc: 0.668\n        delta_vs_zs: -0.4\n        delta_vs_linproj: -1.2\n      de:\n        auroc: 0.665\n        delta_vs_zs: -0.6\n        delta_vs_linproj: -0.9\n      es:\n        auroc: 0.658\n        delta_vs_zs: -0.3\n        delta_vs_linproj: -0.7\n      ja:\n        auroc: 0.649\n        delta_vs_zs: -0.2\n        delta_vs_linproj: -0.4\n      ru:\n        auroc: 0.641\n        delta_vs_zs: -0.3\n        delta_vs_linproj: -0.6\n      ko:\n        auroc: 0.647\n        delta_vs_zs: -0.1\n        delta_vs_linproj: -0.3\n      ar:\n        auroc: 0.628\n        delta_vs_zs: 1.6\n        delta_vs_linproj: 0.2\n      hi:\n        auroc: 0.635\n        delta_vs_zs: 1.7\n        delta_vs_linproj: 0.1\n      vi:\n        auroc: 0.621\n        delta_vs_zs: 1.4\n        delta_vs_linproj: -0.3\n      id:\n        auroc: 0.633\n        delta_vs_zs: 1.5\n        delta_vs_linproj: -0.1\n      th:\n        auroc: 0.607\n        delta_vs_zs: 1.6\n        delta_vs_linproj: 0.3\n      pl:\n        auroc: 0.638\n        delta_vs_zs: 1.7\n        delta_vs_linproj: 0.1\n      uk:\n        auroc: 0.631\n        delta_vs_zs: 1.7\n        delta_vs_linproj: 0.2\n      bn:\n        auroc: 0.601\n        delta_vs_zs: 1.8\n        delta_vs_linproj: 0.5\n      te:\n        auroc: 0.589\n        delta_vs_zs: 1.8\n        delta_vs_linproj: 0.4\n      ta:\n        auroc: 0.587\n        delta_vs_zs: 1.9\n        delta_vs_linproj: 0.6\n      sw:\n        auroc: 0.578\n        delta_vs_zs: 2.1\n        delta_vs_linproj: 0.9\n      yo:\n        auroc: 0.551\n        delta_vs_zs: 2.2\n        delta_vs_linproj: 0.7\n  result_rationale: 'CaCLR''s consistency loss (L_consistency) is designed to align\n    cross-lingual probe activations so that the English probe generalizes. In the\n    worst tier, this fails because the cross-lingual correctness signal is too noisy\n    for the consistency objective to find meaningful invariances. The unlabeled parallel\n    activations contain language-specific variance (script, morphology, tokenization\n    artifacts) that dominates the correctness signal, so minimizing distributional\n    distance between languages collapses both signal and noise. The hyperparameter\n    search confirms this: β (consistency weight) is driven to near-zero (0.05), and\n    removing the consistency term entirely slightly improves performance (+0.2pp).\n    The SB-ECE term helps modestly because it acts as a calibration regularizer on\n    the English side, but this benefit doesn''t compound with consistency. CaCLR ends\n    up being essentially \"zero-shot + SB-ECE regularization\" — functionally a slightly\n    calibration-aware version of the base probe. Linear projection beats CaCLR because\n    projection directly estimates and applies the affine transformation between language\n    representation subspaces, which is a more efficient use of the few available parallel\n    datapoints than trying to learn an invariant representation. The key insight:\n    simple alignment (linproj) outperforms principled invariance (CaCLR) when the\n    signal-to-noise ratio of the target signal is low. For high-resource languages\n    that already transfer well, CaCLR''s overhead yields no benefit; for low-resource\n    languages where help is needed, the consistency signal is too noisy to learn from.\n\n    '\n  tables:\n  - name: 'Table 7: Transfer Method Comparison Summary (19-Language Mean, Both Architectures)'\n    columns:\n    - method\n    - qwen3_auroc\n    - qwen3_ece\n    - llama4_auroc\n    - llama4_ece\n    - labels_needed\n    rows:\n    - - zero_shot\n      - 0.621\n      - 0.194\n      - 0.594\n      - 0.212\n      - 0 target\n    - - mean_shift\n      - 0.604\n      - 0.225\n      - 0.571\n      - 0.248\n      - 0 target (fails)\n    - - linear_projection\n      - 0.648\n      - 0.171\n      - 0.623\n      - 0.189\n      - ~50 parallel\n    - - CaCLR\n      - 0.645\n      - 0.174\n      - 0.618\n      - 0.193\n      - 0 target + parallel\n    - - few_shot_25\n      - 0.654\n      - 0.166\n      - 0.631\n      - 0.182\n      - 25 target\n    - - few_shot_100\n      - 0.671\n      - 0.152\n      - 0.652\n      - 0.168\n      - 100 target\n  - name: 'Table 8: CaCLR Ablation (Qwen3-235B, 19-Language Mean)'\n    columns:\n    - variant\n    - auroc_mean\n    - ece_mean\n    - delta_vs_full_pp\n    rows:\n    - - Full CaCLR (BCE+SB-ECE+Consistency)\n      - 0.645\n      - 0.174\n      - 0.0\n    - - CaCLR − Consistency (BCE+SB-ECE)\n      - 0.647\n      - 0.172\n      - 0.2\n    - - CaCLR − SB-ECE (BCE+Consistency)\n      - 0.629\n      - 0.188\n      - -1.6\n    - - BCE Only (= zero-shot probe)\n      - 0.621\n      - 0.194\n      - -2.4\n    - - Linear Projection\n      - 0.648\n      - 0.171\n      - 0.3\n  figures_description:\n  - 'Figure 3a: Grouped bar chart comparing 6 transfer methods across 20 languages\n    (Qwen3-235B), sorted by language resource tier. Shows that few-shot-100 > few-shot-25\n    ≈ linear projection ≈ CaCLR > zero-shot >> mean-shift. CaCLR and linear projection\n    bars are nearly identical in height across all languages. The visual message is\n    clear: CaCLR adds complexity without benefit.'\n  - 'Figure 3b: Hyperparameter sensitivity plot for CaCLR. Left panel: AUROC vs α\n    (SB-ECE weight), showing a gentle inverted-U peaking at α=0.3. Right panel: AUROC\n    vs β (consistency weight), showing a flat line — β has no effect. This is the\n    key visual evidence that the consistency objective is inert.'\n  - 'Figure 3c: Scatter plot of per-language CaCLR improvement (y-axis) vs zero-shot\n    baseline AUROC (x-axis). Shows that CaCLR helps low-resource languages modestly\n    (+1-2pp) but slightly hurts high-resource languages that already transfer well\n    (-0.3 to -1.2pp). Linear projection shows the same pattern but with uniformly\n    better outcomes. Net: CaCLR''s mechanism doesn''t add value over simple geometric\n    alignment.'\n  analysis: 'CaCLR is a rigorous negative result. The consistency loss term — the\n    core methodological novelty — is inert. This is not a hyperparameter tuning failure;\n    β is swept over 3 orders of magnitude and the landscape is flat. The SB-ECE term\n    provides modest calibration regularization, but this benefit is available without\n    any cross-lingual machinery. Linear projection achieves the same or better results\n    with a simpler mechanism. For the paper, this is framed as: \"consistency-based\n    cross-lingual alignment objectives do not help when the underlying correctness\n    signal has low cross-lingual SNR. This negative result saves the community from\n    pursuing distributional-matching approaches (adversarial, MMD, consistency) for\n    this problem class.\"\n\n    '\n- name: Difficulty-Controlled Ablation (Decomposition)\n  plan_id: plan_004\n  description: 'Train IRT difficulty probes, project out difficulty direction from\n    activations, retrain correctness probes on residuals, evaluate transfer. 10 representative\n    languages × 8 representative layers per model.\n\n    '\n  expected_results:\n    difficulty_probe_r2_en_qwen3: 0.52\n    difficulty_probe_r2_en_llama4: 0.47\n    difficulty_probe_transfer_r2_mean_9lang: 0.41\n    decomp_difficulty_var_explained_pct_qwen3: 14.3\n    decomp_difficulty_var_explained_pct_llama4: 11.8\n    correctness_residual_auroc_en_qwen3: 0.738\n    correctness_residual_auroc_en_llama4: 0.711\n    correctness_residual_transfer_auroc_mean_qwen3: 0.607\n    correctness_residual_transfer_auroc_mean_llama4: 0.581\n    transfer_improvement_after_projection: false\n    transfer_delta_after_projection_pp_qwen3: -1.4\n    transfer_delta_after_projection_pp_llama4: -1.3\n    difficulty_correctness_cosine_mean_qwen3: 0.34\n    difficulty_correctness_cosine_mean_llama4: 0.38\n    difficulty_correctness_cosine_std: 0.11\n    subspace_overlap_mean_angle_deg: 58\n  result_rationale: 'In the worst tier, difficulty and capability are entangled in\n    cross-lingual representations. The difficulty direction explains only 14% (Qwen3)\n    / 12% (Llama4) of correctness probe variance — real but modest. Critically, projecting\n    out difficulty makes transfer WORSE (-1.3 to -1.4pp), not better. This is because\n    the difficulty-shared component actually carries useful cross-lingual signal:\n    questions that are hard in English tend to be hard everywhere due to shared conceptual\n    complexity, and this shared difficulty signal is one of the few reliable cross-lingual\n    bridges for the correctness probe. Removing it strips away a genuine cross-lingual\n    invariance. The residual \"capability-specific\" component is more language-dependent,\n    not less — it contains the idiosyncratic ways each language''s tokens encode competence,\n    which are precisely the non-transferable signals. The cosine similarity of 0.34-0.38\n    between difficulty and correctness directions confirms they are neither orthogonal\n    nor aligned — they share a moderate subspace that cannot be cleanly separated.\n    This contradicts the paper''s original Claim 2 hypothesis that decomposition would\n    be prescriptive. The decomposition is real but useless: it describes variance\n    structure without enabling better transfer.\n\n    '\n  tables:\n  - name: 'Table 9: Difficulty Probe Quality (Ridge Regression, R² on Held-Out)'\n    columns:\n    - language\n    - qwen3_r2\n    - llama4_r2\n    - is_transfer\n    rows:\n    - - en\n      - 0.52\n      - 0.47\n      - false\n    - - zh\n      - 0.48\n      - 0.43\n      - true\n    - - fr\n      - 0.47\n      - 0.42\n      - true\n    - - de\n      - 0.46\n      - 0.41\n      - true\n    - - ar\n      - 0.42\n      - 0.37\n      - true\n    - - hi\n      - 0.41\n      - 0.36\n      - true\n    - - ja\n      - 0.44\n      - 0.39\n      - true\n    - - ko\n      - 0.43\n      - 0.38\n      - true\n    - - sw\n      - 0.33\n      - 0.28\n      - true\n    - - yo\n      - 0.29\n      - 0.24\n      - true\n  - name: 'Table 10: Decomposition Transfer Ablation (9-Language Mean)'\n    columns:\n    - condition\n    - qwen3_auroc\n    - qwen3_delta_pp\n    - llama4_auroc\n    - llama4_delta_pp\n    rows:\n    - - Full activations (baseline)\n      - 0.621\n      - 0.0\n      - 0.594\n      - 0.0\n    - - Residual (difficulty projected out)\n      - 0.607\n      - -1.4\n      - 0.581\n      - -1.3\n    - - Difficulty component only\n      - 0.568\n      - -5.3\n      - 0.551\n      - -4.3\n    - - Random direction projected out (ctrl)\n      - 0.618\n      - -0.3\n      - 0.591\n      - -0.3\n  figures_description:\n  - 'Figure 4a: Scatter plot of correctness AUROC vs difficulty R² across 10 languages\n    × 8 layers, colored by model. Shows moderate positive correlation (r=0.41) — layers\n    where difficulty is well-encoded also support better correctness probing. This\n    contradicts the expectation that difficulty is a confound to be removed.'\n  - 'Figure 4b: Principal angle distribution between difficulty and correctness subspaces\n    across layers. Histogram peaks at ~55-60° — far from both 0° (fully shared) and\n    90° (fully orthogonal). The wide spread (std ~11°) across layers and languages\n    shows the relationship is inconsistent, preventing clean decomposition.'\n  analysis: 'Decomposition fails as a prescriptive tool. The difficulty-shared component,\n    far from being a confound, is actually one of the more reliable cross-lingual\n    bridges — removing it hurts. The capability-specific residual is more language-dependent,\n    not less, because it captures idiosyncratic encoding patterns. For the diagnostic\n    paper, this finding is reframed as: \"difficulty and capability are entangled in\n    multilingual representations, unlike the clean separation reported in English-only\n    work. This entanglement may be fundamental to how multilingual models represent\n    knowledge — the shared difficulty structure is load-bearing for cross-lingual\n    transfer, not a confound to be controlled for.\"\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: 'Extract verbalized confidence direction, compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier and language family.\n\n    '\n  expected_results:\n    orthogonality_cosine_mean_overall: 0.072\n    orthogonality_cosine_std_overall: 0.038\n    orthogonality_cosine_mean_qwen3: 0.068\n    orthogonality_cosine_mean_llama4: 0.076\n    orthogonality_cosine_range:\n    - 0.018\n    - 0.148\n    orthogonality_cosine_high_resource: 0.054\n    orthogonality_cosine_mid_resource: 0.071\n    orthogonality_cosine_low_resource: 0.098\n    pct_langs_cosine_below_0_1: 0.75\n    pct_langs_cosine_below_0_05: 0.35\n    confidence_probe_r2_mean: 0.68\n    confidence_probe_transfer_drops: true\n  result_rationale: 'Orthogonality persists cross-lingually (mean cosine 0.072, all\n    languages below 0.15) because it is a structural property of how LLMs represent\n    confidence vs correctness — the model''s verbalized confidence is calibrated to\n    appear confident regardless of actual correctness, and this dissociation is encoded\n    geometrically at the representation level. However, the worst-tier variance is\n    higher than Miao & Ungar''s English-only finding (std 0.038 vs their ~0.01): low-resource\n    languages show less orthogonality (cosine ~0.098) because the model has less capacity\n    to maintain the confidence-correctness dissociation for languages with limited\n    training data — when the model is uncertain due to lack of language-specific knowledge,\n    both its correctness and confidence signals degrade in correlated ways, slightly\n    breaking orthogonality. Reviewers may see this as incremental: Miao & Ungar showed\n    orthogonality for English, we extend to 20 languages, but the finding is qualitatively\n    the same. The resource- tier modulation is the one novel angle but the effect\n    size is modest (0.054 vs 0.098).\n\n    '\n  tables:\n  - name: 'Table 11: Correctness-Confidence Cosine Similarity by Language'\n    columns:\n    - language\n    - resource_tier\n    - qwen3_cosine\n    - llama4_cosine\n    - mean_cosine\n    rows:\n    - - en\n      - high\n      - 0.038\n      - 0.041\n      - 0.04\n    - - zh\n      - high\n      - 0.042\n      - 0.049\n      - 0.046\n    - - fr\n      - high\n      - 0.045\n      - 0.051\n      - 0.048\n    - - de\n      - high\n      - 0.047\n      - 0.054\n      - 0.051\n    - - es\n      - high\n      - 0.049\n      - 0.056\n      - 0.053\n    - - ja\n      - high\n      - 0.055\n      - 0.062\n      - 0.059\n    - - ru\n      - high\n      - 0.058\n      - 0.064\n      - 0.061\n    - - ko\n      - high\n      - 0.061\n      - 0.068\n      - 0.065\n    - - ar\n      - mid\n      - 0.063\n      - 0.072\n      - 0.068\n    - - hi\n      - mid\n      - 0.065\n      - 0.075\n      - 0.07\n    - - vi\n      - mid\n      - 0.068\n      - 0.077\n      - 0.073\n    - - id\n      - mid\n      - 0.064\n      - 0.073\n      - 0.069\n    - - th\n      - mid\n      - 0.072\n      - 0.082\n      - 0.077\n    - - pl\n      - mid\n      - 0.059\n      - 0.067\n      - 0.063\n    - - uk\n      - mid\n      - 0.062\n      - 0.071\n      - 0.067\n    - - bn\n      - low\n      - 0.081\n      - 0.092\n      - 0.087\n    - - te\n      - low\n      - 0.088\n      - 0.098\n      - 0.093\n    - - ta\n      - low\n      - 0.091\n      - 0.103\n      - 0.097\n    - - sw\n      - low\n      - 0.098\n      - 0.112\n      - 0.105\n    - - yo\n      - low\n      - 0.112\n      - 0.148\n      - 0.13\n  - name: 'Table 12: Orthogonality by Resource Tier (Mean Cosine ± Std)'\n    columns:\n    - resource_tier\n    - n_langs\n    - qwen3_mean\n    - llama4_mean\n    - overall_mean\n    - std\n    rows:\n    - - high\n      - 8\n      - 0.049\n      - 0.056\n      - 0.054\n      - 0.009\n    - - mid\n      - 7\n      - 0.065\n      - 0.074\n      - 0.071\n      - 0.005\n    - - low\n      - 5\n      - 0.094\n      - 0.111\n      - 0.098\n      - 0.016\n    - - all\n      - 20\n      - 0.066\n      - 0.076\n      - 0.072\n      - 0.022\n  figures_description:\n  - 'Figure 5a: Bar chart of cosine similarity (correctness vs confidence direction)\n    for 20 languages, sorted by resource tier, with Miao & Ungar''s English-only threshold\n    (0.04) marked as a horizontal dashed line. Most high-resource languages cluster\n    near the line; low-resource languages are 2-3× higher but still below 0.15. The\n    visual confirms orthogonality persists everywhere but the quantitative story is\n    noisier than prior work suggested.'\n  - 'Figure 5b: Scatter plot of orthogonality cosine (y-axis) vs zero-shot transfer\n    AUROC (x-axis), per language. Moderate negative correlation (r ≈ -0.62): languages\n    where orthogonality is stronger (lower cosine) also transfer better. This connects\n    Claims 1 and 4 — representation quality covaries with both metrics — but the causal\n    direction is ambiguous.'\n  analysis: 'Claim 4 survives in the worst tier but its contribution is incremental.\n    Orthogonality persists (mean 0.072, all < 0.15) — output-based calibration is\n    indeed structurally limited everywhere. The resource-tier gradient (high: 0.054,\n    mid: 0.071, low: 0.098) is novel but the effect size is modest. The correlation\n    between orthogonality and transfer success is intriguing but not causal. For the\n    diagnostic paper, this is framed as the one mechanistic takeaway: \"the correctness-confidence\n    dissociation is a multilingual phenomenon, confirming that output-based calibration\n    methods face a structural ceiling regardless of language. However, this ceiling\n    is slightly lower for low-resource languages, suggesting that the dissociation\n    partly reflects representation quality rather than a pure architectural invariant.\"\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Compare logistic regression vs 2-layer MLP at each probed layer for\n    both models. Test hypothesis that linear probes transfer better cross-lingually.\n\n    '\n  expected_results:\n    mlp_vs_logreg_en_auroc_delta_mean_pp_qwen3: 1.1\n    mlp_vs_logreg_en_auroc_delta_mean_pp_llama4: 0.9\n    mlp_vs_logreg_transfer_auroc_delta_mean_pp_qwen3: -0.4\n    mlp_vs_logreg_transfer_auroc_delta_mean_pp_llama4: -0.2\n    hypothesis_linear_transfers_better: weak support\n    effect_size_cohens_d: 0.18\n    mlp_advantage_shallow_layers_pp: 0.6\n    mlp_advantage_deep_layers_pp: 1.4\n    logreg_transfer_advantage_shallow_pp: 0.1\n    logreg_transfer_advantage_deep_pp: 0.7\n  result_rationale: 'The hypothesis that linear probes transfer better receives only\n    weak support. MLP probes are ~1pp better in English because the 2-layer MLP captures\n    mild nonlinearities in the correctness signal (interaction effects between representation\n    dimensions). But the cross-lingual transfer difference is tiny (-0.2 to -0.4pp\n    favoring logistic regression) and inconsistent across languages and layers — Cohen''s\n    d of 0.18 means the effect would be invisible without large sample sizes. The\n    interaction with depth is the most interesting signal: at deep layers, MLP probes\n    overfit to English-specific patterns more (1.4pp English advantage) and consequently\n    transfer worse (0.7pp transfer penalty). But even this effect is too small to\n    be practically actionable. For the paper, this confirms logistic regression as\n    the appropriate probe choice (simpler, nearly as good) but doesn''t generate a\n    standalone finding.\n\n    '\n  tables:\n  - name: 'Table 13: Probe Complexity Comparison (Mean Across All Layers)'\n    columns:\n    - model\n    - probe\n    - en_auroc_mean\n    - transfer_auroc_mean\n    - en_ece_mean\n    - transfer_ece_mean\n    rows:\n    - - qwen3\n      - logreg\n      - 0.714\n      - 0.621\n      - 0.206\n      - 0.194\n    - - qwen3\n      - mlp\n      - 0.725\n      - 0.617\n      - 0.198\n      - 0.197\n    - - llama4\n      - logreg\n      - 0.697\n      - 0.594\n      - 0.219\n      - 0.212\n    - - llama4\n      - mlp\n      - 0.706\n      - 0.592\n      - 0.212\n      - 0.214\n  figures_description:\n  - 'Figure S1 (supplementary): Paired difference plot (MLP AUROC − LogReg AUROC)\n    vs layer depth, one panel for English (positive differences, increasing with depth)\n    and one for transfer mean (negative but near-zero differences, slightly increasing\n    magnitude with depth). The confidence bands overlap zero at most layers for the\n    transfer panel.'\n  analysis: 'Probe complexity is a non-finding. The effect is real but negligible\n    (Cohen''s d 0.18). Logistic regression is the correct default choice: nearly identical\n    performance with fewer hyperparameters and better interpretability. This goes\n    into the supplementary as a methods validation, not a main finding.\n\n    '\n- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: 'Evaluate best probes + CaCLR on Belebele (reading comprehension, 20\n    languages) and MMLU-ProX (translated MMLU, 20 languages).\n\n    '\n  expected_results:\n    belebele_en_auroc_qwen3: 0.741\n    belebele_en_auroc_llama4: 0.718\n    belebele_zs_transfer_mean_qwen3: 0.598\n    belebele_zs_transfer_mean_llama4: 0.572\n    belebele_drop_vs_globalmmlu_pp: 2.3\n    belebele_caclr_delta_vs_linproj_pp: -0.6\n    mmlupx_en_auroc_qwen3: 0.762\n    mmlupx_en_auroc_llama4: 0.738\n    mmlupx_zs_transfer_mean_qwen3: 0.583\n    mmlupx_zs_transfer_mean_llama4: 0.557\n    mmlupx_drop_vs_globalmmlu_pp: 3.8\n    mmlupx_caclr_delta_vs_linproj_pp: -0.9\n    lang_rank_correlation_globalmmlu_vs_belebele: 0.82\n    lang_rank_correlation_globalmmlu_vs_mmlupx: 0.71\n  result_rationale: 'Belebele partially replicates GlobalMMLU findings because it\n    is also a high-quality, natively multilingual benchmark where translation artifacts\n    are minimal. The 2.3pp drop reflects the domain shift (reading comprehension vs\n    knowledge questions) but the relative ranking of languages is preserved (rank\n    corr 0.82). MMLU-ProX shows worse transfer (3.8pp drop) because it is machine-translated\n    from English MMLU — translation artifacts create systematic distributional shifts\n    that the English-trained correctness probe cannot handle. The translation introduces\n    new failure modes: ambiguous translations for domain-specific terms, cultural\n    references that don''t transfer, and occasional errors in low-resource translations.\n    CaCLR is again no better than linear projection on either benchmark, confirming\n    the negative result generalizes beyond the training benchmark.\n\n    '\n  tables:\n  - name: 'Table 14: Cross-Benchmark Generalization (19-Language Mean)'\n    columns:\n    - benchmark\n    - metric\n    - qwen3\n    - llama4\n    rows:\n    - - GlobalMMLU\n      - zs_transfer_auroc\n      - 0.621\n      - 0.594\n    - - Belebele\n      - zs_transfer_auroc\n      - 0.598\n      - 0.572\n    - - MMLU-ProX\n      - zs_transfer_auroc\n      - 0.583\n      - 0.557\n    - - GlobalMMLU\n      - caclr_vs_linproj_pp\n      - -0.3\n      - -0.5\n    - - Belebele\n      - caclr_vs_linproj_pp\n      - -0.6\n      - -0.8\n    - - MMLU-ProX\n      - caclr_vs_linproj_pp\n      - -0.9\n      - -1.2\n  figures_description:\n  - 'Figure S2 (supplementary): Three-panel scatter plot showing per-language transfer\n    AUROC correlation across benchmark pairs (GlobalMMLU vs Belebele, GlobalMMLU vs\n    MMLU-ProX, Belebele vs MMLU-ProX). High correlation for the first pair, moderate\n    for others. Low-resource languages (marked in red) are consistent outliers on\n    MMLU-ProX due to translation quality.'\n  analysis: 'Results partially generalize: Belebele confirms the main findings, MMLU-ProX\n    is noisier due to translation artifacts. The language ranking is stable across\n    benchmarks (which languages transfer well vs poorly is consistent), but absolute\n    performance degrades with benchmark domain shift. CaCLR''s negative result is\n    robust across all three benchmarks — it never beats linear projection. For the\n    paper, include Belebele in the main results and MMLU-ProX in supplementary with\n    a note about translation artifacts.\n\n    '\n- name: INT8 Validation Ablation\n  plan_id: plan_010\n  description: 'Compare INT8 vs FP16 probing results at 5 representative layers for\n    Llama 4 Scout on 5% random subset. Validate that INT8 quantization doesn''t distort\n    correctness signals.\n\n    '\n  expected_results:\n    int8_vs_fp16_auroc_delta_mean_pp: -0.3\n    int8_vs_fp16_auroc_delta_max_pp: -0.7\n    int8_vs_fp16_ece_delta_mean_pp: 0.2\n    int8_vs_fp16_activation_cosine_sim_mean: 0.994\n    int8_vs_fp16_rank_correlation_layers: 0.98\n    validation_passes: true\n  result_rationale: 'INT8 quantization introduces minimal distortion to correctness\n    signals. The 0.3pp mean AUROC difference is within noise — INT8 preserves the\n    relative ordering of activations that linear probes rely on, even though absolute\n    magnitudes shift slightly. The 0.994 cosine similarity between INT8 and FP16 activations\n    confirms near-perfect directional alignment. This is expected because correctness\n    is encoded in the direction of activations, not their magnitude, and INT8 preserves\n    directions well. The layer ranking is identical (rank corr 0.98). This ablation\n    passes cleanly even in the worst tier — quantization artifacts are not the source\n    of any failures observed elsewhere.\n\n    '\n  tables:\n  - name: 'Table S1 (supplementary): INT8 vs FP16 Probing Comparison'\n    columns:\n    - layer\n    - fp16_auroc\n    - int8_auroc\n    - delta_pp\n    - activation_cosine\n    rows:\n    - - 8\n      - 0.637\n      - 0.633\n      - -0.4\n      - 0.993\n    - - 16\n      - 0.7\n      - 0.697\n      - -0.3\n      - 0.994\n    - - 24\n      - 0.731\n      - 0.729\n      - -0.2\n      - 0.995\n    - - 32\n      - 0.746\n      - 0.743\n      - -0.3\n      - 0.994\n    - - 40\n      - 0.748\n      - 0.741\n      - -0.7\n      - 0.992\n  figures_description:\n  - 'Figure S3 (supplementary): Paired scatter plot of FP16 vs INT8 AUROC at each\n    layer × language combination. Points lie tightly along the y=x diagonal with slight\n    downward bias. Inset shows histogram of deltas, centered near -0.3pp with tight\n    spread.'\n  analysis: 'INT8 validation passes. Quantization is not a confound for any findings\n    in this paper. Include in supplementary appendix as one paragraph + Table S1.\n\n    '\n- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)\n  plan_id: plan_008\n  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers, dense architecture,\n    FP16). Provides dense-vs-MoE architectural contrast for camera-ready extension.\n\n    '\n  expected_results:\n    en_auroc_best_layer: 0.761\n    en_best_layer_idx: 45\n    zs_transfer_auroc_mean_19lang: 0.608\n    zs_transfer_drop_mean_pp: 16.8\n    pareto_depth_transfer_rank_corr: 0.48\n    pareto_frontier_agreement_with_qwen3: 0.42\n    pareto_frontier_agreement_with_llama4: 0.29\n    caclr_vs_linproj_pp: -0.2\n    dense_vs_moe_finding: Dense architecture shows cleaner Pareto frontier (rank corr\n      0.48 vs 0.41/0.22 for MoE models) — MoE routing is a source of non-monotonic\n      noise in the depth-transfer relationship\n  result_rationale: 'Gemma 4 31B Dense shows a cleaner (but still moderate) Pareto\n    frontier because dense architectures have more homogeneous layer-to-layer representation\n    transformations — no expert routing to create non-monotonic jumps. The rank correlation\n    of 0.48 is the highest of the three architectures but still in the worst tier\n    range. English AUROC of 0.761 is between Qwen3 (0.776) and Llama4 (0.749), consistent\n    with its intermediate model size. Transfer is intermediate too (0.608). Cross-architecture\n    agreement remains low (0.42 with Qwen3, 0.29 with Llama4), confirming architecture-dependence.\n    The dense-vs-MoE contrast is the main value-add for camera-ready: it demonstrates\n    that MoE routing is a specific source of frontier noise, not just model variation.\n\n    '\n  tables:\n  - name: 'Table 15: Three-Architecture Comparison Summary'\n    columns:\n    - model\n    - type\n    - layers\n    - en_auroc\n    - transfer_auroc\n    - pareto_rank_corr\n    - pareto_agreement_mean\n    rows:\n    - - Qwen3-235B\n      - MoE\n      - 94\n      - 0.776\n      - 0.621\n      - 0.41\n      - 0.38\n    - - Llama4-Scout\n      - MoE\n      - 48\n      - 0.749\n      - 0.594\n      - 0.22\n      - 0.31\n    - - Gemma4-31B\n      - Dense\n      - 60\n      - 0.761\n      - 0.608\n      - 0.48\n      - 0.36\n  figures_description:\n  - 'Figure 6 (camera-ready): Three-panel Pareto frontier comparison (Qwen3, Llama4,\n    Gemma4). The dense model''s frontier is the most visually coherent, with points\n    forming a recognizable curve. MoE models show increasing scatter. Annotated with\n    rank correlation values.'\n  analysis: 'Gemma4 confirms the diagnostic paper''s thesis from a new angle: the\n    Pareto frontier is more coherent in dense architectures, implicating MoE routing\n    as a specific source of cross-lingual transfer noise. For camera-ready, this strengthens\n    the \"architecture matters\" message without changing the core worst-tier narrative.\n\n    '\n- name: Extended Language Coverage (50+ Languages, Camera-Ready)\n  plan_id: plan_009\n  description: 'Expand from 20 to 50+ languages using full GlobalMMLU/Belebele language\n    sets.\n\n    '\n  expected_results:\n    total_languages: 52\n    zs_transfer_auroc_mean_51lang: 0.587\n    zs_pass_rate_51lang: 0.235\n    new_lang_families_added: 5\n    low_resource_auroc_mean_new_langs: 0.548\n    worst_language_auroc: 0.491\n    resource_tier_gradient_steeper: true\n  result_rationale: 'Expanding to 50+ languages worsens the aggregate picture because\n    the additional languages are predominantly low- and very-low-resource. Many of\n    these languages (e.g., Amharic, Lao, Mongolian, Georgian) have minimal representation\n    in the models'' training data, so their internal representations share even less\n    structure with English. The pass rate drops from ~37% (7/19) to ~24% (12/51),\n    and some languages approach chance (AUROC ~0.49). For the paper, this strengthens\n    the diagnostic message: \"probe-based calibration has a severe language barrier\n    that scales with the number of languages you try to cover.\"\n\n    '\n  tables:\n  - name: 'Table 16: Transfer Success by Resource Tier (Expanded 52-Language Set,\n      Qwen3)'\n    columns:\n    - resource_tier\n    - n_langs\n    - zs_auroc_mean\n    - zs_auroc_std\n    - pass_rate\n    rows:\n    - - high\n      - 10\n      - 0.653\n      - 0.018\n      - 0.7\n    - - mid\n      - 18\n      - 0.603\n      - 0.024\n      - 0.28\n    - - low\n      - 14\n      - 0.558\n      - 0.031\n      - 0.07\n    - - very_low\n      - 10\n      - 0.521\n      - 0.022\n      - 0.0\n  figures_description:\n  - 'Figure 7 (camera-ready): World map heatmap with 52 languages colored by zero-shot\n    transfer AUROC. Europe and East Asia are green/yellow (adequate transfer). South/Southeast\n    Asia is orange. Sub-Saharan Africa and Central Asia are red (near-chance). Visual\n    reinforces the ''language barrier'' framing.'\n  analysis: 'Extended coverage is the nail in the coffin for universal probe-based\n    calibration. With 52 languages, the majority fail to transfer. The resource-tier\n    gradient is steep and monotonic. This is the strongest evidence for the diagnostic\n    paper''s conclusion: \"this research line does not generalize beyond a small set\n    of high-resource languages without fundamental methodological advances.\"'\n",
      "numLines": 1661,
      "startLine": 1,
      "totalLines": 1661
    }
  },
  "sourceToolAssistantUUID": "93b7d840-b16a-4c6a-83c4-ff1031b70355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T20:31:54.699Z_

<details open><summary>🔧 Tool call — Read · `toolu_015Lw135PJ343PaoxqvkL4LK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f9697f6-27cf-411a-b142-1e14d6ca05cf",
  "isSidechain": false,
  "requestId": "req_011CbETRiwsGPd9ctxeZFfxv",
  "type": "assistant",
  "uuid": "3874057a-2d3c-44da-8f83-2499df89cd04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBKXnGFU1Y6jkcSU5y9CPf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1804,
      "cache_read_input_tokens": 25396,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 25396,
          "cache_creation_input_tokens": 1804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1804
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decomposition is inconclusive; but cross-lingual probing viability data and the mean-s…",
  "leafUuid": "3874057a-2d3c-44da-8f83-2499df89cd04",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Probe-based calibration fails multilingually—few-shot and mechanistic insights",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Tool result

_source line 18 · 2026-05-20T20:31:54.961Z_

<details><summary>↩ Tool result · `toolu_015Lw135PJ343PaoxqvkL4LK`</summary>

```text
1	tier: best
2	narrative_guidance: 'Original framing stands: "CaCLR shifts the cross-lingual calibration
3	  Pareto frontier." All 4 claims form an unbroken causal chain — discovery → analysis
4	  → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling
5	  with zero target-language labels. Pareto frontier is the organizing principle, CaCLR
6	  is the actionable contribution, decomposition explains why it works, orthogonality
7	  explains why output-based methods can''t.
8	
9	  '
10	imagined_experiments:
11	- name: Full Pareto Frontier — Qwen3-235B-A22B
12	  plan_id: plan_001
13	  description: 'Extract activations at every 4th layer (24 probed layers out of 94),
14	    20 languages, train English correctness probes (logistic regression + 2-layer
15	    MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection,
16	    few-shot 25/100, CaCLR).
17	
18	    '
19	  expected_results:
20	    en_auroc_best_layer: 0.843
21	    en_best_layer_idx: 72
22	    en_auroc_range:
23	    - 0.621
24	    - 0.843
25	    en_ece_raw_best: 0.162
26	    en_ece_tempcal_best: 0.054
27	    temp_scaling_T: 4.87
28	    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.762
29	    zs_best_transfer_layer_idx: 56
30	    zs_transfer_drop_from_en_mean_pp: 8.1
31	    zs_auroc_by_tier:
32	      high_resource_mean: 0.791
33	      mid_resource_mean: 0.754
34	      low_resource_mean: 0.683
35	    zs_auroc_by_lang:
36	      en: 0.843
37	      zh: 0.802
38	      de: 0.796
39	      fr: 0.793
40	      es: 0.789
41	      ja: 0.785
42	      ru: 0.782
43	      pt: 0.788
44	      it: 0.786
45	      ar: 0.768
46	      hi: 0.761
47	      ko: 0.755
48	      vi: 0.749
49	      th: 0.743
50	      bn: 0.738
51	      tr: 0.756
52	      nl: 0.79
53	      sw: 0.695
54	      yo: 0.672
55	      ig: 0.681
56	    mean_shift_improvement_count: 2
57	    mean_shift_delta_ece_mean: 1.41
58	    linproj_auroc_mean_19lang: 0.724
59	    fewshot_25_auroc_mean_19lang: 0.748
60	    fewshot_100_auroc_mean_19lang: 0.771
61	    pareto_depth_transfer_rank_corr: 0.88
62	    pareto_frontier_layers:
63	    - 40
64	    - 44
65	    - 48
66	    - 52
67	    - 56
68	    - 60
69	    layers_above_0p5_auroc_count: 22
70	  result_rationale: 'Qwen3-235B-A22B is a 94-layer MoE with massive representation
71	    capacity. The jump from MVP''s 7B (en AUROC 0.754) to 235B is expected to yield
72	    ~9pp AUROC gain, consistent with prior probing literature showing log-linear scaling
73	    of linear probe accuracy with model parameters (Burns et al., Marks et al.). The
74	    MoE architecture concentrates expert representations, producing cleaner correctness
75	    signals in intermediate layers. The Pareto frontier emerges because deeper layers
76	    (L72+) specialize for English-dominant pretraining data distribution — the model''s
77	    language-specific processing intensifies past ~75% depth, degrading cross-lingual
78	    invariance. The best transfer layer (L56, ~60% depth) sits in the "universal reasoning"
79	    zone before language-specific heads activate. Low-resource languages (sw, yo,
80	    ig) still transfer above 0.65 AUROC because GlobalMMLU questions share structural
81	    patterns that even underrepresented languages partially align with in middle layers.
82	    Mean-shift continues to mostly fail because correctness directions are not simply
83	    mean-offset between languages — they require rotation, not translation, which
84	    linear projection and CaCLR address.
85	
86	    '
87	  tables:
88	  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by
89	      Layer'
90	    columns:
91	    - layer_idx
92	    - layer_depth_pct
93	    - en_auroc
94	    - zs_mean_auroc_19
95	    - zs_drop_pp
96	    - on_pareto
97	    rows:
98	    - - 4
99	      - 4
100	      - 0.621
101	      - 0.608
102	      - 1.3
103	      - false
104	    - - 8
105	      - 9
106	      - 0.648
107	      - 0.637
108	      - 1.1
109	      - false
110	    - - 12
111	      - 13
112	      - 0.689
113	      - 0.671
114	      - 1.8
115	      - false
116	    - - 16
117	      - 17
118	      - 0.712
119	      - 0.698
120	      - 1.4
121	      - false
122	    - - 20
123	      - 21
124	      - 0.738
125	      - 0.724
126	      - 1.4
127	      - false
128	    - - 24
129	      - 26
130	      - 0.756
131	      - 0.742
132	      - 1.4
133	      - false
134	    - - 28
135	      - 30
136	      - 0.771
137	      - 0.755
138	      - 1.6
139	      - false
140	    - - 32
141	      - 34
142	      - 0.784
143	      - 0.764
144	      - 2.0
145	      - false
146	    - - 36
147	      - 38
148	      - 0.795
149	      - 0.771
150	      - 2.4
151	      - false
152	    - - 40
153	      - 43
154	      - 0.803
155	      - 0.776
156	      - 2.7
157	      - true
158	    - - 44
159	      - 47
160	      - 0.81
161	      - 0.774
162	      - 3.6
163	      - true
164	    - - 48
165	      - 51
166	      - 0.816
167	      - 0.77
168	      - 4.6
169	      - true
170	    - - 52
171	      - 55
172	      - 0.822
173	      - 0.765
174	      - 5.7
175	      - true
176	    - - 56
177	      - 60
178	      - 0.827
179	      - 0.762
180	      - 6.5
181	      - true
182	    - - 60
183	      - 64
184	      - 0.831
185	      - 0.753
186	      - 7.8
187	      - true
188	    - - 64
189	      - 68
190	      - 0.835
191	      - 0.741
192	      - 9.4
193	      - false
194	    - - 68
195	      - 72
196	      - 0.839
197	      - 0.728
198	      - 11.1
199	      - false
200	    - - 72
201	      - 77
202	      - 0.843
203	      - 0.712
204	      - 13.1
205	      - false
206	    - - 76
207	      - 81
208	      - 0.841
209	      - 0.694
210	      - 14.7
211	      - false
212	    - - 80
213	      - 85
214	      - 0.838
215	      - 0.671
216	      - 16.7
217	      - false
218	    - - 84
219	      - 89
220	      - 0.832
221	      - 0.643
222	      - 18.9
223	      - false
224	    - - 88
225	      - 94
226	      - 0.819
227	      - 0.611
228	      - 20.8
229	      - false
230	    - - 92
231	      - 98
232	      - 0.791
233	      - 0.574
234	      - 21.7
235	      - false
236	    - - 94
237	      - 100
238	      - 0.762
239	      - 0.541
240	      - 22.1
241	      - false
242	  - name: 'Table 2: Transfer Condition Comparison (at best-transfer layer L56)'
243	    columns:
244	    - condition
245	    - auroc_mean_19
246	    - ece_mean_19
247	    - ece_reduction_vs_tempcal_pct
248	    rows:
249	    - - zero-shot
250	      - 0.762
251	      - 0.098
252	      - 0
253	    - - mean-shift
254	      - 0.758
255	      - 0.101
256	      - -3.1
257	    - - linear_projection
258	      - 0.781
259	      - 0.082
260	      - 16.3
261	    - - few-shot-25
262	      - 0.748
263	      - 0.089
264	      - 9.2
265	    - - few-shot-100
266	      - 0.771
267	      - 0.079
268	      - 19.4
269	    - - CaCLR
270	      - 0.814
271	      - 0.058
272	      - 40.8
273	  figures_description:
274	  - 'Figure 1a: Pareto frontier scatter plot (EN AUROC x-axis vs ZS mean AUROC y-axis),
275	    each point a layer, Pareto-optimal layers highlighted in red. Clear convex frontier
276	    shape from L40-L60.'
277	  - 'Figure 1b: Heatmap of ZS AUROC by language (y-axis, ordered by resource tier)
278	    × layer depth (x-axis). Shows warm band in mid-layers, cooling at extremes, with
279	    low-resource langs cooling earlier.'
280	  analysis: 'The Pareto frontier is crisp and monotonic: 6 layers form the efficient
281	    frontier between L40-L60. The rank correlation (Spearman) between layer depth
282	    and transfer degradation is ρ=0.88 (p<0.001). The frontier''s shape confirms that
283	    the depth- transferability tradeoff is not an artifact of small models — it amplifies
284	    at scale. The 16pp gap between best-EN layer (L72) and best-transfer layer (L56)
285	    is larger than MVP''s ~3-layer gap, consistent with deeper models having more
286	    room for language-specific specialization. All high-resource languages pass AUROC
287	    > 0.75 at the best-transfer layer; all low-resource languages exceed 0.65.
288	
289	    '
290	- name: Full Pareto Frontier — Llama 4 Scout
291	  plan_id: plan_002
292	  description: 'Extract activations at every 4th layer (12 probed layers out of 48),
293	    20 languages, 5 transfer conditions. INT8 weight quantization.
294	
295	    '
296	  expected_results:
297	    en_auroc_best_layer: 0.821
298	    en_best_layer_idx: 36
299	    en_auroc_range:
300	    - 0.634
301	    - 0.821
302	    en_ece_raw_best: 0.174
303	    en_ece_tempcal_best: 0.061
304	    temp_scaling_T: 5.34
305	    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.741
306	    zs_best_transfer_layer_idx: 28
307	    zs_transfer_drop_from_en_mean_pp: 8.0
308	    zs_auroc_by_tier:
309	      high_resource_mean: 0.771
310	      mid_resource_mean: 0.733
311	      low_resource_mean: 0.661
312	    zs_auroc_by_lang:
313	      en: 0.821
314	      zh: 0.784
315	      de: 0.778
316	      fr: 0.775
317	      es: 0.771
318	      ja: 0.766
319	      ru: 0.762
320	      pt: 0.77
321	      it: 0.768
322	      ar: 0.748
323	      hi: 0.741
324	      ko: 0.735
325	      vi: 0.729
326	      th: 0.722
327	      bn: 0.718
328	      tr: 0.737
329	      nl: 0.772
330	      sw: 0.674
331	      yo: 0.641
332	      ig: 0.667
333	    mean_shift_improvement_count: 1
334	    linproj_auroc_mean_19lang: 0.706
335	    fewshot_25_auroc_mean_19lang: 0.728
336	    fewshot_100_auroc_mean_19lang: 0.752
337	    pareto_depth_transfer_rank_corr: 0.82
338	    pareto_frontier_layers:
339	    - 20
340	    - 24
341	    - 28
342	    - 32
343	  result_rationale: 'Llama 4 Scout has 48 layers (fewer than Qwen3''s 94) and a different
344	    MoE routing strategy (16 experts, top-2). With roughly 109B total / ~17B active
345	    params, its active compute is smaller than Qwen3-235B''s ~22B active. This yields
346	    ~2pp lower EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer
347	    points (4 vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but
348	    the monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout''s best
349	    transfer layer sits at ~58% depth (L28), remarkably close to Qwen3''s 60%, suggesting
350	    a universal "mid-depth transfer zone" across architectures. The rank correlation
351	    is slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant.
352	    Low-resource languages are slightly weaker because Meta''s multilingual pretraining
353	    mix underrepresents African languages compared to Qwen3.
354	
355	    '
356	  tables:
357	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
358	    columns:
359	    - layer_idx
360	    - layer_depth_pct
361	    - en_auroc
362	    - zs_mean_auroc_19
363	    - zs_drop_pp
364	    - on_pareto
365	    rows:
366	    - - 4
367	      - 8
368	      - 0.634
369	      - 0.624
370	      - 1.0
371	      - false
372	    - - 8
373	      - 17
374	      - 0.672
375	      - 0.659
376	      - 1.3
377	      - false
378	    - - 12
379	      - 25
380	      - 0.714
381	      - 0.699
382	      - 1.5
383	      - false
384	    - - 16
385	      - 33
386	      - 0.745
387	      - 0.729
388	      - 1.6
389	      - false
390	    - - 20
391	      - 42
392	      - 0.768
393	      - 0.748
394	      - 2.0
395	      - true
396	    - - 24
397	      - 50
398	      - 0.786
399	      - 0.745
400	      - 4.1
401	      - true
402	    - - 28
403	      - 58
404	      - 0.798
405	      - 0.741
406	      - 5.7
407	      - true
408	    - - 32
409	      - 67
410	      - 0.81
411	      - 0.732
412	      - 7.8
413	      - true
414	    - - 36
415	      - 75
416	      - 0.821
417	      - 0.714
418	      - 10.7
419	      - false
420	    - - 40
421	      - 83
422	      - 0.818
423	      - 0.689
424	      - 12.9
425	      - false
426	    - - 44
427	      - 92
428	      - 0.804
429	      - 0.651
430	      - 15.3
431	      - false
432	    - - 48
433	      - 100
434	      - 0.771
435	      - 0.608
436	      - 16.3
437	      - false
438	  - name: 'Table 4: Cross-Architecture Pareto Frontier Agreement'
439	    columns:
440	    - metric
441	    - qwen3_235b
442	    - llama4_scout
443	    - agreement
444	    rows:
445	    - - best_en_layer_depth_pct
446	      - 77
447	      - 75
448	      - within 2pp
449	    - - best_transfer_layer_depth_pct
450	      - 60
451	      - 58
452	      - within 2pp
453	    - - pareto_zone_depth_range_pct
454	      - 43-64
455	      - 42-67
456	      - overlapping
457	    - - depth_transfer_rank_corr
458	      - 0.88
459	      - 0.82
460	      - both >0.75
461	    - - frontier_shape
462	      - convex monotonic
463	      - convex monotonic
464	      - consistent
465	  figures_description:
466	  - 'Figure 2: Overlaid Pareto frontiers for both architectures (normalized depth
467	    %). Shows near-identical frontier shapes with Qwen3 shifted up-right (better overall)
468	    but same curvature.'
469	  analysis: 'Cross-architecture agreement is high: both models show best transfer
470	    at ~59% depth, the Pareto frontier occupies the 42-67% depth band, and the rank
471	    correlation between depth and transfer degradation exceeds 0.75 in both. The frontier
472	    shape is architecture-invariant — it''s the depth-normalized position, not absolute
473	    layer count, that determines the tradeoff. This validates Claim 1 at scale.
474	
475	    '
476	- name: CaCLR Implementation and Comparative Evaluation
477	  plan_id: plan_003
478	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train
479	    on English labels + unlabeled parallel activations. Compare vs all 5 conditions
480	    across full Pareto frontier, both models × 20 languages. Hyperparameter tuning
481	    (α, β).
482	
483	    '
484	  expected_results:
485	    best_alpha: 0.15
486	    best_beta: 0.08
487	    qwen3_caclr_auroc_mean_19lang: 0.814
488	    qwen3_caclr_ece_mean_19lang: 0.058
489	    qwen3_caclr_vs_linproj_auroc_delta_pp: 3.3
490	    qwen3_caclr_vs_zeroshot_auroc_delta_pp: 5.2
491	    qwen3_caclr_ece_reduction_vs_tempcal_pct: 40.8
492	    qwen3_caclr_best_operating_layer: 64
493	    llama4_caclr_auroc_mean_19lang: 0.793
494	    llama4_caclr_ece_mean_19lang: 0.064
495	    llama4_caclr_vs_linproj_auroc_delta_pp: 3.1
496	    llama4_caclr_vs_zeroshot_auroc_delta_pp: 5.2
497	    llama4_caclr_ece_reduction_vs_tempcal_pct: 38.5
498	    llama4_caclr_best_operating_layer: 32
499	    caclr_vs_linproj_auroc_delta_pp_mean: 3.2
500	    caclr_ece_reduction_vs_tempcal_pct_mean: 39.7
501	    caclr_improvement_pass_rate: 0.92
502	    caclr_pareto_shift_layers: 2
503	    low_resource_caclr_auroc:
504	      sw_qwen3: 0.731
505	      yo_qwen3: 0.709
506	      ig_qwen3: 0.718
507	      sw_llama4: 0.712
508	      yo_llama4: 0.681
509	      ig_llama4: 0.698
510	    low_resource_zs_pass_rate: 1.0
511	  result_rationale: 'CaCLR''s consistency loss (β·L_consistency) directly penalizes
512	    divergence between EN and non-EN probe outputs on parallel/comparable activations,
513	    forcing the probe to learn language-invariant features. This is strictly more
514	    informative than linear projection (which only aligns means and covariances post-hoc)
515	    because it shapes the learned representation during training. The 3.2pp AUROC
516	    gain over linear projection reflects the value of end-to-end optimization: linear
517	    projection corrects first-order distributional mismatch but not the nonlinear
518	    feature interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE)
519	    provides calibration-aware training that temperature scaling cannot — it directly
520	    optimizes the calibration objective rather than post-hoc rescaling. The 40% ECE
521	    reduction over temperature scaling arises because CaCLR addresses the root cause
522	    (representation misalignment) rather than the symptom (miscalibrated probabilities).
523	    The Pareto frontier shift is the key result: CaCLR allows operating 2 layers deeper
524	    than the ZS-optimal point while maintaining equivalent or better transfer — it
525	    literally pushes the Pareto frontier outward. Low-resource languages benefit most
526	    from L_consistency because their activation distributions are most misaligned
527	    from EN; the consistency term provides the strongest gradient signal precisely
528	    where the gap is largest.
529	
530	    '
531	  tables:
532	  - name: 'Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)'
533	    columns:
534	    - method
535	    - auroc_mean_19
536	    - ece_mean_19
537	    - requires_target_labels
538	    - params_overhead
539	    rows:
540	    - - zero-shot
541	      - 0.752
542	      - 0.098
543	      - 'no'
544	      - '0'
545	    - - mean-shift
546	      - 0.747
547	      - 0.102
548	      - 'no'
549	      - '0'
550	    - - linear_projection
551	      - 0.77
552	      - 0.082
553	      - 'no'
554	      - d×d matrix
555	    - - few-shot-25
556	      - 0.738
557	      - 0.089
558	      - yes (25)
559	      - '0'
560	    - - few-shot-100
561	      - 0.762
562	      - 0.079
563	      - yes (100)
564	      - '0'
565	    - - CaCLR
566	      - 0.804
567	      - 0.061
568	      - 'no'
569	      - ~1% probe params
570	  - name: 'Table 6: CaCLR Ablation — Loss Component Contributions'
571	    columns:
572	    - configuration
573	    - auroc_mean_19
574	    - ece_mean_19
575	    - delta_vs_full_auroc_pp
576	    rows:
577	    - - L_BCE_only (= zero-shot probe)
578	      - 0.752
579	      - 0.098
580	      - -5.2
581	    - - L_BCE + L_SB-ECE
582	      - 0.768
583	      - 0.072
584	      - -3.6
585	    - - L_BCE + L_consistency
586	      - 0.793
587	      - 0.078
588	      - -1.1
589	    - - L_BCE + L_SB-ECE + L_consistency (full CaCLR)
590	      - 0.804
591	      - 0.061
592	      - 0.0
593	  - name: 'Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)'
594	    columns:
595	    - layer_idx
596	    - zs_auroc_19
597	    - caclr_auroc_19
598	    - shift_pp
599	    - on_shifted_pareto
600	    rows:
601	    - - 40
602	      - 0.776
603	      - 0.798
604	      - 2.2
605	      - false
606	    - - 44
607	      - 0.774
608	      - 0.8
609	      - 2.6
610	      - false
611	    - - 48
612	      - 0.77
613	      - 0.803
614	      - 3.3
615	      - true
616	    - - 52
617	      - 0.765
618	      - 0.806
619	      - 4.1
620	      - true
621	    - - 56
622	      - 0.762
623	      - 0.81
624	      - 4.8
625	      - true
626	    - - 60
627	      - 0.753
628	      - 0.814
629	      - 6.1
630	      - true
631	    - - 64
632	      - 0.741
633	      - 0.814
634	      - 7.3
635	      - true
636	    - - 68
637	      - 0.728
638	      - 0.808
639	      - 8.0
640	      - true
641	    - - 72
642	      - 0.712
643	      - 0.796
644	      - 8.4
645	      - false
646	  figures_description:
647	  - 'Figure 3: Pareto frontier before/after CaCLR. ZS frontier (blue) vs CaCLR frontier
648	    (red), showing outward shift. CaCLR''s optimal operating point is 2 layers deeper
649	    with +5pp transfer AUROC.'
650	  - 'Figure 4: Per-language AUROC improvement from CaCLR over linear projection, grouped
651	    by resource tier. Low-resource languages show largest gains (4-6pp), high-resource
652	    2-3pp.'
653	  - 'Figure 5: Loss component ablation bar chart — stacked contributions of L_SB-ECE
654	    and L_consistency to final AUROC and ECE improvements.'
655	  analysis: 'CaCLR decisively outperforms all baselines. The ablation shows both loss
656	    terms contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp
657	    alone), while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to
658	    0.061 when added). The interaction is synergistic — joint optimization yields
659	    better results than either term alone. The Pareto shift is the headline result:
660	    at the same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer
661	    vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation
662	    from "use shallower layers for transfer" to "use CaCLR and operate at deeper,
663	    better-calibrated layers." The improvement pass rate of 92% (35/38 model-lang
664	    pairs) demonstrates consistency. The 3 non-improving pairs are high-resource languages
665	    (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already excellent and
666	    the consistency loss has minimal signal to exploit.
667	
668	    '
669	- name: Difficulty-Controlled Ablation
670	  plan_id: plan_004
671	  description: 'IRT difficulty probes (Ridge regression), project out difficulty direction,
672	    retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers
673	    per model.
674	
675	    '
676	  expected_results:
677	    difficulty_probe_r2_mean: 0.72
678	    difficulty_var_explained_pct_mean: 68.4
679	    difficulty_var_explained_pct_range:
680	    - 58.2
681	    - 79.1
682	    residual_en_auroc_drop_pp: 4.2
683	    residual_zs_transfer_drop_pp: 1.1
684	    capability_specific_var_pct: 31.6
685	    capability_specific_transfer_degradation_pct: 87
686	    difficulty_component_transfer_degradation_pct: 13
687	    decomp_prescriptive_accuracy: 0.81
688	    difficulty_var_by_depth:
689	      shallow_20pct: 0.74
690	      mid_50pct: 0.69
691	      deep_80pct: 0.62
692	    capability_transfer_drop_by_depth:
693	      shallow_20pct: 0.8
694	      mid_50pct: 3.4
695	      deep_80pct: 9.7
696	  result_rationale: 'IRT difficulty is a strong, language-agnostic property — harder
697	    questions are harder everywhere. Ridge regression captures this cleanly (R²=0.72)
698	    because difficulty is linearly encoded in intermediate representations (Civelli
699	    et al. confirmed this). The difficulty component accounts for 68% of explained
700	    variance because GlobalMMLU correctness is heavily driven by item difficulty:
701	    a model gets easy questions right in all languages and hard questions wrong in
702	    all languages. After projecting out difficulty, the residual correctness signal
703	    is "capability-specific" — it captures language-dependent competence differences.
704	    This residual transfers poorly at deep layers (9.7pp drop at 80% depth vs 0.8pp
705	    at 20% depth) because deep layers encode language-specific processing that makes
706	    capability assessments non-transferable. The difficulty component transfers well
707	    at all depths (only 13% of total transfer degradation) because it''s language-invariant
708	    by construction. This decomposition is prescriptive: when difficulty explains
709	    most of a language''s correctness variance, simple zero-shot transfer suffices;
710	    when the capability residual is large, CaCLR is needed. The 81% prescriptive accuracy
711	    validates the decomposition as more than descriptive.
712	
713	    '
714	  tables:
715	  - name: 'Table 8: Decomposition Results — Difficulty vs Capability Components'
716	    columns:
717	    - component
718	    - var_explained_pct
719	    - transfer_auroc_mean
720	    - transfer_drop_from_en_pp
721	    - share_of_total_transfer_drop_pct
722	    rows:
723	    - - full_correctness
724	      - 100
725	      - 0.752
726	      - 8.1
727	      - 100
728	    - - difficulty_shared
729	      - 68.4
730	      - 0.738
731	      - 1.1
732	      - 13
733	    - - capability_specific
734	      - 31.6
735	      - 0.614
736	      - 14.2
737	      - 87
738	  - name: 'Table 9: Capability-Specific Transfer Drop by Depth'
739	    columns:
740	    - depth_band
741	    - difficulty_transfer_drop_pp
742	    - capability_transfer_drop_pp
743	    - ratio
744	    rows:
745	    - - 0-30%
746	      - 0.3
747	      - 0.8
748	      - 2.7×
749	    - - 30-60%
750	      - 0.8
751	      - 3.4
752	      - 4.3×
753	    - - 60-90%
754	      - 1.6
755	      - 9.7
756	      - 6.1×
757	  figures_description:
758	  - 'Figure 6: Stacked area chart showing difficulty vs capability variance across
759	    depth. Difficulty dominates at all depths but capability grows at deeper layers.'
760	  - 'Figure 7: Transfer degradation decomposed into difficulty (flat, near-zero) and
761	    capability (exponentially increasing with depth) components.'
762	  analysis: 'The decomposition cleanly separates: difficulty-shared signal is the
763	    majority (68%) of correctness variance and transfers near-perfectly across languages
764	    and depths. The capability-specific residual (32%) drives nearly all transfer
765	    degradation (87%), and this degradation accelerates exponentially with depth.
766	    This explains the Pareto frontier mechanistically: deeper layers have stronger
767	    capability-specific signals that improve EN calibration but impede transfer. CaCLR
768	    works because its consistency loss specifically targets the capability-specific
769	    component — forcing alignment of the non-difficulty residual across languages.
770	    The prescriptive value (81% accuracy in predicting when CaCLR is needed) confirms
771	    this is a load-bearing decomposition, not a post-hoc narrative.
772	
773	    '
774	- name: Cross-Lingual Orthogonality Analysis
775	  plan_id: plan_005
776	  description: 'Extract verbalized confidence direction via prompted confidence scores,
777	    compute cosine similarity with correctness direction across 20 languages × 2 architectures.
778	    Analyze by resource tier and language family.
779	
780	    '
781	  expected_results:
782	    orthogonality_cosine_mean_overall: 0.052
783	    orthogonality_cosine_range:
784	    - 0.018
785	    - 0.094
786	    orthogonality_cosine_en: 0.034
787	    qwen3_cosine_mean: 0.048
788	    llama4_cosine_mean: 0.057
789	    high_resource_cosine_mean: 0.041
790	    mid_resource_cosine_mean: 0.054
791	    low_resource_cosine_mean: 0.074
792	    cosine_by_lang:
793	      en: 0.034
794	      zh: 0.038
795	      de: 0.036
796	      fr: 0.039
797	      es: 0.041
798	      ja: 0.044
799	      ru: 0.043
800	      pt: 0.04
801	      it: 0.042
802	      ar: 0.051
803	      hi: 0.055
804	      ko: 0.049
805	      vi: 0.058
806	      th: 0.061
807	      bn: 0.056
808	      tr: 0.052
809	      nl: 0.037
810	      sw: 0.078
811	      yo: 0.094
812	      ig: 0.082
813	    all_langs_below_0p1: true
814	    cosine_resource_tier_correlation: -0.68
815	  result_rationale: 'Miao & Ungar (2026) established correctness-confidence orthogonality
816	    (cosine < 0.04) for English on 7-8B models. We extend to 20 languages on larger
817	    models. The orthogonality persists universally (all < 0.1) because it reflects
818	    a fundamental architectural property: verbalized confidence is generated by the
819	    language modeling head from surface-level token probabilities, while correctness
820	    is encoded in intermediate representation geometry. These are structurally decoupled
821	    in transformer architectures. The slight increase in cosine for low-resource languages
822	    (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages
823	    have noisier confidence elicitation — the model''s verbalized confidence in Yoruba
824	    is less well-calibrated and leaks some correctness signal, producing weak correlation.
825	    The resource-tier gradient (ρ=-0.68) suggests that better multilingual training
826	    data produces cleaner separation between correctness and confidence representations.
827	    The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this
828	    is not architecture-specific. Llama 4''s slightly higher cosines may reflect its
829	    less aggressive multilingual pretraining compared to Qwen3.
830	
831	    '
832	  tables:
833	  - name: 'Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture'
834	    columns:
835	    - language
836	    - resource_tier
837	    - qwen3_cosine
838	    - llama4_cosine
839	    - mean_cosine
840	    rows:
841	    - - en
842	      - high
843	      - 0.031
844	      - 0.037
845	      - 0.034
846	    - - zh
847	      - high
848	      - 0.035
849	      - 0.041
850	      - 0.038
851	    - - de
852	      - high
853	      - 0.033
854	      - 0.039
855	      - 0.036
856	    - - fr
857	      - high
858	      - 0.036
859	      - 0.042
860	      - 0.039
861	    - - es
862	      - high
863	      - 0.038
864	      - 0.044
865	      - 0.041
866	    - - ja
867	      - high
868	      - 0.041
869	      - 0.047
870	      - 0.044
871	    - - ru
872	      - high
873	      - 0.04
874	      - 0.046
875	      - 0.043
876	    - - pt
877	      - high
878	      - 0.037
879	      - 0.043
880	      - 0.04
881	    - - it
882	      - high
883	      - 0.039
884	      - 0.045
885	      - 0.042
886	    - - nl
887	      - high
888	      - 0.034
889	      - 0.04
890	      - 0.037
891	    - - ar
892	      - mid
893	      - 0.047
894	      - 0.055
895	      - 0.051
896	    - - hi
897	      - mid
898	      - 0.051
899	      - 0.059
900	      - 0.055
901	    - - ko
902	      - mid
903	      - 0.045
904	      - 0.053
905	      - 0.049
906	    - - vi
907	      - mid
908	      - 0.054
909	      - 0.062
910	      - 0.058
911	    - - th
912	      - mid
913	      - 0.057
914	      - 0.065
915	      - 0.061
916	    - - bn
917	      - mid
918	      - 0.052
919	      - 0.06
920	      - 0.056
921	    - - tr
922	      - mid
923	      - 0.048
924	      - 0.056
925	      - 0.052
926	    - - sw
927	      - low
928	      - 0.073
929	      - 0.083
930	      - 0.078
931	    - - yo
932	      - low
933	      - 0.089
934	      - 0.099
935	      - 0.094
936	    - - ig
937	      - low
938	      - 0.077
939	      - 0.087
940	      - 0.082
941	  - name: 'Table 11: Orthogonality Summary Statistics'
942	    columns:
943	    - statistic
944	    - qwen3_235b
945	    - llama4_scout
946	    - both_models
947	    rows:
948	    - - cosine_mean
949	      - 0.048
950	      - 0.057
951	      - 0.052
952	    - - cosine_std
953	      - 0.015
954	      - 0.017
955	      - 0.016
956	    - - cosine_max
957	      - 0.089
958	      - 0.099
959	      - 0.094
960	    - - cosine_min
961	      - 0.031
962	      - 0.037
963	      - 0.018
964	    - - all_below_0.1
965	      - yes (20/20)
966	      - yes (19/20)
967	      - 39/40
968	    - - resource_tier_corr
969	      - -0.71
970	      - -0.65
971	      - -0.68
972	  figures_description:
973	  - 'Figure 8: Cosine similarity violin plots by resource tier, showing clear gradient
974	    from high (tight around 0.04) to low (spread around 0.08). All below 0.1 threshold.'
975	  - 'Figure 9: Scatter plot of cosine similarity vs language resource level (log wiki
976	    size), colored by architecture. Strong negative trend.'
977	  analysis: 'Orthogonality generalizes comprehensively. The mean cosine of 0.052 across
978	    all 40 language-architecture pairs is well within the "near-orthogonal" regime
979	    (< 0.1). The resource-tier gradient is the novel finding: it suggests that output-based
980	    calibration methods are not just structurally limited but are *more* limited for
981	    well-resourced languages where the orthogonality is strongest. This strengthens
982	    the motivation for probe-based approaches universally and for CaCLR specifically
983	    in multilingual settings. Yoruba''s 0.094 is the only value approaching the 0.1
984	    threshold (on Llama4 it hits 0.099), which is worth noting but does not break
985	    the claim.
986	
987	    '
988	- name: Probe Complexity Comparison
989	  plan_id: plan_006
990	  description: 'Logistic regression vs 2-layer MLP at each probed layer, both models.
991	    Compare English accuracy, cross-lingual transfer degradation, calibration quality.
992	
993	    '
994	  expected_results:
995	    logreg_en_auroc_best: 0.843
996	    mlp_en_auroc_best: 0.856
997	    mlp_en_auroc_gain_pp: 1.3
998	    logreg_zs_transfer_drop_mean_pp: 8.1
999	    mlp_zs_transfer_drop_mean_pp: 12.4
1000	    transfer_degradation_ratio: 1.53
1001	    logreg_ece_mean: 0.054
1002	    mlp_ece_mean: 0.068
1003	    logreg_transfer_advantage_shallow_pp: 2.1
1004	    logreg_transfer_advantage_deep_pp: 6.8
1005	  result_rationale: 'Linear probes transfer better because they learn a single hyperplane
1006	    in activation space — the hyperplane generalizes across languages when the underlying
1007	    geometry is approximately shared (as it is in mid-depth layers). MLPs learn nonlinear
1008	    decision boundaries that fit English-specific feature interactions, gaining ~1.3pp
1009	    EN AUROC but losing ~4.3pp in transfer. The transfer gap widens at deeper layers
1010	    (6.8pp advantage for logreg) because deep layers have more language-specific nonlinear
1011	    structure that MLPs exploit but logreg ignores. This justifies our choice of linear
1012	    probes for the main results and supports the geometric interpretation of the Pareto
1013	    frontier: it''s about linear subspace alignment, not complex feature interactions.
1014	
1015	    '
1016	  tables:
1017	  - name: 'Table 12: Probe Complexity Comparison'
1018	    columns:
1019	    - probe_type
1020	    - en_auroc_best
1021	    - zs_auroc_mean_19
1022	    - zs_drop_pp
1023	    - ece_mean_19
1024	    rows:
1025	    - - logistic_regression
1026	      - 0.843
1027	      - 0.762
1028	      - 8.1
1029	      - 0.054
1030	    - - mlp_2layer
1031	      - 0.856
1032	      - 0.733
1033	      - 12.4
1034	      - 0.068
1035	  figures_description:
1036	  - 'Figure S1 (supplementary): Transfer drop (pp) vs layer depth for both probe types.
1037	    MLP line diverges sharply from logreg at deep layers.'
1038	  analysis: 'Linear probes are the correct choice for cross-lingual transfer: they
1039	    sacrifice 1.3pp EN AUROC but gain 4.3pp average transfer. The depth interaction
1040	    effect is notable — the logreg advantage grows from 2.1pp at shallow layers to
1041	    6.8pp at deep layers, confirming that deep-layer transfer degradation is driven
1042	    by nonlinear, language- specific features. CaCLR + logreg is thus the optimal
1043	    configuration.
1044	
1045	    '
1046	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
1047	  plan_id: plan_007
1048	  description: 'Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX
1049	    (20 languages).
1050	
1051	    '
1052	  expected_results:
1053	    belebele_zs_auroc_mean_19: 0.738
1054	    belebele_caclr_auroc_mean_19: 0.789
1055	    belebele_caclr_vs_zs_pp: 5.1
1056	    belebele_ece_reduction_vs_tempcal_pct: 36.2
1057	    mmlupx_zs_auroc_mean_19: 0.722
1058	    mmlupx_caclr_auroc_mean_19: 0.774
1059	    mmlupx_caclr_vs_zs_pp: 5.2
1060	    mmlupx_ece_reduction_vs_tempcal_pct: 33.8
1061	    caclr_benefit_cross_benchmark_cv: 0.08
1062	  result_rationale: 'Belebele tests reading comprehension (vs GlobalMMLU''s factual
1063	    knowledge), providing domain generalization evidence. Transfer AUROC is slightly
1064	    lower (0.738 vs 0.762) because Belebele''s passage-dependent questions have weaker
1065	    difficulty-shared signal — comprehension difficulty is more language-dependent
1066	    than factual difficulty. CaCLR still provides ~5pp improvement, confirming the
1067	    consistency loss generalizes beyond factual MCQA. MMLU-ProX has harder questions
1068	    that compress the AUROC distribution (lower base rate of correctness), yielding
1069	    slightly lower absolute numbers but comparable CaCLR benefit. The cross-benchmark
1070	    CV of 0.08 for CaCLR improvement confirms the method is robust to evaluation domain.
1071	
1072	    '
1073	  tables:
1074	  - name: 'Table 13: Cross-Benchmark Generalization'
1075	    columns:
1076	    - benchmark
1077	    - zs_auroc_mean_19
1078	    - caclr_auroc_mean_19
1079	    - caclr_gain_pp
1080	    - ece_reduction_pct
1081	    rows:
1082	    - - GlobalMMLU
1083	      - 0.752
1084	      - 0.804
1085	      - 5.2
1086	      - 39.7
1087	    - - Belebele
1088	      - 0.738
1089	      - 0.789
1090	      - 5.1
1091	      - 36.2
1092	    - - MMLU-ProX
1093	      - 0.722
1094	      - 0.774
1095	      - 5.2
1096	      - 33.8
1097	  figures_description:
1098	  - 'Figure S2: CaCLR improvement (pp) by benchmark × language, showing consistent
1099	    gains across domains.'
1100	  analysis: 'CaCLR generalizes cleanly across benchmarks. The improvement magnitude
1101	    is remarkably stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method
1102	    addresses a fundamental representation alignment issue rather than overfitting
1103	    to GlobalMMLU- specific patterns. This is critical for reviewer confidence.
1104	
1105	    '
1106	- name: INT8 Validation Ablation
1107	  plan_id: plan_010
1108	  description: 'Compare INT8 vs FP16 probing results at 5 representative layers for
1109	    Llama 4 Scout on 5% random subset.
1110	
1111	    '
1112	  expected_results:
1113	    int8_fp16_auroc_diff_mean_pp: 0.3
1114	    int8_fp16_auroc_diff_max_pp: 0.7
1115	    int8_fp16_ece_diff_mean_pp: 0.2
1116	    int8_fp16_transfer_drop_diff_pp: 0.4
1117	    int8_fp16_rank_correlation: 0.997
1118	    conclusion: INT8 quantization introduces negligible distortion
1119	  result_rationale: 'INT8 weight-only quantization preserves the 8 most significant
1120	    bits of each weight, introducing per-channel quantization noise of ~0.4% relative
1121	    magnitude. Correctness probing relies on the geometry of activation space (direction
1122	    of correctness signal), not absolute magnitudes. The quantization noise is approximately
1123	    isotropic and thus preserves angular relationships between directions. The 0.3pp
1124	    mean AUROC difference is within random seed variance, and the rank correlation
1125	    of 0.997 between INT8 and FP16 layer rankings confirms that the Pareto frontier
1126	    shape is unaffected. This result is expected given prior work showing that probing
1127	    results are robust to quantization down to INT4 (Gao et al., 2024).
1128	
1129	    '
1130	  tables:
1131	  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)'
1132	    columns:
1133	    - layer_idx
1134	    - fp16_auroc
1135	    - int8_auroc
1136	    - diff_pp
1137	    - fp16_zs_auroc_5lang
1138	    - int8_zs_auroc_5lang
1139	    - transfer_diff_pp
1140	    rows:
1141	    - - 8
1142	      - 0.674
1143	      - 0.672
1144	      - 0.2
1145	      - 0.661
1146	      - 0.658
1147	      - 0.3
1148	    - - 16
1149	      - 0.747
1150	      - 0.745
1151	      - 0.2
1152	      - 0.731
1153	      - 0.728
1154	      - 0.3
1155	    - - 24
1156	      - 0.788
1157	      - 0.786
1158	      - 0.2
1159	      - 0.747
1160	      - 0.744
1161	      - 0.3
1162	    - - 32
1163	      - 0.812
1164	      - 0.81
1165	      - 0.2
1166	      - 0.734
1167	      - 0.731
1168	      - 0.3
1169	    - - 40
1170	      - 0.82
1171	      - 0.817
1172	      - 0.3
1173	      - 0.691
1174	      - 0.687
1175	      - 0.4
1176	  figures_description:
1177	  - 'Figure S3: INT8 vs FP16 AUROC scatter plot at all tested layer-language combinations.
1178	    Points fall tightly along y=x diagonal.'
1179	  analysis: 'INT8 quantization is validated as safe for our experimental setup. The
1180	    maximum observed difference (0.7pp at a single layer-language combination) is
1181	    well within the noise floor of probing experiments. The Pareto frontier ordering
1182	    is perfectly preserved (rank correlation 0.997). This ablation preempts reviewer
1183	    concern #5.
1184	
1185	    '
1186	- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)
1187	  plan_id: plan_008
1188	  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages.
1189	    Provides dense vs MoE architectural contrast.
1190	
1191	    '
1192	  expected_results:
1193	    en_auroc_best_layer: 0.812
1194	    en_best_layer_idx: 45
1195	    zs_transfer_auroc_mean_19lang: 0.734
1196	    zs_best_transfer_layer_idx: 36
1197	    zs_transfer_drop_mean_pp: 7.8
1198	    pareto_depth_transfer_rank_corr: 0.86
1199	    caclr_auroc_mean_19lang: 0.786
1200	    caclr_vs_linproj_auroc_delta_pp: 2.9
1201	    dense_vs_moe_transfer_comparison: comparable within 2pp
1202	    pareto_shape: convex monotonic, consistent with MoE models
1203	  result_rationale: 'Gemma 4 31B Dense has fewer total parameters than the MoE models
1204	    but all are active, yielding comparable per-token compute. As a dense model, its
1205	    representations are more uniformly distributed across layers (no expert routing),
1206	    producing slightly smoother Pareto frontiers. The best-transfer depth (~60%) matches
1207	    both MoE models, confirming this is a universal property of transformer depth,
1208	    not MoE-specific. EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B
1209	    active params < 22B active with MoE routing benefits. CaCLR improvement is slightly
1210	    lower (2.9pp) on the dense model because the absence of expert routing means less
1211	    language-specific feature fragmentation to correct. This is the ideal third data
1212	    point: different architecture family, consistent findings.
1213	
1214	    '
1215	  tables:
1216	  - name: 'Table 14: Three-Architecture Summary'
1217	    columns:
1218	    - model
1219	    - type
1220	    - layers
1221	    - en_auroc_best
1222	    - zs_auroc_mean_19
1223	    - best_transfer_depth_pct
1224	    - pareto_rank_corr
1225	    - caclr_gain_pp
1226	    rows:
1227	    - - Qwen3-235B-A22B
1228	      - MoE
1229	      - 94
1230	      - 0.843
1231	      - 0.762
1232	      - 60
1233	      - 0.88
1234	      - 3.3
1235	    - - Llama 4 Scout
1236	      - MoE
1237	      - 48
1238	      - 0.821
1239	      - 0.741
1240	      - 58
1241	      - 0.82
1242	      - 3.1
1243	    - - Gemma 4 31B Dense
1244	      - Dense
1245	      - 60
1246	      - 0.812
1247	      - 0.734
1248	      - 60
1249	      - 0.86
1250	      - 2.9
1251	  figures_description:
1252	  - 'Figure 10: Three-architecture Pareto frontiers overlaid (normalized depth). Remarkably
1253	    similar shapes despite architectural differences.'
1254	  analysis: 'The three-architecture comparison is the strongest evidence for the universality
1255	    of the depth-transferability tradeoff. The best-transfer depth converges to 58-60%
1256	    across dense and MoE architectures with 48-94 layers, CaCLR provides consistent
1257	    2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases.
1258	    Dense vs MoE makes minimal difference — the phenomenon is a property of transformer
1259	    depth, not routing architecture.
1260	
1261	    '
1262	- name: Extended Language Coverage (Camera-Ready)
1263	  plan_id: plan_009
1264	  description: 'Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele
1265	    full language sets.
1266	
1267	    '
1268	  expected_results:
1269	    total_languages: 52
1270	    new_languages_added: 32
1271	    zs_auroc_above_0p60_count: 48
1272	    zs_auroc_below_0p55_count: 2
1273	    caclr_improvement_positive_count: 49
1274	    mean_zs_auroc_51lang: 0.72
1275	    mean_caclr_auroc_51lang: 0.77
1276	    pareto_frontier_holds_all_langs: true
1277	    new_language_families_covered:
1278	    - Austronesian
1279	    - Dravidian
1280	    - Niger-Congo B
1281	    - Uralic
1282	    - Kartvelian
1283	  result_rationale: 'Expanding to 50+ languages primarily adds mid-resource languages
1284	    (Indonesian, Malay, Finnish, Georgian, Tamil, Telugu, etc.) where the model has
1285	    moderate pretraining exposure. Most new languages fall in the 0.65-0.78 AUROC
1286	    range, consistent with the mid-resource tier from the 20-language set. A handful
1287	    of extremely low-resource languages (e.g., Amharic script languages with minimal
1288	    pretraining data) may fall below 0.55, but these represent edge cases rather than
1289	    systematic failures. CaCLR continues to improve 96% of languages because the consistency
1290	    loss mechanism is language-agnostic — it aligns activation distributions without
1291	    requiring any language-specific knowledge. The Pareto frontier structure is preserved
1292	    across all 52 languages, confirming it''s a depth property, not a language-set
1293	    artifact.
1294	
1295	    '
1296	  tables:
1297	  - name: 'Table 15: Extended Language Coverage Summary by Resource Tier'
1298	    columns:
1299	    - tier
1300	    - n_langs
1301	    - zs_auroc_mean
1302	    - caclr_auroc_mean
1303	    - caclr_gain_pp
1304	    - pct_above_0p60
1305	    rows:
1306	    - - high
1307	      - 12
1308	      - 0.782
1309	      - 0.812
1310	      - 3.0
1311	      - 100
1312	    - - mid
1313	      - 25
1314	      - 0.738
1315	      - 0.784
1316	      - 4.6
1317	      - 100
1318	    - - low
1319	      - 10
1320	      - 0.661
1321	      - 0.712
1322	      - 5.1
1323	      - 90
1324	    - - very_low
1325	      - 4
1326	      - 0.582
1327	      - 0.638
1328	      - 5.6
1329	      - 50
1330	  figures_description:
1331	  - 'Figure 11: World map with per-language CaCLR AUROC, colored by performance tier.
1332	    Demonstrates broad geographic and typological coverage.'
1333	  analysis: 'The extension to 52 languages confirms all findings at broader scale.
1334	    The resource-tier gradient is smooth and predictable — no language family shows
1335	    anomalous behavior. CaCLR''s benefit is inversely correlated with resource level
1336	    (3.0pp for high-resource to 5.6pp for very-low-resource), confirming that the
1337	    consistency loss provides most value where representation misalignment is worst.
1338	    The 48/51 pass rate (>0.60 AUROC) for zero-shot CaCLR transfer with no target-language
1339	    labels is the practical headline for camera-ready: usable cross-lingual calibration
1340	    for the vast majority of languages.'
1341	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3874057a-2d3c-44da-8f83-2499df89cd04",
  "isSidechain": false,
  "promptId": "f5a9dccd-f6bd-4a96-b7c0-602929af4008",
  "type": "user",
  "uuid": "2ca9e4f3-adfa-4c2d-b836-a1fabc4c930f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: 'Original framing stands: \"CaCLR shifts the cross-lingual calibration\n  Pareto frontier.\" All 4 claims form an unbroken causal chain — discovery → analysis\n  → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling\n  with zero target-language labels. Pareto frontier is the organizing principle, CaCLR\n  is the actionable contribution, decomposition explains why it works, orthogonality\n  explains why output-based methods can''t.\n\n  '\nimagined_experiments:\n- name: Full Pareto Frontier — Qwen3-235B-A22B\n  plan_id: plan_001\n  description: 'Extract activations at every 4th layer (24 probed layers out of 94),\n    20 languages, train English correctness probes (logistic regression + 2-layer\n    MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection,\n    few-shot 25/100, CaCLR).\n\n    '\n  expected_results:\n    en_auroc_best_layer: 0.843\n    en_best_layer_idx: 72\n    en_auroc_range:\n    - 0.621\n    - 0.843\n    en_ece_raw_best: 0.162\n    en_ece_tempcal_best: 0.054\n    temp_scaling_T: 4.87\n    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.762\n    zs_best_transfer_layer_idx: 56\n    zs_transfer_drop_from_en_mean_pp: 8.1\n    zs_auroc_by_tier:\n      high_resource_mean: 0.791\n      mid_resource_mean: 0.754\n      low_resource_mean: 0.683\n    zs_auroc_by_lang:\n      en: 0.843\n      zh: 0.802\n      de: 0.796\n      fr: 0.793\n      es: 0.789\n      ja: 0.785\n      ru: 0.782\n      pt: 0.788\n      it: 0.786\n      ar: 0.768\n      hi: 0.761\n      ko: 0.755\n      vi: 0.749\n      th: 0.743\n      bn: 0.738\n      tr: 0.756\n      nl: 0.79\n      sw: 0.695\n      yo: 0.672\n      ig: 0.681\n    mean_shift_improvement_count: 2\n    mean_shift_delta_ece_mean: 1.41\n    linproj_auroc_mean_19lang: 0.724\n    fewshot_25_auroc_mean_19lang: 0.748\n    fewshot_100_auroc_mean_19lang: 0.771\n    pareto_depth_transfer_rank_corr: 0.88\n    pareto_frontier_layers:\n    - 40\n    - 44\n    - 48\n    - 52\n    - 56\n    - 60\n    layers_above_0p5_auroc_count: 22\n  result_rationale: 'Qwen3-235B-A22B is a 94-layer MoE with massive representation\n    capacity. The jump from MVP''s 7B (en AUROC 0.754) to 235B is expected to yield\n    ~9pp AUROC gain, consistent with prior probing literature showing log-linear scaling\n    of linear probe accuracy with model parameters (Burns et al., Marks et al.). The\n    MoE architecture concentrates expert representations, producing cleaner correctness\n    signals in intermediate layers. The Pareto frontier emerges because deeper layers\n    (L72+) specialize for English-dominant pretraining data distribution — the model''s\n    language-specific processing intensifies past ~75% depth, degrading cross-lingual\n    invariance. The best transfer layer (L56, ~60% depth) sits in the \"universal reasoning\"\n    zone before language-specific heads activate. Low-resource languages (sw, yo,\n    ig) still transfer above 0.65 AUROC because GlobalMMLU questions share structural\n    patterns that even underrepresented languages partially align with in middle layers.\n    Mean-shift continues to mostly fail because correctness directions are not simply\n    mean-offset between languages — they require rotation, not translation, which\n    linear projection and CaCLR address.\n\n    '\n  tables:\n  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by\n      Layer'\n    columns:\n    - layer_idx\n    - layer_depth_pct\n    - en_auroc\n    - zs_mean_auroc_19\n    - zs_drop_pp\n    - on_pareto\n    rows:\n    - - 4\n      - 4\n      - 0.621\n      - 0.608\n      - 1.3\n      - false\n    - - 8\n      - 9\n      - 0.648\n      - 0.637\n      - 1.1\n      - false\n    - - 12\n      - 13\n      - 0.689\n      - 0.671\n      - 1.8\n      - false\n    - - 16\n      - 17\n      - 0.712\n      - 0.698\n      - 1.4\n      - false\n    - - 20\n      - 21\n      - 0.738\n      - 0.724\n      - 1.4\n      - false\n    - - 24\n      - 26\n      - 0.756\n      - 0.742\n      - 1.4\n      - false\n    - - 28\n      - 30\n      - 0.771\n      - 0.755\n      - 1.6\n      - false\n    - - 32\n      - 34\n      - 0.784\n      - 0.764\n      - 2.0\n      - false\n    - - 36\n      - 38\n      - 0.795\n      - 0.771\n      - 2.4\n      - false\n    - - 40\n      - 43\n      - 0.803\n      - 0.776\n      - 2.7\n      - true\n    - - 44\n      - 47\n      - 0.81\n      - 0.774\n      - 3.6\n      - true\n    - - 48\n      - 51\n      - 0.816\n      - 0.77\n      - 4.6\n      - true\n    - - 52\n      - 55\n      - 0.822\n      - 0.765\n      - 5.7\n      - true\n    - - 56\n      - 60\n      - 0.827\n      - 0.762\n      - 6.5\n      - true\n    - - 60\n      - 64\n      - 0.831\n      - 0.753\n      - 7.8\n      - true\n    - - 64\n      - 68\n      - 0.835\n      - 0.741\n      - 9.4\n      - false\n    - - 68\n      - 72\n      - 0.839\n      - 0.728\n      - 11.1\n      - false\n    - - 72\n      - 77\n      - 0.843\n      - 0.712\n      - 13.1\n      - false\n    - - 76\n      - 81\n      - 0.841\n      - 0.694\n      - 14.7\n      - false\n    - - 80\n      - 85\n      - 0.838\n      - 0.671\n      - 16.7\n      - false\n    - - 84\n      - 89\n      - 0.832\n      - 0.643\n      - 18.9\n      - false\n    - - 88\n      - 94\n      - 0.819\n      - 0.611\n      - 20.8\n      - false\n    - - 92\n      - 98\n      - 0.791\n      - 0.574\n      - 21.7\n      - false\n    - - 94\n      - 100\n      - 0.762\n      - 0.541\n      - 22.1\n      - false\n  - name: 'Table 2: Transfer Condition Comparison (at best-transfer layer L56)'\n    columns:\n    - condition\n    - auroc_mean_19\n    - ece_mean_19\n    - ece_reduction_vs_tempcal_pct\n    rows:\n    - - zero-shot\n      - 0.762\n      - 0.098\n      - 0\n    - - mean-shift\n      - 0.758\n      - 0.101\n      - -3.1\n    - - linear_projection\n      - 0.781\n      - 0.082\n      - 16.3\n    - - few-shot-25\n      - 0.748\n      - 0.089\n      - 9.2\n    - - few-shot-100\n      - 0.771\n      - 0.079\n      - 19.4\n    - - CaCLR\n      - 0.814\n      - 0.058\n      - 40.8\n  figures_description:\n  - 'Figure 1a: Pareto frontier scatter plot (EN AUROC x-axis vs ZS mean AUROC y-axis),\n    each point a layer, Pareto-optimal layers highlighted in red. Clear convex frontier\n    shape from L40-L60.'\n  - 'Figure 1b: Heatmap of ZS AUROC by language (y-axis, ordered by resource tier)\n    × layer depth (x-axis). Shows warm band in mid-layers, cooling at extremes, with\n    low-resource langs cooling earlier.'\n  analysis: 'The Pareto frontier is crisp and monotonic: 6 layers form the efficient\n    frontier between L40-L60. The rank correlation (Spearman) between layer depth\n    and transfer degradation is ρ=0.88 (p<0.001). The frontier''s shape confirms that\n    the depth- transferability tradeoff is not an artifact of small models — it amplifies\n    at scale. The 16pp gap between best-EN layer (L72) and best-transfer layer (L56)\n    is larger than MVP''s ~3-layer gap, consistent with deeper models having more\n    room for language-specific specialization. All high-resource languages pass AUROC\n    > 0.75 at the best-transfer layer; all low-resource languages exceed 0.65.\n\n    '\n- name: Full Pareto Frontier — Llama 4 Scout\n  plan_id: plan_002\n  description: 'Extract activations at every 4th layer (12 probed layers out of 48),\n    20 languages, 5 transfer conditions. INT8 weight quantization.\n\n    '\n  expected_results:\n    en_auroc_best_layer: 0.821\n    en_best_layer_idx: 36\n    en_auroc_range:\n    - 0.634\n    - 0.821\n    en_ece_raw_best: 0.174\n    en_ece_tempcal_best: 0.061\n    temp_scaling_T: 5.34\n    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.741\n    zs_best_transfer_layer_idx: 28\n    zs_transfer_drop_from_en_mean_pp: 8.0\n    zs_auroc_by_tier:\n      high_resource_mean: 0.771\n      mid_resource_mean: 0.733\n      low_resource_mean: 0.661\n    zs_auroc_by_lang:\n      en: 0.821\n      zh: 0.784\n      de: 0.778\n      fr: 0.775\n      es: 0.771\n      ja: 0.766\n      ru: 0.762\n      pt: 0.77\n      it: 0.768\n      ar: 0.748\n      hi: 0.741\n      ko: 0.735\n      vi: 0.729\n      th: 0.722\n      bn: 0.718\n      tr: 0.737\n      nl: 0.772\n      sw: 0.674\n      yo: 0.641\n      ig: 0.667\n    mean_shift_improvement_count: 1\n    linproj_auroc_mean_19lang: 0.706\n    fewshot_25_auroc_mean_19lang: 0.728\n    fewshot_100_auroc_mean_19lang: 0.752\n    pareto_depth_transfer_rank_corr: 0.82\n    pareto_frontier_layers:\n    - 20\n    - 24\n    - 28\n    - 32\n  result_rationale: 'Llama 4 Scout has 48 layers (fewer than Qwen3''s 94) and a different\n    MoE routing strategy (16 experts, top-2). With roughly 109B total / ~17B active\n    params, its active compute is smaller than Qwen3-235B''s ~22B active. This yields\n    ~2pp lower EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer\n    points (4 vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but\n    the monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout''s best\n    transfer layer sits at ~58% depth (L28), remarkably close to Qwen3''s 60%, suggesting\n    a universal \"mid-depth transfer zone\" across architectures. The rank correlation\n    is slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant.\n    Low-resource languages are slightly weaker because Meta''s multilingual pretraining\n    mix underrepresents African languages compared to Qwen3.\n\n    '\n  tables:\n  - name: 'Table 3: Llama 4 Scout Pareto Frontier'\n    columns:\n    - layer_idx\n    - layer_depth_pct\n    - en_auroc\n    - zs_mean_auroc_19\n    - zs_drop_pp\n    - on_pareto\n    rows:\n    - - 4\n      - 8\n      - 0.634\n      - 0.624\n      - 1.0\n      - false\n    - - 8\n      - 17\n      - 0.672\n      - 0.659\n      - 1.3\n      - false\n    - - 12\n      - 25\n      - 0.714\n      - 0.699\n      - 1.5\n      - false\n    - - 16\n      - 33\n      - 0.745\n      - 0.729\n      - 1.6\n      - false\n    - - 20\n      - 42\n      - 0.768\n      - 0.748\n      - 2.0\n      - true\n    - - 24\n      - 50\n      - 0.786\n      - 0.745\n      - 4.1\n      - true\n    - - 28\n      - 58\n      - 0.798\n      - 0.741\n      - 5.7\n      - true\n    - - 32\n      - 67\n      - 0.81\n      - 0.732\n      - 7.8\n      - true\n    - - 36\n      - 75\n      - 0.821\n      - 0.714\n      - 10.7\n      - false\n    - - 40\n      - 83\n      - 0.818\n      - 0.689\n      - 12.9\n      - false\n    - - 44\n      - 92\n      - 0.804\n      - 0.651\n      - 15.3\n      - false\n    - - 48\n      - 100\n      - 0.771\n      - 0.608\n      - 16.3\n      - false\n  - name: 'Table 4: Cross-Architecture Pareto Frontier Agreement'\n    columns:\n    - metric\n    - qwen3_235b\n    - llama4_scout\n    - agreement\n    rows:\n    - - best_en_layer_depth_pct\n      - 77\n      - 75\n      - within 2pp\n    - - best_transfer_layer_depth_pct\n      - 60\n      - 58\n      - within 2pp\n    - - pareto_zone_depth_range_pct\n      - 43-64\n      - 42-67\n      - overlapping\n    - - depth_transfer_rank_corr\n      - 0.88\n      - 0.82\n      - both >0.75\n    - - frontier_shape\n      - convex monotonic\n      - convex monotonic\n      - consistent\n  figures_description:\n  - 'Figure 2: Overlaid Pareto frontiers for both architectures (normalized depth\n    %). Shows near-identical frontier shapes with Qwen3 shifted up-right (better overall)\n    but same curvature.'\n  analysis: 'Cross-architecture agreement is high: both models show best transfer\n    at ~59% depth, the Pareto frontier occupies the 42-67% depth band, and the rank\n    correlation between depth and transfer degradation exceeds 0.75 in both. The frontier\n    shape is architecture-invariant — it''s the depth-normalized position, not absolute\n    layer count, that determines the tradeoff. This validates Claim 1 at scale.\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train\n    on English labels + unlabeled parallel activations. Compare vs all 5 conditions\n    across full Pareto frontier, both models × 20 languages. Hyperparameter tuning\n    (α, β).\n\n    '\n  expected_results:\n    best_alpha: 0.15\n    best_beta: 0.08\n    qwen3_caclr_auroc_mean_19lang: 0.814\n    qwen3_caclr_ece_mean_19lang: 0.058\n    qwen3_caclr_vs_linproj_auroc_delta_pp: 3.3\n    qwen3_caclr_vs_zeroshot_auroc_delta_pp: 5.2\n    qwen3_caclr_ece_reduction_vs_tempcal_pct: 40.8\n    qwen3_caclr_best_operating_layer: 64\n    llama4_caclr_auroc_mean_19lang: 0.793\n    llama4_caclr_ece_mean_19lang: 0.064\n    llama4_caclr_vs_linproj_auroc_delta_pp: 3.1\n    llama4_caclr_vs_zeroshot_auroc_delta_pp: 5.2\n    llama4_caclr_ece_reduction_vs_tempcal_pct: 38.5\n    llama4_caclr_best_operating_layer: 32\n    caclr_vs_linproj_auroc_delta_pp_mean: 3.2\n    caclr_ece_reduction_vs_tempcal_pct_mean: 39.7\n    caclr_improvement_pass_rate: 0.92\n    caclr_pareto_shift_layers: 2\n    low_resource_caclr_auroc:\n      sw_qwen3: 0.731\n      yo_qwen3: 0.709\n      ig_qwen3: 0.718\n      sw_llama4: 0.712\n      yo_llama4: 0.681\n      ig_llama4: 0.698\n    low_resource_zs_pass_rate: 1.0\n  result_rationale: 'CaCLR''s consistency loss (β·L_consistency) directly penalizes\n    divergence between EN and non-EN probe outputs on parallel/comparable activations,\n    forcing the probe to learn language-invariant features. This is strictly more\n    informative than linear projection (which only aligns means and covariances post-hoc)\n    because it shapes the learned representation during training. The 3.2pp AUROC\n    gain over linear projection reflects the value of end-to-end optimization: linear\n    projection corrects first-order distributional mismatch but not the nonlinear\n    feature interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE)\n    provides calibration-aware training that temperature scaling cannot — it directly\n    optimizes the calibration objective rather than post-hoc rescaling. The 40% ECE\n    reduction over temperature scaling arises because CaCLR addresses the root cause\n    (representation misalignment) rather than the symptom (miscalibrated probabilities).\n    The Pareto frontier shift is the key result: CaCLR allows operating 2 layers deeper\n    than the ZS-optimal point while maintaining equivalent or better transfer — it\n    literally pushes the Pareto frontier outward. Low-resource languages benefit most\n    from L_consistency because their activation distributions are most misaligned\n    from EN; the consistency term provides the strongest gradient signal precisely\n    where the gap is largest.\n\n    '\n  tables:\n  - name: 'Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)'\n    columns:\n    - method\n    - auroc_mean_19\n    - ece_mean_19\n    - requires_target_labels\n    - params_overhead\n    rows:\n    - - zero-shot\n      - 0.752\n      - 0.098\n      - 'no'\n      - '0'\n    - - mean-shift\n      - 0.747\n      - 0.102\n      - 'no'\n      - '0'\n    - - linear_projection\n      - 0.77\n      - 0.082\n      - 'no'\n      - d×d matrix\n    - - few-shot-25\n      - 0.738\n      - 0.089\n      - yes (25)\n      - '0'\n    - - few-shot-100\n      - 0.762\n      - 0.079\n      - yes (100)\n      - '0'\n    - - CaCLR\n      - 0.804\n      - 0.061\n      - 'no'\n      - ~1% probe params\n  - name: 'Table 6: CaCLR Ablation — Loss Component Contributions'\n    columns:\n    - configuration\n    - auroc_mean_19\n    - ece_mean_19\n    - delta_vs_full_auroc_pp\n    rows:\n    - - L_BCE_only (= zero-shot probe)\n      - 0.752\n      - 0.098\n      - -5.2\n    - - L_BCE + L_SB-ECE\n      - 0.768\n      - 0.072\n      - -3.6\n    - - L_BCE + L_consistency\n      - 0.793\n      - 0.078\n      - -1.1\n    - - L_BCE + L_SB-ECE + L_consistency (full CaCLR)\n      - 0.804\n      - 0.061\n      - 0.0\n  - name: 'Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)'\n    columns:\n    - layer_idx\n    - zs_auroc_19\n    - caclr_auroc_19\n    - shift_pp\n    - on_shifted_pareto\n    rows:\n    - - 40\n      - 0.776\n      - 0.798\n      - 2.2\n      - false\n    - - 44\n      - 0.774\n      - 0.8\n      - 2.6\n      - false\n    - - 48\n      - 0.77\n      - 0.803\n      - 3.3\n      - true\n    - - 52\n      - 0.765\n      - 0.806\n      - 4.1\n      - true\n    - - 56\n      - 0.762\n      - 0.81\n      - 4.8\n      - true\n    - - 60\n      - 0.753\n      - 0.814\n      - 6.1\n      - true\n    - - 64\n      - 0.741\n      - 0.814\n      - 7.3\n      - true\n    - - 68\n      - 0.728\n      - 0.808\n      - 8.0\n      - true\n    - - 72\n      - 0.712\n      - 0.796\n      - 8.4\n      - false\n  figures_description:\n  - 'Figure 3: Pareto frontier before/after CaCLR. ZS frontier (blue) vs CaCLR frontier\n    (red), showing outward shift. CaCLR''s optimal operating point is 2 layers deeper\n    with +5pp transfer AUROC.'\n  - 'Figure 4: Per-language AUROC improvement from CaCLR over linear projection, grouped\n    by resource tier. Low-resource languages show largest gains (4-6pp), high-resource\n    2-3pp.'\n  - 'Figure 5: Loss component ablation bar chart — stacked contributions of L_SB-ECE\n    and L_consistency to final AUROC and ECE improvements.'\n  analysis: 'CaCLR decisively outperforms all baselines. The ablation shows both loss\n    terms contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp\n    alone), while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to\n    0.061 when added). The interaction is synergistic — joint optimization yields\n    better results than either term alone. The Pareto shift is the headline result:\n    at the same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer\n    vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation\n    from \"use shallower layers for transfer\" to \"use CaCLR and operate at deeper,\n    better-calibrated layers.\" The improvement pass rate of 92% (35/38 model-lang\n    pairs) demonstrates consistency. The 3 non-improving pairs are high-resource languages\n    (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already excellent and\n    the consistency loss has minimal signal to exploit.\n\n    '\n- name: Difficulty-Controlled Ablation\n  plan_id: plan_004\n  description: 'IRT difficulty probes (Ridge regression), project out difficulty direction,\n    retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers\n    per model.\n\n    '\n  expected_results:\n    difficulty_probe_r2_mean: 0.72\n    difficulty_var_explained_pct_mean: 68.4\n    difficulty_var_explained_pct_range:\n    - 58.2\n    - 79.1\n    residual_en_auroc_drop_pp: 4.2\n    residual_zs_transfer_drop_pp: 1.1\n    capability_specific_var_pct: 31.6\n    capability_specific_transfer_degradation_pct: 87\n    difficulty_component_transfer_degradation_pct: 13\n    decomp_prescriptive_accuracy: 0.81\n    difficulty_var_by_depth:\n      shallow_20pct: 0.74\n      mid_50pct: 0.69\n      deep_80pct: 0.62\n    capability_transfer_drop_by_depth:\n      shallow_20pct: 0.8\n      mid_50pct: 3.4\n      deep_80pct: 9.7\n  result_rationale: 'IRT difficulty is a strong, language-agnostic property — harder\n    questions are harder everywhere. Ridge regression captures this cleanly (R²=0.72)\n    because difficulty is linearly encoded in intermediate representations (Civelli\n    et al. confirmed this). The difficulty component accounts for 68% of explained\n    variance because GlobalMMLU correctness is heavily driven by item difficulty:\n    a model gets easy questions right in all languages and hard questions wrong in\n    all languages. After projecting out difficulty, the residual correctness signal\n    is \"capability-specific\" — it captures language-dependent competence differences.\n    This residual transfers poorly at deep layers (9.7pp drop at 80% depth vs 0.8pp\n    at 20% depth) because deep layers encode language-specific processing that makes\n    capability assessments non-transferable. The difficulty component transfers well\n    at all depths (only 13% of total transfer degradation) because it''s language-invariant\n    by construction. This decomposition is prescriptive: when difficulty explains\n    most of a language''s correctness variance, simple zero-shot transfer suffices;\n    when the capability residual is large, CaCLR is needed. The 81% prescriptive accuracy\n    validates the decomposition as more than descriptive.\n\n    '\n  tables:\n  - name: 'Table 8: Decomposition Results — Difficulty vs Capability Components'\n    columns:\n    - component\n    - var_explained_pct\n    - transfer_auroc_mean\n    - transfer_drop_from_en_pp\n    - share_of_total_transfer_drop_pct\n    rows:\n    - - full_correctness\n      - 100\n      - 0.752\n      - 8.1\n      - 100\n    - - difficulty_shared\n      - 68.4\n      - 0.738\n      - 1.1\n      - 13\n    - - capability_specific\n      - 31.6\n      - 0.614\n      - 14.2\n      - 87\n  - name: 'Table 9: Capability-Specific Transfer Drop by Depth'\n    columns:\n    - depth_band\n    - difficulty_transfer_drop_pp\n    - capability_transfer_drop_pp\n    - ratio\n    rows:\n    - - 0-30%\n      - 0.3\n      - 0.8\n      - 2.7×\n    - - 30-60%\n      - 0.8\n      - 3.4\n      - 4.3×\n    - - 60-90%\n      - 1.6\n      - 9.7\n      - 6.1×\n  figures_description:\n  - 'Figure 6: Stacked area chart showing difficulty vs capability variance across\n    depth. Difficulty dominates at all depths but capability grows at deeper layers.'\n  - 'Figure 7: Transfer degradation decomposed into difficulty (flat, near-zero) and\n    capability (exponentially increasing with depth) components.'\n  analysis: 'The decomposition cleanly separates: difficulty-shared signal is the\n    majority (68%) of correctness variance and transfers near-perfectly across languages\n    and depths. The capability-specific residual (32%) drives nearly all transfer\n    degradation (87%), and this degradation accelerates exponentially with depth.\n    This explains the Pareto frontier mechanistically: deeper layers have stronger\n    capability-specific signals that improve EN calibration but impede transfer. CaCLR\n    works because its consistency loss specifically targets the capability-specific\n    component — forcing alignment of the non-difficulty residual across languages.\n    The prescriptive value (81% accuracy in predicting when CaCLR is needed) confirms\n    this is a load-bearing decomposition, not a post-hoc narrative.\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: 'Extract verbalized confidence direction via prompted confidence scores,\n    compute cosine similarity with correctness direction across 20 languages × 2 architectures.\n    Analyze by resource tier and language family.\n\n    '\n  expected_results:\n    orthogonality_cosine_mean_overall: 0.052\n    orthogonality_cosine_range:\n    - 0.018\n    - 0.094\n    orthogonality_cosine_en: 0.034\n    qwen3_cosine_mean: 0.048\n    llama4_cosine_mean: 0.057\n    high_resource_cosine_mean: 0.041\n    mid_resource_cosine_mean: 0.054\n    low_resource_cosine_mean: 0.074\n    cosine_by_lang:\n      en: 0.034\n      zh: 0.038\n      de: 0.036\n      fr: 0.039\n      es: 0.041\n      ja: 0.044\n      ru: 0.043\n      pt: 0.04\n      it: 0.042\n      ar: 0.051\n      hi: 0.055\n      ko: 0.049\n      vi: 0.058\n      th: 0.061\n      bn: 0.056\n      tr: 0.052\n      nl: 0.037\n      sw: 0.078\n      yo: 0.094\n      ig: 0.082\n    all_langs_below_0p1: true\n    cosine_resource_tier_correlation: -0.68\n  result_rationale: 'Miao & Ungar (2026) established correctness-confidence orthogonality\n    (cosine < 0.04) for English on 7-8B models. We extend to 20 languages on larger\n    models. The orthogonality persists universally (all < 0.1) because it reflects\n    a fundamental architectural property: verbalized confidence is generated by the\n    language modeling head from surface-level token probabilities, while correctness\n    is encoded in intermediate representation geometry. These are structurally decoupled\n    in transformer architectures. The slight increase in cosine for low-resource languages\n    (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages\n    have noisier confidence elicitation — the model''s verbalized confidence in Yoruba\n    is less well-calibrated and leaks some correctness signal, producing weak correlation.\n    The resource-tier gradient (ρ=-0.68) suggests that better multilingual training\n    data produces cleaner separation between correctness and confidence representations.\n    The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this\n    is not architecture-specific. Llama 4''s slightly higher cosines may reflect its\n    less aggressive multilingual pretraining compared to Qwen3.\n\n    '\n  tables:\n  - name: 'Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture'\n    columns:\n    - language\n    - resource_tier\n    - qwen3_cosine\n    - llama4_cosine\n    - mean_cosine\n    rows:\n    - - en\n      - high\n      - 0.031\n      - 0.037\n      - 0.034\n    - - zh\n      - high\n      - 0.035\n      - 0.041\n      - 0.038\n    - - de\n      - high\n      - 0.033\n      - 0.039\n      - 0.036\n    - - fr\n      - high\n      - 0.036\n      - 0.042\n      - 0.039\n    - - es\n      - high\n      - 0.038\n      - 0.044\n      - 0.041\n    - - ja\n      - high\n      - 0.041\n      - 0.047\n      - 0.044\n    - - ru\n      - high\n      - 0.04\n      - 0.046\n      - 0.043\n    - - pt\n      - high\n      - 0.037\n      - 0.043\n      - 0.04\n    - - it\n      - high\n      - 0.039\n      - 0.045\n      - 0.042\n    - - nl\n      - high\n      - 0.034\n      - 0.04\n      - 0.037\n    - - ar\n      - mid\n      - 0.047\n      - 0.055\n      - 0.051\n    - - hi\n      - mid\n      - 0.051\n      - 0.059\n      - 0.055\n    - - ko\n      - mid\n      - 0.045\n      - 0.053\n      - 0.049\n    - - vi\n      - mid\n      - 0.054\n      - 0.062\n      - 0.058\n    - - th\n      - mid\n      - 0.057\n      - 0.065\n      - 0.061\n    - - bn\n      - mid\n      - 0.052\n      - 0.06\n      - 0.056\n    - - tr\n      - mid\n      - 0.048\n      - 0.056\n      - 0.052\n    - - sw\n      - low\n      - 0.073\n      - 0.083\n      - 0.078\n    - - yo\n      - low\n      - 0.089\n      - 0.099\n      - 0.094\n    - - ig\n      - low\n      - 0.077\n      - 0.087\n      - 0.082\n  - name: 'Table 11: Orthogonality Summary Statistics'\n    columns:\n    - statistic\n    - qwen3_235b\n    - llama4_scout\n    - both_models\n    rows:\n    - - cosine_mean\n      - 0.048\n      - 0.057\n      - 0.052\n    - - cosine_std\n      - 0.015\n      - 0.017\n      - 0.016\n    - - cosine_max\n      - 0.089\n      - 0.099\n      - 0.094\n    - - cosine_min\n      - 0.031\n      - 0.037\n      - 0.018\n    - - all_below_0.1\n      - yes (20/20)\n      - yes (19/20)\n      - 39/40\n    - - resource_tier_corr\n      - -0.71\n      - -0.65\n      - -0.68\n  figures_description:\n  - 'Figure 8: Cosine similarity violin plots by resource tier, showing clear gradient\n    from high (tight around 0.04) to low (spread around 0.08). All below 0.1 threshold.'\n  - 'Figure 9: Scatter plot of cosine similarity vs language resource level (log wiki\n    size), colored by architecture. Strong negative trend.'\n  analysis: 'Orthogonality generalizes comprehensively. The mean cosine of 0.052 across\n    all 40 language-architecture pairs is well within the \"near-orthogonal\" regime\n    (< 0.1). The resource-tier gradient is the novel finding: it suggests that output-based\n    calibration methods are not just structurally limited but are *more* limited for\n    well-resourced languages where the orthogonality is strongest. This strengthens\n    the motivation for probe-based approaches universally and for CaCLR specifically\n    in multilingual settings. Yoruba''s 0.094 is the only value approaching the 0.1\n    threshold (on Llama4 it hits 0.099), which is worth noting but does not break\n    the claim.\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Logistic regression vs 2-layer MLP at each probed layer, both models.\n    Compare English accuracy, cross-lingual transfer degradation, calibration quality.\n\n    '\n  expected_results:\n    logreg_en_auroc_best: 0.843\n    mlp_en_auroc_best: 0.856\n    mlp_en_auroc_gain_pp: 1.3\n    logreg_zs_transfer_drop_mean_pp: 8.1\n    mlp_zs_transfer_drop_mean_pp: 12.4\n    transfer_degradation_ratio: 1.53\n    logreg_ece_mean: 0.054\n    mlp_ece_mean: 0.068\n    logreg_transfer_advantage_shallow_pp: 2.1\n    logreg_transfer_advantage_deep_pp: 6.8\n  result_rationale: 'Linear probes transfer better because they learn a single hyperplane\n    in activation space — the hyperplane generalizes across languages when the underlying\n    geometry is approximately shared (as it is in mid-depth layers). MLPs learn nonlinear\n    decision boundaries that fit English-specific feature interactions, gaining ~1.3pp\n    EN AUROC but losing ~4.3pp in transfer. The transfer gap widens at deeper layers\n    (6.8pp advantage for logreg) because deep layers have more language-specific nonlinear\n    structure that MLPs exploit but logreg ignores. This justifies our choice of linear\n    probes for the main results and supports the geometric interpretation of the Pareto\n    frontier: it''s about linear subspace alignment, not complex feature interactions.\n\n    '\n  tables:\n  - name: 'Table 12: Probe Complexity Comparison'\n    columns:\n    - probe_type\n    - en_auroc_best\n    - zs_auroc_mean_19\n    - zs_drop_pp\n    - ece_mean_19\n    rows:\n    - - logistic_regression\n      - 0.843\n      - 0.762\n      - 8.1\n      - 0.054\n    - - mlp_2layer\n      - 0.856\n      - 0.733\n      - 12.4\n      - 0.068\n  figures_description:\n  - 'Figure S1 (supplementary): Transfer drop (pp) vs layer depth for both probe types.\n    MLP line diverges sharply from logreg at deep layers.'\n  analysis: 'Linear probes are the correct choice for cross-lingual transfer: they\n    sacrifice 1.3pp EN AUROC but gain 4.3pp average transfer. The depth interaction\n    effect is notable — the logreg advantage grows from 2.1pp at shallow layers to\n    6.8pp at deep layers, confirming that deep-layer transfer degradation is driven\n    by nonlinear, language- specific features. CaCLR + logreg is thus the optimal\n    configuration.\n\n    '\n- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: 'Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX\n    (20 languages).\n\n    '\n  expected_results:\n    belebele_zs_auroc_mean_19: 0.738\n    belebele_caclr_auroc_mean_19: 0.789\n    belebele_caclr_vs_zs_pp: 5.1\n    belebele_ece_reduction_vs_tempcal_pct: 36.2\n    mmlupx_zs_auroc_mean_19: 0.722\n    mmlupx_caclr_auroc_mean_19: 0.774\n    mmlupx_caclr_vs_zs_pp: 5.2\n    mmlupx_ece_reduction_vs_tempcal_pct: 33.8\n    caclr_benefit_cross_benchmark_cv: 0.08\n  result_rationale: 'Belebele tests reading comprehension (vs GlobalMMLU''s factual\n    knowledge), providing domain generalization evidence. Transfer AUROC is slightly\n    lower (0.738 vs 0.762) because Belebele''s passage-dependent questions have weaker\n    difficulty-shared signal — comprehension difficulty is more language-dependent\n    than factual difficulty. CaCLR still provides ~5pp improvement, confirming the\n    consistency loss generalizes beyond factual MCQA. MMLU-ProX has harder questions\n    that compress the AUROC distribution (lower base rate of correctness), yielding\n    slightly lower absolute numbers but comparable CaCLR benefit. The cross-benchmark\n    CV of 0.08 for CaCLR improvement confirms the method is robust to evaluation domain.\n\n    '\n  tables:\n  - name: 'Table 13: Cross-Benchmark Generalization'\n    columns:\n    - benchmark\n    - zs_auroc_mean_19\n    - caclr_auroc_mean_19\n    - caclr_gain_pp\n    - ece_reduction_pct\n    rows:\n    - - GlobalMMLU\n      - 0.752\n      - 0.804\n      - 5.2\n      - 39.7\n    - - Belebele\n      - 0.738\n      - 0.789\n      - 5.1\n      - 36.2\n    - - MMLU-ProX\n      - 0.722\n      - 0.774\n      - 5.2\n      - 33.8\n  figures_description:\n  - 'Figure S2: CaCLR improvement (pp) by benchmark × language, showing consistent\n    gains across domains.'\n  analysis: 'CaCLR generalizes cleanly across benchmarks. The improvement magnitude\n    is remarkably stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method\n    addresses a fundamental representation alignment issue rather than overfitting\n    to GlobalMMLU- specific patterns. This is critical for reviewer confidence.\n\n    '\n- name: INT8 Validation Ablation\n  plan_id: plan_010\n  description: 'Compare INT8 vs FP16 probing results at 5 representative layers for\n    Llama 4 Scout on 5% random subset.\n\n    '\n  expected_results:\n    int8_fp16_auroc_diff_mean_pp: 0.3\n    int8_fp16_auroc_diff_max_pp: 0.7\n    int8_fp16_ece_diff_mean_pp: 0.2\n    int8_fp16_transfer_drop_diff_pp: 0.4\n    int8_fp16_rank_correlation: 0.997\n    conclusion: INT8 quantization introduces negligible distortion\n  result_rationale: 'INT8 weight-only quantization preserves the 8 most significant\n    bits of each weight, introducing per-channel quantization noise of ~0.4% relative\n    magnitude. Correctness probing relies on the geometry of activation space (direction\n    of correctness signal), not absolute magnitudes. The quantization noise is approximately\n    isotropic and thus preserves angular relationships between directions. The 0.3pp\n    mean AUROC difference is within random seed variance, and the rank correlation\n    of 0.997 between INT8 and FP16 layer rankings confirms that the Pareto frontier\n    shape is unaffected. This result is expected given prior work showing that probing\n    results are robust to quantization down to INT4 (Gao et al., 2024).\n\n    '\n  tables:\n  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)'\n    columns:\n    - layer_idx\n    - fp16_auroc\n    - int8_auroc\n    - diff_pp\n    - fp16_zs_auroc_5lang\n    - int8_zs_auroc_5lang\n    - transfer_diff_pp\n    rows:\n    - - 8\n      - 0.674\n      - 0.672\n      - 0.2\n      - 0.661\n      - 0.658\n      - 0.3\n    - - 16\n      - 0.747\n      - 0.745\n      - 0.2\n      - 0.731\n      - 0.728\n      - 0.3\n    - - 24\n      - 0.788\n      - 0.786\n      - 0.2\n      - 0.747\n      - 0.744\n      - 0.3\n    - - 32\n      - 0.812\n      - 0.81\n      - 0.2\n      - 0.734\n      - 0.731\n      - 0.3\n    - - 40\n      - 0.82\n      - 0.817\n      - 0.3\n      - 0.691\n      - 0.687\n      - 0.4\n  figures_description:\n  - 'Figure S3: INT8 vs FP16 AUROC scatter plot at all tested layer-language combinations.\n    Points fall tightly along y=x diagonal.'\n  analysis: 'INT8 quantization is validated as safe for our experimental setup. The\n    maximum observed difference (0.7pp at a single layer-language combination) is\n    well within the noise floor of probing experiments. The Pareto frontier ordering\n    is perfectly preserved (rank correlation 0.997). This ablation preempts reviewer\n    concern #5.\n\n    '\n- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)\n  plan_id: plan_008\n  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages.\n    Provides dense vs MoE architectural contrast.\n\n    '\n  expected_results:\n    en_auroc_best_layer: 0.812\n    en_best_layer_idx: 45\n    zs_transfer_auroc_mean_19lang: 0.734\n    zs_best_transfer_layer_idx: 36\n    zs_transfer_drop_mean_pp: 7.8\n    pareto_depth_transfer_rank_corr: 0.86\n    caclr_auroc_mean_19lang: 0.786\n    caclr_vs_linproj_auroc_delta_pp: 2.9\n    dense_vs_moe_transfer_comparison: comparable within 2pp\n    pareto_shape: convex monotonic, consistent with MoE models\n  result_rationale: 'Gemma 4 31B Dense has fewer total parameters than the MoE models\n    but all are active, yielding comparable per-token compute. As a dense model, its\n    representations are more uniformly distributed across layers (no expert routing),\n    producing slightly smoother Pareto frontiers. The best-transfer depth (~60%) matches\n    both MoE models, confirming this is a universal property of transformer depth,\n    not MoE-specific. EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B\n    active params < 22B active with MoE routing benefits. CaCLR improvement is slightly\n    lower (2.9pp) on the dense model because the absence of expert routing means less\n    language-specific feature fragmentation to correct. This is the ideal third data\n    point: different architecture family, consistent findings.\n\n    '\n  tables:\n  - name: 'Table 14: Three-Architecture Summary'\n    columns:\n    - model\n    - type\n    - layers\n    - en_auroc_best\n    - zs_auroc_mean_19\n    - best_transfer_depth_pct\n    - pareto_rank_corr\n    - caclr_gain_pp\n    rows:\n    - - Qwen3-235B-A22B\n      - MoE\n      - 94\n      - 0.843\n      - 0.762\n      - 60\n      - 0.88\n      - 3.3\n    - - Llama 4 Scout\n      - MoE\n      - 48\n      - 0.821\n      - 0.741\n      - 58\n      - 0.82\n      - 3.1\n    - - Gemma 4 31B Dense\n      - Dense\n      - 60\n      - 0.812\n      - 0.734\n      - 60\n      - 0.86\n      - 2.9\n  figures_description:\n  - 'Figure 10: Three-architecture Pareto frontiers overlaid (normalized depth). Remarkably\n    similar shapes despite architectural differences.'\n  analysis: 'The three-architecture comparison is the strongest evidence for the universality\n    of the depth-transferability tradeoff. The best-transfer depth converges to 58-60%\n    across dense and MoE architectures with 48-94 layers, CaCLR provides consistent\n    2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases.\n    Dense vs MoE makes minimal difference — the phenomenon is a property of transformer\n    depth, not routing architecture.\n\n    '\n- name: Extended Language Coverage (Camera-Ready)\n  plan_id: plan_009\n  description: 'Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele\n    full language sets.\n\n    '\n  expected_results:\n    total_languages: 52\n    new_languages_added: 32\n    zs_auroc_above_0p60_count: 48\n    zs_auroc_below_0p55_count: 2\n    caclr_improvement_positive_count: 49\n    mean_zs_auroc_51lang: 0.72\n    mean_caclr_auroc_51lang: 0.77\n    pareto_frontier_holds_all_langs: true\n    new_language_families_covered:\n    - Austronesian\n    - Dravidian\n    - Niger-Congo B\n    - Uralic\n    - Kartvelian\n  result_rationale: 'Expanding to 50+ languages primarily adds mid-resource languages\n    (Indonesian, Malay, Finnish, Georgian, Tamil, Telugu, etc.) where the model has\n    moderate pretraining exposure. Most new languages fall in the 0.65-0.78 AUROC\n    range, consistent with the mid-resource tier from the 20-language set. A handful\n    of extremely low-resource languages (e.g., Amharic script languages with minimal\n    pretraining data) may fall below 0.55, but these represent edge cases rather than\n    systematic failures. CaCLR continues to improve 96% of languages because the consistency\n    loss mechanism is language-agnostic — it aligns activation distributions without\n    requiring any language-specific knowledge. The Pareto frontier structure is preserved\n    across all 52 languages, confirming it''s a depth property, not a language-set\n    artifact.\n\n    '\n  tables:\n  - name: 'Table 15: Extended Language Coverage Summary by Resource Tier'\n    columns:\n    - tier\n    - n_langs\n    - zs_auroc_mean\n    - caclr_auroc_mean\n    - caclr_gain_pp\n    - pct_above_0p60\n    rows:\n    - - high\n      - 12\n      - 0.782\n      - 0.812\n      - 3.0\n      - 100\n    - - mid\n      - 25\n      - 0.738\n      - 0.784\n      - 4.6\n      - 100\n    - - low\n      - 10\n      - 0.661\n      - 0.712\n      - 5.1\n      - 90\n    - - very_low\n      - 4\n      - 0.582\n      - 0.638\n      - 5.6\n      - 50\n  figures_description:\n  - 'Figure 11: World map with per-language CaCLR AUROC, colored by performance tier.\n    Demonstrates broad geographic and typological coverage.'\n  analysis: 'The extension to 52 languages confirms all findings at broader scale.\n    The resource-tier gradient is smooth and predictable — no language family shows\n    anomalous behavior. CaCLR''s benefit is inversely correlated with resource level\n    (3.0pp for high-resource to 5.6pp for very-low-resource), confirming that the\n    consistency loss provides most value where representation misalignment is worst.\n    The 48/51 pass rate (>0.60 AUROC) for zero-shot CaCLR transfer with no target-language\n    labels is the practical headline for camera-ready: usable cross-lingual calibration\n    for the vast majority of languages.'\n",
      "numLines": 1341,
      "startLine": 1,
      "totalLines": 1341
    }
  },
  "sourceToolAssistantUUID": "3874057a-2d3c-44da-8f83-2499df89cd04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19 · 2026-05-20T20:31:55.031Z_

````json
{
  "parentUuid": "2ca9e4f3-adfa-4c2d-b836-a1fabc4c930f",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**xling_calib_direction**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"xling_calib_direction\")` 或 `load_project_config(\"xling_calib_direction\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n- **xling-calib-direction-research** — Research patterns from 12 papers on cross-lingual calibration and internal representations in LLMs  →  `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md`\n- **xling-calib-direction-writing** — Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations  →  `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/xling_calib_direction/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "ffd67424-02b1-48c7-8e91-599877fae17d",
  "timestamp": "2026-05-20T20:31:55.031Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decomposition is inconclusive; but cross-lingual probing viability data and the mean-s…",
  "leafUuid": "ffd67424-02b1-48c7-8e91-599877fae17d",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Probe-based calibration fails multilingually—few-shot and mechanistic insights",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Assistant

_source line 22 · 2026-05-20T20:34:58.146Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project context and the existing dream report tiers. I need to read the remaining experiments from the existing worst-tier file to see what's already been generated, and then identify if there are any experiments in the plan that are missing from the worst-tier file.

Let me check the existing worst-tier file continuation (it was cut off at line 1661) and also look at the experiments that need imagined data. Let me also check the remaining experiments: plan_011 (CKA), plan_012 (linear projection sensitivity), plan_013 (control tasks).

Looking at the existing worst-tier imagined experiments, I see it covers:


- plan_001 through plan_010 are already documented, with plan_009 appearing to be incomplete or in progress.

Looking at what's actually been captured, plan_009 is labeled as Extended Language Coverage, but the files seem to cut off before I can verify if plans 011, 012, and 013 exist. I need to check whether those three experiments—CKA cross-lingual representation similarity analysis, linear projection sensitivity analysis, and probing control tasks—are actually part of the planned experiments or if they're beyond the scope of what was originally outlined.

Re-reading the user's request, they want detailed data generated for every planned experiment in the experiment_plan. The planned ones include all thirteen plans plus the three MVP experiments, so I should be generating imagined data for the full set rather than just filling in gaps. I'm reviewing the metric ranges for the worst-tier experiments to ensure consistency across all 13 planned experiments, checking the AUROC values, transfer learning performance, and Pareto efficiency indicators that define this performance tier. Now I'm looking at the performance metrics across these experiments and realizing I need to regenerate the comprehensive YAML with all 13 planned experiments, incorporating the updated context from the latest review round that includes the new experiments and revised hypotheses for the CKA pilot results. plan_013 is new (probing control tasks)

I should generate the complete YAML covering all 13 experiments. The existing worst-tier data for plan_001-plan_010 is largely good, but I should revise where needed given the new context, especially:
- plan_011 needs to reflect the updated hypothesis (threshold model instead of simple negative correlation)
- plan_012 needs to be created fresh
- plan_013 needs to be created fresh

Given the instruction to generate the complete file, I'll produce all 13 experiments. Let me be efficient and thorough.

For the worst tier, the key characteristics:
1. Pareto frontier is noisy, architecture-inconsistent
2. CaCLR fails completely (β is inert)
3. CKA correlation with transfer is weak (r < 0.45)
4. Linear projection helps inconsistently
5. Decomposition is inconclusive
6. Zero-shot transfer is mediocre
7. Control tasks reveal probe capacity artifacts in low-resource
8. Orthogonality holds broadly but with outliers

Now I'm generating the full YAML, keeping existing good content for unchanged experiments and revising the new ones. For plan_011, the CKA pilot showed rho=-0.16 overall with negative correlations per language, but at full scale the correlation weakens (r between 0.15-0.45), the threshold model doesn't replicate cleanly, and CKA declines with depth on both models while the transfer AUROC correlation stays noisy—some languages show strong CKA-transfer links while others are near-zero, suggesting the mechanistic explanation is more complex than initially hypothesized. I'm reconsidering whether to write this directly to a file or output it as a YAML block in the chat—the user's format specification calls for a single YAML block, so I'll generate the complete configuration here. I need to ensure internal consistency across the worst-tier data, incorporating the Dream review changes and filling in the three missing experiments while anchoring everything to the MVP baseline metrics.

Writing YAML configuration... Now I'm looking at the performance metrics for various adaptation methods—CaCLR shows minimal gains whether applied alone or in combination, linear projection improves transfer on about half the languages with a modest boost, and the decomposition analysis suggests difficulty removal has negligible impact. The CKA analysis indicates moderate representational similarity in transfer, orthogonality metrics are quite low, and control tasks show minimal selectivity, which raises questions about whether the models are actually learning language-specific features.

Looking at the zero-shot performance distribution, only a small subset of languages exceed the 0.65 threshold across models, and the low-resource language pairs show consistent but modest improvements. The calibration analysis reveals that temperature scaling provides minimal benefit over the baseline.

Now I need to write out the comprehensive YAML file with all these results—given how large it's going to be, I should output it as a single code block rather than trying to paste it into the chat.

Writing YAML results... I'm verifying that all the per-language metrics align with the worst-tier ranges—checking that Qwen3 has 7 languages above 0.65 AUROC, Llama4 has 5, and both models' low-resource languages (Swahili and Bengali) fall within [0.50, 0.56]. I'm also cross-checking the CaCLR deltas to confirm that the consistency term actually hurts performance slightly while the calibration term provides the modest gains, and that temperature scaling already does most of the ECE reduction work. Now I'll construct the complete YAML with all 13 experiments using these validated numbers. worse transfer. So the rho between layer depth and transfer AUROC should be negative.

Per-language rho for Qwen3:
zh: -0.52 (strong negative, tracks well)
fr: -0.48
de: -0.45
es: -0.41
ja: -0.38
ko: -0.35
ru: -0.31 ← median area
pl: -0.28
ar: -0.24
hi: -0.18
id: -0.12
uk: -0.08
vi: -0.03
th: +0.05 (near zero / slightly positive — non-monotonic)
bn: +0.08
te: +0.12
ta: +0.15
sw: +0.22 (positive! — shallow layers are bad for sw, but deep layers also bad; mid layers are optimal, creating a non-monotonic curve)
yo: +0.28

The pattern is clear when I sort these values: languages with strong negative correlations like Chinese and French show consistent depth-performance relationships, while languages toward the end like Swahili and Yoruba flip to positive correlations, suggesting their transfer performance peaks at intermediate depths rather than following a simple monotonic trend.

Now I'm checking whether the median and sign consistency meet my target ranges. The median lands at -0.18, which fits within my [-0.4, -0.1] target, and about 70% of values are negative, putting sign consistency near the upper bound of my [0.5, 0.7] range. I want to tighten this a bit, so I'm adjusting a few language values downward to push the median closer to -0.31 and bring sign consistency back toward 0.60. Now I'm constructing a distribution of 19 per-language Spearman rho values that targets a median around -0.24, with twelve negative values ranging from -0.55 down to -0.01 and seven positive or near-zero values up to +0.38. The median checks out at -0.12, which falls within the target range, and the sign consistency is solid at 65% when including the assumed negative value. Rather than getting bogged down in precise distributions, I should just use reasonable numbers that tell a clear story for this worst-case tier. Now I'm moving on to structure the full YAML output with fields for name, plan_id, description, expected results, rationale, tables, and figures for each experiment.

Given the scope of what I'm about to generate, I'm considering whether to write this to a file, but the user specifically asked for a YAML block in the output, so I'll produce it directly. I'm also reconsidering the per-language Spearman rho values to ensure they reflect the worst tier's key insight about the Pareto frontier, then I'll write out the complete YAML structure.

Writing YAML output... noisy or architecture-inconsistent." So:
- Qwen3: moderate negative median rho (~-0.25), but lots of scatter
- Llama4: very weak/near-zero median rho (~-0.12), nearly random

For CaCLR, the key insight is "CaCLR fully fails":
- β (consistency weight) is inert or harmful
- Full CaCLR ≈ zero-shot + SB-ECE regularization
- No meaningful improvement over zero-shot

For orthogonality, "holds broadly but with enough outliers":
- Mean cosine ~0.07, but max across all lang-model pairs: 0.17
- yo on Llama4 reaches 0.17, weakening universality claim

The CKA pilot gave me important context—weak overall correlation (rho = -0.16) but strong signals in individual languages like Hindi and Swahili (both rho < -0.79), suggesting a threshold model rather than linear relationship. At full scale, the threshold pattern partially holds but gets drowned in noise, with Pearson r around 0.32 and highly inconsistent results across architectures. Now I need to write out the YAML with detailed rationales for each experiment, and I should make sure the mean-shift rank-invariance proof stays prominent since that's a solid novel contribution—the ΔAUROC results should consistently show zero across conditions.

I'm also clarifying the language count: the worst-tier data refers to "19-language" transfer (non-English), so the full setup is 20 languages total including English as the source. But the metric "zs_transfer_auroc_median_20lang" is ambiguous—it could mean 20 target languages or 20 total. I'll need to check the experiment plan wording carefully to stay consistent. I'm going back and forth on whether the metric refers to 20 total languages or 20 non-English targets. The existing worst-tier file consistently uses 19 non-EN languages, which would mean 20 total including English. But the key metric name says "20lang," which creates ambiguity. Rather than get stuck on this inconsistency, I'll stick with the established convention of 19 non-EN target languages for a total of 20, and I'll note this assumption in the output.

Now I need to actually start generating the YAML. I'm going to keep the same structure as the existing worst-tier file but update the numbers for consistency and add the three new plans. The existing file is already 1661 lines, so I'll try to be more concise with the older experiments while being thorough with the new additions, especially plan_011 which incorporates the revised CKA hypothesis from the pilot.

Writing YAML output... Now I'm ready to write out the full experiment specifications, making sure to include the per-language statistical breakdowns with bootstrap confidence intervals and paired permutation tests where they apply, along with effect sizes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffd67424-02b1-48c7-8e91-599877fae17d",
  "isSidechain": false,
  "requestId": "req_011CbETS2fyZBzz9EpV45HHP",
  "type": "assistant",
  "uuid": "a984c183-0484-4451-8cb8-418b7b73e174",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QND7jTCMKfGEbPXkduL1Te",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 47171,
      "cache_read_input_tokens": 27200,
      "output_tokens": 10303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 47171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10303,
          "cache_read_input_tokens": 27200,
          "cache_creation_input_tokens": 47171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 47171
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

_source line 23 · 2026-05-20T20:34:58.148Z_

Let me check the previous worst-tier imagined experiments for completeness, especially for the new experiments added in Dream review round 3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a984c183-0484-4451-8cb8-418b7b73e174",
  "isSidechain": false,
  "requestId": "req_011CbETS2fyZBzz9EpV45HHP",
  "type": "assistant",
  "uuid": "99d469e8-f1f2-4966-9ad6-a2e62f91d6d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QND7jTCMKfGEbPXkduL1Te",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 47171,
      "cache_read_input_tokens": 27200,
      "output_tokens": 10303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 47171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10303,
          "cache_read_input_tokens": 27200,
          "cache_creation_input_tokens": 47171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 47171
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

_source line 24 · 2026-05-20T20:34:58.933Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QnLbsHemUuMwWxkZM7wnEd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
  "offset": 1640
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99d469e8-f1f2-4966-9ad6-a2e62f91d6d3",
  "isSidechain": false,
  "requestId": "req_011CbETS2fyZBzz9EpV45HHP",
  "type": "assistant",
  "uuid": "f5103d6a-228d-43ab-9b04-3105b525eb91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QND7jTCMKfGEbPXkduL1Te",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 47171,
      "cache_read_input_tokens": 27200,
      "output_tokens": 10303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 47171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10303,
          "cache_read_input_tokens": 27200,
          "cache_creation_input_tokens": 47171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 47171
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

_source line 25 · 2026-05-20T20:34:59.294Z_

<details><summary>↩ Tool result · `toolu_01DKH68sbK2MqkaqhUF6q8g7`</summary>

```text
1	tier: median
2	narrative_guidance: 'Rebalance toward discovery + analysis. Claim 1 (Pareto frontier)
3	  becomes the headline contribution — first systematic characterization of depth-transferability
4	  tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as
5	  ''partial but prescriptive'': difficulty component is clearly transferable, capability
6	  residual is noisy but the decomposition still predicts when simple baselines suffice
7	  vs when CaCLR helps. Claim 3 softens: CaCLR is presented as ''matching or exceeding
8	  the best simple baseline (linear projection) while requiring no target-language
9	  data at all'' — emphasize the zero-label setting rather than raw metric superiority.
10	  Add ablation showing where CaCLR''s consistency term specifically helps (mid-resource
11	  languages). Claim 4 presented with resource-tier analysis showing orthogonality
12	  is robust for well-represented languages but noisier for low-resource. Headline:
13	  ''Cross-lingual calibration probes reveal architecture-dependent Pareto frontier;
14	  CaCLR matches supervised transfer without target labels.''
15	
16	  '
17	imagined_experiments:
18	- name: Full Pareto Frontier — Qwen3-235B-A22B
19	  plan_id: plan_001
20	  description: '94-layer MoE model, INT8 quantization. 24 probed layers (every 4th:
21	    L0–L92). 20 languages (7 high / 8 mid / 5 low resource). English logistic-regression
22	    correctness probes trained per layer, evaluated on 5 transfer conditions (zero-shot,
23	    mean-shift, linear projection, few-shot 25/100, CaCLR placeholder). Core Pareto
24	    frontier data for Claim 1.
25	
26	    '
27	  expected_results:
28	    en_auroc_best: 0.812
29	    en_best_layer: L76
30	    en_auroc_range:
31	    - 0.531
32	    - 0.812
33	    en_ece_raw_at_best: 0.168
34	    en_ece_tempcal_at_best: 0.057
35	    temp_scaling_T: 5.83
36	    zs_transfer_auroc_mean_19lang_at_best_en: 0.644
37	    zs_transfer_drop_at_best_en_pp: 16.8
38	    best_transfer_layer: L40
39	    zs_transfer_auroc_mean_at_best_transfer: 0.696
40	    en_auroc_at_best_transfer: 0.776
41	    pareto_depth_transfer_rank_corr: 0.71
42	    low_resource_zs_pass_rate: 0.6
43	    mean_shift_improvement_rate: 0.05
44	    linproj_auroc_mean_at_best_transfer: 0.724
45	    fewshot25_auroc_mean_at_best_transfer: 0.711
46	    fewshot100_auroc_mean_at_best_transfer: 0.743
47	  result_rationale: 'Qwen3-235B-A22B 的 94 层深度提供了充分的层级分辨率来观测 Pareto tradeoff。 深层（L76）英语
48	    AUROC 达 0.812，因为更深层积累了更多 task-specific correctness 信号； 但这些深层 representation 也更
49	    language-specific（MoE routing 在深层更分化）， 导致 zero-shot 迁移退化至 0.644（drop 16.8pp）。最佳迁移层
50	    L40 处于模型 ~42% 深度，此处 representation 仍保留足够的 language-agnostic 结构。跨语言层序一致性 Spearman
51	    ρ=0.71 表明各语言对最优迁移深度的偏好高度一致，Pareto 结构是 robust 的。 Mean-shift 继承 MVP 的失败模式（correctness
52	    ≠ knowledge-boundary），仅 1/19 语言微弱改善。Linear projection 利用无标注目标语激活做线性对齐，在 L40 处比
53	    zero-shot 高 2.8pp，确立为 CaCLR 需要超越的 strong baseline。 低资源语言（sw/te/my 通过，am/yo 失败）符合预期：GlobalMMLU
54	    低资源子集样本量小且 翻译质量不稳定，但 3/5 通过证明 correctness direction 跨语言性在大模型上比 7B 更强。
55	
56	    '
57	  tables:
58	  - title: English AUROC by Layer (Logistic Regression)
59	    columns:
60	    - layer
61	    - depth_pct
62	    - en_auroc
63	    - en_ece_raw
64	    data:
65	    - layer: L0
66	      depth_pct: 0
67	      en_auroc: 0.531
68	      en_ece_raw: 0.341
69	    - layer: L4
70	      depth_pct: 4
71	      en_auroc: 0.557
72	      en_ece_raw: 0.328
73	    - layer: L8
74	      depth_pct: 9
75	      en_auroc: 0.589
76	      en_ece_raw: 0.312
77	    - layer: L12
78	      depth_pct: 13
79	      en_auroc: 0.621
80	      en_ece_raw: 0.293
81	    - layer: L16
82	      depth_pct: 17
83	      en_auroc: 0.653
84	      en_ece_raw: 0.274
85	    - layer: L20
86	      depth_pct: 21
87	      en_auroc: 0.684
88	      en_ece_raw: 0.255
89	    - layer: L24
90	      depth_pct: 26
91	      en_auroc: 0.711
92	      en_ece_raw: 0.237
93	    - layer: L28
94	      depth_pct: 30
95	      en_auroc: 0.735
96	      en_ece_raw: 0.221
97	    - layer: L32
98	      depth_pct: 34
99	      en_auroc: 0.752
100	      en_ece_raw: 0.21
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaaa3f8d-db89-4dcf-aa13-ff41412ee1bc",
  "isSidechain": false,
  "promptId": "f5a9dccd-f6bd-4a96-b7c0-602929af4008",
  "type": "user",
  "uuid": "534dae54-8d19-4147-bf42-d66e084373c7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml",
      "content": "tier: median\nnarrative_guidance: 'Rebalance toward discovery + analysis. Claim 1 (Pareto frontier)\n  becomes the headline contribution — first systematic characterization of depth-transferability\n  tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as\n  ''partial but prescriptive'': difficulty component is clearly transferable, capability\n  residual is noisy but the decomposition still predicts when simple baselines suffice\n  vs when CaCLR helps. Claim 3 softens: CaCLR is presented as ''matching or exceeding\n  the best simple baseline (linear projection) while requiring no target-language\n  data at all'' — emphasize the zero-label setting rather than raw metric superiority.\n  Add ablation showing where CaCLR''s consistency term specifically helps (mid-resource\n  languages). Claim 4 presented with resource-tier analysis showing orthogonality\n  is robust for well-represented languages but noisier for low-resource. Headline:\n  ''Cross-lingual calibration probes reveal architecture-dependent Pareto frontier;\n  CaCLR matches supervised transfer without target labels.''\n\n  '\nimagined_experiments:\n- name: Full Pareto Frontier — Qwen3-235B-A22B\n  plan_id: plan_001\n  description: '94-layer MoE model, INT8 quantization. 24 probed layers (every 4th:\n    L0–L92). 20 languages (7 high / 8 mid / 5 low resource). English logistic-regression\n    correctness probes trained per layer, evaluated on 5 transfer conditions (zero-shot,\n    mean-shift, linear projection, few-shot 25/100, CaCLR placeholder). Core Pareto\n    frontier data for Claim 1.\n\n    '\n  expected_results:\n    en_auroc_best: 0.812\n    en_best_layer: L76\n    en_auroc_range:\n    - 0.531\n    - 0.812\n    en_ece_raw_at_best: 0.168\n    en_ece_tempcal_at_best: 0.057\n    temp_scaling_T: 5.83\n    zs_transfer_auroc_mean_19lang_at_best_en: 0.644\n    zs_transfer_drop_at_best_en_pp: 16.8\n    best_transfer_layer: L40\n    zs_transfer_auroc_mean_at_best_transfer: 0.696\n    en_auroc_at_best_transfer: 0.776\n    pareto_depth_transfer_rank_corr: 0.71\n    low_resource_zs_pass_rate: 0.6\n    mean_shift_improvement_rate: 0.05\n    linproj_auroc_mean_at_best_transfer: 0.724\n    fewshot25_auroc_mean_at_best_transfer: 0.711\n    fewshot100_auroc_mean_at_best_transfer: 0.743\n  result_rationale: 'Qwen3-235B-A22B 的 94 层深度提供了充分的层级分辨率来观测 Pareto tradeoff。 深层（L76）英语\n    AUROC 达 0.812，因为更深层积累了更多 task-specific correctness 信号； 但这些深层 representation 也更\n    language-specific（MoE routing 在深层更分化）， 导致 zero-shot 迁移退化至 0.644（drop 16.8pp）。最佳迁移层\n    L40 处于模型 ~42% 深度，此处 representation 仍保留足够的 language-agnostic 结构。跨语言层序一致性 Spearman\n    ρ=0.71 表明各语言对最优迁移深度的偏好高度一致，Pareto 结构是 robust 的。 Mean-shift 继承 MVP 的失败模式（correctness\n    ≠ knowledge-boundary），仅 1/19 语言微弱改善。Linear projection 利用无标注目标语激活做线性对齐，在 L40 处比\n    zero-shot 高 2.8pp，确立为 CaCLR 需要超越的 strong baseline。 低资源语言（sw/te/my 通过，am/yo 失败）符合预期：GlobalMMLU\n    低资源子集样本量小且 翻译质量不稳定，但 3/5 通过证明 correctness direction 跨语言性在大模型上比 7B 更强。\n\n    '\n  tables:\n  - title: English AUROC by Layer (Logistic Regression)\n    columns:\n    - layer\n    - depth_pct\n    - en_auroc\n    - en_ece_raw\n    data:\n    - layer: L0\n      depth_pct: 0\n      en_auroc: 0.531\n      en_ece_raw: 0.341\n    - layer: L4\n      depth_pct: 4\n      en_auroc: 0.557\n      en_ece_raw: 0.328\n    - layer: L8\n      depth_pct: 9\n      en_auroc: 0.589\n      en_ece_raw: 0.312\n    - layer: L12\n      depth_pct: 13\n      en_auroc: 0.621\n      en_ece_raw: 0.293\n    - layer: L16\n      depth_pct: 17\n      en_auroc: 0.653\n      en_ece_raw: 0.274\n    - layer: L20\n      depth_pct: 21\n      en_auroc: 0.684\n      en_ece_raw: 0.255\n    - layer: L24\n      depth_pct: 26\n      en_auroc: 0.711\n      en_ece_raw: 0.237\n    - layer: L28\n      depth_pct: 30\n      en_auroc: 0.735\n      en_ece_raw: 0.221\n    - layer: L32\n      depth_pct: 34\n      en_auroc: 0.752\n      en_ece_raw: 0.21",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 1673
    }
  },
  "sourceToolAssistantUUID": "aaaa3f8d-db89-4dcf-aa13-ff41412ee1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T20:34:58.944Z_

<details><summary>↩ Tool result · `toolu_01QnLbsHemUuMwWxkZM7wnEd`</summary>

```text
1640	      - 0.28
1641	    - - low
1642	      - 14
1643	      - 0.558
1644	      - 0.031
1645	      - 0.07
1646	    - - very_low
1647	      - 10
1648	      - 0.521
1649	      - 0.022
1650	      - 0.0
1651	  figures_description:
1652	  - 'Figure 7 (camera-ready): World map heatmap with 52 languages colored by zero-shot
1653	    transfer AUROC. Europe and East Asia are green/yellow (adequate transfer). South/Southeast
1654	    Asia is orange. Sub-Saharan Africa and Central Asia are red (near-chance). Visual
1655	    reinforces the ''language barrier'' framing.'
1656	  analysis: 'Extended coverage is the nail in the coffin for universal probe-based
1657	    calibration. With 52 languages, the majority fail to transfer. The resource-tier
1658	    gradient is steep and monotonic. This is the strongest evidence for the diagnostic
1659	    paper''s conclusion: "this research line does not generalize beyond a small set
1660	    of high-resource languages without fundamental methodological advances."'
1661	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5103d6a-228d-43ab-9b04-3105b525eb91",
  "isSidechain": false,
  "promptId": "f5a9dccd-f6bd-4a96-b7c0-602929af4008",
  "type": "user",
  "uuid": "3a3cf311-1918-4414-bd3f-de4a2c415bd1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
      "content": "      - 0.28\n    - - low\n      - 14\n      - 0.558\n      - 0.031\n      - 0.07\n    - - very_low\n      - 10\n      - 0.521\n      - 0.022\n      - 0.0\n  figures_description:\n  - 'Figure 7 (camera-ready): World map heatmap with 52 languages colored by zero-shot\n    transfer AUROC. Europe and East Asia are green/yellow (adequate transfer). South/Southeast\n    Asia is orange. Sub-Saharan Africa and Central Asia are red (near-chance). Visual\n    reinforces the ''language barrier'' framing.'\n  analysis: 'Extended coverage is the nail in the coffin for universal probe-based\n    calibration. With 52 languages, the majority fail to transfer. The resource-tier\n    gradient is steep and monotonic. This is the strongest evidence for the diagnostic\n    paper''s conclusion: \"this research line does not generalize beyond a small set\n    of high-resource languages without fundamental methodological advances.\"'\n",
      "numLines": 22,
      "startLine": 1640,
      "totalLines": 1661
    }
  },
  "sourceToolAssistantUUID": "f5103d6a-228d-43ab-9b04-3105b525eb91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T20:34:59.284Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DKH68sbK2MqkaqhUF6q8g7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a3cf311-1918-4414-bd3f-de4a2c415bd1",
  "isSidechain": false,
  "requestId": "req_011CbETS2fyZBzz9EpV45HHP",
  "type": "assistant",
  "uuid": "aaaa3f8d-db89-4dcf-aa13-ff41412ee1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QND7jTCMKfGEbPXkduL1Te",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 47171,
      "cache_read_input_tokens": 27200,
      "output_tokens": 10303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 47171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10303,
          "cache_read_input_tokens": 27200,
          "cache_creation_input_tokens": 47171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 47171
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decomposition is inconclusive; but cross-lingual probing viability data and the mean-s…",
  "leafUuid": "534dae54-8d19-4147-bf42-d66e084373c7",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Probe-based calibration fails multilingually—few-shot and mechanistic insights",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Assistant

_source line 30 · 2026-05-20T20:35:06.790Z_

<details><summary>Logged reasoning block</summary>

```text
OK, I've confirmed the existing worst-tier file ends at line 1661 with plan_009, missing plan_011, plan_012, and plan_013. The median tier uses a different table format (title/columns/data instead of name/columns/rows). Let me use the same format as the existing worst-tier file for consistency.

Now let me write the complete YAML. I'll structure it with all 13 planned experiments.

Given the massive size, I'll write it directly. Let me be thorough and ensure internal consistency.

Let me also slightly revise the existing experiments where the Dream round 3 changes affect them (mainly plan_011's description changed to reflect CKA pilot results).


Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "534dae54-8d19-4147-bf42-d66e084373c7",
  "isSidechain": false,
  "requestId": "req_011CbETfcs99TuH98U4Sb9FX",
  "type": "assistant",
  "uuid": "ad5760bc-0b61-4f48-94b9-432eca6bd3ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMcpPDzy7mv4XQXUxiqjkw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12473,
      "cache_read_input_tokens": 74371,
      "output_tokens": 24167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 24167,
          "cache_read_input_tokens": 74371,
          "cache_creation_input_tokens": 12473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12473
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

_source line 31 · 2026-05-20T20:41:56.200Z_

Existing worst-tier file covers plan_001 through plan_009 + plan_010 but is missing plan_011 (CKA), plan_012 (linear projection sensitivity), and plan_013 (control tasks). I'll generate the complete worst-tier imagined experiments for all 13 planned experiments, incorporating the CKA pilot revision and Dream round 3 updates.

```yaml
tier: worst
narrative_guidance: >
  Reframe as field-level empirical survey: "Does probe-based calibration work beyond English?
  A systematic investigation across 2 architectures and 20 languages." Three surviving novel
  contributions: (1) mean-shift rank-invariance theorem with proof — explains why mean-shift
  fails (ΔAUROC ≡ 0 under StandardScaler + logistic regression), distinguishing from Xiao et al.;
  (2) resource-tier taxonomy of cross-lingual probe transferability — first quantification across
  20 languages showing high-resource transfers, mid is marginal, low fails;
  (3) practical recommendation — few-shot (25–100 labels) is the only viable path, closing the
  zero-label dream for low-resource languages. CaCLR is relegated to one paragraph as
  attempted-and-failed (consistency loss inert, SB-ECE alone insufficient). Decomposition is
  reported as inconclusive (difficulty removal neither helps nor hurts transfer systematically).
  Pareto frontier is real on Qwen3 but flat/non-monotonic on Llama 4 Scout — architecture-dependent,
  not universal. CKA provides suggestive but not convincing mechanistic explanation (r < 0.45).
  Orthogonality persists broadly but with outliers (cosine up to 0.17 for low-resource),
  weakening the universality claim. Control tasks reveal capacity artifacts in low-resource
  settings (selectivity < 8pp). Paper becomes a "sobering empirical reality check" for the
  probe-based calibration line. Target: borderline at EACL, requires very clean writing and
  strong related-work positioning.

imagined_experiments:

  # ============================================================
  # plan_001 — Full Pareto Frontier: Qwen3-235B-A22B
  # ============================================================
  - name: "Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT8)"
    plan_id: plan_001
    description: >
      Extract activations at 24 probed layers (every 4th of 94), 20 languages on GlobalMMLU.
      Train English logistic regression + 2-layer MLP correctness probes. Evaluate 5 transfer
      conditions: zero-shot, mean-shift, linear projection, few-shot (25/100), CaCLR.
      Report per-language Spearman ρ (depth vs transfer AUROC) alongside global ρ.
      Bootstrap CIs (1000 resamples) on all AUROC/ECE; paired permutation tests for method
      comparisons; Cohen's d for effect sizes.
    expected_results:
      en_auroc_best_layer: 0.776
      en_best_layer_idx: 72
      en_auroc_range: [0.612, 0.776]
      en_ece_raw_best: 0.174
      en_ece_tempcal_best: 0.069
      temp_scaling_T: 5.91
      zs_transfer_auroc_mean_19lang: 0.618
      zs_transfer_auroc_median_19lang: 0.618
      zs_transfer_auroc_std_19lang: 0.046
      zs_transfer_drop_mean_pp: 15.8
      zs_langs_above_0p65: 7
      zs_pass_langs: [zh, fr, de, es, ja, ko, ru]
      zs_fail_langs: [ar, hi, vi, id, th, pl, uk, bn, te, ta, sw, yo]
      mean_shift_delta_auroc_all_langs: 0.000
      mean_shift_delta_ece_unreliable: true
      mean_shift_delta_ece_range_pp: [-1.2, 6.8]
      linproj_auroc_mean_19lang: 0.636
      linproj_improves_over_zs_count: 11
      linproj_delta_auroc_vs_zs_mean_pp: 1.8
      fewshot25_auroc_mean_19lang: 0.644
      fewshot25_improves_over_zs_count: 14
      fewshot100_auroc_mean_19lang: 0.662
      fewshot100_improves_over_zs_count: 16
      pareto_global_spearman_rho: -0.38
      pareto_per_lang_rho_median: -0.25
      pareto_per_lang_rho_range: [-0.55, 0.31]
      pareto_rho_sign_consistency: 0.63
      pareto_frontier_n_nondominated: 5
      pareto_frontier_monotonic: false
      bootstrap_ci_width_auroc_median_pp: 2.8
      per_lang_zs_auroc:
        zh: 0.668
        fr: 0.672
        de: 0.671
        es: 0.661
        ja: 0.658
        ko: 0.656
        ru: 0.652
        ar: 0.625
        hi: 0.618
        vi: 0.607
        id: 0.621
        th: 0.594
        pl: 0.628
        uk: 0.614
        bn: 0.553
        te: 0.571
        ta: 0.568
        sw: 0.537
        yo: 0.512
      per_lang_best_zs_layer:
        zh: 52
        fr: 52
        de: 52
        es: 48
        ja: 48
        ko: 48
        ru: 44
        ar: 40
        hi: 40
        vi: 40
        id: 40
        th: 36
        pl: 44
        uk: 40
        bn: 28
        te: 28
        ta: 28
        sw: 28
        yo: 24
      per_lang_spearman_rho:
        zh: -0.55
        fr: -0.51
        de: -0.48
        es: -0.42
        ja: -0.37
        ko: -0.33
        ru: -0.25
        ar: -0.18
        hi: -0.11
        pl: -0.14
        uk: -0.06
        id: -0.02
        vi: 0.04
        th: 0.09
        bn: 0.14
        te: 0.18
        ta: 0.22
        sw: 0.27
        yo: 0.31
      transfer_by_resource_tier:
        high_mean: 0.663
        high_langs: [zh, fr, de, es, ja, ko, ru]
        mid_mean: 0.615
        mid_langs: [ar, hi, vi, id, th, pl, uk]
        low_mean: 0.548
        low_langs: [bn, te, ta, sw, yo]
    result_rationale: >
      Qwen3-235B improves only modestly over the MVP's Qwen2.5-7B (EN AUROC 0.776 vs 0.754)
      because gains from scale are sublinear for linear probing — the larger model has more
      complex, distributed representations where correctness is encoded across many dimensions
      rather than in a single cleanly accessible direction. The Pareto frontier exists but is
      noisy: global Spearman ρ = -0.38 means depth explains ~15% of transfer variance. Per-language
      rho varies dramatically — high-resource languages that share subspace structure with English
      (zh, fr, de) show clear negative correlation (deeper = worse transfer), while low-resource
      languages (sw, yo, ta) show positive or near-zero rho because their best transfer happens at
      shallow layers where representations are still language-agnostic, and the signal is too weak
      at any depth for a clear depth gradient to emerge. MoE expert routing introduces non-monotonic
      noise at mid-depth layers (36-56) where routing patterns shift. Mean-shift ΔAUROC is exactly
      0.000 across all languages and layers, confirming the rank-invariance proof: under
      StandardScaler + logistic regression, mean subtraction adds a constant to all logits,
      preserving ranks. ECE changes from mean-shift are unreliable because they depend on
      threshold-sensitive binning of shifted probabilities. Linear projection helps 11/19 languages
      by learning the affine transformation between language subspaces, but fails for low-resource
      languages where insufficient parallel data quality prevents reliable transformation
      estimation. Few-shot-100 is the best method but requires per-language labels, partially
      negating the zero-label promise.
    tables:
      - name: "Table 1: Qwen3-235B English Probe Performance by Layer (Selected Layers)"
        columns: [layer, depth_pct, logreg_auroc, mlp_auroc, ece_raw, ece_tempcal]
        rows:
          - [4,   4,  0.612, 0.618, 0.298, 0.192]
          - [16,  17, 0.653, 0.661, 0.251, 0.148]
          - [28,  30, 0.694, 0.708, 0.224, 0.121]
          - [40,  43, 0.721, 0.737, 0.203, 0.098]
          - [52,  55, 0.742, 0.755, 0.191, 0.082]
          - [60,  64, 0.758, 0.769, 0.183, 0.075]
          - [72,  77, 0.776, 0.783, 0.174, 0.069]
          - [80,  85, 0.771, 0.779, 0.177, 0.072]
          - [88,  94, 0.753, 0.762, 0.186, 0.079]
          - [92,  98, 0.728, 0.739, 0.198, 0.091]
      - name: "Table 2: Qwen3-235B Zero-Shot Transfer AUROC by Language (Best Transfer Layer)"
        columns: [language, family, resource_tier, best_zs_layer, best_zs_auroc, en_auroc_same_layer, drop_pp, spearman_rho, rho_p_value]
        rows:
          - [zh, sino_tibetan, high, 52, 0.668, 0.742, 7.4, -0.55, 0.006]
          - [fr, romance, high, 52, 0.672, 0.742, 7.0, -0.51, 0.011]
          - [de, germanic, high, 52, 0.671, 0.742, 7.1, -0.48, 0.017]
          - [es, romance, high, 48, 0.661, 0.735, 7.4, -0.42, 0.041]
          - [ja, japonic, high, 48, 0.658, 0.735, 7.7, -0.37, 0.075]
          - [ko, koreanic, high, 48, 0.656, 0.735, 7.9, -0.33, 0.115]
          - [ru, slavic, high, 44, 0.652, 0.728, 7.6, -0.25, 0.239]
          - [pl, slavic, mid, 44, 0.628, 0.728, 10.0, -0.14, 0.513]
          - [ar, afroasiatic, mid, 40, 0.625, 0.721, 9.6, -0.18, 0.399]
          - [id, austronesian, mid, 40, 0.621, 0.721, 10.0, -0.02, 0.926]
          - [hi, indic, mid, 40, 0.618, 0.721, 10.3, -0.11, 0.609]
          - [uk, slavic, mid, 40, 0.614, 0.721, 10.7, -0.06, 0.782]
          - [vi, austroasiatic, mid, 40, 0.607, 0.721, 11.4, 0.04, 0.854]
          - [th, tai_kadai, mid, 36, 0.594, 0.712, 11.8, 0.09, 0.674]
          - [bn, indic, low, 28, 0.553, 0.694, 14.1, 0.14, 0.514]
          - [te, dravidian, low, 28, 0.571, 0.694, 12.3, 0.18, 0.400]
          - [ta, dravidian, low, 28, 0.568, 0.694, 12.6, 0.22, 0.303]
          - [sw, niger_congo, low, 28, 0.537, 0.694, 15.7, 0.27, 0.202]
          - [yo, niger_congo, low, 24, 0.512, 0.711, 19.9, 0.31, 0.141]
      - name: "Table 3: Qwen3-235B Transfer Method Comparison (19-Language Mean at Oracle Layer)"
        columns: [method, auroc_mean, auroc_median, auroc_std, ece_mean, delta_vs_zs_pp, cohens_d_vs_zs, labels_needed]
        rows:
          - [zero_shot, 0.618, 0.618, 0.046, 0.191, 0.0, "—", 0]
          - [mean_shift, 0.618, 0.618, 0.046, 0.207, 0.0, 0.00, 0]
          - [linear_projection, 0.636, 0.633, 0.042, 0.176, 1.8, 0.24, "~50 parallel"]
          - [few_shot_25, 0.644, 0.641, 0.040, 0.169, 2.6, 0.35, "25 target"]
          - [few_shot_100, 0.662, 0.659, 0.037, 0.154, 4.4, 0.58, "100 target"]
    figures_description:
      - >
        Figure 1a: Heatmap of zero-shot transfer AUROC (y: 24 layers by depth, x: 19
        languages sorted by resource tier). Upper-left (deep × high-resource) shows moderate
        AUROC (0.63–0.67); lower-right (shallow × low-resource) near chance (0.50–0.55).
        Pattern is noisy with no crisp diagonal. Non-monotonic dips at layers 40–56 where
        MoE routing transitions break the depth gradient.
      - >
        Figure 1b: Pareto frontier scatter (x: mean 19-lang ZS AUROC, y: EN AUROC per layer).
        5 non-dominated layers form a thin, noisy front. Error bars (bootstrap 95% CI) overlap
        substantially between adjacent Pareto points — the tradeoff is real but not practically
        exploitable as an engineering tool.
      - >
        Figure 1c: Per-language Spearman ρ (depth vs transfer AUROC) bar chart, colored by
        resource tier. High-resource languages show negative ρ (blue bars extending left);
        low-resource show positive or near-zero ρ (red bars extending right). Dashed line at
        median ρ = −0.25. Confidence intervals from Fisher z-transform.
    analysis: >
      Pareto frontier on Qwen3-235B is real but weak: ρ = −0.38 globally, median per-language
      ρ = −0.25 (explains ~6% of per-language variance). The resource-tier gradient is the
      cleanest finding: high-resource langs (mean 0.663) transfer at 7–8pp below EN,
      mid-resource (0.615) at 10–11pp, low-resource (0.548) at 13–20pp. Mean-shift is
      confirmed mathematically dead (ΔAUROC ≡ 0, validated across all 24 layers × 19 langs).
      Linear projection and few-shot are the only viable transfer methods. For 12/19 languages,
      zero-shot transfer AUROC stays below 0.65 — the field should not assume English probes
      generalize.

  # ============================================================
  # plan_002 — Full Pareto Frontier: Llama 4 Scout
  # ============================================================
  - name: "Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, INT8)"
    plan_id: plan_002
    description: >
      Extract activations at 12 probed layers (every 4th of 48), 20 languages on GlobalMMLU.
      Train English correctness probes, evaluate 5 transfer conditions. INT8 weight quantization.
      Report per-language Spearman ρ. Bootstrap CIs + paired tests + Cohen's d.
    expected_results:
      en_auroc_best_layer: 0.749
      en_best_layer_idx: 36
      en_auroc_range: [0.598, 0.749]
      en_ece_raw_best: 0.188
      en_ece_tempcal_best: 0.074
      temp_scaling_T: 5.47
      zs_transfer_auroc_mean_19lang: 0.588
      zs_transfer_auroc_median_19lang: 0.593
      zs_transfer_auroc_std_19lang: 0.054
      zs_transfer_drop_mean_pp: 18.4
      zs_langs_above_0p65: 5
      zs_pass_langs: [fr, zh, de, ko, es]
      zs_fail_langs: [ja, ru, ar, hi, vi, id, th, pl, uk, bn, te, ta, sw, yo]
      mean_shift_delta_auroc_all_langs: 0.000
      linproj_auroc_mean_19lang: 0.608
      linproj_improves_over_zs_count: 10
      fewshot25_auroc_mean_19lang: 0.617
      fewshot100_auroc_mean_19lang: 0.641
      pareto_global_spearman_rho: -0.18
      pareto_per_lang_rho_median: -0.12
      pareto_per_lang_rho_range: [-0.41, 0.48]
      pareto_rho_sign_consistency: 0.53
      pareto_frontier_n_nondominated: 3
      pareto_frontier_monotonic: false
      pareto_frontier_agreement_with_qwen3_tau: 0.33
      nonmonotonic_layers: [20, 24, 28]
      per_lang_zs_auroc:
        fr: 0.662
        zh: 0.658
        de: 0.655
        ko: 0.652
        es: 0.651
        ja: 0.634
        ru: 0.622
        pl: 0.608
        ar: 0.589
        hi: 0.586
        id: 0.582
        uk: 0.578
        vi: 0.571
        th: 0.558
        bn: 0.532
        te: 0.541
        ta: 0.528
        sw: 0.518
        yo: 0.492
      per_lang_spearman_rho:
        fr: -0.41
        zh: -0.37
        de: -0.32
        ko: -0.21
        es: -0.18
        ja: -0.08
        ru: -0.04
        pl: 0.03
        ar: 0.07
        hi: 0.11
        id: 0.15
        uk: 0.18
        vi: 0.22
        th: 0.28
        bn: 0.31
        te: 0.35
        ta: 0.38
        sw: 0.43
        yo: 0.48
    result_rationale: >
      Llama 4 Scout is the worst-tier's key failure for the Pareto claim. Its 48 layers give
      only 12 probed points (vs 24 for Qwen3), reducing statistical power for Spearman ρ. More
      critically, Llama 4 Scout uses a different MoE routing strategy where experts are more
      language-specialized at intermediate layers (20–28), creating non-monotonic jumps in
      transfer AUROC that break the depth gradient. Per-language rho median = −0.12 means the
      depth-transfer tradeoff essentially vanishes on this architecture. Only 5/19 languages
      pass 0.65 (vs 7 for Qwen3), and the cross-architecture Pareto agreement is τ = 0.33 —
      optimal layer for a language on Qwen3 does not predict optimal layer on Llama 4. English
      AUROC peaks lower (0.749 vs 0.776) because the 48-layer structure compresses the
      representational hierarchy. Transfer is worse overall (0.588 vs 0.618) reflecting
      more English-centric training data and sparser expert allocation for non-English. The
      0.53 sign consistency means the depth-transfer direction is nearly coin-flip across
      languages — the "Pareto frontier" is architecture-specific, not a universal property.
    tables:
      - name: "Table 4: Llama 4 Scout English Probe Performance by Layer"
        columns: [layer, depth_pct, logreg_auroc, mlp_auroc, ece_raw, ece_tempcal]
        rows:
          - [4,  8,   0.598, 0.604, 0.312, 0.201]
          - [8,  17,  0.631, 0.641, 0.274, 0.168]
          - [12, 25,  0.668, 0.679, 0.241, 0.137]
          - [16, 33,  0.694, 0.706, 0.218, 0.112]
          - [20, 42,  0.712, 0.722, 0.205, 0.098]
          - [24, 50,  0.726, 0.735, 0.196, 0.088]
          - [28, 58,  0.734, 0.743, 0.192, 0.083]
          - [32, 67,  0.741, 0.749, 0.189, 0.078]
          - [36, 75,  0.749, 0.755, 0.188, 0.074]
          - [40, 83,  0.744, 0.751, 0.190, 0.077]
          - [44, 92,  0.731, 0.738, 0.195, 0.084]
          - [48, 100, 0.708, 0.718, 0.209, 0.097]
      - name: "Table 5: Llama 4 Scout Zero-Shot Transfer AUROC by Language"
        columns: [language, resource_tier, best_zs_layer, best_zs_auroc, drop_vs_en_pp, spearman_rho]
        rows:
          - [fr,  high, 24, 0.662, 6.4,  -0.41]
          - [zh,  high, 24, 0.658, 6.8,  -0.37]
          - [de,  high, 24, 0.655, 7.1,  -0.32]
          - [ko,  high, 20, 0.652, 6.0,  -0.21]
          - [es,  high, 24, 0.651, 7.5,  -0.18]
          - [ja,  high, 20, 0.634, 7.8,  -0.08]
          - [ru,  high, 20, 0.622, 9.0,  -0.04]
          - [pl,  mid,  20, 0.608, 10.4, 0.03]
          - [ar,  mid,  16, 0.589, 10.5, 0.07]
          - [hi,  mid,  16, 0.586, 10.8, 0.11]
          - [id,  mid,  16, 0.582, 11.2, 0.15]
          - [uk,  mid,  16, 0.578, 11.6, 0.18]
          - [vi,  mid,  16, 0.571, 12.3, 0.22]
          - [th,  mid,  16, 0.558, 13.6, 0.28]
          - [te,  low,  12, 0.541, 12.7, 0.35]
          - [bn,  low,  12, 0.532, 13.6, 0.31]
          - [ta,  low,  12, 0.528, 14.0, 0.38]
          - [sw,  low,  12, 0.518, 15.0, 0.43]
          - [yo,  low,  8,  0.492, 13.9, 0.48]
      - name: "Table 6: Cross-Architecture Pareto Agreement"
        columns: [metric, qwen3_235b, llama4_scout, agreement]
        rows:
          - [global_spearman_rho, -0.38, -0.18, "—"]
          - [per_lang_rho_median, -0.25, -0.12, "—"]
          - [sign_consistency, 0.63, 0.53, "—"]
          - [n_nondominated, "5/24", "3/12", "—"]
          - [zs_auroc_mean, 0.618, 0.588, "—"]
          - [optimal_layer_rank_tau, "—", "—", 0.33]
          - [pass_lang_jaccard, "—", "—", 0.47]
    figures_description:
      - >
        Figure 2a: Side-by-side Pareto scatter plots. Qwen3 (left) shows a discernible convex
        front with 5 non-dominated points. Llama 4 (right) shows a near-flat cloud with 3
        weakly non-dominated points — no meaningful tradeoff curve. Key Figure 2 evidence
        for architecture dependence.
      - >
        Figure 2b: Llama 4 non-monotonicity detail — line plot of transfer AUROC vs layer depth
        for zh, fr, ar, sw. Bump at L20, dip at L24, partial recovery at L28 for zh/fr.
        Attributed to MoE routing transitions.
      - >
        Figure 2c: Per-language Spearman ρ comparison (Qwen3 vs Llama4), paired bar chart.
        High-resource languages show negative ρ on both (but weaker on Llama4). Low-resource
        languages show positive ρ on both architectures.
    analysis: >
      Llama 4 Scout demolishes the universal Pareto claim. ρ = −0.18 globally, median per-lang
      ρ = −0.12, sign consistency 0.53. Cross-architecture agreement τ = 0.33. This transforms
      the paper: the depth-transfer tradeoff is architecture-dependent, not a universal
      transformer property. Practitioners cannot use layer selection findings from one model on
      another. For the diagnostic paper, this is reframed as a key finding: "the field cannot
      assume probe-based calibration will behave consistently across architectures."

  # ============================================================
  # plan_003 — CaCLR Implementation and Comparative Evaluation
  # ============================================================
  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: plan_003
    description: >
      Implement CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency with MMD). Train using English
      labels + unlabeled parallel activations from GlobalMMLU train split. Compare vs zero-shot,
      mean-shift, linear projection, few-shot across full Pareto frontier for both models × 19
      target languages. α sweep (0.01–10.0), β sweep across 3 OOM (0.001–1.0). Fixed-layer
      results (50% depth + EN-optimal) alongside per-language oracle.
    expected_results:
      best_alpha: 0.3
      best_beta: 0.05
      beta_sensitivity: "flat — β from 0.001 to 1.0 changes AUROC by <0.4pp; consistency loss is inert"
      alpha_sensitivity: "moderate — α = 0.1–1.0 gives similar results; inverted-U peaking at 0.3"
      caclr_auroc_mean_qwen3: 0.623
      caclr_auroc_mean_llama4: 0.594
      caclr_vs_zs_delta_auroc_mean_pp_qwen3: 0.5
      caclr_vs_zs_delta_auroc_mean_pp_llama4: 0.6
      caclr_vs_zs_delta_auroc_median_pp: 0.003
      caclr_vs_linproj_delta_auroc_mean_pp_qwen3: -1.3
      caclr_vs_linproj_delta_auroc_mean_pp_llama4: -1.4
      caclr_vs_fewshot100_delta_pp_qwen3: -3.9
      caclr_vs_fewshot100_delta_pp_llama4: -4.7
      caclr_ece_mean_qwen3: 0.186
      caclr_ece_mean_llama4: 0.201
      caclr_ece_reduction_vs_tempcal_pp: -0.002
      ablation_bce_only_auroc_mean: 0.618
      ablation_bce_sbece_auroc_mean: 0.627
      ablation_bce_consistency_auroc_mean: 0.611
      ablation_full_caclr_auroc_mean: 0.621
      beta_delta_over_alpha_only_pp: -0.006
      cohens_d_caclr_vs_zs: 0.04
      cohens_d_caclr_vs_linproj: -0.18
      permutation_test_caclr_vs_zs_p: 0.71
      caclr_per_lang_qwen3:
        zh: {auroc: 0.671, delta_vs_zs_pp: 0.3}
        fr: {auroc: 0.667, delta_vs_zs_pp: -0.5}
        de: {auroc: 0.664, delta_vs_zs_pp: -0.7}
        es: {auroc: 0.657, delta_vs_zs_pp: -0.4}
        ja: {auroc: 0.653, delta_vs_zs_pp: -0.5}
        ko: {auroc: 0.652, delta_vs_zs_pp: -0.4}
        ru: {auroc: 0.649, delta_vs_zs_pp: -0.3}
        pl: {auroc: 0.631, delta_vs_zs_pp: 0.3}
        ar: {auroc: 0.631, delta_vs_zs_pp: 0.6}
        id: {auroc: 0.627, delta_vs_zs_pp: 0.6}
        hi: {auroc: 0.625, delta_vs_zs_pp: 0.7}
        uk: {auroc: 0.621, delta_vs_zs_pp: 0.7}
        vi: {auroc: 0.615, delta_vs_zs_pp: 0.8}
        th: {auroc: 0.603, delta_vs_zs_pp: 0.9}
        bn: {auroc: 0.564, delta_vs_zs_pp: 1.1}
        te: {auroc: 0.581, delta_vs_zs_pp: 1.0}
        ta: {auroc: 0.578, delta_vs_zs_pp: 1.0}
        sw: {auroc: 0.549, delta_vs_zs_pp: 1.2}
        yo: {auroc: 0.526, delta_vs_zs_pp: 1.4}
    result_rationale: >
      CaCLR fully fails as a method contribution. The consistency loss (β·L_consistency) is
      inert: sweeping β over 3 orders of magnitude produces a flat AUROC landscape (<0.4pp
      variation). Adding consistency to BCE+SB-ECE actually hurts by −0.6pp because MMD-based
      alignment collapses both signal and noise — the unlabeled parallel activations contain
      massive language-specific variance (script, morphology, tokenization artifacts) that
      dominates the correctness signal. Minimizing distributional distance between languages
      forces the probe to ignore language-specific activation patterns that sometimes carry
      cross-lingual correctness information. The ablation reveals that the only beneficial
      component is SB-ECE regularization (+0.9pp), which acts as a calibration regularizer on
      the English training side but has nothing to do with cross-lingual transfer. Full CaCLR
      ends up as "zero-shot + SB-ECE regularization" — a trivially achievable benefit that does
      not justify the method's complexity. Linear projection beats CaCLR because it directly
      estimates the geometric transformation between language subspaces, which is more data-efficient
      than trying to learn an invariant representation from noisy distributional signals. The
      paired permutation test CaCLR vs zero-shot gives p = 0.71 — no significant difference.
      Cohen's d = 0.04 confirms negligible effect size. CaCLR slightly helps low-resource
      languages (+1pp) and slightly hurts high-resource (−0.5pp), but both effects are within
      noise. For the paper, CaCLR is relegated to one paragraph: "the natural distributional-
      matching approach fails — consistency-based objectives do not help when cross-lingual
      correctness SNR is low."
    tables:
      - name: "Table 7: Transfer Method Comparison — Both Models (19-Language Mean)"
        columns: [method, qwen3_auroc, qwen3_ece, llama4_auroc, llama4_ece, cohens_d_vs_zs, labels_needed]
        rows:
          - [zero_shot,          0.618, 0.191, 0.588, 0.208, "—",    "0 target"]
          - [mean_shift,         0.618, 0.207, 0.588, 0.224, 0.00,   "0 target (ΔAUROC≡0)"]
          - [CaCLR,              0.623, 0.186, 0.594, 0.201, 0.04,   "0 target + parallel"]
          - [linear_projection,  0.636, 0.176, 0.608, 0.189, 0.24,   "~50 parallel"]
          - [few_shot_25,        0.644, 0.169, 0.617, 0.182, 0.35,   "25 target"]
          - [few_shot_100,       0.662, 0.154, 0.641, 0.168, 0.58,   "100 target"]
      - name: "Table 8: CaCLR Ablation (Qwen3-235B, 19-Language Mean)"
        columns: [variant, auroc_mean, ece_mean, delta_vs_full_pp]
        rows:
          - ["Full CaCLR (BCE+SB-ECE+Consistency)", 0.621, 0.186, 0.0]
          - ["BCE+SB-ECE (no consistency)",          0.627, 0.179, 0.6]
          - ["BCE+Consistency (no SB-ECE)",          0.611, 0.198, -1.0]
          - ["BCE only (= zero-shot probe)",         0.618, 0.191, -0.3]
          - ["Linear Projection (reference)",        0.636, 0.176, 1.5]
      - name: "Table 9: CaCLR β Sensitivity (Qwen3, α fixed at 0.3, 19-lang mean AUROC)"
        columns: [beta, auroc_mean, delta_vs_beta0_pp]
        rows:
          - [0.000, 0.627, 0.0]
          - [0.001, 0.626, -0.1]
          - [0.005, 0.625, -0.2]
          - [0.01,  0.625, -0.2]
          - [0.05,  0.623, -0.4]
          - [0.10,  0.621, -0.6]
          - [0.50,  0.618, -0.9]
          - [1.00,  0.614, -1.3]
    figures_description:
      - >
        Figure 3a: Grouped bar chart of 6 methods × 19 languages (Qwen3), sorted by resource
        tier. Few-shot-100 > few-shot-25 ≈ linproj > CaCLR ≈ zero-shot >> mean-shift (dead).
        CaCLR and zero-shot bars nearly identical height everywhere. Visual message: CaCLR adds
        complexity for zero benefit.
      - >
        Figure 3b: Hyperparameter sensitivity. Left: AUROC vs α, gentle inverted-U peaking
        at 0.3. Right: AUROC vs β (log scale), flat line with slight downward trend — β is
        inert at best, harmful at worst. This is the key evidence that consistency loss fails.
      - >
        Figure 3c: Per-language CaCLR delta (y) vs ZS baseline AUROC (x). Slight positive slope
        (CaCLR helps low-resource modestly, hurts high-resource slightly). But all deltas within
        ±1.5pp. Linear projection dominates CaCLR at every point.
    analysis: >
      CaCLR is a rigorous negative result. The ablation cleanly isolates the failure: consistency
      loss is harmful (adding it to BCE+SB-ECE reduces AUROC by 0.6pp). The β sweep over 3 OOM
      confirms this is not a tuning failure — the entire β landscape is flat or declining. CKA
      analysis (plan_011) provides the mechanistic explanation: cross-lingual misalignment at
      deeper layers is geometric (correctness direction rotates), not distributional (mean/cov
      shift). MMD-based alignment cannot correct rotation, which is why linear projection (learns
      rotation) succeeds where CaCLR (matches distributions) fails. For the paper, CaCLR is
      reported as attempted-and-failed, saving the community from pursuing distributional-matching
      approaches for this problem class.

  # ============================================================
  # plan_004 — Difficulty-Controlled Ablation (Decomposition)
  # ============================================================
  - name: "Difficulty-Controlled Ablation (Decomposition)"
    plan_id: plan_004
    description: >
      Train IRT difficulty probes (Ridge regression on human difficulty scores per Civelli et al.),
      project out difficulty direction from activations, retrain correctness probes on residuals,
      evaluate transfer. 10 languages × 8 layers per model. Include random-direction control.
    expected_results:
      difficulty_probe_r2_en_qwen3: 0.52
      difficulty_probe_r2_en_llama4: 0.47
      difficulty_probe_transfer_r2_mean_9lang: 0.38
      decomp_difficulty_var_explained_pct_qwen3: 14.3
      decomp_difficulty_var_explained_pct_llama4: 11.8
      correctness_on_residual_auroc_en_qwen3: 0.741
      correctness_on_residual_auroc_en_llama4: 0.714
      residual_transfer_auroc_mean_qwen3: 0.613
      residual_transfer_auroc_mean_llama4: 0.583
      transfer_delta_after_projection_pp_qwen3: -0.5
      transfer_delta_after_projection_pp_llama4: -0.5
      transfer_delta_range_across_langs_pp: [-2.1, 1.3]
      random_direction_control_delta_pp: -0.3
      difficulty_correctness_cosine_mean: 0.36
      difficulty_correctness_cosine_std: 0.11
      decomp_prescriptive: false
      pct_langs_helped_by_projection: 0.30
      pct_langs_hurt_by_projection: 0.50
      pct_langs_unchanged: 0.20
    result_rationale: >
      Decomposition is inconclusive. Projecting out difficulty direction changes transfer AUROC
      by −0.5pp on average — within noise (random-direction control shows −0.3pp from
      dimensionality reduction alone). The per-language pattern shows no systematic structure:
      3/10 languages improve slightly (1–1.3pp), 5/10 worsen (0.5–2.1pp), 2/10 unchanged. The
      difficulty direction explains only 14% of correctness variance (Qwen3), meaning the
      decomposition captures a real but minor factor. Critically, the difficulty-shared component
      turns out to carry useful cross-lingual signal: questions that are hard in English tend
      to be hard everywhere, and this shared difficulty is one of few reliable cross-lingual
      bridges. Removing it strips away a genuine invariance. The residual "capability-specific"
      component is more language-dependent, not less — containing idiosyncratic encoding
      patterns. The cosine between difficulty and correctness directions (0.36 ± 0.11) confirms
      they are neither orthogonal nor aligned — the moderate overlap prevents clean separation.
      This contradicts Claim 2's hypothesis that decomposition would be prescriptive. For the
      paper, decomposition is reported as "difficulty and capability are entangled in multilingual
      representations, unlike the clean separation assumed by English-only work."
    tables:
      - name: "Table 10: Difficulty Probe Quality (Ridge, R² on Held-Out)"
        columns: [language, resource_tier, qwen3_r2, llama4_r2]
        rows:
          - [en, "—", 0.52, 0.47]
          - [zh, high, 0.48, 0.43]
          - [fr, high, 0.47, 0.42]
          - [de, high, 0.46, 0.41]
          - [hi, mid,  0.41, 0.36]
          - [ru, mid,  0.43, 0.38]
          - [ko, mid,  0.42, 0.37]
          - [tr, mid,  0.39, 0.34]
          - [sw, low,  0.30, 0.25]
          - [bn, low,  0.28, 0.23]
      - name: "Table 11: Decomposition Transfer Ablation (9-Language Mean)"
        columns: [condition, qwen3_auroc, qwen3_delta_pp, llama4_auroc, llama4_delta_pp]
        rows:
          - ["Full activations (baseline)", 0.618, 0.0,  0.588, 0.0]
          - ["Residual (difficulty out)",    0.613, -0.5, 0.583, -0.5]
          - ["Difficulty component only",    0.569, -4.9, 0.548, -4.0]
          - ["Random direction out (ctrl)",  0.615, -0.3, 0.585, -0.3]
      - name: "Table 12: Per-Language Transfer Delta After Difficulty Projection (Qwen3)"
        columns: [language, resource_tier, delta_auroc_pp, direction]
        rows:
          - [zh, high, -0.8,  hurt]
          - [fr, high, -1.2,  hurt]
          - [de, high, -0.6,  hurt]
          - [hi, mid,   0.4,  helped]
          - [ru, mid,  -0.3,  unchanged]
          - [ko, mid,   1.0,  helped]
          - [tr, mid,  -2.1,  hurt]
          - [sw, low,   1.3,  helped]
          - [bn, low,  -0.8,  hurt]
    figures_description:
      - >
        Figure 4a: Scatter of per-language transfer delta after projection (y) vs baseline ZS
        AUROC (x). Points scatter around zero with no clear pattern — helps some, hurts others,
        irrespective of resource tier. The random-direction control mean (dashed line at −0.3pp)
        shows the projection delta is barely distinguishable from dimensionality-reduction noise.
      - >
        Figure 4b: Principal angle histogram between difficulty and correctness subspaces. Peak
        at ~55–60° with wide spread (std ~11°) across layers and languages. Far from both
        0° and 90° — the relationship is inconsistent, preventing clean decomposition.
    analysis: >
      Decomposition fails as a prescriptive tool. The difficulty-shared component is load-bearing
      for cross-lingual transfer — removing it hurts more often than it helps (5/10 vs 3/10),
      and the average delta (−0.5pp) is barely above the random-direction control (−0.3pp).
      The original Claim 2 hypothesis is abandoned. For the diagnostic paper, this becomes:
      "difficulty and capability are entangled in multilingual representations — the clean
      separation reported in English-only work does not generalize cross-lingually."

  # ============================================================
  # plan_005 — Cross-Lingual Orthogonality Analysis
  # ============================================================
  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: plan_005
    description: >
      Extract verbalized confidence direction (prompt model for confidence score, fit probe),
      compute cosine similarity with correctness direction across 20 languages × 2 architectures.
      Analyze by resource tier and language family.
    expected_results:
      orthogonality_cosine_mean_overall: 0.074
      orthogonality_cosine_std_overall: 0.036
      orthogonality_cosine_mean_qwen3: 0.069
      orthogonality_cosine_mean_llama4: 0.079
      orthogonality_cosine_max_across_all: 0.172
      orthogonality_cosine_high_resource: 0.052
      orthogonality_cosine_mid_resource: 0.073
      orthogonality_cosine_low_resource: 0.108
      pct_langs_cosine_below_0p10: 0.73
      pct_langs_cosine_below_0p05: 0.30
      outlier_langs_above_0p15: [yo_llama4]
      confidence_probe_r2_en: 0.71
      confidence_probe_transfer_r2_mean: 0.58
      cosine_resource_tier_spearman: -0.61
      per_lang_cosine:
        en:  {qwen3: 0.036, llama4: 0.041, mean: 0.039}
        zh:  {qwen3: 0.041, llama4: 0.048, mean: 0.045}
        fr:  {qwen3: 0.044, llama4: 0.052, mean: 0.048}
        de:  {qwen3: 0.046, llama4: 0.054, mean: 0.050}
        es:  {qwen3: 0.048, llama4: 0.057, mean: 0.053}
        ja:  {qwen3: 0.053, llama4: 0.061, mean: 0.057}
        ru:  {qwen3: 0.056, llama4: 0.064, mean: 0.060}
        ko:  {qwen3: 0.058, llama4: 0.067, mean: 0.063}
        ar:  {qwen3: 0.064, llama4: 0.073, mean: 0.069}
        hi:  {qwen3: 0.067, llama4: 0.076, mean: 0.072}
        vi:  {qwen3: 0.069, llama4: 0.078, mean: 0.074}
        id:  {qwen3: 0.065, llama4: 0.074, mean: 0.070}
        th:  {qwen3: 0.074, llama4: 0.084, mean: 0.079}
        pl:  {qwen3: 0.060, llama4: 0.068, mean: 0.064}
        uk:  {qwen3: 0.063, llama4: 0.072, mean: 0.068}
        bn:  {qwen3: 0.085, llama4: 0.098, mean: 0.092}
        te:  {qwen3: 0.092, llama4: 0.106, mean: 0.099}
        ta:  {qwen3: 0.096, llama4: 0.112, mean: 0.104}
        sw:  {qwen3: 0.104, llama4: 0.124, mean: 0.114}
        yo:  {qwen3: 0.121, llama4: 0.172, mean: 0.147}
    result_rationale: >
      Orthogonality persists cross-lingually (mean cosine 0.074) because it reflects a structural
      property of how LLMs separate verbalized confidence from actual correctness at the
      representation level. However, the worst-tier variance is higher than Miao & Ungar's
      English-only finding (std 0.036 vs ~0.01): low-resource languages show weaker
      orthogonality (cosine ~0.108) because the model has less capacity to maintain the
      confidence-correctness dissociation for languages with limited training data. Yoruba on
      Llama4 reaches 0.172 — an outlier above the 0.15 threshold that weakens the universality
      claim. This happens because Llama4 has minimal Yoruba training data, so both correctness
      and confidence signals degrade in correlated ways, partially breaking orthogonality. The
      resource-tier gradient (high: 0.052, mid: 0.073, low: 0.108, Spearman ρ = −0.61 with
      resource level) is the novel angle, but effect size is modest. Reviewers may see the
      extension from English-only (Miao & Ungar) to 20 languages as incremental rather than
      novel, since the qualitative finding is the same.
    tables:
      - name: "Table 13: Correctness-Confidence Cosine Similarity by Resource Tier"
        columns: [resource_tier, n_langs, qwen3_mean, llama4_mean, overall_mean, std]
        rows:
          - [high, 8, 0.048, 0.056, 0.052, 0.008]
          - [mid,  7, 0.066, 0.075, 0.073, 0.005]
          - [low,  5, 0.100, 0.122, 0.108, 0.020]
          - [all, 20, 0.069, 0.079, 0.074, 0.036]
    figures_description:
      - >
        Figure 5a: Bar chart of cosine similarity for 20 languages, sorted by resource tier.
        Miao & Ungar's English threshold (0.04) as dashed line. Most high-resource near the line;
        low-resource 2–3× higher. Yoruba (0.172 on Llama4) breaches 0.15, marked with asterisk.
      - >
        Figure 5b: Scatter of cosine (y) vs log resource size (x), colored by architecture.
        Moderate negative correlation. Yoruba is the visible outlier pulling the trend.
    analysis: >
      Orthogonality survives as the one mechanistic takeaway: output-based calibration is
      structurally limited everywhere, not just in English. But the contribution is incremental —
      same qualitative finding as Miao & Ungar, extended to 20 languages. The resource-tier
      modulation is novel (effect size 0.052 vs 0.108) but the Yoruba outlier at 0.172
      weakens the universality claim. For the paper: "correctness-confidence dissociation is
      multilingual, confirming output-based calibration faces a structural ceiling regardless
      of language, but this ceiling is noisier for low-resource languages."

  # ============================================================
  # plan_006 — Probe Complexity Comparison
  # ============================================================
  - name: "Probe Complexity Comparison"
    plan_id: plan_006
    description: >
      Logistic regression vs 2-layer MLP at each probed layer for both models. Compare English
      accuracy, cross-lingual transfer, calibration. Test hypothesis: linear probes transfer better.
    expected_results:
      mlp_vs_logreg_en_auroc_delta_mean_pp: 1.0
      mlp_vs_logreg_transfer_auroc_delta_mean_pp: -0.3
      hypothesis_linear_transfers_better: "weak support"
      cohens_d_transfer_difference: 0.15
      permutation_test_p: 0.34
      mlp_en_advantage_deep_layers_pp: 1.4
      logreg_transfer_advantage_deep_layers_pp: 0.6
      interaction_depth_probe_significant: false
    result_rationale: >
      Linear probes transfer marginally better (−0.3pp MLP penalty in transfer vs +1.0pp MLP
      advantage in English), but Cohen's d = 0.15 and the permutation test is non-significant
      (p = 0.34). The effect is too small to be practically meaningful. MLP captures mild
      nonlinearities in the correctness signal but these are English-specific features that
      don't generalize. The depth interaction exists weakly (MLP overfits more at deep layers)
      but isn't statistically significant as an interaction term. This validates logistic
      regression as the right default but generates no standalone finding.
    tables:
      - name: "Table 14: Probe Complexity Comparison (Mean Across All Layers)"
        columns: [model, probe, en_auroc_mean, transfer_auroc_mean, en_ece_mean, transfer_ece_mean]
        rows:
          - [qwen3, logreg, 0.714, 0.618, 0.206, 0.191]
          - [qwen3, mlp,    0.725, 0.615, 0.198, 0.194]
          - [llama4, logreg, 0.697, 0.588, 0.219, 0.208]
          - [llama4, mlp,    0.706, 0.586, 0.212, 0.211]
    figures_description:
      - >
        Figure S1 (supp): Paired difference plot (MLP − LogReg AUROC) vs layer depth. English
        panel: positive, increasing with depth. Transfer panel: near-zero, slightly negative.
        Bootstrap CIs overlap zero at most layers for transfer.
    analysis: >
      Non-finding. Effect is real but negligible (d = 0.15). Logistic regression confirmed as
      default choice: simpler, nearly identical performance, better interpretability. Goes in
      supplementary as methods validation.

  # ============================================================
  # plan_007 — Additional Benchmark Evaluation
  # ============================================================
  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: plan_007
    description: >
      Evaluate best probes + CaCLR on Belebele (reading comprehension, 20 languages) and
      MMLU-ProX (translated MMLU, 20 languages). Tests cross-benchmark generalization.
    expected_results:
      belebele_en_auroc_qwen3: 0.741
      belebele_en_auroc_llama4: 0.718
      belebele_zs_transfer_mean_qwen3: 0.594
      belebele_zs_transfer_mean_llama4: 0.567
      belebele_drop_vs_globalmmlu_pp: 2.4
      belebele_caclr_delta_vs_linproj_pp: -0.8
      mmlupx_en_auroc_qwen3: 0.762
      mmlupx_en_auroc_llama4: 0.738
      mmlupx_zs_transfer_mean_qwen3: 0.579
      mmlupx_zs_transfer_mean_llama4: 0.551
      mmlupx_drop_vs_globalmmlu_pp: 3.9
      mmlupx_caclr_delta_vs_linproj_pp: -1.1
      lang_rank_corr_globalmmlu_belebele: 0.83
      lang_rank_corr_globalmmlu_mmlupx: 0.69
    result_rationale: >
      Belebele partially replicates because it is high-quality and natively multilingual. The
      2.4pp transfer drop reflects domain shift (reading comprehension vs knowledge). MMLU-ProX
      shows worse transfer (3.9pp drop) because machine-translated MMLU introduces systematic
      distributional shifts (ambiguous domain terms, cultural references, low-resource
      translation errors). CaCLR remains worse than linear projection on both benchmarks,
      confirming the negative result generalizes. Language ranking is stable for Belebele
      (ρ = 0.83) but degrades for MMLU-ProX (ρ = 0.69) due to translation quality variation.
    tables:
      - name: "Table 15: Cross-Benchmark Generalization (19-Language Mean)"
        columns: [benchmark, zs_auroc_qwen3, zs_auroc_llama4, caclr_vs_linproj_pp, lang_rank_corr]
        rows:
          - [GlobalMMLU, 0.618, 0.588, -1.3, "—"]
          - [Belebele,   0.594, 0.567, -0.8, 0.83]
          - [MMLU-ProX,  0.579, 0.551, -1.1, 0.69]
    figures_description:
      - >
        Figure S2 (supp): Three-panel scatter showing per-language AUROC correlation across
        benchmark pairs. GlobalMMLU–Belebele tight; GlobalMMLU–MMLU-ProX noisier. Low-resource
        languages (red) are outliers on MMLU-ProX.
    analysis: >
      Findings partially generalize: Belebele confirms, MMLU-ProX is noisier. Language ranking
      stable but absolute performance degrades with domain shift. CaCLR's negative result is
      robust across all three benchmarks. Include Belebele in main results, MMLU-ProX in
      supplementary with translation-artifact caveat.

  # ============================================================
  # plan_010 — INT8 Validation Ablation
  # ============================================================
  - name: "INT8 Validation Ablation"
    plan_id: plan_010
    description: >
      Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on
      5% random subset. Validates quantization doesn't distort correctness signals.
    expected_results:
      int8_vs_fp16_auroc_delta_mean_pp: -0.3
      int8_vs_fp16_auroc_delta_max_pp: -0.7
      int8_vs_fp16_ece_delta_mean_pp: 0.2
      int8_vs_fp16_activation_cosine_sim_mean: 0.994
      int8_vs_fp16_rank_correlation_layers: 0.98
      validation_passes: true
    result_rationale: >
      INT8 quantization introduces minimal distortion. The 0.3pp mean AUROC difference is
      within noise — INT8 preserves directional structure of activations that linear probes
      rely on. Cosine similarity 0.994 between INT8 and FP16 activations confirms near-perfect
      directional alignment. Layer ranking is preserved (rank corr 0.98). This passes cleanly
      even in the worst tier — quantization is not a source of failure.
    tables:
      - name: "Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)"
        columns: [layer, fp16_auroc, int8_auroc, delta_pp, activation_cosine]
        rows:
          - [8,  0.637, 0.633, -0.4, 0.993]
          - [16, 0.700, 0.697, -0.3, 0.994]
          - [24, 0.731, 0.729, -0.2, 0.995]
          - [32, 0.746, 0.743, -0.3, 0.994]
          - [40, 0.748, 0.741, -0.7, 0.992]
    figures_description:
      - >
        Figure S3 (supp): Paired scatter of FP16 vs INT8 AUROC at all layer × language
        combinations. Points on y=x diagonal with slight downward bias. Inset: delta
        histogram centered near −0.3pp.
    analysis: >
      INT8 validation passes. Quantization is not a confound. One paragraph + Table S1
      in supplementary.

  # ============================================================
  # plan_011 — CKA Cross-Lingual Representation Similarity
  # ============================================================
  - name: "CKA Cross-Lingual Representation Similarity Analysis"
    plan_id: plan_011
    description: >
      Compute CKA (linear kernel) between English and each target language at every probed
      layer for both models. Correlate CKA with transfer AUROC to provide mechanistic explanation
      for the Pareto frontier. Full-scale validation of pilot finding (revised hypothesis:
      threshold model — transfer collapses only below critical CKA threshold ~0.35). Report
      CKA × layer × language heatmaps, CKA vs transfer degradation correlation per language,
      and threshold analysis.
    expected_results:
      cka_en_vs_target_mean_all: 0.72
      cka_decline_with_depth: true
      cka_shallow_mean: 0.89
      cka_deep_mean: 0.54
      cka_vs_transfer_auroc_pearson_r_overall: 0.32
      cka_vs_transfer_auroc_pearson_r_range_per_lang: [-0.08, 0.71]
      cka_vs_transfer_pearson_significant_langs: 7
      cka_vs_transfer_pearson_nonsig_langs: 12
      cka_threshold_0p35_replicates: "partial"
      n_lang_layer_pairs_below_threshold: 18
      transfer_collapse_below_threshold_pct: 0.61
      transfer_collapse_above_threshold_pct: 0.22
      cka_architecture_consistency: "weak"
      cka_pearson_qwen3: 0.38
      cka_pearson_llama4: 0.24
      cka_by_tier:
        high_resource_mean: 0.76
        mid_resource_mean: 0.71
        low_resource_mean: 0.64
      cka_per_lang_deep_layer:
        zh: 0.68
        fr: 0.71
        de: 0.69
        es: 0.67
        ja: 0.62
        ko: 0.60
        ru: 0.58
        ar: 0.53
        hi: 0.51
        vi: 0.48
        id: 0.52
        th: 0.45
        pl: 0.55
        uk: 0.54
        bn: 0.41
        te: 0.39
        ta: 0.37
        sw: 0.33
        yo: 0.28
      pilot_revision_validated: "partially — threshold exists but is noisy"
    result_rationale: >
      CKA declines with depth on both models (shallow 0.89 → deep 0.54), confirming that
      deeper layers are less cross-lingually aligned. However, the correlation between CKA
      and transfer AUROC is weak overall (Pearson r = 0.32, explaining ~10% of variance).
      This happens because the pilot's revised hypothesis — that transfer collapses only below
      a critical CKA threshold (~0.35) rather than declining linearly — partially replicates
      but with too much noise at full scale. Below the 0.35 threshold, 61% of language-layer
      pairs show transfer collapse (AUROC < 0.55), but 39% do not — meaning the threshold is
      suggestive, not deterministic. Above the threshold, 22% of pairs still show poor transfer,
      indicating CKA captures necessary but not sufficient conditions for transfer. Per-language
      correlations vary wildly: hi (r = 0.71, sig) and sw (r = 0.67, sig) show strong CKA-transfer
      coupling, but zh (r = 0.12, ns) and fr (r = 0.08, ns) show near-zero correlation because
      these high-resource languages transfer well regardless of CKA level. Architecture
      inconsistency is notable: Qwen3 r = 0.38, Llama4 r = 0.24 — the mechanistic explanation
      is model-dependent. For the paper, CKA provides a "suggestive but not convincing"
      mechanistic account: geometric misalignment (lower CKA) correlates with transfer failure,
      but the relationship is too noisy and architecture-dependent to serve as a reliable
      predictor or principled layer selection criterion.
    tables:
      - name: "Table 16: CKA vs Transfer AUROC Correlation by Architecture"
        columns: [model, pearson_r, p_value, n_sig_langs, n_total_langs, spearman_rho]
        rows:
          - [Qwen3-235B,   0.38, 0.002, 5, 19, 0.35]
          - [Llama4-Scout, 0.24, 0.041, 2, 19, 0.21]
          - [Combined,     0.32, 0.001, 7, 38, 0.29]
      - name: "Table 17: CKA Threshold Analysis (threshold = 0.35)"
        columns: [condition, n_pairs, mean_transfer_auroc, pct_below_0p55, pct_above_0p65]
        rows:
          - ["CKA < 0.35", 18,  0.538, 0.61, 0.11]
          - ["CKA ≥ 0.35", 438, 0.612, 0.22, 0.39]
      - name: "Table 18: CKA at Deep Layers (75% depth) by Language"
        columns: [language, resource_tier, cka_qwen3, cka_llama4, transfer_auroc_qwen3, transfer_auroc_llama4]
        rows:
          - [zh, high, 0.71, 0.65, 0.668, 0.658]
          - [fr, high, 0.74, 0.68, 0.672, 0.662]
          - [de, high, 0.72, 0.66, 0.671, 0.655]
          - [ja, high, 0.65, 0.59, 0.658, 0.634]
          - [ru, high, 0.61, 0.55, 0.652, 0.622]
          - [ar, mid,  0.56, 0.50, 0.625, 0.589]
          - [hi, mid,  0.54, 0.48, 0.618, 0.586]
          - [th, mid,  0.48, 0.42, 0.594, 0.558]
          - [sw, low,  0.36, 0.30, 0.537, 0.518]
          - [yo, low,  0.31, 0.25, 0.512, 0.492]
    figures_description:
      - >
        Figure 6a: CKA heatmap (y: layers, x: languages sorted by resource tier) for Qwen3.
        Clear gradient: top-left (shallow × high-resource) is hot (CKA > 0.85); bottom-right
        (deep × low-resource) is cool (CKA < 0.40). But the mid-region is noisy — no clean
        contour separating transfer success from failure.
      - >
        Figure 6b: Scatter of CKA (x) vs transfer AUROC (y), one point per language-layer pair,
        colored by model. Weak positive trend (r = 0.32). Vertical dashed line at CKA = 0.35
        (pilot threshold). Below threshold: most points cluster low-AUROC, but some outliers
        transfer well. Above threshold: wide spread. The scatter is too noisy for CKA to serve
        as a reliable predictor.
      - >
        Figure 6c: Per-language CKA-transfer correlation bars, sorted by magnitude. Hi and sw
        show strong correlations (r > 0.6); zh and fr near zero. Architecture-colored bars
        show Qwen3 correlations consistently higher than Llama4.
    analysis: >
      CKA provides suggestive but not convincing mechanistic explanation. The decline with
      depth is clear, and the threshold model partially replicates (61% transfer collapse
      below CKA 0.35). But the correlation is too weak (r = 0.32) and architecture-dependent
      (0.38 vs 0.24) to serve as a reliable predictor. The key insight survives at a qualitative
      level: cross-lingual misalignment is geometric, which explains why MMD-based CaCLR fails
      (it matches distributions but can't correct rotation) while linear projection succeeds
      (it learns the rotation). But the quantitative story is messy. For the paper: report CKA
      as supporting evidence for the geometric-misalignment interpretation, not as a standalone
      finding. Two paragraphs in the analysis section.

  # ============================================================
  # plan_012 — Linear Projection Sensitivity Analysis
  # ============================================================
  - name: "Linear Projection Sensitivity Analysis"
    plan_id: plan_012
    description: >
      Vary number of parallel pairs (10, 20, 50, 100, 200) for linear projection transfer.
      Determines minimum data requirement for this baseline. Both models × 5 representative
      layers × 19 target languages.
    expected_results:
      linproj_by_n_pairs:
        10:  {auroc_mean: 0.608, delta_vs_zs_pp: -1.0, pct_langs_improved: 0.26}
        20:  {auroc_mean: 0.621, delta_vs_zs_pp: 0.3,  pct_langs_improved: 0.42}
        50:  {auroc_mean: 0.636, delta_vs_zs_pp: 1.8,  pct_langs_improved: 0.55}
        100: {auroc_mean: 0.643, delta_vs_zs_pp: 2.5,  pct_langs_improved: 0.63}
        200: {auroc_mean: 0.647, delta_vs_zs_pp: 2.9,  pct_langs_improved: 0.68}
      minimum_viable_pairs_high_resource: 20
      minimum_viable_pairs_mid_resource: 50
      minimum_viable_pairs_low_resource: ">200 (insufficient quality)"
      saturation_point: "~100 pairs — diminishing returns beyond"
      linproj_fails_low_resource: true
      low_resource_at_200_pairs:
        bn: {auroc: 0.561, delta_vs_zs_pp: 0.8}
        te: {auroc: 0.576, delta_vs_zs_pp: 0.5}
        ta: {auroc: 0.571, delta_vs_zs_pp: 0.3}
        sw: {auroc: 0.543, delta_vs_zs_pp: 0.6}
        yo: {auroc: 0.518, delta_vs_zs_pp: 0.6}
      high_resource_at_50_pairs:
        zh: {auroc: 0.681, delta_vs_zs_pp: 1.3}
        fr: {auroc: 0.686, delta_vs_zs_pp: 1.4}
        de: {auroc: 0.684, delta_vs_zs_pp: 1.3}
      variance_across_random_subsets_std_pp: 1.8
    result_rationale: >
      Linear projection's effectiveness depends heavily on the number and quality of parallel
      pairs. At 10 pairs, the affine transformation is underestimated (high-dimensional activation
      space needs more samples to estimate rotation matrix reliably), actually hurting transfer
      (−1.0pp) by introducing noise. At 20 pairs, high-resource languages start benefiting
      because their parallel pairs have high translation quality and the activation subspaces
      are already partially aligned. At 50 pairs, the projection stabilizes for high and
      mid-resource languages (the "default" setting in the main experiments). But low-resource
      languages fail even at 200 pairs for two reasons: (1) GlobalMMLU parallel translations
      for sw/yo/bn are lower quality (more literal, less natural), so the parallel activations
      don't capture the true language-specific encoding; (2) the activation subspace for these
      languages is itself noisier (less structured due to limited pretraining), making the
      rotation hard to estimate even with many pairs. The variance across random subsets
      (std 1.8pp) is high, indicating the projection is sensitive to which specific pairs are
      used — this is a practical reliability concern. Saturation at ~100 pairs means the
      projection captures most learnable alignment, and remaining transfer gap is due to
      fundamental representational differences, not data limitation.
    tables:
      - name: "Table 19: Linear Projection AUROC by Number of Parallel Pairs (19-Lang Mean)"
        columns: [n_pairs, auroc_mean, auroc_std, delta_vs_zs_pp, pct_langs_improved, pct_langs_hurt]
        rows:
          - [10,  0.608, 0.052, -1.0, 0.26, 0.53]
          - [20,  0.621, 0.047, 0.3,  0.42, 0.32]
          - [50,  0.636, 0.042, 1.8,  0.55, 0.21]
          - [100, 0.643, 0.040, 2.5,  0.63, 0.16]
          - [200, 0.647, 0.039, 2.9,  0.68, 0.11]
      - name: "Table 20: Linear Projection at 50 Pairs by Resource Tier"
        columns: [resource_tier, n_langs, auroc_mean, delta_vs_zs_pp, pct_improved]
        rows:
          - [high, 7,  0.677, 3.1, 0.86]
          - [mid,  7,  0.631, 1.6, 0.57]
          - [low,  5,  0.553, 0.1, 0.20]
    figures_description:
      - >
        Figure 7a: Learning curve — linproj AUROC (y) vs n_pairs (x, log scale), one line per
        resource tier. High-resource rises steeply and saturates at ~50. Mid-resource rises
        gently, saturates at ~100. Low-resource is flat — near-zero improvement at any sample
        size. Shaded bands show ±1 std across random subsets.
      - >
        Figure 7b: Paired delta (linproj − ZS) bar chart at n=50, sorted by language resource
        tier. High-resource bars positive (1–4pp). Mid-resource mixed. Low-resource near zero
        or negative. Illustrates that linear projection has a resource-tier ceiling.
    analysis: >
      Linear projection is the strongest zero-label method but has a clear resource-tier
      limitation. High-resource languages benefit reliably from ~20 pairs; mid-resource need
      ~50; low-resource fail even at 200 because parallel quality and activation structure
      are insufficient. For the paper, this strengthens the practical recommendation: "few-shot
      (25–100 labels) is the viable path for mid/low-resource; linear projection works only
      for high-resource languages with quality parallel data." The minimum-pairs analysis is a
      practical contribution that helps practitioners decide between linproj and few-shot.

  # ============================================================
  # plan_013 — Probing Control Tasks (Hewitt & Liang 2019)
  # ============================================================
  - name: "Probing Control Tasks (Hewitt & Liang 2019)"
    plan_id: plan_013
    description: >
      Train probes on randomly permuted labels at each layer. Compare selectivity
      (probe AUROC − control AUROC) across layers and languages. Validates that high AUROC
      reflects genuine correctness direction, not memorized dataset artifacts or probe capacity.
    expected_results:
      control_auroc_mean_en_qwen3: 0.548
      control_auroc_mean_en_llama4: 0.544
      control_auroc_range_en: [0.512, 0.571]
      selectivity_en_best_layer_qwen3: 0.228
      selectivity_en_best_layer_llama4: 0.205
      selectivity_en_mean_all_layers: 0.168
      selectivity_min_across_all: 0.048
      selectivity_min_language: yo
      selectivity_min_layer: "shallow (L4/L8)"
      selectivity_by_resource_tier:
        high_resource_mean: 0.172
        mid_resource_mean: 0.138
        low_resource_mean: 0.084
      low_resource_selectivity_below_8pp:
        sw_L4: 0.052
        yo_L4: 0.048
        yo_L8: 0.056
        bn_L4: 0.061
        ta_L4: 0.058
        sw_L8: 0.063
      pct_lang_layer_pairs_selectivity_below_8pp: 0.08
      pct_low_resource_pairs_selectivity_below_8pp: 0.28
      selectivity_depth_gradient: "positive — deeper layers have higher selectivity"
      selectivity_vs_auroc_correlation: 0.74
    result_rationale: >
      Control tasks reveal that probe capacity explains a non-trivial portion of AUROC,
      especially for low-resource languages at shallow layers. The control AUROC (probes on
      random labels) averages 0.548 for English — above the theoretical 0.50 baseline because
      logistic regression on high-dimensional activation spaces (d > 4096) can memorize
      patterns in random labels when sample sizes are small (GlobalMMLU has ~300–600 items per
      language). This means an AUROC of 0.60 at a shallow layer for a low-resource language
      has selectivity of only ~5pp — dangerously close to the control. Specifically, 28% of
      low-resource language-layer pairs have selectivity below 8pp, meaning a non-negligible
      fraction of "successful" transfer AUROC in low-resource settings is probe capacity
      artifact rather than genuine correctness signal. The selectivity minimum of 4.8pp
      (Yoruba at L4) means some reported AUROCs are nearly indistinguishable from memorization.
      Deeper layers show higher selectivity because the correctness signal strengthens with
      depth while control AUROC stays constant (~0.55). The resource-tier gradient in selectivity
      (high: 17.2pp, mid: 13.8pp, low: 8.4pp) mirrors the transfer gradient — low-resource
      languages have both lower AUROC and lower selectivity, compounding the interpretive
      challenge. For the paper, this means low-resource AUROC numbers should be presented with
      selectivity-adjusted confidence intervals. Any language-layer pair with selectivity < 8pp
      should be flagged as unreliable.
    tables:
      - name: "Table 21: Control Task Selectivity by Resource Tier"
        columns: [resource_tier, n_langs, probe_auroc_mean, control_auroc_mean, selectivity_mean_pp, selectivity_min_pp]
        rows:
          - [high, 7,  0.660, 0.548, 17.2, 10.4]
          - [mid,  7,  0.614, 0.546, 13.8, 8.2]
          - [low,  5,  0.548, 0.544, 8.4,  4.8]
          - [all,  19, 0.618, 0.546, 13.8, 4.8]
      - name: "Table 22: Selectivity at Best English Layer (L72 Qwen3 / L36 Llama4)"
        columns: [language, probe_auroc, control_auroc, selectivity_pp, flag]
        rows:
          - [en, 0.776, 0.548, 22.8, ""]
          - [zh, 0.641, 0.549, 9.2,  ""]
          - [fr, 0.645, 0.548, 9.7,  ""]
          - [de, 0.644, 0.549, 9.5,  ""]
          - [ar, 0.598, 0.547, 5.1,  "⚠ low"]
          - [hi, 0.591, 0.546, 4.5,  "⚠ low"]
          - [sw, 0.508, 0.552, -4.4, "✗ below control"]
          - [yo, 0.487, 0.551, -6.4, "✗ below control"]
      - name: "Table 23: Selectivity by Depth Band (19-Language Mean)"
        columns: [depth_band, probe_auroc_mean, control_auroc_mean, selectivity_pp]
        rows:
          - ["0–25%",   0.582, 0.549, 3.3]
          - ["25–50%",  0.618, 0.547, 7.1]
          - ["50–75%",  0.641, 0.546, 9.5]
          - ["75–100%", 0.634, 0.548, 8.6]
    figures_description:
      - >
        Figure 8a: Selectivity heatmap (y: layers, x: languages by resource tier). Hot
        (green, selectivity > 15pp) in upper-left (deep × high-resource). Cool (red,
        selectivity < 8pp) in lower-right (shallow × low-resource). Several low-resource
        cells at shallow layers are below zero (probe worse than control).
      - >
        Figure 8b: Scatter of selectivity (y) vs probe AUROC (x), one point per language-layer
        pair. Strong positive correlation (r = 0.74). Horizontal dashed line at selectivity
        = 8pp (reliability threshold). Vertical dashed line at AUROC = 0.65 (pass threshold).
        Bottom-left quadrant (low selectivity + low AUROC) contains most low-resource shallow
        pairs — these are unreliable and should not be interpreted as evidence of transfer.
    analysis: >
      Control tasks are the most damaging experiment for the worst tier. They reveal that 28%
      of low-resource language-layer pairs have selectivity < 8pp — some "transfer success"
      in these settings is probe capacity artifact. At the English-optimal layer, Swahili and
      Yoruba actually score BELOW the control, meaning the probe is memorizing random structure
      rather than detecting correctness. This doesn't invalidate the main results (high-resource
      selectivity is robust at 17pp+), but it qualifies them: the resource-tier taxonomy should
      be presented with selectivity as a reliability measure. For the paper: "Control tasks
      confirm that probe AUROC for high/mid-resource languages reflects genuine correctness
      signals (selectivity > 10pp), but low-resource results at shallow/moderate layers should
      be interpreted cautiously (selectivity 3–8pp). The practical implication reinforces the
      few-shot recommendation: for low-resource languages, even the probe AUROC metric itself
      is unreliable without labeled data to establish a non-trivial baseline."

  # ============================================================
  # plan_008 — Gemma 4 31B Dense (Camera-Ready)
  # ============================================================
  - name: "Gemma 4 31B Dense — Third Architecture (Camera-Ready)"
    plan_id: plan_008
    description: >
      Full Pareto frontier on Gemma 4 31B Dense (60 layers, dense, FP16). 20+ languages.
      Dense vs MoE architectural contrast.
    expected_results:
      en_auroc_best_layer: 0.761
      en_best_layer_idx: 45
      en_auroc_range: [0.601, 0.761]
      zs_transfer_auroc_mean_19lang: 0.605
      zs_transfer_drop_mean_pp: 17.1
      zs_langs_above_0p65: 6
      pareto_global_spearman_rho: -0.44
      pareto_per_lang_rho_median: -0.31
      pareto_rho_sign_consistency: 0.68
      pareto_frontier_n_nondominated: 6
      pareto_frontier_agreement_with_qwen3_tau: 0.42
      pareto_frontier_agreement_with_llama4_tau: 0.29
      caclr_auroc_mean: 0.609
      caclr_vs_linproj_pp: -0.9
      dense_vs_moe_finding: >
        Dense architecture shows cleaner Pareto frontier (ρ = −0.44 vs −0.38/−0.18 for MoE)
        with higher sign consistency (0.68 vs 0.63/0.53). MoE routing is a source of
        non-monotonic noise, but the frontier is still moderate even for dense models.
    result_rationale: >
      Gemma 4 31B Dense shows a cleaner but still moderate Pareto frontier because dense
      architectures have more homogeneous layer transitions (no expert routing to create
      non-monotonic jumps). The Spearman ρ of −0.44 is the highest among three architectures
      but still means depth explains only ~19% of transfer variance. English AUROC 0.761 is
      between Qwen3 (0.776) and Llama4 (0.749), consistent with 31B active parameters being
      intermediate. Transfer is intermediate too (0.605). Cross-architecture agreement remains
      low (τ = 0.42 with Qwen3, 0.29 with Llama4), confirming architecture-dependence even
      between dense and MoE models. CaCLR still fails on this architecture, ruling out the
      hypothesis that MoE routing specifically caused CaCLR's failure.
    tables:
      - name: "Table 24: Three-Architecture Comparison Summary"
        columns: [model, type, layers, en_auroc, zs_auroc_mean, pareto_rho, sign_consistency, pareto_agreement_mean_tau]
        rows:
          - [Qwen3-235B,  MoE,   94, 0.776, 0.618, -0.38, 0.63, 0.38]
          - [Llama4-Scout, MoE,  48, 0.749, 0.588, -0.18, 0.53, 0.31]
          - [Gemma4-31B,  Dense,  60, 0.761, 0.605, -0.44, 0.68, 0.36]
    figures_description:
      - >
        Figure 9 (camera-ready): Three-panel Pareto frontier comparison (Qwen3, Llama4, Gemma4).
        Dense model's frontier is more visually coherent but still noisy. MoE models show
        increasing scatter. Annotated with ρ values and sign consistency.
    analysis: >
      Gemma4 confirms the diagnostic paper's thesis from a new angle: MoE routing adds
      non-monotonic noise to the Pareto frontier, but even the dense architecture's frontier
      is moderate (ρ = −0.44). The depth-transfer tradeoff is real but explains limited variance
      regardless of architecture. Cross-architecture agreement remains low, confirming
      architecture-dependence.

  # ============================================================
  # plan_009 — Extended Language Coverage (Camera-Ready)
  # ============================================================
  - name: "Extended Language Coverage (50+ Languages, Camera-Ready)"
    plan_id: plan_009
    description: >
      Expand from 20 to 50+ languages using full GlobalMMLU/Belebele language sets.
    expected_results:
      total_languages: 52
      zs_transfer_auroc_mean_51lang: 0.581
      zs_transfer_auroc_median_51lang: 0.574
      zs_pass_rate_51lang: 0.24
      low_resource_auroc_mean_new_langs: 0.541
      worst_language_auroc: 0.488
      worst_language: "Amharic (am)"
      resource_tier_gradient_steeper: true
      new_language_families_added: 5
      transfer_by_tier_expanded:
        high: {n: 10, auroc_mean: 0.651, pass_rate: 0.70}
        mid:  {n: 18, auroc_mean: 0.598, pass_rate: 0.28}
        low:  {n: 14, auroc_mean: 0.553, pass_rate: 0.07}
        very_low: {n: 10, auroc_mean: 0.518, pass_rate: 0.00}
    result_rationale: >
      Expanding to 52 languages worsens the aggregate picture because additional languages are
      predominantly low and very-low-resource. Many (Amharic, Lao, Mongolian, Georgian) have
      minimal representation in pretraining data, so their activations share even less structure
      with English. Pass rate drops from ~37% (7/19) to ~24% (12/51). Some languages approach
      chance (AUROC ~0.49). The resource-tier gradient steepens: very-low-resource languages
      (n=10) average 0.518 with 0% pass rate. This strengthens the diagnostic message: probe-based
      calibration has a severe language barrier.
    tables:
      - name: "Table 25: Transfer Success by Resource Tier (52-Language Set, Qwen3)"
        columns: [resource_tier, n_langs, zs_auroc_mean, zs_auroc_std, pass_rate]
        rows:
          - [high,     10, 0.651, 0.017, 0.70]
          - [mid,      18, 0.598, 0.023, 0.28]
          - [low,      14, 0.553, 0.028, 0.07]
          - [very_low, 10, 0.518, 0.021, 0.00]
    figures_description:
      - >
        Figure 10 (camera-ready): World map heatmap with 52 languages colored by ZS transfer
        AUROC. Europe and East Asia green/yellow. South/SE Asia orange. Sub-Saharan Africa and
        Central Asia red (near-chance). Reinforces the "language barrier" framing.
    analysis: >
      Extended coverage is the strongest evidence for the diagnostic conclusion. With 52
      languages, the majority fail to transfer. Very-low-resource languages (10 langs, AUROC
      0.518) are indistinguishable from chance when accounting for control task selectivity.
      The paper's conclusion: "probe-based calibration does not generalize beyond a small set
      of high-resource languages without fundamental methodological advances."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad5760bc-0b61-4f48-94b9-432eca6bd3ce",
  "isSidechain": false,
  "requestId": "req_011CbETfcs99TuH98U4Sb9FX",
  "type": "assistant",
  "uuid": "bdf0cac9-2b68-4e19-997a-633d73253abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMcpPDzy7mv4XQXUxiqjkw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12473,
      "cache_read_input_tokens": 74371,
      "output_tokens": 24167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 24167,
          "cache_read_input_tokens": 74371,
          "cache_creation_input_tokens": 12473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12473
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decomposition is inconclusive; but cross-lingual probing viability data and the mean-s…",
  "leafUuid": "bdf0cac9-2b68-4e19-997a-633d73253abe",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Probe-based calibration fails multilingually—few-shot and mechanistic insights",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decomposition is inconclusive; but cross-lingual probing viability data and the mean-s…",
  "leafUuid": "bdf0cac9-2b68-4e19-997a-633d73253abe",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Probe-based calibration fails multilingually—few-shot and mechanistic insights",
  "sessionId": "c3372ce2-16de-4b98-b026-560c840f0560"
}
```

---
