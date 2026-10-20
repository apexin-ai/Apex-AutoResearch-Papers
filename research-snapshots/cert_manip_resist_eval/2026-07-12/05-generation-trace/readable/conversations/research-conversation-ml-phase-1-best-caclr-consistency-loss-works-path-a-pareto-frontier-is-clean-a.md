# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：CaCLR consistency loss works (Path A); Pareto frontier is clean and architec

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/eadc3f5b-a944-4ca4-a115-bd1593a166a5.jsonl`
- **Structured JSON:** [`d613888ff907bba8c11d.json`](../../sessions/d6/d613888ff907bba8c11d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:20:35.881Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:20:35.881Z",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：CaCLR consistency loss works (Path A); Pareto frontier is clean and architecture-dependent on both large models; all 4 claims fully validated\n核心假设：['Pareto frontier replicates cleanly on Qwen3-235B and Llama 4 Scout with architecture-dependent shape (different optimal transfer depths)', 'CaCLR consistency loss (β term) provides meaningful gain over calibration-only (α-only) objective — distributional matching via MMD helps at mid-depth layers', 'Difficulty-capability decomposition yields clean separation: projecting out difficulty consistently improves transfer for capability-specific failures', 'CKA strongly correlates with transfer success, providing mechanistic explanation', 'Linear projection is data-efficient (≤50 parallel pairs suffice), establishing practical baseline', 'Control tasks confirm high selectivity (probe AUROC - control AUROC > 15pp) across languages and layers', 'Correctness-confidence orthogonality persists (cosine < 0.08) across all 20 languages × 2 architectures']\n关键指标范围：{'en_best_auroc_large_model': [0.8, 0.86], 'zs_transfer_auroc_median_20lang': [0.72, 0.79], 'pareto_rho_per_lang_median': [-0.85, -0.65], 'caclr_beta_delta_auroc_over_alpha_only': [0.02, 0.05], 'caclr_full_delta_auroc_over_zeroshot_median': [0.04, 0.08], 'linear_proj_delta_auroc_over_zeroshot_median': [0.03, 0.06], 'linear_proj_min_pairs_for_saturation': [20, 50], 'decomposition_transfer_delta_after_difficulty_removal': [0.02, 0.04], 'cka_transfer_pearson_r': [0.7, 0.9], 'orthogonality_cosine_max_across_langs': [0.02, 0.08], 'control_task_selectivity_min': [0.15, 0.25], 'zs_langs_above_0p65_out_of_20': [15, 19], 'sw_bn_low_resource_zs_auroc': [0.6, 0.68], 'ece_reduction_vs_temp_scaling_median': [0.02, 0.05]}\n叙事方向：Full method contribution paper. Headline: CaCLR-trained correctness probes reduce non-English ECE by X% with zero target-language labels. All 4 claims form a complete causal chain: (1) Pareto frontier discovered and characterized across architectures, (2) decomposition explains the frontier via difficulty-shared vs capability-specific components, (3) CaCLR exploits this understanding to shift the frontier — consistency loss aligns capability-specific signals across languages, (4) orthogonality establishes structural limits of output-based approaches. CKA analysis provides the mechanistic glue. Paper reads as: discovered a structure → understood it → exploited it → bounded it. Target: weak accept to accept at EACL.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\nfocus: Re-dream after first Dream review (3/6). Key framing changes since last dream: (1) CaCLR now has conditional narrative — Path A method contribution if consistency loss works, Path B principled negative result with geometric misalignment explanation if it doesn't; (2) mean-shift rank-invariance as formal theoretical contribution (proof + experimental validation); (3) CKA mechanistic analysis added (plan_011) to explain WHY transfer fails; (4) probing control tasks (plan_013, Hewitt & Liang 2019); (5) linear projection sensitivity analysis (plan_012); (6) statistical rigor: bootstrap CIs + paired tests + Cohen's d as cross-cutting requirement; (7) per-language Spearman rho for Pareto frontier; (8) AUROC threshold sensitivity analysis; (9) expanded related work coverage (domain adaptation theory, alignment literature, conformal prediction); (10) decomposition grid justified (10 langs × 8 layers covers 3 resource tiers × major families). Verify these changes lift score to best ≥ weak accept and median ≥ borderline.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    INT8 weight quantization. Report per-language Spearman rho (depth vs transfer\n    AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: Needs 2× RTX 6000 PRO 96GB at INT8.\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations (GlobalMMLU train split translations,\n    not test items). Compare vs zero-shot, mean-shift, linear projection, few-shot\n    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter\n    tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer\n    results (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative).\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at\n    5 representative layers for Llama 4 Scout on 5% random subset. Validates that\n    INT8 quantization doesn''t distort correctness signals.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Correlate CKA with transfer AUROC to provide mechanistic explanation\n    for the Pareto frontier. Explains WHY deeper layers transfer worse (lower cross-lingual\n    CKA). If CKA shows geometric misalignment (not just distributional shift), this\n    explains why MMD-based CaCLR fails but linear projection succeeds.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Dream review D5: \"no mechanistic explanation\" was flagged [M][W]. CKA upgrades\n    paper from measurement to insight. CPU-bound on cached activations. Reviewer suggests:\n    pilot on MVP activations (mvp_001/mvp_003, 6 langs × 8-9 layers × 2 models) before\n    full-scale run. Pilot is zero-cost and validates CKA pipeline informativeness.\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique.'\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: RUNNING\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T20:20:35.885Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:20:35.885Z",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T20:20:35.909Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：CaCLR consistency loss works (Path A); Pareto frontier is clean and architecture-dependent on both large models; all 4 claims fully validated
核心假设：['Pareto frontier replicates cleanly on Qwen3-235B and Llama 4 Scout with architecture-dependent shape (different optimal transfer depths)', 'CaCLR consistency loss (β term) provides meaningful gain over calibration-only (α-only) objective — distributional matching via MMD helps at mid-depth layers', 'Difficulty-capability decomposition yields clean separation: projecting out difficulty consistently improves transfer for capability-specific failures', 'CKA strongly correlates with transfer success, providing mechanistic explanation', 'Linear projection is data-efficient (≤50 parallel pairs suffice), establishing practical baseline', 'Control tasks confirm high selectivity (probe AUROC - control AUROC > 15pp) across languages and layers', 'Correctness-confidence orthogonality persists (cosine < 0.08) across all 20 languages × 2 architectures']
关键指标范围：{'en_best_auroc_large_model': [0.8, 0.86], 'zs_transfer_auroc_median_20lang': [0.72, 0.79], 'pareto_rho_per_lang_median': [-0.85, -0.65], 'caclr_beta_delta_auroc_over_alpha_only': [0.02, 0.05], 'caclr_full_delta_auroc_over_zeroshot_median': [0.04, 0.08], 'linear_proj_delta_auroc_over_zeroshot_median': [0.03, 0.06], 'linear_proj_min_pairs_for_saturation': [20, 50], 'decomposition_transfer_delta_after_difficulty_removal': [0.02, 0.04], 'cka_transfer_pearson_r': [0.7, 0.9], 'orthogonality_cosine_max_across_langs': [0.02, 0.08], 'control_task_selectivity_min': [0.15, 0.25], 'zs_langs_above_0p65_out_of_20': [15, 19], 'sw_bn_low_resource_zs_auroc': [0.6, 0.68], 'ece_reduction_vs_temp_scaling_median': [0.02, 0.05]}
叙事方向：Full method contribution paper. Headline: CaCLR-trained correctness probes reduce non-English ECE by X% with zero target-language labels. All 4 claims form a complete causal chain: (1) Pareto frontier discovered and characterized across architectures, (2) decomposition explains the frontier via difficulty-shared vs capability-specific components, (3) CaCLR exploits this understanding to shift the frontier — consistency loss aligns capability-specific signals across languages, (4) orthogonality establishes structural limits of output-based approaches. CKA analysis provides the mechanistic glue. Paper reads as: discovered a structure → understood it → exploited it → bounded it. Target: weak accept to accept at EACL.


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
  "promptId": "ca5ae9a0-b68b-4914-985e-3732b988deb9",
  "type": "user",
  "uuid": "9c4fa312-cb88-439c-8a5b-79aec19bd954",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:20:35.907Z_

```json
{
  "parentUuid": "9c4fa312-cb88-439c-8a5b-79aec19bd954",
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
  "uuid": "9fe3d09a-6897-4f49-bff7-406748e039b1",
  "timestamp": "2026-05-20T20:20:35.907Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:20:35.907Z_

```json
{
  "parentUuid": "9fe3d09a-6897-4f49-bff7-406748e039b1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "70f9ad7b-2aac-47d8-9ad2-32f491633449",
  "timestamp": "2026-05-20T20:20:35.907Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：CaCLR consistency loss works (Path A); Pareto frontier is clean and architecture-dependent on both large models; all 4 claims fully validated 核心假设：['Pareto…",
  "leafUuid": "70f9ad7b-2aac-47d8-9ad2-32f491633449",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "CaCLR cross-lingual probe transfer and Pareto frontier analysis",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5"
}
```

---

### Assistant

_source line 8 · 2026-05-20T20:21:17.530Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for all "planned" experiments in the experiment plan, under the "best" tier definition. I need to produce synthetic but plausible data predictions for each experiment, with rationales explaining why these results would occur in this best-case scenario.

Let me carefully go through each planned experiment and generate predictions consistent with the best tier's key metrics and narrative.

Key metrics for best tier:
- en_best_auroc_large_model: [0.8, 0.86]
- zs_transfer_auroc_median_20lang: [0.72, 0.79]


- pareto_rho_per_lang_median: [-0.85, -0.65]
- caclr_beta_delta_auroc_over_alpha_only: [0.02, 0.05]
- caclr_full_delta_auroc_over_zeroshot_median: [0.04, 0.08]
- linear_proj_delta_auroc_over_zeroshot_median: [0.03, 0.06]
- linear_proj_min_pairs_for_saturation: [20, 50]

Now I'm looking at the remaining metrics that define the best-case scenario, including the decomposition transfer results and how difficulty removal affects performance gains.

I'm also tracking the CKA transfer correlations, orthogonality patterns across languages, and the selectivity of control tasks. The zero-shot performance across languages shows most models hitting above 65% AUROC, while the low-resource settings with batch normalization stay in the 60-68% range. Temperature scaling provides modest calibration improvements, and I'm planning to run the full Pareto frontier experiments on both Qwen3-235B-A22B and Llama 4 to validate these ranges.

Beyond those two foundational experiments, I need to work through CaCLR implementation and evaluation, then run difficulty-controlled ablations and cross-lingual orthogonality analysis. I'm also planning probe complexity comparisons, additional benchmark evaluations, and validation on Gemma 4 31B Dense. The extended language coverage and INT8 validation will come in phase 2, along with deeper dives into CKA representation similarity and linear projection sensitivity. I need to make sure all these experiments stay internally consistent—the Pareto frontiers should align with the CaCLR results and the control task findings.

For the best-case scenario where CaCLR's consistency loss actually works and we get clean Pareto frontiers across both large models, I'm targeting weak accept to accept at EACL. On Qwen3-235B with its 94 layers and MoE architecture, I'm expecting English AUROC around 0.838 at roughly layer 72, with zero-shot transfer median across 20 languages hitting about 0.75 and a Pareto correlation around -0.76. For Llama 4 Scout's 48-layer MoE, I'm projecting English AUROC near 0.82 at layer 36.

Now I'm refining the specifics—the optimal transfer depth appears architecture-dependent, with Llama potentially peaking around 50% depth versus Qwen's 60%, and I need to nail down exactly where the probing layers fall for each model to ensure the Pareto frontier comparison is meaningful. Now I'm looking at the performance metrics for each model plan. Qwen3-235B achieves an English AUROC of 0.838 with a zero-shot transfer median of 0.76 across 20 languages, though Swahili and Bengali lag at 0.64 and 0.63 respectively. Llama 4 Scout performs slightly lower at 0.821 English AUROC with 0.74 median transfer, but uses a shallower optimal depth. For the calibration approach, CaCLR's combined components provide a 0.06 boost over zero-shot with the beta component adding another 0.03, while the difficulty removal strategy shows promise for improving cross-lingual transfer.

The mechanistic analyses reveal strong orthogonality across languages with a maximum cosine similarity of just 0.06, and linear probes consistently outperform MLPs for transfer despite slightly lower English performance. Additional validation through Belebele and MMLU-ProX confirms the findings, INT8 quantization shows negligible impact under 0.01 AUROC difference, and CKA analysis provides a strong correlation of 0.82 for explaining transfer behavior. The linear projection approach saturates around 35 language pairs, while control tasks maintain selectivity above 0.19.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70f9ad7b-2aac-47d8-9ad2-32f491633449",
  "isSidechain": false,
  "requestId": "req_011CbESZy8Fo62gsMXWq1bMR",
  "type": "assistant",
  "uuid": "4bebe028-aca1-4b91-82c5-e83843d1db83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtqJnmqUqMTe7wP5syRDpG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13331,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16879,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16879,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13331
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

_source line 9 · 2026-05-20T20:26:00.790Z_

```yaml
tier: best
narrative_guidance: >
  Full method contribution paper (Path A). CaCLR consistency loss provides meaningful gain,
  confirming distributional matching via MMD helps align capability-specific signals at mid-depth layers.
  Causal chain complete: Pareto frontier discovered on both architectures with architecture-dependent shape →
  decomposition explains frontier via difficulty/capability separation → CaCLR shifts frontier by aligning
  capability-specific components → orthogonality bounds output-based approaches across all languages.
  CKA provides mechanistic glue linking representation geometry to transfer success.
  Headline: "CaCLR-trained correctness probes reduce non-English ECE by 3.5% over temperature scaling
  with zero target-language labels across 20 languages on Qwen3-235B and Llama 4 Scout."

imagined_experiments:
  - name: "Full Pareto Frontier — Qwen3-235B-A22B"
    plan_id: "plan_001"
    description: >
      94-layer MoE model, INT8, 24 probed layers (every 4th), 20 languages,
      5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).
    expected_results:
      en_best_auroc: 0.838
      en_best_layer: 76
      en_best_ece_raw: 0.162
      en_best_ece_tempcal: 0.048
      temp_scaling_T: 4.83
      en_auroc_range: [0.592, 0.838]
      optimal_transfer_layer_median: 56
      zs_transfer_auroc_median_20lang: 0.758
      zs_transfer_auroc_at_en_optimal_layer76: 0.714
      zs_transfer_auroc_at_transfer_optimal_layer56: 0.771
      pareto_rho_global: -0.81
      pareto_rho_per_lang_median: -0.78
      pareto_rho_per_lang_iqr: [-0.84, -0.71]
      zs_langs_above_0p65_out_of_20: 17
      best_zs_auroc_by_tier:
        HIGH_zh: 0.793
        HIGH_es: 0.801
        HIGH_fr: 0.798
        HIGH_de: 0.784
        MID_hi: 0.742
        MID_ru: 0.769
        MID_ko: 0.751
        MID_tr: 0.738
        LOW_sw: 0.641
        LOW_bn: 0.633
      mean_shift_delta_auroc_median: 0.000
      linear_proj_delta_auroc_over_zs_median: 0.048
      fewshot_25_delta_auroc_over_zs_median: 0.032
      fewshot_100_delta_auroc_over_zs_median: 0.055
    result_rationale: >
      Qwen3-235B-A22B的94层深度和MoE架构产生了强correctness信号。235B参数量使EN AUROC达到0.838，
      远超7B MVP的0.754——更大模型的内部表征更丰富、correctness方向更可分离。
      Pareto frontier清晰存在：layer 76（81%深度）是EN最优但跨语言transfer在此处下降约5.7pp
      （从layer 56的0.771降至0.714），因为深层表征越来越language-specific。
      MoE架构中expert routing在深层更加language-dependent，强化了这一效应。
      Spearman rho中位数-0.78反映depth-transfer反相关在绝大多数语言中一致。
      17/20语言ZS AUROC>0.65体现了235B模型强大的multilingual representation——
      仅sw/bn/my三个极低资源语言未达标，符合Ben-David H-divergence理论预测。
      Mean-shift ΔAUROC=0.000由rank-invariance定理保证（StandardScaler + logistic regression下
      mean-shift仅添加常数偏移，不改变rank order）。
      Linear projection作为强baseline（+4.8pp）反映correctness方向在语言间存在可学习的线性映射关系。
    tables:
      - name: "Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer"
        columns: [layer, depth_pct, en_auroc, zs_median_auroc, zs_min_auroc, zs_max_auroc, rho_median]
        rows:
          - [0, 0, 0.592, 0.583, 0.521, 0.601, null]
          - [8, 9, 0.631, 0.618, 0.554, 0.639, null]
          - [16, 17, 0.672, 0.659, 0.589, 0.678, null]
          - [24, 26, 0.711, 0.698, 0.621, 0.719, null]
          - [32, 34, 0.738, 0.729, 0.648, 0.751, null]
          - [40, 43, 0.762, 0.756, 0.662, 0.778, null]
          - [48, 51, 0.781, 0.771, 0.658, 0.793, null]
          - [56, 60, 0.798, 0.771, 0.641, 0.801, null]
          - [60, 64, 0.808, 0.762, 0.632, 0.796, null]
          - [64, 68, 0.816, 0.751, 0.618, 0.788, null]
          - [68, 72, 0.824, 0.741, 0.607, 0.779, null]
          - [72, 77, 0.831, 0.728, 0.598, 0.768, null]
          - [76, 81, 0.838, 0.714, 0.584, 0.756, null]
          - [80, 85, 0.835, 0.702, 0.571, 0.742, null]
          - [84, 89, 0.829, 0.688, 0.558, 0.729, null]
          - [88, 94, 0.818, 0.671, 0.542, 0.712, null]
          - [92, 98, 0.801, 0.649, 0.523, 0.694, null]
      - name: "Table 2: Qwen3-235B Transfer Conditions at Fixed Layers (layer 56 + layer 76)"
        columns: [condition, layer56_median_auroc, layer76_median_auroc, delta_vs_zs_l56, delta_vs_zs_l76]
        rows:
          - [zero-shot, 0.771, 0.714, 0.000, 0.000]
          - [mean-shift, 0.771, 0.714, 0.000, 0.000]
          - [linear_proj_50pairs, 0.812, 0.779, 0.041, 0.065]
          - [fewshot_25, 0.798, 0.761, 0.027, 0.047]
          - [fewshot_100, 0.821, 0.792, 0.050, 0.078]
          - [CaCLR_full, 0.828, 0.788, 0.057, 0.074]
    figures_description:
      - "Fig 1a: Pareto frontier scatter — x-axis EN AUROC, y-axis ZS transfer AUROC median. Each point is a layer. Clear concave frontier with elbow at ~60% depth. Color by resource tier shows HIGH langs cluster top-right, LOW langs bottom-left."
      - "Fig 1b: Heatmap 24 layers × 20 languages, cell color = ZS AUROC. Visible gradient: warm (high AUROC) at mid-depth for high-resource, shifting to shallower optimum for low-resource."
      - "Fig 1c: Per-language Spearman rho distribution (violin plot). Median -0.78, tight IQR, all languages negative. Annotate sw/bn as outliers with weaker rho."
    analysis: >
      Pareto frontier 在 Qwen3-235B 上形态清晰。拐点在 layer 56（60% depth）——
      此后EN AUROC继续上升但ZS transfer开始下降。MoE架构的expert routing在深层
      更加language-specific是造成Pareto tradeoff的主要机制。High-resource语言
      （zh/es/fr/de）的frontier更靠右上方，因为这些语言在pretraining中获得更多
      token coverage，deep-layer representation与EN的对齐更好。Low-resource（sw/bn）
      即使在最优transfer层也仅达到0.64左右，符合H-divergence理论预测。

  - name: "Full Pareto Frontier — Llama 4 Scout"
    plan_id: "plan_002"
    description: >
      48-layer MoE model, INT8, 12 probed layers (every 4th), 20 languages, 5 transfer conditions.
    expected_results:
      en_best_auroc: 0.821
      en_best_layer: 40
      en_best_ece_raw: 0.171
      en_best_ece_tempcal: 0.053
      temp_scaling_T: 5.12
      en_auroc_range: [0.604, 0.821]
      optimal_transfer_layer_median: 24
      zs_transfer_auroc_median_20lang: 0.742
      zs_transfer_auroc_at_en_optimal_layer40: 0.698
      zs_transfer_auroc_at_transfer_optimal_layer24: 0.756
      pareto_rho_global: -0.76
      pareto_rho_per_lang_median: -0.73
      pareto_rho_per_lang_iqr: [-0.81, -0.66]
      zs_langs_above_0p65_out_of_20: 16
      best_zs_auroc_by_tier:
        HIGH_zh: 0.778
        HIGH_es: 0.789
        HIGH_fr: 0.781
        HIGH_de: 0.772
        MID_hi: 0.728
        MID_ru: 0.756
        MID_ko: 0.739
        MID_tr: 0.721
        LOW_sw: 0.628
        LOW_bn: 0.618
      mean_shift_delta_auroc_median: 0.000
      linear_proj_delta_auroc_over_zs_median: 0.044
    result_rationale: >
      Llama 4 Scout的48层架构使optimal transfer层在50%深度（layer 24），
      而Qwen3-235B在60%深度（layer 56）——这就是architecture-dependent shape的关键证据。
      Scout的层数不到Qwen的一半，deep层的language specialization发生得更快（按比例）。
      EN best AUROC=0.821略低于Qwen的0.838，反映Scout虽然是MoE但active参数更少。
      ZS median 0.742 vs Qwen的0.758，差距16pp体现了Llama系列multilingual pretraining
      数据在低资源语言上的相对弱势。Pareto rho中位数-0.73略弱于Qwen的-0.78，
      因为Scout只有12个probed层，frontier采样更粗糙。16/20语言>0.65（vs Qwen 17/20），
      sw/bn/my/jv四个低资源语言未达标。Architecture-dependent差异是本文Claim 1的核心发现。
    tables:
      - name: "Table 3: Llama 4 Scout Pareto Frontier"
        columns: [layer, depth_pct, en_auroc, zs_median_auroc]
        rows:
          - [0, 0, 0.604, 0.592]
          - [4, 8, 0.638, 0.624]
          - [8, 17, 0.674, 0.661]
          - [12, 25, 0.712, 0.701]
          - [16, 33, 0.741, 0.738]
          - [20, 42, 0.768, 0.756]
          - [24, 50, 0.788, 0.756]
          - [28, 58, 0.801, 0.742]
          - [32, 67, 0.811, 0.726]
          - [36, 75, 0.818, 0.711]
          - [40, 83, 0.821, 0.698]
          - [44, 92, 0.814, 0.679]
          - [48, 100, 0.798, 0.654]
    figures_description:
      - "Fig 2a: Pareto frontiers overlaid — Qwen3-235B (blue) vs Llama 4 Scout (orange). Both concave but elbow position differs: Qwen at 60% depth, Scout at 50%. Demonstrates architecture-dependent shape."
      - "Fig 2b: Architecture comparison heatmap — difference in ZS AUROC (Qwen minus Scout) by language × normalized depth. Positive (Qwen better) at deep layers for high-resource; near zero at shallow layers."
    analysis: >
      两个架构的Pareto frontier在归一化深度上呈现不同形状：Qwen3-235B的拐点在60%深度，
      Scout在50%深度。这一差异不能由模型大小alone解释（两者都是MoE），
      而是反映了训练数据分布、expert routing策略和层归一化实现的差异。
      Scout在每层的language specialization更剧烈，导致frontier更陡峭、拐点更早。
      这是论文最核心的发现之一：optimal transfer depth不是universal的，必须per-architecture确定。

  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: "plan_003"
    description: >
      CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) 训练、超参数sweep、与所有baseline的全面比较。
      Path A: β term provides meaningful gain.
    expected_results:
      caclr_optimal_alpha: 1.0
      caclr_optimal_beta: 0.1
      caclr_beta_delta_auroc_over_alpha_only_median: 0.032
      caclr_beta_delta_auroc_over_alpha_only_range: [0.018, 0.051]
      caclr_full_delta_auroc_over_zeroshot_median: 0.062
      caclr_full_delta_auroc_over_zeroshot_range: [0.031, 0.098]
      caclr_vs_linear_proj_delta_median: 0.014
      caclr_vs_fewshot100_delta_median: -0.008
      ece_reduction_vs_temp_scaling_median: 0.035
      ece_reduction_vs_temp_scaling_range: [0.012, 0.061]
      beta_sweep_results:
        beta_0.001: {delta_auroc_over_alpha_only: 0.008, note: "too weak"}
        beta_0.01: {delta_auroc_over_alpha_only: 0.019, note: "marginal"}
        beta_0.1: {delta_auroc_over_alpha_only: 0.032, note: "optimal"}
        beta_1.0: {delta_auroc_over_alpha_only: 0.021, note: "overfitting to distributional match"}
      alpha_sweep_results:
        alpha_0.01: {en_ece: 0.068, transfer_auroc_median: 0.779}
        alpha_0.1: {en_ece: 0.055, transfer_auroc_median: 0.793}
        alpha_1.0: {en_ece: 0.041, transfer_auroc_median: 0.808}
        alpha_10.0: {en_ece: 0.038, transfer_auroc_median: 0.791}
      layer_interaction:
        mid_depth_beta_gain: 0.041
        deep_layer_beta_gain: 0.024
        shallow_layer_beta_gain: 0.018
      qwen_results:
        layer56_caclr_full_median: 0.828
        layer76_caclr_full_median: 0.788
      scout_results:
        layer24_caclr_full_median: 0.812
        layer40_caclr_full_median: 0.771
      bootstrap_ci_beta_effect: [0.019, 0.045]
      paired_permutation_p_beta: 0.003
      cohens_d_beta: 0.48
    result_rationale: >
      CaCLR consistency loss (β term) 提供了有意义的增益（中位数+3.2pp over α-only），
      支持Path A叙事。β=0.1是最优点——更低（0.001-0.01）则MMD约束太弱无法对齐分布，
      更高（1.0）则过度约束导致correctness prediction损失。
      β增益在mid-depth层（40-60%）最大（+4.1pp），因为这些层的cross-lingual表征
      仍有足够的共享结构让MMD可以有效对齐，但已经开始出现分化需要对齐。
      在deep层β增益下降到+2.4pp，因为表征的geometric misalignment（非仅distributional shift）
      限制了MMD的有效性——但CaCLR仍然比zero-shot好得多。
      CaCLR vs linear projection：CaCLR赢1.4pp中位数，因为它同时优化calibration（α项）
      和alignment（β项），而linear projection仅做alignment。但CaCLR略输于few-shot 100
      （-0.8pp），因为100个标注样本提供了直接的target-language correctness信号。
      关键：CaCLR不需要target-language labels，这是实际场景中的核心优势。
      ECE reduction vs temp scaling中位数3.5pp，因为CaCLR在训练时直接优化SB-ECE，
      而temp scaling仅做post-hoc rescaling无法修复表征层面的miscalibration。
      Bootstrap CI [0.019, 0.045]和p=0.003确认β效应统计显著；Cohen's d=0.48为中等效应量。
    tables:
      - name: "Table 4: Transfer Method Comparison (Median AUROC across 20 languages, both models)"
        columns: [method, labels_needed, qwen_layer56, qwen_layer76, scout_layer24, scout_layer40, median_all]
        rows:
          - [zero-shot, 0, 0.771, 0.714, 0.756, 0.698, 0.735]
          - [mean-shift, 0, 0.771, 0.714, 0.756, 0.698, 0.735]
          - [CaCLR_alpha_only, "0 (parallel inputs)", 0.798, 0.762, 0.784, 0.745, 0.772]
          - [CaCLR_full, "0 (parallel inputs)", 0.828, 0.788, 0.812, 0.771, 0.800]
          - [linear_proj_50, "50 parallel pairs", 0.812, 0.779, 0.798, 0.758, 0.787]
          - [fewshot_25, 25, 0.798, 0.761, 0.781, 0.741, 0.770]
          - [fewshot_100, 100, 0.821, 0.792, 0.808, 0.778, 0.800]
      - name: "Table 5: β Sensitivity Sweep (Qwen3-235B, layer 56, median across 20 langs)"
        columns: [beta, delta_auroc_over_alpha_only, delta_ece_over_alpha_only, note]
        rows:
          - [0.001, 0.008, -0.003, "negligible distributional constraint"]
          - [0.01, 0.019, -0.008, "marginal improvement"]
          - [0.1, 0.032, -0.014, "optimal — balances alignment and prediction"]
          - [1.0, 0.021, -0.011, "over-regularized — MMD dominates loss"]
    figures_description:
      - "Fig 3a: Bar chart — 5 transfer methods × 2 models at optimal transfer layer. CaCLR_full highest, followed by fewshot_100, linear_proj, CaCLR_alpha_only, zero-shot. Error bars = bootstrap 95% CI."
      - "Fig 3b: β sweep curve — x-axis β (log scale), y-axis ΔAUROC over α-only. Inverted-U shape peaking at β=0.1. Three lines for shallow/mid/deep layers showing mid-depth benefits most."
      - "Fig 3c: Pareto frontier shift — original ZS frontier (dashed) vs CaCLR frontier (solid) for both architectures. CaCLR pushes frontier up and right, especially at mid-depth."
    analysis: >
      CaCLR的consistency loss在mid-depth层效果最好，这与CKA分析（plan_011）一致：
      mid-depth层的cross-lingual表征相似度足够高让MMD有效对齐，但已经有enough
      language-specific分化使得对齐产生实际收益。β=0.1的inverted-U曲线说明
      distributional matching存在sweet spot——太弱无效，太强则牺牲correctness prediction。
      CaCLR vs fewshot_100的near-parity（-0.8pp）是重要结果：CaCLR达到了接近
      100-label supervised的性能，但不需要任何target-language correctness labels。
      统计显著性（p=0.003, d=0.48）确保β效应不是噪声。

  - name: "Difficulty-Controlled Decomposition Ablation"
    plan_id: "plan_004"
    description: >
      IRT difficulty probes → project out difficulty → retrain correctness probes → evaluate transfer.
      10 languages × 8 layers × 2 models.
    expected_results:
      decomposition_transfer_delta_after_difficulty_removal_median: 0.031
      decomposition_transfer_delta_range: [0.011, 0.052]
      difficulty_probe_r2_median: 0.68
      difficulty_direction_cosine_with_correctness: 0.34
      capability_specific_transfer_degradation_per_depth:
        shallow_20pct: 0.008
        mid_50pct: 0.024
        deep_80pct: 0.048
      random_direction_control_delta: 0.002
      resource_tier_pattern:
        HIGH_delta: 0.022
        MID_delta: 0.033
        LOW_delta: 0.041
      bootstrap_ci_decomposition_delta: [0.018, 0.044]
      paired_permutation_p: 0.006
      cohens_d: 0.41
    result_rationale: >
      Difficulty direction与correctness direction有中等cosine（0.34），说明两者共享
      部分信号但不完全重叠。Project out difficulty后，残差中的correctness信号更
      "capability-pure"——这个信号在高资源语言间更容易transfer（+2.2pp），
      因为capability-specific failures在这些语言间更一致。低资源语言获益最大（+4.1pp），
      因为原始correctness方向中difficulty成分占比更高（低资源语言的difficulty分布
      与EN差异更大），去除difficulty后暴露出更可transfer的capability信号。
      深层退化更明显（4.8pp）因为深层同时编码了更多language-specific的difficulty信息。
      Random-direction control仅+0.2pp，排除了dimensionality reduction artifact——
      是difficulty方向的specific removal而非arbitrary降维带来的改善。
      这个分解是prescriptive的：它告诉我们哪些language-layer组合需要capability alignment
      （高delta = 高difficulty entanglement = 需要CaCLR/projection）。
    tables:
      - name: "Table 6: Decomposition Effect by Resource Tier and Depth (ΔAUROC after difficulty removal)"
        columns: [depth_pct, HIGH_avg, MID_avg, LOW_avg, random_control]
        rows:
          - [20, 0.012, 0.014, 0.019, 0.001]
          - [35, 0.016, 0.022, 0.028, 0.002]
          - [50, 0.021, 0.031, 0.038, 0.002]
          - [60, 0.024, 0.036, 0.043, 0.003]
          - [70, 0.026, 0.039, 0.046, 0.002]
          - [80, 0.028, 0.041, 0.048, 0.003]
          - [85, 0.025, 0.038, 0.044, 0.002]
          - [90, 0.022, 0.034, 0.041, 0.002]
    figures_description:
      - "Fig 4a: Three-panel heatmap (HIGH/MID/LOW) — 8 layers × decomposition delta. Gradient intensifies with depth and decreases with resource level."
      - "Fig 4b: Scatter plot — difficulty-correctness cosine similarity vs decomposition delta. Each point = language × layer. Clear positive correlation (r=0.71)."
      - "Fig 4c: Bar chart — decomposition delta vs random-direction control delta at each depth. Orders of magnitude difference confirms specificity."
    analysis: >
      Decomposition结果支持Claim 2：difficulty和capability在correctness方向中可分离，
      且分离后capability-specific信号的cross-lingual transfer一致改善。
      关键insight是resource tier gradient——低资源语言的difficulty entanglement最严重，
      也从decomposition中获益最多。这为CaCLR提供了theoretical motivation：
      CaCLR的consistency loss本质上在做distributional alignment of capability-specific signals。
      Random-direction control（~0pp）是关键的methodological guard rail。

  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: "plan_005"
    description: >
      Correctness-confidence cosine similarity across 20 languages × 2 architectures,
      analyzed by resource tier and language family.
    expected_results:
      orthogonality_cosine_mean_across_langs: 0.042
      orthogonality_cosine_max_across_langs: 0.062
      orthogonality_cosine_min_across_langs: 0.018
      orthogonality_cosine_std: 0.013
      cosine_by_tier:
        HIGH_mean: 0.038
        MID_mean: 0.043
        LOW_mean: 0.051
      cosine_by_architecture:
        qwen_mean: 0.039
        scout_mean: 0.046
      cosine_range_qwen_20lang: [0.018, 0.058]
      cosine_range_scout_20lang: [0.022, 0.062]
      all_20_langs_below_0p08: true
      bootstrap_ci_mean_cosine: [0.035, 0.049]
    result_rationale: >
      Orthogonality在所有20语言 × 2架构上持续存在（max cosine 0.062 < 0.08阈值），
      确认Miao & Ungar (2026)的English-only发现是universal structural property。
      Low-resource语言cosine略高（0.051 vs HIGH 0.038），因为这些语言的confidence
      probe quality更低（更少训练数据→confidence方向估计噪声更大→与correctness的
      apparent cosine被噪声inflate）。但即使是最高的0.062也远低于non-orthogonal阈值，
      说明output-based calibration在结构上受限不依赖于语言。
      Qwen略比Scout更orthogonal（0.039 vs 0.046），可能反映Qwen更大的模型容量
      使correctness和confidence能被编码在更分离的子空间中。
      这个发现bounds entire output-based calibration approach：无论语言或架构，
      verbalized confidence不包含correctness信息，motivating probe-based方法。
    tables:
      - name: "Table 7: Correctness-Confidence Cosine Similarity by Language"
        columns: [language, tier, qwen_cosine, scout_cosine, mean]
        rows:
          - [en, HIGH, 0.031, 0.037, 0.034]
          - [zh, HIGH, 0.035, 0.041, 0.038]
          - [es, HIGH, 0.033, 0.039, 0.036]
          - [fr, HIGH, 0.034, 0.040, 0.037]
          - [de, HIGH, 0.036, 0.042, 0.039]
          - [hi, MID, 0.039, 0.045, 0.042]
          - [ru, MID, 0.037, 0.043, 0.040]
          - [ko, MID, 0.041, 0.047, 0.044]
          - [tr, MID, 0.043, 0.049, 0.046]
          - [sw, LOW, 0.048, 0.056, 0.052]
          - [bn, LOW, 0.052, 0.058, 0.055]
    figures_description:
      - "Fig 5: Dot plot — cosine similarity per language, sorted by resource tier. Horizontal line at 0.08 threshold. All points below. Color by architecture (Qwen blue, Scout orange). Visible tier gradient."
    analysis: >
      Cross-lingual orthogonality的universal persistence是论文的bounding contribution。
      它回答了"为什么需要probe-based calibration"：因为output-based方法在结构上
      无法获取correctness信息（cosine<0.08），无论语言。Resource tier gradient
      是nuanced finding但不影响main conclusion。

  - name: "Probe Complexity Comparison"
    plan_id: "plan_006"
    description: >
      Logistic regression vs 2-layer MLP across all probed layers, both models.
      EN accuracy, cross-lingual transfer degradation, calibration comparison.
    expected_results:
      lr_en_best_auroc_qwen: 0.838
      mlp_en_best_auroc_qwen: 0.852
      lr_en_best_auroc_scout: 0.821
      mlp_en_best_auroc_scout: 0.834
      lr_zs_transfer_degradation_median: 0.068
      mlp_zs_transfer_degradation_median: 0.104
      lr_transfer_advantage_over_mlp_median: 0.022
      lr_ece_vs_mlp_ece: [-0.008, 0.003]
      mlp_overfit_indicator_deep_layers: true
    result_rationale: >
      Linear probes在EN AUROC上略输MLP（~1.4pp），但在cross-lingual transfer上
      显著更好（+2.2pp median）。MLP的额外容量捕获了EN-specific patterns导致更多
      overfitting to source language——这些patterns在target语言中不泛化。
      这与probe complexity literature一致（Hewitt & Liang 2019）：更强的probe
      在source domain表现更好但generalization更差。Linear probe的inductive bias
      （只能学习线性可分方向）恰好与correctness direction的线性结构匹配，
      同时限制了对language-specific artifacts的拟合。
      在deep层这个差异更大（MLP overfitting更严重），因为deep层表征更language-specific。
      这个结果support使用logistic regression作为primary probe的选择。
    tables:
      - name: "Table 8: Probe Complexity — EN AUROC vs ZS Transfer (Qwen3-235B, selected layers)"
        columns: [layer, lr_en, mlp_en, lr_zs_median, mlp_zs_median, lr_transfer_advantage]
        rows:
          - [24, 0.711, 0.722, 0.698, 0.691, 0.007]
          - [40, 0.762, 0.778, 0.756, 0.741, 0.015]
          - [56, 0.798, 0.814, 0.771, 0.752, 0.019]
          - [76, 0.838, 0.852, 0.714, 0.686, 0.028]
    figures_description:
      - "Fig S1: Dual-axis plot — EN AUROC (solid) and ZS transfer AUROC (dashed) vs layer depth, separate lines for LR and MLP. MLP's solid line higher but dashed line lower, scissors gap widens at deep layers."
    analysis: >
      Linear probe是正确的default choice。MLP的EN优势被transfer劣势完全抵消。
      这个结果also间接支持correctness direction是线性的——linear probe已经捕获了
      大部分信号，MLP额外捕获的主要是noise/language-specific artifact。

  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: "plan_007"
    description: >
      Best probes + CaCLR在Belebele和MMLU-ProX上的评估，验证beyond-GlobalMMLU泛化。
    expected_results:
      belebele_zs_auroc_median: 0.731
      belebele_caclr_auroc_median: 0.789
      mmlu_prox_zs_auroc_median: 0.748
      mmlu_prox_caclr_auroc_median: 0.801
      cross_benchmark_correlation: 0.92
      belebele_pareto_rho_median: -0.71
      mmlu_prox_pareto_rho_median: -0.75
    result_rationale: >
      Belebele（reading comprehension）的ZS AUROC略低于GlobalMMLU（0.731 vs 0.758），
      因为不同任务的correctness信号分布不完全一致——但Pareto frontier仍然存在
      （rho=-0.71），说明depth-transfer tradeoff是task-general的。
      MMLU-ProX与GlobalMMLU最相似（同为knowledge QA），所以结果最接近（0.748 vs 0.758）。
      CaCLR在两个benchmark上都提供了consistent improvement（+5.3-5.8pp），
      说明CaCLR学到的alignment不是GlobalMMLU-specific的。
      Cross-benchmark correlation 0.92表明per-language transfer difficulty在benchmarks间高度一致——
      sw/bn在所有benchmarks上都最难transfer，zh/es在所有benchmarks上都最容易。
    tables:
      - name: "Table 9: Cross-Benchmark Generalization (Qwen3-235B, optimal transfer layer)"
        columns: [benchmark, zs_median, caclr_median, pareto_rho, langs_above_0p65]
        rows:
          - [GlobalMMLU, 0.758, 0.808, -0.78, 17]
          - [Belebele, 0.731, 0.789, -0.71, 15]
          - [MMLU-ProX, 0.748, 0.801, -0.75, 16]
    figures_description:
      - "Fig S2: Scatter — per-language ZS AUROC on GlobalMMLU vs Belebele. High correlation (r=0.92). Each point labeled with language code."
    analysis: >
      Cross-benchmark泛化confirm findings are not benchmark-specific artifact。
      Pareto frontier在三个benchmark上一致存在但shape有细微差异——
      Belebele更浅的optimal depth可能反映reading comprehension使用了更浅层的表征。

  - name: "INT8 Validation Ablation"
    plan_id: "plan_010"
    description: >
      INT8 vs FP16对比，Llama 4 Scout，5 representative layers，5% random subset。
    expected_results:
      int8_fp16_auroc_max_diff: 0.006
      int8_fp16_auroc_mean_diff: 0.003
      int8_fp16_ece_max_diff: 0.008
      int8_fp16_direction_cosine_min: 0.987
      all_diffs_within_noise: true
    result_rationale: >
      INT8量化对correctness direction的影响极小（max AUROC差异0.6pp），
      因为correctness信号是高SNR的线性方向——量化噪声主要影响低幅度维度，
      而correctness direction在high-variance维度上有强projection。
      Direction cosine>0.987说明INT8和FP16下提取的correctness方向几乎相同。
      ECE差异稍大（0.8pp）因为calibration对probability scale更敏感，但仍在噪声范围内。
      这排除了"INT8 artifact"的reviewer concern。
    tables:
      - name: "Table S1: INT8 vs FP16 Comparison (Llama 4 Scout)"
        columns: [layer, int8_auroc, fp16_auroc, diff, direction_cosine]
        rows:
          - [8, 0.674, 0.678, -0.004, 0.991]
          - [16, 0.741, 0.745, -0.004, 0.989]
          - [24, 0.788, 0.791, -0.003, 0.992]
          - [32, 0.811, 0.814, -0.003, 0.990]
          - [40, 0.821, 0.827, -0.006, 0.987]
    figures_description:
      - "Fig S3: Bland-Altman plot — mean of INT8/FP16 AUROC (x) vs difference (y). All points within ±0.01 band. No systematic bias."
    analysis: >
      INT8量化不distort correctness signals。所有差异在bootstrap noise范围内。
      Deep层差异略大（layer 40: 0.6pp）符合预期——深层表征更complex，量化误差累积更多。
      但0.6pp远小于实验效应（CaCLR +6pp），不影响任何结论。

  - name: "CKA Cross-Lingual Representation Similarity"
    plan_id: "plan_011"
    description: >
      CKA (linear kernel) between EN and each target language at every probed layer,
      correlated with transfer AUROC. Mechanistic explanation for Pareto frontier.
    expected_results:
      cka_transfer_pearson_r: 0.82
      cka_transfer_pearson_r_ci: [0.76, 0.87]
      cka_transfer_spearman_rho: 0.79
      cka_en_zh_by_depth_trend: "monotonically decreasing from 0.92 (shallow) to 0.61 (deep)"
      cka_en_sw_by_depth_trend: "monotonically decreasing from 0.84 (shallow) to 0.38 (deep)"
      cka_resource_tier_gradient:
        HIGH_mean_cka_at_optimal_depth: 0.78
        MID_mean_cka_at_optimal_depth: 0.71
        LOW_mean_cka_at_optimal_depth: 0.58
      geometric_misalignment_evidence: >
        CKA drop from mid to deep layers exceeds what mean/covariance shift alone predicts.
        Subspace angle analysis shows correctness direction rotates 15-35° across languages
        at deep layers vs 5-12° at shallow layers.
      cka_explains_caclr_beta_limit: >
        At layers where CKA < 0.55, β term provides diminishing returns because
        geometric misalignment (rotation) dominates distributional shift.
    result_rationale: >
      CKA与transfer AUROC的高相关（r=0.82）提供了Pareto frontier的mechanistic explanation：
      cross-lingual表征相似度随depth monotonically下降，直接导致deep层transfer degradation。
      这不是trivial的"深层更specific"——CKA量化了具体的相似度数值并与transfer成功率
      建立了定量关系。High-resource语言在所有depth保持更高CKA（因为pretraining data overlap），
      解释了resource tier gradient。
      关键insight：deep层的CKA下降不仅是distributional shift（可被MMD修正），
      还包含geometric misalignment（correctness方向在语言间旋转15-35°）。
      这解释了CaCLR β term在deep层效果减弱——MMD对齐分布但不学习旋转，
      而linear projection学习旋转所以在deep层更稳定。
      Subspace angle analysis区分了distributional vs geometric misalignment，
      为Path A narrative提供了theoretical depth：CaCLR works at mid-depth因为
      那里的misalignment主要是distributional的。
    tables:
      - name: "Table 10: CKA by Depth and Resource Tier (Qwen3-235B)"
        columns: [depth_pct, HIGH_cka, MID_cka, LOW_cka, zs_auroc_median]
        rows:
          - [10, 0.93, 0.89, 0.84, 0.618]
          - [25, 0.90, 0.85, 0.78, 0.698]
          - [40, 0.86, 0.79, 0.69, 0.756]
          - [50, 0.82, 0.74, 0.62, 0.771]
          - [60, 0.78, 0.69, 0.55, 0.771]
          - [70, 0.73, 0.63, 0.47, 0.741]
          - [80, 0.67, 0.56, 0.41, 0.714]
          - [90, 0.61, 0.49, 0.35, 0.688]
    figures_description:
      - "Fig 6a: Dual-axis — CKA (left y-axis, lines by tier) and ZS AUROC median (right y-axis, dashed) vs normalized depth. CKA decrease tracks AUROC decrease after elbow."
      - "Fig 6b: Scatter — CKA vs ZS transfer AUROC, each point = language × layer. Strong linear relationship (r=0.82). Color by resource tier."
      - "Fig 6c: Subspace angle between EN and target correctness directions vs depth. Angles increase with depth; LOW languages diverge faster."
    analysis: >
      CKA analysis是论文的mechanistic backbone。它将observation（Pareto frontier）
      与explanation（representation geometry变化）和method（CaCLR的作用机制与局限）
      连接起来。CKA<0.55作为CaCLR β有效性的threshold是一个actionable finding——
      实践者可以用CKA预测CaCLR在哪些layer-language组合上有效。
      Geometric vs distributional misalignment的区分是theoretical contribution：
      它解释了为什么distributional matching（MMD/CaCLR）在mid-depth有效但在deep层递减，
      而geometric alignment（linear projection）在deep层更稳定。

  - name: "Linear Projection Sensitivity Analysis"
    plan_id: "plan_012"
    description: >
      Linear projection pair count sweep (10, 20, 50, 100, 200).
      Both models × 5 layers × 20 languages.
    expected_results:
      linear_proj_min_pairs_for_saturation: 35
      saturation_criterion: "95% of 200-pair performance"
      pairs_sweep:
        10: {median_auroc: 0.762, pct_of_200: 0.88}
        20: {median_auroc: 0.778, pct_of_200: 0.94}
        50: {median_auroc: 0.792, pct_of_200: 0.98}
        100: {median_auroc: 0.796, pct_of_200: 0.99}
        200: {median_auroc: 0.798, pct_of_200: 1.00}
      low_resource_saturation_later: true
      low_resource_min_pairs: 48
      high_resource_min_pairs: 22
    result_rationale: >
      Linear projection在~35 pairs时达到饱和（95% of 200-pair performance），
      因为correctness方向是低维线性结构——学习一个旋转/缩放矩阵不需要很多样本。
      10 pairs已经达到88%性能，说明即使极少数据也能捕获主要的geometric transformation。
      50 pairs后几乎无改善（98%→100%），符合线性映射的low sample complexity理论。
      Low-resource语言需要slightly more pairs（48 vs 22），因为表征空间中
      correctness方向的SNR更低，需要更多样本来robustly估计映射。
      整体saturation在20-50范围内，support "≤50 parallel pairs suffice"的claim。
      这建立了linear projection作为practical baseline的地位——
      50 pairs在任何语言都容易获得（e.g., 翻译50个MCQA items）。
    tables:
      - name: "Table 11: Linear Projection Data Efficiency (median across 20 langs × 2 models)"
        columns: [n_pairs, median_auroc, delta_vs_zs, pct_of_200pair, HIGH_auroc, LOW_auroc]
        rows:
          - [10, 0.762, 0.027, 88, 0.781, 0.638]
          - [20, 0.778, 0.043, 94, 0.798, 0.651]
          - [50, 0.792, 0.057, 98, 0.814, 0.664]
          - [100, 0.796, 0.061, 99, 0.818, 0.668]
          - [200, 0.798, 0.063, 100, 0.821, 0.671]
    figures_description:
      - "Fig S4: Learning curve — n_pairs (x, log) vs median AUROC (y). Rapid rise, plateau at ~50. Separate lines for HIGH/MID/LOW tiers — all plateau but at different levels."
    analysis: >
      Linear projection的data efficiency confirms它作为practical baseline的价值。
      50 pairs的saturation point意味着任何有minimal translation capacity的语言
      都可以使用这个方法。这也为CaCLR设定了benchmark：CaCLR需要beat 50-pair projection
      才能justify its additional complexity（in best tier, CaCLR beats by +1.4pp median）。

  - name: "Probing Control Tasks (Hewitt & Liang 2019)"
    plan_id: "plan_013"
    description: >
      Random-label control probes at each layer. Selectivity = probe AUROC - control AUROC.
      Validates genuine correctness signal.
    expected_results:
      control_task_auroc_range: [0.502, 0.538]
      selectivity_median: 0.284
      selectivity_min: 0.192
      selectivity_max: 0.341
      control_task_selectivity_min_across_langs: 0.192
      selectivity_by_depth:
        shallow: 0.218
        mid: 0.294
        deep: 0.312
      selectivity_by_tier:
        HIGH: 0.301
        MID: 0.278
        LOW: 0.234
    result_rationale: >
      Control probe AUROC在0.50-0.54范围（near chance），selectivity中位数0.284
      远超15pp minimum threshold（min=19.2pp）。这confirm probe AUROC反映
      genuine correctness direction而非memorized artifacts或probe capacity。
      Selectivity随depth增加（0.218→0.312），因为深层表征包含更丰富的correctness
      信号而control仍在chance附近——深层probe的高AUROC不是因为probe容量过大。
      Low-resource语言selectivity最低（0.234）但仍远超threshold，
      说明即使低资源语言的correctness信号也是genuine的（不是noise fitting）。
      这直接回应Hewitt & Liang probing methodology critique——
      我们的probes确实在提取linguistic property而非exploiting high-dimensional capacity。
    tables:
      - name: "Table S2: Control Task Selectivity (Qwen3-235B, selected layers × languages)"
        columns: [layer, en_selectivity, zh_selectivity, sw_selectivity, control_auroc]
        rows:
          - [16, 0.248, 0.231, 0.192, 0.512]
          - [32, 0.281, 0.268, 0.218, 0.519]
          - [48, 0.309, 0.292, 0.241, 0.524]
          - [56, 0.318, 0.301, 0.248, 0.521]
          - [76, 0.341, 0.324, 0.262, 0.538]
    figures_description:
      - "Fig S5: Paired bar chart — probe AUROC (dark) vs control AUROC (light) at each layer. Gap (selectivity) clearly visible and widening with depth. Horizontal line at 15pp threshold."
    analysis: >
      Control task validation是methodological necessity。Selectivity最小值19.2pp
      大幅超过15pp阈值，即使在最challenging的条件（low-resource × shallow layer）
      也确认probe是在提取genuine signal。这让reviewer对所有downstream结果
      （Pareto frontier, CaCLR, decomposition）更有信心。

  - name: "Gemma 4 31B Dense — Camera-Ready Extension"
    plan_id: "plan_008"
    description: >
      Third architecture (dense, FP16), full Pareto frontier. Dense vs MoE contrast for camera-ready.
    expected_results:
      en_best_auroc: 0.809
      en_best_layer: 48
      optimal_transfer_layer: 36
      zs_transfer_auroc_median: 0.738
      pareto_rho_median: -0.69
      pareto_shape: "smoother frontier than MoE models — no sharp elbow"
      dense_vs_moe_key_finding: >
        Dense architecture shows shallower Pareto slope — transfer degrades more
        gradually with depth compared to MoE models. Consistent with hypothesis
        that expert routing accelerates language specialization.
    result_rationale: >
      Gemma 4 31B Dense作为dense对照提供了architectural contrast。
      EN AUROC 0.809低于两个MoE模型（0.838, 0.821），反映31B dense参数<235B MoE active参数。
      关键发现：dense架构的Pareto frontier更平滑（rho=-0.69 vs MoE -0.73/-0.78），
      没有MoE的sharp elbow。这是因为MoE的expert routing在深层创造了discrete language
      specialization（某些experts "负责"特定语言），而dense模型的specialization是gradual的。
      这是architecture-dependent Pareto shape claim的strongest evidence。
      Optimal transfer在75%深度（layer 36/48），比Qwen3浅（60%）但比Scout深（50%），
      提供了第三个data point来characterize architecture-depth relationship。
    tables:
      - name: "Table S3: Three-Architecture Comparison Summary"
        columns: [model, type, params, layers, en_best_auroc, zs_median, optimal_transfer_pct, pareto_rho]
        rows:
          - [Qwen3-235B-A22B, MoE, 235B, 94, 0.838, 0.758, 60, -0.78]
          - [Llama 4 Scout, MoE, "109B (17B active)", 48, 0.821, 0.742, 50, -0.73]
          - [Gemma 4 31B Dense, Dense, 31B, 60, 0.809, 0.738, 75, -0.69]
    figures_description:
      - "Fig S6: Three Pareto frontiers overlaid on normalized depth axis. MoE models show sharper elbows; Dense model is smoother. Annotated with optimal transfer depth for each."
    analysis: >
      Three-architecture comparison is the crown jewel of Claim 1。
      Dense vs MoE对比provides causal insight into WHY frontiers differ——
      expert routing is the mechanism driving sharp language specialization at depth.

  - name: "Extended Language Coverage — Camera-Ready"
    plan_id: "plan_009"
    description: >
      Expand from 20 to 50+ languages. Camera-ready extension using GlobalMMLU/Belebele full sets.
    expected_results:
      total_languages: 52
      zs_langs_above_0p65: 38
      zs_auroc_median_52lang: 0.721
      new_low_resource_findings: >
        Several additional low-resource languages (e.g., Yoruba, Hausa, Malagasy)
        show ZS AUROC 0.58-0.64, confirming resource-tier gradient extends to tail.
      pareto_frontier_robust: true
      caclr_generalizes: true
      caclr_delta_over_zs_52lang_median: 0.058
    result_rationale: >
      52语言验证confirms所有findings at broader scale。ZS median从20 langs的0.758
      降到52 langs的0.721，因为新增语言主要是低资源的——这是expected的composition effect。
      38/52 > 0.65（73%）vs 17/20（85%），比例下降也反映低资源语言的加入。
      Pareto frontier和CaCLR在所有语言上consistent，说明findings是language-general的。
      Key new finding：Yoruba/Hausa等sub-Saharan African语言的ZS AUROC（0.58-0.62）
      与sw/bn相当，但CaCLR对这些语言的improvement更大（+7-9pp），
      可能因为GlobalMMLU translations provide parallel data that partially bridges
      the representation gap for these extremely low-resource languages.
    tables:
      - name: "Table S4: Extended Language Coverage Summary"
        columns: [resource_tier, n_langs, zs_auroc_median, caclr_median, delta]
        rows:
          - [HIGH, 12, 0.786, 0.828, 0.042]
          - [MID, 18, 0.741, 0.798, 0.057]
          - [LOW, 22, 0.648, 0.721, 0.073]
    figures_description:
      - "Fig S7: World map — ZS AUROC by country/language, color gradient from red (low) to green (high). Clear geographic pattern tracking resource availability."
    analysis: >
      Extended coverage是camera-ready的scale argument。核心findings在52语言上robust。
      Low-resource语言从CaCLR获益最多（+7.3pp vs HIGH +4.2pp），
      because these languages have the most room for improvement and
      CaCLR's distributional alignment compensates for sparse pretraining representation.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bebe028-aca1-4b91-82c5-e83843d1db83",
  "isSidechain": false,
  "requestId": "req_011CbESZy8Fo62gsMXWq1bMR",
  "type": "assistant",
  "uuid": "dd054a7e-3406-48f2-ba60-a50f9f70f5d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtqJnmqUqMTe7wP5syRDpG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13331,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16879,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16879,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13331
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：CaCLR consistency loss works (Path A); Pareto frontier is clean and architecture-dependent on both large models; all 4 claims fully validated 核心假设：['Pareto…",
  "leafUuid": "dd054a7e-3406-48f2-ba60-a50f9f70f5d7",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "CaCLR cross-lingual probe transfer and Pareto frontier analysis",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：CaCLR consistency loss works (Path A); Pareto frontier is clean and architecture-dependent on both large models; all 4 claims fully validated 核心假设：['Pareto…",
  "leafUuid": "dd054a7e-3406-48f2-ba60-a50f9f70f5d7",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "CaCLR cross-lingual probe transfer and Pareto frontier analysis",
  "sessionId": "eadc3f5b-a944-4ca4-a115-bd1593a166a5"
}
```

---
