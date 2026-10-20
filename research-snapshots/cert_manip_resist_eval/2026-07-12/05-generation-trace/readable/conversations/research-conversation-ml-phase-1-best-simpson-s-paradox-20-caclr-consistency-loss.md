# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：核心几何洞见（Simpson's Paradox）在双架构 × 20 语言上显著复现；CaCLR consistency loss 提供可测量迁移增益；

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/3bed0805-e277-4cba-a173-e5dbb10b2135.jsonl`
- **Structured JSON:** [`df1ed44b91d6ad79f5d3.json`](../../sessions/df/df1ed44b91d6ad79f5d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:52:58.672Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:52:58.672Z",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：核心几何洞见（Simpson's Paradox）在双架构 × 20 语言上显著复现；CaCLR consistency loss 提供可测量迁移增益；所有 claims 完整保留\n核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均显著 (p < 0.01)，CKA 控制 depth 后确实解释 transfer 差异\", 'CaCLR consistency loss (β > 0) 在深层 layer 上比 zero-shot 提升 ≥2pp AUROC', 'Pareto frontier 架构依赖性清晰：Qwen3 强 tradeoff, Llama 4 弱 tradeoff，与 MVP 模式一致', 'Difficulty decomposition 可处方性地预测哪些语言需要哪种 alignment 策略', 'Control task artifacts 集中在低资源语言 (~25-30%)，不波及中高资源', 'Linear projection ≤50 pairs 达到 95%+ 性能，resource-tier 分层饱和清晰']\n关键指标范围：{'en_best_auroc': [0.77, 0.83], 'zs_pass_rate_20lang': [0.8, 0.9], 'pareto_spearman_rho_significant_archs': [2, 2], 'simpson_partial_rho': [0.3, 0.55], 'simpson_p_value_max': [0.001, 0.01], 'caclr_mean_delta_auroc_vs_zs': [0.02, 0.05], 'linear_proj_pairs_to_95pct': [30, 50], 'control_artifact_rate_lowres': [0.2, 0.3], 'decomp_capability_delta_auroc': [0.02, 0.04], 'procrustes_reversal_threshold_zs_auroc': [0.48, 0.55]}\n叙事方向：原始 framing 完全成立。以 Simpson's Paradox 几何洞见为核心新颖性开篇，CaCLR 作为正面方法贡献。标题强调 'geometric analysis reveals when and why cross-lingual calibration transfer succeeds.' 四条 claim 完整因果链保留：Pareto discovery → decomposition analysis → CaCLR method → CKA geometric explanation。Control task warning + projection sample efficiency 作为加分贡献。无需弱化任何 claims。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\nfocus: Key improvements since last dream: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative but partial correlation controlling for depth is positive (Llama rho=+0.41, p=0.006), genuine geometric insight; (2) Claim 4 downgraded to subsection, space freed for control task finding and projection efficiency; (3) Control task methodological warning elevated to main body (28% low-resource artifacts); (4) Linear projection sample efficiency (~50 pairs, tier-stratified); (5) Procrustes effect reversal (helps ZS<0.50, hurts ZS>0.60); (6) Complete CaCLR implementation spec for reproducibility; (7) 30+ references planned; (8) Statistical framework: bootstrap CI + permutation tests + Cohen's d; (9) Figure plan: Pareto scatter plot, layer-wise AUROC, decomposition visualization. Focus review on whether novelty improvements are sufficient for main conference acceptance.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique.'\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- exp_id: plan_013_probing_controls_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T04:52:58.675Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:52:58.675Z",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-21T04:52:58.710Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：核心几何洞见（Simpson's Paradox）在双架构 × 20 语言上显著复现；CaCLR consistency loss 提供可测量迁移增益；所有 claims 完整保留
核心假设：["Simpson's Paradox partial correlation 在两个架构上均显著 (p < 0.01)，CKA 控制 depth 后确实解释 transfer 差异", 'CaCLR consistency loss (β > 0) 在深层 layer 上比 zero-shot 提升 ≥2pp AUROC', 'Pareto frontier 架构依赖性清晰：Qwen3 强 tradeoff, Llama 4 弱 tradeoff，与 MVP 模式一致', 'Difficulty decomposition 可处方性地预测哪些语言需要哪种 alignment 策略', 'Control task artifacts 集中在低资源语言 (~25-30%)，不波及中高资源', 'Linear projection ≤50 pairs 达到 95%+ 性能，resource-tier 分层饱和清晰']
关键指标范围：{'en_best_auroc': [0.77, 0.83], 'zs_pass_rate_20lang': [0.8, 0.9], 'pareto_spearman_rho_significant_archs': [2, 2], 'simpson_partial_rho': [0.3, 0.55], 'simpson_p_value_max': [0.001, 0.01], 'caclr_mean_delta_auroc_vs_zs': [0.02, 0.05], 'linear_proj_pairs_to_95pct': [30, 50], 'control_artifact_rate_lowres': [0.2, 0.3], 'decomp_capability_delta_auroc': [0.02, 0.04], 'procrustes_reversal_threshold_zs_auroc': [0.48, 0.55]}
叙事方向：原始 framing 完全成立。以 Simpson's Paradox 几何洞见为核心新颖性开篇，CaCLR 作为正面方法贡献。标题强调 'geometric analysis reveals when and why cross-lingual calibration transfer succeeds.' 四条 claim 完整因果链保留：Pareto discovery → decomposition analysis → CaCLR method → CKA geometric explanation。Control task warning + projection sample efficiency 作为加分贡献。无需弱化任何 claims。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: xling_calib_direction
focus: Key improvements since last dream: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative but partial correlation controlling for depth is positive (Llama rho=+0.41, p=0.006), genuine geometric insight; (2) Claim 4 downgraded to subsection, space freed for control task finding and projection efficiency; (3) Control task methodological warning elevated to main body (28% low-resource artifacts); (4) Linear projection sample efficiency (~50 pairs, tier-stratified); (5) Procrustes effect reversal (helps ZS<0.50, hurts ZS>0.60); (6) Complete CaCLR implementation spec for reproducibility; (7) 30+ references planned; (8) Statistical framework: bootstrap CI + permutation tests + Cohen's d; (9) Figure plan: Pareto scatter plot, layer-wise AUROC, decomposition visualization. Focus review on whether novelty improvements are sufficient for main conference acceptance.

## paper_framing.md

# Paper Framing — xling_calib_direction

## Target Venue
- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
- Core submission: 2 models × 20 languages × all contributions
- Camera-ready extension: Gemma 4 31B Dense + 30+ languages

## Core Insight
The model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.

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

### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)
The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty ("method replication to more languages"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).
- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.

### Key Empirical Contributions (elevated from appendix to main body, D012)
- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.
- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.
- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.

## Story Spine
- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.
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
10. **"No mechanistic explanation"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as "geometric analysis" not "mechanistic explanation." **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.
11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
13. **"CaCLR is your own method — self-debunking is less impactful"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.
14. **"CKA is correlational, not mechanistic"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.

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
  "promptId": "71f7a31c-faf5-4838-a851-ebac678d912c",
  "type": "user",
  "uuid": "6fa9429b-9ab0-498c-bce6-99f208f76528",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:52:58.709Z_

```json
{
  "parentUuid": "6fa9429b-9ab0-498c-bce6-99f208f76528",
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
  "uuid": "f157b997-b7fa-455d-ae41-0499bec68185",
  "timestamp": "2026-05-21T04:52:58.709Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:52:58.709Z_

```json
{
  "parentUuid": "f157b997-b7fa-455d-ae41-0499bec68185",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "62aaa55a-6fb2-4bf6-94b8-a3e865dc488f",
  "timestamp": "2026-05-21T04:52:58.709Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：核心几何洞见（Simpson's Paradox）在双架构 × 20 语言上显著复现；CaCLR consistency loss 提供可测量迁移增益；所有 claims 完整保留 核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均显著 (p < 0.01…",
  "leafUuid": "62aaa55a-6fb2-4bf6-94b8-a3e865dc488f",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Simpson's Paradox reveals cross-lingual correctness probe transfer",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Assistant

_source line 8 · 2026-05-21T04:53:48.355Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for every planned experiment in the experiment_plan, based on the "best" tier definition provided. Let me carefully analyze each experiment and produce realistic predicted results that are consistent with:

1. The best tier definition (Simpson's Paradox significant on both architectures, CaCLR provides measurable gains, all claims preserved)
2. The key metric ranges specified
3. The MVP data already collected
4. The paper framing and claims

Let me go through each planned experiment:

**plan_001**: Full Pareto on Qwen3-235B-A22B (94 layers, MoE, INT4), 20 languages, 24 probed layers


- Scaling up from the Qwen2.5-7B MVP results, I'd expect the larger model to achieve around 0.81 AUROC on English within the best tier range of 0.77-0.83, with approximately 17 out of 20 languages passing the threshold.

**plan_002**: Full Pareto on Llama 4 Scout (48 layers, MoE, W4A16), 12 probed layers
- Building on the Llama-3.1-8B MVP baseline, this experiment should show similar performance patterns but with the architectural differences of the Scout variant.

**plan_003**: CaCLR implementation
- Expecting modest improvements in the 0.02-0.05 AUROC range from the contrastive learning approach.

**plan_004**: Difficulty decomposition
- Looking at capability deltas around 0.02-0.04 AUROC across difficulty levels.

**plan_005**: Cross-lingual orthogonality

**plan_006**: Probe complexity comparison

**plan_007**: Additional benchmark evaluation

**plan_010**: Quantization validation

**plan_011**: CKA analysis - this is the key one for Simpson's Paradox
- Examining representational similarity with partial correlations expected between 0.3-0.55, which should help explain the paradox.

**plan_012**: Linear projection sensitivity
- Testing how many language pairs are needed to reach 95% performance, expecting around 30-50 pairs.

**plan_013**: Already complete.

**plan_008**: Gemma 4 evaluation (P2, camera-ready)

**plan_009**: Extended languages (P2, camera-ready)

Now I'm working through the detailed YAML with result rationales for each metric. For the 20 typologically diverse languages, I'm considering the distribution across high-resource languages like Chinese, Spanish, French, and German, mid-resource ones like Hindi, Russian, Korean, and Turkish, and lower-resource languages like Swahili and Bengali.

For plan_001 with Qwen3-235B, I'm predicting stronger English performance around 0.81 AUROC given the larger model size, and expecting richer Pareto frontier structures from the 94-layer MoE architecture.

For plan_002 with Llama 4 Scout, the different MoE design with 17B active parameters should yield weaker Pareto tradeoffs compared to Qwen, with English AUROC closer to 0.79 and fewer languages passing the threshold.

For plan_003 with CaCLR, the β parameter helps in deeper layers by a few percentage points, and α improves calibration, but the gains are incremental rather than dramatic compared to the linear baseline.

For plan_011, the raw correlations show a depth confound masking the true relationship—when I control for depth statistically, the partial correlations flip positive and significant on both architectures, with Qwen at ~0.42 and Llama at ~0.38, both well below p < 0.01. This is the critical insight that resolves the apparent contradiction.

Now I'm laying out the prediction ranges for the best-tier experiments: AUROC around 0.77-0.83, zero-shot pass rates hitting 16-18 out of 20 languages, both architectures showing significant Pareto effects, Simpson's paradox partial correlations between 0.3-0.55 with p-values in the 0.001-0.01 range, and various other metrics like the Procrustes reversal threshold around 0.48-0.55 for zero-shot AUROC.

Writing YAML predictions... For Llama 4 Scout, the active parameter count is comparable to the larger Qwen model, but it shows slightly weaker English performance at around 0.79 AUROC and a less consistent depth-performance relationship across languages. I'm expecting about 80% of languages to pass the zero-shot threshold with this architecture's different layer structure.

Now I need to organize the experimental plans into YAML format, covering the planned experiments while excluding the ones already completed.

Generating YAML structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62aaa55a-6fb2-4bf6-94b8-a3e865dc488f",
  "isSidechain": false,
  "requestId": "req_011CbF7e9qqZMBg3vPQqMuKU",
  "type": "assistant",
  "uuid": "cc1c5dbf-1129-4f16-ae48-5315ec47c8be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpNioindvzTrmjhD94qwkt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17221,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17221,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2180,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17221
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

_source line 9 · 2026-05-21T04:53:48.358Z_

Let me first check the project directory for any existing files that might inform the predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc1c5dbf-1129-4f16-ae48-5315ec47c8be",
  "isSidechain": false,
  "requestId": "req_011CbF7e9qqZMBg3vPQqMuKU",
  "type": "assistant",
  "uuid": "4ac9be51-8851-4fe0-b101-a81de29ab96c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpNioindvzTrmjhD94qwkt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17221,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17221,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2180,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17221
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

_source line 10 · 2026-05-21T04:53:49.124Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01K6G88FDqPVQWuMXV6vgLbq`</summary>

```json
{
  "pattern": "**/*.{md,yaml,yml,json,py}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ac9be51-8851-4fe0-b101-a81de29ab96c",
  "isSidechain": false,
  "requestId": "req_011CbF7e9qqZMBg3vPQqMuKU",
  "type": "assistant",
  "uuid": "e731d15c-656b-41db-92a6-9d447619761e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpNioindvzTrmjhD94qwkt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17221,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17221,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2180,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17221
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

_source line 11 · 2026-05-21T04:53:49.145Z_

<details><summary>↩ Tool result · `toolu_01K6G88FDqPVQWuMXV6vgLbq`</summary>

```text
config/approvals.yaml
config/mcp_config.json
config/backend.yaml
config/pool.json
config/feishu.yaml
config/mcp_config_director.json
config/mcp_config_reviewer.json
.claude/sessions/no_project_9d2a9208/CLAUDE.md
.claude/sessions/no_project_9d2a9208/AGENTS.md
config/mcp_config_no_project.json
config/mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
workspace.yaml
config/venue_registry.yaml
config/venue_rules/corl-2026.yaml
config/venue_rules/emnlp-2026.yaml
idea_generator/ideas.yaml
config/session_state.json
projects/xling_calib_direction/literature_map.yaml
projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/AGENTS.md
config/mcp_config_distiller.json
projects/xling_calib_direction/code/extract_activations.py
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
projects/xling_calib_direction/code/analyze_results.py
projects/xling_calib_direction/checkpoints/mvp_001_PREPARING_20260520T141702.json
config/mcp_config_worker_69e382e805b6f185c49ecc4b6d1f2d44.json
projects/xling_calib_direction/checkpoints/mvp_001_QUEUED_20260520T142501.json
projects/xling_calib_direction/checkpoints/mvp_001_RUNNING_20260520T142506.json
projects/xling_calib_direction/logs/workers/worker_code_mvp_001_setup_and_run_20260520T141803_result.json
config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
projects/xling_calib_direction/logs/workers/worker_diag_mvp_001_download_check_20260520T143045_result.json
config/mcp_config_worker_8164f16cea05223301ec10d99f320a22.json
config/mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
projects/xling_calib_direction/logs/workers/worker_prep_mvp_001_parallel_tasks_20260520T150620_result.json
projects/xling_calib_direction/checkpoints/mvp_002_PREPARING_20260520T162627.json
projects/xling_calib_direction/checkpoints/mvp_002_QUEUED_20260520T170009.json
projects/xling_calib_direction/checkpoints/mvp_002_RUNNING_20260520T170020.json
projects/xling_calib_direction/logs/workers/worker_run_mvp_002_submit_20260520T165936_result.json
projects/xling_calib_direction/checkpoints/mvp_001_RUNNING_20260520T182006.json
projects/xling_calab_direction/registry.yaml
projects/xling_calib_direction/checkpoints/mvp_001_DONE_20260520T182309.json
config/mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
projects/xling_calib_direction/logs/workers/worker_analysis_mvp_001_gate_recheck_20260520T182750_result.json
projects/xling_calib_direction/checkpoints/mvp_003_QUEUED_20260520T184756.json
projects/xling_calib_direction/checkpoints/mvp_003_RUNNING_20260520T184808.json
projects/xling_calib_direction/logs/workers/worker_analysis_mvp_001_layer27_supplement_20260520T184655_result.json
projects/xling_calib_direction/docs/IDEA_BRIEF.md
projects/xling_calib_direction/checkpoints/mvp_002_RUNNING_20260520T185540.json
projects/xling_calib_direction/checkpoints/mvp_002_DONE_20260520T185550.json
projects/xling_calib_direction/logs/workers/worker_analysis_mvp_002_diagnose_20260520T185417_result.json
projects/xling_calib_direction/logs/workers/worker_code_mvp_003_llama_20260520T182822_result.json
projects/xling_calib_direction/checkpoints/mvp_002_DONE_20260520T191328.json
config/mcp_config_worker_32521490f1e5b8d0d98af5e30db64a03.json
projects/xling_calib_direction/code/train_probe.py
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/experiment_data.json
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md
projects/xling_calib_direction/checkpoints/mvp_002_DONE_20260520T192851.json
projects/xling_calib_direction/logs/workers/worker_code_fix_layers_autodetect_20260520T191433_result.json
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/experiment_data.json
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md
config/projects/xling_calib_direction.yaml
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
config/mcp_config_dream_review_director.json
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml
config/mcp_config_review_reviewer_1.json
config/mcp_config_review_reviewer_2.json
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml
config/mcp_config_review_director.json
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_report.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md
projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/CLAUDE.md
projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/AGENTS.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_report.md
projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/meta.yaml
projects/xling_calib_direction/external_review_state.json
projects/xling_calib_direction/artifacts/review_issues.yaml
projects/xling_calib_direction/artifacts/review_reports/round_0.md
projects/xling_calib_direction/logs/workers/worker_analysis_temp_scaling_leakage_fix_20260520T201907_result.json
projects/xling_calib_direction/logs/workers/worker_code_cka_pilot_20260520T201949_result.json
projects/xling_calib_direction/checkpoints/mvp_003_RUNNING_20260520T203425.json
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e731d15c-656b-41db-92a6-9d447619761e",
  "isSidechain": false,
  "promptId": "71f7a31c-faf5-4838-a851-ebac678d912c",
  "type": "user",
  "uuid": "108a16e8-7e73-4fa3-8a27-4216d298bf56",
  "toolUseResult": {
    "filenames": [
      "config/approvals.yaml",
      "config/mcp_config.json",
      "config/backend.yaml",
      "config/pool.json",
      "config/feishu.yaml",
      "config/mcp_config_director.json",
      "config/mcp_config_reviewer.json",
      ".claude/sessions/no_project_9d2a9208/CLAUDE.md",
      ".claude/sessions/no_project_9d2a9208/AGENTS.md",
      "config/mcp_config_no_project.json",
      "config/mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json",
      "workspace.yaml",
      "config/venue_registry.yaml",
      "config/venue_rules/corl-2026.yaml",
      "config/venue_rules/emnlp-2026.yaml",
      "idea_generator/ideas.yaml",
      "config/session_state.json",
      "projects/xling_calib_direction/literature_map.yaml",
      "projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/distiller_70eed89a/AGENTS.md",
      "config/mcp_config_distiller.json",
      "projects/xling_calib_direction/code/extract_activations.py",
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
      "projects/xling_calib_direction/code/analyze_results.py",
      "projects/xling_calib_direction/checkpoints/mvp_001_PREPARING_20260520T141702.json",
      "config/mcp_config_worker_69e382e805b6f185c49ecc4b6d1f2d44.json",
      "projects/xling_calib_direction/checkpoints/mvp_001_QUEUED_20260520T142501.json",
      "projects/xling_calib_direction/checkpoints/mvp_001_RUNNING_20260520T142506.json",
      "projects/xling_calib_direction/logs/workers/worker_code_mvp_001_setup_and_run_20260520T141803_result.json",
      "config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json",
      "projects/xling_calib_direction/logs/workers/worker_diag_mvp_001_download_check_20260520T143045_result.json",
      "config/mcp_config_worker_8164f16cea05223301ec10d99f320a22.json",
      "config/mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json",
      "projects/xling_calib_direction/logs/workers/worker_prep_mvp_001_parallel_tasks_20260520T150620_result.json",
      "projects/xling_calib_direction/checkpoints/mvp_002_PREPARING_20260520T162627.json",
      "projects/xling_calib_direction/checkpoints/mvp_002_QUEUED_20260520T170009.json",
      "projects/xling_calib_direction/checkpoints/mvp_002_RUNNING_20260520T170020.json",
      "projects/xling_calib_direction/logs/workers/worker_run_mvp_002_submit_20260520T165936_result.json",
      "projects/xling_calib_direction/checkpoints/mvp_001_RUNNING_20260520T182006.json",
      "projects/xling_calab_direction/registry.yaml",
      "projects/xling_calib_direction/checkpoints/mvp_001_DONE_20260520T182309.json",
      "config/mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json",
      "projects/xling_calib_direction/logs/workers/worker_analysis_mvp_001_gate_recheck_20260520T182750_result.json",
      "projects/xling_calib_direction/checkpoints/mvp_003_QUEUED_20260520T184756.json",
      "projects/xling_calib_direction/checkpoints/mvp_003_RUNNING_20260520T184808.json",
      "projects/xling_calib_direction/logs/workers/worker_analysis_mvp_001_layer27_supplement_20260520T184655_result.json",
      "projects/xling_calib_direction/docs/IDEA_BRIEF.md",
      "projects/xling_calib_direction/checkpoints/mvp_002_RUNNING_20260520T185540.json",
      "projects/xling_calib_direction/checkpoints/mvp_002_DONE_20260520T185550.json",
      "projects/xling_calib_direction/logs/workers/worker_analysis_mvp_002_diagnose_20260520T185417_result.json",
      "projects/xling_calib_direction/logs/workers/worker_code_mvp_003_llama_20260520T182822_result.json",
      "projects/xling_calib_direction/checkpoints/mvp_002_DONE_20260520T191328.json",
      "config/mcp_config_worker_32521490f1e5b8d0d98af5e30db64a03.json",
      "projects/xling_calib_direction/code/train_probe.py",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/experiment_data.json",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md",
      "projects/xling_calib_direction/checkpoints/mvp_002_DONE_20260520T192851.json",
      "projects/xling_calib_direction/logs/workers/worker_code_fix_layers_autodetect_20260520T191433_result.json",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/experiment_data.json",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md",
      "config/projects/xling_calib_direction.yaml",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml",
      "config/mcp_config_dream_review_director.json",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml",
      "config/mcp_config_review_reviewer_1.json",
      "config/mcp_config_review_reviewer_2.json",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml",
      "config/mcp_config_review_director.json",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_report.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md",
      "projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/CLAUDE.md",
      "projects/xling_calib_direction/.claude/sessions/review_reviewer_2_dfeebd74/AGENTS.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/review_report.md",
      "projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/meta.yaml",
      "projects/xling_calib_direction/external_review_state.json",
      "projects/xling_calib_direction/artifacts/review_issues.yaml",
      "projects/xling_calib_direction/artifacts/review_reports/round_0.md",
      "projects/xling_calib_direction/logs/workers/worker_analysis_temp_scaling_leakage_fix_20260520T201907_result.json",
      "projects/xling_calib_direction/logs/workers/worker_code_cka_pilot_20260520T201949_result.json",
      "projects/xling_calib_direction/checkpoints/mvp_003_RUNNING_20260520T203425.json"
    ],
    "durationMs": 12,
    "numFiles": 100,
    "truncated": true
  },
  "sourceToolAssistantUUID": "e731d15c-656b-41db-92a6-9d447619761e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T04:53:53.605Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BZUjaw2t3CjsLiBMezPKk1`</summary>

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
  "parentUuid": "108a16e8-7e73-4fa3-8a27-4216d298bf56",
  "isSidechain": false,
  "requestId": "req_011CbF7hsgrFfK7E61Punr95",
  "type": "assistant",
  "uuid": "e2c92c38-ebac-43fd-b3a2-a731f5f1f5ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8JDMko4gaHkdrHWtqGw6a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4698,
      "cache_read_input_tokens": 29062,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 29062,
          "cache_creation_input_tokens": 4698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4698
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

_source line 13 · 2026-05-21T04:53:53.896Z_

<details><summary>↩ Tool result · `toolu_01BZUjaw2t3CjsLiBMezPKk1`</summary>

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
  "parentUuid": "e2c92c38-ebac-43fd-b3a2-a731f5f1f5ce",
  "isSidechain": false,
  "promptId": "71f7a31c-faf5-4838-a851-ebac678d912c",
  "type": "user",
  "uuid": "c3d957e5-656f-43c6-9d75-8fff068ca0bb",
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
  "sourceToolAssistantUUID": "e2c92c38-ebac-43fd-b3a2-a731f5f1f5ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T04:53:54.209Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SGCSdmDLXoUvRzkUBLw8z9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3d957e5-656f-43c6-9d75-8fff068ca0bb",
  "isSidechain": false,
  "requestId": "req_011CbF7hsgrFfK7E61Punr95",
  "type": "assistant",
  "uuid": "1d8145de-31e7-4ccb-b736-97ac9ec5006f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8JDMko4gaHkdrHWtqGw6a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4698,
      "cache_read_input_tokens": 29062,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 29062,
          "cache_creation_input_tokens": 4698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4698
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

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：核心几何洞见（Simpson's Paradox）在双架构 × 20 语言上显著复现；CaCLR consistency loss 提供可测量迁移增益；所有 claims 完整保留 核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均显著 (p < 0.01…",
  "leafUuid": "1d8145de-31e7-4ccb-b736-97ac9ec5006f",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Simpson's Paradox reveals cross-lingual correctness probe transfer",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Tool result

_source line 17 · 2026-05-21T04:53:54.535Z_

<details><summary>↩ Tool result · `toolu_01SGCSdmDLXoUvRzkUBLw8z9`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B",
4	    "description": "Extract activations at every 4th layer (24 probed layers out of 94), 20 languages, train English correctness probes (logistic regression + 2-layer MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\n",
5	    "results": {
6	      "en_auroc_best_layer": 0.843,
7	      "en_best_layer_idx": 72,
8	      "en_auroc_range": [
9	        0.621,
10	        0.843
11	      ],
12	      "en_ece_raw_best": 0.162,
13	      "en_ece_tempcal_best": 0.054,
14	      "temp_scaling_T": 4.87,
15	      "zs_transfer_auroc_mean_19lang_best_transfer_layer": 0.762,
16	      "zs_best_transfer_layer_idx": 56,
17	      "zs_transfer_drop_from_en_mean_pp": 8.1,
18	      "zs_auroc_by_tier": {
19	        "high_resource_mean": 0.791,
20	        "mid_resource_mean": 0.754,
21	        "low_resource_mean": 0.683
22	      },
23	      "zs_auroc_by_lang": {
24	        "en": 0.843,
25	        "zh": 0.802,
26	        "de": 0.796,
27	        "fr": 0.793,
28	        "es": 0.789,
29	        "ja": 0.785,
30	        "ru": 0.782,
31	        "pt": 0.788,
32	        "it": 0.786,
33	        "ar": 0.768,
34	        "hi": 0.761,
35	        "ko": 0.755,
36	        "vi": 0.749,
37	        "th": 0.743,
38	        "bn": 0.738,
39	        "tr": 0.756,
40	        "nl": 0.79,
41	        "sw": 0.695,
42	        "yo": 0.672,
43	        "ig": 0.681
44	      },
45	      "mean_shift_improvement_count": 2,
46	      "mean_shift_delta_ece_mean": 1.41,
47	      "linproj_auroc_mean_19lang": 0.724,
48	      "fewshot_25_auroc_mean_19lang": 0.748,
49	      "fewshot_100_auroc_mean_19lang": 0.771,
50	      "pareto_depth_transfer_rank_corr": 0.88,
51	      "pareto_frontier_layers": [
52	        40,
53	        44,
54	        48,
55	        52,
56	        56,
57	        60
58	      ],
59	      "layers_above_0p5_auroc_count": 22
60	    },
61	    "tables": [
62	      {
63	        "name": "Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer",
64	        "columns": [
65	          "layer_idx",
66	          "layer_depth_pct",
67	          "en_auroc",
68	          "zs_mean_auroc_19",
69	          "zs_drop_pp",
70	          "on_pareto"
71	        ],
72	        "rows": [
73	          [
74	            4,
75	            4,
76	            0.621,
77	            0.608,
78	            1.3,
79	            false
80	          ],
81	          [
82	            8,
83	            9,
84	            0.648,
85	            0.637,
86	            1.1,
87	            false
88	          ],
89	          [
90	            12,
91	            13,
92	            0.689,
93	            0.671,
94	            1.8,
95	            false
96	          ],
97	          [
98	            16,
99	            17,
100	            0.712,
101	            0.698,
102	            1.4,
103	            false
104	          ],
105	          [
106	            20,
107	            21,
108	            0.738,
109	            0.724,
110	            1.4,
111	            false
112	          ],
113	          [
114	            24,
115	            26,
116	            0.756,
117	            0.742,
118	            1.4,
119	            false
120	          ],
121	          [
122	            28,
123	            30,
124	            0.771,
125	            0.755,
126	            1.6,
127	            false
128	          ],
129	          [
130	            32,
131	            34,
132	            0.784,
133	            0.764,
134	            2.0,
135	            false
136	          ],
137	          [
138	            36,
139	            38,
140	            0.795,
141	            0.771,
142	            2.4,
143	            false
144	          ],
145	          [
146	            40,
147	            43,
148	            0.803,
149	            0.776,
150	            2.7,
151	            true
152	          ],
153	          [
154	            44,
155	            47,
156	            0.81,
157	            0.774,
158	            3.6,
159	            true
160	          ],
161	          [
162	            48,
163	            51,
164	            0.816,
165	            0.77,
166	            4.6,
167	            true
168	          ],
169	          [
170	            52,
171	            55,
172	            0.822,
173	            0.765,
174	            5.7,
175	            true
176	          ],
177	          [
178	            56,
179	            60,
180	            0.827,
181	            0.762,
182	            6.5,
183	            true
184	          ],
185	          [
186	            60,
187	            64,
188	            0.831,
189	            0.753,
190	            7.8,
191	            true
192	          ],
193	          [
194	            64,
195	            68,
196	            0.835,
197	            0.741,
198	            9.4,
199	            false
200	          ],
201	          [
202	            68,
203	            72,
204	            0.839,
205	            0.728,
206	            11.1,
207	            false
208	          ],
209	          [
210	            72,
211	            77,
212	            0.843,
213	            0.712,
214	            13.1,
215	            false
216	          ],
217	          [
218	            76,
219	            81,
220	            0.841,
221	            0.694,
222	            14.7,
223	            false
224	          ],
225	          [
226	            80,
227	            85,
228	            0.838,
229	            0.671,
230	            16.7,
231	            false
232	          ],
233	          [
234	            84,
235	            89,
236	            0.832,
237	            0.643,
238	            18.9,
239	            false
240	          ],
241	          [
242	            88,
243	            94,
244	            0.819,
245	            0.611,
246	            20.8,
247	            false
248	          ],
249	          [
250	            92,
251	            98,
252	            0.791,
253	            0.574,
254	            21.7,
255	            false
256	          ],
257	          [
258	            94,
259	            100,
260	            0.762,
261	            0.541,
262	            22.1,
263	            false
264	          ]
265	        ]
266	      },
267	      {
268	        "name": "Table 2: Transfer Condition Comparison (at best-transfer layer L56)",
269	        "columns": [
270	          "condition",
271	          "auroc_mean_19",
272	          "ece_mean_19",
273	          "ece_reduction_vs_tempcal_pct"
274	        ],
275	        "rows": [
276	          [
277	            "zero-shot",
278	            0.762,
279	            0.098,
280	            0
281	          ],
282	          [
283	            "mean-shift",
284	            0.758,
285	            0.101,
286	            -3.1
287	          ],
288	          [
289	            "linear_projection",
290	            0.781,
291	            0.082,
292	            16.3
293	          ],
294	          [
295	            "few-shot-25",
296	            0.748,
297	            0.089,
298	            9.2
299	          ],
300	          [
301	            "few-shot-100",
302	            0.771,
303	            0.079,
304	            19.4
305	          ],
306	          [
307	            "CaCLR",
308	            0.814,
309	            0.058,
310	            40.8
311	          ]
312	        ]
313	      }
314	    ],
315	    "figures": [],
316	    "analysis": "The Pareto frontier is crisp and monotonic: 6 layers form the efficient frontier between L40-L60. The rank correlation (Spearman) between layer depth and transfer degradation is ρ=0.88 (p<0.001). The frontier's shape confirms that the depth- transferability tradeoff is not an artifact of small models — it amplifies at scale. The 16pp gap between best-EN layer (L72) and best-transfer layer (L56) is larger than MVP's ~3-layer gap, consistent with deeper models having more room for language-specific specialization. All high-resource languages pass AUROC > 0.75 at the best-transfer layer; all low-resource languages exceed 0.65.\n\n\nQwen3-235B-A22B is a 94-layer MoE with massive representation capacity. The jump from MVP's 7B (en AUROC 0.754) to 235B is expected to yield ~9pp AUROC gain, consistent with prior probing literature showing log-linear scaling of linear probe accuracy with model parameters (Burns et al., Marks et al.). The MoE architecture concentrates expert representations, producing cleaner correctness signals in intermediate layers. The Pareto frontier emerges because deeper layers (L72+) specialize for English-dominant pretraining data distribution — the model's language-specific processing intensifies past ~75% depth, degrading cross-lingual invariance. The best transfer layer (L56, ~60% depth) sits in the \"universal reasoning\" zone before language-specific heads activate. Low-resource languages (sw, yo, ig) still transfer above 0.65 AUROC because GlobalMMLU questions share structural patterns that even underrepresented languages partially align with in middle layers. Mean-shift continues to mostly fail because correctness directions are not simply mean-offset between languages — they require rotation, not translation, which linear projection and CaCLR address.\n"
317	  },
318	  {
319	    "name": "Full Pareto Frontier — Llama 4 Scout",
320	    "description": "Extract activations at every 4th layer (12 probed layers out of 48), 20 languages, 5 transfer conditions. INT8 weight quantization.\n",
321	    "results": {
322	      "en_auroc_best_layer": 0.821,
323	      "en_best_layer_idx": 36,
324	      "en_auroc_range": [
325	        0.634,
326	        0.821
327	      ],
328	      "en_ece_raw_best": 0.174,
329	      "en_ece_tempcal_best": 0.061,
330	      "temp_scaling_T": 5.34,
331	      "zs_transfer_auroc_mean_19lang_best_transfer_layer": 0.741,
332	      "zs_best_transfer_layer_idx": 28,
333	      "zs_transfer_drop_from_en_mean_pp": 8.0,
334	      "zs_auroc_by_tier": {
335	        "high_resource_mean": 0.771,
336	        "mid_resource_mean": 0.733,
337	        "low_resource_mean": 0.661
338	      },
339	      "zs_auroc_by_lang": {
340	        "en": 0.821,
341	        "zh": 0.784,
342	        "de": 0.778,
343	        "fr": 0.775,
344	        "es": 0.771,
345	        "ja": 0.766,
346	        "ru": 0.762,
347	        "pt": 0.77,
348	        "it": 0.768,
349	        "ar": 0.748,
350	        "hi": 0.741,
351	        "ko": 0.735,
352	        "vi": 0.729,
353	        "th": 0.722,
354	        "bn": 0.718,
355	        "tr": 0.737,
356	        "nl": 0.772,
357	        "sw": 0.674,
358	        "yo": 0.641,
359	        "ig": 0.667
360	      },
361	      "mean_shift_improvement_count": 1,
362	      "linproj_auroc_mean_19lang": 0.706,
363	      "fewshot_25_auroc_mean_19lang": 0.728,
364	      "fewshot_100_auroc_mean_19lang": 0.752,
365	      "pareto_depth_transfer_rank_corr": 0.82,
366	      "pareto_frontier_layers": [
367	        20,
368	        24,
369	        28,
370	        32
371	      ]
372	    },
373	    "tables": [
374	      {
375	        "name": "Table 3: Llama 4 Scout Pareto Frontier",
376	        "columns": [
377	          "layer_idx",
378	          "layer_depth_pct",
379	          "en_auroc",
380	          "zs_mean_auroc_19",
381	          "zs_drop_pp",
382	          "on_pareto"
383	        ],
384	        "rows": [
385	          [
386	            4,
387	            8,
388	            0.634,
389	            0.624,
390	            1.0,
391	            false
392	          ],
393	          [
394	            8,
395	            17,
396	            0.672,
397	            0.659,
398	            1.3,
399	            false
400	          ],
401	          [
402	            12,
403	            25,
404	            0.714,
405	            0.699,
406	            1.5,
407	            false
408	          ],
409	          [
410	            16,
411	            33,
412	            0.745,
413	            0.729,
414	            1.6,
415	            false
416	          ],
417	          [
418	            20,
419	            42,
420	            0.768,
421	            0.748,
422	            2.0,
423	            true
424	          ],
425	          [
426	            24,
427	            50,
428	            0.786,
429	            0.745,
430	            4.1,
431	            true
432	          ],
433	          [
434	            28,
435	            58,
436	            0.798,
437	            0.741,
438	            5.7,
439	            true
440	          ],
441	          [
442	            32,
443	            67,
444	            0.81,
445	            0.732,
446	            7.8,
447	            true
448	          ],
449	          [
450	            36,
451	            75,
452	            0.821,
453	            0.714,
454	            10.7,
455	            false
456	          ],
457	          [
458	            40,
459	            83,
460	            0.818,
461	            0.689,
462	            12.9,
463	            false
464	          ],
465	          [
466	            44,
467	            92,
468	            0.804,
469	            0.651,
470	            15.3,
471	            false
472	          ],
473	          [
474	            48,
475	            100,
476	            0.771,
477	            0.608,
478	            16.3,
479	            false
480	          ]
481	        ]
482	      },
483	      {
484	        "name": "Table 4: Cross-Architecture Pareto Frontier Agreement",
485	        "columns": [
486	          "metric",
487	          "qwen3_235b",
488	          "llama4_scout",
489	          "agreement"
490	        ],
491	        "rows": [
492	          [
493	            "best_en_layer_depth_pct",
494	            77,
495	            75,
496	            "within 2pp"
497	          ],
498	          [
499	            "best_transfer_layer_depth_pct",
500	            60,
501	            58,
502	            "within 2pp"
503	          ],
504	          [
505	            "pareto_zone_depth_range_pct",
506	            "43-64",
507	            "42-67",
508	            "overlapping"
509	          ],
510	          [
511	            "depth_transfer_rank_corr",
512	            0.88,
513	            0.82,
514	            "both >0.75"
515	          ],
516	          [
517	            "frontier_shape",
518	            "convex monotonic",
519	            "convex monotonic",
520	            "consistent"
521	          ]
522	        ]
523	      }
524	    ],
525	    "figures": [],
526	    "analysis": "Cross-architecture agreement is high: both models show best transfer at ~59% depth, the Pareto frontier occupies the 42-67% depth band, and the rank correlation between depth and transfer degradation exceeds 0.75 in both. The frontier shape is architecture-invariant — it's the depth-normalized position, not absolute layer count, that determines the tradeoff. This validates Claim 1 at scale.\n\n\nLlama 4 Scout has 48 layers (fewer than Qwen3's 94) and a different MoE routing strategy (16 experts, top-2). With roughly 109B total / ~17B active params, its active compute is smaller than Qwen3-235B's ~22B active. This yields ~2pp lower EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer points (4 vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but the monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout's best transfer layer sits at ~58% depth (L28), remarkably close to Qwen3's 60%, suggesting a universal \"mid-depth transfer zone\" across architectures. The rank correlation is slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant. Low-resource languages are slightly weaker because Meta's multilingual pretraining mix underrepresents African languages compared to Qwen3.\n"
527	  },
528	  {
529	    "name": "CaCLR Implementation and Comparative Evaluation",
530	    "description": "CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train on English labels + unlabeled parallel activations. Compare vs all 5 conditions across full Pareto frontier, both models × 20 languages. Hyperparameter tuning (α, β).\n",
531	    "results": {
532	      "best_alpha": 0.15,
533	      "best_beta": 0.08,
534	      "qwen3_caclr_auroc_mean_19lang": 0.814,
535	      "qwen3_caclr_ece_mean_19lang": 0.058,
536	      "qwen3_caclr_vs_linproj_auroc_delta_pp": 3.3,
537	      "qwen3_caclr_vs_zeroshot_auroc_delta_pp": 5.2,
538	      "qwen3_caclr_ece_reduction_vs_tempcal_pct": 40.8,
539	      "qwen3_caclr_best_operating_layer": 64,
540	      "llama4_caclr_auroc_mean_19lang": 0.793,
541	      "llama4_caclr_ece_mean_19lang": 0.064,
542	      "llama4_caclr_vs_linproj_auroc_delta_pp": 3.1,
543	      "llama4_caclr_vs_zeroshot_auroc_delta_pp": 5.2,
544	      "llama4_caclr_ece_reduction_vs_tempcal_pct": 38.5,
545	      "llama4_caclr_best_operating_layer": 32,
546	      "caclr_vs_linproj_auroc_delta_pp_mean": 3.2,
547	      "caclr_ece_reduction_vs_tempcal_pct_mean": 39.7,
548	      "caclr_improvement_pass_rate": 0.92,
549	      "caclr_pareto_shift_layers": 2,
550	      "low_resource_caclr_auroc": {
551	        "sw_qwen3": 0.731,
552	        "yo_qwen3": 0.709,
553	        "ig_qwen3": 0.718,
554	        "sw_llama4": 0.712,
555	        "yo_llama4": 0.681,
556	        "ig_llama4": 0.698
557	      },
558	      "low_resource_zs_pass_rate": 1.0
559	    },
560	    "tables": [
561	      {
562	        "name": "Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)",
563	        "columns": [
564	          "method",
565	          "auroc_mean_19",
566	          "ece_mean_19",
567	          "requires_target_labels",
568	          "params_overhead"
569	        ],
570	        "rows": [
571	          [
572	            "zero-shot",
573	            0.752,
574	            0.098,
575	            "no",
576	            "0"
577	          ],
578	          [
579	            "mean-shift",
580	            0.747,
581	            0.102,
582	            "no",
583	            "0"
584	          ],
585	          [
586	            "linear_projection",
587	            0.77,
588	            0.082,
589	            "no",
590	            "d×d matrix"
591	          ],
592	          [
593	            "few-shot-25",
594	            0.738,
595	            0.089,
596	            "yes (25)",
597	            "0"
598	          ],
599	          [
600	            "few-shot-100",
601	            0.762,
602	            0.079,
603	            "yes (100)",
604	            "0"
605	          ],
606	          [
607	            "CaCLR",
608	            0.804,
609	            0.061,
610	            "no",
611	            "~1% probe params"
612	          ]
613	        ]
614	      },
615	      {
616	        "name": "Table 6: CaCLR Ablation — Loss Component Contributions",
617	        "columns": [
618	          "configuration",
619	          "auroc_mean_19",
620	          "ece_mean_19",
621	          "delta_vs_full_auroc_pp"
622	        ],
623	        "rows": [
624	          [
625	            "L_BCE_only (= zero-shot probe)",
626	            0.752,
627	            0.098,
628	            -5.2
629	          ],
630	          [
631	            "L_BCE + L_SB-ECE",
632	            0.768,
633	            0.072,
634	            -3.6
635	          ],
636	          [
637	            "L_BCE + L_consistency",
638	            0.793,
639	            0.078,
640	            -1.1
641	          ],
642	          [
643	            "L_BCE + L_SB-ECE + L_consistency (full CaCLR)",
644	            0.804,
645	            0.061,
646	            0.0
647	          ]
648	        ]
649	      },
650	      {
651	        "name": "Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)",
652	        "columns": [
653	          "layer_idx",
654	          "zs_auroc_19",
655	          "caclr_auroc_19",
656	          "shift_pp",
657	          "on_shifted_pareto"
658	        ],
659	        "rows": [
660	          [
661	            40,
662	            0.776,
663	            0.798,
664	            2.2,
665	            false
666	          ],
667	          [
668	            44,
669	            0.774,
670	            0.8,
671	            2.6,
672	            false
673	          ],
674	          [
675	            48,
676	            0.77,
677	            0.803,
678	            3.3,
679	            true
680	          ],
681	          [
682	            52,
683	            0.765,
684	            0.806,
685	            4.1,
686	            true
687	          ],
688	          [
689	            56,
690	            0.762,
691	            0.81,
692	            4.8,
693	            true
694	          ],
695	          [
696	            60,
697	            0.753,
698	            0.814,
699	            6.1,
700	            true
701	          ],
702	          [
703	            64,
704	            0.741,
705	            0.814,
706	            7.3,
707	            true
708	          ],
709	          [
710	            68,
711	            0.728,
712	            0.808,
713	            8.0,
714	            true
715	          ],
716	          [
717	            72,
718	            0.712,
719	            0.796,
720	            8.4,
721	            false
722	          ]
723	        ]
724	      }
725	    ],
726	    "figures": [],
727	    "analysis": "CaCLR decisively outperforms all baselines. The ablation shows both loss terms contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp alone), while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to 0.061 when added). The interaction is synergistic — joint optimization yields better results than either term alone. The Pareto shift is the headline result: at the same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation from \"use shallower layers for transfer\" to \"use CaCLR and operate at deeper, better-calibrated layers.\" The improvement pass rate of 92% (35/38 model-lang pairs) demonstrates consistency. The 3 non-improving pairs are high-resource languages (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already excellent and the consistency loss has minimal signal to exploit.\n\n\nCaCLR's consistency loss (β·L_consistency) directly penalizes divergence between EN and non-EN probe outputs on parallel/comparable activations, forcing the probe to learn language-invariant features. This is strictly more informative than linear projection (which only aligns means and covariances post-hoc) because it shapes the learned representation during training. The 3.2pp AUROC gain over linear projection reflects the value of end-to-end optimization: linear projection corrects first-order distributional mismatch but not the nonlinear feature interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE) provides calibration-aware training that temperature scaling cannot — it directly optimizes the calibration objective rather than post-hoc rescaling. The 40% ECE reduction over temperature scaling arises because CaCLR addresses the root cause (representation misalignment) rather than the symptom (miscalibrated probabilities). The Pareto frontier shift is the key result: CaCLR allows operating 2 layers deeper than the ZS-optimal point while maintaining equivalent or better transfer — it literally pushes the Pareto frontier outward. Low-resource languages benefit most from L_consistency because their activation distributions are most misaligned from EN; the consistency term provides the strongest gradient signal precisely where the gap is largest.\n"
728	  },
729	  {
730	    "name": "Difficulty-Controlled Ablation",
731	    "description": "IRT difficulty probes (Ridge regression), project out difficulty direction, retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers per model.\n",
732	    "results": {
733	      "difficulty_probe_r2_mean": 0.72,
734	      "difficulty_var_explained_pct_mean": 68.4,
735	      "difficulty_var_explained_pct_range": [
736	        58.2,
737	        79.1
738	      ],
739	      "residual_en_auroc_drop_pp": 4.2,
740	      "residual_zs_transfer_drop_pp": 1.1,
741	      "capability_specific_var_pct": 31.6,
742	      "capability_specific_transfer_degradation_pct": 87,
743	      "difficulty_component_transfer_degradation_pct": 13,
744	      "decomp_prescriptive_accuracy": 0.81,
745	      "difficulty_var_by_depth": {
746	        "shallow_20pct": 0.74,
747	        "mid_50pct": 0.69,
748	        "deep_80pct": 0.62
749	      },
750	      "capability_transfer_drop_by_depth": {
751	        "shallow_20pct": 0.8,
752	        "mid_50pct": 3.4,
753	        "deep_80pct": 9.7
754	      }
755	    },
756	    "tables": [
757	      {
758	        "name": "Table 8: Decomposition Results — Difficulty vs Capability Components",
759	        "columns": [
760	          "component",
761	          "var_explained_pct",
762	          "transfer_auroc_mean",
763	          "transfer_drop_from_en_pp",
764	          "share_of_total_transfer_drop_pct"
765	        ],
766	        "rows": [
767	          [
768	            "full_correctness",
769	            100,
770	            0.752,
771	            8.1,
772	            100
773	          ],
774	          [
775	            "difficulty_shared",
776	            68.4,
777	            0.738,
778	            1.1,
779	            13
780	          ],
781	          [
782	            "capability_specific",
783	            31.6,
784	            0.614,
785	            14.2,
786	            87
787	          ]
788	        ]
789	      },
790	      {
791	        "name": "Table 9: Capability-Specific Transfer Drop by Depth",
792	        "columns": [
793	          "depth_band",
794	          "difficulty_transfer_drop_pp",
795	          "capability_transfer_drop_pp",
796	          "ratio"
797	        ],
798	        "rows": [
799	          [
800	            "0-30%",
801	            0.3,
802	            0.8,
803	            "2.7×"
804	          ],
805	          [
806	            "30-60%",
807	            0.8,
808	            3.4,
809	            "4.3×"
810	          ],
811	          [
812	            "60-90%",
813	            1.6,
814	            9.7,
815	            "6.1×"
816	          ]
817	        ]
818	      }
819	    ],
820	    "figures": [],
821	    "analysis": "The decomposition cleanly separates: difficulty-shared signal is the majority (68%) of correctness variance and transfers near-perfectly across languages and depths. The capability-specific residual (32%) drives nearly all transfer degradation (87%), and this degradation accelerates exponentially with depth. This explains the Pareto frontier mechanistically: deeper layers have stronger capability-specific signals that improve EN calibration but impede transfer. CaCLR works because its consistency loss specifically targets the capability-specific component — forcing alignment of the non-difficulty residual across languages. The prescriptive value (81% accuracy in predicting when CaCLR is needed) confirms this is a load-bearing decomposition, not a post-hoc narrative.\n\n\nIRT difficulty is a strong, language-agnostic property — harder questions are harder everywhere. Ridge regression captures this cleanly (R²=0.72) because difficulty is linearly encoded in intermediate representations (Civelli et al. confirmed this). The difficulty component accounts for 68% of explained variance because GlobalMMLU correctness is heavily driven by item difficulty: a model gets easy questions right in all languages and hard questions wrong in all languages. After projecting out difficulty, the residual correctness signal is \"capability-specific\" — it captures language-dependent competence differences. This residual transfers poorly at deep layers (9.7pp drop at 80% depth vs 0.8pp at 20% depth) because deep layers encode language-specific processing that makes capability assessments non-transferable. The difficulty component transfers well at all depths (only 13% of total transfer degradation) because it's language-invariant by construction. This decomposition is prescriptive: when difficulty explains most of a language's correctness variance, simple zero-shot transfer suffices; when the capability residual is large, CaCLR is needed. The 81% prescriptive accuracy validates the decomposition as more than descriptive.\n"
822	  },
823	  {
824	    "name": "Cross-Lingual Orthogonality Analysis",
825	    "description": "Extract verbalized confidence direction via prompted confidence scores, compute cosine similarity with correctness direction across 20 languages × 2 architectures. Analyze by resource tier and language family.\n",
826	    "results": {
827	      "orthogonality_cosine_mean_overall": 0.052,
828	      "orthogonality_cosine_range": [
829	        0.018,
830	        0.094
831	      ],
832	      "orthogonality_cosine_en": 0.034,
833	      "qwen3_cosine_mean": 0.048,
834	      "llama4_cosine_mean": 0.057,
835	      "high_resource_cosine_mean": 0.041,
836	      "mid_resource_cosine_mean": 0.054,
837	      "low_resource_cosine_mean": 0.074,
838	      "cosine_by_lang": {
839	        "en": 0.034,
840	        "zh": 0.038,
841	        "de": 0.036,
842	        "fr": 0.039,
843	        "es": 0.041,
844	        "ja": 0.044,
845	        "ru": 0.043,
846	        "pt": 0.04,
847	        "it": 0.042,
848	        "ar": 0.051,
849	        "hi": 0.055,
850	        "ko": 0.049,
851	        "vi": 0.058,
852	        "th": 0.061,
853	        "bn": 0.056,
854	        "tr": 0.052,
855	        "nl": 0.037,
856	        "sw": 0.078,
857	        "yo": 0.094,
858	        "ig": 0.082
859	      },
860	      "all_langs_below_0p1": true,
861	      "cosine_resource_tier_correlation": -0.68
862	    },
863	    "tables": [
864	      {
865	        "name": "Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture",
866	        "columns": [
867	          "language",
868	          "resource_tier",
869	          "qwen3_cosine",
870	          "llama4_cosine",
871	          "mean_cosine"
872	        ],
873	        "rows": [
874	          [
875	            "en",
876	            "high",
877	            0.031,
878	            0.037,
879	            0.034
880	          ],
881	          [
882	            "zh",
883	            "high",
884	            0.035,
885	            0.041,
886	            0.038
887	          ],
888	          [
889	            "de",
890	            "high",
891	            0.033,
892	            0.039,
893	            0.036
894	          ],
895	          [
896	            "fr",
897	            "high",
898	            0.036,
899	            0.042,
900	            0.039
901	          ],
902	          [
903	            "es",
904	            "high",
905	            0.038,
906	            0.044,
907	            0.041
908	          ],
909	          [
910	            "ja",
911	            "high",
912	            0.041,
913	            0.047,
914	            0.044
915	          ],
916	          [
917	            "ru",
918	            "high",
919	            0.04,
920	            0.046,
921	            0.043
922	          ],
923	          [
924	            "pt",
925	            "high",
926	            0.037,
927	            0.043,
928	            0.04
929	          ],
930	          [
931	            "it",
932	            "high",
933	            0.039,
934	            0.045,
935	            0.042
936	          ],
937	          [
938	            "nl",
939	            "high",
940	            0.034,
941	            0.04,
942	            0.037
943	          ],
944	          [
945	            "ar",
946	            "mid",
947	            0.047,
948	            0.055,
949	            0.051
950	          ],
951	          [
952	            "hi",
953	            "mid",
954	            0.051,
955	            0.059,
956	            0.055
957	          ],
958	          [
959	            "ko",
960	            "mid",
961	            0.045,
962	            0.053,
963	            0.049
964	          ],
965	          [
966	            "vi",
967	            "mid",
968	            0.054,
969	            0.062,
970	            0.058
971	          ],
972	          [
973	            "th",
974	            "mid",
975	            0.057,
976	            0.065,
977	            0.061
978	          ],
979	          [
980	            "bn",
981	            "mid",
982	            0.052,
983	            0.06,
984	            0.056
985	          ],
986	          [
987	            "tr",
988	            "mid",
989	            0.048,
990	            0.056,
991	            0.052
992	          ],
993	          [
994	            "sw",
995	            "low",
996	            0.073,
997	            0.083,
998	            0.078
999	          ],
1000	          [
1001	            "yo",
1002	            "low",
1003	            0.089,
1004	            0.099,
1005	            0.094
1006	          ],
1007	          [
1008	            "ig",
1009	            "low",
1010	            0.077,
1011	            0.087,
1012	            0.082
1013	          ]
1014	        ]
1015	      },
1016	      {
1017	        "name": "Table 11: Orthogonality Summary Statistics",
1018	        "columns": [
1019	          "statistic",
1020	          "qwen3_235b",
1021	          "llama4_scout",
1022	          "both_models"
1023	        ],
1024	        "rows": [
1025	          [
1026	            "cosine_mean",
1027	            0.048,
1028	            0.057,
1029	            0.052
1030	          ],
1031	          [
1032	            "cosine_std",
1033	            0.015,
1034	            0.017,
1035	            0.016
1036	          ],
1037	          [
1038	            "cosine_max",
1039	            0.089,
1040	            0.099,
1041	            0.094
1042	          ],
1043	          [
1044	            "cosine_min",
1045	            0.031,
1046	            0.037,
1047	            0.018
1048	          ],
1049	          [
1050	            "all_below_0.1",
1051	            "yes (20/20)",
1052	            "yes (19/20)",
1053	            "39/40"
1054	          ],
1055	          [
1056	            "resource_tier_corr",
1057	            -0.71,
1058	            -0.65,
1059	            -0.68
1060	          ]
1061	        ]
1062	      }
1063	    ],
1064	    "figures": [],
1065	    "analysis": "Orthogonality generalizes comprehensively. The mean cosine of 0.052 across all 40 language-architecture pairs is well within the \"near-orthogonal\" regime (< 0.1). The resource-tier gradient is the novel finding: it suggests that output-based calibration methods are not just structurally limited but are *more* limited for well-resourced languages where the orthogonality is strongest. This strengthens the motivation for probe-based approaches universally and for CaCLR specifically in multilingual settings. Yoruba's 0.094 is the only value approaching the 0.1 threshold (on Llama4 it hits 0.099), which is worth noting but does not break the claim.\n\n\nMiao & Ungar (2026) established correctness-confidence orthogonality (cosine < 0.04) for English on 7-8B models. We extend to 20 languages on larger models. The orthogonality persists universally (all < 0.1) because it reflects a fundamental architectural property: verbalized confidence is generated by the language modeling head from surface-level token probabilities, while correctness is encoded in intermediate representation geometry. These are structurally decoupled in transformer architectures. The slight increase in cosine for low-resource languages (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages have noisier confidence elicitation — the model's verbalized confidence in Yoruba is less well-calibrated and leaks some correctness signal, producing weak correlation. The resource-tier gradient (ρ=-0.68) suggests that better multilingual training data produces cleaner separation between correctness and confidence representations. The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this is not architecture-specific. Llama 4's slightly higher cosines may reflect its less aggressive multilingual pretraining compared to Qwen3.\n"
1066	  },
1067	  {
1068	    "name": "Probe Complexity Comparison",
1069	    "description": "Logistic regression vs 2-layer MLP at each probed layer, both models. Compare English accuracy, cross-lingual transfer degradation, calibration quality.\n",
1070	    "results": {
1071	      "logreg_en_auroc_best": 0.843,
1072	      "mlp_en_auroc_best": 0.856,
1073	      "mlp_en_auroc_gain_pp": 1.3,
1074	      "logreg_zs_transfer_drop_mean_pp": 8.1,
1075	      "mlp_zs_transfer_drop_mean_pp": 12.4,
1076	      "transfer_degradation_ratio": 1.53,
1077	      "logreg_ece_mean": 0.054,
1078	      "mlp_ece_mean": 0.068,
1079	      "logreg_transfer_advantage_shallow_pp": 2.1,
1080	      "logreg_transfer_advantage_deep_pp": 6.8
1081	    },
1082	    "tables": [
1083	      {
1084	        "name": "Table 12: Probe Complexity Comparison",
1085	        "columns": [
1086	          "probe_type",
1087	          "en_auroc_best",
1088	          "zs_auroc_mean_19",
1089	          "zs_drop_pp",
1090	          "ece_mean_19"
1091	        ],
1092	        "rows": [
1093	          [
1094	            "logistic_regression",
1095	            0.843,
1096	            0.762,
1097	            8.1,
1098	            0.054
1099	          ],
1100	          [
1101	            "mlp_2layer",
1102	            0.856,
1103	            0.733,
1104	            12.4,
1105	            0.068
1106	          ]
1107	        ]
1108	      }
1109	    ],
1110	    "figures": [],
1111	    "analysis": "Linear probes are the correct choice for cross-lingual transfer: they sacrifice 1.3pp EN AUROC but gain 4.3pp average transfer. The depth interaction effect is notable — the logreg advantage grows from 2.1pp at shallow layers to 6.8pp at deep layers, confirming that deep-layer transfer degradation is driven by nonlinear, language- specific features. CaCLR + logreg is thus the optimal configuration.\n\n\nLinear probes transfer better because they learn a single hyperplane in activation space — the hyperplane generalizes across languages when the underlying geometry is approximately shared (as it is in mid-depth layers). MLPs learn nonlinear decision boundaries that fit English-specific feature interactions, gaining ~1.3pp EN AUROC but losing ~4.3pp in transfer. The transfer gap widens at deeper layers (6.8pp advantage for logreg) because deep layers have more language-specific nonlinear structure that MLPs exploit but logreg ignores. This justifies our choice of linear probes for the main results and supports the geometric interpretation of the Pareto frontier: it's about linear subspace alignment, not complex feature interactions.\n"
1112	  },
1113	  {
1114	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
1115	    "description": "Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX (20 languages).\n",
1116	    "results": {
1117	      "belebele_zs_auroc_mean_19": 0.738,
1118	      "belebele_caclr_auroc_mean_19": 0.789,
1119	      "belebele_caclr_vs_zs_pp": 5.1,
1120	      "belebele_ece_reduction_vs_tempcal_pct": 36.2,
1121	      "mmlupx_zs_auroc_mean_19": 0.722,
1122	      "mmlupx_caclr_auroc_mean_19": 0.774,
1123	      "mmlupx_caclr_vs_zs_pp": 5.2,
1124	      "mmlupx_ece_reduction_vs_tempcal_pct": 33.8,
1125	      "caclr_benefit_cross_benchmark_cv": 0.08
1126	    },
1127	    "tables": [
1128	      {
1129	        "name": "Table 13: Cross-Benchmark Generalization",
1130	        "columns": [
1131	          "benchmark",
1132	          "zs_auroc_mean_19",
1133	          "caclr_auroc_mean_19",
1134	          "caclr_gain_pp",
1135	          "ece_reduction_pct"
1136	        ],
1137	        "rows": [
1138	          [
1139	            "GlobalMMLU",
1140	            0.752,
1141	            0.804,
1142	            5.2,
1143	            39.7
1144	          ],
1145	          [
1146	            "Belebele",
1147	            0.738,
1148	            0.789,
1149	            5.1,
1150	            36.2
1151	          ],
1152	          [
1153	            "MMLU-ProX",
1154	            0.722,
1155	            0.774,
1156	            5.2,
1157	            33.8
1158	          ]
1159	        ]
1160	      }
1161	    ],
1162	    "figures": [],
1163	    "analysis": "CaCLR generalizes cleanly across benchmarks. The improvement magnitude is remarkably stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method addresses a fundamental representation alignment issue rather than overfitting to GlobalMMLU- specific patterns. This is critical for reviewer confidence.\n\n\nBelebele tests reading comprehension (vs GlobalMMLU's factual knowledge), providing domain generalization evidence. Transfer AUROC is slightly lower (0.738 vs 0.762) because Belebele's passage-dependent questions have weaker difficulty-shared signal — comprehension difficulty is more language-dependent than factual difficulty. CaCLR still provides ~5pp improvement, confirming the consistency loss generalizes beyond factual MCQA. MMLU-ProX has harder questions that compress the AUROC distribution (lower base rate of correctness), yielding slightly lower absolute numbers but comparable CaCLR benefit. The cross-benchmark CV of 0.08 for CaCLR improvement confirms the method is robust to evaluation domain.\n"
1164	  },
1165	  {
1166	    "name": "INT8 Validation Ablation",
1167	    "description": "Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset.\n",
1168	    "results": {
1169	      "int8_fp16_auroc_diff_mean_pp": 0.3,
1170	      "int8_fp16_auroc_diff_max_pp": 0.7,
1171	      "int8_fp16_ece_diff_mean_pp": 0.2,
1172	      "int8_fp16_transfer_drop_diff_pp": 0.4,
1173	      "int8_fp16_rank_correlation": 0.997,
1174	      "conclusion": "INT8 quantization introduces negligible distortion"
1175	    },
1176	    "tables": [
1177	      {
1178	        "name": "Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)",
1179	        "columns": [
1180	          "layer_idx",
1181	          "fp16_auroc",
1182	          "int8_auroc",
1183	          "diff_pp",
1184	          "fp16_zs_auroc_5lang",
1185	          "int8_zs_auroc_5lang",
1186	          "transfer_diff_pp"
1187	        ],
1188	        "rows": [
1189	          [
1190	            8,
1191	            0.674,
1192	            0.672,
1193	            0.2,
1194	            0.661,
1195	            0.658,
1196	            0.3
1197	          ],
1198	          [
1199	            16,
1200	            0.747,
1201	            0.745,
1202	            0.2,
1203	            0.731,
1204	            0.728,
1205	            0.3
1206	          ],
1207	          [
1208	            24,
1209	            0.788,
1210	            0.786,
1211	            0.2,
1212	            0.747,
1213	            0.744,
1214	            0.3
1215	          ],
1216	          [
1217	            32,
1218	            0.812,
1219	            0.81,
1220	            0.2,
1221	            0.734,
1222	            0.731,
1223	            0.3
1224	          ],
1225	          [
1226	            40,
1227	            0.82,
1228	            0.817,
1229	            0.3,
1230	            0.691,
1231	            0.687,
1232	            0.4
1233	          ]
1234	        ]
1235	      }
1236	    ],
1237	    "figures": [],
1238	    "analysis": "INT8 quantization is validated as safe for our experimental setup. The maximum observed difference (0.7pp at a single layer-language combination) is well within the noise floor of probing experiments. The Pareto frontier ordering is perfectly preserved (rank correlation 0.997). This ablation preempts reviewer concern #5.\n\n\nINT8 weight-only quantization preserves the 8 most significant bits of each weight, introducing per-channel quantization noise of ~0.4% relative magnitude. Correctness probing relies on the geometry of activation space (direction of correctness signal), not absolute magnitudes. The quantization noise is approximately isotropic and thus preserves angular relationships between directions. The 0.3pp mean AUROC difference is within random seed variance, and the rank correlation of 0.997 between INT8 and FP16 layer rankings confirms that the Pareto frontier shape is unaffected. This result is expected given prior work showing that probing results are robust to quantization down to INT4 (Gao et al., 2024).\n"
1239	  },
1240	  {
1241	    "name": "Gemma 4 31B Dense — Third Architecture (Camera-Ready)",
1242	    "description": "Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages. Provides dense vs MoE architectural contrast.\n",
1243	    "results": {
1244	      "en_auroc_best_layer": 0.812,
1245	      "en_best_layer_idx": 45,
1246	      "zs_transfer_auroc_mean_19lang": 0.734,
1247	      "zs_best_transfer_layer_idx": 36,
1248	      "zs_transfer_drop_mean_pp": 7.8,
1249	      "pareto_depth_transfer_rank_corr": 0.86,
1250	      "caclr_auroc_mean_19lang": 0.786,
1251	      "caclr_vs_linproj_auroc_delta_pp": 2.9,
1252	      "dense_vs_moe_transfer_comparison": "comparable within 2pp",
1253	      "pareto_shape": "convex monotonic, consistent with MoE models"
1254	    },
1255	    "tables": [
1256	      {
1257	        "name": "Table 14: Three-Architecture Summary",
1258	        "columns": [
1259	          "model",
1260	          "type",
1261	          "layers",
1262	          "en_auroc_best",
1263	          "zs_auroc_mean_19",
1264	          "best_transfer_depth_pct",
1265	          "pareto_rank_corr",
1266	          "caclr_gain_pp"
1267	        ],
1268	        "rows": [
1269	          [
1270	            "Qwen3-235B-A22B",
1271	            "MoE",
1272	            94,
1273	            0.843,
1274	            0.762,
1275	            60,
1276	            0.88,
1277	            3.3
1278	          ],
1279	          [
1280	            "Llama 4 Scout",
1281	            "MoE",
1282	            48,
1283	            0.821,
1284	            0.741,
1285	            58,
1286	            0.82,
1287	            3.1
1288	          ],
1289	          [
1290	            "Gemma 4 31B Dense",
1291	            "Dense",
1292	            60,
1293	            0.812,
1294	            0.734,
1295	            60,
1296	            0.86,
1297	            2.9
1298	          ]
1299	        ]
1300	      }
1301	    ],
1302	    "figures": [],
1303	    "analysis": "The three-architecture comparison is the strongest evidence for the universality of the depth-transferability tradeoff. The best-transfer depth converges to 58-60% across dense and MoE architectures with 48-94 layers, CaCLR provides consistent 2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases. Dense vs MoE makes minimal difference — the phenomenon is a property of transformer depth, not routing architecture.\n\n\nGemma 4 31B Dense has fewer total parameters than the MoE models but all are active, yielding comparable per-token compute. As a dense model, its representations are more uniformly distributed across layers (no expert routing), producing slightly smoother Pareto frontiers. The best-transfer depth (~60%) matches both MoE models, confirming this is a universal property of transformer depth, not MoE-specific. EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B active params < 22B active with MoE routing benefits. CaCLR improvement is slightly lower (2.9pp) on the dense model because the absence of expert routing means less language-specific feature fragmentation to correct. This is the ideal third data point: different architecture family, consistent findings.\n"
1304	  },
1305	  {
1306	    "name": "Extended Language Coverage (Camera-Ready)",
1307	    "description": "Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele full language sets.\n",
1308	    "results": {
1309	      "total_languages": 52,
1310	      "new_languages_added": 32,
1311	      "zs_auroc_above_0p60_count": 48,
1312	      "zs_auroc_below_0p55_count": 2,
1313	      "caclr_improvement_positive_count": 49,
1314	      "mean_zs_auroc_51lang": 0.72,
1315	      "mean_caclr_auroc_51lang": 0.77,
1316	      "pareto_frontier_holds_all_langs": true,
1317	      "new_language_families_covered": [
1318	        "Austronesian",
1319	        "Dravidian",
1320	        "Niger-Congo B",
1321	        "Uralic",
1322	        "Kartvelian"
1323	      ]
1324	    },
1325	    "tables": [
1326	      {
1327	        "name": "Table 15: Extended Language Coverage Summary by Resource Tier",
1328	        "columns": [
1329	          "tier",
1330	          "n_langs",
1331	          "zs_auroc_mean",
1332	          "caclr_auroc_mean",
1333	          "caclr_gain_pp",
1334	          "pct_above_0p60"
1335	        ],
1336	        "rows": [
1337	          [
1338	            "high",
1339	            12,
1340	            0.782,
1341	            0.812,
1342	            3.0,
1343	            100
1344	          ],
1345	          [
1346	            "mid",
1347	            25,
1348	            0.738,
1349	            0.784,
1350	            4.6,
1351	            100
1352	          ],
1353	          [
1354	            "low",
1355	            10,
1356	            0.661,
1357	            0.712,
1358	            5.1,
1359	            90
1360	          ],
1361	          [
1362	            "very_low",
1363	            4,
1364	            0.582,
1365	            0.638,
1366	            5.6,
1367	            50
1368	          ]
1369	        ]
1370	      }
1371	    ],
1372	    "figures": [],
1373	    "analysis": "The extension to 52 languages confirms all findings at broader scale. The resource-tier gradient is smooth and predictable — no language family shows anomalous behavior. CaCLR's benefit is inversely correlated with resource level (3.0pp for high-resource to 5.6pp for very-low-resource), confirming that the consistency loss provides most value where representation misalignment is worst. The 48/51 pass rate (>0.60 AUROC) for zero-shot CaCLR transfer with no target-language labels is the practical headline for camera-ready: usable cross-lingual calibration for the vast majority of languages.\n\nExpanding to 50+ languages primarily adds mid-resource languages (Indonesian, Malay, Finnish, Georgian, Tamil, Telugu, etc.) where the model has moderate pretraining exposure. Most new languages fall in the 0.65-0.78 AUROC range, consistent with the mid-resource tier from the 20-language set. A handful of extremely low-resource languages (e.g., Amharic script languages with minimal pretraining data) may fall below 0.55, but these represent edge cases rather than systematic failures. CaCLR continues to improve 96% of languages because the consistency loss mechanism is language-agnostic — it aligns activation distributions without requiring any language-specific knowledge. The Pareto frontier structure is preserved across all 52 languages, confirming it's a depth property, not a language-set artifact.\n"
1374	  }
1375	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d8145de-31e7-4ccb-b736-97ac9ec5006f",
  "isSidechain": false,
  "promptId": "71f7a31c-faf5-4838-a851-ebac678d912c",
  "type": "user",
  "uuid": "9e4308b4-5155-49d6-b421-18fa25f490c8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B\",\n    \"description\": \"Extract activations at every 4th layer (24 probed layers out of 94), 20 languages, train English correctness probes (logistic regression + 2-layer MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.843,\n      \"en_best_layer_idx\": 72,\n      \"en_auroc_range\": [\n        0.621,\n        0.843\n      ],\n      \"en_ece_raw_best\": 0.162,\n      \"en_ece_tempcal_best\": 0.054,\n      \"temp_scaling_T\": 4.87,\n      \"zs_transfer_auroc_mean_19lang_best_transfer_layer\": 0.762,\n      \"zs_best_transfer_layer_idx\": 56,\n      \"zs_transfer_drop_from_en_mean_pp\": 8.1,\n      \"zs_auroc_by_tier\": {\n        \"high_resource_mean\": 0.791,\n        \"mid_resource_mean\": 0.754,\n        \"low_resource_mean\": 0.683\n      },\n      \"zs_auroc_by_lang\": {\n        \"en\": 0.843,\n        \"zh\": 0.802,\n        \"de\": 0.796,\n        \"fr\": 0.793,\n        \"es\": 0.789,\n        \"ja\": 0.785,\n        \"ru\": 0.782,\n        \"pt\": 0.788,\n        \"it\": 0.786,\n        \"ar\": 0.768,\n        \"hi\": 0.761,\n        \"ko\": 0.755,\n        \"vi\": 0.749,\n        \"th\": 0.743,\n        \"bn\": 0.738,\n        \"tr\": 0.756,\n        \"nl\": 0.79,\n        \"sw\": 0.695,\n        \"yo\": 0.672,\n        \"ig\": 0.681\n      },\n      \"mean_shift_improvement_count\": 2,\n      \"mean_shift_delta_ece_mean\": 1.41,\n      \"linproj_auroc_mean_19lang\": 0.724,\n      \"fewshot_25_auroc_mean_19lang\": 0.748,\n      \"fewshot_100_auroc_mean_19lang\": 0.771,\n      \"pareto_depth_transfer_rank_corr\": 0.88,\n      \"pareto_frontier_layers\": [\n        40,\n        44,\n        48,\n        52,\n        56,\n        60\n      ],\n      \"layers_above_0p5_auroc_count\": 22\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer\",\n        \"columns\": [\n          \"layer_idx\",\n          \"layer_depth_pct\",\n          \"en_auroc\",\n          \"zs_mean_auroc_19\",\n          \"zs_drop_pp\",\n          \"on_pareto\"\n        ],\n        \"rows\": [\n          [\n            4,\n            4,\n            0.621,\n            0.608,\n            1.3,\n            false\n          ],\n          [\n            8,\n            9,\n            0.648,\n            0.637,\n            1.1,\n            false\n          ],\n          [\n            12,\n            13,\n            0.689,\n            0.671,\n            1.8,\n            false\n          ],\n          [\n            16,\n            17,\n            0.712,\n            0.698,\n            1.4,\n            false\n          ],\n          [\n            20,\n            21,\n            0.738,\n            0.724,\n            1.4,\n            false\n          ],\n          [\n            24,\n            26,\n            0.756,\n            0.742,\n            1.4,\n            false\n          ],\n          [\n            28,\n            30,\n            0.771,\n            0.755,\n            1.6,\n            false\n          ],\n          [\n            32,\n            34,\n            0.784,\n            0.764,\n            2.0,\n            false\n          ],\n          [\n            36,\n            38,\n            0.795,\n            0.771,\n            2.4,\n            false\n          ],\n          [\n            40,\n            43,\n            0.803,\n            0.776,\n            2.7,\n            true\n          ],\n          [\n            44,\n            47,\n            0.81,\n            0.774,\n            3.6,\n            true\n          ],\n          [\n            48,\n            51,\n            0.816,\n            0.77,\n            4.6,\n            true\n          ],\n          [\n            52,\n            55,\n            0.822,\n            0.765,\n            5.7,\n            true\n          ],\n          [\n            56,\n            60,\n            0.827,\n            0.762,\n            6.5,\n            true\n          ],\n          [\n            60,\n            64,\n            0.831,\n            0.753,\n            7.8,\n            true\n          ],\n          [\n            64,\n            68,\n            0.835,\n            0.741,\n            9.4,\n            false\n          ],\n          [\n            68,\n            72,\n            0.839,\n            0.728,\n            11.1,\n            false\n          ],\n          [\n            72,\n            77,\n            0.843,\n            0.712,\n            13.1,\n            false\n          ],\n          [\n            76,\n            81,\n            0.841,\n            0.694,\n            14.7,\n            false\n          ],\n          [\n            80,\n            85,\n            0.838,\n            0.671,\n            16.7,\n            false\n          ],\n          [\n            84,\n            89,\n            0.832,\n            0.643,\n            18.9,\n            false\n          ],\n          [\n            88,\n            94,\n            0.819,\n            0.611,\n            20.8,\n            false\n          ],\n          [\n            92,\n            98,\n            0.791,\n            0.574,\n            21.7,\n            false\n          ],\n          [\n            94,\n            100,\n            0.762,\n            0.541,\n            22.1,\n            false\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Transfer Condition Comparison (at best-transfer layer L56)\",\n        \"columns\": [\n          \"condition\",\n          \"auroc_mean_19\",\n          \"ece_mean_19\",\n          \"ece_reduction_vs_tempcal_pct\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.762,\n            0.098,\n            0\n          ],\n          [\n            \"mean-shift\",\n            0.758,\n            0.101,\n            -3.1\n          ],\n          [\n            \"linear_projection\",\n            0.781,\n            0.082,\n            16.3\n          ],\n          [\n            \"few-shot-25\",\n            0.748,\n            0.089,\n            9.2\n          ],\n          [\n            \"few-shot-100\",\n            0.771,\n            0.079,\n            19.4\n          ],\n          [\n            \"CaCLR\",\n            0.814,\n            0.058,\n            40.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The Pareto frontier is crisp and monotonic: 6 layers form the efficient frontier between L40-L60. The rank correlation (Spearman) between layer depth and transfer degradation is ρ=0.88 (p<0.001). The frontier's shape confirms that the depth- transferability tradeoff is not an artifact of small models — it amplifies at scale. The 16pp gap between best-EN layer (L72) and best-transfer layer (L56) is larger than MVP's ~3-layer gap, consistent with deeper models having more room for language-specific specialization. All high-resource languages pass AUROC > 0.75 at the best-transfer layer; all low-resource languages exceed 0.65.\\n\\n\\nQwen3-235B-A22B is a 94-layer MoE with massive representation capacity. The jump from MVP's 7B (en AUROC 0.754) to 235B is expected to yield ~9pp AUROC gain, consistent with prior probing literature showing log-linear scaling of linear probe accuracy with model parameters (Burns et al., Marks et al.). The MoE architecture concentrates expert representations, producing cleaner correctness signals in intermediate layers. The Pareto frontier emerges because deeper layers (L72+) specialize for English-dominant pretraining data distribution — the model's language-specific processing intensifies past ~75% depth, degrading cross-lingual invariance. The best transfer layer (L56, ~60% depth) sits in the \\\"universal reasoning\\\" zone before language-specific heads activate. Low-resource languages (sw, yo, ig) still transfer above 0.65 AUROC because GlobalMMLU questions share structural patterns that even underrepresented languages partially align with in middle layers. Mean-shift continues to mostly fail because correctness directions are not simply mean-offset between languages — they require rotation, not translation, which linear projection and CaCLR address.\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout\",\n    \"description\": \"Extract activations at every 4th layer (12 probed layers out of 48), 20 languages, 5 transfer conditions. INT8 weight quantization.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.821,\n      \"en_best_layer_idx\": 36,\n      \"en_auroc_range\": [\n        0.634,\n        0.821\n      ],\n      \"en_ece_raw_best\": 0.174,\n      \"en_ece_tempcal_best\": 0.061,\n      \"temp_scaling_T\": 5.34,\n      \"zs_transfer_auroc_mean_19lang_best_transfer_layer\": 0.741,\n      \"zs_best_transfer_layer_idx\": 28,\n      \"zs_transfer_drop_from_en_mean_pp\": 8.0,\n      \"zs_auroc_by_tier\": {\n        \"high_resource_mean\": 0.771,\n        \"mid_resource_mean\": 0.733,\n        \"low_resource_mean\": 0.661\n      },\n      \"zs_auroc_by_lang\": {\n        \"en\": 0.821,\n        \"zh\": 0.784,\n        \"de\": 0.778,\n        \"fr\": 0.775,\n        \"es\": 0.771,\n        \"ja\": 0.766,\n        \"ru\": 0.762,\n        \"pt\": 0.77,\n        \"it\": 0.768,\n        \"ar\": 0.748,\n        \"hi\": 0.741,\n        \"ko\": 0.735,\n        \"vi\": 0.729,\n        \"th\": 0.722,\n        \"bn\": 0.718,\n        \"tr\": 0.737,\n        \"nl\": 0.772,\n        \"sw\": 0.674,\n        \"yo\": 0.641,\n        \"ig\": 0.667\n      },\n      \"mean_shift_improvement_count\": 1,\n      \"linproj_auroc_mean_19lang\": 0.706,\n      \"fewshot_25_auroc_mean_19lang\": 0.728,\n      \"fewshot_100_auroc_mean_19lang\": 0.752,\n      \"pareto_depth_transfer_rank_corr\": 0.82,\n      \"pareto_frontier_layers\": [\n        20,\n        24,\n        28,\n        32\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Llama 4 Scout Pareto Frontier\",\n        \"columns\": [\n          \"layer_idx\",\n          \"layer_depth_pct\",\n          \"en_auroc\",\n          \"zs_mean_auroc_19\",\n          \"zs_drop_pp\",\n          \"on_pareto\"\n        ],\n        \"rows\": [\n          [\n            4,\n            8,\n            0.634,\n            0.624,\n            1.0,\n            false\n          ],\n          [\n            8,\n            17,\n            0.672,\n            0.659,\n            1.3,\n            false\n          ],\n          [\n            12,\n            25,\n            0.714,\n            0.699,\n            1.5,\n            false\n          ],\n          [\n            16,\n            33,\n            0.745,\n            0.729,\n            1.6,\n            false\n          ],\n          [\n            20,\n            42,\n            0.768,\n            0.748,\n            2.0,\n            true\n          ],\n          [\n            24,\n            50,\n            0.786,\n            0.745,\n            4.1,\n            true\n          ],\n          [\n            28,\n            58,\n            0.798,\n            0.741,\n            5.7,\n            true\n          ],\n          [\n            32,\n            67,\n            0.81,\n            0.732,\n            7.8,\n            true\n          ],\n          [\n            36,\n            75,\n            0.821,\n            0.714,\n            10.7,\n            false\n          ],\n          [\n            40,\n            83,\n            0.818,\n            0.689,\n            12.9,\n            false\n          ],\n          [\n            44,\n            92,\n            0.804,\n            0.651,\n            15.3,\n            false\n          ],\n          [\n            48,\n            100,\n            0.771,\n            0.608,\n            16.3,\n            false\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Cross-Architecture Pareto Frontier Agreement\",\n        \"columns\": [\n          \"metric\",\n          \"qwen3_235b\",\n          \"llama4_scout\",\n          \"agreement\"\n        ],\n        \"rows\": [\n          [\n            \"best_en_layer_depth_pct\",\n            77,\n            75,\n            \"within 2pp\"\n          ],\n          [\n            \"best_transfer_layer_depth_pct\",\n            60,\n            58,\n            \"within 2pp\"\n          ],\n          [\n            \"pareto_zone_depth_range_pct\",\n            \"43-64\",\n            \"42-67\",\n            \"overlapping\"\n          ],\n          [\n            \"depth_transfer_rank_corr\",\n            0.88,\n            0.82,\n            \"both >0.75\"\n          ],\n          [\n            \"frontier_shape\",\n            \"convex monotonic\",\n            \"convex monotonic\",\n            \"consistent\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-architecture agreement is high: both models show best transfer at ~59% depth, the Pareto frontier occupies the 42-67% depth band, and the rank correlation between depth and transfer degradation exceeds 0.75 in both. The frontier shape is architecture-invariant — it's the depth-normalized position, not absolute layer count, that determines the tradeoff. This validates Claim 1 at scale.\\n\\n\\nLlama 4 Scout has 48 layers (fewer than Qwen3's 94) and a different MoE routing strategy (16 experts, top-2). With roughly 109B total / ~17B active params, its active compute is smaller than Qwen3-235B's ~22B active. This yields ~2pp lower EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer points (4 vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but the monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout's best transfer layer sits at ~58% depth (L28), remarkably close to Qwen3's 60%, suggesting a universal \\\"mid-depth transfer zone\\\" across architectures. The rank correlation is slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant. Low-resource languages are slightly weaker because Meta's multilingual pretraining mix underrepresents African languages compared to Qwen3.\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train on English labels + unlabeled parallel activations. Compare vs all 5 conditions across full Pareto frontier, both models × 20 languages. Hyperparameter tuning (α, β).\\n\",\n    \"results\": {\n      \"best_alpha\": 0.15,\n      \"best_beta\": 0.08,\n      \"qwen3_caclr_auroc_mean_19lang\": 0.814,\n      \"qwen3_caclr_ece_mean_19lang\": 0.058,\n      \"qwen3_caclr_vs_linproj_auroc_delta_pp\": 3.3,\n      \"qwen3_caclr_vs_zeroshot_auroc_delta_pp\": 5.2,\n      \"qwen3_caclr_ece_reduction_vs_tempcal_pct\": 40.8,\n      \"qwen3_caclr_best_operating_layer\": 64,\n      \"llama4_caclr_auroc_mean_19lang\": 0.793,\n      \"llama4_caclr_ece_mean_19lang\": 0.064,\n      \"llama4_caclr_vs_linproj_auroc_delta_pp\": 3.1,\n      \"llama4_caclr_vs_zeroshot_auroc_delta_pp\": 5.2,\n      \"llama4_caclr_ece_reduction_vs_tempcal_pct\": 38.5,\n      \"llama4_caclr_best_operating_layer\": 32,\n      \"caclr_vs_linproj_auroc_delta_pp_mean\": 3.2,\n      \"caclr_ece_reduction_vs_tempcal_pct_mean\": 39.7,\n      \"caclr_improvement_pass_rate\": 0.92,\n      \"caclr_pareto_shift_layers\": 2,\n      \"low_resource_caclr_auroc\": {\n        \"sw_qwen3\": 0.731,\n        \"yo_qwen3\": 0.709,\n        \"ig_qwen3\": 0.718,\n        \"sw_llama4\": 0.712,\n        \"yo_llama4\": 0.681,\n        \"ig_llama4\": 0.698\n      },\n      \"low_resource_zs_pass_rate\": 1.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)\",\n        \"columns\": [\n          \"method\",\n          \"auroc_mean_19\",\n          \"ece_mean_19\",\n          \"requires_target_labels\",\n          \"params_overhead\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.752,\n            0.098,\n            \"no\",\n            \"0\"\n          ],\n          [\n            \"mean-shift\",\n            0.747,\n            0.102,\n            \"no\",\n            \"0\"\n          ],\n          [\n            \"linear_projection\",\n            0.77,\n            0.082,\n            \"no\",\n            \"d×d matrix\"\n          ],\n          [\n            \"few-shot-25\",\n            0.738,\n            0.089,\n            \"yes (25)\",\n            \"0\"\n          ],\n          [\n            \"few-shot-100\",\n            0.762,\n            0.079,\n            \"yes (100)\",\n            \"0\"\n          ],\n          [\n            \"CaCLR\",\n            0.804,\n            0.061,\n            \"no\",\n            \"~1% probe params\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: CaCLR Ablation — Loss Component Contributions\",\n        \"columns\": [\n          \"configuration\",\n          \"auroc_mean_19\",\n          \"ece_mean_19\",\n          \"delta_vs_full_auroc_pp\"\n        ],\n        \"rows\": [\n          [\n            \"L_BCE_only (= zero-shot probe)\",\n            0.752,\n            0.098,\n            -5.2\n          ],\n          [\n            \"L_BCE + L_SB-ECE\",\n            0.768,\n            0.072,\n            -3.6\n          ],\n          [\n            \"L_BCE + L_consistency\",\n            0.793,\n            0.078,\n            -1.1\n          ],\n          [\n            \"L_BCE + L_SB-ECE + L_consistency (full CaCLR)\",\n            0.804,\n            0.061,\n            0.0\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)\",\n        \"columns\": [\n          \"layer_idx\",\n          \"zs_auroc_19\",\n          \"caclr_auroc_19\",\n          \"shift_pp\",\n          \"on_shifted_pareto\"\n        ],\n        \"rows\": [\n          [\n            40,\n            0.776,\n            0.798,\n            2.2,\n            false\n          ],\n          [\n            44,\n            0.774,\n            0.8,\n            2.6,\n            false\n          ],\n          [\n            48,\n            0.77,\n            0.803,\n            3.3,\n            true\n          ],\n          [\n            52,\n            0.765,\n            0.806,\n            4.1,\n            true\n          ],\n          [\n            56,\n            0.762,\n            0.81,\n            4.8,\n            true\n          ],\n          [\n            60,\n            0.753,\n            0.814,\n            6.1,\n            true\n          ],\n          [\n            64,\n            0.741,\n            0.814,\n            7.3,\n            true\n          ],\n          [\n            68,\n            0.728,\n            0.808,\n            8.0,\n            true\n          ],\n          [\n            72,\n            0.712,\n            0.796,\n            8.4,\n            false\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR decisively outperforms all baselines. The ablation shows both loss terms contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp alone), while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to 0.061 when added). The interaction is synergistic — joint optimization yields better results than either term alone. The Pareto shift is the headline result: at the same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation from \\\"use shallower layers for transfer\\\" to \\\"use CaCLR and operate at deeper, better-calibrated layers.\\\" The improvement pass rate of 92% (35/38 model-lang pairs) demonstrates consistency. The 3 non-improving pairs are high-resource languages (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already excellent and the consistency loss has minimal signal to exploit.\\n\\n\\nCaCLR's consistency loss (β·L_consistency) directly penalizes divergence between EN and non-EN probe outputs on parallel/comparable activations, forcing the probe to learn language-invariant features. This is strictly more informative than linear projection (which only aligns means and covariances post-hoc) because it shapes the learned representation during training. The 3.2pp AUROC gain over linear projection reflects the value of end-to-end optimization: linear projection corrects first-order distributional mismatch but not the nonlinear feature interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE) provides calibration-aware training that temperature scaling cannot — it directly optimizes the calibration objective rather than post-hoc rescaling. The 40% ECE reduction over temperature scaling arises because CaCLR addresses the root cause (representation misalignment) rather than the symptom (miscalibrated probabilities). The Pareto frontier shift is the key result: CaCLR allows operating 2 layers deeper than the ZS-optimal point while maintaining equivalent or better transfer — it literally pushes the Pareto frontier outward. Low-resource languages benefit most from L_consistency because their activation distributions are most misaligned from EN; the consistency term provides the strongest gradient signal precisely where the gap is largest.\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Ablation\",\n    \"description\": \"IRT difficulty probes (Ridge regression), project out difficulty direction, retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers per model.\\n\",\n    \"results\": {\n      \"difficulty_probe_r2_mean\": 0.72,\n      \"difficulty_var_explained_pct_mean\": 68.4,\n      \"difficulty_var_explained_pct_range\": [\n        58.2,\n        79.1\n      ],\n      \"residual_en_auroc_drop_pp\": 4.2,\n      \"residual_zs_transfer_drop_pp\": 1.1,\n      \"capability_specific_var_pct\": 31.6,\n      \"capability_specific_transfer_degradation_pct\": 87,\n      \"difficulty_component_transfer_degradation_pct\": 13,\n      \"decomp_prescriptive_accuracy\": 0.81,\n      \"difficulty_var_by_depth\": {\n        \"shallow_20pct\": 0.74,\n        \"mid_50pct\": 0.69,\n        \"deep_80pct\": 0.62\n      },\n      \"capability_transfer_drop_by_depth\": {\n        \"shallow_20pct\": 0.8,\n        \"mid_50pct\": 3.4,\n        \"deep_80pct\": 9.7\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Decomposition Results — Difficulty vs Capability Components\",\n        \"columns\": [\n          \"component\",\n          \"var_explained_pct\",\n          \"transfer_auroc_mean\",\n          \"transfer_drop_from_en_pp\",\n          \"share_of_total_transfer_drop_pct\"\n        ],\n        \"rows\": [\n          [\n            \"full_correctness\",\n            100,\n            0.752,\n            8.1,\n            100\n          ],\n          [\n            \"difficulty_shared\",\n            68.4,\n            0.738,\n            1.1,\n            13\n          ],\n          [\n            \"capability_specific\",\n            31.6,\n            0.614,\n            14.2,\n            87\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Capability-Specific Transfer Drop by Depth\",\n        \"columns\": [\n          \"depth_band\",\n          \"difficulty_transfer_drop_pp\",\n          \"capability_transfer_drop_pp\",\n          \"ratio\"\n        ],\n        \"rows\": [\n          [\n            \"0-30%\",\n            0.3,\n            0.8,\n            \"2.7×\"\n          ],\n          [\n            \"30-60%\",\n            0.8,\n            3.4,\n            \"4.3×\"\n          ],\n          [\n            \"60-90%\",\n            1.6,\n            9.7,\n            \"6.1×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The decomposition cleanly separates: difficulty-shared signal is the majority (68%) of correctness variance and transfers near-perfectly across languages and depths. The capability-specific residual (32%) drives nearly all transfer degradation (87%), and this degradation accelerates exponentially with depth. This explains the Pareto frontier mechanistically: deeper layers have stronger capability-specific signals that improve EN calibration but impede transfer. CaCLR works because its consistency loss specifically targets the capability-specific component — forcing alignment of the non-difficulty residual across languages. The prescriptive value (81% accuracy in predicting when CaCLR is needed) confirms this is a load-bearing decomposition, not a post-hoc narrative.\\n\\n\\nIRT difficulty is a strong, language-agnostic property — harder questions are harder everywhere. Ridge regression captures this cleanly (R²=0.72) because difficulty is linearly encoded in intermediate representations (Civelli et al. confirmed this). The difficulty component accounts for 68% of explained variance because GlobalMMLU correctness is heavily driven by item difficulty: a model gets easy questions right in all languages and hard questions wrong in all languages. After projecting out difficulty, the residual correctness signal is \\\"capability-specific\\\" — it captures language-dependent competence differences. This residual transfers poorly at deep layers (9.7pp drop at 80% depth vs 0.8pp at 20% depth) because deep layers encode language-specific processing that makes capability assessments non-transferable. The difficulty component transfers well at all depths (only 13% of total transfer degradation) because it's language-invariant by construction. This decomposition is prescriptive: when difficulty explains most of a language's correctness variance, simple zero-shot transfer suffices; when the capability residual is large, CaCLR is needed. The 81% prescriptive accuracy validates the decomposition as more than descriptive.\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Extract verbalized confidence direction via prompted confidence scores, compute cosine similarity with correctness direction across 20 languages × 2 architectures. Analyze by resource tier and language family.\\n\",\n    \"results\": {\n      \"orthogonality_cosine_mean_overall\": 0.052,\n      \"orthogonality_cosine_range\": [\n        0.018,\n        0.094\n      ],\n      \"orthogonality_cosine_en\": 0.034,\n      \"qwen3_cosine_mean\": 0.048,\n      \"llama4_cosine_mean\": 0.057,\n      \"high_resource_cosine_mean\": 0.041,\n      \"mid_resource_cosine_mean\": 0.054,\n      \"low_resource_cosine_mean\": 0.074,\n      \"cosine_by_lang\": {\n        \"en\": 0.034,\n        \"zh\": 0.038,\n        \"de\": 0.036,\n        \"fr\": 0.039,\n        \"es\": 0.041,\n        \"ja\": 0.044,\n        \"ru\": 0.043,\n        \"pt\": 0.04,\n        \"it\": 0.042,\n        \"ar\": 0.051,\n        \"hi\": 0.055,\n        \"ko\": 0.049,\n        \"vi\": 0.058,\n        \"th\": 0.061,\n        \"bn\": 0.056,\n        \"tr\": 0.052,\n        \"nl\": 0.037,\n        \"sw\": 0.078,\n        \"yo\": 0.094,\n        \"ig\": 0.082\n      },\n      \"all_langs_below_0p1\": true,\n      \"cosine_resource_tier_correlation\": -0.68\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture\",\n        \"columns\": [\n          \"language\",\n          \"resource_tier\",\n          \"qwen3_cosine\",\n          \"llama4_cosine\",\n          \"mean_cosine\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"high\",\n            0.031,\n            0.037,\n            0.034\n          ],\n          [\n            \"zh\",\n            \"high\",\n            0.035,\n            0.041,\n            0.038\n          ],\n          [\n            \"de\",\n            \"high\",\n            0.033,\n            0.039,\n            0.036\n          ],\n          [\n            \"fr\",\n            \"high\",\n            0.036,\n            0.042,\n            0.039\n          ],\n          [\n            \"es\",\n            \"high\",\n            0.038,\n            0.044,\n            0.041\n          ],\n          [\n            \"ja\",\n            \"high\",\n            0.041,\n            0.047,\n            0.044\n          ],\n          [\n            \"ru\",\n            \"high\",\n            0.04,\n            0.046,\n            0.043\n          ],\n          [\n            \"pt\",\n            \"high\",\n            0.037,\n            0.043,\n            0.04\n          ],\n          [\n            \"it\",\n            \"high\",\n            0.039,\n            0.045,\n            0.042\n          ],\n          [\n            \"nl\",\n            \"high\",\n            0.034,\n            0.04,\n            0.037\n          ],\n          [\n            \"ar\",\n            \"mid\",\n            0.047,\n            0.055,\n            0.051\n          ],\n          [\n            \"hi\",\n            \"mid\",\n            0.051,\n            0.059,\n            0.055\n          ],\n          [\n            \"ko\",\n            \"mid\",\n            0.045,\n            0.053,\n            0.049\n          ],\n          [\n            \"vi\",\n            \"mid\",\n            0.054,\n            0.062,\n            0.058\n          ],\n          [\n            \"th\",\n            \"mid\",\n            0.057,\n            0.065,\n            0.061\n          ],\n          [\n            \"bn\",\n            \"mid\",\n            0.052,\n            0.06,\n            0.056\n          ],\n          [\n            \"tr\",\n            \"mid\",\n            0.048,\n            0.056,\n            0.052\n          ],\n          [\n            \"sw\",\n            \"low\",\n            0.073,\n            0.083,\n            0.078\n          ],\n          [\n            \"yo\",\n            \"low\",\n            0.089,\n            0.099,\n            0.094\n          ],\n          [\n            \"ig\",\n            \"low\",\n            0.077,\n            0.087,\n            0.082\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: Orthogonality Summary Statistics\",\n        \"columns\": [\n          \"statistic\",\n          \"qwen3_235b\",\n          \"llama4_scout\",\n          \"both_models\"\n        ],\n        \"rows\": [\n          [\n            \"cosine_mean\",\n            0.048,\n            0.057,\n            0.052\n          ],\n          [\n            \"cosine_std\",\n            0.015,\n            0.017,\n            0.016\n          ],\n          [\n            \"cosine_max\",\n            0.089,\n            0.099,\n            0.094\n          ],\n          [\n            \"cosine_min\",\n            0.031,\n            0.037,\n            0.018\n          ],\n          [\n            \"all_below_0.1\",\n            \"yes (20/20)\",\n            \"yes (19/20)\",\n            \"39/40\"\n          ],\n          [\n            \"resource_tier_corr\",\n            -0.71,\n            -0.65,\n            -0.68\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality generalizes comprehensively. The mean cosine of 0.052 across all 40 language-architecture pairs is well within the \\\"near-orthogonal\\\" regime (< 0.1). The resource-tier gradient is the novel finding: it suggests that output-based calibration methods are not just structurally limited but are *more* limited for well-resourced languages where the orthogonality is strongest. This strengthens the motivation for probe-based approaches universally and for CaCLR specifically in multilingual settings. Yoruba's 0.094 is the only value approaching the 0.1 threshold (on Llama4 it hits 0.099), which is worth noting but does not break the claim.\\n\\n\\nMiao & Ungar (2026) established correctness-confidence orthogonality (cosine < 0.04) for English on 7-8B models. We extend to 20 languages on larger models. The orthogonality persists universally (all < 0.1) because it reflects a fundamental architectural property: verbalized confidence is generated by the language modeling head from surface-level token probabilities, while correctness is encoded in intermediate representation geometry. These are structurally decoupled in transformer architectures. The slight increase in cosine for low-resource languages (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages have noisier confidence elicitation — the model's verbalized confidence in Yoruba is less well-calibrated and leaks some correctness signal, producing weak correlation. The resource-tier gradient (ρ=-0.68) suggests that better multilingual training data produces cleaner separation between correctness and confidence representations. The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this is not architecture-specific. Llama 4's slightly higher cosines may reflect its less aggressive multilingual pretraining compared to Qwen3.\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP at each probed layer, both models. Compare English accuracy, cross-lingual transfer degradation, calibration quality.\\n\",\n    \"results\": {\n      \"logreg_en_auroc_best\": 0.843,\n      \"mlp_en_auroc_best\": 0.856,\n      \"mlp_en_auroc_gain_pp\": 1.3,\n      \"logreg_zs_transfer_drop_mean_pp\": 8.1,\n      \"mlp_zs_transfer_drop_mean_pp\": 12.4,\n      \"transfer_degradation_ratio\": 1.53,\n      \"logreg_ece_mean\": 0.054,\n      \"mlp_ece_mean\": 0.068,\n      \"logreg_transfer_advantage_shallow_pp\": 2.1,\n      \"logreg_transfer_advantage_deep_pp\": 6.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Probe Complexity Comparison\",\n        \"columns\": [\n          \"probe_type\",\n          \"en_auroc_best\",\n          \"zs_auroc_mean_19\",\n          \"zs_drop_pp\",\n          \"ece_mean_19\"\n        ],\n        \"rows\": [\n          [\n            \"logistic_regression\",\n            0.843,\n            0.762,\n            8.1,\n            0.054\n          ],\n          [\n            \"mlp_2layer\",\n            0.856,\n            0.733,\n            12.4,\n            0.068\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear probes are the correct choice for cross-lingual transfer: they sacrifice 1.3pp EN AUROC but gain 4.3pp average transfer. The depth interaction effect is notable — the logreg advantage grows from 2.1pp at shallow layers to 6.8pp at deep layers, confirming that deep-layer transfer degradation is driven by nonlinear, language- specific features. CaCLR + logreg is thus the optimal configuration.\\n\\n\\nLinear probes transfer better because they learn a single hyperplane in activation space — the hyperplane generalizes across languages when the underlying geometry is approximately shared (as it is in mid-depth layers). MLPs learn nonlinear decision boundaries that fit English-specific feature interactions, gaining ~1.3pp EN AUROC but losing ~4.3pp in transfer. The transfer gap widens at deeper layers (6.8pp advantage for logreg) because deep layers have more language-specific nonlinear structure that MLPs exploit but logreg ignores. This justifies our choice of linear probes for the main results and supports the geometric interpretation of the Pareto frontier: it's about linear subspace alignment, not complex feature interactions.\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX (20 languages).\\n\",\n    \"results\": {\n      \"belebele_zs_auroc_mean_19\": 0.738,\n      \"belebele_caclr_auroc_mean_19\": 0.789,\n      \"belebele_caclr_vs_zs_pp\": 5.1,\n      \"belebele_ece_reduction_vs_tempcal_pct\": 36.2,\n      \"mmlupx_zs_auroc_mean_19\": 0.722,\n      \"mmlupx_caclr_auroc_mean_19\": 0.774,\n      \"mmlupx_caclr_vs_zs_pp\": 5.2,\n      \"mmlupx_ece_reduction_vs_tempcal_pct\": 33.8,\n      \"caclr_benefit_cross_benchmark_cv\": 0.08\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Cross-Benchmark Generalization\",\n        \"columns\": [\n          \"benchmark\",\n          \"zs_auroc_mean_19\",\n          \"caclr_auroc_mean_19\",\n          \"caclr_gain_pp\",\n          \"ece_reduction_pct\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            0.752,\n            0.804,\n            5.2,\n            39.7\n          ],\n          [\n            \"Belebele\",\n            0.738,\n            0.789,\n            5.1,\n            36.2\n          ],\n          [\n            \"MMLU-ProX\",\n            0.722,\n            0.774,\n            5.2,\n            33.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR generalizes cleanly across benchmarks. The improvement magnitude is remarkably stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method addresses a fundamental representation alignment issue rather than overfitting to GlobalMMLU- specific patterns. This is critical for reviewer confidence.\\n\\n\\nBelebele tests reading comprehension (vs GlobalMMLU's factual knowledge), providing domain generalization evidence. Transfer AUROC is slightly lower (0.738 vs 0.762) because Belebele's passage-dependent questions have weaker difficulty-shared signal — comprehension difficulty is more language-dependent than factual difficulty. CaCLR still provides ~5pp improvement, confirming the consistency loss generalizes beyond factual MCQA. MMLU-ProX has harder questions that compress the AUROC distribution (lower base rate of correctness), yielding slightly lower absolute numbers but comparable CaCLR benefit. The cross-benchmark CV of 0.08 for CaCLR improvement confirms the method is robust to evaluation domain.\\n\"\n  },\n  {\n    \"name\": \"INT8 Validation Ablation\",\n    \"description\": \"Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset.\\n\",\n    \"results\": {\n      \"int8_fp16_auroc_diff_mean_pp\": 0.3,\n      \"int8_fp16_auroc_diff_max_pp\": 0.7,\n      \"int8_fp16_ece_diff_mean_pp\": 0.2,\n      \"int8_fp16_transfer_drop_diff_pp\": 0.4,\n      \"int8_fp16_rank_correlation\": 0.997,\n      \"conclusion\": \"INT8 quantization introduces negligible distortion\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)\",\n        \"columns\": [\n          \"layer_idx\",\n          \"fp16_auroc\",\n          \"int8_auroc\",\n          \"diff_pp\",\n          \"fp16_zs_auroc_5lang\",\n          \"int8_zs_auroc_5lang\",\n          \"transfer_diff_pp\"\n        ],\n        \"rows\": [\n          [\n            8,\n            0.674,\n            0.672,\n            0.2,\n            0.661,\n            0.658,\n            0.3\n          ],\n          [\n            16,\n            0.747,\n            0.745,\n            0.2,\n            0.731,\n            0.728,\n            0.3\n          ],\n          [\n            24,\n            0.788,\n            0.786,\n            0.2,\n            0.747,\n            0.744,\n            0.3\n          ],\n          [\n            32,\n            0.812,\n            0.81,\n            0.2,\n            0.734,\n            0.731,\n            0.3\n          ],\n          [\n            40,\n            0.82,\n            0.817,\n            0.3,\n            0.691,\n            0.687,\n            0.4\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"INT8 quantization is validated as safe for our experimental setup. The maximum observed difference (0.7pp at a single layer-language combination) is well within the noise floor of probing experiments. The Pareto frontier ordering is perfectly preserved (rank correlation 0.997). This ablation preempts reviewer concern #5.\\n\\n\\nINT8 weight-only quantization preserves the 8 most significant bits of each weight, introducing per-channel quantization noise of ~0.4% relative magnitude. Correctness probing relies on the geometry of activation space (direction of correctness signal), not absolute magnitudes. The quantization noise is approximately isotropic and thus preserves angular relationships between directions. The 0.3pp mean AUROC difference is within random seed variance, and the rank correlation of 0.997 between INT8 and FP16 layer rankings confirms that the Pareto frontier shape is unaffected. This result is expected given prior work showing that probing results are robust to quantization down to INT4 (Gao et al., 2024).\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense — Third Architecture (Camera-Ready)\",\n    \"description\": \"Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages. Provides dense vs MoE architectural contrast.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.812,\n      \"en_best_layer_idx\": 45,\n      \"zs_transfer_auroc_mean_19lang\": 0.734,\n      \"zs_best_transfer_layer_idx\": 36,\n      \"zs_transfer_drop_mean_pp\": 7.8,\n      \"pareto_depth_transfer_rank_corr\": 0.86,\n      \"caclr_auroc_mean_19lang\": 0.786,\n      \"caclr_vs_linproj_auroc_delta_pp\": 2.9,\n      \"dense_vs_moe_transfer_comparison\": \"comparable within 2pp\",\n      \"pareto_shape\": \"convex monotonic, consistent with MoE models\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Three-Architecture Summary\",\n        \"columns\": [\n          \"model\",\n          \"type\",\n          \"layers\",\n          \"en_auroc_best\",\n          \"zs_auroc_mean_19\",\n          \"best_transfer_depth_pct\",\n          \"pareto_rank_corr\",\n          \"caclr_gain_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B-A22B\",\n            \"MoE\",\n            94,\n            0.843,\n            0.762,\n            60,\n            0.88,\n            3.3\n          ],\n          [\n            \"Llama 4 Scout\",\n            \"MoE\",\n            48,\n            0.821,\n            0.741,\n            58,\n            0.82,\n            3.1\n          ],\n          [\n            \"Gemma 4 31B Dense\",\n            \"Dense\",\n            60,\n            0.812,\n            0.734,\n            60,\n            0.86,\n            2.9\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The three-architecture comparison is the strongest evidence for the universality of the depth-transferability tradeoff. The best-transfer depth converges to 58-60% across dense and MoE architectures with 48-94 layers, CaCLR provides consistent 2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases. Dense vs MoE makes minimal difference — the phenomenon is a property of transformer depth, not routing architecture.\\n\\n\\nGemma 4 31B Dense has fewer total parameters than the MoE models but all are active, yielding comparable per-token compute. As a dense model, its representations are more uniformly distributed across layers (no expert routing), producing slightly smoother Pareto frontiers. The best-transfer depth (~60%) matches both MoE models, confirming this is a universal property of transformer depth, not MoE-specific. EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B active params < 22B active with MoE routing benefits. CaCLR improvement is slightly lower (2.9pp) on the dense model because the absence of expert routing means less language-specific feature fragmentation to correct. This is the ideal third data point: different architecture family, consistent findings.\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (Camera-Ready)\",\n    \"description\": \"Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele full language sets.\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"new_languages_added\": 32,\n      \"zs_auroc_above_0p60_count\": 48,\n      \"zs_auroc_below_0p55_count\": 2,\n      \"caclr_improvement_positive_count\": 49,\n      \"mean_zs_auroc_51lang\": 0.72,\n      \"mean_caclr_auroc_51lang\": 0.77,\n      \"pareto_frontier_holds_all_langs\": true,\n      \"new_language_families_covered\": [\n        \"Austronesian\",\n        \"Dravidian\",\n        \"Niger-Congo B\",\n        \"Uralic\",\n        \"Kartvelian\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Extended Language Coverage Summary by Resource Tier\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"zs_auroc_mean\",\n          \"caclr_auroc_mean\",\n          \"caclr_gain_pp\",\n          \"pct_above_0p60\"\n        ],\n        \"rows\": [\n          [\n            \"high\",\n            12,\n            0.782,\n            0.812,\n            3.0,\n            100\n          ],\n          [\n            \"mid\",\n            25,\n            0.738,\n            0.784,\n            4.6,\n            100\n          ],\n          [\n            \"low\",\n            10,\n            0.661,\n            0.712,\n            5.1,\n            90\n          ],\n          [\n            \"very_low\",\n            4,\n            0.582,\n            0.638,\n            5.6,\n            50\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The extension to 52 languages confirms all findings at broader scale. The resource-tier gradient is smooth and predictable — no language family shows anomalous behavior. CaCLR's benefit is inversely correlated with resource level (3.0pp for high-resource to 5.6pp for very-low-resource), confirming that the consistency loss provides most value where representation misalignment is worst. The 48/51 pass rate (>0.60 AUROC) for zero-shot CaCLR transfer with no target-language labels is the practical headline for camera-ready: usable cross-lingual calibration for the vast majority of languages.\\n\\nExpanding to 50+ languages primarily adds mid-resource languages (Indonesian, Malay, Finnish, Georgian, Tamil, Telugu, etc.) where the model has moderate pretraining exposure. Most new languages fall in the 0.65-0.78 AUROC range, consistent with the mid-resource tier from the 20-language set. A handful of extremely low-resource languages (e.g., Amharic script languages with minimal pretraining data) may fall below 0.55, but these represent edge cases rather than systematic failures. CaCLR continues to improve 96% of languages because the consistency loss mechanism is language-agnostic — it aligns activation distributions without requiring any language-specific knowledge. The Pareto frontier structure is preserved across all 52 languages, confirming it's a depth property, not a language-set artifact.\\n\"\n  }\n]",
      "numLines": 1375,
      "startLine": 1,
      "totalLines": 1375
    }
  },
  "sourceToolAssistantUUID": "1d8145de-31e7-4ccb-b736-97ac9ec5006f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18 · 2026-05-21T04:53:54.590Z_

````json
{
  "parentUuid": "9e4308b4-5155-49d6-b421-18fa25f490c8",
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
  "uuid": "707fc94c-270c-4354-ae92-597177038ba3",
  "timestamp": "2026-05-21T04:53:54.590Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：核心几何洞见（Simpson's Paradox）在双架构 × 20 语言上显著复现；CaCLR consistency loss 提供可测量迁移增益；所有 claims 完整保留 核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均显著 (p < 0.01…",
  "leafUuid": "707fc94c-270c-4354-ae92-597177038ba3",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Simpson's Paradox reveals cross-lingual correctness probe transfer",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Assistant

_source line 21 · 2026-05-21T04:58:01.803Z_

<details><summary>Logged reasoning block</summary>

```text
Now I've read the previous dream report's best tier. I see that it was generated before the Phase 1 revision that changed the best tier definition. The key differences in the new best tier definition:

1. **Simpson's Paradox** is now the core novelty (not CaCLR as method contribution)
2. **CaCLR consistency loss** provides "measurable transfer gain" (≥2pp AUROC) — this is more modest than the old dream which had CaCLR as a strong method contribution (+5pp, shifting Pareto)
3. The narrative has shifted: CaCLR is a positive method contribution but the Simpson's Paradox geometric insight is the opening


4. All claims are preserved, but the metric ranges are now tighter and more grounded in the actual data

Looking at the specifics, the old dream had en_best_auroc at 0.843, which actually exceeds the new range of [0.77, 0.83], and the CaCLR improvement was overstated at 5.2pp when the new range is 2-5pp. I also notice the old dream was missing the planned analyses around Simpson's Paradox, linear projection sensitivity, and control tasks that should be included now.

Now I'm working through the updated predictions that fit these tighter constraints—picking values like 0.81 for en_best_auroc, 16-18 languages passing out of 20, Simpson's partial correlations around 0.38-0.42 depending on the model, and keeping the mean CaCLR improvement at roughly 3pp.

I'm also anchoring to the actual MVP results: Qwen2.5-7B hit 0.754 at layer 27 and Llama-3.1-8B reached 0.728 at layer 31, plus the CKA pilot showing that negative overall correlation of -0.40 but a positive partial correlation of 0.41 when controlling for other factors.

The new experiment plan focuses on three key areas: the Simpson's Paradox analysis in CKA is the real novelty here, linear projection sensitivity testing, and probing controls which are already complete. I'm also adjusting the quantization experiments—moving to W4A16 versus FP16 for Llama and GPTQ-Int4 versus FP16 for Qwen instead of INT8, plus updating plan_002 to use W4A16 quantization. The narrative has shifted too: CaCLR with β>0 now shows around 2 percentage points improvement rather than the 5 points I was hoping for, linear projection emerges as the practical approach to reach 95% with roughly 50 pairs, and the core contribution is really understanding Simpson's Paradox within the context.

Now I'm looking at the KA-transfer results and the architecture-dependent Pareto frontier—Qwen shows strong tradeoffs while Llama's are weaker. But I need to reconsider the best tier hypotheses more carefully. The key findings are that Simpson's Paradox in partial correlation holds significantly across both architectures and CKA does explain transfer differences when controlling for depth, CaCLR consistency loss with β>0 provides at least 2 percentage points improvement on deeper layers compared to zero-shot, the Pareto frontier shows clear architecture dependence matching the MVP pattern, and difficulty decomposition appears to have prescriptive value.

Looking at the full-scale experiments, Qwen3-235B exhibits strong depth-transfer tradeoffs with most languages showing negative correlation, while Llama 4 Scout displays weaker or mixed tradeoffs where some languages actually improve with depth. Control task artifacts concentrate in low-resource languages around 25-30% without affecting medium or high-resource ones, and linear projection with just 50 or fewer pairs achieves over 95% performance with clear saturation across resource tiers.

Now I need to map out all the planned experiments systematically, from the full Pareto analyses for both architectures through CaCLR, difficulty decomposition, cross-lingual orthogonality, probe complexity, additional benchmarks, quantization validation, and the critical new analyses around CKA and Simpson's Paradox plus linear projection sensitivity.

For the Qwen3-235B baseline, I'm estimating the best AUROC around 0.81 given the model's 235B parameters with MoE and INT4 quantization, scaling up from the 7B baseline that achieved 0.754 at the deepest layers.

The probing strategy for the 94-layer model would sample every 4th layer, giving me roughly 23 layers to test, and I'd expect a strong Pareto tradeoff where deeper layers excel on English but hurt cross-lingual transfer. For the zero-shot pass rate, I'm targeting around 85% across 20 languages, distributed across high-resource (Chinese, Spanish, French, German, Portuguese, Italian, Japanese, Dutch), mid-resource (Arabic, Hindi, Korean, Turkish, Russian, Vietnamese, Thai), and low-resource (Swahili, Bengali, Yoruba, Igbo) groups. I'm categorizing the 20 languages by resource level—high-resource languages like Chinese, Spanish, French, German, Portuguese, Japanese, Dutch, and Italian; mid-resource ones including Arabic, Hindi, Korean, Turkish, Russian, Vietnamese, and Thai; and low-resource languages like Swahili, Bengali, Yoruba, Igbo, and Telugu. Given the 85% zero-shot pass rate, the three lowest-resource languages are likely the ones failing the transfer.

Now I'm estimating the performance drop from English's 0.81 AUROC across resource tiers—high-resource languages probably maintain around 0.74-0.78, mid-resource around 0.68-0.73, and low-resource around 0.58-0.66—which would put Yoruba, Igbo, and Telugu right at the borderline of the 0.60 pass threshold. Looking at larger model capabilities, the transfer gap should actually shrink compared to smaller models, so I'm estimating higher performance across languages—with strong scores in major languages like Chinese, Spanish, and French around 0.77-0.78, mid-tier performance in languages like Arabic and Hindi around 0.71-0.73, and lower-resource languages like Swahili and Yoruba around 0.57-0.63. That puts me at roughly 17-18 languages passing the 0.60 threshold, which fits the expected 85% pass rate.

Rather than fine-tuning the exact language roster, I'm settling on a cleaner grouping: six high-performing languages (Chinese, Spanish, French, German, Japanese, Dutch), eight mid-tier ones (Arabic, Hindi, Korean, Turkish, Russian, Vietnamese, Thai, Italian), and six low-resource languages (Swahili, Bengali, Thai, Yoruba, Igbo, Telugu)—though I need to adjust since Thai shouldn't be in both groups.

The real priority is constructing the YAML experiments with realistic numbers that respect the constraints: keeping English AUROC between 0.77 and 0.83 (0.81 for Qwen, 0.79 for Llama), and making the Pareto frontier architecture-dependent so Qwen shows consistent negative correlations across languages while Llama exhibits a different tradeoff pattern.

Simpson's Paradox is the centerpiece—plan_011 needs to demonstrate that raw CKA-transfer correlation is negative but the partial correlation flips positive when controlling for architecture, which is the key insight. CaCLR contributes modestly (around 3 percentage points), linear projection saturates around 40-50 pairs with clear stratification by resource tier, and control task artifacts account for roughly 25-30% of low-resource variance. Procrustes reversal helps when zero-shot performance is below 0.50 but becomes detrimental above 0.60, with the threshold somewhere in between.

Now checking internal consistency: if English reaches 0.81 AUROC and CaCLR adds 3 points to non-English transfer performance, then the mean across 20 languages should land around 0.75 when zero-shot baseline is roughly 0.72. Looking at the MVP data from Qwen2.5-7B, English sits at 0.754 while other languages like Chinese, Arabic, and Hindi cluster in the 0.65-0.69 range, which aligns with this picture.

For the larger Qwen3-235B model at 0.81 English, I'd expect a similar relative drop of about 15%, putting the zero-shot mean around 0.689 to 0.705 depending on how much the larger model improves multilingual capability. If I'm looking at pass rates where AUROC above 0.60 counts as passing, then with a mean around 0.70 and standard deviation of roughly 0.06, the bottom three languages would fall just below that threshold at around 0.57.

For CaCLR, I'm adding a delta of about 3.5 percentage points over zero-shot performance, which gives me a mean of roughly 0.735. Now I need to write out the YAML configuration, and I'm noticing the quantization specs need adjustment—Llama 4 Scout uses W4A16 weight quantization rather than INT8, and the comparison should be W4A16 versus FP16 for Llama and GPTQ-Int4 versus FP16 for Qwen.

The MVP results show Llama-3.1-8B has weak Pareto characteristics with mixed depth-transfer tradeoffs across languages, which aligns with my hypothesis for Llama 4 Scout showing language-specific Spearman correlations—some negative, some neutral or positive—versus Qwen3 where the pattern is consistently negative across most languages with a clear convex frontier.

Now looking at the CKA analysis, the MVP data reveals Simpson's Paradox: the raw correlation between CKA degradation and transfer performance is negative (rho=-0.3982), but when controlling for layer depth, it flips positive (rho=+0.41). This happens because deeper layers simultaneously reduce CKA values and transfer performance, creating a confounding effect in the raw pooled data. the probe hasn't converged yet at shallow layers. Looking at the deeper layers, CKA drops while transfer AUROC initially rises then falls—the raw correlation gets dominated by this depth confound. But the MVP results show something clearer: the CKA-degradation correlation for Llama is negative (rho = -0.3982, p = 0.0068), meaning higher CKA actually predicts better transfer performance, which aligns with intuition.

The paper's framing reveals the Simpson's Paradox at play: the raw CKA-transfer correlation appears negative because shallow layers have high CKA but weak probes, while deeper layers show lower CKA but sometimes stronger transfer—once I control for depth, the partial correlation flips positive, showing the true relationship where higher CKA genuinely supports better transfer. pooling across depth creates a negative raw correlation

But within each layer:
- Languages with higher CKA at that layer have better transfer → positive partial correlation

This is a genuine Simpson's Paradox. The confound is depth acting on both variables in opposite directions.

Wait but the MVP CKA data showed overall_rho=-0.3982 for CKA vs DEGRADATION (negative means higher CKA = less degradation = better transfer). So the raw correlation for CKA vs transfer AUROC would be POSITIVE in the pilot...

Unless the "raw correlation" in the paper framing is computed differently. Let me re-read the notes in plan_011:

"Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen rho=-0.31 p=0.053)"

But the paper says the raw CKA-transfer correlation is negative, which would mean higher CKA corresponds to lower transfer AUROC. That contradicts what the MVP showed—if CKA negatively correlates with degradation, then it should positively correlate with transfer performance. I think there's a sign discrepancy between what the paper framing describes and what the actual MVP analysis found. The paper might be referring to a different computation altogether, or there's confusion about whether we're looking at degradation versus transfer AUROC directly. The key insight is that probe quality (which improves with depth) dominates over representation alignment (CKA) in determining transfer AUROC—so within each layer, higher CKA correlates with better transfer, but across layers, the shallow layers with high CKA have weak probes overall, creating the negative pooled correlation. Let me verify this against the MVP data where CKA and degradation show a negative correlation. high CKA → low transfer AUROC, low CKA → higher transfer AUROC → NEGATIVE correlation for CKA vs transfer AUROC.

But WITHIN each layer: comparing across languages, a language with higher CKA at L20 has better transfer at L20. Positive partial correlation.

Yes! This works. The Simpson's Paradox is between CKA and transfer AUROC (not degradation).

So for the full-scale predictions:

plan_011 predictions:
- Raw correlation (CKA vs transfer AUROC, pooled across layers): NEGATIVE (Qwen rho~-0.35, Llama rho~-0.40)
- Partial correlation controlling for depth: POSITIVE and significant (Qwen rho~+0.42 p<0.005, Llama rho~+0.38 p<0.008)
- Within each layer, the relationship holds positive.

I'm settling on Qwen partial rho=+0.45 (p=0.003) and Llama partial rho=+0.39 (p=0.007) — both meet the significance threshold and fall within the target range. Now I need to check the per-layer same-language correlations, where at each depth I'm computing the relationship between English-to-language CKA and that language's transfer performance across the 20 languages.

For the CKA threshold work, I'm seeing that transfer performance drops sharply when CKA falls below 0.35, with low-resource languages hitting this cliff earlier in deeper layers than high-resource ones. On the linear projection side, I'm estimating around 42 language pairs needed to reach 95% performance, though high-resource languages saturate much earlier at ~22 pairs while low-resource languages need closer to 48. The Procrustes effect is interesting — it helps when zero-shot performance is below 0.50 but becomes detrimental above 0.60, with the crossover around 0.52. For the probing controls, I already have real data results to reference rather than needing to generate new estimates.

Now I'm digging into the architecture dependence across models. With Qwen3-235B, there's a strong negative correlation between depth and transfer performance — most languages show significant negative correlations, with the global Spearman rho around -0.72. Llama 4 Scout shows a much weaker pattern, with mixed correlations across languages and only a handful reaching statistical significance.

For CaCLR, the gains are more modest than initially expected. It provides a consistent boost of around 3.5 percentage points over zero-shot across languages and architectures, with the consistency loss specifically targeting the capability-specific degradation in transfer. Linear projection remains competitive at roughly 2 percentage points, so CaCLR's actual advantage is closer to 1.5 percentage points — far more conservative than the original 5 percentage point improvement I was hoping for. Writing YAML config... Looking at the narrative structure, I need to make sure the framing is clear: Simpson's Paradox provides the geometric insight that opens the paper, CaCLR is presented as the solution method, and the four claims form a connected chain showing why cross-lingual calibration transfer works. The title should emphasize how geometric analysis reveals the conditions for success, and I need to be precise about what each claim covers—orthogonality is a subsection within the broader framework rather than a standalone claim.

Now I'm checking the existing probing controls data from plan_013 to see what selectivity metrics I already have on record before writing the YAML configuration.

I see the real AUROC values for English across the layers, but the full-scale version would need to cover 20 languages and 2 models, which goes beyond what the current MVP completion provides. Since plan_013 is marked DONE but only covers English, I should fold the comprehensive control analysis into the plan_001/002 predictions rather than treating it as a separate extension.

Now I'm organizing the output structure and finalizing the predicted metrics for each experiment, starting with the Qwen3-235B results. Now I'm looking at the performance metrics for Llama 4 Scout, which shows similar zero-shot transfer capabilities to the previous model but with weaker Pareto efficiency—only 10 out of 20 languages exhibit negative correlations with depth, and fewer reach statistical significance. For CaCLR, I'm seeing that the optimal hyperparameters (α=0.1, β=0.05) yield about 3.5 percentage points of AUROC improvement over zero-shot, with the consistency loss contributing roughly 2.5pp and the calibration loss adding another 1pp, and this benefit holds across the vast majority of language-model combinations. I'm starting to break down the decomposition analysis to understand which factors drive these improvements. R²: ~0.68
- Difficulty component: ~65% of correctness variance, transfers well
- Capability component: ~35%, drives 85%+ of transfer degradation
- Capability delta AUROC: ~3pp (in [0.02, 0.04])
- Prescriptive: 78% accuracy in predicting alignment strategy

### plan_005: Orthogonality
- Mean cosine: ~0.05
- All 40 pairs below 0.10
- Resource-tier gradient: r~-0.65

### plan_006: Probe complexity
- Linear probe: en=0.81, ZS drop=9pp
- MLP: en=0.83, ZS drop=14pp
- Linear better for transfer

### plan_007: Additional benchmarks
- Belebele/MMLU-ProX: CaCLR improvement consistent (~3-4pp)

### plan_010: Quantization validation
- W4A16 vs FP16 (Llama): <0.5pp difference
- GPTQ-Int4 vs FP16 (Qwen): <0.7pp difference

### plan_011: CKA/Simpson's (CORE)
- Raw CKA-transfer AUROC correlation: Qwen rho=-0.38, Llama rho=-0.42
- Partial (controlling depth): Qwen rho=+0.45, p=0.003; Llama rho=+0.39, p=0.007
- Per-layer same-language correlation: ~14-16/20 layers positive
- Subspace angle analysis: correctness direction stable across languages within layer
- CKA cliff threshold: ~0.35

Now looking at the linear projection approach and what it reveals about the underlying structure. 95% performance at ~42 pairs, with saturation points varying by resource level—HIGH at 22, MID at 38, LOW at 48. Procrustes reversal helps when zero-shot performance is below 0.52 but hurts above 0.60.

The control task experiments on full-scale data show English selectivity ranging from 0.02-0.26, matching the patterns I've already observed. Low-resource language-layer combinations have about 27% below the selectivity threshold, while mid and high-resource ones stay around 5%.

Gemma 4 confirms the universality of this depth-transfer tradeoff with English at 0.80, following the same Pareto pattern. Extended language experiments across 50+ languages show consistent CaCLR improvements.

Now I'm reconsidering the best tier hypothesis—the Pareto frontier should show architecture-dependent tradeoffs where Qwen3 exhibits a strong relationship between depth and transfer performance while Llama 4 shows a weaker one. This means both architectures should have significant global Spearman correlations across all languages pooled, but with different magnitudes: Qwen3 at -0.88 with p<0.001 versus Llama 4 at -0.72. Llama-3.1-8B showed strong zero-shot performance across all languages but exhibited language-specific depth-transfer patterns, whereas Llama 4 Scout is a much larger model that should inherit the same architectural trait of heterogeneous multilingual behavior rather than scaling effects. I need to write the rationales carefully, explaining the causal mechanisms behind each result and framing the narrative around Simpson's Paradox and CaCLR as the positive methodological approach.

Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "707fc94c-270c-4354-ae92-597177038ba3",
  "isSidechain": false,
  "requestId": "req_011CbF7iGdV7wNYRDFqEz38f",
  "type": "assistant",
  "uuid": "9d8e83d6-b27b-4c21-96ee-439e527d93e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193aWptsaeEei96PKSwpfRU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39312,
      "cache_read_input_tokens": 33760,
      "output_tokens": 10837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10837,
          "cache_read_input_tokens": 33760,
          "cache_creation_input_tokens": 39312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39312
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

_source line 22 · 2026-05-21T04:58:01.807Z_

Now let me check the existing CKA pilot data and the plan_013 completed results to ground the predictions properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d8e83d6-b27b-4c21-96ee-439e527d93e0",
  "isSidechain": false,
  "requestId": "req_011CbF7iGdV7wNYRDFqEz38f",
  "type": "assistant",
  "uuid": "9c4aba63-37f1-45da-80c4-e8723de583aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193aWptsaeEei96PKSwpfRU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39312,
      "cache_read_input_tokens": 33760,
      "output_tokens": 10837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10837,
          "cache_read_input_tokens": 33760,
          "cache_creation_input_tokens": 39312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39312
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

_source line 23 · 2026-05-21T04:58:02.962Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WD86sHo9TXvhPpkLpXQvqW`</summary>

```json
{
  "pattern": "**/cka_*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c4aba63-37f1-45da-80c4-e8723de583aa",
  "isSidechain": false,
  "requestId": "req_011CbF7iGdV7wNYRDFqEz38f",
  "type": "assistant",
  "uuid": "489a0625-c96a-48aa-aa5b-1af3bd3a0173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193aWptsaeEei96PKSwpfRU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39312,
      "cache_read_input_tokens": 33760,
      "output_tokens": 10837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10837,
          "cache_read_input_tokens": 33760,
          "cache_creation_input_tokens": 39312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39312
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

_source line 24 · 2026-05-21T04:58:02.981Z_

<details><summary>↩ Tool result · `toolu_01WD86sHo9TXvhPpkLpXQvqW`</summary>

```text
projects/xling_calib_direction/artifacts/_project/report/cka_vs_degradation_report.md
projects/xling_calib_direction/artifacts/cka_mvp_full_results.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "489a0625-c96a-48aa-aa5b-1af3bd3a0173",
  "isSidechain": false,
  "promptId": "71f7a31c-faf5-4838-a851-ebac678d912c",
  "type": "user",
  "uuid": "d3743949-6c39-4358-858c-5d712eca4a4f",
  "toolUseResult": {
    "filenames": [
      "projects/xling_calib_direction/artifacts/_project/report/cka_vs_degradation_report.md",
      "projects/xling_calib_direction/artifacts/cka_mvp_full_results.md"
    ],
    "durationMs": 11,
    "numFiles": 2,
    "truncated": false
  },
  "sourceToolAssistantUUID": "489a0625-c96a-48aa-aa5b-1af3bd3a0173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T04:58:04.061Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EGsf96ccWobx698G2HLyzM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/meta.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3743949-6c39-4358-858c-5d712eca4a4f",
  "isSidechain": false,
  "requestId": "req_011CbF7iGdV7wNYRDFqEz38f",
  "type": "assistant",
  "uuid": "91f08030-9b07-4141-8b80-5db6e392687e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193aWptsaeEei96PKSwpfRU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39312,
      "cache_read_input_tokens": 33760,
      "output_tokens": 10837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10837,
          "cache_read_input_tokens": 33760,
          "cache_creation_input_tokens": 39312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39312
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：核心几何洞见（Simpson's Paradox）在双架构 × 20 语言上显著复现；CaCLR consistency loss 提供可测量迁移增益；所有 claims 完整保留 核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均显著 (p < 0.01…",
  "leafUuid": "91f08030-9b07-4141-8b80-5db6e392687e",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Simpson's Paradox reveals cross-lingual correctness probe transfer",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Tool result

_source line 28 · 2026-05-21T04:58:04.367Z_

<details><summary>↩ Tool result · reported error · `toolu_01EGsf96ccWobx698G2HLyzM`</summary>

```text
File content (71152 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91f08030-9b07-4141-8b80-5db6e392687e",
  "isSidechain": false,
  "promptId": "71f7a31c-faf5-4838-a851-ebac678d912c",
  "type": "user",
  "uuid": "a905ce1b-d1be-4a9f-bd55-b67539fa671d",
  "toolUseResult": "Error: File content (71152 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "91f08030-9b07-4141-8b80-5db6e392687e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T04:58:07.602Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NLNZG2a6gsZuYqbGs1cPtZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/cka_mvp_full_results.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a905ce1b-d1be-4a9f-bd55-b67539fa671d",
  "isSidechain": false,
  "requestId": "req_011CbF82gZeL3sUSc7sAr1H3",
  "type": "assistant",
  "uuid": "ef23b871-a5c4-4836-a62a-b8e003010d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkKxdWsay2CeapSMaEVU8Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10965,
      "cache_read_input_tokens": 73072,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 73072,
          "cache_creation_input_tokens": 10965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10965
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

_source line 30 · 2026-05-21T04:58:07.607Z_

<details><summary>↩ Tool result · `toolu_01NLNZG2a6gsZuYqbGs1cPtZ`</summary>

```text
1	# Full CKA Analysis: MVP Models
2	
3	**Date**: 2026-05-21
4	**Script**: `compute_cka.py` (Linear CKA, Kornblith et al. 2019)
5	**Data**: 14,042 parallel samples per language pair, MMLU domains
6	
7	---
8	
9	## 1. Qwen2.5-7B-Instruct (mvp_001)
10	
11	### Full CKA Matrix (en → target)
12	
13	| Layer | zh | ar | hi | sw | ko | **Mean** |
14	|-------|------|------|------|------|------|----------|
15	| 0 | 0.912 | 0.901 | 0.536 | 0.440 | 0.687 | **0.695** |
16	| 4 | 0.652 | 0.642 | 0.519 | 0.470 | 0.630 | **0.583** |
17	| 8 | 0.815 | 0.737 | 0.593 | 0.604 | 0.724 | **0.695** |
18	| 12 | 0.843 | 0.820 | 0.614 | 0.612 | 0.789 | **0.735** |
19	| 16 | 0.886 | 0.883 | 0.575 | 0.593 | 0.865 | **0.760** |
20	| 20 | 0.764 | 0.664 | 0.371 | 0.399 | 0.670 | **0.574** |
21	| 24 | 0.694 | 0.544 | 0.162 | 0.125 | 0.551 | **0.415** |
22	| 27 | 0.345 | 0.356 | 0.117 | 0.084 | 0.318 | **0.244** |
23	| **Mean** | **0.739** | **0.693** | **0.436** | **0.416** | **0.654** | |
24	
25	### Depth Profile
26	- Peak similarity at **layer 16** (mean CKA = 0.760)
27	- Sharp decline after layer 16: 0.760 → 0.574 → 0.415 → 0.244
28	- Layer 0→4 dip (0.695 → 0.583) then recovery through mid-layers
29	
30	---
31	
32	## 2. Llama-3.1-8B-Instruct (mvp_003)
33	
34	### Full CKA Matrix (en → target)
35	
36	| Layer | zh | ar | hi | sw | ko | **Mean** |
37	|-------|------|------|------|------|------|----------|
38	| 0 | 0.881 | 0.678 | 0.198 | 0.265 | 0.767 | **0.558** |
39	| 4 | 0.930 | 0.924 | 0.531 | 0.712 | 0.910 | **0.801** |
40	| 8 | 0.891 | 0.880 | 0.553 | 0.746 | 0.879 | **0.790** |
41	| 12 | 0.922 | 0.905 | 0.624 | 0.705 | 0.893 | **0.810** |
42	| 16 | 0.857 | 0.830 | 0.511 | 0.671 | 0.841 | **0.742** |
43	| 20 | 0.636 | 0.568 | 0.350 | 0.387 | 0.575 | **0.503** |
44	| 24 | 0.607 | 0.527 | 0.275 | 0.300 | 0.542 | **0.450** |
45	| 28 | 0.581 | 0.482 | 0.221 | 0.256 | 0.503 | **0.409** |
46	| 31 | 0.469 | 0.306 | 0.162 | 0.266 | 0.382 | **0.317** |
47	| **Mean** | **0.753** | **0.678** | **0.381** | **0.479** | **0.699** | |
48	
49	### Depth Profile
50	- Peak similarity at **layer 12** (mean CKA = 0.810)
51	- Layer 0 notably low (0.558) due to hi/sw tokenizer divergence at embedding layer
52	- Decline onset earlier than Qwen: layer 12→16 already drops 0.810→0.742
53	
54	---
55	
56	## 3. Cross-Model Comparison
57	
58	### Per-Layer Mean CKA
59	
60	| Depth (relative) | Qwen Layer | Qwen CKA | Llama Layer | Llama CKA |
61	|-------------------|------------|-----------|-------------|-----------|
62	| 0% | 0 | 0.695 | 0 | 0.558 |
63	| ~15% | 4 | 0.583 | 4 | 0.801 |
64	| ~30% | 8 | 0.695 | 8 | 0.790 |
65	| ~45% | 12 | 0.735 | 12 | 0.810 |
66	| ~60% | 16 | 0.760 | 16 | 0.742 |
67	| ~75% | 20 | 0.574 | 20 | 0.503 |
68	| ~85% | 24 | 0.415 | 24 | 0.450 |
69	| ~95% | 27 | 0.244 | 28 | 0.409 |
70	| 100% | — | — | 31 | 0.317 |
71	
72	### Key Patterns
73	
74	1. **Both models show monotonic CKA decline in upper layers** (layer 16/12 onward), confirming language-specific divergence deepens toward output.
75	
76	2. **Qwen peaks later (layer 16) vs Llama (layer 12)**: Qwen maintains higher cross-lingual alignment deeper into the network.
77	
78	3. **Qwen's final-layer CKA is lower** (0.244 at L27) **than Llama's** (0.317 at L31), despite Qwen having fewer layers — suggesting Qwen's representations diverge more sharply at the output.
79	
80	4. **Language ranking is consistent across models**: zh > ar/ko > sw > hi (with ko and ar swapping in some layers).
81	
82	5. **Llama layer 0 anomaly**: CKA at layer 0 is much lower for Llama (0.558) vs Qwen (0.695), driven by hi (0.198) and sw (0.265). This likely reflects tokenizer-level divergence at the embedding layer.
83	
84	### Per-Language Mean CKA Comparison
85	
86	| Language | Qwen | Llama | Delta |
87	|----------|------|-------|-------|
88	| zh | 0.739 | 0.753 | +0.014 |
89	| ar | 0.693 | 0.678 | −0.016 |
90	| ko | 0.654 | 0.699 | +0.045 |
91	| hi | 0.436 | 0.381 | −0.055 |
92	| sw | 0.416 | 0.479 | +0.063 |
93	
94	---
95	
96	## 4. Comparison with Prior cka_vs_degradation Analysis
97	
98	Prior analysis (from registry) established correlations between CKA and calibration transfer degradation:
99	
100	| Metric | Qwen | Llama |
101	|--------|------|-------|
102	| Spearman(CKA, degradation) | ρ=−0.309, p=0.053 | ρ=−0.519, p=0.001 |
103	| Interpretation | Marginal trend | Significant negative correlation |
104	
105	**Consistency check**: The full CKA run here matches the prior per-language means exactly (zh=0.739, ar=0.693, etc.), confirming data integrity.
106	
107	**Key insight**: The stronger CKA–degradation correlation in Llama aligns with Llama's sharper layer-0 anomaly and earlier CKA peak — suggesting Llama's cross-lingual representations are more heterogeneous across the depth axis, making layer selection for calibration transfer more critical.
108	
109	---
110	
111	## 5. CSV File Locations
112	
113	- Qwen2.5-7B: `westd-13176:/root/xling_calib_direction/results_cka_mvp001/cka_matrix_qwen25_7b.csv`
114	- Llama-3.1-8B: `westd-13176:/root/xling_calib_direction/results_cka_mvp003/cka_matrix_llama31_8b.csv`
115	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef23b871-a5c4-4836-a62a-b8e003010d91",
  "isSidechain": false,
  "promptId": "71f7a31c-faf5-4838-a851-ebac678d912c",
  "type": "user",
  "uuid": "4f0691fa-8610-429e-b09c-5d0459c2102b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/cka_mvp_full_results.md",
      "content": "# Full CKA Analysis: MVP Models\n\n**Date**: 2026-05-21\n**Script**: `compute_cka.py` (Linear CKA, Kornblith et al. 2019)\n**Data**: 14,042 parallel samples per language pair, MMLU domains\n\n---\n\n## 1. Qwen2.5-7B-Instruct (mvp_001)\n\n### Full CKA Matrix (en → target)\n\n| Layer | zh | ar | hi | sw | ko | **Mean** |\n|-------|------|------|------|------|------|----------|\n| 0 | 0.912 | 0.901 | 0.536 | 0.440 | 0.687 | **0.695** |\n| 4 | 0.652 | 0.642 | 0.519 | 0.470 | 0.630 | **0.583** |\n| 8 | 0.815 | 0.737 | 0.593 | 0.604 | 0.724 | **0.695** |\n| 12 | 0.843 | 0.820 | 0.614 | 0.612 | 0.789 | **0.735** |\n| 16 | 0.886 | 0.883 | 0.575 | 0.593 | 0.865 | **0.760** |\n| 20 | 0.764 | 0.664 | 0.371 | 0.399 | 0.670 | **0.574** |\n| 24 | 0.694 | 0.544 | 0.162 | 0.125 | 0.551 | **0.415** |\n| 27 | 0.345 | 0.356 | 0.117 | 0.084 | 0.318 | **0.244** |\n| **Mean** | **0.739** | **0.693** | **0.436** | **0.416** | **0.654** | |\n\n### Depth Profile\n- Peak similarity at **layer 16** (mean CKA = 0.760)\n- Sharp decline after layer 16: 0.760 → 0.574 → 0.415 → 0.244\n- Layer 0→4 dip (0.695 → 0.583) then recovery through mid-layers\n\n---\n\n## 2. Llama-3.1-8B-Instruct (mvp_003)\n\n### Full CKA Matrix (en → target)\n\n| Layer | zh | ar | hi | sw | ko | **Mean** |\n|-------|------|------|------|------|------|----------|\n| 0 | 0.881 | 0.678 | 0.198 | 0.265 | 0.767 | **0.558** |\n| 4 | 0.930 | 0.924 | 0.531 | 0.712 | 0.910 | **0.801** |\n| 8 | 0.891 | 0.880 | 0.553 | 0.746 | 0.879 | **0.790** |\n| 12 | 0.922 | 0.905 | 0.624 | 0.705 | 0.893 | **0.810** |\n| 16 | 0.857 | 0.830 | 0.511 | 0.671 | 0.841 | **0.742** |\n| 20 | 0.636 | 0.568 | 0.350 | 0.387 | 0.575 | **0.503** |\n| 24 | 0.607 | 0.527 | 0.275 | 0.300 | 0.542 | **0.450** |\n| 28 | 0.581 | 0.482 | 0.221 | 0.256 | 0.503 | **0.409** |\n| 31 | 0.469 | 0.306 | 0.162 | 0.266 | 0.382 | **0.317** |\n| **Mean** | **0.753** | **0.678** | **0.381** | **0.479** | **0.699** | |\n\n### Depth Profile\n- Peak similarity at **layer 12** (mean CKA = 0.810)\n- Layer 0 notably low (0.558) due to hi/sw tokenizer divergence at embedding layer\n- Decline onset earlier than Qwen: layer 12→16 already drops 0.810→0.742\n\n---\n\n## 3. Cross-Model Comparison\n\n### Per-Layer Mean CKA\n\n| Depth (relative) | Qwen Layer | Qwen CKA | Llama Layer | Llama CKA |\n|-------------------|------------|-----------|-------------|-----------|\n| 0% | 0 | 0.695 | 0 | 0.558 |\n| ~15% | 4 | 0.583 | 4 | 0.801 |\n| ~30% | 8 | 0.695 | 8 | 0.790 |\n| ~45% | 12 | 0.735 | 12 | 0.810 |\n| ~60% | 16 | 0.760 | 16 | 0.742 |\n| ~75% | 20 | 0.574 | 20 | 0.503 |\n| ~85% | 24 | 0.415 | 24 | 0.450 |\n| ~95% | 27 | 0.244 | 28 | 0.409 |\n| 100% | — | — | 31 | 0.317 |\n\n### Key Patterns\n\n1. **Both models show monotonic CKA decline in upper layers** (layer 16/12 onward), confirming language-specific divergence deepens toward output.\n\n2. **Qwen peaks later (layer 16) vs Llama (layer 12)**: Qwen maintains higher cross-lingual alignment deeper into the network.\n\n3. **Qwen's final-layer CKA is lower** (0.244 at L27) **than Llama's** (0.317 at L31), despite Qwen having fewer layers — suggesting Qwen's representations diverge more sharply at the output.\n\n4. **Language ranking is consistent across models**: zh > ar/ko > sw > hi (with ko and ar swapping in some layers).\n\n5. **Llama layer 0 anomaly**: CKA at layer 0 is much lower for Llama (0.558) vs Qwen (0.695), driven by hi (0.198) and sw (0.265). This likely reflects tokenizer-level divergence at the embedding layer.\n\n### Per-Language Mean CKA Comparison\n\n| Language | Qwen | Llama | Delta |\n|----------|------|-------|-------|\n| zh | 0.739 | 0.753 | +0.014 |\n| ar | 0.693 | 0.678 | −0.016 |\n| ko | 0.654 | 0.699 | +0.045 |\n| hi | 0.436 | 0.381 | −0.055 |\n| sw | 0.416 | 0.479 | +0.063 |\n\n---\n\n## 4. Comparison with Prior cka_vs_degradation Analysis\n\nPrior analysis (from registry) established correlations between CKA and calibration transfer degradation:\n\n| Metric | Qwen | Llama |\n|--------|------|-------|\n| Spearman(CKA, degradation) | ρ=−0.309, p=0.053 | ρ=−0.519, p=0.001 |\n| Interpretation | Marginal trend | Significant negative correlation |\n\n**Consistency check**: The full CKA run here matches the prior per-language means exactly (zh=0.739, ar=0.693, etc.), confirming data integrity.\n\n**Key insight**: The stronger CKA–degradation correlation in Llama aligns with Llama's sharper layer-0 anomaly and earlier CKA peak — suggesting Llama's cross-lingual representations are more heterogeneous across the depth axis, making layer selection for calibration transfer more critical.\n\n---\n\n## 5. CSV File Locations\n\n- Qwen2.5-7B: `westd-13176:/root/xling_calib_direction/results_cka_mvp001/cka_matrix_qwen25_7b.csv`\n- Llama-3.1-8B: `westd-13176:/root/xling_calib_direction/results_cka_mvp003/cka_matrix_llama31_8b.csv`\n",
      "numLines": 115,
      "startLine": 1,
      "totalLines": 115
    }
  },
  "sourceToolAssistantUUID": "ef23b871-a5c4-4836-a62a-b8e003010d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T04:58:08.045Z_

<details open><summary>🔧 Tool call — Read · `toolu_018PkEj8w2YhMEw8uEAmv7XS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/_project/report/cka_vs_degradation_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f0691fa-8610-429e-b09c-5d0459c2102b",
  "isSidechain": false,
  "requestId": "req_011CbF82gZeL3sUSc7sAr1H3",
  "type": "assistant",
  "uuid": "04b50718-a0ed-4a35-81f4-a330ce2e817b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkKxdWsay2CeapSMaEVU8Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10965,
      "cache_read_input_tokens": 73072,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 73072,
          "cache_creation_input_tokens": 10965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10965
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

_source line 32 · 2026-05-21T04:58:08.049Z_

<details><summary>↩ Tool result · `toolu_018PkEj8w2YhMEw8uEAmv7XS`</summary>

```text
1	# CKA vs Transfer Degradation Analysis
2	
3	## Qwen2.5-7B-Instruct (mvp_001)
4	- Overall Spearman(CKA, degradation): rho=-0.3086, p=0.0527 (marginal)
5	- Per-language: no individual language reaches significance
6	
7	## Llama-3.1-8B-Instruct (mvp_003)
8	- Overall Spearman(CKA, degradation): rho=-0.5192, p=0.0012 **
9	- Per-language: hi significant (rho=-0.7333, p=0.025)
10	
11	## Cross-model comparison
12	| Lang | Qwen_CKA | Llama_CKA | Qwen_Deg | Llama_Deg |
13	|------|----------|-----------|----------|-----------|
14	| zh   | 0.7388   | 0.7527    | 0.1148   | 0.1462    |
15	| ar   | 0.6934   | 0.6776    | 0.1542   | 0.1698    |
16	| ko   | 0.6559   | N/A       | 0.1516   | N/A       |
17	| hi   | 0.4359   | 0.3805    | 0.2164   | 0.1698    |
18	| sw   | 0.4158   | 0.4788    | 0.2246   | 0.2090    |
19	
20	## Language ranking
21	- By CKA: zh > ar > {ko} > sw/hi (both models agree on top-2 and bottom-2)
22	- By degradation: zh < ar < {ko} < hi < sw (consistent)
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04b50718-a0ed-4a35-81f4-a330ce2e817b",
  "isSidechain": false,
  "promptId": "71f7a31c-faf5-4838-a851-ebac678d912c",
  "type": "user",
  "uuid": "582051fd-feff-4edf-bb66-177c7bafdd7a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/_project/report/cka_vs_degradation_report.md",
      "content": "# CKA vs Transfer Degradation Analysis\n\n## Qwen2.5-7B-Instruct (mvp_001)\n- Overall Spearman(CKA, degradation): rho=-0.3086, p=0.0527 (marginal)\n- Per-language: no individual language reaches significance\n\n## Llama-3.1-8B-Instruct (mvp_003)\n- Overall Spearman(CKA, degradation): rho=-0.5192, p=0.0012 **\n- Per-language: hi significant (rho=-0.7333, p=0.025)\n\n## Cross-model comparison\n| Lang | Qwen_CKA | Llama_CKA | Qwen_Deg | Llama_Deg |\n|------|----------|-----------|----------|-----------|\n| zh   | 0.7388   | 0.7527    | 0.1148   | 0.1462    |\n| ar   | 0.6934   | 0.6776    | 0.1542   | 0.1698    |\n| ko   | 0.6559   | N/A       | 0.1516   | N/A       |\n| hi   | 0.4359   | 0.3805    | 0.2164   | 0.1698    |\n| sw   | 0.4158   | 0.4788    | 0.2246   | 0.2090    |\n\n## Language ranking\n- By CKA: zh > ar > {ko} > sw/hi (both models agree on top-2 and bottom-2)\n- By degradation: zh < ar < {ko} < hi < sw (consistent)\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "04b50718-a0ed-4a35-81f4-a330ce2e817b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T05:00:58.002Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full CKA pilot data. Let me finalize my understanding:

For the Simpson's Paradox analysis:
- The MVP data shows CKA vs degradation (NOT transfer AUROC) correlation
- Qwen: rho=-0.31, p=0.053 (marginal) - higher CKA → less degradation
- Llama: rho=-0.52, p=0.001 (significant) - higher CKA → less degradation

The paper framing talks about "CKA-transfer relationship" where "raw correlation negative." This must be CKA vs transfer AUROC (absolute performance), not degradation.


So I'm checking the layer-by-layer pattern: at layer 16 where CKA is high (0.760), transfer AUROC is moderate (~0.60), but at layer 27 where CKA drops to 0.244, transfer AUROC jumps higher (~0.686). This inverse relationship confirms the negative raw correlation between CKA and absolute transfer performance.

But wait—this is actually Simpson's Paradox at work. Depth is confounding everything: deeper layers naturally produce better probes with higher AUROC, yet deeper layers also show lower CKA values. When I look within individual layers across languages, the pattern flips. At layer 16, higher CKA in Chinese (0.886) corresponds to higher transfer (~0.60) compared to Swahili's lower CKA (0.593) and lower transfer (~0.52). So within each layer, CKA genuinely predicts transfer quality positively.

For the full analysis, I need to disentangle this by computing the raw pooled correlation across all layers and languages, then the partial correlation controlling for normalized depth, plus per-layer correlations within each of the 20 languages to isolate the true relationship.

Now I'm checking what the partial correlation actually looks like across the full dataset. With Qwen's ~480 data points (20 languages × 24 layers) and Llama's ~240 points (20 languages × 12 layers), the partial correlation controlling for depth shows a strong positive relationship—around +0.45 for Qwen and +0.39 for Llama—both highly significant given the sample sizes.

But the reported p-value range of [0.001, 0.01] seems odd for these effect sizes and sample sizes, which would typically yield p << 0.001. This makes me wonder if the analysis is computed per-layer instead of on the pooled data, or if there's a different statistical approach being used. The plan notes emphasize this partial correlation analysis as critical, so I need to figure out exactly how it's being calculated. Now I see the issue — if they're computing per-layer correlations with just n=20 languages per layer, a correlation of 0.45 only gives t≈2.14 and p≈0.046, which is barely significant. That's probably why the p-value range tops out at 0.01 rather than being much smaller.

The partial correlation on pooled data (n=240 across all layers and languages) would give a much smaller p-value, likely well below 0.001. So the reported p_value_max of [0.001, 0.01] might be capturing the worst-case per-layer test rather than the pooled analysis, or there's some correction I'm not accounting for. Let me just work with internally consistent numbers — setting Qwen's partial correlation to around 0.48 should fit within these constraints. I'm settling on these final numbers: Qwen3 shows a raw correlation of -0.36 that flips to +0.48 when controlling for depth (p=0.002), while Llama4 goes from -0.41 to +0.41 (p=0.008), both using bootstrap confidence intervals. For the per-layer analysis with 20 languages, I'd expect roughly 20-25% of layers to reach significance at p<0.05, which aligns with seeing 5 significant layers out of 24 for Qwen and 3 out of 12 for Llama. Now I'm ready to write out the YAML with comprehensive predictions, making sure the Qwen3-235B Pareto front is particularly strong and consistent across languages.

Compiling the per-language correlations for Qwen3-235B, showing layer depth versus transfer performance across all 20 languages with strong negative correlations...

For Llama 4 Scout, the pattern shifts dramatically—most languages still show negative correlations but much weaker, and critically, Arabic, Hindi, and Korean flip to positive correlations, meaning deeper layers actually improve transfer performance in those languages. The median hovers near zero, indicating this model lacks the consistent depth-performance relationship that Qwen3-235B exhibits so strongly.

Looking at the global Spearman correlations across layers, both architectures show statistically significant negative relationships between depth and transfer AUROC, though Qwen3's effect is substantially stronger. This confirms the pareto frontier pattern holds across both models. Now I'm circling back to something about CaCLR—the paper suggests it's a positive contribution in the best tier, but I need to reconcile that with what I'm actually seeing in the data.

The CaCLR gains aren't uniform across layers. Shallow layers where zero-shot transfer already performs well see minimal improvement, but the deeper layers where capability-specific degradation becomes pronounced show much stronger gains, peaking around 60-80% depth where the gap is widest before tapering slightly at the very deepest layers.

Across all layers and languages, I'm seeing roughly 3.5pp improvement on average, with deep layers alone averaging around 4pp—both meeting the ≥2pp threshold at depth and staying within the expected improvement range.

The β parameter sweep shows a clear sweet spot around 0.05, where the consistency loss is strong enough to help but not so dominant that it overwhelms the probe accuracy. Values too low barely move the needle, while values above 0.1 let the MMD term take over and actually hurt performance.

For the α calibration sweep, I'm finding that 0.1 gives the best balance—boosting AUROC by 0.8pp while cutting ECE by over 3pp. Beyond that, the calibration term becomes too aggressive and starts degrading the main metric.

Now I need to structure this into a comprehensive YAML output with the tier, narrative guidance, and imagined experiments the user is expecting.

There's a key architectural consideration I need to flag: plan_002 uses Llama 4 Scout, which is a mixture-of-experts model, whereas the MVP baseline was Llama-3.1-8B, a dense model. The hypothesis assumes the weak tradeoff pattern transfers across architectures, which is reasonable given both are from the Llama family with similar multilingual training, but it's worth noting this assumption explicitly.

Now I'm validating the constraint ranges and pass rates across models. The en_best_auroc needs to stay between 0.77 and 0.83, which both Qwen3-235B at 0.81 and Llama 4 Scout at 0.79 satisfy. For the zero-shot pass rate across 20 languages, I'm working out which languages fail for each model to hit the target distribution—Qwen3 at 18/20 and Llama 4 at 16/20. I'm reconsidering the failure thresholds for Llama4 across the low-resource languages. Bengali shouldn't actually fail given Llama's strong support for Indic languages, so I need to adjust which languages are dropping below the 0.60 cutoff—Yoruba is definitely failing at 0.54, but I should verify the others more carefully before finalizing the pass/fail counts. with Qwen3 hitting 18/20 and Llama4 at 17/20, both landing solidly in that 0.8-0.9 range. Now I need to write out the full YAML output. Actually, I should include the P2 experiments too since they're part of the plan. Let me think about how much detail each experiment deserves—the core ones like plan_011 with the CKA and Simpson's analysis need the most depth, then plan_001/002 for the Pareto findings and plan_003 for CaCLR, while the others like plan_004 on decomposition and plan_012 can get moderate coverage.

For the supporting experiments I'll keep things brief—plan_005 through plan_010 just need enough to show they're there. The camera-ready predictions for plan_008 and plan_009 can be even shorter. I'm aiming for roughly 30-40 lines on the core ones, 15-25 for the important middle tier, and 10-15 for the supporting work.

Each experiment entry needs the name, plan_id, description, expected_results as a dict, result_rationale, tables, figures, and analysis sections. Let me structure the expected_results carefully since that's the foundation for everything else.

I need to be precise about the AUROC scaling—the MVP models hit 0.754 and 0.728 on English, but the full-scale versions (Qwen3-235B and Llama 4 Scout) should show meaningful gains. From the probing literature, accuracy scales roughly logarithmically with parameter count, so jumping from 7-8B to 109-235B should give a solid improvement. I'm working out where that lands...

Writing YAML structure... .81 is ~5.6pp gain. This is reasonable.

Similarly, 8B to 109B (Llama 4 Scout effective size): ~1.1 orders of magnitude. From 0.728 to 0.79 is ~6.2pp gain. Also reasonable.

The transfer gap (EN - mean ZS) should be proportionally maintained or slightly improved with scale.

MVP Qwen: EN=0.754, mean ZS≈0.639, gap≈0.115 (15.3%)
Full Qwen3: EN=0.81, gap should be similar → mean ZS≈0.703

MVP Llama: EN=0.728, mean ZS≈0.619, gap≈0.109 (15.0%)  
Full Llama4: EN=0.79 → mean ZS≈0.672

With improved multilingual capabilities at scale, I'd expect Qwen3 mean ZS around 0.72 and Llama4 around 0.70, which feel reasonable. Now I need to be careful about what I'm actually measuring—the zero-shot mean at the best transfer layer versus the best per-language AUROC across all layers. The Pareto tradeoff is between EN performance improving with depth and transfer performance potentially declining, so when I cite a specific zero-shot mean, that's at a particular layer balancing these competing objectives.

Different languages will have different optimal layers, so a fixed-layer result is conservative compared to an oracle that picks the best layer per language—I'd expect roughly 2-3 percentage points difference between them. I should report both approaches to show the full picture.

Now looking at how the architecture shapes this tradeoff: Qwen3-235B shows a clear, consistent pattern where deeper layers help English but hurt zero-shot performance across the board, while Llama 4 Scout has a weaker and more inconsistent tradeoff where some languages actually benefit from deeper layers. The key insight is that the Pareto frontier's shape depends on the architecture, even though both models exhibit a statistically significant global tradeoff.

Let me now work through the experiments methodically, writing out the YAML with all the necessary fields and rationale. I need to be careful about the CaCLR design—since linear probes produce 1-D logits, the MMD calculation operates in that 1-D space, which is worth noting in the rationale.

The key insight is that even in 1-D, MMD can align the distributions of logit values across languages by penalizing differences in how the probe scores English versus target language data. The joint optimization of the probe with the MMD penalty, combined with the BCE loss keeping English accuracy intact, forces the probe to discover language-invariant features that generalize across languages.

However, this 1-D constraint is fundamentally limiting — CaCLR can only align the scalar projection, not the full representational geometry that linear probes can capture in the full activation space. The comparable performance between the two methods (around 2-3.5pp improvement) suggests that 1-D alignment captures most of the benefit, though higher-dimensional MMD operating on activations rather than logits might close the remaining gap. But there's a constraint in the experimental plan that MMD must operate on logits specifically, not activations.

Looking at the actual design, this makes sense: the probe parameters need to be optimized, and the MMD gradient must flow through them. If MMD operated on raw activations (which are fixed for a given model layer), there'd be no gradient signal for the probe to learn from. So the pipeline is activations feeding into the probe to produce logits, then both BCE loss on English logits and MMD loss comparing English and target-language logits, with gradients flowing back through the probe parameters. The 1-D limitation is just inherent to how linear probes work.

For the best tier, the probe learns a direction in activation space that produces similar logit distributions across languages. This direction aligns with what CKA analysis shows as the universal correctness direction, and the MMD loss nudges the probe toward that universal direction even if it means sacrificing some English-specific accuracy for better cross-lingual transfer. This is a coherent story to include in the CaCLR rationale.

Now I need to actually start writing instead of continuing to deliberate. The original document was around 1350 lines, so my new version should be comparable or slightly longer to fit the additional experiments. I'll keep each experiment entry self-contained and well-reasoned, and I'm doing a final check on numerical consistency across the model results.

Generating metrics table... Generating metrics table... Now I'm ready to generate the YAML configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "582051fd-feff-4edf-bb66-177c7bafdd7a",
  "isSidechain": false,
  "requestId": "req_011CbF82xmiZknd8Hr1wRkiY",
  "type": "assistant",
  "uuid": "3e6ac0c6-ff6b-419f-ab51-b962a8046e86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dpECXeFkfBweXYd6b9omE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 84037,
      "output_tokens": 27213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 27213,
          "cache_read_input_tokens": 84037,
          "cache_creation_input_tokens": 3173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3173
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

_source line 34 · 2026-05-21T05:07:14.053Z_

I have all the data needed. Now I'll produce the complete best-tier imagined experiments, integrating the MVP pilot data, CKA analysis, and the revised framing with Simpson's Paradox as core novelty.

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。以 Simpson's Paradox 几何洞见为核心新颖性开篇——
  raw CKA-transfer correlation 为负（depth confound），partial correlation controlling
  for depth 在双架构上均显著为正（p < 0.01），揭示 within-layer CKA genuinely predicts
  transfer quality。CaCLR 作为正面方法贡献（+3.5pp mean over ZS），不是 headline 但
  构成因果链第三环。标题强调 'geometric analysis reveals when and why cross-lingual
  calibration transfer succeeds'。四条 claim 完整因果链保留：Pareto discovery（architecture-
  dependent depth-transferability tradeoff）→ Decomposition analysis（difficulty vs
  capability separation）→ CaCLR method（consistency loss provides measurable gain at
  deep layers）→ CKA geometric explanation（Simpson's Paradox, subspace persistence）。
  Control task warning（28% low-resource artifacts）和 linear projection sample efficiency
  （~42 pairs to 95%）作为加分实证贡献。Procrustes effect reversal（threshold ~0.52）
  为 practitioner 提供直接指导。无需弱化任何 claims。

imagined_experiments:

  ###################################################################
  # plan_001: Full Pareto — Qwen3-235B-A22B
  ###################################################################
  - name: "Full Pareto Frontier — Qwen3-235B-A22B"
    plan_id: plan_001
    description: >
      94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th),
      20 typologically diverse languages, English logistic regression probes,
      5 transfer conditions: zero-shot, mean-shift, linear projection (200 pairs),
      few-shot 25/100, CaCLR。重点验证 MVP 发现的 strong depth-transferability
      tradeoff 是否在大模型上保持。
    expected_results:
      en_best_auroc: 0.81
      en_best_layer_idx: 72
      en_auroc_range: [0.58, 0.81]
      en_ece_raw_best: 0.168
      zs_mean_auroc_20lang_best_transfer_layer: 0.72
      zs_best_transfer_layer_idx: 52
      zs_pass_rate_20lang: 0.90
      zs_fail_langs: [yo, te]
      zs_auroc_by_tier:
        HIGH_mean: 0.76
        MID_mean: 0.72
        LOW_mean: 0.63
      zs_auroc_selected:
        zh: 0.77
        es: 0.76
        fr: 0.76
        de: 0.77
        ja: 0.75
        nl: 0.76
        pt: 0.75
        it: 0.75
        ar: 0.73
        hi: 0.71
        ko: 0.72
        tr: 0.71
        ru: 0.74
        vi: 0.70
        th: 0.69
        sw: 0.63
        bn: 0.65
        yo: 0.57
        ig: 0.61
        te: 0.58
      per_lang_spearman_rho_median: -0.64
      per_lang_significant_at_005: 15  # out of 20
      global_spearman_rho: -0.91
      global_spearman_p: 0.0001
      pareto_frontier_layers: [40, 44, 48, 52, 56]
      pareto_en_zs_gap_at_knee_pp: 4.2
      mean_shift_delta_auroc: 0.000
      linproj_200pairs_mean_auroc: 0.740
      fewshot_25_mean_auroc: 0.708
      fewshot_100_mean_auroc: 0.735
    result_rationale: >
      Qwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 3×，log-linear probing
      scaling 预期 EN AUROC 从 0.754 提升至 ~0.81。94 层深网络使 depth-transferability
      tradeoff 比 28 层 MVP 更显著：EN-optimal layer (L72, 77% depth) 与 ZS-optimal
      layer (L52, 55% depth) 之间有 20 层间隔（MVP 仅 3 层）。Strong Pareto 源于
      Qwen 架构特征：MoE routing 在深层产生 language-specific expert 激活模式，
      导致 correctness direction 的 cross-lingual alignment 在 L60 后急剧下降。
      15/20 languages 的 per-language Spearman rho 显著为负，表明 tradeoff 是
      跨语言一致的。2 个 fail 语言（yo, te）的 AUROC < 0.60 因为 Qwen3 pretraining
      corpus 中 Yoruba/Telugu 占比极低（<0.1%），embedding 层的 representation
      quality 即不足以支撑 correctness signal。Mean-shift ΔAUROC ≡ 0 因为
      StandardScaler + LR 下 mean-shift 对 AUROC 无影响（已在 MVP 中数学证明）。
      Linear projection (200 pairs) 提供 +2pp 因为 Procrustes alignment 捕获了
      correctness subspace 的旋转，但不触及 distributional matching。
    tables:
      - name: "Table 1: Qwen3-235B Pareto Frontier (selected layers)"
        columns: [layer_idx, depth_pct, en_auroc, zs_mean_20, zs_drop_pp, on_pareto]
        rows:
          - [4,    4,  0.580, 0.572, 0.8, false]
          - [12,  13,  0.645, 0.632, 1.3, false]
          - [20,  21,  0.710, 0.695, 1.5, false]
          - [28,  30,  0.752, 0.733, 1.9, false]
          - [36,  38,  0.778, 0.752, 2.6, false]
          - [40,  43,  0.788, 0.748, 4.0, true]
          - [44,  47,  0.796, 0.740, 5.6, true]
          - [48,  51,  0.802, 0.732, 7.0, true]
          - [52,  55,  0.806, 0.720, 8.6, true]
          - [56,  60,  0.808, 0.706, 10.2, true]
          - [60,  64,  0.810, 0.690, 12.0, false]
          - [68,  72,  0.810, 0.661, 14.9, false]
          - [72,  77,  0.810, 0.638, 17.2, false]
          - [80,  85,  0.805, 0.601, 20.4, false]
          - [88,  94,  0.792, 0.558, 23.4, false]
          - [92,  98,  0.778, 0.531, 24.7, false]
      - name: "Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3"
        columns: [language, tier, spearman_rho, p_value, significant]
        rows:
          - [zh, HIGH, -0.72, 0.001, yes]
          - [es, HIGH, -0.68, 0.002, yes]
          - [fr, HIGH, -0.70, 0.001, yes]
          - [de, HIGH, -0.69, 0.002, yes]
          - [ja, HIGH, -0.74, 0.001, yes]
          - [nl, HIGH, -0.67, 0.003, yes]
          - [pt, MID,  -0.65, 0.004, yes]
          - [it, MID,  -0.66, 0.003, yes]
          - [ar, MID,  -0.71, 0.001, yes]
          - [hi, MID,  -0.63, 0.005, yes]
          - [ko, MID,  -0.67, 0.003, yes]
          - [tr, MID,  -0.62, 0.006, yes]
          - [ru, MID,  -0.69, 0.002, yes]
          - [vi, MID,  -0.61, 0.008, yes]
          - [th, MID,  -0.58, 0.012, yes]
          - [sw, LOW,  -0.52, 0.025, yes]
          - [bn, LOW,  -0.55, 0.018, no]
          - [yo, LOW,  -0.48, 0.042, no]
          - [ig, LOW,  -0.51, 0.028, no]
          - [te, LOW,  -0.45, 0.058, no]
    figures_description:
      - >
        Figure 1a: Pareto frontier scatter (EN AUROC x-axis vs ZS mean AUROC
        y-axis), 24 points, 5 Pareto-optimal layers marked red. Clear convex
        knee at ~55% depth.
      - >
        Figure 1b: Heatmap — ZS AUROC by language (y-axis, ordered by resource
        tier) × normalized depth (x-axis). Warm mid-band, low-resource rows
        cool earlier at shallower depth than high-resource rows.
    analysis: >
      Qwen3-235B 展现 strong, consistent depth-transferability tradeoff：
      global Spearman ρ = -0.91 (p < 0.001), 15/20 per-language ρ 显著为负。
      Pareto frontier 包含 5 层 (L40-L56)，knee 在 ~55% depth。EN-optimal
      (L72) 与 ZS-optimal (L52) 相隔 20 层 / 22pp depth，远大于 MVP 的 3 层
      间隔。这证实 tradeoff 在大模型上不是减弱而是放大——更深的网络有更多
      空间进行 language-specific specialization。High-resource 语言在 Pareto
      knee 以下也保持 AUROC > 0.74，但 low-resource 在 70% depth 后急剧下降。
      这与 CKA 分析一致：CKA 在 L60 后的 cliff 解释了为何 deep-layer transfer
      对 low-resource 影响更大（CKA 基线更低，cliff 更早触及）。

  ###################################################################
  # plan_002: Full Pareto — Llama 4 Scout
  ###################################################################
  - name: "Full Pareto Frontier — Llama 4 Scout"
    plan_id: plan_002
    description: >
      48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every 4th),
      20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B 的 weak/mixed
      tradeoff pattern 是否是 Llama 架构家族特征。
    expected_results:
      en_best_auroc: 0.79
      en_best_layer_idx: 36
      en_auroc_range: [0.56, 0.79]
      en_ece_raw_best: 0.182
      zs_mean_auroc_20lang_best_transfer_layer: 0.70
      zs_best_transfer_layer_idx: 28
      zs_pass_rate_20lang: 0.85
      zs_fail_langs: [yo, te, ig]
      zs_auroc_by_tier:
        HIGH_mean: 0.74
        MID_mean: 0.70
        LOW_mean: 0.61
      per_lang_spearman_rho_median: -0.28
      per_lang_significant_at_005: 6   # out of 20
      per_lang_positive_rho_langs: [ar, hi, ko]
      global_spearman_rho: -0.78
      global_spearman_p: 0.003
      pareto_frontier_layers: [20, 24, 28]
      mean_shift_delta_auroc: 0.000
      linproj_200pairs_mean_auroc: 0.718
      fewshot_25_mean_auroc: 0.692
      fewshot_100_mean_auroc: 0.718
    result_rationale: >
      Llama 4 Scout 延续 MVP Llama-3.1-8B 的 weak tradeoff 模式。虽然 global
      Spearman ρ = -0.78 仍然显著（12 data points, p=0.003），但 per-language
      分析揭示了明显的异质性：仅 6/20 languages 有显著负 ρ，而 ar/hi/ko
      展现正 ρ（深层 transfer 反而改善）。这与 MVP 完全一致（ar/ko 在 L31
      优于 L20），且可归因于 Llama 架构的 multilingual training recipe：Meta
      的训练策略使 ar/hi/ko 在深层保持更好的 cross-lingual alignment，可能
      因为这些语言在 pretraining 中与 English 有更多 code-switching 数据。
      Global rho 仍然显著是因为大多数语言确实有弱负趋势，但 per-language
      分析揭示这不是 universal pattern。与 Qwen3 的对比清晰：Qwen3 的 15/20
      significant vs Llama4 的 6/20，median rho -0.64 vs -0.28。这一
      architecture-dependent tradeoff strength 是 Claim 1 的核心发现。
    tables:
      - name: "Table 3: Llama 4 Scout Pareto Frontier"
        columns: [layer_idx, depth_pct, en_auroc, zs_mean_20, zs_drop_pp, on_pareto]
        rows:
          - [4,   8,  0.560, 0.552, 0.8, false]
          - [8,  17,  0.635, 0.625, 1.0, false]
          - [12, 25,  0.695, 0.682, 1.3, false]
          - [16, 33,  0.735, 0.718, 1.7, false]
          - [20, 42,  0.758, 0.724, 3.4, true]
          - [24, 50,  0.772, 0.714, 5.8, true]
          - [28, 58,  0.782, 0.700, 8.2, true]
          - [32, 67,  0.789, 0.681, 10.8, false]
          - [36, 75,  0.790, 0.655, 13.5, false]
          - [40, 83,  0.785, 0.625, 16.0, false]
          - [44, 92,  0.772, 0.589, 18.3, false]
          - [48, 100, 0.748, 0.548, 20.0, false]
      - name: "Table 4: Architecture-Dependent Pareto Comparison"
        columns: [metric, Qwen3_235B, Llama4_Scout, interpretation]
        rows:
          - [global_rho, -0.91, -0.78, "both significant but Qwen stronger"]
          - [per_lang_sig_count, "15/20", "6/20", "Qwen consistent, Llama mixed"]
          - [median_per_lang_rho, -0.64, -0.28, "2.3x difference in effect size"]
          - [positive_rho_langs, 0, 3, "Llama has ar/hi/ko reversed"]
          - [best_transfer_depth_pct, 55, 58, "comparable location"]
          - [en_zs_gap_at_knee_pp, 4.2, 3.4, "comparable magnitude"]
      - name: "Table 5: Transfer Conditions Comparison (both models, at best-transfer layer)"
        columns: [condition, Qwen3_mean_20, Llama4_mean_20, combined_mean]
        rows:
          - [zero-shot,           0.720, 0.700, 0.710]
          - [mean-shift,          0.720, 0.700, 0.710]
          - [linear_proj_200,     0.740, 0.718, 0.729]
          - [few-shot-25,         0.708, 0.692, 0.700]
          - [few-shot-100,        0.735, 0.718, 0.727]
    figures_description:
      - >
        Figure 2: Overlaid Pareto frontiers (normalized depth), Qwen3 in blue,
        Llama4 in orange. Qwen3 shifted up-right with steeper descent; Llama4
        flatter with more scatter at deep layers.
      - >
        Figure 3: Per-language Spearman ρ distribution: Qwen3 (left) tightly
        clustered around -0.65; Llama4 (right) spread from -0.50 to +0.35,
        ar/hi/ko clearly positive.
    analysis: >
      Architecture-dependent Pareto strength 是 Claim 1 的核心。两个架构的
      global rho 都显著（满足 pareto_spearman_rho_significant_archs = 2 的
      约束），但 effect size 差异明显。Qwen3 的 strong tradeoff 意味着
      practitioner 必须在 EN accuracy 和 transfer quality 之间做明确选择；
      Llama4 的 weak tradeoff 意味着某些语言（ar, hi, ko）可以 "free-ride"
      深层的 EN improvement 而不牺牲 transfer。这一差异无法从 domain
      adaptation theory 预测——它是架构特有的 empirical finding。
      Best-transfer depth 在两个架构上收敛至 55-58%，暗示一个 universal
      "mid-depth transfer zone"，但 frontier 的 steepness 是
      architecture-specific。

  ###################################################################
  # plan_011: CKA / Simpson's Paradox Analysis (CORE NOVELTY)
  ###################################################################
  - name: "CKA Cross-Lingual Similarity & Simpson's Paradox Analysis"
    plan_id: plan_011
    description: >
      Linear CKA (EN vs each target) at every probed layer, 20 languages × 2
      models。核心分析：(a) same-layer cross-language correlation (n=20 per layer),
      (b) partial Spearman controlling for normalized depth — THE single most
      important analysis, (c) subspace angle quantitative analysis, (d) CKA
      cliff threshold identification。验证 pilot finding 的 Simpson's Paradox
      在 full-scale 上双架构复现。
    expected_results:
      # Raw pooled correlation (CKA vs transfer AUROC, all layers×langs)
      qwen3_raw_rho: -0.36
      qwen3_raw_p: 0.0001
      llama4_raw_rho: -0.41
      llama4_raw_p: 0.0001
      # Partial correlation controlling for normalized depth
      qwen3_partial_rho: 0.48
      qwen3_partial_p: 0.002
      qwen3_partial_bootstrap_ci_95: [0.31, 0.62]
      llama4_partial_rho: 0.41
      llama4_partial_p: 0.008
      llama4_partial_bootstrap_ci_95: [0.22, 0.57]
      simpson_paradox_confirmed_both_archs: true
      # Per-layer same-language correlations (n=20 langs per layer)
      qwen3_per_layer_positive_count: 18  # out of 24 layers
      qwen3_per_layer_significant_count: 6  # at p<0.05
      llama4_per_layer_positive_count: 9  # out of 12 layers
      llama4_per_layer_significant_count: 3
      # CKA depth profile (mean across 20 langs)
      qwen3_cka_peak_layer: 16  # ~17% depth
      qwen3_cka_peak_value: 0.82
      qwen3_cka_at_en_optimal_layer: 0.28
      qwen3_cka_cliff_onset_depth_pct: 55
      llama4_cka_peak_layer: 12  # ~25% depth
      llama4_cka_peak_value: 0.84
      llama4_cka_at_en_optimal_layer: 0.35
      llama4_cka_cliff_onset_depth_pct: 50
      # CKA threshold analysis
      transfer_collapse_cka_threshold: 0.35
      below_threshold_mean_zs_auroc: 0.58
      above_threshold_mean_zs_auroc: 0.72
      # Subspace angle analysis
      correctness_subspace_angle_within_layer_mean_deg: 12.4
      correctness_subspace_angle_across_layer_mean_deg: 38.7
      correctness_direction_persists_despite_global_cka_decline: true
    result_rationale: >
      Simpson's Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper →
      representations diverge → CKA drops）和 transfer AUROC（deeper → EN probe
      stronger → higher absolute AUROC up to a point），创造了一个 confound。
      Raw pooled correlation 为负是因为 shallow layers 有 high CKA 但 low AUROC
      （probe 本身弱），deep layers 有 low CKA 但 higher AUROC（probe 强虽然
      transfer degrades）。控制 depth 后，within 每个 layer，higher CKA 的
      语言确实有 better transfer，partial rho 为正。

      MVP pilot（Llama, 5 langs × 9 layers）已展现 rho=+0.41, p=0.006。
      Full-scale（20 langs × 12-24 layers）增强统计 power：per-layer test 从
      n=5 增至 n=20，partial correlation 的 bootstrap CI 不含零。

      Qwen3 partial rho (0.48) 高于 Llama4 (0.41)，与 Qwen 的 steeper CKA
      cliff 一致：Qwen 的 CKA 变异范围更大（peak 0.82 → floor 0.28 vs
      Llama 0.84 → 0.35），为 partial correlation 提供更多 signal。

      MVP Qwen pilot 仅 rho=+0.18 (p=0.274)，full-scale上升至 0.48 是因为：
      (1) n 从 5 增至 20 语言，power 大幅提升；(2) 20 语言覆盖更宽的
      CKA 范围（增加了 yo/ig/te 等极低 CKA 语言和 nl/pt 等高 CKA 语言），
      扩大了 within-layer variance。

      CKA cliff threshold ~0.35 标记了 "transfer collapse zone"：当 CKA
      低于此阈值时，correctness direction 的 cross-lingual overlap 不足以
      支撑 zero-shot transfer。Subspace angle analysis 揭示 correctness
      direction 在同一 layer 内跨语言仅旋转 ~12°（highly aligned），但跨
      layer 旋转 ~39°（significant drift），解释了为何 within-layer CKA
      预测 transfer 但 raw pooled 不预测。
    tables:
      - name: "Table 6: Simpson's Paradox — Raw vs Partial Correlation"
        columns: [model, analysis, spearman_rho, p_value, bootstrap_95CI, interpretation]
        rows:
          - [Qwen3-235B, "raw pooled (CKA vs ZS AUROC)",
             -0.36, "<0.001", "[-0.44, -0.27]", "negative — depth confound"]
          - [Qwen3-235B, "partial (controlling depth)",
             +0.48, 0.002, "[+0.31, +0.62]", "positive — genuine geometric signal"]
          - [Llama4 Scout, "raw pooled (CKA vs ZS AUROC)",
             -0.41, "<0.001", "[-0.50, -0.31]", "negative — depth confound"]
          - [Llama4 Scout, "partial (controlling depth)",
             +0.41, 0.008, "[+0.22, +0.57]", "positive — genuine geometric signal"]
      - name: "Table 7: Per-Layer CKA-Transfer Correlation (Qwen3, selected layers)"
        columns: [layer_idx, depth_pct, mean_CKA_20lang, spearman_rho_n20, p_value]
        rows:
          - [12, 13, 0.78, +0.52, 0.019]
          - [20, 21, 0.81, +0.48, 0.032]
          - [28, 30, 0.76, +0.55, 0.012]
          - [36, 38, 0.68, +0.51, 0.022]
          - [44, 47, 0.56, +0.46, 0.041]
          - [52, 55, 0.45, +0.43, 0.058]
          - [60, 64, 0.38, +0.38, 0.098]
          - [68, 72, 0.30, +0.33, 0.155]
          - [72, 77, 0.28, +0.28, 0.231]
          - [80, 85, 0.22, +0.21, 0.372]
      - name: "Table 8: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)"
        columns: [depth_pct, HIGH_CKA, MID_CKA, LOW_CKA, overall_CKA]
        rows:
          - [13, 0.86, 0.79, 0.62, 0.78]
          - [30, 0.84, 0.77, 0.58, 0.76]
          - [47, 0.68, 0.56, 0.35, 0.56]
          - [64, 0.48, 0.37, 0.22, 0.38]
          - [77, 0.38, 0.27, 0.14, 0.28]
          - [94, 0.25, 0.18, 0.09, 0.19]
      - name: "Table 9: Subspace Angle Analysis (correctness direction)"
        columns: [comparison_type, mean_angle_deg, std_deg, interpretation]
        rows:
          - ["within-layer cross-language (same layer, different langs)",
             12.4, 5.8, "highly aligned — correctness direction is near-universal"]
          - ["cross-layer same-language (same lang, different layers)",
             38.7, 11.2, "significant drift — direction rotates with depth"]
          - ["random baseline (shuffled)",
             87.3, 2.1, "near-orthogonal — signal is non-trivial"]
    figures_description:
      - >
        Figure 4a: Simpson's Paradox visualization — left panel: raw scatter
        (CKA vs ZS AUROC) showing negative trend with depth-colored points;
        right panel: partial residual plot after controlling for depth showing
        positive trend. Two panels side by side dramatically illustrate the
        sign reversal.
      - >
        Figure 4b: CKA × layer × language heatmap for Qwen3 (main) and Llama4
        (inset). Color intensity = CKA value. Clear gradient from warm
        (shallow, high CKA) to cool (deep, low CKA), with low-resource
        languages cooling faster.
      - >
        Figure 4c: CKA threshold scatter — transfer AUROC (y) vs CKA (x),
        vertical dashed line at CKA=0.35 showing transfer collapse zone.
    analysis: >
      Simpson's Paradox 在双架构上显著复现（partial rho Qwen=+0.48 p=0.002,
      Llama=+0.41 p=0.008），是本文的核心几何洞见。这不是 trivially expected
      from measurement overlap（CKA 和 transfer AUROC 都衡量 EN-target 相似性）
      ——sign reversal 从负到正是 non-trivial 的。

      Subspace angle analysis 提供 mechanistic grounding：correctness direction
      在同一 layer 内跨语言仅 ~12° 偏差（near-universal），但跨 layer 偏差
      ~39°（significant rotation）。这解释了为何 CKA（衡量全局 representation
      similarity）与 transfer（衡量 correctness direction alignment）的关系
      需要控制 depth 后才能显现：全局 CKA 下降反映的是 non-correctness
      dimensions 的 divergence，correctness subspace 本身作为 low-dimensional
      feature 持续存在。

      CKA cliff threshold ~0.35 直接解释了 Qwen3 vs Llama4 tradeoff 差异：
      Qwen3 的 CKA cliff 更陡（L52→L60 从 0.45 降至 0.38），导致更多语言
      在 deep layers 穿越 threshold → strong tradeoff；Llama4 的 cliff 更缓
      （L28→L36 从 0.55 降至 0.45），且 ar/hi/ko 因高 baseline CKA 从不穿越
      threshold → weak/mixed tradeoff。

      这一分析将 Claim 1 的 Pareto observation 与 CKA geometry 连接，构成
      完整的 geometric explanation：architecture-dependent CKA cliff steepness
      → architecture-dependent Pareto frontier strength。

  ###################################################################
  # plan_003: CaCLR Implementation & Evaluation
  ###################################################################
  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: plan_003
    description: >
      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits).
      English labels + parallel activations from GlobalMMLU test-split 70/30
      partition. Compare vs zero-shot/mean-shift/linear-proj/few-shot across
      full Pareto frontier, both models × 20 languages. α sweep [0.01–10],
      β sweep [0.001–1.0] across 3 OOM.
    expected_results:
      best_alpha: 0.1
      best_beta: 0.05
      # Combined metrics (mean of both models)
      caclr_mean_delta_auroc_vs_zs: 0.035
      caclr_mean_delta_auroc_vs_linproj: 0.015
      caclr_improvement_at_deep_layers_pp: 4.8
      caclr_improvement_at_shallow_layers_pp: 1.2
      caclr_improvement_pass_rate: 0.88
      # Per-model
      qwen3_caclr_mean_auroc_20lang: 0.757
      qwen3_caclr_delta_vs_zs_pp: 3.7
      qwen3_caclr_ece_mean: 0.078
      llama4_caclr_mean_auroc_20lang: 0.733
      llama4_caclr_delta_vs_zs_pp: 3.3
      llama4_caclr_ece_mean: 0.085
      # β sweep results
      beta_0001_delta_pp: 0.5
      beta_001_delta_pp: 1.8
      beta_005_delta_pp: 3.5
      beta_01_delta_pp: 3.2
      beta_10_delta_pp: 0.8
      # α sweep results
      alpha_001_ece_improvement_pp: 1.5
      alpha_01_ece_improvement_pp: 3.2
      alpha_10_ece_improvement_pp: 2.8
      alpha_100_ece_improvement_pp: -0.5
      # Component ablation
      bce_only_auroc: 0.710
      bce_sbece_auroc: 0.722
      bce_consistency_auroc: 0.738
      bce_sbece_consistency_auroc: 0.745
      # Implementation spec
      mmd_kernel: "Gaussian RBF, bandwidth=median heuristic"
      optimizer: "Adam, lr=1e-3, linear warmup 10%"
      epochs: 50
      early_stopping: "patience=10, monitor=val_auroc"
      initialization: "from standard LR solution"
      batch_size: 256
      mmd_items: "same items as BCE (overlapping)"
      parallel_set_size_range: [1800, 4200]
    result_rationale: >
      CaCLR 的 consistency loss (β·MMD on 1-D logits) 强制 probe 学习
      language-invariant features：EN 和 target-language 的 probe 输出分布
      应相似。在 1-D logit space 中，MMD 有效地匹配了两种语言的 logit mean
      和 variance，等价于让 probe direction 靠近 CKA analysis 中揭示的
      "universal correctness subspace"。

      +3.5pp mean delta（[2, 5] range 内）反映了 1-D MMD 的能力边界：它能
      捕获 first-order distributional alignment（mean/variance matching），
      但无法完成 full rotational alignment（需要 d-dimensional 操作）。Linear
      projection（+2pp）通过 Procrustes 做了 rotational alignment 但不优化
      probe 本身；CaCLR 的优势在于 end-to-end 优化但受 1-D 约束。两者差距
      仅 1.5pp，说明 correctness transfer 的瓶颈主要是 rotational（线性
      投影解决的）而非 distributional（MMD 解决的）。

      β sweep across 3 OOM 清晰展现 "sweet spot"：β=0.001 太弱（gradient
      noise > signal），β=1.0 太强（MMD 主导 BCE，probe accuracy 下降 2pp）。
      Optimal β=0.05 平衡了 accuracy 和 consistency。

      Deep-layer improvement (+4.8pp) 远大于 shallow-layer (+1.2pp)，因为
      deep layers 有更大的 capability-specific component（Claim 2 decomposition
      所揭示），CaCLR 的 consistency loss 正好 target 这个 component。这与
      difficulty-capability decomposition 形成因果闭环。

      88% improvement pass rate（35/40 model-lang pairs）：5 个 non-improving
      pairs 是 HIGH-resource languages（如 Qwen3-zh, Qwen3-nl）on shallow
      layers where ZS transfer 已经接近 ceiling。
    tables:
      - name: "Table 10: β Sweep — Consistency Loss Effect"
        columns: [beta, mean_delta_auroc_vs_zs_pp, mean_delta_ece_pp, note]
        rows:
          - [0.000, 0.0,  0.0,  "baseline (BCE only)"]
          - [0.001, 0.5,  -0.3, "marginal improvement"]
          - [0.01,  1.8,  -1.1, "clear positive signal"]
          - [0.05,  3.5,  -2.4, "optimal — best tradeoff"]
          - [0.10,  3.2,  -2.0, "slight over-regularization"]
          - [1.00,  0.8,  -0.5, "MMD dominates, probe accuracy degrades"]
      - name: "Table 11: CaCLR vs All Methods (at best-transfer layer, both models averaged)"
        columns: [method, auroc_mean_20, ece_mean_20, requires_labels, key_resource]
        rows:
          - [zero-shot,      0.710, 0.118, "none",       "—"]
          - [mean-shift,     0.710, 0.118, "none",       "—"]
          - [linear_proj_50, 0.725, 0.098, "50 parallel pairs", "Procrustes"]
          - [linear_proj_200,0.729, 0.095, "200 parallel pairs", "Procrustes"]
          - [few-shot-25,    0.700, 0.102, "25 labeled",  "target labels"]
          - [few-shot-100,   0.727, 0.088, "100 labeled", "target labels"]
          - [CaCLR,          0.745, 0.082, "none",        "parallel activations"]
      - name: "Table 12: CaCLR Depth Profile (Qwen3, ZS AUROC vs CaCLR AUROC)"
        columns: [depth_pct, zs_auroc, caclr_auroc, delta_pp]
        rows:
          - [30, 0.733, 0.745, 1.2]
          - [43, 0.748, 0.766, 1.8]
          - [55, 0.720, 0.752, 3.2]
          - [64, 0.690, 0.738, 4.8]
          - [77, 0.638, 0.688, 5.0]
          - [85, 0.601, 0.641, 4.0]
    figures_description:
      - >
        Figure 5: β sweep curve — delta AUROC (y) vs log10(β) (x),
        inverted-U shape peaking at β=0.05. Inset shows
        corresponding ECE improvement.
      - >
        Figure 6: CaCLR depth profile — ZS (blue) vs CaCLR (red) AUROC
        across normalized depth. Gap widens at deep layers,
        demonstrating CaCLR specifically addresses deep-layer
        transfer degradation.
    analysis: >
      CaCLR 作为正面方法贡献：β>0 在 deep layers 上提供 ≥2pp AUROC
      improvement（实际 deep-layer mean = +4.8pp），且 β sweep across 3 OOM
      清晰展现最优区间。Component ablation 证实 L_consistency 是主要
      contributor（+2.8pp），L_SB-ECE 提供 complementary calibration
      improvement（+0.7pp ECE, +0.7pp AUROC synergy）。

      CaCLR 超越 linear projection 1.5pp 是因为 end-to-end 优化可以利用
      training dynamics（gradient 信号引导 probe 朝 language-invariant direction
      收敛），而 Procrustes 只做 post-hoc geometric correction。但差距不大
      是因为 1-D MMD 的 expressiveness 有限——它只能匹配 scalar logit
      distributions，不能做 full subspace alignment。

      Deep-layer improvement 模式与 Claim 2 的 decomposition 一致：deep layers
      的 capability-specific component 更大，CaCLR 的 consistency loss 正好
      在这些 layers 有更多 signal 来 exploit。这构成
      Pareto→Decomposition→CaCLR→CKA 因果链的第三环。

  ###################################################################
  # plan_004: Difficulty-Controlled Ablation
  ###################################################################
  - name: "Difficulty-Controlled Ablation (Decomposition)"
    plan_id: plan_004
    description: >
      IRT difficulty probes (Ridge regression), project out difficulty direction,
      retrain correctness probes on residuals, evaluate transfer。10 languages
      (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) × 8 layers (20-90%
      depth) per model。包含 random-direction control。
    expected_results:
      difficulty_probe_r2_mean: 0.68
      difficulty_probe_r2_range: [0.55, 0.78]
      difficulty_var_explained_pct: 65
      capability_var_explained_pct: 35
      difficulty_transfer_degradation_share_pct: 12
      capability_transfer_degradation_share_pct: 88
      decomp_capability_delta_auroc: 0.03
      residual_en_auroc_drop_pp: 4.5
      residual_zs_transfer_drop_pp: 0.8
      random_direction_control_delta_pp: -1.2
      prescriptive_accuracy: 0.78
      capability_transfer_drop_by_depth:
        "20pct": 0.6
        "50pct": 2.8
        "80pct": 8.5
    result_rationale: >
      IRT difficulty 是 language-agnostic property：hard questions are hard
      everywhere。Ridge regression captures this linearly (R²=0.68, 与
      Civelli et al. 的 shared difficulty finding 一致)。Difficulty 占
      correctness variance 的 65% 但仅贡献 12% 的 transfer degradation，
      因为 difficulty signal 本质上是 universal 的。Capability-specific
      residual 仅占 35% variance 但驱动 88% 的 transfer degradation，且
      degradation 随 depth 指数增长（20% depth: 0.6pp → 80% depth: 8.5pp）。

      这一 decomposition 解释了 Pareto frontier 的 mechanistic origin：
      deep layers 的 EN probe improvement 主要来自 capability-specific
      component（language-dependent competence），而这个 component 恰好是
      最难 transfer 的。CaCLR 的 consistency loss works precisely because
      it targets this component。

      Random-direction control（-1.2pp, 随机方向 projection 反而损害）确认
      difficulty direction 不是 arbitrary dimensionality reduction 的 artifact，
      而是 genuine signal。

      Prescriptive accuracy 78%：给定语言-layer 的 difficulty/capability
      ratio，预测应使用 zero-shot（difficulty-dominant）还是 CaCLR
      （capability-dominant）策略，在 78% 的 cases 中正确。
    tables:
      - name: "Table 13: Decomposition Results"
        columns: [component, var_pct, transfer_auroc_mean, transfer_drop_pp, degradation_share_pct]
        rows:
          - [full_correctness,   100, 0.710, 9.0,  100]
          - [difficulty_shared,   65, 0.698, 1.1,   12]
          - [capability_specific, 35, 0.615, 12.8,  88]
      - name: "Table 14: Capability Transfer Drop by Depth"
        columns: [depth_band, difficulty_drop_pp, capability_drop_pp, ratio]
        rows:
          - ["20-30%", 0.2, 0.6,  "3×"]
          - ["40-50%", 0.6, 2.8,  "4.7×"]
          - ["60-70%", 1.0, 5.6,  "5.6×"]
          - ["75-90%", 1.5, 8.5,  "5.7×"]
    figures_description:
      - >
        Figure 7: Stacked area — difficulty (blue, flat) vs capability
        (red, exponentially increasing) transfer degradation across depth.
    analysis: >
      Decomposition 清晰分离 transferable vs non-transferable components。
      Difficulty 占大部分 variance 但 near-perfectly transfers（仅 12%
      degradation share），capability 占少数但驱动几乎所有 degradation。
      这解释了为何 zero-shot transfer 在 mid-depth 工作（difficulty
      dominates there）但在 deep layers 失败（capability grows）。
      Prescriptive accuracy 78% 证实 decomposition 不仅是描述性的，
      而是可以指导 alignment strategy selection。

  ###################################################################
  # plan_012: Linear Projection Sensitivity
  ###################################################################
  - name: "Linear Projection Sensitivity Analysis"
    plan_id: plan_012
    description: >
      Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。
      Both models × 5 representative layers × 20 languages。确定最小数据需求
      和 resource-tier 分层饱和。
    expected_results:
      pairs_to_95pct_overall: 42
      pairs_to_95pct_HIGH: 22
      pairs_to_95pct_MID: 38
      pairs_to_95pct_LOW: 48
      pairs_10_pct_of_200: 0.72
      pairs_20_pct_of_200: 0.86
      pairs_30_pct_of_200: 0.92
      pairs_50_pct_of_200: 0.97
      pairs_100_pct_of_200: 0.99
      pairs_200_baseline_auroc_mean: 0.729
      procrustes_reversal_threshold: 0.52
      procrustes_helps_below_threshold_delta_pp: 3.8
      procrustes_hurts_above_threshold_delta_pp: -1.2
    result_rationale: >
      Linear projection (Procrustes) 学习 EN→target 的 rotation matrix。
      20 pairs 即可估计 dominant rotational components（correctness subspace
      是 low-dimensional 的，前几个 principal angles 解释 90%+ 的 alignment
      structure）。42 pairs 达到 95% 因为边际的 minor components 需要更多
      data 来稳定估计。

      Resource-tier stratification 清晰：HIGH languages（zh/es/de 等）的
      activation distributions 与 EN 更相似，rotation matrix 的 effective
      rank 更低（fewer parameters to estimate），22 pairs 即可。LOW languages
      需要估计更 complex rotation（effective rank 更高），48 pairs。

      Procrustes effect reversal（threshold ~0.52）：当 ZS AUROC < 0.52 时，
      correctness direction 严重 misaligned，Procrustes 纠正旋转带来 +3.8pp。
      当 ZS AUROC > 0.60 时，directions 已经 well-aligned，Procrustes
      引入 estimation noise 反而 hurt -1.2pp。Threshold 0.52 对应 CKA ~0.35
      （与 plan_011 的 cliff threshold 一致）。

      这一 finding 直接 actionable：practitioners 应先测 ZS transfer，
      only apply Procrustes when baseline < 0.52。
    tables:
      - name: "Table 15: Projection Sample Efficiency"
        columns: [n_pairs, pct_of_200pair_performance, mean_auroc, note]
        rows:
          - [10,  72, 0.724, "unstable, high variance across runs"]
          - [20,  86, 0.728, "captures dominant rotation"]
          - [30,  92, 0.731, "near plateau for HIGH langs"]
          - [50,  97, 0.734, "near plateau for all tiers"]
          - [100, 99, 0.737, "marginal returns"]
          - [200, 100, 0.729, "baseline (reference)"]
      - name: "Table 16: Saturation by Resource Tier"
        columns: [tier, pairs_to_90pct, pairs_to_95pct, interpretation]
        rows:
          - [HIGH, 15, 22, "rotation is simple, low effective rank"]
          - [MID,  25, 38, "moderate rotation complexity"]
          - [LOW,  35, 48, "complex rotation, more data needed"]
      - name: "Table 17: Procrustes Effect Reversal"
        columns: [zs_auroc_range, n_lang_layer_pairs, mean_delta_pp, direction]
        rows:
          - ["<0.45",     42, +5.2, "strong positive"]
          - ["0.45-0.52", 68, +2.4, "moderate positive"]
          - ["0.52-0.60", 95, +0.3, "near-zero (transition zone)"]
          - ["0.60-0.70", 88, -1.2, "negative — hurts"]
          - [">0.70",     47, -0.8, "slight negative"]
    figures_description:
      - >
        Figure 8a: Sample efficiency curves — AUROC (y) vs n_pairs (x),
        three curves for HIGH/MID/LOW tiers, showing staggered saturation.
      - >
        Figure 8b: Procrustes effect reversal — delta AUROC (y) vs
        ZS baseline AUROC (x), showing sign change at ~0.52. Dot size
        proportional to sample count.
    analysis: >
      ~42 pairs to 95% performance 是 directly actionable 的 practical
      finding：对于大多数语言，仅需 <50 parallel sentences 即可达到接近
      supervised-level alignment。Resource-tier stratification（HIGH 22
      vs LOW 48 pairs）提供了 per-language guidance。

      Procrustes reversal at 0.52 与 CKA threshold 0.35 形成对应：
      CKA < 0.35 的 language-layer combinations 对应 ZS < 0.52（
      因为 poor alignment → poor transfer），正好是 Procrustes 帮助最大的
      区域。这构成了 geometric explanation 的 practical corollary。

  ###################################################################
  # plan_013: Probing Control Tasks (full-scale)
  ###################################################################
  - name: "Probing Control Tasks — Full-Scale Hewitt & Liang (2019)"
    plan_id: plan_013
    description: >
      Extend MVP English-only control task analysis to 20 languages × 2
      architectures。Train probes on randomly permuted labels, compute
      selectivity = real_AUROC - control_AUROC。Identify capacity artifacts
      by language, layer, and model。
    expected_results:
      # English results (consistent with DONE mvp data)
      en_selectivity_range: [0.02, 0.26]
      en_selectivity_meaningful_layers: [16, 20, 24, 27]
      # Full-scale cross-lingual
      control_artifact_rate_lowres: 0.27
      control_artifact_rate_midres: 0.05
      control_artifact_rate_highres: 0.03
      low_res_langs_most_affected: [yo, ig, te, sw]
      artifact_concentration_depth: "60-100% depth"
      cross_lingual_selectivity_mean:
        HIGH: 0.22
        MID: 0.18
        LOW: 0.09
      languages_with_any_meaningful_selectivity: 17
      control_auroc_mean_all: 0.495
      control_auroc_std: 0.008
    result_rationale: >
      MVP English data（selectivity L27=0.262）确立了 baseline。Cross-lingual
      extension 揭示了 resource-tier dependent artifact pattern：

      LOW-resource languages 的 27% artifact rate 源于两个因素：(1) these
      languages 在 model pretraining 中占比极低，activation distributions
      相对 high-resource 更 "shallow" (less structured)，linear probes 更容易
      通过 capacity 而非 genuine signal 拟合少量 patterns；(2) GlobalMMLU
      的 low-resource translations 质量较低，引入 noise 使 correctness
      signal 更弱，selectivity 更接近 chance。

      Mid/high-resource 的 artifact rate 极低（3-5%）因为 representation
      quality 高，probe 有 genuine signal 可以 leverage。

      Artifacts 集中在 60-100% depth，与 CKA cliff 一致：deep layers 的
      low-resource CKA 已经很低（<0.2），cross-lingual activation structure
      不足以支撑 genuine correctness probing，probe 退化为 memorizing
      dataset-specific patterns。

      这一 finding 是 field-level contribution：此前没有人在 cross-lingual
      probing 中检查 selectivity controls。28% 的 low-resource artifact
      rate 意味着没有 control tasks 的 cross-lingual probing 结果
      （包括 Xiao et al.）需要谨慎解读。
    tables:
      - name: "Table 18: Selectivity by Resource Tier and Depth"
        columns: [depth_band, HIGH_selectivity, MID_selectivity, LOW_selectivity]
        rows:
          - ["0-30%",  0.04, 0.03, 0.01]
          - ["30-60%", 0.18, 0.14, 0.06]
          - ["60-80%", 0.28, 0.22, 0.10]
          - ["80-100%", 0.25, 0.20, 0.08]
      - name: "Table 19: Artifact Rates by Tier"
        columns: [tier, n_lang_layer_combinations, artifact_count, artifact_rate]
        rows:
          - [HIGH, 384, 12, "3%"]
          - [MID,  336, 17, "5%"]
          - [LOW,  240, 65, "27%"]
          - [total, 960, 94, "10%"]
    figures_description:
      - >
        Figure S1: Selectivity heatmap — language (y, ordered by tier) ×
        depth (x). LOW-resource rows show gray (low selectivity) at deep layers.
    analysis: >
      27% low-resource artifact rate 是 methodological warning for the field：
      cross-lingual probing studies 如果不做 selectivity checks 会高估
      low-resource transfer quality。重要的是 artifacts 集中在 low-resource +
      deep layers，不波及 mid/high-resource 或 shallow layers，因此本文的
      核心 Pareto/CKA 分析（主要基于 mid/high-resource patterns）不受影响。

  ###################################################################
  # plan_005: Cross-Lingual Orthogonality
  ###################################################################
  - name: "Cross-Lingual Correctness-Confidence Orthogonality"
    plan_id: plan_005
    description: >
      Extract verbalized confidence direction, compute cosine similarity
      with correctness direction, 20 languages × 2 architectures。
      Supporting evidence for Claim 4 (subsection)。
    expected_results:
      cosine_mean_overall: 0.05
      cosine_range: [0.02, 0.09]
      cosine_en: 0.03
      all_below_0p10: true
      qwen3_cosine_mean: 0.046
      llama4_cosine_mean: 0.054
      HIGH_cosine_mean: 0.038
      MID_cosine_mean: 0.052
      LOW_cosine_mean: 0.072
      resource_tier_correlation: -0.66
    result_rationale: >
      Miao & Ungar (2026) 在 English 7-8B 上测得 cosine < 0.04。Extension to
      20 languages × 大模型应保持 near-orthogonality（< 0.10），因为这反映
      transformer 的 structural property：verbalized confidence 由 language
      modeling head 从 surface-level token probabilities 生成，correctness
      由 intermediate representations geometry 编码，两者 architecturally
      decoupled。Low-resource 略高（0.072 mean）因为 confidence elicitation
      in low-resource languages 更 noisy，不完全 decoupled。Resource-tier
      gradient（r=-0.66）说明更好的 multilingual training → 更清晰的
      correctness/confidence separation。
    tables:
      - name: "Table 20: Orthogonality by Tier (cosine similarity)"
        columns: [tier, n_langs, qwen3_mean, llama4_mean, combined_mean]
        rows:
          - [HIGH, 8, 0.035, 0.041, 0.038]
          - [MID,  7, 0.048, 0.056, 0.052]
          - [LOW,  5, 0.066, 0.078, 0.072]
    figures_description:
      - >
        Figure S2: Cosine similarity violin plots by resource tier, all below
        0.10 threshold line.
    analysis: >
      Orthogonality universally holds (39/40 pairs below 0.10, all 40 below
      0.095)，confirming output-based calibration methods are structurally
      limited across languages。Resource-tier gradient 是新 finding，但
      effect size 小（range only 0.034），作为 subsection 足够。

  ###################################################################
  # plan_006: Probe Complexity Comparison
  ###################################################################
  - name: "Probe Complexity Comparison"
    plan_id: plan_006
    description: >
      Logistic regression vs 2-layer MLP at each probed layer, both models。
      Validates linear probe choice for transfer。
    expected_results:
      logreg_en_auroc_best: 0.81
      mlp_en_auroc_best: 0.83
      mlp_en_gain_pp: 2.0
      logreg_zs_drop_mean_pp: 9.0
      mlp_zs_drop_mean_pp: 14.5
      logreg_transfer_advantage_pp: 5.5
      logreg_advantage_shallow_pp: 2.0
      logreg_advantage_deep_pp: 8.2
    result_rationale: >
      Linear probes learn 一个 hyperplane，跨语言泛化因为 correctness subspace
      是 near-universal linear structure（subspace angle ~12° from plan_011）。
      MLPs fit nonlinear decision boundaries that overfit EN-specific feature
      interactions，gaining +2pp EN AUROC but losing 5.5pp transfer。Gap 在
      deep layers 放大（+8.2pp advantage for logreg at 80% depth）因为 deep
      layers 有更多 language-specific nonlinear structure for MLP to exploit。
      This justifies logreg as primary probe and supports geometric
      interpretation of Pareto frontier。
    tables:
      - name: "Table S2: Probe Complexity (Qwen3, at EN-optimal layer)"
        columns: [probe_type, en_auroc, zs_mean_20, zs_drop_pp]
        rows:
          - [logistic_regression, 0.810, 0.720, 9.0]
          - [mlp_2layer_h128,     0.830, 0.685, 14.5]
    figures_description:
      - >
        Figure S3: Transfer drop (pp) vs depth, logreg (blue) vs MLP (red).
        MLP diverges sharply past 60% depth.
    analysis: >
      Linear probes 为 cross-lingual transfer 的 optimal choice：牺牲 2pp
      EN performance 换取 5.5pp transfer improvement。Depth interaction
      confirms nonlinear language-specific features drive deep-layer
      degradation。

  ###################################################################
  # plan_007: Additional Benchmarks
  ###################################################################
  - name: "Cross-Benchmark Generalization (Belebele + MMLU-ProX)"
    plan_id: plan_007
    description: >
      Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages
      each)。Tests domain generalization。
    expected_results:
      belebele_zs_mean_20: 0.695
      belebele_caclr_mean_20: 0.728
      belebele_caclr_delta_pp: 3.3
      mmlupx_zs_mean_20: 0.680
      mmlupx_caclr_mean_20: 0.715
      mmlupx_caclr_delta_pp: 3.5
      cross_benchmark_caclr_cv: 0.04
    result_rationale: >
      Belebele (reading comprehension) 和 MMLU-ProX (harder factual) 的
      baseline 略低于 GlobalMMLU 因为 domain shift，但 CaCLR 的 improvement
      幅度 consistent（3.3-3.5pp vs GlobalMMLU 的 3.5pp）。Low CV (0.04) 证实
      CaCLR addresses 一个 fundamental representation alignment issue 而非
      overfitting to specific benchmark。
    tables:
      - name: "Table 21: Cross-Benchmark CaCLR Generalization"
        columns: [benchmark, zs_mean_20, caclr_mean_20, delta_pp]
        rows:
          - [GlobalMMLU, 0.710, 0.745, 3.5]
          - [Belebele,   0.695, 0.728, 3.3]
          - [MMLU-ProX,  0.680, 0.715, 3.5]
    figures_description:
      - >
        Figure S4: CaCLR improvement by benchmark × language, showing
        consistent gains.
    analysis: >
      CaCLR generalizes across benchmarks with low variance。Cross-benchmark
      consistency is the strongest defense against overfitting concerns。

  ###################################################################
  # plan_010: Quantization Validation
  ###################################################################
  - name: "Quantization Validation Ablation"
    plan_id: plan_010
    description: >
      (a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset;
      (b) GPTQ-Int4 vs FP16 for Qwen3-235B at 5 layers, 5% subset。
    expected_results:
      llama4_w4a16_fp16_auroc_diff_mean_pp: 0.3
      llama4_w4a16_fp16_auroc_diff_max_pp: 0.8
      llama4_rank_correlation: 0.996
      qwen3_int4_fp16_auroc_diff_mean_pp: 0.5
      qwen3_int4_fp16_auroc_diff_max_pp: 1.1
      qwen3_rank_correlation: 0.994
      conclusion: "quantization introduces negligible distortion for probing"
    result_rationale: >
      W4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation
      geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive
      但 correctness direction 的 angular structure 仍 robust（0.5pp mean diff），
      因为 quantization noise 近似 isotropic，不 preferentially distort
      correctness-relevant directions。Rank correlation > 0.994 确认 Pareto
      frontier ordering 完全保留。Qwen3 的 slightly higher diff (0.5 vs 0.3)
      因为 Int4 比 W4A16 更 lossy。
    tables:
      - name: "Table S3: Quantization Comparison (5 representative layers)"
        columns: [model, layer, fp16_auroc, quant_auroc, diff_pp]
        rows:
          - [Llama4, 8,  0.637, 0.634, 0.3]
          - [Llama4, 16, 0.737, 0.735, 0.2]
          - [Llama4, 28, 0.784, 0.781, 0.3]
          - [Llama4, 36, 0.792, 0.789, 0.3]
          - [Llama4, 44, 0.774, 0.770, 0.4]
          - [Qwen3,  20, 0.712, 0.708, 0.4]
          - [Qwen3,  36, 0.780, 0.775, 0.5]
          - [Qwen3,  52, 0.808, 0.803, 0.5]
          - [Qwen3,  68, 0.812, 0.806, 0.6]
          - [Qwen3,  80, 0.807, 0.800, 0.7]
    figures_description:
      - >
        Figure S5: Quant vs FP16 scatter, y=x diagonal, tight clustering.
    analysis: >
      Quantization safe for both models。Preempts reviewer concern #5。

  ###################################################################
  # plan_008: Gemma 4 31B Dense (Camera-Ready, P2)
  ###################################################################
  - name: "Gemma 4 31B Dense — Third Architecture (Camera-Ready)"
    plan_id: plan_008
    description: >
      Full Pareto frontier on Gemma 4 31B Dense (60 layers, FP16),
      20 languages。Provides dense vs MoE contrast for camera-ready。
    expected_results:
      en_best_auroc: 0.80
      en_best_layer_idx: 45
      zs_mean_20lang: 0.71
      zs_best_transfer_layer_idx: 36
      global_spearman_rho: -0.85
      per_lang_rho_median: -0.58
      caclr_delta_vs_zs_pp: 3.0
      simpson_partial_rho: 0.44
      simpson_partial_p: 0.004
    result_rationale: >
      Gemma 4 31B Dense 是理想的第三 data point：dense architecture（vs two
      MoE models），different pretraining recipe（Google vs Alibaba/Meta），
      60 layers（between Qwen 94 and Llama 48）。EN AUROC 0.80 低于 MoE models
      因为 31B dense < 22B MoE active (MoE routing 提供 effective capacity
      boost)。Pareto strength (ρ=-0.85) 介于 Qwen (-0.91) 和 Llama (-0.78)
      之间。Simpson's partial correlation 仍然显著 (rho=+0.44, p=0.004)，
      确认 geometric insight 是 architecture-universal 而非 MoE-specific。
    tables:
      - name: "Table 22: Three-Architecture Summary"
        columns: [model, type, layers, en_best, zs_mean_20, pareto_rho, simpson_partial_rho, caclr_delta_pp]
        rows:
          - ["Qwen3-235B",    MoE,   94, 0.81, 0.72, -0.91, +0.48, 3.7]
          - ["Llama4 Scout",  MoE,   48, 0.79, 0.70, -0.78, +0.41, 3.3]
          - ["Gemma4 31B",    Dense,  60, 0.80, 0.71, -0.85, +0.44, 3.0]
    figures_description:
      - >
        Figure 9: Three-architecture Pareto frontiers overlaid (normalized
        depth %). Remarkably similar shapes.
    analysis: >
      Three-architecture replication 是 universality claim 最强证据：
      Simpson's Paradox 在 dense 和 MoE 上都成立，Pareto frontier 在
      55-60% depth 处一致出现 knee，CaCLR 提供 3-3.7pp consistent gain。
      Dense vs MoE 的差异 minimal — phenomenon 是 transformer depth 的
      property 而非 routing architecture 的。

  ###################################################################
  # plan_009: Extended Language Coverage (Camera-Ready, P2)
  ###################################################################
  - name: "Extended Language Coverage (Camera-Ready)"
    plan_id: plan_009
    description: >
      Expand from 20 to 50+ languages for camera-ready。
    expected_results:
      total_languages: 50
      zs_pass_rate_50lang: 0.84
      zs_auroc_above_060_count: 42
      caclr_improvement_positive_count: 47
      mean_zs_auroc_50lang: 0.69
      mean_caclr_auroc_50lang: 0.72
      pareto_frontier_holds_all_langs: true
      new_families: [Austronesian, Dravidian, Uralic, Kartvelian, Niger-Congo_B]
    result_rationale: >
      Expansion 主要增加 mid-resource 语言（Indonesian, Finnish, Georgian,
      Tamil, Telugu, etc.），大多 fall in 0.65-0.75 AUROC range。Extremely
      low-resource 语言（Amharic, Khmer, Lao）可能 < 0.55 但代表 edge cases。
      CaCLR 在 94% 的新增语言上 positive 因为 consistency loss mechanism
      是 language-agnostic。Pareto frontier structure 在 50 languages 上
      完全保持。
    tables:
      - name: "Table 23: Extended Coverage by Tier"
        columns: [tier, n_langs, zs_mean, caclr_mean, caclr_gain_pp]
        rows:
          - [HIGH,     10, 0.75, 0.78, 2.8]
          - [MID,      24, 0.71, 0.74, 3.5]
          - [LOW,      12, 0.62, 0.66, 4.2]
          - [VERY_LOW,  4, 0.53, 0.58, 5.0]
    figures_description:
      - >
        Figure 10: World map with per-language CaCLR AUROC, colored by
        performance tier. Broad geographic/typological coverage.
    analysis: >
      50-language extension 确认 all findings at scale。Resource-tier gradient
      smooth, CaCLR benefit inversely correlated with resource level, no
      language family shows anomalous behavior。
```

Key internal consistency checks across all experiments:

| Constraint Metric | Target Range | Achieved | Source |
|---|---|---|---|
| `en_best_auroc` | [0.77, 0.83] | Qwen 0.81, Llama 0.79 | plan_001/002 |
| `zs_pass_rate_20lang` | [0.8, 0.9] | 90%, 85% | plan_001/002 |
| `pareto_spearman_rho_significant_archs` | [2, 2] | 2 (both p<0.005) | plan_001/002 |
| `simpson_partial_rho` | [0.3, 0.55] | +0.48, +0.41 | plan_011 |
| `simpson_p_value_max` | [0.001, 0.01] | max=0.008 | plan_011 |
| `caclr_mean_delta_auroc_vs_zs` | [0.02, 0.05] | 0.035 | plan_003 |
| `linear_proj_pairs_to_95pct` | [30, 50] | 42 | plan_012 |
| `control_artifact_rate_lowres` | [0.2, 0.3] | 0.27 | plan_013 |
| `decomp_capability_delta_auroc` | [0.02, 0.04] | 0.03 | plan_004 |
| `procrustes_reversal_threshold_zs_auroc` | [0.48, 0.55] | 0.52 | plan_012 |

Cross-experiment causal chain coherence:
- CKA cliff at 0.35 (plan_011) → Procrustes reversal at ZS=0.52 (plan_012): CKA<0.35 produces ZS<0.52, exactly where alignment helps
- Capability component drives 88% degradation at deep layers (plan_004) → CaCLR improvement largest at deep layers +4.8pp (plan_003): consistency loss targets capability-specific component
- Control artifact rate 27% low-resource (plan_013) → low-resource fail rate 10-15% on ZS (plan_001/002): artifacts inflate apparent success, real signal is weaker
- Architecture-dependent Pareto (Qwen strong, Llama weak — plan_001/002) → CKA cliff steepness difference (plan_011): Qwen's steeper CKA cliff drives stronger tradeoff

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e6ac0c6-ff6b-419f-ab51-b962a8046e86",
  "isSidechain": false,
  "requestId": "req_011CbF82xmiZknd8Hr1wRkiY",
  "type": "assistant",
  "uuid": "568f53d6-d067-478d-8736-77911732d581",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dpECXeFkfBweXYd6b9omE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 84037,
      "output_tokens": 27213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 27213,
          "cache_read_input_tokens": 84037,
          "cache_creation_input_tokens": 3173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3173
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：核心几何洞见（Simpson's Paradox）在双架构 × 20 语言上显著复现；CaCLR consistency loss 提供可测量迁移增益；所有 claims 完整保留 核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均显著 (p < 0.01…",
  "leafUuid": "568f53d6-d067-478d-8736-77911732d581",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Simpson's Paradox reveals cross-lingual correctness probe transfer",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：核心几何洞见（Simpson's Paradox）在双架构 × 20 语言上显著复现；CaCLR consistency loss 提供可测量迁移增益；所有 claims 完整保留 核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均显著 (p < 0.01…",
  "leafUuid": "568f53d6-d067-478d-8736-77911732d581",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Simpson's Paradox reveals cross-lingual correctness probe transfer",
  "sessionId": "3bed0805-e277-4cba-a173-e5dbb10b2135"
}
```

---
