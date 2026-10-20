# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：CaCLR consistency loss inert（β sweep 无效），但 Pareto discovery 稳固且 linear pro

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9.jsonl`
- **Structured JSON:** [`2f45eff45e9fe08d72ef.json`](../../sessions/2f/2f45eff45e9fe08d72ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:44:46.154Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:44:46.154Z",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：CaCLR consistency loss inert（β sweep 无效），但 Pareto discovery 稳固且 linear projection 是 practical solution；CKA 降级为 suggestive；paper 以 discovery + principled negative result + practical recommendation 发表\n核心假设：['MMD distributional matching fails for correctness probes（conditional distribution mismatch，Zhao et al. 2019 预测成立）', 'Pareto frontier 在至少一个架构上清晰，另一个 language-specific（与 MVP pattern 一致）', 'CKA partial correlation 控制 depth 后变弱（marginal 或 n.s.），但 between-language correlation 成立', 'Linear projection ~50-100 pairs 足够，是 zero-label 的实际方案', 'Control task artifacts 集中在低资源语言，~25-30% 的 lang-layer 组合受影响——本身是方法论贡献', 'Decomposition 定性成立但 effect size 小，需补充 ablation', 'Orthogonality 跨语言持续但方差增大']\n关键指标范围：{'en_probe_auroc': [0.76, 0.82], 'zs_transfer_auroc_avg_20lang': [0.62, 0.68], 'zs_transfer_success_rate': [0.7, 0.85], 'pareto_spearman_rho_strong_arch': [-0.6, -0.4], 'pareto_spearman_rho_weak_arch': [-0.25, -0.05], 'caclr_delta_auroc_vs_zeroshot': [-0.005, 0.015], 'caclr_delta_ece_vs_tempscaling': [-0.01, 0.01], 'linear_proj_50pairs_delta_auroc': [0.02, 0.05], 'cka_partial_corr_controlling_depth': [0.1, 0.25], 'cka_partial_corr_p': [0.05, 0.2], 'selectivity_below_005_fraction': [0.2, 0.3], 'orthogonality_cosine_range': [0.02, 0.12], 'difficulty_projection_transfer_delta': [0.005, 0.025]}\n叙事方向：CaCLR 从方法贡献转为 principled negative result：β sweep across 3 OOM + component ablation 证明 MMD 对 correctness 子空间无效，CKA 几何分析解释 why（MMD matches marginals but not low-dim directional structure）。Pareto discovery + architecture contrast 仍是核心贡献。Headline: 'Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; distributional matching fails, but linear projection with ~50 parallel pairs matches supervised baselines.' Claims 强度调整：Claim 1 保持，Claim 2 降为 qualitative，Claim 3 改为 negative result + practical alternative，Claim 4 加 variance caveat。CKA 降级为 'suggestive correlational analysis'。Control task artifact warning 升级为独立贡献。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff varies across architectures (strong on Qwen, weak on Llama); CKA geometric analysis (not mechanistic explanation — correlational, must control for depth) suggests architecture-specific representation divergence rates as a factor. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. A methodological warning: control task analysis reveals that ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold), challenging uncritical use of cross-lingual probing. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis (framed as correlational, NOT mechanistic) provides two levels of insight: (a) between-language: languages with higher CKA show less transfer degradation; (b) between-architecture: CKA cliff steepness differs. **MUST report partial correlation controlling for normalized depth** — if CKA adds no explanatory power beyond depth, downgrade to \"suggestive correlational analysis.\" Subspace angle analysis (quantitative, not just prose) strengthens geometric narrative.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame CKA analysis as geometric/correlational, not mechanistic. We report partial correlation controlling for depth to test whether CKA adds explanatory power beyond the trivial \"deeper = worse transfer.\" If partial correlation is weak, we explicitly state CKA is suggestive only.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique.'\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- exp_id: plan_013_probing_controls_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:44:46.157Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:44:46.157Z",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-21T03:44:46.192Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：CaCLR consistency loss inert（β sweep 无效），但 Pareto discovery 稳固且 linear projection 是 practical solution；CKA 降级为 suggestive；paper 以 discovery + principled negative result + practical recommendation 发表
核心假设：['MMD distributional matching fails for correctness probes（conditional distribution mismatch，Zhao et al. 2019 预测成立）', 'Pareto frontier 在至少一个架构上清晰，另一个 language-specific（与 MVP pattern 一致）', 'CKA partial correlation 控制 depth 后变弱（marginal 或 n.s.），但 between-language correlation 成立', 'Linear projection ~50-100 pairs 足够，是 zero-label 的实际方案', 'Control task artifacts 集中在低资源语言，~25-30% 的 lang-layer 组合受影响——本身是方法论贡献', 'Decomposition 定性成立但 effect size 小，需补充 ablation', 'Orthogonality 跨语言持续但方差增大']
关键指标范围：{'en_probe_auroc': [0.76, 0.82], 'zs_transfer_auroc_avg_20lang': [0.62, 0.68], 'zs_transfer_success_rate': [0.7, 0.85], 'pareto_spearman_rho_strong_arch': [-0.6, -0.4], 'pareto_spearman_rho_weak_arch': [-0.25, -0.05], 'caclr_delta_auroc_vs_zeroshot': [-0.005, 0.015], 'caclr_delta_ece_vs_tempscaling': [-0.01, 0.01], 'linear_proj_50pairs_delta_auroc': [0.02, 0.05], 'cka_partial_corr_controlling_depth': [0.1, 0.25], 'cka_partial_corr_p': [0.05, 0.2], 'selectivity_below_005_fraction': [0.2, 0.3], 'orthogonality_cosine_range': [0.02, 0.12], 'difficulty_projection_transfer_delta': [0.005, 0.025]}
叙事方向：CaCLR 从方法贡献转为 principled negative result：β sweep across 3 OOM + component ablation 证明 MMD 对 correctness 子空间无效，CKA 几何分析解释 why（MMD matches marginals but not low-dim directional structure）。Pareto discovery + architecture contrast 仍是核心贡献。Headline: 'Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; distributional matching fails, but linear projection with ~50 parallel pairs matches supervised baselines.' Claims 强度调整：Claim 1 保持，Claim 2 降为 qualitative，Claim 3 改为 negative result + practical alternative，Claim 4 加 variance caveat。CKA 降级为 'suggestive correlational analysis'。Control task artifact warning 升级为独立贡献。

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
  "promptId": "acf24c0c-9db5-4a00-b354-14e98fea03c7",
  "type": "user",
  "uuid": "7230d124-2bbb-465d-ba0a-3d17c567061b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:44:46.191Z_

```json
{
  "parentUuid": "7230d124-2bbb-465d-ba0a-3d17c567061b",
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
  "uuid": "2b957d54-bf9e-473d-ae29-2a6b92fe0e11",
  "timestamp": "2026-05-21T03:44:46.191Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:44:46.191Z_

```json
{
  "parentUuid": "2b957d54-bf9e-473d-ae29-2a6b92fe0e11",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8bfec043-3b24-4cab-aa19-7d9c7d1b697a",
  "timestamp": "2026-05-21T03:44:46.191Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：CaCLR consistency loss inert（β sweep 无效），但 Pareto discovery 稳固且 linear projection 是 practical solution；CKA 降级为 suggestive；paper 以 discovery + principled…",
  "leafUuid": "8bfec043-3b24-4cab-aa19-7d9c7d1b697a",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer: Pareto frontiers, negative CaCLR result, linear projection baseline",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Assistant

_source line 8 · 2026-05-21T03:44:49.957Z_

Let我先仔细阅读 experiment_plan 和已有数据，然后基于 median 档定义生成详细预测。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bfec043-3b24-4cab-aa19-7d9c7d1b697a",
  "isSidechain": false,
  "requestId": "req_011CbF2SUXZnPsXrRNs4tfFS",
  "type": "assistant",
  "uuid": "921bd0a0-4cc3-4790-be87-7f6f727c2a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6yZ7dgLHzXUzVb6r9TBU8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16695,
      "cache_read_input_tokens": 11841,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 151,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16695
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

_source line 9 · 2026-05-21T03:44:51.596Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YNDkQpWQNzcw9tGi549zew`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "921bd0a0-4cc3-4790-be87-7f6f727c2a92",
  "isSidechain": false,
  "requestId": "req_011CbF2SUXZnPsXrRNs4tfFS",
  "type": "assistant",
  "uuid": "9e7a8401-f80c-4570-a810-350d2bcac2f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6yZ7dgLHzXUzVb6r9TBU8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16695,
      "cache_read_input_tokens": 11841,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16695,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 151,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16695
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

_source line 10 · 2026-05-21T03:44:51.606Z_

<details><summary>↩ Tool result · `toolu_01YNDkQpWQNzcw9tGi549zew`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
5	- 不要复述用户的问题
6	- 不要给未被要求的建议或补充说明
7	- 推理要彻底，但输出只保留结论和必要信息
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e7a8401-f80c-4570-a810-350d2bcac2f0",
  "isSidechain": false,
  "promptId": "acf24c0c-9db5-4a00-b354-14e98fea03c7",
  "type": "user",
  "uuid": "390c7f3a-bb1c-49fb-891c-e90bc0391f35",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "9e7a8401-f80c-4570-a810-350d2bcac2f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T03:46:54.663Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, based on the median tier definition. Let me carefully go through each experiment and create detailed predictions.

Let me review what I know:

**Median tier definition:**
- CaCLR consistency loss inert (β sweep ineffective), but Pareto discovery solid and linear projection is practical solution
- CKA downgraded to suggestive
- Paper publishes as discovery + principled negative result + practical recommendation

**Key metric ranges:**
- en_probe_auroc: [0.76, 0.82]


- zs_transfer_auroc_avg_20lang: [0.62, 0.68]
- zs_transfer_success_rate: [0.7, 0.85]
- pareto_spearman_rho_strong_arch: [-0.6, -0.4]
- pareto_spearman_rho_weak_arch: [-0.25, -0.05]
- caclr_delta_auroc_vs_zeroshot: [-0.005, 0.015]
- caclr_delta_ece_vs_tempscaling: [-0.01, 0.01]
- linear_proj_50

Now I'm looking at additional performance metrics across the different architectures and probes. The CKA partial correlations controlling for depth show modest effects, and the selectivity and orthogonality measures suggest the representations maintain reasonable structure. My core assumptions are holding: MMD fails for correctness, the Pareto frontier behaves differently across architectures, and around 50 linear projection pairs appear sufficient for a practical zero-label approach.

The MVP results from Qwen2.5-7B and Llama-3.1-8B show strong English performance with decent zero-shot transfer, though the CKA correlations are weak and mostly non-significant within individual languages. Now I need to figure out how these 7B findings scale up to the larger models like Qwen3-235B and Llama 4 Scout.

For Qwen3-235B, the larger capacity and MoE architecture should push English AUROC closer to 0.80, and with 94 layers I'd expect a clearer Pareto frontier with stronger depth gradients. Across 20 languages, zero-shot performance should average around 0.65. This model should exhibit the "strong architecture" pattern with a clear negative correlation around -0.5.

Llama 4 Scout is also MoE but follows a different architectural family, and based on the MVP pattern where Llama showed weaker language-specific Pareto effects, I'd expect English AUROC around 0.78 with the "weak architecture" pattern—language-specific Pareto with a shallower correlation around -0.15.

For CaCLR, I'm sweeping across the β parameter to test how regularization strength affects the decomposition.

Now looking at the remaining experiments: the consistency loss stays inert across the OOM range with delta AUROC within noise, while linear projections consistently outperform CaCLR. The difficulty decomposition holds qualitatively though with modest effect sizes, and projecting out difficulty helps transfer slightly for certain languages. Orthogonality metrics stay tight in English (cosine < 0.04) and persist cross-lingually, though variance climbs in lower-resource tiers. Linear probes transfer better across languages than more complex ones, the pattern generalizes to other benchmarks with some dataset-specific variation, quantization artifacts are minimal, and the CKA analysis shows that controlling for depth significantly weakens the partial correlation between languages.

For the remaining plans: 50 projection pairs hit the practical sweet spot for sensitivity, I need to extend the cross-lingual control task predictions using the existing English data, the Gemma 4 model shows a different Pareto shape due to its dense architecture, and the extended language set follows the same pattern as before.

Now I'm organizing the full experimental results carefully, starting with the 235B Qwen model which should show substantially higher performance than the 7B baseline. The global Spearman correlation is -0.52, with high-resource languages showing stronger negative correlations around -0.55 to -0.45, while low-resource languages are closer to zero or slightly positive. For Llama 4 Scout, the English best AUROC drops to ~0.78 with a weaker overall Pareto pattern and global rho of -0.15, though some languages like Arabic and Korean show depth helping transfer. With CaCLR, sweeping β across multiple values produces similar AUROC results regardless of the parameter, and adjusting α shows only modest improvements in calibration error.

Linear projection substantially outperforms CaCLR, gaining +0.035 AUROC with just 50 pairs, and few-shot learning with 100 examples reaches +0.06 AUROC improvement. Removing difficulty as a confound slightly boosts transfer for high-resource languages (+0.015) but has minimal effect for low-resource ones, with a small effect size around Cohen's d of 0.2-0.3. The cosine similarity between representations ranges from 0.02 to 0.12, where high-resource languages cluster tightly at 0.02-0.05 while low-resource languages show more variability between 0.05-0.12.

MLPs marginally improve English AUROC by 1-2 percentage points but hurt cross-lingual transfer by 2-4 percentage points, confirming that linear probes are the better choice for transfer tasks. The pattern holds across other benchmarks like Belebele and MMLU-ProX, though with slightly lower absolute AUROC values. Quantization to W4A16 maintains strong correlation with FP16 (>0.98) with negligible absolute differences under 0.01 AUROC. CKA analysis shows significant between-language differences at multiple layers (p<0.01), though the partial correlation controlling for depth is weaker at r=0.18 (p=0.12).

Linear projection experiments show consistent gains with more language pairs—starting at +0.01 AUROC with 10 pairs and reaching +0.042 with 200 pairs—with diminishing returns after 50 pairs suggesting that's the practical sweet spot. For cross-lingual control tasks, selectivity below 0.005 is concentrated at 0.25 fraction, primarily in low-resource languages and shallow layers. Gemma 4 presents a denser architecture with English AUROC around 0.79 and moderate Pareto strength, while extending to more languages confirms the existing patterns with some additional low-resource language effects.

Now I'm organizing the detailed experiment data for the YAML output, focusing on the planned experiments and making sure to expand each one with the specific metrics and findings. I'm focusing on the planned experiments and need to construct a detailed YAML with solid result rationales. For plan_001 with Qwen3-235B, I'm estimating the English probe AUROC around 0.80 based on the scaling trajectory from the 7B baseline of 0.7541, and I'll be sampling probes across 24 layers at regular intervals throughout the model's depth.

For the layer-wise AUROC profile, I'm expecting early layers to show weak signal around 0.52-0.62, a gradual buildup through the middle layers reaching 0.72-0.79, with the peak performance clustering around 75-80% of the model's depth before a slight decline in the final layers. The MoE architecture might shift this pattern somewhat, but the general trajectory should hold.

Now I'm selecting the 20 languages to include—likely a mix of high-resource languages like English, Mandarin, Spanish, French, German, and Japanese, paired with medium-resource languages like Portuguese, Russian, Arabic, Hindi, Korean, Vietnamese, Thai, Turkish, Polish, Dutch, and Swahili, plus lower-resource ones like Bengali, Telugu, and Yoruba.

Looking at the zero-shot AUROC at the optimal layer, I see a clear stratification: high-resource languages cluster around 0.70-0.76, mid-resource ones fall in the 0.62-0.70 range, and low-resource languages bottom out at 0.52-0.60, averaging around 0.65 overall. The Spearman correlation between layer depth and transfer performance shows a strong negative relationship of about -0.50 across all languages, but this varies significantly by resource level—high-resource languages show a steep -0.55 to -0.40 correlation indicating a clear performance cliff, while mid-resource languages are more moderate at -0.40 to -0.20, and low-resource languages show almost no correlation or even slight positive trends.

Now testing five different transfer approaches at that same optimal layer: zero-shot and mean-shift both hover around 0.65, linear projection with 50 pairs bumps it to 0.68, few-shot with 25 examples reaches 0.67, few-shot with 100 examples climbs to 0.71, and CaCLR barely improves over zero-shot at 0.655. Shifting focus to Llama 4 Scout, the 17B-16E variant should substantially outperform the previous Llama-3.1-8B baseline of 0.7284, likely reaching around 0.78, and I'm planning to probe every fourth layer across its 48-layer architecture for a total of 12 measurement points.

For the weak architecture variant, the global correlation drops to -0.15 with much more heterogeneous patterns across languages—some like Arabic and Korean show positive relationships while others go negative. The CaCLR experiment is designed to capture a key negative result: sweeping β across three orders of magnitude from 0.001 to 1.0 shows AUROC improvements stay within a narrow [-0.005, +0.015] band relative to zero-shot with no clear monotonic trend, and similarly sweeping α for ECE versus temperature scaling yields no consistent gains.

Looking at the comparison table across 20 languages at the EN-optimal layer, the results are stark: CaCLR barely budges from zero-shot baseline (0.650 AUROC, 0.190 ECE), while linear projection jumps to 0.685 AUROC with 0.180 ECE, and few-shot with 100 examples reaches 0.710 AUROC and 0.160 ECE—making it clear that CaCLR is essentially inert compared to these simpler alternatives.

Now I'm ready to write out the comprehensive YAML configuration, but I need to account for the fact that plan_001 uses Qwen3-235B and plan_002 uses Llama 4 Scout, which are substantially different from the MVP models. Qwen3-235B is a 235B MoE model with 22B active parameters across 94 layers, so the deeper architecture and routing dynamics will behave differently than the smaller baseline. Llama 4 Scout has its own MoE structure with 17B per expert across 16 experts and 48 layers, plus W4A16 quantization instead of INT4, so I need to account for these architectural differences when setting expectations.

The key insight is that the architectural pattern from the MVP should persist at scale—Qwen maintains its strong Pareto properties while Llama remains more language-specific and weaker—because this is an inherent architectural characteristic, not just a scale effect. So I'm mapping the median tier ranges with Qwen3-235B in the strong architecture bracket (pareto_spearman_rho around -0.6 to -0.4) and Llama 4 Scout in the weak architecture bracket (around -0.25 to -0.05), then I'll write out the full configuration.

Now I'm planning the tables and figures for each experiment. For plan_001 with Qwen, I need layer-wise AUROC tables, a heatmap of zero-shot performance across languages and layers, per-language Spearman correlations, a Pareto frontier visualization comparing English AUROC against zero-shot transfer, and a bar chart showing different transfer conditions. Plan_002 repeats this structure for Llama 4 Scout, plus an overlay figure comparing the two architectures' Pareto frontiers. Plan_003 focuses on the hyperparameter sweeps with tables for β and α results, a method comparison table across different approaches, line plots showing the inertness effect, and cross-language method comparisons. Plan_004 wraps up with before-and-after AUROC tables for the difficulty projection transfer.

For the remaining experiments, I'm adding a decomposition figure by resource tier, then moving into plan_005 with cosine similarity matrices and orthogonality heatmaps, plan_006 with probe complexity comparisons, plan_007 with cross-benchmark generalization, plan_010 with quantization effects, plan_011 with CKA analysis and partial correlations, plan_012 with learning curves, plan_008 with Gemma results, and plan_009 with extended language summaries. I'll aim to include specific numbers throughout these tables and figures.

Now I'm thinking through which architectures show strong versus weak Pareto tradeoffs. Qwen exhibits a clear negative correlation between layer depth and cross-lingual transfer—deeper layers help English but hurt other languages consistently. Llama behaves differently, with language-specific patterns rather than a global tradeoff. The MVP data confirms this: Qwen2.5-7B peaks at mid-range layers across languages, never at the deepest layer, while the pattern varies by language rather than showing one dominant trend.

Scaling this up, Qwen3-235B should show the same strong tradeoff with English-optimal layers deep (~L72-L80) but transfer-optimal layers much shallower (~L52-L64), creating a clear Pareto gap. Llama 4 Scout, meanwhile, should have some languages peaking at the deepest layers and others at middle layers, resulting in a weak global correlation. I need to be precise about how this plays out across the full set of 20 languages.

Looking at the transfer performance metrics, I'm seeing average AUROC around 0.65 across the 20 languages with success rates between 75-85%, meaning roughly 15-17 languages exceed the threshold. For the English probe AUROC, the range should be 0.76-0.82 based on the tier specifications—I'll set Qwen3-235B at 0.80 and Llama 4 Scout at 0.78, though I need to clarify whether these ranges apply per-model or across the entire experiment.

For zero-shot transfer, I'm distributing the [0.62, 0.68] range across both models, assigning Qwen3-235B an average of 0.66 and Llama 4 Scout 0.64 to reach that combined 0.65 average. Now I'm ready to write out the full YAML configuration with all planned experiments, structuring each with name, plan_id, description, and expected_results metrics.

Writing YAML configuration...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "390c7f3a-bb1c-49fb-891c-e90bc0391f35",
  "isSidechain": false,
  "requestId": "req_011CbF2SsmJtx69WEJBZts6g",
  "type": "assistant",
  "uuid": "ebfff81a-323f-4cb2-9c62-d1c49f2cb5d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCz5Vdru4tLE8pCfRobfUx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 28536,
      "output_tokens": 6105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6105,
          "cache_read_input_tokens": 28536,
          "cache_creation_input_tokens": 323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 323
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

_source line 12 · 2026-05-21T03:46:54.665Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XAM53fWHja2M5fKHWpoJ86`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebfff81a-323f-4cb2-9c62-d1c49f2cb5d8",
  "isSidechain": false,
  "requestId": "req_011CbF2SsmJtx69WEJBZts6g",
  "type": "assistant",
  "uuid": "50f54b6f-b910-4203-8f3b-7eaa1c23e123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCz5Vdru4tLE8pCfRobfUx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 28536,
      "output_tokens": 6105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6105,
          "cache_read_input_tokens": 28536,
          "cache_creation_input_tokens": 323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 323
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

_source line 13 · 2026-05-21T03:46:54.689Z_

<details><summary>↩ Tool result · `toolu_01XAM53fWHja2M5fKHWpoJ86`</summary>

```text
config/approvals.yaml
config/backend.yaml
config/feishu.yaml
workspace.yaml
config/venue_registry.yaml
config/venue_rules/corl-2026.yaml
config/venue_rules/emnlp-2026.yaml
idea_generator/ideas.yaml
projects/xling_calib_direction/literature_map.yaml
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
config/secrets/xling_calib_direction/manifest.yaml
projects/xling_calab_direction/registry.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
config/projects/xling_calib_direction.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/meta.yaml
projects/xling_calib_direction/artifacts/review_issues.yaml
projects/xling_calib_direction/artifacts/manifest.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/review_context.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/meta.yaml
projects/xling_calib_direction/experiment_plan.yaml
projects/xling_calib_direction/registry.yaml
projects/xling_calib_direction/decisions.yaml
projects/xling_calib_direction/mistakes.yaml
projects/xling_calib_direction/dream_registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50f54b6f-b910-4203-8f3b-7eaa1c23e123",
  "isSidechain": false,
  "promptId": "acf24c0c-9db5-4a00-b354-14e98fea03c7",
  "type": "user",
  "uuid": "c56bcc15-47d5-4fde-89c8-e05cc6363d1c",
  "toolUseResult": {
    "filenames": [
      "config/approvals.yaml",
      "config/backend.yaml",
      "config/feishu.yaml",
      "workspace.yaml",
      "config/venue_registry.yaml",
      "config/venue_rules/corl-2026.yaml",
      "config/venue_rules/emnlp-2026.yaml",
      "idea_generator/ideas.yaml",
      "projects/xling_calib_direction/literature_map.yaml",
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
      "config/secrets/xling_calib_direction/manifest.yaml",
      "projects/xling_calab_direction/registry.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
      "config/projects/xling_calib_direction.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/meta.yaml",
      "projects/xling_calib_direction/artifacts/review_issues.yaml",
      "projects/xling_calib_direction/artifacts/manifest.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/review_context.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/meta.yaml",
      "projects/xling_calib_direction/experiment_plan.yaml",
      "projects/xling_calib_direction/registry.yaml",
      "projects/xling_calib_direction/decisions.yaml",
      "projects/xling_calib_direction/mistakes.yaml",
      "projects/xling_calib_direction/dream_registry.yaml"
    ],
    "durationMs": 15,
    "numFiles": 46,
    "truncated": false
  },
  "sourceToolAssistantUUID": "50f54b6f-b910-4203-8f3b-7eaa1c23e123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：CaCLR consistency loss inert（β sweep 无效），但 Pareto discovery 稳固且 linear projection 是 practical solution；CKA 降级为 suggestive；paper 以 discovery + principled…",
  "leafUuid": "c56bcc15-47d5-4fde-89c8-e05cc6363d1c",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer: Pareto frontiers, negative CaCLR result, linear projection baseline",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Tool call

_source line 16 · 2026-05-21T03:46:57.609Z_

<details open><summary>🔧 Tool call — Read · `toolu_013o3mZWYHkUh2yuoF1S7omc`</summary>

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
  "parentUuid": "c56bcc15-47d5-4fde-89c8-e05cc6363d1c",
  "isSidechain": false,
  "requestId": "req_011CbF2bxByFyfaVYhUdy9hD",
  "type": "assistant",
  "uuid": "fe095b6a-c265-4971-9148-2ea8a7c27df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwqCutoRH3AEK3C4jDcQQL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7091,
      "cache_read_input_tokens": 28859,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 28859,
          "cache_creation_input_tokens": 7091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7091
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

_source line 17 · 2026-05-21T03:46:57.615Z_

<details><summary>↩ Tool result · `toolu_013o3mZWYHkUh2yuoF1S7omc`</summary>

```text
1	experiments:
2	  # === P0: Core submission (must complete for EACL 2027 ARR Aug 3) ===
3	
4	  - id: plan_001
5	    claim: 1
6	    description: >
7	      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4):
8	      extract activations at every 4th layer (24 probed layers),
9	      20 typologically diverse languages, train English correctness probes
10	      (logistic regression + 2-layer MLP), evaluate 5 transfer conditions
11	      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).
12	      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.
13	      Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.
14	    priority: P0
15	    gpu_budget_hours: 80
16	    deps: []
17	    notes: >
18	      4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM).
19	      INT4 (not INT8) required to fit 235B model. Need INT4 validation ablation
20	      (compare INT4 vs INT8 at representative layers on subset — extend plan_010).
21	
22	  - id: plan_002
23	    claim: 1
24	    description: >
25	      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16):
26	      extract activations at every 4th layer (12 probed layers),
27	      20 languages, 5 transfer conditions. W4A16 weight quantization
28	      (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).
29	      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.
30	    priority: P0
31	    gpu_budget_hours: 40
32	    deps: []
33	    notes: >
34	      W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).
35	      Changed from INT8 to W4A16 due to disk constraints (both models must coexist).
36	      plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).
37	
38	  - id: plan_003
39	    claim: 3
40	    description: >
41	      CaCLR implementation and comparative evaluation:
42	      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD distance).
43	      Train CaCLR probes using English labels + unlabeled parallel activations.
44	      DATA: GlobalMMLU test split partitioned 70/30 (probe_train/eval, stratified).
45	      English BCE labels + parallel MMD activations from probe_train only;
46	      evaluate exclusively on eval portion. No train split exists in GlobalMMLU.
47	      MMD operates on probe logits (not raw activations — M007 gradient fix).
48	      Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100)
49	      across full Pareto frontier for both models × 20 languages.
50	      Hyperparameter tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0).
51	      Report fixed-layer results (50% depth + EN-optimal) alongside per-language oracle.
52	    priority: P0
53	    gpu_budget_hours: 20
54	    deps: [plan_001, plan_002]
55	    notes: >
56	      CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS 2021.
57	      L_consistency uses Maximum Mean Discrepancy (MMD).
58	      If β sweep shows inert consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional narrative).
59	      IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1, 3-tier consensus):
60	      (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic
61	      (b) Optimizer: Adam, report LR + schedule
62	      (c) Epochs + early stopping criterion
63	      (d) Initialization: from standard LR solution or from scratch
64	      (e) Batch size for MMD computation
65	      (f) Whether MMD items overlap with BCE training items or held-out
66	      (g) Parallel set size per language + translation quality note for low-resource
67	      Negative result demands higher reproducibility bar than positive.
68	
69	  - id: plan_004
70	    claim: 2
71	    description: >
72	      Difficulty-controlled ablation: train IRT difficulty probes (Ridge regression
73	      on human difficulty scores per Civelli et al.), project out difficulty direction
74	      from activations, retrain correctness probes on residuals, evaluate transfer.
75	      10 representative languages × 8 representative layers per model (20-90% depth).
76	    priority: P0
77	    gpu_budget_hours: 15
78	    deps: [plan_001, plan_002]
79	    notes: >
80	      Need IRT difficulty scores from GlobalMMLU or external source.
81	      Grid justification (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn)
82	      × major language families. 8 layers span 20-90% depth at uniform intervals.
83	      Reduced grid is sufficient because decomposition tests a qualitative hypothesis
84	      (does projecting out difficulty help or hurt?), not a per-language quantitative claim.
85	      Include random-direction control to rule out dimensionality-reduction artifacts.
86	
87	  # === Cross-cutting requirements ===
88	  # Language list (20): en, zh, ar, hi, sw, ko, es, fr, de, ru, tr, bn, ja, pt, vi, te, id, pl, nl, uk
89	  # Note: th (Thai) replaced by te (Telugu) — Thai not in GlobalMMLU; Telugu adds Dravidian family.
90	  # Data split: GlobalMMLU test 70/30 stratified → probe_train / eval. No train split exists.
91	  # Statistics (Dream D1): bootstrap CIs (1000 resamples), paired permutation tests,
92	  # Cohen's d for effect sizes. Report sample sizes per language.
93	  # AUROC threshold sensitivity analysis (0.55/0.60/0.65/0.70/0.75) for pass/fail reporting.
94	
95	  # === P1: Important for strong submission ===
96	
97	  - id: plan_005
98	    claim: 4
99	    description: >
100	      Cross-lingual orthogonality analysis: extract verbalized confidence direction
101	      (prompt model for confidence score, fit probe), compute cosine similarity
102	      with correctness direction across 20 languages × 2 architectures.
103	      Analyze by resource tier (high/mid/low) and language family.
104	    priority: P1
105	    gpu_budget_hours: 10
106	    deps: [plan_001, plan_002]
107	
108	  - id: plan_006
109	    claim: 1
110	    description: >
111	      Probe complexity comparison: logistic regression vs 2-layer MLP
112	      at each probed layer for both models. Compare English accuracy,
113	      cross-lingual transfer degradation, and calibration quality.
114	      Test hypothesis: linear probes transfer better cross-lingually.
115	    priority: P1
116	    gpu_budget_hours: 5
117	    deps: [plan_001, plan_002]
118	    notes: "CPU-bound, uses cached activations."
119	
120	  - id: plan_007
121	    claim: 1
122	    description: >
123	      Additional benchmark evaluation: evaluate best probes + CaCLR
124	      on Belebele (20 languages) and MMLU-ProX (20 languages).
125	      Validates generalization beyond MMLU/GlobalMMLU.
126	    priority: P1
127	    gpu_budget_hours: 30
128	    deps: [plan_001, plan_002, plan_003]
129	
130	  - id: plan_010
131	    claim: 1
132	    description: >
133	      Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative
134	      layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at
135	      5 representative layers for Qwen3-235B on 5% random subset.
136	      Validates that quantization doesn't distort correctness signals.
137	      Note: FP16 baseline requires temporary download of FP16 weights for subset only,
138	      then delete. May need to do sequentially due to disk constraints.
139	    priority: P1
140	    gpu_budget_hours: 10
141	    deps: [plan_001, plan_002]
142	
143	  - id: plan_011
144	    claim: [1, 4]
145	    description: >
146	      CKA cross-lingual representation similarity analysis:
147	      compute CKA (linear kernel) between English and each target language
148	      at every probed layer for both models. Full-scale validation of pilot finding:
149	      correctness direction is a robust low-dimensional subspace feature that persists
150	      despite global CKA decline. Transfer collapses only at critical CKA threshold (~0.35).
151	      Report CKA × layer × language heatmaps, CKA vs transfer degradation
152	      ((EN_AUROC - target_AUROC) / EN_AUROC) correlation per language to isolate
153	      alignment effect from probe quality, and critical threshold analysis.
154	    priority: P1
155	    gpu_budget_hours: 5
156	    deps: [plan_001, plan_002]
157	    notes: >
158	      CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).
159	      Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001,
160	      Qwen rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig.
161	      CAUTION (Reviewer): pooled correlation has depth confound. Pilot per-language
162	      Spearman almost all n.s. (n=9 too small), ko direction reversed. Overall p=0.007
163	      driven by BETWEEN-language differences (zh/ar high CKA + low degradation vs
164	      hi/sw low CKA + high degradation), not within-language depth effects.
165	      Supportable claim: "languages with higher CKA exhibit less transfer degradation"
166	      (between-language, qualitative at n=5). NOT supportable: "CKA predicts within-
167	      language degradation across depth."
168	      Full-scale analysis (20 langs) MUST include: (a) same-layer cross-language
169	      correlation (strongest test, n=20 per layer), (b) partial correlation controlling
170	      for normalized depth — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2,
171	      3-tier consensus); if CKA adds no explanatory power beyond depth, downgrade
172	      framing from "geometric analysis" to "suggestive correlation", (c) per-language
173	      Spearman with denser layer sampling, (d) subspace angle analysis with
174	      QUANTITATIVE tables (not just prose — Dream best-tier W1).
175	      CKA cliff steepness explains Qwen-Llama tradeoff strength difference (qualitative).
176	      Frame as "geometric/correlational analysis" NOT "mechanistic explanation" (Dream RD6/RD9).
177	
178	  - id: plan_012
179	    claim: 1
180	    description: >
181	      Linear projection sensitivity analysis: vary number of parallel
182	      pairs (10, 20, 50, 100, 200) for linear projection transfer.
183	      Determines minimum data requirement for this surprisingly strong baseline.
184	      Both models × 5 representative layers × 20 languages.
185	    priority: P1
186	    gpu_budget_hours: 2
187	    deps: [plan_001, plan_002]
188	    notes: "CPU-bound, uses cached activations. Dream review D11."
189	
190	  - id: plan_013
191	    claim: 1
192	    description: >
193	      Probing control tasks (Hewitt & Liang 2019): train probes on
194	      randomly permuted labels at each layer. Compare selectivity
195	      (probe AUROC - control AUROC) across layers and languages.
196	      Validates that high AUROC reflects genuine correctness direction,
197	      not memorized dataset artifacts or probe capacity.
198	    priority: P1
199	    gpu_budget_hours: 2
200	    deps: [plan_001, plan_002]
201	    notes: "CPU-bound. Dream review D22: probing methodology critique."
202	
203	  # === P2: Camera-ready extension ===
204	
205	  - id: plan_008
206	    claim: 1
207	    description: >
208	      Gemma 4 31B Dense (60 layers, dense, FP16): third architecture
209	      for camera-ready. Full Pareto frontier, 20+ languages.
210	      Provides dense vs MoE architectural contrast.
211	    priority: P2
212	    gpu_budget_hours: 30
213	    deps: []
214	
215	  - id: plan_009
216	    claim: 1
217	    description: >
218	      Extended language coverage: expand from 20 to 50+ languages
219	      for camera-ready. Leverages GlobalMMLU/Belebele full language sets.
220	    priority: P2
221	    gpu_budget_hours: 50
222	    deps: [plan_001, plan_002]
223	
224	  # === MVP experiments (completed/running) ===
225	
226	  - id: mvp_validation
227	    claim: 1
228	    description: "MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift"
229	    priority: P0
230	    registry_id: mvp_001
231	    gpu_budget_hours: 2
232	    deps: []
233	
234	  - id: mvp_complementary
235	    claim: 1
236	    description: "MVP robustness: complementary layer set (2,6,10,14,18,22,26)"
237	    priority: P1
238	    registry_id: mvp_002
239	    gpu_budget_hours: 2
240	    deps: [mvp_validation]
241	
242	  - id: mvp_llama_control
243	    claim: 1
244	    description: "MVP cross-architecture: Llama-3.1-8B control experiment"
245	    priority: P1
246	    registry_id: mvp_003
247	    gpu_budget_hours: 3
248	    deps: [mvp_validation]
249	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe095b6a-c265-4971-9148-2ea8a7c27df2",
  "isSidechain": false,
  "promptId": "acf24c0c-9db5-4a00-b354-14e98fea03c7",
  "type": "user",
  "uuid": "666dc27c-f6d0-4bc8-a58e-ed1f9af9125e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml",
      "content": "experiments:\n  # === P0: Core submission (must complete for EACL 2027 ARR Aug 3) ===\n\n  - id: plan_001\n    claim: 1\n    description: >\n      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4):\n      extract activations at every 4th layer (24 probed layers),\n      20 typologically diverse languages, train English correctness probes\n      (logistic regression + 2-layer MLP), evaluate 5 transfer conditions\n      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\n      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n      Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n    priority: P0\n    gpu_budget_hours: 80\n    deps: []\n    notes: >\n      4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM).\n      INT4 (not INT8) required to fit 235B model. Need INT4 validation ablation\n      (compare INT4 vs INT8 at representative layers on subset — extend plan_010).\n\n  - id: plan_002\n    claim: 1\n    description: >\n      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16):\n      extract activations at every 4th layer (12 probed layers),\n      20 languages, 5 transfer conditions. W4A16 weight quantization\n      (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n    priority: P0\n    gpu_budget_hours: 40\n    deps: []\n    notes: >\n      W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n      Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n      plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n  - id: plan_003\n    claim: 3\n    description: >\n      CaCLR implementation and comparative evaluation:\n      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD distance).\n      Train CaCLR probes using English labels + unlabeled parallel activations.\n      DATA: GlobalMMLU test split partitioned 70/30 (probe_train/eval, stratified).\n      English BCE labels + parallel MMD activations from probe_train only;\n      evaluate exclusively on eval portion. No train split exists in GlobalMMLU.\n      MMD operates on probe logits (not raw activations — M007 gradient fix).\n      Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100)\n      across full Pareto frontier for both models × 20 languages.\n      Hyperparameter tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0).\n      Report fixed-layer results (50% depth + EN-optimal) alongside per-language oracle.\n    priority: P0\n    gpu_budget_hours: 20\n    deps: [plan_001, plan_002]\n    notes: >\n      CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS 2021.\n      L_consistency uses Maximum Mean Discrepancy (MMD).\n      If β sweep shows inert consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional narrative).\n      IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1, 3-tier consensus):\n      (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n      (b) Optimizer: Adam, report LR + schedule\n      (c) Epochs + early stopping criterion\n      (d) Initialization: from standard LR solution or from scratch\n      (e) Batch size for MMD computation\n      (f) Whether MMD items overlap with BCE training items or held-out\n      (g) Parallel set size per language + translation quality note for low-resource\n      Negative result demands higher reproducibility bar than positive.\n\n  - id: plan_004\n    claim: 2\n    description: >\n      Difficulty-controlled ablation: train IRT difficulty probes (Ridge regression\n      on human difficulty scores per Civelli et al.), project out difficulty direction\n      from activations, retrain correctness probes on residuals, evaluate transfer.\n      10 representative languages × 8 representative layers per model (20-90% depth).\n    priority: P0\n    gpu_budget_hours: 15\n    deps: [plan_001, plan_002]\n    notes: >\n      Need IRT difficulty scores from GlobalMMLU or external source.\n      Grid justification (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn)\n      × major language families. 8 layers span 20-90% depth at uniform intervals.\n      Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n      (does projecting out difficulty help or hurt?), not a per-language quantitative claim.\n      Include random-direction control to rule out dimensionality-reduction artifacts.\n\n  # === Cross-cutting requirements ===\n  # Language list (20): en, zh, ar, hi, sw, ko, es, fr, de, ru, tr, bn, ja, pt, vi, te, id, pl, nl, uk\n  # Note: th (Thai) replaced by te (Telugu) — Thai not in GlobalMMLU; Telugu adds Dravidian family.\n  # Data split: GlobalMMLU test 70/30 stratified → probe_train / eval. No train split exists.\n  # Statistics (Dream D1): bootstrap CIs (1000 resamples), paired permutation tests,\n  # Cohen's d for effect sizes. Report sample sizes per language.\n  # AUROC threshold sensitivity analysis (0.55/0.60/0.65/0.70/0.75) for pass/fail reporting.\n\n  # === P1: Important for strong submission ===\n\n  - id: plan_005\n    claim: 4\n    description: >\n      Cross-lingual orthogonality analysis: extract verbalized confidence direction\n      (prompt model for confidence score, fit probe), compute cosine similarity\n      with correctness direction across 20 languages × 2 architectures.\n      Analyze by resource tier (high/mid/low) and language family.\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan_001, plan_002]\n\n  - id: plan_006\n    claim: 1\n    description: >\n      Probe complexity comparison: logistic regression vs 2-layer MLP\n      at each probed layer for both models. Compare English accuracy,\n      cross-lingual transfer degradation, and calibration quality.\n      Test hypothesis: linear probes transfer better cross-lingually.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [plan_001, plan_002]\n    notes: \"CPU-bound, uses cached activations.\"\n\n  - id: plan_007\n    claim: 1\n    description: >\n      Additional benchmark evaluation: evaluate best probes + CaCLR\n      on Belebele (20 languages) and MMLU-ProX (20 languages).\n      Validates generalization beyond MMLU/GlobalMMLU.\n    priority: P1\n    gpu_budget_hours: 30\n    deps: [plan_001, plan_002, plan_003]\n\n  - id: plan_010\n    claim: 1\n    description: >\n      Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n      layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n      5 representative layers for Qwen3-235B on 5% random subset.\n      Validates that quantization doesn't distort correctness signals.\n      Note: FP16 baseline requires temporary download of FP16 weights for subset only,\n      then delete. May need to do sequentially due to disk constraints.\n    priority: P1\n    gpu_budget_hours: 10\n    deps: [plan_001, plan_002]\n\n  - id: plan_011\n    claim: [1, 4]\n    description: >\n      CKA cross-lingual representation similarity analysis:\n      compute CKA (linear kernel) between English and each target language\n      at every probed layer for both models. Full-scale validation of pilot finding:\n      correctness direction is a robust low-dimensional subspace feature that persists\n      despite global CKA decline. Transfer collapses only at critical CKA threshold (~0.35).\n      Report CKA × layer × language heatmaps, CKA vs transfer degradation\n      ((EN_AUROC - target_AUROC) / EN_AUROC) correlation per language to isolate\n      alignment effect from probe quality, and critical threshold analysis.\n    priority: P1\n    gpu_budget_hours: 5\n    deps: [plan_001, plan_002]\n    notes: >\n      CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n      Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001,\n      Qwen rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig.\n      CAUTION (Reviewer): pooled correlation has depth confound. Pilot per-language\n      Spearman almost all n.s. (n=9 too small), ko direction reversed. Overall p=0.007\n      driven by BETWEEN-language differences (zh/ar high CKA + low degradation vs\n      hi/sw low CKA + high degradation), not within-language depth effects.\n      Supportable claim: \"languages with higher CKA exhibit less transfer degradation\"\n      (between-language, qualitative at n=5). NOT supportable: \"CKA predicts within-\n      language degradation across depth.\"\n      Full-scale analysis (20 langs) MUST include: (a) same-layer cross-language\n      correlation (strongest test, n=20 per layer), (b) partial correlation controlling\n      for normalized depth — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2,\n      3-tier consensus); if CKA adds no explanatory power beyond depth, downgrade\n      framing from \"geometric analysis\" to \"suggestive correlation\", (c) per-language\n      Spearman with denser layer sampling, (d) subspace angle analysis with\n      QUANTITATIVE tables (not just prose — Dream best-tier W1).\n      CKA cliff steepness explains Qwen-Llama tradeoff strength difference (qualitative).\n      Frame as \"geometric/correlational analysis\" NOT \"mechanistic explanation\" (Dream RD6/RD9).\n\n  - id: plan_012\n    claim: 1\n    description: >\n      Linear projection sensitivity analysis: vary number of parallel\n      pairs (10, 20, 50, 100, 200) for linear projection transfer.\n      Determines minimum data requirement for this surprisingly strong baseline.\n      Both models × 5 representative layers × 20 languages.\n    priority: P1\n    gpu_budget_hours: 2\n    deps: [plan_001, plan_002]\n    notes: \"CPU-bound, uses cached activations. Dream review D11.\"\n\n  - id: plan_013\n    claim: 1\n    description: >\n      Probing control tasks (Hewitt & Liang 2019): train probes on\n      randomly permuted labels at each layer. Compare selectivity\n      (probe AUROC - control AUROC) across layers and languages.\n      Validates that high AUROC reflects genuine correctness direction,\n      not memorized dataset artifacts or probe capacity.\n    priority: P1\n    gpu_budget_hours: 2\n    deps: [plan_001, plan_002]\n    notes: \"CPU-bound. Dream review D22: probing methodology critique.\"\n\n  # === P2: Camera-ready extension ===\n\n  - id: plan_008\n    claim: 1\n    description: >\n      Gemma 4 31B Dense (60 layers, dense, FP16): third architecture\n      for camera-ready. Full Pareto frontier, 20+ languages.\n      Provides dense vs MoE architectural contrast.\n    priority: P2\n    gpu_budget_hours: 30\n    deps: []\n\n  - id: plan_009\n    claim: 1\n    description: >\n      Extended language coverage: expand from 20 to 50+ languages\n      for camera-ready. Leverages GlobalMMLU/Belebele full language sets.\n    priority: P2\n    gpu_budget_hours: 50\n    deps: [plan_001, plan_002]\n\n  # === MVP experiments (completed/running) ===\n\n  - id: mvp_validation\n    claim: 1\n    description: \"MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift\"\n    priority: P0\n    registry_id: mvp_001\n    gpu_budget_hours: 2\n    deps: []\n\n  - id: mvp_complementary\n    claim: 1\n    description: \"MVP robustness: complementary layer set (2,6,10,14,18,22,26)\"\n    priority: P1\n    registry_id: mvp_002\n    gpu_budget_hours: 2\n    deps: [mvp_validation]\n\n  - id: mvp_llama_control\n    claim: 1\n    description: \"MVP cross-architecture: Llama-3.1-8B control experiment\"\n    priority: P1\n    registry_id: mvp_003\n    gpu_budget_hours: 3\n    deps: [mvp_validation]\n",
      "numLines": 249,
      "startLine": 1,
      "totalLines": 249
    }
  },
  "sourceToolAssistantUUID": "fe095b6a-c265-4971-9148-2ea8a7c27df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T03:46:58.080Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WsfqGDAuv2aEf9YrW4xhtV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "666dc27c-f6d0-4bc8-a58e-ed1f9af9125e",
  "isSidechain": false,
  "requestId": "req_011CbF2bxByFyfaVYhUdy9hD",
  "type": "assistant",
  "uuid": "75f52e8d-2e7f-488a-bbaf-1b9b03e22dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwqCutoRH3AEK3C4jDcQQL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7091,
      "cache_read_input_tokens": 28859,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 28859,
          "cache_creation_input_tokens": 7091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7091
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

_source line 19 · 2026-05-21T03:46:58.086Z_

<details><summary>↩ Tool result · `toolu_01WsfqGDAuv2aEf9YrW4xhtV`</summary>

```text
1	baseline: null
2	experiments:
3	  mvp_001:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-20T14:17:02.273Z'
7	    updated_at: '2026-05-20T20:26:56.163Z'
8	    hypothesis: 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性
9	      probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在
10	      layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp
11	      for ≥3/5 语言）。
12	    spec:
13	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
14	        base && cd /root/xling_calib_direction && bash run_mvp.sh"
15	      server: westd-13176
16	      gpu:
17	      - cuda:0
18	      pid: '9845'
19	      log_path: ~/runs/xling_calib_direction/mvp_001.log
20	      submitted_at: '2026-05-20T16:29:25.456Z'
21	      submitted_via: submit_training_job
22	      backend: tmux
23	      account: root
24	      wall_clock_seconds: 6824.1
25	      gpu_hours: 1.9
26	    conclusion: success
27	    metrics:
28	      en_best_auroc: 0.7541
29	      en_best_layer: 27
30	      en_best_ece_raw: 0.1951
31	      temp_scaling_fixed:
32	        L24:
33	          T: 0.67
34	          ECE_cal: 0.2205
35	        L27:
36	          T: 0.62
37	          ECE_cal: 0.2216
38	        note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens
39	          ECE.
40	      en_auroc_range:
41	      - 0.6113
42	      - 0.7541
43	      layer_depth_delta: 0.1428
44	      layers_tested:
45	      - 0
46	      - 4
47	      - 8
48	      - 12
49	      - 16
50	      - 20
51	      - 24
52	      - 27
53	      zs_pass_langs:
54	      - zh
55	      - ar
56	      - hi
57	      - ko
58	      zs_fail_langs:
59	      - sw
60	      best_zs_auroc:
61	        zh: 0.686
62	        ar: 0.651
63	        hi: 0.652
64	        ko: 0.648
65	        sw: 0.56
66	      mean_shift_delta_ece:
67	        zh: -0.36
68	        ar: -0.06
69	        hi: 2.22
70	        sw: 6.44
71	        ko: 0.01
72	      pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per
73	        D006.
74	      p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)
75	      p2: PASS (4/5)
76	      p3: PASS (14.28pp)
77	      p4: FAIL (0/5, mean-shift no improvement)
78	    checkpoint_path: /root/xling_calib_direction/probes/
79	    log_path: /root/xling_calib_direction/results/summary.txt
80	    completed_at: '2026-05-20T18:23:09.593Z'
81	  mvp_002:
82	    status: DONE
83	    retry_count: 0
84	    created_at: '2026-05-20T16:26:27.143Z'
85	    updated_at: '2026-05-20T19:29:01.161Z'
86	    hypothesis: Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与
87	      mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际
88	      28 层，index 0-27）
89	    parent: mvp_001
90	    spec:
91	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
92	        base && cd /root/xling_calib_direction && bash run_mvp_002.sh"
93	      server: westd-13176
94	      gpu:
95	      - cuda:1
96	      pid: '11397'
97	      log_path: ~/runs/xling_calib_direction/mvp_002.log
98	      submitted_at: '2026-05-20T17:01:16.028Z'
99	      submitted_via: submit_training_job
100	      backend: tmux
101	      account: root
102	      wall_clock_seconds: 6874.5
103	      gpu_hours: 1.91
104	    conclusion: success
105	    metrics:
106	      en_best_auroc: 0.7481
107	      en_best_layer: 26
108	      en_auroc_range:
109	      - 0.6229
110	      - 0.7481
111	      layer_depth_delta: 0.1251
112	      best_zs_auroc:
113	        zh: 0.6774
114	        ar: 0.6302
115	        hi: 0.6068
116	        sw: 0.5467
117	        ko: 0.6678
118	      best_zs_layer:
119	        zh: 26
120	        ar: 26
121	        hi: 22
122	        sw: 22
123	        ko: 26
124	      pass_fail:
125	        P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)
126	        P2_zs_auroc: PASS (4/5)
127	        P3_layer_delta: PASS (12.51pp)
128	        P4_mean_shift: FAIL (0/5, zero delta)
129	        overall: PARTIAL
130	    log_path: /root/xling_calib_direction/results_mvp002/summary.txt
131	    checkpoint_path: /root/xling_calib_direction/probes_mvp002/
132	    completed_at: '2026-05-20T18:55:50.484Z'
133	  mvp_003:
134	    status: DONE
135	    retry_count: 0
136	    created_at: '2026-05-20T18:27:06.449Z'
137	    updated_at: '2026-05-20T20:48:56.916Z'
138	    hypothesis: 'Cross-lingual correctness direction is model-agnostic: an English-trained
139	      linear probe on Llama-3.1-8B-Instruct internal representations will transfer
140	      to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the
141	      pattern observed in Qwen2.5-7B-Instruct (mvp_001).'
142	    parent: mvp_001
143	    spec:
144	      command: CUDA_VISIBLE_DEVICES=2 bash /root/xling_calib_direction/run_mvp_003.sh
145	      server: westd-13176
146	      data_path: cais/mmlu + CohereForAI/Global-MMLU
147	      data_count: ~14K test samples per language
148	      model_name: LLM-Research/Meta-Llama-3.1-8B-Instruct (ModelScope)
149	      seed: 42
150	      gpu: cuda:2
151	      tmux_session: mvp_003
152	      log_path: /root/xling_calib_direction/mvp_003.log
153	      checkpoint_source: LLM-Research/Meta-Llama-3.1-8B-Instruct
154	      eval_data: cais/mmlu + CohereForAI/Global-MMLU
155	    conclusion: success
156	    metrics:
157	      en_best_auroc: 0.7284
158	      en_best_layer: 31
159	      en_best_ece_raw: 0.2052
160	      en_auroc_range:
161	      - 0.6331
162	      - 0.7284
163	      layer_depth_delta: 0.0953
164	      layers_tested:
165	      - 0
166	      - 4
167	      - 8
168	      - 12
169	      - 16
170	      - 20
171	      - 24
172	      - 28
173	      - 31
174	      best_zs_auroc:
175	        zh: 0.64
176	        ar: 0.6146
177	        hi: 0.5935
178	        ko: 0.6481
179	        sw: 0.5838
180	      best_zs_layer:
181	        zh: 20
182	        ar: 31
183	        hi: 31
184	        ko: 31
185	        sw: 16
186	      zs_pass_langs:
187	      - zh
188	      - ar
189	      - hi
190	      - ko
191	      - sw
192	      zs_fail_langs: []
193	      pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)
194	      note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).
195	        P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC
196	        is rank-invariant.'
197	      cka_vs_degradation:
198	        overall_rho: -0.3982
199	        overall_p: 0.0068
200	        per_lang:
201	          ar:
202	            rho: -0.2833
203	            p: 0.46
204	          hi:
205	            rho: -0.6667
206	            p: 0.0499
207	          ko:
208	            rho: 0.25
209	            p: 0.5165
210	          sw:
211	            rho: -0.5833
212	            p: 0.0992
213	          zh:
214	            rho: -0.4833
215	            p: 0.1875
216	    checkpoint_path: /root/xling_calib_direction/probes_mvp003/
217	    log_path: /root/xling_calib_direction/results_mvp003/summary.txt
218	    completed_at: '2026-05-20T20:34:43.102Z'
219	  plan_013:
220	    status: DONE
221	    retry_count: 0
222	    created_at: '2026-05-21T00:39:58.089Z'
223	    updated_at: '2026-05-21T00:59:20.023Z'
224	    hypothesis: 'English correctness probes capture genuine linguistic signal: 5-fold
225	      CV with PCA(100) dimensionality reduction shows real AUROC significantly above
226	      permuted-label baseline (0.746 vs 0.484 at best layer), with selectivity (Hewitt
227	      & Liang 2019) concentrated in later layers (L20-L27), confirming the probe is
228	      not exploiting spurious high-dimensional correlations.'
229	    parent: mvp_001
230	    spec:
231	      command: python probing_controls_v2.py (5-fold CV + PCA-100)
232	      server: westd-13176
233	      data_path: /root/xling_calib_direction/activations/layer*_en.pt
234	      data_count: ~14K MMLU test samples
235	      model_name: Qwen2.5-7B-Instruct (activations from mvp_001)
236	      seed: 42
237	      checkpoint_source: mvp_001 activations
238	      eval_data: same activations, 5-fold CV
239	    conclusion: success
240	    metrics:
241	      method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)
242	      selectivity_hewitt_liang:
243	        L0: 0.02
244	        L4: 0.037
245	        L8: 0.036
246	        L12: 0.042
247	        L16: 0.123
248	        L20: 0.244
249	        L24: 0.248
250	        L27: 0.262
251	      real_auroc:
252	        L0: 0.501
253	        L4: 0.524
254	        L8: 0.529
255	        L12: 0.53
256	        L16: 0.615
257	        L20: 0.733
258	        L24: 0.738
259	        L27: 0.746
260	      permuted_auroc:
261	        L0: 0.481
262	        L4: 0.487
263	        L8: 0.493
264	        L12: 0.488
265	        L16: 0.492
266	        L20: 0.489
267	        L24: 0.49
268	        L27: 0.484
269	      pca_variance_retained:
270	        L0: 0.922
271	        L4: 0.912
272	        L8: 0.885
273	        L12: 0.868
274	        L16: 0.783
275	        L20: 0.738
276	        L24: 0.844
277	        L27: 0.794
278	      note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal
279	        concentrated in L20-L27. PCA(100) retains 73-92% variance.
280	    checkpoint_path: /root/xling_calib_direction/results/probing_controls.csv
281	    log_path: /root/xling_calib_direction/results/probing_controls.csv
282	    completed_at: '2026-05-21T00:59:20.023Z'
283	  plan_013_probing_controls_v2:
284	    status: PREPARING
285	    retry_count: 0
286	    created_at: '2026-05-21T01:04:11.073Z'
287	    updated_at: '2026-05-21T01:04:11.073Z'
288	    conclusion: failed
289	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75f52e8d-2e7f-488a-bbaf-1b9b03e22dd1",
  "isSidechain": false,
  "promptId": "acf24c0c-9db5-4a00-b354-14e98fea03c7",
  "type": "user",
  "uuid": "bf27f49a-427f-490b-9014-4de2bdf9975e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml",
      "content": "baseline: null\nexperiments:\n  mvp_001:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T14:17:02.273Z'\n    updated_at: '2026-05-20T20:26:56.163Z'\n    hypothesis: 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性\n      probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在\n      layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp\n      for ≥3/5 语言）。\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/xling_calib_direction && bash run_mvp.sh\"\n      server: westd-13176\n      gpu:\n      - cuda:0\n      pid: '9845'\n      log_path: ~/runs/xling_calib_direction/mvp_001.log\n      submitted_at: '2026-05-20T16:29:25.456Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 6824.1\n      gpu_hours: 1.9\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7541\n      en_best_layer: 27\n      en_best_ece_raw: 0.1951\n      temp_scaling_fixed:\n        L24:\n          T: 0.67\n          ECE_cal: 0.2205\n        L27:\n          T: 0.62\n          ECE_cal: 0.2216\n        note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens\n          ECE.\n      en_auroc_range:\n      - 0.6113\n      - 0.7541\n      layer_depth_delta: 0.1428\n      layers_tested:\n      - 0\n      - 4\n      - 8\n      - 12\n      - 16\n      - 20\n      - 24\n      - 27\n      zs_pass_langs:\n      - zh\n      - ar\n      - hi\n      - ko\n      zs_fail_langs:\n      - sw\n      best_zs_auroc:\n        zh: 0.686\n        ar: 0.651\n        hi: 0.652\n        ko: 0.648\n        sw: 0.56\n      mean_shift_delta_ece:\n        zh: -0.36\n        ar: -0.06\n        hi: 2.22\n        sw: 6.44\n        ko: 0.01\n      pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n        D006.\n      p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n      p2: PASS (4/5)\n      p3: PASS (14.28pp)\n      p4: FAIL (0/5, mean-shift no improvement)\n    checkpoint_path: /root/xling_calib_direction/probes/\n    log_path: /root/xling_calib_direction/results/summary.txt\n    completed_at: '2026-05-20T18:23:09.593Z'\n  mvp_002:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T16:26:27.143Z'\n    updated_at: '2026-05-20T19:29:01.161Z'\n    hypothesis: Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与\n      mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际\n      28 层，index 0-27）\n    parent: mvp_001\n    spec:\n      command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate\n        base && cd /root/xling_calib_direction && bash run_mvp_002.sh\"\n      server: westd-13176\n      gpu:\n      - cuda:1\n      pid: '11397'\n      log_path: ~/runs/xling_calib_direction/mvp_002.log\n      submitted_at: '2026-05-20T17:01:16.028Z'\n      submitted_via: submit_training_job\n      backend: tmux\n      account: root\n      wall_clock_seconds: 6874.5\n      gpu_hours: 1.91\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7481\n      en_best_layer: 26\n      en_auroc_range:\n      - 0.6229\n      - 0.7481\n      layer_depth_delta: 0.1251\n      best_zs_auroc:\n        zh: 0.6774\n        ar: 0.6302\n        hi: 0.6068\n        sw: 0.5467\n        ko: 0.6678\n      best_zs_layer:\n        zh: 26\n        ar: 26\n        hi: 22\n        sw: 22\n        ko: 26\n      pass_fail:\n        P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n        P2_zs_auroc: PASS (4/5)\n        P3_layer_delta: PASS (12.51pp)\n        P4_mean_shift: FAIL (0/5, zero delta)\n        overall: PARTIAL\n    log_path: /root/xling_calib_direction/results_mvp002/summary.txt\n    checkpoint_path: /root/xling_calib_direction/probes_mvp002/\n    completed_at: '2026-05-20T18:55:50.484Z'\n  mvp_003:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-20T18:27:06.449Z'\n    updated_at: '2026-05-20T20:48:56.916Z'\n    hypothesis: 'Cross-lingual correctness direction is model-agnostic: an English-trained\n      linear probe on Llama-3.1-8B-Instruct internal representations will transfer\n      to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the\n      pattern observed in Qwen2.5-7B-Instruct (mvp_001).'\n    parent: mvp_001\n    spec:\n      command: CUDA_VISIBLE_DEVICES=2 bash /root/xling_calib_direction/run_mvp_003.sh\n      server: westd-13176\n      data_path: cais/mmlu + CohereForAI/Global-MMLU\n      data_count: ~14K test samples per language\n      model_name: LLM-Research/Meta-Llama-3.1-8B-Instruct (ModelScope)\n      seed: 42\n      gpu: cuda:2\n      tmux_session: mvp_003\n      log_path: /root/xling_calib_direction/mvp_003.log\n      checkpoint_source: LLM-Research/Meta-Llama-3.1-8B-Instruct\n      eval_data: cais/mmlu + CohereForAI/Global-MMLU\n    conclusion: success\n    metrics:\n      en_best_auroc: 0.7284\n      en_best_layer: 31\n      en_best_ece_raw: 0.2052\n      en_auroc_range:\n      - 0.6331\n      - 0.7284\n      layer_depth_delta: 0.0953\n      layers_tested:\n      - 0\n      - 4\n      - 8\n      - 12\n      - 16\n      - 20\n      - 24\n      - 28\n      - 31\n      best_zs_auroc:\n        zh: 0.64\n        ar: 0.6146\n        hi: 0.5935\n        ko: 0.6481\n        sw: 0.5838\n      best_zs_layer:\n        zh: 20\n        ar: 31\n        hi: 31\n        ko: 31\n        sw: 16\n      zs_pass_langs:\n      - zh\n      - ar\n      - hi\n      - ko\n      - sw\n      zs_fail_langs: []\n      pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n      note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n        P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n        is rank-invariant.'\n      cka_vs_degradation:\n        overall_rho: -0.3982\n        overall_p: 0.0068\n        per_lang:\n          ar:\n            rho: -0.2833\n            p: 0.46\n          hi:\n            rho: -0.6667\n            p: 0.0499\n          ko:\n            rho: 0.25\n            p: 0.5165\n          sw:\n            rho: -0.5833\n            p: 0.0992\n          zh:\n            rho: -0.4833\n            p: 0.1875\n    checkpoint_path: /root/xling_calib_direction/probes_mvp003/\n    log_path: /root/xling_calib_direction/results_mvp003/summary.txt\n    completed_at: '2026-05-20T20:34:43.102Z'\n  plan_013:\n    status: DONE\n    retry_count: 0\n    created_at: '2026-05-21T00:39:58.089Z'\n    updated_at: '2026-05-21T00:59:20.023Z'\n    hypothesis: 'English correctness probes capture genuine linguistic signal: 5-fold\n      CV with PCA(100) dimensionality reduction shows real AUROC significantly above\n      permuted-label baseline (0.746 vs 0.484 at best layer), with selectivity (Hewitt\n      & Liang 2019) concentrated in later layers (L20-L27), confirming the probe is\n      not exploiting spurious high-dimensional correlations.'\n    parent: mvp_001\n    spec:\n      command: python probing_controls_v2.py (5-fold CV + PCA-100)\n      server: westd-13176\n      data_path: /root/xling_calib_direction/activations/layer*_en.pt\n      data_count: ~14K MMLU test samples\n      model_name: Qwen2.5-7B-Instruct (activations from mvp_001)\n      seed: 42\n      checkpoint_source: mvp_001 activations\n      eval_data: same activations, 5-fold CV\n    conclusion: success\n    metrics:\n      method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n      selectivity_hewitt_liang:\n        L0: 0.02\n        L4: 0.037\n        L8: 0.036\n        L12: 0.042\n        L16: 0.123\n        L20: 0.244\n        L24: 0.248\n        L27: 0.262\n      real_auroc:\n        L0: 0.501\n        L4: 0.524\n        L8: 0.529\n        L12: 0.53\n        L16: 0.615\n        L20: 0.733\n        L24: 0.738\n        L27: 0.746\n      permuted_auroc:\n        L0: 0.481\n        L4: 0.487\n        L8: 0.493\n        L12: 0.488\n        L16: 0.492\n        L20: 0.489\n        L24: 0.49\n        L27: 0.484\n      pca_variance_retained:\n        L0: 0.922\n        L4: 0.912\n        L8: 0.885\n        L12: 0.868\n        L16: 0.783\n        L20: 0.738\n        L24: 0.844\n        L27: 0.794\n      note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n        concentrated in L20-L27. PCA(100) retains 73-92% variance.\n    checkpoint_path: /root/xling_calib_direction/results/probing_controls.csv\n    log_path: /root/xling_calib_direction/results/probing_controls.csv\n    completed_at: '2026-05-21T00:59:20.023Z'\n  plan_013_probing_controls_v2:\n    status: PREPARING\n    retry_count: 0\n    created_at: '2026-05-21T01:04:11.073Z'\n    updated_at: '2026-05-21T01:04:11.073Z'\n    conclusion: failed\n",
      "numLines": 289,
      "startLine": 1,
      "totalLines": 289
    }
  },
  "sourceToolAssistantUUID": "75f52e8d-2e7f-488a-bbaf-1b9b03e22dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T03:46:58.626Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QKVkVAbhXfZMr4BE3RGknk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf27f49a-427f-490b-9014-4de2bdf9975e",
  "isSidechain": false,
  "requestId": "req_011CbF2bxByFyfaVYhUdy9hD",
  "type": "assistant",
  "uuid": "816fb248-1c6f-4e58-ab63-d8204e4adfbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwqCutoRH3AEK3C4jDcQQL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7091,
      "cache_read_input_tokens": 28859,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 28859,
          "cache_creation_input_tokens": 7091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7091
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：CaCLR consistency loss inert（β sweep 无效），但 Pareto discovery 稳固且 linear projection 是 practical solution；CKA 降级为 suggestive；paper 以 discovery + principled…",
  "leafUuid": "816fb248-1c6f-4e58-ab63-d8204e4adfbc",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer: Pareto frontiers, negative CaCLR result, linear projection baseline",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Tool result

_source line 23 · 2026-05-21T03:46:59.019Z_

<details><summary>↩ Tool result · `toolu_01QKVkVAbhXfZMr4BE3RGknk`</summary>

```text
1	tier: median
2	narrative_guidance: 'Analysis paper with principled negative result as centerpiece.
3	  Narrative arc: (1) Pareto frontier established on two large MoE architectures —
4	  qualitatively replicates MVP findings but rho is moderate (median ~-0.52), confirming
5	  architecture-dependent shape; (2) CKA reveals geometric misalignment increasing
6	  with depth — CKA-transfer correlation r≈0.58 provides mechanistic explanation for
7	  WHY deeper layers transfer worse; (3) CaCLR consistency loss (β) is inert across
8	  3 OOM sweep — this is PREDICTED by the geometric explanation: MMD matches distributions
9	  but cannot correct the rotation of the correctness direction across language subspaces;
10	  (4) Linear projection succeeds (~+3.5pp over zero-shot) precisely because it learns
11	  the rotation that MMD cannot, saturating at ~70 parallel pairs. Decomposition and
12	  orthogonality are supporting evidence. Decomposition shows difficulty is shared
13	  but capability-specific component drives degradation (~65% of combos improved).
14	  Orthogonality persists across languages (cosine < 0.10) but with more variance in
15	  low-resource languages. Control tasks confirm probe selectivity (>10pp) but sw/bn
16	  are weaker. ECE improvements over temperature scaling are negligible — emphasize
17	  AUROC and mechanistic understanding. Target: borderline to weak accept at EACL.
18	
19	  '
20	imagined_experiments:
21	- name: Qwen3-235B-A22B Full Pareto Frontier
22	  plan_id: plan_001
23	  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): 24
24	    probed layers, 20 languages, 5 transfer conditions (zero-shot, mean-shift, linear
25	    projection, few-shot 25/100, CaCLR). Per-language and global Spearman rho.
26	
27	    '
28	  expected_results:
29	    en_best_auroc: 0.81
30	    en_best_layer: 72
31	    en_best_ece_raw: 0.17
32	    en_best_ece_tempcal: 0.065
33	    temp_scaling_T: 5.8
34	    en_auroc_range:
35	    - 0.58
36	    - 0.81
37	    en_auroc_50pct_depth_layer47: 0.76
38	    zs_transfer_auroc_median_20lang_at_en_optimal: 0.63
39	    zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.7
40	    best_transfer_layer: 48
41	    pareto_rho_global: -0.58
42	    pareto_rho_per_lang_median: -0.51
43	    pareto_rho_per_lang_range:
44	    - -0.78
45	    - -0.21
46	    zs_langs_above_0p65: 13
47	    zs_auroc_zh: 0.74
48	    zs_auroc_es: 0.73
49	    zs_auroc_fr: 0.73
50	    zs_auroc_de: 0.72
51	    zs_auroc_ar: 0.7
52	    zs_auroc_hi: 0.69
53	    zs_auroc_ru: 0.71
54	    zs_auroc_ko: 0.69
55	    zs_auroc_ja: 0.7
56	    zs_auroc_pt: 0.72
57	    zs_auroc_vi: 0.68
58	    zs_auroc_tr: 0.67
59	    zs_auroc_id: 0.68
60	    zs_auroc_th: 0.66
61	    zs_auroc_pl: 0.69
62	    zs_auroc_uk: 0.68
63	    zs_auroc_he: 0.66
64	    zs_auroc_el: 0.65
65	    zs_auroc_sw: 0.58
66	    zs_auroc_bn: 0.57
67	    mean_shift_delta_auroc_median: 0.0
68	    linear_proj_delta_auroc_over_zs_median: 0.035
69	    fewshot_25_delta_auroc_over_zs_median: 0.025
70	    fewshot_100_delta_auroc_over_zs_median: 0.045
71	    ece_reduction_vs_temp_scaling_median: 0.008
72	  result_rationale: 'Qwen3-235B-A22B is a 94-layer MoE model — significantly deeper
73	    than the 7B MVP. The English best AUROC rises to 0.81 because the larger model
74	    encodes stronger correctness signals (more parameters, more knowledge). The best
75	    English layer is at ~76% depth (layer 72), consistent with the MVP pattern where
76	    correctness peaks in deep-but-not-final layers. The Pareto frontier is present
77	    but rho is moderate (-0.51 median per-language) because: (a) the MoE routing creates
78	    more heterogeneous layer representations, reducing the clean monotonic depth-degradation
79	    pattern seen in dense models; (b) some languages (especially high-resource zh/es/fr)
80	    have strong multilingual representations even at deeper layers due to extensive
81	    pretraining data, attenuating the negative correlation. The per-language rho range
82	    [-0.78, -0.21] reflects that low-resource languages (sw, bn) show stronger negative
83	    correlation (their representations diverge from English more sharply at depth)
84	    while high-resource languages show weaker correlation (they maintain reasonable
85	    alignment throughout). 13/20 languages cross 0.65 AUROC — most European and major
86	    Asian languages transfer adequately at optimal layers, but sw (0.58) and bn (0.57)
87	    remain below threshold due to limited pretraining representation for these languages.
88	    Mean-shift produces exactly zero AUROC change (rank-invariance proof holds), confirming
89	    the MVP finding. Linear projection (+3.5pp) outperforms few-shot-25 (+2.5pp) because
90	    it directly corrects geometric misalignment rather than relying on a small labeled
91	    sample. ECE improvement over temperature scaling is marginal (0.8pp) because probe-based
92	    calibration and temperature scaling address different aspects — at the median
93	    tier, probes don''t provide much additional calibration beyond what temperature
94	    scaling already captures.
95	
96	    '
97	  tables:
98	  - name: 'Table 1: Qwen3-235B-A22B Pareto Frontier — Zero-Shot Transfer AUROC by
99	      Language × Layer'
100	    description: '24 probed layers (rows) × 20 languages + English (columns). Cells
101	      show AUROC. Bold: best layer per language. Gray shading: layers within 1pp of
102	      best. Bottom rows: global and per-language Spearman rho with 95% bootstrap CI.
103	      Key pattern: English-optimal layer (72) ≠ transfer-optimal layer (48) for most
104	      languages. High-resource languages show flatter profiles; low-resource show
105	      steeper drop-off at deep layers.
106	
107	      '
108	  - name: 'Table 2: Qwen3-235B-A22B Transfer Method Comparison at Fixed Layers'
109	    description: '5 transfer methods (columns) × 20 languages (rows), evaluated at
110	      two fixed layers (50% depth = layer 47, EN-optimal = layer 72) plus per-language
111	      oracle. Shows AUROC and ΔAUROC vs zero-shot. Bootstrap 95% CI and paired permutation
112	      test p-values. Cohen''s d for each method vs zero-shot baseline.
113	
114	      '
115	  figures_description:
116	  - 'Figure: Pareto frontier scatter plot — x-axis: English AUROC, y-axis: median
117	    zero-shot transfer AUROC across 20 langs. Each point is a layer. Annotated with
118	    layer numbers. Pareto-optimal layers highlighted. Separate curves for resource
119	    tiers (high/mid/low) showing tier-dependent frontier shape.'
120	  - 'Figure: Per-language Spearman rho bar chart — 20 bars sorted by rho magnitude.
121	    Color-coded by resource tier. Error bars show bootstrap 95% CI. Horizontal line
122	    at rho = -0.5 for reference.'
123	  analysis: 'The Pareto frontier replicates on this large MoE model but with moderate
124	    per-language rho (-0.51 median). The architecture-dependent shape is visible:
125	    MoE routing creates more variable layer representations, so the depth-transfer
126	    tradeoff is less smooth than in a dense model. The key finding is that 13/20 languages
127	    achieve usable zero-shot transfer (>0.65 AUROC) at optimal layers, validating
128	    the approach for most languages. The 7 languages below threshold cluster in low-resource
129	    (sw, bn) and morphologically distant categories (th, he at marginal 0.66). Linear
130	    projection provides the most consistent improvement across languages.
131	
132	    '
133	- name: Llama 4 Scout Full Pareto Frontier
134	  plan_id: plan_002
135	  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): 12 probed
136	    layers, 20 languages, 5 transfer conditions. Per-language Spearman rho.
137	
138	    '
139	  expected_results:
140	    en_best_auroc: 0.79
141	    en_best_layer: 36
142	    en_best_ece_raw: 0.19
143	    en_best_ece_tempcal: 0.07
144	    temp_scaling_T: 6.0
145	    en_auroc_range:
146	    - 0.6
147	    - 0.79
148	    en_auroc_50pct_depth_layer24: 0.74
149	    zs_transfer_auroc_median_20lang_at_en_optimal: 0.62
150	    zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.68
151	    best_transfer_layer: 24
152	    pareto_rho_global: -0.62
153	    pareto_rho_per_lang_median: -0.54
154	    pareto_rho_per_lang_range:
155	    - -0.82
156	    - -0.28
157	    zs_langs_above_0p65: 11
158	    zs_auroc_zh: 0.72
159	    zs_auroc_es: 0.71
160	    zs_auroc_fr: 0.71
161	    zs_auroc_de: 0.7
162	    zs_auroc_ar: 0.68
163	    zs_auroc_hi: 0.67
164	    zs_auroc_ru: 0.69
165	    zs_auroc_ko: 0.66
166	    zs_auroc_ja: 0.67
167	    zs_auroc_pt: 0.7
168	    zs_auroc_vi: 0.65
169	    zs_auroc_tr: 0.64
170	    zs_auroc_id: 0.66
171	    zs_auroc_th: 0.63
172	    zs_auroc_pl: 0.67
173	    zs_auroc_uk: 0.65
174	    zs_auroc_he: 0.63
175	    zs_auroc_el: 0.62
176	    zs_auroc_sw: 0.55
177	    zs_auroc_bn: 0.54
178	    mean_shift_delta_auroc_median: 0.0
179	    linear_proj_delta_auroc_over_zs_median: 0.032
180	    fewshot_25_delta_auroc_over_zs_median: 0.022
181	    fewshot_100_delta_auroc_over_zs_median: 0.04
182	    ece_reduction_vs_temp_scaling_median: 0.005
183	  result_rationale: 'Llama 4 Scout has fewer layers (48 vs 94) and a different MoE
184	    architecture from Qwen3. The English best AUROC is slightly lower (0.79 vs 0.81)
185	    reflecting somewhat weaker correctness encoding in a shallower architecture. The
186	    Pareto rho is slightly stronger negative (-0.54 vs -0.51) because with fewer layers,
187	    each layer step represents a larger proportional depth change, making the depth-transfer
188	    tradeoff more pronounced. The best transfer layer at 50% depth (layer 24) is consistent
189	    with the pattern that mid-depth layers balance English quality and cross-lingual
190	    alignment. 11/20 languages cross 0.65, slightly fewer than Qwen3 — Llama 4''s
191	    multilingual pretraining may be less balanced, particularly for mid-resource languages
192	    like tr (0.64) and vi (0.65) that were marginal on Qwen3. Low-resource sw (0.55)
193	    and bn (0.54) are again the weakest, confirming this is a fundamental limitation
194	    of pretraining representation rather than architecture-specific. The same qualitative
195	    Pareto pattern holds but the quantitative frontier shape differs — the drop-off
196	    from English-optimal to transfer-optimal is steeper on Llama 4, confirming architecture-dependence
197	    without requiring architecture-specific tuning as a paper claim.
198	
199	    '
200	  tables:
201	  - name: 'Table 3: Llama 4 Scout Pareto Frontier — Zero-Shot Transfer AUROC by Language
202	      × Layer'
203	    description: '12 probed layers × 20 languages + English. Same format as Table
204	      1. Key contrast with Qwen3: steeper Pareto drop-off, fewer layers in the Pareto-optimal
205	      set due to coarser layer sampling.
206	
207	      '
208	  - name: 'Table 4: Llama 4 Scout Transfer Method Comparison'
209	    description: 'Same format as Table 2. Llama 4 Scout results. Key finding: linear
210	      projection improvement (+3.2pp) is comparable to Qwen3, suggesting the geometric
211	      correction transfers across architectures.
212	
213	      '
214	  figures_description:
215	  - 'Figure: Side-by-side Pareto frontier comparison — Qwen3-235B (left) vs Llama
216	    4 Scout (right). Same axis scales for direct visual comparison. Annotated with
217	    architecture properties (depth, MoE routing). Shows that qualitative Pareto shape
218	    replicates but quantitative steepness differs.'
219	  analysis: 'Llama 4 Scout confirms the Pareto frontier generalizes across architectures.
220	    The steeper negative rho (-0.54) vs Qwen3 (-0.51) is a moderate difference that
221	    supports the architecture-dependence claim but is not dramatic enough to call
222	    it a strong architectural contrast. This is the median-tier signature: same qualitative
223	    finding, quantitatively less distinct than ideal. Both models agree on the key
224	    implication: mid-depth layers are the right operating point for cross-lingual
225	    transfer.
226	
227	    '
228	- name: CaCLR Implementation and Comparative Evaluation
229	  plan_id: plan_003
230	  description: 'CaCLR probe training with L_BCE + α·L_SB-ECE + β·L_consistency (MMD).
231	    α sweep (0.01–10.0), β sweep (0.001–1.0) across 3 OOM. Full comparison vs zero-shot,
232	    mean-shift, linear projection, few-shot on both models × 20 langs.
233	
234	    '
235	  expected_results:
236	    alpha_optimal: 0.5
237	    alpha_only_en_auroc_at_en_optimal_layer_qwen: 0.805
238	    alpha_only_en_ece_at_en_optimal_layer_qwen: 0.058
239	    alpha_only_zs_median_auroc_qwen: 0.695
240	    alpha_only_zs_median_auroc_llama: 0.675
241	    beta_0p001_delta_auroc_over_alpha_only_median: 0.002
242	    beta_0p01_delta_auroc_over_alpha_only_median: 0.001
243	    beta_0p1_delta_auroc_over_alpha_only_median: -0.001
244	    beta_1p0_delta_auroc_over_alpha_only_median: -0.003
245	    beta_sweep_max_delta_auroc: 0.003
246	    beta_sweep_significant_at_p05: false
247	    caclr_full_delta_auroc_over_zeroshot_median: 0.012
248	    caclr_full_delta_auroc_over_zeroshot_range:
249	    - -0.005
250	    - 0.035
251	    caclr_vs_linear_proj_delta_median: -0.023
252	    caclr_vs_fewshot100_delta_median: -0.033
253	    linear_proj_delta_auroc_over_zs_median_qwen: 0.035
254	    linear_proj_delta_auroc_over_zs_median_llama: 0.032
255	    fewshot_25_delta_auroc_over_zs_median: 0.024
256	    fewshot_100_delta_auroc_over_zs_median: 0.043
257	    mean_shift_delta_auroc_median: 0.0
258	    method_ranking:
259	    - few-shot-100
260	    - linear-projection
261	    - few-shot-25
262	    - CaCLR-full
263	    - CaCLR-α-only
264	    - zero-shot
265	    - mean-shift
266	    caclr_beta_delta_high_resource: 0.004
267	    caclr_beta_delta_mid_resource: 0.0
268	    caclr_beta_delta_low_resource: -0.002
269	    caclr_beta_vs_alpha_only_paired_perm_p: 0.42
270	    caclr_beta_vs_alpha_only_cohens_d: 0.08
271	    linear_proj_vs_zeroshot_paired_perm_p: 0.001
272	    linear_proj_vs_zeroshot_cohens_d: 0.55
273	  result_rationale: 'The β (consistency loss) is inert because MMD-based distributional
274	    matching fundamentally cannot correct the geometric misalignment that CKA reveals.
275	    MMD penalizes differences in mean embeddings and kernel-space distributional moments
276	    — it can align marginal distributions but cannot learn the rotation of the correctness
277	    direction across language subspaces. At low β (0.001), the MMD signal is too weak
278	    to affect optimization. At medium β (0.01–0.1), the gradient signal exists but
279	    points in the wrong direction — it pushes overall distributional alignment without
280	    specifically aligning the correctness-relevant subspace. At high β (1.0), the
281	    MMD term dominates and slightly hurts English AUROC by distorting the probe weights.
282	    The α-only (SB-ECE) variant provides small but real calibration improvement (better
283	    ECE) because smooth-binned ECE regularization is a well-motivated objective that
284	    doesn''t require cross-lingual alignment. The total CaCLR improvement over zero-shot
285	    (+1.2pp) comes entirely from the α term''s calibration regularization, not from
286	    cross-lingual consistency. Cohen''s d = 0.08 for β effect is negligible. In contrast,
287	    linear projection achieves +3.5pp because it directly estimates and corrects the
288	    rotation via a learned affine transformation on parallel pairs. Few-shot-100 achieves
289	    +4.3pp because it sidesteps alignment entirely by training on target-language
290	    labels. This ranking — few-shot > linear-projection > CaCLR ≈ α-only > zero-shot
291	    > mean-shift — is the key empirical result that the geometric explanation predicts.
292	
293	    '
294	  tables:
295	  - name: 'Table 5: β Sensitivity Sweep — ΔAUROC over α-only baseline'
296	    description: 'β values (rows: 0, 0.001, 0.01, 0.1, 1.0) × summary statistics (columns:
297	      median ΔAUROC, mean, std, min, max, # languages improved, paired permutation
298	      p-value, Cohen''s d). Both models shown side-by-side. Key: no β value achieves
299	      p < 0.05 or d > 0.2 — consistency loss is definitively inert.
300	
301	      '
302	  - name: 'Table 6: Transfer Method Comparison — Median AUROC across 20 Languages'
303	    description: 'Methods (rows: zero-shot, mean-shift, CaCLR-α-only, CaCLR-full,
304	      linear-projection, few-shot-25, few-shot-100) × Models (columns: Qwen3, Llama
305	      4) × 2 fixed layers + per-language oracle. ΔAUROC vs zero-shot with bootstrap
306	      95% CI. Ranking is consistent across models. Linear projection and few-shot
307	      clearly dominate.
308	
309	      '
310	  - name: 'Table 7: CaCLR β Effect by Resource Tier'
311	    description: 'Resource tier (rows: HIGH, MID, LOW) × β levels. Shows that inertness
312	      is consistent across tiers — not a power issue with low-resource languages but
313	      a fundamental limitation of distributional matching.
314	
315	      '
316	  figures_description:
317	  - 'Figure: α sensitivity curve — x-axis: log(α), y-axis: English ECE and AUROC at
318	    EN-optimal layer. Shows that α ~0.5 optimizes ECE-AUROC tradeoff. SB-ECE regularization
319	    provides genuine calibration benefit.'
320	  - 'Figure: β sensitivity heatmap — x-axis: log(β), y-axis: languages sorted by resource
321	    tier. Color: ΔAUROC over α-only. Shows near-zero change (white) across entire
322	    grid. Highlights absence of any language × β sweet spot.'
323	  - 'Figure: Transfer method ranking forest plot — each method as a row, showing median
324	    ΔAUROC with bootstrap 95% CI. Clear separation between geometric methods (linear-proj,
325	    few-shot) and distributional methods (CaCLR-β, mean-shift).'
326	  analysis: 'CaCLR''s β inertness is the paper''s centerpiece negative result. The
327	    analysis proceeds in three steps: (1) empirically, β has negligible effect (d=0.08,
328	    p=0.42) across 3 OOM and both architectures; (2) mechanistically, CKA analysis
329	    (plan_011) reveals that cross-lingual misalignment at deeper layers is geometric
330	    (rotation/scaling) rather than distributional (mean/covariance shift); (3) linear
331	    projection''s success (+3.5pp) confirms the geometric explanation — it succeeds
332	    precisely because it learns the rotation that MMD cannot represent. This three-part
333	    argument closes the distributional-matching path with both theory and evidence.
334	    The α-only variant retains value as a calibration regularizer — it improves ECE
335	    without hurting AUROC.
336	
337	    '
338	- name: Difficulty-Controlled Decomposition Ablation
339	  plan_id: plan_004
340	  description: 'IRT difficulty probes, project out difficulty direction, retrain correctness
341	    probes on residuals. 10 languages × 8 layers per model. Random-direction control.
342	
343	    '
344	  expected_results:
345	    difficulty_probe_r2_en_median_across_layers: 0.42
346	    difficulty_probe_r2_range:
347	    - 0.25
348	    - 0.55
349	    decomposition_transfer_delta_median: 0.012
350	    decomposition_transfer_delta_range:
351	    - -0.01
352	    - 0.035
353	    pct_combos_improved: 0.65
354	    pct_combos_improved_by_tier_high: 0.72
355	    pct_combos_improved_by_tier_mid: 0.65
356	    pct_combos_improved_by_tier_low: 0.53
357	    improvement_stronger_at_deep_layers: true
358	    improvement_at_shallow_layers_pct: 0.5
359	    improvement_at_deep_layers_pct: 0.78
360	    random_direction_delta_median: 0.003
361	    random_direction_delta_significant: false
362	    difficulty_correctness_cosine_median: 0.18
363	    difficulty_correctness_cosine_range:
364	    - 0.08
365	    - 0.3
366	    decomposition_vs_baseline_paired_p: 0.03
367	    decomposition_cohens_d: 0.28
368	  result_rationale: 'Decomposition works but is partial because the difficulty-capability
369	    separation is not clean. The difficulty direction (IRT-derived) captures ~42%
370	    variance in human difficulty scores (R²) — reasonable but not perfect, meaning
371	    the projection leaves residual difficulty signal mixed with capability. At deep
372	    layers, removing difficulty helps more often (78% of combos) because the capability-specific
373	    component dominates transfer degradation there — once you remove the shared difficulty
374	    signal, the residual is more language-specific and harder to transfer. At shallow
375	    layers, the improvement rate drops to ~50% (near chance) because both difficulty
376	    and capability signals are more entangled and less linearly separable. The 65%
377	    overall improvement rate is genuine but not universal — it demonstrates the decomposition
378	    is prescriptive for about two-thirds of settings. The random-direction control
379	    (median +0.3pp, not significant) confirms this isn''t a dimensionality-reduction
380	    artifact. Low-resource languages show weaker improvement (53%) because their correctness
381	    probes are noisier to begin with, and the difficulty projection may remove some
382	    of the limited signal they have. The modest Cohen''s d (0.28) reflects that improvements
383	    are real but small — this is a supporting analytical result, not a standalone
384	    method contribution.
385	
386	    '
387	  tables:
388	  - name: 'Table 8: Decomposition Results — 10 Languages × 8 Layers'
389	    description: 'Heatmap table: languages (rows) × layers (columns). Cells show ΔAUROC
390	      after difficulty removal. Green: improved (>0.5pp), white: unchanged, red: degraded.
391	      Marginal summaries: % improved per language, per layer. Shows concentration
392	      of improvement at deep layers and high-resource languages.
393	
394	      '
395	  - name: 'Table 9: Decomposition vs Random Direction Control'
396	    description: 'Comparison: difficulty projection vs random projection vs no projection.
397	      Median ΔAUROC, bootstrap CI, paired test. Confirms difficulty projection specifically
398	      — not arbitrary dimensionality reduction — drives improvement.
399	
400	      '
401	  figures_description:
402	  - 'Figure: Decomposition improvement rate vs layer depth — bar chart showing fraction
403	    of languages improved at each layer. Monotonically increasing trend from ~50%
404	    at shallowest to ~78% at deepest. Supports narrative that capability-specific
405	    component is the deep-layer transfer bottleneck.'
406	  analysis: 'Decomposition provides supporting evidence for the geometric misalignment
407	    narrative. The fact that difficulty removal helps more at deep layers aligns with
408	    the CKA finding — at depth, the capability-specific component (which is geometrically
409	    misaligned across languages) drives transfer failure, and removing the shared
410	    difficulty component isolates this effect. However, the partial success rate (65%)
411	    and modest effect size (d=0.28) keep this as supporting analysis rather than a
412	    standalone claim. The finding is prescriptive: researchers attempting cross-lingual
413	    probe transfer should first assess whether difficulty confounding explains their
414	    transfer gaps — in ~65% of cases, it partially does.
415	
416	    '
417	- name: Cross-Lingual Orthogonality Analysis
418	  plan_id: plan_005
419	  description: 'Verbalized confidence direction extraction, cosine similarity with
420	    correctness direction. 20 languages × 2 architectures. Resource-tier and family
421	    analysis.
422	
423	    '
424	  expected_results:
425	    en_cosine_qwen: 0.035
426	    en_cosine_llama: 0.038
427	    cosine_median_across_langs_qwen: 0.055
428	    cosine_median_across_langs_llama: 0.06
429	    cosine_max_across_langs: 0.1
430	    cosine_max_language: sw
431	    cosine_range:
432	    - 0.02
433	    - 0.1
434	    cosine_median_high_resource: 0.04
435	    cosine_median_mid_resource: 0.06
436	    cosine_median_low_resource: 0.085
437	    cosine_variance_high: 0.0003
438	    cosine_variance_mid: 0.0008
439	    cosine_variance_low: 0.0018
440	    all_langs_below_threshold: true
441	    cosine_vs_resource_spearman_rho: 0.52
442	    cosine_vs_resource_p: 0.018
443	  result_rationale: 'Orthogonality persists across languages because the separation
444	    between correctness and verbalized confidence is a structural property of how
445	    transformers process MCQA — the model''s internal "do I know this?" signal (correctness)
446	    and its verbalized "how confident am I?" output occupy orthogonal subspaces by
447	    design (the former is a representation-level property, the latter is optimized
448	    during RLHF/instruction-tuning for human-readable outputs). The English cosine
449	    (~0.035- 0.038) replicates Miao & Ungar (2026). Non-English cosines are slightly
450	    higher (median 0.055-0.060) because: (a) non-English confidence verbalization
451	    is noisier (models are less calibrated in non-English expression of uncertainty);
452	    (b) the confidence probe may capture some language-switching signal that correlates
453	    weakly with correctness (lower-resource languages trigger more uncertain generation
454	    behavior). The max cosine at 0.10 (sw) still satisfies the orthogonality threshold
455	    (<0.12) but shows more variance — Swahili''s limited pretraining data means both
456	    probes are noisier, and noise correlations inflate apparent cosine. The resource-
457	    tier gradient (rho=0.52, p=0.018) is a novel finding: orthogonality is stronger
458	    (lower cosine) for high-resource languages, suggesting that abundant pretraining
459	    data helps separate correctness from confidence representations. However, even
460	    the worst case (0.10) is far from the ~0.5+ that would indicate meaningful alignment,
461	    confirming that output-based calibration is structurally limited across all languages.
462	
463	    '
464	  tables:
465	  - name: 'Table 10: Correctness–Confidence Cosine Similarity Across Languages'
466	    description: '20 languages (rows, grouped by resource tier) × 2 architectures
467	      (column pairs). Each cell: cosine similarity ± bootstrap 95% CI. Bottom: tier
468	      medians and Spearman correlation with log(pretraining data estimate). All values
469	      < 0.12.
470	
471	      '
472	  figures_description:
473	  - 'Figure: Cosine similarity vs estimated pretraining data — scatter plot, 20 languages
474	    × 2 models. Log scale x-axis (pretraining tokens). Weak positive trend (more data
475	    → lower cosine → stronger orthogonality). Highlights sw/bn as outliers with highest
476	    cosine.'
477	  analysis: 'Orthogonality holds universally (max 0.10 < 0.12 threshold) but with
478	    a resource- tier gradient that is novel relative to Miao & Ungar''s English-only
479	    finding. This extends their claim to multilingual settings with a nuance: the
480	    structural separation is slightly weaker for low-resource languages, though never
481	    approaching a level that would make output-based calibration viable. This supports
482	    the paper''s broader argument that probe-based calibration is the right paradigm
483	    for all languages, but the cross-lingual transfer challenge is the bottleneck
484	    — not the underlying signal quality.
485	
486	    '
487	- name: Probe Complexity Comparison
488	  plan_id: plan_006
489	  description: 'Logistic regression vs 2-layer MLP at each probed layer for both models.
490	    English accuracy, cross-lingual transfer degradation, calibration quality.
491	
492	    '
493	  expected_results:
494	    logreg_en_best_auroc_qwen: 0.81
495	    mlp_en_best_auroc_qwen: 0.835
496	    logreg_en_best_auroc_llama: 0.79
497	    mlp_en_best_auroc_llama: 0.815
498	    logreg_zs_median_qwen: 0.7
499	    mlp_zs_median_qwen: 0.665
500	    logreg_zs_median_llama: 0.68
501	    mlp_zs_median_llama: 0.645
502	    logreg_transfer_gap: 0.11
503	    mlp_transfer_gap: 0.17
504	    logreg_ece_median: 0.068
505	    mlp_ece_median: 0.075
506	    mlp_advantage_en_deep_layers: 0.03
507	    mlp_advantage_en_shallow_layers: 0.01
508	    logreg_better_transfer_pct_langs: 0.8
509	  result_rationale: 'MLP probes achieve ~2.5pp higher English AUROC because they can
510	    capture nonlinear interactions in the representation — the correctness signal
511	    has a small nonlinear component that logistic regression misses. However, this
512	    nonlinear component is language-specific (learned from English data, doesn''t
513	    generalize), so MLP probes show 6pp larger transfer gap than logistic regression.
514	    The MLP essentially overfits to English-specific nonlinearities in the correctness
515	    representation. This confirms the hypothesis that linear probes transfer better
516	    cross-lingually — the linear component of the correctness signal is more universal
517	    across languages, while nonlinear components are language-specific. The MLP advantage
518	    is concentrated at deep layers (+3pp at deep vs +1pp at shallow) because deeper
519	    representations have more complex, language-specific structure for the MLP to
520	    exploit. 80% of languages see better transfer with logistic regression, with the
521	    exceptions being high- resource languages (zh, es) where the MLP''s nonlinear
522	    component partially transfers due to shared pretraining features. This result
523	    justifies the paper''s focus on logistic regression probes and reinforces the
524	    geometric (linear) framing.
525	
526	    '
527	  tables:
528	  - name: 'Table S1: Probe Complexity — English AUROC and Transfer Gap by Layer'
529	    description: 'Supplementary table. Layers (rows) × (LogReg EN, MLP EN, LogReg
530	      ZS-median, MLP ZS-median, LogReg gap, MLP gap) for each model. Shows MLP''s
531	      higher EN AUROC comes at cost of larger transfer gap. Gap difference increases
532	      with depth.
533	
534	      '
535	  figures_description:
536	  - 'Figure: Transfer gap (EN AUROC - ZS median) vs layer depth for LogReg and MLP.
537	    Two lines diverging at deeper layers — MLP gap grows faster, confirming linear
538	    probes are preferable for cross-lingual transfer.'
539	  analysis: 'This experiment justifies the methodological choice of logistic regression
540	    probes and provides additional evidence for the geometric/linear framing. If the
541	    correctness signal were deeply nonlinear, MLP''s advantage would transfer — the
542	    fact that it doesn''t confirms that the transferable component is linear. Goes
543	    in supplementary material as a methodological validation.
544	
545	    '
546	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
547	  plan_id: plan_007
548	  description: 'Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages
549	    each). Validates generalization beyond GlobalMMLU.
550	
551	    '
552	  expected_results:
553	    belebele_en_best_auroc_qwen: 0.78
554	    belebele_zs_median_qwen: 0.68
555	    belebele_pareto_rho_median: -0.48
556	    belebele_linear_proj_delta: 0.03
557	    belebele_caclr_beta_delta: 0.003
558	    mmlupx_en_best_auroc_qwen: 0.82
559	    mmlupx_zs_median_qwen: 0.69
560	    mmlupx_pareto_rho_median: -0.5
561	    mmlupx_linear_proj_delta: 0.033
562	    mmlupx_caclr_beta_delta: 0.002
563	    auroc_rank_correlation_globalmmlu_vs_belebele: 0.82
564	    auroc_rank_correlation_globalmmlu_vs_mmlupx: 0.88
565	    method_ranking_consistent_across_benchmarks: true
566	  result_rationale: 'Belebele is a reading comprehension benchmark — fundamentally
567	    different from MCQA knowledge testing. The correctness signal is still present
568	    (models either comprehend or don''t) but Belebele''s English AUROC is slightly
569	    lower (0.78 vs 0.81) because reading comprehension correctness is less cleanly
570	    encoded than factual knowledge correctness. The Pareto rho is slightly weaker
571	    (-0.48) because Belebele''s parallel passages provide more uniform cross-lingual
572	    signal than GlobalMMLU''s diverse topics. MMLU-ProX, being closer to GlobalMMLU
573	    in format, shows more similar results (0.82 EN AUROC, -0.50 rho). The key finding
574	    is that method rankings are consistent — linear projection still outperforms CaCLR,
575	    and CaCLR''s β term remains inert across benchmarks. This rules out the possibility
576	    that CaCLR''s failure is GlobalMMLU-specific. The high rank correlations (0.82–0.88)
577	    between benchmarks confirm that per-language transfer difficulty is a property
578	    of the model''s multilingual representations, not the benchmark.
579	
580	    '
581	  tables:
582	  - name: 'Table S2: Cross-Benchmark Generalization'
583	    description: 'Supplementary. Benchmarks (rows: GlobalMMLU, Belebele, MMLU-ProX)
584	      × key metrics (EN AUROC, ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ). Shows
585	      consistent patterns across benchmarks. Rank correlation between per-language
586	      AUROCs.
587	
588	      '
589	  figures_description:
590	  - 'Figure: Per-language AUROC scatter — GlobalMMLU vs Belebele, GlobalMMLU vs MMLU-ProX.
591	    Each point is a language. High correlation confirms benchmark-invariant transfer
592	    difficulty ranking.'
593	  analysis: 'Benchmark generalization confirms all findings are not artifacts of GlobalMMLU.
594	    The consistent method ranking across three benchmarks strengthens the negative
595	    result — CaCLR''s β inertness is a fundamental property of distributional matching
596	    vs geometric misalignment, not a benchmark-specific failure. Goes in supplementary
597	    or a short main-text paragraph.
598	
599	    '
600	- name: INT8 Validation Ablation
601	  plan_id: plan_010
602	  description: 'INT8 vs FP16 comparison at 5 representative layers for Llama 4 Scout
603	    on 5% subset.
604	
605	    '
606	  expected_results:
607	    int8_fp16_auroc_max_diff: 0.008
608	    int8_fp16_auroc_mean_diff: 0.003
609	    int8_fp16_ece_max_diff: 0.012
610	    int8_fp16_correlation_r: 0.997
611	    int8_fp16_rank_agreement_pct: 0.98
612	    distortion_significant: false
613	  result_rationale: 'INT8 weight-only quantization preserves the vast majority of
614	    activation-space structure because (a) it quantizes weights, not activations —
615	    the internal representations used for probing are computed in higher precision;
616	    (b) 7B+ models are robust to INT8 quantization (well-established in the quantization
617	    literature); (c) correctness probes operate on high-dimensional representations
618	    (4096+ dims) where small per-dimension perturbations from quantization average
619	    out. The max AUROC difference of 0.8pp across any layer is within bootstrap confidence
620	    intervals. The 0.997 correlation between INT8 and FP16 probe scores confirms that
621	    quantization shifts all scores by a near-constant offset without affecting ranking.
622	    This validation is necessary for reviewer reassurance but expected to be a non-issue.
623	
624	    '
625	  tables:
626	  - name: 'Table S3: INT8 vs FP16 Validation'
627	    description: 'Supplementary. 5 layers × metrics (INT8 AUROC, FP16 AUROC, Δ, rank
628	      correlation). All differences within bootstrap CI. Conclusion: INT8 does not
629	      distort correctness signals.
630	
631	      '
632	  figures_description: []
633	  analysis: 'Straightforward validation that INT8 quantization doesn''t affect conclusions.
634	    One paragraph in supplementary material with the table. Addresses anticipated
635	    reviewer concern #5.
636	
637	    '
638	- name: CKA Cross-Lingual Representation Similarity
639	  plan_id: plan_011
640	  description: 'CKA (linear kernel) between English and each target language at every
641	    probed layer, both models. Correlate CKA with transfer AUROC.
642	
643	    '
644	  expected_results:
645	    cka_en_zh_shallow_layer12_qwen: 0.88
646	    cka_en_zh_deep_layer72_qwen: 0.62
647	    cka_en_sw_shallow_layer12_qwen: 0.78
648	    cka_en_sw_deep_layer72_qwen: 0.38
649	    cka_median_shallow_across_langs: 0.84
650	    cka_median_deep_across_langs: 0.52
651	    cka_decrease_with_depth_significant: true
652	    cka_transfer_pearson_r_qwen: 0.62
653	    cka_transfer_pearson_r_llama: 0.54
654	    cka_transfer_pearson_r_pooled: 0.58
655	    cka_transfer_pearson_p: 1.0e-05
656	    cka_deep_high_resource_median: 0.6
657	    cka_deep_mid_resource_median: 0.48
658	    cka_deep_low_resource_median: 0.36
659	    mmd_transfer_pearson_r: 0.25
660	    mmd_explains_variance_pct: 6
661	    cka_explains_variance_pct: 34
662	  result_rationale: 'CKA measures representational similarity including geometric
663	    structure (rotation, scaling), while MMD measures distributional distance (mean,
664	    variance, higher moments). CKA decreases with depth because deeper transformer
665	    layers specialize more for language-specific processing — the cross-lingual alignment
666	    enforced by shared vocabulary embeddings and early layers gradually gives way
667	    to language- specific feature extraction. The CKA–transfer correlation (r=0.58)
668	    is moderate- to-strong: it explains 34% of variance in transfer AUROC, confirming
669	    that representational geometry is a major (but not the only) factor in transfer
670	    success. The remaining variance comes from factors like probe quality, dataset
671	    difficulty distribution, and non-geometric aspects of the representation. Critically,
672	    CKA (r=0.58) substantially outpredicts MMD (r=0.25) as a predictor of transfer
673	    success — this is the key mechanistic finding. If cross-lingual misalignment were
674	    distributional (mean/covariance shift), MMD would predict transfer as well as
675	    or better than CKA. The fact that CKA is 2.3× more predictive demonstrates that
676	    the misalignment is geometric (rotation/scaling of the entire representational
677	    space), not merely distributional. This directly explains why MMD-based CaCLR
678	    fails: it optimizes the wrong measure of alignment. The resource-tier CKA gradient
679	    (0.60 > 0.48 > 0.36 at deep layers) mirrors the transfer AUROC gradient, providing
680	    a mechanistic explanation for why low-resource languages transfer worse — their
681	    deep-layer representations are more geometrically dissimilar from English.
682	
683	    '
684	  tables:
685	  - name: 'Table 11: CKA Similarity — Languages × Layers'
686	    description: 'Probed layers (rows) × 20 languages (columns, sorted by resource
687	      tier). Cells: CKA values. Clear gradient: high CKA at shallow layers, decreasing
688	      with depth. Resource-tier banding visible. Both models shown.
689	
690	      '
691	  - name: 'Table 12: CKA vs MMD as Transfer Predictors'
692	    description: 'Predictor comparison: CKA linear, CKA RBF, MMD, H-divergence proxy.
693	      Columns: Pearson r, R², p-value. CKA linear clearly dominant. Demonstrates geometric
694	      > distributional as explanation.
695	
696	      '
697	  figures_description:
698	  - 'Figure: CKA heatmap — layers (y-axis) × languages (x-axis, sorted by transfer
699	    AUROC). Color intensity = CKA. Clear diagonal structure: high CKA co-occurs with
700	    high transfer AUROC. Visual demonstration of the CKA–transfer link.'
701	  - 'Figure: CKA vs transfer AUROC scatter — each point is a (layer, language) pair.
702	    Color: resource tier. Linear fit line with r=0.58. Contrasted with MMD vs transfer
703	    scatter (r=0.25) in adjacent panel. The visual gap between the two correlations
704	    is the paper''s mechanistic argument.'
705	  - 'Figure: CKA depth profile — CKA vs layer depth for 3 representative languages
706	    (zh, tr, sw). Three curves showing parallel decline but at different levels. Annotated
707	    with corresponding transfer AUROC at each layer.'
708	  analysis: 'CKA analysis is the mechanistic backbone of the paper. It upgrades the
709	    contribution from "we measured that transfer fails at deep layers" to "we explain
710	    WHY transfer fails — geometric misalignment increases with depth, and this misalignment
711	    type (rotation/scaling) is specifically not addressable by distributional matching
712	    (MMD)." The CKA–transfer correlation (r=0.58) provides quantitative support, and
713	    the CKA vs MMD comparison (34% vs 6% variance explained) provides the critical
714	    distinction that makes the negative CaCLR result theoretically interpretable rather
715	    than just empirically observed. This transforms the paper from a measurement study
716	    to one with mechanistic insight.
717	
718	    '
719	- name: Linear Projection Sensitivity Analysis
720	  plan_id: plan_012
721	  description: 'Vary parallel pairs (10, 20, 50, 100, 200) for linear projection.
722	    Both models × 5 layers × 20 languages.
723	
724	    '
725	  expected_results:
726	    pairs_10_delta_auroc_median: 0.012
727	    pairs_20_delta_auroc_median: 0.022
728	    pairs_50_delta_auroc_median: 0.03
729	    pairs_100_delta_auroc_median: 0.035
730	    pairs_200_delta_auroc_median: 0.036
731	    saturation_knee_point: 70
732	    pairs_for_90pct_max_improvement: 55
733	    pairs_for_95pct_max_improvement: 85
734	    pairs_10_std_across_langs: 0.025
735	    pairs_50_std_across_langs: 0.012
736	    pairs_100_std_across_langs: 0.008
737	    saturation_consistent_across_models: true
738	    qwen_saturation_knee: 65
739	    llama_saturation_knee: 75
740	  result_rationale: 'Linear projection learns a rotation matrix mapping source-language
741	    representations to target-language space. The sample complexity for estimating
742	    a linear mapping in high-dimensional space (4096+ dims) is surprisingly low because:
743	    (a) the effective dimensionality of the correctness-relevant subspace is much
744	    lower than the full representation dimensionality — the probe operates in a low-rank
745	    subspace; (b) parallel pairs provide direct supervision on the mapping, unlike
746	    distributional matching which uses indirect statistical signals. With 10 pairs,
747	    the mapping is underdetermined but captures the dominant rotation component (+1.2pp).
748	    By 50 pairs, 90% of the achievable improvement is captured as the major rotation/scaling
749	    axes are identified. The knee point at ~70 pairs and saturation by 100 pairs is
750	    consistent with the cross-lingual alignment literature (MUSE, VecMap) where bilingual
751	    dictionaries of 50–100 entries suffice for word-level alignment. The slight architecture
752	    difference in knee points (65 vs 75) reflects that Llama 4''s representations
753	    may require slightly more pairs to estimate the rotation due to its MoE routing
754	    introducing more heterogeneity. The practical implication is clear: ~50-100 parallel
755	    pairs (trivially obtainable from GlobalMMLU train split) are sufficient to match
756	    or exceed CaCLR''s entire training pipeline.
757	
758	    '
759	  tables:
760	  - name: 'Table 13: Linear Projection — Sample Efficiency'
761	    description: 'Pair counts (rows: 10, 20, 50, 100, 200) × summary statistics (median
762	      ΔAUROC, mean, std, min, max, % languages improved). Both models. Shows clear
763	      diminishing returns after 50 pairs.
764	
765	      '
766	  figures_description:
767	  - 'Figure: Learning curve — x-axis: number of parallel pairs (log scale), y-axis:
768	    median ΔAUROC. Two curves (Qwen3, Llama4) with shaded ±1 std band. Annotated knee
769	    point. Horizontal dashed line: CaCLR-full ΔAUROC for comparison — linear projection
770	    surpasses CaCLR at just ~20 pairs.'
771	  analysis: 'Linear projection''s sample efficiency is the constructive complement
772	    to CaCLR''s negative result. The message: you don''t need MMD-based distributional
773	    matching (which doesn''t work anyway) — you just need ~50-100 parallel pairs and
774	    a linear mapping. This is practically actionable and theoretically consistent
775	    with the geometric explanation (linear projection learns the rotation that MMD
776	    cannot). The learning curve figure — showing linear projection surpassing CaCLR
777	    at ~20 pairs — is one of the paper''s most compelling visuals.
778	
779	    '
780	- name: Probing Control Tasks (Hewitt & Liang 2019)
781	  plan_id: plan_013
782	  description: 'Train probes on randomly permuted labels at each layer. Selectivity
783	    analysis across layers and languages.
784	
785	    '
786	  expected_results:
787	    control_auroc_en_median: 0.545
788	    control_auroc_en_range:
789	    - 0.52
790	    - 0.58
791	    control_auroc_noneng_median: 0.54
792	    selectivity_en_median: 0.265
793	    selectivity_en_range:
794	    - 0.18
795	    - 0.31
796	    selectivity_noneng_median_high_resource: 0.2
797	    selectivity_noneng_median_mid_resource: 0.16
798	    selectivity_noneng_median_low_resource: 0.1
799	    selectivity_min_across_all: 0.08
800	    selectivity_min_language: sw
801	    selectivity_min_layer: layer_4
802	    all_selectivities_positive: true
803	    pct_above_10pp: 0.88
804	    pct_above_10pp_high_resource: 0.95
805	    pct_above_10pp_low_resource: 0.7
806	    selectivity_peaks_at_mid_depth: true
807	    selectivity_peak_layer_pct_depth: 0.55
808	  result_rationale: 'Control tasks with random labels test whether probe capacity
809	    (model expressiveness) alone can achieve high AUROC without genuine correctness
810	    signal. The control AUROC of ~0.54-0.55 (barely above chance at 0.50) confirms
811	    that logistic regression probes do not have sufficient capacity to memorize random
812	    label assignments in high-dimensional space — any AUROC above this baseline reflects
813	    genuine signal. English selectivity (median 0.265) is strong: the probe captures
814	    real correctness information 26.5pp above what capacity alone could achieve. Non-English
815	    selectivity decreases with resource tier because: (a) the correctness signal itself
816	    is weaker for languages with less pretraining data; (b) the cross-lingual transfer
817	    means probes must generalize from English-learned patterns, which is inherently
818	    harder for distant languages. Low-resource languages (sw, bn) show selectivity
819	    ~10pp, still positive but approaching the threshold where a reviewer might question
820	    signal quality. The 88% of language-layer combinations exceeding 10pp provides
821	    reasonable validation, but the 30% failure rate for low-resource languages at
822	    this threshold is a genuine limitation that the paper should acknowledge. Selectivity
823	    peaks at mid-depth (~55%) because shallow layers have weaker correctness signals
824	    (less processed) and very deep layers have stronger but more language-specific
825	    signals (high probe AUROC but also higher control AUROC due to richer features).
826	
827	    '
828	  tables:
829	  - name: 'Table S4: Control Task Selectivity'
830	    description: 'Supplementary. Languages (rows, grouped by resource tier) × representative
831	      layers (columns). Cells: selectivity (probe AUROC - control AUROC). Color-coded:
832	      green >15pp, yellow 10-15pp, orange 5-10pp. Shows resource- tier gradient in
833	      selectivity.
834	
835	      '
836	  figures_description:
837	  - 'Figure: Selectivity by resource tier — box plots for HIGH, MID, LOW resource
838	    tiers. Shows decreasing median and increasing variance for lower-resource tiers.
839	    Dashed line at 10pp threshold. Most points above threshold but LOW tier shows
840	    some below.'
841	  analysis: 'Control tasks validate that probe AUROC reflects genuine correctness
842	    signal for the large majority of settings (88% above 10pp). The resource-tier
843	    gradient in selectivity is a limitation to acknowledge: for low-resource languages,
844	    probe signal quality is weaker, and conclusions about transfer should be interpreted
845	    with this caveat. This doesn''t undermine the paper''s core claims (which are
846	    about the mechanism of transfer failure, not about achieving high probe quality
847	    in every language) but sets appropriate epistemic bounds.
848	
849	    '
850	- name: Gemma 4 31B Dense Pareto Frontier
851	  plan_id: plan_008
852	  description: 'Third architecture for camera-ready. 60 layers, dense, FP16. Full
853	    Pareto frontier, 20+ languages. Dense vs MoE contrast.
854	
855	    '
856	  expected_results:
857	    en_best_auroc: 0.8
858	    en_best_layer: 45
859	    zs_transfer_auroc_median: 0.69
860	    best_transfer_layer: 33
861	    pareto_rho_per_lang_median: -0.58
862	    zs_langs_above_0p65: 12
863	    pareto_rho_smoother_than_moe: true
864	    pareto_rho_std_across_langs_gemma: 0.12
865	    pareto_rho_std_across_langs_qwen: 0.16
866	    pareto_rho_std_across_langs_llama: 0.15
867	    cka_depth_decline_steeper_dense: true
868	    linear_proj_delta_median: 0.033
869	  result_rationale: 'Gemma 4 31B Dense provides the critical dense-vs-MoE architectural
870	    contrast. As a dense model, every token passes through every layer (no routing),
871	    creating more uniform layer-to-layer transformations. This produces a smoother
872	    Pareto frontier (lower rho variance across languages: 0.12 vs 0.15-0.16 for MoE
873	    models) because the depth-transfer tradeoff is more consistent without routing-induced
874	    heterogeneity. The rho itself is slightly stronger negative (-0.58) because dense
875	    models show a cleaner monotonic decline in cross-lingual alignment with depth
876	    — MoE routing partially breaks this monotonicity by allowing some expert pathways
877	    to maintain cross-lingual features at deeper layers. CKA declines more steeply
878	    with depth in the dense model, confirming that MoE routing provides a modest buffer
879	    against geometric misalignment (different experts can specialize differently per
880	    language). English AUROC (0.80) is comparable to the larger MoE models despite
881	    smaller parameter count because the 31B dense architecture is parameter-efficient
882	    for representation quality. This is a P2 camera-ready experiment that strengthens
883	    the architecture-dependence claim from "two MoE models differ moderately" to "dense
884	    vs MoE is a qualitatively distinct contrast."
885	
886	    '
887	  tables:
888	  - name: 'Table CR1: Three-Architecture Pareto Comparison'
889	    description: 'Camera-ready. Architecture (rows: Qwen3-MoE, Llama4-MoE, Gemma4-Dense)
890	      × key metrics (EN AUROC, ZS median, rho median, rho std, CKA slope, linear-proj
891	      Δ). Highlights dense vs MoE contrast in rho variance and CKA slope.
892	
893	      '
894	  figures_description:
895	  - 'Figure: Three-panel Pareto frontier comparison — Qwen3-MoE, Llama4-MoE, Gemma4-Dense
896	    side-by-side. Dense model shows smoother, more monotonic frontier. Visual argument
897	    for architecture-dependence.'
898	  analysis: 'Camera-ready addition. The dense-vs-MoE contrast is the strongest architecture-
899	    dependence evidence: MoE routing introduces heterogeneity that partially buffers
900	    against geometric misalignment at deep layers, while dense models show cleaner
901	    depth-dependent degradation. This doesn''t change the paper''s conclusions but
902	    provides a more compelling architectural contrast than two MoE models alone.
903	
904	    '
905	- name: Extended Language Coverage (50+ Languages)
906	  plan_id: plan_009
907	  description: 'Expand from 20 to 50+ languages for camera-ready. Full GlobalMMLU/Belebele
908	    language sets.
909	
910	    '
911	  expected_results:
912	    total_languages: 52
913	    zs_langs_above_0p65: 28
914	    zs_median_auroc_52lang: 0.66
915	    zs_auroc_range:
916	    - 0.5
917	    - 0.74
918	    new_low_resource_langs_below_0p55:
919	    - am
920	    - my
921	    - zu
922	    - sn
923	    - rw
924	    resource_tier_gradient_replicates: true
925	    pareto_rho_median_52lang: -0.49
926	    linear_proj_delta_median_52lang: 0.031
927	    tail_langs_below_0p55_count: 8
928	    tail_langs_above_0p70_count: 12
929	  result_rationale: 'Expanding to 52 languages adds many more low-resource and typologically
930	    diverse languages. The median AUROC drops slightly (0.66 vs 0.70 for the curated
931	    20) because the additional languages are disproportionately low-resource. Five
932	    extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda)
933	    fall below 0.55, approaching chance performance — these languages have minimal
934	    pretraining representation in both models. The resource-tier gradient continues
935	    to hold and becomes even more pronounced with the extended tail. Pareto rho weakens
936	    slightly (-0.49) because many of the new languages show weak, noisy correlations
937	    due to low base probe quality. Linear projection improvement remains consistent
938	    (+3.1pp), confirming the geometric correction generalizes beyond the curated language
939	    set. The practical message: probe-based cross-lingual calibration is viable for
940	    ~28/52 languages (54%) without any target-language data, and linear projection
941	    extends this to ~35/52 (67%). The remaining ~17 languages need language-specific
942	    probes or alternative approaches.
943	
944	    '
945	  tables:
946	  - name: 'Table CR2: Extended Language Coverage — 52 Languages'
947	    description: 'Camera-ready. Full 52-language results sorted by zero-shot AUROC.
948	      Columns: language, family, resource tier, ZS AUROC, linear-proj AUROC, few-shot-100
949	      AUROC. Grouped into tiers: >0.70 (strong transfer), 0.65-0.70 (viable), 0.55-0.65
950	      (marginal), <0.55 (failed).
951	
952	      '
953	  figures_description:
954	  - 'Figure: Language coverage map — world map with countries colored by best zero-shot
955	    transfer AUROC. Visual demonstration of where probe-based calibration works and
956	    fails geographically.'
957	  analysis: 'Camera-ready extension. The 52-language analysis adds scale but the median-tier
958	    conclusion is clear: probe-based cross-lingual calibration works for a majority
959	    but not all languages, and the resource-tier gradient is the dominant predictor
960	    of success. This sets realistic expectations for practitioners and motivates future
961	    work on low-resource language probe training.'
962	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "816fb248-1c6f-4e58-ab63-d8204e4adfbc",
  "isSidechain": false,
  "promptId": "acf24c0c-9db5-4a00-b354-14e98fea03c7",
  "type": "user",
  "uuid": "e4975bea-3167-497f-aebb-ace1c3c1f5f0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml",
      "content": "tier: median\nnarrative_guidance: 'Analysis paper with principled negative result as centerpiece.\n  Narrative arc: (1) Pareto frontier established on two large MoE architectures —\n  qualitatively replicates MVP findings but rho is moderate (median ~-0.52), confirming\n  architecture-dependent shape; (2) CKA reveals geometric misalignment increasing\n  with depth — CKA-transfer correlation r≈0.58 provides mechanistic explanation for\n  WHY deeper layers transfer worse; (3) CaCLR consistency loss (β) is inert across\n  3 OOM sweep — this is PREDICTED by the geometric explanation: MMD matches distributions\n  but cannot correct the rotation of the correctness direction across language subspaces;\n  (4) Linear projection succeeds (~+3.5pp over zero-shot) precisely because it learns\n  the rotation that MMD cannot, saturating at ~70 parallel pairs. Decomposition and\n  orthogonality are supporting evidence. Decomposition shows difficulty is shared\n  but capability-specific component drives degradation (~65% of combos improved).\n  Orthogonality persists across languages (cosine < 0.10) but with more variance in\n  low-resource languages. Control tasks confirm probe selectivity (>10pp) but sw/bn\n  are weaker. ECE improvements over temperature scaling are negligible — emphasize\n  AUROC and mechanistic understanding. Target: borderline to weak accept at EACL.\n\n  '\nimagined_experiments:\n- name: Qwen3-235B-A22B Full Pareto Frontier\n  plan_id: plan_001\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): 24\n    probed layers, 20 languages, 5 transfer conditions (zero-shot, mean-shift, linear\n    projection, few-shot 25/100, CaCLR). Per-language and global Spearman rho.\n\n    '\n  expected_results:\n    en_best_auroc: 0.81\n    en_best_layer: 72\n    en_best_ece_raw: 0.17\n    en_best_ece_tempcal: 0.065\n    temp_scaling_T: 5.8\n    en_auroc_range:\n    - 0.58\n    - 0.81\n    en_auroc_50pct_depth_layer47: 0.76\n    zs_transfer_auroc_median_20lang_at_en_optimal: 0.63\n    zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.7\n    best_transfer_layer: 48\n    pareto_rho_global: -0.58\n    pareto_rho_per_lang_median: -0.51\n    pareto_rho_per_lang_range:\n    - -0.78\n    - -0.21\n    zs_langs_above_0p65: 13\n    zs_auroc_zh: 0.74\n    zs_auroc_es: 0.73\n    zs_auroc_fr: 0.73\n    zs_auroc_de: 0.72\n    zs_auroc_ar: 0.7\n    zs_auroc_hi: 0.69\n    zs_auroc_ru: 0.71\n    zs_auroc_ko: 0.69\n    zs_auroc_ja: 0.7\n    zs_auroc_pt: 0.72\n    zs_auroc_vi: 0.68\n    zs_auroc_tr: 0.67\n    zs_auroc_id: 0.68\n    zs_auroc_th: 0.66\n    zs_auroc_pl: 0.69\n    zs_auroc_uk: 0.68\n    zs_auroc_he: 0.66\n    zs_auroc_el: 0.65\n    zs_auroc_sw: 0.58\n    zs_auroc_bn: 0.57\n    mean_shift_delta_auroc_median: 0.0\n    linear_proj_delta_auroc_over_zs_median: 0.035\n    fewshot_25_delta_auroc_over_zs_median: 0.025\n    fewshot_100_delta_auroc_over_zs_median: 0.045\n    ece_reduction_vs_temp_scaling_median: 0.008\n  result_rationale: 'Qwen3-235B-A22B is a 94-layer MoE model — significantly deeper\n    than the 7B MVP. The English best AUROC rises to 0.81 because the larger model\n    encodes stronger correctness signals (more parameters, more knowledge). The best\n    English layer is at ~76% depth (layer 72), consistent with the MVP pattern where\n    correctness peaks in deep-but-not-final layers. The Pareto frontier is present\n    but rho is moderate (-0.51 median per-language) because: (a) the MoE routing creates\n    more heterogeneous layer representations, reducing the clean monotonic depth-degradation\n    pattern seen in dense models; (b) some languages (especially high-resource zh/es/fr)\n    have strong multilingual representations even at deeper layers due to extensive\n    pretraining data, attenuating the negative correlation. The per-language rho range\n    [-0.78, -0.21] reflects that low-resource languages (sw, bn) show stronger negative\n    correlation (their representations diverge from English more sharply at depth)\n    while high-resource languages show weaker correlation (they maintain reasonable\n    alignment throughout). 13/20 languages cross 0.65 AUROC — most European and major\n    Asian languages transfer adequately at optimal layers, but sw (0.58) and bn (0.57)\n    remain below threshold due to limited pretraining representation for these languages.\n    Mean-shift produces exactly zero AUROC change (rank-invariance proof holds), confirming\n    the MVP finding. Linear projection (+3.5pp) outperforms few-shot-25 (+2.5pp) because\n    it directly corrects geometric misalignment rather than relying on a small labeled\n    sample. ECE improvement over temperature scaling is marginal (0.8pp) because probe-based\n    calibration and temperature scaling address different aspects — at the median\n    tier, probes don''t provide much additional calibration beyond what temperature\n    scaling already captures.\n\n    '\n  tables:\n  - name: 'Table 1: Qwen3-235B-A22B Pareto Frontier — Zero-Shot Transfer AUROC by\n      Language × Layer'\n    description: '24 probed layers (rows) × 20 languages + English (columns). Cells\n      show AUROC. Bold: best layer per language. Gray shading: layers within 1pp of\n      best. Bottom rows: global and per-language Spearman rho with 95% bootstrap CI.\n      Key pattern: English-optimal layer (72) ≠ transfer-optimal layer (48) for most\n      languages. High-resource languages show flatter profiles; low-resource show\n      steeper drop-off at deep layers.\n\n      '\n  - name: 'Table 2: Qwen3-235B-A22B Transfer Method Comparison at Fixed Layers'\n    description: '5 transfer methods (columns) × 20 languages (rows), evaluated at\n      two fixed layers (50% depth = layer 47, EN-optimal = layer 72) plus per-language\n      oracle. Shows AUROC and ΔAUROC vs zero-shot. Bootstrap 95% CI and paired permutation\n      test p-values. Cohen''s d for each method vs zero-shot baseline.\n\n      '\n  figures_description:\n  - 'Figure: Pareto frontier scatter plot — x-axis: English AUROC, y-axis: median\n    zero-shot transfer AUROC across 20 langs. Each point is a layer. Annotated with\n    layer numbers. Pareto-optimal layers highlighted. Separate curves for resource\n    tiers (high/mid/low) showing tier-dependent frontier shape.'\n  - 'Figure: Per-language Spearman rho bar chart — 20 bars sorted by rho magnitude.\n    Color-coded by resource tier. Error bars show bootstrap 95% CI. Horizontal line\n    at rho = -0.5 for reference.'\n  analysis: 'The Pareto frontier replicates on this large MoE model but with moderate\n    per-language rho (-0.51 median). The architecture-dependent shape is visible:\n    MoE routing creates more variable layer representations, so the depth-transfer\n    tradeoff is less smooth than in a dense model. The key finding is that 13/20 languages\n    achieve usable zero-shot transfer (>0.65 AUROC) at optimal layers, validating\n    the approach for most languages. The 7 languages below threshold cluster in low-resource\n    (sw, bn) and morphologically distant categories (th, he at marginal 0.66). Linear\n    projection provides the most consistent improvement across languages.\n\n    '\n- name: Llama 4 Scout Full Pareto Frontier\n  plan_id: plan_002\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): 12 probed\n    layers, 20 languages, 5 transfer conditions. Per-language Spearman rho.\n\n    '\n  expected_results:\n    en_best_auroc: 0.79\n    en_best_layer: 36\n    en_best_ece_raw: 0.19\n    en_best_ece_tempcal: 0.07\n    temp_scaling_T: 6.0\n    en_auroc_range:\n    - 0.6\n    - 0.79\n    en_auroc_50pct_depth_layer24: 0.74\n    zs_transfer_auroc_median_20lang_at_en_optimal: 0.62\n    zs_transfer_auroc_median_20lang_at_best_transfer_layer: 0.68\n    best_transfer_layer: 24\n    pareto_rho_global: -0.62\n    pareto_rho_per_lang_median: -0.54\n    pareto_rho_per_lang_range:\n    - -0.82\n    - -0.28\n    zs_langs_above_0p65: 11\n    zs_auroc_zh: 0.72\n    zs_auroc_es: 0.71\n    zs_auroc_fr: 0.71\n    zs_auroc_de: 0.7\n    zs_auroc_ar: 0.68\n    zs_auroc_hi: 0.67\n    zs_auroc_ru: 0.69\n    zs_auroc_ko: 0.66\n    zs_auroc_ja: 0.67\n    zs_auroc_pt: 0.7\n    zs_auroc_vi: 0.65\n    zs_auroc_tr: 0.64\n    zs_auroc_id: 0.66\n    zs_auroc_th: 0.63\n    zs_auroc_pl: 0.67\n    zs_auroc_uk: 0.65\n    zs_auroc_he: 0.63\n    zs_auroc_el: 0.62\n    zs_auroc_sw: 0.55\n    zs_auroc_bn: 0.54\n    mean_shift_delta_auroc_median: 0.0\n    linear_proj_delta_auroc_over_zs_median: 0.032\n    fewshot_25_delta_auroc_over_zs_median: 0.022\n    fewshot_100_delta_auroc_over_zs_median: 0.04\n    ece_reduction_vs_temp_scaling_median: 0.005\n  result_rationale: 'Llama 4 Scout has fewer layers (48 vs 94) and a different MoE\n    architecture from Qwen3. The English best AUROC is slightly lower (0.79 vs 0.81)\n    reflecting somewhat weaker correctness encoding in a shallower architecture. The\n    Pareto rho is slightly stronger negative (-0.54 vs -0.51) because with fewer layers,\n    each layer step represents a larger proportional depth change, making the depth-transfer\n    tradeoff more pronounced. The best transfer layer at 50% depth (layer 24) is consistent\n    with the pattern that mid-depth layers balance English quality and cross-lingual\n    alignment. 11/20 languages cross 0.65, slightly fewer than Qwen3 — Llama 4''s\n    multilingual pretraining may be less balanced, particularly for mid-resource languages\n    like tr (0.64) and vi (0.65) that were marginal on Qwen3. Low-resource sw (0.55)\n    and bn (0.54) are again the weakest, confirming this is a fundamental limitation\n    of pretraining representation rather than architecture-specific. The same qualitative\n    Pareto pattern holds but the quantitative frontier shape differs — the drop-off\n    from English-optimal to transfer-optimal is steeper on Llama 4, confirming architecture-dependence\n    without requiring architecture-specific tuning as a paper claim.\n\n    '\n  tables:\n  - name: 'Table 3: Llama 4 Scout Pareto Frontier — Zero-Shot Transfer AUROC by Language\n      × Layer'\n    description: '12 probed layers × 20 languages + English. Same format as Table\n      1. Key contrast with Qwen3: steeper Pareto drop-off, fewer layers in the Pareto-optimal\n      set due to coarser layer sampling.\n\n      '\n  - name: 'Table 4: Llama 4 Scout Transfer Method Comparison'\n    description: 'Same format as Table 2. Llama 4 Scout results. Key finding: linear\n      projection improvement (+3.2pp) is comparable to Qwen3, suggesting the geometric\n      correction transfers across architectures.\n\n      '\n  figures_description:\n  - 'Figure: Side-by-side Pareto frontier comparison — Qwen3-235B (left) vs Llama\n    4 Scout (right). Same axis scales for direct visual comparison. Annotated with\n    architecture properties (depth, MoE routing). Shows that qualitative Pareto shape\n    replicates but quantitative steepness differs.'\n  analysis: 'Llama 4 Scout confirms the Pareto frontier generalizes across architectures.\n    The steeper negative rho (-0.54) vs Qwen3 (-0.51) is a moderate difference that\n    supports the architecture-dependence claim but is not dramatic enough to call\n    it a strong architectural contrast. This is the median-tier signature: same qualitative\n    finding, quantitatively less distinct than ideal. Both models agree on the key\n    implication: mid-depth layers are the right operating point for cross-lingual\n    transfer.\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: 'CaCLR probe training with L_BCE + α·L_SB-ECE + β·L_consistency (MMD).\n    α sweep (0.01–10.0), β sweep (0.001–1.0) across 3 OOM. Full comparison vs zero-shot,\n    mean-shift, linear projection, few-shot on both models × 20 langs.\n\n    '\n  expected_results:\n    alpha_optimal: 0.5\n    alpha_only_en_auroc_at_en_optimal_layer_qwen: 0.805\n    alpha_only_en_ece_at_en_optimal_layer_qwen: 0.058\n    alpha_only_zs_median_auroc_qwen: 0.695\n    alpha_only_zs_median_auroc_llama: 0.675\n    beta_0p001_delta_auroc_over_alpha_only_median: 0.002\n    beta_0p01_delta_auroc_over_alpha_only_median: 0.001\n    beta_0p1_delta_auroc_over_alpha_only_median: -0.001\n    beta_1p0_delta_auroc_over_alpha_only_median: -0.003\n    beta_sweep_max_delta_auroc: 0.003\n    beta_sweep_significant_at_p05: false\n    caclr_full_delta_auroc_over_zeroshot_median: 0.012\n    caclr_full_delta_auroc_over_zeroshot_range:\n    - -0.005\n    - 0.035\n    caclr_vs_linear_proj_delta_median: -0.023\n    caclr_vs_fewshot100_delta_median: -0.033\n    linear_proj_delta_auroc_over_zs_median_qwen: 0.035\n    linear_proj_delta_auroc_over_zs_median_llama: 0.032\n    fewshot_25_delta_auroc_over_zs_median: 0.024\n    fewshot_100_delta_auroc_over_zs_median: 0.043\n    mean_shift_delta_auroc_median: 0.0\n    method_ranking:\n    - few-shot-100\n    - linear-projection\n    - few-shot-25\n    - CaCLR-full\n    - CaCLR-α-only\n    - zero-shot\n    - mean-shift\n    caclr_beta_delta_high_resource: 0.004\n    caclr_beta_delta_mid_resource: 0.0\n    caclr_beta_delta_low_resource: -0.002\n    caclr_beta_vs_alpha_only_paired_perm_p: 0.42\n    caclr_beta_vs_alpha_only_cohens_d: 0.08\n    linear_proj_vs_zeroshot_paired_perm_p: 0.001\n    linear_proj_vs_zeroshot_cohens_d: 0.55\n  result_rationale: 'The β (consistency loss) is inert because MMD-based distributional\n    matching fundamentally cannot correct the geometric misalignment that CKA reveals.\n    MMD penalizes differences in mean embeddings and kernel-space distributional moments\n    — it can align marginal distributions but cannot learn the rotation of the correctness\n    direction across language subspaces. At low β (0.001), the MMD signal is too weak\n    to affect optimization. At medium β (0.01–0.1), the gradient signal exists but\n    points in the wrong direction — it pushes overall distributional alignment without\n    specifically aligning the correctness-relevant subspace. At high β (1.0), the\n    MMD term dominates and slightly hurts English AUROC by distorting the probe weights.\n    The α-only (SB-ECE) variant provides small but real calibration improvement (better\n    ECE) because smooth-binned ECE regularization is a well-motivated objective that\n    doesn''t require cross-lingual alignment. The total CaCLR improvement over zero-shot\n    (+1.2pp) comes entirely from the α term''s calibration regularization, not from\n    cross-lingual consistency. Cohen''s d = 0.08 for β effect is negligible. In contrast,\n    linear projection achieves +3.5pp because it directly estimates and corrects the\n    rotation via a learned affine transformation on parallel pairs. Few-shot-100 achieves\n    +4.3pp because it sidesteps alignment entirely by training on target-language\n    labels. This ranking — few-shot > linear-projection > CaCLR ≈ α-only > zero-shot\n    > mean-shift — is the key empirical result that the geometric explanation predicts.\n\n    '\n  tables:\n  - name: 'Table 5: β Sensitivity Sweep — ΔAUROC over α-only baseline'\n    description: 'β values (rows: 0, 0.001, 0.01, 0.1, 1.0) × summary statistics (columns:\n      median ΔAUROC, mean, std, min, max, # languages improved, paired permutation\n      p-value, Cohen''s d). Both models shown side-by-side. Key: no β value achieves\n      p < 0.05 or d > 0.2 — consistency loss is definitively inert.\n\n      '\n  - name: 'Table 6: Transfer Method Comparison — Median AUROC across 20 Languages'\n    description: 'Methods (rows: zero-shot, mean-shift, CaCLR-α-only, CaCLR-full,\n      linear-projection, few-shot-25, few-shot-100) × Models (columns: Qwen3, Llama\n      4) × 2 fixed layers + per-language oracle. ΔAUROC vs zero-shot with bootstrap\n      95% CI. Ranking is consistent across models. Linear projection and few-shot\n      clearly dominate.\n\n      '\n  - name: 'Table 7: CaCLR β Effect by Resource Tier'\n    description: 'Resource tier (rows: HIGH, MID, LOW) × β levels. Shows that inertness\n      is consistent across tiers — not a power issue with low-resource languages but\n      a fundamental limitation of distributional matching.\n\n      '\n  figures_description:\n  - 'Figure: α sensitivity curve — x-axis: log(α), y-axis: English ECE and AUROC at\n    EN-optimal layer. Shows that α ~0.5 optimizes ECE-AUROC tradeoff. SB-ECE regularization\n    provides genuine calibration benefit.'\n  - 'Figure: β sensitivity heatmap — x-axis: log(β), y-axis: languages sorted by resource\n    tier. Color: ΔAUROC over α-only. Shows near-zero change (white) across entire\n    grid. Highlights absence of any language × β sweet spot.'\n  - 'Figure: Transfer method ranking forest plot — each method as a row, showing median\n    ΔAUROC with bootstrap 95% CI. Clear separation between geometric methods (linear-proj,\n    few-shot) and distributional methods (CaCLR-β, mean-shift).'\n  analysis: 'CaCLR''s β inertness is the paper''s centerpiece negative result. The\n    analysis proceeds in three steps: (1) empirically, β has negligible effect (d=0.08,\n    p=0.42) across 3 OOM and both architectures; (2) mechanistically, CKA analysis\n    (plan_011) reveals that cross-lingual misalignment at deeper layers is geometric\n    (rotation/scaling) rather than distributional (mean/covariance shift); (3) linear\n    projection''s success (+3.5pp) confirms the geometric explanation — it succeeds\n    precisely because it learns the rotation that MMD cannot represent. This three-part\n    argument closes the distributional-matching path with both theory and evidence.\n    The α-only variant retains value as a calibration regularizer — it improves ECE\n    without hurting AUROC.\n\n    '\n- name: Difficulty-Controlled Decomposition Ablation\n  plan_id: plan_004\n  description: 'IRT difficulty probes, project out difficulty direction, retrain correctness\n    probes on residuals. 10 languages × 8 layers per model. Random-direction control.\n\n    '\n  expected_results:\n    difficulty_probe_r2_en_median_across_layers: 0.42\n    difficulty_probe_r2_range:\n    - 0.25\n    - 0.55\n    decomposition_transfer_delta_median: 0.012\n    decomposition_transfer_delta_range:\n    - -0.01\n    - 0.035\n    pct_combos_improved: 0.65\n    pct_combos_improved_by_tier_high: 0.72\n    pct_combos_improved_by_tier_mid: 0.65\n    pct_combos_improved_by_tier_low: 0.53\n    improvement_stronger_at_deep_layers: true\n    improvement_at_shallow_layers_pct: 0.5\n    improvement_at_deep_layers_pct: 0.78\n    random_direction_delta_median: 0.003\n    random_direction_delta_significant: false\n    difficulty_correctness_cosine_median: 0.18\n    difficulty_correctness_cosine_range:\n    - 0.08\n    - 0.3\n    decomposition_vs_baseline_paired_p: 0.03\n    decomposition_cohens_d: 0.28\n  result_rationale: 'Decomposition works but is partial because the difficulty-capability\n    separation is not clean. The difficulty direction (IRT-derived) captures ~42%\n    variance in human difficulty scores (R²) — reasonable but not perfect, meaning\n    the projection leaves residual difficulty signal mixed with capability. At deep\n    layers, removing difficulty helps more often (78% of combos) because the capability-specific\n    component dominates transfer degradation there — once you remove the shared difficulty\n    signal, the residual is more language-specific and harder to transfer. At shallow\n    layers, the improvement rate drops to ~50% (near chance) because both difficulty\n    and capability signals are more entangled and less linearly separable. The 65%\n    overall improvement rate is genuine but not universal — it demonstrates the decomposition\n    is prescriptive for about two-thirds of settings. The random-direction control\n    (median +0.3pp, not significant) confirms this isn''t a dimensionality-reduction\n    artifact. Low-resource languages show weaker improvement (53%) because their correctness\n    probes are noisier to begin with, and the difficulty projection may remove some\n    of the limited signal they have. The modest Cohen''s d (0.28) reflects that improvements\n    are real but small — this is a supporting analytical result, not a standalone\n    method contribution.\n\n    '\n  tables:\n  - name: 'Table 8: Decomposition Results — 10 Languages × 8 Layers'\n    description: 'Heatmap table: languages (rows) × layers (columns). Cells show ΔAUROC\n      after difficulty removal. Green: improved (>0.5pp), white: unchanged, red: degraded.\n      Marginal summaries: % improved per language, per layer. Shows concentration\n      of improvement at deep layers and high-resource languages.\n\n      '\n  - name: 'Table 9: Decomposition vs Random Direction Control'\n    description: 'Comparison: difficulty projection vs random projection vs no projection.\n      Median ΔAUROC, bootstrap CI, paired test. Confirms difficulty projection specifically\n      — not arbitrary dimensionality reduction — drives improvement.\n\n      '\n  figures_description:\n  - 'Figure: Decomposition improvement rate vs layer depth — bar chart showing fraction\n    of languages improved at each layer. Monotonically increasing trend from ~50%\n    at shallowest to ~78% at deepest. Supports narrative that capability-specific\n    component is the deep-layer transfer bottleneck.'\n  analysis: 'Decomposition provides supporting evidence for the geometric misalignment\n    narrative. The fact that difficulty removal helps more at deep layers aligns with\n    the CKA finding — at depth, the capability-specific component (which is geometrically\n    misaligned across languages) drives transfer failure, and removing the shared\n    difficulty component isolates this effect. However, the partial success rate (65%)\n    and modest effect size (d=0.28) keep this as supporting analysis rather than a\n    standalone claim. The finding is prescriptive: researchers attempting cross-lingual\n    probe transfer should first assess whether difficulty confounding explains their\n    transfer gaps — in ~65% of cases, it partially does.\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: 'Verbalized confidence direction extraction, cosine similarity with\n    correctness direction. 20 languages × 2 architectures. Resource-tier and family\n    analysis.\n\n    '\n  expected_results:\n    en_cosine_qwen: 0.035\n    en_cosine_llama: 0.038\n    cosine_median_across_langs_qwen: 0.055\n    cosine_median_across_langs_llama: 0.06\n    cosine_max_across_langs: 0.1\n    cosine_max_language: sw\n    cosine_range:\n    - 0.02\n    - 0.1\n    cosine_median_high_resource: 0.04\n    cosine_median_mid_resource: 0.06\n    cosine_median_low_resource: 0.085\n    cosine_variance_high: 0.0003\n    cosine_variance_mid: 0.0008\n    cosine_variance_low: 0.0018\n    all_langs_below_threshold: true\n    cosine_vs_resource_spearman_rho: 0.52\n    cosine_vs_resource_p: 0.018\n  result_rationale: 'Orthogonality persists across languages because the separation\n    between correctness and verbalized confidence is a structural property of how\n    transformers process MCQA — the model''s internal \"do I know this?\" signal (correctness)\n    and its verbalized \"how confident am I?\" output occupy orthogonal subspaces by\n    design (the former is a representation-level property, the latter is optimized\n    during RLHF/instruction-tuning for human-readable outputs). The English cosine\n    (~0.035- 0.038) replicates Miao & Ungar (2026). Non-English cosines are slightly\n    higher (median 0.055-0.060) because: (a) non-English confidence verbalization\n    is noisier (models are less calibrated in non-English expression of uncertainty);\n    (b) the confidence probe may capture some language-switching signal that correlates\n    weakly with correctness (lower-resource languages trigger more uncertain generation\n    behavior). The max cosine at 0.10 (sw) still satisfies the orthogonality threshold\n    (<0.12) but shows more variance — Swahili''s limited pretraining data means both\n    probes are noisier, and noise correlations inflate apparent cosine. The resource-\n    tier gradient (rho=0.52, p=0.018) is a novel finding: orthogonality is stronger\n    (lower cosine) for high-resource languages, suggesting that abundant pretraining\n    data helps separate correctness from confidence representations. However, even\n    the worst case (0.10) is far from the ~0.5+ that would indicate meaningful alignment,\n    confirming that output-based calibration is structurally limited across all languages.\n\n    '\n  tables:\n  - name: 'Table 10: Correctness–Confidence Cosine Similarity Across Languages'\n    description: '20 languages (rows, grouped by resource tier) × 2 architectures\n      (column pairs). Each cell: cosine similarity ± bootstrap 95% CI. Bottom: tier\n      medians and Spearman correlation with log(pretraining data estimate). All values\n      < 0.12.\n\n      '\n  figures_description:\n  - 'Figure: Cosine similarity vs estimated pretraining data — scatter plot, 20 languages\n    × 2 models. Log scale x-axis (pretraining tokens). Weak positive trend (more data\n    → lower cosine → stronger orthogonality). Highlights sw/bn as outliers with highest\n    cosine.'\n  analysis: 'Orthogonality holds universally (max 0.10 < 0.12 threshold) but with\n    a resource- tier gradient that is novel relative to Miao & Ungar''s English-only\n    finding. This extends their claim to multilingual settings with a nuance: the\n    structural separation is slightly weaker for low-resource languages, though never\n    approaching a level that would make output-based calibration viable. This supports\n    the paper''s broader argument that probe-based calibration is the right paradigm\n    for all languages, but the cross-lingual transfer challenge is the bottleneck\n    — not the underlying signal quality.\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Logistic regression vs 2-layer MLP at each probed layer for both models.\n    English accuracy, cross-lingual transfer degradation, calibration quality.\n\n    '\n  expected_results:\n    logreg_en_best_auroc_qwen: 0.81\n    mlp_en_best_auroc_qwen: 0.835\n    logreg_en_best_auroc_llama: 0.79\n    mlp_en_best_auroc_llama: 0.815\n    logreg_zs_median_qwen: 0.7\n    mlp_zs_median_qwen: 0.665\n    logreg_zs_median_llama: 0.68\n    mlp_zs_median_llama: 0.645\n    logreg_transfer_gap: 0.11\n    mlp_transfer_gap: 0.17\n    logreg_ece_median: 0.068\n    mlp_ece_median: 0.075\n    mlp_advantage_en_deep_layers: 0.03\n    mlp_advantage_en_shallow_layers: 0.01\n    logreg_better_transfer_pct_langs: 0.8\n  result_rationale: 'MLP probes achieve ~2.5pp higher English AUROC because they can\n    capture nonlinear interactions in the representation — the correctness signal\n    has a small nonlinear component that logistic regression misses. However, this\n    nonlinear component is language-specific (learned from English data, doesn''t\n    generalize), so MLP probes show 6pp larger transfer gap than logistic regression.\n    The MLP essentially overfits to English-specific nonlinearities in the correctness\n    representation. This confirms the hypothesis that linear probes transfer better\n    cross-lingually — the linear component of the correctness signal is more universal\n    across languages, while nonlinear components are language-specific. The MLP advantage\n    is concentrated at deep layers (+3pp at deep vs +1pp at shallow) because deeper\n    representations have more complex, language-specific structure for the MLP to\n    exploit. 80% of languages see better transfer with logistic regression, with the\n    exceptions being high- resource languages (zh, es) where the MLP''s nonlinear\n    component partially transfers due to shared pretraining features. This result\n    justifies the paper''s focus on logistic regression probes and reinforces the\n    geometric (linear) framing.\n\n    '\n  tables:\n  - name: 'Table S1: Probe Complexity — English AUROC and Transfer Gap by Layer'\n    description: 'Supplementary table. Layers (rows) × (LogReg EN, MLP EN, LogReg\n      ZS-median, MLP ZS-median, LogReg gap, MLP gap) for each model. Shows MLP''s\n      higher EN AUROC comes at cost of larger transfer gap. Gap difference increases\n      with depth.\n\n      '\n  figures_description:\n  - 'Figure: Transfer gap (EN AUROC - ZS median) vs layer depth for LogReg and MLP.\n    Two lines diverging at deeper layers — MLP gap grows faster, confirming linear\n    probes are preferable for cross-lingual transfer.'\n  analysis: 'This experiment justifies the methodological choice of logistic regression\n    probes and provides additional evidence for the geometric/linear framing. If the\n    correctness signal were deeply nonlinear, MLP''s advantage would transfer — the\n    fact that it doesn''t confirms that the transferable component is linear. Goes\n    in supplementary material as a methodological validation.\n\n    '\n- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: 'Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages\n    each). Validates generalization beyond GlobalMMLU.\n\n    '\n  expected_results:\n    belebele_en_best_auroc_qwen: 0.78\n    belebele_zs_median_qwen: 0.68\n    belebele_pareto_rho_median: -0.48\n    belebele_linear_proj_delta: 0.03\n    belebele_caclr_beta_delta: 0.003\n    mmlupx_en_best_auroc_qwen: 0.82\n    mmlupx_zs_median_qwen: 0.69\n    mmlupx_pareto_rho_median: -0.5\n    mmlupx_linear_proj_delta: 0.033\n    mmlupx_caclr_beta_delta: 0.002\n    auroc_rank_correlation_globalmmlu_vs_belebele: 0.82\n    auroc_rank_correlation_globalmmlu_vs_mmlupx: 0.88\n    method_ranking_consistent_across_benchmarks: true\n  result_rationale: 'Belebele is a reading comprehension benchmark — fundamentally\n    different from MCQA knowledge testing. The correctness signal is still present\n    (models either comprehend or don''t) but Belebele''s English AUROC is slightly\n    lower (0.78 vs 0.81) because reading comprehension correctness is less cleanly\n    encoded than factual knowledge correctness. The Pareto rho is slightly weaker\n    (-0.48) because Belebele''s parallel passages provide more uniform cross-lingual\n    signal than GlobalMMLU''s diverse topics. MMLU-ProX, being closer to GlobalMMLU\n    in format, shows more similar results (0.82 EN AUROC, -0.50 rho). The key finding\n    is that method rankings are consistent — linear projection still outperforms CaCLR,\n    and CaCLR''s β term remains inert across benchmarks. This rules out the possibility\n    that CaCLR''s failure is GlobalMMLU-specific. The high rank correlations (0.82–0.88)\n    between benchmarks confirm that per-language transfer difficulty is a property\n    of the model''s multilingual representations, not the benchmark.\n\n    '\n  tables:\n  - name: 'Table S2: Cross-Benchmark Generalization'\n    description: 'Supplementary. Benchmarks (rows: GlobalMMLU, Belebele, MMLU-ProX)\n      × key metrics (EN AUROC, ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ). Shows\n      consistent patterns across benchmarks. Rank correlation between per-language\n      AUROCs.\n\n      '\n  figures_description:\n  - 'Figure: Per-language AUROC scatter — GlobalMMLU vs Belebele, GlobalMMLU vs MMLU-ProX.\n    Each point is a language. High correlation confirms benchmark-invariant transfer\n    difficulty ranking.'\n  analysis: 'Benchmark generalization confirms all findings are not artifacts of GlobalMMLU.\n    The consistent method ranking across three benchmarks strengthens the negative\n    result — CaCLR''s β inertness is a fundamental property of distributional matching\n    vs geometric misalignment, not a benchmark-specific failure. Goes in supplementary\n    or a short main-text paragraph.\n\n    '\n- name: INT8 Validation Ablation\n  plan_id: plan_010\n  description: 'INT8 vs FP16 comparison at 5 representative layers for Llama 4 Scout\n    on 5% subset.\n\n    '\n  expected_results:\n    int8_fp16_auroc_max_diff: 0.008\n    int8_fp16_auroc_mean_diff: 0.003\n    int8_fp16_ece_max_diff: 0.012\n    int8_fp16_correlation_r: 0.997\n    int8_fp16_rank_agreement_pct: 0.98\n    distortion_significant: false\n  result_rationale: 'INT8 weight-only quantization preserves the vast majority of\n    activation-space structure because (a) it quantizes weights, not activations —\n    the internal representations used for probing are computed in higher precision;\n    (b) 7B+ models are robust to INT8 quantization (well-established in the quantization\n    literature); (c) correctness probes operate on high-dimensional representations\n    (4096+ dims) where small per-dimension perturbations from quantization average\n    out. The max AUROC difference of 0.8pp across any layer is within bootstrap confidence\n    intervals. The 0.997 correlation between INT8 and FP16 probe scores confirms that\n    quantization shifts all scores by a near-constant offset without affecting ranking.\n    This validation is necessary for reviewer reassurance but expected to be a non-issue.\n\n    '\n  tables:\n  - name: 'Table S3: INT8 vs FP16 Validation'\n    description: 'Supplementary. 5 layers × metrics (INT8 AUROC, FP16 AUROC, Δ, rank\n      correlation). All differences within bootstrap CI. Conclusion: INT8 does not\n      distort correctness signals.\n\n      '\n  figures_description: []\n  analysis: 'Straightforward validation that INT8 quantization doesn''t affect conclusions.\n    One paragraph in supplementary material with the table. Addresses anticipated\n    reviewer concern #5.\n\n    '\n- name: CKA Cross-Lingual Representation Similarity\n  plan_id: plan_011\n  description: 'CKA (linear kernel) between English and each target language at every\n    probed layer, both models. Correlate CKA with transfer AUROC.\n\n    '\n  expected_results:\n    cka_en_zh_shallow_layer12_qwen: 0.88\n    cka_en_zh_deep_layer72_qwen: 0.62\n    cka_en_sw_shallow_layer12_qwen: 0.78\n    cka_en_sw_deep_layer72_qwen: 0.38\n    cka_median_shallow_across_langs: 0.84\n    cka_median_deep_across_langs: 0.52\n    cka_decrease_with_depth_significant: true\n    cka_transfer_pearson_r_qwen: 0.62\n    cka_transfer_pearson_r_llama: 0.54\n    cka_transfer_pearson_r_pooled: 0.58\n    cka_transfer_pearson_p: 1.0e-05\n    cka_deep_high_resource_median: 0.6\n    cka_deep_mid_resource_median: 0.48\n    cka_deep_low_resource_median: 0.36\n    mmd_transfer_pearson_r: 0.25\n    mmd_explains_variance_pct: 6\n    cka_explains_variance_pct: 34\n  result_rationale: 'CKA measures representational similarity including geometric\n    structure (rotation, scaling), while MMD measures distributional distance (mean,\n    variance, higher moments). CKA decreases with depth because deeper transformer\n    layers specialize more for language-specific processing — the cross-lingual alignment\n    enforced by shared vocabulary embeddings and early layers gradually gives way\n    to language- specific feature extraction. The CKA–transfer correlation (r=0.58)\n    is moderate- to-strong: it explains 34% of variance in transfer AUROC, confirming\n    that representational geometry is a major (but not the only) factor in transfer\n    success. The remaining variance comes from factors like probe quality, dataset\n    difficulty distribution, and non-geometric aspects of the representation. Critically,\n    CKA (r=0.58) substantially outpredicts MMD (r=0.25) as a predictor of transfer\n    success — this is the key mechanistic finding. If cross-lingual misalignment were\n    distributional (mean/covariance shift), MMD would predict transfer as well as\n    or better than CKA. The fact that CKA is 2.3× more predictive demonstrates that\n    the misalignment is geometric (rotation/scaling of the entire representational\n    space), not merely distributional. This directly explains why MMD-based CaCLR\n    fails: it optimizes the wrong measure of alignment. The resource-tier CKA gradient\n    (0.60 > 0.48 > 0.36 at deep layers) mirrors the transfer AUROC gradient, providing\n    a mechanistic explanation for why low-resource languages transfer worse — their\n    deep-layer representations are more geometrically dissimilar from English.\n\n    '\n  tables:\n  - name: 'Table 11: CKA Similarity — Languages × Layers'\n    description: 'Probed layers (rows) × 20 languages (columns, sorted by resource\n      tier). Cells: CKA values. Clear gradient: high CKA at shallow layers, decreasing\n      with depth. Resource-tier banding visible. Both models shown.\n\n      '\n  - name: 'Table 12: CKA vs MMD as Transfer Predictors'\n    description: 'Predictor comparison: CKA linear, CKA RBF, MMD, H-divergence proxy.\n      Columns: Pearson r, R², p-value. CKA linear clearly dominant. Demonstrates geometric\n      > distributional as explanation.\n\n      '\n  figures_description:\n  - 'Figure: CKA heatmap — layers (y-axis) × languages (x-axis, sorted by transfer\n    AUROC). Color intensity = CKA. Clear diagonal structure: high CKA co-occurs with\n    high transfer AUROC. Visual demonstration of the CKA–transfer link.'\n  - 'Figure: CKA vs transfer AUROC scatter — each point is a (layer, language) pair.\n    Color: resource tier. Linear fit line with r=0.58. Contrasted with MMD vs transfer\n    scatter (r=0.25) in adjacent panel. The visual gap between the two correlations\n    is the paper''s mechanistic argument.'\n  - 'Figure: CKA depth profile — CKA vs layer depth for 3 representative languages\n    (zh, tr, sw). Three curves showing parallel decline but at different levels. Annotated\n    with corresponding transfer AUROC at each layer.'\n  analysis: 'CKA analysis is the mechanistic backbone of the paper. It upgrades the\n    contribution from \"we measured that transfer fails at deep layers\" to \"we explain\n    WHY transfer fails — geometric misalignment increases with depth, and this misalignment\n    type (rotation/scaling) is specifically not addressable by distributional matching\n    (MMD).\" The CKA–transfer correlation (r=0.58) provides quantitative support, and\n    the CKA vs MMD comparison (34% vs 6% variance explained) provides the critical\n    distinction that makes the negative CaCLR result theoretically interpretable rather\n    than just empirically observed. This transforms the paper from a measurement study\n    to one with mechanistic insight.\n\n    '\n- name: Linear Projection Sensitivity Analysis\n  plan_id: plan_012\n  description: 'Vary parallel pairs (10, 20, 50, 100, 200) for linear projection.\n    Both models × 5 layers × 20 languages.\n\n    '\n  expected_results:\n    pairs_10_delta_auroc_median: 0.012\n    pairs_20_delta_auroc_median: 0.022\n    pairs_50_delta_auroc_median: 0.03\n    pairs_100_delta_auroc_median: 0.035\n    pairs_200_delta_auroc_median: 0.036\n    saturation_knee_point: 70\n    pairs_for_90pct_max_improvement: 55\n    pairs_for_95pct_max_improvement: 85\n    pairs_10_std_across_langs: 0.025\n    pairs_50_std_across_langs: 0.012\n    pairs_100_std_across_langs: 0.008\n    saturation_consistent_across_models: true\n    qwen_saturation_knee: 65\n    llama_saturation_knee: 75\n  result_rationale: 'Linear projection learns a rotation matrix mapping source-language\n    representations to target-language space. The sample complexity for estimating\n    a linear mapping in high-dimensional space (4096+ dims) is surprisingly low because:\n    (a) the effective dimensionality of the correctness-relevant subspace is much\n    lower than the full representation dimensionality — the probe operates in a low-rank\n    subspace; (b) parallel pairs provide direct supervision on the mapping, unlike\n    distributional matching which uses indirect statistical signals. With 10 pairs,\n    the mapping is underdetermined but captures the dominant rotation component (+1.2pp).\n    By 50 pairs, 90% of the achievable improvement is captured as the major rotation/scaling\n    axes are identified. The knee point at ~70 pairs and saturation by 100 pairs is\n    consistent with the cross-lingual alignment literature (MUSE, VecMap) where bilingual\n    dictionaries of 50–100 entries suffice for word-level alignment. The slight architecture\n    difference in knee points (65 vs 75) reflects that Llama 4''s representations\n    may require slightly more pairs to estimate the rotation due to its MoE routing\n    introducing more heterogeneity. The practical implication is clear: ~50-100 parallel\n    pairs (trivially obtainable from GlobalMMLU train split) are sufficient to match\n    or exceed CaCLR''s entire training pipeline.\n\n    '\n  tables:\n  - name: 'Table 13: Linear Projection — Sample Efficiency'\n    description: 'Pair counts (rows: 10, 20, 50, 100, 200) × summary statistics (median\n      ΔAUROC, mean, std, min, max, % languages improved). Both models. Shows clear\n      diminishing returns after 50 pairs.\n\n      '\n  figures_description:\n  - 'Figure: Learning curve — x-axis: number of parallel pairs (log scale), y-axis:\n    median ΔAUROC. Two curves (Qwen3, Llama4) with shaded ±1 std band. Annotated knee\n    point. Horizontal dashed line: CaCLR-full ΔAUROC for comparison — linear projection\n    surpasses CaCLR at just ~20 pairs.'\n  analysis: 'Linear projection''s sample efficiency is the constructive complement\n    to CaCLR''s negative result. The message: you don''t need MMD-based distributional\n    matching (which doesn''t work anyway) — you just need ~50-100 parallel pairs and\n    a linear mapping. This is practically actionable and theoretically consistent\n    with the geometric explanation (linear projection learns the rotation that MMD\n    cannot). The learning curve figure — showing linear projection surpassing CaCLR\n    at ~20 pairs — is one of the paper''s most compelling visuals.\n\n    '\n- name: Probing Control Tasks (Hewitt & Liang 2019)\n  plan_id: plan_013\n  description: 'Train probes on randomly permuted labels at each layer. Selectivity\n    analysis across layers and languages.\n\n    '\n  expected_results:\n    control_auroc_en_median: 0.545\n    control_auroc_en_range:\n    - 0.52\n    - 0.58\n    control_auroc_noneng_median: 0.54\n    selectivity_en_median: 0.265\n    selectivity_en_range:\n    - 0.18\n    - 0.31\n    selectivity_noneng_median_high_resource: 0.2\n    selectivity_noneng_median_mid_resource: 0.16\n    selectivity_noneng_median_low_resource: 0.1\n    selectivity_min_across_all: 0.08\n    selectivity_min_language: sw\n    selectivity_min_layer: layer_4\n    all_selectivities_positive: true\n    pct_above_10pp: 0.88\n    pct_above_10pp_high_resource: 0.95\n    pct_above_10pp_low_resource: 0.7\n    selectivity_peaks_at_mid_depth: true\n    selectivity_peak_layer_pct_depth: 0.55\n  result_rationale: 'Control tasks with random labels test whether probe capacity\n    (model expressiveness) alone can achieve high AUROC without genuine correctness\n    signal. The control AUROC of ~0.54-0.55 (barely above chance at 0.50) confirms\n    that logistic regression probes do not have sufficient capacity to memorize random\n    label assignments in high-dimensional space — any AUROC above this baseline reflects\n    genuine signal. English selectivity (median 0.265) is strong: the probe captures\n    real correctness information 26.5pp above what capacity alone could achieve. Non-English\n    selectivity decreases with resource tier because: (a) the correctness signal itself\n    is weaker for languages with less pretraining data; (b) the cross-lingual transfer\n    means probes must generalize from English-learned patterns, which is inherently\n    harder for distant languages. Low-resource languages (sw, bn) show selectivity\n    ~10pp, still positive but approaching the threshold where a reviewer might question\n    signal quality. The 88% of language-layer combinations exceeding 10pp provides\n    reasonable validation, but the 30% failure rate for low-resource languages at\n    this threshold is a genuine limitation that the paper should acknowledge. Selectivity\n    peaks at mid-depth (~55%) because shallow layers have weaker correctness signals\n    (less processed) and very deep layers have stronger but more language-specific\n    signals (high probe AUROC but also higher control AUROC due to richer features).\n\n    '\n  tables:\n  - name: 'Table S4: Control Task Selectivity'\n    description: 'Supplementary. Languages (rows, grouped by resource tier) × representative\n      layers (columns). Cells: selectivity (probe AUROC - control AUROC). Color-coded:\n      green >15pp, yellow 10-15pp, orange 5-10pp. Shows resource- tier gradient in\n      selectivity.\n\n      '\n  figures_description:\n  - 'Figure: Selectivity by resource tier — box plots for HIGH, MID, LOW resource\n    tiers. Shows decreasing median and increasing variance for lower-resource tiers.\n    Dashed line at 10pp threshold. Most points above threshold but LOW tier shows\n    some below.'\n  analysis: 'Control tasks validate that probe AUROC reflects genuine correctness\n    signal for the large majority of settings (88% above 10pp). The resource-tier\n    gradient in selectivity is a limitation to acknowledge: for low-resource languages,\n    probe signal quality is weaker, and conclusions about transfer should be interpreted\n    with this caveat. This doesn''t undermine the paper''s core claims (which are\n    about the mechanism of transfer failure, not about achieving high probe quality\n    in every language) but sets appropriate epistemic bounds.\n\n    '\n- name: Gemma 4 31B Dense Pareto Frontier\n  plan_id: plan_008\n  description: 'Third architecture for camera-ready. 60 layers, dense, FP16. Full\n    Pareto frontier, 20+ languages. Dense vs MoE contrast.\n\n    '\n  expected_results:\n    en_best_auroc: 0.8\n    en_best_layer: 45\n    zs_transfer_auroc_median: 0.69\n    best_transfer_layer: 33\n    pareto_rho_per_lang_median: -0.58\n    zs_langs_above_0p65: 12\n    pareto_rho_smoother_than_moe: true\n    pareto_rho_std_across_langs_gemma: 0.12\n    pareto_rho_std_across_langs_qwen: 0.16\n    pareto_rho_std_across_langs_llama: 0.15\n    cka_depth_decline_steeper_dense: true\n    linear_proj_delta_median: 0.033\n  result_rationale: 'Gemma 4 31B Dense provides the critical dense-vs-MoE architectural\n    contrast. As a dense model, every token passes through every layer (no routing),\n    creating more uniform layer-to-layer transformations. This produces a smoother\n    Pareto frontier (lower rho variance across languages: 0.12 vs 0.15-0.16 for MoE\n    models) because the depth-transfer tradeoff is more consistent without routing-induced\n    heterogeneity. The rho itself is slightly stronger negative (-0.58) because dense\n    models show a cleaner monotonic decline in cross-lingual alignment with depth\n    — MoE routing partially breaks this monotonicity by allowing some expert pathways\n    to maintain cross-lingual features at deeper layers. CKA declines more steeply\n    with depth in the dense model, confirming that MoE routing provides a modest buffer\n    against geometric misalignment (different experts can specialize differently per\n    language). English AUROC (0.80) is comparable to the larger MoE models despite\n    smaller parameter count because the 31B dense architecture is parameter-efficient\n    for representation quality. This is a P2 camera-ready experiment that strengthens\n    the architecture-dependence claim from \"two MoE models differ moderately\" to \"dense\n    vs MoE is a qualitatively distinct contrast.\"\n\n    '\n  tables:\n  - name: 'Table CR1: Three-Architecture Pareto Comparison'\n    description: 'Camera-ready. Architecture (rows: Qwen3-MoE, Llama4-MoE, Gemma4-Dense)\n      × key metrics (EN AUROC, ZS median, rho median, rho std, CKA slope, linear-proj\n      Δ). Highlights dense vs MoE contrast in rho variance and CKA slope.\n\n      '\n  figures_description:\n  - 'Figure: Three-panel Pareto frontier comparison — Qwen3-MoE, Llama4-MoE, Gemma4-Dense\n    side-by-side. Dense model shows smoother, more monotonic frontier. Visual argument\n    for architecture-dependence.'\n  analysis: 'Camera-ready addition. The dense-vs-MoE contrast is the strongest architecture-\n    dependence evidence: MoE routing introduces heterogeneity that partially buffers\n    against geometric misalignment at deep layers, while dense models show cleaner\n    depth-dependent degradation. This doesn''t change the paper''s conclusions but\n    provides a more compelling architectural contrast than two MoE models alone.\n\n    '\n- name: Extended Language Coverage (50+ Languages)\n  plan_id: plan_009\n  description: 'Expand from 20 to 50+ languages for camera-ready. Full GlobalMMLU/Belebele\n    language sets.\n\n    '\n  expected_results:\n    total_languages: 52\n    zs_langs_above_0p65: 28\n    zs_median_auroc_52lang: 0.66\n    zs_auroc_range:\n    - 0.5\n    - 0.74\n    new_low_resource_langs_below_0p55:\n    - am\n    - my\n    - zu\n    - sn\n    - rw\n    resource_tier_gradient_replicates: true\n    pareto_rho_median_52lang: -0.49\n    linear_proj_delta_median_52lang: 0.031\n    tail_langs_below_0p55_count: 8\n    tail_langs_above_0p70_count: 12\n  result_rationale: 'Expanding to 52 languages adds many more low-resource and typologically\n    diverse languages. The median AUROC drops slightly (0.66 vs 0.70 for the curated\n    20) because the additional languages are disproportionately low-resource. Five\n    extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda)\n    fall below 0.55, approaching chance performance — these languages have minimal\n    pretraining representation in both models. The resource-tier gradient continues\n    to hold and becomes even more pronounced with the extended tail. Pareto rho weakens\n    slightly (-0.49) because many of the new languages show weak, noisy correlations\n    due to low base probe quality. Linear projection improvement remains consistent\n    (+3.1pp), confirming the geometric correction generalizes beyond the curated language\n    set. The practical message: probe-based cross-lingual calibration is viable for\n    ~28/52 languages (54%) without any target-language data, and linear projection\n    extends this to ~35/52 (67%). The remaining ~17 languages need language-specific\n    probes or alternative approaches.\n\n    '\n  tables:\n  - name: 'Table CR2: Extended Language Coverage — 52 Languages'\n    description: 'Camera-ready. Full 52-language results sorted by zero-shot AUROC.\n      Columns: language, family, resource tier, ZS AUROC, linear-proj AUROC, few-shot-100\n      AUROC. Grouped into tiers: >0.70 (strong transfer), 0.65-0.70 (viable), 0.55-0.65\n      (marginal), <0.55 (failed).\n\n      '\n  figures_description:\n  - 'Figure: Language coverage map — world map with countries colored by best zero-shot\n    transfer AUROC. Visual demonstration of where probe-based calibration works and\n    fails geographically.'\n  analysis: 'Camera-ready extension. The 52-language analysis adds scale but the median-tier\n    conclusion is clear: probe-based cross-lingual calibration works for a majority\n    but not all languages, and the resource-tier gradient is the dominant predictor\n    of success. This sets realistic expectations for practitioners and motivates future\n    work on low-resource language probe training.'\n",
      "numLines": 962,
      "startLine": 1,
      "totalLines": 962
    }
  },
  "sourceToolAssistantUUID": "816fb248-1c6f-4e58-ab63-d8204e4adfbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24 · 2026-05-21T03:46:59.091Z_

````json
{
  "parentUuid": "e4975bea-3167-497f-aebb-ace1c3c1f5f0",
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
  "uuid": "9c242a2b-f023-48d5-b5a3-1615f15a9c35",
  "timestamp": "2026-05-21T03:46:59.091Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：CaCLR consistency loss inert（β sweep 无效），但 Pareto discovery 稳固且 linear projection 是 practical solution；CKA 降级为 suggestive；paper 以 discovery + principled…",
  "leafUuid": "9c242a2b-f023-48d5-b5a3-1615f15a9c35",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer: Pareto frontiers, negative CaCLR result, linear projection baseline",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Assistant

_source line 27 · 2026-05-21T03:49:23.126Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the existing median imagined experiments from the previous dream report. I see it's quite detailed already. Let me check the differences between what was asked and what already exists.

The user is asking me to re-generate the imagined experiments for the median tier based on the current Phase 1 definitions. Looking at the existing median imagined experiments, they seem fairly good but there are some issues:

1. The previous version had Qwen and Llama with very similar strong negative rhos (-0.58 and -0.62), but the median tier specifies:
   - pareto_spearman_rho_strong_arch: [-0.6, -0.4] 
   - pareto_spearman_rho_weak_arch: [-0.25, -0.05] - this is a critical distinction I missed, meaning one architecture should show weak language-specific Pareto effects while the other shows strong ones

2. The previous version didn't include the partial correlation analysis for CKA controlling for depth, which is essential for the median tier - this should show weak correlations in the 0.1-0.25 range with p-values between 0.05-0.2

3. I need to verify the selectivity_below_005_fraction aligns with the [0.2, 0.3] range specified for the median tier, particularly checking the control task predictions

4. The previous version's CKA framing needs adjustment to properly reflect the partial correlation requirements rather than positioning it as mechanistic evidence

Now I'm seeing the key architectural contrast more clearly: Qwen should show strong Pareto effects around -0.50 while Llama Scout shows weak effects around -0.15, and the MVP data supports this with Qwen's language-specific selectivity patterns appearing across non-deepest layers versus Llama's concentration in the deepest layers for most languages. I need to regenerate with these corrections to properly align with the median tier definitions.

For the statistical measures, the partial correlation controlling for depth comes in marginal at around 0.18 with p-value near 0.12, which downgrades the framing to suggestive rather than mechanistic. The CaCLR results show inert beta coefficients across three orders of magnitude with minimal AUROC changes, and I'm clarifying whether the selectivity metric refers to values below 0.05 or 0.005—the MVP data suggests it's the former, with roughly 25-30% of language-layer combinations falling below that threshold.

The linear projection pairs show modest gains around 0.035, orthogonality vectors cluster between 0.02 and 0.12 in cosine similarity, and difficulty transfer effects range from 0.005 to 0.025. Now I need to structure the YAML carefully, distinguishing between Qwen's strong Pareto frontier and Llama's weaker, language-specific patterns, then map this against the 20-language experimental set.

For resource allocation across the full language set, I'm grouping into tiers: HIGH tier gets the well-resourced languages like Chinese, Spanish, French, German, Japanese, Portuguese, Russian, and Dutch; MID tier covers Arabic, Hindi, Korean, Vietnamese, Turkish, Indonesian, Polish, and Ukrainian; LOW tier includes Swahili, Bengali, and Telugu, though I should reconsider whether some MID languages might shift based on actual representation in the training data.

Looking at the performance targets, I'm aiming for a zero-shot transfer success rate between 70-85%, which should get 14-17 languages above the 0.60 threshold, with an average AUROC across all 20 languages around 0.62-0.68. For a strong model like Qwen3-235B, I'm seeing English reaching about 0.80 AUROC with a clear Pareto frontier where the global correlation is around -0.50, and per-language correlations vary by tier—HIGH languages show -0.55 to -0.40, MID around -0.45 to -0.30, and LOW languages clustering around -0.60 to -0.45.

In contrast, Llama 4 Scout as a weaker architecture shows English at 0.78 with a much flatter global correlation around -0.15, some languages even displaying positive correlations from the MVP pattern, and overall zero-shot performance dropping to 0.63 average with only about 14 out of 20 languages succeeding. This architectural difference is crucial for establishing the core claim about how model capacity affects the transfer-performance tradeoff.

Now I'm working through the specific predictions for each plan, starting with Qwen3-235B-A22B.

For this model with 94 layers sampled every 4th, I'm mapping out the English AUROC progression across the layer stack—starting from 0.54 at layer 0 and climbing steadily through the middle layers, reaching around 0.80 by layer 64 and plateauing there.

Looking at zero-shot transfer performance at the optimal English layer (L72), I'm seeing the model generalizes reasonably well across 20 languages with an average of 0.66, though performance varies significantly—Chinese and Spanish near 0.71 while Swahili and Bengali drop to 0.55-0.56. The best transfer layer appears to be somewhere different from the English-optimal one.

I'm noticing that shallower layers like L48-L52 might actually be better for cross-lingual transfer since representations are more language-agnostic there, with average performance around 0.68 at L52. Looking at the correlation between layer depth and zero-shot performance per language, there's a consistent negative trend—deeper layers hurt transfer performance, with Spearman correlations ranging from -0.40 to -0.60 depending on the language, and a global median of -0.50.

For the Llama 4 Scout experiment, I'm planning to sample every 4th layer across the 48-layer model to keep the evaluation tractable.

Now examining the English AUROC profile across these sampled layers—performance steadily climbs from 0.55 at L0 to a peak of 0.78 at L40, then slightly drops to 0.77 at L44. But the interesting pattern emerges when I look at zero-shot transfer across languages: Arabic and Korean both peak at L40 (0.65 and 0.66 respectively), while Chinese peaks earlier at L28 (0.69) and actually declines at L40 (0.67). This suggests that unlike the English in-distribution performance, cross-lingual transfer doesn't necessarily follow the same deep-layer advantage—some languages benefit from mid-to-deep layers while others plateau or regress earlier.

Looking at the Spearman correlations between layer depth and performance, the picture becomes clearer: Arabic and Korean show positive correlations (+0.15 and +0.10), meaning they genuinely improve with depth, while Swahili has a strong negative correlation (-0.45), indicating sharp performance drops at deeper layers. Chinese, Spanish, French, and German all show mild negative correlations (ranging from -0.20 to -0.30), suggesting a gentle decline with depth. The global correlation hovers near zero at -0.12 because these language-specific patterns—some improving, others declining—essentially cancel each other out when averaged together. Now I'm drafting the full YAML configuration, and I need to reconsider the CaCLR predictions more carefully for the median tier. The AUROC improvement is essentially negligible—the delta sits right at the noise floor—because the consistency regularization term isn't doing much work. The ECE term might squeeze out a tiny improvement, but nothing substantial shows up in AUROC. Looking at the beta sweep, even small values like 0.001 only nudge the metric by a couple basis points.

When I compare the full CaCLR approach against zero-shot, I'm seeing about 0.8% AUROC gain, which is really just the alpha effect, while linear projection delivers 3.5% gain—a much more compelling result. This makes linear projection the practical winner here. Now I'm turning my attention to plan_011 and how CKA factors into the analysis.

Looking at the median tier results, the partial correlation controlling for depth shows CKA has marginal explanatory power beyond normalized depth alone—around r=0.18, p≈0.10, which doesn't quite hit conventional significance. But the between-language signal should be stronger: at a given depth, languages with higher CKA should show better transfer performance, and that cross-language correlation within layers looks significant at r≈0.55, p<0.01. So CKA does correlate with transfer, but the relationship is more nuanced than it first appears.

The key distinction is that CKA seems to explain between-language differences well, but it's not an independent predictor of how transfer degrades within a single language across depths—depth itself already captures most of that story. This "suggestive" framing means CKA is useful for understanding why some languages transfer better than others, rather than as a standalone depth-effect predictor.

Now moving to the control tasks with plan_013, I'm looking at the cross-lingual extension where English selectivity ranges from 0.02 to 0.262 across layers, and for the full 20-language experiment the median tier shows about 20-30% of layers fall below the 0.005 selectivity threshold.

With 480 total language-layer combinations across 20 languages and 24 layers, roughly 120 would fall below 0.05, but I need to reconsider the distribution—the English data shows the first four layers cluster tightly below 0.05 while deeper layers jump significantly higher, so the concentration pattern is more nuanced than my initial estimate.

For non-English languages, the selectivity calculation becomes trickier because cross-lingual transfer effects interact with the control baseline differently—while zero-shot AUROC drops for low-resource languages at shallow layers, the control task with random labels should stay relatively constant since random structure doesn't benefit from language-specific information. This means low-resource languages at shallow depths could have selectivity around 0.03 (with real AUROC near 0.52 and control near 0.49), while high-resource languages at mid-depth layers push closer to 0.68.

Estimating across all combinations for a 24-layer model like Qwen3, I'm working through which language-layer pairs fall below the 0.05 selectivity threshold—roughly 70% of shallow layer combinations across all languages contribute to low selectivity, plus some mid-depth cases for low-resource languages, which totals around 150 out of 480 possible combinations or about 31%, which feels high. Let me recalibrate by looking at the actual English selectivity profile from the MVP 7B model to ground this better. Now I'm breaking down the threshold violations across resource levels—English sits at 21% below threshold, high-resource non-English languages average around 21% as well, mid-resource languages climb to 29%, and low-resource languages hit 38% below threshold. Aggregating across all language groups gives me 128 out of 480 layers falling below the selectivity threshold, which works out to about 26.7%—right in the target range of 0.2 to 0.3.

So the key insight is that roughly a quarter of language-layer combinations show selectivity below 0.05, with this problem concentrated in shallow layers across all resource levels but extending into mid-depth layers specifically for low-resource languages. This becomes a methodological warning about the limitations of the approach.

Now I need to write out the full YAML configuration, making sure everything aligns properly with the median tier definitions. I'm also keeping in mind the narrative direction: CaCLR shifts from a methodological contribution to a principled negative result, where the β sweep across three orders of magnitude plus component ablation demonstrates that MMD is ineffective for the correctness subspace, and CKA geometric analysis explains why—MMD matches marginals but fails to capture the low-dimensional directional structure. The claims need adjustment too: Claim 1 stays as is, but Claim 2 becomes qualitative rather than quantitative.

The tricky part with Llama 4 Scout as the weak architecture is showing language-specific Pareto fronts rather than just a weaker version of the same negative correlation. Some languages actually show positive correlation where deeper layers improve transfer, while others show negative correlation, which is why the global Spearman rho ends up near zero. I need to be precise about that metric range for the weak architecture.

Writing YAML configuration... Now I'm locking in the specific metric values for each architecture—Qwen gets the stronger performance on the probe task and transfer success, while Llama shows the weaker correlations and smaller calibration improvements, with the CKA delta metrics completing the picture.

Writing YAML config... I need to be more systematic here—the user asked for detailed data on every planned experiment from the experiment_plan, so let me go through and identify all of them clearly, distinguishing between the planned experiments in the plan itself versus what's already marked as done in the registry.

For each of the 13 planned experiments, I'll need to generate comprehensive predictions including the experiment name, plan ID, description, expected results with specific metrics, detailed rationale, table schemas, figure descriptions, and analysis approach. This will be quite extensive, but the user specifically requested detailed data.

I should also pay attention to the specifics of each experiment—like how plan_010 uses different quantization methods for different models (W4A16 vs GPTQ-Int4), and make sure my predictions reflect those technical distinctions rather than treating them generically.

For plan_007, I need to remember that it depends on plan_003 being completed first, so the predictions should show how the CaCLR patterns generalize to the new evaluation datasets.

Now I'll structure this as a YAML block with the exact format requested and write out all 13 experiments with thorough but concise predictions.

I'm also noticing the previous version had some critical errors in the median tier definitions—both architectures showing strong negative correlations when they should show one strong and one weak pattern. I'll make sure my version corrects those issues and keeps all metrics within the proper ranges for the median tier.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c242a2b-f023-48d5-b5a3-1615f15a9c35",
  "isSidechain": false,
  "requestId": "req_011CbF2cH1oF5iNeSGS9EYv6",
  "type": "assistant",
  "uuid": "c36dfab5-0ff7-40c9-acb9-6fe2ab3a9e27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gDkAUqWsCMMAZuVPmyvNU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31059,
      "cache_read_input_tokens": 35950,
      "output_tokens": 27715,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31059,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 27715,
          "cache_read_input_tokens": 35950,
          "cache_creation_input_tokens": 31059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31059
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

_source line 28 · 2026-05-21T03:55:51.118Z_

已有的 median 版 imagined_experiments 存在关键问题：两个架构都给了强负 rho（Qwen -0.58, Llama -0.62），但 median 档明确要求 weak arch rho 在 [-0.25, -0.05]；CKA partial correlation 分析缺失；部分指标超出指定范围。现在基于 Phase 1 median 定义重新生成。

```yaml
tier: median
narrative_guidance: >
  Discovery + principled negative result + practical recommendation 三段叙事。
  (1) Pareto frontier 在 Qwen3-235B 上清晰（rho ~ -0.50），在 Llama 4 Scout 上
  language-specific（global rho ~ -0.12）：部分语言随 depth 改善（ar/ko/hi），
  部分退化（zh/sw），验证 architecture-dependent tradeoff shape。
  (2) CaCLR β sweep 3 OOM 证明 MMD consistency loss inert（d=0.07, p=0.38）。
  CKA 几何分析提供 suggestive 解释——MMD matches marginals but not low-dim
  directional structure——但 partial correlation controlling depth 仅 r=0.18,
  p=0.11，降级为 suggestive correlational analysis。Between-language correlation
  成立（same-layer r=0.52, p<0.01）。
  (3) Linear projection ~50 pairs 是实际方案（+3.5pp over zero-shot），surpasses
  CaCLR at ~20 pairs。
  Decomposition 定性成立（65% combos improved, d=0.25），orthogonality 跨语言持续
  但 low-resource variance 增大（cosine max 0.11）。
  Control task artifact warning 升级为独立贡献：~27% lang-layer combos selectivity
  < 0.05，集中在 low-resource + shallow layers。
  Target: EACL borderline accept，以 discovery + systematic negative result 发表。

imagined_experiments:

  # ============================================================
  # plan_001: Qwen3-235B-A22B — Strong Pareto Architecture
  # ============================================================
  - name: "Qwen3-235B-A22B Full Pareto Frontier"
    plan_id: plan_001
    description: >
      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4):
      24 probed layers (every 4th), 20 languages, EN correctness probes
      (LogReg + MLP), 5 transfer conditions. Per-language Spearman rho.
    expected_results:
      # --- English probe quality ---
      en_best_auroc: 0.80
      en_best_layer: 72
      en_best_ece_raw: 0.175
      en_auroc_range: [0.54, 0.80]
      en_auroc_at_50pct_depth_L48: 0.77
      en_auroc_profile_summary: >
        L0-L20: 0.54-0.67 (early buildup);
        L24-L44: 0.70-0.76 (mid layers);
        L48-L68: 0.77-0.80 (approaching peak);
        L72: 0.80 (peak); L76-L92: 0.79-0.75 (slight decline)

      # --- Zero-shot transfer at EN-optimal layer (L72) ---
      zs_at_en_optimal_L72:
        zh: 0.71
        es: 0.70
        fr: 0.70
        de: 0.69
        ja: 0.67
        pt: 0.69
        nl: 0.68
        ru: 0.67
        ar: 0.65
        hi: 0.64
        ko: 0.66
        vi: 0.64
        tr: 0.63
        id: 0.65
        pl: 0.66
        uk: 0.65
        sw: 0.55
        bn: 0.54
        te: 0.56
        avg: 0.647

      # --- Zero-shot transfer at best transfer layer (L48) ---
      zs_at_best_transfer_L48:
        zh: 0.73
        es: 0.72
        fr: 0.71
        de: 0.70
        ja: 0.69
        pt: 0.70
        nl: 0.69
        ru: 0.69
        ar: 0.67
        hi: 0.66
        ko: 0.68
        vi: 0.66
        tr: 0.65
        id: 0.67
        pl: 0.68
        uk: 0.67
        sw: 0.58
        bn: 0.57
        te: 0.59
        avg: 0.669

      # --- Pareto metrics ---
      pareto_rho_global: -0.50
      pareto_rho_per_lang_median: -0.48
      pareto_rho_per_lang:
        zh: -0.45
        es: -0.42
        fr: -0.43
        de: -0.44
        ja: -0.47
        pt: -0.43
        nl: -0.44
        ru: -0.46
        ar: -0.50
        hi: -0.52
        ko: -0.48
        vi: -0.51
        tr: -0.53
        id: -0.49
        pl: -0.46
        uk: -0.47
        sw: -0.58
        bn: -0.56
        te: -0.55
      pareto_rho_range: [-0.58, -0.42]
      zs_langs_above_060: 16
      zs_langs_above_065: 13

      # --- Transfer method comparison at L48 (best transfer) ---
      transfer_methods_at_L48:
        zero_shot_avg: 0.669
        mean_shift_avg: 0.669
        mean_shift_delta: 0.000
        linear_proj_50_avg: 0.704
        linear_proj_50_delta: 0.035
        fewshot_25_avg: 0.695
        fewshot_25_delta: 0.026
        fewshot_100_avg: 0.715
        fewshot_100_delta: 0.046
        caclr_best_avg: 0.677
        caclr_best_delta: 0.008

      # --- Bootstrap CIs (95%) for key deltas ---
      bootstrap_ci_linear_proj_delta: [0.025, 0.045]
      bootstrap_ci_fewshot100_delta: [0.035, 0.057]
      bootstrap_ci_caclr_delta: [-0.003, 0.019]

    result_rationale: >
      Qwen3-235B-A22B 是 94 层 MoE 架构，显著深于 MVP 的 7B 模型。EN best AUROC
      从 MVP 的 0.754 提升到 0.80，因为更大模型编码更强的 correctness signal。
      Peak 在 ~77% depth (L72)，与 MVP pattern 一致——correctness 在 deep-but-not-final
      层达到峰值。

      Pareto frontier 清晰（median per-lang rho = -0.48）因为：(a) 94 层提供足够
      depth gradient 让 language specialization 逐渐显现；(b) 所有 20 语言在更深层
      的 transfer 都退化，只是退化速度不同。Low-resource 语言（sw/bn/te）rho 更强
      负（-0.55 ~ -0.58）因为它们的跨语言表征从一开始就弱，depth-induced
      specialization 影响更大。High-resource 语言 rho 较温和（-0.42 ~ -0.45）因为
      丰富的预训练数据使深层仍保持合理的跨语言对齐。

      Best transfer layer (L48, ~51% depth) vs EN-optimal (L72, ~77% depth) 的
      gap 是 Pareto tradeoff 的直接体现：L48 平均 ZS AUROC 0.669 vs L72 的 0.647，
      差 2.2pp。

      Mean-shift ΔAUROC ≡ 0 符合数学证明（rank-invariance under StandardScaler +
      logistic regression）。Linear projection +3.5pp 因为直接学习 rotation
      correction。CaCLR +0.8pp 几乎全来自 α (SB-ECE) 项而非 β (MMD) 项。

    tables:
      - name: "Table 1: Qwen3-235B Zero-Shot Transfer AUROC (Language × Layer)"
        description: >
          24 probed layers (rows) × 20 languages + EN (columns)。
          Cells: AUROC。Bold: per-language best layer。Gray: within 1pp of best。
          Bottom: per-language Spearman rho ± bootstrap 95% CI。
          Key pattern: EN-optimal L72 ≠ transfer-optimal L48 for all languages。
          Resource-tier banding visible: HIGH langs (zh/es/fr/de) show flatter
          profiles; LOW langs (sw/bn/te) show steeper drop-off at deep layers。

      - name: "Table 2: Qwen3-235B Transfer Method Comparison"
        description: >
          5 methods (columns) × 20 langs (rows), at two fixed layers (L48 = 50%
          depth, L72 = EN-optimal) + per-lang oracle。AUROC, ΔAUROC vs zero-shot,
          bootstrap 95% CI, paired permutation p, Cohen's d。

    figures_description:
      - >
        Pareto frontier scatter: x = EN AUROC (per layer), y = median ZS transfer
        AUROC (20 langs)。Each point = one layer, annotated with layer number。
        Pareto-optimal frontier highlighted。Separate traces for HIGH/MID/LOW
        resource tiers showing tier-dependent frontier shape。Clear tradeoff visible。
      - >
        Per-language Spearman rho bar chart: 20 bars sorted by |rho|, color by
        resource tier。Error bars = bootstrap 95% CI。All bars negative, clustered
        between -0.42 and -0.58。Horizontal reference at rho = 0 for contrast
        with Llama 4 Scout (plan_002) where some bars cross zero。

    analysis: >
      Qwen3-235B 作为 "strong Pareto architecture" 的角色得到验证：所有 20 语言
      都展现一致的 depth-transfer tradeoff（全部 rho 负值），没有例外。
      Architecture-specific 特征是 MoE routing 引入的层间异质性使 frontier 不如
      dense model 平滑（per-layer variance 较高），但总趋势清晰。
      16/20 语言在最优 transfer layer 达到 >0.60 AUROC，13/20 达到 >0.65，
      验证 zero-shot probe transfer 对 majority languages 可行。
      sw/bn/te 的失败是 pretraining representation 的基础限制，非 architecture-specific。

  # ============================================================
  # plan_002: Llama 4 Scout — Weak/Language-Specific Pareto
  # ============================================================
  - name: "Llama 4 Scout Full Pareto Frontier"
    plan_id: plan_002
    description: >
      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16):
      12 probed layers (every 4th), 20 languages, 5 transfer conditions.
      Per-language Spearman rho. Architecture contrast with Qwen3-235B.
    expected_results:
      # --- English probe quality ---
      en_best_auroc: 0.78
      en_best_layer: 40
      en_best_ece_raw: 0.185
      en_auroc_range: [0.55, 0.78]
      en_auroc_at_50pct_depth_L24: 0.73

      # --- Zero-shot at EN-optimal (L40) ---
      zs_at_en_optimal_L40:
        zh: 0.67
        es: 0.66
        fr: 0.66
        de: 0.65
        ja: 0.64
        pt: 0.65
        nl: 0.64
        ru: 0.64
        ar: 0.65
        hi: 0.63
        ko: 0.66
        vi: 0.62
        tr: 0.61
        id: 0.63
        pl: 0.64
        uk: 0.63
        sw: 0.54
        bn: 0.53
        te: 0.55
        avg: 0.627

      # --- Zero-shot at best transfer layer (varies by lang!) ---
      zs_at_per_lang_best:
        zh: {auroc: 0.69, best_layer: 24}
        es: {auroc: 0.68, best_layer: 24}
        fr: {auroc: 0.68, best_layer: 28}
        de: {auroc: 0.67, best_layer: 24}
        ja: {auroc: 0.66, best_layer: 28}
        pt: {auroc: 0.67, best_layer: 24}
        nl: {auroc: 0.66, best_layer: 28}
        ru: {auroc: 0.66, best_layer: 28}
        ar: {auroc: 0.66, best_layer: 40}
        hi: {auroc: 0.64, best_layer: 36}
        ko: {auroc: 0.67, best_layer: 40}
        vi: {auroc: 0.64, best_layer: 32}
        tr: {auroc: 0.63, best_layer: 32}
        id: {auroc: 0.65, best_layer: 32}
        pl: {auroc: 0.66, best_layer: 32}
        uk: {auroc: 0.65, best_layer: 32}
        sw: {auroc: 0.57, best_layer: 20}
        bn: {auroc: 0.56, best_layer: 20}
        te: {auroc: 0.57, best_layer: 24}
        avg: 0.649

      # --- KEY: Language-specific Pareto ---
      pareto_rho_global: -0.12
      pareto_rho_per_lang_median: -0.10
      pareto_rho_per_lang:
        zh: -0.35
        es: -0.30
        fr: -0.28
        de: -0.32
        ja: -0.25
        pt: -0.27
        nl: -0.22
        ru: -0.18
        ar: +0.15
        hi: +0.08
        ko: +0.12
        vi: -0.05
        tr: -0.08
        id: +0.02
        pl: -0.10
        uk: -0.05
        sw: -0.42
        bn: -0.38
        te: -0.30
      pareto_rho_range: [-0.42, +0.15]
      n_langs_positive_rho: 4
      n_langs_negative_rho_sig: 8
      n_langs_near_zero: 8

      # --- Transfer methods at L28 (compromise layer) ---
      transfer_methods_at_L28:
        zero_shot_avg: 0.638
        mean_shift_avg: 0.638
        mean_shift_delta: 0.000
        linear_proj_50_avg: 0.670
        linear_proj_50_delta: 0.032
        fewshot_25_avg: 0.662
        fewshot_25_delta: 0.024
        fewshot_100_avg: 0.682
        fewshot_100_delta: 0.044
        caclr_best_avg: 0.644
        caclr_best_delta: 0.006

      zs_langs_above_060: 15
      zs_langs_above_065: 10

    result_rationale: >
      Llama 4 Scout 是 median 档的 "weak/language-specific Pareto" 架构。
      MVP 已展示此 pattern：Llama-3.1-8B 上 ar/hi/ko 的 best transfer layer
      在最深层 (L31)，而 zh 在 L20, sw 在 L16——不同语言的最优层方向不一致。

      全量实验中此 pattern 放大：ar (rho=+0.15)、ko (+0.12)、hi (+0.08)
      在更深层 transfer 更好，因为 Llama 4 的 MoE routing 对这些语言在深层
      保持了更好的跨语言对齐（可能与 Llama 4 training data 中
      ar/ko/hi 的分布有关）。同时 zh (-0.35)、sw (-0.42) 展示传统的
      depth-degradation pattern。

      Global rho = -0.12 因为正负 rho 相互抵消——这不是 noise，而是
      genuinely language-specific behavior。与 Qwen3 的 uniform negative rho
      形成 sharp architectural contrast：同一组语言在两个架构上展现
      qualitatively different Pareto shapes。

      这直接支持 Claim 1 的 "architecture-dependent tradeoff shape" 结论。
      Important caveat: n=2 architectures 无法归因于具体 architectural feature
      （MoE routing scheme、training data composition、layer count 都不同），
      仅能报告 observational finding。

    tables:
      - name: "Table 3: Llama 4 Scout Zero-Shot Transfer AUROC (Language × Layer)"
        description: >
          12 probed layers × 20 languages。Same format as Table 1。
          KEY CONTRAST: per-language Spearman rho 有 4 个正值（ar/ko/hi/id），
          与 Qwen3 全负形成对比。用 ↑↓ arrows 标注 rho 方向。

      - name: "Table 4: Architecture Contrast — Per-Language Spearman rho"
        description: >
          20 languages (rows) × 2 architectures (columns: Qwen3 rho, Llama4 rho)。
          Sorted by rho difference。Highlighted: languages where rho sign flips
          between architectures (ar, ko, hi)。Bootstrap 95% CI for each。
          Bottom: architecture-level summary (median, IQR, % negative)。

    figures_description:
      - >
        Side-by-side Pareto scatter: Qwen3-235B (left) vs Llama 4 Scout (right)。
        Same axis scales。Qwen3 shows tight negative trend; Llama4 shows散状
        cloud with no clear single direction。Language labels colored by
        resource tier。The visual contrast IS the main Claim 1 result。
      - >
        Per-language rho comparison: paired dot plot, each language as a
        horizontal line connecting its Qwen3 rho (left dot) and Llama4 rho
        (right dot)。Lines crossing zero for ar/ko/hi clearly visible。
        Demonstrates language-specific architecture dependence。

    analysis: >
      Llama 4 Scout 的 language-specific Pareto 是 paper 最重要的 architecture
      contrast finding。Global rho -0.12 不是 "weak version of same trend"
      而是 "qualitatively different pattern"——4/20 语言的 rho 为正（deeper
      layers transfer BETTER），8/20 near zero，仅 8/20 显著负。
      这与 Qwen3 的 20/20 负值形成 stark contrast。

      实际含义：在 Llama 4 Scout 上不存在单一 "best transfer layer"——
      practitioner 需要 per-language layer selection（或 per-language oracle），
      而 Qwen3 上可以用 50% depth 的 universal rule。这是 architecture-dependent
      的 practical recommendation。

  # ============================================================
  # plan_003: CaCLR — Principled Negative Result
  # ============================================================
  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: plan_003
    description: >
      CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) implementation。
      β sweep 3 OOM (0.001–1.0), α sweep (0.01–10.0)。
      Full comparison vs zero-shot, mean-shift, linear projection,
      few-shot on both models × 20 languages。
    expected_results:
      # --- Implementation spec (reproducibility) ---
      implementation:
        mmd_kernel: gaussian_rbf
        bandwidth: median_heuristic
        optimizer: adam
        lr: 0.001
        lr_schedule: cosine_decay
        epochs: 50
        early_stopping: patience_10_on_val_bce
        init: from_standard_lr_solution
        batch_size: 256
        mmd_items: same_as_bce
        parallel_set_sizes:
          avg_per_lang: 9800
          min_lang_te: 4200
          max_lang_en: 14042

      # --- α sweep (β = 0, SB-ECE only) ---
      alpha_sweep:
        alpha_0p01: {en_auroc: 0.800, en_ece: 0.170, zs_avg_auroc: 0.647}
        alpha_0p1: {en_auroc: 0.798, en_ece: 0.145, zs_avg_auroc: 0.648}
        alpha_0p5: {en_auroc: 0.795, en_ece: 0.125, zs_avg_auroc: 0.650}
        alpha_1p0: {en_auroc: 0.790, en_ece: 0.118, zs_avg_auroc: 0.651}
        alpha_3p0: {en_auroc: 0.780, en_ece: 0.112, zs_avg_auroc: 0.648}
        alpha_10p0: {en_auroc: 0.755, en_ece: 0.108, zs_avg_auroc: 0.635}
        alpha_optimal: 0.5

      # --- β sweep (α = 0.5 fixed) — THE KEY NEGATIVE RESULT ---
      beta_sweep:
        beta_0: {delta_auroc_vs_beta0: 0.000, delta_ece: 0.000}
        beta_0p001: {delta_auroc_vs_beta0: +0.002, delta_ece: -0.001}
        beta_0p003: {delta_auroc_vs_beta0: +0.001, delta_ece: -0.001}
        beta_0p01: {delta_auroc_vs_beta0: +0.001, delta_ece: 0.000}
        beta_0p03: {delta_auroc_vs_beta0: -0.001, delta_ece: +0.001}
        beta_0p1: {delta_auroc_vs_beta0: -0.002, delta_ece: +0.002}
        beta_0p3: {delta_auroc_vs_beta0: -0.005, delta_ece: +0.003}
        beta_1p0: {delta_auroc_vs_beta0: -0.010, delta_ece: +0.005}
      beta_sweep_stats:
        max_delta_auroc: 0.002
        min_delta_auroc: -0.010
        paired_permutation_p: 0.38
        cohens_d: 0.07
        any_beta_significant_at_005: false

      # --- Component ablation ---
      component_ablation:
        bce_only: {zs_avg_auroc: 0.647, ece: 0.175}
        bce_plus_alpha: {zs_avg_auroc: 0.651, ece: 0.125}
        bce_plus_beta: {zs_avg_auroc: 0.649, ece: 0.173}
        bce_plus_alpha_plus_beta: {zs_avg_auroc: 0.652, ece: 0.124}
        alpha_contribution: +0.004_auroc_and_-0.050_ece
        beta_contribution: +0.001_auroc_and_-0.001_ece

      # --- Full method ranking (Qwen3, at L48) ---
      method_comparison_qwen_L48:
        zero_shot: {auroc: 0.669, ece: 0.165}
        mean_shift: {auroc: 0.669, ece: 0.168}
        caclr_alpha_only: {auroc: 0.673, ece: 0.135}
        caclr_full: {auroc: 0.677, ece: 0.133}
        linear_proj_50: {auroc: 0.704, ece: 0.148}
        fewshot_25: {auroc: 0.695, ece: 0.140}
        fewshot_100: {auroc: 0.715, ece: 0.128}
      method_comparison_llama_L28:
        zero_shot: {auroc: 0.638, ece: 0.172}
        mean_shift: {auroc: 0.638, ece: 0.175}
        caclr_alpha_only: {auroc: 0.642, ece: 0.142}
        caclr_full: {auroc: 0.644, ece: 0.140}
        linear_proj_50: {auroc: 0.670, ece: 0.155}
        fewshot_25: {auroc: 0.662, ece: 0.148}
        fewshot_100: {auroc: 0.682, ece: 0.135}

      # --- Tier-level CaCLR β analysis ---
      beta_effect_by_tier:
        high_resource: {delta_auroc: +0.003, n_langs: 8}
        mid_resource: {delta_auroc: +0.001, n_langs: 8}
        low_resource: {delta_auroc: -0.004, n_langs: 3}

      # --- Key deltas for paper headline ---
      caclr_delta_auroc_vs_zeroshot: 0.008
      caclr_delta_ece_vs_tempscaling: -0.003
      linear_proj_50_delta_auroc_vs_zeroshot: 0.035
      linear_proj_50_vs_caclr_delta: 0.027

    result_rationale: >
      β (MMD consistency loss) inert 的根本原因：MMD 基于 kernel-space 的
      distributional moment matching，优化 P(f(x_en)) ≈ P(f(x_tgt)) 其中
      f 是 probe logit（1-D scalar）。但跨语言 correctness 信号的 misalignment
      不是 distributional shift（mean/variance 不同），而是 geometric rotation
      ——correctness direction 在不同语言的 activation space 中指向不同方向。
      MMD 在 1-D probe output space 中无法 capture 这种 rotation，因为
      rotation 发生在高维 activation space 中、在 probe 之前。

      具体机制：(a) β=0.001-0.01 时 MMD gradient 太弱影响不了 probe weights；
      (b) β=0.03-0.1 时 MMD 推动 marginal distribution alignment 但这对
      1-D logit 意味着 match mean + variance，不 address correctness direction
      rotation；(c) β=0.3-1.0 时 MMD 主导 loss 导致 probe 退化——为了 match
      distributions 牺牲 discriminative power。Cohen's d=0.07 < 0.2（negligible
      effect size）。

      α (SB-ECE) 项有效但贡献有限：ECE 从 0.175 降到 0.125（smooth-binned
      calibration regularization），但对 AUROC 的影响仅 +0.004pp。这是因为
      SB-ECE 不改变 ranking，只改变 calibration curve shape。

      Linear projection 成功（+3.5pp）恰好证实 geometric explanation：
      it directly estimates the rotation matrix via parallel pairs，这是
      MMD mathematically cannot do 的事情。Method ranking consistent across
      两个架构，证明这不是 architecture-specific artifact。

      Zhao et al. (2019) 的预测成立：当 conditional distributions P(Y|X)
      across domains 不同时（correctness label 分布 language-dependent），
      marginal distribution matching 不保证 label prediction 改善。

    tables:
      - name: "Table 5: β Sweep — ΔAUROC over α-only Baseline"
        description: >
          β values (rows: 0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0) ×
          summary stats (columns: median ΔAUROC, mean, std, # langs improved,
          paired permutation p, Cohen's d)。Both models side-by-side。
          Key: NO β achieves p < 0.05 or d > 0.2。
          Shaded gray: β = 0 row (reference)。

      - name: "Table 6: Transfer Method Comparison — Full Ranking"
        description: >
          7 methods (rows) × 2 models × 2 fixed layers。
          Columns: AUROC, ΔAUROC vs ZS, bootstrap 95% CI, p-value, Cohen's d。
          Clear visual separation: linear-proj/few-shot cluster significantly
          above zero-shot; CaCLR-full/CaCLR-α-only marginally above;
          mean-shift identical to zero-shot。

      - name: "Table 7: Component Ablation"
        description: >
          4 configurations (BCE-only, +α, +β, +α+β) × AUROC, ECE, ΔAUROC。
          Demonstrates α contributes ECE reduction, β contributes nothing。
          Clean decomposition of CaCLR components。

    figures_description:
      - >
        β sensitivity heatmap: x = log(β), y = 20 languages sorted by
        resource tier。Color = ΔAUROC over α-only。Near-uniform white/gray
        across entire grid。No sweet spot visible。Title: "MMD consistency
        loss inert across 3 orders of magnitude and 20 languages"。
      - >
        Method ranking forest plot: 7 methods as rows, median ΔAUROC vs
        zero-shot with bootstrap 95% CI。Clear gap between
        linear-proj/few-shot cluster and CaCLR/zero-shot cluster。
        CaCLR CI overlaps with zero-shot → not distinguishable。
      - >
        Component ablation bar chart: 4 bars (BCE, +α, +β, +α+β)。
        AUROC 几乎 flat; ECE 只有 +α 的 bars 明显降低。
        Visual proof that β is the inert component。

    analysis: >
      CaCLR β inertness 是 paper 的 centerpiece negative result。论证三步：
      (1) Empirically: β across 3 OOM, d=0.07, p=0.38, both architectures;
      (2) Theoretically: Zhao et al. (2019) predicts MMD failure when
      P(Y|X) differs across domains;
      (3) Constructively: linear projection succeeds (+3.5pp) because it
      addresses the actual misalignment type (geometric rotation)。

      这关闭了 MMD distributional matching 这条路。Paper framing:
      "CaCLR is the natural baseline testing whether distributional matching
      works; the systematic negative result + geometric explanation saves
      the community from pursuing this path." CaCLR 不是 novel method
      contribution，而是 systematic test of an obvious-seeming approach。

      Positive takeaway: α-only CaCLR（即 SB-ECE regularized probes）
      provides marginal ECE improvement，可作为 calibration regularizer
      standalone recommendation。

  # ============================================================
  # plan_004: Difficulty Decomposition
  # ============================================================
  - name: "Difficulty-Controlled Decomposition Ablation"
    plan_id: plan_004
    description: >
      IRT difficulty probes → project out difficulty direction →
      retrain correctness probes on residuals → evaluate transfer。
      10 langs × 8 layers per model。Random-direction control。
    expected_results:
      # --- Difficulty probe quality ---
      difficulty_probe_r2_en:
        median: 0.40
        range: [0.22, 0.52]
        peak_layer_pct_depth: 0.65
      difficulty_probe_r2_per_tier:
        high: {median: 0.43, range: [0.25, 0.55]}
        mid: {median: 0.38, range: [0.20, 0.50]}
        low: {median: 0.30, range: [0.15, 0.42]}

      # --- Decomposition transfer effect ---
      decomposition_delta_auroc:
        overall_median: 0.015
        overall_range: [-0.012, 0.038]
        by_tier:
          high: {median: 0.020, pct_improved: 0.72}
          mid: {median: 0.013, pct_improved: 0.63}
          low: {median: 0.008, pct_improved: 0.50}
        by_depth:
          shallow_20_40pct: {median: 0.005, pct_improved: 0.48}
          mid_40_60pct: {median: 0.015, pct_improved: 0.65}
          deep_60_90pct: {median: 0.022, pct_improved: 0.78}
        overall_pct_improved: 0.65
        paired_permutation_p: 0.028
        cohens_d: 0.25

      # --- Random direction control ---
      random_direction_control:
        delta_auroc_median: 0.003
        pct_improved: 0.52
        paired_p: 0.42
        cohens_d: 0.05

      # --- Difficulty-correctness geometry ---
      difficulty_correctness_cosine:
        median: 0.20
        range: [0.10, 0.32]
        increases_with_depth: true

    result_rationale: >
      Decomposition 定性成立但 effect size 小（d=0.25），原因：
      (1) difficulty-capability separation 不是 clean 的——IRT difficulty
      只解释 ~40% variance，残差中仍混有 difficulty 信号；
      (2) difficulty direction 和 correctness direction 不完全正交
      （cosine ~0.20），projecting out difficulty 会 partially remove
      some correctness signal；
      (3) 对 shallow layers 效果弱（48% improved，接近 chance）因为
      浅层 difficulty 和 capability 更 entangled，线性 projection 分不开。

      Deep layers 效果好（78% improved，d ~0.35）因为 capability-specific
      component 在深层主导 transfer degradation——移除 shared difficulty
      component 后，残差更 cleanly 反映 language-specific capability,
      使 correctness probe 被迫 focus on transferable component。

      Random direction control (d=0.05, p=0.42) 排除 dimensionality
      reduction artifact：不是 "any direction removal helps"，而是
      specifically difficulty direction matters。

      Resource tier gradient 反映 low-resource probes 本身噪声大——
      difficulty projection 可能 remove 它们有限 signal 的一部分。

      总体：支持 Claim 2（difficulty-capability decomposition exists
      and is prescriptive），但 effect size 要求降为 qualitative claim
      with ablation support, 不是 standalone quantitative contribution。

    tables:
      - name: "Table 8: Decomposition ΔAUROC (10 Languages × 8 Layers)"
        description: >
          Languages (rows) × layers (columns)。Cells: ΔAUROC after
          difficulty removal。Green >1pp, white ±1pp, red <-1pp。
          Marginals: % improved per language, per layer。
          Clear pattern: improvement concentrated at deep layers
          and high-resource languages。

      - name: "Table 9: Decomposition vs Random Direction Control"
        description: >
          3 conditions (rows: original, difficulty-removed, random-removed)
          × summary (median AUROC, ΔAUROC, bootstrap CI, p, d)。
          Per-architecture。Demonstrates specificity of difficulty direction。

    figures_description:
      - >
        Improvement rate vs normalized depth: bar chart, 8 bars from
        20% to 90% depth。Monotonic increase from ~48% to ~78%。
        Horizontal dashed line at 50% (chance)。Supports narrative that
        capability-specific component drives deep-layer degradation。
      - >
        Decomposition effect size by resource tier: grouped box plots
        (HIGH/MID/LOW)。Decreasing median and increasing variance
        from HIGH to LOW。

    analysis: >
      Decomposition 是 Claim 2 的 supporting evidence，降级为 qualitative。
      Key insight: difficulty is the transferable component (shared across
      languages), capability is the degrading component (language-specific)。
      At deep layers where capability dominates, removing difficulty helps
      because it forces the probe to rely on the (smaller but still
      transferable) capability signal。

      Effect size (d=0.25) 不足以作为 standalone method recommendation，
      但足以支撑 "difficulty-capability decomposition exists" 的 analytical
      claim。需要 supplementary ablation（vary projection dimension,
      IRT model complexity）来 strengthen。

  # ============================================================
  # plan_005: Cross-Lingual Orthogonality
  # ============================================================
  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: plan_005
    description: >
      Verbalized confidence direction extraction → cosine with
      correctness direction across 20 languages × 2 architectures。
      Resource tier and language family analysis。
    expected_results:
      # --- Cosine similarities ---
      cosine_en_qwen: 0.032
      cosine_en_llama: 0.036
      cosine_per_lang_qwen:
        zh: 0.038
        es: 0.035
        fr: 0.033
        de: 0.036
        ja: 0.040
        pt: 0.034
        nl: 0.033
        ru: 0.042
        ar: 0.055
        hi: 0.058
        ko: 0.050
        vi: 0.060
        tr: 0.062
        id: 0.048
        pl: 0.040
        uk: 0.045
        sw: 0.095
        bn: 0.088
        te: 0.078
      cosine_per_lang_llama:
        zh: 0.042
        es: 0.038
        fr: 0.036
        de: 0.040
        ja: 0.045
        pt: 0.037
        nl: 0.036
        ru: 0.048
        ar: 0.060
        hi: 0.065
        ko: 0.055
        vi: 0.068
        tr: 0.070
        id: 0.052
        pl: 0.045
        uk: 0.050
        sw: 0.110
        bn: 0.098
        te: 0.085

      # --- Summary statistics ---
      cosine_median_all_langs_qwen: 0.044
      cosine_median_all_langs_llama: 0.050
      cosine_range_overall: [0.032, 0.110]
      all_below_012: true
      cosine_by_tier:
        high: {median: 0.037, var: 0.00003}
        mid: {median: 0.054, var: 0.00008}
        low: {median: 0.090, var: 0.00012}
      resource_spearman_rho: -0.58
      resource_spearman_p: 0.008
      cross_architecture_correlation: 0.94

    result_rationale: >
      Orthogonality 持续因为 correctness-confidence separation 是
      transformer 处理 MCQA 的 structural property：correctness 是
      representation-level 属性（模型内部是否 "知道"），confidence 是
      output-level 属性（模型 verbalized 的 uncertainty，受 RLHF 优化）。
      两者 occupy 不同 subspaces。

      English cosine replicates Miao & Ungar (2026)（~0.035）。
      Non-English cosines 较高（median 0.044-0.050）因为：
      (a) Non-English confidence verbalization 更 noisy（模型不擅长
      用非英语表达 uncertainty）→ confidence probe 更 noisy →
      噪声 correlation 微增 cosine；
      (b) Low-resource 语言中 confidence probe 可能 capture
      language-switching signal 而非 pure confidence。

      sw 的 cosine 最高（0.095-0.110）但仍远低于表示 meaningful
      alignment 的 0.5+。Variance 随 resource tier 增加
      （0.00003 → 0.00012）反映 probe quality 在 low-resource 下更
      不稳定。

      Cross-architecture correlation = 0.94：orthogonality pattern
      is model-agnostic，由 language properties 决定而非 architecture。
      Claim 4 加 variance caveat："persists but with increasing
      variance for lower-resource languages"。

    tables:
      - name: "Table 10: Correctness-Confidence Cosine by Language and Architecture"
        description: >
          20 langs (rows, grouped by tier) × 2 architectures (column pairs)。
          Each cell: cosine ± bootstrap 95% CI。Bottom: tier medians,
          Spearman rho with log(resource estimate)。All < 0.12。

    figures_description:
      - >
        Cosine vs resource tier: strip plot with box overlay, 3 tiers
        (HIGH/MID/LOW)。Both architectures as separate colors。
        Clear increasing trend。Max point (sw, 0.110) annotated。
        Dashed line at 0.12 threshold。

    analysis: >
      Extends Miao & Ungar (2026) to multilingual settings。Universal
      orthogonality confirms output-based calibration is structurally
      limited regardless of language. Novel finding: resource-tier gradient
      (rho = -0.58, p = 0.008) suggests abundant pretraining helps
      separate correctness from confidence representations。

      Claim 4 framing: orthogonality holds universally (max 0.11 < 0.12)
      but variance caveat needed for low-resource languages where the
      separation is weaker。

  # ============================================================
  # plan_006: Probe Complexity Comparison
  # ============================================================
  - name: "Probe Complexity Comparison (LogReg vs MLP)"
    plan_id: plan_006
    description: >
      Logistic regression vs 2-layer MLP at each probed layer,
      both models。English AUROC, cross-lingual transfer gap,
      calibration quality comparison。
    expected_results:
      # --- English performance ---
      logreg_en_best_qwen: 0.80
      mlp_en_best_qwen: 0.825
      logreg_en_best_llama: 0.78
      mlp_en_best_llama: 0.80
      mlp_en_advantage: 0.022

      # --- Transfer gap (EN_AUROC - ZS_median) ---
      logreg_transfer_gap_qwen: 0.131
      mlp_transfer_gap_qwen: 0.185
      logreg_transfer_gap_llama: 0.142
      mlp_transfer_gap_llama: 0.195
      gap_difference: 0.054

      # --- Per-layer analysis ---
      mlp_advantage_en_shallow: 0.010
      mlp_advantage_en_deep: 0.030
      mlp_transfer_disadvantage_shallow: 0.020
      mlp_transfer_disadvantage_deep: 0.065

      # --- Cross-lingual comparison ---
      logreg_better_transfer_pct: 0.82
      exceptions: "zh, es (high-resource where MLP nonlinearity partially transfers)"

      # --- Calibration ---
      logreg_ece_median: 0.135
      mlp_ece_median: 0.148

    result_rationale: >
      MLP 在 English 上高 ~2pp 因为 correctness signal 有 small nonlinear
      component（层间交互、feature conjunction）。但 nonlinear component
      is language-specific：MLP 学到的 English-specific nonlinear boundary
      不 generalize cross-lingually，导致 transfer gap 大 5.4pp。

      Gap 在 deep layers 更大（6.5pp vs 2.0pp shallow）因为深层
      representations 有更复杂的 language-specific structure 供 MLP exploit。
      MLP overfits to English deep-layer nonlinearities。

      82% 语言 LogReg transfer 更好；例外是 zh/es，high-resource 语言
      where MLP 的 nonlinear component partially transfers due to shared
      pretraining features。

      This validates paper's focus on linear probes and reinforces
      geometric (linear subspace) framing。Goes in supplementary。

    tables:
      - name: "Table S1: Probe Complexity — EN AUROC and Transfer Gap by Layer"
        description: >
          Supplementary。Layers (rows) × (LogReg EN, MLP EN, LogReg ZS,
          MLP ZS, LogReg gap, MLP gap) for each model。Shows MLP advantage
          concentrates in EN at deep layers, paid for by larger transfer gap。

    figures_description:
      - >
        Transfer gap vs depth: two curves (LogReg, MLP) diverging at
        deeper layers。MLP gap grows ~3× faster。Annotation: "Linear
        probes: better for cross-lingual transfer"。

    analysis: >
      Methodological validation supporting linear probe choice。
      The nonlinear component is real (MLP +2pp EN) but non-transferable
      (MLP -5.4pp gap increase)。Confirms correctness signal's
      transferable component is linear/geometric。Supplementary material。

  # ============================================================
  # plan_007: Additional Benchmark Evaluation
  # ============================================================
  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: plan_007
    description: >
      Evaluate best probes + CaCLR on Belebele (reading comprehension)
      and MMLU-ProX (translated MCQA), 20 languages each。
      Validates generalization beyond GlobalMMLU。
    expected_results:
      # --- Belebele ---
      belebele_en_best_auroc_qwen: 0.77
      belebele_zs_median_qwen: 0.65
      belebele_pareto_rho_qwen: -0.45
      belebele_linear_proj_delta: 0.030
      belebele_caclr_beta_delta: 0.002

      # --- MMLU-ProX ---
      mmlupx_en_best_auroc_qwen: 0.81
      mmlupx_zs_median_qwen: 0.67
      mmlupx_pareto_rho_qwen: -0.48
      mmlupx_linear_proj_delta: 0.034
      mmlupx_caclr_beta_delta: 0.003

      # --- Cross-benchmark consistency ---
      rank_corr_globalmmlu_vs_belebele: 0.80
      rank_corr_globalmmlu_vs_mmlupx: 0.90
      method_ranking_consistent: true
      caclr_beta_inert_all_benchmarks: true

    result_rationale: >
      Belebele 是 reading comprehension → correctness signal 不同于
      factual knowledge，EN AUROC 略低（0.77 vs 0.80）。但 Pareto 和
      method ranking 一致，因为底层机制相同：model representations
      encode correctness at mid-depth, 深层 language-specialize。

      MMLU-ProX 与 GlobalMMLU format 接近（translated MCQA），结果更
      相似（0.81 EN, -0.48 rho）。Per-language rank correlation 0.90
      confirms transfer difficulty is model property, not benchmark artifact。

      CaCLR β inert across all benchmarks → rules out GlobalMMLU-specific
      explanation for negative result。Linear projection consistent
      (+3.0-3.4pp) → the geometric correction generalizes。

    tables:
      - name: "Table S2: Cross-Benchmark Generalization"
        description: >
          Supplementary。3 benchmarks (rows) × key metrics (EN AUROC,
          ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ)。
          Per-language AUROC rank correlations between benchmarks。

    figures_description:
      - >
        Per-language AUROC scatter: GlobalMMLU vs Belebele (left panel),
        GlobalMMLU vs MMLU-ProX (right)。Each point = language。
        Diagonal reference line。High correlation confirms
        benchmark-invariant transfer difficulty ranking。

    analysis: >
      Straightforward generalization validation。One paragraph in
      supplementary。Addresses "only MCQA" concern partially
      (Belebele is reading comprehension)。CaCLR inertness replicates →
      strengthens negative result。

  # ============================================================
  # plan_010: Quantization Validation
  # ============================================================
  - name: "Quantization Validation Ablation"
    plan_id: plan_010
    description: >
      (a) W4A16 vs FP16 at 5 layers for Llama 4 Scout (5% subset);
      (b) GPTQ-Int4 vs FP16 at 5 layers for Qwen3-235B (5% subset)。
    expected_results:
      # --- Llama 4 Scout: W4A16 vs FP16 ---
      llama_w4a16_vs_fp16:
        auroc_max_diff: 0.009
        auroc_mean_diff: 0.004
        pearson_r: 0.996
        rank_agreement_pct: 0.97
        per_layer:
          L8: {w4a16: 0.631, fp16: 0.635, diff: -0.004}
          L16: {w4a16: 0.698, fp16: 0.702, diff: -0.004}
          L24: {w4a16: 0.733, fp16: 0.738, diff: -0.005}
          L32: {w4a16: 0.762, fp16: 0.769, diff: -0.007}
          L40: {w4a16: 0.778, fp16: 0.787, diff: -0.009}

      # --- Qwen3-235B: GPTQ-Int4 vs FP16 ---
      qwen_int4_vs_fp16:
        auroc_max_diff: 0.011
        auroc_mean_diff: 0.005
        pearson_r: 0.995
        rank_agreement_pct: 0.96
        per_layer:
          L16: {int4: 0.642, fp16: 0.648, diff: -0.006}
          L32: {int4: 0.732, fp16: 0.737, diff: -0.005}
          L48: {int4: 0.770, fp16: 0.774, diff: -0.004}
          L64: {int4: 0.798, fp16: 0.803, diff: -0.005}
          L80: {int4: 0.790, fp16: 0.801, diff: -0.011}

      quantization_distortion_significant: false
      conclusion: "Quantization introduces ≤1.1pp AUROC difference, well within bootstrap CIs"

    result_rationale: >
      4-bit weight quantization（W4A16 和 GPTQ-Int4）对 correctness probing
      影响很小，因为：(a) weight quantization 不影响 activation precision
      （W4A16 的 activations 仍是 FP16）；(b) 高维 activation space (4096+
      dims) 中 per-dimension 微扰在 aggregation 后接近 cancel out；
      (c) correctness probe operates on rank-order，not absolute values——
      small uniform perturbations preserve ranking。

      Qwen3 deep layer (L80) 差异略大 (1.1pp) 因为 MoE routing 在深层
      accumulated more quantization error through expert selection。
      但仍在 bootstrap CI 内。Pearson r > 0.995 confirms near-perfect
      linear relationship between quantized and FP16 scores。

    tables:
      - name: "Table S3: Quantization Validation"
        description: >
          Supplementary。5 layers × (Quantized AUROC, FP16 AUROC, Δ,
          rank correlation) for each model。All Δ within bootstrap CI。
          Conclusion: quantization does not distort correctness signals。

    figures_description: []
    analysis: >
      Necessary reviewer reassurance, expected non-issue。One paragraph
      + table in supplementary。Largest observed difference (1.1pp at
      deep layer for Qwen3 INT4) is within noise bounds。

  # ============================================================
  # plan_011: CKA Analysis — Downgraded to Suggestive
  # ============================================================
  - name: "CKA Cross-Lingual Representation Similarity"
    plan_id: plan_011
    description: >
      CKA (linear kernel) between EN and 19 target languages at every
      probed layer, both models。Partial correlation controlling depth。
      Between-language analysis。Subspace angle analysis。
    expected_results:
      # --- CKA values (Qwen3, representative) ---
      cka_qwen_representative:
        zh_L12: 0.87
        zh_L48: 0.72
        zh_L72: 0.58
        zh_L92: 0.50
        sw_L12: 0.76
        sw_L48: 0.55
        sw_L72: 0.38
        sw_L92: 0.28

      # --- CKA summary ---
      cka_shallow_median: 0.83
      cka_deep_median: 0.48
      cka_decline_with_depth_significant: true
      cka_by_tier_at_70pct_depth:
        high: 0.58
        mid: 0.46
        low: 0.34

      # --- KEY: Pooled correlation (confounded by depth) ---
      cka_transfer_pooled:
        qwen_pearson_r: 0.55
        qwen_p: 0.00001
        llama_pearson_r: 0.48
        llama_p: 0.0001
        pooled_r: 0.52
        pooled_p: 0.000001

      # --- KEY: Partial correlation controlling normalized depth ---
      cka_partial_corr_controlling_depth:
        qwen_r: 0.20
        qwen_p: 0.08
        llama_r: 0.15
        llama_p: 0.16
        pooled_r: 0.18
        pooled_p: 0.11

      # --- KEY: Between-language correlation (strongest test) ---
      between_lang_same_layer:
        L_25pct_depth:
          pearson_r: 0.48
          p: 0.032
          n: 19
        L_50pct_depth:
          pearson_r: 0.55
          p: 0.014
          n: 19
        L_75pct_depth:
          pearson_r: 0.52
          p: 0.022
          n: 19
        median_across_layers_r: 0.52
        median_across_layers_p: 0.02

      # --- Per-language within-language Spearman ---
      per_lang_spearman_median: -0.45
      per_lang_spearman_significant_fraction: 0.40
      per_lang_n_per_language_qwen: 24
      per_lang_n_per_language_llama: 12

      # --- Subspace angle analysis ---
      subspace_angle_correctness:
        shallow_median_deg: 15
        deep_median_deg: 38
        increases_with_depth: true
      subspace_angle_random_baseline:
        median_deg: 72

      # --- CKA cliff analysis ---
      cka_cliff_qwen:
        location_pct_depth: 0.72
        cliff_magnitude: 0.15
      cka_cliff_llama:
        location_pct_depth: 0.65
        cliff_magnitude: 0.08

    result_rationale: >
      CKA pooled correlation (r=0.52, p<0.001) 看起来 strong 但有严重
      depth confound：deeper layers simultaneously have lower CKA AND
      lower transfer AUROC，所以 correlation 大部分来自 shared depth effect。

      Partial correlation controlling normalized depth 是 THE critical test
      （Dream RD2, 3-tier consensus）：r=0.18, p=0.11。这意味着 CKA 在
      控制 depth 后几乎没有额外 explanatory power。Depth alone explains
      most of the variance in both CKA and transfer AUROC。这直接导致
      CKA 从 "geometric analysis" 降级为 "suggestive correlational analysis"。

      BUT between-language correlation 成立：在同一 depth，语言间 CKA
      与 transfer 的 correlation r=0.52, p=0.02 (n=19)。这说明
      "languages with higher CKA transfer better" 是 valid between-language
      claim，只是不能说 "CKA predicts within-language depth degradation"。

      Per-language Spearman 只有 40% significant（Qwen n=24 较好，
      Llama n=12 power 不足），与 pilot 一致。

      Subspace angle analysis provides quantitative geometric evidence：
      correctness subspace angle increases from 15° (shallow) to 38° (deep)，
      远小于 random baseline 72°，证实 correctness direction 作为
      low-dimensional subspace feature 存在但 rotation 随 depth 增加。

      CKA cliff steepness 差异（Qwen 0.15 at 72% vs Llama 0.08 at 65%）
      qualitatively explains Pareto strength difference：Qwen 在更深处
      有更 abrupt 的 CKA drop，对应更 uniform 的 negative transfer trend。

    tables:
      - name: "Table 11: CKA Similarity Heatmap (Languages × Layers)"
        description: >
          Probed layers (rows) × 19 target languages (columns, sorted by
          resource tier)。Cells: CKA values, color-coded。Both models。
          Clear depth gradient and resource-tier banding。

      - name: "Table 12: CKA as Transfer Predictor — Partial Correlation Analysis"
        description: >
          KEY TABLE。Rows: (1) Pooled CKA-transfer r, (2) Depth-transfer r,
          (3) Partial CKA-transfer controlling depth, (4) Between-language
          same-depth CKA-transfer r。Columns: r, R², p, interpretation。
          Demonstrates that partial r=0.18 (p=0.11) → CKA is suggestive only,
          but between-language r=0.52 (p=0.02) → valid between-language claim。

      - name: "Table 13: Subspace Angle Analysis"
        description: >
          Depth bins (rows) × statistics (columns: median angle, IQR,
          random baseline)。Both models。Shows correctness subspace
          rotation increases with depth but remains far from random。
          Quantitative support for geometric narrative。

    figures_description:
      - >
        CKA × transfer scatter with depth as confound: three panels。
        (Left) CKA vs transfer AUROC, pooled, r=0.52 — looks impressive。
        (Center) Same scatter but color = normalized depth — reveals that
        depth drives both axes。
        (Right) Residualized CKA vs residualized transfer (after removing
        depth effect) — weak relationship, r=0.18, the honest picture。
      - >
        Between-language CKA-transfer scatter at 50% depth: each point =
        one language。r=0.52, p=0.02。This IS the valid claim。
        Labels on outliers (sw low CKA + low transfer, zh high CKA +
        high transfer)。
      - >
        Subspace angle vs depth: line plots for 3 representative languages
        with shaded band for full 19-language range。Random baseline as
        horizontal reference at 72°。Increasing trend confirms geometric
        rotation hypothesis。

    analysis: >
      CKA analysis 降级为 "suggestive correlational analysis" 基于
      partial correlation result (r=0.18, p=0.11)。Paper 必须明确承认
      depth confound 并 present partial correlation as the honest test。

      Salvageable claims:
      (1) Between-language: "languages with higher CKA show less transfer
      degradation at matched depth" (r=0.52, p=0.02) — valid
      (2) Qualitative: CKA cliff steepness differs across architectures,
      consistent with Pareto strength difference — suggestive
      (3) Subspace angle: correctness direction rotation increases with
      depth (15° → 38°) — quantitative geometric evidence

      NOT supportable: "CKA explains why transfer degrades with depth"
      (depth itself explains this; CKA adds marginal information)。

      For the CaCLR negative result narrative: CKA analysis provides
      suggestive geometric context (rotation not distributional shift)
      but the argument must lean more on Zhao et al. (2019) theory than
      on CKA empirics。

  # ============================================================
  # plan_012: Linear Projection Sensitivity
  # ============================================================
  - name: "Linear Projection Sensitivity Analysis"
    plan_id: plan_012
    description: >
      Vary parallel pairs (10, 20, 50, 100, 200) for linear projection。
      Both models × 5 representative layers × 20 languages。
    expected_results:
      # --- Learning curve ---
      pairs_10: {delta_auroc_median: 0.012, std: 0.022}
      pairs_20: {delta_auroc_median: 0.023, std: 0.016}
      pairs_50: {delta_auroc_median: 0.035, std: 0.011}
      pairs_100: {delta_auroc_median: 0.040, std: 0.008}
      pairs_200: {delta_auroc_median: 0.042, std: 0.007}

      saturation_knee: 60
      pairs_for_90pct_improvement: 50
      pairs_for_95pct_improvement: 80

      # --- Architecture comparison ---
      qwen_knee: 55
      llama_knee: 65
      consistent_across_models: true

      # --- vs CaCLR crossover ---
      pairs_to_match_caclr: 15
      pairs_to_exceed_caclr: 20

      # --- Per-tier response ---
      high_resource_pairs_50_delta: 0.028
      mid_resource_pairs_50_delta: 0.038
      low_resource_pairs_50_delta: 0.045

    result_rationale: >
      Linear projection 学习 rotation matrix mapping source → target
      language representation space。Sample complexity 低因为
      correctness-relevant subspace is low-rank：虽然 full activation
      space is 4096+ dims，但 correctness signal 集中在 few dimensions，
      所以 effective mapping dimension 很小。

      10 pairs: underdetermined but captures dominant rotation (+1.2pp)。
      50 pairs: 90% of achievable improvement（major rotation axes identified）。
      100+ pairs: diminishing returns（fine corrections of minor axes）。

      Knee at ~55-65 pairs consistent with cross-lingual alignment
      literature (MUSE/VecMap: 50-100 bilingual dictionary entries suffice)。
      Llama 略需更多 pairs（65 vs 55）因为其 MoE routing 引入更多
      representation heterogeneity。

      Low-resource 语言 benefit MORE from linear projection (+4.5pp vs
      +2.8pp high-resource) 因为它们的 geometric misalignment 更大
      → more room for correction。

      Practical headline: "~50 parallel pairs + simple linear projection
      matches or exceeds CaCLR's entire training pipeline, surpassing
      CaCLR at just ~20 pairs"。

    tables:
      - name: "Table 14: Linear Projection Sample Efficiency"
        description: >
          Pair counts (rows: 10, 20, 50, 100, 200) × (median ΔAUROC,
          mean, std, min, max, % langs improved)。Both models。
          Clear diminishing returns after 50 pairs。

    figures_description:
      - >
        Learning curve: x = # parallel pairs (log scale), y = median
        ΔAUROC。Two curves (Qwen3, Llama4) with shaded ±1 std band。
        Annotated knee point (~55-65)。Horizontal dashed line: CaCLR-full
        ΔAUROC → linear projection surpasses at ~20 pairs。This is one
        of the paper's most compelling visuals。

    analysis: >
      Linear projection's sample efficiency is the constructive complement
      to CaCLR's negative result。The practical message is clear and
      actionable: ~50 parallel pairs (trivially obtainable) provide a
      simple, effective, zero-target-label solution that outperforms
      distributional matching。

      The learning curve figure — showing linear projection surpassing
      CaCLR at 20 pairs — directly illustrates the cost-benefit argument。

  # ============================================================
  # plan_013: Control Tasks (Cross-lingual Extension)
  # ============================================================
  - name: "Probing Control Tasks — Full Cross-Lingual Analysis"
    plan_id: plan_013
    description: >
      Extend Hewitt & Liang control tasks to 20 languages × both models。
      Selectivity across layers, languages, resource tiers。
      Capacity artifact identification。
    expected_results:
      # --- English baseline (extends MVP result) ---
      en_selectivity_qwen:
        shallow_avg: 0.03
        mid_avg: 0.18
        deep_avg: 0.27
      en_selectivity_llama:
        shallow_avg: 0.03
        mid_avg: 0.15
        deep_avg: 0.24

      # --- Cross-lingual selectivity ---
      selectivity_by_tier:
        high_resource: {median: 0.19, range: [0.03, 0.28]}
        mid_resource: {median: 0.14, range: [0.02, 0.24]}
        low_resource: {median: 0.09, range: [0.01, 0.18]}

      # --- KEY METRIC: fraction below 0.05 threshold ---
      selectivity_below_005_fraction: 0.27
      selectivity_below_005_by_tier:
        high: 0.20
        mid: 0.28
        low: 0.42
      selectivity_below_005_by_depth:
        shallow_0_30pct: 0.85
        mid_30_60pct: 0.18
        deep_60_100pct: 0.08

      # --- Capacity artifact languages ---
      worst_selectivity_combos:
        - {lang: sw, depth_range: "0-50%", median_selectivity: 0.02}
        - {lang: bn, depth_range: "0-50%", median_selectivity: 0.03}
        - {lang: te, depth_range: "0-40%", median_selectivity: 0.02}
        - {lang: all, depth_range: "0-20%", median_selectivity: 0.03}

      # --- Control AUROC (should be near chance) ---
      control_auroc_median: 0.50
      control_auroc_range: [0.48, 0.53]

      # --- Summary ---
      all_selectivities_positive: true
      pct_above_010: 0.73
      pct_above_005: 0.73

    result_rationale: >
      27% of lang-layer combos below 0.05 selectivity — concentrated in
      two dimensions: (a) shallow layers universally (0-20% depth: 85%
      below threshold) because correctness signal hasn't yet emerged;
      (b) low-resource languages at mid-depth (sw/bn/te 42% below).

      Shallow-layer low selectivity is expected and benign — paper doesn't
      claim correctness signal at shallow layers. But low-resource
      mid-depth artifacts are a genuine concern: probes with selectivity
      < 0.05 may reflect capacity memorization rather than correctness signal。
      This means ~42% of low-resource lang-layer combinations should be
      interpreted with caution。

      Paper framing: this is itself a methodological contribution。
      "~27% of cross-lingual probing results in our setting are
      capacity artifacts. We recommend selectivity ≥ 0.05 as minimum
      threshold for cross-lingual probe interpretability, especially
      for low-resource languages." This warning generalizes beyond our
      specific paper to any cross-lingual probing study。

      Control AUROC near 0.50 confirms LogReg has negligible capacity
      to memorize random labels in high-dim space — any above-baseline
      performance reflects real signal。

    tables:
      - name: "Table S4: Control Task Selectivity Heatmap"
        description: >
          20 languages (rows, by tier) × representative layers (columns)。
          Cells: selectivity (real AUROC - control AUROC)。Color: green
          >15pp, yellow 10-15pp, orange 5-10pp, red <5pp。
          Clear resource-tier × depth pattern。Both models。

      - name: "Table 15: Capacity Artifact Warning — Summary Statistics"
        description: >
          Main text table (not supplementary — this is an independent
          contribution)。Resource tiers (rows) × depth bins (columns)。
          Cells: % of combos with selectivity < 0.05。Total: 27%。
          Recommendation: minimum selectivity threshold for interpretable
          cross-lingual probing。

    figures_description:
      - >
        Selectivity by resource tier: box plots (HIGH/MID/LOW)。
        Dashed line at 0.05。LOW tier box extends below threshold,
        showing substantial fraction of capacity artifacts。
      - >
        Selectivity × depth × tier: line plots showing selectivity
        profiles for 3 tiers。LOW tier curve rises slowly and stays
        lower throughout。Shaded region below 0.05 = "artifact zone"。

    analysis: >
      Control task artifact finding 升级为独立贡献。The ~27% artifact
      rate challenges uncritical cross-lingual probing and provides
      actionable guidance (selectivity ≥ 0.05 threshold)。

      This is distinct from the paper's other claims — it's a
      methodological warning for the cross-lingual probing community,
      not specific to correctness or calibration。

      For the paper's own claims: we exclude combos below threshold
      from statistical tests where feasible, and note the caveat
      for low-resource claims where exclusion isn't feasible。

  # ============================================================
  # plan_008: Gemma 4 31B Dense (P2 Camera-Ready)
  # ============================================================
  - name: "Gemma 4 31B Dense Pareto Frontier"
    plan_id: plan_008
    description: >
      Third architecture for camera-ready。60 layers, dense, FP16。
      Provides dense vs MoE architectural contrast。
    expected_results:
      en_best_auroc: 0.79
      en_best_layer: 42
      zs_transfer_auroc_median: 0.67
      best_transfer_layer: 30
      pareto_rho_per_lang_median: -0.55
      pareto_rho_range: [-0.62, -0.48]
      pareto_rho_std: 0.04
      zs_langs_above_065: 12
      linear_proj_delta: 0.033
      cka_cliff_magnitude: 0.18
      cka_cliff_steeper_than_moe: true

    result_rationale: >
      Dense architecture 提供 critical architectural contrast：
      (a) rho std = 0.04 (vs MoE Qwen 0.05, Llama 0.12) 因为 no routing
      heterogeneity → more uniform depth effect;
      (b) rho median = -0.55, 较 MoE 更 consistent negative 因为 dense
      model 所有 tokens 经过所有层 → cleaner monotonic specialization;
      (c) CKA cliff steeper (0.18 vs Qwen's 0.15) 因为 MoE routing
      provides partial buffer against geometric misalignment（different
      experts can maintain cross-lingual features at deep layers）;
      (d) EN AUROC 0.79 与 larger MoE models comparable despite smaller
      parameter count → dense architecture is parameter-efficient for
      representation quality。

      三架构对比 strengthens architecture-dependence claim from
      "two MoE models differ moderately" to "dense shows distinct,
      more uniform Pareto shape"。

    tables:
      - name: "Table CR1: Three-Architecture Pareto Comparison"
        description: >
          Camera-ready。3 architectures (rows) × (EN AUROC, ZS median,
          rho median, rho std, rho range, CKA cliff, linear-proj Δ)。
          Dense model: lowest rho std (most uniform tradeoff)。

    figures_description:
      - >
        Three-panel Pareto frontier: Qwen3-MoE, Llama4-MoE, Gemma4-Dense。
        Dense shows smoothest, most monotonic frontier。
        Visual argument for architecture-dependence。

    analysis: >
      Camera-ready addition。Dense vs MoE is the strongest architecture
      contrast: MoE routing heterogeneity produces language-specific
      Pareto (Llama4) or moderate uniform Pareto (Qwen3); dense model
      produces consistently uniform strong Pareto。Three-architecture
      triangulation makes Claim 1 considerably more convincing。

  # ============================================================
  # plan_009: Extended Language Coverage (P2 Camera-Ready)
  # ============================================================
  - name: "Extended Language Coverage (50+ Languages)"
    plan_id: plan_009
    description: >
      Expand from 20 to 50+ languages for camera-ready。
      Full GlobalMMLU/Belebele language coverage。
    expected_results:
      total_languages: 52
      zs_langs_above_060: 32
      zs_langs_above_065: 25
      zs_median_auroc_52lang: 0.64
      zs_auroc_range: [0.50, 0.73]
      new_failed_langs: [am, my, zu, sn, rw, xh, ny, mg]
      n_below_055: 10
      resource_tier_gradient_replicates: true
      pareto_rho_median_52lang: -0.47
      linear_proj_delta_52lang: 0.032
      fraction_viable_with_linear_proj: 0.67

    result_rationale: >
      52 语言扩展增加大量 low-resource 和 typologically diverse 语言。
      Median AUROC drops（0.64 vs curated 20 的 0.66）因为新增语言
      disproportionately low-resource。10 语言 < 0.55（am/my/zu/sn/rw
      /xh/ny/mg + sw/bn from original）——minimal pretraining representation。

      Resource tier gradient 更 pronounced：extended tail 提供更多
      data points 在 low end。Pareto rho 微弱化（-0.47）因为很多新增
      语言的 probe 本身 noisy → rho estimate 不准。

      Linear projection consistent at +3.2pp，extends viability from
      32/52 (62% ZS) to 35/52 (67% with projection)。
      Remaining 17 需要 language-specific solutions。

      Practical conclusion: probe-based cross-lingual calibration is
      viable for majority (67%) of tested languages with minimal effort;
      the remaining third requires per-language probes or alternative
      approaches。

    tables:
      - name: "Table CR2: Extended 52-Language Results"
        description: >
          Camera-ready。52 languages sorted by ZS AUROC, grouped into
          4 tiers: Strong (>0.70), Viable (0.65-0.70), Marginal
          (0.55-0.65), Failed (<0.55)。Columns: language, family,
          script, resource tier, ZS AUROC, linear-proj AUROC。

    figures_description:
      - >
        Language coverage world map: countries colored by best ZS AUROC。
        Visual demonstration of geographic viability pattern。
        Europe/East Asia green; sub-Saharan Africa/Southeast Asia red。

    analysis: >
      Camera-ready scale extension。Confirms resource-tier gradient is
      the dominant predictor。Sets realistic practitioner expectations
      and motivates future work on low-resource probe training。
      The 67% viability rate (with linear projection) is the practical
      headline for this extension。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c36dfab5-0ff7-40c9-acb9-6fe2ab3a9e27",
  "isSidechain": false,
  "requestId": "req_011CbF2cH1oF5iNeSGS9EYv6",
  "type": "assistant",
  "uuid": "29aa6168-a612-40b2-bfb4-087779ebe697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019gDkAUqWsCMMAZuVPmyvNU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31059,
      "cache_read_input_tokens": 35950,
      "output_tokens": 27715,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31059,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 27715,
          "cache_read_input_tokens": 35950,
          "cache_creation_input_tokens": 31059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31059
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：CaCLR consistency loss inert（β sweep 无效），但 Pareto discovery 稳固且 linear projection 是 practical solution；CKA 降级为 suggestive；paper 以 discovery + principled…",
  "leafUuid": "29aa6168-a612-40b2-bfb4-087779ebe697",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer: Pareto frontiers, negative CaCLR result, linear projection baseline",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：CaCLR consistency loss inert（β sweep 无效），但 Pareto discovery 稳固且 linear projection 是 practical solution；CKA 降级为 suggestive；paper 以 discovery + principled…",
  "leafUuid": "29aa6168-a612-40b2-bfb4-087779ebe697",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Multilingual correctness probe transfer: Pareto frontiers, negative CaCLR result, linear projection baseline",
  "sessionId": "f5ffb2d4-a6f7-45a1-a90b-ea92a386fea9"
}
```

---
