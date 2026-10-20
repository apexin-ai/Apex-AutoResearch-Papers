# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Simpson's Paradox 在 20 语言上双架构均不显著；CaCLR 失败且几何解释不成立；Pareto frontier 噪声大；高 ar

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55.jsonl`
- **Structured JSON:** [`04b9e2a8da043690883b.json`](../../sessions/04/04b9e2a8da043690883b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T05:21:02.210Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T05:21:02.210Z",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Simpson's Paradox 在 20 语言上双架构均不显著；CaCLR 失败且几何解释不成立；Pareto frontier 噪声大；高 artifact rate 动摇 probe 有效性\n核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均不显著——CKA 在 depth 之外无额外解释力，5 语言 pilot 结果是 small-sample artifact\", 'CaCLR 失败且 CKA subspace 解释也不成立——correctness direction 的跨语言 persistence 弱于预期，非 robust low-dimensional subspace', 'Pareto frontier 噪声大：depth-transfer tradeoff 多数语言无一致显著性，非单调模式普遍', 'Difficulty decomposition 无实质效果——投影去除 difficulty 后 transfer 无变化，两信号纠缠不可分', 'Control task artifacts 波及中资源语言 (>35%)，probe 有效性受到广泛质疑，非仅低资源现象', 'Linear projection 效果不稳定——帮助/损害的阈值无法可靠确定，需要大量 pairs 且语言间方差大']\n关键指标范围：{'en_best_auroc': [0.7, 0.76], 'zs_pass_rate_20lang': [0.5, 0.65], 'pareto_spearman_rho_significant_archs': [0, 1], 'simpson_partial_rho': [0.05, 0.2], 'simpson_p_value_max': [0.1, 0.5], 'caclr_mean_delta_auroc_vs_zs': [-0.02, 0.005], 'linear_proj_pairs_to_95pct': [100, 200], 'control_artifact_rate_lowres': [0.35, 0.5], 'decomp_capability_delta_auroc': [-0.01, 0.005], 'procrustes_reversal_threshold_zs_auroc': 'inconsistent — no clean threshold identifiable'}\n叙事方向：需要大幅 reframe，但仍冲 EACL。原始几何洞见 framing 崩塌。新 angle：'The limits of cross-lingual calibration probe transfer: a large-scale negative result with methodological implications.' 核心贡献重构为三层：(1) 领域级方法论警示——control task 分析揭示 >35% 跨语言 probing 结果是 capacity artifacts，这是该发现的最强版本，首次在 cross-lingual transfer 场景应用 selectivity 检验，对所有跨语言 probing 研究有 field-level implication；(2) 综合 negative result 同时关闭 distributional matching (CaCLR) 和 geometric alignment 两条路径，附带 component ablation 和 β sweep 数据，reproducibility bar 高于正面结果；(3) 条件性实用指导——按 resource-tier 和 baseline ZS quality 分层给出推荐，linear projection 作为唯一可行但需 100+ pairs 的暴力方案。'Correctness direction 跨语言 language-agnostic' 这一前提假设在一般情况下被经验性证伪——这本身是对 Miao & Ungar (2026) 和 CORAL 研究线的重要回应。作为 rigorous negative results + methodology paper 仍可发 EACL。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: xling_calib_direction\nfocus: Key improvements since last dream: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative but partial correlation controlling for depth is positive (Llama rho=+0.41, p=0.006), genuine geometric insight; (2) Claim 4 downgraded to subsection, space freed for control task finding and projection efficiency; (3) Control task methodological warning elevated to main body (28% low-resource artifacts); (4) Linear projection sample efficiency (~50 pairs, tier-stratified); (5) Procrustes effect reversal (helps ZS<0.50, hurts ZS>0.60); (6) Complete CaCLR implementation spec for reproducibility; (7) 30+ references planned; (8) Statistical framework: bootstrap CI + permutation tests + Cohen's d; (9) Figure plan: Pareto scatter plot, layer-wise AUROC, decomposition visualization. Focus review on whether novelty improvements are sufficient for main conference acceptance.\n\n## paper_framing.md\n\n# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4): extract\n    activations at every 4th layer (24 probed layers), 20 typologically diverse languages,\n    train English correctness probes (logistic regression + 2-layer MLP), evaluate\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR). Report per-language Spearman rho (depth vs transfer AUROC) alongside global\n    rho. Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps: []\n  notes: '4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM). INT4 (not INT8) required\n    to fit 235B model. Need INT4 validation ablation (compare INT4 vs INT8 at representative\n    layers on subset — extend plan_010).\n\n    '\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Full Pareto frontier on Llama 4 Scout (48 layers, MoE, W4A16): extract\n    activations at every 4th layer (12 probed layers), 20 languages, 5 transfer conditions.\n    W4A16 weight quantization (RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16).\n    Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.\n\n    '\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  notes: 'W4A16 (4-bit weight, 16-bit activation) via RedHatAI quantized version (~50GB).\n    Changed from INT8 to W4A16 due to disk constraints (both models must coexist).\n    plan_010 quantization validation must compare W4A16 vs FP16 (not INT8 vs FP16).\n\n    '\n  status: planned\n- id: plan_003\n  claim: 3\n  description: 'CaCLR implementation and comparative evaluation: L_CaCLR = L_BCE +\n    α·L_SB-ECE + β·L_consistency (MMD distance). Train CaCLR probes using English\n    labels + unlabeled parallel activations. DATA: GlobalMMLU test split partitioned\n    70/30 (probe_train/eval, stratified). English BCE labels + parallel MMD activations\n    from probe_train only; evaluate exclusively on eval portion. No train split exists\n    in GlobalMMLU. MMD operates on probe logits (not raw activations — M007 gradient\n    fix). Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100) across\n    full Pareto frontier for both models × 20 languages. Hyperparameter tuning: α\n    sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0). Report fixed-layer results\n    (50% depth + EN-optimal) alongside per-language oracle.\n\n    '\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS\n    2021. L_consistency uses Maximum Mean Discrepancy (MMD). If β sweep shows inert\n    consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional\n    narrative). IMPLEMENTATION SPEC (must report for reproducibility — Dream RD1,\n    3-tier consensus): (a) MMD kernel: Gaussian RBF, bandwidth via median heuristic\n    (b) Optimizer: Adam, report LR + schedule (c) Epochs + early stopping criterion\n    (d) Initialization: from standard LR solution or from scratch (e) Batch size for\n    MMD computation (f) Whether MMD items overlap with BCE training items or held-out\n    (g) Parallel set size per language + translation quality note for low-resource\n    Negative result demands higher reproducibility bar than positive.\n\n    '\n  status: planned\n- id: plan_004\n  claim: 2\n  description: 'Difficulty-controlled ablation: train IRT difficulty probes (Ridge\n    regression on human difficulty scores per Civelli et al.), project out difficulty\n    direction from activations, retrain correctness probes on residuals, evaluate\n    transfer. 10 representative languages × 8 representative layers per model (20-90%\n    depth).\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Need IRT difficulty scores from GlobalMMLU or external source. Grid justification\n    (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr,\n    LOW: sw/bn) × major language families. 8 layers span 20-90% depth at uniform intervals.\n    Reduced grid is sufficient because decomposition tests a qualitative hypothesis\n    (does projecting out difficulty help or hurt?), not a per-language quantitative\n    claim. Include random-direction control to rule out dimensionality-reduction artifacts.\n\n    '\n  status: planned\n- id: plan_005\n  claim: 4\n  description: 'Cross-lingual orthogonality analysis: extract verbalized confidence\n    direction (prompt model for confidence score, fit probe), compute cosine similarity\n    with correctness direction across 20 languages × 2 architectures. Analyze by resource\n    tier (high/mid/low) and language family.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 1\n  description: 'Probe complexity comparison: logistic regression vs 2-layer MLP at\n    each probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better cross-lingually.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations.\n  status: planned\n- id: plan_007\n  claim: 1\n  description: 'Additional benchmark evaluation: evaluate best probes + CaCLR on Belebele\n    (20 languages) and MMLU-ProX (20 languages). Validates generalization beyond MMLU/GlobalMMLU.\n\n    '\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Quantization validation ablation: (a) compare W4A16 vs FP16 at 5 representative\n    layers for Llama 4 Scout on 5% random subset; (b) compare GPTQ-Int4 vs FP16 at\n    5 representative layers for Qwen3-235B on 5% random subset. Validates that quantization\n    doesn''t distort correctness signals. Note: FP16 baseline requires temporary download\n    of FP16 weights for subset only, then delete. May need to do sequentially due\n    to disk constraints.\n\n    '\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: plan_011\n  claim:\n  - 1\n  - 4\n  description: 'CKA cross-lingual representation similarity analysis: compute CKA\n    (linear kernel) between English and each target language at every probed layer\n    for both models. Full-scale validation of pilot finding: correctness direction\n    is a robust low-dimensional subspace feature that persists despite global CKA\n    decline. Transfer collapses only at critical CKA threshold (~0.35). Report CKA\n    × layer × language heatmaps, CKA vs transfer degradation ((EN_AUROC - target_AUROC)\n    / EN_AUROC) correlation per language to isolate alignment effect from probe quality,\n    and critical threshold analysis.\n\n    '\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).\n    Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001, Qwen\n    rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig. CAUTION (Reviewer):\n    pooled correlation has depth confound. Pilot per-language Spearman almost all\n    n.s. (n=9 too small), ko direction reversed. Overall p=0.007 driven by BETWEEN-language\n    differences (zh/ar high CKA + low degradation vs hi/sw low CKA + high degradation),\n    not within-language depth effects. Supportable claim: \"languages with higher CKA\n    exhibit less transfer degradation\" (between-language, qualitative at n=5). NOT\n    supportable: \"CKA predicts within- language degradation across depth.\" Full-scale\n    analysis (20 langs) MUST include: (a) same-layer cross-language correlation (strongest\n    test, n=20 per layer), (b) partial correlation controlling for normalized depth\n    — THIS IS THE SINGLE MOST IMPORTANT ANALYSIS (Dream RD2, 3-tier consensus); if\n    CKA adds no explanatory power beyond depth, downgrade framing from \"geometric\n    analysis\" to \"suggestive correlation\", (c) per-language Spearman with denser layer\n    sampling, (d) subspace angle analysis with QUANTITATIVE tables (not just prose\n    — Dream best-tier W1). CKA cliff steepness explains Qwen-Llama tradeoff strength\n    difference (qualitative). Frame as \"geometric/correlational analysis\" NOT \"mechanistic\n    explanation\" (Dream RD6/RD9).\n\n    '\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Linear projection sensitivity analysis: vary number of parallel pairs\n    (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data\n    requirement for this surprisingly strong baseline. Both models × 5 representative\n    layers × 20 languages.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: CPU-bound, uses cached activations. Dream review D11.\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Probing control tasks (Hewitt & Liang 2019): train probes on randomly\n    permuted labels at each layer. Compare selectivity (probe AUROC - control AUROC)\n    across layers and languages. Validates that high AUROC reflects genuine correctness\n    direction, not memorized dataset artifacts or probe capacity.\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'CPU-bound. Dream review D22: probing methodology critique.'\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Gemma 4 31B Dense (60 layers, dense, FP16): third architecture for\n    camera-ready. Full Pareto frontier, 20+ languages. Provides dense vs MoE architectural\n    contrast.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Extended language coverage: expand from 20 to 50+ languages for camera-ready.\n    Leverages GlobalMMLU/Belebele full language sets.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  - plan_002\n  status: planned\n- id: mvp_validation\n  claim: 1\n  description: 'MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift'\n  priority: P0\n  registry_id: mvp_001\n  gpu_budget_hours: 2\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- id: mvp_complementary\n  claim: 1\n  description: 'MVP robustness: complementary layer set (2,6,10,14,18,22,26)'\n  priority: P1\n  registry_id: mvp_002\n  gpu_budget_hours: 2\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- id: mvp_llama_control\n  claim: 1\n  description: 'MVP cross-architecture: Llama-3.1-8B control experiment'\n  priority: P1\n  registry_id: mvp_003\n  gpu_budget_hours: 3\n  deps:\n  - mvp_validation\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7541\n    en_best_layer: 27\n    en_best_ece_raw: 0.1951\n    temp_scaling_fixed:\n      L24:\n        T: 0.67\n        ECE_cal: 0.2205\n      L27:\n        T: 0.62\n        ECE_cal: 0.2216\n      note: 3-way split (60/20/20), T on val, ECE on test. Temp scaling worsens ECE.\n    en_auroc_range:\n    - 0.6113\n    - 0.7541\n    layer_depth_delta: 0.1428\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 27\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    zs_fail_langs:\n    - sw\n    best_zs_auroc:\n      zh: 0.686\n      ar: 0.651\n      hi: 0.652\n      ko: 0.648\n      sw: 0.56\n    mean_shift_delta_ece:\n      zh: -0.36\n      ar: -0.06\n      hi: 2.22\n      sw: 6.44\n      ko: 0.01\n    pass_fail: PARTIAL 2/4 (P2+P3 pass, P1+P4 fail). Research phase continues per\n      D006.\n    p1: FAIL (AUROC=0.7541 ok, ECE=0.1951 raw > 0.15, temp scaling ineffective)\n    p2: PASS (4/5)\n    p3: PASS (14.28pp)\n    p4: FAIL (0/5, mean-shift no improvement)\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7481\n    en_best_layer: 26\n    en_auroc_range:\n    - 0.6229\n    - 0.7481\n    layer_depth_delta: 0.1251\n    best_zs_auroc:\n      zh: 0.6774\n      ar: 0.6302\n      hi: 0.6068\n      sw: 0.5467\n      ko: 0.6678\n    best_zs_layer:\n      zh: 26\n      ar: 26\n      hi: 22\n      sw: 22\n      ko: 26\n    pass_fail:\n      P1_en_auroc_ece: FAIL (ECE=0.2112 > 0.15)\n      P2_zs_auroc: PASS (4/5)\n      P3_layer_delta: PASS (12.51pp)\n      P4_mean_shift: FAIL (0/5, zero delta)\n      overall: PARTIAL\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    en_best_auroc: 0.7284\n    en_best_layer: 31\n    en_best_ece_raw: 0.2052\n    en_auroc_range:\n    - 0.6331\n    - 0.7284\n    layer_depth_delta: 0.0953\n    layers_tested:\n    - 0\n    - 4\n    - 8\n    - 12\n    - 16\n    - 20\n    - 24\n    - 28\n    - 31\n    best_zs_auroc:\n      zh: 0.64\n      ar: 0.6146\n      hi: 0.5935\n      ko: 0.6481\n      sw: 0.5838\n    best_zs_layer:\n      zh: 20\n      ar: 31\n      hi: 31\n      ko: 31\n      sw: 16\n    zs_pass_langs:\n    - zh\n    - ar\n    - hi\n    - ko\n    - sw\n    zs_fail_langs: []\n    pass_fail: PARTIAL 2/4 (P2 5/5 PASS, P3 PASS 9.53pp, P1 FAIL ECE, P4 FAIL mean-shift)\n    note: 'zh@L31 sigmoid saturation artifact fixed (decision_function for AUROC).\n      P4 FAIL is expected: mean-shift adds constant offset to linear logits, AUROC\n      is rank-invariant.'\n    cka_vs_degradation:\n      overall_rho: -0.3982\n      overall_p: 0.0068\n      per_lang:\n        ar:\n          rho: -0.2833\n          p: 0.46\n        hi:\n          rho: -0.6667\n          p: 0.0499\n        ko:\n          rho: 0.25\n          p: 0.5165\n        sw:\n          rho: -0.5833\n          p: 0.0992\n        zh:\n          rho: -0.4833\n          p: 0.1875\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: 5-fold CV + PCA(100) + LogisticRegression (C=1.0, L2, lbfgs, max_iter=2000)\n    selectivity_hewitt_liang:\n      L0: 0.02\n      L4: 0.037\n      L8: 0.036\n      L12: 0.042\n      L16: 0.123\n      L20: 0.244\n      L24: 0.248\n      L27: 0.262\n    real_auroc:\n      L0: 0.501\n      L4: 0.524\n      L8: 0.529\n      L12: 0.53\n      L16: 0.615\n      L20: 0.733\n      L24: 0.738\n      L27: 0.746\n    permuted_auroc:\n      L0: 0.481\n      L4: 0.487\n      L8: 0.493\n      L12: 0.488\n      L16: 0.492\n      L20: 0.489\n      L24: 0.49\n      L27: 0.484\n    pca_variance_retained:\n      L0: 0.922\n      L4: 0.912\n      L8: 0.885\n      L12: 0.868\n      L16: 0.783\n      L20: 0.738\n      L24: 0.844\n      L27: 0.794\n    note: Selectivity = real_AUROC - permuted_AUROC (Hewitt & Liang 2019). Signal\n      concentrated in L20-L27. PCA(100) retains 73-92% variance.\n- exp_id: plan_013_probing_controls_v2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T05:21:02.215Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T05:21:02.215Z",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-21T05:21:02.255Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Simpson's Paradox 在 20 语言上双架构均不显著；CaCLR 失败且几何解释不成立；Pareto frontier 噪声大；高 artifact rate 动摇 probe 有效性
核心假设：["Simpson's Paradox partial correlation 在两个架构上均不显著——CKA 在 depth 之外无额外解释力，5 语言 pilot 结果是 small-sample artifact", 'CaCLR 失败且 CKA subspace 解释也不成立——correctness direction 的跨语言 persistence 弱于预期，非 robust low-dimensional subspace', 'Pareto frontier 噪声大：depth-transfer tradeoff 多数语言无一致显著性，非单调模式普遍', 'Difficulty decomposition 无实质效果——投影去除 difficulty 后 transfer 无变化，两信号纠缠不可分', 'Control task artifacts 波及中资源语言 (>35%)，probe 有效性受到广泛质疑，非仅低资源现象', 'Linear projection 效果不稳定——帮助/损害的阈值无法可靠确定，需要大量 pairs 且语言间方差大']
关键指标范围：{'en_best_auroc': [0.7, 0.76], 'zs_pass_rate_20lang': [0.5, 0.65], 'pareto_spearman_rho_significant_archs': [0, 1], 'simpson_partial_rho': [0.05, 0.2], 'simpson_p_value_max': [0.1, 0.5], 'caclr_mean_delta_auroc_vs_zs': [-0.02, 0.005], 'linear_proj_pairs_to_95pct': [100, 200], 'control_artifact_rate_lowres': [0.35, 0.5], 'decomp_capability_delta_auroc': [-0.01, 0.005], 'procrustes_reversal_threshold_zs_auroc': 'inconsistent — no clean threshold identifiable'}
叙事方向：需要大幅 reframe，但仍冲 EACL。原始几何洞见 framing 崩塌。新 angle：'The limits of cross-lingual calibration probe transfer: a large-scale negative result with methodological implications.' 核心贡献重构为三层：(1) 领域级方法论警示——control task 分析揭示 >35% 跨语言 probing 结果是 capacity artifacts，这是该发现的最强版本，首次在 cross-lingual transfer 场景应用 selectivity 检验，对所有跨语言 probing 研究有 field-level implication；(2) 综合 negative result 同时关闭 distributional matching (CaCLR) 和 geometric alignment 两条路径，附带 component ablation 和 β sweep 数据，reproducibility bar 高于正面结果；(3) 条件性实用指导——按 resource-tier 和 baseline ZS quality 分层给出推荐，linear projection 作为唯一可行但需 100+ pairs 的暴力方案。'Correctness direction 跨语言 language-agnostic' 这一前提假设在一般情况下被经验性证伪——这本身是对 Miao & Ungar (2026) 和 CORAL 研究线的重要回应。作为 rigorous negative results + methodology paper 仍可发 EACL。

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
  "promptId": "e4973730-fab6-4287-aa6b-8483d65fee63",
  "type": "user",
  "uuid": "621e065d-7c3a-4f57-a810-fb2ed9181e4a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T05:21:02.253Z_

```json
{
  "parentUuid": "621e065d-7c3a-4f57-a810-fb2ed9181e4a",
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
  "uuid": "3e9c329a-dbc3-4f67-951b-6e9b1d32a127",
  "timestamp": "2026-05-21T05:21:02.253Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T05:21:02.253Z_

```json
{
  "parentUuid": "3e9c329a-dbc3-4f67-951b-6e9b1d32a127",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "65311360-a12a-4203-8a07-e21cab193b3d",
  "timestamp": "2026-05-21T05:21:02.253Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T05:21:02.253Z_

```json
{
  "parentUuid": "65311360-a12a-4203-8a07-e21cab193b3d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "12af1c57-38f7-4208-bbfd-82703145b1b1",
  "timestamp": "2026-05-21T05:21:02.253Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Simpson's Paradox 在 20 语言上双架构均不显著；CaCLR 失败且几何解释不成立；Pareto frontier 噪声大；高 artifact rate 动摇 probe 有效性 核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均不显…",
  "leafUuid": "12af1c57-38f7-4208-bbfd-82703145b1b1",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe transfer: large-scale negative results and methodological implications",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55"
}
```

---

### Assistant

_source line 9 · 2026-05-21T05:23:01.946Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "worst" tier scenario for each planned experiment in the experiment_plan. Let me carefully go through each planned experiment and generate realistic worst-case predictions based on the worst-tier definition provided.

Let me review the worst tier definition:
- Simpson's Paradox partial correlation non-significant on both architectures across 20 languages
- CaCLR fails and geometric explanation doesn't hold
- Pareto frontier noisy
- High artifact rate undermining probe validity
- Key metrics: en_best_auroc [0.7, 0.76], zs_pass_rate_20lang [0.5, 0.65], pareto_spearman_rho_significant_archs [0, 1], simpson_partial_rho [0.05, 0.2], simpson_p_value_max [0.1, 0.5], caclr_mean_delta_auroc_vs_zs [-0.02, 0.005], linear_proj_pairs_to_95pct [

100, 200], control_artifact_rate_lowres [0.35, 0.5], decomp_capability_delta_auroc [-0.01, 0.005], procrustes_reversal_threshold_zs_auroc inconsistent

The core hypotheses that fail in the worst scenario are: Simpson's Paradox shows no significant partial correlation on either architecture, CaCLR completely fails with no meaningful CKA subspace explanation, the Pareto frontier becomes noisy with non-monotonic patterns, difficulty decomposition has zero effect, control task artifacts exceed 35% even in mid-resource languages, and linear projection becomes unstable with unreliable thresholds. Now I'll work through each planned experiment to generate realistic worst-case predictions for these metrics.

Starting with the Pareto frontier experiments on both Qwen3-235B-A22B and Llama 4 Scout, I'm expecting modest performance where English AUROC stays in the 0.71-0.74 range with zero-shot pass rates around 55%, and the frontier itself becomes noisy with non-monotonic tradeoffs across languages, especially in the MoE architecture. For CaCLR, the implementation shows the method failing outright—the mean delta AUROC versus zero-shot hovers near zero or slightly negative, the β sweep doesn't improve consistency, and the α sweep actually hurts discrimination through SB-ECE. Finally, projecting out difficulty has no measurable impact on transfer performance.

Looking at cross-lingual orthogonality, the patterns persist but with high variance that adds noise rather than clarity, and some languages break the orthogonality assumption entirely. The probe complexity comparison shows MLPs marginally outperform linear probes in English but transfer worse overall, confirming that simpler is better despite the noisy gap. Results don't generalize to Belebele or MMLU-ProX, which undermines confidence in the findings. Quantization introduces artifacts that muddy interpretation, and the CKA analysis reveals Simpson's Paradox at scale—partial correlations aren't significant and the subspace explanation doesn't hold. Linear projections need at least 100-200 sample pairs rather than 50 to be reliable.

The cross-lingual probing controls show high artifact rates in low and mid-resource languages, and I'm planning to tackle Gemma 4 and extended language coverage as secondary priorities. Now I'm constructing the detailed YAML output with specific numbers for each experiment, framing this as a large-scale negative result about the limits of cross-lingual calibration probe transfer and its methodological implications. For the worst-case Qwen3-235B scenario with its MoE architecture and INT4 quantization, I'm estimating the English best AUROC around 0.74. Now I'm mapping out the likely language distribution across resource tiers and estimating which ones would pass the zero-shot benchmark—expecting the high-resource languages like Chinese, Spanish, and French to perform better, while low-resource languages like Swahili and Bengali would struggle more, with the mid-tier languages falling somewhere in between.

For the Spearman correlation between model depth and transfer performance, I'm seeing a messy picture where most languages probably show no significant relationship or even negative correlation, meaning deeper models don't necessarily transfer better. Maybe only zero or one architecture would show a statistically significant Pareto pattern across the full language set.

Looking at Qwen specifically, it's right on the edge of significance around p=0.08, while Llama doesn't show anything meaningful. For Llama 4 Scout, the Pareto frontier is weaker overall—only about 60% of language pairs pass the zero-shot threshold, and the per-language correlations are scattered with no clear trend. The W4A16 quantization probably adds noise that obscures any underlying pattern. CaCLR appears to be a wash entirely, with transfer gains essentially flat or slightly negative across the board, and the hyperparameter sweeps for both β and α show no meaningful improvement in the loss metrics.

Difficulty decomposition doesn't seem to help either—projecting it out has negligible impact on transfer performance, and random direction controls suggest any gains are just artifacts of dimensionality reduction rather than actual signal separation. Cross-lingual orthogonality is inconsistent, holding tight in high-resource languages but varying wildly in low-resource ones with no clear pattern tied to resource availability. For probe complexity, MLPs show marginal gains in English but transfer worse overall, while linear probes are slightly better for generalization but the differences are noisy and often not significant. The additional benchmarks section appears to be cut off, but it looks like results aren't replicating cleanly.

Now checking quantization effects—there are small but real impacts, with weight-only quantization showing AUROC shifts up to 0.02 at certain layers, which adds some uncertainty but isn't catastrophic. The CKA analysis is where things really break down: Simpson's Paradox doesn't hold at full scale, and when I control for depth with partial correlation, neither model shows significant explanatory power from CKA, so it's not adding anything beyond what we already know.

The linear projection sensitivity analysis reveals I'd need 100-200 sample pairs for 95% performance rather than the hoped-for 50, with high variance across languages and no consistent resource-tier stratification. Most concerning is the probing controls work—artifact rates exceed 35% even in mid-resource languages, which fundamentally undermines the reliability of the cross-lingual findings and is probably the most damaging result in the worst-case scenario.

Now I'm organizing all the planned experiments into a comprehensive YAML format with detailed metrics, specific numbers, and predictions for the lower-priority P2 experiments like the Qwen and Llama Pareto analyses and the difficulty decomposition work.

I need to clarify the status of plan_013 since there's some ambiguity—the experiment plan lists it as planned, but the registry shows an English version already completed and a cross-lingual variant that's in a failed state, so I should verify whether a fresh cross-lingual probing controls experiment is actually scheduled or if this is a duplicate.

Now I'm constructing the detailed YAML output with all experiment specifications, including name, plan ID, description, expected metrics ranges, result rationales, data tables, figure descriptions, and analysis sections for each experiment. Now I'm drafting the YAML configuration with a typologically diverse set of 20 languages spanning high, mid, and low resource categories, then filling in zero-shot AUROC predictions for the worst tier model across these languages. Looking at the pass rate of 70%, that's too high for the worst tier range I'm targeting. I'm adjusting the scores downward across the mid-resource languages to bring the overall pass rate down and better distribute languages across the performance tiers. Looking at the Llama 4 Scout results, I'm getting 11 out of 20 languages passing at 55%, which still falls within the acceptable range. Now I need to examine the Spearman correlation between model depth and transfer performance across each language.

The pattern is quite messy—some languages show negative correlations where deeper probing actually hurts transfer performance, others are slightly positive, and many cluster near zero. For Qwen3-235B with its 24 probed layers, the correlations are consistently weak and mostly non-significant, with Chinese showing the strongest negative trend at -0.35 but still not statistically significant. Looking at the remaining languages, most show weak or non-significant correlations with the Pareto principle. The global pooled correlation is marginally significant but still weak, and only a handful of languages show the expected negative relationship. For Llama 4 Scout with fewer probed layers, the results are even noisier and less conclusive across the languages tested. Looking at the correlation coefficients across all languages, the global result shows no significant relationship, and with only twelve language samples, none of the individual correlations reach statistical significance either. Now I'm ready to structure the comprehensive YAML documentation covering all the planned experiments with their detailed metrics and rationale.

Examining the worst-tier results more closely: the Pareto significance is marginal at best with Qwen showing p=0.06, so effectively zero architectures meet the p<0.05 threshold. The Simpson's partial correlations are quite weak, ranging from 0.05 to 0.2, and the p-values are all too high to indicate any real effect. Meanwhile, the artifact contamination in low-resource probing is substantial—between 35-50% of results are artifacts, and this problem persists even in mid-resource languages. For the linear projection analysis, I need somewhere between 100 to 200 feature pairs to explain 95% of the variance.

The Procrustes reversal threshold shows no consistent pattern across the data. CaCLR appears neutral at best and slightly harmful at worst, with mean AUROC deltas hovering around -0.02 to 0.005. Decomposition methods similarly show negligible effects on capability, with deltas in the -0.01 to 0.005 range. Now I'm ready to compile the full output with comprehensive but concise rationale sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12af1c57-38f7-4208-bbfd-82703145b1b1",
  "isSidechain": false,
  "requestId": "req_011CbF9nFjkFVPnxRMpqrYm7",
  "type": "assistant",
  "uuid": "909d6c52-c434-495e-a49e-8c7be061358c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZjkMHzufEhpXk4saBe21E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17917,
      "cache_read_input_tokens": 11447,
      "output_tokens": 26129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 26129,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17917
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

_source line 10 · 2026-05-21T05:29:08.273Z_

```yaml
tier: worst
narrative_guidance: >
  原始几何洞见 framing 全面崩塌。Simpson's Paradox 在 20 语言全量验证中双架构均不显著（Qwen partial rho=+0.11, p=0.31; Llama partial rho=+0.08, p=0.42），
  CKA 在 depth 之外无额外解释力——5 语言 pilot 结果被确认为 small-sample artifact。CaCLR 三个 OOM 的 β sweep 证实 consistency loss 完全
  inert，且几何子空间解释也不成立：correctness direction 的跨语言 persistence 远弱于预期，非 robust low-dimensional subspace。
  Pareto frontier 噪声极大，20 语言中仅 2-3 个达到 per-language 显著性，non-monotonic 模式普遍存在。控制任务分析揭示问题远超预期——
  不仅低资源语言 artifact rate 达 42%，中资源语言也有 37% 层级组合出现 capacity artifacts，这对整个跨语言 probing 文献构成方法论挑战。
  Difficulty decomposition 完全无效，random-direction control 产生同量级效果。Linear projection 需要 120-180 pairs（非 50），
  且 Procrustes 效果反转阈值在语言间高度不一致，无法给出可靠的单一阈值。
  新 framing 路线：'The limits of cross-lingual calibration probe transfer — a large-scale negative result with methodological implications'。
  三层贡献重构：(1) 控制任务发现是最强贡献——首次在 cross-lingual probing 场景系统性应用 selectivity 检验，>35% artifact rate
  对整个领域有直接 implication；(2) 综合 negative result 同时关闭 distributional matching 和 geometric alignment 两条路径，
  附完整 ablation 和 sweep 数据；(3) 条件性实用指导——linear projection 作为唯一可行方案但需 100+ pairs，
  按 resource-tier 和 baseline ZS quality 分层推荐。仍可发 EACL 作为 rigorous negative result + methodology paper。

imagined_experiments:

  - name: "Qwen3-235B Full Pareto Frontier"
    plan_id: "plan_001"
    description: "Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th), 20 languages, 5 transfer conditions"
    expected_results:
      en_best_auroc: 0.738
      en_best_layer: 72
      en_auroc_range: [0.598, 0.738]
      en_best_ece_raw: 0.203
      zs_pass_count: 12
      zs_pass_rate: 0.60
      zs_pass_langs: [zh, es, fr, de, ja, pt, it, ar, hi, ru, ko, vi]
      zs_fail_langs: [tr, th, sw, bn, am, yo, te, my]
      best_zs_auroc:
        zh: 0.672
        es: 0.681
        fr: 0.663
        de: 0.654
        ja: 0.582
        pt: 0.668
        it: 0.651
        ar: 0.603
        hi: 0.561
        ru: 0.624
        ko: 0.585
        tr: 0.541
        vi: 0.558
        th: 0.523
        sw: 0.512
        bn: 0.519
        am: 0.482
        yo: 0.471
        te: 0.498
        my: 0.463
      global_spearman_rho: -0.15
      global_spearman_p: 0.062
      per_lang_significant_negative_rho_count: 2
      per_lang_significant_positive_rho_count: 0
      per_lang_nonmonotonic_count: 14
      mean_shift_delta_auroc_all: 0.0
      linear_proj_200pair_mean_delta: +0.038
      fewshot_25_mean_delta: +0.022
      fewshot_100_mean_delta: +0.051
    result_rationale: >
      EN best AUROC 落在 worst 范围 [0.7, 0.76] 内。MoE routing 导致层间 representation 变异度增大，
      每第 4 层采样可能跳过 expert routing 的关键切换点，引入额外噪声。INT4 量化对 correctness signal 有轻微衰减（plan_010 将确认）。
      ZS 60% pass rate 因为：(1) 235B 参数量提升了高/中资源语言的 representation quality，但 INT4 折损部分增益；
      (2) MoE 的 expert specialization 可能导致不同语言路由到不同 expert 子集，correctness direction 的跨语言一致性被 expert 分化削弱；
      (3) 低资源语言在预训练中 token 占比不足，加之 MoE 可能给它们分配较少 expert capacity。
      Global Pareto rho=-0.15 仅 marginally significant (p=0.062)：depth-transfer tradeoff 在多数语言不显著，
      因为 MoE 中 depth 不单调地映射到 representation specialization——expert routing 在不同深度可以"重置"语言特异性。
      14/20 语言呈现 non-monotonic 模式（U 形、倒 U 形、锯齿形），这是 MoE 特有的现象。
      Mean-shift ΔAUROC ≡ 0 符合已证明的数学不变性。Linear projection 和 few-shot 有正增益但方差大。
    tables:
      - name: "Table 1a: Qwen3-235B Per-Language Pareto Spearman ρ (Depth vs ZS-AUROC)"
        columns: [lang, resource_tier, best_zs_auroc, best_zs_layer, spearman_rho, p_value, pattern]
        rows:
          - [zh, HIGH, 0.672, 60, -0.35, 0.093, "weak negative"]
          - [es, HIGH, 0.681, 56, -0.28, 0.184, "n.s."]
          - [fr, HIGH, 0.663, 60, -0.31, 0.141, "n.s."]
          - [de, HIGH, 0.654, 56, -0.22, 0.300, "n.s."]
          - [ja, HIGH, 0.582, 48, +0.15, 0.483, "non-monotonic U-shape"]
          - [pt, HIGH, 0.668, 60, -0.25, 0.238, "n.s."]
          - [it, HIGH, 0.651, 56, -0.19, 0.375, "n.s."]
          - [ar, MID, 0.603, 52, +0.08, 0.710, "flat"]
          - [hi, MID, 0.561, 48, -0.42, 0.041, "significant negative"]
          - [ru, MID, 0.624, 56, -0.18, 0.398, "n.s."]
          - [ko, MID, 0.585, 44, +0.22, 0.301, "inverted — deeper helps"]
          - [tr, MID, 0.541, 44, -0.12, 0.576, "n.s."]
          - [vi, MID, 0.558, 48, +0.05, 0.815, "flat"]
          - [th, MID, 0.523, 40, -0.08, 0.710, "n.s."]
          - [sw, LOW, 0.512, 36, -0.38, 0.067, "marginal negative"]
          - [bn, LOW, 0.519, 40, -0.15, 0.485, "n.s."]
          - [am, LOW, 0.482, 32, +0.10, 0.641, "non-monotonic"]
          - [yo, LOW, 0.471, 28, -0.05, 0.815, "noisy flat"]
          - [te, LOW, 0.498, 36, -0.20, 0.348, "n.s."]
          - [my, LOW, 0.463, 28, +0.12, 0.576, "non-monotonic"]
      - name: "Table 1b: Qwen3-235B 5 Transfer Conditions Summary (mean across 20 langs)"
        columns: [condition, mean_auroc, std, delta_vs_zs, significant_improvement_count]
        rows:
          - [zero-shot, 0.572, 0.072, 0.000, "—"]
          - [mean-shift, 0.572, 0.072, 0.000, "0/20"]
          - [linear_proj_200, 0.610, 0.058, +0.038, "11/20"]
          - [fewshot_25, 0.594, 0.065, +0.022, "7/20"]
          - [fewshot_100, 0.623, 0.054, +0.051, "13/20"]
    figures_description:
      - "Figure 1a: Scatter plot of EN AUROC vs best ZS AUROC per language across 24 layers for Qwen3-235B. Points colored by resource tier. Shows diffuse cloud rather than clean Pareto frontier. Non-monotonic trajectories for ja, ko, am, my highlighted with dashed lines. Annotation shows global rho=-0.15 (p=0.062)."
      - "Figure 1b: Heatmap of ZS AUROC per language (y-axis) × probed layer (x-axis). Shows irregular patterns with MoE-specific layer-to-layer variance. No smooth gradient along depth axis."
    analysis: >
      Qwen3-235B 的 Pareto frontier 远不如 MVP (Qwen2.5-7B) 清晰。MoE 架构的 expert routing 打破了
      dense model 中 depth = specialization 的单调映射，导致 14/20 语言呈现 non-monotonic 模式。
      仅 hi 和 sw 达到 per-language 显著性，但方向相反的 ko (+0.22, n.s.) 和 ja (+0.15, n.s.) 表明
      depth-transfer tradeoff 不是普遍现象。Global rho=-0.15 被 between-language 差异驱动而非 within-language
      depth 效应。MVP 的 clear Pareto 可能是 dense 7B model 的特殊现象，不推广到大规模 MoE。
      5 transfer conditions 中 linear projection 和 few-shot 100 有中等改善，但 significant improvement
      仅覆盖 55-65% 的语言，且主要集中在高资源语言。

  - name: "Llama 4 Scout Full Pareto Frontier"
    plan_id: "plan_002"
    description: "Llama 4 Scout (48 layers, MoE, W4A16), 12 probed layers, 20 languages, 5 transfer conditions"
    expected_results:
      en_best_auroc: 0.715
      en_best_layer: 40
      en_auroc_range: [0.612, 0.715]
      en_best_ece_raw: 0.218
      zs_pass_count: 11
      zs_pass_rate: 0.55
      zs_pass_langs: [zh, es, fr, de, pt, it, ar, ru, ko, vi, ja]
      zs_fail_langs: [hi, tr, th, sw, bn, am, yo, te, my]
      best_zs_auroc:
        zh: 0.643
        es: 0.658
        fr: 0.641
        de: 0.632
        ja: 0.556
        pt: 0.645
        it: 0.628
        ar: 0.581
        hi: 0.542
        ru: 0.602
        ko: 0.571
        tr: 0.523
        vi: 0.555
        th: 0.508
        sw: 0.496
        bn: 0.505
        am: 0.468
        yo: 0.455
        te: 0.487
        my: 0.448
      global_spearman_rho: -0.08
      global_spearman_p: 0.218
      per_lang_significant_negative_rho_count: 0
      per_lang_significant_positive_rho_count: 0
      per_lang_nonmonotonic_count: 11
    result_rationale: >
      Llama 4 Scout 的 EN AUROC 低于 Qwen3 因为模型有效参数量更小（17B active vs 22B active）。
      W4A16 量化对 correctness signal 有轻微额外损耗。ZS pass rate 55% 处于 worst 范围低端。
      仅 12 probed layers 使 per-language Spearman 检验功效极低（n=12），无语言达到显著性。
      MVP (Llama-3.1-8B) 中观察到的 architecture-specific 弱 Pareto 在 Scout 上进一步恶化：
      Scout 是 MoE (16 experts)，与 3.1-8B 的 dense 架构根本不同，expert routing 引入同样的
      non-monotonic 行为。Global rho=-0.08 完全不显著——Llama 架构系列的 depth-transfer tradeoff 不稳定。
    tables:
      - name: "Table 2: Llama 4 Scout Per-Language Pareto Spearman ρ"
        columns: [lang, resource_tier, best_zs_auroc, spearman_rho, p_value]
        rows:
          - [zh, HIGH, 0.643, -0.20, 0.533]
          - [es, HIGH, 0.658, -0.15, 0.641]
          - [fr, HIGH, 0.641, -0.25, 0.432]
          - [de, HIGH, 0.632, -0.10, 0.758]
          - [ja, HIGH, 0.556, +0.30, 0.343]
          - [pt, HIGH, 0.645, -0.18, 0.576]
          - [it, HIGH, 0.628, -0.08, 0.805]
          - [ar, MID, 0.581, +0.25, 0.432]
          - [hi, MID, 0.542, -0.35, 0.264]
          - [ru, MID, 0.602, -0.05, 0.878]
          - [ko, MID, 0.571, +0.40, 0.198]
          - [tr, MID, 0.523, +0.10, 0.758]
          - [vi, MID, 0.555, +0.15, 0.641]
          - [th, MID, 0.508, -0.20, 0.533]
          - [sw, LOW, 0.496, -0.28, 0.379]
          - [bn, LOW, 0.505, -0.10, 0.758]
          - [am, LOW, 0.468, +0.05, 0.878]
          - [yo, LOW, 0.455, -0.15, 0.641]
          - [te, LOW, 0.487, -0.08, 0.805]
          - [my, LOW, 0.448, +0.18, 0.576]
    figures_description:
      - "Figure 2: Llama 4 Scout Pareto scatter, same format as Figure 1a. Cloud更加散乱，global rho=-0.08 (p=0.218)。Ko (+0.40) 和 ja (+0.30) 方向相反于预期。"
    analysis: >
      Llama 4 Scout 确认 worst tier 预期：depth-transfer tradeoff 在 MoE 架构上完全不显著。
      与 Qwen3-235B 合并看，0 个架构在 p<0.05 水平展现清晰的 Pareto——pareto_spearman_rho_significant_archs=0。
      MVP 中 Qwen2.5-7B dense model 的 clear Pareto 是 dense architecture + small scale 的特殊现象，
      不推广到大规模 MoE。这对 Claim 1 是毁灭性的：无法声称存在普遍的 depth-transferability tradeoff。

  - name: "CaCLR Implementation and Comparative Evaluation"
    plan_id: "plan_003"
    description: "CaCLR (BCE + α·SB-ECE + β·MMD), β sweep 3 OOM, α sweep, component ablation, vs 4 baselines, 2 models × 20 langs"
    expected_results:
      caclr_mean_delta_auroc_vs_zs_qwen: -0.008
      caclr_mean_delta_auroc_vs_zs_llama: -0.012
      caclr_mean_delta_auroc_combined: -0.010
      caclr_best_beta: "none — all β values inert or harmful"
      caclr_best_alpha: 0.1
      beta_sweep_results:
        beta_0.001: {mean_delta_auroc: -0.003, std: 0.018}
        beta_0.01: {mean_delta_auroc: -0.006, std: 0.021}
        beta_0.1: {mean_delta_auroc: -0.011, std: 0.025}
        beta_1.0: {mean_delta_auroc: -0.019, std: 0.031}
      alpha_sweep_results:
        alpha_0.01: {mean_delta_auroc: -0.002, mean_delta_ece: +0.008}
        alpha_0.1: {mean_delta_auroc: -0.005, mean_delta_ece: +0.003}
        alpha_1.0: {mean_delta_auroc: -0.012, mean_delta_ece: -0.002}
        alpha_10.0: {mean_delta_auroc: -0.028, mean_delta_ece: -0.005}
      component_ablation:
        bce_only: {delta_vs_zs: -0.001, note: "retraining from scratch ~= standard LR"}
        bce_plus_sbece: {delta_vs_zs: -0.007, note: "SB-ECE regularization hurts discrimination"}
        bce_plus_mmd: {delta_vs_zs: -0.005, note: "MMD inert to slightly harmful"}
        full_caclr: {delta_vs_zs: -0.010, note: "combined losses compound harm"}
      linear_proj_vs_caclr_delta: +0.048
      fewshot100_vs_caclr_delta: +0.061
      implementation_spec:
        mmd_kernel: "Gaussian RBF, bandwidth=median heuristic"
        optimizer: "Adam, lr=1e-3, cosine schedule"
        epochs: 50
        early_stopping: "patience=10 on held-out BCE loss"
        initialization: "from standard LR solution"
        batch_size: 256
        mmd_items: "same items as BCE (probe_train split)"
        parallel_set_size_range: [612, 2847]
    result_rationale: >
      CaCLR 失败的根本原因：MMD 在 probe logits 空间操作，而 logits 是 1-D（线性 probe 的单一输出）。
      1-D MMD 只能 match 两个标量分布的 marginal，无法对齐 correctness direction 的方向性结构。
      即使 marginal logit 分布被 match，EN 和 target 的 conditional distributions P(logit|correct) vs P(logit|incorrect)
      可能仍然不同——Zhao et al. (2019) 的理论预测得到验证。β 越大，MMD 约束越强，
      logits 被拉向无区分性的 marginal match，discrimination 下降。α 高值时 SB-ECE 正则化
      进一步牺牲 AUROC 以换取 calibration 改善，但改善微小且不稳定。Component ablation 证实
      每个额外 loss component 都是净负面的——base BCE（从 LR solution 初始化再微调）已经接近 ZS 性能，
      额外优化无正贡献。Linear projection 和 few-shot 都显著优于 CaCLR，因为它们直接利用
      target-language 信息（parallel pairs 或 labels）而非试图间接 match distributions。
      CKA subspace 解释（correctness direction 是 low-dimensional language-agnostic subspace）
      不成立——如果该 subspace 真的存在且 robust，MMD 应该至少能做到无害，但实际上有害，
      说明 correctness signal 的跨语言结构比预期更 language-specific。
    tables:
      - name: "Table 3a: CaCLR β Sweep (Qwen3-235B, fixed layer 50% depth, 20 langs mean)"
        columns: [beta, mean_auroc, delta_vs_zs, pct_langs_improved, pct_langs_harmed]
        rows:
          - [0.001, 0.570, -0.003, "30%", "45%"]
          - [0.01, 0.567, -0.006, "25%", "55%"]
          - [0.1, 0.562, -0.011, "15%", "65%"]
          - [1.0, 0.554, -0.019, "10%", "80%"]
      - name: "Table 3b: 5-Way Transfer Condition Comparison (both models × 20 langs, EN-optimal layer)"
        columns: [condition, mean_auroc, mean_ece, delta_auroc_vs_zs, win_rate_vs_zs]
        rows:
          - [zero-shot, 0.568, 0.285, "—", "—"]
          - [mean-shift, 0.568, 0.291, 0.000, "0%"]
          - [CaCLR_best, 0.558, 0.278, -0.010, "18%"]
          - [linear_proj_200, 0.606, 0.248, +0.038, "72%"]
          - [fewshot_25, 0.590, 0.262, +0.022, "55%"]
          - [fewshot_100, 0.619, 0.235, +0.051, "78%"]
      - name: "Table 3c: CaCLR Component Ablation"
        columns: [configuration, mean_auroc, delta_vs_zs, note]
        rows:
          - ["BCE only (re-init)", 0.567, -0.001, "≈ ZS baseline"]
          - ["BCE + SB-ECE (α=0.1)", 0.561, -0.007, "ECE gains tiny, AUROC drops"]
          - ["BCE + MMD (β=0.01)", 0.563, -0.005, "MMD inert/harmful"]
          - ["Full CaCLR (α=0.1, β=0.01)", 0.558, -0.010, "compound degradation"]
    figures_description:
      - "Figure 3a: β sweep curve showing monotonic decrease in mean AUROC as β increases from 0.001 to 1.0. Shaded region = bootstrap 95% CI. All CIs include or fall below zero-shot baseline."
      - "Figure 3b: Per-language ΔAUROC (CaCLR vs ZS) bar chart at best β=0.001. Most bars negative; only 3-4 high-resource languages show marginal positive ΔAUROC within noise margin."
    analysis: >
      CaCLR 的 negative result 是 worst tier 的核心。β sweep 证实 consistency loss 在所有 3 OOM 均为 inert 或 harmful——
      这不是超参选择问题而是方法论层面的失败。1-D MMD 的结构性限制（probe logit 空间太低维）加上
      conditional distribution mismatch（Zhao et al. 2019）导致 distributional matching 路径被彻底关闭。
      与此同时，CKA subspace 解释也不成立（plan_011 将确认），所以"MMD 失败是因为它只 match marginal
      而不 match subspace direction"这个 elegant 的解释也变成了 post-hoc rationalization——
      实际上 subspace 本身就不 robust。这是 worst tier 最痛苦的部分：不仅方法失败，解释也失败。
      但作为 negative result，reproducibility 标准高：完整的 implementation spec、β/α sweep、
      component ablation 使社区可以独立验证，避免重复尝试 distributional matching 路径。

  - name: "Difficulty-Controlled Decomposition Ablation"
    plan_id: "plan_004"
    description: "IRT difficulty probes → project out → retrain correctness probes, 10 langs × 8 layers × 2 models"
    expected_results:
      decomp_capability_delta_auroc_mean: -0.003
      decomp_capability_delta_auroc_range: [-0.015, +0.008]
      random_direction_control_delta_mean: -0.005
      random_direction_control_delta_range: [-0.018, +0.006]
      difficulty_probe_r2: 0.31
      decomp_vs_random_paired_test_p: 0.42
      per_tier_delta:
        HIGH: {mean_delta: -0.002, significant_count: "0/4"}
        MID: {mean_delta: -0.004, significant_count: "0/3"}
        LOW: {mean_delta: -0.003, significant_count: "0/3"}
    result_rationale: >
      Difficulty decomposition 在 worst tier 无实质效果。两个原因：(1) difficulty 和 capability 信号在
      representation 空间中高度纠缠——IRT difficulty direction 不是一个干净的、可投影去除的独立子空间，
      而是与 correctness signal 共享大量方差。投影去除 difficulty 后 correctness signal 也被部分损坏，
      导致 retrained probe 的 transfer 性能与原始相当甚至略差。(2) Random-direction control 产生
      同量级的效果（mean delta -0.005 vs -0.003，paired test p=0.42），这意味着观察到的微小变化
      主要来自 dimensionality reduction 效应而非 difficulty-specific 投影。Difficulty probe 本身
      R²=0.31（低于理想值），表明 IRT difficulty 在 LLM representation 中的编码不够线性/集中，
      使得 linear projection 无法有效捕获它。整个 decomposition framing 在经验层面被否定：
      transfer 的降解不能归因于 capability-specific component，或者说两个 component 不可分。
    tables:
      - name: "Table 4: Difficulty Decomposition Ablation (mean across 2 models)"
        columns: [lang, resource_tier, original_zs_auroc, after_projection_auroc, delta, random_control_delta, decomp_vs_random_p]
        rows:
          - [zh, HIGH, 0.658, 0.655, -0.003, -0.006, 0.61]
          - [es, HIGH, 0.670, 0.669, -0.001, -0.004, 0.52]
          - [fr, HIGH, 0.652, 0.649, -0.003, -0.007, 0.38]
          - [de, HIGH, 0.643, 0.642, -0.001, -0.003, 0.71]
          - [hi, MID, 0.552, 0.547, -0.005, -0.008, 0.55]
          - [ru, MID, 0.613, 0.610, -0.003, -0.005, 0.64]
          - [ko, MID, 0.578, 0.572, -0.006, -0.004, 0.48]
          - [tr, MID, 0.532, 0.530, -0.002, -0.006, 0.33]
          - [sw, LOW, 0.504, 0.501, -0.003, -0.005, 0.58]
          - [bn, LOW, 0.512, 0.504, -0.008, -0.007, 0.82]
    figures_description:
      - "Figure 4: Paired bar chart comparing delta AUROC after difficulty projection (blue) vs random-direction projection (gray) for each language. Error bars = bootstrap 95% CI. All CIs overlap; no language shows meaningful separation between decomposition and random control."
    analysis: >
      Decomposition 的 null result 与 random-direction control 不可区分（p=0.42），表明投影效应来自
      dimensionality reduction 而非 difficulty-specific 信号去除。这从根本上否定了 Claim 2 的因果叙述——
      transfer degradation 不能分解为 difficulty-shared 和 capability-specific 两个可操作的 component。
      在 worst tier framing 中，这成为 negative result 的一部分：decomposition 是另一条被关闭的路径。

  - name: "Cross-Lingual Orthogonality Analysis"
    plan_id: "plan_005"
    description: "Correctness-confidence cosine similarity, 20 langs × 2 architectures, resource-tier 和 language family 分析"
    expected_results:
      mean_cosine_high_resource: 0.038
      mean_cosine_mid_resource: 0.065
      mean_cosine_low_resource: 0.112
      std_cosine_low_resource: 0.082
      cosine_range_all: [0.008, 0.198]
      architecture_agreement_rate: 0.65
      outlier_langs: [am, yo, my]
    result_rationale: >
      Orthogonality 在高资源语言基本成立（cosine < 0.05），复现 Miao & Ungar (2026) 的英文发现。
      但低资源语言的 cosine similarity 显著升高且方差极大（mean=0.112, std=0.082），部分语言
      （am=0.198, yo=0.165, my=0.142）接近打破 orthogonality 假设。这可能是因为低资源语言
      的 correctness 和 confidence directions 都更 noisy（probe 本身 selectivity 低——见 plan_013），
      而非真正的非正交结构。Architecture 一致性仅 65%：两个架构在 7/20 语言上对 orthogonality 程度
      给出矛盾信号，削弱了"orthogonality is a universal property"的叙述。
      作为 subsection（已从 standalone claim 降级），这些结果增加了复杂性但没有清晰的 takeaway。
    tables:
      - name: "Table 5: Cross-Lingual Orthogonality (Cosine Similarity)"
        columns: [lang, tier, qwen3_cosine, llama4_cosine, agreement, note]
        rows:
          - [zh, HIGH, 0.031, 0.028, "✓", ""]
          - [es, HIGH, 0.025, 0.033, "✓", ""]
          - [fr, HIGH, 0.029, 0.041, "✓", ""]
          - [de, HIGH, 0.035, 0.038, "✓", ""]
          - [ja, HIGH, 0.048, 0.052, "✓", ""]
          - [pt, HIGH, 0.027, 0.035, "✓", ""]
          - [it, HIGH, 0.033, 0.039, "✓", ""]
          - [ar, MID, 0.042, 0.058, "✓", ""]
          - [hi, MID, 0.055, 0.072, "✓", ""]
          - [ru, MID, 0.038, 0.045, "✓", ""]
          - [ko, MID, 0.061, 0.048, "✗", "direction reversed"]
          - [tr, MID, 0.075, 0.068, "✓", ""]
          - [vi, MID, 0.052, 0.082, "✗", "magnitude mismatch"]
          - [th, MID, 0.088, 0.065, "✗", "magnitude mismatch"]
          - [sw, LOW, 0.095, 0.108, "✓", "elevated"]
          - [bn, LOW, 0.082, 0.118, "✗", ""]
          - [am, LOW, 0.198, 0.152, "✓", "near non-orthogonal"]
          - [yo, LOW, 0.165, 0.128, "✗", ""]
          - [te, LOW, 0.105, 0.092, "✓", ""]
          - [my, LOW, 0.142, 0.118, "✓", "elevated"]
    figures_description:
      - "Figure 5: Box plot of correctness-confidence cosine similarity by resource tier, faceted by architecture. LOW tier shows significantly higher median and wider spread than HIGH/MID. Dashed line at cosine=0.10 marks 'practical orthogonality threshold'."
    analysis: >
      Orthogonality 作为 subsection 贡献了一个 nuanced finding：该性质是 resource-tier dependent，
      低资源语言中不可靠。但在 worst tier 下这个 finding 被 plan_013 的高 artifact rate 进一步削弱——
      低资源语言的高 cosine 可能反映 probe 本身的 capacity artifact 而非真正的非正交 representation 结构。
      Section 简化为："orthogonality generally holds but becomes unreliable for low-resource languages，
      where probe validity itself is questionable (Section X)." 贡献有限。

  - name: "Probe Complexity Comparison"
    plan_id: "plan_006"
    description: "Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer + calibration, 2 models × 20 langs"
    expected_results:
      en_auroc_lr_mean: 0.726
      en_auroc_mlp_mean: 0.741
      mlp_en_advantage: +0.015
      zs_transfer_lr_mean_degradation: 0.152
      zs_transfer_mlp_mean_degradation: 0.191
      mlp_transfer_disadvantage: -0.039
      lr_better_for_transfer_pct: 0.70
      ece_lr_mean: 0.242
      ece_mlp_mean: 0.258
      selectivity_lr_mean: 0.218
      selectivity_mlp_mean: 0.235
    result_rationale: >
      MLP 在 EN 上因更高 capacity 而有 +1.5pp AUROC 优势，但跨语言 transfer 时 degradation 更大
      （-19.1% vs -15.2%），符合"linear probes transfer better"假设。然而在 worst tier 下，
      这个差异虽然方向正确但 effect size 不大（Cohen's d ≈ 0.3），且 70% 而非 90%+ 的语言
      支持 LR > MLP for transfer，因为部分高资源语言中 MLP 的额外 capacity 弥补了 transfer 损失。
      此外 MLP 的 selectivity 仅比 LR 高 0.017，表明额外 capacity 带来的 artifact 风险有限——
      这与 plan_013 的高 artifact rate 形成有趣对比（artifacts 主要来自语言本身而非 probe 复杂度）。
    tables:
      - name: "Table 6: Probe Complexity Comparison Summary"
        columns: [metric, logistic_regression, mlp_2layer, delta, p_value]
        rows:
          - [EN AUROC (mean), 0.726, 0.741, +0.015, 0.008]
          - [ZS degradation (mean), "15.2%", "19.1%", "+3.9pp", 0.023]
          - [ZS AUROC (mean), 0.616, 0.600, -0.016, 0.041]
          - [EN ECE (mean), 0.242, 0.258, +0.016, 0.065]
          - [Selectivity (mean), 0.218, 0.235, +0.017, 0.112]
          - [LR better for transfer, "70%", "30%", "—", "—"]
    figures_description:
      - "Figure S1 (appendix): Layer-wise EN AUROC for LR vs MLP showing MLP advantage increases with depth. Paired with ZS AUROC showing LR advantage for transfer grows at deep layers."
    analysis: >
      LR vs MLP 比较方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下，
      probe complexity 不是主要问题——语言-层级 capacity artifacts 才是。
      结论：保持 LR 作为默认，MLP 结果放 appendix。

  - name: "Additional Benchmark Evaluation (Belebele + MMLU-ProX)"
    plan_id: "plan_007"
    description: "Best probes + CaCLR on Belebele 和 MMLU-ProX, 20 languages each, generalization test"
    expected_results:
      belebele_zs_pass_rate: 0.50
      belebele_mean_zs_auroc: 0.548
      belebele_vs_globalmmlu_spearman_rho: 0.72
      belebele_vs_globalmmlu_mean_auroc_delta: -0.024
      mmlupx_zs_pass_rate: 0.55
      mmlupx_mean_zs_auroc: 0.562
      mmlupx_vs_globalmmlu_spearman_rho: 0.78
      caclr_belebele_delta_vs_zs: -0.013
      caclr_mmlupx_delta_vs_zs: -0.008
      linear_proj_belebele_delta: +0.031
      linear_proj_mmlupx_delta: +0.035
    result_rationale: >
      Belebele 的 reading comprehension 格式与 MCQA correctness probing 的 mismatch 导致更低的 pass rate。
      MMLU-ProX 与 GlobalMMLU 更接近（同为知识 MCQA）所以 correlation 更高。CaCLR 在两个 benchmark 上
      同样失败甚至更差——distribution mismatch 在 out-of-distribution 数据上放大。
      Linear projection 仍有正增益但幅度小于 GlobalMMLU——cross-benchmark generalization 有衰减。
      整体 pattern：在 worst tier 下 generalization 弱化了已经微弱的 positive findings，
      reinforcing negative result narrative。Belebele 的低 pass rate 尤其令人担忧——
      correctness probe 的概念可能不 generalize beyond MCQA knowledge questions。
    tables:
      - name: "Table 7: Cross-Benchmark Generalization"
        columns: [benchmark, zs_pass_rate, mean_zs_auroc, caclr_delta, linproj_delta, correlation_with_globalmmlu]
        rows:
          - [GlobalMMLU, 0.575, 0.572, -0.010, +0.038, "—"]
          - [Belebele, 0.500, 0.548, -0.013, +0.031, 0.72]
          - [MMLU-ProX, 0.550, 0.562, -0.008, +0.035, 0.78]
    figures_description:
      - "Figure S2 (appendix): Scatter plot of per-language ZS AUROC on GlobalMMLU vs Belebele/MMLU-ProX. Moderate positive correlation but visible deviations, especially for low-resource languages."
    analysis: >
      Cross-benchmark generalization moderate but not strong。Belebele 的低 performance 暗示
      correctness probing 可能对任务格式敏感。在 worst-tier paper 中这增加了一层 caveat：
      findings 可能 MCQA-specific，generalization to other formats uncertain。

  - name: "Quantization Validation Ablation"
    plan_id: "plan_010"
    description: "W4A16 vs FP16 (Llama), INT4 vs FP16 (Qwen), 5 representative layers, 5% data subset"
    expected_results:
      llama_w4a16_vs_fp16_max_delta_auroc: 0.018
      llama_w4a16_vs_fp16_mean_delta_auroc: 0.009
      llama_w4a16_vs_fp16_spearman_rank_preservation: 0.91
      qwen_int4_vs_fp16_max_delta_auroc: 0.022
      qwen_int4_vs_fp16_mean_delta_auroc: 0.012
      qwen_int4_vs_fp16_spearman_rank_preservation: 0.88
      problematic_layers_count: 2
    result_rationale: >
      Worst tier 下量化 artifacts 不是灾难性的但 non-negligible。W4A16 mean delta 0.9pp 和
      INT4 mean delta 1.2pp 在多数层可接受，但在 2/5 测试层出现 >1.5pp 偏差——
      特别是在最深层（correctness signal 最集中的地方），quantization 对高频/低方差的
      correctness direction 影响更大。Rank preservation 88-91% 意味着 per-language ranking
      大体保持但不完美。在 worst tier 下这创造了一个 uncomfortable caveat：
      所有关于深层 probe 的结论都 potentially 受量化影响，但无法做完整的 FP16 实验来确认。
      需要在 limitations 中明确讨论。INT4 比 W4A16 worse 因为 4-bit weight-only 比
      4-bit weight + 16-bit activation 更 aggressive。
    tables:
      - name: "Table 8: Quantization Validation"
        columns: [model, quant, layer_pct, fp16_auroc, quant_auroc, delta, rank_preserved]
        rows:
          - [Llama4, W4A16, "20%", 0.648, 0.645, -0.003, "✓"]
          - [Llama4, W4A16, "40%", 0.672, 0.665, -0.007, "✓"]
          - [Llama4, W4A16, "60%", 0.695, 0.683, -0.012, "✓"]
          - [Llama4, W4A16, "80%", 0.708, 0.692, -0.016, "✗ (2 langs swap)"]
          - [Llama4, W4A16, "95%", 0.712, 0.694, -0.018, "✗ (3 langs swap)"]
          - [Qwen3, INT4, "20%", 0.625, 0.620, -0.005, "✓"]
          - [Qwen3, INT4, "40%", 0.668, 0.658, -0.010, "✓"]
          - [Qwen3, INT4, "60%", 0.702, 0.688, -0.014, "✗ (1 lang swap)"]
          - [Qwen3, INT4, "80%", 0.728, 0.710, -0.018, "✗ (3 langs swap)"]
          - [Qwen3, INT4, "95%", 0.738, 0.716, -0.022, "✗ (4 langs swap)"]
    figures_description:
      - "Figure S3 (appendix): Layer-wise quantization delta plot showing increasing divergence with depth for both models."
    analysis: >
      Quantization 在深层引入 1-2pp 的系统性偏差。在 worst tier 下这不改变主要结论（negative results
      不依赖于精确数值），但增加了 limitations section 的内容。Deep layer probe results（包括
      EN-optimal layer 的 AUROC）可能被 overestimate 了 ~1pp by quantization loss。

  - name: "CKA Cross-Lingual Representation Similarity Analysis"
    plan_id: "plan_011"
    description: "CKA (linear kernel) EN vs target, all probed layers, 20 langs × 2 models. Simpson's Paradox 验证。"
    expected_results:
      simpson_partial_rho_qwen: 0.11
      simpson_partial_p_qwen: 0.31
      simpson_partial_rho_llama: 0.08
      simpson_partial_p_llama: 0.42
      raw_correlation_rho_qwen: -0.28
      raw_correlation_rho_llama: -0.35
      raw_correlation_p_qwen: 0.001
      raw_correlation_p_llama: "<0.001"
      same_layer_cross_lang_rho_median: 0.15
      same_layer_cross_lang_significant_layers: "2/24 (Qwen), 0/12 (Llama)"
      cka_threshold_identifiable: false
      subspace_angle_consistency: "low — angles vary 15-65° across languages at same layer"
      pilot_replication_5lang: "partial — Llama rho drops from +0.41 to +0.08 with 20 langs"
    result_rationale: >
      这是 worst tier 最关键的 falsification。5 语言 pilot 中的 Simpson's Paradox (Llama partial rho=+0.41, p=0.006)
      被确认为 small-sample artifact。当 20 语言数据进入分析后：(1) 新增的 15 种语言中多数与 CKA-transfer
      关系不一致，部分语言（特别是 MID/LOW tier）的 CKA 模式与 pilot 的 5 种语言截然不同——
      pilot 恰好选中了 CKA 与 transfer 最相关的语言子集（zh, ar 高 CKA + 低 degradation 拉高了相关性）。
      (2) Partial correlation controlling for depth 大幅缩水：Qwen rho 从 pilot 的 +0.18 降至 +0.11 (仍 n.s.)，
      Llama rho 从 +0.41 骤降至 +0.08。原因是新增语言打破了"within-layer CKA predicts transfer"的模式——
      同一层内不同语言的 CKA 值差异巨大但 transfer 性能差异不 track CKA。
      (3) Same-layer cross-language analysis (n=20 per layer) 是最强检验：median rho=0.15，
      仅 2/24 Qwen layers 和 0/12 Llama layers 达到显著——CKA 在 within-layer 水平几乎无解释力。
      (4) Subspace angle analysis 显示 correctness direction 的跨语言一致性远低于预期——
      angles 在 15-65° 范围波动，不支持"robust low-dimensional language-agnostic subspace"的说法。
      结论：CKA 不提供超越 depth 的解释力，必须从"geometric analysis"降级为"suggestive correlation"。
    tables:
      - name: "Table 9a: Simpson's Paradox Full-Scale Validation"
        columns: [model, raw_rho, raw_p, partial_rho_depth, partial_p, pilot_partial_rho, pilot_partial_p, verdict]
        rows:
          - [Qwen3-235B, -0.28, 0.001, +0.11, 0.31, "+0.18 (n.s.)", 0.274, "n.s. → no Simpson's Paradox"]
          - [Llama4-Scout, -0.35, "<0.001", +0.08, 0.42, "+0.41 (sig.)", 0.006, "pilot artifact confirmed"]
      - name: "Table 9b: Same-Layer Cross-Language CKA-Transfer Correlation (top 5 layers)"
        columns: [model, layer, layer_pct, cka_transfer_rho, p_value, n_langs]
        rows:
          - [Qwen3, 36, "38%", 0.22, 0.35, 20]
          - [Qwen3, 48, "51%", 0.31, 0.18, 20]
          - [Qwen3, 56, "60%", 0.18, 0.45, 20]
          - [Qwen3, 64, "68%", 0.42, 0.065, 20]
          - [Qwen3, 72, "77%", 0.38, 0.098, 20]
          - [Llama4, 16, "33%", 0.12, 0.61, 20]
          - [Llama4, 24, "50%", 0.08, 0.74, 20]
          - [Llama4, 32, "67%", 0.25, 0.29, 20]
          - [Llama4, 40, "83%", 0.15, 0.53, 20]
          - [Llama4, 44, "92%", 0.05, 0.83, 20]
      - name: "Table 9c: Subspace Angle Analysis (Correctness Direction, EN vs Target)"
        columns: [lang, tier, qwen3_angle_deg_L56, llama4_angle_deg_L32, note]
        rows:
          - [zh, HIGH, 18, 22, "relatively aligned"]
          - [es, HIGH, 15, 19, "relatively aligned"]
          - [fr, HIGH, 20, 25, ""]
          - [de, HIGH, 22, 28, ""]
          - [ja, HIGH, 35, 41, "large angle despite HIGH resource"]
          - [ar, MID, 32, 38, ""]
          - [hi, MID, 38, 45, ""]
          - [ko, MID, 28, 35, ""]
          - [tr, MID, 42, 48, ""]
          - [sw, LOW, 52, 58, "near orthogonal"]
          - [bn, LOW, 48, 55, ""]
          - [am, LOW, 62, 65, "correctness direction nearly unrelated"]
    figures_description:
      - "Figure 6a: CKA heatmap (language × layer) for both models. Shows CKA decline with depth but no clear correspondence to transfer AUROC patterns."
      - "Figure 6b: Scatter plot of partial residuals (CKA residualized on depth vs transfer AUROC residualized on depth) for both models. Diffuse cloud with no visible trend. Annotations show partial rho and p-values."
      - "Figure 6c: Subspace angle distribution (violin plot by resource tier). Clear tier gradient but HIGH tier also shows 15-35° range, undermining 'language-agnostic subspace' claim."
    analysis: >
      CKA analysis 的全面失败是 worst tier 的 defining feature。Pilot 的 Simpson's Paradox
      从 Llama rho=+0.41 (p=0.006) 崩溃到 rho=+0.08 (p=0.42)——这是教科书式的 small-sample inflation。
      5 语言 pilot 恰好 overrepresented CKA-transfer 关系最强的语言（zh, ar），排除了关系最弱的语言。
      Subspace angle analysis 进一步否定了"correctness direction is a robust low-dimensional
      language-agnostic subspace"的前提假设：即使 HIGH resource 语言的 angle 也有 15-35° 的 spread，
      LOW resource 达到 48-65°（近乎不相关）。这意味着 Miao & Ungar (2026) 的 EN-only correctness direction
      在跨语言场景下不是 language-agnostic 的——这本身是一个重要的 negative finding，值得在 paper 中强调。
      CKA 框架从 geometric analysis 降级为 descriptive visualization（仅展示 CKA 随 depth 的下降趋势），
      不再承载解释性角色。

  - name: "Linear Projection Sensitivity Analysis"
    plan_id: "plan_012"
    description: "Procrustes alignment with 10/20/50/100/200 parallel pairs, 2 models × 5 layers × 20 langs"
    expected_results:
      pairs_to_95pct_mean: 142
      pairs_to_95pct_range: [85, 198]
      pairs_to_95pct_high_tier: 68
      pairs_to_95pct_mid_tier: 125
      pairs_to_95pct_low_tier: 182
      saturation_curve_r2: 0.82
      pair_10_mean_auroc: 0.548
      pair_20_mean_auroc: 0.568
      pair_50_mean_auroc: 0.588
      pair_100_mean_auroc: 0.601
      pair_200_mean_auroc: 0.610
      procrustes_reversal_threshold: "inconsistent — varies by language"
      helps_when_zs_below: "ranges from 0.48 to 0.58 across languages"
      hurts_when_zs_above: "ranges from 0.55 to 0.68 across languages"
      reversal_overlap_zone: [0.48, 0.68]
    result_rationale: >
      Worst tier 下 linear projection 需要 100-200 pairs（非 50）达到 95% 性能：
      (1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需要更多数据点来
      稳定估计 rotation matrix——50 pairs 在高维空间中 rank-deficient，低资源语言的 parallel pairs
      质量更差（翻译质量低→activation 噪声→需要更多 pairs 来 average out noise）。
      (2) Resource-tier 分层仍然存在（HIGH 68 pairs vs LOW 182 pairs）但 tier 内方差大——
      同一 tier 内语言间差异可达 2-3×（如 zh 需 45 pairs 但 ja 需 95 pairs，都是 HIGH）。
      (3) Procrustes 效果反转的阈值高度 language-specific：帮助的 ZS AUROC 范围和伤害的范围
      有 [0.48, 0.68] 的 overlap zone，意味着对同一 ZS AUROC 值，不同语言可能被帮助或伤害。
      无法给出单一可操作的阈值——这使得"practitioners should use linear projection when ZS < X"
      的建议变得不可靠。
    tables:
      - name: "Table 10a: Linear Projection Sample Efficiency (mean across 2 models × 20 langs)"
        columns: [n_pairs, mean_auroc, pct_of_200pair, std_across_langs, significant_improvement_pct]
        rows:
          - [10, 0.548, "68%", 0.065, "25%"]
          - [20, 0.568, "79%", 0.058, "40%"]
          - [50, 0.588, "89%", 0.052, "55%"]
          - [100, 0.601, "95%", 0.048, "65%"]
          - [200, 0.610, "100%", 0.045, "72%"]
      - name: "Table 10b: Pairs to 95% Performance by Resource Tier"
        columns: [tier, mean_pairs_95pct, min, max, std]
        rows:
          - [HIGH, 68, 42, 98, 22]
          - [MID, 125, 78, 165, 35]
          - [LOW, 182, 145, 198, 28]
      - name: "Table 10c: Procrustes Effect Reversal — Inconsistent Thresholds"
        columns: [lang, tier, zs_auroc, linproj_200_auroc, delta, effect]
        rows:
          - [am, LOW, 0.475, 0.498, +0.023, "helps"]
          - [yo, LOW, 0.463, 0.490, +0.027, "helps"]
          - [sw, LOW, 0.504, 0.518, +0.014, "helps"]
          - [bn, LOW, 0.512, 0.528, +0.016, "helps"]
          - [tr, MID, 0.532, 0.548, +0.016, "helps"]
          - [hi, MID, 0.552, 0.561, +0.009, "helps (marginal)"]
          - [vi, MID, 0.558, 0.558, +0.000, "neutral"]
          - [ko, MID, 0.578, 0.575, -0.003, "neutral/hurts"]
          - [ar, MID, 0.603, 0.598, -0.005, "hurts"]
          - [ru, MID, 0.624, 0.612, -0.012, "hurts"]
          - [zh, HIGH, 0.658, 0.641, -0.017, "hurts"]
          - [es, HIGH, 0.670, 0.650, -0.020, "hurts"]
          - [ja, HIGH, 0.582, 0.590, +0.008, "helps (despite HIGH tier)"]
    figures_description:
      - "Figure 7a: Saturation curves (n_pairs vs AUROC) faceted by resource tier, with 95% threshold marked. HIGH saturates early, LOW saturates late. Per-language thin lines show within-tier variance."
      - "Figure 7b: Scatter plot of ZS AUROC (x) vs linear projection ΔAUROC (y). Shows rough negative trend but wide scatter band. Vertical zone [0.48-0.68] highlighted as 'inconsistent reversal zone' where both positive and negative deltas occur."
    analysis: >
      Linear projection 仍是唯一可行方案但实用性大打折扣：(1) 需 100+ pairs 而非 50，
      对低资源语言来说 parallel data 本身就是稀缺资源；(2) 效果反转阈值 inconsistent，
      practitioner 无法事先知道某语言是否会被帮助或伤害。Paper 中只能给出条件性 recommendation：
      "当 ZS AUROC < 0.50 时大概率有益，> 0.65 时大概率有害，0.50-0.65 区间需要 held-out validation"
      ——这比预期的 clean threshold (0.50/0.60) 弱得多。

  - name: "Probing Control Tasks (Cross-Lingual Extension)"
    plan_id: "plan_013"
    description: "Hewitt & Liang control tasks for 20 languages × all probed layers × 2 models, selectivity analysis"
    expected_results:
      control_artifact_rate_low_resource: 0.42
      control_artifact_rate_mid_resource: 0.37
      control_artifact_rate_high_resource: 0.18
      control_artifact_rate_overall: 0.31
      selectivity_below_0.05_pct_low: "42%"
      selectivity_below_0.05_pct_mid: "37%"
      selectivity_below_0.05_pct_high: "18%"
      mean_selectivity_en: 0.245
      mean_selectivity_high: 0.198
      mean_selectivity_mid: 0.142
      mean_selectivity_low: 0.085
      selectivity_vs_zs_auroc_rho: 0.68
      layers_most_affected: "shallow layers (0-30% depth)"
      worst_lang_layer_combos: ["am-L0", "yo-L4", "my-L0", "am-L4", "yo-L0", "te-L8"]
    result_rationale: >
      这是 worst tier 的最强贡献。Control task artifact rate 在低资源语言达 42%，中资源 37%，
      远超 MVP pilot 的 28%。原因：(1) MVP 的 5 语言中低资源仅 sw 一种，现在 6-7 种低资源语言
      暴露了更系统性的问题——am, yo, my 等在 LLM 预训练中极度不足，对应的 representation
      缺乏区分性结构，probe 学到的主要是 capacity artifacts 而非 correctness signals。
      (2) 中资源语言出现 37% artifact rate 是 worst tier 的 signature finding：
      这不仅仅是"低资源语言有问题"——tr, th, vi 等中资源语言在浅层也有大量 artifacts，
      说明 probing methodology 在 cross-lingual 场景的可靠性比预期差得多。
      (3) Selectivity 与 ZS AUROC 高度相关（rho=0.68），暗示许多看似成功的 cross-lingual transfer
      结果其实是 capacity artifacts 在目标语言中的 shadow。
      这对整个跨语言 probing 文献有 field-level implication：任何不包含 control task 检验的
      跨语言 probing 研究的结论都值得质疑。这是首次在 cross-lingual transfer 场景系统性
      应用 selectivity 检验——贡献的 novelty 和 impact 在 worst tier 下反而最强。
    tables:
      - name: "Table 11a: Control Task Artifact Rate by Resource Tier and Model"
        columns: [tier, n_langs, qwen3_artifact_rate, llama4_artifact_rate, combined, selectivity_mean]
        rows:
          - [HIGH, 7, "16%", "20%", "18%", 0.198]
          - [MID, 7, "35%", "39%", "37%", 0.142]
          - [LOW, 6, "40%", "44%", "42%", 0.085]
          - [ALL, 20, "29%", "33%", "31%", 0.145]
      - name: "Table 11b: Per-Language Selectivity at EN-Optimal Layer"
        columns: [lang, tier, real_auroc, permuted_auroc, selectivity, artifact_flag]
        rows:
          - [en, "—", 0.738, 0.490, 0.248, ""]
          - [zh, HIGH, 0.672, 0.498, 0.174, ""]
          - [es, HIGH, 0.681, 0.495, 0.186, ""]
          - [fr, HIGH, 0.663, 0.492, 0.171, ""]
          - [de, HIGH, 0.654, 0.488, 0.166, ""]
          - [ja, HIGH, 0.582, 0.502, 0.080, ""]
          - [pt, HIGH, 0.668, 0.491, 0.177, ""]
          - [it, HIGH, 0.651, 0.494, 0.157, ""]
          - [ar, MID, 0.603, 0.498, 0.105, ""]
          - [hi, MID, 0.561, 0.505, 0.056, "⚠"]
          - [ru, MID, 0.624, 0.495, 0.129, ""]
          - [ko, MID, 0.585, 0.501, 0.084, ""]
          - [tr, MID, 0.541, 0.508, 0.033, "⚠"]
          - [vi, MID, 0.558, 0.512, 0.046, "⚠"]
          - [th, MID, 0.523, 0.498, 0.025, "⚠"]
          - [sw, LOW, 0.512, 0.505, 0.007, "⚠⚠"]
          - [bn, LOW, 0.519, 0.502, 0.017, "⚠⚠"]
          - [am, LOW, 0.482, 0.478, 0.004, "⚠⚠"]
          - [yo, LOW, 0.471, 0.465, 0.006, "⚠⚠"]
          - [te, LOW, 0.498, 0.488, 0.010, "⚠⚠"]
          - [my, LOW, 0.463, 0.458, 0.005, "⚠⚠"]
      - name: "Table 11c: Layers with Artifact Rate > 40%"
        columns: [model, layer_range, high_artifact_pct, mid_artifact_pct, low_artifact_pct]
        rows:
          - [Qwen3, "L0-L20 (0-21%)", "8%", "48%", "65%"]
          - [Qwen3, "L24-L48 (26-51%)", "12%", "35%", "52%"]
          - [Qwen3, "L52-L72 (55-77%)", "18%", "28%", "35%"]
          - [Qwen3, "L76-L92 (81-98%)", "25%", "32%", "38%"]
          - [Llama4, "L0-L12 (0-25%)", "12%", "52%", "68%"]
          - [Llama4, "L16-L28 (33-58%)", "18%", "38%", "48%"]
          - [Llama4, "L32-L44 (67-92%)", "22%", "30%", "35%"]
          - [Llama4, "L48 (100%)", "28%", "35%", "40%"]
    figures_description:
      - "Figure 8a: Heatmap of selectivity (language × layer) for Qwen3-235B. Color scale: red (< 0.05 artifact) to green (> 0.20 genuine). Large red region in bottom-left (low-resource × shallow layers). Mid-resource languages show surprising red patches even at moderate depths."
      - "Figure 8b: Bar chart of artifact rate by resource tier with 95% CI. Error bars computed via bootstrap over languages within each tier. The CI for MID tier overlaps substantially with LOW tier — the artifact problem is not confined to low-resource."
      - "Figure 8c: Scatter plot of selectivity vs ZS AUROC across all language-layer-model combinations. Strong positive correlation (rho=0.68) suggests many 'successful' ZS transfer results are artifacts."
    analysis: >
      Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact rate
      波及中资源语言是 field-level 发现：不是"低资源语言有问题，审稿人可以忽略"，而是
      "所有跨语言 probing 研究——包括那些只看中/高资源语言的——都需要 selectivity 检验"。
      Selectivity 与 ZS AUROC 的高相关性 (rho=0.68) 尤其尖锐：它暗示 cross-lingual probing
      文献中的许多 positive results 可能是 capacity artifacts。这个 finding 独立于
      本文的其他所有 claims——即使 Pareto, CaCLR, decomposition 全部失败，这个方法论贡献
      仍然足以支撑一篇 findings paper。首次在 cross-lingual transfer 场景应用 Hewitt & Liang
      selectivity 框架，发现 artifact 问题远比 monolingual probing 严重——这是 reframe 后
      paper 叙事的 structural foundation。

  - name: "Gemma 4 31B Dense Pareto Frontier"
    plan_id: "plan_008"
    description: "Gemma 4 31B Dense (60 layers, FP16), 15 probed layers, 20 langs, camera-ready 第三架构"
    expected_results:
      en_best_auroc: 0.742
      en_best_layer: 48
      zs_pass_rate: 0.60
      global_spearman_rho: -0.22
      global_spearman_p: 0.045
      per_lang_significant_count: 4
      dense_vs_moe_pareto_clarity: "moderately clearer but still noisy"
      control_artifact_rate_low: 0.38
    result_rationale: >
      Dense 架构避免了 MoE routing 的 non-monotonic 噪声，global rho marginally significant
      (p=0.045)——pareto_spearman_rho_significant_archs 从 0 变为 1。但这反而增加了叙述复杂性：
      Pareto 是 architecture-dependent 的，dense 模型有 moderate tradeoff，MoE 没有。
      无法声称 depth-transfer tradeoff 是普遍现象。EN AUROC 0.742 在 worst 范围内。
      Control artifact rate 对低资源语言 38%，确认这不是 MoE-specific 的问题。
      作为 camera-ready 扩展，Gemma 增加了 architecture coverage 但不改变核心叙事。
    tables:
      - name: "Table S1: Gemma 4 31B Dense Pareto Summary"
        columns: [metric, value]
        rows:
          - [en_best_auroc, 0.742]
          - [zs_pass_rate, "60% (12/20)"]
          - [global_pareto_rho, "-0.22 (p=0.045)"]
          - [per_lang_significant_rho, "4/20"]
          - [control_artifact_rate_low, "38%"]
          - [simpson_partial_rho, "+0.14 (p=0.22)"]
    figures_description:
      - "Figure S4 (camera-ready): Gemma 4 Pareto scatter showing cleaner but still noisy frontier vs Qwen3/Llama4."
    analysis: >
      Gemma dense 提供了 MoE vs dense 的对比：dense 架构的 Pareto 更清晰但仍远非 universal。
      4/20 语言 per-language significance 比 Qwen3 的 2/20 好但仍是少数。
      Simpson's Paradox 在 Gemma 上也不显著 (partial rho=+0.14, p=0.22)。
      三架构综合：0-1 个有 significant Pareto，0 个有 significant Simpson's Paradox——
      worst tier 叙事的 architecture coverage 从 2 扩展到 3 但结论不变。

  - name: "Extended Language Coverage (50+ Languages)"
    plan_id: "plan_009"
    description: "从 20 扩展到 50+ 语言, camera-ready extension"
    expected_results:
      total_languages: 52
      zs_pass_rate_52lang: 0.52
      control_artifact_rate_low_expanded: 0.45
      new_langs_with_significant_pareto: 1
      additional_artifact_langs: 15
      linear_proj_pairs_to_95pct_expanded_mean: 158
    result_rationale: >
      扩展到 50+ 语言后，新增的大部分是 MID/LOW resource 语言。ZS pass rate 从 60% (20 langs)
      降至 52% (52 langs) 因为新增语言 skew toward lower resource。Control artifact rate
      在扩展后的低资源组升至 45%——更多极低资源语言被纳入。这进一步强化了 control task finding
      的 field-level 意义：近半数低资源跨语言 probing 结果是 artifacts。
      但扩展语言数不改变核心 negative results——主要增加 statistical power 和 coverage。
      Linear projection 需要的 pairs 数在扩展后 mean 升至 158 因为更多 hard languages。
    tables:
      - name: "Table S2: 52-Language Summary vs 20-Language Core"
        columns: [metric, 20_lang, 52_lang, delta]
        rows:
          - [zs_pass_rate, "60%", "52%", "-8pp"]
          - [control_artifact_low, "42%", "45%", "+3pp"]
          - [control_artifact_mid, "37%", "39%", "+2pp"]
          - [linear_proj_mean_pairs, 142, 158, "+16"]
          - [simpson_partial_rho_max, 0.11, 0.09, "-0.02"]
    figures_description:
      - "Figure S5 (camera-ready): World map of ZS AUROC at EN-optimal layer with artifact-flagged languages marked. Large regions (Sub-Saharan Africa, Southeast Asia) dominated by artifact flags."
    analysis: >
      52 语言扩展主要服务于 coverage 和 robustness 声称。
      核心结论不变但 control task finding 更加 impactful：近半数低资源结果是 artifacts
      在 50+ 语言规模下是对跨语言 probing 文献的强警告。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "909d6c52-c434-495e-a49e-8c7be061358c",
  "isSidechain": false,
  "requestId": "req_011CbF9nFjkFVPnxRMpqrYm7",
  "type": "assistant",
  "uuid": "1ecf7299-4350-45f3-a7e2-201ce23da184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZjkMHzufEhpXk4saBe21E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17917,
      "cache_read_input_tokens": 11447,
      "output_tokens": 26129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 26129,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17917
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Simpson's Paradox 在 20 语言上双架构均不显著；CaCLR 失败且几何解释不成立；Pareto frontier 噪声大；高 artifact rate 动摇 probe 有效性 核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均不显…",
  "leafUuid": "1ecf7299-4350-45f3-a7e2-201ce23da184",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe transfer: large-scale negative results and methodological implications",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Simpson's Paradox 在 20 语言上双架构均不显著；CaCLR 失败且几何解释不成立；Pareto frontier 噪声大；高 artifact rate 动摇 probe 有效性 核心假设：[\"Simpson's Paradox partial correlation 在两个架构上均不显…",
  "leafUuid": "1ecf7299-4350-45f3-a7e2-201ce23da184",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual correctness probe transfer: large-scale negative results and methodological implications",
  "sessionId": "e5d1facc-1d4d-4d1e-97c6-e5eaeb7bab55"
}
```

---
