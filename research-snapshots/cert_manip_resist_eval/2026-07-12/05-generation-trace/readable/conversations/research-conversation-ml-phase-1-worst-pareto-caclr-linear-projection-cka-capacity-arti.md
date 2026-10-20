# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：大模型上 Pareto 信号噪声大、CaCLR 和 linear projection 均不稳定、CKA 无解释力、大面积 capacity arti

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a.jsonl`
- **Structured JSON:** [`2a4774ef72a926058c87.json`](../../sessions/2a/2a4774ef72a926058c87.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:55:53.708Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:55:53.708Z",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：大模型上 Pareto 信号噪声大、CaCLR 和 linear projection 均不稳定、CKA 无解释力、大面积 capacity artifacts 侵蚀低资源结果；需重构为 cross-lingual probing 方法论批判 + viability boundary 刻画\n核心假设：['大模型（235B MoE / Scout MoE）的 correctness signal 比 7B dense 更分散，probe AUROC 提升有限或 noisy', 'Pareto frontier 在两个架构上均 noisy（rho 接近零或 language-specific 方向不一致），无法做 clean architecture contrast', 'CaCLR 失败且 linear projection 在低/中资源语言不稳定（high variance across random seeds / pair selection）', 'CKA partial correlation 控制 depth 后完全 n.s.——深度是唯一预测因子', 'Control task 揭示 >30% 的 lang-layer 组合是 capacity artifacts，低资源语言几乎全部受影响', 'Decomposition effect 被 noise dominate，无法区分 difficulty vs capability', 'Orthogonality 在部分语言 cosine > 0.15，不再 universal']\n关键指标范围：{'en_probe_auroc': [0.72, 0.78], 'zs_transfer_auroc_avg_20lang': [0.56, 0.63], 'zs_transfer_success_rate': [0.5, 0.7], 'pareto_spearman_rho_strong_arch': [-0.35, -0.1], 'pareto_spearman_rho_weak_arch': [-0.15, 0.1], 'caclr_delta_auroc_vs_zeroshot': [-0.01, 0.005], 'caclr_delta_ece_vs_tempscaling': [-0.005, 0.02], 'linear_proj_50pairs_delta_auroc': [0.0, 0.03], 'cka_partial_corr_controlling_depth': [-0.05, 0.12], 'cka_partial_corr_p': [0.25, 0.8], 'selectivity_below_005_fraction': [0.3, 0.5], 'orthogonality_cosine_range': [0.03, 0.2], 'difficulty_projection_transfer_delta': [-0.01, 0.015]}\n叙事方向：核心 reframe：从 'cross-lingual calibration method' 转为 'cross-lingual probing viability boundary + methodological warning'。贡献重构：(1) 首个系统性压力测试证明 probe-based calibration 仅在 high-resource 语言 + 特定架构上可行——为领域划定 viability boundary；(2) Control task 分析揭示跨语言 probing 的 capacity artifact 问题（~35% false positive rate），这是对 Hewitt & Liang 框架在多语言场景下的重要扩展；(3) 方法论框架（control tasks + CKA + Pareto analysis）供后续工作评估跨语言 probing 可信度。Headline: 'Stress-testing probe-based calibration beyond English: viability boundaries, capacity artifacts, and when cross-lingual transfer breaks down.' 目标 venue 不降级（EACL）——methodological contribution + negative results + viability characterization 对该 venue 足够，但需增加 discussion section 篇幅，并可能需要补充 few-shot escalation 实验作为 constructive path forward。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff varies across architectures (strong on Qwen, weak on Llama); CKA geometric analysis (not mechanistic explanation — correlational, must control for depth) suggests architecture-specific representation divergence rates as a factor. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. A methodological warning: control task analysis reveals that ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold), challenging uncritical use of cross-lingual probing. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis (framed as correlational, NOT mechanistic) provides two levels of insight: (a) between-language: languages with higher CKA show less transfer degradation; (b) between-architecture: CKA cliff steepness differs. **MUST report partial correlation controlling for normalized depth** — if CKA adds no explanatory power beyond depth, downgrade to \"suggestive correlational analysis.\" Subspace angle analysis (quantitative, not just prose) strengthens geometric narrative.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame CKA analysis as geometric/correlational, not mechanistic. We report partial correlation controlling for depth to test whether CKA adds explanatory power beyond the trivial \"deeper = worse transfer.\" If partial correlation is weak, we explicitly state CKA is suggestive only.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique.'\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- exp_id: plan_013_probing_controls_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:55:53.712Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:55:53.712Z",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-21T03:55:53.744Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：大模型上 Pareto 信号噪声大、CaCLR 和 linear projection 均不稳定、CKA 无解释力、大面积 capacity artifacts 侵蚀低资源结果；需重构为 cross-lingual probing 方法论批判 + viability boundary 刻画
核心假设：['大模型（235B MoE / Scout MoE）的 correctness signal 比 7B dense 更分散，probe AUROC 提升有限或 noisy', 'Pareto frontier 在两个架构上均 noisy（rho 接近零或 language-specific 方向不一致），无法做 clean architecture contrast', 'CaCLR 失败且 linear projection 在低/中资源语言不稳定（high variance across random seeds / pair selection）', 'CKA partial correlation 控制 depth 后完全 n.s.——深度是唯一预测因子', 'Control task 揭示 >30% 的 lang-layer 组合是 capacity artifacts，低资源语言几乎全部受影响', 'Decomposition effect 被 noise dominate，无法区分 difficulty vs capability', 'Orthogonality 在部分语言 cosine > 0.15，不再 universal']
关键指标范围：{'en_probe_auroc': [0.72, 0.78], 'zs_transfer_auroc_avg_20lang': [0.56, 0.63], 'zs_transfer_success_rate': [0.5, 0.7], 'pareto_spearman_rho_strong_arch': [-0.35, -0.1], 'pareto_spearman_rho_weak_arch': [-0.15, 0.1], 'caclr_delta_auroc_vs_zeroshot': [-0.01, 0.005], 'caclr_delta_ece_vs_tempscaling': [-0.005, 0.02], 'linear_proj_50pairs_delta_auroc': [0.0, 0.03], 'cka_partial_corr_controlling_depth': [-0.05, 0.12], 'cka_partial_corr_p': [0.25, 0.8], 'selectivity_below_005_fraction': [0.3, 0.5], 'orthogonality_cosine_range': [0.03, 0.2], 'difficulty_projection_transfer_delta': [-0.01, 0.015]}
叙事方向：核心 reframe：从 'cross-lingual calibration method' 转为 'cross-lingual probing viability boundary + methodological warning'。贡献重构：(1) 首个系统性压力测试证明 probe-based calibration 仅在 high-resource 语言 + 特定架构上可行——为领域划定 viability boundary；(2) Control task 分析揭示跨语言 probing 的 capacity artifact 问题（~35% false positive rate），这是对 Hewitt & Liang 框架在多语言场景下的重要扩展；(3) 方法论框架（control tasks + CKA + Pareto analysis）供后续工作评估跨语言 probing 可信度。Headline: 'Stress-testing probe-based calibration beyond English: viability boundaries, capacity artifacts, and when cross-lingual transfer breaks down.' 目标 venue 不降级（EACL）——methodological contribution + negative results + viability characterization 对该 venue 足够，但需增加 discussion section 篇幅，并可能需要补充 few-shot escalation 实验作为 constructive path forward。

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
  "promptId": "998a9047-c25b-4221-8380-998e229f9418",
  "type": "user",
  "uuid": "5fd76cfe-0c9e-4d80-958d-a23d7dec8927",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:55:53.743Z_

```json
{
  "parentUuid": "5fd76cfe-0c9e-4d80-958d-a23d7dec8927",
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
  "uuid": "ae8fe267-7ae6-4890-a073-673872ddddb0",
  "timestamp": "2026-05-21T03:55:53.743Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:55:53.743Z_

```json
{
  "parentUuid": "ae8fe267-7ae6-4890-a073-673872ddddb0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "28d89cde-dc0f-4f5c-ae75-baae0329eb89",
  "timestamp": "2026-05-21T03:55:53.743Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：大模型上 Pareto 信号噪声大、CaCLR 和 linear projection 均不稳定、CKA 无解释力、大面积 capacity artifacts 侵蚀低资源结果；需重构为 cross-lingual probing 方法论批判 + viability boundary 刻画 核心假设：['大…",
  "leafUuid": "28d89cde-dc0f-4f5c-ae75-baae0329eb89",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Stress-testing probe-based calibration across languages",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a"
}
```

---

### Assistant

_source line 8 · 2026-05-21T03:55:57.543Z_

I'll analyze the experiment plan and generate detailed worst-tier predictions. Let me first review the full project context to ensure accuracy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28d89cde-dc0f-4f5c-ae75-baae0329eb89",
  "isSidechain": false,
  "requestId": "req_011CbF3HgeSjWxw29P6Sx9ie",
  "type": "assistant",
  "uuid": "8d1852eb-7ecc-4bc2-bc3b-17fd992c8d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136n3cqABPWUMZTFKYUzJ37",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16832,
      "cache_read_input_tokens": 11841,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 213,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16832
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

_source line 9 · 2026-05-21T03:56:01.657Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DJVfHaj2ovM5VJDsEDyGwH`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore project structure and key files",
  "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0519_2 for any additional context files. I need to find:\n1. Any files related to experiment plans, results, or analysis\n2. Any YAML/JSON config files\n3. Any existing prediction or tier files\n4. The memory directory contents\n\nSearch breadth: medium. List all relevant files found with their paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d1852eb-7ecc-4bc2-bc3b-17fd992c8d30",
  "isSidechain": false,
  "requestId": "req_011CbF3HgeSjWxw29P6Sx9ie",
  "type": "assistant",
  "uuid": "43a0fc04-6d3a-4144-bdb0-5a729c4a73be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136n3cqABPWUMZTFKYUzJ37",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16832,
      "cache_read_input_tokens": 11841,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 213,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16832
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

_source line 10 · 2026-05-21T03:56:53.860Z_

<details><summary>↩ Tool result · `toolu_01DJVfHaj2ovM5VJDsEDyGwH`</summary>

```text
Perfect! Now let me compile a comprehensive summary of all the context files found.

## Summary of Context Files Found

I've completed a comprehensive search of the project at `/home/ubuntu/.agent-ml-research-idea_gen_0519_2`. Here are all relevant files organized by category:

### 1. **Experiment Plans & Results**

**Core Plan Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml` - Full experimental roadmap with 13+ experiments (P0/P1/P2 priority tiers)
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml` - Experiment execution registry with MVP results (mvp_001: 2/4 PASS, mvp_002: PARTIAL, mvp_003: 2/4 PASS, plan_013: DONE)

**Key Findings:**
- MVPs completed with cross-lingual correctness transfer confirmed (4/5 languages @ AUROC ≥0.58)
- Plan_013 (probing controls) validates genuine signal vs spurious correlations
- CKA pilot shows architecture-dependent Pareto tradeoff (Qwen strong/Llama weak)

### 2. **Decision & Analysis Logs**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml` - 11 decisions logged (D001-D011):
  - D004: MVP gate 3/4 PASS → research phase approved
  - D006: Re-evaluation after temp scaling leakage fix → 2/4 PASS (still proceed)
  - D009: Re-dream processed (4/3/3 scores) with 6 action items integrated
  - D011: Parallel download strategy approved (Llama4 66GB + Qwen3 122GB both fit)

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/mistakes.yaml` - 9 critical issues logged:
  - M005: Temperature scaling data leakage (P1 ECE false positive)
  - M007: CaCLR MMD gradient disconnection (β parameter inert)
  - M006: Code fix deployment not verified
  - M001-M004: Layer list synchronization bugs

### 3. **Strategic Roadmaps & Memory**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md` (9.6 KB) - Current research dashboard in Chinese:
  - Research phase active (MVP complete, Dream approved conditional on code fixes)
  - Model downloads in progress: Llama4 (44GB/66GB), Qwen3 (38GB/122GB)
  - P1 controls (plan_011/012/013) running in parallel
  - Key finding: Pareto tradeoff Qwen strong/Llama weak; mean-shift rank-invariance

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md` - Current state snapshot:
  - plan_001.sh deployed to westd-13176 server
  - Pipeline: Qwen3-235B → extract 20 langs × 24 layers → transfer eval (5 methods)
  - Key design decisions documented (quantization, split ratio, symlink strategy)

### 4. **Configuration Files**

**YAML Configs:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/projects/xling_calib_direction.yaml` - Project configuration
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/backend.yaml` - Backend setup
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/approvals.yaml` - Approval workflow
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/venue_registry.yaml` - Conference venue rules
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/resources.yaml` - Resource allocation
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/dream_registry.yaml` - Dream review metadata

**JSON Configs:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/session_state.json` - Session state tracking
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/pool.json` - Worker pool configuration
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/claude_sessions.json` - Active sessions
- Multiple `mcp_config_*.json` files for worker/director/reviewer MCP configuration

### 5. **Dream Review Artifacts**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/` - Complete dream review package:
  - Scores: best=4/6 (Weak Accept), median=3/6 (Weak Reject), worst=3/6
  - Review reports, paper LaTeX, PDF, experiment_data.json with imagined results
  - Three reviewer tiers (best/median/worst) with distinct critiques

### 6. **Idea Generator & Approval**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/idea_generator/ideas.yaml` - Idea_032 (APPROVED):
  - Core problem: 5x ECE gap for non-English languages
  - Approach: Pareto frontier characterization + CaCLR + difficulty decomposition
  - 4 contributions: Frontier, CaCLR method, decomposition, orthogonality diagnostics
  - EACL 2027 ARR deadline: August 3, 2026 (10.5 weeks)

### 7. **Experiment Analysis & Reports**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md` - Handover summary (150 line limit):
  - 4 successful experiments (mvp_001, mvp_002, mvp_003, plan_013)
  - No failures or running experiments
  - Trend: 4 success / 0 negative / 0 failed

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/_project/report/cka_vs_degradation_report.md`:
  - CKA-degradation correlation analysis (Llama rho=-0.52 p=0.001)
  - Per-language CKA/degradation comparison table
  - Cross-model differences documented

### 8. **Project Documentation**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/AGENTS.md` - Agent overview (355 bytes)
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/AGENTS.md` - Project agent roles and responsibilities (13.6 KB)
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/IDEA_BRIEF.md` - Idea brief documentation
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md` - Paper narrative and claims framework
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml` - Literature reference organization (6.9 KB)

### 9. **Logs & Event Tracking**

**Worker Logs (90+ files):**
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/logs/workers/` - 90+ worker result JSON files
  - Tasks: code fixes, ops (downloads/disk/GPU), data preparation, analysis
  - Recent: plan_002 script run, plan_001 symlink fix, download verification

**Chat & Session Logs:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/logs/chats/` - 30+ chat session logs (JSONL)
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/logs/ralph_loop_timeline.jsonl` - Agent event timeline
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/global/logs/` - Global logs (session_events, skill_usage, manager_api, registry_audit)

### 10. **Distilled Research Papers**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/` - 12 distilled paper YAMLs:
  - karandikar2021sbece.yaml, joshi2025calibration.yaml, ravisankar2026dali.yaml (and 9 others)
  - Structured metadata on calibration, cross-lingual transfer, representation analysis

### 11. **Checkpoints & Artifacts**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/checkpoints/` - Model checkpoint directory
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/` - Output directory with dream reports and analysis docs
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/` - Implementation scripts

### 12. **State & Lock Files**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/state/pool_state_last.json` - Worker pool utilization (3 accounts: 18%, 10%, 13% five-hour utilization)
- Lock files: ROADMAP.lock, decisions.lock, registry.lock, study_status.lock
- Backup file: dream_registry.yaml.bak

### 13. **Other Context**

- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/CLAUDE.md` - Project-level system prompt (extensive, with 30+ embedded skills documentation)
- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/workspace.yaml` - Workspace configuration

**No prediction/tier files found** - The project uses YAML-based decision/registry files rather than separate tier/ranking predictions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43a0fc04-6d3a-4144-bdb0-5a729c4a73be",
  "isSidechain": false,
  "promptId": "998a9047-c25b-4221-8380-998e229f9418",
  "type": "user",
  "uuid": "01c9b4cc-d416-436a-b4e6-b080dfccea3b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0519_2 for any additional context files. I need to find:\n1. Any files related to experiment plans, results, or analysis\n2. Any YAML/JSON config files\n3. Any existing prediction or tier files\n4. The memory directory contents\n\nSearch breadth: medium. List all relevant files found with their paths.",
    "agentId": "a1e7dc86025d149a3",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me compile a comprehensive summary of all the context files found.\n\n## Summary of Context Files Found\n\nI've completed a comprehensive search of the project at `/home/ubuntu/.agent-ml-research-idea_gen_0519_2`. Here are all relevant files organized by category:\n\n### 1. **Experiment Plans & Results**\n\n**Core Plan Files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml` - Full experimental roadmap with 13+ experiments (P0/P1/P2 priority tiers)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/registry.yaml` - Experiment execution registry with MVP results (mvp_001: 2/4 PASS, mvp_002: PARTIAL, mvp_003: 2/4 PASS, plan_013: DONE)\n\n**Key Findings:**\n- MVPs completed with cross-lingual correctness transfer confirmed (4/5 languages @ AUROC ≥0.58)\n- Plan_013 (probing controls) validates genuine signal vs spurious correlations\n- CKA pilot shows architecture-dependent Pareto tradeoff (Qwen strong/Llama weak)\n\n### 2. **Decision & Analysis Logs**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml` - 11 decisions logged (D001-D011):\n  - D004: MVP gate 3/4 PASS → research phase approved\n  - D006: Re-evaluation after temp scaling leakage fix → 2/4 PASS (still proceed)\n  - D009: Re-dream processed (4/3/3 scores) with 6 action items integrated\n  - D011: Parallel download strategy approved (Llama4 66GB + Qwen3 122GB both fit)\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/mistakes.yaml` - 9 critical issues logged:\n  - M005: Temperature scaling data leakage (P1 ECE false positive)\n  - M007: CaCLR MMD gradient disconnection (β parameter inert)\n  - M006: Code fix deployment not verified\n  - M001-M004: Layer list synchronization bugs\n\n### 3. **Strategic Roadmaps & Memory**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md` (9.6 KB) - Current research dashboard in Chinese:\n  - Research phase active (MVP complete, Dream approved conditional on code fixes)\n  - Model downloads in progress: Llama4 (44GB/66GB), Qwen3 (38GB/122GB)\n  - P1 controls (plan_011/012/013) running in parallel\n  - Key finding: Pareto tradeoff Qwen strong/Llama weak; mean-shift rank-invariance\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md` - Current state snapshot:\n  - plan_001.sh deployed to westd-13176 server\n  - Pipeline: Qwen3-235B → extract 20 langs × 24 layers → transfer eval (5 methods)\n  - Key design decisions documented (quantization, split ratio, symlink strategy)\n\n### 4. **Configuration Files**\n\n**YAML Configs:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/projects/xling_calib_direction.yaml` - Project configuration\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/backend.yaml` - Backend setup\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/approvals.yaml` - Approval workflow\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/venue_registry.yaml` - Conference venue rules\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/resources.yaml` - Resource allocation\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/dream_registry.yaml` - Dream review metadata\n\n**JSON Configs:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/session_state.json` - Session state tracking\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/pool.json` - Worker pool configuration\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/config/claude_sessions.json` - Active sessions\n- Multiple `mcp_config_*.json` files for worker/director/reviewer MCP configuration\n\n### 5. **Dream Review Artifacts**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/` - Complete dream review package:\n  - Scores: best=4/6 (Weak Accept), median=3/6 (Weak Reject), worst=3/6\n  - Review reports, paper LaTeX, PDF, experiment_data.json with imagined results\n  - Three reviewer tiers (best/median/worst) with distinct critiques\n\n### 6. **Idea Generator & Approval**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/idea_generator/ideas.yaml` - Idea_032 (APPROVED):\n  - Core problem: 5x ECE gap for non-English languages\n  - Approach: Pareto frontier characterization + CaCLR + difficulty decomposition\n  - 4 contributions: Frontier, CaCLR method, decomposition, orthogonality diagnostics\n  - EACL 2027 ARR deadline: August 3, 2026 (10.5 weeks)\n\n### 7. **Experiment Analysis & Reports**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md` - Handover summary (150 line limit):\n  - 4 successful experiments (mvp_001, mvp_002, mvp_003, plan_013)\n  - No failures or running experiments\n  - Trend: 4 success / 0 negative / 0 failed\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/_project/report/cka_vs_degradation_report.md`:\n  - CKA-degradation correlation analysis (Llama rho=-0.52 p=0.001)\n  - Per-language CKA/degradation comparison table\n  - Cross-model differences documented\n\n### 8. **Project Documentation**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/AGENTS.md` - Agent overview (355 bytes)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/AGENTS.md` - Project agent roles and responsibilities (13.6 KB)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/IDEA_BRIEF.md` - Idea brief documentation\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md` - Paper narrative and claims framework\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml` - Literature reference organization (6.9 KB)\n\n### 9. **Logs & Event Tracking**\n\n**Worker Logs (90+ files):**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/logs/workers/` - 90+ worker result JSON files\n  - Tasks: code fixes, ops (downloads/disk/GPU), data preparation, analysis\n  - Recent: plan_002 script run, plan_001 symlink fix, download verification\n\n**Chat & Session Logs:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/logs/chats/` - 30+ chat session logs (JSONL)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/logs/ralph_loop_timeline.jsonl` - Agent event timeline\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/global/logs/` - Global logs (session_events, skill_usage, manager_api, registry_audit)\n\n### 10. **Distilled Research Papers**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/distill_tmp/` - 12 distilled paper YAMLs:\n  - karandikar2021sbece.yaml, joshi2025calibration.yaml, ravisankar2026dali.yaml (and 9 others)\n  - Structured metadata on calibration, cross-lingual transfer, representation analysis\n\n### 11. **Checkpoints & Artifacts**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/checkpoints/` - Model checkpoint directory\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/` - Output directory with dream reports and analysis docs\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/` - Implementation scripts\n\n### 12. **State & Lock Files**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/state/pool_state_last.json` - Worker pool utilization (3 accounts: 18%, 10%, 13% five-hour utilization)\n- Lock files: ROADMAP.lock, decisions.lock, registry.lock, study_status.lock\n- Backup file: dream_registry.yaml.bak\n\n### 13. **Other Context**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/.claude/CLAUDE.md` - Project-level system prompt (extensive, with 30+ embedded skills documentation)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/workspace.yaml` - Workspace configuration\n\n**No prediction/tier files found** - The project uses YAML-based decision/registry files rather than separate tier/ranking predictions."
      }
    ],
    "totalDurationMs": 52196,
    "totalTokens": 72576,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 68724,
      "output_tokens": 2696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1151
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2696,
          "cache_read_input_tokens": 68724,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1151,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 11,
      "searchCount": 0,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "43a0fc04-6d3a-4144-bdb0-5a729c4a73be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T03:57:06.462Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SduZQqSWVBPwqsp2TZN1gm`</summary>

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
  "parentUuid": "01c9b4cc-d416-436a-b4e6-b080dfccea3b",
  "isSidechain": false,
  "requestId": "req_011CbF3N7bEof5vybt6UZvvs",
  "type": "assistant",
  "uuid": "9c9a058e-ba4c-49b0-a921-8353553be1dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9h2daQeb4rceQdQZqFXMu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 28673,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 28673,
          "cache_creation_input_tokens": 2917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2917
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

_source line 12 · 2026-05-21T03:57:06.473Z_

<details><summary>↩ Tool result · `toolu_01SduZQqSWVBPwqsp2TZN1gm`</summary>

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
  "parentUuid": "9c9a058e-ba4c-49b0-a921-8353553be1dc",
  "isSidechain": false,
  "promptId": "998a9047-c25b-4221-8380-998e229f9418",
  "type": "user",
  "uuid": "d06686aa-a17c-4944-b0e2-6c3460c63b23",
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
  "sourceToolAssistantUUID": "9c9a058e-ba4c-49b0-a921-8353553be1dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T03:57:07.749Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WGZipia3C8NwVPt5oACaGa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/experiment_data.json",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d06686aa-a17c-4944-b0e2-6c3460c63b23",
  "isSidechain": false,
  "requestId": "req_011CbF3N7bEof5vybt6UZvvs",
  "type": "assistant",
  "uuid": "74708d61-bc71-45fa-bf47-4fece3baf014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9h2daQeb4rceQdQZqFXMu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 28673,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 28673,
          "cache_creation_input_tokens": 2917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2917
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

_source line 14 · 2026-05-21T03:57:07.764Z_

<details><summary>↩ Tool result · reported error · `toolu_01WGZipia3C8NwVPt5oACaGa`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74708d61-bc71-45fa-bf47-4fece3baf014",
  "isSidechain": false,
  "promptId": "998a9047-c25b-4221-8380-998e229f9418",
  "type": "user",
  "uuid": "3f3bfd82-ec2e-4cc4-89e5-09c497c2f7e1",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519_2.",
  "sourceToolAssistantUUID": "74708d61-bc71-45fa-bf47-4fece3baf014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-21T03:57:07.785Z_

````json
{
  "parentUuid": "3f3bfd82-ec2e-4cc4-89e5-09c497c2f7e1",
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
  "uuid": "5a36021e-1204-4737-a765-bae95a0186e5",
  "timestamp": "2026-05-21T03:57:07.785Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：大模型上 Pareto 信号噪声大、CaCLR 和 linear projection 均不稳定、CKA 无解释力、大面积 capacity artifacts 侵蚀低资源结果；需重构为 cross-lingual probing 方法论批判 + viability boundary 刻画 核心假设：['大…",
  "leafUuid": "5a36021e-1204-4737-a765-bae95a0186e5",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Stress-testing probe-based calibration across languages",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a"
}
```

---

### Assistant

_source line 18 · 2026-05-21T03:57:27.177Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me construct the worst-tier predictions for each planned experiment. The key constraints from the worst tier definition are:

1. Large model probe AUROC noisy, limited improvement over 7B
2. Pareto frontier noisy on both architectures (rho near zero or inconsistent)
3. CaCLR fails AND linear projection unstable on low/mid-resource
4. CKA partial correlation n.s. after controlling depth
5. Control task reveals >30% capacity artifacts, low-resource almost all affected
6. Decomposition dominated by noise


7. Orthogonality cosine > 0.15 in some languages (not universal)

Now I'm mapping these constraints against the metric ranges I have for the experiments—the English probe AUROC should stay in the noisier band around 0.72-0.78, zero-shot transfer performance will be weak at 0.56-0.63 across languages, and the Pareto frontier correlations will be scattered with weak or negative Spearman rho values depending on architecture. Now I'm mapping out the full set of planned experiments across different model architectures and analysis approaches—covering Pareto frontier explorations for Qwen and Llama, specialized analyses for calibration, difficulty decomposition, orthogonality properties, and extending the control task validation across multiple languages and larger models. Let me generate the complete YAML configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a36021e-1204-4737-a765-bae95a0186e5",
  "isSidechain": false,
  "requestId": "req_011CbF3P92bFQQGAHduxiveZ",
  "type": "assistant",
  "uuid": "efdfcbb9-5656-49dc-b28a-65780d07acdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmVeoxGbPpAfdpSWNmyrpi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9539,
      "cache_read_input_tokens": 31590,
      "output_tokens": 21504,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21504,
          "cache_read_input_tokens": 31590,
          "cache_creation_input_tokens": 9539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9539
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

_source line 19 · 2026-05-21T04:03:51.678Z_

```yaml
tier: worst
narrative_guidance: >
  核心 reframe：从 'cross-lingual calibration method' 转为 'cross-lingual probing viability boundary + methodological warning'。
  Headline: 'Stress-testing probe-based calibration beyond English: viability boundaries, capacity artifacts, and when cross-lingual transfer breaks down.'
  大模型（235B MoE / Scout MoE）的 correctness signal 比 7B dense 更分散——MoE routing 将信息分散到更多 expert，导致 probe AUROC 提升有限且 noisy。
  Pareto frontier 在两个 MoE 架构上均 noisy（rho 接近零），无法支撑 clean architecture contrast。
  CaCLR 失败且 linear projection 在低/中资源语言不稳定。CKA partial correlation 控制 depth 后 n.s.。
  Control task 揭示 >30% 的 lang-layer 组合是 capacity artifacts，低资源语言几乎全部受影响。
  贡献重构为：(1) viability boundary 刻画；(2) capacity artifact 问题揭露（Hewitt & Liang 多语言扩展）；(3) 方法论框架。
  目标 venue 不降级（EACL）——需增加 discussion 篇幅，补充 few-shot escalation 实验作为 constructive path forward。

imagined_experiments:

  # ============================================================
  # plan_001: Qwen3-235B-A22B Full Pareto Frontier
  # ============================================================
  - name: "Qwen3-235B-A22B Full Pareto Frontier (20 langs × 24 layers × 5 transfer conditions)"
    plan_id: "plan_001"
    description: >
      在 Qwen3-235B-A22B（94 层 MoE, INT4）上提取每隔 4 层的激活（24 个 probed layers），
      20 种语言训练英语 correctness probes（LR + MLP），评估 5 种 transfer 条件。
      报告 per-language Spearman rho（depth vs transfer AUROC）和 global rho。
    expected_results:
      # English probe performance — 235B 比 7B 提升有限
      en_best_auroc: 0.76
      en_best_layer: "L72 (约 77% depth)"
      en_auroc_range: [0.58, 0.76]
      en_best_ece_raw: 0.175
      # Zero-shot transfer — 20 语言平均
      zs_transfer_auroc_avg_20lang: 0.59
      zs_transfer_auroc_high_resource_avg: 0.65  # zh/es/fr/de
      zs_transfer_auroc_mid_resource_avg: 0.59   # hi/ru/ko/tr
      zs_transfer_auroc_low_resource_avg: 0.53   # sw/bn + te/vi 等
      zs_transfer_success_rate_above_060: "11/20 (55%)"
      # Pareto frontier — 全局 noisy
      pareto_global_spearman_rho: -0.18
      pareto_global_spearman_p: 0.12
      pareto_per_lang_rho_median: -0.14
      pareto_per_lang_significant_count: "3/19 (zh, es, fr — 仅高资源)"
      pareto_per_lang_positive_rho_count: "6/19 (ar, ko, bn, sw, te, vi — 方向反转)"
      # Transfer conditions (at EN-optimal layer L72)
      mean_shift_delta_auroc_avg: 0.0  # rank-invariant, proven in MVP
      linear_proj_50pairs_delta_auroc_avg: 0.015
      linear_proj_50pairs_delta_auroc_high: 0.025
      linear_proj_50pairs_delta_auroc_low: -0.005
      fewshot_25_delta_auroc_avg: 0.035
      fewshot_100_delta_auroc_avg: 0.065
      # 稳定性
      linear_proj_std_across_seeds_low_resource: 0.028
      zs_auroc_std_across_layers_top10: 0.04
    result_rationale: >
      235B MoE 架构有 94 层但仅 22B 激活参数——expert routing 机制将 correctness 信息分散到不同 expert 子网络中，
      probe 在 shared representation 上只能捕获部分信号，因此 AUROC 相比 7B dense（0.754）提升极有限（→0.76）。
      MoE 的 expert 选择是 input-dependent 的，不同语言激活不同 expert 子集，导致跨语言激活空间异质性更高。
      这直接破坏了 Pareto frontier 的一致性：不同语言的 "最优 transfer 层" 受 expert routing pattern 影响而高度分散，
      global rho 被拉向零。高资源语言（zh/es/fr）与英语共享更多 expert 激活模式，仍显示弱 Pareto；
      低资源语言与英语 expert overlap 极低，transfer AUROC 在深层反而因 expert divergence 而改善（正 rho）。
      Linear projection 在低资源上不稳定，因为 50 parallel pairs 不足以学习 MoE 碎片化空间的旋转矩阵。
    tables:
      - title: "Table 1: Qwen3-235B Zero-Shot Transfer AUROC by Language (EN-optimal layer L72)"
        columns: [Language, Family, Resource_Tier, ZS_AUROC, "95% CI", "vs EN Δ"]
        rows:
          - [en, Germanic, source, 0.760, "[0.74, 0.78]", "—"]
          - [zh, Sinitic, HIGH, 0.672, "[0.65, 0.69]", -0.088]
          - [es, Romance, HIGH, 0.668, "[0.64, 0.69]", -0.092]
          - [fr, Romance, HIGH, 0.662, "[0.64, 0.68]", -0.098]
          - [de, Germanic, HIGH, 0.653, "[0.63, 0.68]", -0.107]
          - [ja, Japonic, MID, 0.631, "[0.60, 0.66]", -0.129]
          - [pt, Romance, MID, 0.624, "[0.60, 0.65]", -0.136]
          - [ru, Slavic, MID, 0.608, "[0.58, 0.64]", -0.152]
          - [ko, Koreanic, MID, 0.602, "[0.57, 0.63]", -0.158]
          - [nl, Germanic, MID, 0.598, "[0.57, 0.63]", -0.162]
          - [hi, Indo-Aryan, MID, 0.588, "[0.56, 0.62]", -0.172]
          - [pl, Slavic, MID, 0.582, "[0.55, 0.61]", -0.178]
          - [id, Austronesian, MID, 0.577, "[0.55, 0.61]", -0.183]
          - [tr, Turkic, MID, 0.571, "[0.54, 0.60]", -0.189]
          - [vi, Austroasiatic, MID, 0.563, "[0.53, 0.60]", -0.197]
          - [uk, Slavic, MID, 0.558, "[0.53, 0.59]", -0.202]
          - [ar, Semitic, MID, 0.555, "[0.52, 0.59]", -0.205]
          - [bn, Indo-Aryan, LOW, 0.538, "[0.50, 0.57]", -0.222]
          - [te, Dravidian, LOW, 0.521, "[0.49, 0.55]", -0.239]
          - [sw, Niger-Congo, LOW, 0.508, "[0.48, 0.54]", -0.252]
      - title: "Table 2: Qwen3-235B Pareto Spearman ρ (depth vs ZS AUROC) per Language"
        columns: [Language, Spearman_rho, p_value, Direction, Significant]
        rows:
          - [zh, -0.52, 0.009, expected, "✓"]
          - [es, -0.44, 0.031, expected, "✓"]
          - [fr, -0.41, 0.046, expected, "✓"]
          - [de, -0.33, 0.11, expected, "✗"]
          - [ja, -0.25, 0.24, expected, "✗"]
          - [ru, -0.18, 0.40, expected, "✗"]
          - [ko, -0.06, 0.79, flat, "✗"]
          - [hi, -0.03, 0.89, flat, "✗"]
          - [tr, 0.02, 0.93, flat, "✗"]
          - [id, -0.11, 0.61, expected, "✗"]
          - [pt, -0.28, 0.19, expected, "✗"]
          - [nl, -0.22, 0.30, expected, "✗"]
          - [pl, -0.08, 0.71, flat, "✗"]
          - [vi, 0.12, 0.58, reversed, "✗"]
          - [uk, -0.15, 0.48, expected, "✗"]
          - [ar, 0.09, 0.67, reversed, "✗"]
          - [bn, 0.18, 0.40, reversed, "✗"]
          - [te, 0.22, 0.30, reversed, "✗"]
          - [sw, 0.15, 0.48, reversed, "✗"]
          - [global, -0.18, 0.12, "—", "✗"]
    figures_description:
      - "Fig 1: 20-panel Pareto frontier heatmap (x=normalized depth, y=language sorted by resource tier), color=ZS AUROC。高资源区域呈现弱对角梯度（浅层 transfer 好→深层差），中/低资源区域为 noisy 棋盘格，无一致趋势。"
      - "Fig 2: Per-language Spearman rho bar chart with 95% bootstrap CI。3 条显著阈值线；大部分 CI 跨零。"
    analysis: >
      Qwen3-235B 的 Pareto frontier 远弱于 7B dense MVP 预期。Global rho=-0.18 不显著，
      仅 3/19 target 语言有显著负相关（均为高资源）。6/19 语言出现方向反转（正 rho），
      集中在低资源。MoE routing 的 input-dependent expert selection 使得不同语言在不同深度
      激活完全不同的子网络，破坏了 "更深=更好英语但更差 transfer" 的简单叙事。
      这意味着 Pareto frontier 在 MoE 架构上不是稳定的 architecture-level property，
      而是 language-specific 的。对 worst tier 叙事：这直接支持 "viability boundary" reframe——
      Pareto analysis 仅在高资源+特定架构上有清晰信号。

  # ============================================================
  # plan_002: Llama 4 Scout Full Pareto Frontier
  # ============================================================
  - name: "Llama 4 Scout Full Pareto Frontier (20 langs × 12 layers × 5 transfer conditions)"
    plan_id: "plan_002"
    description: >
      在 Llama 4 Scout（48 层 MoE, W4A16）上提取激活（12 probed layers），
      20 种语言，5 种 transfer 条件。报告 per-language Spearman rho。
    expected_results:
      en_best_auroc: 0.74
      en_best_layer: "L40 (约 83% depth)"
      en_auroc_range: [0.60, 0.74]
      en_best_ece_raw: 0.185
      zs_transfer_auroc_avg_20lang: 0.57
      zs_transfer_auroc_high_resource_avg: 0.63
      zs_transfer_auroc_mid_resource_avg: 0.57
      zs_transfer_auroc_low_resource_avg: 0.51
      zs_transfer_success_rate_above_060: "8/20 (40%)"
      pareto_global_spearman_rho: -0.05
      pareto_global_spearman_p: 0.62
      pareto_per_lang_rho_median: -0.02
      pareto_per_lang_significant_count: "1/19 (仅 zh)"
      pareto_per_lang_positive_rho_count: "8/19"
      mean_shift_delta_auroc_avg: 0.0
      linear_proj_50pairs_delta_auroc_avg: 0.008
      linear_proj_50pairs_delta_auroc_low: -0.01
      fewshot_25_delta_auroc_avg: 0.028
      fewshot_100_delta_auroc_avg: 0.055
      linear_proj_std_across_seeds_low_resource: 0.035
    result_rationale: >
      Llama 4 Scout 是 17B-16E MoE（272B total, 17B active），48 层比 Qwen3 的 94 层少得多，
      probed layers 仅 12 个，Spearman rho 的统计检验力极低（n=12 时需要 |rho|>0.58 才显著）。
      MVP 阶段 Llama-3.1-8B dense 已经是 weak Pareto（仅 2/5 显著），Scout MoE 继承了 Llama 家族
      的弱 depth-transfer tradeoff 特征（可能因为 Llama 训练数据中多语言比例高于 Qwen，
      导致深层 representation 已经部分语言对齐），加上 MoE routing 碎片化效应，
      global rho 被进一步推向零。W4A16 量化可能引入额外 noise（权重 4-bit 但激活 16-bit，
      correctness probe 依赖的微弱方向性信号可能在权重量化中丢失部分精度）。
      12 个 probed layers 的粗糙采样使得 per-language rho 高度不稳定，
      微小的 AUROC 波动就能翻转 rho 方向。
    tables:
      - title: "Table 3: Llama 4 Scout Zero-Shot Transfer AUROC (EN-optimal L40)"
        columns: [Language, Resource_Tier, ZS_AUROC, "95% CI"]
        rows:
          - [en, source, 0.740, "[0.72, 0.76]"]
          - [zh, HIGH, 0.648, "[0.62, 0.67]"]
          - [es, HIGH, 0.643, "[0.62, 0.67]"]
          - [fr, HIGH, 0.635, "[0.61, 0.66]"]
          - [de, HIGH, 0.628, "[0.60, 0.65]"]
          - [ja, MID, 0.601, "[0.57, 0.63]"]
          - [ru, MID, 0.588, "[0.56, 0.62]"]
          - [ko, MID, 0.583, "[0.55, 0.61]"]
          - [pt, MID, 0.595, "[0.57, 0.62]"]
          - [hi, MID, 0.568, "[0.54, 0.60]"]
          - [nl, MID, 0.575, "[0.54, 0.61]"]
          - [pl, MID, 0.562, "[0.53, 0.59]"]
          - [id, MID, 0.555, "[0.52, 0.59]"]
          - [tr, MID, 0.548, "[0.52, 0.58]"]
          - [vi, MID, 0.541, "[0.51, 0.57]"]
          - [uk, MID, 0.545, "[0.51, 0.58]"]
          - [ar, MID, 0.538, "[0.51, 0.57]"]
          - [bn, LOW, 0.518, "[0.49, 0.55]"]
          - [te, LOW, 0.505, "[0.47, 0.54]"]
          - [sw, LOW, 0.495, "[0.46, 0.53]"]
      - title: "Table 4: Llama 4 Scout Pareto ρ per Language"
        columns: [Language, Spearman_rho, p_value, Significant]
        rows:
          - [zh, -0.62, 0.031, "✓"]
          - [es, -0.38, 0.22, "✗"]
          - [fr, -0.29, 0.36, "✗"]
          - [de, -0.15, 0.64, "✗"]
          - [ja, -0.08, 0.80, "✗"]
          - [ru, 0.05, 0.88, "✗"]
          - [ko, 0.22, 0.49, "✗"]
          - [hi, 0.11, 0.73, "✗"]
          - [tr, 0.08, 0.80, "✗"]
          - [id, -0.03, 0.93, "✗"]
          - [pt, -0.18, 0.58, "✗"]
          - [nl, -0.12, 0.71, "✗"]
          - [pl, 0.15, 0.64, "✗"]
          - [vi, 0.25, 0.43, "✗"]
          - [uk, 0.03, 0.93, "✗"]
          - [ar, 0.18, 0.58, "✗"]
          - [bn, 0.28, 0.38, "✗"]
          - [te, 0.35, 0.26, "✗"]
          - [sw, 0.31, 0.33, "✗"]
          - [global, -0.05, 0.62, "✗"]
    figures_description:
      - "Fig 3: Llama 4 Scout Pareto heatmap——几乎全为 noise，仅 zh 一行可见微弱梯度。"
      - "Fig 4: 两架构 global rho 对比 bar chart（Qwen -0.18 vs Scout -0.05），两者 CI 均跨零。"
    analysis: >
      Scout 上 Pareto 完全崩溃——global rho=-0.05 (p=0.62)，仅 zh 显著。n=12 的采样密度
      使得统计检验力不足以检测中等效应。与 Qwen3 对比：两个 MoE 架构都无法支撑 "clean architecture contrast"，
      因为 rho 都不显著（Qwen -0.18 p=0.12, Scout -0.05 p=0.62）。MVP 阶段观察到的 Qwen(strong)/Llama(weak)
      对比在大模型上被 MoE noise 冲刷。这强化了 worst tier 叙事：Pareto frontier 作为分析工具
      仅在 7B dense + 高资源语言上有效——对 MoE 架构的泛化失败是方法论局限性的核心发现。

  # ============================================================
  # plan_003: CaCLR Implementation & Evaluation
  # ============================================================
  - name: "CaCLR Comparative Evaluation (2 models × 20 langs × Pareto frontier)"
    plan_id: "plan_003"
    description: >
      CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) 与 zero-shot/mean-shift/linear projection/few-shot
      在两个模型全 Pareto frontier 上的对比。α sweep (0.01-10.0), β sweep 3 OOM (0.001-1.0)。
    expected_results:
      # CaCLR vs zero-shot
      caclr_best_beta_auroc_delta_vs_zeroshot_avg: 0.002
      caclr_best_beta_auroc_delta_high_resource: 0.005
      caclr_best_beta_auroc_delta_low_resource: -0.008
      caclr_best_beta_auroc_delta_range: [-0.01, 0.005]
      # β sweep 结果
      beta_0001_delta_auroc: 0.001
      beta_001_delta_auroc: 0.002
      beta_01_delta_auroc: 0.001
      beta_1_delta_auroc: -0.003
      beta_sweep_variance_across_seeds: 0.006
      # ECE
      caclr_delta_ece_vs_tempscaling_avg: 0.008
      caclr_delta_ece_vs_tempscaling_range: [-0.005, 0.02]
      # Component ablation
      bce_only_auroc_delta: 0.0  # baseline
      bce_sbece_auroc_delta: 0.001
      bce_mmd_auroc_delta: 0.002
      bce_sbece_mmd_auroc_delta: 0.002
      # Linear projection comparison
      linear_proj_50pairs_delta_auroc_avg: 0.015
      linear_proj_50pairs_wins_over_caclr: "14/19 languages"
      # Few-shot comparison
      fewshot_25_delta_auroc_avg: 0.032
      fewshot_100_delta_auroc_avg: 0.061
      # α sensitivity
      alpha_optimal: 0.1
      alpha_sensitivity: "robust in [0.01, 1.0], degrades at α=10"
    result_rationale: >
      CaCLR 的 MMD consistency loss 在 1-D probe logit 空间上操作——这是根本性的设计缺陷。
      MMD 匹配的是 probe output 的边缘分布，但跨语言 correctness 失败的原因不是边缘分布不匹配，
      而是条件分布 P(correct|representation) 在不同语言上不同（Zhao et al. 2019 的核心结论）。
      在 MoE 架构上，不同语言激活不同 expert 子集，representation space 的拓扑结构完全不同——
      MMD 在低维投影空间上的匹配无法 capture 这种高维结构差异。
      β sweep 跨 3 OOM 但 delta AUROC 始终在 noise level（±0.005），因为 MMD loss
      的梯度信号太弱（1-D logit，bandwidth 由 median heuristic 决定，在接近正态的分布上
      几乎所有 bandwidth 都给出相似的 gradient）。低资源语言上 CaCLR 甚至略微 hurt（-0.008），
      因为 MMD penalty 迫使 probe 偏离英语最优解但又无法真正对齐目标语言。
      Linear projection（50 pairs）在 14/19 语言上赢过 CaCLR，因为它直接学习子空间旋转
      而不是间接匹配分布。但 linear projection 本身在低资源上不稳定（seed variance 高）。
    tables:
      - title: "Table 5: Transfer Method Comparison — Δ AUROC vs Zero-Shot (Qwen3-235B, EN-optimal layer)"
        columns: [Method, HIGH_avg, MID_avg, LOW_avg, ALL_avg, "Wins/19"]
        rows:
          - [Mean-shift, 0.000, 0.000, 0.000, 0.000, "0/19"]
          - [CaCLR (best β), +0.005, +0.003, -0.008, +0.002, "8/19"]
          - [Linear proj (50), +0.025, +0.015, -0.005, +0.015, "14/19"]
          - [Few-shot (25), +0.038, +0.030, +0.022, +0.032, "17/19"]
          - [Few-shot (100), +0.072, +0.058, +0.045, +0.061, "19/19"]
      - title: "Table 6: CaCLR β Sweep (avg Δ AUROC across 20 langs, Qwen3-235B)"
        columns: [β, Δ_AUROC_mean, Δ_AUROC_std, Δ_ECE_mean, "p (vs ZS)"]
        rows:
          - [0.001, +0.001, 0.006, +0.003, 0.72]
          - [0.01, +0.002, 0.007, +0.005, 0.58]
          - [0.1, +0.001, 0.008, +0.008, 0.63]
          - [1.0, -0.003, 0.011, +0.012, 0.41]
          - ["0 (BCE only)", 0.000, 0.005, +0.001, "—"]
      - title: "Table 7: CaCLR Component Ablation (Qwen3-235B, avg 20 langs)"
        columns: [Components, Δ_AUROC, Δ_ECE, Note]
        rows:
          - [BCE only, 0.000, +0.001, "baseline (= zero-shot retrain)"]
          - [BCE + SB-ECE, +0.001, -0.002, "α=0.1; ECE marginally better"]
          - [BCE + MMD, +0.002, +0.004, "β=0.01; MMD alone slightly helps AUROC but hurts ECE"]
          - [BCE + SB-ECE + MMD, +0.002, +0.006, "joint ≈ max of components, no synergy"]
    figures_description:
      - "Fig 5: β sweep curve (x=log β, y=Δ AUROC) with 95% CI——flat line 在零附近，所有 CI 跨零。"
      - "Fig 6: 5-method transfer comparison grouped bar chart (high/mid/low resource)——CaCLR 与 zero-shot 不可区分，linear projection 和 few-shot 逐步改善。"
      - "Fig 7: Per-language CaCLR Δ AUROC scatter (x=resource tier proxy, y=delta)——低资源侧系统性偏负。"
    analysis: >
      CaCLR 的 consistency loss 完全 inert。β sweep 跨 3 个数量级（0.001→1.0），
      平均 Δ AUROC 从未超过 noise level（+0.002 ± 0.007）。配对置换检验 p 值全部 >0.4。
      Component ablation 确认：SB-ECE 提供微弱 ECE 改善（-0.002），MMD 提供微弱 AUROC 改善（+0.002），
      但两者无协同效应，且均在 noise 范围内。核心 negative result：MMD-based distributional matching
      对 correctness probe transfer 无效——与 Zhao et al. (2019) 理论预测一致（边缘匹配在条件分布不同时失效）。
      Linear projection（50 pairs）作为最强 zero-label 替代方案，但在低资源语言上也不稳定。
      Few-shot 25/100 是唯一 consistently 有效的路径——支持 "constructive path forward" 叙事。

  # ============================================================
  # plan_004: Difficulty-Controlled Decomposition
  # ============================================================
  - name: "Difficulty-Controlled Decomposition Ablation (10 langs × 8 layers × 2 models)"
    plan_id: "plan_004"
    description: >
      训练 IRT difficulty probes，投影出 difficulty direction，在 residuals 上重训 correctness probes，
      评估 transfer。10 种代表性语言 × 8 层 × 2 模型。含 random-direction control。
    expected_results:
      # Difficulty probe quality
      difficulty_probe_r2_en_avg: 0.35
      difficulty_probe_r2_range: [0.18, 0.48]
      # Projection effect on English AUROC
      en_auroc_after_projection_avg_delta: -0.025
      # Projection effect on transfer
      difficulty_projection_transfer_delta_high_resource: 0.012
      difficulty_projection_transfer_delta_mid_resource: 0.003
      difficulty_projection_transfer_delta_low_resource: -0.008
      difficulty_projection_transfer_delta_avg: 0.005
      difficulty_projection_transfer_delta_range: [-0.01, 0.015]
      # Random direction control
      random_projection_transfer_delta_avg: -0.015
      random_vs_difficulty_significant: "4/10 languages (all high-resource)"
      # Decomposition interpretability
      difficulty_shared_fraction_estimate: "0.20-0.55 range across langs, no consistent pattern"
      capability_specific_fraction_variance: "high (std=0.18 across languages)"
    result_rationale: >
      Decomposition 在 worst tier 下被 noise dominate，原因有三：
      (1) IRT difficulty scores 本身 noisy（GlobalMMLU 的 difficulty 基于 human performance，
      与 LLM-perceived difficulty 仅中等相关，r²~0.35）；
      (2) MoE 架构中 difficulty direction 不是一条 clean linear direction——不同 expert 
      以不同方式 encode difficulty，Ridge regression 只能捕获 average effect；
      (3) 投影出 difficulty 后的 residual space 维度仍然很高（4096-D），correctness probe 
      在 residuals 上重训的 noise floor 与原始空间接近。
      结果：projecting out difficulty 对 transfer 的平均效果极小（+0.005），
      且高度 language-dependent。高资源语言略有改善（+0.012，因为 difficulty 确实是 shared component），
      低资源语言反而变差（-0.008，因为 difficulty probe 本身在低资源上就不准确，
      投影出的实际上是 noise direction）。Random-direction control 确认投影本身
      会降低信号（-0.015），difficulty projection 只是 "比 random 好一点"，
      但差异仅在 4/10 语言上显著——无法支撑 "decomposition is prescriptive" 的强 claim。
    tables:
      - title: "Table 8: Difficulty Decomposition — Transfer Δ AUROC (vs no-projection baseline)"
        columns: [Language, Tier, Difficulty_proj_Δ, Random_proj_Δ, "Diff-Rand gap", p_value]
        rows:
          - [zh, HIGH, +0.015, -0.012, 0.027, 0.031]
          - [es, HIGH, +0.013, -0.014, 0.027, 0.028]
          - [fr, HIGH, +0.011, -0.016, 0.027, 0.035]
          - [de, HIGH, +0.008, -0.013, 0.021, 0.062]
          - [hi, MID, +0.005, -0.015, 0.020, 0.088]
          - [ru, MID, +0.003, -0.018, 0.021, 0.075]
          - [ko, MID, +0.002, -0.014, 0.016, 0.145]
          - [tr, MID, +0.001, -0.017, 0.018, 0.118]
          - [sw, LOW, -0.005, -0.019, 0.014, 0.212]
          - [bn, LOW, -0.010, -0.016, 0.006, 0.481]
    figures_description:
      - "Fig 8: Decomposition effect scatter (x=resource tier, y=Δ transfer AUROC) with difficulty vs random overlay——两条线接近，difficulty 仅略高。"
    analysis: >
      Decomposition 效果被 noise dominate。平均 +0.005 transfer delta 远小于 few-shot 25 的 +0.032。
      "Difficulty-shared vs capability-specific" 分解的 fraction 估计高度不稳定（std=0.18），
      无法形成 consistent 叙事。对 worst tier：Claim 2 需要大幅弱化——从 "prescriptive decomposition"
      降为 "exploratory decomposition suggests difficulty component exists but is not cleanly separable
      in MoE architectures"。仍有方法论价值（展示了 how to decompose），但不是 strong empirical finding。

  # ============================================================
  # plan_005: Cross-Lingual Orthogonality
  # ============================================================
  - name: "Cross-Lingual Orthogonality Analysis (20 langs × 2 architectures)"
    plan_id: "plan_005"
    description: >
      提取 verbalized confidence direction，计算与 correctness direction 的 cosine similarity，
      20 种语言 × 2 架构。按 resource tier 和 language family 分析。
    expected_results:
      # Cosine similarity statistics
      cosine_median_all: 0.06
      cosine_range: [0.02, 0.18]
      cosine_below_004_fraction: "7/40 (17.5%)"
      cosine_above_010_fraction: "12/40 (30%)"
      cosine_above_015_fraction: "6/40 (15%)"
      # By resource tier
      cosine_high_resource_mean: 0.04
      cosine_mid_resource_mean: 0.07
      cosine_low_resource_mean: 0.13
      # By architecture
      cosine_qwen_mean: 0.07
      cosine_scout_mean: 0.08
      # Outliers
      worst_lang_cosine: "sw@Scout: 0.18"
      worst_cases_above_015: ["sw@Scout", "bn@Scout", "te@Qwen", "sw@Qwen", "bn@Qwen", "te@Scout"]
    result_rationale: >
      Miao & Ungar (2026) 在英语 7-8B 上报告 cosine<0.04（近乎正交）。
      在大模型 MoE + 多语言设置下正交性部分退化，原因：
      (1) MoE expert 内部空间维度有效降低——当 correctness 和 confidence 信号都被 route 到
      少量共享 expert 时，方向会更 "拥挤"，cosine 从零偏移；
      (2) 低资源语言的 confidence direction 本身就 noisy（模型在低资源上的 verbalized confidence
      更随机，probe 拟合的方向不稳定），noise 方向与 correctness 的 cosine 期望值 ~1/√d
      而非精确零；
      (3) 部分低资源语言（sw, bn, te）可能存在 capacity artifact——probe 学到的不是真正的
      correctness/confidence 方向而是 dataset regularities，这两种 artifact 方向可能有非零相关。
      高资源语言维持 cosine~0.04，但 15% 的 lang×arch 组合 cosine>0.15，
      "universally orthogonal" 的表述不再成立。
    tables:
      - title: "Table 9: Correctness-Confidence Cosine Similarity (selected languages × 2 architectures)"
        columns: [Language, Tier, Qwen3_cosine, Scout_cosine, Avg]
        rows:
          - [en, source, 0.03, 0.03, 0.03]
          - [zh, HIGH, 0.04, 0.03, 0.035]
          - [es, HIGH, 0.03, 0.04, 0.035]
          - [fr, HIGH, 0.04, 0.05, 0.045]
          - [de, HIGH, 0.04, 0.04, 0.04]
          - [ja, MID, 0.05, 0.06, 0.055]
          - [ru, MID, 0.05, 0.06, 0.055]
          - [ko, MID, 0.06, 0.07, 0.065]
          - [hi, MID, 0.07, 0.08, 0.075]
          - [tr, MID, 0.08, 0.09, 0.085]
          - [ar, MID, 0.06, 0.07, 0.065]
          - [bn, LOW, 0.12, 0.14, 0.13]
          - [te, LOW, 0.15, 0.13, 0.14]
          - [sw, LOW, 0.14, 0.18, 0.16]
    figures_description:
      - "Fig 9: Cosine similarity heatmap (lang × arch)——高资源区域冷色（<0.05），低资源区域暖色（>0.10），清晰的 resource-tier gradient。"
      - "Fig 10: Cosine vs resource tier scatter with regression line——正相关，r=-0.65（resource level 越低 cosine 越高）。"
    analysis: >
      Orthogonality 在高资源语言上 robustly holds（cosine<0.05），但低资源语言系统性偏离，
      15% 的 lang×arch 组合 cosine>0.15。这意味着 "correctness-confidence orthogonality is universal"
      (Miao & Ungar) 需要 qualify——仅在 resource-adequate languages 上成立。
      对 worst tier：这是有价值的发现，但方向从 "positive extension" 变为 "qualification + warning"。
      需要讨论 capacity artifact 的混淆：低资源 cosine 升高可能不是 "真正的结构性非正交"，
      而是 probe quality 太差导致方向估计 noisy。与 plan_013 control task 结果联合解读。

  # ============================================================
  # plan_006: Probe Complexity Comparison
  # ============================================================
  - name: "Probe Complexity: Logistic Regression vs 2-Layer MLP (2 models × all layers)"
    plan_id: "plan_006"
    description: >
      比较 LR 和 2-layer MLP 在两个模型每层上的英语 AUROC、cross-lingual transfer degradation 和 calibration 质量。
    expected_results:
      # English AUROC comparison
      mlp_en_auroc_advantage_avg: 0.025
      mlp_en_auroc_advantage_range: [0.01, 0.04]
      # Cross-lingual transfer
      lr_zs_transfer_degradation_avg: 0.155  # (EN - target) / EN
      mlp_zs_transfer_degradation_avg: 0.195  # MLP transfers worse
      mlp_zs_degradation_excess: 0.040
      # Transfer gap by tier
      mlp_excess_degradation_high: 0.020
      mlp_excess_degradation_mid: 0.040
      mlp_excess_degradation_low: 0.065
      # Calibration
      lr_ece_avg: 0.18
      mlp_ece_avg: 0.22
      # Hypothesis test
      lr_transfers_better_significant: "14/19 languages (bootstrap p<0.05)"
    result_rationale: >
      Linear probes transfer better cross-lingually 这个假设在 7B dense 上 well-supported
      （更简单的 probe 拟合的 direction 更 language-agnostic），在大模型 MoE 上同样成立但差异更大。
      MLP 在英语上多学到 ~2.5pp（利用非线性语言特异性模式），但这些模式在 transfer 时成为负担。
      MoE 架构放大了这个效应：MLP 可以学习 expert-routing-dependent 的非线性模式，
      这些模式在不同语言 routing 不同时完全不 transfer。低资源上 MLP excess degradation 最大（6.5pp），
      因为低资源语言的 expert routing 与英语差异最大。
      这支持了 "linear probe is the right methodological choice" 但也意味着 probe 捕获的信号上限
      被 linearity constraint 限制——在 MoE 上，correctness signal 可能本质上需要非线性访问。
    tables:
      - title: "Table 10: Probe Complexity — LR vs MLP (Qwen3-235B, EN-optimal layer)"
        columns: [Metric, LR, MLP, Δ, p_value]
        rows:
          - [EN AUROC, 0.760, 0.785, +0.025, "<0.001"]
          - [ZS AUROC avg (20 lang), 0.590, 0.575, -0.015, 0.042]
          - [Transfer degradation avg, 0.155, 0.195, +0.040, 0.008]
          - [ECE avg (20 lang), 0.180, 0.220, +0.040, 0.015]
    figures_description:
      - "Fig 11: LR vs MLP transfer degradation scatter (x=LR degradation, y=MLP degradation) per language——所有点在 y=x 线上方，MLP 一致更差。"
    analysis: >
      确认 linear probe 是跨语言 transfer 的正确选择。MLP 的英语优势（+2.5pp）在 transfer 中
      被完全 offset 且反转。方法论含义：correctness signal 的 linearly accessible component
      是唯一 cross-lingually stable 的部分。这与 "low-dimensional language-agnostic subspace" 叙事一致。

  # ============================================================
  # plan_007: Additional Benchmark Evaluation
  # ============================================================
  - name: "Belebele + MMLU-ProX Generalization (20 langs × best probes + CaCLR)"
    plan_id: "plan_007"
    description: >
      在 Belebele（阅读理解）和 MMLU-ProX（20 languages）上评估最佳 probes 和 CaCLR，
      验证 GlobalMMLU 之外的泛化。
    expected_results:
      # Belebele results
      belebele_en_auroc: 0.72
      belebele_zs_avg_20lang: 0.56
      belebele_vs_globalmmlu_en_delta: -0.04
      belebele_vs_globalmmlu_zs_delta: -0.03
      belebele_caclr_delta_vs_zs: 0.001
      belebele_rank_correlation_with_globalmmlu: 0.82
      # MMLU-ProX results
      mmlupx_en_auroc: 0.74
      mmlupx_zs_avg_20lang: 0.57
      mmlupx_vs_globalmmlu_en_delta: -0.02
      mmlupx_vs_globalmmlu_zs_delta: -0.02
      mmlupx_caclr_delta_vs_zs: 0.002
      mmlupx_rank_correlation_with_globalmmlu: 0.88
      # Cross-benchmark consistency
      language_ranking_kendall_tau: 0.78
      low_resource_auroc_drop_consistent: true
    result_rationale: >
      Belebele 是阅读理解任务（与 MCQA knowledge 不同），correctness probe 的 transferability 
      预期更差因为 task-specific 信号不同。MMLU-ProX 与 GlobalMMLU 同源但翻译质量可能不同，
      期望更高一致性。两个 benchmark 上的绝对性能均低于 GlobalMMLU（因为 probe 是在 GlobalMMLU 上训练的），
      但语言排序高度一致（Kendall tau=0.78），说明 cross-lingual transfer degradation pattern
      是 task-general 的。CaCLR 在两个 benchmark 上同样 inert（delta~0），进一步确认负面结果
      不是 benchmark-specific artifact。
    tables:
      - title: "Table 11: Cross-Benchmark Generalization (Qwen3-235B)"
        columns: [Benchmark, EN_AUROC, ZS_avg, CaCLR_Δ, Rank_corr_w_GlobalMMLU]
        rows:
          - [GlobalMMLU, 0.760, 0.590, +0.002, "—"]
          - [Belebele, 0.720, 0.560, +0.001, 0.82]
          - [MMLU-ProX, 0.740, 0.570, +0.002, 0.88]
    figures_description:
      - "Fig 12: 三 benchmark 语言排序 parallel coordinates plot——高度一致的降序趋势。"
    analysis: >
      Cross-benchmark generalization 支持 findings 的 robustness：language ranking 一致（tau=0.78），
      CaCLR 一致 inert，low-resource drop 一致。Belebele 上 AUROC 稍低（阅读理解 vs 知识 MCQA），
      但 degradation pattern 相同。这为 "viability boundary" 提供了 cross-task evidence。

  # ============================================================
  # plan_010: Quantization Validation
  # ============================================================
  - name: "Quantization Validation Ablation (W4A16 vs FP16 / INT4 vs FP16)"
    plan_id: "plan_010"
    description: >
      (a) Llama 4 Scout W4A16 vs FP16 at 5 layers on 5% subset;
      (b) Qwen3-235B GPTQ-Int4 vs FP16 at 5 layers on 5% subset.
    expected_results:
      # Scout W4A16 vs FP16
      scout_w4a16_vs_fp16_auroc_delta_avg: -0.008
      scout_w4a16_vs_fp16_auroc_delta_range: [-0.015, 0.002]
      scout_w4a16_vs_fp16_correlation: 0.985
      scout_w4a16_vs_fp16_rank_agreement: "98%"
      # Qwen3 INT4 vs FP16
      qwen_int4_vs_fp16_auroc_delta_avg: -0.012
      qwen_int4_vs_fp16_auroc_delta_range: [-0.022, -0.003]
      qwen_int4_vs_fp16_correlation: 0.978
      qwen_int4_vs_fp16_rank_agreement: "96%"
      # Deep layer vulnerability
      deep_layer_quant_delta: -0.018
      shallow_layer_quant_delta: -0.005
    result_rationale: >
      量化（INT4/W4A16）对 correctness probe 的影响在 worst tier 下比 best tier 更大，
      但仍在可接受范围内。4-bit 权重量化引入的噪声在浅层影响小（-0.005 AUROC），
      在深层影响更大（-0.018），因为深层 representation 的 correctness signal 更细微
      （signal-to-noise ratio 更低），量化 noise 更容易掩盖信号。
      Qwen3-235B 的 INT4 (GPTQ) 影响比 Scout W4A16 更大（-0.012 vs -0.008），
      因为 GPTQ 是 post-training quantization 而 W4A16 保留了 16-bit 激活。
      但 rank agreement >96% 说明量化不改变 per-item correctness 排序——
      AUROC 降低主要来自 decision boundary 模糊，不是信号方向改变。
      结论：量化引入的 AUROC 降低（~1pp）远小于 cross-lingual transfer degradation（~10-15pp），
      不影响核心发现。需要在论文中报告为 limitation。
    tables:
      - title: "Table 12: Quantization Impact on Probe AUROC"
        columns: [Model, Quant, Layer, FP16_AUROC, Quant_AUROC, Δ]
        rows:
          - [Scout, W4A16, L8, 0.645, 0.642, -0.003]
          - [Scout, W4A16, L16, 0.668, 0.660, -0.008]
          - [Scout, W4A16, L24, 0.695, 0.685, -0.010]
          - [Scout, W4A16, L32, 0.718, 0.706, -0.012]
          - [Scout, W4A16, L40, 0.740, 0.725, -0.015]
          - [Qwen3, INT4, L16, 0.640, 0.635, -0.005]
          - [Qwen3, INT4, L36, 0.685, 0.675, -0.010]
          - [Qwen3, INT4, L52, 0.720, 0.705, -0.015]
          - [Qwen3, INT4, L72, 0.762, 0.742, -0.020]
          - [Qwen3, INT4, L88, 0.745, 0.723, -0.022]
    figures_description:
      - "Fig 13: FP16 vs Quantized AUROC scatter per layer——点紧贴 y=x 线但系统性偏下，深层偏移更大。"
    analysis: >
      量化影响存在但可控。深层损失更大是预期的（信号更弱），但 rank agreement >96% 
      保证了相对 ordering 可信。Worst tier 下这个结果的含义：已经偏低的 EN AUROC（0.76）
      中约 1-2pp 来自量化 artifact，真实 FP16 AUROC 可能在 0.77-0.78 区间——
      但即使如此也远低于 best tier 预期的 0.82+。在论文中作为 acknowledged limitation 报告。

  # ============================================================
  # plan_011: CKA Cross-Lingual Representation Similarity
  # ============================================================
  - name: "CKA Full-Scale Analysis (20 langs × all layers × 2 models)"
    plan_id: "plan_011"
    description: >
      计算 CKA（linear kernel）between English and each target language at every probed layer。
      包含 partial correlation controlling depth、same-layer cross-language correlation、
      per-language Spearman、subspace angle analysis。
    expected_results:
      # CKA-degradation correlation (pooled)
      cka_degradation_pooled_rho_qwen: -0.28
      cka_degradation_pooled_p_qwen: 0.008
      cka_degradation_pooled_rho_scout: -0.35
      cka_degradation_pooled_p_scout: 0.003
      # CRITICAL: partial correlation controlling depth
      cka_partial_corr_controlling_depth_qwen: 0.04
      cka_partial_corr_p_qwen: 0.58
      cka_partial_corr_controlling_depth_scout: 0.08
      cka_partial_corr_p_scout: 0.35
      # Same-layer cross-language correlation (n=19 per layer)
      same_layer_cka_vs_degradation_rho_avg: -0.42
      same_layer_significant_layers: "3/24 Qwen, 2/12 Scout"
      # Per-language Spearman
      per_lang_rho_significant_count_qwen: "4/19"
      per_lang_rho_significant_count_scout: "2/19"
      per_lang_rho_reversed_count: "3/19 (ko, vi, te)"
      # CKA cliff
      cka_cliff_depth_qwen: "75-85% depth"
      cka_cliff_depth_scout: "70-80% depth"
      cka_cliff_steepness_qwen: -0.08  # CKA drop per normalized layer
      cka_cliff_steepness_scout: -0.05
      # Subspace angle
      subspace_angle_range: [12, 58]  # degrees
      subspace_angle_high_resource_mean: 18
      subspace_angle_low_resource_mean: 45
    result_rationale: >
      CKA partial correlation controlling depth 是决定性分析——在 worst tier 下完全 n.s.
      （Qwen r=0.04 p=0.58, Scout r=0.08 p=0.35）。这意味着 pilot 阶段观察到的
      CKA-degradation 负相关（Llama rho=-0.52 p=0.001）主要被 depth confound 驱动：
      深层 CKA 低 + 深层 transfer 差，但这不是因为 "CKA 低导致 transfer 差"，
      而是 "depth 同时驱动两者"。控制 depth 后 CKA 的独立解释力归零。
      Pooled correlation 仍显著（p<0.01），但这是 Simpson's paradox 的变体——
      between-language 差异（高资源 CKA 高 + degradation 低 vs 低资源反之）
      和 within-language depth 效应混淆。Same-layer 分析（n=19 per layer）部分有效：
      在给定层深度，CKA 较高的语言确实 transfer 更好（rho=-0.42），
      但仅在少数层（5/36）达到显著——样本量不够或 CKA range 太窄。
      结论：CKA 从 "geometric analysis" 降级为 "suggestive correlational observation"。
    tables:
      - title: "Table 13: CKA Partial Correlation Controlling Depth (THE critical test)"
        columns: [Model, Partial_r, p_value, "Pooled rho (no control)", "Pooled p", Interpretation]
        rows:
          - [Qwen3-235B, 0.04, 0.58, -0.28, 0.008, "depth confound explains all"]
          - [Llama 4 Scout, 0.08, 0.35, -0.35, 0.003, "depth confound explains all"]
      - title: "Table 14: Same-Layer CKA vs Degradation (Qwen3-235B, representative layers)"
        columns: [Layer, "n (langs)", rho, p_value, Significant]
        rows:
          - [L16, 19, -0.35, 0.14, "✗"]
          - [L32, 19, -0.48, 0.037, "✓"]
          - [L48, 19, -0.52, 0.022, "✓"]
          - [L64, 19, -0.41, 0.081, "✗"]
          - [L72, 19, -0.45, 0.053, "✗"]
          - [L80, 19, -0.38, 0.11, "✗"]
          - [L88, 19, -0.28, 0.24, "✗"]
      - title: "Table 15: Subspace Angle (degrees) between EN and Target Correctness Direction"
        columns: [Language, Tier, L48_angle, L72_angle, L88_angle]
        rows:
          - [zh, HIGH, 15, 22, 35]
          - [es, HIGH, 14, 20, 32]
          - [de, HIGH, 18, 25, 38]
          - [ko, MID, 25, 35, 48]
          - [hi, MID, 28, 38, 52]
          - [sw, LOW, 38, 48, 58]
          - [bn, LOW, 35, 45, 55]
          - [te, LOW, 40, 50, 58]
    figures_description:
      - "Fig 14: CKA × layer heatmap (20 langs × 24 layers, Qwen3)——clear depth gradient 从黄(high CKA)到蓝(low CKA)，但 between-language variance 有限。"
      - "Fig 15: Partial correlation forest plot——CI 宽且跨零，与 pooled correlation 的显著结果形成鲜明对比。"
      - "Fig 16: Subspace angle vs depth (3 resource tiers)——所有 tier 随深度增加但低资源起点就高，斜率无显著 tier 差异。"
    analysis: >
      CKA 分析的核心发现是负面的：partial correlation 控制 depth 后 n.s.。
      这在 worst tier 叙事中反而成为贡献——证明了 naively 使用 CKA 解释 transfer degradation 
      是 misleading 的（depth confound），这是对 CKA-based representation analysis 方法论的 warning。
      Same-layer 分析保留了 "languages with higher CKA transfer better" 的弱 claim（between-language），
      但不足以支撑 "CKA 作为 transfer 预测器" 的 quantitative tool。
      Subspace angle 分析提供了更直接的 geometric evidence：correctness direction 的 
      language specialization 随深度增加，低资源语言的 angle 在浅层就已经很大（35-40°），
      说明 representation 从未真正 align。

  # ============================================================
  # plan_012: Linear Projection Sensitivity
  # ============================================================
  - name: "Linear Projection Sample Efficiency (10-200 pairs × 20 langs × 2 models)"
    plan_id: "plan_012"
    description: >
      变化 parallel pair 数量 (10, 20, 50, 100, 200)，评估 linear projection transfer，
      2 模型 × 5 representative layers × 20 语言。
    expected_results:
      # Sample efficiency curve (avg across languages)
      proj_10pairs_auroc_delta: 0.005
      proj_20pairs_auroc_delta: 0.010
      proj_50pairs_auroc_delta: 0.015
      proj_100pairs_auroc_delta: 0.022
      proj_200pairs_auroc_delta: 0.028
      # Variance across seeds
      proj_10pairs_std: 0.032
      proj_20pairs_std: 0.025
      proj_50pairs_std: 0.020
      proj_100pairs_std: 0.014
      proj_200pairs_std: 0.010
      # By resource tier (50 pairs)
      proj_50_high_resource_delta: 0.025
      proj_50_mid_resource_delta: 0.015
      proj_50_low_resource_delta: -0.005
      proj_50_low_resource_std: 0.028
      # Minimum viable pairs
      min_pairs_for_positive_avg_delta: 20
      min_pairs_for_consistent_improvement: "100 (still fails for sw, bn, te)"
      # Comparison point
      proj_50_wins_over_zeroshot: "14/19 languages"
      proj_50_significantly_better: "7/19 languages (bootstrap p<0.05)"
    result_rationale: >
      Linear projection 在 worst tier 下表现不稳定，核心原因是 MoE 架构的高维异质性。
      50 parallel pairs 学习的 rotation matrix 有效自由度为 min(50, d)=50 远小于 d=4096，
      只能 capture 低秩近似。在高资源语言上这足够了（correctness subspace 旋转 angle 小，
      低秩近似够用），但低资源语言 angle 大（45-58°）且 variance 高，50 pairs 不足以
      稳定估计旋转矩阵。200 pairs 改善了稳定性但 delta 仍然只有 +0.028 avg——
      说明瓶颈不只是 estimation noise，而是 correctness direction 在低资源上可能不存在 
      clean linear correspondence（capacity artifact 问题，见 plan_013）。
      Low resource 上 10-50 pairs 的 delta 可以是负的（-0.005 at 50 pairs），
      说明 learned projection 比 identity map（zero-shot）更差——投影 noise 比不投影更有害。
    tables:
      - title: "Table 16: Linear Projection — Δ AUROC by Pair Count (avg across 20 langs, Qwen3-235B)"
        columns: [N_pairs, Δ_AUROC_avg, std, "Wins/19", "Sig wins (p<0.05)"]
        rows:
          - [10, +0.005, 0.032, "10/19", "2/19"]
          - [20, +0.010, 0.025, "12/19", "4/19"]
          - [50, +0.015, 0.020, "14/19", "7/19"]
          - [100, +0.022, 0.014, "16/19", "10/19"]
          - [200, +0.028, 0.010, "17/19", "13/19"]
      - title: "Table 17: Linear Projection 50 Pairs — By Resource Tier"
        columns: [Tier, Δ_AUROC_avg, std, "Sig improvement"]
        rows:
          - [HIGH (4 langs), +0.025, 0.012, "3/4"]
          - [MID (13 langs), +0.015, 0.018, "4/13"]
          - [LOW (3 langs), -0.005, 0.028, "0/3"]
    figures_description:
      - "Fig 17: Sample efficiency curve (x=N pairs, y=Δ AUROC) with 3 tier bands——HIGH 快速饱和，MID 缓慢爬升，LOW 在零附近或偏负。"
      - "Fig 18: Per-language 50-pair Δ AUROC bar chart sorted by magnitude——clear resource-tier gradient。"
    analysis: >
      Linear projection 是 "surprisingly strong baseline" 但仅限于高/中资源语言。
      在低资源上不稳定（std>0.028）且平均效果为负。200 pairs 是 practical minimum for consistency
      但 3 种低资源语言 even at 200 pairs 仍未一致改善。这为 viability boundary 提供了
      另一条 evidence line：linear alignment 需要 source-target correctness subspace 有足够 overlap，
      低资源语言不满足这个前提条件。

  # ============================================================
  # plan_013: Control Tasks (Full-Scale Extension)
  # ============================================================
  - name: "Probing Control Tasks — Full 20 Languages × 2 Models"
    plan_id: "plan_013"
    description: >
      在 20 语言 × 2 模型上训练 control probes（permuted labels），计算 selectivity。
      已完成英语 Qwen-7B baseline（plan_013 registry），现扩展到大模型全语言。
    expected_results:
      # Selectivity statistics
      selectivity_below_005_fraction_overall: 0.38
      selectivity_below_005_fraction_high_resource: 0.15
      selectivity_below_005_fraction_mid_resource: 0.35
      selectivity_below_005_fraction_low_resource: 0.72
      # Per-model
      selectivity_below_005_qwen: 0.35
      selectivity_below_005_scout: 0.41
      # Shallow vs deep layers
      selectivity_below_005_shallow_half: 0.55
      selectivity_below_005_deep_half: 0.22
      # Selectivity values (EN reference from mvp)
      en_selectivity_deep_layers: 0.25  # from plan_013 registry
      # Cross-lingual selectivity
      zh_selectivity_deep_avg: 0.18
      es_selectivity_deep_avg: 0.17
      hi_selectivity_deep_avg: 0.10
      ko_selectivity_deep_avg: 0.09
      sw_selectivity_deep_avg: 0.03
      bn_selectivity_deep_avg: 0.02
      te_selectivity_deep_avg: 0.02
      # Capacity artifact analysis
      capacity_artifact_lang_layer_pairs: "~180/912 total (38%)"
      low_resource_artifact_rate: "72% of low-resource lang-layer combinations"
    result_rationale: >
      Control task 分析是 worst tier 的核心贡献之一。在大模型 MoE 上，shallow layers 的 
      selectivity 普遍低于 0.05——probe 在 permuted labels 上也能达到接近 real labels 的 AUROC，
      说明信号来自 memorization/capacity 而非 genuine correctness direction。
      低资源语言几乎全部受影响（72% artifact rate），原因：
      (1) GlobalMMLU 低资源翻译质量差→test items 有系统性 pattern（如翻译 artifacts）
      可被 probe 利用但与 correctness 无关；
      (2) 低资源 representation 本身 less structured，probe 在 real/permuted labels 上
      表现差异小；
      (3) MoE expert routing 在低资源上更 random（缺乏 consistent routing pattern），
      probe 拟合的是 routing noise 而非 semantic content。
      38% overall artifact rate 大幅超过英语的 plan_013 baseline（浅层 0.02-0.04），
      说明英语 selectivity 分析严重低估了多语言场景的 capacity artifact 问题。
      这是对 Hewitt & Liang (2019) 框架在多语言场景下的重要扩展——
      原论文仅考虑英语单任务，未预见到跨语言 probing 的 artifact 放大效应。
    tables:
      - title: "Table 18: Selectivity by Resource Tier and Depth (Qwen3-235B)"
        columns: [Tier, Shallow_sel, Mid_sel, Deep_sel, "Artifact rate (<0.05)"]
        rows:
          - [EN (source), 0.03, 0.12, 0.25, "25%"]
          - [HIGH (4 langs), 0.03, 0.09, 0.18, "32%"]
          - [MID (12 langs), 0.02, 0.06, 0.10, "48%"]
          - [LOW (3 langs), 0.01, 0.03, 0.03, "72%"]
      - title: "Table 19: Capacity Artifact Language Breakdown (deep layers only, selectivity < 0.05)"
        columns: [Language, Tier, Sel_best_layer, Is_artifact, Real_AUROC, Ctrl_AUROC]
        rows:
          - [en, source, 0.25, "✗", 0.760, 0.510]
          - [zh, HIGH, 0.18, "✗", 0.672, 0.492]
          - [es, HIGH, 0.17, "✗", 0.668, 0.498]
          - [fr, HIGH, 0.15, "✗", 0.662, 0.512]
          - [de, HIGH, 0.14, "✗", 0.653, 0.513]
          - [ko, MID, 0.09, "✗", 0.602, 0.512]
          - [hi, MID, 0.10, "✗", 0.588, 0.488]
          - [ru, MID, 0.08, "✗", 0.608, 0.528]
          - [tr, MID, 0.06, "~", 0.571, 0.511]
          - [ar, MID, 0.05, "~", 0.555, 0.505]
          - [sw, LOW, 0.03, "✓", 0.508, 0.478]
          - [bn, LOW, 0.02, "✓", 0.538, 0.518]
          - [te, LOW, 0.02, "✓", 0.521, 0.501]
    figures_description:
      - "Fig 19: Selectivity heatmap (20 langs × 24 layers, Qwen3)——clear gradient: 右下角（deep+high resource）高 selectivity，左上角和右上低资源区域全部低 selectivity。这是论文核心 figure 之一。"
      - "Fig 20: Selectivity vs ZS AUROC scatter——低 selectivity 区域的 ZS AUROC 'success' 可能全是 artifact，red zone 标记。"
    analysis: >
      这是 worst tier 最重要的发现：38% 的 lang-layer 组合 selectivity<0.05，意味着
      probe AUROC "success" 中近四成可能是 false positive。低资源语言的 72% artifact rate
      意味着 sw/bn/te 的所有 probing 结果都不可信——它们的 "transfer success" 和 "AUROC>0.50"
      可能完全来自 capacity artifact。这从根本上改变了 Claim 1 的解读：
      Pareto frontier 分析中使用的 ZS AUROC 值在低资源端是 corrupted 的，
      frontier 上的低资源数据点需要标注为 "artifact-suspect"。
      对论文叙事：这是 Hewitt & Liang 框架的多语言扩展，本身就是 paper-worthy 的发现，
      也为 "viability boundary" 提供了最强的 evidence——probing-based calibration 
      在低资源语言上不 viable，不是因为 transfer 失败，而是因为 probe 本身不可信。

  # ============================================================
  # plan_008: Gemma 4 31B Dense (Camera-Ready P2)
  # ============================================================
  - name: "Gemma 4 31B Dense Full Pareto (P2 Camera-Ready)"
    plan_id: "plan_008"
    description: >
      第三个架构（dense, 60 layers, FP16），提供 dense vs MoE architectural contrast。
    expected_results:
      en_best_auroc: 0.78
      en_best_layer: "L48 (80% depth)"
      zs_transfer_auroc_avg_20lang: 0.61
      pareto_global_spearman_rho: -0.48
      pareto_global_spearman_p: 0.002
      pareto_per_lang_significant_count: "9/19"
      selectivity_below_005_fraction: 0.22
      linear_proj_50pairs_delta_avg: 0.028
    result_rationale: >
      Dense 架构是 Pareto frontier 分析的最佳场景——没有 MoE routing 碎片化，
      所有语言共享同一 expert（整个 FFN），representation 连续性更强。
      预期 Gemma 31B Dense 的 global rho 回到 MVP 阶段 Qwen-7B 的水平（-0.48, p=0.002），
      约一半语言显著。Selectivity 也更好（22% artifact rate vs MoE 的 38%）。
      EN AUROC 可能是三个模型中最高的（0.78），因为 dense 中 correctness signal 更集中。
      但这是 camera-ready P2 extension——如果 worst tier 的核心叙事已经 established
      （MoE Pareto noisy, control task artifact），dense 结果成为对比证据：
      "dense architecture recovers Pareto tradeoff; MoE disrupts it"——
      这实际上加强了 architecture-dependent viability boundary 的 claim。
    tables:
      - title: "Table 20: Architecture Comparison Summary"
        columns: [Model, Type, Global_rho, p, "Sig langs", "Artifact%"]
        rows:
          - [Qwen3-235B, MoE, -0.18, 0.12, "3/19", "38%"]
          - [Llama4 Scout, MoE, -0.05, 0.62, "1/19", "41%"]
          - [Gemma4 31B, Dense, -0.48, 0.002, "9/19", "22%"]
    figures_description:
      - "Fig 21: 3-architecture Pareto rho comparison——dense 明显强于两个 MoE，支持 architecture-dependent narrative。"
    analysis: >
      Gemma 结果是 worst tier 叙事的关键对照——证明 Pareto frontier 在 dense 架构上仍然有效，
      MoE 的 failure 是 architecture-specific 的。这把 worst tier 从 "method completely fails"
      转为 "method works under specific architectural conditions"——更有 nuance 的 viability boundary。

  # ============================================================
  # plan_009: Extended Language Coverage (Camera-Ready P2)
  # ============================================================
  - name: "Extended Language Coverage (50+ languages, P2 Camera-Ready)"
    plan_id: "plan_009"
    description: >
      从 20 扩展到 50+ 语言，利用 GlobalMMLU/Belebele 的完整语言集。
    expected_results:
      total_languages_tested: 52
      zs_transfer_success_rate_060: "22/51 (43%)"
      artifact_rate_overall: 0.42
      artifact_rate_new_low_resource: 0.85
      viability_boundary_clear: "AUROC>0.60 AND selectivity>0.05: only 18/51 languages"
      new_language_families_covered: 6
    result_rationale: >
      扩展到 50+ 语言主要增加低资源语言（GlobalMMLU 覆盖的尾部语言），
      这些语言的 representation quality 更差，artifact rate 更高（85%+），
      进一步支持 viability boundary 叙事。真正 viable 的语言仅 18/51（35%），
      全部是高/中资源。这个数字本身就是论文的核心 finding：
      probe-based calibration 仅对约 1/3 的测试语言可行。
    tables:
      - title: "Table 21: Viability Classification (52 languages)"
        columns: [Category, Count, Criterion, Example_langs]
        rows:
          - [Viable, 18, "AUROC>0.60 + sel>0.05", "en, zh, es, fr, de, ja, pt, ru, ko, nl..."]
          - [Marginal, 12, "AUROC>0.55 + sel 0.03-0.05", "hi, tr, pl, id, uk, ar..."]
          - [Non-viable, 22, "AUROC<0.55 OR sel<0.03", "sw, bn, te, am, yo, ha, ig..."]
    figures_description:
      - "Fig 22: World map with viability color coding——欧洲/东亚 viable，撒哈拉以南非洲/南亚大部 non-viable。"
    analysis: >
      52 语言版本强化了 viability boundary 叙事的 impact——从 "20 语言上的发现" 
      扩展为 "across majority of world's languages, probe-based calibration is not viable"。
      18/51 viable rate 是 headline-worthy 的。但注意这可能 overstate the problem：
      低资源语言的 non-viability 部分来自 GlobalMMLU 翻译质量差，
      而非 representation 本身的缺陷——需要在 discussion 中 acknowledge。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efdfcbb9-5656-49dc-b28a-65780d07acdb",
  "isSidechain": false,
  "requestId": "req_011CbF3P92bFQQGAHduxiveZ",
  "type": "assistant",
  "uuid": "26cf4c96-a3b7-425a-bff1-a3c22c130b28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmVeoxGbPpAfdpSWNmyrpi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9539,
      "cache_read_input_tokens": 31590,
      "output_tokens": 21504,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21504,
          "cache_read_input_tokens": 31590,
          "cache_creation_input_tokens": 9539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9539
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：大模型上 Pareto 信号噪声大、CaCLR 和 linear projection 均不稳定、CKA 无解释力、大面积 capacity artifacts 侵蚀低资源结果；需重构为 cross-lingual probing 方法论批判 + viability boundary 刻画 核心假设：['大…",
  "leafUuid": "26cf4c96-a3b7-425a-bff1-a3c22c130b28",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Stress-testing probe-based calibration across languages",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：大模型上 Pareto 信号噪声大、CaCLR 和 linear projection 均不稳定、CKA 无解释力、大面积 capacity artifacts 侵蚀低资源结果；需重构为 cross-lingual probing 方法论批判 + viability boundary 刻画 核心假设：['大…",
  "leafUuid": "26cf4c96-a3b7-425a-bff1-a3c22c130b28",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Stress-testing probe-based calibration across languages",
  "sessionId": "d1e44a8f-6c4b-4ca5-9efa-f7c6b3fffa6a"
}
```

---
