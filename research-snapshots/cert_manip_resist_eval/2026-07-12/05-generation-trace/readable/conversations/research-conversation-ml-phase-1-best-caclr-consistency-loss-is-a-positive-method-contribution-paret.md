# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：CaCLR consistency loss is a positive method contribution; Pareto frontier ro

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/a0d496e8-1674-43bb-b810-06fbedbcb6a7.jsonl`
- **Structured JSON:** [`87862a598702c040265f.json`](../../sessions/87/87862a598702c040265f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:30:09.428Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:30:09.428Z",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：CaCLR consistency loss is a positive method contribution; Pareto frontier robust on both architectures; CKA geometric analysis holds after depth control; paper ships as method + discovery\n核心假设：['MMD on probe logits successfully aligns correctness subspace cross-lingually (β > 0 helps)', 'Large-model Pareto frontier is cleaner than 7B MVP (more structured representations)', 'CKA partial correlation (controlling for depth) remains significant at 20-language scale', 'Control task capacity artifacts confined to early layers + lowest-resource languages (<15% of lang-layer grid)', 'Difficulty-capability decomposition cleanly separates: projecting out difficulty improves transfer for capability-dominated langs', 'Cross-lingual orthogonality universally holds (cosine < 0.06)']\n关键指标范围：{'en_probe_auroc': [0.8, 0.85], 'zs_transfer_auroc_avg_20lang': [0.68, 0.74], 'zs_transfer_success_rate': [0.85, 1.0], 'pareto_spearman_rho_strong_arch': [-0.75, -0.55], 'pareto_spearman_rho_weak_arch': [-0.45, -0.2], 'caclr_delta_auroc_vs_zeroshot': [0.03, 0.06], 'caclr_delta_ece_vs_tempscaling': [-0.04, -0.02], 'linear_proj_50pairs_delta_auroc': [0.04, 0.08], 'cka_partial_corr_controlling_depth': [0.3, 0.5], 'cka_partial_corr_p': [0.001, 0.05], 'selectivity_below_005_fraction': [0.05, 0.15], 'orthogonality_cosine_range': [0.01, 0.06], 'difficulty_projection_transfer_delta': [0.02, 0.05]}\n叙事方向：原始 framing 完全成立。CaCLR 是正面方法贡献，Pareto frontier 是 discovery，decomposition 提供 prescriptive 指导，CKA 几何分析解释架构差异。Headline: 'CaCLR enables zero-label cross-lingual calibration, reducing non-English ECE by X% vs temperature scaling across 20 languages.' 四个 claims 均以强形式提出。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff varies across architectures (strong on Qwen, weak on Llama); CKA geometric analysis (not mechanistic explanation — correlational, must control for depth) suggests architecture-specific representation divergence rates as a factor. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. A methodological warning: control task analysis reveals that ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold), challenging uncritical use of cross-lingual probing. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis (framed as correlational, NOT mechanistic) provides two levels of insight: (a) between-language: languages with higher CKA show less transfer degradation; (b) between-architecture: CKA cliff steepness differs. **MUST report partial correlation controlling for normalized depth** — if CKA adds no explanatory power beyond depth, downgrade to \"suggestive correlational analysis.\" Subspace angle analysis (quantitative, not just prose) strengthens geometric narrative.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame CKA analysis as geometric/correlational, not mechanistic. We report partial correlation controlling for depth to test whether CKA adds explanatory power beyond the trivial \"deeper = worse transfer.\" If partial correlation is weak, we explicitly state CKA is suggestive only.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique.'\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- exp_id: plan_013_probing_controls_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:30:09.431Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:30:09.431Z",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T03:30:09.476Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：CaCLR consistency loss is a positive method contribution; Pareto frontier robust on both architectures; CKA geometric analysis holds after depth control; paper ships as method + discovery
核心假设：['MMD on probe logits successfully aligns correctness subspace cross-lingually (β > 0 helps)', 'Large-model Pareto frontier is cleaner than 7B MVP (more structured representations)', 'CKA partial correlation (controlling for depth) remains significant at 20-language scale', 'Control task capacity artifacts confined to early layers + lowest-resource languages (<15% of lang-layer grid)', 'Difficulty-capability decomposition cleanly separates: projecting out difficulty improves transfer for capability-dominated langs', 'Cross-lingual orthogonality universally holds (cosine < 0.06)']
关键指标范围：{'en_probe_auroc': [0.8, 0.85], 'zs_transfer_auroc_avg_20lang': [0.68, 0.74], 'zs_transfer_success_rate': [0.85, 1.0], 'pareto_spearman_rho_strong_arch': [-0.75, -0.55], 'pareto_spearman_rho_weak_arch': [-0.45, -0.2], 'caclr_delta_auroc_vs_zeroshot': [0.03, 0.06], 'caclr_delta_ece_vs_tempscaling': [-0.04, -0.02], 'linear_proj_50pairs_delta_auroc': [0.04, 0.08], 'cka_partial_corr_controlling_depth': [0.3, 0.5], 'cka_partial_corr_p': [0.001, 0.05], 'selectivity_below_005_fraction': [0.05, 0.15], 'orthogonality_cosine_range': [0.01, 0.06], 'difficulty_projection_transfer_delta': [0.02, 0.05]}
叙事方向：原始 framing 完全成立。CaCLR 是正面方法贡献，Pareto frontier 是 discovery，decomposition 提供 prescriptive 指导，CKA 几何分析解释架构差异。Headline: 'CaCLR enables zero-label cross-lingual calibration, reducing non-English ECE by X% vs temperature scaling across 20 languages.' 四个 claims 均以强形式提出。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: xling_calib_direction

## paper_framing.md

# Paper Framing — xling_calib_direction

## Target Venue
- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
- Core submission: 2 models × 20 languages × all contributions
- Camera-ready extension: Gemma 4 31B Dense + 30+ languages

## Core Insight
The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff varies across architectures (strong on Qwen, weak on Llama); CKA geometric analysis (not mechanistic explanation — correlational, must control for depth) suggests architecture-specific representation divergence rates as a factor. CaCLR tests whether distributional matching can shift this frontier without target-language labels.

## Core Claims (4, causal chain)

### Claim 1 — Pareto Frontier (Discovery)
Cross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).
- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).
- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.

### Claim 2 — Decomposition (Analysis)
Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
- Evidence: IRT difficulty probes → project out → retrain → compare transfer.

### Claim 3 — CaCLR (Method / Diagnostic)
CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.
- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.
- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.
- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.
- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.

### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.

## Story Spine
- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. A methodological warning: control task analysis reveals that ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold), challenging uncritical use of cross-lingual probing. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.
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
10. **"No mechanistic explanation"** → CKA geometric analysis (framed as correlational, NOT mechanistic) provides two levels of insight: (a) between-language: languages with higher CKA show less transfer degradation; (b) between-architecture: CKA cliff steepness differs. **MUST report partial correlation controlling for normalized depth** — if CKA adds no explanatory power beyond depth, downgrade to "suggestive correlational analysis." Subspace angle analysis (quantitative, not just prose) strengthens geometric narrative.
11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
13. **"CaCLR is your own method — self-debunking is less impactful"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.
14. **"CKA is correlational, not mechanistic"** → We agree and frame CKA analysis as geometric/correlational, not mechanistic. We report partial correlation controlling for depth to test whether CKA adds explanatory power beyond the trivial "deeper = worse transfer." If partial correlation is weak, we explicitly state CKA is suggestive only.

## Additional Related Work Coverage (Dream-identified gaps)
- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) "On learning invariant representations for domain adaptation" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.
- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.
- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.
- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.
- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.
- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.

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
  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract
    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,
    train English correctness probes (logistic regression + 2-layer MLP), evaluate
    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,
    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global
    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.

    '
  priority: P0
  gpu_budget_hours: 80
  deps: []
  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required
    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative
    layers on subset — extend plan_010).

    '
  status: planned
- id: plan_002
  claim: 1
  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract
    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.
    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).
    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.

    '
  priority: P0
  gpu_budget_hours: 40
  deps: []
  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).
    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).
    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).

    '
  status: planned
- id: plan_003
  claim: 3
  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +
    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English
    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned
    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations
    from probe_train only; evaluate exclusively on eval portion. No train split exists
    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient
    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across
    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α
    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results
    (50% depth + EN-optimal) alongside per-language oracle.

    '
  priority: P0
  gpu_budget_hours: 20
  deps:
  - plan_001
  - plan_002
  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS
    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert
    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional
    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,
    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic
    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion
    (d) Initialization: from standard LR solution or from scratch (e) Batch size for
    MMD computation (f) Whether MMD items overlap with BCE training items or held-out
    (g) Parallel set size per language + translation quality note for low-resource
    Negative result demands higher reproducibility bar than positive.

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
  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative
    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at
    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization
    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download
    of FP16 weights for subset only, then delete. May need to do sequentially due
    to disk constraints.

    '
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_001
  - plan_002
  status: planned
- id: plan_011
  claim:
  - 1
  - 4
  description: 'CKA cross-lingual representation similarity analysis: compute CKA
    (linear kernel) between English and each target language at every probed layer
    for both models. Full-scale validation of pilot finding: correctness direction
    is a robust low-dimensional subspace feature that persists despite global CKA
    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA
    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)
    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,
    and critical threshold analysis.

    '
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_001
  - plan_002
  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).
    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen
    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):
    pooled correlation has depth confound. Pilot per-language Spearman almost all
    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language
    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),
    not within-language depth effects. Supportable claim: "languages with higher CKA
    exhibit less transfer degradation" (between-language, qualitative at n=5). NOT
    supportable: "CKA predicts within- language degradation across depth." Full-scale
    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest
    test, n=20 per layer), (b) partial correlation controlling for normalized depth
    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if
    CKA adds no explanatory power beyond depth, downgrade framing from "geometric
    analysis" to "suggestive correlation", (c) per-language Spearman with denser layer
    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose
    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength
    difference (qualitative). Frame as "geometric/correlational analysis" NOT "mechanistic
    explanation" (Dream RD6/RD9).

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
    temp_scaling_fixed:
      L24:
        T: 0.67
        ECE_cal: 0.2205
      L27:
        T: 0.62
        ECE_cal: 0.2216
      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.
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
    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per
      D006.
    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)
    p2: PASS (4/5)
    p3: PASS (14.28pp)
    p4: FAIL (0/5, mean-shift no improvement)
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
  status: DONE
  conclusion: success
  metrics:
    en_best_auroc: 0.7284
    en_best_layer: 31
    en_best_ece_raw: 0.2052
    en_auroc_range:
    - 0.6331
    - 0.7284
    layer_depth_delta: 0.0953
    layers_tested:
    - 0
    - 4
    - 8
    - 12
    - 16
    - 20
    - 24
    - 28
    - 31
    best_zs_auroc:
      zh: 0.64
      ar: 0.6146
      hi: 0.5935
      ko: 0.6481
      sw: 0.5838
    best_zs_layer:
      zh: 20
      ar: 31
      hi: 31
      ko: 31
      sw: 16
    zs_pass_langs:
    - zh
    - ar
    - hi
    - ko
    - sw
    zs_fail_langs: []
    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)
    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).
      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC
      is rank-invariant.'
    cka_vs_degradation:
      overall_rho: -0.3982
      overall_p: 0.0068
      per_lang:
        ar:
          rho: -0.2833
          p: 0.46
        hi:
          rho: -0.6667
          p: 0.0499
        ko:
          rho: 0.25
          p: 0.5165
        sw:
          rho: -0.5833
          p: 0.0992
        zh:
          rho: -0.4833
          p: 0.1875


## registry (completed experiments)

- exp_id: mvp_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    en_best_auroc: 0.7541
    en_best_layer: 27
    en_best_ece_raw: 0.1951
    temp_scaling_fixed:
      L24:
        T: 0.67
        ECE_cal: 0.2205
      L27:
        T: 0.62
        ECE_cal: 0.2216
      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.
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
    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per
      D006.
    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)
    p2: PASS (4/5)
    p3: PASS (14.28pp)
    p4: FAIL (0/5, mean-shift no improvement)
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
  status: DONE
  conclusion: success
  metrics:
    en_best_auroc: 0.7284
    en_best_layer: 31
    en_best_ece_raw: 0.2052
    en_auroc_range:
    - 0.6331
    - 0.7284
    layer_depth_delta: 0.0953
    layers_tested:
    - 0
    - 4
    - 8
    - 12
    - 16
    - 20
    - 24
    - 28
    - 31
    best_zs_auroc:
      zh: 0.64
      ar: 0.6146
      hi: 0.5935
      ko: 0.6481
      sw: 0.5838
    best_zs_layer:
      zh: 20
      ar: 31
      hi: 31
      ko: 31
      sw: 16
    zs_pass_langs:
    - zh
    - ar
    - hi
    - ko
    - sw
    zs_fail_langs: []
    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)
    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).
      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC
      is rank-invariant.'
    cka_vs_degradation:
      overall_rho: -0.3982
      overall_p: 0.0068
      per_lang:
        ar:
          rho: -0.2833
          p: 0.46
        hi:
          rho: -0.6667
          p: 0.0499
        ko:
          rho: 0.25
          p: 0.5165
        sw:
          rho: -0.5833
          p: 0.0992
        zh:
          rho: -0.4833
          p: 0.1875
- exp_id: plan_013
  name: ''
  status: DONE
  conclusion: success
  metrics:
    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)
    selectivity_hewitt_liang:
      L0: 0.02
      L4: 0.037
      L8: 0.036
      L12: 0.042
      L16: 0.123
      L20: 0.244
      L24: 0.248
      L27: 0.262
    real_auroc:
      L0: 0.501
      L4: 0.524
      L8: 0.529
      L12: 0.53
      L16: 0.615
      L20: 0.733
      L24: 0.738
      L27: 0.746
    permuted_auroc:
      L0: 0.481
      L4: 0.487
      L8: 0.493
      L12: 0.488
      L16: 0.492
      L20: 0.489
      L24: 0.49
      L27: 0.484
    pca_variance_retained:
      L0: 0.922
      L4: 0.912
      L8: 0.885
      L12: 0.868
      L16: 0.783
      L20: 0.738
      L24: 0.844
      L27: 0.794
    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal
      concentrated in L20-L27. PCA(100) retains 73-92% variance.
- exp_id: plan_013_probing_controls_v2
  name: ''
  status: PREPARING
  conclusion: failed
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
  "promptId": "48fce09e-cede-43b8-957b-293e8429dbcf",
  "type": "user",
  "uuid": "578407eb-56c7-41fd-a152-291eb052e103",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:30:09.474Z_

```json
{
  "parentUuid": "578407eb-56c7-41fd-a152-291eb052e103",
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
  "uuid": "8ea66a8f-7b20-4731-8e14-e1e3ac17a6d3",
  "timestamp": "2026-05-21T03:30:09.474Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:30:09.474Z_

```json
{
  "parentUuid": "8ea66a8f-7b20-4731-8e14-e1e3ac17a6d3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "24464ca6-7efe-4523-ae9e-669db01fca76",
  "timestamp": "2026-05-21T03:30:09.474Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：CaCLR consistency loss is a positive method contribution; Pareto frontier robust on both architectures; CKA geometric analysis holds after depth control; p…",
  "leafUuid": "24464ca6-7efe-4523-ae9e-669db01fca76",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe calibration with CaCLR",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7"
}
```

---

### Assistant

_source line 8 · 2026-05-21T03:38:35.321Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, under the "best" tier definition. Let me carefully go through each experiment and generate predictions consistent with the best tier's key metrics, core assumptions, and narrative direction.

Let me review the best tier definition:
- CaCLR consistency loss is a positive method contribution
- Pareto frontier robust on both architectures
- CKA geometric analysis holds after depth control
- Paper ships as method + discovery

Key metrics ranges:
- en_probe_auroc: [0.8, 0.85]
- zs_transfer_auroc_avg_20lang: [0.68, 0.74]


- zs_transfer_success_rate: [0.85, 1.0]
- pareto_spearman_rho_strong_arch: [-0.75, -0.55]
- pareto_spearman_rho_weak_arch: [-0.45, -0.2]
- caclr_delta_auroc_vs_zeroshot: [0.03, 0.06]
- caclr_delta_ece_vs_tempscaling: [-0.04, -0.02]
- linear_proj_50pairs_delta_auroc: [0.04, 0.08]

Now I'm working through the remaining metric ranges to complete the best tier specification.

Looking at my planned experiments: I've got the full Pareto analysis lined up for both the strong architecture on Qwen and the weak architecture on Llama, then moving into CaCLR implementation, difficulty-controlled ablation studies, and cross-lingual orthogonality testing.

The remaining experiments cover probe complexity comparisons, additional benchmarks, quantization validation, CKA analysis, linear projection sensitivity, and control tasks which I've already completed. I'm also planning to evaluate Gemma 4 and extend language coverage as secondary priorities.

The MVP baseline shows solid performance with Qwen2.5-7B hitting 0.7541 AUROC in English and Llama-3.1-8B at 0.7284, with zero-shot performance around 0.686 and 0.648 respectively on other languages. I'm expecting the larger models like the 235B Qwen and Llama 4 Scout to push these numbers higher.

Now I'm working through the predictions systematically. I need to account for what's already completed versus what's still planned, then generate detailed predictions for each experiment with proper rationale. I'm starting with the larger models and their architectural advantages—the 235B Qwen with its MoE design and significantly deeper layer count should show meaningful improvements over the 7B baseline. Looking at the language distribution across the typological spectrum, I'm mapping out which ones fall into high, mid, and low transfer success tiers. Now I need to work through the detailed predictions for both architectures—the strong Qwen model should show that deeper layers consistently hurt cross-lingual transfer with a steep negative correlation around -0.65, while the weaker Llama Scout variant exhibits more scattered per-language behavior with a shallower -0.35 relationship, suggesting architectural capacity plays a role in how depth affects generalization.

Writing YAML configuration... Looking at the probe complexity results, linear models generalize better across languages while MLPs perform better within a single language but degrade significantly when transferring. The additional benchmarks on Belebele and MMLU-ProX show consistent patterns, confirming the findings hold more broadly. For quantization, the weight and activation reductions have minimal impact on the correctness signals, staying well under 0.02 AUROC difference. The CKA analysis reveals that representational similarity explains variance beyond just architectural depth, with the steepness of the CKA cliff varying across model architectures.

For plan_012, I'm seeing that projection sensitivity plateaus around 50 pairs with diminishing returns, reaching about 0.07 AUROC gain at 200 pairs. The control tasks show selectivity concentrated in early layers and lower-resource languages at under 5% of the language-layer grid. Gemma 4 as a third architecture validates the patterns hold across different model families, and extending to 50+ languages confirms the same phenomena persist at scale. Now I'm structuring all these findings into a comprehensive YAML format.

I need to focus on the planned experiments specifically—filtering out the completed plan_013 and the failed preparation attempts—so I can provide detailed predictions for each of the twelve planned experiments across both priority tiers.

Now I'm working through the specific performance numbers more carefully, thinking about how the best-tier assumptions would affect scaling behavior. For the larger models, I'm reasoning through why the AUROC improvements would follow the patterns shown in probing literature—like how Qwen3-235B would reach around 0.83 on English tasks due to better structured internal representations, and how the MoE architecture in Llama 4 Scout would similarly improve linearly separability of the correctness signal.

For cross-lingual transfer, I'm estimating that Qwen3-235B maintains stronger multilingual alignment at 0.72 average across 20 languages, while Llama 4 Scout drops to 0.69. The success rate threshold (AUROC > 0.6) shows Qwen3-235B succeeding on 19 out of 20 languages versus Llama 4 Scout on 17 out of 20. The Pareto Spearman correlation also diverges significantly—Qwen3-235B shows a stronger negative correlation of -0.65 between model size and performance variance, while Llama 4 Scout's weaker architecture only achieves -0.33.

Now I'm mapping out the per-language breakdown across 20 languages selected for typological and resource diversity: seven high-resource languages (Chinese, Spanish, French, German, Japanese, Portuguese, Italian), seven mid-resource languages (Hindi, Russian, Korean, Turkish, Vietnamese, Arabic, Thai), and six low-resource languages (Swahili, Bengali, Yoruba, Telugu, Burmese, Amharic). For Qwen3-235B, I'm assigning zero-shot AUROCs that reflect this resource stratification—high-resource languages cluster around 0.76-0.78, mid-resource around 0.69-0.74, and low-resource dropping to 0.61-0.65.

Computing the category averages: high-resource lands at 0.763, mid-resource at 0.716, and low-resource at 0.63, which gives an overall average of 0.707—right in the expected range of 0.68 to 0.74.

Now looking at Llama 4 Scout with its weaker architecture but best tier performance, I'm seeing similar patterns across the language tiers with high-resource languages clustering around 0.73, mid-resource around 0.69, and low-resource around 0.60.

When I average these out, I get an overall score of 0.677, which falls just slightly below the 0.68 threshold. I'm wondering if I need to adjust this upward, but I'm also realizing I need to clarify what the zs_transfer_auroc_avg_20lang metric actually represents—whether it's computed across both architectures or separately for each one, since the metric definition doesn't specify this clearly.

If it's the combined average across both architectures, then (0.707 + 0.677)/2 = 0.692 would put me in range. But if it's per-architecture, I should bump up the Llama scores slightly. Let me recalculate with adjusted values for Llama 4 Scout across the language tiers.

Now I'm checking whether these numbers are internally consistent and fall within the target ranges. Rather than getting bogged down in overall averages, I should focus on what each experiment actually reports—the specific metrics that matter. For the first two plans, that's the English AUROC per layer, zero-shot transfer AUROC broken down by language and layer, the correlation between depth and transfer performance, and the five different transfer conditions. For the CaCLR experiment, I need to think through what the key outputs should be.

Continuing with the specific metrics for each plan...

Now I'm moving on to actually write out the YAML configuration. I should also think through what tables and figures each experiment will need to present the results clearly.

I'm realizing the MVP used GlobalMMLU with roughly 900 items per language, and the full experiments will expand the language and layer coverage while keeping the same dataset. One key finding stands out: the consistency loss with β > 0 does help, which validates that the MMD regularization on probe logits successfully aligns the correctness subspace—we're seeing moderate improvements of 3-6% AUROC and 2-4% ECE reduction compared to temperature scaling alone.

Now I need to be careful about plan_013 since it's already marked as done. The selectivity results show a clear pattern: layers 0-12 have selectivity barely above chance (< 0.05), while layers 16-27 show meaningful selectivity (0.12-0.26). The full-scale version would extend this across 20 languages and both architectures, but since the MVP is complete, I should focus on what still needs to be run rather than re-predicting what's already finished. I'll include plan_013 in my predictions for the full-scale version since the experiment plan lists it as pending for both architectures across all languages, even though preliminary English-only results exist in the registry. Now I'm structuring the YAML output with the required fields: tier, narrative guidance, and an array of imagined experiments, each containing name, plan ID, description, expected results, rationale, tables, figures, and analysis sections. Let me draft the predictions for each experiment systematically.

I'm anchoring my tier assessment on several key metrics: Qwen3-235B achieves 0.83 AUROC in English at layer 72 (77% depth), Llama 4 Scout reaches 0.81 at layer 40 (83% depth), zero-shot performance averages 0.72 for Qwen and 0.69 for Llama across 20 languages, and the Pareto frontier shows stronger negative correlation for Qwen (-0.65) than Llama (-0.33). I'm also factoring in that CaCLR improves AUROC by 0.045 on average and reduces ECE by 0.03, linear projections show +0.06 gains, CKA partial correlation reaches 0.42 with statistical significance, and orthogonality measurements cluster between 0.01 and 0.06 cosine distance.

Now I'm examining how CaCLR reshapes the Pareto frontier—at deeper layers where English probes perform well but zero-shot transfer collapses, CaCLR partially recovers that lost performance. At layer 72 where English achieves its peak, zero-shot might drop to 0.65 but CaCLR lifts it to 0.70, while at the Pareto-optimal layer around 56, zero-shot sits at 0.72 and CaCLR pushes it to 0.74. This pattern suggests CaCLR is most valuable precisely where the frontier becomes steepest.

Now I'm structuring the results as a YAML format with per-language breakdowns—I'll use summary statistics and resource tier comparisons rather than listing all 20 languages for every metric, then include a few representative language examples to illustrate the patterns.

Writing YAML structure... Defining expected results for the Qwen3 experiment across multiple metrics—AUROC performance at different layers, ECE values, zero-shot transfer success rates across 20 languages, and Spearman correlations showing the relationship between model depth and calibration quality. Compiling the per-language zero-shot AUROC scores and their optimal layers across the full set of languages, from high-resource ones like Portuguese and Italian down to lower-resource languages like Yoruba and Swahili. Now I'm looking at the few-shot performance metrics—25 examples get me to 0.738 AUROC, and scaling to 100 examples pushes it up to 0.771. The larger 235B MoE model has much more structured internal representations than the 7B baseline, with the correctness direction showing stronger linear separability in the mid-to-high layers, which should push the English performance to around 0.83. The increased multilingual pretraining data in the larger model also creates better cross-language alignment, lifting zero-shot transfer from roughly 0.65 to 0.72 compared to the smaller version.

The 94-layer architecture gives me finer depth resolution to identify the Pareto frontier more clearly—there's about a 16-layer gap between the optimal layer for English (L72 at 77% depth) and the optimal layer for transfer (L52-56 at 55-60% depth), creating a strong negative correlation around -0.65. Low-resource languages show the most severe degradation at deeper layers, with correlations dropping to -0.82, because their representations start specializing linguistically at those depths. I've also verified that mean-shift AUROC delta is strictly zero mathematically—constant offsets don't change the ranking under StandardScaler and logistic regression.

Generating markdown table... Generating markdown table... Looking at the scatter plot description showing the relationship between English AUROC and zero-shot transfer performance across layers, with a clear negative correlation of -0.65. The bar chart then breaks down this correlation by language resource tier, revealing that lower-resource languages show even stronger negative correlations. The analysis confirms that Qwen3-235B exhibits a pronounced depth-transferability tradeoff, with the Pareto frontier pattern being more pronounced than in the smaller Qwen2.5-7B model, strengthening the hypothesis that larger models develop more structured representations with more robust frontiers.

The key findings show that 19 out of 20 languages successfully transferred with AUROC above 0.6, with only Amharic at the boundary. There's a clear resource tier gradient where high-resource languages achieve 0.77 AUROC versus 0.63 for low-resource languages, a gap of 0.14. Interestingly, the optimal transfer layers cluster around 40-60% depth rather than at the English optimal layer of 72.

Now examining the Llama 4 Scout results with its 48-layer MoE architecture... Compiling the per-language performance breakdown across all twenty languages, with AUROC scores ranging from 0.618 to 0.762 and optimal layer selections varying between layers 28 and 40. Looking at the performance metrics, Llama 4 Scout achieves an English AUROC of 0.81, which trails Qwen3 but substantially outperforms the baseline Llama-3.1-8B at 0.728. The Pareto frontier shows weak negative correlation (around -0.33), continuing the pattern from the earlier model where certain languages like Russian, Korean, and Arabic maintain or slightly improve performance with depth, while others like Swahili, Yoruba, and Amharic degrade significantly—likely because the MoE routing allocates different experts to different languages at deeper layers, creating heterogeneous per-language behavior.

The overall Pareto strength remains weaker than Qwen3, which aligns with the best-tier expectation of more structured representations being more evident in Qwen. Three low-resource languages (Yoruba, Burmese, Amharic) fall below the 0.60 threshold, though the transfer success rate of 17 out of 20 languages (0.85) meets the best-tier minimum. Now I'm examining the detailed Pareto frontier summary across the 20 languages and 12 layers, looking at the zero-shot AUROC values and correlation patterns for each language family. Now I'm looking at the figure descriptions and analysis for the Llama 4 results — comparing its Pareto frontier against Qwen3, where Llama shows a much flatter slope and higher heterogeneity across languages, with some languages like Russian and Korean trending upward while others like Swahili and Yoruba decline.

Moving into the CaCLR implementation evaluation across both architectures and twenty languages, examining the hyperparameter sweep results...

Generating evaluation metrics... Now I'm looking at the statistical significance of the beta parameter ablation with a p-value of 0.003 and a Cohen's d of 0.52, then examining how CaCLR's improvements vary across different resource tiers—showing stronger gains on lower-tier resources—and noting that at the English-optimal layer the model achieves even better performance with a 0.056 delta improvement. The β = 0.1 weighting strikes the right balance between alignment pressure and preserving the BCE loss signal. SB-ECE contributes a modest +0.006 AUROC improvement mainly through better calibration, while MMD drives the larger gains—especially pronounced in low-resource languages where the zero-shot transfer gap is widest, yielding +0.067 improvement. On deeper layers like L72, CaCLR shows even stronger gains (+0.056 versus +0.045 at shallower depths), demonstrating that the method effectively addresses the more severe degradation in deep layer transfer.

The statistical significance is solid with Cohen's d = 0.52 and p = 0.003, confirming β's positive contribution. Now I'm looking at the comparative performance table across both model architectures at their Pareto-optimal layers. Generating markdown table...

Now I'm describing the figures — there's an α-β heatmap showing the optimal region around α=1.0 and β=0.1, a Pareto frontier comparison where CaCLR points shift the boundary rightward, a per-language breakdown revealing the largest gains for low-resource settings, and a β sensitivity curve that peaks at β=0.1. The analysis section is starting to discuss the statistical significance of CaCLR improvements when β is positive.

The next thinking reveals the key findings: MMD contributes most of the gain (+0.030) while SB-ECE alone adds only +0.006, but they work synergistically together; deeper layers in English-optimal models show larger improvements (+0.056), confirming the Pareto shift; low-resource languages benefit most (+0.067), aligning with domain adaptation theory where the largest distribution mismatches yield the highest alignment gains; and β=1.0 becomes too aggressive, letting the MMD term dominate and hurting probe accuracy.

Now I'm looking at the difficulty-controlled decomposition ablation plan, which uses IRT difficulty probes to isolate and remove specific capability dimensions before retraining to measure how transfer changes. The results show an average improvement of 0.035 after projection, with low-resource languages gaining the most (0.052), mid-resource gaining substantially (0.041), and high-resource gaining least (0.018) since they already transfer well—suggesting the effect is capability-dominated rather than driven by other factors. The pattern across model depths is clear—deeper layers capture increasingly stronger capability signals once difficulty is removed. The key insight is that difficulty and capability are entangled in the activation space, but their roles differ by language resource level: for high-resource languages, removing difficulty noise reveals the true capability signal and improves transfer by 4.2%, while for low-resource languages, difficulty itself carries most of the correctness information, so removing it actually hurts performance. Generating markdown table... 现在我在查看跨语言正交性分析的具体指标——20种语言和2种架构的余弦相似度分布，从西班牙语的最低值0.012到阿姆哈拉语的最高值0.058，平均值0.032。资源层级间存在显著差异，高资源语言的正交性更强（0.028），而低资源语言的正交性较弱（0.039），这与排列检验的p值<0.001一致，表明这种模式远非随机。

架构间的差异较小，Qwen和Llama的平均值分别为0.029和0.035，说明正交性是模型设计的基本特性而非架构特异性的。

资源层级与余弦相似度的关联在统计上处于边界（p=0.052），提示了可能的趋势但证据还不够确定。现在我在查看各语言间的具体数值对比，从英文的0.028到斯瓦希里语的0.045，以及阿姆哈拉语更高的0.047。

这些数据点都集中在很小的范围内，验证了正交性在跨语言中普遍成立，这强化了输出校准方法存在结构性限制的结论，进一步支持采用基于探针的方法。接下来我在比较逻辑回归和两层多层感知机在跨语言迁移中的表现。 The MLP's nonlinear capacity gives it a slight edge on English, but it comes at the cost of learning language-specific patterns that don't transfer well—showing 18.7% degradation versus the linear model's 13.7%. This overfitting is especially pronounced in low-resource languages where the linear probe maintains better generalization, reinforcing that a linear approach is the safer default choice. 线性探针在跨语言迁移上表现更好，这验证了我的假设——MLP 的额外容量捕捉的是语言特定特征而不是语言无关的正确性方向。所以在后续分析中继续使用线性探针是正确的选择。现在我需要用 Belebele 和 MMLU-ProX 这两个基准来验证模型的泛化能力。

Belebele 是阅读理解任务，MMLU-ProX 是翻译后的 MMLU，我看到两个基准上的零样本排名相关性都很高（0.89 和 0.93），说明探针的排名一致性很强，虽然 Belebele 的 AUROC 略低于 GlobalMMLU，这是因为两个任务的领域不同。

关键是 Pareto frontier 的模式在两个基准上都很相似（-0.61 对比 -0.65），这表明深度和可转移性之间的权衡是模型架构的固有特性，而不是数据特性。

语言排名的一致性也很高（0.89-0.93），证实了这些发现能够跨基准泛化。现在我在验证量化对这些结果的影响，比较不同精度设置下的性能。 Now I'm looking at the statistical validation—the paired t-tests show p-values well above 0.15 for both models, confirming that despite the layer-by-layer distortions being measurable, they're not statistically significant. This makes sense because W4A16 only quantizes weights while keeping activations at full precision, so the impact on the linear probe's correctness direction stays under 1 percentage point AUROC, while GPTQ-INT4 shows slightly larger distortion concentrated in the deepest layers where quantization errors accumulate, but still within acceptable bounds. 使用量化模型不影响核心结论。CKA > 0.98 表示量化前后表征高度相似。

现在看量化验证的具体数据——Llama 4 Scout 和 Qwen3-235B 在不同量化方案下的 AUROC 变化都很小，最大偏差只有 1.3pp，远低于论文中观察到的主要效应，所以这个结果可以简要报告在主文，详细放在附录。接下来要分析 CKA 在跨语言表征相似性上的表现，涉及 20 种语言和 2 种架构，需要用偏相关来控制深度的影响。 Looking at the between-language correlations, there's a strong negative relationship between CKA similarity and transfer performance across languages, with subspace angles showing that correctness-relevant representations diverge much more sharply than global representations. The analysis identifies a CKA threshold around 0.35 where transfer capability collapses, particularly affecting languages like Swahili, Yoruba, Amharic, and Burmese.

The partial correlation analysis reveals that CKA has independent explanatory power for transfer degradation beyond just depth effects—it's not simply that deeper layers perform worse. The mechanism appears to be that correctness-relevant features occupy a narrow language-agnostic subspace, and when CKA drops below the critical threshold, this subspace becomes language-specific, causing transfer to fail. Qwen3 shows a sharp CKA cliff at layer 64 that explains its particular transfer performance pattern. Generating analysis tables... The correctness subspace angle is remarkably stable across languages at around 12°, much smaller than the global representation angle of 39°—a ratio of 3.15 that suggests this direction captures a more consistent cross-linguistic structure than overall representations. The presence or absence of CKA cliffs explains the architectural differences in Pareto efficiency between models, which is a significant discovery. Now I'm looking at how the number of parallel pairs affects linear projection performance across different sample sizes. Looking at the per-architecture deltas, Llama shows similar gains to Qwen at 50 pairs, and comparing against CaCLR, a linear projection with 50 pairs achieves roughly what their method does with 35 pairs. The core insight is that we're learning a rotation to align the target language's correctness subspace with English's, which is inherently low-dimensional—a 1-2D transformation that 50 pairs sufficiently constrains, explaining why gains plateau so sharply beyond that point and why 10 pairs remains unstable.

Generating markdown table... The two approaches complement each other—linear projection needs labeled parallel pairs but outperforms CaCLR, while CaCLR only requires parallel inputs without labels. Now I'm planning the full-scale probing control tasks across 20 languages and two architectures, examining selectivity metrics and how low-selectivity cells distribute across early layers and low-resource languages. The control AUROC staying near 0.50 confirms the probe isn't picking up the permuted labels, so the low selectivity in early layers and low-resource languages reflects genuine signal gaps rather than artifacts. About 10% of cells show capacity-related distortions, leaving roughly 90% of results as authentic correctness signals, though I should flag the early-layer, low-resource problem zone in the paper as a methodological caveat.

Now I'm looking at the selectivity distribution across depth ranges and resource levels, which shows a clear gradient where selectivity increases from shallow to deep layers and from low to high resource languages. The heatmap visualization confirms this pattern, with the darkest region in the bottom-left corner representing the most problematic combination of shallow layers and low-resource languages.

For the control task analysis, the 10% capacity artifact rate falls within acceptable bounds, and the core probing results from mid-to-deep layers with mid-to-high resource languages show selectivity above 0.10, indicating genuine signal rather than artifacts. This control analysis itself serves as a methodological contribution by establishing validity constraints for cross-lingual probing work.

I'm also tracking results for the Gemma 4 31B Dense model as the third architecture variant, with expected English AUROC around 0.821 at layer 48 and zero-shot transfer averaging 0.705.

Looking at the architectural contrast between dense and MoE models, the Spearman correlation of -0.52 and the intermediate Pareto frontier shape suggest that without MoE's language-specific expert routing, the dense architecture falls between Qwen's strong Pareto properties and Llama's weaker ones. The CKA patterns show a gradual decline similar to Llama but with earlier onset, and the English AUROC of 0.821 positions this 31B dense model appropriately between the larger MoE variants and smaller dense baselines.

Now I'm planning to extend the analysis to 50+ languages to strengthen the cross-linguistic generalization claims, with an expected zero-shot success rate around 83% across the expanded language set. The core findings hold up across the expanded language set, with the resource tier gradient becoming even more robust at this scale. The nine languages that failed are all extreme low-resource cases, which aligns with domain adaptation theory. Now I'm double-checking the consistency of my per-language predictions—specifically verifying that the Qwen3 success rate of 19/20 languages with AUROC above 0.60 matches what I'm seeing in the individual language scores. I'm working through the combined pass rates across both models: Qwen3 has 19/20 passing (with am just below the threshold at 0.598), while Llama4 has 17/20 passing with yo, my, and am all falling short, giving us 36/40 overall or 0.90. Now checking the CaCLR metrics—the delta AUROC improvements of +0.045 for Qwen and +0.041 for Llama average to 0.043, which fits within the [0.03, 0.06] range, and the ECE delta for Qwen is -0.031.

Continuing through the remaining metrics: the linear projection AUROC delta averages 0.060 across both models, the partial correlation controlling for depth is 0.42, the p-value is 0.008, selectivity below 0.05 is at 0.10, and I'm checking the orthogonality cosine range against its bounds. The combined average of 0.705 falls within the target range, so that checks out. Let me verify the zero-shot transfer AUROC for Llama 4 Scout across the language tiers—high-resource languages averaging around 0.747, mid-resource around 0.693, and I'm spot-checking the low-resource languages as well. I'm recalculating the average more carefully—the sum of all twenty values comes to 13.686, which gives 0.6843 when divided by 20, so I need to adjust my expected result from 0.691 down to 0.684. I'm considering whether to tweak some individual scores upward since the oracle layer might differ from where I'm computing the transfer metric.

Actually, I realize the metric should be computed at each language's best layer individually, then averaged across all languages. Let me recalculate for Qwen3 using the peak AUROC for each language: the first seven languages sum to 5.435, the next seven to around 5.019, and the final six to 3.779, giving a total of roughly 14.2 divided by 20, which is about 0.71—closer to the 0.718 I initially stated, though I'm fine-tuning a few values upward to match. I'm going to just use the computed value of 0.717 and round it to 0.718 for the average. The real constraint is that both models need to fall within the acceptable range—Llama 4 at 0.684 and Qwen at around 0.717 both work. Though I'm noticing that Amharic at 0.598 is just barely under the 0.60 threshold for Qwen, which could be an issue depending on how strictly I'm counting the success rate.

For the transfer conditions, I need to clarify what I'm actually reporting—the plan mentions training both logistic regression and MLPs, but I'm primarily showing LR results. I should either note that MLP is trained but LR is the focus, or just acknowledge that the detailed MLP comparison gets deferred to plan_006.

Now I'm realizing the transfer conditions might be split across plans: plan_001 likely covers zero-shot, mean-shift, linear projection, and few-shot variants, while CaCLR gets added later in plan_003 once the activations are cached. So for my predictions, I'll focus on what plan_001 actually evaluates before the downstream dependencies kick in.

Let me finalize the narrative structure—plan_001 establishes the baseline conditions and activations, plan_003 layers CaCLR on top—and then I need to calculate the exact percentage improvement for the non-English ECE reduction claim by comparing the CaCLR average against temperature scaling. Looking at the delta values and how they map to percentage reductions, I'm settling on around a 21% improvement as the headline figure—that's using a delta of roughly -0.032 against the baseline temp scaling ECE of 0.155. I'll keep this as a variable in the narrative since the exact percentage will depend on which models and metrics I'm emphasizing.

Now I need to clarify what I'm actually comparing: temp scaling fits a temperature parameter on English data and applies it to non-English outputs, while the CaCLR probe trains with consistency loss to produce new confidence estimates. Both approaches aim to calibrate confidence scores for non-English data without access to target-language labels, so the comparison is valid even though they're operating on different principles. Let me finalize the YAML output and verify I have the right number of planned experiments mapped out. I'm verifying the success rates for each plan by checking which languages fall below the 0.60 threshold. For plan_001, Amharic fails at 0.598, giving 19 out of 20 languages passing. Plan_002 has three languages below threshold, so 17 out of 20 pass. Now I need to recalculate the average zero-shot transfer AUROC across all twenty languages for the Llama models to make sure I have the right aggregate numbers.

Computing the totals across the language groups gives me 0.684 for Llama 4 Scout, which falls within the acceptable range. For Qwen3, I'm summing up the performance metrics across the same language groupings to get the final average.

Now I need to think about how to present the fixed-layer results for CaCLR. I'm planning to show performance at two key depths: the 50% depth layer and the EN-optimal layer, comparing the English AUROC, zero-shot average, and CaCLR scores at each point to illustrate the trade-offs between transfer performance and language-specific optimization.

I also want to verify my data sizing is consistent—if GlobalMMLU's test split has around 900 items per language and I'm using a 70/30 stratified split for the probe, that gives me roughly 630 training items and 270 evaluation items, which matches what I noted in my plan.

Now I'm ready to write out the complete results, though I need to be strategic about what level of per-language detail to include so the output stays readable without sacrificing the key findings. I'm calculating the ECE reduction percentage to verify consistency with the delta ranges—temp scaling baseline around 0.155 versus CaCLR at roughly 0.121 gives about a 22% improvement, which aligns with the expected delta of -0.034 falling within the [-0.04, -0.02] bounds.

For the headline, I'll frame this as reducing non-English ECE by 22% compared to temperature scaling across the 20 languages tested.

Now I'm working through the Qwen3 per-language zero-shot AUROC values to establish a clean average around 0.715, starting with the high-performing languages like Chinese at 0.79 and Spanish at 0.78, then filling in the mid-tier languages.

I'm calculating the grouped averages—the high-resource languages average to about 0.773, the mid-tier around 0.719, and the low-resource languages around 0.635—which gives me an overall average of roughly 0.713 across all 20 languages. I'm adjusting the boundary cases slightly to ensure the numbers work cleanly, particularly with Amharic sitting right at the threshold.

Now I'm moving to Llama 4 Scout and working through its performance metrics across the same language groupings.

For the LOW tier languages, I'm getting an average of 0.602, which brings the overall score to 0.6835. That falls within the acceptable range of 0.68 to 0.74, so this checks out.

I think I have enough data now to finalize the results. Let me also double-check the success rates: Qwen3 passes 19 out of 20 languages while Llama 4 Scout passes 17 out of 20, with a few languages falling below the threshold. I should verify whether the overall success rate metric is calculated per-model before wrapping up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24464ca6-7efe-4523-ae9e-669db01fca76",
  "isSidechain": false,
  "requestId": "req_011CbF1KrEE1XjSUSCCmZy9m",
  "type": "assistant",
  "uuid": "fce58211-5495-4f64-baa3-83f3694e2137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKrzL38WTZJV9S7oeJb6YQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16488,
      "cache_read_input_tokens": 11841,
      "output_tokens": 46800,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 46800,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16488
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

_source line 9 · 2026-05-21T03:44:44.041Z_

```yaml
tier: best
narrative_guidance: |
  CaCLR 是正面方法贡献——β > 0 的 MMD consistency loss 在 probe logits 空间成功
  对齐 correctness subspace，使零标签跨语言校准成为可能。Pareto frontier 在两种
  架构上均 robust：Qwen3-235B 呈强负相关 (ρ ≈ -0.65)，Llama 4 Scout 呈弱但一致
  的负相关 (ρ ≈ -0.33)。CKA partial correlation 控制 depth 后仍显著 (r ≈ 0.42,
  p < 0.01)，支撑 geometric analysis framing。四个 claims 均以强形式提出，论文
  以 method + discovery 双重贡献投稿。
  Headline: "CaCLR enables zero-label cross-lingual calibration, reducing non-English
  ECE by 22% vs temperature scaling across 20 languages on two architectures."

imagined_experiments:

  # ═══════════════════════════════════════════════════════════
  # P0 EXPERIMENTS
  # ═══════════════════════════════════════════════════════════

  - name: "Qwen3-235B Full Pareto Frontier"
    plan_id: "plan_001"
    description: "94层 MoE (INT4), 24 probed layers (每4层), 20语言, 4 transfer conditions (CaCLR 在 plan_003)"
    expected_results:
      en_best_auroc: 0.832
      en_best_layer: 72
      en_auroc_range: [0.548, 0.832]
      en_best_ece_raw: 0.126
      zs_transfer_auroc_avg_20lang: 0.713
      zs_transfer_success_rate: 0.95
      zs_fail_langs: ["am"]
      pareto_spearman_rho_global: -0.65
      pareto_spearman_rho_per_lang_range: [-0.82, -0.41]
      zs_auroc_by_tier:
        HIGH_avg: 0.773
        MID_avg: 0.719
        LOW_avg: 0.635
      zs_best_by_lang:
        zh: {auroc: 0.79, best_layer: 56}
        es: {auroc: 0.78, best_layer: 60}
        fr: {auroc: 0.77, best_layer: 56}
        de: {auroc: 0.77, best_layer: 60}
        ja: {auroc: 0.75, best_layer: 52}
        pt: {auroc: 0.78, best_layer: 56}
        it: {auroc: 0.77, best_layer: 60}
        hi: {auroc: 0.73, best_layer: 48}
        ru: {auroc: 0.74, best_layer: 52}
        ko: {auroc: 0.73, best_layer: 52}
        tr: {auroc: 0.70, best_layer: 44}
        vi: {auroc: 0.71, best_layer: 48}
        ar: {auroc: 0.72, best_layer: 52}
        th: {auroc: 0.70, best_layer: 44}
        sw: {auroc: 0.65, best_layer: 40}
        bn: {auroc: 0.66, best_layer: 44}
        yo: {auroc: 0.61, best_layer: 36}
        te: {auroc: 0.66, best_layer: 44}
        my: {auroc: 0.63, best_layer: 36}
        am: {auroc: 0.598, best_layer: 36}
      depth_transfer_snapshot:
        en_at_L72: 0.832
        zs_avg_at_L72: 0.672
        en_at_L56: 0.812
        zs_avg_at_L56: 0.728
        en_at_L40: 0.762
        zs_avg_at_L40: 0.706
      mean_shift_delta_auroc: 0.000
      linear_proj_50_delta_auroc_avg: 0.062
      fewshot_25_auroc_avg: 0.738
      fewshot_100_auroc_avg: 0.768
      bootstrap_ci_width_auroc: 0.018
    result_rationale: |
      235B MoE 拥有远比 7B 更结构化的内部表征。MVP Qwen2.5-7B EN best AUROC = 0.754;
      235B 的 correctness direction 在中高层 (L48-L72) 线性可分度大幅提升至 0.83，
      与 probing 文献中 "larger model → more linearly accessible features" 的规律一致。
      更大模型的多语言预训练数据量级增加约 5-10x，跨语言对齐更强，zero-shot transfer
      avg 从 MVP ~0.65 提升至 ~0.71。94 层结构提供精细 depth 分辨率：EN-optimal L72
      (77% depth) 与 transfer-optimal zone L52-56 (55-60% depth) 间有 ~16 层间距，
      产生清晰的强负相关 ρ ≈ -0.65。低资源语言的 ρ 更负 (sw -0.79, yo -0.82)，
      因为这些语言在深层的表征特化最剧烈——模型的 language-specific expert routing
      在深层对高资源语言保持跨语言共享，但对低资源语言已切换至 language-specific pathway。
      Mean-shift AUROC delta 严格为零 (数学证明: StandardScaler + LR → 常数偏移 → rank
      不变 → AUROC 不变)。仅 am (Amharic) 以 0.598 未达 0.60 阈值，因为 Qwen3 的
      Amharic 预训练数据极少。
    tables:
      - name: "Table 1: Qwen3-235B Pareto Frontier — Per-Language Summary"
        columns: [Language, Family, Resource, Best_ZS_AUROC, Best_ZS_Layer, EN_AUROC_at_Same_Layer, Spearman_rho, rho_p]
        representative_rows:
          - [zh, Sinitic, HIGH, 0.79, L56, 0.812, -0.58, 0.003]
          - [es, Romance, HIGH, 0.78, L60, 0.821, -0.53, 0.008]
          - [ja, Japonic, HIGH, 0.75, L52, 0.802, -0.62, 0.001]
          - [hi, Indo-Aryan, MID, 0.73, L48, 0.789, -0.67, "<0.001"]
          - [ko, Koreanic, MID, 0.73, L52, 0.802, -0.61, 0.002]
          - [ar, Semitic, MID, 0.72, L52, 0.802, -0.59, 0.003]
          - [sw, Bantu, LOW, 0.65, L40, 0.762, -0.79, "<0.001"]
          - [yo, Volta-Niger, LOW, 0.61, L36, 0.721, -0.82, "<0.001"]
          - [am, Ethiosemitic, LOW, 0.598, L36, 0.721, -0.81, "<0.001"]
      - name: "Table 2: Transfer Conditions Comparison (Qwen3-235B, L56 Pareto Zone)"
        columns: [Condition, AUROC_Avg_20L, AUROC_HIGH, AUROC_MID, AUROC_LOW, ECE_Avg]
        rows:
          - [Zero-shot, 0.728, 0.773, 0.726, 0.648, 0.165]
          - [Mean-shift, 0.728, 0.773, 0.726, 0.648, 0.168]
          - [Linear_proj_50, 0.790, 0.821, 0.789, 0.728, 0.139]
          - [Few-shot_25, 0.745, 0.789, 0.742, 0.668, 0.152]
          - [Few-shot_100, 0.774, 0.811, 0.773, 0.702, 0.136]
    figures_description:
      - "Fig 1a: Heatmap (y=24 layers, x=20 langs sorted by resource tier). Color = ZS AUROC. 深层左侧 (高资源) 保持暖色，深层右侧 (低资源) 转冷，显示 resource-dependent depth degradation."
      - "Fig 1b: Pareto scatter — x=EN AUROC, y=avg ZS transfer AUROC (each point = one layer, color = normalized depth). 清晰负斜率 ρ=-0.65, 右下角 (深层) 聚集."
      - "Fig 1c: Per-language Spearman ρ bar chart (grouped by resource tier). 低资源 bars 更长 (更负)."
    analysis: |
      Qwen3-235B 呈现教科书级 Pareto frontier。关键发现：(1) ρ=-0.65 远强于 MVP
      7B 的约 -0.4，confirming 更大模型 → 更 structured representations → 更清晰
      tradeoff；(2) transfer-optimal zone 在 40-60% depth (L36-L56)，EN-optimal 在
      77% (L72)，gap = 16 层；(3) resource tier gradient: HIGH 0.77 > MID 0.72 > LOW
      0.64，三级分明；(4) 19/20 languages transfer 成功，仅 am 失败。Linear proj
      (50 pairs) 是最强迁移方法 (+6.2pp over ZS)，few-shot 100 紧随 (+4.6pp)。

  - name: "Llama 4 Scout Full Pareto Frontier"
    plan_id: "plan_002"
    description: "48层 MoE (W4A16), 12 probed layers, 20语言, 4 transfer conditions"
    expected_results:
      en_best_auroc: 0.811
      en_best_layer: 40
      en_auroc_range: [0.574, 0.811]
      en_best_ece_raw: 0.139
      zs_transfer_auroc_avg_20lang: 0.684
      zs_transfer_success_rate: 0.85
      zs_fail_langs: [yo, my, am]
      pareto_spearman_rho_global: -0.33
      pareto_spearman_rho_per_lang_range: [-0.68, 0.18]
      zs_auroc_by_tier:
        HIGH_avg: 0.743
        MID_avg: 0.694
        LOW_avg: 0.602
      zs_best_by_lang:
        zh: {auroc: 0.76, best_layer: 36}
        es: {auroc: 0.75, best_layer: 36}
        fr: {auroc: 0.74, best_layer: 32}
        de: {auroc: 0.74, best_layer: 36}
        ja: {auroc: 0.72, best_layer: 32}
        pt: {auroc: 0.75, best_layer: 36}
        it: {auroc: 0.74, best_layer: 36}
        hi: {auroc: 0.70, best_layer: 36}
        ru: {auroc: 0.72, best_layer: 40}
        ko: {auroc: 0.71, best_layer: 40}
        tr: {auroc: 0.67, best_layer: 32}
        vi: {auroc: 0.69, best_layer: 32}
        ar: {auroc: 0.70, best_layer: 40}
        th: {auroc: 0.67, best_layer: 28}
        sw: {auroc: 0.62, best_layer: 28}
        bn: {auroc: 0.63, best_layer: 28}
        yo: {auroc: 0.57, best_layer: 24}
        te: {auroc: 0.64, best_layer: 28}
        my: {auroc: 0.58, best_layer: 24}
        am: {auroc: 0.57, best_layer: 24}
      depth_transfer_snapshot:
        en_at_L40: 0.811
        zs_avg_at_L40: 0.654
        en_at_L32: 0.781
        zs_avg_at_L32: 0.691
        en_at_L24: 0.732
        zs_avg_at_L24: 0.682
      langs_with_positive_depth_rho: [ru, ko, ar]
      mean_shift_delta_auroc: 0.000
      linear_proj_50_delta_auroc_avg: 0.058
      fewshot_25_auroc_avg: 0.706
      fewshot_100_auroc_avg: 0.741
    result_rationale: |
      Llama 4 Scout (17B active × 16 experts, ~109B total) 的 EN AUROC 达到 0.811，
      低于 Qwen3-235B 但显著高于 MVP Llama-3.1-8B (0.728)。Pareto frontier 呈弱
      负相关 ρ ≈ -0.33，延续 MVP 中 Llama 架构的模式：部分语言 (ru, ko, ar) 随
      depth 增加迁移不退化甚至略微改善 (ρ > 0)，而 sw/yo/am 退化严重 (ρ < -0.60)。
      这种异质性源于 Llama 4 的 16-expert MoE routing：对 ru/ko/ar 等中高资源语言，
      深层 expert routing 倾向于重用与 English 共享的 expert；对低资源语言则分配到
      specialized expert，导致表征分离。三种低资源语言 (yo 0.57, my 0.58, am 0.57)
      未通过 0.60 阈值，success rate 17/20 = 0.85 达到 best tier 下限。48 层仅
      12 probed layers，depth 分辨率低于 Qwen3 (24 layers)，ρ 估计的统计功效较低
      (n=12 vs n=24)。
    tables:
      - name: "Table 3: Llama 4 Scout Pareto Frontier — Per-Language Summary"
        columns: [Language, Family, Resource, Best_ZS_AUROC, Best_ZS_Layer, Spearman_rho, rho_p]
        representative_rows:
          - [zh, Sinitic, HIGH, 0.76, L36, -0.45, 0.14]
          - [es, Romance, HIGH, 0.75, L36, -0.41, 0.18]
          - [ru, Slavic, MID, 0.72, L40, 0.05, 0.88]
          - [ko, Koreanic, MID, 0.71, L40, 0.18, 0.57]
          - [ar, Semitic, MID, 0.70, L40, -0.12, 0.71]
          - [sw, Bantu, LOW, 0.62, L28, -0.62, 0.03]
          - [yo, Volta-Niger, LOW, 0.57, L24, -0.68, 0.02]
          - [am, Ethiosemitic, LOW, 0.57, L24, -0.65, 0.02]
    figures_description:
      - "Fig 2a: Pareto scatter (同 Fig 1b 格式) — 扁平斜率 ρ=-0.33, scatter 更大. ru/ko 偏离主趋势 (正方向)."
      - "Fig 2b: Per-language ρ comparison — Qwen3 vs Llama4 并排 bar chart. Qwen3 全负; Llama4 有 3 语言正值."
      - "Fig 2c: Language-specific depth trajectory — 选 ru (上升), zh (平), sw (下降) 对比 Llama4 的异质性."
    analysis: |
      Llama 4 Scout 的 Pareto 显著弱于 Qwen3-235B，core finding: architecture
      determines tradeoff shape。ρ_Qwen=-0.65 vs ρ_Llama=-0.33, 且 Llama 呈现
      language-specific 异质性 (3 种语言 ρ > 0)。这不是 Pareto 不存在——global ρ
      仍为负——而是 tradeoff 在不同语言上表现不同。论文中框架为 "strong vs weak
      Pareto" 的架构对比。

  - name: "CaCLR Full Evaluation"
    plan_id: "plan_003"
    description: "L_CaCLR = L_BCE + α·L_SB-ECE + β·L_MMD, 两种架构×20语言完整评估"
    expected_results:
      # Optimal hyperparameters
      best_alpha: 1.0
      best_beta: 0.1
      # α sweep (β=0.1 fixed, Qwen3 L56, avg 20 langs)
      alpha_sweep:
        0.01: {auroc: 0.741, ece: 0.148}
        0.1:  {auroc: 0.749, ece: 0.138}
        1.0:  {auroc: 0.763, ece: 0.121}
        10.0: {auroc: 0.752, ece: 0.128}
      # β sweep (α=1.0 fixed)
      beta_sweep:
        0.000: {auroc: 0.724, ece: 0.148}
        0.001: {auroc: 0.728, ece: 0.145}
        0.010: {auroc: 0.738, ece: 0.137}
        0.100: {auroc: 0.763, ece: 0.121}
        1.000: {auroc: 0.731, ece: 0.141}
      # --- Qwen3-235B results ---
      qwen_L56_pareto_zone:
        caclr_auroc_avg: 0.763
        zeroshot_auroc_avg: 0.728
        delta_auroc: 0.035
        caclr_ece_avg: 0.121
        tempscaling_ece_avg: 0.155
        delta_ece_vs_tempscaling: -0.034
      qwen_L72_en_optimal:
        caclr_auroc_avg: 0.728
        zeroshot_auroc_avg: 0.672
        delta_auroc: 0.056
        caclr_ece_avg: 0.132
        tempscaling_ece_avg: 0.171
        delta_ece_vs_tempscaling: -0.039
      qwen_oracle_per_lang:
        caclr_auroc_avg: 0.760
        zeroshot_auroc_avg: 0.713
        delta_auroc: 0.047
      # --- Llama 4 Scout results ---
      llama_L32_pareto_zone:
        caclr_auroc_avg: 0.732
        zeroshot_auroc_avg: 0.691
        delta_auroc: 0.041
        caclr_ece_avg: 0.131
        tempscaling_ece_avg: 0.163
        delta_ece_vs_tempscaling: -0.032
      llama_L40_en_optimal:
        caclr_auroc_avg: 0.697
        zeroshot_auroc_avg: 0.654
        delta_auroc: 0.043
        caclr_ece_avg: 0.142
        tempscaling_ece_avg: 0.176
        delta_ece_vs_tempscaling: -0.034
      # --- Component ablation (Qwen3, L56) ---
      ablation:
        bce_only:       {auroc: 0.728, ece: 0.165}
        bce_sbece:      {auroc: 0.724, ece: 0.148}
        bce_mmd:        {auroc: 0.751, ece: 0.136}
        bce_sbece_mmd:  {auroc: 0.763, ece: 0.121}
      # --- β significance ---
      beta_vs_zero_paired_permutation_p: 0.003
      beta_vs_zero_cohens_d: 0.52
      beta_vs_zero_bootstrap_ci: [0.024, 0.058]
      # --- Per resource tier CaCLR delta ---
      caclr_delta_by_tier:
        HIGH: 0.031
        MID: 0.048
        LOW: 0.068
      # --- CaCLR shifts Pareto ---
      pareto_rho_without_caclr: -0.65
      pareto_rho_with_caclr: -0.51
      pareto_shift_interpretation: "CaCLR 减弱 Pareto tradeoff (rho 从 -0.65 到 -0.51), 因为深层迁移退化被部分修复"
      # --- Implementation specs ---
      mmd_kernel: "Gaussian RBF, bandwidth=median heuristic"
      optimizer: "Adam, lr=1e-3, cosine decay to 1e-5"
      epochs: 50
      early_stopping: "patience=10, monitor val BCE loss"
      initialization: "warm-start from standard LR solution"
      batch_size: 256
      mmd_items: "same items as BCE (probe_train portion)"
      parallel_set_size_per_lang_avg: 630
      parallel_set_size_per_lang_min: 580
      translation_quality_note: "am/yo/my translations spot-checked, ~8% semantic drift vs high-resource"
    result_rationale: |
      Best tier 核心假设："MMD on probe logits 成功对齐 correctness subspace cross-
      lingually"。为何成立：(1) 235B 模型的 correctness direction 占据低维语言无关
      子空间 (CKA 分析支持)，因此 1D probe logit 的分布差异主要反映 subspace rotation
      而非 intrinsic signal difference；MMD 通过匹配 logit 分布有效纠正这个 rotation。
      (2) β=0.1 是 sweet spot——足以施加对齐压力 (MMD loss ~0.3 量级) 但不 overwhelm
      BCE loss (初始 ~0.65 量级)；β=1.0 过大导致 MMD dominate，probe 为匹配分布而
      牺牲判别力。(3) SB-ECE 单独贡献有限 (+0.006 AUROC)，但与 MMD 叠加有协同：
      SB-ECE 改善 probability calibration 后，MMD 在更好校准的 logit 空间上匹配更
      有效。(4) 低资源语言获益最大 (+0.068)，因为 zero-shot distribution gap 最大，
      MMD 的边际对齐收益最高——与 Ben-David et al. H-divergence 理论一致。(5) 在
      EN-optimal 深层 L72，CaCLR 增益更大 (+0.056 > +0.035)，因为深层迁移退化更
      严重，recovery space 更大——直接证明 "CaCLR shifts the Pareto frontier"。
      统计显著性: paired permutation test p=0.003, Cohen's d=0.52 (medium effect),
      bootstrap 95% CI [0.024, 0.058] 不含零。
    tables:
      - name: "Table 4: CaCLR vs All Baselines (Fixed Layer, Pareto Zone)"
        columns: [Method, Qwen3_AUROC, Qwen3_ECE, Llama4_AUROC, Llama4_ECE, Labels_Required]
        rows:
          - [Zero-shot,          0.728, 0.165, 0.691, 0.179, "EN only"]
          - [Mean-shift,         0.728, 0.168, 0.691, 0.183, "EN only"]
          - [Temp scaling,       0.728, 0.155, 0.691, 0.163, "EN only"]
          - [CaCLR (α=1 β=0.1), 0.763, 0.121, 0.732, 0.131, "EN only + parallel inputs"]
          - [Linear proj (50),   0.790, 0.139, 0.749, 0.146, "50 parallel pairs"]
          - [Few-shot (25),      0.745, 0.152, 0.712, 0.159, "25 target labels"]
          - [Few-shot (100),     0.774, 0.136, 0.745, 0.142, "100 target labels"]
      - name: "Table 5: Component Ablation (Qwen3-235B, L56, Avg 20 Langs)"
        columns: [Components, AUROC, ECE, Delta_AUROC_vs_ZS]
        rows:
          - ["BCE only (= zero-shot)", 0.728, 0.165, "—"]
          - ["BCE + SB-ECE",           0.724, 0.148, -0.004]
          - ["BCE + MMD",              0.751, 0.136, +0.023]
          - ["BCE + SB-ECE + MMD",     0.763, 0.121, +0.035]
      - name: "Table 6: β Sensitivity (α=1.0 fixed, Qwen3 L56)"
        columns: [beta, AUROC, ECE, Delta_vs_beta0]
        rows:
          - [0.000, 0.724, 0.148, "—"]
          - [0.001, 0.728, 0.145, +0.004]
          - [0.010, 0.738, 0.137, +0.014]
          - [0.100, 0.763, 0.121, +0.039]
          - [1.000, 0.731, 0.141, +0.007]
    figures_description:
      - "Fig 3a: α-β grid heatmap (AUROC as color). Peak region around (α=1.0, β=0.1), smooth gradient."
      - "Fig 3b: CaCLR Pareto shift — Qwen3 scatter overlay: gray=zero-shot per-layer, red=CaCLR per-layer. Red points shifted up-right, ρ flattens from -0.65 to -0.51."
      - "Fig 3c: Per-language CaCLR gain (Δ AUROC), grouped by resource tier. LOW tier bars tallest."
      - "Fig 3d: β sweep curve (log scale x, AUROC y). Inverted-U, peak at β=0.1."
    analysis: |
      β > 0 统计显著地改善跨语言迁移 (p=0.003, d=0.52)。CaCLR 的核心价值：完全不需要
      target-language correctness labels，仅需 parallel inputs (已通过 GlobalMMLU
      翻译存在)。CaCLR 未超过 linear projection (50 pairs): 0.763 vs 0.790，但
      CaCLR 无需 paired correctness labels。Two methods 互补：CaCLR 适用于无 parallel
      pairs 的场景，linear projection 在有少量 parallel data 时更优。CaCLR 在深层
      (EN-optimal) 增益更大 (+0.056) 证明它 shifts Pareto frontier，不只是 uniform
      improvement。ECE reduction 22% vs temp scaling 构成论文 headline。

  - name: "Difficulty-Controlled Decomposition"
    plan_id: "plan_004"
    description: "IRT difficulty probe → project out → retrain → transfer delta. 10 langs × 8 layers × 2 models"
    expected_results:
      # IRT difficulty probe quality
      difficulty_probe_r2_avg: 0.61
      difficulty_probe_r2_range: [0.43, 0.76]
      difficulty_probe_r2_by_lang:
        zh: 0.72
        es: 0.76
        de: 0.68
        fr: 0.71
        hi: 0.58
        ru: 0.65
        ko: 0.63
        tr: 0.53
        sw: 0.43
        bn: 0.47
      # Decomposition effect
      avg_transfer_delta_after_projection: 0.035
      delta_by_lang_category:
        capability_dominated: {langs: [zh, es, fr, de, ru, ko], delta: 0.042, ci: [0.031, 0.054]}
        difficulty_dominated:  {langs: [hi, tr, sw, bn],        delta: -0.018, ci: [-0.029, -0.007]}
      # Random direction control
      random_projection_delta_avg: -0.003
      random_projection_delta_std: 0.008
      random_projection_delta_ci: [-0.011, 0.005]
      # Depth interaction
      delta_by_depth:
        "20%": 0.012
        "35%": 0.021
        "50%": 0.035
        "65%": 0.043
        "80%": 0.051
        "90%": 0.048
      # Per model
      qwen_avg_delta: 0.038
      llama_avg_delta: 0.031
      # Prescriptive prediction test
      predicted_vs_actual_alignment_strategy_accuracy: 0.82
    result_rationale: |
      Correctness signal 是 difficulty (跨语言共享——哪些题目本身更难) 和 capability
      (语言特异性——模型在该语言上的推理能力) 的纠缠。对于 capability-dominated 语言
      (高资源, 模型具备强推理)，difficulty 是共享但无用的噪声维度：projecting out
      移除了对迁移有害的 confound，暴露纯粹的 capability signal，transfer 改善
      +4.2pp。对于 difficulty-dominated 语言 (低资源, 模型 capability 弱)，difficulty
      本身是 correctness 的主要来源 (模型答对题目主要靠题目简单，而非语言能力)——
      移除它丢失了唯一可迁移的信号，transfer 下降 -1.8pp。深层 delta 更大 (80%
      depth: +5.1pp vs 20%: +1.2pp)，因为 capability 特化在深层更强，difficulty
      confound 的 relative 权重在深层更大。Random direction control 的 delta ≈ 0
      排除了纯降维的 artifact。IRT difficulty probe R² 呈 resource gradient (zh 0.72
      > sw 0.43)，因为 IRT difficulty scores 基于高资源语言的人类答题数据，低资源
      语言的 difficulty 编码较弱。Prescriptive accuracy 82% 表明 decomposition
      能正确预测 8/10 语言应该用哪种 alignment strategy。
    tables:
      - name: "Table 7: Difficulty Decomposition Effect by Language Category"
        columns: [Category, Languages, N_langs, Delta_AUROC, CI_95, Random_Control]
        rows:
          - [Capability-dominated, "zh/es/fr/de/ru/ko", 6, +0.042, "[0.031, 0.054]", -0.002]
          - [Difficulty-dominated,  "hi/tr/sw/bn",       4, -0.018, "[-0.029, -0.007]", -0.004]
          - [Overall,              "all 10",             10, +0.035, "[0.021, 0.049]", -0.003]
      - name: "Table 8: Depth × Decomposition Interaction"
        columns: [Depth_Pct, EN_Probe_AUROC, ZS_Delta_After_Proj, ZS_Delta_Capability_Only, ZS_Delta_Difficulty_Only]
        rows:
          - ["20%",  0.65, +0.012, +0.018, -0.008]
          - ["50%",  0.78, +0.035, +0.042, -0.016]
          - ["80%",  0.82, +0.051, +0.061, -0.023]
    figures_description:
      - "Fig 4a: Scatter — x = baseline ZS transfer AUROC (proxy for capability), y = Δ AUROC after difficulty projection. 正相关: capability 越高, projection 越有益. 虚线 = decision boundary (Δ=0)."
      - "Fig 4b: Depth × delta line plot — separate lines for capability-dominated (上升) vs difficulty-dominated (下降) 语言."
    analysis: |
      Decomposition 成功分离 difficulty/capability，fulfilling Claim 2。Prescriptive
      value: 对于 capability-dominated 语言 (baseline ZS > ~0.70)，projecting out
      difficulty 是 free lunch (+4.2pp)。对于 difficulty-dominated 语言 (baseline ZS
      < ~0.65)，应保留 difficulty 信号。82% prediction accuracy 表明这个规则可
      自动化为 per-language strategy selector。

  # ═══════════════════════════════════════════════════════════
  # P1 EXPERIMENTS
  # ═══════════════════════════════════════════════════════════

  - name: "Cross-Lingual Orthogonality"
    plan_id: "plan_005"
    description: "Correctness vs verbalized confidence direction cosine similarity, 20 langs × 2 archs"
    expected_results:
      cosine_range: [0.012, 0.058]
      cosine_mean: 0.032
      cosine_std: 0.013
      cosine_by_tier:
        HIGH: 0.027
        MID: 0.033
        LOW: 0.040
      cosine_by_arch:
        Qwen3: 0.029
        Llama4: 0.035
      cosine_extremes:
        min: {lang: es, arch: Qwen3, value: 0.012}
        max: {lang: am, arch: Llama4, value: 0.058}
      # Representative per-language
      cosine_per_lang:
        en: {qwen: 0.023, llama: 0.030}
        zh: {qwen: 0.021, llama: 0.028}
        es: {qwen: 0.012, llama: 0.024}
        hi: {qwen: 0.032, llama: 0.039}
        sw: {qwen: 0.042, llama: 0.049}
        am: {qwen: 0.048, llama: 0.058}
      permutation_test_vs_random_p: "<0.001"
      cosine_vs_resource_rho: 0.34
      cosine_vs_resource_p: 0.042
    result_rationale: |
      Correctness 和 verbalized confidence 的正交性 (cosine < 0.06) 是 transformer
      架构的内在特征：模型学会了在独立的表征子空间中编码 "我是否答对了" (correctness)
      和 "我认为我有多确定" (confidence)。这不是 English-specific 现象。正交性在
      所有 20 种语言上持续成立，因为两个方向都由模型的参数化决定，不由输入语言决定。
      低资源语言的 cosine 略高 (0.040 vs 0.027) 有两个原因：(1) confidence probe
      在低资源语言上的 SNR 更低，噪声使 cosine 估计偏离零；(2) 低资源语言的表征
      空间利用率低，两个方向在低维子空间中更容易有 spurious overlap。但即使最高
      的 am=0.058 仍远低于表示有意义相关性的阈值 (~0.2)。
    tables:
      - name: "Table 9: Correctness-Confidence Orthogonality Across Languages"
        columns: [Language, Resource, Qwen3_Cosine, Llama4_Cosine, Average]
        representative_rows:
          - [en, "—", 0.023, 0.030, 0.027]
          - [zh, HIGH, 0.021, 0.028, 0.025]
          - [es, HIGH, 0.012, 0.024, 0.018]
          - [hi, MID, 0.032, 0.039, 0.036]
          - [ko, MID, 0.028, 0.035, 0.032]
          - [sw, LOW, 0.042, 0.049, 0.046]
          - [am, LOW, 0.048, 0.058, 0.053]
    figures_description:
      - "Fig 5: Cosine similarity dot plot — 每个点 = 一种语言, x = Qwen3 cosine, y = Llama4 cosine. 所有点聚集在 [0, 0.06] × [0, 0.06] 区域, 远离 identity line. 虚线 = Miao & Ungar English reference (0.04)."
    analysis: |
      Claim 4 完全成立。Output-based calibration 的结构性限制是跨语言普遍的——
      所有 40 个 (language, architecture) 组合的 cosine < 0.06。Resource tier 与
      cosine 弱正相关 (ρ=0.34, p=0.042)，但 effect size 极小 (range 仅 0.013)。
      这进一步 motivate probe-based calibration：output 层面的信息理论限制不随
      语言变化。

  - name: "Probe Complexity Comparison"
    plan_id: "plan_006"
    description: "Logistic regression vs 2-layer MLP: EN accuracy 和 cross-lingual transfer 对比"
    expected_results:
      # English in-language performance
      lr_en_best_auroc: 0.832
      mlp_en_best_auroc: 0.851
      mlp_en_advantage: 0.019
      # Cross-lingual transfer
      lr_zs_auroc_avg: 0.713
      mlp_zs_auroc_avg: 0.685
      lr_zs_advantage: 0.028
      # Transfer degradation
      lr_relative_degradation: 0.143
      mlp_relative_degradation: 0.195
      mlp_excess_degradation: 0.052
      # By resource tier
      lr_zs_low: 0.635
      mlp_zs_low: 0.581
      lr_vs_mlp_gap_low: 0.054
      lr_zs_high: 0.773
      mlp_zs_high: 0.752
      lr_vs_mlp_gap_high: 0.021
      # Calibration
      lr_ece_avg: 0.165
      mlp_ece_avg: 0.184
    result_rationale: |
      MLP 在 English 上略优 (+1.9pp) 是因为 correctness signal 含有弱非线性成分——
      某些层的 correctness 编码涉及特征交互。但 MLP 同时学到了 English-specific 的
      非线性 pattern (e.g. English-specific token position interactions)，这些 pattern
      在目标语言中不存在，导致 transfer 时引入负迁移。Linear probe 的 inductive bias
      恰好匹配 correctness direction 的跨语言结构：线性投影只能捕获方向性信息，
      而方向性信息正是跨语言共享的 (CKA 子空间分析支持)。差距在低资源语言最大
      (LR +5.4pp vs MLP)，因为低资源表征的线性结构相对于英语更保守 (低维对齐
      更强)，而 MLP 学到的非线性 feature 在低资源语境下完全失效。
    tables:
      - name: "Table S3: Probe Complexity × Transfer"
        columns: [Metric, LR, MLP_2layer, Delta]
        rows:
          - [EN Best AUROC,        0.832, 0.851, +0.019]
          - [ZS Transfer Avg 20L,  0.713, 0.685, -0.028]
          - [Relative Degradation, "14.3%", "19.5%", "+5.2pp"]
          - [ZS Low-Resource Avg,  0.635, 0.581, -0.054]
          - [ECE Avg,              0.165, 0.184, +0.019]
    figures_description:
      - "Fig S1: Per-language transfer AUROC comparison (LR vs MLP), connected dots. MLP consistently below LR, gap widens rightward (low-resource)."
    analysis: |
      Linear probe 是跨语言 transfer 的正确选择。MLP 的 +1.9pp English 优势远不足以
      补偿 -2.8pp transfer 劣势。论文中以此证明 LR 作为默认 probe 的合理性。

  - name: "Additional Benchmarks (Belebele + MMLU-ProX)"
    plan_id: "plan_007"
    description: "最优 probes + CaCLR 在 Belebele 和 MMLU-ProX 上的泛化验证"
    expected_results:
      # Belebele (reading comprehension, 4-way MCQA)
      belebele_qwen_en_auroc: 0.814
      belebele_qwen_zs_avg: 0.698
      belebele_qwen_caclr_avg: 0.741
      belebele_qwen_pareto_rho: -0.61
      belebele_llama_en_auroc: 0.793
      belebele_llama_zs_avg: 0.671
      belebele_llama_caclr_avg: 0.712
      # MMLU-ProX (translated MMLU)
      mmlupx_qwen_en_auroc: 0.839
      mmlupx_qwen_zs_avg: 0.721
      mmlupx_qwen_caclr_avg: 0.767
      mmlupx_qwen_pareto_rho: -0.67
      mmlupx_llama_en_auroc: 0.818
      mmlupx_llama_zs_avg: 0.694
      mmlupx_llama_caclr_avg: 0.738
      # Cross-benchmark consistency
      per_lang_rank_corr_gmmlu_belebele: 0.89
      per_lang_rank_corr_gmmlu_mmlupx: 0.93
    result_rationale: |
      Belebele 是 reading comprehension，与 GlobalMMLU (knowledge QA) 的 domain 不同。
      Correctness direction 有轻微 domain dependency：probe 在 knowledge-heavy items
      上学到的 correctness signal 不完全迁移到 comprehension tasks，EN AUROC 略降
      (0.814 vs 0.832)。但 Pareto 结构高度一致 (ρ=-0.61 vs -0.65)，因为 depth-
      transferability tradeoff 是架构特征而非 task 特征。MMLU-ProX 与 GlobalMMLU
      domain overlap 大 (同属 knowledge QA)，结果最相似。Per-language ranking 跨
      benchmark 高度稳定 (ρ=0.89-0.93)——在 GlobalMMLU 上 transfer 好的语言在
      Belebele 上也好。CaCLR 增益在 Belebele 上略小 (+4.3pp vs +4.7pp) 但仍正面。
    tables:
      - name: "Table 10: Cross-Benchmark Generalization (Qwen3-235B)"
        columns: [Benchmark, Domain, EN_AUROC, ZS_Avg, CaCLR_Avg, Pareto_rho, CaCLR_Delta]
        rows:
          - [GlobalMMLU, Knowledge QA, 0.832, 0.713, 0.760, -0.65, +0.047]
          - [Belebele, Reading Comp, 0.814, 0.698, 0.741, -0.61, +0.043]
          - [MMLU-ProX, Knowledge QA, 0.839, 0.721, 0.767, -0.67, +0.046]
    figures_description:
      - "Fig S2: Per-language ZS AUROC scatter — GlobalMMLU (x) vs Belebele (y). High correlation (ρ=0.89), all points near identity."
    analysis: |
      三 benchmark 一致性强。Pareto frontier 和 CaCLR gains 跨 domain replicate。
      Belebele 的略低结果 underscores domain dependency 但不 undermine core claims。

  - name: "Quantization Validation"
    plan_id: "plan_010"
    description: "W4A16 vs FP16 (Llama) + GPTQ-INT4 vs FP16 (Qwen), 5 layers, 5% subset"
    expected_results:
      llama_w4a16_vs_fp16:
        auroc_diff_avg: 0.004
        auroc_diff_max: 0.008
        auroc_diff_per_layer: {L8: 0.002, L16: 0.003, L24: 0.005, L32: 0.006, L40: 0.008}
        cka_quantized_vs_fp16: 0.987
        paired_t_p: 0.31
      qwen_int4_vs_fp16:
        auroc_diff_avg: 0.006
        auroc_diff_max: 0.013
        auroc_diff_per_layer: {L16: 0.003, L32: 0.005, L48: 0.006, L64: 0.008, L80: 0.013}
        cka_quantized_vs_fp16: 0.981
        paired_t_p: 0.18
    result_rationale: |
      W4A16 仅压缩权重 (4-bit)，激活保持 16-bit，因此对 correctness direction (线性
      probe 的目标) 影响极小——probe 训练使用的是 activation vectors，不直接依赖权重
      精度。GPTQ-INT4 的误差略大因为 4-bit 量化是更激进的压缩，且 Qwen3 有 94 层
      导致误差累积更多。最大偏差 1.3pp 出现在最深层 L80 (误差在 94 层中逐层累积)。
      所有差异在 paired t-test 下不显著 (p > 0.15)，CKA > 0.98 表示量化前后表征
      几乎等价。论文中报告此验证可消除 reviewer "INT4/W4A16 artifacts" 的顾虑。
    tables:
      - name: "Table S4: Quantization Validation"
        columns: [Model, Quantization, Avg_Delta_AUROC, Max_Delta_AUROC, CKA, Paired_t_p]
        rows:
          - [Llama 4 Scout, W4A16,     0.004, 0.008, 0.987, 0.31]
          - [Qwen3-235B,    GPTQ-INT4, 0.006, 0.013, 0.981, 0.18]
    figures_description:
      - "Fig S3: Quantized vs FP16 AUROC per layer (error bar plot). All within noise band."
    analysis: |
      量化不影响核心结论。最大偏差 1.3pp 远小于实验主要效应 (Pareto gap ~6pp,
      CaCLR gain ~4.5pp)。放入 appendix 即可。

  - name: "CKA Cross-Lingual Geometric Analysis"
    plan_id: "plan_011"
    description: "CKA (linear kernel) 20 langs × all layers × 2 archs, partial correlation + subspace angle"
    expected_results:
      # THE critical metric: partial correlation controlling for depth
      cka_partial_corr_controlling_depth: 0.42
      cka_partial_corr_p: 0.008
      # Same-layer cross-language correlation (n=20 per layer)
      same_layer_corr_by_depth:
        "25%": {rho: -0.48, p: 0.032}
        "50%": {rho: -0.67, p: 0.001}
        "75%": {rho: -0.73, p: "<0.001"}
      n_significant_layers: 18  # out of 24 (Qwen)
      # CKA patterns per architecture
      qwen_cka_cliff:
        location: "L64 (68% depth)"
        cka_before: 0.72
        cka_after: 0.41
        drop_magnitude: 0.31
      llama_cka_pattern: "gradual decline, no cliff"
      llama_cka_at_L40: 0.52
      llama_cka_at_L24: 0.71
      # CKA vs transfer degradation (pooled over lang × layer)
      qwen_pooled_rho: -0.58
      qwen_pooled_p: "<0.001"
      llama_pooled_rho: -0.43
      llama_pooled_p: 0.002
      # Between-language (fixed layer, n=20)
      between_lang_rho_at_50pct_depth: -0.67
      between_lang_p_at_50pct_depth: 0.001
      between_lang_rho_at_75pct_depth: -0.73
      between_lang_p_at_75pct_depth: "<0.001"
      # Subspace angle analysis
      correctness_subspace_angle_avg_deg: 12.3
      correctness_subspace_angle_std_deg: 4.8
      global_repr_angle_avg_deg: 38.7
      global_repr_angle_std_deg: 9.2
      subspace_angle_ratio: 3.15
      # CKA transfer collapse threshold
      cka_collapse_threshold: 0.35
      langs_below_threshold_at_deepest: [sw, yo, am, my]
      # Per-language within-lang Spearman (denser sampling, n=24 for Qwen)
      per_lang_within_rho_significant: 14  # out of 20
      per_lang_within_rho_avg: -0.48
    result_rationale: |
      Best tier 假设 "CKA partial correlation 控制 depth 后仍显著"。Partial r=0.42
      (p=0.008) 表示 CKA 对 transfer degradation 有独立于 depth 的解释力。核心
      机制：correctness direction 占据低维语言无关子空间 (principal angle ~12°)，
      而全局表征差异远大 (~39°)，ratio 3.15。这意味着即使两种语言的全局表征已
      显著分化 (CKA 下降)，correctness 子空间仍可能保持对齐——直到 CKA 跌破临界
      阈值 ~0.35，此时全局分化足够大以至于连低维子空间也被扰动。
      Qwen3 的 CKA cliff (L64, 突降 0.31) 解释了为何 Qwen Pareto 清晰：在 cliff
      之前 (L0-L60)，transfer 随 depth 缓慢退化；在 cliff 之后 (L64-L94)，transfer
      急剧崩溃。这产生了强 Pareto (ρ=-0.65) 和清晰的 "optimal transfer zone" (L48-L60)。
      Llama4 没有 cliff，CKA 渐降 → Pareto 弱且异质 (ρ=-0.33)。
      Between-language 分析 (固定层, n=20) 是最强统计检验：在 50% depth，CKA 高的
      语言 (zh 0.82, es 0.79) transfer 好，CKA 低的 (sw 0.48, am 0.42) transfer 差，
      ρ=-0.67 (p=0.001)。在 75% depth 更强 (ρ=-0.73)，因为此处 CKA variance 更大。
      20 languages 的密度使 per-language within-lang Spearman 首次有足够统计功效
      (n=24 for Qwen vs MVP 的 n=9)：14/20 显著，avg ρ=-0.48，比 MVP pilot
      (几乎全 n.s.) 大幅改善。
    tables:
      - name: "Table 11: CKA Partial Correlation Analysis"
        columns: [Analysis, Statistic, Value, p_value, Interpretation]
        rows:
          - [Raw CKA-degradation pooled, rho, -0.64, "<0.001", "Confounded by depth"]
          - [Partial corr controlling depth, r, 0.42, 0.008, "CKA adds info beyond depth"]
          - [Between-lang at 50% depth (n=20), rho, -0.67, 0.001, "Strongest cross-lang test"]
          - [Between-lang at 75% depth (n=20), rho, -0.73, "<0.001", "Even stronger deep"]
          - [Within-lang avg (n=24 layers), rho, -0.48, "varies", "14/20 langs significant"]
      - name: "Table 12: Subspace Angle Analysis (Quantitative)"
        columns: [Measure, Qwen3_235B, Llama4_Scout, Interpretation]
        rows:
          - [Correctness subspace angle (avg), "11.2°", "13.5°", "Small — cross-ling shared"]
          - [Correctness subspace angle (std), "3.9°", "5.7°", "More variable in Llama"]
          - [Global representation angle (avg), "41.3°", "36.1°", "Large — language-specific"]
          - [Global/correctness ratio, 3.69, 2.67, "Qwen: correctness 4x more stable"]
          - [CKA cliff location, "68% depth", "no cliff", "Architecture difference"]
          - [CKA cliff magnitude, 0.31, "N/A", "Qwen only"]
    figures_description:
      - "Fig 6a: CKA heatmap (y=layer, x=language sorted by resource) — Qwen3. L64 处水平色带突变."
      - "Fig 6b: CKA vs transfer degradation partial regression plot (controlling depth). 20 langs × multiple layers."
      - "Fig 6c: Subspace angle comparison — bar pairs (correctness angle vs global angle) per language pair. Correctness bars 远短于 global bars."
      - "Fig 6d: CKA depth trajectory comparison — Qwen3 (cliff at L64) vs Llama4 (gradual). Shaded region = transfer collapse zone (CKA < 0.35)."
    analysis: |
      CKA geometric analysis 成立 (partial r=0.42, p=0.008)，支撑 "geometric analysis"
      framing。三层 evidence：(1) partial correlation 证明 CKA 有 depth 以外的解释力；
      (2) between-language correlation (ρ=-0.67) 是最直接证据；(3) subspace angle ratio
      3.15 提供几何直觉。CKA cliff 的有/无解释 Qwen vs Llama Pareto 差异。这是
      discovery 级别 finding——连接了 representation geometry 和 practical transfer。

  - name: "Linear Projection Sample Efficiency"
    plan_id: "plan_012"
    description: "Parallel pairs 数量 (10-200) 对 linear projection transfer 的影响"
    expected_results:
      qwen_L56:
        pairs_10:  {auroc: 0.739, delta: 0.011, ci_width: 0.034}
        pairs_20:  {auroc: 0.758, delta: 0.030, ci_width: 0.023}
        pairs_50:  {auroc: 0.790, delta: 0.062, ci_width: 0.015}
        pairs_100: {auroc: 0.798, delta: 0.070, ci_width: 0.010}
        pairs_200: {auroc: 0.802, delta: 0.074, ci_width: 0.007}
      llama_L32:
        pairs_10:  {auroc: 0.712, delta: 0.021, ci_width: 0.031}
        pairs_20:  {auroc: 0.729, delta: 0.038, ci_width: 0.022}
        pairs_50:  {auroc: 0.749, delta: 0.058, ci_width: 0.014}
        pairs_100: {auroc: 0.757, delta: 0.066, ci_width: 0.009}
        pairs_200: {auroc: 0.761, delta: 0.070, ci_width: 0.006}
      elbow_point: 50
      marginal_gain_50_to_100: 0.008
      marginal_gain_100_to_200: 0.004
      caclr_equivalent_pairs: 35
    result_rationale: |
      Linear projection 学习 affine transformation 将 target 语言 correctness subspace
      旋转对齐到 English。Correctness direction 是低维的 (实际是 1D for LR probe)，
      因此旋转矩阵的自由度极低——50 pairs 已充分约束 (条件数稳定)。10 pairs 时 CI
      宽 0.034 (不稳定)，50 pairs CI 收窄至 0.015。超过 50 pairs，marginal gain
      从 +2.2pp/50pairs 骤降至 +0.8pp/50pairs 和 +0.4pp/100pairs。CaCLR (无 parallel
      pairs 的 labels) 等效于 ~35-pair linear projection (AUROC 0.763 vs pairs_35
      插值约 0.76)，表明 MMD distributional matching 实现了部分但非完全的子空间
      对齐。50 pairs 的实用意义大：几乎所有 GlobalMMLU 语言都有 600+ parallel items，
      随机选 50 对即可达到 plateau。
    tables:
      - name: "Table 13: Linear Projection Sample Efficiency (Qwen3, L56)"
        columns: [Pairs, AUROC_Avg, Delta_vs_ZS, Marginal_Gain, CI_95_Width]
        rows:
          - [10,  0.739, +0.011, "—",    0.034]
          - [20,  0.758, +0.030, +0.019, 0.023]
          - [50,  0.790, +0.062, +0.032, 0.015]
          - [100, 0.798, +0.070, +0.008, 0.010]
          - [200, 0.802, +0.074, +0.004, 0.007]
    figures_description:
      - "Fig 7: Sample efficiency curve (log-scale x, AUROC y). Clear elbow at 50. Horizontal line = CaCLR (0.763), intersects curve at ~35 pairs."
    analysis: |
      50 pairs 是实用甜点。Linear projection 在 50 pairs 时超过 CaCLR (0.790 vs
      0.763)，但需要 parallel pairs with correctness labels。两方法互补：CaCLR
      for zero-label 场景，linear projection for minimal-data 场景。

  - name: "Full-Scale Probing Control Tasks"
    plan_id: "plan_013"
    description: "Hewitt & Liang control tasks, 20 langs × 2 archs × all layers (扩展 MVP English-only 结果)"
    expected_results:
      selectivity_below_005_fraction: 0.10
      # Distribution of low-selectivity cells
      low_sel_distribution:
        early_layers_pct: 0.72
        low_resource_pct: 0.68
        overlap_early_AND_low: 0.54
      # Per architecture averages
      qwen_selectivity_avg: 0.178
      llama_selectivity_avg: 0.152
      # Control AUROC (should cluster near 0.50)
      control_auroc_avg: 0.491
      control_auroc_std: 0.012
      control_auroc_max: 0.518
      # Selectivity by depth × resource (Qwen3)
      selectivity_grid_qwen:
        early_HIGH: 0.045
        early_MID: 0.036
        early_LOW: 0.019
        mid_HIGH: 0.142
        mid_MID: 0.118
        mid_LOW: 0.078
        deep_HIGH: 0.261
        deep_MID: 0.242
        deep_LOW: 0.188
      # Problem zone quantification
      problem_zone_cells: 48
      total_cells: 480
      problem_zone_pct: 0.10
      # Cross-lingual extension vs MVP English-only
      english_selectivity_deep_layers: 0.255
      cross_lingual_selectivity_deep_layers_avg: 0.212
      cross_lingual_selectivity_deep_layers_low_resource: 0.168
    result_rationale: |
      Control task AUROC 稳定在 ~0.49 (理论 0.50)，confirming permuted labels 不被
      probe 学到——probing capacity 有限，不会 memorize random labels。10% 的 grid
      cells 有 selectivity < 0.05，集中在 (early layers, LOW resource) 象限：
      (1) Early layers (L0-L20 Qwen / L0-L12 Llama): correctness signal 尚未形成，
      real probe 和 control probe 表现接近，selectivity ≈ 0；(2) Low-resource
      languages: 较少的预训练数据 → correctness 编码更弱 → real probe 提升有限。
      交叉：54% 的 low-selectivity cells 同时满足 early + low-resource。MVP 的
      English-only plan_013 结果 (selectivity 集中在 L20-L27) 与 full-scale 一致，
      但 cross-lingual extension 揭示了资源维度——英语深层 selectivity 0.255 vs
      低资源深层 0.168。这本身是 methodological contribution：跨语言 probing 中
      ~10% 的结果需谨慎解读。
    tables:
      - name: "Table S5: Selectivity by Depth × Resource Tier (Qwen3)"
        columns: [Depth_Range, HIGH_Resource, MID_Resource, LOW_Resource]
        rows:
          - ["0-33% (early)", 0.045, 0.036, 0.019]
          - ["33-67% (mid)",  0.142, 0.118, 0.078]
          - ["67-100% (deep)", 0.261, 0.242, 0.188]
    figures_description:
      - "Fig S4: Selectivity heatmap (y=layer, x=language sorted by resource). 左下角 (low resource × early layer) 颜色最浅 (selectivity → 0)."
    analysis: |
      10% capacity artifact rate 在 best tier [0.05, 0.15] 范围内。核心 probing
      results (中深层 × 中高资源) selectivity > 0.10，genuine signal。Low-resource ×
      early-layer zone 应在 paper 中标注为 "interpret with caution"。

  # ═══════════════════════════════════════════════════════════
  # P2 EXPERIMENTS (Camera-Ready Extension)
  # ═══════════════════════════════════════════════════════════

  - name: "Gemma 4 31B Dense — Third Architecture"
    plan_id: "plan_008"
    description: "60层 Dense (FP16), 第三架构提供 dense vs MoE 对比"
    expected_results:
      en_best_auroc: 0.821
      en_best_layer: 48
      zs_transfer_auroc_avg_20lang: 0.702
      zs_transfer_success_rate: 0.90
      zs_fail_langs: [yo, am]
      pareto_spearman_rho_global: -0.52
      cka_pattern: "gradual decline, onset deeper than Llama (no cliff)"
      cka_correctness_subspace_angle_avg: 13.1
      caclr_delta_auroc_avg: 0.039
    result_rationale: |
      Dense 31B 没有 MoE routing，表征特化更均匀 (无 expert 分配的 language-specific
      路径)，Pareto ρ=-0.52 介于 Qwen3 (ρ=-0.65, 强 MoE cliff) 和 Llama4 (ρ=-0.33,
      弱 MoE) 之间。EN AUROC 0.821 反映 31B dense 的容量低于 235B 但高于 17B active。
      CKA 渐降模式接近 Llama 但 onset 更深——dense model 在中间层保持更强的跨语言
      共享 (无 expert routing 导致的早期分化)。Dense 架构的 Pareto 中等强度提供了
      theory-consistent 的三点比较：cliff MoE (Qwen) > dense (Gemma) > gradual MoE
      (Llama)。仅 yo/am 失败 (2/20)，success rate 0.90。CaCLR delta +3.9pp 低于
      Qwen (+4.7pp) 但高于 Llama (+4.1pp)——dense 的初始 ZS transfer 已较好 (CKA
      更高)，CaCLR 的 marginal room 稍小。
    tables:
      - name: "Table 14: Three-Architecture Comparison"
        columns: [Architecture, Type, EN_AUROC, ZS_Avg, Pareto_rho, CKA_Pattern, CaCLR_Delta]
        rows:
          - [Qwen3-235B, MoE (Int4), 0.832, 0.713, -0.65, "Cliff at 68%", +0.047]
          - [Gemma4-31B, Dense (FP16), 0.821, 0.702, -0.52, "Gradual, deep onset", +0.039]
          - [Llama4-Scout, MoE (W4A16), 0.811, 0.684, -0.33, "Gradual, early onset", +0.041]
    figures_description:
      - "Fig 8: Three-architecture Pareto overlay — Qwen (steep, clear frontier), Gemma (moderate), Llama (flat, scattered). 三种斜率直观展示 architecture dependence."
    analysis: |
      第三架构填充了 dense vs MoE 对比。Pareto 强度排序 (Qwen > Gemma > Llama) 与
      架构差异一致：MoE cliff 产生最强 tradeoff，dense 渐降产生中等 tradeoff，
      无 cliff 的 MoE 最弱。Camera-ready 的 n=3 架构虽仍不足以做因果归因 (type,
      scale, layers, training data 均不同)，但三点一致的模式 strengthens "architecture-
      dependent tradeoff" 的 observational claim。

  - name: "Extended Language Coverage (50+)"
    plan_id: "plan_009"
    description: "扩展至 50+ 语言 (GlobalMMLU + Belebele full sets)"
    expected_results:
      total_languages: 53
      zs_success_rate: 0.83
      n_success: 44
      n_fail: 9
      fail_langs: [am, my, yo, si, lo, km, gu, or, ne]
      pareto_rho_qwen_global_53: -0.62
      pareto_rho_llama_global_53: -0.31
      resource_tier_gradient_r2: 0.71
      new_findings:
        dravidian_cluster: "ta/ml/kn 形成 cluster, ZS AUROC 0.64-0.68, transfer 特征接近 MID tier"
        austronesian_cluster: "id/ms/tl transfer 异常好 (0.72-0.74)，因为与英语的表征对齐度高"
        uralic_outlier: "fi/hu ZS AUROC 差异大 (fi 0.69 vs hu 0.65)，尽管同为 Uralic"
      caclr_delta_avg_53: 0.044
      caclr_delta_new_langs_avg: 0.041
    result_rationale: |
      扩展至 53 语言后，成功率从 ~90% (20 langs) 降至 83% (53 langs)，因为新增
      语言多为 extreme low-resource (si, lo, km 等)。但 Pareto ρ 和主要 patterns
      保持稳定 (Qwen ρ=-0.62 vs -0.65 at 20 langs)，slight reduction 因为新增的
      低资源语言削弱了 global correlation。Resource tier gradient 在更大样本下更
      robust (R²=0.71, up from ~0.60 at 20 langs)。Austronesian 语言 (id/ms/tl)
      transfer 异常好，因为这些语言在大模型预训练中常被 grouped with English-heavy
      corpora (code-switching, romanization)。CaCLR 增益在新增语言上 (+4.1pp) 与
      原 20 语言 (+4.7pp) 相当，confirming method generalizability。
    tables:
      - name: "Table S6: Extended Language Coverage Summary"
        columns: [Metric, 20_Langs, 53_Langs]
        rows:
          - [ZS Success Rate, "95% (Qwen)", "83%"]
          - [Pareto ρ Qwen, -0.65, -0.62]
          - [Pareto ρ Llama, -0.33, -0.31]
          - [Resource Gradient R², ~0.60, 0.71]
          - [CaCLR Δ AUROC avg, +0.047, +0.044]
    figures_description:
      - "Fig S5: 53-language ZS success rate by resource tier. Clear gradient: HIGH ~98%, MID ~90%, LOW ~65%."
    analysis: |
      Camera-ready 扩展确认 core findings 跨 50+ 语言成立。9 种 fail 语言均为
      extreme low-resource (预训练 tokens < 100M)，consistent with domain adaptation
      theory 的 H-divergence 预测。Austronesian cluster 的高 transfer 是 interesting
      secondary finding。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fce58211-5495-4f64-baa3-83f3694e2137",
  "isSidechain": false,
  "requestId": "req_011CbF1KrEE1XjSUSCCmZy9m",
  "type": "assistant",
  "uuid": "83946a7b-f7ca-4537-acc3-c9230284fbf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKrzL38WTZJV9S7oeJb6YQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16488,
      "cache_read_input_tokens": 11841,
      "output_tokens": 46800,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 46800,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16488
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：CaCLR consistency loss is a positive method contribution; Pareto frontier robust on both architectures; CKA geometric analysis holds after depth control; p…",
  "leafUuid": "83946a7b-f7ca-4537-acc3-c9230284fbf0",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe calibration with CaCLR",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：CaCLR consistency loss is a positive method contribution; Pareto frontier robust on both architectures; CKA geometric analysis holds after depth control; p…",
  "leafUuid": "83946a7b-f7ca-4537-acc3-c9230284fbf0",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe calibration with CaCLR",
  "sessionId": "a0d496e8-1674-43bb-b810-06fbedbcb6a7"
}
```

---
