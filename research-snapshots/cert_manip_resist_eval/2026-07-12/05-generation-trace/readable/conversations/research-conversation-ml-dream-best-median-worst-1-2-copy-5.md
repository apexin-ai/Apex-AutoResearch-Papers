# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/bd83f0b8-44ee-4474-a097-6b8adb21dc69.jsonl`
- **Structured JSON:** [`2004c67990fbe669c7ff.json`](../../sessions/20/2004c67990fbe669c7ff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:19:01.388Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:19:01.388Z",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: xling_calib_direction\nfocus: Re-dream after first Dream review (3/6). Key framing changes since last dream: (1) CaCLR now has conditional narrative — Path A method contribution if consistency loss works, Path B principled negative result with geometric misalignment explanation if it doesn't; (2) mean-shift rank-invariance as formal theoretical contribution (proof + experimental validation); (3) CKA mechanistic analysis added (plan_011) to explain WHY transfer fails; (4) probing control tasks (plan_013, Hewitt & Liang 2019); (5) linear projection sensitivity analysis (plan_012); (6) statistical rigor: bootstrap CIs + paired tests + Cohen's d as cross-cutting requirement; (7) per-language Spearman rho for Pareto frontier; (8) AUROC threshold sensitivity analysis; (9) expanded related work coverage (domain adaptation theory, alignment literature, conformal prediction); (10) decomposition grid justified (10 langs × 8 layers covers 3 resource tiers × major families). Verify these changes lift score to best ≥ weak accept and median ≥ borderline.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    INT8 weight quantization. Report per-language Spearman rho (depth vs transfer\n    AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: Needs 2× RTX 6000 PRO 96GB at INT8.\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations (GlobalMMLU train split translations,\n    not test items). Compare vs zero-shot, mean-shift, linear projection, few-shot\n    (25/100) across full Pareto frontier for both models × 20 languages. Hyperparameter\n    tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer\n    results (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative).\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'INT8 validation ablation: compare INT8 vs FP16 probing results at\n    5 representative layers for Llama 4 Scout on 5% random subset. Validates that\n    INT8 quantization doesn''t distort correctness signals.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Correlate CKA with transfer AUROC to provide mechanistic explanation\n    for the Pareto frontier. Explains WHY deeper layers transfer worse (lower cross-lingual\n    CKA). If CKA shows geometric misalignment (not just distributional shift), this\n    explains why MMD-based CaCLR fails but linear projection succeeds.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Dream review D5: \"no mechanistic explanation\" was flagged [M][W]. CKA upgrades\n    paper from measurement to insight. CPU-bound on cached activations. Reviewer suggests:\n    pilot on MVP activations (mvp_001/mvp_003, 6 langs × 8-9 layers × 2 models) before\n    full-scale run. Pilot is zero-cost and validates CKA pipeline informativeness.\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique.'\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: RUNNING\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    en_best_ece_tempcal: 0.0744\n    temp_scaling_T: 6.21\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: CONDITIONAL_PASS (3/4, P4 fail is expected naive baseline negative)\n    p1: PASS (AUROC=0.7541, ECE=0.0744 after T=6.21)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no systematic calibration improvement — retained as\n      naive baseline negative result)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T20:19:01.392Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:19:01.392Z",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T20:19:01.418Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4d99cb0f-0f65-4da6-a602-272fb53e73f3",
  "type": "user",
  "uuid": "acaa2801-0340-4163-8331-52df82c7c730",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:19:01.417Z_

```json
{
  "parentUuid": "acaa2801-0340-4163-8331-52df82c7c730",
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
  "uuid": "97fce010-6436-4dd8-9cdf-f91e4f338cfa",
  "timestamp": "2026-05-20T20:19:01.417Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:19:01.417Z_

```json
{
  "parentUuid": "97fce010-6436-4dd8-9cdf-f91e4f338cfa",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "53cf6194-a8d7-41db-b1f5-f28db5b3c6bb",
  "timestamp": "2026-05-20T20:19:01.417Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "53cf6194-a8d7-41db-b1f5-f28db5b3c6bb",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for cross-lingual calibration research",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69"
}
```

---

### Assistant

_source line 8 · 2026-05-20T20:19:42.667Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a Dream simulation based on the research context provided. Let me analyze the project carefully.

Key aspects of this research:
1. Cross-lingual calibration via correctness direction probes
2. Pareto frontier between depth and transferability
3. CaCLR method with conditional narrative (Path A: works, Path B: principled negative result)
4. Decomposition into difficulty-shared vs capability-specific components
5. Cross-lingual orthogonality of correctness-confidence directions


6. MVP results show Qwen2.5-7B achieving 0.754 AUROC on English at layer 27 with zero-shot transfer working across most languages except Swahili, while mean-shift calibration shows no effect and layer depth variations span roughly 12-14 percentage points in AUROC.

The remaining questions center on whether these patterns hold for larger models, whether the consistency loss in CaCLR actually improves performance, and whether the difficulty decomposition produces interpretable components.

For the best-case scenario, I'm imagining the Pareto frontier replicates consistently across architectures with CaCLR's consistency loss meaningfully shifting it, clean separation between difficulty and capability factors, strong CKA correlation with transfer success, and linear projection proving data-efficient enough to work with minimal training pairs. In the median case, the frontier replicates but noisier and less architecture-dependent, with CaCLR showing no benefit but still yielding interpretable results.

Now I'm thinking through what the worst case looks like—where the core Pareto frontier finding breaks down on larger models, both CaCLR and linear projection fail, transfer performance collapses to near-random for most languages, and I'd need to fundamentally reframe the narrative. I'm also sketching out concrete metric targets based on what the MVP showed: English AUROC around 0.754 on the 7B model, zero-shot transfer in the 0.56-0.686 range, and roughly 13 percentage points of layer delta. For larger models I'd expect better English performance, though the transfer story could shift either direction.

I'm defining nine key metrics to track: English AUROC on larger models, median zero-shot transfer across languages, the Pareto frontier strength, CaCLR's improvement over zero-shot, the consistency loss contribution, linear projection gains, decomposition effects on transfer, CKA-transfer correlation, and cross-lingual orthogonality. Then I'm setting performance ranges for the best case scenario—English AUROC hitting 0.80-0.85, zero-shot transfer around 0.72-0.78, a strong negative Pareto correlation between -0.7 and -0.9, and CaCLR contributing 2-5 percentage points through the consistency loss term.

Now I'm laying out the median performance band where English AUROC sits at 0.77-0.82, zero-shot transfer drops to 0.65-0.72, the Pareto relationship weakens to -0.4 to -0.7, and the consistency loss becomes nearly inert with less than 1 percentage point contribution. The worst-case scenario starts with English AUROC between 0.72-0.77, and I'm establishing these thresholds to evaluate whether the approach is actually working or if we're hitting diminishing returns.

Looking at the lower bound, performance barely clears the MVP baseline with zero-shot median around 0.55-0.63, the Pareto frontier becomes unreliable with weak correlations, and the consistency loss completely fails to activate. The linear projection gains become unpredictable and language-dependent, the decomposition loses its clean structure, and orthogonality breaks down with some languages exceeding the 0.15 threshold. But I'm reconsidering whether this framing is right—the Pareto frontier is already validated by MVP results, so the real question isn't whether it exists but whether it remains clean at scale and whether the architecture dependence holds up. This shifts my thinking toward what actually makes the paper acceptable: the best case validates all four claims, and I need to map out what each tier requires for publication viability.

Writing YAML config...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53cf6194-a8d7-41db-b1f5-f28db5b3c6bb",
  "isSidechain": false,
  "requestId": "req_011CbEST18rw4f9GEcvnYtga",
  "type": "assistant",
  "uuid": "44a22411-b24a-4567-978e-72e12914678a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbRQx6Zxhvd91YpBwMbA8Z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12759,
      "cache_read_input_tokens": 11841,
      "output_tokens": 4404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4404,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12759
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

_source line 9 · 2026-05-20T20:20:33.326Z_

```yaml
tiers:
  best:
    meaning: "CaCLR consistency loss works (Path A); Pareto frontier is clean and architecture-dependent on both large models; all 4 claims fully validated"
    key_assumptions:
      - "Pareto frontier replicates cleanly on Qwen3-235B and Llama 4 Scout with architecture-dependent shape (different optimal transfer depths)"
      - "CaCLR consistency loss (β term) provides meaningful gain over calibration-only (α-only) objective — distributional matching via MMD helps at mid-depth layers"
      - "Difficulty-capability decomposition yields clean separation: projecting out difficulty consistently improves transfer for capability-specific failures"
      - "CKA strongly correlates with transfer success, providing mechanistic explanation"
      - "Linear projection is data-efficient (≤50 parallel pairs suffice), establishing practical baseline"
      - "Control tasks confirm high selectivity (probe AUROC - control AUROC > 15pp) across languages and layers"
      - "Correctness-confidence orthogonality persists (cosine < 0.08) across all 20 languages × 2 architectures"
    number_ranges:
      en_best_auroc_large_model: [0.80, 0.86]
      zs_transfer_auroc_median_20lang: [0.72, 0.79]
      pareto_rho_per_lang_median: [-0.85, -0.65]
      caclr_beta_delta_auroc_over_alpha_only: [0.02, 0.05]
      caclr_full_delta_auroc_over_zeroshot_median: [0.04, 0.08]
      linear_proj_delta_auroc_over_zeroshot_median: [0.03, 0.06]
      linear_proj_min_pairs_for_saturation: [20, 50]
      decomposition_transfer_delta_after_difficulty_removal: [0.02, 0.04]
      cka_transfer_pearson_r: [0.70, 0.90]
      orthogonality_cosine_max_across_langs: [0.02, 0.08]
      control_task_selectivity_min: [0.15, 0.25]
      zs_langs_above_0p65_out_of_20: [15, 19]
      sw_bn_low_resource_zs_auroc: [0.60, 0.68]
      ece_reduction_vs_temp_scaling_median: [0.02, 0.05]
    narrative_direction: >
      Full method contribution paper. Headline: CaCLR-trained correctness probes reduce non-English ECE
      by X% with zero target-language labels. All 4 claims form a complete causal chain: (1) Pareto
      frontier discovered and characterized across architectures, (2) decomposition explains the
      frontier via difficulty-shared vs capability-specific components, (3) CaCLR exploits this
      understanding to shift the frontier — consistency loss aligns capability-specific signals
      across languages, (4) orthogonality establishes structural limits of output-based approaches.
      CKA analysis provides the mechanistic glue. Paper reads as: discovered a structure → understood
      it → exploited it → bounded it. Target: weak accept to accept at EACL.

  median:
    meaning: "CaCLR consistency loss is inert (Path B); but Pareto frontier is solid, linear projection is surprisingly strong, and CKA/decomposition provide genuine mechanistic insight into WHY distributional matching fails"
    key_assumptions:
      - "Pareto frontier replicates on both large models but architecture-dependent shape is moderate (same qualitative trend, quantitatively less distinct than hoped)"
      - "CaCLR consistency loss (β) is inert across 3 OOM sweep — MMD-based distributional matching does not improve correctness probe transfer"
      - "CKA analysis reveals geometric misalignment (rotation/scaling of correctness direction) at deeper layers, explaining both why zero-shot degrades AND why MMD fails (distributional ≠ geometric)"
      - "Linear projection is the winner: learns the rotation that MMD cannot, works with ~50-100 parallel pairs"
      - "Decomposition works but separation is partial — difficulty projection helps in ~60-70% of language-layer combos, not universal"
      - "Control tasks pass (selectivity > 10pp) but some low-resource languages show weaker selectivity"
      - "Orthogonality holds (cosine < 0.12) but with more variance across resource tiers than expected"
    number_ranges:
      en_best_auroc_large_model: [0.77, 0.83]
      zs_transfer_auroc_median_20lang: [0.65, 0.73]
      pareto_rho_per_lang_median: [-0.65, -0.40]
      caclr_beta_delta_auroc_over_alpha_only: [-0.005, 0.01]
      caclr_full_delta_auroc_over_zeroshot_median: [0.005, 0.02]
      linear_proj_delta_auroc_over_zeroshot_median: [0.02, 0.05]
      linear_proj_min_pairs_for_saturation: [50, 100]
      decomposition_transfer_delta_after_difficulty_removal: [0.005, 0.02]
      decomposition_pct_lang_layer_combos_improved: [0.55, 0.75]
      cka_transfer_pearson_r: [0.45, 0.70]
      orthogonality_cosine_max_across_langs: [0.06, 0.12]
      control_task_selectivity_min: [0.08, 0.15]
      zs_langs_above_0p65_out_of_20: [10, 15]
      sw_bn_low_resource_zs_auroc: [0.53, 0.62]
      ece_reduction_vs_temp_scaling_median: [0.00, 0.02]
    narrative_direction: >
      Analysis paper with principled negative result as centerpiece. Headline: distributional matching
      fails for cross-lingual correctness probe transfer because the misalignment is geometric, not
      distributional — CKA proves it, linear projection confirms it. Reorder claims: (1) Pareto
      frontier established, (2) CKA reveals geometric misalignment as mechanism, (3) CaCLR's failure
      is PREDICTED by the geometric explanation — this closes the distributional-matching path with
      both theory and evidence, (4) linear projection succeeds precisely because it learns the rotation.
      Decomposition and orthogonality become supporting evidence rather than standalone claims.
      The negative result is the contribution — it redirects the field away from distributional
      alignment toward geometric alignment for cross-lingual probe transfer. Soften ECE improvement
      claims; emphasize AUROC and mechanistic understanding. Target: borderline to weak accept at EACL.

  worst:
    meaning: "Pareto frontier is noisy or architecture-inconsistent; CaCLR fails; decomposition is inconclusive; but cross-lingual probing viability data and the mean-shift invariance proof are still novel contributions"
    key_assumptions:
      - "Pareto frontier exists qualitatively on one architecture but is weak or reversed on the other — architecture-dependent claim becomes 'architecture-specific, non-generalizable'"
      - "CaCLR fully fails (both α and β inert or harmful) — neither calibration loss nor consistency loss improves over zero-shot"
      - "CKA correlation with transfer is weak (r < 0.45) — mechanistic explanation is suggestive but not convincing"
      - "Linear projection helps but inconsistently: works for mid/high-resource languages, fails for low-resource (insufficient parallel quality)"
      - "Decomposition is inconclusive: difficulty projection sometimes helps, sometimes hurts, no clear pattern by resource tier"
      - "Zero-shot transfer AUROC is mediocre — only high-resource languages reliably above 0.65, many languages near 0.55-0.60"
      - "Control tasks reveal that some high AUROC is probe capacity artifact in low-resource settings (selectivity < 8pp)"
      - "Orthogonality holds broadly but with enough outliers (cosine > 0.15 for some langs) to weaken the universality claim"
    number_ranges:
      en_best_auroc_large_model: [0.73, 0.78]
      zs_transfer_auroc_median_20lang: [0.56, 0.65]
      pareto_rho_per_lang_median: [-0.40, -0.10]
      pareto_rho_sign_consistency_across_langs: [0.50, 0.70]
      caclr_beta_delta_auroc_over_alpha_only: [-0.02, 0.005]
      caclr_full_delta_auroc_over_zeroshot_median: [-0.01, 0.01]
      linear_proj_delta_auroc_over_zeroshot_median: [0.00, 0.03]
      linear_proj_pct_langs_improved: [0.45, 0.65]
      decomposition_transfer_delta_after_difficulty_removal: [-0.01, 0.01]
      cka_transfer_pearson_r: [0.15, 0.45]
      orthogonality_cosine_max_across_langs: [0.10, 0.20]
      control_task_selectivity_min: [0.03, 0.10]
      zs_langs_above_0p65_out_of_20: [5, 10]
      sw_bn_low_resource_zs_auroc: [0.50, 0.56]
      ece_reduction_vs_temp_scaling_median: [-0.01, 0.01]
    narrative_direction: >
      Reframe as field-level empirical survey: "Does probe-based calibration work beyond English?
      A systematic investigation." Drop CaCLR from claims entirely — relegate to one paragraph
      as attempted-and-failed. New claim structure: (1) mean-shift rank-invariance theorem (novel
      formal result with proof, universally validated, explains Xiao et al. vs our divergent findings),
      (2) resource-tier taxonomy of cross-lingual probe transferability (high-resource transfers,
      mid-resource is marginal, low-resource fails — first quantification across 20 languages),
      (3) practical recommendation: few-shot (25-100 labels) is the viable path, not alignment
      methods — closing the zero-label dream for low-resource languages. The paper becomes a
      "sobering empirical reality check" for the probe-based calibration line. The mean-shift
      proof and the 20-language empirical map are still novel. Orthogonality and Pareto data are
      reported but not overclaimed. Lean into the negative-results angle: "we tested every
      reasonable zero-label approach and none works reliably — here's what does work (few-shot)
      and why (geometric misalignment is language-pair specific)." Target: borderline at EACL,
      requires very clean writing and strong related-work positioning.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44a22411-b24a-4567-978e-72e12914678a",
  "isSidechain": false,
  "requestId": "req_011CbEST18rw4f9GEcvnYtga",
  "type": "assistant",
  "uuid": "55c8b97e-883b-4627-bdcc-a3405db7aa08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbRQx6Zxhvd91YpBwMbA8Z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12759,
      "cache_read_input_tokens": 11841,
      "output_tokens": 4404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4404,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12759
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "55c8b97e-883b-4627-bdcc-a3405db7aa08",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for cross-lingual calibration research",
  "sessionId": "bd83f0b8-44ee-4474-a097-6b8adb21dc69"
}
```

---
